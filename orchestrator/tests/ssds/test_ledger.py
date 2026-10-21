"""The Ledger Store: append by compare-and-swap, chain verification, integrity halt, qualification (read path).

Real Git repositories and real ``ssh-keygen`` signatures throughout. The
qualification expectations are transcribed from ``cases_s5_14_25.py``
(``qualification_states``, ``loss_bounds``, ``deployment_classes_sound``); group 4's
admission halves are Phase F.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from ssds.core.api.v1 import canonical_json
from ssds.ledger.append import AppendRefused, append_entry, create_ledger_repository, import_commits, write_checkpoint
from ssds.ledger.qualification import (
    Checkpoint,
    FileWitness,
    HighWaterMark,
    WitnessModel,
    WitnessSpec,
    checkpoint_body,
    checkpoint_message,
    loss_status,
    qualify,
    quorum_sound,
)
from ssds.ledger.read import ChainRejected, RawEntry, read_chain, read_raw, verify_chain
from ssds.ledger.signatures import HostKey, entry_message

from ._fixtures import approve, commit, entry, genesis_record, human_key, init_repo, record


class LedgerFixture(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.product = init_repo(self.root / "product")
        (self.product / "README.md").write_text("# Demo\n")
        self.baseline = commit(self.product, "baseline")
        self.ledger = create_ledger_repository(self.root / "home" / "ledgers" / "demo.git")
        self.witness = FileWitness(self.root / "home" / "witnesses")
        self.key = HostKey.generate()
        self.human_private, self.human_line = human_key(self.root)
        import_commits(self.ledger, self.product, [self.baseline])

    def genesis(self, **kwargs) -> dict:
        return approve(genesis_record(self.key, self.human_line, self.witness.root, self.baseline, **kwargs),
                       self.human_private)

    def append_genesis(self, **kwargs):
        appended = append_entry(self.ledger, entry("demo", 0, None, self.key, lifecycle=self.genesis(**kwargs)),
                                self.key, None, referenced=[self.baseline])
        write_checkpoint(self.witness, appended.checkpoint)
        return appended


class AppendAndRead(LedgerFixture):
    def test_genesis_then_an_entry_round_trip(self) -> None:
        first = self.append_genesis()
        finding = record("FINDING", target={"units": ["readme"]}, fields={"materiality": "ROUTINE"},
                         actor="agent:task-1/1", actor_class="AGENT")
        second = append_entry(self.ledger, entry("demo", 1, first.digest, self.key, kind="ABSORPTION", obs=self.baseline,
                                                 absorption={"fence": None}), self.key, first.commit)
        chain = read_chain(self.ledger, "demo")
        self.assertEqual([e.position for e in chain.entries], [0, 1])
        self.assertIsNone(chain.halt)
        self.assertEqual(chain.readable_through, 1)
        self.assertEqual(chain.entries[1].digest, second.digest)
        self.assertEqual(chain.genesis["kind"], "GENESIS")
        self.assertIn(self.baseline, chain.entries[0].parents, "the baseline commit is kept reachable")
        self.assertEqual(finding["kind"], "FINDING")

    def test_compare_and_swap_refuses_a_stale_expected_head(self) -> None:
        first = self.append_genesis()
        absorption = entry("demo", 1, first.digest, self.key, kind="ABSORPTION", obs=self.baseline, absorption={"fence": None})
        append_entry(self.ledger, absorption, self.key, first.commit)
        with self.assertRaises(AppendRefused):
            append_entry(self.ledger, absorption, self.key, first.commit)

    def test_a_checkpoint_is_never_overwritten(self) -> None:
        first = self.append_genesis()
        forged = replace(first.checkpoint, entry_commit="f" * 40)
        write_checkpoint(self.witness, forged)
        held = self.witness.read("demo")
        self.assertEqual([c.entry_commit for c in held], [first.commit])


class ChainVerification(LedgerFixture):
    """Unauthenticated chains are rejected; authenticated violations halt current assertion (§5.7)."""

    def raws(self) -> list[RawEntry]:
        first = self.append_genesis()
        append_entry(self.ledger, entry("demo", 1, first.digest, self.key, kind="ABSORPTION", obs=self.baseline,
                                        absorption={"fence": None}), self.key, first.commit)
        return read_raw(self.ledger, read_chain(self.ledger, "demo").entries[-1].commit)

    def resigned(self, raw: RawEntry, body: dict | bytes, key: HostKey | None = None) -> RawEntry:
        data = body if isinstance(body, bytes) else canonical_json(body)
        signer = key or self.key
        return RawEntry(raw.commit, raw.parents, {**raw.files, "entry.json": data, "entry.sig": signer.sign(entry_message(data))})

    def test_the_unaltered_chain_verifies(self) -> None:
        chain = verify_chain("demo", self.raws())
        self.assertEqual((len(chain.entries), chain.halt, chain.unreadable), (2, None, None))

    def test_a_changed_byte_without_a_new_signature_is_rejected(self) -> None:
        raws = self.raws()
        body = json.loads(raws[1].files["entry.json"])
        body["incarnation_id"] = "incarnation-2"
        tampered = RawEntry(raws[1].commit, raws[1].parents, {**raws[1].files, "entry.json": canonical_json(body)})
        with self.assertRaises(ChainRejected):
            verify_chain("demo", [raws[0], tampered])

    def test_a_key_not_in_force_is_rejected(self) -> None:
        raws = self.raws()
        stranger = HostKey.generate()
        body = json.loads(raws[1].files["entry.json"])
        body["host_key_id"] = stranger.key_id
        with self.assertRaises(ChainRejected):
            verify_chain("demo", [raws[0], self.resigned(raws[1], body, stranger)])

    def test_a_prev_mismatch_is_rejected(self) -> None:
        raws = self.raws()
        body = json.loads(raws[1].files["entry.json"])
        body["prev"] = "sha256:" + "9" * 64
        with self.assertRaises(ChainRejected):
            verify_chain("demo", [raws[0], self.resigned(raws[1], body)])

    def test_authenticated_schema_violations_halt_from_their_position(self) -> None:
        raws = self.raws()
        body = json.loads(raws[1].files["entry.json"])
        cases = {
            "unknown entry field": {**body, "extra": 1},
            "non-canonical bytes": json.dumps(body, indent=1).encode(),
            "unknown record kind": {**body, "records": [{"kind": "OPINION"}]},
            "obs on a non-absorption differing": {**body, "absorption": {"fence": None}, "records": [
                record("FINDING", target={"units": ["x"]}, fields={"materiality": "ROUTINE"})]},
        }
        for name, altered in cases.items():
            with self.subTest(name):
                chain = verify_chain("demo", [raws[0], self.resigned(raws[1], altered)])
                self.assertEqual((chain.halt, chain.readable_through), (1, 0), chain.halt_reasons)

    def test_an_unreadable_schema_version_is_not_corruption(self) -> None:
        raws = self.raws()
        body = json.loads(raws[1].files["entry.json"])
        chain = verify_chain("demo", [raws[0], self.resigned(raws[1], {**body, "schema": 2})])
        self.assertEqual((chain.halt, chain.unreadable, chain.readable_through), (None, 1, 0))

    def test_the_git_commit_chain_must_agree_with_prev(self) -> None:
        raws = self.raws()
        moved = RawEntry(raws[1].commit, (self.baseline,), raws[1].files)
        self.assertEqual(verify_chain("demo", [raws[0], moved]).halt, 1)

    def test_files_outside_the_entry_layout_halt(self) -> None:
        raws = self.raws()
        extra = RawEntry(raws[1].commit, raws[1].parents, {**raws[1].files, "notes.txt": b"x"})
        self.assertEqual(verify_chain("demo", [raws[0], extra]).halt, 1)


class GenesisChecks(LedgerFixture):
    """Admission's genesis validation: only LEGACY or UNGOVERNED modes, a sound witness model, a verified approval.

    The Ledger Store never interprets records (Manual §26.1), so a chain carrying any genesis
    content still verifies; the checks below are Admission's (§19.9, Phase D step 6).
    """

    def problems(self, genesis: dict) -> list[str]:
        from ssds.admission.genesis import genesis_violations

        return genesis_violations(genesis)

    def test_a_valid_shadow_genesis_passes(self) -> None:
        self.assertEqual(self.problems(self.genesis(modes={"docs": {"mode": "LEGACY", "protocol": "7.2.1"}})), [])

    def test_a_native_mode_is_refused_in_shadow(self) -> None:
        problems = self.problems(self.genesis(modes={"docs": {"mode": "NATIVE", "ruleset": "ssds-rules/1"}}))
        self.assertTrue(any("only LEGACY or UNGOVERNED" in p for p in problems), problems)

    def test_an_approval_by_another_key_or_over_other_bytes_is_refused(self) -> None:
        from ssds.ledger.read import with_id

        other_private, _ = human_key(self.root, "intruder")
        forged = approve(genesis_record(self.key, self.human_line, self.witness.root, self.baseline), other_private)
        self.assertTrue(any("approval signature" in p for p in self.problems(forged)))
        genesis = self.genesis()
        altered = dict(genesis)
        altered["fields"] = {**genesis["fields"], "project": "other-project"}
        self.assertTrue(any("approval signature" in p for p in self.problems(with_id(altered))))

    def test_the_ledger_does_not_interpret_genesis_content(self) -> None:
        appended = append_entry(self.ledger, entry("demo", 0, None, self.key,
                                                   lifecycle=self.genesis(modes={"docs": {"mode": "NATIVE", "ruleset": "x"}})),
                                self.key, None, referenced=[self.baseline])
        self.assertIsNone(read_chain(self.ledger, "demo", appended.commit).halt)


def _model(n: int, q_a: int, r: int, f: int, cls: str = "TEAM") -> WitnessModel:
    return WitnessModel(cls, n, q_a, r, f, tuple(WitnessSpec(f"w{i}", "GIT", f"loc{i}") for i in range(n)))


class Qualification(unittest.TestCase):
    """cases_s5_14_25.py: qualification_states, loss_bounds and deployment_classes_sound."""

    def setUp(self) -> None:
        self.key = HostKey.generate()
        self.keys = {self.key.key_id: self.key.public_hex}

    def chain(self, length: int, ledger_id: str = "demo"):
        from ssds.ledger.read import Chain, LedgerEntry

        entries = tuple(LedgerEntry(i, f"{i:040x}", (), {}, b"", b"", f"sha256:{i:064x}", {}) for i in range(length))
        return Chain(ledger_id, entries)

    def cp(self, position: int, digest: str | None = None) -> Checkpoint:
        body = checkpoint_body("demo", position, digest or f"sha256:{position:064x}", f"{position:040x}", self.key.key_id)
        return Checkpoint(**body, signature=self.key.sign(checkpoint_message(body)).hex())

    def test_qualification_states(self) -> None:
        model = _model(3, 2, 2, 0)
        # ROLLBACK: a replica at 4 below witnessed checkpoint 5
        stale = qualify(self.chain(5), {"w0": [self.cp(4), self.cp(5)], "w1": [self.cp(4), self.cp(5)]}, model, self.keys)
        # UNQUALIFIED: one response for a read quorum of two
        few = qualify(self.chain(6), {"w0": [self.cp(5)], "w1": None, "w2": None}, model, self.keys)
        # QUALIFIED@5: 5 held by two; the replica's 6, which no responder shows a checkpoint for, is provisional
        held = qualify(self.chain(7), {"w0": [self.cp(5)], "w1": [self.cp(5)]}, model, self.keys,
                       HighWaterMark(5, "sha256:" + f"{5:064x}"))
        # FORK: an observed checkpoint on a conflicting chain
        fork = qualify(self.chain(7), {"w0": [self.cp(5, "sha256:" + "e" * 64)], "w1": [self.cp(5, "sha256:" + "e" * 64)]},
                       model, self.keys)
        self.assertEqual((stale.state, few.state, (held.state, held.head, held.provisional), fork.state),
                         ("ROLLBACK", "UNQUALIFIED", ("QUALIFIED", 5, 6), "FORK"))

    def test_more_state_discriminators(self) -> None:
        model = _model(3, 2, 2, 0)
        both = {"w0": [self.cp(4)], "w1": [self.cp(4)]}
        self.assertEqual(qualify(self.chain(5), both, model, self.keys, authoritative=False).state, "QUALIFIED")
        self.assertEqual(qualify(self.chain(5), both, model, self.keys, HighWaterMark(7, "sha256:" + f"{7:064x}"),
                                 authoritative=False).state, "BEHIND")
        self.assertEqual(qualify(self.chain(5), both, model, self.keys, retired=True).state, "RETIRED")
        forged = Checkpoint(**checkpoint_body("demo", 9, "sha256:" + "a" * 64, "a" * 40, self.key.key_id), signature="00" * 64)
        self.assertEqual(qualify(self.chain(5), {"w0": [self.cp(4), forged], "w1": [self.cp(4)]}, model, self.keys).head, 4,
                         "a checkpoint that does not verify holds nothing")
        far = qualify(self.chain(8), both, model, self.keys)
        self.assertEqual((far.state, far.head), ("QUALIFIED", 4))
        self.assertTrue(far.critical, "more than one entry beyond the qualified head is an integrity obligation")

    def test_only_declared_witnesses_respond(self) -> None:
        """Review 0e49deb A-B2: quorums count the declared witness set, never any other report key."""

        model = _model(3, 2, 2, 0)
        declared = {"w0": [self.cp(4)], "w1": [self.cp(4)]}
        self.assertEqual(qualify(self.chain(5), declared, model, self.keys).state, "QUALIFIED")
        foreign = {"w0": [self.cp(4)], "not-declared": [self.cp(4)], "also-not": [self.cp(4)]}
        self.assertEqual(qualify(self.chain(5), foreign, model, self.keys).state, "UNQUALIFIED",
                         "relabelled copies of an authentic checkpoint are not distinct witnesses")
        local = WitnessModel("LOCAL_TRUST", 1, 1, 1, 0, (WitnessSpec("local-file", "FILE", "/w"),))
        self.assertEqual(qualify(self.chain(5), {"not-declared": [self.cp(4)]}, local, self.keys).state, "UNQUALIFIED",
                         "the declared witness has not responded")
        duplicated = WitnessModel("TEAM", 3, 2, 2, 0, tuple(WitnessSpec("w0", "GIT", f"/w{i}") for i in range(3)))
        self.assertEqual(qualify(self.chain(5), declared, duplicated, self.keys).state, "UNQUALIFIED",
                         "a witness set without N distinct identities qualifies nothing")

    def test_no_current_head_below_the_retained_high_water_mark(self) -> None:
        """Review 137b763 A-B7: the provisional allowance is for observed checkpoints, never for the mark."""

        model = _model(3, 2, 2, 0)
        through_4 = {"w0": [self.cp(4)], "w1": [self.cp(4)]}
        mark5 = HighWaterMark(5, "sha256:" + f"{5:064x}")
        self.assertEqual(qualify(self.chain(6), through_4, model, self.keys, mark5).state, "UNQUALIFIED",
                         "5 was qualified before: presenting 4 as current would go back")
        control = qualify(self.chain(6), through_4, model, self.keys, HighWaterMark(4, "sha256:" + f"{4:064x}"))
        self.assertEqual((control.state, control.head, control.provisional), ("QUALIFIED", 4, 5),
                         "a successor never qualified stays provisional")
        restored = qualify(self.chain(6), {"w0": [self.cp(4), self.cp(5)], "w1": [self.cp(5)]}, model, self.keys, mark5)
        self.assertEqual((restored.state, restored.head), ("QUALIFIED", 5))

    def test_the_qualified_head_extends_every_observed_checkpoint(self) -> None:
        """Review d8bdfd3 A-B9: an observed newer checkpoint is never relabelled a provisional successor."""

        model = _model(3, 2, 2, 0)
        # head 1 admitted by w0 + w2; a read reaches w0 + w1 only
        partial = {"w0": [self.cp(0), self.cp(1)], "w1": [self.cp(0)], "w2": None}
        for mark in (None, HighWaterMark(0, "sha256:" + f"{0:064x}")):
            with self.subTest(mark=mark):
                self.assertEqual(qualify(self.chain(2), partial, model, self.keys, mark).state, "UNQUALIFIED",
                                 "1 is observed but not confirmable here: no older head is current")
        repaired = {"w0": [self.cp(0), self.cp(1)], "w1": [self.cp(0), self.cp(1)], "w2": None}  # read repair
        self.assertEqual(qualify(self.chain(2), repaired, model, self.keys).head, 1)
        unwitnessed = qualify(self.chain(2), {"w0": [self.cp(0)], "w1": [self.cp(0)], "w2": None}, model, self.keys)
        self.assertEqual((unwitnessed.state, unwitnessed.head, unwitnessed.provisional), ("QUALIFIED", 0, 1),
                         "a successor no responder has a checkpoint for is the provisional successor")
        for p in range(3):  # property: every qualified head extends every observed checkpoint and the mark
            reports = {"w0": [self.cp(q) for q in range(p + 1)], "w1": [self.cp(0)], "w2": [self.cp(q) for q in range(p + 1)]}
            result = qualify(self.chain(3), reports, model, self.keys)
            if result.current:
                observed = max(c.position for cps in reports.values() for c in cps)
                self.assertGreaterEqual(result.head, observed)

    def test_loss_bounds(self) -> None:
        self.assertEqual((loss_status(0, 1, 0, 2), loss_status(1, 1, 0, 2), loss_status(2, 0, 1, 2)),
                         ("PROVED_NEVER_ADMITTED", "POSSIBLY_ADMITTED", "KNOWN_ADMITTED"))

    def test_deployment_classes_sound(self) -> None:
        self.assertEqual((quorum_sound(1, 1, 1, 0), quorum_sound(3, 2, 2, 0), quorum_sound(4, 3, 3, 1),
                          quorum_sound(3, 2, 1, 0)), (True, True, True, False))
        with self.assertRaises(ValueError):
            _model(3, 2, 1, 0).validate()
        _model(3, 2, 2, 0).validate()
        with self.assertRaises(ValueError):
            WitnessModel("TEAM", 3, 2, 2, 0, tuple(WitnessSpec(f"w{i}", "FILE", "x") for i in range(3))).validate()


if __name__ == "__main__":
    unittest.main()
