"""Phase E step 3b: lint, the plan invariants, control tightening and partition lint at the derivation owner.

Carries the derivation halves of S5 §8-§13 (catalogue §11.3, §13.2-§13.4, §13.7): the tightening cases
(``prose_change_is_not_tightening``, ``narrower_scope_is_tightening``, ``wider_scope_is_not_tightening``,
``larger_budget_is_not_tightening``, ``field_outside_whitelist_is_r2``,
``narrower_dependency_allowance_is_tightening``), ``ref_outside_item_part_rejected``,
``document_item_cannot_touch_authority``, ``partition_lint`` and ``repartition_lint_over_undischarged``.
Expected values are the cases' stated outcomes and the catalogue's rules.
"""

from __future__ import annotations

import unittest

from ssds.derivation import F, T
from ssds.derivation.plans import partition_violations, resolve

from ._scenario import OWNER, Scenario, content, judgment

MANIFEST = '''
    [[unit]]
    id = "plan.work"
    kind = "PLAN"
    role = "composite"
    scope = [{ file = "plans/work.md" }]
    [[unit]]
    id = "plan.work.objective"
    part_of = "plan.work"
    subject = false
    scope = [{ file = "plans/work.md", heading = ["Objective"] }]
    [[unit]]
    id = "plan.work.item"
    part_of = "plan.work"
    subject = false
    scope = [{ file = "plans/work.md", heading = ["Item"] }]
    [[unit]]
    id = "src"
    kind = "D4"
    scope = [{ prefix = "src/" }]
    [[unit]]
    id = "numerics"
    kind = "D2"
    scope = [{ path = "numerics.md" }]
    [[unit]]
    id = "design"
    kind = "D3"
    scope = [{ path = "design.md" }]
    [[unit]]
    id = "tests.conv"
    kind = "EVIDENCE_SPEC"
    scope = [{ path = "specs/conv.toml" }]
    [[unit]]
    id = "records"
    kind = "EVIDENCE_RECORD"
    scope = [{ path = "records.md" }]
'''
FILES = {"src/solver.py": "def step():\n    return 1\n", "src/io.py": "def write():\n    return 2\n",
         "numerics.md": "# Numerics\n", "design.md": "# Design\n", "specs/conv.toml": "kind = 'convergence'\n",
         "records.md": "# Records\n"}
SECONDARY = '[ { check = "TEST_INTEGRITY.no_skips" }, { check = "BOUNDARY.write_scope" } ]'


def item_block(kind: str = "IMPLEMENT", write_scope: str = '["src/"]', affected: str = '["src/"]', budget: int = 3,
               scientific: str = "NOT_APPLIES", slots: str = '["claims", "unverified_assumptions", "deviations"]',
               extra_item: str = "", extra_contract: str = "", dependencies: str = '{ python = ["numpy", "scipy"] }',
               o1_verifier: str = '{ evidence = "tests.conv", runner = "ci" }', o2_verifier: str = '"REVIEW"',
               secondary: str = SECONDARY, objective_ref: str = "#item") -> str:
    return f'''item = "work"
kind = "{kind}"
objective = {{ ref = "{objective_ref}" }}
affected = {affected}
{extra_item}
[contract]
scientific = "{scientific}"
budget = {budget}
{extra_contract}
[contract.boundaries]
write_scope = {write_scope}
dependencies = {dependencies}
[[contract.obligations]]
id = "o1"
statement = {{ ref = "#o1" }}
verifier = {o1_verifier}
secondary = {secondary}
[[contract.obligations]]
id = "o2"
statement = {{ ref = "#o2" }}
verifier = {o2_verifier}
secondary = {secondary}
[contract.expectations]
slots = {slots}
'''


def plan_text(block: str, prose: str = "Make the solver adaptive.\n", objective: str = "Adaptive solver.\n") -> str:
    return (f"# Work\n\n## Objective\n\n{objective}\n## Item\n\n{prose}\n"
            "### o1\n\nThe convergence evidence passes.\n\n### o2\n\nThe change is reviewed.\n\n"
            f"```ssds-item\n{block}```\n")


def scenario(block: str, policy: str | None = None, **kw: str) -> Scenario:
    return Scenario(MANIFEST, {**FILES, "plans/work.md": plan_text(block, **kw)}, policy=policy)


def findings(block: str, policy: str | None = None, **kw: str) -> set[tuple[str, str]]:
    d = scenario(block, policy, **kw).derive()
    return {(f.code, f.detail) for f in d.s.plans.item_lint("plan.work.item")}


def codes(block: str, policy: str | None = None, **kw: str) -> set[str]:
    return {code for code, _ in findings(block, policy, **kw)}


class Lint(unittest.TestCase):
    def test_a_clean_item(self) -> None:
        self.assertEqual(findings(item_block()), set())

    def test_ref_outside_item_part_rejected(self) -> None:
        # S5 §13 ref_outside_item_part_rejected (b595f2c B2): (item1, Objective, item2) -> (True, True, False)
        self.assertNotIn("REF", codes(item_block(objective_ref="#item")))
        self.assertNotIn("REF", codes(item_block(objective_ref="#objective")))
        self.assertIn("REF", codes(item_block(objective_ref="#work")))  # the plan's title, outside both parts

    def test_document_item_cannot_touch_authority(self) -> None:
        # S5 §13 document_item_cannot_touch_authority (b595f2c B3, c6da678 B3):
        # DOCUMENT {D4, D2} F; IMPLEMENT {D3} F; IMPLEMENT {D4, MANIFEST} T; AUTHOR D2 {D2, MANIFEST} T; AUTHOR D2 {D2, D1} F
        cases = [
            ("DOCUMENT", "", '["src/", "numerics.md"]', False),
            ("IMPLEMENT", "", '["design.md"]', False),
            ("IMPLEMENT", "", '["src/", ".ssds/manifest.toml"]', True),
            ("AUTHOR", 'authority = "D2"', '["numerics.md", ".ssds/manifest.toml"]', True),
            ("AUTHOR", 'authority = "D2"', '["numerics.md", "design.md"]', False),
        ]
        for kind, extra, scope, ok in cases:
            with self.subTest(kind=kind, scope=scope):
                block = item_block(kind=kind, write_scope=scope, affected=scope, extra_item=extra)
                self.assertEqual("DOMAIN" not in codes(block), ok)

    def test_scope_refusals(self) -> None:
        self.assertIn("SCOPE", codes(item_block(write_scope='["src/", "design.md"]', affected='["src/"]')))
        self.assertIn("SCOPE", codes(item_block(write_scope='["src/", "plans/"]', affected='["src/", "plans/"]')))
        self.assertIn("SCOPE", codes(item_block(write_scope='["src/", "specs/conv.toml"]',
                                                affected='["src/", "specs/"]')))
        named = item_block(write_scope='["src/", "specs/conv.toml"]', affected='["src/", "specs/"]',
                           extra_contract="").replace('dependencies = ', 'evidence_specs = ["tests.conv"]\ndependencies = ')
        self.assertNotIn("SCOPE", codes(named))
        protected = 'schema = 1\n[workflow]\nprotected_surfaces = ["src/io.py"]\n'
        self.assertIn("SCOPE", codes(item_block(), policy=protected))

    def test_naming_a_units_whole_file_is_not_narrower(self) -> None:
        # Containment is by bytes: an affected span does not contain its whole file.
        view = scenario(item_block()).derive().s.view
        span, _ = resolve(view, ["src"])
        whole, _ = resolve(view, ["src/solver.py"])
        from ssds.derivation.plans import contained

        self.assertTrue(contained(view, whole, span), "src/ covers the whole of src/solver.py")
        unit_view = scenario(item_block()).derive().s.view
        part, _ = resolve(unit_view, ["plan.work.objective"])
        file_atoms, _ = resolve(unit_view, ["plans/work.md"])
        self.assertFalse(contained(unit_view, file_atoms, part), "a part's file is wider than the part")
        self.assertTrue(contained(unit_view, part, file_atoms))

    def test_verifier_slot_coverage_and_budget_refusals(self) -> None:
        self.assertIn("VERIFIER", codes(item_block(o1_verifier='{ check = "FAITHFULNESS.prose_numbers" }')))
        self.assertIn("VERIFIER", codes(item_block(o1_verifier='{ check = "ORACLE.EXACT" }')))
        self.assertIn("VERIFIER", codes(item_block(o1_verifier='{ check = "OBLIGATION.required_evidence" }')))
        self.assertIn("VERIFIER", codes(item_block(o1_verifier='{ evidence = "records", runner = "ci" }')))
        self.assertIn("SLOTS", codes(item_block(slots='["claims"]')))
        self.assertIn("SLOTS", codes(item_block(scientific="APPLIES")))
        self.assertIn("COVERAGE", codes(item_block(o1_verifier='"REVIEW"')))  # no EVIDENCE obligation on D4
        self.assertIn("COVERAGE", codes(item_block(secondary='[ { check = "BOUNDARY.write_scope" } ]')))
        self.assertIn("BUDGET", codes(item_block(budget=11)))

    def test_gates_policy_requires(self) -> None:
        policy = 'schema = 1\n[domains.D4]\ngates = ["release-gate"]\n'
        self.assertIn("GATES", codes(item_block(), policy=policy))
        self.assertNotIn("GATES", codes(item_block(extra_item='gates = ["release-gate"]'), policy=policy))

    def test_unresolved_and_topology(self) -> None:
        self.assertIn("UNRESOLVED", codes(item_block(extra_item='governing = ["missing@sha256:' + "a" * 64 + '"]')))
        self.assertIn("TOPOLOGY", codes(item_block(extra_item='depends_on = ["nowhere"]')))


class Tightening(unittest.TestCase):
    """Amendment classes against the accepted revision (§13.4; S5 §13 tightening cases)."""

    def amended(self, before: str, after: str, prose_after: str = "Make the solver adaptive.\n") -> str:
        sc = scenario(before)
        rev = sc.rev("plan.work.item")
        sc.absorb({"plans/work.md": plan_text(after, prose=prose_after)})
        return sc.derive().s.plans.amendment_class("plan.work.item", rev)

    def test_cases(self) -> None:
        base = item_block(write_scope='["src/"]')
        self.assertEqual(self.amended(base, base, prose_after="Make the solver adaptive, quickly.\n"), "R2",
                         "prose_change_is_not_tightening (6ff4ed1 B2)")
        self.assertEqual(self.amended(base, item_block(write_scope='["src/solver.py"]')), "R1", "narrower_scope_is_tightening")
        self.assertEqual(self.amended(item_block(write_scope='["src/solver.py"]'), base), "R2", "wider_scope_is_not_tightening")
        self.assertEqual(self.amended(base, item_block(budget=5)), "R2", "larger_budget_is_not_tightening")
        self.assertEqual(self.amended(base, item_block(budget=2)), "R1", "a smaller budget is tightening")
        self.assertEqual(self.amended(base, item_block(affected='["src/", "specs/"]')), "R2", "field_outside_whitelist_is_r2")
        self.assertEqual(self.amended(base, item_block(dependencies='{ python = ["numpy"] }')), "R1",
                         "narrower_dependency_allowance_is_tightening")
        self.assertEqual(self.amended(base, item_block(scientific="APPLIES", slots='["claims", "unverified_assumptions", '
                                                       '"deviations", "findings"]')), "R1", "scientific on, more slots")
        self.assertEqual(self.amended(item_block(scientific="APPLIES"), base), "R2", "scientific off")

    def test_tightening_then_loosening_is_caught_against_the_accepted_revision(self) -> None:
        sc = scenario(item_block(write_scope='["src/"]'))
        accepted = sc.rev("plan.work.item")
        sc.absorb({"plans/work.md": plan_text(item_block(write_scope='["src/solver.py"]'))})
        sc.absorb({"plans/work.md": plan_text(item_block(write_scope='["src/", "src/io.py"]'))})
        self.assertEqual(sc.derive().s.plans.amendment_class("plan.work.item", accepted), "R1",
                         "back to the accepted scope is still within it")
        sc.absorb({"plans/work.md": plan_text(item_block(write_scope='["src/", "design.md"]'))})
        self.assertEqual(sc.derive().s.plans.amendment_class("plan.work.item", accepted), "R2")


class PlanAcceptanceCurrency(unittest.TestCase):
    """A plan acceptance names items with consumption class PLAN_CONTROL (§4.4, §11.2)."""

    def accept(self, sc: Scenario) -> dict:
        objective, item = sc.rev("plan.work.objective"), sc.rev("plan.work.item")
        return judgment("PLAN_ACCEPTANCE", {"units": ["plan.work"]}, "ACCEPTED", actor=OWNER,
                        basis=[content("plan.work.objective", objective), content("plan.work.item", item, "PLAN_CONTROL")],
                        fields={"objective": {"unit": "plan.work.objective", "rev": objective},
                                "items": [{"unit": "plan.work.item", "rev": item}]})

    def test_tightening_keeps_it_current_and_any_other_change_does_not(self) -> None:
        for after, prose, expected in ((item_block(write_scope='["src/solver.py"]'), "Make the solver adaptive.\n", T),
                                       (item_block(), "Make the solver adaptive, quickly.\n", F),
                                       (item_block(budget=4), "Make the solver adaptive.\n", F)):
            with self.subTest(after=after[-60:], prose=prose):
                sc = scenario(item_block())
                acceptance = self.accept(sc)
                sc.admit(acceptance)
                self.assertEqual(sc.derive().current(acceptance["id"]), T)
                sc.absorb({"plans/work.md": plan_text(after, prose=prose)})
                self.assertEqual(sc.derive().current(acceptance["id"]), expected)


class PartitionLint(unittest.TestCase):
    def test_partition_lint(self) -> None:
        # S5 §13 partition_lint: (exact, overlapping obligations, overlapping scopes, cyclic order) -> (T, F, F, F)
        view = scenario(item_block()).derive().s.view
        a, _ = resolve(view, ["src/solver.py"])
        b, _ = resolve(view, ["src/io.py"])
        item = a + b
        self.assertEqual(partition_violations({"o1", "o2"}, item, [({"o1"}, a), ({"o2"}, b)], {(0, 1)}, view), [])
        self.assertTrue(partition_violations({"o1", "o2"}, item, [({"o1"}, a), ({"o1", "o2"}, b)], set(), view))
        self.assertTrue(partition_violations({"o1", "o2"}, item, [({"o1"}, a + b), ({"o2"}, b)], set(), view))
        self.assertTrue(partition_violations({"o1", "o2"}, item, [({"o1"}, a), ({"o2"}, b)], {(0, 1), (1, 0)}, view))

    def test_repartition_lint_over_undischarged(self) -> None:
        # S5 §13 repartition_lint_over_undischarged: checked against the obligations undischarged at admission
        view = scenario(item_block()).derive().s.view
        b, _ = resolve(view, ["src/io.py"])
        a, _ = resolve(view, ["src/solver.py"])
        self.assertEqual(partition_violations({"o1", "o2"}, a + b, [({"o2"}, b)], set(), view, undischarged={"o2"}), [])
        self.assertTrue(partition_violations({"o1", "o2"}, a + b, [({"o2"}, b)], set(), view))


if __name__ == "__main__":
    unittest.main()
