# SSDS 8 Architecture Manual — Independent D3 Review, candidate 86ab683

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout /home/samjin/agent-skills/scientific-software-development-system)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 86ab683cb1b16fd818b84805636d66b215131be3
    SCOPE: the whole proposed Manual as durable D3 owner: (a) §21 and §16.2 closure; (b) fidelity to the
           Phase B-reviewed workplan, including refinements R1-R9; (c) out-of-matrix adequacy; (d) inheritance
           and capability transfer (Architecture 1.6.0, workplan §18, PEM HAS); (e) qualification design;
           (f) doctrine-realization map; (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob d6b6480a076f92b345b4d9823f2b86bedbb08f96 (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md, blob 8f1473d247a44a10ae075fb8e40a590245a5aeef (verified)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23;
           Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b97fb8152d2a5742e17fa172e12204756, verified);
           blob at the candidate 91bde236465178f20c7348280e036d2884dfc216 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml, verified)
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml, verified)
    PRIOR REVIEWS (HYPOTHESIS ONLY): MANUAL-REVIEW-SSDS-8.0-1FFBBF0-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-53669A5-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-D837363-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-CC005DB-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-C6DA678-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-B595F2C-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-6FF4ED1-NO-PASS.md; WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
    REVIEW METHOD: entry through source/roles/software-design/SKILL.md at the public source (expanded entry contract and
           scientific checks read in dist/skills/software-design/SKILL.md); owners read there: architecture-and-design,
           abstraction-and-concretization, convergence-and-cycle-economy ("Active simplification trigger", "Review
           strategy after recurrence"), workflow-and-workplans (D1/D2 revision gates), evidence-evolution-and-dependencies
           (restoration), protocol-versioning-and-compatibility (PC-001), source/shared/fragments/scientific-checks.md
           (e=3, e=5); full read of the Manual from a git-archive snapshot of the candidate; word diff 1ffbbf0..86ab683 of
           the Manual, closure map and stakeholder record; clause comparison against workplan §6.6 ACC, §12.4 and §21;
           constructed trajectories in the permissive and restrictive directions; G1 document checks executed
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session

Governing SSDP version for this Review: 7.2.1. The Manual's refinement table, decision markers, §30 pass and qualification claims, the closure map, commit messages, the handoff's scope text, workplan §0.1/§27 rationale, the diagnostic model's reported results and every prior Review record were treated as hypotheses. Section numbers refer to the Manual at the candidate unless prefixed "workplan". Scratch files were written under `$TMPDIR/ssds80-manual-review-86ab683/`, because the sandbox does not permit `/tmp/ssds80-manual-review-86ab683/`.

## SERIOUS CHALLENGE

**None.** No accepted governing authority was found false, contradictory, ambiguous, inadequate or unrealizable.

- The scientific-checks revising duty (e=5), the workflow owner's D1/D2 revision-gate rule and P5 are coherent and realizable here.
- SD-18 and SD-19 are realizable as directed. B1 is a gap in how the Manual realizes SD-19's "exactly `(s, r)`" against e=5, which names a predecessor; the Manual can close it by narrowing which record counts, without contradicting the direction.

## Verdict

**NO-PASS.** One blocker survives, in the D1-D3 change rule (the seventh successive finding in that family).

- **B1.** SD-19 is realized as "a revision-assessment record for `(s, r)` is admitted". The record is matched on the subject and the revision's content identity alone. Its recorded predecessor is never compared with the predecessor §10.2 defines, and its standing is never read. A revision whose bytes recur after `s`'s accepted revision has moved on therefore reuses assessments made against another predecessor and an earlier tension set. Examples: a revert to an earlier assessed draft; a re-cutover after a version rollback. The same holds for a record whose assessments were revoked, or one withheld by a loss boundary. The gate is then shown a wrong predecessor and no applicability assessment of tensions bound to the real predecessor's accepted concretizations.

This is a local defect in the new key rather than another producing-route recurrence. The 1ffbbf0 B2 routes (frame, prospective, merged, slotless) are closed.

These held:
- The matching clause after SD-18. Unobserved external reads fail closed per runner class, and a free seed is a recorded attribute that `ext` compares while (2) and (4) range over every seed. The 1ffbbf0 B1 trajectories now fail as that Review required. The tenth-finding family has no surviving blocker. Its residuals are disclosure gaps (N2, N3).
- Every earlier closure re-checked in §5.

This verdict accepts nothing and authorizes no D4.

## 1. Blockers by earliest owner

### B1 — The revision-assessment record is matched on `(s, r)` and admission alone; a record made against another predecessor, revoked, or withheld by a loss boundary satisfies the SD-19 condition (§10.2, §8.3 step 7, §13.5 `revision_assessments`, §16.6 section 3, §29.4; SD-19; entered with the 1ffbbf0 N3 repair)

**Mechanism.**
- §10.2 defines the record: "an admitted `TASK_RESULT` whose `revision_assessments` slot is complete (`slots_filled`, §14.3) and names exactly subject `s` and revision `r`: the result of an `AUTHOR` task whose candidate yields `r`, or of a task answering `REVIEW(s, r)`". It defines the predecessor separately: "Its **predecessor identity** is `s`'s last accepted revision in its current tenure; for a tenure the frame starts …, the last accepted revisions of the subjects whose regions it received; otherwise none."
- §13.5: the slot holds "the subject and revision assessed `(s, r)`; the predecessor identity (§10.2); per found tension …". The predecessor is a value written when the record is made.
- §8.3 step 7 refuses a passing `ACCEPTANCE` or `GATE_DECISION ACCEPT` "unless a revision-assessment record for `(s, r)` (§10.2) is already admitted". `ACCEPT` and `GATE` readiness read the same condition. `REVIEW(s, r)` is derived only "with no revision-assessment record for `(s, r)`".
- Nothing compares the recorded predecessor with the one §10.2 defines at the acceptance. "Admitted" reads neither `status1` nor `cont`. A `TASK_RESULT` is never superseded (§8.3 step 7), but it can be revoked by an upheld challenge, and a loss boundary withholds it (§23.6: "task results … are not current until requalified or held").
- §16.6 section 3 renders "from the revision-assessment record for exactly that revision (§10.2), the predecessor identity and the tension applicability assessments".
- `rev` is a content hash (§1.5), so the same `(s, r)` recurs whenever the same bytes recur.

**Trajectory T1 — a revert to an assessed draft (D2; every step locally conforming).**
1. D2 subject `s` is accepted at `r0` with its gate, in tenure `τ`.
2. `AUTHOR` item `I1` yields a candidate with `s` at `r1`. Its admitted `TASK_RESULT` carries `revision_assessments` for `(s, r1)`, predecessor `r0`, and no tension found. Review returns `NO_PASS`, or the principal amends the plan to another approach, so `I1`'s candidate never integrates. Its record stays admitted.
3. `AUTHOR` item `I2` yields `r2` with its own record (predecessor `r0`). `r2` is integrated and accepted with its gate, and a D4 item concretizes it as `impl`.
4. Evidence on `impl` exposes a tension `t`. It is persisted in an in-repository `EVIDENCE_RECORD` home that binds `s` and `impl` by `CHALLENGES` (§2.2, §1.11).
5. Judging `r2` wrong, a human pushes a commit that restores `s`'s text to exactly `I1`'s text. The push is absorbed, and `cur(s) = r1`.
6. `ACCEPT(s)` and `GATE(g)` at `r1` are derived. A record for `(s, r1)` exists (`I1`'s), so `REVIEW(s, r1)` is not derived, both obligations are ready, and step 7 refuses nothing.
7. Section 3 renders `I1`'s record: predecessor `r0`, no tension assessed. Section 1 may list `t` if a relying search found it, but no revision-scoped applicability assessment of `t` exists. The authenticated owner records an `UNQUALIFIED` `ACCEPT`, which is admissible because `t` is not unavailable, disputed or stale evidence (§16.6).

Result: the revision `r2 -> r1` is accepted. Its gate evidence names `r0` as predecessor and assesses no tension bound to the real predecessor's accepted concretization.

Restrictive check: re-acceptance of an *unchanged* revision (after `REVALIDATE`, or early cutoff) legitimately reuses its record. The defect is reuse across a *changed* predecessor, not reuse as such.

**Trajectory T2 — a re-cutover after version rollback (§19.7, §19.5).**
1. `s` is `NATIVE` at `r` with record `R`.
2. A rollback `MODE_TRANSITION` returns it to `LEGACY(p)` and ends the tenure. Under the legacy process, tensions are recorded against `s`.
3. After the repair, a cutover with the same bytes needs owner acceptance of the native revision `r` (condition 3).
4. Under the reading in which that acceptance is `NATIVE` (N1), it is admitted on `R`. `R` was made in an earlier tenure, with that tenure's predecessor and tension set. §10.2 defines the new tenure's predecessor as "none".

**Variants (same key; the record's standing is not read).**
- *Revoked record.* An upheld challenge against `R`'s assessments (an applicable tension marked inapplicable) revokes the `TASK_RESULT`. It is still "admitted", so it still satisfies step 7 and readiness, and section 3 renders the revoked assessments.
- *Pre-loss record.* After a `LEDGER_LOSS`, the requalifying `ACCEPTANCE` (§23.6) of an unchanged revision is admitted on a pre-boundary record that the boundary withholds. The lost interval may have held tension records that the record could not have seen. This variant is the weakest of the three. The requalification is itself the human act P5 requires, so it bears mainly on what section 3 presents as current.

**Violated text.**
- Scientific checks e=5: "When revising, renaming, splitting, merging or replacing D1/D2 authority, also search recorded tensions bound to its accepted concretizations. In the revision's own record and its gate evidence, record the predecessor identity and, per found tension, a revision-scoped applicability assessment".
- Workflow owner: "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments, including those marked inapplicable, with their asserters. Acceptance does not ratify an assessment the gate was not shown."
- SD-19 keeps "SD-16's duties, slot and gate display".
- Manual §10.2 against §16.6:
  - §10.2 defines the predecessor as the current last accepted revision (`r2` in T1);
  - §16.6 renders "the predecessor identity" from the record (`r0`).

  An implementer must choose between them, and neither choice gives the gate a correct predecessor with matching assessments.
- §29.4 claims **E0** "for presence and order", and §16.6 says "section 3 always has its record". Both are true by the letter and false for the duty e=5 states.
- For the pre-loss variant, §0.4 P5: "retained permissive effects do not pass without requalification or accountable attestation".

**Earliest owner.** Manual §10.2 (the definition of a counting record), §8.3 step 7 and §16.6. This is not a Serious Challenge: SD-19's "exactly `(s, r)`" stays satisfied when the Manual narrows which `(s, r)` record counts.

**Family-level assessment (convergence owner, "Active simplification trigger"; "Review strategy after recurrence").**
- This is the seventh successive finding in the D1-D3 change rule: `b595f2c` B3, `c6da678` B3, `cc005db` B1, `d837363` B3-B4, `53669a5` B2, `1ffbbf0` B2, and this one.
- The previous six shared one cause: the duty was attached to how a revision was produced. SD-19 removed that mechanism, and every producing route the earlier Reviews named is now closed (§5).
- This finding is in the new key. The key names the revision's *content identity*, which recurs, while the duty is relative to a *predecessor* and to the tensions recorded when the search ran.
- It is a clean local defect of SD-19's realization: one comparison is omitted. It is not a non-local recurrence, and the repair removes nothing and adds no latch.
- Options for the stakeholder:
  - **(a) Key on the predecessor and the record's standing (recommended).**
    - A record counts for an acceptance of `(s, σ, r)` only if:
      - its recorded predecessor equals the predecessor defined at that acceptance: the last revision of `s` *other than `r`* accepted in the tenure, or the source subjects for a tenure the frame starts;
      - it is not revoked or blocked;
      - `cont` holds for it.
    - Otherwise `REVIEW(s, r)` is derived afresh.
    - Machinery supplies the predecessor in the slot, rather than the asserter typing it (A6).
    - Re-acceptance of an unchanged revision keeps reusing its record.
  - **(b) Key on order.** A record counts only if it was admitted after the tenure start and after the latest acceptance of another revision of `s`. This is equivalent in effect for T1 and T2 and slightly simpler to check.
  - **(c) Accept the reuse as a disclosed residual.** This relaxes e=5 for recurring revisions, so it needs the stakeholder's explicit acceptance.
  - **(d) A different-family Review before the repair.**
- Open question for the owner, not part of the blocker: whether a tension recorded *after* the record, with no change of predecessor, should invalidate the record. e=5 ties the search to the revision, and section 1 already shows tensions a relying search finds.

**Required discriminator (real owners: Admission step 7, S3 readiness, Interface gate rendering).**
- T1. Expected:
  - `ACCEPT(s)` and `GATE(g)` at `r1` are not ready;
  - the owner's `ACCEPTANCE PASS` and `GATE_DECISION ACCEPT` are refused (`OBLIGATION_REVIEW_OPEN`);
  - `REVIEW(s, r1)` is derived, and its record names predecessor `r2` and assesses `t`;
  - section 3 renders `r2`.
- T2. Expected: the re-cutover acceptance waits for a record made for the new tenure.
- The revoked-record and pre-loss variants: the record does not count.
- Contrast: re-acceptance of an unchanged `r` after `REVALIDATE` reuses its record.
- An implementation that matches the record on `(s, r)` and admission only must fail.
- §31.5 has none of these cases, so a green §31.5 coexists with B1 (DS-001).

## 2. Non-blocking findings

- **N1 — The cutover owner acceptance is unbound under SD-19 (§19.5 condition 3, §8.3 step 7 "a `NATIVE` D1/D2 triple", §10.2 `REVIEW(s, r)` derived "in a frame `G`", §31.5 "a cutover's owner acceptance (§19.5) behaves the same").**
  - Before the `MODE_TRANSITION`, `s` is `LEGACY(p)`. An acceptance recorded then is not refused, because the triple is not `NATIVE`. It is also outside the native tenure's `ACC`, because `τ(s)` starts at the transition.
  - If the acceptance rides in the cutover admission, it is `NATIVE` after the request's changes. But a `MODE_TRANSITION` is not a transformation, so no frame derives `REVIEW(s, r)` for it, and the cutover can proceed only when an `AUTHOR` task yielded exactly `r`.
  - Neither reading lets an unassessed acceptance count in the native tenure, so there is no permissive escape. But §31.5's expected behavior matches neither reading, and §19.5 does not say when, or in which tenure, condition 3's acceptance is recorded. That gap is pre-existing, from workplan §12.4.
  - Repair: state the binding. For example, the acceptance is recorded in the cutover admission, with `REVIEW(s, r)` derived for the prospective native tenure. Then align §31.5. T2 of B1 depends on this.
- **N2 — Randomness the runner does not supply; stale ensemble sentence (§6.3, §17.5, §6.10, §32.2, §31.3).**
  - §17.5 says "every class records a seed or replicate identity an execution draws", and §6.3 fails closed only for "a seed it drew" that is not recorded.
  - A runner cannot record a seed the code draws itself (an unseeded generator fed by `getrandom` or the clock), and scheduling nondeterminism has no seed at all. These are not file or network reads, so read observation does not catch them, and `ext` holds vacuously.
  - Such a failure is caught only when a differing run on the same content is observed: (2) "nondeterministic in fact". An embedded-oracle flaky test whose reproduction happens to fail and whose post-edit rerun happens to pass becomes stale.
  - This is the reviewed contract's own residual, not a new escape. But the Manual's text claims the seed is always recorded, and §32.2 names only "an execution attribute no runner class records".
  - Repair:
    - state that randomness not supplied by the runner is unrecorded variation, caught only by (2) in fact, and add it to §32.2 and §32.3;
    - optionally let a specification declare itself stochastic, so that a runner-supplied seed is required and anything else fails closed.
  - §31.3 "Ensembles: … without a fixed seed policy no mechanical stop occurs" is now stale. Under §6.10 a recorded, replayable free seed enables (1) and (3) "as a fixed seed policy would".
- **N3 — Whether an execution is unpinnable is not stated to be fixed in the record (§6.3 "is treated as having an unpinnable read"; §17.5 "A realization that does not record a declared attribute is treated as …").**
  - If "declared" is read under the current policy, a later `RULESET_ADOPTION` changes old observations' permissive standing:
    - removing an attribute from a class's declared set makes old realizations that lacked it permissively usable;
    - adding one excludes them.
  - Permissive matching would then depend on a ledger input adopted later, which the R1 guard rules out only for `on⁻`.
  - Repair:
    - state that the realization records its class's read-observation flag and declared set, or the resulting unpinnable mark, by value, so that `ext` reads the record only;
    - have §17.5's declared-set change also show the failures it makes newly matchable.
- **N4 — Residue of 1ffbbf0 N1 (§1.9, §1.3, §2.6).** The repair refuses newly declared `symbol`, `heading` and `anchor` terms that resolve to nothing. Still open:
  - a `path` or `{ file }` term naming a missing file (a typo) is not refused;
  - a term that later comes to resolve to `ABSENT` raises no finding. Only malformed anchors do (§1.3).
  - Analyzer completeness can still be supplied over the emptied unit (§2.6). Sketch:
    1. `kern.solve` is a `symbol` term. A rename `solve -> solve_v2` makes it `ABSENT`, and the code now lies in `kern.~`.
    2. A human `COMPLETENESS(EXEC)` on `{S}` stays current, because its basis is content on `S` only. The analyzer supplies completeness over `{kern.solve}`.
    3. The next realization records `S` and the empty unit only, so later edits of `solve_v2` leave its passing evidence current.

    This also needs a semantically stale completeness judgment, which is challengeable, so it is non-blocking.
  - Repair:
    - never let analyzer completeness cover a unit with an `ABSENT` term;
    - raise an S3 finding when a declared term comes to resolve to `ABSENT`;
    - extend the declaration check to `path` and `file` terms.
- **N5 — Residue of 1ffbbf0 N4 (§18.4).** "for a quarantined structural delta, the files its declared terms resolve to before and after the delta" is undefined for the `("governed", "ignore")` key, which has no terms. Say: the paths whose governed status the delta changes.
- **N6 — Cardinality and selection (§10.2, §13.5, §16.6, §29.4).**
  - The slot and section 3 are singular: "the subject and revision assessed `(s, r)`" and "the predecessor identity". But one `AUTHOR` item may revise several D2 subjects, and a merge tenure has several predecessors ("the last accepted revisions of the subjects"). This is restrictive only, because the other subjects derive `REVIEW`. State one entry per subject and a predecessor set.
  - §16.6 does not say which record is rendered when several exist for `(s, r)`. That bears on B1.
  - §29.4's revising row omits the `NATIVE` qualifier that step 7 carries.
- **N7 — Closure map (aid only).**
  - Items 7, 10 and 27 and the stakeholder-list bullet "no D1/D2 revision, however produced and in whatever frame, can be gate-accepted or accepted until a revision-assessment record for exactly that revision is admitted" are true by the letter but rely on text affected by B1.
  - Item 13's cutover row relies on text affected by N1.
  - Item 11's §6.10 annotation omits the stale §31.3 sentence (N2).
  - Items 1 and 12 do not annotate the §1.9 and §18.4 repairs.

## 3. Closure audit (§21 items and §16.2 rows)

The closure map was used only to locate text, and its annotations were checked against the Manual.

**Not substantively resolved:**
- item 7: the revising-review obligation rule, keyed on a record whose predecessor and standing are not read (B1);
- item 10: the gate template meeting Channel C for a D1/D2 revision whose record is reused across a changed predecessor (B1);
- item 27: the §29.4 revising row's E0 claim (B1).

**Resolved with non-blocking defects:**
- items 1 and 2 (N4);
- items 4, 5 and 11 (N2, N3);
- item 12 (N5);
- item 13 (N1).

**Resolved:** items 3, 6, 8, 9 and 14-26. Each decision was located, and each is a decision rather than a route.
- Delegated D4 space is bounded: file-type table, diff implementation, parser libraries, mutation tool, index and journal engines, limit values, witness kinds.
- Nothing incidental is over-specified.
- Item 14's "monotonic write-ahead publication-attempt record" is resolved by its removal (R4), which is assessed in §4.

**§16.2:** §26.4 is unchanged since 53669a5. Every row of both workplan tables has a final disposition there, as do 1.6.0 §4 and §14, including every Deferred row:
- invariants 4, 9, 15, 17 and 26;
- surfaces §5, §6, §12 and §18.

None was found unresolved.

## 4. Refinements R1-R9

| # | Assessment |
|---|---|
| R1 | **Sound; SD-18 realizes the class it was missing.** Three cases were re-tested. (i) An execution of a class that does not declare complete observation of reads outside the tree is recorded as having an unpinnable read (§6.3, §17.5, §20.1). So (1) and (3) never hold for it, while its adverse uses are unchanged. (ii) A free seed is a recorded attribute, never configuration (§6.5, §17.2), so (1) and (3) need `a⁻`'s seed and (2) and (4) range over every seed (§6.10). (iii) A host file outside a recorded environment component is an external read (§20.1). `on⁻` is untouched, because SD-18 adds only `on⁺` conjuncts, so `on⁺ ⇒ on⁻` and the guard hold, and §5.6 monotonicity is unchanged. The disclosed residual is honest for undeclared attributes and for unobserving classes. It omits randomness the runner does not supply (N2), and it does not state that the unpinnable mark is fixed at realization (N3). |
| R2 | **Sound.** Unchanged; the clamp only lowers values. |
| R3 | **Sound.** Unchanged. |
| R4 | **Sound.** Unchanged. The §22.3 failure points and the VM-snapshot residual were re-read. |
| R5, R6, R7 | **Sound.** Unchanged. |
| R8 | **Sound.** Unchanged. A `TASK_RESULT` is not supersedable, which is relevant to B1's standing variant. |
| R9 | **Sound.** Unchanged. The intake target rule (targets, never timing) was re-read. |

SD-19 is a decision inside §21 items 7 and 10, not a §0.3 refinement; §0.3's narrative lists it. Its defect is B1.

## 5. Previous findings, Phase B closures and N1-N4

**1ffbbf0.**
- **B1** is closed.
  - Trajectory (i): an execution with no observed reads is unpinnable unless its class declares complete observation outside the tree. Under such a class the `M1`/`M2` reads are recorded and pinned, so the rerun under `M1` cannot serve (3).
  - Trajectory (ii): the seed-42 pass is of `conf(a⁻)` and `on⁻` `tree(a⁻)` with another outcome, so (2) fails, `undisputed = P`, and for a D1/D2 claim the floor fires.
  - Both are carried as §31.3 cases with negative discriminators.
  - Residuals are N2 and N3.
- **B2** is closed for every route it named:
  - T1: the prospective acceptance of `numerics.method` is refused until `REVIEW(numerics.method, r_A)`, derived in the adopting frame for the prospective tenure, is answered;
  - T2: the merged revision `r_m ≠ r_C` derives `REVIEW(s, r_m)` in the frame;
  - T3: an empty-slot `NO_PASS` and a slotless human `REVIEW` are not records, so the review stays unanswered.

  The new key's own defect is B1 here.
- **N1** is partly closed; the residue is N4 here.
- **N2** is closed by removal: the write set no longer triggers the review.
- **N3** is closed in form (the predecessor is defined), but the repair left the definition unconnected to the record (B1).
- **N4** is closed for unit-term deltas; the residue is N5 here.
- **N5** is closed by disclosure (§17.5).
- **N6** is closed (§20.1).
- **N7** is superseded by N7 here.

**53669a5.**
- **B1** is closed.
- **B2** is closed: the admitted-state route then, and the frame routes now through SD-19.
- **B3** is closed (targets, never timing).
- **N1**, **N3**, **N4**, **N7** and **N8** are closed.
- **N2** is superseded by SD-19.
- **N5** is closed, with residue N4 here.
- **N6** is closed, with residue N5 here.
- **N9** is superseded.

**d837363.**
- **B1**, **B2** and **B4** are closed.
- **B3** is closed by SD-19; B1 here lies in the same family.
- **N1-N6** are closed.
- **N7** is closed: the predecessor now has a place in the slot and in section 3.
- **N8** is superseded.

**cc005db.** **B1-B3** and **N1-N8** are closed. N2 is now explicit in §20.1.

**c6da678.** **B1-B3** and **N1-N12** are closed. The anchors were re-checked:
- `stands⁻` requires `¬superseded(d)`;
- `same` for `COMPLETENESS` compares member revisions;
- `REFUSED` is named in R9;
- the residual-part `cid` is defined in §6.3;
- `prefix = ""` is stated in §1.8;
- ref locality is in §13.2.

**b595f2c.** **B1-B4** and **N1-N8** are closed. The anchors were re-checked:
- §3.4 has a machinery producer for `COMPLETENESS`;
- §13.3 reads "whatever its kind";
- the `AUTHOR` scope no longer names "document units".

**6ff4ed1.** **B1-B4** and **N1-N12** are closed. The anchors were re-checked:
- `qualification` is in the `GATE_DECISION` schema;
- §8.3 step 5 reads "gains no new … and no existing one grows";
- §26.4 has rows for 1.6.0 §4 and §14;
- export is listed in §0.5.

The changed text touches none of these mechanisms.

**Phase B §3 closures.** §5.3-§6.10 restate workplan §6.6 and change it only in the restrictive direction. The two exceptions recorded at 1ffbbf0 are restored:
- "nondeterministic old-content observations defeat (2)" now holds across free seeds;
- "executed content includes runtime inputs/observed reads" now fails closed for unobserved inputs.

Randomness the runner does not supply remains caught only in fact (N2), as in the reviewed contract.

**Phase B N2 re-test.** The bounding completeness judgment was taken through `P`, blocked, revoked, superseded, loss-withheld, and non-current by a membership change. Against each:
- a differing old-content run on an alternate tree that differs only outside the recorded regions (including another span of a recorded file) stays in (2), with `a⁻`'s seed or with another seed, and whether or not either run is unpinnable;
- a yielding present-content run stays in (4).

Both hold because `on⁻` is unchanged and `ext` reads no completeness. The support-cycle clamp (R2) and the corrupt-prefix halt (R3) are unchanged and fail closed before any current assertion.

**Phase B N1, N3, N4.**
- N1 remains open and disclosed (§32.2, §32.4).
- The N3 limits are carried in §31.3.
- The N4 costs are in §32.3, with a new trigger for unobserving classes.

**Both directions.**
- Permissive: B1 (a reused record); N2 (unsupplied randomness, as in the reviewed contract); N3 (a later policy change); N4 (empty units).
- Restrictive:
  - unobserving classes send red-then-green iterations to the owner and block the lineage's integration until disposition (disclosed, §17.5, §32.2-§32.3);
  - a fix that stops the code drawing a seed makes the old failure unmatchable (fail closed, acceptable);
  - a declared-set change makes failures unmatchable (disclosed);
  - every nested-only and re-identified D1/D2 revision needs a revising review (closure map list);
  - N1 (cutover).
- The previous round's non-blocking repairs were attacked in both directions: N1 is partial (N4); N3 contributes to B1; N4 is partial (N5); N5 and N6 held.

## 6. Out-of-matrix trajectories attempted

**Broke the candidate:**
- B1: a revert to an assessed, never-accepted draft after another revision was accepted; a re-cutover after version rollback; a revoked revision-assessment record; a pre-loss record used for requalification.
- N4: a symbol renamed out from under its unit with analyzer completeness over the empty unit; a `path` typo.
- N3: a declared-set change by `RULESET_ADOPTION`, under a current-policy reading.
- N1: the cutover acceptance under both binding readings.

**Held:**
- **SD-18:**
  - unobserved mesh under an unobserving class (bounded and `UNBOUNDED`);
  - the same under an observing class (pins recorded; `M1` cannot serve (3));
  - a host-mounted file under an image-only class (external read);
  - a missing declared attribute (fails closed);
  - seed 17 against seed 42 in both orders, and same-seed red-then-green;
  - a non-replayable seed (owner);
  - code that stops drawing a seed after a fix (unmatchable, fail closed);
  - an unobserving class's runs keep their adverse uses in (2), (4) and `adm`;
  - the class rule's candidate-own test never lowers the class under an unobserving class;
  - the guard: no SD-18 change reaches `on⁻`.
- **SD-19:**
  - human-pushed and absorbed D2 revisions;
  - direct human `ACCEPTANCE PASS` and `GATE_DECISION ACCEPT` before the record (refused), and an adverse decision (admitted);
  - an adopted promotion's prospective acceptance;
  - a clean merge of an `AUTHOR` candidate with a human edit;
  - an empty-slot `NO_PASS`;
  - a slotless human `REVIEW`;
  - a nested-D4-only revision of a D2 composite;
  - a §27.3 re-identification;
  - re-acceptance of an unchanged revision after `REVALIDATE` (reuse is legitimate);
  - an `AUTHOR` result whose slot is `INCOMPLETE` (not a record, so `REVIEW(s, r)` is derived).
- **Derivation:** the new readiness conditions and the step-7 refusal read S0 record existence only. S2 is unchanged; the stratification check is unaffected; S2 has one least fixed point.
- **§1.9 repair:** misspelled `symbol`, `heading` and `anchor` terms are refused when authored or adopted; a function deleted later stays well formed (no 53669a5 N5 regression).
- **§18.4 repair:** `QUARANTINE` of a unit-term delta names the before and after files.
- **Publication, currentness, gates and floors** (§22-§23, §10.5, §15.4 and §16.6 re-read, unchanged):
  - two processes sharing one host key;
  - a crash after a successful compare-and-swap;
  - a paused publisher against a landed or a pending fence;
  - a risk override never covers `GATE`;
  - an unqualified `ACCEPT` is refused while disputed evidence is listed;
  - floor items cannot be reclassified.
- **Partition and scope identity:** static sibling nesting is rejected; crossed anchors resolve to `ABSENT`; byte-preserving refinement keeps `scope_id`, `rev` and tenure.

## 7. Minimum architecture and capability transfer

**Changes since 1ffbbf0.**
- No component, tier or record kind is added.
- SD-19 removed:
  - the producing-admission classification;
  - the `AUTHOR` exemption;
  - the "current revision" restriction.
- SD-18 adds a read-observation field to an existing runner-class designation and moves the free seed from configuration to attributes.
- §30's statements are accurate, except that "one admissibility condition keyed on the acceptance target" inherits B1.
- B1 option (a) adds one comparison and removes nothing.

**Capability transfer.**
- PC-001 (`AUTHORITY_BOUND`) was independently resolved at the public source ("When a new profile becomes current, every older supported profile remains frozen and independently testable.") and is preserved:
  - Core imports nothing from SSDS (§26.2);
  - §31.8 tests Core without SSDS;
  - the frozen 1.6.0 file, `source/` and `dist/` are byte-unchanged.
- The 1.6.0 transfer in §26.4 is complete.
- The Phase B capabilities narrowed at 1ffbbf0 are restored (§5).
- The e=5 predecessor capability is not fully transferred (B1).

**PEM basis.**
- `origin/main` is `af0455753e20ee54a969c844872e29e270007211`. The PEM blob `1561797125622f355f84eb27319f87e8fa4227d9` is identical at the candidate and on `origin/main`.
- `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run in the checkout, reports "PEM schema 1 valid: 5 families, 0 notices".
- HAS dispositions:
  - PC-001: applicable and binding;
  - DS-001: applicable as evidence only; it bears on §8;
  - SP-001, SP-002 and FF-001: applicable as evidence only.

## 8. Qualification design

§31 binds claims to real owners and marks every runtime group UNEXECUTED; nothing beyond §31.10 is claimed as executed.

**Adequate for what they target:**
- the new §31.3 cases (unobserved external inputs; free seed);
- the expanded §31.5 SD-19 case (adopted promotion, merged revision, answers without the slot, nested revision).

**Green fixtures can coexist with these defects (DS-001):**
- B1: no revert or recurrence after a changed predecessor; no re-cutover; no revoked or pre-loss record;
- N2: no unsupplied-randomness case;
- N3: no declared-set change by policy adoption;
- N1: the cutover expectation in §31.5 matches neither binding reading.

§31.3's "Ensembles" sentence is stale (N2). The discriminators in §1 are required. The §14.7 `HARD` qualification design is adequate as design, with proposed-default values. The diagnostic model was not run: it is unchanged since Phase B and models no attributes, seeds, runner classes or revision gates.

## 9. Doctrine-realization map and O1

The E0/E1 claims are tied to existing mechanisms, with one exception: §29.4's revising row claims E0 "for presence and order" and that "the gate core renders the record". That holds only for the record's existence. The predecessor identity and the tension set it renders can belong to another revision history (B1).

The §29.5 documentation row is accurate by the letter, with the same qualification. The enumeration is complete with its catch-all row, and the disclosed-E3 list (§29.6) is appropriately conservative.

O1 (§0.5) is unchanged: realized record, readers, routine questions, realized-record architecture and marked surfaces. "Beyond the requested deliverable: None" is consistent with the stakeholder record. Technical Review accepts no marked item, product scope or default value.

## 10. What was verified and how; what was not

**Executed** against a `git archive` snapshot of the candidate under `$TMPDIR/ssds80-manual-review-86ab683/`, and against the repository:
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` (in the snapshot): 4 tests, OK.
- `git diff --check 1ffbbf0a918d514694ba1768d0a6d8a8fa579696 86ab683cb1b16fd818b84805636d66b215131be3`: clean.
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 86ab683cb1b16fd818b84805636d66b215131be3`: 21 files, all within the expected set:
  - the Manual and the closure map;
  - seven Manual review handoffs and seven NO-PASS records;
  - the Phase C handoff and the Phase C continuation handoff;
  - the session handoff;
  - the stakeholder record;
  - two index lines.

  The 1ffbbf0..86ab683 diff touches the Manual, the closure map, the 1ffbbf0 handoff and record, and the stakeholder record (SD-18, SD-19).
- `orchestrator/docs/architecture.md` (blob `39e6de7…`), `source/` (tree `fac2238…`) and `dist/` (tree `6bf729e…`) are identical at `fad3ee4…` and at the candidate.
- All header blobs match.
- PEM was validated as in §7. The validator cannot run with `python3 -I` from the snapshot, because its sibling-module import fails; it was run in the checkout, whose PEM blob is identical.

**Read** at the public source: the owners listed in the header, with the exact text quoted in §1 and §7.

**Not verified:**
- any runtime behavior (none exists); the trajectories are deductions from the specified contracts;
- the diagnostic model (not run);
- empirical costs, such as how often D1/D2 revisions recur byte-identically after another acceptance, how often runner classes lack read observation, and how often code draws its own randomness;
- workplan §18 and §27 beyond targeted reads; the earlier workplan NO-PASS records beyond Phase B Review §3;
- the full text of the prior Manual Reviews other than 1ffbbf0 (their finding lists were re-derived against the candidate text);
- D1, D2, D4 and specialist entrypoint texts beyond the software-design entrypoint and the scientific-checks fragment;
- the testing, storage, concurrency, security and inspectability owners, which were not loaded because no finding turned on them.

## 11. Scientific-checks answers

- **Material findings:** B1 and N1-N7 above. No agents were launched. The only tools run were git, the unit test and the PEM validator, and they produced no further findings. No material scientific finding about any project's science was made; this Review concerns D3 authority for software that mediates scientific evidence.
- **Realized results:** this Review produced, ran and reviewed no realized scientific results, including through the tools it ran, and it prepared no gate evidence. Its output is D3 review evidence toward G1. The unit test, `git diff --check` and the PEM validator are structural software checks, not realized results, so no null envelope is owed. For transparency, the review coverage and its limits are stated in §10.
- **Variants:** no analysis, pipeline, preprocessing, model or parameter variant was evaluated or selected (count 0).
  - Constructed trajectories are review hypotheses.
  - Two clauses were compared under two readings each, as interpretation, with textual coherence against the rest of the Manual as the criterion:
    - the binding of the cutover owner acceptance (pre-transition, or inside the cutover admission), which gave N1;
    - whether "treated as having an unpinnable read" is fixed in the record or read under current policy, which gave N3.
  - B1's options (a)-(d) are proposals for the stakeholder, not a selected survivor.
  - There was no delegated or resumed work.
- **Tension search:** not triggered.
  - No consequential judgment relied on accepted project D1/D2 authority. The authorities used are SSDP 7.2.1 process owners, the stakeholder record and the reviewed workplan, a D3 cycle contract.
  - The D2 subjects in the trajectories are hypothetical constructs, not accepted authority of any project.

No part of these answers is left unanswered; the coverage limits are those stated in §10.

## 12. Common-mode note

This reviewer shares the Manual author's model family (Claude). It was launched by the authoring session from the issued handoff, and it shares the corpus, the inherited workplan framing and the toolchain. Fresh context is not epistemic independence. All eight Manual reviewers have been of this family; the Phase B reviewer was of the GPT family.

B1 is the seventh successive finding in the D1-D3 change rule. Its pattern differs from the earlier ones: it is a defect in the new key, not another producing route. That makes option (a) a plausible clean local repair. A different-family Review (option (d)) remains material, because same-family Reviews have now passed over this key's predecessor coordinate for two rounds: at 1ffbbf0, N3 asked only that the predecessor be defined.

## 13. D4 statement

No D4 is authorized. This NO-PASS accepts no architecture, product scope or default value. A later PASS would be technical evidence for G1 only. G1 also needs explicit stakeholder acceptance, and shadow D4 needs G2.
