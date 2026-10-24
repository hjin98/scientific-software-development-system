"""Trust roots in force at a position (Manual §25.2; catalogue §25.2): Dispatcher issue keys and human keys.

Read from the ledger alone: the genesis trust roots, then each admitted ``KEY_LIFECYCLE`` record in order. A
retired issue key keeps the envelopes its retirement lists verifiable for never-lost records (§8.3 step 3); a key
declared compromised is untrusted for envelopes it signed from the named position on.

Every action names its key by ``key.id``, and a rotation names the key it replaces by ``key.retires``, for every role
(Review e6ac009 B6). The reading is total: Admission admits only well-formed lifecycle records, and a stored value
this reader cannot read changes no trust root rather than raising (Manual §25.4).
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from ssds.ledger.read import human_key_id


@dataclass(frozen=True)
class TrustRoots:
    issue: dict[str, str] = field(default_factory=dict)  # issue key id -> Ed25519 public key (hex), in force
    retired: dict[str, tuple[str, frozenset[str]]] = field(default_factory=dict)  # id -> (public key, outstanding)
    compromised: dict[str, int] = field(default_factory=dict)  # id -> the position its signatures are untrusted from
    humans: dict[str, str] = field(default_factory=dict)  # actor id (human:SHA256:...) -> OpenSSH public key line
    former_humans: frozenset[str] = frozenset()  # human key ids retired, rotated away or compromised


def _human(public: Any) -> str | None:
    try:
        return human_key_id(public) if isinstance(public, str) else None
    except Exception:  # a malformed line is no key
        return None


def _keys(value: Any) -> list[Mapping[str, Any]]:
    return [k for k in value if isinstance(k, Mapping)] if isinstance(value, list) else []


def trust_roots(entries) -> TrustRoots:
    """The trust roots after the given admitted entries (positions 0 to n)."""

    issue: dict[str, str] = {}
    retired: dict[str, tuple[str, frozenset[str]]] = {}
    compromised: dict[str, int] = {}
    humans: dict[str, str] = {}
    former: set[str] = set()
    for item in entries:
        lifecycle = item.entry.get("lifecycle")
        fields = lifecycle.get("fields") if isinstance(lifecycle, Mapping) else None
        if not isinstance(fields, Mapping):
            continue
        if lifecycle.get("kind") == "GENESIS":
            roots = fields.get("trust_roots") if isinstance(fields.get("trust_roots"), Mapping) else {}
            for key in _keys(roots.get("dispatcher_keys")):
                if isinstance(key.get("id"), str) and isinstance(key.get("public_key"), str):
                    issue[key["id"]] = key["public_key"]
            for key in _keys(roots.get("human_keys")):
                if (hid := _human(key.get("public_key"))) is not None:
                    humans[hid] = key["public_key"]
            continue
        key, action = fields.get("key"), fields.get("action")
        if lifecycle.get("kind") != "KEY_LIFECYCLE" or not isinstance(key, Mapping):
            continue
        kid, public, gone = key.get("id"), key.get("public_key"), key.get("retires")
        if not isinstance(kid, str) or not isinstance(public, str):
            continue
        if key.get("role") == "ISSUE":
            if action in ("REGISTER", "ROTATE"):
                issue[kid] = public
            old = kid if action == "RETIRE" else gone if action == "ROTATE" else None
            if isinstance(old, str) and old in issue:
                outstanding = fields.get("outstanding")
                listed = frozenset(d for d in outstanding if isinstance(d, str)) if isinstance(outstanding, list) else frozenset()
                retired[old] = (issue.pop(old), listed)
            if action == "COMPROMISED":
                start = fields.get("from_position", item.position)
                compromised[kid] = start if isinstance(start, int) and not isinstance(start, bool) else 0
        elif key.get("role") == "HUMAN":
            if action in ("REGISTER", "ROTATE") and _human(public) == kid:
                humans[kid] = public
            old = kid if action in ("RETIRE", "COMPROMISED") else gone if action == "ROTATE" else None
            if isinstance(old, str) and old in humans:
                humans.pop(old)
                former.add(old)
            if action == "COMPROMISED":
                former.add(kid)
    return TrustRoots(issue, retired, compromised, humans, frozenset(former))


__all__ = ["TrustRoots", "trust_roots"]
