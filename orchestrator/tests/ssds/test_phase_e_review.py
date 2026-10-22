"""Repairs of the Phase E Review of 09f3505 (different family, B1-B6), each case failing on the reviewed code.

The constructions are the Review's executed trajectories (its scratch ``probes.py``), run through the real
derivation and renderer; expected values are the Review's discriminators, written from Manual §10.4 (SD-36),
§5.5 and §16.6, §16.5, §16.3 (3) and §16.8, never computed by the rule under test.
"""

from __future__ import annotations

import unittest

from ssds.derivation import Workflow, queries
from ssds.ledger.read import with_id

from . import test_assessment as ta
from ._fixtures import record
from ._scenario import HUMAN, Scenario, challenge, content, judgment, on_record
from .test_briefs import renderer, section
from .test_lint import FILES, MANIFEST
from .test_obligations import TWO
from .test_routes import Flow, document_item

D4_RECORDS = MANIFEST.replace('id = "records"\n    kind = "EVIDENCE_RECORD"', 'id = "records"\n    kind = "D4"')


class EvidenceFlow(Flow):
    """An item writing a D4 unit whose domain requires evidence ``health``."""

    def __init__(self) -> None:
        text = document_item().replace("secondary = []", 'secondary = [{ check = "TEST_INTEGRITY.no_skips" }, '
                                                         '{ check = "BOUNDARY.write_scope" }]')
        self.sc = Scenario(D4_RECORDS, {**FILES, "plans/work.md": text}, policy='schema = 1\n[domains.D4]\nevidence = ["health"]\n')
        self.counter = 0
        self.accept_plan()

    def assessment(self, realization: dict, outcome: str) -> dict:
        fields = {"mode": "ORDINARY", "reading": {"unit": "tests.conv", "rev": self.sc.rev("tests.conv")}}
        if outcome == "FAIL":
            fields["failing_outputs"] = ["x"]
        rec = judgment("EVIDENCE_ASSESSMENT", {"realization": realization["id"], "obligation": "health"}, outcome,
                       basis=[on_record(realization["id"]), content("tests.conv", self.sc.rev("tests.conv"))], fields=fields)
        self.sc.admit(rec)
        return rec


class Discharge(unittest.TestCase):
    def test_b1_an_item_reads_its_subjects_evidence_at_every_head(self) -> None:
        f = EvidenceFlow()
        x, cand = f.submit("# Records\nDone.\n")
        view = f.sc.view(cand)
        real = with_id(record("REALIZATION", target={"spec": {"unit": "tests.conv", "rev": f.sc.rev("tests.conv")},
                                                     "claim": [{"unit": "records", "rev": view.rev("records")}]},
                              outcome="COMPLETE", actor="machinery:runner-ci", actor_class="MACHINERY",
                              fields={"execution": {"tree": cand, "units": [], "reads": []}, "configuration": {}}))
        f.sc.admit(real)
        f.assessment(real, "PASS")
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        self.assertEqual(f.item().discharge(), "DISCHARGED")
        f.assessment(real, "FAIL")
        w = f.w()
        self.assertLess(w.d.a.ev("records", "health", w._value, w.d.base, w.d.j.nonind), 2)
        self.assertEqual(f.item().discharge(), "OPEN", "never latched (SD-36): no provisional permission was given")
        self.assertNotEqual(f.item().route.route, "discharged")


class EvidenceProjection(unittest.TestCase):
    def test_b2_a_challenged_assessment_is_no_supporting_premise(self) -> None:
        r = ta.Runs()
        real = r.run(r.tree("T0"), ta.GOOD)
        passing = judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": "obl"}, "PASS",
                           basis=[on_record(real["id"]), content("spec", r.sc.rev("spec"))],
                           fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": r.sc.rev("spec")}})
        r.sc.admit(passing)
        self.assertTrue(Workflow(r.sc.derive()).briefing.required_evidence("code")[0]["holds"])
        r.sc.admit(challenge({"record": passing["id"]}))
        w = Workflow(r.sc.derive())
        self.assertEqual(w.d.current(passing["id"]), 0)
        (entry,) = [e for e in queries.evidence(w, "code") if e.get("assessment") == passing["id"]]
        self.assertNotEqual(entry["status"], "current", "a non-current assessment is not current evidence")
        (required,) = w.briefing.required_evidence("code")
        self.assertEqual((required["holds"], required["via"]), (False, []))
        self.assertNotEqual(required["status"], "holding")


class ReviewBriefs(unittest.TestCase):
    def review_of(self, f: Flow, x: str):
        w = f.w()
        return w, next(o for o in w.of_kind("REVIEW") if o.target.get("transformation") == x)

    def test_b3_unresolved_findings_survive_a_prose_amendment(self) -> None:
        f = Flow()
        x, cand = f.submit("# Records\nFirst candidate.\n")
        earlier = f.review(x, cand, "NO_PASS", findings=[{"obligation": "o1", "units": ["records"], "detail": "FIRST_FINDING"}])
        f.sc.absorb({"plans/work.md": document_item(prose="Document it differently.\n")})
        f.accept_plan()
        x2, _ = f.submit("# Records\nSecond candidate.\n")
        w, o = self.review_of(f, x2)
        carried = w.briefing.carried(o)
        self.assertIn(earlier["id"], [c["record"] for c in carried])
        self.assertIn("FIRST_FINDING", section(renderer(w).brief(o), "Carried objections (another judge's)"))

    def test_b4_the_review_brief_shows_the_actual_edit(self) -> None:
        for value in ("REVIEW_PROBE_ALPHA", "REVIEW_PROBE_BETA"):
            with self.subTest(value=value):
                f = Flow()
                x, cand = f.submit(f"# Records\n{value}\n")
                w, o = self.review_of(f, x)
                diff = section(renderer(w).brief(o), "Candidate diff and machine-produced facts")
                self.assertIn(f"+{value}", diff, "the candidate's changed text")
                self.assertIn(cand, diff, "bound to the candidate")
                self.assertIn(x, diff, "and to its transformation")

    def test_b5_governing_text_at_the_bound_revision(self) -> None:
        f = Flow()
        old = f.sc.rev("design")
        f.sc.absorb({"plans/work.md": document_item().replace("[contract]", f'governing = ["design@{old}"]\n[contract]')})
        f.accept_plan()
        f.sc.absorb({"design.md": "# Design\nREVIEW_PROBE_NEW_GOVERNING_TEXT\n"})
        governing = section(renderer(f.w()).brief(f.item().obligation), "3. Governing content")
        self.assertNotIn("REVIEW_PROBE_NEW_GOVERNING_TEXT", governing, "never the current text in its place")
        self.assertIn("# Design", governing)
        self.assertIn(old, governing)

    def test_b5_an_unavailable_revision_is_said_to_be(self) -> None:
        f = Flow()
        missing = "sha256:" + "d" * 64
        f.sc.absorb({"plans/work.md": document_item().replace("[contract]", f'governing = ["design@{missing}"]\n[contract]')})
        f.accept_plan()
        governing = section(renderer(f.w()).brief(f.item().obligation), "3. Governing content")
        self.assertIn("UNAVAILABLE", governing)


class Inspector(unittest.TestCase):
    def test_b6_a_qualified_gate_stays_an_entry_until_superseded(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"},
                      policy='schema = 1\n[domains.D3]\ngates = ["g"]\ngate_holders = ["human:SHA256:alice"]\n'
                             'humans = ["human:SHA256:alice"]\n')
        w = Workflow(sc.derive())
        gate = next(o for o in w.of_kind("GATE") if o.target["subject"]["subject"] == "arch")
        qualified = judgment("GATE_DECISION", dict(gate.target, core="sha256:" + "c" * 64), "ACCEPT", actor=HUMAN,
                             basis=[content("arch", sc.rev("arch"))],
                             fields={"adequacy": "ADEQUATE", "qualification": "QUALIFIED"})
        sc.admit(qualified)
        w = Workflow(sc.derive())
        self.assertEqual(w.of_kind("GATE"), [], "no further gate answer is owed")
        entries = {e["obligation"]: e for e in renderer(w).inspector()["entries"]}
        self.assertIn(qualified["id"], entries, "§16.8: visible while eligible")
        self.assertEqual(entries[qualified["id"]]["kind"], "QUALIFIED_GATE")
        sc.admit(judgment("ACCEPTANCE", sc.triple("impl"), "PASS", actor=HUMAN, basis=[content("impl", sc.rev("impl"))]))
        self.assertIn(qualified["id"], {e["obligation"] for e in renderer(Workflow(sc.derive())).inspector()["entries"]},
                      "after an unrelated admission")
        superseding = judgment("GATE_DECISION", dict(gate.target, core="sha256:" + "c" * 64), "ACCEPT", actor=HUMAN,
                               basis=[content("arch", sc.rev("arch"))], supersedes=[qualified["id"]],
                               fields={"adequacy": "ADEQUATE", "qualification": "UNQUALIFIED"})
        sc.admit(superseding)
        self.assertNotIn(qualified["id"], {e["obligation"] for e in renderer(Workflow(sc.derive())).inspector()["entries"]},
                         "authorized supersession removes it")


if __name__ == "__main__":
    unittest.main()
