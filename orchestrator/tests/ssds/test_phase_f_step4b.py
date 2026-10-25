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

    def test_an_unknown_lineage_is_empty(self) -> None:
        issued = self.issue("MANUAL")
        claimed = self.bind(finding(), issued)
        claimed = with_id({**claimed, "binding": {**claimed["binding"], "lineage": ["session:mine"]}})
        self.assertEqual(dict(self.admit(self.signed(issued, [claimed])).refused)[claimed["id"]], ("AUTH_ENVELOPE",))


if __name__ == "__main__":
    unittest.main()
