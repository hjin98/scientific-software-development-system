Governing SSDP version: 7.2.1.

# SSDS 8 Phase F exit evidence (step 12) at `36b0ab5f`

This file assembles Phase F's exit for the G2 workplan's Phase F row (§5.2): acceptance group 4, the admission halves
of groups 2, 3 and 5, the end-to-end shadow run, and the classified differences from document control. It assembles
evidence recorded elsewhere and names each owner. Plan revision 78 updated it after the other-family exit Review of
`c8122d66` (NO-PASS: XR-C1, XR-B1 to XR-B3), and revision 80 after the re-check of `f97251af` (NO-PASS: RR-1 to
RR-3; SD-102); both records stay as written. It accepts nothing: the independent implementation Review (plan §3,
G2 workplan §5.1 item 5) judges it, and acceptance is the stakeholder's. A case not executed is reported as
unexecuted, never as passed (Manual §31.2; plan §4).

## 1. The candidate

- **Candidate:** `36b0ab5f89a9b99c6979a81050e55fc3198a6c24` (plan revision 80; before it `f97251af`, revision 78,
  and `c8122d66`, revision 74). `orchestrator/` at the evidence commits equals it.
- **Repairs since `c8122d66`:** XR-C1, Admission's commit path (`admission/engine.py`): after an absorption the
  request is revalidated from the held head, so nothing is appended after a retirement or over a provisional entry
  and a request decided meanwhile is found, not appended twice; absorptions and lost compare-and-swaps are bounded
  separately. Tests `test_phase_f_step12.PostAbsorption`, each failing against `c8122d66`. XR-B1 to XR-B3 (revision
  78) and RR-1 to RR-3 (revision 80, SD-102) are the tests and citations of §2; revision 80 changed tests only.
- **Program suite at the candidate:** the whole orchestrator suite, 1,932 tests OK, 10 skipped, on the pinned
  runtime (rebuilt after the 2026-11-02 reboot with the recorded versions), the installed-product build reaching
  PyPI.
- **Repository acceptance:** release state, PEM, protocol snapshot, skill packages built and validated, dist
  parity, root regression (435 OK) and `git diff --check` pass.
- **Focused re-run for this file** (2026-11-02, the pinned runtime, `-B`): the modules cited in §2 below, run
  together. Result in §6.

## 2. Acceptance groups

Status words:
- **executed:** a test at the real owner asserts the case's stated outcome;
- **unexecuted:** not run, with the decision that defers it, or the reason it cannot discriminate in Phase F and
  the stakeholder question that asks for its disposition (Q-F31, plan revision 78).

Since revision 78 every executed test cites its case or discriminator by name (XR-B3).

Test ids are under `orchestrator/tests/ssds/`.

### Group 4: admission, publication, currentness, loss

| Case or discriminator | Status | Where |
|---|---|---|
| S5 §22 `publication_classification` | executed | `test_phase_f_step6d.Classification`, `.Integration` |
| S5 §23 `qualification_states`, Admission side: `ROLLBACK` | executed (441cf5c N7 cites it) | `test_phase_f_step6b.CommitPoint.test_a_rewind_is_rollback`, `.test_a_high_water_mark_beyond_the_ledger_is_rollback` |
| `qualification_states`: `UNQUALIFIED`, `FORK`, a quorum-held head | executed | `test_phase_f_step6b.CommitPoint.test_an_unwitnessed_head_is_not_qualified_and_nothing_is_appended`; `test_phase_f_step7e.Segments.test_an_unreachable_new_set_is_unqualified`; `test_phase_f_step7c.Loss.test_a_fork_takes_a_loss_naming_the_admitted_side`; `test_phase_f_step7e.Segments.test_a_held_redesignation_qualifies_under_the_new_set` |
| S5 §23 `loss_bounds`, Admission side | executed | `test_phase_f_step7c.TeamLoss.test_only_proved_never_admitted_heads_are_a_fork_resolution`; `test_phase_f_step7d.Resolution.test_a_possibly_or_known_admitted_head_is_a_loss`, `.test_a_lost_sub_quorum_entry_is_resolved_and_resubmitted_by_identity` |
| `deployment_classes_sound` at redesignation (step 7e) | executed | `test_phase_f_step7e.LocalRedesign.test_content_refusals` (a set that is not its class's tuple is refused; every declared class's tuple is sound, so the unsound (3,2,1,0) is refused that way, never at the q_a + r > N + f check), `TeamRedesign.test_a_loss_changing_the_set_is_held_by_the_reachable_old_set_too`; `test_phase_f_step7b.Trial` (`TEAM` and `HARDENED` quorums) |
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
| 29da56e N5 (B1 (a)): a revoked passing acceptance; only an independent counter-upholding restores it | executed | `test_phase_f_step12.TripleAndSupportRoute.test_counter_challenge_only_an_independent_counter_upholding_restores_a_revoked_acceptance`: `valid(code)` `T`, revoked to `F` with `ACCEPT(code)` derived, kept `F` through a refused counter-upholding, `T` again after an independent one (revision 80, review RR-2). Run for `ACCEPTANCE`, not the `REVIEW`, `CONFORMANCE`, `PLAN_ACCEPTANCE`, `EQUIVALENCE`, `COMPLETENESS` or `GATE_DECISION` siblings |
| 29da56e N5 (B1 (a)), on a realization's disposal | executed | `test_phase_f_step12.CounterChallengeAndDismissal.test_counter_challenge_only_an_independent_counter_upholding_restores_the_dispute`: an adverse dispute restored, not passing support |
| 29da56e N5 (B1 (d)): a contested resolution; only an independent dismissal ends the objection | executed | `.test_contested_resolution_only_an_independent_dismissal_ends_the_objection` |
| 29da56e N5 (B1 (b)): observation dismissal | executed | `.test_observation_dismissal_a_non_independent_dismissal_leaves_it_not_standing` |
| 29da56e N5 (B1 (c)): triple dismissal | executed | `test_phase_f_step12.TripleAndSupportRoute.test_triple_dismissal_only_an_independent_dismissal_lifts_the_block` |
| 29da56e N5 (B1 (g)): support route | executed | `.test_support_route_a_non_independent_acceptance_supports_nothing` |
| 29da56e N5 (N1): adjudication recovery, a refused adjudication answers nothing | executed | `ADJUDICATE(c)` stays derived after each refusal in the five adjudication tests above: (a) twice, (b), (c), (d); the support-route test has no adjudication |
| 29da56e N5 (B1 (e)): chain class | **unexecuted** | not discriminable at Admission in Phase F: authorship comes only from admitted integrations (none under SD-70), and unknown authorship is never disjoint from an agent's lineage, so every agent adjudication is refused for independence with the same code before the class rule acts. Owner level: `test_phase_f_step4b.AdjudicationEligibility`. Q-F31 |
| Phase D's half of these cases | disclosed | `test_assessment` carries only the counter-challenge and one dismissal of the six named cases |
| 124b0b7 N2 | executed | `test_phase_f_step9d_iii.CountingFailure`, `.ProvisionalDischarge` |

### Group 3: judgment disagreement, admission half

The plan places these at step 4b-ii (row 4b-ii); revision 78 added Admission cases in `test_phase_f_step12`.

| Case or discriminator | Status | Where |
|---|---|---|
| 51070e5 N3: an upheld challenge needs independence and class | executed | `test_phase_f_step4b.AdjudicationEligibility` |
| f03b15e N5: the assessor's and the owner's reassessments admitted and disposing; another reading `AUTH_SUPERSEDES`; an `EQUIVALENCE` of another class `AUTH_SUPERSEDES`, the same class admitted | executed | `test_phase_f_step12.AssessmentSupersession`; owner level `test_phase_f_step4b.Supersession`, `.SupersessionTargets` |
| f03b15e N5: another obligation `AUTH_SUPERSEDES` | executed | `test_phase_f_step12.TwoObligations.test_another_obligation_is_refused`: one realization claims `code` and `other`, so it serves two obligations; a `PASS` for the other is admitted alone, refused `AUTH_SUPERSEDES` naming the first's `FAIL`, which stands, and admitted on the first's own key (revision 80, review RR-1). `SupersessionTargets` varies only the reading |
| f03b15e N5: the `PLAN_ACCEPTANCE` overlap | **unexecuted** | the kind's supersession fails closed, `SCHEMA_UNSUPPORTED` whatever its items (plan review 8a41539 B2; `.test_plan_acceptance_supersession_fails_closed`). Q-F31 |
| 6b986de N6: one definition of each independence input at Admission | executed | `test_phase_f_step4b.OneAuthorshipRule` |
| S1 `OWNER`: `author_owner_failing_disposition` (admitted under the owner exception, common-mode recorded), `non_author_owner`, and `author_owner`'s shape on a subject review (refused alone; the objection waits) | executed | `test_phase_f_step12.OwnerRoutes`, through the real `authorize`, at route 4 |
| S1 `OWNER`: `policy_names_resolver`, its subject-review analogue | executed | `OwnerRoutes.test_policy_names_resolver_owner_supersession_open_author_upholding_closed`: route 2, the owner's supersession, admitted and ending the adverse review, while an attested non-owner peer's and the owner's unattested supersession are each refused `AUTH_SUPERSEDES` and leave it standing (§5.10 (e)); route 4 refused alone to the author adjudicator (revision 80, review RR-3, same-family SF-R1). Route 3, relief by the owner, and the transformation-review form (a task result, SD-70) are not run |
| S1 `OWNER`: `unknown_lineage_owner_agent` | **unexecuted** | reachable but not discriminating: with every root of unknown authorship an attested-fresh agent is refused with the same `AUTH_ACTOR`, so the lineage cannot be told apart without a known author (SD-70); owner level `test_phase_f_step4b.AdjudicationEligibility`. Q-F31 |
| RR-11's resolver and Dispatcher half | executed | `test_phase_f_step4b.OneAuthorshipRule.test_nb1_judge_selection_and_classification_read_the_same_authors`, `.test_nb1_a_reviewer_dispatched_is_one_admission_would_find_independent` |

### Group 5: workflow, contracts, conformance, routing, admission half

| Case or discriminator | Status | Where |
|---|---|---|
| S5 §8 `rejected_request_salvages_never_lost` | executed | `test_phase_f_step12.RejectedRequestSalvage`: exactly `{rep, fail, adv}` admitted; the passing judgment, refused by nothing, not admitted; the case's `tr` left out (SD-70) |
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
- **Limit:** no new command ran against `ssdp-shadow-3` at `c8122d66`, `f97251af` or `36b0ab5f`. The source delta
  from `8cf829c3` is the grammar repair, which the re-read shows changes no record's reading, and XR-C1's
  commit-path repair, which changes what Admission does only when another writer appends between an absorption and
  the revalidation; 10d's windows had one writer and no absorption between their commands. Revision 80 changed
  tests only.

## 4. Differences from document control

- **11b at `36b0ab5f`** (F123, F124; plan revision 80): window `PASS`, 353 commits evaluated, 740 excluded, 994
  observations: 720 in class (iii) and 274 in class (v), none in class (i) or (iv). The first 349 rows equal
  `f97251af`'s field for field, whose first 341 equal `c8122d66`'s; the earlier 977 observations are an unchanged
  prefix, and the 4 new rows (the first-parent commits `f97251af..36b0ab5f`) add 17. Owner: the study evidence
  file's last sections.
- **Other-family review:** the narrow re-check of `c8122d66` independently rebuilt the population, the 308
  unchanged rows and all 942 classifications, and passed them; the exit Review passed its repaired classifier (part
  A), with the limit that the classifier is no completeness oracle for the harness; the re-check of `f97251af`
  rebuilt its 35 new observations and all 977. The 17 new at `36b0ab5f` are not yet other-family checked.
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

The fifteen modules cited in §2, at `36b0ab5f`, on 2026-11-02: **346 tests OK** in 169 s, no bytecode written under
`orchestrator/src`. Command, from `orchestrator/`:

```bash
PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /tmp/claude-1000/ssds-runtime-20261030/bin/python -B -m unittest tests.ssds.test_phase_f_step6b tests.ssds.test_phase_f_step6c tests.ssds.test_phase_f_step6d tests.ssds.test_phase_f_step7b tests.ssds.test_phase_f_step7c tests.ssds.test_phase_f_step7d tests.ssds.test_phase_f_step7e tests.ssds.test_phase_f_step9d_iii tests.ssds.test_phase_f_step9f_i tests.ssds.test_phase_f_step4b tests.ssds.test_phase_f_step5a tests.ssds.test_phase_f_step5b tests.ssds.test_phase_f_step5b_iii tests.ssds.test_admission_requests tests.ssds.test_phase_f_step12
```

This confirms that the cited tests pass. It does not confirm that each one asserts the case it is mapped to; that
check belongs to the Review.

## 7. The citation shortfall: closed

The exit Review judged the trace in this file insufficient (XR-B3). Revision 78 put the case names in the tests
themselves, in the same change as the XR-C1 repair, so one re-freeze covers both.
