"""The closed ledger schema, version 1 (catalogue §3.2-§3.6, §21.2).

Every record is a canonical JSON object with the common envelope of §3.2 and
the kind-specific fields under ``fields``. The schema is closed: an unknown
kind, an unknown or missing field, or a value outside its grammar is a
violation (C5). A record's identity is the digest of its canonical JSON
without ``id``.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any

from ssds.core.api.v1 import canonical_json

SCHEMA_VERSION = 1
READABLE_SCHEMAS = frozenset({1})
SYSTEM_RULESET = "ssds-rules/1"

DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
UNIT_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,62}(?:\.[a-z0-9][a-z0-9_-]{0,62})*(?:\.~)?$")
ACTOR_RE = re.compile(r"^(?:human|agent|machinery|admission):[\x21-\x7e]{1,200}$")
TOKEN_RE = re.compile(r"^[A-Za-z0-9_.:/@+-]{1,200}$")
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")

ACTOR_CLASSES = frozenset({"HUMAN", "AGENT", "MACHINERY", "ADMISSION"})
BASIS_MODES = frozenset({"content", "validity", "execution", "record", "standing", "identity"})
CONSUMPTION_CLASSES = frozenset({"EXACT", "EDITORIAL", "REPRESENTATION", "MIGRATION", "PLAN_CONTROL"})
ENTRY_KINDS = frozenset({"ADMISSION", "ABSORPTION", "LIFECYCLE"})

TIERS = ("support", "challenge", "observation", "admission", "lifecycle")


class SchemaViolation(ValueError):
    """A record or entry outside the closed schema."""


Check = Callable[[Any], bool]


def is_digest(v: Any) -> bool:
    return isinstance(v, str) and bool(DIGEST_RE.match(v))


def is_commit(v: Any) -> bool:
    return isinstance(v, str) and bool(COMMIT_RE.match(v))


def is_unit(v: Any) -> bool:
    return isinstance(v, str) and bool(UNIT_RE.match(v))


def is_token(v: Any) -> bool:
    return isinstance(v, str) and bool(TOKEN_RE.match(v))


def is_bool(v: Any) -> bool:
    return isinstance(v, bool)


def is_int(v: Any) -> bool:
    return isinstance(v, int) and not isinstance(v, bool) and v >= 0


def one_of(*values: str) -> Check:
    allowed = frozenset(values)
    return lambda v: isinstance(v, str) and v in allowed


def list_of(check: Check) -> Check:
    return lambda v: isinstance(v, list) and all(check(x) for x in v)


def optional(check: Check) -> Check:
    return lambda v: v is None or check(v)


def shape(required: Mapping[str, Check], optional_fields: Mapping[str, Check] | None = None) -> Check:
    extra = dict(optional_fields or {})

    def check(v: Any) -> bool:
        if not isinstance(v, dict) or not set(required) <= set(v) or not set(v) <= set(required) | set(extra):
            return False
        return all(c(v[k]) for k, c in required.items()) and all(c(v[k]) for k, c in extra.items() if k in v)

    return check


def is_json_object(v: Any) -> bool:
    return isinstance(v, dict)


TRIPLE = shape({"subject": is_unit, "scope_id": is_digest, "rev": is_digest})
UNIT_REV = shape({"unit": is_unit, "rev": is_digest})
RECORD_REF = shape({"record": is_digest})
RECORDS_REF = shape({"records": list_of(is_digest)})
TRANSFORMATION = shape({"transformation": is_digest}, {"item": UNIT_REV})
INTEGRATED = shape({"integrated": one_of("ITEM", "JOINT_INVARIANT", "HIGH_CONSEQUENCE"), "of": is_token,
                    "at": is_digest, "changes": list_of(is_digest)}, {"scope": list_of(is_unit)})
TARGET_TYPES: dict[str, Check] = {
    "triple": TRIPLE,
    "transformation": TRANSFORMATION,
    "integrated": INTEGRATED,
    "record": RECORD_REF,
    "records": RECORDS_REF,
    "equivalence": shape({"unit": is_unit, "from": is_digest, "to": is_digest, "class": is_token}),
    "completeness": shape({"scope": list_of(is_unit), "classes": list_of(one_of("DEF", "WARRANT", "GOVERNING", "EXEC", "STRUCT")),
                           "membership": is_digest}, {"analyzer": is_token}),
    "realization": shape({"realization": is_digest, "obligation": is_token}),
    "units": shape({"units": list_of(is_unit)}),
    "unit_rev": UNIT_REV,
    "task": shape({"task": is_token}, {"candidate": is_commit, "transformation": is_digest, "base": is_commit,
                                        "adopts": list_of(is_json_object)}),
    "obligation": shape({"obligation": is_token}),
    "gate": shape({"gate": is_token, "subject": TRIPLE, "core": is_digest}),
    "spec": shape({"spec": UNIT_REV, "claim": list_of(UNIT_REV)}),
    "contract": shape({"obligation": is_token, "candidate": is_commit}),
    "external": shape({"external": is_token}),
    "analyzer": shape({"analyzer": is_token, "inputs": list_of(UNIT_REV)}),
    "content_ref": shape({"digest": is_digest}),
    "custody": shape({"runner": is_token}),
    "loss": shape({"loss": is_digest}),
    "none": lambda v: v is None,
}


@dataclass(frozen=True)
class KindSpec:
    tier: str
    targets: tuple[str, ...]
    outcomes: frozenset[str] | None  # None: the kind has no outcome
    fields: Mapping[str, Check]
    required: frozenset[str] = frozenset()


def _k(tier: str, targets: str, outcomes: str | None, fields: Mapping[str, Check] | None = None,
       required: tuple[str, ...] = ()) -> KindSpec:
    return KindSpec(tier, tuple(targets.split("|")), None if outcomes is None else frozenset(outcomes.split()),
                    dict(fields or {}), frozenset(required))


_REPORT_FIELDS = {"materiality": one_of("ROUTINE", "MATERIAL", "CRITICAL"), "blocking": is_bool}
_LIFECYCLE_TARGET = "none"

KINDS: dict[str, KindSpec] = {
    # support tier
    "ACCEPTANCE": _k("support", "triple", "PASS FAIL"),
    "REVIEW": _k("support", "transformation|triple|integrated", "PASS NO_PASS"),
    "CONFORMANCE": _k("support", "transformation", "CONFORMANT NONCONFORMANT"),
    "EQUIVALENCE": _k("support", "equivalence", "EQUIVALENT NOT_EQUIVALENT"),
    "COMPLETENESS": _k("support", "completeness", "COMPLETE INCOMPLETE"),
    "EVIDENCE_ASSESSMENT": _k("support", "realization", "PASS FAIL INCONCLUSIVE",
                              {"mode": one_of("ORDINARY", "DISCRIMINATING"), "reading": UNIT_REV,
                               "failing_outputs": list_of(is_token), "observations": list_of(is_json_object)},
                              ("mode", "reading")),
    "IMMATERIALITY": _k("support", "records", "IMMATERIAL"),
    "PLAN_ACCEPTANCE": _k("support", "units", "ACCEPTED REJECTED", {"objective": UNIT_REV, "items": list_of(UNIT_REV)},
                          ("objective", "items")),
    "INTAKE_CLASSIFICATION": _k("support", "units|content_ref", "PROPOSED", {"kind": is_token}),
    "INTAKE_DISPOSITION": _k("support", "units|content_ref", "ADOPT ABSORB REALIGN QUARANTINE REJECT"),
    "LEGACY_ACCEPTANCE": _k("support", "triple", "IMPORTED", {"legacy": list_of(is_token)}),
    "EXTERNAL_ACCEPTANCE": _k("support", "external", "IMPORTED"),
    "RECONSTRUCTION_PROPOSAL": _k("support", "units", "PROPOSED PROVISIONAL UNKNOWN"),
    "TASK_RESULT": _k("support", "task", "COMPLETE INCOMPLETE PARTIAL", {"slots": is_json_object}),
    "FINDING": _k("support", "units|records", None, _REPORT_FIELDS, ("materiality",)),
    "AMENDMENT_REQUEST": _k("support", "units|records", None, _REPORT_FIELDS, ("materiality",)),
    "BLOCKER": _k("support", "units|records", None, _REPORT_FIELDS, ("materiality",)),
    "HUMAN_QUESTION": _k("support", "units|records", None, _REPORT_FIELDS, ("materiality",)),
    "COORDINATION_DECISION": _k("support", "records|units", "RESOLVE_LOCAL AMEND CHALLENGE ESCALATE DECLINE PARTITION",
                                {"tasks": list_of(is_token)}),
    "MATERIALITY_RECLASSIFICATION": _k("support", "record", "ROUTINE"),
    "HUMAN_DECISION": _k("support", "obligation", "ACKNOWLEDGE ANSWER ACCEPT REJECT REDIRECT MOOT"),
    "GATE_DECISION": _k("support", "gate", "ACCEPT REJECT",
                        {"adequacy": one_of("ADEQUATE", "INADEQUATE"),
                         "qualification": one_of("UNQUALIFIED", "QUALIFIED"), "qualifying": list_of(is_digest)},
                        ("adequacy", "qualification")),
    "PRODUCT_SCOPE_ACCEPTANCE": _k("support", "unit_rev", "ACCEPTED REJECTED"),
    "LINEAGE_ATTESTATION": _k("support", "record", "HUMAN_ATTESTED_FRESH"),
    "NON_AUTHORSHIP_ATTESTATION": _k("support", "record", "NOT_AUTHOR"),
    # challenge tier
    "CHALLENGE": _k("challenge", "record|triple", None,
                    {"blocking": is_bool, "serious": is_bool, "inquiry": one_of("EXPLORATORY", "CONFIRMATORY"),
                     "locus": optional(is_unit), "materiality": one_of("ROUTINE", "MATERIAL", "CRITICAL")},
                    ("blocking", "serious", "inquiry")),
    "ADJUDICATION": _k("challenge", "record", "UPHELD DISMISSED"),
    "WITHDRAWAL": _k("challenge", "record", None),
    # §10.5: the continuation scope is a closed set of subjects and items, the obligation kinds that may
    # discharge provisionally, and whether descendants created later inherit it (default no).
    "RISK_OVERRIDE": _k("challenge", "record", None,
                        {"continuation": shape({"subjects": list_of(is_unit), "items": list_of(is_unit),
                                                "kinds": list_of(is_token)}, {"inherit": is_bool})},
                        ("continuation",)),
    "CONTINUITY_ATTESTATION": _k("challenge", "loss", None,
                                 {"scope_form": one_of("COMPLEMENT", "EXPLICIT"), "listed": list_of(is_token),
                                  "evidence": list_of(is_digest)}, ("scope_form", "listed")),
    # observation tier
    "REALIZATION": _k("observation", "spec", "COMPLETE INCOMPLETE",
                      {"execution": is_json_object, "configuration": is_json_object, "evaluated": optional(is_digest)},
                      ("execution",)),
    "CHECK_EXECUTION": _k("observation", "contract", "CLEAN SIGNAL VIOLATION",
                          {"template": is_token, "tool": is_token}, ("template",)),
    "EXTERNAL_CONSULTATION": _k("observation", "external", "ACCEPTED NOT_ACCEPTED FORK ROLLBACK RETIRED UNQUALIFIED"),
    "ANALYZER_OUTPUT": _k("observation", "analyzer", None, {"output": is_digest}, ("output",)),
    "AVAILABILITY": _k("observation", "content_ref", "AVAILABLE UNAVAILABLE"),
    "CUSTODY_ENUMERATION": _k("observation", "custody", None, {"runs": list_of(is_digest)}, ("runs",)),
    # lifecycle tier (the record carried by a LIFECYCLE entry)
    "GENESIS": _k("lifecycle", _LIFECYCLE_TARGET, None,
                  {"project": is_token, "ledger_id": is_unit, "location": is_json_object,
                   "trust_roots": is_json_object, "witnesses": is_json_object, "structure": is_json_object,
                   "modes": is_json_object, "baseline_commit": is_commit, "deployment_class": one_of("LOCAL_TRUST", "TEAM", "HARDENED"),
                   "manifest_path": is_token, "policy_path": is_token, "approval": is_json_object},
                  ("project", "ledger_id", "location", "trust_roots", "witnesses", "structure", "modes",
                   "baseline_commit", "deployment_class", "manifest_path", "policy_path", "approval")),
    # ``doctrine`` pins the SSDP version and immutable public-source commit of native briefs (§16.9, §28;
    # Phase E reading E37); optional, so an adoption without one renders no native doctrine text
    "RULESET_ADOPTION": _k("lifecycle", _LIFECYCLE_TARGET, None,
                           {"system": is_token, "policy": is_digest, "analyzers": list_of(is_token),
                            "doctrine": shape({"version": is_token, "source": is_commit})},
                           ("system", "policy", "analyzers")),
    "SCHEMA_MIGRATION": _k("lifecycle", _LIFECYCLE_TARGET, None, {"to": is_int, "rules": is_json_object}, ("to", "rules")),
    "MODE_TRANSITION": _k("lifecycle", _LIFECYCLE_TARGET, None, {"subject": is_unit, "mode": is_json_object}, ("subject", "mode")),
    "LEGACY_RELEASE": _k("lifecycle", _LIFECYCLE_TARGET, None, {"scope": list_of(is_unit)}, ("scope",)),
    "KEY_LIFECYCLE": _k("lifecycle", _LIFECYCLE_TARGET, None,
                        {"action": one_of("REGISTER", "ROTATE", "RETIRE", "COMPROMISED"), "key": is_json_object,
                         "from_position": is_int, "outstanding": list_of(is_digest)}, ("action", "key")),
    "TRUST_MECHANISM_CHANGE": _k("lifecycle", _LIFECYCLE_TARGET, None, {"mechanism": is_json_object}, ("mechanism",)),
    "PROJECT_FORK": _k("lifecycle", _LIFECYCLE_TARGET, None, {"project": is_token}, ("project",)),
    "REPLICA_REDESIGNATION": _k("lifecycle", _LIFECYCLE_TARGET, None, {"location": is_json_object}, ("location",)),
    "WITNESS_SET_REDESIGNATION": _k("lifecycle", _LIFECYCLE_TARGET, None, {"witnesses": is_json_object, "continues_from": is_digest},
                                    ("witnesses", "continues_from")),
    "LEDGER_LOSS": _k("lifecycle", _LIFECYCLE_TARGET, None,
                      {"retained": is_json_object, "abandoned": list_of(is_json_object), "report": is_digest,
                       "controls": is_json_object}, ("retained", "abandoned", "report", "controls")),
    "FORK_RESOLUTION": _k("lifecycle", _LIFECYCLE_TARGET, None, {"abandoned": list_of(is_json_object)}, ("abandoned",)),
    "LINEAGE_MIGRATION": _k("lifecycle", _LIFECYCLE_TARGET, None, {"predecessor": is_json_object}, ("predecessor",)),
    "LINEAGE_RETIREMENT": _k("lifecycle", _LIFECYCLE_TARGET, None, {"successor": is_json_object}, ("successor",)),
    "REDACTION_NOTICE": _k("lifecycle", _LIFECYCLE_TARGET, None, {"objects": list_of(is_digest)}, ("objects",)),
}

#: The ADMISSION and ABSORPTION kinds are entry kinds, carried in an entry's own sections (§21.2).
CHALLENGE_TIER = frozenset(k for k, s in KINDS.items() if s.tier == "challenge")
SUPPORT_TIER = frozenset(k for k, s in KINDS.items() if s.tier == "support")
OBSERVATION_TIER = frozenset(k for k, s in KINDS.items() if s.tier == "observation")
LIFECYCLE_TIER = frozenset(k for k, s in KINDS.items() if s.tier == "lifecycle")
RECOVERY_LIFECYCLE = frozenset({"LEDGER_LOSS", "FORK_RESOLUTION", "WITNESS_SET_REDESIGNATION",
                                "REPLICA_REDESIGNATION", "LINEAGE_RETIREMENT"})

_ENVELOPE_REQUIRED: dict[str, Check] = {
    "id": is_digest,
    "kind": lambda v: v in KINDS,
    "schema": lambda v: v == SCHEMA_VERSION,
    "ruleset": shape({"system": is_token, "policy": is_digest, "analyzers": is_digest}),
    "actor": lambda v: isinstance(v, str) and bool(ACTOR_RE.match(v)),
    "actor_class": lambda v: v in ACTOR_CLASSES,
    "frame": lambda v: v == "ADMITTED" or shape({"transformation": is_digest})(v),
    "target": lambda v: True,  # checked per kind
    "basis": lambda v: isinstance(v, list),
    "outcome": lambda v: v is None or isinstance(v, str),
    "reason": list_of(is_token),
    "supersedes": list_of(is_digest),
    "binding": optional(shape(
        {"task": is_token, "obligation": is_token, "role": is_token, "lineage": list_of(is_token),
         "lineage_class": one_of("ATTESTED_FRESH", "HUMAN_ATTESTED_FRESH", "UNKNOWN")},
        {"item": shape({"unit": is_unit, "rev": is_digest}), "item_key": is_digest, "write_scope": list_of(is_unit),
         "envelope": is_digest})),
    "governs": lambda v: shape({"mode": one_of("NATIVE"), "ruleset": is_token})(v)
    or shape({"mode": one_of("LEGACY"), "protocol": is_token})(v),
    "provenance": lambda v: v is None or isinstance(v, dict),
    "refs": list_of(shape({"store": one_of("LEDGER", "REPO", "HOME", "RUNNER"), "digest": is_digest,
                           "media_type": is_token}, {"locator": is_token})),
    "recorded_at": lambda v: isinstance(v, str) and bool(TIMESTAMP_RE.match(v)),
    "fields": is_json_object,
}

_BASIS_TARGET = {
    "content": UNIT_REV,
    "validity": UNIT_REV,
    "execution": is_json_object,
    "record": RECORD_REF,
    "standing": RECORD_REF,
    "identity": lambda v: RECORD_REF(v) or TRIPLE(v) or UNIT_REV(v),
}


def _basis_entry_ok(entry: Any) -> bool:
    if not isinstance(entry, dict) or not {"mode", "target", "class"} <= set(entry) <= {"mode", "target", "class", "role"}:
        return False
    mode = entry["mode"]
    if mode not in BASIS_MODES or not _BASIS_TARGET[mode](entry["target"]):
        return False
    cls = entry["class"]
    if not (cls in CONSUMPTION_CLASSES or (isinstance(cls, str) and cls.startswith("CONSUMER:") and is_token(cls))):
        return False
    return entry.get("role") in (None, "BEFORE", "OUTPUT", "CONTEXT")


def record_id(record: Mapping[str, Any]) -> str:
    body = {k: v for k, v in record.items() if k != "id"}
    return "sha256:" + hashlib.sha256(canonical_json(body)).hexdigest()


def with_id(record: Mapping[str, Any]) -> dict[str, Any]:
    out = {k: v for k, v in record.items() if k != "id"}
    out["id"] = record_id(out)
    return out


def record_violations(record: Any) -> list[str]:
    """Every way the record violates the closed schema; empty when it conforms."""

    if not isinstance(record, dict):
        return ["a record is an object"]
    problems = []
    missing = set(_ENVELOPE_REQUIRED) - set(record)
    unknown = set(record) - set(_ENVELOPE_REQUIRED)
    if missing:
        problems.append(f"missing fields {sorted(missing)}")
    if unknown:
        problems.append(f"unknown fields {sorted(unknown)}")
    for name, check in _ENVELOPE_REQUIRED.items():
        if name in record and not check(record[name]):
            problems.append(f"field {name} outside its grammar")
    if problems:
        return problems
    spec = KINDS[record["kind"]]
    if not any(TARGET_TYPES[t](record["target"]) for t in spec.targets):
        problems.append(f"target outside the {record['kind']} target types {list(spec.targets)}")
    if spec.outcomes is None and record["outcome"] is not None:
        problems.append(f"{record['kind']} has no outcome")
    if spec.outcomes is not None and record["outcome"] not in spec.outcomes:
        problems.append(f"outcome outside {sorted(spec.outcomes)}")
    fields = record["fields"]
    if set(fields) - set(spec.fields):
        problems.append(f"unknown kind fields {sorted(set(fields) - set(spec.fields))}")
    if spec.required - set(fields):
        problems.append(f"missing kind fields {sorted(spec.required - set(fields))}")
    for name, check in spec.fields.items():
        if name in fields and not check(fields[name]):
            problems.append(f"kind field {name} outside its grammar")
    if not all(_basis_entry_ok(e) for e in record["basis"]):
        problems.append("a basis entry is outside its grammar")
    if record["kind"] == "GATE_DECISION" and record["outcome"] == "ACCEPT" and fields.get("adequacy") != "ADEQUATE":
        problems.append("a gate ACCEPT requires adequacy ADEQUATE")
    try:
        if record_id(record) != record["id"]:
            problems.append("id is not the digest of the record")
    except ValueError as exc:
        problems.append(f"not canonical JSON: {exc}")
    return problems


def tier(kind: str) -> str:
    return KINDS[kind].tier


DELTA = shape({"key": list_of(is_token), "value": lambda v: True, "source": one_of("AUTHORED", "ADOPTED")})
_ADMISSION_SECTION = shape(
    {"request_id": is_digest, "decision": one_of("ACCEPT", "REJECT"), "reasons": list_of(is_token),
     "base_commit": is_commit, "admitted_commit": is_commit, "adopted_deltas": list_of(DELTA),
     "integrates": optional(is_digest),
     "refused": list_of(shape({"record_id": is_digest, "reasons": list_of(is_token)}, {"object": is_digest}))}
)
_ABSORPTION_SECTION = shape({"fence": optional(shape({"base": is_commit, "fence_commit": is_commit}))})


def entry_violations(entry: Any) -> list[str]:
    """Violations of the entry shape of §21.2 (records are checked separately)."""

    if not isinstance(entry, dict):
        return ["an entry is an object"]
    required = {"ledger_id", "position", "schema", "prev", "entry_kind", "host_key_id", "incarnation_id", "obs",
                "admission", "absorption", "lifecycle", "records"}
    problems = []
    if set(entry) != required:
        problems.append(f"entry fields must be exactly {sorted(required)}")
        return problems
    if entry["schema"] not in READABLE_SCHEMAS:
        problems.append("UNREADABLE_SCHEMA")
        return problems
    if not is_unit(entry["ledger_id"]) or not is_int(entry["position"]):
        problems.append("ledger_id or position outside its grammar")
    if entry["position"] == 0 and entry["prev"] is not None:
        problems.append("genesis has no prev")
    if entry["position"] > 0 and not is_digest(entry["prev"]):
        problems.append("prev is the previous entry digest")
    if entry["entry_kind"] not in ENTRY_KINDS:
        problems.append("entry_kind outside its grammar")
    if not is_token(entry["host_key_id"]) or not is_token(entry["incarnation_id"]):
        problems.append("host key or incarnation outside its grammar")
    if not (entry["obs"] is None or is_commit(entry["obs"])):
        problems.append("obs is a commit or null")
    kind = entry["entry_kind"]
    if kind == "ADMISSION" and not (_ADMISSION_SECTION(entry["admission"]) and entry["absorption"] is None and entry["lifecycle"] is None):
        problems.append("an admission entry carries exactly its admission section")
    if kind == "ABSORPTION" and not (_ABSORPTION_SECTION(entry["absorption"]) and entry["admission"] is None
                                     and entry["lifecycle"] is None and entry["records"] == []):
        problems.append("an absorption entry carries its absorption section and no submitted records")
    if kind == "LIFECYCLE":
        lifecycle = entry["lifecycle"]
        if not (isinstance(lifecycle, dict) and lifecycle.get("kind") in LIFECYCLE_TIER and entry["admission"] is None
                and entry["absorption"] is None):
            problems.append("a lifecycle entry carries one lifecycle record")
        elif entry["obs"] is None and lifecycle.get("kind") not in RECOVERY_LIFECYCLE | {"GENESIS"}:
            problems.append("obs is null only for recovery lifecycle entries")
        if entry["position"] == 0 and isinstance(lifecycle, dict) and lifecycle.get("kind") != "GENESIS":
            problems.append("position 0 is GENESIS")
    if entry["position"] == 0 and kind != "LIFECYCLE":
        problems.append("position 0 is GENESIS")
    if not isinstance(entry["records"], list):
        problems.append("records is a list")
    return problems
