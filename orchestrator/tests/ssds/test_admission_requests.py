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
from ssds.ledger.read import read_chain, transformation_id

from ._fixtures import record, sshsig
from .test_admission_genesis import GenesisFixture, product_state


def finding(units=("guide",), materiality="ROUTINE", note: str | None = None) -> dict:
    """A report; ``note`` goes into its free-form provenance, where the closed schema admits arbitrary text."""

    from ssds.ledger.read import with_id

    rec = record("FINDING", target={"units": list(units)}, fields={"materiality": materiality})
    if note is not None:
        rec = with_id({**rec, "provenance": {"note": note}})
    return rec


def unbound(*codes: str) -> tuple[str, ...]:
    """An unbound request's reasons: its own, and the authentication it lacks (§8.3 step 3)."""

    return tuple(sorted({*codes, "AUTH_ENVELOPE"}))


class RequestFixture(GenesisFixture):
    """A fixture ledger whose subject ``guide`` is ``NATIVE``, so it derives an agent-held obligation (its
    ``ACCEPT``, held by a reviewer) that envelopes can name (§8.3 step 3). A shadow genesis declares only
    ``LEGACY`` or ``UNGOVERNED`` subjects, and the real one still does; the test lifts that check for this
    fixture alone, so Admission's own checks run against agent-held obligations."""

    def setUp(self) -> None:
        from unittest import mock

        super().setUp()
        native = {"guide": {"mode": "NATIVE", "ruleset": "ssds-rules/1"}, "*": {"mode": "UNGOVERNED"}}
        with mock.patch("ssds.admission.genesis.SHADOW_MODES", ("LEGACY", "UNGOVERNED", "NATIVE")):
            prepared = prepare_genesis(self.spec(modes=native), self.home, self.trees)
            admit_genesis(self.home, "demo", sshsig(self.private, prepared.message))
        self.admission = Admission(self.home, "demo", self.trees)
        self.issuer = self.register_issue_key()

    def obligation(self, holder: str = "REVIEWER") -> str:
        """An obligation the head derives for ``holder``: what an envelope names."""

        from ssds.derivation import Workflow, derive

        support = derive(read_chain(self.home.ledger_repository("demo"), "demo"), self.trees)
        return next(o.id for o in Workflow(support).obligations if o.holder == holder)

    def human(self) -> str:
        from ssds.ledger.read import human_key_id

        return human_key_id(self.public)

    def lifecycle(self, action: str, key: dict, private=None, actor=None, **fields) -> int:
        """A ``KEY_LIFECYCLE`` record through the human gate's real path (§25.2), approved by ``private``."""

        rec = record("KEY_LIFECYCLE", target=None, actor=actor or self.human(),
                     fields={"action": action, "key": key, **fields})
        return self.admission.admit_lifecycle(rec, sshsig(private or self.private, self.admission.lifecycle_message(rec)),
                                              self.baseline)

    def issuer_at(self, name: str):
        from ssds.dispatcher.issue import Issuer
        from ssds.ledger.qualification import Home

        return Issuer(Home(self.root / name), "demo")

    def register_issue_key(self):
        """A Dispatcher issue key registered by the human gate's real ``KEY_LIFECYCLE`` path (§25.2)."""

        from ssds.dispatcher.issue import Issuer

        issuer = Issuer(self.home, "demo")
        self.lifecycle("REGISTER", issuer.trust_root())
        return issuer

    def issue(self, route="HARNESS", issuer=None):
        head = len(self.entries()) - 1
        return (issuer or self.issuer).issue(task_id=f"task-{head}-{route}", obligation_id=self.obligation(), role="REVIEWER",
                                             contract_revision=None, governs={"mode": "LEGACY", "protocol": "7.2.1"},
                                             route=route, issued_at_position=head)

    def bind(self, rec: dict, issued, keep_id: bool = False, keep_actor: bool = False) -> dict:
        """The record bound to the issued envelope as its task's agent's (§25.1); ``keep_id`` keeps a deliberately
        wrong ``id``, ``keep_actor`` the record's own actor."""

        from ssds.admission.request import binding_digest
        from ssds.ledger.read import with_id

        lineage = "ATTESTED_FRESH" if issued.envelope["route"] == "HARNESS" else "UNKNOWN"
        sessions = [issued.attestation["session"]] if issued.attestation else []  # the closure, no inputs (F11)
        if not keep_actor:
            rec = {**rec, "actor": f"agent:{issued.envelope['task_id']}/1", "actor_class": "AGENT"}
        envelope = issued.envelope
        out = with_id({**rec, "binding": {"task": envelope["task_id"], "obligation": envelope["obligation_id"],
                                         "role": envelope["role"], "lineage": sessions, "lineage_class": lineage,
                                         "envelope": binding_digest(issued.binding())}})
        return {**out, "id": rec["id"]} if keep_id else out

    def signed(self, issued, records, extra=None, **overrides) -> dict:
        """The request, bound and signed by the task's credential over its final content."""

        req = self.request(records, base_position=len(self.entries()) - 1, **overrides)
        req.update(extra or {})
        req["binding"] = issued.binding(req)
        return req

    def bound(self, records, route="HARNESS", issuer=None, **overrides):
        issued = self.issue(route, issuer)
        rebound = [self.bind(r, issued) for r in records]
        return self.signed(issued, rebound, **overrides), rebound

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
        self.assertEqual(len(self.entries()), 3, "genesis, the issue key's registration and one admission entry")

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
        self.assertEqual(len(self.entries()), 2)


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
        issued = self.issue()
        first = self.bind(finding(), issued)
        second = self.bind(record("FINDING", target={"records": [first["id"]]}, fields={"materiality": "ROUTINE"}), issued)
        decision = self.admit(self.signed(issued, [first, second]))
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
        self.assertEqual((decision.decision, decision.reasons, decision.admitted), ("REJECT", unbound(), ()))

    def test_an_authenticated_rejected_request_salvages_its_never_lost_records(self) -> None:
        issued = self.issue()
        report, bad = self.bind(finding(), issued), self.bind(finding(note="ghp_" + "a1B2" * 9), issued)
        decision = self.admit(self.signed(issued, [report, bad]))
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



SUBMITTED_BASE, SUBMITTED_CANDIDATE = "1" * 40, "2" * 40
SUBMITTED = transformation_id(SUBMITTED_BASE, SUBMITTED_CANDIDATE)


def task_result(x: str, scope=("guide",), key: str | None = "sha256:" + "a" * 64, task="t-1") -> dict:
    from ssds.ledger.read import with_id

    target = {"task": task, "transformation": x}
    if x == SUBMITTED:  # a result that submits X carries B and C under §7.1's identity (review 64a0330)
        target.update(base=SUBMITTED_BASE, candidate=SUBMITTED_CANDIDATE)
    rec = record("TASK_RESULT", target=target, outcome="COMPLETE", actor="agent:t/1", actor_class="AGENT",
                 fields={"slots": {}})
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
        self.assertEqual(len(self.entries()), 3, "the chain still verifies")
        self.assertTrue(self.admit(self.request([finding()])).appended, "and the next request appends")

    def test_b2_salvage_admits_only_records_that_passed_their_own_checks(self) -> None:
        issued = self.issue()
        good = self.bind(finding(), issued)
        broken = self.bind({**finding(materiality="MATERIAL"), "id": "sha256:" + "f" * 64}, issued, keep_id=True)
        secret = self.bind(finding(note="ghp_" + "a1B2" * 9), issued)
        dangling = self.bind(record("FINDING", target={"records": [secret["id"]]}, fields={"materiality": "ROUTINE"}), issued)
        digest, text = ledger_object({"token": "Zq8vR2xK9mW4pT7nL3sY6cB1Hk5Jd0Fg"})
        decision = self.admit(self.signed(issued, [good, broken, secret, dangling], extra={"extra": True},
                                          objects={digest: text}))
        self.assertEqual(decision.reasons, ("SCHEMA_REQUEST",))
        self.assertEqual(decision.admitted, (good["id"],))
        refused = dict(decision.refused)
        self.assertEqual(refused[secret["id"]], ("SECRET_DETECTED",))
        self.assertEqual(refused[dangling["id"]], ("REF_RECORD",), "a reference resolves only to an admitted record")
        self.assertIn("SCHEMA_RECORD", refused[next(r for r in refused if r not in (secret["id"], dangling["id"]))])
        self.assertEqual(set(self.entries()[-1].objects), {good["binding"]["envelope"]},
                         "only the binding is written: no object that no admitted record references")

    def test_b2_only_verified_referenced_objects_are_written(self) -> None:
        from ssds.ledger.read import with_id

        issued = self.issue()
        digest, text = ledger_object({"parts": []})
        report = self.bind(with_id({**finding(), "refs": [{"store": "LEDGER", "digest": digest,
                                                          "media_type": "application/json"}]}), issued)
        self.admit(self.signed(issued, [report], objects={digest: text}))
        self.assertEqual(set(self.entries()[-1].objects), {digest, report["binding"]["envelope"]})

    def test_b3_objects_are_what_their_key_says(self) -> None:
        digest, text = ledger_object({"a": 1})
        for objects in ({"../evil": text}, {digest: '{"a": 1}'}, {"sha256:" + "0" * 64: text}, {digest: 7}):
            with self.subTest(objects=list(objects)):
                self.assertEqual(self.admit(self.request([finding()], objects=objects)).reasons, unbound("SCHEMA_OBJECT"))
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
                self.assertEqual(self.admit(bad).reasons, unbound("SCHEMA_REQUEST"))
        self.admission.submit(self.request([finding()], base_position=0.25))
        self.admission.submit(self.request([finding(materiality="CRITICAL")]))
        decisions = self.admission.process(self.baseline)
        self.assertEqual(len(decisions), 2)
        self.assertEqual(self.admission.queue, [])

    def test_b7_the_base_commit_must_match_the_base_position(self) -> None:
        self.assertEqual(self.admit(self.request([finding()], base_commit="1" * 40)).reasons, unbound("REF_BASE"))
        self.assertEqual(self.admit(self.request([finding()], base_position=-1)).reasons, unbound("REF_BASE"))

    def test_b8_the_s2_binding_cases_and_duplicates(self) -> None:
        x = SUBMITTED
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
        issued = self.issue()
        x = self.bind(task_result("sha256:" + "b" * 64), issued)
        naming = self.bind(record("FINDING", target={"records": [x["id"]]}, fields={"materiality": "ROUTINE"}), issued)
        decision = self.admit(self.signed(issued, [x, naming]))
        self.assertEqual(decision.admitted, ())
        self.assertIn((naming["id"], ("REF_RECORD",)), decision.refused)

    def test_s2_a_malformed_record_never_poisons_the_queue(self) -> None:
        self.admission.submit(self.request([{"kind": ["x"], "outcome": "y"}]))
        self.admission.submit(self.request([finding(materiality="CRITICAL")]))
        self.assertEqual(len(self.admission.process(self.baseline)), 2)
        self.assertEqual(self.admission.queue, [])

    def test_s3_a_request_beyond_its_bounds_gets_no_per_record_work_and_salvages_nothing(self) -> None:
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

        issued = self.issue()
        used, used_text = ledger_object({"parts": []})
        spare, spare_text = ledger_object({"other": True})
        report = self.bind(with_id({**finding(), "refs": [{"store": "LEDGER", "digest": used,
                                                          "media_type": "application/json"}]}), issued)
        self.admit(self.signed(issued, [report], objects={used: used_text, spare: spare_text}))
        self.assertEqual(set(self.entries()[-1].objects), {used, report["binding"]["envelope"]})

    def test_n6_remaining_discriminators(self) -> None:
        import hashlib

        from ssds.admission.checks import content_identity

        text = '{"a": 1}'
        digest = "sha256:" + hashlib.sha256(text.encode()).hexdigest()
        self.assertEqual(self.admit(self.request([finding()], objects={digest: text})).reasons, unbound("SCHEMA_OBJECT"),
                         "a non-canonical text whose digest matches is still refused")
        for field, value in (("candidates", ["not-a-commit"]), ("adopted_deltas", ["x"]), ("binding", "x")):
            with self.subTest(field=field):
                self.assertEqual(self.admit(self.request([finding()], **{field: value})).reasons, unbound("SCHEMA_REQUEST"))
        issued = self.issue()
        kept = self.bind(finding(materiality="CRITICAL"), issued)
        self.admit(self.signed(issued, [kept]))
        again = self.admit(self.signed(issued, [kept, self.bind(finding(materiality="MATERIAL"), issued)]))
        self.assertIn((kept["id"], ("REF_DUPLICATE",)), again.refused, "a record already in the ledger is a duplicate")
        self.assertNotEqual(content_identity(["a"]), content_identity(["b"]))


class StepTwoThirdCheck(RequestFixture):
    """The third same-family check of 36497a1c: the byte bound measured without encoding (T2) and the repaired
    behaviours' discriminators (T1)."""

    def test_t2_an_unencodable_request_cannot_slip_past_the_byte_bound(self) -> None:
        from ssds.ledger.read import with_id

        issued = self.issue()
        big = self.bind(with_id({**finding(), "provenance": {"note": ["y" * 4000] * 2200}}), issued)
        decision = self.admit(self.signed(issued, [big], extra={"objects": {"x": 1.5}}))
        self.assertIn("SCHEMA_BOUND", decision.reasons)
        self.assertEqual((decision.admitted, decision.refused), ((), ()))

    def test_t1_salvage_drops_dangling_chains_to_a_fixed_point_and_keeps_admitted_names(self) -> None:
        first = self.issue()
        earlier = self.bind(finding(materiality="CRITICAL"), first)
        self.admit(self.signed(first, [earlier]))
        issued = self.issue()
        x = self.bind(task_result("sha256:" + "b" * 64), issued)
        b = self.bind(record("FINDING", target={"records": [x["id"]]}, fields={"materiality": "ROUTINE"}), issued)
        a = self.bind(record("FINDING", target={"records": [b["id"]]}, fields={"materiality": "ROUTINE"}), issued)
        names_earlier = self.bind(record("FINDING", target={"records": [earlier["id"]]}, fields={"materiality": "MATERIAL"}),
                                  issued)
        decision = self.admit(self.signed(issued, [x, b, a, names_earlier]))
        self.assertEqual(decision.admitted, (names_earlier["id"],))
        refused = dict(decision.refused)
        self.assertEqual((refused[a["id"]], refused[b["id"]]), (("REF_RECORD",), ("REF_RECORD",)))

    def test_t1_a_halted_request_returns_to_the_front(self) -> None:
        first, second = self.request([finding()]), self.request([finding(materiality="MATERIAL")])
        self.admission.submit(first)
        self.admission.submit(second)
        with self.assertRaises(AdmissionHalted):
            self.admission.process("0" * 40)
        self.assertEqual(self.admission.queue, [first, second])

    def test_t1_beyond_depth_nothing_is_refused_or_salvaged(self) -> None:
        deep: object = "x"
        for _ in range(100):
            deep = [deep]
        decision = self.admit(self.request([finding()], adopted_deltas=[{"d": deep}]))
        self.assertEqual((decision.reasons, decision.admitted, decision.refused), (("SCHEMA_BOUND",), (), ()))

    def test_t1_each_schema_type_guard_holds_through_the_queue(self) -> None:
        from ssds.ledger.read import with_id

        base = finding()
        broken = [with_id({**base, "actor_class": ["HUMAN"]}),
                  with_id({**base, "basis": [{"mode": ["content"], "target": {}, "class": "EXACT"}]}),
                  with_id({**base, "basis": [{"mode": "content", "target": {"unit": "guide", "rev": "sha256:" + "0" * 64},
                                              "class": ["EXACT"]}]})]
        for record_ in broken:
            self.admission.submit(self.request([record_]))
        self.admission.submit(self.request([finding(materiality="CRITICAL")]))
        decisions = self.admission.process(self.baseline)
        self.assertEqual(len(decisions), 4)
        self.assertTrue(all(d.refused and d.refused[0][1] == ("SCHEMA_RECORD",) for d in decisions[:3]))


def acceptance() -> dict:
    """A passing judgment: not never-lost."""

    return record("ACCEPTANCE", target={"subject": "guide", "scope_id": "sha256:" + "4" * 64, "rev": "sha256:" + "5" * 64},
                  outcome="PASS")


class Envelopes(RequestFixture):
    """Phase F step 3: the task binding's authentication (Manual §8.3 step 3, §12.2, §25.1-§25.2)."""

    def test_a_harness_binding_proves_attested_fresh_lineage(self) -> None:
        req, (report,) = self.bound([finding()])
        decision = self.admit(req)
        self.assertEqual((decision.reasons, decision.admitted), (("SCHEMA_UNSUPPORTED",), (report["id"],)))
        entry = self.entries()[-1]
        self.assertIn(report["binding"]["envelope"], entry.objects, "the binding is stored for replay (§12.2)")

    def test_a_manual_route_is_unknown_lineage_and_cannot_claim_fresh(self) -> None:
        issued = self.issue("MANUAL")
        honest = self.bind(finding(), issued)
        claims_fresh = {**honest, "binding": {**honest["binding"], "lineage_class": "ATTESTED_FRESH"}}
        from ssds.ledger.read import with_id

        claims_fresh = with_id(claims_fresh)
        decision = self.admit(self.signed(issued, [honest, claims_fresh]))
        self.assertEqual(decision.admitted, (honest["id"],))
        self.assertIn((claims_fresh["id"], ("AUTH_ENVELOPE",)), decision.refused)

    def test_a_credential_signature_replayed_onto_another_request_proves_no_fresh_lineage(self) -> None:
        issued = self.issue()
        report = self.bind(finding(), issued)
        first = self.signed(issued, [report])
        second = self.signed(issued, [report, self.bind(finding(materiality="MATERIAL"), issued)])
        second["binding"] = first["binding"]  # the credential signed the first request, not this one
        decision = self.admit(second)
        self.assertEqual(decision.admitted, ())
        self.assertTrue(all(why == ("AUTH_ENVELOPE",) for _, why in decision.refused))

    def test_a_forged_envelope_or_an_unknown_key_authenticates_nothing(self) -> None:
        from ssds.dispatcher.issue import Issuer

        req, _ = self.bound([finding()])
        req["binding"]["envelope"] = {**req["binding"]["envelope"], "role": "PRINCIPAL"}
        forged = self.admit(req)
        self.assertEqual((forged.admitted, "AUTH_ENVELOPE" in forged.reasons), ((), True))
        stranger = self.issuer_at("other-home")
        req, _ = self.bound([finding(materiality="MATERIAL")], issuer=stranger)
        unknown = self.admit(req)
        self.assertEqual((unknown.admitted, "AUTH_ENVELOPE" in unknown.reasons), ((), True))

    def test_auth_version_when_a_record_governs_differently_from_its_envelope(self) -> None:
        from ssds.ledger.read import with_id

        issued = self.issue()
        other = self.bind(with_id({**finding(), "governs": {"mode": "LEGACY", "protocol": "7.1.0"}}), issued)
        self.assertEqual(self.admit(self.signed(issued, [other])).refused, ((other["id"], ("AUTH_VERSION",)),))

    def test_a_retired_key_covers_only_never_lost_records_of_the_envelopes_it_lists(self) -> None:
        from ssds.admission.request import binding_digest
        from ssds.dispatcher.issue import Issuer

        old = self.issuer_at("old-dispatcher")
        self.lifecycle("REGISTER", old.trust_root())
        listed, unlisted = self.issue(issuer=old), self.issue("MANUAL", issuer=old)
        self.lifecycle("RETIRE", old.trust_root(), outstanding=[binding_digest(listed.binding())])
        report, judgment_ = self.bind(finding(), listed), self.bind(acceptance(), listed)
        decision = self.admit(self.signed(listed, [report, judgment_]))
        self.assertEqual(decision.admitted, (report["id"],))
        self.assertIn((judgment_["id"], ("AUTH_ENVELOPE",)), decision.refused)
        late = self.admit(self.signed(unlisted, [self.bind(finding(materiality="MATERIAL"), unlisted)]))
        self.assertEqual((late.admitted, "AUTH_ENVELOPE" in late.reasons), ((), True))

    def test_a_compromised_key_is_untrusted_from_its_position_on(self) -> None:
        before = self.issue()
        self.lifecycle("COMPROMISED", self.issuer.trust_root(), from_position=len(self.entries()))
        after = self.issue()
        ok = self.admit(self.signed(before, [self.bind(finding(), before)]))
        self.assertEqual(len(ok.admitted), 1, "an envelope issued before the compromise position still verifies")
        bad = self.admit(self.signed(after, [self.bind(finding(materiality="MATERIAL"), after)]))
        self.assertEqual((bad.admitted, "AUTH_ENVELOPE" in bad.reasons), ((), True))

    def test_a_human_binding_covers_only_that_humans_records(self) -> None:
        from ssds.admission.request import request_message
        from ssds.ledger.read import with_id

        mine = with_id({**finding(), "actor": self.human()})
        theirs = finding(materiality="MATERIAL")
        req = self.request([mine, theirs], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        decision = self.admit(req)
        self.assertEqual(decision.admitted, (mine["id"],))
        self.assertIn((theirs["id"], ("AUTH_ACTOR",)), decision.refused)
        req["binding"]["human"]["signature"] = sshsig(self.private, b"something else")
        self.assertIn("AUTH_ENVELOPE", self.admit(req).reasons)

    def test_a_lifecycle_record_needs_a_registered_humans_approval(self) -> None:
        from ssds.admission.engine import EntryInvalid

        other_private, _ = __import__("tests.ssds._fixtures", fromlist=["human_key"]).human_key(self.root, "intruder")
        rec = record("KEY_LIFECYCLE", target=None, actor=self.human(),
                     fields={"action": "REGISTER", "key": self.issuer_at("x").trust_root()})
        with self.assertRaises(EntryInvalid):
            self.admission.admit_lifecycle(rec, sshsig(other_private, self.admission.lifecycle_message(rec)),
                                           self.baseline)
        position = self.admission.admit_lifecycle(rec, sshsig(self.private, self.admission.lifecycle_message(rec)),
                                                  self.baseline)
        lifecycle = self.entries()[position].entry["lifecycle"]
        self.assertEqual(lifecycle["provenance"]["approval"]["actor"], self.human())

    def test_the_issue_key_is_private_operator_state(self) -> None:
        import os

        from ssds.dispatcher.issue import Issuer
        from ssds.ledger.qualification import Home, HomeRefused

        os.chmod(self.issuer.path, 0o644)
        with self.assertRaises(HomeRefused):
            Issuer(self.home, "demo")
        os.chmod(self.issuer.path, 0o600)
        linked = self.root / "linked-home"
        (linked / "keys").mkdir(parents=True)
        os.symlink(self.issuer.path.parent, linked / "keys" / "dispatcher")
        with self.assertRaises(HomeRefused):
            Issuer(Home(linked), "demo")


class JournalAndBrief(RequestFixture):
    """Phase F step 3b: the operator journal (§8.1, §22.4, §25.2) and the brief's identity in the envelope (§16.4)."""

    def test_a_retirement_lists_the_outstanding_envelopes_the_journal_compiles(self) -> None:
        from ssds.dispatcher.journal import Journal

        journal = Journal(self.home, "demo")
        done, open_ = self.issue(), self.issue("MANUAL")
        journal.issued(done.envelope["task_id"], done.binding())
        journal.issued(open_.envelope["task_id"], open_.binding())
        outstanding = journal.outstanding(self.issuer.key_id, finished_tasks=[done.envelope["task_id"]])
        self.assertEqual(len(outstanding), 1)
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=outstanding)
        still = self.admit(self.signed(open_, [self.bind(finding(), open_)]))
        self.assertEqual(len(still.admitted), 1, "an outstanding envelope still covers its never-lost records")
        gone = self.admit(self.signed(done, [self.bind(finding(materiality="MATERIAL"), done)]))
        self.assertEqual((gone.admitted, "AUTH_ENVELOPE" in gone.reasons), ((), True))

    def test_undecided_requests_are_kept_for_resubmission_by_identity(self) -> None:
        from ssds.dispatcher.journal import Journal

        journal = Journal(self.home, "demo")
        req, _ = self.bound([finding()])
        rid = journal.submitted(req)
        self.assertEqual(journal.undecided(), [req])
        journal.decided(self.admit(req).request_id)
        self.assertEqual((rid, journal.undecided()), (request_id(req), []))

    def test_the_journal_is_private_operator_state(self) -> None:
        import os

        from ssds.dispatcher.journal import Journal
        from ssds.ledger.qualification import Home, HomeRefused

        journal = Journal(self.home, "demo")
        journal.decided("sha256:" + "0" * 64)
        os.chmod(journal.path, 0o644)
        with self.assertRaises(HomeRefused):
            journal.entries()
        os.chmod(journal.path, 0o600)
        linked = self.root / "elsewhere"
        linked.mkdir()
        target = Journal(Home(self.root / "linked-home"), "demo")
        target.path.parent.parent.mkdir(parents=True)
        os.symlink(linked, target.path.parent)  # placed after the construction's check: the write walk refuses it
        with self.assertRaises(HomeRefused):
            target.decided("sha256:" + "1" * 64)

    def test_the_rendered_brief_is_recorded_in_the_envelope_and_signed(self) -> None:
        import hashlib

        head = len(self.entries()) - 1
        brief = b"# Task brief\n\nDo the thing.\n"
        issued = self.issuer.issue(task_id="t-brief", obligation_id=self.obligation(), role="REVIEWER", contract_revision=None,
                                   governs={"mode": "LEGACY", "protocol": "7.2.1"}, route="HARNESS",
                                   issued_at_position=head, brief=brief)
        self.assertEqual(issued.envelope["brief"], "sha256:" + hashlib.sha256(brief).hexdigest())
        report = self.bind(finding(), issued)
        self.assertEqual(len(self.admit(self.signed(issued, [report])).admitted), 1)
        tampered = self.signed(issued, [self.bind(finding(materiality="MATERIAL"), issued)])
        tampered["binding"]["envelope"] = {**tampered["binding"]["envelope"], "brief": "sha256:" + "9" * 64}
        self.assertIn("AUTH_ENVELOPE", self.admit(tampered).reasons, "the brief's identity is under the signature")


class _Item:
    """A stored entry as :func:`ssds.derivation.trust_roots` reads it."""

    def __init__(self, position: int, lifecycle) -> None:
        self.position, self.entry = position, {"lifecycle": lifecycle}


class StepThreeReview(RequestFixture):
    """The same-family review of e6ac0091 (Phase F step 3a): each blocker's and surviving mutant's discriminator."""

    def assert_unauthenticated(self, decision, reason="AUTH_ENVELOPE") -> None:
        self.assertIn(reason, decision.reasons)
        self.assertEqual((decision.admitted, decision.refused), ((), ()))
        self.assertEqual(dict(self.entries()[-1].objects), {}, "nothing of an unauthenticated binding is stored")

    # -- B1: an envelope authenticates its task's agent only --------------------------------------------------

    def test_b1_a_bound_human_machinery_or_other_task_record_is_refused(self) -> None:
        from ssds.ledger.read import with_id

        issued = self.issue()
        human = self.bind(finding(), issued, keep_actor=True)  # the fixture's human:SHA256:test, class HUMAN
        runner = self.bind(with_id({**record("CHECK_EXECUTION", target={"obligation": "obl", "candidate": self.baseline},
                                             outcome="CLEAN", fields={"template": "unit-tests"}),
                                    "actor": "machinery:runner", "actor_class": "MACHINERY"}), issued, keep_actor=True)
        other = self.bind(with_id({**finding(materiality="MATERIAL"), "actor": "agent:another-task/1",
                                   "actor_class": "AGENT"}), issued, keep_actor=True)
        mine = self.bind(finding(materiality="CRITICAL"), issued)
        decision = self.admit(self.signed(issued, [human, runner, other, mine]))
        refused = dict(decision.refused)
        for rec in (human, runner, other):
            self.assertIn("AUTH_ACTOR", refused[rec["id"]])
        self.assertEqual(decision.admitted, (mine["id"],))

    # -- B2: a binding that carries a secret authenticates nothing -------------------------------------------

    def test_b2_a_binding_carrying_a_secret_is_neither_authenticated_nor_stored(self) -> None:
        head = len(self.entries()) - 1
        issued = self.issuer.issue(task_id="t-secret", obligation_id=self.obligation(), role="REVIEWER", contract_revision=None,
                                   governs={"mode": "LEGACY", "protocol": "7.2.1"}, route="HARNESS",
                                   issued_at_position=head, predecessors={"note": "Zq8mX3vT9kL2pW7nR4sY6bH1cJ5dF0gA"})
        self.assert_unauthenticated(self.admit(self.signed(issued, [self.bind(finding(), issued)])), "SECRET_DETECTED")

    # -- B3: unverified attestation material is never stored ------------------------------------------------

    def test_b3_a_manual_envelope_with_made_up_attestation_material_authenticates_nothing(self) -> None:
        issued = self.issue("MANUAL")
        req = self.signed(issued, [self.bind(finding(), issued)])
        req["binding"] = {**req["binding"], "attestation": {"task_id": issued.envelope["task_id"], "anything": "goes"},
                          "attestation_signature": "00" * 64}
        self.assert_unauthenticated(self.admit(req))

    def test_b3_m3b_a_self_minted_credential_never_proves_fresh_lineage(self) -> None:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

        from ssds.dispatcher.issue import TaskCredential

        issued = self.issue()
        mine = TaskCredential(Ed25519PrivateKey.generate())
        attestation = {**issued.attestation, "credential_key": mine.public_hex}
        req = self.signed(issued, [self.bind(finding(), issued)])
        req["binding"] = {**req["binding"], "attestation": attestation}
        req["binding"]["credential_signature"] = mine.sign(req)
        self.assert_unauthenticated(self.admit(req))

    def test_b3_an_attestation_is_bound_to_its_envelope(self) -> None:
        first = self.issue()
        second = self.issuer.issue(task_id=first.envelope["task_id"], obligation_id=self.obligation(), role="REVIEWER",
                                   contract_revision="another", governs={"mode": "LEGACY", "protocol": "7.2.1"},
                                   route="HARNESS", issued_at_position=len(self.entries()) - 1)
        req = self.signed(second, [self.bind(finding(), second)])
        req["binding"] = {**req["binding"], "attestation": first.attestation,
                          "attestation_signature": first.attestation_signature,
                          "credential_signature": first.credential.sign(req)}
        self.assert_unauthenticated(self.admit(req))

    def test_b3_a_harness_binding_without_its_attestation_authenticates_nothing(self) -> None:
        issued = self.issue()
        req = self.signed(issued, [self.bind(finding(), issued)])
        req["binding"] = {**req["binding"], "attestation": None, "attestation_signature": None,
                          "credential_signature": None}
        self.assert_unauthenticated(self.admit(req))

    # -- B4: untrusted input inside a well-shaped binding never crashes Admission ---------------------------

    def test_b4_a_float_inside_the_envelope_or_attestation_is_a_recorded_rejection(self) -> None:
        for where in ("envelope", "attestation"):
            issued = self.issue()
            req = self.signed(issued, [self.bind(finding(note=where), issued)])
            field_ = "contract_revision" if where == "envelope" else "session"
            req["binding"] = {**req["binding"], where: {**req["binding"][where], field_: 1.5}}
            before = len(self.entries())
            decision = self.admit(req)
            self.assertIn("AUTH_ENVELOPE", decision.reasons)
            self.assertEqual((len(self.entries()), decision.admitted), (before + 1, ()))

    # -- B5: a lifecycle approval is spent by its entry -------------------------------------------------------

    def test_b5_a_replayed_register_after_its_retirement_is_refused(self) -> None:
        from ssds.admission.engine import EntryInvalid
        from ssds.derivation import trust_roots

        old = self.issuer_at("replayed")
        register = record("KEY_LIFECYCLE", target=None, actor=self.human(),
                          fields={"action": "REGISTER", "key": old.trust_root()})
        approval = sshsig(self.private, self.admission.lifecycle_message(register))
        self.admission.admit_lifecycle(register, approval, self.baseline)
        self.lifecycle("RETIRE", old.trust_root())
        with self.assertRaises(EntryInvalid):
            self.admission.admit_lifecycle(register, approval, self.baseline)
        with self.assertRaises(EntryInvalid):  # re-signed for the new head, it is still the admitted record
            self.admission.admit_lifecycle(register, sshsig(self.private, self.admission.lifecycle_message(register)),
                                           self.baseline)
        self.assertNotIn(old.key_id, trust_roots(self.entries()).issue)

    def test_b5_an_identical_lifecycle_record_is_admitted_once(self) -> None:
        from ssds.admission.engine import EntryInvalid

        compromise = record("KEY_LIFECYCLE", target=None, actor=self.human(),
                            fields={"action": "COMPROMISED", "key": self.issuer.trust_root(), "from_position": 1})
        self.admission.admit_lifecycle(compromise, sshsig(self.private, self.admission.lifecycle_message(compromise)),
                                       self.baseline)
        with self.assertRaises(EntryInvalid):  # the only action an identical replay could pass otherwise
            self.admission.admit_lifecycle(compromise, sshsig(self.private, self.admission.lifecycle_message(compromise)),
                                           self.baseline)

    def test_b5_the_approval_names_the_ledger_position_and_head(self) -> None:
        from ssds.admission.engine import EntryInvalid
        from ssds.admission.lifecycle import lifecycle_message

        rec = record("KEY_LIFECYCLE", target=None, actor=self.human(),
                     fields={"action": "REGISTER", "key": self.issuer_at("stale").trust_root()})
        head = self.entries()[-1]
        here = lifecycle_message("demo", head.position + 1, head.digest, rec)
        self.assertEqual(here, self.admission.lifecycle_message(rec))
        self.assertNotEqual(here, lifecycle_message("other", head.position + 1, head.digest, rec))
        stale = sshsig(self.private, here)
        self.lifecycle("REGISTER", self.issuer_at("between").trust_root())
        with self.assertRaises(EntryInvalid):
            self.admission.admit_lifecycle(rec, stale, self.baseline)

    # -- B6: closed key shapes; a reader that never raises --------------------------------------------------

    def test_b6_malformed_or_rebinding_key_objects_are_refused_and_the_ledger_keeps_working(self) -> None:
        from ssds.admission.engine import EntryInvalid

        key = self.issuer.trust_root()
        other = self.issuer_at("other").trust_root()
        cases = [("COMPROMISED", {"role": "ISSUE"}, {}),
                 ("RETIRE", {**other, "retires": key["id"]}, {}),
                 ("RETIRE", {"id": key["id"], "retires": key["id"], "role": "ISSUE"}, {}),
                 ("REGISTER", {**other, "id": key["id"]}, {}),
                 ("REGISTER", key, {}),
                 ("RETIRE", other, {}),
                 ("ROTATE", {**other, "retires": "ed25519:" + "0" * 64}, {}),
                 ("REGISTER", {**other, "role": "RUNNER"}, {}),
                 ("REGISTER", other, {"from_position": 1}),
                 ("COMPROMISED", key, {"from_position": 10 ** 6})]
        for action, key_object, extra in cases:
            with self.subTest(action=action, key=key_object, extra=extra), self.assertRaises(EntryInvalid):
                self.lifecycle(action, key_object, **extra)
        req, (report,) = self.bound([finding()])
        self.assertEqual(self.admit(req).admitted, (report["id"],), "the ledger still validates")

    def test_b6_m11_a_rotation_retires_the_old_key(self) -> None:
        from ssds.admission.request import binding_digest

        listed, unlisted = self.issue(), self.issue("MANUAL")
        new = self.issuer_at("rotated")
        self.lifecycle("ROTATE", {**new.trust_root(), "retires": self.issuer.key_id},
                       outstanding=[binding_digest(listed.binding())])
        orphan = self.bind(finding(), unlisted)
        refused = self.admit(self.signed(unlisted, [orphan]))
        self.assertEqual((refused.admitted, refused.refused), ((), ((orphan["id"], ("AUTH_ENVELOPE",)),)),
                         "the rotated key no longer covers it: refused by identity, kept for re-issue (step 4b-ii)")
        kept = self.admit(self.signed(listed, [self.bind(finding(materiality="MATERIAL"), listed)]))
        self.assertEqual(len(kept.admitted), 1, "a listed envelope still covers its never-lost records")
        fresh = self.issue(issuer=new)
        self.assertEqual(len(self.admit(self.signed(fresh, [self.bind(finding(materiality="CRITICAL"), fresh)]))
                             .admitted), 1)

    def test_b6_the_reader_is_total_and_m20_reads_genesis_issue_keys(self) -> None:
        from ssds.derivation import trust_roots

        key = self.issuer.trust_root()
        junk = [_Item(1, {"kind": "KEY_LIFECYCLE", "fields": {"action": "COMPROMISED", "key": {"role": "ISSUE"}}}),
                _Item(2, {"kind": "KEY_LIFECYCLE", "fields": {"action": "RETIRE", "key": [1]}}),
                _Item(3, {"kind": "KEY_LIFECYCLE", "fields": None}),
                _Item(4, {"kind": "GENESIS", "fields": {"trust_roots": {"dispatcher_keys": [7, {"id": 1}]}}}),
                _Item(5, "not a record")]
        self.assertEqual(trust_roots(junk).issue, {})
        genesis = _Item(0, {"kind": "GENESIS", "fields": {"trust_roots": {"dispatcher_keys": [key], "human_keys": []}}})
        self.assertEqual(trust_roots([genesis, *junk]).issue, {key["id"]: key["public_key"]})

    def test_b6_m2b_a_retired_and_compromised_key_covers_nothing(self) -> None:
        from ssds.admission.request import binding_digest

        listed = self.issue()
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[binding_digest(listed.binding())])
        self.lifecycle("COMPROMISED", self.issuer.trust_root(), from_position=len(self.entries()))
        self.assert_unauthenticated(self.admit(self.signed(listed, [self.bind(finding(), listed)])))

    def test_b6_m7b_a_lifecycle_approval_is_the_named_humans_own(self) -> None:
        from ssds.admission.engine import EntryInvalid
        from ssds.ledger.read import human_key_id

        from ._fixtures import human_key

        second, line = human_key(self.root, "second")
        self.lifecycle("REGISTER", {"role": "HUMAN", "id": human_key_id(line), "public_key": line})
        with self.assertRaises(EntryInvalid):
            self.lifecycle("REGISTER", self.issuer_at("by-the-wrong-human").trust_root(), private=second)
        self.lifecycle("REGISTER", self.issuer_at("by-the-second-human").trust_root(), private=second,
                       actor=human_key_id(line))

    def test_b6_the_last_human_key_is_rotated_never_retired(self) -> None:
        from ssds.admission.engine import EntryInvalid
        from ssds.derivation import trust_roots
        from ssds.ledger.read import human_key_id

        from ._fixtures import human_key

        mine = {"role": "HUMAN", "id": self.human(), "public_key": self.public}
        with self.assertRaises(EntryInvalid):
            self.lifecycle("RETIRE", mine)
        successor, line = human_key(self.root, "successor")
        self.lifecycle("ROTATE", {"role": "HUMAN", "id": human_key_id(line), "public_key": line, "retires": self.human()})
        roots = trust_roots(self.entries())
        self.assertEqual((set(roots.humans), self.human() in roots.former_humans), ({human_key_id(line)}, True))
        with self.assertRaises(EntryInvalid):  # a former key is never registered again
            self.lifecycle("REGISTER", mine, private=successor, actor=human_key_id(line))

    # -- M4b, M4c: each bound record names this envelope and this task ------------------------------------

    def test_m4_a_record_naming_another_envelope_or_task_is_refused(self) -> None:
        from ssds.ledger.read import with_id

        issued, elsewhere = self.issue(), self.issue("MANUAL")
        good = self.bind(finding(), issued)
        wrong_envelope = with_id({**self.bind(finding(materiality="MATERIAL"), issued),
                                  "binding": {**good["binding"], "envelope": self.bind(finding(), elsewhere)["binding"][
                                      "envelope"]}})
        wrong_task = with_id({**self.bind(finding(materiality="CRITICAL"), issued),
                              "binding": {**good["binding"], "task": "another-task"}})
        decision = self.admit(self.signed(issued, [good, wrong_envelope, wrong_task]))
        self.assertEqual(decision.admitted, (good["id"],))
        refused = dict(decision.refused)
        self.assertEqual((refused[wrong_envelope["id"]], refused[wrong_task["id"]]), (("AUTH_ENVELOPE",),) * 2)

    # -- B7: the issue key and the journal live in the Home owner's checked tree --------------------------

    def test_b7_a_traversing_ledger_id_or_a_home_inside_a_repository_is_refused(self) -> None:
        from ssds.dispatcher.issue import Issuer
        from ssds.dispatcher.journal import Journal
        from ssds.ledger.qualification import Home, HomeRefused

        for owner in (Issuer, Journal):
            with self.subTest(owner=owner.__name__):
                with self.assertRaises(HomeRefused):
                    owner(self.home, "../../escaped")
                with self.assertRaises(HomeRefused):
                    owner(Home(self.product / "home"), "demo")
        self.assertFalse((self.root / "escaped.ed25519").exists())
        self.assertFalse((self.product / "home").exists())

    def test_b7_a_link_placed_after_the_check_is_never_followed_even_inside_the_home(self) -> None:
        import os

        from ssds.dispatcher.journal import Journal
        from ssds.ledger.qualification import Home, HomeRefused

        journal = Journal(Home(self.root / "fresh-home"), "demo")
        decoy = self.root / "fresh-home" / "state" / "decoy"
        decoy.mkdir(parents=True)
        os.symlink(decoy, journal.path.parent)  # resolves inside the home: only the no-follow walk refuses it
        with self.assertRaises(HomeRefused):
            journal.decided("sha256:" + "2" * 64)
        self.assertEqual(list(decoy.iterdir()), [])



class StepThreeRecheck(RequestFixture):
    """The same-family re-check of a71cca2f: N1 (a compromise never relaxed), N2 (a torn journal tail) and N3 (the
    repaired claims' discriminators, named by the re-check's mutants m1-m47)."""

    assert_unauthenticated = StepThreeReview.assert_unauthenticated

    def resigned(self, issued, req, envelope=None, attestation=None) -> dict:
        """``req`` with its binding's envelope or attestation replaced and re-signed by the real issue key, and the
        request signed again by the task's credential: only the replaced content can be what is refused."""

        from ssds.admission.request import attestation_message, envelope_message

        binding = dict(req["binding"])
        if envelope is not None:
            binding.update(envelope=envelope, signature=self.issuer._key.sign(envelope_message(envelope)).hex())
        if attestation is not None:
            binding.update(attestation=attestation,
                           attestation_signature=self.issuer._key.sign(attestation_message(attestation)).hex())
        out = {**req, "binding": binding}
        out["binding"]["credential_signature"] = issued.credential.sign(out) if issued.credential else None
        return out

    # -- N1 ----------------------------------------------------------------------------------------------------

    def test_n1_a_later_compromise_never_relaxes_an_earlier_one(self) -> None:
        from ssds.admission.engine import EntryInvalid
        from ssds.derivation import trust_roots

        early = self.issue()
        self.lifecycle("COMPROMISED", self.issuer.trust_root(), from_position=early.envelope["issued_at_position"])
        with self.assertRaises(EntryInvalid):
            self.lifecycle("COMPROMISED", self.issuer.trust_root(), from_position=len(self.entries()))
        self.assert_unauthenticated(self.admit(self.signed(early, [self.bind(finding(), early)])))
        self.lifecycle("COMPROMISED", self.issuer.trust_root(), from_position=0)  # earlier: admitted
        self.assertEqual(trust_roots(self.entries()).compromised[self.issuer.key_id], 0)

    def test_n1_both_readers_keep_the_earliest_compromise(self) -> None:
        from ssds.derivation import trust_roots
        from ssds.ledger.read import _keys_in_force

        key = {**self.issuer.trust_root()}
        items = [_Item(1, {"kind": "KEY_LIFECYCLE", "fields": {"action": "COMPROMISED", "key": key, "from_position": 1}}),
                 _Item(5, {"kind": "KEY_LIFECYCLE", "fields": {"action": "COMPROMISED", "key": key, "from_position": 4}})]
        self.assertEqual(trust_roots(items).compromised[key["id"]], 1)
        host = [_Host(i.position, {**i.entry["lifecycle"], "fields": {**i.entry["lifecycle"]["fields"],
                                                                     "key": {**key, "role": "ADMISSION"}}})
                for i in items]
        self.assertEqual(_keys_in_force(host)[1][key["id"]], 1)

    # -- N2 ----------------------------------------------------------------------------------------------------

    def test_n2_a_torn_tail_is_dropped_and_the_next_entry_is_kept(self) -> None:
        from ssds.dispatcher.journal import Journal

        journal = Journal(self.home, "demo")
        done, open_ = self.issue(), self.issue("MANUAL")
        journal.issued(done.envelope["task_id"], done.binding())
        with open(journal.path, "ab") as handle:  # a crash part-way through the next append
            handle.write(b'{"kind":"ISSUED","task_id":"tor')
        self.assertEqual(len(journal.entries()), 1, "an unterminated last line was never acknowledged")
        journal.issued(open_.envelope["task_id"], open_.binding())
        self.assertEqual(len(journal.outstanding(self.issuer.key_id, finished_tasks=[])), 2)
        self.assertTrue(journal.path.read_bytes().endswith(b"\n"))

    def test_n2_corruption_before_the_last_line_is_refused(self) -> None:
        from ssds.dispatcher.journal import Journal, JournalCorrupt

        journal = Journal(self.home, "demo")
        journal.decided("sha256:" + "0" * 64)
        with open(journal.path, "ab") as handle:
            handle.write(b"not json\n")
        journal.decided("sha256:" + "1" * 64)
        with self.assertRaises(JournalCorrupt):
            journal.entries()

    # -- N3: authentication --------------------------------------------------------------------------------

    def test_m1_m2_the_agent_actor_needs_its_class_and_an_attempt_number(self) -> None:
        from ssds.ledger.read import with_id

        issued = self.issue()
        task = issued.envelope["task_id"]
        no_attempt = self.bind(with_id({**finding(), "actor": f"agent:{task}/x", "actor_class": "AGENT"}), issued,
                               keep_actor=True)
        human_class = self.bind(with_id({**finding(materiality="MATERIAL"), "actor": f"agent:{task}/1",
                                         "actor_class": "HUMAN"}), issued, keep_actor=True)
        refused = dict(self.admit(self.signed(issued, [no_attempt, human_class])).refused)
        self.assertEqual((refused[no_attempt["id"]], refused[human_class["id"]]), (("AUTH_ACTOR",),) * 2)

    def test_m3_m4_an_envelope_beyond_the_head_or_on_no_route_authenticates_nothing(self) -> None:
        for change in ({"issued_at_position": 10 ** 6}, {"route": "TELEPATHY"}):
            with self.subTest(change=change):
                issued = self.issue("MANUAL")
                req = self.signed(issued, [self.bind(finding(note=str(change)), issued)])
                self.assert_unauthenticated(self.admit(self.resigned(issued, req, envelope={**issued.envelope, **change})))

    def test_m5_to_m8_an_issue_signed_attestation_must_still_be_this_tasks(self) -> None:
        issued = self.issue()
        changes = [{"task_id": "another-task"}, {"input_sessions": ["session:other"]}, {"extra": "field"},
                   {"session": "not a token"}]
        for change in changes:
            with self.subTest(change=change):
                req = self.signed(issued, [self.bind(finding(note=str(change)), issued)])
                self.assert_unauthenticated(self.admit(self.resigned(issued, req,
                                                                     attestation={**issued.attestation, **change})))

    def test_m14_m15_a_human_binding_covers_only_unbound_human_class_records(self) -> None:
        from ssds.admission.request import request_message
        from ssds.ledger.read import with_id

        issued = self.issue()
        bound = self.bind(with_id({**finding(), "actor": self.human()}), issued, keep_actor=True)
        agent_class = with_id({**finding(materiality="MATERIAL"), "actor": self.human(), "actor_class": "AGENT"})
        req = self.request([bound, agent_class], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        refused = dict(self.admit(req).refused)
        self.assertEqual((refused[bound["id"]], refused[agent_class["id"]]), (("AUTH_ACTOR",),) * 2)

    def test_m16_a_binding_is_stored_only_with_admitted_records(self) -> None:
        from ssds.ledger.read import with_id

        issued = self.issue()
        other = self.bind(with_id({**finding(), "governs": {"mode": "LEGACY", "protocol": "7.1.0"}}), issued)
        decision = self.admit(self.signed(issued, [other]))
        self.assertEqual((decision.admitted, dict(self.entries()[-1].objects)), ((), {}))

    def test_m47_a_secret_in_a_human_binding_is_a_secret_not_a_bad_signature(self) -> None:
        req = self.request([finding()], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": "ghp_" + "a1B2" * 9}}
        self.assertEqual(self.admit(req).reasons, ("SECRET_DETECTED",))

    # -- N3: lifecycle -----------------------------------------------------------------------------------------

    def test_m18_m21_m22_m36_m38_lifecycle_shapes_and_the_gate(self) -> None:
        from ssds.admission.engine import EntryInvalid
        from ssds.ledger.read import with_id

        other = self.issuer_at("shapes").trust_root()
        cases = [("COMPROMISED", self.issuer_at("never-registered").trust_root(), {}),  # m18
                 ("REGISTER", {**other, "note": "x"}, {}),  # m21
                 ("REGISTER", other, {"outstanding": []}),  # m22
                 ("REGISTER", {**other, "id": "ed25519:" + "1" * 64}, {}),  # m38
                 ("REGISTER", {**other, "role": ["ISSUE"]}, {}),  # a list-valued role
                 ("COMPROMISED", self.issuer.trust_root(), {"outstanding": []})]
        for action, key_object, extra in cases:
            with self.subTest(action=action, key=key_object, extra=extra), self.assertRaises(EntryInvalid):
                self.lifecycle(action, key_object, **extra)
        rec = with_id({**record("KEY_LIFECYCLE", target=None, actor=self.human(),
                                fields={"action": "REGISTER", "key": other}), "actor_class": "AGENT"})
        with self.assertRaises(EntryInvalid):  # m36
            self.admission.admit_lifecycle(rec, sshsig(self.private, self.admission.lifecycle_message(rec)), self.baseline)
        listed = record("KEY_LIFECYCLE", target=None, actor=self.human(), fields={"action": ["REGISTER"], "key": other})
        with self.assertRaises(EntryInvalid):  # a list-valued action
            self.admission.admit_lifecycle(listed, sshsig(self.private, self.admission.lifecycle_message(listed)),
                                           self.baseline)

    def test_m23_a_compromise_without_a_position_starts_at_its_own_entry(self) -> None:
        before = self.issue()
        self.lifecycle("COMPROMISED", self.issuer.trust_root())
        self.assertEqual(len(self.admit(self.signed(before, [self.bind(finding(), before)])).admitted), 1)

    def test_m24_m37_the_readers_check_ids_and_retire_by_id(self) -> None:
        from ssds.derivation import trust_roots
        from ssds.ledger.read import _keys_in_force

        forged = _Item(1, {"kind": "KEY_LIFECYCLE", "fields": {"action": "REGISTER", "key": {
            "role": "HUMAN", "id": "human:SHA256:" + "A" * 43, "public_key": self.public}}})
        self.assertNotIn("human:SHA256:" + "A" * 43, trust_roots([forged]).humans)
        key = {"role": "ADMISSION", "id": "ed25519:" + "2" * 64, "public_key": "3" * 64}
        host = [_Host(0, {"kind": "KEY_LIFECYCLE", "fields": {"action": "REGISTER", "key": key}}),
                _Host(1, {"kind": "KEY_LIFECYCLE", "fields": {"action": "RETIRE", "key": key}})]
        self.assertEqual(_keys_in_force(host)[0], {})

    # -- N3: the home ----------------------------------------------------------------------------------------

    def test_m26_m28_the_journal_writes_through_no_other_name_and_reads_only_a_regular_file(self) -> None:
        import os

        from ssds.dispatcher.journal import Journal
        from ssds.ledger.qualification import Home, HomeRefused

        journal = Journal(self.home, "demo")
        journal.decided("sha256:" + "0" * 64)
        os.link(journal.path, self.root / "alias")
        with self.assertRaises(HomeRefused):  # m26
            journal.decided("sha256:" + "1" * 64)
        other = Journal(Home(self.root / "dir-home"), "demo")
        other.path.mkdir(parents=True, mode=0o700)
        os.chmod(other.path, 0o700)  # private: only its kind refuses it
        with self.assertRaises(HomeRefused):  # m28
            other.entries()

    def test_m29_m46_a_link_after_the_name_check_is_never_followed(self) -> None:
        import os
        from unittest import mock

        from ssds.dispatcher.home import DispatcherHome
        from ssds.dispatcher.journal import Journal
        from ssds.ledger.qualification import Home, HomeRefused

        journal = Journal(Home(self.root / "race-home"), "demo")
        decoy = self.root / "race-home" / "state" / "decoy"
        decoy.mkdir(parents=True)
        os.symlink(decoy, journal.path.parent)
        with self.assertRaises(HomeRefused):  # m46: the read walk refuses the directory link
            journal.entries()
        os.unlink(journal.path.parent)
        journal.path.parent.mkdir()
        (decoy / "target").write_bytes(b"")
        os.chmod(decoy / "target", 0o600)  # private and single-named: only the no-follow open refuses it
        os.symlink(decoy / "target", journal.path)
        with mock.patch.object(DispatcherHome, "path", lambda self, parts: None):  # the link lands after the check
            with self.assertRaises(HomeRefused):  # m29: the final open refuses it
                journal.decided("sha256:" + "3" * 64)
        self.assertEqual((decoy / "target").read_bytes(), b"")

    def test_m31_concurrent_first_use_reads_the_winning_key(self) -> None:
        from unittest import mock

        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, PrivateFormat

        from ssds.dispatcher.home import DispatcherHome
        from ssds.dispatcher.issue import Issuer
        from ssds.ledger.qualification import Home

        winner = Ed25519PrivateKey.generate().private_bytes(Encoding.Raw, PrivateFormat.Raw, NoEncryption())
        original = DispatcherHome.create_private

        def raced(home, parts, data):
            original(home, parts, winner)  # another process creates the key first
            return original(home, parts, data)

        with mock.patch.object(DispatcherHome, "create_private", raced):
            issuer = Issuer(Home(self.root / "race-key"), "demo")
        self.assertEqual(issuer.public_hex, Ed25519PrivateKey.from_private_bytes(winner).public_key().public_bytes(
            Encoding.Raw, __import__("cryptography.hazmat.primitives.serialization", fromlist=["PublicFormat"])
            .PublicFormat.Raw).hex())

    def test_m32_outstanding_lists_only_that_keys_envelopes(self) -> None:
        from ssds.dispatcher.journal import Journal

        journal = Journal(self.home, "demo")
        mine, theirs = self.issue(), self.issue(issuer=self.issuer_at("someone-else"))
        journal.issued(mine.envelope["task_id"], mine.binding())
        journal.issued(theirs.envelope["task_id"], theirs.binding())
        self.assertEqual(len(journal.outstanding(self.issuer.key_id, finished_tasks=[])), 1)

    def test_m35_keys_dispatcher_is_in_the_checked_operator_tree(self) -> None:
        import os

        from ssds.dispatcher.issue import Issuer
        from ssds.ledger.qualification import Home, HomeRefused

        home = self.root / "stray-home"
        (home / "keys" / "dispatcher").mkdir(parents=True)
        os.symlink(self.root, home / "keys" / "dispatcher" / "stray")
        with self.assertRaises(HomeRefused):
            Issuer(Home(home), "demo")


class StepThreeThirdCheck(RequestFixture):
    """The narrow re-check of 496311ee (R1): the append lock, and the m43 and m48 cases that are not equivalent."""

    def test_r1_concurrent_appends_lose_no_entry(self) -> None:
        import multiprocessing

        from ssds.dispatcher.journal import Journal
        from ssds.ledger.qualification import Home

        root = self.root / "concurrent-home"
        Journal(Home(root), "demo").decided("sha256:" + "f" * 64)
        context = multiprocessing.get_context("fork")
        writers = [context.Process(target=_append_many, args=(str(root), w, 60)) for w in range(6)]
        for process in writers:
            process.start()
        for process in writers:
            process.join(120)
        self.assertEqual([p.exitcode for p in writers], [0] * 6)
        entries = Journal(Home(root), "demo").entries()
        self.assertEqual((len(entries), len({e["request_id"] for e in entries})), (361, 361))

    def test_r1_m48_an_identical_compromise_of_a_former_human_key_is_admitted_once(self) -> None:
        from ssds.admission.engine import EntryInvalid
        from ssds.ledger.read import human_key_id

        from ._fixtures import human_key

        _, line = human_key(self.root, "second")
        second = {"role": "HUMAN", "id": human_key_id(line), "public_key": line}
        self.lifecycle("REGISTER", second)
        compromise = record("KEY_LIFECYCLE", target=None, actor=self.human(),
                            fields={"action": "COMPROMISED", "key": second})
        self.admission.admit_lifecycle(compromise, sshsig(self.private, self.admission.lifecycle_message(compromise)),
                                       self.baseline)
        with self.assertRaises(EntryInvalid):  # the state rules pass it: only the already-admitted rule refuses it
            self.admission.admit_lifecycle(compromise, sshsig(self.private, self.admission.lifecycle_message(compromise)),
                                           self.baseline)

    def test_r1_m43_a_retirement_names_the_key_line_in_force_exactly(self) -> None:
        from ssds.admission.engine import EntryInvalid
        from ssds.ledger.read import human_key_id

        from ._fixtures import human_key

        _, line = human_key(self.root, "second")
        self.lifecycle("REGISTER", {"role": "HUMAN", "id": human_key_id(line), "public_key": line})
        renamed = " ".join(line.split()[:2] + ["another-comment"])
        self.assertEqual(human_key_id(renamed), human_key_id(line))
        with self.assertRaises(EntryInvalid):
            self.lifecycle("RETIRE", {"role": "HUMAN", "id": human_key_id(line), "public_key": renamed})

    def test_journal_lines_are_non_empty_objects_and_a_fifo_never_blocks(self) -> None:
        import os
        import signal

        from ssds.dispatcher.journal import Journal, JournalCorrupt
        from ssds.ledger.qualification import Home, HomeRefused

        journal = Journal(self.home, "demo")
        with self.assertRaises(ValueError):
            journal.home.append_line(journal.parts, b"\n")
        journal.decided("sha256:" + "0" * 64)
        with open(journal.path, "ab") as handle:
            handle.write(b"[1, 2]\n")
        with self.assertRaises(JournalCorrupt):  # JSON, but not an entry
            journal.entries()
        fifo = Journal(Home(self.root / "fifo-home"), "demo")
        fifo.path.parent.mkdir(parents=True, mode=0o700)
        os.mkfifo(fifo.path, 0o600)
        previous = signal.signal(signal.SIGALRM, _blocked)  # not an OSError, which the home would turn into a refusal
        signal.alarm(10)
        try:
            with self.assertRaises(HomeRefused):
                fifo.entries()
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, previous)


class _Blocked(Exception):
    pass


def _blocked(*_) -> None:
    raise _Blocked("blocked on a FIFO")


def _append_many(root: str, writer: int, count: int) -> None:
    from pathlib import Path

    from ssds.dispatcher.journal import Journal
    from ssds.ledger.qualification import Home

    journal = Journal(Home(Path(root)), "demo")
    for n in range(count):
        journal.decided(f"sha256:{writer:032x}{n:032x}")


class _Host:
    """A stored entry as the host-key reader of ``ledger.read`` reads it."""

    def __init__(self, position: int, lifecycle) -> None:
        self.position, self.lifecycle = position, lifecycle


if __name__ == "__main__":
    unittest.main()
