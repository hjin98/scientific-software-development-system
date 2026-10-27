"""Phase F step 9g-iii: the read-observation flag by hermetic confinement (catalogue §6.3, §6.5, §17.5; SD-80, SD-86;
plan reading F118).

Everything a run inherits from the Executor is either fixed or recorded. Fixed: the ids, the hostname, the
environment, the umask, the signal mask, the soft limits (lowered to a lower host hard limit), the priority and the
personality. Recorded: each bound component's declared identity, ``dev``, ``sandbox``, ``kernel`` (release and
version), ``machine``, ``cpu``, ``cpus``, ``memory``, ``environment``, ``provider``, ``identity`` and ``limits``. A
provider binding a directory it does not declare is held. The fixture policies declaring the flag true, and the
``RERUN`` servable ``ext``-equal, are provisional on Q-F27 (a); no non-fixture policy declares it (plan §6). The live
checks need user namespaces and run on the host with ``SSDS_LIVE_SANDBOX=1``.
"""

from __future__ import annotations

import json
import os
import resource
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from ssds.content import Entry, Tree
from ssds.dispatcher.home import DispatcherHome
from ssds.dispatcher.runner import (ENVIRONMENT, HOSTNAME, RUNNER_GID, RUNNER_UID, UMASK, RunnerProvider, Sandbox,
                                    Workspaces, child_setup, environment_attributes, mount_destinations, run_limits,
                                    run_priority, sandbox_argv)

from . import test_phase_f_step9d_iii as harness
from .test_phase_f_step9f_ii_iii import Fixture

USR = (("/usr", "host-usr"),)
PROVIDER = RunnerProvider(argv=("/bin/true",), components=USR)
NAMES = ("env:/usr", "dev", "sandbox", "kernel", "machine", "cpu", "cpus", "memory", "environment", "provider",
         "identity", "limits")


def attributes(provider: RunnerProvider = PROVIDER) -> dict[str, str]:
    return dict(environment_attributes(provider, "0.6.1-test", run_limits(), run_priority()))


class Fixed(unittest.TestCase):
    def test_the_argv_fixes_ids_hostname_and_environment(self) -> None:
        argv = sandbox_argv(PROVIDER, 3, 4, 5)
        pairs = {argv[i]: argv[i + 1] for i in range(len(argv) - 1) if argv[i] in ("--uid", "--gid", "--hostname")}
        self.assertEqual(pairs, {"--uid": str(RUNNER_UID), "--gid": str(RUNNER_GID), "--hostname": HOSTNAME})
        envs = {argv[i + 1]: argv[i + 2] for i in range(len(argv) - 2) if argv[i] == "--setenv"}
        self.assertEqual(envs, dict(ENVIRONMENT))
        self.assertIn("--clearenv", argv)
        self.assertNotIn(HOSTNAME, mount_destinations(argv), "the flags' values are no mount destinations")
        self.assertNotIn(str(RUNNER_UID), mount_destinations(argv))

    def test_a_soft_limit_lowered_to_a_lower_hard_limit(self) -> None:
        infinity = resource.RLIM_INFINITY
        limits = dict((n, (s, h)) for n, s, h in run_limits(lambda which: (0, 4096)))
        self.assertEqual(limits["RLIMIT_STACK"], (4096, 4096), "8 MiB lowered to the host's hard limit")
        self.assertEqual(limits["RLIMIT_CORE"], (0, 4096))
        self.assertEqual(limits["RLIMIT_AS"], (4096, 4096), "unlimited: the hard limit")
        limits = dict((n, (s, h)) for n, s, h in run_limits(lambda which: (0, infinity)))
        self.assertEqual(limits["RLIMIT_STACK"], (8 << 20, infinity))
        self.assertEqual(limits["RLIMIT_NOFILE"], (1024, infinity))
        self.assertEqual(limits["RLIMIT_CPU"], (infinity, infinity))

    def test_every_platform_limit_is_fixed_or_recorded(self) -> None:
        """Review of a235ad1a, B1: a limit outside the class's list keeps the Executor's values, recorded."""

        numbers = {getattr(resource, n) for n in dir(resource) if n.startswith("RLIMIT_")}
        names = [n for n, _, _ in run_limits()]
        self.assertEqual(sorted(getattr(resource, n) for n in names), sorted(numbers), "each limit once")
        if hasattr(resource, "RLIMIT_OFILE"):
            self.assertIn("RLIMIT_NOFILE", names, "an alias named as the class fixes it")
            self.assertNotIn("RLIMIT_OFILE", names)
        self.assertIn("RLIMIT_SIGPENDING", names)
        limits = dict((n, (s, h)) for n, s, h in run_limits(lambda which: (7, 4096)))
        self.assertEqual(limits["RLIMIT_SIGPENDING"], (7, 4096), "inherited, and recorded")
        self.assertEqual(sorted(json.loads(attributes()["limits"])), sorted(names))

    def test_the_priority_is_never_lowered(self) -> None:
        self.assertEqual(run_priority(lambda which, who: -5), 0, "raised to the class's")
        self.assertEqual(run_priority(lambda which, who: 7), 7, "a higher nice value kept: lowering needs a privilege")

    def test_the_child_starts_with_what_is_recorded(self) -> None:
        """The setup runs in a real child before exec; the child reports what it inherited."""

        probe = ("import json, os, resource, signal; print(json.dumps({'umask': os.umask(0), 'nice': "
                 "os.getpriority(os.PRIO_PROCESS, 0), 'mask': sorted(int(s) for s in signal.pthread_sigmask("
                 "signal.SIG_BLOCK, ())), 'limits': {n: list(resource.getrlimit(getattr(resource, n))) for n in "
                 + repr([n for n, _, _ in run_limits()]) + "}}))")
        limits, nice = run_limits(), run_priority()
        import signal

        old = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGUSR1})  # a blocked signal the child must not keep
        try:
            found = subprocess.run([sys.executable, "-I", "-c", probe], capture_output=True, text=True, check=True,
                                   preexec_fn=child_setup(limits, nice), timeout=60)
        finally:
            signal.pthread_sigmask(signal.SIG_SETMASK, old)
        seen = json.loads(found.stdout)
        self.assertEqual(seen["umask"], UMASK)
        self.assertEqual(seen["nice"], nice)
        self.assertEqual(seen["mask"], [], "no signal blocked")
        self.assertEqual(seen["limits"], {n: [s, h] for n, s, h in limits})
        self.assertEqual(json.loads(attributes()["limits"]), seen["limits"], "the recorded limits are the child's")


    def test_the_spawn_fixes_the_child(self) -> None:
        """The sandbox spawns with the setup, the signals restored and no other descriptor (F118)."""

        from .test_phase_f_step9f_ii_ii import FakeProcess

        seen = {}

        def popen(argv, **kw):
            seen.update(kw)
            return FakeProcess(argv, outputs=b"{\"x\": 1}", **kw)

        with tempfile.TemporaryDirectory() as tmp:
            workspaces = Workspaces(DispatcherHome(Path(tmp) / "home"))
            tree = Tree({"a.txt": Entry("100644", b"x\n")})
            found = Sandbox(workspaces, (), popen=popen).execute(workspaces.materialize("demo", tree), tree,
                                                                 PROVIDER, 10.0)
        self.assertIsNone(found.incomplete, found.detail)
        self.assertTrue(callable(seen.get("preexec_fn")), "the child is set up before it execs")
        self.assertEqual((seen.get("restore_signals"), seen.get("close_fds")), (True, True))
        self.assertEqual(len(seen["pass_fds"]), 3, "the tree, the outputs and the status: nothing else")


class Recorded(unittest.TestCase):
    def test_each_attribute(self) -> None:
        found = attributes()
        self.assertEqual(tuple(found), NAMES)
        self.assertTrue(all(isinstance(v, str) and v for v in found.values()))
        uname = os.uname()
        self.assertEqual(found["env:/usr"], "host-usr", "the provider's declared identity of the component")
        self.assertEqual((found["dev"], found["sandbox"]), ("bwrap-minimal", "0.6.1-test"))
        self.assertEqual(found["kernel"], f"{uname.release} {uname.version}", "release and version (re-check R1)")
        self.assertEqual(found["machine"], uname.machine)
        self.assertEqual(found["cpus"], str(len(os.sched_getaffinity(0))))
        self.assertTrue(found["cpu"].startswith("sha256:") or found["cpu"] == "unknown")
        self.assertEqual(json.loads(found["environment"]), dict(ENVIRONMENT))
        identity = json.loads(found["identity"])
        self.assertEqual((identity["uid"], identity["gid"], identity["hostname"], identity["umask"]),
                         (RUNNER_UID, RUNNER_GID, HOSTNAME, f"{UMASK:04o}"))
        self.assertEqual(identity["capabilities"], [], "recorded empty (re-check of 1e0d5c8a, note 1)")
        self.assertEqual(identity["personality"], 0, "Linux's default: address-space randomization on")
        self.assertEqual(identity["groups"], len(os.getgroups()), "the supplementary groups a run keeps, counted")

    def test_the_provider_identity_distinguishes_providers(self) -> None:
        other = RunnerProvider(argv=("/bin/false",), components=USR)
        renamed = RunnerProvider(argv=("/bin/true",), components=(("/usr", "host-usr-2"),))
        self.assertNotEqual(attributes()["provider"], attributes(other)["provider"])
        self.assertNotEqual(attributes()["provider"], attributes(renamed)["provider"])
        self.assertEqual(attributes()["provider"], attributes(RunnerProvider(argv=("/bin/true",), components=USR))
                         ["provider"])

    def test_the_sandbox_records_the_environment_then_the_providers_own(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            sandbox = Sandbox(Workspaces(DispatcherHome(Path(tmp))), (), version=lambda: "v1")
            provider = RunnerProvider(argv=("/bin/true",), components=USR, attributes=(("regime", "default"),))
            found = sandbox.attributes(provider)
        self.assertEqual([k for k, _ in found], [*NAMES, "regime"])
        self.assertEqual(dict(found)["sandbox"], "v1")


class Undeclared(unittest.TestCase):
    def test_a_provider_binding_an_undeclared_component_never_starts(self) -> None:
        provider = RunnerProvider(argv=("/bin/true",), system=("/usr", "/opt"), components=USR)
        self.assertEqual(provider.undeclared(), ["/opt"])
        with tempfile.TemporaryDirectory() as tmp:
            workspaces = Workspaces(DispatcherHome(Path(tmp) / "home"))
            tree = Tree({"a.txt": Entry("100644", b"x\n")})
            ws = workspaces.materialize("demo", tree)
            sandbox = Sandbox(workspaces, (), popen=lambda *a, **k: self.fail("it ran"))
            found = sandbox.execute(ws, tree, provider, 10.0)
        self.assertEqual(found.incomplete, "FAILED_TO_START")
        self.assertIn("undeclared environment component", found.detail)


class Colliding(unittest.TestCase):
    def test_a_provider_attribute_named_as_the_environments(self) -> None:
        """Review of a235ad1a, note 4: it would override the environment's in an ext comparison."""

        for name in ("cpu", "kernel", "env:/usr"):
            provider = RunnerProvider(argv=("/bin/true",), components=USR, attributes=((name, "mine"),))
            self.assertEqual(provider.undeclared(), [name], name)
        self.assertEqual(RunnerProvider(argv=("/bin/true",), components=USR, attributes=(("regime", "a"),))
                         .undeclared(), [])


class Held(Fixture):
    def test_the_executor_holds_an_undeclared_component(self) -> None:
        ex = self.executor()
        ex.providers = {"ci": RunnerProvider(argv=("/bin/true",), system=("/usr", "/opt"), components=USR)}
        (item,) = [r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE"]
        self.assertIn("undeclared environment component", item.held)


class Pinnable(Fixture):
    """Provisional on Q-F27 (a): the fixture class declares the flag true (plan §6)."""

    def policy(self) -> str:
        names = ", ".join(f'"{n}"' for n in NAMES)
        return super().policy().replace('[runners.ci]\nkind = "DISPATCHER"\n'
                                        f'keys = ["{self.runner.key_id}"]\nattributes = []\n',
                                        '[runners.ci]\nkind = "DISPATCHER"\n'
                                        f'keys = ["{self.runner.key_id}"]\nattributes = [{names}]\n')

    def executor(self, *results, **kw):
        ex = super().executor(*results, **kw)
        recorded = tuple(attributes().items())
        self.fake.attributes = lambda provider: recorded
        return ex

    def test_a_run_recording_every_attribute_is_pinnable(self) -> None:
        from .test_phase_f_step9f_ii_iii import GOOD

        ex = self.executor(GOOD)
        (item,) = [r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE"]
        decision = ex.run(self.derive(), item)
        real = decision.admitted[0]
        basis = self.derive().s.record(real)["fields"]["execution"]
        self.assertEqual([k for k, _ in basis["attributes"]], list(NAMES))
        self.assertFalse(self.derive().a.unpinnable(real), "every class attribute recorded, the flag true")

    def test_a_run_missing_one_is_unpinnable(self) -> None:
        t0 = self.tree("T0")
        partial = [(k, v) for k, v in attributes().items() if k != "cpu"]
        real = self.realize(t0, harness.BAD, pins=(), attributes=partial, class_attributes=NAMES)
        self.assertTrue(self.derive().a.unpinnable(real["id"]), "F90: a class attribute missing")

    def test_a_rerun_now_servable_ext_equal(self) -> None:
        """Provisional on Q-F27 (a)."""

        t0 = self.tree("T0")
        self.fail(self.realize(t0, harness.BAD, pins=(), attributes=list(attributes().items()),
                               class_attributes=NAMES))
        ex = self.executor()
        reruns = [r for r in ex.runs(self.derive()) if r.obligation.kind == "RERUN"]
        self.assertTrue(reruns)
        self.assertTrue(all(r.held is None or "ext-equal" not in r.held for r in reruns), [r.held for r in reruns])
        self.assertTrue(any(r.held is None for r in reruns))


LIVE = os.environ.get("SSDS_LIVE_SANDBOX") == "1"
PROBE = r'''
import json, os, resource, signal, socket
out = {"uid": os.getuid(), "gid": os.getgid(), "hostname": socket.gethostname(), "umask": os.umask(0),
       "nice": os.getpriority(os.PRIO_PROCESS, 0),
       "mask": sorted(int(s) for s in signal.pthread_sigmask(signal.SIG_BLOCK, ())),
       "limits": {n: list(resource.getrlimit(getattr(resource, n))) for n in NAMES}, "groups": len(os.getgroups())}
try:
    os.setuid(0)
    out["setuid"] = "allowed"
except OSError as exc:
    out["setuid"] = type(exc).__name__
try:
    os.chown("/tmp", 0, 0)
    out["chown"] = "allowed"
except OSError as exc:
    out["chown"] = type(exc).__name__
open("/out/outputs.json", "w").write(json.dumps(out))
'''


@unittest.skipUnless(LIVE, "needs user namespaces: run on the host with SSDS_LIVE_SANDBOX=1 (F118's live check)")
class LiveEnvironment(unittest.TestCase):
    def test_what_the_run_sees_is_what_is_recorded(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workspaces = Workspaces(DispatcherHome(Path(tmp) / "home"))
            names = [n for n, _, _ in run_limits()]
            tree = Tree({"probe.py": Entry("100644", PROBE.replace("NAMES", repr(names)).encode())})
            ws = workspaces.materialize("demo", tree)
            provider = RunnerProvider(argv=("/usr/bin/python3", "-I", "/work/probe.py"), components=USR)
            sandbox = Sandbox(workspaces, (Path(tmp),))
            found = sandbox.execute(ws, tree, provider, 60.0)
            recorded = dict(sandbox.attributes(provider))
        self.assertIsNone(found.incomplete, found.detail)
        seen, identity = found.outcome, json.loads(recorded["identity"])
        self.assertEqual((seen["uid"], seen["gid"]), (identity["uid"], identity["gid"]), "the class's ids")
        self.assertEqual(seen["hostname"], identity["hostname"], "the host's hostname never read")
        self.assertEqual(seen["umask"], UMASK)
        self.assertEqual(seen["nice"], identity["nice"])
        self.assertEqual(seen["mask"], [])
        self.assertEqual(seen["limits"], json.loads(recorded["limits"]), "the recorded limits are the run's")
        self.assertEqual(seen["groups"], identity["groups"], "the supplementary group count as recorded")
        self.assertNotEqual(seen["setuid"], "allowed", "no capability kept")
        self.assertNotEqual(seen["chown"], "allowed", "no capability kept")
        self.assertNotEqual(recorded["sandbox"], "unknown", "the package version read on the host")


if __name__ == "__main__":
    unittest.main()
