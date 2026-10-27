"""Phase F step 8d: judge selection and a human's attestation of a fresh session (catalogue §5.10 (a), (f), §12.2,
§16.5; plan §3.5, reading F72).

The Dispatcher chooses among derivation's eligible judges: a freshly launched agent reviewer on the harness route,
whose launch names no input session, else an eligible human on the manual route. The judge's facts are an unverified
audit stamp in provenance. A judgment brief over content of unknown authorship says how an answer can be
independent. On the manual or Git-envelope route, the human who ran the fresh session co-signs the request; the
co-signature authenticates only that human's ``LINEAGE_ATTESTATION`` of a record bound to the task in the same
request, which alone lets that record carry ``HUMAN_ATTESTED_FRESH``.
"""

from __future__ import annotations

import unittest
from types import SimpleNamespace

from ssds.admission.authenticate import authenticate
from ssds.admission.request import request_message
from ssds.derivation import Workflow, derive, trust_roots
from ssds.dispatcher import FRESH_REVIEWER, Judge, judge_provenance, select_judge
from ssds.ledger.read import with_id

from ._fixtures import human_key, record, sshsig
from .test_admission_requests import RequestFixture, finding


class Selection(unittest.TestCase):
    def test_a_fresh_agent_reviewer_is_preferred_then_a_human(self) -> None:
        w = SimpleNamespace(eligible_judges=lambda o: ("human:SHA256:zed", "human:SHA256:amy", FRESH_REVIEWER))
        self.assertEqual(select_judge(w, None), Judge(FRESH_REVIEWER, "HARNESS"))
        w = SimpleNamespace(eligible_judges=lambda o: ("human:SHA256:zed", "human:SHA256:amy"))
        self.assertEqual(select_judge(w, None), Judge("human:SHA256:amy", "MANUAL"))
        self.assertIsNone(select_judge(SimpleNamespace(eligible_judges=lambda o: ()), None))

    def test_the_judges_facts_are_an_audit_stamp(self) -> None:
        issued = SimpleNamespace(envelope={"lineage_class": "ATTESTED_FRESH", "route": "HARNESS"})
        self.assertEqual(judge_provenance(issued, "family-a", "toolchain-1"), {"judge": {
            "lineage_class": "ATTESTED_FRESH", "route": "HARNESS", "model_family": "family-a",
            "toolchain": "toolchain-1"}})


class Attestation(RequestFixture):
    """The co-signature's authentication rules (F72; plan check of 8f1c948 notes 1, 4)."""

    def roots(self):
        return trust_roots(self.entries())

    def head(self) -> int:
        return len(self.entries()) - 1

    def bound(self, issued, lineage_class="HUMAN_ATTESTED_FRESH"):
        rec = self.bind(finding(note=lineage_class), issued)
        return with_id({**rec, "binding": {**rec["binding"], "lineage_class": lineage_class}})

    def attest(self, rec, actor=None):
        return with_id({**record("LINEAGE_ATTESTATION", target={"record": rec["id"]}, outcome="HUMAN_ATTESTED_FRESH"),
                        "actor": actor or self.human()})

    def cosigned(self, issued, records, private=None, actor=None):
        req = self.request(records, base_position=self.head())
        req["binding"] = {**issued.binding(req), "human": {
            "actor": actor or self.human(), "signature": sshsig(private or self.private, request_message(req))}}
        return req

    def authenticated(self, req):
        return authenticate(req, req["records"], self.roots(), self.head())

    def test_an_attested_record_carries_the_class(self) -> None:
        issued = self.issue("MANUAL")
        rec = self.bound(issued)
        auth = self.authenticated(self.cosigned(issued, [rec, self.attest(rec)]))
        self.assertTrue(auth.ok)
        self.assertEqual(auth.refused, ())

    def test_without_its_attestation_the_class_is_refused(self) -> None:
        issued = self.issue("MANUAL")
        rec = self.bound(issued)
        other = self.bound(issued, "UNKNOWN")
        auth = self.authenticated(self.cosigned(issued, [rec, other, self.attest(other)]))
        self.assertIn("AUTH_ENVELOPE", dict(auth.refused)[rec["id"]])
        self.assertIn("AUTH_ENVELOPE", dict(auth.refused)[other["id"]],
                      "an attested record states the class its attestation fixes")

    def test_only_the_cosigners_attestation_is_authenticated(self) -> None:
        issued = self.issue("MANUAL")
        rec = self.bound(issued)
        stray = with_id({**finding(note="the human's own report"), "actor": self.human()})
        auth = self.authenticated(self.cosigned(issued, [rec, self.attest(rec), stray]))
        self.assertIn("AUTH_ACTOR", dict(auth.refused)[stray["id"]])
        by_another = self.attest(rec, actor="human:SHA256:someone-else")
        auth = self.authenticated(self.cosigned(issued, [rec, by_another]))
        self.assertIn("AUTH_ACTOR", dict(auth.refused)[by_another["id"]])
        self.assertIn("AUTH_ENVELOPE", dict(auth.refused)[rec["id"]], "not attested by the co-signer")

    def test_an_attestation_of_a_record_not_bound_here_is_not_authenticated(self) -> None:
        issued = self.issue("MANUAL")
        rec = self.bound(issued, "UNKNOWN")
        elsewhere = self.attest({"id": "sha256:" + "5" * 64})
        auth = self.authenticated(self.cosigned(issued, [rec, elsewhere]))
        self.assertIn("AUTH_ACTOR", dict(auth.refused)[elsewhere["id"]])

    def test_a_harness_route_or_a_bad_signature_authenticates_nothing(self) -> None:
        issued = self.issue("HARNESS")
        rec = self.bound(issued, "ATTESTED_FRESH")
        req = self.cosigned(issued, [rec, self.attest(rec)])
        req["binding"]["credential_signature"] = issued.credential.sign(req)
        self.assertFalse(self.authenticated(req).ok, "a harness lineage is proved by its attestation")
        issued = self.issue("MANUAL")
        rec = self.bound(issued)
        stranger, _ = human_key(self.root, "stranger")
        self.assertFalse(self.authenticated(self.cosigned(issued, [rec, self.attest(rec)], private=stranger)).ok)

    def test_a_cosignature_moved_to_another_envelope_attests_nothing(self) -> None:
        issued, other = self.issue("MANUAL"), self.issue("GIT_ENVELOPE")
        rec = self.bound(issued)
        req = self.cosigned(issued, [rec, self.attest(rec)])
        req["binding"] = {**other.binding(req), "human": req["binding"]["human"]}
        auth = self.authenticated(req)
        refused = dict(auth.refused)
        self.assertIn("AUTH_ENVELOPE", refused[rec["id"]])
        self.assertTrue(any("AUTH_ACTOR" in codes for codes in refused.values()))

    def test_an_attesting_human_is_not_checked_against_the_authors(self) -> None:
        """Plan check of 8f1c948 note 4: authentication reads no authorship; an author's attestation is admitted
        and its correction is a challenge (F13). The fixture's human is the ledger's only registered human."""

        issued = self.issue("MANUAL")
        rec = self.bound(issued)
        self.assertTrue(self.authenticated(self.cosigned(issued, [rec, self.attest(rec)])).ok)


class Admitting(RequestFixture):
    def test_a_cosigned_request_admits_the_record_and_its_attestation(self) -> None:
        """Found building the review of 4f5caedb's N1: authorization judged the co-signer's attestation under the
        envelope's role (AUTH_ROLE_KIND), so the record carried its class with no evidence in the ledger."""

        issued = self.issue("MANUAL")
        rec = self.bind(finding(note="HUMAN_ATTESTED_FRESH"), issued)
        rec = with_id({**rec, "binding": {**rec["binding"], "lineage_class": "HUMAN_ATTESTED_FRESH"}})
        attestation = with_id({**record("LINEAGE_ATTESTATION", target={"record": rec["id"]},
                                        outcome="HUMAN_ATTESTED_FRESH"), "actor": self.human()})
        req = self.request([rec, attestation], base_position=len(self.entries()) - 1)
        req["binding"] = {**issued.binding(req), "human": {
            "actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        decision = self.admit(req)
        self.assertEqual((decision.decision, set(decision.admitted)), ("ACCEPT", {rec["id"], attestation["id"]}))

    def test_an_attestation_classifies_only_a_co_submitted_record(self) -> None:
        rec = with_id({**record("LINEAGE_ATTESTATION", target={"record": "sha256:" + "4" * 64},
                                outcome="HUMAN_ATTESTED_FRESH"), "actor": self.human()})
        req = self.request([rec], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        decision = self.admit(req)
        self.assertIn("REF_TARGET", dict(decision.refused).get(rec["id"], ()) + tuple(decision.reasons))
        own = with_id({**finding(note="the human's own"), "actor": self.human()})
        of_own = with_id({**record("LINEAGE_ATTESTATION", target={"record": own["id"]}, outcome="HUMAN_ATTESTED_FRESH"),
                          "actor": self.human()})
        req = self.request([own, of_own], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        decision = self.admit(req)
        self.assertIn("REF_TARGET", dict(decision.refused).get(of_own["id"], ()) + tuple(decision.reasons),
                      "a human's own record is no task-bound target (review 50954f9 N1)")


class Notice(RequestFixture):
    def test_a_judgment_brief_over_unknown_authorship_says_how_to_be_independent(self) -> None:
        from ssds.interface.render import Renderer

        w = Workflow(derive(self.chain(), self.trees))
        accept = next(o for o in w.obligations if o.kind == "ACCEPT")
        head = {"label": "QUALIFIED", "position": w.s.n, "digest": "sha256:" + "0" * 64}
        text = Renderer(w, head, lambda source, path: None).brief(accept).text
        if "UNKNOWN" in w.judged_authors(accept):
            self.assertIn("NON_AUTHORSHIP_ATTESTATION", text)
        else:
            self.assertNotIn("authorship is unknown", text)

    def chain(self):
        from ssds.ledger.read import read_chain

        return read_chain(self.home.ledger_repository("demo"), "demo")


if __name__ == "__main__":
    unittest.main()
