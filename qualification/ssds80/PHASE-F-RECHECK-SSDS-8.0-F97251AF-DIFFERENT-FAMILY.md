Governing SSDP version: 7.2.1.

# Independent Phase F repair re-check — f97251af

**Overall: NO-PASS.** The XR-C1 implementation repair passes this bounded re-check, and the retained 11b comparison and classifications reproduce. Qualification gaps remain in the case-to-assertion trace, including an incorrect claim of owner-level execution. These are evidence/acceptance blockers, not newly demonstrated production failures.

**SERIOUS CHALLENGE:** no new Serious Challenge against accepted authority. Existing SC-U4 remains open under G2 revision 4 and SD-91/SD-99, outside this repair's dependency scope. This record neither resolves it nor accepts Phase F, G3, a campaign or a cutover.

## Identity and scope

- Reviewer/asserter: AI reviewer, Codex family, independent of the Claude-family implementation and same-family check. No subagents were used.
- User-authorized handoff: `qualification/ssds80/PHASE-F-RECHECK-HANDOFF-SSDS-8.0-F97251AF.md` at `b89f5a4568efe799220bc4f505c7aee1c891b5e7`.
- Candidate: `f97251af91477b9a66ff29bc7d871c326a7dff26`; prior reviewed candidate: `c8122d66edbf7d19320f7b155e0c31033566b854`. HEAD remained the handoff commit. `git diff f97251af HEAD -- orchestrator/` is empty. Source/test line references below therefore apply to the candidate; updated evidence/plan references apply to the handoff envelope.
- Governing owners: SSDP 7.2.1, the accepted SSDS 8 Manual, G2 workplan revision 4 and its settled register, and applicable stakeholder decisions through item 83. The release-state owner confirms public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954` and recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`. Plan revision 78, the exit evidence, earlier reviews and same-family conclusions were treated as claims to test.
- Entered the software-design review skill and the repository D3 entrypoint; applied abstraction/concretization, architecture, workflow, testing, evidence, semantic-definition and project-memory guidance to this bounded implementation/evidence review. No authority amendment or implementation was undertaken.
- PEM: G2 binds integrated `main@af0455753e20ee54a969c844872e29e270007211`. Its PEM blob, current `main`'s blob and HEAD's blob are all `1561797125622f355f84eb27319f87e8fa4227d9`; there is no distinct overlay. The schema check passed: schema 1, five families, zero notices. Canonical family metadata was searched. Task-local HAS: DS-001 applicable to real-owner and claim-scope checking; PC-001 applicable through G2 §2 item 6's frozen-surface constraint; FF-001, SP-001 and SP-002 not applicable to this narrow repair review. Coverage remains partial; neither the watermark nor this search establishes historical completeness. Memory supplies no acceptance authority.

## Verdicts in handoff §3 order

| Item | Verdict | Decision |
|---|---|---|
| 1. XR-C1 commit-path repair | **PASS** | Full restart after absorption restores the held-head and identity checks; existing interleaving/duplicate tests pass. Separate bounds are present in source. |
| 2. XR-B1 named 29da56e cases | **NO-PASS** | The added observation, triple, contested-resolution and support tests are useful and correctly assert their bounded outcomes. The counter-challenge test does not carry B1(a)'s restoration of revoked passing support (RR-2); chain-class execution remains undisposed (RR-3). |
| 3. XR-B2 three mismatches | **NO-PASS** | Real authorization replaces the earlier OWNER stand-in, and rejected-request salvage now carries the discriminating set. Assessment supersession still lacks the other-obligation discriminator, including at the cited owner (RR-1); PLAN_ACCEPTANCE remains unexecuted (RR-3). |
| 4. XR-B3 citations and overclaim | **NO-PASS** | The missing case-name comments were added. Placement is repaired, but the claimed obligation-key owner evidence is absent (RR-1), and B1(a)'s citation remains a narrower trajectory (RR-2). |
| 5. Unexecuted cases and their reasons | **NO-PASS** | The class/agent independence confounder and unsupported PLAN_ACCEPTANCE supersession are real limits. “Another obligation” is a fixture restriction, not a Phase F restriction (RR-1). The resolver explanation conflates human and agent cases. Q-F31 remains a question, not an accepted scope change (RR-3). |
| 6. 11b at f97251af | **PASS** | 341 unchanged rows, eight new rows, 35 new observations and all 977 retained classifications verified within the declared historical-survey scope. |

## Blockers

### RR-1 — The obligation member of assessment supersession is not discriminated, even by the cited owner test

**Locations:** `qualification/ssds80/PHASE-F-EXIT-EVIDENCE-SSDS-8.0.md:83`; `orchestrator/tests/ssds/test_phase_f_step12.py:396`; `orchestrator/tests/ssds/test_phase_f_step4b.py:416`. **Owner:** Phase F group-3 qualification/exit evidence under G2 §5.3; production semantics remain owned by Admission's supersession authorization and Manual §5.10/§6.2/§6.7.

The exit says “another obligation AUTH_SUPERSEDES” is executed at the owner only and assigns the key's obligation member to `SupersessionTargets`. That class's assessment test fixes `obligation = "obl"` for every record and varies only the reading. It never tests a changed obligation. The new Admission test instead uses `obligation_token("code", "other")`, although the realization's specification is `spec`. Its asserted `REF_TARGET` occurs before the intended supersession discriminator. Neither test establishes the stated result.

**Concrete escaping failure:** a supersession key retaining realization and reading but omitting obligation would pass both cited discriminators: the direct-owner test never changes obligation, while the new Admission test still rejects an invalid realization/obligation reference. For a realization serving two claims, that faulty key could authorize a PASS for one obligation to supersede a FAIL for the other. This is a coverage counterexample, not an assertion that the present key is faulty: `derivation/judgment.py:771` currently includes the obligation.

**Why Phase F can carry the case:** `ledger/schema.py:124` allows a list of claim unit/revision pairs. `admission/evidence.py:54` checks each against the admitted tree, and lines 141-144 accept any obligation token formed from a named claim and the realization's specification. An admitted realization can therefore name two existing claim units, with a specification evidencing both; no accepted integration or TASK_RESULT is needed. Assess the same realization under the same reading for those two distinct, valid tokens, then attempt cross-obligation supersession. That reaches the required `AUTH_SUPERSEDES` check rather than manufacturing `REF_TARGET`. The existing runner and human admission paths suffice.

**Closure:** supply that real-Admission discriminator with authority-derived expected values and preserve the original failing assessment's disposition; correct the false owner-level claim. Alternatively, a scope change must come from the acceptance owner. The current fixture choice is not such a disposition. No new execution of this proposed trajectory was performed in this review; the reachability conclusion is source-based.

### RR-2 — B1(a)'s revoked-support counter-challenge is replaced by a realization-disposition trajectory

**Locations:** `qualification/ssds80/PHASE-F-EXIT-EVIDENCE-SSDS-8.0.md:65`; `orchestrator/tests/ssds/test_phase_f_step12.py:196` and `:208`. **Owner:** Phase F group-2 qualification, carrying `MANUAL-REVIEW-SSDS-8.0-29DA56E-NO-PASS.md` B1(a)/N5 through Admission.

The original B1 trajectory revokes a passing acceptance with an upheld non-blocking challenge, then uses a counter-upholding to restore that passing support; the sibling row names other passing judgments and the subject-triple route. The new test starts at a failing realization and observes `disposition(failing)` returning from 2 to 0. That restores an adverse dispute. It never observes a revoked passing judgment becoming usable again, nor the resulting `valid`/ACCEPT obligation consequences. The exit discloses the different root, which is good, but disclosure does not establish the original named outcome.

**Concrete escaping failure:** an implementation could correctly refuse an unattested counter-adjudication and correctly reverse realization-based disposition, yet leave a passing acceptance revoked after a valid independent counter-upholding. The new counter test and the separate direct triple-dismissal test would still pass. The required B1(a) trajectory would fail. Conversely, no test here asserts that passing support remains absent throughout the refused counter-restoration attempt.

This trajectory is available without known integration authors: the candidate's `TripleAndSupportRoute.acceptance` already admits an attested passing acceptance and establishes `valid(code) = T`. Use that acceptance as the root, uphold a non-blocking challenge independently, counter-challenge its upholding, then compare an unattested counter-upholding with an attested one. Observe refusal/ADJUDICATE recovery and the revoked/restored support and obligation states. This uses the same authorized fixture mechanisms as the new tests and needs no class-distinguishing agent or TASK_RESULT.

**Closure:** execute and cite the original support-restoration discriminator, or obtain an explicit acceptance-owner disposition of its substitution. The realization-root test should remain accurately described as its own useful case. No production malfunction or new concurrency probe is claimed here.

### RR-3 — Required unexecuted discriminators still need their acceptance-owner disposition

**Locations:** `workplans/active/SSDS-8.0-G2-PHASE-F-PLAN.md:431`, `:436`, `:437` and `:4677`; exit evidence `:71`, `:84`, `:87`. **Owner:** stakeholder acceptance of the Phase F qualification scope; the author/evidence owner must present an accurate case-specific request.

Plan §4 carries groups 2 and 3 with no deferral. Revision 78 asks Q-F31 to accept nonexecution of chain class, two S1 cases and PLAN_ACCEPTANCE overlap. The stakeholder record ends at item 83/SD-101; it contains no Q-F31 acceptance. A test being unable to discriminate the case in the present gated implementation explains the gap but does not waive it.

**Concrete closure failure:** an exit reader could combine “all tests pass” with the proposed Q-F31 rationale and mark groups 2/3 complete, although the required R2-versus-R3 chain-class case and functional PLAN_ACCEPTANCE overlap were never executed. That would convert an author's proposed disposition into stakeholder acceptance. The source/evidence correctly reports these as unexecuted; keep that status until the owner decides.

The reasons need to remain separate:

- **29da56e B1(e), chain class:** the stated confounder is supported for the Phase F histories under review. With no admitted producing integration or supported candidate-producing task result, judged authors remain unknown. `judgment.py:721` makes an agent non-independent on unknown authors; `authorize.py:112` refuses it before the class distinction. An attested human can pass independence but does not discriminate the lower-class prohibition. The direct-owner chain-class tests remain useful, explicitly owner-level evidence.
- **S1 unknown_lineage_owner_agent:** similarly, an unknown-author fixture cannot distinguish UNKNOWN lineage from fresh lineage because both agents fail the authorship test. A refusal can run; the intended lineage-sensitive comparison is not established by it. The literal Stage S case also concerns a transformation review. Do not describe these different limitations as a successful Admission discriminator.
- **S1 policy_names_resolver:** the blanket agent-lineage explanation does not describe this case. `models/cases.py:131` names two humans, non-author owner O and author adjudicator H, with owner-supersession/relief open and challenge-upholding closed. Humans can be distinguished using the attestation route already used in `OwnerRoutes`; a subject-review supersession/challenge analogue is not prevented by unknown authorship. The exact Stage S transformation-review/relief case has the additional SD-70 task-result limitation, and a subject analogue would not establish all of it. State precisely which shape and routes are required and which are deferred; “an attested-fresh agent also fails” cannot justify omitting this human-policy distinction.
- **f03b15e PLAN_ACCEPTANCE overlap:** the source and passing test confirm `SCHEMA_UNSUPPORTED` for conditional supersession, regardless of overlap. That is a genuine fail-closed limitation, not qualification of the functional overlap rule. Q-F31 must remain pending unless accepted by its owner.
- **f03b15e another obligation:** excluded from the legitimate Phase F impossibility rationale; see RR-1. It is not even included in Q-F31's requested disposition.

This review does not answer Q-F31 for the stakeholder and does not recommend waiving reachable discriminators merely because the current fixtures omit them.

## Repair findings and notes

### XR-C1: implementation repair passes

`Admission._admit_once` now returns after successful absorption (`engine.py:433-437`). `admit` re-enters through `held_head`, then searches admitted request identity before validating/appending (`:421-431`). It no longer installs a bare reload's last entry as the expected CAS parent. A losing CAS also restarts the procedure. This is consistent with Manual §8.3 step 9, §21.3, §22.4, §23.4 and §24.2.

All four `PostAbsorption` tests passed. They exercise a retirement admitted in the gap, a provisional admission left by checkpoint failure and settled before A's next append, the same request decided in the gap, and two lost admission CAS attempts after an absorption. The latter distinguishes the old shared retry budget from the separate counters. Source inspection confirms `_CAS_ATTEMPTS = 3`, independent `lost` and `absorbed` counters, and a halt when either bound is exhausted. The test is not an exhaustive test of every exhaustion sequence; the separate bounds are established by source plus the discriminating retry test. No new concurrency or key-forging probes were built. The author's claim that each test fails against the old engine was not independently rerun.

### What the new case tests do establish

- `CounterChallengeAndDismissal` carries observation dismissal, contested resolution and refused-adjudication recovery through real Admission with registered humans. Their literal disposition/standing and ADJUDICATE assertions agree with §5.10(f) and the named requirements. Its counter-challenge remains bounded as described in RR-2.
- `TripleAndSupportRoute` asserts `valid(code)` T -> F -> F -> T across a blocking triple challenge and refused/accepted dismissals. Its non-independent acceptance is admitted as data, has base/support consequences consistent with §5.10(f), leaves validity F and leaves ACCEPT derived. These are useful positive/negative discriminators.
- `OwnerRoutes` now uses the real authorization owner. It establishes the human owner's failing-assessment exception with common-mode recorded, refusal of an unattested human on the subject-review shape, and an attested human's successful upholding. These are the disclosed route-4/subject analogues, not all routes of the original transformation-review cases.
- `AssessmentSupersession` establishes the assessor's and owner's disposing reassessments, the changed-reading refusal, and cross-class EQUIVALENCE refusal with a same-class positive control. RR-1 and the disclosed PLAN_ACCEPTANCE limit prevent blanket f03b15e N5 closure.
- `RejectedRequestSalvage` repairs the earlier mismatch: the rejected carrier admits exactly report, failing assessment and adverse judgment; its passing judgment has no own refusal yet is not admitted. The secret-bearing record triggers rejection. Leaving TASK_RESULT out avoids the earlier unclean-result confounder and is disclosed under SD-70.

### Citation and scope notes

The added comments in steps 4b, 6b, 7b, 7c, 7d and 7e name the intended cases. The corrected 7e comment accurately describes a class-tuple refusal rather than claiming execution of the quorum inequality itself. XR-B3's original placement defect is repaired; the remaining NO-PASS concerns semantic mappings, especially RR-1/RR-2.

Exit row 70 says ADJUDICATE recovery is checked “in each of the above.” The support-route acceptance test has no challenge/adjudication and cannot make that assertion. Read the recovery claim as the four relevant adjudication tests, and correct the wording. This is a bounded reporting note, not a separate blocker. Likewise the group-3 direct eligibility and reviewer-selection rows remain owner-level checks; they do not execute a complete Dispatcher transport/issue path or every record-kind independence input. The prior exit Review's limits remain applicable.

## 11b retained-evidence verification

`/tmp/ssds80-phase-f-recheck-f97251af/study-verification.json` records the local comparison results. No study, boundary or window script was executed.

- The first **341** commit-row objects equal `c8122d66`'s complete array, field for field and in order. Initialization and all **740** exclusions are unchanged.
- The **8** added commit identities equal `git rev-list --first-parent --reverse c8122d66..f97251af`. Every one of the 349 rows' parent links matches Git, forming a contiguous chain from initialization to the candidate.
- The existing classifier reproduces the complete **977** observation objects exactly. The old **942** form an unchanged prefix. Independently rebuilding the new observation identities/classes/reasons from the eight rows yields exactly **35**: 16 reserved-leaf scratch-quarantine observations in class (iii), 11 conditional credential-template observations in class (v), and eight conditional protected-touch observations in class (v). No added row has a consequence change or writes `.ssds/` paths. The protected unit remains `ssds.unclassified` in the declared scratch-genesis regime.
- Totals match: **712 (iii), 265 (v)**. No new observation warrants class (i) or (iv) on this evidence. Credential enablement and agent authorship remain unestablished; no credential value or matched line was reconstructed.
- Report SHA-256: `aabe7f13992bd44ad7629e42b24c2b23f1a7a4ba6f17f33bc220491276a9b42b`; classification: `87e248da885d60eb7aac41106d35c06b13f3b7bf42466b41fd00f15220f610e0`. Both match the declared bindings. The window, harness and boundary-script file hashes match the retained window record. That record identifies the candidate, harness exit 0, compare exit 0, PASS and 1,950 seconds.

This verifies retained data consistency and the classification, not the original execution's exclusivity or a fresh historical replay. The 740 exclusion reasons were compared, not independently rederived from every historical tree. Check (4) stays vacuous; record-dependent behavior and production/runtime completeness remain outside the survey. Shared harness/production owners retain common-mode risk. The classifier's previously disclosed inability to prove completeness of an empty consequence report is unchanged. No earlier failed or contaminated window becomes qualified through this PASS.

## Executed checks and limits

From `orchestrator/`, with `TMPDIR=/tmp/ssds80-phase-f-recheck-f97251af`:

```bash
PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /tmp/claude-1000/ssds-runtime-20261030/bin/python -B -m unittest tests.ssds.test_phase_f_step12 tests.ssds.test_phase_f_step4b tests.ssds.test_phase_f_step6a tests.ssds.test_phase_f_step6b
```

**89 tests passed in 50.706 seconds.** Output: `/tmp/ssds80-phase-f-recheck-f97251af/focused-tests.log`. Existing fixtures created their own scratch homes under the designated TMPDIR. The PEM validator also passed. These checks do not replace the author's full-suite/build/packaging results, which were not independently rerun.

Read-only work covered the source delta, its held-head/commit context, the new tests and their fixtures, the named prior-review discriminators and Stage S case definitions, current Manual owners, relevant authorization/authorship/assessment-reference/supersession owners, revision 78, the exit evidence and retained study files. Stage S models were read, never run for expected values. No new behavioral probe was constructed; the proposed missing trajectories above are source-based review counterexamples. The only newly executed product variant was candidate f97251af through existing focused tests; no mutation-selected or old-engine result is represented as a fresh observation.

Not checked: a new live-ledger reading or append; the re-read or 11b windows; harness execution; physical witness deployment; a fresh full Admission/Dispatcher/Derivation audit; all record-kind independence inputs; original window exclusivity; lost raw historical logs; full-suite, root regression, package, distribution or Core requalification. No `~/.ssh` or `~/.ssds` was read. No scientific dataset or scientific outcome was evaluated, and no accepted D1/D2 result is being affirmed; the realized results here are bounded software qualification evidence. The materiality basis is the handoff's protected commit invariants and mandatory real-owner discriminators. No scientific retention/projection change was made.

Only this review record was authored in the repository; scratch stayed under the named directory. No tracked candidate/evidence/authority file was edited, and no commit or push was made. Later status showed unrelated untracked dotfiles/configuration that were absent from the initial status output; their origin was not established and they were left untouched. This record supplies neither a waiver of RR-1/RR-2 nor acceptance of Q-F31. Re-review closure requires corrected, discriminating evidence and the acceptance owner's explicit disposition of genuinely unexecutable mandatory cases.
