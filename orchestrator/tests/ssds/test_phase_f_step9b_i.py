"""Phase F step 9b-i: the specification declaration, canonical values and the specification lint (catalogue §17.1,
§17.3, §6.5, §6.9; plan §3.6, readings F79, F84, F86; plan checks of db0bf1ce and 93ead500).

One closed parser reads exactly one declaration per ``EVIDENCE_SPEC`` unit, from a fenced ``ssds-spec`` block or a
``*.ssds-spec.toml`` file; anything else is a static error that makes the specification defective. Outputs are
§17.3's scalar forms, an embedded verdict an ``enum`` output (``PASS``, ``FAIL``), and a declarative verdict one of the
seven templates with its parameters' obvious constraints checked now. Lint reports a defective specification, a runner
class policy does not designate, a Dispatcher class's bound above 168 h and a fixed attribute the class does not
record.
"""

from __future__ import annotations

import math
import unittest

from ssds.content import canonical_float, canonical_reference, float_of, is_canonical, parse_spec
from ssds.content.spec import Output, SpecDeclaration, SpecFailure

from ._scenario import Scenario

EMBEDDED = '''oracle = "EMBEDDED"
runner = "ci"
time_bound_hours = 24
outputs = [{ name = "x", type = "float64", canonical = "decimal-shortest" },
           { name = "x_verdict", type = "enum", values = ["PASS", "FAIL"] }]
verdicts = [{ output = "x", embedded = "x_verdict" }]
'''
DECLARATIVE = '''oracle = "DECLARATIVE"
runner = "ci"
time_bound_hours = 24
outputs = [{ name = "l2", type = "float64", canonical = "binary64-hex" }, { name = "a", type = "int" },
           { name = "b", type = "int" }, { name = "ok", type = "bool" }]
verdicts = [{ output = "l2", template = "ABS_TOL", params = { reference = 0.0, tol = 1e-8 } },
            { output = "a", template = "MONOTONE", params = { outputs = ["a", "b"], order = "INCREASING" } },
            { output = "ok", template = "EXACT", params = { reference = true } }]
fixed = { regime = "re<2000" }
granularity = { mode = "ENSEMBLE", replicates = 32, statistic = "mean_and_ci95", seed_policy = "FIXED_SEQUENCE" }
'''


def declared(text: str):
    return parse_spec(text.encode())


def with_line(base: str, old: str, new: str) -> str:
    assert old in base, old
    return base.replace(old, new, 1)


class Grammar(unittest.TestCase):
    def test_the_three_oracles(self) -> None:
        embedded = declared(EMBEDDED)
        self.assertIsInstance(embedded, SpecDeclaration)
        self.assertEqual(embedded.verdict("x").embedded, "x_verdict")
        decl = declared(DECLARATIVE)
        self.assertIsInstance(decl, SpecDeclaration)
        self.assertEqual((decl.verdict("l2").template, decl.granularity["replicates"]), ("ABS_TOL", 32))
        reader = declared('oracle = "ASSESSOR_READ"\nrunner = "ci"\ntime_bound_hours = 1\n'
                          'outputs = [{ name = "report", type = "digest" }]\n')
        self.assertEqual((reader.verdicts, reader.granularity), ((), {"mode": "SINGLE"}))

    def test_refusals(self) -> None:
        cases = {
            "unknown key": EMBEDDED + "extra = 1\n",
            "missing key": with_line(EMBEDDED, 'runner = "ci"\n', ""),
            "unknown oracle": with_line(EMBEDDED, '"EMBEDDED"', '"ORACULAR"'),
            "empty runner": with_line(EMBEDDED, 'runner = "ci"', 'runner = ""'),
            "zero bound": with_line(EMBEDDED, "time_bound_hours = 24", "time_bound_hours = 0"),
            "infinite bound": with_line(EMBEDDED, "time_bound_hours = 24", "time_bound_hours = inf"),
            "no outputs": with_line(DECLARATIVE, DECLARATIVE[DECLARATIVE.index("outputs"):DECLARATIVE.index("verdicts")],
                                    "outputs = []\n"),
            "repeated output": with_line(EMBEDDED, '{ name = "x_verdict"', '{ name = "x"'),
            "unknown type": with_line(DECLARATIVE, '{ name = "a", type = "int" }', '{ name = "a", type = "float32" }'),
            "float without a form": with_line(EMBEDDED, ', canonical = "decimal-shortest"', ""),
            "unknown form": with_line(EMBEDDED, '"decimal-shortest"', '"decimal-long"'),
            "rounded:0": with_line(EMBEDDED, '"decimal-shortest"', '"rounded:0"'),
            "a canonical on an int": with_line(DECLARATIVE, '{ name = "a", type = "int" }',
                                              '{ name = "a", type = "int", canonical = "binary64-hex" }'),
            "an empty enum": with_line(EMBEDDED, 'values = ["PASS", "FAIL"]', "values = []"),
            "verdicts on an assessor read": with_line(EMBEDDED, '"EMBEDDED"', '"ASSESSOR_READ"'),
            "no verdicts": with_line(EMBEDDED, 'verdicts = [{ output = "x", embedded = "x_verdict" }]\n', ""),
            "an undeclared output": with_line(EMBEDDED, '{ output = "x",', '{ output = "y",'),
            "a carrier not PASS/FAIL": with_line(EMBEDDED, 'values = ["PASS", "FAIL"]', 'values = ["OK", "FAIL"]'),
            "an unknown template": with_line(DECLARATIVE, 'template = "EXACT"', 'template = "CLOSE"'),
            "a negative tolerance": with_line(DECLARATIVE, "tol = 1e-8", "tol = -1e-8"),
            "an infinite tolerance": with_line(DECLARATIVE, "tol = 1e-8", "tol = inf"),
            "lo above hi": with_line(DECLARATIVE, 'template = "ABS_TOL", params = { reference = 0.0, tol = 1e-8 }',
                                     'template = "RANGE", params = { lo = 1.0, hi = 0.0 }'),
            "a range with no bound": with_line(DECLARATIVE,
                                               'template = "ABS_TOL", params = { reference = 0.0, tol = 1e-8 }',
                                               'template = "RANGE", params = {}'),
            "a non-integer n": with_line(DECLARATIVE, 'template = "ABS_TOL", params = { reference = 0.0, tol = 1e-8 }',
                                         'template = "ULP_TOL", params = { reference = 0.0, n = 1.5 }'),
            "MONOTONE over one output": with_line(DECLARATIVE, 'outputs = ["a", "b"]', 'outputs = ["a"]'),
            "MONOTONE over an undeclared output": with_line(DECLARATIVE, 'outputs = ["a", "b"]', 'outputs = ["a", "c"]'),
            "MONOTONE over a non-numeric output": with_line(DECLARATIVE, 'outputs = ["a", "b"]', 'outputs = ["a", "ok"]'),
            "an unknown order": with_line(DECLARATIVE, '"INCREASING"', '"UPWARD"'),
            "an EXACT reference of another type": with_line(DECLARATIVE, "reference = true", 'reference = "true"'),
            "a non-string fixed value": with_line(DECLARATIVE, 'regime = "re<2000"', "regime = 2000"),
            "a rename to an undeclared output": DECLARATIVE + 'output_renames = { old = "new" }\n',
            "a one-replicate ensemble": with_line(DECLARATIVE, "replicates = 32", "replicates = 1"),
            "two verdicts on one output": with_line(EMBEDDED, 'verdicts = [{ output = "x", embedded = "x_verdict" }]',
                                                    'verdicts = [{ output = "x", embedded = "x_verdict" }, '
                                                    '{ output = "x", embedded = "x_verdict" }]'),
            "not TOML": "oracle = \n",
        }
        for name, text in cases.items():
            with self.subTest(case=name):
                self.assertIsInstance(declared(text), SpecFailure)

    def test_ulp_on_a_rounded_output_and_an_exact_reference_under_rounding(self) -> None:
        rounded = with_line(DECLARATIVE, '{ name = "l2", type = "float64", canonical = "binary64-hex" }',
                            '{ name = "l2", type = "float64", canonical = "rounded:3" }')
        self.assertIsInstance(declared(with_line(rounded, 'template = "ABS_TOL", params = { reference = 0.0, tol = 1e-8 }',
                                                 'template = "ULP_TOL", params = { reference = 0.0, n = 1 }')),
                              SpecFailure)
        exact = with_line(rounded, 'template = "ABS_TOL", params = { reference = 0.0, tol = 1e-8 }',
                          'template = "EXACT", params = { reference = %s }')
        self.assertIsInstance(declared(exact % '"6.67e-1"'), SpecDeclaration, "already canonical")
        for reference in ("0.667", '"0.667"', '"6.670e-1"'):
            with self.subTest(reference=reference):
                self.assertIsInstance(declared(exact % reference), SpecFailure, "not canonical under rounded:3")


class Canonical(unittest.TestCase):
    def test_the_float_forms(self) -> None:
        self.assertEqual(canonical_float("binary64-hex", 1.0), "0x3ff0000000000000")
        self.assertEqual(canonical_float("binary64-hex", -0.0), "0x8000000000000000")
        self.assertEqual(canonical_float("decimal-shortest", 0.1), "0.1")
        self.assertEqual(canonical_float("rounded:3", 2 / 3), "6.67e-1")
        self.assertEqual(canonical_float("rounded:1", 2.5), "2e+0", "half-even")
        self.assertEqual(canonical_float("rounded:2", math.inf), "Infinity")
        for form, value in (("binary64-hex", 1e-300), ("decimal-shortest", 1 / 3), ("rounded:4", 12345.678)):
            with self.subTest(form=form):
                text = canonical_float(form, value)
                self.assertEqual(canonical_float(form, float_of(form, text)), text, "a fixed point")
        self.assertIsNone(float_of("decimal-shortest", "0.10"), "not the shortest")
        self.assertIsNone(float_of("binary64-hex", "0x3FF0000000000000"), "lower case only")
        self.assertIsNone(float_of("rounded:3", "0.667"))

    def test_each_type(self) -> None:
        cases = [(Output("f", "float64", "decimal-shortest"), "1e-08", 1e-8),
                 (Output("i", "int"), 3, True), (Output("b", "bool"), False, 0),
                 (Output("e", "enum", values=("A", "B")), "A", "C"),
                 (Output("d", "digest"), "sha256:" + "a" * 64, "sha256:A")]
        for output, good, bad in cases:
            with self.subTest(type=output.type):
                self.assertTrue(is_canonical(output, good))
                self.assertFalse(is_canonical(output, bad))
        self.assertEqual(canonical_reference(Output("f", "float64", "binary64-hex"), 1), "0x3ff0000000000000")


SPECS = '''
    [[unit]]
    id = "claim"
    kind = "D2"
    scope = [{ path = "claim.md" }]
    [[unit]]
    id = "spec"
    kind = "EVIDENCE_SPEC"
    scope = [{ path = "spec.md" }]
    [[unit]]
    id = "case"
    kind = "EVIDENCE_SPEC"
    scope = [{ path = "case.ssds-spec.toml" }]
'''
DISPATCHER = '[runners.ci]\nkind = "DISPATCHER"\nkeys = ["ed25519:a"]\nattributes = ["regime"]\n' \
             'observes_outside_reads = true\n'


def block(text: str) -> str:
    return f"# Spec\n\n```ssds-spec\n{text}```\n"


class Declarations(unittest.TestCase):
    def specs(self, spec_md: str, case: str = EMBEDDED, policy: str = "schema = 1\n" + DISPATCHER):
        sc = Scenario(SPECS, {"claim.md": "c\n", "spec.md": spec_md, "case.ssds-spec.toml": case}, policy=policy)
        return sc, sc.derive().s.specs

    def test_a_block_and_a_file(self) -> None:
        _, specs = self.specs(block(EMBEDDED))
        self.assertEqual(specs.units, ("case", "spec"))
        self.assertIsInstance(specs.declaration("spec"), SpecDeclaration)
        self.assertIsInstance(specs.declaration("case"), SpecDeclaration)
        self.assertEqual(specs.lint, {})

    def test_none_or_two_is_defective(self) -> None:
        for name, text, code in (("none", "# Spec\n\nprose\n", "MISSING"),
                                 ("two", block(EMBEDDED) + block(EMBEDDED), "BLOCKS"),
                                 ("bad", block(EMBEDDED + "extra = 1\n"), "GRAMMAR")):
            with self.subTest(case=name):
                _, specs = self.specs(text)
                self.assertTrue(specs.defective("spec"))
                ((finding,),) = [specs.lint["spec"]]
                self.assertEqual(finding.code, "SPEC")
                self.assertTrue(finding.detail.startswith(code))
        _, specs = self.specs(block(EMBEDDED))
        self.assertFalse(specs.defective("spec"))

    def test_lint_against_policy(self) -> None:
        _, specs = self.specs(block(EMBEDDED), policy="schema = 1\n")
        self.assertEqual({f.code for f in specs.lint["spec"]}, {"RUNNER"})
        bounded = with_line(DECLARATIVE, "time_bound_hours = 24", "time_bound_hours = 200")
        bounded = with_line(bounded, 'fixed = { regime = "re<2000" }', 'fixed = { regime = "re<2000", backend = "gpu" }')
        _, specs = self.specs(block(bounded))
        self.assertEqual({(f.code, f.detail.split()[0]) for f in specs.lint["spec"]},
                         {("BOUND", "a"), ("FIXED", "fixed")})
        custody = DISPATCHER.replace('"DISPATCHER"', '"EXTERNAL_CUSTODY"').replace('["regime"]', '["regime", "backend"]')
        _, specs = self.specs(block(bounded), policy="schema = 1\n" + custody)
        self.assertNotIn("spec", specs.lint, "an external custody class is bounded by its declaration alone")

    def test_an_earlier_revisions_declaration(self) -> None:
        sc, specs = self.specs(block(EMBEDDED))
        old = sc.rev("spec")
        sc.absorb({"claim.md": "c\n", "spec.md": block(DECLARATIVE), "case.ssds-spec.toml": EMBEDDED})
        specs = sc.derive().s.specs
        self.assertEqual(specs.declaration("spec").oracle, "DECLARATIVE")
        self.assertEqual(specs.declaration_at("spec", old).oracle, "EMBEDDED")
        self.assertIsNone(specs.declaration_at("spec", "sha256:" + "0" * 64))
        self.assertTrue(specs.defective("spec", "sha256:" + "0" * 64), "an unknown revision is not usable")


if __name__ == "__main__":
    unittest.main()
