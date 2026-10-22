"""Phase E step 3a: revision runs and revision-assessment records at the real derivation owner (§10.2).

Carries S5 §10 ``revert_starts_a_new_run`` and ``in_run_acceptance_current``, and the D1/D2 revision-run
variants deferred from Phase D: 575dc78 N5 and f7419d5 N4 (a gate decided afresh in a later run over a
qualified earlier decision), f22b4dc N5 (a revert restoring under the obligation that started the earlier
run). Expected values are written from catalogue §10.2 and the Stage S cases, not computed by the rule.
"""

from __future__ import annotations

import hashlib
import unittest

from ssds.content import Structure, TreeView
from ssds.derivation import F, P, T
from ssds.derivation.frames import frame_state
from ssds.derivation.support import Support
from ssds.ledger.read import with_id

from ._fixtures import admission_body, record, tree
from ._scenario import HUMAN, HUMAN_B, OWNER, Scenario, agent, content, fresh, judgment
from .test_lint import item_block, plan_text

MANIFEST = '''
    [[unit]]
    id = "numerics"
    kind = "D2"
    scope = [{ path = "numerics.md" }]
    [[unit]]
    id = "notes"
    kind = "D3"
    scope = [{ path = "notes.md" }]
    [[unit]]
    id = "plan.work"
    kind = "PLAN"
    role = "composite"
    scope = [{ file = "plans/work.md" }]
    [[unit]]
    id = "plan.work.objective"
    part_of = "plan.work"
    subject = false
    scope = [{ file = "plans/work.md", heading = ["Objective"] }]
    [[unit]]
    id = "plan.work.item"
    part_of = "plan.work"
    subject = false
    scope = [{ file = "plans/work.md", heading = ["Item"] }]
'''
#: The AUTHOR D2 item whose tasks revise ``numerics`` (§10.2: only an AUTHOR task's result is a revision assessment).
AUTHOR_PLAN = plan_text(item_block(kind="AUTHOR", extra_item='authority = "D2"', write_scope='["numerics.md"]',
                                   affected='["numerics.md"]', o1_verifier='"REVIEW"', secondary="[]",
                                   slots='["claims", "unverified_assumptions", "deviations", "revision_assessments", '
                                         '"o1_content"]'))
RUN_FILES = {"numerics.md": "v0\n", "notes.md": "n\n", "plans/work.md": AUTHOR_PLAN}
POLICY = '''schema = 1
[domains.D2]
gates = ["d2-gate"]
gate_holders = ["human:SHA256:alice", "human:SHA256:bob", "human:SHA256:owner"]
owner = "human:SHA256:owner"
'''
NO_GATE = "schema = 1\n"


def rev_in(sc: Scenario, commit: str, unit: str = "numerics") -> str:
    return TreeView(sc.trees[commit], Structure(sc.structure.decl)).rev(unit)


def candidate(sc: Scenario, files: dict[str, str]) -> tuple[str, str, str, dict[str, str]]:
    merged = dict(sc.files, **files)
    cand = sc.add_tree(tree(merged, sc.manifest))
    x = "sha256:" + hashlib.sha256(f"ssds.transformation.v1|{sc.head}|{cand}".encode()).hexdigest()
    return sc.head, cand, x, merged


def assessed_result(sc: Scenario, base: str, cand: str, x: str, task: str, producer: str, assess: bool = True,
                    obligation: str = "obl", item: bool = True) -> dict:
    slots = {"revision_assessments": [{"subject": "numerics", "rev": rev_in(sc, cand)}]} if assess else {}
    result = record("TASK_RESULT", target={"task": task, "candidate": cand, "transformation": x, "base": base},
                    outcome="COMPLETE", actor=producer, actor_class="AGENT", frame={"transformation": x},
                    fields={"slots": slots})
    result["binding"] = fresh(producer, task)
    result["binding"]["obligation"] = obligation
    if item:
        result["binding"]["contract_revision"] = {"unit": "plan.work.item", "rev": sc.rev("plan.work.item")}
    return with_id(result)


def author(sc: Scenario, text: str, task: str, producer: str = agent("reviser"), obligation: str = "obl") -> dict:
    """An AUTHOR task's candidate revising ``numerics``, with its revision assessment, integrated."""

    base, cand, x, merged = candidate(sc, {"numerics.md": text})
    result = assessed_result(sc, base, cand, x, task, producer, obligation=obligation)
    sc.entries.append(admission_body(sc.position, base, cand, records=[result], integrates=x))
    sc.files, sc.head = merged, cand
    return result


def standing(rid: str) -> dict:
    return {"mode": "standing", "target": {"record": rid}, "class": "EXACT"}


def accept(sc: Scenario, assessment: str | None, frame="ADMITTED", rev: str | None = None) -> dict:
    t = sc.triple("numerics")
    if rev is not None:
        t = dict(t, rev=rev)
    basis = [content("numerics", t["rev"])] + ([standing(assessment)] if assessment else [])
    return judgment("ACCEPTANCE", t, "PASS", actor=OWNER, basis=basis, frame=frame)


def gate(sc: Scenario, assessment: str, actor: str, qualification: str = "UNQUALIFIED", frame="ADMITTED",
         rev: str | None = None) -> dict:
    t = sc.triple("numerics")
    if rev is not None:
        t = dict(t, rev=rev)
    return judgment("GATE_DECISION", {"gate": "d2-gate", "subject": t, "core": "sha256:" + "c" * 64}, "ACCEPT",
                    actor=actor, basis=[content("numerics", t["rev"]), standing(assessment)], frame=frame,
                    fields={"adequacy": "ADEQUATE", "qualification": qualification})


class RunCurrency(unittest.TestCase):
    def test_in_run_acceptance_current(self) -> None:
        # S5 §10 in_run_acceptance_current: an acceptance made in the current run is current
        sc = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        r1 = author(sc, "v1\n", "task-1")
        sc.admit(accept(sc, r1["id"]))
        self.assertEqual(sc.derive().valid("numerics"), T)

    def test_an_acceptance_without_its_counting_premise_is_not_current(self) -> None:
        # reading E19: Admission refuses it (§8.3 step 7); derivation fails closed on it in the meantime
        sc = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        author(sc, "v1\n", "task-1")
        sc.admit(accept(sc, None))
        self.assertEqual(sc.derive().valid("numerics"), F)

    def test_a_task_result_with_no_assessment_slot_counts_for_nothing(self) -> None:
        sc = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        base, cand, x, merged = candidate(sc, {"numerics.md": "v1\n"})
        result = assessed_result(sc, base, cand, x, "task-1", agent("reviser"), assess=False)
        sc.entries.append(admission_body(sc.position, base, cand, records=[result], integrates=x))
        sc.files, sc.head = merged, cand
        sc.admit(accept(sc, result["id"]))
        self.assertEqual(sc.derive().valid("numerics"), F)

    def test_only_the_author_tasks_result_is_a_revision_assessment(self) -> None:
        # §10.2 (step 3 review B1): a reviewer's result naming X, or a producing task bound to no AUTHOR item,
        # is no revision-assessment record however its slot reads.
        sc = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        base, cand, x, merged = candidate(sc, {"numerics.md": "v1\n"})
        producer = assessed_result(sc, base, cand, x, "task-1", agent("reviser"), assess=False)
        sc.entries.append(admission_body(sc.position, base, cand, records=[producer], integrates=x))
        sc.files, sc.head = merged, cand
        reviewer = record("TASK_RESULT", target={"task": "task-r", "transformation": x}, outcome="COMPLETE",
                          actor=agent("checker"), actor_class="AGENT", frame={"transformation": x},
                          fields={"slots": {"revision_assessments": [{"subject": "numerics", "rev": rev_in(sc, cand)}]}})
        reviewer["binding"] = dict(fresh(agent("checker"), "task-r"), obligation="review-x")
        reviewer = with_id(reviewer)
        sc.admit(reviewer)
        sc.admit(accept(sc, reviewer["id"]))
        self.assertEqual(sc.derive().valid("numerics"), F)
        sc2 = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        base, cand, x, merged = candidate(sc2, {"numerics.md": "v1\n"})
        unbound = assessed_result(sc2, base, cand, x, "task-1", agent("reviser"), item=False)
        sc2.entries.append(admission_body(sc2.position, base, cand, records=[unbound], integrates=x))
        sc2.files, sc2.head = merged, cand
        sc2.admit(accept(sc2, unbound["id"]))
        self.assertEqual(sc2.derive().valid("numerics"), F)

    def test_revert_starts_a_new_run(self) -> None:
        # S5 §10 revert_starts_a_new_run (798b2b4 B2, 71cf9b3 B2): after a revert to earlier bytes the earlier
        # acceptance of those bytes is not current; the reuse-bytes reading would make it current again.
        sc = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        r1 = author(sc, "v1\n", "task-1")
        first = accept(sc, r1["id"])
        sc.admit(first)
        r2 = author(sc, "v2\n", "task-2")
        sc.admit(accept(sc, r2["id"]))
        self.assertEqual(sc.derive().valid("numerics"), T)
        r3 = author(sc, "v1\n", "task-3")
        d = sc.derive()
        self.assertEqual(d.s.cur("numerics"), first["target"]["rev"], "the bytes are back")
        self.assertEqual((d.current(first["id"]), d.valid("numerics")), (F, F))
        # The earlier run's assessment record does not count in the new run either.
        sc.admit(accept(sc, r1["id"]))
        self.assertEqual(sc.derive().valid("numerics"), F)
        sc.admit(accept(sc, r3["id"]))
        self.assertEqual(sc.derive().valid("numerics"), T, "the new run's own assessment and acceptance")

    def test_a_restore_under_the_obligation_that_started_the_earlier_run_is_a_new_run(self) -> None:
        # f22b4dc N5 (the revision-run half): the same obligation, even the same task, does not restore a run
        for second_task in ("task-3", "task-1"):
            with self.subTest(task=second_task):
                sc = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
                r1 = author(sc, "v1\n", "task-1", obligation="obl-item")
                first = accept(sc, r1["id"])
                sc.admit(first)
                author(sc, "v2\n", "task-2", obligation="obl-item")
                author(sc, "v1\n", second_task, obligation="obl-item")
                self.assertEqual(sc.derive().current(first["id"]), F)


class RunGates(unittest.TestCase):
    def test_a_gate_decided_afresh_in_a_later_run_over_a_qualified_earlier_decision(self) -> None:
        # 575dc78 N5, f7419d5 N4 (the D1/D2 run variant): the earlier run's QUALIFIED decision on the same bytes
        # is no longer eligible after a revert; the new run's fresh UNQUALIFIED decision alone decides (T).
        sc = Scenario(MANIFEST, RUN_FILES, policy=POLICY)
        r1 = author(sc, "v1\n", "task-1")
        sc.admit(accept(sc, r1["id"]), gate(sc, r1["id"], HUMAN, "QUALIFIED"))
        self.assertEqual(sc.derive().valid("numerics"), P, "a qualified decision caps validity in its run")
        author(sc, "v2\n", "task-2")
        r3 = author(sc, "v1\n", "task-3")
        sc.admit(accept(sc, r3["id"]), gate(sc, r3["id"], HUMAN_B))
        self.assertEqual(sc.derive().valid("numerics"), T)

    def test_a_frame_decision_on_the_revision_its_frame_produces_counts_once_it_integrates(self) -> None:
        # The run a frame record names is its transformation's enactment when the transformation changes cur(s).
        sc = Scenario(MANIFEST, RUN_FILES, policy=POLICY)
        base, cand, x, merged = candidate(sc, {"numerics.md": "v1\n"})
        result = assessed_result(sc, base, cand, x, "task-1", agent("reviser"))
        sc.admit(result)
        new_rev = rev_in(sc, cand)
        frame = {"transformation": x}
        sc.admit(accept(sc, result["id"], frame=frame, rev=new_rev), gate(sc, result["id"], HUMAN, frame=frame, rev=new_rev))
        d = sc.derive()
        in_frame = Support(frame_state(d.s.h, d.s.n, x, d.s))
        self.assertEqual(in_frame.valid("numerics"), T, "in its own frame")
        self.assertEqual(d.valid("numerics"), F, "not before integration")
        sc.entries.append(admission_body(sc.position, base, cand, integrates=x))
        sc.files, sc.head = merged, cand
        self.assertEqual(sc.derive().valid("numerics"), T, "after integration the frame's run is the admitted run")

    def test_a_frame_decision_that_leaves_the_subject_names_the_admitted_run(self) -> None:
        # A frame X that leaves cur(s) unchanged: its decision names the admitted run and stays in it when X
        # integrates; after a later revert to the same bytes it is out of the run with every other earlier record.
        sc = Scenario(MANIFEST, RUN_FILES, policy=POLICY)
        r1 = author(sc, "v1\n", "task-1")
        sc.admit(accept(sc, r1["id"]))
        base, cand, x, merged = candidate(sc, {"notes.md": "n2\n"})
        notes = assessed_result(sc, base, cand, x, "task-n", agent("writer"), assess=False)
        sc.admit(notes)
        decision = gate(sc, r1["id"], HUMAN, "QUALIFIED", frame={"transformation": x})
        sc.admit(decision)
        sc.entries.append(admission_body(sc.position, base, cand, integrates=x))
        sc.files, sc.head = merged, cand
        d = sc.derive()
        self.assertEqual((d.current(decision["id"]), d.valid("numerics")), (T, P), "in the admitted run after integration")
        author(sc, "v2\n", "task-2")
        r3 = author(sc, "v1\n", "task-3")
        sc.admit(accept(sc, r3["id"]), gate(sc, r3["id"], HUMAN_B))
        d = sc.derive()
        self.assertEqual((d.current(decision["id"]), d.valid("numerics")), (F, T), "out of the run after the revert")

if __name__ == "__main__":
    unittest.main()
