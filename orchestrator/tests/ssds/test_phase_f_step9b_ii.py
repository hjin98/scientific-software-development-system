"""Phase F step 9b-ii: outcomes in §17.3's shape, and verdicts read through the declaration (catalogue §6.5, §17.3,
§17.4; plan §3.6, readings F83-F86).

The evaluated outcome is ``{output name: canonical value}``. A verdict on a failing output is read through the
declaration of the reading in force: an embedded verdict, a declared ``enum`` output, counts only under the reading the
execution ran; ``EXACT`` is recomputed from the stored outcome under any reading; every other template is not computable
until Q-F21, and a defective or unknown reading is not usable, so each yields the failure (fail closed). A passing
assessment under a defective specification is not admissible; a failing one still counts.
"""

from __future__ import annotations

import unittest

from ._scenario import HUMAN_B, Scenario, content, judgment, on_record
from .test_assessment import BAD, DECLARATION, GOOD, POLICY, SPEC, UNITS, Runs

DECLARATIVE = """oracle = "DECLARATIVE"
runner = "ci"
time_bound_hours = 24
outputs = [{ name = "x", type = "int" }, { name = "y", type = "float64", canonical = "decimal-shortest" },
           { name = "z", type = "bool" }]
verdicts = [{ output = "x", template = "EXACT", params = { reference = 2 } },
            { output = "y", template = "ABS_TOL", params = { reference = 0.0, tol = 0.5 } }]
"""


class Declared(Runs):
    def __init__(self, declaration: str) -> None:
        self.files = {"a.py": "v = 1\n", "s.py": SPEC, "s.ssds-spec.toml": declaration}
        self.sc = Scenario(UNITS, self.files, policy=POLICY)
        self.trees = {"T0": self.sc.head}
        self.completeness = {}

    def assessments(self):
        return self.sc.derive().a

    def assess(self, realization: dict, outcome: str, failing=("x",)) -> dict:
        view = self.sc.view(self.trees["T0"])
        fields = {"mode": "ORDINARY", "reading": {"unit": "spec", "rev": view.rev("spec")}}
        if failing:
            fields["failing_outputs"] = list(failing)
        a = judgment("EVIDENCE_ASSESSMENT", {"realization": realization["id"], "obligation": "obl"}, outcome,
                     actor=HUMAN_B, basis=[on_record(realization["id"]), content("spec", view.rev("spec"))], fields=fields)
        self.sc.admit(a)
        return a

    def revise(self, declaration: str) -> None:
        self.sc.absorb({"a.py": "v = 1\n", "s.py": SPEC, "s.ssds-spec.toml": declaration})


class Verdicts(unittest.TestCase):
    def test_an_embedded_verdict_counts_under_the_reading_it_ran(self) -> None:
        r = Declared(DECLARATION)
        t0 = r.tree("T0")
        failing = r.fail(r.run(t0, BAD))
        good, bad, missing = r.run(t0, GOOD), r.run(t0, BAD), r.run(t0, {"x_verdict": "PASS"})
        a = r.assessments()
        self.assertFalse(a.yields(good["id"], failing["id"]), "PASS under the reading it ran")
        self.assertTrue(a.yields(bad["id"], failing["id"]))
        self.assertTrue(a.yields(missing["id"], failing["id"]), "the output missing")
        r.revise(DECLARATION + "# a new revision of the reading\n")
        self.assertTrue(r.assessments().yields(good["id"], failing["id"]),
                        "under another reading an embedded verdict is not computable (§6.5)")

    def test_exact_is_recomputed_under_any_reading(self) -> None:
        r = Declared(DECLARATIVE)
        t0 = r.tree("T0")
        failing = r.fail(r.run(t0, {"x": 1, "y": "0.0"}))
        good, bad = r.run(t0, {"x": 2, "y": "0.0"}), r.run(t0, {"x": 1, "y": "0.0"})
        a = r.assessments()
        self.assertFalse(a.yields(good["id"], failing["id"]), "x equals EXACT's reference")
        self.assertTrue(a.yields(bad["id"], failing["id"]))
        r.revise(DECLARATIVE + "# a new revision of the reading\n")
        self.assertFalse(r.assessments().yields(good["id"], failing["id"]), "recomputed under the new reading")
        r.revise(DECLARATIVE.replace("reference = 2", "reference = 3"))
        self.assertTrue(r.assessments().yields(good["id"], failing["id"]), "the new reading's reference")

    def test_other_templates_and_unusable_readings_fail_closed(self) -> None:
        r = Declared(DECLARATIVE)
        t0 = r.tree("T0")
        failing = r.fail(r.run(t0, {"x": 1, "y": "9.0"}))
        failing_y = r.assess(r.run(t0, {"x": 1, "y": "9.0"}), "FAIL", failing=("y",))
        good = r.run(t0, {"x": 2, "y": "0.0"})
        self.assertTrue(r.assessments().yields(good["id"], failing_y["id"]), "ABS_TOL waits for Q-F21 (F86)")
        r.revise("oracle = \n")
        self.assertTrue(r.assessments().yields(good["id"], failing["id"]), "a defective reading")

    def test_the_judged_outputs_default_to_the_declared_verdicts(self) -> None:
        r = Declared(DECLARATIVE)
        t0 = r.tree("T0")
        unnamed = r.assess(r.run(t0, {"x": 1, "y": "0.0", "z": True}), "FAIL", failing=())  # z has no verdict
        good = r.run(t0, GOOD)
        self.assertEqual(r.assessments().failing_outputs(unnamed["id"]), ["x", "y"])
        self.assertEqual(r.assessments().restricted(good["id"], ["x", "z"]), {"x": 2, "z": None})


class Admissibility(unittest.TestCase):
    def test_a_defective_specification_admits_no_passing_assessment(self) -> None:
        r = Declared("oracle = \n")
        t0 = r.tree("T0")
        passing = r.assess(r.run(t0, GOOD), "PASS")
        failing = r.assess(r.run(t0, BAD), "FAIL")
        a = r.assessments()
        self.assertFalse(a.admissible(passing["id"], "obl"))
        self.assertTrue(a.admissible(failing["id"], "obl"), "failing evidence is never dropped (§6)")
        self.assertFalse(a.admissible(failing["id"], "other"))
        sound = Declared(DECLARATION)
        admitted = sound.assess(sound.run(sound.tree("T0"), GOOD), "PASS")
        self.assertTrue(sound.assessments().admissible(admitted["id"], "obl"))


if __name__ == "__main__":
    unittest.main()
