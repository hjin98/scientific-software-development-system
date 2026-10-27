"""The Git-envelope transport (Manual §16.10; catalogue §16.10; Phase F step 8f, reading F70).

For zero-context web agents: an immutable signed task envelope ``task.json`` and the rendered brief ``brief.md`` on an
isolated run ref, ``refs/heads/ssds/run/<task-id>``; the agent writes a result envelope ``result.json`` and its
candidate commits back onto that ref; the result is read by fetching that one ref. Run refs are transport: never
merged, regenerable from the ledger and the obligations.

This module is fitness B1's reserved exception for a writing Git subcommand. It writes only in a scratch repository:
at run time it refuses any repository whose common Git directory is the product repository's, or lies inside the
product's working tree (a repository nested there), and anything that is no repository; the ``GIT_*`` environment is
dropped, so no variable redirects a write, and the scratch's hooks do not run. So no ref, object or file of the
governed repository is ever written (Phase F reading F70; review of 4d949827, notes 1-3).
"""

from __future__ import annotations

import json
import os
import subprocess
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from ssds.core.api.v1 import canonical_json

RUN_REF = "refs/heads/ssds/run/"
_IDENTITY = {"GIT_AUTHOR_NAME": "ssds", "GIT_AUTHOR_EMAIL": "ssds@localhost", "GIT_COMMITTER_NAME": "ssds",
             "GIT_COMMITTER_EMAIL": "ssds@localhost", "GIT_AUTHOR_DATE": "1970-01-01T00:00:00Z",
             "GIT_COMMITTER_DATE": "1970-01-01T00:00:00Z"}


class TransportRefused(RuntimeError):
    """The target repository is the governed product repository, or the run ref is not this task's to write."""


def _git(repo: Path, args: list[str], data: bytes | None = None, check: bool = True) -> subprocess.CompletedProcess:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")} | _IDENTITY
    return subprocess.run(["git", "-C", str(repo), "-c", "core.hooksPath=/dev/null", *args], input=data,
                          capture_output=True, env=env, check=check, timeout=60)


def _common_dir(repo: Path) -> Path:
    found = _git(repo, ["rev-parse", "--path-format=absolute", "--git-common-dir"], check=False)
    if found.returncode != 0:
        raise TransportRefused(f"{repo} is no Git repository")
    return Path(found.stdout.decode().strip()).resolve()


def _top_level(repo: Path) -> Path | None:
    found = _git(repo, ["rev-parse", "--show-toplevel"], check=False)
    return Path(found.stdout.decode().strip()).resolve() if found.returncode == 0 and found.stdout.strip() else None


def run_ref(task_id: str) -> str:
    """The task's run ref, a valid ref name under ``RUN_REF`` (``git check-ref-format``; review of 4d949827, note 6)."""

    ref = RUN_REF + task_id if isinstance(task_id, str) else ""
    if not task_id or "/" in task_id or any(c in task_id for c in " ~^:?*[\\") or ".." in task_id \
            or subprocess.run(["git", "check-ref-format", ref], capture_output=True, timeout=60).returncode != 0:
        raise TransportRefused(f"{task_id!r} is no task id a run ref can name")
    return ref


def _guard(scratch: Path, product: Path) -> None:
    """Refuse the governed product repository, however it is reached (a linked worktree, a path alias, a
    subdirectory), a repository nested in its working tree, and anything that is no repository."""

    common, top = _common_dir(scratch), _top_level(product)
    if common == _common_dir(product) or top is not None and common.is_relative_to(top):
        raise TransportRefused(f"{scratch} is or lies in the product repository: the Git-envelope transport writes "
                               f"only in a scratch repository (reading F70)")


def publish(scratch: Path, product: Path, binding: Mapping[str, Any], brief: bytes) -> str:
    """Write ``task.json`` (the signed binding object: envelope and issue-key signature) and ``brief.md`` on the
    task's run ref in ``scratch``, creating the ref only if absent. Returns the commit."""

    _guard(scratch, product)
    ref = run_ref(binding["envelope"]["task_id"])
    task = canonical_json({"envelope": binding["envelope"], "signature": binding["signature"]})
    blobs = {name: _git(scratch, ["hash-object", "-w", "--stdin"], data).stdout.decode().strip()
             for name, data in (("task.json", task), ("brief.md", brief))}
    listing = "".join(f"100644 blob {sha}\t{name}\n" for name, sha in sorted(blobs.items())).encode()
    tree = _git(scratch, ["mktree"], listing).stdout.decode().strip()
    commit = _git(scratch, ["commit-tree", tree, "-m", f"ssds task {binding['envelope']['task_id']}"]).stdout \
        .decode().strip()
    created = _git(scratch, ["update-ref", ref, commit, ""], check=False)  # create only, whatever the hash function
    if created.returncode != 0:
        if _git(scratch, ["rev-parse", "--verify", "--quiet", ref], check=False).returncode == 0:
            raise TransportRefused(f"{ref} already exists: a task envelope is written once")
        raise TransportRefused(f"{ref} could not be created: {created.stderr.decode(errors='replace').strip()}")
    return commit


def fetch(scratch: Path, product: Path, task_id: str) -> dict[str, Any] | None:
    """The result envelope the agent wrote on the task's run ref, with the commit it sits on, or None. Only this one
    ref is read (polling-first)."""

    _guard(scratch, product)
    ref = run_ref(task_id)
    tip = _git(scratch, ["rev-parse", "--verify", "--quiet", ref], check=False)
    if tip.returncode != 0:
        return None
    commit = tip.stdout.decode().strip()
    shown = _git(scratch, ["cat-file", "-p", f"{commit}:result.json"], check=False)
    if shown.returncode != 0:
        return None
    try:
        result = json.loads(shown.stdout)
    except ValueError:
        return None
    return {"commit": commit, "result": result} if isinstance(result, dict) else None


__all__ = ["RUN_REF", "TransportRefused", "fetch", "publish", "run_ref"]
