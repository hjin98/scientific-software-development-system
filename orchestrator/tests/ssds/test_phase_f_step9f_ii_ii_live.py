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
import errno, json, os, socket
out = {"env": sorted(os.environ), "home": os.environ.get("HOME"), "cwd": os.getcwd()}
out["ssh"] = os.environ.get("SSH_AUTH_SOCK")
out["agent_path"] = os.path.exists(os.environ["AGENT"])
out["ifaces"] = sorted(name for _, name in socket.if_nameindex())
try:
    socket.create_connection(("127.0.0.1", int(os.environ["PORT"])), timeout=2).close()
    out["listener"] = "connected"
except OSError as exc:
    out["listener"] = type(exc).__name__
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
    out["work"] = errno.errorcode.get(exc.errno, str(exc.errno))
out["tree"] = open("/work/a.txt").read()
open("/out/outputs.json", "w").write(json.dumps(out))
'''


@unittest.skipUnless(LIVE, "needs user namespaces: run on the host with SSDS_LIVE_SANDBOX=1 (F113's live tests)")
class Live(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.home = DispatcherHome(Path(self._tmp.name) / "home")
        # the canary outside /tmp, which the sandbox replaces with its own tmpfs (review of cc028146): under the
        # real home, in a directory of its own, removed afterwards
        canaries = Path(tempfile.mkdtemp(prefix="ssds-live-canary-", dir=Path.home() / ".cache"))
        self.addCleanup(lambda: __import__("shutil").rmtree(canaries, ignore_errors=True))
        self.canary = canaries / "canary"
        self.canary.write_bytes(b"secret")
        self.workspaces = Workspaces(self.home)
        self.tree = Tree({"a.txt": Entry("100644", b"hello\n"), "probe.py": Entry("100644", PROBE.encode())})

    def run_probe(self) -> dict:
        import socket
        import threading

        agent = os.environ.get("SSH_AUTH_SOCK") or f"/run/user/{os.getuid()}"  # the real agent socket's path
        listener = socket.socket()
        listener.bind(("127.0.0.1", 0))
        listener.listen(1)
        self.addCleanup(listener.close)
        port = listener.getsockname()[1]
        threading.Thread(target=lambda: listener.accept(), daemon=True).start()
        setup = (f"import os; os.environ['CANARY'] = {str(self.canary)!r}; os.environ['AGENT'] = {agent!r}; "
                 f"os.environ['PORT'] = '{port}'; exec(open('/work/probe.py').read())")
        provider = RunnerProvider(argv=("/usr/bin/python3", "-I", "-c", setup))
        ws = self.workspaces.materialize("demo", self.tree)
        found = Sandbox(self.workspaces, (self.home.root,)).execute(ws, self.tree, provider, 60.0)
        self.assertIsNone(found.incomplete, found.detail)
        self.assertTrue(self.canary.exists(), "the canary exists outside")
        self.assertTrue(os.path.exists(agent), f"{agent} exists outside, so its absence inside means something")
        return found.outcome

    def test_the_f2_properties(self) -> None:
        seen = self.run_probe()
        with self.subTest(property="a scrubbed environment"):
            self.assertLessEqual(set(seen["env"]), {"PATH", "HOME", "LANG", "TMPDIR", "PWD", "LC_CTYPE", "CANARY",
                                                    "AGENT", "PORT"})
        with self.subTest(property="its own HOME"):
            self.assertEqual(seen["home"], "/home/runner")
        with self.subTest(property="no agent socket or credentials"):
            self.assertIsNone(seen["ssh"])
            self.assertFalse(seen["agent_path"], "the agent socket's path is absent inside")
        with self.subTest(property="no network"):
            self.assertEqual(seen["ifaces"], ["lo"], "only its own loopback")
            self.assertNotEqual(seen["listener"], "connected", "the host's loopback listener is unreachable")
            self.assertNotEqual(seen["net"], "connected")
        with self.subTest(property="an operator tree unreadable"):
            self.assertNotEqual(seen["canary"], "read")
        with self.subTest(property="the workspace read-only"):
            self.assertEqual(seen["work"], "EROFS")
        self.assertEqual(seen["tree"], "hello\n", "the materialized tree is what runs")

    def test_a_reached_time_bound(self) -> None:
        """The child is gone, not merely reported: it stops ticking once the bound is reached."""

        import time

        provider = RunnerProvider(argv=("/bin/sh", "-c", "while :; do date +%s%N > /out/tick; sleep 0.1; done"))
        ws = self.workspaces.materialize("demo", self.tree)
        found = Sandbox(self.workspaces, (self.home.root,)).execute(ws, self.tree, provider, 1.0)
        self.assertEqual(found.incomplete, "TIME_BOUND")
        tick = ws.root.parent / "out" / "tick"
        self.assertTrue(tick.exists(), "it ran")
        before = tick.read_bytes()
        time.sleep(1.0)
        self.assertEqual(tick.read_bytes(), before, "no process survives the bound")


if __name__ == "__main__":
    unittest.main()
