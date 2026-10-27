"""Phase F step 4b-i: validation step 3's authorization (Manual §8.3 step 3; catalogue §8.3 step 3, §3.5, §12.3).

Request cases run the real Admission engine on a fixture ledger whose subject ``guide`` derives an agent-held
obligation (the ``RequestFixture``). Cases whose state a records-only shadow request cannot build yet (a
``REVOKED`` triple, an ill-formed subject, a support-tier supersession) query the same decision functions over
histories the derivation scenario builder makes.
"""

from __future__ import annotations

import unittest

from ssds.admission.authenticate import lineage_closure
from ssds.admission.authorize import _acceptance_target, _supersession_authorized
from ssds.ledger.read import read_chain, with_id

from ._fixtures import record
from ._scenario import HUMAN, HUMAN_B, OWNER, Scenario, adjudication, agent, attested, challenge, judgment
from .test_admission_requests import RequestFixture, finding

DOC = '''
    [[unit]]
    id = "doc"
    kind = "D3"
    subject = true
    scope = [{ path = "doc.md" }]
'''


class EnvelopeAndRole(RequestFixture):
    """The envelope names an obligation at the request's base, of the role it was issued for; the role's
    template permits each kind and outcome (§12.3)."""

    def issue_for(self, obligation: str, role: str = "REVIEWER"):
        head = len(self.entries()) - 1
        return self.issuer.issue(task_id=f"t-{obligation[:12]}-{role}", obligation_id=obligation, role=role,
                                 contract_revision=None, governs={"mode": "LEGACY", "protocol": "7.2.1"},
                                 route="HARNESS", issued_at_position=head)

    def test_an_envelope_for_no_obligation_or_the_wrong_role_authenticates_nothing(self) -> None:
        for obligation, role in (("sha256:" + "0" * 64, "REVIEWER"), (self.obligation(), "IMPLEMENTER")):
            with self.subTest(role=role):
                issued = self.issue_for(obligation, role)
                decision = self.admit(self.signed(issued, [self.bind(finding(note=role), issued)]))
                self.assertIn("AUTH_ENVELOPE", decision.reasons)
                self.assertEqual(decision.admitted, (), "nothing under an unauthorized envelope is salvaged")

    def test_the_role_template_permits_each_kind_and_outcome(self) -> None:
        issued = self.issue()
        partial = self.bind(record("TASK_RESULT", target={"task": issued.envelope["task_id"]}, outcome="PARTIAL",
                                   fields={"slots": {}}), issued)
        decided = self.bind(record("COORDINATION_DECISION", target={"records": []}, outcome="AMEND",
                                   fields={}), issued, keep_id=False)
        report = self.bind(finding(), issued)
        decision = self.admit(self.signed(issued, [partial, report]))
        refused = dict(decision.refused)
        self.assertEqual(refused[partial["id"]], ("AUTH_ROLE_KIND",), "a reviewer's result is COMPLETE or BLOCKED")
        self.assertEqual(decision.admitted, (report["id"],))
        from ssds.derivation import role_permits

        self.assertFalse(role_permits("REVIEWER", decided["kind"], decided["outcome"]))
        self.assertTrue(role_permits("PRINCIPAL", "COORDINATION_DECISION", "AMEND"))
        self.assertTrue(all(role_permits(r, "FINDING", None) and role_permits(r, "CHALLENGE", None)
                            for r in ("PRINCIPAL", "IMPLEMENTER", "REVIEWER", "INVESTIGATOR")))

    def test_sd67_task_result_outcomes_are_the_roles(self) -> None:
        issued = self.issue()
        blocked = self.bind(record("TASK_RESULT", target={"task": issued.envelope["task_id"]}, outcome="BLOCKED",
                                   fields={"slots": {}}), issued)
        incomplete = self.bind(record("TASK_RESULT", target={"task": issued.envelope["task_id"]}, outcome="INCOMPLETE",
                                      fields={"slots": {"n": 1}}), issued)
        refused = dict(self.admit(self.signed(issued, [blocked, incomplete])).refused)
        self.assertNotIn(blocked["id"], refused, "a reviewer's BLOCKED is in schema 1 and its template (SD-67)")
        self.assertEqual(refused.get(incomplete["id"]), ("AUTH_ROLE_KIND",), "INCOMPLETE waits on Stage S: no role")

    def test_the_human_floor_refuses_an_agent(self) -> None:
        issued = self.issue()
        gate = self.bind(record("HUMAN_DECISION", target={"obligation": self.obligation()}, outcome="ACKNOWLEDGE"),
                         issued)
        report = self.bind(finding(), issued)
        decision = self.admit(self.signed(issued, [gate, report]))
        refused = dict(decision.refused)
        gate_codes = refused.get(gate["id"]) or next(v for k, v in refused.items() if k != report["id"])
        self.assertIn("AUTH_ACTOR", gate_codes)

    def test_unbuilt_checks_fail_closed(self) -> None:
        state = derive_state(self)
        subject, scope, rev = state.subject_triple("guide")
        issued = self.issue()
        framed = self.bind(record("ACCEPTANCE", target={"subject": subject, "scope_id": scope, "rev": rev}, outcome="PASS",
                                  frame={"transformation": "sha256:" + "7" * 64}), issued)
        decision = self.admit(self.signed(issued, [framed]))
        self.assertEqual(dict(decision.refused).get(framed["id"]), ("REF_TRANSFORMATION",),
                         "a frame no result fixes (4c-iii)")
        adjudicating = self.issue()
        challenged = self.bind(finding(materiality="MATERIAL"), adjudicating)
        self.admit(self.signed(adjudicating, [challenged]))
        ruling = self.bind(record("ADJUDICATION", target={"record": challenged["id"]}, outcome="UPHELD"), adjudicating)
        self.assertEqual(dict(self.admit(self.signed(adjudicating, [ruling])).refused).get(ruling["id"]),
                         ("DEP_TARGET_KIND",), "an adjudication targets a challenge (§3.4; step 4d)")
        candidate = self.issue()
        rec = self.bind(finding(), candidate)
        with_candidate = self.admit(self.signed(candidate, [rec], candidates=["0" * 40]))
        self.assertIn("REF_TRANSFORMATION", with_candidate.reasons, "no admitted result submits that candidate (4c-iii)")


def derive_state(fixture):
    from ssds.derivation import derive

    return derive(read_chain(fixture.home.ledger_repository("demo"), "demo"), fixture.trees).s


class Targets(RequestFixture):
    def test_an_acceptance_of_a_part_is_refused(self) -> None:
        state = derive_state(self)
        part = "guide.intro"
        issued = self.issue()
        rec = self.bind(record("ACCEPTANCE", target={"subject": part, "scope_id": state.view.scope_id(part),
                                                     "rev": state.view.rev(part)}, outcome="PASS"), issued)
        self.assertEqual(dict(self.admit(self.signed(issued, [rec])).refused)[rec["id"]], ("AUTH_TARGET_PART",))

    def test_a_revoked_or_ill_formed_target_is_refused(self) -> None:
        from ssds.derivation import triple_key

        sc = Scenario(DOC, {"doc.md": "r0\n"})
        t = sc.triple("doc")
        c = challenge(t)
        sc.admit(c)
        sc.admit(adjudication(c["id"], "UPHELD"))
        acceptance = judgment("ACCEPTANCE", t, "PASS", actor=HUMAN)
        sc.admit(acceptance)
        d = sc.derive()
        self.assertEqual(d.s.status1(triple_key(t["subject"], t["scope_id"], t["rev"])), "REVOKED")
        self.assertEqual(_acceptance_target(acceptance, d), {"AUTH_TARGET_REVOKED"})
        broken = Scenario('''
    [[unit]]
    id = "doc"
    kind = "D3"
    subject = true
    scope = [{ file = "missing.md" }]
''', {"doc.md": "r0\n"})
        rec = judgment("ACCEPTANCE", broken.triple("doc"), "PASS", actor=HUMAN)
        broken.admit(rec)
        d = broken.derive()
        self.assertTrue(d.s.s0.absent_term("doc"))
        self.assertEqual(_acceptance_target(rec, d), {"AUTH_ILL_FORMED"})


class Supersession(RequestFixture):
    def test_a_report_is_superseded_only_by_its_raiser(self) -> None:
        issued = self.issue()
        first = self.bind(finding(materiality="MATERIAL"), issued)
        self.admit(self.signed(issued, [first]))
        own = self.bind(record("FINDING", target={"units": ["guide"]}, fields={"materiality": "ROUTINE"},
                               supersedes=[first["id"]]), issued)
        decision = self.admit(self.signed(issued, [own]))
        self.assertEqual(decision.admitted, (own["id"],), "the same task's agent raised it")
        other = self.issue()
        theirs = self.bind(record("FINDING", target={"units": ["guide"]}, fields={"materiality": "CRITICAL"},
                                  supersedes=[first["id"]]), other)
        self.assertEqual(dict(self.admit(self.signed(other, [theirs])).refused)[theirs["id"]], ("AUTH_SUPERSEDES",))

    def test_support_tier_supersession_by_kind(self) -> None:
        policy = 'schema = 1\n[domains.D3]\nowner = "%s"\n' % OWNER
        sc = Scenario(DOC, {"doc.md": "r0\n"}, policy=policy)
        t = sc.triple("doc")
        original = judgment("ACCEPTANCE", t, "FAIL", actor=HUMAN)
        sc.admit(original)
        c = challenge(t)
        sc.admit(c)
        cases = {
            "the author's reassessment": (judgment("ACCEPTANCE", t, "PASS", actor=HUMAN, supersedes=[original["id"]]), True),
            "the owner's": (judgment("ACCEPTANCE", t, "PASS", actor=OWNER, supersedes=[original["id"]]), True),
            "a peer's": (judgment("ACCEPTANCE", t, "PASS", actor=HUMAN_B, supersedes=[original["id"]]), False),
            "another kind": (judgment("REVIEW", t, "PASS", actor=HUMAN, supersedes=[original["id"]]), False),
            "a challenge": (with_id({**challenge(t, actor=HUMAN_B), "supersedes": [c["id"]]}), False),
        }
        for name, (rec, allowed) in cases.items():
            with self.subTest(name=name):
                scenario = Scenario(DOC, {"doc.md": "r0\n"}, policy=policy)
                scenario.entries = list(sc.entries)
                scenario.objects = dict(sc.objects)
                scenario.admit(*attested(rec))
                d = scenario.derive()
                self.assertEqual(_supersession_authorized(rec, rec["supersedes"][0], None, d, None, None), allowed)

    def test_an_authors_reassessment_must_be_independent(self) -> None:
        from ._scenario import agent as agent_

        sc = Scenario(DOC, {"doc.md": "r0\n"})
        sc.integrate({"doc.md": "r1\n"}, agent_("author"), "task-1", lineage=[HUMAN])  # HUMAN authored doc
        t = sc.triple("doc")
        original = judgment("ACCEPTANCE", t, "FAIL", actor=HUMAN)
        again = judgment("ACCEPTANCE", t, "PASS", actor=HUMAN, supersedes=[original["id"]])
        sc.admit(original)
        sc.admit(again)
        d = sc.derive()
        self.assertTrue(d.j.nonind(again["id"]))
        self.assertFalse(_supersession_authorized(again, original["id"], None, d, None, None))

    def test_a_coordination_decision_is_superseded_only_by_its_plans_principal(self) -> None:
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        first = judgment("COORDINATION_DECISION", {"records": []}, "AMEND", actor=HUMAN, fields={})
        sc.admit(first)
        again = judgment("COORDINATION_DECISION", {"records": []}, "AMEND", actor=HUMAN, supersedes=[first["id"]],
                         fields={})
        sc.admit(again)
        self.assertFalse(_supersession_authorized(again, first["id"], None, sc.derive(), None, None))


class Lineage(RequestFixture):
    """A bound record's lineage is the attestation closure (reading F11)."""

    def test_the_closure_follows_stored_attestations_and_stays_open_otherwise(self) -> None:
        self.assertEqual(lineage_closure("s3", ["s2"], {"s2": ["s1"], "s1": []}), ["s3", "s1", "s2"])
        self.assertEqual(lineage_closure("s3", ["s2"], {}), ["s3", "s2", "UNKNOWN"])

    def test_a_bound_lineage_must_be_the_closure(self) -> None:
        first = self.issue()
        self.admit(self.signed(first, [self.bind(finding(materiality="MATERIAL"), first)]))
        head = len(self.entries()) - 1
        inputs = [first.attestation["session"]]
        later = self.issuer.issue(task_id="t-later", obligation_id=self.obligation(), role="REVIEWER",
                                  contract_revision=None, governs={"mode": "LEGACY", "protocol": "7.2.1"},
                                  route="HARNESS", issued_at_position=head, input_sessions=inputs)
        closure = [later.attestation["session"], *inputs]
        short = self.bind(finding(), later)
        right = with_id({**short, "binding": {**short["binding"], "lineage": closure}})
        decision = self.admit(self.signed(later, [short, right]))
        self.assertEqual(decision.admitted, (right["id"],))
        self.assertEqual(dict(decision.refused)[short["id"]], ("AUTH_ENVELOPE",), "the input's session is missing")

    def test_nb2_a_lineage_is_exactly_the_closure(self) -> None:
        issued = self.issue()
        for extra in ("session:more", "UNKNOWN", "human:SHA256:" + "A" * 43):
            with self.subTest(extra=extra):
                wider = self.bind(finding(note=extra), issued)
                wider = with_id({**wider, "binding": {**wider["binding"],
                                                      "lineage": [issued.attestation["session"], extra]}})
                refused = dict(self.admit(self.signed(issued, [wider])).refused)
                self.assertEqual(refused.get(wider["id"]), ("AUTH_ENVELOPE",),
                                 "a producing record's lineage is authorship: no token beyond the closure")

    def test_n20_a_session_two_bindings_attest_differently_stays_open(self) -> None:
        import json

        from ssds.admission.authenticate import stored_attestations

        one = json.dumps({"attestation": {"session": "s1", "input_sessions": ["a"]}}).encode()
        two = json.dumps({"attestation": {"session": "s1", "input_sessions": ["b"]}}).encode()
        three = json.dumps({"attestation": {"session": "s2", "input_sessions": []}}).encode()
        objects = {"sha256:1": one, "sha256:2": two, "sha256:3": three}
        self.assertEqual(stored_attestations(objects, set(objects)), {"s2": []})
        self.assertEqual(stored_attestations(objects, {"sha256:3"}), {"s2": []}, "only named bindings are read")

    def test_an_unknown_lineage_is_empty(self) -> None:
        issued = self.issue("MANUAL")
        claimed = self.bind(finding(), issued)
        claimed = with_id({**claimed, "binding": {**claimed["binding"], "lineage": ["session:mine"]}})
        self.assertEqual(dict(self.admit(self.signed(issued, [claimed])).refused)[claimed["id"]], ("AUTH_ENVELOPE",))



class Recheck(RequestFixture):
    """The review of 8a415395: verified attestations only (B1), supersession targets by kind (B2), the current
    triple and the product-scope authority failing closed (B3, B4), never-lost records recorded when salvage is
    withheld (B5), and a case for each check the review's mutants left untested (B6)."""

    def test_b1_a_stored_object_never_supplies_an_attestation(self) -> None:
        import hashlib

        from ssds.core.api.v1 import canonical_json

        head = len(self.entries()) - 1
        reviewer = self.issuer.issue(task_id="t-r", obligation_id=self.obligation(), role="REVIEWER",
                                     contract_revision=None, governs={"mode": "LEGACY", "protocol": "7.2.1"},
                                     route="HARNESS", issued_at_position=head, input_sessions=["session:X"])
        forger = self.issue("MANUAL")
        forged = canonical_json({"attestation": {"session": "session:X", "input_sessions": []}})
        digest = "sha256:" + hashlib.sha256(forged).hexdigest()
        report = with_id({**record("FINDING", target={"units": ["guide"]}, fields={"materiality": "ROUTINE"}),
                          "refs": [{"store": "LEDGER", "digest": digest, "media_type": "application/json"}]})
        report = self.bind(report, forger)
        self.assertEqual(self.admit(self.signed(forger, [report], extra={"objects": {digest: forged.decode()}})).admitted,
                         (report["id"],))
        session = reviewer.attestation["session"]
        closed = self.bind(finding(note="closed"), reviewer)
        closed = with_id({**closed, "binding": {**closed["binding"], "lineage": [session, "session:X"]}})
        open_ = with_id({**closed, "binding": {**closed["binding"], "lineage": [session, "session:X", "UNKNOWN"]},
                         "provenance": {"note": "open"}})
        decision = self.admit(self.signed(reviewer, [closed, open_]))
        self.assertEqual(decision.admitted, (open_["id"],), "session:X's closure stays open")
        self.assertEqual(dict(decision.refused)[closed["id"]], ("AUTH_ENVELOPE",))

    def test_b5_never_lost_records_are_recorded_when_salvage_is_withheld(self) -> None:
        head = len(self.entries()) - 1
        wrong = self.issuer.issue(task_id="t-x", obligation_id=self.obligation(), role="IMPLEMENTER",
                                  contract_revision=None, governs={"mode": "LEGACY", "protocol": "7.2.1"},
                                  route="HARNESS", issued_at_position=head)
        report = self.bind(finding(), wrong)
        decision = self.admit(self.signed(wrong, [report]))
        self.assertEqual((decision.admitted, dict(decision.refused).get(report["id"])), ((), ("AUTH_ENVELOPE",)))
        issued = self.issue()
        report = self.bind(finding(materiality="MATERIAL"), issued)
        adopting = self.admit(self.signed(issued, [report], adopted_deltas=[{"key": ["guide", "kind"], "value": "D3"}],
                                          candidates=[self.baseline]))
        self.assertEqual((adopting.admitted, dict(adopting.refused).get(report["id"])), ((), ("SCHEMA_UNSUPPORTED",)),
                         "an adoption with a candidate stays unsupported (revision 15): nothing is salvaged")

    def test_e10_an_invalid_base_salvages_nothing_and_records_why(self) -> None:
        issued = self.issue()
        report = self.bind(finding(), issued)
        decision = self.admit(self.signed(issued, [report], extra={"base_position": 10 ** 6}))
        self.assertEqual((decision.admitted, dict(decision.refused).get(report["id"])), ((), ("REF_BASE",)))

    def test_b3_b4_an_earlier_revision_or_product_scope_fails_closed(self) -> None:
        state = derive_state(self)
        subject, scope, _ = state.subject_triple("guide")
        issued = self.issue()
        earlier = self.bind(record("ACCEPTANCE", target={"subject": subject, "scope_id": scope,
                                                         "rev": "sha256:" + "6" * 64}, outcome="PASS"), issued)
        removed = self.bind(record("ACCEPTANCE", target={"subject": "nowhere", "scope_id": scope,
                                                         "rev": "sha256:" + "6" * 64}, outcome="PASS"), issued)
        decision = self.admit(self.signed(issued, [earlier, removed]))
        refused = dict(decision.refused)
        self.assertIn(refused.get(earlier["id"]), (("AUTH_TARGET_NOT_CURRENT",), ("REF_REVISION",)))
        self.assertIn(refused.get(removed["id"]), (("AUTH_TARGET_NOT_EFFECTIVE",), ("REF_REVISION",)))
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        t = sc.triple("doc")
        stale = judgment("ACCEPTANCE", {**t, "scope_id": "sha256:" + "5" * 64}, "PASS", actor=HUMAN)
        gone = judgment("ACCEPTANCE", {**t, "subject": "nowhere"}, "PASS", actor=HUMAN)
        sc.admit(stale, gone)
        d = sc.derive()
        self.assertEqual((_acceptance_target(stale, d), _acceptance_target(gone, d)),
                         ({"AUTH_TARGET_NOT_CURRENT"}, {"AUTH_TARGET_NOT_EFFECTIVE"}), "SD-68's codes")
        from ssds.admission.authorize import _record_codes

        product = with_id({**record("PRODUCT_SCOPE_ACCEPTANCE", target={"item": "x", "rev": "sha256:" + "1" * 64},
                                    outcome="ACCEPTED"), "actor": HUMAN})
        self.assertEqual(_record_codes(product, None, sc.derive(), None, None), {"SCHEMA_UNSUPPORTED"})

    def test_b6_lifecycle_and_discriminating_records_fail_closed(self) -> None:
        from ssds.admission.authorize import _record_codes

        sc = Scenario(DOC, {"doc.md": "r0\n"})
        d = sc.derive()
        lifecycle = with_id({**record("MODE_TRANSITION", target=None, fields={"subject": "doc", "mode": {}}),
                             "actor": HUMAN})
        envelope = {"role": "REVIEWER"}
        self.assertEqual(_record_codes(lifecycle, None, d, None, None), {"SCHEMA_UNSUPPORTED"})
        self.assertEqual(_record_codes(lifecycle, envelope, d, None, None), {"AUTH_ROLE_KIND"})
        reading = judgment("EVIDENCE_ASSESSMENT", {"realization": "sha256:" + "1" * 64, "obligation": "e"}, "PASS",
                           fields={"mode": "DISCRIMINATING", "reading": {"unit": "doc", "rev": "sha256:" + "2" * 64}})
        self.assertEqual(_record_codes(reading, None, d, None, None), {"SCHEMA_UNSUPPORTED"})

    def test_b6_the_role_templates_are_exactly_catalogue_12_3(self) -> None:
        from ssds.derivation import ROLE_TEMPLATES

        every = {"FINDING": None, "AMENDMENT_REQUEST": None, "BLOCKER": None, "HUMAN_QUESTION": None, "CHALLENGE": None}
        expected = {
            "PRINCIPAL": {"TASK_RESULT": {"COMPLETE", "BLOCKED"}, "COORDINATION_DECISION": None,
                          "MATERIALITY_RECLASSIFICATION": None, **every},
            "IMPLEMENTER": {"TASK_RESULT": {"COMPLETE", "PARTIAL", "BLOCKED", "INFEASIBLE"}, **every},
            "REVIEWER": {"TASK_RESULT": {"COMPLETE", "BLOCKED"}, "REVIEW": None, "CONFORMANCE": None, "ACCEPTANCE": None,
                         "PLAN_ACCEPTANCE": None, "EVIDENCE_ASSESSMENT": None, "EQUIVALENCE": None, "COMPLETENESS": None,
                         "IMMATERIALITY": None, "ADJUDICATION": None, "INTAKE_DISPOSITION": None, **every},
            "INVESTIGATOR": {"TASK_RESULT": {"FOUND", "NONE_FOUND", "INCONCLUSIVE"}, "INTAKE_CLASSIFICATION": None,
                             "RECONSTRUCTION_PROPOSAL": None, **every},
        }
        actual = {role: {k: (set(v) if v is not None else None) for k, v in t.items()} for role, t in ROLE_TEMPLATES.items()}
        self.assertEqual(actual, expected)

    def test_b6_absent_term_reads_only_the_subjects_file_terms(self) -> None:
        sc = Scenario('''
    [[unit]]
    id = "doc"
    kind = "D3"
    subject = true
    scope = [{ prefix = "nowhere/" }]
    [[unit]]
    id = "other"
    kind = "D3"
    subject = true
    scope = [{ file = "missing.md" }]
''', {"docs/a.md": "a\n"})
        d = sc.derive()
        self.assertEqual((d.s.s0.absent_term("doc"), d.s.s0.absent_term("other")), (False, True))

    def test_b6_e6_a_refusal_in_one_round_reaches_the_next(self) -> None:
        theirs = self.issue()
        earlier = self.bind(finding(materiality="CRITICAL"), theirs)
        self.admit(self.signed(theirs, [earlier]))
        issued = self.issue()
        first = self.bind(record("FINDING", target={"units": ["guide"]}, fields={"materiality": "MATERIAL"},
                                 supersedes=[earlier["id"]]), issued)  # another task's report: refused in round one
        second = self.bind(record("FINDING", target={"units": ["guide"]}, fields={"materiality": "ROUTINE"},
                                  supersedes=[first["id"]]), issued)  # its own task's: authorized while first is there
        decision = self.admit(self.signed(issued, [first, second]))
        refused = dict(decision.refused)
        self.assertEqual(refused[first["id"]], ("AUTH_SUPERSEDES",))
        self.assertEqual(refused[second["id"]], ("AUTH_SUPERSEDES",), "its superseded record left in round one")
        self.assertEqual(decision.admitted, ())


class SupersessionTargets(unittest.TestCase):
    """Catalogue §5.10 (b), "Supersession target", per kind (plan review 8a41539 B2)."""

    def authorized(self, original, again):
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        sc.admit(original)
        sc.admit(*attested(again))  # an independent human presents its non-authorship attestation (§5.10 (f))
        return _supersession_authorized(again, original["id"], None, sc.derive(), None, None)

    def test_an_assessment_is_reassessed_only_under_its_own_reading(self) -> None:
        target = {"realization": "sha256:" + "1" * 64, "obligation": "obl"}
        reading = {"unit": "doc", "rev": "sha256:" + "2" * 64}
        failing = judgment("EVIDENCE_ASSESSMENT", target, "FAIL", fields={"mode": "ORDINARY", "reading": reading})
        same = judgment("EVIDENCE_ASSESSMENT", target, "PASS", supersedes=[failing["id"]],
                        fields={"mode": "ORDINARY", "reading": reading})
        other = judgment("EVIDENCE_ASSESSMENT", target, "PASS", supersedes=[failing["id"]],
                         fields={"mode": "ORDINARY", "reading": {**reading, "rev": "sha256:" + "3" * 64}})
        self.assertEqual((self.authorized(failing, same), self.authorized(failing, other)), (True, False))

    def test_a_gate_is_reassessed_on_the_same_gate_and_triple_whatever_its_core(self) -> None:
        t = Scenario(DOC, {"doc.md": "r0\n"}).triple("doc")
        fields = {"adequacy": "ADEQUATE", "qualification": "UNQUALIFIED"}
        rejected = judgment("GATE_DECISION", {"gate": "g", "subject": t, "core": "sha256:" + "8" * 64}, "REJECT",
                            fields=fields)
        accepted = judgment("GATE_DECISION", {"gate": "g", "subject": t, "core": "sha256:" + "9" * 64}, "ACCEPT",
                            supersedes=[rejected["id"]], fields=fields)
        other_gate = judgment("GATE_DECISION", {"gate": "h", "subject": t, "core": "sha256:" + "9" * 64}, "ACCEPT",
                              supersedes=[rejected["id"]], fields=fields)
        self.assertEqual((self.authorized(rejected, accepted), self.authorized(rejected, other_gate)), (True, False))

    def test_judged_scope_kinds_and_principal_decisions_fail_closed(self) -> None:
        from ssds.admission.authorize import _record_codes

        sc = Scenario(DOC, {"doc.md": "r0\n"})
        rejected = judgment("PLAN_ACCEPTANCE", {"units": ["doc"]}, "REJECTED",
                            fields={"objective": {"unit": "doc", "rev": "sha256:" + "4" * 64},
                                    "items": [{"unit": "doc", "rev": "sha256:" + "5" * 64}]})
        decision = judgment("COORDINATION_DECISION", {"records": []}, "AMEND", actor=HUMAN, fields={})
        sc.admit(rejected, decision)
        again = judgment("PLAN_ACCEPTANCE", {"units": ["doc"]}, "ACCEPTED", supersedes=[rejected["id"]],
                         fields=rejected["fields"])
        redecided = judgment("COORDINATION_DECISION", {"records": []}, "AMEND", actor=HUMAN, supersedes=[decision["id"]],
                             fields={})
        sc.admit(again, redecided)
        d = sc.derive()
        for rec in (again, redecided):
            self.assertEqual(_record_codes(rec, None, d, None, None) & {"SCHEMA_UNSUPPORTED", "AUTH_SUPERSEDES"},
                             {"SCHEMA_UNSUPPORTED"})

    def test_observation_records_are_never_superseded(self) -> None:
        realization = judgment("REALIZATION", {"spec": {"unit": "doc", "rev": "sha256:" + "1" * 64},
                                               "claim": [{"unit": "doc", "rev": "sha256:" + "1" * 64}]},
                               "COMPLETE", actor="machinery:dispatcher@ed25519:test", actor_class="MACHINERY",
                               fields={"execution": {}})
        again = judgment("REALIZATION", realization["target"], "COMPLETE", actor="machinery:dispatcher@ed25519:test",
                         actor_class="MACHINERY", fields={"execution": {}}, supersedes=[realization["id"]])
        self.assertFalse(self.authorized(realization, again))


class OneAuthorshipRule(unittest.TestCase):
    """Routing reads authorship by the rule classification reads (§5.10 (b); plan review 6e0fa9e NB-1, N3)."""

    def test_nb1_judge_selection_and_classification_read_the_same_authors(self) -> None:
        from ssds.derivation import Workflow

        from ._scenario import agent, submit

        sc = Scenario(DOC + '''
    [[unit]]
    id = "notes"
    kind = "D3"
    subject = true
    scope = [{ path = "notes.md" }]
''', {"doc.md": "r0\n", "notes.md": "n0\n"})
        x, _, _ = submit(sc, {"doc.md": "r1\n"}, agent("x"), "task-x")
        sc.integrate({"doc.md": "r1\n", "notes.md": "n1\n"}, agent("y"), "task-y", lineage=[HUMAN])
        review = judgment("REVIEW", {"transformation": x}, "PASS", actor=HUMAN)
        sc.admit(review)
        d = sc.derive()
        at_admission = d.j.judged_authors(review["id"], d.s.position_of(review["id"]))
        self.assertIn(HUMAN, at_admission)
        self.assertEqual(d.j.judged_authors(review["id"]), at_admission)
        self.assertIn(HUMAN, d.j.transformation_authors(x))

    def test_nb1_a_reviewer_dispatched_is_one_admission_would_find_independent(self) -> None:
        """Re-check d0f1044 B1: judge selection for REVIEW(X) reads the one authorship rule, so an earlier producer
        of content X restores is never chosen (SD-51)."""

        from ssds.derivation import Workflow

        from ._scenario import OWNER, agent, content
        from .test_conformance import SECONDARY, realize, submit
        from .test_lint import FILES, MANIFEST, RUNNERS, item_block, plan_text

        policy = 'schema = 1\n[domains.""]\nhumans = ["%s", "%s"]\n' % (HUMAN, HUMAN_B) + RUNNERS
        sc = Scenario(MANIFEST, {**FILES, "plans/work.md": plan_text(item_block(secondary=SECONDARY))}, policy=policy)
        objective, item = sc.rev("plan.work.objective"), sc.rev("plan.work.item")
        sc.admit(*attested(judgment("PLAN_ACCEPTANCE", {"units": ["plan.work"]}, "ACCEPTED", actor=OWNER,
                                    basis=[content("plan.work.objective", objective),
                                           content("plan.work.item", item, "PLAN_CONTROL")],
                                    fields={"objective": {"unit": "plan.work.objective", "rev": objective},
                                            "items": [{"unit": "plan.work.item", "rev": item}]})))
        sc.integrate({"src/solver.py": "def step():\n    return 2\n"}, agent("y"), "task-y", lineage=[HUMAN])
        sc.integrate({"src/solver.py": "def step():\n    return 3\n"}, agent("z"), "task-z")
        x, candidate, _ = submit(sc, {"src/solver.py": "def step():\n    return 2\n"}, task="task-x")  # restores HUMAN's
        realize(sc, candidate)
        w = Workflow(sc.derive())
        (review,) = [o for o in w.of_kind("REVIEW") if o.target.get("transformation") == x]
        self.assertIn(HUMAN, w.judged_authors(review))
        self.assertNotIn(HUMAN, w.eligible_judges(review))
        self.assertIn(HUMAN_B, w.eligible_judges(review))

    def test_n3_a_maker_reviewing_its_own_candidate_is_never_independent(self) -> None:
        from ._scenario import agent, submit

        sc = Scenario(DOC, {"doc.md": "r0\n"})
        x, _, result = submit(sc, {"doc.md": "r1\n"}, agent("x"), "task-x")
        sc.entries.pop()
        result = dict(result)
        result["binding"] = dict(result["binding"], lineage=[HUMAN])
        result.pop("id")
        sc.admit(with_id(result))
        review = judgment("REVIEW", {"transformation": x}, "PASS", actor=HUMAN)
        sc.admit(review)
        self.assertTrue(sc.derive().j.nonind(review["id"]), "the candidate's own maker, before integration")

    def test_nb3_unknown_authorship_admits_only_an_attested_human(self) -> None:
        sc = Scenario(DOC, {"doc.md": "r0\n"})  # baseline content: no admitted record produced it
        bare = judgment("ACCEPTANCE", sc.triple("doc"), "PASS", actor=HUMAN)
        attesting = judgment("ACCEPTANCE", sc.triple("doc"), "PASS", actor=HUMAN_B)
        sc.admit(bare)
        sc.admit(*attested(attesting))
        d = sc.derive()
        self.assertEqual(d.j.judged_authors(bare["id"]), frozenset({"UNKNOWN"}))
        self.assertEqual((d.j.nonind(bare["id"]), d.j.nonind(attesting["id"])), (True, False),
                         "Manual §5.10 (f): only with a NON_AUTHORSHIP_ATTESTATION")
        later = judgment("ACCEPTANCE", sc.triple("doc"), "FAIL", actor=HUMAN)
        sc.admit(later)
        sc.admit(judgment("NON_AUTHORSHIP_ATTESTATION", {"record": later["id"]}, "NOT_AUTHOR", actor=HUMAN))
        borrowed = judgment("ACCEPTANCE", sc.triple("doc"), "PASS", actor=OWNER)
        sc.admit(borrowed, judgment("NON_AUTHORSHIP_ATTESTATION", {"record": borrowed["id"]}, "NOT_AUTHOR", actor=HUMAN_B))
        d = sc.derive()
        self.assertTrue(d.j.nonind(later["id"]), "co-submitted only: a later attestation changes nothing (§5.10 (a))")
        self.assertTrue(d.j.nonind(borrowed["id"]), "the judge's own: another human's attestation is no attestation")
        from ssds.derivation import Workflow

        w = Workflow(d)
        self.assertTrue(w.routes.independent(HUMAN, frozenset({"UNKNOWN"})),
                        "a human outside the known authors stays eligible: it can present the attestation")

    def test_a14_an_ill_formed_subject_without_an_absent_term(self) -> None:
        sc = Scenario('''
    [[unit]]
    id = "theory"
    kind = "D1"
    subject = true
    scope = [{ path = "theory.md" }]
    [[unit]]
    id = "code"
    kind = "D4"
    subject = true
    scope = [{ path = "code.md" }]
''', {"theory.md": "<!-- ssds:rel DEPENDS_ON code -->\n", "code.md": "x\n"})  # a layer violation (§2.5)
        rec = judgment("ACCEPTANCE", sc.triple("theory"), "PASS", actor=HUMAN)
        sc.admit(rec)
        d = sc.derive()
        self.assertEqual((d.s.s0.well_formed("theory"), d.s.s0.absent_term("theory")), (False, False))
        self.assertEqual(_acceptance_target(rec, d), {"AUTH_ILL_FORMED"})

    def test_newly_built_supersession_targets(self) -> None:
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        transformation = "sha256:" + "7" * 64
        review = judgment("REVIEW", {"transformation": transformation}, "NO_PASS", actor=HUMAN,
                          frame={"transformation": transformation})
        again = judgment("REVIEW", {"transformation": transformation}, "PASS", actor=HUMAN, supersedes=[review["id"]],
                         frame={"transformation": transformation})
        from ssds.derivation import supersession_target

        self.assertIsNotNone(supersession_target(review))
        self.assertEqual(supersession_target(review), supersession_target(again))
        for kind, target in (("CONFORMANCE", {"transformation": transformation}),
                             ("EQUIVALENCE", {"unit": "doc", "from": "sha256:" + "1" * 64, "to": "sha256:" + "2" * 64,
                                              "class": "EDITORIAL"}),
                             ("PRODUCT_SCOPE_ACCEPTANCE", {"item": "x", "rev": "sha256:" + "3" * 64})):
            self.assertIsNotNone(supersession_target({"kind": kind, "target": target, "fields": {}, "frame": "ADMITTED"}),
                                 f"{kind}: the column's target")
        completeness = judgment("COMPLETENESS", {"scope": ["doc"], "classes": ["WARRANT"], "membership": "sha256:" + "1" * 64,
                                                 "analyzer": "ssds.analyzer.python/1"}, "INCOMPLETE")
        by_judgment = judgment("COMPLETENESS", {"scope": ["doc"], "classes": ["WARRANT"], "membership": "sha256:" + "1" * 64},
                               "COMPLETE")
        self.assertIsNotNone(supersession_target(completeness))
        self.assertEqual(supersession_target(completeness), supersession_target(by_judgment), "without the analyzer")
        plan = judgment("PLAN_ACCEPTANCE", {"units": ["doc"]}, "REJECTED",
                        fields={"objective": {"unit": "doc", "rev": "sha256:" + "4" * 64},
                                "items": [{"unit": "doc", "rev": "sha256:" + "5" * 64}]})
        self.assertIsNone(supersession_target(plan), "conditional on its basis: not built")


class AdjudicationEligibility(unittest.TestCase):
    """Step 4b-ii: an adjudication is independent of its chain's root and of a class not lower than the chain's
    (catalogue §5.10 (e), §12.4, §3.5), refused alone otherwise. Its engine path opens once challenges are
    admissible (4d); the decision functions are checked over derivation histories."""

    def chain(self, root_actor: str, serious: bool = False, policy: str | None = None):
        from ._scenario import agent as agent_, fresh

        sc = Scenario(DOC, {"doc.md": "r0\n"}, policy=policy)
        sc.integrate({"doc.md": "r1\n"}, agent_("author"), "task-1", lineage=[agent_("author")])
        t = sc.triple("doc")
        if root_actor.startswith("agent:"):
            root = judgment("REVIEW", t, "PASS", actor=root_actor, actor_class="AGENT", binding=fresh(root_actor))
        else:
            root = judgment("REVIEW", t, "PASS", actor=root_actor)
        c = with_id({**challenge({"record": root["id"]}), "fields": {**challenge({"record": root["id"]})["fields"],
                                                                     "serious": serious}})
        sc.admit(*attested(root))
        sc.admit(c)
        return sc, c

    def adjudicate(self, sc, c, actor: str, actor_class: str = "HUMAN", binding=None):
        rec = judgment("ADJUDICATION", {"record": c["id"]}, "UPHELD", actor=actor, actor_class=actor_class,
                       binding=binding)
        sc.admit(*attested(rec))
        return rec, sc.derive()

    def test_an_agent_adjudicates_an_agent_chain_and_never_a_human_or_serious_one(self) -> None:
        from ssds.admission.authorize import _adjudication_eligible

        from ._scenario import agent as agent_, fresh

        for root, serious, eligible in ((agent_("reviewer"), False, True), (HUMAN, False, False),
                                        (agent_("reviewer"), True, False)):
            with self.subTest(root=root, serious=serious):
                sc, c = self.chain(root, serious)
                rec, d = self.adjudicate(sc, c, agent_("judge"), "AGENT", fresh(agent_("judge")))
                self.assertEqual(d.j.chain_needs_human(c["id"]), not eligible)
                self.assertEqual(_adjudication_eligible(rec, d), eligible)

    def test_a_human_adjudicates_any_class_but_never_its_own_root(self) -> None:
        from ssds.admission.authorize import _adjudication_eligible

        sc, c = self.chain(HUMAN, serious=True)
        rec, d = self.adjudicate(sc, c, HUMAN_B)
        self.assertTrue(_adjudication_eligible(rec, d))
        from ._scenario import agent as agent_

        sc = Scenario(DOC, {"doc.md": "r0\n"})
        sc.integrate({"doc.md": "r1\n"}, agent_("author"), "task-1", lineage=[HUMAN])  # HUMAN authored the root content
        root = judgment("REVIEW", sc.triple("doc"), "PASS", actor=HUMAN_B)
        sc.admit(*attested(root))
        c2 = challenge({"record": root["id"]})
        sc.admit(c2)
        own = judgment("ADJUDICATION", {"record": c2["id"]}, "UPHELD", actor=HUMAN)
        sc.admit(own)
        d = sc.derive()
        self.assertTrue(d.j.nonind(own["id"]))
        self.assertFalse(_adjudication_eligible(own, d), "never independent of the authors at its chain's root")

    def test_b4_a_d1_d2_root_needs_a_human(self) -> None:
        from ._scenario import agent as agent_, fresh

        theory = '''
    [[unit]]
    id = "theory"
    kind = "D1"
    subject = true
    scope = [{ path = "theory.md" }]
'''
        sc = Scenario(theory, {"theory.md": "t0\n"})
        sc.integrate({"theory.md": "t1\n"}, agent_("author"), "task-1", lineage=[agent_("author")])
        root = judgment("REVIEW", sc.triple("theory"), "PASS", actor=agent_("reviewer"), actor_class="AGENT",
                        binding=fresh(agent_("reviewer")))
        sc.admit(root)
        c = challenge({"record": root["id"]})
        sc.admit(c)
        self.assertTrue(sc.derive().j.chain_needs_human(c["id"]), "an adjudication of a D1/D2 claim is R3 (§3.4)")

    def test_b4_residual_every_judged_unit_counts_and_an_undetermined_root_fails_closed(self) -> None:
        """Review 799d1ba B4: the root is about a D1/D2 claim when any unit it judged lies in D1 or D2, read from a
        completeness's scope, a report's units, a record target or a triple; undetermined units fail closed."""

        from ._scenario import agent as agent_, fresh

        theory = DOC + '''
    [[unit]]
    id = "theory"
    kind = "D1"
    subject = true
    scope = [{ path = "theory.md" }]
'''
        reviewer = dict(actor=agent_("reviewer"), actor_class="AGENT", binding=fresh(agent_("reviewer")))

        def completeness(scope):
            return judgment("COMPLETENESS", {"scope": scope, "classes": ["DEF"], "membership": "sha256:" + "1" * 64},
                            "COMPLETE", **reviewer)

        def report(units):
            return judgment("FINDING", {"units": units}, None, fields={"materiality": "ROUTINE"}, **reviewer)

        def reclassified(units):
            r = report(units)
            return [r, judgment("MATERIALITY_RECLASSIFICATION", {"record": r["id"]}, "ROUTINE", **reviewer)]

        cases = {"completeness of D1": ([completeness(["theory"])], True),
                 "completeness of D3": ([completeness(["doc"])], False),
                 "multi-domain completeness": ([completeness(["doc", "theory"])], True),
                 "report on D1": ([report(["theory"])], True),
                 "multi-domain report": ([report(["theory", "doc"])], True),
                 "record target on D1": (reclassified(["theory"]), True),
                 "record target on D3": (reclassified(["doc"]), False),
                 "no units": ([judgment("TASK_RESULT", {"task": "task-x"}, "COMPLETE", fields={"slots": {}},
                                        **reviewer)], True)}
        for name, (roots, r3) in cases.items():
            with self.subTest(root=name):
                sc = Scenario(theory, {"doc.md": "r0\n", "theory.md": "t0\n"})
                sc.admit(*roots)
                c = challenge({"record": roots[-1]["id"]})
                sc.admit(c)
                self.assertEqual(sc.derive().j.chain_needs_human(c["id"]), r3)
        for unit, r3 in (("theory", True), ("doc", False)):
            with self.subTest(triple=unit):
                sc = Scenario(theory, {"doc.md": "r0\n", "theory.md": "t0\n"})
                c = challenge(sc.triple(unit))
                sc.admit(c)
                self.assertEqual(sc.derive().j.chain_needs_human(c["id"]), r3, "a challenge made on a triple")
        self.assertTrue(sc.derive().j.chain_needs_human("sha256:" + "9" * 64), "no root reached: fail closed")

    def test_b4_the_union_over_everything_the_root_judged(self) -> None:
        """Re-check c5a6457 B4: an immateriality covering several failures, or a report on several records, is
        about every unit any of them judged, in any order; a realization root reads its claim (R2 for a D3 claim);
        D2 counts as D1 does; an undeclared unit fails closed."""

        from ._scenario import agent as agent_, fresh

        units = DOC + '''
    [[unit]]
    id = "spec"
    kind = "D2"
    subject = true
    scope = [{ path = "spec.md" }]
'''
        reviewer = dict(actor=agent_("reviewer"), actor_class="AGENT", binding=fresh(agent_("reviewer")))

        def failures(sc):
            out, reals = [], []
            for unit in ("doc", "spec"):
                rev = sc.rev(unit)
                real = judgment("REALIZATION", {"spec": {"unit": unit, "rev": rev}, "claim": [{"unit": unit, "rev": rev}]},
                                "COMPLETE", actor="machinery:dispatcher@ed25519:test", actor_class="MACHINERY",
                                fields={"execution": {}})
                failing = judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": "e-" + unit},
                                   "FAIL", fields={"mode": "ORDINARY", "reading": {"unit": unit, "rev": rev}},
                                   **reviewer)
                sc.admit(real, failing)
                out.append(failing["id"])
                reals.append(real["id"])
            return out, reals

        def class_of(root_of):
            sc = Scenario(units, {"doc.md": "d0\n", "spec.md": "s0\n"})
            covered, reals = failures(sc)
            root = root_of(covered, reals)
            if isinstance(root, dict):
                sc.admit(root)
                root = root["id"]
            c = challenge({"record": root})
            sc.admit(c)
            return sc.derive().j.chain_needs_human(c["id"])

        for order in ((0, 1), (1, 0)):
            with self.subTest(immateriality=order):
                self.assertTrue(class_of(lambda f, _r: judgment("IMMATERIALITY", {"records": [f[i] for i in order]},
                                                               "IMMATERIAL", **reviewer)))
            with self.subTest(report=order):
                self.assertTrue(class_of(lambda f, _r: judgment("FINDING", {"records": [f[i] for i in order]}, None,
                                                               fields={"materiality": "ROUTINE"}, **reviewer)))
        with self.subTest(root="a D3 failure alone"):
            self.assertFalse(class_of(lambda f, _r: judgment("IMMATERIALITY", {"records": [f[0]]}, "IMMATERIAL",
                                                            **reviewer)))
        with self.subTest(root="a D2 failure alone"):
            self.assertTrue(class_of(lambda f, _r: f[1]))
        with self.subTest(root="a realization of a D3 claim"):
            self.assertFalse(class_of(lambda _f, r: r[0]), "R2: an agent may adjudicate (§3.4, §12.4)")
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        self.assertTrue(sc.derive().j._about_d1_d2(["no-such-unit"]), "an undeclared unit fails closed")

    def test_b1_00fb3cb_shared_record_targets_are_walked_once(self) -> None:
        """Re-check 00fb3cb B1: reports each targeting the previous two form a DAG whose paths grow like the
        Fibonacci numbers; the units of each record are computed once, so a deep one is read in bounded time."""

        import time

        sc = Scenario(DOC, {"doc.md": "r0\n"})
        first = judgment("FINDING", {"units": ["doc"]}, None, fields={"materiality": "ROUTINE"})
        second = judgment("FINDING", {"records": [first["id"]]}, None, fields={"materiality": "ROUTINE"})
        sc.admit(first, second)
        previous, before = second["id"], first["id"]
        for depth in range(34):
            top = judgment("FINDING", {"records": [previous, before]}, None, fields={"materiality": "ROUTINE"},
                           actor=HUMAN if depth % 2 else HUMAN_B)
            sc.admit(top)
            previous, before = top["id"], previous
        d = sc.derive()
        started = time.monotonic()
        self.assertEqual(d.j.judged_units(d.s.record(previous)), ["doc"])
        self.assertLess(time.monotonic() - started, 2.0, "a walk per path takes tens of seconds at depth 34, hours at 50")
        chain = Scenario(DOC, {"doc.md": "r0\n"})
        link = judgment("FINDING", {"units": ["doc"]}, None, fields={"materiality": "ROUTINE"})
        chain.admit(link)
        for depth in range(1000):  # re-check c23f3ce: a linear chain overflowed a recursive walk at about 400
            link = judgment("FINDING", {"records": [link["id"]]}, None, fields={"materiality": "ROUTINE"},
                            actor=HUMAN if depth % 2 else HUMAN_B)
            chain.admit(link)
        d = chain.derive()
        self.assertEqual(d.j.judged_units(d.s.record(link["id"])), ["doc"])

    def test_n1_the_walk_stops_at_the_root(self) -> None:
        from ._scenario import agent as agent_, fresh

        sc = Scenario(DOC, {"doc.md": "r0\n"})
        report = judgment("FINDING", {"units": ["doc"]}, None, actor=HUMAN, fields={"materiality": "MATERIAL"})
        sc.admit(report)
        reclassified = judgment("MATERIALITY_RECLASSIFICATION", {"record": report["id"]}, "ROUTINE",
                                actor=agent_("principal"), actor_class="AGENT", binding=fresh(agent_("principal")))
        sc.admit(reclassified)
        c = challenge({"record": reclassified["id"]})
        sc.admit(c)
        self.assertFalse(sc.derive().j.chain_needs_human(c["id"]), "the human's report lies beyond the root")

    def test_n7_judge_selection_reads_the_chain_class(self) -> None:
        from ssds.derivation import Workflow

        from ._scenario import agent as agent_

        policy = 'schema = 1\n[domains.""]\nadjudicators = ["%s", "%s"]\n' % (agent_("judge"), HUMAN_B)
        for root, agent_eligible in ((HUMAN, False), (agent_("reviewer"), True)):
            with self.subTest(root=root):
                sc, c = self.chain(root, policy=policy)
                w = Workflow(sc.derive())
                (o,) = [x for x in w.obligations if x.kind == "ADJUDICATE" and x.target.get("record") == c["id"]]
                self.assertIn(HUMAN_B, w.eligible_judges(o))
                self.assertEqual(agent_("judge") in w.eligible_judges(o), agent_eligible)

    def test_an_ineligible_adjudication_is_refused_alone(self) -> None:
        from ssds.admission.authorize import authorize

        from ._scenario import agent as agent_, fresh

        sc, c = self.chain(HUMAN)
        rec, d = self.adjudicate(sc, c, agent_("judge"), "AGENT", fresh(agent_("judge")))
        result = authorize({"binding": None}, [rec], d, None)
        self.assertEqual((result.ok, result.refused, result.alone), (True, (), ((rec["id"], ("AUTH_ACTOR",)),)))


class RefusedAlone(RequestFixture):
    """Review 8d274c4 B3: a refusal alone leaves the decision to the rest of the request, through the one rule the
    fail-closed check and the decision both read. Until challenges are admissible (4d) no real adjudication reaches
    the engine's eligibility check, so a stand-in for ``authorize`` refuses one record alone."""

    def test_a_refusal_alone_is_recorded_and_decides_nothing(self) -> None:
        from unittest import mock

        from ssds.admission.authorize import Authorization

        issued = self.issue()
        kept, ineligible = self.bind(finding(), issued), self.bind(finding(materiality="MATERIAL"), issued)

        def fake(request, records, trial, base, resubmitted=None):
            present = {r["id"] for r in records}
            return Authorization(True, frozenset(), (), tuple((rid, ("AUTH_ACTOR",)) for rid in [ineligible["id"]]
                                                             if rid in present))

        with mock.patch("ssds.admission.engine.authorize", fake):
            decision = self.admit(self.signed(issued, [kept, ineligible]))
        self.assertEqual((decision.decision, decision.reasons), ("ACCEPT", ()),
                         "no request-level reason: the rest of the request is accepted (step 6c)")
        self.assertIn((ineligible["id"], ("AUTH_ACTOR",)), decision.refused)
        self.assertEqual(decision.admitted, (kept["id"],), "the rest of the request is judged without it")


class SameRequestChallenge(RequestFixture):
    def test_n3_an_adjudication_of_a_co_submitted_challenge_is_dep_target_order(self) -> None:
        from ssds.admission.request import request_message

        from ._fixtures import sshsig

        subject, scope, rev = derive_state(self).subject_triple("guide")
        c = with_id({**record("CHALLENGE", target={"subject": subject, "scope_id": scope, "rev": rev},
                              fields={"blocking": True, "serious": False, "inquiry": "EXPLORATORY",
                                      "materiality": "MATERIAL"}), "actor": self.human()})
        a = with_id({**record("ADJUDICATION", target={"record": c["id"]}, outcome="UPHELD"), "actor": self.human()})
        req = self.request([c, a], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        refused = dict(self.admit(req).refused)
        self.assertEqual(refused.get(a["id"]), ("DEP_TARGET_ORDER",),
                         "its target is not strictly earlier (§8.5; step 4d, review 8d274c4 N3)")


class Reissue(RequestFixture):
    """Step 4b-ii: a never-lost record under a retired key's unlisted envelope is refused by identity, its bytes
    retained, and REISSUE(envelope) derived until a record citing the refusal is admitted (§8.3 step 3, §10.2)."""

    def test_an_unlisted_envelopes_report_is_kept_and_reissued(self) -> None:
        from ssds.admission.request import request_message
        from ssds.derivation import Workflow

        from ._fixtures import sshsig

        unlisted = self.issue("MANUAL")
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[])
        orphan = self.bind(finding(materiality="MATERIAL"), unlisted)
        decision = self.admit(self.signed(unlisted, [orphan]))
        self.assertEqual((decision.admitted, decision.refused), ((), ((orphan["id"], ("AUTH_ENVELOPE",)),)))
        entry = self.entries()[-1]
        self.assertIn(orphan["id"], entry.objects, "its bytes, by content identity")
        self.assertIn(orphan["binding"]["envelope"], entry.objects, "and its binding")
        w = Workflow(derive_state_support(self))
        (reissue,) = [o for o in w.obligations if o.kind == "REISSUE"]
        self.assertEqual((reissue.target, reissue.params, reissue.holder),
                         ({"envelope": orphan["binding"]["envelope"]}, {"records": [orphan["id"]]}, "DISPATCHER"))
        citing = with_id({**finding(), "actor": self.human(), "provenance": {"reissue_of": orphan["id"]}})
        req = self.request([citing], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        refused = self.admit(req)
        self.assertEqual((refused.admitted, dict(refused.refused).get(citing["id"])), ((), ("SCHEMA_UNSUPPORTED",)),
                         "only step 8's Dispatcher resubmits (review 8d274c4 B2)")
        self.assertTrue([o for o in Workflow(derive_state_support(self)).obligations if o.kind == "REISSUE"],
                        "a citation alone discharges nothing")

    def test_b2_only_a_matching_resubmission_discharges_reissue(self) -> None:
        from ssds.derivation import Workflow

        unlisted = self.issue("MANUAL")
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[])
        orphan = self.bind(finding(materiality="MATERIAL"), unlisted)
        self.admit(self.signed(unlisted, [orphan]))
        chain = read_chain(self.home.ledger_repository("demo"), "demo")
        head = chain.entries[chain.readable_through]
        rebound = {**orphan["binding"], "envelope": "sha256:" + "cd" * 32}
        cases = {"matching": (with_id({**orphan, "binding": rebound, "provenance": {"reissue_of": orphan["id"]}}), False),
                 "another finding": (with_id({**orphan, "fields": {"materiality": "ROUTINE"}, "binding": rebound,
                                              "provenance": {"reissue_of": orphan["id"]}}), True),
                 "another actor": (with_id({**orphan, "actor": "agent:someone/1", "binding": rebound,
                                            "provenance": {"reissue_of": orphan["id"]}}), True),
                 "another lineage class": (with_id({**orphan, "binding": {**rebound, "lineage_class": "ATTESTED_FRESH"},
                                                    "provenance": {"reissue_of": orphan["id"]}}), True),
                 "another provenance": (with_id({**orphan, "binding": rebound,  # review of 26907956, B2
                                                 "provenance": {"reissue_of": orphan["id"], "note": "x"}}), True)}
        for name, (resubmitted, still_open) in cases.items():
            with self.subTest(name=name):
                entry = self.admission.admission_entry(head, self.baseline, "sha256:" + "0" * 64, "ACCEPT", [],
                                                       [resubmitted], [], self.baseline)
                w = Workflow(self.admission.trial(chain, entry))
                self.assertEqual(bool([o for o in w.obligations if o.kind == "REISSUE"]), still_open)

    def test_b1_the_unlisted_path_runs_every_check(self) -> None:
        unlisted = self.issue("MANUAL")
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[])
        human = self.bind(finding(), unlisted, keep_actor=True)  # the fixture's human actor, under an agent envelope
        forged = with_id({**self.bind(finding(materiality="CRITICAL"), unlisted),
                          "binding": {**self.bind(finding(), unlisted)["binding"], "envelope": "sha256:" + "ab" * 32}})
        decision = self.admit(self.signed(unlisted, [human, forged]))
        refused = dict(decision.refused)
        self.assertIn("AUTH_ACTOR", refused[human["id"]])
        self.assertIn("AUTH_ENVELOPE", refused[forged["id"]])
        entry = self.entries()[-1]
        self.assertNotIn(human["id"], entry.objects, "a record failing its own checks is not retained")
        self.assertNotIn(forged["id"], entry.objects)
        from ssds.derivation import Workflow

        self.assertFalse([o for o in Workflow(derive_state_support(self)).obligations if o.kind == "REISSUE"])

    def test_b1_an_unverified_harness_credential_stores_nothing(self) -> None:
        unlisted = self.issue()
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[])
        req = self.signed(unlisted, [self.bind(finding(), unlisted)])
        req["binding"] = {**req["binding"], "credential_signature": "00" * 64}
        decision = self.admit(req)
        self.assertEqual((decision.admitted, decision.refused), ((), ()))
        self.assertEqual(dict(self.entries()[-1].objects), {})

    def test_b1_residual_a_bad_envelope_signature_authenticates_nothing(self) -> None:
        """Review 799d1ba B1: the envelope's issue-key signature is checked on every path: in force (harness
        route, whose attestation still verifies) and a retired key's unlisted envelope."""

        import dataclasses

        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

        from ssds.admission.request import envelope_message

        forger = Ed25519PrivateKey.generate()
        for path in ("in force", "retired unlisted"):
            with self.subTest(path=path):
                self.setUp()
                issued = self.issue("HARNESS" if path == "in force" else "MANUAL")
                if path != "in force":
                    self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[])
                forged = dataclasses.replace(issued, signature=forger.sign(envelope_message(issued.envelope)).hex())
                rec = self.bind(finding(materiality="MATERIAL"), forged)
                decision = self.admit(self.signed(forged, [rec]))
                self.assertEqual((decision.admitted, decision.refused), ((), ()))
                self.assertEqual(dict(self.entries()[-1].objects), {}, "nothing stored")

    def test_b1_residual_a_record_authorization_refuses_is_not_retained_for_reissue(self) -> None:
        """Review 799d1ba B1 (E1): the unlisted path runs authorization too; a record it refuses is not kept."""

        from ssds.derivation import Workflow

        unlisted = self.issue("MANUAL")
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[])
        rec = self.bind({**finding(materiality="MATERIAL"), "provenance": {"reissue_of": "sha256:" + "ab" * 32}},
                        unlisted)
        decision = self.admit(self.signed(unlisted, [rec]))
        self.assertEqual((decision.admitted, dict(decision.refused).get(rec["id"])), ((), ("SCHEMA_UNSUPPORTED",)))
        self.assertNotIn(rec["id"], self.entries()[-1].objects)
        self.assertFalse([o for o in Workflow(derive_state_support(self)).obligations if o.kind == "REISSUE"])

    def test_n4_an_envelope_issued_after_its_keys_retirement_is_no_outstanding_one(self) -> None:
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[])
        late = self.issue("MANUAL")  # issued_at_position: the head, after the retirement
        decision = self.admit(self.signed(late, [self.bind(finding(), late)]))
        self.assertEqual((decision.admitted, decision.refused), ((), ()))

    def test_a_compromised_retired_key_keeps_nothing(self) -> None:
        unlisted = self.issue("MANUAL")
        self.lifecycle("RETIRE", self.issuer.trust_root(), outstanding=[])
        self.lifecycle("COMPROMISED", self.issuer.trust_root(), from_position=len(self.entries()))
        orphan = self.bind(finding(), unlisted)
        decision = self.admit(self.signed(unlisted, [orphan]))
        self.assertEqual((decision.admitted, decision.refused), ((), ()))
        self.assertNotIn(orphan["id"], self.entries()[-1].objects)


def derive_state_support(fixture):
    from ssds.derivation import derive

    return derive(read_chain(fixture.home.ledger_repository("demo"), "demo"), fixture.trees)


class PlanCoverage(unittest.TestCase):
    """Catalogue §11.2: an item is issuable only while a current plan acceptance covers it, so a non-independent
    plan acceptance (an unattested human over baseline content, §5.10 (f)) issues nothing (re-check d0f1044 M30)."""

    def test_only_a_current_plan_acceptance_makes_an_item_issuable(self) -> None:
        from ssds.derivation import Workflow

        from ._scenario import OWNER, content
        from .test_conformance import SECONDARY
        from .test_lint import DESIGNATED, FILES, MANIFEST, item_block, plan_text

        for attest, issuable in ((False, False), (True, True)):
            with self.subTest(attested=attest):
                sc = Scenario(MANIFEST, {**FILES, "plans/work.md": plan_text(item_block(secondary=SECONDARY))},
                              policy=DESIGNATED)
                objective, item = sc.rev("plan.work.objective"), sc.rev("plan.work.item")
                acceptance = judgment("PLAN_ACCEPTANCE", {"units": ["plan.work"]}, "ACCEPTED", actor=OWNER,
                                      basis=[content("plan.work.objective", objective),
                                             content("plan.work.item", item, "PLAN_CONTROL")],
                                      fields={"objective": {"unit": "plan.work.objective", "rev": objective},
                                              "items": [{"unit": "plan.work.item", "rev": item}]})
                sc.admit(*(attested(acceptance) if attest else [acceptance]))
                w = Workflow(sc.derive())
                self.assertEqual(w.d.j.nonind(acceptance["id"]), not attest)
                self.assertEqual(w.issuable("plan.work.item"), issuable)


class ProductionShapedLedger(unittest.TestCase):
    """On a shadow genesis as production makes it (``LEGACY``/``UNGOVERNED`` only), nothing derives an agent-held
    obligation, so every agent-bound request is ``AUTH_ENVELOPE`` and its reports are recorded as refused: the
    real shadow ledger's behaviour until a campaign (Phase F reading F8; step 10 plans for it)."""

    def test_an_agent_envelope_on_a_shadow_ledger_names_no_obligation(self) -> None:
        from ssds.admission.engine import Admission
        from ssds.admission.genesis import admit_genesis, prepare_genesis
        from ssds.dispatcher.issue import Issuer

        from ._fixtures import sshsig
        from .test_admission_genesis import GenesisFixture

        fixture = GenesisFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture._tmp.cleanup)
        prepared = prepare_genesis(fixture.spec(), fixture.home, fixture.trees)
        admit_genesis(fixture.home, "demo", sshsig(fixture.private, prepared.message))
        admission = Admission(fixture.home, "demo", fixture.trees)
        issuer = Issuer(fixture.home, "demo")
        from ssds.ledger.read import human_key_id

        register = record("KEY_LIFECYCLE", target=None, actor=human_key_id(fixture.public),
                          fields={"action": "REGISTER", "key": issuer.trust_root()})
        admission.admit_lifecycle(register, sshsig(fixture.private, admission.lifecycle_message(register)),
                                  fixture.baseline)
        head = 1
        issued = issuer.issue(task_id="t-shadow", obligation_id="sha256:" + "0" * 64, role="REVIEWER",
                              contract_revision=None, governs={"mode": "LEGACY", "protocol": "7.2.1"}, route="MANUAL",
                              issued_at_position=head)
        report = with_id({**finding(), "actor": "agent:t-shadow/1", "actor_class": "AGENT",
                          "binding": {"task": "t-shadow", "obligation": "sha256:" + "0" * 64, "role": "REVIEWER",
                                      "lineage": [], "lineage_class": "UNKNOWN",
                                      "envelope": __import__("ssds.admission.request", fromlist=["binding_digest"])
                                      .binding_digest(issued.binding())}})
        request = {"binding": None, "claims": [], "base_position": head, "base_commit": fixture.baseline,
                   "candidates": [], "adopted_deltas": [], "records": [report], "objects": {}}
        request["binding"] = issued.binding(request)
        decision = admission.admit(request, fixture.baseline)
        self.assertIn("AUTH_ENVELOPE", decision.reasons)
        self.assertEqual((decision.admitted, dict(decision.refused).get(report["id"])), ((), ("AUTH_ENVELOPE",)))

if __name__ == "__main__":
    unittest.main()
