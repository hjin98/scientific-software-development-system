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
from ._scenario import HUMAN, HUMAN_B, OWNER, Scenario, adjudication, agent, challenge, judgment
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
        self.assertEqual(dict(decision.refused).get(framed["id"]), ("SCHEMA_UNSUPPORTED",), "frame records are 4c's")
        adjudicating = self.issue()
        challenged = self.bind(finding(materiality="MATERIAL"), adjudicating)
        self.admit(self.signed(adjudicating, [challenged]))
        ruling = self.bind(record("ADJUDICATION", target={"record": challenged["id"]}, outcome="UPHELD"), adjudicating)
        self.assertEqual(dict(self.admit(self.signed(adjudicating, [ruling])).refused).get(ruling["id"]),
                         ("SCHEMA_UNSUPPORTED",), "adjudication eligibility is step 4b-ii's")
        candidate = self.issue()
        rec = self.bind(finding(), candidate)
        with_candidate = self.admit(self.signed(candidate, [rec], candidates=["0" * 40]))
        self.assertIn("SCHEMA_UNSUPPORTED", with_candidate.reasons)
        self.assertEqual(with_candidate.admitted, (), "a content request is step 4c's: nothing is salvaged")


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
                scenario.admit(rec)
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

    def test_a_lineage_covering_the_closure_with_more_is_admitted(self) -> None:
        issued = self.issue()
        wider = self.bind(finding(), issued)
        wider = with_id({**wider, "binding": {**wider["binding"],
                                              "lineage": [issued.attestation["session"], "session:more"]}})
        self.assertEqual(self.admit(self.signed(issued, [wider])).admitted, (wider["id"],),
                         "more sessions can only make it less independent")

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
        content = self.admit(self.signed(issued, [report], candidates=["0" * 40]))
        self.assertEqual((content.admitted, dict(content.refused).get(report["id"])), ((), ("SCHEMA_UNSUPPORTED",)))

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
        for rec in (earlier, removed):
            self.assertIn(refused.get(rec["id"]), (("SCHEMA_UNSUPPORTED",), ("REF_REVISION",)))
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        t = sc.triple("doc")
        stale = judgment("ACCEPTANCE", {**t, "scope_id": "sha256:" + "5" * 64}, "PASS", actor=HUMAN)
        sc.admit(stale)
        self.assertEqual(_acceptance_target(stale, sc.derive()), {"SCHEMA_UNSUPPORTED"})
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
        sc.admit(again)
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
