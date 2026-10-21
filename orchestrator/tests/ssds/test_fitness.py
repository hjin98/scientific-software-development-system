"""Manual §26.2 executable architecture fitness, and the shadow-boundary sensor.

The real repository must show no violation. Each discriminator builds a small
synthetic repository that is clean except for one change, and states by hand,
from the Manual's rule, the violations that change must produce; a checker that
accepted the change, or blamed a different rule or file, fails.
"""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from .fitness import COMPONENTS, check

REPO_ROOT = Path(__file__).resolve().parents[3]
PROGRAM_PACKAGE = REPO_ROOT / "orchestrator/src/ssds"
MODEL_STEMS = frozenset({"cases_s5_1", "framework"})

S = "orchestrator/src/ssds"
C = "orchestrator/src/ssds/core"
PYPROJECT = "orchestrator/pyproject.toml"

#: A clean minimal repository: the program package with Core, the components and the root module.
CLEAN: dict[str, str] = {
    PYPROJECT: (
        '[project]\nname = "ssds"\ndependencies = ["typer>=0.12", "python-frontmatter>=1.1"]\n'
        '[project.scripts]\nssds = "ssds.cli:main"\n'
    ),
    f"{S}/__init__.py": 'VERSION = "8.0.0"\n',
    f"{S}/cli.py": (
        "import typer\n"
        "from ssds.core import cli as core_cli\n"
        "from ssds.core.api.v1 import Problem\n"
        "def main():\n    return core_cli.main(typer.Typer())\n"
    ),
    f"{C}/__init__.py": "",
    f"{C}/records.py": "",
    f"{C}/cli.py": "import typer\nfrom .records import *\n",
    f"{C}/application.py": 'ENTRY_POINT_GROUP = "ssds.extensions.v1"\nSTATUS = "ssds.core.discovery"\n',
    f"{C}/api/__init__.py": "",
    f"{C}/api/v1.py": "from ..records import *\n",
    f"{C}/spi/__init__.py": "",
    f"{C}/spi/v1.py": "from ..records import *\n",
    f"{S}/api/__init__.py": "",
    f"{S}/api/v1.py": "from ssds.derivation import *\n",
    f"{S}/spi/__init__.py": "",
    f"{S}/spi/v1.py": "",
    f"{S}/ledger/read.py": "import subprocess\nsubprocess.run(['git', 'cat-file', '--batch'])\n",
    f"{S}/ledger/qualification.py": "",
    f"{S}/ledger/append.py": "import subprocess\nsubprocess.run(['git', 'update-ref', 'refs/ssds/ledger/x'])\n",
    f"{S}/admission/request.py": "",
    f"{S}/admission/genesis.py": (
        "from ssds.ledger import append, qualification\n"
        "from ssds import derivation\n"
        "from ssds.core.api.v1 import DigestRef\n"
    ),
    f"{S}/interface/render.py": "",
    f"{S}/content/model.py": "import frontmatter\nTEXT = b''.decode('utf-8', 'replace')\nKIND = 'commit'\n",
    f"{S}/derivation/strata.py": (
        "from __future__ import annotations\n"
        "import hashlib, json\n"
        "from collections import abc\n"
        "from ..ledger import read\n"
        "from ssds import content, analyzers\n"
    ),
    "orchestrator/tests/__init__.py": "",
    "orchestrator/tests/ssds/__init__.py": "",
    "orchestrator/tests/ssds/test_example.py": '"""Expected values from qualification/ssds80/models/cases_s5_1.py."""\nimport unittest\n',
    **{f"{S}/{component}/__init__.py": "" for component in COMPONENTS},
}


def _git_files() -> list[str]:
    result = subprocess.run(  # noqa: S603
        ["git", "-C", str(REPO_ROOT), "ls-files", "--cached", "--others", "--exclude-standard"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in result.stdout.splitlines() if line]


def _run(changes: dict[str, str | None]) -> set[tuple[str, str]]:
    files = {**CLEAN, **changes}
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for relative, text in files.items():
            if text is None:
                continue
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        listed = sorted(relative for relative, text in files.items() if text is not None)
        return {(v.code, v.path) for v in check(root, listed, MODEL_STEMS)}


class RealRepositoryTests(unittest.TestCase):
    def test_repository_has_no_fitness_violation(self) -> None:
        stems = frozenset(
            path.stem for path in (REPO_ROOT / "qualification/ssds80/models").glob("*.py")
        )
        violations = check(REPO_ROOT, _git_files(), stems)
        self.assertEqual(violations, [], "\n".join(map(str, violations)))

    def test_every_component_package_exists_so_the_rules_are_not_vacuous(self) -> None:
        for component in (*COMPONENTS, "api", "spi", "core"):
            self.assertTrue((PROGRAM_PACKAGE / component / "__init__.py").is_file(), component)
        self.assertTrue((PROGRAM_PACKAGE / "cli.py").is_file())
        self.assertTrue((PROGRAM_PACKAGE / "__init__.py").is_file(), "one regular package (A7)")
        self.assertGreater(len(list((PROGRAM_PACKAGE / "core").rglob("*.py"))), 10)


class CleanSyntheticRepositoryTests(unittest.TestCase):
    def test_the_clean_fixture_is_clean(self) -> None:
        """Positive control: every allowed edge of the fixture is accepted."""

        self.assertEqual(_run({}), set())


class _Discriminator(unittest.TestCase):
    def assertViolations(self, changes: dict[str, str | None], expected: set[tuple[str, str]]) -> None:
        self.assertEqual(_run(changes), expected)


class DependencyRuleDiscriminatorTests(_Discriminator):
    """One broken rule per synthetic repository; the expected violations are stated from §26.2."""

    def test_content_may_not_import_the_ledger(self) -> None:
        path = f"{S}/content/model.py"
        self.assertViolations({path: "from ssds.ledger import read\n"}, {("F1", path)})

    def test_analyzers_may_import_only_core_public_api(self) -> None:
        path = f"{S}/analyzers/python.py"
        self.assertViolations({path: "from ssds.core import records\n"}, {("F11", path)})
        self.assertViolations({path: "from ssds.core import cli\n"}, {("F11", path)})

    def test_derivation_may_not_import_ledger_qualification(self) -> None:
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "from ..ledger import qualification\n"}, {("F2", path)})
        # A declared public module is recognized before its file exists.
        self.assertViolations(
            {path: "from ..ledger import qualification\n", f"{S}/ledger/qualification.py": None}, {("F2", path)}
        )

    def test_derivation_may_not_import_core(self) -> None:
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "from ssds.core.api.v1 import DigestRef\n"}, {("F2", path)})

    def test_an_import_under_type_checking_still_counts(self) -> None:
        path = f"{S}/derivation/view.py"
        text = "from typing import TYPE_CHECKING\nif TYPE_CHECKING:\n    from ssds.admission import request\n"
        self.assertViolations({path: text}, {("F2", path)})

    def test_only_admission_imports_the_append_api(self) -> None:
        for owner in ("interface", "dispatcher", "derivation", "api"):
            path = f"{S}/{owner}/x.py"
            with self.subTest(owner=owner):
                self.assertViolations({path: "import ssds.ledger.append as append\n"}, {("F3", path)})
        path = f"{S}/cli.py"
        self.assertViolations({path: "from ssds.ledger import append\n"}, {("F3", path)})

    def test_the_ledger_package_does_not_re_export_append(self) -> None:
        path = f"{S}/ledger/__init__.py"
        self.assertViolations({path: "from . import append\n"}, {("F3", path)})

    def test_the_ledger_imports_no_other_component(self) -> None:
        path = f"{S}/ledger/store.py"
        self.assertViolations({path: "from ssds import derivation\n"}, {("F3", path)})

    def test_admission_never_imports_dispatcher_or_interface(self) -> None:
        path = f"{S}/admission/validate.py"
        self.assertViolations({path: "from ssds import dispatcher\n"}, {("F4", path)})
        self.assertViolations({path: "from ssds.interface import render\n"}, {("F4", path)})

    def test_dispatcher_uses_only_the_admission_request_api(self) -> None:
        path = f"{S}/dispatcher/schedule.py"
        self.assertViolations({path: "from ssds.admission import request\n"}, set())
        self.assertViolations({path: "import ssds.admission\n"}, {("F11", path)})
        self.assertViolations({path: "from ssds.admission import genesis\n"}, {("F11", path)})

    def test_dispatcher_reads_only_ledger_qualification(self) -> None:
        path = f"{S}/dispatcher/schedule.py"
        self.assertViolations({path: "from ssds.ledger import read\n"}, {("F5", path)})

    def test_interface_never_imports_the_dispatcher(self) -> None:
        path = f"{S}/interface/render.py"
        self.assertViolations({path: "from ssds import dispatcher\n"}, {("F6", path)})

    def test_core_imports_no_component_and_not_the_root_module(self) -> None:
        path = f"{C}/application.py"
        self.assertViolations({path: "import ssds.derivation\n"}, {("F7", path)})
        self.assertViolations({path: "from ssds import cli\n"}, {("F7", path)})
        self.assertViolations({path: "from .. import ledger\n"}, {("F7", path)})
        self.assertViolations({path: "NAME = 'ssds.ledger.append'\n"}, {("F7", path)})
        self.assertViolations({path: "NAME = 'ssds.cli'\n"}, {("F7", path)})

    def test_derivation_reads_no_clock_environment_network_or_process(self) -> None:
        path = f"{S}/derivation/view.py"
        for text in ("import time\n", "from os import environ\n", "import socket\n", "from datetime import datetime\n",
                     "import pathlib\n", "import random\n"):
            with self.subTest(text=text):
                self.assertViolations({path: text}, {("F8", path)})
        self.assertViolations({path: "import subprocess\n"}, {("F8", path), ("B1", path)})

    def test_derivation_performs_no_io_through_builtins(self) -> None:
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "def f(p):\n    return open(p).read()\n"}, {("F8", path)})

    def test_derivation_reaches_no_git_reader_through_a_permitted_facade(self) -> None:
        """Review 0e49deb N2: the content facade exposes read_tree; derivation must not use it."""

        path = f"{S}/derivation/view.py"
        for text in ("from ssds.content import read_tree\ndef f(r):\n    return read_tree(r, 'HEAD')\n",
                     "from ssds import content\ndef f(r):\n    return content.read_tree(r, 'HEAD')\n",
                     "from ..ledger.read import read_chain\n",
                     "import ssds.content\ndef f(r):\n    return ssds.content.read_tree(r, 'HEAD')\n",
                     "from ..ledger import read\ndef f(r):\n    return read.read_chain(r, 'demo')\n",
                     "import ssds.content as c\ndef f(r):\n    return c.read_tree(r, 'HEAD')\n"
                     "def g():\n    import collections as c\n    return c.Counter()\n"):
            with self.subTest(text=text):
                self.assertViolations({path: text}, {("F8", path)})
        pure = ("from dataclasses import dataclass\n@dataclass\nclass Snapshot:\n    read_raw: bytes\n"
                "def f(snapshot):\n    return snapshot.read_raw\n")
        self.assertViolations({path: pure}, set())  # Review 517af45 NF1: an unrelated attribute of that name is pure
        unrelated = ("def f():\n    import ssds.content as c\n    return c.TreeView\n"
                     "def g(c):\n    return c.read_raw\n")
        self.assertViolations({path: unrelated}, set())  # Review d8bdfd3 NF6: another scope's binding
        aliased = "import ssds.content as c\nreader = c\nvalue = reader.read_tree\n"
        self.assertViolations({path: aliased}, {("F8", path)})  # d8bdfd3 NF6: an assignment alias
        before_rebinding = "import ssds.content as c\nx = c.read_tree\nc = None\n"
        self.assertViolations({path: before_rebinding}, {("F8", path)})  # b341109 NF7: binding order
        annotated = ("import ssds.content as c\nclass Snapshot:\n    read_raw: bytes\n"
                     "def f(snapshot):\n    c: Snapshot = snapshot\n    return c.read_raw\n")
        self.assertViolations({path: annotated}, set())  # b341109 NF7: an annotated local shadows
        class_local = ("class K:\n    import ssds.content as c\n    def m(self):\n        return c.read_raw\n"
                       "c = object()\n")
        self.assertViolations({path: class_local}, set())  # b341109 NF7: methods do not see the class body

    def test_derivation_imports_no_third_party_module(self) -> None:
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "import typer\n"}, {("F8", path)})
        self.assertViolations({path: "import yaml\n"}, {("F12", path)})

    def test_program_source_lives_under_orchestrator_src_ssds(self) -> None:
        for stray in ("src/ssds/x.py", "orchestrator/ssds/x.py", "tools/ssds/x.py"):
            with self.subTest(stray=stray):
                self.assertViolations({stray: ""}, {("F9", stray)})

    def test_one_program_distribution(self) -> None:
        path = "tools/pyproject.toml"
        self.assertViolations({path: '[project]\nname = "ssds"\n'}, {("F9", PYPROJECT)})

    def test_one_composition_root(self) -> None:
        text = CLEAN[PYPROJECT] + 'ssds-admin = "ssds.admission.genesis:main"\n'
        self.assertViolations({PYPROJECT: text}, {("F10", PYPROJECT)})
        other = "tools/pyproject.toml"
        self.assertViolations(
            {other: '[project]\nname = "x"\n[project.scripts]\nssds = "x:main"\n'}, {("F10", other)}
        )
        path = f"{S}/admission/genesis.py"
        self.assertViolations({path: "if __name__ == '__main__':\n    pass\n"}, {("F10", path)})
        main = f"{S}/__main__.py"
        self.assertViolations({main: ""}, {("F0", main)})
        core_main = f"{C}/__main__.py"
        self.assertViolations({core_main: ""}, {("F10", core_main)})

    def test_the_program_is_not_an_extension_of_itself(self) -> None:
        text = CLEAN[PYPROJECT] + '[project.entry-points."ssds.extensions.v1"]\nx = "ssds.cli:main"\n'
        self.assertViolations({PYPROJECT: text}, {("F10", PYPROJECT)})

    def test_no_private_cross_module_import(self) -> None:
        path = f"{S}/content/model.py"
        self.assertViolations({path: "from ssds.analyzers import _helper\n"}, {("F11", path)})
        self.assertViolations({path: "from ssds.analyzers.python import imports\n"}, {("F11", path)})

    def test_no_dynamic_import_or_code_execution(self) -> None:
        path = f"{S}/content/model.py"
        self.assertViolations({path: "import importlib\n"}, {("F11", path)})
        self.assertViolations({path: "m = __import__('ssds.ledger.append')\n"}, {("F11", path)})
        self.assertViolations({path: "exec('x = 1')\n"}, {("F11", path)})

    def test_no_component_imports_the_facades_or_the_root_module(self) -> None:
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "from ssds.api import v1\n"}, {("F12", path)})
        path = f"{S}/admission/x.py"
        self.assertViolations({path: "from ssds import cli\n"}, {("F12", path)})

    def test_the_top_package_imports_nothing(self) -> None:
        path = f"{S}/__init__.py"
        self.assertViolations({path: "from . import derivation\n"}, {("F12", path)})

    def test_only_declared_dependencies(self) -> None:
        path = f"{S}/content/model.py"
        self.assertViolations({path: "import yaml\n"}, {("F12", path)})

    def test_every_module_has_an_owner(self) -> None:
        path = f"{S}/util.py"
        self.assertViolations({path: ""}, {("F0", path)})

    def test_nothing_imports_or_loads_the_stage_s_models(self) -> None:
        test = "orchestrator/tests/ssds/test_example.py"
        self.assertViolations({test: "from qualification.ssds80.models import cases_s5_1\n"}, {("F13", test)})
        self.assertViolations({test: "import cases_s5_1\n"}, {("F13", test)})
        self.assertViolations(
            {test: "import sys\nsys.path.insert(0, 'qualification/ssds80/models')\n"}, {("F13", test)}
        )
        core_test = "orchestrator/tests/test_core_example.py"
        self.assertViolations({core_test: "import framework\n"}, {("F13", core_test)})
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "import framework\n"}, {("F13", path)})


class ShadowBoundarySensorTests(_Discriminator):
    """G2 workplan §5.1 item 2: only the ledger append moves a ref or writes Git objects."""

    def test_writing_git_subcommands_appear_only_in_the_append(self) -> None:
        path = f"{S}/ledger/read.py"
        self.assertViolations({path: "ARGS = ['git', 'push']\n"}, {("B1", path)})
        path = f"{S}/content/git.py"
        self.assertViolations({path: "ARGS = ['git', 'update-ref']\n"}, {("B1", path)})
        self.assertViolations({path: "ARGS = ['git', '-C', 'repo', 'push']\n"}, {("B1", path)})
        self.assertViolations({path: "run(repo, ['hash-object', '-w'])\n"}, {("B1", path)})
        self.assertViolations({path: "run(repo, ['cat-file', '--batch'])\n"}, set())

    def test_only_content_and_ledger_start_processes(self) -> None:
        path = f"{S}/admission/genesis.py"
        self.assertViolations({path: "import subprocess\n"}, {("B1", path)})
        self.assertViolations({path: "import os\nos.system('git push')\n"}, {("B1", path)})


if __name__ == "__main__":
    unittest.main()
