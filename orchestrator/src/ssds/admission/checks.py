"""Validation steps 1 and 2 (Manual §8.3; catalogue §8.3, §8.4, §24.1, §25.4): schema, secrets and bounds; reference.

Each check returns reason codes from the closed list of schema version 1 (catalogue §8.4: the members of each ``*``
family are delegated and closed per schema version). Request-level reasons reject the request; record-level
reasons refuse a record, and a never-lost record that passes its own checks is still admitted (step 6).
"""

from __future__ import annotations

import math
import re
from collections import Counter
from collections.abc import Iterator, Mapping
from typing import Any

from ssds.core.api.v1 import canonical_json

from .request import REQUEST_FIELDS

#: The closed reason codes of schema version 1, by step (catalogue §8.4). The ``*`` families' members are fixed
#: here; a needed refusal with no code returns to Stage S (Phase F reading F6).
REASONS = frozenset({
    # step 1
    "SCHEMA_REQUEST", "SCHEMA_RECORD", "SCHEMA_BOUND", "SCHEMA_OBJECT", "SCHEMA_UNSUPPORTED", "SECRET_DETECTED",
    # step 2
    "REF_BASE", "REF_RECORD", "REF_REVISION", "REF_OBLIGATION", "REF_DUPLICATE", "REF_PRODUCING_CONTEXT",
})

#: Input bounds at the Admission boundary (Manual §25.4; the values are delegated, proposed defaults).
MAX_RECORDS = 256
MAX_STRING = 4096
MAX_OBJECT_BYTES = 1 << 20
MAX_REQUEST_BYTES = 8 << 20

#: Known credential forms (§24.1 item 2): provider token formats, private-key headers, connection strings. Policy may
#: extend this list and never shrink it.
CREDENTIAL_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    re.compile(r"\b[a-z][a-z0-9+.-]*://[^\s:/@]+:[^\s@/]+@[^\s/]+"),
)
ENTROPY_BITS = 4.5  # §24.1: [proposed default] Shannon entropy per character
ENTROPY_MIN_LENGTH = 20
_TOKEN = re.compile(r"[A-Za-z0-9+/=_.-]{20,}")
_DIGEST = re.compile(r"sha256:[0-9a-f]{64}")
_HEX = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
#: Fields whose grammar is a digest or an identity, which the entropy check skips (§24.1).
IDENTITY_KEYS = frozenset({"id", "digest", "key_id", "public_key", "signature", "record_id", "request_id"})


def _strings(value: Any, key: str | None = None) -> Iterator[tuple[str | None, str]]:
    if isinstance(value, str):
        yield key, value
    elif isinstance(value, Mapping):
        for k, v in value.items():
            yield from _strings(k, None)
            yield from _strings(v, k if isinstance(k, str) else None)
    elif isinstance(value, list):
        for v in value:
            yield from _strings(v, key)


def _entropy(token: str) -> float:
    counts = Counter(token)
    return -sum(c / len(token) * math.log2(c / len(token)) for c in counts.values())


def secret_detected(value: Any) -> bool:
    """A known credential form anywhere, or a high-entropy token outside a digest or identity field (§24.1)."""

    for key, text in _strings(value):
        if any(p.search(text) for p in CREDENTIAL_PATTERNS):
            return True
        if key in IDENTITY_KEYS:
            continue
        for token in _TOKEN.findall(text):
            if _DIGEST.fullmatch(token) or _HEX.fullmatch(token) or token.startswith("sha256:"):
                continue
            if _entropy(token) >= ENTROPY_BITS:
                return True
    return False


def oversize(value: Any) -> bool:
    return any(len(text) > MAX_STRING for _, text in _strings(value))


def request_problems(request: Any) -> list[str]:
    """Step 1 at the request level: its shape and bounds."""

    if not isinstance(request, Mapping) or set(request) - {"request_id"} != REQUEST_FIELDS:
        return ["SCHEMA_REQUEST"]
    problems = []
    if not isinstance(request["records"], list) or not isinstance(request["claims"], list) \
            or not isinstance(request["candidates"], list) or not isinstance(request["adopted_deltas"], list) \
            or not isinstance(request["objects"], Mapping) or not isinstance(request["base_position"], int) \
            or isinstance(request["base_position"], bool) or not isinstance(request["base_commit"], str):
        return ["SCHEMA_REQUEST"]
    if len(request["records"]) > MAX_RECORDS or len(canonical_json(dict(request))) > MAX_REQUEST_BYTES:
        problems.append("SCHEMA_BOUND")
    for digest, text in request["objects"].items():
        if not isinstance(text, str) or len(text.encode("utf-8")) > MAX_OBJECT_BYTES:
            problems.append("SCHEMA_OBJECT")
        elif secret_detected(text):
            problems.append("SECRET_DETECTED")
    if secret_detected({k: request[k] for k in ("binding", "claims", "adopted_deltas")}):
        problems.append("SECRET_DETECTED")
    return sorted(set(problems))


def record_problems(record: Any, schema_violations) -> list[str]:
    """Step 1 at the record level: the closed schema, bounds and the secret scan."""

    problems = ["SCHEMA_RECORD"] if schema_violations(record) else []
    if oversize(record):
        problems.append("SCHEMA_BOUND")
    if secret_detected(record):
        problems.append("SECRET_DETECTED")
    return problems


def referenced_records(record: Mapping[str, Any]) -> set[str]:
    """Record identities a record names: its record-typed targets, basis entries and supersessions."""

    out = set(record.get("supersedes") or [])
    target = record.get("target")
    if isinstance(target, Mapping):
        for key in ("record", "realization"):
            if isinstance(target.get(key), str) and target[key].startswith("sha256:"):
                out.add(target[key])
        if isinstance(target.get("records"), list):
            out.update(r for r in target["records"] if isinstance(r, str) and r.startswith("sha256:"))
    for entry in record.get("basis") or []:
        if entry.get("mode") in ("record", "standing") or (entry.get("mode") == "identity"
                                                           and isinstance(entry.get("target"), Mapping)
                                                           and "record" in entry["target"]):
            ref = entry["target"].get("record") if isinstance(entry["target"], Mapping) else None
            if isinstance(ref, str):
                out.add(ref)
    return out


def referenced_revisions(record: Mapping[str, Any]) -> set[tuple[str, str]]:
    """``(unit, revision)`` pairs a record's ``content`` and ``validity`` basis entries name."""

    out = set()
    for entry in record.get("basis") or []:
        target = entry.get("target")
        if entry.get("mode") in ("content", "validity") and isinstance(target, Mapping):
            if isinstance(target.get("unit"), str) and isinstance(target.get("rev"), str):
                out.add((target["unit"], target["rev"]))
    return out


__all__ = ["REASONS", "record_problems", "referenced_records", "referenced_revisions", "request_problems",
           "secret_detected"]
