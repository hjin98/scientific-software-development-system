"""Phase F step 5c: result conformance at Admission (catalogue §8.3 step 7; plan §3.2, reading F30).

The result-only ``HARD`` templates (``slots_filled``, ``outcome_consistent`` over those alone, ``citations_support``)
are evaluated on the trial; when one yields ``INCOMPLETE`` or ``DISCREPANCY``, every passing judgment and principal
decision record in the request is refused alone (``CONFORMANCE_RESULT``) and the result and never-lost records
stand. Under SD-70 a request carrying a ``TASK_RESULT`` is not accepted in Phase F, so the decision function and
the conformance owner are tested on derivation histories.
"""

from __future__ import annotations

import unittest

from ssds.admission.legality import conformance_alone
from ssds.derivation.conformance import CLEAN, DISCREPANCY, INCOMPLETE
from ssds.ledger.read import with_id

from ._fixtures import record
from ._scenario import HUMAN, OWNER, judgment
from .test_conformance import SLOTS, accepted_plan, conformance, realize, submit
from .test_phase_f_step4c import AdmissionRequests

SOLVED = {"src/solver.py": "def step():\n    return 2\n"}


def classes(hits) -> dict[str, str]:
    return {h.template: h.cls for h in hits if h.cls != CLEAN}


class ResultOnly(unittest.TestCase):
    def test_unmet_required_evidence_is_not_a_result_only_discrepancy(self) -> None:
        sc = accepted_plan()
        _, _, result = submit(sc, SOLVED)
        c = conformance(sc, result)[1]
        self.assertEqual(c.classes, frozenset({INCOMPLETE, DISCREPANCY}), "the full templates: evidence unmet")
        self.assertEqual(classes(c.result_only), {}, "F30: evidence is met only after a runner runs")

    def test_an_empty_required_slot_fails_result_only(self) -> None:
        sc = accepted_plan()
        _, cand, result = submit(sc, SOLVED, slots=dict(SLOTS, unverified_assumptions=[]))
        realize(sc, cand)
        c = conformance(sc, result)[1]
        self.assertEqual(classes(c.result_only), {"OBLIGATION.slots_filled": INCOMPLETE,
                                                  "FAITHFULNESS.outcome_consistent": DISCREPANCY})
        _, _, partial = submit(sc, SOLVED, slots=dict(SLOTS, unverified_assumptions=[]), outcome="PARTIAL",
                               task="task-2")
        self.assertEqual(classes(conformance(sc, partial)[1].result_only), {"OBLIGATION.slots_filled": INCOMPLETE})

    def test_a_citation_of_no_record_fails_result_only(self) -> None:
        sc = accepted_plan()
        slots = dict(SLOTS, claims=[{"claim": "measured", "records": ["sha256:" + "e" * 64]}])
        _, _, result = submit(sc, SOLVED, slots=slots)
        self.assertEqual(classes(conformance(sc, result)[1].result_only),
                         {"FAITHFULNESS.citations_support": DISCREPANCY})


class Refusal(unittest.TestCase):
    """``CONFORMANCE_RESULT`` refuses passing judgments and principal decisions alone; the rest stands."""

    def records(self, sc, result):
        passing = judgment("REVIEW", {"transformation": result["target"]["transformation"]}, "PASS", actor=HUMAN,
                           frame={"transformation": result["target"]["transformation"]})
        adverse = judgment("REVIEW", {"transformation": result["target"]["transformation"]}, "NO_PASS", actor=HUMAN,
                           frame={"transformation": result["target"]["transformation"]})
        decision = with_id({**record("COORDINATION_DECISION", target={"records": []}, outcome="DECLINE",
                                     fields={"tasks": []}), "actor": OWNER})
        report = with_id({**record("FINDING", target={"units": ["plan.work"]}, fields={"materiality": "ROUTINE"}),
                          "actor": HUMAN})
        return [result, passing, adverse, decision, report]

    def test_a_failing_result_refuses_passing_judgments_and_decisions(self) -> None:
        sc = accepted_plan()
        _, _, result = submit(sc, SOLVED, slots=dict(SLOTS, unverified_assumptions=[]))
        recs = self.records(sc, result)
        refused = dict(conformance_alone(recs, sc.derive()))
        self.assertEqual(refused, {recs[1]["id"]: ("CONFORMANCE_RESULT",), recs[3]["id"]: ("CONFORMANCE_RESULT",)},
                         "the result, the adverse review and the report stand")

    def test_a_clean_result_refuses_nothing(self) -> None:
        sc = accepted_plan()
        _, _, result = submit(sc, SOLVED)  # evidence unmet, but result-only clean (F30)
        self.assertEqual(conformance_alone(self.records(sc, result), sc.derive()), [])

    def test_no_result_no_check(self) -> None:
        sc = accepted_plan()
        _, _, result = submit(sc, SOLVED, slots=dict(SLOTS, unverified_assumptions=[]))
        self.assertEqual(conformance_alone(self.records(sc, result)[1:], sc.derive()), [])
        self.assertEqual(conformance_alone(self.records(sc, result), None), [])



class Engine(AdmissionRequests):
    def test_a_co_submitted_results_conformance_refuses_a_passing_judgment_alone(self) -> None:
        from ssds.content import read_tree
        from ssds.derivation import derive
        from ssds.ledger.read import read_chain

        from ._fixtures import view as tree_view
        from ._scenario import content

        changed = "# Guide\n\n## Introduction\n\nHello again.\n\n## Usage\n\nRun it.\n"
        cand = self.candidate({"guide.md": changed})
        result = self.submitting(cand)  # a human's result naming no contract: slots_filled INCOMPLETE
        x = result["target"]["transformation"]
        admitted = derive(read_chain(self.f.home.ledger_repository("demo"), "demo"), self.f.trees).s
        frame_rev = tree_view(read_tree(self.f.product, cand)).rev("guide")
        passing = self.acceptance(x, "guide", admitted.subject_triple("guide")[1], frame_rev,
                                  basis=[content("guide", frame_rev)])
        refused = dict(self.admit([result, passing]).refused)
        self.assertEqual(refused.get(passing["id"]), ("CONFORMANCE_RESULT",))
        self.assertNotEqual(refused.get(result["id"]), ("CONFORMANCE_RESULT",), "the result itself is not")


if __name__ == "__main__":
    unittest.main()
