#!/usr/bin/env python3
"""The product repository's side of the shadow boundary (Phase F step 10d; plan reading F122, F1).

SSDS reads the product repository and writes nothing to it: no ref, no reflog, no object, no worktree or index
change. Around every SSDS command of the real shadow ledger's runbook, the operator takes a snapshot before and
compares after:

    python orchestrator/scripts/shadow_boundary.py snapshot --repository <product> --out <file outside it>
    <the SSDS command>
    python orchestrator/scripts/shadow_boundary.py compare --repository <product> --before <file>

A snapshot holds refs, reflogs, objects and status, plus filesystem fingerprints of every registered worktree
(ignored files included) and Git storage. Symlinks are recorded without following them. Submodules and special
files refuse the comparison. ``compare`` exits 1 on an endpoint difference. A write reverted between snapshots
cannot be excluded by this sensor; the read-only execution paths also need review. Reads may update access times,
which are excluded. Git optional locks are off, so ``status`` never refreshes the index.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import subprocess
import sys
from pathlib import Path

ENV = {**os.environ, "GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"}
SCHEMA = 2


def git(repository: Path, *args: str) -> bytes:
    return subprocess.run(["git", "--no-optional-locks", "-C", str(repository), *args], check=True,
                          capture_output=True, stdin=subprocess.DEVNULL, env=ENV, timeout=600).stdout


def optional(repository: Path, *args: str) -> str | None:
    """A read that may find nothing (an unborn or detached ``HEAD``)."""

    try:
        return git(repository, *args).decode().strip() or None
    except subprocess.CalledProcessError:
        return None


def git_path(repository: Path, *args: str) -> Path:
    path = Path(os.fsdecode(git(repository, "rev-parse", *args).removesuffix(b"\n")))
    return path if path.is_absolute() else (repository / path)


def reflogs(repository: Path) -> dict[str, str]:
    """Every reflog under the repository's Git directories, by its path relative to its ``logs`` directory."""

    out: dict[str, str] = {}
    for label, root in (("common", git_path(repository, "--git-common-dir") / "logs"),
                        ("worktree", git_path(repository, "--git-dir") / "logs")):
        if not root.is_dir():
            continue
        if root.is_symlink():
            raise SystemExit(f"symlink reflog directory is unsupported: {root}")
        for path in sorted(root.rglob("*")):
            if path.is_symlink():
                raise SystemExit(f"symlink reflog is unsupported: {path}")
            if path.is_dir():
                continue
            if not stat.S_ISREG(path.lstat().st_mode):
                raise SystemExit(f"nonregular reflog is unsupported: {path}")
            key = f"{label}:{path.relative_to(root).as_posix()}"
            out[key] = "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
    return out


def worktrees(repository: Path) -> list[Path]:
    """All registered, present worktrees; a missing one cannot be certified unchanged."""

    try:
        inventory = git(repository, "worktree", "list", "--porcelain", "-z")
    except subprocess.CalledProcessError:
        # Older Git emits ambiguous newline-delimited paths. It is safe only without linked worktrees.
        registry = git_path(repository, "--git-common-dir") / "worktrees"
        if registry.exists() or registry.is_symlink():
            raise SystemExit("linked worktree inventory requires Git with worktree list --porcelain -z") from None
        root = git(repository, "rev-parse", "--show-toplevel").removesuffix(b"\n")
        roots = [Path(os.fsdecode(root)).resolve()]
    else:
        roots = [Path(os.fsdecode(row[len(b"worktree "):])).resolve() for row in inventory.split(b"\0")
                 if row.startswith(b"worktree ")]
    if not roots or any(not root.is_dir() for root in roots):
        raise SystemExit("all registered worktrees must be present for a boundary comparison")
    for root in roots:
        if git(root, "rev-parse", "--is-bare-repository").strip() == b"true":
            raise SystemExit("the boundary comparison requires a non-bare product repository")
        if any(row.startswith(b"160000 ") for row in git(root, "ls-files", "--stage", "-z").split(b"\0")):
            raise SystemExit("submodules are unsupported by this boundary comparison; no unchanged claim is available")
    return sorted(set(roots))


def fingerprint(root: Path, *, skip_git: bool = False) -> dict[str, dict]:
    """Filesystem content and write metadata, including ignored files; never follow a symlink.

    Only digests and metadata leave the reader. Special files and concurrent changes refuse the snapshot.
    Access times are omitted because reading files can update them.
    """

    found = {}

    def visit(path: Path) -> None:
        before = path.lstat()
        mode = before.st_mode
        row = {"mode": mode, "device": before.st_dev, "inode": before.st_ino,
               "ctime_ns": before.st_ctime_ns, "mtime_ns": before.st_mtime_ns}
        if stat.S_ISLNK(mode):
            row.update(target=os.readlink(path), mtime_ns=before.st_mtime_ns)
        elif stat.S_ISREG(mode):
            digest = hashlib.sha256()
            fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
            with os.fdopen(fd, "rb") as stream:
                opened = os.fstat(stream.fileno())
                if (opened.st_dev, opened.st_ino) != (before.st_dev, before.st_ino):
                    raise SystemExit(f"changed during snapshot: {path}")
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
            row.update(digest="sha256:" + digest.hexdigest(), size=before.st_size, mtime_ns=before.st_mtime_ns)
        elif stat.S_ISDIR(mode):
            for child in sorted(path.iterdir()):
                if skip_git and path == root and child.name == ".git" and child.is_dir() and not child.is_symlink():
                    continue
                visit(child)
        else:
            raise SystemExit(f"unsupported filesystem entry in boundary snapshot: {path}")
        after = path.lstat()
        if (before.st_dev, before.st_ino, before.st_mode, before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (
                after.st_dev, after.st_ino, after.st_mode, after.st_size, after.st_mtime_ns, after.st_ctime_ns):
            raise SystemExit(f"changed during snapshot: {path}")
        found[path.relative_to(root).as_posix()] = row

    visit(root)
    return found


def snapshot(repository: Path) -> dict:
    roots = worktrees(repository)
    refs = {}
    for line in git(repository, "for-each-ref", "--format=%(refname) %(objectname)").decode().splitlines():
        name, target = line.rsplit(" ", 1)
        refs[name] = target
    objects = sorted(git(repository, "cat-file", "--batch-all-objects", "--batch-check=%(objectname)",
                         "--unordered").decode().split())
    return {
        "schema": SCHEMA,
        "repository": str(repository),
        "head": {"symbolic": optional(repository, "symbolic-ref", "-q", "HEAD"),
                 "commit": optional(repository, "rev-parse", "-q", "--verify", "HEAD^{commit}")},
        "refs": refs,
        "reflogs": reflogs(repository),
        "objects": objects,
        "status": git(repository, "status", "--porcelain=v2", "--branch", "--untracked-files=all").decode(),
        "worktrees": {str(root): fingerprint(root, skip_git=True) for root in roots},
        "git_storage": {str(root): fingerprint(root) for root in sorted({
            git_path(repository, "--git-common-dir").resolve(),
            *(git_path(root, "--git-dir").resolve() for root in roots),
        })},
    }


def differences(before: dict, after: dict) -> list[str]:
    if before.get("schema") != SCHEMA or after.get("schema") != SCHEMA:
        raise SystemExit("boundary snapshot schema changed: take a new snapshot before the command")
    found: list[str] = []
    if before["head"] != after["head"]:
        found.append(f"HEAD: {before['head']} -> {after['head']}")
    for field, label in (("refs", "ref"), ("reflogs", "reflog")):
        for name in sorted(set(before[field]) | set(after[field])):
            old, new = before[field].get(name), after[field].get(name)
            if old != new:
                found.append(f"{label} {name}: {old} -> {new}")
    added = sorted(set(after["objects"]) - set(before["objects"]))
    removed = sorted(set(before["objects"]) - set(after["objects"]))
    if added or removed:
        found.append(f"objects: {len(added)} added {added[:5]}, {len(removed)} removed {removed[:5]}")
    if before["status"] != after["status"]:
        found.append("status:\n--- before\n" + before["status"] + "--- after\n" + after["status"])
    for field in ("worktrees", "git_storage"):
        for root in sorted(set(before[field]) | set(after[field])):
            old, new = before[field].get(root, {}), after[field].get(root, {})
            for path in sorted(set(old) | set(new)):
                if old.get(path) != new.get(path):
                    found.append(f"{field} {root}: {path} changed")
    return found


def outside(repository: Path, path: Path) -> None:
    """The snapshot file lies outside the repository's worktree and Git directory, so writing it changes nothing
    the comparison reads."""

    resolved = path.resolve()
    roots = worktrees(repository)
    for inner in (*roots, git_path(repository, "--git-common-dir").resolve(),
                  *(git_path(root, "--git-dir").resolve() for root in roots)):
        if inner is not None and resolved.is_relative_to(inner):
            raise SystemExit(f"{path} lies inside {inner}: keep the snapshot outside the product repository")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    commands = parser.add_subparsers(dest="command", required=True)
    take = commands.add_parser("snapshot", help="record the repository's refs, reflogs, objects and status")
    take.add_argument("--repository", required=True, type=Path)
    take.add_argument("--out", required=True, type=Path)
    check = commands.add_parser("compare", help="compare a fresh snapshot with an earlier one")
    check.add_argument("--repository", required=True, type=Path)
    check.add_argument("--before", required=True, type=Path)
    args = parser.parse_args(argv)
    repository = args.repository.resolve()
    if args.command == "snapshot":
        outside(repository, args.out)
        args.out.write_text(json.dumps(snapshot(repository), indent=1, sort_keys=True) + "\n")
        print(f"snapshot of {repository} in {args.out}")
        return 0
    before = json.loads(args.before.read_text())
    if before.get("repository") != str(repository):
        raise SystemExit(f"{args.before} is a snapshot of {before.get('repository')}, not {repository}")
    found = differences(before, snapshot(repository))
    for line in found:
        print(line)
    print(f"{repository}: {'CHANGED' if found else 'unchanged'} since {args.before}")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
