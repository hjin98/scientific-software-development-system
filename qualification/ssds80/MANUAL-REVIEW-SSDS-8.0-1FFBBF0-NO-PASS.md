# SSDS 8 Architecture Manual — Independent D3 Review, candidate 1ffbbf0

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout /home/samjin/agent-skills/scientific-software-development-system)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 1ffbbf0a918d514694ba1768d0a6d8a8fa579696
    SCOPE: the whole proposed Manual as durable D3 owner: (a) §21 and §16.2 closure; (b) fidelity to the
           Phase B-reviewed workplan, including refinements R1-R9; (c) out-of-matrix adequacy; (d) inheritance
           and capability transfer (Architecture 1.6.0, workplan §18, PEM HAS); (e) qualification design;
           (f) doctrine-realization map; (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob 175d15e0c967a84af2cbb32c62f29afd252109fd (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md, blob 1e313c42328a2ef3dffc4e72803477dcf6ea1e9d (verified)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23;
           Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b97fb8152d2a5742e17fa172e12204756, verified);
           blob at the candidate 91bde236465178f20c7348280e036d2884dfc216 (verified; word diff against the Phase B blob
           shows Review/lifecycle coordination text only)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml)
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS (HYPOTHESIS ONLY): MANUAL-REVIEW-SSDS-8.0-53669A5-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-D837363-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-CC005DB-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-C6DA678-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-B595F2C-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-6FF4ED1-NO-PASS.md;
           WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
    REVIEW METHOD: entry through source/roles/software-design/SKILL.md at the public source (expanded entry contract and
           scientific checks read in dist/skills/software-design/SKILL.md); owners read there: architecture-and-design,
           abstraction-and-concretization, convergence-and-cycle-economy (active simplification; review strategy after
           recurrence), evidence-evolution-and-dependencies (applicability dimensions, attribution, assessment
           disagreement), workflow-and-workplans (D1/D2 revision gates), protocol-versioning-and-compatibility (PC-001),
           source/shared/fragments/scientific-checks.md (e=5); full read of the Manual from a git-archive snapshot of the
           candidate; word diff 53669a5..1ffbbf0 of the Manual and closure map; clause comparison of Manual §6 with
           workplan §6.6 and §21; constructed trajectories in the permissive and restrictive directions; G1 document
           checks executed
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session

Governing SSDP version for this Review: 7.2.1. The Manual's refinement table, decision markers, §30 pass and qualification claims, the closure map, commit messages, the handoff's scope text, workplan §0.1/§27 rationale, the diagnostic model's reported results and every prior Review record were treated as hypotheses. Section numbers refer to the Manual at the candidate unless prefixed "workplan". Scratch files were written under `$TMPDIR/ssds80-manual-review-1ffbbf0/`, because the sandbox does not permit `/tmp/ssds80-manual-review-1ffbbf0/`.

## SERIOUS CHALLENGE

**None.** No accepted governing authority was found false, contradictory, ambiguous, inadequate or unrealizable.

- The evidence owner, the workflow owner's D1/D2 revision-gate rule and scientific checks e=5 are coherent and realizable here.
- SD-16 and SD-17 are realizable as directed. B1 is a gap in realizing SD-17's class. B2 is a gap in realizing SD-16's "before its acceptance".
- B2 option (a) shows that SD-16 and the reviewed prospective-acceptance rule (workplan §6.9, Manual §7.6, §19.4) can hold together. Neither the stakeholder direction nor the reviewed contract is defective.

## Verdict

**NO-PASS.** Two blockers survive. Both are recurrences in the two families the handoff names.

- **B1 (matching clause; the tenth successive finding).** SD-17 states the construction rule over "every recorded execution attribute the specification leaves free". Two members of the class the rule itself defines ("whatever can distinguish two executions of one configuration and is not tree-resident recorded content") still escape:
  - **Unobserved external inputs.** An external input that the designated runner did not observe is recorded neither as a pin nor as an unpinnable read, so `ext` holds vacuously. No rule requires runners to observe reads. The fallback for incomplete reads reaches only the governed tree.
  - **The free seed.** It is placed in the configuration by definition ("seed and replicate identity are configuration"). Condition (2) therefore never sees another seed's run on the same content. This contradicts §6.2, §6.6 and §6.10 of the Manual, and workplan §21 item 11 ("edit-and-rerun is not a route to a pass").

  In both cases a live failure is made stale by non-discriminating evidence.
- **B2 (D1-D3 change rule; the sixth successive finding).** The revising review is derived from the admission that *produces* a revision, after the fact. Three routes defeat the 53669a5 B2 repair:
  - an acceptance made in a transformation's frame, which for a promotion must be bound to that admission (§7.6, §19.4);
  - a human change folded into an `AUTHOR` integration through a clean merge;
  - an obligation "answered" by an adverse empty-slot judgment or a slotless direct human judgment.

  In each, a D1/D2 revision is accepted, or reaches its gate, with no revising assessment of it. §29.4's E0 claim is false for these routes.

These held:
- SD-17's attribute class for recorded backend, precision, environment and hardware attributes, with one definition of configuration for attributes;
- the withdrawal of the SD-15 restriction (no stale statement found);
- the 53669a5 B3 repair (targets, never timing);
- the N7 repair (declaration-key conflict);
- every earlier closure re-checked in §5.

This verdict accepts nothing and authorizes no D4.

## 1. Blockers by earliest owner

### B1 — The construction rule's class is cut by representation: an external input the runner did not observe escapes `ext`, and a free seed is placed in the configuration (§6.3, §6.5 configuration and construction rule, §6.6 (2), §6.10, §17.5, §32.2; refinement R1; SD-17)

**Mechanism.**

*(i) Unobserved external inputs.*
- §6.3 records "every read the designated runner observed". Its fallback reads: "Where no current completeness judgment bounds the closure and the runner's observed reads are not complete, the widening reaches the whole tree". Widened entries are "over the governed files", so the fallback stops at the tree.
- An external read is "recorded by content identity where it can be pinned (§20.1) and otherwise as unpinnable". Only a *recorded* unpinnable read keeps an observation out of permissive uses.
- `ext(o, x) ⇔ neither o nor x recorded an unpinnable read ∧ every external locator that both record has the same pin ∧ … attributes`.
- No clause requires a designated runner to observe reads. §17.5 makes runner classes declare *attributes* only, and the Manual's own §31.3 SD-11 trajectory has "no observed reads".
- An execution that reads an input outside the tree without the runner observing it therefore records nothing, and `ext` holds against any other such execution.
- The fail-closed rule "an execution that does not record a declared attribute is treated as having an unpinnable read" covers missing attributes. It does not cover unobserved inputs.

*(ii) The free seed.*
- §6.5 defines configuration as "specification unit identity, regime, parameter instance, seed or replicate identity, and every execution attribute the specification fixes". The construction rule adds: "seed and replicate identity are configuration".
- §17.1 fixes a seed policy only for an `ENSEMBLE` granularity. A `SINGLE` specification that declares none leaves its seed free, and §17.2 records it.
- (2) and (4) range over "observation `o` of `conf(a⁻)`", so a run with another seed on the same content never enters them.
- The Manual also says:
  - §6.2: "stochastic replicate identity; every execution attribute the specification leaves **free** … | **execution variation**";
  - §6.6: "**Nondeterminism goes to the owner.** … (2) no other outcome on that content, ever, under any free attribute";
  - §6.10: "A stochastic failure becomes stale mechanically only if the specification fixes its seed policy so that (1) and (2) can hold; otherwise it goes to the owner".

  An implementer must choose between §6.5 and those statements. Under §6.5 the §6.10 claim is false whenever a recorded seed can be replayed, because the §6.9 rerun obligation reruns "the configuration".

**Trajectory (i) (D2 claim, declarative oracle; every step locally conforming).**
1. Specification `S` (`SINGLE`) evidences a D2 claim. Its runner class `hpc` is an external-custody class that declares image, backend and precision as recorded attributes and observes no file reads.
2. The solver reads a mesh by absolute path, `/shared/meshes/m.h5`, outside the repository. `S` neither fixes nor pins it. The closure is bounded by a current `COMPLETENESS(EXEC)` on `{S, kern}`; an `UNBOUNDED` closure gives the same result.
3. At `T0` the facility has replaced the mesh with version `M2`. `r0` fails `l2_error` because the solver mishandles a feature of `M2`, a real defect in the claimed regime. It is assessed `a⁻` and counts.
4. The reproduction `r1` on `tree(a⁻)` reads `M2` with the same attributes and fails identically, so (1) holds. No other run on `T0` exists, so (2) holds.
5. The mesh reverts to `M1`: a restore, or a node mounting a stale copy. An `IMPLEMENT` item changes a recorded region and integrates `T1`. The rerun `q` reads `M1` unobserved and passes.
6. (3) holds:
   - `on⁻(q, T1)`;
   - `ext(q, real(a⁻))`: neither records a pin or an unpinnable read, and the attributes are equal;
   - `bound(q)`.

   (4) holds because nothing on `T1` yields. The custody enumeration lists `r0`, `r1` and `q`.
7. `a⁻` is stale and `undisputed = T`. The defect that `M2` exposes is still in `T1`. Only the unrecorded input changed.

**Trajectory (ii).**
1. A `SINGLE` specification of a Monte Carlo estimator leaves its seed free. The runner draws a seed per run and records it, and the Dispatcher can replay a recorded seed.
2. On `T0`, `r0` (seed 17) fails `REL_TOL` through a bias defect that some seeds expose, and `p` (seed 42) passes. `a⁻` counts, the two assessments conflict (§6.2), and `undisputed = P`.
3. The rerun obligation reproduces seed 17 on `tree(a⁻)`, which fails identically, so (1) holds. (2) ranges over seed-17 runs only, so `p` is excluded and (2) holds.
4. An `IMPLEMENT` item edits a recorded region, perhaps one that consumes the random stream in another order. `q` (seed 17) on `T1` passes, so (3) and (4) hold. `a⁻` is stale and `undisputed = T`.
5. `p` had already shown, on unchanged content, that the outcome depends on the seed. The same-seed pass on `T1` discriminates nothing. Edit and rerun has produced a pass.

For a D1/D2 claim, both trajectories end with validity `T`, and the gate core lists the failure as stale, not disputed.

**Violated text.**
- Workplan §6.6 (reviewed): "missing dependency knowledge never proves that two executions read the same content"; a read outside the governed tree "that cannot be pinned makes the execution's content its own, never `on` any other execution's, so it supports no mechanical stop (fail closed)".
- Workplan §21 item 11: "acceptance never depends on the latest single replicate (edit-and-rerun is not a route to a pass)".
- Evidence owner:
  - "Where material, applicability must be recoverable over … environment/backend/precision/configuration, stochastic replicate identity …", which lists replicate identity apart from configuration;
  - "An assembled outcome after several simultaneous changes cannot be attributed to one mechanism without discriminating evidence";
  - "preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence".
- Manual:
  - R1 row: "every unfixed external input … is execution variation adversely and a difference permissively", and "the class statement leaves no named dimension for a later one to escape";
  - §6.2, §6.6 and §6.10 as quoted above;
  - §32.2: "never when it read an unpinnable input".
- Phase B closures: "executed content includes runtime inputs/observed reads" and "nondeterministic old-content observations defeat (2)" (6FE1000 B2).
- SD-17 names its disclosed residual as variation in what runner classes record about *attributes*. Unobserved inputs are neither in that residual nor fail-closed. The seed is excluded from the class by definition.

**Earliest owner.** Manual §6.3, §6.5 and §17.5, with §6.10 and §32.2; refinement R1. The Manual may narrow a permissive predicate under R1, and for (i) the reviewed workplan already states the fail-closed principle. This is therefore an ordinary blocker against the Manual, not a Serious Challenge.

**Family-level assessment (convergence owner, "Active simplification trigger"; "Review strategy after recurrence").**
- This is the tenth successive finding in the matching clause: `ef8445a` N2, `552ac01` N2, Phase B N2, `6ff4ed1` B1, `b595f2c` B1, `c6da678` B1, `cc005db` B2, `d837363` B1-B2, `53669a5` B1, and this one.
- SD-17 replaced the list with a class statement, which is the right direction. The class it protects is defined by a semantic property. The mechanism, however, admits a member only through its *representation*:
  - an input exists for the rule only if the runner observed it;
  - a seed leaves the class by being written into the configuration.
- The fail-closed default ("treated as having an unpinnable read") is applied to a declared attribute that is missing, but not to an undeclared observation capability.
- This is a non-local recurrence. These options go to the stakeholder (Phase C handoff §5) rather than a single repair:
  - **(a) Complete the class (minimal).**
    - Configuration is the specification unit, regime, parameter instance and the attributes the specification fixes. A free seed or replicate identity becomes a recorded free attribute that `ext` compares: (1) and (3) need the same seed, while (2) and (4) range over every seed, which realizes §6.10.
    - Each runner-class designation also declares whether it observes reads outside the tree (file and network) completely. An execution of a class that does not is treated as having an unpinnable read.
    - Cost: such classes get no mechanical stops, so their red-then-green iterations go to the owner. Disclose this in R1, §32.2 and §32.3.
  - **(b) As (a) for the seed, but accept unobserved inputs as a disclosed residual.** State it in R1, §17.5 and §32.2. This relaxes the reviewed fail-closed principle, so it needs the stakeholder's explicit acceptance.
  - **(c) Judgment-only staleness.** Delete (1)-(4), `on⁺`, `ext`, `bound`, the rerun and reading obligations and the class rule's mechanical candidate-own test. This removes the surface on which ten findings have recurred.
  - **(d) A different-family Review before the next repair.** For three rounds running, a same-family Review has missed a sibling of the dimension the previous round named.
- The reviewer's assessment: (a) is the smallest repair that keeps the reviewed fail-closed principle, and its cost falls only on runner classes that cannot observe reads. (c) remains the only option that removes the surface. The choice is the stakeholder's.

**Required discriminator.**
- (i) A runner class that observes no reads, with trajectory (i), at the real owners.
  - Under (a): `r0` is treated as having an unpinnable read, (1) and (3) never hold, `a⁻` keeps counting, `undisputed = P` and the owner's adjudication obligation is derived. An implementation that treats an execution with no recorded external read as having read none must fail.
  - Under (b): the §31.3 residual case asserts the disclosed behavior, and §32.2 names it.
- (ii) Trajectory (ii). Expected:
  - `p` defeats (2), `a⁻` is never stale mechanically, `undisputed = P` and the adjudication obligation is derived;
  - for a D1/D2 claim the floor fires when (2) fails;
  - an implementation that limits (2) or (4) to runs with `a⁻`'s seed must fail.

§31.3 has neither case, so a green §31 can coexist with B1 (DS-001).

### B2 — The revising review is keyed on the admission that produces a revision, after the fact; acceptances made in a frame, or folded into an `AUTHOR` integration, precede it, and "answered" is not "assessed" (§10.2 `REVIEW(s, r)`, `ACCEPT(s)`, `GATE(g)`; §8.3 step 7; §7.5-§7.6; §19.4; §10.3; §16.6; §29.4; SD-16; 53669a5 B2 repair)

**Mechanism.**
- §10.2 derives `REVIEW(s, r)` for "the current revision `r = cur(s)` of a `NATIVE` D1 or D2 subject `s` that is in the write set … of the admission producing `r`, where that admission integrated no `AUTHOR` item's transformation".
- §8.3 step 7 refuses a `GATE_DECISION ACCEPT` and an `ACCEPTANCE PASS` "on that revision of `s`" only "while `REVIEW(s, r)` (§10.2) is derived and unanswered".
- Acceptances are made in frames before the integrating admission. §7.5: "An acceptance in frame `X` … is a **prospective acceptance**". After integration, a frame acceptance on the merged revision is an admitted passing `ACCEPTANCE` on `(s, scope_id(s), cur(s))` and enters `ACC(s)`.
- A promotion's acceptance must be "recorded beforehand as a prospective acceptance in the promoting candidate's frame … and bound to the integrating admission" (§19.4, §7.6). That holds also for a promotion adopted from a quarantined declaration (§18.4: "a prospective acceptance bound to the same admission for any promotion").
- In a frame, no admission has yet produced the frame revision, so `REVIEW(s, ·)` is not derived there and step 7 refuses nothing.
- §10.3: a judgment obligation is answered by "the first admitted judgment of its kind on its target that is bound to it or recorded on its target by an authenticated human". Step 7 admits adverse judgments even when `slots_filled` refuses the request's passing judgments.

**Trajectory T1 — an adopted promotion (splitting D2 authority).**
1. D2 composite `numerics` is accepted at `r1`. Its part `numerics.method` is a heading span. A recorded tension `t` (an in-repository `CHALLENGES` home) binds `numerics`' accepted concretization `numerics.impl`.
2. A human pushes a commit that edits the text of `numerics.method` and declares it `subject = true` in the manifest.
   - The commit is absorbed at `k1`. The content change derives `REVIEW(numerics, r2)`.
   - The declaration becomes a governance-affecting quarantined delta.
3. An R2 reviewer submits an adopting request (`ABSORB`). In its frame, the authenticated D2 owner records the prospective `ACCEPTANCE PASS` on `(numerics.method, σ_A, r_A)` that §19.4 requires. At step 7, `numerics.method` is not yet a subject and no admission has produced `r_A`, so `REVIEW(numerics.method, r_A)` is not derived and nothing is refused.
4. The adoption is admitted at `k2` and the tenure of `numerics.method` starts with `bind(j) = τ`. `REVIEW(numerics.method, r_A)` is now derived, after the acceptance, and `ACCEPT(numerics.method)` is never derived.
5. The revising review later finds `t` applicable. The acceptance that it should have informed already stands. A gate that policy requires separately is decided in the admitted frame (§7.5) and still waits. The D2 acceptance itself does not.
6. A cutover (§19.5 condition 3, owner acceptance of the native revision before the `MODE_TRANSITION`) follows the same order.

**Trajectory T2 — a human change folded into an `AUTHOR` integration.**
1. D2 subject `s` is accepted at `r0`. An accepted D2 `AUTHOR` item `I` is issued on base `B`. Its implementer edits section A of `s`'s file (candidate revision `r_C`) and records `revision_assessments` against what it changed.
2. A human pushes an edit to section B of the same file, absorbed at `k1`. Then `cur(s) = r_h`; `REVIEW(s, r_h)` is derived; `ACCEPT` and `GATE` on `r_h` are not ready.
3. `M_n(X)` merges both edits cleanly (diff3, no overlapping hunk). `s` "changed on both sides is judged at its merged revision" `r_m` (§7.3).
   - `REVIEW(X)` is re-requested. That is a transformation review, and §16.3 injects the revising duty only for `AUTHOR` items and for `REVIEW(s, r)`.
   - In frame `X`, `cur(s) = r_m`, so `REVIEW(s, ·)` is not derived there.
4. The D2 owner records `ACCEPTANCE PASS` on `(s, σ, r_m)` in frame `X`. Step 7's refusal concerns "that revision" `r_h`, so the acceptance is admitted. The gate brief's section 3 shows `I`'s assessments, made before the human edit existed.
5. Integration at `k2` produces `r_m` through an admission that "integrated an `AUTHOR` item's transformation", so `REVIEW(s, r_m)` is not derived. `REVIEW(s, r_h)` disappears because `r_h` is no longer `cur(s)`. `GATE(g)` on `r_m` is ready.
6. The human's change is accepted without any revising assessment of it. §13.5 also leaves undefined which predecessor `I`'s `revision_assessments` names (N3).

**Trajectory T3 — answered without assessments.**
1. A human's D2 revision is absorbed, and `REVIEW(s, r)` is derived.
2. Either of these answers it:
   - the dispatched reviewer returns `REVIEW NO_PASS` with an empty `revision_assessments` slot: `slots_filled` yields `INCOMPLETE`, passing judgments are refused, and the adverse judgment is admitted and answers the obligation (§10.3);
   - an authenticated human who is not an author records a `REVIEW` judgment on the triple directly, which carries no `TASK_RESULT` and so no slot.
3. `GATE(g)` becomes ready. Section 3 renders "no revising-duty assessment recorded". An `UNQUALIFIED` `ACCEPT` is admissible, because the refusal rule lists only unavailable, disputed or stale evidence and classified missing records.

That is the outcome of the option the stakeholder declined, "Show absence only". §16.6's "so section 3 is rendered from an answered review" is true and does not help.

**Violated text.**
- SD-16, stakeholder record item 12, chosen option: "any D1/D2 revision not produced by an `AUTHOR` item gets the revising and tension-search duties and the `revision_assessments` slot before its acceptance … and the gate core shows them". The declined alternatives included "Show absence only".
- Workflow owner: "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments, including those marked inapplicable, with their asserters. Acceptance does not ratify an assessment the gate was not shown."
- Scientific checks e=5: "When revising, renaming, splitting, merging or replacing D1/D2 authority … In the revision's own record and its gate evidence, record the predecessor identity and, per found tension, a revision-scoped applicability assessment".
- §29.4 (E0): "every other D1/D2 revision (human, absorbed, adopted) derives a revising review, the revision's gate and acceptance obligations are not ready until it is answered, and Admission refuses a gate `ACCEPT` or an `ACCEPTANCE PASS` on the revision before then". T1 and T2 falsify it. The closure map's stakeholder-list bullet repeats the claim.

**Earliest owner.** Manual §10.2-§10.3, §8.3 step 7, §16.6 and §13.5; §29.4.

**Family-level assessment.**
- This is the sixth successive finding in the D1-D3 change rule: `b595f2c` B3, `c6da678` B3, `cc005db` B1, `d837363` B3-B4, `53669a5` B2, and this one.
- The common cause is visible: the duty is attached to *how a revision was produced* (an `AUTHOR` item or another route, decided at the producing admission), while acceptance attaches to a triple in a frame.
- Each repair has added a route or an ordering check on the producing side. The next route then reaches the acceptance from the other side: a frame, a prospective binding, or a merge.
- This is a non-local recurrence. Options:
  - **(a) Key the duty on the acceptance target (removes mechanism).**
    - Every passing `ACCEPTANCE` (prospective or not) and every `GATE_DECISION ACCEPT` on a D1/D2 triple `(s, σ, r)`, in any frame, is admissible only once a `revision_assessments` record for exactly `(s, r)` is admitted.
    - That record comes from the `AUTHOR` task whose result yields `r`, or from a revising review that S3 derives *in that frame* for `(s, r)` whenever none exists.
    - Its predecessor identity is `s`'s last accepted revision in the tenure, or the source subjects for a split, merge or rename.
    - `ACCEPT` and `GATE` readiness read the same condition.
    - This deletes the producing-admission classification, the `AUTHOR` exemption and the "current revision" restriction. It covers merged revisions, promotions, adoptions and cutovers by construction, and it matches e=5's own anchor ("the revision's own record and its gate evidence").
  - **(b) Keep the producing-admission trigger and add frame derivation, merged-revision coverage and a slot requirement for answering.** This is additive.
  - **(c) Backstop:** refuse an `UNQUALIFIED` gate `ACCEPT` while section 3 states absence. This is the "Absence blocks unqualified accept" option declined at SD-16, so the stakeholder would have to revisit it.
  - **(d) A different-family Review.**
- Under any option, T3 needs a rule. Either the revising review counts as answered only by a record carrying `revision_assessments` (a human answers through a task that carries the slot), or the stakeholder states what absence after an answer means.
- The reviewer's assessment: (a).

**Required discriminator.**
- T1, T2 and T3 at the real owners. Expected:
  - T1: the prospective acceptance of `numerics.method` is refused until revision assessments for `r_A` exist.
  - T2: the acceptance of `r_m` is refused until assessments covering `r_m`, with predecessor `r0`, exist.
  - T3: the gate is not ready, or behaves as the stakeholder decides for absence.
- An implementation that derives the review only from the producing admission must fail T1 and T2.
- An implementation that treats an adverse empty-slot answer or a slotless direct judgment as discharging the duty must fail T3.

§31.5's SD-16 case covers only the admitted-state route, so it passes with this defect.

## 2. Non-blocking findings

- **N1 — A `symbol` term that never resolves is now well formed (§1.9, §14.5, §2.6; entered through the 53669a5 N5 repair).**
  - "The check concerns the resolver, never the result" admits a term that resolves to `ABSENT` *at its own declaration*: a typo, or a C++ macro-generated definition.
  - That unit's content is then constant. The real bytes fall to the enclosing residual part. An analyzer that finds no marker in an empty unit can supply `COMPLETENESS` over it, so a realization whose recorded basis names the unit stays current when the real code changes.
  - §14.5 still says such a definition "cannot be named by a `symbol` term".
  - Repair: refuse an authored or adopted declaration whose term resolves to `ABSENT` in the merged tree at its own admission; keep a later `ABSENT` as a value; never let analyzer completeness cover an `ABSENT` unit.
- **N2 — Whether a composite subject is in the write set when only its parts' bytes change (§1.2; trigger of §10.2).**
  - The trigger requires the *subject* `s` in the write set. A part owns its bytes by innermost ownership, so the composite enters only through "its resolved regions".
  - If regions compare by location, a prefix-scoped D2 composite whose part file is edited by a human derives no revising review. The exclusion sentence ("A composite whose revision changes only because a nested subject of another kind … changed is not in it") implies the content reading.
  - State the content reading, or key the trigger on "`s` or a part of `s`". (Option (a) of B2 removes the question.)
- **N3 — The predecessor identity of an `AUTHOR` item's `revision_assessments` is undefined (§13.5).** It is defined only for `REVIEW(s, r)`. Define it as the last accepted revision in the tenure. This matters for T2 of B2.
- **N4 — "a `QUARANTINE` only naming paths of that object" is undefined for a structural delta (§18.4; residue of the 53669a5 N6 repair).** A delta is a declaration key. If its paths are the manifest's, a `QUARANTINE` of a foreign declaration can mark only `ssds.manifest`. Say whether the paths are the declared terms' resolved files, before and after the delta.
- **N5 — Runner-class declarations over time and volatile attributes (§17.5, §6.5 `ext`; restrictive).**
  - "`o` and `x` record the same value for every execution attribute either records" makes every failure recorded before a runner class gains or loses a declared attribute permanently unmatchable: (1) and (3) can never hold for it.
  - A declared attribute that cannot be requested (host or node identity) has the same effect for every failure.
  - Show this re-matching burden at the `RULESET_ADOPTION` that changes a runner designation, as §27.3 does for re-identification, and state that declared attributes should be requestable.
- **N6 — §20.1 "(other than its declared execution environment)".** After SD-17 the environment is whatever the runner class records. Say whether a read of a host file outside the declared components (a host-mounted library under an image-only class) is an external read or the §17.5 residual.
- **N7 — Closure map (aid only).**
  - Item 4 (observed-read fallback), item 5 (configuration matching) and item 11 (stochastic replicates) are annotated DECIDED or REFINED on text affected by B1.
  - Items 7, 10 and 27 are annotated on text affected by B2.
  - The stakeholder-list bullet "a D1/D2 revision outside an `AUTHOR` item cannot be gate-accepted or accepted until its revising review is answered" is false for T1-T2.

## 3. Closure audit (§21 items and §16.2 rows)

The closure map was used only to locate text, and its annotations were checked against the Manual.

**Not substantively resolved:**
- item 4: the executed-content computation's fallback for incomplete observed reads reaches only the tree (B1 (i));
- item 5: configuration matching and `stale` for unobserved inputs and free seeds (B1);
- item 11: replicate rules for `SINGLE` specifications with a free seed, against "edit-and-rerun is not a route to a pass" (B1 (ii));
- items 10 and 27: the gate template meeting Channel C for D1/D2 revisions accepted in frames, promoted, adopted or merged, and the §29.4 revising row (B2);
- item 13: promotion and cutover acceptances precede the revising review (B2 T1).

**Resolved with non-blocking defects:**
- item 1 (N1, N2);
- item 2 (N1);
- item 7 (N2);
- item 12 (N4);
- item 24 (N3).

**Resolved:** items 3, 6, 8, 9 and 14-26 apart from those listed. Each decision was located, and each is a decision rather than a route. Delegated D4 space is bounded, and nothing incidental is over-specified.

**§16.2:** every row of both workplan tables has a final disposition in §26.4, which also adds rows for 1.6.0 §4 and §14. That covers invariants 1-26 and frozen surfaces §3, §5-§13 and §15-§22, including every Deferred row (invariants 4, 9, 15, 17 and 26; surfaces §5, §6, §12 and §18). §26.4 is unchanged since 53669a5. None was found unresolved.

## 4. Refinements R1-R9

| # | Assessment |
|---|---|
| R1 | **Sound for recorded attributes; unsound in two members of its own class (B1).** SD-17 closes the 53669a5 B1 trajectory and its variants. Backend, precision and recorded host attributes enter `ext`; there is one definition of configuration for attributes (§6.5, §17.2); and an undeclared recorded attribute fails closed. The withdrawal of (0) and `mech` left no stale statement: "One reading per frame", "Standing per frame", "Accepted change", §6.8's floor list, §6.9 and §17.4 were each re-checked. `on⁺ ⇒ on⁻` still holds by construction, and `ext` reads only S0 facts, so §5.6 monotonicity is unchanged. The disclosed residual is honest for attributes. It is not honest for unobserved external inputs: §32.2's "never when it read an unpinnable input" and the row's "leaves no named dimension" are false (B1 (i)). The seed is excluded from the class by definition (B1 (ii)). |
| R2 | **Sound.** Unchanged; the clamp only lowers values. |
| R3 | **Sound.** Unchanged. |
| R4 | **Sound.** Unchanged; the publication failure points were re-read (§6), and the VM-snapshot residual is disclosed. |
| R5, R6, R7 | **Sound.** Unchanged. |
| R8 | **Sound.** Unchanged. |
| R9 | **Sound.** The 53669a5 B3 repair restores order symmetry for `INTAKE_DISPOSITION`: the rule now concerns targets, never timing. The veto, `stands⁻` and `vetoed` read S0 and S1 only. |

The SD-16 trigger and refusal, and the §7.2 declaration-key conflict, are decisions inside §21 items 10 and 5, not §0.3 refinements. §0.3's narrative lists both.

## 5. Previous findings, Phase B closures and N1-N4

**53669a5.**
- **B1** is closed for its named dimensions: backend, precision, recorded host and hardware attributes, and the double definition of configuration. The trajectory and its variants now fail as the Review required: `q` cannot serve (3), and a passing CPU run on `T0` defeats (2). Its unenumerated siblings are B1 here.
- **B2** is partly closed. The admitted-state route is closed: `GATE` and `ACCEPT` readiness, refusal including a direct human acceptance, and §31.5. The frame, prospective, merged and answered-without-assessment routes are B2 here.
- **B3** is closed. "for which an `INTAKE` obligation has been derived at some position … The rule concerns targets, never timing" admits the later contrary disposition and the owner's adjudication. A disposition on a never-intake subject is refused.
- **N1** is closed (restriction withdrawn; stale statements now true; §31.3 red-then-green case).
- **N2** is closed in all six bullets; residues are N2 and N3 here.
- **N3** is closed.
- **N4** is closed: release by an actor of the current domain; "both domains" removed; the uncovered-content statement corrected.
- **N5** is closed, and the repair introduced N1 here.
- **N6** is closed, with residue N4 here.
- **N7** is closed by the declaration-key conflict rule (held, §6).
- **N8** is closed.
- **N9** is superseded by N7 here.

**d837363.**
- **B1** is closed (environment, now inside the attribute class).
- **B2** is closed (pure resolvers; context recorded by value; unchanged).
- **B3** is closed for the admitted-state route; its frame routes are B2 here.
- **B4** is closed.
- **N1** and **N2** are closed.
- **N3** is closed through the 53669a5 B3 repair.
- **N4** is closed by disclosure (§27.3).
- **N5**, **N6** and **N7** are closed.
- **N8** is superseded.

**cc005db.**
- **B1-B3** are closed.
- **N1-N4** are closed. N2 is closed by SD-15 and SD-17; for unobserved reads see B1 (i).
- **N5** is closed by the target rule.
- **N6** and **N7** are closed as disclosed restrictive trades.
- **N8** is superseded.

**c6da678.**
- **B1** is closed for observed external inputs; its unobserved sibling is B1 (i) here.
- **B2** and **B3** are closed.
- **N1-N12** are closed as recorded at 53669a5. The changed text reopens none of them, and N2's residue is now fully closed by the target rule.

**b595f2c.** **B1-B4** and **N1-N8** are closed. The changed text touches none of their mechanisms.

**6ff4ed1.** **B1-B4** and **N1-N12** are closed. The changed text touches none of their mechanisms.

**Phase B §3 closures.** A clause comparison of §5.3-§6.10 with workplan §6.6 found these restated and changed only in the restrictive direction: S1 polarity, `cont`, `base`, `ev`, `undisputed`, `qual`, `about`/`starts`/`home`, Y1/Y2 coverage, the class rule's candidate-own exception, the absorbed-reading exclusion, never-lost salvage, independence, unknown authorship, retirement/split/retarget and `eff`. Two exceptions:
- "nondeterministic old-content observations defeat (2)" fails for nondeterminism across a free seed (B1 (ii));
- "executed content includes runtime inputs/observed reads" fails for inputs outside the tree that the runner did not observe (B1 (i)).

The W1/W2 "one reading per frame" stop and the Phase B §4 result "No persistent false global stop from test-first work", withdrawn by SD-15, are restored.

**Phase B N2 re-test.** The bounding completeness judgment was taken through `P`, blocked, revoked, superseded, loss-withheld and vetoed by an `INCOMPLETE`. Against each:
- a differing old-content run on an alternate tree that differs only outside the recorded regions (including another span of a recorded file), with `a⁻`'s seed, stays in (2);
- a yielding present-content run stays in (4).

Both hold because `on⁻` is unchanged and `ext` reads no completeness. A differing run with *another* seed is excluded by B1 (ii), which is a configuration defect, not a polarity defect. The support-cycle clamp (R2) and the corrupt-prefix halt (R3) are unchanged and fail-closed before any current assertion.

**Phase B N1, N3, N4.** N1 remains open and disclosed (§32.2, §32.4). The N3 limits are carried in §31.3. The N4 costs are in §32.3, with an updated attribute trigger.

**Both directions.**
- Permissive: B1 (i) and (ii) hide live failures; B2 lets a D1/D2 revision be accepted without assessments.
- Restrictive: N5 (permanently unmatchable failures after a runner-designation change).
- The repairs of the previous round's non-blocking findings were attacked in both directions:
  - N1 (53669a5 N5) admits never-resolving terms;
  - N4 (53669a5 N6) is undefined for deltas;
  - the N7 repair held;
  - the N2 repair's trigger depends on the write-set reading (N2 here).

## 6. Out-of-matrix trajectories attempted

**Broke the candidate:**
- B1: an unobserved mesh read under an external-custody class (bounded and `UNBOUNDED` closures); a free replayable seed under `SINGLE` granularity.
- B2: an adopted promotion with a prospective acceptance; a cutover acceptance; a human change folded into an `AUTHOR` integration by a clean merge; an adverse empty-slot revising review; a direct human `REVIEW` answer.
- N1: a C++ macro-generated `symbol` term and a misspelled one.
- N2: a prefix-scoped D2 composite whose part file is edited by a human.
- N5: a runner class gaining a declared attribute; a declared host identity.

**Held:**
- **SD-17 class over recorded attributes:**
  - CUDA versus CPU, `float32` versus `float64`, and AVX-512 versus AVX2 with the instruction set recorded: (3) refused, (2) defeated by a passing run on `tree(a⁻)`;
  - a host-mounted driver under a fixed image is free and compared;
  - a declared attribute missing from a realization fails closed;
  - `ext`'s "either records" is symmetric;
  - a §17.2 configuration read as including free attributes is excluded by "This is the only definition";
  - red-then-green under a free environment becomes stale in the lineage frame and the admitted state once (1) and (3) stand;
  - Dispatcher unavailability of a matching runner keeps the failure with the owner and never feeds derived state.
- **SD-13 guard and SD-15 repairs:** unchanged. `on⁻` reads no S2 value, structure, `ignore`, analyzer, system version, pin or attribute.
- **SD-16 admitted-state route:**
  - a human-pushed D2 revision derives `REVIEW(s, r)`, and `GATE(g)` and `ACCEPT(s)` are not ready;
  - a direct human `ACCEPTANCE PASS` or `GATE_DECISION ACCEPT` is refused with `OBLIGATION_REVIEW_OPEN`, and an adverse one is admitted;
  - parallel dispatch is impossible;
  - a nested-D4-only revision of a D2 composite derives none;
  - a re-identification with no byte change derives none.
- **Intake order (53669a5 B3):**
  - `ABSORB` then an independent `QUARANTINE`: admitted; it vetoes the `ABSORB` record's support and derives `ADJUDICATE_DISAGREEMENT`;
  - the owner's upholding adjudication: admitted, and realignment follows;
  - a disposition on a never-intake subject: refused.
- **Frame structure (53669a5 N7):** a both-sides change of one multi-line `scope` value is a conflict; one-sided and identical changes merge. Adopted deltas take the head's observed value, so the frame structure equals the enacted structure.
- **R9:** both orders for review, acceptance, conformance, plan acceptance, equivalence, completeness, gate, intake and product scope; peer supersession rejected; an answered obligation is never re-dispatched.
- **Publication, currentness, gates and floors (re-read §22-§23, §10.5, §15.4, §16.6):**
  - two processes sharing one host key;
  - a crash after a successful compare-and-swap;
  - a paused publisher against a landed or a pending fence;
  - a risk override never covers `GATE`;
  - an unqualified gate `ACCEPT` is refused while disputed evidence is listed;
  - floor items cannot be reclassified.
- **Partition and scope identity:** static sibling nesting rejected; crossed anchors resolve to `ABSENT`; byte-preserving refinement keeps `scope_id`, `rev` and tenure.
- **Derivation:** `ext` and the veto are S0/S1 constants, so S2 stays monotone with one least fixed point, and the stratification check is unaffected.

## 7. Minimum architecture and capability transfer

**Changes since 53669a5.**
- No component, tier or record kind is added.
- Removed: condition (0) and the S0 conjunct `mech`.
- Added:
  - a runner-class attribute declaration (a field of the existing policy designation);
  - one Admission refusal (`OBLIGATION_REVIEW_OPEN`, inside the existing `OBLIGATION_*` family);
  - readiness conditions on `ACCEPT` and `GATE`;
  - a stricter merge rule for declaration keys.
- §30's statements are accurate, except that its sentence "which that revision's gate and acceptance wait for" inherits B2.

**Minimality.**
- B1 option (a) adds one runner-class declaration and moves the seed out of the configuration. Option (c) removes the §6 stopping machinery.
- B2 option (a) removes mechanism: the producing-admission classification and the `AUTHOR` exemption.

**Capability transfer.**
- PC-001 (`AUTHORITY_BOUND`) was independently resolved at the public source ("When a new profile becomes current, every older supported profile remains frozen and independently testable.") and is preserved:
  - Core imports nothing from SSDS (§26.2);
  - §31.8 tests Core without SSDS;
  - the frozen 1.6.0 file, `source/` and `dist/` are byte-unchanged.
- The 1.6.0 transfer in §26.4 is complete.
- The Phase B capability "executed content includes runtime inputs/observed reads" is narrowed for unobserved inputs outside the tree (B1 (i)). No owner permits that narrowing silently.

**PEM basis.**
- `origin/main` is `af0455753e20ee54a969c844872e29e270007211`. The PEM blob `1561797125622f355f84eb27319f87e8fa4227d9` is identical at the candidate.
- `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run in the checkout, reports "PEM schema 1 valid: 5 families, 0 notices".
- HAS dispositions: PC-001 applicable and binding; DS-001 applicable as evidence only (it bears on §8); SP-001, SP-002 and FF-001 applicable as evidence only.

## 8. Qualification design

§31 binds claims to real owners and marks every runtime group UNEXECUTED; nothing beyond §31.10 is claimed as executed.

Green §31 fixtures can coexist with both blockers (DS-001):
- §31.3 has no runner class without read observation and no free-seed `SINGLE` case (B1);
- §31.5's SD-16 case covers the admitted-state route only, never a frame, promotion, adoption, cutover, merged revision or answer without assessments (B2).

The new §31.3 cases (free attributes; red then green) and the §31.5 refusal cases are adequate for what they target. The discriminators in §1 are required. The §14.7 `HARD` qualification design is adequate as design, with proposed-default values. The diagnostic model was not run: it is unchanged since Phase B and models no attributes, seeds, write sets or revision gates.

## 9. Doctrine-realization map and O1

The E0/E1 claims are tied to existing mechanisms, with two exceptions:
- §29.4's revising row claims E0 for "the order", which fails for frame, prospective and merged acceptances and for answers without assessments (B2);
- §29.5's documentation row ("a human's or absorbed revision of D1/D2 text derives its revising review first") fails for T2.

The enumeration is complete with its catch-all row, and the disclosed-E3 list (§29.6) is appropriately conservative.

O1 (§0.5) is unchanged: realized record, readers, routine questions, realized-record architecture and marked surfaces. "Beyond the requested deliverable: None" is consistent with the stakeholder record. Technical Review accepts no marked item, product scope or default value.

## 10. What was verified and how; what was not

**Executed** against a `git archive` snapshot of the candidate under `$TMPDIR/ssds80-manual-review-1ffbbf0/`, and against the repository:
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- `git diff --check 53669a583aa4858167c891f816756daac7ab7b22 1ffbbf0a918d514694ba1768d0a6d8a8fa579696`: clean.
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 1ffbbf0a918d514694ba1768d0a6d8a8fa579696`: 19 files, all within the expected set:
  - the Manual and the closure map;
  - six Manual review handoffs and six NO-PASS records;
  - the Phase C handoff and the Phase C continuation handoff;
  - the session handoff;
  - the stakeholder record;
  - two index lines.

  The 53669a5..1ffbbf0 diff touches the Manual, the closure map, the 53669a5 handoff and record, the continuation handoffs, and the stakeholder record (SD-17).
- `orchestrator/docs/architecture.md` (blob `39e6de7…`), `source/` (tree `fac2238…`) and `dist/` (tree `6bf729e…`) are identical at `fad3ee4…` and the candidate.
- All header blobs match. PEM was validated as in §7.

**Read** at the public source: the owners listed in the header, with the exact text quoted in §1 and §7.

**Not verified:**
- any runtime behavior (none exists); the trajectories are deductions from the specified contracts, not executed probes;
- the diagnostic model (not run);
- empirical costs, including how often runner classes lack read observation or how often seeds are free and replayable; B1 rests on the Manual permitting both, and §31.3's own trajectory assumes no observed reads;
- workplan §18 and §27 beyond a targeted search, and the earlier workplan NO-PASS records beyond the Phase B Review's §3-§4;
- D1, D2, D4 and specialist entrypoint texts beyond the software-design entrypoint and the scientific-checks fragment;
- the testing, PEM, storage, concurrency and security owners, which were not loaded because no finding turned on them.

## 11. Scientific-checks answers

- **Material findings:** B1, B2 and N1-N7 above. No agents or tools were launched beyond git, the unit test and the PEM validator, and none produced further findings. No material scientific finding about any project's science was made; this Review concerns D3 authority for software that mediates scientific evidence.
- **Realized results:** this Review produced, ran and reviewed no realized scientific results, including through the tools it ran, and it prepared no gate evidence. Its output is D3 review evidence toward G1. The unit test, `git diff --check` and the PEM validator are structural software checks, not realized results. Null envelope:
  - *Examined:* the Manual in full; the 53669a5..1ffbbf0 diff; the closure map and its diff; workplan §6.6 (assessed content, configuration, `stale`), §16.2 and §21; the 53669a5 Review in full; the finding lists of the d837363, cc005db, c6da678, b595f2c and 6ff4ed1 Reviews; Phase B Review §3-§4; the stakeholder record's SD-16 and SD-17 entries; PEM PC-001 and DS-001; the governing owners in the header.
  - *Materially not examined:* workplan §18 and §27 beyond a targeted search; the earlier workplan NO-PASS records; the diagnostic model's source; D1, D2, D4 and specialist entrypoint texts beyond the scientific-checks fragment; any runtime system.
  - *Materiality basis:* decision relevance to G1 closure, to the Manual's §0.4 invariants and to the stakeholder decisions SD-11 to SD-17.
- **Variants:** no analysis, pipeline, preprocessing, model or parameter variant was evaluated or selected (count 0).
  - Constructed trajectories are review hypotheses.
  - Two readings of one clause (§1.2 "its resolved regions": location or content) were compared as interpretation, with textual coherence as the criterion; the result is N2.
  - The B1 and B2 options are proposals for the stakeholder, not a selected survivor.
  - There was no delegated or resumed work.
- **Tension search:** not triggered. No consequential judgment relied on accepted project D1/D2 authority. The authorities used are SSDP 7.2.1 process owners, the stakeholder record and the reviewed workplan (a D3 cycle contract).

No part of these answers is left unanswered; the coverage limits are those of the null envelope and §10.

## 12. Common-mode note

This reviewer shares the Manual author's model family (Claude). It was launched by the authoring session from the issued handoff, and it shares the corpus, the inherited workplan framing and the toolchain. Fresh context is not epistemic independence. All seven Manual reviewers have been of this family; the Phase B reviewer was of the GPT family.

The B1 recurrence pattern, a sibling of the dimension the previous same-family Review named, now spans three rounds. That makes option (d) of both blockers material.

## 13. D4 statement

No D4 is authorized. This NO-PASS accepts no architecture, product scope or default value. A later PASS would be technical evidence for G1 only. G1 also needs explicit stakeholder acceptance, and shadow D4 needs G2.
