"""Phase F step 9f-ii-iii: the Dispatcher runs its evidence obligations and submits them (catalogue §6.9, §17.2-§17.5,
§25.1; plan §3.6, readings F114-F115).

On ``AdmittedRuns``'s ledger, its runner key the Executor's own: a ``REALIZE`` runs and its realization is admitted
and ends it; an incomplete run keeps it open; outputs the declaration does not hold are ``MALFORMED_OUTPUT``; the
budget and backoff hold an obligation; an outstanding execution holds its configuration; a restart submits an
execution never ended as ``INCOMPLETE CRASHED``; a ``RERUN`` no run here could serve is held; external custody and a
real ledger run nothing; a ``READING`` closed in the journal is issued no more. The sandbox is a stand-in here (its
live behaviour is 9f-ii-ii's). Expected values are from §6.9, §17.2-§17.3 and F114-F115.
"""

from __future__ import annotations

import unittest
from types import SimpleNamespace
from unittest import mock

from ssds.dispatcher import realize
from ssds.dispatcher.realize import Budget, Executor, RunnerKey
from ssds.dispatcher.runner import Execution, RunnerProvider
from ssds.ledger.qualification import Home

from . import test_phase_f_step9d_iii as harness

GOVERNS = {"mode": "LEGACY", "protocol": "7.2.1"}
PROVIDER = RunnerProvider(argv=("/bin/true",), components=(("/usr", "host-usr"),))


class FakeSandbox:
    def __init__(self, *results: Execution) -> None:
        self.results = list(results)
        self.calls = 0

    def attributes(self, provider):
        return tuple(provider.attributes)

    def execute(self, workspace, tree, provider, bound_seconds):
        self.calls += 1
        self.bound = bound_seconds
        return self.results.pop(0)


class Fixture(harness.AdmittedRuns):
    """``AdmittedRuns`` whose designated runner key is the Executor's own, in the same SSDS home."""

    def setUp(self) -> None:
        original, made = harness.RunnerKey, []

        def first_is_the_executors() -> object:  # the runner; the custodian stays a key of its own
            made.append(None)
            return RunnerKey(Home(self.home.root), "demo", "ci") if len(made) == 1 else original()

        with mock.patch.object(harness, "RunnerKey", first_is_the_executors):
            super().setUp()

    def executor(self, *results: Execution, **kw) -> Executor:
        self.fake = FakeSandbox(*results)
        return Executor(Home(self.home.root), "demo", self.chain, self.trees, {"ci": PROVIDER},
                        lambda req: self.admission.admit(req, self.head()), governs=GOVERNS, sandbox=self.fake,
                        **kw)

    def realizes(self) -> list:
        from ssds.derivation import Workflow

        return [o for o in Workflow(self.derive()).obligations if o.kind == "REALIZE"]


GOOD = Execution({"x": 2, "x_verdict": "PASS"}, None, 0)


class Runs(Fixture):
    def test_a_realization_is_run_admitted_and_ends_realize(self) -> None:
        ex = self.executor(GOOD)
        (item,) = [r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE"]
        self.assertIsNone(item.held)
        decision = ex.run(self.derive(), item)
        self.assertEqual((decision.reasons, decision.refused), ((), ()), "admitted")
        self.assertEqual(len(decision.admitted), 1)
        real = self.derive().s.record(decision.admitted[0])
        self.assertEqual((real["actor"], real["outcome"]), (f"machinery:runner@{self.runner.key_id}", "COMPLETE"))
        self.assertEqual(self.realizes(), [], "a current, complete, admissible realization ends REALIZE (F95)")
        self.assertEqual(self.fake.bound, 24 * 3600, "the declared bound, under the 168 h cap (F79)")

    def test_an_incomplete_run_keeps_it_open(self) -> None:
        ex = self.executor(Execution(None, "TIME_BOUND", -9))
        (item,) = [r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE"]
        decision = ex.run(self.derive(), item)
        real = self.derive().s.record(decision.admitted[0])
        self.assertEqual((real["outcome"], real["fields"]["execution"]["incomplete"]), ("INCOMPLETE", "TIME_BOUND"))
        self.assertEqual(len(self.realizes()), 1)

    def test_outputs_the_declaration_does_not_hold(self) -> None:
        """§17.3 (review of cc028146, note 3): the submitter applies ``outcome_problems``."""

        ex = self.executor(Execution({"x": 2, "x_verdict": "PASS", "log": "extra"}, None, 0))
        (item,) = [r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE"]
        decision = ex.run(self.derive(), item)
        real = self.derive().s.record(decision.admitted[0])
        self.assertEqual(real["fields"]["execution"]["incomplete"], "MALFORMED_OUTPUT")
        self.assertNotIn("evaluated", real["fields"])

    def test_a_crash_keeps_its_surviving_outputs(self) -> None:
        """F114 (plan check of 23d2f5f2, note 4): a failing outcome written before the end stays visible."""

        raw = b'{"x":1,"x_verdict":"FAIL"}'
        ex = self.executor(Execution(None, "CRASHED", -11, raw=raw))
        (item,) = [r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE"]
        decision = ex.run(self.derive(), item)
        real = self.derive().s.record(decision.admitted[0])
        (ref,) = real["refs"]
        self.assertEqual(ref["store"], "RUNNER")
        kept = ex.home.read_private(ex.home.artifact_parts("demo", ref["digest"]))
        self.assertEqual(kept, raw)

    def test_the_record_identity_is_the_ledgers(self) -> None:
        from ssds.ledger.schema import record_id

        ex = self.executor(GOOD)
        (item,) = [r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE"]
        decision = ex.run(self.derive(), item)
        real = self.derive().s.record(decision.admitted[0])
        self.assertEqual(real["id"], record_id(real))


class Holds(Fixture):
    def realize_item(self, ex):
        return next(r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE")

    def test_the_retry_budget_and_its_backoff(self) -> None:
        now = [1000.0]
        ex = self.executor(*[Execution(None, "FAILED_TO_START", None)] * 3,
                             budget=Budget(attempts=2, base_seconds=60.0), wall=lambda: now[0])
        ex.run(self.derive(), self.realize_item(ex))
        self.assertEqual(self.realize_item(ex).held, "waiting out the retry backoff")
        now[0] += 61
        ex.run(self.derive(), self.realize_item(ex))
        self.assertIn("retry budget is spent", self.realize_item(ex).held)

    def test_an_outstanding_execution_holds_its_configuration(self) -> None:
        ex = self.executor()
        item = self.realize_item(ex)
        ex.journal.exec_intent("r-1", item.obligation.id, ex._hold_key(item.obligation, "spec"), {})
        self.assertEqual(self.realize_item(ex).held, "an execution of this configuration is outstanding")

    def test_a_real_ledger_runs_nothing(self) -> None:
        ex = self.executor(real_ledger=True)
        self.assertIn("F8", self.realize_item(ex).held)

    def test_external_custody_and_an_undesignated_key(self) -> None:
        ex = self.executor()
        item = self.realize_item(ex)
        custody = SimpleNamespace(kind="EXTERNAL_CUSTODY", keys=(), observes_outside_reads=True)
        self.assertIn("custodian", ex._held(self.derive(), item.obligation, custody, "ci", None, "spec", set()))
        stranger = SimpleNamespace(kind="DISPATCHER", keys=("ed25519:other",), observes_outside_reads=True)
        self.assertIn("no key", ex._held(self.derive(), item.obligation, stranger, "ci", None, "spec", set()))

    def test_a_rerun_no_run_here_could_serve(self) -> None:
        """§6.9's availability (review of 8f6cec9b, note): real(a⁻) recorded a pin this runner never records."""

        t0 = self.tree("T0")
        failure = self.fail(self.realize(t0, harness.BAD))  # not reproduced: (1) lacks, a RERUN on its tree
        ex = self.executor()
        reruns = [r for r in ex.runs(self.derive()) if r.obligation.kind == "RERUN"]
        self.assertTrue(reruns, "the failure derives a RERUN")
        self.assertTrue(all("ext-equal" in r.held for r in reruns))
        blind = SimpleNamespace(kind="DISPATCHER", keys=(self.runner.key_id,), observes_outside_reads=False)
        self.assertIn("unpinnable", ex._held(self.derive(), reruns[0].obligation, blind, "ci",
                                             failure["target"]["realization"], "spec", set()))


class FailingTree(Fixture):
    """A ``RERUN`` on the failing tree runs at that tree's own position (F114): its basis and target are ``view(k)``'s,
    not the head's, and Admission's step 2 accepts it there (F97)."""

    def bound(self, unit: str) -> None:
        from ._fixtures import record

        s = self.derive().s
        view = s.view
        c = record("COMPLETENESS", target={"scope": [unit], "classes": ["EXEC"],
                                           "membership": view.membership_digest((unit,))},
                   outcome="COMPLETE", actor=self.human(),
                   basis=[{"mode": "content", "target": {"unit": unit, "rev": view.rev(unit)}, "class": "EXACT"}])
        attestation = record("NON_AUTHORSHIP_ATTESTATION", target={"record": c["id"]}, outcome="NOT_AUTHOR",
                             actor=self.human())
        self.admit_human(c, attestation)

    def test_a_rerun_on_the_failing_tree(self) -> None:
        self.bound("code"), self.bound("spec")
        bad = Execution({"x": 1, "x_verdict": "FAIL"}, None, 0)
        ex = self.executor(bad, bad)
        first = ex.run(self.derive(), next(r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE"))
        failing_real = self.derive().s.record(first.admitted[0])
        self.assertNotEqual(failing_real["fields"]["execution"]["bounded_by"], "UNBOUNDED", "a bounded basis")
        self.fail(failing_real)
        t0 = failing_real["fields"]["execution"]["tree"]
        self.tree("T1", **{"a.py": "v = 2\n"})  # the head moves: the failing tree is an older one
        rerun = next(r for r in ex.runs(self.derive()) if r.obligation.kind == "RERUN"
                     and r.obligation.target["on"] == "FAILING")
        self.assertIsNone(rerun.held, rerun.held)
        decision = ex.run(self.derive(), rerun)
        self.assertEqual((decision.reasons, decision.refused), ((), ()))
        again = self.derive().s.record(decision.admitted[0])
        self.assertEqual(again["fields"]["execution"]["tree"], t0)
        self.assertEqual(again["target"], failing_real["target"], "view(k)'s revisions, not the head's")


class Recovery(Fixture):
    def test_an_execution_never_ended_is_reported_crashed(self) -> None:
        f = self

        class Interrupted(FakeSandbox):
            def execute(self, *a):
                raise KeyboardInterrupt  # the Dispatcher dies mid-run

        ex = f.executor()
        ex.sandbox = Interrupted()
        item = next(r for r in ex.runs(f.derive()) if r.obligation.kind == "REALIZE")
        with self.assertRaises(KeyboardInterrupt):
            ex.run(f.derive(), item)
        restarted = f.executor()
        (decision,) = restarted.recover()
        real = f.derive().s.record(decision.admitted[0])
        self.assertEqual((real["outcome"], real["fields"]["execution"]["incomplete"]), ("INCOMPLETE", "CRASHED"))
        self.assertEqual(restarted.recover(), [], "no duplicate")


class CrashWindows(Fixture):
    """Review of cc7abfed, B1 and B2: every crash point after the intent is recoverable, and a crashed run's
    surviving outputs are kept."""

    def realize_item(self, ex):
        return next(r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE")

    def admitted_realizations(self) -> list:
        s = self.derive().s
        return [r for r in s.of_kind("REALIZATION")]

    def test_a_failure_before_the_request_is_journaled(self) -> None:
        ex = self.executor(Execution(None, "CRASHED", -11, raw=b'{"x":1}'))
        with mock.patch.object(Executor, "_keep", side_effect=OSError("disk full")), self.assertRaises(OSError):
            ex.run(self.derive(), self.realize_item(ex))
        restarted = self.executor()
        (decision,) = restarted.recover()
        self.assertEqual(len(decision.admitted), 1, "reported, not lost (§6.9)")
        self.assertEqual(restarted.recover(), [])
        self.assertEqual(len(self.admitted_realizations()), 1)

    def test_a_failure_after_the_request_is_journaled(self) -> None:
        ex = self.executor(GOOD)
        with mock.patch.object(ex.journal, "exec_ended", side_effect=OSError("crash")), self.assertRaises(OSError):
            ex.run(self.derive(), self.realize_item(ex))
        restarted = self.executor()
        decisions = restarted.recover()
        self.assertEqual(len(self.admitted_realizations()), 1, "the journaled request, never a second CRASHED one")
        self.assertEqual(self.derive().s.record(self.admitted_realizations()[0])["outcome"], "COMPLETE")
        self.assertEqual(len(decisions), 1)
        self.assertEqual(restarted.journal.open_executions(), [])

    def test_a_restart_keeps_the_crashed_runs_outputs(self) -> None:
        import os

        raw = b'{"x":1,"x_verdict":"FAIL"}'

        class DiesAfterWriting(FakeSandbox):
            def execute(self, workspace, tree, provider, bound_seconds):
                out = workspace.root.parent / "out"
                out.mkdir()
                (out / "outputs.json").write_bytes(raw)
                raise KeyboardInterrupt  # the Dispatcher dies mid-run, outputs written

        ex = self.executor()
        ex.sandbox = DiesAfterWriting()
        with self.assertRaises(KeyboardInterrupt):
            ex.run(self.derive(), self.realize_item(ex))
        (decision,) = self.executor().recover()
        real = self.derive().s.record(decision.admitted[0])
        self.assertEqual(real["fields"]["execution"]["incomplete"], "CRASHED")
        (ref,) = real["refs"]
        self.assertEqual(ex.home.read_private(ex.home.artifact_parts("demo", ref["digest"])), raw)
        self.assertEqual(os.listdir(ex.home.root / "runs" / "demo"), ["artifacts"], "the workspace removed")

    def test_one_outstanding_execution_per_configuration(self) -> None:
        """Review of cc7abfed, note 1: keyed on the configuration and tree, not the obligation."""

        ex = self.executor()
        realize = SimpleNamespace(kind="REALIZE", target={"obligation": "e"}, params={})
        here = SimpleNamespace(kind="RERUN", target={"record": "a", "on": "HERE"}, params={"tree": "t1"})
        failing = SimpleNamespace(kind="RERUN", target={"record": "b", "on": "FAILING"}, params={"tree": "t0"})
        other = SimpleNamespace(kind="RERUN", target={"record": "c", "on": "FAILING"}, params={"tree": "t0"})
        self.assertEqual(ex._hold_key(realize, "spec"), ex._hold_key(here, "spec"), "both on the head")
        self.assertEqual(ex._hold_key(failing, "spec"), ex._hold_key(other, "spec"), "two failures, one tree")
        self.assertNotEqual(ex._hold_key(realize, "spec"), ex._hold_key(failing, "spec"))


class ReadingClose(Fixture):
    def test_a_closed_reading_is_issued_no_more(self) -> None:
        """F115: journal state only (§3.1); READING stays derived."""

        from ssds.dispatcher.schedule import Task, issuable

        task = Task("task-1-abc", "sha256:" + "9" * 64, "READING", "REVIEWER", None, (), None)
        allowed, held = issuable((task,), (), frozenset({task.obligation_id}))
        self.assertEqual((allowed, held[0][1]), ((), "closed by the Dispatcher's journal into the owner's adjudication"))
        f = self
        ex = f.executor()
        ex.journal.intent("task-1-abc", task.obligation_id, 0, "sha256:" + "0" * 64)
        ex.journal.close_reading("task-1-abc", task.obligation_id, "sha256:" + "8" * 64)
        self.assertEqual(ex.journal.closed_readings(), frozenset({task.obligation_id}))
        self.assertEqual(ex.journal.open_tasks(), [], "the reviewer's task holds nothing more")



@unittest.skipUnless(__import__("os").environ.get("SSDS_LIVE_SANDBOX") == "1",
                     "needs user namespaces: run on the host with SSDS_LIVE_SANDBOX=1 (F113's live tests)")
class LiveEndToEnd(Fixture):
    def test_a_realize_run_in_the_sandbox_and_admitted(self) -> None:
        provider = RunnerProvider(argv=("/bin/sh", "-c", "printf '{\"x\":2,\"x_verdict\":\"PASS\"}' > /out/outputs.json"),
                                  components=(("/usr", "host-usr"),))
        ex = Executor(Home(self.home.root), "demo", self.chain, self.trees, {"ci": provider},
                      lambda req: self.admission.admit(req, self.head()), governs=GOVERNS)
        item = next(r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE")
        decision = ex.run(self.derive(), item)
        real = self.derive().s.record(decision.admitted[0])
        self.assertEqual(real["outcome"], "COMPLETE")
        self.assertEqual(self.realizes(), [])


if __name__ == "__main__":
    unittest.main()
