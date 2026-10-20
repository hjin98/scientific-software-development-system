"""Admission's genesis path (Manual §19.9; catalogue §19.9, §21.3, §22.4, §23.3).

Procedure: build the genesis entry and ``Σ_0`` in an isolated workspace in the
SSDS home; validate every declaration, static check, trust root and witness
reachability; obtain the human gate; append and admit the entry under its own
quorum; only then is the ledger an identity derivation may read as current. A
genesis that fails validation publishes nothing.

A shadow genesis declares every subject ``LEGACY(p)`` or ``UNGOVERNED``, a
witness model meeting ``q_a + r > N + f``, and carries the human gate: an SSH
signature, by a registered human key under namespace ``ssds``, over one line
naming the genesis digest. The human holds that key; Admission never sees it.

Operator data lives in the SSDS home (Manual §26.3): the dedicated ledger
repository (catalogue §21.5 option (ii)), the file witness, the Admission host
key, the high-water mark and the genesis workspace. Nothing is written to the
product repository, whose baseline commit is only read.
"""

from __future__ import annotations

import hashlib
import json
import os
import secrets
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ssds.core.api.v1 import canonical_json
from ssds.derivation import Policy, baseline_structure
from ssds.ledger.append import HostKey, append_entry, create_ledger_repository, import_commits, write_checkpoint
from ssds.ledger.qualification import FileWitness, HighWaterMark, HighWaterStore, WitnessModel, qualify
from ssds.ledger.read import (
    SYSTEM_RULESET,
    entry_violations,
    human_key_id,
    ledger_head,
    ledger_ref,
    read_chain,
    is_unit,
    record_violations,
    verify_sshsig,
    with_id,
)

SHADOW_MODES = ("LEGACY", "UNGOVERNED")
DEFAULT_POLICY = b"schema = 1\n"
#: The analyzer set the system ruleset pins (catalogue §5.9), recorded with the genesis by digest.
SYSTEM_ANALYZERS = ("ssds.analyzer.python/1",)


# -- the genesis record's own checks --------------------------------------------------------------


def genesis_violations(genesis: Mapping[str, Any]) -> list[str]:
    """The genesis record's own checks: shadow modes, the witness model, the human approval (catalogue §19.9)."""

    problems: list[str] = []
    fields = genesis["fields"]
    for subject, mode in fields["modes"].items():
        if mode.get("mode") not in SHADOW_MODES:
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


# -- the SSDS home layout ------------------------------------------------------------------------------


class Home:
    """Where Admission keeps a project's operator data, under the SSDS home (created on first write).

    Every path it hands out is checked first: the ledger id must be a unit
    identity (catalogue §1.1) and the resolved path, symbolic links followed,
    must stay inside the resolved home, so no input can direct a write
    outside it.
    """

    def __init__(self, root: Path) -> None:
        if not root.is_absolute():
            raise ValueError("the SSDS home is an absolute directory")
        self.root = root

    @staticmethod
    def check_ledger_id(ledger_id: str) -> None:
        if not is_unit(ledger_id):
            raise HomeRefused(f"{ledger_id!r} is not a ledger id: lowercase dot-separated segments of [a-z0-9_-]")

    def _inside(self, *parts: str) -> Path:
        path = self.root.joinpath(*parts)
        if not path.resolve().is_relative_to(self.root.resolve()):
            raise HomeRefused(f"{path} resolves outside the SSDS home {self.root}")
        return path

    def ledger_repository(self, ledger_id: str) -> Path:
        self.check_ledger_id(ledger_id)
        return self._inside("ledgers", f"{ledger_id}.git")

    @property
    def witness_root(self) -> Path:
        return self._inside("witness")

    def admission_key(self, ledger_id: str) -> Path:
        self.check_ledger_id(ledger_id)
        return self._inside("keys", "admission", f"{ledger_id}.ed25519")

    def workspace(self, ledger_id: str) -> Path:
        self.check_ledger_id(ledger_id)
        return self._inside("genesis", ledger_id)

    def high_water(self, ledger_id: str) -> HighWaterStore:
        self.check_ledger_id(ledger_id)
        return HighWaterStore(self._inside("state", ledger_id, "high-water.json"))

    def check(self, ledger_id: str) -> None:
        """Refuse before any filesystem effect: every path this ledger would use stays in the home."""

        self.ledger_repository(ledger_id), self.witness_root, self.admission_key(ledger_id)
        self.workspace(ledger_id), self.high_water(ledger_id)


class HomeRefused(ValueError):
    """An input that would place operator data outside the SSDS home."""


def _write_private(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        os.write(descriptor, data)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _host_key(home: Home, ledger_id: str) -> HostKey:
    """The project's Admission host key, held only in private operator state (catalogue §23.2)."""

    path = home.admission_key(ledger_id)
    if path.is_file():
        return HostKey.from_private_bytes(path.read_bytes())
    key = HostKey.generate()
    _write_private(path, key.private_bytes())
    return key


# -- preparing a genesis -------------------------------------------------------------------------------


TreeSource = Callable[[str], Mapping[str, Any]]


@dataclass(frozen=True)
class GenesisSpec:
    """What a genesis declares; Admission fills in trust roots, witnesses, ruleset and ``Σ_0``."""

    project: str
    ledger_id: str
    product_repository: Path
    baseline_commit: str
    human_keys: tuple[str, ...]  # OpenSSH ssh-ed25519 public key lines: the human authentication trust roots
    protocol: str  # the document-controlled protocol p the shadow genesis is taken under (its ``governs``)
    modes: Mapping[str, Mapping[str, Any]]  # per subject, and "*" for subjects declared later
    manifest_path: str = ".ssds/manifest.toml"
    policy_path: str = ".ssds/policy.toml"
    deployment_class: str = "LOCAL_TRUST"
    recorded_at: str | None = None  # default: now, in UTC


@dataclass(frozen=True)
class Prepared:
    ledger_id: str
    genesis: dict[str, Any] | None  # the record without approval; None when validation refused it
    digest: str | None
    message: bytes | None  # the exact bytes the human signs
    problems: tuple[str, ...]
    findings: tuple[str, ...]
    workspace: Path | None  # None when the ledger id itself was refused: nothing was written
    report: Path | None

    @property
    def valid(self) -> bool:
        return not self.problems


def prepare_genesis(spec: GenesisSpec, home: Home, trees: TreeSource) -> Prepared:
    """Build and validate the genesis in its isolated workspace; publishes nothing.

    The workspace holds the proposal, the approval message and a validation
    report. Nothing is appended; the ledger repository is not created.
    """

    try:
        home.check(spec.ledger_id)
    except HomeRefused as refused:
        return Prepared(spec.ledger_id, None, None, None, (str(refused),), (), None, None)
    workspace = home.workspace(spec.ledger_id)
    problems: list[str] = []
    findings: list[str] = []
    repository = home.ledger_repository(spec.ledger_id)
    if repository.exists() and ledger_head(repository, spec.ledger_id) is not None:
        problems.append(f"ledger {spec.ledger_id} already exists at {repository}")
    try:
        tree = trees(spec.baseline_commit)
    except (KeyError, ValueError, OSError, RuntimeError) as exc:
        tree = None
        problems.append(f"the baseline commit {spec.baseline_commit} cannot be read: {exc}")
    structure: dict[str, Any] | None = None
    policy = DEFAULT_POLICY
    if tree is not None:
        baseline = baseline_structure(tree, spec.manifest_path)  # type: ignore[arg-type]
        problems.extend(baseline.problems)
        findings.extend(baseline.findings)
        structure = baseline.structure
        declared = set(baseline.subjects)
        for subject in spec.modes:
            if subject != "*" and subject not in declared:
                problems.append(f"a mode names {subject}, which the manifest does not declare as a subject")
        if "*" not in spec.modes:
            missing = sorted(declared - set(spec.modes))
            if missing:
                problems.append(f"no mode for {', '.join(missing)} and no default mode \"*\"")
        entry = tree.get(spec.policy_path)
        if entry is not None:
            policy = entry.data
    for subject, mode in spec.modes.items():
        if mode.get("mode") not in SHADOW_MODES:
            problems.append(f"shadow genesis declares {subject} {mode.get('mode')}; only LEGACY or UNGOVERNED")
        if mode.get("mode") == "LEGACY" and not mode.get("protocol"):
            problems.append(f"LEGACY mode of {subject} names no protocol p")
    try:
        Policy.parse(policy)
    except (ValueError, UnicodeDecodeError) as exc:
        problems.append(f"policy: {exc}")
    humans = []
    for line in spec.human_keys:
        try:
            humans.append({"id": human_key_id(line), "public_key": line.strip()})
        except (ValueError, IndexError) as exc:
            problems.append(f"human key: {exc}")
    if not humans:
        problems.append("genesis registers no human key for its gate")
    witness = FileWitness(home.witness_root)
    model = WitnessModel.from_json({"class": spec.deployment_class, "N": 1, "q_a": 1, "r": 1, "f": 0,
                                    "witnesses": [{"id": "local-file", "kind": "FILE",
                                                   "location": str(home.witness_root)}]})
    try:
        model.validate()
    except ValueError as exc:
        problems.append(f"witness model: {exc}")
    try:
        home.witness_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    except OSError as exc:
        problems.append(f"witness unreachable: {exc}")
    held = witness.read(spec.ledger_id)
    if held is None:
        problems.append(f"witness unreachable at {home.witness_root}")
    elif held:
        problems.append(f"the witness already holds checkpoints for {spec.ledger_id}")

    genesis = digest = message = None
    if not problems:
        key = _host_key(home, spec.ledger_id)
        analyzers = canonical_json(list(SYSTEM_ANALYZERS))
        ruleset = {"system": SYSTEM_RULESET, "policy": _digest(policy), "analyzers": _digest(analyzers)}
        fields = {
            "project": spec.project,
            "ledger_id": spec.ledger_id,
            "location": {"repository": f"ssds-home:ledgers/{spec.ledger_id}.git", "ref": ledger_ref(spec.ledger_id)},
            "trust_roots": {"admission_keys": [{"id": key.key_id, "public_key": key.public_hex}],
                            "dispatcher_keys": [], "human_mechanism": "SSHSIG", "human_keys": humans},
            "witnesses": model.to_json(),
            "structure": structure,
            "modes": {s: dict(m) for s, m in sorted(spec.modes.items())},
            "baseline_commit": spec.baseline_commit,
            "deployment_class": spec.deployment_class,
            "manifest_path": spec.manifest_path,
            "policy_path": spec.policy_path,
        }
        genesis = {
            "kind": "GENESIS", "schema": 1, "ruleset": ruleset, "actor": f"admission:{key.key_id}",
            "actor_class": "ADMISSION", "frame": "ADMITTED", "target": None, "basis": [], "outcome": None,
            "reason": [], "supersedes": [], "binding": None, "governs": {"mode": "LEGACY", "protocol": spec.protocol}, "provenance": None, "refs": [],
            "recorded_at": spec.recorded_at or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "fields": fields,
        }
        problems.extend(f"record: {p}" for p in record_violations(with_id({**genesis, "fields": {**fields, "approval": {}}})))
    if not problems and genesis is not None:
        digest = genesis_digest(genesis)
        message = genesis_approval_message(genesis)
        _write_private(workspace / "proposal.json", canonical_json(genesis))
        _write_private(workspace / "objects.json", canonical_json(
            {"policy": policy.decode("utf-8"), "analyzers": list(SYSTEM_ANALYZERS)}))
        _write_private(workspace / "approval-message.txt", message)
        _write_private(workspace / "source.json", canonical_json(
            {"product_repository": str(spec.product_repository), "baseline_commit": spec.baseline_commit}))
    report = workspace / "report.json"
    _write_private(report, json.dumps({
        "ledger_id": spec.ledger_id, "valid": not problems, "genesis_digest": digest, "problems": problems,
        "findings": findings, "subjects": sorted((structure or {}).get("units", {})) if structure else [],
        "modes": {s: dict(m) for s, m in sorted(spec.modes.items())}, "baseline_commit": spec.baseline_commit,
        "approval_message": message.decode("ascii") if message else None,
    }, indent=2, sort_keys=True).encode("utf-8") + b"\n")
    return Prepared(spec.ledger_id, genesis, digest, message, tuple(problems), tuple(findings), workspace, report)


def _digest(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


# -- admitting a prepared genesis ------------------------------------------------------------------


class GenesisRefused(ValueError):
    """The genesis was not admitted; nothing was published."""

    def __init__(self, problems: Sequence[str]) -> None:
        super().__init__("; ".join(problems))
        self.problems = tuple(problems)


@dataclass(frozen=True)
class Admitted:
    ledger_id: str
    repository: Path
    entry_commit: str
    entry_digest: str
    genesis_digest: str
    qualification: str
    findings: tuple[str, ...] = field(default=())


def admit_genesis(home: Home, ledger_id: str, signature: str) -> Admitted:
    """Append and admit the prepared genesis once the human gate's signature verifies.

    The proposal is read back from the workspace and must be byte-for-byte what
    was prepared; the approval key is whichever registered human key verifies
    the signature over the approval message. The entry is admitted when the
    file witness acknowledges its checkpoint (``q_a = 1``) and the read-back
    chain qualifies.
    """

    try:
        home.check(ledger_id)
    except HomeRefused as refused:
        raise GenesisRefused([str(refused)]) from None
    workspace = home.workspace(ledger_id)
    try:
        genesis = json.loads((workspace / "proposal.json").read_bytes())
        objects = json.loads((workspace / "objects.json").read_bytes())
        source = json.loads((workspace / "source.json").read_bytes())
        message = (workspace / "approval-message.txt").read_bytes()
    except (OSError, ValueError) as exc:
        raise GenesisRefused([f"no prepared genesis for {ledger_id}: {exc}"]) from None
    if canonical_json(genesis) != (workspace / "proposal.json").read_bytes() or genesis_approval_message(genesis) != message:
        raise GenesisRefused(["the prepared proposal changed after it was prepared"])
    repository = home.ledger_repository(ledger_id)
    if repository.exists() and ledger_head(repository, ledger_id) is not None:
        raise GenesisRefused([f"ledger {ledger_id} already exists"])
    policy = objects["policy"].encode("utf-8")
    analyzers = canonical_json(list(objects["analyzers"]))
    if genesis["ruleset"] != {**genesis["ruleset"], "policy": _digest(policy), "analyzers": _digest(analyzers)}:
        raise GenesisRefused(["the prepared ledger objects do not match the ruleset"])
    humans = [k["public_key"] for k in genesis["fields"]["trust_roots"]["human_keys"]]
    signer = next((k for k in humans if verify_sshsig(k, message, signature)), None)
    if signer is None:
        raise GenesisRefused(["the genesis approval signature does not verify under a registered human key"])
    signed = dict(genesis)
    signed["fields"] = {**genesis["fields"], "approval": {"key_id": human_key_id(signer), "signature": signature}}
    record = with_id(signed)
    key = _host_key(home, ledger_id)
    entry = {"ledger_id": ledger_id, "position": 0, "schema": 1, "prev": None, "entry_kind": "LIFECYCLE",
             "host_key_id": key.key_id, "incarnation_id": secrets.token_hex(16), "obs": None, "admission": None,
             "absorption": None, "lifecycle": record, "records": []}
    problems = genesis_violations(record) + [f"record: {p}" for p in record_violations(record)] + entry_violations(entry)
    if key.key_id not in {k["id"] for k in genesis["fields"]["trust_roots"]["admission_keys"]}:
        problems.append("the Admission host key is not the genesis trust root")
    if problems:
        raise GenesisRefused(problems)

    create_ledger_repository(repository)
    import_commits(repository, Path(source["product_repository"]), [genesis["fields"]["baseline_commit"]])
    appended = append_entry(repository, entry, key, None, objects={_digest(policy): policy, _digest(analyzers): analyzers},
                            referenced=[genesis["fields"]["baseline_commit"]])
    witness = FileWitness(home.witness_root)
    write_checkpoint(witness, appended.checkpoint)
    chain = read_chain(repository, ledger_id)
    model = WitnessModel.from_json(genesis["fields"]["witnesses"])
    host_keys = {k["id"]: k["public_key"] for k in genesis["fields"]["trust_roots"]["admission_keys"]}
    qualification = qualify(chain, {"local-file": witness.read(ledger_id)}, model, host_keys)
    if not qualification.current or qualification.head != 0:
        raise GenesisRefused([f"the appended genesis did not qualify: {qualification.state}"])
    home.high_water(ledger_id).set(HighWaterMark(0, appended.digest))
    return Admitted(ledger_id, repository, appended.commit, appended.digest, genesis_digest(record), qualification.state)


__all__ = ["Admitted", "GenesisRefused", "GenesisSpec", "Home", "HomeRefused", "Prepared", "admit_genesis", "genesis_approval_message",
           "genesis_digest", "genesis_proposal", "genesis_violations", "prepare_genesis"]
