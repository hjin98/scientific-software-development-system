Governing SSDP version: 7.2.1.

# Independent frozen-candidate Review — SSDS 8 Phase F, `8cf829c3`

**Existing SERIOUS CHALLENGE SC-U4 remains open.** Its owner is the Manual's §14.7/§0.6 `HARD`-template qualification contract, resolved through U4's D1/D2 acceptance and the Manual/ruleset acceptance route. SD-91 accepted the challenge and its routing, not its resolution. It blocks template qualification/adoption and G3 criterion 10, not the independent Phase F work reviewed here. This Review raises no additional Serious Challenge: the two blockers below violate coherent requirements at their implementation/evidence owners.

**Overall verdict: NO-PASS.**

| Part | Verdict | Decision |
|---|---|---|
| A — frozen source delta | **NO-PASS** | FR-A1: the new nonce grammar accepts a trailing newline through both authenticated Admission and chain reading. |
| B — frozen 11b run and F124 classification | **NO-PASS** | The recorded population and all 814 classifications check out. FR-B1 blocks the separately required fail-closed classifier claim: unexpected consequence semantics can receive class (iii). |
| C — G2 revision 4 | **PASS** | U1-U4, SC-U4's route and the interim restrictions preserve the governing decisions within the reviewed scope. This is technical Review, not acceptance of revision 4 or resolution of SC-U4. |

This record accepts nothing. Acceptance of 11b, revision 4 and Phase F exit/step 12 remains the stakeholder's. It supplies no new D4 authorization, campaign authorization, native authority, cutover or release approval. In particular, it does not close the live 10d run.

## Identity, engagement and authority

- Review date: 2026-11-01. Reviewer: independent Codex/OpenAI-family context; no authorship of this candidate. The engagement is the stakeholder's standing request for one other-family review per frozen candidate, launched through Codex CLI in the stakeholder's terminal. The author's session typed only the pointer prompt. Author evidence and same-family conclusions were treated as hypotheses, not inherited verdicts. No subagents were used.
- Repository: local `scientific-software-development-system`, branch `ssds-8.0-graph-native-architecture`. HEAD at intake was the envelope `26f34516db2f343f8838d82af128aac547d339d7`.
- Instruction: `qualification/ssds80/PHASE-F-FROZEN-REVIEW-HANDOFF-SSDS-8.0-8CF829C3.md` at that envelope; blob `73dfe4072a0ccf9950468357bb02c268a9cbc655`.
- Frozen candidate: `8cf829c34020ebffb5ad50ad7ba5b03343c005ce`; tree `bf2d384ce85fb9f298ee185dd96f44378d506491`. The checked-out `orchestrator/` equals this candidate. The envelope changes neither that tree nor the candidate's G2 workplan.
- A baseline: `1abf37cf9e0ef6de445aefce27d386cb3d2a003d`. Independently confirmed delta: 16 files, +851/-67.
- C baseline: `7adf5e5ad2443b47e1afef2a27ab53ad6c672b7c`, compared with the frozen candidate's G2 workplan revision 4.
- Accepted Manual: `orchestrator/docs/ssds-8.0-architecture.md`, verified candidate blob `438cb113b155c2e79715430338a543615fa7f143`, with accepted A1-A10. The settled G2 register and stakeholder decision items 77-81 were read, including SD-90 through SD-97 and the Scheduler note that SD-90 maps onto the current architecture.
- Governing public protocol source, resolved from `PROTOCOL-RELEASE-STATE.yaml`: `aaeaf8b6b2121b9fb8aba31917c8265649c43954`. Entered its software-implementation and software-design roles and applicable shared owners: abstraction/concretization, D4 specification, architecture, workflow, evidence, testing, definitions, PEM, security, performance, storage and Python engineering. No newer protocol was substituted.
- Phase F readings F120-F126, the 10d/11 rows, interim upstream restrictions and revision records 64-71 were read at the envelope. The handoff's distinction between frozen semantic source and later evidence/envelope records was retained.

## Blockers

### FR-A1 — nonce validation accepts bytes outside F125's closed grammar

**Location:** `orchestrator/src/ssds/ledger/schema.py:317-318` (with `NONCE_RE` at line 30). **Owner:** D4 ledger schema, shared by Admission step 1 and authenticated ledger reading; parent requirements are F125 and Manual §3.2/§5.7.

`NONCE_RE` is `^[0-9a-f]{32}$`, but the two members call `match`, not whole-string matching. A terminal LF is accepted before `$`. Thus `{"run": "a1" repeated 16 times, followed by LF}` is a 33-character value outside the required 32-hex nonce grammar, yet `record_violations` returns no violation. The same is true for `report`.

**Concrete execution:** in a new fixture home, issue an authenticated task, bind a FINDING carrying that provenance, sign the request with its fixture task credential, and call the real `Admission.admit`. Both malformed `run` and `report` records appear in `decision.admitted`. A separately authenticated fixture chain containing the malformed `run` record also passes `verify_chain` without a halt. Expected behavior is `SCHEMA_RECORD` on submission and `INTEGRITY_HALT` on authenticated historical reading. Neither occurs.

This is a bounded grammar defect, not demonstrated arbitrary narrative injection, a credential leak, or a change to derived workflow authority. It nevertheless falsifies the exact closed-grammar and shared-enforcement requirements being qualified. The authentic producers normally generate valid nonces; their happy paths do not exercise this rejection boundary.

**Repair/closure route:** enforce whole-value matching at the schema owner and add the terminal-LF discriminator at both consumers. Review the same endpoint issue in the token/digest/actor predicates reused by provenance, rather than applying a nonce-only exception that leaves the same grammar boundary inconsistent. Re-run affected schema/admission/reading regression and bind subsequent qualification to the repaired immutable source; no repair was made by this reviewer.

**Evidence:** `/tmp/ssds80-phase-f-frozen-review-8cf829c3/provenance_probe.py`, `provenance-probe.log`. The final two probes reproduced authenticated admission and reading acceptance. The first scratch attempt had a reviewer-fixture `AttributeError` from using the wrong fixture base; that probe error was corrected before the final run and is not a product failure.

### FR-B1 — class-(iii) consequence rule accepts unexpected discharge and identity semantics

**Location:** `qualification/ssds80/PHASE-F-DIFFERENCE-STUDY-CLASSIFY.py:75-90`, especially lines 76-78 and 85-86. **Owner:** the F124 classification instrument/evidence owner, under the Phase F 11b workplan. The relevant production meaning is Manual §18.2-§18.5: absorption quarantines structural deltas and derives intake obligations; it does not supply their human disposition.

The intake rule checks `kind`, `detail` and only the first element of `about`. It does not check discharge state, the declaration field, or identity consistency. The quarantine rule checks only the first element of the decoded key and ignores its value. Those are material omissions from the assertion that any unexpected observation stops unclassified.

**Concrete counterexample:** copy the committed report in memory, change only the first added intake obligation at `11ec88e4` from `discharge: OPEN` to `discharge: DISCHARGED`, and run the actual classifier. It still emits 814 classified observations, 630 (iii) and 184 (v), with the changed obligation labelled `reserved_leaf_repair_absorbed_as_foreign_change`. An unexpectedly discharged obligation in this no-adoption replay is a potential SSDS defect requiring investigation, not an established harmless genesis deviation.

Two further discriminators survive: replace a quarantine key's declaration-field component with `unknown`, or keep its key and change its value to `["unrelated.unit", "kind"]`. Both are still classed (iii). An unknown check-2 code, by contrast, correctly stops unclassified. Hashing each observation preserves the changed bytes' identity; it does not validate their meaning. Supplying the hash of a newly generated report would not cure this rule defect.

**Effect on the actual frozen evidence:** none of those mutations occurs in the committed report. Independently checking the complete identities, field set, values and `OPEN` status of all eight obligations and eight quarantine changes confirms that the actual 16 changes warrant class (iii). FR-B1 blocks B's explicit fail-closed requirement, not the numerical inventory or a fabricated claim that the observed run already contained an unearned discharge.

**Repair/closure route:** constrain the reason to the complete material shape of the known reserved-leaf declaration changes and their open obligations, with identity/value consistency and complete coverage; leave other outcomes unclassified for review. Preserve the actual observation identities and recheck both preliminary and frozen reports plus the three negative cases. This is an evidence-instrument repair, distinguishable from semantic-source mutation; FR-A1 independently requires source repair.

**Evidence:** `/tmp/ssds80-phase-f-frozen-review-8cf829c3/audit.py`, `audit.json`. No mutated report was written into the repository.

## A — remaining source findings

The provenance table is one owner: Admission uses its `record_violations`, and authenticated chain verification uses the same check. Empty objects and free keys are refused; `attempt` excludes booleans and negative/out-of-range integers; `judge` fixes its four members and lineage vocabulary; `reissue_of` uses the record-digest predicate. The approval member is restricted to lifecycle records, a human actor and whole-string SSH armour, including its line bound. Lifecycle admission verifies the human signature and validates the stamped record before appending. I found no legal, contract-conforming producer shape rejected by the table. The producer, secret-scanner, approval-cap/actor/tier/trailer and historical narrative-halt tests passed. FR-A1 qualifies the positive conclusion about exact grammar enforcement.

**D-C7-OBJECTS is a bounded deferral, not full C7 conformance.** F125 explicitly leaves other object-typed fields with their kind readers, requires the audit before any new producer of those fields, and requires disclosure at Phase F exit if unfinished. The delta adds no such producer. Keeping this as a residual is consistent with the bounded provenance repair; neither this Review nor the passing tests establish that every record surface already satisfies C7. This remains non-blocking for the handoff's source delta and must remain visible at exit.

**Cost repairs:** the import cache keys on path and content SHA-256, retains immutable facts including incompleteness markers, and evicts by its declared accounted-size budget. Fresh-versus-cached, changed-content, relative-path and eviction tests passed. The batch reader retains first-parent order, stored bytes, blob peeling and rejection of missing/wrong-type/corrupt objects; its explicit stack avoids Python recursion depth. Differential tests against the old per-object reader passed in SHA-1 and SHA-256 repositories, including malformed entries and 1,101-level nesting. No result-changing cost-repair counterexample survived the inspected cases. This is bounded equivalence evidence, not exhaustive proof over every corrupt Git object, an RSS bound, or a new performance measurement.

**Missing blobs and small fixes:** the content reader translates missing/ambiguous or malformed batch responses into `GitReadError`, preserving valid blob bytes. The real missing-blob fixture passed; source inspection covers header/type/size/truncation branches. The study catches that error as a refusal. Protected-touch wording now accurately distinguishes a unit containing a protected surface from an exact protected path. The prepared-input refactor reuses the same public request/signature loader and canonicalization; its fixture confirms unchanged public file bytes/modes and successful signed admission.

**Test reconciliation:** identity-distinguishing prose becomes a legal numeric attempt; secret tests still exercise legal token fields and stored objects; the signature-key scanner test retains its negative purpose. The bound-only TASK_RESULT-slots case is explicitly separated from the token case that owes both `SCHEMA_BOUND` and `SCHEMA_RECORD`. The review-brief test still excludes the author's marker, narrative-reference digest and outcome while retaining the author's claims as claims to test. I found no weakened original assertion that explains away a product failure. The missed terminal-LF rejection is an omitted discriminator, not a test that was deliberately relaxed.

## B — independent reconstruction of the frozen study

The committed window records harness exit 0, compare exit 0, no bytecode under source, the frozen candidate and a new scratch home. The wrapper establishes source/cleanliness/worktree preconditions, explicitly sets scratch `SSDS_HOME`, runs the harness under `-I -B`, and performs the outer comparison. The harness itself rejects reused/unsafe homes, creates its own throwaway genesis, checks the held parent before each absorption, and records the final boundary independently. I inspected those paths but did not rerun either harness or boundary sensor on the real repository.

Verified SHA-256 bindings:

| Artifact | SHA-256 |
|---|---|
| frozen report | `8ec603a8a2005377088006f500f2ee76f27ee820a7b942964e11d8c9f73a2ee1` |
| frozen classification | `aea9f477f965530886f79f1a0d99ee7bc3c8876ae1d1e4288c0717440bf9d901` |
| reviewed classifier at envelope | `911cd3750787204283f4d9f4e494b566b963379b682a1ca0eac57583f2d0f2ef` |
| frozen harness | `cb7c8d03936529b7395c25508880999b3effb306a371bf634fb190d315dc54d7` |
| window wrapper | `14a5c116906fa3aef3b8d715b01acb2a097f945a035bcf2cc937` |
| boundary sensor | `79770bc29f27fe1ba773b7c98270b32c7e82f23cd04b334ae00222a33a757722` |

The window's three tool digests match the committed files; the classification binds the actual report digest. The report is `COMPLETE`, `FINISHED`, `pending: null`, expected/evaluated 308, with its own boundary `PASSED`, unchanged true and no differences. These are verified committed evidence records, not a claim that this reviewer witnessed the historical host window or independently proved the absence of all historical accesses.

**Population:** independently reconstructed from Git's first-parent chain: **1,049 = 740 exclusions + 1 initialization + 308 evaluated deltas**. All excluded identities and all row-parent pairs agree. The exclusions are 690 commits without a manifest and 50 beginning at `db0e9f42` whose structure lacks `ssds.unclassified`. For every manifest-bearing excluded commit and `G`, I called the real `baseline_structure` and removed only the two permitted reserved-leaf errors from its result. The retained exclusion reasons agree exactly; the first passing initialization is `09f35057aec00467372aa8fbbda37f540a9bbc1f`. The split at `53d5a22c04f8c8035dfccd4577a3cdd9ece06a2b` is **66 / 242**. This was a read-only structural check, not a historical harness run or a real-ledger read.

**Preliminary comparison:** initialization and exclusions are equal; the 301 preliminary commit identities are the frozen report's prefix. **288 rows are identical**, and **13 differ only in the unit-level check-3 wording**. The path-level policy wording at the repair commit is unchanged. The seven new rows are `da93dd07`, `e4a2590d`, `b5f811d5`, `35f20c56`, `3ea6d029`, `46dbcc4b`, `8cf829c3`: each has two reserved-leaf findings and one protected touch, none has a consequence change, and five rows carry nine credential-template observations (zero in `e4a2590d` and `8cf829c3`).

**Every observation:** an independent reconstruction, with stronger exact-shape checks for the actual consequences, reproduces all 814 source/index/finding identities, reason keys and classes. The supplied classifier also reproduces the 784 preliminary observations exactly.

| Reason | Class | Count |
|---|---|---:|
| missing reserved leaves before repair | iii | 576 |
| repaired declarations still quarantined in scratch | iii | 38 |
| repair's eight quarantines and eight open INTAKE obligations | iii | 16 |
| protected touch with agent authorship unestablished | v | 21 |
| credential template with policy enablement unestablished | v | 163 |
| **Total** | **630 iii / 184 v** | **814** |

The 614 reserved-leaf findings reflect the historical genesis exemption and, after repair, the absence of human adoption in the scratch replay. The declaration commit has no check-2 finding, but its absorption leaves eight declaration keys quarantined. That is consistent with the separation between observed content and effective structure in Manual §18, not automatic adoption.

At `11ec88e4`, check 3 sees the newly created policy file by path and unit. All 19 later protected touches are of `ssds.unclassified`; Git confirms that those commits do not change `.ssds/`. The effective structure still lacks the quarantined policy leaf, so that file remains within `ssds.unclassified`, and the unit-granularity protected-surface owner produces the conditional touch. This is the disclosed scratch-genesis regime. It does not establish agent authorship or a current-policy refusal. I found no independent evidence converting these observations to class (i) or (iv).

Credential observations were checked only by code, changed path, owners and applicability; no matched credential line or value was retrieved, printed or retained. This cannot establish that an observed credential-shaped value was a real credential or that an actual confidentiality defect existed.

The evidence's limits are appropriate: check 1 has no submitted strings/objects and its diff-template observations are conditional; check 3 lacks established agent authorship; check 4 has no evaluated records and is vacuous. Record-dependent behavior needs separately authorized evidence. Consequences are this scratch ledger's, not the live ledger's; 10d owns the real-ledger comparison. Endpoint fingerprints exclude transient reverted writes and access times. Shared harness/production owners leave common-mode risk. Thus neither the all-classified count nor the absence of (i)/(iv) demonstrates general document-control or SSDS correctness. FR-B1 must be added to those limitations until repaired.

## C — revision 4 and bounded Challenge Pass

The revision preserves the settled register and accepted architecture as parents. SD-90 authorizes evaluation and planning, not papers, implementation or campaigns; SD-91 specifically establishes U4's hold; SD-95 selects later-version U1, the narrower first predictor release, paper routes, permitted history and stakeholder ratification, while leaving revision 4 proposed. The workplan represents these distinctions correctly.

- **U1:** formulation owns estimands, completion/discharge meaning, error costs, ranking objective, censoring, validity and adequacy; D2 owns prediction/update/pooling/calibration and sizing. D3 cannot fix a dependent rule before that acceptance. Existing dependency direction, operator-state separation, K4 and the resource-policy fail-closed floor survive. The stronger meter/ranking intent from Architecture 1.6.0 is not falsely promoted to accepted Manual authority. SD-95's deferral is a disclosed product-scope decision; the Manual's listed functions are not claimed implemented or removed.
- **U2:** paired baseline/population, missingness, uncertainty, multiplicity, calibration and instrument validation are routed upstream before the §31.9 campaign is proposed. G3 criteria 9 and 10 still require their live evidence; the plan does not turn separate authorization into permission to omit it.
- **U3:** claim meaning remains with the governed specification's D1/D2 owner (Manual §17.1); SSDS's exact statistic/replicate/seed evaluation contract belongs to D2. F112 continues to hold ENSEMBLE. Rule 1's explicit U3 alternative prevents the general D1-then-D2 wording from creating an unnecessary new SSDS D1 stage.
- **U4:** the population/estimand and statistical-method gaps in HARD qualification are routed to the correct upstream owners. Sidedness, clustered detections and multiplicity can change qualification, so SC-U4 is substantive rather than a demand for more samples alone. No replacement interval or threshold is smuggled into the plan. SD-91 preserves the present baseline and unqualified template forces until resolution; qualification/adoption and G3 criterion 10 remain blocked.

The interim Phase F restrictions at line 948 are consistent with these gates: no prediction, reservations, future reserves, AUTO selection or benchmark ranking; deterministic dispatch only; no statistical campaign proposal without its accepted family; no HARD qualification while SC-U4 is open; ENSEMBLE held. They are read together with G2 §5.7 rule 2: accepting D1/D2 alone does not bypass D3 reconciliation. Rule 4's provisional acceptance retains the conservative fallback, not speculative execution. Non-statistical live runs still require the separately authorized campaign route.

**Out-of-matrix challenge:** I considered whether a formally compliant stage could use provisional acceptance to start a predictor, discharge an intake obligation without adoption, substitute an audit lineage fact for authenticated independence, or use conditional study hits as real refusals. The plan's fallback and D3 gate block the first; the actual report does not do the second, but FR-B1's instrument would conceal it; F72's binding distinction blocks the third; F124's retained predicates block the fourth. No additional accepted-authority contradiction survived. Revision 4 itself needs stakeholder acceptance, but no additional Manual amendment is required merely to install these prerequisites. U4's eventual resolution and any changed D3 semantics must take the amendment/ruleset route already named.

## Evidence, non-blocking notes and limits

Executed on Python **3.12.16**, with bytecode disabled and fixture temporary directories/SSDS homes under `/tmp/ssds80-phase-f-frozen-review-8cf829c3/`:

| Check | Result and scope |
|---|---|
| focused product regression | **309 tests passed**, no skips reported: admission requests, ledger, content, prepared requests, briefs, F4b, F8g-ii, F9c-ii-iii, batch-reader/differential tests and study refusal handling; `focused.log` |
| study fixtures and import cache | **11 tests passed**, no skips reported; real fixture study owners, incomplete-progress/boundary failure cases and cache tests; `study-fixtures.log` |
| independent provenance probes | two probes reproduced FR-A1; not positive product qualification; `provenance-probe.log` |
| population and initialization | exact Git-chain and real structural-owner agreement; `initialization.py`, `initialization.log` |
| independent report/classification audit | all actual observations agree; three consequence mutations survive and unknown check-2 code is rejected; `audit.py`, `audit.json` |
| integrity/whitespace | candidate/envelope source equality and exact Manual blob verified; source-delta `git diff --check` clean; frozen protocol source/distribution/Core resources and Architecture 1.6.0 unchanged across A's delta |
| PEM | schema 1 valid, five families, zero notices; pinned base and candidate bytes equal |

For the 11 study/cache tests only, `Path.home()` was redirected to a scratch path so even unsafe-home rejection tests could not resolve the real home. This substitutes the external user-home location, not a structural, admission, derivation or classification owner. The historical harness was never run against the real repository. All other fixture homes were explicitly scratch-owned. The final source inventory contains no new bytecode.

**Non-blocking notes:**

1. D-C7-OBJECTS remains an explicit incomplete C7 audit, with its before-new-producer and exit-disclosure conditions. It cannot be erased by passing this narrower review.
2. The 8 MiB cache limit is the declared `sys.getsizeof` accounting bound; it is not a measured total-process memory cap. Prior timings are diagnostic observations, not service-level or scaling qualification. No new speedup claim is made here.
3. G2 §5.7's introductory description of all four families as statistical is broader than U3's exact computation contract; the detailed U3 row and exception carry the correct scope. This wording does not authorize a different method or create a blocker.
4. The valid committed study remains useful evidence despite FR-B1. Preserve its exact observations and passing window; a classifier defect is not grounds to rewrite the run as failed or claim an actual historical class-(iv) observation that was not found.

**PEM/HAS:** the parent workplan pins accepted project state `af0455753e20ee54a969c844872e29e270007211`, independently confirmed on project-designated `main`, with accepted PEM blob `1561797125622f355f84eb27319f87e8fa4227d9`; candidate bytes are identical, no new overlay. Canonical metadata of every family and the notices section were inspected. Task-local basis is `accepted_project_state` = that commit, `accepted_pem` = that commit/path/blob, `candidate_overlay_semantic_candidate` = `NONE`. DS-001 is APPLICABLE to real-owner evidence and limits; PC-001 is APPLICABLE to unchanged frozen-resource boundaries, supported by the current workflow's §5.1 item 6; SP-001, SP-002 and FF-001 are NOT_APPLICABLE to this non-publication, non-package-routing review. Coverage remains PARTIAL; no absence claim or historical recurrence count is inferred. The bounded cost-repair and source-delta history was inspected directly. No PEM update was made.

**Not checked / not claimed:** no full 1,907-test rerun, package build/installed-product qualification, fresh performance campaign, arbitrary corrupt-object exhaustive proof, complete untyped-field C7 audit, real-runner/model trajectory, U1-U4 method acceptance, or numerical/statistical qualification experiment. Revision 66's full-suite evidence is an inspected prior record, not a fresh result from this reviewer. The focused checks cannot convert it into a new whole-system PASS. No private keys or real SSDS homes were read; no live ledger, pending signature, 10d command, retirement/genesis operation or real-repository boundary window was touched. Historical window exclusivity is not independently observable from the committed summaries. No actual credential values were investigated. Scientific formulation, estimator accuracy and empirical outcome improvement are not claimed; C reviews their future ownership/gates only.

Only this review record was written in the repository. Existing unrelated untracked files were preserved. Scratch evidence is under the handoff's specified directory. No implementation file, plan, evidence input or release state was edited; nothing was committed or pushed.
