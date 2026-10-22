"""The S3 workflow layer: obligations, answering, readiness and discharge (catalogue §10.2-§10.5, §11.2).

Derived obligations follow from rules and state; they are never authored and
appear and disappear as derivation changes (§10.1). Each has a deterministic
identity (reading E4), a holder role (§10.2, §12.3), and in each state an
answer (§10.3), a readiness and a discharge value (§10.4). Readiness is
derived from the ledger and content alone; whether a ready obligation is
dispatched is the Dispatcher's (Phase F) and never feeds back here.

This module derives the judgment obligations and plan obligations of Phase E
step 3: ``PLAN_ACCEPT``, ``CONTRACT``, ``ACCEPT``, ``GATE``, the revising
review ``REVIEW(s, r)``, ``ADJUDICATE``, ``ADJUDICATE_DISAGREEMENT``,
``REVALIDATE``, ``SPEC_REVIEW`` and ``JOINT_INVARIANT``. Item obligations and
their routes, ``COORDINATE`` and ``HUMAN_ATTENTION`` are step 5's; ``REVIEW(X)``
comes with conformance (step 4); ``REALIZE``, ``ASSESS``, ``RERUN`` and
``READING`` are triggered by §17's realization machinery (Phase F).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import cached_property
from typing import Any

from ssds.content import Item

from .judgment import RouteEligibility
from .obligations import obligation_id
from .outcomes import ADVERSE, PASSING
from .runs import REVISING_REVIEW, revising_review_id
from .state import NEVER_PROVISIONAL, UNKNOWN, F, P, T, triple_key

# Holder roles (§12.3) and the Dispatcher.
PRINCIPAL, IMPLEMENTER, INVESTIGATOR, REVIEWER, HUMAN, DISPATCHER = (
    "PRINCIPAL", "IMPLEMENTER", "INVESTIGATOR", "REVIEWER", "HUMAN", "DISPATCHER")
READY, READY_PROVISIONAL, WAITING, ANSWERED = "READY", "READY_PROVISIONAL", "WAITING", "ANSWERED"
DISCHARGED, DISCHARGED_PROVISIONAL, OPEN, REFUSED = "DISCHARGED", "DISCHARGED_PROVISIONAL", "OPEN", "REFUSED"
#: The judgment kind that answers each judgment obligation kind (§10.3).
ANSWER_KIND = {"ACCEPT": "ACCEPTANCE", "GATE": "GATE_DECISION", "PLAN_ACCEPT": "PLAN_ACCEPTANCE",
               "ADJUDICATE": "ADJUDICATION", "SPEC_REVIEW": "REVIEW", "JOINT_INVARIANT": "REVIEW", "REVIEW": "REVIEW"}
#: Kinds whose answer carries an independence requirement (§5.10 (f)).
INDEPENDENT = frozenset({"ACCEPT", "PLAN_ACCEPT", "SPEC_REVIEW", "JOINT_INVARIANT", REVISING_REVIEW, "ADJUDICATE",
                         "REVIEW"})


@dataclass(frozen=True, order=True)
class Obligation:
    kind: str
    target_json: str  # canonical JSON of the target, so obligations order and hash deterministically
    params_json: str
    id: str
    holder: str
    plan: str | None = None
    detail: str = ""

    @property
    def target(self) -> Any:
        return json.loads(self.target_json)

    @property
    def params(self) -> Any:
        return json.loads(self.params_json)


def make(kind: str, target: Any, params: Any = None, holder: str = REVIEWER, plan: str | None = None,
         detail: str = "") -> Obligation:
    params = params or {}
    return Obligation(kind, json.dumps(target, sort_keys=True), json.dumps(params, sort_keys=True),
                      obligation_id(kind, target, params), holder, plan, detail)


@dataclass(frozen=True)
class Readiness:
    state: str  # READY | READY_PROVISIONAL | WAITING | ANSWERED
    waiting_on: tuple[str, ...] = ()


class Workflow:
    """The obligations of one derived state, with their answers, readiness and discharge."""

    def __init__(self, support: Any) -> None:
        self.d = support
        self.s = support.s
        self.routes = RouteEligibility(support.j)

    # -- helpers --------------------------------------------------------------------------------

    def _value(self, node: Any) -> int:
        return self.d.values.get(node, F)

    def _native(self, subject: str) -> bool:
        return self.s.mode(subject) == "NATIVE"

    def _revised_kind(self, subject: str) -> bool:
        return self._native(subject) and self.s.view.structure.kind(subject) in ("D1", "D2")

    def _subjects(self) -> list[str]:
        units = self.s.view.structure.units
        return sorted(u for u, unit in units.items() if unit.subject and self.s.view.structure.subj(u) == u)

    def _triple(self, subject: str) -> dict[str, str]:
        s, scope, rev = self.s.subject_triple(subject)
        return {"subject": s, "scope_id": scope, "rev": rev}

    def _run_params(self, subject: str) -> dict[str, Any]:
        if not self._revised_kind(subject):
            return {}
        run = self.s.runs.rid(subject)
        return {"run": list(run)} if run else {}

    def counting(self, subject: str) -> list[str]:
        """Revision-assessment records for ``(s, cur(s))`` that count: in the run, standing (§10.2)."""

        rev = self.s.cur(subject)
        return [r for r in self.s.runs.assessment_records(subject, rev)
                if self.s.runs.in_run(r, subject) and self.d.base(r) != F]

    # -- plan acceptance and issuability (§11.2) ------------------------------------------------

    @cached_property
    def plan_acceptances(self) -> list[str]:
        return [r for r in self.s.of_kind("PLAN_ACCEPTANCE")
                if self.s.record(r)["outcome"] == "ACCEPTED" and self.d.current(r) > F]

    def covered(self, item_unit: str) -> str | None:
        """A current plan acceptance covering the item's current revision (through ``⊑``), or None."""

        for rid in self.plan_acceptances:
            for named in self.s.record(rid)["fields"]["items"]:
                if named["unit"] == item_unit and self.s.plans.tightens_to_current(item_unit, named["rev"]):
                    return rid
        return None

    def issuable(self, item_unit: str) -> bool:
        """Covered by a current plan acceptance, with a contract and no lint finding (§11.2, §11.3)."""

        if item_unit not in self.s.plans.items or self.covered(item_unit) is None:
            return False
        _, part = self.s.plans.items[item_unit]
        return isinstance(part.parsed, Item) and part.parsed.contract is not None and not self.s.plans.item_lint(item_unit)

    # -- the obligations ------------------------------------------------------------------------

    @cached_property
    def obligations(self) -> tuple[Obligation, ...]:
        found: list[Obligation] = []
        found += self._plan_obligations()
        found += self._subject_obligations()
        found += self._challenge_obligations()
        found += self._disagreement_obligations()
        found += self._spec_and_invariant_obligations()
        found += self._review_obligations()
        found += self._revalidations(found)
        unique = {o.id: o for o in found}
        return tuple(sorted(unique.values()))

    def of_kind(self, *kinds: str) -> list[Obligation]:
        return [o for o in self.obligations if o.kind in kinds]

    def _plan_obligations(self) -> list[Obligation]:
        out = []
        for subject, plan in self.s.plans.plans.items():
            items = sorted(plan.items)
            uncovered = [u for u in items if self.covered(u) is None]
            if uncovered and plan.objective is not None:
                target = {"plan": subject, "objective": {"unit": plan.objective, "rev": self.s.cur(plan.objective)},
                          "items": [{"unit": u, "rev": self.s.cur(u)} for u in items]}
                out.append(make("PLAN_ACCEPT", target, holder=REVIEWER, plan=subject,
                                detail=f"uncovered items: {', '.join(uncovered)}"))
            for unit in items:
                if self.covered(unit) is None:
                    continue
                part = plan.items[unit]
                lacking = not isinstance(part.parsed, Item) or part.parsed.contract is None or self.s.plans.item_lint(unit)
                if lacking:
                    out.append(make("CONTRACT", {"item": unit, "rev": self.s.cur(unit)}, holder=PRINCIPAL, plan=subject))
        return out

    def _subject_obligations(self) -> list[Obligation]:
        out = []
        for subject in self._subjects():
            if not self._native(subject):
                continue  # LEGACY(p) and UNGOVERNED subjects owe no SSDS acceptance (§19.2)
            triple, params = self._triple(subject), self._run_params(subject)
            domain = self.s.view.structure.domain(subject)
            holder = HUMAN if domain in ("D1", "D2") else REVIEWER
            accept = make("ACCEPT", triple, params, holder=holder)
            # "Without a valid acceptance": discharged, or provisionally inside a declared scope (§10.4, §10.5).
            accepted = self.discharge(accept) in (DISCHARGED, DISCHARGED_PROVISIONAL)
            needs_gate = []
            for gate in self.s.policy.get(domain, "gates"):
                if self.d.gterm(subject, gate, self._value) == F:
                    needs_gate.append(gate)
                    out.append(make("GATE", {"gate": gate, "subject": triple}, params, holder=HUMAN))
            if not accepted:
                out.append(accept)
            if (not accepted or needs_gate) and self._revised_kind(subject) and not self.counting(subject):
                out.append(make(REVISING_REVIEW, {"subject": subject, "rev": triple["rev"]}, params, holder=REVIEWER))
        return out

    def _challenge_obligations(self) -> list[Obligation]:
        out = []
        for c in self.s.of_kind("CHALLENGE"):
            if self.s.open(c) and self.s.acts(c):
                serious = bool(self.s.record(c)["fields"].get("serious"))
                out.append(make("ADJUDICATE", {"record": c}, holder=HUMAN if serious else REVIEWER))
        return out

    def _disagreement_obligations(self) -> list[Obligation]:
        out = []
        for z in sorted(self.s.records):
            if not self.d.passing(z) or not self.s.acts(z):
                continue
            for x in self._vetoes_of(z):
                out.append(make("ADJUDICATE_DISAGREEMENT", {"record": x}, {"vetoes": z}, holder=REVIEWER))
        for obligation, records in sorted(self.d.a.by_obligation.items()):
            for a in records:
                if not (self.d.a.failing(a) and self.d.a.starts(a)) or self.d.a.stale(a, self.d.base, self._value):
                    continue
                if self.d.a.disposition(a, self._value, self.d.base, self.d.j.nonind) == F:
                    out.append(make("ADJUDICATE_DISAGREEMENT", {"record": a}, {"obligation": obligation}, holder=REVIEWER))
        return out

    def _vetoes_of(self, z: str) -> list[str]:
        j = self.d.j
        return [x for x in j.adverse_by_kind.get(self.s.record(z)["kind"], [])
                if j.stands_adverse(x) and j.same(x, z) and not j.relieved(x, z)]

    def _spec_and_invariant_obligations(self) -> list[Obligation]:
        out = []
        h, structure = self.s.h, self.s.view.structure
        for unit in sorted(u for u in structure.units if structure.kind(u) == "EVIDENCE_SPEC" and structure.subj(u) == u):
            changed = self._last_change(unit)
            if changed:
                out.append(make("SPEC_REVIEW", self._triple(unit), {"change": changed}, holder=REVIEWER))
        for decl in self.s.view.semantic_declarations:
            if decl.get("decl") != "joint_invariant":
                continue
            units = set(decl["units"])
            for k in range(self.s.n, 0, -1):
                before, after = h.view(k - 1), h.view(k)
                if any((u in after.structure.units) != (u in before.structure.units) or
                       (u in after.structure.units and after.rev(u) != before.rev(u)) for u in units):
                    out.append(make("JOINT_INVARIANT", {"invariant": decl["id"], "change": h.chain.entries[k].digest},
                                    holder=REVIEWER))
                    break
        return out

    # -- conformance and REVIEW(X) (§11.5, §14) ------------------------------------------------------

    @cached_property
    def _conformance(self) -> dict[str, Any]:
        return {}

    def conformance(self, result: str) -> Any:
        """The conformance of an admitted task result (§14.1)."""

        from .conformance import Conformance

        if result not in self._conformance:
            self._conformance[result] = Conformance(self, result)
        return self._conformance[result]

    def submitting_result(self, transformation: str) -> str | None:
        """The task result that first submitted ``X`` (§7.1)."""

        for rid in self.s.of_kind("TASK_RESULT"):
            if self.s.record(rid)["target"].get("transformation") == transformation:
                return rid
        return None

    def _review_obligations(self) -> list[Obligation]:
        """``REVIEW(X)``: a task result whose conformance is CLEAN, while ``X`` is unintegrated (§10.2)."""

        out = []
        for transformation, task in sorted(self.s.submissions.items()):
            if task in self.s.integrated:
                continue
            result = self.submitting_result(transformation)
            if result is not None and self.s.record(result)["outcome"] == "COMPLETE" and self.conformance(result).clean:
                out.append(make("REVIEW", {"transformation": transformation}, holder=REVIEWER))
        return out

    def _frame_support(self, transformation: str) -> Any:
        from .frames import frame_state
        from .support import Support

        state = frame_state(self.s.h, self.s.n, transformation, self.s)
        return Support(state) if state is not None else None

    def _last_change(self, unit: str) -> str | None:
        h = self.s.h
        for k in range(self.s.n, 0, -1):
            before, after = h.view(k - 1), h.view(k)
            if unit not in before.structure.units or before.rev(unit) != after.rev(unit):
                return h.chain.entries[k].digest
        return None

    def _revalidations(self, found: list[Obligation]) -> list[Obligation]:
        """``REVALIDATE(x)``: an acting, unsuperseded, unvetoed judgment no longer current that an obligation's
        term needs, because no other judgment satisfies that term (§10.2); each member of a minimum (``gterm``)."""

        out = []
        for o in found:
            if o.kind not in ("ACCEPT", "GATE", "PLAN_ACCEPT") or self.discharge(o) in (DISCHARGED, DISCHARGED_PROVISIONAL):
                continue
            candidates = self._answers(o)
            if o.kind == "GATE":
                members = candidates
            else:
                members = candidates if not any(self.d.current(r) > F for r in candidates) else []
            for x in members:
                if self.d.current(x) == F and not self.s.superseded(x) and not self.d.j.vetoed(x):
                    holder = HUMAN if self.s.record(x)["actor_class"] == "HUMAN" else REVIEWER
                    out.append(make("REVALIDATE", {"record": x}, {"for": o.id}, holder=holder))
        return out

    # -- answers (§10.3) ------------------------------------------------------------------------

    def _on_target(self, o: Obligation, rid: str) -> bool:
        record, target = self.s.record(rid), o.target
        if o.kind == "ACCEPT":
            return record["target"] == target
        if o.kind == "GATE":
            return record["target"]["gate"] == target["gate"] and record["target"]["subject"] == target["subject"]
        if o.kind == "PLAN_ACCEPT":
            fields = record["fields"]
            return fields["objective"] == target["objective"] and \
                sorted(map(json.dumps, fields["items"])) == sorted(map(json.dumps, target["items"]))
        if o.kind == "ADJUDICATE":
            return record["target"] == target
        if o.kind == "SPEC_REVIEW":
            return record["target"] == target
        if o.kind == "REVIEW":
            return record["target"].get("transformation") == target["transformation"]
        if o.kind == "JOINT_INVARIANT":
            t = record["target"]
            return t.get("integrated") == "JOINT_INVARIANT" and t.get("of") == target["invariant"] and \
                t.get("at") == target["change"]
        return False

    def _answers(self, o: Obligation) -> list[str]:
        """Judgments of the obligation's kind acting here on its exact target, in its run where it has one."""

        kind = ANSWER_KIND.get(o.kind)
        if kind is None:
            return []
        subject = o.target.get("subject") if o.kind == "ACCEPT" else (
            o.target["subject"]["subject"] if o.kind == "GATE" else None)
        out = []
        for rid in self.s.of_kind(kind):
            # A review of X declares frame id(X) (§11.5): it answers REVIEW(X) in that frame, the obligation's state.
            in_frame = o.kind == "REVIEW" and self.s.record(rid)["frame"] == {"transformation": o.target["transformation"]}
            if not (self.s.acts(rid) or in_frame) or not self._on_target(o, rid):
                continue
            if subject and self._revised_kind(subject) and self.s.runs.named(rid, subject) != self.s.runs.rid(subject):
                continue
            out.append(rid)
        return out

    def answer(self, o: Obligation) -> str | None:
        """The first judgment acting here of its kind on its exact target, bound to it or by an authenticated
        human; a non-independent passing judgment does not answer an obligation that requires independence."""

        for rid in self._answers(o):
            record = self.s.record(rid)
            bound = (record.get("binding") or {}).get("obligation") == o.id
            if not (bound or record["actor_class"] == "HUMAN"):
                continue
            if o.kind in INDEPENDENT and self.d.passing(rid) and self.d.j.nonind(rid):
                continue
            return rid
        return None

    def iterations(self, o: Obligation) -> int:
        """Admitted ``TASK_RESULT`` records bound to the obligation (§10.3)."""

        return sum(1 for r in self.s.of_kind("TASK_RESULT") if (self.s.record(r).get("binding") or {}).get("obligation") == o.id)

    # -- discharge (§10.4, §10.5) ---------------------------------------------------------------

    def provisional_allowed(self, o: Obligation, subject: str | None) -> bool:
        """``P`` inputs discharge provisionally only inside an in-force override's scope or where policy
        permits it for the kind; never for gate, human-attention, adjudication or integrity obligations."""

        if o.kind in NEVER_PROVISIONAL:
            return False
        if o.kind in self.s.policy.flow("provisional_kinds"):
            return True
        for rid in self.s.of_kind("RISK_OVERRIDE"):
            scope = self.s.record(rid)["fields"]["continuation"]
            if not self.s.in_force(rid) or not isinstance(scope, dict) or o.kind not in scope.get("kinds", ()):
                continue
            if subject is not None and subject in scope.get("subjects", ()):
                return True
            plan = self.s.plans.plans.get(o.plan) if o.plan is not None else None
            if plan is not None and set(plan.items) & set(scope.get("items", ())):
                return True
        return False

    def _subject_of(self, o: Obligation) -> str | None:
        target = o.target
        if o.kind in ("ACCEPT", "SPEC_REVIEW"):
            return target["subject"]
        if o.kind == "GATE":
            return target["subject"]["subject"]
        return None

    def discharge(self, o: Obligation) -> str:
        answer = self.answer(o)
        if answer is None:
            return OPEN
        record = self.s.record(answer)
        if ADVERSE.get(record["kind"]) == record["outcome"] and self.d.j.stands_adverse(answer):
            return REFUSED
        if PASSING.get(record["kind"]) != record["outcome"]:
            return OPEN
        subject = self._subject_of(o)
        value = self.d.current(answer)
        if o.kind == "REVIEW":
            framed = self._frame_support(o.target["transformation"])
            value = framed.current(answer) if framed is not None else F
        if o.kind == "GATE":
            value = self.d.gterm(subject, o.target["gate"], self._value)
        elif subject is not None and o.kind == "ACCEPT":
            status = self.s.status1(triple_key(*self.s.subject_triple(subject)))
            if status in ("REVOKED", "BLOCKED"):
                return OPEN
            if status == "PROVISIONAL":
                value = min(value, P)
            domain = self.s.view.structure.domain(subject)
            for obligation in self.s.policy.get(domain, "evidence"):
                value = min(value, self.d.a.ev(subject, obligation, self._value, self.d.base, self.d.j.nonind))
            value = min(value, self.d.a.qual(subject, self._value, self.d.base, self.d.j.nonind))
        if value == T:
            return DISCHARGED
        if value == P and self.provisional_allowed(o, subject):
            return DISCHARGED_PROVISIONAL
        return OPEN

    # -- readiness (§10.3) ----------------------------------------------------------------------

    def readiness(self, o: Obligation) -> Readiness:
        if o.kind in ANSWER_KIND and self.answer(o) is not None:
            return Readiness(ANSWERED)
        waiting: list[str] = []
        subject = self._subject_of(o) or (o.target.get("subject") if o.kind == REVISING_REVIEW else None)
        if o.kind in ("ACCEPT", "GATE") and subject is not None:
            if not self.d.ok(subject):
                waiting.append(f"{subject} is ill-formed or carries quarantined structure")
            if self._revised_kind(subject) and not self.counting(subject):
                run = self.s.runs.rid(subject)
                waiting.append(f"REVIEW(s, r): {revising_review_id(subject, self.s.cur(subject), run) if run else subject}")
        if o.kind == "PLAN_ACCEPT":
            findings = self.s.plans.lint.get(o.plan, ())
            if findings:
                waiting.append(f"lint: {len(findings)} finding(s) on {o.plan}")
        judges = self.eligible_judges(o)
        if not judges:
            waiting.append("no eligible judge")
        if waiting:
            return Readiness(WAITING, tuple(waiting))
        return Readiness(READY)

    def judged_authors(self, o: Obligation) -> frozenset[str]:
        """The authors of what an answer to ``o`` judges (§5.10 (b))."""

        target = o.target
        subject = self._subject_of(o) or (target.get("subject") if o.kind == REVISING_REVIEW else None)
        if subject is not None:
            return self.s.authors(subject, self.s.cur(subject))
        if o.kind == "PLAN_ACCEPT":
            out: set[str] = set()
            for entry in [target["objective"], *target["items"]]:
                out |= self.s.authors(entry["unit"], entry["rev"])
            return frozenset(out)
        if o.kind == "REVIEW":
            return frozenset(self.s._makers(target["transformation"])) or frozenset({UNKNOWN})
        if o.kind in ("ADJUDICATE", "ADJUDICATE_DISAGREEMENT", "REVALIDATE"):
            return self.d.j.root_authors(target["record"]) if target["record"] in self.s.records else frozenset({UNKNOWN})
        return frozenset({UNKNOWN})

    def domain_of(self, o: Obligation) -> str | None:
        """The domain an answer to ``o`` is judged in: its subject's, its plan's, or its record's (§5.10 (e))."""

        subject = self._subject_of(o) or (o.target.get("subject") if o.kind == REVISING_REVIEW else None)
        if subject is not None:
            return self.s.view.structure.domain(subject)
        if o.plan is not None:
            return self.s.view.structure.domain(o.plan)
        record = o.target.get("record") if isinstance(o.target, dict) else None
        if record in self.s.records:
            return self.d.j.domain_of(self.s.record(record))
        return None

    def eligible_judges(self, o: Obligation) -> tuple[str, ...]:
        """Who could give an admissible answer here (reading E23): named humans outside the authors, or a
        freshly launched agent reviewer when agents may answer the kind and the authorship is known."""

        subject = self._subject_of(o) or (o.target.get("subject") if o.kind == REVISING_REVIEW else None)
        domain = self.domain_of(o)
        policy = self.s.policy
        authors = self.judged_authors(o)
        if o.kind == "GATE":
            holders = policy.get(domain, "gate_holders", ())
            return tuple(h for h in holders if h.startswith("human:"))
        if o.kind == "ADJUDICATE_DISAGREEMENT":
            x = o.target["record"]
            vetoed = o.params.get("vetoes")
            if vetoed:
                routes = self.routes.routes(x, vetoed)
                return tuple(sorted(routes.admissible))
            owner = policy.get(self.d.j.domain_of(self.s.record(x)), "owner", None)
            return (owner,) if owner else ()
        if o.kind == "ADJUDICATE":
            record = self.s.record(o.target["record"])
            domain = self.d.j.domain_of(record)
            owner = policy.get(domain, "owner", None)
            names = list(policy.get(domain, "adjudicators", [owner] if owner else []))
            if record["fields"].get("serious"):
                names = [n for n in names if n.startswith("human:")]
            return tuple(n for n in names if self.routes.independent(n, authors, domain))
        humans = list(policy.get(domain, "humans", ())) + [a for a in policy.get(domain, "acceptors", ()) or ()
                                                            if a.startswith("human:")]
        if o.kind == "REVALIDATE" and o.target["record"] in self.s.records:
            actor = self.s.record(o.target["record"])["actor"]
            if actor.startswith("human:"):
                humans.append(actor)  # its own author may reassess it (§5.10 (d) route 1)
        out = sorted({h for h in humans if self.routes.independent(h, authors, domain)})
        revalidated = self.s.record(o.target["record"]) if o.kind == "REVALIDATE" and o.target["record"] in self.s.records else None
        human_only = (o.kind == "ACCEPT" and domain in ("D1", "D2")) or (
            revalidated is not None and (revalidated["actor_class"] == "HUMAN" and domain in ("D1", "D2")
                                         or revalidated["kind"] in ("GATE_DECISION",)))
        acceptors = policy.get(domain, "acceptors", None)
        agents_allowed = not human_only and (o.kind != "ACCEPT" or acceptors is None or "class:AGENT" in acceptors)
        if agents_allowed and UNKNOWN not in authors:
            out.append("agent:fresh-reviewer")
        return tuple(out)
