"""Phase F step 9d-ii: admitting ordinary assessments and their dispositions (catalogue §3.4, §6.5, §6.7, §6.8,
§17.2, §17.4; plan §3.6, readings F99-F101).

An ``ORDINARY`` assessment targets an admitted realization (``REF_TARGET``), never a ``PASS`` or ``FAIL`` of an
incomplete one, under the obligation its specification and a claim give, reading a revision of that specification;
it names failing outputs only when it fails, and only declared ones, and carries no discriminating observations
(``SCHEMA_RECORD``). An ``IMMATERIALITY`` is the owner's or the bound adjudicator's (``AUTH_ACTOR``). Disposing of
another actor's failure about a subject that is or has been D1 or D2 is a human's (§6.8, R3). A realization may be
challenged (§6.7, Manual §6.7). Expected values are from the cited text (no Stage S case covers them).
"""

from __future__ import annotations

import unittest
from unittest import mock

from ssds.admission.authorize import _record_codes
from ssds.admission.dependency import dependency_codes
from ssds.admission.evidence import assessment_references
from ssds.ledger.read import with_id

from . import test_assessment as ta
from ._scenario import HUMAN, HUMAN_B, OWNER, agent, challenge, content, judgment, on_record
from .test_assessment import BAD, GOOD, OBL, Runs


def ordinary(r, real, outcome, *, obligation=OBL, reading=None, actor=HUMAN_B, supersedes=(), **fields):
    view = r.sc.view(r.trees["T0"])
    reading = reading or {"unit": "spec", "rev": view.rev("spec")}
    if outcome == "FAIL" and "failing_outputs" not in fields:
        fields["failing_outputs"] = ["x"]
    return judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": obligation}, outcome,
                    actor=actor, actor_class="HUMAN" if actor.startswith("human:") else "AGENT",
                    basis=[on_record(real["id"]), content("spec", view.rev("spec"))], supersedes=supersedes,
                    fields={"mode": "ORDINARY", "reading": reading, **{k: v for k, v in fields.items()
                                                                        if v is not None}})


def codes(r, rec):
    return assessment_references(rec, r.sc.derive().s, {})


class Assessments(unittest.TestCase):
    def test_a_well_formed_assessment_passes(self) -> None:
        r = Runs()
        real = r.run(r.tree("T0"), BAD)
        self.assertEqual((codes(r, ordinary(r, real, "FAIL")), codes(r, ordinary(r, real, "PASS"))), ([], []))

    def test_its_target_is_an_admitted_realization(self) -> None:
        r = Runs()
        real = r.run(r.tree("T0"), BAD)
        other = with_id({**ordinary(r, real, "PASS"), "target": {"realization": "sha256:" + "1" * 64,
                                                                 "obligation": OBL}})
        self.assertEqual(codes(r, other), ["REF_TARGET"])
        failing = r.fail(real)
        aimed = with_id({**ordinary(r, real, "PASS"), "target": {"realization": failing["id"], "obligation": OBL}})
        self.assertEqual(codes(r, aimed), ["REF_TARGET"], "an assessment is no realization")

    def test_never_a_verdict_on_an_incomplete_realization(self) -> None:
        from .test_phase_f_step9b_ii import DECLARATIVE
        from .test_phase_f_step9c_ii_i import Fixture

        r = Fixture(DECLARATIVE)
        real = r.realization("INCOMPLETE")
        self.assertEqual(codes(r, ordinary(r, real, "PASS")), ["REF_TARGET"], "§17.2")

    def test_the_obligation_and_the_reading(self) -> None:
        r = Runs()
        real = r.run(r.tree("T0"), BAD)
        view = r.sc.view(r.trees["T0"])
        self.assertEqual(codes(r, ordinary(r, real, "PASS", obligation="evidence:" + "0" * 64)), ["REF_TARGET"])
        self.assertEqual(codes(r, ordinary(r, real, "PASS", reading={"unit": "code", "rev": view.rev("code")})),
                         ["REF_TARGET"], "not the realization's specification")
        self.assertEqual(codes(r, ordinary(r, real, "PASS", reading={"unit": "code", "rev": view.rev("spec")})),
                         ["REF_TARGET"], "another unit, whatever the revision")
        self.assertEqual(codes(r, ordinary(r, real, "PASS", reading={"unit": "spec", "rev": "sha256:" + "2" * 64})),
                         ["REF_TARGET"], "no revision of it")

    def test_failing_outputs_and_observations(self) -> None:
        r = Runs()
        real = r.run(r.tree("T0"), BAD)
        self.assertEqual(codes(r, ordinary(r, real, "PASS", failing_outputs=["x"])), ["SCHEMA_RECORD"],
                         "only a failure names failing outputs")
        self.assertEqual(codes(r, ordinary(r, real, "FAIL", failing_outputs=["y"])), ["SCHEMA_RECORD"],
                         "a declared output (routed from 9c-ii-iii)")
        self.assertEqual(codes(r, ordinary(r, real, "FAIL", observations=[{"o": 1}])), ["SCHEMA_RECORD"], "F80")

    def test_an_unusable_declaration_skips_the_output_check(self) -> None:
        """Derivation fails closed there (F94's residual repair)."""

        from .test_phase_f_step9b_ii import Declared

        r = Declared("oracle = \n")
        real = r.run(r.tree("T0"), {"x": 1})
        self.assertEqual(codes(r, ordinary(r, real, "FAIL", failing_outputs=["anything"])), [])


def owned(text: str) -> str:
    return text.replace("evidence = true", f'evidence = true\nowner = "{OWNER}"')


class Dispositions(unittest.TestCase):
    def failing(self, kind="D4"):
        with mock.patch.object(ta, "UNITS", ta.UNITS.replace('kind = "D4"', f'kind = "{kind}"')), \
                mock.patch.object(ta, "POLICY", owned(ta.POLICY).replace("domains.D4", f"domains.{kind}")):
            r = Runs()
        real = r.run(r.tree("T0"), BAD)
        return r, real, r.fail(real)

    def record_codes(self, r, rec, obligation=None):
        return _record_codes(rec, None, r.sc.derive(), None, obligation)

    def test_an_immateriality_is_the_owners(self) -> None:
        r, _, failing = self.failing()
        for actor, expected in ((OWNER, set()), (HUMAN, {"AUTH_ACTOR"})):
            with self.subTest(actor=actor):
                rec = judgment("IMMATERIALITY", {"records": [failing["id"]]}, "IMMATERIAL", actor=actor)
                self.assertEqual(self.record_codes(r, rec) & {"AUTH_ACTOR"}, expected)

    def test_or_the_adjudicator_bound_to_the_disagreement(self) -> None:
        from types import SimpleNamespace

        r, _, failing = self.failing()
        rec = judgment("IMMATERIALITY", {"records": [failing["id"]]}, "IMMATERIAL", actor=HUMAN)
        bound = SimpleNamespace(kind="ADJUDICATE_DISAGREEMENT", target={"record": failing["id"]})
        self.assertNotIn("AUTH_ACTOR", self.record_codes(r, rec, bound))
        elsewhere = SimpleNamespace(kind="ADJUDICATE_DISAGREEMENT", target={"record": "sha256:" + "3" * 64})
        self.assertIn("AUTH_ACTOR", self.record_codes(r, rec, elsewhere))

    def test_an_agent_disposing_of_a_d1_or_d2_failure(self) -> None:
        """§6.8: R3, by each of the three disposing kinds (plan check of b5364cc3, B1)."""

        for kind, needs in (("D2", True), ("D4", False)):
            r, real, failing = self.failing(kind)
            reviewer = agent("reviewer")
            c = challenge({"record": failing["id"]})
            on_real = challenge({"record": real["id"]})
            r.sc.admit(c, on_real)
            records = {
                "immateriality": judgment("IMMATERIALITY", {"records": [failing["id"]]}, "IMMATERIAL",
                                          actor=reviewer, actor_class="AGENT"),
                "a superseding assessment": ordinary(r, real, "PASS", actor=reviewer, supersedes=[failing["id"]],
                                                     failing_outputs=None),
                "an upheld adjudication": judgment("ADJUDICATION", {"record": c["id"]}, "UPHELD", actor=reviewer,
                                                   actor_class="AGENT"),
                "one of a challenge of its realization": judgment("ADJUDICATION", {"record": on_real["id"]},
                                                                  "UPHELD", actor=reviewer, actor_class="AGENT"),
            }
            a = r.sc.derive().a
            for name, rec in records.items():
                with self.subTest(kind=kind, record=name):
                    self.assertEqual(a.disposition_needs_human(rec), needs)
            dismissed = judgment("ADJUDICATION", {"record": c["id"]}, "DISMISSED", actor=reviewer, actor_class="AGENT")
            self.assertFalse(a.disposition_needs_human(dismissed), "a dismissal disposes of nothing")
            own = ordinary(r, real, "PASS", actor=failing["actor"], supersedes=[failing["id"]], failing_outputs=None)
            self.assertFalse(a.disposition_needs_human(own), "its own author's reassessment is no other actor's")

    def test_a_disposition_through_a_supersession_chain(self) -> None:
        """Review of e643fa07, B1 (§6.7: "directly or through a chain of supersessions"): another actor's failure
        reached through its author's own reassessment."""

        r, real, failing = self.failing("D2")
        own = ordinary(r, real, "PASS", actor=failing["actor"], supersedes=[failing["id"]], failing_outputs=None)
        r.sc.admit(own)
        later = ordinary(r, real, "PASS", actor=agent("reviewer"), supersedes=[own["id"]], failing_outputs=None)
        d = r.sc.derive()
        self.assertEqual(d.j.disposed_failures(later), [failing["id"]])
        self.assertTrue(d.a.disposition_needs_human(later))
        self.assertIn("AUTH_ACTOR", self.record_codes(r, later))

    def test_every_failure_a_chain_reaches(self) -> None:
        """Review of e643fa07, B1: the chain's nearer failure is the agent's own; the deeper one is another's."""

        r, real, failing = self.failing("D2")
        reviewer = agent("reviewer")
        own_failure = ordinary(r, real, "FAIL", actor=reviewer, supersedes=[failing["id"]])
        r.sc.admit(own_failure)
        later = ordinary(r, real, "PASS", actor=reviewer, supersedes=[own_failure["id"]], failing_outputs=None)
        d = r.sc.derive()
        self.assertEqual(d.j.disposed_failures(later), sorted([failing["id"], own_failure["id"]]))
        self.assertTrue(d.a.disposition_needs_human(later))

    def test_an_immateriality_of_ones_own_failure(self) -> None:
        """§6.8's "another actor's" qualifies supersessions and adjudications only."""

        r, real, _ = self.failing("D2")
        reviewer = agent("reviewer")
        own = ordinary(r, real, "FAIL", actor=reviewer)
        r.sc.admit(own)
        rec = judgment("IMMATERIALITY", {"records": [own["id"]]}, "IMMATERIAL", actor=reviewer, actor_class="AGENT")
        self.assertTrue(r.sc.derive().a.disposition_needs_human(rec))

    def test_through_authorize_an_agents_d2_disposition(self) -> None:
        for kind, expected in (("D2", True), ("D4", False)):
            with self.subTest(kind=kind):
                r, real, failing = self.failing(kind)
                rec = ordinary(r, real, "PASS", actor=agent("reviewer"), supersedes=[failing["id"]],
                               failing_outputs=None)
                self.assertEqual("AUTH_ACTOR" in self.record_codes(r, rec), expected)

    def test_a_unit_that_has_been_d2(self) -> None:
        """"Is, or has been": retyped D4 after the failure, and D2 only before it (re-check of 2d0ed5f0, note 3)."""

        from ssds.derivation.state import State

        r, _, failing = self.failing("D4")
        s = r.sc.derive().s
        self.assertFalse(s.ever_authority("code"))
        with mock.patch.object(State, "_authority_roots", frozenset({"code"})):
            self.assertTrue(r.sc.derive().a.disposition_needs_human(
                judgment("IMMATERIALITY", {"records": [failing["id"]]}, "IMMATERIAL", actor=agent("reviewer"),
                         actor_class="AGENT")))

    def test_ever_authority_folds_every_admitted_structure_by_lineage(self) -> None:
        r, _, _ = self.failing("D2")
        s = r.sc.derive().s
        self.assertTrue(s.ever_authority("code"))
        self.assertFalse(s.ever_authority("spec"))


class Challenges(unittest.TestCase):
    def test_a_realization_may_be_challenged(self) -> None:
        """§6.7, Manual §6.7 (reading F101)."""

        r = Runs()
        real = r.run(r.tree("T0"), GOOD)
        c = challenge({"record": real["id"]})
        r.sc.admit(c)
        self.assertNotIn("DEP_TARGET_KIND", dependency_codes(c, r.sc.derive()))


class ThroughAdmission(unittest.TestCase):
    """A human's ordinary assessment of a runner's admitted realization, accepted and, failing, salvaged (F99)."""

    def setUp(self) -> None:
        from .test_phase_f_step9d_i import Realizations

        class Fixture(Realizations):
            def runTest(self) -> None:
                pass

        self.f = Fixture()
        self.f.setUp()
        self.addCleanup(self.f.doCleanups)
        rec = self.f.realization()
        rec = with_id({**rec, "target": {**rec["target"], "claim": [rec["target"]["spec"]]}})
        self.assertEqual(self.f.codes(rec), ())
        self.real = rec

    def human(self, records):
        from ssds.admission.request import request_message

        from ._fixtures import sshsig

        f = self.f
        req = f.request(records, base_position=f.head())
        req["binding"] = {"human": {"actor": f.human(), "signature": sshsig(f.private, request_message(req))}}
        return f.admit(req)

    def assessment(self, outcome, **fields):
        from ssds.derivation.evidence import obligation_token

        from ._fixtures import record

        spec = self.real["target"]["spec"]
        return record("EVIDENCE_ASSESSMENT", target={"realization": self.real["id"],
                                                     "obligation": obligation_token(spec["unit"], spec["unit"])},
                      outcome=outcome, actor=self.f.human(), basis=[on_record(self.real["id"])],
                      fields={"mode": "ORDINARY", "reading": spec, **fields})

    def test_an_assessment_is_accepted(self) -> None:
        rec = self.assessment("PASS")
        decision = self.human([rec])
        self.assertEqual((decision.admitted, decision.reasons, decision.refused), ((rec["id"],), (), ()))

    def test_its_references_are_checked_at_step_2(self) -> None:
        rec = with_id({**self.assessment("PASS"), "target": {"realization": self.real["id"],
                                                             "obligation": "evidence:" + "0" * 64}})
        decision = self.human([rec])
        self.assertEqual(dict(decision.refused).get(rec["id"]), ("REF_TARGET",))

    def test_a_failing_one_is_salvaged(self) -> None:
        from ._fixtures import record

        failing = self.assessment("FAIL")
        bad = record("EVIDENCE_ASSESSMENT", target={"realization": "sha256:" + "4" * 64, "obligation": "o"},
                     outcome="PASS", actor=self.f.human(), fields={"mode": "ORDINARY", "reading": {}})
        decision = self.human([failing, bad])
        self.assertEqual(decision.admitted, (failing["id"],), "never lost (§8.3 step 6)")


if __name__ == "__main__":
    unittest.main()
