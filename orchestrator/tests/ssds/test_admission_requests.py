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



def task_result(x: str, scope=("guide",), key: str | None = "sha256:" + "a" * 64, task="t-1") -> dict:
    from ssds.ledger.read import with_id

    rec = record("TASK_RESULT", target={"task": task, "transformation": x}, outcome="COMPLETE", actor="agent:t/1",
                 actor_class="AGENT", fields={"slots": {}})
    binding = {"task": task, "obligation": "obl", "role": "IMPLEMENTER", "lineage": ["agent:t/1"],
               "lineage_class": "ATTESTED_FRESH", "write_scope": list(scope)}
    if key is not None:
        binding["item_key"] = key
    return with_id({**rec, "binding": binding})


def ledger_object(value) -> tuple[str, str]:
    import hashlib

    from ssds.core.api.v1 import canonical_json

    text = canonical_json(value).decode("utf-8")
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest(), text


class StepTwoReview(RequestFixture):
    """The same-family review of 0933e5db: each blocker as a discriminating case."""

    def test_b1_a_record_with_a_malformed_id_never_halts_the_ledger(self) -> None:
        bad = {**finding(), "id": "x"}
        decision = self.admit(self.request([bad, {"no": "id"}]))
        self.assertEqual(decision.decision, "REJECT")
        self.assertTrue(all(r.startswith("sha256:") and len(r) == 71 for r, _ in decision.refused))
        self.assertEqual(len({r for r, _ in decision.refused}), 2, "each refused element by its own content identity")
        self.assertEqual(len(self.entries()), 2, "the chain still verifies")
        self.assertTrue(self.admit(self.request([finding()])).appended, "and the next request appends")

    def test_b2_salvage_admits_only_records_that_passed_their_own_checks(self) -> None:
        self.admission.authenticated = lambda request: True
        good, broken, secret = finding(), {**finding(materiality="MATERIAL"), "id": "sha256:" + "f" * 64}, finding(note="ghp_" + "a1B2" * 9)
        dangling = record("FINDING", target={"records": [secret["id"]]}, fields={"materiality": "ROUTINE"})
        digest, text = ledger_object({"token": "Zq8vR2xK9mW4pT7nL3sY6cB1Hk5Jd0Fg"})
        req = {**self.request([good, broken, secret, dangling], objects={digest: text}), "extra": True}
        decision = self.admit(req)
        self.assertEqual(decision.reasons, ("SCHEMA_REQUEST",))
        self.assertEqual(decision.admitted, (good["id"],))
        refused = dict(decision.refused)
        self.assertEqual(refused[secret["id"]], ("SECRET_DETECTED",))
        self.assertEqual(refused[dangling["id"]], ("REF_RECORD",), "a reference resolves only to an admitted record")
        self.assertIn("SCHEMA_RECORD", refused[next(r for r in refused if r not in (secret["id"], dangling["id"]))])
        self.assertEqual(self.entries()[-1].objects, {}, "no object is written that no admitted record references")

    def test_b2_only_verified_referenced_objects_are_written(self) -> None:
        from ssds.ledger.read import with_id

        self.admission.authenticated = lambda request: True
        digest, text = ledger_object({"parts": []})
        report = with_id({**finding(), "refs": [{"store": "LEDGER", "digest": digest, "media_type": "application/json"}]})
        self.admit(self.request([report], objects={digest: text}))
        self.assertEqual(set(self.entries()[-1].objects), {digest})

    def test_b3_objects_are_what_their_key_says(self) -> None:
        digest, text = ledger_object({"a": 1})
        for objects in ({"../evil": text}, {digest: '{"a": 1}'}, {"sha256:" + "0" * 64: text}, {digest: 7}):
            with self.subTest(objects=list(objects)):
                self.assertEqual(self.admit(self.request([finding()], objects=objects)).reasons, ("SCHEMA_OBJECT",))
        secret_digest, secret_text = ledger_object({"k": "ghp_" + "a1B2" * 9})
        self.assertIn("SECRET_DETECTED", self.admit(self.request([finding()], objects={secret_digest: secret_text})).reasons)

    def test_b3_a_ledger_ref_must_resolve(self) -> None:
        from ssds.ledger.read import with_id

        report = with_id({**finding(), "refs": [{"store": "LEDGER", "digest": "sha256:" + "6" * 64, "media_type": "application/json"}]})
        self.assertEqual(self.admit(self.request([report])).refused, ((report["id"], ("REF_OBJECT",)),))

    def test_b4_never_lost_follows_the_derivation_owner(self) -> None:
        from ssds.admission.request import never_lost

        cases = [("REVIEW", {"triple": None}, "NO_PASS", True), ("REVIEW", {}, "PASS", False),
                 ("PRODUCT_SCOPE_ACCEPTANCE", {}, "REJECTED", True), ("INTAKE_DISPOSITION", {}, "REJECT", True),
                 ("INTAKE_DISPOSITION", {}, "ABSORB", False), ("EVIDENCE_ASSESSMENT", {}, "FAIL", True)]
        for kind, _, outcome, expected in cases:
            with self.subTest(kind=kind, outcome=outcome):
                self.assertEqual(never_lost({"kind": kind, "outcome": outcome, "actor": "human:x"}), expected)

    def test_b5_a_secret_never_hides_under_an_identity_key_name(self) -> None:
        from ssds.ledger.read import with_id

        hidden = with_id({**finding(), "provenance": {"signature": "Zq8vR2xK9mW4pT7nL3sY6cB1Hk5Jd0Fg"}})
        self.assertEqual(self.admit(self.request([hidden])).refused, ((hidden["id"], ("SECRET_DETECTED",)),))

    def test_b6_untrusted_input_is_rejected_and_never_blocks_the_queue(self) -> None:
        for bad in (self.request([finding()], base_position=0.5), self.request([finding()], claims=[{"x": 1}]),
                    self.request([finding()], base_position=True), self.request([finding()], base_commit="not-a-commit")):
            with self.subTest(field=[k for k in bad if bad[k] != self.request([finding()])[k]]):
                self.assertEqual(self.admit(bad).reasons, ("SCHEMA_REQUEST",))
        self.admission.submit(self.request([finding()], base_position=0.25))
        self.admission.submit(self.request([finding(materiality="CRITICAL")]))
        decisions = self.admission.process(self.baseline)
        self.assertEqual(len(decisions), 2)
        self.assertEqual(self.admission.queue, [])

    def test_b7_the_base_commit_must_match_the_base_position(self) -> None:
        self.assertEqual(self.admit(self.request([finding()], base_commit="1" * 40)).reasons, ("REF_BASE",))
        self.assertEqual(self.admit(self.request([finding()], base_position=-1)).reasons, ("REF_BASE",))

    def test_b8_the_s2_binding_cases_and_duplicates(self) -> None:
        x = "sha256:" + "b" * 64
        joins = self.admit(self.request([task_result(x), task_result(x, task="t-2")]))
        self.assertEqual(joins.refused, (), "S2 same_context_joins")
        for name, other in (("different_scope_refused", task_result(x, scope=("code",), task="t-2")),
                            ("different_key_refused", task_result(x, key="sha256:" + "c" * 64, task="t-2"))):
            with self.subTest(case=name):
                self.assertEqual(self.admit(self.request([task_result(x), other])).refused,
                                 ((other["id"], ("REF_PRODUCING_CONTEXT",)),))
        twice = finding(materiality="CRITICAL")
        self.assertEqual(self.admit(self.request([twice, twice])).refused, ((twice["id"], ("REF_DUPLICATE",)),))

    def test_b8_the_remaining_credential_forms_and_request_fields(self) -> None:
        for value in ("github_pat_" + "A1b2" * 11, "sk-" + "A1b2C3d4" * 3, "AIza" + "B" * 35):
            with self.subTest(value=value[:12]):
                self.assertEqual(self.admit(self.request([finding(note=value)])).refused[0][1], ("SECRET_DETECTED",))
        self.assertIn("SECRET_DETECTED", self.admit(self.request([finding()], binding={"note": "ghp_" + "a1B2" * 9})).reasons)

    def test_b8_the_identity_is_the_catalogue_formula(self) -> None:
        import hashlib

        from ssds.core.api.v1 import canonical_json

        req = self.request([finding()])
        self.assertEqual(request_id(req), "sha256:" + hashlib.sha256(b"ssds.request.v1" + canonical_json(req)).hexdigest())

    def test_b8_bounds_trigger_exactly_their_code(self) -> None:
        long = finding(note="x" * 5000)
        self.assertEqual(self.admit(self.request([long])).refused, ((long["id"], ("SCHEMA_BOUND",)),))


class StepTwoRereview(RequestFixture):
    """The same-family re-review of e95e770c: each remaining blocker as a discriminating case."""

    def test_s1_salvage_never_admits_a_record_naming_one_it_dropped(self) -> None:
        self.admission.authenticated = lambda request: True
        x = task_result("sha256:" + "b" * 64)
        naming = record("FINDING", target={"records": [x["id"]]}, fields={"materiality": "ROUTINE"})
        decision = self.admit(self.request([x, naming]))
        self.assertEqual(decision.admitted, ())
        self.assertIn((naming["id"], ("REF_RECORD",)), decision.refused)

    def test_s2_a_malformed_record_never_poisons_the_queue(self) -> None:
        self.admission.submit(self.request([{"kind": ["x"], "outcome": "y"}]))
        self.admission.submit(self.request([finding(materiality="CRITICAL")]))
        self.assertEqual(len(self.admission.process(self.baseline)), 2)
        self.assertEqual(self.admission.queue, [])

    def test_s3_a_request_beyond_its_bounds_gets_no_per_record_work_and_salvages_nothing(self) -> None:
        self.admission.authenticated = lambda request: True
        decision = self.admit(self.request([finding(materiality="MATERIAL", note=str(i)) for i in range(261)]))
        self.assertEqual((decision.reasons, decision.admitted, decision.refused), (("SCHEMA_BOUND",), (), ()))
        deep: object = "x"
        for _ in range(100):
            deep = [deep]
        self.assertEqual(self.admit(self.request([finding()], adopted_deltas=[{"d": deep}])).reasons, ("SCHEMA_BOUND",))
        self.assertEqual(self.admit(self.request([finding()], binding={"a": deep})).reasons, ("SCHEMA_BOUND",))

    def test_s4_a_halted_request_keeps_its_place(self) -> None:
        req = self.request([finding()])
        self.admission.submit(req)
        with self.assertRaises(AdmissionHalted):
            self.admission.process("0" * 40)
        self.assertEqual(self.admission.queue, [req])

    def test_s5_an_unreferenced_clean_object_is_not_written(self) -> None:
        from ssds.ledger.read import with_id

        self.admission.authenticated = lambda request: True
        used, used_text = ledger_object({"parts": []})
        spare, spare_text = ledger_object({"other": True})
        report = with_id({**finding(), "refs": [{"store": "LEDGER", "digest": used, "media_type": "application/json"}]})
        self.admit(self.request([report], objects={used: used_text, spare: spare_text}))
        self.assertEqual(set(self.entries()[-1].objects), {used})

    def test_n6_remaining_discriminators(self) -> None:
        import hashlib

        from ssds.admission.checks import content_identity

        text = '{"a": 1}'
        digest = "sha256:" + hashlib.sha256(text.encode()).hexdigest()
        self.assertEqual(self.admit(self.request([finding()], objects={digest: text})).reasons, ("SCHEMA_OBJECT",),
                         "a non-canonical text whose digest matches is still refused")
        for field, value in (("candidates", ["not-a-commit"]), ("adopted_deltas", ["x"]), ("binding", "x")):
            with self.subTest(field=field):
                self.assertEqual(self.admit(self.request([finding()], **{field: value})).reasons, ("SCHEMA_REQUEST",))
        self.admission.authenticated = lambda request: True
        kept = finding(materiality="CRITICAL")
        self.admit(self.request([kept]))
        again = self.admit(self.request([kept], claims=[]) | {"base_position": 1, "base_commit": self.baseline})
        self.assertIn((kept["id"], ("REF_DUPLICATE",)), again.refused, "a record already in the ledger is a duplicate")
        self.assertNotEqual(content_identity(["a"]), content_identity(["b"]))

if __name__ == "__main__":
    unittest.main()
