# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 12

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 4c35d92d2c75c9961d4d3b97c35c6dfad04c6336
    SCOPE: whole proposed architecture; (a) the revision-12 repairs: applicable adverse
           evidence (S0 `applicable`, `adverse`), effective disposition (S2 `ev`, `undisputed`,
           `disp`, `eff`, `contested`), removal of the assessment key, the single `ev` term
           shared by validity and discharge, the decision class, independence and D1/D2 floor
           of dispositions, the scoping of Admission step 8, and the rewritten bounded model
           check; (b) workflow execution and verification layer and the doctrine-realization
           objective; (c) persistence, derivation, concurrency and migration; (d) Protocol
           7.2.1 inheritance reconciliation
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: 7f18ae39d8e31be0427d424b5ae7bbec1911230c (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5,
           AC71FA9, 730490D, FB3E542, 124B0B7, 97E753F; all NO-PASS
    REVIEW METHOD: immutable-owner reconstruction; attack of each revision-12 repair as a
           new mechanism (which basis entries carry adversity; which premises dispose;
           disposition currency and contest); cross-stratum, frame, Admission-currency and
           loss interaction attacks; prior-finding re-derivation; qualification-method
           challenge; exact-candidate structural tests and bounded model check, with a
           scratch extension of the model's own ledger class
    REVIEWER: Claude Opus 5.5 (model id claude-opus-5-5), a fresh-context sub-agent launched
           by the authoring session from REVIEW-HANDOFF-SSDS-8.0-REVISION-12.md (stakeholder
           SD-8); same model family as the author
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-4C35D92-NO-PASS.md

Candidate section references below mean the [primary workplan at the candidate][wp]. Governing-owner links pin the public source above. This context authored neither the candidate nor any prior Review, received none of the authoring conversation, and treated the handoff's scope description, the workplan's self-assessments (§0.1, §27.18-§27.19), the model check's green result and every prior verdict as hypotheses.

The blocker below is a deduction from the proposed contracts, not an observed SSDS runtime failure. Its asserter is the reviewer named above; its disposition is **OPEN** against the exact candidate. This record is its canonical home. Revisit after the D3 owner fixes which premises of an adverse assessment carry its adversity (§6.6, with §6.8 step 6, §10, §15.4, §22 and the model check regenerated from it) and freezes a replacement candidate. No accepted project scientific D1/D2 claim is challenged.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The [kernel][kernel] says: “A coherent parent with a wrong child is an ordinary blocker.” The governing [evidence owner][evidence] is coherent and realizable here. It names the dimensions over which applicability must be recoverable, says a valid failing observation is evidence, requires `review-required` when applicability is uncertain, and requires an unresolved disagreement to keep closure qualified. A D3 predicate that tests adversity over those dimensions, keeps uncertain adversity in force and lets dispositions count only while they stand satisfies all of these together. The blocker below belongs to the proposed D3 concretization.

The stakeholder record supports what the workplan attributes to it. SD-5 and SD-6 accept the revision-5 principles and an aspiration that is measured, not claimed. SD-8 quotes the 2026-10-13 instruction verbatim and directs a same-family sub-agent cycle. Nothing in the candidate claims that a sub-agent PASS accepts the architecture. Acceptance of objectives, product scope and the major change stays with the stakeholder (§25 items 11-12; [workflow owner][workflow]).

## Verdict

**NO-PASS.** One blocker family remains, in the mechanism revision 12 introduced:

- **A — adversity follows the assessor's whole basis, not the evidence's applicability.** `applicable(a−)` tests every basis entry of the failing assessment. That basis includes everything the assessor read, declared or was widened to. Any move of such an entry removes the failing evidence from the adverse set, while the failing realization stays current and nothing disposed of it. The same over-breadth lets an upheld challenge against any record in the assessment's record-mode basis, such as a completeness judgment, permanently dispose of the failing evidence.

Revision 12 closes the `97e753f` trajectories it targeted. An equivalence-covered key split, a stale disposition and an upholding under an open blocking counter-challenge now keep the claim qualified, and §6.6 and §7.4 read one `ev` term. The effective-disposition half (`eff`, `contested`) is sound as far as this Review could attack it, and should be kept. The failure is in the other half: each of revisions 10, 11 and 12 has replaced *“failing evidence that may still apply”* with a proxy — currency, then key identity, now basis satisfaction — and each proxy is permissive somewhere. The [convergence owner][convergence]'s bounded reconsideration should derive adversity from the owner's own applicability dimensions rather than from a fourth proxy.

Requested checks: the four routing tests pass; `git diff --check` is clean; the model check is green at depth 5 and red under `REV11=1` and `REV10=1`. None of them discriminates A (§6 below), and none establishes semantic adequacy.

## 1. Blockers by earliest owner

### A — adversity lapses with the assessor's context

**Owner text at the candidate.**

- §6.6, applicability: “`applicable(x)` ⇔ every basis entry of x passes, in its role and frame: content (u, r, k) : r = cur(u), or r reaches cur(u) through admitted EQUIVALENCE judgments on u of class k […] `adverse(s, e)` = { failing assessments a- for e on s's claim unit : applicable(a-) }”. Also: “It over-approximates currency: whatever is current is applicable. […] A failing assessment therefore leaves the adverse set only by staleness, or stops counting only by disposition.”
- §6.4: a `content` entry covers “everything the actor saw: the judged revision, **context supplied or read**, change base, content behind evidence”. The basis of every record is the union of the mechanical minimum (including “the dependency closure over the relation classes the rule requires (§6.5), the completeness judgments that closure used (record)”), “**recorded reads** made through the interface, plus harness-observed reads”, and “**declared reliance** the actor adds at submission. An actor can add to the mechanical minimum, never remove from it.” §9.1: `read(ref)` is “recorded into the basis”.
- §6.6, disposition: “`d` is an `UPHELD` adjudication of a challenge targeting `a-`, **or targeting a record in `a-`'s record-mode basis** (a revoked realization premise)”. §6.4 assigns record mode to “premises that are themselves judgments: completeness, evidence realization/assessment, plan acceptance”.
- §10: “Failing evidence that is not applicable (§6.6) never qualifies the current claim.” §22: “These must not qualify the claim at all: a failing assessment whose execution or claim revision moved with no admitted equivalence, **or whose oracle subject moved**”.

**A1 — primary trajectory (every step locally compliant).**

1. Claim unit of subject `s` at revision `c`, evidence obligation `e`. The designated runner produces realizations `ρ1` (seed 1) and `ρ2` (seed 2) on unchanged execution content. Qualified assessor `X` assesses `ρ1` PASS (`a+`); qualified assessor `Y` assesses `ρ2` FAIL (`a−`). While assessing, `Y` calls `read(w)` on a unit `w` that is neither the claim, the specification, the oracle nor in `ρ2`'s execution basis. It might be a design note on the tolerance, a neighbouring module, or the test's README. The read enters `a−`'s basis as `content (w, w0)`. `X` did not read `w`. Then `ev(s, e) = min(T, P ∨ F) = P`, the evidence is labelled `disputed`, and an adjudication obligation goes to the owner.
2. An implementer task in another plan item edits `w` to `w1` inside its own write scope. Nobody needs an equivalence judgment on `w`, so none is recorded.
3. `applicable(a−) = F`, because `(w, w0)` fails and no equivalence path exists. `adverse(s, e) = ∅` and `undisputed(s, e) = T`. `current(a+) = T`. So `ev(s, e) = T`, `valid(s) = T`, and §7.4 discharge is `DISCHARGED`.
4. The adjudication obligation, which exists “for each adverse assessment with no standing disposition”, disappears, and so does the `disputed` label. `ρ2` is still a current, admissible failing realization: same target, same execution, same specification and oracle. No supersession, upheld challenge or `IMMATERIALITY` judgment occurred. For a non-D1/D2 claim nothing reaches a human. For a D1/D2 claim the floor item survives, because it is keyed on existence, but validity and discharge are unqualified meanwhile.

A scratch subclass of the candidate's own `Ledger` (`s1_disagreement_model_check.py`) gives the failing assessment this one extra content entry. It reproduces the trajectory: `ev = P` before the edit, `ev = T` after it. The model's plain-language oracle also reports the claim unqualified, because it reuses `applicable` (N2).

**Siblings (same cause).**

- *The implementer grades its own exam.* In frame `X`, a reviewer's failing assessment of the candidate's evidence read a unit inside the implementer's write scope that is not in the execution basis, such as a docstring module or a test note. The obligation cannot be discharged, so §7.10 issues a new iteration whose brief carries the review findings as data. The iteration touches that unit. Under §6.9 (“A frame-`X` record counts for `X'` only if every one of its entries holds, in its role, in `D_n[X']`”), `a−` is inapplicable in `D_n[X']`, while a passing assessment, carried over or fresh, is not affected. The candidate integrates unqualified. This defeats §7.6 item 6, “No implementer grades its own exam”, without any `VIOLATION`.
- *Missing dependency knowledge proves independence.* Where the assessment kind's mechanical minimum includes a closure and no completeness judgment exists in the chain, the basis is the whole governed tree (§6.5 fallback, the expected state of a newly adopted legacy repository). Any admitted change anywhere makes `a−` inapplicable. Both assessments go stale, and the claim's outcome is decided by whichever realization is reassessed first. This reverses §6.5's own rule, “Missing dependency knowledge never proves independence”, in the permissive direction.
- *Admission currency gates adversity.* §6.8 step 6 routes a failing assessment whose read unit moved during its task to revalidation as stale, and does not admit it. Reports and challenges are exempt precisely so that what was found is not lost (`f3608f5` Blocker A), but an assessment is neither. A passing assessment admitted alongside yields `T` until the failing one is redone.
- *An interpretive premise moved.* The oracle or tolerance subject moves. Both assessments are stale, and the failing realization `ρ2` stays current. If `ρ1` is reassessed first and passes, the claim is unqualified while `ρ2`'s meaning under the new oracle is unknown. The outcome depends on reassessment order. §22's oracle (“must not qualify the claim at all … whose oracle subject moved”) would certify this.

**A2 — disposal by an unrelated premise.** `a−`'s record-mode basis holds a completeness judgment `k` used by its closure, or an earlier assessment it relied on. A challenge against `k` is upheld by an independent adjudicator: the boundary completeness missed an undeclared prerequisite. By the third disposition bullet, that upholding disposes of `a−` while it stays in force and uncontested, which is permanently. `a+` also loses currency through `k`, but an ordinary reassessment with a corrected context restores it. `valid(s)` is then `T`, with `a−` disposed although no record judged the failing observation. The adjudicator judged `k`, not `a−`. The parenthesis “(a revoked realization premise)” states the intended case, but the rule covers every record premise.

**What it violates.**

- The [evidence owner, Applicability][evidence]: “A valid failing observation is evidence.” “Use `review-required` when applicability is uncertain.” Its applicability dimensions: “Where material, applicability must be recoverable over evidence-spec revision, subject/candidate, governed-claim revision, input/validity regime, oracle semantics, environment/backend/precision/configuration, stochastic replicate identity and protocol obligation.” An assessor's context reads, declared reliance, widened closure and completeness premises are none of these.
- Its Assessment disagreement section: “Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position. […] supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement. An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.” A1 ends the disagreement by an unrelated edit; its siblings resolve it by reassessment order; A2 resolves it by an adjudication that never judged it.
- “Do not suppress contradictory admissible observations to manufacture a pass.”
- The candidate's own rules: S4 (“failing evidence that **may still apply** keeps the claim qualified until disposed of”); §1.2 (“mechanically decidable only conservatively -> […] sound over-approximation (never under-approximation)”); §6.5; §7.6 item 6.

**Why this is D3, not Manual.** §6.4 fixes at D3 that every record's basis contains its recorded reads and declared reliance, and §6.6 fixes `applicable` over every entry. Manual item 4 composes the mechanical minimum per kind. It cannot drop reads from assessment bases without weakening K1 for *passing* assessments, whose currency rightly depends on what their assessors read. One basis is asked to be conservative in opposite directions: broad for the currency of support, narrow for the applicability of adverse evidence. Only D3 can separate the two.

**Earliest owner.** D3 §6.6: `applicable`, `adverse` and the disposing relation, with §6.8 step 6, §10, the §15.4 disagreement row, §22 and §27.18 regenerated from it. Not the evidence owner, not a Manual detail, not D4.

**Minimum repair direction.** Name at D3 the *evidentiary premises* of an assessment. Compute them mechanically at admission, as §6.9 computes entry roles:

- the realization record, and through it the target and execution entries;
- the evidence specification's revision;
- the oracle and tolerance subjects the specification names.

Then:

- Test adversity over those premises only, with equivalence counted by existence as now.
- Treat every other entry as provenance for adversity, as §6.8 step 6 already treats a report's basis. That covers context reads, harness-observed reads, declared reliance, the widening closure and completeness records. A move of one of them may end the assessment's *currency* and raise a reassessment obligation, but it never removes adversity.
- Where an interpretive premise (oracle, tolerance or specification) moves while the realization stays applicable, keep the failing assessment adverse (`review-required`) until an authorized reassessment of that realization supersedes it.
- Let premise disposal come only from an upheld challenge against the realization or another evidentiary premise.
- Admit, or keep visible through its realization, a failing assessment whose non-evidentiary context moved during its task.

No record kind, store, stratum or component is needed. `applicable` stays a syntactic S0 relaxation over strictly earlier records, and S2 stays monotone.

**Required discriminators.** Through real Admission, Derivation, discharge and inspection consumers:

- Live PASS and FAIL; a unit read only by the failing assessor is edited without equivalence. The claim stays qualified and labelled `disputed`, and the adjudication obligation stays open. Contrasts: the same edit to a unit read only by the passing assessor (the passing assessment goes stale); an execution edit without equivalence (genuinely not adverse).
- The implementer-iteration sibling, end to end: an iteration touching only a unit the failing reviewer read is never integrated unqualified.
- An `UNBOUNDED` assessment basis with an unrelated admitted change, with reassessment order varied: the outcome is order-independent and qualified until the failing realization is reassessed or disposed of.
- An oracle move with the passing realization reassessed first: qualified until the failing realization is reassessed.
- An upheld challenge against a completeness judgment in `a−`'s basis disposes of nothing. Contrast: an upheld challenge against `a−`'s realization disposes of it.
- A failing assessment submitted after a context unit it read moved keeps the claim qualified.
- §22's “must not qualify … whose oracle subject moved” rewritten to match the repair.
- The model check extended with per-entry premise classes and record premises of more than one kind. Its oracle must be written without reusing `applicable`, `disposers` or `stands`, and a sensitivity mode must reproduce revision 12.

## 2. Non-blocking findings

### N1 — historical governing-version adoption remains partly evidenced

Unchanged from `97e753f` N1. The 2026-10-12 adoption instruction is still a paraphrase (§0.4; stakeholder record, Not covered). The handoff independently binds this Review to 7.2.1. Earliest owner: §0.4, pending stakeholder restatement.

### N2 — the model check's oracle is a second transcription of the same predicates

`oracle_unqualified` and `stands` call the same `applicable`, `disposers`, `in_force`, `cont` and `contested` methods as the lattice. They are therefore checked against the same notion of applicability and disposal they are meant to test. Under `REV11=1` the owner-grounded properties P1-P4 report **0** failures; all 1871 failures come from `O`, the oracle written in revision 12's terms. The `REV11` sensitivity therefore shows only that revision 11 differs from revision 12, not that it violates an owner property. `applicable` models execution moves only. The model has no context entries and no realization or completeness premises, and represents the basis of an `IMMATERIALITY` judgment as one governing-subject bit. Green and A therefore coexist (PEM DS-001). Earliest owner: §22 and the model check; repair with A.

### N3 — independence wording for dispositions, and the self-supersession exemption

§6.6 requires independence “against the claim's author”. §6.8 step 3 requires lineage “disjoint from the author's” for “every disposition of another actor's failing assessment”, which an implementer could read as the *assessor's* author. §6.6 also lets “a failing assessment's own assessor […] supersede it as an ordinary reassessment”, and step 3 does not list evidence assessments among the judgments that need independence. If the claim's author may assess its own claim's evidence, it can reverse its own failing assessment with no independent judgment, which conflicts with A9. Earliest owner: one sentence at §6.6 and step 3, with Manual items 3 and 23 (assessment qualifications).

### N4 — a disposition's reliance on the failing assessment should not be currency-bearing

If an `IMMATERIALITY` judgment, or a superseder, holds `a−` in `record` mode, then a blocking challenge filed against `a−` makes the disposition non-current and re-qualifies the claim. This is restrictive, so not unsafe. But it means challenging failing evidence *increases* that evidence's effect. `identity` mode, which §6.4 already uses for targets, is the natural assignment. Earliest owner: Manual item 4.

### N5 — the D1/D2 disagreement floor also fires on inapplicable failing evidence

§7.9 creates human attention for any admitted failing assessment beside any admitted passing one, including failing assessments on long-superseded code. This is restrictive and keyed correctly on existence, but it feeds the §26 human-attention-volume trigger. The Manual (item 26) may scope the floor by an immutable fact, such as applicability when the assessment was admitted, without making it currency-keyed.

### N6 — edit-and-rerun as sampling until pass

A non-equivalent trivial edit to execution content legitimately makes a stochastic failing realization stale, and the rerun is a fresh sample. Repeated, this is a lawful route to a pass for stochastic specifications. Manual item 11 (assessment granularity) should make ensemble acceptance independent of the latest single replicate. The §26 trigger already names routine disagreement.

### N7 — “conservative” is claimed in the wrong direction

§0.1 calls `applicable` “a conservative S0 over-approximation per claim and evidence obligation”. It over-approximates *currency*, which is conservative for support and the opposite for adversity. This is editorial and is repaired with A.

## 3. Re-verification of previous Reviews' findings

“Closed” means the named deductive trajectory is excluded by the candidate's contract, not executed qualification or acceptance.

### 97E753F

| Finding | Disposition | Basis |
|---|---|---|
| A — equivalence-covered key split; §6.6 vs §7.4 | **Closed** for the named trajectories | The key is removed; an admitted equivalence keeps `a−` applicable; one `ev(s, e)` term is read by `valid` and §7.4. Discriminator “A” gives `P`; contrast gives `T`. The replacement mechanism has its own defect (A above) |
| B1 — stale disposition | **Closed** | `eff(d) = current(d)` for support-tier dispositions, read positively; discriminator “B1” gives `P` |
| B2 — upholding under an open blocking counter-challenge | **Closed** | `contested(d)` ignores counter polarity; revocation keeps S1 polarity; discriminators give `P`, then `T` after dismissal |
| N1 adoption provenance | **Partly closed** | N1 above |
| N2 §15.4 supersession row; double supersession | **Closed** | The row now defers dispositional effects to the next row; re-disposal and chains are specified (§6.6) |
| N3 “S4 by construction” | **Partly closed** | The restrictive residue is gone (a moved oracle makes `a−` inapplicable), but the repair overshoots into the permissive direction (A1 interpretive-premise sibling; A2) |
| N4 D1/D2 attention keyed on a predicate | **Closed** | Disagreement floor keyed on the failing assessment's existence (§7.9) |
| N5 decision class and independence | **Closed**, with wording residue | R2 independent, R3 for D1/D2 (§6.6, §7.5, step 3); see N3 |
| N6 step 8 overbroad | **Closed** | Scoped to content and structural changes; admitted evidence is never collateral regression |
| N7 per-replicate assessment | **Closed as routed** | Manual item 11 and §26; see N6 |

### Earlier Reviews

The `97e753f..4c35d92` diff touches §0, S4, §6.6, §6.8 steps 3 and 8, §7.4, §7.5, §7.9, §10, the §15.4 disagreement rows, §21 items 3, 5 and 11, §22, §26, §27.18-§27.19 and §28. It touches no persistence, publication, frame, intake, migration, component or inheritance section.

- **124B0B7 A** (a challenge or loss ends a dispute): **closed**. Model-check P1 and P2 are green to depth 5, and the named discriminators “open challenge against the failing assessment” and “loss with both assessments retained” give `P`.
- **FB3E542 A** (prospective acceptance reused after restoration): **closed**; `bind(j)` is unchanged.
- **FB3E542 B** (current PASS selected beside a competent FAIL): **partly closed**, through A.
- **FFBAD17 A** (S1 polarity): **closed**. S1 is unchanged, and P3 and P4 are green to depth 5.
- **Strata.** `applicable` reads only the observed tree, effective structure and record syntax, and recurses on strictly earlier records, so it is well-founded S0. In S2, `current(d)` enters `undisputed` only through `P ∨ ·` and `max`, and upholding effects are S1 constants. S2 is monotone, the least fixed point is unique, and the one-pass topological claim holds with dispositions as static support edges.
- **Cycle protection.** The f9d9de8 configuration and mutual-validity cycles remain rejected by step 5 and evaluate to `F`.

The remaining 730490D, AC71FA9, F3608F5 and FFBAD17 closures that the `97e753f` record lists do not depend on the changed text and remain **closed**. FFBAD17 N7 (inherited index and whitespace residue) remains outside this scope.

## 4. Out-of-matrix trajectories attempted

| Attempt | Result |
|---|---|
| Edit of a unit only the failing assessor read, no equivalence | **Fails** (A1); reproduced with the candidate's ledger class extended by one context entry |
| Implementer iteration touches a unit the failing frame reviewer read | **Fails** (A1 sibling) |
| `UNBOUNDED` assessment basis, unrelated admitted change, reassessment order varied | **Fails** (A1 sibling; outcome order-dependent) |
| Failing assessment whose context moved during its task, at step 6 | **Fails** (A1 sibling; routed to revalidation, not admitted) |
| Oracle moves; passing realization reassessed first | **Fails** (A1 sibling; order-dependent) |
| Upheld challenge against a completeness premise of `a−` | **Fails** (A2) |
| Upheld challenge against `a−`'s realization | Holds: correct disposal |
| Equivalence-covered execution move, passing rerun; editorial claim revision with equivalence, either order | Holds |
| Non-equivalent execution move, rerun | Holds as designed (genuinely stale); N6 for stochastic specifications |
| `IMMATERIALITY` whose prerequisite moves; stale superseder; re-disposal through a chain | Holds |
| Upholding under an open blocking counter-challenge; under an open non-blocking one | Holds; the non-blocking case keeps the disposition by design (no S1 effect) |
| Frame-`X` superseder of an admitted `a−`, `X` never integrated | Holds: `eff = F` in `D_n`, and `a−` stays adverse |
| Spurious, challenged or self-declared equivalence | Holds: restrictive only |
| Blocking challenge filed against `a−` after an `IMMATERIALITY` judgment | Restrictive inversion if the judgment holds `a−` in record mode (N4) |
| Claim's author as `a−`'s assessor reverses it by self-supersession | Open wording (N3) |
| Disposition whose validity basis leads back to the claim | Holds: step 5 rejects it |
| Adverse assessment admitted against another subject's discharged obligation | Holds: step 8 scoped |
| Agent disposition of a D1/D2 dispute | Holds: R3, and human attention keyed on existence |
| Loss boundary with both assessments retained; pre-boundary disposition not re-recorded; positive-only attestation | Holds |
| `applicable` or `disputed`-like terms read antitonically in S2 | Holds: no antitone read |
| Workflow layer: role overstep, task partition, tightening then loosening, floor downgrade; publication: paused publisher, two fences, foreign return to `B_n` | Holds as recorded by earlier Reviews; untouched by revision 12 |

## 5. Minimum architecture, capability transfer and inheritance

**Minimality.** Revision 12 is a genuine simplification. It removes the assessment key and three S1 predicates, keeps S2 monotone and adds no primitive, record kind, store or component (§27.19). Repair A needs none either. It needs a mechanical classification of an assessment's basis entries, of the kind §6.9 already performs for frame roles, and a narrower disposing relation.

The convergence owner's progression puts this family past post-simplification recurrence. Three successive proxies for “failing evidence that may still apply” have each failed permissively. The earliest affected abstraction is that proxy, and the owner already supplies the non-proxy definition: its enumerated applicability dimensions together with `review-required` under uncertainty. The effective-disposition half should be kept as it stands. Practical minimality otherwise remains conditional on the empirical items of §26.

**Predecessor comparison.** Revision 12 did not touch §16.2 or §18. Blobs verified at the candidate:

| Predecessor | Blob |
|---|---|
| befe678 hypothesis archive | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |
| Consolidated Protocol 8 plan archive | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| Orchestrator Architecture 1.6.0 (equal at public source and candidate) | `39e6de727f6c35402962509d30d947962992eaad` |

The frozen Core profile resources `ssdp-protocol-6.6`, `7.0`, `7.1` and `7.2` are present at the candidate, consistent with PC-001 and §24. The bounded semantic comparison of §16.2 and §18 recorded by earlier Reviews still holds by identity.

**PEM basis and HAS.** Project instructions designate `main` as the integrated publication line. The local tracking ref `origin/main` is `af0455753e20ee54a969c844872e29e270007211`, equal to the workplan's basis. Its `PROJECT-ENGINEERING-MEMORY.md` blob equals the candidate's, `1561797125622f355f84eb27319f87e8fa4227d9`. There is no branch overlay. The uncovered later interval proves no absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: The model check and its plain-language oracle share the predicates under test, and stay green while A holds.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen profiles required through the versioning owner; present at the candidate; preserved by §24.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy; repair the one canonical adversity owner (§6.6) and regenerate §6.8 step 6, §10, §15.4, §22 and the check from it.
  - id: SP-002
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: Self-reference-safe identity unchanged by revision 12.
  - id: FF-001
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: No immutable publication in scope; remains applicable to later genesis and release.
```

**7.2.1 reconciliation.** The release state at the candidate names 7.2.1 accepted-current, with distinct public source `aaeaf8b6…` and recovery `efdd1b59…`. The `97e753f..4c35d92` diff changes no `source/`, `dist/`, `orchestrator/`, release-state or PEM path, and no §0.4, §19 or §24 text. The `97e753f` record's owner comparison between `22f4bdba` and `aaeaf8b6` therefore still applies, and the §0.4 obligation table and the §19 landing points stand. The one place where the inherited evidence doctrine is not yet realized is A.

## 6. Qualification-program adequacy

§22's disagreement group now enumerates the `97e753f` discriminators and requires `valid` and §7.4 to agree on every generated ledger. That closes the earlier gap. It still cannot discriminate A:

- It has no case where a non-evidentiary basis entry of the failing assessment moves.
- It has no case of disposal through a non-realization premise.
- Its oracle “must not qualify the claim at all … whose oracle subject moved” would certify the interpretive-premise sibling.

The bounded model check is honest about its status, but its sensitivity against revision 11 rests only on an oracle phrased in revision 12's own predicates (N2). The [testing owner][testing] asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Revision 12 with a context-sensitive `applicable` is such a concretization. Add the discriminators named under A, and give the oracle an independent statement of adversity.

The four consolidation tests establish frontmatter and routing only. HARD-template thresholds, mutation strength, evaluator calibration, custody, blinding, paired baselines and doctrine-realization measurement remain later-gate obligations (§22-§25). No campaign was run and no improvement estimate is asserted.

## 7. What was verified and how

- **Candidate identity.** Resolved the candidate SHA and workplan blob `7f18ae39…`. Extracted a `git archive` of the exact candidate into a scratch directory; later commits, including the handoff commit `9f2e037`, were excluded.
- **Owners read** at `aaeaf8b6` with `git show`: the D3 role entrypoint; architecture; evidence (Applicability, binding health, Assessment disagreement, applicability dimensions); testing (oracle strength); convergence (core progression, family routing, review strategy after recurrence); the kernel's Challenge text; and the workflow owner's independence and common-mode text.
- **Candidate read.** §0-§2, §5-§7.10, §8, §9, §10, §15.4, §21, §22, §26, §27.18-§28 in full; the full `97e753f..4c35d92` diff; the stakeholder record; the authority-index SSDS 8 section diff; the routing test; and the model check.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the archive: **4 passed, 0 failures, 0.021 s**, Python **3.13.16**.
- **Whitespace.** `git diff --check 97e753f8… 4c35d92d…`: **exit 0**, no diagnostics.
- **Model check** (default depth 5):
  - default mode: **81 171 transitions, 0 failures, 11/11 discriminators as expected, exit 0**, matching §27.18;
  - `REV11=1`: **1871 failures, all in `O`, with P1-P4 = 0**; four discriminators differ; **exit 1**;
  - `REV10=1`: **5033 failures (P1 620, O 4413)**; five discriminators differ; **exit 1**.
- **A1 reproduction.** A scratch subclass of the candidate's `Ledger`, loaded read-only, adds one context entry to failing assessments and one event editing it. Live dispute: `ev = P`. After the edit: `ev = T`, and `oracle_unqualified = True`. This is diagnostic arithmetic only, kept outside the repository.
- **Identities.** Verified the predecessor blobs, the release-state identities, the frozen-profile presence, the PEM blob identity and the changed-path list above.
- **Repository untouched.** No candidate, source, distribution, index, release state, PEM or frozen resource was changed. The only repository output is this record. Nothing was committed or pushed.

**Scientific inquiry envelope.** Examined architecture-mediated evidence applicability, disagreement, disposition, closure and frame integration. Materiality here is the ability to change support, closure or the next authorized action. No physical or numerical result is asserted. One pinned candidate was reviewed through multiple deductive trajectories; no variant search over scientific analyses was performed and no delegates were launched. The judgment relies on accepted engineering and evidence doctrine, not on project D1/D2 authority, so the tension-search duty was not triggered.

## 8. What could not be verified

- **PEM schema validation.** `source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, on the working-tree file whose blob equals the candidate's, failed with `UNAVAILABLE: repository revision is not resolvable as an immutable object` for historical evidence routes (`55c08526…`, `81375d81…` and others). This checkout is a **shallow clone** (`git rev-parse --is-shallow-repository` = `true`). That is an environment limitation, not a PEM defect and not a pass. The blob is unchanged since the `124B0B7` record's passing validation.
- **Remote state.** `origin/main` is the local tracking ref. No fetch was performed and no remote-state claim is made.
- **Assessment-kind composition.** Whether the evidence-assessment kind's mechanical minimum includes a dependency closure, and so completeness records, is a Manual decision (item 4). The `UNBOUNDED` sibling of A1 and the completeness instance of A2 are therefore conditional on it. A1's primary trajectory, which needs only a recorded read, is not. Neither is A2 in general: it applies to any record premise, including an earlier assessment.
- **Runtime evidence.** No SSDS production owner, witness deployment, harness adapter or Architecture Manual exists. Runtime fidelity, read recording per harness, failure injection, lineage attestation, privacy enforcement, scaling and burden reduction remain unexecuted (§21-§26), and none is counted as a pass.
- **Repository acceptance.** The full repository regression, package build and validation, distribution parity, frozen-resource census and Core snapshot tests were not rerun. This Review changes no protocol source or descendants.

## 9. Common-mode dependency

This reviewer is a fresh-context sub-agent **of the same model family as the author** (Claude), launched by the authoring session from a handoff the author wrote, under stakeholder SD-8. That is a material common-mode dependency: shared blind spots, framing inherited from the handoff's scope list, and the same corpus and toolchain are all plausible.

The handoff gave no author conclusions. This record supplies **no different-family corroboration**. The design's own §9.6 lets policy require that for high-consequence surfaces, and the stakeholder has waived it for this cycle. A PASS from this cycle would still need the owner adjudication and production evidence of later gates ([workflow, Optional independent cognitive trajectories][workflow]).

## 10. D4 statement

**D4 remains NOT AUTHORIZED.** Phase B Review is NO-PASS. The next step is the owning D3 reconsideration of which premises carry adversity (§6.6, with §6.8 step 6, §10, §15.4, §22 and the model check regenerated from it) and a replacement immutable candidate. Even a later Phase B PASS authorizes nothing by itself:

- G1 needs the accepted Manual and explicit stakeholder acceptance of the major change.
- G2 needs a separately reviewed shadow workplan and stakeholder authorization.
- G3 needs real-owner implementation evidence.
- G4 adds per-subject cutover, quiescence and rollback (§23-§25).

This Review grants no Manual acceptance, implementation permission, spend release, cutover, ratification or promotion.

[wp]: https://github.com/hjin98/scientific-software-development-system/blob/4c35d92d2c75c9961d4d3b97c35c6dfad04c6336/workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
[kernel]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md
[workflow]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md
[evidence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/evidence-evolution-and-dependencies.md
[testing]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md
[convergence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md
