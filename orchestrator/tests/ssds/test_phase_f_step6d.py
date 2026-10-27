"""Phase F step 6d: publication classification and the entry-shape rule (catalogue §22.1-§22.2; plan §3.3, reading
F43). Group 4's S5 §22 ``publication_classification`` and 730490d N2's records-only form (``OVERTAKEN`` then
``LATE_PUBLICATION``), on derivation histories with a commit-graph stub.
"""

from __future__ import annotations

import unittest

from ssds.derivation import consequences
from ssds.derivation.history import History
from ssds.derivation.publication import OVERTAKEN, PENDING, PUBLISHED, UNKNOWN, Publication

from ._fixtures import absorption_body, admission_body, chain_of, commit_id
from ._scenario import Scenario
from .test_phase_f_step4d import FILES, THREE


class Graph:
    """``is_ancestor`` over named edges child -> parents."""

    def __init__(self, edges: dict[str, list[str]]) -> None:
        self.edges = edges

    def __call__(self, a: str, b: str) -> bool:
        seen, stack = set(), [b]
        while stack:
            c = stack.pop()
            if c == a:
                return True
            if c not in seen:
                seen.add(c)
                stack.extend(self.edges.get(c, []))
        return False


def history(sc: Scenario, ancestry=None) -> History:
    return History(chain_of("demo", sc.entries, sc.objects), sc.trees.__getitem__, None, ancestry)


class Classification(unittest.TestCase):
    def setUp(self) -> None:
        self.sc = Scenario(THREE, dict(FILES))
        self.base = self.sc.head
        self.sc.entries.append(admission_body(self.sc.position, self.base, self.base))  # records-only: C = B
        self.n = self.sc.position - 1
        self.later = commit_id("later")
        self.elsewhere = commit_id("rewritten")
        self.sc.trees[self.later] = self.sc.trees[self.base]
        self.sc.trees[self.elsewhere] = self.sc.trees[self.base]
        self.graph = Graph({self.later: [self.base], self.elsewhere: []})

    def classify(self, ancestry=None) -> str:
        return Publication(history(self.sc, ancestry)).classes[self.n]

    def test_pending_until_an_entry_carries_obs(self) -> None:
        self.assertEqual(self.classify(self.graph), PENDING)

    def test_published_when_the_next_obs_is_c(self) -> None:
        self.sc.entries.append(admission_body(self.sc.position, self.base, self.base))
        self.assertEqual(self.classify(), PUBLISHED, "obs = C_n needs no graph")

    def test_published_when_a_descendant_is_absorbed(self) -> None:
        self.sc.entries.append(absorption_body(self.sc.position, self.later))
        self.assertEqual(self.classify(self.graph), PUBLISHED)
        self.assertEqual(self.classify(None), UNKNOWN, "descent cannot be shown without the graph")

    def test_overtaken_when_a_rewrite_is_absorbed(self) -> None:
        self.sc.trees[self.elsewhere] = self.sc.trees[self.base].__class__({})
        self.sc.entries.append(absorption_body(self.sc.position, self.elsewhere))
        self.assertEqual(self.classify(self.graph), OVERTAKEN)
        self.assertEqual(self.classify(None), UNKNOWN, "without the graph, nothing is shown")

    def test_late_publication_is_a_critical_integrity_finding(self) -> None:
        """730490d N2, records-only form."""

        self.sc.trees[self.elsewhere] = self.sc.trees[self.base].__class__({})
        self.sc.entries.append(absorption_body(self.sc.position, self.elsewhere))
        self.sc.entries.append(absorption_body(self.sc.position, self.later))  # a later obs newly reaches C_n
        published = Publication(history(self.sc, self.graph))
        self.assertEqual(published.late, (self.n,))
        findings = consequences(chain_of("demo", self.sc.entries, self.sc.objects), self.sc.trees.__getitem__,
                                ancestry=self.graph).findings
        self.assertTrue(any(f.code == "LATE_PUBLICATION" and f.integrity for f in findings))


    def test_an_entry_carrying_no_obs_reconciles_nothing(self) -> None:
        from ._fixtures import lifecycle_body, record

        loss = record("LEDGER_LOSS", target=None, actor="human:SHA256:owner", fields={
            "retained": {"position": 1}, "abandoned": [], "report": "sha256:" + "b" * 64, "controls": {}})
        self.sc.entries.append(lifecycle_body(self.sc.position, loss))  # a recovery entry: obs = null
        self.assertEqual(self.classify(self.graph), PENDING)


class Integration(unittest.TestCase):
    """An admission with an effect: equivalence needs both descent from ``B_n`` and ``C_n``'s tree."""

    def setUp(self) -> None:
        from ._scenario import agent, submit

        self.sc = Scenario(THREE, dict(FILES))
        self.base = self.sc.head
        x, self.candidate, _ = submit(self.sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        self.sc.entries.append(admission_body(self.sc.position, self.base, self.candidate, integrates=x))
        self.n = self.sc.position - 1

    def absorb(self, name: str, tree_of: str, parents: list[str]) -> Graph:
        obs = commit_id(name)
        self.sc.trees[obs] = self.sc.trees[tree_of]
        self.sc.entries.append(absorption_body(self.sc.position, obs))
        return Graph({obs: parents, self.candidate: [self.base]})

    def test_an_equivalent_publication_is_published(self) -> None:
        graph = self.absorb("merge", self.candidate, [self.base])  # C_n itself unreachable, its tree published
        self.assertEqual(Publication(history(self.sc, graph)).classes[self.n], PUBLISHED)

    def test_the_same_tree_off_the_base_is_overtaken(self) -> None:
        graph = self.absorb("elsewhere", self.candidate, [])
        self.assertEqual(Publication(history(self.sc, graph)).classes[self.n], OVERTAKEN, "no descent from B_n")

    def test_a_graph_that_cannot_say_is_unknown(self) -> None:
        """Review 0ab46e4 N4: an unreadable graph is never "not an ancestor"."""

        self.absorb("unreadable", self.base, [])
        self.assertEqual(Publication(history(self.sc, lambda a, b: None)).classes[self.n], UNKNOWN)

    def test_a_descendant_with_another_tree_is_overtaken(self) -> None:
        graph = self.absorb("other", self.base, [self.base])
        self.assertEqual(Publication(history(self.sc, graph)).classes[self.n], OVERTAKEN, "not C_n's tree")


class EntryShape(unittest.TestCase):
    def setUp(self) -> None:
        self.sc = Scenario(THREE, dict(FILES))
        self.base = self.sc.head

    def test_an_admission_whose_obs_is_not_the_expected_head_is_corrupt(self) -> None:
        stray = admission_body(self.sc.position, self.base, self.base)
        stray["obs"] = commit_id("elsewhere")
        self.sc.entries.append(stray)
        self.assertEqual(Publication(history(self.sc)).violations, (self.sc.position - 1,))
        findings = consequences(chain_of("demo", self.sc.entries, self.sc.objects), self.sc.trees.__getitem__).findings
        self.assertTrue(any(f.code == "ENTRY_SHAPE" and f.integrity for f in findings))

    def test_an_absorption_and_an_equivalent_publication_keep_the_shape(self) -> None:
        from ._scenario import agent, submit

        moved = commit_id("moved")
        self.sc.trees[moved] = self.sc.trees[self.base]
        self.sc.entries.append(absorption_body(self.sc.position, moved))  # obs differs from E: an absorption may
        self.sc.entries.append(absorption_body(self.sc.position, self.base))
        x, candidate, _ = submit(self.sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        self.sc.entries.append(admission_body(self.sc.position, self.base, candidate, integrates=x))
        merged = commit_id("merge of the same tree")
        self.sc.trees[merged] = self.sc.trees[candidate]
        follow = admission_body(self.sc.position, merged, merged)
        self.sc.entries.append(follow)  # E becomes obs: an equivalent publication of the integration
        graph = Graph({merged: [self.base], candidate: [self.base]})
        self.assertEqual(Publication(history(self.sc, graph)).violations, ())
        self.assertEqual(Publication(history(self.sc)).violations, (self.sc.position - 1,),
                         "without the graph no equivalence is shown: strict")

    def test_only_the_admission_that_set_e_excuses_an_equivalent(self) -> None:
        """Review 0ab46e4 N2: an absorption that returns E to an old C sets E itself."""

        from ._scenario import agent, submit

        x, candidate, _ = submit(self.sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        self.sc.entries.append(admission_body(self.sc.position, self.base, candidate, integrates=x))
        away = commit_id("away")
        self.sc.trees[away] = self.sc.trees[self.base]
        self.sc.entries.append(absorption_body(self.sc.position, away))
        self.sc.entries.append(absorption_body(self.sc.position, candidate))  # E returns to the old C
        merged = commit_id("merge of the same tree")
        self.sc.trees[merged] = self.sc.trees[candidate]
        self.sc.entries.append(admission_body(self.sc.position, merged, merged))
        graph = Graph({merged: [self.base], candidate: [self.base]})
        self.assertEqual(Publication(history(self.sc, graph)).violations, (self.sc.position - 1,))


class Ancestry(unittest.TestCase):
    def test_the_commit_graph_reader(self) -> None:
        import tempfile
        from pathlib import Path

        from ssds.content import ancestry

        from ._fixtures import commit, init_repo

        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp) / "r")
            (repo / "a.txt").write_text("1\n")
            first = commit(repo, "first")
            (repo / "a.txt").write_text("2\n")
            second = commit(repo, "second")
            is_ancestor = ancestry(repo)
            self.assertTrue(is_ancestor(first, second))
            self.assertTrue(is_ancestor(first, first))
            self.assertFalse(is_ancestor(second, first))
            self.assertIsNone(is_ancestor("f" * 40, second), "a missing object: the graph cannot say (review N4)")
            self.assertFalse(is_ancestor("--all", second), "validated before any Git call")


if __name__ == "__main__":
    unittest.main()
