# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 20

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 947370d31fbd7bc53272bdbc401244624137c855
    SCOPE: whole proposed architecture; (a) the revision-20 repairs: one content notion for every stop,
           standing and withdrawal (assessed content = executed content + reading; `on`; passing
           currency on the same execution basis; "admitted" defined once); the revised discriminating
           pair (rerun trigger, base trial, conditions 1-5 on executed content, the reading pair,
           withdrawal latch, signed run enumeration); `here` with mechanical-oracle "reproduces"; the
           decision-class exception, floor deferral ending on admitted (possibly INCOMPLETE)
           observations, mechanical resubmission of refused never-lost bytes, the corrected C2b
           statement; the model check with named/un-named content, three outcomes, P13, P14 and REV19;
           (b) workflow execution and verification layer and the doctrine-realization objective;
           (c) persistence, derivation, concurrency and migration; (d) Protocol 7.2.1 inheritance
           reconciliation; plus, by mid-review stakeholder instruction, a family-level convergence
           assessment of the §6.6 assessment-disagreement machinery (§5 below)
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: 40267d35b1ace7d505c0596a786cf8f3fd1d54de (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5,
           AC71FA9, 730490D, FB3E542, 124B0B7, 97E753F, 4C35D92, 644EB72, 62C0B24,
           203A42B, A414588, 6FE1000, 4EC0024, BA7F738; all NO-PASS
    REVIEW METHOD: immutable-owner reconstruction; each revision-20 repair attacked as a new mechanism,
           in particular where two repairs of the previous cycle meet; prior-finding re-derivation;
           family-level convergence assessment (mid-review instruction); exact-candidate structural
           tests, whitespace check, the bounded model check in every requested mode, and a bounded
           probe of the model on one trajectory found here
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session from
           REVIEW-HANDOFF-SSDS-8.0-REVISION-20.md (stakeholder SD-8); same model family as the author
    MID-REVIEW INSTRUCTION: during this Review the coordinator relayed an additional stakeholder
           instruction (2026-10-13): read the convergence owner's "Active simplification trigger" and
           "Review strategy after recurrence"; assess the §6.6 disagreement family for post-simplification
           recurrence, minimum justified concretization and common-mode causes; route at family level;
           record that the instruction was added mid-review. It gave no author conclusion. Everything
           else in the handoff stood.
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-947370D-NO-PASS.md

Candidate section references below mean the [primary workplan at the candidate][wp]. Governing-owner links pin the public source above. This context authored neither the candidate nor any prior Review, received none of the authoring conversation, and treated the handoff's scope description, the workplan's self-assessments (§0.1, §27.34-§27.35), the model check's green result and every prior verdict as hypotheses.

The blocker below is a deduction from the proposed contracts, not an observed SSDS runtime failure. One of its two trajectories is reproduced in the candidate's own bounded model (§7); the other is not representable there. Its asserter is the reviewer named above; its disposition is **OPEN** against the exact candidate. This record is its canonical home. Revisit after the D3 owner has performed the bounded reconsideration of the §6.6 disagreement family that §5 describes, regenerated §0.1, §22, §27 and the model check from the result, and frozen a replacement candidate. No accepted project scientific D1/D2 claim is challenged.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The [kernel][kernel] says: “A coherent parent with a wrong child is an ordinary blocker.” The governing [evidence owner][evidence] is coherent and realizable for this concern. It requires that applicability be recoverable over “evidence-spec revision, subject/candidate, governed-claim revision, input/validity regime, oracle semantics, environment/backend/precision/configuration, stochastic replicate identity and protocol obligation”, and says:

- “A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority. A stale passing observation is not admissible confirmation.”
- “Use `review-required` when applicability is uncertain.”
- “When competent evidence assessments materially conflict, preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence. … supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement.”

The [convergence owner][convergence] is also coherent here: “post-simplification recurrence, or evidence governing abstraction is wrong -> bounded reconsideration of the earliest affected abstraction”, and active simplification “is **mandatory before another additive durable repair** when evidence shows repeated patches around the same mechanism, patch-on-patch repair, … special cases accumulating around one owner”. The blocker lies in the D3 candidate, which is proposed and not accepted, so it is an ordinary blocker routed through that owner, not a Serious Challenge.

The stakeholder record (blob `edbf40da…`, unchanged since `a414588`) supports what the workplan attributes to it. SD-2 (“A deterministic flow carries important discoveries and decisions to the human inspector …, while agents and the deterministic framework handle the rest”), SD-5, SD-6 and SD-8 are cited faithfully. Nothing in the candidate claims that a sub-agent PASS accepts the architecture (§25).

## Verdict

**NO-PASS.** One family-level blocker remains, **W**, with two concrete members found in this cycle. Both sit where two of the previous cycle's repairs meet, and both make a stated revision-20 guarantee false:

- **W1 — a reading counts as "admitted" if it was ever admitted.** The reading pair applies only where `a-`'s reading “was never admitted”, and revision 20 defines admitted as present or required “at some ledger position, by any route”. A candidate that restores a specification or claim revision which was admitted once and later relaxed, and fails under it, can therefore never be paired. Its trial on admitted content under the admitted (relaxed) reading passes, the outcome is unchanged, and condition 2 forbids the ordinary pair. The failure counts in the admitted state, qualifies the admitted D1/D2 subject and blocks other lineages that require the obligation. Its floor item latches, and only an R3 human decision lifts it. That contradicts §6.6's own guarantee: “the pair fails to form only where the admitted content, under the admitted reading, yields the same failure”.
- **W2 — a mechanical reading pair stops standing whenever the output moves at all.** In `here`, an observation “shows `a-`'s assessed value … (for a mechanical oracle: when `a-`'s reading fails it)”, and the reading-pair exception exempts only “an outcome `p`'s trial had”. For the test-first tightened tolerance that the reading pair was built for, the admitted code fails `a-`'s never-admitted reading by construction. Any later admitted change that shifts the evaluated output at all, while still passing the admitted reading, therefore “reproduces” the abandoned candidate's failure. The failure counts again in the admitted state and needs a new pair. Under the reading of the floor in which deferral ends once both first executions are admitted and no disposition stands, a latched human item follows. This is `4ec0024` C1 (“resolved failures resurrected at every later edit”) reproduced in the reading-pair branch, and it falsifies “The pair therefore never lapses through mere change”.

Revision 20 closes `ba7f738` U1 (U1a, U1b, U1c) and U2 on their trajectories, and closes N3, N5, N6 and N7. It closes N4 in part. N2 is partly closed, and its mechanical clause is the cause of W2. N1 remains partial. The earlier Reviews' closures hold (§3).

This is the eleventh consecutive NO-PASS on the §6.6 disagreement family since revision 10, and the fourth since revision 17's declared simplification. Per the convergence owner, and as the mid-review instruction asks, **W is routed as one family**: post-simplification recurrence that calls for bounded reconsideration of the §6.6 disposition abstraction before any further additive repair (§5). Two narrow local fixes are available and are recorded under W. This Review does not hold that applying only them would close the family.

Requested checks: the four routing tests pass and `git diff --check` is clean. The model check is green at depth 4 (814,450 transitions, 64/64 discriminators) and at depth 5 (DEPTH5_RESULT). Every sensitivity mode is red on owner-grounded properties. `REV19=1` is red only on the two properties revision 20 added (P13, P14); see §6. A bounded probe shows the model reproduces W1 and P13 does not flag it, because P13's “owner's sense” predicate reuses the candidate's “never admitted” test. W2 is unrepresentable in the model, which has no mechanical verdict function. None of these checks establishes semantic adequacy.

## 1. Blockers by earliest owner

### W — the §6.6 disposition machinery's sub-predicates disagree about which reading a failure belongs to (members W1, W2)

**Owner text at the candidate.**

- §6.6, “One content notion”: “The start over-approximates and the stop covers it: a failure that counts in the admitted state although its assessed content differs from the admitted content can always be paired against admitted content, and the pair fails to form only where the admitted content, under the admitted reading, yields the same failure.”
- §6.6, definition: “**Admitted** means, for content, a revision or an obligation, present in the observed tree, or required, in the admitted state at some ledger position, by any route: integration, absorption or adoption (`ba7f738` N6).”
- §6.6, pair: “The trial is read under `a-`'s reading, except in a **reading pair**: where `a-`'s reading includes a specification or claim revision that was never admitted, and the trial ran on admitted content, the trial is read under that content's own admitted reading.” Condition 2: “On every failing output, the trial's evaluated outcome differs from the reproduction's. A reading pair needs no outcome change”.
- §6.6, `here`: “o shows a-'s assessed value on an output when its outcome there is a-'s (for a mechanical oracle: when a-'s reading fails it), except that, where p is a reading pair and G's reading is the admitted reading p's trial was read under, an outcome p's trial had is not a-'s value”.
- §6.6, standing: “The pair therefore never lapses through mere change”; “A failure caused by anything a candidate changed (named code, a runtime parameter file, data read by path, a tightened tolerance, a revised claim) therefore costs one pair”.
- §0.1 U2 row: “A reading pair stands while the admitted reading is the one its trial was read under; another admitted change of that specification or claim needs one new trial, never a human decision by itself.” §27.34: “Unrelated change inside the execution basis after a pair | Provisional until the configuration reruns”.
- §6.6 floor and §7.9: the floor item “is created once the reproduction and the first trial of its scheduled pair against admitted content both have admitted observations and no disposition stands”, and it “latches”.

**W1 trajectory (every step locally compliant).** D2 claim unit `u` of admitted D2 subject `s`; specification `σ EVIDENCES u`, with a mechanical or assessor-read oracle.

1. At position 10 a proposal tightens the claim or tolerance to `u'`/`σ'`, with a code change that meets it; it is integrated. `u'` is now admitted.
2. At position 20 the owner relaxes it back to `u`/`σ` (for example, a benchmark was found too strict). The relaxation is accepted and integrated; the admitted code still passes `σ`.
3. At position 30 an implementer item based on position 25 restores `σ'` byte-identically, test-first, without the code change. The reviewer assesses the designated run FAIL under `σ'` (`a-`). The proposal is rejected and the item abandoned.
4. `a-`'s obligation is admitted, so `starts` holds and `a-` counts in the admitted state at once. Its reading differs from the admitted one, so S3 derives the rerun obligation. The trial on the base, read under `σ`, PASSes, and the reproduction under `σ'` FAILs. But `σ'` was admitted at position 10, so this is **not a reading pair**. As an ordinary pair it needs condition 2, and the outcome is identical (same code), so **no pair can ever form**.
5. Admitted `s` is `P` and its dependents are provisional. Other lineages whose frames require `(σ, u)` count `a-`. The floor deferral ends with both first executions admitted and no disposition, so the D2 floor item is created and latches. Only an owner adjudication or `IMMATERIALITY`, each R3 for D1/D2, lifts it.

The candidate's own model reproduces W1 (§7): with `ORACLE(tight)`, then `ORACLE`, then `PASS`, `FAIL(tight)` and a reading pair whose trial outcome equals the reproduction's, the pair is refused and `V = P`. The same ledger without the earlier admission of the tight reading gives `V = T`. The same predicate also routes a pure code revert to an R3 assessor-read pair, because it keys the second decision-class exception on content that “was never admitted”: a candidate that reverts a fix to an earlier admitted revision and fails is not “the candidate's own” under it.

**W2 trajectory (every step locally compliant).** The `ba7f738` U2a case, which revision 20 claims to repair, with a mechanical oracle: the admitted code's error on the benchmark is `5.0e-6`, `σ` has tolerance `1e-5` and the candidate's `σ'` has `1e-6`.

1. The candidate tightens `σ` to `σ'` test-first. Its designated run gives evaluated outcome `X` (5.0e-6), which `σ'` fails (`a-`). Abandoned.
2. Reading pair: reproduction outcome `X` on the candidate tree; trial on the base with the same outcome `X`, which `σ` passes. It forms (R2, mechanical) and stands in the admitted state, because the exception exempts the trial's outcome `X`.
3. Any later admitted change inside the execution basis (whole tree wherever completeness is not established; an unrelated refactor, a compiler flag, a reordered reduction) shifts the error to `5.1e-6` (`Y2`). The integration's rerun of the configuration (§6.6, §10) yields `Y2`, which `σ` passes and `σ'` fails. In `here`, `Y2` is not the trial's outcome, so it is not exempt, and “`a-`'s reading fails it”, so it **shows `a-`'s assessed value**. `here` is false and **`a-` counts again in the admitted state**, although the admitted content passes the admitted reading and nothing admitted ever contained `σ'`.
4. A fresh reading pair (retained reproduction, new trial on `Y2`) can re-form, but only after the next drift, and again after each later one. Meanwhile:
   - `s` is `P`;
   - the floor's deferral condition (both first executions admitted, no standing disposition) is already met, so under the state reading of “once … and no disposition stands” a D2 human item latches;
   - an integration whose rerun causes the regression may fail §6.8 step 8 (“every obligation discharged at the current head and affected by the merged tree stays discharged”) unless it carries the new pair.

The assessor-read variant does not fail this way, because there “reproduces” is outcome identity. The defect is the `ba7f738` N2 repair (mechanical “reproduces” means FAIL under the failure's reading), applied unchanged to a pair whose failing reading is by definition not the admitted one.

**What it violates.**

- The [evidence owner][evidence]: in both members `a-` applied a governed-claim or specification revision that is not the one in force, so it “is not admissible evidence against current authority”. The design's own discriminating evidence (a trial on admitted content passing under the admitted reading) exists, yet the disagreement is presented as live, so the record does not “distinguish resolved reassessment from still-live disagreement”.
- The stakeholder direction SD-2 and §1.2 (“reduces, rather than transfers, complexity to agents and humans”): a rejected or abandoned interpretive proposal becomes a latched human item and a project-wide provisional status.
- The candidate's guarantees quoted above. W2 also reproduces `4ec0024` C1, which revision 19 closed and revision 20 claims to keep closed (§27.34 C1 rows).

An implementer cannot satisfy both the §6.6 predicates and the §6.6, §0.1 and §27.34 guarantees on these trajectories without choosing between them.

**Earliest owner.** D3 §6.6, Assessment disagreement: the reading-pair predicate, the definition of admitted as used by the pair and by the decision-class exception, and `here`'s mechanical clause, with §7.9 (floor) and §22. Not Manual: §6.6 fixes each predicate explicitly, and §0.1, §22 and §27.34 fix the intended outcomes.

**Minimum repair direction.** Family first (convergence owner; §5): reconsider the earliest affected abstraction, the representation of “a failing observation does not stand here” as a supersession record gated by a five-condition pair whose standing `here` then re-derives per frame, before adding another clause. If the owner, after that reconsideration, keeps the pair abstraction, the two members have narrow subtractive fixes:

- **W1:** key the reading pair, and the decision-class exception, on whether `a-`'s reading (or content) was **in force in the admitted state at `a-`'s base position**, not on whether it was ever admitted. The positional test the floor already uses (“where `a-`'s assessed content was the admitted content when `a-` was admitted”) is the model. The transient-push case of N6 then needs no separate rule: a reading in force only while a foreign push stood is in force for failures based there, and for no others.
- **W2:** for a reading pair in a frame whose reading is the admitted reading its trial was read under, decide “shows `a-`'s value” under **that admitted reading** (a mechanical FAIL under it, or identity with an outcome `a-` had and the trial did not), not under `a-`'s never-admitted reading.

**Required discriminators**, through real Admission, Derivation, discharge and inspection consumers:

- W1: a tightened reading admitted, relaxed, restored test-first in a frame, failed, rejected and abandoned: admitted `s` unqualified after the pair on the base, no human item. Contrast: a failure made while the tightened reading was in force still counts after the relaxation until a judgment (`4c35d92` oracle-move cases kept).
- W2: a mechanical reading pair, then an unrelated admitted change that shifts the output within the admitted tolerance: no qualification and no floor item. Contrasts: a change that makes the admitted reading fail the output counts; a revert to an outcome `a-` had and the trial did not still reproduces.
- In the model or a separate bounded check: a reading that can be admitted, relaxed and restored, and a mechanical verdict function distinct from outcome identity. P13's “owner's sense” must be stated independently of the candidate's reading-pair predicate (§6).

## 2. Non-blocking findings

### N1 — historical governing-version adoption remains partly evidenced

Unchanged since `62c0b24` N1 (§0.4; stakeholder record, “Not covered”). The handoff independently binds this Review to 7.2.1, and the release state at the candidate names 7.2.1 accepted-current. Earliest owner: §0.4, pending stakeholder restatement.

### N2 — floor creation: evaluation point, and a deferral that can never end

“Created once the reproduction and the first trial … both have admitted observations and no disposition stands” can be read as an event (evaluated when the second execution is admitted) or as a state (at any later position). Under the state reading, any transient loss of standing after the pair, such as an absorption with no rerun or W2, latches a human item. Separately, “S3 derives no rerun obligation whose pair would already fail condition 5”. For a candidate failure whose configuration is already nondeterministic in fact, no pair is ever scheduled, the deferral condition never becomes true, and the D1/D2 floor item is never created. The R3 adjudication obligation still exists, so the human is not wholly bypassed, but the floor's latch and inspector guarantee are missing on that path. Repair: state the event reading, and create the floor at once where S3 schedules no pair. Earliest owner: §6.6, §7.9.

### N3 — whole-tree fallback is forced by any incompleteness marker

§6.6 widens the execution basis to the whole governed tree “where no current completeness judgment bounds the closure, **or** an incompleteness marker is present”. That overrides even a qualified actor's `COMPLETENESS` judgment and complete harness-observed reads. Runtime configuration and data read by path are nearly universal in scientific code, so the whole-tree basis becomes the norm. Passing currency now reads the same basis (§10), so every admitted change anywhere stales every passing realization of such specifications, and assessor-read ones need a new judgment. §26 lists this cost as a reopen trigger, so it is not a blocker. But the predicate removes the two cheapest bounding routes, and §6.8 step 8 (“affected evidence rerun”) then requires every integration to carry them. Also, §10 dropped “data identity” from the execution part, and `on` is undefined for reads outside the governed tree (unpinned external data, ignored or untracked paths), which §11.4's “immutable pins” covers only for supported projects. Earliest owner: §6.6, §10; Manual item 11.

### N4 — a disposed earlier disagreement permanently forbids reading pairs on that content

Condition 5's third bullet is existence-keyed: “no admitted failing assessment of an execution of it on the trial's executed content, under the trial's reading, exists”. An earlier interpretive failure of admitted content that the owner has already disposed of (dismissed by an upheld challenge, or `IMMATERIALITY`) still exists. Every later candidate failure under a tightened reading on that content therefore goes to the owner. This is restrictive and rare, but §26 does not list it. Earliest owner: §6.6, §26.

### N5 — a reading pair can retire an interpretive concern raised under an editorially varied reading

A reading pair waives condition 2 for any never-admitted claim or specification revision, including a purely editorial one. For an assessor-read oracle the only guard is one assessor's dual reading (§27.34: “One honest reading of one outcome cannot give FAIL and PASS under editorially equal readings”). That is owner-conformant: `a-` applied a reading not in force, so it is not admissible against the admitted claim. But a reviewer's material concern about admitted content, voiced under an editorially varied claim in a frame, is retired at R2 for D1/D2, and no record carries the concern under the admitted reading. State it as a residual (§26), or require the dual-reading record to name the material difference between the readings. Earliest owner: §6.6 decision class.

### N6 — attribution of resubmitted never-lost bytes

The Dispatcher resubmits refused bytes “under the re-issued task's envelope with the refusal named as their provenance”. The text does not say whose actor and lineage class the record then carries. That matters for “`a-`'s own assessor” (own reassessment) and for independence checks on any later disposition. Repair: keep the original actor, and treat the envelope as transport. Earliest owner: §6.8 step 3; Manual.

## 3. Re-verification of previous Reviews' findings

“Closed” means the named deductive trajectory is excluded by the candidate's contract, not executed qualification or acceptance.

### BA7F738

| Finding | Disposition | Basis |
|---|---|---|
| U1a candidate failure from un-premised content | **Closed** | Executed content (§6.6, §10); rerun trigger; base trial; R2 or mechanical. Model discriminators |
| U1b unrelated candidate run withdraws a pair | **Closed** | Condition 5 and the latch read observations on either side's executed content only |
| U1c starvation | **Closed** | Run enumeration by tree; other trees never delay |
| U2a tightened tolerance, test-first | **Closed on its trajectory** | Reading pair. Residual members W1 (once-admitted reading) and W2 (mechanical standing) |
| U2b claim revised or added in an existing unit | **Closed on its trajectory** | Reading pair (assessor-read). Residual W1 for a restored earlier claim; N5 |
| N1 | **Partly closed** | Unchanged |
| N2 byte identity; `here` permissive | **Partly closed** | Assessor-read: identity, with the own-assessment route. Mechanical: verdict under `a-`'s reading, which causes W2 for reading pairs |
| N3 second R2 exception | **Closed** | Trial on `a-`'s base required. Residual: the “never admitted” content test (W1) |
| N4 unrecorded custody and deadline facts | **Partly closed** | Enumeration in the pair record; `INCOMPLETE` ends executions. New gap N2 |
| N5 discretionary resubmission | **Closed** | R0 resubmission. Attribution N6 |
| N6 “admitted” | **Closed** as a definition | Its “at some position” choice causes W1 |
| N7 residual cost | **Closed** | §26 lists both |

### Earlier Reviews

The `ba7f738..947370d` diff touches only the workplan (§0, §0.1, §6.2 tail, §6.6, §6.8 step 3, §7.9, §10, §21 item, §22, §26, §27.34-§27.35, §28), three lines of the authority index, the model check and three qualification records. The added records are the revision-19 handoff, the continuation handoff and the `ba7f738` Review. No earlier Review record was edited. No `source/`, `dist/`, `orchestrator/`, test, release-state, PEM, stakeholder-record or archived-predecessor path changed. This was verified by `git diff --stat`, hunk positions and blob identities at both commits.

- **4EC0024.**
  - B′1: **closed** for ordinary pairs (condition 2). The reading-pair branch relies on condition 3's single dual reading (N5).
  - B′2: **closed** (condition 5, enumeration, latch).
  - C1: **closed** for ordinary pairs; **reopened** for mechanical reading pairs (W2).
  - C2a, C2c: **closed**.
  - C2b: **closed**, except W1.
  - N1-N8: as recorded at `ba7f738`, with N8 now closed.
- **6FE1000.** A1-A3: **closed**. A2 holds through the reading pair's trial under the admitted reading. B1, B2: **closed**.
- **A414588 A1-A3 and B, 203A42B A and B, 62C0B24 A, 644EB72 A and B, 4C35D92 A, 97E753F A, B1 and B2, 124B0B7 A, FFBAD17 A, FB3E542 A: closed.**
  - `home`, the anchor sets, authorship fail-closed, `qual` over retired obligations, `IMMATERIALITY` currency and `bind(j)` are unchanged.
  - All 64 discriminators hold to depth 5.
  - FB3E542 B: **partly closed**, through W.
- **Strata.**
  - `on`, `here` (including the reading-pair exception), the reading-pair predicate and the “admitted at some position” fold are S0. They read admitted records, the trees they name and the effective-structure history.
  - `eff` keeps its shape; S2 stays monotone with a unique least fixed point; S1 is unchanged.
  - The strata stay well-founded and single-valued. The floor's event/state ambiguity (N2) is S3 and does not affect single-valuedness of `D_n`.
- **“Impossible” claims.**
  - “No run on either side can be hidden from conditions 1 and 5” holds for the latch: a later-observed run on the same executed content withdraws.
  - “a busy specification cannot starve one” holds.
  - “never lapses through mere change” is false for mechanical reading pairs (W2).
  - “the pair fails to form only where the admitted content, under the admitted reading, yields the same failure” is false (W1).

The remaining 730490D, AC71FA9, F3608F5, 8A75346, 441CF5C and F9D9DE8 closures do not depend on the changed text and remain **closed**. FFBAD17 N7 (inherited index and whitespace residue) remains outside this scope.

## 4. Out-of-matrix trajectories attempted

| Attempt | Result |
|---|---|
| Candidate failure from a runtime parameter file; returned, fixed, abandoned | Holds: base trial pair, R2 or mechanical |
| Unrelated candidate run differing only in un-named content after a pair | Holds: on neither side |
| Same executed content, different tree, run not enumerated, admitted after the pair with another outcome | Pair withdrawn later; correct (nondeterminism in fact) |
| Test-first tightened tolerance, abandoned (assessor-read) | Holds: reading pair; standing by outcome identity |
| Same with a mechanical oracle, then an unrelated output-shifting change | **Fails** (W2) |
| Once-admitted, later relaxed reading restored by a candidate and failed | **Fails** (W1); reproduced in the model |
| Candidate reverts a fix to an earlier admitted code revision and fails | Pair forms; R3 instead of R2 (W1, decision-class exception) |
| Editorial claim edit in a frame, failure from admitted code (`6fe1000` A2) | Holds: the admitted reading fails the trial |
| Editorial claim edit carrying a reviewer's interpretive concern about admitted content | Retired at R2 by one dual reading; owner-conformant (N5) |
| Interpretive failure, comment-only code change (`4ec0024` B′1) | Holds: condition 2 |
| Earlier owner-disposed failure of admitted content, then a tightened-reading candidate | No reading pair ever (N4); restrictive |
| Candidate failure whose configuration is already nondeterministic in fact | No pair scheduled; floor never created (N2) |
| Absorption after a pair, before any rerun on the new content | Transient `P`; latched floor under the state reading (N2) |
| Whole-tree basis with a qualified completeness judgment and a runtime-config marker | Whole tree anyway; every change stales passing evidence (N3) |
| Read of an absent optional file later added inside a widened scope | Holds: scope membership is recorded |
| External dataset read by path, unpinned, changed in place | `on` undefined (N3) |
| Re-issued task after refused never-lost bytes | Resubmitted at R0; attribution unstated (N6) |
| Pair, then a loss boundary | Holds: `cont` withholds the disposition |
| Non-independent superseder; unauthorized `supersedes` | Holds: rejected at step 3 |
| Workflow layer, publication, frame enactment, intake, migration and recovery trajectories of earlier records | Hold as recorded; that text is untouched by revision 20 |

## 5. Family-level convergence assessment (mid-review instruction), minimum architecture and capability transfer

**(1) Post-simplification recurrence.** Yes. The assessment-disagreement family has been re-derived in every revision since 10:

| Revisions | Approach | Outcome |
|---|---|---|
| 10-16 | Mechanical lapse on progressively refined content notions | Each defeated in the permissive direction (§6.6 lists them) |
| 17 | Declared simplification: removed every lapse (“Revision 17 therefore removes the lapse instead of refining it”) | Defeated |
| 18 | Count from admission; pair supersession | Defeated |
| 19 | Start latch, five pair conditions, withdrawal latch, `here` | Defeated |
| 20 | `on`, reading pairs, run enumeration, `INCOMPLETE` deferral | Defeated (this record) |

Each post-simplification revision repaired the previous Review's members additively, and each new defect lies where two of the previous cycle's repairs meet:

- `6fe1000` → `4ec0024`: counting from admission × candidate frames;
- `4ec0024` → `ba7f738`: premise identity × the pair;
- `ba7f738` → here: the N6 definition × the reading pair (W1); the N2 mechanical clause × the reading pair (W2).

That is the convergence owner's “patch-on-patch repair” and “special cases accumulating around one owner”, after a simplification: “post-simplification recurrence … -> bounded reconsideration of the earliest affected abstraction”. The owner's caveat (“A clean local repair that genuinely closes the cause remains sufficient”) does not apply. The two local fixes in W are clean for their members, but nothing in this cycle's evidence suggests they close the cause, which is the number of independently defined sub-predicates that must agree about what a failure is about.

**The earliest affected abstraction** is the decision, made in revision 18 and kept since, to represent “this failing observation does not stand here” as an admitted **supersession record** whose admission is gated by a five-condition pair, and whose standing `here` then re-derives in every frame from the admitted observations anyway. Around it sit compensating mechanisms:

- a start rule (obligation identity) that deliberately over-counts;
- a stop rule (the pair) that must cover the over-count;
- a reading pair for the reading dimension;
- a withdrawal latch for late observations;
- run enumeration so that formation does not race them;
- decision-class exceptions for the pair cases;
- a floor deferral that waits for the pair.

**(2) Minimum justified concretization.** The candidate is not shown to be the minimum. A materially simpler concretization is evident in outline. It is offered as a hypothesis for the owner's bounded reconsideration, not as a verified design; this Review shares the author's model family, so it carries the same common-mode risk. The candidate already concedes the key step: standing in every frame is decided by admitted observations on that frame's executed content (`here`), not by the pair record. The outline makes that per-frame S0 test the disposition itself, and keeps judgments for what observations cannot settle.

| Could be removed or merged | Replaced by | Owner-required property the removal must preserve |
|---|---|---|
| Pair as a supersession record; conditions 1, 2, 4, 5 checked at Admission; the withdrawal latch | One S0 per-frame applicability test of each failing assessment: it does not count in `G` while an admitted, `cont`-held observation of its configuration on `G`'s executed content differs from `a-`'s outcome on the failing outputs, none reproduces it, `a-` has been reproduced on its own executed content, and no observation on that content differs (nondeterminism in fact keeps it counting) | “obtain discriminating evidence”: identical outcomes never discriminate (`6fe1000` B1, `4ec0024` B′1); nondeterminism goes to the owner (`6fe1000` B2, B′2); a revert re-counts (C1 contrast); loss boundaries withhold permissive effects (P2, P4); the inspector shows which observation discriminates (“distinguish resolved reassessment from still-live disagreement”) |
| Run enumeration as a formation guard | Never-lost designated-runner observations, which S0 re-reads whenever they arrive | “Do not suppress contradictory admissible observations”: every designated-runner execution still ends in an admitted observation |
| Condition 3's separate pair assessment for outcome-flip cases | The ordinary passing assessment of the new realization that `ev` already needs | A differing outcome that still fails is never confirmation (stale/other-outcome passing evidence never confirms); the lenient-assessor residual is the same as the candidate's assessor-read `here` today |
| Start latch on obligation identity, two anchor sets used for start, reading pair, “admitted at any position” | One reading test: a failure counts outside its lineage where its reading was in force in the admitted state at its base, or is in force in `G`. Where neither holds, it counts in the admitted state only until one execution on `G`'s content is read under `G`'s reading in a single dual-reading record (condition 3's form kept for this case) | `6fe1000` A2 (an editorial reading change cannot hide an admitted-code failure); `4c35d92` (an admitted reading change raises reassessment, never lapse); `4ec0024` C2a-C2c; W1 |
| The two decision-class pair exceptions; floor deferral keyed on a scheduled pair | Floor created when a D1/D2 failure counts in the admitted state with an admitted observation on admitted content reproducing it, or at once for a failure of admitted content | SD-2 and A8: a material D1/D2 disagreement reaches the human and latches; nothing is lowered below the floor |
| Kept unchanged | — | No mechanical lapse on content or structure presence (revision 17), `home` never shed, `qual` over retired obligations, owner dispositions (own reassessment, adjudication, `IMMATERIALITY` at currency), independence and authorship fail-closed, S2 monotonicity |

Whether this outline survives the trajectories that defeated revisions 10-19 is exactly what the bounded reconsideration must test. The table names the trajectories it must hold. It adds no primitive, record kind or component, and it removes several sub-predicates. If the owner finds it inequivalent, the reason belongs in §27 as the recorded justification for the pair abstraction.

**(3) Common-mode causes across the prior Reviews and revisions.**

1. **Repair directions adopted near-verbatim from same-family Reviews.** `4ec0024` proposed the start latch and condition (i); `ba7f738` proposed “one content notion”, extending the exception “to every never-admitted interpretive premise”, defining “admitted” once, and the mechanical-oracle reading of “reproduces”. Revision 20 adopted these. W1 sits in the “never-admitted” wording combined with the requested single definition; W2 sits in the N2 suggestion. Reviewer and author share framing, so a Review's proposed repair inherits its own blind spot.
2. **Handoff and Review framing biased toward additive repair.** Handoffs list the previous repairs as the scope, and Reviews end with “narrow rule changes, not new mechanisms” and “don't redesign”. Both steer toward patching members, against the convergence owner's mandatory simplification once recurrence is evident. This record's own handoff had the same framing until the mid-review instruction.
3. **A qualification instrument that transcribes the rule under test.** The model's oracle and its new properties reuse the candidate's predicates (P13's `discriminates` uses the same “never admitted” test; outcomes are compared by identity only, with no mechanical verdict function). Its sensitivity modes show that older rules fail, never that the current rule meets the owner. Green results therefore coexist with W (PEM DS-001).
4. **Verification on motivating trajectories.** §22 and §27 add the last Review's trajectories and their contrasts. Interactions between the new clauses are not enumerated.
5. **Many cross-cutting exceptions stated in several places** (§0.1, §6.6, §7.9, §10, §22, §26, §27). The defects arise in their pairwise interactions.
6. **Shared model family, corpus and toolchain** between author and every Review since revision 11 (SD-8), and a scratchpad shared with the authoring session (§9).

**Minimality otherwise.** Revision 20 adds no primitive, record kind, store or component (§27.35). It removes the named premises, the never-admitted-specification exception, the outstanding-envelope guard and the floor deadline. It adds `on`, the reading pair, run enumeration, `INCOMPLETE` deferral and R0 resubmission. In the family's surface it is not a net simplification (above). The rest of the architecture is untouched and its minimality assessments by earlier Reviews stand.

**Predecessor comparison.** Revision 20 did not touch §16.2 or §18. Blobs verified at the candidate and equal at `ba7f738`:

| Predecessor | Blob |
|---|---|
| befe678 hypothesis archive | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |
| Consolidated Protocol 8 plan archive | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| Orchestrator Architecture 1.6.0 (equal at public source and candidate) | `39e6de727f6c35402962509d30d947962992eaad` |

The bounded semantic comparison of §16.2 and §18 recorded by earlier Reviews still holds by identity.

**PEM basis and HAS.** Project instructions designate `main` as the integrated publication line. `git ls-remote origin refs/heads/main` gives `af0455753e20ee54a969c844872e29e270007211`, equal to the workplan's basis. Its `PROJECT-ENGINEERING-MEMORY.md` blob equals the candidate's, `1561797125622f355f84eb27319f87e8fa4227d9`. There is no branch overlay. Missing coverage proves no absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: The model is green in all 64 discriminators and at depth 5 while W holds. Its P13 "owner's sense" reuses the candidate's never-admitted predicate (so W1 is excluded from P13's premise; reproduced by probe), and it has no mechanical verdict function (W2 unrepresentable). §22 has no case for a once-admitted reading restored by a candidate, or for a mechanical reading pair after an output-shifting change.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen profiles are required through the versioning owner; preserved by §24; unchanged by revision 20.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy. Repair at the owning D3 rule family (§6.6) and regenerate §0.1, §22, §27 and the model from it.
  - id: SP-002
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: Self-reference-safe identity unchanged by revision 20.
  - id: FF-001
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: No immutable publication in scope; it remains applicable to later genesis and release.
```

**7.2.1 reconciliation.** The release state at the candidate names 7.2.1 accepted-current, with public source `aaeaf8b6…` and recovery `efdd1b59…`, matching the handoff; `source/PROTOCOL_VERSION` is 7.2.1 at both the public source and the candidate. The diff changes no §0.4, §19 or §24 text, and no `source/`, `dist/`, `orchestrator/`, release-state or PEM path. The §0.4 obligation table and the §19 landing points therefore stand. The inherited evidence doctrine is not yet realized at W.

## 6. Qualification-program adequacy

§22's disagreement group now carries the `ba7f738` U1 and U2 cases with contrasts, and the floor and class group. It cannot discriminate W:

- every reading case uses a reading that was never admitted; none restores a once-admitted reading;
- the standing cases after a reading pair use “an execution-basis change … rerun with the same outcome”, never a changed outcome that passes the admitted reading and fails `a-`'s.

The [testing owner][testing] asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Revision 20 as written is such a concretization for W.

The model check's sensitivity is real but self-referential:

- `REV19=1` fails only P13 and P14. Both properties were added for revision 20 and encode its rule: P13's `discriminates` contains the same `unadmitted` test as the candidate, and P14's premise is the U1b trajectory. They therefore detect the old rule's distance from the new rule, not from the owner.
- The earlier modes fail long-standing owner-grounded properties (P9, P10, P12, Q2), so their sensitivity stands.

The model has no mechanical/assessor split, no verdict function and no reading that can be restored, so W is outside it.

Add the discriminators named in §1. State P13's “owner's sense” from the owner's applicability dimensions: the failing reading is not the reading in force at the trial's content. Give the model, or a separate bounded check, a mechanical verdict function and a restorable reading.

The four consolidation tests establish frontmatter and routing only. HARD-template thresholds, mutation strength, evaluator calibration, custody, blinding, paired baselines and doctrine-realization measurement remain later-gate obligations (§22-§25). No campaign was run and no improvement estimate is asserted.

## 7. What was verified and how

- **Candidate identity.** Resolved the candidate SHA and the workplan blob `40267d35…`. Extracted a `git archive` of the exact candidate into a scratch directory under a distinct name. Later commits, including the handoff commit `8bab01c`, were excluded.
- **Governing source.** The checkout is shallow and lacked the governing commits. `aaeaf8b6…`, `efdd1b59…` and `af045575…` were fetched by SHA with `git fetch --depth=1` into the object store only; no ref or working file changed.
- **Owners read** at `aaeaf8b6` with `git show`:
  - the D3 role entrypoint (`software-design/SKILL.md`: routing, D3 design contract, Independent Review and Challenge, Completion);
  - architecture, read first in full;
  - evidence, in full;
  - convergence, in full, including “Active simplification trigger” and “Review strategy after recurrence” (mid-review instruction);
  - workflow (Optional independent cognitive trajectories);
  - testing (smallest plausible wrong concretization);
  - the kernel's Challenge text;
  - PEM entries by identifier.

  Release identities were resolved from `PROTOCOL-RELEASE-STATE.yaml` at the candidate.
- **Candidate read.**
  - In full: §0-§0.1, §6.1-§6.8, §7.5, §7.9, §10, §11.4, §22's disagreement group and model-check item, §26, §27.34-§27.35 and §28.
  - The `ba7f738..947370d` diff hunk list; the authority-index diff; the stakeholder record; the model-check source in full.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the archive (stale bytecode removed first): **4 passed, 0 failures**, Python **3.13.16**.
- **Whitespace.** `git diff --check ba7f7380… 947370d3…`: **exit 0**, no diagnostics.
- **Model check**, depth 4, 814,450 transitions in every mode:

  | Mode | Failures | By property | Discriminators differing | Exit |
  |---|---|---|---|---|
  | default `REV20` | 0 | — | 0 (64/64 as expected) | 0 |
  | `REV19=1` | 1,845 | P13 1,825, P14 20, O 0 | 10 | 1 |
  | `REV18=1` | 4,640 | P10 869, P11 12, P12 1,890, P13 1,757, Q2 112, O 0 | 15 | 1 |
  | `REV17=1` | 103,453 | P9 16,595, P10 54,579, P11 72, P12 3,958, P13 6, Q2 28,243, O 0 | 19 | 1 |
  | `REV16=1` | 111,169 | P7 366, P9 16,553, P10 54,477, P12 3,994, P13 6, Q 3,192, Q2 28,243, O 4,338 | 22 | 1 |
  | `REV14=1` | 119,527 | P7 720, P8 768, P9 16,511, P10 54,345, P12 4,030, P13 6, Q 6,312, Q2 28,243, O 8,592 | 23 | 1 |
  | `REV13=1` | 218,397 | P7 9,486, P9 15,125, P10 50,904, P12 3,729, P13 6, Q 41,208, Q2 28,243, O 69,696 | 25 | 1 |
  | `REV12=1` | 223,261 | P5 239, P7 9,486, P9 15,109, P10 50,842, P12 3,745, P13 6, Q 43,439, Q2 28,243, O 72,152 | 29 | 1 |
  | `REV11=1` | 225,355 | P7 9,486, P9 15,263, P10 51,350, P11 84, P12 3,503, P13 6, Q 42,174, Q2 28,243, O 75,246 | 32 | 1 |
  | `REV10=1` | 225,673 | P1 1,974, P7 9,486, P9 15,137, P10 50,938, P11 84, P12 3,717, P13 6, Q 39,438, Q2 28,243, O 76,650 | 30 | 1 |

  Every mode fails properties other than the oracle; for `REV19` those are only P13 and P14 (§6).
- **Model check**, depth 5, default mode: DEPTH5_RESULT.
- **W1 probe.** The candidate's own `Ledger`, `discriminates` and `oracle_unqualified`, imported unmodified from the archive:
  - `(ORACLE tight, ORACLE, PASS, FAIL tight, PAIR(ro=1, to=1), PASS)`: pair `authorized = False`, P13's `discriminates = False`, `V = P`, oracle not unqualified;
  - the same with the first record a plain `ORACLE` (reading never admitted): `authorized = True`, `discriminates = True`, `V = T`.
- **W2, N2-N6.** Deductive, from the quoted contract text; W2 is not representable in the model.
- **Identities.** Verified the predecessor blobs, the release-state identities, the PEM blob at the candidate and at `af04557`, the stakeholder-record blob, the test blob, and the changed-path list, at both `ba7f738` and the candidate.
- **Repository untouched.** No candidate, source, distribution, index, release state, PEM or frozen resource was changed. The only repository output is this record. Nothing was committed or pushed.

**Scientific inquiry envelope.** Examined architecture-mediated evidence applicability, readings, executed content, pairs, standing, withdrawal, decision classes and escalation. Materiality here is the ability to change support, closure, human routing or the next authorized action. No physical or numerical result is asserted; the numerical values in W2 are illustrative. One pinned candidate was reviewed through multiple deductive trajectories and one model probe. No variant search over scientific analyses was performed and no delegates were launched. The judgment relies on accepted engineering, evidence, workflow and convergence doctrine, not on project D1/D2 authority, so the tension-search duty was not triggered.

## 8. What could not be verified

- **PEM schema validation** was not rerun. The checkout is a shallow clone, and the PEM blob is unchanged since earlier Reviews. This is not a pass.
- **Remote state** was read once by `git ls-remote`. No further remote-state claim is made.
- **Readings and Manual compositions.**
  - W1 assumes a specification or claim revision identity is byte-identical on restoration (a whole-unit restore). A restore that differs elsewhere in the unit is a new revision and does form a reading pair.
  - W2's floor consequence depends on the state reading of the floor's deferral clause (N2). The qualification and the need for a new pair do not.
  - W2's step-8 consequence depends on how step 8 treats a provisional `ev` caused by the request's own content change; it is stated as possible, not certain.
- **The §5 outline** is a hypothesis. Its equivalence to the candidate on the trajectories that defeated revisions 10-19 was not verified. That is the owner's bounded reconsideration.
- **Runtime evidence.** No SSDS production owner, witness deployment, harness adapter or Architecture Manual exists. Runtime fidelity, read recording per harness, failure injection, lineage attestation, privacy enforcement, scaling and burden reduction remain unexecuted (§21-§26), and none is counted as a pass.
- **Repository acceptance.** The full repository regression, package build and validation, distribution parity, frozen-resource census and Core snapshot tests were not rerun. This Review changes no protocol source or descendants.

## 9. Common-mode dependency

This reviewer is a fresh-context sub-agent **of the same model family as the author** (Claude), launched by the authoring session from a handoff the author wrote, under stakeholder SD-8. The author also relayed the mid-review instruction. That is a material common-mode dependency: shared blind spots, framing inherited from the handoff's scope list, and the same corpus and toolchain are all plausible. The [workflow owner][workflow] says: “Separate context improves process independence but not epistemic independence when agents share model, source corpus, toolchain or oracle”.

This cycle shows the dependency concretely again (§5, item 3, cause 1). Both members of W sit in wording that the previous same-family Review proposed and the author adopted. The §5 outline and the repair directions in this record carry the same risk.

The scratchpad directory provided to this sub-agent is shared with the authoring session. This reviewer read none of the author's files there and wrote its own outputs under distinct names.

The handoff gave no author conclusions. This record supplies **no different-family corroboration**. The design's own §9.6 lets policy require it for high-consequence surfaces, and the stakeholder has waived it for this cycle. A PASS from this cycle would still need owner adjudication and the production evidence of later gates ([workflow, Optional independent cognitive trajectories][workflow]).

## 10. D4 statement

**D4 remains NOT AUTHORIZED.** Phase B Review is NO-PASS. The next step is the owning D3 step that the convergence owner requires:

- a bounded reconsideration of the §6.6 assessment-disagreement family at its earliest affected abstraction, the pair-as-supersession disposition and its compensating start, reading, withdrawal, custody, class and floor clauses (§5), which must at least close W1 and W2;
- then regeneration of §0.1, §22, §27 and the model check from the result, with an owner-stated P13;
- then a frozen replacement immutable candidate.

Even a later Phase B PASS authorizes nothing by itself:

- G1 needs the accepted Manual and explicit stakeholder acceptance of the major change.
- G2 needs a separately reviewed shadow workplan and stakeholder authorization.
- G3 needs real-owner implementation evidence.
- G4 adds per-subject cutover, quiescence and rollback (§23-§25).

This Review grants no Manual acceptance, implementation permission, spend release, cutover, ratification or promotion.

[wp]: https://github.com/hjin98/scientific-software-development-system/blob/947370d31fbd7bc53272bdbc401244624137c855/workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
[kernel]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md
[evidence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/evidence-evolution-and-dependencies.md
[workflow]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md
[testing]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md
[convergence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md
