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

    def test_a_refused_genesis_prints_why_and_publishes_nothing(self) -> None:
        (self.repo / ".ssds" / "manifest.toml").write_text(MANIFEST.replace('id = "ssds8.manual"', 'id = "other"'))
        commit(self.repo, "no manual subject")
        prepared = self.run_script("prepare", "--public-key", str(self.public))
        self.assertEqual(prepared.returncode, 1)
        self.assertIn("ssds8.manual, which the manifest does not declare", prepared.stdout)
        self.assertFalse((self.home / "ledgers").exists())


if __name__ == "__main__":
    unittest.main()
