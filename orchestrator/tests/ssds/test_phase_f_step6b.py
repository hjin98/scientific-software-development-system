"""Phase F step 6b: the commit point (catalogue §21.3, §22.4, §23.3-§23.4; plan §3.3).

Admission qualifies the ledger against the genesis witness model before deciding anything and appends nothing
when it is not ``QUALIFIED``. It appends by the ledger's compare-and-swap, a loser re-reading and revalidating;
writes each checkpoint to the witnesses; and reports a request decided only once a witness quorum holds its entry,
raising the high-water mark. A crash between the compare-and-swap and the checkpoint leaves one provisional entry,
whose distribution the next start completes before the request is found by its identity (8a75346 N2, ledger form).
A rewind is ``ROLLBACK`` (441cf5c N7).
"""

from __future__ import annotations

import shutil
import unittest
from types import SimpleNamespace
from unittest import mock

from ssds.admission.engine import Admission, AdmissionHalted
from ssds.ledger.append import AppendRefused
from ssds.ledger.qualification import HighWaterMark
from ssds.ledger.read import ledger_ref, with_id

from ._fixtures import git
from .test_admission_requests import RequestFixture, finding


class CommitPoint(RequestFixture):
    def human_request(self, note: str = "x"):
        from ssds.admission.request import request_message

        from ._fixtures import sshsig

        rec = with_id({**finding(note=note), "actor": self.human()})
        req = self.request([rec], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return req

    def test_a_decision_raises_the_high_water_mark(self) -> None:
        decision = self.admit(self.human_request())
        mark = self.home.high_water("demo").get()
        self.assertEqual(mark.position, decision.position)
        self.assertEqual(mark.entry_digest, self.entries()[-1].digest)

    def test_an_unwitnessed_head_is_not_qualified_and_nothing_is_appended(self) -> None:
        shutil.rmtree(self.home.witness_root / "demo")
        before = len(self.entries())
        with self.assertRaises(AdmissionHalted):
            self.admit(self.human_request())
        self.assertEqual(len(self.entries()), before)

    def test_a_rewind_is_rollback(self) -> None:
        """441cf5c N7: the ledger ref rewound below the retained high-water mark."""

        self.admit(self.human_request("one"))
        ledger = self.home.ledger_repository("demo")
        tip = git(ledger, "rev-parse", ledger_ref("demo"))
        git(ledger, "update-ref", ledger_ref("demo"), git(ledger, "rev-parse", tip + "^"))
        state = self.admission.qualification(self.admission.chain()).state
        self.assertEqual(state, "ROLLBACK")
        with self.assertRaises(AdmissionHalted):
            self.admit(self.human_request("two"))

    def test_a_crash_before_the_checkpoint_is_recovered_by_request_identity(self) -> None:
        """8a75346 N2, ledger form: the entry is appended but not yet held; the next start completes its
        checkpoint's distribution and returns the recorded decision, appending nothing more."""

        request = self.human_request()
        with mock.patch("ssds.admission.engine.write_checkpoint", side_effect=OSError("crash")):
            with self.assertRaises(AdmissionHalted):
                self.admit(request)
        appended = len(self.entries())
        self.assertEqual(self.admission.qualification(self.admission.chain()).provisional, appended - 1)
        restarted = Admission(self.home, "demo", self.trees)
        decision = restarted.admit(request, self.baseline)
        self.assertFalse(decision.appended, "found by its identity")
        self.assertEqual(len(self.entries()), appended)
        held = restarted.qualification(restarted.chain())
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", appended - 1, None))
        self.assertEqual(self.home.high_water("demo").get().position, appended - 1, "the recovered head is retained")

    def test_a_lost_compare_and_swap_revalidates(self) -> None:
        from ssds.ledger import append

        real = append.append_entry
        calls = []

        def racing(*args, **kwargs):
            calls.append(1)
            if len(calls) == 1:
                raise AppendRefused("another writer moved the ledger")
            return real(*args, **kwargs)

        before = len(self.entries())
        with mock.patch("ssds.admission.engine.append_entry", side_effect=racing):
            decision = self.admit(self.human_request())
        self.assertEqual(len(calls), 2, "re-read and revalidated once")
        self.assertEqual(len(self.entries()), before + 1)
        self.assertTrue(decision.appended)

    def test_a_ledger_that_keeps_moving_halts(self) -> None:
        with mock.patch("ssds.admission.engine.append_entry", side_effect=AppendRefused("moving")):
            with self.assertRaises(AdmissionHalted):
                self.admit(self.human_request())

    def test_another_hosts_provisional_entry_is_not_redistributed(self) -> None:
        foreign = SimpleNamespace(entry={"position": 3, "host_key_id": "ed25519:other"}, digest="sha256:" + "0" * 64,
                                  commit="c" * 40)
        with self.assertRaises(AdmissionHalted):
            self.admission.distribute(foreign)

    def test_a_high_water_mark_beyond_the_ledger_is_rollback(self) -> None:
        self.home.high_water("demo").set(HighWaterMark(len(self.entries()) + 3, "sha256:" + "1" * 64))
        with self.assertRaises(AdmissionHalted):
            self.admit(self.human_request())


if __name__ == "__main__":
    unittest.main()
