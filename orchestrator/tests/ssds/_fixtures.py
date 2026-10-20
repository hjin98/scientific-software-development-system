"""Shared fixtures for SSDS tests: in-memory trees with a manifest, and real Git repositories."""

from __future__ import annotations

import os
import subprocess
import tempfile
import textwrap
from pathlib import Path

from ssds.content import DEFAULT_MANIFEST_PATH, Entry, Manifest, Structure, Tree, TreeView, parse_manifest

GIT_ENV = {
    **os.environ,
    "GIT_AUTHOR_NAME": "ssds-test",
    "GIT_AUTHOR_EMAIL": "ssds-test@example.invalid",
    "GIT_COMMITTER_NAME": "ssds-test",
    "GIT_COMMITTER_EMAIL": "ssds-test@example.invalid",
    "GIT_CONFIG_GLOBAL": os.devnull,
    "GIT_CONFIG_SYSTEM": os.devnull,
    "LC_ALL": "C",
}


def manifest(text: str) -> bytes:
    return ("schema = 1\n" + textwrap.dedent(text)).encode("utf-8")


def tree(files: dict[str, bytes | str | Entry], manifest_text: str | None = None) -> Tree:
    entries: dict[str, Entry | bytes] = {}
    for path, value in files.items():
        entries[path] = value.encode("utf-8") if isinstance(value, str) else value
    if manifest_text is not None:
        entries[DEFAULT_MANIFEST_PATH] = manifest(manifest_text)
    return Tree(entries)


def structure_of(t: Tree) -> Structure:
    parsed = parse_manifest(t[DEFAULT_MANIFEST_PATH].data)
    assert isinstance(parsed, Manifest), parsed
    return Structure(parsed.decl)


def view(t: Tree) -> TreeView:
    """The tree under the structure its own manifest declares."""

    return TreeView(t, structure_of(t))


def git(root: Path, *args: str, data: bytes | None = None) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args], input=data, capture_output=True, env=GIT_ENV, check=True
    )
    return result.stdout.decode("utf-8").strip()


def init_repo(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    git(root, "init", "--quiet", "--initial-branch=main")
    return root


def commit(root: Path, message: str = "change") -> str:
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "--allow-empty", "-m", message)
    return git(root, "rev-parse", "HEAD")


# -- ledger fixtures ----------------------------------------------------------------------

RULESET = {"system": "ssds-rules/1", "policy": "sha256:" + "0" * 64, "analyzers": "sha256:" + "1" * 64}


def human_key(directory: Path, name: str = "approver") -> tuple[Path, str]:
    """A fresh OpenSSH Ed25519 key pair; returns the private key path and the public key line."""

    path = directory / name
    subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-C", name, "-f", str(path)], check=True,
                   stdin=subprocess.DEVNULL, timeout=60)
    return path, (path.with_suffix(".pub")).read_text().strip()


def sshsig(private_key: Path, message: bytes, namespace: str = "ssds") -> str:
    """What the human runs: ``ssh-keygen -Y sign -f <key> -n ssds <file>``."""

    folder = Path(tempfile.mkdtemp(dir=private_key.parent))
    target = folder / "message.txt"
    target.write_bytes(message)
    subprocess.run(["ssh-keygen", "-q", "-Y", "sign", "-f", str(private_key), "-n", namespace, str(target)],
                   check=True, capture_output=True, stdin=subprocess.DEVNULL, timeout=60)
    return (folder / "message.txt.sig").read_text()


def record(kind: str, *, target, outcome=None, actor="human:SHA256:test", actor_class="HUMAN", frame="ADMITTED",
           basis=(), fields=None, supersedes=(), reason=()) -> dict:
    from ssds.ledger.read import with_id

    return with_id({
        "kind": kind, "schema": 1, "ruleset": dict(RULESET), "actor": actor, "actor_class": actor_class,
        "frame": frame, "target": target, "basis": list(basis), "outcome": outcome, "reason": list(reason),
        "supersedes": list(supersedes), "binding": None, "governs": {"mode": "LEGACY", "protocol": "7.2.1"},
        "provenance": None, "refs": [], "recorded_at": "2026-10-19T00:00:00Z", "fields": dict(fields or {}),
    })


def genesis_record(host_key, human_line: str, witness_root: Path, baseline: str, *, modes=None,
                   structure=None, approval=None, ledger_id: str = "demo") -> dict:
    from ssds.ledger.signatures import human_key_id

    fields = {
        "project": "demo-project",
        "ledger_id": ledger_id,
        "location": {"repository": "ssds-home:ledgers/" + ledger_id, "ref": "refs/ssds/ledger/" + ledger_id},
        "trust_roots": {"admission_keys": [{"id": host_key.key_id, "public_key": host_key.public_hex}],
                        "dispatcher_keys": [], "human_mechanism": "SSHSIG",
                        "human_keys": [{"id": human_key_id(human_line), "public_key": human_line}]},
        "witnesses": {"class": "LOCAL_TRUST", "N": 1, "q_a": 1, "r": 1, "f": 0,
                      "witnesses": [{"id": "w1", "kind": "FILE", "location": str(witness_root)}]},
        "structure": structure or {"units": {}, "governed": {}},
        "modes": modes or {},
        "baseline_commit": baseline,
        "deployment_class": "LOCAL_TRUST",
        "manifest_path": ".ssds/manifest.toml",
        "policy_path": ".ssds/policy.toml",
        "approval": approval or {"key_id": human_key_id(human_line), "signature": ""},
    }
    return record("GENESIS", target=None, actor="admission:" + host_key.key_id, actor_class="ADMISSION", fields=fields)


def approve(genesis: dict, private_key: Path) -> dict:
    from ssds.ledger.read import genesis_approval_message, with_id

    signed = dict(genesis)
    signed["fields"] = dict(genesis["fields"])
    signed["fields"]["approval"] = {**genesis["fields"]["approval"], "signature": sshsig(private_key, genesis_approval_message(genesis))}
    return with_id(signed)


def entry(ledger_id: str, position: int, prev, key, *, kind="LIFECYCLE", lifecycle=None, records=(), obs=None,
          admission=None, absorption=None) -> dict:
    return {"ledger_id": ledger_id, "position": position, "schema": 1, "prev": prev, "entry_kind": kind,
            "host_key_id": key.key_id, "incarnation_id": "incarnation-1", "obs": obs, "admission": admission,
            "absorption": absorption, "lifecycle": lifecycle, "records": list(records)}
