"""Phase F step 8e: the task-bound interface (catalogue §16.1, §16.4; plan §3.5, reading F69).

``open(task)`` finds the issued envelope and renders the task's brief at its basis (the envelope's
``issued_at_position``), refusing a brief whose digest is not the envelope's. ``read`` during a task answers at the
basis and records the read in the task's basis; the brief says whether its route observes reads. ``ask(changed)``
defaults to the task's basis and its work's subjects.
"""

from __future__ import annotations

import unittest

from ssds.cli import HomeAccess
from ssds.dispatcher import brief_for, issue, would_issue
from ssds.dispatcher.journal import Journal
from ssds.interface.operations import Refused, Session

from .test_admission_requests import finding
from .test_phase_f_step8a import Fixture

GOVERNS = {"mode": "LEGACY", "protocol": "7.2.1"}


class TaskBound(Fixture):
    def issued(self, route: str = "MANUAL", brief: bytes | None = None):
        task = would_issue(self.chain(), self.trees, self.held())[0]
        text = brief if brief is not None else brief_for(self.chain(), self.trees, self.held(), task, route)
        issued = issue(Journal(self.home, "demo"), self.issuer, task, self.held(), governs=GOVERNS, route=route,
                       brief=text)
        return task, issued

    def session(self) -> Session:
        return Session(HomeAccess(self.home, "demo"), self.trees)

    def test_open_renders_the_issued_brief_at_its_basis(self) -> None:
        task, issued = self.issued()
        opened = self.session().open_task(task.task_id, Journal(self.home, "demo"))
        self.assertEqual(opened["answer"]["digest"], issued.envelope["brief"])
        self.assertIn(f"ISSUED task {task.task_id} on route MANUAL", opened["answer"]["text"])
        self.assertEqual(opened["head"]["position"], issued.envelope["issued_at_position"])

    def test_a_brief_that_is_not_the_issued_one_is_refused(self) -> None:
        task, _ = self.issued(brief=b"another brief")
        with self.assertRaisesRegex(Refused, "not the"):
            self.session().open_task(task.task_id, Journal(self.home, "demo"))

    def test_only_a_task_handed_out_is_opened(self) -> None:
        with self.assertRaisesRegex(Refused, "no task"):
            self.session().open_task("task-0-unknown", Journal(self.home, "demo"))

    def test_an_envelope_never_handed_out_is_not_opened(self) -> None:
        from unittest import mock

        task = would_issue(self.chain(), self.trees, self.held())[0]
        with mock.patch.object(Journal, "handed", side_effect=OSError("crash")), self.assertRaises(OSError):
            issue(Journal(self.home, "demo"), self.issuer, task, self.held(), governs=GOVERNS, route="MANUAL")
        with self.assertRaisesRegex(Refused, "no task"):
            self.session().open_task(task.task_id, Journal(self.home, "demo"))

    def test_answers_stay_at_the_basis_as_the_head_moves(self) -> None:
        from ssds.admission.engine import Admission

        from ._fixtures import commit

        task, issued = self.issued()
        before = (self.product / "guide.md").read_text()
        (self.product / "guide.md").write_text(before + "\nA later paragraph.\n")
        moved = commit(self.product, "the product moves")
        Admission(self.home, "demo", self.trees, product=self.product).admit(self.signed_by_human_finding("later"), moved)
        session = self.session()
        self.assertEqual(session.read_task(task.task_id, "guide.md", Journal(self.home, "demo"))["answer"]["content"],
                         before, "read at the basis, not at the absorbed head")
        self.assertGreater(session.presented.head["position"], issued.envelope["issued_at_position"])
        opened = session.open_task(task.task_id, Journal(self.home, "demo"))
        self.assertEqual(opened["answer"]["digest"], issued.envelope["brief"], "the same brief at the basis")
        changed = session.changed_since_basis(task.task_id, Journal(self.home, "demo"))
        self.assertEqual(changed["query"], "changed")

    def signed_by_human_finding(self, note: str):
        from ssds.admission.request import request_message
        from ssds.ledger.read import with_id

        from ._fixtures import sshsig

        rec = with_id({**finding(note=note), "actor": self.human()})
        req = self.request([rec], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return req

    def test_reads_are_recorded_in_the_tasks_basis(self) -> None:
        task, _ = self.issued()
        journal = Journal(self.home, "demo")
        session = self.session()
        unit = session.read_task(task.task_id, "guide", journal)
        self.assertEqual(unit["answer"]["unit"], "guide")
        path = session.read_task(task.task_id, "guide.md", journal)
        self.assertIn("content", path["answer"])
        reads = Journal(self.home, "demo").reads(task.task_id)
        self.assertEqual(reads[0], {"unit": "guide", "rev": unit["answer"]["rev"]})
        self.assertEqual(reads[1]["path"], "guide.md")
        self.assertTrue(reads[1]["digest"].startswith("sha256:"))
        with self.assertRaises(Refused):
            session.read_task(task.task_id, "nowhere", journal)
        self.assertEqual(len(Journal(self.home, "demo").reads(task.task_id)), 2, "a refused read records nothing")

    def test_the_brief_says_whether_its_route_observes_reads(self) -> None:
        for route, says in (("HARNESS", "reads observed"), ("MANUAL", "reads not observed (route MANUAL)")):
            with self.subTest(route=route):
                task = would_issue(self.chain(), self.trees, self.held())[0]
                self.assertIn(says, brief_for(self.chain(), self.trees, self.held(), task, route).decode())


if __name__ == "__main__":
    unittest.main()
