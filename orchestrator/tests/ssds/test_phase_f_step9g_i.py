"""Phase F step 9g-i: the numeric oracles, judged exactly (catalogue §6.5, §17.1, §17.3; SD-81, Q-F21 items 1-8; plan
reading F116).

``ABS_TOL``, ``REL_TOL``, ``ULP_TOL``, ``RANGE`` and ``MONOTONE`` are judged on exact rationals: an output's canonical
value exactly (a ``binary64-hex`` value its binary64, a decimal form its decimal), a declared parameter as the decimal
written. ``ULP_TOL`` reads binary64 values, its reference the binary64 nearest the decimal written. A NaN fails, equal
infinities pass only where the rules say, and a parameter outside the rules is a static error, never a runtime
``FAIL``. Expected values come from SD-81's items, never from the judge's output.
"""

from __future__ import annotations

import math
import sys
import unittest
from decimal import Decimal

from ssds.content import canonical_float, exact_of, judge, parse_spec
from ssds.content.spec import SpecDeclaration, SpecFailure

from .test_phase_f_step9b_ii import Declared

#: Exact decimals of binary64 values: the largest finite one, the smallest subnormal and the one nearest 0.1 (a
#: ``ULP_TOL`` reference is exactly a binary64 until Q-F28).
LARGEST, SMALLEST, TENTH = (str(Decimal(v)) for v in (sys.float_info.max, 5e-324, 0.1))
HEADER = 'oracle = "DECLARATIVE"\nrunner = "ci"\ntime_bound_hours = 24\n'


def spec(outputs: str, verdict: str) -> SpecDeclaration | SpecFailure:
    return parse_spec(f"{HEADER}outputs = [{outputs}]\nverdicts = [{verdict}]\n".encode())


def one(canonical: str, template: str, params: str, kind: str = "float64"):
    """A declaration of one output ``x`` with one verdict."""

    form = f', canonical = "{canonical}"' if kind == "float64" else ""
    return spec(f'{{ name = "x", type = "{kind}"{form} }}',
                f'{{ output = "x", template = "{template}", params = {{ {params} }} }}')


def verdict_on(declared: SpecDeclaration, values: dict[str, object]) -> bool | None:
    return judge(declared.verdict("x"), {o.name: o for o in declared.outputs}, values.get)


class Oracle(unittest.TestCase):
    def passes(self, declared, value) -> bool | None:
        self.assertIsInstance(declared, SpecDeclaration, declared)
        return verdict_on(declared, {"x": value})

    def static_error(self, declared) -> None:
        self.assertIsInstance(declared, SpecFailure, "a static error of the specification (item 5), not a FAIL")


class Formulas(Oracle):
    def test_abs_tol_inclusive(self) -> None:
        d = one("decimal-shortest", "ABS_TOL", "reference = 1.0, tol = 0.5")
        self.assertTrue(self.passes(d, "1.5"), "at the boundary: |x − r| ≤ t (item 1)")
        self.assertTrue(self.passes(d, "0.5"))
        self.assertFalse(self.passes(d, "1.5000000000000002"), "beside it")
        self.assertFalse(self.passes(d, "0.49999999999999994"))

    def test_rel_tol_relative_to_the_reference(self) -> None:
        d = one("decimal-shortest", "REL_TOL", "reference = -4.0, tol = 0.25")
        self.assertTrue(self.passes(d, "-5.0"), "|x − r| ≤ t·|r|, relative to r, not max(|x|, |r|) (item 1)")
        self.assertTrue(self.passes(d, "-3.0"))
        self.assertFalse(self.passes(d, "-5.000000000000001"))

    def test_rel_tol_with_a_zero_reference_is_exact_equality(self) -> None:
        d = one("decimal-shortest", "REL_TOL", "reference = 0.0, tol = 1.0")
        self.assertTrue(self.passes(d, "0.0"))
        self.assertTrue(self.passes(d, "-0.0"), "−0 and +0 are one rational")
        self.assertFalse(self.passes(d, "5e-324"))

    def test_an_int_output(self) -> None:
        d = one("", "ABS_TOL", "reference = 10, tol = 2", kind="int")
        self.assertTrue(self.passes(d, 12))
        self.assertFalse(self.passes(d, 13))
        self.assertFalse(self.passes(d, "12"), "not canonical: fails")


class Ulp(Oracle):
    def test_distance_at_and_beside_n(self) -> None:
        d = one("binary64-hex", "ULP_TOL", "reference = 1.0, n = 2")
        self.assertTrue(self.passes(d, canonical_float("binary64-hex", math.nextafter(math.nextafter(1.0, 2), 2))))
        self.assertFalse(self.passes(d, canonical_float("binary64-hex", 1.0000000000000007)), "three ULP")
        self.assertTrue(self.passes(d, canonical_float("binary64-hex", math.nextafter(1.0, 0))), "below, one ULP")

    def test_across_zero(self) -> None:
        d = one("decimal-shortest", "ULP_TOL", f"reference = {SMALLEST}, n = 2")
        self.assertTrue(self.passes(d, "-5e-324"), "+0 and −0 one point: the distance is 2 (item 2)")
        self.assertTrue(self.passes(one("decimal-shortest", "ULP_TOL", "reference = 0.0, n = 0"), "-0.0"))
        self.assertFalse(self.passes(one("decimal-shortest", "ULP_TOL", f"reference = {SMALLEST}, n = 1"), "-5e-324"))

    def test_at_the_largest_finite_value(self) -> None:
        d = one("decimal-shortest", "ULP_TOL", f"reference = {LARGEST}, n = 1")
        self.assertTrue(self.passes(d, "1.7976931348623155e+308"))
        self.assertFalse(self.passes(one("decimal-shortest", "ULP_TOL", f"reference = {LARGEST}, n = 1000"), "inf"),
                         "+∞ is never within n ULP of the largest finite value (item 3)")

    def test_a_decimal_shortest_output_is_read_as_its_binary64(self) -> None:
        d = one("decimal-shortest", "ULP_TOL", f"reference = {TENTH}, n = 0")
        self.assertTrue(self.passes(d, "0.1"), "the output denotes the binary64 the reference is exactly (item 6)")
        e = one("decimal-shortest", "ABS_TOL", f"reference = {TENTH}, tol = 0.0")
        self.assertFalse(self.passes(e, "0.1"), "under ABS_TOL the decimal values differ (item 6)")


class NonFinite(Oracle):
    def test_nan_either_side_and_infinities(self) -> None:
        for template, params in (("ABS_TOL", "reference = 0.0, tol = 1e300"),
                                 ("REL_TOL", "reference = 1.0, tol = 1e300"),
                                 ("ULP_TOL", "reference = 0.0, n = 9007199254740992")):
            d = one("decimal-shortest", template, params)
            with self.subTest(template):
                self.assertFalse(self.passes(d, "nan"), "a NaN fails (item 3)")
                self.assertFalse(self.passes(d, "inf"), "any other infinity fails")
                self.assertFalse(self.passes(d, "-inf"))
                self.assertFalse(self.passes(d, None), "the output missing")

    def test_rounded_non_finite(self) -> None:
        d = one("rounded:3", "ABS_TOL", "reference = 0.0, tol = 1e300")
        self.assertFalse(self.passes(d, "Infinity"))
        self.assertFalse(self.passes(d, "NaN"))
        self.assertTrue(self.passes(d, "-0.00e+0"))


class Exactness(Oracle):
    def test_no_overflow(self) -> None:
        d = one("decimal-shortest", "REL_TOL", "reference = 1e308, tol = 2")
        self.assertTrue(self.passes(d, "-1e+308"), "1e308 − (−1e308) = 2e308, exactly at t·|r| (item 4)")
        self.assertFalse(self.passes(d, "-1.0000000000000002e+308"),
                         "beside it: binary64 arithmetic would compare ∞ ≤ ∞ and pass")

    def test_a_tolerance_read_as_written(self) -> None:
        self.assertTrue(self.passes(one("decimal-shortest", "ABS_TOL", "reference = 0.0, tol = 1e-8"), "1e-08"),
                        "the decimal 10⁻⁸ against the tolerance 10⁻⁸ written (items 6 and 7)")
        x = canonical_float("binary64-hex", 1e-8)
        self.assertFalse(self.passes(one("binary64-hex", "ABS_TOL", "reference = 0.0, tol = 1e-8"), x),
                         "the binary64 nearest 10⁻⁸ exceeds it; binary64 parameters would pass it")

    def test_rounded_outputs_are_their_decimals(self) -> None:
        d = one("rounded:3", "ABS_TOL", "reference = 0.0, tol = 1e-8")
        self.assertTrue(self.passes(d, "1.00e-8"))
        self.assertFalse(self.passes(d, "1.01e-8"))
        self.assertEqual(exact_of(d.output("x"), "6.67e-1"), exact_of(d.output("x"), "6.67e-1"))
        self.assertIsNone(exact_of(d.output("x"), "0.667"), "not canonical")


class Range(Oracle):
    def test_bounds_inclusive_and_open(self) -> None:
        d = one("decimal-shortest", "RANGE", "lo = 0.0, hi = 1.0")
        self.assertTrue(self.passes(d, "0.0"))
        self.assertTrue(self.passes(d, "1.0"))
        self.assertFalse(self.passes(d, "1.0000000000000002"))
        open_hi = one("decimal-shortest", "RANGE", "lo = 0.0")
        self.assertTrue(self.passes(open_hi, "1e+300"))
        self.assertFalse(self.passes(open_hi, "inf"), "an overflow never passes an open bound (item 8)")
        self.assertFalse(self.passes(open_hi, "nan"))
        self.assertFalse(self.passes(open_hi, "-5e-324"))

    def test_a_declared_infinite_bound(self) -> None:
        d = one("decimal-shortest", "RANGE", "lo = -inf, hi = inf")
        self.assertTrue(self.passes(d, "inf"), "a matching declared infinity passes (item 8)")
        self.assertTrue(self.passes(d, "-inf"))
        self.assertTrue(self.passes(d, "0.0"))
        self.assertFalse(self.passes(d, "nan"))
        self.assertFalse(self.passes(one("decimal-shortest", "RANGE", "lo = 0.0, hi = inf"), "-inf"),
                         "only the bound on that side")


class Monotone(Oracle):
    def ordered(self, order: str, a: str, b: str, c: str | None = None) -> bool | None:
        names = ["x", "y"] + (["z"] if c is not None else [])
        outputs = ", ".join(f'{{ name = "{n}", type = "float64", canonical = "decimal-shortest" }}' for n in names)
        d = spec(outputs, f'{{ output = "x", template = "MONOTONE", params = {{ outputs = {names!r}, '
                          f'order = "{order}" }} }}'.replace("'", '"'))
        self.assertIsInstance(d, SpecDeclaration, d)
        return verdict_on(d, dict(zip(names, [a, b, c])))

    def test_the_orders(self) -> None:
        self.assertTrue(self.ordered("INCREASING", "1.0", "2.0", "inf"))
        self.assertFalse(self.ordered("INCREASING", "1.0", "1.0"), "strict")
        self.assertTrue(self.ordered("NON_DECREASING", "1.0", "1.0", "2.0"))
        self.assertFalse(self.ordered("NON_DECREASING", "2.0", "1.0"))
        self.assertTrue(self.ordered("DECREASING", "inf", "1.0", "-inf"))
        self.assertTrue(self.ordered("NON_INCREASING", "1.0", "1.0"))
        self.assertFalse(self.ordered("DECREASING", "1.0", "1.0"))

    def test_infinities_nan_and_signed_zeros(self) -> None:
        self.assertTrue(self.ordered("NON_DECREASING", "inf", "inf"), "equal infinities: non-strict (item 8)")
        self.assertFalse(self.ordered("INCREASING", "inf", "inf"))
        self.assertFalse(self.ordered("NON_DECREASING", "1.0", "nan"), "a NaN fails")
        self.assertFalse(self.ordered("NON_INCREASING", "nan", "nan"))
        self.assertTrue(self.ordered("NON_DECREASING", "-0.0", "0.0"), "−0 and +0 are equal")
        self.assertTrue(self.ordered("NON_INCREASING", "0.0", "-0.0"))
        self.assertFalse(self.ordered("INCREASING", "-0.0", "0.0"))
        self.assertFalse(self.ordered("INCREASING", "1.0", None), "an output missing")


class StaticErrors(Oracle):
    def test_parameters_outside_the_rules(self) -> None:
        for template, params, canonical in (
                ("ABS_TOL", "reference = 0.0, tol = -1e-9", "decimal-shortest"),
                ("ABS_TOL", "reference = 0.0, tol = inf", "decimal-shortest"),
                ("ABS_TOL", "reference = 0.0, tol = nan", "decimal-shortest"),
                ("ABS_TOL", "reference = nan, tol = 1.0", "decimal-shortest"),
                ("ABS_TOL", "reference = inf, tol = 1.0", "decimal-shortest"),
                ("REL_TOL", "reference = -inf, tol = 1.0", "decimal-shortest"),
                ("ULP_TOL", "reference = inf, n = 1", "decimal-shortest"),
                ("ULP_TOL", "reference = 1.0, n = -1", "decimal-shortest"),
                ("ULP_TOL", "reference = 1.0, n = 1.5", "decimal-shortest"),
                ("ULP_TOL", "reference = 1.0, n = 1", "rounded:3"),
                ("RANGE", "lo = 1.0, hi = 0.0", "decimal-shortest"),
                ("RANGE", "lo = 0.10000000000000000001, hi = 0.1", "decimal-shortest"),
                ("RANGE", "lo = nan", "decimal-shortest"),
                ("EXACT", "reference = nan", "decimal-shortest")):
            with self.subTest(template=template, params=params):
                self.static_error(one(canonical, template, params))
        self.static_error(one("", "ULP_TOL", "reference = 1, n = 1", kind="int"))

    def test_monotone_with_fewer_than_two(self) -> None:
        self.static_error(spec('{ name = "x", type = "int" }', '{ output = "x", template = "MONOTONE", '
                                                                 'params = { outputs = ["x"], order = "INCREASING" } }'))

    def test_a_ulp_reference_not_exactly_a_binary64(self) -> None:
        self.static_error(one("decimal-shortest", "ULP_TOL", "reference = 0.1, n = 0"))  # until Q-F28 (F116)
        self.static_error(one("decimal-shortest", "ULP_TOL", "reference = 1.7976931348623157e308, n = 0"))
        self.assertIsInstance(one("decimal-shortest", "ULP_TOL", f"reference = {TENTH}, n = 0"), SpecDeclaration)
        self.assertIsInstance(one("decimal-shortest", "ULP_TOL", "reference = 0.5, n = 0"), SpecDeclaration)

    def test_lo_below_hi_exactly(self) -> None:
        self.assertIsInstance(one("decimal-shortest", "RANGE", "lo = 0.1, hi = 0.10000000000000000001"),
                              SpecDeclaration, "lo < hi exactly, though their binary64 values are equal")


TOLERANCE = """oracle = "DECLARATIVE"
runner = "ci"
time_bound_hours = 24
outputs = [{ name = "x", type = "int" }, { name = "y", type = "float64", canonical = "decimal-shortest" },
           { name = "z", type = "float64", canonical = "decimal-shortest" }]
verdicts = [{ output = "x", template = "EXACT", params = { reference = 2 } },
            { output = "y", template = "ABS_TOL", params = { reference = 0.0, tol = 0.5 } },
            { output = "z", template = "MONOTONE", params = { outputs = ["y", "z"], order = "NON_DECREASING" } }]
"""


class Staleness(unittest.TestCase):
    """A failure goes stale where a passing tolerance verdict judges what it found failing (§6.5; F116)."""

    def test_a_failure_stale_under_a_passing_tolerance_verdict(self) -> None:
        r = Declared(TOLERANCE)
        t0 = r.tree("T0")
        failing = r.assess(r.run(t0, {"x": 2, "y": "9.0", "z": "9.0"}), "FAIL", failing=("y",))
        at, beyond = r.run(t0, {"x": 2, "y": "-0.5", "z": "1.0"}), r.run(t0, {"x": 2, "y": "0.5000000000000001",
                                                                                "z": "1.0"})
        a = r.assessments()
        self.assertFalse(a.yields(at["id"], failing["id"]), "within the tolerance, at its boundary: stale")
        self.assertTrue(a.yields(beyond["id"], failing["id"]))
        r.revise(TOLERANCE.replace("tol = 0.5", "tol = 0.25"))
        self.assertTrue(r.assessments().yields(at["id"], failing["id"]), "the new reading's tolerance")

    def test_monotone_through_derivation(self) -> None:
        r = Declared(TOLERANCE)
        t0 = r.tree("T0")
        failing = r.assess(r.run(t0, {"x": 2, "y": "0.0", "z": "-1.0"}), "FAIL", failing=("z",))
        good, equal, bad = (r.run(t0, {"x": 2, "y": "0.0", "z": z}) for z in ("1.0", "-0.0", "-1.0"))
        a = r.assessments()
        self.assertFalse(a.yields(good["id"], failing["id"]))
        self.assertFalse(a.yields(equal["id"], failing["id"]), "−0 equals +0 under NON_DECREASING")
        self.assertTrue(a.yields(bad["id"], failing["id"]))

    def test_a_renamed_output_is_judged_on_the_value_the_run_stored(self) -> None:
        r = Declared(TOLERANCE)
        t0 = r.tree("T0")
        failing = r.assess(r.run(t0, {"x": 2, "y": "9.0", "z": "9.0"}), "FAIL", failing=("y",))
        good = r.run(t0, {"x": 2, "y": "0.25", "z": "1.0"})
        r.revise(TOLERANCE.replace('name = "y"', 'name = "y2"').replace('output = "y"', 'output = "y2"')
                 .replace('["y", "z"]', '["y2", "z"]') + 'output_renames = { y = "y2" }\n')
        self.assertFalse(r.assessments().yields(good["id"], failing["id"]),
                         "the reading's y2 is the run's y (§6.5; F94): within the tolerance")


if __name__ == "__main__":
    unittest.main()
