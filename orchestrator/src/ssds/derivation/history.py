"""S0 facts folded over the readable ledger prefix (catalogue §5.2).

Every fact here is a function of the authenticated chain and the trees it
names: the expected integration head ``E_k`` and observed tree ``T_k``,
effective structure ``Σ_k`` (a fold over admitted structural deltas, never a
stored copy), governance modes, the ruleset in force, loss boundaries,
integrations, and every record with the position that admitted it. Trees are
supplied by the caller, keyed by commit identity, so derivation reads no Git.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from functools import cached_property, lru_cache
from typing import Any

from ssds.content import (
    DEFAULT_MANIFEST_PATH,
    Manifest,
    Structure,
    Tree,
    TreeView,
    decl_from_json,
    decl_to_json,
    value_from_json,
)
from ssds.ledger.read import SCHEMA_VERSION, Chain

TreeSource = Callable[[str], Tree]


@dataclass(frozen=True)
class Integration:
    position: int
    transformation: str | None
    base: str
    admitted: str


@dataclass(frozen=True)
class RecordFact:
    record: dict[str, Any]
    position: int
    entry_kind: str


#: The derivation system version a checkpoint key names (§5.9); a change invalidates every checkpoint.
DERIVATION_VERSION = "ssds-derivation/1"


class CheckpointInvalid(ValueError):
    """A derivation checkpoint whose key does not recompute from the ledger, or whose body digest does not match.

    The body digest detects accidental corruption only; it does not authenticate the cached fold. A
    checkpoint is private cache: on any doubt, discard it and derive from genesis (catalogue §21.6).
    """


class History:
    """S0 facts at every position of the readable prefix of one chain.

    ``checkpoint`` resumes the fold from a verified derivation checkpoint
    (:meth:`checkpoint`) instead of replaying from genesis; the result equals
    the from-scratch fold (catalogue §5.9).
    """

    def __init__(self, chain: Chain, trees: TreeSource, checkpoint: bytes | None = None) -> None:
        if chain.genesis is None:
            raise ValueError("derivation needs a readable genesis")
        self.chain = chain
        self.trees = trees
        self.last = chain.readable_through
        genesis = chain.genesis["fields"]
        self.ledger_id = chain.ledger_id
        self.manifest_path = genesis["manifest_path"]
        self.policy_path = genesis["policy_path"]
        self._heads: list[str] = []
        self._sigmas: list[dict[tuple[str, str], Any]] = []
        self._modes: list[dict[str, dict[str, Any]]] = []
        self._rulesets: list[dict[str, Any]] = []
        self.integrations: dict[int, Integration] = {}
        self.records: dict[str, RecordFact] = {}
        self.boundaries: list[int] = []
        self.objects: dict[str, bytes] = {}
        if checkpoint is None:
            head = genesis["baseline_commit"]
            sigma = decl_from_json(genesis["structure"])
            mode = {s: dict(m) for s, m in genesis["modes"].items()}
            ruleset = dict(chain.genesis["ruleset"])
            first = 0
        else:
            head, sigma, mode, ruleset = self._resume(checkpoint)
            first = len(self._heads)
        for entry in chain.entries[first: self.last + 1]:
            head, sigma, mode, ruleset = self._fold(entry, head, sigma, mode, ruleset)

    def _fold(self, entry, head, sigma, mode, ruleset):
        body = entry.entry
        self.objects.update(entry.objects)
        if entry.position > 0:
            kind = body["entry_kind"]
            if kind == "ADMISSION":
                admission = body["admission"]
                if admission["decision"] == "ACCEPT":
                    if admission["admitted_commit"] != head or admission["base_commit"] != head:
                        self.integrations[entry.position] = Integration(
                            entry.position, admission.get("integrates"), admission["base_commit"],
                            admission["admitted_commit"])
                    head = admission["admitted_commit"]
                    if admission["adopted_deltas"]:
                        sigma = dict(sigma)
                        for delta in admission["adopted_deltas"]:
                            key = tuple(delta["key"])
                            value = value_from_json(key[1], delta["value"])
                            if value is None:
                                sigma.pop(key, None)  # type: ignore[arg-type]
                            else:
                                sigma[key] = value  # type: ignore[index]
            elif kind == "ABSORPTION":
                fence = body["absorption"]["fence"]
                head = fence["fence_commit"] if fence else body["obs"]
            elif kind == "LIFECYCLE":
                record = body["lifecycle"]
                fields = record["fields"]
                if record["kind"] == "MODE_TRANSITION":
                    mode = dict(mode)
                    mode[fields["subject"]] = dict(fields["mode"])
                elif record["kind"] == "RULESET_ADOPTION":
                    ruleset = _adopted(fields)
                elif record["kind"] == "LEDGER_LOSS":
                    self.boundaries.append(entry.position)
        carried = list(body["records"]) + ([body["lifecycle"]] if body["lifecycle"] else [])
        for record in carried:
            self.records.setdefault(record["id"], RecordFact(record, entry.position, body["entry_kind"]))
        self._heads.append(head)
        self._sigmas.append(sigma)
        self._modes.append(mode)
        self._rulesets.append(ruleset)
        return head, sigma, mode, ruleset

    # -- derivation checkpoints (§5.9) ------------------------------------------------------------

    def checkpoint_key(self, position: int) -> dict[str, Any]:
        """``(ledger position, entry digest, ruleset including its analyzer set, schema, system version)``."""

        return {"ledger": self.ledger_id, "position": position, "entry": self.chain.entries[position].digest,
                "ruleset": dict(_ruleset_at(self.chain, position)), "schema": SCHEMA_VERSION,
                "system": DERIVATION_VERSION}

    def checkpoint(self, position: int) -> bytes:
        """The complete S0 fold through ``position``, keyed; it carries no currentness."""

        if not 0 <= position <= self.last:
            raise ValueError("position outside the readable prefix")
        tables: dict[str, list[Any]] = {"sigma": [], "mode": [], "ruleset": []}
        index: dict[str, dict[int, int]] = {name: {} for name in tables}

        def ref(name: str, value: Any, encoded: Any) -> int:
            if id(value) not in index[name]:
                index[name][id(value)] = len(tables[name])
                tables[name].append(encoded)
            return index[name][id(value)]

        positions = [[self._heads[k], ref("sigma", self._sigmas[k], decl_to_json(self._sigmas[k])),
                      ref("mode", self._modes[k], self._modes[k]), ref("ruleset", self._rulesets[k], self._rulesets[k])]
                     for k in range(position + 1)]
        body = {
            "positions": positions, **tables,
            "integrations": [[i.position, i.transformation, i.base, i.admitted]
                             for i in self.integrations.values() if i.position <= position],
            "boundaries": [b for b in self.boundaries if b <= position],
            "records": sorted([rid, f.position] for rid, f in self.records.items() if f.position <= position),
        }
        payload = {"key": self.checkpoint_key(position), "body": body, "digest": _digest(body)}
        return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")

    def _resume(self, data: bytes):
        try:
            payload = json.loads(data)
            key, body = payload["key"], payload["body"]
            position = key["position"]
        except (ValueError, KeyError, TypeError) as error:
            raise CheckpointInvalid(f"unreadable checkpoint: {error}") from None
        if not isinstance(position, int) or not 0 <= position <= self.last \
                or key != self.checkpoint_key(position) or payload.get("digest") != _digest(body):
            raise CheckpointInvalid("checkpoint key does not recompute from the ledger")
        sigmas = [decl_from_json(raw) for raw in body["sigma"]]
        modes = [{s: dict(m) for s, m in raw.items()} for raw in body["mode"]]
        rulesets = [dict(raw) for raw in body["ruleset"]]
        for head, si, mi, ri in body["positions"]:
            self._heads.append(head)
            self._sigmas.append(sigmas[si])
            self._modes.append(modes[mi])
            self._rulesets.append(rulesets[ri])
        if len(self._heads) != position + 1:
            raise CheckpointInvalid("checkpoint body does not cover its position")
        for k, transformation, base, admitted in body["integrations"]:
            self.integrations[k] = Integration(k, transformation, base, admitted)
        self.boundaries = list(body["boundaries"])
        wanted = {rid: k for rid, k in body["records"]}
        for entry in self.chain.entries[: position + 1]:
            self.objects.update(entry.objects)
            carried = list(entry.records) + ([entry.lifecycle] if entry.lifecycle else [])
            for record in carried:
                if wanted.get(record["id"]) == entry.position:
                    self.records.setdefault(record["id"], RecordFact(record, entry.position, entry.entry["entry_kind"]))
        if len(self.records) != len(wanted):
            raise CheckpointInvalid("checkpoint names records the ledger does not carry there")
        return self._heads[-1], self._sigmas[-1], self._modes[-1], self._rulesets[-1]

    def head(self, position: int) -> str:
        return self._heads[position]

    def sigma(self, position: int) -> Mapping[tuple[str, str], Any]:
        return self._sigmas[position]

    def modes(self, position: int) -> Mapping[str, Mapping[str, Any]]:
        return self._modes[position]

    def ruleset(self, position: int) -> Mapping[str, Any]:
        return self._rulesets[position]

    def tree(self, position: int) -> Tree:
        return self.trees(self.head(position))

    @lru_cache(maxsize=256)  # noqa: B019 - one History per derivation; keyed by its inputs
    def _view(self, head: str, sigma_index: int) -> TreeView:
        return TreeView(self.trees(head), Structure(self._sigmas[sigma_index]), self.manifest_path)

    def view(self, position: int) -> TreeView:
        """``T_k`` under ``Σ_k``; memoized by (head, structure)."""

        return self._view(self.head(position), self._first_sigma(position))

    def _first_sigma(self, position: int) -> int:
        sigma = self._sigmas[position]
        index = position
        while index > 0 and self._sigmas[index - 1] is sigma:
            index -= 1
        return index

    @cached_property
    def positions(self) -> range:
        return range(self.last + 1)

    def mode(self, position: int, subject: str) -> Mapping[str, Any]:
        """A subject's governance mode; one first declared after genesis takes genesis's ``"*"`` mode, else UNGOVERNED."""

        modes = self.modes(position)
        return modes.get(subject) or modes.get("*", {"mode": "UNGOVERNED"})


def _ruleset_at(chain: Chain, position: int) -> Mapping[str, Any]:
    """The ruleset in force at ``position``, recomputed from the ledger's lifecycle entries alone."""

    ruleset = dict(chain.genesis["ruleset"]) if chain.genesis else {}
    for entry in chain.entries[1: position + 1]:
        record = entry.lifecycle
        if record and record["kind"] == "RULESET_ADOPTION":
            ruleset = _adopted(record["fields"])
    return ruleset


def _adopted(fields: Mapping[str, Any]) -> dict[str, Any]:
    """The ruleset an adoption puts in force, with the doctrine pin it names, if any (§16.9, §28)."""

    ruleset = {"system": fields["system"], "policy": fields["policy"], "analyzers": fields["analyzers"]}
    if "doctrine" in fields:
        ruleset["doctrine"] = dict(fields["doctrine"])
    return ruleset


def _digest(body: Any) -> str:
    return "sha256:" + hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def manifest_decl(view: TreeView) -> dict[tuple[str, str], Any] | None:
    """``decl(T)`` of the observed tree's manifest; None when it does not parse (every key quarantined)."""

    manifest = view.manifest
    if isinstance(manifest, Manifest):
        return dict(manifest.decl)
    if manifest is None:
        return {}
    return None


__all__ = ["CheckpointInvalid", "DERIVATION_VERSION", "DEFAULT_MANIFEST_PATH", "History", "Integration", "RecordFact", "TreeSource", "manifest_decl"]
