"""Phase F step 9f-ii-ii: the sandbox, without a live namespace (catalogue §17.2; plan §3.6, readings F2, F113).

The ``bwrap`` command is built on an allowlisted root: every mount destination on bwrap's tmpfs root, none beneath
the workspace (Q-F26's design rule), no home, ``/run``, ``/proc`` or ``/sys``, no network. A provider binding a
directory inside the SSDS home or the product repository never starts. With ``popen`` injected: the exit status never
decides admissibility; no outputs is ``MALFORMED_OUTPUT``, or ``CRASHED`` after a signal; a sandbox that cannot be set
up is ``FAILED_TO_START``; reaching the bound is ``TIME_BOUND``; a workspace changed before execution never runs, and
one changed during it is ``CRASHED``. The live properties are ``test_phase_f_step9f_ii_ii_live``'s, run on the host.
Expected values are from §17.2 and F113.
"""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from ssds.content import Entry, Tree
from ssds.dispatcher import runner
from ssds.dispatcher.home import DispatcherHome
from ssds.dispatcher.runner import (OUT, WORK, RunnerProvider, Sandbox, Workspaces, mount_destinations,
                                    refused_sources, sandbox_argv)

TREE = Tree({"a.py": Entry("100644", b"v = 1\n"), "run.sh": Entry("100755", b"#!/bin/sh\n")})
PROVIDER = RunnerProvider(argv=("/bin/sh", "run.sh"), components=(("/usr", "host-usr"),))


class Argv(unittest.TestCase):
    def setUp(self) -> None:
        self.argv = sandbox_argv(PROVIDER, 7, 8, 9)

    def test_an_allowlisted_root(self) -> None:
        for flag in ("--unshare-all", "--die-with-parent", "--new-session", "--clearenv"):
            self.assertIn(flag, self.argv)
        self.assertEqual(self.argv[self.argv.index("--ro-bind-fd") + 1:self.argv.index("--ro-bind-fd") + 3], ["7", WORK])
        self.assertEqual(self.argv[self.argv.index("--bind-fd") + 1:self.argv.index("--bind-fd") + 3], ["8", OUT],
                         "/out by its descriptor too (review of cc028146, note 2)")
        self.assertEqual(self.argv[self.argv.index("--") + 1:], list(PROVIDER.argv))

    def test_the_design_rule_no_destination_beneath_the_workspace(self) -> None:
        """Q-F26, F113: every destination absolute on bwrap's root, nothing mounted under ``/work``."""

        destinations = mount_destinations(self.argv)
        self.assertIn(WORK, destinations)
        self.assertIn(OUT, destinations)
        self.assertTrue(all(d.startswith("/") for d in destinations), destinations)
        self.assertFalse([d for d in destinations if d != WORK and (d + "/").startswith(WORK + "/")])

    def test_nothing_of_the_operator_is_bound(self) -> None:
        destinations = mount_destinations(self.argv)
        for absent in ("/proc", "/sys", "/run", str(Path.home()), "/home"):
            self.assertNotIn(absent, destinations)
        self.assertFalse(any(a == "--share-net" for a in self.argv), "no network")
        sources = [self.argv[i + 1] for i, a in enumerate(self.argv) if a in ("--ro-bind", "--bind")]
        self.assertEqual(sources, list(PROVIDER.system), "only the provider's system bound by path")

    def test_a_provider_binding_a_forbidden_tree_never_starts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / "home"
            home.mkdir()
            inside = RunnerProvider(argv=("true",), system=("/usr", str(home / "keys")))
            self.assertEqual(refused_sources(inside, (home,)), [str(home / "keys")])
            self.assertEqual(refused_sources(RunnerProvider(argv=("true",), system=("/",)), (home,)), ["/"],
                             "a directory holding the home binds it")
            self.assertEqual(refused_sources(PROVIDER, (home,)), [])
            for never in (str(Path.home()), "/run/user", "/var/run"):  # whatever the caller passes (note 1)
                self.assertEqual(refused_sources(RunnerProvider(argv=("true",), system=(never,)), ()), [never])


class FakeProcess:
    """A sandbox run by ``popen``'s stand-in: it writes bwrap's status and the provider's outputs."""

    def __init__(self, argv, *, status=True, outputs=None, returncode=0, run=None, never_ends=False, **_):
        self.pid = 12345
        status_fd = int(argv[argv.index("--json-status-fd") + 1])
        out = int(argv[argv.index("--bind-fd") + 1])
        if status:
            os.write(status_fd, json.dumps({"child-pid": 1}).encode() + b"\n")
        if outputs is not None:
            descriptor = os.open(runner.OUTPUTS, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600, dir_fd=out)
            os.write(descriptor, outputs)
            os.close(descriptor)
        if run is not None:
            run()
        self.returncode = None if never_ends else returncode
        self._final = returncode

    def poll(self):
        return self.returncode

    def wait(self):
        self.returncode = -9
        return self.returncode


class Executions(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.home = DispatcherHome(Path(self._tmp.name) / "home")
        self.workspaces = Workspaces(self.home)
        self.ws = self.workspaces.materialize("demo", TREE)

    def execute(self, bound=10.0, clock=None, **fake):
        self.ws = self.workspaces.materialize("demo", TREE)  # one execution per workspace
        sandbox = Sandbox(self.workspaces, (self.home.root,), popen=lambda argv, **kw: FakeProcess(argv, **fake),
                          clock=clock or (lambda: 0.0), poll_seconds=0)
        return sandbox.execute(self.ws, TREE, PROVIDER, bound)

    def test_a_workspace_executes_once(self) -> None:
        self.execute(outputs=b"{}")
        again = Sandbox(self.workspaces, (self.home.root,), popen=lambda argv, **kw: self.fail("it ran"))
        self.assertEqual(again.execute(self.ws, TREE, PROVIDER, 10.0).incomplete, "FAILED_TO_START",
                         "no earlier outputs can be read as this run's")

    def test_the_exit_status_never_decides(self) -> None:
        """§17.2: a nonzero exit with good outputs is complete; a zero exit with none is not."""

        done = self.execute(outputs=b'{"x": 1}', returncode=3)
        self.assertEqual((done.outcome, done.incomplete, done.exit_status), ({"x": 1}, None, 3))
        self.assertEqual(self.execute(returncode=0).incomplete, "MALFORMED_OUTPUT")

    def test_outputs_that_are_no_object(self) -> None:
        too_big = b'{"x": "' + b"a" * runner.MAX_OUTPUT_BYTES + b'"}'  # a valid object, over the cap (§25.4)
        for raw in (b"not json", b"[1]", too_big):
            with self.subTest(raw=raw[:8]):
                self.assertEqual(self.execute(outputs=raw).incomplete, "MALFORMED_OUTPUT")

    def test_a_signal_with_no_outputs_crashed(self) -> None:
        self.assertEqual(self.execute(returncode=-11).incomplete, "CRASHED")

    def test_a_sandbox_that_cannot_be_set_up(self) -> None:
        self.assertEqual(self.execute(status=False, returncode=1).incomplete, "FAILED_TO_START")
        sandbox = Sandbox(self.workspaces, (self.home.root,), bwrap="/nonexistent/bwrap")
        found = sandbox.execute(self.ws, TREE, PROVIDER, 10.0)
        self.assertEqual((found.incomplete, found.outcome), ("FAILED_TO_START", None), "never retried unsandboxed")

    def test_reaching_the_bound(self) -> None:
        times = iter([0.0, 5.0, 11.0, 12.0])
        with mock.patch.object(runner.os, "killpg") as kill:
            found = self.execute(bound=10.0, clock=lambda: next(times), never_ends=True)
        self.assertEqual(found.incomplete, "TIME_BOUND")
        kill.assert_called_once()

    def test_a_workspace_changed_before_or_during_execution(self) -> None:
        def change() -> None:
            os.chmod(self.ws.root / "a.py", 0o600)

        self.assertEqual(self.execute(outputs=b"{}", run=change).incomplete, "CRASHED", "changed during it")
        # (the stand-in reads self.ws as execute sets it, before the sandbox runs)
        fresh = self.workspaces.materialize("demo", TREE)
        (fresh.root / "a.py").chmod(0o600)
        sandbox = Sandbox(self.workspaces, (self.home.root,), popen=lambda argv, **kw: self.fail("it ran"))
        self.assertEqual(sandbox.execute(fresh, TREE, PROVIDER, 10.0).incomplete, "FAILED_TO_START")

    def test_no_descriptor_survives_a_failed_spawn(self) -> None:
        """Review of cc028146, note 4: the status pipe and the bound directories are closed on every path."""

        def opened() -> int:
            return len(os.listdir("/proc/self/fd")) if os.path.isdir("/proc/self/fd") else -1

        sandbox = Sandbox(self.workspaces, (self.home.root,), bwrap="/nonexistent/bwrap")
        ws = self.workspaces.materialize("demo", TREE)
        before = opened()
        self.assertEqual(sandbox.execute(ws, TREE, PROVIDER, 10.0).incomplete, "FAILED_TO_START")
        self.assertEqual(opened(), before)

    def test_an_interrupted_wait_kills_the_sandbox(self) -> None:
        def interrupted(*_):
            raise KeyboardInterrupt

        sandbox = Sandbox(self.workspaces, (self.home.root,), popen=lambda argv, **kw: FakeProcess(argv, never_ends=True),
                          poll_seconds=0)
        ws = self.workspaces.materialize("demo", TREE)
        with mock.patch.object(Sandbox, "_wait", interrupted), mock.patch.object(runner.os, "killpg") as kill, \
                self.assertRaises(KeyboardInterrupt):
            sandbox.execute(ws, TREE, PROVIDER, 10.0)
        kill.assert_called_once()

    def test_a_forbidden_source_never_starts(self) -> None:
        provider = RunnerProvider(argv=("true",), system=("/usr", str(self.home.root)))
        sandbox = Sandbox(self.workspaces, (self.home.root,), popen=lambda argv, **kw: self.fail("it ran"))
        self.assertEqual(sandbox.execute(self.ws, TREE, provider, 10.0).incomplete, "FAILED_TO_START")


if __name__ == "__main__":
    unittest.main()
