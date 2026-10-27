"""Phase F step 7e: the witness model per position and witness set redesignation (catalogue §22.4, §23.3-§23.8; plan
§3.4, readings F59-F62).

7e-i: a ``WITNESS_SET_REDESIGNATION`` (or a loss re-establishing the set) starts a segment at its own position, whose
entry belongs to both segments. Qualification reads the newest segment first: its verdict governs unless its holding
from its start is proved never admitted (§23.6's bound), when the older segment reads the redesignation as provisional.
"""

from __future__ import annotations

import unittest

from ssds.admission.engine import AdmissionHalted, EntryInvalid
from ssds.ledger.append import HostKey, append_entry, write_checkpoint
from ssds.ledger.qualification import (Checkpoint, FileWitness, HighWaterMark, WitnessModel, WitnessSpec,
                                       checkpoint_body, checkpoint_message, lineage_witnesses, qualify_segments,
                                       segment_witnesses, segments)
from ssds.ledger.read import Chain, LedgerEntry

from ._fixtures import approve, entry, genesis_record, git, record, sshsig
from .test_admission_requests import RequestFixture
from .test_phase_f_step7c import TeamLedger

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

    def test_a_redesignation_over_a_provisional_entry_raises_no_critical_flag(self) -> None:
        """§23.4: the one chain carrying two entries beyond H* (F61)."""

        from ssds.ledger.qualification import qualify

        chain = self.chain(3, redesign_at=2)
        held = qualify(chain, {"a0": self.holds(0), "a1": self.holds(0)}, OLD, self.keys)
        self.assertEqual((held.state, held.head, held.critical), ("QUALIFIED", 0, ()))
        plain = qualify(self.chain(3, redesign_at=None), {"a0": self.holds(0), "a1": self.holds(0)}, OLD, self.keys)
        self.assertTrue(plain.critical)


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




TEAM_NEW = {"class": "TEAM", "N": 3, "q_a": 2, "r": 2, "f": 0,
            "witnesses": [{"id": f"n{i}", "kind": "GIT", "location": f"git:n{i}"} for i in range(3)]}


def redesignation(actor: str, fields: dict, refs=()) -> dict:
    from ssds.ledger.read import with_id

    return with_id({**record("WITNESS_SET_REDESIGNATION", target=None, actor=actor, fields=fields), "refs": list(refs)})


class LocalRedesign(RequestFixture):
    """7e-ii on the LOCAL_TRUST fixture ledger, to a TEAM set of fixture witnesses (F53)."""

    def setUp(self) -> None:
        super().setUp()
        self.new = {f"n{i}": self.root / f"new-n{i}" for i in range(3)}
        for folder in self.new.values():
            folder.mkdir()
        from ssds.admission.engine import Admission

        self.engine = Admission(self.home, "demo", self.trees, fixture_witnesses=self.new)

    def redesign(self, fields=None, refs=None, engine=None) -> int:
        engine = engine or self.engine
        prepared, prepared_refs = engine.prepare_redesignation(TEAM_NEW)
        rec = redesignation(self.human(), fields or prepared, prepared_refs if refs is None else refs)
        return engine.admit_lifecycle(rec, sshsig(self.private, engine.lifecycle_message(rec)), None)

    def held(self):
        return self.engine.qualification(self.engine.chain())

    def test_a_routine_redesignation_moves_the_ledger_to_the_new_set(self) -> None:
        position = self.redesign()
        held = self.held()
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", position, None))
        chain = self.engine.chain()
        self.assertEqual([(s, m.deployment_class) for s, m in segments(chain)], [(0, "LOCAL_TRUST"), (position, "TEAM")])
        old = FileWitness(self.home.witness_root).read("demo")
        self.assertEqual(max(c.position for c in old), position, "the redesignation is held by both sets")
        for folder in self.new.values():
            self.assertEqual([c.position for c in FileWitness(folder).read("demo")], [position])
        decision = self.engine.admit(self.human_request(), self.baseline)
        self.assertEqual(decision.decision, "ACCEPT")
        self.assertEqual(max(c.position for c in FileWitness(self.home.witness_root).read("demo")), position,
                         "the old set is written no more")
        self.assertEqual(self.held().head, decision.position)

    def human_request(self):
        from ssds.admission.request import request_message
        from ssds.ledger.read import with_id

        from .test_admission_requests import finding

        rec = with_id({**finding(note="after"), "actor": self.human()})
        req = self.request([rec], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return req

    def test_retirement_and_loss_evidence_read_the_new_set(self) -> None:
        """RETIRED under the last segment; review ae5ab38 N1: a head is counted over its own segment's witnesses."""

        position = self.redesign()
        decision = self.engine.admit(self.human_request(), self.baseline)
        lost = self.engine.chain().entries[decision.position]
        ledger = self.home.ledger_repository("demo")
        git(ledger, "update-ref", "refs/ssds/ledger/demo", self.engine.chain().entries[position].commit)
        abandoned = self.engine.prepare_loss()["abandoned"]
        self.assertEqual([(a["digest"], a["status"]) for a in abandoned], [(lost.digest, "KNOWN_ADMITTED")],
                         "held by the TEAM set's q_a; under the old single witness it would read never admitted")
        git(ledger, "update-ref", "refs/ssds/ledger/demo", lost.commit)
        rec = record("LINEAGE_RETIREMENT", target=None, actor=self.human(),
                     fields={"successor": {"ledger_id": "demo-2", "genesis_digest": "sha256:" + "2" * 64}})
        self.engine.admit_lifecycle(rec, sshsig(self.private, self.engine.lifecycle_message(rec)), None)
        self.assertEqual(self.held().state, "RETIRED")

    def test_a_head_in_an_older_segment_is_counted_over_that_segments_witnesses(self) -> None:
        """Review ae5ab38 N1: a conflicting checkpoint before the redesignation, held by the old single witness, is
        known admitted there; counted over the TEAM set it would read never admitted."""

        from ssds.admission.genesis import host_key

        position = self.redesign()
        key = host_key(self.home, "demo")
        body = checkpoint_body("demo", position - 1, "sha256:" + "c" * 64, "c" * 40, key.key_id)
        write_checkpoint(FileWitness(self.home.witness_root),
                         Checkpoint(**body, signature=key.sign(checkpoint_message(body)).hex()))
        abandoned = self.engine.prepare_loss()["abandoned"]
        self.assertEqual([(a["position"], a["status"]) for a in abandoned], [(position - 1, "KNOWN_ADMITTED")])

    def test_retirement_counts_only_the_set_in_force(self) -> None:
        """Step 8a's ``currentness`` (F65): a statement an old witness holds is not counted toward the new set's
        q_a; one old and one new witness holding it is one holder, below TEAM's two."""

        from ssds.admission.genesis import host_key
        from ssds.ledger.append import write_retirement
        from ssds.ledger.qualification import RetirementStatement, retirement_message

        self.redesign()
        key = host_key(self.home, "demo")
        body = {"ledger_id": "demo", "kind": "RETIREMENT", "last_position": 99, "last_entry_digest": "sha256:" + "0" * 64,
                "successor_ledger_id": "demo-2", "successor_genesis_digest": "sha256:" + "2" * 64}
        statement = RetirementStatement(body, ((key.key_id, key.sign(retirement_message(body)).hex()),))
        write_retirement(FileWitness(self.home.witness_root), statement)
        write_retirement(FileWitness(self.new["n0"]), statement)
        self.assertNotEqual(self.held().state, "RETIRED")
        write_retirement(FileWitness(self.new["n1"]), statement)
        self.assertEqual(self.held().state, "RETIRED")

    def test_the_old_set_must_hold_it_where_it_is_reachable(self) -> None:
        import os

        folder = self.home.witness_root / "demo"
        os.chmod(folder, 0o500)
        self.addCleanup(os.chmod, folder, 0o700)
        if os.access(folder, os.W_OK):
            self.skipTest("the permission bits do not bind this user")
        before = len(self.entries())
        with self.assertRaisesRegex(AdmissionHalted, "both"):
            self.redesign()
        self.assertEqual(len(self.entries()), before)

    def test_under_unqualified_it_continues_from_the_intact_head_naming_its_evidence(self) -> None:
        moved = self.root / "lost-witness"
        self.home.witness_root.rename(moved)  # the old set is lost beyond its fault bound
        self.assertEqual(self.held().state, "UNQUALIFIED")
        fields, refs = self.engine.prepare_redesignation(TEAM_NEW)
        self.assertEqual(len(refs), 1)
        with self.assertRaisesRegex(EntryInvalid, "names the report"):
            self.redesign(refs=[])
        position = self.redesign()
        stored = self.engine.chain().entries[position]
        self.assertIn(refs[0]["digest"], stored.objects)
        self.assertEqual((self.held().state, self.held().head), ("QUALIFIED", position))

    def test_content_refusals(self) -> None:
        head = self.engine.chain().entries[-1]
        genesis_model = self.engine.chain().genesis["fields"]["witnesses"]
        unsound = {**TEAM_NEW, "N": 2, "witnesses": TEAM_NEW["witnesses"][:2]}
        before = len(self.entries())
        for fields, refusal in (({"witnesses": genesis_model, "continues_from": head.digest}, "the one in force"),
                                ({"witnesses": unsound, "continues_from": head.digest}, "not sound"),
                                ({"witnesses": TEAM_NEW, "continues_from": "sha256:" + "4" * 64}, "continues_from"),
                                ({"witnesses": TEAM_NEW, "continues_from": head.digest, "note": 1}, "exactly")):
            with self.subTest(refusal=refusal), self.assertRaisesRegex(EntryInvalid, refusal):
                self.redesign(fields=fields)
        with self.assertRaisesRegex(EntryInvalid, "names the report"):
            self.redesign(refs=[{"store": "LEDGER", "digest": "sha256:" + "5" * 64, "media_type": "application/json"}])
        self.assertEqual(len(self.entries()), before)


class TeamRedesign(TeamLedger):
    """7e-ii on a TEAM ledger: over another host's provisional entry, and the loss carrying a redesignation."""

    def other_host(self):
        """A second Admission host key, a trust root of a fresh TEAM genesis built for this case."""

        from ssds.ledger.append import create_ledger_repository, import_commits
        from ssds.ledger.read import with_id

        other = HostKey.generate()
        repository = self.home.ledger_repository("pair")
        create_ledger_repository(repository)
        import_commits(repository, self.product, [self.baseline])
        from ssds.admission.genesis import host_key

        key = host_key(self.home, "pair")
        genesis = genesis_record(key, self.public, self.root, self.baseline, ledger_id="pair")
        genesis["fields"]["trust_roots"]["admission_keys"].append({"id": other.key_id, "public_key": other.public_hex})
        genesis["fields"]["witnesses"] = {"class": "TEAM", "N": 3, "q_a": 2, "r": 2, "f": 0,
                                          "witnesses": [{"id": w, "kind": "GIT", "location": f"git:{w}"} for w in self.roots]}
        genesis["fields"]["deployment_class"] = "TEAM"
        first = append_entry(repository, entry("pair", 0, None, key, lifecycle=approve(with_id(genesis), self.private)),
                             key, None, referenced=[self.baseline])
        for folder in self.roots.values():
            write_checkpoint(FileWitness(folder), first.checkpoint)
        return repository, other, first

    def test_over_another_hosts_provisional_entry(self) -> None:
        """§22.4: appended over it, its admission settles that prefix; review 7d2d1c0 N1."""

        from ssds.admission.engine import Admission

        repository, other, first = self.other_host()
        adoption = record("RULESET_ADOPTION", target=None, actor=self.human(),
                          fields={"system": "ssds-rules/1", "policy": "sha256:" + "1" * 64,
                                  "analyzers": ["ssds.analyzer.python/1"]})
        append_entry(repository, entry("pair", 1, first.digest, other, lifecycle=adoption, obs=self.baseline), other,
                     first.commit)  # the other host crashed before distributing it: provisional, no checkpoint
        new = {f"n{i}": self.root / f"pair-n{i}" for i in range(3)}
        for folder in new.values():
            folder.mkdir()
        engine = Admission(self.home, "pair", self.trees, fixture_witnesses={**self.roots, **new})
        held = engine.qualification(engine.chain())
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", 0, 1))
        fields, refs = engine.prepare_redesignation(TEAM_NEW)
        rec = redesignation(self.human(), fields, refs)
        position = engine.admit_lifecycle(rec, sshsig(self.private, engine.lifecycle_message(rec)), None)
        held = engine.qualification(engine.chain())
        self.assertEqual((position, held.state, held.head, held.provisional), (2, "QUALIFIED", 2, None))

    def test_a_loss_re_establishes_the_witness_set(self) -> None:
        """§23.8's witness-loss row with a later head (F62): the loss carries the redesignation."""

        one = self.append(self.genesis, 1, "1")
        self.checkpoint(one, "w0", "w1", "w2")
        self.rewind_to_genesis()
        new = {f"n{i}": self.root / f"team-n{i}" for i in range(3)}
        for folder in new.values():
            folder.mkdir()
        admission = self.team({"w0": self.roots["w0"], **new})  # two of the old three lost
        self.assertEqual(admission.qualification(admission.chain()).state, "UNQUALIFIED")
        fields = admission.prepare_loss()
        self.assertEqual([a["status"] for a in fields["abandoned"]], ["POSSIBLY_ADMITTED"])
        with self.assertRaisesRegex(AdmissionHalted, "reading F51"):
            self.loss(admission)  # under the lost set, as 7c found
        with self.assertRaisesRegex(EntryInvalid, "a later head is in evidence"):
            prepared, refs = admission.prepare_redesignation(TEAM_NEW)
            rec = redesignation(self.human(), prepared, refs)
            admission.admit_lifecycle(rec, sshsig(self.private, admission.lifecycle_message(rec)), None)
        carried = {**fields, "controls": {**fields["controls"], "witnesses": TEAM_NEW}}
        rec = record("LEDGER_LOSS", target=None, actor=self.human(), fields=carried)
        position = admission.admit_lifecycle(rec, sshsig(self.private, admission.lifecycle_message(rec)), None)
        held = admission.qualification(admission.chain())
        self.assertEqual((held.state, held.head), ("QUALIFIED", position))
        self.assertEqual([s for s, _ in segments(admission.chain())], [0, position])
        from ssds.admission.loss import controls_problems

        bad = {**fields["controls"], "witnesses": {**TEAM_NEW, "q_a": 1}}
        self.assertTrue(any("not sound" in p for p in controls_problems(bad, fields["controls"])))

    def test_a_loss_changing_the_set_is_held_by_the_reachable_old_set_too(self) -> None:
        """F61 for a loss (F62): the old set responds but only one witness can write, so it cannot hold the loss."""

        import os

        one = self.append(self.genesis, 1, "1")
        self.checkpoint(one, "w0", "w1")
        self.rewind_to_genesis()
        new = {f"n{i}": self.root / f"team-n{i}" for i in range(3)}
        for folder in new.values():
            folder.mkdir()
        admission = self.team({**self.roots, **new})
        self.assertEqual(admission.qualification(admission.chain()).state, "ROLLBACK")
        for w in ("w1", "w2"):
            folder = self.roots[w] / "team"
            os.chmod(folder, 0o500)
            self.addCleanup(os.chmod, folder, 0o700)
            if os.access(folder, os.W_OK):
                self.skipTest("the permission bits do not bind this user")
        fields = admission.prepare_loss()
        carried = {**fields, "controls": {**fields["controls"], "witnesses": TEAM_NEW}}
        rec = record("LEDGER_LOSS", target=None, actor=self.human(), fields=carried)
        with self.assertRaisesRegex(AdmissionHalted, "both"):
            admission.admit_lifecycle(rec, sshsig(self.private, admission.lifecycle_message(rec)), None)
        self.assertEqual(len(admission.chain().entries), 1)


if __name__ == "__main__":
    unittest.main()
