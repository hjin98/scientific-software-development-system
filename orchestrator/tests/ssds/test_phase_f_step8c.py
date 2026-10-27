"""Phase F step 8c: scheduling constraints (catalogue §9.1-§9.2, §12.5, K2; plan §3.5, reading F67).

Serialization surfaces are a policy key: at most one open task whose write scope meets a surface, a unit meeting a
surface when one contains the other. Every change plan is a surface for coordination: at most one open coordination
task per plan. Per-worktree leases give one mutating execution per worktree, and their expiry changes scheduling,
never correctness. A suspended task stays open and resumes by its identity. The principal is an agent role (§12.3).
"""

from __future__ import annotations

import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from ssds.derivation import AGENT_ROLES, READY, Workflow, derive
from ssds.derivation.state import Policy
from ssds.dispatcher import Leases, NotIssuable, Task, issuable, issue, observe, would_issue
from ssds.dispatcher.journal import Journal

from .test_phase_f_step8a import Fixture

GOVERNS = {"mode": "LEGACY", "protocol": "7.2.1"}
SRC = Path(__file__).resolve().parents[2] / "src" / "ssds"


def task(n: int, surfaces=(), plan=None, obligation=None) -> Task:
    return Task(f"task-1-{n:016x}", obligation or f"sha256:{n:064x}", "IMPLEMENT", "IMPLEMENTER",
                {"unit": "u", "rev": "r"}, tuple(surfaces), plan)


def open_task(t: Task) -> dict:
    return {"task_id": t.task_id, "obligation_id": t.obligation_id, "surfaces": list(t.surfaces), "plan": t.plan}


class PolicyKey(unittest.TestCase):
    def test_serialization_surfaces_are_a_list_of_unit_ids(self) -> None:
        policy = Policy.parse(b'schema = 1\n[workflow]\nserialization_surfaces = ["guide", "src"]\n')
        self.assertEqual(policy.flow("serialization_surfaces"), ("guide", "src"))
        self.assertEqual(Policy.parse(b"schema = 1\n").flow("serialization_surfaces"), ())
        with self.assertRaises(ValueError):
            Policy.parse(b'schema = 1\n[workflow]\nserialization_surfaces = "guide"\n')

    def test_the_principal_is_an_agent_role(self) -> None:
        """§12.3: the principal's R1 role template holds COORDINATE and CONTRACT; tasks issue to it."""

        self.assertEqual(AGENT_ROLES, {"PRINCIPAL", "IMPLEMENTER", "INVESTIGATOR", "REVIEWER"})


class Scheduling(unittest.TestCase):
    def test_one_open_task_per_surface(self) -> None:
        allowed, held = issuable((task(1, ["guide"]), task(2, ["guide"]), task(3, ["src"])), ())
        self.assertEqual([t.task_id for t in allowed], [task(1).task_id, task(3).task_id])
        self.assertIn("serialization surface guide", held[0][1])
        allowed, held = issuable((task(4, ["guide"]),), (open_task(task(1, ["guide"])),))
        self.assertEqual((allowed, held[0][0].task_id), ((), task(4).task_id))

    def test_one_open_coordination_task_per_plan(self) -> None:
        allowed, held = issuable((task(1, plan="plan-a"), task(2, plan="plan-a"), task(3, plan="plan-b"), task(4)), ())
        self.assertEqual([t.task_id for t in allowed], [task(1).task_id, task(3).task_id, task(4).task_id])
        self.assertIn("plan plan-a", held[0][1])

    def test_no_second_task_for_an_open_obligation(self) -> None:
        first = task(1, obligation="sha256:" + "a" * 64)
        allowed, held = issuable((task(2, obligation="sha256:" + "a" * 64),), (open_task(first),))
        self.assertEqual((allowed, held[0][1]), ((), "its obligation has a task open"))

class JointInvariant(Fixture):
    def test_a_joint_invariant_review_is_scheduled_as_a_system_task(self) -> None:
        """§9.2's joint-invariant reviews, which derivation derives, are issued like any judgment (SD-77)."""

        made = SimpleNamespace(id="sha256:" + "9" * 64, kind="JOINT_INVARIANT", holder="REVIEWER", plan=None)
        fake = SimpleNamespace(obligations=[made], readiness=lambda o: SimpleNamespace(state=READY),
                               contract_revision=lambda o: {"system": o.kind, "version": "ssds-rules/1"},
                               serialization=lambda o: ((), None))
        with mock.patch("ssds.dispatcher.schedule.Workflow", return_value=fake):
            (only,) = would_issue(self.chain(), self.trees, self.held())
        self.assertEqual(only.contract_revision, {"system": "JOINT_INVARIANT", "version": "ssds-rules/1"})


class Surfaces(Fixture):
    POLICY = ('schema = 1\n[domains.D3]\nhumans = ["human:SHA256:carol"]\n'
              '[workflow]\nserialization_surfaces = ["guide", "ssds.policy", "nowhere"]\n')

    def test_a_write_unit_meets_a_surface_that_contains_it_or_that_it_contains(self) -> None:
        w = Workflow(derive(self.chain(), self.trees))
        o = next(o for o in w.obligations if o.kind == "ACCEPT")
        for writes, met in (({"guide.intro"}, ("guide",)), ({"guide"}, ("guide",)), ({"src"}, ())):
            with self.subTest(writes=writes), mock.patch.object(w, "item_of",
                                                                return_value=SimpleNamespace(write_units=writes)):
                self.assertEqual(w.serialization(o), (met, None))
        self.assertEqual(w.serialization(o), ((), None), "a judgment writes nothing")

    def test_a_principals_task_serializes_on_its_plan(self) -> None:
        w = Workflow(derive(self.chain(), self.trees))
        coordinate = SimpleNamespace(holder="PRINCIPAL", plan="plan-a", kind="COORDINATE")
        with mock.patch.object(w, "item_of", return_value=None):
            self.assertEqual(w.serialization(coordinate), ((), "plan-a"))


class JournalStates(Fixture):
    def issued(self):
        t = would_issue(self.chain(), self.trees, self.held())[0]
        return t, issue(Journal(self.home, "demo"), self.issuer, t, self.held(), governs=GOVERNS, route="MANUAL")

    def test_a_finished_task_frees_its_obligation(self) -> None:
        t, _ = self.issued()
        journal = Journal(self.home, "demo")
        self.assertEqual(would_issue(self.chain(), self.trees, self.held(), journal.open_tasks()), ())
        journal.finished(t.task_id)
        self.assertEqual([x.task_id for x in would_issue(self.chain(), self.trees, self.held(), journal.open_tasks())],
                         [t.task_id])

    def test_a_suspended_task_stays_open_and_resumes_by_identity(self) -> None:
        t, _ = self.issued()
        journal = Journal(self.home, "demo")
        journal.suspend(t.task_id, "BLOCKER sha256:" + "b" * 64)
        self.assertEqual(journal.suspended(), {t.task_id})
        self.assertIn(t.task_id, [x["task_id"] for x in journal.open_tasks()])
        with self.assertRaises(NotIssuable):
            issue(journal, self.issuer, t, self.held(), governs=GOVERNS, route="MANUAL")
        with self.assertRaises(ValueError):
            journal.suspend(t.task_id, "again")
        issued_before = sum(1 for e in journal.entries() if e["kind"] == "ISSUED")
        journal.resume(t.task_id)
        self.assertEqual(journal.suspended(), frozenset())
        self.assertEqual(sum(1 for e in journal.entries() if e["kind"] == "ISSUED"), issued_before, "no new envelope")
        with self.assertRaises(ValueError):
            journal.resume(t.task_id)

    def test_observe_reports_what_is_held(self) -> None:
        report = observe(self.chain(), self.trees, self.held())
        self.assertIn("held", report)
        self.assertTrue(report["would_issue"])


class Lease(Fixture):
    def test_one_execution_per_worktree_and_expiry_changes_only_scheduling(self) -> None:
        leases = Leases(self.home, "demo")
        self.assertTrue(leases.acquire("wt:1", "task-a", now=0, ttl=10))
        self.assertFalse(leases.acquire("wt:1", "task-b", now=5, ttl=10), "a live lease of another task")
        self.assertTrue(leases.acquire("wt:2", "task-b", now=5, ttl=10), "another worktree")
        self.assertTrue(leases.acquire("wt:1", "task-a", now=6, ttl=10), "its own task renews")
        self.assertTrue(leases.acquire("wt:1", "task-b", now=20, ttl=10), "after expiry")
        self.assertEqual(leases.holder("wt:1", now=21), "task-b")
        leases.release("wt:1", "task-b")
        self.assertIsNone(leases.holder("wt:1", now=22))

    def test_nothing_admission_or_derivation_reads_depends_on_a_lease(self) -> None:
        """Leases are the Dispatcher's operational facts (§3.1, §9.1): no Admission or derivation module reads them."""

        import re

        importing = re.compile(r"^\s*(from|import)\s+(ssds\.dispatcher|\.\.dispatcher)", re.MULTILINE)
        for owner in ("admission", "derivation", "ledger"):
            for path in (SRC / owner).rglob("*.py"):
                with self.subTest(path=str(path.relative_to(SRC))):
                    self.assertIsNone(importing.search(path.read_text()))


if __name__ == "__main__":
    unittest.main()
