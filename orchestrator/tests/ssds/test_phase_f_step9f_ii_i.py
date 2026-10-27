"""Phase F step 9f-ii-i: what a runner's execution records, decided by derivation (catalogue §4.6, §6.3, §6.5,
§17.1-§17.3; plan §3.6, reading F112).

The builder returns the state-decided part of the execution basis: the tree, the record's own context, the
execution closure with the completeness judgments that bounded it or the whole-tree fallback, and the class facts by
value. A realization built on it and the Dispatcher's own fields is admitted. An outcome is every declared output once,
each canonical; the bound is the declared one, capped at 168 hours for a Dispatcher-run class. Expected values are
from §4.6, §6.3, §6.5, §17.3 and F79 (no Stage S case covers the builder).
"""

from __future__ import annotations

import unittest

from ssds.content import parse_spec
from ssds.derivation import effective_bound_hours, execution_basis, outcome_problems, run_configuration
from ssds.derivation.realization import read

from ._scenario import HUMAN_B, attested, content, judgment
from .test_assessment import DECLARATION, Runs


def complete(r: Runs, scope: list[str]) -> str:
    view = r.sc.view(r.sc.head)
    c = judgment("COMPLETENESS", {"scope": scope, "classes": ["EXEC"], "membership": view.membership_digest(tuple(scope))},
                 "COMPLETE", actor=HUMAN_B, basis=[content(u, view.rev(u)) for u in scope])
    r.sc.admit(*attested(c))
    return c["id"]


class Basis(unittest.TestCase):
    def test_with_no_bounding_judgment_the_whole_tree(self) -> None:
        """§4.6, §6.3: missing completeness widens to the tracked whole tree, recorded ``UNBOUNDED``."""

        r = Runs()
        b = execution_basis(r.sc.derive(), "spec", ["code"], "ci")
        self.assertEqual((b["units"], b["bounded_by"], b["widened"][0][0]), ([], "UNBOUNDED", {"tracked": "*"}))
        self.assertEqual(b["tree"], r.sc.head)
        self.assertEqual(b["context"], {"system": "ssds-rules/1", "ignore": [], "analyzers": ["ssds.analyzer.python/1"]})

    def test_a_bounded_closure_records_its_units_and_judgments(self) -> None:
        r = Runs()
        bounds = {complete(r, ["code"]), complete(r, ["spec"])}
        d = r.sc.derive()
        b = execution_basis(d, "spec", ["code"], "ci")
        self.assertEqual(set(b["bounded_by"]), bounds)
        units = {u["unit"]: u for u in b["units"]}
        self.assertEqual(set(units), {"code", "spec"})
        self.assertEqual(units["code"]["rev"], d.s.view.rev("code"))
        self.assertEqual([t for t, _ in units["code"]["terms"]], [{"path": "a.py"}])
        self.assertNotIn("widened", b)

    def test_the_class_facts_by_value(self) -> None:
        """§6.3: decided at realization, recorded by value from the policy in force."""

        from unittest import mock

        from . import test_assessment as ta

        policy = ta.POLICY.replace("attributes = []", 'attributes = ["python"]').replace(
            "observes_outside_reads = true", "observes_outside_reads = false")
        with mock.patch.object(ta, "POLICY", policy):
            r = Runs()
        b = execution_basis(r.sc.derive(), "spec", ["code"], "ci")
        self.assertEqual((b["class_attributes"], b["observes_outside_reads"]), (["python"], False))

    def test_a_judgment_no_longer_current_bounds_nothing(self) -> None:
        from ._scenario import challenge

        r = Runs()
        code, spec = complete(r, ["code"]), complete(r, ["spec"])
        r.sc.admit(challenge({"record": code}))
        b = execution_basis(r.sc.derive(), "spec", ["code"], "ci")
        self.assertEqual(b["bounded_by"], "UNBOUNDED", "a challenged completeness judgment bounds nothing")

    def test_a_built_realization_is_well_formed_and_current(self) -> None:
        from ssds.derivation import F

        from ._scenario import store
        from ._scenario import judgment as make

        r = Runs()
        complete(r, ["code"]), complete(r, ["spec"])
        d = r.sc.derive()
        basis = execution_basis(d, "spec", ["code"], "ci")
        execution = {**basis, "runner": {"class": "ci", "key": "ed25519:test"}, "attributes": [], "pins": [],
                     "unpinnable": True, "start": d.s.n, "end": d.s.n}
        view = r.sc.view(r.sc.head)
        real = make("REALIZATION", {"spec": {"unit": "spec", "rev": view.rev("spec")},
                                    "claim": [{"unit": "code", "rev": view.rev("code")}]}, "COMPLETE",
                    actor="machinery:runner@ed25519:test", actor_class="MACHINERY",
                    fields={"execution": execution, "configuration": run_configuration(d, "spec"),
                            "evaluated": store(r.sc, {"x": 2, "x_verdict": "PASS"})})
        r.sc.admit(real)
        self.assertTrue(read(real["id"], real).well_formed, read(real["id"], real).problems)
        d = r.sc.derive()
        self.assertGreater(d.current(real["id"]), F)
        self.assertTrue(d.a.on_minus(real["id"], d.a.tree_of(real["id"])))

    def test_nothing_runs_for_an_undesignated_class_or_an_unusable_declaration(self) -> None:
        from .test_phase_f_step9b_ii import Declared

        r = Runs()
        self.assertIsNone(execution_basis(r.sc.derive(), "spec", ["code"], "nobody"))
        self.assertIsNone(execution_basis(Declared("oracle = \n").sc.derive(), "spec", ["code"], "ci"))
        self.assertIsNone(execution_basis(r.sc.derive(), "missing", ["code"], "ci"))

    def test_an_ensemble_specification_is_held(self) -> None:
        from .test_phase_f_step9b_ii import Declared

        ensemble = DECLARATION + 'granularity = { mode = "ENSEMBLE", replicates = 3, statistic = "mean", ' \
                                 'seed_policy = "fixed" }\n'
        r = Declared(ensemble)
        self.assertEqual(r.sc.derive().s.specs.declaration("spec").granularity["mode"], "ENSEMBLE")
        self.assertIsNone(execution_basis(r.sc.derive(), "spec", ["code"], "ci"))


class Configuration(unittest.TestCase):
    def test_the_specification_and_its_fixed_attributes(self) -> None:
        """§6.5: the specification unit and every execution attribute it fixes."""

        from .test_phase_f_step9b_ii import DECLARATIVE, Declared

        r = Declared(DECLARATIVE.replace('runner = "ci"', 'runner = "ci"\nfixed = { regime = "re<2000" }'))
        self.assertEqual(run_configuration(r.sc.derive(), "spec"), {"spec": "spec", "fixed": [["regime", "re<2000"]]})


class Outcome(unittest.TestCase):
    """§17.3: ``{output name: canonical value}`` over the declared outputs."""

    def setUp(self) -> None:
        self.declared = parse_spec(DECLARATION.encode())

    def test_a_well_formed_outcome(self) -> None:
        self.assertEqual(outcome_problems(self.declared, {"x": 2, "x_verdict": "PASS"}), [])

    def test_missing_extra_and_non_canonical(self) -> None:
        self.assertTrue(outcome_problems(self.declared, {"x": 2}))
        self.assertTrue(outcome_problems(self.declared, {"x": 2, "x_verdict": "PASS", "log": "…"}))
        self.assertTrue(outcome_problems(self.declared, {"x": "2", "x_verdict": "PASS"}))
        self.assertTrue(outcome_problems(self.declared, {"x": 2, "x_verdict": "MAYBE"}))
        self.assertTrue(outcome_problems(self.declared, [2]))


class Bound(unittest.TestCase):
    def test_a_dispatcher_run_class_is_capped_at_168_hours(self) -> None:
        """F79: the smaller of the declared bound and 168 h for a Dispatcher-run class."""

        long = parse_spec(DECLARATION.replace("time_bound_hours = 24", "time_bound_hours = 200").encode())
        short = parse_spec(DECLARATION.encode())
        self.assertEqual((effective_bound_hours(long, "DISPATCHER"), effective_bound_hours(short, "DISPATCHER")),
                         (168, 24))
        self.assertEqual(effective_bound_hours(long, "EXTERNAL_CUSTODY"), 200)



class ThroughAdmission(unittest.TestCase):
    def test_a_realization_on_the_built_basis_is_admitted(self) -> None:
        """F112 with F97: step 2's checks (an admitted head, its tree's revisions, on⁻, the positions, the outcome)
        hold for what the builder records, the runner's own fields added."""

        import hashlib

        from ssds.core.api.v1 import canonical_json
        from ssds.ledger.read import with_id

        from ._fixtures import record
        from .test_phase_f_step9d_iii import AdmittedRuns

        class Fixture(AdmittedRuns):
            def runTest(self) -> None:
                pass

        f = Fixture()
        f.setUp()
        self.addCleanup(f.doCleanups)
        d = f.derive()
        basis = execution_basis(d, "spec", ["code"], "ci")
        execution = {**basis, "runner": {"class": "ci", "key": f.runner.key_id}, "attributes": [], "pins": [],
                     "unpinnable": True, "start": d.s.n, "end": d.s.n}
        text = canonical_json({"x": 2, "x_verdict": "PASS"}).decode()
        digest = "sha256:" + hashlib.sha256(text.encode()).hexdigest()
        view = d.s.view
        real = with_id({**record("REALIZATION", target={"spec": {"unit": "spec", "rev": view.rev("spec")},
                                                        "claim": [{"unit": "code", "rev": view.rev("code")}]},
                                 outcome="COMPLETE", actor=f"machinery:runner@{f.runner.key_id}",
                                 actor_class="MACHINERY",
                                 fields={"execution": execution, "configuration": run_configuration(d, "spec"),
                                         "evaluated": digest})})
        f.admit_runner(real, objects={digest: text})  # asserts nothing refused


if __name__ == "__main__":
    unittest.main()
