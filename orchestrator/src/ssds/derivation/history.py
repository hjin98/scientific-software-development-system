"""S0 facts folded over the readable ledger prefix (catalogue §5.2).

Every fact here is a function of the authenticated chain and the trees it
names: the expected integration head ``E_k`` and observed tree ``T_k``,
effective structure ``Σ_k`` (a fold over admitted structural deltas, never a
stored copy), governance modes, the ruleset in force, loss boundaries,
integrations, and every record with the position that admitted it. Trees are
supplied by the caller, keyed by commit identity, so derivation reads no Git.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from functools import cached_property, lru_cache
from typing import Any

from ssds.content import DEFAULT_MANIFEST_PATH, Manifest, Structure, Tree, TreeView, decl_from_json, value_from_json
from ssds.ledger.read import Chain

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


class History:
    """S0 facts at every position of the readable prefix of one chain."""

    def __init__(self, chain: Chain, trees: TreeSource) -> None:
        if chain.genesis is None:
            raise ValueError("derivation needs a readable genesis")
        self.chain = chain
        self.trees = trees
        self.last = chain.readable_through
        genesis = chain.genesis["fields"]
        self.ledger_id = chain.ledger_id
        self.manifest_path = genesis["manifest_path"]
        self.policy_path = genesis["policy_path"]
        heads: list[str] = []
        sigmas: list[dict[tuple[str, str], Any]] = []
        modes: list[dict[str, dict[str, Any]]] = []
        rulesets: list[dict[str, Any]] = []
        self.integrations: dict[int, Integration] = {}
        self.records: dict[str, RecordFact] = {}
        self.boundaries: list[int] = []
        self.objects: dict[str, bytes] = {}
        head = genesis["baseline_commit"]
        sigma = decl_from_json(genesis["structure"])
        mode = {s: dict(m) for s, m in genesis["modes"].items()}
        ruleset = dict(chain.genesis["ruleset"])
        for entry in chain.entries[: self.last + 1]:
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
                        ruleset = {"system": fields["system"], "policy": fields["policy"],
                                   "analyzers": fields["analyzers"]}
                    elif record["kind"] == "LEDGER_LOSS":
                        self.boundaries.append(entry.position)
            carried = list(body["records"]) + ([body["lifecycle"]] if body["lifecycle"] else [])
            for record in carried:
                self.records.setdefault(record["id"], RecordFact(record, entry.position, body["entry_kind"]))
            heads.append(head)
            sigmas.append(sigma)
            modes.append(mode)
            rulesets.append(ruleset)
        self._heads = heads
        self._sigmas = sigmas
        self._modes = modes
        self._rulesets = rulesets

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


def manifest_decl(view: TreeView) -> dict[tuple[str, str], Any] | None:
    """``decl(T)`` of the observed tree's manifest; None when it does not parse (every key quarantined)."""

    manifest = view.manifest
    if isinstance(manifest, Manifest):
        return dict(manifest.decl)
    if manifest is None:
        return {}
    return None


__all__ = ["DEFAULT_MANIFEST_PATH", "History", "Integration", "RecordFact", "TreeSource", "manifest_decl"]
