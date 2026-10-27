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

import inspect
import os
import secrets
import shutil
import stat
from collections.abc import Mapping
from dataclasses import dataclass
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


__all__ = ["MaterializeRefused", "RUNS", "Workspace", "Workspaces", "reads_as_git"]
