"""The step 7 operator script, end to end on a fixture repository and a temporary SSDS home.

The stakeholder's key is played by a throwaway key; the commands are the ones
the script prints. The repository is checked unchanged afterwards.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from ._fixtures import commit, git, human_key, init_repo

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "shadow_genesis.py"
MANIFEST = '''schema = 1

[[unit]]
id = "ssdp.protocol"
kind = "D3"
role = "composite"
scope = [{ prefix = "source/" }]

[[unit]]
id = "ssdp.protocol.roles"
subject = false
part_of = "ssdp.protocol"
scope = [{ prefix = "source/roles/" }]

[[unit]]
id = "ssds8.manual"
kind = "D3"
scope = [{ path = "manual.md" }]

[[unit]]
id = "orchestrator.program"
kind = "D4"
scope = [{ prefix = "orchestrator/src/" }]
'''
RELEASE_STATE = 'schema_version: 1\naccepted_current:\n  version: "9.9.9"\n'


class ShadowGenesisScript(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        root = Path(self._tmp.name)
        self.repo = init_repo(root / "repo")
        for path, text in {".ssds/manifest.toml": MANIFEST, "PROTOCOL-RELEASE-STATE.yaml": RELEASE_STATE,
                           "source/roles/a.md": "# A\n", "source/README.md": "# Source\n", "manual.md": "# Manual\n",
                           "orchestrator/src/tool.py": "import os\n"}.items():
            (self.repo / path).parent.mkdir(parents=True, exist_ok=True)
            (self.repo / path).write_text(text)
        self.baseline = commit(self.repo, "baseline")
        self.home = root / "home"
        self.private, _ = human_key(root)
        self.public = root / "approver.pub"
        self.env = {**os.environ, "SSDS_HOME": str(self.home)}

    def run_script(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), "--repository", str(self.repo), "--ledger-id", "demo", *args],
                              capture_output=True, text=True, env=self.env, timeout=240, check=False)

    def test_prepare_sign_admit_derive(self) -> None:
        before = git(self.repo, "for-each-ref"), git(self.repo, "status", "--porcelain", "--ignored")
        prepared = self.run_script("prepare", "--public-key", str(self.public))
        self.assertEqual(prepared.returncode, 0, prepared.stdout + prepared.stderr)
        digest = re.search(r"genesis digest:\s+(sha256:[0-9a-f]{64})", prepared.stdout).group(1)
        message = Path(re.search(r"approval message:\s+(\S+)", prepared.stdout).group(1))
        report = json.loads((self.home / "genesis" / "demo" / "report.json").read_text())
        self.assertEqual((report["valid"], report["genesis_digest"], report["baseline_commit"]), (True, digest, self.baseline))
        self.assertEqual(report["modes"]["ssdp.protocol"], {"mode": "LEGACY", "protocol": "9.9.9"},
                         "p comes from the release-state owner")
        self.assertIn(f"ssh-keygen -Y sign -f <your private key> -n ssds {message}", prepared.stdout)

        subprocess.run(["ssh-keygen", "-q", "-Y", "sign", "-f", str(self.private), "-n", "ssds", str(message)],
                       check=True, capture_output=True, stdin=subprocess.DEVNULL, timeout=60)
        admitted = self.run_script("admit", "--signature", str(message) + ".sig")
        self.assertEqual(admitted.returncode, 0, admitted.stdout + admitted.stderr)
        self.assertIn("qualification:     QUALIFIED", admitted.stdout)
        derivation = json.loads((self.home / "genesis" / "demo" / "derivation.json").read_text())
        self.assertTrue(derivation["current_assertion"], derivation["assertion_withheld"])
        self.assertEqual({s: v["mode"] for s, v in derivation["subjects"].items()},
                         {"ssdp.protocol": "LEGACY", "ssds8.manual": "LEGACY", "orchestrator.program": "UNGOVERNED"})
        self.assertEqual(derivation["subjects"]["ssdp.protocol"]["parts"], ["ssdp.protocol.roles"])
        self.assertEqual(self.run_script("derive").returncode, 0)
        self.assertEqual((git(self.repo, "for-each-ref"), git(self.repo, "status", "--porcelain", "--ignored")), before,
                         "the repository is only read")

    def admitted(self) -> None:
        prepared = self.run_script("prepare", "--public-key", str(self.public))
        message = Path(re.search(r"approval message:\s+(\S+)", prepared.stdout).group(1))
        subprocess.run(["ssh-keygen", "-q", "-Y", "sign", "-f", str(self.private), "-n", "ssds", str(message)],
                       check=True, capture_output=True, stdin=subprocess.DEVNULL, timeout=60)
        self.assertEqual(self.run_script("admit", "--signature", str(message) + ".sig").returncode, 0)

    def report(self) -> tuple[int, dict]:
        result = self.run_script("derive")
        return result.returncode, json.loads((self.home / "genesis" / "demo" / "derivation.json").read_text())

    def test_no_current_assertion_without_qualification(self) -> None:
        """Review 0e49deb A-B1: the report qualifies first; an unqualified replica gives historical views only."""

        self.admitted()
        code, report = self.report()
        self.assertEqual((code, report["qualification"], report["qualified_head"], report["current_assertion"]),
                         (0, "QUALIFIED", 0, True))
        checkpoint = next((self.home / "witness" / "demo").glob("*.json"))
        held = checkpoint.read_bytes()
        checkpoint.unlink()
        code, report = self.report()
        self.assertEqual((code, report["qualification"], report["current_assertion"]), (1, "UNQUALIFIED", False))
        self.assertTrue(report["assertion_withheld"][0].startswith("qualification UNQUALIFIED"))
        checkpoint.write_bytes(held)
        mark = self.home / "state" / "demo" / "high-water.json"
        kept = mark.read_bytes()
        mark.write_text(json.dumps({"position": 5, "entry_digest": "sha256:" + "5" * 64}))
        code, report = self.report()
        self.assertEqual((code, report["qualification"], report["current_assertion"]), (1, "ROLLBACK", False))
        mark.write_bytes(kept)
        self.assertEqual(self.report()[0], 0, "restored, it qualifies again")

    def test_a_provisional_successor_is_never_the_current_head(self) -> None:
        from ssds.ledger.append import HostKey, append_entry
        from ssds.ledger.read import read_chain

        from ._fixtures import entry, record

        self.admitted()
        repository = self.home / "ledgers" / "demo.git"
        chain = read_chain(repository, "demo")
        key = HostKey.from_private_bytes((self.home / "keys" / "admission" / "demo.ed25519").read_bytes())
        adoption = record("RULESET_ADOPTION", target=None, actor="human:SHA256:x",
                          fields={"system": "ssds-rules/1", "policy": "sha256:" + "0" * 64, "analyzers": ["x/1"]})
        append_entry(repository, entry("demo", 1, chain.entries[0].digest, key, lifecycle=adoption, obs=self.baseline),
                     key, chain.entries[0].commit)  # appended, never checkpointed: provisional
        code, report = self.report()
        self.assertEqual((report["entries"], report["qualification"], report["qualified_head"], report["provisional"]),
                         (2, "QUALIFIED", 0, 1))
        self.assertEqual((report["position"], report["head"]), (0, chain.entries[0].digest),
                         "the answer is derived at H*, not at the provisional entry")
        self.assertEqual((code, report["current_assertion"]), (0, True))

    def test_the_consumer_keeps_the_last_head_it_qualified(self) -> None:
        """Review 517af45 A-B5: after presenting head 1 current, a chain restored to 0 is a rollback."""

        from ssds.ledger.append import HostKey, append_entry, write_checkpoint
        from ssds.ledger.qualification import FileWitness
        from ssds.ledger.read import read_chain

        from ._fixtures import entry, record

        self.admitted()
        repository = self.home / "ledgers" / "demo.git"
        chain = read_chain(repository, "demo")
        key = HostKey.from_private_bytes((self.home / "keys" / "admission" / "demo.ed25519").read_bytes())
        adoption = record("RULESET_ADOPTION", target=None, actor="human:SHA256:x",
                          fields={"system": "ssds-rules/1", "policy": "sha256:" + "0" * 64,
                                  "analyzers": ["ssds.analyzer.python/1"]})
        appended = append_entry(repository, entry("demo", 1, chain.entries[0].digest, key, lifecycle=adoption,
                                                  obs=self.baseline), key, chain.entries[0].commit)
        write_checkpoint(FileWitness(self.home / "witness"), appended.checkpoint)
        code, report = self.report()
        self.assertEqual((code, report["qualified_head"], report["current_assertion"]), (0, 1, True))
        mark = json.loads((self.home / "state" / "demo" / "high-water.json").read_text())
        self.assertEqual((mark["position"], mark["entry_digest"]), (1, appended.digest), "the mark rose to H*")
        git(repository, "update-ref", "refs/ssds/ledger/demo", chain.entries[0].commit)  # a stale-consistent restore
        for checkpoint in (self.home / "witness" / "demo").glob("000000000001-*.json"):
            checkpoint.unlink()
        code, report = self.report()
        self.assertEqual((code, report["qualification"], report["current_assertion"]), (1, "ROLLBACK", False))

    def test_a_witness_only_restore_never_presents_an_older_head(self) -> None:
        """Review 137b763 A-B7: chain at 1, mark at 1, witnesses through 0 only: nothing current."""

        from ssds.ledger.append import HostKey, append_entry, write_checkpoint
        from ssds.ledger.qualification import FileWitness
        from ssds.ledger.read import read_chain

        from ._fixtures import entry, record

        self.admitted()
        repository = self.home / "ledgers" / "demo.git"
        chain = read_chain(repository, "demo")
        key = HostKey.from_private_bytes((self.home / "keys" / "admission" / "demo.ed25519").read_bytes())
        adoption = record("RULESET_ADOPTION", target=None, actor="human:SHA256:x",
                          fields={"system": "ssds-rules/1", "policy": "sha256:" + "0" * 64,
                                  "analyzers": ["ssds.analyzer.python/1"]})
        appended = append_entry(repository, entry("demo", 1, chain.entries[0].digest, key, lifecycle=adoption,
                                                  obs=self.baseline), key, chain.entries[0].commit)
        write_checkpoint(FileWitness(self.home / "witness"), appended.checkpoint)
        self.assertEqual(self.report()[1]["qualified_head"], 1)
        mark = self.home / "state" / "demo" / "high-water.json"
        kept = mark.read_bytes()
        (checkpoint,) = (self.home / "witness" / "demo").glob("000000000001-*.json")
        held = checkpoint.read_bytes()
        checkpoint.unlink()
        code, report = self.report()
        self.assertEqual((code, report["qualification"], report["current_assertion"]), (1, "UNQUALIFIED", False))
        self.assertEqual(mark.read_bytes(), kept, "the mark is unchanged")
        checkpoint.write_bytes(held)
        code, report = self.report()
        self.assertEqual((code, report["qualified_head"], report["current_assertion"]), (0, 1, True))

    def test_a_retired_witness_lineage_presents_nothing_current(self) -> None:
        """Review 517af45 NF3: the consumer passes the witness's retirement to qualification."""

        self.admitted()
        (self.home / "witness" / "demo" / "RETIREMENT").write_text("{}\n")
        code, report = self.report()
        self.assertEqual((code, report["qualification"], report["current_assertion"]), (1, "RETIRED", False))

    def test_the_report_is_never_written_through_a_link(self) -> None:
        """Review 517af45 A-B3, the report consumer's write."""

        self.admitted()
        sentinel = self.home.parent / "sentinel.txt"
        sentinel.write_text("untouched\n")
        target = self.home / "genesis" / "demo" / "derivation.json"
        target.unlink()
        target.symlink_to(sentinel)
        result = self.run_script("derive")
        self.assertEqual(result.returncode, 1)
        self.assertTrue("outside the SSDS home" in result.stdout or "symbolic link" in result.stdout, result.stdout)
        self.assertEqual(sentinel.read_text(), "untouched\n")

    def test_a_hard_linked_report_never_overwrites_the_product(self) -> None:
        """Review d8bdfd3 A-B8, through the CLI."""

        self.admitted()
        manual = (self.repo / "manual.md").read_bytes()
        target = self.home / "genesis" / "demo" / "derivation.json"
        target.unlink()
        os.link(self.repo / "manual.md", target)
        code, report = self.report()
        self.assertEqual((code, report["current_assertion"]), (0, True))
        self.assertEqual((self.repo / "manual.md").read_bytes(), manual)

    def test_a_home_inside_the_repository_is_refused(self) -> None:
        """Review d8bdfd3 A-B10, through the CLI."""

        self.env["SSDS_HOME"] = str(self.repo / "operator-state")
        result = self.run_script("prepare", "--public-key", str(self.public))
        self.assertEqual(result.returncode, 1)
        self.assertIn("outside every repository", result.stdout)
        self.assertFalse((self.repo / "operator-state").exists())

    def test_a_refused_genesis_prints_why_and_publishes_nothing(self) -> None:
        (self.repo / ".ssds" / "manifest.toml").write_text(MANIFEST.replace('id = "ssds8.manual"', 'id = "other"'))
        commit(self.repo, "no manual subject")
        prepared = self.run_script("prepare", "--public-key", str(self.public))
        self.assertEqual(prepared.returncode, 1)
        self.assertIn("ssds8.manual, which the manifest does not declare", prepared.stdout)
        self.assertFalse((self.home / "ledgers").exists())


    def test_the_cli_refuses_a_traversing_ledger_id(self) -> None:
        result = subprocess.run([sys.executable, str(SCRIPT), "--repository", str(self.repo), "--ledger-id", "../../escaped",
                                 "prepare", "--public-key", str(self.public)],
                                capture_output=True, text=True, env=self.env, timeout=240, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn("not a ledger id", result.stdout)
        self.assertFalse(self.home.exists())
        self.assertFalse((self.home.parent.parent / "escaped").exists())

if __name__ == "__main__":
    unittest.main()
