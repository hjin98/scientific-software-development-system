"""Transformation frames: identity, the frame state, basis-entry roles and existence (catalogue §7.1-§7.4).

At admitted head ``n`` the frame ``D_n[X]`` of ``X = (B, C, A)`` is derivation
over the same ledger prefix with the observed tree replaced by the pinned merge
``M_n(X)`` of ``tree(C)`` onto ``T_n`` with base ``tree(B)``, and effective
structure replaced by ``Σ_n ⊕ Δ_Σ(X)``. Without a clean merge or a well-formed
``Δ_Σ(X)`` the frame does not exist (§7.4); machinery never resolves a conflict.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property
from typing import Any

from ssds.content import Structure, Tree, TreeView, merge3, static_errors, value_from_json, write_set
from ssds.ledger.read import submits

from .history import History, manifest_decl
from .state import F, T, State


@dataclass(frozen=True)
class Transformation:
    id: str
    base: str
    candidate: str
    adopts: tuple[tuple[tuple[str, str], Any], ...] = field(default=())


def transformation_of(state: State, transformation_id: str) -> Transformation | None:
    """``X`` as the task result that first submitted it fixed it (§7.1)."""

    for rid in state.of_kind("TASK_RESULT"):
        target = state.record(rid)["target"]
        if target.get("transformation") == transformation_id and submits(target):
            adopts = tuple((tuple(a["key"]), a["value"]) for a in target.get("adopts", []))
            return Transformation(transformation_id, target["base"], target["candidate"], adopts)  # type: ignore[arg-type]
    return None


class Frame:
    """``D_n[X]``: the view a frame state evaluates in, plus the facts its roles read."""

    def __init__(self, history: History, position: int, x: Transformation, enactment: str | None) -> None:
        self.h = history
        self.n = position
        self.x = x
        self.enactment = enactment
        manifest = history.manifest_path
        self.base_tree: Tree = history.trees(x.base)
        self.candidate_tree: Tree = history.trees(x.candidate)
        self.head_tree: Tree = history.tree(position)
        self.merged, self.conflict = merge3(self.base_tree, self.head_tree, self.candidate_tree, manifest)
        sigma = dict(history.sigma(position))
        for key, value in self.structure_delta.items():
            if value is None:
                sigma.pop(key, None)
            else:
                sigma[key] = value
        self.structure = Structure(sigma)
        self.view = TreeView(self.merged if self.merged is not None else self.head_tree, self.structure, manifest)

    @cached_property
    def structure_delta(self) -> dict[tuple[str, str], Any]:
        """``Δ_Σ(X)``: the declaration changes ``C`` authors relative to ``B``, with the adopted deltas ``A``."""

        manifest = self.h.manifest_path
        before = manifest_decl(TreeView(self.base_tree, Structure({}), manifest)) or {}
        after = manifest_decl(TreeView(self.candidate_tree, Structure({}), manifest)) or {}
        delta = {k: after.get(k) for k in set(before) | set(after) if before.get(k) != after.get(k)}
        for key, value in self.x.adopts:
            delta[key] = value_from_json(key[1], value)
        return delta

    @cached_property
    def exists(self) -> bool:
        """A clean merge and a well-formed structure (§7.4); the enactment condition is Admission's."""

        if self.merged is None:
            return False
        return not static_errors(self.structure)

    @property
    def head_view(self) -> TreeView:
        """``T_n`` under ``Σ_n``: the write set's head side (§1.2)."""

        return self.h.view(self.n)

    def _modes(self, structure: Structure) -> dict[str, str]:
        return {u: self.h.mode(self.n, structure.subj(u) or u).get("mode", "UNGOVERNED") for u in structure.units}

    @cached_property
    def write_set(self) -> dict[str, frozenset[str]]:
        """The one write set of ``X`` (§1.2): ``T_n`` under ``Σ_n`` against ``M_n(X)`` under ``Σ_n ⊕ Δ_Σ(X)``,
        with each side's governance modes; empty when the merge conflicts."""

        if self.merged is None:
            return {}
        head = self.head_view
        return write_set(head, self.view, self._modes(head.structure), self._modes(self.structure))

    @cached_property
    def changed_files(self) -> dict[str, tuple[bytes | None, bytes | None]]:
        """Path -> (``T_n`` bytes, ``M_n(X)`` bytes) for every file the merge changes; empty on a conflict."""

        if self.merged is None:
            return {}
        head, merged = self.head_tree, self.merged
        out = {}
        for path in sorted(set(head) | set(merged)):
            before = head[path].data if path in head else None
            after = merged[path].data if path in merged else None
            if before != after:
                out[path] = (before, after)
        return out

    @cached_property
    def _base_view(self) -> TreeView:
        return TreeView(self.base_tree, self.structure, self.h.manifest_path)

    @cached_property
    def _candidate_view(self) -> TreeView:
        return TreeView(self.candidate_tree, self.structure, self.h.manifest_path)

    @cached_property
    def changed(self) -> frozenset[str]:
        """``Δ(X)``: the effective units whose revision in ``tree(C)`` differs from ``tree(B)``."""

        return frozenset(u for u in self.structure.units if self._base_view.rev(u) != self._candidate_view.rev(u))

    @property
    def base_view(self) -> TreeView:
        """``tree(B)`` under the frame's structure."""

        return self._base_view

    @property
    def candidate_view(self) -> TreeView:
        """``tree(C)`` under the frame's structure."""

        return self._candidate_view

    def candidate_rev(self, unit: str) -> str | None:
        """The revision ``tree(C)`` gives ``unit`` under the frame's structure."""

        return self._candidate_view.rev(unit) if unit in self.structure.units else None

    def role(self, unit: str, rev: str) -> str:
        """The role of a ``content`` entry ``(u, r)`` of a frame-``X`` record (§7.3)."""

        if unit not in self.changed:
            return "context"
        if rev == self._base_view.rev(unit):
            return "before-image"
        if rev == self._candidate_view.rev(unit):
            return "output"
        return "never"


def integrating_position(state: State, transformation_id: str) -> int | None:
    """The admission at or before ``state``'s position that integrated ``X``, if any."""

    found = [k for k, i in state.h.integrations.items() if k <= state.n and i.transformation == transformation_id]
    return min(found) if found else None


def frame_of(state: State, x: Transformation) -> Frame:
    """``X``'s frame where its checks read it (reading F17): at ``state``'s head while ``X`` is unintegrated;
    once integrated at ``k``, its tree and structure facts fixed at ``k - 1``, the head its integration merged
    onto. Currency is never read from the second: an integrated enactment's records are current in the
    admitted state (catalogue §7.3)."""

    k = integrating_position(state, x.id)
    return Frame(state.h, state.n if k is None else k - 1, x, state.enactment(x.id))


def role_sat(frame: Frame, unit: str, rev: str, in_frame: bool, ordinary: int) -> int:
    """``sat`` of a frame record's content entry by its role, in the frame or after integration."""

    role = frame.role(unit, rev)
    if role == "never":
        return F
    if role == "before-image":
        if not in_frame:
            return T  # after the integrating admission: a fixed fact about what it transformed
        return T if unit in frame.h.view(frame.n).structure.units and frame.h.view(frame.n).rev(unit) == rev else F
    return ordinary  # output and context: ordinary currency in the state at hand


def frame_state(history: History, position: int, transformation_id: str, base_state: State) -> State | None:
    """The state ``D_n[X]``, or None when ``X`` is unknown or its frame does not exist."""

    x = transformation_of(base_state, transformation_id)
    if x is None:
        return None
    frame = Frame(history, position, x, base_state.enactment(transformation_id))
    if not frame.exists:
        return None
    return State(history, position, frame)
