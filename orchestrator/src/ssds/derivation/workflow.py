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
from ssds.ledger.read import submits

from .judgment import RouteEligibility
from .obligations import obligation_id
from .outcomes import ADVERSE, PASSING
from .runs import REVISING_REVIEW, revising_review_id
from .state import NEVER_PROVISIONAL, UNKNOWN, F, P, T, triple_key

# Holder roles (§12.3) and the Dispatcher.
PRINCIPAL, IMPLEMENTER, INVESTIGATOR, REVIEWER, HUMAN, DISPATCHER = (
    "PRINCIPAL", "IMPLEMENTER", "INVESTIGATOR", "REVIEWER", "HUMAN", "DISPATCHER")
READY, READY_PROVISIONAL, WAITING, ANSWERED = "READY", "READY_PROVISIONAL", "WAITING", "ANSWERED"
#: The holders a task is issued to (§12.3's agent role templates, the principal's R1 included); the human holds briefs
#: and the Dispatcher's own obligations are its mechanical duty.
AGENT_ROLES = frozenset({PRINCIPAL, IMPLEMENTER, INVESTIGATOR, REVIEWER})
DISCHARGED, DISCHARGED_PROVISIONAL, OPEN, REFUSED = "DISCHARGED", "DISCHARGED_PROVISIONAL", "OPEN", "REFUSED"
#: The judgment kind that answers each judgment obligation kind (§10.3).
ANSWER_KIND = {"ACCEPT": "ACCEPTANCE", "GATE": "GATE_DECISION", "PLAN_ACCEPT": "PLAN_ACCEPTANCE",
               "ADJUDICATE": "ADJUDICATION", "SPEC_REVIEW": "REVIEW", "JOINT_INVARIANT": "REVIEW", "REVIEW": "REVIEW"}
#: Item obligation kinds (§10.2): an accepted, issuable item of that kind with a contract.
ITEM_KINDS = frozenset({"IMPLEMENT", "REPAIR", "MIGRATE", "AUTHOR", "DOCUMENT", "INVESTIGATE"})
#: Obligation kinds answered by a judgment, which wait on an eligible judge (§10.3).
JUDGED = frozenset(ANSWER_KIND) | {REVISING_REVIEW, "ADJUDICATE_DISAGREEMENT", "REVALIDATE", "ASSESS", "READING"}
#: Subject kinds that owe no ACCEPT(s): plans (PLAN_ACCEPT, §11.2) and the system units (§1.8).
NO_ACCEPT_KINDS = frozenset({"PLAN", "MANIFEST", "POLICY", "UNCLASSIFIED"})
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
        """A current plan acceptance covering the item's current revision (through ``⊑``), or None.

        Current means ``T``, or ``P`` only inside a provisional scope covering the item (§10.3, §10.5); the
        acceptance must also name the plan's current Objective revision, which every plan acceptance names
        ``EXACT`` (§13.2)."""

        subject = self.s.plans.items[item_unit][0] if item_unit in self.s.plans.items else None
        plan = self.s.plans.plans.get(subject) if subject else None
        objective = (plan.objective, self.s.cur(plan.objective)) if plan is not None and plan.objective else None
        for rid in self.plan_acceptances:
            fields = self.s.record(rid)["fields"]
            if objective is None or (fields["objective"]["unit"], fields["objective"]["rev"]) != objective:
                continue
            if self.d.current(rid) == P and not self.provisional_scope("PLAN_ACCEPT", (), (item_unit,)):
                continue
            for named in fields["items"]:
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
        """Every obligation of the state: the base obligations, and the report, floor and recurrence
        obligations with human attention for judgments waiting on a missing judge (§15)."""

        from .reports import Reports

        reports = Reports(self)
        base = list(self.base_obligations)
        found = base + reports.obligations + reports.waiting_attention([o for o in base if o.kind in JUDGED])
        unique = {o.id: o for o in found}
        return tuple(sorted(unique.values()))

    def _reissue_obligations(self) -> list[Obligation]:
        """``REISSUE(envelope)`` for the Dispatcher (R0; catalogue §8.3 step 3, §10.2): an admission refused a
        never-lost record under a retired key's envelope its retirement did not list, keeping the record's bytes by
        content identity. Open until a record whose provenance cites each such refusal (``reissue_of``) is
        admitted, the Dispatcher resubmitting it under the re-issued task's envelope."""

        h = self.s.h
        pending: dict[str, set[str]] = {}
        for entry in h.chain.entries[1: self.s.n + 1]:
            admission = entry.entry.get("admission") or {}
            for refusal in admission.get("refused", []):
                rid = refusal.get("record_id")
                if "AUTH_ENVELOPE" not in refusal.get("reasons", []) or rid not in entry.objects:
                    continue
                try:
                    body = json.loads(entry.objects[rid])
                except ValueError:
                    continue
                envelope = (body.get("binding") or {}).get("envelope") if isinstance(body, dict) else None
                if isinstance(envelope, str) and not self._resubmitted(rid, body):
                    pending.setdefault(envelope, set()).add(rid)
        return [make("REISSUE", {"envelope": envelope}, {"records": sorted(records)}, holder=DISPATCHER)
                for envelope, records in sorted(pending.items())]

    def _evidence_obligations(self) -> list[Obligation]:
        """``REALIZE``, ``ASSESS``, ``RERUN`` and ``READING`` (§10.2, §6.8-§6.9; reading F95), in the admitted
        state only: a frame derives none (SD-70)."""

        if self.s.frame is not None:
            return []
        from ssds.content import SpecDeclaration

        s, a = self.s, self.d.a
        structure = s.view.structure
        subjects = [u for u, unit in structure.units.items() if unit.subject]
        out: list[Obligation] = []
        required = sorted({e for subject in subjects for e in s.evidence.required(subject)})
        realizations = [r for r in s.of_kind("REALIZATION") if s.record(r)["outcome"] == "COMPLETE"]
        for e in required:  # REALIZE(e): no current, complete, admissible realization of the current revisions
            claim, spec = s.evidence.readable(e) or (None, None)
            if claim is None or s.specs.defective(spec):
                continue  # a defective specification derives none (F84)
            current = {(spec, s.cur(spec)), (claim, s.cur(claim))}

            def serves(r: str) -> bool:
                record = s.record(r)
                target = record["target"]
                revisions = {(target["spec"]["unit"], target["spec"]["rev"])} | {
                    (c["unit"], c["rev"]) for c in target.get("claim") or []}
                return current <= revisions and a.realization_ok(r, e) and self.d.current(r) > F \
                    and not a.unavailable_needed(r)

            if not any(serves(r) for r in realizations):
                out.append(make("REALIZE", {"obligation": e},
                                {"spec": {"unit": spec, "rev": s.cur(spec)}, "claim": [{"unit": claim, "rev": s.cur(claim)}]},
                                holder=DISPATCHER))
        for r in realizations:  # ASSESS(realization, e): admitted, complete, admissible, no acting assessment for e
            record = s.record(r)
            spec = record["target"]["spec"]["unit"]
            for claim in sorted({c["unit"] for c in record["target"].get("claim") or [] if isinstance(c, dict)}):
                e = s.evidence.token(claim, spec)
                if not s.evidence.required_somewhere(e) or not a.realization_ok(r, e, adverse=True):
                    continue
                if any(s.acts(x) and s.record(x)["target"].get("realization") == r
                       and s.record(x)["target"].get("obligation") == e for x in s.of_kind("EVIDENCE_ASSESSMENT")):
                    continue
                out.append(make("ASSESS", {"realization": r}, {"obligation": e}, holder=REVIEWER))
        for e, records in sorted(a.by_obligation.items()):  # RERUN and READING for a counting, unstale failure
            for x in records:
                if not (a.failing(x) and a.admissible(x, e) and a.starts(x)) \
                        or not any(a.about(x, subject) for subject in subjects) \
                        or a.stale(x, self.d.base, self._value) \
                        or a.disposition(x, self._value, self.d.base, self.d.j.nonind) != F:
                    continue
                found = a.explain(x, self.d.base, self._value)
                real = a.real(x)
                if real is None or found["differed"]:
                    continue  # (2) failed: nondeterministic in fact, the owner's (§6.9)
                for on, tree, lacking in (("FAILING", a.basis(real).get("tree"), not found["reproduced"]),
                                          ("HERE", s.h.head(s.n), not found["observed_here"])):
                    if lacking and self._bounded(real, on) and not self._rerun_done(x, real, tree):
                        out.append(make("RERUN", {"record": x, "on": on}, {"tree": tree}, holder=DISPATCHER))
                declared = a.declaration(real)
                unit = s.record(x)["fields"]["reading"]["unit"]
                rev = s.cur(unit) if unit in structure.units else None
                # another run here that no standing reading covers under G's reading: the failing one is read
                # (§6.9; reading F110)
                here = [o for o in found["observed_here"] if o != real and not a.covered(o, x, unit, rev)]
                if isinstance(declared, SpecDeclaration) and declared.oracle == "ASSESSOR_READ" and here:
                    o = here[0]  # one observation names the obligation; any other run here would serve (N2)
                    if not any(s.acts(y) and s.record(y)["target"].get("realization") == o and a.failing(y)
                               for y in s.of_kind("EVIDENCE_ASSESSMENT")):
                        cls = "R3" if a.needs_r3(x) else "R2"  # §6.8's class, the one predicate (F108)
                        out.append(make("READING", {"record": x}, {"observation": o, "class": cls}, holder=REVIEWER))
        return out

    def _bounded(self, real: str, on: str) -> bool:
        """A completeness judgment bounds the configuration's execution closure where the rerun would run (§6.9;
        plan check note 3; review of affd87fa, N3): on the failing tree, ``bound(o, tree(o))``, the judgments the
        realization recorded checked there by the one owner (re-check of 2136fb90, note 1); here, a current one."""

        a = self.d.a
        basis = a.basis(real)
        bounded = basis.get("bounded_by")
        if on == "FAILING":
            return a.bound(real, a.tree_of(real), self.d.base, self._value)
        if isinstance(bounded, list) and bounded and all(c in self.s.records and self.d.current(c) > F for c in bounded):
            return True
        units = {u.get("unit") for u in basis.get("units", []) if isinstance(u, dict)}
        return bool(units) and any(  # any current completeness judgment of the closure, a fresh one included
            self.s.acts(c) and self.s.record(c)["outcome"] == "COMPLETE" and self.d.current(c) > F
            and "EXEC" in (self.s.record(c)["target"].get("classes") or [])
            and units <= set(self.s.record(c)["target"].get("scope") or []) for c in self.s.of_kind("COMPLETENESS"))

    def _rerun_done(self, failing: str, real: str, tree: str) -> bool:
        """A complete admitted observation of ``conf(a⁻)`` on ``tree`` with ``ext``-equal pins and attributes
        exists: the rerun ran, whether or not it serves, so it never loops; an INCOMPLETE run does not end it (F95)."""

        a = self.d.a
        return any(o != real and self.s.record(o)["outcome"] == "COMPLETE" and a.basis(o).get("tree") == tree
                   and a.ext(o, real) for o in a.observations(failing))

    def _resubmitted(self, rid: str, body: dict[str, Any]) -> bool:
        """An admitted record is the refused one resubmitted: the same record apart from its binding, by the same
        actor, with the same lineage class (catalogue §8.3 step 3: "keeping its original actor and lineage class";
        review 8d274c4 B2), its provenance the retained one with the refusal cited (``reissue_of``; review of 26907956,
        B2). A citation alone discharges nothing."""

        def content(record: dict[str, Any]) -> dict[str, Any]:
            return {k: v for k, v in record.items() if k not in ("id", "binding", "provenance")}

        lineage = (body.get("binding") or {}).get("lineage_class")
        kept = body.get("provenance") if isinstance(body.get("provenance"), dict) else {}
        return any(self.s.record(r).get("provenance") == {**kept, "reissue_of": rid}  # review of 26907956, B2
                   and content(self.s.record(r)) == content(body)
                   and (self.s.record(r).get("binding") or {}).get("lineage_class") == lineage
                   for r in self.s.records)

    @cached_property
    def base_obligations(self) -> tuple[Obligation, ...]:
        found: list[Obligation] = []
        found += self._plan_obligations()
        found += self._subject_obligations()
        found += self._challenge_obligations()
        found += self._disagreement_obligations()
        found += self._spec_and_invariant_obligations()
        found += self._review_obligations()
        found += self._reissue_obligations()
        found += self._evidence_obligations()
        for item in self.items.all:
            found.append(item.obligation)
            found.extend(item.route.decisions)
            for part in item.parts:
                found.append(part.obligation)
                found.extend(part.route.decisions)
            if (item.route.route == "item-level-review" or item.carried_review_owed) and not item.waived \
                    and item.item_level_target is not None:
                found.append(make("REVIEW", item.item_level_target, holder=REVIEWER, plan=item.plan))
        found += self.items.orphan_decisions
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
            if self.s.view.structure.kind(subject) in NO_ACCEPT_KINDS:
                continue  # a plan is accepted by PLAN_ACCEPTANCE (§11.2); system units are no work (reading E23)
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
            if not self.d.passing(z) or not self.s.acts(z) or self.s.superseded(z):
                continue  # the disagreement ends with the vetoed judgment's supersession (§5.10 (d), §10.3)
            for x in self._vetoes_of(z):
                out.append(make("ADJUDICATE_DISAGREEMENT", {"record": x}, {"vetoes": z}, holder=REVIEWER))
        for obligation, records in sorted(self.d.a.by_obligation.items()):
            for a in records:
                if not (self.d.a.failing(a) and self.d.a.starts(a) and self.d.a.admissible(a, obligation)) \
                        or self.d.a.stale(a, self.d.base, self._value):
                    continue  # an inadmissible assessment enters neither side (§6.2; reading F89)
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
        # The latest change derives its obligation; an earlier one stays derived while REFUSED, until a
        # coordination decision answers it (§10.2 "or while REFUSED", SD-37; the decision is step 5's).
        for unit in sorted(u for u in structure.units if structure.kind(u) == "EVIDENCE_SPEC" and structure.subj(u) == u):
            for index, k in enumerate(self._changes(unit)):
                view = h.view(k)
                target = {"subject": unit, "scope_id": view.scope_id(unit), "rev": view.rev(unit)}
                o = make("SPEC_REVIEW", target, {"change": h.chain.entries[k].digest}, holder=REVIEWER)
                if index == 0 or self.discharge(o) == REFUSED:
                    out.append(o)
        for decl in self.s.view.semantic_declarations:
            if decl.get("decl") != "joint_invariant":
                continue
            changes = [k for k in range(self.s.n, 0, -1) if self._touches(set(decl["units"]), k)]
            for index, k in enumerate(changes):
                o = make("JOINT_INVARIANT", {"invariant": decl["id"], "change": h.chain.entries[k].digest}, holder=REVIEWER)
                if index == 0 or self.discharge(o) == REFUSED:
                    out.append(o)
        return out

    def _touches(self, units: set[str], k: int) -> bool:
        before, after = self.s.h.view(k - 1), self.s.h.view(k)
        return any((u in after.structure.units) != (u in before.structure.units) or
                   (u in after.structure.units and after.rev(u) != before.rev(u)) for u in units)

    def _changes(self, unit: str) -> list[int]:
        """Positions at which ``unit``'s revision changed, latest first."""

        h = self.s.h
        return [k for k in range(self.s.n, 0, -1)
                if unit in h.view(k).structure.units and (unit not in h.view(k - 1).structure.units
                                                           or h.view(k - 1).rev(unit) != h.view(k).rev(unit))]

    # -- item obligations (§10.4) --------------------------------------------------------------------

    @cached_property
    def items(self) -> Any:
        from .items import Items

        return Items(self)

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

    def binding_index(self) -> dict[str, Obligation]:
        """Obligation identity -> obligation, for resolving what a result is bound to without deriving
        REVIEW(X) through conformance (step 4 review B2): REVIEW(X) is listed for every unintegrated submission."""

        if "_binding_index" not in self.__dict__:
            found: list[Obligation] = []
            found += self._plan_obligations()
            found += self._subject_obligations()
            found += self._challenge_obligations()
            found += self._disagreement_obligations()
            found += self._spec_and_invariant_obligations()
            for transformation, task in sorted(self.s.submissions.items()):
                if task not in self.s.integrated:
                    found.append(make("REVIEW", {"transformation": transformation}, holder=REVIEWER))
            for item in self.items.all:
                found.append(item.obligation)
                found.extend(item.route.decisions)
                for part in item.parts:
                    found.append(part.obligation)
                    found.extend(part.route.decisions)
            found += self.items.orphan_decisions
            from .reports import Reports

            found += Reports(self).identities()  # review 879fa490 N1
            self.__dict__["_binding_index"] = {o.id: o for o in found}
        return self.__dict__["_binding_index"]

    def covers_outputs(self, review: str, transformation: str) -> bool:
        """A judgment about work carries a content entry on every unit of its judged content (§4.3, §5.10 (b)):
        each unit ``X`` changed, at its output revision (step 4 review B13; Admission's §8.3 minimum in Phase F)."""

        from .frames import frame_of, transformation_of

        x = transformation_of(self.s, transformation)
        if x is None:
            return False
        frame = frame_of(self.s, x)
        entries = {(e["target"].get("unit"), e["target"].get("rev")) for e in self.s.record(review)["basis"]
                   if e["mode"] == "content"}
        return all((unit, frame.candidate_rev(unit)) in entries for unit in frame.changed)

    def submitting_result(self, transformation: str) -> str | None:
        """The task result that first submitted ``X`` (§7.1)."""

        for rid in self.s.of_kind("TASK_RESULT"):
            target = self.s.record(rid)["target"]
            if target.get("transformation") == transformation and submits(target):
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
            if o.kind not in ("ACCEPT", "GATE", "PLAN_ACCEPT") or self.discharge(o) in (DISCHARGED, DISCHARGED_PROVISIONAL, REFUSED):
                continue
            # A passing, independent judgment that was current when admitted and is no longer (§10.2); an adverse
            # judgment's currency is irrelevant (§5.10 (d)) and a non-independent one supports nothing (§5.10 (f)).
            candidates = [r for r in self._answers(o) if self.d.passing(r) and not self.d.j.nonind(r) and self._was_current(r)]
            if o.kind == "GATE":
                members = candidates
            else:
                members = candidates if not any(self.d.current(r) > F for r in candidates) else []
            for x in members:
                if self.d.current(x) == F and not self.s.superseded(x) and not self.d.j.vetoed(x):
                    holder = HUMAN if self.s.record(x)["actor_class"] == "HUMAN" else REVIEWER
                    out.append(make("REVALIDATE", {"record": x}, {"for": o.id}, holder=holder))
        return out

    def _was_current(self, rid: str) -> bool:
        from .state import State
        from .support import Support

        position = self.s.position_of(rid)
        if position == self.s.n and self.s.frame is None:
            return self.d.current(rid) > F
        return Support(State(self.s.h, position)).current(rid) > F

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
        if o.kind == "REVIEW" and "integrated" in target:
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
            in_frame = o.kind == "REVIEW" and "transformation" in o.target and \
                self.s.record(rid)["frame"] == {"transformation": o.target["transformation"]}
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

        target = o.target if isinstance(o.target, dict) else {}
        items = tuple(e["unit"] for e in target.get("items", ())) + ((target["item"],) if "item" in target else ())
        return self.provisional_scope(o.kind, (subject,) if subject else (), items)

    def provisional_scope(self, kind: str, subjects: tuple[str, ...], items: tuple[str, ...]) -> bool:
        """Whether ``kind`` may continue provisionally for these subjects and items (§10.3, §10.5): every one of
        them inside one in-force override's declared scope that lists the kind, or the kind permitted by policy."""

        if kind in NEVER_PROVISIONAL:
            return False
        if kind in self.s.policy.flow("provisional_kinds"):
            return True
        wanted = [(s, "subjects") for s in subjects] + [(i, "items") for i in items]
        if not wanted:
            return False
        for rid in self.s.of_kind("RISK_OVERRIDE"):
            scope = self.s.record(rid)["fields"]["continuation"]
            if not self.s.in_force(rid) or not isinstance(scope, dict) or kind not in scope.get("kinds", ()):
                continue
            if all(name in scope.get(field, ()) for name, field in wanted):
                return True
        return False

    def _subject_of(self, o: Obligation) -> str | None:
        target = o.target
        if o.kind in ("ACCEPT", "SPEC_REVIEW"):
            return target["subject"]
        if o.kind == "GATE":
            return target["subject"]["subject"]
        return None

    def _support_for(self, o: Obligation) -> Any:
        if o.kind == "REVIEW" and "transformation" in o.target:
            return self._frame_support(o.target["transformation"])
        return self.d

    def _qualifies(self, o: Obligation, rid: str) -> bool:
        """A passing judgment that may discharge ``o``: by an actor qualified for its kind, independent where
        the kind requires it (§10.4)."""

        record = self.s.record(rid)
        if PASSING.get(record["kind"]) != record["outcome"]:
            return False
        subject = self._subject_of(o)
        domain = self.s.view.structure.domain(subject) if subject else self.domain_of(o)
        if not self.d.qualified(record, domain):
            return False
        if o.kind == "REVIEW" and "transformation" in o.target and not self.covers_outputs(rid, o.target["transformation"]):
            return False
        return not (o.kind in INDEPENDENT and self.d.j.nonind(rid))

    def discharge(self, o: Obligation) -> str:
        """§10.4: discharged iff some current, qualified, independent passing judgment of the kind on the exact
        target (in its run) satisfies the predicate, whatever the order of admission; ``REFUSED`` when it is
        answered and a standing, unrelieved adverse judgment of its kind is in its reach; otherwise ``OPEN``."""

        if o.kind in ITEM_KINDS:
            item = self.items.of(o.id)
            return item.discharge() if item is not None else OPEN
        if o.kind not in ANSWER_KIND:
            return OPEN
        support = self._support_for(o)
        subject = self._subject_of(o)
        candidates = [r for r in self._answers(o) if self._qualifies(o, r)]
        value = max((support.current(r) for r in candidates), default=F) if support is not None else F
        if o.kind == "GATE":
            value = self.d.gterm(subject, o.target["gate"], self._value)
        elif subject is not None and o.kind == "ACCEPT" and value > F:
            status = self.s.status1(triple_key(*self.s.subject_triple(subject)))
            if status in ("REVOKED", "BLOCKED"):
                return OPEN
            if status == "PROVISIONAL":
                value = min(value, P)
            domain = self.s.view.structure.domain(subject)
            for obligation in self.s.evidence.required(subject):
                value = min(value, self.d.a.ev(subject, obligation, self._value, self.d.base, self.d.j.nonind))
            value = min(value, self.d.a.qual(subject, self._value, self.d.base, self.d.j.nonind))
        if value == T:
            return DISCHARGED
        if value == P and self.provisional_allowed(o, subject):
            return DISCHARGED_PROVISIONAL
        if self.answer(o) is not None and any(
                ADVERSE.get(self.s.record(r)["kind"]) == self.s.record(r)["outcome"] and self.d.j.stands_adverse(r)
                for r in self._answers(o)):
            return REFUSED
        return OPEN

    # -- readiness (§10.3) ----------------------------------------------------------------------

    def readiness(self, o: Obligation) -> Readiness:
        if o.kind in ITEM_KINDS:
            item = self.items.of(o.id)
            return item.readiness() if item is not None else Readiness(WAITING, ("not derived",))
        if o.kind in ANSWER_KIND and self.answer(o) is not None:
            return Readiness(ANSWERED)
        waiting: list[str] = []
        if o.kind == "REALIZE":  # no designated runner of the specification's class: nothing can realize it (F95)
            from ssds.content import SpecDeclaration

            declared = self.s.specs.declaration(o.params["spec"]["unit"])
            if not isinstance(declared, SpecDeclaration) or declared.runner not in self.s.policy.runners:
                waiting.append("no designated runner of the specification's class")
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
        if o.kind in JUDGED and not self.eligible_judges(o):
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
        if o.kind == "REVIEW" and "integrated" in target:
            item = next((i for i in self.items.all if i.key == target["of"]), None)
            authors: set[str] = set()
            for part in item.parts if item is not None else ():
                for unit, rev in part.outputs.items():
                    authors |= self.s.authors(unit, rev)
            return frozenset(authors) or frozenset({UNKNOWN})
        if o.kind == "REVIEW":
            return self.d.j.transformation_authors(target["transformation"])  # the one rule (plan review 6e0fa9e NB-1)
        if o.kind in ("ADJUDICATE", "ADJUDICATE_DISAGREEMENT", "REVALIDATE"):
            return self.d.j.root_authors(target["record"]) if target["record"] in self.s.records else frozenset({UNKNOWN})
        if o.kind in ("ASSESS", "READING"):  # the claim's authors and the realization's lineage (§10.3, §6.9)
            real = target.get("realization") or o.params.get("observation")
            if real not in self.s.records:
                return frozenset({UNKNOWN})
            record = self.s.record(real)
            out = {record["actor"]}
            for claim in record["target"].get("claim") or []:
                if isinstance(claim, dict) and claim.get("unit") in self.s.view.structure.units:
                    out |= self.s.authors(claim["unit"], claim["rev"])
            if o.kind == "READING" and target["record"] in self.s.records:
                out |= self.d.j.root_authors(target["record"])
            return frozenset(out)
        return frozenset({UNKNOWN})

    # -- what the renderers read (Phase E step 7) --------------------------------------------------------

    @cached_property
    def briefing(self) -> Any:
        """What a brief of an obligation projects (``derivation.briefing``)."""

        from .briefing import Briefing

        return Briefing(self)

    def contract_revision(self, o: Obligation) -> dict[str, str]:
        """The contract a task for ``o`` binds (§12.2; SD-77; Phase F reading F66): an item's ``{unit, rev}`` at this
        state, or the system contract id ``{system: <obligation kind>, version: <system version in force>}``, that
        kind's entry in the system version's table (§13.6) under the ruleset in force here."""

        item = self.item_of(o)
        if item is not None:
            return {"unit": item.unit, "rev": self.s.view.rev(item.unit)}
        return {"system": o.kind, "version": self.s.h.ruleset(self.s.n)["system"]}

    def serialization(self, o: Obligation) -> tuple[tuple[str, ...], str | None]:
        """What a task for ``o`` serializes on (§9.2; Phase F step 8c, reading F67): the policy's serialization
        surfaces its write scope meets, a unit meeting a surface when one contains the other; and, for a principal's
        coordination task, its plan, since every change plan is a surface for coordination."""

        coordination = o.plan if o.holder == PRINCIPAL else None
        item = self.item_of(o)
        if item is None:
            return (), coordination
        structure = self.s.view.structure
        surfaces = [u for u in self.s.policy.flow("serialization_surfaces") if u in structure.units]
        writes = item.write_units
        met = sorted({s for s in surfaces for w in writes
                      if w == s or s in structure.ancestors(w) or w in structure.ancestors(s)})
        return tuple(met), coordination

    def item_of(self, o: Obligation) -> Any:
        """The item or part obligation ``o`` is, or None."""

        return self.items.of(o.id) if o.kind in ITEM_KINDS else None

    def at(self, position: int) -> "Workflow":
        """The workflow of the same ledger at an earlier position (a historical view)."""

        return Workflow.historical(self.s.h, position)

    @staticmethod
    def historical(history: Any, position: int) -> "Workflow":
        """The workflow of a ledger at a position, built once per history and shared by every consumer: a
        derivation is a function of its prefix (§5), so each position is derived once (PERF-E1; Phase F
        reading F7)."""

        from .state import State
        from .support import Support

        cache = history.__dict__.setdefault("_workflows_at", {})
        found = cache.get(position)
        if found is None:
            found = cache[position] = Workflow(Support(State(history, position)))
        return found

    def challenges_on(self, subject: str) -> list[str]:
        """The challenge records on the subject's current triple."""

        if subject not in self.s.view.structure.units:
            return []
        key = triple_key(*self.s.subject_triple(subject))
        return [c for c in self.s.targeting.get(key, []) if self.s.record(c)["kind"] == "CHALLENGE"]

    def standing_adverse(self) -> list[str]:
        """Every standing adverse judgment, in admission order (§5.10 (c))."""

        out = []
        for rid, fact in sorted(self.s.records.items(), key=lambda kv: (kv[1].position, kv[0])):
            record = fact.record
            if ADVERSE.get(record["kind"]) == record["outcome"] and self.d.j.stands_adverse(rid):
                out.append(rid)
        return out

    def subject_of(self, o: Obligation) -> str | None:
        """The subject an obligation is about, for its version binding and briefs (§16.9): a judgment's subject,
        else the subject of the plan an item or decision belongs to, else none (a system obligation)."""

        subject = self._subject_of(o) or (o.target.get("subject") if o.kind == REVISING_REVIEW else None)
        return subject if subject is not None else o.plan

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
        real = o.target.get("realization") if isinstance(o.target, dict) else None
        if real in self.s.records:  # ASSESS: the claim's domain (§10.3)
            claims = [c["unit"] for c in self.s.record(real)["target"].get("claim") or [] if isinstance(c, dict)]
            units = self.s.view.structure.units
            return next((self.s.view.structure.domain(u) for u in claims if u in units), None)
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
            if self.d.j.chain_needs_human(o.target["record"]):
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
            o.kind == "READING" and o.params.get("class") == "R3") or (
            revalidated is not None and (revalidated["actor_class"] == "HUMAN" and domain in ("D1", "D2")
                                         or revalidated["kind"] in ("GATE_DECISION",)))
        acceptors = policy.get(domain, "acceptors", None)
        agents_allowed = not human_only and (o.kind != "ACCEPT" or acceptors is None or "class:AGENT" in acceptors)
        if agents_allowed and UNKNOWN not in authors:
            out.append("agent:fresh-reviewer")
        return tuple(out)
