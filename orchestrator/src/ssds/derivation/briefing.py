"""What a brief projects that derivation owns (Manual §16.3-§16.8; Phase E step 7 review repairs).

A renderer formats; it decides nothing. The facts a brief carries are derived here, each from its one owner: the
work an obligation is about (its domain, item, subjects and whether it is authority or scientific work), the
objections carried to a judge by the judgment owner's reach (§5.10 (c), §16.5, SD-30 to SD-34), the slots the
answer owes (the item's, or the system contract's, §13.5-§13.6), the outcomes a decision may take (§15.5), the
required evidence of a gate (§16.6), and which obligations R3 owns (§12.4, §16.8).
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Any

from ssds.content import Item, ItemPart

from .conformance import system_slots
from .items import IMPLEMENTER_KINDS, ItemObligation
from .plans import resolve, units_in, work_key
from .reports import NO_REPORT_OUTCOMES, Reports

ROUTE_OUTCOMES = ("AMEND", "ESCALATE", "PARTITION")  # §15.5: an item route's decision; DECLINE for a kept fence
TASK_OUTCOMES = ("COMPLETE", "PARTIAL", "BLOCKED", "INFEASIBLE")
AUTHORITY = ("D1", "D2", "D3")


@dataclass(frozen=True)
class Work:
    """The work an obligation is about."""

    domain: str | None
    item: Item | None  # the item revision the work is bound to
    part: ItemPart | None
    holder: ItemObligation | None  # the derived item obligation, when one is
    plan: str | None
    subjects: tuple[str, ...]  # every subject the work touches: the subject asked, the plan, the write scope's
    written: frozenset[str]  # the units its write scope holds at the current head
    authority: bool  # an authority review or authoring of D1-D3
    scientific: bool


class Briefing:
    def __init__(self, workflow: Any) -> None:
        self.w = workflow
        self.s = workflow.s
        self.d = workflow.d

    # -- the work ------------------------------------------------------------------------------------------

    def work(self, o: Any) -> Work:
        w, s = self.w, self.s
        structure = s.view.structure
        holder = w.item_of(o)
        item, part, plan = None, None, o.plan
        if holder is not None:
            item, part = holder.item, holder.part
        elif o.kind == "REVIEW" and "transformation" in o.target:
            result = w.submitting_result(o.target["transformation"])
            binding = (s.record(result).get("binding") or {}) if result else {}
            named = binding.get("item")
            found = s.plans.item_at(named["unit"], named["rev"]) if isinstance(named, dict) else None
            if found is not None and isinstance(found[1].parsed, Item):
                item, part = found[1].parsed, found[1]
                plan = structure.subj(named["unit"]) if named["unit"] in structure.units else plan
            holder = w.items.of(binding.get("obligation", "")) if binding.get("obligation") else None
        elif o.kind == "REVIEW" and o.target.get("integrated") == "ITEM":
            holder = next((i for i in w.items.all if i.key == o.target.get("of")), None)
            if holder is not None:
                item, part, plan = holder.item, holder.part, holder.plan
        subjects: set[str] = set()
        written: frozenset[str] = frozenset()
        asked = w.subject_of(o)
        if asked is not None:
            subjects.add(asked)
        if plan is not None:
            subjects.add(plan)
        if item is not None and item.contract is not None:
            entries = holder.share[3] if holder is not None and holder.share is not None else item.contract.write_scope
            atoms, _ = resolve(s.view, entries)
            written = frozenset(units_in(s.view, atoms))
            subjects |= {structure.subj(u) for u in written if structure.subj(u)}
        if item is not None:
            domain = item.authority or ("D4" if item.kind in IMPLEMENTER_KINDS else None)
        else:
            domain = w.domain_of(o)
        authority = (item is not None and item.kind == "AUTHOR" and domain in AUTHORITY) or \
            (o.kind in ("ACCEPT", "REVIEW_REVISION") and domain in AUTHORITY)
        scientific = item is not None and item.contract is not None and item.contract.scientific == "APPLIES"
        return Work(domain, item, part, holder, plan, tuple(sorted(subjects)), written, authority, scientific)

    # -- carried objections (§16.5) ------------------------------------------------------------------------

    def carried(self, o: Any) -> list[dict[str, Any]]:
        """Every standing adverse judgment whose reach includes the target asked; standing objections on a
        subject the asked one's lineage links to, as history; for a re-review, the earlier review findings on
        the same plan subject that no later independent, acting, unvetoed review records ``RESOLVED``; for a
        plan acceptance, the standing rejections naming any item of the plan at any revision, or an item
        elsewhere with the same prose and fixed fields (SD-30 to SD-34)."""

        from . import queries
        from .workflow import ANSWER_KIND

        w, s, j = self.w, self.s, self.d.j
        out: dict[str, dict[str, Any]] = {}

        def add(rid: str, why: str) -> None:
            if rid not in out:
                record = s.record(rid)
                out[rid] = {"record": rid, "kind": record["kind"], "actor": record["actor"], "outcome": record["outcome"],
                            "position": s.position_of(rid), "why": why}

        kind = ANSWER_KIND.get(o.kind)
        standing = w.standing_adverse()
        for rid in standing:
            if kind is not None and j.reaches_target(rid, kind, o.target):
                add(rid, "its reach includes the target asked")
        asked = w.subject_of(o)
        if asked is not None and asked in s.view.structure.units:
            predecessors = set(queries.lineage(w, asked)) - {asked}
            for rid in standing:
                target = s.record(rid)["target"]
                about = target.get("subject") if isinstance(target, dict) else None
                about = about.get("subject") if isinstance(about, dict) else about
                if about in predecessors:
                    add(rid, "history: a predecessor the asked subject's lineage links to")
        work = self.work(o)
        if o.kind == "REVIEW" and work.plan is not None:
            for rid, findings in self._unresolved_reviews(work.plan, o):
                add(rid, "a re-review: earlier findings on this plan, not recorded RESOLVED")
                out[rid]["findings"] = findings
        if o.kind == "PLAN_ACCEPT":
            for rid in self._plan_rejections(o.target.get("plan") or o.plan, standing):
                add(rid, "a standing rejection naming an item of this plan, or the same work elsewhere")
        return sorted(out.values(), key=lambda e: (e["position"], e["record"]))

    def _unresolved_reviews(self, plan: str, asked: Any) -> list[tuple[str, Any]]:
        w, s = self.w, self.s
        out = []
        holders = [h for h in w.items.holders if h.plan == plan]
        seen: set[str] = set()
        for holder in holders:
            for e in holder.enactments:
                if not e.transformation or e.transformation == asked.target.get("transformation"):
                    continue
                for rid in holder.reviews(e.transformation):
                    if rid in seen or s.record(rid)["outcome"] != "NO_PASS":
                        continue
                    seen.add(rid)
                    if not self._resolved(rid):
                        out.append((rid, w.items.findings_of(rid)))
        return out

    def _resolved(self, review: str) -> bool:
        """A later independent, acting, unvetoed review records the earlier review's findings ``RESOLVED`` (a
        ``findings`` entry ``{"of": <review>, "status": "RESOLVED"}``, §13.5; reading E38)."""

        s, j = self.s, self.d.j
        position = s.position_of(review)
        for later in s.of_kind("REVIEW"):
            record = s.record(later)
            x = record["target"].get("transformation") if isinstance(record["target"], dict) else None
            acting = s.acts(later) or (x is not None and record["frame"] == {"transformation": x})  # in its own frame
            if s.position_of(later) <= position or not acting or j.nonind(later) or j.vetoed(later):
                continue
            for finding in self.w.items.findings_of(later) or []:
                if isinstance(finding, dict) and finding.get("of") == review and finding.get("status") == "RESOLVED":
                    return True
        return False

    def _plan_rejections(self, plan: str | None, standing: list[str]) -> list[str]:
        if plan is None:
            return []
        s = self.s
        current = s.plans.plans.get(plan)
        keys = set()
        for unit, part in (current.items.items() if current is not None else ()):
            if isinstance(part.parsed, Item):
                keys.add(work_key(part.parsed, s.plans.prose(part)))
        out = []
        for rid in standing:
            record = s.record(rid)
            if record["kind"] != "PLAN_ACCEPTANCE":
                continue
            then = s.h.view(s.position_of(rid))
            for named in record["fields"].get("items", []):
                unit = named["unit"]
                member = any(v.structure.subj(unit) == plan for v in (then, s.view) if unit in v.structure.units)
                found = s.plans.item_at(unit, named["rev"])
                same = found is not None and isinstance(found[1].parsed, Item) and \
                    work_key(found[1].parsed, s.plans.prose(found[1], found[0])) in keys
                if member or same:
                    out.append(rid)
                    break
        return out

    # -- slots, outcomes, evidence ---------------------------------------------------------------------------

    def owed_slots(self, o: Any) -> list[str]:
        holder = self.w.item_of(o)
        return list(holder.required_slots) if holder is not None else sorted(system_slots(self.w, o))

    @cached_property
    def _reports(self) -> Reports:
        return Reports(self.w)

    def decision_outcomes(self, o: Any) -> list[str]:
        """The outcomes a decision may take (§15.5), from the owner of each."""

        target = o.target
        if o.kind == "CONTRACT":
            return list(TASK_OUTCOMES)  # the principal authors the contract by a plan change
        if "report" in target and target["report"] in self.s.records:
            return sorted(self._reports.report_outcomes(target["report"]))
        if "recurrence" in target or "refused" in target:
            return sorted(NO_REPORT_OUTCOMES)
        if target.get("condition") == "kept-fence":
            return sorted({*ROUTE_OUTCOMES, "DECLINE"})
        return sorted(ROUTE_OUTCOMES)

    def required_evidence(self, subject: str) -> list[dict[str, Any]]:
        """Each evidence obligation the subject's domain requires, holding through its current passing
        admissible assessments, or why not: ``UNAVAILABLE``, stale, disputed or failing (§16.6)."""

        from . import queries

        structure = self.s.view.structure
        if subject not in structure.units:
            return []
        claims = [u for u in structure.units if structure.subj(u) == subject]
        entries = [e for claim in claims for e in queries.evidence(self.w, claim) if "assessment" in e]
        out = []
        for obligation in self.s.policy.get(structure.domain(subject), "evidence"):
            mine = sorted({e["assessment"]: e for e in entries if e["obligation"] == obligation}.values(),
                          key=lambda e: e["assessment"])
            passing = [e["assessment"] for e in mine if e["outcome"] == "PASS" and e["status"] == "current"]
            if any(e["status"] == "disputed" for e in mine):
                status = "disputed"
            elif any(e["outcome"] == "FAIL" and e["status"] == "current" for e in mine):
                status = "failing"
            elif passing:
                status = "holding"
            elif mine:
                status = "stale"
            else:
                status = "UNAVAILABLE"
            out.append({"obligation": obligation, "holds": status == "holding", "status": status,
                        "via": passing if status == "holding" else [],
                        "records": [{"assessment": e["assessment"], "outcome": e["outcome"], "status": e["status"],
                                     **({"failing_outputs": e["failing_outputs"]} if "failing_outputs" in e else {})}
                                    for e in mine]})
        return out

    def unfloored_failures(self) -> list[tuple[str, str]]:
        """(obligation, assessment) for every failure that counts but has raised no floor event (§16.8 digest)."""

        a, d = self.d.a, self.d
        floors = {h.target.get("floor") for h in self.w.of_kind("HUMAN_ATTENTION")}
        return [(obligation, rid) for obligation, records in sorted(a.by_obligation.items()) for rid in records
                if a.failing(rid) and a.starts(rid) and not a.stale(rid, d.base, self.w._value)
                and f"disagreement:{rid}" not in floors]

    def r3(self, o: Any) -> bool:
        """Whether a human decides it (§12.4 R3): a gate, human attention, an obligation held by the human, an
        acceptance of D1 or D2 authority, or a judgment only humans are eligible to give."""

        from .workflow import HUMAN, JUDGED

        if o.kind in ("GATE", "HUMAN_ATTENTION") or o.holder == HUMAN:
            return True
        if o.kind == "ACCEPT" and self.w.domain_of(o) in ("D1", "D2"):
            return True
        if o.kind in JUDGED:
            judges = self.w.eligible_judges(o)
            return bool(judges) and all(j.startswith("human:") for j in judges)
        return False


__all__ = ["Briefing", "Work"]
