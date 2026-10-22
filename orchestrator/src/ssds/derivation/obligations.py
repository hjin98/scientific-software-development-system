"""Obligation identity (catalogue §10.2; Phase E reading E4).

An obligation's identity is deterministic from the rule, target and parameters
that derive it: ``sha256("ssds.obligation.v1" ‖ rule id ‖ JCS(target) ‖
JCS(parameters))``, each field length-prefixed so no concatenation is
ambiguous. A rule id names the system ruleset and the obligation kind.
"""

from __future__ import annotations

import hashlib
from typing import Any

from ssds.content import jcs

SYSTEM_RULESET = "ssds-rules/1"


def _field(data: bytes) -> bytes:
    return len(data).to_bytes(8, "big") + data


def rule_id(kind: str) -> str:
    return f"{SYSTEM_RULESET}#{kind}"


def obligation_id(kind: str, target: Any, parameters: Any = None) -> str:
    fields = (b"ssds.obligation.v1", rule_id(kind).encode("utf-8"), jcs(target), jcs(parameters or {}))
    return "sha256:" + hashlib.sha256(b"".join(_field(f) for f in fields)).hexdigest()
