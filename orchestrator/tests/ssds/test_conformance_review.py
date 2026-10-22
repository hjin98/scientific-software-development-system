"""Regression cases from the independent review of Phase E step 4 (conformance): B1, B3-B13 and SC-1's fail-closed
half. Each case is a counterexample the review executed against the earlier code; the expected class is §14.4's.
"""

from __future__ import annotations

import unittest

from ssds.derivation.conformance import CLEAN, DISCREPANCY, INCOMPLETE, VIOLATION
from ssds.derivation.workflow import DISCHARGED, Workflow
from ssds.ledger.read import with_id

from ._fixtures import record
from ._scenario import OWNER, agent, content, fresh, judgment
from .test_conformance import SECONDARY, SLOTS, accepted_plan, conformance, realize, submit
from .test_conformance_python import TEST_FILE, classes_of
from .test_lint import item_block

FROZEN = item_block(secondary=SECONDARY).replace("dependencies = ", 'frozen = ["src.solver.step"]\ndependencies = ')


def run(files: dict[str, str], block: str | None = None, slots: dict | None = None, base: dict | None = None,
        policy_extra: str | None = None):
    sc = accepted_plan(block or item_block(secondary=SECONDARY))
    if base:
        sc.absorb(base)
    _, cand, result = submit(sc, files, slots=slots, outcome="PARTIAL")
    realize(sc, cand)
    return conformance(sc, result)[1]


def classes(c, template: str) -> set[str]:
    found = {h.cls for h in c.hits if h.template == template}
    return found - {CLEAN} if found - {CLEAN} else found


class ContractBoundariesAlwaysRun(unittest.TestCase):
    """B1: the contract's frozen interface, the D4 test-integrity minimum and the expectations run unnamed."""

    def test_frozen_tests_and_artifacts(self) -> None:
        c = run({"src/solver.py": "def step(scale):\n    return scale\n"}, FROZEN)
        self.assertEqual(classes(c, "BOUNDARY.frozen_interface"), {VIOLATION})
        deleted = TEST_FILE.replace("    def test_io(self):\n        assert solver.step() == 1\n", "")
        c = run({"src/test_solver.py": deleted}, base={"src/test_solver.py": TEST_FILE})
        self.assertEqual(classes(c, "TEST_INTEGRITY.no_deletions"), {VIOLATION})
        block = item_block(secondary=SECONDARY).replace("[contract.expectations]", '[contract.expectations]\nartifacts = ["src/timestep.py"]')
        c = run({"src/solver.py": "def step():\n    return 2\n"}, block)
        self.assertEqual(classes(c, "OBLIGATION.required_artifact"), {INCOMPLETE})


class Disclosure(unittest.TestCase):
    """B3: §14.4, an undisclosed breach is both VIOLATION and DISCREPANCY; a disclosed one is not discrepant."""

    def test_any_boundary_breach(self) -> None:
        breach = {"src/solver.py": "def step(scale):\n    return scale\n"}
        self.assertEqual(run(breach, FROZEN).classes & {VIOLATION, DISCREPANCY}, {VIOLATION, DISCREPANCY})
        disclosed = dict(SLOTS, deviations=[{"unit": "src", "reason": "SCOPE_DEVIATION"}])
        self.assertEqual(run(breach, FROZEN, slots=disclosed).classes & {VIOLATION, DISCREPANCY}, {VIOLATION})


class MissingFrame(unittest.TestCase):
    def test_a_named_transformation_without_a_frame_is_incomplete(self) -> None:
        # B4: no candidate or base, so no frame: nothing about the candidate is CLEAN, and REVIEW(X) is not ready
        sc = accepted_plan()
        x = "sha256:" + "9" * 64
        result = record("TASK_RESULT", target={"task": "task-1", "transformation": x}, outcome="COMPLETE",
                        actor=agent("maker"), actor_class="AGENT", frame={"transformation": x}, fields={"slots": SLOTS})
        result["binding"] = dict(fresh(agent("maker"), "task-1"), obligation="obl",
                                 item={"unit": "plan.work.item", "rev": sc.rev("plan.work.item")})
        result = with_id(result)
        sc.admit(result)
        w = Workflow(sc.derive())
        self.assertIn(INCOMPLETE, w.conformance(result["id"]).classes)
        self.assertEqual(w.of_kind("REVIEW"), [])


class UnanalyzedSurfaces(unittest.TestCase):
    """B5, B6: what the Python test analysis cannot judge fails closed."""

    def test_python_skip_forms(self) -> None:
        base = {"src/test_solver.py": TEST_FILE}
        forms = {
            "skipif": TEST_FILE.replace("    def test_io(self):", "    @pytest.mark.skipif(True, reason='x')\n    def test_io(self):"),
            "pytestmark": "import pytest\npytestmark = pytest.mark.skip\n" + TEST_FILE,
            "importorskip": TEST_FILE.replace("        assert solver.step() == 1\n", "        pytest.importorskip('nope')\n"),
            "raise SkipTest": TEST_FILE.replace("        assert solver.step() == 1\n", "        raise unittest.SkipTest('x')\n"),
        }
        for name, text in forms.items():
            with self.subTest(form=name):
                self.assertEqual(classes_of("TEST_INTEGRITY.no_skips", {"src/test_solver.py": text}, base=base), {VIOLATION})
        shadowed = TEST_FILE + "\n    def test_io(self):\n        pass\n"
        self.assertEqual(classes_of("TEST_INTEGRITY.no_deletions", {"src/test_solver.py": shadowed}, base=base), {VIOLATION})
        hidden = "__test__ = False\n" + TEST_FILE
        self.assertEqual(classes_of("TEST_INTEGRITY.no_deletions", {"src/test_solver.py": hidden}, base=base), {VIOLATION})
        self.assertEqual(classes_of("TEST_INTEGRITY.no_deletions", {"src/conftest.py": "collect_ignore_glob = ['*']\n"}),
                         {VIOLATION}, "test-collection configuration")

    def test_other_languages(self) -> None:
        base = {"src/tests/test_kernel.cpp": "TEST(K, A) { EXPECT_EQ(1, 1); }\nTEST(K, B) { EXPECT_EQ(2, 2); }\n"}
        self.assertEqual(classes_of("TEST_INTEGRITY.no_deletions", {"src/tests/test_kernel.cpp": "TEST(K, A) { EXPECT_EQ(1, 1); }\n"},
                                    base=base), {VIOLATION})
        self.assertEqual(classes_of("OBLIGATION.no_new_stubs", {"src/kernel.cpp": "int f() { return 0; }\n"}), {INCOMPLETE})
        self.assertEqual(classes_of("DOMAIN.dimensional_consistency", {"src/kernel.cpp": "// ssds:unit dt = s\ndouble dt;\n"}),
                         {INCOMPLETE})


class Dependencies(unittest.TestCase):
    """B7: requirement forms the analyzer cannot check, and more manifests."""

    def test_forms(self) -> None:
        template = "BOUNDARY.dependency_allowance"
        base = {"src/requirements.txt": "numpy>=1.20\n"}
        self.assertEqual(classes_of(template, {"src/requirements.txt": "numpy>=1.20\n-r extra.txt\n"}, base=base), {VIOLATION})
        self.assertEqual(classes_of(template, {"src/requirements.txt": "numpy>=1.20\n-e git+https://example.invalid/x\n"},
                                    base=base), {VIOLATION})
        for path in ("src/requirements/dev.txt", "src/dev-requirements.txt", "src/constraints.txt"):
            with self.subTest(path=path):
                self.assertEqual(classes_of(template, {path: "evilpkg\n"}), {VIOLATION})
        poetry = '[tool.poetry.dependencies]\npython = "^3.11"\nevilpkg = "*"\n'
        self.assertEqual(classes_of(template, {"src/pyproject.toml": poetry}), {VIOLATION})
        build = '[build-system]\nrequires = ["evilpkg"]\n'
        self.assertEqual(classes_of(template, {"src/pyproject.toml": build}), {VIOLATION})


class ProtectedAndUncovered(unittest.TestCase):
    def test_a_protected_path_owned_by_no_unit(self) -> None:
        # B8: the policy file is protected whether or not a unit owns it (§25.3)
        c = run({".ssds/policy.toml": "schema = 1\n"})
        self.assertEqual(classes(c, "BOUNDARY.protected_surfaces"), {VIOLATION})

    def test_content_owned_by_no_unit_outside_the_write_scope(self) -> None:
        # SC-1's fail-closed half: §12.3 limits a write to the write scope even where the write set cannot see it
        for path in ("evil.py", "README.md", ".github/workflows/ci.yml"):
            with self.subTest(path=path):
                c = run({"src/solver.py": "def step():\n    return 2\n", path: "x = 1\n"})
                self.assertEqual(classes(c, "BOUNDARY.write_scope"), {VIOLATION})


class Runner(unittest.TestCase):
    """B9: any current failing observation fails; a HARD template never yields SIGNAL."""

    def observe(self, outcomes: list[str]) -> set[str]:
        secondary = SECONDARY[:-2] + ', { check = "OBLIGATION.mutation_strength" } ]'
        sc = accepted_plan(item_block(secondary=secondary))
        _, cand, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"}, outcome="PARTIAL")
        realize(sc, cand)
        for outcome in outcomes:
            for ob in ("o1", "o2"):
                sc.admit(with_id(record("CHECK_EXECUTION", target={"obligation": ob, "candidate": cand}, outcome=outcome,
                                        actor="machinery:runner-ci", actor_class="MACHINERY",
                                        fields={"template": "OBLIGATION.mutation_strength", "tool": "mutmut-2"})))
        return classes(conformance(sc, result)[1], "OBLIGATION.mutation_strength")

    def test_rerun_and_signal(self) -> None:
        self.assertEqual(self.observe(["VIOLATION", "CLEAN"]), {INCOMPLETE}, "a passing re-run does not hide a failure")
        self.assertEqual(self.observe(["SIGNAL"]), {INCOMPLETE})


class Evidence(unittest.TestCase):
    def test_an_agents_own_realization_is_no_evidence(self) -> None:
        # B10: by a designated runner (§14.3, §17.5)
        sc = accepted_plan()
        _, cand, result = submit(sc, {"src/solver.py": "def step():\n    return 2\n"}, outcome="PARTIAL")
        spec_rev = sc.rev("tests.conv")
        real = with_id(record("REALIZATION", target={"spec": {"unit": "tests.conv", "rev": spec_rev}, "claim": []},
                              outcome="COMPLETE", actor=agent("maker"), actor_class="AGENT",
                              fields={"execution": {"tree": cand, "units": [], "reads": []}, "configuration": {}}))
        sc.admit(real)
        sc.admit(judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": "o1"}, "PASS", actor=OWNER,
                          fields={"mode": "ORDINARY", "reading": {"unit": "tests.conv", "rev": spec_rev}}))
        self.assertEqual(classes(conformance(sc, result)[1], "OBLIGATION.required_evidence"), {INCOMPLETE})


class ReviewOfX(unittest.TestCase):
    def setup_review(self, scientific: bool = False):
        block = item_block(secondary=SECONDARY, scientific="APPLIES" if scientific else "NOT_APPLIES",
                           slots='["claims", "unverified_assumptions", "deviations", "findings", "null_envelope", '
                                 '"variant_search", "tension_search", "choices", "retention", "delegate_returns"]'
                           if scientific else '["claims", "unverified_assumptions", "deviations"]')
        sc = accepted_plan(block)
        slots = dict(SLOTS, **({k: {"none": "NOT_APPLICABLE"} for k in ("findings", "null_envelope", "variant_search",
                                                                       "tension_search", "choices", "retention",
                                                                       "delegate_returns")} if scientific else {}))
        x, cand, _ = submit(sc, {"src/solver.py": "def step():\n    return 2\n"}, slots=slots)
        realize(sc, cand)
        w = Workflow(sc.derive())
        (review,) = w.of_kind("REVIEW")
        return sc, x, cand, review

    def test_a_review_citing_none_of_the_judged_content_does_not_discharge(self) -> None:
        # B13: a judgment about work carries a content entry on every unit of its judged content (§4.3)
        sc, x, cand, review = self.setup_review()
        sc.admit(judgment("REVIEW", {"transformation": x}, "PASS", actor=agent("checker"), actor_class="AGENT", basis=[],
                          frame={"transformation": x}, binding=dict(fresh(agent("checker"), "r"), obligation=review.id)))
        self.assertNotEqual(Workflow(sc.derive()).discharge(review), DISCHARGED)

    def test_a_scientific_review_needs_its_bidirectional_slot(self) -> None:
        # B11: §13.6
        sc, x, cand, review = self.setup_review(scientific=True)
        result = record("TASK_RESULT", target={"task": "r"}, outcome="COMPLETE", actor=agent("checker"), actor_class="AGENT",
                        fields={"slots": {"claims": [], "findings": {"none": "NONE_FOUND"}}})
        result["binding"] = dict(fresh(agent("checker"), "r"), obligation=review.id)
        result = with_id(result)
        sc.admit(result)
        c = Workflow(sc.derive()).conformance(result["id"])
        self.assertTrue(any(h.template == "OBLIGATION.slots_filled" and "bidirectional" in h.finding for h in c.hits))


class Units(unittest.TestCase):
    def test_literal_factors_and_compound_statements(self) -> None:
        # B12: inside reading E29's claimed scope
        from .test_conformance_domain import CONSISTENT

        for line in ("total = dist + 2.0 * time\n", "total = dist + time / 2\n", "flag = dist < 3 * time\n",
                     "for i in range(2):\n    total = dist + time\n",
                     "if True:\n    reach: Annotated[float, Unit('m')] = time\n"):
            with self.subTest(line=line.strip()):
                self.assertEqual(classes_of("DOMAIN.dimensional_consistency", {"src/solver.py": CONSISTENT + line}), {INCOMPLETE})


if __name__ == "__main__":
    unittest.main()
