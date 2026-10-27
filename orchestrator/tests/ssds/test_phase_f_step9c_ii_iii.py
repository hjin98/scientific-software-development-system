"""Phase F step 9c-ii-iii: completing ``stale`` (catalogue §6.5, §6.6, §6.9, §17.5; plan §3.6, readings F81,
F93-F94).

``link⁻``'s anchor ranges over every admitted observation of the configuration, ``INCOMPLETE`` ones included, so a
narrow incomplete run can link a differing run and keep a failure counting. An external custody runner's observation
serves conditions (1) and (3) only under its class's latest enumeration listing it and every admitted run of the
configuration by that class, every listed run admitted. Where an observation lacks an output or the reading has no
verdict on it, the failure is yielded only if ``a⁻``'s check on it was in force at ``a⁻``'s base; a name follows one
hop of renames. Expected values are from §6.6 and §6.9 (no Stage S case covers custody or the "either" clause).
"""

from __future__ import annotations

import unittest
from unittest import mock

from ssds.content import recorded_identity

from . import test_assessment as ta
from ._fixtures import RUNNER_KEY, record
from ._scenario import designated, judgment, store
from .test_assessment import BAD, GOOD, SPEC_TERM, Runs
from .test_phase_f_step9b_ii import DECLARATIVE, Declared


def narrow_incomplete(r: Runs, head: str) -> dict:
    """An INCOMPLETE run on ``head`` whose basis records only the specification's terms: it links any two trees
    that agree there (§6.6)."""

    from ssds.ledger.read import with_id

    t = r.sc.trees[head]
    view = r.sc.view(head)
    basis = designated({"tree": head, "context": {"system": "ssds-rules/1", "ignore": [],
                                                  "analyzers": ["ssds.analyzer.python/1"]},
                        "pins": [["dataset:input", "p1"]], "unpinnable": False, "attributes": [],
                        "units": [{"unit": "spec", "rev": view.rev("spec"),
                                   "terms": [[SPEC_TERM, recorded_identity(t, SPEC_TERM, ())]]}],
                        "bounded_by": [r.bound_judgment(head)], "incomplete": "CRASHED"})
    real = judgment("REALIZATION", {"spec": {"unit": "spec", "rev": view.rev("spec")},
                                    "claim": [{"unit": "code", "rev": view.rev("code")}]}, "INCOMPLETE",
                    actor=f"machinery:dispatcher@{RUNNER_KEY}", actor_class="MACHINERY",
                    fields={"execution": basis, "configuration": {"regime": "default"}})
    real = with_id({**real, "provenance": {"attempt": "narrow"}})
    r.sc.admit(real)
    return real


class Anchors(unittest.TestCase):
    def test_an_incomplete_anchor_links_a_differing_run(self) -> None:
        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(t0, BAD))
        r.run(t0, BAD)
        r.run(t1, GOOD)
        narrow_incomplete(r, t0)
        self.assertFalse(r.stale(failing, "T1"), "the narrow incomplete run links T1's differing run to T0 (2)")

    def test_without_it_the_genuine_fix_is_stale(self) -> None:
        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(t0, BAD))
        r.run(t0, BAD)
        r.run(t1, GOOD)
        self.assertTrue(r.stale(failing, "T1"))


CUSTODY_POLICY = ta.POLICY.replace('kind = "DISPATCHER"', 'kind = "EXTERNAL_CUSTODY"')


class Custody(unittest.TestCase):
    def setUp(self) -> None:
        with mock.patch.object(ta, "POLICY", CUSTODY_POLICY):
            self.r = Runs()
        r = self.r
        self.t0, self.t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        self.failing = r.fail(r.run(self.t0, BAD))
        self.reproduced = r.run(self.t0, BAD)
        self.passed = r.run(self.t1, GOOD)

    def enumerate(self, runs) -> None:
        self.r.sc.admit(record("CUSTODY_ENUMERATION", target={"runner": "ci"}, actor=f"machinery:custody@{RUNNER_KEY}",
                               actor_class="MACHINERY", fields={"runs": sorted(runs)}))

    def every_run(self):
        return {self.failing["target"]["realization"], self.reproduced["id"], self.passed["id"]}

    def test_no_enumeration_no_stop(self) -> None:
        self.assertFalse(self.r.stale(self.failing, "T1"))

    def test_the_full_enumeration_lets_it_stop(self) -> None:
        self.enumerate(self.every_run())
        self.assertTrue(self.r.stale(self.failing, "T1"))

    def test_an_unlisted_run(self) -> None:
        self.enumerate(self.every_run() - {self.passed["id"]})
        self.assertFalse(self.r.stale(self.failing, "T1"))

    def test_another_run_of_the_class_unlisted(self) -> None:
        self.enumerate(self.every_run() - {self.failing["target"]["realization"]})
        self.assertFalse(self.r.stale(self.failing, "T1"), "every admitted run of the configuration by the class")

    def test_an_enumerated_run_not_admitted(self) -> None:
        self.enumerate(self.every_run() | {"sha256:" + "9" * 64})
        self.assertFalse(self.r.stale(self.failing, "T1"), "every enumerated run counts (F81)")


class Either(unittest.TestCase):
    def test_a_removed_admitted_check_is_still_yielded(self) -> None:
        r = Declared(DECLARATIVE)
        t0 = r.tree("T0")
        failing = r.fail(r.run(t0, {"x": 1, "y": "0.0"}))
        good = r.run(t0, {"x": 2, "y": "0.0"})
        r.revise(DECLARATIVE.replace('{ output = "x", template = "EXACT", params = { reference = 2 } },\n', ""))
        self.assertTrue(r.assessments().yields(good["id"], failing["id"]), "its check was in force at its base")

    def test_an_output_never_checked_at_its_base_is_not_yielded(self) -> None:
        r = Declared(DECLARATIVE)
        t0 = r.tree("T0")
        failing = r.assess(r.run(t0, {"x": 2, "y": "0.0", "z": True}), "FAIL", failing=("z",))
        good = r.run(t0, {"x": 2, "y": "0.0", "z": True})
        self.assertFalse(r.assessments().yields(good["id"], failing["id"]), "z had no check at a⁻'s base")


RENAMED = DECLARATIVE.replace('{ name = "x", type = "int" }', '{ name = "x2", type = "int" }') \
    .replace('{ output = "x", template = "EXACT"', '{ output = "x2", template = "EXACT"')


class Renames(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Declared(DECLARATIVE)
        self.failing = self.r.fail(self.r.run(self.r.tree("T0"), {"x": 1, "y": "0.0"}))

    def test_a_mapped_rename_is_evaluated(self) -> None:
        self.r.revise(RENAMED + 'output_renames = { x = "x2" }\n')
        good = self.r.run(self.r.sc.head, {"x2": 2, "y": "0.0"})
        self.assertFalse(self.r.assessments().yields(good["id"], self.failing["id"]))

    def test_an_outcome_is_read_under_its_own_names(self) -> None:
        self.r.revise(RENAMED + 'output_renames = { x = "x2" }\n')
        renamed = self.r.run(self.r.sc.head, {"x2": 1, "y": "0.0"})
        self.assertEqual(self.r.assessments().restricted(renamed["id"], ["x"]), {"x": "1"})

    def test_an_unmapped_rename_is_not_evaluated(self) -> None:
        self.r.revise(RENAMED)
        good = self.r.run(self.r.sc.head, {"x2": 2, "y": "0.0"})
        self.assertTrue(self.r.assessments().yields(good["id"], self.failing["id"]), "x's check was in force")


if __name__ == "__main__":
    unittest.main()
