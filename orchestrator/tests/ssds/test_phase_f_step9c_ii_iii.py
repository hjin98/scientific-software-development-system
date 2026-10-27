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
from .test_assessment import BAD, GOOD, OBL, SPEC_TERM, Runs
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


def other_anchor(r: Runs, head: str) -> dict:
    """An INCOMPLETE run on ``head`` whose basis records only ``other.txt``: it links exactly the trees agreeing
    there (§6.6), so it separates conditions (2) and (4) (review of babcbd22, U1/U8)."""

    from ssds.ledger.read import with_id

    t = r.sc.trees[head]
    view = r.sc.view(head)
    term = {"path": "other.txt"}
    basis = designated({"tree": head, "context": {"system": "ssds-rules/1", "ignore": [],
                                                  "analyzers": ["ssds.analyzer.python/1"]},
                        "pins": [["dataset:input", "p1"]], "unpinnable": False, "attributes": [], "units": [],
                        "reads": [[term, recorded_identity(t, term, ())]], "bounded_by": [r.bound_judgment(head)],
                        "incomplete": "CRASHED"})
    real = judgment("REALIZATION", {"spec": {"unit": "spec", "rev": view.rev("spec")},
                                    "claim": [{"unit": "code", "rev": view.rev("code")}]}, "INCOMPLETE",
                    actor=f"machinery:dispatcher@{RUNNER_KEY}", actor_class="MACHINERY",
                    fields={"execution": basis, "configuration": {"regime": "default"}})
    real = with_id({**real, "provenance": {"attempt": f"other-{head}"}})
    r.sc.admit(real)
    return real


class Separated(unittest.TestCase):
    def test_condition_two_alone(self) -> None:
        """The anchor links a differing run on T1 to the failing tree T0, and nothing to G = T2."""

        r = Runs(other=True)
        t0 = r.tree("T0")
        t1 = r.tree("T1", **{"a.py": "v = 2\n"})
        t2 = r.tree("T2", **{"a.py": "v = 2\n", "other.txt": "2\n"})
        failing = r.fail(r.run(t0, BAD))
        r.run(t0, BAD)
        r.run(t1, GOOD)
        r.run(t2, GOOD)
        other_anchor(r, t0)
        self.assertFalse(r.stale(failing, "T2"), "(2): the run on T1 differed")

    def test_condition_four_alone(self) -> None:
        """The anchor links an unfixed run on X to G = T2, and nothing to the failing tree T0."""

        r = Runs(other=True)
        t0 = r.tree("T0")
        x = r.tree("X", **{"other.txt": "2\n"})
        t2 = r.tree("T2", **{"a.py": "v = 2\n", "other.txt": "2\n"})
        failing = r.fail(r.run(t0, BAD))
        r.run(t0, BAD)
        r.run(x, BAD)
        r.run(t2, GOOD)
        other_anchor(r, x)
        self.assertFalse(r.stale(failing, "T2"), "(4): the unfixed run on X yields here")


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

    def test_an_enumeration_by_a_key_outside_the_class(self) -> None:
        self.r.sc.admit(record("CUSTODY_ENUMERATION", target={"runner": "ci"}, actor="machinery:custody@ed25519:other",
                               actor_class="MACHINERY", fields={"runs": sorted(self.every_run())}))
        self.assertFalse(self.r.stale(self.failing, "T1"))

    def test_the_latest_enumeration_decides(self) -> None:
        self.enumerate(self.every_run())
        self.enumerate(self.every_run() - {self.passed["id"]})
        self.assertFalse(self.r.stale(self.failing, "T1"), "the newer enumeration omits a run")

    def test_an_enumeration_that_does_not_act(self) -> None:
        from ssds.ledger.read import with_id

        from ._scenario import agent, submit

        x, _, _ = submit(self.r.sc, {"b.py": "w = 1\n"}, agent("maker"), "t-pending")
        self.r.sc.admit(with_id({**record("CUSTODY_ENUMERATION", target={"runner": "ci"},
                                          actor=f"machinery:custody@{RUNNER_KEY}", actor_class="MACHINERY",
                                          fields={"runs": sorted(self.every_run())}),
                                 "frame": {"transformation": x}}))
        self.assertFalse(self.r.stale(self.failing, "T1"), "a pending frame's enumeration does not act")

    def test_an_untrusted_enumeration(self) -> None:
        """Re-check of 9031b16d (w1-w3): an enumeration counts only under a realization's trust."""

        from .test_phase_f_step9c_ii_i import adopt

        cases = {"compromised": None, "not a trust root": "ed25519:other", "not machinery": RUNNER_KEY}
        for case, key in cases.items():
            with self.subTest(case=case):
                self.setUp()
                if case == "compromised":
                    self.enumerate(self.every_run())
                    at = self.r.sc.derive().s.position_of(self.passed["id"]) + 1
                    self.r.sc.lifecycle(record("KEY_LIFECYCLE", target=None, fields={
                        "action": "COMPROMISED", "key": {"role": "RUNNER", "id": RUNNER_KEY, "public_key": "00" * 32},
                        "from_position": at}))
                elif case == "not a trust root":
                    adopt(self.r.sc, CUSTODY_POLICY.replace('keys = ["ed25519:test"]',
                                                            'keys = ["ed25519:test", "ed25519:other"]'))
                    self.r.sc.admit(record("CUSTODY_ENUMERATION", target={"runner": "ci"},
                                           actor=f"machinery:custody@{key}", actor_class="MACHINERY",
                                           fields={"runs": sorted(self.every_run())}))
                else:
                    self.r.sc.admit(record("CUSTODY_ENUMERATION", target={"runner": "ci"},
                                           actor=f"machinery:custody@{key}", actor_class="AGENT",
                                           fields={"runs": sorted(self.every_run())}))
                self.assertFalse(self.r.stale(self.failing, "T1"))

    def test_an_enumerated_run_not_admitted(self) -> None:
        self.enumerate(self.every_run() | {"sha256:" + "9" * 64})
        self.assertFalse(self.r.stale(self.failing, "T1"), "every enumerated run counts (F81)")


class UnreadablePolicy(unittest.TestCase):
    def test_an_unreadable_historical_policy_never_drops_failing_evidence(self) -> None:
        """Review of babcbd22, note 3 (v9)."""

        from .test_phase_f_step9c_ii_i import adopt

        r = Runs()
        adopt(r.sc, ta.POLICY + "unknown_table = 1\n")  # a policy this parser refuses
        real = r.run(r.tree("T0"), BAD)
        failing = r.fail(real)
        adopt(r.sc, ta.POLICY)
        d = r.sc.derive()
        self.assertTrue(d.a.admissible(failing["id"], ta.OBL), "(d) is met on the adverse side")
        self.assertFalse(d.a.realization_ok(real["id"], ta.OBL), "and never on the permissive side")


class Either(unittest.TestCase):
    def test_a_removed_admitted_check_is_still_yielded(self) -> None:
        r = Declared(DECLARATIVE)
        t0 = r.tree("T0")
        failing = r.fail(r.run(t0, {"x": 1, "y": "0.0"}))
        good = r.run(t0, {"x": 2, "y": "0.0"})
        r.revise(DECLARATIVE.replace('{ output = "x", template = "EXACT", params = { reference = 2 } },\n', ""))
        self.assertTrue(r.assessments().yields(good["id"], failing["id"]), "its check was in force at its base")

    def test_a_declared_output_with_no_verdict_is_yielded(self) -> None:
        """Review of babcbd22, B1: z is declared but checked by no verdict: not computable, so yielded."""

        r = Declared(DECLARATIVE)
        t0 = r.tree("T0")
        failing = r.assess(r.run(t0, {"x": 2, "y": "0.0", "z": True}), "FAIL", failing=("z",))
        good = r.run(t0, {"x": 2, "y": "0.0", "z": True})
        self.assertTrue(r.assessments().yields(good["id"], failing["id"]))

    def test_an_output_removed_from_the_declaration(self) -> None:
        """The either clause's genuine case: x was declared at a⁻'s base and G's reading no longer declares it."""

        r = Declared(DECLARATIVE)
        t0 = r.tree("T0")
        failing = r.fail(r.run(t0, {"x": 1, "y": "0.0"}))
        removed = DECLARATIVE.replace('{ name = "x", type = "int" }, ', "") \
            .replace('{ output = "x", template = "EXACT", params = { reference = 2 } },\n', "")
        r.revise(removed)
        good = r.run(r.sc.head, {"y": "0.0"})
        self.assertTrue(r.assessments().yields(good["id"], failing["id"]), "its check was in force at its base")

    def test_a_frame_records_base_is_its_frames(self) -> None:
        """Re-check of 9031b16d (w5): a⁻ in a candidate's frame, admitted after an absorbed revision dropped x; its
        base is the frame's, where x was declared, so its check was in force there."""

        from ssds.ledger.read import with_id

        from ._scenario import HUMAN_B, agent, content, on_record, submit

        r = Declared(DECLARATIVE)
        t0 = r.tree("T0")
        real = r.run(t0, {"x": 1, "y": "0.0"})
        spec_rev = r.sc.view(t0).rev("spec")
        x, _, _ = submit(r.sc, {"b.py": "w = 1\n"}, agent("maker"), "t-frame")
        removed = DECLARATIVE.replace('{ name = "x", type = "int" }, ', "") \
            .replace('{ output = "x", template = "EXACT", params = { reference = 2 } },\n', "")
        r.revise(removed)
        failing = with_id({**judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": OBL}, "FAIL",
                                      actor=HUMAN_B, basis=[on_record(real["id"]), content("spec", spec_rev)],
                                      fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": spec_rev},
                                              "failing_outputs": ["x"]}),
                           "frame": {"transformation": x}})
        r.sc.admit(failing)
        good = r.run(r.sc.head, {"y": "0.0"})
        self.assertTrue(r.assessments().yields(good["id"], failing["id"]))

    def test_an_output_never_declared_fails_closed(self) -> None:
        r = Declared(DECLARATIVE)
        t0 = r.tree("T0")
        failing = r.assess(r.run(t0, {"x": 2, "y": "0.0"}), "FAIL", failing=("w",))
        good = r.run(t0, {"x": 2, "y": "0.0"})
        self.assertTrue(r.assessments().yields(good["id"], failing["id"]),
                        "w is no declared output of a⁻'s reading: F(a⁻) names none of it, so fail closed")


class NeverStaleByMechanics(unittest.TestCase):
    """Review of babcbd22, B1: its three probes; re-check of 9031b16d: an undeclared failing name."""

    def test_a_failing_name_no_declaration_has(self) -> None:
        reader = 'oracle = "ASSESSOR_READ"\nrunner = "ci"\ntime_bound_hours = 24\noutputs = [{ name = "x", type = "int" }]\n'
        for declaration, outcome in ((DECLARATIVE, {"x": 2, "y": "0.0"}), (reader, {"x": 1})):
            with self.subTest(oracle=declaration.split("\n")[0]):
                self.assertFalse(self.stale(declaration, outcome, outcome, outcome, ("typo",)))

    def stale(self, declaration, failing_outcome, rerun_outcome, here_outcome, failing_outputs=None):
        r = Declared(declaration)
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.assess(r.run(t0, failing_outcome), "FAIL", failing=failing_outputs or ("x",))
        r.run(t0, rerun_outcome)
        r.run(t1, here_outcome)
        return r.stale(failing, "T1")

    def test_assessor_read_identical_or_different(self) -> None:
        reader = 'oracle = "ASSESSOR_READ"\nrunner = "ci"\ntime_bound_hours = 24\noutputs = [{ name = "x", type = "int" }]\n'
        self.assertFalse(self.stale(reader, {"x": 1}, {"x": 1}, {"x": 1}), "a value alone discriminates nothing")
        self.assertFalse(self.stale(reader, {"x": 1}, {"x": 1}, {"x": 2}))

    def test_an_unchecked_declared_output(self) -> None:
        self.assertFalse(self.stale(DECLARATIVE, {"x": 2, "y": "0.0", "z": True}, {"x": 2, "y": "0.0", "z": True},
                                    {"x": 2, "y": "0.0", "z": True}, ("z",)))


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
