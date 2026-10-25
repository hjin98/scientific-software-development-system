"""S0 in one state: quarantine, tenure, relations, well-formedness and closure (catalogue §1.6, §2, §4.5-§4.6, §5.2).

A state is the admitted state at a position or a transformation frame; both
are one observed tree under one effective structure (``TreeView``). Nothing
here reads a derived acceptance or validity; closure takes the currency of
completeness judgments as an argument, which only S2 supplies.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from functools import cached_property
from typing import Any

from ssds import analyzers
from ssds.content import ABSENT, RESIDUAL_SUFFIX, Structure, TreeView, static_errors

from .vocabulary import CHALLENGES_INQUIRY, DOMAIN_LAYERED, LAYER, LAYER_FREE, VOCABULARY

Decl = Mapping[tuple[str, str], Any]


@dataclass(frozen=True, order=True)
class Relation:
    subject: str
    type: str
    object: str
    provenance: str  # authored | derived
    attrs: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True, order=True)
class Defect:
    code: str
    unit: str
    detail: str


def strongly_connected(nodes: Iterable[str], edges: Iterable[tuple[str, str]]) -> list[frozenset[str]]:
    """Tarjan's strongly connected components, iteratively (no recursion limit)."""

    adjacency: dict[str, list[str]] = {}
    for a, b in edges:
        adjacency.setdefault(a, []).append(b)
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    on_stack: set[str] = set()
    stack: list[str] = []
    out: list[frozenset[str]] = []
    counter = 0
    for root in sorted(set(nodes) | set(adjacency)):
        if root in index:
            continue
        work = [(root, iter(sorted(adjacency.get(root, ()))))]
        index[root] = low[root] = counter
        counter += 1
        stack.append(root)
        on_stack.add(root)
        while work:
            node, children = work[-1]
            advanced = False
            for child in children:
                if child not in index:
                    index[child] = low[child] = counter
                    counter += 1
                    stack.append(child)
                    on_stack.add(child)
                    work.append((child, iter(sorted(adjacency.get(child, ())))))
                    advanced = True
                    break
                if child in on_stack:
                    low[node] = min(low[node], index[child])
            if advanced:
                continue
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[node])
            if low[node] == index[node]:
                component = set()
                while True:
                    item = stack.pop()
                    on_stack.discard(item)
                    component.add(item)
                    if item == node:
                        break
                out.append(frozenset(component))
    return out


def nontrivial(component: frozenset[str], edges: set[tuple[str, str]]) -> bool:
    return len(component) > 1 or any((n, n) in edges for n in component)


class StructureFacts:
    """S0 facts of one observed tree under one effective structure."""

    def __init__(self, view: TreeView, observed_decl: Decl | None) -> None:
        self.view = view
        self.structure: Structure = view.structure
        self.observed_decl = observed_decl  # decl(T); None when the manifest does not parse

    # -- quarantine and its classification (§1.6) ---------------------------------------

    @cached_property
    def quarantine(self) -> frozenset[tuple[str, str]]:
        sigma = self.structure.decl
        if self.observed_decl is None:
            return frozenset(sigma)
        keys = set(sigma) | set(self.observed_decl)
        return frozenset(k for k in keys if self.observed_decl.get(k) != sigma.get(k))

    def _signature_map(self, structure: Structure) -> dict[str, tuple[Any, ...]]:
        view = TreeView(self.view.tree, structure, self.view.manifest_path)
        out: dict[str, tuple[Any, ...]] = {}
        for uid, unit in structure.units.items():
            region = view.regions.get(uid)
            covered = tuple(sorted((s.path, s.start, s.end) for s in region)) if region else None
            out[uid] = (structure.kind(uid), structure.domain(uid), unit.role, unit.part_of, unit.subject,
                        view.scope_id(uid) if unit.subject else None, covered if unit.subject else None)
        out[""] = (view.governed_paths,)  # the governed boundary; "" is no unit identity
        return out

    @cached_property
    def _base_signature(self) -> dict[str, tuple[Any, ...]]:
        return self._signature_map(self.structure)

    def governance_affecting(self, key: tuple[str, str]) -> bool:
        """Whether applying this quarantined delta alone changes governance (§1.6)."""

        value = None if self.observed_decl is None else self.observed_decl.get(key)
        overridden = self.structure.override(key, value)
        if static_errors(overridden) != static_errors(self.structure) and static_errors(overridden):
            return True
        return self._signature_map(overridden) != self._base_signature

    @cached_property
    def affected_subjects(self) -> frozenset[str]:
        """``aff(Q)``: every effective subject a governance-affecting delta names or whose signature changes."""

        if not self.quarantine:
            return frozenset()
        decl = dict(self.structure.decl)
        if self.observed_decl is None:
            return frozenset(u for u, unit in self.structure.units.items() if unit.subject)
        for key in self.quarantine:
            value = self.observed_decl.get(key)
            if value is None:
                decl.pop(key, None)
            else:
                decl[key] = value
        overridden = Structure(decl)
        after = self._signature_map(overridden)
        before = self._base_signature
        named = {k[0] for k in self.quarantine if self.governance_affecting(k)}
        overridden_view = TreeView(self.view.tree, overridden, self.view.manifest_path)
        out = set()
        for uid, unit in self.structure.units.items():
            if not unit.subject:
                continue
            contained = set(self.view.inside(uid))
            if uid in overridden.units:
                contained |= set(overridden_view.inside(uid))  # a carve-out by a foreign declaration affects P
            if contained & named or before.get(uid) != after.get(uid):
                out.add(uid)
        return frozenset(out)

    # -- relations (§2) -------------------------------------------------------------------

    @cached_property
    def relations(self) -> tuple[Relation, ...]:
        rels = [Relation(s, t, o, "authored", tuple(sorted(a.items()))) for s, t, o, a in self.view.authored_relations()]
        rels.extend(self.derived_relations)
        return tuple(sorted(set(rels)))

    @cached_property
    def derived_relations(self) -> tuple[Relation, ...]:
        """``IMPORTS`` from the pinned Python analyzer, between the units whose terms resolve into the files."""

        tree = self.view.tree
        files_of: dict[str, set[str]] = {}
        for uid, resolutions in self.view.term_resolutions.items():
            for region in resolutions:
                for span in region or ():
                    files_of.setdefault(span.path, set()).add(uid)
        by_module: dict[str, set[str]] = {}
        for path in self.view.governed_paths:
            if analyzers.analyzer_for(path) == analyzers.python.ANALYZER_ID:
                for name in analyzers.python.module_names(path):
                    by_module.setdefault(name, set()).add(path)
        out = set()
        for path in self.view.governed_paths:
            if analyzers.analyzer_for(path) != analyzers.python.ANALYZER_ID or not tree[path].is_text_file:
                continue
            facts = analyzers.python.imports(path, tree[path].data)
            for module in facts.modules:
                for target in by_module.get(module, ()):
                    for subject in files_of.get(path, ()):
                        for obj in files_of.get(target, ()):
                            if subject != obj:
                                out.add(Relation(subject, "IMPORTS", obj, "derived"))
        return tuple(sorted(out))

    def prerequisites(self, unit: str, classes: frozenset[str]) -> set[str]:
        return {r.object for r in self.relations
                if r.subject == unit and VOCABULARY.get(r.type) and VOCABULARY[r.type].completeness in classes}

    # -- well-formedness (§2.4-§2.5, §1.7, §1.9) -------------------------------------------

    def _kind(self, uid: str) -> str | None:
        return self.structure.kind(uid)

    def _layer(self, uid: str, seen: frozenset[str] = frozenset()) -> int | None:
        kind = self._kind(uid)
        if kind in LAYER:
            return LAYER[kind]
        if kind in DOMAIN_LAYERED and uid not in seen:
            via = {"EVIDENCE_SPEC": "EVIDENCES", "GENERATED": "GENERATED_FROM"}.get(kind)
            layers = [self._layer(r.object, seen | {uid}) for r in self.relations if r.subject == uid and r.type == via]
            known = [x for x in layers if x is not None]
            return min(known) if known else None
        return None

    @cached_property
    def sdgs(self) -> tuple[tuple[str, str, frozenset[str]], ...]:
        """(declaring unit, group id, members) for every simultaneous-definition group."""

        out = []
        for d in self.view.semantic_declarations:
            if d["decl"] == "sdg":
                owner = d["unit"][: -len(RESIDUAL_SUFFIX)] if d["unit"].endswith(RESIDUAL_SUFFIX) else d["unit"]
                out.append((owner, d["id"], frozenset(d["members"])))
        return tuple(sorted(out, key=lambda g: (g[0], g[1])))

    @cached_property
    def defects(self) -> tuple[Defect, ...]:
        units = self.structure.units
        out: list[Defect] = [Defect(e.code, e.unit, e.detail) for e in static_errors(self.structure)]
        for rel in self.relations:
            spec = VOCABULARY.get(rel.type)
            if spec is None:
                out.append(Defect("RELATION_UNKNOWN_TYPE", rel.subject, rel.type))
                continue
            if rel.provenance not in spec.classes:
                out.append(Defect("RELATION_CLASS", rel.subject, f"{rel.type} is not {rel.provenance}"))
            if rel.object not in units:
                out.append(Defect("RELATION_OBJECT", rel.subject, f"{rel.type} names no effective unit {rel.object}"))
                continue
            subject_kind, object_kind = self._kind(rel.subject), self._kind(rel.object)
            if spec.layer == "NON_ASCENDING":
                ls, lo = self._layer(rel.subject), self._layer(rel.object)
                if ls is not None and lo is not None and lo > ls:
                    out.append(Defect("RELATION_LAYER", rel.subject, f"{rel.type} ascends to {rel.object}"))
            elif spec.layer.startswith("SUBJECT:"):
                allowed = spec.layer.split(":", 1)[1].split("|")
                if subject_kind not in allowed:
                    out.append(Defect("RELATION_SUBJECT_KIND", rel.subject, f"{rel.type} from a {subject_kind}"))
                if rel.type == "CHALLENGES" and dict(rel.attrs).get("inquiry") not in CHALLENGES_INQUIRY:
                    out.append(Defect("RELATION_ATTRIBUTE", rel.subject, "CHALLENGES needs inquiry"))
            elif spec.layer == "SAME_KIND" and subject_kind != object_kind:
                out.append(Defect("RELATION_SAME_KIND", rel.subject, f"{rel.type} across kinds"))
            if rel.subject == rel.object:
                out.append(Defect("RELATION_SELF", rel.subject, rel.type))
        groups = self.sdgs
        for owner, gid, members in groups:
            subjects = {self.structure.subj(m) for m in members}
            if any(m not in units for m in members) or len(subjects) != 1 or any(units[m].subject for m in members if m in units):
                out.append(Defect("SDG_MALFORMED", owner, f"group {gid}"))
        for i, (o1, g1, m1) in enumerate(groups):
            for o2, g2, m2 in groups[i + 1 :]:
                if m1 & m2 and not (m1 <= m2 or m2 <= m1):
                    out.append(Defect("SDG_NOT_LAMINAR", o1, f"{g1} and {g2}"))
        out.extend(self._cycle_defects())
        definers: dict[str, set[str]] = {}
        for d in self.view.semantic_declarations:
            if d["decl"] == "defines":
                owner = d["unit"][: -len(RESIDUAL_SUFFIX)] if d["unit"].endswith(RESIDUAL_SUFFIX) else d["unit"]
                definers.setdefault(d["object"], set()).add(owner)
        for name, owners in definers.items():
            if len(owners) > 1:
                out.extend(Defect("SINGLE_DEFINER", o, name) for o in owners)
        return tuple(sorted(set(out)))

    def _cycle_defects(self) -> list[Defect]:
        """Every cycle lies inside one SDG and uses only SIMULTANEOUS edges (§2.4)."""

        edges: set[tuple[str, str]] = set()
        cycle_class: dict[tuple[str, str], set[str]] = {}
        for rel in self.relations:
            spec = VOCABULARY.get(rel.type)
            if spec is None or rel.type == "CHALLENGES":
                continue
            if rel.provenance == "derived" and spec.cycle == "NEUTRAL":
                continue
            edges.add((rel.subject, rel.object))
            cycle_class.setdefault((rel.subject, rel.object), set()).add(spec.cycle)
        out = []
        groups = [m for _, _, m in self.sdgs]
        for component in strongly_connected(self.structure.units, edges):
            if not nontrivial(component, edges):
                continue
            inside = [e for e in edges if e[0] in component and e[1] in component]
            if not any(component <= g for g in groups) or any(cycle_class[e] != {"SIMULTANEOUS"} for e in inside):
                out.extend(Defect("ILLEGAL_CYCLE", u, f"cycle through {sorted(component)}") for u in component)
        return out

    def well_formed(self, subject: str) -> bool:
        members = {u for u in self.structure.units if self.structure.subj(u) == subject}
        return not any(d.unit in members for d in self.defects)

    def absent_term(self, subject: str) -> bool:
        """Some declared file or span term of the subject's units resolves to ``ABSENT`` (§1.9): no acceptance is
        admitted on such a revision (catalogue §8.3 step 3, ``AUTH_ILL_FORMED``)."""

        resolutions = self.view.term_resolutions
        for uid, unit in self.structure.units.items():
            if self.structure.subj(uid) != subject:
                continue
            if any(term.kind != "prefix" and region is ABSENT for term, region in zip(unit.scope, resolutions[uid])):
                return True
        return False

    # -- conservative widening and closure (§4.5-§4.6) --------------------------------------

    def chain(self, unit: str) -> list[frozenset[str]]:
        """The enclosing-scope chain of a unit, smallest first, ending with the whole governed tree."""

        steps: list[frozenset[str]] = [frozenset({unit})]
        for composite in self.structure.ancestors(unit):
            steps.append(frozenset({composite, *(u for u in self.structure.units if self.structure.is_member_of(u, composite))}))
        files = sorted({s.path for s in (self.view.regions.get(unit) or ())})
        directories: list[str] = []
        for path in files:
            parts = path.split("/")[:-1]
            for i in range(len(parts), -1, -1):
                prefix = "/".join(parts[:i]) + ("/" if i else "")
                if prefix not in directories:
                    directories.append(prefix)
        for prefix in sorted(directories, key=len, reverse=True):
            inside = set()
            for uid, region in self.view.regions.items():
                if region and all(s.path.startswith(prefix) for s in region):
                    inside.add(uid)
            steps.append(frozenset(inside))
        steps.append(self.whole_tree)
        out: list[frozenset[str]] = []
        for step in steps:
            merged = (out[-1] | step) if out else step
            if not out or merged != out[-1]:
                out.append(merged)
        return out

    @cached_property
    def whole_tree(self) -> frozenset[str]:
        return frozenset(self.structure.units)

    def closure(self, start: Iterable[str], classes: frozenset[str],
                complete: Callable[[frozenset[str], str], bool]) -> tuple[frozenset[str], bool]:
        """``closure(S, R)``: the least fixed point; ``unbounded`` when some reached unit had no bounding judgment."""

        reached = set(start)
        queue = list(reached)
        unbounded = False
        while queue:
            unit = queue.pop()
            new = self.prerequisites(unit, classes)
            bound = next((scope for scope in self.chain(unit) if all(complete(scope, c) for c in classes)), None)
            if bound is None:
                bound, unbounded = self.whole_tree, True
            new |= set(bound)
            for other in sorted(new - reached):
                reached.add(other)
                queue.append(other)
        return frozenset(reached), unbounded


def tenure_start(signatures: list[tuple[Any, ...] | None]) -> int | None:
    """The first position of the current uninterrupted run of an unchanged governance signature."""

    if not signatures or signatures[-1] is None:
        return None
    start = len(signatures) - 1
    while start > 0 and signatures[start - 1] == signatures[-1]:
        start -= 1
    return start
