"""Currentness qualification, witnesses and the non-admission bound (catalogue §23.3-§23.6).

A head is current-qualified only when a witness quorum holds its exact identity
and it extends every checkpoint and the high-water mark the evaluator observes.
Derivation never consults witnesses; Admission, the Interface and the
Dispatcher consult this module before presenting anything as current.
"""

from __future__ import annotations

import json
import os
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ssds.core.api.v1 import canonical_json

from .read import Chain
from .signatures import CHECKPOINT_DOMAIN, verify_host

DEPLOYMENT_CLASSES = {"LOCAL_TRUST": (1, 1, 1, 0), "TEAM": (3, 2, 2, 0), "HARDENED": (4, 3, 3, 1)}
STATES = ("QUALIFIED", "FORK", "ROLLBACK", "BEHIND", "UNQUALIFIED", "RETIRED", "INTEGRITY_HALT")


def quorum_sound(n: int, q_a: int, r: int, f: int) -> bool:
    """``q_a + r > N + f``: any admission and read quorum share more than ``f`` witnesses."""

    return 0 < q_a <= n and 0 < r <= n and 0 <= f and q_a + r > n + f


@dataclass(frozen=True)
class WitnessSpec:
    id: str
    kind: str  # FILE (local trust only) | GIT | LOG
    location: str


@dataclass(frozen=True)
class WitnessModel:
    deployment_class: str
    n: int
    q_a: int
    r: int
    f: int
    witnesses: tuple[WitnessSpec, ...]

    @classmethod
    def from_json(cls, raw: Mapping[str, Any]) -> WitnessModel:
        return cls(raw["class"], raw["N"], raw["q_a"], raw["r"], raw["f"],
                   tuple(WitnessSpec(w["id"], w["kind"], w["location"]) for w in raw["witnesses"]))

    def to_json(self) -> dict[str, Any]:
        return {"class": self.deployment_class, "N": self.n, "q_a": self.q_a, "r": self.r, "f": self.f,
                "witnesses": [{"id": w.id, "kind": w.kind, "location": w.location} for w in self.witnesses]}

    def validate(self) -> None:
        if self.deployment_class not in DEPLOYMENT_CLASSES:
            raise ValueError(f"unknown deployment class {self.deployment_class}")
        if (self.n, self.q_a, self.r, self.f) != DEPLOYMENT_CLASSES[self.deployment_class]:
            raise ValueError(f"{self.deployment_class} is {DEPLOYMENT_CLASSES[self.deployment_class]}")
        if not quorum_sound(self.n, self.q_a, self.r, self.f):
            raise ValueError("q_a + r > N + f does not hold")
        if len(self.witnesses) != self.n or len({w.id for w in self.witnesses}) != self.n:
            raise ValueError("the witness set has N distinct witnesses")
        for witness in self.witnesses:
            if witness.kind == "FILE" and self.deployment_class != "LOCAL_TRUST":
                raise ValueError("a file witness serves local trust only")
            if witness.kind not in ("FILE", "GIT", "LOG"):
                raise ValueError(f"unknown witness kind {witness.kind}")


def checkpoint_body(ledger_id: str, position: int, entry_digest: str, entry_commit: str, host_key_id: str) -> dict[str, Any]:
    return {"ledger_id": ledger_id, "position": position, "entry_digest": entry_digest,
            "entry_commit": entry_commit, "host_key_id": host_key_id}


def checkpoint_message(body: Mapping[str, Any]) -> bytes:
    return CHECKPOINT_DOMAIN + canonical_json(dict(body))


@dataclass(frozen=True)
class Checkpoint:
    ledger_id: str
    position: int
    entry_digest: str
    entry_commit: str
    host_key_id: str
    signature: str  # hex

    @classmethod
    def from_json(cls, raw: Mapping[str, Any]) -> Checkpoint:
        return cls(raw["ledger_id"], raw["position"], raw["entry_digest"], raw["entry_commit"], raw["host_key_id"],
                   raw["signature"])

    def body(self) -> dict[str, Any]:
        return checkpoint_body(self.ledger_id, self.position, self.entry_digest, self.entry_commit, self.host_key_id)

    def to_json(self) -> dict[str, Any]:
        return {**self.body(), "signature": self.signature}

    def authentic(self, host_keys: Mapping[str, str]) -> bool:
        key = host_keys.get(self.host_key_id)
        return key is not None and verify_host(key, checkpoint_message(self.body()), bytes.fromhex(self.signature))


class FileWitness:
    """An append-only directory witness on another medium (local trust only, catalogue §23.3)."""

    def __init__(self, root: Path) -> None:
        self.root = root

    def directory(self, ledger_id: str) -> Path:
        return self.root / ledger_id

    def read(self, ledger_id: str) -> list[Checkpoint] | None:
        """Every checkpoint the witness holds for the ledger, or None when the witness is unreachable."""

        if not self.root.is_dir():
            return None
        folder = self.directory(ledger_id)
        if not folder.is_dir():
            return []
        out = []
        for path in sorted(folder.glob("*.json")):
            try:
                out.append(Checkpoint.from_json(json.loads(path.read_bytes())))
            except (KeyError, TypeError, ValueError):
                continue  # unreadable files are not checkpoints; they hold nothing
        return out

    def retired(self, ledger_id: str) -> bool:
        return (self.directory(ledger_id) / "RETIREMENT").exists()


@dataclass(frozen=True)
class HighWaterMark:
    position: int
    entry_digest: str


class HighWaterStore:
    """A participant's high-water mark, in its private operator state."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def get(self) -> HighWaterMark | None:
        if not self.path.is_file():
            return None
        raw = json.loads(self.path.read_bytes())
        return HighWaterMark(raw["position"], raw["entry_digest"])

    def set(self, mark: HighWaterMark) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(".tmp")
        with open(temporary, "wb") as handle:
            handle.write(canonical_json({"position": mark.position, "entry_digest": mark.entry_digest}))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, self.path)


@dataclass(frozen=True)
class Qualification:
    state: str
    head: int | None = None  # the qualified head H*, by position
    head_digest: str | None = None
    provisional: int | None = None  # the replica's single provisional successor of H*
    critical: tuple[str, ...] = ()  # integrity obligations with CRITICAL attention

    @property
    def current(self) -> bool:
        return self.state == "QUALIFIED"


def _abandoned(chain: Chain, through: int) -> frozenset[str]:
    """Entry digests an admitted human-gated resolution in the chain names as abandoned."""

    out = set()
    for entry in chain.entries[: through + 1]:
        lifecycle = entry.lifecycle
        if lifecycle and lifecycle["kind"] in ("FORK_RESOLUTION", "LEDGER_LOSS"):
            out.update(a.get("digest", "") for a in lifecycle["fields"]["abandoned"])
    return frozenset(out)


def qualify(
    chain: Chain,
    reports: Mapping[str, Sequence[Checkpoint] | None],
    model: WitnessModel,
    host_keys: Mapping[str, str],
    high_water: HighWaterMark | None = None,
    authoritative: bool = True,
    retired: bool = False,
) -> Qualification:
    """Classify the replica's chain against witness reports (catalogue §23.4)."""

    if chain.halt is not None:
        return Qualification("INTEGRITY_HALT")
    if retired:
        return Qualification("RETIRED")
    try:
        model.validate()
    except ValueError:
        return Qualification("UNQUALIFIED")  # quorums are meaningless over an unsound or malformed witness set
    # Quorums count the declared witness set only (§23.3): a report keyed by any other identity is no
    # response, however authentic the checkpoints it carries.
    declared = {w.id for w in model.witnesses}
    responders = {w: [c for c in cps if c.ledger_id == chain.ledger_id and c.authentic(host_keys)]
                  for w, cps in reports.items() if cps is not None and w in declared}
    if len(responders) < model.r:
        return Qualification("UNQUALIFIED")
    digests = chain.digests()
    top = len(digests) - 1
    abandoned = _abandoned(chain, top)
    seen = {(c.position, c.entry_digest) for cps in responders.values() for c in cps}
    by_position: dict[int, set[str]] = {}
    for position, digest in seen:
        by_position.setdefault(position, set()).add(digest)
    for position, found in by_position.items():
        if len(found - abandoned) > 1:
            return Qualification("FORK")
        if position <= top and any(d != digests[position] and d not in abandoned for d in found):
            return Qualification("FORK")
    marks = [(p, d) for p, d in seen if d not in abandoned]
    if high_water is not None and high_water.entry_digest not in abandoned:
        if high_water.position <= top and digests[high_water.position] != high_water.entry_digest:
            return Qualification("FORK")
        marks.append((high_water.position, high_water.entry_digest))
    if any(p > top for p, _ in marks):
        return Qualification("ROLLBACK" if authoritative else "BEHIND")
    holders = {p: sum(1 for cps in responders.values() if any(c.position == p and c.entry_digest == digests[p] for c in cps))
               for p in range(len(digests))}
    floor = max((p for p, _ in marks), default=-1)
    candidates = [p for p, n in holders.items() if n >= model.q_a and p >= floor - 1]
    candidates = [p for p in candidates if all(p >= m or m == p + 1 for m, _ in marks)]
    if not candidates:
        return Qualification("UNQUALIFIED")
    head = max(candidates)
    critical = ()
    if top > head + 1:
        critical = ("more than one entry beyond the qualified head",)
    provisional = head + 1 if top >= head + 1 else None
    return Qualification("QUALIFIED", head, digests[head], provisional, critical)


def loss_status(h: int, m: int, f: int, q_a: int) -> str:
    """An abandoned entry: proved never admitted iff ``h + m + f < q_a``; known admitted iff ``h >= q_a`` (§23.6)."""

    if h + m + f < q_a:
        return "PROVED_NEVER_ADMITTED"
    if h >= q_a:
        return "KNOWN_ADMITTED"
    return "POSSIBLY_ADMITTED"


__all__ = [
    "Checkpoint", "DEPLOYMENT_CLASSES", "FileWitness", "HighWaterMark", "HighWaterStore", "Qualification",
    "STATES", "WitnessModel", "WitnessSpec", "checkpoint_body", "checkpoint_message", "loss_status", "qualify",
    "quorum_sound",
]
