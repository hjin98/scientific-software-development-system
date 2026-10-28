"""Phase F step 10b: observe-only Admission (catalogue §8.2-§8.6, §22.3; plan §3.7, readings F1, F120; SD-64 Q-F2).

``ssds admission serve`` runs one pass: the observed ref checked (a branch, resolving to a commit, the name recorded
on first use and changed only with ``--rebind-observed-ref``), the held head taken, the observed head absorbed when it
moved and descends from the last observation, nothing else appended. The shadow-boundary policy refuses, before
validation and on every route, a candidate, a record of a kind Phase F does not accept, and an adoption beyond
SD-69's repair, logging each refusal in operator state and appending nothing.
"""

from __future__ import annotations

import json
import unittest
from unittest import mock

from ssds.admission.engine import BoundaryRefused, shadow_boundary
from ssds.admission.request import request_message

from . import test_phase_f_step9d_iii as harness
from ._fixtures import commit, git, init_repo, record, sshsig


class Served(harness.AdmittedRuns):
    def setUp(self) -> None:
        super().setUp()
        patch = mock.patch("ssds.cli.ssds_home", return_value=self.home.root)
        patch.start()
        self.addCleanup(patch.stop)

    def composition(self):
        from ssds.cli import Composition

        return Composition("demo", self.product)

    def move(self, **files: str) -> str:
        self.write(files)
        return commit(self.product, "a later commit on the observed branch")

    def logged(self, name: str) -> list[dict]:
        path = self.home.root / "state" / "demo" / name
        return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

    def human_request(self, *records, candidates=(), adopted=()):
        req = self.request(records)
        req["candidates"], req["adopted_deltas"] = list(candidates), list(adopted)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return req

    def availability(self):
        return record("AVAILABILITY", target={"digest": "sha256:" + "6" * 64}, outcome="AVAILABLE", actor=self.human(),
                      actor_class="HUMAN")


class Pass(Served):
    def test_a_moved_head_is_absorbed_once(self) -> None:
        head = self.move(**{"other.txt": "2\n"})
        before = len(self.entries())
        report = self.composition().serve("main")
        self.assertEqual((report["absorbed"], report["obs"]), (True, head))
        self.assertEqual(len(self.entries()), before + 1)
        self.assertEqual(self.entries()[-1].entry["entry_kind"], "ABSORPTION")
        again = self.composition().serve("main")
        self.assertFalse(again["absorbed"], "an unmoved head appends nothing")
        self.assertEqual(len(self.entries()), before + 1)

    def test_the_ref_is_checked(self) -> None:
        from ssds.interface.operations import Refused

        before = len(self.entries())
        for name in ("-main", "nonexistent", "main..x", self.baseline, "HEAD/"):
            with self.subTest(name=name), self.assertRaises(Refused):
                self.composition().serve(name)
        git(self.product, "checkout", "--quiet", "--orphan", "elsewhere")
        self.write({"a.py": "v = 9\n"})
        commit(self.product, "an unrelated history")
        git(self.product, "checkout", "--quiet", "main")
        self.composition().serve("main")  # the first use records main
        with self.assertRaises(Refused) as refused:
            self.composition().serve("elsewhere", rebind=True)
        self.assertIn("does not descend", str(refused.exception))
        self.assertEqual(len(self.entries()), before, "nothing appended")
        self.assertEqual([e["ref"] for e in self.logged("observed-ref.jsonl")], ["main"], "a refused pass records no rebind")

    def test_the_observed_ref_is_recorded_and_a_switch_needs_rebind(self) -> None:
        from ssds.interface.operations import Refused

        self.composition().serve("main")
        git(self.product, "branch", "other")
        with self.assertRaises(Refused):
            self.composition().serve("other")
        self.composition().serve("other", rebind=True)
        self.assertEqual([(e["ref"], e["previous"]) for e in self.logged("observed-ref.jsonl")],
                         [("main", None), ("other", "main")])
        self.composition().serve("other")  # now the recorded one

    def test_a_restart_after_a_records_only_admission_appends_no_fence(self) -> None:
        admission = self.composition().admission()
        decision = admission.admit(self.human_request(self.availability()), self.head())
        self.assertEqual(decision.decision, "ACCEPT")
        before = len(self.entries())
        for _ in range(2):  # two restarts
            self.assertFalse(self.composition().serve("main")["absorbed"])
        self.assertEqual(len(self.entries()), before, "a records-only admission is never fenced (F1)")

    def test_an_unqualified_ledger_is_refused(self) -> None:
        """The held head (``held_head``): nothing is absorbed into a ledger that is not qualified (§23.4)."""

        import shutil

        from ssds.admission.engine import AdmissionHalted

        self.move(**{"other.txt": "4\n"})
        shutil.rmtree(self.home.witness_root / "demo")
        before = len(self.entries())
        with self.assertRaises(AdmissionHalted):
            self.composition().serve("main")
        self.assertEqual(len(self.entries()), before)

    def test_a_refused_absorption_records_no_rebind(self) -> None:
        """Review of 6de6cf0d, B1: the ref is recorded once the pass took effect, never before ``absorb``."""

        from ssds.admission.engine import Admission, AdmissionHalted

        self.composition().serve("main")
        git(self.product, "checkout", "--quiet", "-b", "other")
        self.move(**{"other.txt": "5\n"})
        before = len(self.entries())
        with mock.patch.object(Admission, "absorb", side_effect=AdmissionHalted("publication pending (F39)")), \
                self.assertRaises(AdmissionHalted):
            self.composition().serve("other", rebind=True)
        self.assertEqual(len(self.entries()), before)
        self.assertEqual([e["ref"] for e in self.logged("observed-ref.jsonl")], ["main"], "refused: no rebind")
        original = Admission.absorb

        def appended_then_halted(admission, entries, obs):
            original(admission, entries, obs)
            raise AdmissionHalted("appended but not yet held")

        with mock.patch.object(Admission, "absorb", appended_then_halted), self.assertRaises(AdmissionHalted):
            self.composition().serve("other", rebind=True)
        self.assertEqual(len(self.entries()), before + 1)
        self.assertEqual([e["ref"] for e in self.logged("observed-ref.jsonl")], ["main", "other"],
                         "the absorption took effect: the ledger observes other")

    def test_a_repository_without_the_last_observation_is_refused(self) -> None:
        """Review of 6de6cf0d, R1: descent unknown is no descent; another repository's ``main`` is refused."""

        from ssds.cli import Composition
        from ssds.interface.operations import Refused

        elsewhere = init_repo(self.product.parent / "elsewhere")
        (elsewhere / "a.py").write_text("v = 7\n")
        commit(elsewhere, "another project")
        before = len(self.entries())
        with self.assertRaises(Refused) as refused:
            Composition("demo", elsewhere).serve("main")
        self.assertIn("does not descend", str(refused.exception))
        self.assertEqual(len(self.entries()), before)
        self.assertEqual(self.logged("observed-ref.jsonl"), [])

    def test_the_command(self) -> None:
        from typer.testing import CliRunner

        from ssds.cli import app

        self.move(**{"other.txt": "3\n"})
        args = ["admission", "serve", "--ledger", "demo", "--repository", str(self.product), "--observed-ref"]
        result = CliRunner().invoke(app, [*args, "main"])
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertTrue(json.loads(result.output)["absorbed"])
        refused = CliRunner().invoke(app, [*args, "nonexistent"])
        self.assertEqual(refused.exit_code, 1)
        self.assertIn("refused", json.loads(refused.output))
        help_text = CliRunner().invoke(app, ["admission", "serve", "--help"]).output
        self.assertIn("Never rewrite the observed branch", help_text)


class Boundary(Served):
    def test_a_candidate_on_every_route(self) -> None:
        """The library API, the queue, and the Dispatcher's submit callable all end at Admission's entry."""

        from ssds.dispatcher.realize import Executor
        from ssds.ledger.qualification import Home

        admission = self.composition().admission()
        before = len(self.entries())
        candidate = self.human_request(self.availability(), candidates=["0" * 40])
        with self.assertRaises(BoundaryRefused):
            admission.admit(candidate, self.head())
        with self.assertRaises(BoundaryRefused):
            admission.submit(candidate)
        self.assertEqual(admission.queue, [], "refused before any queue")
        executor = Executor(Home(self.home.root), "demo", self.chain, self.trees, {},
                            lambda req: admission.admit(req, self.head()), governs={})
        with self.assertRaises(BoundaryRefused):
            executor.submit(candidate)
        self.assertEqual(len(self.entries()), before, "nothing appended")
        self.assertEqual(len(self.logged("boundary.jsonl")), 3, "each refusal logged")
        self.assertIn("candidate", self.logged("boundary.jsonl")[0]["reason"])

    def test_a_kind_phase_f_does_not_accept(self) -> None:
        later = record("MODE_TRANSITION", target={"units": ["code"]}, actor=self.human(), actor_class="HUMAN")
        self.assertIn("later phase", shadow_boundary(self.request([later])))
        self.assertIsNone(shadow_boundary(self.request([self.availability()])))
        self.assertIsNone(shadow_boundary("not an object"), "validation records its rejection")

    def test_only_sd69s_adoption(self) -> None:
        absorption = "sha256:" + "4" * 64

        def adopting(unit: str, absorbed: bool = True):
            delta = {"absorption": absorption, "key": [unit, "kind"], "value": "MANIFEST"}
            disposition = record("INTAKE_DISPOSITION", target={"absorption": absorption, "key": [unit, "kind"]},
                                 outcome="ABSORB" if absorbed else "REJECT", actor=self.human(), actor_class="HUMAN")
            return {**self.request([disposition]), "adopted_deltas": [delta]}

        self.assertIsNone(shadow_boundary(adopting("ssds.manifest")))
        self.assertIsNone(shadow_boundary(adopting("ssds.policy")))
        self.assertIn("beyond SD-69", shadow_boundary(adopting("code")), "another unit's key")
        self.assertIn("beyond SD-69", shadow_boundary(adopting("ssds.manifest", absorbed=False)), "not by ABSORB")
        for key in (["ssds.manifest", "renamed_from"], ["ssds.policy", "part_of"], ["ssds.policy"],
                    ["ssds.policy", "kind", "x"], ["ssds.policy", "semantic"]):
            with self.subTest(key=key):  # review of 6de6cf0d, N1: the leaf's own fields only
                request = adopting("ssds.policy")
                request["adopted_deltas"][0]["key"] = key
                request["records"][0]["target"]["key"] = key
                self.assertIn("beyond SD-69", shadow_boundary(request))
        for field in ("kind", "role", "subject", "scope"):
            request = adopting("ssds.manifest")
            request["adopted_deltas"][0]["key"] = request["records"][0]["target"]["key"] = ["ssds.manifest", field]
            self.assertIsNone(shadow_boundary(request), field)
        bare = {**self.request([]), "adopted_deltas": [{"absorption": absorption, "key": ["ssds.policy", "kind"]}]}
        self.assertIn("beyond SD-69", shadow_boundary(bare), "no disposition in the request")

    def test_an_admitted_records_only_request_passes(self) -> None:
        decision = self.composition().admission().admit(self.human_request(self.availability()), self.head())
        self.assertEqual(decision.decision, "ACCEPT")
        self.assertEqual(self.logged("boundary.jsonl"), [])


if __name__ == "__main__":
    unittest.main()
