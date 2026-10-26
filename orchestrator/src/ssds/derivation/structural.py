"""Validation step 4's structural owner (Manual §8.3 step 4 (a)-(c); catalogue §8.3 step 4, §1.9, §2.5, §7.4;
Phase F plan §3.1, step 4c-ii, readings F15, F16, F18).

One function of the admitted state at ``n`` and a transformation's frame there returns ``Σ_{n+1}``, the
classification of each declaration key against the quarantine ``Q_n``, and the step 4 findings. Admission reads
every finding (``admission``, 4c-iii), and so does ``Frame.exists`` (Manual §7.4: "every structural check except
the enactment condition"; reading F18).

- **Per key (§8.3 4 (a)).** A key outside ``Q_n`` takes ``decl(M)[k]`` (authored, or unchanged). A key in
  ``Q_n`` realigns when ``decl(M)[k] = Σ_n[k]``, is carried when ``decl(M)[k] = decl(T_n)[k]``, and otherwise
  routes to revalidation (``STRUCT_REVALIDATE``). Where ``Σ_n ⊕ Δ_Σ(X)`` would differ from ``Σ_{n+1}`` (a key in
  ``Q_n`` that ``C`` authors to a foreign change's value), Manual §7.2 and the catalogue's precedence disagree,
  and the request is routed to revalidation (plan revision 7, R4). A key in ``Q_n`` that a records-only
  adoption (``X = (B, B, A)``) adopts by ``ABSORB`` at its observed value is ``ADOPTED``, validated exactly as if
  authored (§18.4, SD-69); an adopted value that is not the observed delta routes to revalidation, and an
  adoption with a candidate is ``SCHEMA_UNSUPPORTED`` (plan revision 15).
- **Well-formedness, over ``Σ_{n+1}`` on ``M``.** §1.9's static checks (``STRUCT_<code>``); scope conservation is
  their containment and sibling-disjointness checks with the residual part (§1.4 rule 2), so it has no code of
  its own; newly declared or changed file and span terms resolve (``STRUCT_TERM_UNRESOLVED``); the reserved
  leaves are declared (``STRUCT_RESERVED_LEAF``, reading F18); no unit's governing subject changes mode
  (``STRUCT_MODE_MIXED``: a ``MODE_TRANSITION`` never travels with a request); no existing unit's kind or
  owning domain changes (``SCHEMA_UNSUPPORTED``: no record expresses the old owner's release, reading F16).
- **Freeze (§8.3 4 (b)).** A subject whose current triple in ``D_n`` is ``REVOKED``, ``BLOCKED`` or
  ``PROVISIONAL`` keeps its signature, declarations, regions and membership (every unit inside it by
  ``part_of``, nested subjects included): ``FREEZE_SOURCE`` where it changes or loses units,
  ``FREEZE_DESTINATION`` where it gains them. Its regions are compared as their terms' resolution status; bytes,
  files under a prefix and anchor lines are content, which a challenge's resolution works through (reading F20).
- **Semantic structure (§8.3 4 (c), §2.5).** The S0 defects an affected subject, or any unit of one, has in the
  frame and not at the head, keyed by code, unit and detail (reading F15): ``RELATION_*`` under their own names, the SDG, cycle and
  single-definer defects as ``STRUCT_*`` members.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Any

from ssds.content import RESIDUAL_SUFFIX, Structure, TreeView, static_errors, value_from_json

from .baseline import reserved_leaf_problems

from .history import manifest_decl
from .s0 import StructureFacts
from .state import triple_key

FROZEN = frozenset({"REVOKED", "BLOCKED", "PROVISIONAL"})
SEMANTIC_STRUCT = {"SDG_MALFORMED": "STRUCT_SDG_MALFORMED", "SDG_NOT_LAMINAR": "STRUCT_SDG_NOT_LAMINAR",
                   "ILLEGAL_CYCLE": "STRUCT_ILLEGAL_CYCLE", "SINGLE_DEFINER": "STRUCT_SINGLE_DEFINER"}


@dataclass(frozen=True)
class Finding:
    code: str
    unit: str
    detail: str


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
        quarantine = self.s.s0.quarantine  # the admitted state's: T_n under Σ_n, as ``head`` is
        merged = self.merged_decl or {}
        adopted = {key: value_from_json(key[1], value) for key, value in self.frame.x.adopts}
        out, classes = dict(sigma), {}
        for key in sorted(set(sigma) | set(merged) | set(observed or {}) | set(quarantine)):
            value = merged.get(key)
            if key in quarantine and key in adopted and adopted[key] == value:
                classes[key] = "ADOPTED"  # adopted by ABSORB: validated exactly as if authored (§18.4)
                if value is None:
                    out.pop(key, None)
                else:
                    out[key] = value
            elif key not in quarantine:
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

        if self.sigma == dict(self.frame.structure.decl):
            return self.frame.view  # the same tree under the same structure: reuse it
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
        x = self.frame.x
        if x.adopts and x.base != x.candidate:
            out.append(Finding("SCHEMA_UNSUPPORTED", "", "adoption with a candidate (revision 15)"))
        for key, _ in x.adopts:
            if self.classes.get(tuple(key)) != "ADOPTED":
                out.append(Finding("STRUCT_REVALIDATE", key[0], f"{key[1]}: an adopted value that is not the observed delta"))
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
        out = [Finding(f"STRUCT_{e.code}", e.unit, e.detail) for e in static_errors(self.structure)]
        out += [Finding("STRUCT_RESERVED_LEAF", unit, detail) for unit, detail in reserved_leaf_problems(self.structure)]
        out += [Finding("STRUCT_TERM_UNRESOLVED", unit, "a newly declared or changed term resolves to nothing")
                for unit in self.view.unresolved_declared_terms(head)]
        return out

    def _release_and_modes(self) -> list[Finding]:
        before, after = self.frame.head_view.structure, self.structure
        out = []
        for uid in sorted(set(after.units) - set(before.units)):
            for source in after.units[uid].renamed_from:  # a rename carrying another kind escapes the release (F16)
                if source in before.units and (before.kind(source) != after.kind(uid)
                                               or before.domain(source) != after.domain(uid)):
                    out.append(Finding("SCHEMA_UNSUPPORTED", uid, f"renamed from {source} with another kind or domain"))
        for uid in sorted(set(before.units) & set(after.units)):
            if before.kind(uid) != after.kind(uid) or before.domain(uid) != after.domain(uid):
                out.append(Finding("SCHEMA_UNSUPPORTED", uid, "a kind or domain change needs the old owner's release (Q-F6 (ii))"))
            old, new = before.subj(uid), after.subj(uid)
            if old and new and self._mode(old) != self._mode(new):
                out.append(Finding("STRUCT_MODE_MIXED", uid, f"its subject moves from {old} to {new} across modes"))
        return out

    @cached_property
    def tenure_starts(self) -> tuple[str, ...]:
        """The subjects integrating ``X`` would promote (a part made a subject) or restore (a subject returning
        after its tenure ended), whose tenure §7.6's enactment condition binds to a prospective acceptance (§19.4).
        A subject declared under a new name counts by its ``renamed_from`` lineage too (§1.11; review 23b487a B3).
        A newly declared subject is neither."""

        head = self.frame.head_view.structure
        earlier = self.h.former_subjects(self.frame.n)
        out = []
        for uid, unit in sorted(self.structure.units.items()):
            if not unit.subject or (uid in head.units and head.units[uid].subject):
                continue
            sources = {uid, *unit.renamed_from}
            # a head part, or a former subject absent at the head, makes it a promotion or restoration; a source
            # that is a head subject (an ordinary rename) contributes nothing but vetoes no other (re-check 88d9a74)
            if any((src in head.units and not head.units[src].subject) or (src not in head.units and src in earlier)
                   for src in sources):
                out.append(uid)
        return tuple(out)

    def _mode(self, subject: str) -> str:
        return self.h.mode(self.frame.n, subject).get("mode", "UNGOVERNED")

    def _freeze(self) -> list[Finding]:
        """The subject compared on the one merged tree under ``Σ_n`` and under ``Σ_{n+1}``, so only a declaration
        can move it (reading F20; re-check ad8daeb RB1): a unit overlapping it, an ``ignore`` entry or a stranger
        nested in it changes its regions or owned bytes there, while an edit, a file added under its prefix or a
        moved anchor is the same on both sides."""

        before = TreeView(self.frame.merged, self.frame.head_view.structure, self.manifest)
        after = self.view
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
            if members_before - members_after or self._shape(before, uid) != self._shape(after, uid) \
                    or self._held(before, uid) != self._held(after, uid):
                out.append(Finding("FREEZE_SOURCE", uid, "its signature, scope, regions or membership changes"))
        return out

    @staticmethod
    def _held(view: TreeView, uid: str) -> tuple[Any, ...] | None:
        """``uid``'s region and the bytes it and its members own, by owner, in ``view``."""

        structure = view.structure
        if uid not in structure.units:
            return None
        family = {uid} | {u for u in structure.units if structure.is_member_of(u, uid)}
        owned = sorted((owner, path, mode, data) for owner, files in view.owned.items()
                       if owner.removesuffix(RESIDUAL_SUFFIX) in family for path, (mode, data) in files.items())
        return view.regions.get(uid), tuple(owned)

    @staticmethod
    def _members(structure: Structure, subject: str) -> frozenset[str]:
        """Every unit inside ``subject`` by membership, nested subjects included (review 2aadf33 B2)."""

        return frozenset(u for u in structure.units if u != subject and structure.is_member_of(u, subject))

    def _shape(self, view: TreeView, uid: str) -> tuple[Any, ...] | None:
        structure = view.structure
        if uid not in structure.units:
            return None
        unit = structure.units[uid]
        resolved = tuple(view.term_region(t) is not None for t in unit.scope)
        return (unit.subject, view.scope_id(uid), structure.kind(uid), self._mode(uid), structure.keys_of(uid),
                resolved)

    def _semantic(self) -> list[Finding]:
        head = self.s.s0  # the admitted state's S0 facts: T_n under Σ_n
        frame = StructureFacts(self.view, self.merged_decl)
        static = {(e.code, e.unit, e.detail) for e in static_errors(self.structure)}
        before = {(d.code, d.unit, d.detail) for d in head.defects}
        affected = set(self.frame.write_set)
        affected |= {self.structure.subj(u) for u in affected if u in self.structure.units} - {None}
        out = []
        for d in frame.defects:
            key = (d.code, d.unit, d.detail)
            if key in static or key in before or (d.unit not in affected and self.structure.subj(d.unit) not in affected):
                continue
            out.append(Finding(SEMANTIC_STRUCT.get(d.code, d.code), d.unit, d.detail))
        return out

def adoption_codes(state: Any, head: str, elements: Any, named: set[tuple[str, tuple[str, ...]]]) -> set[str]:
    """Step 4's checks of a records-only adoption (Phase F 4c-iv; SD-69, readings F21): ``elements`` are the
    request's ``adopted_deltas``, ``{absorption, key, value}`` each, and ``named`` the deltas its ``ABSORB``
    dispositions name. They must be the same deltas, each the key's current delta at its observed value
    (``REF_ADOPTION``). The adoption is then judged as the frame record of ``X = (B, B, A)`` at the head: the
    structural owner's codes, and a promotion or restoration failing closed (no prospective acceptance can travel
    with a records-only request)."""

    from ssds.ledger.read import transformation_id

    from .frames import Frame, Transformation

    pairs = set()
    for element in elements if isinstance(elements, list) else []:
        if not isinstance(element, dict) or set(element) != {"absorption", "key", "value"} \
                or not isinstance(element["key"], list) or len(element["key"]) != 2:
            return {"REF_ADOPTION"}
        key = tuple(element["key"])
        current = state.current_delta(key)
        if current is None or current[0] != element["absorption"] \
                or value_from_json(key[1], element["value"]) != current[1]:
            return {"REF_ADOPTION"}
        pairs.add((element["absorption"], key))
    if not pairs or pairs != named:
        return {"REF_ADOPTION"}
    adopts = tuple((tuple(e["key"]), e["value"]) for e in elements)
    x = Transformation(transformation_id(head, head, elements), head, head, adopts)
    check = Frame(state.h, state.n, x, None).structural
    codes = {f.code for f in check.findings}
    if check.tenure_starts:
        codes.add("SCHEMA_UNSUPPORTED")  # a promoting or restoring adoption (§18.4; revision 13)
    return codes


__all__ = ["FROZEN", "Finding", "StructuralCheck", "adoption_codes"]
