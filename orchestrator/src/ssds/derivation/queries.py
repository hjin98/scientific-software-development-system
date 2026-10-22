"""The query classes of the agent and human interface, over the derived strata (Manual §16.2; catalogue §26.1).

Every function is a pure function of one derived state (a ``Workflow`` over its
``Support``) and its arguments; the Interface adds the qualified head, renders and
transports the answer. Each item carries one epistemic label and an acceptance
status (§16.2). Answers are deterministic for an identical state, query and
policy; ``search`` returns ``CANDIDATE`` items only.
"""

from __future__ import annotations

from typing import Any

from ssds.content import ABSENT, Tree, TreeView, named_spans, write_set

from .state import F, P, T, triple_key

GOVERNING, IMPLIED, ADJACENT, EVIDENTIAL, HISTORICAL, CANDIDATE = (
    "GOVERNING", "IMPLIED", "ADJACENT", "EVIDENTIAL", "HISTORICAL", "CANDIDATE")
CLASSES = ("DEF", "WARRANT", "GOVERNING", "EXEC", "STRUCT")
_VALUE = {F: "F", P: "P", T: "T"}


def status(w: Any, unit: str) -> str:
    """A unit's acceptance status (§16.2)."""

    s, d = w.s, w.d
    if unit not in s.view.structure.units:
        return "unclassified"
    subject = s.view.structure.subj(unit)
    if subject is None or s.view.structure.kind(subject) == "UNCLASSIFIED":
        return "unclassified"
    if subject in s.s0.affected_subjects:
        return "quarantined"
    if not s.s0.well_formed(subject):
        return "ill-formed"
    triple = s.subject_triple(subject)
    status1 = s.status1(triple_key(*triple))
    if status1 in ("REVOKED", "BLOCKED"):
        return "challenged"
    acceptances = d.acceptances(subject)
    if acceptances and not any(s.cont(r) for r in acceptances):
        return "loss-withheld"
    valid = d.valid(subject)
    if valid == T:
        return "valid"
    if valid == P:
        return "provisional"
    if acceptances:
        return "stale"
    return "unclassified" if s.mode(subject) == "UNGOVERNED" else "stale"


def _relations(w: Any, classes: frozenset[str]) -> list[Any]:
    from .vocabulary import VOCABULARY

    return [r for r in w.s.s0.relations if VOCABULARY.get(r.type) and VOCABULARY[r.type].completeness in classes]


def _item(w: Any, unit: str, label: str, **extra: Any) -> dict[str, Any]:
    view = w.s.view
    rev = view.rev(unit) if unit in view.structure.units else None
    return {"unit": unit, "rev": rev, "label": label, "status": status(w, unit), **extra}


def governs(w: Any, x: str) -> list[dict[str, Any]]:
    """The governing units of ``x`` with revisions, validity and inclusion path (§16.2): the transitive targets
    of ``x``'s governing relations, each with the relation path that reaches it."""

    relations = _relations(w, frozenset({"GOVERNING"}))
    out: dict[str, list[str]] = {}
    frontier = [(x, [])]
    while frontier:
        unit, path = frontier.pop(0)
        for r in sorted(relations, key=lambda r: (r.subject, r.type, r.object)):
            if r.subject == unit and r.object not in out and r.object != x:
                out[r.object] = path + [f"{r.type} {r.object}"]
                frontier.append((r.object, out[r.object]))
    return [_item(w, unit, GOVERNING, path=path) for unit, path in sorted(out.items())]


def _complete(w: Any, scope: frozenset[str], cls: str) -> bool:
    for rid in w.s.of_kind("COMPLETENESS"):
        record = w.s.record(rid)
        target = record["target"]
        if record["outcome"] == "COMPLETE" and frozenset(target["scope"]) == scope and cls in target["classes"] \
                and w.d.current(rid) > F:
            return True
    return False


def depends(w: Any, x: str, cls: str = "WARRANT", direction: str = "prerequisites") -> dict[str, Any]:
    """Prerequisites or dependents of ``x`` per completeness class, with the widening state: ``EXACT``,
    a widened scope, or ``UNBOUNDED`` (§16.2, §4.5-§4.6)."""

    if cls not in CLASSES or direction not in ("prerequisites", "dependents"):
        raise ValueError(f"depends takes a class in {CLASSES} and prerequisites or dependents")
    classes = frozenset({cls})
    relations = _relations(w, classes)
    label = ADJACENT if cls == "STRUCT" else IMPLIED
    if direction == "dependents":
        reached, frontier = set(), [x]
        while frontier:
            unit = frontier.pop()
            for r in relations:
                if r.object == unit and r.subject not in reached and r.subject != x:
                    reached.add(r.subject)
                    frontier.append(r.subject)
        return {"widening": "EXACT", "items": [_item(w, u, label) for u in sorted(reached)]}
    exact, frontier = set(), [x]
    while frontier:
        unit = frontier.pop()
        for r in relations:
            if r.subject == unit and r.object not in exact and r.object != x:
                exact.add(r.object)
                frontier.append(r.object)
    reached, unbounded = w.s.s0.closure([x], classes, lambda scope, c: _complete(w, scope, c))
    reached = set(reached) - {x}
    widening = "UNBOUNDED" if unbounded else ("EXACT" if reached <= exact else "WIDENED")
    return {"widening": widening, "items": [_item(w, u, label, exact=u in exact) for u in sorted(reached | exact)]}


def explain(w: Any, ref: str) -> dict[str, Any]:
    """A unit, record or obligation: kind, status, basis, why current or not (§16.2)."""

    s, d = w.s, w.d
    if ref in s.view.structure.units:
        subject = s.view.structure.subj(ref)
        out = {"unit": ref, "kind": s.view.structure.kind(ref), "subject": subject, "rev": s.cur(ref),
               "status": status(w, ref)}
        if subject is not None:
            out.update(mode=s.mode(subject), valid=_VALUE[d.valid(subject)],
                       acceptances=[{"record": r, "current": _VALUE[d.current(r)]} for r in d.acceptances(subject)],
                       status1=s.status1(triple_key(*s.subject_triple(subject))),
                       well_formed=s.s0.well_formed(subject), quarantined=subject in s.s0.affected_subjects)
        return out
    if ref in s.records:
        record = s.record(ref)
        why = []
        for name, holds in (("acts", s.acts(ref)), ("not superseded", not s.superseded(ref)), ("continuity", s.cont(ref)),
                            ("target conditions", s.tgt(ref)), ("not vetoed", not d.j.vetoed(ref)),
                            ("independent", not d.j.nonind(ref))):
            if not holds:
                why.append(f"fails: {name}")
        basis = [{"entry": e, "sat": _VALUE[d.sat(e, w._value, ref)]} for e in record["basis"]]
        return {"record": ref, "kind": record["kind"], "outcome": record["outcome"], "status1": s.status1(ref),
                "base": _VALUE[d.base(ref)], "current": _VALUE[d.current(ref)], "why": why, "basis": basis}
    for o in w.obligations:
        if o.id == ref:
            readiness = w.readiness(o)
            return {"obligation": ref, "kind": o.kind, "target": o.target, "holder": o.holder, "plan": o.plan,
                    "readiness": readiness.state, "waiting_on": list(readiness.waiting_on), "discharge": w.discharge(o),
                    "detail": o.detail}
    raise KeyError(f"{ref} is no unit, record or obligation of this state")


def evidence(w: Any, claim: str) -> list[dict[str, Any]]:
    """Evidence for a claim: realizations, assessments, disagreement state, binding health (§16.2)."""

    s, a = w.s, w.d.a
    out = []
    for obligation, records in sorted(a.by_obligation.items()):
        for rid in records:
            if claim not in a.claim_units(rid):
                continue
            stale = a.stale(rid, w.d.base, w._value)
            out.append({"assessment": rid, "obligation": obligation, "realization": a.real(rid),
                        "outcome": s.record(rid)["outcome"], "label": EVIDENTIAL,
                        "status": "stale" if stale else ("disputed" if a.failing(rid) else "current"),
                        "current": _VALUE[w.d.current(rid)]})
    return out


def blocked(w: Any, x: str) -> dict[str, Any]:
    """Why ``x`` is blocked or not current: challenges, quarantine, loss withholding or integrity (§16.2)."""

    s = w.s
    subject = s.view.structure.subj(x) if x in s.view.structure.units else None
    reasons = []
    if s.h.chain.halt is not None:
        reasons.append(f"INTEGRITY_HALT from position {s.h.chain.halt}")
    if subject is not None:
        key = triple_key(*s.subject_triple(subject))
        for c in s.targeting.get(key, []):
            record = s.record(c)
            if record["kind"] == "CHALLENGE" and s.open(c):
                reasons.append(f"open {'blocking ' if record['fields']['blocking'] else ''}challenge {c}")
        if subject in s.s0.affected_subjects:
            reasons.append("quarantined structure")
        if not s.s0.well_formed(subject):
            reasons += [f"{d.code}: {d.detail}" for d in s.s0.defects if d.unit == subject]
        for r in w.d.acceptances(subject):
            if not s.cont(r):
                reasons.append(f"acceptance {r} withheld by a loss boundary")
    return {"unit": x, "status": status(w, x), "reasons": reasons}


def stale(w: Any, x: str) -> dict[str, Any]:
    """Why ``x``'s acceptances are not current: each basis entry that no longer holds (§16.2)."""

    s, d = w.s, w.d
    subject = s.view.structure.subj(x) if x in s.view.structure.units else None
    entries = []
    for kind in ("ACCEPTANCE", "LEGACY_ACCEPTANCE"):
        for rid in s.of_kind(kind):
            if subject is None or s.record(rid)["target"].get("subject") != subject:
                continue
            for e in s.record(rid)["basis"]:
                value = d.sat(e, w._value, rid)
                if value < T:
                    entries.append({"record": rid, "entry": e, "sat": _VALUE[value]})
    return {"unit": x, "status": status(w, x), "failing_entries": entries}


def impact(w: Any, workspace: Tree) -> dict[str, Any]:
    """The derived impact set of a workspace: its effect-keyed write set against the state, and every unit
    depending on those through any relation class (§16.2, §5.8)."""

    candidate = TreeView(workspace, w.s.view.structure, w.s.h.manifest_path)
    writes = sorted(write_set(w.s.view, candidate))
    relations = _relations(w, frozenset(CLASSES))
    reached, frontier = set(), list(writes)
    while frontier:
        unit = frontier.pop()
        for r in relations:
            if r.object == unit and r.subject not in reached and r.subject not in writes:
                reached.add(r.subject)
                frontier.append(r.subject)
    return {"write_set": writes, "impacted": [_item(w, u, ADJACENT) for u in sorted(reached)]}


def locate(w: Any, locator: str) -> dict[str, Any]:
    """§1.11 resolution of a locator ``unit[@rev][#name]``: the unit's region and current revision, whether the
    named revision is current, and the named anchor or heading inside it."""

    unit, _, name = locator.partition("#")
    unit, _, rev = unit.partition("@")
    view = w.s.view
    if unit not in view.structure.units:
        return {"locator": locator, "resolved": False, "reason": f"{unit} is not a unit"}
    region = view.regions.get(unit)
    out: dict[str, Any] = {"locator": locator, "unit": unit, "rev": view.rev(unit),
                           "current": (rev == view.rev(unit)) if rev else True,
                           "region": [[sp.path, sp.start, sp.end] for sp in region] if region else None}
    if name and region:
        spans = [sp for r in region for sp in named_spans(r.path, view.tree[r.path].data, r, name)]
        out["named"] = [[sp.path, sp.start, sp.end] for sp in spans]
    out["resolved"] = region is not ABSENT and (not name or len(out.get("named", [])) == 1)
    return out


def tensions(w: Any, authority: str) -> list[dict[str, Any]]:
    """In-repository ``CHALLENGES`` relations and recorded challenges bound to the authority's identity, its
    earlier revisions and predecessors (§16.2); native homes are listed as searchable elsewhere."""

    s = w.s
    names = {authority}
    unit = s.view.structure.units.get(authority)
    if unit is not None:
        names |= set(unit.renamed_from)
    out = []
    for r in s.s0.relations:
        if r.type == "CHALLENGES" and r.object in names:
            out.append({"source": "relation", "unit": r.subject, "attributes": dict(getattr(r, "attrs", {}) or {}),
                        "label": EVIDENTIAL})
    for c in s.of_kind("CHALLENGE"):
        target = s.record(c)["target"]
        bound = target.get("subject") if isinstance(target, dict) else None
        if bound in names:
            out.append({"source": "challenge", "record": c, "rev": target.get("rev"), "open": s.open(c),
                        "asserter": s.record(c)["actor"], "label": EVIDENTIAL})
    return out


def history(w: Any, x: str) -> list[dict[str, Any]]:
    """The ledger history of ``x``: each position its revision changed and each record about it (§16.2);
    offered only on explicit request or when the PEM predicate fires (``HISTORICAL``)."""

    s = w.s
    out = []
    previous = None
    for k in range(s.n + 1):
        view = s.h.view(k)
        rev = view.rev(x) if x in view.structure.units else None
        if rev != previous:
            out.append({"position": k, "rev": rev, "label": HISTORICAL})
            previous = rev
    for rid, fact in sorted(s.records.items(), key=lambda item: (item[1].position, item[0])):
        target = fact.record["target"]
        if isinstance(target, dict) and (target.get("subject") == x or x in target.get("units", [])):
            out.append({"position": fact.position, "record": rid, "kind": fact.record["kind"], "label": HISTORICAL})
    return sorted(out, key=lambda e: (e["position"], e.get("record", "")))


def search(w: Any, text: str) -> list[dict[str, Any]]:
    """A deterministic substring search over governed content; every hit is ``CANDIDATE`` (§16.2)."""

    view = w.s.view
    needle = text.encode("utf-8")
    hits = []
    for path in view.governed_paths:
        data = view.tree[path].data
        index = data.find(needle)
        if index >= 0:
            hits.append({"path": path, "offset": index, "owner": view.owner_of_line(path, index), "label": CANDIDATE})
    return hits


def changed(w: Any, since: int, units: list[str] | None = None) -> list[dict[str, Any]]:
    """Admitted changes since position ``since`` intersecting ``units`` (all units when none given) (§16.2)."""

    s = w.s
    out = []
    for k in range(max(since, 0) + 1, s.n + 1):
        before, after = s.h.view(k - 1), s.h.view(k)
        moved = sorted(u for u in after.structure.units
                       if (units is None or u in units) and (u not in before.structure.units or before.rev(u) != after.rev(u)))
        if moved:
            out.append({"position": k, "entry": s.h.chain.entries[k].digest, "units": moved})
    return out


def verify(w: Any, item_unit: str, workspace: Tree) -> dict[str, Any]:
    """Advisory pre-flight (§14.4): the pure templates of the item's contract on a workspace, labeled advisory;
    never a stand-in for the designated runner, and an agent's report of it is a finding, never evidence."""

    if item_unit not in w.s.plans.items:
        raise KeyError(f"{item_unit} is not an item of a plan in this state")
    rev = w.s.cur(item_unit)
    advisory = _Advisory(w, item_unit, rev, workspace)
    return {"advisory": True, "item": item_unit, "classes": sorted(advisory.classes), "view": advisory.view(),
            "note": "advisory pre-flight: runner checks are not executed and nothing here is evidence"}


class _Advisory:
    """Conformance of a workspace as if submitted against the item's current contract (no record, no frame)."""

    def __new__(cls, w: Any, item_unit: str, rev: str, workspace: Tree) -> Any:
        from .conformance import Conformance

        class Workspace(Conformance):
            @property
            def transformation(self) -> str | None:
                return None

            @property
            def frame(self) -> Any:
                return None

            @property
            def base_view(self) -> TreeView:
                return w.s.view

            @property
            def candidate_view(self) -> TreeView:
                return TreeView(workspace, w.s.view.structure, w.s.h.manifest_path)

            @property
            def has_candidate(self) -> bool:
                return True

            @property
            def changed_files(self) -> dict[str, tuple[bytes | None, bytes | None]]:
                base, cand = w.s.view.tree, workspace
                return {p: (base[p].data if p in base else None, cand[p].data if p in cand else None)
                        for p in sorted(set(base) | set(cand))
                        if (base[p].data if p in base else None) != (cand[p].data if p in cand else None)}

        instance = Workspace.__new__(Workspace)
        instance.w, instance.s, instance.d, instance.rid = w, w.s, w.d, ""
        instance.record = {"kind": "TASK_RESULT", "outcome": "PARTIAL", "target": {"task": "advisory"}, "frame": "ADMITTED",
                           "binding": {"item": {"unit": item_unit, "rev": rev}}, "fields": {"slots": {}}, "basis": []}
        return instance
