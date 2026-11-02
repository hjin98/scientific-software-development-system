Governing SSDP version: 7.2.1.

# Independent Phase F exit Review — c8122d66

**Overall: NO-PASS. Part A: PASS. Part B: NO-PASS. Part C: NO-PASS.**

The repaired classification and re-read checks pass their bounded review. The exit package does not establish all required Admission discriminators, and the implementation can append after a concurrent retirement or over another writer's provisional entry. Passing tests do not discharge those findings. This Review accepts neither Phase F nor G3 and authorizes no live operation.

## Identity, authority and method

- Reviewer: Codex, independent of the Claude-family implementation and same-family checks. Engagement is the stakeholder's standing other-family request and SD-101, conveyed by the pointer-only launch described in the user instruction. This is not an author-engaged approval inferred from repository prose.
- Candidate: `c8122d66edbf7d19320f7b155e0c31033566b854`; Phase E baseline: `c2b1ec27`; handoff envelope: `43d82db4c685415fc61852a847cb39b87358ce42`, on `ssds-8.0-graph-native-architecture`. The envelope's `orchestrator/` equals the candidate's. Line references below are to this review's candidate/envelope files, not a proposed repair.
- Governing owners: SSDP 7.2.1; `PROTOCOL-RELEASE-STATE.yaml` (accepted/public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`); the accepted SSDS 8 Manual; G2 workplan revision 4 accepted by SD-99; its settled register; applicable stakeholder decisions through SD-101. The Phase F plan, exit evidence and earlier reviews were assessed as claims/evidence against those owners.
- Entered `source/roles/software-implementation/SKILL.md` and its applicable shared references, including abstraction/concretization, specification/implementation, testing/validation, evidence evolution, semantic definitions, workflow/workplans and project memory. No implementation authority was inferred from the Review role.
- PEM applicability: G2's bound integrated base on `main` was `af0455753e20ee54a969c844872e29e270007211`. Accepted/base and candidate PEM blobs were both `1561797125622f355f84eb27319f87e8fa4227d9`; there was no distinct overlay. The memory check passed, schema 1, five families, zero notices. Task-local HAS: DS-001 applicable to proxy versus real-owner evidence; PC-001 applicable through the current G2 §2 item 6 owner; FF-001, SP-001 and SP-002 not applicable to this bounded exit Review. This is a partial historical search, not proof that no other history exists. Memory supplied caution and routes, not current authority.
- Parts were approached in handoff order A, B, C. The user then directed immediate recording from the accumulated evidence. No new probes or scripts were run after that direction. Only this review file was written in the repository; scratch stayed under `/tmp/ssds80-phase-f-exit-c8122d66/`. Existing unrelated untracked dotfiles/configuration were left untouched.

## A. Repair review — PASS

### RC-C1: closed within the classifier's declared observation scope

`probes_a.json` records exact equality of the newly computed observation arrays with all three committed classifications: preliminary `6ae91c3d`, **784**; frozen `8cf829c3`, **814**; re-frozen `c8122d66`, **942**. This checked complete observation arrays, not only totals.

The three RC-C1 counterexamples now stop unclassified: swapping obligation targets without changing their identities; replacing an identity by zeroes; and duplicating an identity. The additional FR-B1 mutations also stop: a discharged obligation, an unknown declaration field, a wrong quarantine value, an extra obligation field, a missing obligation, a duplicate obligation, and an unexpected integrity consequence. The guard binds each of the eight INTAKE identities to its own two-string target and requires the exact eight quarantine keys and eight obligations, with no other nonempty change.

**All repair consequences absent:** clearing every consequence list at the repair commit is accepted and yields **926**, rather than 942, observations. This is a real limitation, not a failed probe to omit. In `qualification/ssds80/PHASE-F-DIFFERENCE-STUDY-CLASSIFY.py`, `classify` invokes `repair_consequences` only when some consequence list is nonempty. Thus it rejects a partial or incorrect nonempty repair but does not require the repair's existence in an otherwise empty report.

I do **not** count that as a remaining RC-C1 blocker. F124 classifies reported differences; with every list empty, no reported consequence is assigned an incorrect class. The classifier is not an independent completeness oracle for the harness. The actual committed report contains the exact sixteen repair consequences, and their classifications were reproduced. Conversely, the accepted empty mutation must not be cited as evidence that omission of those consequences is detected. Were mandatory report completeness delegated to this classifier, this bypass would need to be closed by that owner. Part A's PASS does not make that stronger claim.

### RC-D1 and attempt 2: closed on the retained evidence

The probe extracted and evaluated the actual comparison expressions and final result predicate without running the re-read window. A successful read, completed comparison, no differences and successful boundary compare yield PASS. Interruption before comparison, interruption after comparison, a partial comparison and a failed read yield INCOMPLETE; a failed boundary compare yields FAILED. Missing versus null, an extra field, a missing ledger, an extra empty ledger and changed values all produce differences. The completion flag and interruption guard prevent the old partial-comparison PASS.

Attempt 2 has `read_exit: 0`, `compared: true`, no differences, `compare_exit: 0`, and PASS. Its ledger-name set is exactly the three required names, and the entire retained `ledgers` object equals W9's. The recorded states meet plan revision 72 step 5: `ssdp-shadow-3` QUALIFIED; `ssdp-shadow-2` INTEGRITY_HALT at 6; `ssdp-shadow` RETIRED, with unchanged record-violation readings. The probe matched the current window script, boundary sensor and W9 file to the recorded hashes. The retained command explicitly names all three ledgers and the candidate source tree; it records the PREFLIGHT-A hash `f2fecb328d47ad676f83a119887083c637330cf3489e90aa9aa8323fc582a969`.

This is verification of retained evidence, not a fresh observation of exclusive execution or a new live-ledger read. Attempt 1 remains FAILED; attempt 2 does not retroactively qualify it. Endpoint equality does not establish absence of transient writes between snapshots.

## B. Exit-package review — NO-PASS

### XR-B1 — Required reachable Admission cases are left at derivation

**Location:** `qualification/ssds80/PHASE-F-EXIT-EVIDENCE-SSDS-8.0.md:58`; `workplans/active/SSDS-8.0-G2-PHASE-F-PLAN.md:3696`. **Owner:** Phase F step 9d-iii qualification/exit-evidence owner, under the G2 acceptance-group owner.

The exit marks the remaining `29da56e N5` cases “at derivation only,” explaining that Admission needs further human trust roots. Plan §4, lines 421 and 426, requires the stated outcomes at the real owner and gives group 2's Admission half no deferral. The original discriminator at `MANUAL-REVIEW-SSDS-8.0-29DA56E-NO-PASS.md:179` names counter-challenge, observation dismissal, triple dismissal, chain class, support route and adjudication recovery. A fixture needing another human is not an unreachable operation or a stakeholder deferral.

Concrete sequence in `probes_bc.json`:

1. Through the real owners in a scratch ledger, admit a realization and a failing assessment, then a challenge of that realization, its UPHELD adjudication and the required non-authorship attestation. The failing assessment's disposition is 2.
2. Generate a second throwaway human key and register it through the real lifecycle path.
3. Submit that human's signed counter-challenge of the upholding adjudication. Admission returns ACCEPT at position 9, with no refused record.
4. Submit the signed UPHELD adjudication of the counter-challenge and its non-authorship attestation. Admission returns ACCEPT at position 10, with no refusal. Disposition becomes 0.

This falsifies the claimed practical reason for leaving at least the counter-challenge at derivation. It does not qualify all the remaining cases. The owner must supply the missing Admission cases and their authority-derived expectations, or obtain an explicit scope change from the actual acceptance owner. The step record's own explanation cannot waive §4.

### XR-B2 — Several “executed” mappings prove less than their named case

**Locations:** exit evidence lines 68, 70 and 77; `orchestrator/tests/ssds/test_phase_f_step4b.py:859-882`; `orchestrator/tests/ssds/test_admission_requests.py:354-360`; `orchestrator/tests/ssds/test_phase_f_step5a.py:98-135`. **Owner:** Phase F acceptance-evidence/test owner, with authorization and salvage owners supplying the real discriminating paths.

Three concrete mismatches prevent accepting the matrix as a complete case-to-assertion trace:

1. **S1 OWNER refusal:** the exit cites `AdjudicationEligibility` and `RefusedAlone`. The former supplies useful direct checks of the production eligibility/authorization owner on constructed histories. The latter submits two FINDING records and replaces `ssds.admission.engine.authorize` with a fake that returns `AUTH_ACTOR` for one. The test then checks generic refusal-alone propagation. An implementation that mishandles an actual owner-authored objection could still pass that test, because the distinguishing authorization decision was injected. The S1 OWNER cases at `qualification/ssds80/models/cases.py:118-146` distinguish author-owner, nonauthor, resolver, unknown lineage and reassessment situations; these cannot all be discharged by that generic two-FINDING carrier. This is a coverage finding, not a claim that the production owner necessarily implements those cases wrongly.
2. **Supersession:** the exit maps the whole `f03b15e N5` discriminator to `Supersession` and `SupersessionTargets`. The original review at `MANUAL-REVIEW-SSDS-8.0-F03B15E-NO-PASS.md:191` specifically requires assessment supersession after the judgment-key change, PLAN_ACCEPTANCE overlap and EQUIVALENCE class supersession. The inspected classes cover particular assessment/gate targets and refusal of unsupported PLAN_ACCEPTANCE, but do not establish that entire sequence of required expectations, including EQUIVALENCE class supersession. A conservative unsupported-kind refusal is not execution of the positive overlap case. “Key change” here is the judgment-key design change, not a claim about cryptographic key rotation.
3. **Rejected-request salvage:** the Stage S expectation contains report, failing assessment and adverse judgment (`rep`, `fail`, `adv`). The cited `SalvageAndQueue` test rejects a carrier containing a good FINDING and a secret-bearing FINDING, then asserts only the good FINDING survives. `Salvage.test_salvageable_kinds` checks a predicate; its adverse-judgment engine test asserts an ACCEPT carrier. Together those assertions do not execute the stated mixed never-lost set through a rejected carrier. A defect specific to retaining the failing/adverse records on rejection can escape those assertions. This does not assert absence of every related test elsewhere; the cited evidence does not close the named case.

Fix the mapping at the case/outcome level. Where equivalent production evidence already exists, name its exact assertions and circumstances. Otherwise add the missing discriminators through the actual owner. Do not replace these gaps with another passing aggregate count or a test of the expected-value helper.

### XR-B3 — The mandatory in-test citation condition remains unmet

**Location:** `workplans/active/SSDS-8.0-G2-PHASE-F-PLAN.md:421`; exit evidence §7, beginning at line 156. **Owner:** Phase F qualification-plan/exit owner; a change to the accepted requirement belongs to its stakeholder acceptance owner.

The plan requires literal expected outcomes with the case name cited in the test. The exit explicitly acknowledges that multiple tests lack those citations and asks whether its external trace suffices. My judgment is that the external trace is useful review evidence but does not, by itself, satisfy that mandatory placement condition. XR-B2 also shows that it is not yet a complete semantic substitute.

Sequence: select an “executed, uncited” row; follow its mapped test; find no named case binding there; rely instead on the author's exit mapping. That fails the plan's stated reproducible trace requirement. The cost of changing the immutable candidate and rerunning its required checks does not waive the requirement. This is a bounded qualification-conformance blocker, lower consequence than XR-C1. Close it by satisfying the condition or by an explicit acceptance-owner disposition of the proposed substitution; this Review supplies no waiver.

### Disposition of the rest of the matrix

The following records the extent of the case audit. “Supported” means the inspected assertions support the bounded row, not that the whole implementation owner was read or proved correct.

| Exit row(s) | Review disposition |
|---|---|
| Group 4 S5 publication classification; 730490d N2 records-only OVERTAKEN/LATE_PUBLICATION | Supported by the cited classification and integration assertions. The fence form remains distinct. |
| Group 4 ROLLBACK, including repeated 441cf5c N7 row | Supported: rewind and high-water-beyond-chain assertions exercise qualification/Admission. |
| Group 4 UNQUALIFIED, FORK and quorum-held head | Supported by the named commit, loss and segment cases; not a complete concurrency qualification, as XR-C1 demonstrates. |
| Group 4 loss_bounds | Supported for the named never-admitted versus possibly/known-admitted cases and identity resubmission. |
| Group 4 deployment_classes_sound at redesignation | Supported for the named unsound-set refusal, reachable-old-set condition and TEAM/HARDENED trial quorums. Fixture witness reachability is not a physical deployment claim. |
| Group 4 8a75346 N2 ledger crash before checkpoint | Supported for the cited single crash/retry identity sequence. It does not cover the post-absorption interleaving in XR-C1. |
| Group 4 publication crash, fence form of 730490d N2, 362af9f N6 reapplication, 61cd09b N6 kept fence/re-gating | Validly unexecuted under SD-70/SD-73; no accepted integration/publisher/fence in Phase F. |
| Group 4 other failure points | Validly reported unexecuted for Phase H; this does not excuse defects in the built commit path. |
| Group 2 seven S5 §6 histories | Admission tests cover their stated histories; the context/structure-override portion is expressly partial and remains derivation-side. Do not read “seven” as every possible context mutation through Admission. |
| Group 2 5c55d4b N6, 798b2b4 B4, first 29da56e N5 case, 124b0b7 N2 | Supported by the named bounded-reproduction, recorded-link, challenge, counting and provisional-discharge assertions. |
| Group 2 remaining 29da56e N5 cases | XR-B1; not an authorized deferral. |
| Group 3 51070e5 N3 | Useful production eligibility and chain-class assertions on constructed histories; not a blanket end-to-end OWNER-case result. |
| Group 3 f03b15e N5 and S1 OWNER | XR-B2. |
| Group 3 6b986de N6 | `OneAuthorshipRule` checks shared authorship inputs for specific review/transformation situations and unknown authors. I did not establish every record-kind input required by the broad discriminator; no all-kinds PASS. |
| Group 3 RR-11 resolver/Dispatcher half | The cited tests compare eligible judges with the same authorship reading. This is bounded selection evidence, not execution of the entire Dispatcher transport/issue path. |
| Group 5 rejected-request salvage | XR-B2. |
| Group 5 unclean result and clean request | Correctly unexecuted at the stated outcomes under SD-70: those cases carry TASK_RESULT, which remains unsupported pending A10 D4. |
| Group 5 no-longer-derived obligation | The cited tests establish the request-level OBLIGATION_NOT_DERIVED check and decision behavior. They do not demonstrate a successful integration carrying a candidate; that remains gated. Treat the helper/decision scope explicitly. |
| Group 5 five S3 kept-fence cases | Validly unexecuted under SD-73. |
| Group 1 designated runner/materialized representation | The named byte-exact materialization test supplies bounded runner-half evidence. It is not a review of all runner confinement code. |

Expected values in the inspected tests were literal assertions or authority-derived states, rather than outputs obtained by running the Stage S models. I did not execute anything under `qualification/ssds80/models/`. This is not a corpus-wide proof of the provenance of every expectation. The steps 9c-ii-i through 9c-ii-iv Manual-derived obligations are not falsely relabeled Stage S cases, but their full expected-value audit was not completed here.

### Exit disclosures, 10d and 11b

The checked §5 disclosures carry the material deferrals: F47/ref restoration and the three recovery consequences, replacement lineage, publisher/fences/settlement, rebase and no-collateral-regression, SD-70/A10, CHECK_EXECUTION parameters, Phase G intake/neutral-auto, D-C7-OBJECTS, cross-ledger request identity, wall-clock variation, Q-F24, U1-U4/SC-U4, live campaign limits, inherited Phase E limits and `ssdp-shadow-2`'s C7 halt. No additional missing mandatory exit disclosure was established in the completed reading. This is not an exhaustive reconciliation of every historical plan sentence. XR-B1 is a disclosed omission whose proposed reason does not authorize it.

Sections 3 and 4 are supportable **with their routed evidence limits**:

- 10d ran on `8cf829c3`, not anew on `c8122d66`. The re-read establishes equal readings of the retained ledger records after the grammar repair; it does not repeat signed appends with the repaired candidate. The closing FINDING/AVAILABILITY appends, signed decide refusal and candidate refusal remain the recorded bounded run, not an accepted integration or real-runner campaign.
- The 10d evidence owner discloses loss of the rehearsal and real W1-W5a raw logs in the reboot. Its contemporaneous narrative and later retained read-back survive. The original full dependency set was not pinned, although the rebuilt Python and Typer versions were recorded. I did not reconstruct those lost logs or independently witness their boundary windows. The short exit summary must be consumed with this routed limit.
- Attempt 1's failed boundary, the earlier contaminated `ssdp-shadow-2` append boundary and its integrity halt remain historical facts; neither the later successful windows nor this Review retroactively qualifies them.
- The re-frozen 11b record reports 341 evaluated commits, 740 excluded and 942 observations, 696 class (iii) and 246 class (v). This round reproduced all classification observations. The earlier narrow re-check's population reconstruction and comparison of the 308 unchanged rows remain inherited evidence; this round did not rerun the harness or independently reconstruct that whole population again.
- Credential enablement and protected-touch agent authorship remain conditional, check (4) vacuous, and the consequences belong to a scratch ledger. Shared harness/production owners leave common-mode error possible. Neither the absence of class (i)/(iv) nor the classifier's successful execution proves absence of runtime defects; XR-C1 is outside that bounded historical survey.

## C. Implementation review — NO-PASS

### XR-C1 — Post-absorption reload bypasses the held-head gate

**Location:** `orchestrator/src/ssds/admission/engine.py:428-434`, especially `chain = self.chain()` at line 430; append at lines 477-490 and `commit` lines 384-398. The existing gate is `held_head`, lines 330-350. **Owner:** Admission's commit/currentness owner, with ledger qualification/retirement as the semantic dependency; D4 implementation repair under Manual §§8.3, 21.3, 22.4, 23.4 and 24.2.

The initial head is qualified, but after absorbing a moved observed branch, `_admit_once` reloads the chain without qualifying that newly loaded head. A second writer can change the chain between the completed absorption and that reload. Admission then validates against the new suffix and uses its head in the append compare-and-swap. The CAS therefore succeeds; it does not force the held-head retry that would have occurred had the writer retained the earlier expected head.

**Sequence 1: retirement.**

1. Writer A starts a permitted records-only request at a held head and absorbs the moved product branch.
2. Before A's post-absorption reload, writer B admits a correctly signed LINEAGE_RETIREMENT and publishes its retirement statement to the scratch witnesses.
3. A reloads the retired chain via `chain()`, validates and calls `commit` against its newest entry. The probe observes RETIRED before A commits.
4. A appends an ADMISSION after retirement. Its later qualification check raises `AdmissionHalted`, but that is after the append.

In `probes_bc.json`, B retires at position 3; the chain grows from four entries to five; the extra position 4 carries an ACCEPT admission with no refused record. The subsequent halt does not undo that ledger write. Manual §24.2 makes retirement the last entry; raising an error after appending violates that rule.

**Sequence 2: another writer's provisional entry.**

1. A again completes its absorption.
2. B appends a valid records-only request, then its checkpoint write fails. B halts, leaving position 3 provisional and the held head at 2.
3. A reloads the full chain, validates with the provisional suffix present and appends position 4 without first completing B's checkpoint distribution.
4. A returns ACCEPT. Immediately before that commit, the recorded qualification still has `provisional: 3`.

Manual §22.4 requires completing the provisional entry's commit point before appending the next ordinary entry; §§8.3/23.4 require the held-head basis. A later checkpoint at the new head does not make the required earlier sequencing true retroactively.

**Independent composition confirmation and causal control:** `commit_interleaving.json` repeats both interleavings using `test_phase_f_step10b.Served` and actual `Composition.admission()` instances, so F1 is installed through the production composition. Here B's position is 4. The retired chain grows from five entries to six before A halts; the provisional branch reaches A's commit with held head 3 and provisional 4 and appends position 5. These composition probes used a FINDING shape rejected as `SCHEMA_RECORD`; the provisional branch returns REJECT. That does not weaken the append counterexample: recording a rejection is still a ledger append. The earlier `probes_bc.json` supplies the valid-record ACCEPT variant. These distinct results must not be conflated.

For the control only, a scratch-compiled copy of `_admit_once` replaced its single post-absorption `chain()` call with `held_head()`; no repository source changed. Retirement then left five entries, with no later admission. The provisional control reached A's commit only after head 4 was held and provisional was null. This isolates the missing gate. It is evidence for repair direction, not qualification of a complete patch or of every concurrent lifecycle race.

Both probes use real scratch ledger/signature/qualification owners. The test hook schedules the second writer deterministically; the provisional variant injects a checkpoint-write `OSError`. Neither substitutes the qualification result or append decision. No live ledger was touched. The demonstrated breach is of allowed ledger sequencing, not evidence that an integration was published or a product file was changed outside SD-59.

### Other implementation conclusions and Serious Challenge

The inspected entry-policy and composition paths route candidate and unsupported-record refusals before normal Admission. Observe-only composition has no publisher. The focused tests corroborate its bounded refusal/no-append behavior in the covered scenarios. Those observations do not overcome XR-C1 and are not a universal proof against all writes outside SD-59; filesystem primitives and all caller paths were not exhaustively audited.

**No new SERIOUS CHALLENGE is established.** XR-C1 contradicts a coherent existing commit/retirement rule and belongs to its implementation owner. XR-B1/B2/B3 concern qualification and compliance with the accepted exit requirements. Existing **SC-U4** remains open at its routed upstream scientific/numerical owner under G2 U4/SD-90/SD-99; this Review neither resolves it nor permits HARD qualification or statistical campaigns.

## Executed evidence and limits

All evidence below predates the user's final instruction to stop probing and write. Scratch paths are reproducibility aids, not durable repository authority.

| Artifact under `/tmp/ssds80-phase-f-exit-c8122d66/` | What it establishes |
|---|---|
| `probes_a.py`, `probes_a.json` | Exact classification-array reproduction, RC-C1/FR-B1 mutations including the accepted empty repair, extracted RC-D1 predicates/comparison, retained attempt-2 equality and three tool/file hashes. No window or sensor execution. |
| `probes_bc.py`, `probes_bc.json` | Reachable signed counter-challenge with a second scratch human; valid-record ACCEPT versions of the two commit interleavings. |
| `commit_interleaving.py`, `commit_interleaving.json` | Production-composition confirmation and the one-call scratch control; schema-refused carriers as expressly described above. |
| `focused-retry.log` | **357 tests, OK, 159.977 s**, no skipped tests reported. |
| `focused.log` | Earlier interrupted test attempt; no completion result, therefore not a pass. |

The completed test run used the pinned `/tmp/claude-1000/ssds-runtime-20261030/bin/python`, `-B`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH=src`, and scratch `TMPDIR`/SSDS home placement. Modules: `test_phase_f_step6b`, `6c`, `6d`, `7b`, `7c`, `7d`, `7e`, `9d_iii`, `9f_i`, `4b`, `5a`, `5b`, `5b_iii`, `test_admission_requests`, `test_phase_f_step10b`, `test_phase_f_step10c`, all under `tests.ssds`. These tests are narrower than the complete 1,911-test candidate suite reported by the author. I did not rerun that full suite, installed-product/PyPI tests, package build/parity or root acceptance during this exit Review.

## Source read, and what was not checked

This inventory distinguishes reading from execution/import. A test importing a function does not count as reading or independently reviewing it. Reading a caller does not qualify its unread callee. Part C stopped with a demonstrated priority-1 defect and partial priority-2 reading; lower-priority recovery, Dispatcher and derivation owners remain expressly unpassed.

| Owner | Functions/source read | Not read or not completely reviewed |
|---|---|---|
| `admission/engine.py` | Lines 1-813: policy, salvage/decision helpers; `Admission.__post_init__`, `submit`, `_entry`, `order`, `process`, `chain`, `expected_head`, `absorb`, `recorded`, `witness_set`, `qualification`, `loss_evidence`, `prepare_loss`, `_extended`, `trial_qualification`, `old_set_holds`, `prepare_redesignation`, `host_keys`, `held_head`, `publish_retirement`, `distribute`, `commit`, `admit`, `_admit_once`, `lifecycle_message`, `admission_entry`, `trial`, `admit_lifecycle`, `validate`. Also `adoptable`, `_shape`, `gated` at 986-1051. | `cascade`, `_fixed_transformations`, `authorized`, `_absorbs`, `_writable`, `admissible`, `_content_problems`, `attestation_references`, `_retiring`, `target_type` (814-985); `submitted_with` not fully read; `integration_frame`, `_waits`, `conformance_codes`, `review_codes`, `integration_codes`. In particular, no full helper-level review of validation/salvage or recovery follows from reading `validate`/`admit_lifecycle`. |
| `admission/request.py` | Whole 175-line module: request identity/message, binding/never-lost and expected-head helpers, boundary/observe-only wrappers. | No exhaustive transport/cross-ledger replay audit; the SD-89 restriction remains. |
| `cli.py` | `HomeAccess` methods; all `Composition` methods from constructor through `observe`; `request_command` and its `run` closure; `admission_serve`. | `command_takes`, `_human_record`, `canonical_signature`, `read_prepared`, `_summary`; `connect`, `command_name`, `compose`, `dispatcher_serve`, `mcp_serve`, `main` and surrounding registration glue were not fully read. Thus report/submit/decide composition was read, but not every input-loading/command helper. |
| `ledger/qualification.py` | Lines 1-180, 185-270, 329-725: quorum/model checks, checkpoint representation/authentication, FileWitness reading, retirement authentication/verification/holding, HighWaterStore, `write_all`, `qualify` including its local `assess`, segment/witness selection, `qualify_segments`, `host_keys`, `currentness`, `loss_status`, Home path checks and `_mode`, `_listing`, `_is_repository`. | The end of `RetirementStatement.from_json`/`to_json` at 181-184, `publish_private`, `Qualification.current`, `_abandoned` and intervening definitions at 271-328 were not read. No complete atomic-file/publication or physical witness-medium audit. |
| `admission/authenticate.py` | Main `authenticate`, retained/resubmission and attestation storage helpers, `_content`, `_verify`, `_encodable`, `_attests`, `_runner`, `_human`; most of module read. | The `_envelope`/`_attested`/`lineage_closure` region was not completely read because the displayed source was truncated. No claim of complete authentication/lineage-closure audit. |
| `admission/authorize.py` | `_cosigners`, `_cited`, `_adjudication_eligible`; beginning of `_record_codes`, around lines 94-132. | `authorize` body was not fully read; remainder of `_record_codes`, `_reading_codes`, `_immateriality_actor`, `_custody_actor`, `_availability_actor`, `_supersession_unbuilt`, `_in_frame`, `_acceptance_target`, `_supersession_authorized` unread. Tests invoking them do not close that limit. |
| `admission/lifecycle.py` | `lifecycle_message`, `key_identity`, beginning of `lifecycle_problems` through about line 100. | Remainder of `lifecycle_problems`; `retirement_problems`, `replica_problems`, `migration_problems`, `redaction_problems`. |
| Remaining Admission validation owners | Some behavior exercised by the focused tests and read through `validate`. | **All functions** in `admission/checks.py`, `legality.py`, `dependency.py`, `evidence.py` were not source-reviewed in this round. |
| Recovery owner | Engine recovery call sites/trial and lifecycle flow as above; focused loss/redesignation tests. | **All functions** in `admission/loss.py`, plus the unread recovery gate/content helpers named above. No full recovery-source verdict. |
| Dispatcher | Composition call sites and selected test assertions only. | **All functions and methods** in `dispatcher/issue.py`, `journal.py`, `home.py`, `schedule.py`, `runner.py`, `realize.py`. No full envelope/journal, scheduling or sandbox-confinement review. |
| Derivation Phase F additions | Test assertions and engine dependency routes only. | **All functions and methods** in `derivation/publication.py`, `assessment.py`, `judgment.py`, `realization.py`, `evidence.py`, `structural.py`, `workflow.py` were not source-reviewed as implementation owners here. |

Additional limits: the entire 162-file Phase F delta was not read; validation reason-code closure was not exhaustively rederived; no model/campaign was launched; no live SSDS home, SSH keys, re-read/11b window, sensor or repository difference harness was accessed or run. The classifier and isolated AST probes do not substitute for the harness. The interleavings are deterministic counterexamples, not a concurrent stress campaign. Read-only Git/source/evidence inspection and temporary-key scratch fixtures supply the findings above.

The requested outcome is this decision record. XR-C1 requires a commit-path repair and discriminating regression evidence; XR-B1/B2 require truthful case-level closure; XR-B3 requires the prescribed trace or an explicit owner disposition. Any changed semantic candidate must follow its governing freeze/review obligations. Acceptance remains the stakeholder's decision.
