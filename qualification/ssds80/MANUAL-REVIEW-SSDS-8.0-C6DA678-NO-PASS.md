# SSDS 8 Architecture Manual — Independent D3 Review, candidate c6da678

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout /home/user/scientific-software-development-system)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: c6da6789695fa4f8b39cd1a3edb93d86fba151fc
    SCOPE: the whole proposed Manual as durable D3 owner: (a) §21 and §16.2 closure; (b) fidelity to the
           Phase B-reviewed workplan, including refinements R1-R9; (c) out-of-matrix adequacy; (d) inheritance
           and capability transfer (Architecture 1.6.0, workplan §18, PEM HAS); (e) qualification design;
           (f) doctrine-realization map; (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob 25beaad472a93f388daee4f86f94b4eee7a9044d (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md, blob 625d1f606cb7a6f6de115d4aee363b7b22be557f (verified)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23;
           Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b97fb8152d2a5742e17fa172e12204756, verified);
           blob at the candidate 91bde236465178f20c7348280e036d2884dfc216 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml)
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS (HYPOTHESIS ONLY): MANUAL-REVIEW-SSDS-8.0-B595F2C-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-6FF4ED1-NO-PASS.md;
           WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
    REVIEW METHOD: entry through source/roles/software-design/SKILL.md at the public source; owner reconstruction
           (architecture-and-design, abstraction-and-concretization, convergence, evidence, workflow, versioning,
           scientific-checks fragment); full read of the Manual at a git-archive snapshot; independent §21/§16.2 audit;
           clause comparison of Manual §0.3, §4-§6, §8.3, §10-§14 and §17 with workplan §6.6, §7 and §9.6; diff
           review b595f2c..c6da678; constructed trajectories in the permissive and restrictive directions; G1 document
           checks executed
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session

The Manual's refinement table, decision markers, §30 pass and qualification claims, the closure map, commit messages, the handoff's scope text, workplan §0.1/§27 rationale, the diagnostic model's results, the stakeholder record's characterization of SD-11 options and every prior Review record were treated as hypotheses. Section numbers refer to the Manual at the candidate unless prefixed "workplan".

## SERIOUS CHALLENGE

**None.** No accepted governing authority was found false, contradictory, ambiguous, inadequate or unrealizable. The 7.2.1 evidence owner ("A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority."; "When competent evidence assessments materially conflict, preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence."), the workflow owner ("it cannot erase unresolved contradictory material evidence by vote"; "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments"), the scientific-checks e=5 revising duty and the D3 owner's "one authoritative representation/state" are coherent and realizable here. Part of B1 is inherited from the reviewed workplan's unpinnable-read clause; the workplan is the cycle contract, not accepted authority, and the Manual's own R1 polarity split is the right place to repair it. Every blocker is repairable at Manual sections without changing a parent.

## Verdict

**NO-PASS.** Three blockers survive. B1 is in the assessment-disagreement matching clause, the sixth successive finding there: external inputs enter the adverse predicate with the permissive polarity, so a failure caused by an unfixed external input can become stale on a run that never used that input. The SD-11 recording itself held under every attack below. B2 is a clean local defect in the R9 repair: the veto's sameness test for reviews keys on the contract item revision, which a principal's control-tightening amendment changes without changing what is asked, so an adverse review can be outvoted by re-dispatch. B3 is an incomplete repair of the previous B3: D1-D3 semantic and structural declarations live in the manifest unit, so a non-`AUTHOR` item can revise D1/D2 authority without the revising duties. This verdict accepts nothing and authorizes no D4.

## 1. Blockers by earliest owner

### B1 — External inputs narrow the adverse predicate; a failure caused by an unfixed external input is made stale on non-discriminating evidence (§6.5, §6.3, §6.6, §6.8; refinement R1)

**Change.** The reviewed contract (workplan §6.6) says: "`on(o, K)` holds when content `K` (a tree, or a frame's content) has, on every unit and widened scope of execution `o`'s recorded execution basis, the content identity and membership `o` recorded." It compares tree-resident content only. The candidate's `on⁻` adds "∧ where K = K(x): every locator that o and x both record has the same pin", and states "Pins are compared only between observations; a frame's content fixes no input outside the tree, so a pin entry restricts no comparison with a frame". It also keeps, inside `on⁻`, the inherited rule "An observation with an unpinnable read satisfies neither predicate for any K except its own execution." So an external input is treated as **content** where observations are compared ((1), (2)) and as **free variation** where an observation is compared with a frame ((3), (4), `adm`). The mixture is the defect. R1's stated property, "never removes an adverse recorded match", is false for both conjuncts. §31.3 "External pins" encodes the permissive behavior as expected: "a differing outcome between them leaves (2) intact". SD-11 chose "one recorded execution basis at the reviewed granularity"; the pin conjunct goes beyond that text, because pins are not part of the reviewed `on`.

**Trajectory (every step locally conforming; D4 claim, so no floor).**
1. Specification `S` (declarative oracle) reads a dataset through locator `L`; its `fixed` table does not fix `L`, so it is free (§17.1). The runner pins each read by digest (§20.1). Claim `c` is evidenced by `S`. The code's result depends on the dataset version.
2. At admitted tree `T0` realization `p` reads `L` at pin `P1` and passes; it is assessed `PASS`.
3. `L` now serves `P2`. A run on `T0` (any admitted-state rerun) reads `P2` and fails `l2_error`; it is assessed `a⁻` and counts in the admitted state. §6.9 schedules a reproduction `r` on `tree(a⁻)`; it reads `P2` and fails identically.
4. An `IMPLEMENT` item refactors `solve` (a recorded region changes) and integrates as `T1`. Its affected-evidence rerun `q` reads `L` on a runner whose cache still holds `P1` (or a mirror serves `P1`) and passes.
5. `stale_{T1}(a⁻)`: (1) `r` has `on⁺(r, K(real(a⁻)))` (same terms, same pin) and the identical outcome. (2) `p` matches `T0` on every recorded term but its pin `P1 ≠ P2`, so it is excluded; `r` and `real(a⁻)` agree. (3) `q` stands with `on⁺(q, T1)` (pins ignored against a frame). (4) only `q` is `on⁻` `T1`, and it passes. So `a⁻` is stale, `undisputed = T`, `ev = T`, `c` is valid and no adjudication obligation is derived. `r`'s own failing assessment, if assessed, is stale by the same argument. `T1` was never observed under `P2`.
6. Under the reviewed formula `p` is on `tree(a⁻)` with another outcome, so (2) fails, the failure goes to the owner and keeps counting. For a D1/D2 claim whose failure is a frame failure (`adm` false), the floor clause "(2) has failed" is likewise lost.

**Inherited sibling (restated in `on⁻`).** An unpinnable read (for example a network fetch on a cache miss) removes an observation from (2) and (4) and makes `adm(real(a⁻), T_b)` false. Consequences: a passing run on `tree(a⁻)` whose only difference is an unpinnable read never defeats (2); for a D1/D2 failure whose realization has an unpinnable read, `¬adm` holds, so a discriminating reading whose passing observation has `on⁺(p, T_b)` is admitted at R2 as "candidate-own" although the candidate changed nothing the failure read; the floor clause `adm` never fires. A yielding present-content run with an unpinnable read is excluded from (4); this is partly compensated when that run is itself assessed (its own failure is kept counting by (2)).

**Violated text.** Workplan §6.6 `on` (above) and its Phase B closure "nondeterministic old-content observations defeat (2)" (6FE1000 B2, 4EC0024 B′2), which no longer holds for external-input variation. Manual §6.2: "every execution attribute the specification leaves **free** | **execution variation**: admissible assessments differing only here conflict". Manual §6.6: "**Nondeterminism goes to the owner.**" Evidence owner: "preserve the disagreement and route adjudication ... or obtain discriminating evidence" (step 5's stop discriminates nothing about `P2`). Manual §0.4 S4.

**Earliest owner.** Manual §6.5 (`on⁻` definition) with §6.3 and the R1 row. The unpinnable clause is inherited from workplan §6.6 ("never `on` any other execution's ... (fail closed)"), whose stated intent was fail-closed for stops; applied to `on⁻` it fails open.

**Convergence assessment.** The matching clause has now produced findings in six successive reviews (`ef8445a` N2, `552ac01` N2, Phase B N2, `6ff4ed1` B1, `b595f2c` B1, this one). At family level each finding is one dimension of "the same content" handled with the wrong polarity in at least one consumer: completeness standing, effective structure, recording granularity, and now inputs outside the tree. The SD-11 core (one record, reviewed granularity, frozen resolution context, every consumer reading it) held under every attack in §6 of this record. The defect is confined to dimensions that are not tree-resident, and its immediate cause is a polarity judgment in the previous review's N4 ("restrictive only"), made by a reviewer of this reviewer's family. I classify it as a recurrence of the clause that is local in cause and has a strictly subtractive repair in `on⁻`. A family-level guard removes the class: state one construction rule, "`on⁻` compares only tree-resident recorded terms (unit, read and widened entries) under the frozen context; every other dimension (pins, unpinnable reads, completeness, same root tree) appears only in `on⁺`'s extra conjunct", and qualify each non-tree dimension in both predicates. No latch or exception is needed.

**Options for the stakeholder (Phase C handoff §5).** (a) **Subtractive (this review's recommendation):** drop the pin conjunct and the unpinnable exclusion from `on⁻`; `on⁺` additionally requires equal pins on shared locators and no unpinnable read on either side, and for (3) the observation's pins must equal `a⁻`'s, because a frame fixes none. `on⁺ ⇒ on⁻` still holds by construction. (b) Subtractive plus dropping narrow matching: `on⁺ := on⁻ ∧ same root tree ∧ equal pins ∧ no unpinnable read`, which also removes `bound`, the S2 read in `stale` and support-graph edge 4, at the cost of more reruns. (c) A different-family Review before the next repair: all three Manual reviews share the author's family, and this defect entered through a same-family review finding. (d) Reconsideration above §6.6: for example, failures whose execution read any external input stop only by judgment.

**Required discriminator.** The trajectory above at the real owners. Expected: `p` stays in (2), (2) fails, `undisputed = P`, the owner's adjudication obligation is derived, and for a D1/D2 claim the floor fires at the first position at which (2) fails. Variants: a passing run on `tree(a⁻)` differing only by an unpinnable read keeps (2) failing; a D1/D2 failure whose realization has an unpinnable read and whose candidate changed no recorded region is not candidate-own (R3). Contrast that must hold: a reproduction under a different pin does not satisfy (1). An implementation that compares pins in `on⁻`, or excludes unpinnable-read observations from (2), (4) or `adm`, must fail. The §31.3 "External pins" expectation for (2) must be inverted.

### B2 — The veto's sameness test for reviews keys on the item revision; a control-tightening amendment lets a fresh reviewer outvote a standing `NO_PASS` on identical content (§5.5 `same`, §10.3, §13.4; refinement R9; previous B4 partly reopened)

**Trajectory (every step locally conforming).**
1. Implementer task for item `i` at revision `i1` submits candidate `C`; transformation `X`. Conformance is `CLEAN`. Reviewer A, fresh and independent, records `REVIEW NO_PASS` on `X` with findings inside the item's scope. `REVIEW(X)` is answered and `REFUSED`; it is never dispatched again (§10.3).
2. The findings lie inside the item, so the next implementer iteration starts mechanically (§13.7). The principal, deciding the routed findings, makes an R1 control-tightening amendment of `i` (for example adds a `HARD` secondary check or lowers the budget). The plan acceptance stays current through `PLAN_CONTROL`; the item revision is now `i2`.
3. The implementer, disputing the findings, resubmits identical changed-unit content as a new candidate `C'` (a new commit, or the same changes on a moved base). `X' ≠ X`, so `REVIEW(X')` is a new obligation. Conformance under `i2` is `CLEAN`.
4. Reviewer B, fresh, records `PASS` on `X'`. Its basis names the item at `i2` (`EXACT`, §4.3). `same(A, B)` requires "the same contract item revision and the same candidate content"; the revisions differ, so B is not vetoed. `REVIEW(X')` is discharged, no `ADJUDICATE_DISAGREEMENT` is derived, and §11.5 integrates `C'`.

A and B judged identical code and contradict each other: a tightened item asks the same thing under stricter controls ("It claims only that the acceptance's conclusion about what is asked still applies under tighter controls"; obligation statements are unchanged), so a `PASS` under `i2` implies a `PASS` under `i1`. The same holds for `CONFORMANCE`. The re-review brief need not even show A's findings ("policy may supply the previous review's findings").

**Violated text.** R9's own property: "a review or acceptance disagreement is never resolved by re-dispatch, count or order". Workflow owner: "it cannot erase unresolved contradictory material evidence by vote." Convergence owner: "No recurrence count, review count, cycle budget, or convergence target can force acceptance". The b595f2c B4 discriminator ("A `NO_PASS` on `X` followed by an independent `PASS` on the same `X` does not integrate `X` without an adjudication") is satisfied only while the item revision is unchanged.

**Earliest owner.** Manual §5.5 `same` for `REVIEW` and `CONFORMANCE` of a transformation (R9). A clean local defect introduced by the repair.

**Minimum repair direction.** For `REVIEW` and `CONFORMANCE` of a transformation, `same(j⁻, z)` holds for the same item and the same changed-unit content whenever `z`'s item revision is reached from `j⁻`'s by the tightening order (`rev(j⁻) ⊑ rev(z)`). A simpler conservative alternative is the same item at any revision, with an R2 amendment routed to the owner's adjudication rather than to a fresh review.

**Required discriminator.** `NO_PASS` on `X` under `i1`; an R1 tightening to `i2`; a new candidate with identical changed-unit content; an independent `PASS`. Expected: the `PASS` is vetoed, `REVIEW(X')` is `REFUSED`, the owner's adjudication obligation is derived and nothing integrates. Same for `CONFORMANCE`. An implementation comparing item revisions by equality must fail. §31.5's R9 cases vary order but not the item revision, so they pass with the defect.

### B3 — D1-D3 semantic and structural declarations are written through the manifest unit; a non-`AUTHOR` item revises D1/D2 authority without the revising duties (§13.2 domain rule, §14.3/§14.5 write-scope mapping, §1.2, §1.5; previous B3 partly reopened)

**Trajectory.** An `IMPLEMENT` item for D4 work lists `ssds.manifest` in its write scope, as is ordinary when an implementer declares new D4 units (the manifest is kind `MANIFEST`, "content edits are ordinary", and is not a protected surface, §25.3). The implementer also edits the `[unit.semantic]` table of D2 unit `numerics.solver` in the manifest (removes a `CONSTRAINED_BY` relation, or changes `defines`). The domain rule passes: the write scope contains no D1-D3 unit. The `write_scope` template passes: it maps the diff by "changed byte ranges to owning units" (§14.5), and those bytes belong to `ssds.manifest`. Yet "The `[unit.semantic]` table is semantic content of that unit and is part of its revision" (§1.2, §1.5), so `rev(numerics.solver)` changes on integration. The D2 subject becomes invalid and `ACCEPT` (R3) is derived. The item kind is `IMPLEMENT`, so no `revision_assessments` slot, no tension-search injection and no `o1_content` slot exist, and the D2 gate's §16.6 section 3 renders nothing, with nothing marking it missing. The human accepts the revision without the assessments. The same route lets a non-`AUTHOR` item re-scope or re-member a D1-D3 subject through its structural keys (tenure ends; re-acceptance at R3 without revising duties). Conversely an `AUTHOR` item cannot edit its own unit's manifest declarations, because its write scope may contain "only units of that kind".

**Violated text.** Scientific checks e=5: "When revising, renaming, splitting, merging or replacing D1/D2 authority, also search recorded tensions bound to its accepted concretizations. In the revision's own record and its gate evidence, record the predecessor identity and, per found tension, a revision-scoped applicability assessment". Workflow owner: "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments". SD-4: deterministic verification of "any over-stepping of boundaries". Manual §29.4: "**E0** (only an `AUTHOR` item can change D1-D3 units, §13.2, so the slot is always triggered ...)", and §29.5's documentation E0 claim, both false on this route.

**Earliest owner.** Manual §13.2 domain rule with the §14.3/§14.5 write-set mapping and the §13.5/§16.3 `AUTHOR` triggers. A clean local defect: the previous repair keyed authority changes on the kind of the unit owning the changed bytes, while a unit's revision spans the manifest.

**Minimum repair direction.** Map a manifest diff to the units whose declaration keys or semantic tables it changes, and apply the write-scope check, the domain rule and the `AUTHOR` triggers to those units (one rule for write set and domain). Alternatively, allow semantic declarations of D1-D3 units only as inline markers and their structural keys only in `AUTHOR` items (with owner release where §8.3 step 4 requires it).

**Required discriminator.** An `IMPLEMENT` or `DOCUMENT` item with `ssds.manifest` in scope that edits a D2 unit's semantic table or scope is a `VIOLATION` (or rejected at lint or Admission). An `AUTHOR` item for that D2 unit can edit those declarations and its brief carries the revising and tension-search duties. An implementation mapping write sets by byte ownership alone must fail. §31.5 tests only `DOCUMENT` scopes containing D1-D3 units, so it passes with the defect.

## 2. Non-blocking findings

- **N1 — `stands⁻` ignores supersession of the disposing record (§5.5).** It requires only "`status1(d) = CLEAR ∧ cont(d)`". §6.7's standing for the same act requires "not superseded, not revoked or blocked". If the owner's adjudication `d1` is later superseded by `d2` and `d2` is revoked, §6.7 would revive the disagreement; `stands⁻` keeps `j⁻` disposed by the withdrawn `d1`. Permissive in a narrow chain; use `base(d)`-style standing.
- **N2 — R9 siblings.** `INTAKE_DISPOSITION` (`ABSORB` versus `REJECT`/`QUARANTINE` on one delta) has no adverse outcome in R9, and `INTAKE` is not an answered kind, so intake disagreement is resolved by order or re-dispatch (adoption still passes §8.3 step 4 and needs prospective acceptances for promotions). A `PRODUCT_SCOPE_ACCEPTANCE REJECTED` by the product-scope owner does not veto a `GATE_DECISION` naming the surface (§3.5), a different kind.
- **N3 — "Own author's reassessment" is unrealizable for agents.** An agent actor is `agent:<task id>/<attempt>` (§25.1), and a task ends with its one result (§8.3 step 7), so no agent judgment can ever be reassessed by its author. R8, R9, §10.3 and the closure map present the route as available. Restrictive only; say it is human-only or define it by lineage.
- **N4 — `same` for `COMPLETENESS` omits content (§5.5).** The target `(X, R, membership)` survives edits of `X`'s members, so an `INCOMPLETE` judgment on old content vetoes every later `COMPLETE` judgment on repaired content until owner adjudication. Restrictive; it contrasts with "A stale failing observation is not admissible evidence against current authority". Compare the members' revisions.
- **N5 — `REFUSED`.** It is a fourth discharge value against workplan §21 item 7 ("three-valued discharge") and §7.4, not named in the R9 row. It keys on the obligation's target while the veto keys on `same`, so the two can disagree (restrictive).
- **N6 — Frozen-analyzer re-resolution of host-dependent output (§5.9, §6.3).** An analyzer whose output depends on host inputs is "recorded as an `ANALYZER_OUTPUT` observation", but re-resolving a recorded term under an older analyzer set in a new `K` has no recorded output and no defined value. Require host-independent symbol resolution, or define per-polarity fail-closed values (`on⁻` true, `on⁺` and currency false).
- **N7 — Read-entry identity and classification (§6.3, §20.1).** "for every file the designated runner observed being read, `({ path = p }, cid)`, whether or not the file is governed" overlaps "A read outside the governed tree is recorded by content identity where it can be pinned". For untracked or ignored in-repository files (build products, caches) an implementer must choose between a read entry, a pin and unpinnable, and must choose whether `cid` is taken over the observed bytes or over `tree(o)`. Over observed bytes, every realization reading a generated file is never current and never on any tree. State that `cid` is over the realization's tree and that only reads outside the repository are pinned. Also state that "`Σ` at the realization" means `Σ_n ⊕ Δ_Σ(X)` for a frame realization.
- **N8 — Residual-part entries.** §1.5 defines `cid` per scope term; a residual entry "denotes the composite's resolved regions minus its members' resolved regions" but its content identity is not defined. Comparing the composite's own terms would be coarser and narrow `on⁻`. Define it as the `cid` of the denoted difference.
- **N9 — Empty prefix.** §1.8 calls `ssds.unclassified`'s scope "the only use of the empty prefix"; §6.3 uses `{ prefix = "" }` for whole-tree widened entries; §1.3 requires prefixes to end in `/`. Editorial.
- **N10 — Re-review continuity (inherited, workplan §9.6).** Any change to a changed unit makes a new target, so a standing `NO_PASS` lapses on any edit, and the next reviewer receives its findings only if policy supplies them. R9's "extends the reviewed assessment rule" overstates this: a failing assessment does not lapse on change (§6.1), an adverse judgment does. Consider supplying unresolved findings of earlier iterations by default.
- **N11 — `ref` resolution.** Lint requires a `ref` to resolve inside the item's part or the `Objective` part, but resolution itself is undefined. If resolution is document-global (first matching anchor), an edit outside the item could move it without changing the item's revision, and a failing lint makes only "changed items" non-issuable. Define resolution as scoped to the item's part (plus `Objective`).
- **N12 — Stale summary claims.** §30 "the §6 family is unchanged in mechanism" omits the pin conjunct and the obligation to keep every analyzer set a recorded basis names; the closure map's R1 annotation presents pins as the b595f2c N4 repair, and its R9 bullet relies on "its own author reassesses" (N3).

## 3. Closure audit (§21 items and §16.2 rows)

The closure map was used to locate text only; its annotations were checked against the Manual.

- **Not substantively resolved:** item 5 (`on`, B1); items 3 and 7 (the effect of adverse judgments and discharge, B2); items 23-24 (domain rule and write-scope enforcement keyed on byte ownership, B3); item 27 (the §29.4 and §29.5 E0 claims depend on B3).
- **Resolved with non-blocking defects:** item 4 (read-entry recording, N7, N8); items 5 and 19 (analyzer re-resolution, N6); item 7 (`REFUSED`, N5); item 8 (`ref` resolution, N11); item 12 (intake disagreement, N2).
- **Resolved:** items 1, 2, 6, 9, 10, 11, 13, 14 (with R4), 15-18, 20-22, 25 and 26. Each decision was located and is a decision, not a route. Delegated D4 space is bounded (merge diff implementation, parser libraries, mutation tool, storage engines, reason-code members, limit values), and nothing incidental is over-specified to a blocking degree.
- **§16.2:** every row of both workplan tables, including every Deferred row, has a final disposition in §26.4 (with §26.3 for invariant 4, §5, §6, §7, §9-§12 and §18). None found unresolved.

## 4. Refinements R1-R9

| # | Assessment |
|---|---|
| R1 | **Sound in its SD-11 core, unsound in its external-input conjuncts.** One record at unit/region granularity with a frozen `ignore` and analyzer context, read by currency (`execution` mode), (1)-(4), `adm` and the class rule, closes the previous B1 and keeps the 6ff4ed1 B1 closure. The pin conjunct and the retained unpinnable exclusion narrow `on⁻` below the reviewed `on`, and the stated property is false for them (B1). Needs different treatment. |
| R2 | **Sound.** Clamping every non-trivial SCC to `F` only lowers values; the veto is a constant inside `base`. |
| R3 | **Sound.** |
| R4 | **Sound** (re-checked at the level of the failure-point list: a restart, a second process on one key, copied operator state and a paused publisher all fence; the VM-snapshot residual is disclosed). |
| R5, R6, R7 | **Sound.** |
| R8 | **Sound** in removing peer supersession. "Own author's reassessment" is unrealizable for agents (N3; restrictive). |
| R9 | **Partly sound.** The per-task `TASK_RESULT` carrier, answered judgment obligations and the existence-keyed veto close the b595f2c B4 trajectory in both orders, and the veto keeps S2 monotone. `same` for reviews keys on the item revision (B2); `stands⁻` diverges from §6.7 standing (N1); sibling kinds are omitted (N2); the fourth discharge value is not surfaced (N5). |

## 5. Previous findings, Phase B closures and N1-N4

**b595f2c blockers.** B1 **closed for its trajectory and variants**: with symbol terms re-resolved under the frozen analyzer, `on⁻(p, K(real(a⁻)))` holds after a `helper`-only change, `p` stays in (2), and `adm(a⁻)` holds so the floor fires; the sibling-file and ignored-file variants leave no changed recorded term; prefix addition changes the prefix term's `cid`. One representation now serves every consumer. **The family is not closed** (B1 above). B2 **closed**: `ref` locality plus `EXACT` objective coverage (residue N11). B3 **partly closed**: `DOCUMENT` scopes exclude D1-D3 units, but the manifest route is open (B3 above). B4 **partly closed**: carrier, answering and veto exist; the item-revision escape remains (B2 above).

**b595f2c non-blocking.** N1 closed (machinery `COMPLETENESS` targets name the analyzer, `tgt` checks it is pinned; §3.4 producer column amended). N2 closed (host-dependent output recorded), with residue N6. N3 closed (§3.4, §27.1, §28). N4 "repaired" with the wrong polarity (B1). N5 closed. N6 closed (`TEST_INTEGRITY` keyed on scope content; `audit_conclusion` slot and `specialist` field; bidirectional slot carried on the reviewer's result), except the §29.4/§29.5 claims (B3). N7 updated, with residue N12. N8 closed.

**6ff4ed1 blockers.** B1 closed (frozen terms; `on⁺ := on⁻ ∧ …`). B2 closed (prose byte-identity in §13.4). B3 closed (analyzer set pinned by `ρ_n`; residue N6). B4 closed (obligation kinds, holder, minimum, injection).

**6ff4ed1 non-blocking.** N1, N2 (by R8), N3, N4, N5, N6, N8, N9, N10, N11 and N12 closed as checked against the text. N7 partly closed: rule 1 covers prefix-versus-span; the empty prefix is special-cased but conflicts with §6.3 (N9); `EVIDENCE_RECORD` is layer-free.

**Phase B §3 closures.** Clause comparison of §5.3-§6.10 with workplan §6.6 found S1 polarity, `cont`, `base`, `ev`, `undisputed`, `qual`, `about`/`starts`/`home`, Y1/Y2 coverage, the class rule's candidate-own exception, absorbed-reading exclusion, never-lost salvage, independence and unknown authorship, and retirement/split/retarget restated. **Exception:** "nondeterministic old-content observations defeat (2)" (6FE1000 B2, 4EC0024 B′2) fails for runs differing only in an unfixed external input or an unpinnable read (B1).

**Both directions.** Permissive: B1 hides a live failure; B2 outvotes an adverse review; N1 narrowly. Restrictive: N4 keeps a stale `INCOMPLETE` vetoing; N3 removes a promised exit; R1's pin conjunct makes (1) stricter (harmless). Overridden challenges, loss boundaries (adverse judgments keep their veto; dispositions withheld), absorbed readings and unauthorized supersessions held. Nothing else resurrected a settled failure or withdrew a stop without cause.

**Phase B N2 re-test.** For a bounding completeness judgment that becomes `P`, blocked, revoked, superseded, loss-withheld or vetoed by an `INCOMPLETE`, a differing old-content run on an alternate tree differing only outside the recorded regions (including another span of a recorded file) stays in (2), and a yielding present-content run stays in (4), because `on⁻` reads no S2 value, no current `Σ`, `ignore` or analyzer. That holds, except when the alternate run also differs in a pinned or unpinnable external input (B1). The support-cycle clamp (R2) and the corrupt-prefix halt (R3) are specified fail-closed. Phase B N1 remains open and disclosed (§32.2); N3 limits are carried in §31.3; N4 costs in §32.3, now including analyzer retention and veto stalls.

## 6. Out-of-matrix trajectories attempted

**Broke the candidate:** B1 (differing pins on one tree; unpinnable passing run in (2); unpinnable failure and the class rule; yielding unpinnable run in (4)); B2 (R1 tightening between contrary reviews of identical content); B3 (manifest semantic table and structural keys of a D2 unit from an `IMPLEMENT` item); N1 (superseded-then-revoked adjudication chain).

**Held:**
- **Derivation and stratification:** the veto reads S0/S1 only; analyzer adoption mid-dispute (adverse use unchanged, permissive use narrowed); the support graph with `execution` entries and `record` entries on bounding completeness.
- **Recording and matching (SD-11):** span sibling edit; another unit's file in a bounded closure; ignored tracked file under a widened directory; prefix gains a file; `ignore` adoption with an unchanged tree; byte-preserving refinement; a unit removed after realization (frozen terms still re-resolve); observed whole-file reads (consistent with the reviewed `on`, since the execution read the whole file).
- **Partition and scope:** foreign file under a prefix; crossed anchors; residual ownership.
- **Publication and currentness:** the R4 failure points; settlement before human decisions.
- **Roles, envelopes and R9:** `NO_PASS` then `PASS` and `PASS` then `NO_PASS` on identical content and item revision (vetoed, `REFUSED`, adjudication derived); peer `FAIL` superseding `PASS` (rejected); concurrent reviewers on one obligation; an unbound adverse judgment from another reviewer task (restrictive; routes to adjudication); an agent `FAIL` on a D1 acceptance (rejected at step 3, not salvaged); a reviewer result with an empty `bidirectional` slot (passing judgments refused); adverse judgments across a loss boundary.
- **Gates and floors:** a floor item cannot be reclassified; an unqualified gate `ACCEPT` refused while disputed evidence is listed.

## 7. Minimum architecture and capability transfer

No component, tier or record kind is added. R9 adds a rule (the veto), an obligation state (answered) and a discharge value (`REFUSED`), all derived; R1 adds a per-realization resolution context and an operational obligation to keep every analyzer set a recorded basis names (disclosed as a reopen trigger). Each is justified by a capability an owner requires, and no simpler equivalent was found, except that B1's repair makes `on⁻` simpler. The removals (R4, R5) drop no owner-required capability.

1.6.0 transfer is complete in §26.4. PC-001 (`AUTHORITY_BOUND`) was independently resolved at the public source ("When a new profile becomes current, every older supported profile remains frozen and independently testable.") and is preserved: Core imports nothing from SSDS (§26.2), §31.8 tests Core without SSDS, and the frozen 1.6.0 file, `source/` and `dist/` are byte-unchanged. PEM basis verified: `origin/main` = `af0455753e20ee54a969c844872e29e270007211`, PEM blob `1561797125622f355f84eb27319f87e8fa4227d9` identical at the candidate, schema 1 valid (5 families, 0 notices). HAS dispositions as inherited: PC-001 applicable and binding; DS-001, SP-001, SP-002 and FF-001 applicable as evidence only. DS-001 bears on §8.

## 8. Qualification design

§31 binds claims to real owners and marks every runtime group UNEXECUTED; nothing beyond §31.10 is claimed as executed. Green §31 fixtures can coexist with all three blockers (DS-001): §31.3 "External pins" asserts B1's behavior; §31.5's R9 cases never change the item revision (B2); §31.5 tests `DOCUMENT` scopes but not manifest declarations of D1-D3 units (B3). The three discriminators in §1 are required. The §14.7 `HARD` qualification design is adequate as design, with proposed-default values. The diagnostic model (blob `d063df91b7d00c7f8ed1deb2a9b52a39910fcf6d`, unchanged since Phase B) models neither pins nor judgment vetoes.

## 9. Doctrine-realization map and O1

E0/E1 claims are tied to existing mechanisms except §29.4 (revising D1/D2 "only an `AUTHOR` item can change D1-D3 units") and §29.5 (documentation "never self-approve semantic changes"), both false on the manifest route (B3). The bidirectional E2 claim now has a carrier and an admission check. The disclosed-E3 list (§29.6) is appropriately conservative; enumeration is complete with the catch-all row.

O1 (§0.5) states the realized record, readers, routine questions, realized-record architecture and marked surfaces, including the export and tool-independent ledger routes. "Beyond the requested deliverable: None" is consistent with SD-2. Technical Review accepts no marked item, product scope or default value.

## 10. What was verified and how; what was not

Executed against a `git archive` snapshot of the candidate under `/tmp/ssds80-manual-review-c6da678/cand`:
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- `git diff --check b595f2c… c6da678…`: clean.
- `git diff --stat fad3ee4… c6da678…`: the Manual, the closure map, the 6ff4ed1 and b595f2c handoffs and NO-PASS records, the Phase C handoff, a one-line session-handoff change, the stakeholder record (SD-11) and two index lines.
- `orchestrator/docs/architecture.md` (blob `39e6de7…`), `source/` (tree `fac2238…`) and `dist/` (tree `6bf729e…`) identical at `fad3ee4…` and the candidate.
- All header blobs match. PEM validator run in the working tree (PEM and validator identical to the candidate's): valid.
- Owners read at the public source: the D3 entrypoint; architecture-and-design; abstraction-and-concretization; convergence; evidence; workflow (review and gate rules); versioning (PC-001); the scientific-checks fragment.

Not verified: any runtime behavior (none exists). The trajectories are deductions from the specified contracts, not executed probes. The diagnostic model was not run. Empirical costs were not assessed. Workplan §27 history and the earlier workplan NO-PASS records were not read beyond the Phase B record's summaries.

## 11. Scientific-checks answers

- **Material findings:** B1-B3 and N1-N12 above. No agents were launched; tools were limited to git, the unit test and the PEM validator, which produced no further findings.
- **Realized results:** this review, including the tools it ran, produced, ran and reviewed no realized scientific results and prepared no gate evidence; its output is D3 review evidence toward G1. Null envelope, examined: the Manual in full; the b595f2c..c6da678 diff; the closure map; workplan §6.6, §7.1-§7.5, §7.8-§7.10, §9.6, §16.2 and §21; the b595f2c, 6ff4ed1 and Phase B Review records (Phase B §2-§4); the Phase C handoff; the stakeholder record; PEM identities; the governing owners listed in §10. Materially not examined: workplan §27 and other sections not listed, the earlier workplan NO-PASS records, the diagnostic model's source, D1/D2/D4 and specialist entrypoint texts beyond the Manual's citations, and any runtime system. Materiality basis: decision relevance to G1 closure and to the Manual's §0.4 invariants.
- **Variants:** none evaluated or selected. Constructed trajectories are review hypotheses, not analysis variants. There was no delegated or resumed work.
- **Tension search:** not triggered. No consequential judgment relied on accepted project D1/D2 authority; the authorities used are SSDP 7.2.1 process owners, the stakeholder record and the reviewed workplan.

## 12. Common-mode note

This reviewer shares the Manual author's model family (Claude), was launched by the authoring session from the issued handoff, and shares the corpus, the inherited workplan framing and the toolchain. Fresh context is not epistemic independence. Both previous Manual reviewers were of the same family; the Phase B reviewer was of the GPT family. B1's immediate cause is a polarity judgment in a same-family review finding (b595f2c N4), which makes the Phase C option of a different-family Review material.

## 13. D4 statement

No D4 is authorized. This NO-PASS accepts no architecture, product scope or default value. A later PASS would be technical evidence for G1 only; G1 also needs explicit stakeholder acceptance, and shadow D4 needs G2.
