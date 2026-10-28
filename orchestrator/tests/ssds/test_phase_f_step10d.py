"""Phase F step 10d: the runbook rehearsed on a fixture ledger shaped like ``ssdp-shadow-2`` (plan reading F122).

The genesis declares no ``ssds.manifest`` or ``ssds.policy`` (SD-69). The rehearsal follows the runbook: the
declarations committed on the observed branch; ``admission serve`` absorbing them, their keys quarantined;
``scripts/reserved_leaves.py`` writing the ``ABSORB`` inputs; ``ssds submit --prepare``, the human's signature and
``--admit``; ``Σ`` then declaring the three reserved leaves; the restart check; ``dispatcher serve``; a records-only
``report`` and ``submit``; a ``decide`` and a candidate refused at entry. ``scripts/shadow_boundary.py`` compares
the product repository around every SSDS command after the declarations' commit.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

from ssds.admission.genesis import admit_genesis, prepare_genesis
from ssds.admission.request import BoundaryRefused, request_message
from ssds.derivation import derive
from ssds.ledger.read import read_chain

from ._fixtures import commit, record, sshsig
from .test_admission_genesis import GenesisFixture

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
UNREPAIRED = '''schema = 1
[[unit]]
id = "guide"
kind = "D3"
scope = [{ path = "guide.md" }]
[[unit]]
id = "code"
kind = "D4"
scope = [{ prefix = "src/" }]
[[unit]]
id = "ssds.unclassified"
kind = "UNCLASSIFIED"
scope = [{ prefix = "" }]
'''
DECLARATIONS = '''[[unit]]
id = "ssds.manifest"
kind = "MANIFEST"
scope = [{ file = ".ssds/manifest.toml" }]
[[unit]]
id = "ssds.policy"
kind = "POLICY"
scope = [{ file = ".ssds/policy.toml" }]
'''


def script(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Rehearsal(GenesisFixture):
    def setUp(self) -> None:
        super().setUp()
        (self.product / ".ssds" / "manifest.toml").write_text(UNREPAIRED)
        (self.product / ".ssds" / "policy.toml").unlink()  # as on the observed branch: the policy path holds no file
        self.baseline = commit(self.product, "the unrepaired baseline")
        from ssds.derivation import baseline

        original = baseline.reserved_leaf_problems

        def before_a9(structure):  # the rule ssdp-shadow-2's genesis predates (SD-69); ssds.unclassified still holds
            return [(u, d) for u, d in original(structure) if u not in ("ssds.manifest", "ssds.policy")]

        with mock.patch.object(baseline, "reserved_leaf_problems", before_a9):
            prepared = prepare_genesis(self.spec(modes={"*": {"mode": "UNGOVERNED"}}), self.home, self.trees)
            self.assertTrue(prepared.valid, prepared.problems)
            admit_genesis(self.home, "demo", sshsig(self.private, prepared.message))
        patch = mock.patch("ssds.cli.ssds_home", return_value=self.home.root)
        patch.start()
        self.addCleanup(patch.stop)
        self.snapshot = self.root / "boundary.json"

    def human(self) -> str:
        from ssds.ledger.read import human_key_id

        return human_key_id(self.public)

    def composition(self):
        from ssds.cli import Composition

        return Composition("demo", self.product)

    def entries(self):
        chain = read_chain(self.home.ledger_repository("demo"), "demo")
        return chain.entries[: chain.readable_through + 1]

    def state(self):
        access = self.composition().access
        return derive(access.chain(), self.trees, ancestry=access.ancestry()).s

    def ruleset(self) -> dict:
        from ssds.derivation.history import History

        chain = read_chain(self.home.ledger_repository("demo"), "demo")
        return dict(History(chain, self.trees).ruleset(chain.readable_through))

    def boundary(self, command: str) -> None:
        args = ["--repository", str(self.product)]
        if command == "snapshot":
            args += ["--out", str(self.snapshot)]
        else:
            args += ["--before", str(self.snapshot)]
        result = subprocess.run([sys.executable, str(SCRIPTS / "shadow_boundary.py"), command, *args],
                                capture_output=True, text=True, timeout=120)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def around(self, action):
        """The runbook's rule: a snapshot before and a comparison after every SSDS command."""

        self.boundary("snapshot")
        result = action()
        self.boundary("compare")
        return result

    def signed(self, directory: Path) -> Path:
        (directory / "request-message.txt.sig").write_text(
            sshsig(self.private, (directory / "request-message.txt").read_bytes()))
        return directory

    def test_the_runbook(self) -> None:
        self.assertNotIn("ssds.manifest", self.state().view.structure.units, "SD-69: the genesis lacks it")

        # (1) the declarations committed on the observed branch, with the policy file the genesis default names
        # (ssds.policy's scope resolves only to a file that exists: STRUCT_TERM_UNRESOLVED otherwise); a product
        # change, before the comparison starts
        manifest = self.product / ".ssds" / "manifest.toml"
        manifest.write_text(UNREPAIRED + DECLARATIONS)
        (self.product / ".ssds" / "policy.toml").write_text("schema = 1\n")
        commit(self.product, "declare the reserved leaves (SD-69)")
        ruleset_before = self.ruleset()

        # (2) one pass absorbs them: their keys quarantined
        report = self.around(lambda: self.composition().serve("main"))
        self.assertTrue(report["absorbed"], report)
        quarantined = {k for k in self.state().s0.quarantine if k[0].startswith("ssds.")}
        self.assertEqual({u for u, _ in quarantined}, {"ssds.manifest", "ssds.policy"}, quarantined)

        # (3) the author writes the inputs and prepares the request
        records, deltas = script("reserved_leaves").repair_inputs(self.composition(), "2026-10-27T00:00:00Z")
        self.assertEqual(sorted(tuple(d["key"]) for d in deltas), sorted(quarantined), "one per key")
        directory, summary = self.around(lambda: self.composition().prepare("submit", records, deltas, self.human()))
        for delta in deltas:
            self.assertIn(json.dumps(delta, sort_keys=True), summary)

        # (4) the stakeholder signs and admits
        decision = self.around(lambda: self.composition().admit_prepared(self.signed(directory), "main"))
        self.assertEqual((decision["decision"], decision["reasons"], decision["refused"]), ("ACCEPT", (), ()),
                         decision)

        # (5) Σ declares the three reserved leaves
        state = self.state()
        units = state.view.structure.units
        self.assertEqual(units["ssds.manifest"].declared_kind, "MANIFEST")
        self.assertEqual(units["ssds.policy"].declared_kind, "POLICY")
        self.assertIn("ssds.unclassified", units)
        self.assertFalse({k for k in state.s0.quarantine if k[0] in ("ssds.manifest", "ssds.policy")},
                         "nothing of theirs is left quarantined")
        import hashlib

        self.assertEqual(self.ruleset(), ruleset_before, "the repair adopts no ruleset")
        policy = (self.product / ".ssds" / "policy.toml").read_bytes()
        self.assertEqual(ruleset_before["policy"], "sha256:" + hashlib.sha256(policy).hexdigest(),
                         "the committed policy file is the genesis policy object, byte for byte")

        # (6) the restart check: two passes, the second appending nothing
        before = len(self.entries())
        for _ in range(2):
            self.assertFalse(self.around(lambda: self.composition().serve("main"))["absorbed"])
        self.assertEqual(len(self.entries()), before, "a records-only admission is never fenced (F1)")

        # (7) dispatcher serve issues nothing; a records-only report and submit; a decide refused
        observed = self.around(lambda: self.composition().observe())
        self.assertNotIn("withheld", observed, observed)
        finding = {k: v for k, v in record("FINDING", target={"units": ["code"]},
                                           fields={"materiality": "ROUTINE"}).items()
                   if k not in ("id", "actor", "actor_class", "binding")}
        available = {k: v for k, v in record("AVAILABILITY", target={"digest": "sha256:" + "6" * 64},
                                             outcome="AVAILABLE").items()
                     if k not in ("id", "actor", "actor_class", "binding")}
        for command, body in (("report", finding), ("submit", available)):
            with self.subTest(command=command):
                prepared, _ = self.around(lambda: self.composition().prepare(command, [body], [], self.human()))
                admitted = self.around(lambda: self.composition().admit_prepared(self.signed(prepared), "main"))
                self.assertEqual(admitted["decision"], "ACCEPT", admitted)
        decision_record = {k: v for k, v in record("HUMAN_DECISION", target={"units": ["code"]},
                                                   outcome="APPROVE").items()
                           if k not in ("id", "actor", "actor_class", "binding")}
        refused, _ = self.composition().prepare("decide", [decision_record], [], self.human())
        before = len(self.entries())
        self.boundary("snapshot")
        with self.assertRaises(BoundaryRefused):
            self.composition().admit_prepared(self.signed(refused), "main")
        self.boundary("compare")

        # (8) one candidate request through the library API, refused at entry and logged
        admission = self.composition().admission()
        chain = read_chain(self.home.ledger_repository("demo"), "demo")
        from ssds.admission.request import expected_head

        entries = chain.entries[: chain.readable_through + 1]
        candidate = {"binding": None, "claims": [], "base_position": len(entries) - 1,
                     "base_commit": expected_head(entries), "candidates": ["0" * 40], "adopted_deltas": [],
                     "records": [], "objects": {}}
        candidate["binding"] = {"human": {"actor": self.human(),
                                          "signature": sshsig(self.private, request_message(candidate))}}
        self.boundary("snapshot")
        with self.assertRaises(BoundaryRefused):
            admission.admit(candidate, expected_head(entries))
        self.boundary("compare")
        self.assertEqual(len(self.entries()), before, "the decide and the candidate appended nothing")
        logged = (self.home.root / "state" / "demo" / "boundary.jsonl").read_text().splitlines()
        self.assertEqual(len(logged), 2, logged)

    def test_without_the_policy_file_the_adoption_is_rejected(self) -> None:
        """The finding the rehearsal made: F122's step (1) needs the policy file, not only the declarations."""

        (self.product / ".ssds" / "manifest.toml").write_text(UNREPAIRED + DECLARATIONS)
        commit(self.product, "declare the reserved leaves, no policy file")
        self.composition().serve("main")
        records, deltas = script("reserved_leaves").repair_inputs(self.composition(), "2026-10-27T00:00:00Z")
        directory, _ = self.composition().prepare("submit", records, deltas, self.human())
        decision = self.composition().admit_prepared(self.signed(directory), "main")
        self.assertEqual((decision["decision"], decision["reasons"]), ("REJECT", ("STRUCT_TERM_UNRESOLVED",)))

    def test_the_inputs_script(self) -> None:
        import contextlib
        import io

        helper = script("reserved_leaves")
        args = ["--ledger", "demo", "--repository", str(self.product), "--actor", self.human()]
        with self.assertRaises(SystemExit) as nothing:
            helper.main([*args, "--out", str(self.root / "early")])
        self.assertIn("no declaration key", str(nothing.exception))
        self.assertFalse((self.root / "early").exists())
        (self.product / ".ssds" / "manifest.toml").write_text(UNREPAIRED + DECLARATIONS)
        commit(self.product, "declare the reserved leaves (SD-69)")
        self.composition().serve("main")
        out, printed = self.root / "inputs", io.StringIO()
        with contextlib.redirect_stdout(printed):
            self.assertEqual(helper.main([*args, "--out", str(out)]), 0)
        records = json.loads((out / "records.json").read_text())
        deltas = sorted(out.glob("delta-*.json"))
        self.assertEqual(len(records), len(deltas))
        self.assertTrue(all(r["kind"] == "INTAKE_DISPOSITION" and r["outcome"] == "ABSORB" and "id" not in r
                            for r in records))
        self.assertEqual([r["governs"] for r in records], [{"mode": "LEGACY", "protocol": "7.2.1"}] * len(records),
                         "the genesis record's governs")
        command = printed.getvalue().splitlines()[-1].split()
        self.assertEqual(command[:4], ["ssds", "submit", "--ledger", "demo"])
        self.assertEqual(command.count("--adopt"), len(deltas))
        with self.assertRaises(FileExistsError):
            helper.main([*args, "--out", str(out)])  # a new directory each time


if __name__ == "__main__":
    unittest.main()
