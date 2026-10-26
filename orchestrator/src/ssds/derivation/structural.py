"""Validation step 4's structural owner (Manual §8.3 step 4 (a)-(c); catalogue §8.3 step 4, §1.9, §2.5, §7.4;
Phase F plan §3.1, step 4c-ii, readings F15, F16, F18).

One function of the admitted state at ``n`` and a transformation's frame there returns ``Σ_{n+1}``, the
classification of each declaration key against the quarantine ``Q_n``, and the step 4 findings. Admission reads
every finding (``admission``, 4c-iii). ``Frame.exists`` reads the findings ``X`` is responsible for
(catalogue §7.4: "``Δ_Σ(X)`` is well-formed"): every per-key, freeze, mode, release and semantic finding, and a
whole-structure finding only where ``Σ_n`` passes the same check (reading F18).

- **Per key (§8.3 4 (a)).** A key outside ``Q_n`` takes ``decl(M)[k]`` (authored, or unchanged). A key in
  ``Q_n`` realigns when ``decl(M)[k] = Σ_n[k]``, is carried when ``decl(M)[k] = decl(T_n)[k]``, and otherwise
  routes to revalidation (``STRUCT_REVALIDATE``). Where ``Σ_n ⊕ Δ_Σ(X)`` would differ from ``Σ_{n+1}`` (a key in
  ``Q_n`` that ``C`` authors to a foreign change's value), Manual §7.2 and the catalogue's precedence disagree,
  and the request is routed to revalidation (plan revision 7, R4). Adoption by ``ABSORB``
  cannot be expressed in schema 1 (``SCHEMA_UNSUPPORTED``, reading F16).
- **Well-formedness, over ``Σ_{n+1}`` on ``M``.** §1.9's static checks (``STRUCT_<code>``); scope conservation is
  their containment and sibling-disjointness checks with the residual part (§1.4 rule 2), so it has no code of
  its own; newly declared or changed file and span terms resolve (``STRUCT_TERM_UNRESOLVED``); the reserved
  leaves are declared (``STRUCT_RESERVED_LEAF``, reading F18); no unit's governing subject changes mode
  (``STRUCT_MODE_MIXED``: a ``MODE_TRANSITION`` never travels with a request); no existing unit's kind or
  owning domain changes (``SCHEMA_UNSUPPORTED``: no record expresses the old owner's release, reading F16).
- **Freeze (§8.3 4 (b)).** A subject whose current triple in ``D_n`` is ``REVOKED``, ``BLOCKED`` or
  ``PROVISIONAL`` keeps its signature, scope, region shape and membership: ``FREEZE_SOURCE`` where it changes or
  loses units, ``FREEZE_DESTINATION`` where it gains them. A region's shape is which paths it covers and whether
  each term resolves; an edit of bytes inside it is content, not structure.
- **Semantic structure (§8.3 4 (c), §2.5).** The S0 defects an affected subject has in the frame and not at the
  head, keyed by code, unit and detail (reading F15): ``RELATION_*`` under their own names, the SDG, cycle and
  single-definer defects as ``STRUCT_*`` members.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Any

from ssds.content import Structure, TreeView, static_errors

from .baseline import reserved_leaf_problems

from .history import manifest_decl
from .s0 import StructureFacts
from .state import triple_key

FROZEN = frozenset({"REVOKED", "BLOCKED", "PROVISIONAL"})
SEMANTIC_STRUCT = {"SDG_MALFORMED": "STRUCT_SDG_MALFORMED", "SDG_NOT_LAMINAR": "STRUCT_SDG_NOT_LAMINAR",
                   "ILLEGAL_CYCLE": "STRUCT_ILLEGAL_CYCLE", "SINGLE_DEFINER": "STRUCT_SINGLE_DEFINER"}
#: Findings over the whole structure: they count against a frame only where ``Σ_n`` passes the same check (F18).
WHOLE_STRUCTURE = "whole"


@dataclass(frozen=True)
class Finding:
    code: str
    unit: str
    detail: str
    scope: str = "request"  # "request": the request is responsible; WHOLE_STRUCTURE: a check of all of Σ_{n+1}


class StructuralCheck:
    """Step 4 (a)-(c) for ``frame`` against the admitted state ``admitted`` at the frame's position."""

    def __init__(self, admitted: Any, frame: Any) -> None:
        self.s = admitted
        self.frame = frame
        self.h = frame.h
        self.manifest = frame.h.manifest_path

    # -- (a) the effective-structure delta ----------------------------------------------------

    @cached_property
    def merged_decl(self) -> dict[tuple[str, str], Any] | None:
        return manifest_decl(TreeView(self.frame.merged, Structure({}), self.manifest))

    @cached_property
    def _per_key(self) -> tuple[dict[tuple[str, str], Any], dict[tuple[str, str], str]]:
        sigma = dict(self.h.sigma(self.frame.n))
        head = self.frame.head_view
        observed = manifest_decl(head)
        quarantine = StructureFacts(head, observed).quarantine
        merged = self.merged_decl or {}
        out, classes = dict(sigma), {}
        for key in sorted(set(sigma) | set(merged) | set(observed or {}) | set(quarantine)):
            value = merged.get(key)
            if key not in quarantine:
                if value != sigma.get(key):
                    classes[key] = "AUTHORED"
                    if value is None:
                        out.pop(key, None)
                    else:
                        out[key] = value
            elif value == sigma.get(key):
                classes[key] = "REALIGNED"
            elif observed is not None and value == observed.get(key):
                classes[key] = "CARRIED"
            else:
                classes[key] = "REVALIDATE"
        return out, classes

    @property
    def sigma(self) -> dict[tuple[str, str], Any]:
        """``Σ_{n+1}``."""

        return self._per_key[0]

    @property
    def classes(self) -> dict[tuple[str, str], str]:
        """Each changed or quarantined key's class: ``AUTHORED``, ``REALIGNED``, ``CARRIED`` or ``REVALIDATE``."""

        return self._per_key[1]

    @cached_property
    def structure(self) -> Structure:
        return Structure(self.sigma)

    @cached_property
    def view(self) -> TreeView:
        """``M_n(X)`` under ``Σ_{n+1}``."""

        return TreeView(self.frame.merged, self.structure, self.manifest)

    # -- the findings ----------------------------------------------------------------------------

    @cached_property
    def findings(self) -> tuple[Finding, ...]:
        if self.frame.merged is None:
            return ()  # no merge: no frame and no structure to check (§7.4)
        out: list[Finding] = []
        if self.merged_decl is None:
            out.append(Finding("STRUCT_MANIFEST_UNPARSED", "ssds.manifest", "the merged manifest does not parse"))
            return tuple(out)
        if self.frame.x.adopts:
            out.append(Finding("SCHEMA_UNSUPPORTED", "", "adoption by ABSORB (Q-F6 (i))"))
        for key, cls in sorted(self.classes.items()):
            if cls == "REVALIDATE":
                out.append(Finding("STRUCT_REVALIDATE", key[0], f"{key[1]}: a quarantined key changed to a third value"))
        if dict(self.frame.structure.decl) != self.sigma:
            differing = sorted(k for k in set(self.frame.structure.decl) | set(self.sigma)
                               if self.frame.structure.decl.get(k) != self.sigma.get(k))
            for key in differing:
                out.append(Finding("STRUCT_REVALIDATE", key[0],
                                   f"{key[1]}: authored to a quarantined value; the frame and the integration differ"))
        out += self._whole_structure()
        out += self._release_and_modes()
        out += self._freeze()
        out += self._semantic()
        return tuple(sorted(set(out), key=lambda f: (f.code, f.unit, f.detail)))

    def _whole_structure(self) -> list[Finding]:
        head = Structure(dict(self.h.sigma(self.frame.n)))
        before_static = {(e.code, e.unit, e.detail) for e in static_errors(head)}
        out = [Finding(f"STRUCT_{e.code}", e.unit, e.detail,
                       WHOLE_STRUCTURE if (e.code, e.unit, e.detail) in before_static else "request")
               for e in static_errors(self.structure)]
        before_reserved = set(reserved_leaf_problems(head))
        out += [Finding("STRUCT_RESERVED_LEAF", unit, detail,
                        WHOLE_STRUCTURE if (unit, detail) in before_reserved else "request")
                for unit, detail in reserved_leaf_problems(self.structure)]
        out += [Finding("STRUCT_TERM_UNRESOLVED", unit, "a newly declared or changed term resolves to nothing")
                for unit in self.view.unresolved_declared_terms(head)]
        return out

    def _release_and_modes(self) -> list[Finding]:
        before, after = self.frame.head_view.structure, self.structure
        out = []
        for uid in sorted(set(before.units) & set(after.units)):
            if before.kind(uid) != after.kind(uid) or before.domain(uid) != after.domain(uid):
                out.append(Finding("SCHEMA_UNSUPPORTED", uid, "a kind or domain change needs the old owner's release (Q-F6 (ii))"))
            old, new = before.subj(uid), after.subj(uid)
            if old and new and self._mode(old) != self._mode(new):
                out.append(Finding("STRUCT_MODE_MIXED", uid, f"its subject moves from {old} to {new} across modes"))
        return out

    def _mode(self, subject: str) -> str:
        return self.h.mode(self.frame.n, subject).get("mode", "UNGOVERNED")

    def _freeze(self) -> list[Finding]:
        before, after = self.frame.head_view, self.view
        out = []
        for uid, unit in sorted(before.structure.units.items()):
            if not unit.subject:
                continue
            if self.s.status1(triple_key(*self.s.subject_triple(uid))) not in FROZEN:
                continue
            members_before = self._members(before.structure, uid)
            members_after = self._members(after.structure, uid) if uid in after.structure.units else frozenset()
            if members_after - members_before:
                out.append(Finding("FREEZE_DESTINATION", uid, f"gains {sorted(members_after - members_before)}"))
            if members_before - members_after or self._shape(before, uid) != self._shape(after, uid):
                out.append(Finding("FREEZE_SOURCE", uid, "its signature, scope, region shape or membership changes"))
        return out

    @staticmethod
    def _members(structure: Structure, subject: str) -> frozenset[str]:
        return frozenset(u for u in structure.units if u != subject and structure.subj(u) == subject)

    def _shape(self, view: TreeView, uid: str) -> tuple[Any, ...] | None:
        structure = view.structure
        if uid not in structure.units:
            return None
        unit = structure.units[uid]
        region = view.regions.get(uid) or ()
        resolved = tuple(view.term_region(t) is not None for t in unit.scope)
        return (unit.subject, view.scope_id(uid), structure.kind(uid), self._mode(uid), structure.keys_of(uid),
                frozenset(span.path for span in region), resolved)

    def _semantic(self) -> list[Finding]:
        head = StructureFacts(self.frame.head_view, manifest_decl(self.frame.head_view))
        frame = StructureFacts(self.view, self.merged_decl)
        static = {(e.code, e.unit, e.detail) for e in static_errors(self.structure)}
        before = {(d.code, d.unit, d.detail) for d in head.defects}
        affected = set(self.frame.write_set)
        affected |= {self.structure.subj(u) for u in affected if u in self.structure.units} - {None}
        out = []
        for d in frame.defects:
            key = (d.code, d.unit, d.detail)
            if key in static or key in before or d.unit not in affected:
                continue
            out.append(Finding(SEMANTIC_STRUCT.get(d.code, d.code), d.unit, d.detail))
        return out

    # -- the readers ----------------------------------------------------------------------------

    @property
    def frame_findings(self) -> tuple[Finding, ...]:
        """What makes ``Δ_Σ(X)`` ill-formed (catalogue §7.4): every finding but a whole-structure one ``Σ_n``
        already fails (reading F18)."""

        return tuple(f for f in self.findings if f.scope != WHOLE_STRUCTURE)


__all__ = ["FROZEN", "Finding", "StructuralCheck", "reserved_leaf_problems"]
