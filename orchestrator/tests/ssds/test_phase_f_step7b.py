"""Phase F step 7b: the recovery gate and the trial qualification (catalogue §5.7, §22.1, §23.4-§23.8, §25.2; plan
§3.4, readings F50-F53).

A recovery-tier lifecycle record passes one gate: ``obs = null``, the human gate's approval for this ledger, position
and head, and the qualification states its kind is admitted in (F50). Before it is appended, the extended chain is
qualified on trial, its checkpoint taken as held by every witness this host can write (F51). The losses, fork
resolutions and redesignations pass the gate and are refused by their content checks until 7c-7e. ``TEAM`` and
``HARDENED`` quorums run on fixture witnesses (F53).
"""

from __future__ import annotations

import os
import re
import unittest
from pathlib import Path
from unittest import mock

from ssds.admission.engine import RECOVERY_STATES, Admission, AdmissionHalted, EntryInvalid, admissible
from ssds.admission.genesis import host_key
from ssds.ledger.append import append_entry, create_ledger_repository, import_commits, write_checkpoint
from ssds.ledger.qualification import FileWitness, Qualification
from ssds.ledger.read import ledger_ref, with_id

from ._fixtures import approve, entry, genesis_record, git, record, sshsig
from .test_admission_requests import RequestFixture

SRC = Path(__file__).resolve().parents[2] / "src" / "ssds"
SUCCESSOR = {"ledger_id": "demo-2", "genesis_digest": "sha256:" + "2" * 64}
LOSS = {"retained": {}, "abandoned": [], "report": "sha256:" + "0" * 64, "controls": {}}
FIELDS = {"LEDGER_LOSS": LOSS, "FORK_RESOLUTION": {"abandoned": []},
          "WITNESS_SET_REDESIGNATION": {"witnesses": {}, "continues_from": "sha256:" + "0" * 64},
          "REPLICA_REDESIGNATION": {"location": {}}, "LINEAGE_RETIREMENT": {"successor": SUCCESSOR}}


class Denying(FileWitness):
    """A witness that holds every checkpoint written to it and reports none: one of ``f`` faulty witnesses."""

    def read(self, ledger_id):
        return [] if self.root.is_dir() else None


class GateTable(unittest.TestCase):
    def test_each_kind_by_state(self) -> None:
        settled, provisional = Qualification("QUALIFIED", 3, "d", None), Qualification("QUALIFIED", 3, "d", 4)
        states = {"settled": settled, "provisional": provisional, **{s: Qualification(s) for s in
                  ("ROLLBACK", "FORK", "UNQUALIFIED", "BEHIND", "RETIRED", "INTEGRITY_HALT")}}
        expected = {
            "LINEAGE_RETIREMENT": {"settled"},
            "LEDGER_LOSS": {"ROLLBACK", "FORK", "UNQUALIFIED"},
            "FORK_RESOLUTION": {"FORK", "ROLLBACK"},  # check of 31b3ed34 B1
            "WITNESS_SET_REDESIGNATION": {"settled", "provisional", "UNQUALIFIED"},  # B3
            "REPLICA_REDESIGNATION": set(),
            "KEY_LIFECYCLE": set(), "GENESIS": set(), "OTHER": set(),
        }
        for kind, admitted in expected.items():
            for name, held in states.items():
                with self.subTest(kind=kind, state=name):
                    self.assertEqual(admissible(kind, held), name in admitted)
        self.assertEqual(set(RECOVERY_STATES), {k for k, v in expected.items() if k in FIELDS})

    def test_the_composition_root_never_passes_fixture_witnesses(self) -> None:
        """F53: only tests map fixture witnesses; the real ledger's witnesses are its FILE ones (F3)."""

        users = sorted(str(p.relative_to(SRC)) for p in SRC.rglob("*.py") if "fixture_witnesses" in p.read_text())
        self.assertEqual(users, ["admission/engine.py"])


class Gate(RequestFixture):
    def recovery(self, kind: str, private=None, message: bytes | None = None, admission=None):
        admission = admission or self.admission
        rec = record(kind, target=None, actor=self.human(), fields=FIELDS[kind])
        signed = sshsig(private or self.private, message if message is not None else admission.lifecycle_message(rec))
        return admission.admit_lifecycle(rec, signed, None)

    def rewind(self) -> None:
        """The ledger ref rewound one entry below the witnessed head: ROLLBACK."""

        ledger = self.home.ledger_repository("demo")
        tip = git(ledger, "rev-parse", ledger_ref("demo"))
        git(ledger, "update-ref", ledger_ref("demo"), git(ledger, "rev-parse", tip + "^"))
        self.assertEqual(self.admission.qualification(self.admission.chain()).state, "ROLLBACK")

    def test_a_qualified_ledger_admits_no_loss_or_fork_resolution(self) -> None:
        before = len(self.entries())
        for kind in ("LEDGER_LOSS", "FORK_RESOLUTION", "REPLICA_REDESIGNATION"):
            with self.subTest(kind=kind), self.assertRaisesRegex(AdmissionHalted, "reading F50"):
                self.recovery(kind)
        self.assertEqual(len(self.entries()), before)

    def test_under_rollback_a_loss_and_a_fork_resolution_pass_the_gate(self) -> None:
        """Each then meets its content check (7c's, and 7d's unbuilt one); B1: a fork resolution under ROLLBACK."""

        self.rewind()
        before = len(self.entries())
        for kind, refusal in (("LEDGER_LOSS", "recomputed"), ("FORK_RESOLUTION", "step 7d")):  # 7c builds the loss
            with self.subTest(kind=kind), self.assertRaisesRegex(EntryInvalid, refusal):
                self.recovery(kind)
        with self.assertRaisesRegex(AdmissionHalted, "reading F50"):
            self.recovery("WITNESS_SET_REDESIGNATION")
        self.assertEqual(len(self.entries()), before)

    def test_a_settled_head_takes_a_redesignation_through_the_gate(self) -> None:
        """B3: the routine change of a witness set; its content check is 7e's."""

        with self.assertRaisesRegex(EntryInvalid, "step 7e"):
            self.recovery("WITNESS_SET_REDESIGNATION")

    def test_nothing_is_admitted_under_an_integrity_halt(self) -> None:
        """§5.7's route waits for F47's ref restore (B2, Phase H)."""

        before = len(self.entries())
        with mock.patch.object(Admission, "qualification", return_value=Qualification("INTEGRITY_HALT")):
            for kind in FIELDS:
                with self.subTest(kind=kind), self.assertRaises(AdmissionHalted):
                    self.recovery(kind)
        self.assertEqual(len(self.entries()), before)

    def test_a_kind_outside_this_path_is_refused_before_any_state_is_read(self) -> None:
        for kind in ("GENESIS", "RULESET_ADOPTION", "FINDING"):
            rec = record(kind, target=None, actor=self.human())
            with self.subTest(kind=kind), mock.patch.object(Admission, "qualification") as qualification, \
                    self.assertRaisesRegex(EntryInvalid, "not admitted through this path"):
                self.admission.admit_lifecycle(rec, "", None)
            qualification.assert_not_called()

    def test_a_recovery_record_carries_obs_null(self) -> None:
        self.rewind()
        rec = record("LEDGER_LOSS", target=None, actor=self.human(), fields=LOSS)
        with self.assertRaisesRegex(EntryInvalid, "obs = null"):
            self.admission.admit_lifecycle(rec, sshsig(self.private, self.admission.lifecycle_message(rec)),
                                           self.baseline)

    def test_the_approval_names_this_position_and_head(self) -> None:
        self.rewind()
        head = self.admission.chain().entries[-1]
        for message in (f"ssds lifecycle demo #{head.position + 2} {head.digest} x\n".encode(),
                        f"ssds lifecycle demo #{head.position + 1} sha256:{'1' * 64} x\n".encode()):
            with self.subTest(message=message), self.assertRaisesRegex(EntryInvalid, "approval"):
                self.recovery("LEDGER_LOSS", message=message)

    def test_an_approval_from_an_earlier_head_is_not_replayed(self) -> None:
        rec = record("LINEAGE_RETIREMENT", target=None, actor=self.human(), fields=FIELDS["LINEAGE_RETIREMENT"])
        early = sshsig(self.private, self.admission.lifecycle_message(rec))
        self.lifecycle("REGISTER", self.issuer_at("second").trust_root())
        before = len(self.entries())
        with self.assertRaisesRegex(EntryInvalid, "approval"):
            self.admission.admit_lifecycle(rec, early, None)
        self.assertEqual(len(self.entries()), before)

    def test_an_own_provisional_entry_is_completed_before_the_gate(self) -> None:
        """6b's recovery runs first: the completed entry is settled, and a retirement then passes the gate."""

        with mock.patch("ssds.admission.engine.write_checkpoint", side_effect=OSError("crash")):
            with self.assertRaises(AdmissionHalted):
                self.lifecycle("REGISTER", self.issuer_at("second").trust_root())
        held = self.admission.qualification(self.admission.chain())
        self.assertIsNotNone(held.provisional)
        position = self.recovery("LINEAGE_RETIREMENT")
        self.assertEqual(position, held.provisional + 1)

    def test_an_unpublished_retirement_halts_every_recovery_kind(self) -> None:
        """A settled head goes through the held head, which completes a retirement's statement and halts (7a)."""

        with mock.patch("ssds.admission.engine.write_retirement", side_effect=OSError("crash")):
            with self.assertRaises(AdmissionHalted):
                self.recovery("LINEAGE_RETIREMENT")
        before = len(self.entries())
        with self.assertRaisesRegex(AdmissionHalted, "retired"):
            self.recovery("WITNESS_SET_REDESIGNATION")
        self.assertEqual(len(self.entries()), before)
        self.assertEqual(self.admission.qualification(self.admission.chain()).state, "RETIRED")


class Trial(RequestFixture):
    """The trial qualification on ledgers whose genesis declares TEAM or HARDENED fixture witnesses (F53)."""

    def ledger(self, ledger_id: str, cls: str, n: int, q_a: int, r: int, f: int):
        key = host_key(self.home, ledger_id)
        repository = self.home.ledger_repository(ledger_id)
        create_ledger_repository(repository)
        import_commits(repository, self.product, [self.baseline])
        roots = {f"w{i}": self.root / f"{ledger_id}-w{i}" for i in range(n)}
        for folder in roots.values():
            folder.mkdir()
        genesis = genesis_record(key, self.public, self.root, self.baseline, ledger_id=ledger_id)
        genesis["fields"]["witnesses"] = {"class": cls, "N": n, "q_a": q_a, "r": r, "f": f,
                                          "witnesses": [{"id": w, "kind": "GIT", "location": f"git:{w}"} for w in roots]}
        genesis["fields"]["deployment_class"] = cls
        genesis = approve(with_id(genesis), self.private)
        appended = append_entry(repository, entry(ledger_id, 0, None, key, lifecycle=genesis), key, None,
                                referenced=[self.baseline])
        for folder in roots.values():
            write_checkpoint(FileWitness(folder), appended.checkpoint)
        return roots

    def retire(self, ledger_id: str, witnesses) -> Admission:
        admission = Admission(self.home, ledger_id, self.trees, fixture_witnesses=witnesses)
        rec = record("LINEAGE_RETIREMENT", target=None, actor=self.human(), fields={"successor": SUCCESSOR})
        admission.admit_lifecycle(rec, sshsig(self.private, admission.lifecycle_message(rec)), None)
        return admission

    def length(self, ledger_id: str) -> int:
        return len(Admission(self.home, ledger_id, self.trees).chain().entries)

    def unwritable(self, folder: Path) -> None:
        os.chmod(folder, 0o500)
        self.addCleanup(os.chmod, folder, 0o700)
        if os.access(folder, os.W_OK):
            self.skipTest("the permission bits do not bind this user")

    def test_team_holds_with_one_witness_unwritable(self) -> None:
        roots = self.ledger("team", "TEAM", 3, 2, 2, 0)
        self.unwritable(roots["w0"] / "team")
        admission = self.retire("team", roots)
        self.assertEqual(admission.qualification(admission.chain()).state, "RETIRED")

    def test_team_refuses_what_one_writable_witness_cannot_hold(self) -> None:
        roots = self.ledger("team", "TEAM", 3, 2, 2, 0)
        self.unwritable(roots["w0"] / "team")
        self.unwritable(roots["w1"] / "team")
        with self.assertRaisesRegex(AdmissionHalted, "reading F51"):
            self.retire("team", roots)
        self.assertEqual(self.length("team"), 1)

    def test_hardened_holds_with_one_witness_unreachable(self) -> None:
        roots = self.ledger("hard", "HARDENED", 4, 3, 3, 1)
        reachable = {w: p for w, p in roots.items() if w != "w3"}
        admission = self.retire("hard", reachable)
        self.assertEqual(admission.qualification(admission.chain()).state, "RETIRED")

    def test_hardened_refuses_with_one_unreachable_and_one_denying(self) -> None:
        """With w3 unreachable and w2 denying what it holds, two report the entry: below q_a = 3."""

        roots = self.ledger("hard", "HARDENED", 4, 3, 3, 1)
        witnesses = {"w0": roots["w0"], "w1": roots["w1"], "w2": Denying(roots["w2"])}
        with self.assertRaises(AdmissionHalted):
            self.retire("hard", witnesses)
        self.assertEqual(self.length("hard"), 1)

    def test_a_trial_names_the_extended_chain(self) -> None:
        roots = self.ledger("team", "TEAM", 3, 2, 2, 0)
        admission = Admission(self.home, "team", self.trees, fixture_witnesses=roots)
        chain = admission.chain()
        head = chain.entries[-1]
        probe = entry("team", 1, head.digest, admission.key,
                      lifecycle=record("LINEAGE_RETIREMENT", target=None, actor=self.human(),
                                       fields={"successor": SUCCESSOR}))
        held = admission.trial_qualification(chain, probe)
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", 1, None))
        self.assertEqual(self.length("team"), 1, "a trial appends nothing")
        self.assertTrue(re.fullmatch(r"sha256:[0-9a-f]{64}", held.head_digest))


if __name__ == "__main__":
    unittest.main()
