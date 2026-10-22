"""The Interface (Phase E step 6): the query classes over derived state, and ``status``/``ask``/``read`` through
the root module's wiring at a qualified head, or labeled ``UNQUALIFIED`` as historical views (Manual §16.1-§16.2,
§23.4).

The queries run on the real derivation owner over scenario chains. The commands run the checkout launcher in a
fresh interpreter against a temporary SSDS home admitted by the operator script, so the root module, the home's
checks, the witnesses and the high-water mark are the owners exercised.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from ssds.derivation import Workflow, queries

from ._fixtures import commit, human_key, init_repo, tree
from ._scenario import Scenario
from .test_shadow_genesis_script import MANIFEST, RELEASE_STATE, SCRIPT

LAUNCHER = Path(__file__).resolve().parents[2] / "bin" / "ssds"
LAYERS = '''
    [[unit]]
    id = "arch"
    kind = "D3"
    scope = [{ path = "arch.md" }]
    [[unit]]
    id = "impl"
    kind = "D4"
    scope = [{ path = "impl.md" }]
    [[unit]]
    id = "tool"
    kind = "D4"
    scope = [{ path = "tool.md" }]
'''


class Queries(unittest.TestCase):
    def setUp(self) -> None:
        self.sc = Scenario(LAYERS, {"arch.md": "# Arch\n\n## Ports\n\nports text\n",
                                    "impl.md": "<!-- ssds:rel CONCRETIZES arch -->\nimpl body\n",
                                    "tool.md": "<!-- ssds:rel DEPENDS_ON impl -->\ntool body\n"},
                           modes={"tool": {"mode": "UNGOVERNED"}})

    def workflow(self) -> Workflow:
        return Workflow(self.sc.derive())

    def test_governs_follows_governing_relations_with_their_path(self) -> None:
        w = self.workflow()
        self.assertEqual([(i["unit"], i["label"], i["path"]) for i in queries.governs(w, "impl")],
                         [("arch", "GOVERNING", ["CONCRETIZES arch"])])
        self.assertEqual(queries.governs(w, "tool"), [], "a WARRANT edge does not govern")

    def test_depends_by_class_and_direction(self) -> None:
        w = self.workflow()
        warrant = queries.depends(w, "tool")
        self.assertEqual([i["unit"] for i in warrant["items"] if i["exact"]], ["impl"])
        self.assertEqual(warrant["widening"], "UNBOUNDED", "with no completeness judgment the closure is the whole tree")
        self.assertEqual([i["unit"] for i in queries.depends(w, "impl", direction="dependents")["items"]], ["tool"])
        self.assertEqual(queries.depends(w, "impl", "GOVERNING")["items"][0]["label"], "IMPLIED")
        with self.assertRaises(ValueError):
            queries.depends(w, "impl", "NOPE")

    def test_search_hits_are_candidates_only(self) -> None:
        hits = queries.search(self.workflow(), "body")
        self.assertEqual([(h["path"], h["owner"], h["label"]) for h in hits],
                         [("impl.md", "impl", "CANDIDATE"), ("tool.md", "tool", "CANDIDATE")])

    def test_locate_resolves_a_heading_and_names_staleness(self) -> None:
        w = self.workflow()
        rev = self.sc.rev("arch")
        found = queries.locate(w, f"arch@{rev}#ports")
        self.assertTrue(found["resolved"] and found["current"])
        self.assertEqual(len(found["named"]), 1)
        self.assertFalse(queries.locate(w, "arch@sha256:" + "0" * 64)["current"])
        self.assertFalse(queries.locate(w, "arch#missing")["resolved"])
        self.assertFalse(queries.locate(w, "nowhere")["resolved"])

    def test_changed_and_history_follow_admitted_positions(self) -> None:
        self.sc.absorb({"impl.md": "<!-- ssds:rel CONCRETIZES arch -->\nimpl body two\n"})
        w = self.workflow()
        self.assertEqual([(c["position"], c["units"]) for c in queries.changed(w, 0)], [(1, ["impl"])])
        self.assertEqual(queries.changed(w, 0, ["arch"]), [])
        self.assertEqual([(h["position"], h["label"]) for h in queries.history(w, "impl")],
                         [(0, "HISTORICAL"), (1, "HISTORICAL")])

    def test_explain_and_status(self) -> None:
        w = self.workflow()
        self.assertEqual(queries.explain(w, "tool")["mode"], "UNGOVERNED")
        self.assertEqual(queries.status(w, "tool"), "unclassified")
        self.assertEqual(queries.status(w, "impl"), "stale", "a NATIVE subject with no acceptance is not valid")
        with self.assertRaises(KeyError):
            queries.explain(w, "nothing")

    def test_impact_takes_the_write_set_and_its_dependents(self) -> None:
        w = self.workflow()
        files = dict(self.sc.files, **{"impl.md": "<!-- ssds:rel CONCRETIZES arch -->\nedited\n"})
        answer = queries.impact(w, tree(files, self.sc.manifest))
        self.assertEqual(answer["write_set"], ["impl"])
        self.assertEqual([i["unit"] for i in answer["impacted"]], ["tool"])

    def test_answers_are_deterministic(self) -> None:
        first, second = self.workflow(), self.workflow()
        for name, args in (("governs", ("impl",)), ("depends", ("tool",)), ("search", ("body",)),
                           ("explain", ("impl",)), ("history", ("arch",))):
            self.assertEqual(json.dumps(getattr(queries, name)(first, *args), sort_keys=True),
                             json.dumps(getattr(queries, name)(second, *args), sort_keys=True), name)


class Commands(unittest.TestCase):
    """``status``, ``ask`` and ``read`` through the root module over a temporary SSDS home."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        root = Path(self._tmp.name)
        self.repo = init_repo(root / "repo")
        for path, text in {".ssds/manifest.toml": MANIFEST, "PROTOCOL-RELEASE-STATE.yaml": RELEASE_STATE,
                           "source/roles/a.md": "# A\n", "source/README.md": "# Source\n", "manual.md": "# Manual\n",
                           "orchestrator/src/tool.py": "import os\n"}.items():
            (self.repo / path).parent.mkdir(parents=True, exist_ok=True)
            (self.repo / path).write_text(text)
        commit(self.repo, "baseline")
        self.home = root / "home"
        private, _ = human_key(root)
        self.env = {**os.environ, "SSDS_HOME": str(self.home)}
        base = [sys.executable, str(SCRIPT), "--repository", str(self.repo), "--ledger-id", "demo"]
        prepared = subprocess.run([*base, "prepare", "--public-key", str(root / "approver.pub")], capture_output=True,
                                  text=True, env=self.env, timeout=240, check=True)
        message = re.search(r"approval message:\s+(\S+)", prepared.stdout).group(1)
        subprocess.run(["ssh-keygen", "-q", "-Y", "sign", "-f", str(private), "-n", "ssds", message], check=True,
                       capture_output=True, stdin=subprocess.DEVNULL, timeout=60)
        subprocess.run([*base, "admit", "--signature", message + ".sig"], capture_output=True, text=True, env=self.env,
                       timeout=240, check=True)

    def ssds(self, *args: str) -> tuple[int, dict | None, str]:
        result = subprocess.run([sys.executable, str(LAUNCHER), *args, "--ledger", "demo", "--repository", str(self.repo)],
                                capture_output=True, text=True, env=self.env, timeout=240, check=False)
        try:
            return result.returncode, json.loads(result.stdout), result.stderr
        except json.JSONDecodeError:
            return result.returncode, None, result.stdout + result.stderr

    def test_status_names_the_qualified_head(self) -> None:
        code, report, err = self.ssds("status")
        self.assertEqual(code, 0, err)
        self.assertEqual((report["head"]["label"], report["head"]["position"], report["qualification"]),
                         ("QUALIFIED", 0, "QUALIFIED"))
        self.assertTrue(report["current_assertion"])
        self.assertEqual({s: v["mode"] for s, v in report["subjects"].items()},
                         {"ssdp.protocol": "LEGACY", "ssds8.manual": "LEGACY", "orchestrator.program": "UNGOVERNED"})
        self.assertEqual(self.ssds("status")[1], report, "identical state, identical answer")

    def test_ask_and_read_answer_at_the_head(self) -> None:
        code, answer, err = self.ssds("ask", "explain", "ssds8.manual")
        self.assertEqual(code, 0, err)
        self.assertEqual((answer["head"]["label"], answer["answer"]["mode"]), ("QUALIFIED", "LEGACY"))
        code, answer, err = self.ssds("read", "manual.md")
        self.assertEqual((code, answer["answer"]["content"]), (0, "# Manual\n"), err)
        code, answer, err = self.ssds("read", "ssdp.protocol.roles")
        self.assertEqual((code, answer["answer"]["content"]), (0, "# A\n"), err)
        code, answer, err = self.ssds("ask", "nonsense")
        self.assertEqual((code, answer), (2, None), "an unknown query class is refused")
        self.assertIn("refused: unknown query 'nonsense'", err)
        self.assertEqual(self.ssds("read", "nowhere.md")[0], 2)

    def test_without_qualification_every_answer_is_unqualified(self) -> None:
        checkpoint = next((self.home / "witness" / "demo").glob("*.json"))
        checkpoint.unlink()
        code, report, err = self.ssds("status")
        self.assertEqual((code, report["head"]["label"], report["current_assertion"]), (1, "UNQUALIFIED", False), err)
        self.assertTrue(report["assertion_withheld"][0].startswith("qualification UNQUALIFIED"))
        code, answer, err = self.ssds("ask", "explain", "ssds8.manual")
        self.assertEqual((code, answer["head"]["label"]), (0, "UNQUALIFIED"), err)

    def test_the_home_check_holds_before_anything_is_read(self) -> None:
        mark = self.home / "state" / "demo" / "high-water.json"
        held = mark.read_bytes()
        (self.home / "genesis" / "demo" / "planted").symlink_to(self.repo)
        code, report, err = self.ssds("status")
        self.assertEqual((code, report), (2, None), "nothing is presented from a home that fails its check")
        self.assertIn("is a symbolic link", err)
        self.assertEqual(mark.read_bytes(), held, "and nothing is written")


if __name__ == "__main__":
    unittest.main()
