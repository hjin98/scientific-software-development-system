# Independent D3 Review — SSDS 8 Architecture Manual, candidate 653e88c

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          653e88c10f469c1da4b89b55cd09b4c5ff595b37
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g));
                        technical evidence for G1 only
    MANUAL blob:        de2d62e06a395c1d8c44942d19b2f91ae7460e1f (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   963033b979fecdf5bbbb899500bdd1c0bd30f726 (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the different-family d94a293
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; delta-first attack of SD-35 in both
                        directions; consumer-to-premise trace of every `record` entry SD-35 keeps;
                        family-level recheck of earlier families; diagnostic model run in full
                        (parallel, all families and mutations); structural checks of handoff §3 step 9
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched
                        by the authoring session; did not author the candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-653e88c/snap`. The later commit adding the handoff (`28a36000`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. The accepted SSDP owners, the reviewed workplan's early-cutoff and impact-closure contract, and the stakeholder's SD-20/SD-22 and SD-35 directions can be realized together. B1 below is a defect in how the proposed Manual composes its own rules (a `record` entry imports a referenced record's whole currency while the counting rule and every refresh route read only its standing). SD-20's own text ("the record stands (not revoked or blocked, continuity holding)") points to a repair inside the stakeholder's direction, so no accepted authority is shown false or unrealizable.

## Verdict

**NO-PASS.** One blocker, B1, in the **D1-D3 change-rule / revising-duty family** (revision-assessment record and revision run), with a sibling at the gate consumer that SD-35 newly names as a required supporting premise. It is a long-standing latent defect, not one introduced by SD-35's repair, but SD-35 re-affirms it for the gate, and it is not disclosed anywhere in the Manual.

SD-35 itself is realized soundly for the trajectories that motivated it: the d94a293 B1 case and its four siblings no longer make displayed challenges, reports, adverse, historical or other-enactment records support premises, and no challenge-tier record reaches `current`. The plan-row policy restatement (d94a293 N1) is coherent. The diagnostic model is green on all five families and catches all 32 mutations; it cannot see B1.

## Blockers

### B1 — A basis-stale revision-assessment record keeps counting but can no longer be relied on, and nothing can replace it within the run: every `NATIVE` D1/D2 acceptance and gate in that run is stranded

**Family:** D1-D3 change rule / revising duty (revision-assessment record and revision run; the family of the b595f2c-798b2b4 findings); sibling at the gate consumer (SD-35's required premises). **Earliest owner:** proposed D3, Manual §4.3 (the `ACCEPTANCE` and `GATE_DECISION` rows' `record` entry on the revision-assessment record) together with §10.2 (what counts, and the `REVIEW(s, r)` trigger). **Status:** open, material. Non-local: it crosses basis composition (§4.3), currency (§5.5), frame roles (§7.3), Admission (§8.3 steps 6-7) and obligation derivation (§10.2).

**Exact rules at the candidate.**

- §4.3 line 565, `ACCEPTANCE`: "for a `NATIVE` D1/D2 subject, `record` on the revision-assessment record it relies on (§10.2)". Line 575, `GATE_DECISION` (SD-35): "`record` only on its required supporting premises: … and, for a D1/D2 revision, the revision-assessment record section 3 rendered".
- §4.3 line 572, `TASK_RESULT`: "`content` on the item revision (`EXACT`); frame-role `content` on reads and on `Δ(X)`; `validity` on governing units across subjects". A revision-assessment record *is* a `TASK_RESULT` (§10.2 line 1276).
- §5.5 lines 723, 729: `current(x) = base(x) ∧ ⋀ sat(e)`; `sat(record x) = current(x)`. §7.3 line 1117: a `context` entry (`u ∉ Δ(X)`) has "ordinary currency in the admitted state" after integration. §4.4: `EXACT` admits no equivalence coverage.
- §8.3 step 6 (line 1182): "every basis entry of every submitted support-tier record other than a report is satisfied … Otherwise the record is classified stale and routed to revalidation, not admitted." Step 7 (line 1183): a passing `ACCEPTANCE` or `GATE_DECISION ACCEPT` on a `NATIVE` D1/D2 triple is refused "unless a revision-assessment record for `(s, r)` already admitted counts for it … and the judgment carries a `record` entry on it".
- §10.2 line 1280: a record **counts** when "it is in the run …, `status1 ∉ {REVOKED, BLOCKED}`, and `cont` holds for it" — standing only, no currency; and "the accepting judgment carries a `record` basis entry on that record (§4.3), so the record's later revocation, block, risk override (`P`) or loss withholding reaches the acceptance". Line 1253: `REVIEW(s, r)` is derived only "with no revision-assessment record for `(s, r)` that counts". Line 1276: a revision-assessment record is only "the result of an `AUTHOR` task whose candidate yields `r`, or of a task answering `REVIEW(s, r)`".
- §10.2 line 1279: "Re-accepting an unchanged revision within its run reuses its record." §31.5 line 2673 qualifies the same: "re-acceptance of an unchanged revision after `REVALIDATE` within its run reuses its record." §5.5 line 766 (early cutoff): after upstream `a` changes and a re-review of `b` passes without changing `b`, "`b` is valid again", and records that "did not itself see `a`'s text" are current again.

**Decisive trajectory — the canonical D1 -> D2 cascade.**

1. `NATIVE` D1 subject `a` is accepted at `a1`. `NATIVE` D2 subject `b` has a `GOVERNING` prerequisite on `a` (another subject). An `AUTHOR` item `I` (revision `i1`) authors `b` at `r_b`. The task's brief inlines `a`'s text and the author reads it, so its `TASK_RESULT` `R` carries `revision_assessments` for `(b, r_b)` and has `content (a, a1)` (context role), `validity (a, a1)` (governing across subjects) and `content (I, i1, EXACT)`.
2. `X` integrates; the run `rid(b)` starts; `R` counts. A qualified reviewer records `j = ACCEPTANCE PASS` on `(b, σ, r_b)` with `validity (a, a1)` and `record R`; the gate holder records `h = GATE_DECISION ACCEPT` with `content (b, r_b)` and `record R` (SD-35). Both are current; `b` is valid.
3. A later accepted `AUTHOR` change moves `a` to `a2` (gated, accepted). This is the intended impact route (step 8: "an accepted change to a prerequisite authority, whose derived impact obligations are the intended consequence"). `j` is no longer current (its `validity (a, a1)` fails). `R` is no longer current either: `content (a, a1)` and `validity (a, a1)` fail permanently, since `a`'s change is real (no equivalence for `CONSUMER:TASK_RESULT`). So `h` is no longer current; it stays eligible, so `gterm = F` (§5.5 minimum).
4. The reviewed early cutoff now asks for a re-review of the unchanged `b` against `a2`. `b`'s revision and run are unchanged. `ACCEPT(b)` is derived and is **ready**, because `R` still counts (in the run, `CLEAR`, `cont`). The reviewer submits `j' = ACCEPTANCE PASS` with `validity (a, a2)` and, as step 7 requires, `record R`. Step 6 evaluates `sat(record R) = current(R) = F` and refuses `j'` as stale. Every further dispatch within budget is refused the same way.
5. No route produces a replacement record. `REVIEW(b, r_b)` is not derived (`R` counts). A revision-assessment record can only come from an `AUTHOR` task yielding `r_b` or a task answering `REVIEW(b, r_b)`, so the `ACCEPT` task cannot supply one, and a `REVALIDATE(R)` task (§12.3 line 1391, implementer) cannot either. `R` is never superseded, since task results are not. The gate is stranded the same way: `REVALIDATE(h)` is derived for `h`'s author or the owner (line 1255), but any superseding `ACCEPT` carries `record R` and is refused at step 6. Meanwhile `h` stays in `gterm`'s minimum at `F`.
6. `b` stays invalid for the rest of its run. The only exits are a byte change to `b` (a new run with a new `AUTHOR` result) or a tenure restart. Every descendant whose support passes through `b` is `F`.

**Siblings (same cause, each checked against the written rules).**

| Sibling | Trigger making the counting record permanently non-current | Result |
|---|---|---|
| (a) item amendment | any later byte change to the `AUTHOR` item's part (`content (I, i1, EXACT)`; `EXACT` admits no equivalence), even an R1 tightening or an editorial fix after integration | acceptance and gate stranded exactly as above |
| (b) incidental context read | the author or reviser read any unit outside `Δ(X)` (a sibling module, a README, a non-governing D3 document) that later changes | acceptance and gate of `b` become non-current through `R`, though `b`'s own acceptance basis never depended on that unit; then stranded |
| (c) revising-review result | the counting record is the `TASK_RESULT` of a task answering `REVIEW(s, r)` (absorbed, human, merged or adopted revision); its reads and governing validity go stale the same way | same |
| (d) gate consumer (SD-35) | each case above | the stale decision stays eligible at `F`; its author's or owner's superseding `ACCEPT` is refused at step 6; another holder's fresh `ACCEPT` is also refused, and could not raise the minimum anyway |
| (e) cutover / prospective tenure | the carrier's result on legacy context that later changes | same, after the cutover integrates |
| control: revocation, block, loss | upheld or open blocking challenge on `R`, or a loss boundary withholding it | `R` stops counting, so `REVIEW(s, r)` is derived, a fresh record is produced and re-acceptance works; risk override caps at `P`. **Holds.** |
| control: transient upstream invalidity | `a` momentarily invalid at the same revision, then re-accepted | `R`'s entries come back; no strand. **Holds.** |

Shared cause: **a `record` entry imports the referenced record's entire currency (its own basis), while the counting rule, the `REVIEW(s, r)` trigger and the stated purpose (§10.2: "revocation, block, risk override (`P`) or loss withholding") read only the record's standing. A record whose basis is stale but whose standing is intact can be neither relied on nor replaced.** §29.4's E0 row (line 2532) and SD-20 ("the record stands (not revoked or blocked, continuity holding)") both say "standing". Discovery stops here; further variants re-derive the same composition.

**Violated owner text.**

- Reviewed workplan early cutoff (workplan line 1397, restated in Manual §5.5 line 766): "If a re-review of `b` against the new `a` passes *without changing `b`*, `b` is valid again." For a `NATIVE` D2 `b`, no re-review can pass admission.
- Workflow owner at `aaeaf8b:source/shared/references/workflow-and-workplans.md`, "Authority lifecycle, mutation, and impact closure": "acceptance -> bounded dependent impact -> reconcretization/revalidation". Manual §0.4 S3 states the same. The impact on `b` can be closed only by an unrelated byte change.
- Evidence owner at `aaeaf8b:source/shared/references/evidence-evolution-and-dependencies.md`, binding health: when a required route becomes stale, "withdraw unsupported positive guidance, and rerun/remap where required". Here no rerun or remap route exists.
- Architecture owner at `aaeaf8b:source/shared/references/architecture-and-design.md`, "D3 formal-contract discipline": lifecycle states and transitions must be defined before dependent invariants use them. The lifecycle of a counting-but-stale record is undefined.
- The Manual's own claims at §10.2 line 1279 and §31.5 line 2673 ("reuses its record") are false for every in-run re-acceptance triggered by a context change.

An implementer must choose between incompatible statements: (i) read the entry by standing, against §5.5's `sat(record x) = current(x)`; (ii) derive `REVIEW(s, r)` on staleness, against line 1253; (iii) treat a `REVALIDATE` result as a revision-assessment record, against line 1276; or (iv) accept the strand, against line 1279, §31.5 and the early cutoff. Workplan §21 items 4, 5 and 7, and the gate side of items 10 and 26, are therefore not closed.

**Minimum repair directions (stakeholder options under the convergence owner; this is a non-local recurrence in a family with nine earlier findings).**

1. **Standing, not currency (recommended; closest to SD-20 and §29.4).** The acceptance's and gate decision's dependence on the revision-assessment record reads exactly what "counts" reads: in the run, `status1`, `cont`, with a `PROVISIONAL` record capping at `P`. For example, make that entry `identity` and fold the count into `tgt` plus a `P` cap in `base`, or give the entry a standing-only satisfaction. This narrows what the acceptance imports and keeps in-run reuse as §10.2 states. It adds one small clause, which **adds mechanism**: either a satisfaction variant or a `base` term.
2. **Currency, with a refresh route (no new mechanism; restrictive).** "Counts" also requires `current(R) ≠ F`. A basis-stale record then stops counting, `REVIEW(s, r)` is derived within the same run, and its answer is a fresh record. Readiness, Admission and the trigger read S2 at S3 or Admission, so stratification holds. Cost: a revising review after every change to anything the author read (sibling (b)) or to the item (sibling (a)), unless the `TASK_RESULT` minimum is also narrowed for this use. It re-runs the tension search after an upstream D1 change, which the stakeholder may want; it is not SD-20's "standing".

Either option must also reconcile §10.2 line 1280's purpose sentence, §16.6 section 3, §29.4 and §31.5, and should state the choice once at §10.2.

**Required discriminator.** At the future real owners (Admission step 6-7 -> Derivation `current`/`gterm` -> readiness/`REVIEW(s, r)` derivation -> inspector), run: `NATIVE` D1 `a` and `NATIVE` D2 `b` governed by it; `b`'s `AUTHOR` result reads `a`; integrate; accept and gate `b`; then accept a real change of `a`. Under option 1, an in-run re-acceptance and gate of unchanged `b` must be admitted, and `b` valid again with the old record. Under option 2, `REVIEW(b, r_b)` must be derived in the same run, and its answer must make re-acceptance and gate admissible. Under both, `ACCEPT(b)` must never be ready while every acceptance it can produce is refused `STALE_BASIS`. Add siblings (a)-(c), both admission orders, and a frame case (the change of `a` pending in `D_n[X_a]`). Negative controls: revocation, block and loss withholding of the record still make the acceptance non-current, and a risk override still makes it `P`. The diagnostic model cannot discriminate this: its revision-assessment record (`ra`) has an empty basis, and it has no Admission step 6, no `TASK_RESULT` basis and no `REVIEW(s, r)` trigger.

## Non-blocking findings

### N1 — "The required evidence the core cites" is not a defined core field; three boundary cases read two ways

**Earliest owner:** D3 wording, §4.3 line 575 with §16.6. SD-35's record names §16.6 as a realized section, but §16.6 is unchanged: the core does not mark which displayed records are required supporting premises. "Supporting premises", "every other record" and the identity list (historical judgments, non-required evidence, qualifying records) settle most cases. Three need one sentence:

- (i) **Replaced evidence of a required obligation.** Old realization or assessment `R1` is stale and fresh `R2`/`A2` support `e`. If `R1` is "a record of the required evidence the core cites", step 6 refuses every `ACCEPT` while the core shows `R1`, and §16.6's refusal of an `UNQUALIFIED` `ACCEPT` "while the evidence core lists required evidence that is … stale" fires too. That strands the gate whenever stale history of a required obligation is displayed.
- (ii) **Several current passing assessments of one obligation.** `record` on each makes the decision a conjunction where `ev` is a disjunction. This is a restrictive, liftable revalidation, but it should be stated as intended.
- (iii) **A qualifying record that is itself required evidence.** "Every other" makes it `record`, which is right, but worth stating.

**Suggested repair (subtractive):** the required supporting premises are, for each required obligation `e`, the passing admissible assessments through which the core shows `ev(s, e)` holding at the rendering head (their realizations are reached by the assessments' own entries). Every other evidence record, stale or replaced ones of a required obligation included, gets `identity`. Have §16.6 mark them, so the mode assignment is a projection. The model's gate family takes the role as input ("required evidence (current or not)"), so it cannot test this classification.

### N2 — Citation and scope drift from the delta

- §0.3 (line 101) still says "SD-11 to SD-34 are cited where they apply", although §4.3 and §5.10 (b) now cite SD-35.
- The §5.10 heading lists SD-24…SD-34 but its table cites SD-35.
- §31.3 says "All of them check §5.10 (g) 1-8 against the oracle", but the fifth (gate-basis) family checks only I1/I3 and I9, and (g) states no I9. The gate-basis rule is §4.3's, not §5.10's, so (g)'s new sentence "a gate decision's basis built from its evidence core" lists a case whose property (g) does not state.
- SD-35's record lists §13.4 and §16.6 among the realized sections, but neither changed. §13.4 is consistent as it stands ("feasibility is not claimed"); §16.6 is N1.

Editorial; none makes a material rule ambiguous.

### N3 — The gate-basis diagnostic transcribes SD-35 rather than testing it

The new family (600 scenarios) gives each core item a role (`required`, `revision`, `shown`), maps role to mode exactly as §4.3 does, and its oracle (`oracle_gate`) reads the same roles. Its premises are empty-basis records. A green run therefore shows only that `identity` items never reach `current` and that challenge-tier records stay outside it. It cannot show that the roles are right (N1) or that a required premise is usable (B1). This is consistent with §5.10 (g)'s disclaimer and PEM DS-001. §31.6's new (Y) discriminator is good at the real owners for d94a293 B1. It should gain B1's discriminator and N1 (i)-(ii).

### N4 — Plan-row policy wording (d94a293 N1): held, with the stakeholder option still open

The plan row now states the denial as "a conservative resolution policy, not a claim about why the plan was rejected". The reach is unchanged: same prose and fixed fields, any item or plan, `cur` not read. A rejection for over-tight or infeasible controls cured by a loosening `r'` still vetoes a peer's acceptance of `r'`, because `r*` is a common tightening of both. Only the rejecter's or owner's relief or supersession lifts it. This is exactly what the row now says, and §13.4's "feasibility is not claimed" agrees. Whether ordinary peers should certify such cures remains a stakeholder option (5895687 N5, 913db8f N7, d94a293 N1), not a defect.

## Closure audit

The closure map was used to navigate. I checked its claims against the workplan §21 list (all 27 items read in full at the candidate) and the Manual sections it names; the §16.2 rows were checked against §26.4 at the level of row disposition. This audit spot-checks subordinate clauses (fsync configuration, fence-commit format, witness model `(N, q_a, r, f)`, takeover and ABA policy, `output_renames`, the 168-hour cap, custody enumeration, `INFEASIBLE_CRITERION`, bootstrap, quiescence, genesis, `HARD` qualification); it does not re-derive every clause independently.

| Item | Disposition at this candidate |
|---|---|
| 4 (basis composition and mode assignment per kind) | **partly closed (B1)**: the `ACCEPTANCE`/`GATE_DECISION` entry on the revision-assessment record composes with the `TASK_RESULT` minimum into an unrecoverable dependency; N1 for the gate's evidence classification |
| 5 (derivation) | **partly closed (B1)**: currency of in-run D1/D2 re-acceptance is contradictory |
| 7 (obligation rules, readiness, discharge) | **partly closed (B1)**: `ACCEPT(s)`/`GATE(g)` ready while unanswerable; `REVIEW(s, r)` never derived for a basis-stale record |
| 10, 26 (gate template; decision/inspector templates) | gate consumer inherits B1 (sibling (d)); d94a293 B1's display/support conflict is closed |
| 1-3, 6, 8, 9, 11-25, 27 | no unresolved architectural decision found in this bounded audit |

§16.2 rows: the 26 product-invariant rows and the frozen-surface rows have explicit replacements, retirements or preserved boundaries in §26.4. No **Deferred** row survives (the word does not occur in the Manual). None found unresolved.

## Refinements R1-R14

| # | Assessment |
|---|---|
| R1 | Sound as stated (one recorded execution basis, `on⁺ ⇒ on⁻ ⇒ link⁻` by construction, positive-only completeness); its residuals are disclosed in §32.2. Rechecked the completeness-polarity text of §6.6 for Phase B N2 (below). |
| R2, R3 | Sound fail-closed SCC clamp and integrity halt. |
| R4 | Sound under the declared incarnation model; costs disclosed. Not re-derived beyond the text. |
| R5-R7 | Sound; not re-derived beyond the bounded checks of earlier Reviews and the text. |
| R8, R9 | Sound locally; supersession authority and the never-lost veto are unchanged by the delta. |
| R10 | **Unsound in part (B1)**: its within-run statement ("current only within the revision run") presumes in-run re-acceptance and re-gating exist, but they do not once the revision-assessment record's basis moves. The cross-tenure and cross-run statements hold. |
| R11 | Sound against fallback to an earlier unqualified decision; B1 shows a non-supersedable stale member pinning `gterm` at `F` for a run. The minimum is not at fault: the unanswerable premise is. |
| R12 | Sound; unchanged by the delta. |
| R13 | Sound; unchanged. |
| R14 | Sound as the selected conservative reach policy; the plan row's restatement as a policy is coherent (N4). |

SD-35's change is a D3 decision inside §21 item 4's delegated space (the workplan fixes no gate basis composition), not a refinement of the reviewed contract, so its absence from §0.3 is correct.

## Re-verification of earlier findings (family level)

Disposition key: **C** closed by the named current rule; **D** design/disclosure closure with real-owner execution owed later; **R** retained, disclosed decision or stakeholder option; **P** partly closed. Reviews before d94a293 were not replayed item by item. The delta since d94a293 touches only §0.3 R14's wording, §4.3's gate row, §5.10 (b)'s plan-row wording, §5.10 (g)'s case list and §31.3/§31.6. I therefore re-derived the family mechanisms below independently, and I treat each earlier record's per-item closure as unchanged unless a mechanism below reopens it.

**Mechanisms independently checked at this candidate:**

- Gate basis (SD-35): d94a293 B1's primary case and siblings (i) open non-blocking challenge, (ii) risk-overridden challenge, (iii) stale non-required realization and moved-provenance finding, (iv) standing gate rejection from another enactment, (v) holder's own rejection superseded by its `ACCEPT` are all now `identity`. None reaches `current`; the core stays exact; vetoes still act by existence (§5.10 (c)); required evidence still lowers the decision. **C.** The kept required premise for D1/D2 is B1's sibling (d).
- Judgment disagreement (§5.10): the one reach rule over S0/S1 `asserts`; per-kind table; plan closed form (same prose and fixed fields, `cur` unread) over chains, incomparable branches, joins, reverts, loosenings and R2 amendments; review reach on changed-unit content under any item or plan; relief and supersession admissibility; `nonind` in `base`; adjudication root/class at Admission; acting rule for every permissive route. Unchanged by the delta; model green with all mutations caught. **C/R** as in d94a293.
- Matching (§6.3-§6.6): frozen resolution context, `on⁻` tree-only, class-stated `ext`/`bound`, `link⁻` for (2)/(4), no identical-tree shortcut. Phase B N2 re-tested in text: an alternate tree differing only outside a recorded narrow basis, for a differing old-content run in (2) and a yielding present-content run in (4), under a completeness judgment becoming `P`, blocked, revoked or loss-withheld. Only (1)/(3) narrow, because both adverse conditions use `link⁻` anchored on the failing run's record. **C.** Support cycles (§5.6) and corrupt prefixes (§5.7) still fail closed. **C.**
- D1-D3 change rule and revising duty (§1.2, §10.2): the effect-keyed write set and the event-keyed run with `tgt` hold for revert, absorption, adoption, re-identification and cutover. **P**: B1 is a new sibling in this family, outside every earlier trajectory, which all concerned which record counts, never a counting record whose own basis moved.
- Content identity, gate qualification (`unq`, `gterm`), equal-region partition: unchanged; no new finding. **C.**

| Prior record | Disposition at this candidate |
|---|---|
| D94A293 (different family) | B1 **C** for its stated trajectory and siblings (above); N1 **C** wording / **R** stakeholder option (N4 here); N2 **R** cross-plan amended copy, disclosed in §32.2; N3 **P**: a gate-basis family was added but transcribes roles (N3 here) |
| 913DB8F | B1 **C** (changed-unit content key, plan-subject carries; reconfirmed by d94a293 and unchanged); N1-N8 as in d94a293's table, unchanged by the delta |
| 5895687, 4C52205, both E548472, D6734C4, 83A82DF, 0D2B35E, 34803DF, BF23372, A6ED164 | plan, review, equivalence and completeness rows: blockers and SCs **C** by the closed-form plan reach, content-keyed review reach, union composition, orientation-free authors and the one reach rule (unchanged since d94a293); N items **C/R/D** as d94a293 records; plan-policy items **R** (N4) |
| 6B986DE, 29DA56E, 51070E5, 9E5A763, 051CCE3, 63DDF91, F03B15E, 61CD09B, 362AF9F, F22B4DC, both B46C250, F7419D5, 575DC78 | independence, adjudication, acting/enactment, run identity, gate minimum and supersession families: **C** for their blockers. Gate-consumer residues that d94a293 held at **P** under its B1 are now **C** for display/support, but sibling (d) of B1 here keeps the gate consumer **P** |
| 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC, 3540D98 | matching, content identity, qualification and partition: **C**, with R items unchanged |
| 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363, CC005DB, C6DA678, B595F2C, 6FF4ED1 | **C** for each stated blocker (run-keyed counting, event-keyed run, `tgt` read by every consumer, frozen matching, effect-keyed write set). In the D1-D3 change-rule family, 86ab683's restrictive check ("re-acceptance of an unchanged revision … legitimately reuses its record") and 798b2b4's run closures are **P**: B1 shows in-run reuse fails once the record's basis moves |
| Phase B closures, N1-N4 | closures in Phase B §3 re-verified for the matching family (above); N1 **R** paraphrase-only adoption instruction (§32.2); N2 **C/D**; N3 **R/D** diagnostic limits; N4 **R** empirical costs |

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Upstream D1 change, then early-cutoff re-acceptance and re-gate of an unchanged `NATIVE` D2 subject | **B1** |
| Amendment of an integrated `AUTHOR` item; change of a unit the author merely read | **B1** siblings (a), (b) |
| Stale gate decision on a D1/D2 subject: author's supersession, another holder's fresh `ACCEPT` | **B1** sibling (d): both refused, minimum stays `F` |
| Revision-assessment record revoked, blocked, risk-overridden or loss-withheld | held: stops counting, `REVIEW(s, r)` derived; `P` propagates |
| Gate core showing open non-blocking and overridden challenges, stale non-required evidence, another enactment's `REJECT`, the holder's superseded `REJECT` | held (SD-35) |
| Gate core showing replaced stale evidence of a required obligation; two current assessments of one obligation | N1 (ambiguous classification; potential strand under one reading) |
| `QUALIFIED` `ACCEPT` over stale required evidence | held as a consequence: step 6 refuses it and `ev` is `F` anyway; a `QUALIFIED` decision is useful only for limitations outside required evidence, as §31.5 states |
| New required evidence obligation added after an unchanged gate decision | held as designed: `valid` and discharge read `ev` for the current requirement set directly; the decision does not cover evidence it was not shown, and nothing claims it does |
| Plan rejection for infeasibility cured by a loosening; peer acceptance of the loosened revision | held as policy (N4) |
| Composition, chain and union reach; review re-identification with a one-byte heading edit | held (unchanged; model green) |
| Completeness lapse under a narrow-basis failure (Phase B N2) | held |

## Minimum architecture and capability transfer

No new primitive, component, record kind or persistent surface is added by the delta, and SD-35 narrows the use of an existing mode, which is the minimum repair d94a293 asked for. B1's option 2 needs no new mechanism. Option 1 needs one small clause, marked above. Neither requires a registry, latch or new state.

Architecture 1.6.0 (`orchestrator/docs/architecture.md`, blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41`, so the version-bound Core and frozen profiles are preserved (PEM PC-001). Capability transfer is unchanged by the delta; the d94a293 map was not re-derived in full.

**PEM.** Activated, since this is mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` both resolve to `af0455753e20ee54a969c844872e29e270007211`, with PEM blob `1561797125622f355f84eb27319f87e8fa4227d9`. The candidate's PEM is byte-identical, so there is no overlay. Schema validation with the candidate's own validator and the original object store: "PEM schema 1 valid: 5 families, 0 notices". Task-local HAS:

- **PC-001**: APPLICABLE (frozen profiles; preserved).
- **DS-001**: APPLICABLE (a green diagnostic coexists with B1 and with N1).
- **SP-001**: evidence-only (one owner for the revision-assessment condition; B1 is two readers of one record disagreeing).
- **SP-002, FF-001**: evidence-only, not material here.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 separates G1 document checks from G2-G4 runtime evidence and claims no execution it lacks. Two gaps:

- §31.5's revision-assessment case asserts "re-acceptance of an unchanged revision after `REVALIDATE` within its run reuses its record". Under the written rules that is false whenever `REVALIDATE` arose from a context change, which is the early-cutoff case. A production owner faithful to §4.3, §5.5 and §8.3 would fail this discriminator, or pass it only by deviating from the Manual. B1's discriminator must replace or extend it.
- The diagnostic (N3) shares claim definitions and helpers. Its new gate family transcribes role-to-mode. It models no `TASK_RESULT` basis, Admission currency, readiness or `REVIEW(s, r)` derivation, so it cannot discriminate B1 or N1.

## Doctrine-realization map and O1

§29 maps all seven entrypoints. The D1/D2 revising-duty row (line 2532) claims E0 "for presence and order … (in the revision run, standing)", and line 2540 makes every `NATIVE` D1/D2 revision need a counting record "before acceptance and for validity". The E0 claim about presence and order holds. Its assembled effect does not (B1): a standing record that the acceptance cannot rely on makes the E0 mechanism block legitimate reconcretization. No other map claim depends on the delta.

O1 (§0.5) is unchanged: the realized record, readers, routine questions, retention and marked surfaces (all within the requested deliverable; none beyond) are stated. The gate brief remains a marked within-deliverable surface. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

Executed against the extracted candidate:

- Blob identities above (`git rev-parse` at the candidate).
- `git diff --check d94a293015bb06b9ed2cda2b5d505d324fe7c856 653e88c10f469c1da4b89b55cd09b4c5ff595b37`: exit 0. The delta is 7 files (Manual 12 lines changed, closure map, model, stakeholder record, continuation handoff, previous handoff and Review record).
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests OK (routing and lifecycle structure only).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 bf2337285dfdaba5d535e73cf76af3d5b78978f0`: 73 files, 23,269 insertions, 1 deletion (that historical comparison only).
- `git diff --name-only fad3ee41… 653e88c… -- source dist orchestrator/docs/architecture.md`: empty.
- PEM validation as above.
- Diagnostic model at the candidate, blob `fd154cbca217e566895945ce53313d4b6dbc6cfd` (hash re-checked equal to the snapshot file). I imported it unmodified with `python3 -I` from a scratch driver that runs exactly the `--mutations` workload. That is `run_family` for each of the five families (`CORE`, the three in `FAMILIES`, `GATE_BASIS`) with `MUT` cleared, then, for each of the 32 entries of `MUTATIONS`, `MUT = {m}` and `run_family` on each family that mutation names: 39 jobs (5 base + 34 mutation-family runs), on 24 forked worker processes. The job set was audited against the module's own lists: 39/39, no omission or duplicate.
  - Base results, all with zero invariant failures: transformation-review/acceptance/gate 1,515,364 scenarios; equivalence-chain 299,760; completeness-cover 37,600; plan-coverage 205,800; gate-basis 600.
  - Every one of the 32 mutations is caught, by the same invariant groups as the d94a293 record, plus `gate_basis_record_all` caught by I1/I3 and I9 and `gate_basis_identity_all` caught by I1/I3.
  - Sum of per-job times: 9,048.6 s.
  - I did not run the module's `main()` itself; the driver calls the same functions in the same configuration.
- Governing owners read at `aaeaf8b`: `source/roles/software-design/SKILL.md`, `architecture-and-design.md` ("D3 formal-contract discipline"), `workflow-and-workplans.md` (authority lifecycle and impact closure; D1/D2 revision gates), `evidence-evolution-and-dependencies.md` (stale-state; binding health), `convergence-and-cycle-economy.md` (family closure; review strategy), `testing-and-validation.md` (proxy-proof), `project-engineering-memory.md` (activation, HAS).

Not verified:

- No production SSDS, real gate or runtime was exercised.
- The doctrine map was checked only for rows touching the delta and B1.
- Earlier Reviews' per-item closures were not replayed (stated above).
- I noticed, but did not establish, whether Admission step 8 ("no collateral regression") combined with non-latched discharge and `content` entries on reads lets a later admitted change to a file that an earlier, integrated item's task read be refused as collateral regression. This is a workplan-level interaction outside the delta, and I make no finding on it. The author may wish to check it alongside B1's family, because it shares B1's mechanism (a `record` entry on a `TASK_RESULT` whose reads move).

## Scientific checks

Method: one pinned architecture candidate; deductive counterexamples bound to exact owner text; a family-level recheck; structural tests; and the candidate's diagnostic with its prescribed mutations. Material findings: B1 and N1-N4; none concerns a scientific observable, numerical method or realized scientific result.

**I produced, ran or reviewed no realized scientific results.**

Variants evaluated: one normative candidate. Five B1 siblings plus two controls, three N1 boundary cases, and eleven out-of-matrix trajectory classes (overlapping, not independent trials). One diagnostic configuration with 5 base families and 32 mutations. The criterion was to find a material counterexample, not to select a favourable result.

No accepted project D1/D2 scientific authority was relied on for a consequential judgment, so no tension search was triggered. Gaps: real-owner execution, reader adequacy and operating costs.

## Common-mode note

The reviewer is of the **Claude family**, the same family as the Manual's author and as most earlier Manual reviewers. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. This reviewer was engaged as a fresh-context sub-agent launched by the authoring session. It did not receive the authoring conversation, but fresh context is not epistemic independence. It shares the corpus, the inherited workplan and handoff framing, the prior Review records (read as hypotheses), the Git/Python toolchain and the diagnostic's claim definitions and helpers.

B1 was found by tracing a premise that SD-35 keeps back through the referenced record's own basis. That route lies outside the diagnostic's model and outside every earlier Review's trajectories in this family, of both families. Shared-family blind spots remain possible; a different-family confirmation of the repair is advisable.

## D4 statement

This Review authorizes **no D4**, cutover, architecture acceptance, product-scope extension or proposed default. Repair B1 at D3 (stakeholder choice between the options above), reconcile §10.2, §16.6, §29.4 and §31.5, consider N1-N3, extend the diagnostic or the qualification design for B1 and N1 as the testing owner requires, freeze a replacement candidate, and obtain an independent Review before stakeholder G1 acceptance. G2 still separately requires a reviewed shadow workplan and explicit stakeholder authorization.
