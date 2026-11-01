Governing SSDP version: 7.2.1.

# SSDS 8 Phase F exit evidence (step 12) at `c8122d66`

This file assembles Phase F's exit for the G2 workplan's Phase F row (§5.2): acceptance group 4, the admission halves
of groups 2, 3 and 5, the end-to-end shadow run, and the classified differences from document control. It assembles
evidence recorded elsewhere and names each owner. It accepts nothing: the independent implementation Review (plan §3,
G2 workplan §5.1 item 5) judges it, and acceptance is the stakeholder's. A case not executed is reported as
unexecuted, never as passed (Manual §31.2; plan §4).

## 1. The candidate

- **Candidate:** `c8122d66edbf7d19320f7b155e0c31033566b854` (plan revision 74). `orchestrator/` at the evidence
  commits equals it.
- **Program suite at the candidate:** 1,911 tests OK, 10 skipped, on the pinned runtime, with the installed-product
  build reaching PyPI (plan revision 74).
- **Repository acceptance:** release state, PEM, protocol snapshot, skill packages built and validated, dist
  parity and `git diff --check` pass (revision 74). The root regression passes since SD-99 (revision 75).
- **Focused re-run for this file** (2026-11-01, the pinned runtime, `-B`): the modules cited in §2 below, run
  together. Result in §6.

## 2. Acceptance groups

Status words:
- **executed:** a test at the real owner asserts the case's stated outcome;
- **executed, uncited:** as executed, but the test does not cite the case or discriminator by name, which plan §4
  asks for. The mapping comes from the plan's step record and is for the Review to confirm;
- **unexecuted:** not run, with the decision that defers it.

Test ids are under `orchestrator/tests/ssds/`.

### Group 4: admission, publication, currentness, loss

| Case or discriminator | Status | Where |
|---|---|---|
| S5 §22 `publication_classification` | executed | `test_phase_f_step6d.Classification`, `.Integration` |
| S5 §23 `qualification_states`, Admission side: `ROLLBACK` | executed (441cf5c N7 cites it) | `test_phase_f_step6b.CommitPoint.test_a_rewind_is_rollback`, `.test_a_high_water_mark_beyond_the_ledger_is_rollback` |
| `qualification_states`: `UNQUALIFIED`, `FORK`, a quorum-held head | executed, uncited | `test_phase_f_step6b.CommitPoint.test_an_unwitnessed_head_is_not_qualified_and_nothing_is_appended`; `test_phase_f_step7e.Segments.test_an_unreachable_new_set_is_unqualified`; `test_phase_f_step7c.Loss.test_a_fork_takes_a_loss_naming_the_admitted_side`; `test_phase_f_step7e.Segments.test_a_held_redesignation_qualifies_under_the_new_set` |
| S5 §23 `loss_bounds`, Admission side | executed, uncited | `test_phase_f_step7c.TeamLoss.test_only_proved_never_admitted_heads_are_a_fork_resolution`; `test_phase_f_step7d.Resolution.test_a_possibly_or_known_admitted_head_is_a_loss`, `.test_a_lost_sub_quorum_entry_is_resolved_and_resubmitted_by_identity` |
| `deployment_classes_sound` at redesignation (step 7e) | executed, uncited | `test_phase_f_step7e.LocalRedesign.test_content_refusals` (an unsound set refused "not sound"), `TeamRedesign.test_a_loss_changing_the_set_is_held_by_the_reachable_old_set_too`; `test_phase_f_step7b.Trial` (`TEAM` and `HARDENED` quorums) |
| 441cf5c N7: a rewind is `ROLLBACK` | executed | `test_phase_f_step6b.CommitPoint.test_a_rewind_is_rollback` |
| 8a75346 N2, ledger form: a crash before the checkpoint | executed | `test_phase_f_step6b.CommitPoint.test_a_crash_before_the_checkpoint_is_recovered_by_request_identity` |
| 8a75346 N2, publication form: a crash after the integration-ref compare-and-swap | **unexecuted** | step 6g, deferred with SD-70's gate (SD-73); no publication exists in Phase F |
| 730490d N2, records-only form: `OVERTAKEN`, then `LATE_PUBLICATION` | executed | `test_phase_f_step6d.Classification.test_overtaken_when_a_rewrite_is_absorbed`, `.test_late_publication_is_a_critical_integrity_finding` |
| 730490d N2, fence form | **unexecuted** | step 6f (SD-73) |
| 362af9f N6: re-application of a fenced or `OVERTAKEN` integration | **unexecuted** | step 6f (SD-73) |
| 61cd09b N6: a kept fence and the D1/D2 re-gating | **unexecuted** | step 6f (SD-73) |
| faults beyond these named failure points | **unexecuted** | Phase H (plan §4) |

### Group 2: assessment disagreement, admission half

| Case or discriminator | Status | Where |
|---|---|---|
| the seven S5 §6 cases (`cases_s5_6.py`), records admitted at Admission | executed | `test_phase_f_step9d_iii.Staleness` (seven tests, one per case). The structure-override half of on⁺ ⇒ on⁻ stays derivation-side: Admission cannot change a context in place (plan, step 9d-iii) |
| 5c55d4b N6 | executed | `test_phase_f_step9d_iii.Group2Discriminators.test_a_failure_whose_only_reproductions_are_unbounded_stays_counting` |
| 798b2b4 B4: each link traversed is recorded | executed | `Group2Discriminators.test_each_link_traversed_is_recorded` |
| 29da56e N5, first case: an upheld challenge of the realization disposes | executed | `Group2Discriminators.test_an_upheld_challenge_of_the_realization_disposes` |
| 29da56e N5, the rest (counter-challenge, observation dismissal, triple dismissal, chain class, support route, adjudication recovery) | **at derivation only** | `test_assessment` (Phase D). At Admission they need further human trust roots; the plan's step 9d-iii record says so |
| 124b0b7 N2 | executed | `test_phase_f_step9d_iii.CountingFailure`, `.ProvisionalDischarge` |

### Group 3: judgment disagreement, admission half

The plan places these at step 4b-ii (row 4b-ii). The tests there do not cite the discriminators.

| Case or discriminator | Status | Where |
|---|---|---|
| 51070e5 N3: an upheld challenge needs independence and class | executed, uncited | `test_phase_f_step4b.AdjudicationEligibility` |
| f03b15e N5: supersession after the key change, by kind and target | executed, uncited | `test_phase_f_step4b.Supersession`, `.SupersessionTargets` |
| 6b986de N6: one definition of each independence input at Admission | executed, uncited | `test_phase_f_step4b.OneAuthorshipRule` |
| S1 `OWNER` cases whose distinguishing step is an Admission refusal | executed, uncited | `test_phase_f_step4b.AdjudicationEligibility`, `.RefusedAlone` |
| RR-11's resolver and Dispatcher half | executed, uncited | `test_phase_f_step4b.OneAuthorshipRule.test_nb1_judge_selection_and_classification_read_the_same_authors`, `.test_nb1_a_reviewer_dispatched_is_one_admission_would_find_independent` |

### Group 5: workflow, contracts, conformance, routing, admission half

| Case or discriminator | Status | Where |
|---|---|---|
| S5 §8 `rejected_request_salvages_never_lost` | executed, uncited | `test_admission_requests.SalvageAndQueue.test_an_authenticated_rejected_request_salvages_its_never_lost_records`; `test_phase_f_step5a.Salvage` |
| S5 §8 `unclean_result_refuses_passing_judgments` | **unexecuted** | the case needs a `TASK_RESULT` in the request. Under SD-70 such a request is `SCHEMA_UNSUPPORTED` (`test_phase_f_step6c.Accepting.test_a_task_result_or_a_runners_evidence_is_not_yet_accepted`) until A10's D4 |
| S5 §8 `clean_request_admits_all` | **unexecuted** | likewise (SD-70) |
| the refusal of a candidate bound to an obligation no longer derived | executed | `test_phase_f_step5b.RequestLevel.test_the_bound_obligation_exists_at_the_head` (`OBLIGATION_NOT_DERIVED`); `test_phase_f_step5b_iii.Decisions` |
| the five S3 kept-fence cases | **unexecuted** | step 6f (SD-73) |

### Group 1: runner half (carried by plan §4)

| Case or discriminator | Status | Where |
|---|---|---|
| 3540d98 B1, e2154ac B1, e9e6e9f B1: one representation, materialized by a designated runner | executed | `test_phase_f_step9f_i.Materialized.test_group_1_runner_half_byte_exact` |

### Authority-derived expected values

No Stage S case covers admissibility, custody or the evidence obligations. The expected values of steps 9c-ii-i to
9c-ii-iv come from the cited Manual text alone (§6, §10.2, §17), as the plan records at each step (note 6 of its
check). They are executed, but not against a Stage S expectation.

## 3. The end-to-end shadow run

- **10d on `ssdp-shadow-3`** (F126; plan revision 73): windows W1-W9, each `PASS` with the shadow boundary compared
  after the command, on the first freeze `8cf829c3`. The FINDING (position 3) and the AVAILABILITY (5) were
  accepted through `report` and `submit`. The signed ACKNOWLEDGE was refused at entry, as F1 requires. The candidate
  was refused at entry (W8). W9 read `ssdp-shadow-3` `QUALIFIED` with 6 entries. Owner:
  `PHASE-F-10D-SHADOW-3-EVIDENCE-SSDS-8.0.md`.
- **At the re-frozen candidate:** the FR-A1-repaired reader re-read all three ledgers in one boundary window (SD-98,
  attempt 2): every field equals W9's, compare 0. So 10d's closure on `8cf829c3` stands at `c8122d66` for every
  record on the ledgers. Owner: plan revision 75; `PHASE-F-FR-A1-REREAD-WINDOWS/attempt-2/`.
- **Limit:** no new command ran against `ssdp-shadow-3` at `c8122d66` itself. Its source delta from `8cf829c3` is
  the grammar repair, which the re-read shows changes no record's reading.

## 4. Differences from document control

- **11b at `c8122d66`** (F123, F124): 341 commits evaluated, 740 excluded, 942 observations: 696 in class (iii)
  and 246 in class (v), none in class (i) or (iv). Owner: the study evidence file's last section.
- **Other-family review:** the narrow re-check of `c8122d66` independently rebuilt the population, the 308
  unchanged rows and all 942 classifications, and passed them. Its RC-C1, on the classifier's fail-closed guard and
  not on any classification, is repaired (plan revision 75) and is part A of the exit Review.
- **Limits, as the survey found them:** checks (1) and (3) are conditional (a credential template whose policy
  enablement is absent; a protected touch whose agent authorship is not established), and check (4) is vacuous.
  Record-dependent effects need an authorized campaign. The consequences are the scratch ledger's. The rows share
  the harness and production owners with the program they study, so a common-mode limitation remains.

## 5. Unbuilt, deferred and disclosed

Each fails toward "not supported" (plan §6).

| Item | Owner and decision |
|---|---|
| fences, settlement, the kept-fence route, `NOT_SETTLED` (6f) | the phase that lifts SD-70's gate (SD-73) |
| the publisher's side: integration-ref compare-and-swap, merge commit, fence commits, takeover wait, ABA policy (6g) | same (SD-73) |
| the rebase (5e: a rebase frame is refused `REF_TRANSFORMATION`) and the no-collateral-regression check (5f) | same (SD-71) |
| any accepted integration; a request carrying a `TASK_RESULT` or depending on a task result's conformance (`SCHEMA_UNSUPPORTED`) | A10's D4 (SD-70, Q-F9 (a)) |
| A10's step 7 clauses and §16.11 (c)'s occasion templates | A10's D4 (SD-66) |
| template parameters on `CHECK_EXECUTION` | A10's D4 (Q-F19 (a)) |
| F47's ref restore, so §5.7's recovery under `INTEGRITY_HALT`, §23.8's "authoritative replica lost" and "abandoned entries later surface" rows | Phase H (SD-75) |
| §24.2's replacement lineage; `LINEAGE_MIGRATION` refused | Phase H (SD-76) |
| failure points beyond group 4's | Phase H |
| intake beyond SD-69's reserved-leaf `ABSORB`; `intake.neutral_auto` off | Phase G (Q-F18 (a)) |
| D-C7-OBJECTS: the C7 audit of object-typed fields (`fields`, an `execution` basis, lifecycle `controls`, genesis `fields.approval`, TASK_RESULT `slots`) | not done; done before any of them gains a new producer (F125) |
| a signed request names no ledger; no human key on two live ledgers | the request-identity owner (SD-89, Q-F29 (a)) |
| wall-clock time is unrecorded variation | disclosed (SD-87, Q-F27 (a)) |
| §6.6's reading realizable only under Q-F24 (a) | disclosed (plan, step 9e) |
| Dispatcher predictions, reservations, AUTO routes; statistical campaigns; `HARD` templates; `ENSEMBLE` | U1-U4 (SD-90, SD-99); SC-U4 open |
| live agent submissions, real-runner execution on the real ledger | an authorized campaign (G2 workplan §5.1 item 7) |
| the Phase E items plan §4 lists | as Phase E §6 states them |
| `ssdp-shadow-2` reads `INTEGRITY_HALT` at 6 under C7 | disclosed historical effect, not rewritten (F125) |

## 6. Focused re-run

The fourteen modules cited in §2, at `c8122d66`, on 2026-11-01: **325 tests OK** in 138 s, no bytecode written under
`orchestrator/src`. Command, from `orchestrator/`:

```bash
PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /tmp/claude-1000/ssds-runtime-20261030/bin/python -B -m unittest tests.ssds.test_phase_f_step6b tests.ssds.test_phase_f_step6c tests.ssds.test_phase_f_step6d tests.ssds.test_phase_f_step7b tests.ssds.test_phase_f_step7c tests.ssds.test_phase_f_step7d tests.ssds.test_phase_f_step7e tests.ssds.test_phase_f_step9d_iii tests.ssds.test_phase_f_step9f_i tests.ssds.test_phase_f_step4b tests.ssds.test_phase_f_step5a tests.ssds.test_phase_f_step5b tests.ssds.test_phase_f_step5b_iii tests.ssds.test_admission_requests
```

This confirms that the cited tests pass. It does not confirm that each one asserts the case it is mapped to; that
check belongs to the Review.

## 7. The citation shortfall

Plan §4 asks that each test cite its case by name. The rows marked "executed, uncited" do not. The behaviour is
tested at the real owner, but the trace from case to test lives in this file and the plan's step records, not in the
tests. Adding the citations, or a named assembly test, changes `orchestrator/` and so the candidate (SD-94), which
would mean a new freeze and an 11b re-run. This file does not do that. The exit Review judges whether it blocks the
exit, and the stakeholder decides.
