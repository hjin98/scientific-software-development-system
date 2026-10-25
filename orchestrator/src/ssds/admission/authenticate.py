"""Authentication of a request's binding (Manual §8.3 step 3, §12.2, §25.1-§25.2; catalogue §8.3 step 3, §12.2).

A **task binding** carries the task's envelope signed by a Dispatcher issue key, and on a harness route the launch
attestation and the per-task credential's signature over the request. The envelope verifies against an issue key
in force at the held head, or, for never-lost records only, against a retired, never-compromised key whose
retirement lists it. A key declared compromised is untrusted for envelopes issued from the named position on. A
harness binding authenticates only when its attestation names this task, this envelope and its input sessions and
verifies under the issue key, and the credential it names signed this request: lineage ``ATTESTED_FRESH``. Any
other route carries none of the three, and its lineage is ``UNKNOWN``. Material that does not verify is never
stored: the binding then authenticates nothing (Review e6ac009 B3).

A bound record's lineage is exactly the attestation closure Admission computes from the verified launch
attestations the ledger stores, and empty under ``UNKNOWN`` (§12.2; reading F11). An envelope authenticates its task's agent and
nothing else (§25.1): each bound record's actor is
``agent:<task id>/<attempt>`` of class ``AGENT`` (``AUTH_ACTOR`` otherwise), so a binding cannot speak for a human,
machinery or a designated runner, whose observations wait for runner keys (Phase F step 9; Review e6ac009 B1). Each
bound record's binding must name this envelope, task, obligation, role and lineage, and its ``governs`` must equal
the envelope's (``AUTH_VERSION``).

A **human binding** is a signature by a registered human key in the SSH signature format, namespace ``ssds``, over
the request without its binding; every record it carries is that human's (``AUTH_ACTOR`` otherwise).

A binding is untrusted input: one canonical JSON cannot encode, or one carrying a secret, authenticates nothing,
and nothing in it is stored (Manual §24.1, §25.4; Review e6ac009 B2, B4).

The role, record-kind, write-scope and other authorization checks of step 3 are Phase F step 4's.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from ssds.core.api.v1 import canonical_json
from ssds.derivation import TrustRoots
from ssds.ledger.read import is_token, verify_host, verify_sshsig

from .checks import secret_detected
from .request import (ATTESTATION_FIELDS, ENVELOPE_FIELDS, ROUTES, attestation_message, binding_digest, binding_object,
                      envelope_digest, envelope_message, never_lost, request_message)

TASK_BINDING = frozenset({"envelope", "signature", "attestation", "attestation_signature", "credential_signature"})
HUMAN_BINDING = frozenset({"actor", "signature"})
_ATTEMPT = re.compile(r"[0-9]{1,9}")
_PUBLIC_KEY = re.compile(r"[0-9a-f]{64}")
_SIGNATURE = re.compile(r"[0-9a-f]{128}")


@dataclass(frozen=True)
class Authentication:
    ok: bool  # the binding authenticates: never-lost salvage may proceed
    reasons: frozenset[str] = frozenset()  # request-level
    refused: tuple[tuple[str, tuple[str, ...]], ...] = ()  # (record id, reasons): records the binding does not cover
    lineage: str | None = None
    objects: dict[str, bytes] = field(default_factory=dict)  # the binding object, stored with admitted records
    retired_key: bool = False  # under a retired key: only never-lost records are admissible


NOT_AUTHENTICATED = Authentication(False, frozenset({"AUTH_ENVELOPE"}))


def _verify(public_hex: str, message: bytes, signature: Any) -> bool:
    return isinstance(signature, str) and bool(_SIGNATURE.fullmatch(signature)) \
        and verify_host(public_hex, message, bytes.fromhex(signature))


def _encodable(value: Any) -> bool:
    try:
        canonical_json(value)
    except (ValueError, TypeError):
        return False
    return True


def _envelope(envelope: Any, head: int) -> bool:
    """The envelope's closed shape, its route and an issue position the held head has reached."""

    if not isinstance(envelope, Mapping) or set(envelope) != ENVELOPE_FIELDS:
        return False
    position = envelope["issued_at_position"]
    return isinstance(envelope["route"], str) and envelope["route"] in ROUTES \
        and isinstance(position, int) and not isinstance(position, bool) and 0 <= position <= head \
        and isinstance(envelope["governs"], Mapping) \
        and all(is_token(envelope[k]) for k in ("task_id", "obligation_id", "role", "issue_key_id"))


def _attested(request: Mapping[str, Any], binding: Mapping[str, Any], public: str) -> bool:
    """A harness launch: the attestation is this envelope's and the issue key's, and its credential signed this
    request (§12.2)."""

    envelope, attestation = binding["envelope"], binding["attestation"]
    return isinstance(attestation, Mapping) and set(attestation) == ATTESTATION_FIELDS \
        and attestation["task_id"] == envelope["task_id"] and attestation["envelope"] == envelope_digest(envelope) \
        and is_token(attestation["session"]) and attestation["input_sessions"] == envelope["input_sessions"] \
        and isinstance(attestation["credential_key"], str) and bool(_PUBLIC_KEY.fullmatch(attestation["credential_key"])) \
        and _verify(public, attestation_message(attestation), binding["attestation_signature"]) \
        and _verify(attestation["credential_key"], request_message(request), binding["credential_signature"])


def lineage_closure(session: str, inputs: list[str], attestations: Mapping[str, list[str]]) -> list[str]:
    """The attestation closure of a launched session (§12.2; Phase F reading F11): the session, then every session
    reachable through the input sessions of stored launch attestations, sorted, and ``UNKNOWN`` when an input
    session has no stored attestation, so the closure is open and never disjoint from anything."""

    seen, frontier, open_ = {session}, list(inputs), False
    while frontier:
        current = frontier.pop()
        if current in seen:
            continue
        seen.add(current)
        if current in attestations:
            frontier.extend(attestations[current])
        else:
            open_ = True
    return [session, *sorted(seen - {session}), *(["UNKNOWN"] if open_ else [])]


def stored_attestations(objects: Mapping[str, bytes], bindings: set[str]) -> dict[str, list[str]]:
    """Session -> its input sessions, from the launch attestations of the stored binding objects that admitted
    records name (``bindings``: their ``binding.envelope`` digests), each verified when its records were admitted.
    No other stored object is read, so a record cannot inject an attestation (plan review 8a41539 B1). A session
    two bindings attest differently is left out, so its closure stays open."""

    import json

    out: dict[str, list[str]] = {}
    conflicted: set[str] = set()
    for digest in sorted(bindings):
        data = objects.get(digest)
        try:
            value = json.loads(data) if data is not None else None
        except ValueError:
            continue
        attestation = value.get("attestation") if isinstance(value, dict) else None
        if isinstance(attestation, dict) and isinstance(attestation.get("session"), str) \
                and isinstance(attestation.get("input_sessions"), list):
            session = attestation["session"]
            inputs = [x for x in attestation["input_sessions"] if isinstance(x, str)]
            if session in out and out[session] != inputs:
                conflicted.add(session)
            out.setdefault(session, inputs)
    return {k: v for k, v in out.items() if k not in conflicted}


def authenticate(request: Mapping[str, Any], records: list[dict], roots: TrustRoots, head: int,
                 attestations: Mapping[str, list[str]] | None = None) -> Authentication:
    binding = request.get("binding")
    if not isinstance(binding, Mapping) or not _encodable(binding):
        return NOT_AUTHENTICATED
    if secret_detected(binding):
        return Authentication(False, frozenset({"SECRET_DETECTED"}))
    if set(binding) == {"human"}:
        return _human(request, binding["human"], records, roots)
    if set(binding) != TASK_BINDING or not _envelope(binding["envelope"], head):
        return NOT_AUTHENTICATED
    envelope = binding["envelope"]
    key_id = envelope["issue_key_id"]
    compromised = roots.compromised.get(key_id)
    if compromised is not None and envelope["issued_at_position"] >= compromised:
        return NOT_AUTHENTICATED
    digest = binding_digest(binding)
    retired = False
    if key_id in roots.issue:
        public = roots.issue[key_id]
    elif key_id in roots.retired and compromised is None and digest in roots.retired[key_id][1]:
        public, retired = roots.retired[key_id][0], True
    else:
        return NOT_AUTHENTICATED
    if not _verify(public, envelope_message(envelope), binding["signature"]):
        return NOT_AUTHENTICATED
    if envelope["route"] == "HARNESS":
        if not _attested(request, binding, public):
            return NOT_AUTHENTICATED
        lineage = "ATTESTED_FRESH"
    elif any(binding[k] is not None for k in ("attestation", "attestation_signature", "credential_signature")):
        return NOT_AUTHENTICATED
    else:
        lineage = "UNKNOWN"
    agent = f"agent:{envelope['task_id']}/"
    attestation = binding["attestation"]
    lineage_list = lineage_closure(attestation["session"], attestation["input_sessions"], attestations or {}) \
        if lineage == "ATTESTED_FRESH" else []
    refused = []
    for record in records:
        own = []
        actor = record.get("actor")
        if record.get("actor_class") != "AGENT" or not isinstance(actor, str) or not actor.startswith(agent) \
                or not _ATTEMPT.fullmatch(actor[len(agent):]):
            own.append("AUTH_ACTOR")
        rb = record.get("binding")
        rb = rb if isinstance(rb, Mapping) else {}
        if (rb.get("envelope"), rb.get("task"), rb.get("obligation"), rb.get("role"), rb.get("lineage_class")) != \
                (digest, envelope["task_id"], envelope["obligation_id"], envelope["role"], lineage):
            own.append("AUTH_ENVELOPE")
        if (rb.get("lineage") or []) != lineage_list:
            # exactly what the binding proves: derivation reads a producing record's lineage as authorship, so a
            # superset would plant authors (plan review 6e0fa9e NB-2); none under UNKNOWN (reading F11)
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
    if not isinstance(human, Mapping) or set(human) != HUMAN_BINDING or not isinstance(human["actor"], str) \
            or human["actor"] not in roots.humans or not isinstance(human["signature"], str) \
            or not verify_sshsig(roots.humans[human["actor"]], request_message(request), human["signature"]):
        return NOT_AUTHENTICATED
    refused = [(r["id"], ("AUTH_ACTOR",)) for r in records
               if r.get("actor") != human["actor"] or r.get("actor_class") != "HUMAN" or r.get("binding") is not None]
    return Authentication(True, frozenset(), tuple(refused), None, {})


__all__ = ["Authentication", "NOT_AUTHENTICATED", "authenticate", "lineage_closure", "stored_attestations"]
