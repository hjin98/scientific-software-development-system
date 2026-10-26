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

from ._fixtures import manifest, record, tree
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
        # u's governing subject moves from s1 (LEGACY) to p, which takes genesis's "*" mode: only its mode differs
        self.assertIn("u", frame.write_set)
        # and such a move needs its MODE_TRANSITION, so the frame does not exist (§19.1; 4c-ii)
        self.assertIn("STRUCT_MODE_MIXED", {f.code for f in frame.structural.findings})
        self.assertFalse(frame.exists)

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
        self.assertEqual(set(Frame(d.s.h, d.s.position_of(_result_of(d, x)), transformation_of(d.s, x), None).write_set),
                         {"ssds.unclassified"}, "at its own base the edit reaches only the outermost owner (§1.8)")

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

    def test_a_forged_first_result_fixes_no_judged_scope(self) -> None:
        """Re-check dcae3e9: the binding that fixes a review's judged scope ``J`` (write scope, item key) and the
        §7.1 producing-context check read only results that submit ``X``."""

        def judged(forge: bool):
            sc = accepted_plan()
            x = transformation_id(sc.head, sc.add_tree(tree(dict(sc.files, **SOLVED), sc.manifest)))
            if forge:
                evil = agent("evil")
                sc.admit(with_id({**record("TASK_RESULT", target={"task": "task-evil", "transformation": x},
                                           outcome="COMPLETE", actor=evil, actor_class="AGENT", fields={"slots": {}}),
                                  "binding": dict(fresh(evil, "task-evil"), write_scope=["records"])}))
            submit(sc, SOLVED)
            review = judgment("REVIEW", {"transformation": x}, "PASS")
            sc.admit(review)
            d = sc.derive()
            return sorted(d.j.judged_content(review["id"])), d.j.binding_conflicts(x)

        self.assertEqual(judged(True), judged(False))
        self.assertEqual(judged(False)[1], False)
        self.assertTrue(judged(False)[0], "the review judges the candidate's change")

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


LAYERED = '''
    [[unit]]
    id = "theory"
    kind = "D1"
    scope = [{ path = "theory.md" }]
    [[unit]]
    id = "doc"
    kind = "D3"
    scope = [{ path = "doc.md" }]
    [[unit]]
    id = "code"
    kind = "D4"
    scope = [{ prefix = "src/" }]
'''
LAYERED_FILES = {"theory.md": "# Theory\n", "doc.md": "# Doc\n", "src/a.py": "a = 1\n"}


def codes(frame: Frame) -> set[str]:
    return {f.code for f in frame.structural.findings}


class StructuralOwner(unittest.TestCase):
    """Step 4c-ii: §8.3 step 4 (a)-(c) at one owner, which ``Frame.exists`` and Admission read (catalogue §7.4)."""

    def test_a_clean_change_exists(self) -> None:
        sc = Scenario(LAYERED, LAYERED_FILES)
        frame = frame_for(sc, LAYERED, {**LAYERED_FILES, "doc.md": "# Doc\nmore\n"})
        self.assertEqual(frame.structural.findings, ())
        self.assertTrue(frame.exists)
        self.assertEqual(frame.structural.sigma, dict(sc.derive().s.h.sigma(sc.derive().s.n)))

    def quarantined(self):
        """``doc``'s scope changed by an absorbed (foreign) commit: the key is in ``Q_n``, ``Σ`` unchanged."""

        sc = Scenario(LAYERED, LAYERED_FILES)
        foreign = LAYERED.replace('scope = [{ path = "doc.md" }]', 'scope = [{ path = "doc.md" }, { path = "more.md" }]')
        sc.manifest = foreign
        sc.absorb({"more.md": "m\n"})
        return sc, foreign

    def test_per_key_classes_against_the_quarantine(self) -> None:
        sc, foreign = self.quarantined()
        files = {**LAYERED_FILES, "more.md": "m\n"}
        key = ("doc", "scope")
        carried = frame_for(sc, foreign, {**files, "src/a.py": "a = 2\n"})  # C was built over T_n: it keeps the value
        self.assertEqual(carried.structural.classes.get(key), "CARRIED")
        realigned = frame_for(sc, LAYERED, files)
        self.assertEqual(realigned.structural.classes.get(key), "REALIGNED")
        third = LAYERED.replace('scope = [{ path = "doc.md" }]', 'scope = [{ path = "more.md" }]')
        changed = frame_for(sc, third, files)
        self.assertEqual(changed.structural.classes.get(key), "REVALIDATE")
        self.assertIn("STRUCT_REVALIDATE", codes(changed))
        self.assertFalse(changed.exists)

    def test_a_quarantined_value_authored_by_c_routes_to_revalidation(self) -> None:
        """Plan revision 7 R4: the frame would show ``C``'s value while integration carries ``Σ_n``'s (§7.2)."""

        sc = Scenario(LAYERED, LAYERED_FILES)
        foreign = LAYERED.replace('scope = [{ path = "doc.md" }]', 'scope = [{ path = "doc.md" }, { path = "more.md" }]')
        d = sc.derive()
        base = sc.head
        candidate = sc.add_tree(tree({**LAYERED_FILES, "more.md": "m\n"}, foreign))  # C authors the widening
        sc.manifest = foreign
        sc.absorb({"more.md": "m\n"})  # the same value arrives foreign, quarantined
        d = sc.derive()
        frame = Frame(d.s.h, d.s.n, Transformation(transformation_id(base, candidate), base, candidate), None)
        self.assertEqual(frame.structural.classes.get(("doc", "scope")), "CARRIED")
        self.assertIn("STRUCT_REVALIDATE", codes(frame))
        self.assertFalse(frame.exists)

    def test_well_formedness_codes(self) -> None:
        sc = Scenario(LAYERED, LAYERED_FILES)
        overlap = LAYERED + '''
    [[unit]]
    id = "doc2"
    kind = "D3"
    scope = [{ path = "doc.md" }]
'''
        self.assertIn("STRUCT_SIBLING_OVERLAP", codes(frame_for(sc, overlap, LAYERED_FILES)))
        missing = LAYERED + '''
    [[unit]]
    id = "ghost"
    kind = "D3"
    scope = [{ file = "ghost.md" }]
'''
        self.assertIn("STRUCT_TERM_UNRESOLVED", codes(frame_for(sc, missing, LAYERED_FILES)))
        rekinded = LAYERED.replace('id = "doc"\n    kind = "D3"', 'id = "doc"\n    kind = "D2"')
        self.assertIn("SCHEMA_UNSUPPORTED", codes(frame_for(sc, rekinded, LAYERED_FILES)), "F16 (ii): no release")
        unparsed = frame_for(sc, "[[unit\n", LAYERED_FILES)
        self.assertFalse(unparsed.exists, "a manifest that does not parse merges by no key: no frame (§7.2)")

    def test_adoption_fails_closed(self) -> None:
        sc = Scenario(LAYERED, LAYERED_FILES)
        d = sc.derive()
        x = Transformation("sha256:" + "a" * 64, sc.head, sc.head, ((("doc", "kind"), "D3"),))
        self.assertIn("SCHEMA_UNSUPPORTED", codes(Frame(d.s.h, d.s.n, x, None)), "F16 (i): no disposition names a key")

    def test_the_reserved_leaves(self) -> None:
        from ._fixtures import RESERVED_LEAVES

        sc = Scenario(LAYERED, LAYERED_FILES)
        d = sc.derive()
        for leaf in ("ssds.manifest", "ssds.policy", "ssds.unclassified"):
            with self.subTest(dropped=leaf):
                kept = "".join(b for u, b in RESERVED_LEAVES.items() if u != leaf)
                candidate = sc.add_tree(tree({**LAYERED_FILES, ".ssds/manifest.toml": manifest(LAYERED + kept, reserved=False)}))
                frame = Frame(d.s.h, d.s.n, Transformation(transformation_id(sc.head, candidate), sc.head, candidate), None)
                self.assertIn(("STRUCT_RESERVED_LEAF", leaf), {(f.code, f.unit) for f in frame.structural.findings})
                self.assertFalse(frame.exists)
        narrowed = sc.add_tree(tree({**LAYERED_FILES, ".ssds/manifest.toml": manifest(
            LAYERED + RESERVED_LEAVES["ssds.manifest"] + RESERVED_LEAVES["ssds.policy"]
            + RESERVED_LEAVES["ssds.unclassified"].replace('prefix = ""', 'prefix = "docs/"'), reserved=False)}))
        frame = Frame(d.s.h, d.s.n, Transformation(transformation_id(sc.head, narrowed), sc.head, narrowed), None)
        self.assertIn("STRUCT_RESERVED_LEAF", codes(frame))

    def test_the_freeze_at_source_and_destination(self) -> None:
        from ._scenario import challenge

        sc = Scenario(NESTED, NESTED_FILES)
        sc.admit(challenge(sc.triple("s1")))  # an unresolved blocking challenge on s1's current triple
        rescoped = NESTED.replace('scope = [{ prefix = "pkg/" }]', 'scope = [{ prefix = "pkg/" }, { path = "theory.md" }]')
        self.assertIn("FREEZE_SOURCE", codes(frame_for(sc, rescoped, NESTED_FILES)))
        grown = NESTED + '''
    [[unit]]
    id = "q"
    part_of = "s1"
    subject = false
    scope = [{ file = "pkg/a.py" }]
'''
        frame = frame_for(sc, grown, NESTED_FILES)
        self.assertIn("FREEZE_DESTINATION", codes(frame))
        self.assertFalse(frame.exists)
        content_only = frame_for(sc, NESTED, {**NESTED_FILES, "pkg/a.py": "a = 2\n"})
        self.assertFalse(codes(content_only) & {"FREEZE_SOURCE", "FREEZE_DESTINATION"}, "an edit is content")

    def test_semantic_defects_are_read_causally(self) -> None:
        """Reading F15: a defect an affected subject has in the frame and not at the head, keyed by code, unit and
        detail; a foreign one it already has neither refuses the request nor ends the frame."""

        sc = Scenario(LAYERED, LAYERED_FILES)
        ascending = "# Theory\n<!-- ssds:rel DEPENDS_ON code -->\n"
        added = frame_for(sc, LAYERED, {**LAYERED_FILES, "theory.md": ascending})
        self.assertIn("RELATION_LAYER", codes(added))
        self.assertFalse(added.exists)
        sc.absorb({"theory.md": ascending})  # the same defect arrives foreign: S2's, not the request's
        unrelated = frame_for(sc, LAYERED, {**sc.files, "theory.md": ascending + "more\n"})
        self.assertNotIn("RELATION_LAYER", codes(unrelated))
        self.assertTrue(unrelated.exists)
        second = frame_for(sc, LAYERED, {**sc.files, "theory.md": ascending + "<!-- ssds:rel DEPENDS_ON doc -->\n"})
        self.assertIn("RELATION_LAYER", codes(second), "a second same-code defect is new")

    def test_a_defect_on_a_subject_the_request_does_not_affect_is_s2s(self) -> None:
        """§2.5: only an affected subject's new defect refuses; removing the object of an unchanged subject's
        relation leaves that subject ill-formed in S2."""

        files = {**LAYERED_FILES, "src/a.py": "a = 1\n# ssds:rel DEPENDS_ON theory\n"}
        sc = Scenario(LAYERED, files)
        without = LAYERED.replace('''    [[unit]]
    id = "theory"
    kind = "D1"
    scope = [{ path = "theory.md" }]
''', "")
        frame = frame_for(sc, without, files)
        self.assertNotIn("theory", frame.structural.view.structure.units)
        self.assertNotIn("code", frame.write_set)
        self.assertFalse({f.unit for f in frame.structural.findings} & {"code"}, frame.structural.findings)


PARTS3 = '''
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
    [[unit]]
    id = "s.c"
    subject = false
    part_of = "s"
    scope = [{ file = "s.md", heading = ["C"] }]
    [[unit]]
    id = "t"
    kind = "D2"
    scope = [{ path = "t.md" }]
'''
S_FILES = {"s.md": "# A\nx\n# B\ny\n# C\nz\n", "t.md": "t\n"}


class StructuralOwnerCases(unittest.TestCase):
    """Review 2aadf33 B1-B7: the cases its blockers named, one per defect."""

    def test_semantic_codes_under_struct_names(self) -> None:
        sc = Scenario(PARTS3, S_FILES)
        rel = "<!-- ssds:rel {t} {o} -->\n"
        cycle = {**S_FILES, "s.md": "# A\n" + rel.format(t="DERIVED_FROM", o="s.b") + "x\n# B\n"
                 + rel.format(t="DERIVED_FROM", o="s.a") + "y\n# C\nz\n"}
        self.assertIn("STRUCT_ILLEGAL_CYCLE", codes(frame_for(sc, PARTS3, cycle)))
        defined = {**S_FILES, "s.md": "# A\n<!-- ssds:defines heat -->\nx\n# B\ny\n# C\nz\n",
                   "t.md": "<!-- ssds:defines heat -->\nt\n"}
        self.assertIn("STRUCT_SINGLE_DEFINER", codes(frame_for(sc, PARTS3, defined)))
        across = PARTS3 + '[unit.semantic]\nsdg = [{ id = "g", members = ["s.a", "t"] }]\n'
        self.assertIn("STRUCT_SDG_MALFORMED", codes(frame_for(sc, across, S_FILES)), "SDG members never separated")
        crossing = PARTS3 + ('[unit.semantic]\nsdg = [{ id = "g1", members = ["s.a", "s.b"] }, '
                             '{ id = "g2", members = ["s.b", "s.c"] }]\n')
        self.assertIn("STRUCT_SDG_NOT_LAMINAR", codes(frame_for(sc, crossing, S_FILES)))

    def test_a_new_defect_on_a_part_of_an_affected_subject(self) -> None:
        """B3: ``well_formed(s)`` reads every unit of ``s``; editing one part affects ``s``."""

        units = PARTS3.replace('kind = "D2"\n    role = "composite"', 'kind = "D4"\n    role = "composite"')
        files = {**S_FILES, "s.md": "# A\nx\n# B\n<!-- ssds:rel DEPENDS_ON t -->\ny\n# C\nz\n"}
        sc = Scenario(units, files)
        without_t = units[: units.index('    [[unit]]\n    id = "t"')]
        frame = frame_for(sc, without_t, {**files, "s.md": files["s.md"].replace("x\n", "x2\n")})
        self.assertIn("s.a", frame.write_set)
        self.assertIn("s.b", {f.unit for f in frame.structural.findings if f.code.startswith("RELATION_")})
        self.assertFalse(frame.exists)

    def test_the_freeze_counts_nested_subjects_and_every_unresolved_state(self) -> None:
        """B2: a subject nested by ``part_of`` is a member; B7: ``PROVISIONAL`` and ``REVOKED`` freeze too."""

        from ._scenario import adjudication, challenge

        files = {**NESTED_FILES, "pkg/b.py": "b = 1\n"}
        nested = NESTED + '''
    [[unit]]
    id = "n"
    part_of = "s1"
    kind = "D3"
    scope = [{ file = "pkg/b.py" }]
'''
        for state in ("BLOCKED", "PROVISIONAL", "REVOKED"):
            with self.subTest(state=state):
                sc = Scenario(NESTED, files)
                c = challenge(sc.triple("s1"))
                sc.admit(c)
                if state == "PROVISIONAL":
                    sc.admit(judgment("RISK_OVERRIDE", {"record": c["id"]}, None, actor=OWNER,
                                      fields={"continuation": {"subjects": ["s1"], "items": [], "kinds": []}}))
                if state == "REVOKED":
                    sc.admit(adjudication(c["id"], "UPHELD"))
                d = sc.derive()
                self.assertEqual(d.s.status1("triple:s1:" + sc.triple("s1")["scope_id"] + ":" + sc.triple("s1")["rev"]),
                                 state)
                self.assertIn("FREEZE_DESTINATION", codes(frame_for(sc, nested, files)))

    def test_the_freeze_reads_resolution_status_never_files_or_bytes(self) -> None:
        """Reading F20: a file added under a frozen prefix is content, as an edit is."""

        from ._scenario import challenge

        sc = Scenario(NESTED, NESTED_FILES)
        sc.admit(challenge(sc.triple("s1")))
        added = frame_for(sc, NESTED, {**NESTED_FILES, "pkg/new.py": "n = 1\n"})
        self.assertFalse(codes(added) & {"FREEZE_SOURCE", "FREEZE_DESTINATION"})

    def test_a_reserved_leaf_is_a_top_level_leaf(self) -> None:
        """B5: a composite ``ssds.unclassified`` would hide its bytes in its residual."""

        from ssds.derivation.baseline import reserved_leaf_problems

        from ._fixtures import RESERVED_LEAVES, structure_of

        composite = (RESERVED_LEAVES["ssds.manifest"] + RESERVED_LEAVES["ssds.policy"]
                     + RESERVED_LEAVES["ssds.unclassified"].replace('kind = "UNCLASSIFIED"',
                                                                     'kind = "UNCLASSIFIED"\nrole = "composite"')
                     + '\n[[unit]]\nid = "docs"\npart_of = "ssds.unclassified"\nsubject = false\nscope = [{ prefix = "docs/" }]\n')
        problems = reserved_leaf_problems(structure_of(tree({}, composite, reserved=False)))
        self.assertIn("ssds.unclassified", {u for u, _ in problems})

    def test_a_deletion_is_a_write_on_the_head_side(self) -> None:
        """B1: a unit whose bytes leave lies within the scope only if its head region does, for the outermost
        owner and for an ordinary unit."""

        from .test_conformance import SECONDARY
        from .test_lint import item_block

        for scope, extra, gone in (('["src/", "notes/"]', {"README.md": "r\n", "notes/n.md": "n\n"}, "README.md"),
                                   ('["src/solver.py"]', {}, "src/io.py")):
            with self.subTest(deleted=gone):
                sc = accepted_plan(item_block(secondary=SECONDARY, write_scope=scope, affected='["src/"]'))
                if extra:
                    sc.absorb(extra)
                files = dict(sc.files, **SOLVED)
                files.pop(gone)
                x, cand, result = submit_dropping(sc, files)
                _, c = conformance(sc, result)
                self.assertTrue(c.frame.exists)
                self.assertTrue(c.outside_scope(c.contract[0]), f"deleting {gone} is outside {scope}")

    def test_a_frame_that_does_not_exist_derives_what_a_conflict_derives(self) -> None:
        from ssds.derivation.conformance import INCOMPLETE

        sc = accepted_plan()
        ascending = {"numerics.md": "# Numerics\n<!-- ssds:rel DEPENDS_ON src -->\n"}
        _, _, structural = submit(sc, ascending)
        conflicted = accepted_plan()
        _, _, mine = submit(conflicted, {"records.md": "# Mine\n"}, task="task-a")
        conflicted.integrate({"records.md": "# Theirs\n"}, agent("other"), "task-b")
        for flow, result in ((sc, structural), (conflicted, mine)):
            _, c = conformance(flow, result)
            self.assertFalse(c.frame.exists)
            self.assertIn(("BOUNDARY.write_scope", INCOMPLETE, "the candidate's frame does not exist"),
                          {(h.template, h.cls, h.finding) for h in c.hits})

    def test_the_layer_template_still_judges_where_the_frame_exists(self) -> None:
        """B7: an ascending relation already on the head (absorbed) and introduced by ``C`` against ``B`` leaves
        the frame in place (the defect is not new there) and the template reports the candidate's breach."""

        from ssds.derivation.conformance import INCOMPLETE

        from .test_conformance import SECONDARY, realize
        from .test_lint import item_block

        secondary = SECONDARY[:-2] + ', { check = "DOMAIN.layer_direction" } ]'
        sc = accepted_plan(item_block(secondary=secondary, write_scope='["src/", "numerics.md"]',
                                      affected='["src/", "numerics.md"]'))
        ascending = {"numerics.md": "# Numerics\n<!-- ssds:rel DEPENDS_ON src -->\n"}
        _, cand, result = submit(sc, ascending)
        realize(sc, cand)
        sc.absorb(ascending)  # the same change reaches the head foreign
        _, c = conformance(sc, result)
        self.assertTrue(c.frame.exists)
        self.assertIn(INCOMPLETE, {h.cls for h in c.hits if h.template == "DOMAIN.layer_direction"})


class OutermostOwnerRevision(unittest.TestCase):
    """Reading F19 and review 2aadf33 B4, V03, V04: ``ssds.unclassified``'s revision is the bytes it owns, in
    place, with their modes, and no other unit's content or declarations."""

    UNITS = '''
    [[unit]]
    id = "h"
    kind = "D3"
    scope = [{ file = "README.md", heading = ["H"] }]
'''
    TEXT = "# A\na\n## H\nh\n# B\nb\n"

    def rev(self, text: str, mode: str = "100644") -> str:
        from ssds.content import Entry

        from ._fixtures import view

        return view(tree({"README.md": Entry(mode, text.encode())}, self.UNITS)).rev("ssds.unclassified")

    def test_order_modes_and_other_units(self) -> None:
        base = self.rev(self.TEXT)
        self.assertNotEqual(self.rev("# A\na\n# B\nb\n## H\nh\n"), base, "another unit moved past its bytes")
        self.assertEqual(self.rev(self.TEXT.replace("h\n", "h edited\n")), base, "an edit inside another unit")
        self.assertEqual(self.rev(self.TEXT.replace("h\n", "<!-- ssds:rel DEPENDS_ON h -->\nh\n")), base,
                         "another unit's semantic declarations")
        self.assertNotEqual(self.rev(self.TEXT, mode="100755"), base, "the mode of a file it owns bytes of")
        self.assertNotEqual(self.rev(self.TEXT.replace("a\n", "a2\n")), base, "its own bytes")

    def test_two_other_units_swapped_between_its_pieces(self) -> None:
        """Its own pieces stay apart and unchanged; only which owner sits between them changes."""

        from ssds.content import Entry

        from ._fixtures import view

        units = self.UNITS + '''
    [[unit]]
    id = "k"
    kind = "D3"
    scope = [{ file = "README.md", heading = ["K"] }]
'''
        before = "# A\na\n## H\nh\n# B\nb\n## K\nk\n"
        after = "# A\na\n## K\nk\n# B\nb\n## H\nh\n"
        revs = [view(tree({"README.md": Entry("100644", t.encode())}, units)).rev("ssds.unclassified") for t in (before, after)]
        self.assertNotEqual(*revs)

    def test_a_reorder_past_its_bytes_enters_the_write_set(self) -> None:
        """Re-check ad8daeb N-a: the write set compares its content in the revision's one form (§1.5)."""

        from ssds.content import Entry

        units = self.UNITS + '''
    [[unit]]
    id = "k"
    kind = "D3"
    scope = [{ file = "README.md", heading = ["K"] }]
'''
        before = "# A\na\n## H\nh\n# B\nb\n## K\nk\n"
        sc = Scenario(units, {"README.md": before})
        frame = frame_for(sc, units, {"README.md": Entry("100644", "# A\na\n## K\nk\n# B\nb\n## H\nh\n".encode())})
        self.assertEqual(set(frame.write_set), {"ssds.unclassified"})

    def test_a_declaration_change_of_the_outermost_owner_alone(self) -> None:
        """No byte moves: judged as any unit's, so naming it in the scope covers it (re-check ad8daeb W3)."""

        from ssds.derivation.writescope import outside_scope

        from ._fixtures import RESERVED_LEAVES

        sc = Scenario(LAYERED, LAYERED_FILES)
        restated = LAYERED + RESERVED_LEAVES["ssds.manifest"] + RESERVED_LEAVES["ssds.policy"] + \
            RESERVED_LEAVES["ssds.unclassified"] + '[unit.semantic]\ndefines = ["thing"]\n'
        frame = frame_for(sc, restated, LAYERED_FILES)
        self.assertIn("ssds.unclassified", frame.write_set)
        self.assertEqual(outside_scope(frame, ["ssds.unclassified", "ssds.manifest"]), [])
        self.assertIn("ssds.unclassified", outside_scope(frame, ["ssds.manifest"]))

    def test_derived_imports_attribute_only_owned_files(self) -> None:
        """Review 2aadf33 N1: the outermost owner imports nothing a declared unit owns."""

        from ssds.derivation.history import manifest_decl
        from ssds.derivation.s0 import StructureFacts

        from ._fixtures import view

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
        v = view(tree({"pkg/a.py": "from pkg import b\n", "pkg/b.py": "x = 1\n"}, units))
        relations = {(r.subject, r.type, r.object) for r in StructureFacts(v, manifest_decl(v)).derived_relations}
        self.assertEqual(relations, {("pa", "IMPORTS", "pb")})

    def test_the_freeze_sees_regions_a_declaration_moves(self) -> None:
        """Re-check ad8daeb RB1: compared on one tree, a unit overlapping the subject, an ``ignore`` entry and a
        stranger nested in it change it by declaration alone."""

        from ._scenario import challenge

        doc = '''
    [[unit]]
    id = "fz"
    kind = "D3"
    scope = [{ file = "doc.md", heading = ["A"] }]
'''
        files = {"doc.md": "# A\na1\na2\n# B\nb\n<!-- ssds:begin g -->\nmid\n<!-- ssds:end g -->\n"}
        sc = Scenario(doc, files)
        sc.admit(challenge(sc.triple("fz")))
        stranger = doc + '''
    [[unit]]
    id = "g"
    kind = "D3"
    scope = [{ file = "doc.md", heading = ["A"] }]
'''
        self.assertIn("FREEZE_SOURCE", codes(frame_for(sc, stranger, files)), "a coinciding unit ends its region")
        prefixed = Scenario(NESTED, NESTED_FILES)
        prefixed.admit(challenge(prefixed.triple("s1")))
        ignored = '[governed]\nignore = ["pkg/a.py"]\n' + NESTED
        self.assertIn("FREEZE_SOURCE", codes(frame_for(prefixed, ignored, NESTED_FILES)), "an ignore entry")

    def test_a_stranger_nested_in_a_frozen_subject_freezes(self) -> None:
        """Re-check ad8daeb RB1 case 3: a non-member unit declared inside the frozen subject's region takes its
        bytes by innermost ownership; only ``_held``'s owned bytes see it."""

        from ._scenario import challenge

        doc = '''
    [[unit]]
    id = "fz"
    kind = "D3"
    scope = [{ file = "doc.md", heading = ["A"] }]
'''
        files = {"doc.md": "# A\na1\n<!-- ssds:begin g -->\na2\n<!-- ssds:end g -->\n# B\nb\n"}
        sc = Scenario(doc, files)
        sc.admit(challenge(sc.triple("fz")))
        stranger = doc + '''
    [[unit]]
    id = "g"
    kind = "D3"
    scope = [{ file = "doc.md", anchor = "g" }]
'''
        frame = frame_for(sc, stranger, files)
        self.assertNotIn("STRUCT_SIBLING_OVERLAP", codes(frame))
        self.assertIn("FREEZE_SOURCE", codes(frame))

    def test_a_term_ceasing_to_resolve_by_declaration_freezes(self) -> None:
        """Review ad8daeb N-b (R15): F20's "a term coming to resolve or not"."""

        from ._scenario import challenge

        sc = Scenario(NESTED, NESTED_FILES)
        sc.admit(challenge(sc.triple("s1")))
        rescoped = NESTED.replace('scope = [{ file = "pkg/sub/u.py" }]', 'scope = [{ file = "pkg/sub/v.py" }]')
        self.assertIn("FREEZE_SOURCE", codes(frame_for(sc, rescoped, NESTED_FILES)))

    def test_a_scope_may_name_a_unit_the_request_creates(self) -> None:
        """Re-check ad8daeb RB2 and its granularity gap: a new unit named in the scope covers its files on the head
        side, and a write of bytes no other unit owns needs only those bytes in the scope."""

        from ssds.derivation.writescope import outside_scope

        units = LAYERED
        files = {**LAYERED_FILES, "README.md": "r\n", "notes/n.md": "n\n"}
        sc = Scenario(units, files)
        readme = units + '''
    [[unit]]
    id = "readme"
    kind = "D3"
    scope = [{ path = "README.md" }]
'''
        frame = frame_for(sc, readme, files)
        self.assertTrue(frame.exists)
        self.assertEqual(outside_scope(frame, ["readme", "ssds.manifest"]), [])
        self.assertEqual(outside_scope(frame, ["ssds.manifest"]), ["readme", "ssds.unclassified"])
        widened = frame_for(sc, readme, {k: v for k, v in files.items() if k != "notes/n.md"})
        self.assertIn("ssds.unclassified", outside_scope(widened, ["readme", "ssds.manifest"]),
                      "the head-side widening is the new unit's files, never more (re-check c550803 M14)")
        added = frame_for(sc, units, {**files, "notes/new.md": "new\n"})
        self.assertEqual(outside_scope(added, ["notes/"]), [], "README.md, elsewhere, is not in this write")
        self.assertEqual(outside_scope(added, ["src/"]), ["ssds.unclassified"])

    def test_the_reserved_leaf_conditions_one_by_one(self) -> None:
        """Review ad8daeb N-b (R08, R09, R07, R10): each condition of a reserved leaf alone."""

        from ssds.derivation.baseline import reserved_leaf_problems

        from ._fixtures import RESERVED_LEAVES, structure_of

        base = RESERVED_LEAVES["ssds.manifest"] + RESERVED_LEAVES["ssds.policy"]
        leaf = RESERVED_LEAVES["ssds.unclassified"]
        cases = {"a part": leaf.replace('kind = "UNCLASSIFIED"', 'kind = "UNCLASSIFIED"\npart_of = "host"')
                 + '\n[[unit]]\nid = "host"\nkind = "D3"\nrole = "composite"\nscope = [{ prefix = "" }]\n',
                 "not a subject": leaf.replace('kind = "UNCLASSIFIED"', 'kind = "UNCLASSIFIED"\nsubject = false'),
                 "a composite": leaf.replace('kind = "UNCLASSIFIED"', 'kind = "UNCLASSIFIED"\nrole = "composite"')}
        for name, text in cases.items():
            with self.subTest(case=name):
                problems = reserved_leaf_problems(structure_of(tree({}, base + text, reserved=False)))
                self.assertIn("ssds.unclassified", {u for u, _ in problems})

    def test_a_unit_with_a_region_on_neither_side_is_outside(self) -> None:
        """Review ad8daeb N-b (R01)."""

        from ssds.derivation.writescope import _within

        sc = Scenario(LAYERED, LAYERED_FILES)
        frame = frame_for(sc, LAYERED, LAYERED_FILES)
        self.assertFalse(_within(frame.head_view, frame.view, "no-such-unit", ["src/"]))


def submit_dropping(sc, files: dict[str, str]):
    """``test_conformance.submit`` for a candidate tree given whole, so that it can delete files."""

    from .test_conformance import SLOTS

    base = sc.head
    cand = sc.add_tree(tree(files, sc.manifest))
    x = transformation_id(base, cand)
    result = record("TASK_RESULT", target={"task": "task-1", "candidate": cand, "transformation": x, "base": base},
                    outcome="PARTIAL", actor=agent("maker"), actor_class="AGENT", frame={"transformation": x},
                    fields={"slots": SLOTS})
    result["binding"] = dict(fresh(agent("maker"), "task-1"), obligation="obl-item",
                             item={"unit": "plan.work.item", "rev": sc.rev("plan.work.item")})
    result = with_id(result)
    sc.admit(result)
    return x, cand, result


if __name__ == "__main__":
    unittest.main()
