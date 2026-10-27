"""Phase F step 9e-i: discriminating readings in derivation (catalogue §6.5-§6.9; plan §3.6, readings F105-F110).

F105 first: a failure naming no outputs found every declared output failing (§6.5), so an assessor-read failure,
whose declaration has no verdicts, is compared on its outputs and never goes stale by mechanics alone (§6.6: "a
value alone discriminates nothing"). Expected values are from §6.5-§6.6 (found by the 9e survey's probe).
"""

from __future__ import annotations

import unittest

from ._scenario import HUMAN_B, content, judgment, on_record
from .test_assessment import OBL
from .test_phase_f_step9b_ii import Declared
from .test_phase_f_step9c_ii_iv import ASSESSOR_READ


def unnamed_failure(r, realization: dict) -> dict:
    """A failing assessment naming no failing outputs."""

    view = r.sc.view(r.trees["T0"])
    a = judgment("EVIDENCE_ASSESSMENT", {"realization": realization["id"], "obligation": OBL}, "FAIL", actor=HUMAN_B,
                 basis=[on_record(realization["id"]), content("spec", view.rev("spec"))],
                 fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": view.rev("spec")}})
    r.sc.admit(a)
    return a


class NamingNone(unittest.TestCase):
    def test_an_unnamed_assessor_read_failure_is_never_stale_mechanically(self) -> None:
        r = Declared(ASSESSOR_READ)
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = unnamed_failure(r, r.run(t0, {"x": 1}))
        r.run(t0, {"x": 1})
        r.run(t1, {"x": 2})
        self.assertEqual(r.sc.derive().a.failing_outputs(failing["id"]), ["x"], "every declared output")
        self.assertFalse(r.stale(failing, "T1"), "a value alone discriminates nothing (§6.6)")

    def test_a_mechanical_failure_naming_none_reads_every_declared_output(self) -> None:
        from .test_assessment import BAD, Runs

        r = Runs()
        failing = unnamed_failure(r, r.run(r.tree("T0"), BAD))
        self.assertEqual(r.sc.derive().a.failing_outputs(failing["id"]), ["x", "x_verdict"],
                         "the verdict carrier included (plan check of beaa9e46, note 1)")


    def test_a_genuine_fix_of_an_embedded_failure_naming_none(self) -> None:
        """Review of 3f976498, note 1: the carrier in F(a⁻) is judged by the output it carries, so the mechanical stop
        stays (as test_assessment's genuine fix, naming none)."""

        from .test_assessment import BAD, GOOD, Runs

        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = unnamed_failure(r, r.run(t0, BAD))
        r.run(t0, BAD)
        r.run(t1, GOOD)
        self.assertTrue(r.stale(failing, "T1"))



class Readings(Declared):
    """s1's vocabulary on the evidence fixture (``s1_disagreement_model_check.py``), its assessor-read failure ``a⁻``
    run on T0 with ``x = 1``:
    - ``MOVE`` an integrated change of the claim (``a.py``); ``ORACLE`` an integrated change of the specification,
      the reading; ``UMOVE`` an integrated change outside both (``other.txt``), toggled;
    - ``EXEC(o, old=True)`` a reproduction on ``a⁻``'s tree; ``EXEC(o)`` a run on the head;
    - ``DUAL(o)`` a run on the head with ``x = o`` and one discriminating reading of it against the latest
      reproduction, its basis as Q-F24 (a) gives it (``record`` on ``p``; ``identity`` on ``q`` and ``a⁻``);
    - ``PASS_`` after the failure, an ordinary passing assessment of the latest run. s1's leading ``PASS_`` is an
      assessment outside ``conf(a⁻)`` and leaves the claim's final value unchanged, so it is left out here."""

    def __init__(self) -> None:
        from .test_phase_f_step9c_ii_iv import ASSESSOR_READ

        super().__init__(ASSESSOR_READ)
        self.failure = self.fail(self.run(self.tree("T0"), {"x": 1}))
        self.moves, self.latest, self.reproduction = 0, None, None

    def integrate(self, files: dict[str, str]) -> None:
        from ._scenario import agent

        self.moves += 1
        self.sc.integrate(files, agent("maker"), f"task-{self.moves}")

    def move(self) -> None:
        self.integrate({"a.py": f"v = {self.moves + 2}\n"})

    def oracle(self) -> None:
        from .test_assessment import SPEC

        self.integrate({"s.py": SPEC + f"# reading {self.moves}\n"})

    def umove(self) -> None:
        self.integrate({"other.txt": f"{self.moves % 2}\n"})

    def exec(self, o: int, old: bool = False) -> dict:
        real = self.run(self.trees["T0"] if old else self.sc.head, {"x": o})
        if old:
            self.reproduction = real
        self.latest = real
        return real

    def dual(self, o: int, attest: bool = True) -> dict:
        from ._scenario import judgment as make

        p, q = self.exec(o), self.reproduction
        view = self.sc.view(self.sc.head)
        now = {"unit": "spec", "rev": view.rev("spec")}
        then = self.failure["fields"]["reading"]
        failing = {"observation": q["id"], "reading": then, "verdict": "FAIL", "assessment": self.failure["id"]}
        if now != then:
            failing |= {"reason": "READING_REVISED", "reference": "sha256:" + "6" * 64}
        reading = make("EVIDENCE_ASSESSMENT", {"realization": p["id"], "obligation": OBL}, "PASS", actor=HUMAN_B,
                       basis=[on_record(p["id"]), content("spec", now["rev"]), content("code", view.rev("code")),
                              on_record(q["id"], "identity"), on_record(self.failure["id"], "identity")],
                       fields={"mode": "DISCRIMINATING", "reading": now,
                               "observations": [{"observation": p["id"], "reading": now, "verdict": "PASS"}, failing]})
        attestation = make("NON_AUTHORSHIP_ATTESTATION", {"record": reading["id"]}, "NOT_AUTHOR", actor=HUMAN_B)
        self.sc.admit(*([reading, attestation] if attest else [reading]))  # without it, not independent (F108)
        self.reading = {"record": reading, "observations": [p["id"], q["id"]]}
        return reading

    def pass_(self) -> None:
        from ._scenario import judgment as make

        view = self.sc.view(self.sc.head)
        now = {"unit": "spec", "rev": view.rev("spec")}
        self.sc.admit(make("EVIDENCE_ASSESSMENT", {"realization": self.latest["id"], "obligation": OBL}, "PASS",
                           actor=HUMAN_B, basis=[on_record(self.latest["id"]), content("spec", now["rev"])],
                           fields={"mode": "ORDINARY", "reading": now}))

    def ev(self) -> int:
        from ssds.derivation import F

        d = self.sc.derive()
        return d.a.ev("code", OBL, lambda node: d.values.get(node, F), d.base, d.j.nonind)


class S1Discriminators(unittest.TestCase):
    """The named s1 discriminators reachable in the admitted state (FAIL_CAND and FAIL_TIGHT are frame evidence,
    SD-70), their expected values transcribed from ``s1_disagreement_model_check.py``: T (stale, covered) or P (the
    failure counts)."""

    def assertValue(self, r: Readings, expected: str) -> None:
        from ssds.derivation import P, T

        self.assertEqual(r.ev(), {"T": T, "P": P}[expected])

    def test_x2_a_later_assessor_passing_the_new_outcome_never_settles_it(self) -> None:
        # ef8445a X2: (PASS_, FAIL_, MOVE, EXEC(1, 1, old=True), EXEC(1, 3), PASS_) -> P
        r = Readings()
        r.move(), r.exec(1, old=True), r.exec(3), r.pass_()
        self.assertValue(r, "P")

    def test_x2_contrast_one_honest_record_reads_both_outcomes(self) -> None:
        # ef8445a X2 contrast: (PASS_, FAIL_, MOVE, EXEC(1, 1, old=True), DUAL(1, 2), PASS_) -> T
        r = Readings()
        r.move(), r.exec(1, old=True), r.dual(2), r.pass_()
        self.assertValue(r, "T")

    def test_x3_a_change_with_no_new_assessment(self) -> None:
        """ef8445a X3: (PASS_, FAIL_, CMOVE, EXEC(1, 1, old=True), EXEC(1, 3)) -> P. What it discriminates holds: with
        no new reading the failure keeps counting and the claim is not T. s1's P rests on the equivalence keeping its
        leading ``PASS_`` current; here a realization supports its claim only at the claim's exact revision (§17.4,
        F91; §4.4: ``EXACT`` takes no equivalence), so that pass is not current and the value is F. A Stage S note.
        The change is therefore a plain move: an equivalence would not reach the ``EXACT`` entry."""

        from ssds.derivation import T

        r = Readings()
        r.move(), r.exec(1, old=True), r.exec(3)
        d = r.sc.derive()
        self.assertEqual(d.a.adverse("code", OBL, d.base), [r.failure["id"]], "the failure counts")
        self.assertNotEqual(r.ev(), T)

    def test_a_reading_made_under_an_earlier_reading_no_longer_stands(self) -> None:
        # (PASS_, FAIL_, EXEC(1, 1, old=True), MOVE, DUAL(1, 0), ORACLE, EXEC(1, 0), PASS_) -> P
        r = Readings()
        r.exec(1, old=True), r.move(), r.dual(0), r.oracle(), r.exec(0), r.pass_()
        self.assertValue(r, "P")

    def test_y1_after_a_change_an_identical_outcome_stays_covered(self) -> None:
        # 552ac01 Y1: (PASS_, FAIL_, MOVE, EXEC(1, 1, old=True), DUAL(1, 0), MOVE, EXEC(1, 0), PASS_) -> T
        r = Readings()
        r.move(), r.exec(1, old=True), r.dual(0), r.move(), r.exec(0), r.pass_()
        self.assertValue(r, "T")

    def test_y1_contrast_a_perturbed_outcome_needs_a_new_reading(self) -> None:
        # (PASS_, FAIL_, MOVE, EXEC(1, 1, old=True), DUAL(1, 0), MOVE, EXEC(1, 2), PASS_) -> P
        r = Readings()
        r.move(), r.exec(1, old=True), r.dual(0), r.move(), r.exec(2), r.pass_()
        self.assertValue(r, "P")

    def test_y1_contrast_a_revert_yields_the_failing_outcome_again(self) -> None:
        # (PASS_, FAIL_, UMOVE, EXEC(1, 1, old=True), DUAL(1, 0), UMOVE, EXEC(1, 1), PASS_) -> P
        r = Readings()
        r.umove(), r.exec(1, old=True), r.dual(0), r.umove(), r.exec(1), r.pass_()
        self.assertValue(r, "P")



class Coverage(unittest.TestCase):
    """§6.6's standing and absorption clauses, §6.9's ``READING`` and §6.8's class (readings F107, F108, F110)."""

    def covered_case(self, **dual) -> Readings:
        r = Readings()
        r.move(), r.exec(1, old=True), r.dual(0, **dual), r.move(), r.exec(0), r.pass_()
        return r

    def test_the_y1_case_is_covered_and_explained(self) -> None:
        from ssds.derivation import T

        r = self.covered_case()
        self.assertEqual(r.ev(), T)
        d = r.sc.derive()
        self.assertEqual(len(d.a.explain(r.failure["id"], d.base)["readings"]), 1, "the covering reading shown")

    def test_a_reading_that_does_not_stand_covers_nothing(self) -> None:
        from ssds.derivation import P

        from ._scenario import challenge

        cases = {"not independent": dict(attest=False)}
        for name, dual in cases.items():
            with self.subTest(case=name):
                self.assertEqual(self.covered_case(**dual).ev(), P)
        r = self.covered_case()
        r.sc.admit(challenge({"record": r.reading["observations"][0]}))  # p's realization, blocking
        self.assertEqual(r.ev(), P, "its passing observation no longer stands")

    def test_a_superseded_reading_covers_nothing(self) -> None:
        from ssds.derivation import P

        from ._scenario import judgment as make

        r = self.covered_case()
        reading = r.reading["record"]
        later = make("EVIDENCE_ASSESSMENT", reading["target"], "PASS", actor=HUMAN_B, supersedes=[reading["id"]],
                     basis=reading["basis"], fields={"mode": "ORDINARY", "reading": reading["fields"]["reading"]})
        r.sc.admit(later)
        self.assertEqual(r.ev(), P)

    def test_an_absorbed_claim_revision_covers_nothing_until_integrated(self) -> None:
        """§6.6: "a reading under a specification or claim revision that the admitted state holds only by absorption
        covers nothing there until an admission integrates that revision"."""

        from ssds.derivation import P

        r = Readings()
        r.exec(1, old=True)
        r.sc.absorb({"a.py": "v = 9\n"})  # p runs on content held only by absorption
        r.dual(0), r.move(), r.exec(0), r.pass_()
        self.assertEqual(r.ev(), P)

    def test_reading_is_derived_until_covered_and_classed_by_its_history(self) -> None:
        from unittest import mock

        from ssds.derivation import Workflow
        from ssds.derivation.state import State

        r = Readings()
        r.move(), r.exec(1, old=True), r.exec(0)

        def readings():
            return [o for o in Workflow(r.sc.derive()).obligations if o.kind == "READING"]

        (reading,) = readings()
        self.assertEqual(reading.params["class"], "R2")
        with mock.patch.object(State, "_authority_roots", frozenset({"code"})):
            (r3,) = readings()
        self.assertEqual(r3.params["class"], "R3", "a unit that has been D2 (F108)")
        r.dual(0)
        self.assertEqual(readings(), [], "a standing reading covers the observation here (F110)")

    def test_reading_names_an_observation_no_reading_covers(self) -> None:
        """F110: a covered observation here needs no reading; another outcome here still does."""

        from ssds.derivation import Workflow

        r = Readings()
        r.move(), r.exec(1, old=True), r.dual(0)
        other = r.exec(5)
        (reading,) = [o for o in Workflow(r.sc.derive()).obligations if o.kind == "READING"]
        self.assertEqual(reading.params["observation"], other["id"])


    def test_an_overridden_reading_covers_nothing(self) -> None:
        """F107: ``status1`` ``CLEAR``, stricter than "not ``REVOKED`` or ``BLOCKED``" (a Stage S note): a risk
        override never resolves a challenge, so a reading under one covers nothing."""

        from ssds.derivation import P, T

        from ._scenario import OWNER, challenge
        from ._scenario import judgment as make

        r = self.covered_case()
        c = challenge({"record": r.reading["record"]["id"]})
        r.sc.admit(c)
        r.sc.admit(make("RISK_OVERRIDE", {"record": c["id"]}, None, actor=OWNER,
                        fields={"continuation": {"subjects": ["code"], "items": [], "kinds": []}}))
        d = r.sc.derive()
        self.assertNotEqual(d.s.status1(r.reading["record"]["id"]), "CLEAR")
        self.assertIn(r.ev(), (P,), "the failure counts again")
        self.assertNotEqual(r.ev(), T)

    def test_a_readings_judged_authors(self) -> None:
        """F108: the claim authors of both observations and ``a⁻``'s root authors."""

        from unittest import mock

        from ssds.derivation.judgment import Judgments
        from ssds.derivation.state import State

        def by_rev(self, unit, rev, *rest):
            return frozenset({f"human:author-{rev[:8]}"})

        r = self.covered_case()
        reading = r.reading["record"]
        d = r.sc.derive()
        claims = {c["rev"] for o in r.reading["observations"] for c in d.s.record(o)["target"]["claim"]}
        claims |= {c["rev"] for c in d.s.record(r.failure["target"]["realization"])["target"]["claim"]}
        with mock.patch.object(State, "authors", by_rev), mock.patch.object(Judgments, "piece_authors", by_rev):
            authors = r.sc.derive().j.judged_authors(reading["id"])
        self.assertEqual(set(authors), {f"human:author-{rev[:8]}" for rev in claims})
        self.assertGreater(len(claims), 1, "the observations ran on different claim revisions")

    def test_a_readings_judged_authors_include_the_failures_own(self) -> None:
        """F108: ``a⁻``'s root authors, even where neither observation ran on ``a⁻``'s claim revision (``q`` may be
        any complete run of ``conf(a⁻)`` with ``a⁻``'s outcome, F109)."""

        from unittest import mock

        from ssds.derivation.judgment import Judgments
        from ssds.derivation.state import State

        def by_rev(self, unit, rev, *rest):
            return frozenset({f"human:author-{rev[:8]}"})

        r = Readings()
        r.move()
        r.reproduction = r.exec(1)  # a⁻'s outcome, on the moved head
        reading = r.dual(0)
        d = r.sc.derive()
        failure_rev = d.s.record(r.failure["target"]["realization"])["target"]["claim"][0]["rev"]
        with mock.patch.object(State, "authors", by_rev), mock.patch.object(Judgments, "piece_authors", by_rev):
            authors = r.sc.derive().j.judged_authors(reading["id"])
        self.assertIn(f"human:author-{failure_rev[:8]}", authors)


class Shape(unittest.TestCase):
    """F106: the reading's closed inner shape, read by one owner."""

    def test_the_closed_shape(self) -> None:
        from ssds.derivation.reading import read

        r = Readings()
        r.move(), r.exec(1, old=True)
        reading = r.dual(0)
        self.assertTrue(read(reading["id"], reading).well_formed)
        fields = reading["fields"]
        pass_item, same_item = fields["observations"]  # the readings are equal: no difference named
        fail_item = {**same_item, "reading": {"unit": "spec", "rev": "sha256:" + "5" * 64}, "reason": "R",
                     "reference": "sha256:" + "6" * 64}  # a revised reading, its difference named

        def well_formed(items, **changes) -> bool:
            return read("x", {**reading, **changes, "fields": {**fields, "observations": items}}).well_formed

        self.assertTrue(well_formed([pass_item, fail_item]))
        self.assertTrue(well_formed([fail_item, pass_item]), "in either order")
        cases = {
            "three items": [pass_item, fail_item, fail_item],
            "two passes": [pass_item, pass_item],
            "an extra key": [pass_item, {**fail_item, "extra": 1}],
            "no difference named": [pass_item, {k: v for k, v in fail_item.items() if k not in ("reason", "reference")}],
            "a difference where the readings agree": [pass_item, {**same_item, "reason": "R",
                                                                  "reference": "sha256:" + "6" * 64}],
            "a bad reference": [pass_item, {**fail_item, "reference": "x"}],
            "an empty reason": [pass_item, {**fail_item, "reason": ""}],
            "not the target": [{**pass_item, "observation": fail_item["observation"]}, fail_item],
            "not the reading": [{**pass_item, "reading": fail_item["reading"]}, fail_item],
            "a failure unnamed": [pass_item, {k: v for k, v in fail_item.items() if k != "assessment"}],
        }
        for name, items in cases.items():
            with self.subTest(case=name):
                self.assertFalse(well_formed(items))
        self.assertFalse(well_formed([pass_item, same_item], outcome="FAIL"), "a reading's outcome is PASS")
        self.assertFalse(read("x", {**reading, "fields": {**fields, "failing_outputs": ["x"]}}).well_formed)

if __name__ == "__main__":
    unittest.main()
