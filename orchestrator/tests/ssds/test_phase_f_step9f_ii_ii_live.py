"""Phase F step 9f-ii-ii: the sandbox's live properties (reading F2, F113), run under a real ``bwrap``.

They need unprivileged user namespaces, which the agent's own sandbox denies, so they run on the host, where the
operator sets ``SSDS_LIVE_SANDBOX=1`` and records the results in the qualification evidence file (plan check of
23d2f5f2, answer 3). Without it they are skipped with that reason, and the step's exit counts them unexecuted:
required checks, which block until recorded. One test per F2 property: a scrubbed environment, its own ``HOME``, no
agent socket or credentials, no network, an operator tree unreadable, the workspace read-only; and a reached time
bound ending ``TIME_BOUND``.
"""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from ssds.content import Entry, Tree
from ssds.dispatcher.home import DispatcherHome
from ssds.dispatcher.runner import RunnerProvider, Sandbox, Workspaces

LIVE = os.environ.get("SSDS_LIVE_SANDBOX") == "1"
PROBE = r'''
import json, os, socket
out = {"env": sorted(os.environ), "home": os.environ.get("HOME"), "cwd": os.getcwd()}
out["ssh"] = os.environ.get("SSH_AUTH_SOCK")
try:
    socket.create_connection(("1.1.1.1", 53), timeout=2).close()
    out["net"] = "connected"
except OSError as exc:
    out["net"] = type(exc).__name__
try:
    open(os.environ.get("CANARY", "/nonexistent"), "rb").read()
    out["canary"] = "read"
except OSError as exc:
    out["canary"] = type(exc).__name__
try:
    open("/work/written", "w").write("x")
    out["work"] = "written"
except OSError as exc:
    out["work"] = type(exc).__name__
out["tree"] = open("/work/a.txt").read()
open("/out/outputs.json", "w").write(json.dumps(out))
'''


@unittest.skipUnless(LIVE, "needs user namespaces: run on the host with SSDS_LIVE_SANDBOX=1 (F113's live tests)")
class Live(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.home = DispatcherHome(Path(self._tmp.name) / "home")
        canary = self.home.root / "keys" / "dispatcher" / "canary"
        canary.parent.mkdir(parents=True)
        canary.write_bytes(b"secret")
        self.canary = canary
        self.workspaces = Workspaces(self.home)
        self.tree = Tree({"a.txt": Entry("100644", b"hello\n"), "probe.py": Entry("100644", PROBE.encode())})

    def run_probe(self) -> dict:
        os.environ["SSH_AUTH_SOCK"] = os.environ.get("SSH_AUTH_SOCK", "/tmp/agent.sock")  # present outside
        provider = RunnerProvider(argv=("/usr/bin/python3", "-I", "-c",
                                        f"import os; os.environ['CANARY'] = {str(self.canary)!r}; "
                                        "exec(open('/work/probe.py').read())"))
        ws = self.workspaces.materialize("demo", self.tree)
        found = Sandbox(self.workspaces, (self.home.root,)).execute(ws, self.tree, provider, 60.0)
        self.assertIsNone(found.incomplete, found.detail)
        return found.outcome

    def test_the_f2_properties(self) -> None:
        seen = self.run_probe()
        with self.subTest(property="a scrubbed environment"):
            self.assertLessEqual(set(seen["env"]), {"PATH", "HOME", "LANG", "TMPDIR", "PWD", "LC_CTYPE", "CANARY"})
        with self.subTest(property="its own HOME"):
            self.assertEqual(seen["home"], "/home/runner")
        with self.subTest(property="no agent socket or credentials"):
            self.assertIsNone(seen["ssh"])
        with self.subTest(property="no network"):
            self.assertNotEqual(seen["net"], "connected")
        with self.subTest(property="an operator tree unreadable"):
            self.assertNotEqual(seen["canary"], "read")
        with self.subTest(property="the workspace read-only"):
            self.assertNotEqual(seen["work"], "written")
        self.assertEqual(seen["tree"], "hello\n", "the materialized tree is what runs")

    def test_a_reached_time_bound(self) -> None:
        provider = RunnerProvider(argv=("/bin/sh", "-c", "sleep 30"))
        ws = self.workspaces.materialize("demo", self.tree)
        found = Sandbox(self.workspaces, (self.home.root,)).execute(ws, self.tree, provider, 1.0)
        self.assertEqual(found.incomplete, "TIME_BOUND")


if __name__ == "__main__":
    unittest.main()
