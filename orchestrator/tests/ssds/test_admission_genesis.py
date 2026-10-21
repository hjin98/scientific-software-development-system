"""Admission's genesis path on fixture repositories (catalogue §19.9, §21.3, §22.4, §23.3; plan step 6).

The human gate is played by a throwaway key made for the test, signing with
the same ``ssh-keygen -Y sign -n ssds`` command the stakeholder runs. Each
refusal case states the catalogue rule it breaks; the shadow-boundary checks
compare the product repository before and after at run time.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from ssds.admission.genesis import GenesisRefused, GenesisSpec, Home, admit_genesis, prepare_genesis
from ssds.content import read_tree
from ssds.derivation import consequences
from ssds.ledger.qualification import FileWitness
from ssds.ledger.read import read_chain

from ._fixtures import commit, git, human_key, init_repo, sshsig

MANIFEST = '''schema = 1

[[unit]]
id = "guide"
kind = "D3"
role = "composite"
scope = [{ path = "guide.md" }]

[[unit]]
id = "guide.intro"
subject = false
part_of = "guide"
scope = [{ file = "guide.md", heading = ["Introduction"] }]

[[unit]]
id = "code"
kind = "D4"
scope = [{ prefix = "src/" }]
'''
GUIDE = "# Guide\n\n## Introduction\n\nHello.\n\n## Usage\n\nRun it.\n"
LEGACY = {"mode": "LEGACY", "protocol": "7.2.1"}


def product_state(repo: Path) -> tuple[str, str, str]:
    """Refs, the object inventory and the working tree status: the shadow boundary's run-time sensor."""

    return (git(repo, "for-each-ref", "--format=%(refname) %(objectname)"),
            git(repo, "count-objects", "-v"), git(repo, "status", "--porcelain", "--ignored"))


class GenesisFixture(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.product = init_repo(self.root / "product")
        (self.product / ".ssds").mkdir()
        (self.product / ".ssds" / "manifest.toml").write_text(MANIFEST)
        (self.product / "guide.md").write_text(GUIDE)
        (self.product / "src").mkdir()
        (self.product / "src" / "tool.py").write_text("import os\n")
        self.baseline = commit(self.product, "baseline")
        self.home = Home(self.root / "ssds-home")
        self.private, self.public = human_key(self.root)

    def trees(self, commit_id: str):
        return read_tree(self.product, commit_id)

    def spec(self, **overrides) -> GenesisSpec:
        values = dict(project="demo-project", ledger_id="demo", product_repository=self.product,
                      baseline_commit=self.baseline, human_keys=(self.public,), protocol="7.2.1",
                      modes={"guide": LEGACY, "*": {"mode": "UNGOVERNED"}}, recorded_at="2026-10-19T00:00:00Z")
        values.update(overrides)
        return GenesisSpec(**values)  # type: ignore[arg-type]


class Admission(GenesisFixture):
    def test_prepare_sign_admit_then_derive(self) -> None:
        before = product_state(self.product)
        prepared = prepare_genesis(self.spec(), self.home, self.trees)
        self.assertTrue(prepared.valid, prepared.problems)
        self.assertEqual(prepared.message, f"ssds genesis {prepared.digest}\n".encode("ascii"))
        report = json.loads(prepared.report.read_bytes())
        self.assertEqual((report["valid"], report["genesis_digest"]), (True, prepared.digest))
        self.assertFalse(self.home.ledger_repository("demo").exists(), "nothing is published before the gate")
        self.assertEqual(FileWitness(self.home.witness_root).read("demo"), [])

        admitted = admit_genesis(self.home, "demo", sshsig(self.private, prepared.message))
        self.assertEqual(admitted.qualification, "QUALIFIED")
        self.assertEqual(admitted.genesis_digest, prepared.digest)
        chain = read_chain(admitted.repository, "demo")
        self.assertIsNone(chain.halt)
        self.assertEqual(len(chain.entries), 1)
        self.assertEqual(chain.entries[0].digest, admitted.entry_digest)
        self.assertEqual(len(FileWitness(self.home.witness_root).read("demo")), 1, "the witness acknowledged it")
        self.assertEqual(self.home.high_water("demo").get().entry_digest, admitted.entry_digest)

        view = consequences(chain, self.trees)
        self.assertTrue(view.current_assertion, view.assertion_withheld)
        self.assertEqual(view.s.mode("guide"), "LEGACY")
        self.assertEqual(view.s.mode("code"), "UNGOVERNED", "a subject without its own mode takes \"*\"")
        self.assertEqual(sorted(view.s.view.structure.units), ["code", "guide", "guide.intro"])
        self.assertFalse(view.s.s0.quarantine, "Σ_0 is the baseline manifest")

        self.assertEqual(product_state(self.product), before, "nothing is written to the product repository")
        refs = git(admitted.repository, "for-each-ref", "--format=%(refname)").split()
        self.assertEqual(refs, ["refs/ssds/ledger/demo"], "the append touches only the ledger ref")
        for path in (self.home.ledger_repository("demo"), self.home.witness_root, self.home.admission_key("demo")):
            self.assertTrue(path.is_relative_to(self.home.root))

    def test_a_second_genesis_for_the_same_ledger_is_refused(self) -> None:
        prepared = prepare_genesis(self.spec(), self.home, self.trees)
        admit_genesis(self.home, "demo", sshsig(self.private, prepared.message))
        again = prepare_genesis(self.spec(), self.home, self.trees)
        self.assertTrue(any("already exists" in p for p in again.problems), again.problems)
        with self.assertRaises(GenesisRefused):
            admit_genesis(self.home, "demo", sshsig(self.private, prepared.message))


class Refusals(GenesisFixture):
    def assertRefused(self, fragment: str, **overrides) -> None:
        prepared = prepare_genesis(self.spec(**overrides), self.home, self.trees)
        self.assertFalse(prepared.valid)
        self.assertTrue(any(fragment in p for p in prepared.problems), prepared.problems)
        self.assertIsNone(prepared.digest, "a refused genesis offers nothing to sign")
        self.assertTrue(prepared.workspace is None or not (prepared.workspace / "proposal.json").exists())
        self.assertFalse(self.home.ledger_repository("demo").exists(), "a refused genesis publishes nothing")

    def test_only_legacy_or_ungoverned_modes(self) -> None:
        self.assertRefused("only LEGACY or UNGOVERNED", modes={"guide": {"mode": "NATIVE", "ruleset": "ssds-rules/1"},
                                                               "*": {"mode": "UNGOVERNED"}})
        self.assertRefused("only LEGACY or UNGOVERNED", modes={"guide": LEGACY, "*": {"mode": "NATIVE"}})

    def test_every_declaration_is_validated(self) -> None:
        self.assertRefused("does not declare as a subject", modes={"guide.intro": LEGACY, "*": {"mode": "UNGOVERNED"}})
        self.assertRefused("no default mode", modes={"guide": LEGACY})
        self.assertRefused("names no protocol", modes={"guide": {"mode": "LEGACY"}, "*": {"mode": "UNGOVERNED"}})

    def test_static_checks_of_the_baseline_structure(self) -> None:
        (self.product / ".ssds" / "manifest.toml").write_text(MANIFEST.replace('kind = "D4"\n', ""))
        broken = commit(self.product, "subject without kind")
        prepared = prepare_genesis(self.spec(baseline_commit=broken), self.home, self.trees)
        self.assertFalse(prepared.valid)
        self.assertIsNone(prepared.digest)
        (self.product / ".ssds" / "manifest.toml").write_text("schema = [\n")
        self.assertRefused("does not parse", baseline_commit=commit(self.product, "unparsable"))
        (self.product / ".ssds" / "manifest.toml").unlink()
        self.assertRefused("no unit manifest", baseline_commit=commit(self.product, "no manifest"))

    def test_every_newly_declared_term_resolves(self) -> None:
        """Review 0e49deb A-B4: no file or span unit is declared over nothing (catalogue §1.9)."""

        extra = {
            "missing file": '[{ path = "missing.md" }]',
            "missing heading": '[{ file = "guide.md", heading = ["Nowhere"] }]',
            "missing symbol": '[{ file = "src/tool.py", symbol = "absent" }]',
            "missing anchor": '[{ file = "guide.md", anchor = "absent" }]',
        }
        for name, scope in extra.items():
            with self.subTest(name):
                (self.product / ".ssds" / "manifest.toml").write_text(
                    MANIFEST + f'\n[[unit]]\nid = "docs"\nkind = "D3"\nscope = {scope}\n')
                self.assertRefused("TERM_ABSENT docs", baseline_commit=commit(self.product, name))
        (self.product / "empty.md").write_text("")
        (self.product / ".ssds" / "manifest.toml").write_text(
            MANIFEST + '\n[[unit]]\nid = "docs"\nkind = "D3"\nscope = [{ path = "empty.md" }]\n'
            '\n[[unit]]\nid = "later"\nkind = "D4"\nscope = [{ prefix = "later/" }]\n')
        prepared = prepare_genesis(self.spec(baseline_commit=commit(self.product, "empty file, empty prefix")),
                                   self.home, self.trees)
        self.assertTrue(prepared.valid, "an empty file is present, and a prefix is exempt from the presence check")

    def test_trust_roots_and_witness_reachability(self) -> None:
        self.assertRefused("no human key", human_keys=())
        self.assertRefused("human key", human_keys=("ssh-rsa AAAA not-ed25519",))
        self.assertRefused("witness model", deployment_class="TEAM")
        self.home.root.mkdir(parents=True, exist_ok=True)
        if self.home.witness_root.is_dir():
            self.home.witness_root.rmdir()
        self.home.witness_root.write_text("a file, not a witness directory\n")
        self.assertRefused("witness unreachable")

    def test_a_ledger_id_never_directs_a_write_outside_the_home(self) -> None:
        """Review 0e49deb A-B3: the id is checked before any path is built or anything is written."""

        outside = self.root / "outside"
        for ledger_id in ("../../escaped", "/abs/olute", "a/b", "..", "Upper"):
            with self.subTest(ledger_id=ledger_id):
                prepared = prepare_genesis(self.spec(ledger_id=ledger_id), self.home, self.trees)
                self.assertFalse(prepared.valid)
                self.assertIsNone(prepared.report)
                self.assertTrue(any("not a ledger id" in p for p in prepared.problems), prepared.problems)
                with self.assertRaises(GenesisRefused):
                    admit_genesis(self.home, ledger_id, "signature")
        self.assertFalse(self.home.root.exists(), "a refused id creates nothing, not even the home")
        self.assertFalse((self.root / "escaped").exists())
        outside.mkdir()
        self.home.root.mkdir(parents=True)
        (self.home.root / "genesis").symlink_to(outside, target_is_directory=True)
        prepared = prepare_genesis(self.spec(), self.home, self.trees)
        self.assertFalse(prepared.valid)
        self.assertTrue(any("outside the SSDS home" in p or "symbolic link" in p for p in prepared.problems),
                                prepared.problems)
        self.assertEqual(list(outside.iterdir()), [], "a symbolic link does not carry a write out of the home")

    def test_a_symbolic_link_at_a_file_never_carries_a_write_out_of_the_home(self) -> None:
        """Review 517af45 A-B3: every file written is checked, not only its directory."""

        sentinel = self.root / "sentinel.txt"
        for name in ("report.json", "proposal.json", "approval-message.txt"):
            with self.subTest(name=name):
                sentinel.write_text("untouched\n")
                workspace = self.home.root / "genesis" / "demo"
                workspace.mkdir(parents=True, exist_ok=True)
                for existing in workspace.iterdir():
                    existing.unlink()
                (workspace / name).symlink_to(sentinel)
                prepared = prepare_genesis(self.spec(), self.home, self.trees)
                self.assertFalse(prepared.valid)
                self.assertTrue(any("outside the SSDS home" in p or "symbolic link" in p for p in prepared.problems),
                                prepared.problems)
                self.assertEqual(sentinel.read_text(), "untouched\n")
                with self.assertRaises(GenesisRefused):
                    admit_genesis(self.home, "demo", "signature")
                (workspace / name).unlink()
        inside = self.home.root / "inside.txt"
        inside.write_text("home file\n")
        workspace = self.home.root / "genesis" / "demo"
        (workspace / "report.json").symlink_to(inside)
        prepared = prepare_genesis(self.spec(), self.home, self.trees)
        self.assertTrue(any("symbolic link" in p for p in prepared.problems), "a link is refused even into the home")
        self.assertEqual(inside.read_text(), "home file\n")
        (workspace / "report.json").unlink()
        state = self.home.root / "state" / "demo"
        state.mkdir(parents=True)
        (state / "high-water.json").symlink_to(sentinel)
        self.assertFalse(prepare_genesis(self.spec(), self.home, self.trees).valid)
        self.assertEqual(sentinel.read_text(), "untouched\n")

    def test_no_symbolic_link_anywhere_in_the_operator_tree(self) -> None:
        """Review 137b763 A-B3: one rule for the family; Git writes included, the product never touched."""

        before = product_state(self.product)
        outside = self.root / "outside"
        outside.mkdir()

        def bare_ledger_with(link: str, target: Path) -> Path:
            repository = self.home.root / "ledgers" / "demo.git"
            repository.mkdir(parents=True)
            subprocess.run(["git", "init", "--quiet", "--bare", str(repository)], check=True)
            moved = repository / link
            if moved.is_dir():
                shutil.rmtree(moved)
            moved.symlink_to(target, target_is_directory=True)
            return repository

        cases = {
            "objects outside": ("objects", outside),
            "refs outside": ("refs", outside),
            "refs into the product": ("refs", self.product / ".git" / "refs"),
        }
        for name, (link, target) in cases.items():
            with self.subTest(name):
                repository = bare_ledger_with(link, target)
                prepared = prepare_genesis(self.spec(), self.home, self.trees)
                self.assertFalse(prepared.valid)
                self.assertTrue(any("already exists" in p or "symbolic link" in p for p in prepared.problems),
                                prepared.problems)
                shutil.rmtree(repository)
        prepared = prepare_genesis(self.spec(), self.home, self.trees)
        self.assertTrue(prepared.valid, prepared.problems)
        signature = sshsig(self.private, prepared.message)
        bare_ledger_with("refs", self.product / ".git" / "refs")  # appears between the gate and the append
        with self.assertRaises(GenesisRefused):
            admit_genesis(self.home, "demo", signature)
        shutil.rmtree(self.home.root / "ledgers" / "demo.git")
        for component in ("witness", "state"):
            with self.subTest(component=component):
                target = self.home.root / component
                kept = self.root / f"kept-{component}"
                if target.exists():
                    target.rename(kept)
                target.symlink_to(outside, target_is_directory=True)
                with self.assertRaises(GenesisRefused):
                    admit_genesis(self.home, "demo", signature)
                target.unlink()
                if kept.exists():
                    kept.rename(target)
        (self.home.root / "witness" / "planted").symlink_to(outside)
        with self.assertRaises(GenesisRefused):
            admit_genesis(self.home, "demo", signature)
        (self.home.root / "witness" / "planted").unlink()
        self.assertEqual(list(outside.iterdir()), [], "nothing was written outside the home")
        self.assertEqual(product_state(self.product), before, "nothing was written to the product")
        self.assertEqual(admit_genesis(self.home, "demo", signature).qualification, "QUALIFIED", "the clean control")
        self.assertEqual(product_state(self.product), before)

    def test_operator_files_are_published_never_written_through(self) -> None:
        """Review d8bdfd3 A-B8: a hard link at an operator file never carries the write to its other name."""

        before = product_state(self.product)
        guide = (self.product / "guide.md").read_bytes()
        workspace = self.home.root / "genesis" / "demo"
        workspace.mkdir(parents=True)
        os.link(self.product / "guide.md", workspace / "report.json")
        state = self.home.root / "state" / "demo"
        state.mkdir(parents=True)
        os.link(self.product / "guide.md", state / "high-water.json")
        prepared = prepare_genesis(self.spec(), self.home, self.trees)
        self.assertTrue(prepared.valid, prepared.problems)
        admitted = admit_genesis(self.home, "demo", sshsig(self.private, prepared.message))
        self.assertEqual(admitted.qualification, "QUALIFIED")
        self.assertEqual((self.product / "guide.md").read_bytes(), guide, "the product file keeps its bytes")
        self.assertEqual(product_state(self.product), before)
        self.assertEqual(json.loads((workspace / "report.json").read_bytes())["valid"], True, "the name was replaced")
        self.assertEqual(os.stat(workspace / "report.json").st_nlink, 1)
        self.assertEqual(json.loads((state / "high-water.json").read_bytes())["position"], 0)

    def test_the_home_lies_outside_every_repository(self) -> None:
        """Review d8bdfd3 A-B10: a home inside the product worktree is refused before anything is created."""

        before = product_state(self.product)
        inside = Home(self.product / "operator-state")
        prepared = prepare_genesis(self.spec(), inside, self.trees)
        self.assertFalse(prepared.valid)
        self.assertTrue(any("outside every repository" in p for p in prepared.problems), prepared.problems)
        self.assertFalse((self.product / "operator-state").exists())
        self.assertEqual(product_state(self.product), before)
        bare = self.root / "bare.git"
        subprocess.run(["git", "init", "--quiet", "--bare", str(bare)], check=True)
        self.assertFalse(prepare_genesis(self.spec(), Home(bare / "home"), self.trees).valid, "nor in a bare one")
        marker_only = self.root / "plain"
        (marker_only / ".git").mkdir(parents=True)  # an empty .git directory is not a repository
        self.assertTrue(prepare_genesis(self.spec(ledger_id="plain"), Home(marker_only / "home"), self.trees).valid)
        outside = self.root / "real-home"
        outside.mkdir()
        (self.root / "linked-home").symlink_to(outside, target_is_directory=True)
        linked = prepare_genesis(self.spec(), Home(self.root / "linked-home"), self.trees)
        self.assertTrue(linked.valid, linked.problems)

    def test_no_repository_inside_the_operator_tree(self) -> None:
        """Review b341109 A-B12: a repository nested at an operator write location is refused before any write."""

        for location in ("genesis/demo", "state/demo", "genesis", "keys/admission"):
            with self.subTest(location=location):
                nested = init_repo(self.home.root / location)
                (nested / "report.json").write_text("tracked\n")
                commit(nested, "a tracked output")
                before = product_state(nested)
                prepared = prepare_genesis(self.spec(), self.home, self.trees)
                self.assertFalse(prepared.valid)
                self.assertTrue(any("is a repository" in p for p in prepared.problems), prepared.problems)
                self.assertEqual((nested / "report.json").read_text(), "tracked\n")
                self.assertEqual(product_state(nested), before)
                shutil.rmtree(self.home.root)
        prepared = prepare_genesis(self.spec(), self.home, self.trees)
        self.assertTrue(prepared.valid, "the clean control")
        admitted = admit_genesis(self.home, "demo", sshsig(self.private, prepared.message))
        self.assertEqual(admitted.qualification, "QUALIFIED", "the ledger's own repository is allowed")
        self.home.check("demo")

    def test_an_unreadable_baseline_or_policy(self) -> None:
        self.assertRefused("cannot be read", baseline_commit="0" * 40)
        (self.product / ".ssds" / "policy.toml").write_text("schema = 2\n")
        self.assertRefused("policy", baseline_commit=commit(self.product, "bad policy"))

    def test_the_gate_refuses_another_key_other_bytes_and_a_changed_proposal(self) -> None:
        prepared = prepare_genesis(self.spec(), self.home, self.trees)
        intruder, _ = human_key(self.root, "intruder")
        for name, signature in (("another key", sshsig(intruder, prepared.message)),
                                ("other bytes", sshsig(self.private, prepared.message + b"x")),
                                ("another namespace", sshsig(self.private, prepared.message, namespace="git"))):
            with self.subTest(name):
                with self.assertRaises(GenesisRefused):
                    admit_genesis(self.home, "demo", signature)
                self.assertFalse(self.home.ledger_repository("demo").exists())
        signature = sshsig(self.private, prepared.message)
        proposal = prepared.workspace / "proposal.json"
        original = proposal.read_bytes()
        proposal.write_bytes(original.replace(b'"demo-project"', b'"other-project"'))
        with self.assertRaises(GenesisRefused):
            admit_genesis(self.home, "demo", signature)
        self.assertFalse(self.home.ledger_repository("demo").exists())
        proposal.write_bytes(original)
        self.assertEqual(admit_genesis(self.home, "demo", signature).qualification, "QUALIFIED")


if __name__ == "__main__":
    unittest.main()
