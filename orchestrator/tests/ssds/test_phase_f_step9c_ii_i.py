"""Phase F step 9c-ii-i: the realization reader and §17.4's admissibility (catalogue §6.2, §6.3, §17.2, §17.4,
§17.5, §25.2; plan §3.6, readings F88-F90; plan check of 4432948d).

A realization is admissible for an obligation when its specification and claim give the obligation, every fixed
attribute of the instantiated revision is recorded with that value, it is complete, and a runner the policy at its
admission designated for the declaration's class ran it under a runner key then in force. A passing assessment needs
all of it and its key never compromised by its admission; a failing one keeps counting under that compromise, since
failing evidence is never dropped. A class that does not observe outside reads, or a missing class attribute, leaves
the realization unpinnable. Expected values are from §6.2, §17.4 and §17.5 (no Stage S case covers them; note 6).
"""

from __future__ import annotations

import unittest

from ssds.derivation.realization import read

from ._fixtures import RUNNER_KEY, RUNNER_ROOT, record
from ._scenario import HUMAN_B, content, designated, judgment, on_record, store
from .test_assessment import OBL
from .test_phase_f_step9b_ii import DECLARATIVE, Declared

FIXED = DECLARATIVE.replace('runner = "ci"', 'runner = "ci"\nfixed = { regime = "re<2000" }')


class Fixture(Declared):
    def realization(self, outcome_record="COMPLETE", outcome=None, *, actor_key=RUNNER_KEY, attributes=(),
                    execution=None, **extra):
        view = self.sc.view(self.trees["T0"])
        basis = {**designated({"tree": self.trees["T0"], "units": [], "reads": [], "pins": [], "unpinnable": False,
                               "attributes": [list(a) for a in attributes], "bounded_by": "UNBOUNDED",
                               "context": {"system": "ssds-rules/1", "ignore": [],
                                           "analyzers": ["ssds.analyzer.python/1"]}}), **(execution or {})}
        fields = {"execution": basis, "configuration": {}}
        if outcome_record == "COMPLETE":
            fields["evaluated"] = store(self.sc, outcome or {"x": 2, "y": "0.0"})
        else:
            fields["execution"] = {**basis, "incomplete": "CRASHED"}
        real = judgment("REALIZATION", {"spec": {"unit": "spec", "rev": view.rev("spec")},
                                        "claim": [{"unit": "code", "rev": view.rev("code")}]}, outcome_record,
                        actor=f"machinery:dispatcher@{actor_key}", actor_class="MACHINERY", fields=fields)
        from ssds.ledger.read import with_id

        self.attempts = getattr(self, "attempts", 0) + 1
        real = with_id({**real, **extra, "provenance": {"attempt": self.attempts}})
        self.sc.admit(real)
        return real

    def both(self, real):
        return self.assess(real, "PASS", failing=()), self.assess(real, "FAIL")

    def admissible(self, *assessments):
        a = self.assessments()
        return tuple(a.admissible(x["id"], OBL) for x in assessments)


class Admissibility(unittest.TestCase):
    def test_a_designated_complete_realization_is_admissible_on_both_sides(self) -> None:
        r = Fixture(DECLARATIVE)
        self.assertEqual(r.admissible(*r.both(r.realization())), (True, True))

    def test_a_fixed_attribute_mismatch_enters_neither_side(self) -> None:
        r = Fixture(FIXED)
        self.assertEqual(r.admissible(*r.both(r.realization(attributes=[("regime", "re<2000")]))), (True, True))
        self.assertEqual(r.admissible(*r.both(r.realization(attributes=[("regime", "re>9000")]))), (False, False))
        self.assertEqual(r.admissible(*r.both(r.realization())), (False, False), "not recorded")

    def test_an_incomplete_realization_enters_no_assessment(self) -> None:
        r = Fixture(DECLARATIVE)
        self.assertEqual(r.admissible(*r.both(r.realization("INCOMPLETE"))), (False, False))

    def test_a_misfiled_obligation_or_reading(self) -> None:
        r = Fixture(DECLARATIVE)
        real = r.realization()
        view = r.sc.view(r.trees["T0"])
        other = judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": "evidence:" + "0" * 64},
                         "PASS", actor=HUMAN_B, basis=[on_record(real["id"]), content("spec", view.rev("spec"))],
                         fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": view.rev("spec")}})
        r.sc.admit(other)
        self.assertFalse(r.assessments().admissible(other["id"], "evidence:" + "0" * 64))

    def test_a_reading_of_another_specification(self) -> None:
        r = Fixture(DECLARATIVE)
        real = r.realization()
        view = r.sc.view(r.trees["T0"])
        misread = judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": OBL}, "PASS",
                           actor=HUMAN_B, basis=[on_record(real["id"]), content("code", view.rev("code"))],
                           fields={"mode": "ORDINARY", "reading": {"unit": "code", "rev": view.rev("code")}})
        r.sc.admit(misread)
        self.assertFalse(r.assessments().admissible(misread["id"], OBL), "the reading is not the specification's")

    def test_an_undesignated_key_or_class_facts(self) -> None:
        r = Fixture(DECLARATIVE)
        self.assertEqual(r.admissible(*r.both(r.realization(actor_key="ed25519:stranger",
                                                             execution={"runner": {"class": "ci",
                                                                                   "key": "ed25519:stranger"}}))),
                         (False, False))
        self.assertEqual(r.admissible(*r.both(r.realization(execution={"observes_outside_reads": False}))),
                         (False, False), "recorded class facts other than the policy's")
        self.assertEqual(r.admissible(*r.both(r.realization(execution={"runner": {"class": "other",
                                                                                  "key": RUNNER_KEY}}))),
                         (False, False), "another class than the declaration's")

    def test_a_compromised_key_drops_passing_never_failing(self) -> None:
        r = Fixture(DECLARATIVE)
        real = r.realization()
        early = r.both(real)
        at = r.sc.derive().s.position_of(real["id"])
        r.sc.lifecycle(record("KEY_LIFECYCLE", target=None, fields={
            "action": "COMPROMISED", "key": {**RUNNER_ROOT, "role": "RUNNER"}, "from_position": at}))
        self.assertEqual(r.admissible(*early), (False, True), "admitted at or after the compromise: failing counts")

    def test_a_retired_keys_earlier_observation_stays_trusted(self) -> None:
        r = Fixture(DECLARATIVE)
        early = r.both(r.realization())
        r.sc.lifecycle(record("KEY_LIFECYCLE", target=None, fields={
            "action": "RETIRE", "key": {**RUNNER_ROOT, "role": "RUNNER"}}))
        self.assertEqual(r.admissible(*early), (True, True))

    def test_an_agent_reported_realization_is_never_evidence(self) -> None:
        r = Fixture(DECLARATIVE)
        real = r.realization(actor_class="AGENT")
        self.assertEqual(r.admissible(*r.both(real)), (False, False))


def adopt(sc, policy_text: str) -> None:
    """A ruleset adoption putting ``policy_text`` in force (§28)."""

    import hashlib

    data = policy_text.encode()
    digest = "sha256:" + hashlib.sha256(data).hexdigest()
    sc.objects.setdefault(sc.position, {})[digest] = data
    sc.lifecycle(record("RULESET_ADOPTION", target=None, fields={
        "system": "ssds-rules/1", "policy": digest, "analyzers": ["ssds.analyzer.python/1"]}))


class Standing(unittest.TestCase):
    """Review of d481277f, B1: a permissive use needs a trusted, designated observation (F90)."""

    def genuine_fix(self):
        from .test_assessment import BAD as RUNS_BAD, GOOD as RUNS_GOOD, Runs

        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(t0, RUNS_BAD))
        return r, t0, t1, failing, RUNS_BAD, RUNS_GOOD

    def test_the_control_goes_stale(self) -> None:
        r, t0, t1, failing, bad, good = self.genuine_fix()
        r.run(t0, bad)
        r.run(t1, good)
        self.assertTrue(r.stale(failing, "T1"))

    def test_compromised_observations_never_make_a_failure_stale(self) -> None:
        r, t0, t1, failing, bad, good = self.genuine_fix()
        at = r.sc.derive().s.position_of(failing["target"]["realization"]) + 1
        r.run(t0, bad)
        r.run(t1, good)
        # declared afterwards, from an earlier position: the observations already admitted become untrusted
        r.sc.lifecycle(record("KEY_LIFECYCLE", target=None, fields={
            "action": "COMPROMISED", "key": {**RUNNER_ROOT, "role": "RUNNER"}, "from_position": at}))
        self.assertFalse(r.stale(failing, "T1"), "untrusted from the named position (§25.2)")

    def test_an_undesignated_runners_observations_never_make_it_stale(self) -> None:
        from .test_assessment import POLICY as RUNS_POLICY

        r, t0, t1, failing, bad, good = self.genuine_fix()
        adopt(r.sc, RUNS_POLICY.split("[runners.ci]")[0])  # the class is no longer designated
        r.run(t0, bad)
        r.run(t1, good)
        self.assertFalse(r.stale(failing, "T1"))
        d = r.sc.derive()
        self.assertTrue(d.a.admissible(failing["id"], OBL), "an earlier designation is not withdrawn by a later "
                                                               "policy (review note 2)")

    def test_a_later_designation_admits_no_earlier_evidence(self) -> None:
        from .test_assessment import POLICY as RUNS_POLICY

        r = Fixture(DECLARATIVE)
        r.sc = type(r.sc)(r.sc.manifest, r.files, policy=RUNS_POLICY.split("[runners.ci]")[0])
        r.trees = {"T0": r.sc.head}
        passing, failing = r.both(r.realization())
        self.assertEqual(r.admissible(passing, failing), (False, False))
        adopt(r.sc, RUNS_POLICY)
        self.assertEqual(r.admissible(passing, failing), (False, False), "decided at realization, by value (§6.3)")


class Reader(unittest.TestCase):
    def test_the_closed_shape(self) -> None:
        r = Fixture(DECLARATIVE)
        good = read("x", r.realization())
        self.assertTrue(good.well_formed, good.problems)
        for name, execution in (("unknown member", {"extra": 1}), ("runner shape", {"runner": {"class": "ci"}}),
                                ("start", {"start": -1})):
            with self.subTest(case=name):
                self.assertFalse(read("x", r.realization(execution=execution)).well_formed)
        self.assertFalse(read("x", r.realization(actor_key="ed25519:other")).well_formed, "the actor's key")

    def test_a_basis_outside_its_types_is_never_indexed(self) -> None:
        """Step 9d-i (F96): currency reads F and ``on⁻`` links adversely, neither indexing the malformed basis."""

        from ssds.derivation import F

        r = Fixture(DECLARATIVE)
        real = r.realization(execution={"units": [{"unit": "code"}]})
        self.assertFalse(read(real["id"], real).well_formed)
        d = r.sc.derive()
        self.assertEqual(d.current(real["id"]), F)
        self.assertTrue(d.a.on_minus(real["id"], d.a.tree_of(real["id"])))

    def test_a_class_that_does_not_observe_leaves_it_unpinnable(self) -> None:
        r = Fixture(DECLARATIVE)
        observed = r.realization()
        blind = r.realization(execution={"observes_outside_reads": False})
        lacking = r.realization(execution={"class_attributes": ["python"]})
        a = r.assessments()
        self.assertEqual([a.unpinnable(x["id"]) for x in (observed, blind, lacking)], [False, True, True])


class Consumers(unittest.TestCase):
    def test_an_inadmissible_failure_derives_no_disagreement(self) -> None:
        from ssds.derivation import Workflow

        bad = Fixture(DECLARATIVE)
        bad.assess(bad.realization("INCOMPLETE"), "FAIL")
        w = Workflow(bad.sc.derive())
        self.assertEqual([o for o in w.obligations if o.kind == "ADJUDICATE_DISAGREEMENT"], [])


if __name__ == "__main__":
    unittest.main()
