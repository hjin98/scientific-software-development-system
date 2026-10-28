"""Phase F step 10a: publication wired (catalogue §22.1-§22.2; plan §3.7, reading F119).

The composition root passes the ledger repository's commit graph to every derivation that classifies publication:
Admission's (its own and its trial states), the Interface's ``present`` and ``dispatcher serve``'s ``observe``, all
built through one factory. With it a records-only admission followed by an absorption of a descendant is
``PUBLISHED``; without it ``UNKNOWN``. ``LATE_PUBLICATION`` over a directly built ledger is step 6d's
``test_late_publication_is_a_critical_integrity_finding``: ``admission serve`` never absorbs a rewind (F120).
"""

from __future__ import annotations

import unittest
from unittest import mock

from ssds.content import ancestry
from ssds.derivation import derive
from ssds.derivation.history import History
from ssds.derivation.publication import PUBLISHED, UNKNOWN, Publication

from . import test_phase_f_step9d_iii as harness
from ._fixtures import record


class Graphs:
    """Every ``History`` built while it is active, with the graph it was given."""

    def __init__(self) -> None:
        self.seen: list = []

    def __enter__(self) -> "Graphs":
        original = History.__init__
        seen = self.seen

        def spy(history, chain, trees, checkpoint=None, ancestry=None):
            seen.append(ancestry)
            original(history, chain, trees, checkpoint, ancestry)

        self._patch = mock.patch.object(History, "__init__", spy)
        self._patch.start()
        return self

    def __exit__(self, *_) -> None:
        self._patch.stop()


class Published(harness.AdmittedRuns):
    def graph(self):
        return ancestry(self.home.ledger_repository("demo"))

    def records_only(self) -> int:
        rec = record("AVAILABILITY", target={"digest": "sha256:" + "6" * 64}, outcome="AVAILABLE", actor=self.human(),
                     actor_class="HUMAN")
        self.admit_human(rec)
        return len(self.entries()) - 1

    def test_a_records_only_admission_then_a_descendant(self) -> None:
        n = self.records_only()
        self.tree("T1", **{"other.txt": "2\n"})  # a later commit on the observed branch, absorbed
        with_graph = Publication(derive(self.chain(), self.trees, ancestry=self.graph()).s.h).classes
        without = Publication(derive(self.chain(), self.trees).s.h).classes
        self.assertEqual(with_graph[n], PUBLISHED, "C_n = B_n, and the absorbed obs descends from it")
        self.assertEqual(without[n], UNKNOWN, "no graph: a publication that is not obs itself is unknown")

    def test_the_ledger_repository_holds_every_observed_commit(self) -> None:
        """F119: the graph read is the ledger repository's, never the product repository's."""

        from ssds.cli import HomeAccess
        from ssds.ledger.qualification import Home

        n = self.records_only()
        head = self.tree("T1", **{"other.txt": "2\n"})
        base = self.chain().entries[n].entry["admission"]["base_commit"]
        self.assertTrue(self.graph()(base, head), "imported by the absorption (step 6a)")
        composed = HomeAccess(Home(self.home.root), "demo").ancestry()
        self.assertTrue(composed(base, head), "the composition's graph is the ledger repository's (review N, M8)")

    def test_admissions_derivations_carry_the_graph(self) -> None:
        self.admission.ancestry = self.graph()
        with Graphs() as graphs:
            self.records_only()
        self.assertTrue(graphs.seen, "Admission derived")
        self.assertTrue(all(g is self.admission.ancestry for g in graphs.seen), graphs.seen)


class Commands(harness.AdmittedRuns):
    def test_every_command_derives_with_the_graph(self) -> None:
        """Plan check of 603295c8, note 1: one factory, so no command omits it."""

        from typer.testing import CliRunner

        from ssds.cli import app

        for command in (["status"], ["inspect"], ["ask", "blocked", "code"], ["dispatcher", "serve"]):
            with self.subTest(command=command), Graphs() as graphs, \
                    mock.patch("ssds.cli.ssds_home", return_value=self.home.root):
                result = CliRunner().invoke(app, [*command, "--ledger", "demo", "--repository", str(self.product)])
                self.assertIsNone(result.exception, result.output)
                self.assertTrue(graphs.seen, "it derived")
                self.assertTrue(all(g is not None for g in graphs.seen), "every derivation carries the graph")

    def test_an_unqualified_ledger_derives_with_the_graph_too(self) -> None:
        """Review of abcb194e, N1: ``present``'s historical branch."""

        import shutil

        from typer.testing import CliRunner

        from ssds.cli import app

        shutil.rmtree(self.home.witness_root / "demo")  # the witness holds nothing: not a qualified head
        with Graphs() as graphs, mock.patch("ssds.cli.ssds_home", return_value=self.home.root):
            result = CliRunner().invoke(app, ["status", "--ledger", "demo", "--repository", str(self.product)])
        self.assertEqual(result.exit_code, 1, result.output)  # no current assertion: exit 1, an answer all the same
        self.assertIn("historical views only", result.output)
        self.assertTrue(graphs.seen and all(g is not None for g in graphs.seen))


if __name__ == "__main__":
    unittest.main()
