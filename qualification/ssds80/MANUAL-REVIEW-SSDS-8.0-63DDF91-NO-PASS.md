# SSDS 8 Architecture Manual — Independent D3 Review, candidate 63ddf91

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 63ddf9174c79d013fc555d16f55ef377a4b6e9df
    SCOPE: whole proposed Manual as durable D3 owner: (a) closure of workplan §21 and both §16.2 tables;
           (b) fidelity and refinements R1-R12; (c) adequacy (out-of-matrix); (d) inheritance, capability
           transfer and PEM HAS; (e) qualification design; (f) doctrine-realization map; (g) O1
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob c35afd880fdf981c1ef0145ff2b32050789b1425
    CLOSURE MAP (aid, not authority): qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md,
           blob b527aa1375e6d96d5c644b543606cc1681ce67c0
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE: e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756),
           Phase B Review PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
           (both resolved from PROTOCOL-RELEASE-STATE.yaml)
    FROZEN ARCHITECTURE 1.6.0: orchestrator/docs/architecture.md, blob 39e6de727f6c35402962509d30d947962992eaad
    PRIOR REVIEWS (HYPOTHESES ONLY): Manual NO-PASS records 6FF4ED1, B595F2C, C6DA678, CC005DB, D837363,
           53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98, E2154AC, E9E6E9F, A18B544, 0B6C4FA,
           27EF339, 5C55D4B, 575DC78, F7419D5, B46C250 (same family), B46C250 (different family), F22B4DC,
           362AF9F, 61CD09B and F03B15E; Phase B PASS E23F142
    REVIEW METHOD: immutable-candidate reconstruction (git archive of the candidate), word-level diff
           f03b15e..63ddf91, read in full of Part 0, §1-§10.4, §13.7, §19, §22.1-§22.4, §31.1-§31.6 and §32.2,
           and of §26.4 and §29.1-§29.3 for the closure and doctrine checks; deductive falsification of the
           restored supersession target, the widened gate/review target, the OBLIGATION_ANSWERED exemption,
           the partition identity and the cutover timing rule in both directions, with sibling search over
           every supersedable kind (convergence owner, "Review strategy after recurrence"); prior-finding
           regression; G1 document checks
    REVIEWER: Claude model family, the same family as the Manual's author; a fresh-context sub-agent
           launched by the authoring session, with none of the authoring conversation
    MUTATION: this record only; no commit, no push

All Manual section numbers refer to the candidate blob above. Governing owners are quoted at the public-source commit `aaeaf8b`.

## SERIOUS CHALLENGE

**None against accepted authority.** SSDP 7.2.1, the reviewed workplan contract, the frozen Architecture 1.6.0 and the stakeholder record are not shown to be false, contradictory or unrealizable. The blocker below is a defect of the proposed D3 Manual; the owners it violates are coherent and realizable.

Owner texts applied (public source `aaeaf8b`):

| Owner | Exact text |
|---|---|
| D3 role, Independent Review and Challenge | "Literal workplan compliance is insufficient when the workplan/architecture itself is too weak for the protected outcome." |
| D3 role, design contract | "prefer cohesive ownership, direct flow, one authoritative representation/state" |
| Architecture, D3 formal-contract discipline | "When an architectural concept carries normative meaning, define it before dependent invariants use it" |
| Evidence, Assessment disagreement | "When a durable representation stores multiple assessments, supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement." |
| Evidence, completeness | "a dependency trace may say “no dependency” or “complete” only for an explicitly declared reviewed scope and relation family." |
| Workflow, Human gates | "Orchestration may represent pending/accepted/rejected state but cannot self-approve it." |
| Convergence, Active simplification trigger | "Active simplification/re-derivation is **mandatory before another additive durable repair** when evidence shows repeated patches around the same mechanism, patch-on-patch repair, ... duplicated/synchronized authoritative state, competing authorities" |
| Convergence, Review readiness | "Review sufficiency is not proof of zero conceivable defects." |

## Verdict

**NO-PASS.** One blocking D3 defect survives. It entered through the repair of `f03b15e` B1, which followed that Review's recommended Option 1.

- **B1 (judgment-disagreement and supersession-authority family; local defect inside a non-local recurrence, with a consequence in the assessment-disagreement matching clause).** The candidate restores "a record of the same kind **on the same target**" as supersession authority for every kind except gate decisions and transformation reviews, and states that "for every other adverse-capable kind the target already contains the veto's reach". For `COMPLETENESS` the §3.4 target is `(X, R, membership)`, which omits the member revisions that the judgment is about and that the §5.5 veto reads ("the same `(X, R, membership)` with the same revisions of `X`'s members"). The supersession target is therefore **wider** than the judgment: a completeness judgment about new revisions may supersede, and so withdraw, an `INCOMPLETE` about old revisions. On a revert the old, disputed `COMPLETE` becomes current and unvetoed although nobody re-judged that content. It then bounds closures and, through `bound(o)`, lets a failing evidence assessment become stale on the strength of a completeness judgment whose dispute was never resolved.

The `f03b15e` repairs otherwise close what they target:
- assessment supersession by the assessor or the owner on the same realization, obligation and reading, with other obligations and readings refused (`f03b15e` B1 trajectories 1 and 2);
- the keyless kinds (every kind now has a §3.4 target), `PLAN_ACCEPTANCE` overlap and `EQUIVALENCE` class supersession (`f03b15e` B1 (i)-(iii));
- the late cutover record, the non-carrier frame and the repeated record (`f03b15e` B2 and siblings (i)-(iv));
- `f03b15e` N1-N3, and N4 except one residue.

The matching clause (§6.5-§6.6), the content-identity family and the D1-D3 change rule show no new defect of their own; §6 is unchanged in this round. B1 reaches the matching clause only through the currency of a bounding completeness judgment, which is an input `on⁺` reads.

This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blocker by earliest owner

### B1 — `COMPLETENESS` supersession reaches content the judgment never addressed

**Family and earliest owner.** Proposed D3, Manual §3.4 (`COMPLETENESS` target), §8.3 step 3 (supersession authority), §5.5 (`same`, `stands⁻`, veto), §0.3 R8 and R9 and the §0.3 history sentence for `f03b15e`. These realize workplan §21 items 2 ("boundary-completeness judgment semantics"), 3 (judgment kinds) and 7 (obligation rules, adjudication), and R9's extension of the reviewed assessment rule "to every judgment kind with an adverse outcome, on that judgment's exact target".

**Recurrence.** This is the fourteenth round of the gate and judgment-disagreement family and the third in which supersession identity and veto identity are defined in two places that disagree. `61cd09b` keyed supersession on the veto's comparison; `f03b15e` showed that comparison undefined or too broad for several kinds and recommended restoring "the same target", stating that `COMPLETENESS` "need[s] no exception, because [its] `same` already equals [its] target". That premise was false for `COMPLETENESS`. The `61cd09b` key happened to include the revisions; restoring the target dropped them again. The common cause is unchanged: the §3.4 target column is not, for every kind, "the exact thing judged", yet supersession authority and R9 both treat it as if it were.

**Contract text (candidate):**

- §3.4: `COMPLETENESS` target "`(X, R, membership)`, plus the analyzer identity for a machinery record".
- §4.3: "its target `m` is the membership digest `sha256(sorted (id, scope_id) of X's members)`"; the revisions are `content` basis entries only.
- §5.5 `same`: "`COMPLETENESS`, the same `(X, R, membership)` with the same revisions of `X`'s members".
- §8.3 step 3: "every other support-tier record, `EVIDENCE_ASSESSMENT` included, only by a record of the same kind on the same target that is either `x`'s **own author's reassessment** ... or the **owner's adjudication** ... For every other adverse-capable kind the target already contains the veto's reach".
- §5.5 `stands⁻`: `j⁻` stops standing once some `d` that "supersedes `j⁻` ... acts(d) ∧ ¬superseded(d) ∧ status1(d) = CLEAR ∧ cont(d)"; the superseder need not be current.
- §0.3 R9: "Changed candidate content or a new revision is a new target, which the adverse judgment does not reach"; "Applies the reviewed assessment rule ... to every judgment kind with an adverse outcome, on that judgment's exact target."
- §6.5: `bound(o)` holds when "every `COMPLETENESS` judgment that bounded it is current with value `T` in the frame of evaluation"; `on⁺ ⇔ on⁻ ∧ ext ∧ bound`.

**Trajectory (no malice; the natural reassessment).**

1. Specification `S` declares `EXECUTION_DEPENDS_ON kern.solve`, and a current singleton `COMPLETENESS(EXEC)` on `{S}` exists, as in the §31.3 granularity case. Agent `A` records `COMPLETENESS(EXEC) COMPLETE c_A` on the singleton `X = {kern.solve}` at revision `v1`. It is current, so the execution closure is bounded through it (§4.6).
2. Realization `r` on tree `T1` (members at `v1`), bounded by `c_A`, fails and is assessed `a⁻`; reproduction `r2`, also bounded by `c_A`, fails identically.
3. Human reviewer `H` finds that the solver also reads `data/mesh.dat` by path, outside the declared closure, and records `INCOMPLETE i_H` on `(X, EXEC, m)` at `v1`. By §5.5, `i_H` vetoes `c_A`: `bound(r2)` is false and `a⁻` cannot be made stale. This is correct, because the closure may have missed the cause.
4. An implementer adds the missing `EXECUTION_DEPENDS_ON` declaration to `kern.solve` (revision `v2`; `X`'s membership digest is unchanged). `H`, satisfied, records `COMPLETE c_H` at `v2` with `supersedes = [i_H]`. Step 3 admits it: same kind, same target `(X, EXEC, m)`, `H`'s own reassessment. `c_H` declares the admitted frame, so it acts in every state.
5. `kern.solve` returns to `v1`: an absorbed revert, a fence that restores `tree(B_n)` (R4), or a revert item. In the state at hand, `c_A`'s `content` entries at `v1` are satisfied, `tgt` holds, and `i_H` no longer stands, because its superseder `c_H` acts, is not superseded, is `CLEAR` and is held. So `vetoed(c_A)` is false and `current(c_A) = T`.
6. A new run `o3` on present content (members at `v1`; `data/mesh.dat` has changed meanwhile) is again bounded by `c_A` at realization (§4.6) and passes. Now `r2` serves (1) and `o3` serves (3) through `on⁺`. If no recorded run yields the failure, `a⁻` is **stale**: the failure stops counting, and for a D1/D2 claim no floor event fires. The stop rests on a completeness judgment that `H` disputed for exactly this content, and on a run that differs from `a⁻`'s only in the read `H` named.

The same step 5 also makes any **new** agent `COMPLETE` on `X` at `v1` unvetoed, and acceptances whose closures `c_A` bounds read it as current (§4.3 `record` on each completeness judgment the closure used).

**Siblings (one cause: a §3.4 target that omits what the judgment is about).** I checked every supersedable kind's §3.4 target against its judged content and its §5.5 `same`:

- `ACCEPTANCE`, `REVIEW` of a subject triple, `PRODUCT_SCOPE_ACCEPTANCE`, `INTAKE_DISPOSITION`, `EQUIVALENCE` (endpoints and class) and `EVIDENCE_ASSESSMENT` (realization, obligation, reading): the target includes the judged revision or content. **No sibling.**
- `GATE_DECISION` and a transformation's `REVIEW`/`CONFORMANCE`: the widened target (gate and triple; item and changed-unit content) equals the veto's `same`. **No sibling.**
- `PLAN_ACCEPTANCE`: the target (the exact item-revision set) is narrower than the overlap veto. That is not permissive; it is a relief-availability limit (N1).
- `IMMATERIALITY`: the target (the failing assessments) omits the governing state its conclusion is about, but superseding a disposition only withdraws it. That direction is restrictive. **Not a defect.**
- **Only `COMPLETENESS` is permissive.**

**Violations.**
- The evidence owner's "supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement": the ledger shows the `v1` disagreement between `A` and `H` as resolved by a record about `v2`.
- The evidence owner's bounded completeness ("'complete' only for an explicitly declared reviewed scope"), and S5: a closure is narrowed, and a failure made stale, by a completeness judgment whose standing objection about the same content was withdrawn by a judgment about other content.
- S4 ("a failing assessment that counts keeps its claim qualified until a judgment addressing it, or discriminating evidence, disposes of it"): `a⁻` stops counting through observations whose discrimination rests on the disputed bound.
- The Manual's own R9 ("on that judgment's exact target"; "a new revision is a new target") contradicts step 3's target for this kind. An implementer must choose between the two statements.
- The step 3 sentence "the target already contains the veto's reach" is true here, but the converse it needs (the target is no wider than the judgment) is false, and it is that converse that keeps relief inside what the superseder judged.

**Family assessment and options for the stakeholder.** This is a clean local defect, one kind's target, inside a non-local recurrence. A latch or exception would be additive and is not proposed.

- **Option 1 (recommended; narrows, adds no rule).** Make the §3.4 `COMPLETENESS` target the exact thing judged, `(X, R, membership)` at the revisions of `X`'s members that its `content` basis names. Supersession "on the same target" and the veto's `same` then coincide. In §0.3 R8/R9 and in the §3.4 preamble, state once that a support-tier kind's target is the exact thing judged, so supersession never crosses content. Correct the step 3 sentence to "for every other adverse-capable kind the target is the veto's reach or narrower".
- **Option 2 (adds a conjunct).** Keep the targets and require, for every adverse-capable kind, that a superseder also satisfies the kind's `same` against the superseded record. This is one more rule in the place where the family keeps recurring, and it inherits `PLAN_ACCEPTANCE`'s overlap. **Adds mechanism.**

I would put Option 1 versus Option 2 to the stakeholder. Neither is an SD choice; the present text is the author's under item 19.

**Required discriminators (real owners: Admission → Derivation → inspector, nothing seeded resolved).**
- `H`'s `COMPLETE` at `v2` naming its `INCOMPLETE` at `v1` in `supersedes` is rejected (`AUTH_SUPERSEDES`); the same holds for the owner's adjudicating `COMPLETE` at `v2`.
- `H`'s, or the owner's, `COMPLETE` at `v1` naming the `v1` `INCOMPLETE` is admitted and ends the veto.
- After the revert in step 5, `c_A` stays vetoed, `bound(r2)` is false, `a⁻` is not stale, and the owner's adjudication obligation stays derived.
- An implementation that keys `COMPLETENESS` supersession on `(X, R, membership)` alone must fail.

## 2. Non-blocking findings

**N1 — `PLAN_ACCEPTANCE` relief can become inadmissible (B1 family; restrictive, liveness).** The overlap veto ("any item revision both name") reaches item sets other than the rejected record's target. A passing superseder must lie on that exact target, and step 6 refuses a passing record whose basis is not current.

Trajectory: `REJECTED {A1, B1}`; the plan amends `B1` to `B2`; a peer's `ACCEPTED {A1, B2}` is vetoed through `A1`. The owner's adjudicating `ACCEPTED {A1, B1}` is stale (B1 not current) and is refused. An adverse superseder vetoes in turn. The only remaining routes are an upheld challenge of the rejection or amending `A1`.

This fails closed, but the `ADJUDICATE_DISAGREEMENT` holder cannot answer with its own judgment, and step 3's "a veto can be lifted wherever it bites" overclaims for this kind. Repair: state the challenge route for this case, or say that the relief is available only while the rejected set is current. No mechanism.

**N2 — Re-partition after a discharged part has no stated mechanism (repair of `f03b15e` N2).** Part obligations now carry the `PARTITION` record's identity (§13.7), and supersession withdraws a whole record. Yet §13.7 still says "A later partition supersedes an earlier one only for obligations not yet discharged", and also that every partition's "obligation sets partition the item's obligations exactly".

After part 1 of `P1` integrates, a `P2` that supersedes `P1` either re-derives part-1's share as a new undischarged obligation (repeat work) or must leave `P1` in force for the discharged part, which supersession cannot express. Both are fail-closed; the implementer must choose. Repair: say that a re-partition partitions only the undischarged obligations and that a superseded `PARTITION` keeps its discharged parts' obligations, or that a re-partition repeats them. This is the pattern the handoff names: a repair of a non-blocking finding that leaves a new ambiguity.

**N3 — Cutover residue (`f03b15e` B2 family; all fail closed).**
- (a) A `LEGACY(p)`/`UNGOVERNED` → `NATIVE` `MODE_TRANSITION` that declares the **admitted** frame is not explicitly refused. §19.5's "enacted only by an integration that carries it" excludes enactment, but §19.1's "any other at its admission" invites a misreading. State the refusal and add it to (S).
- (b) The enactment condition does not require `s`'s admitted mode at integration to equal the record's source mode. With two pending carriers of one subject, the second integration "cuts over" an already `NATIVE` subject and, since a `MODE_TRANSITION` ends tenure, restarts its tenure. This is restrictive, but undefined.
- (c) After a fenced cutover (now disclosed, §19.5, §32.2), re-application is an ordinary `NATIVE` change, so none of conditions 1-6 is re-checked. In particular, no quiescence attestation covers legacy work that may have resumed while the legacy bytes were back. Such edits arrive as foreign changes to a `NATIVE` subject and go to intake, so nothing is silent. Disclose it with the existing half-state residual.

**N4 — Residue.**
- §0.3 R12's why-column still says "The cross-run reach of a gate `REJECT` and of its relief is R9's single judgment key", a concept this candidate deleted.
- §0.3 R8 and R9 do not list the widened supersession target for gate decisions and transformation reviews; it appears only in the history paragraph and §8.3 step 3.

Editorial.

**N5 — Qualification gaps (DS-001).**
- §31.6 (R) has no case for `COMPLETENESS` supersession across revisions (B1).
- No case covers `PLAN_ACCEPTANCE` relief after an amendment of a non-overlapping item (N1).
- No case covers an admitted-frame cutover record or two parallel carriers (N3).
- No case covers a re-partition after a discharged part (N2's liveness).

A §31 implemented to the present expected values would encode B1. These are design-program omissions, not runtime demands at G1.

**N6 — Stakeholder-level trade-offs (reported as such, not blockers).**
- The cutover race: without an item-level cutover declaration, the Dispatcher may integrate the carrier before the human records the cutover, costing a further iteration or a new item. The alternative, a contract field that makes the acting record an enactment condition, **adds mechanism**.
- The cross-run gate veto with relief in the later run.
- SD-26's per-iteration acceptance and gate cost.
- R4's fence cost.
- SD-17's partial reversal and SD-24's narrowing (closure map §5).
- The exact-identity cost.
- SD-25's consequences.
- Phase B N1 (paraphrase-only adoption instruction, §32.2).

## 3. Closure audit: workplan §21 and §16.2

**Method.**
- The diff `f03b15e..63ddf91` changes only:
  - §0.3 (history sentence);
  - §5.5 (one sentence of `same`);
  - §8.3 step 3 (supersession authority) and step 7 (`OBLIGATION_ANSWERED`);
  - §13.7 (part obligation identity);
  - §19.5 (head sentence, carrier paragraph, half-state disclosure);
  - §31.6 (discriminators (R), (S) and the (Q) wording);
  - §32.2 (one residual);
  - closure-map row 13 and §5.
- I listed the 27 §21 items from the workplan at the candidate and located the deciding text myself for every item the diff or the B1 family touches (2, 3, 5, 7, 13, 24). I used the closure map only to find text, and its claims for these rows match the text except as noted below.
- For the other items I confirmed that the cited sections are unchanged since `f03b15e`, and I spot-read §1-§10, §19, §22 and §26.4 in full.

**Not substantively resolved at this candidate:**

| §21 item | Clause | Gap |
|---|---|---|
| 2 | boundary-completeness judgment semantics | A completeness judgment's standing objection can be withdrawn by a judgment about other member revisions (B1) |
| 7 | obligation rules (adjudication) | The `COMPLETENESS` supersession route resolves a disagreement over content the superseder never judged (B1). `PLAN_ACCEPTANCE` relief by supersession can be refused (N1, non-blocking) |
| 24 | task-partition checks | Re-partition after a discharged part is ambiguous (N2, non-blocking; closure otherwise holds) |

Item 13 (cutover, quiescence) is now resolved: the record is admissible only in a pending carrier of the stated kind, conditions 1-6 are checked at the carrying integration, and the residue is non-blocking (N3).

**§16.2.** Both tables are resolved in §26.4, unchanged since `f03b15e`. I re-read §26.4: every workplan `Deferred` row (invariants 4, 9, 15, 17 and 26; §5 API standard; §6 SPI; §7 shared records; §12; §18) has a final disposition there.

**Material decision versus delegated choice.** B1 is an under-specification an implementer would have to decide architecturally. I found no new over-specification.

## 4. Refinements R1-R12

| # | Assessment |
|---|---|
| R1 | **Sound as a construction.** `on⁺ ⇒ on⁻ ⇒ link⁻` holds by construction and the guard is unchanged. B1 does not break R1. It feeds `bound` a completeness currency that should have stayed vetoed, so R1's permissive conjunct is only as sound as completeness supersession |
| R2, R3 | Sound; unchanged |
| R4 | Sound; the fenced-cutover half state is now disclosed (`f03b15e` N3 closed); N3 (c) adds one further disclosure |
| R5, R6, R7 | Sound; unchanged |
| R8 | **Unsound for one kind.** "By its own author's reassessment or the owner's adjudication ... on the same target" is right for every kind whose target is the exact thing judged; `COMPLETENESS`'s is not (B1). The widened gate/review target is not listed in the row (N4) |
| R9 | **Veto sound. Relief sound** for gate decisions and transformation reviews across runs and enactments, and for assessments. **Too wide** for `COMPLETENESS` (B1); **sometimes unavailable** for `PLAN_ACCEPTANCE` (N1) |
| R10 | Sound; the cutover's run is its carrying enactment and is never enacted late |
| R11 | Sound; `gterm`, `unq` and `elig` are unchanged |
| R12 | Sound; editorial residue in its why-column (N4) |

## 5. Previous findings re-derived

"Closed" means I re-derived that the present text excludes the named trajectory. It is not runtime evidence.

**Depth.**
- In full against the new text: `f03b15e` B1-B2 and N1-N6.
- For older records, I took the `f03b15e` record's dispositions as hypotheses. I confirmed that each family's governing text is unchanged except in the hunks listed in section 3, and re-checked the mechanisms those hunks touch (§8.3 steps 3 and 7, §5.5, §13.7, §19.5). I did not re-read every older record's prose.

### F03B15E

| ID | Disposition |
|---|---|
| B1 trajectory 1 (assessor's own `PASS` rejected) | **Closed**: same realization, obligation and reading is the same target, so it is authorized; the (R) discriminator states it |
| B1 trajectory 2 (another obligation or reading disposing of `a⁻`) | **Closed**: a different target, so it is rejected |
| B1 (i) keyless kinds | **Closed**: each has its §3.4 target |
| B1 (ii) `PLAN_ACCEPTANCE` overlap | **Closed** (the exact set). The relief limit is N1 |
| B1 (iii) `EQUIVALENCE` class | **Closed** (the target includes the class) |
| B1 family | **Recurs as B1** for `COMPLETENESS`, whose target omits the revisions |
| B2 (late record after carrier integration) | **Closed**: Admission refuses a cutover record once the enactment has an admitted integration (§19.5); (S) states it |
| B2 (i) non-carrier frame | **Closed**: the carrier kind and naming are checked at the record's admission |
| B2 (ii) head sentence | **Closed** ("enacted only by an integration that carries it") |
| B2 (iii) old frame | **Closed** (same refusal) |
| B2 (iv) repeated records | **Closed** (a second record in one enactment is refused) |
| N1 (`OBLIGATION_ANSWERED`) | **Closed**: "bound to it there" is restored, with an exemption for authorized supersessions |
| N2 (partition identity collision) | **Closed as stated; new ambiguity N2** |
| N3 (fenced cutover half state) | **Closed** (disclosed in §19.5 and §32.2); see N3 (c) |
| N4 (residue) | **Partly closed**: the carrier wording, history sentence and closure-map row are fixed; R12's "single judgment key" remains (N4) |
| N5 (qualification) | **Partly closed**: (R) and (S) added; new gaps N5 |
| N6 | Stakeholder; carried as N6 |

### 61CD09B, 362AF9F, F22B4DC, B46C250 (both families)

| Review | IDs | Disposition |
|---|---|---|
| 61CD09B | B1 (gate veto relief across runs) and siblings (i)-(iv) | **Closed**: the widened target for gate decisions and transformation reviews is kept; the relief acts only where the superseder acts |
| 61CD09B | B2 (cutover carrier) | **Closed**, with the timing completed (above) |
| 61CD09B | N1-N3, N5 | Closed |
| 61CD09B | N4 | Superseded by `f03b15e` N2 and this N2 |
| 61CD09B | N6 | Partly closed (N5) |
| 61CD09B | N7 | Stakeholder |
| 362AF9F | B1-A and siblings | Closed (veto unchanged) |
| 362AF9F | B1-B (cutover run identity) | Closed |
| 362AF9F | N1-N5 | Closed |
| 362AF9F | N6 | Partly closed |
| 362AF9F | N7 | Stakeholder |
| F22B4DC | B1-A to B1-F | Closed |
| F22B4DC | N1-N4 | Closed |
| F22B4DC | N5 | Partly closed |
| F22B4DC | N6 | Stakeholder |
| B46C250, different family | B1-A, B1-B (frame relief must not act in the admitted state) | Closed; the restored target does not change where relief acts |
| B46C250, different family | B1-C, B1-D | Closed |
| B46C250, different family | N1, N3, N6 | Closed |
| B46C250, different family | N2 | Disclosure |
| B46C250, different family | N4 | Partly closed |
| B46C250, different family | N5 | Stakeholder |
| B46C250, same family | B1 (i)-(iv) | Closed |
| B46C250, same family | N1, N3 | Closed |
| B46C250, same family | N2 | Disclosure |
| B46C250, same family | N4 | Partly closed |
| B46C250, same family | N5 | Stakeholder |

### F7419D5 to E2154AC

| Review | IDs | Disposition |
|---|---|---|
| F7419D5 | B1, N1-N3, N5 | Closed |
| F7419D5 | N4 | Partly closed |
| F7419D5 | N6 | Stakeholder |
| 575DC78 | B1, N1-N7 | Closed (`gterm` unchanged) |
| 5C55D4B | B1-B2, N1-N7 | Closed, apart from stakeholder items |
| 27EF339 | B1-B3, others | Closed |
| 27EF339 | N2 | Stakeholder |
| 0B6C4FA | B1-B2, others | Closed |
| 0B6C4FA | N1 | Stakeholder |
| 0B6C4FA | N2 | Partly closed as before |
| A18B544 | B1-B2, N1-N5 | Closed |
| A18B544 | N6 | Superseded |
| E9E6E9F | B1-B2, N1-N5 | Closed or superseded |
| E2154AC | B1, N1-N5 | Closed; its "bound to" reading of `OBLIGATION_ANSWERED` is the text again |

### 3540D98 (GPT family), 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363

| Review | IDs | Disposition |
|---|---|---|
| 3540D98 | B1 (exact identity), B2 (`ext`), B4 (equal regions) | Closed |
| 3540D98 | B3 (gate qualification) | Closed for its trajectory; the judgment family recurs as B1 here |
| 3540D98 | N1 | Closed |
| 3540D98 | N2-N4 | Held as disclosures |
| 798B2B4 | B1-B4, N1-N8 | Closed; no D1/D2 revival on revert on any route, and a late cutover is now refused |
| 71CF9B3 | B1-B2, N1-N8 | Closed |
| 86AB683, 1FFBBF0 | B and N items | Closed (SD-18 class unchanged) |
| 53669A5 | B1-B3, N2-N3, N5-N9 | Closed |
| 53669A5 | N4 (the `COMPLETENESS` veto needs the same revisions) | **Closed for the veto; its supersession counterpart is B1** |
| 53669A5 | N1 | Stakeholder |
| D837363 | B1-B4, N1-N8 | Closed |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

| Review | IDs | Disposition |
|---|---|---|
| CC005DB | B1-B3, N1-N8 | Closed |
| C6DA678 | B1-B3, N1-N12 | Closed |
| B595F2C | B1-B3, N1-N8 | Closed |
| B595F2C | B4 (no resolution by re-dispatch, count or order) | **Closed** for every kind except `COMPLETENESS` supersession across revisions (B1) |
| 6FF4ED1 | B1-B4, N1, N3-N12 | Closed |
| 6FF4ED1 | N2 (R8 reconciliation of supersession authority) | **Partly closed**: defined for every kind, too wide for `COMPLETENESS` (B1) |

### Phase B §3 closures and N1-N4 carry-forward

| Closure | Present reconstruction |
|---|---|
| Completeness polarity (Phase B N2), both directions | **Held as stated.** §6 is unchanged. An alternate tree differing from `tree(a⁻)` only outside a recorded narrow basis carries a differing old-content run in (2) and a yielding present-content run in (4). Under a bounding judgment that becomes `P`, blocked, revoked or loss-withheld, both stay counted through `link⁻` (S0, no completeness read); losing the judgment only narrows (1) and (3). Restrictive direction: a stop is withdrawn only by a newly admitted narrow anchor. **Caveat:** B1 is a distinct route by which a bounding judgment wrongly **regains** currency, so (1) and (3) can be served where a standing objection should prevent it |
| Support cycles fail closed; corrupt prefixes | Held: the §5.6 clamp and §5.7 `INTEGRITY_HALT` are unchanged; supersession authorization is an admission fact and adds no support edge |
| Y1/Y2, X1-X3, candidate-own latch, floor and class | Held (§6.8 unchanged). The floor depends on staleness, so B1 can suppress a D1/D2 floor event in its trajectory |
| Contrary-run retention, nondeterminism, U1/U2/W1/W2 | Held (§6.6 unchanged) |
| Absorbed relaxation; adversity versus currency, challenge, loss; salvage; independence; start latch; structure, quarantine, tenure; publication and fencing | Held |
| Phase B N1 | Disclosed (§32.2) |
| Phase B N3 | Held (§31.3 model limits) |
| Phase B N4 | Held (§32.3) |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | `INCOMPLETE` at `v1` superseded by the author's `COMPLETE` at `v2`; revert to `v1` | **Fails: B1** |
| 2 | As 1, with a new agent `COMPLETE` at `v1` after the revert | **Fails: B1** (unvetoed) |
| 3 | As 1, through a frame: a candidate whose merged tree restores `v1` | **Fails: B1** in that frame (permissive readiness) |
| 4 | Own assessor's `PASS` superseding their `FAIL` (same realization, obligation, reading) | Held: admitted, disposes where it acts |
| 5 | Assessor's `PASS` under another reading naming `a⁻` | Held: rejected |
| 6 | Owner's `PLAN_ACCEPTANCE ACCEPTED {A1}` naming `REJECTED {A1, B1}` | Held: rejected |
| 7 | `REJECTED {A1, B1}`, amendment to `B2`, owner's relief on `{A1, B1}` | Fails closed: relief refused as stale (N1) |
| 8 | Owner's `EQUIVALENT` of class `CONSUMER:k` superseding `NOT_EQUIVALENT CONSUMER:k`; a peer's `EDITORIAL` | Held: the veto ends for every covering class, which the owner's judgment covers |
| 9 | `ACCEPTANCE FAIL` in an abandoned frame; identical triple in a later frame; author's `PASS` there | Held: same target; acts in that enactment |
| 10 | `ACCEPTANCE FAIL` in run `R1`; revert to the same triple in run `R3`; author's `PASS` naming `R3` | Held: the run is a named field, not the target |
| 11 | Gate `REJECT` in run `R1` lifted by the owner's `ACCEPT` in run `R3`; a later run `R5` at the same triple | Held: the owner judged the same gate and triple |
| 12 | Owner's `REVIEW PASS` on `X2` lifting `NO_PASS` on `X1` with identical content but another base | Held: symmetric with the veto, which ignores the base |
| 13 | Passing judgment with an authorized `supersedes` added to evade `OBLIGATION_ANSWERED` | Held: only the author or the owner qualifies, and the veto still applies |
| 14 | Human author's direct reassessing `ACCEPTANCE PASS` after its `FAIL` answered `ACCEPT(s)` | Held: admitted |
| 15 | Carrier integrates first; human cutover record afterwards | Held: refused; mode unchanged |
| 16 | D2 cutover record in a `MIGRATE` frame | Held: refused |
| 17 | Cutover record in `X`'s frame; clean rebase `X'` integrates | Held: same enactment, acts in `X'`, conditions checked |
| 18 | Admitted-frame `LEGACY` → `NATIVE` record | Not enacted under §19.5's "only"; refusal unstated (N3 (a)) |
| 19 | Two parallel carriers of one subject | Fails closed but undefined (N3 (b)) |
| 20 | Fenced cutover, fence kept, carrier re-applied | Fails closed; conditions not re-checked (N3 (c)) |
| 21 | Re-partition after part 1 of `P1` is discharged | Ambiguous, fails closed (N2) |
| 22 | Stratification and single-valuedness with the restored target | Held: authorization is an admission fact; `stands⁻` reads S0/S1 |
| 23 | `D_n[X]` versus the post-integration state with a frame-acting cutover | Held |
| 24 | Phase B N2 polarity variants | Held (section 5) |
| 25 | Structure, `ignore` or analyzer change with `K` fixed | Held (guard unchanged) |

I stopped discovery once B1's cause was characterized and every supersedable kind had been checked (section 1). Further siblings would be implementation-like:
- every lifecycle kind's frame behaviour;
- every interaction of the partition identity with budgets.

Section 6 is a bounded negative result elsewhere, not a completeness claim.

## 7. Minimum architecture and capability transfer

- **What `63ddf91` changes.**
  - It restores one identity (the §3.4 target) as supersession authority and widens it for two kinds.
  - It bounds the cutover record's admission to a pending carrier of the stated kind.
  - It adds the partition record's identity to part obligations.
  - It adds no component, store, record kind or tier.
  - The supersession repair is subtractive and is the right shape. B1 is a defect in one row of the §3.4 table it relies on.
- **Dropped capability.** None found. The reviewed own-assessor and owner routes are restored.
- **Withdrawn protection (B1).** A standing `INCOMPLETE` loses its protective effect on reverted content.
- **§30.** Accurate.
- **Architecture 1.6.0 supersession (PC-001).**
  - §26.4 preserves the version-bound Level 0 Core, the frozen profiles and the single composition root.
  - `orchestrator/docs/architecture.md` is byte-identical to `fad3ee4` (blob `39e6de7`).
  - Nothing under `source/` or `dist/` changed (section 10).
- **PEM Historical Applicability Set.** PEM was activated, because this is replacement of mature machinery under a memory-bound workplan. The PEM file at the candidate is blob `1561797`, equal to the checkout's, and schema-valid.

| Entry | Applicable | Disposition |
|---|---|---|
| PC-001 | yes | Held, as above |
| DS-001 | yes | Applied in N5: (R) cannot discriminate B1 |
| FF-001 | yes, for genesis and cutover | Held for genesis (§19.9); the cutover's validation is no longer bypassable |
| SP-001 | no | No source-to-package routing change |
| SP-002 | no | No immutable self-reference construction in this cycle |

I did not re-read the archived §18 inheritance workplans. The diff touches no inherited capability.

## 8. Qualification-design adequacy

- **Status.** §31.1 correctly marks every runtime group `UNEXECUTED`. G1 needs only §31.10, which I ran (section 10).
- **Discrimination.** The real-owner requirement and the negative discriminators are adequate in form. (R) discriminates the `f03b15e` B1 cases and (S) the cutover timing. But no case exercises `COMPLETENESS` supersession across revisions, so a §31 implemented to the present expected values would encode B1 (N5).
- **Executed-evidence claims.** Nothing is claimed as executed beyond §31.10.
- **Diagnostic model.** Optional. I did not run it; it is unchanged and models none of the clauses at issue.

## 9. Doctrine-realization map and O1

- **Coverage.** §29.1-§29.3 are unchanged since `f03b15e`; I re-read them. All seven 7.2.1 entrypoints and the scientific checks are mapped with E0-E3 levels, and §29.6 discloses the E3 duties.
- **Rows that depend on B1's repair.** The cutover-related "human ratification where required" presence claim (E0) now holds. The rows claiming explicit supersession and adjudication of disagreements depend on B1's repair for completeness judgments.
- **Other rows.** No other row overclaims beyond the limits its level discloses.
- **O1 (§0.5).** Unchanged and adequate:
  - the realized record, readers, routine questions and realized-record architecture are stated;
  - product surfaces are marked within the deliverable;
  - **none** is marked beyond it.

  Product-scope acceptance remains with the stakeholder (S12). Technical Review accepts nothing.

## 10. What I verified and how; what I could not verify

**Verified.**

- Reviewed exactly `63ddf9174c79d013fc555d16f55ef377a4b6e9df` through a `git archive` snapshot in `$TMPDIR/ssds80-manual-review-63ddf91/`. Blobs confirmed: Manual `c35afd8…`, closure map `b527aa1…`, workplan `91bde23…`.
- Diffed `f03b15e..63ddf91` by word for the Manual and by line for the closure map (section 3).
- Read the Manual sections listed in the header, the `f03b15e` Review in full, workplan §21 and §16.2, and the workplan's §6.8 step 3 supersession sentence (which fixes no target).
- Checked the `COMPLETENESS` `same` clause at `798b2b4`, `362af9f` and `61cd09b`: unchanged ("with the same revisions of `X`'s members").
- Read the governing owners at `aaeaf8b`: the D3 role entrypoint; architecture (formal-contract discipline); evidence ("Assessment disagreement", completeness bounds); workflow ("Human gates"); convergence (simplification trigger, review readiness, "Review strategy after recurrence").
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the candidate snapshot: **4 tests OK**.
- `git diff --check f03b15e55de77fe230f404fcb0b3bf12b21b6a3d 63ddf9174c79d013fc555d16f55ef377a4b6e9df`: clean (exit 0).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 63ddf9174c79d013fc555d16f55ef377a4b6e9df`: 57 files, 18,185 insertions and 1 deletion. They are the Manual, `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`, and 55 files under `qualification/ssds80/`.
- `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4` (empty diff; frozen blob `39e6de7`).
- PEM: `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md` in the checkout gave "PEM schema 1 valid: 5 families, 0 notices"; blob `1561797` at the candidate and in the checkout. In the archive snapshot it reports binding-health `REVIEW_REQUIRED`, only because the snapshot has no Git repository.

**Not verified or not established.**

- No production or runtime behaviour; none exists at G1.
- The diagnostic model was not run.
- I did not read §10.5-§13.6, §14-§18, §20-§21, §23-§25, §27-§28 and §29.4-§30 line by line; they are unchanged since `f03b15e`.
- I did not re-read every older Review record's prose or the archived §18 workplans. Section 5 states the depth.
- B1 is deductive from the Manual's own rules. It depends on:
  - §3.4's `COMPLETENESS` target omitting member revisions;
  - §8.3 step 3's "on the same target";
  - §5.5's `stands⁻` not requiring the superseder's currency.

  I searched the candidate for any rule that adds revisions to a completeness target or restricts its supersession, and found none.

## 11. Scientific-checks answers

- **Material findings.** None about scientific or numerical meaning. B1 and N1-N6 are D3 findings about software that mediates scientific evidence. B1 affects whether a disputed completeness judgment can bound an execution closure and so make a failing evidence assessment stale, which decides whether a scientific claim stays visibly disputed.
- **Realized results.** I produced, ran and reviewed no realized scientific results. Null envelope: I examined the Manual's D3 text, the governing owners and prior Review records. Materially unexamined: any runtime evidence (none exists) and the diagnostic model.
- **Variants.**
  - Repair directions for B1: two, of kind D3 options. The criterion was to keep supersession inside what the superseder judged and to remove rather than add mechanism. Option 1 is recommended.
  - Trajectories: 25, of kind out-of-matrix, chosen as high-information siblings of the restored target, the widened targets, the `OBLIGATION_ANSWERED` exemption, the partition identity and the cutover timing (section 6).
  - Sibling check: every supersedable kind's §3.4 target compared with its judged content and its §5.5 `same`.
- **Reliance on accepted D1/D2 authority.** I relied on no accepted D1/D2 authority for a consequential judgment, so no tension search was owed.
- **Gaps.** Runtime qualification (G2-G4), the unchanged sections not read line by line, the full prose of older records, and the archived §18 workplans.

## 12. Common-mode note

- **Family.** I am of the Claude family, the same as the Manual's author and as the reviewers of e2154ac, e9e6e9f, a18b544, 0b6c4fa, 27ef339, 5c55d4b, 575dc78, f7419d5, the same-family b46c250, f22b4dc, 362af9f, 61cd09b and f03b15e. The 3540d98, different-family b46c250 and Phase B reviewers were of the GPT family.
- **Engagement.** I was engaged as a fresh-context sub-agent launched by the authoring session.
- **Shared dependencies.** Fresh context does not make me independent. I share:
  - the corpus;
  - the inherited workplan framing and its target, veto, enactment, run and acting vocabulary;
  - the prior Review records, which I read and which shaped my attention to the newest clauses;
  - the toolchain;
  - the model family with the author and with most prior reviewers.
- **Provenance of B1.** I found B1 by reconstruction from the candidate text, checking every supersedable kind's target against its veto, not from a prior record. It entered by following the previous same-family Review's recommended option, whose premise ("`COMPLETENESS` ... `same` already equals [its] target") was false. That repeats the pattern the handoff names and is evidence of shared-framing risk. A different-family review of the supersession repair would reduce it.

## 13. D4 statement

No SSDS 8 D4 is authorized. This Review accepts no architecture, product scope or proposed default. G1 remains open: it needs a repaired Manual candidate, an independent D3 Review with no surviving blocker, and explicit stakeholder acceptance. Shadow implementation additionally needs G2.
