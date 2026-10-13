# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 11

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 97e753f83f1ddfb916547fdb984abf1053c362aa
    SCOPE: whole proposed architecture; (a) the revision-11 repairs: existence-keyed
           assessment disagreement (S1 disputed/disposed, in_effect dispositions, widened
           assessment key, monotone S2), the §22/§7.4 provisional-discharge alignment and
           the bounded model check; (b) workflow execution and verification layer and the
           doctrine-realization objective; (c) persistence, derivation, concurrency and
           migration; (d) Protocol 7.2.1 inheritance reconciliation
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: aac0635225b677639ec3502df29192ef0f684a40 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5,
           AC71FA9, 730490D, FB3E542, 124B0B7; all NO-PASS
    REVIEW METHOD: immutable-owner reconstruction; attack of each revision-11 repair as a
           new mechanism (key identity versus applicability, disposition polarity versus
           currency and counter-challenge); cross-stratum and frame/loss interaction
           attacks; prior-finding re-derivation; qualification-method challenge;
           exact-candidate structural tests and bounded model check
    REVIEWER: Claude (same model family as the author), a fresh-context sub-agent launched
           by the authoring session from REVIEW-HANDOFF-SSDS-8.0-REVISION-11.md (stakeholder
           SD-8); same model family as the author
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-97E753F-NO-PASS.md

Candidate section references below mean the [primary workplan at the candidate][wp]. Governing-owner links pin the public source above. This context authored neither the candidate nor any prior Review, received none of the authoring conversation, and treated the handoff's scope description, the workplan's self-assessments (§0.1, §27.16-§27.17), the model check's green result and every prior verdict as hypotheses.

The blockers below are deductions from the proposed contracts, not observed SSDS runtime failures. Their asserter is the reviewer named above; their disposition is **OPEN** against the exact candidate. This record is their canonical home. Revisit after the D3 owner reconciles the assessment-disagreement contract (§6.6, §7.4, §10, §15.4, §22) and freezes a replacement candidate. No accepted project scientific D1/D2 claim is challenged.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The [kernel, Verification and Challenge][kernel] says: “A coherent parent with a wrong child is an ordinary blocker.” The governing evidence owner's disagreement, applicability and binding-health requirements are coherent and jointly realizable: a conservative over-approximation of which adverse assessments apply, plus dispositions that count only while current and uncontested, satisfies all of them. Both blockers below belong to the proposed D3 concretization.

The stakeholder record supports what the workplan attributes to it: SD-5/SD-6 accept the revision-5 principles and an aspiration measured rather than claimed; SD-8 quotes the 2026-10-13 instruction verbatim and directs a same-family sub-agent cycle. Nothing in the candidate claims that a sub-agent PASS accepts the architecture; acceptance of objectives, product scope and the major change remains with the stakeholder (§25 items 11-12; [workflow owner][workflow]).

## Verdict

**NO-PASS.** Two blockers remain, both in the assessment-disagreement mechanism that revision 11 re-derived:

- **A — key identity is not applicability.** The widened key treats “different execution or claim revision” as “stale”, but the candidate's own equivalence rule keeps such evidence current. A competent, current failing assessment can then sit outside the key of a later passing assessment, and the claim and its discharge become unqualified with nothing resolved. §7.4 and §6.6 also compute disputedness differently in exactly this case.
- **B — dispositions do not carry their own polarity.** A disposition counts regardless of its own currency (B1), and an upheld challenge that disposes a failing assessment keeps disposing while a blocking challenge against it is open (B2). B2 contradicts the candidate's own stated rule.

Revision 11 closes the `124b0b7` Blocker A trajectories it targeted: an open ordinary challenge, a loss boundary and positive-only requalification no longer end a dispute. It also closes `124b0b7` N2. The family nevertheless recurs after the simplification pass, so the [convergence owner][convergence]'s next step applies: bounded reconsideration of the assessment-disagreement abstraction at its owner (§6.6), not another local exception.

Requested checks: the four routing tests pass, `git diff --check` is clean, and the model check is green at depths 4 and 5 and red under `REV10=1`. None of them discriminates A or B (§6 below), and none establishes semantic adequacy.

## 1. Blockers by earliest owner

### A — a split key hides a live, current disagreement

**Owner text at the candidate.**

- §6.6, Assessment key: “Execution identity means the execution-mode content revisions, data identity, environment, backend and precision, but **not** seed or replicate. […] A failing assessment on superseded code or a moved claim revision has a different key from a passing one on the current code and revision, so stale failing evidence never conflicts with fresh passing evidence. That is S4, satisfied by construction rather than by a currency test.”
- §10: “A realization supports a claim at revision `c` only while its execution basis is current and its target is `c`, **or an equivalence judgment covers the change**.” §6.6 `sat(content)` likewise satisfies a content entry through `EQUIVALENCE` paths. §6.7 and the §13 “Manual edit of authority” row make such judgments the ordinary early-cutoff route.
- §6.6 S2 evidence term: `⋁_{passing admissible assessment a for e at cur(s)} ( current(a) ∧ undisputed(key(a)) )`.

**Primary trajectory (execution side; every step locally compliant).**

1. Claim subject `s` at revision `c`, evidence obligation `e`, one regime and parameter instance, execution dependency `u` at `r0`. Designated-runner realizations with seeds 1 and 2 are assessed PASS (`a+1`) and FAIL (`a−`) by competent assessors. Both have key `K0 = (s@c, spec, regime, exec{u@r0, …})`. `disputed(K0)` holds, `valid(s) ≤ P`, and an adjudication obligation goes to the owner. This is the §22 base case.
2. An implementer task changes `u` from `r0` to `r1`, for example a refactor or comment edit that normalization does not remove. An independent qualified reviewer records `EQUIVALENCE(u: r0 → r1)` for the consumption class covering the realizations' execution entries. This is the early-cutoff path of §6.7.
3. Through that judgment, `a+1`, `a−` and their realizations stay current at `r1` (§6.6 `sat`, §10). `a−` is therefore a valid, current failing assessment for the present state.
4. The Dispatcher runs the candidate's required executions (§7.8), or the execution-change rerun obligation of §10. A seed-3 rerun passes and is assessed PASS (`a+3`) with key `K1 = (…, exec{u@r1, …})`.
5. `K1` has no failing assessment, so `undisputed(K1) = T`. The evidence term is `max(current(a+1) ∧ P, current(a+3) ∧ T) = T`, and `valid(s) = T`. A diagnostic transcription of the two equations gives `P` before step 4 and `T` after it.
6. `disputed(K0)` and its adjudication obligation stay open, but nothing reads them for `s`. No supersession, upheld challenge or `IMMATERIALITY` judgment occurred. The accepted equivalence asserts the *opposite* of resolution: that the failing evidence still applies.

**§7.4 contradicts §6.6 in this very case.** §7.4 requires that “every evidence obligation of o has a current admissible realization assessed passing for the current claim revision, **and is undisputed**”. Read per obligation, `e` has a disputed key (`K0`, current via equivalence) and discharge is at most provisional. Read per realization, as S2's disjunction computes it, discharge is `DISCHARGED`. An implementer must choose between two owners of one predicate. The [architecture owner][arch] says such a disagreement cannot be resolved by file order or route priority.

**Sibling trajectories.**

- *Claim side:* an editorial claim revision `c → c'` with an equivalence judgment keeps `a−` current at `c'` under key `(c, …)`. The target change raises assessment-review obligations, which do not gate validity. Whichever realization is reassessed first decides the outcome: if the passing one is reassessed first, the claim is unqualified until (and unless) the failing realization's reassessment lands.
- *Concurrent environments:* if two designated runners with different environment, backend or precision identities are both admissible for one specification, PASS on one and FAIL on the other never conflict. Whether both can be current is a Manual realization question (§21 item 11). The candidate fixes the key composition at D3, however, so nothing prevents the split.

**What it violates.**

- The [evidence owner, Assessment disagreement][evidence]: “An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.” It also requires that “supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement.”
- Its Applicability section: “A valid failing observation is evidence.” And: “Do not suppress contradictory admissible observations to manufacture a pass.”
- The candidate's §10: a disagreement is “ended only by an in-effect supersession, upheld challenge or `IMMATERIALITY` judgment”. None occurred.

Revision 10's §27.15 rejected “computing conflicts from S0/S1 facts, which would let stale failing evidence qualify claims”. Revision 11 adopts S0/S1 facts and approximates staleness by key inequality. That approximation is unsound in the permissive direction whenever equivalence or several concurrently current execution identities exist. It is also unsound in the restrictive direction (N3).

**Earliest owner.** D3 §6.6 Assessment disagreement (the key and the conflict set) together with §7.4's discharge predicate and the §22 oracle. Not the evidence owner, not a Manual detail, not D4.

**Minimum repair direction.** Make the conflict set track applicability in the conservative direction without reading S2 currency antitonically. For example, a failing assessment conflicts with passing assessments of the same claim and evidence obligation unless its target or execution revision differs from the current one and no admitted, not superseded, not revoked `EQUIVALENCE` judgment links the two. The existence of such a judgment is an S0/S1 fact, and counting it adds conflicts, so S2 stays monotone. Decide at D3, not by Manual omission, whether environment, backend, precision and data identity are claim-defining (part of the specification, so a mismatch is inadmissible) or execution variation (so a mismatch conflicts). Make §7.4 and §6.6 compute one predicate per evidence obligation. Reuse existing records; no store, registry or component is needed.

**Required discriminators.** Through real Admission, Derivation, discharge and inspection consumers:

- PASS and FAIL at `u@r0`; equivalence `r0 → r1`; a passing rerun at `r1`. The claim stays qualified and labelled `disputed` until an in-effect disposition.
- Contrast: the same change without equivalence, which is genuinely stale. There must be no qualification.
- The claim-side editorial variant, with reassessment order varied.
- Two concurrently admissible execution identities, if the Manual permits them.
- §6.6 `valid` and §7.4 discharge agree on every generated ledger containing a disputed and an undisputed key for one obligation.

§22's present oracle, “These must not qualify the claim at all: a failing assessment on superseded execution code or a moved claim revision (a different key)”, must be rewritten. As written it would certify the defect as expected behaviour.

### B — disposition effects ignore currency and counter-challenge polarity

**Owner text at the candidate.**

- §6.6: `in_effect(d) ⇔ cont(d) ∧ ( d challenge-tier: in_force(d) ; d support-tier: ¬superseded(d) ∧ status1(d) = CLEAR )`.
- §6.6: “Dispositions are permissive for the claim. […] They therefore count only while in effect: **suspended by an open blocking challenge**, ended by an upheld one, withheld after a loss boundary. Their other effects keep their own polarity.”
- §0.1: “Each disposition counts only while **not challenged**, not superseded and not withheld by a loss boundary.”
- §27.16: “Challenge of a dismissal; challenge of `IMMATERIALITY` | Holds: the disposition is not in effect while challenged.”
- S1: `in_force(y) ⇔ gate(y) ∧ ¬∃ c : c.target = y ∧ (upheld(c) ∨ (c.blocking ∧ open(c) ∧ ¬counter(c)))`, and `counter(c) ⇔ restrictive(c.target)`.

**B1 — a stale disposition keeps disposing.** `in_effect` never consults `current(d)`.

1. Live dispute: `a+` and `a−` of one key on claim `s`, governed by D2 subject `G@g0`.
2. A qualified actor records `IMMATERIALITY` `i` covering `a−`, reasoning that the failing regime boundary lies outside `G@g0`'s stated scope. Its basis holds a `validity` entry on `G@g0`; `a−`'s basis does not depend on `G`. `disputed` becomes false.
3. The D2 owner revises `G` to `g1` and brings that boundary into scope. `i`'s basis fails, so `current(i) = F` in S2. `s`'s acceptance also goes stale through its validity entry on `G`. `a−` stays current.
4. Re-review of `s` against `G@g1` passes without changing `s` (§6.7 early cutoff). `in_effect(i)` is still `T` (`cont`, not superseded, `status1 = CLEAR`), so `a−` stays disposed and `valid(s) = T`.

A derived “judgment no longer current” obligation for `i` exists (§7.1), but nothing makes validity or discharge wait for it. The same omission lets a discriminating superseder count after its own basis moves. It also lets a disposition count irrespective of whether it is current in the frame where it is used; the candidate does not forbid frame-`X` assessments from superseding admitted-frame records.

B1 reverses the candidate's own allocation rule, “judgment already made, basis still current -> reused mechanically” (§1.2). §15.4 already treats dispositions as permissive across loss; currency has the same polarity and is unhandled. The `124b0b7` Review's minimum repair direction named “target/execution movement” among the effects to re-derive. Revision 11 handled movement of the *assessments* by key and did not handle movement of the *dispositions*.

**B2 — an open counter-challenge does not suspend an upholding-based disposition.**

1. Live dispute on key `K`.
2. Ordinary blocking challenge `c` against `a−`; adjudication `d` upholds it. `d` is restrictive (it revokes `a−`) and disposes `a−`; `disputed(K)` becomes false.
3. A qualified actor files a **blocking** challenge `c2` against `d`, contesting the revocation: `a−` was a valid FAIL. By S1, `c2` is a counter-challenge, inert while open. `in_force(d)` stays `T`, so `in_effect(d)` stays `T` and the claim stays unqualified while the disposition is contested.

Evaluated with the candidate's own `s1_disagreement_model_check.py` ledger class: after step 2 `disputed = False`; after appending `c2`, still `False` (`counter = True`). For contrast, an `IMMATERIALITY` judgment under an open blocking challenge gives `disputed = True`. The formula implements revocation polarity for both of `d`'s effects. The stated rule (“suspended by an open blocking challenge”; “not in effect while challenged”) requires the claim-side effect to be suspended. The formula and the prose cannot both govern.

**What B violates.**

- The [evidence owner, Applicability][evidence]: “Use `review-required` when applicability is uncertain. PASS/accepted/closed cannot depend on stale, rejected, unavailable-required or otherwise inadmissible evidence.”
- Its binding-health rule: when a route becomes “stale, revoked, or no longer applicable, degrade present use to `REVIEW_REQUIRED`/`UNAVAILABLE`, withdraw unsupported positive guidance”.
- Its disagreement rule, quoted under A.
- For B2, the candidate's own §6.6, §0.1 and §27.16 rules, and the `124b0b7` minimum direction that “a contested applicability/disposition must not manufacture unqualified support”.

**Earliest owner.** D3 §6.6 (`disposed`/`in_effect`), with the §15.4 polarity table and §22. S1's revocation semantics are correct for the revocation effect and should not change.

**Minimum repair direction.** Give the disposition effect its own polarity, separately from a record's other effects:

- it counts only while the disposition is current in the evaluating frame;
- it counts only while no blocking challenge against it is open, counter-challenge or not;
- it is withheld by a loss boundary.

Disposition currency can enter S2 *positively*, so `undisputed` stays monotone: it may read `current(d)` for dispositions, never for failing assessments. Under the existing acyclicity check this keeps the least fixed point. Revocation stays as S1 defines it.

**Required discriminators.**

- B1: an `IMMATERIALITY` judgment whose prerequisite moves while the failing assessment stays current; the qualification returns until a current disposition exists. The same for a discriminating superseder whose basis moves.
- B2: an upheld challenge disposes `a−`; an open blocking counter-challenge against the upholding re-qualifies the claim while `a−` stays `REVOKED`; dismissal of the counter-challenge restores the disposition.
- An extension of the bounded check with an abstract currency bit per record and these two properties, plus a sensitivity mode reproducing revision 11, so that the check shows it can tell the two apart.

## 2. Non-blocking findings

### N1 — historical governing-version adoption remains partly evidenced

Unchanged from `124b0b7` N1: the 2026-10-12 adoption instruction is still a paraphrase (§0.4; stakeholder record, Not covered). The handoff independently binds this Review to 7.2.1. Earliest owner: §0.4, pending stakeholder restatement.

### N2 — §15.4's supersession row keeps a justification revision 11 falsified

The row “ordinary challenges …, supersessions | unchanged (never gated by `cont`; **none of them can relax anything**)” sits beside the new row withholding dispositions. §6.6 now says “One family of ungated records does relax something”. The behaviour is specified by the next row, so this is editorial. The Manual must still state how a failing assessment that is already superseded can be disposed again after a boundary (double supersession is unspecified).

### N3 — “S4 by construction” is overstated in the restrictive direction

A failing assessment whose basis moved outside its key (a governing oracle or tolerance subject, a revoked realization premise) keeps disputing its key forever. That is restrictive, and arguably the owner's `review-required`, so not unsafe. But the claim that stale failing evidence “never conflicts” is false, and every such movement creates owner work. Repair it together with A.

### N4 — human attention for D1/D2 disputes is keyed on a predicate, not a record

§6.6 routes disputed D1/D2 claims to human attention via the domain floor. That floor (§7.9) is defined for reports. A8 requires escalation “keyed on the escalating record's existence” and discharged only by an authenticated human judgment. If the obligation is keyed on `disputed(K)`, an agent disposition removes it with no human decision. §7.9/§21 item 26 should key it on the failing assessment's existence.

### N5 — the decision class, role and independence of dispositions are unfixed

Step 3 lists the judgments that need independence and omits `IMMATERIALITY` and disposing supersessions. The role table assigns neither. A9 (“no actor reviews or accepts its own work”) suggests R2 with independence, and R3 for D1/D2. This is Manual items 3 and 23, but it should be stated with the A/B repair.

### N6 — Admission step 8's “only legal way to reopen others' closures” is overbroad

With existence-keyed disagreement, admitting a competent adverse assessment (or a challenge) can turn another obligation's `DISCHARGED` into provisional. Read literally, step 8 would reject that as collateral regression and suppress the evidence. The phrase “affected by the merged tree” supports a content-change-only reading. Scope the sentence explicitly.

### N7 — per-replicate stochastic assessment will dispute routinely

Excluding the seed from the key is right for disagreement, but a stochastic specification assessed per replicate will produce disputes whenever any replicate fails. Manual item 11 should define assessment granularity (for example, ensemble assessment) so that `IMMATERIALITY` does not become routine; candidate reopen trigger (§26).

## 3. Re-verification of previous Reviews' findings

“Closed” means the named deductive trajectory is excluded by the candidate's contract, not executed qualification or acceptance.

### 124B0B7

| Finding | Disposition | Basis |
|---|---|---|
| A primary — challenge `a−`, no adjudication | **Closed** | Disagreement is keyed on existence; only an *upheld* challenge disposes. Model check P1 green to depth 5 (§6.6) |
| A recovery sibling — loss, positive-only requalification or attestation | **Closed** | `a−` still exists; pre-loss dispositions are withheld by `cont`; the §15.4 rows added (§6.6, §15.4) |
| A further assumption — supersession/disposition polarity across recovery, supersession and movement | **Partly closed** | Loss and ordinary challenge reconciled; disposition currency and counter-challenge not (B); target/execution movement handled by a key that misses equivalence (A) |
| N1 adoption provenance | **Partly closed** | N1 above |
| N2 §22 provisional oracle narrower than §7.4 | **Closed** | §22 now says “in-force risk override or policy permitting provisional continuation (§7.4)” |

### FB3E542

| Finding | Disposition | Basis |
|---|---|---|
| A — prospective acceptance reused after restoration | **Closed** | `bind(j)` unchanged by revision 11 (§6.9); not reopened by the disagreement change |
| B — current PASS selected beside a competent FAIL | **Partly closed** | Same-key live conflict caps at `P`; A shows a competent current FAIL outside the passing assessment's key; B shows a contested or stale disposition ending the cap |
| N1, N2 | Partly closed; closed | As in `124B0B7` |

### Earlier Reviews

Revision 11 changed only §6.6's disagreement predicates and key, §7.4's parenthetical, §10's assessment row, the §15.4 rows, §21 items 3 and 5, §22's disagreement group and the bookkeeping sections (`git diff 124b0b7..97e753f`). The prior closures that the `124B0B7` record lists for 730490D, AC71FA9, F3608F5 and FFBAD17 do not depend on the changed text, except FFBAD17 A (S1 polarity).

- **FFBAD17 A** was re-checked: model-check P3/P4 (an open counter-challenge or a loss never lifts a revocation) are green to depth 5. Removing the inhibition edges does not reintroduce the original trajectory.
- **Strata.** `disputed` is a post-S1 function: S1's recursion never reads it, and S2 reads it as a constant. S2 is monotone, and the least-fixed-point and one-pass topological claims hold again.
- **Cycle protection.** Mutual-validity cycles and the f9d9de8 configuration remain rejected by step 5 and S2's least fixed point.

FFBAD17 N7 (inherited index and whitespace residue) remains outside this scope. 730490D, AC71FA9 and F3608F5 N1 remain partly closed as N1 above. All others listed there remain **closed**.

## 4. Out-of-matrix trajectories attempted

| Attempt | Result |
|---|---|
| Equivalence-covered execution change, passing rerun in the new key | **Fails** (A) |
| Editorial claim revision with equivalence, passing realization reassessed first | **Fails** (A, claim-side sibling) |
| `IMMATERIALITY` whose prerequisite moves while the failing assessment stays current | **Fails** (B1) |
| Upheld challenge disposes `a−`; open blocking counter-challenge against the upholding | **Fails** (B2; reproduced with the candidate's ledger class) |
| Frame-`X` reassessment superseding an admitted failing assessment, `X` never integrated | **Plausible** instance of B1: cross-frame supersession is not forbidden; disposition ignores frame currency |
| Open ordinary challenge, override or not, against `a−`; `LEDGER_LOSS`; positive-only attestation | Holds (§6.6, §15.4) |
| `IMMATERIALITY` or superseder under an open blocking challenge, or under a risk override | Holds: `status1 ≠ CLEAR`, so not in effect |
| Pre-loss disposition not re-recorded | Holds: withheld by `cont` |
| Replicates differing only in seed; reversed ledger order | Holds: same key, conflict; order-independent |
| Stale failing assessment after a non-equivalent code change | Holds as designed (different key and genuinely stale) |
| Failing assessment whose basis moved outside the key | Restrictive residue (N3) |
| Adverse assessment admitted against another subject's discharged obligation | Ambiguous at step 8 (N6) |
| Agent disposition of a D1/D2 dispute | Human attention may vanish without a human judgment (N4) |
| `disputed` read inside S1 or S2 recursion; inhibition cycle | Holds: post-S1 constant; no inhibition edges remain |
| Spurious failing assessments to hold a claim provisional | Holds within the trust model: qualified actors only; the cap is provisional; abuse is challengeable |
| Workflow layer: principal, implementer or reviewer attempts outside role; task partition; tightening then loosening; floor-item downgrade | Holds as recorded by earlier Reviews; revision 11 does not touch §7.5-§7.10 |
| Publication: paused publisher, two fences, foreign return to `B_n` | Holds within the disclosed residual (§15.3) |

## 5. Minimum architecture, capability transfer and inheritance

**Minimality.** Removing revision 10's inhibition edges and restoring monotone S2 is a genuine simplification, and no primitive, store, record category or component was added (§27.17). The repairs A and B need none either. They change what existing S0/S1 facts and S2 currency the disagreement predicate reads. The convergence owner's core progression places this family at “post-simplification recurrence”, so the next pass should reconsider the disagreement abstraction as a whole: one notion of *applicable adverse evidence* (conservative) and one notion of *effective disposition* (polarity-aware, currency-aware). Otherwise it risks a fourth local patch. Practical minimality otherwise remains conditional on the empirical items of §26.

**Predecessor comparison.** The bounded semantic comparison recorded by `124B0B7` was re-checked for identity: revision 11 did not touch §16.2 or §18. Verified blobs at the candidate:

| Predecessor | Blob |
|---|---|
| befe678 hypothesis archive (equal to `513da27` source) | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |
| Consolidated plan archive (equal to `af04557` active source) | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| Architecture 1.6.0 (equal at public source and candidate) | `39e6de727f6c35402962509d30d947962992eaad` |

Frozen Core profile resources `ssdp-protocol-6.6`, `7.0`, `7.1` and `7.2` are present at the candidate, consistent with PC-001 and §24. The original `befe678` object is not in this clone.

**PEM basis and HAS.** Project instructions designate `main` as the integrated publication line. The local tracking ref `origin/main` is `af0455753e20ee54a969c844872e29e270007211`, equal to the workplan's basis. Its `PROJECT-ENGINEERING-MEMORY.md` blob equals the candidate's: `1561797125622f355f84eb27319f87e8fa4227d9`, coverage `PARTIAL`, watermark `23e46543…`. The uncovered later interval proves no absence. There is no branch overlay.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: The bounded model check and the §22 disagreement oracle stay green while A and B hold; neither can close the owner claim.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen profiles required through the versioning owner; present at the candidate; preserved by §24.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy; repair the one canonical disagreement owner (§6.6) and regenerate §7.4, §15.4 and §22 from it.
  - id: SP-002
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: Self-reference-safe identity unchanged by revision 11.
  - id: FF-001
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: No immutable publication in scope; remains applicable to later genesis and release.
```

Schema validation could not be completed in this environment (§8). No PEM update was made.

**7.2.1 reconciliation.** The release state at the candidate names 7.2.1 accepted-current with public source `aaeaf8b6…` and recovery `efdd1b59…`, distinct; the same holds at `origin/main`. Between `22f4bdba` and `aaeaf8b6`, the kernel, semantic-definition and Git owners are byte-unchanged. Workflow, evidence, concurrency, storage, security and versioning changed by additions only: the concurrency change extends one sentence, and the versioning change extends the profile list. This is consistent with §0.4. The §0.4 obligation table and the §19 landing points stand. The inherited disagreement behaviour is the one place where the reconciliation is not yet realized (A, B).

## 6. Qualification-program adequacy

§22's assessment-disagreement group is much stronger than revision 10's: nothing is seeded resolved, real consumers are required, and challenge, override, loss and attestation siblings are enumerated. It still cannot discriminate A or B.

- It has no equivalence-covered key split, no stale disposition and no counter-challenged upholding.
- Its “must not qualify” oracle for “superseded execution code” would pass the defective behaviour in A.
- It does not require §6.6 and §7.4 to agree.

The bounded model check is honest about its status (DS-001), and its sensitivity mode does discriminate revision 10. But it models a single key, no basis, no currency, no equivalence and no frames. Its properties P1-P4 test only that appending restrictive records never *ends* a dispute or lifts a revocation. B2's ledger is generated by its own candidate enumeration and passes, because no property checks disposition suspension. The [testing owner][testing] asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Revision 11 itself is such a concretization for both blockers. Add the discriminators named under A and B, and extend the check as stated.

The four consolidation tests establish frontmatter and routing only. HARD-template thresholds, mutation strength, evaluator calibration, custody, blinding, paired baselines and doctrine-realization measurement remain later-gate obligations (§22-§25). No campaign was run and no improvement estimate is asserted.

## 7. What was verified and how

- **Candidate identity.** Resolved the candidate SHA and workplan blob `aac0635…`. Extracted a `git archive` of the exact candidate into a scratch directory; later commits, including the handoff commit `0db420d`, were excluded.
- **Owners read.** Read at `aaeaf8b6` with `git show`: the D3 role entrypoint, architecture, evidence (Applicability, binding health, Assessment disagreement), testing (evidence classes, oracle strength, proxy-proof), convergence (core progression, active trigger, review strategy) and the kernel's Challenge text. Compared the owners changed between `22f4bdba` and `aaeaf8b6`.
- **Candidate read.** Read §0-§28 of the candidate, the full `124b0b7..97e753f` diff, the stakeholder record, the authority-index SSDS 8 section diff, the routing test and the model check.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the archive: **4 passed, 0 failures, 0.023 s**, Python **3.13.16**.
- **Whitespace.** `git diff --check 124b0b75… 97e753f8…`: **exit 0**, no diagnostics.
- **Model check.** `python3 qualification/ssds80/s1_disagreement_model_check.py --depth 4`: **1677 transitions, 0 failures, exit 0**. With `REV10=1`: **49 failures, exit 1**. At depth 5: **23 933 transitions, 0 failures**, matching §27.16.
- **B2 reproduction.** Loaded the candidate's `Ledger` class read-only and evaluated the counter-challenge ledgers: `disputed` stays `False` under an open blocking counter-challenge against the disposing upholding, and becomes `True` for an `IMMATERIALITY` judgment under an open blocking challenge.
- **A and B1 arithmetic.** A scratch transcription of the S2 evidence term reproduced A (`P → T`) and B1 (`T` with `current(i) = F`). This is diagnostic arithmetic only, kept outside the repository.
- **Identities.** Verified the predecessor blobs, the release-state identities, the frozen-profile presence and the PEM blob identity above.
- **Repository untouched.** No candidate, source, distribution, index, release state, PEM or frozen resource was changed. The only repository output is this record. Nothing was committed or pushed.

**Scientific inquiry envelope.** Examined architecture-mediated evidence applicability, disagreement, disposition, closure and recovery. Materiality here is the ability to change support, closure or the next authorized action. No physical or numerical result is asserted. One pinned candidate was reviewed with multiple deductive trajectories; no variant search over scientific analyses was performed and no delegates were launched. This judgment relies on accepted engineering and evidence doctrine, not on project D1/D2 authority, so the tension-search duty was not triggered.

## 8. What could not be verified

- **PEM schema validation.** `source/project_engineering_memory.py` against the candidate PEM failed with `UNAVAILABLE: repository revision is not resolvable as an immutable object` for every historical evidence route (for example `b59adc77…`, `55c08526…`, `7f7b5e24…`). This checkout is a **shallow clone** (`git rev-parse --is-shallow-repository` = `true`) lacking those objects. This is an environment limitation, not a PEM defect and not a pass. The `124B0B7` record reports a passing validation with a full object store; the blob is unchanged since.
- **Remote state.** `origin/main` is the local tracking ref; no fetch was performed and no remote-state claim is made. The original `befe678` object is unavailable.
- **Runtime evidence.** No SSDS production owner, witness deployment, harness adapter or Architecture Manual exists. Runtime fidelity, failure injection, lineage attestation, privacy enforcement, scaling and burden reduction remain unexecuted (§21-§26) and none is counted as a pass.
- **Repository acceptance.** The full repository regression, package build and validation, distribution parity, frozen-resource census and Core snapshot tests were not rerun. This Review changes no protocol source or descendants.
- **Environment currency.** Whether several environment, backend or precision identities can be concurrently current for one specification is a Manual realization. A's concurrent-environment sibling is therefore conditional; its primary trajectory is not.

## 9. Common-mode dependency

This reviewer is a fresh-context sub-agent **of the same model family as the author** (Claude), launched by the authoring session from a handoff the author wrote, under stakeholder SD-8. That is a material common-mode dependency. Shared blind spots, framing inherited from the handoff's scope list, and the same corpus and toolchain are all plausible. The handoff gave no author conclusions, and the findings above arose from attacking the revision-11 mechanisms directly. This record supplies **no different-family corroboration**: the design's own §9.6 lets policy require that for high-consequence surfaces, and the stakeholder has waived it for this cycle. A PASS from this cycle would still need the owner adjudication and production evidence of later gates ([workflow, Optional independent cognitive trajectories][workflow]).

## 10. D4 statement

**D4 remains NOT AUTHORIZED.** Phase B Review is NO-PASS. The next step is owning D3 reconsideration of the assessment-disagreement abstraction (§6.6, with §7.4, §10, §15.4 and §22 regenerated from it) and a replacement immutable candidate. Even a later Phase B PASS authorizes nothing by itself:

- G1 needs the accepted Manual and explicit stakeholder acceptance of the major change.
- G2 needs a separately reviewed shadow workplan and stakeholder authorization.
- G3 needs real-owner implementation evidence.
- G4 adds per-subject cutover, quiescence and rollback (§23-§25).

This Review grants no Manual acceptance, implementation permission, spend release, cutover, ratification or promotion.

[wp]: https://github.com/hjin98/scientific-software-development-system/blob/97e753f83f1ddfb916547fdb984abf1053c362aa/workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
[kernel]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md
[arch]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/architecture-and-design.md
[workflow]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md
[evidence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/evidence-evolution-and-dependencies.md
[testing]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md
[convergence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md
