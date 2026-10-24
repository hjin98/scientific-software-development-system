"""The Ledger Store read API: the closed schema, chain reading and verification (catalogue §3, §5.7, §21.2, §23.2).

``read_chain`` returns the authenticated chain of a ledger. A chain with a
missing or invalid signature, a key not in force or a ``prev`` mismatch is
rejected (:class:`ChainRejected`); derivation never sees it. An authenticated
entry that violates the closed schema, the entry tree layout or the agreement
of the Git commit chain puts that position and every later one into
``INTEGRITY_HALT``. An entry of an unreadable schema version ends current
assertion without being corruption.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ssds.core.api.v1 import canonical_json

from .schema import (
    CHALLENGE_TIER,
    KINDS,
    LIFECYCLE_TIER,
    OBSERVATION_TIER,
    RECOVERY_LIFECYCLE,
    SCHEMA_VERSION,
    SUPPORT_TIER,
    SYSTEM_RULESET,
    SchemaViolation,
    entry_violations,
    is_commit,
    is_digest,
    is_token,
    record_id,
    record_violations,
    is_unit,
    tier,
    with_id,
)
from .signatures import entry_message, human_key_id, verify_host, verify_sshsig  # noqa: F401 - authentication API

LEDGER_REF_PREFIX = "refs/ssds/ledger/"
_OBJECT_PATH = re.compile(r"^objects/([0-9a-f]{64})\.json$")


class ChainRejected(ValueError):
    """An unauthenticated chain: derivation never runs over it."""


@dataclass(frozen=True)
class RawEntry:
    """One entry commit as stored: its parents and the files of its tree."""

    commit: str
    parents: tuple[str, ...]
    files: Mapping[str, bytes]


@dataclass(frozen=True)
class LedgerEntry:
    position: int
    commit: str
    parents: tuple[str, ...]
    entry: dict[str, Any]
    entry_json: bytes
    signature: bytes
    digest: str
    objects: Mapping[str, bytes]

    @property
    def records(self) -> list[dict[str, Any]]:
        records = self.entry.get("records")
        return list(records) if isinstance(records, list) else []

    @property
    def lifecycle(self) -> dict[str, Any] | None:
        lifecycle = self.entry.get("lifecycle")
        return lifecycle if isinstance(lifecycle, dict) else None


@dataclass(frozen=True)
class Chain:
    ledger_id: str
    entries: tuple[LedgerEntry, ...]  # every authenticated entry, in position order
    halt: int | None = None  # INTEGRITY_HALT from this position
    halt_reasons: tuple[str, ...] = ()
    unreadable: int | None = None  # an unreadable schema version from this position

    @property
    def readable_through(self) -> int:
        """The last position derivation may read: before a halt or an unreadable entry."""

        stops = [p for p in (self.halt, self.unreadable) if p is not None]
        return (min(stops) if stops else len(self.entries)) - 1

    @property
    def genesis(self) -> dict[str, Any] | None:
        if not self.entries or self.readable_through < 0:
            return None
        return self.entries[0].lifecycle

    def digests(self) -> list[str]:
        return [e.digest for e in self.entries]


def entry_digest(entry_json: bytes, signature: bytes) -> str:
    return "sha256:" + hashlib.sha256(entry_json + signature).hexdigest()


def ledger_ref(ledger_id: str) -> str:
    return LEDGER_REF_PREFIX + ledger_id


def _keys_in_force(chain_so_far: Sequence[LedgerEntry]) -> tuple[dict[str, str], dict[str, int]]:
    """Admission host keys in force after the given entries, and compromise positions.

    Every action names its key by ``key.id`` and a rotation names the key it replaces by ``key.retires``, as for
    every role (Review e6ac009 B6); a stored value this reader cannot read changes no key rather than raising.
    """

    keys: dict[str, str] = {}
    compromised: dict[str, int] = {}
    for item in chain_so_far:
        lifecycle = item.lifecycle
        fields = lifecycle.get("fields") if isinstance(lifecycle, Mapping) else None
        if not isinstance(fields, Mapping):
            continue
        if lifecycle.get("kind") == "GENESIS":
            roots = fields.get("trust_roots")
            for key in (roots.get("admission_keys") if isinstance(roots, Mapping) else None) or []:
                if isinstance(key, Mapping) and isinstance(key.get("id"), str) and isinstance(key.get("public_key"), str):
                    keys[key["id"]] = key["public_key"]
            continue
        key, action = fields.get("key"), fields.get("action")
        if lifecycle.get("kind") != "KEY_LIFECYCLE" or not isinstance(key, Mapping) or key.get("role") != "ADMISSION" \
                or not isinstance(key.get("id"), str):
            continue
        if action in ("REGISTER", "ROTATE") and isinstance(key.get("public_key"), str):
            keys[key["id"]] = key["public_key"]
        old = key["id"] if action == "RETIRE" else key.get("retires") if action == "ROTATE" else None
        if isinstance(old, str):
            keys.pop(old, None)
        if action == "COMPROMISED":
            start = fields.get("from_position", item.position)
            start = start if isinstance(start, int) and not isinstance(start, bool) else 0
            compromised[key["id"]] = min(start, compromised.get(key["id"], start))  # never relaxed
    return keys, compromised


def _genesis_keys(raw: RawEntry) -> dict[str, str]:
    try:
        entry = json.loads(raw.files["entry.json"])
        roots = entry["lifecycle"]["fields"]["trust_roots"]
        return {k["id"]: k["public_key"] for k in roots.get("admission_keys", [])}
    except (KeyError, TypeError, ValueError):
        return {}


def verify_chain(ledger_id: str, raws: Sequence[RawEntry]) -> Chain:
    """Verify stored entries in position order (first parent first)."""

    accepted: list[LedgerEntry] = []
    halt: int | None = None
    halt_reasons: tuple[str, ...] = ()
    unreadable: int | None = None
    previous_digest: str | None = None
    previous_commit: str | None = None
    for position, raw in enumerate(raws):
        entry_json = raw.files.get("entry.json")
        signature = raw.files.get("entry.sig")
        if entry_json is None or signature is None:
            raise ChainRejected(f"position {position}: entry or signature missing")
        try:
            entry = json.loads(entry_json)
        except ValueError:
            raise ChainRejected(f"position {position}: entry is not JSON") from None
        if not isinstance(entry, dict):
            raise ChainRejected(f"position {position}: entry is not an object")
        trusted = accepted if halt is None else accepted[:halt]
        keys, compromised = _keys_in_force(trusted) if trusted else (_genesis_keys(raw), {})
        key_id = entry.get("host_key_id")
        if key_id not in keys:
            raise ChainRejected(f"position {position}: key not in force")
        if not verify_host(keys[key_id], entry_message(entry_json), signature):
            raise ChainRejected(f"position {position}: invalid signature")
        if entry.get("prev") != previous_digest:
            raise ChainRejected(f"position {position}: prev does not name the previous entry")
        digest = entry_digest(entry_json, signature)
        objects = {}
        layout_ok = True
        for path, data in raw.files.items():
            if path in ("entry.json", "entry.sig"):
                continue
            match = _OBJECT_PATH.match(path)
            if not match or hashlib.sha256(data).hexdigest() != match.group(1):
                layout_ok = False
            else:
                objects["sha256:" + match.group(1)] = data
        item = LedgerEntry(position, raw.commit, raw.parents, entry, entry_json, signature, digest, objects)
        accepted.append(item)
        previous_digest, prev_commit_was = digest, previous_commit
        previous_commit = raw.commit
        if halt is not None or unreadable is not None:
            continue
        problems = entry_violations(entry)
        if problems == ["UNREADABLE_SCHEMA"]:
            unreadable = position
            continue
        if canonical_json(entry) != entry_json:
            problems.append("entry.json is not canonical")
        if entry.get("ledger_id") != ledger_id or entry.get("position") != position:
            problems.append("ledger id or position does not match the chain")
        if not layout_ok:
            problems.append("the entry tree holds files outside its layout")
        if position > 0 and (not raw.parents or raw.parents[0] != prev_commit_was):
            problems.append("the Git commit chain disagrees with the prev chain")
        if key_id in compromised and position >= compromised[key_id]:
            problems.append("signed by a key declared compromised")
        records = list(entry.get("records", [])) if isinstance(entry.get("records"), list) else []
        if isinstance(entry.get("lifecycle"), dict):
            records.append(entry["lifecycle"])
        for record in records:
            problems.extend(f"record: {p}" for p in record_violations(record))
        if problems:
            halt, halt_reasons = position, tuple(problems)
    return Chain(ledger_id, tuple(accepted), halt, halt_reasons, unreadable)


# -- the Git store ------------------------------------------------------------------------


def _environment() -> dict[str, str]:
    keep = {name: value for name, value in os.environ.items() if name in ("PATH", "HOME", "SYSTEMROOT")}
    return {**keep, "GIT_TERMINAL_PROMPT": "0", "LC_ALL": "C", "GIT_CONFIG_NOSYSTEM": "1"}


def _git(repo: Path, args: list[str], data: bytes | None = None, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run(  # noqa: S603 - fixed argv
        ["git", "-C", str(repo), *args], input=data, capture_output=True, check=False, env=_environment()
    )
    if check and result.returncode != 0:
        raise ChainRejected(result.stderr.decode("utf-8", "replace").strip())
    return result


def ledger_head(repo: Path, ledger_id: str) -> str | None:
    """The authoritative replica's ledger ref, or None when it does not exist."""

    result = _git(repo, ["rev-parse", "--verify", "--quiet", ledger_ref(ledger_id) + "^{commit}"], check=False)
    return result.stdout.decode("ascii").strip() if result.returncode == 0 else None


def read_raw(repo: Path, head: str) -> list[RawEntry]:
    """The entry chain ending at ``head``, oldest first: each entry's first parent until the genesis entry."""

    raws: list[RawEntry] = []
    commit: str | None = head
    while commit is not None:
        header = _git(repo, ["cat-file", "commit", commit]).stdout.decode("utf-8", "replace")
        parents = tuple(line.split()[1] for line in header.split("\n\n", 1)[0].splitlines() if line.startswith("parent "))
        tree = _git(repo, ["ls-tree", "-r", "-z", commit]).stdout
        files = {}
        for item in tree.split(b"\0"):
            if not item:
                continue
            meta, _, path = item.partition(b"\t")
            oid = meta.split(b" ")[2].decode("ascii")
            files[path.decode("utf-8")] = _git(repo, ["cat-file", "blob", oid]).stdout
        raws.append(RawEntry(commit, parents, files))
        try:
            position = json.loads(files.get("entry.json", b"{}")).get("position")
        except ValueError:
            position = None
        if position == 0 or not parents or len(raws) > 10_000_000:
            break
        commit = parents[0]
    raws.reverse()
    return raws


def read_chain(repo: Path, ledger_id: str, head: str | None = None) -> Chain:
    """The verified chain of ``ledger_id`` in ``repo``, at ``head`` or at the ledger ref."""

    head = head or ledger_head(repo, ledger_id)
    if head is None:
        return Chain(ledger_id, ())
    return verify_chain(ledger_id, read_raw(repo, head))


@dataclass(frozen=True)
class RecordIndex:
    """Every record of the readable prefix, with the position that admitted it."""

    records: dict[str, dict[str, Any]] = field(default_factory=dict)
    position: dict[str, int] = field(default_factory=dict)


def index_records(chain: Chain, through: int | None = None) -> RecordIndex:
    last = chain.readable_through if through is None else min(through, chain.readable_through)
    index = RecordIndex()
    for entry in chain.entries[: last + 1]:
        carried = list(entry.records)
        if entry.lifecycle is not None:
            carried.append(entry.lifecycle)
        for record in carried:
            index.records[record["id"]] = record
            index.position[record["id"]] = entry.position
    return index


__all__ = [
    "CHALLENGE_TIER", "Chain", "ChainRejected", "KINDS", "LEDGER_REF_PREFIX", "LIFECYCLE_TIER", "LedgerEntry",
    "OBSERVATION_TIER", "RECOVERY_LIFECYCLE", "RawEntry", "RecordIndex", "SCHEMA_VERSION", "SUPPORT_TIER",
    "SYSTEM_RULESET", "SchemaViolation", "entry_digest", "entry_violations", "human_key_id", "is_commit", "is_digest", "is_token", "index_records",
    "is_unit", "ledger_head", "ledger_ref", "read_chain", "read_raw", "record_id", "record_violations", "tier",
    "verify_chain", "verify_sshsig", "with_id",
]
