"""Phase F step 8a: the Dispatcher at a named ``H*`` (catalogue §9, §23.4; plan §3.5, reading F65).

The ledger's currentness has one composition, in the Ledger Store, which Admission, the Interface and the Dispatcher
call. The Dispatcher issues only at a ``QUALIFIED`` head with no provisional entry; its would-issue set is every
agent-held obligation derivation finds ``READY`` there. Issuing is written ahead, intent then effect then hand-out,
and a restart abandons any intent never handed out. ``dispatcher serve`` is observe-only on a shadow ledger (F8).
"""

from __future__ import annotations

import json
import unittest
from unittest import mock

from ssds.derivation import AGENT_ROLES, READY, Workflow, derive
from ssds.dispatcher import NotIssuable, Task, issue, observe, task_id, would_issue
from ssds.dispatcher.journal import Journal
from ssds.ledger.qualification import Qualification, currentness
from ssds.ledger.read import read_chain

from .test_admission_requests import RequestFixture


class Fixture(RequestFixture):
    """The request fixture, its baseline's policy naming a human for the D3 domain, so the reviewer-held
    ``ACCEPT`` has an eligible judge and is ``READY`` (§16.5): the baseline's authorship is unknown, so no fresh
    agent reviewer is eligible for it."""

    POLICY = 'schema = 1\n[domains.D3]\nhumans = ["human:SHA256:carol"]\n'

    def setUp(self) -> None:
        from unittest import mock as _mock

        from ssds.admission.engine import Admission
        from ssds.admission.genesis import admit_genesis, prepare_genesis

        from ._fixtures import commit, sshsig
        from .test_admission_genesis import GenesisFixture

        GenesisFixture.setUp(self)
        (self.product / ".ssds" / "policy.toml").write_text(self.POLICY)
        self.baseline = commit(self.product, "policy names a human judge")
        native = {"guide": {"mode": "NATIVE", "ruleset": "ssds-rules/1"}, "*": {"mode": "UNGOVERNED"}}
        with _mock.patch("ssds.admission.genesis.SHADOW_MODES", ("LEGACY", "UNGOVERNED", "NATIVE")):
            prepared = prepare_genesis(self.spec(modes=native), self.home, self.trees)
            admit_genesis(self.home, "demo", sshsig(self.private, prepared.message))
        self.admission = Admission(self.home, "demo", self.trees)
        self.issuer = self.register_issue_key()

    def chain(self):
        return read_chain(self.home.ledger_repository("demo"), "demo")

    def held(self):
        return self.admission.qualification(self.chain())


class Currentness(Fixture):
    def test_one_composition_for_every_reader(self) -> None:
        from ssds.cli import HomeAccess
        from ssds.interface.operations import present

        held = self.held()
        presented = present(HomeAccess(self.home, "demo"), self.trees).qualification
        self.assertEqual((held.state, held.head), (presented.state, presented.head))
        self.assertEqual(held.state, "QUALIFIED")

    def test_an_empty_chain_is_unqualified(self) -> None:
        empty = self.chain().__class__("demo", ())
        self.assertEqual(currentness(empty, {}, {}).state, "UNQUALIFIED")


class WouldIssue(Fixture):
    def test_the_would_issue_set_is_every_ready_agent_held_obligation(self) -> None:
        held = self.held()
        tasks = would_issue(self.chain(), self.trees, held)
        workflow = Workflow(derive(self.chain(), self.trees))
        expected = sorted(o.id for o in workflow.obligations
                          if o.holder in AGENT_ROLES and workflow.readiness(o).state == READY)
        self.assertTrue(expected, "the fixture's NATIVE subject derives a reviewer-held obligation")
        self.assertEqual(sorted(t.obligation_id for t in tasks), expected)
        for t in tasks:
            self.assertEqual(t.task_id, task_id(t.obligation_id, held.head), "stable across a restart")
            self.assertEqual(t.contract_revision, {"system": t.kind, "version": "ssds-rules/1"} if "unit" not in
                             t.contract_revision else t.contract_revision)

    def test_only_ready_agent_held_obligations_become_tasks(self) -> None:
        from types import SimpleNamespace

        held = self.held()
        made = [SimpleNamespace(id=f"sha256:{i:064x}", kind=k, holder=h) for i, (k, h) in enumerate(
            (("ACCEPT", "REVIEWER"), ("REVIEW", "REVIEWER"), ("GATE", "HUMAN"), ("REISSUE", "DISPATCHER"),
             ("IMPLEMENT", "IMPLEMENTER")))]
        states = {made[0].id: READY, made[1].id: "WAITING", made[2].id: READY, made[3].id: READY, made[4].id: READY}
        fake = SimpleNamespace(obligations=made, readiness=lambda o: SimpleNamespace(state=states[o.id]),
                               contract_revision=lambda o: {"unit": "u", "rev": "r"} if o.kind == "IMPLEMENT" else
                               {"system": o.kind, "version": "v"}, serialization=lambda o: ((), None))
        with mock.patch("ssds.dispatcher.schedule.Workflow", return_value=fake):
            tasks = would_issue(self.chain(), self.trees, held)
        self.assertEqual([(t.kind, t.contract_revision) for t in sorted(tasks, key=lambda t: t.kind)],
                         [("ACCEPT", {"system": "ACCEPT", "version": "v"}), ("IMPLEMENT", {"unit": "u", "rev": "r"})])

    def test_nothing_is_issued_from_a_head_that_is_not_named(self) -> None:
        for held in (Qualification("UNQUALIFIED"), Qualification("ROLLBACK"), Qualification("RETIRED"),
                     Qualification("QUALIFIED", 2, "sha256:" + "0" * 64, 3)):
            with self.subTest(state=held.state, provisional=held.provisional), self.assertRaises(NotIssuable):
                would_issue(self.chain(), self.trees, held)

    def test_observe_only_writes_nothing(self) -> None:
        mark = self.home.high_water("demo").get()
        report = observe(self.chain(), self.trees, self.held())
        self.assertEqual(report["issued"], [])
        self.assertTrue(report["would_issue"])
        self.assertIn("observe-only", report["mode"])
        self.assertFalse(Journal(self.home, "demo").path.exists(), "no journal written")
        self.assertEqual(self.home.high_water("demo").get(), mark, "no mark written")
        withheld = observe(self.chain(), self.trees, Qualification("UNQUALIFIED"))
        self.assertEqual(withheld["would_issue"], [])
        self.assertIn("nothing is issued", withheld["withheld"])

    def test_dispatcher_serve(self) -> None:
        from typer.testing import CliRunner

        from ssds.cli import app

        with mock.patch("ssds.cli.ssds_home", return_value=self.home.root):
            result = CliRunner().invoke(app, ["dispatcher", "serve", "--ledger", "demo",
                                              "--repository", str(self.product)])
        self.assertEqual(result.exit_code, 0, result.output)
        report = json.loads(result.output)
        self.assertEqual((report["qualification"], report["issued"]), ("QUALIFIED", []))
        self.assertEqual(len(report["would_issue"]), len(would_issue(self.chain(), self.trees, self.held())))
        import shutil

        shutil.rmtree(self.home.witness_root / "demo")  # the witness holds nothing: not a named head
        with mock.patch("ssds.cli.ssds_home", return_value=self.home.root):
            withheld = CliRunner().invoke(app, ["dispatcher", "serve", "--ledger", "demo",
                                                "--repository", str(self.product)])
        self.assertEqual(withheld.exit_code, 1, withheld.output)
        self.assertEqual(json.loads(withheld.output)["would_issue"], [])


class WriteAhead(Fixture):
    def task(self) -> Task:
        return would_issue(self.chain(), self.trees, self.held())[0]

    def issue(self, task=None, held=None):
        return issue(Journal(self.home, "demo"), self.issuer, task or self.task(), held or self.held(),
                     governs={"mode": "LEGACY", "protocol": "7.2.1"}, route="MANUAL")

    def test_intent_then_effect_then_hand_out(self) -> None:
        issued = self.issue()
        kinds = [(e["kind"], e["task_id"]) for e in Journal(self.home, "demo").entries()]
        self.assertEqual(kinds, [("INTENT", issued.envelope["task_id"]), ("ISSUED", issued.envelope["task_id"]),
                                 ("HANDED", issued.envelope["task_id"])])
        self.assertEqual(Journal(self.home, "demo").recover(), [], "nothing to recover")

    def test_a_crash_before_the_hand_out_is_abandoned(self) -> None:
        task = self.task()
        with mock.patch.object(self.issuer, "issue", side_effect=OSError("crash")):
            with self.assertRaises(OSError):
                self.issue(task)
        journal = Journal(self.home, "demo")
        self.assertEqual(journal.recover(), [task.task_id])
        self.assertEqual(journal.recover(), [], "abandoned once")
        self.assertEqual(journal.outstanding(self.issuer.key_id, []), [])

    def test_a_crash_after_the_envelope_before_its_hand_out_is_abandoned(self) -> None:
        task = self.task()
        with mock.patch.object(Journal, "handed", side_effect=OSError("crash")):
            with self.assertRaises(OSError):
                self.issue(task)
        journal = Journal(self.home, "demo")
        self.assertEqual(journal.recover(), [task.task_id])
        self.assertEqual(len(journal.outstanding(self.issuer.key_id, [])), 1,
                         "signed, perhaps handed: it stays listed, the fail-safe direction (review 546cc86 N3)")

    def test_an_obligation_with_a_task_handed_out_is_not_issued_again(self) -> None:
        """Review 546cc86 N2: at a later head the same obligation is still READY, with another task id."""

        task = self.task()
        self.issue(task)
        held = self.held()
        later = Task(task_id(task.obligation_id, held.head + 1), task.obligation_id, task.kind, task.holder,
                     task.contract_revision)
        moved = Qualification("QUALIFIED", held.head + 1, "sha256:" + "1" * 64)
        with self.assertRaisesRegex(NotIssuable, "has a task open"):
            self.issue(later, moved)

    def test_an_issued_envelope_is_outstanding_until_its_task_finishes(self) -> None:
        issued = self.issue()
        journal = Journal(self.home, "demo")
        self.assertEqual(len(journal.outstanding(self.issuer.key_id, [])), 1)
        self.assertEqual(journal.outstanding(self.issuer.key_id, [issued.envelope["task_id"]]), [])

    def test_a_task_is_issued_only_at_its_own_named_head(self) -> None:
        task = self.task()
        held = self.held()
        elsewhere = Qualification("QUALIFIED", held.head + 1, "sha256:" + "1" * 64)
        with self.assertRaises(NotIssuable):
            self.issue(task, elsewhere)
        with self.assertRaises(NotIssuable):
            self.issue(task, Qualification("QUALIFIED", held.head, held.head_digest, held.head + 1))
        self.assertFalse(Journal(self.home, "demo").path.exists(), "no intent written")


if __name__ == "__main__":
    unittest.main()
