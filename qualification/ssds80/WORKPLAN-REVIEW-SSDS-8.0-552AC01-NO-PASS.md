# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 22

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 552ac01bb799c22dece5a33d93bd4244bea21d2a
    SCOPE: whole proposed architecture; (a) the revision-22 repair after the ef8445a Review: the discriminating
           reading for assessor-read failures (§6.6), its refusal rule, coverage limits, class rule and reading
           obligation; removal of the reading-ground IMMATERIALITY; standing of completeness judgments that bound
           an observation's basis and the S2 read in `stale`; relaxations held only by absorption; the review-brief
           item for specification changes (§9.6); the assessor-read floor events (§6.6, §7.9); §7.4 and §10
           wording; stakeholder record item 7 and SD-9; the bounded model check (DUAL records, mode-independent
           owner-stated predicates, restated P10, narrowed P11, REV21); (b) workflow execution and verification
           layer and the doctrine-realization objective; (c) persistence, derivation, concurrency and migration;
           (d) Protocol 7.2.1 inheritance reconciliation; plus the family-level convergence assessment
           (method step 5)
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: 8970b617b377756523db1ad783d0863383949fa2 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5,
           AC71FA9, 730490D, FB3E542, 124B0B7, 97E753F, 4C35D92, 644EB72, 62C0B24,
           203A42B, A414588, 6FE1000, 4EC0024, BA7F738, 947370D, EF8445A; all NO-PASS
    REVIEW METHOD: immutable-owner reconstruction in the D3 role; the repair attacked as a new mechanism and
           against every earlier closure it touches, with emphasis on how long its stop stands; prior-finding
           re-derivation; family-level convergence assessment; exact-candidate structural tests, whitespace
           check, the bounded model check in every requested mode, and a bounded probe of the model on the
           trajectories found here
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session from
           REVIEW-HANDOFF-SSDS-8.0-REVISION-22.md (stakeholder SD-8); same model family as the author
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-552AC01-NO-PASS.md

Candidate section references below mean the [primary workplan at the candidate][wp]. Governing-owner links pin the public source above. This context authored neither the candidate nor any prior Review, received none of the authoring conversation, and treated the handoff's scope description, the workplan's self-assessments (§0.1, §27.38-§27.39), the model check's green result and every prior verdict as hypotheses.

The blocker below is a deduction from the proposed contracts, not an observed SSDS runtime failure. Its trajectory is reproduced in the candidate's own bounded model, which returns the restrictive value on it, and which states that value as an expected named discriminator (§1, §6). Its asserter is the reviewer named above; its disposition is **OPEN** against the exact candidate. This record is its canonical home. Revisit after the D3 owner has repaired the coverage and the class rule of the discriminating reading at §6.6, regenerated §7.9, §0.1, §22, §26, §27 and the model check from the result, and frozen a replacement candidate. No accepted project scientific D1/D2 claim is challenged.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The [kernel][kernel] says: “A coherent parent with a wrong child is an ordinary blocker.” The governing [evidence owner][evidence] is coherent and realizable for this concern:

- “A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority. A stale passing observation is not admissible confirmation.”
- “Use `review-required` when applicability is uncertain.”
- “Evidence only establishes claims its oracle and exercised semantic owner can discriminate.”
- “When competent evidence assessments materially conflict, preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence. … When a durable representation stores multiple assessments, supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement. An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.”

The [convergence owner][convergence] is coherent too: “Add machinery only when a required capability genuinely remains absent or one canonical mechanism replaces broader existing complexity”, and “A clean local repair that genuinely closes the cause remains sufficient; recurrence does not automatically force redesign.” The blocker lies in the proposed D3 candidate. It is therefore an ordinary blocker.

The stakeholder record (blob `c02bbeb9…`) now holds item 7 verbatim: “Read the protocol version 7.2.1 and use the software-design role for your revision and reviews. You should be aware of convergence and the active simplification rule when issues don't converge or exposes repeatedly.” SD-9 restates it faithfully; “under the governing 7.2.1 owners” slightly extends “read the protocol version 7.2.1”, which §0.4 already makes governing. Nothing in the candidate claims that a sub-agent PASS accepts the architecture (§25).

## Verdict

**NO-PASS.** Revision 22 closes `ef8445a` X on its three trajectories, but one blocker remains, **Y**: the discriminating reading covers an outcome only on the content it was made on, and its class rule escalates every later reading to R3 for D1/D2. A stop that the reading earned therefore lapses at every later change of the execution basis, **even when the rerun's evaluated outcome is byte-identical to the one the reading passed under the same reading**. The failure then counts again, the claim is labelled `disputed`, a new reading is owed and, for D1/D2, a floor item opens and only an authenticated human can read it again. This is `4ec0024` C1, a closed blocker, reopened for assessor-read oracles.

- **Y1 — a settled assessor-read failure resurrects on a change that alters nothing the oracle reads.** An equivalence-covered, comment-only change to a file in the execution basis (with whole-tree fallback, any admitted change) is followed by the ordinary rerun, whose outcome is identical. The earlier reading no longer covers it, so (4) fails, the failure counts, and the claim goes from `T` to `P`. In the candidate's model the same ledger moves from `T` to `P`, and the model lists this as an expected value.
- **Y2 — for D1/D2 every later reading is R3 and opens a floor item.** The class rule's R2 exception requires the reading's passing observation to be “on `a-`'s base”. After any later admitted change it never is, so every re-reading “needs an R3 reading”, which is also a floor event. Failing assessments never retire in the admitted state (the start latch), so each historical assessor-read candidate failure on the obligation needs an authenticated human at each change of its basis. That is the accumulation `4ec0024` C1 described: “Failing assessments therefore accumulate without end and resurrect at each change.”

The cause is single: coverage and class are keyed on content identity, a proxy, instead of on what the oracle reads. The candidate's own refusal rule states the principle that settles the identical case (“one outcome cannot be read both ways under one reading”). The repair is subtractive (§1).

Revision 22 otherwise holds. X1, X2 and X3 are closed for honest readers; the lenient but formally consistent reader is a disclosed E3 residual. `ef8445a` N2 and N5 are closed; N1 and N3 are closed in part; N4 is not changed in substance, although §0.1 says it is repaired (N5 below). The mechanical branch of `stale_G` is unchanged and survived every trajectory attempted here (§4).

This is the thirteenth consecutive NO-PASS on the §6.6 disagreement family. The defect again sits where two repairs meet: the X repair and the `4ec0024` C1 closure. Both elements of it were in the previous same-family Review's repair direction (§9).

Requested checks:

- The four routing tests pass, and `git diff --check` is clean.
- The model check is green at depth 4 (1,574,464 transitions, 77/77 discriminators) and at depth 5 (D5_RESULT).
- Every sensitivity mode is red on properties other than the oracle, with totals matching §27.38. `REV21=1` is red on P7 and Q, measured against an `owner_stale` that now transcribes revision 22's own assessor-read rule (§6).
- A bounded probe shows that the model returns `P` on Y1, where `REV21=1` returns `T`, and that `owner_stale` agrees with the candidate, because it duplicates the candidate's rule; P11, which would see it, was narrowed to mechanical failures.

None of these checks establishes semantic adequacy.

## 1. Blockers by earliest owner

### Y — the discriminating reading's stop lapses at every change of content, and re-escalates for D1/D2 (members Y1, Y2)

**Owner text at the candidate.**

- §6.6 `stale_G`, assessor-read clause of “yields”: “no standing discriminating reading of a- read o's outcome PASS under G's reading”.
- §6.6: “discriminating reading of a- in G (revision 22): one assessment, by a qualified assessor independent of the claim's authors, of an execution o with on(o, G), that records in one record PASS for o's outcome under G's reading and FAIL for a-'s reproduced outcome under a-'s reading … refused at Admission where the two readings are the same and the two outcomes identical (one outcome cannot be read both ways under one reading); it covers its outcome only while G's reading is the one it read under”.
- §27.38, attacks on the repair: “Reuse a reading after the content changes | It covers only observations on its own content”.
- §6.6 decision class: “A discriminating reading is an evidence assessment, R2. It is R3 where any such subject is, or has been, D1 or D2 authority, unless it shows the failure to be the candidate's own: its passing observation is on `a-`'s base and `a-`'s assessed content was not the admitted content at its base.”
- §6.6 Scheduling: “When `a-` counts in `G` with no disposition standing and is not stale there, S3 derives … one **reading obligation**”.
- §6.6 floor: “for an assessor-read oracle, its reading obligation is answered by a failing assessment of the admitted outcome …, or needs an R3 reading”; §7.9: “or whose reading needs R3 (assessor-read)”.
- §6.6 family rule: “standing: … a stop by discriminating observations holds in each frame exactly while that frame's observations show it”; and “**Standing per frame, without lapse by change.**”
- §22: “*Standing (`4ec0024` C1).* After a failure became stale, an unrelated edit of the evaluated code followed by the ordinary rerun of the configuration on the new content, not yielding it, leaves the claim unqualified, with no `disputed` label and no reproduction, assessment, adjudication or human item.”
- §0.1: “P11 applies to mechanical failures, whose stop needs no reading.”

**Y1 trajectory (every step locally compliant).** D3 subject `s` with claim `c`, evidenced by specification `σ` with an **assessor-read** oracle on a declared evaluated outcome (a convergence plot's data series). The admitted state's passing assessment `a+` is current.

1. Candidate `X` changes a runtime parameter file inside the execution basis. Reviewer `Y` assesses `X`'s outcome FAIL (`a-`). Its obligation is admitted, so `a-` counts in the admitted state at once.
2. S3 schedules the reproduction on `X`'s retained tree; it is identical, so (1) and (2) hold. The admitted state's evidence run on the base is standing, so (3) holds.
3. The scheduled reading obligation is discharged by an independent reviewer `Z`, who reads the admitted outcome `v0` PASS and the reproduction FAIL in one record: a discriminating reading, R2, admitted (the outcomes differ). (4) holds. `a-` is stale; `X` is abandoned; `ev(s, e) = T`. Everything so far is the §22 “X1 contrast”.
4. Later an admitted change edits only a comment in a module the execution reads, with an `EQUIVALENCE` judgment of class “editorial only”. `a+` stays current through it (§6.4, §6.7).
5. The configuration's rerun on the new admitted content returns an evaluated outcome **byte-identical** to `v0`, under the same reading.
6. `Z`'s reading is “of an execution o with on(o, G)”; `o` is not `on` the new content, so it is not a discriminating reading in the new admitted state. The new observation is covered by none, so it “yields” `a-`'s failure, (4) fails, and `a-` counts again. `undisputed(s, e) = P`, `ev(s, e) = P`, the evidence is labelled `disputed`, an adjudication obligation and a reading obligation open.

Nothing that the oracle reads changed between steps 3 and 6: the same outcome, under the same reading, was already read PASS by an independent reader in a standing record. The candidate's own refusal rule says that outcome cannot honestly be read otherwise. The resolved reassessment is nonetheless presented as a live disagreement.

**Y2 trajectory.** The same, with `s` a D2 subject.

1. Steps 1-3 hold at R2: `Z`'s passing observation is on `a-`'s base and `a-`'s assessed content was not the base's, so the failure is shown to be the candidate's own. No human item.
2. After step 5, any new discriminating reading's passing observation is on the new admitted content, not on `a-`'s base, so the class rule makes it **R3**. The floor event “needs an R3 reading” fires and the floor item latches. The claim stays `P` until an authenticated human records the reading.
3. At the next change of the execution basis the same happens again: the floor item is already latched, but a new R3 reading is owed and the claim is `P` meanwhile.
4. Every assessor-read candidate failure ever recorded on this obligation behaves the same way, because a failing assessment on an admitted obligation “counts in the admitted state at every later position whatever happens to the content, and never stops by machinery”, and staleness is re-read per frame. Where the execution basis falls back to the whole governed tree (§6.6, §26), every admitted change triggers all of them.

The X3 rationale for R3 (“A reading of later admitted content may carry a fix of a failure the base already had”) does not apply here. A standing R2 reading has already recorded that the base did not have `a-`'s failure.

**Bounded probe** (the candidate's model, unmodified). Each line gives `V`, `stale`, the model's own `owner_stale` and its oracle:

- `(PASS, FAIL(cand), EXEC(old, 1), DUAL(0))`: `T / True / True / unqualified` (the X1 contrast);
- the same, then `MOVE(equiv)`, `EXEC(0)` (Y1: identical outcome, no new assessment): `T` → **`P / False / False / qualified`**;
- the same with a non-equivalent `MOVE` and a fresh ordinary `PASS`: `P / False / False / qualified`;
- an admitted failure fixed and read (`PASS, FAIL, MOVE, EXEC(old, 1), DUAL(0)`), then `MOVE(equiv)`, `EXEC(0)`: `P`;
- under `REV21=1`, the Y1 ledger gives `T`;
- the model's own named discriminator “a discriminating reading does not cover a later change of content” is `(PASS, FAIL, MOVE, EXEC(old, 1), DUAL(0), MOVE, EXEC(0), PASS)` and **expects `P`**, with a rerun outcome identical to the one the reading passed.

Y is restrictive, so Q and P13 cannot flag it. P11 (“a disagreement resolved by a pair is not presented as live again”) would, but revision 22 restricted it to mechanical failures. `owner_stale` is a line-for-line duplicate of the candidate's assessor-read rule. The decision class and the floor are outside the model, so Y2 is invisible to it.

**What it violates.**

- The [evidence owner][evidence]: “supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement.” Y1 re-presents a recorded resolution as live with nothing it read changed. “Use `review-required` when applicability is uncertain”: nothing is uncertain here, by the candidate's own refusal rule.
- The candidate's own guarantees: §22 *Standing* (`4ec0024` C1) as written, for an assessor-read oracle; the §6.6 family rule's standing clause and “without lapse by change”; P11's stated purpose.
- The closed `4ec0024` blocker C1, reopened for assessor-read oracles: “At every later change of what the trial evaluated, a long-fixed failure becomes adverse again, the claim is labelled `disputed`, and a new pair and a new independent assessment are owed (R3, a human, for D1/D2). Failing assessments therefore accumulate without end and resurrect at each change.” Revision 21 had kept it closed for assessor-read outcomes by identity; revision 22 dropped that without carrying the capability.
- The stakeholder's SD-2 direction, “The human investigator then can interface cleanly and handle the important questions while letting the agents as well as the deterministic framework handle the rest”: Y2 sends settled candidate failures back to the human at every change.
- The [convergence owner][convergence]: “Add machinery only when a required capability genuinely remains absent”. Capability X needs a reading of each **new** outcome; it does not need content-bound coverage or the R3 re-escalation.

An implementer cannot satisfy §6.6 and §22 *Standing* together for an assessor-read oracle on these trajectories without choosing between them.

**Earliest owner.** D3 §6.6: the coverage clause of the discriminating reading and the class rule's R2 exception; then the §7.9 floor event, §22, §26, §27.38 and the model check. Not Manual: §6.6 fixes `on(o, G)` and “its passing observation is on `a-`'s base” explicitly, and §27.38 confirms the choice.

**Minimum repair direction.** Subtractive, inside the revision-22 abstraction:

- **Key coverage on what the oracle reads.** A standing discriminating reading of `a-` covers, in any frame, every observation whose evaluated outcome on the failing outputs is identical to the outcome it read PASS, while that frame's reading is the one it read under. This is the converse of the refusal rule. Drop `on(o, G)` from the reading's coverage; condition (3) still needs a standing observation of the frame's content.
- **Do not re-escalate a failure already shown to be the candidate's own.** Where a standing discriminating reading has shown `a-` to be the candidate's own (the R2 case), a later reading of a new outcome of `a-` is R2. R3 remains for failures of admitted content and for failures never shown to be the candidate's own. The floor's “needs an R3 reading” follows.
- **Disclose the remaining cost.** One R2 reading per genuinely new outcome per counted assessor-read failure is the price of X. Name it in §26 with a reopen trigger, restate §22 *Standing* for assessor-read oracles (identical outcome: no reading; new outcome: one reading, R2 where already shown candidate-own), restore P11 for assessor-read failures with identical outcomes, and state `owner_stale` from the owner instead of transcribing the candidate's rule.
- **Alternatively**, remove assessor-read staleness and route those failures to the owner's adjudication or a supersession, which stands on immutable facts (`ef8445a`'s alternative). §26 then carries the cost.

Either form removes mechanism. Neither restores the pair, the latch, `here`, the reading-ground judgment or the enumeration.

**Required discriminators**, through real Admission, Derivation, discharge and inspection consumers:

- **Y1.** A candidate assessor-read failure is shown candidate-own by an R2 reading; an equivalence-covered admitted change follows; the rerun's outcome is identical. The claim stays unqualified, with no reading obligation, label or human item. Contrast: a rerun outcome that differs needs one new reading.
- **Y2.** The same on a D2 subject with a differing outcome: one R2 reading, no floor item. Contrast: a later admitted outcome identical to `a-`'s failing outcome counts at once (a revert), with the floor events as today; a D2 failure of admitted content still needs R3.
- **In the model.** Replace the discriminator “a discriminating reading does not cover a later change of content” with an identical-outcome case expecting `T` and a perturbed-outcome case expecting `P`. Restore P11 for identical assessor-read outcomes. Add the materiality partition that `ef8445a` asked for, so that `owner_stale` is not a transcription of the rule it checks.

## 2. Non-blocking findings

### N1 — stakeholder-instruction provenance (ef8445a N1, partly closed)

The D3-role and convergence instruction is now verbatim (item 7, SD-9). The 2026-10-12 adoption instruction remains paraphrase-only (`f3608f5` N1; stakeholder record, “Not covered”). Earliest owner: §0.4, pending stakeholder restatement.

### N2 — `stale` now reads an S2 value, but the strata text and the support graph were not regenerated

The repair of `ef8445a` N2 is sound in its trajectory: a permissive use needs the bounding completeness judgment current, otherwise the whole tree. `stale` stays monotone in that value, so S2 keeps its unique least fixed point. Four residues remain:

- §6.6's S0 bullet still says `stale` “is a constant in S2”, and the Uniqueness paragraph still lists `stale` among the constants. The new paragraph says it reads an S2 value. An implementer who evaluates `stale` before S2 cannot read `current(J)`.
- The support-graph edge list (“Its edges come from three sources”) was not extended. A reproduction or a scheduled execution has no assessment naming `s`, so nothing orders its bounding judgment before `valid(s)`. “A one-pass topological evaluation therefore computes the least fixed point” is then unsupported. A legitimate cycle (the judgment's basis reaching `s`) evaluates to `F`, which fails closed, but is misreported as corrupted input (“Any other cycle … can arise only from corrupted input”).
- “Still current” does not say whether `P` suffices. If it does, a completeness judgment under a risk-overridden blocking challenge lets an observation make a failure stale, contrary to the standing clause's own rule that “a risk override never resolves a challenge”.
- The class rule's “on `a-`'s base” is checked from the recorded basis. A wrongly narrow basis can therefore admit an R2 reading where the whole tree would require R3, and the reading keeps its effect after the judgment is revoked.

Repair: regenerate the S0 bullet and Uniqueness from the new rule, add the edge, require `T`, and apply the basis rule to the class check. Earliest owner: §6.6.

### N3 — the absorption rule covers only mechanical verdicts (ef8445a N3, partly closed)

§0.1 states “A relaxation held only by absorption makes nothing stale” generally. §6.6 implements it only for the mechanical verdict (“the verdict is then also taken under the last revision an admission integrated”). A discriminating reading “covers its outcome only while G's reading is the one it read under”, and after an absorbed foreign relaxation `G`'s reading is the absorbed one. An R2 reading under it can therefore make an assessor-read failure (not D1/D2) stale before any admission integrates the relaxation. The §9.6 brief item likewise lists only mechanical failures. Intake and re-acceptance of the changed subject narrow the effect, as for the mechanical case. Repair: read the discriminating reading's reading against the last integrated revision as well. Earliest owner: §6.6, §9.6.

### N4 — the assessor-read floor dropped the case that needs no reading

Revision 21's floor fired at once where an admitted observation yields the failure under the admitted reading. For an assessor-read oracle with an identical outcome under the same reading, that is still decidable without a reader: no discriminating reading can be admitted (it would be refused), so the failure is provably one of admitted behaviour. Revision 22 replaces the event for assessor-read oracles by “its reading obligation is answered by a failing assessment …, or needs an R3 reading”. A D1/D2 candidate failure whose outcome equals the admitted one therefore waits for an R2 reader before reaching the human. The reading obligation also demands “either a discriminating reading or a failing assessment of `G`'s outcome”. A competent reviewer who disagrees with `a-` over that one outcome can record neither, although §6.6 routes that case to the owner. The claim stays `P`, so this is restrictive. Repair: keep the identity event for an identical outcome under the same reading, and route that reading obligation to the owner's adjudication. Earliest owner: §6.6 floor and Scheduling, §7.9.

### N5 — ef8445a N4 is not changed in substance, although §0.1 says it is repaired

§0.1 says N4 is repaired by “The discriminating reading's class rule (R3 unless the failure is the candidate's own)”. The R2 exception tests “`a-`'s assessed content was not the admitted content at its base”, and assessed content includes the reading. Any byte change to the claim unit in the frame satisfies it. A D1/D2 concern about admitted behaviour, voiced in a frame that touched the claim text editorially, is retired by one R2 reading with no floor item, exactly as by revision 21's reading-ground judgment. The removed judgment also had to name the material difference between the readings; §6.6's discriminating reading does not, although §22's U2 case still says “naming the material difference”. §22's “Contrasts kept” still says “An editorial claim or specification edit while the failure comes from admitted code: never stale”; under revision 22 that holds only for an honest reader, not by mechanism. The disclosure in §26 is adequate for a residual. Correct §0.1 and §27.38, and either require the named difference or keep R3 where `a-`'s executed content was the base's. Earliest owner: §6.6 decision class.

### N6 — editorial residues

- The refusal compares “the two outcomes”, while the reading is “on the failing outputs”. State that the comparison is on the failing outputs.
- §7.9's floor text omits the “answered by a failing assessment” case that §6.6 lists. It is covered, because that assessment is itself a failure of admitted content.
- §27.38 cites §26 for “a lenient but formally consistent reader”; §26 words it as “lenient assessments of outcomes that differ from a failing one only cosmetically”.

## 3. Re-verification of previous Reviews' findings

“Closed” means the named deductive trajectory is excluded by the candidate's contract, not executed qualification or acceptance.

### EF8445A

| Finding | Disposition | Basis |
|---|---|---|
| X1 candidate failure shared with admitted code, perturbed bits | **Closed** | Staleness needs a discriminating reading; an honest reader records the admitted outcome FAIL, a failure of admitted content, with a floor item for D1/D2. Identical outcome: refused, never stale. Lenient reader: E3 residual. Model discriminators |
| X2 later assessor wins after a perturbation | **Closed** | A later ordinary PASS is not a discriminating reading; one record must read the reproduction FAIL too |
| X3 D1/D2 admitted-content failure through an equivalence judgment | **Closed** | No reading, no staleness; the reading is R3 because `a-`'s content was the base's. The class rule over-escalates later readings (Y2) |
| N1 provenance | **Partly closed** | Item 7 and SD-9 verbatim; adoption still paraphrase (N1) |
| N2 basis-bounding judgments | **Closed** in its trajectory | Permissive use needs the judgment current; residues in N2 above |
| N3 relaxation premise | **Partly closed** | Brief item and absorption rule for mechanical verdicts; assessor-read absorption gap (N3) |
| N4 R2 retirement under edited readings | **Open** | Unchanged in substance (N5) |
| N5 residual prose | **Closed** | §7.4 and §10 mention staleness |

### Earlier Reviews

The `ef8445a..552ac01` diff touches:

- the workplan: front matter, §0, §0.1, §6.6, §6.8 step 3, §7.4, the §7.5 R3 row, the §7.9 floor, §9.6, §10, §21 item 5, §22, §26, §27.38-§27.39 and §28;
- the authority index (three lines) and the stakeholder record (item 7, SD-9);
- the model check, the continuation handoff, and two added qualification records (the revision-21 handoff and the `ef8445a` Review).

No other earlier Review record, `source/`, `dist/`, `orchestrator/`, test, release-state, PEM or archived-predecessor path changed. This was verified by `git diff --name-status`, hunk positions and blob identities.

- **4EC0024.**
  - B′1: **closed**, including perturbed assessor-read outcomes (X2).
  - B′2: **closed**; (2) and (4) still read every admitted observation, whatever its standing.
  - C1: **closed** for mechanical oracles; **reopened** for assessor-read oracles (Y).
  - C2a-C2c: **closed**; the start latch is kept.
- **6FE1000.** A1 and A3 **closed**; A2 **closed**, including assessor-read failures with perturbed outcomes (X1); B1 and B2 **closed**.
- **BA7F738.** U1a-U1c, U2a and U2b **closed** on their trajectories (U2 assessor-read now by an R2 reading); N3 **closed** (X3), with over-escalation (Y2); N4-N7 closed or superseded.
- **947370D.** W1 and W2 **closed** (mechanical unchanged; assessor-read W1 by a reading under the relaxed admitted reading); N5 remains as `ef8445a` N4 (N5 above).
- **A414588 A1-A3 and B, 203A42B A and B, 62C0B24 A, 644EB72 A and B, 4C35D92 A, 97E753F A, B1 and B2, 124B0B7 A, FFBAD17 A, FB3E542 A: closed.**
  - `home`, the anchor sets, authorship fail-closed, `qual` over retired obligations, `IMMATERIALITY` currency and `bind(j)` are unchanged.
  - `644eb72` B's case (removing a check in force at the base) is preserved by the “either” clause of “yields”.
  - `4c35d92`'s assessor-read reading change still raises reassessment, or a discriminating reading under the new reading (R2; R3 for a D1/D2 failure of admitted content).
  - FB3E542 B: **partly closed**, through Y.
- **Strata.**
  - S0 and S1 are unchanged. `stale` now reads one S2 value positively, so `undisputed` stays monotone and S2 keeps its unique least fixed point; the floor event is S3. The strata stay well-founded and single-valued. The text claiming that `stale` is an S2 constant, and the support-graph edge list, are stale (N2).
- **“Impossible” claims.**
  - “a later assessor's ordinary PASS of a new outcome never settles it by being later” holds.
  - “machinery never decides that a frame failure does not concern admitted content” holds for both oracle kinds.
  - “one outcome cannot be read both ways under one reading” holds at Admission as stated, for identical readings only (N5).
  - “no run can be hidden from (2) or (4)” and “runs on other content never delay anything” hold.

The remaining 730490D, AC71FA9, F3608F5, 8A75346, 441CF5C and F9D9DE8 closures do not depend on the changed text and remain **closed**. FFBAD17 N7 (inherited index and whitespace residue) remains outside this scope.

## 4. Out-of-matrix trajectories attempted

| Attempt | Result |
|---|---|
| Stale assessor-read candidate failure; later equivalence-covered admitted change; identical rerun outcome | **Fails** restrictively (Y1); reproduced in the model |
| Same on a D2 subject; later readings | **Fails**: R3 and a floor item at every change (Y2) |
| X1, X2, X3 with an honest reader | Hold |
| Lenient but formally consistent reader passes a perturbed outcome that still shows the defect | Residual (E3), disclosed; R3 for D1/D2 admitted-content failures |
| One outcome read PASS and FAIL under one reading | Holds: refused |
| Reuse of a reading after the admitted reading changes | Holds: it covers only under its own reading |
| Reading recorded before the reproduction | Holds: the reproduction must be identical, and P10 accepts the completion |
| Reading or its observation under an open, overridden or upheld blocking challenge; pre-loss reading | Holds: not standing |
| D1/D2 admitted-content failure made stale at R2 by reading the base | Holds: same content and reading is refused; a changed admitted reading is R3 |
| Editorial claim edit in a frame; D1/D2 failure of admitted behaviour | R2 retirement with no floor item (N5) |
| Identical-outcome D1/D2 candidate failure under the same reading | Never stale (holds); floor deferred to a reader (N4) |
| Reviewer disagrees with `a-` over one identical outcome | Cannot answer the reading obligation (N4); the claim stays `P` |
| Revoked completeness judgment behind an observation's narrow basis | Holds for (1) and (3); class check uses the recorded basis (N2) |
| Bounding judgment whose basis reaches the claim's subject | `F` by the least fixed point, misreported as corruption (N2) |
| Absorbed foreign relaxation, mechanical | Holds: verdict also under the last integrated revision |
| Absorbed foreign relaxation, assessor-read | R2 reading under the absorbed reading makes it stale (N3) |
| Mechanical branch: U1a, U1 revert, W1, W2, accepted relaxation, tightened reading integrated | Hold: text unchanged since revision 21 |
| Nondeterminism on the failure's own content | Holds: (2) fails; floor event for D1/D2 |
| External custody runner without run enumeration | Holds: makes nothing stale |
| Non-independent or unauthorized `supersedes` | Holds: refused at step 3 |
| Workflow layer, publication, frame enactment, intake, migration and recovery trajectories of earlier records | Hold as recorded; that text is untouched by revision 22 |

## 5. Minimum-architecture and capability-transfer assessment

**Minimality.** Revision 22 adds no primitive, record kind, store or component (§27.39). Carrying the reading on the ordinary passing assessment, with a one-line refusal rule, is the minimum concretization of the capability X restored, and removing the reading-ground judgment is a genuine subtraction. Two elements exceed what the capability needs: coverage bound to content identity, and R3 re-escalation of later readings. Both add cost and no protection (Y). Removing them is the minimum.

**Capability transfer** (§18, PEM). §27.38's table has four rows. A fifth is needed:

| Capability | Revision 21 | Revision 22 |
|---|---|---|
| Identical outcomes never discriminate | (4) | (4) |
| Nondeterminism goes to the owner | (2) | (2) |
| A revert re-counts | per-frame (3), (4) | per-frame (3), (4) |
| An assessor-read stop needs one independent reading of both outcomes | nowhere | discriminating reading |
| A stop, once earned, stands across a change that leaves what the oracle reads unchanged (`4ec0024` C1) | identity (assessor-read), verdict (mechanical) | verdict (mechanical); **nowhere** for assessor-read (Y) |

The [architecture owner][architecture] says: “do not drop an authority-bound capability merely because the old mechanism is ugly or because a new implementation appears simpler”. The fifth capability is bound by the evidence owner's “distinguish resolved reassessment from still-live disagreement”.

**Predecessor comparison.** Revision 22 did not touch §16.2 or §18. Blobs verified at the candidate, equal at `ef8445a`:

| Predecessor | Blob |
|---|---|
| befe678 hypothesis archive | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |
| Consolidated Protocol 8 plan archive | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| Orchestrator Architecture 1.6.0 (equal at public source and candidate) | `39e6de727f6c35402962509d30d947962992eaad` |

The bounded semantic comparison of §16.2 and §18 recorded by earlier Reviews still holds by identity.

**PEM basis and HAS.** Project instructions designate `main` as the integrated publication line. `git ls-remote origin refs/heads/main` gives `af0455753e20ee54a969c844872e29e270007211`, which equals the workplan's basis. Its `PROJECT-ENGINEERING-MEMORY.md` blob equals the candidate's, `1561797125622f355f84eb27319f87e8fa4227d9`. There is no branch overlay. Missing coverage proves no absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: The model is green at depth 4 and 5 with 77/77 discriminators while Y holds. It encodes Y as an expected discriminator value, P11 was narrowed so that it cannot see it, and owner_stale duplicates the candidate's assessor-read rule. Decision classes and the floor are outside the model, so Y2 is invisible. Section 22 still requires the C1 behaviour that section 6.6 now contradicts for assessor-read oracles.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen profiles required through the versioning owner; preserved by section 24; untouched by revision 22.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy. Repair at the owning D3 rule (section 6.6) and regenerate sections 7.9, 0.1, 22, 26, 27 and the model from it.
  - id: SP-002
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: Self-reference-safe identity unchanged by revision 22.
  - id: FF-001
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: No immutable publication in scope; it remains applicable to later genesis and release.
```

**7.2.1 reconciliation (scope d).** The release state at the candidate names 7.2.1 accepted-current, with public source `aaeaf8b6…` and recovery `efdd1b59…`, matching the handoff. `source/PROTOCOL_VERSION` is 7.2.1 at the public source. The diff changes no §0.4, §19 or §24 text, and no `source/`, `dist/`, `orchestrator/`, release-state or PEM path. The §0.4 obligation table and the §19 landing points therefore stand. The inherited evidence doctrine is not yet realized at Y.

**Workflow layer and doctrine realization (scope b).** §7.5 changed only in its R3 row, §7.9 only in its disagreement floor, and §9.6 by one brief item. The rest of §7.5-§7.10 and §9.6-§9.8 is unchanged, and earlier closures there stand. Y2 is a place where SD-2 is not realized in the intended direction: the human receives settled, repeated readings instead of only the important questions. §1.1 claims only what mechanism and evidence establish, consistent with SD-6.

**Persistence, derivation, concurrency, migration (scope c).** Untouched apart from §6.6 and §10. The strata assessment is in §3 and N2.

## 6. Qualification-program adequacy

§22's disagreement group now carries X1-X3, the basis-judgment and absorbed-relaxation cases, and the refusal. Its *Standing* (`4ec0024` C1) item was not restated, and for an assessor-read oracle it contradicts §6.6. A fixture suite built from §22 would be red against a faithful implementation of §6.6, or green against an implementation that silently deviates from §6.6. Neither outcome discriminates Y as a defect. §22 has no case of a later change with an identical assessor-read outcome, and none for the class of a re-reading.

The [testing owner][testing] asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Revision 22 is one for Y in the model.

The model check's sensitivity is real, but at the repaired point it is again self-referential:

- `owner_stale` no longer branches on the mode, but for assessor-read failures it is the candidate's own rule, transcribed. P13 and Q therefore cannot test that rule in the default mode, only other modes' distance from it. `REV21=1`'s red result (P7 166, Q 8,819) is meaningful for X, because X was genuine, but it measures distance from revision 22.
- The named discriminator “a discriminating reading does not cover a later change of content” uses a rerun outcome identical to the one read, and expects `P`. That is Y, recorded as correct.
- P11 was narrowed to mechanical failures (“whose stop needs no reading”). For identical assessor-read outcomes no reading is needed either, so the narrowing removes exactly the check that would have seen Y.
- The materiality partition that `ef8445a` asked for (outcomes that differ in value but not in what a reading finds) was not added. The model cannot represent a lenient reading or the class rule.
- The earlier modes fail long-standing properties (P7, P9, P10, P11, P12, Q, Q2), so their sensitivity stands.

Add the discriminators named in §1, restore P11 for identical assessor-read outcomes, and add the partition.

The four consolidation tests establish frontmatter and routing only. HARD-template thresholds, mutation strength, evaluator calibration, custody, blinding, paired baselines and doctrine-realization measurement remain later-gate obligations (§22-§25). No campaign was run and no improvement estimate is asserted.

## 7. What was verified and how

- **Candidate identity.** Resolved the candidate SHA and the workplan blob `8970b617…`, matching the handoff. Extracted a `git archive` of the exact candidate into a scratch subdirectory. Later commits, including the handoff commit `95d770a`, were excluded.
- **Governing source.** `aaeaf8b6…`, `efdd1b59…`, `af045575…` and `22f4bdba…` were present as commits.
- **Owners read** at `aaeaf8b6` with `git show`:
  - the D3 role entrypoint (`software-design/SKILL.md`: routing, D3 design contract, Independent Review and Challenge, Completion);
  - architecture, read first (learned-capability binding, mechanism-to-capability transfer, Review);
  - evidence (stale-state rule, binding health, discrimination, assessment disagreement);
  - convergence: active simplification trigger, review strategy after recurrence;
  - workflow: optional independent cognitive trajectories;
  - testing: the smallest plausible wrong concretization;
  - the kernel's Challenge text;
  - PEM entries by identifier.

  Release identities were resolved from `PROTOCOL-RELEASE-STATE.yaml` at the candidate.
- **Candidate read.**
  - In full: §0.1 (revision 22 record), §2.1, §2.5, §6.6, §10, §11.3, the stakeholder record.
  - The `ef8445a..552ac01` diff of the workplan, the authority index and the stakeholder record; the §7.5, §7.9, §9.6, §22, §26 and §27.38-§27.39 changes in context; the model-check source in full.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the archive: **4 passed, 0 failures**, Python **3.13.16**.
- **Whitespace.** `git diff --check ef8445a3… 552ac01b…`: **exit 0**, no diagnostics.
- **Model check**, depth 4, `--jobs 4`, 1,574,464 transitions in every mode:

  | Mode | Failures | By property | Discriminators differing | Exit |
  |---|---|---|---|---|
  | default `REV22` | 0 | — | 0 (77/77 as expected) | 0 |
  | `REV21=1` | 8,985 | P7 166, Q 8,819, O 0 | 8 | 1 |
  | `REV20=1` | 4,290 | P10 1,686, P13 2,604, O 0 | 12 | 1 |
  | `REV19=1` | 4,983 | P10 130, P13 4,813, P14 40, O 0 | 18 | 1 |
  | `REV18=1` | 7,540 | P10 1,130, P11 24, P12 2,156, P13 4,230, O 0 | 20 | 1 |
  | `REV17=1` | 117,031 | P9 29,719, P10 78,686, P11 192, P12 6,360, P13 2,074, O 0 | 23 | 1 |
  | `REV16=1` | 127,879 | P7 540, P9 29,663, P10 76,360, P12 6,408, P13 2,050, Q 5,416, Q2 300, O 7,142 | 28 | 1 |
  | `REV14=1` | 139,151 | P7 1,060, P8 1,126, P9 29,607, P10 73,288, P12 6,456, P13 1,860, Q 10,708, Q2 874, O 14,172 | 29 | 1 |
  | `REV13=1` | 325,687 | P7 16,338, P9 27,633, P10 71,072, P12 6,227, P13 1,860, Q 71,596, Q2 12,841, O 118,120 | 31 | 1 |
  | `REV12=1` | 331,438 | P5 347, P7 16,338, P9 27,613, P10 67,927, P12 6,247, P13 1,850, Q 75,601, Q2 13,069, O 122,446 | 34 | 1 |
  | `REV11=1` | 342,774 | P7 16,338, P9 27,865, P10 76,393, P11 216, P12 5,881, P13 2,074, Q 73,200, Q2 12,797, O 128,010 | 38 | 1 |
  | `REV10=1` | 343,752 | P1 3,514, P7 16,338, P9 27,649, P10 76,393, P11 216, P12 6,211, P13 2,074, Q 68,272, Q2 12,721, O 130,364 | 34 | 1 |

  Every mode fails properties other than the oracle, and the totals match §27.38.
- **Model check**, depth 5, default mode, `--jobs 4`: D5_DETAIL
- **Probe.** The candidate's own `Ledger`, `owner_stale`, `untouched_bearing_failure` and `oracle_unqualified`, loaded unmodified from the archive (§1). The probe script lives in a scratch subdirectory and is not part of the record.
- **Identities.** Verified the predecessor blobs, the release-state identities, the PEM blob at the candidate and at `af04557`, the stakeholder-record blob `c02bbeb9…`, the test blob `39ce361e…`, and the changed-path list.
- **Repository untouched.** No candidate, source, distribution, index, release state, PEM or frozen resource was changed. The only repository output is this record. Nothing was committed or pushed.

**Scientific inquiry envelope.** Examined how long an assessor-read stop stands, its decision class, the floor events and the strata after the repair. Materiality here is the ability to change support, closure, human routing or the next authorized action. No physical or numerical result is asserted; the examples are illustrative. One pinned candidate was reviewed through multiple deductive trajectories and one model probe. No variant search over scientific analyses was performed, and no delegates were launched. The judgment relies on accepted engineering, evidence, workflow and convergence doctrine, not on project D1/D2 authority, so the tension-search duty was not triggered.

## 8. What could not be verified

- **PEM schema validation** was not rerun. The PEM blob is unchanged since earlier Reviews. This is not a pass.
- **Remote state** was read once by `git ls-remote`. No further remote-state claim is made.
- **Readings and Manual compositions.**
  - Y assumes that the reading's `on(o, G)` restriction binds its coverage, as §6.6 writes and §27.38 and the model confirm. A Manual reading that let “covers its outcome” extend to identical outcomes on other content would contradict §27.38.
  - Y2 assumes that the evidence obligation's execution basis includes the changed file, or falls back to the whole governed tree; §26 names that fallback as a plausible routine case.
  - The class of a reading whose `about` set changes between frames (a reading admitted in a frame where no subject was D1/D2) is not specified; it is Manual-level.
- **The §1 repair** is a direction, not a verified design. Its equivalence on the trajectories that defeated revisions 10-21 is the owner's to establish.
- **Runtime evidence.** No SSDS production owner, witness deployment, harness adapter or Architecture Manual exists. Runtime fidelity, read recording per harness, failure injection, lineage attestation, privacy enforcement, scaling and burden reduction remain unexecuted (§21-§26), and none is counted as a pass.
- **Repository acceptance.** The full repository regression, package build and validation, distribution parity, frozen-resource census and Core snapshot tests were not rerun. This Review changes no protocol source or descendants.

## 9. Family-level convergence assessment (method step 5)

**(1) Did the repair reduce the failure surface or move it?** It closed the surface `ef8445a` found: no assessor-read failure now stops on a value difference, and the reading-ground judgment is gone. It moved part of the surface to the other end of the stop. Revision 21 compared assessor-read outcomes by identity both to stop a failure and to keep it stopped. Revision 22 replaced identity with a reading for the stop, which X required, and also for keeping it stopped, which nothing required. The family's recurring cause is the same in a new place: a stop keyed on a proxy (here, content identity of the observation) instead of on what the oracle reads.

**(2) Is it the minimum justified concretization?** Nearly. The minimum is revision 22 with the reading's coverage keyed on the outcome it read and the frame's reading, and without re-escalation of a failure already shown to be the candidate's own (§1). That removes text and adds nothing.

**(3) Is the family still recurring?** Yes, for the thirteenth consecutive cycle. `ef8445a` found the defect where a removal dropped a capability; Y is back in the “two repairs meet” pattern of revisions 18-20, between the X repair and the `4ec0024` C1 closure. This Review routes Y at family level, as the question of how long every stop of the family stands for both oracle kinds, and names the subtractive repair and an alternative that removes assessor-read staleness. It does not hold that the disposition abstraction needs another redesign.

**(4) Common-mode causes still present.**

1. **A same-family Review's repair direction adopted with its blind spot, for the third consecutive cycle.** The `ef8445a` Review proposed a reading of “`G`'s observed outcome” and R3 where “`G`'s content is later admitted content that may carry a fix of a failure the base already had”. Revision 22 adopted both. Content-bound coverage and the re-escalation are exactly Y.
2. **The qualification instrument encodes the choice under test.** The model's discriminator expects Y's value, P11 was narrowed to avoid it, and `owner_stale` transcribes the candidate's assessor-read rule (DS-001).
3. **Framing.** This Review's handoff lists “its coverage limits (its own content, the reading it was made under)” among the features to re-verify, which presents content-bound coverage as a given. §27.38 lists “Reuse a reading after the content changes” as an attack that holds, and asks only the permissive direction.
4. **Verification in one direction.** Every attack in §27.38 asks whether the repair can be made permissive. None asks whether a settled failure resurrects, although `4ec0024` C1 is exactly that.
5. **Shared model family, corpus and toolchain** between the author and every Review since revision 11 (SD-8), and a scratchpad shared with the authoring session (§10).

## 10. Common-mode dependency

This reviewer is a fresh-context sub-agent **of the same model family as the author** (Claude), launched by the authoring session from a handoff the author wrote, under stakeholder SD-8. That is a material common-mode dependency. Shared blind spots, framing inherited from the handoff's scope list, and the same corpus and toolchain are all plausible. The [workflow owner][workflow] says: “Separate context improves process independence but not epistemic independence when agents share model, source corpus, toolchain or oracle”. §9 item 1 shows the dependency concretely: the blocker sits in wording that the previous same-family Review proposed. The repair direction in this record carries the same risk.

The scratchpad directory provided to this sub-agent is shared with the authoring session, and its root already held files from that session. This reviewer read none of them and wrote only inside its own subdirectory, `review-552ac01/`.

The handoff gave no author conclusions. This record supplies **no different-family corroboration**. The design's own §9.6 lets policy require it for high-consequence surfaces, and the stakeholder has waived it for this cycle. A PASS from this cycle would still need owner adjudication and the production evidence of later gates ([workflow, Optional independent cognitive trajectories][workflow]).

## 11. D4 statement

**D4 remains NOT AUTHORIZED.** Phase B Review is NO-PASS. The next step is the owning D3 repair:

- key the discriminating reading's coverage on the outcome it read and the frame's reading, and remove the R3 re-escalation of failures already shown to be the candidate's own, at §6.6 (§1), keeping the rest of revision 22;
- regenerate §7.9, §0.1, §22, §26, §27 and the model check from the result, with P11 restored for identical assessor-read outcomes and a materiality partition;
- freeze a replacement immutable candidate.

Even a later Phase B PASS authorizes nothing by itself:

- G1 needs the accepted Manual and explicit stakeholder acceptance of the major change.
- G2 needs a separately reviewed shadow workplan and stakeholder authorization.
- G3 needs real-owner implementation evidence.
- G4 adds per-subject cutover, quiescence and rollback (§23-§25).

This Review grants no Manual acceptance, implementation permission, spend release, cutover, ratification or promotion.

[wp]: https://github.com/hjin98/scientific-software-development-system/blob/552ac01bb799c22dece5a33d93bd4244bea21d2a/workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
[kernel]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md
[evidence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/evidence-evolution-and-dependencies.md
[architecture]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/architecture-and-design.md
[workflow]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md
[testing]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md
[convergence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md
