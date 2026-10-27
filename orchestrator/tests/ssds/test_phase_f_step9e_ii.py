"""Phase F step 9e-ii: admitting a discriminating reading (catalogue §6.6, §6.8, §8.3 steps 1-3, §8.4; plan §3.6,
readings F106, F108, F109; Q-F24).

Step 1 refuses a reading outside its closed shape (``SCHEMA_RECORD``). Step 2 refuses a reading of a mechanical
failure, of a run outside ``conf(a⁻)``, whose failing item is not read under ``a⁻``'s reading or does not show
``a⁻``'s outcome (``REF_TARGET``), and one in a frame (``SCHEMA_UNSUPPORTED``). Step 3 refuses one that reads one
outcome both ways under one reading (``READING_CONTRADICTION``) and a non-human's where its class is R3
(``AUTH_ACTOR``): 4b-ii's moved items. Expected values are from §6.6, §6.8 and §8.3 and s1's "a reading that passes
the outcome it fails, under one reading, is refused".
"""

from __future__ import annotations

import unittest
from unittest import mock

from ssds.admission.authorize import _record_codes
from ssds.admission.checks import referenced_objects, referenced_records
from ssds.admission.evidence import assessment_references, reading_shape
from ssds.derivation.state import State
from ssds.ledger.read import with_id

from ._scenario import HUMAN_B, agent
from .test_phase_f_step9e_i import Readings


def reading_of(r: Readings, **dual) -> dict:
    r.move(), r.exec(1, old=True)
    return r.dual(0, **dual)


def step2(r: Readings, rec: dict) -> list[str]:
    d = r.sc.derive()
    return assessment_references(rec, d.s, {}, d.a)


class Steps1And2(unittest.TestCase):
    def test_a_well_formed_reading_passes(self) -> None:
        r = Readings()
        rec = reading_of(r)
        self.assertEqual((reading_shape(rec), step2(r, rec)), ([], []))

    def test_its_shape_at_step_1(self) -> None:
        r = Readings()
        rec = reading_of(r)
        fields = rec["fields"]
        bad = with_id({**rec, "fields": {**fields, "observations": fields["observations"][:1]}})
        self.assertEqual(reading_shape(bad), ["SCHEMA_RECORD"])

    def test_its_observations_and_failure_are_references(self) -> None:
        r = Readings()
        rec = reading_of(r)
        p, q = (item["observation"] for item in rec["fields"]["observations"])
        bare = {**rec, "basis": []}  # read from the observations themselves, not the basis
        self.assertLessEqual({p, q, r.failure["id"]}, referenced_records(bare))
        revised = {**rec["fields"]["observations"][1], "reason": "R", "reference": "sha256:" + "6" * 64}
        rec = {**rec, "fields": {**rec["fields"], "observations": [rec["fields"]["observations"][0], revised]}}
        self.assertIn("sha256:" + "6" * 64, referenced_objects(rec))

    def test_a_reading_of_a_mechanical_failure(self) -> None:
        """§6.6: a reading discriminates an assessor-read failure; a mechanical one reads its own verdicts."""

        from ._scenario import content, judgment, on_record
        from .test_assessment import BAD, GOOD, OBL, Runs

        r = Runs()
        failing = r.fail(r.run(r.tree("T0"), BAD))
        q = r.run(r.tree("T0"), BAD)
        r.sc.integrate({"a.py": "v = 2\n"}, agent("maker"), "task-move")
        p = r.run(r.sc.head, GOOD)
        view = r.sc.view(r.sc.head)
        now = {"unit": "spec", "rev": view.rev("spec")}
        rec = judgment("EVIDENCE_ASSESSMENT", {"realization": p["id"], "obligation": OBL}, "PASS", actor=HUMAN_B,
                       basis=[on_record(p["id"]), content("spec", now["rev"])],
                       fields={"mode": "DISCRIMINATING", "reading": now, "observations": [
                           {"observation": p["id"], "reading": now, "verdict": "PASS"},
                           {"observation": q["id"], "reading": failing["fields"]["reading"], "verdict": "FAIL",
                            "assessment": failing["id"]}]})
        d = r.sc.derive()
        self.assertEqual(reading_shape(rec), [])
        self.assertEqual(assessment_references(rec, d.s, {}, d.a), ["REF_TARGET"])

    def test_its_failing_item(self) -> None:
        r = Readings()
        r.exec(1, old=True), r.oracle(), r.move()
        rec = r.dual(0, fail_reading="now")
        self.assertEqual(step2(r, rec), ["REF_TARGET"], "not read under a⁻'s reading")
        r = Readings()
        r.exec(1, old=True), r.move()
        r.reproduction = r.exec(2)
        rec = r.dual(0)
        self.assertEqual(step2(r, rec), ["REF_TARGET"], "not a⁻'s reproduced outcome")

    def test_a_run_outside_its_configuration(self) -> None:
        r = Readings()
        rec = reading_of(r)
        stranger = with_id({**rec, "fields": {**rec["fields"], "observations": [
            rec["fields"]["observations"][0],
            {**rec["fields"]["observations"][1], "observation": r.failure["id"]}]}})  # an assessment, not a run
        self.assertEqual(step2(r, stranger), ["REF_TARGET"], "q is a run of conf(a⁻)")

    def test_a_run_of_another_configuration_with_the_failures_outcome(self) -> None:
        r = Readings()
        rec = reading_of(r)
        q = r.sc.derive().s.record(rec["fields"]["observations"][1]["observation"])
        other = with_id({**q, "fields": {**q["fields"], "configuration": {"regime": "other"}}})
        r.sc.admit(other)
        moved = with_id({**rec, "fields": {**rec["fields"], "observations": [
            rec["fields"]["observations"][0], {**rec["fields"]["observations"][1], "observation": other["id"]}]}})
        self.assertEqual(step2(r, moved), ["REF_TARGET"], "not conf(a⁻)")

    def test_its_failure_is_a_failing_assessment(self) -> None:
        """A passing assessment of the failure's own run, with its outcome, is no failure to discriminate."""

        from ._scenario import content, judgment, on_record
        from .test_assessment import OBL

        r = Readings()
        rec = reading_of(r)
        real = r.failure["target"]["realization"]
        reading = r.failure["fields"]["reading"]
        passing = judgment("EVIDENCE_ASSESSMENT", {"realization": real, "obligation": OBL}, "PASS", actor=HUMAN_B,
                           basis=[on_record(real), content("spec", reading["rev"])],
                           fields={"mode": "ORDINARY", "reading": reading})
        r.sc.admit(passing)
        aimed = with_id({**rec, "fields": {**rec["fields"], "observations": [
            rec["fields"]["observations"][0], {**rec["fields"]["observations"][1], "assessment": passing["id"]}]}})
        self.assertEqual(step2(r, aimed), ["REF_TARGET"])

    def test_its_failure_is_for_its_own_obligation(self) -> None:
        from ._scenario import content, judgment, on_record

        r = Readings()
        rec = reading_of(r)
        real = r.failure["target"]["realization"]
        reading = r.failure["fields"]["reading"]
        elsewhere = judgment("EVIDENCE_ASSESSMENT", {"realization": real, "obligation": "evidence:" + "0" * 64},
                             "FAIL", actor=HUMAN_B, basis=[on_record(real), content("spec", reading["rev"])],
                             fields={"mode": "ORDINARY", "reading": reading, "failing_outputs": ["x"]})
        r.sc.admit(elsewhere)
        aimed = with_id({**rec, "fields": {**rec["fields"], "observations": [
            rec["fields"]["observations"][0], {**rec["fields"]["observations"][1], "assessment": elsewhere["id"]}]}})
        self.assertEqual(step2(r, aimed), ["REF_TARGET"], "another obligation's failure")

    def test_a_frame_reading_is_unsupported(self) -> None:
        r = Readings()
        rec = reading_of(r)
        framed = with_id({**rec, "frame": {"transformation": "sha256:" + "7" * 64}})
        self.assertEqual(step2(r, framed), ["SCHEMA_UNSUPPORTED"], "SD-70")


class Step3(unittest.TestCase):
    """4b-ii's moved items: a reading's class and contradiction (§6.8, §8.3 step 3)."""

    def codes(self, r: Readings, rec: dict) -> set[str]:
        return _record_codes(rec, None, r.sc.derive(), None, None)

    def test_a_reading_of_one_outcome_both_ways_under_one_reading(self) -> None:
        r = Readings()
        r.exec(1, old=True)
        rec = r.dual(1)
        self.assertIn("READING_CONTRADICTION", self.codes(r, rec))

    def test_differing_readings_with_their_difference_named(self) -> None:
        r = Readings()
        r.exec(1, old=True), r.oracle(), r.move()
        rec = r.dual(1)  # the same outcome, read PASS under a revised reading: no contradiction
        self.assertTrue(rec["fields"]["observations"][1].get("reason"))
        self.assertNotIn("READING_CONTRADICTION", self.codes(r, rec))

    def test_its_class(self) -> None:
        r = Readings()
        human = reading_of(r)
        machine = with_id({**human, "actor": agent("reviewer"), "actor_class": "AGENT"})
        self.assertNotIn("AUTH_ACTOR", self.codes(r, machine), "an agent at R2")
        with mock.patch.object(State, "_authority_roots", frozenset({"code"})):  # a unit D2 only before
            self.assertIn("AUTH_ACTOR", self.codes(r, machine), "an agent at R3")
            self.assertNotIn("AUTH_ACTOR", self.codes(r, human), "a human at R3")
        self.assertEqual(human["actor"], HUMAN_B)



class QF24ThroughAdmission(unittest.TestCase):
    """Plan check of beaa9e46, note 4: two readings of s1's X2 through Admission. With Q-F24 (a)'s basis
    (``record`` on ``p``; ``identity`` on ``q`` and ``a⁻``) the reading is admitted; with the catalogue row's
    (``record`` on both realizations) it is stale, since ``q`` ran on the content before the change (F91), and a
    passing record is refused ``STALE_BASIS`` (§8.3 step 6). The claim change is an absorption at Admission, so the
    admitted reading covers nothing yet (§6.6's absorption clause): the failure still counts."""

    def test_two_readings_of_x2(self) -> None:
        from ssds.admission.request import request_message

        from ._fixtures import record, sshsig
        from .test_phase_f_step9c_ii_iv import ASSESSOR_READ
        from .test_phase_f_step9d_iii import OBL, AdmittedRuns

        class Fixture(AdmittedRuns):
            DECLARATION = ASSESSOR_READ

            def runTest(self) -> None:
                pass

        f = Fixture()
        f.setUp()
        self.addCleanup(f.doCleanups)
        t0 = f.tree("T0")
        failure = f.fail(f.realize(t0, {"x": 1}))
        q = f.realize(t0, {"x": 1})
        t1 = f.tree("T1", **{"a.py": "v = 2\n"})
        p = f.realize(t1, {"x": 0})
        s = f.derive().s
        now = p["target"]["spec"]
        code = p["target"]["claim"][0]

        def reading(q_mode: str) -> tuple[dict, dict]:
            rec = record("EVIDENCE_ASSESSMENT", target={"realization": p["id"], "obligation": OBL}, outcome="PASS",
                         actor=f.human(),
                         basis=[{"mode": "record", "target": {"record": p["id"]}, "class": "EXACT"},
                                {"mode": "content", "target": now, "class": "EXACT"},
                                {"mode": "content", "target": code, "class": "EXACT"},
                                {"mode": q_mode, "target": {"record": q["id"]}, "class": "EXACT"},
                                {"mode": "identity", "target": {"record": failure["id"]}, "class": "EXACT"}],
                         fields={"mode": "DISCRIMINATING", "reading": now, "observations": [
                             {"observation": p["id"], "reading": now, "verdict": "PASS"},
                             {"observation": q["id"], "reading": failure["fields"]["reading"], "verdict": "FAIL",
                              "assessment": failure["id"]}]})
            attestation = record("NON_AUTHORSHIP_ATTESTATION", target={"record": rec["id"]}, outcome="NOT_AUTHOR",
                                 actor=f.human())
            return rec, attestation

        def admit(*records):
            req = f.request(records)
            req["binding"] = {"human": {"actor": f.human(), "signature": sshsig(f.private, request_message(req))}}
            return f.admission.admit(req, f.head())

        malformed = reading("identity")[0]
        malformed = record("EVIDENCE_ASSESSMENT", target=malformed["target"], outcome="PASS", actor=f.human(),
                           basis=malformed["basis"], fields={**malformed["fields"],
                                                             "observations": malformed["fields"]["observations"][:1]})
        self.assertEqual(dict(admit(malformed).refused).get(malformed["id"]), ("SCHEMA_RECORD",), "step 1 (F106)")
        row = reading("record")
        self.assertIn("STALE_BASIS", set(dict(admit(*row).refused).get(row[0]["id"], ())), "the catalogue row's basis")
        manual = reading("identity")
        decision = admit(*manual)
        self.assertEqual((decision.reasons, decision.refused), ((), ()), "Q-F24 (a)'s basis")
        d = f.derive()
        self.assertEqual(d.a.adverse("code", OBL, d.base), [failure["id"]],
                         "an absorbed claim revision: the reading covers nothing yet (§6.6)")
        self.assertTrue(s.n < d.s.n)


if __name__ == "__main__":
    unittest.main()
