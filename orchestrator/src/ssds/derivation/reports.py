"""Reports, escalation floors, routing, persistence and recurrence (catalogue §15; Manual §15, A8).

Every communication from an agent that can change what happens next is a typed
report record. This module derives, from reports and floor events, the
``HUMAN_ATTENTION`` and ``COORDINATE`` obligations of the routing table (§15.3)
with the effective materiality the floors fix (§15.4), keyed on the report's
existence and identity and closed only by a resolving record in force (§15.2);
human attention for every ``ESCALATE`` decision (§15.5); and the coordination
decisions owed with no report behind them: detected recurrence (§15.7) and
refused joint-invariant or specification reviews (§10.4). Floor events latch:
once one has held, its human attention stays until an authenticated human
decides it, whatever later happens to its target (§6.8, A8). Human attention is
discharged only by an authenticated human decision (A8).
"""

from __future__ import annotations

from functools import cached_property
from typing import Any

from .conformance import DISCREPANCY, FAILING
from .library import HEURISTIC, TEMPLATES
from .state import F, MATERIALITY

REPORT_KINDS = ("FINDING", "AMENDMENT_REQUEST", "BLOCKER", "HUMAN_QUESTION", "CHALLENGE")
_RANK = {m: i for i, m in enumerate(MATERIALITY)}


def allowed_outcomes(kind: str, reasons: tuple[str, ...] = (), domain: str | None = None, floor: bool = False) -> frozenset[str]:
    """A coordination decision's allowed outcomes for a routed report (§15.5)."""

    out = {"CHALLENGE", "ESCALATE"}
    defect = {"AUTHORITY_DEFECT", "CONTRACT_DEFECT"} & set(reasons)
    if kind in ("BLOCKER", "FINDING") or (kind == "AMENDMENT_REQUEST" and not defect):
        out.add("RESOLVE_LOCAL")
    if kind in ("AMENDMENT_REQUEST", "BLOCKER") or "CONTRACT_DEFECT" in reasons:
        out.add("AMEND")
    if not floor:
        out.add("DECLINE")
    if kind == "AMENDMENT_REQUEST" and "AUTHORITY_DEFECT" in reasons and domain in ("D3", "D4"):
        out = {"CHALLENGE", "ESCALATE"}  # a challenge against the earliest affected owner is required
    return frozenset(out)


#: Outcomes of a decision owed with no report behind it: detected recurrence, a refused review (§15.5).
NO_REPORT_OUTCOMES = frozenset({"AMEND", "DECLINE", "CHALLENGE", "ESCALATE"})


class Reports:
    """The report-derived and floor obligations of one state."""

    def __init__(self, workflow: Any) -> None:
        self.w = workflow
        self.s = workflow.s
        self.d = workflow.d

    # -- reports and their materiality (§15.1, §15.4, §15.6) ---------------------------------------------

    @cached_property
    def reports(self) -> list[str]:
        return [r for r in self.s.of_kind(*REPORT_KINDS) if self.s.acts(r)]

    def report_outcomes(self, rid: str) -> frozenset[str]:
        """The outcomes a coordination decision on this report may take (§15.5): of its kind, reasons, target
        domain and floor. The one owner, for resolution and the decision brief."""

        record = self.s.record(rid)
        domain = next(iter(sorted(self._domains(rid))), None)
        return allowed_outcomes(record["kind"], tuple(record.get("reason") or ()), domain, self.materiality(rid)[1])

    def _target_units(self, rid: str, view: Any = None) -> set[str]:
        view = view if view is not None else self.s.view
        target = self.s.record(rid)["target"]
        units = set(target.get("units", [])) if isinstance(target, dict) else set()
        for key in (target.get("records", []) if isinstance(target, dict) else []) + \
                ([target["record"]] if isinstance(target, dict) and "record" in target else []):
            if key in self.s.records:
                inner = self.s.record(key)["target"]
                if isinstance(inner, dict):
                    if isinstance(inner.get("subject"), str):
                        units.add(inner["subject"])
                    elif isinstance(inner.get("subject"), dict):
                        units.add(inner["subject"]["subject"])
                    units |= set(inner.get("units", []))
        if isinstance(target, dict) and isinstance(target.get("subject"), str):
            units.add(target["subject"])
        return {u for u in units if u in view.structure.units}

    def _domains(self, rid: str) -> set[str]:
        """Its target's domains at its admission and now: a floor raised when it was raised stays raised when
        its target later leaves the structure (§15.2, A8; review 879fa490 B7)."""

        then = self.s.h.view(self.s.position_of(rid))
        return ({then.structure.kind(u) or "" for u in self._target_units(rid, then)}
                | {self.s.view.structure.kind(u) or "" for u in self._target_units(rid)})

    def _accepted_d1_d2(self, rid: str) -> bool:
        """A target unit is D1 or D2 authority accepted now, or when the report was admitted."""

        if any(self.s.view.structure.kind(u) in ("D1", "D2") and self.d.valid(u) > F for u in self._target_units(rid)):
            return True
        position = self.s.position_of(rid)
        then = self.s.h.view(position)
        earlier = [u for u in self._target_units(rid, then) if then.structure.kind(u) in ("D1", "D2")]
        if not earlier or position == self.s.n:
            return False
        support = self._support_at(position)
        return any(u in support.s.view.structure.units and support.valid(u) > F for u in earlier)

    def _support_at(self, position: int) -> Any:
        from .state import State
        from .support import Support

        cache = self.__dict__.setdefault("_supports", {})
        if position not in cache:
            cache[position] = self.d if position == self.s.n else Support(State(self.s.h, position))
        return cache[position]

    def materiality(self, rid: str) -> tuple[str, bool]:
        """(effective materiality, floor item) of a report: declared, raised by floors, never lowered (§15.4);
        a non-floor MATERIAL report reclassified ROUTINE while the reclassification is in force (§15.6)."""

        record = self.s.record(rid)
        kind, reasons = record["kind"], tuple(record.get("reason") or ())
        fields = record.get("fields") or {}
        declared = fields.get("materiality") or ("CRITICAL" if fields.get("serious") else "ROUTINE")
        level = _RANK.get(declared, 0)
        floor = False
        domains = self._domains(rid)
        accepted_d1_d2 = bool(domains & {"D1", "D2"}) and (kind == "CHALLENGE" or "TENSION" in reasons) \
            and self._accepted_d1_d2(rid)
        critical = (
            (kind == "CHALLENGE" and fields.get("serious"))
            or kind == "HUMAN_QUESTION"
            or (accepted_d1_d2 and (kind == "CHALLENGE" or "TENSION" in reasons))
            or (kind == "AMENDMENT_REQUEST" and "AUTHORITY_DEFECT" in reasons and domains & {"D1", "D2"})
        )
        if critical:
            level, floor = _RANK["CRITICAL"], True
        elif domains & {"D1", "D2"} and level < _RANK["MATERIAL"]:
            level, floor = _RANK["MATERIAL"], True
        elif domains & {"D1", "D2"}:
            floor = True
        for entry in self.s.policy.flow("floors"):
            if entry["kind"] == kind and (not entry.get("reason") or entry["reason"] in reasons) and \
                    (not entry.get("domain") or entry["domain"] in domains) and _RANK[entry["materiality"]] >= level:
                level, floor = _RANK[entry["materiality"]], True  # at or above the declared level: a floor (B6)
        if not floor and level == _RANK["MATERIAL"] and self._reclassified(rid):
            level = _RANK["ROUTINE"]
        return MATERIALITY[level], floor

    def _reclassified(self, rid: str) -> bool:
        return any(self.s.record(m)["target"].get("record") == rid and self._in_force(m)
                   for m in self.s.of_kind("MATERIALITY_RECLASSIFICATION"))

    def _in_force(self, rid: str) -> bool:
        """A resolving record stays in force: acting, not superseded, not revoked or blocked, not withheld (§15.2)."""

        return self.s.acts(rid) and not self.s.superseded(rid) and self.s.status1(rid) not in ("REVOKED", "BLOCKED") \
            and self.s.cont(rid)

    def withdrawn(self, rid: str) -> bool:
        """Withdrawn or superseded by its raiser (§15.2)."""

        raiser = self.s.record(rid)["actor"]
        if any(self.s.record(x)["actor"] == raiser for x in self.s.supersessions.get(rid, [])):
            return True
        return any(self.s.record(w)["target"].get("record") == rid and self.s.record(w)["actor"] == raiser and self._in_force(w)
                   for w in self.s.of_kind("WITHDRAWAL"))

    def changed_since_raised(self, rid: str) -> bool:
        """Its target moved since it was raised: annotated so the decider can answer ``MOOT`` (§15.2)."""

        then = self.s.h.view(self.s.position_of(rid))
        return any(u not in then.structure.units or then.rev(u) != self.s.cur(u) for u in self._target_units(rid))

    # -- where a report's decision goes ----------------------------------------------------------------

    def plan_of(self, rid: str) -> str | None:
        """The plan the report bears on: the plan of the item obligation its raising task is bound to."""

        task = (self.s.record(rid).get("binding") or {}).get("task")
        obligation = (self.s.record(rid).get("binding") or {}).get("obligation")
        for item in self.w.items.all:
            ids = {item.obligation.id} | {p.obligation.id for p in item.parts}
            if obligation in ids or any(e.task == task for e in item.enactments):
                return item.plan
        return None

    def open_item_units(self) -> set[str]:
        out: set[str] = set()
        for item in self.w.items.all:
            if item.discharge() == "OPEN" and item.item.contract is not None:
                from .plans import resolve, units_in

                atoms, _ = resolve(self.s.view, item.item.contract.write_scope)
                out |= set(units_in(self.s.view, atoms))
        return out

    def principal(self, plan: str | None) -> tuple[str, str | None]:
        """(holder, plan) of a decision owed on ``plan``, or outside every plan the standing plan's principal,
        or with none the human (§12.5)."""

        from .workflow import HUMAN, PRINCIPAL

        if plan is not None:
            return PRINCIPAL, plan
        standing = self.s.policy.flow("standing_plan")
        return (PRINCIPAL, standing) if standing else (HUMAN, None)

    # -- the obligations ------------------------------------------------------------------------------

    def _resolved_by_decision(self, rid: str, allowed: frozenset[str], holder: str | None = None) -> bool:
        """A coordination decision in force names it with an allowed outcome; a decision owed to the human is
        resolved only by an authenticated human's (§12.5; review 879fa490 N2)."""

        from .workflow import HUMAN

        return any(rid in (self.s.record(c)["target"] or {}).get("records", []) and self._in_force(c)
                   and self.s.record(c)["outcome"] in allowed
                   and (holder != HUMAN or self.s.record(c)["actor_class"] == "HUMAN")
                   for c in self.s.of_kind("COORDINATION_DECISION"))

    def _resolved_by_human(self, obligation_id: str) -> bool:
        return any(self.s.record(h)["target"].get("obligation") == obligation_id and self.s.record(h)["actor_class"] == "HUMAN"
                   and self._in_force(h) for h in self.s.of_kind("HUMAN_DECISION"))

    def _attention(self, target: dict[str, Any], materiality: str, plan: str | None = None, detail: str = "") -> Any:
        from .workflow import HUMAN, make

        return make("HUMAN_ATTENTION", target, {"materiality": materiality}, holder=HUMAN, plan=plan, detail=detail)

    @cached_property
    def obligations(self) -> list[Any]:
        from .workflow import make

        out: list[Any] = []
        open_units = None
        for rid in self.reports:
            record = self.s.record(rid)
            kind, reasons = record["kind"], tuple(record.get("reason") or ())
            materiality, floor = self.materiality(rid)
            withdrawn = self.withdrawn(rid)
            if withdrawn and not floor:
                continue  # a non-floor report withdrawn by its raiser moves to the digest (§15.2)
            plan = self.plan_of(rid)
            notes = []
            if withdrawn:
                notes.append("withdrawn by raiser")
            if self.changed_since_raised(rid):
                notes.append("target changed since raised")
            detail = "; ".join(notes)
            wants_attention = (kind == "HUMAN_QUESTION" or materiality in ("MATERIAL", "CRITICAL")
                               or (kind == "CHALLENGE" and (record.get("fields") or {}).get("serious")))
            if wants_attention:
                o = self._attention({"report": rid}, materiality, plan, detail)
                if not self._resolved_by_human(o.id):
                    out.append(o)
            coordinate = kind in ("AMENDMENT_REQUEST", "BLOCKER") or (materiality != "ROUTINE" and plan is not None)
            if kind == "FINDING" and materiality == "ROUTINE":
                open_units = self.open_item_units() if open_units is None else open_units
                coordinate = bool(self._target_units(rid) & open_units)
            if coordinate and kind != "CHALLENGE":
                holder, owner = self.principal(plan)
                if not self._resolved_by_decision(rid, self.report_outcomes(rid), holder):
                    out.append(make("COORDINATE", {"report": rid}, holder=holder, plan=owner, detail=detail))
        out += self._escalations()
        out += self._floor_events()
        out += self._recurrence()
        out += self._refused_reviews()
        return out

    def identities(self) -> list[Any]:
        """The report-derived obligations a principal's result can be bound to, computed without conformance
        (review 879fa490 N1): each report's decision and human attention, and each escalation's."""

        from .workflow import make

        out: list[Any] = []
        for rid in self.reports:
            holder, owner = self.principal(self.plan_of(rid))
            out.append(make("COORDINATE", {"report": rid}, holder=holder, plan=owner))
            out.append(self._attention({"report": rid}, self.materiality(rid)[0]))
        out += self._escalations(every=True)
        return out

    def _escalations(self, every: bool = False) -> list[Any]:
        """``ESCALATE`` means human attention (§15.5; review 879fa490 B2): one per escalating decision, at least
        ``MATERIAL`` and at the materiality of the reports it names, until an authenticated human decides it."""

        out = []
        for rid in self.s.of_kind("COORDINATION_DECISION"):
            record = self.s.record(rid)
            if record["outcome"] != "ESCALATE" or not self.s.acts(rid):
                continue
            named = [r for r in (record["target"] or {}).get("records", []) if r in self.s.records
                     and self.s.record(r)["kind"] in REPORT_KINDS]
            level = max([_RANK["MATERIAL"]] + [_RANK[self.materiality(r)[0]] for r in named])
            plan = next((self.plan_of(r) for r in named if self.plan_of(r)), None)
            o = self._attention({"escalated": rid}, MATERIALITY[level], plan, "escalated by a coordination decision")
            if every or not self._resolved_by_human(o.id):
                out.append(o)
        return out

    def waiting_attention(self, judged: list[Any]) -> list[Any]:
        """Human attention for every judgment obligation waiting on no eligible judge (§5.10 (f), §10.3)."""

        out = []
        for o in judged:
            readiness = self.w.readiness(o)
            if "no eligible judge" in readiness.waiting_on:
                a = self._attention({"waiting": o.id}, "MATERIAL", o.plan, f"{o.kind} waits on a missing judge")
                if not self._resolved_by_human(a.id):
                    out.append(a)
        return out

    # -- floor events (§15.4) -------------------------------------------------------------------------------

    def _floor_events(self) -> list[Any]:
        from .s3 import Consequences

        out = []
        for finding in Consequences(self.d).findings:
            if finding.integrity:
                key = f"integrity:{finding.code}:{','.join(finding.about)}"
                o = self._attention({"floor": key}, "CRITICAL", detail=finding.detail)
                if not self._resolved_by_human(o.id):
                    out.append(o)
        out += self._plan_amendments()
        out += self._disagreement_floor()
        out += self._delegate_floor()
        return out

    def _plan_amendments(self) -> list[Any]:
        """An amendment changing a plan's objective, or changing or removing an acceptance criterion, against the
        revision then accepted (§15.4), found over the history since the first acceptance and latched: a later
        acceptance does not retire it; only an authenticated human decision does (A8; review 879fa490 B5)."""

        out = []
        for key, plan, detail in self._amendment_events():
            o = self._attention({"floor": key}, "CRITICAL", plan, detail)
            if not self._resolved_by_human(o.id):
                out.append(o)
        return out

    def _amendment_events(self) -> list[tuple[str, str | None, str]]:
        from ssds.content import Item

        from .plans import plans as plans_of

        acceptances = sorted((self.s.position_of(r), r) for r in self.s.of_kind("PLAN_ACCEPTANCE")
                             if self.s.acts(r) and self.s.record(r)["outcome"] == "ACCEPTED")
        if not acceptances:
            return []
        events: dict[str, tuple[str | None, str]] = {}
        accepted_objective: dict[str, str] = {}
        accepted_items: dict[str, str] = {}
        criteria_at: dict[tuple[str, str], dict[str, Any] | None] = {}
        seen: dict[str, str | None] = {}
        index = 0

        def criteria(view: Any, unit: str) -> dict[str, Any] | None:
            for plan in plans_of(view).values():
                if unit in plan.items and isinstance(plan.items[unit].parsed, Item):
                    return dict(plan.items[unit].parsed.acceptance_criteria)
            return None

        for k in range(acceptances[0][0], self.s.n + 1):
            while index < len(acceptances) and acceptances[index][0] <= k:
                fields = self.s.record(acceptances[index][1])["fields"]
                accepted_objective[fields["objective"]["unit"]] = fields["objective"]["rev"]
                for named in fields["items"]:
                    accepted_items[named["unit"]] = named["rev"]
                index += 1
            view = self.s.h.view(k)
            for unit, accepted in accepted_objective.items():
                now = view.rev(unit) if unit in view.structure.units else "ABSENT"
                if now != accepted and seen.get(unit) != now:
                    subject = view.structure.subj(unit) if unit in view.structure.units else unit
                    events[f"objective:{subject}:{now}"] = (subject, "the plan objective changed")
                seen[unit] = now
            for unit, accepted in accepted_items.items():
                now = view.rev(unit) if unit in view.structure.units else "ABSENT"
                if now == accepted or seen.get(unit) == now:
                    seen[unit] = now
                    continue
                seen[unit] = now
                if (unit, accepted) not in criteria_at:
                    found = self.s.plans.item_at(unit, accepted)
                    criteria_at[(unit, accepted)] = criteria(found[0], unit) if found is not None else None
                old = criteria_at[(unit, accepted)]
                new = criteria(view, unit) if now != "ABSENT" else None
                if old and (new is None or any(new.get(c) != e for c, e in old.items())):
                    subject = view.structure.subj(unit) if unit in view.structure.units else None
                    events[f"criteria:{unit}:{now}"] = (subject, "an acceptance criterion changed or was removed")
        return [(key, plan, detail) for key, (plan, detail) in sorted(events.items())]

    def _disagreement_floor(self) -> list[Any]:
        """§6.8's D1/D2 floor event: derived as soon as a failing assessment counts (reading E34) and latched
        from the first position it held, so it is closed only by an authenticated human (review 879fa490 B8)."""

        out = []
        for rid in self._disagreement_events():
            o = self._attention({"floor": f"disagreement:{rid}"}, "CRITICAL", detail="a counting failure on D1/D2 authority")
            if not self._resolved_by_human(o.id):
                out.append(o)
        return out

    def _disagreement_events(self) -> list[str]:
        candidates = []
        for rid in self.s.of_kind("EVIDENCE_ASSESSMENT"):
            then = self.s.h.view(self.s.position_of(rid))
            units = self.d.a.claim_units(rid)
            if any(v.structure.kind(u) in ("D1", "D2") for v in (then, self.s.view) for u in units if u in v.structure.units):
                candidates.append(rid)
        held = []
        for rid in sorted(candidates, key=lambda r: (self.s.position_of(r), r)):
            for k in [self.s.n, *range(self.s.position_of(rid), self.s.n)]:
                if self._disagreement_holds(rid, self._support_at(k)):
                    held.append(rid)
                    break
        return held

    @staticmethod
    def _disagreement_holds(rid: str, d: Any) -> bool:
        a = d.a
        value = lambda node: d.values.get(node, F)  # noqa: E731
        for obligation, records in a.by_obligation.items():
            if rid not in records or not any(a.passing(r) and a.admissible(r, obligation) for r in records):
                continue
            if not (a.failing(rid) and a.starts(rid) and a.admissible(rid, obligation)) or a.stale(rid, d.base, value):
                return False  # an inadmissible assessment enters neither side (§6.2; reading F89)
            return a.disposition(rid, value, d.base, d.j.nonind) == F
        return False

    def _delegate_floor(self) -> list[Any]:
        """Under ``scientific = APPLIES``, every material finding in a result's slots creates human attention."""

        out = []
        for rid in self.s.of_kind("TASK_RESULT"):
            contract = self.w.conformance(rid).contract[0]
            if contract is None or contract.scientific != "APPLIES":
                continue
            slots = (self.s.record(rid).get("fields") or {}).get("slots") or {}
            for name in ("findings", "delegate_returns"):
                entries = slots.get(name)
                for index, entry in enumerate(entries if isinstance(entries, list) else []):
                    if isinstance(entry, dict) and entry.get("materiality") in ("MATERIAL", "CRITICAL"):
                        o = self._attention({"floor": f"delegate:{rid}:{name}:{index}"}, entry["materiality"],
                                            detail="a material finding in a scientific result's slots")
                        if not self._resolved_by_human(o.id):
                            out.append(o)
        return out

    # -- decisions with no report (§15.5, §15.7, §10.4) ----------------------------------------------------

    def _answered(self, obligation_id: str) -> bool:
        return any(c for c in self.w.items.answers_to(obligation_id) if self.s.record(c)["outcome"] in NO_REPORT_OUTCOMES)

    def _recurrence(self) -> list[Any]:
        """The same HARD template failing on one obligation across iterations; the same template failing across
        items; repeated discrepancies by one route (§15.7). Detection is mechanical; the response is judgment."""

        from .workflow import make

        out = []
        by_template: dict[str, set[str]] = {}
        for item in self.w.items.all:
            for holder in (item, *item.parts):
                counts: dict[str, int] = {}
                discrepancies = 0
                for e in holder.enactments:
                    hits = self.w.conformance(e.result).hits
                    failed = {h.template for h in hits if h.cls in FAILING and TEMPLATES.get(h.template, None) is not None
                              and TEMPLATES[h.template].force != HEURISTIC}
                    for template in failed:
                        counts[template] = counts.get(template, 0) + 1
                        by_template.setdefault(template, set()).add(item.unit)
                    discrepancies += any(h.cls == DISCREPANCY for h in hits)
                keys = [("template", t, n) for t, n in sorted(counts.items()) if n >= 2]
                if discrepancies >= 2:
                    keys.append(("discrepancy", "*", discrepancies))
                for kind, value, count in keys:
                    # keyed on the occurrence count, so a further failure after an answer is a new recurrence (N5)
                    o = make("COORDINATE", {"recurrence": kind, "obligation": holder.obligation.id, "of": value, "count": count},
                             holder="PRINCIPAL", plan=item.plan, detail=f"recurrence: {kind} {value} x{count}")
                    if not self._answered(o.id):
                        out.append(o)
        for template, units in sorted(by_template.items()):
            if len(units) >= 2:
                holder, plan = self.principal(None)
                o = make("COORDINATE", {"recurrence": "family", "of": template, "items": sorted(units)}, holder=holder,
                         plan=plan, detail=f"recurrence across items: {template}")
                if not self._answered(o.id):
                    out.append(o)
        return out

    def _refused_reviews(self) -> list[Any]:
        """A REFUSED joint-invariant or specification review derives a coordination decision until one answers
        it (§10.4): for the plan of the item whose enactment made the change, else the standing plan."""

        from .workflow import REFUSED, make

        out = []
        for o in self.w.base_obligations:
            if o.kind not in ("JOINT_INVARIANT", "SPEC_REVIEW") or self.w.discharge(o) != REFUSED:
                continue
            holder, plan = self.principal(self._plan_of_change(o.params.get("change") or o.target.get("change")))
            decision = make("COORDINATE", {"refused": o.id}, holder=holder, plan=plan, detail=f"refused {o.kind}")
            if not self._answered(decision.id):
                out.append(decision)
        return out

    def _plan_of_change(self, digest: str | None) -> str | None:
        for entry in self.s.h.chain.entries[: self.s.n + 1]:
            if entry.digest != digest:
                continue
            integration = self.s.h.integrations.get(entry.position)
            if integration is None or not integration.transformation:
                return None
            result = self.w.submitting_result(integration.transformation)
            named = (self.s.record(result).get("binding") or {}).get("item") if result else None
            if isinstance(named, dict):
                for item in self.w.items.all:
                    if item.unit == named.get("unit"):
                        return item.plan
        return None
