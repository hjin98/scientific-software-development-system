"""Admission's genesis path: validation of a shadow genesis (Manual §19.9; catalogue §19.9).

A shadow genesis declares every subject ``LEGACY(p)`` or ``UNGOVERNED``,
a witness model meeting ``q_a + r > N + f``, and carries the human gate: an
SSH signature, by a registered human key under namespace ``ssds``, over one
line naming the genesis digest.
"""

from __future__ import annotations

import hashlib
from collections.abc import Mapping
from typing import Any

from ssds.core.api.v1 import canonical_json
from ssds.ledger.qualification import WitnessModel
from ssds.ledger.read import human_key_id, verify_sshsig


def genesis_violations(genesis: Mapping[str, Any]) -> list[str]:
    """The genesis record's own checks: shadow modes, the witness model, the human approval (catalogue §19.9)."""

    problems: list[str] = []
    fields = genesis["fields"]
    for subject, mode in fields["modes"].items():
        if mode.get("mode") not in ("LEGACY", "UNGOVERNED"):
            problems.append(f"shadow genesis declares {subject} {mode.get('mode')}; only LEGACY or UNGOVERNED")
    try:
        WitnessModel.from_json(fields["witnesses"]).validate()
    except (KeyError, TypeError, ValueError) as exc:
        problems.append(f"witness model: {exc}")
    approval = fields["approval"]
    humans = {human_key_id(k["public_key"]): k["public_key"] for k in fields["trust_roots"].get("human_keys", [])}
    key = humans.get(approval.get("key_id"))
    if key is None:
        problems.append("the genesis approval key is not a registered human key")
    elif not verify_sshsig(key, genesis_approval_message(genesis), approval.get("signature", "")):
        problems.append("the genesis approval signature does not verify")
    return problems


def genesis_proposal(genesis: Mapping[str, Any]) -> dict[str, Any]:
    """The genesis record as the human gate approves it: without its id and approval."""

    fields = {k: v for k, v in genesis["fields"].items() if k != "approval"}
    return {k: (fields if k == "fields" else v) for k, v in genesis.items() if k != "id"}


def genesis_digest(genesis: Mapping[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(genesis_proposal(genesis))).hexdigest()


def genesis_approval_message(genesis: Mapping[str, Any]) -> bytes:
    """The exact bytes the human signs: one line naming the genesis digest."""

    return f"ssds genesis {genesis_digest(genesis)}\n".encode("ascii")
