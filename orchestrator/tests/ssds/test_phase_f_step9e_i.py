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


if __name__ == "__main__":
    unittest.main()
