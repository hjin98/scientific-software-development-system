# SSDS 8 Architecture Manual — Independent D3 Review, candidate 051cce3

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 051cce30ff64566ea79bb5d25e97daf803dc6c51
    SCOPE: whole proposed Manual as durable D3 owner: (a) closure of workplan §21 and both §16.2 tables;
           (b) fidelity and refinements R1-R12; (c) adequacy (out-of-matrix); (d) inheritance, capability
           transfer and PEM HAS; (e) qualification design; (f) doctrine-realization map; (g) O1
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob a3532abd9e82fc5e2b1b6590d8bcd8a03d699e88
    CLOSURE MAP (aid, not authority): qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md,
           blob 0a81fd3de32b36c72ff09f71fadc394a93c8b98a
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
           362AF9F, 61CD09B, F03B15E and 63DDF91; Phase B PASS E23F142
    REVIEW METHOD: immutable-candidate reconstruction (git archive of the candidate); word-level diff
           63ddf91..051cce3; read in full of Part 0, §3-§5, §6, §7, §8, §10-§13.7 and §19, and targeted reads of
           §31.6, §32.2, §29.2-§29.3 and the closure map; deductive falsification of the restated target rule,
           the COMPLETENESS target, the "veto's reach or narrower" relief statement, the PLAN_ACCEPTANCE relief
           limit, the re-partition rule and the cutover source-mode and admitted-frame refusals, in both
           directions, with a sibling search over every adverse-capable kind comparing (i) its §3.4 target,
           (ii) its supersession target, (iii) its §5.5 `same` and (iv) the content its judgment is actually
           about, and (v) how its passing side aggregates (∃ versus minimum) (convergence owner, "Review
           strategy after recurrence"); prior-finding regression; G1 document checks
    REVIEWER: Claude model family, the same family as the Manual's author; a fresh-context sub-agent
           launched by the authoring session, with none of the authoring conversation
    MUTATION: this record only; no commit, no push

All Manual section numbers refer to the candidate blob above. Governing owners are quoted at the public-source commit `aaeaf8b`.

## SERIOUS CHALLENGE

**None against accepted authority.** SSDP 7.2.1, the reviewed workplan contract, the frozen Architecture 1.6.0 and the stakeholder record are not shown to be false, contradictory or unrealizable. The blocker below is a defect of the proposed D3 Manual; the owners it violates are coherent and realizable.

Owner texts applied (public source `aaeaf8b`):

| Owner | Exact text |
|---|---|
| D3 role, Independent Review | "Literal workplan compliance is insufficient when the workplan/architecture itself is too weak for the protected outcome." |
| D3 role, design contract | "prefer cohesive ownership, direct flow, one authoritative representation/state" |
| Architecture, formal-contract discipline | "When an architectural concept carries normative meaning, define it before dependent invariants use it" |
| Evidence, assessment disagreement | "When a durable representation stores multiple assessments, supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement." |
| Workflow, synthesis | "A synthesizer reconciles findings through evidence and owner adjudication; it cannot erase unresolved contradictory material evidence by vote" |
| Convergence, Active simplification trigger | "Active simplification/re-derivation is **mandatory before another additive durable repair** when evidence shows repeated patches around the same mechanism, patch-on-patch repair, ... duplicated/synchronized authoritative state, competing authorities" |
| Convergence, Review strategy after recurrence | "A clean local repair that genuinely closes the cause remains sufficient; recurrence does not automatically force redesign." |
| Convergence, Review readiness | "Review sufficiency is not proof of zero conceivable defects." |

## Verdict

**NO-PASS.** One blocking D3 defect survives. It is not in this round's new text. It sits in the widened supersession target that the `61cd09b` repair introduced for a transformation's `REVIEW` and `CONFORMANCE`, which the `f03b15e` and `63ddf91` rounds kept and which this candidate's restated target rule now explicitly exempts.

- **B1 (judgment-disagreement and supersession-authority family; fifteenth round; non-local recurrence of the `63ddf91` B1 cause).** For a transformation's `REVIEW` or `CONFORMANCE`, the author's or owner's relief may name an adverse judgment on another item revision or another base ("the plan item and the changed-unit content in any enactment", §8.3 step 3). Such relief withdraws the objection for every item revision and base the veto reaches, although the superseder judged only its own. On the transformation path, passing reviews discharge by ∃, not by a minimum. So after a revert, a peer's passing review of exactly the content and item revision the objection addressed becomes current and unvetoed, and the candidate integrates on it. Nobody adjudicated the original disagreement. This is the `63ddf91` B1 shape (relief wider than what the superseder judged, exposed by a revert), now in one of the two kinds the `63ddf91` sibling check cleared because it compared the supersession target with the veto's `same`, not with the content judged.

The `63ddf91` repairs close what they target:
- the `COMPLETENESS` target now names member revisions, so the `63ddf91` B1 trajectory is refused;
- `63ddf91` N1 is stated (the `PLAN_ACCEPTANCE` relief limit); N2 is stated, with a residual inconsistency; N3 (a)-(c) are stated; N4 is fixed;
- §31.6 gains the B1, N1 and N3 discriminators.

The matching clause (§6.3-§6.6), the content-identity family and the D1-D3 change rule are unchanged in this round and show no new defect. With the `COMPLETENESS` target repaired, the caveat that `63ddf91` attached to the Phase B N2 polarity re-check no longer applies.

This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blocker by earliest owner

### B1 — Widened review relief reaches item revisions and bases the superseder never judged

**Family and earliest owner.** Proposed D3:
- Manual §8.3 step 3 (the widened supersession target for a transformation's `REVIEW`/`CONFORMANCE`);
- §5.5 (`same`, `stands⁻`, `vetoed`);
- §0.3 R8 and R9;
- §10.4 (discharge by ∃ current passing judgment).

These realize workplan §21 item 3 (judgment kinds) and item 7 (obligation rules, adjudication), and R9's extension of the reviewed assessment rule "to every judgment kind with an adverse outcome, on that judgment's exact target".

**Contract text (candidate):**

- §3.4 preamble (new): "A support-tier record's **target** is the exact thing it judges, so supersession on the same target (§8.3 step 3) never reaches content the superseder did not judge."
- §3.4: `REVIEW` target "transformation `id(X)` or subject triple"; `CONFORMANCE` target "transformation `id(X)` and contract item revision". §7.1: `id(X) = sha256(… ‖ B ‖ C ‖ …)`, so the base is part of the transformation. §4.3: a `REVIEW` holds `content` on "the contract item revision (`EXACT`)" and ctx `content` on the governing closure.
- §5.5 `same`: "`REVIEW` and `CONFORMANCE` of a transformation, the same plan item at any of its revisions and the same candidate content (the same changed units, each with the same content in both candidates)".
- §8.3 step 3: "Two kinds, whose §5.5 `same` test deliberately crosses targets, take a wider target here so that a veto can be lifted wherever it bites ...: ... for a `REVIEW` or `CONFORMANCE` of a transformation, the plan item and the changed-unit content in any enactment. For every other adverse-capable kind the target is the veto's reach or narrower, so relief never reaches content the superseder did not judge".
- §5.5 `stands⁻`: `j⁻` stops standing once some acting, unsuperseded, `CLEAR`, held `d` supersedes it; `d` need not be current.
- §5.2: a frame record acts "in the admitted state ... once that enactment integrates", permanently ("an integration is permanent").
- §10.4: "`discharged(o) ⇔ ∃ current judgment j of kind(o) …`"; "Discharge is not latched".
- §0.3 R9: "Changed candidate content or a new revision is a new target, which the adverse judgment does not reach"; "on that judgment's exact target".

**Trajectory A (item revision; no malice).** Policy requires one independent `REVIEW` for a D4 `IMPLEMENT` item.

1. Item `I` is at revision `i1` and its obligations include `o3`. Task `T1` produces `X1 = (B1, C1, ∅)` with changed-unit content `c`; conformance is `CLEAN`. Agent reviewer `R1` records `REVIEW PASS` on `X1`. Human reviewer `H` records `REVIEW NO_PASS` on `X1` ("`c` does not meet `o3`"). `R1`'s `PASS` is vetoed, `REVIEW(X1)` is `REFUSED`, and `ADJUDICATE_DISAGREEMENT` is derived.
2. The principal answers the adverse result with `AMEND`: the item becomes `i2`, with `o3` reworded (an R2 amendment), and an independent `PLAN_ACCEPTANCE` of `i2` is admitted.
3. Iteration task `T2` produces `X2 = (B2, C2, ∅)` with the same changed-unit content `c`. Agent reviewer `R2`'s `PASS` on `X2` is vetoed by `H`'s `NO_PASS` (same item, any revision, same content), and adjudication routes to the owner `O`. `O` records `REVIEW PASS` on `X2` with `supersedes = [H's NO_PASS]`. Step 3 admits it: owner's adjudication, same kind, same widened target. `X2` integrates, and from then on `O`'s `PASS` acts in every state (§5.2).
4. A human pushes a revert of the last two merges, restoring the tree to `tree(B1)`: plan unit at `i1` and the changed units at their `B1` bytes. Admission absorbs it.
   - The `i1` `PLAN_ACCEPTANCE` is current again (`cur = r`), so the item is issuable.
   - The implementer obligation is open again (drift; discharge is not latched).
   - In `D_n[X1]`, the merge is `tree(C1)`. Every before-image, output and context entry of `R1`'s `PASS` holds, and so does `T1`'s `TASK_RESULT` (item `i1`, `EXACT`).
   - `H`'s `NO_PASS` does not stand, because its superseder `O`'s `PASS` acts, is unsuperseded, `CLEAR` and held; its currency is not read. So `R1`'s `PASS` is current and unvetoed.
5. `X1`'s discharge predicate holds and the Dispatcher submits its integration. A clean rebase onto the reverted head is in `X1`'s enactment (§5.2), and `R1`'s `PASS` counts for it (§7.6 Rebase). Steps 1-9 pass and `c` integrates against `i1`.

Result: the human's objection "`c` does not meet `o3` of `i1`" was never adjudicated for `i1`. `O` judged `c` only against `i2`. `R1`'s `PASS`, which the objection vetoed, now carries the integration.

**Trajectory B (base or context; inside one enactment; no foreign change).**

1. As A step 1.
2. An admitted change moves a unit `g` in the review's governing closure from `g1` to `g2`; `g` is not in `Δ(X1)`. The Dispatcher rebases `X1` cleanly to `X1'` (same task, same enactment, same changed-unit content), and `REVIEW(X1')` is re-requested (§11.5 step 3).
3. An agent `PASS` on `X1'` is vetoed by `H`'s `NO_PASS`. The owner `O` records `PASS` on `X1'` (context `g2`), superseding the `NO_PASS`; the widened target is satisfied. If `T1`'s result had read `g`, a `REVALIDATE` task resubmits the identical transformation, which joins the same enactment (§5.2).
4. A later admitted change reverts `g` to `g1`. On the next rebase `X1''`, every entry of `R1`'s `PASS` holds again (§7.6 Rebase). `H`'s `NO_PASS` does not stand, because `O`'s `PASS` acts in the enactment's frames. `X1''` integrates on `R1`'s `PASS`, judged under `g1`, the context in which `H`'s objection to the same transformation content was raised. `O` judged only under `g2`.

**Siblings (one cause: relief whose target crosses components of what the superseder judged, exposed where passing judgments aggregate by ∃).** For each adverse-capable kind I compared the four sets named in the header and its aggregation:

| Kind | Supersession target vs content judged | Passing aggregation | Result |
|---|---|---|---|
| `REVIEW`/`CONFORMANCE` of a transformation | wider: crosses item revision and base | ∃ (§10.4) | **B1** |
| `GATE_DECISION` | wider: crosses run and rendered core | `gterm` = minimum over every eligible unsuperseded passing decision (§5.5) | **Held.** The superseder's own decision stays in the minimum, so an earlier decision on another core can count only while the superseder's own judgment of the same triple is current. For `NATIVE` D1/D2, an earlier run's decision is never current again (`tgt`) |
| `COMPLETENESS` | equal (repaired) | — | Held (`63ddf91` B1 closed) |
| `ACCEPTANCE`, `REVIEW` of a subject triple, `EQUIVALENCE`, `EVIDENCE_ASSESSMENT`, `PRODUCT_SCOPE_ACCEPTANCE`, `INTAKE_DISPOSITION` | equal or narrower | — | Held. The relief's target is the exact triple, endpoints-and-class, realization-obligation-reading, item revision or delta. The context-revert residue common to every kind is N6 |
| `PLAN_ACCEPTANCE` | narrower in item set | — | Held for item revisions. The objective's revision is stated only through the preamble (N1) |

**Violations.**
- The evidence owner's "supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement". The ledger shows the `(c, i1)` (or `(c, g1)`) disagreement as resolved by a judgment about `(c, i2)` (or `(c, g2)`).
- The workflow owner's "cannot erase unresolved contradictory material evidence by vote", and B595F2C B4 / R9's "never resolved by re-dispatch, count or order". The disagreement ends because a different review of other content was adjudicated, not because anyone adjudicated this one.
- The Manual's own R9: "Changed candidate content or a new revision is a new target, which the adverse judgment does not reach" and "on that judgment's exact target". Read with the §3.4 preamble, this promises that relief stays within what the reliever judged. The widened target is a deliberate exception that the Manual does not disclose as reaching unjudged item revisions and bases. §0.3 R8's why-column gives only the liveness motive ("so a veto that reaches across runs or enactments can be lifted where it bites").
- The closure map (row 3, §5) states that "supersession never crosses content", which is false for these two kinds.

**Why this is not a clean local defect.** This is the fifteenth round of the family, and the fourth in which supersession identity and veto identity are reconciled by redefining one in terms of the other:
- `61cd09b` keyed supersession on the veto;
- `f03b15e` restored "the same target" and widened it for two kinds;
- `63ddf91` found one target too wide;
- this round finds the widening itself too wide.

The shared cause is structural. For a kind whose veto deliberately reaches beyond the vetoed judgment's own target (so that amendment or rebase cannot escape it), lifting the veto by supersession necessarily reaches equally far, and so reaches judgments the reliever never made. The design is safe only where the passing side is aggregated by a minimum (gates). This meets the convergence owner's simplification trigger ("repeated patches around the same mechanism, patch-on-patch repair").

**Options for the stakeholder (Phase C handoff §5).** None is an SD choice; the present text is the author's under stakeholder record item 19.

- **Option 1 (recommended; removes the widened target for reviews, adds one exemption).** For a transformation's `REVIEW` and `CONFORMANCE`:
  - supersession authority returns to the exact §3.4 target (`id(X)`, and for `CONFORMANCE` the item revision);
  - the veto's reach is kept;
  - `vetoed(z)` exempts a passing judgment by the adverse judgment's own author or by the owner, since that judgment is their own reassessment of a target the veto reaches, not a peer's contrary judgment.

  In both trajectories, `O`'s or `H`'s `PASS` on `X2`/`X1'` then counts without superseding anything. `H`'s `NO_PASS` keeps standing against `R1`'s `PASS`, so after the revert `X1` needs `H`'s or `O`'s judgment of its exact target or an upheld challenge. Liveness is kept, because the author or owner can always pass the new target. Gates keep the present widened target, which the minimum makes harmless. **Adds mechanism** (one exemption clause) while deleting one (the widened review target). The adjudication-obligation trigger must also exclude author- and owner-exempt passes.
- **Option 2 (adds a latch; covers N6 too).** A passing judgment that has been vetoed in the admitted state at any position never supports again (an S0/S1 fold over admitted history, like supersession's "never becomes current again"). It closes B1 and N6 uniformly. However, it is a new latch in the family, gates would need eligibility adjusted so that a latched decision leaves `elig` rather than pinning `gterm` at `F`, and it removes `R1`'s `PASS` even where the owner later agrees with it. **Adds mechanism.**
- **Not viable:** making relief lapse with the superseder's currency (reading `current(d)` in `stands⁻`). It puts an S2 value under negation in `base` and breaks §5.6 monotonicity and C8.

**Required discriminators (real owners: Admission → Derivation → Dispatcher → inspector, nothing seeded resolved).**
- Trajectory A: after the revert, `R1`'s `PASS` on `X1` is vetoed, `REVIEW(X1)` is not discharged, `ADJUDICATE_DISAGREEMENT` (or its Option 1 equivalent) is derived, and `X1`'s integration is refused.
- Trajectory B: after `g` returns to `g1`, the rebased `X1''` does not integrate on `R1`'s `PASS`.
- Under Option 1, `O`'s `PASS` on `X2` discharges `REVIEW(X2)` without naming `H`'s `NO_PASS` in `supersedes`, while `R2`'s `PASS` on `X2` stays vetoed.
- §31.6's present case "an owner's adjudicating `REVIEW PASS` in `X2`'s frame lifting an agent's `NO_PASS` on identical content in `X1`", and its discriminator "keys a review's supersession on one transformation ... must fail", must be revised. As written they encode B1 (DS-001).

## 2. Non-blocking findings

**N1 — Target rows still rely on the preamble (B1 family; editorial ambiguity).** The preamble states that a target is "the exact thing it judges". Some rows still do not:
- `PLAN_ACCEPTANCE`'s row says "plan objective section and item revisions". The objective's revision is in the target only through the preamble, although §4.3 and §11.2 make it an `EXACT` basis entry. Read literally, the row yields the `63ddf91` B1 shape through the objective:
  - `H`'s `REJECTED (o1, {A1})` is superseded by `H`'s `ACCEPTED (o2, {A1})`;
  - the objective returns to `o1`;
  - a peer's `ACCEPTED (o1, {A1})` becomes current and unvetoed.

  Read with the preamble, the step 3 relief statement ("available only while the rejected item revisions are current") is incomplete: the objective must be current too.
- `ACCEPTANCE`'s row says "`(s, scope_id, rev)` in its frame". If the frame is part of the target, relief of a `FAIL` recorded in an abandoned frame can never act where the veto bites (restrictive). §10.3 and the `63ddf91` trajectory 9 read it as the triple alone.
- Step 3's "where it is narrower (`PLAN_ACCEPTANCE` …)" omits `EQUIVALENCE`, whose exact-class target is also narrower than its covering-class veto. Its relief is always available, so this is editorial.
- The `ADJUDICATE_DISAGREEMENT` trigger reads `vetoed`, which ignores the vetoed judgment's currency and supersession. After the content moves on, an obligation can remain whose natural answer (a passing superseder) is inadmissible. It fails closed, and the owner's adverse adjudication or a challenge remains available.

Repair: state each row's target exactly (objective revision; the triple, with the frame only as where it resolves). No mechanism.

**N2 — Re-partition text is internally inconsistent (repair of `63ddf91` N2).** §13.7 now says a later partition "partitions only the item's undischarged obligations", but the same paragraph still says every partition's obligation sets "partition the item's obligations exactly" and that "Lint checks all three".
- Because discharge is not latched (§10.4), "discharged part obligations" is position-relative. A part obligation of a superseded `PARTITION` that later reopens by drift must still be derived from the superseded record, which the text implies but does not state.
- Fails closed. Repair: state that lint checks the re-partition against the undischarged set at its admission, and that a superseded partition's part obligations stay derived.

**N3 — Cutover residue (repair of `63ddf91` N3; fails closed).**
- (a) "a second pending carrier of an already cut-over subject cannot integrate its cutover" leaves open whether that carrier integrates without the cutover or is refused outright. Since its cutover record acts in its frames and lifecycle records are never superseded, the only consistent reading is that the enactment can never integrate and the work needs a new iteration. State it.
- (b) In that carrier's frame, the record still applies a `LEGACY`/`UNGOVERNED` → `NATIVE` transition to a subject that is already `NATIVE`, and that frame derivation is undefined. Define it as no frame (or as the source-mode refusal) in §7.4.

**N4 — Overclaims (editorial; repaired with B1).**
- The closure map says "supersession never crosses content".
- §0.3 R8's why-column does not say that the widened review target reaches item revisions and bases the superseder did not judge.
- The §3.4 preamble should name its two exceptions.

**N5 — Qualification gaps (DS-001).**
- §31.6 (N) encodes the widened review relief as expected behaviour (B1).
- No case covers a revert after cross-target relief.
- No case covers the `PLAN_ACCEPTANCE` objective revision (N1).
- No case covers a reopened part obligation of a superseded `PARTITION` (N2).
- No case covers the frame of a refused second carrier (N3 (b)).

These are design-program omissions, not runtime demands at G1.

**N6 — Context-relative judgments (family boundary; stakeholder-level).** For every kind, a superseder judges its exact target under its own basis context. Example:
- `H`'s `ACCEPTANCE FAIL` on `(s, σ, r)` under governing `g1`;
- the owner's `PASS` on the same triple under `g2`, superseding it;
- a revert of `g` to `g1`;
- an agent's `PASS` on the triple under `g1` is then current and unvetoed.

This agrees with the reviewed contract (targets are triples; early cutoff, §5.5) and the superseder judged the same target, so it is not a blocker. It is the residue of "exact thing judged" meaning "target, not relied-on context". The stakeholder should know that Option 1 does not close it and Option 2 does.

**N7 — Stakeholder-level trade-offs (reported as such, not blockers).** Carried from `63ddf91` N6:
- the cutover race;
- the cross-run gate veto and its relief;
- SD-26's per-iteration acceptance and gate cost;
- R4's fence cost;
- SD-17's partial reversal and SD-24's narrowing (closure map §5);
- the exact-identity cost;
- SD-25's consequences;
- Phase B N1 (§32.2).

Added: §19.5's disclosed non-re-check of conditions 1-6 on re-application after a fenced cutover (`63ddf91` N3 (c)), which leaves M6 quiescence resting on intake of foreign legacy edits.

## 3. Closure audit: workplan §21 and §16.2

**Method.**
- The diff `63ddf91..051cce3` changes only:
  - §0.3 (R8, R12, history);
  - the §3.4 preamble and `COMPLETENESS` row;
  - §8.3 step 3;
  - §13.7;
  - §19.1 and §19.5;
  - §31.6;
  - closure-map rows 3 and §5.
- I listed the 27 §21 items from the workplan at the candidate and located the deciding text myself for every item the diff or B1 touches (2, 3, 5, 7, 8, 13, 24). I used the closure map only to find text; its row-3 claim is corrected under N4.
- For the other items, every other section is byte-identical to the candidate `63ddf91` reviewed. I re-read §3-§13.7 and §19 in full.

**Not substantively resolved at this candidate:**

| §21 item | Clause | Gap |
|---|---|---|
| 3 | judgment kinds (supersession authority per kind) | The transformation `REVIEW`/`CONFORMANCE` relief reaches item revisions and bases the superseder did not judge (B1) |
| 7 | obligation rules (adjudication, discharge) | A vetoed passing review discharges after a revert without adjudication of its disagreement (B1) |
| 8 | plan acceptance | The objective revision is in the target only through the preamble (N1, non-blocking) |
| 24 | task-partition checks | Lint text is inconsistent for a re-partition (N2, non-blocking) |

Item 2 (boundary-completeness judgment semantics) is now resolved (`63ddf91` B1 closed). Item 13 is resolved, with non-blocking residue (N3).

**§16.2.** Both tables are resolved in §26.4, which is unchanged since `63ddf91`. Every workplan `Deferred` row has a final disposition there.

**Material decision versus delegated choice.** B1 is an architectural under-specification. I found no new over-specification.

## 4. Refinements R1-R12

| # | Assessment |
|---|---|
| R1 | **Sound as a construction**, unchanged. `on⁺ ⇒ on⁻ ⇒ link⁻` holds, and the guard holds. With the `COMPLETENESS` target repaired, `bound` no longer reads a wrongly regained currency |
| R2, R3 | Sound; unchanged |
| R4 | Sound; the fenced-cutover half state and re-application are disclosed (§19.5, §32.2) |
| R5, R6, R7 | Sound; unchanged |
| R8 | **Unsound for one widened kind.** Same-target supersession is sound for every kind whose target is the exact thing judged. The widened target for a transformation's `REVIEW`/`CONFORMANCE` reaches item revisions and bases the superseder did not judge (B1). The widened gate target is sound because of `gterm`'s minimum |
| R9 | **Veto sound. Relief sound** for gate decisions and every exact-target kind, **too wide** for transformation reviews (B1). Exact-target statements depend on the preamble for `PLAN_ACCEPTANCE`'s objective (N1) |
| R10 | Sound; unchanged |
| R11 | Sound; `gterm`, `unq` and `elig` are unchanged |
| R12 | Sound; the why-column residue is fixed |

## 5. Previous findings re-derived

"Closed" means I re-derived that the present text excludes the named trajectory. It is not runtime evidence.

**Depth.**
- In full against the new text: `63ddf91` B1 and N1-N6.
- For older records, I took the `63ddf91` record's dispositions as hypotheses. I confirmed that every governing section outside the diff hunks listed in section 3 is byte-identical to `63ddf91`, and re-checked each mechanism those hunks touch.
- I did not re-read every older record's prose.

### 63DDF91

| ID | Disposition |
|---|---|
| B1 (`COMPLETENESS` supersession across revisions) | **Closed.** The target is `(X, R, membership)` at the member revisions the `content` basis names, equal to `same`. `H`'s `COMPLETE` at `v2` naming the `v1` `INCOMPLETE` is rejected, and after the revert `c_A` stays vetoed. (R) states it |
| B1 family | **Recurs as B1** in the widened review target, which the `63ddf91` sibling check cleared on a `same`-equality criterion |
| N1 (`PLAN_ACCEPTANCE` relief) | **Closed as stated.** The objective is omitted (N1) |
| N2 (re-partition) | **Partly closed** (N2) |
| N3 (a) admitted-frame cutover record | Closed (§19.1, (S)) |
| N3 (b) parallel carriers | **Closed as to enactment**; refusal shape and frame undefined (N3) |
| N3 (c) re-application | Closed as a disclosure |
| N4 | Closed (R12 why-column; R8 lists the widened targets) |
| N5 | **Partly closed** (new gaps N5) |
| N6 | Stakeholder; carried as N7 |

### 63DDF91 out-of-matrix table, re-read

The `63ddf91` trajectory 12 ("Owner's `REVIEW PASS` on `X2` lifting `NO_PASS` on `X1` with identical content but another base: Held: symmetric with the veto, which ignores the base") **fails on a revert of the base**. This is B1 trajectory B.

### F03B15E, 61CD09B, 362AF9F, F22B4DC, B46C250 (both families)

| Review | IDs | Disposition |
|---|---|---|
| F03B15E | B1 (trajectories 1-2, (i)-(iii)) | Closed |
| F03B15E | B2 and siblings | Closed |
| F03B15E | N1-N3 | Closed |
| F03B15E | N4 | Closed |
| F03B15E | N5 | Partly closed |
| F03B15E | N6 | Stakeholder |
| 61CD09B | B1 (gate veto relief across runs) | **Closed for gates**. For transformation reviews its repair (the widened target) is **B1** here |
| 61CD09B | B2 | Closed |
| 61CD09B | N1-N5 | Closed or superseded |
| 61CD09B | N6 | Partly closed |
| 61CD09B | N7 | Stakeholder |
| 362AF9F | B1-A | Closed |
| 362AF9F | B1-B | Closed |
| 362AF9F | N1-N5 | Closed |
| 362AF9F | N6 | Partly closed |
| 362AF9F | N7 | Stakeholder |
| F22B4DC | B1-A to B1-F | Closed |
| F22B4DC | N1-N4 | Closed |
| F22B4DC | N5 | Partly closed |
| F22B4DC | N6 | Stakeholder |
| B46C250, different family | B1-A to B1-D | Closed |
| B46C250, different family | N1, N3, N6 | Closed |
| B46C250, different family | N2 | Disclosure |
| B46C250, different family | N4 | Partly closed |
| B46C250, different family | N5 | Stakeholder |
| B46C250, same family | B1 | Closed |
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
| E2154AC | B1, N1-N5 | Closed |

### 3540D98 (GPT family), 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363

| Review | IDs | Disposition |
|---|---|---|
| 3540D98 | B1, B2, B4 | Closed |
| 3540D98 | B3 | Closed for its trajectory; the judgment family recurs as B1 |
| 3540D98 | N1 | Closed |
| 3540D98 | N2-N4 | Held as disclosures |
| 798B2B4 | B1-B4, N1-N8 | Closed |
| 71CF9B3 | B1-B2, N1-N8 | Closed |
| 86AB683, 1FFBBF0 | B and N items | Closed (SD-18 class unchanged) |
| 53669A5 | B1-B3, N2-N9 | Closed (N4's supersession counterpart now also closed) |
| 53669A5 | N1 | Stakeholder |
| D837363 | B1-B4, N1-N8 | Closed |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

| Review | IDs | Disposition |
|---|---|---|
| CC005DB | B1-B3, N1-N8 | Closed |
| C6DA678 | B1 | Closed |
| C6DA678 | B2 (item-revision-independent veto) | **Closed for the veto**; its relief counterpart is B1 |
| C6DA678 | B3, N1-N12 | Closed |
| B595F2C | B1-B3, N1-N8 | Closed |
| B595F2C | B4 (no resolution by re-dispatch, count or order) | **Partly closed**: reopened for transformation reviews by B1 |
| 6FF4ED1 | B1-B4, N1, N3-N12 | Closed |
| 6FF4ED1 | N2 (R8 reconciliation) | **Partly closed** (B1) |

### Phase B §3 closures and N1-N4 carry-forward

| Closure | Present reconstruction |
|---|---|
| Completeness polarity (Phase B N2), both directions | **Held.** §6 is unchanged. A differing old-content run on a tree that differs from `tree(a⁻)` only outside a recorded narrow basis stays in (2) through `link⁻` with `o' = real(a⁻)`, and a yielding present-content run stays in (4). Under a bounding judgment that becomes `P`, blocked, revoked or loss-withheld, only (1) and (3) narrow (`on⁺` reads completeness positively). The restrictive direction holds: a stop is withdrawn only by a newly admitted narrow anchor. The `63ddf91` caveat (a bounding judgment wrongly regaining currency) is **closed** by the repaired `COMPLETENESS` target |
| Support cycles fail closed; corrupt prefixes | Held: §5.6 clamp, §5.7 `INTEGRITY_HALT`; supersession authorization is an admission fact |
| Y1/Y2, X1-X3, candidate-own latch, floor and class | Held (§6.8 unchanged) |
| Contrary-run retention, nondeterminism, U1/U2/W1/W2 | Held (§6.6 unchanged) |
| Absorbed relaxation; adversity versus currency, challenge, loss; salvage; independence; start latch; structure, quarantine, tenure; publication and fencing | Held |
| Phase B N1 | Disclosed (§32.2) |
| Phase B N3 | Held (§31.3) |
| Phase B N4 | Held (§32.3) |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | `NO_PASS` on `X1`/`i1`; amendment to `i2`; owner `PASS` on `X2` superseding; `X2` integrates; foreign revert of plan and code; `X1` integrates on an agent `PASS` | **Fails: B1** (A) |
| 2 | `NO_PASS` on `X1`; context change; owner `PASS` on rebase `X1'` superseding; context revert; `X1''` integrates on the agent `PASS` | **Fails: B1** (B) |
| 3 | As 1 for `CONFORMANCE` (`NONCONFORMANT` on `X1` with item revision) | **Fails: B1** |
| 4 | Gate `REJECT` (core `E1`) superseded by holder's `ACCEPT` (core `E2`); revert; peer `ACCEPT` on `E1` | Held: `gterm` minimum keeps the holder's own decision binding |
| 5 | `NATIVE` D1/D2 gate: `REJECT` in run `R1`, relief in `R3`, peer `ACCEPT` from `R1` | Held: `tgt` (run) |
| 6 | `63ddf91` B1 (`COMPLETENESS` `v1`/`v2`/revert) | Held: superseder rejected (`AUTH_SUPERSEDES`) |
| 7 | `COMPLETENESS` analyzer record versus human `INCOMPLETE` | Held: the human vetoes; the machinery record cannot supersede the human's |
| 8 | `PLAN_ACCEPTANCE` objective `o1`→`o2`→`o1` with relief at `o2` | Holds under the preamble; **fails under the row read literally** (N1) |
| 9 | `PLAN_ACCEPTANCE` `REJECTED {A1, B1}`; `B` amended; owner relief | Held, fails closed; challenge route stated |
| 10 | `ACCEPTANCE FAIL` in an abandoned frame; owner `PASS` in a later frame | Held under the triple reading; restrictive under the frame-in-target reading (N1) |
| 11 | `ACCEPTANCE` context revert after owner relief on the same triple | Agent `PASS` revives; reviewed-contract residue (N6) |
| 12 | `EQUIVALENCE` `NOT_EQUIVALENT` class `k` relieved by the owner; agent `EDITORIAL` | Held: no unjudged adverse judgment remains |
| 13 | `IMMATERIALITY` superseded by another about another governing state; revert | Held: restrictive (the disposition is lost) |
| 14 | Re-partition after part 1 discharged; part 1 later reopened by drift | Fails closed; text inconsistent (N2) |
| 15 | Two pending carriers; first integrates the cutover | Second refused; frame undefined (N3) |
| 16 | Admitted-frame cutover record | Held: refused |
| 17 | Fenced cutover; re-application | Held as disclosed |
| 18 | Stratification with the repaired target | Held: authorization is an admission fact; `stands⁻` reads S0/S1 |
| 19 | `rid` uniqueness under rebase, re-dispatch and resubmission | Held (§10.2 unchanged) |
| 20 | Phase B N2 polarity variants | Held (section 5) |
| 21 | Structure, `ignore` or analyzer change with `K` fixed | Held (guard unchanged) |

**Where I stopped.** I stopped discovery once B1's cause was characterized and every adverse-capable kind had been placed in the section 1 sibling table. Further search would be implementation-like:
- every lifecycle kind's frame behaviour;
- every obligation identity's parameterization by item revision.

Trajectory 1 depends on an obligation identity that is equal, or recurs identically, when the item returns to `i1`. §10.2's deterministic identity makes it recur. Trajectory 2 does not depend on it. Section 6 is a bounded negative result elsewhere, not a completeness claim.

## 7. Minimum architecture and capability transfer

- **What `051cce3` changes.** It states the target rule once, corrects one target row and states three relief, partition and cutover rules. It adds no component, store, record kind or tier. The `COMPLETENESS` repair is subtractive and the right shape.
- **Mechanism at issue.** The widened review target (from `61cd09b`) is the mechanism B1 targets. Option 1 removes it and adds one exemption clause; Option 2 adds a latch.
- **Dropped capability.** None found.
- **Withdrawn protection (B1).** A standing human `NO_PASS` loses its protective effect on a reverted item revision or base.
- **§30.** Accurate except as B1 affects R8.
- **Architecture 1.6.0 supersession (PC-001).**
  - §26.4 preserves the version-bound Level 0 Core, the frozen profiles and the single composition root.
  - `orchestrator/docs/architecture.md` is byte-identical to `fad3ee4` (blob `39e6de7`).
  - Nothing under `source/` or `dist/` changed (section 10).
- **PEM Historical Applicability Set.** PEM was activated, because this is replacement of mature machinery under a memory-bound workplan. The PEM file is blob `1561797` at the candidate and in the checkout, and schema-valid.

| Entry | Applicable | Disposition |
|---|---|---|
| PC-001 | yes | Held, as above |
| DS-001 | yes | Applied in N5: §31.6 (N) encodes B1 |
| FF-001 | yes, for genesis and cutover | Held |
| SP-001 | no | No source-to-package routing change |
| SP-002 | no | No immutable self-reference construction in this cycle |

I did not re-read the archived §18 inheritance workplans. The diff touches no inherited capability.

## 8. Qualification-design adequacy

- **Status.** §31.1 correctly marks every runtime group `UNEXECUTED`. G1 needs only §31.10, which I ran (section 10).
- **Discrimination.**
  - (R) now discriminates `63ddf91` B1, and (S) the admitted-frame and second-carrier refusals.
  - §31.6 (N) expects the widened review relief and its discriminator requires it, so an implementation built to §31 would encode B1.
  - No case covers a revert after cross-target relief (N5).
- **Executed-evidence claims.** Nothing is claimed as executed beyond §31.10.
- **Diagnostic model.** Optional. I did not run it; it is unchanged and models none of the clauses at issue.

## 9. Doctrine-realization map and O1

- **Coverage.** §29.1-§29.7 are unchanged since `63ddf91`. All seven 7.2.1 entrypoints and the scientific checks are mapped with E0-E3 levels, and §29.6 discloses the E3 duties.
- **Rows that depend on B1's repair.**
  - The D1-D3 row "durable authority mutation needs its acceptance process, independent falsification ..." (E0) is unaffected for D1/D2, where a human `ACCEPTANCE` is also required.
  - Review-route rows that rely on independent review being the deciding judgment for D4 items depend on B1's repair, because B1 lets an agent's vetoed review decide after a revert.
- **Other rows.** No other row overclaims beyond the limits its level discloses.
- **O1 (§0.5).** Unchanged and adequate:
  - the realized record, readers, routine questions and realized-record architecture are stated;
  - product surfaces are marked within the deliverable;
  - **none** is marked beyond it.

  Product-scope acceptance remains with the stakeholder (S12).

## 10. What I verified and how; what I could not verify

**Verified.**

- Reviewed exactly `051cce30ff64566ea79bb5d25e97daf803dc6c51` through a `git archive` snapshot in `$TMPDIR/ssds80-manual-review-051cce3/`. Blobs confirmed: Manual `a3532ab…`, closure map `0a81fd3…`, workplan `91bde23…`.
- Diffed `63ddf91..051cce3` by word for the Manual and the closure map.
- Read the `63ddf91` Review in full, and workplan §21.
- Read the governing owners at `aaeaf8b`: the D3 role entrypoint; architecture (formal-contract discipline); evidence (assessment disagreement); workflow (synthesis by vote); convergence (simplification trigger, Review strategy after recurrence, review readiness). `PROTOCOL-RELEASE-STATE.yaml` gives public source `aaeaf8b` and recovery `efdd1b5`.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the candidate snapshot: **4 tests OK**.
- `git diff --check 63ddf9174c79d013fc555d16f55ef377a4b6e9df 051cce30ff64566ea79bb5d25e97daf803dc6c51`: clean (exit 0).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 051cce30ff64566ea79bb5d25e97daf803dc6c51`: 59 files, 18,738 insertions and 1 deletion. They are the Manual, `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`, and 57 files under `qualification/ssds80/`.
- `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4` (empty diff; frozen blob `39e6de7`).
- PEM: `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md` gave "PEM schema 1 valid: 5 families, 0 notices"; blob `1561797`.

**Not verified or not established.**

- No production or runtime behaviour; none exists at G1.
- The diagnostic model was not run.
- I did not read line by line §14-§18, §20-§25, §27-§28 and §29.4-§30; they are byte-identical to `63ddf91`.
- I did not re-read every older Review record's prose or the archived §18 workplans.
- B1 is deductive from the Manual's own rules. It depends on:
  - §8.3 step 3's widened review target;
  - §5.5 `same` reaching any item revision and any base;
  - `stands⁻` not reading the superseder's currency;
  - §5.2's permanent acting after integration;
  - §10.4's ∃ discharge and non-latched discharge;
  - §7.6's rebase counting.

  I searched the candidate for any rule that withdraws a vetoed passing review or ties relief to the superseder's item revision or base, and found none.

## 11. Scientific-checks answers

- **Material findings.** None about scientific or numerical meaning. B1 and N1-N7 are D3 findings about software that mediates scientific evidence. B1 decides whether a human reviewer's standing objection to a candidate stays visible and decisive after a revert.
- **Realized results.** I produced, ran and reviewed no realized scientific results. Null envelope: I examined the Manual's D3 text, the governing owners and prior Review records. Materially unexamined: any runtime evidence (none exists) and the diagnostic model.
- **Variants.**
  - Repair directions for B1: two viable and one rejected, of kind D3 options. The criterion was to keep relief inside what the reliever judged while preserving liveness, and to prefer removing mechanism. Option 1 is recommended.
  - Trajectories: 21, of kind out-of-matrix (section 6).
  - Sibling check: every adverse-capable kind, by the five comparisons in the header.
- **Reliance on accepted D1/D2 authority.** I relied on no accepted D1/D2 authority for a consequential judgment, so no tension search was owed.
- **Gaps.** Runtime qualification (G2-G4), the unchanged sections not read line by line, older records' full prose, and the archived §18 workplans.

## 12. Common-mode note

- **Family.** I am of the Claude family, the same as the Manual's author and as the reviewers of e2154ac, e9e6e9f, a18b544, 0b6c4fa, 27ef339, 5c55d4b, 575dc78, f7419d5, the same-family b46c250, f22b4dc, 362af9f, 61cd09b, f03b15e and 63ddf91. The 3540d98, different-family b46c250 and Phase B reviewers were of the GPT family.
- **Engagement.** I was engaged as a fresh-context sub-agent launched by the authoring session.
- **Shared dependencies.** Fresh context does not make me independent. I share:
  - the corpus;
  - the inherited workplan framing and its target, veto, enactment, run and acting vocabulary;
  - the prior Review records, which I read and which shaped my attention;
  - the toolchain;
  - the model family with the author and with most prior reviewers.
- **Provenance of B1.** I found B1 by applying the `63ddf91` B1 cause to the two kinds that record exempted. The widened target entered through the `61cd09b` same-family Review's suggestion and was kept by two later same-family Reviews. One of them explicitly tested and passed a variant of this trajectory without the revert (`63ddf91` trajectory 12). That is evidence of shared-framing risk. A different-family review of the supersession and veto design as a whole, rather than of the latest repair, would reduce it.

## 13. D4 statement

No SSDS 8 D4 is authorized. This Review accepts no architecture, product scope or proposed default. G1 remains open: it needs a repaired Manual candidate, an independent D3 Review with no surviving blocker, and explicit stakeholder acceptance. Shadow implementation additionally needs G2.
