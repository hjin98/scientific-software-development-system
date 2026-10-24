"""Phase F step 2: admission requests, validation steps 1-2 and the minimal commit path (Manual §8.1-§8.4, §24.1,
§25.4; catalogue §7.1, §8.1-§8.4).

Each case builds a real shadow ledger on fixture repositories (the genesis of ``test_admission_genesis``), hands
requests to the real Admission engine and reads the appended entries back through the verified chain. Steps 3-8
are not realized yet, so a request that passes steps 1-2 is rejected as unsupported, and nothing is salvaged
without an authenticated binding (step 3).
"""

from __future__ import annotations

import unittest

from ssds.admission.engine import Admission, AdmissionHalted
from ssds.admission.genesis import admit_genesis, prepare_genesis
from ssds.admission.request import request_id
from ssds.ledger.qualification import FileWitness
from ssds.ledger.read import read_chain

from ._fixtures import record, sshsig
from .test_admission_genesis import GenesisFixture, product_state


def finding(units=("guide",), materiality="ROUTINE", note: str | None = None) -> dict:
    """A report; ``note`` goes into its free-form provenance, where the closed schema admits arbitrary text."""

    from ssds.ledger.read import with_id

    rec = record("FINDING", target={"units": list(units)}, fields={"materiality": materiality})
    if note is not None:
        rec = with_id({**rec, "provenance": {"note": note}})
    return rec


class RequestFixture(GenesisFixture):
    def setUp(self) -> None:
        super().setUp()
        prepared = prepare_genesis(self.spec(), self.home, self.trees)
        admit_genesis(self.home, "demo", sshsig(self.private, prepared.message))
        self.admission = Admission(self.home, "demo", self.trees)

    def request(self, records, **overrides) -> dict:
        value = {"binding": None, "claims": [], "base_position": 0, "base_commit": self.baseline, "candidates": [],
                 "adopted_deltas": [], "records": list(records), "objects": {}}
        value.update(overrides)
        return value

    def admit(self, request):
        return self.admission.admit(request, self.baseline)

    def entries(self):
        chain = read_chain(self.home.ledger_repository("demo"), "demo")
        return chain.entries[: chain.readable_through + 1]


class Identity(RequestFixture):
    def test_an_identical_request_returns_the_recorded_decision_and_appends_nothing(self) -> None:
        req = self.request([finding()])
        first = self.admit(req)
        self.assertTrue(first.appended)
        self.assertEqual(first.request_id, request_id(req))
        again = self.admit(dict(req))
        self.assertFalse(again.appended)
        self.assertEqual((again.decision, again.reasons, again.position), (first.decision, first.reasons, first.position))
        self.assertEqual(len(self.entries()), 2, "genesis and one admission entry")

    def test_the_identity_ignores_a_request_id_field_and_any_change_makes_another_request(self) -> None:
        req = self.request([finding()])
        self.assertEqual(request_id(req), request_id({**req, "request_id": "anything"}))
        self.assertNotEqual(request_id(req), request_id(self.request([finding(materiality="MATERIAL")])))

    def test_every_decision_is_appended_signed_checkpointed_and_verifies(self) -> None:
        before = product_state(self.product)
        decision = self.admit(self.request([finding()]))
        entry = self.entries()[-1].entry
        self.assertEqual(entry["entry_kind"], "ADMISSION")
        self.assertEqual(entry["admission"]["request_id"], decision.request_id)
        self.assertEqual(entry["obs"], self.baseline)
        self.assertEqual(FileWitness(self.home.witness_root).read("demo")[-1].position, decision.position)
        self.assertEqual(product_state(self.product), before, "the product repository is only read")

    def test_an_observed_head_other_than_the_expected_head_appends_nothing(self) -> None:
        with self.assertRaises(AdmissionHalted):
            self.admission.admit(self.request([finding()]), "0" * 40)
        self.assertEqual(len(self.entries()), 1)


class SchemaAndSecrets(RequestFixture):
    def assertRefused(self, records, code) -> None:
        decision = self.admit(self.request(records))
        self.assertEqual(decision.decision, "REJECT")
        self.assertIn(code, {c for _, why in decision.refused for c in why} | set(decision.reasons))

    def test_a_malformed_request_is_rejected(self) -> None:
        for bad in ({"records": []}, {**self.request([]), "extra": 1}, {**self.request([]), "records": "x"}):
            with self.subTest(request=bad):
                decision = self.admit(bad)
                self.assertEqual((decision.decision, decision.reasons), ("REJECT", ("SCHEMA_REQUEST",)))

    def test_a_record_outside_the_closed_schema_is_refused(self) -> None:
        broken = dict(finding())
        broken["id"] = "sha256:" + "f" * 64
        self.assertRefused([broken], "SCHEMA_RECORD")

    def test_each_credential_form_is_detected(self) -> None:
        for value in ("-----BEGIN OPENSSH PRIVATE KEY-----", "ghp_" + "a1B2" * 9, "AKIA" + "ABCDEFGHIJKLMNOP",
                      "postgres://user:hunter2@db.example.org/x", "xoxb-" + "1234567890-abcdef"):
            with self.subTest(value=value[:12]):
                self.assertRefused([finding(note=value)], "SECRET_DETECTED")

    def test_high_entropy_is_detected_but_not_in_digests_or_identities(self) -> None:
        self.assertRefused([finding(note="Zq8vR2xK9mW4pT7nL3sY6cB1")], "SECRET_DETECTED")
        decision = self.admit(self.request([finding(note="sha256:" + "a1" * 32)]))
        self.assertNotIn("SECRET_DETECTED", {c for _, why in decision.refused for c in why})

    def test_bounds_are_enforced(self) -> None:
        self.assertRefused([finding(note="x" * 5000)], "SCHEMA_BOUND")
        decision = self.admit(self.request([finding(note=str(i)) for i in range(257)]))
        self.assertIn("SCHEMA_BOUND", decision.reasons)


class References(RequestFixture):
    def test_a_named_record_that_does_not_exist_is_refused(self) -> None:
        missing = record("FINDING", target={"records": ["sha256:" + "9" * 64]}, fields={"materiality": "ROUTINE"})
        decision = self.admit(self.request([missing]))
        self.assertEqual(decision.refused, ((missing["id"], ("REF_RECORD",)),))

    def test_a_record_may_name_one_submitted_earlier_in_the_request(self) -> None:
        first = finding()
        second = record("FINDING", target={"records": [first["id"]]}, fields={"materiality": "ROUTINE"})
        decision = self.admit(self.request([first, second]))
        self.assertEqual(decision.refused, ())
        self.assertEqual(decision.reasons, ("SCHEMA_UNSUPPORTED",), "steps 3-8 are not realized: fail closed")

    def test_an_unknown_revision_and_a_claimed_unknown_obligation_are_refused(self) -> None:
        stale = record("FINDING", target={"units": ["guide"]}, fields={"materiality": "ROUTINE"},
                       basis=[{"mode": "content", "target": {"unit": "guide", "rev": "sha256:" + "3" * 64}, "class": "EXACT"}])
        decision = self.admit(self.request([stale], claims=["no-such-obligation"]))
        self.assertIn("REF_OBLIGATION", decision.reasons)
        self.assertEqual(decision.refused, ((stale["id"], ("REF_REVISION",)),))

    def test_a_base_beyond_the_head_is_rejected(self) -> None:
        self.assertIn("REF_BASE", self.admit(self.request([finding()], base_position=7)).reasons)


class SalvageAndQueue(RequestFixture):
    def test_nothing_is_salvaged_without_an_authenticated_binding(self) -> None:
        decision = self.admit(self.request([finding()]))
        self.assertEqual((decision.decision, decision.admitted), ("REJECT", ()))

    def test_an_authenticated_rejected_request_salvages_its_never_lost_records(self) -> None:
        # stands in for step 3's authentication, which is not built yet; the salvage itself is the real owner's
        self.admission.authenticated = lambda request: True
        report, bad = finding(), finding(note="ghp_" + "a1B2" * 9)
        decision = self.admit(self.request([report, bad]))
        self.assertEqual(decision.decision, "REJECT")
        self.assertEqual(decision.admitted, (report["id"],))
        self.assertEqual(decision.refused, ((bad["id"], ("SECRET_DETECTED",)),))

    def test_a_never_lost_only_request_is_not_delayed_behind_one_that_may_need_revalidation(self) -> None:
        stale = self.request([record("ACCEPTANCE", target={"subject": "guide", "scope_id": "sha256:" + "4" * 64,
                                                           "rev": "sha256:" + "5" * 64}, outcome="PASS")])
        report = self.request([finding()])
        self.admission.submit(stale)
        self.admission.submit(report)
        self.assertEqual(self.admission.order(), [report, stale])


if __name__ == "__main__":
    unittest.main()
