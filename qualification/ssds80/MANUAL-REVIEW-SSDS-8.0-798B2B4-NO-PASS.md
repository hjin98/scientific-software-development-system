# SSDS 8 Architecture Manual — Independent D3 Review, candidate 798b2b4

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout /home/samjin/agent-skills/scientific-software-development-system)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 798b2b4e9b10aedc1161e4a50d5e8f6582014d0c
    SCOPE: the whole proposed Manual as durable D3 owner: (a) §21 and §16.2 closure; (b) fidelity to the
           Phase B-reviewed workplan, including refinements R1-R10; (c) out-of-matrix adequacy; (d) inheritance
           and capability transfer (Architecture 1.6.0, workplan §18, PEM HAS); (e) qualification design;
           (f) doctrine-realization map; (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob 3269a8ca253d14bacf5067cd00cbe517c81baaf5 (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md, blob d65a713aa35a0c1ff03ce908a8b6d12ea7b0a766 (verified)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23;
           Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b97fb8152d2a5742e17fa172e12204756, verified);
           blob at the candidate 91bde236465178f20c7348280e036d2884dfc216 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml, verified)
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml, verified)
    PRIOR REVIEWS (HYPOTHESIS ONLY): MANUAL-REVIEW-SSDS-8.0-71CF9B3-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-86AB683-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-1FFBBF0-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-53669A5-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-D837363-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-CC005DB-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-C6DA678-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-B595F2C-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-6FF4ED1-NO-PASS.md; WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
    REVIEW METHOD: entry through source/roles/software-design/SKILL.md at the public source (expanded entry contract and
           scientific checks read in dist/skills/software-design/SKILL.md); owners read there: architecture-and-design,
           abstraction-and-concretization, convergence-and-cycle-economy ("Active simplification trigger", "Review strategy
           after recurrence"), workflow-and-workplans (D1/D2 revision gates), evidence-evolution-and-dependencies
           (revert/restoration), source/shared/fragments/scientific-checks.md (e=3, e=5); full read of the Manual from a
           git-archive snapshot of the candidate; word diff 71cf9b3..798b2b4 of the Manual, closure map and stakeholder
           record; clause comparison against workplan §2 S11, §6.9 frame rules, §21 and §25; constructed trajectories in
           the permissive and restrictive directions; G1 document checks executed
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session

Governing SSDP version for this Review: 7.2.1. The Manual's refinement table, decision markers, §30 pass and qualification claims, the closure map, commit messages, the handoff's scope text, workplan §0.1/§27 rationale, the diagnostic model's reported results and every prior Review record were treated as hypotheses. Section numbers refer to the Manual at the candidate unless prefixed "workplan". Scratch files were written under `$TMPDIR/ssds80-manual-review-798b2b4/` (resolved to `/tmp/claude-1000/ssds80-manual-review-798b2b4/`), because the sandbox does not permit `/tmp/ssds80-manual-review-798b2b4/`.

## SERIOUS CHALLENGE

**None.** No accepted governing authority was found false, contradictory, ambiguous, inadequate or unrealizable.

- The scientific-checks revising duty (e=5), the workflow owner's D1/D2 revision-gate rule, the evidence owner's restoration and stale-evidence rules, the reviewed workplan's frame isolation and SD-21 are coherent and realizable together.
- SD-21's wording ("within a tenure, the latest acceptance of another revision; at a tenure start, the latest acceptances of every subject that owned the new tenure's bytes") admits the defective literal readings that B1 and B3 exploit, but it is soundly realizable: by acceptances that took effect, and by byte ownership read through identity lineage. The defects are therefore Manual blockers. How the direction is realized is still the stakeholder's to choose (family assessment below).

## Verdict

**NO-PASS.** Four blockers survive.

- **B1, B2 and B3** are in the D1-D3 change rule. This is the ninth successive Review with a finding in that family. Two of the three entered through the repairs of the previous round (the 71cf9b3 N1 repair and the SD-21 consumer list).
- **B4** is a clean local defect in the execution-basis recording. It entered through the 71cf9b3 N6 repair.

The four blockers:

- **B1.** A frame acceptance changes the admitted state. §10.2 defines "accepted" as any admitted passing acceptance record, "whatever its later standing". So a prospective acceptance of an unintegrated, pending or abandoned candidate moves the admitted-state predecessor.
  - In the ordinary `AUTHOR` flow, the accepted D1/D2 subject becomes invalid in the admitted state the moment its candidate's prospective acceptance is admitted.
  - A concurrent candidate is told, and its gate is shown, a predecessor that never governed.
- **B2.** The state condition is not read by every consumer. The `GATE(g)` trigger and §10.4 discharge read currency, not `holds`.
  - After a revert, or after the predecessor moves, the old acceptance and gate decision are current but do not hold. `ACCEPT(s)` is then discharged at once and `GATE(g)` is never derived.
  - Validity stays `F` with no derived route back. This contradicts §10.2's "derived afresh" and §31.5.
- **B3.** The tenure-start predecessor is keyed on positional byte ownership. A rename with a move, a split into new files, and a replacement at a new path give an empty machinery-supplied predecessor, which the reviser cannot override. Under one reading, so does a plain move. §31.5 claims "never empty".
- **B4.** A read through a symbolic link is recorded only at its resolved target. Retargeting a tracked link to an input that was never run leaves the old passing realization current and lets it serve (3). Stale passing evidence is presented as current.

These held:
- The 71cf9b3 B2 validity defect (a revert reviving an earlier D1/D2 acceptance) is closed.
- These 71cf9b3 B1 trajectories are closed: the scope extension, the scope round trip and the same-bytes re-cutover.
- The matching construction rule and guard hold (Phase B N2 re-tested in both directions).
- Stratification and single-valuedness hold.
- Every earlier closure re-checked in §5 holds.

This verdict accepts nothing and authorizes no D4.

## 1. Blockers by earliest owner

### B1 — "Accepted" includes acceptances that never took effect; a frame acceptance moves the admitted-state predecessor (§10.2, §5.5 `ACC`/`holding`, §16.6, §7.4-§7.5; SD-21; entered through the 71cf9b3 N1 repair)

**Mechanism.**
- §10.2: "**Accepted** means that an admitted passing `ACCEPTANCE`, `LEGACY_ACCEPTANCE` or `EXTERNAL_ACCEPTANCE` record names the revision, whatever its later standing: an S0 fact."
- The predecessor: "If some revision of `s` other than `r` has been accepted in `s`'s current tenure, it is the latest such acceptance record."
- §7.5: "An acceptance in frame `X` must name a subject effective in `Σ_n ⊕ Δ_Σ(X)` at its frame `scope_id` and revision; it is a **prospective acceptance**." It is admitted at a ledger position in `s`'s current tenure when `X` changes no structure. Under the definition it is therefore "accepted" in the admitted state too, whether `X` later integrates or not.
- §10.2 derives `ACCEPT(s)` and `REVIEW(s, r)` "in a frame `G`" for a `NATIVE` D1/D2 subject "in its current or a prospective tenure", and §31.5's merged-revision case accepts in the frame. Frame acceptance is the ordinary route for an `AUTHOR` item.
- `holds` requires "`pred_k(s, r)` equals `pred` at `j`'s admission", and `valid(s)` uses only acceptances and gate decisions that hold (§5.5). Every admitted frame acceptance of another revision is thus read by the admitted state's validity.

**Trajectory T1 — the ordinary `AUTHOR` flow (restrictive; every step conforming).**
1. `NATIVE` D2 subject `numerics.method` (`docs/method.md`), tenure `τ`, is accepted at `r0` by `j0` and gate-accepted by `h0`. Its record `R0` names predecessor `P0`. D4 subjects rely on it through `validity` entries.
2. A D2 `AUTHOR` item's candidate `X` yields `r1`. Its record `R1` (envelope predecessor `{j0}`) counts in frame `X`.
   - The review passes. In frame `X`, `ACCEPT(s)` is derived.
   - The owner's prospective `ACCEPTANCE PASS` `j1` on `(s, σ, r1)` is admitted (step 7: `R1` counts in the frame).
3. In the admitted state `cur(s) = r0`, and `j1` is "an admitted passing `ACCEPTANCE`" of another revision in the current tenure.
   - So `pred_n(s, r0) = {j1} ≠ P0`.
   - `R0` stops counting, and `j0` and `h0` stop holding.
   - `valid(numerics.method) = F` in the admitted state. Every `validity` entry on it fails, and D4 work governed by it becomes unready, while `X` is only pending.
4. S3 derives, in the admitted state, `ACCEPT(s)` and `REVIEW(s, r0)` with predecessor `{j1}`. A reviewer is told that `r0` replaced `r1`, a revision that never governed.
5. If `X` is abandoned, `j1` stays accepted "whatever its later standing", and `s` stays invalid at `r0`. Abandonment includes a gate `REJECT` in the frame, a later `NO_PASS`, or a conflict that is never rebased. With B2, no gate obligation is ever derived for it.
6. If a human answers step 4's obligation (`j0'`, re-accepting `r0`) and `X` then integrates, `pred_k(s, r1) = {j0'} ≠ {j0}`. `j1` and the frame gate decision stop holding at the moment of integration.

**Trajectory T2 — concurrent candidates (a wrong predecessor reaches the gate).**
1. As T1 step 1, and a tension `t` is recorded against `kern`, a concretization of `r0`.
2. Two `AUTHOR` items, `X` and `Y`, revise `s` concurrently. That is legal: serialization surfaces are scheduling only (§9.2). `X`'s prospective acceptance `j1` of `r1` is admitted.
3. In frame `Y`, `pred(s, r2) = {j1}`.
   - `Y`'s own record (envelope predecessor `{j0}`) stops counting, and `REVIEW(s, r2)` is derived with predecessor `r1`.
   - An entry naming `r0` "is a `DISCREPANCY` of `slots_filled`, so that record counts for nothing". The revising reviewer therefore cannot record the true predecessor.
4. `X` is abandoned and `Y` integrates. `Y`'s acceptance holds, with `{j1}` both at admission and afterwards.
   - Section 3 of `Y`'s gate core states that `r2` replaced `r1`.
   - The revision that governed until `r2`, `r0` with `t` against its concretization, is never named as predecessor. No gate sees the revision `r0 -> r2`.

**Trajectory T3 — other subjects' later acceptances (ambiguity in the same definition).** This is the §31.5 adopted promotion of `numerics.method` out of the composite `numerics`. `numerics` keeps its tenure (§1.6), and its revision changes whenever `numerics.method` or another of its parts changes. "The latest acceptance record, in any earlier tenure …, of every subject … that owned a byte" has three readings:
- *latest as of `k`*: every later re-acceptance of `numerics` moves `pred(numerics.method, r)` while the subject has one accepted revision in its tenure. Its acceptance then stops holding each time (restrictive churn).
- *ended tenures only*: `numerics`' ongoing tenure contributes nothing, and the predecessor is empty. That contradicts §31.5 ("with predecessor `numerics`' last accepted revision").
- *records before the tenure start*: this gives the intended value, but the text does not say it.

**Violated text.**
- Manual §7.5: "Nothing evaluated in a frame changes the admitted state: in `D_n` a review or prospective acceptance of `X` is admitted but not current". §7.4: "`D_n[X]` is never presented as current state, and nothing in `D_n` reads it." Workplan §6.9 states the same, and workplan §27 rejects "admitting frame records as current in the admitted state: it would let unintegrated work count as governing (P4, S11)". In T1 and T2, unintegrated work changes admitted validity and fixes the governing predecessor.
- Scientific checks e=5: "When revising, renaming, splitting, merging or replacing D1/D2 authority … In the revision's own record and its gate evidence, record the predecessor identity". In T2 the recorded identity is a revision that never governed, and the true one cannot be recorded.
- Workflow owner, D1/D2 revision gates: "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments … Acceptance does not ratify an assessment the gate was not shown." T2's gate is shown assessments against `r1`, not against the authority `r2` replaces.
- §0.4 S11 "Effective governance is admitted, never observed", and SD-21 "within a tenure, the latest acceptance of another revision". An acceptance of a candidate that never integrated is not an acceptance within the tenure in the sense these protect.

**Earliest owner.** Manual §10.2, the predecessor definition (§21 item 7), with §5.5 (item 5) and §16.6 (item 10).

**Minimum repair direction.** Define the predecessor only over acceptances that **took effect in the admitted state**:
- an acceptance admitted in the admitted frame, or a prospective acceptance from its binding integration on (`bind(j)`, §7.6);
- in a frame: the admitted state at the frame's base plus that frame's own lineage, never another transformation's frame records;
- at a tenure start: fixed from the records in effect before that start, so later acceptances of other subjects never move it.

The family options are in the assessment after B3.

**Required discriminator (real owners: Derivation S2/S3, Admission step 7, Dispatcher envelope, Interface gate rendering).**
- T1. Expected: admitted-state `valid(numerics.method)` stays `T` while `X` is pending and after `X` is abandoned; no admitted-state `ACCEPT`, `GATE` or `REVIEW(s, r0)` is derived.
- T2. Expected: `Y`'s brief and section 3 name `r0`'s acceptance, and `Y`'s own record counts.
- T3. Expected: the adopted promotion's predecessor stays `numerics`' acceptance in effect at the tenure start, and later acceptances of `numerics` do not invalidate the promoted subject.
- An implementation that reads every admitted passing acceptance as "accepted" must fail. §31.5 has no pending-frame, abandoned-candidate or concurrent-candidate case, so a green §31.5 coexists with B1 (DS-001).

### B2 — The state condition is not read by the gate trigger or by discharge; after a revert or a moved predecessor the derived route never returns (§10.2 `GATE(g)` row and state-condition bullet, §10.3, §10.4, §11.5 step 3, §31.5; SD-21)

**Mechanism.**
- §10.2 lists "Three consumers [that] read this one condition: Admission …; `ACCEPT(s)` and `GATE(g)` are ready only while one counts; and `valid(s)` uses `j` only while it holds". It concludes that a revert or a moved predecessor leaves "the earlier acceptance and gate decision unable to support validity, and `ACCEPT(s)`, `GATE(g)` and `REVIEW(s, r)` are derived afresh".
- The `GATE(g)` trigger is "a required human gate without a **current** `ACCEPT`".
- §10.4: "`discharged(o)` ⇔ ∃ **current** judgment `j` of `kind(o)` on `subject(o)` … ∧ every human gate of `o` has a **current** authenticated `ACCEPT`". Integration reads the same predicate ("required gates", §11.5 step 3).
- `current(x) = base(x) ∧ ⋀ sat(e)`, and `base` does not read `holds`. An old acceptance `j0` and gate decision `h0` are current again whenever their basis holds again: `content (s, r0, EXACT)`, and `record` on the core's records. For a revert to `r0`, that is exactly the case.

**Trajectory T1 — the 71cf9b3 B2 restore, under this candidate (restrictive; every step conforming).**
1. `r0` is accepted (`j0`) and gate-accepted (`h0`). Tension `t` is recorded. `r2` is accepted (`j2`, record with predecessor `{j0}`). A foreign push restores `r0`'s bytes.
2. `valid(s) = F`, because `j0` and `h0` do not hold (predecessor `{j2}`). This part is repaired.
3. `ACCEPT(s)` (parameter `{j2}`) is derived but immediately **discharged**. §10.4 holds through `j0` and `h0`, which are current. `ACCEPT(s)` is never open, so it is never dispatched.
4. `GATE(g)` is **not derived**: `h0` is a current `ACCEPT`.
5. `REVIEW(s, r0)` is derived because `ACCEPT(s)` was. A `REVIEW` judgment on the triple `(s, σ, r0)` from `r0`'s first revising review is current again too, so the same discharge question arises for it (71cf9b3 N2 asked for the answering rule; §10.4 does not use it).
6. Even if a counting record `R0'` is admitted, no open obligation asks a human for a new acceptance or gate decision. `valid(s)` stays `F` indefinitely, and every dependent stays unready.

**Variants.**
- *Revert through an `AUTHOR` item.* In frame `X`, `h0` is current (`cur(s) = r0` there), so `GATE(g)` is not derived in the frame either. The item integrates with its "required gates" satisfied by `h0` and its obligation discharged. Afterwards `s` is invalid with no gate obligation, and the item's record is never shown to a gate.
  - The 71cf9b3 discriminator "`j0` does not answer or discharge the item's acceptance" fails: `j0` does not answer it, but it discharges it.
- *With B1 T1.* An abandoned candidate leaves the admitted D2 authority invalid with no derived route back.

**Violated text.**
- Manual §10.2's own "derived afresh".
- §31.5, Revert and tenure starts: "`ACCEPT`, `GATE` and `REVIEW(s, r0)` are derived with predecessor `r2`'s acceptance record".
- SD-21 as recorded: "readiness, Admission and validity read that condition". A trigger and a discharge predicate that read a different condition are a second representation of it.
- Workplan §21 item 7 ("obligation rules …, readiness, three-valued discharge") and §25 criterion 4 ("currency, validity, three-valued discharge"). Validity `F` with the acceptance obligation `DISCHARGED` and no gate obligation is not one coherent derivation.
- This is a contradiction an implementer cannot resolve without choosing between the trigger table and the bullet.

**Earliest owner.** Manual §10.2-§10.4 (§21 item 7).

**Minimum repair direction.** Make the condition part of currency rather than a separate filter. For a `NATIVE` D1/D2 subject, express `holds` as the target condition `tgt` of `ACCEPTANCE` and `GATE_DECISION` (an S0/S1 predicate that `base` already reads). Every consumer of `current`, `valid`, the `GATE` trigger, discharge, integration's "required gates" and `REVALIDATE`, then reads one condition. The separate `holding` filters and the predecessor parameters can then be removed.

Alternatively, change the `GATE(g)` trigger to "without a holding `ACCEPT`", and require §10.4 discharge of `ACCEPT`, `GATE` and `REVIEW(s, r)` to come from the judgment that answers the obligation.

**Required discriminator (real owners: Derivation S3 obligations and discharge, Dispatcher, Admission integration).**
- T1. Expected: `GATE(g)` is derived with predecessor `{j2}`; `ACCEPT(s)` is open, and becomes ready once a counting record exists; `REVIEW(s, r0)` is open until a counting record answers it.
- The `AUTHOR` variant. Expected: the integration is refused until a holding gate decision on `r0` exists.
- An implementation that triggers or discharges on `current` must fail.

### B3 — The tenure-start predecessor is keyed on positional byte ownership; moves, renames with moves, splits and replacements at new paths get an empty predecessor the reviser cannot override (§10.2, §16.6, §31.5; residual of 71cf9b3 B1)

**Mechanism.**
- At a tenure start, the predecessor is "the latest acceptance record … of every subject (`s`'s own earlier tenures included) that owned a byte of the regions `s` covers at its tenure's start, … it is empty only when no such record exists".
- Regions are resolved scope terms in a tree (§1.3-§1.4). The Manual defines no byte identity across paths.
- The rule ignores the Manual's own lineage facts. §1.11 resolves "former names or paths" by "`renamed_from` lineage" and Git rename history, and "recorded predecessors" by "`SUPERSEDES`/`REPLACES` relations and refinement/promotion history".
- The predecessor is machinery-supplied, and "an entry naming another is a `DISCREPANCY` … so that record counts for nothing". The reviser therefore cannot record a predecessor the class rule misses.

**Trajectory T1 — a declared rename with a move (permissive; every step conforming).**
1. D2 subject `numerics.method` (`docs/method.md`) is accepted at `r0` with its gate. Tension `t` is recorded against its concretization.
2. A D2 `AUTHOR` item removes `numerics.method` and declares `numerics.scheme` with `renamed_from = ["numerics.method"]` and scope `[{ path = "docs/scheme.md" }]`. It moves the file and edits it.
3. In the frame, `numerics.scheme` starts a prospective tenure over `docs/scheme.md`. No subject ever owned a byte at that path, and `numerics.scheme` has no earlier tenure. So `pred = ∅`.
4. The revising review is told there is no predecessor. An entry naming `numerics.method`'s acceptance is a `DISCREPANCY`. Section 3 of the gate core renders no predecessor for a renamed, accepted D2 authority.

**Variants.**
- A split of `docs/numerics.md` into two new files under two new D2 subjects: both get `∅`.
- A replacement at a new path: `∅`.
- A move of the same subject's file: `∅` if "(`s`'s own earlier tenures included)" is restricted by "that owned a byte of the regions …", and non-empty if it is read as unconditional. The text does not say which.

**Violated text.**
- e=5, as quoted in B1: "renaming, splitting, merging or replacing … record the predecessor identity".
- The workflow owner's D1/D2 revision-gate rule.
- Manual §31.5: "A move of a D2 document's file, a kind or domain change, and a replacement without `renamed_from` give the new tenure a predecessor naming the prior owner's last acceptance, never empty." This contradicts §10.2 for moves and new-path replacements.
- §10.2 lists "split, merge, rename, replacement" among the tenure starts the rule covers.
- §29.4 claims E0 "with the machinery-supplied current predecessor".

**Earliest owner.** Manual §10.2 (§21 items 7 and 10).

**Minimum repair direction.**
- Include in the tenure-start class: `s`'s own earlier tenures, unconditionally; the transitive `renamed_from` lineage; and the subjects that a `REPLACES`/`SUPERSEDES` relation of `s` names.
- Fail closed for a D1/D2 tenure start whose class is empty in an admission that removed, re-scoped or moved D1/D2 authority: require a declared lineage, or an explicit human record that there is no predecessor.
- Align §31.5 with the result.

**Required discriminator.**
- T1. Expected: the predecessor names `numerics.method`'s acceptance.
- The split variant. Expected: both new subjects name the old subject's acceptance.
- The same-subject move. Expected: non-empty.
- An implementation that resolves tenure-start ownership by path alone must fail. §31.5's "move" sentence has no trajectory that discriminates path from lineage (DS-001).

### Family-level assessment for B1-B3 (convergence owner, "Active simplification trigger"; "Review strategy after recurrence")

**Recurrence.** D1-D3 change-rule findings by Review:
- `b595f2c` B3; `c6da678` B3; `cc005db` B1; `d837363` B3-B4; `53669a5` B2; `1ffbbf0` B2; `86ab683` B1; `71cf9b3` B1-B2;
- this Review adds B1-B3.

**The pattern.** Each repair attached the revising duty and, since SD-20/SD-21, validity itself, to a mechanically computed predecessor that is compared by equality. Each Review found a set the computation reads wrongly:
- producing admissions;
- content identity;
- a route list;
- now every admitted acceptance, including unintegrated ones (B1), and positional ownership (B3).

SD-21 also left two consumers outside the condition (B2).

**Origin of the new defects.** Two of the three entered through the previous Review's own suggestions:
- B1 through "define 'accepted' by admitted records" (71cf9b3 N1);
- B2 through option (a)'s consumer list ("readiness and validity then read one condition").

This is common-mode evidence.

**Classification.** The owner's trigger applies: "repeated patches around the same mechanism, patch-on-patch repair, … family closure that does not reduce the failure surface". The equality condition now couples admitted validity to every acceptance anywhere: in frames, of other subjects, and across positional ownership. The surface has grown. This is a **non-local recurrence**, and another listed exception should not be added. The governing semantics are held fixed: e=5, the workflow gate rule, the evidence restoration rule, and the stakeholder's requirement that reverts of D1/D2 authority need a revising review.

**Options for the stakeholder** (Phase C handoff §5 boundary):

**(a) Local repairs inside SD-21.**
- B1: define the predecessor over effective acceptances.
- B2: carry the condition in `tgt`.
- B3: add declared lineage.
- Keeps the chosen equality. Adds definitions. Risk: recurrence on the next unread set.

**(b) Subtractive: a revision-run key, with the predecessor used for display only.**
- For a `NATIVE` D1/D2 subject, an acceptance or gate decision is current only if it was admitted, or bound by integration, at or after the latest admitted position at which `cur(s)` took its current value. That is an S0 target condition read by `base`, so every consumer reads it.
- Admission and readiness still require a revision-assessment record for exactly `(s, r)`.
- The predecessor becomes a machinery-computed display: effective history plus declared lineage, which the reviser may extend and the gate core shows. It is no longer an equality condition for counting or validity.
- Removes:
  - the predecessor equality in `counts` and `holds`;
  - the predecessor obligation parameters;
  - the `holding` filters;
  - frame coupling, by construction.
- Reverts still need a new review, acceptance and gate.
- Changes SD-20/SD-21's chosen equality, so it needs the stakeholder.

**(c) Accept as residuals.**
- B1 and B2 are restrictive and B3 is permissive for e=5. This relaxes e=5 for renames and splits across paths, and needs explicit stakeholder acceptance.
- §29.4, §29.5, §31.5 and the closure-map bullet must then be corrected.

**(d) A different-family Review before choosing.**
- All ten Manual Reviews have been same-family, and the last round's same-family suggestions introduced two of these blockers.
- This reviewer's lean, not a decision: (d) together with (b), because (b) removes the mechanism on which the last six findings occurred.

### B4 — A read through a symbolic link is recorded only at its resolved target; retargeting the link leaves the old passing realization current (§6.3 read entries, §17.4, §4.1 `execution`, §6.6 (3); R1 recording; entered through the 71cf9b3 N6 repair)

**Mechanism.**
- §6.3: "a read through a symbolic link is recorded at its resolved target, as a read entry when the target is a file of the tree and as an external read otherwise". The link itself is a tracked tree entry whose content is its target string. It is recorded nowhere unless a unit or widened entry happens to cover it.
- It is not covered in the cases below:
  - a tracked but ignored link (widened entries are "over the governed files");
  - a link outside the declared EXEC closure when the closure is bounded, and observed reads are the safety net (§6.3: the whole-tree widening applies only where "the runner's observed reads are not complete").
- §4.1 `execution`: "every read and widened entry re-resolves to its recorded content identity". §17.4: "A realization supports a claim at revision `c` only while its recorded execution basis is satisfied".

**Trajectory (permissive; every step conforming, every judgment honest).**
1. Specification `S` (declarative oracle) declares `EXECUTION_DEPENDS_ON kern`. Current `COMPLETENESS(EXEC)` holds for `{S}` and `{kern}`. The runner class observes every read.
2. The solver opens `data/current`, a tracked symbolic link to `data/mesh_v1.dat`. `data/` is in `ignore`.
3. Realization `q` passes. Its basis holds unit entries for `S` and `kern`, and the read entry `({ path = "data/mesh_v1.dat" }, cid)`.
4. An admitted change repoints `data/current` to a new `data/mesh_v2.dat`, on which the solver fails. No unit entry, widened entry or read entry of `q` changes.
5. `q`'s `execution` entry stays satisfied, so `q` stays current passing evidence for the claim. `REALIZE` is not derived and nothing reruns. The claim is valid on a run that read an input the current tree no longer reads.
6. Failure variant: an earlier failure `a⁻` whose recorded target was later removed becomes stale in the new content through `q` under (3), with (4) vacuous. The new mesh was never run.

**Violated text.**
- Evidence owner: "A stale passing observation is not admissible confirmation."
- Manual §17.4: "Stale passing evidence never discharges."
- R1's stated property: "one representation serves every consumer".
- §6.3's own boundary: only "regions the closure did not reach" may be unrecorded. The link is content the execution read.

**Earliest owner.** Manual §6.3 read entries (§21 items 4 and 11).

**Family assessment.** This is a **clean local defect** at the recording boundary, not a recurrence of the construction rule or the guard. Both stay sound, and `on⁺ ⇒ on⁻` holds. The 71cf9b3 Review noted that recording the link path alone loses the target's content. The repair chose the target alone, which loses the link. A correct rule needs both, and no new mechanism.

**Minimum repair direction.** Record a read through links as a read entry for every link the resolution traversed, `({ path = link }, cid over the link entry)`, in addition to the resolved target. A target outside the tree stays an external read. Add the case to §31.3.

**Required discriminator (real owners: Dispatcher runner recording, Derivation `sat(execution)` and `stale`).**
- The trajectory. Expected: after the repoint, `q` is not current, `REALIZE` is derived, and `q` cannot serve (3).
- Contrast: changing an unrelated ignored file changes nothing.

## 2. Non-blocking findings

- **N1 — R10/S11 scope does not match §5.5 (§0.4 S11, §0.3 R10, §5.5, §1.1).**
  - S11 now says "within one tenure only a D3 or D4 subject's acceptance is reused by content identity". §5.5 restricts only `NATIVE` D1/D2 subjects. Legacy and external D1/D2 imports, and the subjects of other kinds (`EVIDENCE_SPEC`, `GENERATED`, `PLAN`, `POLICY`), are still reused.
  - "A D1/D2 subject" is not defined as kind or domain. `EVIDENCE_SPEC` takes "the domain of the claims it `EVIDENCES`", and `GENERATED` "the domain of its generator". So it is unclear whether every revision of an evidence specification for a D2 claim, or every regeneration of D2-domain content, needs a revising review.
  - Say "`NATIVE` subject of kind D1 or D2" in both places.
- **N2 — A risk override is lost through `holds` (§10.2 `counts`, §5.5).**
  - A record whose `status1` is `PROVISIONAL` (an open, overridden blocking challenge) counts, and `holds` is two-valued. Where no gate is required for the subject, its acceptance is then `T`, not `P`, against S2 ("a risk override leaves dependents visibly provisional").
  - Where a gate is required, the gate's `record` entry on the core propagates `P`.
  - Make `holds` take `P` from `status1`.
- **N3 — The envelope predecessor is under-specified (§12.2, §10.2, §13.5).**
  - `predecessor` is one field, but an `AUTHOR` task may revise several D1/D2 subjects, "one entry per subject".
  - `pred_k(s, r)` depends on `r`, which the Dispatcher does not know at issue. A candidate yielding the latest accepted value gets another predecessor, which fails closed.
  - State a per-subject map, computed for "any `r` other than the latest accepted value", with the frame record re-derived otherwise.
- **N4 — Cutover route, residue of 71cf9b3 N4 (§10.2, §19.5).**
  - §19.5 condition 3 says `REVIEW(s, r)` "is derived for that prospective tenure" for every cutover. §10.2 derives it only where "an accepted `MIGRATE` item proposes" the cutover. A cutover by a human's direct `MODE_TRANSITION` has no route to its record (restrictive).
  - No item field identifies which subject and native revision a `MIGRATE` item proposes to cut over.
- **N5 — §1.9 overclaims (residue of 71cf9b3 N7).**
  - "So no unit is declared over nothing" is false for `prefix` terms, which "are exempt": a misspelled prefix declares a unit over nothing.
  - No S3 finding is raised when a declared term later resolves to `ABSENT`.
- **N6 — Name collision.** `holds` (§10.2, used in §5.5) and `holds(a, x)` (§23.7) are different predicates. Rename one.
- **N7 — Qualification coverage.** §31.5 has no case for B1 (pending, abandoned or concurrent frame acceptances; a parent re-accepted after a promotion), B2 (gate re-derivation and discharge after a revert), or B3 (rename with a move, a split into new files). §31.3 has no symbolic-link case (71cf9b3 N6 asked for one; B4).
- **N8 — Closure map (aid only).**
  - Items 5, 7, 10 and 27 rely on text affected by B1-B3. Items 4 and 11 rely on B4's text.
  - The stakeholder bullet "A revert of D1/D2 authority to an earlier accepted revision therefore needs a new revising review, acceptance and gate" is not realized by the derivation (B2).
  - The stakeholder record's SD-21 row correctly says "(pending)".

## 3. Closure audit (§21 items and §16.2 rows)

The closure map was used only to locate text, and its annotations were checked against the Manual.

**Not substantively resolved:**
- item 7: the obligation rules (B1, B2), predecessor definition (B1, B3), and readiness and discharge coherence (B2);
- item 5: `ACC` filtered by `holds`, which reads unintegrated frame acceptances (B1). The rest of item 5 is resolved.
- item 10: the gate template meeting Channel C. Section 3 can render a predecessor that never governed (B1 T2), or none for a renamed or split authority (B3).
- items 4 and 11: the mechanical computation of executed content omits traversed links (B4). The rest of both items is resolved.
- item 27: the §29.4 revising row claims E0 for a "machinery-supplied current predecessor" and "a revert … needs a new record and a new acceptance". The predecessor can be wrong or empty (B1, B3), and the gate is not re-derived (B2). The §29.5 documentation row ("needs a counting revision-assessment record before acceptance and for validity") relies on the same text.

**Resolved with non-blocking defects:** item 1 (N5); item 13 (N4; the re-cutover predecessor is correct under the class rule); item 3 (N1).

**Resolved:** items 2, 6, 8, 9, 12 and 14-26. Each decision was located, and each is a decision rather than a route.
- Delegated D4 space is bounded: anchor file-type table, diff implementation, parser libraries, mutation tool, index and journal engines, limit values, witness kinds.
- Item 14's write-ahead publication-attempt record is resolved by its removal (R4, §22.3).

**§16.2:** §26.4 is untouched by the 71cf9b3..798b2b4 diff and was re-read in full. Every row of both workplan tables, including every Deferred row and 1.6.0 §4 and §14, has a final disposition there. None was found unresolved.

## 4. Refinements R1-R10

| # | Assessment |
|---|---|
| R1 | **Sound in construction, with a recording defect.** The guard, the construction rule and `on⁺ ⇒ on⁻` are unchanged, and re-derived. The seed repair ("a seed the runner supplied") narrows the fail-closed clause to what a runner can know, and its residual is disclosed in §6.10 and §32.2; it is sound. The symbolic-link repair is unsound (B4). |
| R2-R7 | **Sound.** Unchanged since 71cf9b3 and re-read. |
| R8 | **Sound.** Unchanged. A `TASK_RESULT` cannot be superseded, so a record's standing correctly reads only `status1` and `cont`. |
| R9 | **Sound.** Unchanged. The veto reads only S0/S1 facts. B2 concerns non-holding judgments, not vetoed ones. |
| R10 | **Sound as a scope statement, with defects downstream.** Across tenures nothing revives. Within a tenure, D3/D4 reuse by content identity is the reviewed early cutoff (workplan §6.6 `ACC`), and the stakeholder's SD-21 cost statement concerns only D1/D2 reverts. R10 narrows the verbatim reviewed clause ("restoring old bytes … restores no validity") for D3/D4 within a tenure. It is listed, so it is surfaced for the stakeholder's acceptance at G1. Its D1/D2 half relies on `holds`, which B1-B3 defeat, and its wording mismatches §5.5 (N1). |

SD-21 is a decision inside §21 items 5, 7 and 10 rather than a refinement. Its realization carries B1-B3.

## 5. Previous findings, Phase B closures and N1-N4

**Method.**
- The 71cf9b3 findings were re-derived against the candidate text.
- For earlier Reviews, each record's finding list and the 71cf9b3 record's re-verification were taken as hypotheses. Their anchors were re-checked in the candidate.
- The 71cf9b3..798b2b4 diff was checked for whether it touches their mechanism. It touches §0.3-§0.4, §1.9, §5.5, §6.3 (seeds, links), §10.2-§10.3, §12.2, §16.6, §17.5, §19.5, §29.4-§29.5, §30 and §31.5.

**71cf9b3.**
- **B1** is partly closed. These are closed: the scope extension, the kind change, a replacement over the same regions, the scope round trip (the earlier tenure's acceptance is in the class), and the same-bytes re-cutover (the predecessor includes the legacy-interval import or the first native acceptance). §31.5 and §10.2 now agree on the re-cutover. The "renames the file and updates the term" variant stays open (B3).
- **B2** is partly closed. The validity defect is closed: `valid` reads `holds`, and the presence variant stays `F`. S11's restoration clause is restored and listed (R10). The derived route back is not closed (B2 here), and the 71cf9b3 `AUTHOR`-variant discriminator fails.
- **N1** is closed for the ABA case (the predecessor names records). Its repair introduced B1.
- **N2** is closed for answering ("only by a record that counts"; the predecessor parameter). Discharge does not use answering (B2).
- **N3** is closed: the envelope field, the `DISCREPANCY` rule, the frame named, "counts" in §16.6 and §31.5, and the §30 accounting.
- **N4** is partly closed: the `MIGRATE` trigger is in §10.2. Residue: N4 here.
- **N5** is closed.
- **N6** is closed in form, but its chosen recording introduced B4, and no §31.3 case was added.
- **N7** is mostly closed. Residue: N5 here.
- **N8** is superseded by N8 here.

**86ab683.**
- **B1** is closed for T1, for the revoked and pre-loss variants, and for T2 (same-bytes re-cutover, via the class rule). The family remains open through B1-B3 here.
- **N1** is partly closed. Residue: N4 here.
- **N2** is closed, and its wording residue is now closed too.
- **N3-N6** are closed.
- **N7** is superseded.

**1ffbbf0.**
- **B1** is closed (SD-18). The seed text now reads "a seed the runner supplied", and the §31.3 free-seed case is consistent with it.
- **B2** is closed for the routes it named. The family remains open.
- **N1** is closed.
- **N2** is closed by removal.
- **N3** is closed in form. Residue: N3 here.
- **N4-N6** are closed.
- **N7** is superseded.

**53669a5.**
- **B1** and **B3** are closed.
- **B2** is closed for readiness and order. The family remains open.
- **N1**, **N3**, **N4**, **N7** and **N8** are closed.
- **N2** and **N9** are superseded.
- **N5** and **N6** are closed.

**d837363.**
- **B1**, **B2** and **B4** are closed (§6.3, §6.5 and §1.2 are unchanged in mechanism).
- **B3** is closed for the human, absorption and adoption routes.
- **N1-N7** are closed.
- **N8** is superseded.

**cc005db.** **B1-B3** and **N1-N8** are closed. The diff touches neither the write set, the resolution context nor the product-scope veto.

**c6da678.** **B1-B3** and **N1-N12** are closed. These anchors were re-checked:
- `stands⁻` requires `¬superseded(d)`;
- `same` for `COMPLETENESS` compares member revisions;
- `REFUSED` is in R9;
- the residual-part `cid` is defined in §6.3;
- `prefix = ""` is stated in §1.8;
- ref locality is in §13.2;
- the agent-reassessment disclosure is in §5.5.

**b595f2c.** **B1-B4** and **N1-N8** are closed. These anchors were re-checked:
- §3.4 has the machinery `COMPLETENESS` producer;
- §13.3 reads "whatever its kind";
- §13.2's `AUTHOR` scope lists unit kinds;
- §14.5 records host-dependent analyzer output.

**6ff4ed1.** **B1-B4** and **N1-N12** are closed. These anchors were re-checked:
- `qualification` is in the `GATE_DECISION` schema;
- §8.3 step 5 reads "gains no new … and no existing one grows";
- §26.4 has rows for 1.6.0 §4 and §14;
- export is listed in §0.5;
- §29.3 has the common-mode and priority rows.

**Phase B §3 closures.** §5.3-§6.10 restate workplan §6.6 and change it only in the restrictive direction, except for B4's recording edge.
- Nondeterministic old-content observations still defeat (2), across recorded free attributes and runner-supplied seeds.
- Executed content still includes observed reads, except for traversed links (B4).
- The promotion, tenure and restoration closures hold across tenures.

**Phase B N2 re-test.** The bounding completeness judgment was taken through `P`, blocked, revoked, superseded, loss-withheld, and non-current by a membership change. In each case:
- a differing old-content run on an alternate tree that differs only outside the recorded regions (including in another span of a recorded file) stays in (2);
- a yielding present-content run stays in (4).

Both hold because `on⁻` is unchanged and reads no completeness. In the permissive direction, only the narrow-basis serving of (1) and (3) is lost. The support-cycle clamp (R2) and the corrupt-prefix halt (R3) are unchanged and fail closed before any current assertion.

**Phase B N1, N3, N4.**
- N1 is open and disclosed (§32.2, §32.4).
- N3's limits are carried in §31.3.
- N4's costs are in §32.3.

**Both directions.**
- Permissive:
  - B1 T2 (a gate shown a never-governing predecessor);
  - B3 (empty predecessors for renamed, split or moved authority);
  - B4 (stale passing evidence after a link retarget);
  - N2 (a risk override lost).
- Restrictive:
  - B1 T1 and T3 (admitted validity lost to frame acceptances or a parent's re-acceptance);
  - B2 (no derived route after a revert);
  - N3 (an unknown `r` at issue);
  - N4 (a cutover without a `MIGRATE` item).
- Repairs of the previous round's non-blocking findings:
  - N1 introduced B1;
  - N6 introduced B4;
  - N2, N3, N5 and N7 hold;
  - N4 holds with residue.

## 6. Out-of-matrix trajectories attempted

**Broke the candidate:**
- B1:
  - an ordinary `AUTHOR` revision with a frame acceptance;
  - an abandoned candidate;
  - concurrent candidates;
  - a parent re-accepted after an adopted promotion.
- B2:
  - a foreign-push restore;
  - an `AUTHOR`-item revert;
  - B1 T1 followed by abandonment.
- B3:
  - a rename with `renamed_from` and a move;
  - a split into new files;
  - a replacement at a new path;
  - a same-subject move (under one reading).
- B4: a retarget of an ignored tracked link; an out-of-closure link under complete read observation.
- N2: an overridden blocking challenge on a revision-assessment record of a subject without a required gate.

**Held:**
- **SD-21 core:**
  - a revert to an accepted revision makes `valid` `F`;
  - a revoked or blocked record stops holding;
  - a pre-loss record is withheld, and one held by an attestation counts;
  - a forged entry predecessor is refused;
  - re-acceptance of an unchanged revision reuses its record;
  - a value that returns by re-acceptance is a new predecessor (no ABA);
  - the scope round trip and the same-bytes re-cutover;
  - a kind change (the subject's earlier tenure is in the class);
  - a carve-out from a legacy subject;
  - re-identification under a system-version adoption (each revision needs a new record);
  - D3/D4 in-tenure reuse is unaffected.
- **Derivation:**
  - `holds` reads acceptance records, positions, tenures, ownership history, and the S1 facts `status1` and `cont`;
  - it is a constant in S2, so S2 stays monotone with one least fixed point under the §5.6 clamp;
  - no new support-graph edge.
- **Matching family:**
  - Phase B N2 as above;
  - the construction rule over runner-supplied and fixed seeds;
  - a declared-set change after the by-value repair (fail closed);
  - an unobserving class;
  - a link to a file outside the tree (an external read);
  - the revert of a link to a still-present target (fail closed);
  - a Git submodule read (pinnable);
  - an LFS pointer.
- **§1.9 repair:**
  - a misspelled `path` is refused;
  - an empty `__init__.py` is accepted;
  - a realignment to `Σ`'s value after a foreign deletion is accepted;
  - analyzer completeness over an `ABSENT` term is refused.
- **Publication, currentness, gates and floors** (§22-§23, §10.5, §15.4 and §16.6 re-read):
  - two processes sharing one host key;
  - a crash after a successful compare-and-swap;
  - a paused publisher against a landed fence;
  - a risk override never covers `GATE`;
  - an unqualified `ACCEPT` is refused while disputed evidence is listed;
  - floor items cannot be reclassified;
  - fail-closed independence on manual routes;
  - `AUTH_VERSION`.
- **Partition and scope identity:**
  - static sibling nesting is rejected;
  - crossed anchors resolve to `ABSENT`;
  - byte-preserving refinement keeps `scope_id`, `rev` and tenure.

## 7. Minimum architecture and capability transfer

**Changes since 71cf9b3.**
- No component, tier or record kind is added.
- SD-21 adds the `holds` filter, the predecessor obligation parameters and the class rule. §30 accounts for them.
- B2's repair direction (the condition in `tgt`) and option (b) would each remove mechanism.
- §30's "No new primitive, component, persistent surface or record tier" remains true.

**Capability transfer.**
- PC-001 (`AUTHORITY_BOUND`) was independently resolved at the public source (protocol-versioning: older supported profiles stay frozen and independently testable) and is preserved:
  - Core imports nothing from SSDS (§26.2);
  - §31.8 tests Core without SSDS;
  - the 1.6.0 file, `source/` and `dist/` are byte-unchanged.
- The 1.6.0 transfer in §26.4 is complete.
- These 7.2.1 capabilities are not fully transferred:
  - e=5, predecessor identity for renaming, splitting and replacing (B3) and for concurrent revisions (B1);
  - the evidence owner's stale-passing-evidence rule (B4).

**PEM basis.**
- PEM is activated: replacement of mature machinery (the 1.6.0 supersession) and a suspected recurrence.
- `origin/main` is `af0455753e20ee54a969c844872e29e270007211`. The PEM blob `1561797125622f355f84eb27319f87e8fa4227d9` is identical there and at the candidate.
- `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md` reports "PEM schema 1 valid: 5 families, 0 notices".
- HAS dispositions:
  - PC-001: applicable and binding;
  - DS-001: applicable as evidence only; it bears on §8 and N7;
  - FF-001: applicable as evidence only (§19.9 genesis procedure present);
  - SP-001 and SP-002: not material to this candidate's decisions.

## 8. Qualification design

§31 binds claims to real owners and marks every runtime group UNEXECUTED; nothing beyond §31.10 is claimed as executed.

**Adequate for what they target:**
- the §31.5 revert-to-accepted case, for validity;
- the scope and re-cutover predecessor cases;
- the §31.3 SD-17/SD-18 cases.

**Green fixtures can coexist with these defects (DS-001):**
- B1: no pending, abandoned or concurrent frame acceptance case;
- B2: §31.5 asserts that `GATE` is derived, but no case checks the trigger or discharge independently of readiness;
- B3: the "move" sentence has no trajectory distinguishing path from lineage, and there is no rename-with-move or split case;
- B4: no link case.

The discriminators in §1 are required. The §14.7 `HARD` qualification design is adequate as design, with proposed-default values. The diagnostic model was not run: its model file is unchanged since Phase B, and it models no revision gates, predecessors, runner classes, seeds or links.

## 9. Doctrine-realization map and O1

The E0/E1 claims are tied to existing mechanisms, with two exceptions:
- §29.4's revising row claims **E0** for "the machinery-supplied current predecessor … however the revision was produced, and it supports validity only while it holds, so a revert or a moved predecessor needs a new record and a new acceptance". The predecessor can be one that never governed (B1) or empty (B3), and the derived workflow never re-asks the gate (B2).
- §29.5's documentation row relies on the same text.

The enumeration is complete with its catch-all row, and the disclosed-E3 list (§29.6) is appropriately conservative.

O1 (§0.5) is unchanged: realized record, readers, routine questions, realized-record architecture and marked surfaces.
- "Beyond the requested deliverable: None" is consistent with the stakeholder record.
- B1 bears on the routine question "What governs this subject, at which revision?": an admitted D1/D2 subject reads as invalid because of a pending candidate.
- B4 bears on "Is this result current against its basis, and if not, what moved?": a retargeted input is not shown as having moved.
- Technical Review accepts no marked item, product scope or default value.

## 10. What was verified and how; what was not

**Executed** against a `git archive` snapshot of the candidate under `$TMPDIR/ssds80-manual-review-798b2b4/`, and against the repository:
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` (in the snapshot): 4 tests, OK.
- `git diff --check 71cf9b3ac72a23a33c6b7038e6696ebb6f27190f 798b2b4e9b10aedc1161e4a50d5e8f6582014d0c`: clean (exit 0).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 798b2b4e9b10aedc1161e4a50d5e8f6582014d0c`: 25 files, 7295 insertions, 1 deletion, all within the expected set:
  - the Manual and the closure map;
  - nine Manual review handoffs and nine NO-PASS records;
  - the Phase C and Phase C continuation handoffs;
  - the session handoff;
  - the stakeholder record;
  - two index lines.

  The 71cf9b3..798b2b4 diff touches the Manual, the closure map, the 71cf9b3 handoff and record, and the stakeholder record (item 16, SD-21).
- `orchestrator/docs/architecture.md` (blob `39e6de7…`), `source/` (tree `fac2238…`) and `dist/` (tree `6bf729e…`) are identical at `fad3ee4…` and at the candidate (`git diff --quiet`).
- All header blobs match.
- PEM was validated as in §7.

**Read** at the public source: the owners listed in the header, with the exact text quoted in §1.

**Read in full:** the Manual at the candidate; the 71cf9b3 Review record.

**Read in part:**
- the word diff of the Manual and stakeholder record;
- the closure-map diff;
- workplan §2 S11, §6.9 frame lines, §21, §25 and the §27 rejected alternative;
- the Phase C handoff §5;
- the finding lists of every earlier Manual Review.

**Not verified:**
- any runtime behavior (none exists); the trajectories are deductions from the specified contracts;
- the diagnostic model (not run);
- empirical frequencies of concurrent D1/D2 candidates, renames across paths, and linked inputs;
- the full text of the Manual Reviews before 71cf9b3 beyond their finding lists;
- workplan §18 and §27 beyond targeted reads;
- the D1, D2, D4 and specialist entrypoint texts beyond the software-design entrypoint and the scientific-checks fragment;
- the testing, storage, concurrency, security and inspectability owners, which were not loaded because no finding turned on them.

## 11. Scientific-checks answers

Scientific checks apply: this Review reviews D3 authority for software that mediates scientific evidence.

1. **Material findings.** B1-B4 and N1-N8 above. No agents were launched. The tools run (git, the unit test, the PEM validator) produced no further findings. No material scientific finding about any project's science was made.
2. **Realized results.** This Review produced, ran and reviewed no realized scientific results, including through the tools it ran, and it prepared no gate evidence. Its output is D3 review evidence toward G1.
   - The unit test, `git diff --check` and the PEM validator are structural software checks, not realized results. No null envelope is owed.
   - Review coverage and its limits are stated in §10. The materiality basis for this Review is the handoff's blocker definition and the kernel's materiality test.
3. **Variants.** No analysis, pipeline, preprocessing, model or parameter variant was evaluated or selected (count 0).
   - Constructed trajectories are review hypotheses, not variants.
   - Seven clauses were compared under alternative readings, as interpretation, with textual coherence against the rest of the Manual and the governing owners as the criterion:
     - "accepted" (any admitted record, or one that took effect): gave B1;
     - "latest … in any earlier tenure" (as of `k`, ended tenures only, or before the tenure start): gave B1 T3;
     - the parenthetical "(`s`'s own earlier tenures included)" (restrictive or unconditional): gave B3's move variant;
     - "current `ACCEPT`" in the `GATE` trigger against "holds": gave B2;
     - §10.4 discharge (formula, or answering judgment): gave B2;
     - what a link read records: gave B4;
     - "D1/D2 subject" (kind or domain): gave N1.
   - Repair options (a)-(d) are proposals for the stakeholder, not a selected survivor. There was no delegated or resumed work.
4. **Tension search.** Not triggered.
   - No consequential judgment in this Review relied on accepted D1/D2 authority of any project. The authorities relied on are SSDP 7.2.1 process owners, the stakeholder record and the reviewed workplan, which is a D3 cycle contract.
   - The D2 subjects in the trajectories are hypothetical constructs, not accepted authority.

No part of these answers is left unanswered. The coverage limits are those stated in §10.

## 12. Common-mode note

This reviewer shares the Manual author's model family (Claude). It was launched by the authoring session from the issued handoff, and it shares the corpus, the inherited workplan framing and the toolchain. Fresh context is not epistemic independence.

All ten Manual reviewers have been of this family; the Phase B reviewer was of the GPT family. Two of this Review's blockers (B1, B4) entered through repairs that the previous same-family Review suggested, and B2 through its option (a)'s consumer list. This is direct evidence of common-mode failure in same-family review of this family, and option (d) is therefore material.

## 13. D4 statement

No D4 is authorized. This NO-PASS accepts no architecture, product scope or default value. A later PASS would be technical evidence for G1 only. G1 also needs explicit stakeholder acceptance, and shadow D4 needs G2.
