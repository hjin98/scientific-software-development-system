"""Phase F step 7a: retirement (catalogue §22.1, §23.3-§23.4, §24.2; plan §3.4, readings F44-F45).

A ``LINEAGE_RETIREMENT`` is a human-gated recovery lifecycle entry with ``obs = null``, admitted only at a settled
head and only when ``q_a`` witnesses can hold it. Its successor is named for discovery only (F44). Admission then
publishes the retirement statement, signed by its host key and naming that entry as the ledger's last (F45); a
participant reads ``RETIRED`` when ``q_a`` witnesses hold a statement that verifies, and Admission appends nothing
more. A bare marker file is no retirement.
"""

from __future__ import annotations

import dataclasses
import json
import os
import unittest
from unittest import mock

from ssds.admission.engine import Admission, AdmissionHalted, EntryInvalid
from ssds.admission.lifecycle import retirement_problems
from ssds.ledger.append import HostKey, append_entry, retirement_statement, write_checkpoint
from ssds.ledger.qualification import (RETIREMENT_FILE, FileWitness, RetirementStatement, retirement_held,
                                       retirement_message, retirement_verified)

from ._fixtures import entry, record, sshsig
from .test_admission_requests import RequestFixture

SUCCESSOR = {"ledger_id": "demo-2", "genesis_digest": "sha256:" + "2" * 64}


class Retirement(RequestFixture):
    def retirement(self, successor=None, actor=None, **fields) -> dict:
        return record("LINEAGE_RETIREMENT", target=None, actor=actor or self.human(),
                      fields={"successor": dict(successor or SUCCESSOR), **fields})

    def retire(self, rec=None, private=None, obs=None, admission=None) -> int:
        admission = admission or self.admission
        rec = rec or self.retirement()
        return admission.admit_lifecycle(rec, sshsig(private or self.private, admission.lifecycle_message(rec)), obs)

    def state(self) -> str:
        return self.admission.qualification(self.admission.chain()).state

    def statement_path(self):
        return self.home.witness_root / "demo" / RETIREMENT_FILE

    def keys(self):
        return Admission.host_keys(self.admission.chain())

    # -- admission of the entry --------------------------------------------------------------------------------

    def test_a_retirement_is_admitted_published_and_read_retired(self) -> None:
        before = len(self.entries())
        position = self.retire()
        self.assertEqual(position, before)
        last = self.entries()[-1]
        self.assertEqual((last.entry["obs"], last.lifecycle["kind"]), (None, "LINEAGE_RETIREMENT"))
        self.assertEqual(last.lifecycle["fields"]["successor"], SUCCESSOR)
        self.assertIn("approval", last.lifecycle["provenance"])
        held = FileWitness(self.home.witness_root).statement("demo")
        self.assertEqual(held.body, {"ledger_id": "demo", "kind": "RETIREMENT", "last_position": position,
                                     "last_entry_digest": last.digest, "successor_ledger_id": "demo-2",
                                     "successor_genesis_digest": SUCCESSOR["genesis_digest"]})
        self.assertTrue(retirement_verified(held, "demo", self.keys(), self.admission.chain()))
        self.assertEqual(self.state(), "RETIRED")
        self.assertEqual(self.home.high_water("demo").get().position, position, "the mark keeps the last head")

    def test_nothing_is_appended_to_a_retired_ledger(self) -> None:
        self.retire()
        before = len(self.entries())
        with self.assertRaises(AdmissionHalted):
            self.lifecycle("REGISTER", self.issuer_at("other").trust_root())
        with self.assertRaises(AdmissionHalted):
            self.retire(self.retirement({"ledger_id": "demo-3", "genesis_digest": "sha256:" + "3" * 64}))
        with self.assertRaises(AdmissionHalted):
            Admission(self.home, "demo", self.trees).held_head()
        self.assertEqual(len(self.entries()), before)

    def test_a_retirement_carries_obs_null(self) -> None:
        before = len(self.entries())
        with self.assertRaises(EntryInvalid):
            self.retire(obs=self.baseline)
        self.assertEqual(len(self.entries()), before)

    def test_the_successor_shape_is_closed(self) -> None:
        before = len(self.entries())
        for successor in ({"ledger_id": "demo", "genesis_digest": SUCCESSOR["genesis_digest"]},
                          {"ledger_id": "demo-2"},
                          {**SUCCESSOR, "binding": "sha256:" + "4" * 64},
                          {"ledger_id": "Demo 2", "genesis_digest": SUCCESSOR["genesis_digest"]},
                          {"ledger_id": "demo-2", "genesis_digest": "not-a-digest"}):
            with self.subTest(successor=successor), self.assertRaises(EntryInvalid):
                self.retire(self.retirement(successor))
        with self.assertRaises(EntryInvalid):
            self.retire(self.retirement(migration="sha256:" + "5" * 64))
        self.assertEqual(len(self.entries()), before)

    def test_retirement_problems(self) -> None:
        self.assertEqual(retirement_problems({"successor": SUCCESSOR}, "demo"), [])
        self.assertTrue(retirement_problems({"successor": SUCCESSOR}, "demo-2"))
        self.assertTrue(retirement_problems({}, "demo"))
        self.assertTrue(retirement_problems({"successor": "demo-2"}, "demo"))
        self.assertTrue(retirement_problems(None, "demo"))

    def test_only_a_registered_humans_approval_retires(self) -> None:
        from ._fixtures import human_key

        stranger, _ = human_key(self.root, "stranger")
        before = len(self.entries())
        with self.assertRaises(EntryInvalid):
            self.retire(private=stranger)
        with self.assertRaises(EntryInvalid):
            self.retire(self.retirement(actor="human:SHA256:nobody"))
        rec = self.retirement()
        with self.assertRaises(EntryInvalid):  # an approval for another ledger head
            self.admission.admit_lifecycle(rec, sshsig(self.private, b"ssds lifecycle demo #9 x y\n"), None)
        self.assertEqual(len(self.entries()), before)

    def test_other_recovery_kinds_are_not_admitted_through_this_path_yet(self) -> None:
        rec = record("LEDGER_LOSS", target=None, actor=self.human(),
                     fields={"retained": {}, "abandoned": [], "report": "sha256:" + "0" * 64, "controls": {}})
        with self.assertRaises(EntryInvalid):
            self.admission.admit_lifecycle(rec, sshsig(self.private, self.admission.lifecycle_message(rec)), None)

    # -- the settled head and the trial ------------------------------------------------------------------------

    def test_an_unqualified_ledger_is_not_retired(self) -> None:
        import shutil

        shutil.rmtree(self.home.witness_root / "demo")
        before = len(self.entries())
        with self.assertRaises(AdmissionHalted):
            self.retire()
        self.assertEqual(len(self.entries()), before)

    def test_a_retirement_no_quorum_can_hold_is_not_appended(self) -> None:
        """The trial: the witness answers reads but cannot hold a new entry."""

        folder = self.home.witness_root / "demo"
        before = len(self.entries())
        os.chmod(folder, 0o500)
        self.addCleanup(os.chmod, folder, 0o700)
        if os.access(folder, os.W_OK):
            self.skipTest("the permission bits do not bind this user")
        self.assertEqual(self.state(), "QUALIFIED", "the witness still answers")
        with self.assertRaises(AdmissionHalted):
            self.retire()
        self.assertEqual(len(self.entries()), before)

    def test_a_crash_before_the_statement_is_completed_at_the_next_start(self) -> None:
        with mock.patch("ssds.admission.engine.write_retirement", side_effect=OSError("crash")):
            with self.assertRaises(AdmissionHalted):
                self.retire()
        retired_at = len(self.entries()) - 1
        held = self.admission.qualification(self.admission.chain())
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", retired_at, None))
        self.assertFalse(self.statement_path().exists())
        with self.assertRaises(AdmissionHalted):
            Admission(self.home, "demo", self.trees).held_head()
        self.assertEqual(self.state(), "RETIRED")
        self.assertEqual(len(self.entries()), retired_at + 1)

    def test_a_retirement_not_last_halts_and_publishes_nothing(self) -> None:
        """A chain carrying an entry after its retirement came from no conforming Admission: it halts."""

        with mock.patch("ssds.admission.engine.write_retirement", side_effect=OSError("crash")):
            with self.assertRaises(AdmissionHalted):
                self.retire()
        head = self.entries()[-1]
        key = HostKey.from_private_bytes((self.home.root / "keys" / "admission" / "demo.ed25519").read_bytes())
        adoption = record("RULESET_ADOPTION", target=None, actor=self.human(),
                          fields={"system": "ssds-rules/1", "policy": "sha256:" + "0" * 64,
                                  "analyzers": ["ssds.analyzer.python/1"]})
        appended = append_entry(self.home.ledger_repository("demo"),
                                entry("demo", head.position + 1, head.digest, key, lifecycle=adoption,
                                      obs=self.baseline), key, head.commit)
        write_checkpoint(FileWitness(self.home.witness_root), appended.checkpoint)
        with self.assertRaises(AdmissionHalted):
            Admission(self.home, "demo", self.trees).held_head()
        self.assertFalse(self.statement_path().exists())

    # -- the statement and its verifier ------------------------------------------------------------------------

    def test_the_verifier(self) -> None:
        self.retire()
        chain = self.admission.chain()
        good = FileWitness(self.home.witness_root).statement("demo")
        keys = self.keys()
        stranger = HostKey.generate()
        last = chain.entries[-1]
        forged = retirement_statement(stranger, "demo", last)
        self.assertFalse(retirement_verified(forged, "demo", keys, chain), "a key outside the trust roots")
        self.assertTrue(retirement_verified(forged, "demo", {stranger.key_id: stranger.public_hex}, chain))
        tampered = RetirementStatement({**good.body, "successor_ledger_id": "demo-9"}, good.signatures)
        self.assertFalse(retirement_verified(tampered, "demo", keys, chain), "the signature covers the body")
        self.assertFalse(retirement_verified(good, "other", keys, chain), "another ledger")
        self.assertFalse(retirement_verified(None, "demo", keys, chain))
        key = HostKey.from_private_bytes((self.home.root / "keys" / "admission" / "demo.ed25519").read_bytes())
        previous = chain.entries[-2]
        earlier = retirement_statement(key, "demo", dataclasses.replace(previous, entry={**previous.entry,
                                                                                     "lifecycle": last.lifecycle}))
        self.assertFalse(retirement_verified(earlier, "demo", keys, chain), "not the chain's retirement entry")
        wrong_digest = RetirementStatement({**good.body, "last_entry_digest": "sha256:" + "9" * 64}, ())
        signed = RetirementStatement(wrong_digest.body, ((key.key_id, key.sign(
            retirement_message(wrong_digest.body)).hex()),))
        self.assertFalse(retirement_verified(signed, "demo", keys, chain), "another entry at that position")
        behind = chain.__class__(chain.ledger_id, chain.entries[:-1])
        self.assertTrue(retirement_verified(good, "demo", keys, behind), "a participant behind the retirement")
        self.assertTrue(retirement_verified(good, "demo", keys), "a chainless participant, its genesis pinned")
        self.assertFalse(retirement_held([good], 2, "demo", keys, chain))
        self.assertFalse(retirement_held([forged, None], 1, "demo", keys, chain))

        def signed_body(**changes):
            body = {**good.body, **changes}
            return RetirementStatement(body, ((key.key_id, key.sign(retirement_message(body)).hex()),))

        self.assertFalse(retirement_verified(signed_body(kind="CHECKPOINT"), "demo", keys), "another kind")
        self.assertFalse(retirement_verified(signed_body(last_position=0), "demo", keys), "genesis is never last")
        self.assertFalse(retirement_verified(signed_body(last_position=True), "demo", keys))

    def test_a_statement_file_is_closed_and_never_a_link(self) -> None:
        self.retire()
        path = self.statement_path()
        good = json.loads(path.read_bytes())
        path.unlink()
        path.write_text(json.dumps({**good, "note": "x"}))
        self.assertIsNone(FileWitness(self.home.witness_root).statement("demo"), "an extra field")
        path.unlink()
        elsewhere = self.root / "statement.json"
        elsewhere.write_text(json.dumps(good))
        path.symlink_to(elsewhere)
        self.assertIsNone(FileWitness(self.home.witness_root).statement("demo"), "a link")
        path.unlink()
        path.write_text(json.dumps(good))
        self.assertIsNotNone(FileWitness(self.home.witness_root).statement("demo"))

    def test_a_bare_or_unreadable_marker_is_no_retirement(self) -> None:
        folder = self.home.witness_root / "demo"
        for text in ("", "{}\n", "not json", json.dumps({"ledger_id": "demo", "kind": "RETIREMENT"})):
            with self.subTest(text=text):
                (folder / RETIREMENT_FILE).write_text(text)
                self.assertIsNone(FileWitness(self.home.witness_root).statement("demo"))
                self.assertEqual(self.state(), "QUALIFIED")

    def test_a_witness_holding_another_statement_holds_nothing_of_this_one(self) -> None:
        (self.home.witness_root / "demo" / RETIREMENT_FILE).write_text("{}\n")
        before = len(self.entries())
        with self.assertRaises(AdmissionHalted):
            self.retire()
        self.assertEqual(len(self.entries()), before + 1, "admitted, its statement not held")
        self.assertEqual(self.state(), "QUALIFIED")

    def test_the_interface_reads_retired(self) -> None:
        from ssds.cli import HomeAccess
        from ssds.interface.operations import present

        self.retire()
        presented = present(HomeAccess(self.home, "demo"), self.trees)
        self.assertEqual(presented.state, "RETIRED")
        self.assertFalse(presented.current)


if __name__ == "__main__":
    unittest.main()
