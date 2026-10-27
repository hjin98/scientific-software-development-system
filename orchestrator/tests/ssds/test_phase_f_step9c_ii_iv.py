"""Phase F step 9c-ii-iv: the evidence obligations (catalogue §10.2, §6.8-§6.9; plan §3.6, reading F95; plan check
of 4432948d, notes 3-6).

``REALIZE(e)`` stands while a required obligation has no current, complete, admissible realization of the current
revisions; ``ASSESS`` while an admissible realization has no acting assessment for its obligation; ``RERUN`` for each
of conditions (1) and (3) a counting, unstale failure without a disposition lacks, unless (2) failed or no current
completeness judgment bounds the closure, ending on a complete observation of the configuration on that tree; and
``READING`` for an assessor-read failure observed here. None is derived in a frame (SD-70). Expected values are from
§6.8-§6.9 and §10.2 (no Stage S case covers them).
"""

from __future__ import annotations

import unittest

from ssds.derivation import Workflow

from ._scenario import HUMAN_B, content, judgment, on_record
from .test_assessment import BAD, GOOD, OBL, Runs
from .test_phase_f_step9b_ii import Declared


def kinds(r, kind: str):
    return [o for o in Workflow(r.sc.derive()).obligations if o.kind == kind]


class Realize(unittest.TestCase):
    def test_a_required_obligation_with_no_realization(self) -> None:
        r = Runs()
        (realize,) = kinds(r, "REALIZE")
        view = r.sc.view(r.trees["T0"])
        self.assertEqual((realize.target, realize.holder), ({"obligation": OBL}, "DISPATCHER"))
        self.assertEqual(realize.params["claim"], [{"unit": "code", "rev": view.rev("code")}])
        self.assertEqual(Workflow(r.sc.derive()).readiness(realize).state, "READY")

    def test_a_current_realization_ends_it_and_an_edit_reopens_it(self) -> None:
        r = Runs()
        r.run(r.tree("T0"), GOOD)
        self.assertEqual(kinds(r, "REALIZE"), [])
        r.sc.absorb({"a.py": "v = 2\n"})
        self.assertEqual(len(kinds(r, "REALIZE")), 1, "the claim changed: the realization is not current")

    def test_a_realization_no_longer_current_reopens_it(self) -> None:
        from ._scenario import challenge

        r = Runs()
        real = r.run(r.tree("T0"), GOOD)
        self.assertEqual(kinds(r, "REALIZE"), [])
        (bounding,) = real["fields"]["execution"]["bounded_by"]
        r.sc.admit(challenge({"record": bounding}))
        self.assertEqual(len(kinds(r, "REALIZE")), 1, "the same revisions, but its bounding judgment no longer holds")

    def test_an_incomplete_run_never_ends_it(self) -> None:
        from .test_phase_f_step9c_ii_iii import narrow_incomplete

        r = Runs()
        narrow_incomplete(r, r.tree("T0"))
        self.assertEqual(len(kinds(r, "REALIZE")), 1)

    def test_a_defective_specification_derives_none(self) -> None:
        self.assertEqual(kinds(Declared("oracle = \n"), "REALIZE"), [])

    def test_an_undesignated_class_waits(self) -> None:
        from unittest import mock

        from . import test_assessment as ta

        with mock.patch.object(ta, "POLICY", ta.POLICY.split("[runners.ci]")[0]):
            r = Runs()
        (realize,) = kinds(r, "REALIZE")
        self.assertEqual(Workflow(r.sc.derive()).readiness(realize).state, "WAITING")


    def test_an_unavailable_realization_never_ends_it(self) -> None:
        """Review of affd87fa, N5 (q3): a realization needing an unavailable reference serves nothing (§17.4)."""

        from ._fixtures import record

        r = Runs()
        real = r.run(r.tree("T0"), GOOD)
        r.sc.admit(record("AVAILABILITY", target={"digest": real["fields"]["evaluated"]}, outcome="UNAVAILABLE",
                          actor=HUMAN_B))
        self.assertEqual(len(kinds(r, "REALIZE")), 1)


class Assess(unittest.TestCase):
    def test_an_unassessed_realization_until_assessed(self) -> None:
        r = Runs()
        real = r.run(r.tree("T0"), BAD)
        (assess,) = kinds(r, "ASSESS")
        self.assertEqual((assess.target, assess.params, assess.holder),
                         ({"realization": real["id"]}, {"obligation": OBL}, "REVIEWER"))
        r.fail(real)
        self.assertEqual(kinds(r, "ASSESS"), [])

    def test_a_realization_admissible_only_adversely(self) -> None:
        """Review of affd87fa, N5 (q4): under a compromise from its admission it can still fail (F89)."""

        from ._fixtures import RUNNER_ROOT, record

        r = Runs()
        real = r.run(r.tree("T0"), BAD)
        at = r.sc.derive().s.position_of(real["id"])
        r.sc.lifecycle(record("KEY_LIFECYCLE", target=None, fields={
            "action": "COMPROMISED", "key": {**RUNNER_ROOT, "role": "RUNNER"}, "from_position": at}))
        self.assertEqual([o.target for o in kinds(r, "ASSESS")], [{"realization": real["id"]}])

    def test_judges_exclude_the_claims_authors_and_the_runs_lineage(self) -> None:
        """Review of affd87fa, N4: ASSESS is a judgment obligation (§10.3)."""

        r = Runs()
        r.run(r.tree("T0"), BAD)
        w = Workflow(r.sc.derive())
        (assess,) = [o for o in w.obligations if o.kind == "ASSESS"]
        authors = w.judged_authors(assess)
        self.assertIn("machinery:dispatcher@ed25519:test", authors)
        self.assertTrue(authors & r.sc.derive().s.authors("code", r.sc.view(r.trees["T0"]).rev("code")))
        self.assertFalse(set(w.eligible_judges(assess)) & authors)
        self.assertEqual(w.domain_of(assess), "D4", "the claim's domain")
        self.assertEqual(w.readiness(assess).waiting_on, ("no eligible judge",), "the claim's authorship is unknown")

    def test_a_named_human_outside_the_authors_judges_it(self) -> None:
        from unittest import mock

        from . import test_assessment as ta

        with mock.patch.object(ta, "POLICY", ta.POLICY.replace("evidence = true",
                                                               'evidence = true\nhumans = ["human:SHA256:carol"]')):
            r = Runs()
        r.run(r.tree("T0"), BAD)
        w = Workflow(r.sc.derive())
        (assess,) = [o for o in w.obligations if o.kind == "ASSESS"]
        self.assertEqual((w.eligible_judges(assess), w.readiness(assess).state), (("human:SHA256:carol",), "READY"))


class Rerun(unittest.TestCase):
    def failing(self, **run):
        r = Runs()
        failing = r.fail(r.run(r.tree("T0"), BAD, **run))
        return r, failing

    def test_both_conditions_lacking(self) -> None:
        r, failing = self.failing()
        self.assertEqual([o.target["on"] for o in kinds(r, "RERUN")], ["FAILING"],
                         "on its own tree the failing run is observed here (3)")
        r.sc.absorb({"a.py": "v = 2\n"})
        self.assertEqual([o.target["on"] for o in kinds(r, "RERUN")], ["FAILING"],
                         "its bounding judgment still holds for the failing tree, but nothing current bounds it here "
                         "(review of affd87fa, N3)")
        r.bound_judgment(r.sc.head)  # a current completeness judgment of the new tree bounds it again (§6.9)
        reruns = kinds(r, "RERUN")
        self.assertEqual(sorted(o.target["on"] for o in reruns), ["FAILING", "HERE"])
        self.assertTrue(all(o.target["record"] == failing["id"] and o.holder == "DISPATCHER" for o in reruns))

    def test_a_complete_rerun_ends_it_and_an_incomplete_one_does_not(self) -> None:
        r, failing = self.failing()
        r.run(r.tree("T0"), BAD)  # reproduced on the failing tree, which is also here
        self.assertEqual(kinds(r, "RERUN"), [])

    def test_an_incomplete_rerun_never_ends_it(self) -> None:
        from .test_phase_f_step9c_ii_iii import narrow_incomplete

        r, failing = self.failing()
        narrow_incomplete(r, r.tree("T0"))
        self.assertEqual([o.target["on"] for o in kinds(r, "RERUN")], ["FAILING"])

    def test_never_in_a_frame(self) -> None:
        from ssds.derivation.frames import Frame, transformation_of
        from ssds.derivation.state import State
        from ssds.derivation.support import Support

        from ._scenario import agent, submit

        r, failing = self.failing()
        x, _, _ = submit(r.sc, {"b.py": "w = 1\n"}, agent("maker"), "t-frame")
        s = r.sc.derive().s
        framed = Workflow(Support(State(s.h, None, Frame(s.h, s.n, transformation_of(s, x), s.enactment(x)))))
        self.assertEqual([o for o in framed.obligations if o.kind in ("REALIZE", "ASSESS", "RERUN", "READING")], [],
                         "SD-70: a frame derives no evidence obligation")
        self.assertTrue(kinds(r, "RERUN"), "the admitted state does")

    def test_a_challenged_bounding_judgment_bounds_nothing(self) -> None:
        """Review of affd87fa, N3: on the failing tree, the recorded judgments while they still stand."""

        from ._scenario import challenge

        r, failing = self.failing()
        (bounding,) = r.sc.derive().s.record(failing["target"]["realization"])["fields"]["execution"]["bounded_by"]
        r.sc.admit(challenge({"record": bounding}))
        self.assertEqual(kinds(r, "RERUN"), [])

    def test_a_disposed_failure_derives_none(self) -> None:
        """Review of affd87fa, N5 (q6)."""

        from ssds.derivation import T

        from ._scenario import attested, challenge

        r, failing = self.failing()
        self.assertTrue(kinds(r, "RERUN"))
        c = challenge({"record": failing["id"]})
        r.sc.admit(c)
        r.sc.admit(*attested(judgment("ADJUDICATION", {"record": c["id"]}, "UPHELD", actor=HUMAN_B)))
        d = r.sc.derive()
        self.assertEqual(d.a.disposition(failing["id"], d.values.get, d.base, d.j.nonind), T)
        self.assertEqual(kinds(r, "RERUN"), [])

    def test_a_rerun_of_another_configuration_never_ends_it(self) -> None:
        """Review of affd87fa, N5 (q7): another pin set is not ext-equal, so it observes nothing for (1)."""

        r, failing = self.failing()
        r.run(r.tree("T0"), BAD, pins=("p2",))
        self.assertEqual([o.target["on"] for o in kinds(r, "RERUN")], ["FAILING"])

    def test_an_unserving_rerun_ends_it(self) -> None:
        from ._scenario import challenge

        r, failing = self.failing()
        rerun = r.run(r.tree("T0"), BAD)
        r.sc.admit(challenge({"record": rerun["id"]}))  # not standing: it serves no condition
        self.assertEqual(kinds(r, "RERUN"), [], "it ran: no loop; the failure stays with its owner")

    def test_never_when_it_differed_or_the_closure_is_unbounded(self) -> None:
        r, failing = self.failing()
        r.run(r.tree("T0"), GOOD, pins=("p2",))  # other pins, so no rerun; same tree, a differing outcome: (2)
        self.assertEqual(kinds(r, "RERUN"), [], "nondeterministic in fact: the owner's")
        unbounded, _ = self.failing(bounded=False)
        self.assertEqual(kinds(unbounded, "RERUN"), [], "no completeness judgment bounds the closure")


ASSESSOR_READ = """oracle = "ASSESSOR_READ"
runner = "ci"
time_bound_hours = 24
outputs = [{ name = "x", type = "int" }]
"""


class Reading(unittest.TestCase):
    def test_an_assessor_read_failure_observed_here(self) -> None:
        r = Declared(ASSESSOR_READ)
        t0 = r.tree("T0")
        failing = r.fail(r.run(t0, {"x": 1}))
        r.run(t0, {"x": 1})
        (reading,) = kinds(r, "READING")
        self.assertEqual((reading.target, reading.holder, reading.params["class"]),
                         ({"record": failing["id"]}, "REVIEWER", "R2"))
        observed = reading.params["observation"]
        view = r.sc.view(t0)
        r.sc.admit(judgment("EVIDENCE_ASSESSMENT", {"realization": observed, "obligation": OBL}, "FAIL",
                            actor=HUMAN_B, basis=[on_record(observed), content("spec", view.rev("spec"))],
                            fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": view.rev("spec")},
                                    "failing_outputs": ["x"]}))
        self.assertEqual(kinds(r, "READING"), [], "a failing assessment of the outcome answers it")

    def test_only_a_failing_assessment_ends_it(self) -> None:
        """Review of affd87fa, N5 (q10); N4: a judgment. (N1's wait on 9e is lifted by 9e-i, reading F110.)"""

        r = Declared(ASSESSOR_READ)
        t0 = r.tree("T0")
        r.fail(r.run(t0, {"x": 1}))
        r.run(t0, {"x": 1})
        (reading,) = kinds(r, "READING")
        observed = reading.params["observation"]
        view = r.sc.view(t0)
        r.sc.admit(judgment("EVIDENCE_ASSESSMENT", {"realization": observed, "obligation": OBL}, "PASS",
                            actor=HUMAN_B, basis=[on_record(observed), content("spec", view.rev("spec"))],
                            fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": view.rev("spec")}}))
        (reading,) = kinds(r, "READING")
        w = Workflow(r.sc.derive())
        self.assertEqual(w.readiness(reading).waiting_on, ("no eligible judge",),
                         "9e lifted its wait (F110): only the judge is lacking, the claim's authorship being unknown")
        self.assertIn("machinery:dispatcher@ed25519:test", w.judged_authors(reading),
                      "the observation's lineage, and a⁻'s root authors")

    def test_the_failing_revisions_authors_never_judge_it(self) -> None:
        """Re-check of 2136fb90, note 2: a⁻'s claim revision and the observation's differ, so a⁻'s root authors are
        needed beside the observation's."""

        from unittest import mock

        from ssds.derivation.judgment import Judgments
        from ssds.derivation.state import State

        def by_rev(self, unit, rev, *rest):
            return frozenset({f"human:author-{rev[:8]}"})

        r = Declared(ASSESSOR_READ)
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        r.fail(r.run(t0, {"x": 1}))
        r.sc.absorb({"a.py": "v = 2\n"})
        r.run(t1, {"x": 1})
        before, after = r.sc.view(t0).rev("code"), r.sc.view(t1).rev("code")
        with mock.patch.object(State, "authors", by_rev), mock.patch.object(Judgments, "piece_authors", by_rev):
            w = Workflow(r.sc.derive())
            (reading,) = [o for o in w.obligations if o.kind == "READING"]
            self.assertLessEqual({f"human:author-{before[:8]}", f"human:author-{after[:8]}"},
                                 set(w.judged_authors(reading)))

    def test_a_class_r3_reading_is_a_humans(self) -> None:
        """Review of affd87fa, N4: at its class, R3 for a D1 or D2 subject (§3.4)."""

        import dataclasses
        from unittest import mock

        r = Declared(ASSESSOR_READ)
        t0 = r.tree("T0")
        r.fail(r.run(t0, {"x": 1}))
        r.run(t0, {"x": 1})
        w = Workflow(r.sc.derive())
        (reading,) = [o for o in w.obligations if o.kind == "READING"]
        r3 = dataclasses.replace(reading, params_json=reading.params_json.replace('"R2"', '"R3"'))
        with mock.patch.object(Workflow, "judged_authors", lambda self, o: frozenset({"machinery:x"})):
            self.assertEqual((w.eligible_judges(reading), w.eligible_judges(r3)), (("agent:fresh-reviewer",), ()))

    def test_never_for_a_mechanical_oracle(self) -> None:
        """Review of affd87fa, N5 (q9)."""

        r = Runs()
        t0 = r.tree("T0")
        r.fail(r.run(t0, BAD))
        r.run(t0, BAD)
        self.assertEqual(kinds(r, "READING"), [])

    def test_an_assessor_read_failure_is_never_stale_mechanically(self) -> None:
        r = Declared(ASSESSOR_READ)
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(t0, {"x": 1}))
        r.run(t0, {"x": 1})
        r.run(t1, {"x": 2})
        self.assertFalse(r.stale(failing, "T1"), "no mechanical verdict is computable (§6.5)")


class Floor(unittest.TestCase):
    def test_the_floor_latches_for_a_failure_whose_rerun_ended_incomplete(self) -> None:
        """§6.8's INCOMPLETE trigger is subsumed by E34's floor (F95): a D2 claim's counting failure beside passing
        evidence raises it, and an INCOMPLETE rerun changes nothing (test_step5_review's b8 scenario)."""

        from unittest import mock

        from . import test_assessment as ta
        from ._scenario import agent, attested
        from .test_phase_f_step9c_ii_iii import narrow_incomplete
        from .test_step5_review import attention

        with mock.patch.object(ta, "UNITS", ta.UNITS.replace('kind = "D4"', 'kind = "D2"')), \
                mock.patch.object(ta, "POLICY", 'schema = 1\n[domains.D2]\nevidence = true\n' + ta.RUNNERS):
            r = Runs()
            t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
            failing = r.fail(r.run(t0, ta.BAD))
            r.run(t0, ta.BAD)
            good = r.run(t1, ta.GOOD)
            view = r.sc.view(t0)
            r.sc.admit(*attested(judgment("EVIDENCE_ASSESSMENT", {"realization": good["id"], "obligation": ta.OBL},
                                          "PASS", actor=agent("assessor"), actor_class="AGENT",
                                          basis=[on_record(good["id"]), content("spec", view.rev("spec"))],
                                          fields={"mode": "ORDINARY",
                                                  "reading": {"unit": "spec", "rev": view.rev("spec")}})))
            narrow_incomplete(r, t0)
            floors = [k for k in attention(Workflow(r.sc.derive())) if isinstance(k, str)
                      and k.startswith("disagreement:")]
            self.assertEqual(floors, [f"disagreement:{failing['id']}"])


if __name__ == "__main__":
    unittest.main()
