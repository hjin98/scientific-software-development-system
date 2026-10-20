"""Shared fixtures for SSDS tests: in-memory trees with a manifest, and real Git repositories."""

from __future__ import annotations

import os
import subprocess
import textwrap
from pathlib import Path

from ssds.content import DEFAULT_MANIFEST_PATH, Entry, Manifest, Structure, Tree, TreeView, parse_manifest

GIT_ENV = {
    **os.environ,
    "GIT_AUTHOR_NAME": "ssds-test",
    "GIT_AUTHOR_EMAIL": "ssds-test@example.invalid",
    "GIT_COMMITTER_NAME": "ssds-test",
    "GIT_COMMITTER_EMAIL": "ssds-test@example.invalid",
    "GIT_CONFIG_GLOBAL": os.devnull,
    "GIT_CONFIG_SYSTEM": os.devnull,
    "LC_ALL": "C",
}


def manifest(text: str) -> bytes:
    return ("schema = 1\n" + textwrap.dedent(text)).encode("utf-8")


def tree(files: dict[str, bytes | str | Entry], manifest_text: str | None = None) -> Tree:
    entries: dict[str, Entry | bytes] = {}
    for path, value in files.items():
        entries[path] = value.encode("utf-8") if isinstance(value, str) else value
    if manifest_text is not None:
        entries[DEFAULT_MANIFEST_PATH] = manifest(manifest_text)
    return Tree(entries)


def structure_of(t: Tree) -> Structure:
    parsed = parse_manifest(t[DEFAULT_MANIFEST_PATH].data)
    assert isinstance(parsed, Manifest), parsed
    return Structure(parsed.decl)


def view(t: Tree) -> TreeView:
    """The tree under the structure its own manifest declares."""

    return TreeView(t, structure_of(t))


def git(root: Path, *args: str, data: bytes | None = None) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args], input=data, capture_output=True, env=GIT_ENV, check=True
    )
    return result.stdout.decode("utf-8").strip()


def init_repo(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    git(root, "init", "--quiet", "--initial-branch=main")
    return root


def commit(root: Path, message: str = "change") -> str:
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "--allow-empty", "-m", message)
    return git(root, "rev-parse", "HEAD")
