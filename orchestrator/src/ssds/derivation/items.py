"""Item obligations and their one route (catalogue §10.4, §13.7, §15.5; SD-37 to SD-41, SD-52, SD-54, SD-55).

An item obligation's identity is its item and the prose and fixed fields of its
accepted revision (SD-52): it is derived while some plan acceptance accepted a
revision of the item with the current work key, so an R1 tightening and a
loosening keep it (the loosened item waits for a new plan acceptance before it is
issuable) and only a prose or fixed-field change derives a new one.

In each state the obligation has exactly one route, in §10.4's order: the
predicate holds (discharged); a pending candidate keeps its own routes; a
standing out-of-scope adverse review of the latest integrated enactment, or a
DISCREPANCY or VIOLATION of the latest result, goes to the principal; a spent
budget goes to the principal; otherwise it is dispatched again (drift when its
outputs moved). Every out-of-scope adverse review of any integrated enactment is
also a routed finding with its own decision, beside the route (RR-8).

A decision owed on an item route follows SD-54's one post-answer rule: it is
keyed on (condition, item revision, the answer it follows); ``ESCALATE`` answers
nothing; an ``AMEND`` that leaves the item unchanged makes it wait until that plan
change integrates, after which a condition that still holds derives the chain's
next decision naming that answer; ``PARTITION`` hands the route to the parts.
Once a chain holds 3 counted answers (SD-55), each further decision of it is held
for human attention and only an authenticated human's answer counts; a
``CHALLENGE`` counts only on a held decision and waits for its adjudication. A
fence (§22.3) is Phase F's, so this module has no fence route.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Any

from ssds.content import Item, ItemPart

from .plans import contained, resolve, work_key
from .state import F, P, T, triple_key

RECURRENCE = 3  # SD-55
IMPLEMENTER_KINDS = frozenset({"IMPLEMENT", "REPAIR", "MIGRATE", "AUTHOR", "DOCUMENT"})
ITEM_ROUTE_OUTCOMES = frozenset({"AMEND", "PARTITION", "DECLINE", "CHALLENGE", "ESCALATE"})


@dataclass(frozen=True)
class Enactment:
    task: str
    result: str  # the TASK_RESULT that ends the task
    position: int
    transformation: str | None
    outcome: str
    integrated: int | None  # the position of its integration
    refused: bool  # an integration of it was refused


@dataclass(frozen=True)
class Route:
    route: str
    decisions: tuple[Any, ...]  # open decision obligations derived beside or by the route


class ItemObligation:
    """One item obligation in one state."""

    def __init__(self, items: "Items", unit: str, plan: str, part: ItemPart) -> None:
        self.items = items
        self.w = items.w
        self.s = items.w.s
        self.d = items.w.d
        self.unit = unit
        self.plan = plan
        self.part = part
        self.item: Item = part.parsed  # type: ignore[assignment]

    # -- identity (SD-52) ------------------------------------------------------------------------

    @cached_property
    def key(self) -> str:
        return work_key(self.item, self.s.plans.prose(self.part))

    @cached_property
    def obligation(self) -> Any:
        from .workflow import IMPLEMENTER as IMPLEMENTER_ROLE
        from .workflow import INVESTIGATOR, make

        holder = IMPLEMENTER_ROLE if self.item.kind in IMPLEMENTER_KINDS else INVESTIGATOR
        return make(self.item.kind, {"item": self.unit}, {"key": self.key}, holder=holder, plan=self.plan)

    @cached_property
    def derived(self) -> bool:
        """Some acting, unsuperseded plan acceptance accepted a revision of the item with this work key."""

        for rid in self.s.of_kind("PLAN_ACCEPTANCE"):
            record = self.s.record(rid)
            if record["outcome"] != "ACCEPTED" or not self.s.acts(rid) or self.s.superseded(rid):
                continue
            for named in record["fields"]["items"]:
                if named["unit"] != self.unit:
                    continue
                found = self.s.plans.item_at(self.unit, named["rev"])
                if found is not None and isinstance(found[1].parsed, Item) and \
                        work_key(found[1].parsed, self.s.plans.prose(found[1], found[0])) == self.key:
                    return True
        return False

    # -- enactments, iterations, outputs (§10.3, §10.4) ----------------------------------------------

    @cached_property
    def enactments(self) -> tuple[Enactment, ...]:
        out = []
        for rid in self.s.of_kind("TASK_RESULT"):
            record = self.s.record(rid)
            if (record.get("binding") or {}).get("obligation") != self.obligation.id:
                continue
            target = record["target"]
            x = target.get("transformation")
            task = target["task"]
            integrated = self.s.integrated.get(task) if x and self.s.enactment(x) == task else None
            out.append(Enactment(task, rid, self.s.position_of(rid), x, record["outcome"], integrated,
                                 x in self.items.refused))
        return tuple(sorted(out, key=lambda e: (e.position, e.result)))

    @property
    def iterations(self) -> int:
        return len(self.enactments)

    @property
    def budget(self) -> int:
        return self.item.contract.budget if self.item.contract is not None else 0

    @property
    def budget_spent(self) -> bool:
        return self.iterations >= self.budget

    @cached_property
    def integrated(self) -> tuple[Enactment, ...]:
        return tuple(e for e in self.enactments if e.integrated is not None)

    @property
    def latest_integrated(self) -> Enactment | None:
        return max(self.integrated, key=lambda e: e.integrated) if self.integrated else None

    @cached_property
    def outputs(self) -> dict[str, str]:
        """``out(o)``: units its integrated enactments changed, at their revisions after its latest integration."""

        h = self.s.h
        changed: set[str] = set()
        for e in self.integrated:
            before, after = h.view(e.integrated - 1), h.view(e.integrated)
            changed |= {u for u in after.structure.units
                        if u not in before.structure.units or before.rev(u) != after.rev(u)}
        latest = self.latest_integrated
        if latest is None:
            return {}
        view = h.view(latest.integrated)
        return {u: view.rev(u) for u in sorted(changed) if u in view.structure.units}

    @property
    def moved(self) -> bool:
        return any(u not in self.s.view.structure.units or self.s.cur(u) != r for u, r in self.outputs.items())

    @property
    def subjects(self) -> frozenset[str]:
        structure = self.s.view.structure
        return frozenset(s for s in (structure.subj(u) for u in self.outputs) if s)

    # -- reviews of an enactment and the pending candidate ------------------------------------------

    def reviews(self, transformation: str) -> list[str]:
        out = []
        for rid in self.s.of_kind("REVIEW"):
            record = self.s.record(rid)
            if record["target"].get("transformation") != transformation:
                continue
            if self.s.acts(rid) or record["frame"] == {"transformation": transformation}:
                out.append(rid)
        return out

    def adverse_reviews(self, transformation: str) -> list[str]:
        return [r for r in self.reviews(transformation)
                if self.s.record(r)["outcome"] == "NO_PASS" and self.d.j.stands_adverse(r)]

    def out_of_scope(self, review: str) -> bool:
        """A NO-PASS whose findings lie outside the item's write scope and obligations (reading E30)."""

        findings = self.items.findings_of(review)
        if findings is None:
            return True  # no findings stated: the principal decides, so a finding is never lost (A8)
        contract = self.item.contract
        scope, _ = resolve(self.s.view, contract.write_scope if contract else ())
        obligations = {o.id for o in contract.obligations} if contract else set()
        for finding in findings:
            if finding.get("obligation") in obligations:
                continue
            units = finding.get("units") or []
            atoms = []
            for unit in units:
                region = self.s.view.regions.get(unit) if unit in self.s.view.structure.units else None
                if not region:
                    return True
                atoms.extend(("span", sp.path, sp.start, sp.end) for sp in region)
            if not units or not contained(self.s.view, atoms, scope):
                return True
        return False

    @cached_property
    def pending(self) -> Enactment | None:
        """The latest iteration's candidate while it is open (RR-7): complete, clean, not integrated or
        refused, no adverse answer to its review."""

        if not self.enactments:
            return None
        latest = self.enactments[-1]
        if latest.outcome != "COMPLETE" or not latest.transformation or latest.integrated is not None or latest.refused:
            return None
        if not self.w.conformance(latest.result).clean or self.adverse_reviews(latest.transformation):
            return None
        return latest

    # -- the predicate and discharge (§10.4) ---------------------------------------------------------

    @cached_property
    def predicate(self) -> int:
        """Clean conformance and a current, qualified, independent passing review of the latest integrated
        enactment; its subjects unblocked; every gate of the item (reading E30)."""

        latest = self.latest_integrated
        if latest is None or not self.w.conformance(latest.result).clean:
            return F
        value = max((self.d.current(r) for r in self.reviews(latest.transformation)
                     if self.s.record(r)["outcome"] == "PASS" and not self.d.j.nonind(r)), default=F)
        for subject in self.subjects:
            status = self.s.status1(triple_key(*self.s.subject_triple(subject)))
            if status in ("REVOKED", "BLOCKED"):
                return F
            if status == "PROVISIONAL":
                value = min(value, P)
            for gate in self.item.gates:
                value = min(value, self.d.gterm(subject, gate, self.w._value))
        return value

    def discharge(self) -> str:
        from .workflow import DISCHARGED, DISCHARGED_PROVISIONAL, OPEN

        if self.predicate == T:
            return DISCHARGED
        if self.predicate == P and self.w.provisional_scope(self.item.kind, tuple(sorted(self.subjects)), (self.unit,)):
            return DISCHARGED_PROVISIONAL
        return OPEN

    # -- decisions and their answer chains (SD-54, SD-55) --------------------------------------------

    def _decision(self, condition: str, after: str | None) -> Any:
        from .workflow import PRINCIPAL, make

        target = {"plan": self.plan, "item": self.unit, "condition": condition, "rev": self.s.cur(self.unit), "after": after}
        return make("COORDINATE", target, holder=PRINCIPAL, plan=self.plan, detail=f"{condition} on {self.unit}")

    def _finding_decision(self, kind: str, record: str) -> Any:
        from .workflow import PRINCIPAL, make

        return make("COORDINATE", {"plan": self.plan, "item": self.unit, kind: record}, holder=PRINCIPAL, plan=self.plan,
                    detail=f"{kind} {record[:19]} on {self.unit}")

    def _counts(self, answer: str, condition: str, held: bool) -> bool:
        record = self.s.record(answer)
        outcome = record["outcome"]
        if outcome not in ITEM_ROUTE_OUTCOMES or outcome == "ESCALATE":
            return False  # ESCALATE answers nothing (§15.5)
        if outcome == "DECLINE" and condition != "kept-fence":
            return False
        if outcome == "CHALLENGE" and not held:
            return False
        if held and record["actor_class"] != "HUMAN":
            return False  # a held decision is answered only by an authenticated human (SD-55)
        return True

    def _settled(self, answer: str) -> bool:
        record = self.s.record(answer)
        position = self.s.position_of(answer)
        task = (record.get("binding") or {}).get("task")
        if record["outcome"] == "AMEND":
            # The plan change follows in the same request (§15.5): settled once that change integrates.
            for rid in self.s.of_kind("TASK_RESULT"):
                other = self.s.record(rid)
                if self.s.position_of(rid) == position and (other.get("binding") or {}).get("task") == task and \
                        other["target"].get("transformation"):
                    return self.s.enactment(other["target"]["transformation"]) in self.s.integrated
            return False
        if record["outcome"] == "CHALLENGE":
            challenges = [c for c in self.s.of_kind("CHALLENGE")
                          if self.s.position_of(c) == position and self.s.record(c)["actor"] == record["actor"]]
            return bool(challenges) and not any(self.s.open(c) for c in challenges)
        return True

    def chain(self, condition: str) -> tuple[str, tuple[Any, ...], int]:
        """(route, open decisions, counted answers) of one condition's chain at the current item revision."""

        counted: list[str] = []
        after: str | None = None
        while True:
            decision = self._decision(condition, after)
            held = len(counted) >= RECURRENCE
            answer = next((a for a in self.items.answers_to(decision.id) if self._counts(a, condition, held)), None)
            if answer is None:
                if held:
                    from .workflow import HUMAN

                    decision = self._held(decision, HUMAN)
                    return f"human-attention:{condition}", (decision,), len(counted)
                return f"COORDINATE:{condition}", (decision,), len(counted)
            counted.append(answer)
            outcome = self.s.record(answer)["outcome"]
            if outcome == "DECLINE":
                return "resume", (), len(counted)
            if outcome == "PARTITION":
                return f"partitioned:{answer}", (), len(counted)
            if not self._settled(answer):
                kind = "challenge" if outcome == "CHALLENGE" else "amendment"
                return f"awaiting-{kind}:{answer}", (), len(counted)
            after = answer

    @staticmethod
    def _held(decision: Any, holder: str) -> Any:
        from dataclasses import replace

        return replace(decision, holder=holder, detail=decision.detail + " (held for human attention)")

    # -- the one route (§10.4) -----------------------------------------------------------------------

    @cached_property
    def finding_decisions(self) -> list[tuple[str, Any, bool]]:
        """(review, its decision, of the latest integrated enactment) for every standing out-of-scope adverse
        review of an integrated enactment (RR-8)."""

        latest = self.latest_integrated
        out = []
        for e in self.integrated:
            for review in self.adverse_reviews(e.transformation):
                if self.out_of_scope(review):
                    out.append((review, self._finding_decision("finding", review), e is latest))
        return out

    @cached_property
    def route(self) -> Route:
        decisions: list[Any] = []
        open_findings = [(r, o, latest) for r, o, latest in self.finding_decisions if not self.items.answers_to(o.id)]
        decisions += [o for _, o, _ in open_findings]
        if self.integrated and self.discharge() != "OPEN":
            return Route("discharged", tuple(decisions))
        if self.pending is not None:
            return Route("pending-candidate", tuple(decisions))
        latest_findings = [o for _, o, latest in open_findings if latest]
        if latest_findings:
            return Route(f"COORDINATE:finding:{latest_findings[0].target['finding']}", tuple(decisions))
        if not self.integrated and self.enactments:
            last = self.enactments[-1]
            classes = self.w.conformance(last.result).classes
            if {"DISCREPANCY", "VIOLATION"} & classes:
                o = self._finding_decision("conformance", last.result)
                if not self.items.answers_to(o.id):
                    return Route(f"COORDINATE:conformance:{last.result}", tuple(decisions + [o]))
            for review in (self.adverse_reviews(last.transformation) if last.transformation else []):
                if self.out_of_scope(review):
                    o = self._finding_decision("finding", review)
                    if not self.items.answers_to(o.id):
                        return Route(f"COORDINATE:finding:{review}", tuple(decisions + [o]))
        if self.budget_spent:
            route, opened, _ = self.chain("budget-spent")
            return Route(route, tuple(decisions) + opened)
        if not self.enactments:
            return Route("dispatch", tuple(decisions))
        return Route("re-dispatch", tuple(decisions))

    def readiness(self) -> Any:
        from .workflow import READY, WAITING, Readiness

        route = self.route.route
        if route not in ("dispatch", "re-dispatch"):
            return Readiness(WAITING, (route,))
        waiting = []
        if not self.w.issuable(self.unit):
            waiting.append("not issuable: no current plan acceptance covers the item's revision, or lint fails")
        for dependency in self.item.depends_on:
            other = self.items.by_id(self.plan, dependency)
            if other is None or other.discharge() == "OPEN":
                waiting.append(f"depends on {dependency}, not discharged")
        for unit, _ in self.item.governing:
            subject = self.s.view.structure.subj(unit) if unit in self.s.view.structure.units else None
            if subject is None or self.d.valid(subject) == F:
                waiting.append(f"governing unit {unit} is not valid")
        return Readiness(WAITING, tuple(waiting)) if waiting else Readiness(READY)


class Items:
    """The item obligations of one state."""

    def __init__(self, workflow: Any) -> None:
        self.w = workflow
        self.s = workflow.s

    @cached_property
    def all(self) -> tuple[ItemObligation, ...]:
        out = []
        for subject, plan in self.s.plans.plans.items():
            for unit, part in plan.items.items():
                if isinstance(part.parsed, Item) and part.parsed.contract is not None:
                    candidate = ItemObligation(self, unit, subject, part)
                    if candidate.derived:
                        out.append(candidate)
        return tuple(out)

    def by_id(self, plan: str, item_id: str) -> ItemObligation | None:
        return next((o for o in self.all if o.plan == plan and o.item.id == item_id), None)

    def of(self, obligation_id: str) -> ItemObligation | None:
        return next((o for o in self.all if o.obligation.id == obligation_id), None)

    @cached_property
    def refused(self) -> frozenset[str]:
        """Transformations whose integration Admission refused (an admission entry deciding REJECT)."""

        out = set()
        for entry in self.s.h.chain.entries[1: self.s.n + 1]:
            admission = entry.entry.get("admission")
            if admission and admission.get("decision") != "ACCEPT" and admission.get("integrates"):
                out.add(admission["integrates"])
        return frozenset(out)

    @cached_property
    def _answers(self) -> dict[str, list[str]]:
        out: dict[str, list[str]] = {}
        for rid in self.s.of_kind("COORDINATION_DECISION"):
            if not self.s.acts(rid):
                continue
            record = self.s.record(rid)
            named = set((record["target"] or {}).get("records", []))
            bound = (record.get("binding") or {}).get("obligation")
            for key in named | ({bound} if bound else set()):
                out.setdefault(key, []).append(rid)
        return out

    def answers_to(self, obligation_id: str) -> list[str]:
        """Coordination decisions naming the decision obligation, in position order (§15.5)."""

        return self._answers.get(obligation_id, [])

    def findings_of(self, review: str) -> list[dict[str, Any]] | None:
        """The findings of an adverse review, from its reviewer's task result (reading E30): entries naming
        ``units`` and/or an item ``obligation``. None when no result states them."""

        record = self.s.record(review)
        task = (record.get("binding") or {}).get("task")
        for rid in self.s.of_kind("TASK_RESULT"):
            result = self.s.record(rid)
            if task is not None and result["target"].get("task") == task:
                findings = ((result.get("fields") or {}).get("slots") or {}).get("findings")
                if isinstance(findings, list):
                    return [f for f in findings if isinstance(f, dict)]
                return None
        return None
