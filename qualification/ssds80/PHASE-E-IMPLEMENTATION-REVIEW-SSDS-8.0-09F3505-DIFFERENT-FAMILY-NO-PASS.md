# Independent Review — SSDS 8.0 Phase E and Manual amendment A9 — NO-PASS / A9 PASS

```text
GOVERNING SSDP: 7.2.1
  public source: aaeaf8b6b2121b9fb8aba31917c8265649c43954
  recovery: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
HANDOFF ENVELOPE: 55e6f3a7b144a6ec3110b56dbd3f6b343cb444c1
  qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-HANDOFF-SSDS-8.0-09F3505.md
CANDIDATE: 09f35057aec00467372aa8fbbda37f540a9bbc1f
BASELINE: 55c01a8369037465aa4fdb776b115b89041b177e
SCOPE: Phase E implementation and exit; A9 as proposed D3 and its genesis realization
MANUAL: orchestrator/docs/ssds-8.0-architecture.md
  blob: 25122b5e2bf0f5c7755afe0cc32161aa5a6215c4
CATALOGUE blob: f4c515bb1c3d7d5cdc3b762a18dcf2f67bbe5341
PHASE E PLAN blob: d9c7b0f2a316eef89ba29c9fa5308fcd7f4ed430
G2 WORKPLAN blob: f3596966c06ff9fb51838352a774838f2cb6fecd
REVIEW METHOD: independent owner reconstruction, bounded Challenge Pass,
  assembled-behavior counterexamples, prescribed regression, repair reversions,
  and A9 guard mutations; author readings treated as hypotheses
REVIEWER: OpenAI GPT family (Codex); launched through the Codex CLI in the
  stakeholder's own terminal at the stakeholder's request. The author's session
  typed only the handoff pointer supplied as the engagement prompt. This context
  did not author the candidate. The author and prior step reviewers are Claude-family.
DATE: 2026-10-22
SCRATCH: /tmp/ssds80-phase-e-review-09f3505
```

## SERIOUS CHALLENGE

No new SERIOUS CHALLENGE survives this Review. The six findings below violate coherent accepted D3; none requires weakening it. In particular, the subject's separate `ACCEPT` obligation cannot replace the evidence and disagreement terms that §10.4 explicitly requires the item's own discharge to read.

SC-E1 is well founded against the pre-A9 baseline. SD-61 selects its architectural resolution; A9 states that resolution adequately. A9 remains proposed until the stakeholder accepts its wording. This technical PASS does not perform that acceptance, amend an admitted genesis, or authorize a replacement genesis.

## Verdict

**Phase E implementation: NO-PASS. Phase E exit: NO-PASS. Neither the implementation nor the exit passes.** Six counterexamples through the real package expose false discharge, false evidence support, lost review findings, incomplete review context, substituted governing text, and lost visibility of a qualified gate. Passing the recorded routing matrix and regression suites does not cure these defects. Phase F's dependent work must not start on the strength of this Review.

**Amendment A9 as a D3 change: PASS. A9 as realized at the named genesis preparation/admission boundaries: PASS.** Its continuing structural invariant also binds Phase F's general Admission implementation; this Review does not qualify that unbuilt path. The interim pre-A9 protection is sound within the shadow boundary and must remain until the replacement shadow genesis is separately approved and admitted.

The highest-consequence defects are B1 and B2: the system can call work fully discharged while its evidence is disputed, and can tell a human that a required premise holds when the production evidence predicate is false. B3–B6 independently block the Phase E interface deliverable.

## Phase E blockers

All locators below refer to the pinned candidate. Scratch `probes.py` and `probes.log` contain the executed constructions and results. The test helpers construct ledger records and trees; the production `ssds` package performs derivation and rendering. No semantic owner is mocked in these counterexamples. Numeric predicate values are `F=0`, `P=1`, `T=2`.

### B1 — An integrated item stays fully discharged after its subject's evidence becomes disputed

**Owner:** Manual §10.4, including “Discharge is not latched” (SD-36), and the settled catalogue §10.4 predicate: discharge reads `ev(subject(o), e)` and `qual(subject(o))`; the item's subject is the union of the subjects its integrated enactments changed. `P` is permitted only within the applicable provisional scope or policy, and must never be reported as unqualified discharge.

**Implementation:** `derivation/items.py:313`, `ItemObligation.predicate`, checks clean conformance, the latest integrated review, challenge status and gates, but omits the subject's `ev` and `qual` terms. This is the gap reading E30 acknowledges and postpones.

**Executed trajectory:** Construct a lint-clean `DOCUMENT` item writing a D4 `records` unit, with `TEST_INTEGRITY.no_skips` and `BOUNDARY.write_scope` secondaries. Policy requires evidence obligation `health` for D4. Admit a realization claiming the candidate's `records` revision, a passing `health` assessment, an independent passing review, and integrate. Then admit a failing assessment on that realization and obligation, without changing content or the review.

```text
lint findings: []
before: ev(records, health)=T; item=DISCHARGED
after:  ev(records, health)=P; qual(records)=P
        item=DISCHARGED; route=discharged
subjects(item)={records}; no provisional permission was supplied
```

The newly admitted adverse assessment is never-lost evidence, not an integration that Admission could prevent by checking collateral regression. The item's predicate must be recomputed. A separate subject acceptance does not satisfy this item's mandatory terms.

**Minimum repair:** Compose the production evidence and disagreement terms into the item's predicate over its complete integrated subject set, preserving the declared provisional-scope rules and partition behavior. Remove E30's attempted deferral of this already-owned S3 behavior.

**Discriminator:** The trajectory above must change full discharge to `OPEN` without provisional permission, or to `DISCHARGED_PROVISIONAL` only with applicable permission. Also exercise a failure affecting a subject changed by an earlier retained enactment and a partitioned item. No case may remain fully `DISCHARGED` with an input at `P` or `F`.

### B2 — Required-evidence presentation promotes a non-current assessment into a holding gate premise

**Owner:** Manual §16.2 evidence statuses and §16.6's required-evidence core: it shows holding evidence through passing admissible assessments at the rendering head, or shows that it does not hold. §5.5's production evidence predicate owns that meaning.

**Implementation:** `derivation/queries.py:211`, `evidence`, labels an assessment `current` from the absence of staleness/dispute without requiring `d.current(r)>F`. It can emit `status=current` alongside `current=F`. `derivation/briefing.py:221`, `required_evidence`, subsequently treats that status string as the support test and drops the contradictory currentness field from the records it presents. The gate renderer consumes this projection.

**Executed trajectory:** Using `test_assessment.Runs`, admit a passing assessment with its realization and specification premises, then a blocking challenge targeting that assessment.

```text
assessment currentness: T -> F
ev(code, obl)=F
ask/evidence projection: outcome=PASS, status=current, current=F
briefing.required_evidence(code):
  obligation=obl, holds=true, status=holding, via=[the challenged assessment]
```

This is a consequential misstatement in the human evidence core, not merely an awkward label. It can make an unavailable supporting premise appear established while the underlying owner correctly rejects it.

**Minimum repair:** Derive holding/status/supporting-premise selection from the actual currentness, admissibility, evidence and disagreement owners. Preserve `P`, challenges, loss withholding and stale/history distinctions; do not repair only the displayed word while retaining false `holds` or `via` values.

**Discriminator:** The challenged-assessment trajectory must yield `holds=false`, no supporting `via`, and an explicit reason in both query and gate projections. Add corresponding provisional and superseded-assessment controls. An inadmissible historical PASS must never become a current supporting premise.

### B3 — A prose amendment loses earlier unresolved findings from a re-review brief

**Owner:** Manual §16.5: a re-review carries earlier findings on the same plan subject unless a later independent, acting, unvetoed review records them `RESOLVED`. This carry is broader than the adverse judgment's present veto reach.

**Implementation:** `derivation/briefing.py:137`, `_unresolved_reviews`, searches only `w.items.holders`, whose root is the currently derived work keys. A prose amendment replaces the item obligation; the earlier obligation's enactments disappear from that search. The separate standing-adverse reach pass cannot recover findings when the next candidate has different content.

**Executed trajectory:** With `test_routes.Flow`, submit candidate 1 and admit `NO_PASS` with an in-scope finding on `records`/`o1`. Change the item's prose, accept the changed plan, and submit candidate 2 with different `records` content. No review resolves the earlier finding.

```text
earlier review: sha256:390f9b955aceecb1e91caa73c5027121c08358a252d214a154930a275a1a41bd
stands_adverse(earlier)=true
findings_of(earlier)=[{obligation:o1, units:[records], detail:FIRST_FINDING}]
briefing.carried(REVIEW(candidate2))=[]
rendered Carried objections section: none
```

**Minimum repair:** Find earlier reviews by admitted plan/work history, including replaced/removed item obligations and superseded partitions; retain the owner's explicit resolution test. Do not broaden veto reach to compensate for a missing historical carry.

**Discriminator:** The trajectory above must carry the complete earlier finding as another judge's, with its review identity. A later independent qualifying `RESOLVED` record should remove it; a prose amendment, replacement partition, different candidate content, or author claim alone must not.

### B4 — A review brief contains a path summary in place of the candidate diff

**Owner:** Manual §16.5 requires the candidate diff and machine-produced facts in the review brief. A reviewer must be able to inspect the actual proposed change while receiving the required independent context.

**Implementation:** `interface/render.py:502`, `review`, builds “Candidate diff and machine-produced facts” solely as `path: added/removed/changed`. It includes neither before/after content nor a resolvable candidate/base binding sufficient to supply that content as the prescribed diff.

**Executed discriminator pair:** Independently submit `# Records\nREVIEW_PROBE_ALPHA\n` and `# Records\nREVIEW_PROBE_BETA\n` through `Flow`. Both clean candidates derive `REVIEW(X)`. Both sections are exactly:

```text
- records.md: changed
```

Neither candidate's changed text nor its candidate commit appears anywhere in its review brief. The transformation identity appears in the header, but is not a diff. The existing `ReviewBriefs.test_contains_and_excludes` checks for `records.md`, which this incomplete projection satisfies.

**Minimum repair:** Render an identity-bound diff from the real content/frame owner, with actual before/after changes and relevant type/mode facts. Supply truthful limitations and exact retrieval bindings for content that cannot safely be inlined. Preserve the author's narrative/outcome exclusions.

**Discriminator:** Two different changes to the same path must expose their different actual edits, bound to the correct base, candidate and transformation. Include deletion and mode/type changes. A path name or a section heading alone must fail the oracle.

### B5 — Governing text at head is substituted for the contract's named revision

**Owner:** Manual §16.3(3): the exact text of governing units at the basis revisions is inline. The revision binding is substantive; a notice naming the old digest does not make different text that text.

**Implementation:** `interface/render.py:345`, `_governing_inline`, always calls `_unit_text(unit)` on the current view. When the requested revision differs, it merely adds a parenthetical notice and renders the current bytes.

**Executed trajectory:** Add `design@<old revision>` to a `Flow` item's governing entries and accept it. Absorb a later edit of `design.md`. Render the still-derived item obligation. Its governing section names the old digest in a parenthetical but contains `REVIEW_PROBE_NEW_GOVERNING_TEXT` from the later revision. The production `issuable` query still returns true; even a waiting obligation's unissued brief would owe an honest projection.

**Minimum repair:** Resolve each requested revision through the historical content owner and render those exact bytes. If unavailable, report unavailable context rather than substituting a later version. Keep current-versus-bound comparisons separately labeled.

**Discriminator:** Change a governing unit after an item's binding; the bound old text must remain the governing content, and the new text must not replace it. Exercise historical-item review briefs and missing-revision refusal/incompleteness as well as current task briefs.

### B6 — A qualified gate disappears from the inspector without supersession, even within one tenure

**Owner:** Manual §16.8: a qualified gate ACCEPT stays an inspector entry in every state where it is eligible until superseded, naming its qualifying records. This covers the current tenure as well as tenure restarts.

**Implementation:** `derivation/workflow.py:220`, `_subject_obligations`, derives a gate only when `gterm==F`. A qualified ACCEPT caps `gterm` at `P`, so the gate obligation disappears. `interface/render.py:724`, `inspector`, considers derived obligations only and has no separate projection of those still-effective qualified gate decisions.

**Executed trajectory:** Construct a D3 `arch` subject with required gate `g` and a named human gate holder. Admit that holder's `ACCEPT` with `adequacy=ADEQUATE`, `qualification=QUALIFIED` and the content premise. No tenure restart or supersession occurs.

```text
current(gate decision)=T; gterm(arch,g)=P
derived GATE obligations=[]
inspector: no entry for this gate or its qualifying decision
```

Other human-attention/acceptance entries can remain; they do not name this decision or replace its required visibility. E38's disclosed omission of qualified-gate entries across a tenure restart understates the defect: the immediate same-tenure case fails too.

**Minimum repair:** Project every eligible qualified gate decision through an owner-derived inspector entry until valid supersession, separately from whether another gate answer is owed. Preserve run/tenure eligibility and expose the qualification premises.

**Discriminator:** Same-tenure qualified ACCEPT remains visible, with its qualifying records, after later unrelated admissions and after an additional unqualified decision that does not supersede it. Authorized supersession removes the old qualifying entry. Then exercise the disclosed tenure-restart case.

## Step-review closure audit

The historical repairs are substantive, not merely claimed in prose. The candidate's full suite passes. I also copied production sources to scratch and, for each repair commit below, restored its changed production files to the parent versions while retaining candidate tests. These are **repair-reversion variants**, not complete historical checkouts or independent one-defect mutants. The selected tests are all green on the candidate. A failure count can include multiple subtests; errors are reported separately.

| Repair reverted | Selected candidate tests | Executed result |
| --- | --- | --- |
| step 3, `f4fb53d1` | `test_obligations`, `test_runs`, `test_lint` | 47 tests; 10 assertion failures, 0 errors |
| step 4, `8165f24f` | `test_conformance_review` | 13 tests; 21 assertion/subtest failures, 0 errors |
| step 5, `434454f6` | `test_step5_review` classes Partitions, Escalation, Routes, FindingsSurvive, Floors, Index, Identity | 24 tests; 21 assertion/subtest failures, 4 errors |
| step 6, `fc7577b9` | `test_interface` | 21 tests; 4 assertion failures, 2 errors |
| step 7, `412fe009` | `test_briefs.StepSevenReview` | 13 tests; 11 assertion/subtest failures, 2 errors |

The step 5 errors are missing expected decisions/floor entries in the old behavior; step 6's two errors concern changed query item shapes; step 7's errors concern the absent contract section and absent `waits` method. These do not substitute for isolated semantic mutation evidence. Logs are `step3-reversion.log` through `step7-reversion.log` under scratch.

The following accounts for **each numbered blocker actually described in the plan**. “Closed” means its recorded discriminator is repaired at its owner and exercised by the candidate tests, not that all related trajectories are correct.

| Step / blocker | Owner and discriminating test or test group | Judgment |
| --- | --- | --- |
| 3 B1 | `runs.assessment_records`; `test_runs.RunCurrency.test_only_the_author_tasks_result_is_a_revision_assessment` | closed |
| 3 B2 | `Workflow._qualifies`; `ReviewRepairs.test_an_unqualified_pass_discharges_nothing` | closed |
| 3 B3 | `Workflow.discharge` existential; `test_discharge_and_refusal_do_not_depend_on_the_order_of_admission` | closed |
| 3 B4 | `_spec_and_invariant_obligations`; `SpecAndInvariant.test_a_refused_review_is_never_retired_by_a_later_change` | closed |
| 3 B5 | `covered`/provisional scope; `test_a_provisional_plan_acceptance_covers_only_inside_a_scope` | closed |
| 3 B6 | plan lint protected surfaces; `test_lint.Lint.test_scope_refusals` | closed |
| 3 B7 | `_revalidations`; `test_revalidation_only_for_a_passing_independent_judgment_once_current` | closed for its recorded cases |
| 3 B8 | disagreement derivation; `test_a_disagreement_ends_with_the_vetoed_judgments_supersession` | closed |
| 4 B1 | automatic conformance templates; `ContractBoundariesAlwaysRun.test_frozen_tests_and_artifacts` | closed |
| 4 B2 | `Conformance.contract` binding and nonrecursive `Workflow.binding_index`; schema-valid result/review tests in `test_conformance` and `ReviewOfX` | repaired; candidate tests execute the corrected grammar/path; not isolated in my reversion workload |
| 4 B3 | deviations over boundary/test-integrity hits; `Disclosure.test_any_boundary_breach` | closed |
| 4 B4 | frame existence; `MissingFrame.test_a_named_transformation_without_a_frame_is_incomplete` | closed |
| 4 B5 | unsupported inputs fail incomplete; `UnanalyzedSurfaces.test_other_languages` | closed |
| 4 B6 | Python skip/collection facts; `UnanalyzedSurfaces.test_python_skip_forms` | closed for the represented forms |
| 4 B7 | requirement/manifest analysis; `Dependencies.test_forms` | closed for the represented forms |
| 4 B8 | path-aware protected surfaces; `ProtectedAndUncovered.test_a_protected_path_owned_by_no_unit` | closed |
| 4 B9 | current exact observations, any failure, HARD/SIGNAL distinction; `Runner.test_rerun_and_signal` | closed for the recorded observation cases |
| 4 B10 | machinery realization requirement; `Evidence.test_an_agents_own_realization_is_no_evidence` | closed; designation remains F |
| 4 B11 | scientific review system slots; `ReviewOfX.test_a_scientific_review_needs_its_bidirectional_slot` | closed |
| 4 B12 | unit analyzer; `Units.test_literal_factors_and_compound_statements` | closed for these bounded static facts |
| 4 B13 | `Workflow.covers_outputs`; `ReviewOfX.test_a_review_citing_none_of_the_judged_content_does_not_discharge` | closed |
| 5 B1 | required parts; `Partitions.test_b1_a_repartition_keeps_an_undischarged_sibling` | closed |
| 5 B2 | answer classes/escalation attention; three `Escalation.test_b2_*` tests | closed |
| 5 B3 | latest pending result's route; `Routes.test_b3_a_later_candidates_out_of_scope_no_pass_reaches_the_principal` | closed |
| 5 B4 | latest integration by position; `Partitions.test_b4_the_item_level_target_is_the_latest_integration` | closed |
| 5 B5 | latched objective/criterion floors; two `Floors.test_b5_*` tests | closed |
| 5 B6 | equal-level policy floor; `Floors.test_b6_a_policy_floor_equal_to_the_declared_level_is_a_floor` | closed |
| 5 B7 | admission/current domain floors; `Floors.test_b7_a_floor_outlives_its_target_unit` | closed |
| 5 B8 | disagreement latch; `Floors.test_b8_the_disagreement_floor_latches` | closed |
| 5 B9 | item-level objections; both `Partitions.test_b9_*` tests | closed for the recorded named/no-part trajectories |
| 5 B10 | orphan routed findings; both `FindingsSurvive.test_b10_*` tests | closed for routed out-of-scope findings; this does not close B3's different review-brief carry |
| 5 B11 | settled refused/missing amendment; both `Routes.test_b11_*` tests | closed |
| 5 B12 | invalid partition never answers; `Partitions.test_b12_an_invalid_partition_answers_nothing` | closed |
| 5 B13 | typed conjunctive scope; `Routes.test_b13_findings_in_scope_only_within_write_scope_and_obligations` | closed |
| 5 B14 | real-owner lifecycle; `Lifecycle`, named `LifecycleFull` | sample freshly passed; full enumeration reused as qualified below |
| 6 B1 | depends widening/labels; `StepSixReview.test_b1_depends_claims_no_exactness_it_lacks` | closed |
| 6 B2 | dispute/unavailable/drift projections; two `StepSixReview.test_b2_*` tests | recorded cases closed; challenged supporting evidence still fails B2 above |
| 6 B3 | transitive lineage; `StepSixReview.test_b3_tensions_and_locate_follow_lineage` | closed |
| 6 B4 | NF5 and read-only commands; both `Commands.test_b4_*` tests | evidence added and passed; reverting a previously correct implementation need not fail newly added tests |
| 7 B1 | work/domain owner; `StepSevenReview.test_b1_a_review_of_authority_work_carries_its_domain` | closed |
| 7 B2 | events over work; `test_b2_and_b3_events_over_the_work` | closed for recorded events |
| 7 B3 | definition injection; same test | closed for represented declarations |
| 7 B4 | judgment reach and historical carries; three `test_b4_*` tests | recorded cases repaired; **not fully closed**, B3 above |
| 7 B5 | contract and item prose; `test_b5_the_review_brief_carries_the_contract_and_the_item` | recorded case closed; B4/B5 above expose other missing/wrong review context |
| 7 B6 | required-evidence gate core; `test_b6_and_b7_the_gate_core_and_the_inspector`, D2 readiness test | recorded failure/unavailable cases repaired; **not fully closed**, B2 above |
| 7 B7 | all human decisions in inspector; `test_b6_and_b7_the_gate_core_and_the_inspector` | recorded open-obligation cases repaired; **not fully closed**, B6 above |
| 7 B8 | owner-derived outcomes/contract lint; `test_b8_decision_outcomes_are_the_owners` | closed |
| 7 B9 | owner-derived drift changes; `test_b9_the_drift_brief_names_the_moving_change` | closed |
| 7 B10 | source-version mismatch; `test_b10_a_mismatching_doctrine_source_is_not_applied` | closed for mismatch; public-source resolution still F |
| 7 B11 | event absence/presence, dependency weights; `test_b11_every_event_and_its_absence`, `test_b11_weight_follows_item_dependencies` | stronger tests exist; **not a general oracle-strength closure**, B2–B6 survive the suite |

The known non-latching subject-evidence gap was not cured by the step 5 repair: B1 executes it. Repair it at the item predicate, not by increasing test counts or adding a renderer guard. The step 7 consolidation into `Briefing` is a useful ownership improvement, but B2/B3 show that the new projection still reconstructs some semantics incompletely. No general architectural replacement is required by the evidence collected here.

## Readings E1–E38 and the phase boundary

| Readings | Judgment |
| --- | --- |
| E1–E3 | Unissued, read-only operations and qualified presentation are appropriate; `Home`/`AdmissionHome` split and root wiring respect the declared component boundary. No task/read-recording claim is made prematurely. |
| E4–E8 | Deterministic identities, derived lint, missing-execution incompleteness, campaign-only HARD qualification and the bounded analyzer set are appropriate. E6's missing observation parameters/designation remain explicit F obligations, not accepted runner evidence. |
| E9 | The intended version-bound reader remains correct, but E37 acknowledges that Phase E does not actually perform Core's full public-source resolution. Treat that as unfinished F integration, not as proof that a matching version file establishes public-source identity. |
| E10–E14 | Closed policy choices, transports, candidate-only search, explicit history and inspector dependency weights are reasonable bounded concretizations. They do not waive any readiness/discharge term. |
| E15 | The sample/full split and P1–P6 versus fence/P7 split are honestly stated and permitted by this handoff. Evidence reuse is qualified below. |
| E16–E21 | Local prose-reference grammar, exact revision syntax, stricter whole-plan review, derived runs, deferred runner designation and layer/gate mapping are consistent with their owners in the examined cases. |
| E22–E23 | Revised slot coverage retains `o1_content` for AUTHOR and scientific obligations rather than narrowing it. Eligibility fails closed on unknown authorship/lineage. No new weakening found in these readings. |
| E24 | The closed continuation object realizes §10.5 rather than the earlier narrower list. This additive schema-1 correction has no admitted override to reinterpret in the shadow ledger; prohibited kinds remain prohibited. It is not evidence of compatibility with an old reader accepting new grammar. |
| E25–E29 | Set-valued conformance, mandatory boundary/expectation checks, typed/NONE slots, bounded Python facts and the explicit UCUM subset are honest static concretizations within their declared limits. Their execution does not establish scientific adequacy. No further authority change is justified by this Review. |
| **E30** | **Unfaithful in the consequential sentence postponing the item's `ev`/`qual` terms to F.** The subject's ACCEPT does not replace §10.4. B1 falsifies the justification. The other revised scope/pending-candidate choices have tests and preserve the recorded finding routes. |
| E31–E32 | Answer-qualified chains, visible waits, invalid-partition nonanswers and preservation of siblings realize the settled register on the exercised histories. Missing/refused AMEND is a conservative visible continuation. Fence behavior and Admission legality remain F. Part-index ambiguity and all repartition histories are not exhaustively qualified here. |
| E33–E35 | The interim uncovered-path check, early/latched D1/D2 floor, and report persistence are conservative for the shadow. Human decisions stay separate from principal decisions. The disclosed missing merge/upgrade and qualification machinery cannot be counted as implemented. |
| **E36** | The corrected widening and lineage rules are supported on their recorded cases. **The evidence-status interpretation is incomplete/unfaithful where it calls non-current support current; B2.** |
| **E37** | Optional doctrine grammar and source-version rejection are sound as draft-brief functionality. A version match is not Core public-source resolution. Full identity resolution must precede issued native briefs in F. |
| **E38** | Consolidating derived facts is appropriate. **Its complete projection claim is false:** B3 loses same-plan findings; B2 misstates supporting premises; B4/B5 omit or substitute context; B6 loses qualified gates before any restart. Its qualification-visibility limitation is materially understated. |

Plan §6 is **not an honest complete account of what prevents Phase E completion**. The later-phase implementation list is broadly explicit, but it does not turn B1 into F work, and “fails toward not supported” is false for B1/B2. Several E38 omissions are discoverable only in E38 although it labels them “Not realized (§6)”; §6 does not enumerate them. The missing same-tenure gate entry is not disclosed there or in E38. Reconcile the scope/limitations after repairs; do not simply relabel these accepted Phase E obligations as future work.

## Exit evidence, later phases, and non-blocking findings

**Group 5:** The real-owner routing, partition, identity and revision-run tests execute; production code does not import the Stage S models. The current S3 model list contains **31** routing cases, consisting of the handoff's 26 non-fence cases and five fence cases. “32” in the plans is a count error, not evidence of a missing thirty-second named case. The five actual fence cases are `kept_fence_recurrence_human_decline_resumes`, `kept_fence_decline_resumes`, `kept_fence_decline_then_budget`, `kept_fence_amend_elsewhere_integrated`, and `fence_awaiting`. They and P7 legitimately belong to F's publication/fence owner. The S5 admission refusals likewise belong to F. None of those deferrals explains B1.

**Lifecycle:** The in-suite real-owner sample passed afresh. I independently counted 3,627 chains per condition, agreeing with the recorded full real-owner total of 7,254. I did **not** rerun the roughly 25-minute `SSDS_SLOW=1 tests.ssds.test_step5_review.LifecycleFull` workload. I reviewed the plan's recorded 1,412-second result and the named slow implementation. The post-step-7 item delta adds `drift_changes`, and the reports delta factors the same report-outcome computation; the lifecycle replay's routing/answer logic is preserved. This supports bounded reuse of the recorded routing result, not a claim of a fresh full run or independent raw-log/interpreter verification. The model's separate 14,508-chain run executed freshly and is diagnostic evidence only.

**Group 6:** I reproduced the collection: **392 states from 110 tests**, zero source-test failures/errors, and zero `stranded` findings. Its scope is the explicit `GROUPS` list. **N2, non-blocking oracle limitation:** its generic property does not independently establish the full non-current-judgment half of §10.3. In the existing challenged-premise acceptance trajectory, replacing `Workflow._revalidations` with an empty result removes both revalidation routes yet `stranded(w)` still returns `[]`. The direct `test_a_non_current_answer_is_revalidated` does discriminate that behavior, and is run inside the group collector; therefore this is not a claim that the entire group test accepts that mutant. It is a limit on the advertised per-state property and a reason to strengthen its dependency-based check. Do not infer universal no-stranding from the 392-state count.

**End-to-end shadow run:** I reviewed the recorded `ssdp-shadow` qualified position-0 result, named head `sha256:69a182a6800c144591d6f1d5d6659eca2b09c78ac651d2ab81f05b00fb876ad2`, legacy/ungoverned statuses, empty native work and unchanged refs/objects/status/high-water mark. Those are internally consistent with a shadow genesis containing no native subjects. I did not read or alter the stakeholder's private home. Candidate CLI/Interface tests independently prepare throwaway homes, qualify/read/render through the root module, exercise unqualified/refusal paths and check product state; they passed. The private record establishes that recorded genesis path, not the behavior of native review/gate briefs with substantive work.

**N1, non-blocking accounting/traceability:** The plan describes step 5 as finding “fifteen blockers” but enumerates B1–B14 only. I accounted for all fourteen it actually describes; an unnamed fifteenth blocker cannot be inferred closed. Correct that count or identify the missing finding. The same accounting discipline applies to S3's 31-versus-32 count.

**Later-phase findings/obligations:** F owns actual dispatch, lineage/issue credentials, task envelopes, recorded reads, runner designation, parameter-bound observations, Admission's role/refusal checks, fences and the three S5 admission cases. It also owes complete public-source resolution, rederived conformance at integration after a clean rebase, the findings-only investigation completion path, and complete realization machinery. General Admission must enforce A9 after genesis, including attempts to remove/narrow the reserved owner. G owns intake routing, migration and external pilots. H and separately authorized G3 campaigns own adversarial/fault and live burden/doctrine evidence. Merging/upgrading/annotations, omitted inspector/brief notices, and the disclosed specification-change stale-failure review item remain explicit unfinished obligations at their §15/§16 owners; this Review does not waive them for G3. B1–B6 above are Phase E repairs, not members of this later-work allowance.

## Amendment A9 and shadow/frozen boundaries

A9 makes the missing outer owner mandatory at its structural owner (§1.8/§1.9) and explains why effect-keyed writes, boundary checks, Admission proof and impact must see changes. The empty-prefix reservation and special outermost fallback agree with the existing partition construction: other units retain their own bytes; otherwise unowned governed bytes fall to `ssds.unclassified`. It does not create native acceptance, change the domain rule, broaden an implementer's write scope, or make ignored/untracked content governed. §19 Case C can still start with coarse ungoverned subjects, now with this mandatory fallback; no fine scientific reconstruction is demanded at genesis. Mature repositories and §19.9 shadow genesis retain their existing migration/authority boundaries.

The wording is a small owner-local change. Apart from proposed-status/header material, the Manual delta is §1.8 and §1.9; the catalogue is byte-unchanged. No new competing write-set mechanism is introduced.

`derivation.baseline.genesis_structure_problems` is used by preparation through `baseline_structure`, and by `admission.genesis.genesis_violations`. The two A9 tests pass. I separately disabled the preparation guard and the admission guard in memory: each corresponding test failed at its expected assertion, with no test errors. An additional direct content-owner check produced a valid baseline with the fallback, then added `new-root.txt`: its owner was `ssds.unclassified` and the real write set contained `ssds.unclassified`. These establish the named genesis realization; they do not qualify future general integration.

E33 preserves pre-A9 ledgers rather than rewriting their signed history. Its uncovered-path and protected-path negative tests pass, and fail under the step 4 production reversion. Keeping that stricter fail-closed shadow check while the admitted ledger lacks the new leaf is appropriate. Leave the old ledger untouched under P2; prepare/admit a replacement only through the separate human approval procedure after A9's acceptance. Do not retire the interim check merely because this review file exists.

Frozen comparison against `55c01a83` found no changes in `source/`, `dist/`, frozen Core protocol resources or `orchestrator/docs/architecture.md`. Core's source delta is limited to the additive facade exports `ssds_home`, `profile_for_protocol`, and the latter's read-only lookup implementation. Its existing tests are byte-unchanged. The snapshot check and Core suite passed. Fitness tests, including the binding/evaluation-order sensor changes and component dependency rules, passed; they are bounded static sensors, not a general capability-security proof.

The Phase E operations read/derive/render; their only intended operator mutation is the checked high-water raise. `HomeAccess` checks before reads and again before raising, with the private atomic-write owner preserved. Admission's key/workspace methods stay on `AdmissionHome`. Tests exercise the non-root permission boundary, symlink/refusal cases, high-water monotonicity and read-only product state. No shadow-boundary breach was observed. Neither private operator state nor a product ledger was modified by this Review.

## Verification, provenance and gaps

Execution used CPython **3.11.15**, UID **1000**, in the prescribed scratch directory, with a scratch venv, caches, temporary homes and candidate checkout. The initial archive lacked Git metadata; I supplied a scratch shared-object clone detached at the exact candidate before final regression. An initial attempt to export `GIT_DIR` globally contaminated child fixture Git commands; the final runs use the scratch checkout's own metadata without that export. Initial network-restricted installation/build attempts failed; the authorized network-enabled dependency install and Core build completed. These initial environment failures are retained in scratch logs and are not candidate findings.

| Required command/check at the candidate | Final result |
| --- | --- |
| `python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt` | completed in scratch venv |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | **448 run, 0 failures/errors, 2 skips**; both skips are the optional slow class's methods; non-root permission tests executed |
| `python orchestrator/scripts/run_core_tests.py` | **393 tests across 13 modules, OK**, installed-product build included |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | current 7.2 snapshot matches; frozen snapshots coherent |
| `python -m unittest discover -s tests -v` | **435 run, 0 failures/errors, 3 skips**; optional remote 6.2/6.3/6.4 fallback realizations not enabled |
| `python3 -I qualification/ssds80/models/run_models.py --seeds` | **OK**, settled cases/seeds pass; intentionally refuted historical readings report their expected misses |
| `git diff --check 55c01a83 09f35057` | clean |
| project-memory validator | schema 1 valid; 5 families, 0 notices |
| independent probes | six material defect families reproduced; seven executed constructions because B4 used two candidates |
| repair-reversion variants | five executed; every variant detected, with the error limitations above |
| A9 guard variants | unmodified two-test control green; preparation-disabled and admission-disabled variants each detected |

Final logs: `install-network.log`, `ssds-suite-rerun.log`, `core-suite-rerun.log`, `repo-suite-rerun.log`, `models.log`, `repair-reversions.log`, `step*-reversion.log`, `a9-mutations.log`, `probes.log`, `final-checks.log`, all under scratch. The report preserves the decisive trajectories so their meaning does not depend on scratch retention.

Required unavailable or unfinished evidence is not counted as a pass. Specific gaps are the unrerun full real-owner lifecycle enumeration, independent raw verification of its recorded environment, the private-ledger rerun, optional remote historical fallback probes, exhaustive analyzer/language/partition/adversarial coverage, and unbuilt later-phase production owners. I did not execute live agents, scientific workloads, campaigns, native cutover, or runtime qualification. Historical grouped repair reversions do not prove one-to-one detection of every original defect; the closure table states the bounded test/inspection support instead.

The G2 workplan explicitly activates project PEM. Its integrated base independently resolves on designated `main` to `af0455753e20ee54a969c844872e29e270007211`; its PEM blob is `1561797125622f355f84eb27319f87e8fa4227d9`, byte-identical at the candidate. No additional branch delta was composed. Schema/publication validation passed; partial historical coverage remains partial. Task-local HAS:

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen resources preserved under the independently binding G2 workplan and Manual/Core boundaries.
  - id: DS-001
    disposition: APPLICABLE
    reason: Green fixture and model evidence must be tested against real semantic consumers; B1-B6 supply counterexamples.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No source-to-generated-package route repair is performed.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No immutable public-source publication or release identity is created.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: This review publishes no bootstrap and performs no fallback designation.
```

PEM supplies hypotheses and preservation reminders, not an additional authority or a claim of schema-qualified recurrence. No memory file was changed.

## Scientific checks and common-mode limits

- **Material findings:** B1–B6 above. No new upstream Serious Challenge or scientific tension survives the bounded Challenge Pass.
- **Realized scientific results/null envelope:** I produced, ran and reviewed **no realized scientific results**. All executions were synthetic software/qualification diagnostics. Examined areas are the pinned Phase E semantic paths, selected historical repairs, regression and A9 genesis boundary. Scientific model validity, numerical convergence/accuracy and empirical outcome improvement were not evaluated and no such claim is made.
- **Variants:** Seven counterexample constructions across six defect families; five grouped historical production-reversion variants; two A9 guard-removal variants with an unmodified control; one revalidation-removal oracle probe and one successful A9 new-file ownership probe. Selection was consequence-driven: current support, lost findings/attention, exact context binding, and the claimed repairs. These are exploratory engineering probes, not a pre-registered scientific variant search or evidence of held-out performance.
- **Tension search:** No consequential judgment here relies on accepted D1/D2 scientific authority; therefore no scientific tension-search result is claimed. The synthetic D4 evidence terms test D3 semantics, not a scientific claim. The architectural Challenge Pass considered A9's coverage/overlap and migration consequences, lost objections, non-latching evidence, visibility of qualifications and exact source bindings; no argument for weakening the accepted architecture survived.
- **Unanswered parts:** The explicit gaps above remain gaps; sampled or inherited evidence is not presented as exhaustive fresh execution.

This is a different-family review from the Claude-family author and step reviewers, with fresh-context process separation. It still shares the Manual, catalogue, author-built fixtures, expected-value corpus, Python/Git toolchain and qualification environment. The historical reversions share those tests and are correlated evidence. The new real-owner trajectories reduce that common-mode risk but do not establish universal semantic adequacy or live operational fitness.

Nothing in this record accepts the implementation at G3, accepts A9 for the stakeholder, authorizes a new genesis signature, starts a campaign, changes subject authority, permits cutover/G4, or authorizes anything beyond the existing shadow scope. No commit or push was made; the sole repository write is this review record.
