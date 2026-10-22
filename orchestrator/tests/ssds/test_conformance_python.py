"""Phase E step 4b: the check library's Python analyzer templates (catalogue §14.3, §14.5).

Each case states the defect the template exists to catch, from §14.3's table, and a clean control.
"""

from __future__ import annotations

import unittest

from ssds.derivation.conformance import CLEAN, INCOMPLETE, SIGNAL, VIOLATION

from .test_conformance import accepted_plan, conformance, realize, submit
from .test_lint import item_block

TEST_FILE = '''import unittest
import solver


class TestSolver(unittest.TestCase):
    def test_step(self):
        self.assertEqual(solver.step(), 1)
        self.assertAlmostEqual(solver.step(), 1.0, delta=0.01)

    def test_io(self):
        assert solver.step() == 1
'''


def classes_of(template: str, files: dict[str, str], params: str = "", base: dict[str, str] | None = None,
               outcome: str = "PARTIAL") -> set[str]:
    check = f'{{ check = "{template}"{", params = " + params if params else ""} }}'
    secondary = f'[ {{ check = "BOUNDARY.write_scope" }}, {{ check = "TEST_INTEGRITY.evidence_specs_untouched" }}, {check} ]'
    sc = accepted_plan(item_block(secondary=secondary))
    if base:
        sc.absorb(base)  # the plan is unchanged, so its acceptance stays current
    _, cand, result = submit(sc, files, outcome=outcome)
    realize(sc, cand)
    c = conformance(sc, result)[1]
    return {h.cls for h in c.hits if h.template == template}


class TestIntegrity(unittest.TestCase):
    base = {"src/test_solver.py": TEST_FILE}

    def test_no_deletions(self) -> None:
        deleted = TEST_FILE.replace("    def test_io(self):\n        assert solver.step() == 1\n", "")
        self.assertEqual(classes_of("TEST_INTEGRITY.no_deletions", {"src/test_solver.py": deleted}, base=self.base), {VIOLATION})
        self.assertEqual(classes_of("TEST_INTEGRITY.no_deletions", {"src/solver.py": "def step():\n    return 1\n"},
                                    base=self.base), {CLEAN})

    def test_no_skips(self) -> None:
        skipped = TEST_FILE.replace("    def test_io(self):", "    @unittest.skip('later')\n    def test_io(self):")
        self.assertEqual(classes_of("TEST_INTEGRITY.no_skips", {"src/test_solver.py": skipped}, base=self.base), {VIOLATION})
        called = TEST_FILE.replace("        assert solver.step() == 1\n", "        self.skipTest('later')\n")
        self.assertEqual(classes_of("TEST_INTEGRITY.no_skips", {"src/test_solver.py": called}, base=self.base), {VIOLATION})

    def test_no_xfail(self) -> None:
        marked = TEST_FILE.replace("    def test_io(self):", "    @unittest.expectedFailure\n    def test_io(self):")
        self.assertEqual(classes_of("TEST_INTEGRITY.no_xfail", {"src/test_solver.py": marked}, base=self.base), {VIOLATION})

    def test_selectors_restrict_the_check(self) -> None:
        skipped = TEST_FILE.replace("    def test_io(self):", "    @unittest.skip('later')\n    def test_io(self):")
        self.assertEqual(classes_of("TEST_INTEGRITY.no_skips", {"src/test_solver.py": skipped}, '{ selectors = ["other/"] }',
                                    base=self.base), {CLEAN})

    def test_fewer_assertions_and_widened_tolerance_only_signal(self) -> None:
        fewer = TEST_FILE.replace("        self.assertEqual(solver.step(), 1)\n", "")
        self.assertEqual(classes_of("TEST_INTEGRITY.fewer_assertions", {"src/test_solver.py": fewer}, base=self.base), {SIGNAL})
        wider = TEST_FILE.replace("delta=0.01", "delta=0.5")
        self.assertEqual(classes_of("TEST_INTEGRITY.widened_tolerance", {"src/test_solver.py": wider}, base=self.base), {SIGNAL})


class Obligation(unittest.TestCase):
    def test_no_new_stubs(self) -> None:
        stubbed = "def step():\n    return 1\n\n\ndef refine():\n    raise NotImplementedError\n"
        self.assertEqual(classes_of("OBLIGATION.no_new_stubs", {"src/solver.py": stubbed}), {INCOMPLETE})
        real = "def step():\n    return 1\n\n\ndef refine():\n    return 2\n"
        self.assertEqual(classes_of("OBLIGATION.no_new_stubs", {"src/solver.py": real}), {CLEAN})

    def test_required_artifact(self) -> None:
        params = '{ artifact = "src/solver.py" }'
        linked = {"src/solver.py": "def step():\n    return 1\n", "src/test_solver.py": TEST_FILE}
        self.assertEqual(classes_of("OBLIGATION.required_artifact", linked, params), {CLEAN})
        self.assertEqual(classes_of("OBLIGATION.required_artifact", {"src/solver.py": "def step():\n    return 2\n"}, params),
                         {INCOMPLETE}, "present but linked by no TESTS relation")
        self.assertEqual(classes_of("OBLIGATION.required_artifact", {"src/io.py": "def write():\n    return 3\n"},
                                    '{ artifact = "src/absent.py" }'), {INCOMPLETE})


class Boundary(unittest.TestCase):
    def test_frozen_interface(self) -> None:
        params = '{ symbols = ["src.solver.step"] }'
        self.assertEqual(classes_of("BOUNDARY.frozen_interface", {"src/solver.py": "def step():\n    return 5\n"}, params),
                         {CLEAN}, "a body change keeps the signature")
        self.assertEqual(classes_of("BOUNDARY.frozen_interface", {"src/solver.py": "def step(scale):\n    return scale\n"},
                                    params), {VIOLATION})
        self.assertEqual(classes_of("BOUNDARY.frozen_interface", {"src/solver.py": "def other():\n    return 1\n"}, params),
                         {VIOLATION}, "removed")

    def test_dependency_allowance(self) -> None:
        base = {"src/requirements.txt": "numpy>=1.20\n"}
        self.assertEqual(classes_of("BOUNDARY.dependency_allowance", {"src/requirements.txt": "numpy>=1.20\nSciPy==1.11\n"},
                                    base=base), {CLEAN}, "scipy is in the contract's allowance")
        self.assertEqual(classes_of("BOUNDARY.dependency_allowance", {"src/requirements.txt": "numpy>=1.20\npandas\n"},
                                    base=base), {VIOLATION})
        self.assertEqual(classes_of("BOUNDARY.dependency_allowance", {"src/package.json": '{"dependencies": {"left-pad": "1"}}'}),
                         {VIOLATION}, "a manifest of an unanalyzed language cannot be checked")

    def test_credential_values(self) -> None:
        self.assertEqual(classes_of("BOUNDARY.credential_values", {"src/solver.py": "KEY = 'AKIA" + "ABCDEFGHIJKLMNOP" + "'\n"}),
                         {VIOLATION})
        token = "Zx9kQ2mP8vR4tY7wL1nB6cF3hJ5dS0gA"
        self.assertEqual(classes_of("BOUNDARY.credential_values", {"src/solver.py": f"TOKEN = '{token}'\n"}), {VIOLATION})
        self.assertEqual(classes_of("BOUNDARY.credential_values", {"src/solver.py": "def step():\n    return 1\n"}), {CLEAN})


if __name__ == "__main__":
    unittest.main()
