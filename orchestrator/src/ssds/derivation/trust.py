"""Trust roots in force at a position (Manual §25.2; catalogue §25.2): Dispatcher issue keys and human keys.

Read from the ledger alone: the genesis trust roots, then each admitted ``KEY_LIFECYCLE`` record in order. A
retired issue key keeps the envelopes its retirement lists verifiable for never-lost records (§8.3 step 3); a key
declared compromised is untrusted for envelopes it signed from the named position on.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ssds.ledger.read import human_key_id


@dataclass(frozen=True)
class TrustRoots:
    issue: dict[str, str] = field(default_factory=dict)  # issue key id -> Ed25519 public key (hex), in force
    retired: dict[str, tuple[str, frozenset[str]]] = field(default_factory=dict)  # id -> (public key, outstanding)
    compromised: dict[str, int] = field(default_factory=dict)  # id -> the position its signatures are untrusted from
    humans: dict[str, str] = field(default_factory=dict)  # actor id (human:SHA256:...) -> OpenSSH public key line


def trust_roots(entries) -> TrustRoots:
    """The trust roots after the given admitted entries (positions 0 to n)."""

    issue: dict[str, str] = {}
    retired: dict[str, tuple[str, frozenset[str]]] = {}
    compromised: dict[str, int] = {}
    humans: dict[str, str] = {}
    for item in entries:
        lifecycle = item.entry.get("lifecycle")
        if not lifecycle:
            continue
        fields = lifecycle["fields"]
        if lifecycle["kind"] == "GENESIS":
            roots = fields["trust_roots"]
            for key in roots.get("dispatcher_keys", []):
                issue[key["id"]] = key["public_key"]
            for key in roots.get("human_keys", []):
                humans[human_key_id(key["public_key"])] = key["public_key"]
        elif lifecycle["kind"] == "KEY_LIFECYCLE":
            key, action = fields["key"], fields["action"]
            role = key.get("role")
            if role == "ISSUE":
                if action in ("REGISTER", "ROTATE"):
                    issue[key["id"]] = key["public_key"]
                if action in ("RETIRE", "ROTATE"):
                    gone = key["id"] if action == "RETIRE" else key.get("retires")
                    if gone in issue:
                        retired[gone] = (issue.pop(gone), frozenset(fields.get("outstanding") or ()))
                if action == "COMPROMISED":
                    compromised[key["id"]] = fields.get("from_position", item.position)
            elif role == "HUMAN" and action == "REGISTER":
                humans[human_key_id(key["public_key"])] = key["public_key"]
            elif role == "HUMAN" and action in ("RETIRE", "COMPROMISED"):
                humans.pop(human_key_id(key["public_key"]), None)
    return TrustRoots(issue, retired, compromised, humans)


__all__ = ["TrustRoots", "trust_roots"]
