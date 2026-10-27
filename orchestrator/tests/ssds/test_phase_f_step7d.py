"""Phase F step 7d: ``FORK_RESOLUTION`` (catalogue §22.4, §23.6, §23.8; plan §3.4, reading F58).

A fork resolution abandons exactly the heads a loss would name (F54), every one proved never admitted, so it sets no
boundary; any other abandonment is a ``LEDGER_LOSS``. It is admitted under ``FORK`` or ``ROLLBACK`` (F50, B1): an
entry that reached fewer than ``q_a`` witnesses before the replica lost it reads ``ROLLBACK``, and is resubmitted by
its identity once resolved (§22.4). The replica keeps its own side; choosing the other side needs a ref restore (F47).
"""

from __future__ import annotations

import os
import unittest

from ssds.admission.engine import AdmissionHalted, EntryInvalid
from ssds.derivation import History
from ssds.ledger.qualification import HighWaterMark
from ssds.ledger.read import ledger_ref, read_chain

from ._fixtures import git, record, sshsig
from .test_phase_f_step7c import LossFixture, TeamLedger


class Resolution(TeamLedger):
    def resolve(self, admission, abandoned=None) -> int:
        fields = {"abandoned": admission.prepare_loss()["abandoned"] if abandoned is None else abandoned}
        rec = record("FORK_RESOLUTION", target=None, actor=self.human(), fields=fields)
        return admission.admit_lifecycle(rec, sshsig(self.private, admission.lifecycle_message(rec)), None)

    def unwritable(self, *witnesses: str) -> None:
        for w in witnesses:
            folder = self.roots[w] / "team"
            os.chmod(folder, 0o500)
            self.addCleanup(os.chmod, folder, 0o700)
            if os.access(folder, os.W_OK):
                self.skipTest("the permission bits do not bind this user")

    def writable(self, *witnesses: str) -> None:
        for w in witnesses:
            os.chmod(self.roots[w] / "team", 0o700)

    def test_a_lost_sub_quorum_entry_is_resolved_and_resubmitted_by_identity(self) -> None:
        """§23.8: only proved-never-admitted entries lost; no boundary; the request resubmitted by identity."""

        admission = self.team()
        issuer = self.issuer_at("team-issuer")
        register = record("KEY_LIFECYCLE", target=None, actor=self.human(),
                          fields={"action": "REGISTER", "key": issuer.trust_root()})
        self.unwritable("w1", "w2")
        with self.assertRaises(AdmissionHalted):  # held by w0 alone: provisional
            admission.admit_lifecycle(register, sshsig(self.private, admission.lifecycle_message(register)),
                                      self.baseline)
        self.writable("w1", "w2")
        self.rewind_to_genesis()  # the replica loses the provisional entry
        self.assertEqual(admission.qualification(admission.chain()).state, "ROLLBACK")
        self.assertEqual([a["status"] for a in admission.prepare_loss()["abandoned"]], ["PROVED_NEVER_ADMITTED"])
        position = self.resolve(admission)
        self.assertEqual(position, 1)
        held = admission.qualification(admission.chain())
        self.assertEqual((held.state, held.head), ("QUALIFIED", 1))
        self.assertEqual(History(read_chain(self.repository, "team"), self.trees).boundaries, [], "no boundary")
        again = admission.admit_lifecycle(register, sshsig(self.private, admission.lifecycle_message(register)),
                                          self.baseline)
        self.assertEqual(again, 2, "the same record, by its identity, admitted afresh")

    def test_a_resolution_after_a_loss_names_only_new_heads(self) -> None:
        """A head an earlier loss abandoned is not named again, so it bars no later resolution."""

        one = self.append(self.genesis, 1, "1")
        self.checkpoint(one, "w0", "w1")  # known admitted: a loss's
        self.rewind_to_genesis()
        admission = self.team()
        position = self.loss(admission)
        after = admission.chain().entries[position]
        two = self.append(after, position + 1, "2")
        self.checkpoint(two, "w0")  # one of three, then lost by the replica
        git(self.repository, "update-ref", ledger_ref("team"), after.commit)
        self.assertEqual(admission.qualification(admission.chain()).state, "ROLLBACK")
        self.assertEqual([(a["digest"], a["status"]) for a in admission.prepare_loss()["abandoned"]],
                         [(two.digest, "PROVED_NEVER_ADMITTED")])
        self.assertEqual(self.resolve(admission), position + 1)

    def test_a_fork_keeps_the_replicas_side(self) -> None:
        one = self.append(self.genesis, 1, "1")
        self.checkpoint(one, "w0")  # witnessed by one of three
        self.rewind_to_genesis()
        self.append(self.genesis, 1, "2")  # the replica's own side, unwitnessed
        admission = self.team()
        self.assertEqual(admission.qualification(admission.chain()).state, "FORK")
        abandoned = admission.prepare_loss()["abandoned"]
        self.assertEqual([(a["position"], a["digest"], a["status"]) for a in abandoned],
                         [(1, one.digest, "PROVED_NEVER_ADMITTED")])
        position = self.resolve(admission)
        held = admission.qualification(admission.chain())
        self.assertEqual((held.state, held.head, position), ("QUALIFIED", 2, 2))

    def test_a_possibly_or_known_admitted_head_is_a_loss(self) -> None:
        one = self.append(self.genesis, 1, "1")
        self.checkpoint(one, "w0", "w1")  # held by q_a
        self.rewind_to_genesis()
        admission = self.team()
        with self.assertRaisesRegex(EntryInvalid, "LEDGER_LOSS"):
            self.resolve(admission)
        self.assertEqual(len(admission.chain().entries), 1)

    def test_a_marks_head_is_never_resolved_away(self) -> None:
        """Review 8bfaaf0 N2: a qualified mark's head is floored at possibly admitted, so only a loss abandons it."""

        self.home.high_water("team").set(HighWaterMark(1, "sha256:" + "7" * 64))
        admission = self.team({"w0": self.roots["w0"], "w1": self.roots["w1"]})
        self.assertEqual(admission.qualification(admission.chain()).state, "ROLLBACK")
        with self.assertRaisesRegex(EntryInvalid, "LEDGER_LOSS"):
            self.resolve(admission)

    def test_the_abandoned_set_is_exact(self) -> None:
        one = self.append(self.genesis, 1, "1")
        self.checkpoint(one, "w0")
        self.rewind_to_genesis()
        admission = self.team()
        named = admission.prepare_loss()["abandoned"]
        for wrong in ([], named + [{"position": 5, "digest": "sha256:" + "5" * 64, "status": "PROVED_NEVER_ADMITTED"}],
                      [{**named[0], "status": "POSSIBLY_ADMITTED"}]):
            with self.subTest(abandoned=wrong), self.assertRaisesRegex(EntryInvalid, "recomputed abandoned"):
                self.resolve(admission, wrong)
        rec = record("FORK_RESOLUTION", target=None, actor=self.human(), fields={"abandoned": named, "note": "x"})
        with self.assertRaisesRegex(EntryInvalid, "exactly"):
            admission.admit_lifecycle(rec, sshsig(self.private, admission.lifecycle_message(rec)), None)
        self.assertEqual(len(admission.chain().entries), 1)

    def test_nothing_to_resolve(self) -> None:
        git(self.repository, "update-ref", ledger_ref("team"), self.genesis.commit)
        admission = self.team({"w0": self.roots["w0"]})  # UNQUALIFIED: not a fork resolution's state
        with self.assertRaisesRegex(AdmissionHalted, "reading F50"):
            self.resolve(admission)


class SingleWitness(LossFixture):
    def test_on_local_trust_a_witnessed_head_is_always_a_loss(self) -> None:
        """With q_a = 1 any witnessed checkpoint is known admitted: a fork resolution never abandons it."""

        self.admit_finding("one")
        self.rewind()
        with self.assertRaisesRegex(EntryInvalid, "LEDGER_LOSS"):
            rec = record("FORK_RESOLUTION", target=None, actor=self.human(),
                         fields={"abandoned": self.admission.prepare_loss()["abandoned"]})
            self.admission.admit_lifecycle(rec, sshsig(self.private, self.admission.lifecycle_message(rec)), None)


if __name__ == "__main__":
    unittest.main()
