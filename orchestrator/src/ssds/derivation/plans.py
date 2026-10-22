"""Plan facts: lint and the plan invariants, control tightening and partition lint (catalogue §11.3, §13.2-§13.7).

All of it is S3 and mechanical, a function of the plan unit's content in a
state and of ``Σ`` there; Admission enforces lint at plan-unit admission in
Phase F, and until then a plan failing lint leaves its changed items
non-issuable (Phase E reading E5). Lint establishes form only (§13.2).

Write scopes, affected units and protected surfaces resolve to byte regions of
the state's tree: a unit to its region, ``dir/`` to every governed file under
it, any other path to that whole file (which may not exist yet). Containment
and intersection are by bytes, so naming a unit's whole file is never narrower
than naming the unit.
"""

from __future__ import annotations

import hashlib
from collections.abc import Iterable
from dataclasses import dataclass
from functools import cached_property
from typing import Any

from ssds.content import (
    ABSENT,
    REVIEW,
    Check,
    EvidenceVerifier,
    Item,
    ItemFailure,
    ItemPart,
    Plan,
    TreeView,
    jcs,
    parse_term,
    plans,
)

from .library import check_problems
from .state import BUDGET_CAP, Policy

#: Atoms: ("prefix", p), ("file", path) or ("span", path, start, end).
Atom = tuple[Any, ...]
IMPLEMENTER = frozenset({"IMPLEMENT", "REPAIR", "MIGRATE", "AUTHOR", "DOCUMENT"})
NOT_AUTHORITY = frozenset({"IMPLEMENT", "REPAIR", "MIGRATE", "DOCUMENT"})
#: Item layer for dependency direction (Phase E reading E21): an item depends only on its own or higher layers.
_LAYER = {"D1": 1, "D2": 2, "D3": 3}


@dataclass(frozen=True, order=True)
class LintFinding:
    code: str  # PARSE | OBJECTIVE | TOPOLOGY | UNRESOLVED | REF | SCOPE | DOMAIN | GATES | VERIFIER | SLOTS | COVERAGE | BUDGET
    item: str | None  # the item part, or None for a plan-level finding
    detail: str


# -- scopes as byte regions ---------------------------------------------------------------------------


def resolve(view: TreeView, entries: Iterable[str]) -> tuple[list[Atom], list[str]]:
    """Atoms of scope entries in ``view``, and the entries that do not resolve."""

    atoms: list[Atom] = []
    problems: list[str] = []
    for entry in entries:
        if entry in view.structure.units:
            region = view.regions.get(entry)
            if region is ABSENT or region is None:
                problems.append(f"unit {entry} is ABSENT")
                continue
            atoms.extend(("span", s.path, s.start, s.end) for s in region)
            continue
        try:
            term = parse_term({"prefix": entry} if entry.endswith("/") else {"path": entry})
        except Exception:  # noqa: BLE001 - the term grammar's own refusal
            problems.append(f"{entry!r} is neither a unit nor a path")
            continue
        atoms.append(("prefix", term.file) if term.kind == "prefix" else ("file", term.file))
    return atoms, problems


def _length(view: TreeView, path: str) -> int | None:
    entry = view.tree.get(path)
    return len(entry.data) if entry is not None else None


def _within(view: TreeView, inner: Atom, outer: Atom) -> bool:
    kind = outer[0]
    if kind == "prefix":
        return inner[1].startswith(outer[1])
    if inner[0] == "prefix":
        return False
    if kind == "file":
        return inner[1] == outer[1]
    if inner[1] != outer[1]:
        return False
    if inner[0] == "file":
        length = _length(view, inner[1])
        return length is not None and outer[2] == 0 and outer[3] >= length
    return outer[2] <= inner[2] and inner[3] <= outer[3]


def contained(view: TreeView, inner: list[Atom], outer: list[Atom]) -> bool:
    """Every inner atom lies inside one outer atom (spans of one file may also be covered by several)."""

    for atom in inner:
        if any(_within(view, atom, o) for o in outer):
            continue
        if atom[0] == "span":
            spans = sorted((o[2], o[3]) for o in outer if o[0] == "span" and o[1] == atom[1])
            reach = atom[2]
            for start, end in spans:
                if start <= reach < end:
                    reach = end
            if reach >= atom[3]:
                continue
        return False
    return True


def intersects(view: TreeView, atoms: list[Atom], path: str, start: int, end: int) -> bool:
    for atom in atoms:
        if atom[0] == "prefix" and path.startswith(atom[1]):
            return True
        if atom[0] == "file" and atom[1] == path:
            return True
        if atom[0] == "span" and atom[1] == path and atom[2] < end and start < atom[3]:
            return True
        if atom[0] == "span" and atom[1] == path and start == end == atom[2]:
            return True
    return False


def units_in(view: TreeView, atoms: list[Atom]) -> frozenset[str]:
    """Every unit whose region meets the atoms."""

    found = set()
    for uid, region in view.regions.items():
        if region is ABSENT or region is None:
            continue
        if any(intersects(view, atoms, s.path, s.start, s.end) for s in region):
            found.add(uid)
    return frozenset(found)


# -- control tightening (§13.4) ----------------------------------------------------------------------


def tightens(old: Item, old_prose: bytes, new: Item, new_prose: bytes, view: TreeView) -> bool:
    """``old ⊑ new``: byte-identical prose and every field unchanged or moved in its tightening direction."""

    if old_prose != new_prose:
        return False
    fixed = ("id", "kind", "authority", "specialist", "objective", "governing", "acceptance_criteria", "affected",
             "gates", "depends_on")
    if any(getattr(old, name) != getattr(new, name) for name in fixed):
        return False
    a, b = old.contract, new.contract
    if a is None or b is None:
        return a is b
    if b.scientific != a.scientific and not (a.scientific == "NOT_APPLIES" and b.scientific == "APPLIES"):
        return False
    if b.budget > a.budget:
        return False
    old_scope, old_problems = resolve(view, a.write_scope)
    new_scope, new_problems = resolve(view, b.write_scope)
    if old_problems or new_problems or not contained(view, new_scope, old_scope):
        return False
    old_deps, new_deps = dict(a.dependencies), dict(b.dependencies)
    if not set(new_deps) <= set(old_deps) or any(not set(v) <= set(old_deps[k]) for k, v in new_deps.items()):
        return False
    if not (set(b.evidence_specs) <= set(a.evidence_specs) and set(b.homes) <= set(a.homes)):
        return False
    if not set(a.frozen) <= set(b.frozen):
        return False
    old_obligations = {o.id: o for o in a.obligations}
    new_obligations = {o.id: o for o in b.obligations}
    if set(old_obligations) != set(new_obligations):
        return False  # adding or removing an obligation is R2
    for oid, ob in old_obligations.items():
        nb = new_obligations[oid]
        if (nb.statement, nb.verifier) != (ob.statement, ob.verifier) or not set(ob.secondary) <= set(nb.secondary):
            return False
    if not (set(a.slots) <= set(b.slots) and set(a.triggers) <= set(b.triggers)):
        return False
    return (a.artifacts, a.evidence) == (b.artifacts, b.evidence)


def work_key(item: Item, prose: bytes) -> str:
    """The key of an item's work: its prose and fixed fields (§13.4, §10.4; SD-52).

    The fixed fields are those control tightening keeps unchanged: everything but the tightenable fields
    (write scope, dependency allowance, evidence specifications, homes, frozen interface, secondary checks,
    slots, triggers, budget, the ``scientific`` flag)."""

    contract = item.contract
    fixed = {
        "id": item.id, "kind": item.kind, "authority": item.authority, "specialist": item.specialist,
        "objective": item.objective.name, "governing": [list(g) for g in item.governing],
        "acceptance_criteria": [list(c) for c in item.acceptance_criteria], "affected": list(item.affected),
        "gates": list(item.gates), "depends_on": list(item.depends_on),
        "obligations": None if contract is None else [
            [o.id, o.statement.name, repr(o.verifier)] for o in contract.obligations],
        "artifacts": None if contract is None else list(contract.artifacts),
        "evidence": None if contract is None else list(contract.evidence),
    }
    return "sha256:" + hashlib.sha256(prose + b"\x00" + jcs(fixed)).hexdigest()


# -- partition lint (§13.7) --------------------------------------------------------------------------


def partition_violations(obligations: set[str], write_scope: list[Atom], parts: list[tuple[set[str], list[Atom]]],
                         order: set[tuple[int, int]], view: TreeView, undischarged: set[str] | None = None) -> list[str]:
    """Parts' obligation sets partition the item's (undischarged ones for a re-partition) exactly; their
    write scopes are pairwise disjoint subsets of the item's; their order is acyclic."""

    problems = []
    wanted = obligations if undischarged is None else undischarged
    shares = [set(p[0]) for p in parts]
    if set().union(*shares) != wanted or sum(len(s) for s in shares) != len(wanted):
        problems.append("the parts' obligation sets do not partition the item's obligations")
    for index, (_, scope) in enumerate(parts):
        if not contained(view, scope, write_scope):
            problems.append(f"part {index}'s write scope is not within the item's")
        for other in range(index + 1, len(parts)):
            if any(a[0] == "span" and intersects(view, parts[other][1], a[1], a[2], a[3]) for a in scope) or any(
                    a[0] != "span" and any(_within(view, b, a) or _within(view, a, b) for b in parts[other][1])
                    for a in scope):
                problems.append(f"parts {index} and {other} share write scope")
    graph = {i: {b for a, b in order if a == i} for i in range(len(parts))}
    if any(not (0 <= a < len(parts) and 0 <= b < len(parts)) for a, b in order) or _cyclic(graph):
        problems.append("the parts' order is not acyclic")
    return problems


def _cyclic(graph: dict[Any, set[Any]]) -> bool:
    state: dict[Any, int] = {}

    def visit(node: Any) -> bool:
        if state.get(node) == 1:
            return True
        if state.get(node) == 2:
            return False
        state[node] = 1
        if any(visit(n) for n in graph.get(node, ())):
            return True
        state[node] = 2
        return False

    return any(visit(node) for node in list(graph))


# -- slots and coverage (§13.3, §13.5) ---------------------------------------------------------------


def required_slots(item: Item) -> frozenset[str]:
    """Slots an item's kind, authority domain, specialist and ``scientific`` flag trigger (§13.5; reading E22)."""

    contract = item.contract
    scientific = contract is not None and contract.scientific == "APPLIES"
    slots = {"claims", "unverified_assumptions"}
    if item.kind in IMPLEMENTER:
        slots.add("deviations")
    if scientific or item.kind == "INVESTIGATE":
        slots.add("findings")
    if scientific:
        slots |= {"null_envelope", "variant_search", "tension_search", "choices", "retention", "delegate_returns"}
    if item.kind == "AUTHOR":
        slots.add("o1_content")  # §13.3: every AUTHOR item; NONE with a reason where it is not scientific software
    if item.kind == "AUTHOR" and item.authority in ("D1", "D2"):
        slots.add("revision_assessments")
    if item.kind == "INVESTIGATE" and item.specialist == "MAINTENANCE_AUDIT":
        slots.add("audit_conclusion")
    return frozenset(slots)


def _evidence_obligation(verifier: Any) -> bool:
    return isinstance(verifier, EvidenceVerifier) or (
        isinstance(verifier, Check) and verifier.template == "OBLIGATION.required_evidence")


class PlanFacts:
    """Plans, items, lint and amendment classes in one state."""

    def __init__(self, state: Any) -> None:
        self.s = state
        self.view: TreeView = state.view

    @cached_property
    def policy(self) -> Policy:
        return self.s.policy

    @cached_property
    def plans(self) -> dict[str, Plan]:
        return plans(self.view)

    @cached_property
    def items(self) -> dict[str, tuple[str, ItemPart]]:
        """Item part unit -> (plan subject, part)."""

        return {unit: (subject, part) for subject, plan in self.plans.items() for unit, part in plan.items.items()}

    def prose(self, part: ItemPart, view: TreeView | None = None) -> bytes:
        return part.prose((view or self.view).tree[part.path].data)

    # -- lint -----------------------------------------------------------------------------------

    @cached_property
    def lint(self) -> dict[str, tuple[LintFinding, ...]]:
        """Plan subject -> every lint and plan-invariant finding of its current content."""

        return {subject: tuple(sorted(self._lint_plan(subject, plan))) for subject, plan in self.plans.items()}

    def item_lint(self, unit: str) -> tuple[LintFinding, ...]:
        subject, _ = self.items[unit]
        return tuple(f for f in self.lint[subject] if f.item in (unit, None))

    def _lint_plan(self, subject: str, plan: Plan) -> list[LintFinding]:
        out: list[LintFinding] = []
        if plan.objective is None:
            out.append(LintFinding("OBJECTIVE", None, "the plan has no single part headed Objective"))
        parsed = {unit: part.parsed for unit, part in plan.items.items()}
        ids: dict[str, str] = {}
        for unit, item in parsed.items():
            if isinstance(item, ItemFailure):
                out.append(LintFinding("PARSE", unit, f"{item.reason}: {item.detail}"))
                continue
            if item.id in ids:
                out.append(LintFinding("TOPOLOGY", unit, f"item id {item.id} repeats {ids[item.id]}"))
            ids.setdefault(item.id, unit)
        by_id = {item.id: (unit, item) for unit, item in parsed.items() if isinstance(item, Item)}
        graph = {item.id: set(item.depends_on) for _, item in by_id.values()}
        for unit, item in by_id.values():
            for dep in item.depends_on:
                if dep not in by_id:
                    out.append(LintFinding("TOPOLOGY", unit, f"depends on unknown item {dep}"))
                elif "INVESTIGATE" not in (item.kind, by_id[dep][1].kind) and _layer(by_id[dep][1]) > _layer(item):
                    out.append(LintFinding("TOPOLOGY", unit, f"depends on {dep}, a lower layer"))
        if _cyclic(graph):
            out.append(LintFinding("TOPOLOGY", None, "item dependencies are cyclic"))
        for unit, item in by_id.values():
            out.extend(self._lint_item(plan, unit, item))
        return out

    def _lint_item(self, plan: Plan, unit: str, item: Item) -> list[LintFinding]:
        out: list[LintFinding] = []

        def err(code: str, detail: str) -> None:
            out.append(LintFinding(code, unit, detail))

        structure = self.view.structure
        for ref in item.refs:
            found = len(plan.resolve_ref(unit, ref))
            if found != 1:
                err("REF", f"#{ref.name} resolves to {found} spans in the item and the Objective, not one")
        for governing, _ in item.governing:
            if governing not in structure.units:
                err("UNRESOLVED", f"governing unit {governing} is not in Σ")
        affected, problems = resolve(self.view, item.affected)
        for problem in problems:
            err("UNRESOLVED", f"affected: {problem}")
        specs = {u for u in structure.units if structure.kind(u) == "EVIDENCE_SPEC"}
        for criterion, evidence in item.acceptance_criteria:
            if evidence != REVIEW and evidence not in specs:
                err("UNRESOLVED", f"acceptance criterion {criterion} names no evidence specification ({evidence})")
        contract = item.contract
        if contract is None:
            return out  # an item without a contract owes CONTRACT (§10.2); there is nothing more to lint
        scope, problems = resolve(self.view, contract.write_scope)
        for problem in problems:
            err("UNRESOLVED", f"write scope: {problem}")
        if not contained(self.view, scope, affected):
            err("SCOPE", "the write scope is not within the item's affected units")
        touched = units_in(self.view, scope)
        protected = self.protected()
        if any(intersects(self.view, protected, a[1], a[2], a[3]) if a[0] == "span" else
               any(_within(self.view, p, a) or _within(self.view, a, p) for p in protected) for a in scope):
            err("SCOPE", "the write scope holds a protected surface")
        kinds = {u: structure.kind(u) for u in touched}
        if any(k == "PLAN" for k in kinds.values()):
            err("SCOPE", "the write scope holds a plan unit")
        for spec in sorted(u for u, k in kinds.items() if k == "EVIDENCE_SPEC" and u not in contract.evidence_specs):
            err("SCOPE", f"the write scope holds evidence specification {spec}, not named in evidence_specs")
        for spec in contract.evidence_specs:
            if spec not in specs:
                err("UNRESOLVED", f"evidence_specs names {spec}, not an evidence specification")
        # The domain rule (§13.2): D1-D3 content changes only through an AUTHOR item of that one domain.
        if item.kind in NOT_AUTHORITY:
            for u in sorted(u for u, k in kinds.items() if k in ("D1", "D2", "D3")):
                err("DOMAIN", f"an {item.kind} write scope holds {kinds[u]} unit {u}")
        elif item.kind == "AUTHOR":
            allowed = {item.authority, "MANIFEST", "EVIDENCE_RECORD"}
            for u in sorted(touched):
                if kinds[u] not in allowed and u not in contract.evidence_specs:
                    err("DOMAIN", f"an AUTHOR {item.authority} write scope holds {kinds[u]} unit {u}")
        domains = {item.authority} if item.kind == "AUTHOR" else {k for k in kinds.values() if k in ("D1", "D2", "D3", "D4")}
        for domain in sorted(d for d in domains if d):
            for gate in self.policy.get(domain, "gates"):
                if gate not in item.gates:
                    err("GATES", f"policy requires gate {gate} for {domain}")
        for ob in contract.obligations:
            verifier = ob.verifier
            if isinstance(verifier, Check):
                for problem in check_problems(verifier.template, dict(verifier.params)):
                    err("VERIFIER", f"obligation {ob.id}: {problem}")
                spec = dict(verifier.params).get("spec")
                if verifier.template == "OBLIGATION.required_evidence" and spec is not None and spec not in specs:
                    err("VERIFIER", f"obligation {ob.id} names {spec}, not an evidence specification")
            elif isinstance(verifier, EvidenceVerifier) and verifier.spec not in specs:
                err("VERIFIER", f"obligation {ob.id} names {verifier.spec}, not an evidence specification")
            for check in ob.secondary:
                for problem in check_problems(check.template, dict(check.params)):
                    err("VERIFIER", f"obligation {ob.id} secondary: {problem}")
        for spec in contract.evidence:
            if spec not in specs:
                err("UNRESOLVED", f"expectations.evidence names {spec}, not an evidence specification")
        missing = required_slots(item) - set(contract.slots)
        if missing:
            err("SLOTS", f"required slots missing: {sorted(missing)}")
        out.extend(LintFinding("COVERAGE", unit, d) for d in self._coverage(item, kinds))
        if contract.budget > BUDGET_CAP:
            err("BUDGET", f"budget {contract.budget} exceeds the system cap {BUDGET_CAP}")
        return out

    def protected(self) -> list[Atom]:
        """Protected surfaces in the tree: the system's (the policy unit and file, §25.3) and the policy's own."""

        entries = list(self.policy.flow("protected_surfaces"))
        if "ssds.policy" in self.view.structure.units:
            entries.append("ssds.policy")
        atoms, _ = resolve(self.view, entries)
        policy_path = getattr(self.s.h, "policy_path", None)
        if policy_path:
            atoms.append(("file", policy_path))
        return atoms

    def _coverage(self, item: Item, kinds: dict[str, str | None]) -> list[str]:
        """Minimum verifier coverage per item kind (§13.3); the ACCEPT obligation of an AUTHOR item is
        derived for its subject (§10.2), not a contract obligation (reading E22)."""

        contract = item.contract
        assert contract is not None
        out = []
        verifiers = [o.verifier for o in contract.obligations]
        reviews = sum(1 for v in verifiers if v == REVIEW)
        evidence = sum(1 for v in verifiers if _evidence_obligation(v))
        if item.kind in ("IMPLEMENT", "REPAIR") and "D4" in kinds.values():
            if not evidence:
                out.append(f"an {item.kind} item changing D4 units needs an EVIDENCE obligation")
            if not reviews:
                out.append(f"an {item.kind} item changing D4 units needs a REVIEW obligation")
        if {"D4", "EVIDENCE_SPEC"} & set(kinds.values()):
            for ob in contract.obligations:
                families = {c.template.split(".")[0] for c in ob.secondary}
                if not {"TEST_INTEGRITY", "BOUNDARY"} <= families:
                    out.append(f"obligation {ob.id} needs TEST_INTEGRITY and BOUNDARY secondary checks")
        if item.kind == "REPAIR" and not (evidence or reviews):
            out.append("a REPAIR item needs a regression EVIDENCE obligation or a REVIEW stating why none exists")
        if item.kind in ("MIGRATE", "AUTHOR", "INVESTIGATE", "DOCUMENT") and not reviews:
            out.append(f"an {item.kind} item needs a REVIEW obligation")
        return out

    # -- control tightening against an accepted revision -------------------------------------------

    def item_at(self, unit: str, rev: str) -> tuple[TreeView, ItemPart] | None:
        """The item part at revision ``rev``, from the latest admitted view that has it."""

        for k in range(self.s.n, -1, -1):
            view = self.s.h.view(k)
            if unit in view.structure.units and view.rev(unit) == rev:
                for plan in plans(view).values():
                    if unit in plan.items:
                        return view, plan.items[unit]
                return None
        return None

    def tightens_to_current(self, unit: str, accepted_rev: str) -> bool:
        """``accepted_rev ⊑ cur``: the plan acceptance's conclusion still applies to the current revision."""

        if unit not in self.items:
            return False
        if self.view.rev(unit) == accepted_rev:
            return True
        found = self.item_at(unit, accepted_rev)
        if found is None:
            return False
        old_view, old_part = found
        _, new_part = self.items[unit]
        if not isinstance(old_part.parsed, Item) or not isinstance(new_part.parsed, Item):
            return False
        return tightens(old_part.parsed, self.prose(old_part, old_view), new_part.parsed, self.prose(new_part), self.view)

    def amendment_class(self, unit: str, accepted_rev: str) -> str:
        """``R1`` (control tightening) or ``R2`` against the accepted revision (§11.4, §13.4)."""

        return "R1" if self.tightens_to_current(unit, accepted_rev) else "R2"


def _layer(item: Item) -> int:
    if item.kind == "AUTHOR":
        return _LAYER.get(item.authority or "", 4)
    return 4  # IMPLEMENT, REPAIR, MIGRATE, DOCUMENT; INVESTIGATE is layer-free and never compared
