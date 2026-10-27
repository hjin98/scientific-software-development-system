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


def brief_digest(data: bytes) -> str:
    """A rendered brief's content identity: the one formula the Issuer's envelope and the renderer share (§16.4;
    Phase F step 8b)."""

    return "sha256:" + hashlib.sha256(data).hexdigest()


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

        return brief_digest(self.text.encode("utf-8"))

    def to_json(self) -> dict[str, Any]:
        return {"form": self.form, "obligation": self.obligation, "governs": self.governs, "duties": list(self.duties),
                "sections": [{"title": t, "text": b} for t, b in self.sections], "digest": self.digest, "text": self.text}


class Renderer:
    """Briefs and the inspector view over one presented state."""

    def __init__(self, workflow: Any, head: dict[str, Any], doctrine: Doctrine,
                 task: dict[str, Any] | None = None) -> None:
        self.w = workflow
        self.s = workflow.s
        self.d = workflow.d
        self.head = head
        self.read_doctrine = doctrine
        #: an issued task's brief (Phase F step 8e, reading F69): ``{task_id, route}``, named before its envelope is
        #: signed, so the rendered bytes the envelope's digest covers are reproduced exactly at the task's basis
        self.issued = task

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

    def doctrine_problem(self, governs: dict[str, Any]) -> str | None:
        """Why no doctrine text can be rendered for this binding, or None: no pin, a source that cannot be read,
        or a source whose ``source/PROTOCOL_VERSION`` is not the pinned version (§16.9, §29.2: never apply a
        non-matching package)."""

        pin = governs.get("doctrine")
        if pin is None:
            return "the ruleset pins no doctrine"
        cache = self.__dict__.setdefault("_doctrine_checked", {})
        key = (pin["source"], pin["version"])
        if key not in cache:
            declared = self.read_doctrine(pin["source"], "source/PROTOCOL_VERSION")
            if declared is None:
                cache[key] = "the pinned doctrine source cannot be read"
            elif declared.decode("utf-8", "replace").strip() != pin["version"]:
                cache[key] = (f"the pinned source declares SSDP {declared.decode('utf-8', 'replace').strip()}, "
                              f"not the pinned {pin['version']}")
            else:
                cache[key] = None
        return cache[key]

    def _doctrine_text(self, governs: dict[str, Any], path: str) -> str | None:
        if self.doctrine_problem(governs) is not None:
            return None
        data = self.read_doctrine(governs["doctrine"]["source"], path)
        return data.decode("utf-8", "replace") if data is not None else None

    def _version_section(self, governs: dict[str, Any]) -> str:
        if governs["mode"] == "LEGACY":
            return (f"LEGACY({governs['protocol']}): rendered through the frozen Core profile "
                    f"{governs['profile'] or 'UNAVAILABLE'}; SSDS compiles no native duties for this subject")
        if governs["mode"] == "UNGOVERNED":
            return "UNGOVERNED: no protocol governs this subject; SSDS renders its derived facts only"
        pin = governs.get("doctrine")
        problem = self.doctrine_problem(governs)
        doctrine = f"SSDP {pin['version']} at {pin['source']}" if pin else "no doctrine pinned"
        if problem is not None:
            doctrine += f" (no doctrine text rendered: {problem})"
        return f"NATIVE: ruleset {governs['ruleset']}; doctrine {doctrine}"

    def _status(self) -> str:
        if self.issued is None:
            return NOT_ISSUED
        return f"ISSUED task {self.issued['task_id']} on route {self.issued['route']}"

    def _reads(self) -> str:
        """§16.4: a harness observes reads into the task's basis; the manual and Git-envelope routes cannot."""

        if self.issued is None:
            return "reads not observed (Phase E: no harness route)"
        if self.issued["route"] == "HARNESS":
            return "reads observed: each read through this route is recorded in the task's basis (§16.4)"
        return (f"reads not observed (route {self.issued['route']}): the basis is the mechanical minimum, the reads "
                f"recorded through read, and declared reliance (§16.4)")

    def _header(self, o: Any, form: str, governs: dict[str, Any]) -> str:
        head = self.head
        return "\n".join([
            f"Governing version: {self._version_section(governs)}",
            f"Status: {self._status()}",
            f"Obligation: {o.kind} {o.id}",
            f"Target: {o.target_json}",
            f"Holder: {o.holder}" + (f"; plan {o.plan}" if o.plan else ""),
            f"Qualified head: {head.get('label')} position {head.get('position')} {head.get('digest')}",
        ])

    # -- duty compilation (§16.3) ------------------------------------------------------------------------

    def events(self, o: Any, governs: dict[str, Any] | None = None) -> list[tuple[str, str]]:
        """The injection events that fire for ``o``, over the work it is about: (event, owner reference path)."""

        kind, s = o.kind, self.s
        work = self.w.briefing.work(o)
        item = work.item
        out: list[tuple[str, str]] = []
        judged = kind in ("ACCEPT", "REVIEW", "REVIEW_REVISION") or (item is not None and item.kind == "AUTHOR")
        if judged and work.domain in DOMAIN_OWNER:
            out.append((f"domain:{work.domain}", REFERENCES + DOMAIN_OWNER[work.domain]))
        if kind in ("ASSESS", "READING", "ADJUDICATE_DISAGREEMENT", "SPEC_REVIEW"):
            out.append(("evidence", REFERENCES + OWNER["evidence"]))
        if self._declares_definitions(work):
            out.append(("definition", REFERENCES + OWNER["definition"]))
        recurrence = kind == "COORDINATE" and "recurrence" in o.target
        budget = (work.holder is not None and work.holder.budget_spent and kind not in REVIEW_KINDS) \
            or o.target.get("condition") == "budget-spent"
        if recurrence or budget:
            out.append(("convergence", REFERENCES + OWNER["convergence"]))
        if recurrence or (item is not None and item.kind == "MIGRATE"):
            out.append(("pem", REFERENCES + OWNER["pem"]))
        if kind == "GATE" or (kind in REVIEW_KINDS and work.scientific):
            out.append(("channel-c", REFERENCES + OWNER["channel-c"]))
            out.append(("inspectability", REFERENCES + OWNER["inspectability"]))
        if kind == "REVIEW_REVISION" or (item is not None and item.kind == "AUTHOR" and work.domain in ("D1", "D2")):
            out.append(("revising", REFERENCES + OWNER["revising"]))
        if self._serious_challenge(o, work):
            out.append(("kernel-challenge", REFERENCES + OWNER["kernel-challenge"]))
        mismatch = governs is not None and governs.get("doctrine") is not None and \
            (self.doctrine_problem(governs) or "").startswith("the pinned source declares")
        if any(s.mode(x) == "LEGACY" for x in work.subjects if x in s.view.structure.units) or mismatch:
            out.append(("versioning", REFERENCES + OWNER["versioning"]))
        written = work.written
        for concern, units in sorted(s.policy.flow("concern_tags").items()):
            if written & set(units):
                out.append((f"concern:{concern}", REFERENCES + CONCERN_OWNER[concern]))
        return out

    def _declares_definitions(self, work: Any) -> bool:
        """A subject the work touches, or its governing closure, declares ``defines``, a definition relation
        (``USES_DEFINITION``) or an external import (an ``EXTERNAL`` unit governing it)."""

        structure = self.s.view.structure
        units = {u for u in structure.units if structure.subj(u) in work.subjects}
        governing = set()
        for subject in work.subjects:
            governing |= {g["unit"] for g in derivation.queries.governs(self.w, subject)}
        if work.item is not None:
            governing |= {u for u, _ in work.item.governing}
        scope = units | governing | {u for u in structure.units if structure.subj(u) in governing}
        if any(d.get("decl") == "defines" and d.get("unit") in scope for d in self.s.view.semantic_declarations):
            return True
        if any(r.type == "USES_DEFINITION" and r.subject in scope for r in self.s.s0.relations):
            return True
        return any(structure.kind(u) == "EXTERNAL" for u in governing if u in structure.units)

    def _serious_challenge(self, o: Any, work: Any) -> bool:
        if o.kind == "ADJUDICATE" and o.target.get("record") in self.s.records:
            if self.s.record(o.target["record"])["fields"].get("serious"):
                return True
        return any(self.s.record(c)["fields"].get("serious") for subject in work.subjects
                   for c in self.w.challenges_on(subject))

    def duties(self, o: Any, governs: dict[str, Any], slots: list[str]) -> tuple[list[str], list[tuple[str, str]], list[str]]:
        """(compiled duty identifiers, their rendered texts, incompleteness notices) for ``o`` (§16.3)."""

        ids: list[str] = []
        texts: list[tuple[str, str]] = []
        notices: list[str] = []
        work = self.w.briefing.work(o)
        item = work.item
        role = o.holder if o.holder in ROLE_CORE else "REVIEWER"
        ids.append(f"role:{role}")
        texts.append((f"Role core ({role}, §12.3)", ROLE_CORE[role]))
        entry = None
        if item is not None and item.kind == "DOCUMENT":
            entry = ("specialist:DOCUMENT", SPECIALIST_ENTRYPOINT["DOCUMENT"])
        elif item is not None and item.specialist:
            entry = (f"specialist:{item.specialist}", SPECIALIST_ENTRYPOINT[item.specialist])
        elif work.domain in DOMAIN_ENTRYPOINT:
            entry = (f"domain:{work.domain}", DOMAIN_ENTRYPOINT[work.domain])
        if entry is not None:
            ids.append(f"core:{entry[0]}")
            text = self._doctrine_text(governs, entry[1])
            if text is None:
                notices.append(f"domain core {entry[1]} not rendered: {self._why_no_text(governs)}")
                text = f"(not rendered: {entry[1]})"
            texts.append((f"Domain core ({entry[0]}: {entry[1]})", text))
        if o.kind in REVIEW_KINDS:
            ids.append("kind:review")
            texts.append(("Kind duty: Challenge Pass", KIND_DUTIES["review"]))
            if work.authority:
                ids.append("kind:out-of-matrix")
                texts.append(("Kind duty: out-of-matrix pass", KIND_DUTIES["out-of-matrix"]))
        for slot in slots:
            ids.append(f"slot:{slot}")
        injected: set[str] = set()
        for event, path in self.events(o, governs):
            ids.append(f"inject:{event}")
            if path in injected:
                continue  # one owner's text once, whichever events name it
            injected.add(path)
            text = self._doctrine_text(governs, path)
            if text is None:
                notices.append(f"injected owner {path} not rendered: {self._why_no_text(governs)}")
                text = f"(not rendered: {path})"
            texts.append((f"Injected owner ({event}: {path})", text))
        return ids, texts, notices

    def _why_no_text(self, governs: dict[str, Any]) -> str:
        return self.doctrine_problem(governs) or "the pinned doctrine source does not hold this file"

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
            if rev is None or rev == current:
                out.append(f"### {unit} @ {current}\n\n{self._unit_text(unit)}")
                continue
            # the exact text at the revision named, never the current one in its place (Phase E review B5)
            data = derivation.queries.content_at(self.w, unit, rev)
            note = f"the current revision is {current}, not shown here" if current else "the unit is not at this head"
            if data is None:
                out.append(f"### {unit} @ {rev}\n\nUNAVAILABLE: no admitted state holds this revision ({note})")
            else:
                out.append(f"### {unit} @ {rev} ({note})\n\n{data.decode('utf-8', 'replace')}")
        return "\n\n".join(out)

    def _incompleteness(self, work: Any, extra: list[str]) -> str:
        notices = list(extra)
        for subject in work.subjects:
            if subject not in self.s.view.structure.units:
                continue
            if subject in self.s.s0.affected_subjects:
                notices.append(f"{subject} carries quarantined structure")
            for r in self.d.acceptances(subject):
                if not self.s.cont(r):
                    notices.append(f"acceptance {r} is withheld by a loss boundary")
            for cls in ("WARRANT", "GOVERNING"):
                widening = derivation.queries.depends(self.w, subject, cls)["widening"]
                if widening != "EXACT":
                    notices.append(f"{cls} prerequisites of {subject}: {widening}")
        notices.append(self._reads())
        notices.append(f"qualified head: {self.head.get('label')} at position {self.head.get('position')}")
        return "\n".join(f"- {n}" for n in notices)

    def _open_states(self, work: Any) -> str:
        """Open challenges, findings and provisional states touching every subject the work touches (§16.3 (6))."""

        lines = []
        for subject in work.subjects:
            if subject not in self.s.view.structure.units:
                continue
            blocked = derivation.queries.blocked(self.w, subject)
            lines.append(f"{subject}: {blocked['status']}")
            lines += [f"- {r}" for r in blocked["reasons"]]
        return "\n".join(lines) or "none"

    def _item_text(self, work: Any) -> str:
        """The item's prose at the revision the work is bound to: its objective reference and every obligation
        statement (§13.1); contract, never the author's narrative."""

        if work.part is None:
            return "no item"
        found = self.s.plans.item_at(work.part.unit, self.s.cur(work.part.unit)) if work.part.unit in self.s.view.structure.units else None
        view = found[0] if found is not None and found[1] == work.part else None
        try:
            prose = self.s.plans.prose(work.part, view).decode("utf-8", "replace")
        except KeyError:
            prose = "(the item's revision is not at this head)"
        return f"Item {work.item.id} ({work.item.kind}):\n\n{prose.strip()}"

    # -- task brief (§16.3) ------------------------------------------------------------------------------------

    def task(self, o: Any) -> Brief:
        governs = self.governs(o)
        if governs["mode"] == "LEGACY":
            return self._legacy(o, governs)
        work = self.w.briefing.work(o)
        item = work.holder
        if item is None:
            return self._generic(o, governs)
        it = item.item
        contract = it.contract
        slots = self.w.briefing.owed_slots(o)
        ids, duty_texts, notices = self.duties(o, governs, slots)
        plan = self.s.plans.plans.get(item.plan)
        objective = self._unit_text(plan.objective) if plan is not None and plan.objective else "(no objective)"
        prose = self.s.plans.prose(item.part).decode("utf-8", "replace")
        role_section = "\n\n".join([f"Objective of plan {item.plan}:\n\n{objective.strip()}",
                                    f"Item {it.id} ({it.kind}), workflow role {o.holder}:\n\n{prose.strip()}"]
                                   + [f"### {t}\n\n{b.strip()}" for t, b in duty_texts])
        boundaries = "\n".join([
            f"write_scope: {_json(list(item.share[3] if item.share else contract.write_scope))}",
            f"frozen interface: {_json(list(contract.frozen))}",
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
        open_states = self._open_states(work)
        previous = self._previous_iteration(item)
        if previous:
            open_states += "\n\nPrevious iteration (data, never its narrative):\n" + previous
        drift = item.drift_changes() if item.moved else []
        if drift:
            open_states += "\n\nDrift (§10.4): the changes that moved this item's outputs since its latest integration:\n"
            open_states += "\n".join(f"- {c['unit']} at position {c['position']} ({c['entry']}): "
                                     + (f"integration of {c['transformation']} for item {c['item']}" if c["made_by"] == "integration"
                                        else "an absorption") for c in drift)
            open_states += ("\nThose later accepted changes are preserved: the next iteration starts from the current "
                            "content, never from the item's last integration.")
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
            ("7. Incompleteness notices", self._incompleteness(work, notices)),
            ("8. Governing version", self._version_section(governs)),
            ("9. Escalation triggers, budget, workspace and submission", escalation),
        )
        return Brief("TASK", o.id, governs, tuple(ids), sections)

    def _previous_iteration(self, item: Any) -> str:
        if not item.enactments:
            return ""
        last = item.enactments[-1]
        conformance = self.w.conformance(last.result)
        lines = [f"iteration {item.iterations}: conformance {_json(sorted(conformance.classes))}"]
        lines += [f"- {ob}: {h['template']} {h['class']} {h['finding']}" for ob, hits in sorted(conformance.view().items())
                  for h in hits if h["class"] != "CLEAN"]
        for review in (item.reviews(last.transformation) if last.transformation else []):
            lines.append(f"- review {review}: {self.s.record(review)['outcome']}; findings {_json(item.items.findings_of(review))}")
        return "\n".join(lines)

    def _generic(self, o: Any, governs: dict[str, Any]) -> Brief:
        work = self.w.briefing.work(o)
        ids, duty_texts, notices = self.duties(o, governs, self.w.briefing.owed_slots(o))
        sections = (
            ("Header", self._header(o, "TASK", governs)),
            ("1. Objective, obligation kind and workflow role",
             "\n\n".join([f"{o.kind} {o.detail or o.target_json}"] + [f"### {t}\n\n{b.strip()}" for t, b in duty_texts])),
            ("2. Allowed outcomes", JUDGMENT_OUTCOMES.get(o.kind, TASK_OUTCOMES)),
            ("6. Open challenges, findings and provisional states", self._open_states(work)),
            ("7. Incompleteness notices", self._incompleteness(work, notices)),
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
        work = self.w.briefing.work(o)
        slots = self.w.briefing.owed_slots(o)
        ids, duty_texts, notices = self.duties(o, governs, slots)
        if derivation.UNKNOWN in self.w.judged_authors(o):
            # §5.10 (f) and §16.5 (Phase F step 8d, reading F72): the judged content's authorship is unknown
            notices.append("the judged content's authorship is unknown: an agent's answer is never independent of it; "
                           "a human judge's is independent only with a NON_AUTHORSHIP_ATTESTATION (the human rule, "
                           "§5.10 (f)), or is the owner's")
        x = o.target.get("transformation") if isinstance(o.target, dict) else None
        result = self.w.submitting_result(x) if x else None
        conformance = self.w.conformance(result) if result else None
        contract = conformance.contract[0] if conformance is not None else (work.item.contract if work.item else None)
        governing: set[tuple[str, str | None]] = set()
        for subject in work.subjects:
            governing |= {(g["unit"], g["rev"]) for g in derivation.queries.governs(self.w, subject)}
        asked = self.w.subject_of(o)
        if asked is not None and asked in self.s.view.structure.units and asked != work.plan:
            governing.add((asked, self.s.cur(asked)))
        if work.item is not None:
            governing |= {(u, r) for u, r in work.item.governing}
        candidate = "none (a judgment of standing content)"
        disclosure = "none"
        if result is not None:
            record = self.s.record(result)
            candidate = _candidate_diff(conformance, record)
            slot_values = ((record.get("fields") or {}).get("slots") or {})
            # §16.5: the result's disclosure slots, labeled as the author's claims to test; never its outcome,
            # rationale, narrative, commit messages or transcripts
            disclosure = "\n".join(f"- {name} (the author's claim, to test): {_json(slot_values[name])}"
                                   for name in ("deviations", "unverified_assumptions", "claims") if name in slot_values) or "none"
        view = conformance.view() if conformance is not None else {}
        conf = "\n".join(f"- {ob}: {h['template']} {h['class']}" + (" (SIGNAL: a pointer to look, not a finding)"
                                                                     if h["class"] == "SIGNAL" else "")
                         for ob, hits in sorted(view.items()) for h in hits) or "none"
        evidence = []
        for subject in work.subjects:
            evidence += [f"- {subject}: {_json(e)}" for e in self.w.briefing.required_evidence(subject)]
        carried = self.w.briefing.carried(o)
        sections = (
            ("Header", self._header(o, "REVIEW", governs)),
            ("Duties", "\n\n".join(f"### {t}\n\n{b.strip()}" for t, b in duty_texts)
             + "\n\nRequired slots:\n" + "\n".join(f"- {SLOT_DUTIES.get(s_, s_)}" for s_ in slots)),
            ("Allowed outcomes", JUDGMENT_OUTCOMES.get(o.kind, "PASS, NO_PASS")),
            ("Governing content", self._governing_inline(sorted(governing, key=lambda g: (g[0], g[1] or "")))),
            ("Contract and item", (_json(_contract_json(contract)) if contract is not None else "no contract")
             + "\n\n" + self._item_text(work)),
            ("Candidate diff and machine-produced facts", candidate),
            ("Conformance view", conf),
            ("Evidence", "\n".join(evidence) or "no evidence obligation required"),
            ("Disclosure slots (the author's claims to test)", disclosure),
            ("Carried objections (another judge's)", _carried_text(carried)),
            ("Incompleteness notices", self._incompleteness(work, notices)),
        )
        return Brief("REVIEW", o.id, governs, tuple(ids), sections)

    # -- gate brief (§16.6) ---------------------------------------------------------------------------------------

    def gate(self, o: Any) -> Brief:
        governs = self.governs(o)
        if governs["mode"] == "LEGACY":
            return self._legacy(o, governs)
        work = self.w.briefing.work(o)
        subject = self.w.subject_of(o)
        ids, duty_texts, notices = self.duties(o, governs, [])
        required = self.w.briefing.required_evidence(subject) if subject else []
        core = "\n".join([
            f"gate: {o.target.get('gate')}; decision asked: GATE_DECISION on {_json(o.target.get('subject'))}",
            f"qualified head: {self.head.get('label')} position {self.head.get('position')} {self.head.get('digest')}",
            "required evidence (the decision's supporting premises, or why each does not hold):",
            *[f"- {e['obligation']}: {e['status']}" + (f" via {', '.join(e['via'])}" if e["via"] else "")
              + "".join(f"\n  - {_json(r)}" for r in e["records"]) for e in required],
            "findings as data (standing adverse judgments whose reach includes the decision asked):",
            _carried_text(self.w.briefing.carried(o)),
            "open challenges, quarantine, loss and provisional states:", self._open_states(work),
            "tensions found by the relying search:",
            *[f"- {_json(t)}" for t in (derivation.queries.tensions(self.w, subject) if subject else [])],
            "known missing realized records: Admission classifies them (Phase F); none recorded"])
        rev = self.s.cur(subject) if subject in self.s.view.structure.units else None
        earlier = []
        for kind in ("GATE_DECISION", "ACCEPTANCE"):
            for r in self.s.of_kind(kind):
                target = self.s.record(r)["target"]
                about = target.get("subject") if isinstance(target, dict) else None
                triple = about if isinstance(about, dict) else target
                if isinstance(triple, dict) and triple.get("subject") == subject and triple.get("rev") == rev:
                    fields = self.s.record(r).get("fields") or {}
                    earlier.append(f"- {kind} {r}: {self.s.record(r)['outcome']} by {self.s.record(r)['actor']}"
                                   + (f"; qualification {fields['qualification']}" if "qualification" in fields else ""))
        revision = "not a D1/D2 revision"
        if subject is not None and self.s.view.structure.kind(subject) in ("D1", "D2"):
            counting = self.w.counting(subject)
            revision = "\n".join(f"- revision-assessment record {r} by {self.s.record(r)['actor']} (proposed until "
                                 f"accepted): {_json(self.s.record(r).get('fields') or {})}" for r in counting) \
                or "no counting revision-assessment record: the gate is not ready (§10.2)"
        sections = (
            ("Header", self._header(o, "GATE", governs)),
            ("1. Evidence core", core),
            ("2. Consequential-decision disclosure", "\n".join(earlier) or "no earlier decision on this content"),
            ("3. D1/D2 revision assessments", revision),
            ("4. Interpretation (Channel A)", "none recorded (labeled interpretation, never evidence)"),
            ("5. Allowed outcomes and required fields", "ACCEPT, REJECT; GATE_DECISION requires adequacy and qualification"),
            ("Duties", "\n\n".join(f"### {t}\n\n{b.strip()}" for t, b in duty_texts)),
            ("Incompleteness notices", self._incompleteness(work, notices)),
        )
        return Brief("GATE", o.id, governs, tuple(ids), sections)

    # -- decision brief (§16.7) -----------------------------------------------------------------------------------

    def _no_part_triggers(self, x: Any) -> list[str]:
        """What makes an item-level-no-part decision owed (§16.7: the relevant review outcomes): each standing
        item-level review naming no part, with its outcome, target and findings, and failing retained work no part
        covers (re-Review of 9c7d77d, E-R4)."""

        item = next((i for i in self.w.items.all if i.unit == x.target.get("item") and i.plan == x.plan), None)
        if item is None:
            return []
        lines = []
        for r in item.no_part_objections:
            record = self.s.record(r)
            lines.append(f"  - standing review {r} by {record['actor']}: {record['outcome']} on {_json(record['target'])}; "
                         f"findings {_json(self.w.items.findings_of(r))}")
        if item.uncovered_failing:
            lines.append(f"  - failing retained work no part covers: {_json(list(item.uncovered_failing))}")
        return lines

    def decision(self, o: Any) -> Brief:
        governs = self.governs(o)
        work = self.w.briefing.work(o)
        ids, duty_texts, notices = self.duties(o, governs, self.w.briefing.owed_slots(o))
        plan = self.s.plans.plans.get(o.plan) if o.plan else None
        objective = self._unit_text(plan.objective).strip() if plan is not None and plan.objective else "(no plan)"
        items = [f"- {i.unit} ({i.item.kind}): route {i.route.route}; discharge {i.discharge()}; "
                 f"{i.iterations}/{i.budget} iterations"
                 + (f"; failing retained work no part covers: {_json(list(i.uncovered_failing))}"
                    if i.partition is not None and i.uncovered_failing else "")
                 for i in self.w.items.all if i.plan == o.plan]
        owed = {x.id: x for x in self.w.of_kind("COORDINATE", "CONTRACT") if o.plan is not None and x.plan == o.plan}
        owed[o.id] = o
        decisions = []
        for x in sorted(owed.values(), key=lambda x: x.id):
            core = x.target
            outcomes = ", ".join(self.w.briefing.decision_outcomes(x))
            report = core.get("report") if isinstance(core, dict) else None
            if report in self.s.records:
                record = self.s.record(report)
                decisions.append(f"- {x.id}: report {record['kind']} {report} on {_json(record['target'])} reasons "
                                 f"{_json(record.get('reason') or [])}; allowed {outcomes}")
            elif x.kind == "CONTRACT":
                lint = [f.detail if hasattr(f, "detail") else str(f) for f in self.s.plans.item_lint(core["item"])]
                decisions.append(f"- {x.id}: the contract of {core['item']} @ {core['rev']} (the principal's plan change); "
                                 f"lint {_json(lint)}; outcomes {outcomes}")
            else:
                decisions.append(f"- {x.id}: {x.detail or x.target_json}; allowed {outcomes}")
                if isinstance(core, dict) and core.get("condition") == "item-level-no-part":
                    decisions += self._no_part_triggers(x)
        attention = [f"- {h.id}: {h.target_json} ({h.params.get('materiality')})"
                     for h in self.w.of_kind("HUMAN_ATTENTION") if h.plan == o.plan]
        since = max((self.s.position_of(r) for r in self.s.of_kind("COORDINATION_DECISION")
                     if (self.s.record(r).get("binding") or {}).get("obligation") in owed
                     or set((self.s.record(r)["target"] or {}).get("records", [])) & set(owed)), default=0)
        changed = derivation.queries.changed(self.w, since)
        sections = (
            ("Header", self._header(o, "DECISION", governs)),
            ("Plan objective and items", objective + "\n\n" + ("\n".join(items) or "no item obligations")),
            ("Decisions owed", "\n".join(decisions)),
            ("Budgets, recurrences and discrepancies",
             "\n".join(f"- {x.detail}" for x in owed.values() if "recurrence" in x.target or "conformance" in x.target
                       or x.target.get("condition") == "budget-spent") or "none"),
            ("Open human-attention items of the plan", "\n".join(attention) or "none"),
            ("What changed since the previous coordination",
             "\n".join(f"- position {c['position']}: {_json(c['units'])}" for c in changed) or "nothing"),
            ("Duties", "\n\n".join(f"### {t}\n\n{b.strip()}" for t, b in duty_texts)),
            ("Incompleteness notices", self._incompleteness(work, notices)),
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

    def waits(self) -> dict[str, set[str]]:
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

    def consequence(self, h: Any) -> str:
        """``c``: human attention's materiality; every other decision R3 owns is ``CRITICAL`` (§15.4)."""

        return h.params.get("materiality", "CRITICAL") if h.kind == "HUMAN_ATTENTION" else "CRITICAL"

    def inspector(self) -> dict[str, Any]:
        """Everything R3 owns, open, by ``(-w, c, p, id)`` (§16.8): human attention, gates and every decision a
        human holds; then the digest."""

        rank = {"CRITICAL": 0, "MATERIAL": 1, "ROUTINE": 2}
        waits = self.waits()
        entries = []
        for h in self.w.obligations:
            if not self.w.briefing.r3(h) or self.w.discharge(h) in ("DISCHARGED", "DISCHARGED_PROVISIONAL"):
                continue
            c = self.consequence(h)
            entries.append(((-self.weight(h, waits), rank.get(c, 3), self.opened_at(h), h.id), h, c))
        out = []
        for key, h, c in sorted(entries, key=lambda e: e[0]):
            out.append({"obligation": h.id, "kind": h.kind, "key": {"w": -key[0], "c": c, "p": key[2]},
                        "evidence_core": self._attention_core(h), "framing": "none recorded (interpretation)",
                        "allowed_outcomes": self._r3_outcomes(h)})
        # §16.8: a QUALIFIED gate ACCEPT stays an entry while it is eligible, until superseded; nothing waits on
        # it, so it follows the open obligations of its consequence class, oldest first
        gates = sorted(self.w.briefing.qualified_gates(), key=lambda g: (g["position"], g["record"]))
        for g in gates:
            out.append({"obligation": g["record"], "kind": "QUALIFIED_GATE", "key": {"w": 0, "c": "CRITICAL", "p": g["position"]},
                        "evidence_core": g, "framing": "none recorded (interpretation)",
                        "allowed_outcomes": "a superseding GATE_DECISION by an authenticated gate holder"})
        out.sort(key=lambda e: (-e["key"]["w"], rank.get(e["key"]["c"], 3), e["key"]["p"], e["obligation"]))
        return {"head": self.head, "entries": out, "digest": self.digest_items()}

    def _r3_outcomes(self, h: Any) -> str:
        if h.kind == "GATE":
            return "GATE_DECISION: ACCEPT or REJECT, with adequacy and qualification"
        if h.kind == "HUMAN_ATTENTION":
            return "HUMAN_DECISION by an authenticated human (A8)"
        if h.kind in ("COORDINATE", "CONTRACT"):
            return ", ".join(self.w.briefing.decision_outcomes(h)) + " (an authenticated human's decision)"
        return JUDGMENT_OUTCOMES.get(h.kind, "an authenticated human's judgment")

    def _attention_core(self, h: Any) -> dict[str, Any]:
        target = h.target
        core: dict[str, Any] = {"kind": h.kind, "target": target, "detail": h.detail}
        if h.kind == "HUMAN_ATTENTION":
            core["materiality"] = h.params.get("materiality")
        rid = target.get("report") or target.get("escalated") if isinstance(target, dict) else None
        if rid in self.s.records:
            record = self.s.record(rid)
            core["record"] = {"id": rid, "kind": record["kind"], "outcome": record["outcome"], "target": record["target"],
                              "reason": record.get("reason") or [], "actor": record["actor"]}
        if isinstance(target, dict) and "waiting" in target:
            core["waiting"] = target["waiting"]
        subject = self.w.subject_of(h)
        if h.kind in ("GATE", "ACCEPT") and subject is not None:
            core["required_evidence"] = self.w.briefing.required_evidence(subject)
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
        for obligation, rid in self.w.briefing.unfloored_failures():
            out.append({"record": rid, "position": self.s.position_of(rid), "item": "failure counted, no floor event",
                        "obligation": obligation, "challengeable": True})
        return sorted(out, key=lambda e: (e.get("position", self.s.n + 1), e.get("record") or e.get("obligation")))

    def attention_brief(self, h: Any) -> Brief:
        governs = self.governs(h)
        waits = self.waits()
        sections = (
            ("Header", self._header(h, "ATTENTION", governs)),
            ("Evidence core", _json(self._attention_core(h))),
            ("Framing (interpretation)", "none recorded"),
            ("Allowed outcomes", self._r3_outcomes(h)),
            ("Ordering key", _json({"w": self.weight(h, waits), "c": self.consequence(h), "p": self.opened_at(h)})),
        )
        return Brief("ATTENTION", h.id, governs, ("role:HUMAN",), sections)


#: The most diff lines inlined per file; a longer change is bound by its content identities instead (§16.5).
DIFF_LINES = 400


def _candidate_diff(conformance: Any, record: dict[str, Any]) -> str:
    """The candidate diff (§16.5): bound to its base, candidate and transformation, every changed path with its
    type and mode change and a unified diff of its text; binary or overlong content by its content identity."""

    import difflib

    target = record["target"]
    lines = [f"transformation {target.get('transformation')}: base {target.get('base')} -> candidate {target.get('candidate')}"]
    base, cand = conformance.base_tree, conformance.candidate_tree
    if base is None or cand is None:
        return "\n".join(lines + ["the candidate's frame is not available at this head: no diff can be shown"])
    for path in sorted(set(base) | set(cand)):
        old, new = base.get(path), cand.get(path)
        if old is not None and new is not None and old.mode == new.mode and old.data == new.data:
            continue
        kind = "added" if old is None else "removed" if new is None else "changed"
        endpoints = f"{_entry(old)} -> {_entry(new)}"  # existence, type and mode of both ends (§1.5)
        mode = "" if old is not None and new is not None and old.mode == new.mode else f"; mode {old.mode if old else 'absent'} -> {new.mode if new else 'absent'}"
        lines.append(f"\n### {path}: {kind} ({endpoints}){mode}")
        before = old.data if old is not None else b""
        after = new.data if new is not None else b""
        try:
            a_text, b_text = before.decode("utf-8"), after.decode("utf-8")
        except UnicodeDecodeError:
            lines.append(f"binary content: {_identity(before)} -> {_identity(after)}")
            continue
        diff = list(difflib.unified_diff(a_text.splitlines(keepends=True), b_text.splitlines(keepends=True),
                                         fromfile=f"a/{path}", tofile=f"b/{path}"))
        if len(diff) > DIFF_LINES:
            lines.append(f"{len(diff)} diff lines, not inlined: {_identity(before)} -> {_identity(after)}")
        else:
            # a line with no final newline keeps git's marker, so the patch reconstructs the bytes it shows
            lines.append("```diff\n" + "".join(d if d.endswith("\n") else d + "\n\\ No newline at end of file\n"
                                               for d in diff) + "```")
    return "\n".join(lines) if len(lines) > 1 else lines[0] + "\nno file changed"


def _entry(entry: Any) -> str:
    return "absent" if entry is None else f"{entry.type} {entry.mode}"


def _identity(data: bytes) -> str:
    return f"{len(data)} bytes, sha256:{hashlib.sha256(data).hexdigest()}" if data else "absent"


def _carried_text(carried: list[dict[str, Any]]) -> str:
    return "\n".join(f"- {c['kind']} {c['record']} by {c['actor']}: {c['outcome']} ({c['why']})"
                     + (f"; findings {_json(c['findings'])}" if "findings" in c else "") for c in carried) or "none"


def _contract_json(contract: Any) -> dict[str, Any]:
    return {"scientific": contract.scientific, "budget": contract.budget, "write_scope": list(contract.write_scope),
            "frozen": list(contract.frozen), "evidence_specs": list(contract.evidence_specs), "homes": list(contract.homes),
            "obligations": [[o.id, repr(o.verifier)] for o in contract.obligations], "slots": list(contract.slots)}


__all__ = ["Brief", "Doctrine", "NOT_ISSUED", "Renderer", "brief_digest"]
