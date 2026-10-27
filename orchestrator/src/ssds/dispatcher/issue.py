"""Task envelopes, issue keys and launch attestations (Manual §12.2, §25.1-§25.2; catalogue §12.2).

The Dispatcher signs every task's envelope with an issue key held only in private operator state (the SSDS home,
``keys/dispatcher/<ledger id>.ed25519``, under the SD-59 boundary). On a harness route it also starts the task's
fresh session with a per-task submission credential, an Ed25519 key of its own, and signs a launch attestation
naming the task's envelope, the session, the sessions of the task's inputs and the credential's public key: a request
signed by that credential carries lineage ``ATTESTED_FRESH``. On manual and Git-envelope routes the session is not
observed, and lineage is ``UNKNOWN`` unless a human attests it. No secret enters the ledger: the credential's
private key stays with the session.
"""

from __future__ import annotations

import hashlib
import secrets
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, PrivateFormat, PublicFormat

from ssds.admission.request import ROUTES, attestation_message, envelope_digest, envelope_message, request_message
from ssds.interface.render import brief_digest
from ssds.ledger.qualification import Home

from .home import DispatcherHome


def _public_hex(key: Ed25519PrivateKey) -> str:
    return key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw).hex()


def key_id(public_hex: str) -> str:
    """The issue key's identity: the same form as an Admission host key's (§25.2)."""

    return "ed25519:" + hashlib.sha256(bytes.fromhex(public_hex)).hexdigest()


@dataclass
class TaskCredential:
    """A task's per-task submission credential: signs that task's requests (§12.2)."""

    key: Ed25519PrivateKey

    @property
    def public_hex(self) -> str:
        return _public_hex(self.key)

    def sign(self, request: Mapping[str, Any]) -> str:
        return self.key.sign(request_message(request)).hex()


@dataclass(frozen=True)
class Issued:
    envelope: dict[str, Any]
    signature: str
    attestation: dict[str, Any] | None
    attestation_signature: str | None
    credential: TaskCredential | None

    def binding(self, request: Mapping[str, Any] | None = None) -> dict[str, Any]:
        """The request's task binding; on a harness route, signed by the task's credential over ``request``."""

        return {"envelope": self.envelope, "signature": self.signature, "attestation": self.attestation,
                "attestation_signature": self.attestation_signature,
                "credential_signature": self.credential.sign(request) if self.credential and request is not None else None}


class Issuer:
    """The Dispatcher's issue key for one ledger, in the SSDS home's checked operator tree (Review e6ac009 B7)."""

    def __init__(self, home: Home, ledger_id: str) -> None:
        self.home = DispatcherHome(home.root)
        self.home.check(ledger_id)
        self.parts = self.home.issue_key_parts(ledger_id)
        self.path = self.home.path(self.parts)
        self._key = self._load_or_create()

    def _load_or_create(self) -> Ed25519PrivateKey:
        data = self.home.read_private(self.parts)
        if data is None:
            self.home.create_private(self.parts, Ed25519PrivateKey.generate().private_bytes(
                Encoding.Raw, PrivateFormat.Raw, NoEncryption()))
            data = self.home.read_private(self.parts)  # whichever creation won (concurrent first use)
        return Ed25519PrivateKey.from_private_bytes(data)

    @property
    def public_hex(self) -> str:
        return _public_hex(self._key)

    @property
    def key_id(self) -> str:
        return key_id(self.public_hex)

    def trust_root(self) -> dict[str, str]:
        """The key as a genesis ``dispatcher_keys`` entry or a ``KEY_LIFECYCLE`` key (role ``ISSUE``)."""

        return {"id": self.key_id, "public_key": self.public_hex, "role": "ISSUE"}

    def issue(self, *, task_id: str, obligation_id: str, role: str, contract_revision: Any, governs: Mapping[str, Any],
              route: str, issued_at_position: int, input_sessions: Sequence[str] = (),
              predecessors: Mapping[str, Any] | None = None, brief: bytes | None = None) -> Issued:
        """Sign the task's envelope. ``brief`` is the rendered brief the task is given: its content identity is
        recorded in the envelope, so the doctrine text the agent received is recoverable exactly (§16.4)."""

        if route not in ROUTES:
            raise ValueError(f"route {route!r} is not one of {sorted(ROUTES)}")
        harness = route == "HARNESS"
        envelope = {"task_id": task_id, "obligation_id": obligation_id, "role": role,
                    "contract_revision": contract_revision, "governs": dict(governs), "route": route,
                    "lineage_class": "ATTESTED_FRESH" if harness else "UNKNOWN", "input_sessions": list(input_sessions),
                    "issued_at_position": issued_at_position, "issue_key_id": self.key_id,
                    "predecessors": dict(predecessors) if predecessors else None,
                    "brief": brief_digest(brief) if brief is not None else None}
        signature = self._key.sign(envelope_message(envelope)).hex()
        if not harness:
            return Issued(envelope, signature, None, None, None)
        credential = TaskCredential(Ed25519PrivateKey.generate())
        attestation = {"task_id": task_id, "envelope": envelope_digest(envelope),
                       "session": "session:" + secrets.token_hex(16), "input_sessions": list(input_sessions),
                       "credential_key": credential.public_hex}
        return Issued(envelope, signature, attestation, self._key.sign(attestation_message(attestation)).hex(), credential)


__all__ = ["Issued", "Issuer", "TaskCredential", "key_id"]
