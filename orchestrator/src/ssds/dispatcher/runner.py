"""A designated runner's workspace: an exact tree materialized under ``runs/`` (Manual §1.5, §26.3; Phase F step 9f-i,
readings F2, F104; SD-64 Q-F3).

A workspace is ``<home>/runs/<ledger id>/<run id>/tree``, ``<run id>`` a fresh random token. ``runs/`` is no
operator tree, so ``Home.check`` does not walk it; its containment is this module's. Every directory down to the run
directory is created and opened one component at a time without following a link, and a run directory that already
exists refuses before anything is written. Each tree entry is then written below the workspace through directory
descriptors, never by path, so no entry can redirect a later write:

- a regular file (``0644``) or an executable (``0755``) holds the blob bytes exactly, whatever the umask: no
  end-of-line conversion, filter or smudge, so a CRLF file stays CRLF, an LFS pointer stays the pointer, and a file
  carrying an anchor line keeps it (§1.5's normalization is identity's, never materialization's);
- a symbolic link is created with the blob bytes as its target, never resolved or followed;
- a gitlink is an empty directory, as Git checks out an uninitialized submodule.

A component Git's own path rule reads as ``.git`` is refused, so no workspace is a nested repository; so are
colliding paths and a link target holding a NUL. (A path that is not valid UTF-8 never reaches here: ``Tree``
refuses it.) After writing, the workspace is read back without following a link and compared with the tree entry by
entry; a difference refuses the run. Removal goes through directory descriptors and never descends through a link.
Execution is step 9f-ii's. The tree is the composition root's (``content.read_tree``): this module reads only each
entry's Git mode and bytes, and imports no content model.
"""

from __future__ import annotations

import ctypes
import hashlib
import inspect
import json
import os
import resource
import secrets
import shutil
import signal
import stat
import subprocess
import time
from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ssds.ledger.qualification import HomeRefused, write_all

from .home import DispatcherHome

RUNS = "runs"
#: Code points HFS+ ignores in a name (Git's ``is_hfs_dotgit``), so ``.g‌it`` is ``.git`` there.
_HFS_IGNORABLE = frozenset("‌‍‎‏‪‫‬‭‮"
                           "⁪⁫⁬⁭⁮⁯﻿")
_FILE_MODES = {"100644": 0o644, "100755": 0o755}
LINK, GITLINK = "120000", "160000"


class MaterializeRefused(HomeRefused):
    """The tree cannot be materialized exactly, or the workspace is not what was written."""


def reads_as_git(component: str) -> bool:
    """Git's path rule would read ``component`` as ``.git`` on some filesystem (plan check of ab2a04b9, note 1):
    after HFS+-ignorable code points are removed, an NTFS stream suffix is cut, trailing dots and spaces are stripped
    and the letter case is folded, it is ``.git`` or the 8.3 short name ``git~1``."""

    name = "".join(ch for ch in component if ch not in _HFS_IGNORABLE).split(":", 1)[0].rstrip(". ").casefold()
    return name in (".git", "git~1")


@dataclass(frozen=True)
class Workspace:
    ledger_id: str
    run_id: str
    root: Path  # the materialized tree


class Workspaces:
    def __init__(self, home: DispatcherHome) -> None:
        self.home = home

    def materialize(self, ledger_id: str, tree: Mapping[str, Any]) -> Workspace:
        """Write ``tree`` into a fresh workspace and verify it; a refusal leaves nothing behind it wrote."""

        for path, entry in tree.items():
            _admissible(path, entry)
        self.home.check_ledger_id(ledger_id)
        runs = self.home._directory((RUNS, ledger_id), create=True)
        run_id = secrets.token_hex(16)
        try:
            os.mkdir(run_id, 0o700, dir_fd=runs)  # never an existing directory: FileExistsError refuses
        except FileExistsError:
            os.close(runs)
            raise MaterializeRefused(f"run directory {run_id} already exists") from None
        try:
            run = os.open(run_id, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=runs)
            try:
                os.mkdir("tree", 0o700, dir_fd=run)
                top = os.open("tree", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=run)
                try:
                    for path, entry in tree.items():
                        _write(top, path, entry)
                    found = _read_back(top)
                finally:
                    os.close(top)
            finally:
                os.close(run)
            difference = _difference(tree, found)
            if difference:
                raise MaterializeRefused(f"the workspace is not the tree: {difference}")
        except BaseException as exc:
            failures: list[str] = []
            if shutil.rmtree.avoids_symlink_attacks:
                _rmtree_collecting(run_id, runs, failures)
            else:
                failures.append("this platform cannot remove a tree without following links")
            if failures:  # never silent (review of dad8e4cd, note 3), never masking the refusal
                exc.add_note(f"run directory {run_id} not fully removed: {'; '.join(failures)}")
            raise
        finally:
            os.close(runs)
        return Workspace(ledger_id, run_id, self.home.root / RUNS / ledger_id / run_id / "tree")

    def verify(self, workspace: Workspace, tree: Mapping[str, Any]) -> None:
        """The workspace still holds exactly ``tree`` (the one check 9f-ii's execution relies on)."""

        top = self._tree(workspace)
        try:
            difference = _difference(tree, _read_back(top))
        finally:
            os.close(top)
        if difference:
            raise MaterializeRefused(f"the workspace is not the tree: {difference}")

    def remove(self, workspace: Workspace) -> None:
        """Remove the run directory through descriptors, never descending through a link (F104)."""

        if not shutil.rmtree.avoids_symlink_attacks:
            raise MaterializeRefused("this platform cannot remove a tree without following links")
        runs = self.home._directory((RUNS, workspace.ledger_id), create=False)
        if runs is None:
            return
        try:
            shutil.rmtree(workspace.run_id, dir_fd=runs)
        finally:
            os.close(runs)

    def surviving_outputs(self, ledger_id: str, run_id: str) -> bytes | None:
        """A crashed run's ``outputs.json``, read through descriptors with ``_outputs``'s rules, or ``None``."""

        out = self.home._directory((RUNS, ledger_id, run_id, "out"), create=False)
        if out is None:
            return None
        try:
            return _outputs(out)
        finally:
            os.close(out)

    def remove_run(self, ledger_id: str, run_id: str) -> None:
        self.remove(Workspace(ledger_id, run_id, self.home.root / RUNS / ledger_id / run_id / "tree"))

    def _tree(self, workspace: Workspace) -> int:
        runs = self.home._directory((RUNS, workspace.ledger_id, workspace.run_id, "tree"), create=False)
        if runs is None:
            raise MaterializeRefused(f"no workspace for run {workspace.run_id}")
        return runs


def _rmtree_collecting(name: str, directory: int, failures: list[str]) -> None:
    """``rmtree`` through a descriptor, each failure collected: ``onexc`` where this Python has it (3.12 onward),
    ``onerror`` on 3.11, which the project supports (re-check of 088ed1bf, B2)."""

    if "onexc" in inspect.signature(shutil.rmtree).parameters:
        shutil.rmtree(name, dir_fd=directory, onexc=lambda _f, path, error: failures.append(f"{path}: {error}"))
    else:
        shutil.rmtree(name, dir_fd=directory, onerror=lambda _f, path, info: failures.append(f"{path}: {info[1]}"))


def _admissible(path: str, entry: Any) -> None:
    # containment is this module's whatever mapping it is handed (review of dad8e4cd, B1): a relative path of
    # named components only, as ``content.check_path`` requires of a Tree
    if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path or "\0" in path \
            or any(part in ("", ".", "..") for part in path.split("/")):
        raise MaterializeRefused(f"{path!r} is not a relative path of named components")
    if any(reads_as_git(part) for part in path.split("/")):
        raise MaterializeRefused(f"{path!r} names a .git component; a workspace is no repository")
    if entry.mode not in (*_FILE_MODES, LINK, GITLINK):
        raise MaterializeRefused(f"{path!r} has no Git entry mode a workspace holds ({entry.mode!r})")
    if entry.mode == LINK and b"\0" in entry.data:
        raise MaterializeRefused(f"{path!r} is a link whose target holds a NUL byte")


def _write(top: int, path: str, entry: Any) -> None:
    *parents, name = path.split("/")
    directory = os.dup(top)
    try:
        for part in parents:
            try:
                os.mkdir(part, 0o700, dir_fd=directory)
            except FileExistsError:
                pass
            try:
                inner = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=directory)
            except OSError as exc:
                raise MaterializeRefused(f"{path!r} collides with another entry ({exc.strerror})") from None
            os.close(directory)
            directory = inner
        try:
            if entry.mode in _FILE_MODES:
                descriptor = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600,
                                     dir_fd=directory)
                try:
                    write_all(descriptor, entry.data)
                    os.fchmod(descriptor, _FILE_MODES[entry.mode])  # the umask never applies
                finally:
                    os.close(descriptor)
            elif entry.mode == LINK:
                os.symlink(entry.data, os.fsencode(name), dir_fd=directory)
            else:  # a gitlink: Git's uninitialized submodule
                os.mkdir(name, 0o755, dir_fd=directory)
        except FileExistsError:
            raise MaterializeRefused(f"{path!r} collides with another entry") from None
    finally:
        os.close(directory)


def _read_back(top: int) -> dict[str, tuple[str, bytes]]:
    """Every file, link and empty directory under ``top``: ``path -> (kind, bytes)``, never following a link."""

    found: dict[str, tuple[str, bytes]] = {}
    pending: list[tuple[str, int]] = [("", os.dup(top))]
    while pending:
        prefix, directory = pending.pop()
        try:
            names = sorted(os.listdir(directory))
            if not names and prefix:
                found[prefix[:-1]] = ("empty", b"")
            for name in names:
                path = prefix + name
                info = os.lstat(name, dir_fd=directory)
                if stat.S_ISLNK(info.st_mode):
                    found[path] = ("120000", os.readlink(os.fsencode(name), dir_fd=directory))
                elif stat.S_ISDIR(info.st_mode):
                    inner = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=directory)
                    pending.append((path + "/", inner))
                elif stat.S_ISREG(info.st_mode):
                    mode = {0o644: "100644", 0o755: "100755"}.get(stat.S_IMODE(info.st_mode), oct(info.st_mode))
                    # a file swapped for a FIFO never blocks the read, and the one opened is the one examined
                    # (review of dad8e4cd, note 1); a second name would share the inode outside (note 2)
                    try:
                        descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory)
                    except OSError:  # swapped for a socket or removed since it was examined (re-check of 088ed1bf)
                        found[path] = ("replaced", b"")
                        continue
                    with os.fdopen(descriptor, "rb") as handle:
                        opened = os.fstat(handle.fileno())
                        if (opened.st_ino, opened.st_dev) != (info.st_ino, info.st_dev) \
                                or not stat.S_ISREG(opened.st_mode):
                            found[path] = ("replaced", b"")
                        elif opened.st_nlink != 1:
                            found[path] = ("linked", b"")
                        else:
                            found[path] = (mode, handle.read())
                else:
                    found[path] = (oct(info.st_mode), b"")
        finally:
            os.close(directory)
    return found


def _difference(tree: Mapping[str, Any], found: dict[str, tuple[str, bytes]]) -> str | None:
    """The first way ``found`` is not ``tree``: the same paths, a gitlink as an empty directory, each mode and each
    file's or link's bytes; ``None`` when they agree."""

    expected = {path: ("empty", b"") if entry.mode == GITLINK else (entry.mode, entry.data)
                for path, entry in tree.items()}
    for path in sorted(set(expected) | set(found)):
        if path not in found:
            return f"{path!r} is missing"
        if path not in expected:
            return f"{path!r} is not in the tree"
        if found[path] != expected[path]:
            return f"{path!r} differs ({found[path][0]} for {expected[path][0]})"
    return None


# -- execution in the sandbox (step 9f-ii-ii; reading F113) ---------------------------------------------------------

#: The sandbox's fixed places: the workspace, read-only; the one writable directory; a home of its own.
WORK, OUT, RUNNER_HOME = "/work", "/out", "/home/runner"
OUTPUTS = "outputs.json"
#: An outcome object larger than this is no outcome (§25.4: readers are total over untrusted input).
MAX_OUTPUT_BYTES = 1 << 20
_MERGED_USR = (("usr/bin", "/bin"), ("usr/lib", "/lib"), ("usr/lib64", "/lib64"), ("usr/sbin", "/sbin"))


@dataclass(frozen=True)
class RunnerProvider:
    """What a designated runner class runs (F113; Manual §26.3's runner provider contract, re-exported by
    ``ssds.spi.v1``): the argv inside the sandbox, run in ``/work``; the system directories bound read-only at their
    own paths, each with its declared identity in ``components`` (F118: a directory bound without one is an
    undeclared environment component, and the run is held); the execution attributes it records beyond the
    environment's; and the output convention, ``/out/outputs.json``. It writes only to ``/tmp`` or ``/out``: the
    tree is read-only."""

    argv: tuple[str, ...]
    system: tuple[str, ...] = ("/usr",)
    attributes: tuple[tuple[str, str], ...] = ()
    components: tuple[tuple[str, str], ...] = ()

    def undeclared(self) -> list[str]:
        """The bound directories with no declared identity (F118), and the provider's own attributes named as an
        environment attribute, which would override it in an ``ext`` comparison (review of a235ad1a, note 4)."""

        declared = dict(self.components)
        return [d for d in self.system if not declared.get(d)] \
            + [name for name, _ in self.attributes if name in ENVIRONMENT_ATTRIBUTES or name.startswith("env:")]


@dataclass(frozen=True)
class Execution:
    """One execution's result: the outcome object read from ``/out`` (or ``None``), the ``INCOMPLETE`` reason
    (or ``None`` when complete) and the exit status, which never decides admissibility (§17.2)."""

    outcome: dict[str, Any] | None
    incomplete: str | None
    exit_status: int | None = None
    detail: str = ""
    raw: bytes | None = field(default=None, repr=False)  # a surviving outcome's bytes, kept for the owner


# -- the confined environment (step 9g-iii; reading F118) ----------------------------------------------------------
#
# Everything the process inherits from the Executor is either fixed here or recorded as an execution attribute
# (re-check of fdfd99c9, R1). Fixed: the user and group ids, the hostname, the environment, the umask, the signal
# mask and dispositions (``restore_signals``), the descriptors (only those bound), the soft resource limits, the
# scheduling priority (never lowered below the Executor's, which needs a privilege) and the personality (Linux's
# default, address-space randomization on). Recorded: each bound component's declared identity, ``/dev``, the
# sandbox's version, the kernel, the architecture, the processor, the usable processors, the memory, the fixed
# environment, the provider, the identity (with the supplementary group count, which an unprivileged user namespace
# cannot clear) and every resource limit the platform defines (review of a235ad1a, B1). Unrecorded and disclosed
# (§6.5): ``/dev/urandom``, address-space randomization, wall-clock time (Q-F27), a host quota the process cannot read,
# its ``oom_score_adj``, the operator's process count ``RLIMIT_NPROC`` counts, and the processor's microcode and other
# cores; the quota-like ones can only make a run fail.

RUNNER_UID = RUNNER_GID = 1000
HOSTNAME = "ssds-runner"
UMASK = 0o022
NICE = 0
ENVIRONMENT = (("PATH", "/usr/bin:/bin"), ("HOME", RUNNER_HOME), ("LANG", "C.UTF-8"), ("TMPDIR", "/tmp"))
#: The soft limits a run starts with (``None``: unlimited), each lowered to the host's hard limit where that is
#: lower; the hard limits are the host's, recorded. Every other limit the platform defines keeps the Executor's
#: values and is recorded (review of a235ad1a, B1).
LIMITS = (("RLIMIT_STACK", 8 << 20), ("RLIMIT_NOFILE", 1024), ("RLIMIT_AS", None), ("RLIMIT_CORE", 0),
          ("RLIMIT_NPROC", None), ("RLIMIT_FSIZE", None), ("RLIMIT_CPU", None), ("RLIMIT_DATA", None),
          ("RLIMIT_MEMLOCK", 64 << 10))
#: ``personality(2)``'s ``PER_LINUX``: no flag set, so address-space randomization is on.
PER_LINUX = 0
#: The attributes the environment records beside each ``env:<path>``; a provider's own may not reuse them.
ENVIRONMENT_ATTRIBUTES = frozenset({"dev", "sandbox", "kernel", "machine", "cpu", "cpus", "memory", "environment",
                                    "provider", "identity", "limits"})


def platform_limits() -> tuple[str, ...]:
    """Every resource limit the platform defines, each once by name: an alias (``RLIMIT_OFILE`` of
    ``RLIMIT_NOFILE``) is the class's name for it where the class fixes it, else the first."""

    by_number: dict[int, list[str]] = {}
    for name in sorted(dir(resource)):
        if name.startswith("RLIMIT_") and isinstance(getattr(resource, name), int):
            by_number.setdefault(getattr(resource, name), []).append(name)
    fixed = dict(LIMITS)
    return tuple(sorted(next((n for n in names if n in fixed), names[0]) for names in by_number.values()))


def run_limits(getrlimit: Callable[[int], tuple[int, int]] = resource.getrlimit) -> tuple[tuple[str, int, int], ...]:
    """Each limit the platform defines as ``(name, soft, hard)``: a class limit's soft value lowered to the host's
    hard limit, any other the Executor's own (F118)."""

    infinity, fixed = resource.RLIM_INFINITY, dict(LIMITS)
    out = []
    for name in platform_limits():
        soft, hard = getrlimit(getattr(resource, name))
        if name in fixed:
            wanted = fixed[name]
            soft = hard if wanted is None else wanted if hard == infinity else min(wanted, hard)
        out.append((name, soft, hard))
    return tuple(out)


def run_priority(getpriority: Callable[[int, int], int] = os.getpriority) -> int:
    """The scheduling priority a run starts with: the class's, unless the Executor's is lower (a higher nice value),
    which only a privilege could undo."""

    return max(NICE, getpriority(os.PRIO_PROCESS, 0))


def _personality() -> Callable[[int], int]:
    libc = ctypes.CDLL(None, use_errno=True)
    libc.personality.argtypes, libc.personality.restype = [ctypes.c_ulong], ctypes.c_int
    return libc.personality


def child_setup(limits: tuple[tuple[str, int, int], ...], nice: int) -> Callable[[], None]:
    """What the spawned child fixes before it execs ``bwrap`` (F118). Everything it calls is resolved here, before the
    fork; the Executor runs one execution at a time, so no lock is held across it."""

    personality = _personality()
    settings = [(getattr(resource, name), soft, hard) for name, soft, hard in limits]

    def setup() -> None:
        signal.pthread_sigmask(signal.SIG_SETMASK, ())
        os.umask(UMASK)
        for which, soft, hard in settings:
            resource.setrlimit(which, (soft, hard))
        os.setpriority(os.PRIO_PROCESS, 0, nice)
        if personality(PER_LINUX) == -1:
            raise OSError(ctypes.get_errno(), "personality")

    return setup


def _cpu_identity() -> str:
    """The processor's model and features, as a digest of the first processor's ``/proc/cpuinfo`` lines that name
    them, read by the Executor on the host (the sandbox mounts no ``/proc``)."""

    keys = ("vendor_id", "cpu family", "model", "model name", "stepping", "flags", "Features", "CPU implementer",
            "CPU architecture", "CPU variant", "CPU part")
    try:
        text = Path("/proc/cpuinfo").read_text(errors="replace")
    except OSError:
        return "unknown"
    first = text.split("\n\n", 1)[0]
    lines = sorted(line.split(":", 1)[0].strip() + ":" + line.split(":", 1)[1].strip()
                   for line in first.splitlines() if ":" in line and line.split(":", 1)[0].strip() in keys)
    return "sha256:" + hashlib.sha256("\n".join(lines).encode()).hexdigest()


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def bubblewrap_version() -> str:
    """The host's ``bubblewrap`` package version (SD-86), or ``unknown``."""

    try:
        found = subprocess.run(["dpkg-query", "-W", "-f=${Version}", "bubblewrap"], capture_output=True, text=True,
                               timeout=30, check=False)
    except (OSError, subprocess.SubprocessError):
        return "unknown"
    return found.stdout.strip() if found.returncode == 0 and found.stdout.strip() else "unknown"


def environment_attributes(provider: RunnerProvider, version: str, limits: tuple[tuple[str, int, int], ...],
                           nice: int) -> tuple[tuple[str, str], ...]:
    """The execution attributes a run in this sandbox records (F118), each ``[name, value]`` with a string value."""

    uname = os.uname()
    declared = dict(provider.components)
    identity = {"uid": RUNNER_UID, "gid": RUNNER_GID, "hostname": HOSTNAME, "umask": f"{UMASK:04o}", "nice": nice,
                "personality": PER_LINUX, "capabilities": [],  # bwrap keeps none in its user namespace
                "groups": len(os.getgroups())}  # kept, unmapped: setgroups is denied (review of a235ad1a, B1)
    shown = {"argv": list(provider.argv), "system": list(provider.system),
             "components": sorted(map(list, declared.items()))}
    return (*((f"env:{d}", declared[d]) for d in provider.system),
            ("dev", "bwrap-minimal"), ("sandbox", version), ("kernel", f"{uname.release} {uname.version}"),
            ("machine", uname.machine), ("cpu", _cpu_identity()), ("cpus", str(len(os.sched_getaffinity(0)))),
            ("memory", str(os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES"))),
            ("environment", _canonical(dict(ENVIRONMENT))),
            ("provider", "sha256:" + hashlib.sha256(_canonical(shown).encode()).hexdigest()),
            ("identity", _canonical(identity)), ("limits", _canonical({n: [s, h] for n, s, h in limits})))


def sandbox_argv(provider: RunnerProvider, tree_fd: int, out_fd: int, status_fd: int,
                 bwrap: str = "/usr/bin/bwrap") -> list[str]:
    """The ``bwrap`` command on an allowlisted root (F113). Every mount destination sits on bwrap's own tmpfs root
    and none lies beneath the workspace, the design rule the host package's dropped link-resolution fix requires
    (Q-F26). The user's home, the SSDS home and ``/run`` are never bound; ``/proc`` and ``/sys`` are not mounted;
    ``--unshare-all`` leaves no network. The ids and the hostname are the class's (F118)."""

    argv = [bwrap, "--unshare-all", "--die-with-parent", "--new-session", "--clearenv",
            "--uid", str(RUNNER_UID), "--gid", str(RUNNER_GID), "--hostname", HOSTNAME]
    for name, value in ENVIRONMENT:
        argv += ["--setenv", name, value]
    argv += ["--json-status-fd", str(status_fd)]
    for directory in provider.system:
        argv += ["--ro-bind", directory, directory]
    for target, link in _MERGED_USR:
        argv += ["--symlink", target, link]
    argv += ["--ro-bind-fd", str(tree_fd), WORK, "--bind-fd", str(out_fd), OUT, "--tmpfs", "/tmp", "--tmpfs", RUNNER_HOME,
             "--dev", "/dev", "--chdir", WORK, "--", *provider.argv]
    return argv


def mount_destinations(argv: list[str]) -> list[str]:
    """Every mount destination a ``sandbox_argv`` names, for the design rule's check."""

    takes_two = {"--ro-bind", "--bind", "--symlink", "--setenv"}
    out, i = [], 1
    while i < len(argv) and argv[i] != "--":
        flag = argv[i]
        if flag in ("--ro-bind", "--bind", "--symlink", "--ro-bind-fd", "--bind-fd"):
            out.append(argv[i + 2])
        if flag in ("--tmpfs", "--dev"):
            out.append(argv[i + 1])
        i += 3 if flag in takes_two | {"--ro-bind-fd", "--bind-fd"} else 2 if flag in ("--tmpfs", "--dev", "--chdir",
                                                                          "--json-status-fd", "--uid", "--gid",
                                                                          "--hostname") else 1
    return out


def refused_sources(provider: RunnerProvider, forbidden: tuple[Path, ...]) -> list[str]:
    """The provider's bound directories that resolve inside a forbidden tree: the SSDS home or the product repository
    (F113's check before spawning; the workspace itself is bound by descriptor, never by path)."""

    # F113's never-bound list, whatever the caller passes (review of cc028146, note 1): the user's home, and /run,
    # where the SSH agent and D-Bus sockets live
    forbidden = (*forbidden, Path.home(), Path("/run"), Path("/var/run"))
    out = []
    for directory in provider.system:
        resolved = Path(directory).resolve()
        if not Path(directory).is_absolute() or any(resolved == f.resolve() or resolved.is_relative_to(f.resolve())
                                                    or f.resolve().is_relative_to(resolved) for f in forbidden):
            out.append(directory)
    return out


class Sandbox:
    """Runs a provider over a verified workspace under ``bwrap`` (F113). The workspace is verified through the
    descriptor that is bound, immediately before execution, and re-verified after it exits (review of dad8e4cd,
    note 4). Time runs on the injected monotonic ``clock`` from the spawn; reaching the bound kills the sandbox's
    process group. ``popen`` is injected for tests."""

    def __init__(self, workspaces: Workspaces, forbidden: tuple[Path, ...], *, bwrap: str = "/usr/bin/bwrap",
                 clock: Callable[[], float] = time.monotonic, popen: Callable[..., Any] = subprocess.Popen,
                 poll_seconds: float = 0.05, version: Callable[[], str] = bubblewrap_version) -> None:
        self.workspaces, self.forbidden, self.bwrap = workspaces, forbidden, bwrap
        self.clock, self.popen, self.poll_seconds = clock, popen, poll_seconds
        self._version, self._read_version = None, version

    @property
    def version(self) -> str:
        if self._version is None:
            self._version = self._read_version()
        return self._version

    def attributes(self, provider: RunnerProvider) -> tuple[tuple[str, str], ...]:
        """What a run of ``provider`` here records: the environment's attributes, then the provider's own (F118)."""

        return (*environment_attributes(provider, self.version, run_limits(), run_priority()), *provider.attributes)

    def execute(self, workspace: Workspace, tree: Mapping[str, Any], provider: RunnerProvider,
                bound_seconds: float) -> Execution:
        refused = refused_sources(provider, self.forbidden)
        if refused:
            return Execution(None, "FAILED_TO_START", detail=f"bound sources inside a forbidden tree: {refused}")
        if provider.undeclared():
            return Execution(None, "FAILED_TO_START",
                             detail=f"an undeclared environment component: {provider.undeclared()} (F118)")
        try:
            top = self.workspaces._tree(workspace)
        except HomeRefused as exc:
            return Execution(None, "FAILED_TO_START", detail=str(exc))
        try:
            difference = _difference(tree, _read_back(top))
            if difference:  # verified through the descriptor that is bound, immediately before execution
                return Execution(None, "FAILED_TO_START", detail=f"the workspace is not the tree: {difference}")
            try:
                out = self._out(workspace)
            except MaterializeRefused as exc:
                return Execution(None, "FAILED_TO_START", detail=str(exc))
            try:
                return self._run(top, out, tree, provider, bound_seconds)
            finally:
                os.close(out)
        finally:
            os.close(top)

    def _run(self, top: int, out: int, tree: Mapping[str, Any], provider: RunnerProvider,
             bound_seconds: float) -> Execution:
        read_status, write_status = os.pipe()
        try:
            try:
                argv = sandbox_argv(provider, top, out, write_status, self.bwrap)
                try:
                    # what the run inherits is fixed in the child before it execs (F118); recorded by attributes()
                    setup = child_setup(run_limits(), run_priority())
                    process = self.popen(argv, pass_fds=(top, out, write_status), start_new_session=True,
                                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                         stderr=subprocess.DEVNULL, close_fds=True, restore_signals=True,
                                         preexec_fn=setup)
                except OSError as exc:
                    return Execution(None, "FAILED_TO_START", detail=f"the sandbox could not start: {exc}")
            finally:
                os.close(write_status)
            try:
                timed_out = self._wait(process, bound_seconds)
            except BaseException:  # an interrupted wait leaves no sandbox behind (review of cc028146, note 4)
                _kill(process)
                raise
            status = _status(read_status)
        finally:
            os.close(read_status)  # every path, a failed spawn included (note 4)
        exit_status = process.returncode
        if "child-pid" not in status:
            return Execution(None, "FAILED_TO_START", exit_status, "the sandbox could not be set up")
        raw = _outputs(out)
        if timed_out:
            return Execution(None, "TIME_BOUND", exit_status, raw=raw)
        after = _difference(tree, _read_back(top))
        if after:
            return Execution(None, "CRASHED", exit_status, f"the workspace changed: {after}", raw=raw)
        if raw is None:
            if exit_status is not None and exit_status < 0:
                return Execution(None, "CRASHED", exit_status, "ended by a signal with no outputs")
            return Execution(None, "MALFORMED_OUTPUT", exit_status, "no outputs")
        try:
            outcome = json.loads(raw)
        except (ValueError, UnicodeDecodeError):
            return Execution(None, "MALFORMED_OUTPUT", exit_status, "outputs are not JSON", raw=raw)
        if not isinstance(outcome, dict):
            return Execution(None, "MALFORMED_OUTPUT", exit_status, "outputs are not an object", raw=raw)
        return Execution(outcome, None, exit_status, raw=raw)  # the exit status decides nothing (§17.2)

    def _out(self, workspace: Workspace) -> int:
        run = self.workspaces.home._directory((RUNS, workspace.ledger_id, workspace.run_id), create=False)
        if run is None:
            raise MaterializeRefused(f"no run directory for {workspace.run_id}")
        try:
            try:
                os.mkdir("out", 0o700, dir_fd=run)  # one execution per workspace: no earlier outputs survive
            except FileExistsError:
                raise MaterializeRefused(f"run {workspace.run_id} has executed already") from None
            # bound by its descriptor, as /work is (review of cc028146, note 2)
            return os.open("out", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=run)
        finally:
            os.close(run)

    def _wait(self, process: Any, bound_seconds: float) -> bool:
        """Waits for the sandbox; on reaching the bound kills its process group and reports it."""

        started = self.clock()
        while process.poll() is None:
            if self.clock() - started >= bound_seconds:
                _kill(process)
                return True
            time.sleep(self.poll_seconds)
        return False


def _kill(process: Any) -> None:
    """Kills the sandbox's process group; ``--die-with-parent`` takes its pid namespace with it."""

    try:
        os.killpg(process.pid, signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        pass
    process.wait()


def _status(descriptor: int) -> dict[str, Any]:
    """bwrap's JSON status lines, merged; empty when it could not set the sandbox up."""

    data = b""
    while len(data) < 1 << 16:  # read to end of file; the caller owns and closes the descriptor
        chunk = os.read(descriptor, 1 << 16)
        if not chunk:
            break
        data += chunk
    out: dict[str, Any] = {}
    for line in data.splitlines():
        try:
            item = json.loads(line)
        except ValueError:
            continue
        if isinstance(item, dict):
            out.update(item)
    return out


def _outputs(out: int) -> bytes | None:
    """``/out/outputs.json``'s bytes, read through ``/out``'s descriptor without following a link and capped, or
    ``None``. Everything else in ``/out`` is the sandboxed code's and hostile (review of cc028146, note 5)."""

    try:
        descriptor = os.open(OUTPUTS, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=out)
    except OSError:
        return None
    with os.fdopen(descriptor, "rb") as handle:
        if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
            return None
        data = handle.read(MAX_OUTPUT_BYTES + 1)
    return data if len(data) <= MAX_OUTPUT_BYTES else None


__all__ = ["ENVIRONMENT", "Execution", "HOSTNAME", "LIMITS", "MaterializeRefused", "OUT", "RUNNER_GID", "RUNNER_UID",
           "RUNS", "RunnerProvider", "Sandbox", "UMASK", "WORK", "Workspace", "Workspaces", "bubblewrap_version",
           "child_setup", "environment_attributes", "mount_destinations", "reads_as_git", "refused_sources",
           "run_limits", "run_priority", "sandbox_argv"]
