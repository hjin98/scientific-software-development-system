"""Task envelopes, issue keys and launch attestations (Manual §12.2, §25.1-§25.2; catalogue §12.2).

The Dispatcher signs every task's envelope with an issue key held only in private operator state (the SSDS home,
``keys/dispatcher/<ledger id>.ed25519``, under the SD-59 boundary). On a harness route it also starts the task's
fresh session with a per-task submission credential, an Ed25519 key of its own, and signs a launch attestation
naming the session, the sessions of the task's inputs and the credential's public key: a request signed by that
credential carries lineage ``ATTESTED_FRESH``. On manual and Git-envelope routes the session is not observed, and
lineage is ``UNKNOWN`` unless a human attests it. No secret enters the ledger: the credential's private key stays
with the session.
"""

from __future__ import annotations

import hashlib
import os
import secrets
import stat
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, PrivateFormat, PublicFormat

from ssds.admission.request import ROUTES, attestation_message, envelope_message, request_message


def _public_hex(key: Ed25519PrivateKey) -> str:
    return key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw).hex()


def key_id(public_hex: str) -> str:
    """The issue key's identity: the same form as an Admission host key's (§25.2)."""

    return "ed25519:" + hashlib.sha256(bytes.fromhex(public_hex)).hexdigest()


class IssueKeyRefused(RuntimeError):
    """The issue key file is not private operator state (SD-59)."""


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
    """The Dispatcher's issue key for one ledger."""

    def __init__(self, home_root: Path, ledger_id: str) -> None:
        self.path = Path(home_root) / "keys" / "dispatcher" / f"{ledger_id}.ed25519"
        self._key = self._load_or_create()

    def _load_or_create(self) -> Ed25519PrivateKey:
        directory = self.path.parent
        for part in (directory.parent, directory, self.path):
            if part.is_symlink():
                raise IssueKeyRefused(f"{part} is a symbolic link")
        if self.path.exists():
            mode = stat.S_IMODE(self.path.stat().st_mode)
            if mode & 0o077:
                raise IssueKeyRefused(f"{self.path} is readable by others ({oct(mode)})")
            return Ed25519PrivateKey.from_private_bytes(self.path.read_bytes())
        directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        key = Ed25519PrivateKey.generate()
        fd = os.open(self.path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "wb") as handle:
            handle.write(key.private_bytes(Encoding.Raw, PrivateFormat.Raw, NoEncryption()))
        return key

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
              predecessors: Mapping[str, Any] | None = None) -> Issued:
        if route not in ROUTES:
            raise ValueError(f"route {route!r} is not one of {sorted(ROUTES)}")
        harness = route == "HARNESS"
        envelope = {"task_id": task_id, "obligation_id": obligation_id, "role": role,
                    "contract_revision": contract_revision, "governs": dict(governs), "route": route,
                    "lineage_class": "ATTESTED_FRESH" if harness else "UNKNOWN", "input_sessions": list(input_sessions),
                    "issued_at_position": issued_at_position, "issue_key_id": self.key_id,
                    "predecessors": dict(predecessors) if predecessors else None}
        signature = self._key.sign(envelope_message(envelope)).hex()
        if not harness:
            return Issued(envelope, signature, None, None, None)
        credential = TaskCredential(Ed25519PrivateKey.generate())
        attestation = {"task_id": task_id, "session": "session:" + secrets.token_hex(16),
                       "input_sessions": list(input_sessions), "credential_key": credential.public_hex}
        return Issued(envelope, signature, attestation, self._key.sign(attestation_message(attestation)).hex(), credential)


__all__ = ["IssueKeyRefused", "Issued", "Issuer", "TaskCredential", "key_id"]
