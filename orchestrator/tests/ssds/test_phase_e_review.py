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



# -- the re-Review of b791215 (E-B1 to E-B4): its executed constructions (scratch probes.py), as tests --------


def _submit(f: Flow, changes: dict, tree_edit=None) -> tuple[str, str]:
    import hashlib

    from ._scenario import agent, fresh
    from .test_routes import SLOTS

    f.counter += 1
    task = f"probe-task-{f.counter}"
    base, cand, x, _ = f._candidate(changes)
    if tree_edit:
        t = dict(f.sc.trees[cand])
        tree_edit(t)
        cand = f.sc.add_tree(t)
        x = "sha256:" + hashlib.sha256(f"ssds.transformation.v1|{base}|{cand}".encode()).hexdigest()
    holder = f.item()
    binding = dict(fresh(agent("maker"), task), obligation=holder.obligation.id, item={"unit": holder.unit, "rev": f.sc.rev(holder.unit)})
    result = record("TASK_RESULT", target={"task": task, "candidate": cand, "transformation": x, "base": base},
                    outcome="COMPLETE", actor=agent("maker"), actor_class="AGENT", frame={"transformation": x},
                    fields={"slots": SLOTS})
    f.sc.admit(with_id(dict(result, binding=binding)))
    return x, cand


def _realization(f, unit: str = "records") -> dict:
    real = with_id(record("REALIZATION", target={"spec": {"unit": "tests.conv", "rev": f.sc.rev("tests.conv")},
                                                 "claim": [{"unit": unit, "rev": f.sc.rev(unit)}]},
                          outcome="COMPLETE", actor="machinery:runner-ci", actor_class="MACHINERY",
                          fields={"execution": {"tree": f.sc.head, "units": [], "reads": []}, "configuration": {}}))
    f.sc.admit(real)
    return real


def _partitioned_with_evidence():
    from .test_partition import NOTES, PartFlow, plan

    f = PartFlow.__new__(PartFlow)
    text = plan().replace('verifier = "REVIEW"', 'verifier = "REVIEW"\nsecondary = [{check="TEST_INTEGRITY.no_skips"}, '
                                                 '{check="BOUNDARY.write_scope"}]')
    f.sc = Scenario(D4_RECORDS + NOTES, {**FILES, "plans/work.md": text, "notes/a.md": "a\n", "notes/b.md": "b\n"},
                    policy='schema = 1\n[domains.D4]\nevidence = ["health"]\n')
    f.counter = 0
    f.accept_plan()
    f.spend(f.item().obligation)
    f.partition(f.budget_decision(f.item()), [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
    f.work_part(f.item().parts[0], {"records.md": "# Records done\n"})
    real = _realization(f)
    EvidenceFlow.assessment(f, real, "PASS")
    f.work_part(f.item().parts[1], {"notes/a.md": "a done\n", "notes/b.md": "b done\n"})
    f.item_level("PASS")
    return f, real


class ReReview(unittest.TestCase):
    """The re-Review of b791215: E-B1 to E-B4, each failing on b791215, with the controls it named."""

    def override(self, f, subjects: list[str]) -> None:
        from ._scenario import OWNER

        c = challenge(f.sc.triple("design"))
        f.sc.admit(c)
        f.sc.admit(judgment("RISK_OVERRIDE", {"record": c["id"]}, None, actor=OWNER,
                            fields={"continuation": {"subjects": subjects, "items": ["plan.work.item"], "kinds": ["DOCUMENT"]}}))

    def test_e_b1_no_composite_discharge_around_an_open_part(self) -> None:
        f, real = _partitioned_with_evidence()
        self.assertEqual(f.item().discharge(), "DISCHARGED")
        EvidenceFlow.assessment(f, real, "FAIL")
        self.assertEqual(f.item().discharge(), "OPEN")
        self.override(f, [])
        item = f.item()
        self.assertIn("OPEN", [p.discharge() for p in item.parts])
        self.assertEqual(item.discharge(), "OPEN", "a part outside the provisional permission keeps the whole open")
        self.assertNotEqual(item.route.route, "discharged")

    def test_e_b1_complete_permission_discharges_provisionally(self) -> None:
        f, real = _partitioned_with_evidence()
        EvidenceFlow.assessment(f, real, "FAIL")
        self.override(f, ["records", "notes.a", "notes.b"])
        item = f.item()
        self.assertEqual(item.discharge(), "DISCHARGED_PROVISIONAL")
        self.assertTrue(all(p.discharge() in ("DISCHARGED", "DISCHARGED_PROVISIONAL") for p in item.parts))

    def test_e_b2_an_item_level_re_review_carries_earlier_findings(self) -> None:
        from .test_partition import partitioned_and_worked

        f = partitioned_and_worked()
        old = f.item_level("NO_PASS", [{"part": 0, "units": ["records"], "detail": "WHOLE_RESULT_FINDING"}])
        f.work_part(f.item().parts[0], {"records.md": "# Repaired result\n"})
        w = f.w()
        o = next(o for o in w.of_kind("REVIEW") if o.target.get("integrated") == "ITEM")
        self.assertIn(old["id"], [c["record"] for c in w.briefing.carried(o)])
        self.assertIn("WHOLE_RESULT_FINDING", section(renderer(w).brief(o), "Carried objections (another judge's)"))

    def diff(self, edit, addition: bool = False) -> str:
        from .test_partition import NOTES

        f = Flow()
        if addition:
            text = document_item(write_scope='["records.md", "notes/"]').replace('affected = ["records.md"]',
                                                                                 'affected = ["records.md", "notes/"]')
            f.sc = Scenario(MANIFEST + NOTES, {**FILES, "plans/work.md": text, "notes/b.md": "b\n"})
            f.accept_plan()
        x, _ = _submit(f, {}, tree_edit=edit)
        w = f.w()
        o = next(o for o in w.of_kind("REVIEW") if o.target.get("transformation") == x)
        return section(renderer(w).brief(o), "Candidate diff and machine-produced facts")

    def test_e_b3_added_entry_types_are_distinguished(self) -> None:
        from ssds.content import Entry

        bodies = []
        for mode in ("100644", "100755", "120000"):
            d = self.diff(lambda t, m=mode: t.__setitem__("notes/a.md", Entry(m, b"target\n")), addition=True)
            bodies.append(d[d.index("### notes/a.md"):])
        self.assertEqual(len(set(bodies)), 3, "regular, executable and symbolic-link additions")
        self.assertIn("absent -> link 120000", bodies[2])

    def test_e_b3_a_final_newline_edit_is_kept(self) -> None:
        from ssds.content import Entry

        bodies = []
        for data in (b"# Records\nSAME_TEXT", b"# Records\nSAME_TEXT\n"):
            d = self.diff(lambda t, v=data: t.__setitem__("records.md", Entry("100644", v)))
            bodies.append(d[d.index("### records.md"):])
        self.assertNotEqual(bodies[0], bodies[1])
        self.assertIn("\\ No newline at end of file", bodies[0])

    def test_e_b3_controls(self) -> None:
        from ssds.content import Entry

        for label, edit, needle in (("deletion", lambda t: t.pop("records.md"), "-# Records"),
                                    ("mode", lambda t: t.__setitem__("records.md", Entry("100755", t["records.md"].data)),
                                     "100644 -> 100755"),
                                    ("type", lambda t: t.__setitem__("records.md", Entry("120000", b"target\n")),
                                     "100644 -> 120000"),
                                    ("binary", lambda t: t.__setitem__("records.md", Entry("100644", b"\xff\xfe\x00")),
                                     "binary content:")):
            with self.subTest(label=label):
                self.assertIn(needle, self.diff(edit))

    def test_e_b4_an_eligible_qualified_gate_stays_visible_when_not_current(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"},
                      policy='schema = 1\n[domains.D3]\ngates = ["g"]\ngate_holders = ["human:SHA256:alice"]\n'
                             'humans = ["human:SHA256:alice"]\n')
        w = Workflow(sc.derive())
        gate = next(o for o in w.of_kind("GATE") if o.target["subject"]["subject"] == "arch")
        qualified = judgment("GATE_DECISION", dict(gate.target, core="sha256:" + "c" * 64), "ACCEPT", actor=HUMAN,
                             basis=[content("arch", sc.rev("arch"))], fields={"adequacy": "ADEQUATE", "qualification": "QUALIFIED"})
        sc.admit(qualified)
        sc.admit(challenge({"record": qualified["id"]}))
        w = Workflow(sc.derive())
        self.assertEqual(w.d.current(qualified["id"]), 0)
        self.assertIn(qualified["id"], w.d.eligible_gate_decisions("arch", "g"))
        entries = {e["obligation"]: e for e in renderer(w).inspector()["entries"]}
        self.assertIn(qualified["id"], entries, "only loss of eligibility or supersession removes it")
        self.assertEqual(entries[qualified["id"]]["evidence_core"]["current"], "F")


# -- the re-Review of 89684fb (E-R1): retained work across partition history, its constructions as tests -----


FOLLOWUP_UNIT = '''
    [[unit]]
    id = "plan.work.followup"
    part_of = "plan.work"
    subject = false
    scope = [{ file = "plans/work.md", heading = ["Followup"] }]
'''


def _retained_flow():
    from .test_lint import item_block, plan_text
    from .test_partition import NOTES, PartFlow, plan

    text = plan().replace('verifier = "REVIEW"', 'verifier = "REVIEW"\nsecondary = [{check="TEST_INTEGRITY.no_skips"}, '
                                                 '{check="BOUNDARY.write_scope"}]')
    followup = item_block(kind="DOCUMENT", write_scope='["notes/b.md"]', affected='["notes/b.md"]', o1_verifier='"REVIEW"',
                          secondary="[]", dependencies="{}", extra_item='depends_on = ["work"]')
    followup = followup.replace('item = "work"', 'item = "followup"').replace('ref = "#item"', 'ref = "#followup"')
    text += "\n## Followup" + plan_text(followup).split("## Item", 1)[1]

    class RetainedFlow(PartFlow):
        def __init__(self) -> None:
            self.sc = Scenario(D4_RECORDS + NOTES + FOLLOWUP_UNIT, {**FILES, "plans/work.md": text, "notes/a.md": "a\n",
                                                                    "notes/b.md": "b\n"},
                               policy='schema = 1\n[domains.D4]\nevidence = ["health"]\n')
            self.counter = 0
            from ._scenario import OWNER

            units = ["plan.work.item", "plan.work.followup"]
            sc = self.sc
            sc.admit(judgment("PLAN_ACCEPTANCE", {"units": ["plan.work"]}, "ACCEPTED", actor=OWNER,
                              basis=[content("plan.work.objective", sc.rev("plan.work.objective"))]
                              + [content(u, sc.rev(u), "PLAN_CONTROL") for u in units],
                              fields={"objective": {"unit": "plan.work.objective", "rev": sc.rev("plan.work.objective")},
                                      "items": [{"unit": u, "rev": sc.rev(u)} for u in units]}))

        def item(self):
            return self.w().items.by_id("plan.work", "work")

    return RetainedFlow()


def _retained(kind: str):
    f = _retained_flow()
    if kind == "whole":  # history A: the whole item integrated the work before its first partition
        x, cand = _submit(f, {"records.md": "# Retained whole result\n"})
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        real = _realization(f)
        EvidenceFlow.assessment(f, real, "PASS")
        assert f.item().discharge() == "DISCHARGED"
        EvidenceFlow.assessment(f, real, "FAIL")
        assert f.item().discharge() == "OPEN"
        f.attempt(f.item().obligation, "notes/a.md")
        f.partition(f.budget_decision(f.item()), [(["o1"], ["records", "notes.a"]), (["o2", "o3"], ["notes.b"])])
        f.work_part(f.item().parts[0], {"notes/a.md": "a final\n"})
        f.work_part(f.item().parts[1], {"notes/b.md": "b final\n"})
    else:  # history B: a part integrated the work, then was replaced by a re-partition
        f.spend(f.item().obligation)
        f.partition(f.budget_decision(f.item()), [(["o1"], ["records", "notes.a"]), (["o2", "o3"], ["notes.b"])])
        f.work_part(f.item().parts[0], {"records.md": "# Retained part result\n"})
        real = _realization(f)
        EvidenceFlow.assessment(f, real, "PASS")
        f.work_part(f.item().parts[1], {"notes/b.md": "b done\n"})
        f.item_level("PASS")
        assert f.item().discharge() == "DISCHARGED"
        EvidenceFlow.assessment(f, real, "FAIL")
        assert f.item().discharge() == "OPEN"
        f.attempt(f.item().parts[0].obligation, "notes/a.md")
        f.partition(f.budget_decision(f.item().parts[0]), [(["o1"], ["records", "notes.a"])])
        replacement = next(p for p in f.item().parts if p.share[2] == frozenset({"o1"}))
        f.work_part(replacement, {"notes/a.md": "a replaced\n"})
    f.item_level("PASS")
    return f


class RetainedWork(unittest.TestCase):
    """E-R1: a failing term of retained work reopens the item across partition history, its restoring route is
    live and dependent work waits; complete permission gives at most provisional discharge."""

    def check(self, kind: str) -> None:
        for scope, want in ((None, "OPEN"), ([], "OPEN"), (["records", "notes.a", "notes.b"], "DISCHARGED_PROVISIONAL")):
            with self.subTest(history=kind, permission=scope):
                f = _retained(kind)
                if scope is not None:
                    ReReview().override(f, scope)
                w = f.w()
                item = w.items.by_id("plan.work", "work")
                followup = w.items.by_id("plan.work", "followup")
                self.assertIn("records", item.subjects, "the retained subject is the item's")
                self.assertEqual(item.discharge(), want)
                if want == "OPEN":
                    self.assertNotEqual(item.route.route, "discharged")
                    self.assertEqual(followup.readiness().state, "WAITING", "dependent work waits")
                    restoring = [p for p in item.parts if p.discharge() == "OPEN"]
                    self.assertTrue(restoring, "the part that answers for the retained work reopens")
                    self.assertIn(restoring[0].route.route.split(":")[0], ("re-dispatch", "COORDINATE", "dispatch"))

    def test_history_a_work_of_the_whole_before_its_partition(self) -> None:
        self.check("whole")

    def test_history_b_work_of_a_replaced_part(self) -> None:
        self.check("replacement")

    def test_retained_work_no_part_covers_goes_to_the_principal(self) -> None:
        f = _retained_flow()
        x, cand = _submit(f, {"records.md": "# Retained whole result\n"})
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        real = _realization(f)
        EvidenceFlow.assessment(f, real, "PASS")
        EvidenceFlow.assessment(f, real, "FAIL")
        f.attempt(f.item().obligation, "notes/a.md")
        f.partition(f.budget_decision(f.item()), [(["o1"], ["notes.a"]), (["o2", "o3"], ["notes.b"])])
        f.work_part(f.item().parts[0], {"notes/a.md": "a final\n"})
        f.work_part(f.item().parts[1], {"notes/b.md": "b final\n"})
        f.item_level("PASS")
        item = f.item()
        self.assertEqual(item.uncovered_subjects, frozenset({"records"}))
        self.assertEqual(item.discharge(), "OPEN")
        self.assertEqual(item.route.route, "COORDINATE:item-level-no-part", "the principal decides, on SD-54's chain")
        self.assertTrue(item.route.decisions)

if __name__ == "__main__":
    unittest.main()
