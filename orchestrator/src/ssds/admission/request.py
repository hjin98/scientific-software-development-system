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

REQUEST_FIELDS = frozenset({"binding", "claims", "base_position", "base_commit", "candidates", "adopted_deltas",
                            "records", "objects"})
REPORT_KINDS = frozenset({"FINDING", "AMENDMENT_REQUEST", "BLOCKER", "HUMAN_QUESTION"})
#: Judgment outcomes that are adverse (§5.10): they veto while they stand, whatever their context's currency.
ADVERSE_OUTCOMES = {
    "ACCEPTANCE": "FAIL", "REVIEW": "NO_PASS", "CONFORMANCE": "NONCONFORMANT", "EQUIVALENCE": "NOT_EQUIVALENT",
    "COMPLETENESS": "INCOMPLETE", "PLAN_ACCEPTANCE": "REJECTED", "GATE_DECISION": "REJECT",
}
#: Observations a designated runner's execution produces (§17.5).
RUNNER_OBSERVATIONS = frozenset({"REALIZATION", "CHECK_EXECUTION"})


def request_id(request: Mapping[str, Any]) -> str:
    """The request's content identity (catalogue §8.1)."""

    body = {k: v for k, v in request.items() if k != "request_id"}
    return "sha256:" + hashlib.sha256(b"ssds.request.v1" + canonical_json(body)).hexdigest()


def never_lost(record: Mapping[str, Any]) -> bool:
    """Reports, challenges, failing assessments, adverse judgments and designated-runner observations: admitted
    whatever the request's fate when they pass their own checks (catalogue §8.3 step 6)."""

    kind = record.get("kind")
    if kind in REPORT_KINDS or kind == "CHALLENGE":
        return True
    if kind == "EVIDENCE_ASSESSMENT" and record.get("outcome") == "FAIL":
        return True
    if ADVERSE_OUTCOMES.get(str(kind)) == record.get("outcome"):
        return True
    return kind in RUNNER_OBSERVATIONS and str(record.get("actor", "")).startswith("machinery:")


__all__ = ["ADVERSE_OUTCOMES", "REPORT_KINDS", "REQUEST_FIELDS", "RUNNER_OBSERVATIONS", "never_lost", "request_id"]
