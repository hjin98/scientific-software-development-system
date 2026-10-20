"""Ed25519 entry and checkpoint signatures, and human approvals in the SSH signature format (catalogue §21.2, §23.2, §25.1).

An Admission host key signs ``"ssds.entry.v1" ‖ sha256(entry.json)`` and each
checkpoint. A human authenticates with a registered OpenSSH Ed25519 key,
signing in OpenSSH's ``SSHSIG`` format under the namespace ``ssds``, which
``ssh-keygen -Y sign -n ssds`` produces; the private key never leaves its
holder.
"""

from __future__ import annotations

import base64
import hashlib
import struct

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, PrivateFormat, PublicFormat

ENTRY_DOMAIN = b"ssds.entry.v1"
CHECKPOINT_DOMAIN = b"ssds.checkpoint.v1"
SSH_NAMESPACE = "ssds"
_SSHSIG_MAGIC = b"SSHSIG"


class SignatureError(ValueError):
    """A signature or key outside what the trust roots accept."""


def host_key_id(public_key: bytes) -> str:
    return "ed25519:" + hashlib.sha256(public_key).hexdigest()


def verify_host(public_key_hex: str, message: bytes, signature: bytes) -> bool:
    try:
        Ed25519PublicKey.from_public_bytes(bytes.fromhex(public_key_hex)).verify(signature, message)
    except (InvalidSignature, ValueError):
        return False
    return True


def entry_message(entry_json: bytes) -> bytes:
    return ENTRY_DOMAIN + hashlib.sha256(entry_json).digest()


class HostKey:
    """An Admission host signing key, held only in private operator state."""

    def __init__(self, private_key: Ed25519PrivateKey) -> None:
        self._key = private_key

    @classmethod
    def generate(cls) -> HostKey:
        return cls(Ed25519PrivateKey.generate())

    @classmethod
    def from_private_bytes(cls, raw: bytes) -> HostKey:
        return cls(Ed25519PrivateKey.from_private_bytes(raw))

    @property
    def public_hex(self) -> str:
        return self._key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw).hex()

    @property
    def key_id(self) -> str:
        return host_key_id(bytes.fromhex(self.public_hex))

    def sign(self, message: bytes) -> bytes:
        return self._key.sign(message)

    def private_bytes(self) -> bytes:
        return self._key.private_bytes(Encoding.Raw, PrivateFormat.Raw, NoEncryption())


# -- OpenSSH keys and SSHSIG --------------------------------------------------------------


def _read_string(data: bytes, offset: int) -> tuple[bytes, int]:
    if offset + 4 > len(data):
        raise SignatureError("truncated SSH wire string")
    (length,) = struct.unpack(">I", data[offset : offset + 4])
    end = offset + 4 + length
    if end > len(data):
        raise SignatureError("truncated SSH wire string")
    return data[offset + 4 : end], end


def _string(value: bytes) -> bytes:
    return struct.pack(">I", len(value)) + value


def parse_openssh_ed25519(line: str) -> bytes:
    """The SSH wire blob of an ``ssh-ed25519 AAAA... [comment]`` public key line."""

    parts = line.strip().split()
    if len(parts) < 2 or parts[0] != "ssh-ed25519":
        raise SignatureError("only ssh-ed25519 human keys are accepted")
    blob = base64.b64decode(parts[1], validate=True)
    kind, offset = _read_string(blob, 0)
    raw, offset = _read_string(blob, offset)
    if kind != b"ssh-ed25519" or len(raw) != 32 or offset != len(blob):
        raise SignatureError("malformed ssh-ed25519 key")
    return blob


def human_key_id(public_key_line: str) -> str:
    """``human:SHA256:<base64>``, the OpenSSH fingerprint of the key (catalogue §25.1)."""

    blob = parse_openssh_ed25519(public_key_line)
    fingerprint = base64.b64encode(hashlib.sha256(blob).digest()).decode("ascii").rstrip("=")
    return f"human:SHA256:{fingerprint}"


def verify_sshsig(public_key_line: str, message: bytes, armored: str, namespace: str = SSH_NAMESPACE) -> bool:
    """Whether ``armored`` is an SSHSIG by that key over ``message`` under ``namespace``."""

    try:
        expected_blob = parse_openssh_ed25519(public_key_line)
        lines = [ln.strip() for ln in armored.strip().splitlines()]
        if not lines or lines[0] != "-----BEGIN SSH SIGNATURE-----" or lines[-1] != "-----END SSH SIGNATURE-----":
            return False
        blob = base64.b64decode("".join(lines[1:-1]), validate=True)
        if not blob.startswith(_SSHSIG_MAGIC):
            return False
        offset = len(_SSHSIG_MAGIC)
        (version,) = struct.unpack(">I", blob[offset : offset + 4])
        offset += 4
        public_blob, offset = _read_string(blob, offset)
        signed_namespace, offset = _read_string(blob, offset)
        reserved, offset = _read_string(blob, offset)
        hash_algorithm, offset = _read_string(blob, offset)
        signature_blob, offset = _read_string(blob, offset)
        if version != 1 or offset != len(blob) or public_blob != expected_blob:
            return False
        if signed_namespace != namespace.encode() or hash_algorithm not in (b"sha256", b"sha512"):
            return False
        digest = (hashlib.sha512 if hash_algorithm == b"sha512" else hashlib.sha256)(message).digest()
        signed = (_SSHSIG_MAGIC + _string(namespace.encode()) + _string(reserved) + _string(hash_algorithm)
                  + _string(digest))
        sig_kind, sig_offset = _read_string(signature_blob, 0)
        sig_raw, sig_offset = _read_string(signature_blob, sig_offset)
        if sig_kind != b"ssh-ed25519" or sig_offset != len(signature_blob):
            return False
        raw_key, _ = _read_string(expected_blob, _read_string(expected_blob, 0)[1])
        Ed25519PublicKey.from_public_bytes(raw_key).verify(sig_raw, signed)
    except (SignatureError, InvalidSignature, ValueError, struct.error):
        return False
    return True
