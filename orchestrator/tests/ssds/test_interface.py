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

from ._scenario import attested
from ._fixtures import commit, git, human_key, init_repo, tree
from ._scenario import HUMAN, Scenario, agent, content, judgment, on_record, submit
from ._scenario import integrate as integrate_change
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
        self.assertEqual([i["unit"] for i in warrant["items"] if i["via"] == "relation"], ["impl"])
        self.assertEqual(warrant["widening"], "UNBOUNDED", "with no completeness judgment the closure is the whole tree")
        self.assertEqual([i["unit"] for i in queries.depends(w, "impl", direction="dependents")["items"]], ["tool"])
        self.assertEqual(queries.depends(w, "impl", "GOVERNING")["items"][0]["label"], "CANDIDATE",
                         "no completeness judgment: not inside a judged-complete scope")
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
        with self.assertRaises(queries.QueryError):
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


class StepSixReview(unittest.TestCase):
    """The step 6 review of f9e26a81 (B1-B3), each case failing on the reviewed code; expected values from
    Manual §16.2's labels and statuses, §4.6 and §1.11."""

    def layers(self) -> Scenario:
        return Scenario(LAYERS, {"arch.md": "# Arch\n", "impl.md": "<!-- ssds:rel CONCRETIZES arch -->\nimpl\n",
                                 "tool.md": "<!-- ssds:rel DEPENDS_ON impl -->\ntool\n"})

    def test_b1_depends_claims_no_exactness_it_lacks(self) -> None:
        sc = self.layers()
        w = Workflow(sc.derive())
        prerequisites = queries.depends(w, "tool")
        self.assertEqual(prerequisites["widening"], "UNBOUNDED")
        self.assertEqual({i["label"] for i in prerequisites["items"]}, {"CANDIDATE"},
                         "nothing is IMPLIED outside a judged-complete scope")
        dependents = queries.depends(w, "impl", direction="dependents")
        self.assertEqual(dependents["widening"], "UNBOUNDED", "missing dependency knowledge never proves independence")
        self.assertEqual([(i["unit"], i["label"]) for i in dependents["items"]], [("tool", "CANDIDATE")])
        d = sc.derive()
        # every unit, the reserved leaves of §1.8 included, must be judged complete before no dependent is missing
        for unit in ("arch", "impl", "tool", "ssds.manifest", "ssds.policy", "ssds.unclassified"):
            sc.admit(*attested(judgment("COMPLETENESS", {"scope": [unit], "classes": ["WARRANT"],
                                               "membership": d.s.membership_digest([unit])}, "COMPLETE", actor=HUMAN,
                              basis=[content(unit, sc.rev(unit))])))
        w = Workflow(sc.derive())
        self.assertEqual(queries.depends(w, "tool")["widening"], "EXACT")
        self.assertEqual([(i["unit"], i["label"]) for i in queries.depends(w, "tool")["items"]], [("impl", "IMPLIED")])
        dependents = queries.depends(w, "impl", direction="dependents")
        self.assertEqual((dependents["widening"], [(i["unit"], i["label"]) for i in dependents["items"]]),
                         ("EXACT", [("tool", "IMPLIED")]))

    def test_b2_disputed_and_unavailable_evidence(self) -> None:
        from .test_assessment import BAD, GOOD, Runs

        none = Runs()
        self.assertEqual(queries.evidence(Workflow(none.sc.derive()), "code"),
                         [{"obligation": "obl", "label": "EVIDENTIAL", "status": "unavailable"}])
        r = Runs()
        t0 = r.tree("T0")
        r.fail(r.run(t0, BAD))
        w = Workflow(r.sc.derive())
        self.assertEqual([e["status"] for e in queries.evidence(w, "code")], ["current"], "a lone failure is no dispute")
        good = r.run(t0, GOOD)
        view = r.sc.view(t0)
        r.sc.admit(judgment("EVIDENCE_ASSESSMENT", {"realization": good["id"], "obligation": "obl"}, "PASS",
                            actor=agent("assessor"), actor_class="AGENT",
                            basis=[on_record(good["id"]), content("spec", view.rev("spec"))],
                            fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": view.rev("spec")}}))
        w = Workflow(r.sc.derive())
        self.assertEqual(queries.status(w, "code"), "disputed")
        self.assertEqual(sorted((e["outcome"], e["status"]) for e in queries.evidence(w, "code")),
                         [("FAIL", "disputed"), ("PASS", "disputed")], "the pair is the disagreement")

    def test_b2_drift(self) -> None:
        from .test_routes import Flow

        f = Flow()
        x, cand = f.submit("# Records\nDone.\n")
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        f.sc.absorb({"records.md": "# Records\nSomeone else.\n"})
        self.assertEqual(queries.status(f.w(), "records"), "drift", "its item's outputs moved (§10.4)")

    def test_b3_tensions_and_locate_follow_lineage(self) -> None:
        units = LAYERS + '''
            [[unit]]
            id = "pred"
            kind = "D3"
            scope = [{ path = "pred.md" }]
            [[unit]]
            id = "succ"
            kind = "D3"
            scope = [{ path = "succ.md" }]
            [[unit]]
            id = "critic"
            kind = "EVIDENCE_RECORD"
            scope = [{ path = "critic.md" }]
            [[unit]]
            id = "newname"
            kind = "D3"
            renamed_from = ["oldname"]
            scope = [{ path = "new.md" }]
        '''
        files = {"arch.md": "a\n", "impl.md": "i\n", "tool.md": "t\n", "pred.md": "p\n",
                 "succ.md": "<!-- ssds:rel SUPERSEDES pred -->\ns\n", "critic.md": "<!-- ssds:rel CHALLENGES pred -->\nc\n",
                 "new.md": "# New\n"}
        sc = Scenario(units, files)
        w = Workflow(sc.derive())
        found = queries.tensions(w, "succ")
        self.assertIn(("relation", "critic"), [(t["source"], t.get("unit")) for t in found], "predecessors' tensions")
        native = [t for t in found if t["source"] == "native"]
        self.assertEqual(native[0]["identities"], ["pred", "succ"], "native homes listed with their identities")
        located = queries.locate(w, "oldname")
        self.assertEqual((located["resolved"], located["unit"], located["former_name"]), (True, "newname", "oldname"))
        x, cand, _ = submit(sc, {}, agent("restructurer"), "t-1", manifest=units.replace('renamed_from = ["oldname"]\n', ""))
        integrate_change(sc, x, cand)
        w = Workflow(sc.derive())
        self.assertEqual(queries.locate(w, "oldname")["unit"], "newname", "lineage folds over every admitted structure")


class Commands(unittest.TestCase):
    """``status``, ``ask`` and ``read`` through the root module over a temporary SSDS home."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        root = Path(self._tmp.name)
        self.repo = init_repo(root / "repo")
        for path, text in {".ssds/manifest.toml": MANIFEST, ".ssds/policy.toml": "schema = 1\n",
                           "PROTOCOL-RELEASE-STATE.yaml": RELEASE_STATE,
                           "source/roles/a.md": "# A\n", "source/README.md": "# Source\n", "manual.md": "# Manual\n",
                           "orchestrator/src/tool.py": "import os\n"}.items():
            (self.repo / path).parent.mkdir(parents=True, exist_ok=True)
            (self.repo / path).write_text(text)
        self.baseline = commit(self.repo, "baseline")
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
                         {"ssdp.protocol": "LEGACY", "ssds8.manual": "LEGACY", "orchestrator.program": "UNGOVERNED",
                          "ssds.manifest": "UNGOVERNED", "ssds.policy": "UNGOVERNED", "ssds.unclassified": "UNGOVERNED"})
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

    def test_b4_the_mark_rises_to_a_qualified_head_whose_assertion_is_withheld(self) -> None:
        """NF5: the high-water mark keeps the last head qualified, whatever derivation withholds there."""

        from ssds.ledger.append import HostKey, append_entry, write_checkpoint
        from ssds.ledger.qualification import FileWitness
        from ssds.ledger.read import read_chain

        from ._fixtures import entry, record

        repository = self.home / "ledgers" / "demo.git"
        chain = read_chain(repository, "demo")
        key = HostKey.from_private_bytes((self.home / "keys" / "admission" / "demo.ed25519").read_bytes())
        adoption = record("RULESET_ADOPTION", target=None, actor="human:SHA256:x",
                          fields={"system": "ssds-rules/1", "policy": "sha256:" + "0" * 64, "analyzers": ["x/1"]})
        appended = append_entry(repository, entry("demo", 1, chain.entries[0].digest, key, lifecycle=adoption,
                                                  obs=self.baseline), key, chain.entries[0].commit)
        write_checkpoint(FileWitness(self.home / "witness"), appended.checkpoint)
        code, report, err = self.ssds("status")
        self.assertEqual((code, report["qualification"], report["current_assertion"]), (1, "QUALIFIED", False), err)
        self.assertEqual((report["head"]["label"], report["head"]["position"]), ("QUALIFIED", 1),
                         "a qualified head with its assertion withheld is still the qualified head")
        mark = json.loads((self.home / "state" / "demo" / "high-water.json").read_text())
        self.assertEqual((mark["position"], mark["entry_digest"]), (1, appended.digest))

    def test_b4_the_commands_only_read_the_product(self) -> None:
        def snapshot() -> tuple[str, ...]:
            files = sorted((str(p.relative_to(self.repo)), p.read_bytes()) for p in self.repo.rglob("*")
                           if p.is_file() and ".git" not in p.parts)
            return (git(self.repo, "for-each-ref"), git(self.repo, "count-objects", "-v"),
                    git(self.repo, "status", "--porcelain", "--ignored"), repr(files))

        before = snapshot()
        for args in (("status",), ("ask", "governs", "ssds8.manual"), ("ask", "search", "Manual"), ("ask", "changed"),
                     ("ask", "impact", self.baseline), ("read", "manual.md"), ("inspect",),
                     ("open", "sha256:" + "0" * 64)):
            self.assertIn(self.ssds(*args)[0], (0, 1, 2), args)
        self.assertEqual(snapshot(), before)

    def test_refusals_present_nothing(self) -> None:
        for args, says in ((("ask", "impact"), "impact"), (("ask", "changed", "nope"), "position")):
            code, answer, err = self.ssds(*args)
            self.assertEqual((code, answer), (2, None), args)
            self.assertIn(says, err)
        result = subprocess.run([sys.executable, str(LAUNCHER), "status", "--ledger", "demo", "--repository",
                                 str(self.home)], capture_output=True, text=True, env=self.env, timeout=240, check=False)
        self.assertEqual((result.returncode, result.stdout), (2, ""), "a repository that is not the ledger's refuses")
        self.assertIn("refused: cannot read", result.stderr)

    def test_open_and_inspect(self) -> None:
        from ssds.ledger.append import HostKey, append_entry, write_checkpoint
        from ssds.ledger.qualification import FileWitness
        from ssds.ledger.read import read_chain

        from ._fixtures import entry, record

        # a native subject owes work to open; the shadow ledger's LEGACY and UNGOVERNED subjects owe none
        repository = self.home / "ledgers" / "demo.git"
        chain = read_chain(repository, "demo")
        key = HostKey.from_private_bytes((self.home / "keys" / "admission" / "demo.ed25519").read_bytes())
        native = record("MODE_TRANSITION", target=None, actor="human:SHA256:x",
                        fields={"subject": "orchestrator.program", "mode": {"mode": "NATIVE", "ruleset": "ssds-rules/1"}})
        appended = append_entry(repository, entry("demo", 1, chain.entries[0].digest, key, lifecycle=native,
                                                  obs=self.baseline), key, chain.entries[0].commit)
        write_checkpoint(FileWitness(self.home / "witness"), appended.checkpoint)
        code, report, err = self.ssds("status")
        self.assertEqual(code, 0, err)
        self.assertTrue(report["obligations"], "the fixture derives obligations to open")
        for obligation in report["obligations"]:
            code, answer, err = self.ssds("open", obligation["id"])
            self.assertEqual(code, 0, err)
            self.assertEqual(answer["head"]["label"], "QUALIFIED")
            self.assertIn("NOT ISSUED", answer["answer"]["text"])
        code, answer, err = self.ssds("open", "sha256:" + "0" * 64)
        self.assertEqual((code, answer), (2, None), "an obligation not derived is refused")
        code, view, err = self.ssds("inspect")
        self.assertEqual(code, 0, err)
        self.assertEqual(set(view["answer"]), {"head", "entries", "digest"})
        self.assertEqual(self.ssds("inspect")[1], view, "deterministic")

    def test_the_mark_is_raised_only_through_a_rechecked_home(self) -> None:
        from ssds.cli import HomeAccess
        from ssds.ledger.qualification import HighWaterMark, Home, HomeRefused

        access = HomeAccess(Home(self.home), "demo")
        mark = self.home / "state" / "demo" / "high-water.json"
        held = mark.read_bytes()
        (self.home / "genesis" / "demo" / "planted").symlink_to(self.repo)
        with self.assertRaises(HomeRefused):
            access.raise_high_water(HighWaterMark(5, "sha256:" + "5" * 64))
        self.assertEqual(mark.read_bytes(), held)


if __name__ == "__main__":
    unittest.main()
