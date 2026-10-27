"""Phase F step 8g-ii: a re-issue's resubmission (catalogue §8.3 steps 3 and 7, §10.2, §12.2; plan §3.5, reading
F74; plan checks of 53216046, 25bd1d0d and 70cef9cf).

A never-lost record refused under a retired key's unlisted envelope is retained, and ``REISSUE(envelope)`` lists it.
The Dispatcher re-issues the original task by a key in force, its envelope copying the original's task, obligation,
role, contract revision and ``governs``, and resubmits the retained record unchanged but for its binding and a
provenance citing the refusal. Admission authenticates it against the retained record, for exactly the identities the
``REISSUE`` obligation at the base lists: the existence half of step 3 is met by that obligation, and the role is
judged against the original obligation as at its issue. Admitted, it discharges ``REISSUE`` and stays bound to what it
answers.
"""

from __future__ import annotations

import unittest
from unittest import mock

from ssds.admission.request import binding_digest, resubmitted
from ssds.derivation import Workflow, derive
from ssds.dispatcher import reissue, reissues, resubmission

from .test_admission_requests import finding
from .test_phase_f_step8a import Fixture


class Retained(Fixture):
    def setUp(self) -> None:
        super().setUp()
        self.original = self.issue("MANUAL")
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[])
        self.orphan = self.bind(finding(materiality="MATERIAL"), self.original)
        decision = self.admit(self.signed(self.original, [self.orphan]))
        self.assertEqual(decision.refused, ((self.orphan["id"], ("AUTH_ENVELOPE",)),))
        self.in_force = self.issuer_at("other")
        self.lifecycle("REGISTER", self.in_force.trust_root())

    def workflow(self) -> Workflow:
        return Workflow(derive(self.chain(), self.trees))

    def open_reissues(self):
        return [o for o in self.workflow().obligations if o.kind == "REISSUE"]

    def pending(self):
        ((original, kept),) = reissues(self.chain(), self.trees, self.held())
        return original, kept

    def resubmit(self, original=None, kept=None, issuer=None):
        o, k = self.pending()
        issued = reissue(issuer or self.in_force, original or o, self.held())
        return issued, resubmission(issued, kept or k, len(self.entries()) - 1, self.baseline)


class Resubmission(Retained):
    def test_the_dispatcher_reads_what_reissue_lists(self) -> None:
        original, kept = self.pending()
        self.assertEqual(original, self.original.envelope)
        self.assertEqual(kept, {self.orphan["id"]: {k: v for k, v in self.orphan.items() if k != "id"}})

    def test_a_resubmission_is_admitted_and_discharges_reissue(self) -> None:
        issued, req = self.resubmit()
        envelope = issued.envelope
        self.assertEqual({k: envelope[k] for k in ("task_id", "obligation_id", "role", "contract_revision", "governs")},
                         {k: self.original.envelope[k]
                          for k in ("task_id", "obligation_id", "role", "contract_revision", "governs")})
        self.assertEqual((envelope["issue_key_id"], envelope["route"]), (self.in_force.key_id, "MANUAL"))
        (rec,) = req["records"]
        self.assertEqual((rec["actor"], rec["binding"]["lineage_class"], rec["provenance"]["reissue_of"]),
                         (self.orphan["actor"], self.orphan["binding"]["lineage_class"], self.orphan["id"]))
        decision = self.admit(req)
        self.assertEqual((decision.decision, decision.admitted, decision.refused), ("ACCEPT", (rec["id"],), ()))
        self.assertEqual(self.open_reissues(), [], "REISSUE is discharged")
        bound = self.workflow().s.record(rec["id"])["binding"]
        self.assertEqual(bound["obligation"], self.original.envelope["obligation_id"], "bound to what it answers")

    def test_nothing_is_reissued_from_a_head_that_is_not_named(self) -> None:
        from ssds.dispatcher import NotIssuable
        from ssds.ledger.qualification import Qualification

        held = self.held()
        for other in (Qualification("UNQUALIFIED"), Qualification("QUALIFIED", held.head, held.head_digest, held.head)):
            with self.subTest(state=other.state, provisional=other.provisional):
                with self.assertRaises(NotIssuable):
                    reissue(self.in_force, self.original.envelope, other)
                with self.assertRaises(NotIssuable):
                    reissues(self.chain(), self.trees, other)

    def test_another_record_under_the_original_envelope_is_retained_too(self) -> None:
        """Mutant R10: the original, unlisted envelope is no re-issue; a never-lost record under it is retained."""

        other = self.bind(finding(materiality="CRITICAL"), self.original)
        decision = self.admit(self.signed(self.original, [other]))
        self.assertEqual(decision.refused, ((other["id"], ("AUTH_ENVELOPE",)),))
        (open_,) = self.open_reissues()
        self.assertEqual(set(open_.params["records"]), {self.orphan["id"], other["id"]})

    def test_a_second_resubmission_is_not_listed(self) -> None:
        _, req = self.resubmit()
        self.admit(req)
        issued = reissue(self.in_force, self.original.envelope, self.held())
        again = resubmission(issued, {self.orphan["id"]: {k: v for k, v in self.orphan.items() if k != "id"}},
                             len(self.entries()) - 1, self.baseline)
        decision = self.admit(again)
        self.assertEqual(decision.admitted, ())
        self.assertIn("AUTH_ENVELOPE", dict(decision.refused)[again["records"][0]["id"]],
                      "no longer listed, and a re-issue carries only listed resubmissions (review of 26907956, B1)")

    def test_it_counts_as_the_original_would_have(self) -> None:
        """Plan check of 70cef9cf: the resubmitted report derives what the original would have, had it been admitted
        at the same head (Admission's trial extension with the original record admitted)."""

        def derived(workflow):
            return sorted((o.kind, o.holder) for o in workflow.obligations if o.kind != "REISSUE")

        chain = self.chain()
        head = chain.entries[chain.readable_through]
        entry = self.admission.admission_entry(head, self.baseline, "sha256:" + "0" * 64, "ACCEPT", [], [self.orphan],
                                               [], self.baseline)
        direct = derived(Workflow(self.admission.trial(chain, entry)))
        _, req = self.resubmit()
        self.assertEqual(self.admit(req).decision, "ACCEPT")
        self.assertEqual(derived(self.workflow()), direct)
        self.assertNotEqual(direct, derived(Workflow(derive(chain, self.trees))), "the report derives something")


class OriginalGone(Retained):
    def test_admitted_when_the_original_obligation_is_no_longer_derived(self) -> None:
        """Plan check of 53216046, B1: the existence half is met by REISSUE at the base; the role is judged against
        the original obligation as at its issue. Without that, authentication or step 3 would refuse it and the
        record would stay retained."""

        gone = self.original.envelope["obligation_id"]
        real = Workflow.obligations

        def without(workflow):
            found = real.__get__(workflow)
            return found if workflow.s.n <= self.original.envelope["issued_at_position"] \
                else tuple(o for o in found if o.id != gone)

        _, req = self.resubmit()
        with mock.patch.object(Workflow, "obligations", property(without)):
            self.assertNotIn(gone, {o.id for o in Workflow(derive(self.chain(), self.trees)).obligations})
            decision = self.admit(req)
        # step 7 refuses the request, its obligation gone; the never-lost record is admitted whatever the state of
        # its task (§8.3 step 7), so the adverse report is not lost (F41)
        self.assertEqual((decision.decision, decision.reasons, decision.admitted),
                         ("REJECT", ("OBLIGATION_NOT_DERIVED",), (req["records"][0]["id"],)))
        with mock.patch.object(Workflow, "obligations", property(without)):
            self.assertEqual(self.open_reissues(), [], "REISSUE is discharged")

    def test_another_record_under_the_reissue_is_refused(self) -> None:
        gone = self.original.envelope["obligation_id"]
        real = Workflow.obligations

        def without(workflow):
            found = real.__get__(workflow)
            return found if workflow.s.n <= self.original.envelope["issued_at_position"] \
                else tuple(o for o in found if o.id != gone)

        issued, req = self.resubmit()
        extra = self.bind(finding(note="new"), issued)
        req = {**req, "records": [*req["records"], extra]}
        req["binding"] = issued.binding(req)
        with mock.patch.object(Workflow, "obligations", property(without)):
            decision = self.admit(req)
        self.assertEqual(dict(decision.refused).get(extra["id"]), ("AUTH_ENVELOPE",))
        self.assertEqual(decision.admitted, (req["records"][0]["id"],), "the resubmission alone")


class Attested(Fixture):
    """Review of 26907956, note on (a): a record retained with ``HUMAN_ATTESTED_FRESH`` is resubmitted only with its
    co-signer's new attestation, so the ledger holds the evidence for its class again."""

    def test_an_attested_record_is_reattested(self) -> None:
        from ssds.admission.request import request_message
        from ssds.ledger.read import with_id

        from ._fixtures import record, sshsig

        def attest(target):
            return with_id({**record("LINEAGE_ATTESTATION", target={"record": target["id"]},
                                     outcome="HUMAN_ATTESTED_FRESH"), "actor": self.human()})

        def cosign(issued, req):
            req["binding"] = {**issued.binding(req), "human": {
                "actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
            return req

        original = self.issue("MANUAL")
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[])
        rec = self.bind(finding(materiality="MATERIAL"), original)
        rec = with_id({**rec, "binding": {**rec["binding"], "lineage_class": "HUMAN_ATTESTED_FRESH"}})
        req = self.request([rec, attest(rec)], base_position=len(self.entries()) - 1)
        refused = self.admit(cosign(original, req))
        self.assertIn((rec["id"], ("AUTH_ENVELOPE",)), refused.refused, "retained with its class")
        in_force = self.issuer_at("other")
        self.lifecycle("REGISTER", in_force.trust_root())
        ((envelope, kept),) = reissues(self.chain(), self.trees, self.held())
        issued = reissue(in_force, envelope, self.held())
        plain = resubmission(issued, kept, len(self.entries()) - 1, self.baseline)
        self.assertEqual(dict(self.admit(plain).refused).get(plain["records"][0]["id"]), ("AUTH_ENVELOPE",),
                         "no evidence for its class")
        again = resubmission(issued, kept, len(self.entries()) - 1, self.baseline)
        (resubmitted_rec,) = again["records"]
        again = cosign(issued, {**again, "records": [resubmitted_rec, attest(resubmitted_rec)]})
        decision = self.admit(again)
        self.assertIn(resubmitted_rec["id"], decision.admitted)
        self.assertFalse([o for o in Workflow(derive(self.chain(), self.trees)).obligations if o.kind == "REISSUE"])


class Refused(Retained):
    def assertRefused(self, req, code="AUTH_ENVELOPE") -> None:
        decision = self.admit(req)
        self.assertEqual(decision.admitted, ())
        self.assertIn(code, dict(decision.refused)[req["records"][0]["id"]])
        self.assertEqual(len(self.open_reissues()), 1, "still listed")

    def changed(self, **fields):
        original, kept = self.pending()
        body = {**kept[self.orphan["id"]], **fields}
        return self.resubmit(kept={self.orphan["id"]: body})[1]

    def test_changed_content(self) -> None:
        self.assertRefused(self.changed(fields={"materiality": "ROUTINE"}))

    def test_another_actor(self) -> None:
        self.assertRefused(self.changed(actor="agent:someone/1"))

    def test_another_lineage(self) -> None:
        original, kept = self.pending()
        body = kept[self.orphan["id"]]
        for change in ({"lineage_class": "ATTESTED_FRESH"}, {"lineage": ["session:x"]}):
            with self.subTest(change=change):
                self.assertRefused(self.resubmit(kept={self.orphan["id"]: {
                    **body, "binding": {**body["binding"], **change}}})[1])

    def test_an_envelope_not_copying_the_original(self) -> None:
        for change in ({"obligation_id": "sha256:" + "5" * 64}, {"role": "IMPLEMENTER"},
                       {"governs": {"mode": "NATIVE", "protocol": "7.2.1"}}):
            with self.subTest(change=change):
                self.assertRefused(self.resubmit(original={**self.original.envelope, **change})[1])

    def test_a_retired_key_cannot_reissue(self) -> None:
        self.lifecycle("RETIRE", self.in_force.trust_root(), outstanding=[])
        _, req = self.resubmit()
        decision = self.admit(req)
        self.assertEqual(decision.admitted, ())
        self.assertEqual(len(self.open_reissues()), 1)

    def test_a_retired_key_listing_the_reissue_cannot_resubmit(self) -> None:
        """The re-issue is by a key in force: a retired key's listed envelope covers never-lost records on its own
        task's path, never a resubmission (survivor A05)."""

        issued, req = self.resubmit()
        self.lifecycle("RETIRE", self.in_force.trust_root(), outstanding=[binding_digest(issued.binding())])
        req = {**req, "base_position": len(self.entries()) - 1}
        req["binding"] = issued.binding(req)
        self.assertRefused(req)

    def test_a_record_naming_the_original_envelope(self) -> None:
        """Survivor A06: the resubmitted record names the re-issued envelope, not the retired one it was refused
        under."""

        issued, _ = self.resubmit()
        stale = resubmitted({k: v for k, v in self.orphan.items() if k != "id"}, self.orphan["id"],
                            self.orphan["binding"]["envelope"])
        req = resubmission(issued, {}, len(self.entries()) - 1, self.baseline)
        req = {**req, "records": [stale]}
        req["binding"] = issued.binding(req)
        self.assertRefused(req)

    def test_a_reissue_carries_only_resubmissions(self) -> None:
        """Review of 26907956, B1: the original actor is accepted only for the listed identities, while the original
        obligation stands and after REISSUE is discharged."""

        issued, req = self.resubmit()
        fresh = self.bind(finding(note="fresh"), issued)
        self.assertEqual(fresh["actor"], self.orphan["actor"], "the original task's actor namespace")
        mixed = {**req, "records": [*req["records"], fresh]}
        mixed["binding"] = issued.binding(mixed)
        decision = self.admit(mixed)
        self.assertEqual(dict(decision.refused).get(fresh["id"]), ("AUTH_ENVELOPE",))
        self.assertEqual(decision.admitted, (req["records"][0]["id"],))
        self.assertEqual(self.open_reissues(), [], "discharged")
        alone = resubmission(issued, {}, len(self.entries()) - 1, self.baseline)
        later = self.bind(finding(note="later"), issued)
        alone = {**alone, "records": [later]}
        alone["binding"] = issued.binding(alone)
        self.assertEqual(dict(self.admit(alone).refused).get(later["id"]), ("AUTH_ENVELOPE",))

    def test_provenance_is_the_retained_one_and_a_citation_counts_once(self) -> None:
        """Review of 26907956, B2."""

        from ssds.ledger.read import with_id

        issued, req = self.resubmit()
        (rec,) = req["records"]
        forged = with_id({**rec, "provenance": {**rec["provenance"], "model_family": "forged"}})
        twin = with_id({**rec, "provenance": {**rec["provenance"], "note": "twin"}})
        for records in ([forged], [rec, twin]):
            with self.subTest(records=len(records)):
                bad = {**req, "records": records}
                bad["binding"] = issued.binding(bad)
                decision = self.admit(bad)
                self.assertEqual(dict(decision.refused).get(records[-1]["id"]), ("AUTH_ENVELOPE",))
                self.assertEqual(decision.admitted, tuple(r["id"] for r in records[:-1]))

    def test_an_unlisted_citation_is_refused(self) -> None:
        issued, _ = self.resubmit()
        stray = resubmitted({k: v for k, v in self.orphan.items() if k != "id"}, "sha256:" + "ab" * 32,
                            binding_digest(issued.binding()))
        req = resubmission(issued, {}, len(self.entries()) - 1, self.baseline)
        req = {**req, "records": [stray]}
        req["binding"] = issued.binding(req)
        self.assertRefused(req, "AUTH_ENVELOPE")  # under a re-issue (B1); elsewhere SCHEMA_UNSUPPORTED (step 4b-ii)


if __name__ == "__main__":
    unittest.main()
