"""Phase E step 4a: conformance of a task result at the derivation owner (catalogue §14.1-§14.6, §11.5).

Expected classes are written from §14.4's table and the templates' definitions in §14.3, never computed by
the rule under test.
"""

from __future__ import annotations

import hashlib
import unittest

from ssds.derivation.conformance import CLEAN, DISCREPANCY, INCOMPLETE, SIGNAL, VIOLATION
from ssds.derivation.workflow import DISCHARGED, OPEN, READY, Workflow
from ssds.ledger.read import with_id

from ._fixtures import record, tree
from ._scenario import OWNER, Scenario, agent, content, fresh, judgment
from .test_lint import FILES, MANIFEST, item_block, plan_text

SECONDARY = '[ { check = "BOUNDARY.write_scope" }, { check = "TEST_INTEGRITY.evidence_specs_untouched" } ]'
SLOTS = {"claims": [{"claim": "the solver adapts", "records": []}], "unverified_assumptions": {"none": "NONE_MADE"},
         "deviations": {"none": "NO_DEVIATION"}}


def accepted_plan(block: str | None = None) -> Scenario:
    sc = Scenario(MANIFEST, {**FILES, "plans/work.md": plan_text(block or item_block(secondary=SECONDARY))})
    objective, item = sc.rev("plan.work.objective"), sc.rev("plan.work.item")
    sc.admit(judgment("PLAN_ACCEPTANCE", {"units": ["plan.work"]}, "ACCEPTED", actor=OWNER,
                      basis=[content("plan.work.objective", objective), content("plan.work.item", item, "PLAN_CONTROL")],
                      fields={"objective": {"unit": "plan.work.objective", "rev": objective},
                              "items": [{"unit": "plan.work.item", "rev": item}]}))
    return sc


def submit(sc: Scenario, files: dict[str, str], slots: dict | None = None, outcome: str = "COMPLETE",
           task: str = "task-1", producer: str = agent("maker")) -> tuple[str, str, dict]:
    base = sc.head
    merged = dict(sc.files, **files)
    cand = sc.add_tree(tree(merged, sc.manifest))
    x = "sha256:" + hashlib.sha256(f"ssds.transformation.v1|{base}|{cand}".encode()).hexdigest()
    result = record("TASK_RESULT", target={"task": task, "candidate": cand, "transformation": x, "base": base},
                    outcome=outcome, actor=producer, actor_class="AGENT", frame={"transformation": x},
                    fields={"slots": SLOTS if slots is None else slots})
    result["binding"] = dict(fresh(producer, task), obligation="obl-item",
                             contract_revision={"unit": "plan.work.item", "rev": sc.rev("plan.work.item")})
    result = with_id(result)
    sc.admit(result)
    return x, cand, result


def realize(sc: Scenario, candidate: str, outcome: str = "PASS") -> None:
    spec_rev = sc.rev("tests.conv")
    real = with_id(record("REALIZATION", target={"spec": {"unit": "tests.conv", "rev": spec_rev}, "claim": []},
                          outcome="COMPLETE", actor="machinery:runner-ci", actor_class="MACHINERY",
                          fields={"execution": {"tree": candidate, "units": [], "reads": []}, "configuration": {}}))
    sc.admit(real)
    sc.admit(judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": "o1"}, outcome,
                      actor=OWNER, fields={"mode": "ORDINARY", "reading": {"unit": "tests.conv", "rev": spec_rev}}))


def conformance(sc: Scenario, result: dict):
    w = Workflow(sc.derive())
    return w, w.conformance(result["id"])


class Classes(unittest.TestCase):
    def test_clean_and_review_follows(self) -> None:
        sc = accepted_plan()
        x, cand, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"})
        realize(sc, cand)
        w, c = conformance(sc, result)
        self.assertEqual(c.classes, frozenset({CLEAN}), c.hits)
        (review,) = w.of_kind("REVIEW")
        self.assertEqual((review.target, w.readiness(review).state), ({"transformation": x}, READY))

    def test_missing_evidence_is_incomplete_and_a_complete_outcome_then_discrepant(self) -> None:
        sc = accepted_plan()
        _, _, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"})
        w, c = conformance(sc, result)
        self.assertEqual(c.classes, frozenset({INCOMPLETE, DISCREPANCY}), "a set: no class takes precedence")
        self.assertEqual(w.of_kind("REVIEW"), [], "REVIEW(X) is ready only once conformance is CLEAN")

    def test_partial_outcome_with_missing_evidence_is_only_incomplete(self) -> None:
        sc = accepted_plan()
        _, _, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"}, outcome="PARTIAL")
        self.assertEqual(conformance(sc, result)[1].classes, frozenset({INCOMPLETE}))

    def test_an_undisclosed_breach_is_violation_and_discrepancy_a_disclosed_one_violation(self) -> None:
        sc = accepted_plan()
        _, cand, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n", "records.md": "# Records changed\n"})
        realize(sc, cand)
        self.assertEqual(conformance(sc, result)[1].classes, frozenset({VIOLATION, DISCREPANCY}))
        sc2 = accepted_plan()
        slots = dict(SLOTS, deviations=[{"unit": "records", "reason": "SCOPE_DEVIATION"}])
        _, cand2, result2 = submit(sc2, {"src/solver.py": "def step():\n    return 2\n", "records.md": "# Records changed\n"},
                                   slots=slots)
        realize(sc2, cand2)
        self.assertEqual(conformance(sc2, result2)[1].classes, frozenset({VIOLATION}))

    def test_a_d3_unit_in_an_implement_write_set_is_a_violation(self) -> None:
        block = item_block(secondary=SECONDARY, write_scope='["src/", "design.md"]', affected='["src/", "design.md"]')
        sc = accepted_plan(block)
        _, cand, result = submit(sc, {"design.md": "# Design changed\n"})
        realize(sc, cand)
        c = conformance(sc, result)[1]
        self.assertIn(VIOLATION, c.classes)
        self.assertTrue(any("only an AUTHOR item" in h.finding for h in c.hits))

    def test_an_evidence_specification_outside_evidence_specs_is_a_violation(self) -> None:
        block = item_block(secondary=SECONDARY, write_scope='["src/", "specs/conv.toml"]', affected='["src/", "specs/"]')
        sc = accepted_plan(block)
        _, cand, result = submit(sc, {"specs/conv.toml": "kind = 'weaker'\n"})
        realize(sc, cand)
        c = conformance(sc, result)[1]
        self.assertTrue(any(h.template == "TEST_INTEGRITY.evidence_specs_untouched" and h.cls == VIOLATION for h in c.hits))

    def test_an_empty_required_slot_is_incomplete(self) -> None:
        sc = accepted_plan()
        _, cand, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"},
                                 slots=dict(SLOTS, unverified_assumptions=[]), outcome="PARTIAL")
        realize(sc, cand)
        c = conformance(sc, result)[1]
        self.assertEqual(c.classes, frozenset({INCOMPLETE}))
        self.assertTrue(any(h.template == "OBLIGATION.slots_filled" and h.cls == INCOMPLETE for h in c.hits))

    def test_a_runner_template_reads_its_observation(self) -> None:
        secondary = SECONDARY[:-2] + ', { check = "OBLIGATION.mutation_strength" } ]'
        for outcome, expected in ((None, INCOMPLETE), ("CLEAN", CLEAN), ("VIOLATION", INCOMPLETE)):
            with self.subTest(outcome=outcome):
                sc = accepted_plan(item_block(secondary=secondary))
                _, cand, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"}, outcome="PARTIAL")
                realize(sc, cand)
                if outcome is not None:
                    for ob in ("o1", "o2"):
                        sc.admit(with_id(record("CHECK_EXECUTION", target={"obligation": ob, "candidate": cand},
                                                outcome=outcome, actor="machinery:runner-ci", actor_class="MACHINERY",
                                                fields={"template": "OBLIGATION.mutation_strength", "tool": "mutmut-2"})))
                c = conformance(sc, result)[1]
                mutation = {h.cls for h in c.hits if h.template == "OBLIGATION.mutation_strength"}
                self.assertEqual(mutation, {expected})

    def test_signals_change_no_disposition(self) -> None:
        # §14.3: removing every HEURISTIC template leaves every admission decision and discharge unchanged.
        sc = accepted_plan()
        slots = dict(SLOTS, claims=[{"claim": "this proves the solver is 2.5 times faster", "records": []}])
        _, cand, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"}, slots=slots)
        realize(sc, cand)
        c = conformance(sc, result)[1]
        self.assertIn(SIGNAL, c.classes)
        self.assertTrue(c.clean)
        failing = {h.cls for h in c.hits if h.cls not in (CLEAN, SIGNAL)}
        self.assertEqual(failing, set())

    def test_citations_and_governing_basis(self) -> None:
        sc = accepted_plan(item_block(secondary=SECONDARY, extra_item=f'governing = ["design@sha256:{"b" * 64}"]'))
        slots = dict(SLOTS, claims=[{"claim": "measured", "records": ["sha256:" + "e" * 64]}])
        _, cand, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"}, slots=slots)
        realize(sc, cand)
        c = conformance(sc, result)[1]
        templates = {h.template for h in c.hits if h.cls == DISCREPANCY}
        self.assertEqual(templates, {"FAITHFULNESS.citations_support", "FAITHFULNESS.governing_at_basis"})


class ReviewOfX(unittest.TestCase):
    def test_review_answered_and_discharged_in_its_frame(self) -> None:
        sc = accepted_plan()
        x, cand, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"})
        realize(sc, cand)
        w = Workflow(sc.derive())
        (review,) = w.of_kind("REVIEW")
        self.assertEqual(w.discharge(review), OPEN)
        verdict = judgment("REVIEW", {"transformation": x}, "PASS", actor=agent("checker"), actor_class="AGENT",
                           basis=[content("src", sc.view(cand).rev("src"))], frame={"transformation": x},
                           binding=dict(fresh(agent("checker"), "task-r"), obligation=review.id))
        sc.admit(verdict)
        w = Workflow(sc.derive())
        self.assertEqual(w.answer(review), verdict["id"])
        self.assertEqual(w.discharge(review), DISCHARGED)

    def test_the_authors_review_does_not_answer(self) -> None:
        sc = accepted_plan()
        x, cand, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"})
        realize(sc, cand)
        w = Workflow(sc.derive())
        (review,) = w.of_kind("REVIEW")
        own = judgment("REVIEW", {"transformation": x}, "PASS", actor=agent("maker"), actor_class="AGENT",
                       basis=[content("src", sc.view(cand).rev("src"))], frame={"transformation": x},
                       binding=dict(fresh(agent("maker"), "task-r"), obligation=review.id))
        sc.admit(own)
        self.assertIsNone(Workflow(sc.derive()).answer(review))


if __name__ == "__main__":
    unittest.main()
