"""Phase F step 7c: ``LEDGER_LOSS`` (catalogue §23.6, §23.8; plan §3.4, readings F54-F57).

A loss names the retained head, the replica's last readable entry, and exactly the abandoned heads the witnesses and
the high-water mark show beyond it or off its chain, each with its recomputed admission status; the stored
qualification report by digest; and the controls in force, unchanged (F46). Admission recomputes every field. A loss
abandoning only proved-never-admitted heads is a fork resolution, and one abandoning nothing a redesignation. Once
admitted, qualification reads the named heads as abandoned and derivation's boundary withholds what came before.
"""

from __future__ import annotations

import dataclasses
import json
import unittest
from unittest import mock

from ssds.admission.engine import Admission, AdmissionHalted, EntryInvalid
from ssds.admission.genesis import host_key
from ssds.derivation import Consequences, History, derive
from ssds.ledger.append import AppendRefused, append_entry, create_ledger_repository, import_commits, write_checkpoint
from ssds.ledger.qualification import FileWitness
from ssds.ledger.read import ledger_ref, read_chain, with_id

from ._fixtures import approve, commit, entry, genesis_record, git, record, sshsig
from .test_admission_requests import RequestFixture, finding


class LossFixture(RequestFixture):
    """A ledger's loss helpers; no tests of its own, so later steps subclass it."""

    def human_request(self, records):
        from ssds.admission.request import request_message

        req = self.request(records, base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return req

    def admit_finding(self, note: str):
        rec = with_id({**finding(note=note), "actor": self.human()})
        decision = self.admit(self.human_request([rec]))
        self.assertEqual(decision.decision, "ACCEPT")
        return decision

    def rewind(self, steps: int = 1) -> None:
        ledger = self.home.ledger_repository("demo")
        tip = git(ledger, "rev-parse", ledger_ref("demo"))
        git(ledger, "update-ref", ledger_ref("demo"), git(ledger, "rev-parse", f"{tip}~{steps}"))

    def loss(self, fields=None, admission=None) -> int:
        admission = admission or self.admission
        rec = record("LEDGER_LOSS", target=None, actor=self.human(), fields=fields or admission.prepare_loss())
        return admission.admit_lifecycle(rec, sshsig(self.private, admission.lifecycle_message(rec)), None)

    def state(self):
        return self.admission.qualification(self.admission.chain())


class Loss(LossFixture):
    # -- §23.8's rows ------------------------------------------------------------------------------------------

    def test_a_truncated_ledger_takes_a_loss_and_then_absorbs_a_newer_product(self) -> None:
        self.admit_finding("one")
        lost = self.admit_finding("two")
        lost_digest = self.entries()[-1].digest
        self.rewind()
        self.assertEqual(self.state().state, "ROLLBACK")
        replica = self.entries()[-1]
        fields = self.admission.prepare_loss()
        self.assertEqual(fields["retained"], {"position": replica.position, "digest": replica.digest})
        self.assertEqual(fields["abandoned"], [{"position": lost.position, "digest": lost_digest,
                                                "status": "KNOWN_ADMITTED"}])
        self.assertEqual(fields["controls"]["trust_roots"]["human_mechanism"], "SSHSIG", "genesis's full shape")
        self.assertEqual([k["id"] for k in fields["controls"]["trust_roots"]["dispatcher_keys"]],
                         [self.issuer.trust_root()["id"]], "the folded issue key, registered after genesis")
        position = self.loss(fields)
        self.assertEqual(position, replica.position + 1)
        held = self.state()
        self.assertEqual((held.state, held.head, held.provisional), ("QUALIFIED", position, None))
        self.assertEqual(self.home.high_water("demo").get().position, position, "the mark follows the loss")
        stored = json.loads(self.entries()[-1].objects[fields["report"]])
        self.assertEqual(stored["replica_head"], fields["retained"])
        self.assertIn(position, History(read_chain(self.home.ledger_repository("demo"), "demo"), self.trees).boundaries)
        # the newer product is absorbed by the next ordinary entry (6a)
        (self.product / "guide.md").write_text("# Guide\n\nnewer\n")
        newer = commit(self.product, "newer")
        admission = Admission(self.home, "demo", self.trees, product=self.product)
        rec = with_id({**finding(note="after"), "actor": self.human()})
        decision = admission.admit(self.human_request([rec]), newer)
        self.assertEqual(self.entries()[position + 1].entry["entry_kind"], "ABSORPTION")
        self.assertEqual(decision.decision, "ACCEPT")

    def test_a_stale_consistent_restore_resurrects_nothing(self) -> None:
        """Ledger and product restored to one stale snapshot: the boundary alone protects (§23.6)."""

        from .test_phase_f_step4b import derive_state

        rev = derive_state(self).subject_triple("guide")[2]
        proposal = with_id({**record("EQUIVALENCE", target={"unit": "guide", "from": rev, "to": rev,
                                                            "class": "EDITORIAL"}, outcome="EQUIVALENT"),
                            "actor": self.human()})  # a permissive record in effect at the retained head
        accepted = self.admit(self.human_request([proposal]))
        self.assertEqual(accepted.decision, "ACCEPT")
        before = derive(read_chain(self.home.ledger_repository("demo"), "demo"), self.trees)
        self.assertTrue(before.s.cont(proposal["id"]))
        self.admit_finding("lost")
        self.rewind()
        self.loss()
        after = derive(read_chain(self.home.ledger_repository("demo"), "demo"), self.trees)
        self.assertFalse(after.s.cont(proposal["id"]), "withheld by the boundary unless held")
        # §23.6 requalifies what was in effect at R; this equivalence was not current there, so nothing is owed. The
        # positive REQUALIFY case is derivation's, tested in test_s3 and test_support (no permissive record Phase F's
        # admission accepts is current at a fixture head)
        self.assertEqual(before.current(proposal["id"]), 0)
        self.assertNotIn((proposal["id"],), [o.about for o in Consequences(after).obligations if o.kind == "REQUALIFY"])

    def test_a_fork_takes_a_loss_naming_the_admitted_side(self) -> None:
        """§23.6: abandoning a known-admitted head is a loss, whichever state it is recorded in."""

        lost = self.admit_finding("witnessed")
        lost_digest = self.entries()[-1].digest
        self.rewind()
        head = self.entries()[-1]
        key = host_key(self.home, "demo")
        other = record("RULESET_ADOPTION", target=None, actor=self.human(),
                       fields={"system": "ssds-rules/1", "policy": "sha256:" + "0" * 64,
                               "analyzers": ["ssds.analyzer.python/1"]})
        append_entry(self.home.ledger_repository("demo"), entry("demo", head.position + 1, head.digest, key,
                                                                lifecycle=other, obs=self.baseline), key, head.commit)
        self.assertEqual(self.state().state, "FORK")
        fields = self.admission.prepare_loss()
        self.assertEqual(fields["abandoned"], [{"position": lost.position, "digest": lost_digest,
                                                "status": "KNOWN_ADMITTED"}])
        self.assertEqual(fields["controls"]["ruleset"]["policy"], "sha256:" + "0" * 64, "the ruleset in force at A")
        position = self.loss(fields)
        self.assertEqual(self.state().head, position)

    def test_the_mark_beyond_the_replica_is_named(self) -> None:
        """Note 2: the mark's own head was qualified, so it is never proved never admitted."""

        self.admit_finding("one")
        mark = self.home.high_water("demo").get()
        self.rewind()
        abandoned = self.admission.prepare_loss()["abandoned"]
        named = [a for a in abandoned if (a["position"], a["digest"]) == (mark.position, mark.entry_digest)]
        self.assertEqual(len(named), 1)
        self.assertNotEqual(named[0]["status"], "PROVED_NEVER_ADMITTED")

    def test_a_forged_checkpoint_names_nothing(self) -> None:
        from ssds.ledger.append import HostKey
        from ssds.ledger.qualification import Checkpoint, checkpoint_body, checkpoint_message

        self.admit_finding("one")
        self.rewind()
        fields = self.admission.prepare_loss()
        stranger = HostKey.generate()
        body = checkpoint_body("demo", 9, "sha256:" + "8" * 64, "0" * 40, stranger.key_id)
        write_checkpoint(FileWitness(self.home.witness_root),
                         Checkpoint(**body, signature=stranger.sign(checkpoint_message(body)).hex()))
        self.assertEqual(self.admission.prepare_loss()["abandoned"], fields["abandoned"])

    # -- refusals ----------------------------------------------------------------------------------------------

    def test_every_field_is_its_recomputation(self) -> None:
        self.admit_finding("one")
        self.rewind()
        fields = self.admission.prepare_loss()
        before = len(self.entries())
        wrong = {
            "retained": {"position": 0, "digest": fields["retained"]["digest"]},
            "abandoned": [],
            "report": "sha256:" + "9" * 64,
            "controls": {**fields["controls"], "ruleset": {"system": "other"}},
        }
        for name, value in wrong.items():
            with self.subTest(field=name), self.assertRaisesRegex(EntryInvalid, f"{name} is not the recomputed"):
                self.loss({**fields, name: value})
        with self.assertRaisesRegex(EntryInvalid, "recomputed abandoned"):
            self.loss({**fields, "abandoned": [{**fields["abandoned"][0], "status": "POSSIBLY_ADMITTED"}]})
        with self.assertRaisesRegex(EntryInvalid, "exactly"):
            self.loss({**fields, "note": "x"})
        self.assertEqual(len(self.entries()), before)

    def test_a_witness_that_changes_after_prepare_refuses_the_record(self) -> None:
        self.admit_finding("one")
        self.rewind()
        fields = self.admission.prepare_loss()
        extra = next((self.home.witness_root / "demo").glob("*.json"))
        (self.home.witness_root / "demo" / ("999999999999-" + "f" * 64 + ".json")).write_bytes(b"not a checkpoint")
        unchanged = self.admission.prepare_loss()
        self.assertEqual(unchanged["report"], fields["report"], "an unreadable file holds nothing")
        extra.unlink()
        with self.assertRaisesRegex(EntryInvalid, "recomputed report"):
            self.loss(fields)

    def test_a_qualified_ledger_takes_no_loss(self) -> None:
        with self.assertRaisesRegex(AdmissionHalted, "reading F50"):
            self.loss({"retained": {}, "abandoned": [], "report": "sha256:" + "0" * 64, "controls": {}})

    def test_the_compare_and_swap_refuses_a_ref_past_the_readable_prefix(self) -> None:
        """Note 1 / N2: an unreadable suffix keeps the ref beyond A; moving it is F47's restore."""

        self.admit_finding("one")
        real = Admission.chain
        before = len(self.entries())

        def readable_prefix(admission):
            chain = real(admission)
            return dataclasses.replace(chain, entries=chain.entries[:-1])

        with mock.patch.object(Admission, "chain", readable_prefix):
            self.assertEqual(self.state().state, "ROLLBACK")
            with self.assertRaises(AppendRefused):
                self.loss()
        self.assertEqual(len(self.entries()), before)


class TeamLedger(RequestFixture):
    """A TEAM (3, 2, 2, 0) ledger with fixture witnesses (F53); no tests of its own, so later steps subclass it."""

    def setUp(self) -> None:
        super().setUp()
        self.key = host_key(self.home, "team")
        self.repository = self.home.ledger_repository("team")
        create_ledger_repository(self.repository)
        import_commits(self.repository, self.product, [self.baseline])
        self.roots = {f"w{i}": self.root / f"team-w{i}" for i in range(3)}
        for folder in self.roots.values():
            folder.mkdir()
        genesis = genesis_record(self.key, self.public, self.root, self.baseline, ledger_id="team")
        genesis["fields"]["witnesses"] = {"class": "TEAM", "N": 3, "q_a": 2, "r": 2, "f": 0,
                                          "witnesses": [{"id": w, "kind": "GIT", "location": f"git:{w}"} for w in self.roots]}
        genesis["fields"]["deployment_class"] = "TEAM"
        self.genesis = append_entry(self.repository, entry("team", 0, None, self.key,
                                                           lifecycle=approve(with_id(genesis), self.private)),
                                    self.key, None, referenced=[self.baseline])
        self.checkpoint(self.genesis, *self.roots)

    def checkpoint(self, appended, *witnesses: str) -> None:
        for w in witnesses:
            write_checkpoint(FileWitness(self.roots[w]), appended.checkpoint)

    def append(self, prev, position: int, note: str):
        adoption = record("RULESET_ADOPTION", target=None, actor=self.human(),
                          fields={"system": "ssds-rules/1", "policy": "sha256:" + note * 64,
                                  "analyzers": ["ssds.analyzer.python/1"]})
        return append_entry(self.repository, entry("team", position, prev.digest, self.key, lifecycle=adoption,
                                                   obs=self.baseline), self.key, prev.commit)

    def team(self, witnesses=None) -> Admission:
        return Admission(self.home, "team", self.trees, fixture_witnesses=witnesses or self.roots)

    def loss(self, admission: Admission) -> int:
        rec = record("LEDGER_LOSS", target=None, actor=self.human(), fields=admission.prepare_loss())
        return admission.admit_lifecycle(rec, sshsig(self.private, admission.lifecycle_message(rec)), None)

    def rewind_to_genesis(self) -> None:
        git(self.repository, "update-ref", ledger_ref("team"), self.genesis.commit)



class TeamLoss(TeamLedger):
    """Losses on the TEAM ledger."""

    def test_a_mixed_set_is_one_loss_naming_both(self) -> None:
        one = self.append(self.genesis, 1, "1")
        self.checkpoint(one, "w0", "w1")  # held by q_a: known admitted
        two = self.append(one, 2, "2")
        self.checkpoint(two, "w0")  # one of three, all responding: proved never admitted
        self.rewind_to_genesis()
        admission = self.team()
        self.assertEqual(admission.qualification(admission.chain()).state, "ROLLBACK")
        statuses = {a["position"]: a["status"] for a in admission.prepare_loss()["abandoned"]}
        self.assertEqual(statuses, {1: "KNOWN_ADMITTED", 2: "PROVED_NEVER_ADMITTED"})
        position = self.loss(admission)
        held = admission.qualification(admission.chain())
        self.assertEqual((held.state, held.head), ("QUALIFIED", position))

    def test_only_proved_never_admitted_heads_are_a_fork_resolution(self) -> None:
        one = self.append(self.genesis, 1, "1")
        self.checkpoint(one, "w0")
        self.rewind_to_genesis()
        admission = self.team()
        self.assertEqual([a["status"] for a in admission.prepare_loss()["abandoned"]], ["PROVED_NEVER_ADMITTED"])
        with self.assertRaisesRegex(EntryInvalid, "FORK_RESOLUTION"):
            self.loss(admission)

    def test_a_loss_under_unqualified_cannot_be_held_without_a_redesignation(self) -> None:
        """§23.8's witness-loss row: the gate admits the loss, but the unchanged witness set cannot hold it (F46,
        F51); a redesignation carrying the loss is 7e's."""

        one = self.append(self.genesis, 1, "1")
        self.checkpoint(one, "w0", "w1", "w2")
        self.rewind_to_genesis()
        admission = self.team({"w0": self.roots["w0"]})  # two of three witnesses lost
        self.assertEqual(admission.qualification(admission.chain()).state, "UNQUALIFIED")
        self.assertEqual([a["status"] for a in admission.prepare_loss()["abandoned"]], ["POSSIBLY_ADMITTED"])
        with self.assertRaisesRegex(AdmissionHalted, "reading F51"):
            self.loss(admission)
        self.assertEqual(len(admission.chain().entries), 1)

    def test_a_mark_no_witness_reports_is_named(self) -> None:
        from ssds.ledger.qualification import HighWaterMark

        self.home.high_water("team").set(HighWaterMark(1, "sha256:" + "7" * 64))
        admission = self.team({"w0": self.roots["w0"], "w1": self.roots["w1"]})  # w2 does not respond
        abandoned = admission.prepare_loss()["abandoned"]
        self.assertEqual([(a["position"], a["digest"]) for a in abandoned], [(1, "sha256:" + "7" * 64)])
        # no witness reports it (h = 0, m = 1, f = 0 < q_a), yet the qualified mark floors it (review 8bfaaf0 N2)
        self.assertEqual(abandoned[0]["status"], "POSSIBLY_ADMITTED")

    def test_nothing_abandoned_is_refused(self) -> None:
        admission = self.team({"w0": self.roots["w0"]})
        self.assertEqual(admission.qualification(admission.chain()).state, "UNQUALIFIED")
        self.assertEqual(admission.prepare_loss()["abandoned"], [])
        with self.assertRaisesRegex(EntryInvalid, "redesignation"):
            self.loss(admission)


if __name__ == "__main__":
    unittest.main()
