"""Phase F step 6a: the expected head and absorption (catalogue §8.3 step 9, §8.6, §22.3; plan §3.3, reading F39).

When the observed head moved, Admission first appends an absorption of it, its commits imported into the ledger
repository, and revalidates the request at the new head. Without a product repository to read, an observed head
that is no commit, or a head admission with a pending publication effect, Admission halts and appends nothing.
"""

from __future__ import annotations

import unittest
from types import SimpleNamespace

from ssds.admission.engine import Admission, AdmissionHalted
from ssds.derivation import derive
from ssds.ledger.read import ledger_ref, read_chain, with_id

from ._fixtures import commit, git
from .test_admission_requests import RequestFixture, finding


class Absorption(RequestFixture):
    def moved(self) -> str:
        (self.product / "notes.md").write_text("observed later\n")
        return commit(self.product, "a change of unknown provenance")

    def human_request(self, records):
        from ssds.admission.request import request_message

        from ._fixtures import sshsig

        req = self.request(records, base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return req

    def test_a_moved_head_is_absorbed_then_the_request_revalidated(self) -> None:
        obs = self.moved()
        admission = Admission(self.home, "demo", self.trees, product=self.product)
        before = len(self.entries())
        rec = with_id({**finding(), "actor": self.human()})
        decision = admission.admit(self.human_request([rec]), obs)
        entries = self.entries()
        self.assertEqual(len(entries), before + 2, "the absorption, then the request's entry")
        absorbed = entries[before].entry
        self.assertEqual((absorbed["entry_kind"], absorbed["obs"], absorbed["absorption"]), ("ABSORPTION", obs, {"fence": None}))
        self.assertEqual(entries[before + 1].entry["admission"]["base_commit"], obs, "revalidated at the new head")
        self.assertEqual(decision.position, before + 1)
        self.assertEqual(Admission.expected_head(entries), obs)
        support = derive(read_chain(self.home.ledger_repository("demo"), "demo"), self.trees)
        self.assertEqual(support.s.h.head(support.s.n), obs, "derivation folds the same head")
        ledger = self.home.ledger_repository("demo")
        tip = git(ledger, "rev-parse", ledger_ref("demo"))
        git(ledger, "merge-base", "--is-ancestor", obs, tip)  # kept reachable from the ledger ref, not just stored

    def test_no_product_repository_halts_and_appends_nothing(self) -> None:
        obs = self.moved()
        before = len(self.entries())
        with self.assertRaises(AdmissionHalted):
            self.admission.admit(self.human_request([with_id({**finding(), "actor": self.human()})]), obs)
        self.assertEqual(len(self.entries()), before)

    def test_an_observed_head_that_is_no_commit_halts(self) -> None:
        admission = Admission(self.home, "demo", self.trees, product=self.product)
        before = len(self.entries())
        with self.assertRaises(AdmissionHalted):
            admission.admit(self.human_request([with_id({**finding(), "actor": self.human()})]), "f" * 40)
        self.assertEqual(len(self.entries()), before)

    def test_an_observed_head_is_validated_before_any_git_call(self) -> None:
        """Review c06f5be N1: an option-shaped ``obs`` never reaches Git."""

        admission = Admission(self.home, "demo", self.trees, product=self.product)
        before = len(self.entries())
        for obs in ("--upload-pack=touch /tmp/x", "HEAD", "abc"):
            with self.subTest(obs=obs), self.assertRaises(AdmissionHalted):
                admission.absorb(self.entries(), obs)
        self.assertEqual(len(self.entries()), before)

    def test_an_unmoved_head_appends_no_absorption(self) -> None:
        admission = Admission(self.home, "demo", self.trees, product=self.product)
        before = len(self.entries())
        admission.admit(self.human_request([with_id({**finding(), "actor": self.human()})]), self.baseline)
        self.assertEqual(len(self.entries()), before + 1)
        self.assertEqual(self.entries()[before].entry["entry_kind"], "ADMISSION")

    def test_a_pending_publication_effect_is_not_absorbed(self) -> None:
        """Reading F39: §22.3's procedure governs, not a plain absorption."""

        admission = Admission(self.home, "demo", self.trees, product=self.product)
        effect = SimpleNamespace(entry={"entry_kind": "ADMISSION", "position": 5,
                                        "admission": {"decision": "ACCEPT", "base_commit": "a" * 40,
                                                      "admitted_commit": "b" * 40}},
                                 digest="sha256:" + "0" * 64, commit="c" * 40)
        with self.assertRaises(AdmissionHalted):
            admission.absorb([effect], self.moved())
        # a records-only admission (C = B) has no effect and is never fenced (F1): the engine case above absorbs
        # after one

    def test_expected_head_folds_absorptions_and_fences(self) -> None:
        def entry(body):
            return SimpleNamespace(entry=body)

        genesis = entry({"entry_kind": "LIFECYCLE", "lifecycle": {"kind": "GENESIS", "fields": {"baseline_commit": "g"}}})
        absorbed = entry({"entry_kind": "ABSORPTION", "obs": "o", "absorption": {"fence": None}})
        fenced = entry({"entry_kind": "ABSORPTION", "obs": "o2", "absorption": {"fence": {"base": "b", "fence_commit": "f"}}})
        rejected = entry({"entry_kind": "ADMISSION", "admission": {"decision": "REJECT", "admitted_commit": "x"}})
        self.assertEqual(Admission.expected_head([genesis]), "g")
        self.assertEqual(Admission.expected_head([genesis, absorbed]), "o")
        self.assertEqual(Admission.expected_head([genesis, absorbed, fenced]), "f")
        self.assertEqual(Admission.expected_head([genesis, absorbed, rejected]), "o", "a rejection moves nothing")


if __name__ == "__main__":
    unittest.main()
