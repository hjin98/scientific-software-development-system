"""Read a commit's tree from a Git repository, exactly as Git stores it (Manual §1.5).

Only object identities are accepted, never ref names, so nothing read through
the Content Model depends on where a live ref points. Reading uses ``ls-tree``
and ``cat-file --batch``, which apply no attribute, filter or line-ending
conversion.
"""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

from .tree import Entry, Tree

_OBJECT_ID = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")


class GitReadError(RuntimeError):
    """The repository could not supply the requested objects."""


def _environment() -> dict[str, str]:
    keep = {name: value for name, value in os.environ.items() if name in ("PATH", "HOME", "SYSTEMROOT")}
    return {**keep, "GIT_TERMINAL_PROMPT": "0", "LC_ALL": "C", "GIT_CONFIG_NOSYSTEM": "1"}


def _git(repo: Path, args: list[str], data: bytes | None = None) -> bytes:
    result = subprocess.run(  # noqa: S603 - fixed argv
        ["git", "-C", str(repo), *args],
        input=data,
        capture_output=True,
        check=False,
        env=_environment(),
    )
    if result.returncode != 0:
        raise GitReadError(result.stderr.decode("utf-8", "replace").strip())
    return result.stdout


def read_tree(repo: Path, commit: str) -> Tree:
    """The tree of ``commit`` (a full object identity) in ``repo``."""

    if not _OBJECT_ID.match(commit):
        raise ValueError("read_tree takes a full object identity, never a ref name")
    listing = _git(repo, ["ls-tree", "-r", "-z", "--full-tree", commit])
    records = []
    for item in listing.split(b"\0"):
        if not item:
            continue
        meta, _, raw_path = item.partition(b"\t")
        mode, kind, oid = meta.decode("ascii").split(" ")
        records.append((raw_path.decode("utf-8"), mode, kind, oid))
    blobs = [oid for _, _, kind, oid in records if kind == "blob"]
    contents = _cat_blobs(repo, blobs)
    entries = {}
    for path, mode, kind, oid in records:
        if kind == "commit":
            entries[path] = Entry("160000", oid.encode("ascii"))
        else:
            entries[path] = Entry(mode, contents[oid])
    return Tree(entries)


def _cat_blobs(repo: Path, oids: list[str]) -> dict[str, bytes]:
    unique = sorted(set(oids))
    if not unique:
        return {}
    out = _git(repo, ["cat-file", "--batch"], ("\n".join(unique) + "\n").encode("ascii"))
    contents: dict[str, bytes] = {}
    position = 0
    for oid in unique:
        header_end = out.index(b"\n", position)
        name, kind, size = out[position:header_end].decode("ascii").split(" ")
        if name != oid or kind != "blob":
            raise GitReadError(f"unexpected object {name} {kind}")
        start = header_end + 1
        contents[oid] = out[start : start + int(size)]
        position = start + int(size) + 1
    return contents
