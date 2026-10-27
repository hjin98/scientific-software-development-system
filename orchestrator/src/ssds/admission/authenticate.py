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

A **re-issue's resubmission** (Phase F step 8g-ii, reading F74): a never-lost record refused under a retired key's
unlisted envelope is retained, and the derived ``REISSUE(envelope)`` obligation lists its identity. The Dispatcher
resubmits it under the original task re-issued by a key in force, whose envelope copies the original task, obligation,
role, contract revision and ``governs``. For exactly the identities a ``REISSUE`` obligation at the request's base
lists, a record citing one (``provenance.reissue_of``) is authenticated against the retained record instead of the
envelope's launch: its content apart from ``id``, ``binding`` and ``provenance`` equals the retained body, and its
actor, ``lineage_class`` and ``lineage`` equal the retained record's, which were verified against the original stored
binding object when it was refused (F9, F11; re-check of 70cef9cf, note 1).

The role, record-kind, write-scope and other authorization checks of step 3 are Phase F step 4's.
"""

from __future__ import annotations

import json
import re
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from ssds.core.api.v1 import canonical_json
from ssds.derivation import TrustRoots, Workflow
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
    reissue: str | None = None  # a verified envelope of a retired key its retirement does not list (§8.3 step 3)
    retained: Mapping[str, "Retained"] = field(default_factory=dict)  # the listed identities resubmitted here (F74)


@dataclass(frozen=True)
class Retained:
    """A never-lost record refused under an unlisted retired envelope, whose identity a ``REISSUE`` obligation at the
    request's base lists (reading F74)."""

    body: dict[str, Any]  # the retained record, without its id
    envelope: dict[str, Any]  # the original envelope, from the binding object stored with the refusal
    obligation: Any  # the original obligation as derived at the original issue position, or None


def retained(history: Any, position: int, objects: Mapping[str, bytes]) -> dict[str, Retained]:
    """The identities the ``REISSUE`` obligations derived at ``position`` list, each with its retained body, its
    original envelope and its original obligation, judged under the ruleset in force at the original issue
    (re-check of 25bd1d0d, note 1)."""

    out: dict[str, Retained] = {}
    for o in Workflow.historical(history, position).obligations:
        if o.kind != "REISSUE":
            continue
        for rid in (o.params or {}).get("records", []):
            try:
                body = json.loads(objects[rid])
                original = json.loads(objects[body["binding"]["envelope"]])["envelope"]
            except (KeyError, TypeError, ValueError):
                continue
            if not isinstance(original, dict) or set(original) != ENVELOPE_FIELDS \
                    or not isinstance(original["issued_at_position"], int) \
                    or not 0 <= original["issued_at_position"] <= position:
                continue
            at = Workflow.historical(history, original["issued_at_position"])
            obligation = next((x for x in at.obligations if x.id == original["obligation_id"]), None)
            out[rid] = Retained(body, original, obligation)
    return out


def resubmission(record: Mapping[str, Any], listed: Mapping[str, Retained]) -> Retained | None:
    """The retained record ``record`` resubmits, when it cites a listed identity (``provenance.reissue_of``)."""

    provenance = record.get("provenance")
    cited = provenance.get("reissue_of") if isinstance(provenance, Mapping) else None
    return listed.get(cited) if isinstance(cited, str) else None


def _content(record: Mapping[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in record.items() if k not in ("id", "binding", "provenance")}


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
                 attestations: Mapping[str, list[str]] | None = None,
                 listed: Mapping[str, Retained] | None = None) -> Authentication:
    binding = request.get("binding")
    if not isinstance(binding, Mapping) or not _encodable(binding):
        return NOT_AUTHENTICATED
    if secret_detected(binding):
        return Authentication(False, frozenset({"SECRET_DETECTED"}))
    if set(binding) == {"human"}:
        return _human(request, binding["human"], records, roots)
    cosigned = set(binding) == TASK_BINDING | {"human"}
    if (set(binding) != TASK_BINDING and not cosigned) or not _envelope(binding["envelope"], head):
        return NOT_AUTHENTICATED
    envelope = binding["envelope"]
    key_id = envelope["issue_key_id"]
    compromised = roots.compromised.get(key_id)
    if compromised is not None and envelope["issued_at_position"] >= compromised:
        return NOT_AUTHENTICATED
    digest = binding_digest(binding)
    retired = unlisted = False
    if key_id in roots.issue:
        public = roots.issue[key_id]
    elif key_id in roots.retired and compromised is None \
            and envelope["issued_at_position"] < roots.retired_at.get(key_id, 0):  # issued while in force (N4)
        public, retired = roots.retired[key_id][0], True
        unlisted = digest not in roots.retired[key_id][1]  # the one difference the re-issue path makes
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
    cosigner = None
    if cosigned:
        # step 8d, reading F72: on the manual or Git-envelope route, the human who ran the fresh session co-signs the
        # request, whose bound records name this envelope, so the signature is this task's; it authenticates only that
        # human's LINEAGE_ATTESTATION of a record bound here, which alone lets that record carry HUMAN_ATTESTED_FRESH
        human = binding["human"]
        if lineage != "UNKNOWN" or not isinstance(human, Mapping) or set(human) != HUMAN_BINDING \
                or not isinstance(human["actor"], str) or human["actor"] not in roots.humans \
                or not isinstance(human["signature"], str) \
                or not verify_sshsig(roots.humans[human["actor"]], request_message(request), human["signature"]):
            return NOT_AUTHENTICATED
        cosigner = human["actor"]
    bound_here = {r.get("id") for r in records if isinstance(r.get("binding"), Mapping)
                  and r["binding"].get("envelope") == digest}
    attested = {r["target"].get("record") for r in records if cosigner is not None and _attests(r, cosigner, bound_here)}
    agent = f"agent:{envelope['task_id']}/"
    attestation = binding["attestation"]
    lineage_list = lineage_closure(attestation["session"], attestation["input_sessions"], attestations or {}) \
        if lineage == "ATTESTED_FRESH" else []
    refused = []
    resubmitted: dict[str, Retained] = {}
    for record in records:
        own = []
        actor = record.get("actor")
        if cosigner is not None and _attests(record, cosigner, bound_here):
            continue  # the co-signer's own attestation, authenticated by the co-signature
        kept = resubmission(record, listed or {})
        if kept is not None:
            # a re-issue's resubmission (reading F74): against the retained record, under the original task re-issued
            # by a key in force, whose envelope copies the original's task, obligation, role, contract and governs
            original, rb, kb = kept.envelope, record.get("binding"), kept.body.get("binding")
            rb, kb = (rb if isinstance(rb, Mapping) else {}), (kb if isinstance(kb, Mapping) else {})
            fields = ("task_id", "obligation_id", "role", "contract_revision", "governs")
            if retired or any(envelope[k] != original[k] for k in fields) \
                    or _content(record) != _content(kept.body) \
                    or (actor, record.get("actor_class")) != (kept.body.get("actor"), kept.body.get("actor_class")) \
                    or rb.get("envelope") != digest \
                    or {k: v for k, v in rb.items() if k != "envelope"} != \
                    {k: v for k, v in kb.items() if k != "envelope"}:
                refused.append((record["id"], ("AUTH_ENVELOPE",)))
            else:
                resubmitted[record["provenance"]["reissue_of"]] = kept
            continue
        if record.get("id") in attested:
            expected = "HUMAN_ATTESTED_FRESH"  # fixed at admission by the co-submitted attestation (§5.10 (a))
        else:
            expected = lineage
        if record.get("actor_class") != "AGENT" or not isinstance(actor, str) or not actor.startswith(agent) \
                or not _ATTEMPT.fullmatch(actor[len(agent):]):
            own.append("AUTH_ACTOR")
        rb = record.get("binding")
        rb = rb if isinstance(rb, Mapping) else {}
        if (rb.get("envelope"), rb.get("task"), rb.get("obligation"), rb.get("role"), rb.get("lineage_class")) != \
                (digest, envelope["task_id"], envelope["obligation_id"], envelope["role"], expected):
            own.append("AUTH_ENVELOPE")
        if rb.get("item") != envelope.get("contract_revision"):
            # the contract revision a record works under is the envelope's, never self-declared: conformance and
            # step 7's currency read it (§12.2; review fed5d82 B3)
            own.append("AUTH_ENVELOPE")
        if record.get("kind") == "TASK_RESULT" and isinstance(record.get("target"), Mapping) \
                and record["target"].get("task") != envelope["task_id"]:
            own.append("AUTH_ENVELOPE")  # a result is its own task's: enactment and step 7 read it (review fed5d82 B1)
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
    if unlisted:
        # genuinely issued by a retired key, but its retirement does not list it: every check above has run, and its
        # never-lost records that passed them are refused, retained and re-issued (§8.3 step 3; review 8d274c4 B1)
        return Authentication(False, frozenset({"AUTH_ENVELOPE"}), tuple(refused), lineage, {digest: obj}, retired,
                              reissue=digest)
    return Authentication(True, frozenset(), tuple(refused), lineage, {digest: obj}, retired, retained=resubmitted)


def _attests(record: Mapping[str, Any], cosigner: str, bound_here: set) -> bool:
    """The co-signer's ``LINEAGE_ATTESTATION`` of a record bound to this task in this request (reading F72). Such a
    record is authenticated by the co-signature instead of the per-record agent checks (actor, envelope fields,
    contract, lineage, ``AUTH_VERSION``, the retired-key rule): its governing version does not matter, and under a
    retired key its target, not never-lost, is refused, so the cascade drops it (review 50954f9 N2)."""

    target = record.get("target")
    return record.get("kind") == "LINEAGE_ATTESTATION" and record.get("outcome") == "HUMAN_ATTESTED_FRESH" \
        and record.get("actor") == cosigner and record.get("actor_class") == "HUMAN" \
        and record.get("binding") is None and isinstance(target, Mapping) and target.get("record") in bound_here


def _human(request: Mapping[str, Any], human: Any, records: list[dict], roots: TrustRoots) -> Authentication:
    if not isinstance(human, Mapping) or set(human) != HUMAN_BINDING or not isinstance(human["actor"], str) \
            or human["actor"] not in roots.humans or not isinstance(human["signature"], str) \
            or not verify_sshsig(roots.humans[human["actor"]], request_message(request), human["signature"]):
        return NOT_AUTHENTICATED
    refused = [(r["id"], ("AUTH_ACTOR",)) for r in records
               if r.get("actor") != human["actor"] or r.get("actor_class") != "HUMAN" or r.get("binding") is not None]
    return Authentication(True, frozenset(), tuple(refused), None, {})


__all__ = ["Authentication", "NOT_AUTHENTICATED", "Retained", "authenticate", "lineage_closure", "resubmission",
           "retained", "stored_attestations"]
