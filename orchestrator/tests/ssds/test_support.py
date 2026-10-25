"""S1 and the S2 support core at the real derivation owner (catalogue §5.3-§5.6; Manual §5.5-§5.6).

Expectations are stated from the Manual's text; the two Stage S §5 cases
(``provisional_propagates_by_min``, ``mutual_acceptance_forced_false`` in
``cases_s5_2_4.py``) are transcribed as named.
"""

from __future__ import annotations

import unittest

from ssds.derivation import F, P, T

from ._fixtures import lifecycle_body, record
from ._scenario import (
    attested,
    HUMAN,
    HUMAN_B,
    OWNER,
    Scenario,
    adjudication,
    agent,
    challenge,
    content,
    fresh,
    judgment,
    on_record,
    validity,
)

TWO = '''
    [[unit]]
    id = "arch"
    kind = "D3"
    scope = [{ path = "arch.md" }]
    [[unit]]
    id = "impl"
    kind = "D4"
    scope = [{ path = "impl.md" }]
'''


def accept(sc: Scenario, subject: str, actor: str = HUMAN, actor_class: str = "HUMAN", outcome: str = "PASS",
           extra=(), supersedes=(), binding=None) -> dict:
    t = sc.triple(subject)
    return judgment("ACCEPTANCE", t, outcome, actor=actor, actor_class=actor_class,
                    basis=[content(subject, t["rev"]), *extra], supersedes=supersedes, binding=binding)


class Validity(unittest.TestCase):
    def test_a_current_acceptance_on_the_exact_triple_makes_a_subject_valid(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        self.assertEqual(sc.derive().valid("arch"), F, "no acceptance, no validity")
        sc.admit(*attested(accept(sc, "arch")))
        self.assertEqual(sc.derive().valid("arch"), T)
        sc.absorb({"arch.md": "a2\n"})
        self.assertEqual(sc.derive().valid("arch"), F, "the acceptance is on the previous revision")

    def test_early_cutoff_after_an_upstream_change(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        sc.admit(*attested(accept(sc, "arch")))
        accept_impl = accept(sc, "impl", extra=[validity("arch", sc.rev("arch"))])
        consumer = judgment("REVIEW", sc.triple("impl"), "PASS", actor=HUMAN_B, basis=[validity("impl", sc.rev("impl"))])
        sc.admit(*attested(accept_impl, consumer))
        d = sc.derive()
        self.assertEqual((d.valid("impl"), d.current(consumer["id"])), (T, T))
        sc.absorb({"arch.md": "a2\n"})
        d = sc.derive()
        self.assertEqual((d.valid("arch"), d.valid("impl"), d.current(consumer["id"])), (F, F, F))
        sc.admit(*attested(accept(sc, "arch")))
        sc.admit(*attested(accept(sc, "impl", actor=HUMAN_B, extra=[validity("arch", sc.rev("arch"))])))
        d = sc.derive()
        self.assertEqual((d.valid("impl"), d.current(consumer["id"])), (T, T),
                         "a re-review that keeps impl unchanged makes its consumer current again with no further work")

    def test_a_superseded_record_never_becomes_current_again(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        first = accept(sc, "arch")
        sc.admit(*attested(first))
        second = accept(sc, "arch", supersedes=[first["id"]])
        sc.admit(*attested(second))
        d = sc.derive()
        self.assertEqual((d.current(first["id"]), d.current(second["id"]), d.valid("arch")), (F, T, T))


class ChallengeTier(unittest.TestCase):
    """S1 polarity and effects (catalogue §5.3)."""

    def setUp(self) -> None:
        self.sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        self.acc = accept(self.sc, "arch")
        self.sc.admit(*attested(self.acc))

    def test_an_open_blocking_challenge_blocks_and_a_risk_override_makes_it_provisional(self) -> None:
        c = challenge({"record": self.acc["id"]})
        self.sc.admit(*attested(c))
        self.assertEqual(self.sc.derive().valid("arch"), F)
        override = judgment("RISK_OVERRIDE", {"record": c["id"]}, None, actor=OWNER, fields={"continuation": {"subjects": ["arch"], "items": [], "kinds": []}})
        self.sc.admit(*attested(override))
        self.assertEqual(self.sc.derive().valid("arch"), P)

    def test_a_non_blocking_challenge_has_no_s1_effect(self) -> None:
        self.sc.admit(*attested(challenge({"record": self.acc["id"]}, blocking=False)))
        self.assertEqual(self.sc.derive().valid("arch"), T)

    def test_upholding_revokes_and_an_upheld_counter_challenge_relaxes(self) -> None:
        c = challenge(self.sc.triple("arch"))
        upheld = adjudication(c["id"], "UPHELD")
        self.sc.admit(*attested(c, upheld))
        d = self.sc.derive()
        self.assertEqual(d.s.status1(f"triple:arch:{self.sc.triple('arch')['scope_id']}:{self.sc.triple('arch')['rev']}"), "REVOKED")
        self.assertEqual(d.valid("arch"), F)
        counter = challenge({"record": upheld["id"]}, actor=HUMAN)
        self.sc.admit(*attested(counter))
        self.assertEqual(self.sc.derive().valid("arch"), F, "an open counter-challenge has no effect")
        self.sc.admit(*attested(adjudication(counter["id"], "UPHELD", actor=OWNER)))
        d = self.sc.derive()
        key = f"triple:arch:{self.sc.triple('arch')['scope_id']}:{self.sc.triple('arch')['rev']}"
        self.assertEqual(d.s.status1(key), "BLOCKED",
                         "the upheld counter-challenge ends the revocation; the original challenge is open again")
        self.sc.admit(*attested(adjudication(c["id"], "DISMISSED", actor=OWNER)))
        self.assertEqual(self.sc.derive().valid("arch"), T)

    def test_dismissal_and_withdrawal_end_a_block(self) -> None:
        c = challenge({"record": self.acc["id"]})
        self.sc.admit(*attested(c))
        self.sc.admit(*attested(judgment("WITHDRAWAL", {"record": c["id"]}, None, actor=HUMAN_B)))
        self.assertEqual(self.sc.derive().valid("arch"), T)


class SupportCycles(unittest.TestCase):
    """cases_s5_2_4.py: the clamp and min-propagation (Manual §5.6, R2)."""

    def test_mutual_acceptance_forced_false(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        ja = accept(sc, "arch", extra=[validity("impl", sc.rev("impl"))])
        jb = accept(sc, "impl", actor=HUMAN_B, extra=[validity("arch", sc.rev("arch"))])
        sc.admit(ja, jb)
        d = sc.derive()
        self.assertEqual({"ja": d.current(ja["id"]), "vb": d.valid("impl"), "jb": d.current(jb["id"]), "va": d.valid("arch")},
                         {"ja": F, "vb": F, "jb": F, "va": F})
        self.assertEqual(len(d.forced), 1, "one forced component, one finding")

    def test_provisional_propagates_by_min(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        acc_arch = accept(sc, "arch")
        c = challenge({"record": acc_arch["id"]})
        override = judgment("RISK_OVERRIDE", {"record": c["id"]}, None, actor=OWNER, fields={"continuation": {"subjects": ["arch", "impl"], "items": [], "kinds": []}})
        acc_impl = accept(sc, "impl", actor=HUMAN_B, extra=[validity("arch", sc.rev("arch"))])
        sc.admit(*attested(acc_arch, c, override, acc_impl))
        d = sc.derive()
        self.assertEqual((d.valid("arch"), d.valid("impl")), (P, P))


class LossBoundary(unittest.TestCase):
    def test_a_loss_boundary_withholds_permissive_records_until_held(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        sc.admit(*attested(accept(sc, "arch")))
        loss = record("LEDGER_LOSS", target=None, actor=OWNER, fields={
            "retained": {"position": 1}, "abandoned": [{"digest": "sha256:" + "a" * 64}], "report": "sha256:" + "b" * 64,
            "controls": {}})
        sc.entries.append(lifecycle_body(sc.position, loss))
        self.assertEqual(sc.derive().valid("arch"), F)
        attest = judgment("CONTINUITY_ATTESTATION", {"loss": loss["id"]}, None, actor=OWNER,
                          fields={"scope_form": "COMPLEMENT", "listed": [], "evidence": []})
        sc.admit(*attested(attest))
        self.assertEqual(sc.derive().valid("arch"), T, "a complement attestation listing nothing holds everything")


class Equivalence(unittest.TestCase):
    def test_a_current_equivalence_path_satisfies_a_covered_content_entry(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        r1 = sc.rev("arch")
        consumer = judgment("REVIEW", sc.triple("impl"), "PASS", basis=[content("arch", r1, "EDITORIAL")])
        exact = judgment("REVIEW", sc.triple("impl"), "PASS", actor=HUMAN_B, basis=[content("arch", r1)])
        sc.admit(*attested(consumer, exact))
        sc.absorb({"arch.md": "a1 \n"})
        r2 = sc.rev("arch")
        eq = judgment("EQUIVALENCE", {"unit": "arch", "from": r1, "to": r2, "class": "EDITORIAL"}, "EQUIVALENT",
                      actor=HUMAN_B, basis=[{"mode": "identity", "target": {"unit": "arch", "rev": r1}, "class": "EXACT"},
                                            {"mode": "identity", "target": {"unit": "arch", "rev": r2}, "class": "EXACT"}])
        sc.admit(*attested(eq))
        d = sc.derive()
        self.assertEqual((d.current(consumer["id"]), d.current(exact["id"])), (T, F), "EXACT is never covered")
        veto = judgment("EQUIVALENCE", {"unit": "arch", "from": r1, "to": r2, "class": "EDITORIAL"}, "NOT_EQUIVALENT",
                        actor=OWNER)
        sc.admit(*attested(veto))
        self.assertEqual(sc.derive().current(consumer["id"]), F, "a standing NOT_EQUIVALENT vetoes the hop")


POLICY_GATE = '''schema = 1
[domains.D3]
gates = ["design-gate"]
gate_holders = ["human:SHA256:alice", "human:SHA256:bob"]
'''


class GateTerm(unittest.TestCase):
    def gate(self, sc: Scenario, outcome: str, actor: str, qualification: str = "UNQUALIFIED") -> dict:
        return judgment("GATE_DECISION", {"gate": "design-gate", "subject": sc.triple("arch"), "core": "sha256:" + "c" * 64},
                        outcome, actor=actor, basis=[content("arch", sc.rev("arch"))],
                        fields={"adequacy": "ADEQUATE" if outcome == "ACCEPT" else "INADEQUATE", "qualification": qualification})

    def test_the_gate_term_is_the_minimum_over_eligible_decisions(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"}, policy=POLICY_GATE)
        sc.admit(*attested(accept(sc, "arch", actor=OWNER)))
        self.assertEqual(sc.derive().valid("arch"), F, "no eligible decision: F")
        sc.admit(*attested(self.gate(sc, "ACCEPT", HUMAN)))
        self.assertEqual(sc.derive().valid("arch"), T)
        sc.admit(*attested(self.gate(sc, "ACCEPT", HUMAN_B, "QUALIFIED")))
        self.assertEqual(sc.derive().valid("arch"), P, "a QUALIFIED decision caps the minimum at P")
        sc.admit(*attested(self.gate(sc, "REJECT", OWNER)))
        self.assertEqual(sc.derive().valid("arch"), F, "a gate REJECT vetoes every passing decision on that gate")


class TargetConditionsAndIndependence(unittest.TestCase):
    def test_a_completeness_judgment_is_current_only_while_its_membership_holds(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        wrong = judgment("COMPLETENESS", {"scope": ["arch"], "classes": ["WARRANT"], "membership": "sha256:" + "0" * 64},
                         "COMPLETE", actor=HUMAN_B)
        d0 = sc.derive()
        right = judgment("COMPLETENESS", {"scope": ["arch"], "classes": ["WARRANT"],
                                          "membership": d0.s.membership_digest(["arch"])}, "COMPLETE", actor=HUMAN_B,
                         basis=[content("arch", sc.rev("arch"))])
        sc.admit(*attested(wrong, right))
        d = sc.derive()
        self.assertEqual((d.current(wrong["id"]), d.current(right["id"])), (F, T))

    def test_no_actor_accepts_its_own_work(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        sc.integrate({"impl.md": "i2\n"}, agent("maker"), "task-1")
        own = accept(sc, "impl", actor=agent("maker"), actor_class="AGENT", binding=fresh(agent("maker"), "task-2"))
        other = accept(sc, "impl", actor=agent("checker"), actor_class="AGENT", binding=fresh(agent("checker"), "task-3"))
        sc.admit(own, other)
        d = sc.derive()
        self.assertTrue(d.j.nonind(own["id"]))
        self.assertFalse(d.j.nonind(other["id"]))
        self.assertEqual((d.current(own["id"]), d.current(other["id"]), d.valid("impl")), (F, T, T))

    def test_unknown_authorship_is_never_disjoint_from_an_agent_lineage(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        rec = accept(sc, "impl", actor=agent("checker"), actor_class="AGENT", binding=fresh(agent("checker")))
        sc.admit(rec)
        self.assertTrue(sc.derive().j.nonind(rec["id"]), "the genesis content has no admitted producer")

    def test_a_human_author_needs_a_non_authorship_attestation(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        sc.integrate({"impl.md": "i2\n"}, agent("maker"), "task-1", lineage=[HUMAN])
        rec = accept(sc, "impl", actor=HUMAN)
        sc.admit(rec)
        self.assertTrue(sc.derive().j.nonind(rec["id"]))
        rec2 = accept(sc, "impl", actor=HUMAN, extra=[on_record(rec["id"], "identity")])
        attest = judgment("NON_AUTHORSHIP_ATTESTATION", {"record": rec2["id"]}, "NOT_AUTHOR", actor=HUMAN)
        sc.admit(rec2, attest)
        self.assertFalse(sc.derive().j.nonind(rec2["id"]))

    def test_d1_d2_acceptance_needs_a_human(self) -> None:
        manifest = TWO.replace('kind = "D3"', 'kind = "D2"')
        sc = Scenario(manifest, {"arch.md": "a1\n", "impl.md": "i1\n"}, modes={"arch": {"mode": "LEGACY", "protocol": "7.2.1"}})
        t = sc.triple("arch")
        sc.admit(judgment("LEGACY_ACCEPTANCE", t, "IMPORTED", actor=OWNER, basis=[content("arch", t["rev"])],
                          fields={"legacy": ["PROTOCOL-RELEASE-STATE.yaml"]}))
        self.assertEqual(sc.derive().valid("arch"), T, "a LEGACY subject is accepted by its imported legacy acceptance")


POLICY_EVIDENCE = '''schema = 1
[domains.D3]
evidence = ["arch-check"]
'''


class EvidenceTerm(unittest.TestCase):
    def setUp(self) -> None:
        self.sc = Scenario(TWO + '''
            [[unit]]
            id = "spec"
            kind = "EVIDENCE_SPEC"
            scope = [{ path = "spec.md" }]
        ''', {"arch.md": "a1\n", "impl.md": "i1\n", "spec.md": "<!-- ssds:rel EVIDENCES arch -->\n"}, policy=POLICY_EVIDENCE)
        sc = self.sc
        self.real = judgment("REALIZATION", {"spec": {"unit": "spec", "rev": sc.rev("spec")},
                                             "claim": [{"unit": "arch", "rev": sc.rev("arch")}]}, "COMPLETE",
                             actor="machinery:dispatcher@ed25519:test", actor_class="MACHINERY",
                             basis=[content("arch", sc.rev("arch"))], fields={"execution": {}})
        sc.admit(*attested(accept(sc, "arch"), self.real))

    def assessment(self, outcome: str, actor: str = HUMAN_B) -> dict:
        return judgment("EVIDENCE_ASSESSMENT", {"realization": self.real["id"], "obligation": "arch-check"}, outcome,
                        actor=actor, basis=[on_record(self.real["id"]), content("spec", self.sc.rev("spec"))],
                        fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": self.sc.rev("spec")}})

    def test_required_evidence_holds_and_a_counting_failure_caps_validity_at_p(self) -> None:
        self.assertEqual(self.sc.derive().valid("arch"), F, "no passing assessment of the required obligation")
        self.sc.admit(*attested(self.assessment("PASS")))
        self.assertEqual(self.sc.derive().valid("arch"), T)
        failing = self.assessment("FAIL", actor=HUMAN)
        self.sc.admit(*attested(failing))
        self.assertEqual(self.sc.derive().valid("arch"), P, "a live disagreement caps validity at P, never F")
        immaterial = judgment("IMMATERIALITY", {"records": [failing["id"]]}, "IMMATERIAL", actor=OWNER,
                              basis=[on_record(failing["id"], "identity"), content("spec", self.sc.rev("spec"))])
        self.sc.admit(*attested(immaterial))
        self.assertEqual(self.sc.derive().valid("arch"), T, "an independent IMMATERIALITY disposes of it")


if __name__ == "__main__":
    unittest.main()
