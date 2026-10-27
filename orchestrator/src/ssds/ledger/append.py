"""The ledger append API; its only importer is Admission (Manual §26.2; catalogue §21.2-§21.3, §23.3).

An append is a compare-and-swap of the single ledger ref from the expected
previous entry commit, with object and reference fsync requested. The entry
commit's first parent is the previous entry commit and its further parents are
the content commits it newly references, so the ledger keeps them reachable.
Commit metadata is fixed and never read. A checkpoint reaches a file witness
by an exclusive, fsynced write that never overwrites, as does a retirement statement.

Git before 2.36 has no reference fsync setting; on such a host the ref update's
durability rests on the operating system, a limit of the host, not of the rule.
"""

from __future__ import annotations

import os
import secrets
import subprocess
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ssds.core.api.v1 import canonical_json

from .qualification import (RETIREMENT_FILE, Checkpoint, FileWitness, RetirementStatement, checkpoint_body,
                            checkpoint_message, retirement_message, write_all)
from .read import entry_digest, ledger_head, ledger_ref
from .signatures import HostKey, entry_message

_ZERO = "0" * 40
_FIXED_IDENTITY = {
    "GIT_AUTHOR_NAME": "ssds-admission",
    "GIT_AUTHOR_EMAIL": "ssds-admission@invalid",
    "GIT_COMMITTER_NAME": "ssds-admission",
    "GIT_COMMITTER_EMAIL": "ssds-admission@invalid",
    "GIT_AUTHOR_DATE": "1970-01-01T00:00:00Z",
    "GIT_COMMITTER_DATE": "1970-01-01T00:00:00Z",
}
_DURABLE = ["-c", "core.fsyncObjectFiles=true", "-c", "core.fsync=objects,reference", "-c", "core.fsyncMethod=fsync"]


class AppendRefused(RuntimeError):
    """The compare-and-swap lost: the ledger ref moved from the expected entry."""


class AppendFailed(RuntimeError):
    """Git could not perform the append."""


def _environment(extra: Mapping[str, str] | None = None) -> dict[str, str]:
    keep = {name: value for name, value in os.environ.items() if name in ("PATH", "HOME", "SYSTEMROOT")}
    return {**keep, "GIT_TERMINAL_PROMPT": "0", "LC_ALL": "C", "GIT_CONFIG_NOSYSTEM": "1", **(extra or {})}


def _git(repo: Path, args: list[str], data: bytes | None = None, extra: Mapping[str, str] | None = None,
         check: bool = True) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run(  # noqa: S603 - fixed argv
        ["git", *_DURABLE, "-C", str(repo), *args], input=data, capture_output=True, check=False,
        env=_environment(extra),
    )
    if check and result.returncode != 0:
        raise AppendFailed(result.stderr.decode("utf-8", "replace").strip())
    return result


def create_ledger_repository(path: Path) -> Path:
    """A dedicated bare ledger repository (catalogue §21.5 option (ii))."""

    path.mkdir(parents=True, exist_ok=True)
    if not (path / "HEAD").exists():
        _git(path, ["init", "--quiet", "--bare"])
    return path


def import_commits(ledger_repo: Path, source_repo: Path, commits: Sequence[str]) -> None:
    """Copy referenced content commits into a dedicated ledger repository so entries can keep them reachable."""

    missing = [c for c in commits if _git(ledger_repo, ["cat-file", "-e", c + "^{commit}"], check=False).returncode != 0]
    if missing:
        _git(ledger_repo, ["fetch", "--quiet", "--no-tags", str(source_repo), *missing])


def _blob(repo: Path, data: bytes) -> str:
    return _git(repo, ["hash-object", "-w", "--stdin"], data).stdout.decode("ascii").strip()


def _tree(repo: Path, entries: Sequence[tuple[str, str, str]]) -> str:
    listing = "".join(f"{mode} {kind} {oid}\t{name}\0" for mode, kind, oid, name in
                      ((m, "tree" if m == "040000" else "blob", o, n) for m, o, n in sorted(entries, key=lambda e: e[2])))
    return _git(repo, ["mktree", "-z"], listing.encode("utf-8")).stdout.decode("ascii").strip()


@dataclass(frozen=True)
class Appended:
    position: int
    commit: str
    digest: str
    checkpoint: Checkpoint


def seal(entry: Mapping[str, Any], key: HostKey) -> tuple[bytes, bytes, str]:
    """``entry``'s canonical bytes, its host-key signature and its digest: exactly what ``append_entry`` writes, as
    Ed25519 signs deterministically (a trial qualification reads the digest before the append, reading F51)."""

    entry_json = canonical_json(dict(entry))
    signature = key.sign(entry_message(entry_json))
    return entry_json, signature, entry_digest(entry_json, signature)


def append_entry(
    repo: Path,
    entry: Mapping[str, Any],
    key: HostKey,
    expected_head: str | None,
    objects: Mapping[str, bytes] | None = None,
    referenced: Sequence[str] = (),
) -> Appended:
    """Sign and append ``entry`` if the ledger ref is still at ``expected_head``."""

    ledger_id = entry["ledger_id"]
    entry_json, signature, digest = seal(entry, key)
    files = [("100644", _blob(repo, entry_json), "entry.json"), ("100644", _blob(repo, signature), "entry.sig")]
    object_entries = [("100644", _blob(repo, data), f"{digest.removeprefix('sha256:')}.json")
                      for digest, data in sorted((objects or {}).items())]
    if object_entries:
        files.append(("040000", _tree(repo, object_entries), "objects"))
    tree = _tree(repo, files)
    parents = [expected_head] if expected_head else []
    for commit in referenced:
        if commit in parents:
            continue
        if expected_head and _git(repo, ["merge-base", "--is-ancestor", commit, expected_head], check=False).returncode == 0:
            continue
        parents.append(commit)
    message = f"ssds ledger {ledger_id} #{entry['position']}\n".encode("utf-8")
    args = ["commit-tree", tree] + [x for p in parents for x in ("-p", p)]
    commit = _git(repo, args, message, _FIXED_IDENTITY).stdout.decode("ascii").strip()
    result = _git(repo, ["update-ref", ledger_ref(ledger_id), commit, expected_head or _ZERO], check=False)
    if result.returncode != 0:
        if ledger_head(repo, ledger_id) != expected_head:
            raise AppendRefused(f"ledger {ledger_id} moved from {expected_head}")
        raise AppendFailed(result.stderr.decode("utf-8", "replace").strip())
    body = checkpoint_body(ledger_id, entry["position"], digest, commit, key.key_id)
    checkpoint = Checkpoint(**body, signature=key.sign(checkpoint_message(body)).hex())
    return Appended(entry["position"], commit, digest, checkpoint)


def write_checkpoint(witness: FileWitness, checkpoint: Checkpoint) -> None:
    """Durably retain a checkpoint: append-only, complete, fsynced; an existing checkpoint is never replaced.

    The complete checkpoint is written and fsynced in a fresh, exclusively created temporary file, then
    given its name by a hard link, which fails if the name exists, so the name only ever denotes a
    complete checkpoint (Review b341109 A-B13). An existing checkpoint of that name must be this one.
    """

    name = f"{checkpoint.position:012d}-{checkpoint.entry_digest.removeprefix('sha256:')}.json"
    retain(witness.directory(checkpoint.ledger_id), name, canonical_json(checkpoint.to_json()))


def retirement_statement(key: HostKey, ledger_id: str, last: Any) -> RetirementStatement:
    """The statement retiring ``ledger_id`` at ``last``, the chain's ``LINEAGE_RETIREMENT`` entry, signed by the
    Admission host key ``key`` (§24.2; reading F45)."""

    successor = last.lifecycle["fields"]["successor"]
    body = {"ledger_id": ledger_id, "kind": "RETIREMENT", "last_position": last.position,
            "last_entry_digest": last.digest, "successor_ledger_id": successor["ledger_id"],
            "successor_genesis_digest": successor["genesis_digest"]}
    return RetirementStatement(body, ((key.key_id, key.sign(retirement_message(body)).hex()),))


def write_retirement(witness: FileWitness, statement: RetirementStatement) -> None:
    """Durably retain a retirement statement at a file witness, append-only like a checkpoint: a different
    statement already there raises ``AppendFailed``."""

    retain(witness.directory(statement.body["ledger_id"]), RETIREMENT_FILE, canonical_json(statement.to_json()))


def retain(folder: Path, name: str, data: bytes) -> None:
    """Durably retain ``data`` at ``folder/name``, append-only (``write_checkpoint``'s discipline): an existing file
    of that name must hold exactly ``data``."""

    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    temporary = folder / f".{name}.{secrets.token_hex(8)}.tmp"
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)  # a new file only
    try:
        try:
            write_all(descriptor, data)
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        try:
            os.link(temporary, path)
        except FileExistsError:
            if path.is_symlink() or path.read_bytes() != data:
                raise AppendFailed(f"the witness holds a different file at {path}") from None
    finally:
        temporary.unlink(missing_ok=True)
    directory = os.open(folder, os.O_RDONLY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


__all__ = ["AppendFailed", "AppendRefused", "Appended", "HostKey", "append_entry", "create_ledger_repository",
           "import_commits", "retain", "retirement_statement", "seal", "write_checkpoint", "write_retirement"]
