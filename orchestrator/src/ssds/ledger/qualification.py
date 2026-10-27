"""Currentness qualification, witnesses and the non-admission bound (catalogue §23.3-§23.6).

A head is current-qualified only when a witness quorum holds its exact identity
and it extends every checkpoint and the high-water mark the evaluator observes.
Derivation never consults witnesses; Admission, the Interface and the
Dispatcher consult this module before presenting anything as current.
"""

from __future__ import annotations

import json
import os
import secrets
import stat
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ssds.core.api.v1 import canonical_json

from .read import Chain, is_unit
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

    def statement(self, ledger_id: str) -> RetirementStatement | None:
        """The retirement statement the witness holds for the ledger, or None: an unreachable witness, no file, or one
        that is not a closed-shape regular file (a bare marker is none)."""

        path = self.directory(ledger_id) / RETIREMENT_FILE
        if path.is_symlink() or not path.is_file():
            return None
        try:
            return RetirementStatement.from_json(json.loads(path.read_bytes()))
        except (KeyError, TypeError, ValueError, AttributeError):
            return None


# -- retirement statements (catalogue §23.3-§23.4, §24.2; Phase F step 7a, reading F45) ----------------------------
#
# A ledger is retired by a human-gated LINEAGE_RETIREMENT lifecycle entry; Admission then publishes a retirement
# statement to the witnesses, signed by its host key like a checkpoint, naming that entry as the ledger's last, whose
# approval the chain carries. A participant reads RETIRED when q_a declared witnesses hold a statement that verifies.

#: Retirement statements are signed apart from entries and checkpoints.
RETIREMENT_DOMAIN = b"ssds.retirement.v1"
#: The file a witness retains the statement in, beside the ledger's checkpoints.
RETIREMENT_FILE = "RETIREMENT"
_RETIREMENT_BODY = ("ledger_id", "kind", "last_position", "last_entry_digest", "successor_ledger_id",
                    "successor_genesis_digest")


def retirement_message(body: Mapping[str, Any]) -> bytes:
    return RETIREMENT_DOMAIN + canonical_json(dict(body))


@dataclass(frozen=True)
class RetirementStatement:
    """``{ledger_id, kind: RETIREMENT, last_position, last_entry_digest, successor_ledger_id,
    successor_genesis_digest, signatures}`` (§23.3)."""

    body: dict[str, Any]
    signatures: tuple[tuple[str, str], ...]  # (host key id, hex signature)

    @classmethod
    def from_json(cls, raw: Mapping[str, Any]) -> RetirementStatement:
        if set(raw) != {*_RETIREMENT_BODY, "signatures"} or not isinstance(raw["signatures"], list):
            raise ValueError("not a retirement statement")
        signatures = tuple((s["key_id"], s["signature"]) for s in raw["signatures"])
        if not all(isinstance(k, str) and isinstance(v, str) for k, v in signatures):
            raise ValueError("a signature is a key id and a hex string")
        return cls({k: raw[k] for k in _RETIREMENT_BODY}, signatures)

    def to_json(self) -> dict[str, Any]:
        return {**self.body, "signatures": [{"key_id": k, "signature": v} for k, v in self.signatures]}

    def authentic(self, host_keys: Mapping[str, str]) -> bool:
        """Signed by a host key of the trust roots."""

        message = retirement_message(self.body)
        for key_id, signature in self.signatures:
            try:
                if key_id in host_keys and verify_host(host_keys[key_id], message, bytes.fromhex(signature)):
                    return True
            except ValueError:
                continue
        return False


def retirement_verified(statement: RetirementStatement | None, ledger_id: str, host_keys: Mapping[str, str],
                        chain: Chain | None = None) -> bool:
    """Whether ``statement`` retires ``ledger_id``: authentic under the trust roots ``host_keys`` and, where ``chain``
    holds its last position, naming the ``LINEAGE_RETIREMENT`` entry there. A participant behind the retirement, or
    one holding no chain (which passes the trust roots of the genesis it pins), verifies by the trust roots alone."""

    if statement is None or statement.body["ledger_id"] != ledger_id or statement.body["kind"] != "RETIREMENT" \
            or not statement.authentic(host_keys):
        return False
    position = statement.body["last_position"]
    if not isinstance(position, int) or isinstance(position, bool) or position < 1:
        return False
    if chain is None or position >= len(chain.entries):
        return True
    last = chain.entries[position]
    lifecycle = last.lifecycle or {}
    return last.digest == statement.body["last_entry_digest"] and lifecycle.get("kind") == "LINEAGE_RETIREMENT"


def retirement_statements(model: WitnessModel, ledger_id: str) -> dict[str, RetirementStatement | None]:
    """Each declared witness's statement; only ``FILE`` witnesses are reachable here (F3)."""

    return {w.id: FileWitness(Path(w.location)).statement(ledger_id) if w.kind == "FILE" else None
            for w in model.witnesses}


def retirement_held(statements: Iterable[RetirementStatement | None], q_a: int, ledger_id: str,
                    host_keys: Mapping[str, str], chain: Chain | None = None) -> bool:
    """``RETIRED``: ``q_a`` witnesses hold one and the same verified statement (§24.2), one statement per witness;
    distinct statements never add up to a quorum (review 749b37d N2)."""

    held: dict[bytes, int] = {}
    for s in statements:
        if retirement_verified(s, ledger_id, host_keys, chain):
            identity = canonical_json(s.to_json())
            held[identity] = held.get(identity, 0) + 1
    return max(held.values(), default=0) >= q_a


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
        publish_private(self.path, canonical_json({"position": mark.position, "entry_digest": mark.entry_digest}))


def write_all(descriptor: int, data: bytes) -> None:
    """Write every byte or raise: ``os.write`` may return a short count (Review b341109 A-B13)."""

    view = memoryview(data)
    while view:
        written = os.write(descriptor, view)
        if written <= 0:
            raise OSError("no progress writing operator state")
        view = view[written:]


def publish_private(path: Path, data: bytes) -> None:
    """The one way operator state is written: a fresh file, then an atomic rename over the name.

    The bytes go into a newly created file (``O_CREAT | O_EXCL | O_NOFOLLOW``, mode 0600, a unique
    name in the same directory), which is fsynced and then renamed over ``path``, and the directory is
    fsynced. No existing file is ever opened for writing, so whatever ``path`` was (a hard link to
    another file, a symbolic link, a stale temporary) nothing but the name is replaced. Every byte is
    written before the rename; a short or failed write publishes nothing and leaves no temporary.
    """

    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    temporary = path.with_name(f".{path.name}.{secrets.token_hex(8)}.tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    try:
        try:
            write_all(descriptor, data)
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise
    directory = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


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
    """Entry digests the human-gated resolutions in the chain's first ``through + 1`` entries name as abandoned.

    Admission of those records is the caller's to establish: ``qualify`` reads them only inside a
    quorum-held prefix.
    """

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
    seen = {(c.position, c.entry_digest) for cps in responders.values() for c in cps}
    holders = {p: sum(1 for cps in responders.values() if any(c.position == p and c.entry_digest == digests[p] for c in cps))
               for p in range(len(digests))}
    quorum_held = sorted((p for p, n in holders.items() if n >= model.q_a), reverse=True)

    def assess(through: int) -> tuple[str, int]:
        """The read under the abandonment that recovery records within the prefix through ``through`` admit.

        A recovery record counts only once it lies inside a quorum-held prefix (Review b341109 A-B11): a
        signed record in the replica's unwitnessed suffix is not admitted and abandons nothing. Returns
        ("OK", floor) or the failing state.
        """

        abandoned = _abandoned(chain, through) if through >= 0 else frozenset()
        by_position: dict[int, set[str]] = {}
        for position, digest in seen:
            by_position.setdefault(position, set()).add(digest)
        for position, found in by_position.items():
            if len(found - abandoned) > 1:
                return "FORK", -1
            if position <= top and any(d != digests[position] and d not in abandoned for d in found):
                return "FORK", -1
        marks = [p for p, d in seen if d not in abandoned]
        retained = None  # the evaluator's own high-water mark: the last head it qualified (§23.4)
        if high_water is not None and high_water.entry_digest not in abandoned:
            if high_water.position <= top and digests[high_water.position] != high_water.entry_digest:
                return "FORK", -1
            retained = high_water.position
        if any(p > top for p in marks) or (retained is not None and retained > top):
            return ("ROLLBACK" if authoritative else "BEHIND"), -1
        # H* extends every checkpoint the evaluator observes and its own retained mark (§23.1, §23.4): an
        # observed checkpoint not yet held by an admission quorum withholds currentness until read repair;
        # it is never relabelled a provisional successor. The provisional successor is only the replica's
        # own entry beyond H* that no responder has shown a checkpoint for.
        return "OK", max(marks + ([retained] if retained is not None else []), default=-1)

    for head in quorum_held:  # the highest quorum-held prefix whose own recovery records explain every mark
        state, floor = assess(head)
        if state == "OK" and head >= floor:
            critical = ("more than one entry beyond the qualified head",) if top > head + 1 else ()
            provisional = head + 1 if top >= head + 1 else None
            return Qualification("QUALIFIED", head, digests[head], provisional, critical)
    state, _ = assess(quorum_held[0] if quorum_held else -1)
    return Qualification(state if state != "OK" else "UNQUALIFIED")


def segments(chain: Chain) -> list[tuple[int, WitnessModel | None]]:
    """The witness model in force per position (Phase F step 7e, reading F59): genesis's from position 0; each
    ``WITNESS_SET_REDESIGNATION`` in the readable chain, and each ``LEDGER_LOSS`` whose ``controls.witnesses``
    re-establishes a different set (F62), starts a segment at its own position, whose entry belongs to both segments.
    A model that does not parse is ``None``: nothing qualifies under it."""

    out: list[tuple[int, WitnessModel | None]] = []
    for entry in chain.entries[: chain.readable_through + 1]:
        lifecycle = entry.lifecycle
        kind = lifecycle.get("kind") if lifecycle else None
        try:
            if kind == "GENESIS" and entry.position == 0 or kind == "WITNESS_SET_REDESIGNATION" and out:
                raw = lifecycle["fields"]["witnesses"]
            elif kind == "LEDGER_LOSS" and out:
                raw = lifecycle["fields"]["controls"]["witnesses"]
            else:
                continue
            model = WitnessModel.from_json(raw)
        except (KeyError, TypeError, ValueError, AttributeError):
            model = None
        if kind == "LEDGER_LOSS" and model is not None and model == out[-1][1]:
            continue  # a loss re-establishing the same set starts no segment
        out.append((entry.position, model))
    return out


def segment_witnesses(chain: Chain, position: int) -> list[WitnessSpec]:
    """The witnesses an entry at ``position`` is checkpointed to: those of every segment it lies in (F59)."""

    found = segments(chain)
    out: dict[str, WitnessSpec] = {}
    for i, (start, model) in enumerate(found):
        end = found[i + 1][0] if i + 1 < len(found) else None
        if model is not None and start <= position and (end is None or position <= end):
            out.update((w.id, w) for w in model.witnesses)
    return list(out.values())


def lineage_witnesses(chain: Chain) -> list[WitnessSpec]:
    """Every witness any segment declares, each once: what a reader gathers reports from (F59)."""

    out: dict[str, WitnessSpec] = {}
    for _, model in segments(chain):
        if model is not None:
            out.update((w.id, w) for w in model.witnesses)
    return list(out.values())


def qualify_segments(
    chain: Chain,
    reports: Mapping[str, Sequence[Checkpoint] | None],
    host_keys: Mapping[str, str],
    high_water: HighWaterMark | None = None,
    authoritative: bool = True,
    retired: bool = False,
) -> Qualification:
    """Qualify ``chain`` across its witness segments (reading F59), newest first, each under its own model and its own
    declared witnesses' reports. A later segment starting at ``p`` passes to the older one only when its holding from
    ``p`` is proved never admitted (§23.6's bound, ``h + m + f < q_a``, ``h`` counting its witnesses reporting an
    authentic checkpoint at ``p`` or later and ``m`` those not responding); the older segment then reads the
    redesignation as provisional, its result counting inside its range, up to but excluding ``p``. Otherwise the
    later segment's verdict is the answer, whatever it is: ``FORK`` and ``ROLLBACK`` included, and ``UNQUALIFIED``
    when too few respond, so neither a denying witness nor an unreachable set lets an older set present a stale head
    (plan revisions 26-27, checks of c36b278e B1 and 3b6ebcc0 R1). Old witnesses are not read once it may be held."""

    if chain.halt is not None:
        return Qualification("INTEGRITY_HALT")
    if retired:
        return Qualification("RETIRED")
    found = segments(chain)
    if not found:
        return Qualification("UNQUALIFIED")
    for i in reversed(range(len(found))):
        start, model = found[i]
        if model is None:
            return Qualification("UNQUALIFIED")
        declared = {w.id for w in model.witnesses}
        own = {w: r for w, r in reports.items() if w in declared}
        verdict = qualify(chain, own, model, host_keys, high_water, authoritative)
        if i > 0:
            responders = [cps for cps in own.values() if cps is not None]
            h = sum(1 for cps in responders if any(c.ledger_id == chain.ledger_id and c.position >= start
                                                   and c.authentic(host_keys) for c in cps))
            m = len(declared) - len(responders)
            if loss_status(h, m, model.f, model.q_a) == "PROVED_NEVER_ADMITTED":
                continue  # proved never held from its start: the older segment reads the redesignation as provisional
        # this segment governs, FORK and ROLLBACK included; when a newer one was skipped, its start is the end of this
        # one's range, whatever this segment is (review ae5ab38 B1)
        end = found[i + 1][0] if i + 1 < len(found) else None
        if verdict.current and end is not None and verdict.head is not None and verdict.head >= end:
            # this set holds the next redesignation (or beyond), its successor does not: the redesignation is
            # provisional over the head before it
            digests = chain.digests()
            critical = ("more than one entry beyond the qualified head",) if len(digests) - 1 > end else ()
            return Qualification("QUALIFIED", end - 1, digests[end - 1], end, critical)
        return verdict
    return Qualification("UNQUALIFIED")


def loss_status(h: int, m: int, f: int, q_a: int) -> str:
    """An abandoned entry: proved never admitted iff ``h + m + f < q_a``; known admitted iff ``h >= q_a`` (§23.6)."""

    if h + m + f < q_a:
        return "PROVED_NEVER_ADMITTED"
    if h >= q_a:
        return "KNOWN_ADMITTED"
    return "POSSIBLY_ADMITTED"


__all__ = [
    "Checkpoint", "DEPLOYMENT_CLASSES", "FileWitness", "HighWaterMark", "HighWaterStore", "Home", "HomeRefused",
    "Qualification", "RETIREMENT_DOMAIN", "RETIREMENT_FILE", "RetirementStatement",
    "STATES", "WitnessModel", "WitnessSpec", "checkpoint_body", "checkpoint_message", "loss_status",
    "lineage_witnesses", "publish_private", "qualify", "qualify_segments", "retirement_held", "segment_witnesses",
    "segments", "retirement_message", "retirement_statements",
    "retirement_verified", "write_all",
    "quorum_sound",
]


# -- the SSDS home: where operator data lives (Manual §26.3, A7; Phase D threat boundary SD-59) -------------


class Home:
    """A project's operator data under the SSDS home (created on first write): the ledger repository, the
    witnesses and the high-water mark, and the check that guards the whole operator tree. Admission's own
    files (its key, the genesis workspace) are its subclass's (``admission.genesis.AdmissionHome``), so the
    Interface and the Dispatcher, which may import this module, reach none of them (§26.1-§26.2).

    One rule closes every way a path could be redirected out of the home: the
    home lies outside every repository and holds none but its own ledgers, and the
    operator tree a ledger uses (its ledger repository, witness, keys, genesis
    workspace and state, and the directories that hold them) contains no
    symbolic link at all, checked by :meth:`check` before any effect. The ledger
    id must be a unit identity (catalogue §1.1), every resolved path must stay
    inside the resolved home, and every write publishes a fresh file over the name
    (:func:`publish_private`), so no existing file object, a hard link
    included, is ever written through.
    The home itself may be reached through a link; nothing inside it may be one.
    A genesis creates its ledger repository afresh, so no pre-existing Git
    layout (internal links, alternates, configuration) is ever written through.
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

    def _file(self, *parts: str) -> Path:
        path = self._inside(*parts)
        if path.is_symlink():
            raise HomeRefused(f"{path} is a symbolic link; the SSDS home writes only its own files")
        return path

    def ledger_repository(self, ledger_id: str) -> Path:
        self.check_ledger_id(ledger_id)
        return self._inside("ledgers", f"{ledger_id}.git")

    @property
    def witness_root(self) -> Path:
        return self._inside("witness")

    def witness_directory(self, ledger_id: str) -> Path:
        self.check_ledger_id(ledger_id)
        return self._inside("witness", ledger_id)

    def high_water(self, ledger_id: str) -> HighWaterStore:
        self.check_ledger_id(ledger_id)
        return HighWaterStore(self._file("state", ledger_id, "high-water.json"))

    def operator_tree(self, ledger_id: str) -> tuple[Path, ...]:
        """Every directory tree this ledger's operator data lives in."""

        self.check_ledger_id(ledger_id)
        return (self.root / "ledgers" / f"{ledger_id}.git", self.root / "witness", self.root / "keys" / "admission",
                self.root / "keys" / "dispatcher", self.root / "genesis" / ledger_id, self.root / "state" / ledger_id)

    def outside_repositories(self) -> None:
        """The resolved home lies outside every repository (SD-56, Manual §26.3): no ancestor, nor the home
        itself, is a Git worktree (holds ``.git``) or a bare repository (``HEAD``, ``objects/``, ``refs/``)."""

        resolved = self.root.resolve()
        for directory in (resolved, *resolved.parents):
            if _is_repository(directory):
                raise HomeRefused(f"the SSDS home {self.root} lies inside the repository at {directory}; "
                                  "set SSDS_HOME to a directory outside every repository")

    def check(self, ledger_id: str) -> None:
        """Refuse before any filesystem effect: the home outside every repository, no link anywhere in this
        ledger's operator tree, every path inside.

        A tree is certified only as far as it was read (Review df911c0 A-B12): every directory of the
        operator tree is listed and every entry classified as a directory or a regular file; a directory
        that cannot be listed, an entry that cannot be examined, or an entry of any other kind refuses.
        """

        self.outside_repositories()
        ledger = self.root / "ledgers" / f"{ledger_id}.git"
        for top in self.operator_tree(ledger_id):
            relative = top.relative_to(self.root).parts
            for depth in range(1, len(relative) + 1):  # the directories that hold it
                component = self.root.joinpath(*relative[:depth])
                mode = _mode(component)
                if mode is None:
                    break
                if stat.S_ISLNK(mode):
                    raise HomeRefused(f"{component} is a symbolic link; nothing inside the SSDS home may be one")
                if not stat.S_ISDIR(mode):
                    raise HomeRefused(f"{component} is not a directory; the SSDS home keeps its operator data there")
                if component != ledger and _is_repository(component):
                    raise HomeRefused(f"{component} is a repository; the SSDS home holds none but its ledgers")
            else:  # the whole path is present: read the tree under it whole
                pending = [top]
                while pending:
                    here = pending.pop()
                    if here != ledger and _is_repository(here):  # Review b341109 A-B12: a nested repository
                        raise HomeRefused(f"{here} is a repository; the SSDS home holds none but its ledgers")
                    for path in _listing(here):
                        mode = _mode(path)
                        if mode is None:
                            raise HomeRefused(f"{path} vanished while the SSDS home was read")
                        if stat.S_ISLNK(mode):
                            raise HomeRefused(f"{path} is a symbolic link; nothing inside the SSDS home may be one")
                        if stat.S_ISDIR(mode):
                            pending.append(path)
                        elif not stat.S_ISREG(mode):
                            raise HomeRefused(f"{path} is neither a file nor a directory; the SSDS home holds "
                                              "only its own files")
        self._check_paths(ledger_id)

    def _check_paths(self, ledger_id: str) -> None:
        """Every path this home names for the ledger resolves inside it."""

        self.ledger_repository(ledger_id), self.witness_root, self.witness_directory(ledger_id)
        self.high_water(ledger_id)


def _mode(path: Path) -> int | None:
    """The ``lstat`` mode of ``path``, or ``None`` when nothing is there; any other failure refuses."""

    try:
        return os.lstat(path).st_mode
    except (FileNotFoundError, NotADirectoryError):
        return None
    except OSError as exc:
        raise HomeRefused(f"{path} cannot be examined ({exc.strerror}); the SSDS home certifies only what it reads"
                          ) from None


def _listing(directory: Path) -> list[Path]:
    """Every entry of ``directory``; a directory that cannot be listed whole refuses."""

    try:
        with os.scandir(directory) as entries:
            return sorted(directory / entry.name for entry in entries)
    except OSError as exc:
        raise HomeRefused(f"{directory} cannot be listed ({exc.strerror}); the SSDS home certifies only what it "
                          "reads") from None


def _is_repository(directory: Path) -> bool:
    """A Git worktree or a bare repository at ``directory``.

    A worktree has a ``.git`` file (a ``gitdir:`` pointer) or a ``.git`` directory that is a Git directory
    (``HEAD`` inside); a bare repository has ``HEAD``, ``objects/`` and ``refs/``. An empty ``.git``
    directory is not a repository. A marker that cannot be examined refuses rather than counting as absent.
    """

    marker = _mode(directory / ".git")
    if marker is not None and not stat.S_ISDIR(marker):
        return True
    if marker is not None and _mode(directory / ".git" / "HEAD") is not None:
        return True
    head, objects, refs = (_mode(directory / name) for name in ("HEAD", "objects", "refs"))
    return (head is not None and not stat.S_ISDIR(head)
            and all(m is not None and (stat.S_ISDIR(m) or stat.S_ISLNK(m)) for m in (objects, refs)))


class HomeRefused(ValueError):
    """An input that would place operator data outside the SSDS home."""
