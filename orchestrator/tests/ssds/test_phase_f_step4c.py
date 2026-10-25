"""Phase F step 4c-i: the frame at the head, its one write set, and ``id(X)`` (plan §3.1 4c-i, reading F17).

Expected values come from catalogue §1.2 (the write set compares ``T_n`` under ``Σ_n`` with ``M_n(X)``), §7.1
(``id(X)``), §7.3 (currency after integration) and §10.4/SD-40 (an integrated enactment's conformance is settled),
never from the code under test.
"""

from __future__ import annotations

import unittest

from ssds.derivation import State, Workflow
from ssds.derivation.conformance import CLEAN
from ssds.derivation.frames import Frame, Transformation, frame_of, transformation_of
from ssds.ledger.read import transformation_id, with_id

from ._fixtures import record, tree
from ._scenario import OWNER, Scenario, agent, fresh, integrate, judgment
from ._scenario import submit as submit_x
from .test_conformance import accepted_plan, conformance, submit

SOLVED = {"src/solver.py": "def step():\n    return 2\n"}


def framed_evidence(sc, x: str, candidate: str) -> None:
    """A realization and its passing assessment declaring ``X``'s frame (§7.5)."""

    spec_rev = sc.rev("tests.conv")
    real = with_id(record("REALIZATION", target={"spec": {"unit": "tests.conv", "rev": spec_rev}, "claim": []},
                          outcome="COMPLETE", actor="machinery:runner-ci", actor_class="MACHINERY",
                          fields={"execution": {"tree": candidate, "units": [], "reads": []}, "configuration": {}},
                          frame={"transformation": x}))
    sc.admit(real)
    sc.admit(judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": "o1"}, "PASS", actor=OWNER,
                      fields={"mode": "ORDINARY", "reading": {"unit": "tests.conv", "rev": spec_rev}},
                      frame={"transformation": x}))


class WriteSetAtTheHead(unittest.TestCase):
    """§1.2: the write set is computed at the admitted head, so a change admitted concurrently since ``B``
    never enters it, and a pending result's conformance is read at each head (reading F17)."""

    def test_a_change_already_on_the_head_is_not_in_the_write_set(self) -> None:
        sc = accepted_plan()
        x, cand, result = submit(sc, SOLVED)
        w, c = conformance(sc, result)
        self.assertIn("src", c.writes, "at the base's head, the candidate's change is the effect")
        # the same change integrates by another task, with another file (so another tree and transformation): on
        # T_n it is already there, so M_n(X) = T_n for that file
        sc.integrate({**SOLVED, "records.md": "# Records changed elsewhere\n"}, agent("other"), "task-other")
        w, c = conformance(sc, result)
        self.assertNotIn("src", c.writes, "the base-to-candidate set would still hold it")
        self.assertEqual(c.writes, c.frame.write_set, "one owner: the frame's")
        self.assertEqual(c.changed_files, {})

    def test_a_concurrent_write_outside_scope_is_not_the_requests(self) -> None:
        sc = accepted_plan()
        _, cand, result = submit(sc, SOLVED)
        sc.integrate({"records.md": "# Records changed elsewhere\n"}, agent("other"), "task-other")
        _, c = conformance(sc, result)
        self.assertNotIn("records", c.writes)
        self.assertEqual(c.outside_scope(c.contract[0]), [])

    def test_the_write_scope_resolves_on_the_merged_tree(self) -> None:
        """A write scope naming a unit resolves to that unit's region in ``M_n(X)``, where a concurrent file has
        joined it; resolved on ``tree(C)`` it would miss that file and call the unit outside its own scope."""

        from .test_conformance import SECONDARY
        from .test_lint import item_block

        sc = accepted_plan(item_block(secondary=SECONDARY, write_scope='["src"]', affected='["src"]'))
        _, cand, result = submit(sc, SOLVED)
        sc.integrate({"src/extra.py": "def more():\n    return 4\n"}, agent("other"), "task-other")
        _, c = conformance(sc, result)
        self.assertEqual(c.outside_scope(c.contract[0]), [])


NESTED = '''
    [[unit]]
    id = "s1"
    kind = "D3"
    role = "composite"
    scope = [{ prefix = "pkg/" }]
    [[unit]]
    id = "p"
    part_of = "s1"
    role = "composite"
    subject = false
    scope = [{ prefix = "pkg/sub/" }]
    [[unit]]
    id = "u"
    part_of = "p"
    subject = false
    scope = [{ file = "pkg/sub/u.py" }]
'''
NESTED_FILES = {"pkg/a.py": "a = 1\n", "pkg/sub/u.py": "u = 1\n", "theory.md": "t\n"}


def frame_for(sc: Scenario, manifest: str, files: dict[str, str]) -> Frame:
    d = sc.derive()
    candidate = sc.add_tree(tree(files, manifest))
    return Frame(d.s.h, d.s.n, Transformation(transformation_id(sc.head, candidate), sc.head, candidate), None)


class FrameWriteSet(unittest.TestCase):
    """Review 2280eae B2: the frame's write set compares two structures and two mode maps (§1.2)."""

    def test_a_new_subject_over_unchanged_content_is_in_it(self) -> None:
        sc = Scenario(NESTED, NESTED_FILES)
        frame = frame_for(sc, NESTED + '''
    [[unit]]
    id = "w"
    kind = "D1"
    subject = true
    scope = [{ file = "theory.md" }]
''', NESTED_FILES)
        self.assertTrue(frame.exists)
        self.assertIn("w", frame.write_set, "§1.2: a newly declared unit is in it, read under the merged structure")

    def test_a_governance_signature_changed_only_by_mode_is_in_it(self) -> None:
        sc = Scenario(NESTED, NESTED_FILES, modes={"s1": {"mode": "LEGACY", "ruleset": "ssds-rules/1"}})
        promoted = NESTED.replace('''id = "p"
    part_of = "s1"
    role = "composite"
    subject = false''', '''id = "p"
    part_of = "s1"
    role = "composite"
    subject = true
    kind = "D3"''')
        frame = frame_for(sc, promoted, NESTED_FILES)
        self.assertTrue(frame.exists)
        # u's governing subject moves from s1 (LEGACY) to p, which takes genesis's "*" mode: only its mode differs
        self.assertIn("u", frame.write_set)

    def test_an_effect_arising_only_where_the_candidate_meets_the_head(self) -> None:
        doc = '''
    [[unit]]
    id = "doc"
    kind = "D3"
    subject = true
    scope = [{ path = "doc.md" }]
'''
        sc = Scenario(doc, {"doc.md": "d0\n", "more.md": "m0\n"})
        x, candidate, _ = submit_x(sc, {"more.md": "m1\n"}, agent("maker"), "task-x")
        # concurrently, doc's scope widens over more.md, with its structural delta admitted
        widened = doc.replace('[{ path = "doc.md" }]', '[{ path = "doc.md" }, { path = "more.md" }]')
        y, cy, _ = submit_x(sc, {}, agent("other"), "task-y", manifest=widened)
        integrate(sc, y, cy)
        d = sc.derive()
        frame = frame_of(d.s, transformation_of(d.s, x))
        self.assertIn("doc", frame.write_set, "more.md is doc's only on the head, where C's edit meets it")
        self.assertEqual(Frame(d.s.h, d.s.position_of(_result_of(d, x)), transformation_of(d.s, x), None).write_set,
                         {}, "at its own base the edit owned by nothing reaches no unit")

    def test_a_historical_state_reads_the_frame_at_its_own_head(self) -> None:
        sc = Scenario('''
    [[unit]]
    id = "doc"
    kind = "D3"
    subject = true
    scope = [{ path = "doc.md" }]
''', {"doc.md": "d0\n"})
        x, candidate, result = submit_x(sc, {"doc.md": "d1\n"}, agent("maker"), "task-x")
        sc.admit(judgment("FINDING", {"units": ["doc"]}, None, fields={"materiality": "ROUTINE"}))
        integrate(sc, x, candidate)
        d = sc.derive()
        submitted = d.s.position_of(result["id"])
        then = State(d.s.h, submitted)
        self.assertEqual(frame_of(then, transformation_of(then, x)).n, submitted,
                         "an integration after the state's position is not yet one")
        self.assertEqual(frame_of(d.s, transformation_of(d.s, x)).n, d.s.n - 1)


def _result_of(d, x: str) -> str:
    return next(r for r in d.s.of_kind("TASK_RESULT") if d.s.record(r)["target"].get("transformation") == x)


class FirstSubmittingResult(unittest.TestCase):
    """Review 2280eae B1: one predicate decides the result that submits ``X`` for every owner (§7.1)."""

    def test_a_result_naming_x_with_another_candidate_claims_nothing(self) -> None:
        sc = accepted_plan()
        base = sc.head
        cand = sc.add_tree(tree(dict(sc.files, **SOLVED), sc.manifest))
        real = transformation_id(base, cand)
        other = sc.add_tree(tree(dict(sc.files, **{"src/solver.py": "def step():\n    return 9\n"}), sc.manifest))
        forged = with_id({**record("TASK_RESULT", target={"task": "task-evil", "candidate": other, "transformation": real,
                                                          "base": base},
                                   outcome="COMPLETE", actor=agent("evil"), actor_class="AGENT",
                                   frame={"transformation": real}, fields={"slots": {}}),
                          "binding": fresh(agent("evil"), "task-evil")})
        sc.admit(forged)
        x, _, result = submit(sc, SOLVED)
        self.assertEqual(x, real)
        d = sc.derive()
        self.assertEqual(transformation_of(d.s, x).candidate, cand)
        self.assertEqual(d.s.enactment(x), "task-1")
        self.assertEqual(Workflow(d).submitting_result(x), result["id"])

    def test_a_forged_first_result_authors_nothing(self) -> None:
        """Review 64a0330 B1: the lineage that authors ``X``'s content is the submitting result's, so a maker's
        review of its own work stays non-independent whatever an earlier result naming ``id(X)`` claims."""

        from ._scenario import attested

        sc = accepted_plan()
        x = transformation_id(sc.head, sc.add_tree(tree(dict(sc.files, **SOLVED), sc.manifest)))
        evil = agent("evil")
        forged = with_id({**record("TASK_RESULT", target={"task": "task-evil", "transformation": x}, outcome="COMPLETE",
                                   actor=evil, actor_class="AGENT", fields={"slots": {}}),
                          "binding": fresh(evil, "task-evil")})
        sc.admit(forged)
        submitted, _, _ = submit(sc, SOLVED)
        self.assertEqual(submitted, x)
        maker = agent("maker")
        review = judgment("REVIEW", {"transformation": x}, "PASS", actor=maker, actor_class="AGENT",
                          binding=fresh(maker, "task-review"))
        sc.admit(*attested(review))
        d = sc.derive()
        self.assertEqual(d.s.h.makers(x, d.s.n), [maker])
        self.assertTrue(d.j.nonind(review["id"]), "A5: no actor reviews its own work")

    def test_malformed_adopted_elements_submit_nothing_and_never_crash(self) -> None:
        """Review 64a0330 B3: derivation is total over schema-valid ``adopts``; Admission's producing context too."""

        from ssds.admission.checks import producing_context
        from ssds.ledger.read import record_violations, submits

        sc = accepted_plan()
        base = sc.head
        cand = sc.add_tree(tree(dict(sc.files, **SOLVED), sc.manifest))
        target = {"task": "task-odd", "candidate": cand, "base": base, "transformation": transformation_id(base, cand),
                  "adopts": [{"note": 1}]}
        odd = with_id({**record("TASK_RESULT", target=target, outcome="COMPLETE", actor=agent("odd"),
                                actor_class="AGENT", fields={"slots": {}}), "binding": fresh(agent("odd"), "task-odd")})
        self.assertEqual(record_violations(odd), [], "schema 1 admits any JSON object as an element")
        self.assertFalse(submits(target))
        sc.admit(odd)
        self.assertEqual(sc.derive().s.enactment(target["transformation"]), None)
        self.assertIsNone(producing_context(odd), "a result that submits nothing claims no producing context")


class IntegratedEnactment(unittest.TestCase):
    """Reading F17: an integrated enactment's tree facts are fixed at its integrating head and its frame records
    are current in the admitted state (catalogue §7.3), so later heads, an overlapping edit included, change
    nothing (§10.4, SD-40)."""

    def test_conformance_of_an_integrated_result_is_unchanged_by_later_heads(self) -> None:
        sc = accepted_plan()
        x, cand, result = submit(sc, SOLVED)
        framed_evidence(sc, x, cand)
        _, before = conformance(sc, result)
        self.assertEqual(before.classes, frozenset({CLEAN}), before.hits)
        integrate(sc, x, cand)
        # an edit overlapping the candidate's hunk: M_n(X) at the new head would conflict
        sc.integrate({"src/solver.py": "def step():\n    return 3\n"}, agent("later"), "task-later")
        _, after = conformance(sc, result)
        self.assertTrue(after.frame.exists, "the frame is the one its integration merged")
        self.assertEqual(after.writes, before.writes)
        self.assertEqual(after.classes, frozenset({CLEAN}), "the framed assessment is read in the admitted state")


class TransformationIdentity(unittest.TestCase):
    """Catalogue §7.1: ``id(X) = sha256("ssds.transformation.v1" ‖ B ‖ C ‖ JCS(sorted A))``."""

    B, C = "a" * 40, "b" * 40

    def test_the_identity_covers_the_adopted_deltas_in_any_order(self) -> None:
        import hashlib

        expected = "sha256:" + hashlib.sha256(b"ssds.transformation.v1" + self.B.encode() + self.C.encode()
                                              + b"[]").hexdigest()
        self.assertEqual(transformation_id(self.B, self.C), expected)
        one = {"key": ["u", "kind"], "value": "D4"}
        two = {"key": ["v", "kind"], "value": "D3"}
        self.assertNotEqual(transformation_id(self.B, self.C, [one]), expected)
        self.assertEqual(transformation_id(self.B, self.C, [one, two]), transformation_id(self.B, self.C, [two, one]))
        self.assertEqual(transformation_id(self.B, self.C, [one, one]), transformation_id(self.B, self.C, [one]), "a set")
        self.assertEqual(transformation_id(self.B, self.C, [{**one, "note": "x"}]), transformation_id(self.B, self.C, [one]))

    def test_a_result_naming_another_identity_fixes_nothing(self) -> None:
        sc = accepted_plan()
        x, cand, result = submit(sc, SOLVED)
        d = sc.derive()
        self.assertIsNotNone(transformation_of(d.s, x))
        forged = "sha256:" + "f" * 64
        bogus = with_id({**result, "target": {**result["target"], "transformation": forged, "task": "task-2"},
                         "frame": {"transformation": forged}})
        sc.admit(bogus)
        self.assertIsNone(transformation_of(sc.derive().s, forged))


if __name__ == "__main__":
    unittest.main()
