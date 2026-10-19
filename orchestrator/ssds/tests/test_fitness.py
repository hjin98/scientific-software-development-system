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

from .fitness import COMPONENTS, Violation, check

REPO_ROOT = Path(__file__).resolve().parents[3]
SSDS_PACKAGE = REPO_ROOT / "orchestrator/ssds/src/sdp_orchestrator/ssds"
MODEL_STEMS = frozenset({"cases_s5_1", "framework"})

S = "orchestrator/ssds/src/sdp_orchestrator/ssds"
C = "orchestrator/src/sdp_orchestrator/core"

#: A clean minimal repository: the SSDS layout, a Core with its public surfaces, both pyprojects.
CLEAN: dict[str, str] = {
    "orchestrator/pyproject.toml": '[project]\nname = "sdp-orchestrator-core"\ndependencies = ["pydantic>=2"]\n',
    "orchestrator/ssds/pyproject.toml": (
        '[project]\nname = "sdp-orchestrator-ssds"\ndependencies = ["sdp-orchestrator-core"]\n'
        '[project.entry-points."sdp_orchestrator.extensions.v1"]\n'
        '"sdp.ssds" = "sdp_orchestrator.ssds.extension:provider"\n'
    ),
    f"{C}/__init__.py": "",
    f"{C}/records.py": "",
    f"{C}/api/__init__.py": "",
    f"{C}/api/v1.py": "from ..records import *\n",
    f"{C}/spi/__init__.py": "",
    f"{C}/spi/v1.py": "from ..records import *\n",
    f"{S}/__init__.py": 'VERSION = "8.0.0"\n',
    f"{S}/api/__init__.py": "",
    f"{S}/api/v1.py": "from sdp_orchestrator.ssds.derivation import *\n",
    f"{S}/spi/__init__.py": "",
    f"{S}/spi/v1.py": "",
    f"{S}/extension.py": "from sdp_orchestrator.core.spi.v1 import ExtensionManifest\nfrom . import VERSION\n",
    f"{S}/ledger/read.py": "import subprocess\nsubprocess.run(['git', 'cat-file', '--batch'])\n",
    f"{S}/ledger/qualification.py": "",
    f"{S}/ledger/append.py": "import subprocess\nsubprocess.run(['git', 'update-ref', 'refs/ssds/ledger/x'])\n",
    f"{S}/admission/request.py": "",
    f"{S}/admission/genesis.py": (
        "from sdp_orchestrator.ssds.ledger import append, qualification\n"
        "from sdp_orchestrator.ssds import derivation\n"
        "from sdp_orchestrator.core.api.v1 import DigestRef\n"
    ),
    f"{S}/interface/render.py": "",
    f"{S}/derivation/strata.py": (
        "from __future__ import annotations\n"
        "import hashlib, json\n"
        "from collections import abc\n"
        "from ..ledger import read\n"
        "from sdp_orchestrator.ssds import content, analyzers\n"
    ),
    "orchestrator/ssds/tests/__init__.py": "",
    "orchestrator/ssds/tests/test_example.py": '"""Expected values from qualification/ssds80/models/cases_s5_1.py."""\nimport unittest\n',
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
        for component in (*COMPONENTS, "api", "spi"):
            self.assertTrue((SSDS_PACKAGE / component / "__init__.py").is_file(), component)
        self.assertTrue((SSDS_PACKAGE / "extension.py").is_file())
        self.assertFalse((SSDS_PACKAGE.parent / "__init__.py").exists(), "PEP 420 namespace root")
        self.assertGreater(len(list((REPO_ROOT / "orchestrator/src/sdp_orchestrator/core").rglob("*.py"))), 10)


class CleanSyntheticRepositoryTests(unittest.TestCase):
    def test_the_clean_fixture_is_clean(self) -> None:
        """Positive control: every allowed edge of the fixture is accepted."""

        self.assertEqual(_run({}), set())


class DependencyRuleDiscriminatorTests(unittest.TestCase):
    """One broken rule per synthetic repository; the expected violations are stated from §26.2."""

    def assertViolations(self, changes: dict[str, str | None], expected: set[tuple[str, str]]) -> None:
        self.assertEqual(_run(changes), expected)

    def test_content_may_not_import_the_ledger(self) -> None:
        path = f"{S}/content/model.py"
        self.assertViolations({path: "from sdp_orchestrator.ssds.ledger import read\n"}, {("F1", path)})

    def test_analyzers_may_import_only_core_public_api(self) -> None:
        path = f"{S}/analyzers/python.py"
        self.assertViolations({path: "from sdp_orchestrator.core import records\n"}, {("F11", path)})

    def test_derivation_may_not_import_ledger_qualification(self) -> None:
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "from ..ledger import qualification\n"}, {("F2", path)})
        # A declared public module is recognized before its file exists.
        self.assertViolations(
            {path: "from ..ledger import qualification\n", f"{S}/ledger/qualification.py": None}, {("F2", path)}
        )

    def test_derivation_may_not_import_core(self) -> None:
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "from sdp_orchestrator.core.api.v1 import DigestRef\n"}, {("F2", path)})

    def test_an_import_under_type_checking_still_counts(self) -> None:
        path = f"{S}/derivation/view.py"
        text = "from typing import TYPE_CHECKING\nif TYPE_CHECKING:\n    from sdp_orchestrator.ssds.admission import request\n"
        self.assertViolations({path: text}, {("F2", path)})

    def test_only_admission_imports_the_append_api(self) -> None:
        for component in ("interface", "dispatcher", "derivation"):
            path = f"{S}/{component}/x.py"
            with self.subTest(component=component):
                self.assertViolations(
                    {path: "import sdp_orchestrator.ssds.ledger.append as append\n"}, {("F3", path)}
                )

    def test_the_ledger_package_does_not_re_export_append(self) -> None:
        path = f"{S}/ledger/__init__.py"
        self.assertViolations({path: "from . import append\n"}, {("F3", path)})

    def test_the_ledger_imports_no_other_component(self) -> None:
        path = f"{S}/ledger/store.py"
        self.assertViolations({path: "from sdp_orchestrator.ssds import derivation\n"}, {("F3", path)})

    def test_admission_never_imports_dispatcher_or_interface(self) -> None:
        path = f"{S}/admission/validate.py"
        self.assertViolations({path: "from sdp_orchestrator.ssds import dispatcher\n"}, {("F4", path)})
        self.assertViolations({path: "from sdp_orchestrator.ssds.interface import render\n"}, {("F4", path)})

    def test_dispatcher_uses_only_the_admission_request_api(self) -> None:
        path = f"{S}/dispatcher/schedule.py"
        self.assertViolations({path: "from sdp_orchestrator.ssds.admission import request\n"}, set())
        self.assertViolations({path: "import sdp_orchestrator.ssds.admission\n"}, {("F11", path)})
        self.assertViolations({path: "from sdp_orchestrator.ssds.admission import genesis\n"}, {("F11", path)})

    def test_dispatcher_reads_only_ledger_qualification(self) -> None:
        path = f"{S}/dispatcher/schedule.py"
        self.assertViolations({path: "from sdp_orchestrator.ssds.ledger import read\n"}, {("F5", path)})

    def test_interface_never_imports_the_dispatcher(self) -> None:
        path = f"{S}/interface/render.py"
        self.assertViolations({path: "from sdp_orchestrator.ssds import dispatcher\n"}, {("F6", path)})

    def test_core_imports_nothing_from_ssds(self) -> None:
        path = f"{C}/application.py"
        self.assertViolations({path: "import sdp_orchestrator.ssds.derivation\n"}, {("F7", path)})
        self.assertViolations({path: "NAME = 'sdp_orchestrator.ssds.extension'\n"}, {("F7", path)})

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

    def test_derivation_imports_no_third_party_module(self) -> None:
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "import sdp_orchestrator.core.api.v1\n"}, {("F2", path)})
        self.assertViolations({path: "import yaml\n"}, {("F12", path)})

    def test_ssds_files_live_under_orchestrator_ssds(self) -> None:
        for stray in ("src/sdp_orchestrator/ssds/x.py", "orchestrator/src/sdp_orchestrator/ssds/x.py"):
            with self.subTest(stray=stray):
                self.assertViolations({stray: ""}, {("F9", stray)})

    def test_the_ssds_distribution_is_declared_once_under_orchestrator_ssds(self) -> None:
        path = "tools/pyproject.toml"
        self.assertViolations({path: '[project]\nname = "sdp-orchestrator-ssds"\n'}, {("F9", path)})

    def test_one_extension_registration(self) -> None:
        second = "orchestrator/other/pyproject.toml"
        text = '[project]\nname = "x"\n[project.entry-points."sdp_orchestrator.extensions.v1"]\nx = "x:provider"\n'
        self.assertViolations({second: text}, {("F10", "orchestrator/ssds/pyproject.toml")})
        renamed = CLEAN["orchestrator/ssds/pyproject.toml"].replace('"sdp.ssds"', '"ssds"')
        self.assertViolations({"orchestrator/ssds/pyproject.toml": renamed}, {("F10", "orchestrator/ssds/pyproject.toml")})

    def test_the_ssds_distribution_adds_no_second_root(self) -> None:
        path = "orchestrator/ssds/pyproject.toml"
        text = CLEAN[path] + '[project.scripts]\nsdp-ssds = "sdp_orchestrator.ssds.extension:main"\n'
        self.assertViolations({path: text}, {("F10", path)})

    def test_no_private_cross_module_import(self) -> None:
        path = f"{S}/content/model.py"
        self.assertViolations({path: "from sdp_orchestrator.ssds.analyzers import _helper\n"}, {("F11", path)})
        self.assertViolations({path: "from sdp_orchestrator.ssds.analyzers.python import imports\n"}, {("F11", path)})

    def test_no_dynamic_import_or_code_execution(self) -> None:
        path = f"{S}/content/model.py"
        self.assertViolations({path: "import importlib\n"}, {("F11", path)})
        self.assertViolations({path: "m = __import__('sdp_orchestrator.ssds.ledger.append')\n"}, {("F11", path)})
        self.assertViolations({path: "exec('x = 1')\n"}, {("F11", path)})

    def test_no_component_imports_the_facades_or_the_extension(self) -> None:
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "from sdp_orchestrator.ssds.api import v1\n"}, {("F12", path)})
        path = f"{S}/admission/x.py"
        self.assertViolations({path: "from sdp_orchestrator.ssds import extension\n"}, {("F12", path)})

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
        test = "orchestrator/ssds/tests/test_example.py"
        self.assertViolations({test: "from qualification.ssds80.models import cases_s5_1\n"}, {("F13", test)})
        self.assertViolations({test: "import cases_s5_1\n"}, {("F13", test)})
        self.assertViolations(
            {test: "import sys\nsys.path.insert(0, 'qualification/ssds80/models')\n"}, {("F13", test)}
        )
        path = f"{S}/derivation/view.py"
        self.assertViolations({path: "import framework\n"}, {("F13", path)})


class ShadowBoundarySensorTests(unittest.TestCase):
    """G2 workplan §5.1 item 2: only the ledger append moves a ref or writes Git objects."""

    def assertViolations(self, changes: dict[str, str | None], expected: set[tuple[str, str]]) -> None:
        self.assertEqual(_run(changes), expected)

    def test_writing_git_subcommands_appear_only_in_the_append(self) -> None:
        path = f"{S}/ledger/read.py"
        self.assertViolations({path: "ARGS = ['git', 'push']\n"}, {("B1", path)})
        path = f"{S}/content/git.py"
        self.assertViolations({path: "ARGS = ['git', 'update-ref']\n"}, {("B1", path)})

    def test_only_content_and_ledger_start_processes(self) -> None:
        path = f"{S}/admission/genesis.py"
        self.assertViolations({path: "import subprocess\n"}, {("B1", path)})
        self.assertViolations({path: "import os\nos.system('git push')\n"}, {("B1", path)})


if __name__ == "__main__":
    unittest.main()
