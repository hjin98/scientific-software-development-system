"""Authentication of a request's binding (Manual §8.3 step 3, §12.2, §25.1-§25.2; catalogue §8.3 step 3, §12.2).

A **task binding** carries the task's envelope signed by a Dispatcher issue key, and on a harness route the launch
attestation and the per-task credential's signature over the request. The envelope verifies against an issue key
in force at the held head, or, for never-lost records only, against a retired, never-compromised key whose
retirement lists it. A key declared compromised is untrusted for envelopes issued from the named position on. The
lineage class is what the binding proves: ``ATTESTED_FRESH`` only with a valid attestation and credential
signature, otherwise ``UNKNOWN``. Each bound record's binding must name this envelope, task, obligation, role and
lineage, and its ``governs`` must equal the envelope's (``AUTH_VERSION``).

A **human binding** is a signature by a registered human key in the SSH signature format, namespace ``ssds``, over
the request without its binding; every record it carries is that human's (``AUTH_ACTOR`` otherwise).

The role, record-kind, write-scope and other authorization checks of step 3 are Phase F step 4's.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from ssds.core.api.v1 import canonical_json
from ssds.derivation import TrustRoots
from ssds.ledger.read import is_token, verify_host, verify_sshsig

from .request import (ENVELOPE_FIELDS, ROUTES, attestation_message, binding_digest, binding_object, envelope_message,
                      never_lost, request_message)

TASK_BINDING = frozenset({"envelope", "signature", "attestation", "attestation_signature", "credential_signature"})


@dataclass(frozen=True)
class Authentication:
    ok: bool  # the binding authenticates: never-lost salvage may proceed
    reasons: frozenset[str] = frozenset()  # request-level
    refused: tuple[tuple[str, tuple[str, ...]], ...] = ()  # (record id, reasons): records the binding does not cover
    lineage: str | None = None
    objects: dict[str, bytes] = field(default_factory=dict)  # the binding object, stored with admitted records
    retired_key: bool = False  # under a retired key: only never-lost records are admissible


def _verify(public_hex: str, message: bytes, signature: Any) -> bool:
    if not isinstance(signature, str):
        return False
    try:
        return verify_host(public_hex, message, bytes.fromhex(signature))
    except ValueError:
        return False


def authenticate(request: Mapping[str, Any], records: list[dict], roots: TrustRoots, head: int) -> Authentication:
    binding = request.get("binding")
    if not isinstance(binding, Mapping):
        return Authentication(False, frozenset({"AUTH_ENVELOPE"}))
    if set(binding) == {"human"}:
        return _human(request, binding["human"], records, roots)
    if set(binding) != TASK_BINDING or not isinstance(binding.get("envelope"), Mapping):
        return Authentication(False, frozenset({"AUTH_ENVELOPE"}))
    envelope = binding["envelope"]
    if set(envelope) != ENVELOPE_FIELDS or envelope.get("route") not in ROUTES \
            or not isinstance(envelope.get("issued_at_position"), int) or isinstance(envelope.get("issued_at_position"), bool) \
            or not 0 <= envelope["issued_at_position"] <= head or not isinstance(envelope.get("governs"), Mapping) \
            or not all(is_token(envelope.get(k)) for k in ("task_id", "obligation_id", "role", "issue_key_id")):
        return Authentication(False, frozenset({"AUTH_ENVELOPE"}))
    key_id = envelope["issue_key_id"]
    compromised = roots.compromised.get(key_id)
    if compromised is not None and envelope["issued_at_position"] >= compromised:
        return Authentication(False, frozenset({"AUTH_ENVELOPE"}))
    digest = binding_digest(binding)
    retired = False
    if key_id in roots.issue:
        public = roots.issue[key_id]
    elif key_id in roots.retired and compromised is None and digest in roots.retired[key_id][1]:
        public, retired = roots.retired[key_id][0], True
    else:
        return Authentication(False, frozenset({"AUTH_ENVELOPE"}))
    if not _verify(public, envelope_message(envelope), binding.get("signature")):
        return Authentication(False, frozenset({"AUTH_ENVELOPE"}))
    lineage = "UNKNOWN"
    attestation = binding.get("attestation")
    if envelope["route"] == "HARNESS" and isinstance(attestation, Mapping) \
            and attestation.get("task_id") == envelope["task_id"] and isinstance(attestation.get("credential_key"), str) \
            and _verify(public, attestation_message(attestation), binding.get("attestation_signature")) \
            and _verify(attestation["credential_key"], request_message(request), binding.get("credential_signature")):
        lineage = "ATTESTED_FRESH"
    refused = []
    for record in records:
        own = []
        rb = record.get("binding") or {}
        if (rb.get("envelope"), rb.get("task"), rb.get("obligation"), rb.get("role"), rb.get("lineage_class")) != \
                (digest, envelope["task_id"], envelope["obligation_id"], envelope["role"], lineage):
            own.append("AUTH_ENVELOPE")
        if record.get("governs") != envelope["governs"]:
            own.append("AUTH_VERSION")
        if retired and not never_lost(record):
            own.append("AUTH_ENVELOPE")  # a retired key's envelope covers never-lost records only (§8.3 step 3)
        if own:
            refused.append((record["id"], tuple(sorted(set(own)))))
    obj = canonical_json(binding_object(binding))
    return Authentication(True, frozenset(), tuple(refused), lineage, {digest: obj}, retired)


def _human(request: Mapping[str, Any], human: Any, records: list[dict], roots: TrustRoots) -> Authentication:
    if not isinstance(human, Mapping) or not isinstance(human.get("actor"), str) or human["actor"] not in roots.humans \
            or not isinstance(human.get("signature"), str) \
            or not verify_sshsig(roots.humans[human["actor"]], request_message(request), human["signature"]):
        return Authentication(False, frozenset({"AUTH_ENVELOPE"}))
    refused = [(r["id"], ("AUTH_ACTOR",)) for r in records
               if r.get("actor") != human["actor"] or r.get("actor_class") != "HUMAN" or r.get("binding") is not None]
    return Authentication(True, frozenset(), tuple(refused), None, {})


__all__ = ["Authentication", "authenticate"]
