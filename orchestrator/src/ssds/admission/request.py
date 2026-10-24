"""Admission requests (Manual §8.1; catalogue §8.1): the one public surface through which other components submit.

A request is a JSON object built by machinery:

- ``binding``: the task envelope that produced it (§12.2), or ``None`` for records an authenticated human or a
  machinery component records directly;
- ``claims``: the obligation identities whose discharge it claims, possibly none;
- ``base_position`` and ``base_commit``: the admitted position and integration commit it worked from;
- ``candidates``: its candidate commits on isolated refs, empty for a records-only request;
- ``adopted_deltas``: the quarantined structural deltas it adopts;
- ``records``: the records it submits, each carrying its own ``id``;
- ``objects``: the ``LEDGER``-store objects its records reference, by digest, as canonical JSON text.

Its identity is ``sha256("ssds.request.v1" ‖ JCS(request without request_id))`` [D3 decision], so a repeated
identical request is recognised and returns the recorded decision, appending nothing.
"""

from __future__ import annotations

import hashlib
from collections.abc import Mapping
from typing import Any

from ssds.core.api.v1 import canonical_json
from ssds.derivation import adverse

REQUEST_FIELDS = frozenset({"binding", "claims", "base_position", "base_commit", "candidates", "adopted_deltas",
                            "records", "objects"})
REPORT_KINDS = frozenset({"FINDING", "AMENDMENT_REQUEST", "BLOCKER", "HUMAN_QUESTION"})
#: Observations a designated runner's execution produces (§17.5).
RUNNER_OBSERVATIONS = frozenset({"REALIZATION", "CHECK_EXECUTION"})


def request_id(request: Any) -> str:
    """The request's content identity (catalogue §8.1). A request that is not an object, or that canonical JSON
    cannot encode (a float, a non-string key), still gets a deterministic identity, so its rejection is recorded
    once and repeats return it (Manual §25.4: untrusted input is data)."""

    body = {k: v for k, v in request.items() if k != "request_id"} if isinstance(request, Mapping) else request
    try:
        return "sha256:" + hashlib.sha256(b"ssds.request.v1" + canonical_json(body)).hexdigest()
    except (ValueError, TypeError):
        return "sha256:" + hashlib.sha256(b"ssds.request.v1.unencodable" + repr(body).encode("utf-8")).hexdigest()


#: The task envelope's fields (catalogue §12.2; the ``retained`` field is dropped, G2 register RR-2), with the
#: rendered brief's content identity, which Manual §16.4 records in the envelope.
ENVELOPE_FIELDS = frozenset({"task_id", "obligation_id", "role", "contract_revision", "governs", "route", "lineage_class",
                             "input_sessions", "issued_at_position", "issue_key_id", "predecessors", "brief"})
ROUTES = frozenset({"HARNESS", "MANUAL", "GIT_ENVELOPE"})


def _digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value)).hexdigest()


def binding_object(binding: Mapping[str, Any]) -> dict[str, Any]:
    """What a task binding stores in the ledger, so derivation and replay read it from the ledger alone (§12.2): the
    envelope, its issue-key signature and the launch attestation; never the per-task credential's request
    signature, which is about one request."""

    return {k: binding.get(k) for k in ("envelope", "signature", "attestation", "attestation_signature")}


def binding_digest(binding: Mapping[str, Any]) -> str:
    """The digest a bound record's ``binding.envelope`` names: that of the stored binding object."""

    return _digest(binding_object(binding))


def envelope_message(envelope: Mapping[str, Any]) -> bytes:
    return b"ssds envelope " + _digest(dict(envelope)).encode("ascii") + b"\n"


def attestation_message(attestation: Mapping[str, Any]) -> bytes:
    return b"ssds launch " + _digest(dict(attestation)).encode("ascii") + b"\n"


def request_message(request: Mapping[str, Any]) -> bytes:
    """What a per-task credential or an authenticated human signs: the request's identity without its binding."""

    return b"ssds request " + request_id({**request, "binding": None}).encode("ascii") + b"\n"


def never_lost(record: Mapping[str, Any]) -> bool:
    """Reports, challenges, failing assessments, adverse judgments and designated-runner observations: admitted
    whatever the request's fate when they pass their own checks (catalogue §8.3 step 6)."""

    kind, outcome = record.get("kind"), record.get("outcome")
    if not isinstance(kind, str) or not (outcome is None or isinstance(outcome, str)):
        return False  # total over untrusted input: a malformed record is never-lost to no one (Manual §25.4)
    if kind in REPORT_KINDS or kind == "CHALLENGE":
        return True
    if kind == "EVIDENCE_ASSESSMENT" and outcome == "FAIL":
        return True
    if "outcome" in record and adverse({"kind": kind, "outcome": outcome}):  # the derivation owner (§5.10 (a))
        return True
    return kind in RUNNER_OBSERVATIONS and str(record.get("actor", "")).startswith("machinery:")


__all__ = ["ENVELOPE_FIELDS", "REPORT_KINDS", "REQUEST_FIELDS", "ROUTES", "RUNNER_OBSERVATIONS", "attestation_message",
           "binding_digest", "binding_object", "envelope_message", "never_lost", "request_id", "request_message"]
