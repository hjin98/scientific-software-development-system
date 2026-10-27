"""Phase F step 8g-i: retry, integration requests and §9.1's re-request (catalogue §9.1, §11.5 (3), §13.7; plan
§3.5, reading F73; plan checks of 53216046 and 25bd1d0d).

Retry composes what is built: a finished task whose obligation derivation still finds ``READY`` is issued again at
the new head, and once derivation stops routing it (its budget spent, §13.7) nothing is issued. An integrating request
is built from the candidate and the bound ``TASK_RESULT`` and is refused under SD-70. The Dispatcher acts on an
overtaken basis only after Admission's outcome: while it is pending no second task is issued for the obligation.
"""

from __future__ import annotations

import unittest
from unittest import mock

from ssds.admission.engine import gated
from ssds.derivation import Workflow, derive
from ssds.derivation.workflow import WAITING, Readiness
from ssds.dispatcher import issue, rerequest, would_issue
from ssds.dispatcher.journal import Journal
from ssds.dispatcher.requests import integration_request
from ssds.ledger.schema import transformation_id

from ._fixtures import commit, git, sshsig
from .test_admission_requests import finding, task_result
from .test_phase_f_step8a import Fixture

GOVERNS = {"mode": "LEGACY", "protocol": "7.2.1"}


class Dispatching(Fixture):
    def journal(self) -> Journal:
        return Journal(self.home, "demo")

    def issue_first(self):
        task = would_issue(self.chain(), self.trees, self.held())[0]
        return task, issue(self.journal(), self.issuer, task, self.held(), governs=GOVERNS, route="MANUAL")

    def move_head(self):
        """An admitted human finding: the head moves, the reviewer-held ``ACCEPT`` stays ``READY``."""

        from ssds.admission.request import request_message
        from ssds.ledger.read import with_id

        rec = with_id({**finding(note="the head moves"), "actor": self.human()})
        req = self.request([rec], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        decision = self.admit(req)
        self.assertEqual(decision.decision, "ACCEPT", decision.reasons)
        return decision

    def ready_again(self, task):
        return [t for t in would_issue(self.chain(), self.trees, self.held(), self.journal().open_tasks())
                if t.obligation_id == task.obligation_id]


class Retry(Dispatching):
    def test_a_finished_task_still_ready_is_issued_again_at_the_new_head(self) -> None:
        task, _ = self.issue_first()
        self.move_head()
        self.assertEqual(self.ready_again(task), [], "its task is open: no second task")
        self.journal().finished(task.task_id)
        (again,) = self.ready_again(task)
        self.assertNotEqual(again.task_id, task.task_id)
        self.assertEqual(again.task_id.split("-")[1], str(self.held().head), "issued at the new head")
        issue(self.journal(), self.issuer, again, self.held(), governs=GOVERNS, route="MANUAL")

    def test_nothing_is_issued_once_derivation_stops_routing_it(self) -> None:
        task, _ = self.issue_first()
        self.journal().finished(task.task_id)
        real = Workflow.readiness

        def spent(workflow, o):  # the budget spent: derivation routes it to coordination, not re-dispatch (§13.7)
            return Readiness(WAITING, ("budget",)) if o.id == task.obligation_id else real(workflow, o)

        with mock.patch.object(Workflow, "readiness", spent):
            self.assertEqual(self.ready_again(task), [])


class Integration(Fixture):
    def candidate(self) -> str:
        git(self.product, "checkout", "-q", "-b", "work")
        (self.product / "guide.md").write_text("# Guide\n\nRevised.\n")
        cand = commit(self.product, "candidate")
        git(self.product, "checkout", "-q", "-")
        return cand

    def test_an_integrating_request_is_built_and_refused(self) -> None:
        """Review of 26907956, B3: §11.5's two requests. The result is its own records-only request (admitted here
        with SD-70's gate lifted for it alone); the integrating request is the candidate plus references, carrying no
        record, and reaches the integration checks of the real owner, which SD-70 then refuses."""

        issued = self.issue("HARNESS")
        cand = self.candidate()
        x = transformation_id(self.baseline, cand, [])
        result = self.bind(task_result(x, base=self.baseline, candidate=cand, task=issued.envelope["task_id"]), issued)
        with mock.patch("ssds.admission.engine.gated", return_value=False):
            first = self.admit(self.signed(issued, [result]))
        self.assertEqual((first.decision, first.admitted), ("ACCEPT", (result["id"],)))
        self.assertIn(x, derive(self.chain(), self.trees).s.submissions, "the result is admitted and fixes X")
        position = len(self.entries()) - 1
        req = integration_request(issued, cand, position, self.baseline)
        self.assertEqual((req["candidates"], req["records"], req["base_position"], req["base_commit"]),
                         ([cand], [], position, self.baseline))
        self.assertEqual(req["binding"], issued.binding(req), "signed by the producing task's credential")
        with mock.patch("ssds.admission.engine.gated", return_value=False):
            lifted = self.admit(req)
        # the real owner finds the admitted result's X and judges the integration: this fixture's reviewer task has
        # no contract, so the candidate's own checks refuse it (§8.3 steps 3 and 7); SD-70's gate follows them
        self.assertEqual(lifted.reasons, ("AUTH_WRITE_SCOPE", "CONFORMANCE_FAILED", "OBLIGATION_PREDICATE_UNMET"))
        decision = self.admit({**req, "base_position": len(self.entries()) - 1,
                               "binding": issued.binding({**req, "base_position": len(self.entries()) - 1})})
        self.assertEqual((decision.decision, decision.admitted), ("REJECT", ()))
        self.assertNotIn("REF_TRANSFORMATION", decision.reasons)
        support = derive(self.chain(), self.trees)
        self.assertFalse(support.s.integrated, "nothing integrates")
        # SD-70 at its owner: even with every built check passing, a request carrying a candidate fails closed
        self.assertTrue(gated(req, req["records"], support, None))


class Rerequest(Dispatching):
    def test_the_dispatcher_acts_only_on_admissions_outcome(self) -> None:
        task, _ = self.issue_first()
        self.move_head()
        with self.assertRaisesRegex(ValueError, "Admission's outcome"):
            rerequest(self.journal(), task, None, self.chain(), self.trees, self.held())
        self.assertIn(task.task_id, {t["task_id"] for t in self.journal().open_tasks()}, "still open")
        self.assertEqual(self.ready_again(task), [], "pending revalidation: no duplicate task")

    def test_an_overtaken_basis_is_rederived_and_reissued_at_the_new_head(self) -> None:
        task, _ = self.issue_first()
        outcome = self.move_head()  # Admission's outcome at the moved head
        again = rerequest(self.journal(), task, outcome, self.chain(), self.trees, self.held())
        self.assertNotIn(task.task_id, {t["task_id"] for t in self.journal().open_tasks()}, "finished")
        self.assertIsNotNone(again)
        self.assertEqual((again.obligation_id, again.task_id.split("-")[1]),
                         (task.obligation_id, str(self.held().head)))
        self.assertNotEqual(again.task_id, task.task_id, "a new task; the old basis is never resubmitted")
        issued = issue(self.journal(), self.issuer, again, self.held(), governs=GOVERNS, route="MANUAL")
        self.assertEqual(issued.envelope["issued_at_position"], self.held().head)

    def test_nothing_is_issued_when_the_obligation_is_no_longer_ready(self) -> None:
        task, _ = self.issue_first()
        outcome = self.move_head()
        real = Workflow.readiness
        with mock.patch.object(Workflow, "readiness",
                               lambda w, o: Readiness("ANSWERED") if o.id == task.obligation_id else real(w, o)):
            self.assertIsNone(rerequest(self.journal(), task, outcome, self.chain(), self.trees, self.held()))
        self.assertEqual(self.journal().open_tasks(), [], "the old task is finished")

    def test_only_its_own_obligation_is_reissued(self) -> None:
        import dataclasses

        task, _ = self.issue_first()
        outcome = self.move_head()
        other = dataclasses.replace(task, task_id="task-9-other", obligation_id="sha256:" + "6" * 64)
        with mock.patch("ssds.dispatcher.requests.ready", return_value=(other,)):
            self.assertIsNone(rerequest(self.journal(), task, outcome, self.chain(), self.trees, self.held()),
                              "another obligation's readiness re-requests nothing")


if __name__ == "__main__":
    unittest.main()
