# SSDS 8 Architecture Manual — Independent D3 Review, candidate f22b4dc

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: f22b4dc4c5cc56da962bee9eca843fa204af40bc
    SCOPE: whole proposed Manual as durable D3 owner: (a) closure of workplan §21 and both §16.2 tables;
           (b) fidelity and refinements R1-R11; (c) adequacy (out-of-matrix); (d) inheritance, capability
           transfer and PEM HAS; (e) qualification design; (f) doctrine-realization map; (g) O1
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob 976bececc691920b63116f3e0836f6bd52052858
    CLOSURE MAP (aid, not authority): qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md,
           blob 1247127deea389ef120e6991feb2cc5525f646c7
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
           27EF339, 5C55D4B, 575DC78, F7419D5, B46C250 (same family) and B46C250 (different family);
           Phase B PASS E23F142
    REVIEW METHOD: immutable-candidate reconstruction (git archive of the candidate), whole-Manual read,
           deductive falsification in both directions with family/sibling closure (convergence owner,
           "Review strategy after recurrence"), prior-finding regression, G1 document checks
    REVIEWER: Claude model family, the same family as the Manual's author; a fresh-context sub-agent
           launched by the authoring session, with none of the authoring conversation
    MUTATION: this record only; no commit, no push

All Manual section numbers below refer to the candidate blob above. Quotations of governing owners are from the public-source commit `aaeaf8b`.

## SERIOUS CHALLENGE

**None against accepted authority.** SSDP 7.2.1, the reviewed workplan contract, the frozen Architecture 1.6.0 and the stakeholder record are not shown to be false, contradictory or unrealizable. The blocker below is a defect in the proposed D3 Manual. The owners it violates are coherent and realizable.

Owner texts applied (public source `aaeaf8b`):

| Owner | Exact text |
|---|---|
| D3 role, Independent Review and Challenge | "Literal workplan compliance is insufficient when the workplan/architecture itself is too weak for the protected outcome." |
| Architecture, D3 formal-contract discipline | "When an architectural concept carries normative meaning, define it before dependent invariants use it" |
| Evidence, Change impact and closure | "Restoring an old file does not restore old evidence validity by timestamp." |
| Evidence, Assessment disagreement | "supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement. An unresolved material disagreement keeps dependent present guidance/closure visibly qualified." |
| Scientific checks, revising D1/D2 authority | "When revising, renaming, splitting, merging or replacing D1/D2 authority, also search recorded tensions bound to its accepted concretizations. In the revision's own record and its gate evidence, record the predecessor identity and, per found tension, a revision-scoped applicability assessment" |
| Workflow, Human gates (Channel C) | "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments, including those marked inapplicable, with their asserters. Acceptance does not ratify an assessment the gate was not shown." |
| Workflow, Human gates (Channel C) | "The gate does not close unqualified when missing realized records could plausibly change its judgment." |
| Convergence, Active simplification trigger | "Active simplification/re-derivation is **mandatory before another additive durable repair**" under the stated recurrence triggers |
| Convergence, Review readiness | "Review sufficiency is not proof of zero conceivable defects." |
| Testing (via DS-001) | qualification evidence must stay bounded to the property its method actually tests |

Reviewed-contract and stakeholder texts applied:

- Workplan §2 S11: "An acceptance belongs to one subject tenure and never revives once that tenure ends; restoring old bytes or old declarations restores no validity."
- Stakeholder record SD-22 (standing in its protected property; SD-25 changed only how the run is identified): "for a `NATIVE` D1/D2 subject, an acceptance or gate decision is current only if admitted, or bound by integration, at or after the latest admitted position at which `cur(s)` took its current value".
- Stakeholder record SD-25: "a revision run is identified by the event that starts it, not by its ledger position, so a frame can name the run its integration would start".

## Verdict

**NO-PASS.** One blocking D3 family survives: **B1**.

The SD-25 repair uses the **enactment lineage** (the bound obligation of §7.6 rule 1) as if it named **one enactment**. It does so twice:

- in the acting rule (§5.2): a frame record acts in the admitted state once "that lineage integrates";
- in the revision-run identity (§10.2): an integration's event `ι` is "its enactment lineage".

A lineage is not one enactment. It contains transformations that never integrate (earlier iterations, partition siblings), and it can enact more than once (an implementer obligation whose S3 discharge lapses and is dispatched again; partition parts; a re-requested cutover). The Manual's stated premise for uniqueness, "Admission discharges or answers each obligation at most once (§8.3 step 7), so no two events share `ι`", is not established by step 7, which checks only that the claimed obligation is "undischarged at the current head".

Consequences with concrete trajectories:

- **B1-A (D1-D3 change-rule family, permissive).** A `NATIVE` D2 subject restored to an earlier revision by the same lineage re-enters its earlier run. The old acceptance, gate decision and revision-assessment record become current again with no new acceptance, no new gate and no gate shown the revert. This contradicts R10, workplan S11, SD-22's protected property and §10.2's own sentence.
- **B1-B (gate/frame family, both directions).** A reassessment recorded in a rejected iteration's frame acts in the admitted state once a later iteration of the same lineage integrates. It lifts an admitted veto on evidence that never integrated (the b46c250 B1-A harm). The gate variant drops an admitted `P` to `F` (the b46c250 B1-B harm).
- **B1-C (regression).** f7419d5 B1 (vii) is reopened: an earlier iteration's gate decision on a revision its lineage never integrated becomes eligible when identical bytes arrive later. §31.6 (F) still asserts the opposite.
- **B1-D, B1-E, B1-F.** Partitioned tasks, cutover requesters and ruleset re-identification leave the run identity non-unique or undefined.

The SD-25 repair otherwise closes what it targets:

- the b46c250 single-iteration trajectories (B1-A and B1-B with one pending or abandoned candidate);
- computability of frame obligation identities before issue (B1-C);
- unchanged-subject run membership (B1-D);
- every b46c250 non-blocking finding (N1, N2, N3, N6 closed; N4 partly closed; N5 a stakeholder matter).

The assessment-disagreement matching clause (§6.5-§6.6) has no new defect. It is touched by B1-B only through dispositions that read the acting rule.

This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blocker by earliest owner

### B1 — SD-25 treats an enactment lineage as one enactment, in both the acting rule and the revision-run identity

**Family and earliest owner.** Proposed D3, Manual:

- §5.2 (acting records; `superseded_G`; `tgt`);
- §10.2 (revision run `rid`, run membership, obligations);
- §5.5 (`stands⁻`, `elig`, gate-term prose);
- §6.7 (`eff` of a supersession);
- §7.5-§7.6 (declared frame, enactment lineage);
- §13.7 (partition);
- §19.5 (cutover run);
- §8.3 steps 2 and 7;
- §10.3-§10.4 (answering and discharge);
- §31.5-§31.6.

These realize workplan §21 items 5 (declared frame per kind, prospective-acceptance rule), 7 (obligation rules, discharge, iteration identity), 13 (cutover) and 24 (task-partition checks).

This is a **non-local recurrence**. It is the tenth round of the gate-qualification family (3540d98 B3 → … → f7419d5 B1 → b46c250 B1). It is also a new route to the property the D1-D3 change-rule family protects (no D1/D2 revival on revert: 71cf9b3 B2, 798b2b4 B1-B3). It entered through the SD-25 repair. Part of the run sibling (B1-A) was latent earlier: the b46c250 run-membership rule already admitted "an earlier iteration or rebase of the same enactment lineage". It is now made explicit by the Manual's new uniqueness claim.

**Contract text the trajectories violate (Manual, candidate):**

- §10.2: "`ι` identifies the event at which `cur(s)` took its current value in `G` … for an integration, its enactment lineage … Admission discharges or answers each obligation at most once (§8.3 step 7), so no two events share `ι` … a later change of `cur(s)`, including a return to earlier bytes, is a new event and a new run."
- R10: a `NATIVE` D1/D2 subject "has its acceptance and gate decision current only within the revision run in which they were made, a run identified by the event that started it (§10.2), so restoring an earlier revision's bytes restores no D1/D2 validity and derives a new revising review, acceptance and gate".
- §5.2: "An admitted record **acts** in `G` iff it declares the admitted frame; or it declares a frame of an enactment lineage (§7.6 rule 1) that has integrated at or before `n`; or `G = D_n[X]` and it declares a frame of `X`'s own enactment lineage (`X`, its earlier iterations, its rebases)."
- §5.5: "a reassessment recorded in a candidate's frame ends the veto in that frame and, after integration, in the admitted state, never in the admitted state while the candidate is pending or after it is abandoned (b46c250 B1)".
- §8.3 step 7: "Each obligation whose discharge the request claims is undischarged at the current head (a duplicate discharge is rejected and recorded)".
- §10.4: "Discharge is an S3 classification"; §5.8: S3 holds the "Non-monotone functions"; §27.1: "a previously discharged obligation the new ruleset no longer considers discharged becomes open".

#### B1-A. Permissive: a same-lineage restoration re-enters the earlier run and revives D2 validity

**Setup.**
- `s` is a `NATIVE` D2 subject. Policy keeps the defaults: R3 acceptance for D2, and a required D2 human gate `g`.
- Item `I` is an accepted `AUTHOR` item (authority D2). Its obligation is `o = AUTHOR(I)`.

**Trajectory.**

1. **Iteration 1.** Task `t1` produces `X1`, changing `s` from `r0` to `r1`.
   - `t1`'s `TASK_RESULT` carries `revision_assessments` for `(s, r1)`. Its displayed predecessor is `r0`.
   - In `D_n[X1]`, `rid(s) = (s, o)` (§10.2: `ι` is `X1`'s enactment lineage).
   - `REVIEW(X1)` passes. In `X1`'s frame, the D2 owner records `ACCEPTANCE PASS j1` on `(s, σ, r1)` and holder `H` records `GATE_DECISION ACCEPT h1`. Both name `(s, o)`.
   - Integration `k1`, bound to `t1`, claims `o`. Admitted `rid(s) = (s, o)`. `j1`, `h1` and `t1`'s record act and are in the run, and `valid(s) = T`.
2. **Foreign change.** A foreign change (legacy-route push, manual edit or restore) changes `s` and is absorbed at `k2`.
   - `cur(s) = r2` and `rid(s) = (s, k2)`. `j1` and `h1` leave the run, `valid(s) = F`, and `REVIEW(s, r2)`, `ACCEPT` and `GATE` are derived. All correct.
   - `REVIEW(X1)`'s output-role entry on `s` now needs "ordinary currency in the admitted state" (§7.3) and fails. So does `j1`'s.
   - Therefore `discharged(o)` (§10.4: "∃ current judgment j of kind(o) on subject(o)") is false, and `o` is `OPEN`.
   - Its item is still accepted and issuable, so `o` is ready (§10.3). The Dispatcher may dispatch iteration 2 within the default budget of 3 (§13.7).
3. **Iteration 2.** Task `t2` re-applies the authored text over the foreign clobber, producing `X2` with `rev(s, C2) = r1`.
   - In `D_n[X2]`, `X2` changes `cur(s)`, so `rid(s) = (s, o)`. That is **the same `ι` as `k1`'s event**.
   - `j1`, `h1` and `t1`'s record act (lineage `o` integrated at `k1`; also `X2`'s own lineage). They name `(s, o)`, so they are in the run.
   - Their bases hold: `content (s, r1)` against `M_n(X2)`; unchanged governing and evidence records.
   - So:
     - `REVIEW(s, r1)` is not derived, because a counting record exists;
     - `ACCEPT(s)` is answered and discharged by `j1` (§10.3);
     - `elig(g) ∋ h1` and `gterm(g) = T`.
   - Integration `k3`, bound to `t2`, claims `o`. Step 7's test "undischarged at the current head" holds, so `k3` is admitted with `valid(s) = T`.
4. **Variant without absorption.** Another `AUTHOR` item `I'` revises `s` from `r1` to `r2` through its own run, accepted and gated. `o`'s discharge lapses as in step 2. Iteration 2 of `o` reverts to `r1`. Same result, and the accepted `r2` is the skipped predecessor.

**Violation.** A D2 revision change `r2 → r1` becomes valid, accepted and gated through records decided on the different change `r0 → r1`.

- No acceptance or human gate decides the revert.
- `h1`'s core (§16.6 section 3) showed the predecessor `r0` and never the tensions recorded on `r2` or since `k1`.
- The predecessor display itself becomes ambiguous: "the last revision … before the run started", but the run `(s, o)` started twice.

This contradicts:
- §10.2 and R10 (quoted above);
- workplan S11 "restoring old bytes … restores no validity";
- SD-22's protected property ("at or after the latest admitted position at which `cur(s)` took its current value");
- the evidence owner's "Restoring an old file does not restore old evidence validity";
- the workflow owner's "Acceptance does not ratify an assessment the gate was not shown".

**Alternative reading.** If "at most once" were read as a historical latch (Admission refuses any later discharge claim of `o`), then `o` is `OPEN`, ready and dispatched indefinitely, while its integration is always refused. That is a livelock nothing states. An implementer must choose between the two readings, so the uniqueness premise is either false or an unstated rule with an unstated liveness consequence.

#### B1-B. Both directions: an earlier iteration's frame reassessment acts after a later iteration integrates

**Setup.**
- `s` is a `NATIVE` D3 subject at `(s, σ, r)`. A D3 subject is used so that no revision-assessment condition applies.
- In the admitted state, a reviewer agent's `ACCEPTANCE PASS p` (bound to `ACCEPT(s)`) and human `H`'s `ACCEPTANCE FAIL f` (never-lost) stand on the same triple.
- So `vetoed(p)`, `valid(s) = F`, and `ADJUDICATE_DISAGREEMENT(f)` is derived. Correct.

**Trajectory.**

1. Iteration `X1` of item `I` (lineage `o`) leaves `s` unchanged and adds evidence specification `E` with realization `ρ1`, which persuades `H`.
2. `H` records directly an `ACCEPTANCE PASS d` in frame `id(X1)` on `(s, σ, r)`, with `supersedes = [f]` and a `record` entry on `ρ1`. Admission checks:
   - §7.5 permits the frame (the subject is effective in it);
   - step 3: own author's reassessment, same kind, same target;
   - step 6: current in `D_n[X1]`;
   - step 7's `OBLIGATION_ANSWERED` concerns judgments bound to the answered obligation, and `d` is a direct human record.

   `d` is admitted. While `X1` is pending, `d` does not act in `D_n`, `f` stands, and the result is correct.
3. `X1` is rejected (`REVIEW NO_PASS` on a D4 defect). A fresh task produces iteration `X2` of the same lineage without `E` (or with different content there). `X2` passes and integrates at `k`.
4. At `k`, `d` acts, because §5.2 makes every frame of an integrated lineage act. Then:
   - `superseded(f)` holds;
   - `stands⁻(f)` is false: `d` acts, is unsuperseded, `CLEAR` and `cont`, and §5.5 asks nothing about currency;
   - `p` is no longer vetoed and is current, so `ACC(s) ∋ p` and `valid(s) = T`;
   - `ADJUDICATE_DISAGREEMENT(f)` disappears;
   - `d` is non-current (`ρ1`'s execution basis fails against `T_k`), but no obligation depends on `d`, so no `REVALIDATE` is derived.

**Violation (permissive).** The only objection is lifted in the admitted state by a reassessment whose ground never integrated. That is exactly the b46c250 B1-A harm, which §5.5 says cannot happen ("never in the admitted state … after it is abandoned"). It also breaks the evidence owner's distinction between resolved reassessment and live disagreement.

The same holds for:
- `REVIEW`, `CONFORMANCE`, `PLAN_ACCEPTANCE`, `EQUIVALENCE`, `COMPLETENESS` and `INTAKE_DISPOSITION` vetoes;
- the owner's adjudication recorded in `X1`'s frame;
- failing assessments (§6 family): an owner's adjudicating supersession of `a⁻` in `X1`'s frame disposes `a⁻` in the admitted state after `X2` integrates, because a supersession's `eff` is `base(d)` (§6.7) and stands on immutable facts.

**Gate variant (restrictive).** `H`'s admitted `QUALIFIED` decision `q` is superseded by `H`'s `UNQUALIFIED` decision `d` in `X1`'s frame, relying on `ρ1`. `X1` is rejected and `X2` integrates. Now `q` is superseded in `D_n`, and `d` is eligible but non-current. `gterm` drops from `P` to `F`, and permitted provisional work stops. This is b46c250 B1-B through an iteration that never integrated. §31.6 (D) tests only one pending or abandoned candidate, not this route.

#### B1-C. Regression of f7419d5 B1 (vii): an earlier iteration's gate decision becomes eligible when identical bytes arrive

At b46c250, `elig` admitted a frame decision in `D_n` only "for the obligation that integration produced". The same-family b46c250 Review recorded f7419d5 B1 (vii) as closed by that phrase. SD-25 deleted it. §5.5 now reads: "every authenticated passing GATE_DECISION acting in G, not superseded in G, on the gate obligation G derives for g".

**Trajectory.**
1. `X1` changes a gated D3 subject (or a D2-domain evidence specification) to `r1`, and `H` records `h1` in its frame.
2. `X1` is rejected, and `X2` of the same lineage integrates `r2`.
3. Later, an absorption or another lineage brings `r1`. Now `h1` acts and is on the gate obligation derived for `(s, σ, r1)`, so it enters the minimum:
   - permissively, if it is current and `UNQUALIFIED`;
   - restrictively (`F`, or `P` that only `H` or the owner can retire) otherwise.

§31.6 (F) still expects: "an earlier iteration's decision on a revision its lineage never integrated never counts when identical bytes arrive later". The normative rule and the qualification design contradict each other.

#### B1-D. Partition parts share one lineage

§13.7: a `PARTITION` "splits the **execution** of one item revision into tasks, never the item … The item is discharged when every part is". The tasks therefore carry the item's obligation, and their transformations share one lineage.

- **(i) Acting.** After part A integrates, every frame record of part B acts in the admitted state while B is still pending, and permanently if B is abandoned. This is the B1-B harm without even a rejected iteration.
- **(ii) Run identity.** If A and B each change a `NATIVE` D1/D2 subject composed of parts in both write scopes, both integrations have `ι = o`. `s` stays in one run across two changes of `cur(s)`, contrary to §10.2.
- **(iii) Binding.** The Manual does not state which obligation each part's integration claims. §11.5 says an integration claims "its obligation", while §13.7 discharges the item only when every part is. The implementer must decide an architectural binding.

#### B1-E. The cutover's run identity is not defined

§10.2 gives "for a cutover, the obligation that requested it". §19.5 names two possible requesters: "a `MIGRATE` item whose contract names `s` and its native revision" or "the cutover gate's derivation".

- **The gate case is self-referential.** §10.2 makes `GATE(g)` "carry `rid_G(s)` among their parameters", so the run would be defined through an obligation whose identity contains the run.
- **The `MIGRATE` case can repeat.** A re-cutover after version rollback requested under the same item obligation (its §10.4 discharge can lapse like `o`'s in B1-A) receives the first native tenure's run. Gate decisions have no tenure filter (R10, 0b6c4fa B2). So the first tenure's gate decision and revision-assessment record count again, contrary to:
  - §5.5 "A new revision run's gate (`NATIVE` D1/D2) decides afresh";
  - §31.5 "a re-cutover after rollback … start[s] a new run".
- **Step 2 conflicts with the cutover rule.** §8.3 step 2 requires "a run a record names is its subject's `rid` in the record's declared frame". Cutover records name the run the cutover will start, while their subject is still `LEGACY` and §10.2's rules "apply to every `NATIVE` subject".

The identity an Admission check depends on is undefined (formal-contract discipline).

#### B1-F. `ι` is undefined for lifecycle re-identification

`cur(s)` also changes at a `RULESET_ADOPTION` that changes normalization or the analyzer set resolving `symbol` terms (§27.3 expects such re-identification). This is neither "the admission of a request bound to an obligation" nor an absorption, so §10.2 assigns it no `ι`. The natural completion is the entry identity. On its own this is non-blocking; it is listed because it is the same identity rule.

#### Family assessment and options for the stakeholder

**Common cause.** A-F share one cause: SD-25's unit of enactment is the bound obligation. Each consumer that does not read currency inherits the mismatch:

- `stands⁻` relief and supersession-disposition `eff` stand on immutable facts;
- `elig` membership;
- `tgt` through `rid`.

Consumers that read currency (`base ∧` basis) are protected only where the frame's content changed. This is not a clean local defect. Adding another per-consumer frame clause would recreate the cause of the last four rounds. The convergence owner's simplification trigger applies.

**Option 1 (recommended): narrow the unit from lineage to the integrated transformation.** One rule, and mostly subtractive.

- **Unit.** The unit of enactment is the transformation fixed by one `TASK_RESULT`, carried only across that result's clean machinery rebases (§11.5 step 3).
- **Acting in `D_n`.** Admitted-frame records, plus frame records of transformations that integrated, or of their rebases.
- **Acting in `D_n[X]`.** Additionally, `X` and its rebases.
- **Run identity.**
  - `ι` of an integration is that producing task.
  - Admission must refuse a second integration of one result. This is one ledger check; it **adds mechanism**, minimally.
  - A cutover's `ι` is its own requesting task or request, fixed before issue.
  - A lifecycle re-identification's `ι` is the entry.

What it closes:
- A is closed: re-dispatch is a new task, hence a new run;
- B and C are closed: earlier iterations never act in the admitted state;
- D is closed: partition parts are distinct tasks;
- E and F are closed.

Costs:
- A later iteration needs its own review, acceptance and gate decision. Human gate load per iteration rises.
- §7.6 rule 1 ("a later iteration") prospective-acceptance carry is narrowed to rebases. This changes a reviewed workplan rule (§6.9 rule 1), so it must be listed in §0.3 as a restrictive refinement and put to the stakeholder.
- §31.6 (B)'s earlier-iteration visibility clause becomes unnecessary.

**Option 2: keep lineage acting for currency-read support, and require transformation-level integration only for the immutable-fact consumers.** Those consumers are `stands⁻`, supersession-disposition `eff`, `superseded_G` and `elig`, with `ι` keyed on the producing task. This keeps rule 1's later-iteration reuse, but it reintroduces two notions of "acting", the per-consumer scoping that drove the recurrence. Not recommended.

**Option 3 (workplan-level): decide gates and acceptances, and supersessions of admitted judgments, only in the admitted state on integrated content.** `ι` is the admission entry. This reverses workplan §7.8's integration precondition. It is the option the stakeholder declined at SD-25, and it is listed only because the family has not converged.

**Option 4: latch discharge so that each lineage enacts once.** This adds a latch, and it leaves B, C and D(i) open. Insufficient alone.

**Stakeholder note.** SD-25 chose "one state rule" without fixing its unit. The choice of lineage over transformation was the author's, made under stakeholder record item 19. I would put Option 1 versus Option 3 to the stakeholder, with Option 1's per-iteration gate cost stated.

#### Required discriminators

These run at real owners (Admission → Derivation → discharge → Dispatcher → inspector), with obligation reopening produced by derivation and nothing seeded resolved.

- **(A)** B1-A as written, and its `I'` variant:
  - after `k3`, `valid(s) ≠ T`;
  - `ACCEPT`, `GATE` and the record condition are derived in a new run;
  - `j1`, `h1` and `t1`'s record are in no run;
  - the predecessor shown is `r2`.

  An implementation keying the run on the bound obligation must fail.
- **(B)** B1-B: after `X2` integrates, `f` still vetoes `p` and `ADJUDICATE_DISAGREEMENT(f)` stays derived. The gate variant stays exactly `P`. The disposition variant leaves `undisputed = P`.
- **(C)** B1-C: `h1` is never eligible when `r1` arrives by absorption or by another lineage (§31.6 (F) as stated, now enforced by the rule).
- **(D)** Partition:
  - part B's frame records do not act after part A integrates;
  - two parts changing one D1/D2 subject start two runs;
  - each part's integration claims a defined obligation.
- **(E)** Re-cutover of an unchanged native revision after rollback under the same item: a new run, the first tenure's gate decision is ineligible, and step 2 accepts records naming the pending cutover run.
- **(F)** An analyzer-set adoption that re-identifies a D2 revision starts a new run, and its reversal revives nothing.

## 2. Non-blocking findings

**N1 — The "one rule" claim does not cover §6.6's permissive reads.** §5.2 says the acting rule "is the one rule for which records a state reads permissively". But two permissive reads in §6.6 never mention acting:

- condition (1) and (3) observations ("some standing admitted observation");
- discriminating-reading coverage in (4) (a reading "stands iff `cont(d)`, it is not superseded, …").

A reading recorded in a pending or abandoned frame therefore covers outcomes in the admitted state. I found no violating trajectory: a reading judges outcomes under a reading, and observations are R0 facts. State that both are outside the acting rule and why, as is done for adverse records, so that an implementer does not filter them and silently restrict stops.

**N2 — The acting rule narrows a reviewed contract, but §0.3 does not list it.** Workplan §6.9 allowed "A `record` entry on a record of a different transformation is satisfied only if that record's basis holds in this frame". §7.3 now makes such a record support nothing until its lineage integrates. §30, §32.3 and closure map §5 disclose this, but §0.1 says "§0.3 lists each refinement; there is no other intended difference". The narrowing is sound in direction (it only withholds support), but list it in §0.3 (as R12, or under R9-R11), together with any rule-1 narrowing B1 adopts.

**N3 — Gate-term prose overclaims.** §5.5: "the admitted gate term (`F`, `P` or `T`) is unchanged by a pending or abandoned candidate in either direction". This is false for adverse frame decisions: a frame `REJECT` on a subject the candidate leaves unchanged vetoes admitted `ACCEPT`s at once, while the candidate is pending. §32.3 discloses only the persistence after abandonment. Restrict the sentence to passing decisions and supersessions, and disclose the pending effect.

**N4 — Implementer-obligation discharge is non-latching and unstated as such.** Apart from B1-A:

- every later change of an integrated item's outputs makes that item's `IMPLEMENT`/`AUTHOR` obligation `OPEN` and ready again (§10.4, §7.3 output roles);
- the Manual states no rule for retiring completed items, nor whether such re-dispatch is intended.

State it, and add re-dispatch churn to §32.3. The B1 repair should settle the identity consequence. This finding concerns the liveness consequence.

**N5 — Qualification gaps (DS-001).**

- §31.5 "Revert" does not distinguish a restore under the obligation that started the earlier run.
- §31.6 (F) contradicts the normative `elig` (B1-C).
- No case relieves an admitted veto from a rejected iteration or a partition sibling.
- (G) covers only different lineages.
- No case covers a re-cutover by the same requester, or analyzer re-identification of a D1/D2 revision.

A §31 transcribed from the present expected values can stay green with B1 present. These are design-program omissions, not runtime demands at G1.

**N6 — Stakeholder-level trade-offs (reported as such, not blockers).**

- SD-17's partial reversal (stops need a bounded reproduction).
- SD-24's narrowing (only the decision's author or the owner lifts a qualification).
- The exact-identity cost.
- SD-25's consequences: cross-candidate frame reuse withdrawn; frame `REJECT` persistence; gate-member accumulation.

All are listed in closure map §5. Directions chosen from candidate 13 onward are the author's under item 19. B1's options belong with them.

## 3. Closure audit: workplan §21 and §16.2

**Method.** For every §21 item I located the deciding Manual section myself, using the closure map only to find text faster, and checked the map's citations against the candidate. For items 1-4, 6, 8-12, 14-23 and 25-27 the cited text is unchanged since b46c250, apart from the §1.4 precedence, the §6.3 residual subtraction and the §29.5 audit row. Both b46c250 Reviews found those items resolved. I spot-checked each section during the whole-Manual read and re-read the changed passages in full. **No unresolved item was found among them.**

**Affected by B1 (not substantively resolved at this candidate):**

| §21 item | Clause | Gap |
|---|---|---|
| 5 | "each record kind's declared frame (§6.9)", the prospective-acceptance rule's lineage | What a frame record's integration means is keyed on a lineage that can contain non-integrating transformations (B1-B, B1-C, B1-D(i)) |
| 7 | obligation rules; three-valued discharge; iteration/attempt identity | The run identity rests on an unestablished "each obligation at most once" premise; the reopening of discharged implementer obligations is unstated (B1-A, N4) |
| 13 | cutover | The run a cutover starts has no defined identity (B1-E) |
| 24 | task-partition checks | Which obligation each partition task binds and claims is undefined, and this now determines acting and run identity (B1-D(iii)) |

**§16.2.** Both tables are resolved in §26.4. Every **Deferred** row of the workplan has a final disposition there:

| Deferred row | Resolved by |
|---|---|
| invariant 4 | §26.3 single root |
| invariant 9 | benchmark fields |
| invariant 15 | harness-adapter SPI verbs |
| invariant 17 | capability keys |
| invariant 26 | containment root |
| §5 sub-rules | adopted one by one |
| §6 | composition SPI |
| §7 | `CandidateRef` and `StageResultEnvelope` declined, the rest mapped |
| §9-§11 | function replacement |
| §12 | `[ssds]` configuration |
| §18 | §26.2 fitness checks |

None is unresolved.

**Material decision versus delegated choice.** `[delegated]` marks remain on genuinely D4 choices: diff implementation, checkpoint encoding, parser libraries, mutation tool, limit values, reason-code members. I found no new over-specification. The B1 items are under-specifications an implementer would have to decide architecturally.

## 4. Refinements R1-R11

| # | Assessment |
|---|---|
| R1 | **Sound.** Unchanged since b46c250. `on⁺ ⇒ on⁻ ⇒ link⁻` holds by construction, and the guard keeps `on⁻` a function of the record and `K`. Re-tested in both directions (sections 5 and 6). |
| R2 | Sound. The clamp is unchanged; acting adds no support edge. |
| R3 | Sound. |
| R4 | Sound. |
| R5 | **Sound, and improved.** The b46c250 N6 precedence (innermost ownership before residual and uncovered) is stated in §1.4, and the residual's execution-basis subtraction in §6.3 now subtracts every byte-owning unit. Pairwise tests on the original resolutions leave the surviving regions laminar, so ownership is unique. |
| R6, R7, R8 | Sound, unchanged. |
| R9 | **Reviewed core sound** (a same-kind veto that counts by existence, author/owner relief). **Its SD-25 clause is unsound at lineage granularity**: "a reassessment or adjudication ends it only in the states where that record acts" lets a rejected iteration's or a partition sibling's frame relief act in the admitted state (B1-B). Repair with B1. |
| R10 | **Unsound as concretized.** The run "identified by the event that started it" uses an `ι` that two events can share, so a same-lineage restoration revives D1/D2 validity (B1-A). For cutover and re-identification the run is undefined (B1-E, B1-F). R10's statement of intent is right; its realization is not. |
| R11 | **Aggregation sound** (`gterm` minimum, `unq`, adequacy refusal). **Its SD-25 restatement of eligibility reopened f7419d5 B1 (vii)** (B1-C). |
| (unlisted) | The acting rule is itself a refinement of workplan §6.9. It is sound in withholding direction, but unlisted (N2), and its lineage unit is the B1 cause. |

## 5. Previous findings re-derived

"Closed" means I re-derived that the present text excludes the named trajectory. It is not runtime evidence.

**Depth.**
- In full against the new text: both b46c250 Reviews' blockers and N items, and every f7419d5 B1 sibling.
- For older records, the cited text is unchanged since b46c250 (the diff hunks are listed in section 10). I took the b46c250 same-family dispositions as hypotheses and spot-checked each family's governing mechanism during the whole-Manual read:
  - SD-17/18 classes in §6.5 and §17.5;
  - the effect-keyed write set in §1.2;
  - the domain rule in §13.2;
  - R8 supersession authority;
  - the R9 veto;
  - `ref` locality;
  - exact identity in §1.5;
  - `ext` in §6.5.
- I did not re-read every older record's prose.

### B46C250 — different family (GPT)

| ID | Disposition |
|---|---|
| B1-A (frame supersession lifts admitted veto) | **Closed for a single pending or abandoned candidate**: `superseded_G` and `stands⁻` read only acting records. **Reopens through a rejected earlier iteration or a partition sibling of a lineage that integrates: B1-B** |
| B1-B (frame supersession drops admitted `P`) | Closed for a single candidate (§31.6 (D)); **reopens by the same route (B1-B gate variant)** |
| B1-C (frame identity not computable) | **Closed for computability**: `rid = (s, ι)` is known before issue and stable under unrelated admissions. **Uniqueness fails: B1-A, B1-E** |
| B1-D (unchanged-subject run membership) | **Closed**: frame `rid` equals the admitted `rid`, and a frame record naming it is in the run after integration |
| N1 (evaluation frame of admitted records) | **Closed**: §4.1 and §5.5 evaluate "in the state at hand"; §7.3 says "An admitted-frame record evaluated in `D_n[X]` is evaluated against `M_n(X)`" |
| N2 (accumulating gate members) | Closed as disclosure (§32.3) |
| N3 (aid and wording residue) | **Closed**: closure map item-5 row rewritten; §31.3 names `link⁻`; the maintenance-audit map row corrected |
| N4 (qualification gaps) | **Partly closed**: B1-A/B, run identity (G)/(H), the 5c55d4b B2(D) anchor move and the isolated region case are added. New gaps: N5 |
| N5 (trade-offs, provenance) | Stakeholder matter, carried (N6); Phase B N1 still disclosed |
| N6 (residual/uncovered precedence) | **Closed** (§1.4 precedence, §6.3 subtraction, §31.2 (F)) |

### B46C250 — same family (Claude)

| ID | Disposition |
|---|---|
| B1 (i) restrictive frame supersession | Closed for a single candidate; B1-B route |
| B1 (ii) permissive frame relief | Closed for a single candidate; B1-B route |
| B1 (iii) identity | Computable; not unique (B1-A) |
| B1 (iv) unchanged D1/D2 subject | Closed |
| N1 | Closed |
| N2 | Closed as disclosure |
| N3 | Closed |
| N4 | Partly closed (N5) |
| N5 | Stakeholder matter |

### F7419D5

| ID | Disposition |
|---|---|
| B1 primary, (i), (iii), (v), (vi), qualified variant | Closed (state-relative `superseded_G`, `elig` over acting records, hygiene rule gone) |
| B1 (ii) earlier iterations | Closed for passing decisions on subjects the lineage changes; the iteration relief route is B1-B |
| B1 (iv) identity across integration | Closed for computability (B1-C of b46c250); uniqueness: B1-A |
| **B1 (vii) abandoned iteration** | **Reopened (B1-C)**: the closing phrase "for the obligation that integration produced" was deleted |
| N1-N3, N5 | Closed |
| N4 | Partly closed (N5) |
| N6 | Stakeholder |

### 575DC78, 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC

| Review | IDs | Disposition |
|---|---|---|
| 575DC78 | B1 | Closed (`gterm` minimum unchanged) |
| 575DC78 | N4 | Closed (lineage-valued `ι` restores a frame run value; uniqueness is B1) |
| 575DC78 | N5 | Closed (anchor-move discriminator added) |
| 575DC78 | others | Closed |
| 5C55D4B | B1, B2 | Closed |
| 5C55D4B | N3 | Closed (frame declaration, identity, standing per state) |
| 5C55D4B | others | Closed |
| 27EF339 | B1, B2 | Closed |
| 27EF339 | B3 | Closed for its trajectory; the family recurs as B1 |
| 27EF339 | N2 | Stakeholder |
| 27EF339 | others | Closed |
| 0B6C4FA | B1 | Closed |
| 0B6C4FA | B2 | Closed for its trajectory; family B1 |
| 0B6C4FA | N1 | Stakeholder |
| 0B6C4FA | N2 | **Partly closed** as before: an author may still supersede its own decision while a blocking challenge against the triple is open; that is unchanged and author-accountable |
| 0B6C4FA | others | Closed |
| A18B544 | B1 | Closed |
| A18B544 | B2 | Closed for its trajectory; family B1 |
| A18B544 | N1-N5 | Closed |
| A18B544 | N6 | Superseded |
| E9E6E9F | B1, N1-N5 | Closed or superseded |
| E9E6E9F | B2 | Closed for its trajectory; family B1 |
| E2154AC | B1, N1-N5 | Closed (N2 (b) by the §16.8 state rule) |

### 3540D98 (GPT family)

| ID | Disposition |
|---|---|
| B1 | Closed (exact identity, §1.5) |
| B2 | Closed (complete external-input record, §6.5) |
| B3 | Closed for its qualified-gate trajectory; the gate family recurs as B1-B/C |
| B4 | Closed (equal regions) |
| N1 | Prospective run representation closed for computability; uniqueness open (B1-A, B1-E) |
| N2-N4 | Held as disclosures |

### 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363

| Review | IDs | Disposition |
|---|---|---|
| 798B2B4 | B1-B4, N1-N8 | Closed for their trajectories: predecessor equality replaced; symbolic-link reads recorded. The protected property, no D1/D2 revival on revert, fails by the new route B1-A |
| 71CF9B3 | B1 | Closed |
| 71CF9B3 | B2 | **Closed as text**: the S11 restoration clause is restored as R10. **Violated in realization by B1-A** |
| 71CF9B3 | N1-N8 | Closed |
| 86AB683, 1FFBBF0 | B and N items | Closed (SD-18 class rule in §6.3, §6.5, §17.5 unchanged) |
| 53669A5 | B1-B3, N2-N9 | Closed |
| 53669A5 | N1 | Stakeholder |
| D837363 | B1-B4, N1-N8 | Closed |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

Closed. Unchanged text for:
- `on⁻`'s frozen resolution context;
- the effect-keyed write set and the `AUTHOR`-only domain rule;
- R8;
- R9's veto and the `TASK_RESULT` carrier;
- `ref` locality.

The D1-D3 change-rule items of these records (b595f2c B3, c6da678 B3, cc005db B1) hold for every route except the same-lineage restoration of B1-A.

### Phase B §3 closures and N1-N4 carry-forward

| Closure | Present reconstruction |
|---|---|
| Completeness polarity (Phase B N2), both directions | **Held.** Take an alternate tree differing only outside a recorded narrow basis, with a differing old-content run (2) and a yielding present-content run (4), under a bounding judgment that becomes `P`, blocked, revoked or loss-withheld. (2) and (4) read `link⁻`, an S0 existential over admitted observations that never reads completeness, so the claim stays `P`. Losing the judgment only removes `bound` and narrows (1) and (3). Restrictive direction: a stop is withdrawn only by a newly admitted narrow anchor that links a differing run, which has a cause, is fail-closed, and is disclosed (§32.2). The acting rule does not touch observations (N1) |
| Support cycles fail closed; corrupt prefixes | Held: the §5.6 clamp and §5.7 `INTEGRITY_HALT` are unchanged; `acts`, `superseded_G` and `rid` are S0 facts and add no S2 edge |
| Y1/Y2, X1-X3, candidate-own latch, floor and class | Held (unchanged §6.8) |
| Contrary-run retention, nondeterminism, U1/U2/W1/W2 | Held (unchanged) |
| Absorbed relaxation; adversity vs currency, challenge, loss; salvage; independence; start latch; structure, quarantine, tenure | Held. Dispositions now read acting records: correct for a single candidate, B1-B for earlier iterations |
| Phase B N1 | Disclosed (§32.2, §32.4) |
| Phase B N3 | Held (§31.3 diagnostic-model limits) |
| Phase B N4 | Held (§32.3 reopen triggers) |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | Same obligation re-dispatched after its discharge lapses; it restores an earlier D2 revision | **Fails: B1-A** |
| 2 | Restore by a different `AUTHOR` item, by absorption, or while the later acceptance is revoked | Held: new `ι`, new run |
| 3 | Frame supersession in a single pending, then abandoned, candidate (b46c250 B1-A/B) | Held |
| 4 | Rejected iteration's frame reassessment, then a later iteration of the lineage integrates | **Fails: B1-B** (acceptance, review and disposition variants permissive; gate variant restrictive) |
| 5 | Earlier iteration's gate decision on a never-integrated revision; identical bytes arrive later | **Fails: B1-C** |
| 6 | Partition parts of one item: acting and run identity | **Fails or undefined: B1-D** |
| 7 | Rollback, then re-cutover of the same native revision | **Undefined: B1-E** |
| 8 | Analyzer-set adoption re-identifying a D2 revision, then reversed | `ι` undefined: B1-F |
| 9 | Clean rebase across an unrelated records-only admission | Held: `rid` and obligation identities unchanged |
| 10 | Concurrent absorption changing the frame's subject before integration | Held: frame records stale, revalidation derived, merged revision derives `REVIEW(s, r_m)` |
| 11 | Frame on an unchanged subject; an absorption then changes it before integration | Held: frame `rid` follows the admitted run, and the old frame decision leaves the run |
| 12 | The candidate's own change arrives first by absorption | Held restrictively: new run `(s, entry)`, frame records out of the run |
| 13 | Abandoned candidate's `REJECT` on an unchanged subject | Restrictive, disclosed after abandonment; the pending effect is not disclosed (N3) |
| 14 | Stratification and single-valuedness with `acts`, `superseded_G`, `rid` | Held: all S0, positive in S2; `D_n[X]` equals the post-integration acting set at head `n` |
| 15 | `LEDGER_LOSS` whose lost interval held a lineage's integration | Held: acting is monotone on the retained chain; that lineage's frame records do not act |
| 16 | Discriminating reading recorded in an abandoned frame | Covers outcomes in `D_n`; harmless by construction, but outside the stated rule (N1) |
| 17 | Overtaken integration republished under `REVALIDATE_OVERTAKEN` | Held restrictively: a distinct obligation, a new run |
| 18 | Direct human reassessment while the judgment obligation is answered | Admitted (step 7's refusal binds only bound judgments); used in B1-B |
| 19 | Partition precedence (b46c250 N6): anchor unit moved into a class composite; member surviving an `ABSENT` composite | Held |
| 20 | Phase B N2 polarity, structure, `ignore` and analyzer changes with `K` fixed | Held (guard) |
| 21 | Publication crash windows, fence chains, ABA (§22.3) | Held (unchanged) |
| 22 | Write set, `AUTHOR`-only domain rule, nested composite sentence | Held (unchanged) |

I stopped discovery in B1's family once its common cause was characterized. Further siblings (other lifecycle records, inspector rendering of runs) would be implementation-like. Section 6 is a bounded negative result elsewhere, not a completeness claim.

## 7. Minimum architecture and capability transfer

- **What SD-25 changes.** It adds an S0 acting predicate and a run field on three existing record kinds, and removes the per-consumer prospective clauses. It adds no component, store, record kind or tier. The §30 table remains accurate apart from B1.
- **Capability withdrawn.** SD-25 withdraws one reviewed capability: cross-transformation `record` support from another pending lineage (workplan §6.9). It is disclosed in §30 and §32.3, but unlisted in §0.3 (N2). No governing owner requires that capability. K1 and S4 are preserved, because the change only withholds support.
- **Cost of B1 Option 1.** It would withdraw the later-iteration carry of prospective acceptances (workplan §6.9 rule 1), keeping rebase carry. This is a restrictive change of a reviewed rule and must be surfaced.
- **Architecture 1.6.0 supersession (PC-001).** §26.4 preserves the version-bound Level 0 Core, frozen profiles and the single composition root. `orchestrator/docs/architecture.md` is byte-identical to `fad3ee4` (blob `39e6de7`), and nothing under `source/` or `dist/` changed (section 10).
- **PEM Historical Applicability Set.** PEM was activated: this is replacement of mature machinery under a memory-bound workplan. The PEM file at the candidate is blob `1561797`, schema-valid (section 10).

| Entry | Applicable | Disposition |
|---|---|---|
| PC-001 | yes | Held, as above |
| DS-001 | yes | Applied in N5: §31's expected values can stay green with B1 |
| FF-001 | yes, for genesis publication | Held: §19.9 publishes nothing before validation and quorum |
| SP-001 | no | No source-to-package routing change |
| SP-002 | no | No immutable self-reference construction in this cycle |

I did not re-read the archived §18 inheritance workplans in full. SD-25 touches no inherited capability other than the one noted above.

## 8. Qualification-design adequacy

- **Status.** §31.1 correctly marks every runtime group `UNEXECUTED`. G1 needs only §31.10, and I ran it (section 10).
- **Discrimination.** The real-owner requirement and the negative discriminators are adequate in form. The run-identity and acting-rule cases do not discriminate B1:
  - §31.5's revert case uses a different item;
  - §31.6 (G) uses different lineages;
  - §31.6 (F) asserts a result the rule contradicts.

  Per DS-001, a §31 implemented to the present expected values could be green with B1 present (N5).
- **Executed-evidence claims.** Nothing is claimed as executed beyond §31.10.
- **Diagnostic model.** Optional; I did not run it. It is unchanged and does not model the new clauses.

## 9. Doctrine-realization map and O1

- **Coverage.** The map covers all seven 7.2.1 entrypoints (four roles, three specialists) and the scientific checks, with E0-E3 levels and mechanisms. The b46c250 N3 correction to the maintenance-audit row is made.
- **§29.4 revising D1/D2 row.** Its E0 claim, "it is current only within that run, so a revert or any change of the revision needs a new record, acceptance and gate", is **false for a same-lineage restoration** (B1-A). §29.5's documentation row repeats the claim. Both stand once B1 is repaired.
- **Other rows.** No other row overclaims beyond what the rows' own E2/E3 limits disclose.
- **O1 (§0.5).** Unchanged and adequate:
  - realized record, readers, routine questions and realized-record architecture are stated;
  - product surfaces are marked within the deliverable;
  - **none** is marked beyond it, so nothing awaits `PRODUCT_SCOPE_ACCEPTANCE`.

  Product-scope acceptance remains with the stakeholder (S12). Technical Review accepts nothing.

## 10. What I verified and how; what I could not verify

**Verified.**

- Reviewed exactly `f22b4dc4c5cc56da962bee9eca843fa204af40bc` through a `git archive` snapshot in scratch. Blobs confirmed: Manual `976bece…`, closure map `1247127…`, workplan `91bde23…`.
- Read the whole Manual (2697 lines). Read in the workplan: §2, §6.9, §7.1-§7.4, §7.8, §16.2 and §21.
- Read the stakeholder record's item 20 and SD-22 to SD-25 entries, the closure map changes, and both b46c250 Review records (blockers, N items, re-derivation tables). Read f7419d5 B1 (vi)-(vii).
- Read the governing owners at `aaeaf8b`: the D3 role entrypoint; the architecture, convergence, evidence and workflow owners (sections cited above); the scientific-checks revising duty.
- Diffed the Manual `b46c250..f22b4dc` by hunk and word. The changes are §0.3 R9, R10 and the history paragraph; §1.4 precedence; §4.1; §5.2 acting; §5.3; §5.5; §6.3 residual; §7.3; §7.5; §8.3 steps 2 and 7; §10.2-§10.3; §13.5; §16.8; §19.5; §29.5; §30; §31.2; §31.3; §31.5; §31.6; §32.3.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the candidate snapshot: **4 tests OK**.
- `git diff --check b46c250aefdb78524ac5153097f559a21b512b24 f22b4dc4c5cc56da962bee9eca843fa204af40bc`: clean.
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 f22b4dc4c5cc56da962bee9eca843fa204af40bc`: 49 files, all under `orchestrator/docs` (the Manual), `qualification/ssds80` and `workplans/active`.
- `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4` (empty diff; frozen blob `39e6de7`).
- PEM schema validation of the candidate's `PROJECT-ENGINEERING-MEMORY.md` (blob `1561797`, identical in the checkout): "PEM schema 1 valid: 5 families, 0 notices". It was run in the checkout because the archive lacks Git for route realization.

**Not verified or not established.**

- No production or runtime behavior; none exists at G1.
- The diagnostic model was not run.
- I did not re-read every older Review record's prose (section 5 states the depth).
- I did not re-read the archived §18 workplans in full.
- The B1 trajectories are deductive, from the Manual's own rules. Their premises (discharge lapse, re-dispatch, direct human frame records, partition binding) are each cited, and an implementer could instead adopt a reading I flagged as ambiguous. That ambiguity is itself part of B1.

## 11. Scientific-checks answers

- **Material findings.** None about scientific or numerical meaning. B1 and N1-N6 are D3 findings about software that mediates scientific evidence. B1-A affects how D1/D2 revisions are accepted and gated.
- **Realized results.** I produced, ran and reviewed no realized scientific results. Null envelope: examined the Manual's D3 text, the governing owners and prior Review records. Materially unexamined: any runtime evidence (none exists) and the diagnostic model.
- **Variants.**
  - Repair directions: four, of kind D3 options. The criterion was that a direction must close all six siblings, remove or narrow mechanism, and preserve reviewed contracts. Option 1 is recommended; Options 2-4 were rejected or deferred to the stakeholder as stated.
  - Trajectories: 22, of kind out-of-matrix, chosen as high-information siblings of the newest clauses and of earlier families (section 6).
- **Reliance on accepted D1/D2 authority.** I relied on no accepted D1/D2 authority for a consequential judgment, so no tension search was owed. I quote the scientific-checks revising duty only as the owner B1-A violates.
- **Gaps.** Runtime qualification (G2-G4), and full re-tracing of older records.

## 12. Common-mode note

- **Family.** I am of the Claude family, the same as the Manual's author and as the reviewers of e2154ac, e9e6e9f, a18b544, 0b6c4fa, 27ef339, 5c55d4b, 575dc78, f7419d5 and the same-family b46c250 Review. The 3540d98, different-family b46c250 and Phase B reviewers were of the GPT family.
- **Engagement.** I was engaged as a fresh-context sub-agent launched by the authoring session.
- **Shared dependencies.** Fresh context does not make me independent. I share:
  - the corpus;
  - the inherited workplan framing and its lineage vocabulary;
  - the prior Review records, which I read and which shaped B1-B and B1-C by analogy with b46c250 B1-A/B and f7419d5 B1 (vii);
  - the toolchain;
  - the model family with the author and with most prior reviewers.
- **Provenance of the findings.** B1-A's mechanism (a reopened discharge reusing the lineage's `ι`) and B1-D, B1-E and B1-F were found by reconstruction from the candidate text, not from a prior record. A different-family review of the B1 repair would reduce the shared-framing risk.

## 13. D4 statement

No SSDS 8 D4 is authorized. This Review accepts no architecture, product scope or proposed default. G1 remains open: it needs a repaired Manual candidate, an independent D3 Review with no surviving blocker, and explicit stakeholder acceptance. Shadow implementation additionally needs G2.
