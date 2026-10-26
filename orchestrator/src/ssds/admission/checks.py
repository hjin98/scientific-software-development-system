"""Validation steps 1 and 2 (Manual §8.3; catalogue §8.3, §8.4, §24.1, §25.4): schema, secrets and bounds; reference.

Each check returns reason codes from the closed list of schema version 1 (catalogue §8.4: the members of each ``*``
family are delegated and closed per schema version). Request-level reasons reject the request; record-level
reasons refuse a record, and a never-lost record that passes its own checks is still admitted (step 6). Every
record is checked on its own, whatever the request's other faults, so salvage never admits an unchecked record.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections import Counter
from collections.abc import Iterable, Iterator, Mapping
from typing import Any

from ssds.core.api.v1 import canonical_json
from ssds.ledger.read import is_commit, is_digest, is_token, record_id, submits

from .request import REQUEST_FIELDS

#: The closed reason codes of schema version 1, by step (catalogue §8.4). The ``*`` families' members are fixed
#: here; a needed refusal with no code returns to Stage S (Phase F reading F6).
REASONS = frozenset({
    # step 1
    "SCHEMA_REQUEST", "SCHEMA_RECORD", "SCHEMA_BOUND", "SCHEMA_OBJECT", "SCHEMA_UNSUPPORTED", "SECRET_DETECTED",
    # step 2
    "REF_BASE", "REF_RECORD", "REF_REVISION", "REF_OBJECT", "REF_OBLIGATION", "REF_DUPLICATE",
    "REF_PRODUCING_CONTEXT", "REF_TRANSFORMATION", "REF_DELTA", "REF_ADOPTION",
    # step 3: authentication and authorization (Phase F steps 3-4)
    "AUTH_ENVELOPE", "AUTH_ACTOR", "AUTH_VERSION", "AUTH_ROLE_KIND", "AUTH_TARGET_PART", "AUTH_TARGET_REVOKED",
    "AUTH_ILL_FORMED", "AUTH_TARGET_NOT_CURRENT", "AUTH_TARGET_NOT_EFFECTIVE", "AUTH_SUPERSEDES",
    "AUTH_WRITE_SCOPE", "AUTH_PROTECTED",
    # step 4, structure (Phase F step 4c): STRUCT_<code> for each §1.9 static check and STRUCT_TERM_UNRESOLVED,
    # STRUCT_RESERVED_LEAF, STRUCT_MODE_MIXED, STRUCT_REVALIDATE, STRUCT_SDG_*, STRUCT_ILLEGAL_CYCLE,
    # STRUCT_SINGLE_DEFINER and STRUCT_MANIFEST_UNPARSED (reading F15); RELATION_<code> for each S0 relation defect
    "STRUCT_MERGE_CONFLICT", "FREEZE_SOURCE", "FREEZE_DESTINATION", "ENACTMENT_MISSING",
    # step 5's checks other than cycles (SD-68), realized by Phase F step 4d
    "DEP_TARGET_ORDER", "DEP_TARGET_KIND", "DEP_COUNTER_CHALLENGE", "DEP_OWN_SUBJECT", "DEP_CONSUMER",
    "CYCLE_SUPPORT", "CYCLE_WARRANT", "STALE_BASIS",  # CYCLE_WARRANT is not emitted until Stage S defines it (reading F25)
    # step 7, legality (Phase F step 5; the delegated OBLIGATION_* members named by reading F34, Stage S notes)
    "OBLIGATION_NOT_DERIVED", "OBLIGATION_RESULT_DUPLICATE", "OBLIGATION_DISCHARGED", "OBLIGATION_CONTRACT_STALE",
    "OBLIGATION_PREDICATE_UNMET", "OBLIGATION_CLAIM_UNSUPPORTED", "OBLIGATION_REENACTED", "OBLIGATION_ANSWERED",
    "OBLIGATION_REVIEW_OPEN", "OBLIGATION_PARTITION_INVALID", "STALE_RETAINED", "CONFORMANCE_RESULT", "NOT_SETTLED",
    # step 8 and step 9
    "REGRESSION", "HEAD_MOVED",
})

#: The codes that refuse an integration on its candidate's merits (reading F35): a rejection carrying only these
#: names ``X``, so the item takes a new iteration (``Items.refused``). A rejection for anything else leaves the
#: candidate pending: a binding, an unbuilt check, a moved head, a freeze (the head's state, lifted when its challenge
#: is resolved) or a missing enactment acceptance (the review route's, recorded in ``X``'s frame; review 87b4fa8 B1).
MERIT_PREFIXES = ("STRUCT_", "RELATION_", "CONFORMANCE_")
MERIT_CODES = frozenset({"AUTH_WRITE_SCOPE", "AUTH_PROTECTED", "CYCLE_SUPPORT", "CYCLE_WARRANT", "STALE_RETAINED",
                         "OBLIGATION_REENACTED", "REGRESSION"})


def on_merits(reasons: Iterable[str]) -> bool:
    """Whether a rejection's reasons all judge the candidate itself (reading F35)."""

    reasons = set(reasons)
    return bool(reasons) and all(r in MERIT_CODES or r.startswith(MERIT_PREFIXES) for r in reasons)

#: Input bounds at the Admission boundary (Manual §25.4; the values are delegated, proposed defaults).
MAX_RECORDS = 256
MAX_STRING = 4096
MAX_OBJECT_BYTES = 1 << 20
MAX_REQUEST_BYTES = 8 << 20
MAX_DEPTH = 64

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
#: §24.1 [proposed default]: Shannon entropy of at least 4.5 bits per character over any token of at least 20
#: characters. A token of n characters cannot exceed log2(n) bits per character, so the threshold detects little
#: below about 30 characters; recalibrating it is policy's (the step 2 review's note).
ENTROPY_BITS = 4.5
_TOKEN = re.compile(r"[A-Za-z0-9+/=_.-]{20,}")
#: The digest and identity grammars the entropy check exempts (§24.1 "outside fields whose grammar is a digest or
#: identity"): by the value's grammar, never by the key it sits under.
_EXEMPT = (re.compile(r"sha256:[0-9a-f]{64}"), re.compile(r"[0-9a-f]{40}"), re.compile(r"[0-9a-f]{64}"))
#: Whole values whose grammar is an identity or a signature, never a secret: a human actor's key fingerprint
#: (§25.1), a key id, and an armoured SSH signature (the human authentication of §25.1).
_IDENTITY_VALUES = (
    re.compile(r"human:SHA256:[A-Za-z0-9+/]{43}"),
    re.compile(r"ed25519:[0-9a-f]{64}"),
    re.compile(r"-----BEGIN SSH SIGNATURE-----\n[A-Za-z0-9+/=\n]+-----END SSH SIGNATURE-----\n?"),
)


def _strings(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, Mapping):
        for k, v in value.items():
            yield from _strings(k)
            yield from _strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from _strings(v)


def _entropy(token: str) -> float:
    counts = Counter(token)
    return -sum(c / len(token) * math.log2(c / len(token)) for c in counts.values())


def secret_detected(value: Any) -> bool:
    """A known credential form anywhere, or a high-entropy token whose grammar is not a digest or identity."""

    for text in _strings(value):
        if any(p.search(text) for p in CREDENTIAL_PATTERNS):
            return True
        if any(p.fullmatch(text) for p in _IDENTITY_VALUES):
            continue
        for token in _TOKEN.findall(text):
            if any(p.fullmatch(token) for p in _EXEMPT):
                continue
            if _entropy(token) >= ENTROPY_BITS:
                return True
    return False


def oversize(value: Any) -> bool:
    return any(len(text) > MAX_STRING for text in _strings(value))


def content_identity(record: Any) -> str:
    """A refused record's identity: its content digest, never its claimed ``id`` (catalogue §8.3 step 6: refused "by
    identity and reason"), so a refusal is always recordable."""

    try:
        if isinstance(record, Mapping):
            return record_id(record)
        return "sha256:" + hashlib.sha256(b"ssds.element.v1" + canonical_json(record)).hexdigest()
    except (ValueError, TypeError):
        return "sha256:" + hashlib.sha256(b"ssds.element.unencodable" + repr(record).encode("utf-8")).hexdigest()


def verified_objects(objects: Any) -> tuple[dict[str, bytes], list[str]]:
    """The request's ``LEDGER``-store objects that are what their key says (a digest of their canonical JSON text),
    and the step 1 reasons for those that are not."""

    good: dict[str, bytes] = {}
    problems: list[str] = []
    if not isinstance(objects, Mapping):
        return good, ["SCHEMA_REQUEST"]
    for digest, text in objects.items():
        if not is_digest(digest) or not isinstance(text, str) or len(text.encode("utf-8")) > MAX_OBJECT_BYTES:
            problems.append("SCHEMA_OBJECT")
            continue
        data = text.encode("utf-8")
        try:
            parsed = json.loads(text)
            canonical = canonical_json(parsed) == data
        except (ValueError, TypeError):
            canonical = False
        if not canonical or "sha256:" + hashlib.sha256(data).hexdigest() != digest:
            problems.append("SCHEMA_OBJECT")
            continue
        if secret_detected(parsed):
            problems.append("SECRET_DETECTED")
            continue
        good[digest] = data
    return good, problems


def too_deep(value: Any, limit: int = MAX_DEPTH) -> bool:
    """Nesting deeper than the bound, measured without recursion, so no input can exhaust the stack."""

    stack = [(value, 1)]
    while stack:
        item, depth = stack.pop()
        if isinstance(item, (Mapping, list, tuple)):
            if depth > limit:
                return True
            children = item.values() if isinstance(item, Mapping) else item
            stack.extend((child, depth + 1) for child in children)
    return False


def measured_size(value: Any, limit: int = MAX_REQUEST_BYTES) -> int:
    """An upper estimate of a value's serialized size, measured without encoding it (so an unencodable value
    cannot slip past the byte bound) and without recursion; it stops counting once past ``limit``."""

    total, stack = 0, [value]
    while stack and total <= limit:
        item = stack.pop()
        if isinstance(item, str):
            total += len(item.encode("utf-8", "surrogatepass")) + 2
        elif isinstance(item, Mapping):
            total += 2
            for k, v in item.items():
                stack.append(k)
                stack.append(v)
        elif isinstance(item, (list, tuple)):
            total += 2 + len(item)
            stack.extend(item)
        else:
            total += len(repr(item))
    return total


def over_bounds(request: Any) -> bool:
    """A request beyond a count, depth or byte bound gets no per-record work and salvages nothing (§25.4)."""

    if too_deep(request):
        return True
    if isinstance(request, Mapping):
        records = request.get("records")
        if isinstance(records, list) and len(records) > MAX_RECORDS:
            return True
    return measured_size(request) > MAX_REQUEST_BYTES


def request_problems(request: Any) -> list[str]:
    """Step 1 at the request level: its shape, the grammar of each field, bounds, objects and secrets."""

    if too_deep(request):
        return ["SCHEMA_BOUND"]
    if not isinstance(request, Mapping) or set(request) - {"request_id"} != REQUEST_FIELDS:
        return ["SCHEMA_REQUEST"]
    position = request["base_position"]
    if not isinstance(request["records"], list) or not isinstance(request["claims"], list) \
            or not all(is_token(c) for c in request["claims"]) \
            or not isinstance(request["candidates"], list) or not all(is_commit(c) for c in request["candidates"]) \
            or not isinstance(request["adopted_deltas"], list) \
            or not all(isinstance(d, Mapping) for d in request["adopted_deltas"]) \
            or not isinstance(position, int) or isinstance(position, bool) or not is_commit(request["base_commit"]) \
            or not (request["binding"] is None or isinstance(request["binding"], Mapping)):
        return ["SCHEMA_REQUEST"]
    problems = []
    if over_bounds(request):
        problems.append("SCHEMA_BOUND")
    try:
        canonical_json(dict(request))
    except (ValueError, TypeError):
        problems.append("SCHEMA_REQUEST")
    problems += verified_objects(request["objects"])[1]
    if secret_detected({k: request[k] for k in ("binding", "claims", "adopted_deltas")}):
        problems.append("SECRET_DETECTED")
    return sorted(set(problems))


def record_problems(record: Any, schema_violations) -> list[str]:
    """Step 1 at the record level: the closed schema, bounds and the secret scan, each reported."""

    if not isinstance(record, Mapping):
        return ["SCHEMA_RECORD"]
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
        # a coordination decision names the decision obligations it answers there (reading E32), which step 7
        # checks against the head's derived obligations (Phase F 5b-iii), so they are no record references
        if isinstance(target.get("records"), list) and record.get("kind") != "COORDINATION_DECISION":
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


def referenced_objects(record: Mapping[str, Any]) -> set[str]:
    """The ``LEDGER``-store object digests a record's refs name."""

    return {r["digest"] for r in record.get("refs") or [] if isinstance(r, Mapping) and r.get("store") == "LEDGER"}


def transformation_named(record: Mapping[str, Any]) -> str | None:
    """The transformation a record names: the frame it declares, or the target of a work judgment or task result
    (catalogue §7.5, §8.3 step 2). A step 2 reference, which a result must have fixed (Phase F 4c-iii)."""

    frame = record.get("frame")
    if isinstance(frame, Mapping) and isinstance(frame.get("transformation"), str):
        return frame["transformation"]
    target = record.get("target")
    if record.get("kind") in ("REVIEW", "CONFORMANCE", "TASK_RESULT") and isinstance(target, Mapping) \
            and isinstance(target.get("transformation"), str):
        return target["transformation"]
    return None


def producing_context(record: Mapping[str, Any]) -> tuple[str, tuple[str, ...], Any] | None:
    """A task result's transformation and producing context (write scope, work key), §7.1; None otherwise."""

    if record.get("kind") != "TASK_RESULT":
        return None
    target = record.get("target") or {}
    if not submits(target):  # a result naming another candidate's identity claims no producing context (64a0330)
        return None
    x = target["transformation"]
    binding = record.get("binding") or {}
    return x, tuple(sorted(binding.get("write_scope") or ())), binding.get("item_key")


__all__ = ["REASONS", "content_identity", "producing_context", "transformation_named", "record_problems", "referenced_objects",
           "referenced_records", "referenced_revisions", "request_problems", "secret_detected", "verified_objects"]
