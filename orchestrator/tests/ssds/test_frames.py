"""Frames: the pinned merge, roles and prospective acceptance at their real owners (catalogue §7; Manual §7).

Expectations are transcribed from ``cases_s5_7.py`` (named per test).
"""

from __future__ import annotations

import unittest

from ssds.content import Entry, Tree, merge3, merge_text
from ssds.derivation import F, T
from ssds.derivation.frames import Frame, transformation_of

from ._fixtures import manifest
from ._scenario import HUMAN, Scenario, agent, content, integrate, judgment, submit

M = ".ssds/manifest.toml"


def t(files: dict) -> Tree:
    return Tree({p: (v if isinstance(v, Entry) else v.encode() if isinstance(v, str) else v) for p, v in files.items()})


B = {"a.py": "x\ny\n", "bin": Entry("100644", b"\x001"), "m.toml": "k=1\n"}


class Merge(unittest.TestCase):
    """cases_s5_7.py merge cases."""

    def test_one_side_change(self) -> None:
        merged, conflict = merge3(t(B), t(B), t({**B, "a.py": "x\nY\n"}), M)
        self.assertEqual((merged["a.py"].data, conflict), (b"x\nY\n", None))

    def test_disjoint_lines_merge(self) -> None:
        merged, conflict = merge3(t(B), t({**B, "a.py": "X\ny\n"}), t({**B, "a.py": "x\nY\n"}), M)
        self.assertEqual((merged["a.py"].data, conflict), (b"X\nY\n", None))

    def test_overlapping_hunk_conflict(self) -> None:
        merged, conflict = merge3(t(B), t({**B, "a.py": "x\nY1\n"}), t({**B, "a.py": "x\nY2\n"}), M)
        self.assertIsNone(merged)
        self.assertIsNotNone(conflict)

    def test_binary_both_sides_conflict(self) -> None:
        merged, _ = merge3(t(B), t({**B, "bin": Entry("100644", b"\x002")}), t({**B, "bin": Entry("100644", b"\x003")}), M)
        self.assertIsNone(merged)

    def test_declaration_key_conflict(self) -> None:
        def m(*terms: str) -> bytes:
            lines = "".join(f'  {{ prefix = "{p}" }},\n' for p in terms)
            return manifest(f'[[unit]]\nid = "u"\nkind = "D4"\nscope = [\n{lines}]\n')

        base, head, candidate = t({M: m("a/")}), t({M: m("a/", "h/")}), t({M: m("c/", "a/")})
        self.assertIsNotNone(merge_text(base[M].data, head[M].data, candidate[M].data), "the manifest's lines merge cleanly")
        merged, conflict = merge3(base, head, candidate, M)
        self.assertIsNone(merged)
        self.assertIn("declaration key", conflict)

    def test_other_both_sides_changes_conflict(self) -> None:
        for head, candidate in (({**B, "a.py": Entry("100755", b"x\ny\n")}, {**B, "a.py": "x\nZ\n"}),
                                ({k: v for k, v in B.items() if k != "a.py"}, {**B, "a.py": "x\nZ\n"}),
                                ({**B, "new": "1\n"}, {**B, "new": "2\n"})):
            with self.subTest(head=sorted(head), candidate=sorted(candidate)):
                self.assertIsNone(merge3(t(B), t(head), t(candidate), M)[0])


UNITS = '''
    [[unit]]
    id = "u"
    kind = "D4"
    scope = [{ path = "u.md" }]
    [[unit]]
    id = "w"
    kind = "D4"
    scope = [{ path = "w.md" }]
'''
WITH_NEW = UNITS + '''
    [[unit]]
    id = "newsub"
    kind = "D3"
    scope = [{ path = "new.md" }]
'''


class Roles(unittest.TestCase):
    def test_roles(self) -> None:
        # roles: before-image, output and context are fixed by B, C and the entry
        sc = Scenario(UNITS, {"u.md": "1\n", "w.md": "5\n"})
        u_before = sc.rev("u")
        x, candidate, _ = submit(sc, {"u.md": "2\n"}, agent("maker"), "task-1")
        state = sc.derive().s
        frame = Frame(state.h, state.n, transformation_of(state, x), state.enactment(x))
        u_after = frame.view.rev("u")
        self.assertEqual((frame.role("u", u_before), frame.role("u", u_after), frame.role("w", sc.rev("w")),
                          frame.role("u", "sha256:" + "9" * 64)),
                         ("before-image", "output", "context", "never"))


class ProspectiveAcceptance(unittest.TestCase):
    """cases_s5_7.py: a prospective acceptance binds once, to its own enactment and structure (R12, SD-26)."""

    def setUp(self) -> None:
        self.sc = Scenario(UNITS, {"u.md": "1\n", "w.md": "5\n"})

    def prospective(self, x: str, candidate: str) -> dict:
        state = self.sc.derive().s
        frame = Frame(state.h, state.n, transformation_of(state, x), state.enactment(x))
        rev = frame.view.rev("newsub")
        target = {"subject": "newsub", "scope_id": frame.view.scope_id("newsub"), "rev": rev}
        return judgment("ACCEPTANCE", target, "PASS", actor=HUMAN, basis=[content("newsub", rev)],
                        frame={"transformation": x})

    def test_same_enactment_counts(self) -> None:
        x, candidate, _ = submit(self.sc, {"new.md": "n\n"}, agent("maker"), "task-1", manifest=WITH_NEW)
        j = self.prospective(x, candidate)
        self.sc.admit(j)
        integrate(self.sc, x, candidate)
        self.assertEqual(self.sc.derive().valid("newsub"), T)

    def test_later_iteration_needs_its_own_acceptance(self) -> None:
        x1, c1, _ = submit(self.sc, {"new.md": "n\n"}, agent("maker"), "task-1", manifest=WITH_NEW)
        self.sc.admit(self.prospective(x1, c1))
        x2, c2, _ = submit(self.sc, {"new.md": "n\n", "w.md": "6\n"}, agent("maker"), "task-2", manifest=WITH_NEW)
        integrate(self.sc, x2, c2)
        self.assertEqual(self.sc.derive().valid("newsub"), F,
                         "iteration 1's acceptance does not act after iteration 2 integrates")

    def test_structure_changed_does_not_count(self) -> None:
        x1, c1, _ = submit(self.sc, {"new.md": "n\n"}, agent("maker"), "task-1", manifest=WITH_NEW)
        self.sc.admit(self.prospective(x1, c1))
        other = WITH_NEW + '''
            [[unit]]
            id = "extra"
            kind = "D4"
            scope = [{ path = "extra.md" }]
        '''
        x2, c2, _ = submit(self.sc, {"new.md": "n\n", "extra.md": "e\n"}, agent("maker"), "task-1", manifest=other)
        integrate(self.sc, x2, c2)
        self.assertEqual(self.sc.derive().valid("newsub"), F, "a rebase that changes the proposed structure")

    def test_counts_for_at_most_one_tenure(self) -> None:
        x, candidate, _ = submit(self.sc, {"new.md": "n\n"}, agent("maker"), "task-1", manifest=WITH_NEW)
        self.sc.admit(self.prospective(x, candidate))
        integrate(self.sc, x, candidate)
        self.assertEqual(self.sc.derive().valid("newsub"), T)
        demoted = WITH_NEW.replace('id = "newsub"\n    kind = "D3"', 'id = "newsub"\n    kind = "D4"')
        x2, c2, _ = submit(self.sc, {}, agent("maker"), "task-3", manifest=demoted)
        integrate(self.sc, x2, c2)
        x3, c3, _ = submit(self.sc, {}, agent("maker"), "task-4", manifest=WITH_NEW)
        integrate(self.sc, x3, c3)
        self.assertEqual(self.sc.derive().valid("newsub"), F, "a later tenure of the same triple needs a new acceptance")


class FrameState(unittest.TestCase):
    def test_a_frame_record_acts_in_its_own_frame_and_after_integration_only(self) -> None:
        sc = Scenario(UNITS, {"u.md": "1\n", "w.md": "5\n"})
        x, candidate, _ = submit(sc, {"u.md": "2\n"}, agent("maker"), "task-1")
        state = sc.derive().s
        frame = Frame(state.h, state.n, transformation_of(state, x), state.enactment(x))
        review = judgment("REVIEW", {"transformation": x}, "PASS", actor=HUMAN,
                          basis=[content("u", frame.view.rev("u"))], frame={"transformation": x})
        sc.admit(review)
        admitted = sc.derive()
        self.assertFalse(admitted.s.acts(review["id"]))
        from ssds.derivation.frames import frame_state
        from ssds.derivation.support import Support

        in_frame = Support(frame_state(admitted.s.h, admitted.s.n, x, admitted.s))
        self.assertTrue(in_frame.s.acts(review["id"]))
        self.assertEqual(in_frame.current(review["id"]), T)
        integrate(sc, x, candidate)
        self.assertEqual(sc.derive().current(review["id"]), T, "after integration the output entry holds as ordinary currency")


if __name__ == "__main__":
    unittest.main()
