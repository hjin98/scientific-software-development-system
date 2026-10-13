# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 13

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 644eb7262f01752a0d8059f32e38a1fb8b9c99ea
    SCOPE: whole proposed architecture; (a) the revision-13 repairs: fixed roles for the
           evidence owner's applicability dimensions, the S0 predicate `bears` over evidentiary
           premises, the narrowed disposing relation, the step-6 admission of failing
           assessments, independence and identity-mode reliance of dispositions, the scoped
           D1/D2 floor, and the rewritten bounded model check (independent oracle, P5, P6, Q,
           discriminators, sensitivity modes); (b) workflow execution and verification layer
           and the doctrine-realization objective; (c) persistence, derivation, concurrency and
           migration; (d) Protocol 7.2.1 inheritance reconciliation
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: ff78959d8ba7dd4e85bd91a585a67128fea4b24c (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5,
           AC71FA9, 730490D, FB3E542, 124B0B7, 97E753F, 4C35D92; all NO-PASS
    REVIEW METHOD: immutable-owner reconstruction; attack of each revision-13 repair as a
           new mechanism, by enumerating every route by which a submitted or admitted failing
           assessment can stop affecting validity (bearing, disposition, admissibility,
           obligation, Admission, frame, loss) and testing whether each is an evidentiary move
           or an accountable disposition; cross-stratum, frame and Admission-boundary attacks;
           prior-finding re-derivation; qualification-method challenge; exact-candidate
           structural tests and bounded model check in all requested modes
    REVIEWER: Claude Opus 5.5 (model id claude-opus-5-5), a fresh-context sub-agent launched
           by the authoring session from REVIEW-HANDOFF-SSDS-8.0-REVISION-13.md (stakeholder
           SD-8); same model family as the author
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-644EB72-NO-PASS.md

Candidate section references below mean the [primary workplan at the candidate][wp]. Governing-owner links pin the public source above. This context authored neither the candidate nor any prior Review, received none of the authoring conversation, and treated the handoff's scope description, the workplan's self-assessments (§0.1, §27.20-§27.21), the model check's green result and every prior verdict as hypotheses.

The blockers below are deductions from the proposed contracts, not observed SSDS runtime failures. Their asserter is the reviewer named above; their disposition is **OPEN** against the exact candidate. This record is their canonical home. Revisit after the D3 owner closes the two boundary routes named below (§6.8 steps 6-7; the protocol-obligation row and decision class of §6.6), regenerates §0.1, §22, §27 and the model check from them, and freezes a replacement candidate. No accepted project scientific D1/D2 claim is challenged.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The [kernel][kernel] says: “A coherent parent with a wrong child is an ordinary blocker.” The governing [evidence owner][evidence] is coherent and realizable here. It names the applicability dimensions, says “A valid failing observation is evidence”, requires `review-required` when applicability is uncertain, forbids resolving a disagreement by “serialized record position”, and requires that “supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement”. A D3 design that admits every competent failing assessment and lets it stop counting only by an evidentiary move or an explicit disposition satisfies all of these together. Revision 13's predicate already does this for admitted assessments whose obligation persists. Both blockers below lie at its boundaries and belong to the proposed D3 concretization.

The stakeholder record supports what the workplan attributes to it. SD-5 and SD-6 accept the revision-5 principles and an aspiration that is measured, not claimed. SD-8 quotes the 2026-10-13 instruction verbatim (“until all remaining blocking issues are closed”) and directs a same-family sub-agent cycle. Nothing in the candidate claims that a sub-agent PASS accepts the architecture. Acceptance of objectives, product scope and the major change stays with the stakeholder (§25 items 11-12; [workflow owner][workflow]).

## Verdict

**NO-PASS.** Two blockers remain, both at the boundaries of the revision-13 mechanism:

- **A — Admission still loses competent failing assessments.** Step 6 exempts a failing assessment from its own currency check, but its salvage clause and step 7's legality exemption still cover only reports and challenges. A failing assessment submitted together with any stale record of its task (in practice, always its task result), or bound to a contract revision that was tightened or an obligation that a passing assessment discharged first, is routed to revalidation and not admitted.
- **B — retiring the evidence obligation ends a live disagreement without a disposition.** `valid` reads `ev(s, e)` only for currently required obligations. An accepted specification change that removes, splits or retargets the obligation drops a bearing, undisposed failing assessment from validity, although §6.6 says a specification move leaves it adverse, and although a disposition of a D1/D2 disagreement must be R3.

Revision 13 genuinely closes the `4c35d92` blocker family on its stated trajectories. `bears` over the owner's dimensions is the first non-proxy formulation, the effective-disposition half is unchanged and sound, and S2 stays monotone. Neither blocker needs a new mechanism. Each is closed by one rule that puts the boundary route into the class of either evidentiary moves or dispositions.

Requested checks: the four routing tests pass; `git diff --check` is clean; the model check is green at depths 4 and 5 and red under `REV12=1`, `REV11=1` and `REV10=1`, each failing at least one owner-grounded property. None of them models Admission or obligations, so none discriminates A or B (§6 below), and none establishes semantic adequacy.

## 1. Blockers by earliest owner

### A — failing assessments are still lost at Admission

**Owner text at the candidate.**

- §6.8 step 6: “**Reports and challenges are exempt** (`f3608f5` Blocker A), and so are failing assessments (`4c35d92` Blocker A): […] so one whose context moved during its task is admitted rather than lost, and S2 decides its currency. […] When a request is routed to revalidation, the admission record that rejects it still admits **the report and challenge records** it carries, bound to the same task, so nothing reported is lost with the rejected work”.
- §6.8 step 7: “A task result or discharge claim bound to an obligation already discharged, or to a contract revision that is no longer current, is recorded with that classification and routed to revalidation; it is not admitted as current work. **Reports and challenges** are admitted whatever the state of their task, so nothing reported is lost.”
- §9.1: `submit(result)` carries the “outcome classification from the task's allowed set”, and machinery supplies “reads, basis”; `read(ref)` is “recorded into the basis”. §7.8 item 2: “A reviewer task (§9.6) submits its review and conformance judgments as a records-only request bound to the review task”. §7.2: “tasks whose basis names a changed item become non-current”.
- The candidate's own closure claims: §0.1, “Admission step 6 admits failing assessments whatever the currency of their context”; §27.20, “Failing assessment whose context moved during its task | Admitted under the step-6 exemption; adverse”.

**A1 — co-submitted stale record (step 6).**

1. Claim unit of subject `s`, evidence obligation `e`. The designated runner realizes `ρ1` (seed 1) and `ρ2` (seed 2). Assessor `X`'s PASS `a+` on `ρ1` is admitted and current.
2. Reviewer `Y` reads a context unit `w` through the interface, assesses `ρ2` FAIL (`a−`), and submits. Machinery builds one records-only request from that submission. It carries `a−` together with the task's own non-exempt support-tier records: the task result that every `submit` produces and, for a review task, the review judgment. Each has `(w, w0)` in its basis.
3. Before Admission reaches the request, an unrelated admitted integration moves `w` to `w1`.
4. Step 6: `a−` is exempt, but the task result and the review judgment are not, and they are stale. The request is routed to revalidation. The rejecting entry admits only “the report and challenge records it carries”. `a−` is not admitted.
5. `adverse(s, e) = ∅`, so `ev(s, e) = T`, and `valid(s)` and §7.4 discharge are unqualified. Nothing is labelled `disputed`, no adjudication obligation is derived, and for a D1/D2 claim no floor item exists, because the floor is keyed on an *admitted* failing assessment.
6. Revalidation re-issues `Y`'s task at best. A fresh execution may assess `ρ2` PASS, since assessment is judgment. The competent failing assessment then never enters canonical state, and the disagreement has been settled by which record survived Admission.

The exemption therefore helps only a failing assessment submitted alone. In this design that is the exception, because every `submit` produces a task result whose basis carries the task's reads and contract revision.

**A2 — task state (step 7).** Either of two locally compliant events suffices:

- *Contract tightening.* While `Y` works, the principal admits an R1 control-tightening amendment of the item (§7.9), for example a secondary `HARD` check. `Y`'s task is now bound to a contract revision that is no longer current. Step 7 routes its request to revalidation, and only reports and challenges are admitted.
- *Discharged first.* `Y`'s task is bound to an evidence or assessment obligation that `X`'s passing assessment discharged first. `Y`'s later failing assessment is bound to “an obligation already discharged” and is not admitted. There is no undischarged obligation left to re-issue, so the loss is permanent, and the outcome is decided by admission order.

**What it violates.**

- The [evidence owner][evidence]: “A valid failing observation is evidence.” “Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position.” “Do not suppress contradictory admissible observations to manufacture a pass.”
- The candidate's S4 (“failing evidence whose realization still bears on the claim keeps it qualified until disposed of, whatever else in its assessor's context moved”), and its own closure claims in §0.1 and §27.20.
- The same defect class as `f3608f5` Blocker A, which the candidate closed for reports and challenges at *both* steps, by both clauses. Revision 13 added failing assessments to step 6's first sentence only.

**Earliest owner.** D3 §6.8 steps 6 and 7. Request shape (§7.8, §9.1) is D3 too. It is not Manual: the list of record kinds that survive a rejected request is D3 text.

**Minimum repair direction.** Put failing assessments in the never-lost class wherever reports and challenges are:

- the step-6 salvage clause admits them from the rejecting entry, bound to the same task;
- step 7 admits them whatever the state of their task, contract revision or obligation.

S2 already decides their currency, and `bears` already decides their adversity, so nothing else changes. No record kind, stratum or component is added.

**Required discriminators**, through real Admission, Derivation, discharge and inspection consumers:

- a failing assessment co-submitted with the task result (and review judgment) made stale by a moved context unit: the rejecting entry admits it, and the claim is qualified and labelled `disputed`;
- a failing assessment whose task's item was control-tightened during the task;
- a failing assessment bound to an obligation discharged by a passing assessment admitted first, with admission order of the two requests reversed: the outcome is order-independent;
- §22's existing case (“a failing assessment submitted after a context unit it read moved”) restated so that it carries the task result, not a failing assessment alone.

### B — retiring the evidence obligation ends the disagreement without a disposition

**Owner text at the candidate.**

- §6.6, role table: “protocol obligation | the evidence obligation `e` | assessments for different obligations never conflict”; and “evidence-specification revision; oracle and tolerance semantics | **interpretive premise** | none on adversity: the observation still stands and its meaning is uncertain, so it stays adverse (`review-required`) until its realization is reassessed or judged immaterial”.
- §6.6, `valid(s) = … ∧ ⋀_{required evidence obligation e} ev(s, e)`; §6.6, “Decision class and independence”: “`IMMATERIALITY` judgments, and supersessions or adjudications that dispose of another actor's failing assessment, are R2 (§7.5); for a claim unit that is D1 or D2 authority they are R3.”
- §7.1: derived obligations include “an evidence specification without a current admissible realization for its claim”, with identities “derived from `(rule, subject)`”. §10: a specification is an “evidence unit with `EVIDENCES` -> claim unit”. §6.2: authored relations “take effect when that subject's revision is accepted”.
- §7.6: the contract field `evidence_specs` names “evidence-specification units the item may change”, and item 6 says that a change to a named evidence specification “raises its owner's specification-review obligation”.

**Trajectory (every step locally compliant).**

1. A live disagreement on obligation `e` of claim `c`, from specification `σ` with `σ EVIDENCES c`: `ev(c, e) = P`. `a−` bears, nothing disposes of it, and an adjudication obligation is open.
2. An item contract names `σ` in `evidence_specs`, which lint permits. Its implementer revises `σ`. It removes the `EVIDENCES -> c` relation, or splits `σ` into a new unit `σ'` that carries the same tests under a new identity, or retargets it. The revision raises `σ`'s specification-review obligation. An independent R2 reviewer accepts `σ`'s new revision on the specification's own merits. Nothing in that judgment names `a−`.
3. Once that revision is accepted, `e` is no longer a required evidence obligation of `c`, or it has become `e'` with a new `(rule, subject)` identity. `valid(c)` reads no `ev(c, e)`. `a−` is still admissible for `e`, still bears (its realization's claim revision and named execution content have not moved), and is still undisposed. Yet `valid(c) = T`, and §7.4 discharge of `c`'s obligations is unqualified.
4. The interpretive row promised the opposite outcome for a specification revision. For a D1/D2 claim the disagreement has been ended by an R2 acceptance of an evidence unit, while every disposition of it must be R3. The D1/D2 floor item survives because it is keyed on existence, but validity and discharge are unqualified meanwhile.

The candidate does not say whether `undisputed` still ranges over an obligation that has stopped being required. One implementer will drop it, as the equation reads. Another will keep it, which the role table implies. That is a choice between two readings of the same owner, with opposite permissiveness.

**What it violates.**

- The [evidence owner][evidence]: “An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.” “When a durable representation stores multiple assessments, supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement.” Its retirement rule: an artifact is ordinarily retireable only when “no supported current concretization/evidence/compatibility path materially depends on it”.
- The candidate's S4 and its own §6.6 decision class (R3 for a D1/D2 disposition).

**Earliest owner.** D3 §6.6: the protocol-obligation row of the role table and the decision class of dispositions. Manual item 7 composes the obligation rules, but whether leaving an obligation ends adversity is a semantic decision about disagreement, so it is D3.

**Minimum repair direction.** Choose one of the following and state it at §6.6. Either keeps S2 monotone and adds no record kind:

- *Keep it adverse.* `undisputed` for a claim unit ranges over the bearing failing assessments of every obligation that was required for that unit when the assessment was admitted (an immutable fact), not only the obligations required now. Retiring, splitting or retargeting a specification then leaves the claim qualified until a disposition.
- *Make retirement a disposition.* An accepted change that removes or renames an obligation carrying an undisposed bearing failing assessment is a disposition of it. It is then admitted only with the disposition's decision class (R2; R3 for D1/D2) and independence, and it names the failing assessment.

**Required discriminators:**

- live disagreement, then specification `EVIDENCES` removed and accepted by R2: the claim stays qualified (first option), or the acceptance needs R3 for a D1/D2 claim and is recorded as a disposition (second option);
- the same, with the specification split into a renamed unit carrying the same tests;
- contrast: an explicit standing disposition, then retirement: the claim is unqualified.

## 2. Non-blocking findings

### N1 — historical governing-version adoption remains partly evidenced

Unchanged from `4c35d92` N1. The 2026-10-12 adoption instruction is still a paraphrase (§0.4; stakeholder record, Not covered). The handoff independently binds this Review to 7.2.1. Earliest owner: §0.4, pending stakeholder restatement.

### N2 — the model check is honest and better, but cannot see either blocker

The rewrite partly closes `4c35d92` N2.

What improved:

- The oracle is separate code that does not call `bears`, `disposers` or `eff`.
- P5, P6 and Q are stated over raw ledger syntax.
- Every sensitivity mode now fails at least one non-oracle property.

What remains:

- **The oracle shares the partition.** It encodes the same role partition (only a non-equivalent `MOVE` ends bearing) and the same disposal rules as revision 13. It can catch a transcription slip, but not an error in the partition.
- **Equivalence is never challenged.** “Equivalence judgments are taken as current”, so the asymmetry the design relies on (an equivalence counts for bearing once admitted, but for support only while current) is never exercised.
- **Superseders are idealized.** Every superseder is a PASS reassessment, and every disposition is independent.
- **Out of scope:** Admission steps, obligations, frames, specification-revision admissibility and the D1/D2 floor. A and B are therefore outside the model.
- **Fidelity of `REV12`.** Its `bears` does not test record premises, as revision 12's `applicable` did.
- **Depth of the sensitivity claim.** At the script's default depth 4, `REV12=1` fails P5, Q and O, with **P6 = 0**. P6 fails only from depth 5 (16 failures). §0.1's “`REV12=1` fails P5, P6, Q and the oracle” holds at depth 5, not at the default. `REV11=1` fails only Q and O.

Earliest owner: §22 and the model check. Add the discriminators named under A and B to §22. Extend the model only if it is cheap: one challenged-equivalence event and one non-independent superseder would exercise the two rules it cannot see now (PEM DS-001).

### N3 — the independence rule for dispositions is in prose, not in the equation

§6.6 says “A disposition admitted as non-independent (§6.8 step 3) has `eff = F`”. The displayed equation gives `eff(d) = current(d)` for a support-tier disposition, and `current` does not read independence. An implementer following the equation would count a non-independent superseder. Put the condition in the disposing relation or in `eff`. Residue of `4c35d92` N3: the claim's author's own *passing* assessment still counts in `ev`, because evidence assessments are not in step 3's independence list. That belongs to Manual items 3 and 23 (assessment qualifications).

### N4 — step 6's exemption sentence now contradicts itself

After failing assessments joined the exemption, step 6 says of all exempt records: “Their basis records what the raiser saw, as provenance; it is never checked for currency and never consumed by any rule”. A failing assessment's evidentiary premises are consumed by `bears`, and S2 decides its currency. This is editorial; scope the sentence to reports and challenges.

### N5 — admissibility is fixed against the specification revision the assessor chooses to name

Admissibility is “decided against the specification revision the assessment named”. Failing assessments are now exempt from step 6. A failing assessor can therefore name a superseded specification revision under which a realization the current specification excludes was admissible. That qualifies the claim until a disposition. This is restrictive, not unsafe, but it conflicts in spirit with §22's “must not qualify the claim at all: … an environment the specification excludes”. Deciding admissibility against the specification revision the *realization* instantiated (immutable in the realization record) removes the assessor's choice. Earliest owner: §6.6, one phrase, or Manual item 4.

### N6 — the D1/D2 floor misses failing evidence that begins to bear after admission

“Bore when admitted” is immutable, as the `4c35d92` N5 repair intended. But a failing assessment admitted while not bearing can begin to bear later, through a later admitted equivalence or a revert of the named execution content. It then creates no floor item. Validity stays qualified, and any disposition of a D1/D2 disagreement is R3, so this is not permissive for validity. It does lose A8's proactive human attention. Keying the floor on “bore at some admitted position” would keep it immutable once true. Earliest owner: Manual item 26.

### N7 — provenance includes exercised but unnamed code

Execution content the specification does not name is provenance: for example, code reached through dynamic dispatch, or code reached only through an incomplete analyzer's fallback. A genuine fix there leaves the failing assessment adverse until `IMMATERIALITY` or supersession. This is restrictive by design (§27.20 records the interpretive analogue). §26's routine-disagreement trigger should name this case too, because it is the commonest route by which disposition could become routine.

## 3. Re-verification of previous Reviews' findings

“Closed” means the named deductive trajectory is excluded by the candidate's contract, not executed qualification or acceptance.

### 4C35D92

| Finding | Disposition | Basis |
|---|---|---|
| A1 primary — edit of a unit only the failing assessor read | **Closed** | Context reads are provenance (§6.6 table); `bears` tests only evidentiary premises; discriminator “4c35d92 A1” gives `P`, contrast gives `F` |
| A1 — implementer iteration | **Closed** | In `D_n[X']` the named execution content holds in its role; the read unit is provenance (§6.6, §6.9) |
| A1 — `UNBOUNDED` basis | **Closed** | “The fallback of an incomplete execution closure … is provenance” |
| A1 — step-6 rejection | **Partly closed** | A failing assessment submitted alone is admitted. With a stale co-submitted record, or at step 7, it is not (blocker A) |
| A1 — interpretive move, order-dependent reassessment | **Closed** | Specification, oracle and tolerance are interpretive: adverse until reassessed or `IMMATERIALITY`; discriminators give `P`, then `T` |
| A2 — disposal through an unrelated premise | **Closed** | Only an upholding against `a−` or `real(a−)` disposes; discriminator “A2” gives `P`, contrast `T` |
| N1 adoption provenance | **Partly closed** | Unchanged (N1) |
| N2 oracle reused predicates | **Partly closed** | N2 above |
| N3 independence of self-supersession | **Closed in prose** | §6.6 and step 3; equation residue (N3 above) |
| N4 identity-mode reliance | **Closed** | §6.6, last sentence of Effective disposition |
| N5 floor on stale failures | **Closed**, with residue | N6 above |
| N6 edit-and-rerun | **Closed as routed** | Manual item 11 now states it |
| N7 “conservative” direction | **Closed** | §6.6 states the two directions explicitly |

### Earlier Reviews

The `4c35d92..644eb72` workplan diff touches §0, §0.1, S4, §6.6 (S0 bullet, Assessment disagreement), §6.8 steps 3 and 6, §7.4, §7.9 (floor), §10, the §15.4 disagreement row, §21 items 4, 5 and 11, §22, §26, §27.20-§27.21 and §28. It touches no persistence, publication, frame, intake, migration, component or inheritance section. No `source/`, `dist/`, `orchestrator/`, release-state or PEM path changed.

- **97E753F A, B1, B2: closed.** S2's `ev`, `undisputed`, `disp`, `eff` and `contested` are unchanged; their discriminators give the expected values.
- **124B0B7 A** (a challenge or loss ends a dispute): **closed**. P1 and P2 are green to depth 5.
- **FB3E542 A** (prospective acceptance reused after restoration): **closed**; `bind(j)` is unchanged.
- **FB3E542 B** (current PASS selected beside a competent FAIL): **partly closed**, through A and B.
- **FFBAD17 A** (S1 polarity): **closed**; P3 and P4 are green to depth 5.
- **Strata.** `bears` reads the realization record's evidentiary entries, which are fixed at admission, the observed tree, effective structure and admitted equivalence records. It does not read S1 or S2, so it is S0. In S2 it is a constant, and dispositions enter `undisputed` only positively. S2 stays monotone, with one least fixed point. Identity-mode dispositions add no support edge to `a−`, so the one-pass topological claim holds. The `f9d9de8` configuration and mutual-validity cycles remain rejected by step 5 and evaluate to `F`.

The remaining 730490D, AC71FA9, F3608F5 and FFBAD17 closures do not depend on the changed text and remain **closed**. FFBAD17 N7 (inherited index and whitespace residue) remains outside this scope.

## 4. Out-of-matrix trajectories attempted

| Attempt | Result |
|---|---|
| Unit read only by the failing assessor edited without equivalence | Holds |
| Implementer iteration touching only a unit the failing frame reviewer read | Holds |
| `UNBOUNDED` closure, unrelated change, reassessment order varied | Holds |
| Failing assessment submitted alone after a context move | Holds (step-6 exemption) |
| Failing assessment co-submitted with its task result or review judgment, context moved | **Fails** (A1) |
| Failing assessment whose item was control-tightened during the task | **Fails** (A2) |
| Failing assessment bound to an obligation a passing assessment discharged first | **Fails** (A2; permanent, order-decided) |
| Specification `EVIDENCES` removed, split or retargeted, accepted by independent R2 review | **Fails** (B) |
| Oracle, tolerance or specification revision move, passing realization reassessed first | Holds |
| Upheld challenge against a completeness or context premise; against the realization | Holds: disposes of nothing; correct disposal |
| Challenge against `a−` to destabilize an identity-mode disposition | Holds |
| Admitted equivalence later challenged | Holds: restrictive only |
| Byte-preserving restructure of the claim unit; non-equivalent edit of named execution content | Holds as designed: both sides stale, rerun; stochastic residue in Manual item 11 |
| Revert of named execution content to the failing realization's revision | Holds for validity (bears again); floor residue (N6) |
| Frame-`X` failing assessment, `X` never integrated | Holds: does not bear in `D_n` |
| Failing assessor names a superseded specification revision | Restrictive anomaly (N5) |
| Non-independent superseder | Holds by prose; equation silent (N3) |
| Real fix in exercised but unnamed code | Restrictive residue (N7) |
| Disposition whose validity basis leads back to the claim | Holds: step 5 rejects it |
| Loss boundary with both assessments retained; pre-boundary disposition | Holds |
| `bears` or disposition terms read antitonically in S2 | Holds: none |
| Workflow layer, publication and frame trajectories of earlier records | Hold as recorded; untouched by revision 13 |

## 5. Minimum architecture, capability transfer and inheritance

**Minimality.** Revision 13 is a further simplification. It replaces `applicable` (whole-basis satisfaction with three relaxations and record recursion) with a fixed role per owner dimension, and a test over a premise set computed at admission. It narrows the disposing relation. It adds no primitive, record kind, store or component, and leaves S2 unchanged (§27.21). Repairs A and B each need one rule and nothing else.

**Convergence.** The [convergence owner][convergence] asks that review after recurrence shift “toward bounded sibling/family closure, simplification/re-derivation, evidence-method challenge”. Revision 13 answers that for the predicate: it no longer approximates “failing evidence that may still apply” but takes the owner's own dimensions. The remaining defects are not a fifth proxy failure. They are the routes by which a failing assessment can leave validity *without* passing through the predicate at all: not admitted (A), or attached to an obligation that stops being read (B).

The next revision should close the family by enumeration rather than by trajectory. List every route by which a submitted or admitted failing assessment can stop affecting `valid` and discharge: an evidentiary move, a disposition, inadmissibility, obligation change, non-admission, a frame never integrated, and a loss interval. Then show that each one is either an evidentiary move or an accountable disposition. On this Review's attempts, only A and B fall outside. Practical minimality otherwise remains conditional on the empirical items of §26.

**Predecessor comparison.** Revision 13 did not touch §16.2 or §18. Blobs verified at the candidate:

| Predecessor | Blob |
|---|---|
| befe678 hypothesis archive | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |
| Consolidated Protocol 8 plan archive | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| Orchestrator Architecture 1.6.0 (equal at public source and candidate) | `39e6de727f6c35402962509d30d947962992eaad` |

The frozen Core profile resources `ssdp-protocol-6.0` through `6.6`, `7.0`, `7.1` and `7.2` are present at the candidate, consistent with PC-001 and §24. The bounded semantic comparison of §16.2 and §18 recorded by earlier Reviews still holds by identity.

**PEM basis and HAS.** Project instructions designate `main` as the integrated publication line. The local tracking ref `origin/main` is `af0455753e20ee54a969c844872e29e270007211`, equal to the workplan's basis. Its `PROJECT-ENGINEERING-MEMORY.md` blob equals the candidate's, `1561797125622f355f84eb27319f87e8fa4227d9`. There is no branch overlay. The uncovered later interval proves no absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: The model check is green while A and B hold; it models neither Admission nor obligations, and its oracle shares the role partition under test.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen profiles required through the versioning owner; present at the candidate; preserved by §24.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy; repair at the owning D3 rules (§6.8 steps 6-7; §6.6) and regenerate §0.1, §22, §27 and the check from them.
  - id: SP-002
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: Self-reference-safe identity unchanged by revision 13.
  - id: FF-001
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: No immutable publication in scope; remains applicable to later genesis and release.
```

**7.2.1 reconciliation.** The release state names 7.2.1 accepted-current, with distinct public source `aaeaf8b6…` and recovery `efdd1b59…`. The `4c35d92..644eb72` diff changes no `source/`, `dist/`, `orchestrator/`, release-state or PEM path, and no §0.4, §19 or §24 text. The earlier owner comparison between `22f4bdba` and `aaeaf8b6` therefore still applies, and the §0.4 obligation table and the §19 landing points stand. The places where the inherited evidence doctrine is not yet realized are A and B.

## 6. Qualification-program adequacy

§22's disagreement group now enumerates the `4c35d92` discriminators, requires `valid` and §7.4 to agree on every generated ledger, and drops the oracle clause that certified the interpretive sibling. It still cannot discriminate A or B:

- Its step-6 case submits a failing assessment with no stale co-submitted record, and it has no step-7 case.
- It has no case in which an obligation carrying a disagreement is retired, split or retargeted.

The model check is honest about its status (N2). The [testing owner][testing] asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Revision 13 with A or B unrepaired is such a concretization: every §22 case and every model-check property stays green. Add the discriminators named under A and B.

The four consolidation tests establish frontmatter and routing only. HARD-template thresholds, mutation strength, evaluator calibration, custody, blinding, paired baselines and doctrine-realization measurement remain later-gate obligations (§22-§25). No campaign was run and no improvement estimate is asserted.

## 7. What was verified and how

- **Candidate identity.** Resolved the candidate SHA and the workplan blob `ff78959d…`. Extracted a `git archive` of the exact candidate into a scratch directory; later commits, including the handoff commit `3471097`, were excluded.
- **Owners read** at `aaeaf8b6` with `git show`: the D3 role entrypoint (`software-design/SKILL.md`); architecture (read first); evidence (core model, Applicability, applicability dimensions, binding health, Assessment disagreement, Retirement); testing (oracle strength, real-owner and qualification evidence classes); convergence (core progression, active simplification, review strategy after recurrence); the kernel's Challenge text; and the workflow owner's independence and common-mode text.
- **Candidate read.** §0, §0.1, §1, §2, §5, §6.1-§6.9, §7.1-§7.10, §9.1-§9.8 and §10 in full; §15.4 disagreement rows, §21, §22, §26, §27.20-§28; the full `4c35d92..644eb72` diff; the stakeholder record; the authority-index SSDS 8 diff; the routing test; and the model check.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the archive: **4 passed, 0 failures, 0.023 s**, Python **3.13.16**.
- **Whitespace.** `git diff --check 4c35d92d… 644eb726…`: **exit 0**, no diagnostics.
- **Model check**, depth 4:
  - default mode (revision 13): **42 677 transitions, 0 failures, 17/17 discriminators as expected, exit 0**;
  - `REV12=1`: **711 failures (P5 66, Q 286, O 359; P6 0)**; three discriminators differ; **exit 1**;
  - `REV11=1`: **740 failures (Q 272, O 468)**; five discriminators differ; **exit 1**;
  - `REV10=1`: **1672 failures (P1 226, Q 142, O 1304)**; six discriminators differ; **exit 1**.
- **Model check**, depth 5:
  - default mode: **920 081 transitions, 0 failures, 17/17 discriminators, exit 0**, matching §0.1;
  - `REV12=1`: **22 622 failures (P5 1790, P6 16, Q 8339, O 12477)**;
  - `REV11=1`: **24 420 failures (Q 7752, O 16668)**;
  - `REV10=1`: **52 056 failures (P1 5504, Q 4122, O 42430)**.

  Each sensitivity mode fails at least one owner-grounded property (P1-P6 or Q), not only the oracle.
- **A and B.** Deductive, from the quoted contract text. Neither is in the model's vocabulary, so no scratch reproduction was attempted.
- **Identities.** Verified the predecessor blobs, the release-state identities, the frozen-profile presence, the PEM blob identity and the changed-path list above.
- **Repository untouched.** No candidate, source, distribution, index, release state, PEM or frozen resource was changed. The only repository output is this record. Nothing was committed or pushed.

**Scientific inquiry envelope.** Examined architecture-mediated evidence applicability, admission, obligation, disagreement, disposition and closure. Materiality here is the ability to change support, closure or the next authorized action. No physical or numerical result is asserted. One pinned candidate was reviewed through multiple deductive trajectories; no variant search over scientific analyses was performed and no delegates were launched. The judgment relies on accepted engineering and evidence doctrine, not on project D1/D2 authority, so the tension-search duty was not triggered.

## 8. What could not be verified

- **PEM schema validation.** `source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, on the working-tree file whose blob equals the candidate's, failed with `UNAVAILABLE: repository revision is not resolvable as an immutable object` for historical evidence routes (`55c08526…`, `81375d81…`). This checkout is a **shallow clone** (`git rev-parse --is-shallow-repository` = `true`). That is an environment limitation, not a PEM defect and not a pass. The blob is unchanged since the `124B0B7` record's passing validation.
- **Remote state.** `origin/main` is the local tracking ref. No fetch was performed and no remote-state claim is made.
- **Request composition and obligation granularity.** A1 assumes that a submission's failing assessment travels with its task result, which §9.1 and §6.3 make the default. The "discharged first" case of A2 assumes that two tasks can be bound to one evidence or assessment obligation, and B assumes that required evidence obligations follow accepted `EVIDENCES` relations (§7.1, §6.2, §10). These are Manual compositions (items 6, 7). The contract-tightening case of A2 and the removal case of B need only the D3 text quoted.
- **Runtime evidence.** No SSDS production owner, witness deployment, harness adapter or Architecture Manual exists. Runtime fidelity, read recording per harness, failure injection, lineage attestation, privacy enforcement, scaling and burden reduction remain unexecuted (§21-§26), and none is counted as a pass.
- **Repository acceptance.** The full repository regression, package build and validation, distribution parity, frozen-resource census and Core snapshot tests were not rerun. This Review changes no protocol source or descendants.

## 9. Common-mode dependency

This reviewer is a fresh-context sub-agent **of the same model family as the author** (Claude), launched by the authoring session from a handoff the author wrote, under stakeholder SD-8. That is a material common-mode dependency: shared blind spots, framing inherited from the handoff's scope list, and the same corpus and toolchain are all plausible. Two previous same-family Reviews each found one blocker family in the then-new mechanism. This Review deliberately searched the mechanism's *boundaries* instead, and that choice is itself a framing a different family might not share.

The handoff gave no author conclusions. This record supplies **no different-family corroboration**. The design's own §9.6 lets policy require that for high-consequence surfaces, and the stakeholder has waived it for this cycle. A PASS from this cycle would still need the owner adjudication and production evidence of later gates ([workflow, Optional independent cognitive trajectories][workflow]).

## 10. D4 statement

**D4 remains NOT AUTHORIZED.** Phase B Review is NO-PASS. The next step is the owning D3 repair of §6.8 steps 6-7 (A) and of the protocol-obligation row and disposition class of §6.6 (B), with §0.1, §22, §27 and the model check regenerated from them, and a replacement immutable candidate. Even a later Phase B PASS authorizes nothing by itself:

- G1 needs the accepted Manual and explicit stakeholder acceptance of the major change.
- G2 needs a separately reviewed shadow workplan and stakeholder authorization.
- G3 needs real-owner implementation evidence.
- G4 adds per-subject cutover, quiescence and rollback (§23-§25).

This Review grants no Manual acceptance, implementation permission, spend release, cutover, ratification or promotion.

[wp]: https://github.com/hjin98/scientific-software-development-system/blob/644eb7262f01752a0d8059f32e38a1fb8b9c99ea/workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
[kernel]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md
[workflow]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md
[evidence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/evidence-evolution-and-dependencies.md
[testing]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md
[convergence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md
