"""Phase F step 7e: the witness model per position and witness set redesignation (catalogue §22.4, §23.3-§23.8; plan
§3.4, readings F59-F62).

7e-i: a ``WITNESS_SET_REDESIGNATION`` (or a loss re-establishing the set) starts a segment at its own position, whose
entry belongs to both segments. Qualification reads the newest segment first: its verdict governs unless its holding
from its start is proved never admitted (§23.6's bound), when the older segment reads the redesignation as provisional.
"""

from __future__ import annotations

import unittest

from ssds.ledger.append import HostKey, append_entry, write_checkpoint
from ssds.ledger.qualification import (Checkpoint, FileWitness, HighWaterMark, WitnessModel, WitnessSpec,
                                       checkpoint_body, checkpoint_message, lineage_witnesses, qualify_segments,
                                       segment_witnesses, segments)
from ssds.ledger.read import Chain, LedgerEntry

from ._fixtures import entry, record
from .test_admission_requests import RequestFixture

OLD = WitnessModel("TEAM", 3, 2, 2, 0, tuple(WitnessSpec(f"a{i}", "GIT", f"old{i}") for i in range(3)))
NEW = WitnessModel("HARDENED", 4, 3, 3, 1, tuple(WitnessSpec(f"n{i}", "GIT", f"new{i}") for i in range(4)))
P = 3  # the redesignation's position


class Segments(unittest.TestCase):
    def setUp(self) -> None:
        self.key = HostKey.generate()
        self.keys = {self.key.key_id: self.key.public_hex}

    def chain(self, length: int, redesign_at: int | None = P, loss: bool = False) -> Chain:
        def body(i: int) -> dict:
            if i == 0:
                return {"lifecycle": {"kind": "GENESIS", "fields": {"witnesses": OLD.to_json()}}}
            if i == redesign_at:
                if loss:
                    return {"lifecycle": {"kind": "LEDGER_LOSS", "fields": {"controls": {"witnesses": NEW.to_json()}}}}
                return {"lifecycle": {"kind": "WITNESS_SET_REDESIGNATION", "fields": {"witnesses": NEW.to_json()}}}
            return {}

        return Chain("demo", tuple(LedgerEntry(i, f"{i:040x}", (), body(i), b"", b"", f"sha256:{i:064x}", {})
                                   for i in range(length)))

    def cp(self, position: int, digest: str | None = None) -> Checkpoint:
        body = checkpoint_body("demo", position, digest or f"sha256:{position:064x}", f"{position:040x}",
                               self.key.key_id)
        return Checkpoint(**body, signature=self.key.sign(checkpoint_message(body)).hex())

    def holds(self, *positions: int) -> list[Checkpoint]:
        return [self.cp(p) for p in positions]

    def qualify(self, chain, reports, mark=None, authoritative=True):
        return qualify_segments(chain, reports, self.keys, mark, authoritative)

    def old_through(self, last: int) -> dict:
        return {"a0": self.holds(*range(last + 1)), "a1": self.holds(*range(last + 1)), "a2": None}

    def test_segments_and_where_a_checkpoint_goes(self) -> None:
        chain = self.chain(6)
        self.assertEqual([(start, model.deployment_class) for start, model in segments(chain)],
                         [(0, "TEAM"), (P, "HARDENED")])
        ids = lambda position: sorted(w.id for w in segment_witnesses(chain, position))  # noqa: E731
        self.assertEqual(ids(P - 1), ["a0", "a1", "a2"])
        self.assertEqual(ids(P), ["a0", "a1", "a2", "n0", "n1", "n2", "n3"], "the redesignation goes to both sets")
        self.assertEqual(ids(P + 1), ["n0", "n1", "n2", "n3"])
        self.assertEqual(len(lineage_witnesses(chain)), 7)
        self.assertEqual([s for s, _ in segments(self.chain(6, loss=True))], [0, P], "a loss re-establishing the set")
        same = self.chain(6, loss=True)
        same = Chain("demo", same.entries[:P] + (LedgerEntry(P, f"{P:040x}", (), {"lifecycle": {
            "kind": "LEDGER_LOSS", "fields": {"controls": {"witnesses": OLD.to_json()}}}}, b"", b"",
            f"sha256:{P:064x}", {}),) + same.entries[P + 1:])
        self.assertEqual([s for s, _ in segments(same)], [0], "a loss keeping the set starts no segment")

    def test_a_held_redesignation_qualifies_under_the_new_set(self) -> None:
        reports = {**self.old_through(P), **{f"n{i}": self.holds(P, 4, 5) for i in range(3)}, "n3": None}
        held = self.qualify(self.chain(6), reports)
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", 5, None))
        fresh = self.qualify(self.chain(6), reports, authoritative=False)
        self.assertEqual((fresh.state, fresh.head), ("QUALIFIED", 5), "a fresh clone, no mark")

    def test_a_redesignation_the_new_set_does_not_hold_is_provisional(self) -> None:
        nothing = {f"n{i}": [] for i in range(4)}
        for old in (self.old_through(P - 1), self.old_through(P)):  # the old set without and with its copy of P
            with self.subTest(old_holds_p=P in [c.position for c in old["a0"]]):
                held = self.qualify(self.chain(P + 1), {**old, **nothing})
                self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", P - 1, P))

    def test_truncation_to_p_while_the_new_set_holds_later_reads_rollback(self) -> None:
        """Check of c36b278e B1: an older segment never masks the newer one's ROLLBACK."""

        reports = {**self.old_through(P), **{f"n{i}": self.holds(P, 4, 5) for i in range(3)}, "n3": []}
        self.assertEqual(self.qualify(self.chain(P + 1), reports).state, "ROLLBACK")

    def test_one_denying_new_witness_does_not_open_the_old_set(self) -> None:
        """Re-check of 3b6ebcc0 R1: HARDENED, h = 2, f = 1: not proved never admitted, so the new verdict governs."""

        reports = {**self.old_through(P), "n0": self.holds(P, 4, 5), "n1": self.holds(P, 4, 5), "n2": [], "n3": []}
        self.assertEqual(self.qualify(self.chain(P + 1), reports).state, "ROLLBACK")

    def test_one_partial_copy_is_still_provisional(self) -> None:
        """h = 1 under HARDENED: 1 + 0 + 1 < 3, proved never admitted from p: the older segment reads it."""

        reports = {**self.old_through(P - 1), "n0": self.holds(P), "n1": [], "n2": [], "n3": []}
        held = self.qualify(self.chain(P + 1), reports)
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", P - 1, P))

    def test_a_third_segment_unheld_is_provisional_over_the_second(self) -> None:
        """Review ae5ab38 B1: S0 TEAM from 0, S1 HARDENED from 3, S2 TEAM from 5; S1 holds 3-5, S2 holds nothing."""

        third = WitnessModel("TEAM", 3, 2, 2, 0, tuple(WitnessSpec(f"t{i}", "GIT", f"third{i}") for i in range(3)))
        base = self.chain(6)
        chain = Chain("demo", base.entries[:5] + (LedgerEntry(5, f"{5:040x}", (), {"lifecycle": {
            "kind": "WITNESS_SET_REDESIGNATION", "fields": {"witnesses": third.to_json()}}}, b"", b"",
            f"sha256:{5:064x}", {}),))
        self.assertEqual([s for s, _ in segments(chain)], [0, P, 5])
        reports = {**self.old_through(P), **{f"n{i}": self.holds(P, 4, 5) for i in range(3)}, "n3": None,
                   **{f"t{i}": [] for i in range(3)}}
        held = self.qualify(chain, reports)
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", 4, 5))
        held = self.qualify(chain, {**reports, **{f"t{i}": self.holds(5) for i in range(2)}})
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", 5, None), "once the third set holds it")

    def test_forged_new_checkpoints_hold_nothing(self) -> None:
        stranger = HostKey.generate()
        body = checkpoint_body("demo", P, f"sha256:{P:064x}", f"{P:040x}", stranger.key_id)
        forged = Checkpoint(**body, signature=stranger.sign(checkpoint_message(body)).hex())
        reports = {**self.old_through(P - 1), **{f"n{i}": [forged] for i in range(4)}}
        held = self.qualify(self.chain(P + 1), reports)
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", P - 1, P))

    def test_an_unreachable_new_set_is_unqualified(self) -> None:
        reports = {**self.old_through(P), **{f"n{i}": None for i in range(4)}}
        self.assertEqual(self.qualify(self.chain(P + 2), reports).state, "UNQUALIFIED")

    def test_an_old_set_fork_after_a_held_redesignation_is_not_read(self) -> None:
        old = {w: cps + [self.cp(4, "sha256:" + "e" * 64)] for w, cps in self.old_through(P).items() if cps}
        reports = {**old, "a2": None, **{f"n{i}": self.holds(P, 4) for i in range(3)}, "n3": None}
        held = self.qualify(self.chain(5), reports)
        self.assertEqual((held.state, held.head), ("QUALIFIED", 4))

    def test_a_mark_is_read_in_the_segment_that_governs(self) -> None:
        reports = {**self.old_through(P), **{f"n{i}": self.holds(P, 4) for i in range(3)}, "n3": None}
        self.assertEqual(self.qualify(self.chain(5), reports, HighWaterMark(7, "sha256:" + "7" * 64)).state, "ROLLBACK")

    def test_an_unparseable_new_model_qualifies_nothing(self) -> None:
        chain = self.chain(5)
        broken = Chain("demo", chain.entries[:P] + (LedgerEntry(
            P, chain.entries[P].commit, (), {"lifecycle": {"kind": "WITNESS_SET_REDESIGNATION", "fields": {}}}, b"",
            b"", chain.entries[P].digest, {}),) + chain.entries[P + 1:])
        self.assertEqual(self.qualify(broken, self.old_through(4)).state, "UNQUALIFIED")


class Readers(RequestFixture):
    """Admission and the Interface agree across a redesignation on a real fixture ledger (LOCAL_TRUST to another
    LOCAL_TRUST file witness, which both readers reach)."""

    def test_admission_and_the_interface_agree_across_segments(self) -> None:
        from ssds.admission.genesis import host_key
        from ssds.cli import HomeAccess
        from ssds.interface.operations import present

        key = host_key(self.home, "demo")
        new_root = self.root / "new-witness"
        new_root.mkdir()
        model = {"class": "LOCAL_TRUST", "N": 1, "q_a": 1, "r": 1, "f": 0,
                 "witnesses": [{"id": "fresh", "kind": "FILE", "location": str(new_root)}]}
        head = self.entries()[-1]
        redesign = record("WITNESS_SET_REDESIGNATION", target=None, actor=self.human(),
                          fields={"witnesses": model, "continues_from": head.digest})
        appended = append_entry(self.home.ledger_repository("demo"), entry("demo", head.position + 1, head.digest, key,
                                                                           lifecycle=redesign), key, head.commit)
        for root in (self.home.witness_root, new_root):
            write_checkpoint(FileWitness(root), appended.checkpoint)
        views = lambda: (self.admission.qualification(self.admission.chain()),  # noqa: E731
                         present(HomeAccess(self.home, "demo"), self.trees).qualification)
        for held in views():
            self.assertEqual((held.state, held.head), ("QUALIFIED", appended.position))
        later = append_entry(self.home.ledger_repository("demo"),
                             entry("demo", appended.position + 1, appended.digest, key,
                                   lifecycle=record("RULESET_ADOPTION", target=None, actor=self.human(),
                                                    fields={"system": "ssds-rules/1", "policy": "sha256:" + "0" * 64,
                                                            "analyzers": ["ssds.analyzer.python/1"]}),
                                   obs=self.baseline), key, appended.commit)
        self.admission.distribute(self.admission.chain().entries[later.position])
        self.assertEqual(len(FileWitness(self.home.witness_root).read("demo")), appended.position + 1,
                         "after the redesignation, only the new set is written")
        for held in views():
            self.assertEqual((held.state, held.head), ("QUALIFIED", later.position))


if __name__ == "__main__":
    unittest.main()
