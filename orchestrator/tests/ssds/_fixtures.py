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


RESERVED_LEAVES = {
    "ssds.manifest": '''
[[unit]]
id = "ssds.manifest"
kind = "MANIFEST"
scope = [{ file = ".ssds/manifest.toml" }]
''',
    "ssds.policy": '''
[[unit]]
id = "ssds.policy"
kind = "POLICY"
scope = [{ file = ".ssds/policy.toml" }]
''',
    "ssds.unclassified": '''
[[unit]]
id = "ssds.unclassified"
kind = "UNCLASSIFIED"
scope = [{ prefix = "" }]
''',
}


def manifest(text: str, reserved: bool = True) -> bytes:
    """A manifest declaring ``text``'s units and, unless it declares them itself, the reserved leaves of Manual
    §1.8, so that fixture inputs conform to §1.8 and §1.9 (plan reading F18). ``reserved=False`` builds a
    manifest without them, for the cases that check the leaves themselves."""

    body = textwrap.dedent(text)
    if reserved:
        body += "".join(block for uid, block in RESERVED_LEAVES.items() if f'id = "{uid}"' not in body)
    return ("schema = 1\n" + body).encode("utf-8")


#: The ledger JSON form of a structure declaring only the reserved leaves of Manual §1.8 (plan reading F18).
GENESIS_STRUCTURE = {"units": {
    "ssds.manifest": {"kind": "MANIFEST", "role": "leaf", "scope": [{"file": ".ssds/manifest.toml"}], "subject": True},
    "ssds.policy": {"kind": "POLICY", "role": "leaf", "scope": [{"file": ".ssds/policy.toml"}], "subject": True},
    "ssds.unclassified": {"kind": "UNCLASSIFIED", "role": "leaf", "scope": [{"prefix": ""}], "subject": True}},
    "governed": {}}

def tree(files: dict[str, bytes | str | Entry], manifest_text: str | None = None, reserved: bool = True) -> Tree:
    entries: dict[str, Entry | bytes] = {}
    for path, value in files.items():
        entries[path] = value.encode("utf-8") if isinstance(value, str) else value
    if manifest_text is not None:
        entries[DEFAULT_MANIFEST_PATH] = manifest(manifest_text, reserved)
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
        "structure": structure or GENESIS_STRUCTURE,  # §1.8, A9: every genesis declares the reserved leaves
        "modes": modes or {},
        "baseline_commit": baseline,
        "deployment_class": "LOCAL_TRUST",
        "manifest_path": ".ssds/manifest.toml",
        "policy_path": ".ssds/policy.toml",
        "approval": approval or {"key_id": human_key_id(human_line), "signature": ""},
    }
    return record("GENESIS", target=None, actor="admission:" + host_key.key_id, actor_class="ADMISSION", fields=fields)


def approve(genesis: dict, private_key: Path) -> dict:
    from ssds.admission.genesis import genesis_approval_message
    from ssds.ledger.read import with_id

    signed = dict(genesis)
    signed["fields"] = dict(genesis["fields"])
    signed["fields"]["approval"] = {**genesis["fields"]["approval"], "signature": sshsig(private_key, genesis_approval_message(genesis))}
    return with_id(signed)


def entry(ledger_id: str, position: int, prev, key, *, kind="LIFECYCLE", lifecycle=None, records=(), obs=None,
          admission=None, absorption=None) -> dict:
    return {"ledger_id": ledger_id, "position": position, "schema": 1, "prev": prev, "entry_kind": kind,
            "host_key_id": key.key_id, "incarnation_id": "incarnation-1", "obs": obs, "admission": admission,
            "absorption": absorption, "lifecycle": lifecycle, "records": list(records)}


# -- derivation fixtures: an authenticated chain as derivation receives it -------------------

def chain_of(ledger_id: str, entries: list[dict], objects: dict[int, dict[str, bytes]] | None = None):
    """A verified chain built in memory: derivation's input once the Ledger Store has authenticated it."""

    from ssds.core.api.v1 import canonical_json
    from ssds.ledger.read import Chain, LedgerEntry

    from ssds.ledger.schema import record_violations

    out = []
    for position, body in enumerate(entries):
        for rec in list(body.get("records") or []) + ([body["lifecycle"]] if body.get("lifecycle") else []):
            problems = record_violations(rec)
            if problems:  # derivation only ever reads records the Ledger Store authenticated under the closed schema
                raise AssertionError(f"schema: {rec.get('kind')}: {problems}")
        data = canonical_json(body)
        out.append(LedgerEntry(position, f"{position:040x}", (), body, data, b"", f"sha256:{position:064x}",
                               (objects or {}).get(position, {})))
    return Chain(ledger_id, tuple(out))


#: The fixtures' designated runner key, a runner trust root at every scenario's genesis (Phase F step 9c-ii-i, F89).
RUNNER_KEY = "ed25519:test"
RUNNER_ROOT = {"id": RUNNER_KEY, "public_key": "00" * 32}


def genesis_body(baseline: str, structure: dict, modes: dict | None = None, ruleset: dict | None = None,
                 manifest_path: str = ".ssds/manifest.toml") -> dict:
    fields = {
        "project": "demo", "ledger_id": "demo", "location": {}, "trust_roots": {"admission_keys": [], "runner_keys": [RUNNER_ROOT]},
        "witnesses": {}, "structure": structure, "modes": modes or {}, "baseline_commit": baseline,
        "deployment_class": "LOCAL_TRUST", "manifest_path": manifest_path, "policy_path": ".ssds/policy.toml",
        "approval": {},
    }
    genesis = record("GENESIS", target=None, actor="admission:ed25519:test", actor_class="ADMISSION", fields=fields)
    if ruleset:
        from ssds.ledger.read import with_id

        genesis = with_id({k: v for k, v in dict(genesis, ruleset=ruleset).items() if k != "id"})
    return {"ledger_id": "demo", "position": 0, "schema": 1, "prev": None, "entry_kind": "LIFECYCLE",
            "host_key_id": "ed25519:test", "incarnation_id": "i", "obs": None, "admission": None, "absorption": None,
            "lifecycle": genesis, "records": []}


def admission_body(position: int, base: str, admitted: str, records=(), deltas=(), integrates=None,
                   decision: str = "ACCEPT") -> dict:
    return {"ledger_id": "demo", "position": position, "schema": 1, "prev": f"sha256:{position - 1:064x}",
            "entry_kind": "ADMISSION", "host_key_id": "ed25519:test", "incarnation_id": "i", "obs": base,
            "admission": {"request_id": "sha256:" + f"{position:064x}", "decision": decision, "reasons": [],
                          "base_commit": base, "admitted_commit": admitted, "adopted_deltas": list(deltas),
                          "integrates": integrates, "refused": []},
            "absorption": None, "lifecycle": None, "records": list(records)}


def lifecycle_body(position: int, lifecycle: dict, obs=None) -> dict:
    return {"ledger_id": "demo", "position": position, "schema": 1, "prev": f"sha256:{position - 1:064x}",
            "entry_kind": "LIFECYCLE", "host_key_id": "ed25519:test", "incarnation_id": "i", "obs": obs,
            "admission": None, "absorption": None, "lifecycle": lifecycle, "records": []}


def absorption_body(position: int, observed: str) -> dict:
    return {"ledger_id": "demo", "position": position, "schema": 1, "prev": f"sha256:{position - 1:064x}",
            "entry_kind": "ABSORPTION", "host_key_id": "ed25519:test", "incarnation_id": "i", "obs": observed,
            "admission": None, "absorption": {"fence": None}, "lifecycle": None, "records": []}


def commit_id(name: str) -> str:
    import hashlib

    return hashlib.sha1(name.encode()).hexdigest()
