---
kind: architecture-manual-amendment-proposal
amendment: A10
amends: orchestrator/docs/ssds-8.0-architecture.md (SSDS-ARCHITECTURE-MANUAL 1.0.0, accepted-current, A1-A9), blob fe43f04f5a698688727f7473a7c2e4d5345ae911 at 072841443b0ee362ff4157f31d4870c6aec9c9c2
status: proposed
protocol_version: 7.2.1
target_system_version: 8.0.0
decision: SD-63 (stakeholder decision record item 59)
source_material: ~/SSDP-8.0-AMENDMENT-1-HANDOFF-TO-CLAUDE-CODE.md (outside the repository; sha256 4a4b477b459acd4441b5026e7d7523ab8449cc5d4859a8cb34bac951e48a52e4), embedding the reviewed SSDP 8.0 Amendment 1 revision 4 (sha256 bcf611b6c310deaca9463df5745823aca263c035606e3ebda16ecccff62d3048), written against workplans/archive/SSDP-8.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-CONSOLIDATED.md (sha256 beb7936be89484f8613e0598b763286dbfd39339d9abf970e9caec8b5608bd8c) under SSDP 6.6.0
items_re_derived: A, B, D, E (item C routed separately to the PEM schema owner; item F kept as a reopen trigger)
companion_proposal: qualification/ssds80/PEM-SCHEMA-PROPOSAL-TYPED-APPLICABILITY-BINDINGS.md (item C, for hjin98/scientific-software-development-protocol; not submitted)
review: a different-family Review is required before acceptance; handoff to be written for the commit that holds this file
pem_doctrine_mutation: none
d4: not authorized; the SSDS PEM lineage reconciliation (§8) is a prerequisite of any D4 work for the derived PEM facts
active_serious_challenge: none
---

# SSDS 8 Manual amendment A10 (proposed): Project Engineering Memory occasions, derived memory facts and closeout learning

```text
STATUS:      PROPOSED. Changes nothing until a different-family Review passes it and the stakeholder
             accepts it, as A9 was (SD-61, SD-62). The accepted Manual is not edited by this file.
DECISION:    SD-63 (stakeholder decision record item 59): re-derive items A, B, D and E of the SSDP 8.0
             Amendment 1 handoff as a proposed Manual amendment against the accepted Manual under SSDP
             7.2.1, after Phase E passed (re-Review of c2b1ec2, PASS).
GOVERNING:   SSDP 7.2.1 (identities from PROTOCOL-RELEASE-STATE.yaml: public source aaeaf8b6b2121b9fb8aba31917c8265649c43954,
             recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d). PEM meaning is owned by
             source/shared/references/project-engineering-memory.md and project-engineering-memory-schema.md
             at that public source, both unchanged since 6.6.
LEVEL:       architecture. Mechanism goes to the catalogue as proposed material settled at G2 (§0.1).
EFFECT:      one new owner subsection (§16.11) and pointer edits in §0.6, §5.1, §8.3, §13.1, §13.4, §13.5,
             §14.3, §15.5, §15.7, §16.2, §16.3, §16.5, §19.8, §29.3, §29.6, §30, §31.2, §31.9, §32.2,
             §32.3 and §33 (§4 below). No new primitive, component, record kind, record tier, obligation
             kind, persistent store or PEM field.
PREREQUISITE: the repository's PROJECT-ENGINEERING-MEMORY.md names the protocol project; its lineage is
             reconciled by project governance before any D4 work for §16.11 (a) and (e) (§8).
SERIOUS CHALLENGE: none
```

## 1. Why a re-derivation, and what the Manual already does

The handoff's amendment was reviewed against the SSDP 8.0 consolidated workplan: TaskEnvelope and ResultEnvelope fields, a reducer, a §9 typed graph and §21 materiality facts. That design was archived byte-identically (`513da27c`, 2026-10-01) and replaced by the SSDS 8 graph-native architecture, whose owners differ: work is obligations (§10) and items with work contracts (§11, §13); what a task owes is compiled into its brief (§16.3) and returned in typed slots (§13.5); facts come from a pure derivation over the ledger and content (§5); every decision owed with no report behind it goes to a principal as a `COORDINATE` decision (§12.5, §15.5). The amendment's own reopen trigger ("control plane narrowed: re-derive A, B and D against the narrowed design rather than re-adding machinery") applies. Nothing below is folded from the handoff by reference.

The accepted Manual already realizes part of the PEM contract:

| Accepted text | What it does |
|---|---|
| §0.4 S8, T3 | PEM is non-authoritative; a HAS is task-local; memory text is data |
| §16.3 injection table, PEM row | on "the item kind is `MIGRATE`, or the task replaces mature machinery (policy-tagged units), or recurrence detection", the brief carries the PEM owner text and `HISTORICAL` items |
| §16.2 `history(x)`, `HISTORICAL` label | ledger history and PEM entries offered only when the PEM predicate fires or on request |
| §15.7 | recurrence detected mechanically creates a `COORDINATE` decision carrying the convergence duty |
| §29.5 maintenance-audit row | no PEM admission or authority by assertion |
| §31.10 | PEM schema validation for the bound basis is a G1 document check |

Phase E realized the row for `MIGRATE` and recurrence (reading E13; `ssds.interface.render`). What remains at E3 today is the rest of the PEM contract: whether memory activates on the occasion (the clauses' qualifiers), retrieval and the HAS, freshness of a HAS against memory and owner changes, reverse reconciliation when an owner cited by an `AUTHORITY_BOUND` capability or normative notice changes, and the closeout learning assessment. The 7.x evidence that motivated the handoff stands (conditional "read the owner when …" routing loaded the owner in 15 of 41 owed cases; `qualification/ssdp70/PROTOCOL-7X-QUALIFICATION-STUDY-EVIDENCE-AND-LESSONS-2026-10-12.md` §2, §3.2), and §29.1 already names typed slots as the default form for owed questions.

## 2. Governing parents

**Manual.** S8 and T3; S5 (absence of a relation proves independence only inside judged-complete scope); S9 and A6 (no machine vocabulary turns a judgment into a fact; facts by machinery, judgment in typed slots); A4 (a duty a task owes is carried in its brief or enforced mechanically; briefs carry only triggered duties); A7 (no control decision parses prose); C3 and C7 (external facts only as records; minimum control data); P3 (derived state is rebuildable; canonical records win); T2 (unknown artifacts are never executed or deserialized to classify them); §5.1 (policy parameterizes, never adds a rule language); §16.4 (typed control facts in records, narrative by content reference); §33 (no registries, wrappers or fields solely to mirror inherited doctrine).

**PEM owners at the 7.2.1 public source** (both unchanged from 6.6.0; this proposal changes neither):

- *Activation* ("When memory activates"): memory loads only when demonstrated history can materially change the decision: substantial rework of mature D1-D4 semantics or concretization; replacement or consolidation of mature machinery; suspected recurrence; substantial optimization or scaling; migration, recovery, revert or restoration where prior choices matter; or an active workplan explicitly binding relevant memory. A first clean local defect, trivial or unrelated work, or the mere presence of a PEM file does not load it.
- *Retrieval and HAS*: resolve the accepted/base PEM by project Git acceptance policy, compose a validated candidate overlay (visibly candidate, never erasing accepted entries by omission), search canonical family and notice metadata regardless of temperature or summary, record the canonical HAS (`pem_basis` with exactly `accepted_project_state`, `accepted_pem`, `candidate_overlay_semantic_candidate`; rows `id`/`disposition`/`reason`), build a capability-transfer map when mature machinery is replaced, and refresh dispositions when the memory basis, overlay or a governing owner materially advances before integration or closeout.
- *Missing memory is not absence*: for missing, malformed, unsupported, partial or stale memory, "perform bounded historical intake over the affected scope **or** keep explicit `REVIEW_REQUIRED` uncertainty"; PEM is not a runtime single point of failure.
- *Authority binding*: `AUTHORITY_BOUND` force comes only from the exact current owner; an unhealthy or unavailable binding is `REVIEW_REQUIRED`, not retained force. The reverse reconciliation duty on owner change is in the workflow, architecture and evidence owners the schema owner routes to.
- *Closeout learning*: after an accepted material repair, rework, optimization, revert or restoration, the closeout learning assessment precedes lifecycle closure; updates only through admission thresholds and PEM governance; no specialist self-promotes or declares `AUTHORITY_BOUND`.
- *Scope and portability*: copying or forking memory does not manufacture local incidence; inherited entries are external or historical evidence until project governance reconciles lineage.

## 3. The re-derivation

### 3.1 Mapping

| Handoff item and mechanism | SSDS 8 owner after A10 | Change from the handoff |
|---|---|---|
| A.2 trigger tiers (`ACTIVATED`, `ASSESSMENT_REQUIRED`, `NONE`) | occasion table in §16.11 (b); the §16.3 injection row points to it | tiers become "activates" (only the contract's memory binding) and "assessment" (every other detected occasion); `NONE` is simply no occasion |
| A.2 "typed binding in the governing workplan" | contract field `memory.bind` (§13.1), authored by the principal, judged relevant by plan acceptance (R2) | the plan item is the SSDS "governing workplan"; its acceptance is the recorded planning-time relevance judgment |
| A.2 `intended_change_class`; D.1 `change_class` | contract field `change_intent` (§13.1), declared at planning and judged in plan acceptance | one planning-time declaration replaces the two classes; the realized revert is **detected** on the candidate (byte identity), not declared |
| A.2 "requested action type" for revert, restoration, recovery | declared `change_intent`, a detected revert on the candidate, or a candidate that restores a subject (§19.4) | recovery has no SSDS action type; it is declared as `restoration` or stays an E3 judgment (§16.11 (b); handoff open item 8) |
| A.3 candidate set | §16.11 (d), derived in each state | owner-bound candidates are bound to the units the brief already carries as `GOVERNING`; tag match reads contract `memory.terms` |
| A.4 envelope fields `pem_context`, `pem_trigger_assessment`, `has_record_ref`, `pem_uncertainty` | brief items (`HISTORICAL`, §16.2) and three result slots `pem_activation`, `historical_applicability`, `closeout_learning` (§13.5) | slots, not envelope fields: §13.5 is the SSDS delegation return; `NONE` with a typed reason replaces `pem_uncertainty` |
| A.5 coverage, replay and claim limit | `OBLIGATION` `HARD` templates (§14.3) over the candidates the recorded brief lists (§16.4) | conformance, not a reducer step; adequacy stays with review (E3) |
| A.5 corroboration of `pem_uncertainty` | the reader state is itself derived; a `PEM_UNAVAILABLE` reason is admissible only where the derived reader state is `UNREADABLE` | no separate read observation is needed |
| A.5 memory-review obligation | the unavailability is a required review item of the item's review (§16.5) | the independent review (or a human) accepts or rejects the stated uncertainty; no new obligation kind |
| A.5 HAS freshness (publication advance, bound-owner advance, checked at ingestion and at closure) | §16.11 (f): an `OBLIGATION` `HARD` template evaluated in the state the result is evaluated in, re-derived after every rebase (§11.5) | one check reaches both "ingestion" and "closure" because integration re-derives conformance on the rebased candidate; nothing is reopened after integration |
| B.1 realization (i) persistent projection or (ii) on-demand query observation | (iii) a pinned data-only **PEM reader** analyzer deriving **PEM facts** from the PEM units' content (§16.11 (a)) | PEM is repository content that derivation already reads; no projection, no observation record, nothing mirrored, so no `MISMATCH` state and no rebuild obligation (handoff open decision 5) |
| B.2 overlay scoping | frames (§7): a candidate's PEM change is visible only in its frame | the SSDS frame is the candidate overlay; base and overlay candidates are unioned (handoff open item 2) |
| B.2 "reconciliation state is not a PEM fact" | reconciliation decisions are derived S3 obligations keyed on state | holds by construction |
| B.2 scoped completeness | §16.11 (d), (e) | completeness only for resolved owner routes; never for tags (S5) |
| B.3 reverse impact on accepted owner change with typed materiality | §16.11 (e): a binding is stale when its owner unit's revision is not reached from the bound revision by an `EDITORIAL` or `REPRESENTATION` equivalence path (§4.4); each stale binding derives a `COORDINATE` decision | materiality is the existing equivalence judgment, failing closed; a state predicate, so an owner change during an unreadable interval is never lost; the binding-discovery obligation is unnecessary (handoff open item 6) |
| B.4 Phase G retention | §19.8 and §29.6: the PEM owner text is injected whole; the duties A10 does not mechanize are listed as disclosed E3 | SSDS does not edit protocol text, so retention is a statement, not a cut-over rule |
| D.1 closeout-learning obligation | slot `closeout_learning` on the item's results; `UPDATE_PROPOSED` derives a `COORDINATE` decision | a slot, not a new obligation; no answer writes memory |
| D.2 recurrence signals | §15.7, extended with a detected revert of integrated work | the existing recurrence route; the maintenance audit stays reachable through the principal's `AMEND` (handoff open decision 3) |
| E retrieval-quality record | §31.9 G3 measures | a measurement, not a view or record; recall reads canonical PEM at later revisions outside derivation (handoff open item 5) |
| F similarity net | §32.3 reopen trigger; §16.2 `search` already returns `CANDIDATE` only | deferred, as proposed |
| C typed applicability bindings | companion proposal to the PEM schema owner; §16.11 (d)(3) consumes owner and surface bindings once adopted | A10 works without C |

### 3.2 What the re-derivation buys and costs

It adds two contract fields (`memory`, `change_intent`), three slots, two `COORDINATE` triggers, one analyzer, one policy parameter (`pem_root`), one proposed default (the candidate cap) and four `OBLIGATION` templates. It adds no record kind, obligation kind, component or store. The handoff's projection, `facts_state`, mismatch handling, rebuild obligation, discovery obligation, memory-review obligation, HAS-refresh obligation and `pem_uncertainty` are not needed, because each is replaced by derivation the Manual already performs or by an existing route.

The cost is mainly burden: an answer per fired occasion, a HAS whenever memory activates, and, rarely, an iteration spent when memory or a bound owner changes under in-flight work. §32.3 gains reopen triggers for both.

## 4. Proposed Manual text

Each edit names the section, the accepted text it changes and the proposed text. On acceptance the text is applied verbatim, each changed place marked *[Amendment A10, SD-63.]* as A9 was, and the lifecycle header and status lines record it.

### 4.1 New §16.11 (inserted after §16.10)

> #### 16.11 Project Engineering Memory [D3 decision; amendment A10]
>
> This section is the one owner of how SSDS realizes the governing PEM contract: which of its occasions machinery detects, what a task owes when one fires, what machinery derives from memory, and what follows. PEM meaning (the activation predicate and its qualifiers, retrieval, the HAS shape, binding meanings, admission, maturity and claim strength) stays with the PEM owners at the governing source (S8). Nothing here adds a PEM field, a memory store or a judgment, and every other section that touches memory points here.
>
> **(a) Memory is content; its facts are derived.** Policy names the PEM root unit and its partition units (`pem_root`, §5.1), by default the unit that owns the project's discovery root. With none named, no PEM fact is derived and every PEM duty stays at the level the injected PEM owner text gives it (E3). A pinned, data-only **PEM reader**, an analyzer in the sense of §5.9 that never executes content or instantiates objects from it (T2), derives in each state from those units' content, for every family and notice: identity, kind, state, authority binding, recorded owner route, notice normative status, applicability tags, typed applicability bindings where the schema defines them, and lineage relations; and the **reader state**, `READABLE`, or `UNREADABLE` with a cause (absent, unparseable, unsupported schema, partial or conflicting composition). These **PEM facts** are S3: cached only in the derived index, rebuilt like derived relations, never stored in a record (P3). No copy of memory exists, so none can disagree with it. The reader is not schema authority: what it cannot read with certainty makes it `UNREADABLE`, never a guess. In the admitted state the PEM units' content is the **accepted PEM publication**, which policy declares the project's PEM publication line by naming `pem_root`; in a frame `D_n[X]` (§7) a candidate's changes to them are a **candidate overlay**, visible only in that frame. When the root's project identity differs from the project identity genesis records (§19.9), every entry is **foreign**: shown as external or historical evidence, never an owner-bound candidate, its owner routes unresolved, until project governance reconciles lineage and the root records it.
>
> **(b) Occasions.** Machinery detects these occasions of the PEM activation predicate, each in its own clause's words:
>
> | Occasion | Detected from | Effect |
> |---|---|---|
> | a plan item explicitly binds relevant memory | the item contract's `memory.bind` (§13.1), whose relevance plan acceptance judged | memory **activated** |
> | migration | item kind `MIGRATE`, or `change_intent` contains `migration` | **assessment** |
> | rework of mature semantics or concretization; replacement or consolidation of mature machinery; optimization or scaling | `change_intent` contains `rework`, `replacement`, `consolidation`, `optimization` or `scaling`; or the write scope intersects units policy tags `mature` | **assessment** |
> | revert or restoration | `change_intent` contains `revert` or `restoration`; or, on the candidate, a unit of its effect-keyed write set returns to a revision it held at an earlier admitted position other than its current one, or the candidate restores a subject (§19.4) | **assessment** |
> | recurrence | recurrence detection (§15.7), on the `COORDINATE` decision it creates | **assessment** |
> | any further occasion policy adds as a trigger (§5.1), for example a non-empty tag match | policy | **assessment** |
>
> An assessment occasion never activates memory by itself; it requires the task to judge the clause's qualifier ("substantial", "mature", "where prior choices matter"). Occasions machinery cannot detect stay agent judgment under the injected owner text (E3): suspected recurrence that detection has not found; history that can materially change a decision; a revert, restoration or recovery neither declared nor byte-identical. An agent may activate memory on any task and returns a HAS when it does.
>
> **(c) What a task owes.** When any occasion fires, the brief carries the PEM owner text (§16.3) and the candidates of (d) as `HISTORICAL` items with their match path and binding state, and the result owes two slots (§13.5). `pem_activation` holds one answer per fired assessment occasion: activates or not, with a content reference to the reason. `historical_applicability` is owed when the binding occasion fires or any answer activates: a content reference to the HAS in its canonical shape (in the durable home the governing work names, otherwise the result envelope), whose typed part is the three `pem_basis` identities and each dispositioned entry's identity and disposition; reasons stay in the home (§16.4). `HARD` `OBLIGATION` templates check that every fired occasion has an answer, that the HAS dispositions every candidate the recorded brief listed (§16.4), and that its basis identities are those of the state it was made in. They establish presence, coverage and identity only; whether a judgment, a disposition or the search behind it is adequate is review's (E3). Candidates are a floor: the bounded canonical-metadata search the PEM owner requires is still owed whenever memory is activated. An occasion detected only on the candidate (a revert, a restoration) triggers the slots at conformance, and a result without them is `INCOMPLETE` (§14.4).
>
> **(d) Candidates.** In a state, a task's candidates are: (1) the entries its contract binds; (2) **owner-bound** entries: `AUTHORITY_BOUND` families, owner-recorded `PROPOSED_FOR_PROMOTION` families and normative notices whose owner route resolves (e) to a unit the brief carries as `GOVERNING` (§16.2), whatever their binding state; (3) **typed matches**, where the schema defines owner or surface bindings: those resolving to a unit of the task's subjects or write scope (mechanism and regime bindings are shown, never matched, because SSDS holds no mechanism or regime facts); (4) **tag matches**: exact equality, after the normalization the catalogue fixes, between the contract's `memory.terms` and an entry's applicability tags. Match-path candidates (3, 4) are capped (§0.6); a truncation is shown with the omitted count, and the result says whether the agent widened its search. Owner-bound and bound candidates are never truncated. In a frame, the candidates are the union of those derived from the accepted publication and from the overlay, each entry the overlay changes or retires marked so. Foreign entries are never owner-bound or typed candidates. Completeness is declared only for owner-bound candidates and only over resolved routes; an empty candidate set is rendered "no candidate", never "no applicable memory" (S5).
>
> **(e) Owner bindings and reverse impact.** An owner route **resolves** when it names this project and its path and section locate a governed unit (§1.11); the entry is then bound to that unit at the content the route's revision gives it. A route that names this project and locates no unit is **unresolved**; one naming another project is **external**. A resolved binding is **current** in a state iff the unit's content there is the bound content or is reached from it by a path of current `EDITORIAL` or `REPRESENTATION` equivalence judgments (§4.4); otherwise it is **stale**. Machinery decides only byte identity, so every other owner change is stale until an equivalence judgment says otherwise (failing closed). A stale, unresolved or external binding is never shown as healthy: wherever the entry appears (candidates, `HISTORICAL` items, `memory(x)`), its binding state is shown, and the PEM owner's rule that an unhealthy binding carries no retained force applies. Each stale binding in the admitted state derives a `COORDINATE` decision for the standing plan's principal (§12.5), keyed on the entry, the unit and the unit's current revision, whose brief carries the PEM owner and its schema-governance owner, with outcomes `AMEND` (a plan item that reconciles the entry through PEM governance: confirm, remap, downgrade or retire), `CHALLENGE` (against the owner change) or `ESCALATE`. A later owner change derives a new decision. A candidate that would make a binding stale lists it in its review brief (§16.5) and in `impact(diff)`. The entries in scope are those of (d)(2); reverse reconciliation for owner-recorded `PROPOSED_FOR_PROMOTION` families is stronger than the inherited duty, which names `AUTHORITY_BOUND` entries and normative notices. External and unresolved bindings stay under the inherited reverse-reconciliation duty (E3). Because staleness is a predicate on state, an owner change made while the reader is `UNREADABLE` is not lost: the stale binding appears once the reader reads again.
>
> **(f) Freshness.** A HAS is **fresh** in a state iff, for every entry it dispositions and every entry that would be a candidate of the task there, the PEM facts (binding state included) are those of the HAS's basis. A `HARD` `OBLIGATION` template checks freshness in the state the result is evaluated in: the candidate's frame, re-derived after every clean rebase (§11.5), or, for a result without a candidate, the admitted head at its admission. A stale HAS makes the result `INCOMPLETE` and takes that class's route (§14.4); the next iteration's brief names the entries that changed. Because integration requires clean conformance on the rebased candidate (§8.3 step 7), a memory or bound-owner advance before integration cannot close work on an obsolete HAS. After integration nothing is re-checked: later memory does not reopen closed work.
>
> **(g) Memory unavailable.** While the reader is `UNREADABLE` in the state a task is issued in, no candidate is derived and the brief states the cause. A slot owed under (c) or (h) may then be `NONE` with the typed reason `PEM_UNAVAILABLE`, and only then: the template compares the reason with the derived reader state, so the claim is corroborated by derivation and never by assertion. The review brief of that work carries the unavailability as a required review item (§16.5), so the stated uncertainty is accepted only by an independent reviewer or a human, never by machinery. Work that owes no PEM slot is unaffected: memory is never a single point of failure. While the reader is `READABLE`, the PEM owner's other fallbacks remain the agent's: dispositions may be `REVIEW_REQUIRED`, and partial coverage is handled by bounded intake or stated uncertainty (E3).
>
> **(h) Closeout learning.** The results of an item whose kind is `REPAIR`, whose `change_intent` contains `rework`, `replacement`, `consolidation`, `optimization`, `scaling`, `revert` or `restoration`, or whose candidate carries a detected revert or restoration owe the slot `closeout_learning`: `NOT_MATERIAL` (a first clean local defect with no recurrence or generalization signal, or no material change), `NO_UPDATE`, `UPDATE_PROPOSED` (a content reference to the proposed memory change) or, under (g), `NONE` with `PEM_UNAVAILABLE`; each but the last with a content reference to its reasoning. `migration` alone does not owe it, because the PEM owner's closeout clause does not name it. An `UPDATE_PROPOSED` answer derives a `COORDINATE` decision for the plan's principal with outcomes `AMEND` (a plan item that changes memory under PEM governance) or `DECLINE` with a reason. No answer writes, admits or promotes memory. An under-classified change (a material repair answered `NOT_MATERIAL`, a rework planned without an intent) is for review and for later recurrence detection; the risk is accepted (§32.2).
>
> **(i) Limits.** Machinery never judges applicability, a qualifier, recurrence, materiality, adequacy or admission; never writes, admits or promotes memory; never copies lesson text into a record or brief beyond the entry identities, enumerations and content references above; and never derives from a PEM entry an obligation that blocks or closes a D1-D4 subject. Only (e) and (h) derive decisions, and both go to a principal.

### 4.2 Pointer and consequence edits

1. **§0.6 Proposed defaults**, new row:

   > | PEM match-path candidates per task | 10 | policy | §16.11 (d) |

2. **§5.1 Fixed predicate templates**, the parenthesized policy list. Accepted: "(judgment kinds and passing outcomes, qualifications above the floors, additions to mechanical minima, required judgments, gates and evidence per domain, triggers, routing and raised floors, role narrowing, enabled templates, budgets and time bounds)". Proposed: insert "the project-memory root (§16.11)," after "triggers,".

3. **§8.3 step 7 (legality)**, after "with clean conformance for a contracted task obligation (§14.6)", add: "; clean conformance includes the freshness of a HAS the result carries (§16.11 (f))".

4. **§13.1 Schema**, after "and **escalation triggers**", add: "; optionally **memory** (`memory.bind`, entries or the project memory bound as relevant to the item, and `memory.terms`, applicability terms for candidate matching) and a **change intent** (`change_intent`, a set from `rework`, `replacement`, `consolidation`, `optimization`, `scaling`, `migration`, `revert`, `restoration`), declared by the principal and judged in plan acceptance like every other field (§16.11)".

5. **§13.4 Control tightening**, inside the tightening-direction list after "more required slots and triggers", add: "(entries added to `memory.bind` or `memory.terms`, intents added to `change_intent`)".

6. **§13.5 Result slots**, the slot vocabulary. Accepted ends "`revision_assessments` and `audit_conclusion`". Proposed: "`revision_assessments`, `audit_conclusion`, `pem_activation`, `historical_applicability` and `closeout_learning`", and after "as catalogue §13.5 lists" add: "; the three memory slots are triggered as §16.11 (c) and (h) state".

7. **§14.3 The library**, `OBLIGATION` family. Accepted: "(`HARD`: required artifact linked by a derived `TESTS` relation, required evidence realized by the designated runner on the exact candidate, evidence basis fields, slots filled, no new stubs, mutation strength)". Proposed: insert "memory occasions answered, HAS coverage and basis identity, HAS freshness, memory-unavailable reasons matching the reader state (§16.11)," after "slots filled,".

8. **§15.5 Principal decisions**, the sentence on decisions owed with no report. Accepted: "(an item-obligation route of §10.4, detected recurrence, a `REFUSED` integrated-result or specification review)". Proposed: "(an item-obligation route of §10.4, detected recurrence, a `REFUSED` integrated-result or specification review, a stale memory binding or a proposed memory update, §16.11 (e), (h))".

9. **§15.7 Recurrence**, first sentence. Accepted: "the same `HARD` template failing on the same obligation across iterations; the same finding family (template, target unit or relation family) across items; repeated discrepancies by one route." Proposed: append "; a candidate that reverts integrated work (§16.11 (b))". Add at the end of the section: "Detection never creates a memory entry; a recurrence is also a memory occasion (§16.11 (b))."

10. **§16.2 Query classes.** Row `history(x)`: replace "the PEM predicate fires" with "a memory occasion fires (§16.11)". New row after it:

    > | `memory(x)` | PEM facts bearing on `x`: owner-bound entries with binding states, tag and typed matches for given terms, the reader state and the accepted and overlay identities; `HISTORICAL`, offered on request or when a memory occasion fires (§16.11) |

    Label `HISTORICAL`: replace "offered only when the PEM predicate fires or on explicit request" with "offered only when a memory occasion fires or on explicit request (§16.11)".

11. **§16.3 Injection events**, PEM row. Accepted: "| PEM predicate: the item kind is `MIGRATE`, or the task replaces mature machinery (policy-tagged units), or recurrence detection | PEM owner, plus `HISTORICAL` items |". Proposed: "| a memory occasion (§16.11 (b)) | PEM owner, plus the candidates and `HISTORICAL` items and the memory slots of §16.11 (c) |".

12. **§16.5 Review briefs**, the list of what a review brief contains, after "the result's disclosure slots, labeled as the author's claims to test;", add: "the memory bindings the candidate would make stale and any memory-unavailable reason, the latter as a required review item (§16.11 (e), (g));".

13. **§19.8 Documents, workplans and skills after cutover**, after "Skills remain epistemic procedures and stop owning workflow transitions represented by rules.", add: "The PEM owner text is injected whole (§16.3); no memory duty is removed from it because §16.11 realizes part of it mechanically, and §29.6 lists the parts that stay judgment."

14. **§29.3 Map: role contracts**, rows added before "every entrypoint":

    > | all roles | load memory on the activation predicate's occasions; judge the qualifiers | E0 + E2 + E3 | detected occasions inject the owner and require `pem_activation` (§16.11 (b), (c)); undetectable occasions stay E3 (§29.6) |
    > | all roles | retrieve memory and record a canonical HAS covering what is materially relevant | E0 + E2 + E3 | candidates as a floor; `historical_applicability` coverage and basis checked; the search beyond candidates and every disposition judged (§16.11 (c), (d)) |
    > | all roles | refresh a HAS when the memory basis, overlay or a governing owner advances before closure | **E0** | freshness template, re-derived on every rebase; integration needs it (§16.11 (f), §8.3 step 7) |
    > | all roles | reconcile owner-bound learning when its owner changes | E1 + E3 | stale bindings shown and routed to the principal (§16.11 (e)); external and unresolved owners stay E3 |
    > | all roles | missing memory is not absence; memory is no single point of failure | **E0** + E3 | empty candidates never rendered as absence; `PEM_UNAVAILABLE` only against the derived reader state, accepted only in review (§16.11 (d), (g)) |
    > | all roles | closeout learning assessment before closure of a material repair, rework, optimization, revert or restoration | E2 + E1 + E3 | `closeout_learning` slot; `UPDATE_PROPOSED` routed to the principal (§16.11 (h)) |

15. **§29.6 Disclosed E3 duties**, add after "the adequacy of a tension search;": "whether memory activates on a detected occasion, and noticing an occasion machinery cannot detect (suspected recurrence, history that can change a decision, an undeclared partial revert or recovery); the adequacy of a HAS and of the search beyond its candidates, including partial-coverage intake; the capability-transfer map; reverse reconciliation for external or unresolved owners; whether a change was material for closeout learning;".

16. **§30**, new table row after "derived index":

    > | PEM reader and derived PEM facts (§16.11) | candidate floor, binding staleness and HAS freshness without a copy of memory | prose duties only (the 7.x load rate); a persistent projection (a mirror that can disagree); an on-demand query recorded as an observation (records a pure function of content) | keep; an analyzer, no store |

    And in "What the refinements changed", append: "Amendment A10 adds an analyzer, two contract fields, three slots and two `COORDINATE` triggers; no primitive, component, store, record kind or tier."

17. **§31.2**, append: "Amendment A10 adds the memory group of §7 of its proposal (occasions, coverage, freshness, staleness, unavailability, closeout, foreign lineage, and the absence of any memory write)."

18. **§31.9**, append to the measured costs: "memory occasions answered `activates: false` and candidates dispositioned `NOT_APPLICABLE`, per occasion and match path (precision), and accepted recurrences whose earlier task had no candidate for the recurring family (recall, read from canonical PEM at later revisions outside derivation); integrations refused for a stale HAS; stale-binding decisions per owner change (§16.11). These are retrieval-mechanism evaluation data, never PEM evidence, application episodes or input to temperature or maturity."

19. **§32.2 Residual risks**, new bullet: "Memory occasions are detected only from declared intent, policy tags, byte-identical reverts, restorations and recurrence detection: an undeclared rework or a partial revert raises no occasion, and a material repair answered `NOT_MATERIAL` owes no further closeout; review and later recurrence detection are the mitigation (§16.11 (b), (h)). Tag matching finds only exact declared terms, and every owner change without an editorial or representation equivalence makes its bindings stale (§16.11 (d), (e))."

20. **§32.3 Reopen triggers**, new bullet: "*amendment A10:* memory answers or dispositions become rote, or stale-binding decisions or HAS-freshness iterations become a material cost; the §31.9 measures show a recall gap that owner, typed and tag matching cannot close (then consider a similarity recall net producing `CANDIDATE` observations under an explicit trust decision for memory text); or the PEM schema owner rejects typed applicability bindings and tag matching proves too weak to keep (§16.11)."

21. **§33 Non-goals**, after "add registries, wrappers or fields solely to mirror inherited doctrine (the realization map of §29 is a design artifact);", add: "keep a copy, registry or database of project memory, copy lesson text into records, judge memory applicability or admission, or write memory (§16.11);".

### 4.3 What acceptance would further require (outside this Manual text)

- **Catalogue.** The mechanism of §16.11 (the reader's field list and failure causes, the revert predicate, route resolution across revisions before genesis, tag normalization, the slot schemas, the templates, the decision keys and outcomes) enters the catalogue as proposed material with register entries for G2, like every other mechanism (§0.1).
- **G2.** Implementation needs a G2 workplan change placing it in Stage D. It touches the contract schema and lint (Phase E owners), conformance templates (Phase E) and Admission legality (Phase F), so the natural place is a step after Phase F. D4 stays unauthorized until then and until the prerequisite of §8.
- **Lifecycle lines.** An `amendment_a10` header line and an `AMENDMENT A10` status block, as for A9.

## 5. Disposition of the handoff's round-4 open items

| # | Item | Disposition in A10 |
|---|---|---|
| 1 | §2 paraphrase ("intake **or** `REVIEW_REQUIRED`"); A.5 restriction as stronger rule; partial coverage in retention | §2 quotes the "or". The A.5 restriction becomes: a `PEM_UNAVAILABLE` reason only where the derived reader state is `UNREADABLE`; while readable, `REVIEW_REQUIRED` dispositions and partial-coverage handling stay the agent's (§16.11 (g)), so no stronger rule is needed. Partial-coverage intake is in §29.6. |
| 2 | Overlay edits other than retirement can drop a base candidate | Candidates in a frame are the union of base- and overlay-derived, changed or retired entries marked (§16.11 (d)). |
| 3 | Closure-time freshness depends on observation timing | Freshness is evaluated in the state the result is evaluated in and re-derived on every rebase; integration needs it (§16.11 (f)). No observation is involved. |
| 4 | Realized-class row double-counts | There is no realized class. Only a revert or restoration is detected on the candidate; if the task already answered that occasion at issue, the answer covers it (one answer per occasion). |
| 5 | Item E recall needs family recurrence facts not mirrored | Recall is a §31.9 measurement that reads canonical PEM at later revisions outside derivation. |
| 6 | Binding-discovery obligation: which closure it blocks | Not needed: staleness is a state predicate (§16.11 (e)). |
| 7 | Wording ("normative notices"; 6.6 not 6.3; "inputs"; criterion 23) | "Normative notices" used throughout; the governing version is 7.2.1; the §37.2a and criterion 23 references belong to the archived design and are not carried. |
| 8 | Recovery not identifiable by action type | Declared as `restoration`, otherwise E3 (§16.11 (b), §29.6). |

## 6. What is not carried, and why

- **Envelope tiers and fields** (`pem_trigger`, `pem_context`, `facts_identity`, `pem_uncertainty`): SSDS's delegation return is the `TASK_RESULT` with typed slots (§13.5), and the brief is recorded by content identity (§16.4), so the issued candidate set is already replayable.
- **`facts_state: MISMATCH`, rebuild obligation, reconciliation state outside PEM facts:** nothing is mirrored (§16.11 (a)).
- **Memory-review and HAS-refresh obligations:** replaced by a required review item and by the freshness template on existing routes.
- **Result-declared `change_class`:** replaced by planning-time `change_intent` plus detection; a result declaring its own class would be the author classifying its own work, which review already judges.
- **Candidate match as a default occasion:** the activation predicate does not name it, and §16.3 carries only triggered duties. Policy may add it as a trigger (open decision 2).
- **Phase G retention rule and criterion 25:** the archived design's; §19.8, §29 and §31 carry the substance.
- **Item C:** PEM schema doctrine, owned by the protocol repository; see the companion proposal.
- **Item F:** a reopen trigger only (§32.3).

## 7. Qualification discriminators to carry to G2

Each is a case a shallow realization passes and a correct one fails. Mechanical properties need executable cases at the real owners; adequacy needs review.

1. A `MIGRATE` item, a `change_intent` of `optimization`, a write scope touching a `mature`-tagged unit, and a recurrence decision each require one `pem_activation` answer per occasion; an item with none of these requires none, and its brief carries no PEM owner text.
2. A `memory.bind` contract requires `historical_applicability` whatever `pem_activation` says; an all-`false` assessment with reasons requires no HAS.
3. A HAS missing a disposition for one listed candidate makes the result `INCOMPLETE`; coverage is checked against the recorded brief's candidates, not a recomputed set.
4. A candidate that reverts a unit to an earlier admitted revision raises the revert occasion at conformance and owes `closeout_learning`; a partial revert does not (disclosed, §32.2).
5. An accepted PEM change to a dispositioned entry, or a new entry that becomes a candidate, after the result's admission and before integration, makes the rebased candidate `INCOMPLETE`; the same change after integration reopens nothing; an unrelated PEM change makes nothing stale.
6. An owner unit change without an equivalence makes its bindings stale and derives one `COORDINATE` decision per binding; an `EDITORIAL` equivalence on the hop leaves it current; a second owner change derives a new decision.
7. An owner change made while the PEM root is unparseable produces the stale binding once the root parses again.
8. A route naming another project is external and never an owner-bound candidate; a PEM root naming another project makes every entry foreign (this repository's PEM today).
9. `PEM_UNAVAILABLE` is rejected while the reader is `READABLE`, accepted while `UNREADABLE`, and appears as a required review item; an item owing no PEM slot proceeds while memory is unreadable.
10. Owner-bound candidates survive any cap; match-path truncation is shown with the omitted count.
11. In a frame whose overlay retires or narrows a base entry, that entry is still a candidate, marked.
12. `REPAIR` with `NOT_MATERIAL` derives nothing; `UPDATE_PROPOSED` derives a principal decision and writes nothing; `migration` alone owes no `closeout_learning`.
13. No ledger record, brief section or derived-index entry contains lesson text, and removing every memory template leaves every non-memory admission decision unchanged.
14. Semantic (review): a trivial revert answered `activates: false` with a sound reason passes review; a decisive untagged entry missing from a HAS with an empty candidate set fails review; a complete but wrong HAS passes the templates and fails review.

## 8. Prerequisite: the SSDS PEM lineage

The repository's `PROJECT-ENGINEERING-MEMORY.md` (blob `1561797125622f355f84eb27319f87e8fa4227d9` on `main` at `af045575` and on this branch) records `project_id: hjin98-scientific-software-development-protocol`, `repository: hjin98/scientific-software-development-protocol`, `maintained_under_protocol: 6.5.0` and an accepted base `23e46543…` from the protocol line, and `PC-001`'s owner route names the protocol repository. Under the PEM owner's scope rule, inherited entries are external or historical evidence until project governance reconciles lineage. Under §16.11 (a) and (e) every entry of this PEM is therefore foreign and every owner route external: the mechanism would derive no owner-bound candidate and no stale binding here.

**Prerequisite.** Before any D4 work for the derived PEM facts (§16.11 (a), (d), (e)), project governance reconciles the lineage of this repository's PEM: either declares lineage continuity with the protocol project's memory for this repository and remaps owner routes to this repository where the owners now live here, or starts this project's own memory with the protocol entries kept as external evidence. Either is a PEM change under PEM governance, outside this amendment, and edits neither `PROJECT-ENGINEERING-MEMORY.md` nor its validator now. The G2 workplan's bound PEM basis (its §1 "Bindings", row "PEM basis") is unaffected.

## 9. Open decisions for the stakeholder

1. **Realization.** Derive PEM facts with a pinned reader from repository content (this proposal), instead of the handoff's persistent projection or recorded query. Recommended: yes; it removes the mismatch, rebuild and discovery machinery.
2. **Candidate match as an occasion.** Off by default, policy may add it (this proposal), or always on (the handoff). Recommended: off; the predicate does not name it and §16.3 carries only triggered duties.
3. **Contract fields.** Add `change_intent` and `memory` (`bind`, `terms`), or a subset. Without `change_intent`, optimization, scaling and rework are not detectable and closeout learning falls back to `REPAIR` items only; without `memory.terms`, there is no tag match. Recommended: both.
4. **`PROPOSED_FOR_PROMOTION` in reverse impact.** Keep this rule, which is stronger than the inherited duty, or limit to `AUTHORITY_BOUND` entries and normative notices. Recommended: keep (low cost; a moved owner usually moots or changes a promotion proposal).
5. **Stale-HAS route.** Use the existing `INCOMPLETE` route (an iteration, within budget), or add a lighter refresh route, which would change §10.4. Recommended: the existing route, with the §32.3 trigger.
6. **Candidate cap.** Proposed default 10 match-path candidates per task.
7. **Form of the proposal.** Review this standalone file, or first write it into the Manual with PROPOSED status lines as A9 was. This file follows the instruction not to change the accepted Manual's text.
8. **Placement.** Where in Stage D the implementation goes (§4.3; after Phase F recommended), once the amendment is accepted.
9. **PEM lineage (§8).** Which reconciliation project governance chooses, and when.
10. **Item C.** Whether and when to open the companion proposal in the protocol repository.
11. **Review.** Approval of the different-family Review run.
