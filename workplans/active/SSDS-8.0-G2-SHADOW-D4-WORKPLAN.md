---
kind: ssds-shadow-d3-d4-workplan
workplan_id: SSDS-8.0-G2-SHADOW-D4-WORKPLAN
protocol_version: 7.2.1
target_system_version: 8.0.0
status: proposed
created_date: 2026-10-18
revised_date: 2026-10-18
revision: 1
governing_architecture: orchestrator/docs/ssds-8.0-architecture.md (accepted at G1, SD-50, semantic candidate dddfedf72ed9711b8fcd46865b5c99eb50771ac5; amendments A1-A3 accepted, SD-53, semantic candidate 2a17a8305db5ed312dc453f9d86ccf5faee8ab74)
governing_workplan: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md (design revision 24, accepted at G1)
mechanism_input: orchestrator/docs/ssds-8.0-mechanism-catalogue.md (non-authoritative; residual register RR-1 to RR-11)
stakeholder_record: qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md (items 46-49, SD-50 to SD-53)
gate: G2-open
implementation_handoff: not-authorized
active_serious_challenge: none
---

Governing SSDP version: 7.2.1.

# SSDS 8.0 — G2 shadow D3->D4 workplan

```text
STATUS: PROPOSED, revision 1, frozen for independent Review (S6, 2026-10-18; opened under SD-50). Not
        reviewed. Not authorized.
GATE: G2 (workplan §25 criteria 13-14) is OPEN. SSDS 8 D4 is NOT AUTHORIZED: nothing in this file
      authorizes implementation until it is independently reviewed and the stakeholder explicitly
      authorizes shadow implementation.
GOVERNS: the settlement of the mechanism catalogue against executable design models (Stage S, done at revision 1) and
         the plan for shadow implementation, Phases D-H (Stage D, only after G2).
DOES NOT GOVERN: architecture (the accepted Manual owns it), any subject's governance (no SSDS authority
                 over any subject before G4), cutover, the frozen Level 0 Core or SSDP protocol source.
NEXT ACTION: independent Review of revision 1 (handoff G2-WORKPLAN-REVIEW-HANDOFF-SSDS-8.0-R1.md); then the
             stakeholder's G2 decision (criterion 14). A4 and the A1-A3 Review findings N1 and N2 wait for the
             next Manual amendment batch (§4.10).
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
| accepted architecture | Manual semantic candidate `2a17a8305db5ed312dc453f9d86ccf5faee8ab74`, blob `e90c1a4db68e9410e81eefafdcfcff92b888c57b` (G1 text `dddfedf72ed9711b8fcd46865b5c99eb50771ac5`, SD-50, with amendments A1-A3, SD-53); Reviews `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-DDDFEDF-DIFFERENT-FAMILY-PASS.md` and `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-2A17A83-A1A2A3-DIFFERENT-FAMILY-PASS.md` |
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
| **S4** | Historical replay (RR-9): each B and N finding of the earlier Manual and workplan Review records that concerns mechanism. Revision 0 asked for a replay against the S1-S3 models; those models cover only the judgment and routing layers, so S4 is an index that routes each finding to the section that owns it, and the per-finding judgment is part of that section's S5 settlement. | `G2-S4-FINDING-INDEX.md`, generated by `models/finding_index.py`: each finding closed by a named model case, or open with its owning section | every finding is in the index; S5 closes no section while a finding routed to it lacks a disposition (closed by the settled mechanism, not applicable after SD-47, or open with its owner, with evidence) |
| **S5** | Remaining catalogue sections in dependency order, each disposing of the S4 findings routed to it: units and manifest (§1), relations (§2), records and schema (§3), basis (§4), derivation strata (§5.1-§5.9), assessment disagreement (§6), frames (§7), admission (§8), concurrency (§9), plans, roles, contracts, conformance, reports (§11-§15), interface (§16), evidence (§17), intake (§18), migration (§19), external units (§20), storage, publication, currentness, confidentiality, trust (§21-§25), components and evolution (§26-§28). | a disposition per subsection, with model evidence where the subsection carries logic and a stated reason where it is a data format | no catalogue subsection lacks a disposition |
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
| §5.10 (d)/(h)(4) liftable or waiting, per state | **ACCEPT** the per-route, per-state waiting state, realizing Manual amendment A1 (SD-51, accepted SD-53): an objection or obligation waits on human attention when no actor is eligible for any route there | §5.10 (f), (h)(4) as amended | `G1_QUESTIONS` in `cases_s2.py`: the dddfedf reading reproduces the gap, the amended one closes it | RR-11 (waiting) |
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
| §10.4 item-obligation identity under an R2 amendment keeping the prose and fixed fields | **REPLACE** by the identity key, realizing Manual amendment A2 (SD-52, accepted SD-53): a tightening or a loosening-only amendment keeps the obligation, `out(o)`, subjects and iteration count, the loosened item waiting for a new plan acceptance; only a prose or fixed-field change derives a new obligation | §10.4 as amended | `IDENTITY_CASES` in `cases_s3.py` (a direct test of the decision; its routing consequences are the S3 budget and drift cases) | RR-4 |
| §1.1 unit, identity grammar, kinds | **ACCEPT** (data format; identities opaque, `ssds.` reserved) | §1.1 | inspection | — |
| §1.2 manifest location and TOML format, declaration keys, inline anchors | **ACCEPT** (data format) | §1.2 | inspection | — |
| §1.2 write set | **ACCEPT**: head-to-merged at the head where the check runs, by owned content and declarations, never by position | §1.2 (SD-14) | S5 §1 `governed_boundary`, `concurrent_admission_not_counted`, `combination_effect`, `new_part_over_existing_bytes`, `span_shift_not_a_change` | findings cc005db B1, d837363 B4, 5c55d4b B2 |
| §1.3 scope-term grammar and resolution to `ABSENT` | **ACCEPT** (grammar; pure resolvers are a Phase D analyzer test) | §1.3 | inspection; S5 §1 partition cases use `ABSENT` | — |
| §1.4 partition by construction | **ACCEPT**: equal or partial overlap of units not nested by membership and a member outside its composite resolve to `ABSENT` in one pass without cascade; innermost ownership first, residual and uncovered only for unowned bytes | §1.4 (R5) | S5 §1 `equal_sibling_regions`, `partial_overlap`, `nested_non_member`, `member_outside_composite`, `composite_absent_member_survives` | findings 3540d98 B4, b46c250 N6 |
| §1.5 content identity, representation, scope identity | **ACCEPT** (one representation, the Git tree entry; a data and runner contract whose risk is in materialization, a Phase D/H runner test) | §1.5 (R6) | inspection; Stage D discriminators: CRLF, mode, symlink, gitlink, LFS and submodule materialization | findings 3540d98 B1, e2154ac B1, e9e6e9f B1 |
| §1.6 effective structure, quarantine, governance-affecting classification, tenure | **ACCEPT** (definitions over structure comparisons; the risk is in the comparison implementation, a Phase D derivation test) | §1.6 | inspection | — |
| §1.7-§1.11 semantic declarations, system units, static checks, identity facts, tension locators | **ACCEPT** (formats and checks) | §1.7-§1.11 | inspection | — |
| §2.1-§2.3 relation classes, vocabulary table, adoption checks | **ACCEPT** (closed vocabulary and its adoption checks; data) | §2.1-§2.3 | inspection | — |
| §2.4-§2.5 SDGs, cycle legality, well-formedness | **ACCEPT** | §2.4-§2.5 | S5 §2 cycle cases (definitional cycle in one SDG legal; warrant, mixed and cross-SDG cycles illegal; NEUTRAL recursion and `CHALLENGES` excluded) | — |
| §2.6 completeness and analyzer declarations | **ACCEPT**, composition by union and the analyzer identity as a currency condition | §2.6, §5.10 (c) | regression seed: `judgment_disagreement_model_check.py` completeness-cover family (RR-10 limits) | finding 34803df N3 |
| §3.1-§3.3, §3.5-§3.6 ledger, envelope, tiers, qualifications, compatibility | **ACCEPT** (schema and floors; data) | §3 | inspection | findings 29da56e N3, 6b986de N4 |
| §3.4 record kinds, apart from the review-target rows | **ACCEPT** (closed kinds) | §3.4 | inspection | finding 63ddf91 B1 (completeness target with member revisions: closed; completeness-cover seed) |
| §4.1 basis modes and routes | **ACCEPT** (`content`, `validity`, `execution`, `record`, `standing`, `identity`; every `record` entry with a route; §4.1's route list as amended by A2) | §4.1 | regression seed: gate-basis family (`revision_assessment_record_mode`) | findings 653e88c B1, edabd81 N1, 82d618c N2, 82d618c N5, b46c250 N1 |
| §4.2 composition | **ACCEPT** | §4.2 | inspection | — |
| §4.3 per-kind table, apart from the review rows | **ACCEPT**, with gate decisions relying in `record` mode only on required supporting premises | §4.3 (SD-35) | regression seed: gate-basis family | findings d94a293 B1, 653e88c N1, 653e88c N3, 83a82df N2 |
| §4.4 consumption classes and equivalence paths | **ACCEPT**, hops current, unvetoed and in their recorded direction (cost restored to Manual §32.2 by A3) | §4.4 | regression seed: equivalence-chain family | findings a6ed164 B1, 0d2b35e N2 |
| §4.5-§4.6 widening chain and closure | **ACCEPT** | §4.5-§4.6 | S5 §4 closure cases (bounded by judgments, widened to a composite, whole tree when unbounded, order independence, losing a judgment only widens) | — |
| §5.1 derivation function, fixed predicate templates, stratification check | **ACCEPT** | §5.1 | inspection; incremental equals from-scratch is a Phase D test | — |
| §5.2 S0 facts and the acting rule | **ACCEPT** | §5.2 (SD-25, SD-26, R12) | regression seed: core family (`frame_acts_everywhere`) | findings b46c250 B1, f22b4dc B1, f22b4dc N1 |
| §5.3-§5.4 S1 polarity, force, continuity; polarity summary | **ACCEPT** | §5.3-§5.4 | regression seeds: core family; `s1_disagreement_model_check.py` (depth 3) | findings via the seeds |
| §5.5 S2 support, gate term, evidence term, early cutoff | **ACCEPT** | §5.5 (R11) | regression seeds: core and gate-basis families; S5 §5 `provisional_propagates_by_min` | findings 3540d98 B3, a18b544 B2, e9e6e9f B2, 575dc78 B1, f7419d5 B1 |
| §5.6 uniqueness and the support-cycle clamp | **ACCEPT** | §5.6 (R2) | S5 §5 `mutual_acceptance_forced_false` (the unclamped reading fails it) | — |
| §5.7-§5.9 corrupt prefixes, S3, determinism, analyzer pinning, checkpoints | **ACCEPT** (fail-closed rules and keyed caches; their risk is implementation, Phase D and H tests) | §5.7-§5.9 (R3) | inspection | finding 6ff4ed1 B3 |
| §6.1-§6.4 owner requirements, family rule, dimensions, assessed content, start | **ACCEPT** | §6.1-§6.4 | regression seed: `s1_disagreement_model_check.py` | workplan findings (Phase B) |
| §6.5 matching predicates and construction rule | **ACCEPT**: `on⁻` over tree-resident terms under the record's own context; `on⁺` adds the complete external-input record, every recorded attribute and a bounded basis | §6.5 (R1, SD-11 to SD-18, SD-23) | S5 §6 `differing_pin_goes_to_owner`, `differing_free_attribute_goes_to_owner`, `unpinnable_supports_no_stop`, `context_change_keeps_implication` | findings c6da678 B1, 3540d98 B2, 53669a5 B1, d837363 B1-B2, 1ffbbf0 B1, 6ff4ed1 B1, cc005db B2 |
| §6.6 staleness by discriminating observations | **ACCEPT**, adverse uses through the linking predicate | §6.6 | S5 §6 `unbounded_run_still_linked`, `genuine_fix_is_stale`, `revert_yields_again`; `s1_disagreement_model_check.py` | findings 0b6c4fa B1, 5c55d4b B1 |
| §6.7-§6.10 disposition, class, floor, scheduling, effects | **ACCEPT** | §6.7-§6.10 | regression seed: `s1_disagreement_model_check.py` | workplan findings (Phase B) |
| §7.1 transformation identity | **ACCEPT** with the one-context rule (row above) | §7.1 | S2 binding cases | findings 362af9f N3, 61cd09b N5 |
| §7.2 pinned three-way merge | **ACCEPT** | §7.2 | S5 §7 `one_side_change`, `disjoint_lines_merge`, `overlapping_hunk_conflict`, `binary_both_sides_conflict`, `declaration_key_conflict` | — |
| §7.3-§7.5 roles, existence, declared frame | **ACCEPT** | §7.3-§7.5 | S5 §7 `roles`; inspection | finding 27ef339 B3 |
| §7.6 prospective acceptance binds once; rebase | **ACCEPT** | §7.6 (R12, SD-26) | S5 §7 `later_iteration_needs_its_own_acceptance` (the lineage reading fails it), `same_enactment_counts_once`, `structure_changed_does_not_count` | finding f22b4dc B1 |
| §8.1-§8.2 requests, identity, queue order | **ACCEPT** | §8.1-§8.2 | inspection (idempotency by request identity is a Phase F test) | — |
| §8.3 validation order, apart from rows above | **ACCEPT**: never-lost salvage whatever the request's fate; a non-clean result refuses passing judgments while its result and never-lost records are admitted; step 8 refuses only evidence regression | §8.3 (R9, R15) | S5 §8 `rejected_request_salvages_never_lost` (the all-or-nothing reading fails it), `unclean_result_refuses_passing_judgments`, `clean_request_admits_all` | findings 82d618c B1, f03b15e B1, f03b15e N1, 8f4e75d N1-N2, f185036 N4, edabd81 N7 |
| §8.4-§8.7 reason codes, dependency rules, absorption, self-reference | **ACCEPT** | §8.4-§8.7 | inspection | — |
| §9 concurrency, serialization surfaces, joint invariants, generated units, residual disclosure | **ACCEPT** (scheduling never correctness; one joint-invariant review per change in scope) | §9 | inspection; regression seed: routing family | findings c77447b N3, eb86a71 N5, f185036 N2 |
| §10.1-§10.2 obligation kinds and triggers, revision assessments and the run, evidence obligations | **ACCEPT**, with the `COORDINATE(plan)` keying row above | §10.2 (SD-16, SD-19, SD-22, SD-25) | S5 §10 `revert_starts_a_new_run` (the reuse-bytes reading fails it), `in_run_acceptance_current`; gate-basis seed | findings 1ffbbf0 B2, 53669a5 B2, 798b2b4 B1-B3, 86ab683 B1, d837363 B3, edabd81 B1, 095ce55 N1, 6ff4ed1 B4 |
| §10.3 readiness, iterations, answered obligations | **ACCEPT**, as amended by A1 | §10.3 | regression seed: routing family; S2 route cases | findings 29da56e N1, 51070e5 N2, 6b986de N1, 093164f N4, edabd81 N5, 82d618c N1, N3, b595f2c B4 |
| §10.5 provisional propagation and risk-override scope | **ACCEPT** | §10.5 | S5 §5 `provisional_propagates_by_min` | — |
| §11 plan structure, acceptance, invariants, amendment policy, result-review-integration flow | **ACCEPT** | §11 | S5 §13 tightening cases; S2 transformation cases | — |
| §12 roles, envelopes, lineage classes, templates, decision classes, standing plan | **ACCEPT** (authority envelopes and fixed classes; independence over `W`) | §12 | inspection; S1-S2 independence cases | finding 51070e5 N1 |
| §13.1 contract schema | **ACCEPT** (data) | §13.1 | inspection | — |
| §13.2 lint, ref locality, domain rule | **ACCEPT** | §13.2 | S5 §13 `ref_outside_item_part_rejected`, `document_item_cannot_touch_authority`; S5 §1 write-set cases | findings b595f2c B2-B3, c6da678 B3 |
| §13.3, §13.5, §13.6 coverage minima, result slots, system contracts | **ACCEPT** (data) | §13.3, §13.5, §13.6 | inspection | — |
| §13.4 control tightening | **ACCEPT** | §13.4 | S5 §13 `prose_change_is_not_tightening` (the fields-only reading fails it), `narrower_scope_is_tightening`, `wider_scope_is_not_tightening`, `larger_budget_is_not_tightening`, `field_outside_whitelist_is_r2`, `narrower_dependency_allowance_is_tightening` | findings 6ff4ed1 B2, e548472 N3 |
| §13.7 partition and budgets, apart from the item-level row above | **ACCEPT** | §13.7 | S5 §13 `partition_lint`, `repartition_keeps_discharged_parts`, `repartition_lint_over_undischarged` | findings 051cce3 N2, 63ddf91 N2, 9e5a763 N3, 362af9f N2, 61cd09b N4, f03b15e N2 |
| §14 conformance, templates, the library, analyzers, the view, `HARD` qualification | **ACCEPT** (set-valued classes; `SIGNAL` changes no disposition; `CLEAN` discharges nothing) | §14 | S5 §14 `conformance_is_a_set` (the first-wins precedence reading fails it), `signal_changes_nothing` | — |
| §15 reports, routing, escalation floors, principal decisions, recurrence | **ACCEPT** | §15 | S5 §15 `floors_raise_never_lower`; inspection | findings 093164f N1 (§15.5 outcomes); 093164f N2, ad7ece7 N5 not applicable after SD-40/SD-47; c4e8de7 N4-N5 latch (SD-36) |
| §16 logical operations, query classes, briefs, read recording, inspector, version binding, transports | **ACCEPT** (§16.5 carries every standing rejection naming an asked item at any revision; §16.6 lists every standing adverse judgment in reach) | §16 | inspection; S2 review-target cases | findings 4c52205 N3, e548472 N1, d6734c4 B1, 61cd09b N1, f185036 N3; d94a293 N2 cost (§32.2) |
| §17 evidence specifications, realization basis, outcomes, admissibility, runners and custody | **ACCEPT** (data and custody; currency by the §6 predicates) | §17 | S5 §6 matching cases; inspection | — |
| §18 intake detection, classification, dispositions, structural intake and realignment | **ACCEPT** | §18 | inspection | finding 53669a5 B3 (§18.4) |
| §19 governance modes, legacy reliance, promotion, cutover, carve-out, rollback, genesis | **ACCEPT** (the cutover record is admitted only while its carrier's enactment has not integrated, once, for a carrier of the right kind naming the subject) | §19 | S5 §19 `cutover_record_after_carrier_integrated_refused` | findings 61cd09b B2, f03b15e B2, 63ddf91 N3; f03b15e N3 cost (§19.5, §32.2) |
| §20 external units, pins, consultation, other ledgers, multi-repository change | **ACCEPT** (data; pins feed §6's `ext`) | §20 | S5 §6 `ext` cases; inspection | — |
| §21 stores, entry format, append and durability, retention, location, derived index | **ACCEPT** (data and realization choices; Stage D runner discriminators) | §21 | inspection | the historical, provenance and retained-trade-off findings routed here are costs (§32.2, §32.5); 27ef339 B1-B2 closed by S5 §6 and §1 cases; 9431629 N4 by this index |
| §22 publication, fencing and settlement, commit point | **ACCEPT** | §22 | S5 §22 `publication_classification` | findings 61cd09b N2 (§22.3 fence re-gating, §32.3); 362af9f N1 (re-application a new enactment) |
| §23 contract, authentication, witnesses, qualification, fresh clone, known loss, continuity, recovery | **ACCEPT** (`q_a + r > N + f`; qualification states; loss bounds) | §23 | S5 §23 `deployment_classes_sound` (brute-force intersection), `qualification_states`, `loss_bounds` | — |
| §24 confidentiality prevention and breach protocol | **ACCEPT** (data and procedure) | §24 | inspection | — |
| §25 actor identity, trust roots, protected surfaces, untrusted input | **ACCEPT** (untrusted input is data) | §25 | inspection | — |
| §0.1-§0.2, §0.4-§0.5 orientation, authority, invariants, inspectability | **DROP** as mechanism: architecture owned by Manual §0 (accepted at G1, amended by SD-53); the catalogue's candidate-61 wording is not carried | Manual §0 | inspection | findings 051cce3 N4, 4c52205 N1, 653e88c N2, 63ddf91 N4, bf23372 N5, f22b4dc N2 (closed by the Manual's §0.3 as rewritten at SD-47) |
| §0.3 refinement rationale and cost cells | **ACCEPT** as the record of each refinement's full statement, rationale and costs (Manual §0.3 points there), read under the Manual's decisions and this register where its candidate-61 wording differs | §0.3 | inspection | findings 5895687 N2 (A3), 4c52205 N7, 5895687 N7 (costs) |
| §26 components, fitness, deployment, the 1.6.0 supersession | **ACCEPT** (component boundaries and fitness checks as Stage D structure) | §26 | inspection; fitness checks are Stage D Phase H | — |
| §27 ruleset, schema, system-version and successor evolution | **ACCEPT** (positional rulesets; discharge recomputed, never rewritten; re-identification by adoption) | §27 | inspection; consistent with S5 §10 run identity and §13 discharge cases | — |
| §28 versions | **ACCEPT** (data) | §28 | inspection | — |
| §29 doctrine realization maps | **ACCEPT** (data; E-level claims measured at G3, Manual §31.9) | §29 | inspection | — |
| §30 minimum-justified-architecture reassessment | **ACCEPT** | §30 | inspection | finding 362af9f N5 |
| §31.1-§31.3, §31.9-§31.10 principles, diagnostics, usability, document checks | **ACCEPT**, the diagnostics read as regression seeds (RR-10, S1) | §31 | S1-S5 models; `run_models.py --seeds` | findings 085c979 N1, 093164f N5, 494c810 N1, 8f4e75d N5, b365947 N1, c4e8de7 N1, eb86a71 N6 (RR-10); f044820 N3 (the full mutation run, SD-48) |
| §31.4-§31.8 acceptance-program groups and their expected values | **REPLACE** the expected values: Stage D takes each case's expected result from this register and the Stage S models, never from the catalogue's tables, several of which encoded blockers repaired later; every discriminator a Review named for these groups joins its group (index rows marked `STAGE-D`) | §31.2 | `G2-S4-FINDING-INDEX.md` (18 `STAGE-D` rows, assigned to groups in §5.3); S1-S5 cases already model several of them | findings 051cce3 N5, 29da56e N5, 362af9f N6, 51070e5 N3, 61cd09b N6, 63ddf91 N5, 6b986de N6, f03b15e N5, f22b4dc N5, 9e5a763 N1, b46c250 N4, 8f4e75d N4, b365947 N4, d94a293 N3; 9431629 N1 (S1 item cases); 095ce55 N7, c77447b N5 (discriminators for the withdrawn latch, SD-36) |
| §32 limits, residual risks, reopen triggers, open uncertainties | **ACCEPT** the catalogue's disclosures as G2 and Stage D runner-design considerations; the Manual's §32 (amended by A3) governs, and the catalogue disclosures it lacks go to the next amendment batch (2a17a83 N1, N2, with A4) | §32 | inspection; comparison in the 2a17a83 Review | findings 085c979 N2, 34803df N4, 47b9f77 N3, 61cd09b N3, 6b986de N3, ad7ece7 N3, b46c250 N2, e810508 N3 (closed by the Manual's text); 83a82df N3 (A3); 82d618c N4 and the trade-off lists 51070e5 N6, 9e5a763 N4, b46c250 N5, e548472 N5, f03b15e N6 (costs); 095ce55 N4, N6, 494c810 N4, c4e8de7 N3 (latch, SD-36) |
| §33 non-goals | **ACCEPT** | §33 | inspection | — |

### 4.3 Stop rules

- A model showing that no mechanism can realize a Manual decision, or that two Manual decisions conflict, stops that step and reopens G1 at the Manual's owner, with the stakeholder choosing the direction.
- A family of mechanism counterexamples that recurs after a repair triggers simplification of that family before another additive repair, and the stakeholder chooses when the options differ materially (Phase C convergence rule).
- A step that becomes implementation-like (building production components) has left Stage S; it waits for G2.

### 4.4 S1 result (2026-10-18)

The framework is `qualification/ssds80/models/` (`framework.py`: history replay, provenance, the item-level target, actors, policy and the enumeration of admissible independent ending routes; `rules.py`: one rule set per candidate reading, differing only where the candidates differ; `cases.py`: cases whose expectations are written from the Manual's decisions and A5, each naming the rule sets it refutes; `run_models.py`: the runner). Run `python3 -I qualification/ssds80/models/run_models.py --seeds`.

Result: 11 item-level cases and 12 objection cases; framework self-tests pass; the accepted Manual's rule set meets every case; and every known counterexample is reproduced as a failure of the rule it refuted: the 9431629 B1 histories and their drift sibling (candidate 61's latest-change entries), the SD-46 replaced-part and copy cases (SD-46's first wording and candidate 61), the f044820 B1 author-owner trajectory over seven target kinds and its human-reviewer sibling (the general owner exception of candidates 61 and 62), and the 8c1f2f2 B1 no-eligible-judge state with its unknown-lineage sibling (the unconditional liftability invariant of candidates 61-63). The regression seeds pass: `item_review_history_probe.py`, and the review-scope and obligation-routing families of `judgment_disagreement_model_check.py`.

What S1 can discriminate: judged-content selection from explicit histories and its authors; the owner exception's scope; route admissibility and independence for a policy and authorship; whether a stated liftability invariant holds in the waiting state. What it cannot: challenge-tier polarity, acting and frames, supersession chains, basis currency, admission order, routing, evidence disagreement, or any production consumer; and its expectations are the author's reading of the Manual, so a shared misreading would agree on both sides (independent Review checks that). RR-10 is not closed by S1: S2-S4 must extend the framework to the transformation scope (RR-2), target typing (RR-3), state-local route eligibility with acting and basis admissibility (RR-11, dddfedf N4) and routing (RR-4 to RR-8) before the old diagnostic stops being the only coverage of those layers.

### 4.5 S2 result (2026-10-18)

The framework gained `models/judgment.py` (transformation `W` and the integration support check, the one-context binding, typed targets with answering and relief, and route enumeration per state: independence over what each route record judges, acting per Manual §5.2 and §7.5, relief basis) and `models/cases_s2.py` (7 transformation, 3 binding, 5 target and 7 route cases, expectations written from the Manual). Result: the settled mechanism meets all 22 S2 cases and the S1 cases; the catalogue's reading misses the 11 S2 cases that name it (over-exclusion by same-key work in another scope, `STALE_RETAINED`'s over-refusal, two producing contexts for one identity, the joint-invariant and high-consequence target collisions, relief across colliding targets, and four route-eligibility cases); seeds pass. §4.2's rows record the dispositions. RR-1, RR-2 and RR-3 are settled pending this workplan's Review; RR-11 is settled except the waiting state, which is blocked on Q1. (Q1 was resolved by A1, accepted under SD-53; §4.11.)

### 4.6 G1 question Q1 (resolved by SD-51; amendment A1 accepted, SD-53)

S2's route model found a lawful state in which the accepted Manual's §5.10 (h)(4) ("liftable or waiting") is false if §5.10 (f)'s "No eligible judge" is read as written. A standing NO-PASS was recorded in the frame of transformation X, which was abandoned; it vetoes the passing review of a re-dispatch Z that keeps the rejected content. Its author was an agent whose task has ended. The owner O is qualified and did not author the NO-PASS's judged content, but a supersession of a judgment about X must declare X's frame (§7.5) and so never acts in Z's; O authored part of Z's judged content, so O cannot relieve Z's review; the policy adjudicator H authored the NO-PASS's content. No route record can act there. Yet (f) says an obligation waits only when every qualified actor is among the authors, which O is not; so the state neither has an ending record nor is waiting. Read per route and per state ("no eligible independent judge for any of those routes exists there", as (h)(4) words it), the objection waits and (h)(4) holds. The model case is `G1_QUESTIONS` in `models/cases_s2.py`; the runner prints both readings. By §4.3 this reopened G1 at §5.10. The stakeholder chose SD-51 (record item 47): amend §5.10 (f) so that eligibility is per route and per state (independent of what the route's record judges, acting there, basis admissible). Amendment A1 makes that change in §5.10 (f), (h)(4), §10.2 and §10.3; its GPT-family review of the delta passed (`MANUAL-REVIEW-SSDS-8.0-2A17A83-A1A2A3-DIFFERENT-FAMILY-PASS.md`) and the stakeholder accepted it (SD-53). The runner now requires the dddfedf reading to reproduce the gap and the amended reading to close it.

### 4.7 S3 result (2026-10-18)

`models/routing.py` models an item obligation after integration (fence, predicate, iteration candidates, budget, partition and item-level review, out-of-scope adverse reviews, answered decisions) and derives its single route and the open decision obligations under the catalogue's reading and the settled one; `models/cases_s3.py` holds 13 cases with expectations from the Manual's principles (no stranded obligation, findings survive to their owner and are never retired by a later obligation, a pending candidate keeps its routes, drift re-dispatches). The settled routing meets all 13; the catalogue's misses every case that names it. RR-5 to RR-8 are settled pending this workplan's Review (§4.2). RR-4 is not a routing mechanism: it is G1 question Q2.

### 4.8 G1 question Q2 (resolved by SD-52; amendment A2 accepted, SD-53)

Manual §10.4 says an item obligation's identity is "its item and the prose and fixed fields of its accepted revision", and that "an R1 tightening keeps it and an R2 amendment derives a new one". By §13.4 an amendment that only loosens a tightenable field (a wider write scope, a larger budget, fewer frozen symbols) is R2, yet keeps the prose and fixed fields. There the two statements disagree: the key keeps the obligation (its `out(o)`, its subjects and its iteration count); the R2 clause derives a new obligation (empty `out(o)`, a fresh budget). No mechanism satisfies both, so the Manual must say which; this is the SD-41 residual (a), now reached by S3. By §4.3 it reopened G1 at §10.4. The stakeholder chose SD-52 (record item 48): the identity key governs; a loosening-only amendment keeps the obligation and waits for a new plan acceptance; only a prose or fixed-field change derives a new obligation. Amendment A2 makes that change in §4.1 and §10.4 and is folded into A1 for one delta review.

### 4.9 S4 result (2026-10-18)

`qualification/ssds80/G2-S4-FINDING-INDEX.md` (generated by `models/finding_index.py`) indexes 490 heading-level findings from 87 Review records: 8 closed by named S1-S3 model cases, 482 open and routed to their owning sections (the largest shares are §5 derivation, 91; §6 assessment disagreement, 74; §10 obligations, 60; §0 refinements, 35; §31 qualification, 29). Extraction is mechanical, so a finding stated only in running prose may be missing; S5 reads each owned record in full before closing its section. S5 disposed of every finding; the index now covers 493 findings from 88 records, none open (§4.10).

### 4.10 S5 progress

S5 settles catalogue sections in dependency order; each records its dispositions in §4.2 and disposes of every S4 finding routed to it. Model families are listed in `models/run_models.py` (`S5_MODULES`).

**§1 (2026-10-18).** `models/structure.py` and `models/cases_s5_1.py`: 10 cases, the settled partition and write-set rules meet all of them, and each refuted reading (equal regions with two owners; a residual that subtracts only members; changed-path attribution; base-to-merged comparison; position comparison) fails its case. Findings routed to §1: 3540d98 B4, b46c250 N6, 5c55d4b B2, cc005db B1 and d837363 B4 are closed by the settled mechanism (model cases above); 3540d98 B1, e2154ac B1 and e9e6e9f B1 (one representation that every consumer and runner reads) are closed at the architecture level by Manual §1.5 and carried as Stage D runner discriminators; 6ff4ed1 B3 (analyzer set not bound to the ledger) is closed by Manual §5.9's pinning and goes with §5; workplan 6fe1000 N5 (fail-closed authorship removes agent dispositions over absorbed and legacy content) is the cost Manual §32.2 discloses for §5.10 (f), not a mechanism defect.

**§2-§4 (2026-10-18).** `models/relations.py` and `models/cases_s5_2_4.py`: 11 cases (cycle legality, closure); the settled rules meet all of them. The judgment-layer families of `judgment_disagreement_model_check.py` (core, equivalence-chain, completeness-cover, plan-coverage, gate-basis) remain the regression evidence for §2.6, §4.1, §4.3 and §4.4, within RR-10's limits (hand-chosen tables, shared helpers); their full mutation run was green at candidate 63's tree and the module is unchanged. Findings routed to §2-§4 (32): closed by the S1-S3 models: 9431629 B1, e810508 B2 (item-level judged content), 9431629 N2, ad7ece7 N4, e810508 N4, 051cce3 N1 (typed review targets, S2), ad7ece7 B1 (one judged content, S2), 6b986de B1 (one independence input over `W`, S1-S2), 093164f B1, 8f4e75d B1 (one route statement and settled routing, S3); closed by the settled mechanism with seed evidence: a6ed164 B1 and 0d2b35e N2 (equivalence paths; the hop-direction cost restored to the Manual by A3), 63ddf91 B1 and 34803df N3 (completeness target and analyzer identity), 653e88c B1 and edabd81 N1 (`standing` mode), d94a293 B1, 653e88c N1 and 83a82df N2 (gate basis on required premises), 3540d98 B3 (qualified gate capped, R11); closed at the architecture level by the accepted Manual's text (repaired in later candidates and checked by the G1 Reviews): 29da56e N3 and 6b986de N4 (R3 floors and the chain's class), 82d618c N2 and N5, b46c250 N1 (evaluation in the state at hand), f185036 N1 (drift cost, §32.3); not applicable after SD-47 (findings on the diagnostic's construction, now RR-10): 653e88c N3, ad7ece7 N1, edabd81 N6; disclosed costs carried, not defects: 6b986de N8, 63ddf91 N1 (§32.2); workplan 6fe1000 N8 (residual pre-revision-17 workplan text) concerns the cycle record, not the catalogue.

**§5-§7 (2026-10-18).** Models: `relations.py` (support-cycle clamp, min propagation), `matching.py` with `cases_s5_6.py` (the two matching predicates, the linking predicate and mechanical staleness, 7 cases), `frames.py` with `cases_s5_7.py` (merge, roles, prospective acceptance, 9 cases); `s1_disagreement_model_check.py` joins the regression seeds at depth 3. The settled rules meet every case, and each refuted reading fails its case (the pin and attribute readings are modelled as their candidates had them, before the linking predicate existed). Per-finding dispositions are in `G2-S4-FINDING-INDEX.md`, now generated with a hand-written disposition for each finding judged and with evidence taken mechanically from the named mutations of `judgment_disagreement_model_check.py` and the named discriminators of `s1_disagreement_model_check.py`; no finding routed to §1-§7 remains open. Workplan Review findings from before the Phase B PASS are recorded as closed in the workplan by that PASS's re-verification, the catalogue realizing the reviewed contract.

**A4 (to propose with the next amendment batch).** §5.10 (e) of the Manual lost, in the SD-47 condensation, the catalogue's rule that where a reach crosses items or plans the owner is the owner of the adverse judgment's target and the reached judgment's own owner is shown on the obligation (finding 913db8f N6). The catalogue keeps it, so G2's mechanism is unaffected; the Manual should state it. It is held for the next amendment so as not to disturb the A1-A3 review already arranged. By SD-53 the next batch also carries that Review's findings N1 (Manual §32.2 to say that qualified independent actors may all lack a record that acts, or an admissible basis, in the needed state) and N2 (the catalogue §32.3 trigger for failures caused by unrecorded execution attributes being made stale and later found live, and for retained trees and reproductions costing more than the dispositions they make cheap; catalogue §17.5's costs of an attribute the Dispatcher cannot request and of a change of a class's declared attribute set).

**§8-§13 (2026-10-18).** `models/work.py` and `models/cases_s5_8_13.py`: 16 cases (never-lost salvage and the non-clean-result refusal, the revision run under a revert, the control-tightening order, ref locality, the domain rule, partition and re-partition lint); the settled rules meet every case and each refuted reading (all-or-nothing admission, acceptance reused by bytes across runs, prose ignored by tightening) fails its case. No finding routed to §8-§13 remains open; 22 of them concern R15's latch, withdrawn by SD-36.

**§14-§25 (2026-10-18).** `models/persistence.py` and `models/cases_s5_14_25.py`: 8 cases (set-valued conformance against a first-wins precedence reading, `SIGNAL` changing nothing, floors that only raise, the cutover carrier window, publication classification, witness-quorum soundness by brute force over small deployments, known-loss bounds, qualification states); the settled rules meet every case and the first-wins precedence reading fails its case; the cutover case encodes the window the two Blockers found missing rather than replaying an earlier reading. Sections 17, 18, 20, 21, 24 and 25 are mainly data, procedure and realization choices accepted on inspection, with their behaviour checked as Stage D runner discriminators. No finding routed to §14-§25 remains open: most of those routed to §21 are the historical, provenance and empirical limits and retained trade-offs that Manual §32.2, §32.3 and §32.5 disclose; the rest are closed by the accepted Manual's text, by S1-S5 cases, or are not applicable after SD-36, SD-40 or SD-47. The open findings left are owned by §0 (9), §30 (1), §31 (29) and §32 (17).

**§0 and §26-§33 (2026-10-18).** Settled on inspection: these sections are orientation, components, evolution procedure, version data, doctrine maps, the reassessment, qualification design and disclosures, so §7's stop rule applies and no new model was built; §27's positional rulesets and recomputed discharge agree with the S5 §10 and §13 cases. The one substantive change is to the acceptance program: catalogue §31.4-§31.8's expected values are replaced by this register and the Stage S models, because several Reviews found those tables encoding blockers later repaired; the discriminators they named (index rows `STAGE-D`) join the Stage D groups (§5). The finding index now has no open finding: 493 findings across 88 records, including the 2a17a83 Review's (N1 and N2 carried with A4, N3 noted).

**A3 (accepted with A1 and A2, SD-53).** While disposing of 0d2b35e N2 the author found that the SD-47 condensation had dropped disclosed costs from Manual §32.2 and §32.3 that the catalogue still states (the equivalence-hop direction, an unpinnable passing realization staying current, `ABSENT` terms raising no finding, fail-closed adverse linking, incidental host reads, attestation challenges, the re-partition consequence of the judged-content rule, plan-rejection reach on control-only branches, a frame `REJECT` after abandonment, and several reopen triggers). Amendment A3 restores them in the Manual's current terms, changing no decision, for review and acceptance with A1 and A2.

### 4.11 Residual-register closure (S6)

Each entry of catalogue C.2 is closed here for G2 at the same no-blocker bar, pending this workplan's independent Review. Closure is design evidence: the production behaviour each entry concerns is qualified at its real owner in Stage D (§5.3), never by these models (DS-001).

| Entry | Closed by | Evidence | Stage D carry |
|---|---|---|---|
| RR-1 item-level review judged content | S2 (§4.5); register rows §3.4, §4.3, §13.7 | S1 item cases (11) built from integration histories; S2 target cases | group 3 history-derived item-level cases |
| RR-2 transformation judged scope and retained units | S2 (§4.5); register rows §5.10 (b), §8.3 step 2 | S2 transformation and binding cases (10) | group 3 |
| RR-3 review target typing | S2 (§4.5); register row §3.4 | S2 target cases (5) | groups 3, 5 |
| RR-4 identity under a loosening amendment | Q2, decided by SD-52, amendment A2 accepted (SD-53); register row §10.4 identity | S3 `IDENTITY_CASES` (4) | group 5: the assembled transition (`out(o)`, subjects, count through amendment, acceptance wait and budget change), which the identity cases do not implement (2a17a83 Review) |
| RR-5 to RR-8 routing residuals | S3 (§4.7); register rows §10.4 | S3 routing cases (13) | group 5: the real-owner routing replay the register names (§5.4) |
| RR-9 historical findings | S4 index and S5 (§4.9, §4.10) | `G2-S4-FINDING-INDEX.md`: 493 findings, none open | the 18 `STAGE-D` rows (§5.3) |
| RR-10 diagnostic construction | S1-S5: models whose expectations are stated from the Manual and from recorded histories; the earlier diagnostics kept as regression seeds | `run_models.py --seeds`; each step's stated limits (§4.4-§4.10) | expected values rule (§5.1 item 3) |
| RR-11 owner exception, missing-judge waiting, per-state eligibility | S2 (§4.5) and Q1, decided by SD-51, amendment A1 accepted (SD-53) | S2 route cases (7), `G1_QUESTIONS` | group 3: per-record judged content, acting state, class and basis admissibility through the resolver and Dispatcher (2a17a83 Review) |

## 5. Stage D — shadow implementation plan (authorized only at G2)

Stage D builds the shadow system of the architecture workplan's Phases D-H (its §23) within §2. It adds no architecture and no mechanism beyond the settled register (§4.2): every behaviour it builds names the register row it realizes, and a behaviour no row covers goes back to Stage S (§5.6).

### 5.1 Rules for every phase

1. **Delivery.** One distribution, `sdp-orchestrator-ssds`, under `orchestrator/`, with the namespace package `sdp_orchestrator.ssds` and one subpackage per Manual §26.1 component, registered through Core's existing entry-point group `sdp_orchestrator.extensions.v1` (Manual §26.3). No Core change is needed or allowed. The Manual §26.2 fitness checks are written first, in Phase D, and run in repository acceptance for every later change.
2. **Shadow boundary.** The shadow ledger is at a location designated at shadow genesis (Manual §21.5) that document control never reads. No SSDS process holds a credential that can move a governed ref or write a governed file. Every subject is `LEGACY(p)` or `UNGOVERNED` (§2 item 1). Each phase's acceptance checks this boundary.
3. **Expected values.** Each acceptance case states its expected result from the register row it tests and the Manual decision behind that row. Stage S cases supply expectations as written (their stated expected outcomes), never by running the model rules on production output, and production code never imports `qualification/ssds80/models/`. The catalogue's §31.4-§31.8 tables do not supply expected values (§4.2). Each group keeps its negative discriminators (Manual §31.2).
4. **Real owners.** Each group runs at the production owner the catalogue names for it (for example, ledger-only replay as the oracle for publication classification). Fixtures alone qualify only mechanical properties (DS-001).
5. **Phase Review.** Each phase ends with an independent implementation Review recorded in `qualification/ssds80/`. A phase PASS lets the next phase's dependent work start and accepts nothing; acceptance is G3 (criterion 15). The human gate of the shadow genesis (Phase D) is the stakeholder's.
6. **Frozen surfaces.** §2 item 6 holds throughout; Core's own suite and the frozen-profile tests run unchanged and pass at every phase (PC-001).
7. **Campaigns.** A live agent trajectory or any measurement spend (Manual §31.9; Phase E's burden and doctrine measurements; any live agent run in Phase F) is a campaign. It needs a frozen measurement plan (gates calibrated from simulated operating characteristics, instruments validated first, rules, custody and blinding frozen before runs), that plan's independent Review, and the stakeholder's explicit authorization, separate from G2. Without one, a phase runs on recorded histories, this repository's history and synthetic fixtures only.

### 5.2 Phases

Phases run in order; each starts after the previous phase's Review. Register rows are named by catalogue section (§4.2).

| Phase | Builds (shadow, no authority) | Realizes register rows | Exit evidence for G3 |
|---|---|---|---|
| **D** read-only kernel | `content`, `analyzers`, `ledger` (schema, chain verification, store, qualification read path), `derivation` (strata S0-S3 and queries), the §26.2 fitness checks, and Admission's genesis path only: the shadow genesis of Manual §19.9 (validation, the human gate, append under its own quorum, `LOCAL_TRUST` allowed), so that only Admission appends from the first entry; derivation reads that genesis with this repository's content and Git history | §1-§7, §19.9, §21, §23 read path, §27-§28 | groups 1, 2 and 3 (derivation halves); determinism and replay; incremental equals from-scratch; a shadow genesis of this repository's history derived end to end |
| **E** read-only interface and workflow layer | `interface` (`open`, `ask`, `read`; task, review, decision and gate briefs; the inspector view and digest); S3 conformance, routing and escalation views; contract lint | §10-§16, §29 | groups 5 and 6 (derivation halves), with the routing residual replay on recorded histories (§5.4); live trajectories only under an authorized campaign (§5.1 item 7) |
| **F** Admission and Dispatcher in shadow | `admission` (validation steps, witness quorum, publication and fencing) and `dispatcher` (scheduling, envelopes, designated-runner realizations in sandboxed workspaces without push credentials), computing decisions beside document control | §8-§9, §17, §22-§25 | group 4; the admission halves of groups 2, 3 and 5; every material difference from document control classified (SSDS defect, baseline ambiguity or defect, deliberate stronger rule, unresolved judgment) and independently reviewed |
| **G** intake and migration pilot | intake, the migration path for this repository's legacy documents (Case B) and one external scientific repository (Case C/D) on a read-only clone with its owner's permission; external units | §18-§20 | group 7, with cutover cases on shadow ledgers and fixtures only (no subject changes mode) |
| **H** adversarial and fault qualification | adversarial, privacy and fault harnesses over the whole shadow system | §26, and §24-§25 under attack and fault | group 8; the G3 package (§5.5) |

### 5.3 Acceptance groups and the named discriminators

Groups are Manual §31.2's. Stage S cases carry over as expected values (§5.1 item 3); the discriminators are the `STAGE-D` rows of the finding index, each a case its Review found missing from the catalogue's qualification design, with its expected result taken from the register.

| Group | Phase | Stage S cases carried | Review-named discriminators |
|---|---|---|---|
| 1 derivation, structure, relations | D | S5 §1 (10), §2-§4 (13) | 3540d98 B1, e2154ac B1, e9e6e9f B1 (one representation read by every consumer and runner, with Phase F); f22b4dc N5 (analyzer re-identification of a D1/D2 revision); b46c250 N4 (an anchor move giving a D2 unit different bytes is a `VIOLATION`; a case isolating the region criterion from owned content) |
| 2 assessment disagreement | D, F | S5 §6 (7); the `s1_disagreement_model_check.py` seed | 798b2b4 B4 (each link traversed is recorded); 29da56e N5 (counter-challenge, observation dismissal, triple dismissal, chain class, support route, adjudication recovery) |
| 3 judgment disagreement | D, F | S1 (23), S2 (22 and Q1), S5 §5 and §7 | 051cce3 N5 (revert after cross-target relief; the plan objective's revision); 362af9f N6 (no identical-content gate veto); 51070e5 N3 (an upheld challenge needs independence and class; relief variants); 61cd09b N6 (relief in a later run); 63ddf91 N5 (`COMPLETENESS` supersession across revisions; `PLAN_ACCEPTANCE` relief after a non-overlapping amendment); 6b986de N6 (one definition of each independence input for every record kind); f03b15e N5 (assessment supersession after the key change, `PLAN_ACCEPTANCE` overlap, `EQUIVALENCE` class supersession, a human reassessment of an answered non-gate obligation); f22b4dc N5 (relief of an admitted veto from a rejected iteration or a partition sibling; a revert restoring under the earlier run's obligation); 9e5a763 N1 (a non-independent owner or author pass composed with a separately vetoed peer pass); b46c250 N4 (an admitted gate kept above `F`; a frame superseding an admitted adverse gate decision; an item-required gate on an unchanged D1/D2 subject); d94a293 N3 (gate basis from source to consumer) |
| 4 admission, publication, currentness, loss | F | S5 §14-§25 (publication, quorum soundness, loss bounds, qualification states) | 362af9f N6 (re-application of a fenced or `OVERTAKEN` integration); 61cd09b N6 (a kept fence and the D1/D2 re-gating) |
| 5 workflow, contracts, conformance, routing | E, F | S3 (13 and the 4 identity cases), S5 §8-§13 (16) | 051cce3 N5 (a reopened part obligation of a superseded `PARTITION`); 51070e5 N3 (the §13.7 re-partition example); 63ddf91 N5 and f03b15e N5 (a re-partition after a discharged part); b365947 N4 (an R1 tightening the content already meets still re-dispatches) |
| 6 escalation and the inspector | E | S3 no-stranded-obligation cases | 8f4e75d N4 (§10.3's second half: no non-current judgment that a current obligation depends on is left with neither a ready nor a waiting route) |
| 7 frames, migration, intake, external units | G | S5 §7 frames (9), S5 §19 cutover case | 051cce3 N5 (the frame of a refused second carrier); 362af9f N6 (cutover obligations derivable from the ledger alone); 61cd09b N6 (who may submit the `MODE_TRANSITION`, when the conditions are checked, the D1-D3 carrier); 63ddf91 N5 (an admitted-frame cutover record; two parallel carriers); f03b15e N5 (the carrier integrating before the cutover record exists; the mechanism of its `VIOLATION`); f22b4dc N5 (a re-cutover by the same requester) |
| 8 security, Core independence, fitness | H | — | none named |

### 5.4 Catalogue qualification clauses replaced at S6

- Catalogue §31.4-§31.8's expected values: replaced by the register (§4.2, §5.1 item 3).
- Catalogue §31.5's "exercised at the real owners before G2" for the routing residual, and the "real-owner routing replay" register RR-4 to RR-8 name as their G2 discriminator: no real owner exists before G2, so G2 closure rests on the S3 models (§4.11), and the real-owner replay is a group 5 case in Phases E and F.
- The history-derived item-level and transformation cases of RR-1 and RR-2 that Manual §31.2 places in group 3 run at the real owners in Phases D and F, from the S1 and S2 histories.

### 5.5 Exit to G3

G3 (criteria 9, 10 and 15) is the stakeholder's decision on a package Stage D assembles: each phase's implementation Review; each group's executed results at its real owners, discriminators included; Phase F's classified differences with their Reviews; and, if campaigns were authorized, their measurement reports against the 7.2.1 baseline with their limits (Manual §31.9). A group not executed is reported as unexecuted, never as passed.

### 5.6 Stop and reopen rules

- A Manual decision that fails in practice reopens G1 at the Manual's owner (Manual §32.3), not a local patch.
- A register row that fails at its real owner, or a needed behaviour with no row, returns to Stage S: a design-model case first, then the row's changed disposition in this workplan and its Review, then implementation.
- A failure family that recurs after a repair triggers simplification before another additive repair (§2 item 3).
- Any breach of the shadow boundary (§5.1 item 2) stops Stage D and goes to the stakeholder.

## 6. G2 checklist

| Criterion 13 element | Where it is met |
|---|---|
| derived from the accepted Manual | §0-§2; every settled mechanism names the Manual decision it realizes (§4.2) |
| each catalogue mechanism accepted, replaced or dropped against executable models | §4.2, complete (S5, §4.10); qualification clauses §5.4 |
| every residual-register entry closed | §4.11 |
| bounded to shadow operation | §2 item 1, §5.1 item 2, §5.2 |
| independently reviewed | the review of the frozen revision (S6), recorded in `qualification/ssds80/` |
| **Criterion 14:** explicit stakeholder authorization of the shadow implementation | recorded verbatim in the stakeholder decision record after that review |

## 7. Reopen triggers and risks

Every Manual §32.3 trigger applies. In addition: a Stage S model needs a semantic the Manual does not state (a missing architecture decision; reopen G1); the settled mechanism is materially more complex than the catalogue it replaces; Stage S cost outgrows its value for a section that is a data format (stop and record the format as accepted by inspection, with the reason).

## 8. State

| Item | State |
|---|---|
| G1 | accepted (SD-50, 2026-10-18) |
| this workplan | revision 1, proposed, frozen for independent Review (S6) |
| Stage S | S1 done (§4.4); S2 done (§4.5, §4.6); S3 done (§4.7, §4.8); A1-A3 accepted (SD-53); S4 index done, no finding open (§4.9, §4.10); S5 done (§4.10); S6 done: Stage D made concrete (§5), register closure (§4.11), revision 1 frozen |
| Stage D | not authorized |
| G2 | open |

**Revision 1 (2026-10-18, S6).** Revision 0 opened the workplan under SD-50 and recorded Stage S as it ran (§4.4-§4.10). Revision 1 adds the register closure (§4.11) and the concrete Stage D plan (§5, replacing revision 0's outline), brings the Stage S results current with SD-53, and freezes the file for independent Review. Nothing in it authorizes Stage D.
