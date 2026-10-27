"""Phase F step 9c-ii-ii: a realization's currency and binding health (catalogue §17.4; plan §3.6, readings F91-F92).

A realization supports a claim only while its recorded execution basis holds, together with its bounding completeness
judgments, and its target is the claim's revision; stale passing evidence never discharges. A passing assessment
whose realization needs a reference the latest acting ``AVAILABILITY`` record marks unavailable contributes at most
``P``, and its observation is not standing; adverse uses are unchanged. Expected values are from §17.4 (no Stage S
case covers them).
"""

from __future__ import annotations

import unittest

from ssds.derivation import F, P, T

from ._fixtures import record
from ._scenario import HUMAN_B, challenge, content, judgment, on_record
from .test_assessment import GOOD, OBL, Runs


class Passing(Runs):
    def __init__(self) -> None:
        super().__init__()
        self.real = self.run(self.tree("T0"), GOOD)
        view = self.sc.view(self.trees["T0"])
        self.passing = judgment("EVIDENCE_ASSESSMENT", {"realization": self.real["id"], "obligation": OBL}, "PASS",
                                actor=HUMAN_B, basis=[on_record(self.real["id"]), content("spec", view.rev("spec"))],
                                fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": view.rev("spec")}})
        self.sc.admit(self.passing)

    def current(self) -> int:
        return self.sc.derive().current(self.real["id"])

    def ev(self) -> int:
        d = self.sc.derive()
        return d.a.ev("code", OBL, lambda node: d.values.get(node, F), d.base, d.j.nonind)


class Currency(unittest.TestCase):
    def test_a_current_realization(self) -> None:
        r = Passing()
        self.assertEqual((r.current(), r.ev()), (T, T))

    def test_a_claim_edit_makes_it_stale(self) -> None:
        r = Passing()
        r.sc.absorb({"a.py": "v = 2\n"})
        self.assertEqual(r.current(), F, "its target is no longer the claim's revision")
        self.assertEqual(r.ev(), F, "stale passing evidence never discharges")

    def test_the_target_alone_makes_it_stale(self) -> None:
        """A realization whose execution basis does not record the claim: its target entry alone (F91)."""

        from .test_phase_f_step9b_ii import DECLARATIVE
        from .test_phase_f_step9c_ii_i import Fixture

        r = Fixture(DECLARATIVE)
        real = r.realization()
        self.assertEqual(r.sc.derive().current(real["id"]), T)
        r.sc.absorb({"a.py": "v = 2\n"})
        self.assertEqual(r.sc.derive().current(real["id"]), F)

    def test_a_dependency_edit_makes_it_stale(self) -> None:
        r = Passing()
        spec = r.files["s.py"].replace("return 1", "return 3")
        r.sc.absorb({"s.py": spec})
        self.assertEqual(r.current(), F, "its execution basis no longer holds")

    def test_a_bounding_judgment_no_longer_current(self) -> None:
        r = Passing()
        (bounding,) = r.real["fields"]["execution"]["bounded_by"]
        r.sc.admit(challenge({"record": bounding}))
        self.assertEqual(r.current(), F, "its bounding completeness judgment no longer holds")


class BindingHealth(unittest.TestCase):
    def availability(self, r, outcome):
        r.sc.admit(record("AVAILABILITY", target={"digest": r.real["fields"]["evaluated"]}, outcome=outcome,
                          actor=HUMAN_B))

    def test_an_unavailable_outcome_holds_at_most_provisionally(self) -> None:
        r = Passing()
        self.availability(r, "UNAVAILABLE")
        self.assertEqual(r.ev(), P, "not T")
        self.assertFalse(r.sc.derive().a.standing(r.real["id"]))
        self.availability(r, "AVAILABLE")
        self.assertEqual(r.ev(), T, "the latest record restores it")

    def test_a_reference_its_envelope_names(self) -> None:
        """Review of 06a20532, note 4 (y8)."""

        from .test_phase_f_step9b_ii import DECLARATIVE
        from .test_phase_f_step9c_ii_i import Fixture

        r = Fixture(DECLARATIVE)
        log = "sha256:" + "4" * 64
        real = r.realization(refs=[{"store": "RUNNER", "digest": log, "media_type": "text/plain"}])
        self.assertTrue(r.sc.derive().a.standing(real["id"]))
        r.sc.admit(record("AVAILABILITY", target={"digest": log}, outcome="UNAVAILABLE", actor=HUMAN_B))
        self.assertFalse(r.sc.derive().a.standing(real["id"]))

    def test_only_an_acting_record_counts(self) -> None:
        """Review of 06a20532, note 4 (y7): a record in the frame of a transformation not integrated does not act
        (§5.2), so it decides nothing."""

        from ssds.ledger.read import with_id

        from ._scenario import agent, submit

        r = Passing()
        x, _, _ = submit(r.sc, {"b.py": "w = 1\n"}, agent("maker"), "t-pending")
        pending = with_id({**record("AVAILABILITY", target={"digest": r.real["fields"]["evaluated"]},
                                    outcome="UNAVAILABLE", actor=HUMAN_B), "frame": {"transformation": x}})
        r.sc.admit(pending)
        self.assertEqual(r.ev(), T, "not acting")

    def test_an_unavailable_reference_never_changes_adverse_use(self) -> None:
        r = Runs()
        failing = r.fail(r.run(r.tree("T0"), {"x": 1, "x_verdict": "FAIL"}))
        d = r.sc.derive()
        before = d.a.qual("code", lambda node: d.values.get(node, F), d.base, d.j.nonind)
        real = r.sc.derive().s.record(failing["target"]["realization"])
        r.sc.admit(record("AVAILABILITY", target={"digest": real["fields"]["evaluated"]}, outcome="UNAVAILABLE",
                          actor=HUMAN_B))
        d = r.sc.derive()
        self.assertEqual(d.a.qual("code", lambda node: d.values.get(node, F), d.base, d.j.nonind), before)


if __name__ == "__main__":
    unittest.main()
