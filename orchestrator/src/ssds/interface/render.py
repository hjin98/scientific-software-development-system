"""Deterministic renderers: task, review, gate and decision briefs, and the inspector view (Manual §16.3-§16.9, §29).

Every brief is a pure projection of one derived state (a ``derivation.Workflow`` at the presented head), the
obligation it is for, the head it names and the doctrine text the governing version pins; no model translates
machine state. A brief's sections follow the Manual's order for its form, and the duties it carries are compiled
from the obligation's role, domain, kind, required slots and the derived injection events of §16.3, never
selected by wording (A4): a duty whose event does not fire is not carried.

Version binding (§16.9): a ``NATIVE`` subject's brief states the ruleset in force and the doctrine pin it names
(SSDP version and immutable public-source commit), and its domain core and injected owner text are read there;
with no pin, or a source that cannot be read, the text is not rendered and an incompleteness notice says so. A
``LEGACY(p)`` subject's brief is rendered through ``p``'s frozen Core profile, which this renderer names and
does not reproduce. In Phase E nothing is issued: every brief is labeled ``NOT ISSUED`` (reading E1).

This module is the public renderer the Dispatcher will import (Phase F).
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from ssds import derivation
from ssds.core.api.v1 import profile_for_protocol

#: Reads one file of the doctrine source: (public-source commit, repository path) -> bytes, or None.
Doctrine = Callable[[str, str], "bytes | None"]

NOT_ISSUED = "NOT ISSUED (Phase E: no task, envelope, route or lineage; reads not recorded)"
REFERENCES = "source/shared/references/"
DOMAIN_ENTRYPOINT = {"D1": "source/roles/scientific-formulation/SKILL.md",
                     "D2": "source/roles/numerical-algorithm-design/SKILL.md",
                     "D3": "source/roles/software-design/SKILL.md",
                     "D4": "source/roles/software-implementation/SKILL.md"}
SPECIALIST_ENTRYPOINT = {"DOCUMENT": "source/specialists/software-documentation/SKILL.md",
                         "MAINTENANCE_AUDIT": "source/specialists/software-maintenance-audit/SKILL.md",
                         "REPOSITORY_HYGIENE": "source/specialists/repository-hygiene/SKILL.md"}
DOMAIN_OWNER = {"D1": "scientific-formulation.md", "D2": "numerical-algorithm-design.md",
                "D3": "architecture-and-design.md", "D4": "specification-and-implementation.md"}
CONCERN_OWNER = {"security": "security-and-trust-boundaries.md", "storage": "storage-and-io.md",
                 "concurrency": "concurrency-and-orchestration.md", "performance": "performance-and-parallelism.md",
                 "configuration": "configuration-and-policy.md", "release": "release-and-distribution.md"}
#: §16.3's injection events and the owner text each injects (paths under the doctrine source's references).
OWNER = {"evidence": "evidence-evolution-and-dependencies.md", "definition": "semantic-definition-and-traceability.md",
         "convergence": "convergence-and-cycle-economy.md", "pem": "project-engineering-memory.md",
         "channel-c": "workflow-and-workplans.md", "inspectability": "scientific-inspectability-and-initiative.md",
         "revising": "scientific-inspectability-and-initiative.md", "kernel-challenge": "abstraction-and-concretization.md",
         "versioning": "protocol-versioning-and-compatibility.md"}

#: §12.3's role templates: what the role holds, may write and submit, and may not.
ROLE_CORE = {
    "PRINCIPAL": ("holds COORDINATE and CONTRACT; may write its plan's units and submit its TASK_RESULT, coordination "
                  "decisions, materiality reclassifications, reports and challenges; may not write product, authority or "
                  "evidence units, submit review, conformance, acceptance, plan-acceptance or human judgments, keep its "
                  "own amendment covered, or change verification rules"),
    "IMPLEMENTER": ("holds the implementer item kinds and REVALIDATE of its own result; may write its contract's write "
                    "scope and named evidence specifications and submit its TASK_RESULT (COMPLETE, PARTIAL, BLOCKED, "
                    "INFEASIBLE), reports and challenges; may not edit plans, contracts, other evidence specifications, "
                    "verification rules or protected surfaces, or judge its own work"),
    "REVIEWER": ("holds review, acceptance, plan acceptance, assessment, reading, adjudication, specification and "
                 "integrated-result reviews and their revalidation; submits records only: its judgments, TASK_RESULT, "
                 "reports and challenges; may not write content, judge work or a contract its own execution or lineage "
                 "authored, or receive the author's narrative or conclusions"),
    "INVESTIGATOR": ("holds INVESTIGATE and intake classification; may write scratch workspaces and named finding "
                     "homes and submit findings, classifications, reconstruction proposals and proposed relations; may "
                     "not write product or authority units or submit acceptance"),
    "HUMAN": "holds GATE, HUMAN_ATTENTION and every R3 decision; an authenticated human judgment is recorded as such",
}
#: Kind duties (§16.3): what a judgment of the kind owes beyond its role.
KIND_DUTIES = {
    "review": ("Challenge Pass: reconstruct the parent semantics and accepted authority independently of the author's "
               "rationale, attempt falsification of conformance, adequacy, ownership, affected surfaces, testing and "
               "impact closure, and lead with any Serious Challenge before ordinary findings"),
    "out-of-matrix": ("out-of-matrix pass: judge whether the authority under review is itself adequate for the outcome "
                      "it protects, not only whether the work complies with it"),
}
#: Slot duties (§13.5, §29.4): each owed question, inline, as its typed slot.
SLOT_DUTIES = {
    "claims": "claims: each factual claim with the records establishing it",
    "unverified_assumptions": "unverified_assumptions: every assumption the work relies on and did not verify, or NONE with a reason",
    "deviations": "deviations: every deviation from the contract, or NONE with a reason",
    "findings": "findings: your material findings, including delegates' and out-of-scope ones, or NONE with a reason",
    "null_envelope": ("null_envelope: if the work produced, ran or reviewed realized results or prepared gate evidence, "
                      "what you examined and what material areas you did not, with the materiality basis"),
    "variant_search": ("variant_search: if more than one analysis, pipeline, preprocessing, model or parameter variant "
                       "was evaluated, count and kind, selection criterion and data, and lineage"),
    "tension_search": ("tension_search: before relying on accepted D1/D2 authority for a consequential judgment, what you "
                       "searched for recorded tensions, what you could not reach, and each tension with its entries, "
                       "binding and asserter"),
    "choices": "choices: each consequential choice with its effective value, origin, chooser and binding",
    "retention": "retention: what the change retains, projects and omits of the realized record",
    "delegate_returns": "delegate_returns: each delegate's answers to the findings, results, variant and tension questions",
    "bidirectional": ("bidirectional: whether the work is faithful to its authority and whether the authority is "
                      "adequate for the work"),
    "o1_content": "o1_content: the authority content the revision states, or NONE with a reason",
    "revision_assessments": ("revision_assessments: the predecessor identity and the revision-scoped tension "
                             "assessments, with asserters, proposed until accepted"),
    "audit_conclusion": "audit_conclusion: HEALTHY, WATCH or ACTION REQUIRED, with per-finding scope and expected improvement",
}
REVIEW_KINDS = frozenset({"REVIEW", "ACCEPT", "PLAN_ACCEPT", "SPEC_REVIEW", "JOINT_INVARIANT", "REVIEW_REVISION",
                          "ADJUDICATE", "ADJUDICATE_DISAGREEMENT", "REVALIDATE"})
JUDGMENT_OUTCOMES = {"REVIEW": "PASS, NO_PASS", "ACCEPT": "PASS, NO_PASS", "PLAN_ACCEPT": "ACCEPTED, REJECTED",
                     "SPEC_REVIEW": "PASS, NO_PASS", "JOINT_INVARIANT": "PASS, NO_PASS",
                     "REVIEW_REVISION": "PASS, NO_PASS", "ADJUDICATE": "UPHELD, DISMISSED",
                     "ADJUDICATE_DISAGREEMENT": "UPHELD, DISMISSED", "REVALIDATE": "PASS, NO_PASS"}
TASK_OUTCOMES = "COMPLETE, PARTIAL, BLOCKED, INFEASIBLE"


def _json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False)


@dataclass(frozen=True)
class Brief:
    """One rendered brief: its form, the obligation, the version it is bound to, the duties compiled into it and
    its sections in the Manual's order."""

    form: str  # TASK | REVIEW | GATE | DECISION | ATTENTION | LEGACY
    obligation: str
    governs: dict[str, Any]
    duties: tuple[str, ...]
    sections: tuple[tuple[str, str], ...]

    @property
    def text(self) -> str:
        parts = [f"# {self.form} brief {self.obligation}", ""]
        for title, body in self.sections:
            parts += [f"## {title}", "", body.rstrip(), ""]
        return "\n".join(parts)

    @property
    def digest(self) -> str:
        """The brief's content identity, as an issued envelope records it (§16.4)."""

        return "sha256:" + hashlib.sha256(self.text.encode("utf-8")).hexdigest()

    def to_json(self) -> dict[str, Any]:
        return {"form": self.form, "obligation": self.obligation, "governs": self.governs, "duties": list(self.duties),
                "sections": [{"title": t, "text": b} for t, b in self.sections], "digest": self.digest, "text": self.text}


class Renderer:
    """Briefs and the inspector view over one presented state."""

    def __init__(self, workflow: Any, head: dict[str, Any], doctrine: Doctrine) -> None:
        self.w = workflow
        self.s = workflow.s
        self.d = workflow.d
        self.head = head
        self.read_doctrine = doctrine

    # -- version binding (§16.9) ----------------------------------------------------------------------

    def governs(self, o: Any) -> dict[str, Any]:
        subject = self.w.subject_of(o)
        mode = self.s.h.mode(self.s.n, subject) if subject is not None else {"mode": "NATIVE"}
        if mode.get("mode") == "LEGACY":
            protocol = mode.get("protocol")
            return {"mode": "LEGACY", "protocol": protocol, "profile": profile_for_protocol(protocol) if protocol else None}
        if mode.get("mode") == "UNGOVERNED":
            return {"mode": "UNGOVERNED"}
        ruleset = self.s.h.ruleset(self.s.n)
        out: dict[str, Any] = {"mode": "NATIVE", "ruleset": ruleset["system"]}
        if "doctrine" in ruleset:
            out["doctrine"] = dict(ruleset["doctrine"])
        return out

    def _doctrine_text(self, governs: dict[str, Any], path: str) -> str | None:
        pin = governs.get("doctrine")
        if pin is None:
            return None
        data = self.read_doctrine(pin["source"], path)
        return data.decode("utf-8", "replace") if data is not None else None

    def _version_section(self, governs: dict[str, Any]) -> str:
        if governs["mode"] == "LEGACY":
            return (f"LEGACY({governs['protocol']}): rendered through the frozen Core profile "
                    f"{governs['profile'] or 'UNAVAILABLE'}; SSDS compiles no native duties for this subject")
        if governs["mode"] == "UNGOVERNED":
            return "UNGOVERNED: no protocol governs this subject; SSDS renders its derived facts only"
        pin = governs.get("doctrine")
        doctrine = f"SSDP {pin['version']} at {pin['source']}" if pin else "no doctrine pinned (no doctrine text rendered)"
        return f"NATIVE: ruleset {governs['ruleset']}; doctrine {doctrine}"

    def _header(self, o: Any, form: str, governs: dict[str, Any]) -> str:
        head = self.head
        return "\n".join([
            f"Governing version: {self._version_section(governs)}",
            f"Status: {NOT_ISSUED}",
            f"Obligation: {o.kind} {o.id}",
            f"Target: {o.target_json}",
            f"Holder: {o.holder}" + (f"; plan {o.plan}" if o.plan else ""),
            f"Qualified head: {head.get('label')} position {head.get('position')} {head.get('digest')}",
        ])

    # -- duty compilation (§16.3) ------------------------------------------------------------------------

    def events(self, o: Any) -> list[tuple[str, str]]:
        """The injection events that fire for ``o``: (event, owner reference path)."""

        kind, s = o.kind, self.s
        item = self.w.item_of(o)
        subject = self.w.subject_of(o)
        domain = self.w.domain_of(o) if item is None else (item.item.authority or "D4")
        out: list[tuple[str, str]] = []
        judged = kind in ("ACCEPT", "REVIEW") or (item is not None and item.item.kind == "AUTHOR")
        if judged and domain in DOMAIN_OWNER:
            out.append((f"domain:{domain}", REFERENCES + DOMAIN_OWNER[domain]))
        if kind in ("ASSESS", "READING", "ADJUDICATE_DISAGREEMENT", "SPEC_REVIEW"):
            out.append(("evidence", REFERENCES + OWNER["evidence"]))
        if subject is not None and self._declares_definitions(subject):
            out.append(("definition", REFERENCES + OWNER["definition"]))
        recurrence = kind == "COORDINATE" and "recurrence" in o.target
        budget = (item is not None and item.budget_spent) or o.target.get("condition") == "budget-spent"
        if recurrence or budget:
            out.append(("convergence", REFERENCES + OWNER["convergence"]))
        if recurrence or (item is not None and item.item.kind == "MIGRATE"):
            out.append(("pem", REFERENCES + OWNER["pem"]))
        scientific = self._scientific(o, item)
        if kind == "GATE" or (kind in REVIEW_KINDS and scientific):
            out.append(("channel-c", REFERENCES + OWNER["channel-c"]))
            out.append(("inspectability", REFERENCES + OWNER["inspectability"]))
        revising = kind == "REVIEW_REVISION" or (item is not None and item.item.kind == "AUTHOR"
                                                 and item.item.authority in ("D1", "D2"))
        if revising:
            out.append(("revising", REFERENCES + OWNER["revising"]))
        if self._serious_challenge(o, subject):
            out.append(("kernel-challenge", REFERENCES + OWNER["kernel-challenge"]))
        if subject is not None and s.mode(subject) == "LEGACY":
            out.append(("versioning", REFERENCES + OWNER["versioning"]))
        if item is not None and item.item.contract is not None:
            written = item.write_units
            for concern, units in sorted(s.policy.flow("concern_tags").items()):
                if written & set(units):
                    out.append((f"concern:{concern}", REFERENCES + CONCERN_OWNER[concern]))
        return out

    def _declares_definitions(self, subject: str) -> bool:
        """The subject or its governing closure declares a definition, a parameter family or an external import:
        a ``USES_DEFINITION`` relation from it, or an ``EXTERNAL`` unit among what governs it."""

        structure = self.s.view.structure
        units = {u for u in structure.units if structure.subj(u) == subject}
        governing = {g["unit"] for g in derivation.queries.governs(self.w, subject)}
        for r in self.s.s0.relations:
            if r.type == "USES_DEFINITION" and r.subject in units | governing:
                return True
        return any(structure.kind(u) == "EXTERNAL" for u in governing if u in structure.units)

    def _scientific(self, o: Any, item: Any) -> bool:
        if item is not None:
            return item.item.contract is not None and item.item.contract.scientific == "APPLIES"
        x = o.target.get("transformation") if isinstance(o.target, dict) else None
        result = self.w.submitting_result(x) if x else None
        contract = self.w.conformance(result).contract[0] if result else None
        return contract is not None and contract.scientific == "APPLIES"

    def _serious_challenge(self, o: Any, subject: str | None) -> bool:
        if o.kind == "ADJUDICATE" and o.target.get("record") in self.s.records:
            return bool(self.s.record(o.target["record"])["fields"].get("serious"))
        if subject is None:
            return False
        return any(self.s.record(c)["fields"].get("serious") for c in self.w.challenges_on(subject))

    def duties(self, o: Any, governs: dict[str, Any], slots: list[str]) -> tuple[list[str], list[tuple[str, str]], list[str]]:
        """(compiled duty identifiers, their rendered texts, incompleteness notices) for ``o`` (§16.3)."""

        ids: list[str] = []
        texts: list[tuple[str, str]] = []
        notices: list[str] = []
        item = self.w.item_of(o)
        role = o.holder if o.holder in ROLE_CORE else "REVIEWER"
        ids.append(f"role:{role}")
        texts.append((f"Role core ({role}, §12.3)", ROLE_CORE[role]))
        domain = self.w.domain_of(o) if item is None else (item.item.authority or "D4")
        entry = None
        if item is not None and item.item.kind == "DOCUMENT":
            entry = ("specialist:DOCUMENT", SPECIALIST_ENTRYPOINT["DOCUMENT"])
        elif item is not None and item.item.specialist:
            entry = (f"specialist:{item.item.specialist}", SPECIALIST_ENTRYPOINT[item.item.specialist])
        elif domain in DOMAIN_ENTRYPOINT:
            entry = (f"domain:{domain}", DOMAIN_ENTRYPOINT[domain])
        if entry is not None:
            ids.append(f"core:{entry[0]}")
            text = self._doctrine_text(governs, entry[1])
            if text is None:
                notices.append(f"domain core {entry[1]} not rendered: {self._why_no_doctrine(governs)}")
                text = f"(not rendered: {entry[1]})"
            texts.append((f"Domain core ({entry[0]}: {entry[1]})", text))
        if o.kind in REVIEW_KINDS:
            ids.append("kind:review")
            texts.append(("Kind duty: Challenge Pass", KIND_DUTIES["review"]))
            if o.kind in ("ACCEPT", "REVIEW_REVISION") and domain in ("D1", "D2", "D3"):
                ids.append("kind:out-of-matrix")
                texts.append(("Kind duty: out-of-matrix pass", KIND_DUTIES["out-of-matrix"]))
        for slot in slots:
            ids.append(f"slot:{slot}")
        for event, path in self.events(o):
            ids.append(f"inject:{event}")
            text = self._doctrine_text(governs, path)
            if text is None:
                notices.append(f"injected owner {path} not rendered: {self._why_no_doctrine(governs)}")
                text = f"(not rendered: {path})"
            texts.append((f"Injected owner ({event}: {path})", text))
        return ids, texts, notices

    def _why_no_doctrine(self, governs: dict[str, Any]) -> str:
        return "the ruleset pins no doctrine" if "doctrine" not in governs else "the pinned doctrine source cannot be read"

    # -- shared projections --------------------------------------------------------------------------------

    def _unit_text(self, unit: str) -> str:
        view = self.s.view
        region = view.regions.get(unit) if unit in view.structure.units else None
        if not region:
            return f"({unit}: no content at this head)"
        return b"".join(view.tree[sp.path].data[sp.start:sp.end] for sp in region).decode("utf-8", "replace")

    def _governing_inline(self, units: list[tuple[str, str | None]]) -> str:
        if not units:
            return "none"
        out = []
        for unit, rev in units:
            current = self.s.cur(unit) if unit in self.s.view.structure.units else None
            note = "" if rev is None or rev == current else f" (named {rev}; the current revision is {current})"
            out.append(f"### {unit} @ {current}{note}\n\n{self._unit_text(unit)}")
        return "\n\n".join(out)

    def _incompleteness(self, subject: str | None, extra: list[str]) -> str:
        notices = list(extra)
        if subject is not None and subject in self.s.view.structure.units:
            if subject in self.s.s0.affected_subjects:
                notices.append(f"{subject} carries quarantined structure")
            for r in self.d.acceptances(subject):
                if not self.s.cont(r):
                    notices.append(f"acceptance {r} is withheld by a loss boundary")
            for cls in ("WARRANT", "GOVERNING"):
                widening = derivation.queries.depends(self.w, subject, cls)["widening"]
                if widening != "EXACT":
                    notices.append(f"{cls} prerequisites of {subject}: {widening}")
        notices.append("reads not observed (Phase E: no harness route)")
        notices.append(f"qualified head: {self.head.get('label')} at position {self.head.get('position')}")
        return "\n".join(f"- {n}" for n in notices)

    def _open_states(self, subject: str | None) -> str:
        if subject is None or subject not in self.s.view.structure.units:
            return "none"
        blocked = derivation.queries.blocked(self.w, subject)
        lines = [f"status: {blocked['status']}"] + [f"- {r}" for r in blocked["reasons"]]
        return "\n".join(lines)

    # -- task brief (§16.3) ------------------------------------------------------------------------------------

    def task(self, o: Any) -> Brief:
        governs = self.governs(o)
        if governs["mode"] == "LEGACY":
            return self._legacy(o, governs)
        item = self.w.item_of(o)
        if item is None:
            return self._generic(o, governs)
        it = item.item
        contract = it.contract
        slots = item.required_slots
        ids, duty_texts, notices = self.duties(o, governs, slots)
        plan = self.s.plans.plans.get(item.plan)
        objective = self._unit_text(plan.objective) if plan is not None and plan.objective else "(no objective)"
        prose = self.s.plans.prose(item.part).decode("utf-8", "replace")
        role_section = "\n\n".join([f"Objective of plan {item.plan}:\n\n{objective.strip()}",
                                    f"Item {it.id} ({it.kind}), workflow role {o.holder}:\n\n{prose.strip()}"]
                                   + [f"### {t}\n\n{b.strip()}" for t, b in duty_texts])
        boundaries = "\n".join([
            f"write_scope: {_json(list(contract.write_scope))}", f"frozen interface: {_json(list(contract.frozen))}",
            f"dependencies: {_json([[k, list(v)] for k, v in contract.dependencies])}",
            f"evidence specifications: {_json(list(contract.evidence_specs))}", f"homes: {_json(list(contract.homes))}",
            f"artifacts: {_json(list(contract.artifacts))}", f"scientific: {contract.scientific}",
            "delegated space: everything inside the write scope the obligations leave open"]) if contract else "no contract yet"
        obligations = []
        for ob in (contract.obligations if contract else ()):
            obligations.append(f"- {ob.id}: verifier {ob.verifier!r}; statement #{ob.statement.name}; secondary "
                               f"{_json([c.template for c in ob.secondary])}")
        obligations += [f"- acceptance criterion {c}: {e}" for c, e in it.acceptance_criteria]
        obligations += [f"- required evidence: {e}" for e in (contract.evidence if contract else ())]
        obligations += ["", "Required slots (each owed question, as its typed slot):"]
        obligations += [f"- {SLOT_DUTIES.get(slot, slot)}" for slot in slots]
        previous = self._previous_iteration(item)
        open_states = self._open_states(self.w.subject_of(o))
        if previous:
            open_states += "\n\nPrevious iteration (data, never its narrative):\n" + previous
        if item.route.route.startswith(("re-dispatch",)) and item.moved:
            open_states += "\n\nDrift: outputs moved since the latest integration: " + _json(item.outputs)
        escalation = "\n".join([
            f"budget: {item.iterations} of {item.budget} iterations used",
            "escalation triggers: a BLOCKER, AMENDMENT_REQUEST, FINDING or CHALLENGE report; budget exhaustion, "
            "out-of-scope findings and discrepancies go to the principal",
            "workspace and submission: none (NOT ISSUED; the Dispatcher issues tasks in Phase F)"])
        sections = (
            ("Header", self._header(o, "TASK", governs)),
            ("1. Objective, obligation kind and workflow role", role_section),
            ("2. Allowed outcomes", TASK_OUTCOMES),
            ("3. Governing content", self._governing_inline([(u, r) for u, r in it.governing])),
            ("4. Contract boundaries, constraints, non-goals and delegated space", boundaries),
            ("5. Obligations, criteria, required evidence and slots", "\n".join(obligations)),
            ("6. Open challenges, findings and provisional states", open_states),
            ("7. Incompleteness notices", self._incompleteness(self.w.subject_of(o), notices)),
            ("8. Governing version", self._version_section(governs)),
            ("9. Escalation triggers, budget, workspace and submission", escalation),
        )
        return Brief("TASK", o.id, governs, tuple(ids), sections)

    def _previous_iteration(self, item: Any) -> str:
        if not item.enactments:
            return ""
        last = item.enactments[-1]
        view = self.w.conformance(last.result).view()
        lines = [f"iteration {item.iterations}: conformance {_json(sorted(self.w.conformance(last.result).classes))}"]
        lines += [f"- {ob}: {h['template']} {h['class']} {h['finding']}" for ob, hits in sorted(view.items()) for h in hits
                  if h["class"] != "CLEAN"]
        for review in (item.reviews(last.transformation) if last.transformation else []):
            findings = item.items.findings_of(review)
            lines.append(f"- review {review}: {self.s.record(review)['outcome']}; findings {_json(findings)}")
        return "\n".join(lines)

    def _generic(self, o: Any, governs: dict[str, Any]) -> Brief:
        ids, duty_texts, notices = self.duties(o, governs, [])
        subject = self.w.subject_of(o)
        sections = (
            ("Header", self._header(o, "TASK", governs)),
            ("1. Objective, obligation kind and workflow role",
             "\n\n".join([f"{o.kind} {o.detail or o.target_json}"] + [f"### {t}\n\n{b.strip()}" for t, b in duty_texts])),
            ("2. Allowed outcomes", JUDGMENT_OUTCOMES.get(o.kind, TASK_OUTCOMES)),
            ("6. Open challenges, findings and provisional states", self._open_states(subject)),
            ("7. Incompleteness notices", self._incompleteness(subject, notices)),
            ("8. Governing version", self._version_section(governs)),
        )
        return Brief("TASK", o.id, governs, tuple(ids), sections)

    def _legacy(self, o: Any, governs: dict[str, Any]) -> Brief:
        sections = (
            ("Header", self._header(o, "LEGACY", governs)),
            ("Governing version", self._version_section(governs)),
            ("Rendering", f"This obligation's brief is the Core profile {governs['profile'] or 'UNAVAILABLE'}'s stage prompt "
                          f"(`ssds <stage>`), rendered by Core under protocol {governs['protocol']}."),
        )
        return Brief("LEGACY", o.id, governs, ("inject:versioning",), sections)

    # -- review brief (§16.5) -----------------------------------------------------------------------------------

    def review(self, o: Any) -> Brief:
        governs = self.governs(o)
        if governs["mode"] == "LEGACY":
            return self._legacy(o, governs)
        subject = self.w.subject_of(o)
        target = o.target
        x = target.get("transformation") if isinstance(target, dict) else None
        result = self.w.submitting_result(x) if x else None
        conformance = self.w.conformance(result) if result else None
        contract = conformance.contract[0] if conformance is not None else None
        slots = ["claims", "findings"] + (["bidirectional"] if self._scientific(o, None) or (
            subject is not None and self.s.view.structure.kind(subject) in ("D1", "D2")) else [])
        if o.kind == "REVIEW_REVISION":
            slots.append("revision_assessments")
        ids, duty_texts, notices = self.duties(o, governs, slots)
        governing: list[tuple[str, str | None]] = []
        if subject is not None:
            governing = [(g["unit"], g["rev"]) for g in derivation.queries.governs(self.w, subject)]
            if subject in self.s.view.structure.units:
                governing.insert(0, (subject, self.s.cur(subject)))
        candidate = "none (a judgment of standing content)"
        disclosure = "none"
        if result is not None:
            record = self.s.record(result)
            named = (record.get("binding") or {}).get("item")
            if isinstance(named, dict):
                found = self.s.plans.item_at(named["unit"], named["rev"])
                if found is not None:
                    governing += [(u, r) for u, r in getattr(found[1].parsed, "governing", ())]
            files = conformance.changed_files
            candidate = "\n".join(f"- {path}: {'added' if old is None else 'removed' if new is None else 'changed'}"
                                  for path, (old, new) in sorted(files.items())) or "no file changed"
            slot_values = ((record.get("fields") or {}).get("slots") or {})
            # §16.5: the result's disclosure slots, labeled as the author's claims to test; never its outcome,
            # rationale, narrative, commit messages or transcripts
            disclosure = "\n".join(f"- {name} (the author's claim, to test): {_json(slot_values[name])}"
                                   for name in ("deviations", "unverified_assumptions", "claims") if name in slot_values) or "none"
        view = conformance.view() if conformance is not None else {}
        conf = "\n".join(f"- {ob}: {h['template']} {h['class']}" + (" (SIGNAL: a pointer to look, not a finding)"
                                                                     if h["class"] == "SIGNAL" else "")
                         for ob, hits in sorted(view.items()) for h in hits) or "none"
        evidence = "none"
        if subject is not None and subject in self.s.view.structure.units:
            evidence = "\n".join(f"- {_json(e)}" for e in derivation.queries.evidence(self.w, subject)) or "none"
        carried = self._carried_objections(o, subject)
        sections = (
            ("Header", self._header(o, "REVIEW", governs)),
            ("Duties", "\n\n".join(f"### {t}\n\n{b.strip()}" for t, b in duty_texts)
             + "\n\nRequired slots:\n" + "\n".join(f"- {SLOT_DUTIES.get(s_, s_)}" for s_ in slots)),
            ("Allowed outcomes", JUDGMENT_OUTCOMES.get(o.kind, "PASS, NO_PASS")),
            ("Governing content", self._governing_inline(sorted(set(governing)))),
            ("Contract", _json(_contract_json(contract)) if contract is not None else "none"),
            ("Candidate diff and machine-produced facts", candidate),
            ("Conformance view", conf),
            ("Evidence", evidence),
            ("Disclosure slots (the author's claims to test)", disclosure),
            ("Carried objections (another judge's)", carried),
            ("Incompleteness notices", self._incompleteness(subject, notices)),
        )
        return Brief("REVIEW", o.id, governs, tuple(ids), sections)

    def _carried_objections(self, o: Any, subject: str | None) -> str:
        """Every standing adverse judgment whose reach includes the target asked (§16.5; SD-30 to SD-34)."""

        lines = []
        names = set(derivation.queries.lineage(self.w, subject)) if subject is not None else set()
        for rid in self.w.standing_adverse():
            record = self.s.record(rid)
            target = record["target"] if isinstance(record["target"], dict) else {}
            about = target.get("subject") if isinstance(target.get("subject"), str) else (target.get("subject") or {}).get("subject")
            if target == o.target or (about is not None and about in names) or \
                    (target.get("transformation") is not None and target.get("transformation") == o.target.get("transformation")):
                label = "on the target asked" if about == subject or target == o.target else "history: a linked predecessor"
                lines.append(f"- {record['kind']} {rid} by {record['actor']} ({label}): {record['outcome']}")
        return "\n".join(lines) or "none"

    # -- gate brief (§16.6) ---------------------------------------------------------------------------------------

    def gate(self, o: Any) -> Brief:
        governs = self.governs(o)
        if governs["mode"] == "LEGACY":
            return self._legacy(o, governs)
        subject = self.w.subject_of(o)
        ids, duty_texts, notices = self.duties(o, governs, [])
        evidence = derivation.queries.evidence(self.w, subject) if subject is not None else []
        required = [e for e in evidence if e["status"] in ("unavailable", "stale", "disputed") or e.get("outcome") == "PASS"]
        core = "\n".join([
            f"gate: {o.target.get('gate')}; decision asked: GATE_DECISION on {_json(o.target.get('subject'))}",
            f"qualified head: {self.head.get('label')} position {self.head.get('position')} {self.head.get('digest')}",
            "required evidence (supporting premises, or why not holding):",
            *[f"- {e.get('obligation')}: {e['status']}" + (f" via {e['assessment']}" if "assessment" in e else "") for e in required],
            "findings as data (standing adverse judgments, open challenges, quarantine and loss states):",
            self._carried_objections(o, subject), self._open_states(subject),
            "tensions found by the relying search:",
            *[f"- {_json(t)}" for t in (derivation.queries.tensions(self.w, subject) if subject else [])],
            "known missing realized records: none recorded in Phase E (Admission's classification is Phase F's)"])
        earlier = [r for r in self.s.of_kind("GATE_DECISION") if self.s.record(r)["target"].get("gate") == o.target.get("gate")
                   and (self.s.record(r)["target"].get("subject") or {}).get("subject") == subject]
        disclosure = "\n".join(f"- earlier decision {r}: {self.s.record(r)['outcome']} by {self.s.record(r)['actor']}"
                               for r in earlier) or "none recorded"
        revision = "not a D1/D2 revision"
        if subject is not None and self.s.view.structure.kind(subject) in ("D1", "D2"):
            counting = self.w.counting(subject)
            revision = "\n".join(f"- revision-assessment record {r} (proposed until accepted)" for r in counting) \
                or "no counting revision-assessment record: the gate is not ready (§10.2)"
        sections = (
            ("Header", self._header(o, "GATE", governs)),
            ("1. Evidence core", core),
            ("2. Consequential-decision disclosure", disclosure),
            ("3. D1/D2 revision assessments", revision),
            ("4. Interpretation (Channel A)", "none recorded (labeled interpretation, never evidence)"),
            ("5. Allowed outcomes and required fields", "ACCEPT, REJECT; GATE_DECISION requires adequacy and qualification"),
            ("Duties", "\n\n".join(f"### {t}\n\n{b.strip()}" for t, b in duty_texts)),
            ("Incompleteness notices", self._incompleteness(subject, notices)),
        )
        return Brief("GATE", o.id, governs, tuple(ids), sections)

    # -- decision brief (§16.7) -----------------------------------------------------------------------------------

    def decision(self, o: Any) -> Brief:
        governs = self.governs(o)
        ids, duty_texts, notices = self.duties(o, governs, ["claims"])
        plan = self.s.plans.plans.get(o.plan) if o.plan else None
        objective = self._unit_text(plan.objective).strip() if plan is not None and plan.objective else "(no plan)"
        items = [f"- {i.unit} ({i.item.kind}): route {i.route.route}; discharge {i.discharge()}; "
                 f"{i.iterations}/{i.budget} iterations" for i in self.w.items.all if i.plan == o.plan]
        owed = [x for x in self.w.of_kind("COORDINATE") if x.plan == o.plan or x.id == o.id]
        decisions = []
        for x in owed:
            core = x.target
            report = core.get("report") if isinstance(core, dict) else None
            if report in self.s.records:
                record = self.s.record(report)
                decisions.append(f"- {x.id}: report {record['kind']} {report} on {_json(record['target'])} reasons "
                                 f"{_json(record.get('reason') or [])}; allowed "
                                 f"{_json(sorted(derivation.allowed_outcomes(record['kind'], tuple(record.get('reason') or ()))))}")
            else:
                decisions.append(f"- {x.id}: {x.detail or x.target_json}; allowed AMEND, PARTITION, ESCALATE"
                                 + ("; DECLINE" if "recurrence" in core or "refused" in core else ""))
        attention = [f"- {h.id}: {h.target_json} ({h.params.get('materiality')})"
                     for h in self.w.of_kind("HUMAN_ATTENTION") if h.plan == o.plan]
        since = max((self.s.position_of(r) for r in self.s.of_kind("COORDINATION_DECISION")
                     if (self.s.record(r).get("binding") or {}).get("obligation") in {x.id for x in owed}
                     or set((self.s.record(r)["target"] or {}).get("records", [])) & {x.id for x in owed}), default=0)
        changed = derivation.queries.changed(self.w, since)
        sections = (
            ("Header", self._header(o, "DECISION", governs)),
            ("Plan objective and items", objective + "\n\n" + ("\n".join(items) or "no item obligations")),
            ("Decisions owed", "\n".join(decisions) or "none"),
            ("Budgets, recurrences and discrepancies",
             "\n".join(f"- {x.detail}" for x in owed if "recurrence" in x.target or "conformance" in x.target) or "none"),
            ("Open human-attention items of the plan", "\n".join(attention) or "none"),
            ("What changed since the previous coordination",
             "\n".join(f"- position {c['position']}: {_json(c['units'])}" for c in changed) or "nothing"),
            ("Duties", "\n\n".join(f"### {t}\n\n{b.strip()}" for t, b in duty_texts)),
            ("Incompleteness notices", self._incompleteness(None, notices)),
        )
        return Brief("DECISION", o.id, governs, tuple(ids), sections)

    # -- dispatch -------------------------------------------------------------------------------------------------

    def brief(self, o: Any) -> Brief:
        if o.kind == "GATE":
            return self.gate(o)
        if o.kind in ("COORDINATE", "CONTRACT"):
            return self.decision(o)
        if o.kind == "HUMAN_ATTENTION":
            return self.attention_brief(o)
        if o.kind in REVIEW_KINDS:
            return self.review(o)
        return self.task(o)

    # -- the inspector view and digest (§16.8) --------------------------------------------------------------------

    def _waits(self) -> dict[str, set[str]]:
        """Obligation -> the obligations its readiness or discharge waits on (reading E14)."""

        obligations = list(self.w.obligations)
        ids = {o.id for o in obligations}
        waits: dict[str, set[str]] = {o.id: set() for o in obligations}
        for o in obligations:
            for reason in self.w.readiness(o).waiting_on:
                waits[o.id] |= {i for i in ids if i in reason}
            item = self.w.item_of(o)
            if item is not None:
                for dependency in item.item.depends_on:
                    other = self.w.items.by_id(item.plan, dependency)
                    if other is not None:
                        waits[o.id].add(other.obligation.id)
                waits[o.id] |= {d.id for d in item.route.decisions}
            if o.kind == "HUMAN_ATTENTION" and "waiting" in o.target and o.target["waiting"] in waits:
                waits[o.target["waiting"]].add(o.id)
        return waits

    def weight(self, h: Any, waits: dict[str, set[str]]) -> int:
        """``w``: the obligations whose readiness or discharge waits on ``h``, transitively (§16.8)."""

        waiting_on_h = {h.id}
        changed = True
        while changed:
            changed = False
            for o, on in waits.items():
                if o not in waiting_on_h and on & waiting_on_h:
                    waiting_on_h.add(o)
                    changed = True
        return len(waiting_on_h) - 1

    def opened_at(self, h: Any) -> int:
        """``p``: the ledger position at which ``h`` opened, the start of its latest uninterrupted presence."""

        cache = self.__dict__.setdefault("_present", {})
        position = self.s.n
        while position > 0:
            k = position - 1
            if k not in cache:
                cache[k] = {o.id for o in self.w.at(k).obligations}
            if h.id not in cache[k]:
                break
            position = k
        return position

    def inspector(self) -> dict[str, Any]:
        rank = {"CRITICAL": 0, "MATERIAL": 1, "ROUTINE": 2}
        waits = self._waits()
        entries = []
        for h in self.w.of_kind("HUMAN_ATTENTION"):
            w_, c, p = self.weight(h, waits), rank.get(h.params.get("materiality"), 3), self.opened_at(h)
            entries.append(((-w_, c, p, h.id), h))
        out = []
        for key, h in sorted(entries, key=lambda e: e[0]):
            out.append({"obligation": h.id, "key": {"w": -key[0], "c": h.params.get("materiality"), "p": key[2]},
                        "evidence_core": self._attention_core(h), "framing": "none recorded (interpretation)",
                        "allowed_outcomes": "HUMAN_DECISION (authenticated human); GATE_DECISION for a gate"})
        return {"head": self.head, "entries": out, "digest": self.digest_items()}

    def _attention_core(self, h: Any) -> dict[str, Any]:
        target = h.target
        core: dict[str, Any] = {"target": target, "materiality": h.params.get("materiality"), "detail": h.detail}
        rid = target.get("report") or target.get("escalated")
        if rid in self.s.records:
            record = self.s.record(rid)
            core["record"] = {"id": rid, "kind": record["kind"], "outcome": record["outcome"], "target": record["target"],
                              "reason": record.get("reason") or [], "actor": record["actor"]}
        if "waiting" in target:
            core["waiting"] = target["waiting"]
        return core

    def digest_items(self) -> list[dict[str, Any]]:
        """What agents settled, oldest first (§16.8); Phase E has no acknowledgment record, so since genesis."""

        out = []
        for rid in self.s.of_kind("COORDINATION_DECISION", "MATERIALITY_RECLASSIFICATION"):
            record = self.s.record(rid)
            if record["actor_class"] == "HUMAN":
                continue
            what = "downgrade" if record["kind"] == "MATERIALITY_RECLASSIFICATION" else (
                "declined report" if record["outcome"] == "DECLINE" else "R1 decision")
            out.append({"record": rid, "position": self.s.position_of(rid), "item": what, "outcome": record["outcome"],
                        "challengeable": True})
        for x in self.w.of_kind("COORDINATE"):
            if "recurrence" in x.target or "conformance" in x.target:
                out.append({"obligation": x.id, "item": "recurrence" if "recurrence" in x.target else "discrepancy",
                            "detail": x.detail, "challengeable": True})
        return sorted(out, key=lambda e: (e.get("position", self.s.n + 1), e.get("record") or e.get("obligation")))

    def attention_brief(self, h: Any) -> Brief:
        governs = self.governs(h)
        waits = self._waits()
        sections = (
            ("Header", self._header(h, "ATTENTION", governs)),
            ("Evidence core", _json(self._attention_core(h))),
            ("Framing (interpretation)", "none recorded"),
            ("Allowed outcomes", "HUMAN_DECISION by an authenticated human (A8)"),
            ("Ordering key", _json({"w": self.weight(h, waits), "c": h.params.get("materiality"), "p": self.opened_at(h)})),
        )
        return Brief("ATTENTION", h.id, governs, ("role:HUMAN",), sections)


def _contract_json(contract: Any) -> dict[str, Any]:
    return {"scientific": contract.scientific, "budget": contract.budget, "write_scope": list(contract.write_scope),
            "frozen": list(contract.frozen), "evidence_specs": list(contract.evidence_specs), "homes": list(contract.homes),
            "obligations": [[o.id, repr(o.verifier)] for o in contract.obligations], "slots": list(contract.slots)}


__all__ = ["Brief", "Doctrine", "NOT_ISSUED", "Renderer"]
