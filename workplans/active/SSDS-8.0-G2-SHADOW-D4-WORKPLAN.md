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
NEXT ACTION: Manual amendments A1 and A2 (SD-51, SD-52) await one GPT-family delta review and acceptance (§4.6, §4.8); S4 and S5 proceed meanwhile.
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

One row per catalogue subsection: catalogue section, disposition (`ACCEPT`, `REPLACE` with the replacement, or `DROP` with the reason), the Manual decision it realizes, model evidence (path and result), and the register entries it closes. A `REPLACE` that is simpler than the catalogue clause is preferred to an `ACCEPT` of a complicated one. Rows added by S2 (2026-10-18); evidence is `python3 -I qualification/ssds80/models/run_models.py --seeds` (S2 families in `models/judgment.py` and `models/cases_s2.py`, item cases in `models/cases.py`).

| Catalogue § | Disposition | Realizes Manual § | Evidence | Closes |
|---|---|---|---|---|
| §3.4 `REVIEW` and `CONFORMANCE` target rows | **REPLACE**: three typed targets with distinct identities — a transformation `id(X)` (with the contract item revision for `CONFORMANCE`); a subject triple; an integrated result named by its kind (item-level, joint invariant, high consequence), its subject (item revision, invariant, surface) and the change or part integrations that derived it | §3.4 | target cases (a joint-invariant or high-consequence review of X answers nothing about `REVIEW(X)`; relief stays on its typed target) | RR-3 |
| §4.3 `REVIEW`, `CONFORMANCE` row | **REPLACE** the judged-content entries: a `content` entry on every unit of `W` for the target's type (§5.10 (b)), in place of the `J`, retained-unit and "latest outputs" clauses; **ACCEPT** the rest of the row (before-images, contract, governing closure, task-result and evidence records, identity of what is only shown), split by target type | §4.3, §5.10 (b) | item and transformation cases | RR-1, RR-3 |
| §5.10 (a) judged scope `J`, retained units `U_X` | **REPLACE** by `W`: the content, at the target's state, of every unit in the target's scope that the work changed, the work keyed on the producing task's prose and fixed fields; for a transformation it is computed from `id(X)`'s base, change and its one producing context, so it is the same for every judgment of `X` | §5.10 (b) | 7 transformation cases (no over-exclusion by same-key work in another scope; retained work kept) | RR-2 |
| §5.10 (a) `authors(x)` and the independence test | **ACCEPT**, read over `W` | §5.10 (b), (f) | item, transformation and route cases | RR-1, RR-2 |
| §5.10 (a) owner exception | **REPLACE** by the narrow exception: an authenticated owner's disposition of a failing assessment only | §5.10 (f) (SD-48) | S1 objection cases; `failing_disposition_exception`, `author_owner_waits` | RR-11 (exception scope) |
| §5.10 (b) `REVIEW` of a transformation and `CONFORMANCE` reach rows | **REPLACE** `J` by `W` in the containment test; **ACCEPT** the empty-scope rule and per-target relief | §5.10 (c) | S1 history cases; route cases | RR-1, RR-2 |
| §5.10 (c) objection, (e) enforcement points, (f) S3 consequences | **ACCEPT** | §5.10 (d), (f), (g) | — (unchanged by S2) | — |
| §5.10 (d) the four routes | **ACCEPT**, with each route's independence measured over what its record judges (the objection's `W` for reassessment, supersession and adjudication; the relieved target's `W` for relief) and its record acting where the veto bites (§5.2, §7.5) | §5.10 (e), (f) | route cases (`reached_larger_judged_set`, `abandoned_review_frame`, `relief_basis_moved`) | RR-11 (routes) |
| §5.10 (g) invariants | **REPLACE** by the Manual's (h) 1-9 | §5.10 (h) | S1 and S2 cases | — |
| §5.10 (d)/(h)(4) liftable or waiting, per state | **ACCEPT** the per-route, per-state waiting state, realizing Manual amendment A1 (SD-51; pending its review and acceptance): an objection or obligation waits on human attention when no actor is eligible for any route there | §5.10 (f), (h)(4) as amended | `G1_QUESTIONS` in `cases_s2.py`: the dddfedf reading reproduces the gap, the amended one closes it | RR-11 (waiting), pending A1's acceptance |
| §7.1 transformation identity "fixed by the task result that first submits the candidate"; §5.2 a later identical submission joins that enactment | **ACCEPT** with one addition: a result submitting an already-bound `(B, C, A)` under a different scope or work key is refused (`REF_*` family), so each identity has one producing context | §5.10 (b) ("a fact of `id(X)`") | binding cases | RR-2 (context discriminator) |
| §8.3 step 2 retained-field recomputation | **DROP**: there is no `retained` field | §5.10 (b) | transformation cases | RR-2 |
| §8.3 step 3 independence and supersession authority | **ACCEPT**, with the narrow owner exception | §5.10 (f) | S1 objection cases | RR-11 |
| §8.3 step 7 `STALE_RETAINED` | **REPLACE** by the judged-content support check: an integration is refused, as a new iteration, when `W` recomputed over the merged state differs from the reviewed `W`. Narrower than `STALE_RETAINED` (a same-key integration outside the scope no longer refuses) and wider than it (a foreign change to judged content refuses) | §5.10 (b), §8.3 step 7 | `same_key_other_scope_after_issue`, `same_key_in_scope_after_issue`, `foreign_in_scope_after_issue`, `unrelated_after_issue` | RR-2 |
| §12.2 envelope `retained` field | **DROP** | §12.2 | — | RR-2 |
| §13.7 item-level review target and entries | **REPLACE** by the typed integrated-result target and `W` over the item revision's work in its scope | §13.7, §5.10 (b) | 11 item cases | RR-1 |
| §16.5 reviewer selection "independent of `authors(J)`" | **REPLACE** `J` by `W` | §16.5 | — | RR-1, RR-2 |
| §10.4 the pending candidate (route 3) | **REPLACE**: the pending candidate is the latest iteration's candidate while it is open (result complete, not integrated or refused, no adverse answer to its review); a rejected, `INCOMPLETE` or `PARTIAL` iteration is closed by its own iteration route, so it never masks drift | §10.4 (a pending candidate keeps its own routes; drift re-dispatches) | S3 `rejected_candidate_not_pending`, `incomplete_candidate_not_pending`, `open_candidate_keeps_its_routes` | RR-7 |
| §10.2 `COORDINATE(plan)` row and §15.5 decisions with no report | **REPLACE** the keying: a decision owed for an item route is keyed on (condition, item revision), so an amendment after which the condition still holds derives a new decision; **ACCEPT** the outcomes, and that `ESCALATE` answers no item route | §10.2, §10.3 (no stranded obligation), §15.5 | S3 `budget_answered_condition_holds`, `budget_open` | RR-5 |
| §10.4 route 4 for an item-level review naming no part; §13.7 partition | **REPLACE**: a partitioned item keeps its own obligation as the composite of its parts and the item-level review; its predicate fails while the item-level review is adverse, and it carries route 4's `COORDINATE(plan)` for findings naming no part (a part whose outputs are named takes its own route) | §10.4, §13.7 | S3 `item_level_no_part`, `partitioned_all_good` | RR-6 |
| §10.4 route 4 for out-of-scope adverse reviews | **REPLACE**: every standing out-of-scope adverse review of any integrated enactment is admitted as a routed finding (its out-of-scope findings are report records, Manual §15.1) with its own `COORDINATE(plan)` keyed on that review, beside the item's single route; for the latest enactment, when no open candidate is pending, that decision is also the item's route 4; an answered one lets the item's route continue | §10.4 (findings never retired), A8, §15.1 | S3 `oos_on_earlier_enactment`, `oos_latest_masked_by_pending`, `oos_latest`, `oos_latest_answered` | RR-8 |
| §10.4 item-obligation identity under an R2 amendment keeping the prose and fixed fields | **REPLACE** by the identity key, realizing Manual amendment A2 (SD-52; pending its review and acceptance): a tightening or a loosening-only amendment keeps the obligation, `out(o)`, subjects and iteration count, the loosened item waiting for a new plan acceptance; only a prose or fixed-field change derives a new obligation | §10.4 as amended | `IDENTITY_CASES` in `cases_s3.py` (a direct test of the decision; its routing consequences are the S3 budget and drift cases) | RR-4, pending A2's acceptance |

### 4.3 Stop rules

- A model showing that no mechanism can realize a Manual decision, or that two Manual decisions conflict, stops that step and reopens G1 at the Manual's owner, with the stakeholder choosing the direction.
- A family of mechanism counterexamples that recurs after a repair triggers simplification of that family before another additive repair, and the stakeholder chooses when the options differ materially (Phase C convergence rule).
- A step that becomes implementation-like (building production components) has left Stage S; it waits for G2.

### 4.4 S1 result (2026-10-18)

The framework is `qualification/ssds80/models/` (`framework.py`: history replay, provenance, the item-level target, actors, policy and the enumeration of admissible independent ending routes; `rules.py`: one rule set per candidate reading, differing only where the candidates differ; `cases.py`: cases whose expectations are written from the Manual's decisions and A5, each naming the rule sets it refutes; `run_models.py`: the runner). Run `python3 -I qualification/ssds80/models/run_models.py --seeds`.

Result: 11 item-level cases and 12 objection cases; framework self-tests pass; the accepted Manual's rule set meets every case; and every known counterexample is reproduced as a failure of the rule it refuted: the 9431629 B1 histories and their drift sibling (candidate 61's latest-change entries), the SD-46 replaced-part and copy cases (SD-46's first wording and candidate 61), the f044820 B1 author-owner trajectory over seven target kinds and its human-reviewer sibling (the general owner exception of candidates 61 and 62), and the 8c1f2f2 B1 no-eligible-judge state with its unknown-lineage sibling (the unconditional liftability invariant of candidates 61-63). The regression seeds pass: `item_review_history_probe.py`, and the review-scope and obligation-routing families of `judgment_disagreement_model_check.py`.

What S1 can discriminate: judged-content selection from explicit histories and its authors; the owner exception's scope; route admissibility and independence for a policy and authorship; whether a stated liftability invariant holds in the waiting state. What it cannot: challenge-tier polarity, acting and frames, supersession chains, basis currency, admission order, routing, evidence disagreement, or any production consumer; and its expectations are the author's reading of the Manual, so a shared misreading would agree on both sides (independent Review checks that). RR-10 is not closed by S1: S2-S4 must extend the framework to the transformation scope (RR-2), target typing (RR-3), state-local route eligibility with acting and basis admissibility (RR-11, dddfedf N4) and routing (RR-4 to RR-8) before the old diagnostic stops being the only coverage of those layers.

### 4.5 S2 result (2026-10-18)

The framework gained `models/judgment.py` (transformation `W` and the integration support check, the one-context binding, typed targets with answering and relief, and route enumeration per state: independence over what each route record judges, acting per Manual §5.2 and §7.5, relief basis) and `models/cases_s2.py` (7 transformation, 3 binding, 5 target and 7 route cases, expectations written from the Manual). Result: the settled mechanism meets all 22 S2 cases and the S1 cases; the catalogue's reading misses the 11 S2 cases that name it (over-exclusion by same-key work in another scope, `STALE_RETAINED`'s over-refusal, two producing contexts for one identity, the joint-invariant and high-consequence target collisions, relief across colliding targets, and four route-eligibility cases); seeds pass. §4.2's rows record the dispositions. RR-1, RR-2 and RR-3 are settled pending this workplan's Review; RR-11 is settled except the waiting state, which is blocked on Q1.

### 4.6 G1 question Q1 (resolved by SD-51; amendment A1 pending review and acceptance)

S2's route model found a lawful state in which the accepted Manual's §5.10 (h)(4) ("liftable or waiting") is false if §5.10 (f)'s "No eligible judge" is read as written. A standing NO-PASS was recorded in the frame of transformation X, which was abandoned; it vetoes the passing review of a re-dispatch Z that keeps the rejected content. Its author was an agent whose task has ended. The owner O is qualified and did not author the NO-PASS's judged content, but a supersession of a judgment about X must declare X's frame (§7.5) and so never acts in Z's; O authored part of Z's judged content, so O cannot relieve Z's review; the policy adjudicator H authored the NO-PASS's content. No route record can act there. Yet (f) says an obligation waits only when every qualified actor is among the authors, which O is not; so the state neither has an ending record nor is waiting. Read per route and per state ("no eligible independent judge for any of those routes exists there", as (h)(4) words it), the objection waits and (h)(4) holds. The model case is `G1_QUESTIONS` in `models/cases_s2.py`; the runner prints both readings. By §4.3 this reopened G1 at §5.10. The stakeholder chose SD-51 (record item 47): amend §5.10 (f) so that eligibility is per route and per state (independent of what the route's record judges, acting there, basis admissible). Amendment A1 makes that change in §5.10 (f), (h)(4), §10.2 and §10.3; its GPT-family review of the delta and the stakeholder's acceptance are pending, and until then the dddfedf text governs. The runner now requires the dddfedf reading to reproduce the gap and the amended reading to close it.

### 4.7 S3 result (2026-10-18)

`models/routing.py` models an item obligation after integration (fence, predicate, iteration candidates, budget, partition and item-level review, out-of-scope adverse reviews, answered decisions) and derives its single route and the open decision obligations under the catalogue's reading and the settled one; `models/cases_s3.py` holds 13 cases with expectations from the Manual's principles (no stranded obligation, findings survive to their owner and are never retired by a later obligation, a pending candidate keeps its routes, drift re-dispatches). The settled routing meets all 13; the catalogue's misses every case that names it. RR-5 to RR-8 are settled pending this workplan's Review (§4.2). RR-4 is not a routing mechanism: it is G1 question Q2.

### 4.8 G1 question Q2 (resolved by SD-52; amendment A2 pending review and acceptance)

Manual §10.4 says an item obligation's identity is "its item and the prose and fixed fields of its accepted revision", and that "an R1 tightening keeps it and an R2 amendment derives a new one". By §13.4 an amendment that only loosens a tightenable field (a wider write scope, a larger budget, fewer frozen symbols) is R2, yet keeps the prose and fixed fields. There the two statements disagree: the key keeps the obligation (its `out(o)`, its subjects and its iteration count); the R2 clause derives a new obligation (empty `out(o)`, a fresh budget). No mechanism satisfies both, so the Manual must say which; this is the SD-41 residual (a), now reached by S3. By §4.3 it reopened G1 at §10.4. The stakeholder chose SD-52 (record item 48): the identity key governs; a loosening-only amendment keeps the obligation and waits for a new plan acceptance; only a prose or fixed-field change derives a new obligation. Amendment A2 makes that change in §4.1 and §10.4 and is folded into A1 for one delta review.

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
| Stage S | S1 done (§4.4); S2 done, its waiting row pending A1 (§4.5, §4.6); S3 done, its identity row pending A2 (§4.7, §4.8); S4-S5 not started |
| Stage D | not authorized |
| G2 | open |
