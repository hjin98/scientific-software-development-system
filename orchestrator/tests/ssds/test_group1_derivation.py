"""Acceptance group 1 (derivation half): cycle legality, closure, quarantine, tenure and the S0 history fold.

Expectations are transcribed by hand from ``cases_s5_2_4.py`` (named per test) and
from Manual §1.6, §2.4-§2.5 and §4.5-§4.6. The owner exercised is ``ssds.derivation``.
"""

from __future__ import annotations

import unittest

from ssds.content import TreeView, decl_to_json
from ssds.derivation.history import History, manifest_decl
from ssds.derivation.s0 import StructureFacts

from ._fixtures import admission_body, chain_of, commit_id, genesis_body, structure_of, view
from ._fixtures import manifest as _manifest, tree as _tree


# Group 1's cases are written over manifests without the reserved leaves of §1.8: they check the content and
# derivation primitives, uncovered region included, not frames or Admission (plan reading F18, fixtures).


def tree(files, manifest_text=None, reserved=False):
    return _tree(files, manifest_text, reserved)


def manifest(text, reserved=False):
    return _manifest(text, reserved)


def facts(t) -> StructureFacts:
    v = view(t)
    return StructureFacts(v, manifest_decl(v))


PARTS = '''
    [[unit]]
    id = "s"
    kind = "D2"
    role = "composite"
    scope = [{ path = "s.md" }]
    [[unit]]
    id = "s.a"
    subject = false
    part_of = "s"
    scope = [{ file = "s.md", heading = ["A"] }]
    [[unit]]
    id = "s.b"
    subject = false
    part_of = "s"
    scope = [{ file = "s.md", heading = ["B"] }]
'''


def two_parts(rels_a: str, rels_b: str, sdg: str = "") -> StructureFacts:
    text = f"# A\n{rels_a}x\n# B\n{rels_b}y\n{sdg}"
    return facts(tree({"s.md": text}, PARTS))


def cycle_codes(f: StructureFacts) -> set[str]:
    return {d.code for d in f.defects if d.code == "ILLEGAL_CYCLE"}


class CycleLegality(unittest.TestCase):
    """cases_s5_2_4.py cycle cases (Manual §2.4)."""

    REL = "<!-- ssds:rel {t} {o} -->\n"
    SDG = "<!-- ssds:sdg {g} {m} -->\n"

    def test_definitional_cycle_in_one_sdg(self) -> None:
        f = two_parts(self.REL.format(t="USES_DEFINITION", o="s.b"), self.REL.format(t="USES_DEFINITION", o="s.a"),
                      "")
        legal = facts(tree({"s.md": "# A\n" + self.REL.format(t="USES_DEFINITION", o="s.b") + "x\n# B\n"
                            + self.REL.format(t="USES_DEFINITION", o="s.a") + "y\n"},
                           PARTS + '[unit.semantic]\nsdg = [{ id = "core", members = ["s.a", "s.b"] }]\n'))
        self.assertEqual(cycle_codes(legal), set(), "legal inside one SDG")
        self.assertEqual(cycle_codes(f), {"ILLEGAL_CYCLE"}, "without the SDG the same cycle is illegal")

    def _with_sdg(self, rel_a: str, rel_b: str, groups: str) -> StructureFacts:
        return facts(tree({"s.md": "# A\n" + rel_a + "x\n# B\n" + rel_b + "y\n"},
                          PARTS + f"[unit.semantic]\nsdg = [{groups}]\n"))

    def test_warrant_cycle_illegal(self) -> None:
        f = self._with_sdg(self.REL.format(t="DERIVED_FROM", o="s.b"), self.REL.format(t="DERIVED_FROM", o="s.a"),
                           '{ id = "core", members = ["s.a", "s.b"] }')
        self.assertEqual(cycle_codes(f), {"ILLEGAL_CYCLE"})

    def test_mixed_cycle_illegal(self) -> None:
        f = self._with_sdg(self.REL.format(t="USES_DEFINITION", o="s.b"), self.REL.format(t="DERIVED_FROM", o="s.a"),
                           '{ id = "core", members = ["s.a", "s.b"] }')
        self.assertEqual(cycle_codes(f), {"ILLEGAL_CYCLE"})

    def test_cycle_across_sibling_sdgs(self) -> None:
        f = self._with_sdg(self.REL.format(t="USES_DEFINITION", o="s.b"), self.REL.format(t="USES_DEFINITION", o="s.a"),
                           '{ id = "one", members = ["s.a"] }, { id = "two", members = ["s.b"] }')
        self.assertEqual(cycle_codes(f), {"ILLEGAL_CYCLE"})

    def test_code_recursion_neutral(self) -> None:
        units = '''
            [[unit]]
            id = "pa"
            kind = "D4"
            scope = [{ path = "pkg/a.py" }]
            [[unit]]
            id = "pb"
            kind = "D4"
            scope = [{ path = "pkg/b.py" }]
        '''
        f = facts(tree({"pkg/a.py": "from pkg import b\n", "pkg/b.py": "from pkg import a\n"}, units))
        self.assertEqual({(r.subject, r.type, r.object) for r in f.derived_relations},
                         {("pa", "IMPORTS", "pb"), ("pb", "IMPORTS", "pa")})
        self.assertEqual(cycle_codes(f), set())
        self.assertTrue(f.well_formed("pa") and f.well_formed("pb"))

    def test_challenges_excluded(self) -> None:
        units = '''
            [[unit]]
            id = "home"
            kind = "EVIDENCE_RECORD"
            scope = [{ path = "home.md" }]
            [[unit]]
            id = "claim"
            kind = "D4"
            scope = [{ path = "claim.md" }]
        '''
        f = facts(tree({"home.md": "<!-- ssds:rel CHALLENGES claim inquiry=EXPLORATORY -->\n",
                        "claim.md": "<!-- ssds:rel DEPENDS_ON home -->\n"}, units))
        self.assertEqual(cycle_codes(f), set())


CLOSURE_UNITS = '''
    [[unit]]
    id = "a"
    kind = "D4"
    scope = [{ path = "pair/a.md" }]
    [[unit]]
    id = "b"
    kind = "D4"
    scope = [{ path = "pair/b.md" }]
    [[unit]]
    id = "c"
    kind = "D4"
    scope = [{ path = "solo/c.md" }]
    [[unit]]
    id = "d"
    kind = "D4"
    scope = [{ path = "other/d.md" }]
'''
WARRANT = frozenset({"WARRANT"})


class Closure(unittest.TestCase):
    """cases_s5_2_4.py closure cases (Manual §4.6). The completeness currency S2 supplies is given directly."""

    def setUp(self) -> None:
        self.f = facts(tree({"pair/a.md": "<!-- ssds:rel DEPENDS_ON b -->\n", "pair/b.md": "b\n", "solo/c.md": "c\n",
                             "other/d.md": "d\n"}, CLOSURE_UNITS))
        self.all = frozenset({"a", "b", "c", "d"})

    def closure(self, start, judged):
        return self.f.closure(start, WARRANT, lambda scope, cls: frozenset(scope) in judged)

    def test_the_enclosing_chain(self) -> None:
        self.assertEqual(self.f.chain("a"), [frozenset({"a"}), frozenset({"a", "b"}), self.all])
        self.assertEqual(self.f.chain("c"), [frozenset({"c"}), self.all])

    def test_closure_bounded_by_judgments(self) -> None:
        self.assertEqual(self.closure(["a"], {frozenset({"a"}), frozenset({"b"})}), (frozenset({"a", "b"}), False))

    def test_closure_widens_to_composite(self) -> None:
        self.assertEqual(self.closure(["a"], {frozenset({"a", "b"})}), (frozenset({"a", "b"}), False))

    def test_closure_unbounded_without_judgments(self) -> None:
        self.assertEqual(self.closure(["a"], set()), (self.all, True))

    def test_closure_order_independent(self) -> None:
        judged = {frozenset({"a"}), frozenset({"b"})}
        self.assertEqual(self.closure(["a", "c"], judged), self.closure(["c", "a"], judged))

    def test_losing_a_judgment_only_widens(self) -> None:
        both = self.closure(["a"], {frozenset({"a"}), frozenset({"b"})})[0]
        fewer = self.closure(["a"], {frozenset({"a"})})[0]
        self.assertTrue(fewer >= both)


class WellFormedness(unittest.TestCase):
    def test_layer_subject_kind_unknown_type_and_single_definer(self) -> None:
        units = '''
            [[unit]]
            id = "theory"
            kind = "D1"
            scope = [{ path = "theory.md" }]
            [[unit]]
            id = "code"
            kind = "D4"
            scope = [{ path = "code.md" }]
        '''
        ascending = facts(tree({"theory.md": "<!-- ssds:rel DEPENDS_ON code -->\n", "code.md": "x\n"}, units))
        self.assertIn("RELATION_LAYER", {d.code for d in ascending.defects})
        self.assertFalse(ascending.well_formed("theory"))
        descending = facts(tree({"theory.md": "t\n", "code.md": "<!-- ssds:rel CONCRETIZES theory -->\n"}, units))
        self.assertTrue(descending.well_formed("code"))
        unknown = facts(tree({"theory.md": "<!-- ssds:rel RELATED_TO code -->\n", "code.md": "x\n"}, units))
        self.assertIn("RELATION_UNKNOWN_TYPE", {d.code for d in unknown.defects})
        wrong_subject = facts(tree({"theory.md": "<!-- ssds:rel EVIDENCES code -->\n", "code.md": "x\n"}, units))
        self.assertIn("RELATION_SUBJECT_KIND", {d.code for d in wrong_subject.defects})
        authored_structural = facts(tree({"theory.md": "t\n", "code.md": "<!-- ssds:rel IMPORTS theory -->\n"}, units))
        self.assertIn("RELATION_CLASS", {d.code for d in authored_structural.defects})
        two = facts(tree({"theory.md": "<!-- ssds:defines heat -->\n", "code.md": "<!-- ssds:defines heat -->\n"}, units))
        self.assertFalse(two.well_formed("theory") or two.well_formed("code"))


class QuarantineAndHistory(unittest.TestCase):
    UNITS = '''
        [[unit]]
        id = "doc"
        kind = "D3"
        role = "composite"
        scope = [{ path = "doc.md" }]
    '''

    def test_quarantine_and_governance_affecting_classification(self) -> None:
        part = self.UNITS + '''
            [[unit]]
            id = "doc.a"
            subject = false
            part_of = "doc"
            scope = [{ file = "doc.md", heading = ["A"] }]
        '''
        admitted = structure_of(tree({}, part))
        repartition = tree({"doc.md": "# A\nx\n# B\ny\n# C\nz\n"}, part.replace(
            'scope = [{ file = "doc.md", heading = ["A"] }]', 'scope = [{ file = "doc.md", heading = ["A"] }, { file = "doc.md", heading = ["C"] }]'))
        f = StructureFacts(TreeView(repartition, admitted), manifest_decl(view(repartition)))
        self.assertEqual(set(f.quarantine), {("doc.a", "scope")})
        self.assertFalse(f.governance_affecting(("doc.a", "scope")), "a re-partition inside one subject's regions")
        self.assertEqual(f.affected_subjects, frozenset())
        new_part = tree({"doc.md": "# A\nx\n# B\ny\n"}, part + '''
            [[unit]]
            id = "doc.b"
            subject = false
            part_of = "doc"
            scope = [{ file = "doc.md", heading = ["B"] }]
        ''')
        n = StructureFacts(TreeView(new_part, admitted), manifest_decl(view(new_part)))
        self.assertTrue(all(n.governance_affecting(k) for k in n.quarantine),
                        "each key of a new unit alone is statically invalid, so governance-affecting (§1.6)")
        admitted = structure_of(tree({}, self.UNITS))
        carve = tree({"doc.md": "# A\nx\n# B\ny\n"}, self.UNITS + '''
            [[unit]]
            id = "doc.a"
            kind = "D2"
            part_of = "doc"
            scope = [{ file = "doc.md", heading = ["A"] }]
        ''')
        g = StructureFacts(TreeView(carve, admitted), manifest_decl(view(carve)))
        self.assertTrue(any(g.governance_affecting(k) for k in g.quarantine), "a nested subject of another kind")
        self.assertIn("doc", g.affected_subjects)
        broken = tree({"doc.md": "x\n", ".ssds/manifest.toml": b"schema = [\n"})
        h = StructureFacts(TreeView(broken, admitted), manifest_decl(TreeView(broken, admitted)))
        self.assertEqual(h.quarantine, frozenset(admitted.decl), "an unparsed manifest quarantines every key")

    def test_effective_structure_is_a_fold_over_admitted_entries(self) -> None:
        t0 = tree({"doc.md": "x\n"}, self.UNITS)
        t1 = tree({"doc.md": "y\n"}, self.UNITS)
        trees = {commit_id("t0"): t0, commit_id("t1"): t1}
        sigma0 = decl_to_json(structure_of(t0).decl)
        delta = {"key": ["doc.p", "scope"], "value": [{"file": "doc.md"}], "source": "AUTHORED"}
        chain = chain_of("demo", [
            genesis_body(commit_id("t0"), sigma0),
            admission_body(1, commit_id("t0"), commit_id("t1"), deltas=[delta]),
            admission_body(2, commit_id("t1"), commit_id("t1"), decision="REJECT"),
        ])
        history = History(chain, trees.__getitem__)
        self.assertEqual([history.head(k) for k in (0, 1, 2)], [commit_id("t0"), commit_id("t1"), commit_id("t1")])
        self.assertNotIn(("doc.p", "scope"), history.sigma(0))
        self.assertIn(("doc.p", "scope"), history.sigma(1))
        self.assertIn(1, history.integrations)
        self.assertNotIn(2, history.integrations, "a rejected request enacts nothing")


if __name__ == "__main__":
    unittest.main()
