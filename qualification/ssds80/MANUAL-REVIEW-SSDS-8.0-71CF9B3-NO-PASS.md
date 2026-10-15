# SSDS 8 Architecture Manual — Independent D3 Review, candidate 71cf9b3

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout /home/samjin/agent-skills/scientific-software-development-system)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 71cf9b3ac72a23a33c6b7038e6696ebb6f27190f
    SCOPE: the whole proposed Manual as durable D3 owner: (a) §21 and §16.2 closure; (b) fidelity to the
           Phase B-reviewed workplan, including refinements R1-R9; (c) out-of-matrix adequacy; (d) inheritance
           and capability transfer (Architecture 1.6.0, workplan §18, PEM HAS); (e) qualification design;
           (f) doctrine-realization map; (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob b47fea96f568cbf94934f35356fbfc8e5328dc22 (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md, blob c77135ae6ac81eb990b2301f9789991e38d35aac (verified)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23;
           Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b97fb8152d2a5742e17fa172e12204756, verified);
           blob at the candidate 91bde236465178f20c7348280e036d2884dfc216 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml, verified)
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml, verified)
    PRIOR REVIEWS (HYPOTHESIS ONLY): MANUAL-REVIEW-SSDS-8.0-86AB683-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-1FFBBF0-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-53669A5-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-D837363-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-CC005DB-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-C6DA678-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-B595F2C-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-6FF4ED1-NO-PASS.md;
           WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
    REVIEW METHOD: entry through source/roles/software-design/SKILL.md at the public source (expanded entry contract and
           scientific checks read in dist/skills/software-design/SKILL.md); owners read there: architecture-and-design,
           convergence-and-cycle-economy ("Active simplification trigger", "Review strategy after recurrence"),
           workflow-and-workplans (D1/D2 revision gates), evidence-evolution-and-dependencies (revert/restoration),
           protocol-versioning-and-compatibility (PC-001), source/shared/fragments/scientific-checks.md (e=3, e=5);
           full read of the Manual from a git-archive snapshot of the candidate; word diff 86ab683..71cf9b3 of the
           Manual, closure map and stakeholder record; clause comparison against workplan §2 S11, §6.6 ACC and §21;
           constructed trajectories in the permissive and restrictive directions; G1 document checks executed
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session

Governing SSDP version for this Review: 7.2.1. The Manual's refinement table, decision markers, §30 pass and qualification claims, the closure map, commit messages, the handoff's scope text, workplan §0.1/§27 rationale, the diagnostic model's reported results and every prior Review record were treated as hypotheses. Section numbers refer to the Manual at the candidate unless prefixed "workplan". Scratch files were written under `$TMPDIR/ssds80-manual-review-71cf9b3/` (resolved to `/tmp/claude-1000/ssds80-manual-review-71cf9b3/`), because the sandbox does not permit `/tmp/ssds80-manual-review-71cf9b3/`.

## SERIOUS CHALLENGE

**None.** No accepted governing authority was found false, contradictory, ambiguous, inadequate or unrealizable.

- The scientific-checks revising duty (e=5), the workflow owner's D1/D2 revision-gate rule, the evidence owner's revert/restoration rule, P5 and SD-20 are coherent and realizable together.
- The Phase B-reviewed workplan carries an internal tension that B2 below exposes. Its §2 S11 says "restoring old bytes or old declarations restores no validity", while its §6.6 `ACC` lets an earlier in-tenure acceptance count again when a subject's bytes return. The workplan is the cycle contract this Manual supersedes, and the Manual can resolve the tension without changing any accepted owner. It is therefore a Manual blocker (B2), not a Serious Challenge.

## Verdict

**NO-PASS.** Two blockers survive, both in the D1-D3 change rule. This is the eighth successive Review with a finding in that family.

- **B1.** SD-20 compares a record's predecessor with "the predecessor of `(s, r)` at that acceptance". §10.2 defines that predecessor by a list of routes. The list misses tenure starts by scope change, by kind or domain change, and by replacement without `renamed_from`; every such acceptance gets the predecessor "empty". The gate is then told that a revised D1/D2 authority has no predecessor, and a record made under an empty predecessor counts again after a scope round trip. For a cutover, the "other than `r`" exclusion makes a same-bytes re-cutover reuse the earlier native tenure's record. §31.5 expects the opposite, so the 86ab683 B1 re-cutover trajectory is not closed by the normative text.
- **B2.** SD-19/SD-20 are enforced when an acceptance or gate decision is admitted and when `ACCEPT`/`GATE` become ready. Validity reads none of it. When a NATIVE D1/D2 subject's bytes return to an earlier revision accepted in the same tenure, that old acceptance and gate decision support validity again, with no revising review, no counting record and no gate shown the reverted revision's assessments. §10.2 itself says a record counts only while its predecessor has not moved. In a variant, a foreign push alone raises a D2 subject from invalid to valid. The Manual's §0.4 S11 dropped the reviewed clause "restoring old bytes or old declarations restores no validity" without listing the change in §0.3.

These held:
- 86ab683 B1 T1 (a revert to an assessed, never-accepted draft), the revoked-record variant and the pre-loss variant are closed.
- The matching clause had no surviving blocker in the 86ab683 Review. The repairs of that round's N2 and N3 hold in both directions. No new blocker was found in the §6 family; one non-blocking recording gap is N6.
- Every earlier closure re-checked in §5.

This verdict accepts nothing and authorizes no D4.

## 1. Blockers by earliest owner

### B1 — The predecessor is defined by a list of tenure-start routes; scope, kind and replacement starts get "empty", and the cutover case contradicts §31.5 (§10.2, §8.3 step 7, §13.5, §16.6, §19.5, §29.4, §31.5; SD-20)

**Mechanism.**
- §10.2: "The **predecessor** of `(s, r)` at a position is a set of revisions: the last revision of `s` other than `r` accepted in its current tenure; for an acceptance that starts a tenure, for a promotion, split, merge or rename the last accepted revisions of the subjects whose regions it received, and for a cutover or restoration the last revision of `s` other than `r` accepted in an earlier tenure of `s`; otherwise empty."
- "A record **counts** for an acceptance of `(s, σ, r)` only if its entry's predecessor equals the predecessor of `(s, r)` at that acceptance, the record is not revoked or blocked (`status1`), and `cont` holds for it".
- §1.6: "A tenure ends when `s` is demoted to a part, its `scope_id` changes, its kind or domain changes, or its governance mode changes". §1.5: "A change to the subject's own terms is a scope change and ends its tenure."
- So a tenure can start in five ways. Restoration and cutover are listed; a promotion, split, merge or rename creates a new subject identity and is listed. A `scope_id` change of an existing subject, a kind or domain change, and the replacement of one subject by another without `renamed_from` are not listed, and they fall to "otherwise empty".
- §13.2 lets an `AUTHOR` item change a D1/D2 subject's scope terms through `ssds.manifest`, and remove one D2 unit while declaring another of the same kind. A kind change is a human or adopted change with release by the old domain's owner.

**Trajectory T1 — a D2 document moved or re-scoped (restrictive in form, wrong in content; every step conforming).**
1. D2 subject `numerics.solver`, scope `[{ path = "docs/solver.md" }]`, is accepted with its gate at `r0` in tenure `τ1`. Its D4 concretization `kern` carries a recorded tension `t`, an in-repository `CHALLENGES` home binding `numerics.solver` and `kern`.
2. A D2 `AUTHOR` item adds `docs/solver-appendix.md` to the subject's scope, or renames the file and updates the term. `scope_id` changes, so the integrating admission starts `τ2`.
3. The Dispatcher computed the `AUTHOR` task's predecessor at its base, in `τ1`, as `{r0}`. At the acceptance of `r1` in `τ2`, no revision of `s` has been accepted in `τ2`, and a scope change is not a listed route, so the predecessor is empty. The item's record does not count.
4. `REVIEW(s, r1)` is derived with predecessor empty. Its record (predecessor empty) counts. The owner's `ACCEPTANCE PASS` and `GATE_DECISION ACCEPT` are admitted.
5. Section 3 of the gate brief renders "predecessor: none" for a revision of an accepted D2 authority. The brief of the revising review tells the reviewer there is no predecessor. The item's own assessments, made against `r0`, were discarded.

Variants with the same result:
- a kind or domain change of an accepted D1/D2 subject (§13.2);
- an `AUTHOR` item that removes D2 unit `numerics.method` and declares D2 unit `numerics.scheme` over the same regions without `renamed_from`. That is "replacing" in e=5.

**Trajectory T2 — a scope round trip (permissive; the 86ab683 B1 class through an unlisted route).**
1. D2 subject `s` with scope `A` is declared and has no accepted revision. `AUTHOR` item `I1` yields `r1` with record `R1`, whose predecessor is empty, which is correct here. `r1` gets `NO_PASS` and is never accepted.
2. `I2` yields `r2` (predecessor empty). `r2` is accepted with its gate, concretized, and a tension `t` is recorded against that concretization.
3. An `AUTHOR` item changes the scope to `B` (tenure `τ2`). `r3` is accepted there with a record whose predecessor is empty, by T1.
4. A later change restores scope `A` and `r1`'s bytes. `rev` depends only on the terms and the bytes (§1.5), so `cur(s) = r1` in tenure `τ3`.
5. At the acceptance in `τ3` the predecessor is empty again (a scope change). `R1` names the empty predecessor, stands and has `cont`, so it counts. `REVIEW(s, r1)` is not derived. `ACCEPT` and `GATE` are ready. Section 3 renders `R1`: no predecessor and no tension assessed. Yet `r2` and `r3` were accepted since `R1` was made, and `t` was recorded against `r2`'s concretization.

**Trajectory T3 — a same-bytes re-cutover (86ab683 B1 T2).**
1. `s` cuts over to `NATIVE` at `r` with record `R`. `R`'s predecessor is the last revision of `s` other than `r` accepted in an earlier tenure: `r_L`, or empty.
2. A version rollback returns `s` to `LEGACY(p)`. §19.7: "a fresh `LEGACY_ACCEPTANCE` is needed". Tensions are recorded against `s` during the legacy interval.
3. After the repair, the cutover uses the same bytes `r`. §10.2 again excludes `r` and gives `r_L` (or empty), so `R` counts, and the re-cutover's gate is shown the first cutover's assessments.
4. §31.5 expects the opposite: "A re-cutover after a version rollback needs a record whose predecessor is the native revision last accepted before the rollback". With the same bytes that revision is `r` itself, which §10.2's "other than `r`" can never produce. The case is unsatisfiable under §10.2.

An implementer must choose between §10.2 and §31.5. Following §10.2 leaves the 86ab683 T2 reuse open; following §31.5 contradicts the definition.

**Violated text.**
- Scientific checks e=5: "When revising, renaming, splitting, merging or replacing D1/D2 authority, also search recorded tensions bound to its accepted concretizations. In the revision's own record and its gate evidence, record the predecessor identity and, per found tension, a revision-scoped applicability assessment". T1's gate evidence records no predecessor for a revision that has one.
- Workflow owner: "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments, including those marked inapplicable, with their asserters. Acceptance does not ratify an assessment the gate was not shown." In T2 and T3 the gate is shown assessments made against another accepted history.
- SD-20 as recorded: a record counts only if its predecessor "equals the predecessor defined at that acceptance". The direction is realizable; the Manual's definition does not realize it for these routes.
- Manual §10.2 against §31.5 (T3): two statements an implementer cannot both satisfy.
- §29.4 claims **E0** "with the machinery-supplied current predecessor"; the closure map's stakeholder bullet says "no `NATIVE` D1/D2 revision, however produced and in whatever frame, can be gate-accepted or accepted unless a revision-assessment record for exactly that revision counts". Both rely on this definition.

**Earliest owner.** Manual §10.2 (the predecessor definition, §21 item 7), with §16.6 (§21 item 10), §19.5 (§21 item 13) and §31.5. This is not a Serious Challenge: SD-20 stays satisfied when the predecessor is defined as a class.

**Minimum repair direction.** Replace the route list by one class rule, and drop "other than `r`" at a tenure start. For example:
- within a tenure: the last revision of `s` other than `r` accepted in it;
- for the first acceptance of a tenure, prospective or not: the last accepted revisions, in any earlier tenure and governance mode (legacy imports included), of every subject that owned a byte of the regions the new tenure of `s` covers at its start. `s`'s own earlier tenures are included.

Define "accepted" by admitted records (see N1), so the predicate stays an S0/S1 fact. Align §31.5 and §19.5 with the result. The family-level options are in "Family-level assessment" below.

**Required discriminator (real owners: Dispatcher envelope, Admission step 7, S3 readiness, Interface gate rendering).**
- T1 and its variants. Expected:
  - the brief and section 3 name `{r0}` (for a replacement, the replaced subject's last accepted revision);
  - the `AUTHOR` item's record made against `r0` counts.
- T2. Expected: `R1` does not count, and `REVIEW(s, r1)` is derived with predecessor `{r3}`.
- T3. Expected: one statement in §10.2 and §31.5. Under the class rule, the re-cutover's predecessor includes the legacy-interval acceptance, so `R` does not count.
- An implementation that returns "empty" for a scope, kind or replacement start, or that excludes `r` at a cutover, must fail.
- §31.5 has no scope-change, kind-change or replacement case, and its re-cutover case contradicts §10.2. A green §31.5 coexists with B1 (DS-001).

### B2 — SD-19/SD-20 gate the admission of acceptances, but validity reuses an earlier in-tenure acceptance of a reverted D1/D2 revision; the reviewed S11 clause against restoration was dropped unsurfaced (§5.5 `ACC`, §10.2, §8.3 step 7, §10.3, §0.4 S11, §0.3, §29.4, §29.5; SD-19, SD-20)

**Mechanism.**
- §5.5: "`ACC(s)` = admitted passing ACCEPTANCE (or LEGACY_ACCEPTANCE, EXTERNAL_ACCEPTANCE per mode) on exactly `(s, scope_id(s), cur(s))`, admitted at or after `τ(s)`". Nothing restricts it to the latest accepted revision. §1.10: acceptance is "a passing acceptance judgment on exact `(subject, scope_id, rev)` in the current tenure".
- An acceptance `j0` of `(s, σ, r0)` is never superseded when `r2` is later accepted: supersession needs the same target (§8.3 step 3). Its basis entry `content (s, r0, EXACT)` is satisfied again whenever `cur(s) = r0`. So `j0` is current again after any return to `r0`'s bytes in the same tenure.
- The required gate's `GATE_DECISION` has basis "`content` on the gated subject revision; `record` on every record of the evidence core shown" (§4.3), so it is current again too.
- The SD-19/SD-20 condition lives only in Admission step 7 ("Admission refuses a passing `ACCEPTANCE` … and a `GATE_DECISION ACCEPT` … unless a revision-assessment record … counts") and in `ACCEPT`/`GATE` readiness.
- `ACCEPT(s)` is derived only for "a subject without a valid acceptance". `GATE(g)` is derived only for "a required human gate without a current `ACCEPT`". `REVIEW(s, r)` is derived only from those. A revert therefore derives none of them.
- §10.2 itself: "Re-accepting an unchanged revision whose predecessor has not moved reuses its record". After `r2`'s acceptance the predecessor of `(s, r0)` is `r2`, so `j0`'s record no longer counts. Yet `j0` and its gate decision support validity.
- §5.8 shows the result only as "**drift** (`cur(s)` differs from `acc(s)`, the latest revision with a passing acceptance — a display view only)".

**Trajectory T1 — a stale restore of a D2 authority known to be wrong (every step conforming).**
1. D2 subject `numerics.method`, `NATIVE`, tenure `τ`. `r0` is accepted (`j0`, with record `R0`) and gate-accepted (`h0`).
2. Evidence on its concretization shows `r0`'s method is wrong. A tension `t` is recorded (a `CHALLENGES` home binding `numerics.method` and `kern`).
3. A D2 `AUTHOR` item yields `r2`. Its record `R2` (predecessor `r0`) assesses `t` as applicable. `r2` is accepted (`j2`) and gate-accepted (`h2`). D4 work concretizes `r2`.
4. A human restores `docs/method.md` from an old backup, or resolves a merge by taking the old side. The push is absorbed (§8.6), and `cur(numerics.method) = r0`. The tree's declarations are unchanged, so nothing is quarantined.
5. `j0` is in `ACC`. Its base is `T`, its content entry holds, and its governing prerequisites are unchanged. `h0` is current. Evidence whose target is `r0`'s claim content is current again. `valid(numerics.method) = T`, or `P` only if a failing assessment counts.
6. No `ACCEPT`, `GATE` or `REVIEW(s, r0)` obligation is derived, and step 7 is never consulted. The only consequences are a drift display and an `INTAKE` obligation for the foreign change. Its disposition is R2, so an agent may `ABSORB` it, and validity is `T` meanwhile.
7. D4 items whose governing unit is `numerics.method` become ready against `r0`, the revision `t` showed wrong. No gate saw the revision `r2 -> r0`, its predecessor `r2`, or a revision-scoped assessment of `t`.

**Variants.**
- *The revert through an `AUTHOR` item.* The item's candidate yields `r0` and carries its own record (predecessor `r2`, `t` assessed). After integration `s` is valid through `j0` and `h0`. Any acceptance obligation on `(s, σ, r0)` is answered by `j0`, "the first admitted judgment of its kind on its target that is bound to it or recorded on its target by an authenticated human" (§10.3). The item's record is never shown to a gate.
- *Validity raised from `F` by presence.* `j2` was revoked by an upheld challenge, or `r2` was integrated and its acceptance is still pending, so `s` is invalid. A foreign push restoring `r0`'s bytes alone makes `valid(s) = T`.

**Violated text.**
- Scientific checks e=5 and the workflow owner's D1/D2 revision-gate rule, as quoted in B1. The revert is "revising … D1/D2 authority". It takes effect with no record of its own counting, and with no gate shown its assessments: "Acceptance does not ratify an assessment the gate was not shown."
- Evidence owner: "Revert/restoration preserves the historical realization/event but reconciles present applicability, assessment/admissibility, authority binding … over the affected surface."
- Workplan §2 S11 (the reviewed contract): "An acceptance belongs to one subject tenure and never revives once that tenure ends; restoring old bytes or old declarations restores no validity."
  - Manual §0.4 S11 reads only "An acceptance belongs to one subject tenure and never revives." It drops the restoration clause, and dropping "once that tenure ends" makes "never revives" absolute, which §5.5 contradicts.
  - §0.1 says of the superseded workplan sections: "Where this Manual refines them, §0.3 lists each refinement; there is no other intended difference." §0.3 does not list this change.
- Manual §0.4 S3: "Repository presence promotes nothing" (the presence variant).
- SD-20 as realized in §10.2: a record counts only while the predecessor has not moved. §29.4 claims **E0**, and §29.5 (documentation row) says "every D1/D2 revision, however produced, needs its revision-assessment record before acceptance". The revert route makes the D1/D2 revision effective without one.

**Earliest owner.** Manual §5.5 `ACC` for `NATIVE` D1/D2 subjects together with §10.2 and §8.3 step 7 (§21 items 5, 7 and 10), and §0.4/§0.3 for the unsurfaced S11 change.

For D3 and D4 subjects, in-tenure reuse by content identity is the reviewed early-cutoff design (FB3E542: "This is not ordinary early cutoff within one tenure", contrasting cross-tenure revival). This Review does not ask to change it. For D1/D2 subjects, SD-19/SD-20 and e=5 make the transition itself the object of the revising duty.

**Minimum repair direction.** For a `NATIVE` D1/D2 subject, make "a revision-assessment record for `(s, cur(s))` counts" (B1's class-defined predecessor; S0/S1 facts) a condition under which an acceptance and a gate decision support validity. A revert then derives `ACCEPT(s)` and `REVIEW(s, r0)` with predecessor `r2`, and an unchanged re-acceptance keeps reusing its record. Restate S11 explicitly, and list the restatement in §0.3: in-tenure content reuse stays for D3/D4 subjects, and no D1/D2 validity returns without a counting record. Alternatives are in the family-level assessment.

**Required discriminator (real owners: Derivation S2/S3, Admission step 7, Interface gate rendering).**
- T1. Expected:
  - after the restore, `valid(numerics.method)` is not `T`;
  - `ACCEPT` and `REVIEW(numerics.method, r0)` are derived with predecessor `r2`, and the brief carries `t`;
  - `GATE(g)` waits for that record, and section 3 renders `r2` and the assessment of `t`.
- The `AUTHOR` variant. Expected: `j0` does not answer or discharge the item's acceptance; the item's own record counts and is shown to the gate.
- The presence variant. Expected: validity stays `F`.
- Contrast: a D4 subject reverted within its tenure is valid again through its old acceptance, as reviewed.
- An implementation that enforces the condition only at admission and readiness must fail. §31.5 has no revert-to-accepted case, so a green §31.5 coexists with B2 (DS-001).

### Family-level assessment (convergence owner, "Active simplification trigger"; "Review strategy after recurrence")

- Findings in the D1-D3 change rule, by Review: `b595f2c` B3, `c6da678` B3, `cc005db` B1, `d837363` B3-B4, `53669a5` B2, `1ffbbf0` B2, `86ab683` B1. This Review adds B1 and B2.
- One pattern recurs. The revising duty has been attached to particular events or routes, and each Review found a route outside the list:
  - producing admissions (repaired by SD-19);
  - acceptance admissions keyed on content identity (repaired by SD-20);
  - now tenure-start routes (B1) and the validity reuse that no admission touches (B2).
- The owner's mandatory trigger applies: "repeated patches around the same mechanism … special cases accumulating around one owner … family closure that does not reduce the failure surface". This is a non-local recurrence. Another listed exception should not be added.
- The convergence owner says to prefer "removing, narrowing, altering, consolidating" over additive repair, and to hold accepted parent semantics fixed. The governing semantics here are e=5, the workflow D1/D2 gate rule, the evidence owner's restoration rule, and SD-19/SD-20 as directions.
- Options for the stakeholder (Phase C handoff §5 boundary):
  - **(a) One state condition with a class-defined predecessor (recommended).**
    - A `NATIVE` D1/D2 subject's acceptance and gate decision support validity only while a revision-assessment record for `(s, cur(s))` counts.
    - The predecessor is defined by B1's class rule.
    - Step 7's refusal stays, to order the gate after the record.
    - Readiness and validity then read one condition. Every route (producing, accepting, reverting, re-scoping, cutting over) is covered by the state rather than by a list.
    - It removes the route list and keeps SD-20's equality as chosen. D3/D4 early cutoff is untouched.
    - Cost: reverts of D1/D2 authority to an earlier accepted revision, and first acceptances after a scope or kind change, need a revising review. The latter already need acceptance.
  - **(b) Order key instead of equality.**
    - A record counts only if it was admitted after the current tenure's start and after the latest acceptance of any other revision of `s`. `ACC` for D1/D2 likewise excludes acceptances admitted before such a later acceptance.
    - The predecessor becomes display-only, though e=5 still needs it defined as a class.
    - This changes SD-20's chosen equality, so it needs the stakeholder.
  - **(c) Accept as disclosed residuals.** Same-tenure reverts reviving an earlier D1/D2 acceptance; an empty predecessor at scope, kind and replacement starts; same-bytes re-cutover reuse.
    - This relaxes e=5 and the workflow gate rule for those routes and needs explicit stakeholder acceptance.
    - §29.4, §29.5, §31.5, the S11 statement and the closure-map bullet must then be corrected.
  - **(d) A different-family Review before the repair.** Same-family Reviews passed over the revert route for eight Manual rounds.
- Open question for the owner, not part of a blocker: whether an ABA return of the predecessor value should count (N1).

## 2. Non-blocking findings

- **N1 — "Accepted" is undefined, and the predecessor is a revision value (§10.2).**
  - "the last revision of `s` … accepted" does not say whether it means an admitted passing `ACCEPTANCE` (an S0 fact), a standing acceptance (not revoked or vetoed) or validity. It also does not say whether a `LEGACY_ACCEPTANCE` counts in an earlier tenure.
  - The readings give different predecessors after a revocation, a veto or a legacy import. B1's T3 and the B1/B2 repair depend on the answer.
  - Because the predecessor is a set of revision identities, a return of the value (`r0 -> r2 -> r0` by re-acceptance, or `r2` revoked under the standing reading) makes a record made before `r2` count again.
  - SD-20's table text covers it ("A tension recorded after the record does not invalidate it"). The stakeholder's question, however, was posed "with no change of predecessor".
  - Repair: define "accepted" by admitted records, and either key the predecessor on the accepting record's identity or disclose the ABA case.
- **N2 — The re-derived revising review may collide with the answered one (§10.2, §10.3).**
  - §10.3 makes `REVIEW(s, r)` answered by "a revision-assessment record", and §10.2's definition of such a record does not require that it counts.
  - When a record stops counting with the predecessor unchanged (revoked, blocked, withheld by a loss boundary), "`REVIEW(s, r)` is derived afresh". Obligation identity is "`sha256(… ‖ rule id ‖ JCS(target) ‖ JCS(parameters))`", and no parameter distinguishes the fresh obligation. It is then already answered and "never dispatched again", and `ACCEPT` and `GATE` stay unready.
  - This fails closed, as a liveness gap. Repair: only a counting record answers it, or the parameters include the predecessor and the answering record.
- **N3 — SD-20's machinery is not fully stated.**
  - §12.2's envelope grammar has no predecessor field, although §10.2 places the predecessor "in the envelope and brief".
  - "Admission refuses an entry naming another (`CONFORMANCE_*`)" does not say whether the `TASK_RESULT` or only the slot is refused. It also does not say whether the comparison is with the envelope or with the predecessor at admission.
  - For a revising review derived in a frame, "at the task's base" should name the frame.
  - §16.6's rule sentence ("A gate on a D1/D2 revision without a revision-assessment record for it is not ready") and §31.5's first sentence ("until a revision-assessment record for exactly that revision is admitted") still say "admitted" rather than "counts".
  - §30 accounts for SD-16 and SD-19 but not for SD-20's envelope field and Admission comparison.
- **N4 — Cutover binding, residue of 86ab683 N1 (§19.5, §10.2).**
  - §19.5 now states the binding, but the trigger "once a `MIGRATE` item proposing the cutover is accepted, S3 derives `REVIEW(s, r)` for that prospective tenure" is a second trigger, absent from §10.2's table.
  - It names no frame. A `MODE_TRANSITION` is not a transformation, and mode is not a declaration key, so no frame holds `s` as `NATIVE` before the transition. "Bound to that admission (§7.6)" is by analogy, since §7.6 binds acceptances "made in the frame of `X_0`".
  - A cutover not proposed by a `MIGRATE` item has no route to its record (restrictive).
  - Repair: state the trigger and its derivation context in §10.2.
- **N5 — Seed wording, residue of 86ab683 N2 (§6.3, §17.5 versus §6.10).**
  - §6.3 still treats an execution that does not record "a seed it drew" as unpinnable, and §17.5 says "every class records a seed or replicate identity an execution draws".
  - §6.10 now says runner-external randomness has "no recorded seed" and is unrecorded variation.
  - Read literally, the first requires detecting code-drawn seeds. Say "a seed the runner supplied". The disclosure itself (§6.10, §31.3, §32.2) is accurate.
- **N6 — Reads through symbolic links (§6.3 read entries, §20.1; matching family, recording boundary).**
  - A read entry is "for every file of the realization's tree the designated runner observed being read, `({ path = p }, cid)` with `cid` over that file in the tree". A tracked symbolic link is a tree entry whose blob is its target string.
  - If a runner records the link path, two things escape. A link to a file outside the tree (`data -> /scratch/mesh`) hides an external read as a tree-resident one, which SD-18's fail-closed class rule does not catch. A link to a tracked file outside the closure leaves that file's content unrecorded.
  - Runs on different targets are then the same content in both predicates. Permissively, a run on another mesh can serve (1) or (3).
  - The intended reading (the file whose bytes were read) is available, and a class that does not resolve links does not "observe every read outside the tree". The gap is therefore non-blocking.
  - Repair: state that a read through a link is recorded at its resolved target, as a read entry for a tracked target or an external read otherwise. Add a §31.3 discriminator.
- **N7 — §1.9 repair edges, residue of 86ab683 N4.**
  - "(`path`, `file`, `heading`, `symbol` or `anchor`; a `prefix` may be empty)" is ambiguous: an exemption for `prefix` terms, or the empty-string prefix.
  - The non-empty requirement refuses a unit over an empty file (`__init__.py`, `py.typed`). It may also refuse a realignment back to `Σ`'s term after a foreign deletion, if realignment counts as changing the term.
  - No S3 finding is raised when a declared term later resolves to `ABSENT`; only malformed anchors raise one.
  - The analyzer-completeness restriction (§2.6) closes 86ab683 N4's trajectory.
- **N8 — Closure map (aid only).**
  - Items 7, 10, 13 and 27, and the stakeholder-list bullet "no `NATIVE` D1/D2 revision, however produced and in whatever frame, can be gate-accepted or accepted unless …", rely on text affected by B1 and B2.
  - Item 5 relies on §5.5 `ACC` (B2).
  - The stakeholder record's SD-20 row correctly still says "(pending)".

## 3. Closure audit (§21 items and §16.2 rows)

The closure map was used only to locate text, and its annotations were checked against the Manual.

**Not substantively resolved:**
- item 7: the revising-review obligation rule, keyed on a route-listed predecessor (B1) and enforced only at admission and readiness (B2);
- item 10: the gate template meeting Channel C, which shows "no predecessor", or another history's assessments, for D1/D2 revisions (B1), and is never reached for a revert (B2);
- item 13: the cutover owner acceptance, whose predecessor contradicts §31.5 (B1 T3);
- item 27: the §29.4 revising row and §29.5 documentation row E0 claims (B1, B2).

**Resolved with a blocker in part:** item 5 (§5.5 `ACC` for `NATIVE` D1/D2 subjects, B2). The rest of item 5 is resolved.

**Resolved with non-blocking defects:**
- item 1 (N7);
- items 4 and 11 (N5, N6).

**Resolved:** items 2, 3, 6, 8, 9, 12 and 14-26. Each decision was located, and each is a decision rather than a route.
- Delegated D4 space is bounded: file-type table, diff implementation, parser libraries, mutation tool, index and journal engines, limit values, witness kinds.
- Item 14's "monotonic write-ahead publication-attempt record" is resolved by its removal (R4).

**§16.2:** §26.4 is untouched by the 86ab683..71cf9b3 diff and was re-read. Every row of both workplan tables has a final disposition there, as do 1.6.0 §4 and §14, including every Deferred row:
- invariants 4, 9, 15, 17 and 26;
- surfaces §5, §6, §12 and §18.

None was found unresolved.

## 4. Refinements R1-R9

| # | Assessment |
|---|---|
| R1 | **Sound.** The 86ab683 N3 repair records the unpinnable mark, the class's declared attribute set and its read-observation flag by value at realization. `ext` therefore reads the record only, and a later policy change can only make old failures unmatchable (fail closed). The N2 repair discloses runner-external randomness as unrecorded variation, caught only by (2) in fact. `on⁻` is untouched, so `on⁺ ⇒ on⁻` and the guard hold. Residuals: N5 (wording) and N6 (symlink recording). |
| R2-R7 | **Sound.** Unchanged since 86ab683 and re-read. |
| R8 | **Sound.** Unchanged. A `TASK_RESULT` cannot be superseded (a second result for one task is rejected), so SD-20's standing correctly reads only `status1` and `cont`. |
| R9 | **Sound.** Unchanged. The adverse-judgment veto is unaffected by B2: B2 concerns passing judgments that were never contradicted. |

SD-20 is a decision inside §21 items 7 and 10, not a §0.3 refinement; §0.3's narrative lists it. Its defects are B1 and B2. §0.4 S11's dropped clause is an unlisted difference from the reviewed workplan (B2).

## 5. Previous findings, Phase B closures and N1-N4

Method: the 86ab683 findings were re-derived against the candidate text. Earlier findings were taken from each record's finding list and from the 86ab683 record's re-verification (a hypothesis). Their anchors were re-checked in the candidate, and the 86ab683..71cf9b3 diff was checked for whether it touches their mechanism.

**86ab683.**
- **B1** is partly closed.
  - T1 (a revert to an assessed, never-accepted draft) is closed: the predecessor of `(s, r1)` is `r2` and the old record names `r0`.
  - The revoked-record variant (`status1`) and the pre-loss variant (`cont`) are closed.
  - T2 (a same-bytes re-cutover) is not closed by §10.2 and is contradicted by §31.5 (B1 T3 here).
  - The repair's own definition has the scope, kind and replacement gaps (B1).
- **N1** is closed in form (§19.5 states the binding); its residue is N4.
- **N2** is closed by disclosure (§6.10, §31.3, §32.2); the wording residue is N5.
- **N3** is closed (by-value recording; §17.5 shows newly unmatchable failures).
- **N4** is closed for the trajectory it gave (§1.9 now covers `path`/`file`; §2.6 forbids analyzer completeness over an `ABSENT` term). The residue is N7.
- **N5** is closed (§18.4 names the paths whose governed status the delta changes).
- **N6** is closed: one entry per subject, a predecessor set, "every … record that counts", and `NATIVE` in §29.4.
- **N7** is superseded by N8.

**1ffbbf0.**
- **B1** is closed (SD-18 cases in §31.3; re-checked with the by-value repair).
- **B2** is closed for each route it named: frame and prospective acceptances, merged revisions, slotless answers. The family remains open through B1 and B2 here.
- **N1** is closed through 86ab683 N4's repair, with N7 residue.
- **N2** is closed by removal.
- **N3** is closed in form (the predecessor is defined and machinery-supplied); its definition is B1.
- **N4** is closed (86ab683 N5).
- **N5** and **N6** are closed.
- **N7** is superseded.

**53669a5.**
- **B1** is closed.
- **B2** is closed for readiness and gate ordering; the family residue is B1 and B2 here.
- **B3** is closed (targets, never timing; §18.4 re-read).
- **N1**, **N3**, **N4**, **N7** and **N8** are closed.
- **N2** and **N9** are superseded.
- **N5** and **N6** are closed, with residues closed or in N7.

**d837363.**
- **B1**, **B2** and **B4** are closed. §6.3, §6.5 and §1.2 are unchanged in mechanism.
- **B3** is closed for the human, absorption and adoption routes it named. B2 here is a route it did not name.
- **N1-N6** are closed.
- **N7** is closed (the slot carries the predecessor).
- **N8** is superseded.

**cc005db.** **B1-B3** and **N1-N8** are closed. The diff does not touch the write set, the resolution context or the product-scope veto. §27.3 still discloses re-identification and now requires each re-identified D1/D2 revision's record.

**c6da678.** **B1-B3** and **N1-N12** are closed. The anchors were re-checked:
- `stands⁻` requires `¬superseded(d)`;
- `same` for `COMPLETENESS` compares member revisions;
- `REFUSED` is named in R9;
- the residual-part `cid` is defined in §6.3;
- `prefix = ""` is stated in §1.8;
- ref locality is in §13.2;
- the agent-reassessment disclosure is in §5.5.

**b595f2c.** **B1-B4** and **N1-N8** are closed. The anchors were re-checked:
- §3.4 has the machinery `COMPLETENESS` producer;
- §13.3 reads "whatever its kind";
- §13.2's `AUTHOR` scope lists unit kinds, not "document units";
- §14.5 records host-dependent analyzer output.

**6ff4ed1.** **B1-B4** and **N1-N12** are closed. The anchors were re-checked:
- `qualification` is in the `GATE_DECISION` schema;
- §8.3 step 5 reads "gains no new … and no existing one grows";
- §26.4 has rows for 1.6.0 §4 and §14;
- export is listed in §0.5;
- §29.3 has the common-mode and priority rows.

**Phase B §3 closures.** §5.3-§6.10 restate workplan §6.6 and change it only in the restrictive direction.
- "Nondeterministic old-content observations defeat (2)" holds across recorded free attributes and seeds. Runner-external randomness defeats (2) only in fact, as in the reviewed contract.
- "Executed content includes runtime inputs/observed reads" holds, except for the N6 recording edge.
- The promotion, tenure and restoration closures (FB3E542 A and siblings) hold across tenures. B2 concerns reuse inside one tenure for D1/D2 subjects only.

**Phase B N2 re-test.** The bounding completeness judgment was taken through `P`, blocked, revoked, superseded, loss-withheld, and non-current by a membership change. Against each:
- a differing old-content run on an alternate tree that differs only outside the recorded regions (including another span of a recorded file) stays in (2);
- a yielding present-content run stays in (4).

Both hold because `on⁻` is unchanged and `ext` reads the by-value record and no completeness. The support-cycle clamp (R2) and the corrupt-prefix halt (R3) are unchanged and fail closed before any current assertion.

**Phase B N1, N3, N4.**
- N1 remains open and disclosed (§32.2, §32.4).
- N3's limits are carried in §31.3.
- N4's costs are in §32.3.

**Both directions.**
- Permissive:
  - B1 T2 and T3 (record reuse across tenure starts);
  - B2 (validity reuse on revert);
  - N1 (ABA);
  - N6 (symlinked inputs).
- Restrictive:
  - B1 T1 (the `AUTHOR` item's correct record is discarded);
  - N2 (a re-derived review that is never dispatched);
  - N4 (no route for a cutover without a `MIGRATE` item);
  - N7 (units over empty files).
- The previous round's non-blocking repairs were attacked in both directions:
  - N1's repair holds, with residue N4;
  - N2 holds, with wording residue N5;
  - N3 holds;
  - N4 holds, with residue N7;
  - N5 and N6 hold;
  - the B1 repair introduced B1 here (its definition) and left B2's route open.

## 6. Out-of-matrix trajectories attempted

**Broke the candidate:**
- B1:
  - a D2 document re-scoped or moved;
  - a kind change;
  - a replacement without `renamed_from`;
  - a scope round trip reusing an empty-predecessor record;
  - a same-bytes re-cutover.
- B2:
  - a stale restore of a known-wrong D2 revision;
  - an `AUTHOR`-item revert answered by the old acceptance;
  - a foreign push raising validity after revocation or while acceptance is pending.
- N1: an ABA return of the predecessor value; a revoked intervening acceptance under the standing reading of "accepted".
- N2: a revoked revising record with the predecessor unchanged.
- N6: a tracked symbolic link to a dataset outside the tree.

**Held:**
- **SD-20:**
  - 86ab683 T1;
  - a revoked or blocked record (does not count) and an overridden blocking challenge (`PROVISIONAL`, counts; the override is the human's accountable act);
  - a pre-loss record (withheld) and one held by a continuity attestation (counts);
  - two `AUTHOR` items on one subject, where the second's acceptance moves the predecessor and the first's record stops counting (correct, restrictive);
  - a gate decided after the acceptance of the same `r` ("other than `r`" keeps the predecessor);
  - an `AUTHOR` item revising two D2 subjects (one entry each);
  - an adopted promotion (predecessor from the parent);
  - a forged predecessor in an entry (refused, `CONFORMANCE_*`).
- **Derivation:**
  - "counts" reads S0 records and positions and the S1 facts `status1` and `cont`, and is read only by S3 readiness and Admission;
  - S2 is unchanged;
  - the stratification check and the least fixed point are unaffected.
- **Matching family:**
  - a declared-set change by `RULESET_ADOPTION` after the N3 repair (old observations keep their recorded flag and set; new and old compare unequal, fail closed);
  - an observing-class run against an unobserving-class failure (`ext` false);
  - variation in the clock or an environment variable (an unrecorded attribute, disclosed);
  - a Git submodule read (an external read pinnable by the git pin grammar);
  - an LFS pointer (its blob changes with the content);
  - Phase B N2 and the completeness-polarity variants as above.
- **§1.9 and §2.6 repairs:**
  - a misspelled `path` term is refused;
  - a file deleted later stays well formed;
  - analyzer completeness over a unit with an `ABSENT` term is refused, so the 86ab683 N4 rename sketch widens.
- **§18.4 repair:** a `QUARANTINE` of an `ignore` delta names the paths whose governed status changes, and the effective `Σ` still governs them.
- **Publication, currentness, gates and floors** (§22-§23, §10.5, §15.4 and §16.6 re-read; unchanged except §16.6's wording):
  - two processes sharing one host key;
  - a crash after a successful compare-and-swap;
  - a paused publisher against a landed fence;
  - a risk override never covers `GATE`;
  - an unqualified `ACCEPT` is refused while disputed evidence is listed;
  - floor items cannot be reclassified.
- **Partition and scope identity:**
  - static sibling nesting is rejected;
  - crossed anchors resolve to `ABSENT`;
  - byte-preserving refinement keeps `scope_id`, `rev` and tenure.

## 7. Minimum architecture and capability transfer

**Changes since 86ab683.**
- No component, tier or record kind is added.
- SD-20 adds an envelope value, an Admission comparison and a counting predicate. §30 does not account for them (N3).
- Option (a) of the family assessment replaces two event-point conditions with one state condition. It adds no component.
- §30's "No new primitive, component, persistent surface or record tier" remains true.

**Capability transfer.**
- PC-001 (`AUTHORITY_BOUND`) was independently resolved at the public source (protocol-versioning-and-compatibility: "When a new profile becomes current, every older supported profile remains frozen and independently testable.") and is preserved:
  - Core imports nothing from SSDS (§26.2);
  - §31.8 tests Core without SSDS;
  - the frozen 1.6.0 file, `source/` and `dist/` are byte-unchanged.
- The 1.6.0 transfer in §26.4 is complete.
- The 7.2.1 e=5 capability (predecessor identity and revision-scoped assessments before a D1/D2 revision takes effect) is not fully transferred (B1, B2). Nor is the evidence owner's revert/restoration reconciliation for D1/D2 authority (B2).

**PEM basis.**
- PEM is activated: replacement of mature machinery and a suspected recurrence.
- `origin/main` is `af0455753e20ee54a969c844872e29e270007211`. The PEM blob `1561797125622f355f84eb27319f87e8fa4227d9` is identical at the candidate and on `origin/main`.
- `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run in the checkout, reports "PEM schema 1 valid: 5 families, 0 notices".
- HAS dispositions:
  - PC-001: applicable and binding;
  - DS-001: applicable as evidence only; it bears on §8;
  - FF-001: applicable as evidence only (§19.9 genesis procedure present);
  - SP-001 and SP-002: applicable as evidence only.

## 8. Qualification design

§31 binds claims to real owners and marks every runtime group UNEXECUTED; nothing beyond §31.10 is claimed as executed.

**Adequate for what they target:**
- the §31.3 SD-18 cases and the corrected ensemble sentence;
- the §31.5 recurring-bytes case for a revert to an unaccepted draft;
- the revoked and pre-loss record variants.

**Green fixtures can coexist with these defects (DS-001):**
- B1: no scope-change, kind-change or replacement case, and the re-cutover expectation contradicts §10.2;
- B2: no revert to an accepted revision and no presence variant;
- N2: no re-derivation after revocation with an unchanged predecessor;
- N6: no symbolic-link input.

§31.5's first sentence says "admitted" (N3). The discriminators in §1 are required. The §14.7 `HARD` qualification design is adequate as design, with proposed-default values. The diagnostic model was not run: its model file is unchanged since Phase B, and it models no revision gates, predecessors, runner classes or seeds.

## 9. Doctrine-realization map and O1

The E0/E1 claims are tied to existing mechanisms, with two exceptions:
- §29.4's revising row claims **E0** "with the machinery-supplied current predecessor and standing, however the revision was produced". This is false for B1's routes (wrong or empty predecessor) and B2's revert route (no record, no gate).
- §29.5's documentation row, "every D1/D2 revision, however produced, needs its revision-assessment record before acceptance", is false for B2's route if validity is read as acceptance.

The enumeration is complete with its catch-all row, and the disclosed-E3 list (§29.6) is appropriately conservative.

O1 (§0.5) is unchanged: realized record, readers, routine questions, realized-record architecture and marked surfaces.
- "Beyond the requested deliverable: None" is consistent with the stakeholder record.
- B2 bears on the routine question "What governs this subject, at which revision?". After a revert, the answer is a revision no gate saw as a revision; the drift display is the only signal.
- Technical Review accepts no marked item, product scope or default value.

## 10. What was verified and how; what was not

**Executed** against a `git archive` snapshot of the candidate under `$TMPDIR/ssds80-manual-review-71cf9b3/`, and against the repository:
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` (in the snapshot): 4 tests, OK.
- `git diff --check 86ab683cb1b16fd818b84805636d66b215131be3 71cf9b3ac72a23a33c6b7038e6696ebb6f27190f`: clean (exit 0).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 71cf9b3ac72a23a33c6b7038e6696ebb6f27190f`: 23 files, all within the expected set:
  - the Manual and the closure map;
  - eight Manual review handoffs and eight NO-PASS records;
  - the Phase C handoff and the Phase C continuation handoff;
  - the session handoff;
  - the stakeholder record;
  - two index lines.

  The 86ab683..71cf9b3 diff touches the Manual, the closure map, the 86ab683 handoff and record, and the stakeholder record (item 15, SD-20).
- `orchestrator/docs/architecture.md` (blob `39e6de7…`), `source/` (tree `fac2238…`) and `dist/` (tree `6bf729e…`) are identical at `fad3ee4…` and at the candidate (`git diff --quiet`).
- All header blobs match.
- PEM was validated as in §7, in the checkout, whose PEM blob is identical to the candidate's.

**Read** at the public source: the owners listed in the header, with the exact text quoted in §1 and §7.

**Read in full:** the Manual at the candidate.

**Read in part:**
- the closure map diff;
- the stakeholder record diff;
- workplan §2 S11, §6.6 `valid`/`ACC`, §19 rows, §21 and its structural-intake counterexamples;
- Phase B Review §3;
- the 86ab683 record in full;
- the 1ffbbf0 B2 and d837363 B3 trajectories;
- the FB3E542 revival finding;
- the finding lists of every earlier Manual Review.

**Not verified:**
- any runtime behavior (none exists); the trajectories are deductions from the specified contracts;
- the diagnostic model (not run);
- empirical costs: how often D1/D2 subjects are re-scoped, moved or reverted; how often runner inputs pass through symbolic links;
- the full text of the Manual Reviews before 86ab683 beyond their finding lists and the passages named above;
- workplan §18 and §27 beyond targeted reads;
- the earlier workplan NO-PASS records beyond Phase B Review §3;
- D1, D2, D4 and specialist entrypoint texts beyond the software-design entrypoint and the scientific-checks fragment;
- the testing, storage, concurrency, security and inspectability owners, which were not loaded because no finding turned on them.

## 11. Scientific-checks answers

- **Material findings:** B1, B2 and N1-N8 above. No agents were launched. The only tools run were git, the unit test and the PEM validator, and they produced no further findings. No material scientific finding about any project's science was made; this Review concerns D3 authority for software that mediates scientific evidence.
- **Realized results:** this Review produced, ran and reviewed no realized scientific results, including through the tools it ran, and it prepared no gate evidence. Its output is D3 review evidence toward G1. The unit test, `git diff --check` and the PEM validator are structural software checks, not realized results, so no null envelope is owed. For transparency, review coverage and its limits are stated in §10.
- **Variants:** no analysis, pipeline, preprocessing, model or parameter variant was evaluated or selected (count 0).
  - Constructed trajectories are review hypotheses.
  - Five clauses were compared under two readings each, as interpretation, with textual coherence against the rest of the Manual and the owners as the criterion:
    - "accepted" in §10.2 (admitted record or standing acceptance), which gave N1 and bears on B1 T3;
    - §0.4 S11 "never revives" (absolute or tenure-bound), which gave part of B2;
    - whether a non-counting record answers `REVIEW(s, r)`, which gave N2;
    - what "observed being read" denotes for a symbolic link, which gave N6;
    - §1.9 "a `prefix` may be empty", which gave N7.
  - The family options (a)-(d) are proposals for the stakeholder, not a selected survivor.
  - There was no delegated or resumed work.
- **Tension search:** not triggered.
  - No consequential judgment relied on accepted project D1/D2 authority. The authorities used are SSDP 7.2.1 process owners, the stakeholder record and the reviewed workplan, a D3 cycle contract.
  - The D2 subjects in the trajectories are hypothetical constructs, not accepted authority of any project.

No part of these answers is left unanswered; the coverage limits are those stated in §10.

## 12. Common-mode note

This reviewer shares the Manual author's model family (Claude). It was launched by the authoring session from the issued handoff, and it shares the corpus, the inherited workplan framing and the toolchain. Fresh context is not epistemic independence. All nine Manual reviewers have been of this family; the Phase B reviewer was of the GPT family.

B2's route has been open since the first Manual candidate: a revert reviving an in-tenure D1/D2 acceptance is the reviewed `ACC` combined with SD-16/SD-19's event keys. Eight same-family Reviews attacked "every route by which a revision or an acceptance can arise" without naming it. This is direct evidence that same-family Review is saturating on this family, and option (d) is therefore material.

## 13. D4 statement

No D4 is authorized. This NO-PASS accepts no architecture, product scope or default value. A later PASS would be technical evidence for G1 only. G1 also needs explicit stakeholder acceptance, and shadow D4 needs G2.
