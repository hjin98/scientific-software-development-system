"""Phase E step 4c: the DOMAIN family of the check library (catalogue §14.3, §14.5; class INCOMPLETE, reading E25).

Each case states the defect the template exists to catch and a clean control; the unit grammar is the
analyzer's UCUM subset, and an expression outside it is never assumed consistent.
"""

from __future__ import annotations

import unittest

from ssds.analyzers import dimension
from ssds.derivation.conformance import CLEAN, INCOMPLETE, SIGNAL

from .test_conformance import SLOTS
from .test_conformance_python import classes_of

HEADER = "from typing import Annotated\nfrom units import Unit\n\n\ndef step():\n    return 1\n\n\n"
CONSISTENT = HEADER + ('dist: Annotated[float, Unit("m")] = 1.0\ntime: Annotated[float, Unit("s")] = 2.0\n'
                       'speed: Annotated[float, Unit("m/s")] = dist / time\n')


class Units(unittest.TestCase):
    def test_the_ucum_subset(self) -> None:
        self.assertEqual(dimension("kg.m2/s2"), dimension("J"))
        self.assertEqual(dimension("km/h"), dimension("m.s-1"))
        self.assertEqual(dimension("(m/s)2"), dimension("m2/s2"))
        self.assertIsNone(dimension("furlong"), "outside the subset: not analyzable")
        self.assertIsNone(dimension("m/("))


class DimensionalConsistency(unittest.TestCase):
    template = "DOMAIN.dimensional_consistency"

    def test_consistent_and_introduced_inconsistency(self) -> None:
        self.assertEqual(classes_of(self.template, {"src/solver.py": CONSISTENT}), {CLEAN})
        bad = CONSISTENT + "total = dist + time\n"
        self.assertEqual(classes_of(self.template, {"src/solver.py": bad}), {INCOMPLETE})
        assigned = CONSISTENT + "def f(v: Annotated[float, Unit(\"m/s\")]):\n    d: Annotated[float, Unit(\"m\")] = v\n"
        self.assertEqual(classes_of(self.template, {"src/solver.py": assigned}), {INCOMPLETE})

    def test_a_pre_existing_inconsistency_is_not_the_candidates(self) -> None:
        bad = CONSISTENT + "total = dist + time\n"
        self.assertEqual(classes_of(self.template, {"src/solver.py": bad + "extra = 1\n"}, base={"src/solver.py": bad}),
                         {CLEAN})

    def test_unanalyzable_units_fail_closed(self) -> None:
        odd = HEADER + 'reach: Annotated[float, Unit("furlong")] = 1.0\n'
        self.assertEqual(classes_of(self.template, {"src/solver.py": odd}), {INCOMPLETE})
        self.assertEqual(classes_of(self.template, {"src/limits.toml": "# ssds:unit dt = s\ndt = 0.1\n"}), {INCOMPLETE},
                         "units declared in a language the pinned analyzers do not cover")


class ToleranceDeclared(unittest.TestCase):
    template = "DOMAIN.tolerance_declared"

    def test_claims_in_units_carry_tolerance_and_precision(self) -> None:
        bare = dict(SLOTS, claims=[{"claim": "the step is 0.1 s", "unit": "s", "records": []}])
        self.assertEqual(classes_of(self.template, {"src/solver.py": CONSISTENT}, slots=bare), {INCOMPLETE})
        full = dict(SLOTS, claims=[{"claim": "the step is 0.1 s", "unit": "s", "tolerance": "0.001", "precision": "float64",
                                    "records": []}])
        self.assertEqual(classes_of(self.template, {"src/solver.py": CONSISTENT}, slots=full), {CLEAN})


class LayerDirection(unittest.TestCase):
    def test_an_ascending_relation_the_candidate_introduces(self) -> None:
        template = "DOMAIN.layer_direction"
        ascending = "# Numerics\n<!-- ssds:rel DEPENDS_ON src -->\n"
        self.assertEqual(classes_of(template, {"numerics.md": ascending}), {INCOMPLETE})
        descending = "def step():\n    return 1\n# ssds:rel DEPENDS_ON numerics\n"
        self.assertEqual(classes_of(template, {"src/solver.py": descending}), {CLEAN})


class UnitInference(unittest.TestCase):
    def test_an_unannotated_quantity_only_signals(self) -> None:
        self.assertEqual(classes_of("DOMAIN.unit_inference", {"src/solver.py": HEADER + "length_m = 4.0\n"}), {SIGNAL})


if __name__ == "__main__":
    unittest.main()
