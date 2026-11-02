Governing SSDP version: 7.2.1.

# Independent narrow Phase F re-check — 36b0ab5f

**SERIOUS CHALLENGE:** no new Serious Challenge identified. SC-U4 remains open at the accepted Manual §14.7 / G2 §5.7 owner under SD-91 and SD-99; this test-only repair neither resolves it nor depends on resolving it.

**Overall: PASS for the five items in the pinned handoff's §3.** RR-1 and RR-2's missing discriminators are repaired. RR-3's reachable resolver analogue is repaired and the remaining nonexecution is accurately disclosed. This is not a Phase F exit PASS: RR-3's acceptance-owner disposition remains pending as Q-F31. SD-102 expressly leaves that question open. No acceptance, waiver, campaign, G3, cutover or dependent-phase authorization is supplied by this record.

## Identity, authority and mutation boundary

- Reviewer/asserter: AI reviewer, Codex family, independent of the Claude-family author and same-family check. No subagents were used.
- Handoff: `qualification/ssds80/PHASE-F-RECHECK-HANDOFF-SSDS-8.0-36B0AB5F.md` at `967e9c9ec94c1a91f70972cdeecca2cd7bae5e13`, which remained HEAD throughout this review.
- Candidate: `36b0ab5f89a9b99c6979a81050e55fc3198a6c24`; prior candidate: `f97251af91477b9a66ff29bc7d871c326a7dff26`. `git diff 36b0ab5f HEAD -- orchestrator/` is empty. The orchestrator delta between candidates changes only `tests/ssds/test_phase_f_step12.py` and `tests/ssds/test_phase_f_step9d_iii.py`. Production code is unchanged.
- Governing owners: SSDP 7.2.1; accepted Manual `orchestrator/docs/ssds-8.0-architecture.md` (candidate blob `438cb113b155c2e79715430338a543615fa7f143`), especially §5.3, §5.5, §5.10, §6.2-§6.8 and §31; G2 workplan revision 4 and its settled register (§4.2, §5.1, §5.3); applicable stakeholder decisions through item 84/SD-102. The release-state owner binds public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954` and recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`.
- The previous re-check, f03b15e B1/N5, 29da56e B1/N5 and Stage S `models/cases.py` supply the named counterexamples/expected outcomes. Stage S models were read, never executed for expected values. Plan revision 80, exit evidence and same-family conclusions were treated as claims to test.
- Entered the repository software-design role and installed 7.2.1 software-design skill, with abstraction/concretization, architecture, workflow, testing, evidence, semantic-definition and PEM guidance. This is a bounded D4 evidence review, not an authority amendment.
- Source/test line references below apply to the candidate. Evidence/plan line references apply to the handoff envelope at HEAD. Only this record is authored in the repository; all scratch is under `/tmp/ssds80-phase-f-recheck-36b0ab5f/`.

## Verdicts in handoff §3 order

| Item | Verdict | Basis |
|---|---|---|
| 1. RR-1: other-obligation discriminator at Admission | **PASS** | Both obligations are valid targets of one realization; the other-obligation PASS succeeds alone, fails with exactly `AUTH_SUPERSEDES` across the key, and same-key supersession succeeds and disposes. |
| 2. RR-2: revoked passing acceptance restored by independent counter-upholding | **PASS** | The test now uses the acceptance itself as the root and observes validity, renewed ACCEPT and refused-adjudication recovery through the complete revoked/restored trajectory. |
| 3. RR-3: resolver analogue and truthful remaining scope | **PASS** | Real authorization distinguishes the independent policy owner from an independent peer and a non-independent owner, and refuses the non-independent human adjudicator. Q-F31 remains pending, narrowed to the three stated unexecuted discriminators. |
| 4. Exit evidence for these cases | **PASS** | The rows now match the tests, distinguish the acceptance and realization trajectories, correct the false obligation-key owner claim, and delimit recovery, analogue and sibling coverage. |
| 5. 11b at 36b0ab5f | **PASS** | The 349 old rows, 977 old observations, four new rows and 17 new observations verify; all 994 classifications reproduce within the retained-data scope below. |

## Blockers and pending acceptance

**No new blocker in this narrow re-check; no RR2-n finding is assigned.** There is no newly demonstrated production failure or escaping failure scenario for the three repaired discriminators.

The earlier RR-3 acceptance condition is **not closed**. Phase F plan §4 (`:433`, `:436-437`) still carries the required group-2/group-3 cases without deferral. Stakeholder decision item 84 (`STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md:557-559`) explicitly leaves Q-F31 unanswered. The concrete closure error to avoid is treating this narrow PASS or the green suite as permission to mark chain class, agent-lineage discrimination or functional PLAN_ACCEPTANCE overlap executed/accepted. The owner of that disposition is the stakeholder; the evidence owner must continue to preserve their unexecuted status. This record does not silently convert the earlier overall NO-PASS into a Phase F exit PASS.

## Repair analysis

### RR-1: obligation-key attribution

`test_phase_f_step12.py:458-491` constructs a second D4 unit and an EVIDENCES edge to it, then admits one realization claiming both `code` and `other`. The changed `AdmittedRuns.realize` helper (`test_phase_f_step9d_iii.py:179-210`) preserves its original default and sends the requested claim list through the existing runner admission path. The unbounded execution basis covers the whole tree; no bounded-completeness claim about the added unit is assumed. Neither supersession authorization nor its key branches on that bound.

Three assertions distinguish the former escaping concretization:

1. A PASS for `obligation_token("other", "spec")` is admitted without supersession. Thus a malformed or unsupported second target cannot explain the negative result.
2. The same realization, reading, actor and attested independence, now naming the first obligation's FAIL in `supersedes`, receives exactly `AUTH_SUPERSEDES`; the failure remains undisposed (`0`, F).
3. A PASS on the FAIL's own obligation, retaining the other key members and actor, is accepted and changes disposition to `2` (T). A blanket prohibition on assessment supersession cannot satisfy the test.

The production reference check accepts obligation tokens for the realization's named claims (`admission/evidence.py:132-144`). `_supersession_authorized` compares the supersession targets before actor/independence checks (`admission/authorize.py:260-284`), and `supersession_target` includes realization, obligation and reading (`derivation/judgment.py:771-773`). Removing only the obligation member would remove the distinguishing refusal in this trajectory. That is a source-based counterfactual judgment; the author's mutation run was not repeated. The earlier `SupersessionTargets` reading-only test is no longer offered as evidence of this obligation member.

### RR-2: restoration of revoked support

`test_phase_f_step12.py:320-346` now carries B1(a)'s relevant support trajectory, not merely the earlier realization-disposition analogue. A passing attested ACCEPTANCE makes `valid(code) = T`; a non-blocking challenge leaves T; an independent upholding changes it to F and derives ACCEPT. A non-blocking counter-challenge followed by an unattested counter-upholding leaves F and ACCEPT, with `ADJUDICATE(c2)` still open. The attested counter-upholding restores T and removes both obligations.

The genesis human and three additional humans registered through lifecycle admission are distinct. The challenge, upholding, counter-challenge and counter-upholding go through real Admission, and validity/obligations come from real Derivation/Workflow. No revocation or resolution is seeded. The negative helper (`:202-205`) checks refusal of the adjudication alone with `AUTH_ACTOR` and its absence from admitted records. The former failure scenario—realization disposal working while a passing acceptance never regains support—would fail the final validity/ACCEPT assertions. A non-independent counter-upholding restoring support would fail the refusal and intermediate-state assertions.

This establishes the ACCEPTANCE instance. It does not execute the other passing-judgment siblings, an R2-versus-R3 agent chain, a full Dispatcher transport or an inspector trajectory. The exit row explicitly limits the record-kind claim.

### RR-3: owner route and remaining nonexecution

Stage S `policy_names_resolver` (`models/cases.py:131-135`) separates the non-author policy owner from the author adjudicator. Its subject-review analogue now executes at `test_phase_f_step12.py:531-558`:

- The adverse REVIEW stands. An unattested human's challenge-upholding is refused alone and the adverse review still stands.
- An attested non-owner peer's supersession is refused with exactly `AUTH_SUPERSEDES`. Independence alone is insufficient.
- The policy owner's unattested supersession is likewise refused, leaving the objection standing. Ownership alone is insufficient.
- The policy owner's attested supersession is accepted and ends the adverse review. A blanket supersession refusal is excluded.

The test uses the real `authorize`, not a stand-in. `NativeCode.policy` (`:281-283`) names the genesis human as owner; the adverse reviewer and peer are distinct humans. The test therefore catches SF-R1's escaping behavior, in which any independent peer could supersede another actor's judgment.

**Analogue limit:** the human called `author-adjudicator` is not established as a known content author by an admitted integration. It is a human of unknown authorship with no non-authorship attestation, hence non-independent under the exercised rule. The module and test comments disclose this. The independent side uses authenticated attestations; actual authorship truth is not empirically established by this fixture. This is sufficient for the expressly requested subject-review analogue, not proof of the original transformation-review history. Route 3 relief and that transformation-review form are explicitly unexecuted; subject-triple reviews have no per-target-relief route under Manual §5.10(c).

The narrowed Q-F31 rationale is supported by the source and remains a request, not acceptance:

- **29da56e B1(e), chain class:** unknown content authorship prevents agent independence (`judgment.py:718-722`); `_adjudication_eligible` refuses non-independence before its chain-class branch (`authorize.py:108-115`). An attested human always satisfies that class branch, so these Phase F histories do not discriminate an otherwise independent lower-class agent. Step 4b supplies owner-level evidence only.
- **S1 `unknown_lineage_owner_agent`:** unknown and fresh agent lineages both fail against unknown content authorship. Running that refusal would not discriminate the intended lineage distinction. The transformation form additionally needs the SD-70-gated task-result path.
- **f03b15e PLAN_ACCEPTANCE overlap:** conditional supersession remains unsupported (`judgment.py:746-763`, `authorize.py:153-158`, `:215-224`). The existing fail-closed test passes, but it does not establish functional overlap preservation.

The resolver analogue and the other-obligation case are no longer incorrectly grouped with those limitations.

### Exit-evidence reconciliation

The requested diff from `6a7ad8d9` was inspected. `PHASE-F-EXIT-EVIDENCE-SSDS-8.0.md:67-74` separates acceptance restoration from realization disposal and restricts the ADJUDICATE recovery claim to the five adjudication tests, explicitly excluding the support-route test. Rows `:85-91` correct the obligation-key claim, identify routes 2/4 of the resolver analogue and its peer/owner controls, and retain the unexecuted cases. No remaining material overclaim was found in these rows when read with their cited fixture limits. Their use of “author adjudicator” should be understood as the disclosed non-independent-human analogue above, not independently proven known authorship.

## 11b retained evidence

Scratch `verify_study.py` and `study-verification.json` record the checks. No window, harness or `shadow_boundary.py` was executed.

- All **349** earlier commit-row objects equal `PHASE-F-DIFFERENCE-STUDY-REFROZEN-f97251af.json` field for field and in order. Initialization and all **740** exclusions are unchanged.
- The four new rows are exactly the first-parent interval `f97251af..36b0ab5f`: `367bc16b`, `b89f5a45`, `6a7ad8d9`, `36b0ab5f`. All **353** commit/parent pairs match Git and form the contiguous chain from initialization `09f35057` to the candidate.
- The existing classifier reproduces all **994** observation objects and its reason table exactly. The previous **977** observations are an unchanged prefix. Separately constructing the new identities, classes and reasons from the four new rows reproduces exactly **17** observations: eight reserved-leaf scratch-quarantine observations in class (iii), five conditional credential-template observations in class (v), and four conditional protected-touch observations in class (v).
- All four new rows have empty consequence changes; none writes a `.ssds/` path. The protected owner is `ssds.unclassified` in the declared scratch-genesis regime. There is no new evidence for class (i) or (iv). Credential-policy enablement and agent authorship remain unestablished; no matched credential value or line was reconstructed.
- Totals agree: **720 class (iii), 274 class (v)**. The report is COMPLETE with final boundary PASSED. Report SHA-256 is `a7394627c28c071d6b5e18db9fe37ac844f5f075373fd5f4ecff27a37c0c8d5d`; classification SHA-256 is `a324c40aa1cdd2d561530e94d1889b152c91bc1577e0be8b94d7ec99f9303447`. Both match the retained bindings.
- Window metadata binds this candidate, harness/compare exits 0, PASS and 1,950 seconds. Its three tool hashes match the retained window script, harness and boundary-script bytes.

This verifies retained-data consistency and classification, not a fresh historical replay or the original window's exclusivity. Exclusion reasons were compared, not independently rederived across every excluded tree. Check (4) remains vacuous; record-dependent outcomes and production/runtime completeness remain outside the survey. Shared harness/production owners retain common-mode risk, and the classifier cannot prove completeness of an empty consequence report. No prior failed or contaminated window becomes qualified by this result.

## Executed checks, historical applicability and limits

From `orchestrator/`, the prescribed interpreter and bytecode controls were used:

```bash
TMPDIR=/tmp/ssds80-phase-f-recheck-36b0ab5f PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /tmp/claude-1000/ssds-runtime-20261030/bin/python -B -m unittest tests.ssds.test_phase_f_step12 tests.ssds.test_phase_f_step9d_iii tests.ssds.test_phase_f_step4b
```

**93 tests passed in 74.047 seconds**, with no skips reported. Log: `/tmp/ssds80-phase-f-recheck-36b0ab5f/focused-tests.log`. This covers the repaired tests, the changed realization helper's existing consumers and adjacent authorization tests, including the existing PostAbsorption regression tests. It does not independently reproduce the author's mutation checks or full-suite/build claims. The PEM schema validator passed (schema 1, five families, zero notices). No Python bytecode appeared under `orchestrator/src`.

PEM activated because G2 explicitly binds it and this round revisits a case-to-assertion failure family. The task-local basis is:

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: 1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: Test each claim at its real owner and preserve analogue and nonexecution limits.
  - id: PC-001
    disposition: APPLICABLE
    reason: G2 section 2 item 6 independently requires frozen-surface preservation; this review changes none.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: No protocol bootstrap or public-source publication.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No source/package routing repair or regeneration.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No release publication or recovery selection.
```

The workplan-bound base, designated integrated `main` and HEAD all resolve to that same PEM blob, so there is no distinct overlay. Canonical family metadata, not just summary temperature, was searched. The file's historical overlay wording does not create a new overlay or current authority. Its coverage is PARTIAL; this bounded lookup does not establish historical completeness. Memory supplied hypotheses and scope discipline, not acceptance authority.

Not checked: real-ledger reads or appends; any re-read/11b window or harness execution; physical witness deployment; a new Admission/Dispatcher/Derivation audit outside these repaired claims; complete original Stage S trajectories or all record-kind/lineage variants; original window exclusivity; full-suite, root regression, package, distribution or Core requalification. No new concurrency, mutation or key-forging probe was built. Existing tests used their fixture keys and scratch homes; no `~/.ssh` or `~/.ssds` was read.

The only newly executed product variant was candidate `36b0ab5f` through existing tests. The historical study was reviewed as retained evidence, not rerun or selected from new trials; earlier run/selection history remains bounded by its existing records. No scientific dataset or scientific outcome was evaluated, and no accepted D1/D2 proposition is affirmed. The realized results are software qualification evidence; materiality follows the handoff's three discriminators and truthful exit/classification claims. No scientific retention/projection change was made.

No implementation, authority, plan, evidence or PEM file was edited. The pre-existing untracked dotfiles/configuration were left untouched. No commit or push was made. RR-1/RR-2 and the resolver repair pass this round; Q-F31 and Phase F's exit remain with their acceptance owner.
