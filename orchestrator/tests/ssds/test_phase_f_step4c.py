"""Phase F step 4c-i: the frame at the head, its one write set, and ``id(X)`` (plan §3.1 4c-i, reading F17).

Expected values come from catalogue §1.2 (the write set compares ``T_n`` under ``Σ_n`` with ``M_n(X)``), §7.1
(``id(X)``), §7.3 (currency after integration) and §10.4/SD-40 (an integrated enactment's conformance is settled),
never from the code under test.
"""

from __future__ import annotations

import unittest

from ssds.derivation.conformance import CLEAN
from ssds.derivation.frames import transformation_of
from ssds.ledger.read import transformation_id, with_id

from ._fixtures import record
from ._scenario import OWNER, agent, integrate, judgment
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
