"""Human-gated ``KEY_LIFECYCLE`` records (Manual §25.2; catalogue §25.2; Phase F reading F5).

The human gate signs the record for one place in one ledger: the ledger id, the position the entry will take and
the digest of the head it extends, with the record's identity without the provenance that carries the approval. A
signature is spent by its entry, so an old approval cannot be replayed onto this ledger or another one, and an
already-admitted lifecycle record is refused besides (Review e6ac009 B5).

Each action has a closed key shape (Review e6ac009 B6). Every key object is ``{role, id, public_key}``, and a
rotation adds ``retires``, the in-force key it replaces; ``id`` is the key's own identity (``ed25519:`` of an issue
key's raw public key, the OpenSSH fingerprint of a human's), so no id is ever bound to another key. A
registration or rotation introduces a key never known before; a retirement names a key in force with its public
key; a compromise names a known key. Only an issue key's retirement or rotation lists outstanding envelopes, and
only a compromise names a position. Admission host keys and designated runner keys are not rotated through this
path yet (the engine's own key switch and runner keys are later Phase F steps): those roles are refused.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from typing import Any

from ssds.derivation import TrustRoots
from ssds.ledger.read import human_key_id, record_id

ACTIONS = frozenset({"REGISTER", "ROTATE", "RETIRE", "COMPROMISED"})
ROLES = frozenset({"ISSUE", "HUMAN"})
_PUBLIC_HEX = re.compile(r"[0-9a-f]{64}")


def lifecycle_message(ledger_id: str, position: int, prev: str, record: Mapping[str, Any]) -> bytes:
    """What the human gate signs: this ledger, this position after the head ``prev``, and the record."""

    identity = record_id({**record, "provenance": None})
    return f"ssds lifecycle {ledger_id} #{position} {prev} {identity}\n".encode("ascii")


def key_identity(role: Any, public_key: Any) -> str | None:
    """The identity a key of ``role`` with ``public_key`` has, or ``None`` when the key is not well formed."""

    if not isinstance(public_key, str):
        return None
    if role == "HUMAN":
        try:
            return human_key_id(public_key)
        except Exception:  # any malformed line is simply not a key (Manual §25.4)
            return None
    if _PUBLIC_HEX.fullmatch(public_key):
        return "ed25519:" + hashlib.sha256(bytes.fromhex(public_key)).hexdigest()
    return None


def lifecycle_problems(fields: Any, roots: TrustRoots, position: int) -> list[str]:
    """Why a ``KEY_LIFECYCLE`` record's fields cannot be admitted at ``position`` under ``roots``; none if it can."""

    if not isinstance(fields, Mapping) or fields.get("action") not in ACTIONS or not isinstance(fields.get("key"), Mapping):
        return ["a lifecycle record names an action and a key object"]
    action, key = fields["action"], fields["key"]
    role = key.get("role")
    if role not in ROLES:
        return [f"keys of role {role!r} do not change through this path yet"]
    problems = []
    shape = {"role", "id", "public_key"} | ({"retires"} if action == "ROTATE" else set())
    if set(key) != shape:
        problems.append(f"a {action} key object has exactly the fields {sorted(shape)}")
    kid = key.get("id")
    if not isinstance(kid, str) or key_identity(role, key.get("public_key")) != kid:
        return problems + ["the key's id is not its public key's identity"]  # nothing below reads an unhashable id
    allowed = {"action", "key"} | ({"outstanding"} if role == "ISSUE" and action in ("RETIRE", "ROTATE") else set()) \
        | ({"from_position"} if action == "COMPROMISED" else set())
    if set(fields) - allowed:
        problems.append(f"a {role} {action} carries only {sorted(allowed)}")
    if role == "ISSUE":
        in_force = roots.issue
        known = set(roots.issue) | set(roots.retired) | set(roots.compromised)
    else:
        in_force = roots.humans
        known = set(roots.humans) | set(roots.former_humans)
    if action in ("REGISTER", "ROTATE") and kid in known:
        problems.append(f"{kid} is already known; a new key has a new identity")
    if action == "ROTATE" and (not isinstance(key.get("retires"), str) or key["retires"] not in in_force):
        problems.append("a rotation retires a key in force")
    if action == "RETIRE":
        if in_force.get(kid) != key.get("public_key"):
            problems.append("a retirement names a key in force")
        elif role == "HUMAN" and set(in_force) == {kid}:
            problems.append("the last human key is never retired: rotate it")
    if action == "COMPROMISED":
        if kid not in known:
            problems.append("a compromise names a known key")
        start = fields.get("from_position", position)
        if not isinstance(start, int) or isinstance(start, bool) or not 0 <= start <= position:
            problems.append("a compromise's position is one the ledger has reached")
    return problems


__all__ = ["ACTIONS", "ROLES", "key_identity", "lifecycle_message", "lifecycle_problems"]
