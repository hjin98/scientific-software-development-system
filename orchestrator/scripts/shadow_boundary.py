#!/usr/bin/env python3
"""The product repository's side of the shadow boundary (Phase F step 10d; plan reading F122, F1).

SSDS reads the product repository and writes nothing to it: no ref, no reflog, no object, no worktree or index
change. Around every SSDS command of the real shadow ledger's runbook, the operator takes a snapshot before and
compares after:

    python orchestrator/scripts/shadow_boundary.py snapshot --repository <product> --out <file outside it>
    <the SSDS command>
    python orchestrator/scripts/shadow_boundary.py compare --repository <product> --before <file>

A snapshot holds every ref and its target (``HEAD`` included), the digest of every reflog's bytes, the object set
(loose and packed) and ``git status --porcelain=v2``. ``compare`` takes a fresh snapshot and prints each difference;
any difference exits 1. Every Git call here is a read with optional locks off, so ``status`` never refreshes the
index: the script itself leaves the repository as it found it.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ENV = {**os.environ, "GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"}


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
    path = Path(git(repository, "rev-parse", *args).decode().strip())
    return path if path.is_absolute() else (repository / path)


def reflogs(repository: Path) -> dict[str, str]:
    """Every reflog under the repository's Git directories, by its path relative to its ``logs`` directory."""

    out: dict[str, str] = {}
    for label, root in (("common", git_path(repository, "--git-common-dir") / "logs"),
                        ("worktree", git_path(repository, "--git-dir") / "logs")):
        if not root.is_dir():
            continue
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            key = f"{label}:{path.relative_to(root).as_posix()}"
            out[key] = "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
    return out


def snapshot(repository: Path) -> dict:
    refs = {}
    for line in git(repository, "for-each-ref", "--format=%(refname) %(objectname)").decode().splitlines():
        name, target = line.rsplit(" ", 1)
        refs[name] = target
    objects = sorted(git(repository, "cat-file", "--batch-all-objects", "--batch-check=%(objectname)",
                         "--unordered").decode().split())
    return {
        "repository": str(repository),
        "head": {"symbolic": optional(repository, "symbolic-ref", "-q", "HEAD"),
                 "commit": optional(repository, "rev-parse", "-q", "--verify", "HEAD^{commit}")},
        "refs": refs,
        "reflogs": reflogs(repository),
        "objects": objects,
        "status": git(repository, "status", "--porcelain=v2", "--branch", "--untracked-files=all").decode(),
    }


def differences(before: dict, after: dict) -> list[str]:
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
    return found


def worktree(repository: Path) -> Path | None:
    top = optional(repository, "rev-parse", "--show-toplevel")
    return Path(top).resolve() if top else None


def outside(repository: Path, path: Path) -> None:
    """The snapshot file lies outside the repository's worktree and Git directory, so writing it changes nothing
    the comparison reads."""

    resolved = path.resolve()
    for inner in (worktree(repository), git_path(repository, "--git-common-dir").resolve(),
                  git_path(repository, "--git-dir").resolve()):
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
