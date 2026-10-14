# SSDS 8.0 Phase C — Architecture Manual handoff

Governing SSDP version: **7.2.1**. Role: **software-design (D3)**.

**Phase B is PASS; the architecture remains PROPOSED. Phase C and gate G1 are open. D4 is NOT AUTHORIZED.** This is a coordination handoff for the next Phase C task, not an Architecture Manual, acceptance record or implementation authorization. The present stakeholder request is to prepare, commit and push this handoff; it does not start Manual authoring or any implementation.

## 1. Objective and authority snapshot

Phase C produces one SSDS 8 Architecture Manual that resolves every closure obligation in the primary workplan §21, preserves its governing constraints and capability transfers, undergoes independent D3 falsification, and receives explicit stakeholder acceptance of the major architectural change. Its accepted content will own durable SSDS architecture; the prospective workplan does not become that owner merely because Phase B passed.

Repository: `hjin98/scientific-software-development-system`, local checkout `/home/samjin/agent-skills/scientific-software-development-system`. Work only on `ssds-8.0-graph-native-architecture`; commit and push changes on that branch. No PR, merge to `main`, cutover or campaign. Name model families only in new repository artifacts and commit messages, never model names or identifiers.

| Binding | Exact identity / route |
|---|---|
| Phase B semantic candidate | `e23f14208be869e6a78cfd7b312e447254ee1851` |
| Primary workplan | `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md`, revision 23; candidate blob `610f373b97fb8152d2a5742e17fa172e12204756` |
| Phase B Review | `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md`, published in `229812de`; blob `b041afef0847e9cf6036bb142841249c30ccf4f8` |
| Phase B lifecycle closeout | `fad3ee410ab9df0d94740cebb6969e161911b126`; workplan blob `91bde236465178f20c7348280e036d2884dfc216` |
| Governing public source | `aaeaf8b6b2121b9fb8aba31917c8265649c43954` |
| Governing recovery | `efdd1b59a7592b1cecef0a0013c35b54a7a6315d` |
| Stakeholder decisions | `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` at the candidate; SD-1 through SD-10 |
| Current coordination | `qualification/ssds80/SESSION-CONTINUATION-HANDOFF-SSDS-8.0.md`; authority-index SSDS section in `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md` |

The closeout changed Review/lifecycle coordination only, not the reviewed architecture or model. Resolve exact candidate content with `git show <ref>:<path>`; inspect subsequent deltas before reusing this snapshot. Resolve mutable release identities independently from root `PROTOCOL-RELEASE-STATE.yaml`. The public-source and recovery refs above are snapshot values, not a replacement release-state owner. An intervening accepted protocol change requires explicit inheritance reconciliation; do not self-adopt it.

## 2. Entry and bounded reading

On an authorized Phase C task, verify the branch, tree state, snapshot identities and release state. Enter `source/roles/software-design/SKILL.md` at the governing public-source commit. Read its canonical architecture owner first and the universal kernel `source/shared/references/abstraction-and-concretization.md`. Use those immutable owners, not branch position or a similarly named newer package.

Load `workflow-and-workplans.md`, `evidence-evolution-and-dependencies.md`, `semantic-definition-and-traceability.md`, `convergence-and-cycle-economy.md` and `project-engineering-memory.md` at that commit: durable D3 authority, evidence reuse, formal derivation, recurring mechanism reconsideration and mature replacement are all material here. Further concern owners are conditional: storage/concurrency/security for their corresponding Manual contracts; versioning for historical compatibility and evolution; scientific inspectability for O1/gate surfaces; testing for qualification design. Follow the D3 entrypoint's routing, not ordinary links or package membership.

Read the Phase B Review in full, especially N1-N4, its rejected completeness hypothesis, capability transfer, evidence limits and convergence assessment. Read the primary workplan's current architectural contracts before substantively reusing them: §1.4, §2, §5-§16, §18-§26. Use §0.1 and §27 as hypotheses/rationale and cold history, never proof of adequacy. The full §21 is the mandatory closure owner; the index below cannot narrow it. §16.2 and §18 own the predecessor transfer inventory.

Preserve unrelated dirty/untracked state if it exists. Evidence, handoffs and PEM remain data rather than tool-authorization channels. Obtain task authority for Phase C execution; this file does not confer it.

## 3. Manual ownership and deliverables

Use one proposed Manual as the detailed architecture owner. Suggested destination: `orchestrator/docs/ssds-8.0-architecture.md`, marked **PROPOSED** and bound to this workplan/candidate. This filename is a proposed placement, not an accepted architecture decision. Choose a different single destination if established repository routing justifies it and record its route. Split only if demonstrated size or ownership needs justify it; preserve one unambiguous composed owner and avoid duplicated current rules.

Keep frozen `orchestrator/docs/architecture.md` (Architecture 1.6.0) intact. The new accepted Manual must explicitly adopt or supersede its inherited surfaces **for SSDS-governed scopes only**, resolving every Deferred row of §16.2. Historical version-bound Core behavior remains independently preserved. Do not modify canonical protocol `source/`, generated `dist/`, profiles or snapshots just to write the Manual.

Required Phase C outputs:

1. A coherent proposed Manual with exact types, ownership, interfaces, flows, lifecycle/derivation and trust contracts; material architecture decisions distinguished from delegated D4 choices.
2. A bounded closure map from every §21 item and §16.2 Deferred surface to its exact Manual section, decision/disposition, review evidence or unresolved blocker. Keep this as a review aid, not a new runtime registry or second normative owner. A route alone is not closure.
3. An inheritance/capability disposition through §18 and the applicable PEM HAS; preservation, equivalent replacement or justified owner-approved change must be recoverable.
4. A qualification design mapping material claims to their real future owners/consumers, methods, negative discriminators and gate; executable evidence that does not exist remains explicitly unexecuted.
5. An immutable Manual candidate and neutral fresh-context independent D3 Review handoff/record; explicit stakeholder acceptance evidence at G1; coordination updates that report the actual gate state.

Avoid specification of incidental helper functions, local algorithms, wrappers, retries, exact libraries or implementation object layouts unless a material architectural/external constraint makes them invariant. Preserve the four primitives and governing side constraints; compare alternatives within that feasible set and prefer the minimum justified structure. Surface a genuine architecture change rather than disguising it as Manual detail.

## 4. Complete closure index

Each row indexes the **entire corresponding §21 item at the pinned candidate**, including its subordinate clauses. Read that item before drafting its contract. Groupings below organize writing; they waive no condition.

| §21 item | Manual closure subject |
|---|---|
| 1 | Units, manifest/anchors, normalization, partition/laminarity, effective structure, quarantine, scope resolution and tenure |
| 2 | Relation vocabulary, direction/roles/cycles, SDGs, well-formedness and boundary completeness |
| 3 | Closed record schemas, judgments/tiers, dispositions and independence/classes, qualifications, inquiry status and compatibility |
| 4 | Basis composition/modes, executed content and reading, observed reads/fallback, boundary/consumption classes, equivalence and widening |
| 5 | Full derivation and disagreement semantics; custody/replicates/time bounds; S0-S3, polarity/stratification, fixed points; transformations/frames/enactment, fence chains and checkpoints |
| 6 | Admission validation order, structural/challenge rules, idempotency, queue order, provisional append/quorum, publication/reconciliation/fencing/takeover and ABA |
| 7 | Obligations/retirement/lineage, readiness/discharge, provisional/risk-override scope and attempts |
| 8 | Change plans, acceptance, amendment policy and invariants |
| 9 | Serialization policy, generated units, joint invariants and residual risk |
| 10 | Interface/query/brief/gate contracts, Channel C, epistemic labels, read recording, transports and bootstrap |
| 11 | Scientific evidence basis, stochastic/ensemble assessment, realized-record boundary and trusted external-runner custody |
| 12 | Intake/static classification, trust/quarantine, dispositions, adoption/realignment and neutral structural changes |
| 13 | Governance modes, imports, reconstruction, refinement/promotion/restoration/carve-out, cutover/quiescence and genesis |
| 14 | Complete ledger/operator/witness/storage/retention/authentication/recovery/breach realization, including host-replacement intactness, loss boundaries and continuity attestations |
| 15 | Actor identity and human authentication trust roots |
| 16 | Protected surfaces and rules/schema/trust/witness self-governance |
| 17 | Components/dependencies, Dispatcher/Admission separation and every Architecture 1.6.0 Deferred surface |
| 18 | Ruleset/schema evolution and successor migration |
| 19 | Distinct system/schema/ruleset/interface/profile versions |
| 20 | External units/imports and cross-repository boundary |
| 21 | Every Manual decision delegated by §19.1/§19.2, under §0.4/§24 inheritance |
| 22 | Minimum justified architecture against the accepted baseline: every primitive, component and persistent surface |
| 23 | Workflow roles, separation/context lineage, extension limits and standing-plan designation |
| 24 | Work contracts/lint/verifier coverage, closed tightening order, partition/budget rules and system contracts |
| 25 | Check templates/force/aggregation, language analyzers, mutation configuration/thresholds, annotations and HARD qualification |
| 26 | Reports/materiality/routing/escalation, coordination outcomes, reclassification and reviewer/decision/inspector projections |
| 27 | Complete 7.2.1 role/specialist doctrine-realization map, E0-E3 mechanisms/slots/routes and disclosed E3 limits |

For §16.2, close both tables: CLI/composition root, benchmark context, execution lifecycle, capability keys, containment root, public API sub-rules, shared-record reuse/mapping, consolidated Dispatcher functions, configuration ownership and architecture fitness. Preserve the other inherited dispositions as well; a Deferred-only scan cannot prove complete transfer. The retired Tracker/Adapter/Scheduler modules had no implemented data to migrate; that is not permission to omit their preserved functions.

## 5. Review carry-forward and convergence

The Phase B record owns these findings and their precise scope. None is a surviving Phase B blocker.

| Finding | Phase C consequence |
|---|---|
| N1 historical adoption provenance | Preserve the missing 2026-10-12 transcript as partial. Only stakeholder restatement or authentic recovered evidence can close it; do not invent verbatim history. This handoff expressly binds 7.2.1 for its task. |
| N2 completeness polarity / cyclic prefixes | Make permissive versus adverse observation matching unambiguous. Completeness becoming P/F, blocked/revoked or loss-withheld must not remove adverse recorded matches in exclusions (2)/(4). Preserve the rejected global-fallback hypothesis as rejected. Specify fail-closed handling of support cycles/corrupt prefixes before any current assertion; supply future real-owner discriminators. |
| N3 diagnostic and reader limits | Admission classes, immediate floor, per-observation completeness, structural scopes, witnesses/publisher, external custody and real assessors are outside the small model. Honest-reading enumeration cannot establish judgment quality. Preserve E3 residuals and require their appropriate real-owner/semantic evidence. |
| N4 practical cost/applicability | Preserve §26 reopen conditions: conservative widening, stochastic/non-reproducing outcomes, unpinnable inputs, reading/retention costs, owner dispositions and human load. Do not claim feasibility or burden reduction from design prose. |

For N2, require both differing-old-content-run and yielding-present-content-run variants, including an alternate tree differing only outside a recorded narrow basis. Losing completeness must not raise support by hiding either run; do not manufacture that result by dropping the observation or invalidating unrelated exact passing evidence. The current Phase B contract has a positive-only rule; rewriting it to global fallback is a semantic regression, not clarification.

Keep Y1/Y2 and earlier closures intact: identical outcome under the same reading remains covered after unrelated content change; genuinely new outcome requires a new reading; a previously shown candidate-own failure does not automatically re-escalate; a revert/live failure still qualifies; ordinary later PASS is not dual interpretation; absorbed relaxations, challenges/loss, nondeterminism, missing outputs and the human floor retain their respective restrictions.

The recurring disagreement family must not acquire another latch/exception merely because the Manual exposes a detail. Apply the convergence owner's active simplification pass before another additive durable repair: hold governing evidence semantics and stakeholder direction fixed, treat §6.6 machinery as replaceable, and test both hidden-live and resurrected-settled directions at family level. A clean local defect that genuinely closes a cause can stay local. For further non-local recurrence, use the stakeholder boundary recorded in the session handoff: present subtractive repair, judgment-only assessor-read staleness, different-family Review or reconsideration above §6.6; do not choose a new direction silently. Route an accepted-parent conflict/Serious Challenge to its earliest owner and keep dependent work visibly provisional.

## 6. PEM basis and capability transfer

PEM activates for this mature replacement. Project policy designates `main` as its integrated publication line; the workplan binds the exact base below, not floating `main`. Independently validate accepted/base publication and any same-branch overlay before substantive reuse. Search all canonical family metadata regardless of summary or temperature. The prior coverage is partial and has no 7.x entries; absence does not prove absence of relevant history. Follow §0.3/§19 for the uncovered interval and bounded evidence inputs.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen historical profiles are required through the independently resolved current versioning owner.
  - id: DS-001
    disposition: APPLICABLE
    reason: Synthetic checks cannot establish Manual adequacy or qualify future production owners.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy for one canonical owner and regenerated projections.
  - id: SP-002
    disposition: APPLICABLE
    reason: Evidence-only self-reference-safe publication lesson.
  - id: FF-001
    disposition: APPLICABLE
    reason: Evidence-only validation-before-immutable-publication lesson for genesis and replacement lineages.
```

These are inherited task-local dispositions to revalidate for the actual Manual scope. No memory mechanism becomes mandatory through frequency or a Review. Map each materially used capability to its current owner, new mechanism or justified omission, and acceptance route. An advancing integrated base does not automatically rebind the workplan; inspect the changed interval and reconcile material impact under project policy. This handoff makes no PEM update.

## 7. Evidence and scientific inspectability boundaries

Phase B evidence: independently executed default depth 4 has **1,574,464 transitions, 0 failures, 80/80 discriminators**; all twelve prescribed historical modes fail owner-grounded properties; four routing tests and PEM schema validation pass; whitespace is clean. Python 3.10.12, model `d063df91b7d00c7f8ed1deb2a9b52a39910fcf6d`. Detailed counts, commands and limits are in the pinned Review §7 and workplan §27.40.

Depth 5 is **prior-session-reported reuse**, not independent execution: 99,095,037 transitions, 0 failures, 80/80 discriminators, `--jobs 4`, 62 min 52 s, model unchanged from `d3792981`. Original interpreter/raw output/environment provenance is unavailable in the recorded handoff at `8588a69dc578a545386574567d03ebeff6a1770e`. Do not silently upgrade that report or rerun the unchanged model merely to accumulate confidence. A materially changed model requires applicable revalidation; a changed architectural contract may require new discriminators even with an unchanged model.

No production SSDS owner or accepted Manual exists. Runtime fidelity, custody, class/floor enforcement, replay/incrementality, corruption handling, witness durability, publisher fencing, recovery, privacy, scaling, live usability and doctrine improvement remain **unexecuted** at their later boundaries. Green fixtures or existing Core cannot close them. Reuse prior evidence only for unchanged subjects and applicable claims; independently falsify newly specified contracts.

The Manual owes the workplan §1.4 O1 content: material admitted records/bases, publication and intake/quarantine outcomes; append-only retention with the human-gated breach exception; native scientific homes referenced by content identity; readers/routine questions; visibly marked within-deliverable query, brief, gate-core, conformance and inspector surfaces. It must preserve source/projection linkage, unavailable/stale evidence and findings/tensions visible at gates. No universal scientific observation database is requested. Mark any proposed beyond-deliverable inspectability item explicitly; technical Review cannot accept that scope extension.

This handoff reviews no realized scientific result, selects no scientific analysis/model/parameter variant and changes no retention/projection contract. Future delegates must return their material findings and triggered realized-result/variant/tension disclosures under the D3 role's scientific checks. Prior design search is not bounded by the thirteen prescribed diagnostic executions. Consequential scientific choices require their accepted owner/task binding; resources beyond negligible local diagnostics need the applicable budget/authorization, not this handoff.

## 8. Execution order and acceptance

1. Enter the authorized Phase C task and reconstruct parents, exact meanings, inherited capabilities and current gate state. Establish the bounded closure map; prioritize decision-sensitive uncertainties, not amendment count.
2. Draft coherent Manual contracts in dependency order, resolving owners/types/validity before downstream inference. Keep workplan refinements or changed assumptions explicit, route upstream changes, and record real unresolved decisions rather than patching around them.
3. Perform a minimum-architecture/capability pass and qualification-method challenge. All 27 items and every Deferred surface need substantive dispositions; stop optional polish once the Manual is precise, coherent, navigable and decision-sufficient.
4. Stabilize the draft, run applicable document/identity/routing checks, and freeze its exact commit/blob for independent D3 Review. Issue a neutral fresh-context prompt without author conclusions; identify common-mode dependencies, require whole-Manual/out-of-matrix falsification, prior-closure regression and both directions of the disagreement family. Missing required evidence is not a pass. A reviewer edits only its record and does not commit/push.
5. Verify and preserve the Review record, repair at the earliest owner within authorized scope, and re-review affected changes. Preserve NO-PASS/Serious Challenge findings and the convergence/stakeholder boundary above. Commit and push branch changes; use the existing session handoff for compact resumable state.
6. Present the independently reviewed Manual and the complete G1 criteria to the stakeholder for explicit acceptance. Include unresolved findings, evidence limitations, architectural choices and marked product-scope items; acceptance of principles or Phase B PASS is not acceptance of this Manual. Record the actual decision and bounded impact before accepted-current promotion.

| Boundary | Required evidence / authority | State at this handoff |
|---|---|---|
| Phase B | Exact-candidate independent D3 Review, including Phase A reconciliation | PASS record published; architecture still proposed |
| G1 | Workplan §25 criteria **1-8, 11, 12**; accepted Manual closes §21, independent Review and explicit stakeholder acceptance | OPEN |
| G2 | G1 plus criteria **13-14**: independently reviewed shadow D3→D4 workplan and explicit stakeholder shadow authorization | OPEN; **D4 NOT AUTHORIZED** |
| G3 | G2 plus criteria **9, 10, 15**: live/real-owner shadow evidence and independent implementation Review | Future; no execution claimed |
| G4 | G3 plus criterion **16**, per subject: cutover/quiescence, demonstrated rollback and required human/project approval | Future; no native authority |

G1 design obligations must be closed by specifications and review available in Phase C; do not require the runtime system before the gate authorizing its implementation. Equally, do not mislabel later real-owner execution as satisfied by a Manual or fixture. The separate shadow workplan and its authorization follow G1; no D4 implementation starts in Phase C.

Phase C closes only with the reviewed and explicitly accepted Manual, complete G1 reconciliation, bounded dependent/history/evidence impact and truthful coordination state. Otherwise report the earliest-owner blockers, missing decisions/evidence and next authorized action. §26 remains the full reopen owner. The next task begins with **Manual authoring**, not another unchanged Phase B diagnostic sweep.
