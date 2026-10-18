---
kind: ssds-shadow-d3-d4-workplan
workplan_id: SSDS-8.0-G2-SHADOW-D4-WORKPLAN
protocol_version: 7.2.1
target_system_version: 8.0.0
status: proposed
created_date: 2026-10-18
revised_date: 2026-10-18
revision: 0
governing_architecture: orchestrator/docs/ssds-8.0-architecture.md (accepted at G1, SD-50; semantic candidate dddfedf72ed9711b8fcd46865b5c99eb50771ac5)
governing_workplan: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md (design revision 24, accepted at G1)
mechanism_input: orchestrator/docs/ssds-8.0-mechanism-catalogue.md (non-authoritative; residual register RR-1 to RR-11)
stakeholder_record: qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md (item 46, SD-50)
gate: G2-open
implementation_handoff: not-authorized
active_serious_challenge: none
---

Governing SSDP version: 7.2.1.

# SSDS 8.0 — G2 shadow D3->D4 workplan

```text
STATUS: PROPOSED, revision 0 (opened 2026-10-18 under SD-50). Not reviewed. Not authorized.
GATE: G2 (workplan §25 criteria 13-14) is OPEN. SSDS 8 D4 is NOT AUTHORIZED: nothing in this file
      authorizes implementation until it is independently reviewed and the stakeholder explicitly
      authorizes shadow implementation.
GOVERNS: the settlement of the mechanism catalogue against executable design models (Stage S, now) and
         the plan for shadow implementation, Phases D-H (Stage D, only after G2).
DOES NOT GOVERN: architecture (the accepted Manual owns it), any subject's governance (no SSDS authority
                 over any subject before G4), cutover, the frozen Level 0 Core or SSDP protocol source.
NEXT ACTION: Stage S steps S2 and S3 (§4.1); S1 is done (§4.4).
```

## 0. Purpose and authority

Gate G1 accepted the SSDS 8 Architecture Manual and workplan design revision 24 (SD-50, stakeholder decision record item 46). Gate G2 needs two things (workplan §25):

- **criterion 13:** a D3->D4 workplan for the shadow phases, derived from the accepted Manual and independently reviewed, that accepts, replaces or drops each mechanism-catalogue entry against executable models, closes every residual-register entry, and bounds its scope to shadow operation (no SSDS authority over any subject, no cutover, the document-controlled baseline governing);
- **criterion 14:** the stakeholder's explicit authorization of that shadow implementation.

This file is that workplan, from its opening revision. It is a D3 cycle contract. Its Stage S produces design evidence (executable models of the Manual's decisions, under `qualification/ssds80/`), which the accepted architecture and the G1 Reviews treat as diagnostic design work, not implementation of native authority. Its Stage D is a plan only until G2.

**Authority order.** The accepted Manual owns every architecture decision, invariant and authority boundary; this workplan never changes one. Where settling a mechanism shows that a Manual decision is unrealizable, contradictory or inadequate, the work stops on that point and G1 reopens at the Manual's owner (workplan §25 criterion 11; Manual §32.3). The catalogue is input: a catalogue mechanism binds nothing until this workplan accepts it, and then only as a cycle-scoped concretization (SSDP workflow owner, "Durable authority vs cycle freeze"), never as architecture.

## 1. Bindings

| Binding | Identity |
|---|---|
| governing protocol | SSDP 7.2.1; public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`, resolved from `PROTOCOL-RELEASE-STATE.yaml` |
| accepted architecture | Manual semantic candidate `dddfedf72ed9711b8fcd46865b5c99eb50771ac5`, blob `b4077eb5879570b0aee56b068be8588beeaa5e9e`; G1 Review `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-DDDFEDF-DIFFERENT-FAMILY-PASS.md` |
| accepted cycle contract | architecture workplan design revision 24, blob `11b1462b20dac578af5e3e14f9df616a1da424d0` |
| mechanism input | catalogue blob `31d7a8a3477a9a0c127786f75b698959bc313cd4` (body: Manual candidate 61 text verbatim; register C.2) |
| accepted defaults | Manual §0.6, as proposed (SD-50) |
| PEM basis | `main` at `af0455753e20ee54a969c844872e29e270007211`, `PROJECT-ENGINEERING-MEMORY.md` blob `1561797125622f355f84eb27319f87e8fa4227d9`; no overlay; HAS PC-001, DS-001, SP-001, SP-002, FF-001 as the G1 Reviews recorded |
| pre-cutover baseline | the document-controlled protocol resolved from `PROTOCOL-RELEASE-STATE.yaml` (7.2.1) keeps governing every subject throughout this workplan |

## 2. Invariants and constraints for every stage

1. **Shadow only.** No SSDS component holds authority over any subject. A shadow genesis declares every subject `LEGACY(p)` or `UNGOVERNED` (Manual §19.9); SSDS derives, renders and records beside document control and never gates it. No `NATIVE` mode, no cutover, no `MODE_TRANSITION` to `NATIVE` (that is G4, per subject).
2. **Architecture fixed.** Every Manual decision and invariant holds; a mechanism is acceptable only if a model shows it realizes them on the stated cases. No mechanism is accepted because it exists, recurs, passes tests or was reviewed (SSDP kernel, "Feasibility, authority, and delegation").
3. **Simplification first.** Prefer removing, narrowing or consolidating a catalogue mechanism over adding one; the SD-47 lesson applies to mechanism as it did to the Manual (convergence owner, "Active simplification trigger").
4. **Real owners for claims.** A model qualifies only the property its method discriminates (DS-001). Stage S models are design evidence; production-owner evidence is Stage D's (G3).
5. **Independent oracles.** Every model's expectations are stated from the Manual's decisions or from recorded histories, never computed by the rule under test (register RR-10).
6. **Frozen surfaces.** No change to protocol `source/`, `dist/`, profiles, snapshots, the frozen `orchestrator/docs/architecture.md` (Architecture 1.6.0) or the Level 0 Core's accepted behavior (PC-001).
7. **Repository discipline.** Work and push only on branch `ssds-8.0-graph-native-architecture`; no pull request, merge or campaign; no model names or identifiers in artifacts; review records name the model family only.

## 3. Non-goals

Changing the architecture; native governance of any subject; cutover or rollback execution; performance tuning before correctness; a general rule language; hosted services; claims of burden reduction or doctrine improvement before the Stage D measurements (Manual §31.9).

## 4. Stage S — settle the mechanism catalogue (before G2; design evidence)

### 4.1 Steps, in order

| Step | Scope | Output | Done when |
|---|---|---|---|
| **S1** | Model framework (RR-10). Replace the hand-tabled diagnostic's confidence route with executable design models under `qualification/ssds80/models/`: a ledger-and-history generator, the Manual's decisions as independently stated expectations, and per-state evaluation; the existing `judgment_disagreement_model_check.py` and `item_review_history_probe.py` become regression seeds, not oracles. | framework, its own self-tests, and a statement of what each model can and cannot discriminate | the framework reproduces the known counterexamples (9431629 B1, the SD-46 cases, f044820 B1, 8c1f2f2 B1) as failures of the earlier rules and passes them under the Manual's rules |
| **S2** | Judgment layer: RR-1 (item-level judged content from integration histories), RR-2 (transformation judged content; whether the `retained` envelope field, the step-2 check and `STALE_RETAINED` remain needed or reduce to transformation identity and rebase staleness; one producing context per `(B, C, A)`), RR-3 (three disjoint review target types with answering, supersession, relief and `REFUSED` per type), RR-11 (the narrow owner exception, missing-judge waiting, per-state route eligibility and later relief, with a resolver-policy matrix). | a disposition (accept, replace or drop) of every catalogue clause in body §3.4, §4.3, §5.10, §8.3 steps 2-3 and 7, §12.2 and §13.7, each with its model evidence | every case named in register RR-1, RR-2, RR-3 and RR-11 and in the four G1 Reviews' discriminators runs under the chosen mechanism with the Manual's expected outcome |
| **S3** | Routing: RR-4 to RR-8 (identity under a prose-keeping R2 amendment; a no-change coordination answer; unattributed item-level findings; a never-ending pending candidate; out-of-scope findings on masked or non-latest enactments), keeping §10.3's no-stranded-obligation invariant. | a disposition of catalogue body §10.2-§10.4 and §15.5 | each residual has a route that a state-transition model shows terminating or waiting visibly, or the Manual decision it would need is reported for G1 |
| **S4** | Historical replay (RR-9): each B and N finding of the earlier Manual and workplan Review records that concerns mechanism, replayed against the S1-S3 models. | a replay table: closed by the settled mechanism, not applicable after SD-47, or open with its owner | every finding has one of those dispositions with evidence |
| **S5** | Remaining catalogue sections in dependency order: units and manifest (§1), relations (§2), records and schema (§3), basis (§4), derivation strata (§5.1-§5.9), assessment disagreement (§6), frames (§7), admission (§8), concurrency (§9), plans, roles, contracts, conformance, reports (§11-§15), interface (§16), evidence (§17), intake (§18), migration (§19), external units (§20), storage, publication, currentness, confidentiality, trust (§21-§25), components and evolution (§26-§28). | a disposition per subsection, with model evidence where the subsection carries logic and a stated reason where it is a data format | no catalogue subsection lacks a disposition |
| **S6** | Stage D plan made concrete from the settled mechanism (§5), and this workplan frozen for independent Review. | revision 1 of this file with the settled-mechanism register (§4.2) complete | §6's G2 checklist is satisfiable by the frozen revision |

Steps S2 and S3 may run in parallel once S1 exists; S4 follows them; S5 may proceed section by section beside S2-S4 where it does not depend on them.

### 4.2 Settled-mechanism register (filled during Stage S)

One row per catalogue subsection: catalogue section, disposition (`ACCEPT`, `REPLACE` with the replacement, or `DROP` with the reason), the Manual decision it realizes, model evidence (path and result), and the register entries it closes. A `REPLACE` that is simpler than the catalogue clause is preferred to an `ACCEPT` of a complicated one. Empty at revision 0.

| Catalogue § | Disposition | Realizes Manual § | Evidence | Closes |
|---|---|---|---|---|
| — | — | — | — | — |

### 4.3 Stop rules

- A model showing that no mechanism can realize a Manual decision, or that two Manual decisions conflict, stops that step and reopens G1 at the Manual's owner, with the stakeholder choosing the direction.
- A family of mechanism counterexamples that recurs after a repair triggers simplification of that family before another additive repair, and the stakeholder chooses when the options differ materially (Phase C convergence rule).
- A step that becomes implementation-like (building production components) has left Stage S; it waits for G2.

### 4.4 S1 result (2026-10-18)

The framework is `qualification/ssds80/models/` (`framework.py`: history replay, provenance, the item-level target, actors, policy and the enumeration of admissible independent ending routes; `rules.py`: one rule set per candidate reading, differing only where the candidates differ; `cases.py`: cases whose expectations are written from the Manual's decisions and A5, each naming the rule sets it refutes; `run_models.py`: the runner). Run `python3 -I qualification/ssds80/models/run_models.py --seeds`.

Result: 11 item-level cases and 12 objection cases; framework self-tests pass; the accepted Manual's rule set meets every case; and every known counterexample is reproduced as a failure of the rule it refuted: the 9431629 B1 histories and their drift sibling (candidate 61's latest-change entries), the SD-46 replaced-part and copy cases (SD-46's first wording and candidate 61), the f044820 B1 author-owner trajectory over seven target kinds and its human-reviewer sibling (the general owner exception of candidates 61 and 62), and the 8c1f2f2 B1 no-eligible-judge state with its unknown-lineage sibling (the unconditional liftability invariant of candidates 61-63). The regression seeds pass: `item_review_history_probe.py`, and the review-scope and obligation-routing families of `judgment_disagreement_model_check.py`.

What S1 can discriminate: judged-content selection from explicit histories and its authors; the owner exception's scope; route admissibility and independence for a policy and authorship; whether a stated liftability invariant holds in the waiting state. What it cannot: challenge-tier polarity, acting and frames, supersession chains, basis currency, admission order, routing, evidence disagreement, or any production consumer; and its expectations are the author's reading of the Manual, so a shared misreading would agree on both sides (independent Review checks that). RR-10 is not closed by S1: S2-S4 must extend the framework to the transformation scope (RR-2), target typing (RR-3), state-local route eligibility with acting and basis admissibility (RR-11, dddfedf N4) and routing (RR-4 to RR-8) before the old diagnostic stops being the only coverage of those layers.

## 5. Stage D — shadow implementation plan (authorized only at G2)

Stage D follows the architecture workplan's Phases D-H (its §23). Each phase is bounded to shadow operation by §2, delivers through the accepted component boundaries (Manual §26), and is accepted only through production-owner evidence and independent implementation Review at G3 (criterion 15). The detailed acceptance program is Manual §31.2 with the catalogue's §31 discriminators as settled in Stage S.

| Phase | Scope (shadow, no authority) | Acceptance evidence at G3 |
|---|---|---|
| **D** read-only kernel | Content Model, Analyzers, ledger schema and Ledger Store, Derivation over this repository, a shadow genesis from existing history | derivation, structure and relation groups; determinism and replay; currency and widening; incremental equals from-scratch |
| **E** read-only interface and workflow layer | `open`, `ask`, `read`; briefs, contract lint, conformance views, report routing, decision briefs and the inspector, computed beside document control | interface, workflow-roles, contracts, conformance and escalation groups; live trajectories on the 7.x panel against the 7.2.1 baseline (Manual §31.9) |
| **F** Admission and Dispatcher in shadow | admission decisions computed beside document control; every material difference classified (SSDS defect, baseline defect, deliberate stronger rule, unresolved judgment) and independently reviewed | admission, publication, crash-window, currentness and loss groups with deterministic failpoints; frames end to end |
| **G** intake and migration pilot | this repository's legacy documents (Case B) and one external scientific repository (Case C/D), without disturbing production | intake, migration and refinement, cross-repository groups |
| **H** adversarial and fault qualification | the security, privacy, semantic-adversarial and fault groups | those groups; independent implementation Review |

Stage D adds no architecture. A Stage D finding that a Manual decision fails in practice is a reopen trigger for the Manual (§32.3), not a local patch.

## 6. G2 checklist

| Criterion 13 element | Where it is met |
|---|---|
| derived from the accepted Manual | §0-§2; every settled mechanism names the Manual decision it realizes (§4.2) |
| each catalogue mechanism accepted, replaced or dropped against executable models | §4.2 complete after S5 |
| every residual-register entry closed | S1 (RR-10), S2 (RR-1, RR-2, RR-3, RR-11), S3 (RR-4 to RR-8), S4 (RR-9) |
| bounded to shadow operation | §2 item 1, §5 |
| independently reviewed | the review of the frozen revision (S6), recorded in `qualification/ssds80/` |
| **Criterion 14:** explicit stakeholder authorization of the shadow implementation | recorded verbatim in the stakeholder decision record after that review |

## 7. Reopen triggers and risks

Every Manual §32.3 trigger applies. In addition: a Stage S model needs a semantic the Manual does not state (a missing architecture decision; reopen G1); the settled mechanism is materially more complex than the catalogue it replaces; Stage S cost outgrows its value for a section that is a data format (stop and record the format as accepted by inspection, with the reason).

## 8. State

| Item | State |
|---|---|
| G1 | accepted (SD-50, 2026-10-18) |
| this workplan | revision 0, proposed, unreviewed |
| Stage S | S1 done (§4.4); next S2 and S3 |
| Stage D | not authorized |
| G2 | open |
