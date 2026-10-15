# SSDS 8 Architecture Manual — Independent D3 Review, candidate 53669a5

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout /home/user/scientific-software-development-system)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 53669a583aa4858167c891f816756daac7ab7b22
    SCOPE: the whole proposed Manual as durable D3 owner: (a) §21 and §16.2 closure; (b) fidelity to the
           Phase B-reviewed workplan, including refinements R1-R9; (c) out-of-matrix adequacy; (d) inheritance
           and capability transfer (Architecture 1.6.0, workplan §18, PEM HAS); (e) qualification design;
           (f) doctrine-realization map; (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob 341d6bf0b9304fe3690e40f5642276b381c6c5a6 (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md, blob 2fc8a17aa051240e453e93ef7ab63222963b6246 (verified)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23;
           Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b97fb8152d2a5742e17fa172e12204756, verified);
           blob at the candidate 91bde236465178f20c7348280e036d2884dfc216 (verified; the difference from the Phase B blob
           is Review/lifecycle coordination text only, checked by word diff)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml)
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS (HYPOTHESIS ONLY): MANUAL-REVIEW-SSDS-8.0-D837363-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-CC005DB-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-C6DA678-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-B595F2C-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-6FF4ED1-NO-PASS.md; WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
    REVIEW METHOD: entry through source/roles/software-design/SKILL.md at the public source; owners read there:
           architecture-and-design, abstraction-and-concretization, evidence-evolution-and-dependencies (applicability,
           assessment disagreement), workflow-and-workplans (D1/D2 revision gates; independent trajectories),
           convergence-and-cycle-economy (active simplification; review strategy after recurrence),
           protocol-versioning-and-compatibility (PC-001), source/shared/fragments/scientific-checks.md (e=5);
           full read of the Manual from a git-archive snapshot of the candidate; word diff d837363..53669a5;
           clause comparison of Manual §6 with workplan §6.6; constructed trajectories in the permissive and
           restrictive directions; G1 document checks executed
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session

Governing SSDP version for this Review: 7.2.1. The Manual's refinement table, decision markers, §30 pass and qualification claims, the closure map, commit messages, the handoff's scope text, workplan §0.1/§27 rationale, the diagnostic model's reported results, the stakeholder record's characterization of options and every prior Review record were treated as hypotheses. Section numbers refer to the Manual at the candidate unless prefixed "workplan".

## SERIOUS CHALLENGE

**None.** No accepted governing authority was found false, contradictory, ambiguous, inadequate or unrealizable. The evidence owner ("When competent evidence assessments materially conflict, preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence"), the workflow owner's D1/D2 revision-gate rule and scientific checks e=5 are coherent and realizable here. SD-15 and SD-16 are realizable as directed. B1 below is a gap in realizing SD-15's own rationale across every free execution dimension, and B2 is a gap in realizing SD-16's ordering. Neither is a defect in the stakeholder's direction. N1 records a decision-relevant consequence of SD-15 as realized; it is surfaced for the stakeholder, not raised as a Challenge.

## Verdict

**NO-PASS.** Three blockers survive.

- **B1** is the ninth successive finding in the matching clause and has the same shape as the d837363 B1 finding. SD-15 put the software *environment* into `on⁺`, and condition (0) requires the specification to fix it. Every other execution attribute that the specification leaves free still escapes the construction rule: backend, precision, and host or hardware components outside the runner class's recorded granularity. A failure caused by one of them is therefore made stale by a run that differs only there. The R1 row's claim that (0) "confines mechanical stops to fully recorded executions" is false. The Manual also defines "configuration" twice (§6.5 and §17.2), and under either reading a live failure can be hidden. This is a non-local recurrence, so §1 names options for the stakeholder.
- **B2** is new. SD-16 is realized only as the dispatch readiness of `ACCEPT`. `GATE(g)` for the same D1/D2 revision is ready at once, and nothing at Admission orders a gate decision or a human `ACCEPTANCE` after the revising review. In ordinary parallel dispatch, the gate the workflow owner names decides before any assessment exists and is shown only the absence statement. That is the outcome of the option the stakeholder declined ("Show absence only"), and it falsifies §29.4's E0 claim "before its acceptance".
- **B3** is new and entered through the repair of the d837363 Review's non-blocking N3. §18.4 now admits an `INTAKE_DISPOSITION` "only on an intake object that carries an `INTAKE` obligation". `INTAKE(δ)` is derived only while `δ` is quarantined, so once an `ABSORB` adopts `δ`, a contrary disposition and the owner's adjudication are both refused. The first disposition then wins by ledger order. The same paragraph and §31.5 say the opposite.

The SD-14 write set, the SD-13 guard, the SD-15 pure-resolver and by-value resolution-context repairs, and every earlier closure re-checked in §6 held.

This verdict accepts nothing and authorizes no D4.

## 1. Blockers by earliest owner

### B1 — Free execution attributes other than the environment escape the construction rule; a failure caused by a free backend, precision or unrecorded host component is made stale by a run that differs only there (§6.5 `ext` and construction rule, §6.6 (0), §6.2, §17.1-§17.2; refinement R1; SD-15)

**Mechanism.**
- §6.2 puts every free attribute in one class: "every environment, backend, precision or configuration attribute the specification **fixes**" is admissibility, and "every execution attribute the specification leaves **free**" is execution variation.
- §17.1: "Precision, backend and environment are fixed only when declared ... the default (free) is the conservative one for disagreement."
- §6.5 defines configuration as "its specification unit identity, regime, parameter instance, seed or replicate identity, and every execution attribute the specification fixes". A free backend or precision is therefore not part of `conf(a⁻)`.
- `ext` compares only unpinnable reads, pins and "the same identity for every environment component either records". §6.3 lists environment components as "interpreter, libraries, compilers, toolchain, runner image, at the granularity the runner class declares". Backend and precision are not environment components. §17.2 records "every free attribute's observed value" and "environment, backend, precision, toolchain and runner identity" separately, and no predicate reads them.
- (0) requires only that "the specification revision `a⁻` applied fixes its environment".

**Trajectory (D4 claim, declarative oracle; every step locally conforming).**
1. Specification `S` fixes `regime`, `parameters` and `environment = "image:sha256:I"` and leaves `backend` and `precision` free (the §17.1 default). Its runner class has CUDA and CPU nodes, and the execution uses CUDA when a device is present.
2. At admitted `T0`, realization `r0` runs on a CUDA node and fails `l2_error`, because of a defect in a CUDA-only code path. The failure is assessed as `a⁻` and counts. `mech(a⁻)` holds: the environment is fixed, its entries are recorded, and there is no unpinnable read.
3. The rerun obligation produces reproduction `r1` on `T0`, again on a CUDA node, and it fails identically. So (1) holds: `ext` is satisfied, with the same image and the same pins. No other run on `T0` exists, so (2) holds.
4. An `IMPLEMENT` item changes another recorded region and integrates `T1`. The affected-evidence rerun `q` lands on a CPU node and passes.
5. (3) holds: `q` is of `conf(a⁻)`, `on⁻(q, T1)` holds, `ext(q, real(a⁻))` holds because backend is no environment component, and `bound(q)` holds. (4) holds because no run on `T1` yields.
6. `a⁻` is stale and `undisputed = T`. The CUDA defect is still in `T1` and is now hidden. Nothing about the content discriminated the failure; only the backend changed.

**Variants with the same result.**
- **Precision.** `float32` versus `float64`, both free.
- **Hardware.** A fixed image `I` whose BLAS selects kernels by CPU at run time. `a⁻` and `r1` run on AVX-512 nodes and hit a kernel defect; `q` runs on an AVX2 node. The runner class records only the image, so the clause "not recorded at that granularity" never fires. §17.1 says a fixed environment "determines every environment entry the runner class records", which holds vacuously for an image-only class. Host-mounted GPU drivers and kernels behave the same way.

**The two definitions of "configuration".** §17.2 labels a realization's recorded "configuration (each fixed attribute's value and every free attribute's observed value ...)". If an implementer reads `conf(a⁻)` that way, a passing CPU run on `T0` is not "of `conf(a⁻)`", so it no longer defeats (2), and backend-dependent nondeterminism is hidden on the adverse side. Under the §6.5 reading, the hole is (3) as above. Under both readings a live failure is hidden, so an implementer must choose between two statements and either choice is unsound.

For a D1/D2 claim, `adm(a⁻)` makes the floor fire at step 2. Validity still becomes `T`, and the gate core lists the failure as stale, not disputed, exactly as in the d837363 B1 trajectory.

**Violated text.**
- R1 row: "the restriction (0) confines mechanical stops to fully recorded executions". §6.6 (SD-15 paragraph): "Condition (0) restricts mechanical stops to failures whose execution is fully recorded by content the construction rule can compare".
- §6.5 construction rule: "An unfixed external input or environment attribute is execution variation (§6.2): ... permissively they are not [the same]"; "A dimension added later follows the same rule".
- Evidence owner: "preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence"; "Where material, applicability must be recoverable over ... environment/backend/precision/configuration"; "An assembled outcome after several simultaneous changes cannot be attributed to one mechanism without discriminating evidence."
- SD-15's rationale (free environment attributes enter only the permissive predicate), which applies by its own terms to every attribute in the same §6.2 class.

Workplan §6.6 (3) has the same gap: "some standing admitted observation o of the configuration has on(o, G)", with configuration excluding free attributes. The Phase B Review and the diagnostic model did not vary free attributes. The Manual may narrow a permissive predicate under R1, so this is an ordinary blocker against the Manual, not a Serious Challenge to the reviewed contract.

**Earliest owner.** Manual §6.5 (`ext`, the construction rule, the configuration definition), §6.6 (0), §17.1-§17.2; refinement R1.

**Family-level assessment (convergence owner, "Active simplification trigger"; "Review strategy after recurrence").** This is the ninth successive finding in the matching clause: `ef8445a` N2, `552ac01` N2, Phase B N2, `6ff4ed1` B1, `b595f2c` B1, `c6da678` B1, `cc005db` B2, `d837363` B1-B2, and this one. The common cause is visible in the text. The construction rule is stated as an *enumeration* ("external pins, unpinnable reads, the execution environment, completeness standing, the same root tree"), not over the class it protects ("every dimension of the execution that is neither tree-resident recorded content nor fixed by the specification"). Each repair has added the dimension the previous Review named, and the next unnamed dimension escapes. This is a non-local recurrence, so these options go to the stakeholder (Phase C handoff §5) rather than a single repair:

- **(a) Class-level construction rule (minimal).** Permissive uses (`on⁺` through `ext`) require identity with `real(a⁻)` on every execution attribute the realization records and the specification leaves free. That includes backend, precision, environment components and any host or hardware attribute the runner class records; seed and replicate identity are already in the configuration. Delete the second definition of "configuration" (§17.2 becomes "recorded execution attributes"). State the class, never a list, in R1. Unrecorded host components stay a disclosed residual unless runner classes must record them.
- **(b) Generalized restriction.** (0) requires the specification to fix every execution attribute its runner class records, except declared stochastic ones. Same residual for unrecorded components.
- **(c) A different-family Review before or after the repair.** Every Manual reviewer has shared the author's model family, and this finding has the shape of the previous Review's B1, which that same-family round did not generalize.
- **(d) Reconsideration above §6.6: judgment-only staleness.** Every counted failure goes to the owner. Delete conditions (1)-(4), `on⁺`, `ext`, `bound`, the rerun and reading obligations, and the class rule's mechanical candidate-own test. This removes the family's whole failure surface. Under (0), the default free-environment case already pays this cost (see N1), so (d) mainly removes mechanism that serves only fixed-environment specifications.

The reviewer's assessment: (a) is the smallest repair consistent with SD-15. (d) is the only option that removes the surface on which nine findings have recurred, and its marginal cost over the already-chosen (0) is limited to fixed-environment specifications. The choice is the stakeholder's.

**Required discriminator.** Run the trajectory and its variants at the real owners. Expected:
- `a⁻` keeps counting, `undisputed = P`, and the owner's adjudication obligation stays derived.
- A CUDA run on `T1` can serve (3).
- A passing CPU run on `T0` defeats (2).
- An implementation that ignores a recorded free backend or precision in permissive uses, or that reads the §17.2 field as the configuration, must fail.

The new §31.3 case "Environment and pure resolvers" varies only the runner image, so §31 passes with this defect.

### B2 — SD-16 is realized only as `ACCEPT` dispatch readiness; the D1/D2 gate, and a human acceptance, can precede the revising review (§10.2 `REVIEW(s, r)`, `ACCEPT(s)` and `GATE(g)` triggers, §10.3, §16.6, §29.4; SD-16)

**Mechanism.**
- §10.2 derives `REVIEW(s, r)` for "a D1/D2 subject revision `r` not produced by an `AUTHOR` item". It makes `ACCEPT(s)` "ready only once its revising review is answered".
- `GATE(g)` is triggered by "a required human gate without a current `ACCEPT`", with no such condition.
- §10.3 lets a judgment obligation be answered by a judgment "recorded on its target by an authenticated human", without dispatch.
- §16.6 section 3 renders "no revising-duty assessment recorded" when none exists. Its refusal rule refuses an `UNQUALIFIED` `ACCEPT` only for listed unavailable, disputed or stale evidence, or a missing record classified material uncertainty or blocker. An absent revising assessment is classified neither way.
- Admission has no check tying a `GATE_DECISION` or `ACCEPTANCE` on such a revision to the revising review.

**Trajectory.**
1. D2 subject `numerics.method` is accepted at `r1`. A recorded tension `t` (an in-repository `CHALLENGES` home) is bound to its accepted concretization `numerics.impl`.
2. A human's direct push edits the D2 text and is absorbed, giving revision `r2` (route: absorbed). S3 derives:
   - `REVIEW(s, r2)`;
   - `GATE(g)` for the required D2 gate;
   - `ACCEPT(s)`, which is not ready.
3. The Dispatcher dispatches `REVIEW(s, r2)` and `GATE(g)` concurrently; both are ready. The gate brief's section 3 reads "no revising-duty assessment recorded" with route `ABSORBED`.
4. The gate holder records `GATE_DECISION ACCEPT`, `qualification = UNQUALIFIED`. The refusal rule does not fire, so it is admitted.
5. An authorized human who is not the author records `ACCEPTANCE PASS` on `(s, σ, r2)` directly, which §10.3 permits. `valid(s) = T`.
6. The revising review later records `t` as applicable, marked proposed. No gate is ever shown it. By e=5 it stays proposed "until the revision's acceptance considers it", which never happens.

Step 5 is not needed for the defect: step 4 alone means the gate the workflow owner names decides before any assessment exists.

**Violated text.**
- SD-16, stakeholder record item 12, chosen option: "any D1/D2 revision not produced by an `AUTHOR` item gets the revising and tension-search duties and the `revision_assessments` slot before its acceptance, the assessments marked proposed and attributed to their asserter, and the gate core shows them". The declined alternatives were "Absence blocks unqualified accept" and "Show absence only". The realized behavior in step 4 is "Show absence only".
- §29.4: "**E0** for the trigger: ... every other D1/D2 revision (human, absorbed, adopted) derives a revising review before its acceptance (§10.2)". The review is derived before acceptance but not answered before it, and nothing mechanical enforces the order.
- Scientific checks e=5: "an agent's assessment is marked proposed until the revision's acceptance considers it".
- Workflow owner: "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments". This is met only by the absence statement, which the stakeholder chose not to rely on.

**Earliest owner.** Manual §10.2-§10.3 (triggers and readiness) and §16.6 (gate refusal rule); §29.4 (the E0 claim). This is a clean local defect: the effect-keyed write set (SD-14) held, and no new mechanism is needed.

**Minimum repair direction.**
- `GATE(g)` and `ACCEPT(s)` for a D1/D2 revision not produced by an `AUTHOR` item are ready only once `REVIEW(s, r)` is answered.
- Admission refuses a `GATE_DECISION ACCEPT` and an `ACCEPTANCE PASS` on that revision while `REVIEW(s, r)` is unanswered.
- If the stakeholder wants a human override, it is a stated, recorded exception (for example `QUALIFIED`, naming the unanswered review), and §29.4 says so.

**Required discriminator.**
- For a human-authored D2 revision and for an absorbed one, `GATE(g)` is not ready before `REVIEW(s, r)` is answered.
- An authenticated `GATE_DECISION ACCEPT` and an `ACCEPTANCE PASS` submitted before then are refused, or are admitted only under the stated override.
- An implementation that dispatches the gate in parallel must fail.

§31.5's SD-16 case checks only `ACCEPT` readiness, so it passes with this defect.

### B3 — The intake-disposition target restriction refuses contrary dispositions and the owner's adjudication after an adoption, so an intake disagreement is resolved by order (§18.4, §10.2 `INTAKE(δ)`, §5.5 veto, §8.3 step 3; refinement R9; d837363 N3 repair)

**Mechanism.** §18.4 now ends: "Admission admits an `INTAKE_DISPOSITION` only on an intake object that carries an `INTAKE` obligation, and refuses an `ABSORB` of a delta on which an adverse disposition already stands, so neither order lets enactment outrun a standing objection." Three other rules interact with it:
- §10.2 derives `INTAKE(δ)` for "each quarantined delta; each uncovered or foreign observed change".
- §10.1 says derived obligations "appear and disappear as derivation changes". An `ABSORB` sets `Σ[k] := decl(M)[k]`, so `k ∉ Q` and `INTAKE(δ)` is no longer derived.
- §8.3 step 3 lets an `INTAKE_DISPOSITION` be superseded only by a record of the same kind: its author's reassessment or the owner's adjudication.

**Trajectory.**
1. A foreign push changes a structural declaration. The resulting delta `δ` is quarantined, and `INTAKE(δ)` is derived.
2. Reviewer A records an R2 `ABSORB` bound to `INTAKE(δ)` in an adopting request, admitted at `k1`. `δ` is enacted and leaves `Q`, so `INTAKE(δ)` is no longer derived.
3. Independent reviewer B submits `QUARANTINE` or `REJECT` on `δ`. The new sentence refuses it. It fails its own step-3 check, so it is not salvaged as never-lost, and S0 never reads it.
4. The owner's adjudication, an `INTAKE_DISPOSITION` naming A's record in `supersedes`, is refused the same way.
5. A's `ABSORB` stands unopposed by any disposition. The paragraph's first sentence ("a later standing adverse disposition of the same delta (§5.5) vetoes the `ABSORB` record's support ... where the owner upholds the adverse disposition, a realignment obligation follows") can never apply.

**Violated text.**
- §5.5: "The veto is symmetric in ledger order, so a passing judgment admitted before or after the adverse one is vetoed alike".
- R9: "vetoes every passing judgment of its kind on the same target, whatever their order".
- §31.5: "The same cases run for ... `INTAKE_DISPOSITION`" (in both orders).
- Evidence owner, applied by R9 to every judgment kind: "Do not resolve material assessment disagreement by ... serialized record position".
- Workflow owner: "cannot erase unresolved contradictory material evidence by vote".

The literal reading of the new sentence contradicts the first sentence of the same paragraph and §31.5. An implementer must choose, and the literal choice resolves the disagreement by order. This reopens the intake-order family (c6da678 N2, cc005db N5, d837363 N3) through the repair of its last non-blocking finding.

**Earliest owner.** Manual §18.4.

**Minimum repair direction (one phrase; no new mechanism).** The restriction concerns targets, never timing. It should read "only on an intake object for which an `INTAKE` obligation has been derived at some position (a quarantined delta, or an uncovered or foreign observed change)". It applies alike to a later contrary disposition, to the owner's adjudication and to the author's reassessment.

**Required discriminator.**
- `ABSORB` of `δ` at `k1`, then an independent `QUARANTINE`: the quarantine is admitted, vetoes the `ABSORB` record's support and derives `ADJUDICATE_DISAGREEMENT`. The owner's upholding adjudication is admitted and derives realignment.
- An `INTAKE_DISPOSITION` on a subject that was never an intake object is refused.
- An implementation that refuses the later disposition must fail.

## 2. Non-blocking findings

- **N1 — SD-15 as realized withdraws reviewed stops for free-environment specifications, and the Manual still asserts them (§6.6 (0); §6.4; §6.6 "What the four conditions keep"; §17.4; §32.2-§32.3). Decision-relevant for G1.** (0) makes every failure of a specification whose environment is free (the §17.1 default) never stale. That includes:
  - failures that are discriminated by *reading*, not by environment;
  - a candidate's failure of an admitted obligation, which "counts at once" in the admitted state (§6.4). Such a failure now qualifies the admitted claim until a disposition stands. For a D1/D2 claim, `mech(a⁻)` false raises a floor item at once, with human attention for every failing iteration.
  - an iteration-1 failure in a candidate's own lineage, which now blocks that lineage's integration after iteration 2 fixes it, unless the owner disposes of it (`ev` is `P`, so discharge is `OPEN` outside an override).

  This withdraws, for the default case, the reviewed W1/W2 property and the Phase B §4 result "No persistent false global stop from test-first work". Several statements remain unchanged and are now false for free-environment specifications:
  - "a candidate's tightened tolerance or test-first case is stale in the admitted state as soon as the admitted reading passes the admitted outcome" (One reading per frame);
  - "a⁻ counts again in G until one execution on the new content ... shows it not yielded" (Standing per frame);
  - "an admitted specification revision that the admitted outcome passes makes an earlier mechanical failure stale" (Accepted change);
  - §17.4: "An execution-dependency change triggers a rerun obligation, including the configuration of every failing assessment", against §6.9's "nothing is scheduled".

  The (0) formula is normative (§0.1), so this is not a blocker. However, §32.3's "most failures go to the owner" understates the consequence, and the stakeholder chose SD-15 without these consequences stated. Repair:
  - correct the stale statements;
  - state the consequence in R1, §32.2 and the closure map's stakeholder list;
  - add a §31.3 red-then-green iteration case under a free environment.

  The stakeholder may confirm the restriction or scope it.
- **N2 — Revising-review trigger details (§10.2, §16.6, §29.4).**
  - The trigger is "a D1/D2 subject revision r not produced by an `AUTHOR` item: a human's ordinary change, an absorbed or an adopted change". A D2 composite's revision that changes only because an `IMPLEMENT` item changed a nested D4 subject (§1.2) is neither in the list nor produced by `AUTHOR`. Under the list reading `ACCEPT(s)` is never ready (a dispatch deadlock); under the general reading a revising review runs on unchanged own content. State which applies.
  - The trigger has no currency condition, so every intermediate revision derives an obligation; restrict it to `cur(s)`.
  - Say whether it applies to `LEGACY(p)` and `UNGOVERNED` subjects, where SSDS "never adjudicates".
  - A re-identifying `RULESET_ADOPTION` (§27.3) derives a revising review for every byte-identical D1/D2 revision. Disclose this or exempt it.
  - Define "the predecessor identity" for a human revision (the last accepted revision).
  - §29.4's "an agent can change a D1-D3 unit only through an `AUTHOR` item" should read "owned content" (d837363 N1 residue).
- **N3 — A stale qualification sentence contradicts §1.2 (§31.5).** "an `AUTHOR` item for that D2 unit may edit those declarations without `ssds.manifest` in scope". §1.2 now puts `ssds.manifest` in the write set "whenever the manifest's bytes change", and §8.3 step 3 requires the write set to lie within the write scope; §13.2 accordingly admits `ssds.manifest` to `AUTHOR` scopes. As written, the case would force D4 to violate §1.2. This entered through the d837363 N5 repair.
- **N4 — Cross-domain structural route (§13.2, §8.3 step 4).**
  - §13.2 requires "release by the old domain's owner (§8.3 step 4)" for nesting or carving across domains. Step 4 checks only "a change of a unit's kind or owning domain", so byte transfer between subjects of different kinds has no release check.
  - "Actors qualified for both domains" has no policy mapping.
  - With no catch-all declared, the uncovered region is not a unit. An `AUTHOR` item can then declare a new D1-D3 unit over uncovered content without any unit of another kind entering its write set, contrary to "classifying uncovered content as D1-D3 ... has no agent item route". The effect is restrictive-safe, because the `AUTHOR` duties and acceptance apply, but the statement is false.
- **N5 — §1.9 "every `symbol` term resolvable by its analyzer as a pure function of file bytes".** If "resolvable" means "resolves", this contradicts §1.3 ("`ABSENT` is a value, not an error"): deleting a named function becomes a static error, and an absorbed deletion makes the subject ill-formed. State that the check concerns the resolver's purity (term kind and language), never the result.
- **N6 — `QUARANTINE` residue (§18.4).**
  - "until the owner's adjudication supersedes it or an upheld challenge disposes of it" omits the author's reassessment that `stands⁻` allows.
  - "owns any of those paths" is undefined for files whose spans several subjects own.
  - Content moved to a new path escapes "under".
  - The paths a `QUARANTINE` names are not restricted to the intake object's paths, so the target restriction alone does not stop a reviewer bound to one foreign change from quarantining unrelated subjects (d837363 N3 residue).
- **N7 — Frame structure versus enacted structure (§7.1, §7.2, §7.6 versus §8.3 step 4(a); pre-existing, now load-bearing for the write set).**
  - `Δ_Σ(X)` is `C`'s declaration changes relative to `B`. The frame and the write set use `Σ_n ⊕ Δ_Σ(X)`, and §7.6 says integration admits that structure.
  - Step 4(a), however, enacts `decl(M)[k]`. When the head and `C` change different lines of one multi-line declaration value, diff3 merges cleanly and the two differ.
  - The frame then silently reverts the head's admitted change. Judgments and the write set are computed under a structure that is not enacted, or `Σ` loses the head's change into quarantine.
  - Define `Δ_Σ(X)` against `decl(M_n(X))` and `decl(T_n)`, or treat a both-sides change of one declaration key as a merge conflict.
- **N8 — Stale summary rows.**
  - §30 does not mention SD-16's new obligation trigger, the environment entries or the `mech` conjunct.
  - §29.5's documentation row ("authority text changes only through `AUTHOR`") is unbounded although human revisions exist (d837363 residue).
  - §13.6's `REVIEW` system contract does not list `revision_assessments` for the revising review; only §13.5 triggers it.
- **N9 — Closure map (aid only).** Items 5, 10, 12 and 27 are annotated DECIDED or CARRIED on text affected by B1-B3. Item 5's annotation repeats the "fully recorded" premise.

## 3. Closure audit (§21 items and §16.2 rows)

The closure map was used to locate text only, and its annotations were checked against the Manual.

**Not substantively resolved:**
- item 5: configuration matching and `stale` over free execution attributes (B1);
- item 3: which execution attributes are claim-defining, in so far as "configuration" has two definitions (B1);
- items 10 and 27: the gate template meeting Channel C for D1/D2 revisions not produced by `AUTHOR`, and the §29.4 revising row (B2);
- item 12: dispositions and adoption, in the later-adverse order (B3).

**Resolved with non-blocking defects:**
- item 1 (N7);
- item 7 (N2);
- item 13 (N4);
- item 23 (N3, N4);
- item 22 (N8).

**Resolved:** items 2, 4, 6, 8, 9, 11 and 14-21; items 24-26. Each decision was located, and each is a decision rather than a route. Delegated D4 space is bounded and nothing incidental is over-specified. The pure-resolver constraint that the d837363 Review found missing from the parser delegation is now stated (§14.5).

**§16.2:** every row of both workplan tables (invariants 1-26; frozen surfaces §3, §5-§13 and §15-§22), including every Deferred row (invariants 4, 9, 15, 17 and 26; surfaces §5, §6, §7, §9-§11, §12 and §18), has a final disposition in §26.4, which adds rows for 1.6.0 §4 and §14. None found unresolved.

## 4. Refinements R1-R9

| # | Assessment |
|---|---|
| R1 | **Unsound in one dimension class; sound otherwise.** The SD-13 guard now holds: resolvers are pure functions of file bytes, the `ANALYZER_OUTPUT` scheduling step is deleted, and the resolution context is recorded by value at the start position. `on⁻` reads no S2 value, no current `Σ`, `ignore`, analyzer, system version, pin or environment, and `on⁺ ⇒ on⁻` holds. The environment conjunct and (0) close the d837363 B1 trajectory. B1: the construction rule is enumerated, so free backend, precision and unrecorded host components escape it, and the row's "fully recorded" claim is false. N1: the consequences of (0) for reading-discriminated and candidate-own stops are not stated, and statements that contradict (0) remain. |
| R2 | **Sound.** The clamp only lowers values; `mech`, the veto, `stands⁻` and `ok` are S0/S1 constants. |
| R3 | **Sound.** |
| R4 | **Sound.** The failure points were re-checked at text level (see §6); the VM-snapshot residual is disclosed. |
| R5, R6, R7 | **Sound.** |
| R8 | **Sound.** |
| R9 | **Sound in mechanism; broken for one kind and one order by B3.** Product-scope acceptance stays one kind. `REFUSED` is surfaced. The veto, `stands⁻` and `vetoed` read S0/S1 only. |

The SD-14 write set (now head-to-merged, with every declaration key and lineage as a fold) and the SD-16 revising review are decisions inside §21 items 23 and 10, not §0.3 refinements. Both are listed in §0.3's narrative.

## 5. Previous findings, Phase B closures and N1-N4

**d837363.**
- **B1** is closed for the environment, through `ext`'s environment conjunct and (0). Its sibling dimensions are B1 here.
- **B2** is closed: (i) the pending window is gone with the scheduling step; (ii) host-dependent resolution is excluded by §1.3, §1.9 and §14.5; (iii) the context is recorded "computed together with its terms at the execution's start position, never inferred from the record's envelope `ruleset`".
- **B3** is partly closed: the revising review is derived and the gate core states absence. The ordering is B2 here.
- **B4** is closed: `T_n` under `Σ_n` is compared with `M_n(X)`, every declaration key is included, and lineage is a fold. Its residues are N3 and N7.
- **N1** is closed in mechanism (composite excluded; gate statement); its residue is N2.
- **N2** is stated, with residue N4.
- **N3** is repaired, and the repair introduced B3. Its residue is N6.
- **N4** is closed by disclosure (§27.3).
- **N5** is closed (the manifest is always in the write set); the repair left N3.
- **N6** and **N7** are closed.
- **N8** is superseded by N9.

**cc005db.**
- **B1** and **B2** are closed, with the residues above.
- **B3** is closed (§3.5).
- **N1** is closed (§4.2 and §20.1 agree with §6.3).
- **N2** is closed for the environment; its sibling dimensions are B1.
- **N3** and **N4** are closed (pure, term-level resolution).
- **N5** is reopened as B3, in the later order.
- **N6** and **N7** are closed, disclosed as restrictive trades.
- **N8** is superseded.

**c6da678.**
- **B1** is closed (SD-12).
- **B2** is closed (`same` covers any item revision with the same content).
- **B3** is closed (effect-keyed write set).
- **N1** is closed (`stands⁻` requires `¬superseded(d)`).
- **N2** is closed in the R9 adverse list, with residue B3.
- **N3** is closed (disclosed: "an agent's task has ended").
- **N4** is closed (the same revisions of `X`'s members).
- **N5** is closed (the R9 row names `REFUSED`).
- **N6** is closed by pure resolvers.
- **N7-N12** are closed as checked against §6.3, §1.3, §1.8, §16.5, §13.2 and §30.

**b595f2c.**
- **B1-B4** are closed.
- **N1-N8** are closed: §3.4 producer column; §14.5; §3.4 and §27.1 name the analyzer set; SD-12; §31.2; §13.3 "whatever its kind"; §30; the undefined term removed.

**6ff4ed1.**
- **B1-B4** are closed.
- **N1-N12** are closed as checked against the text:
  - the "either" clause;
  - R8;
  - the `qualification` field in §3.4;
  - §8.3 step 5;
  - §2.6;
  - `CHALLENGES` excluded from cycle legality;
  - §1.4 rule 1;
  - §23.4;
  - the §29 rows;
  - §26.4 rows for §4 and §14;
  - export in §0.5;
  - the closure-map 168-hour note.

**Phase B §3 closures.** A clause comparison of §5.3-§6.10 with workplan §6.6 found the following restated, and changed only in the restrictive direction: S1 polarity, `cont`, `base`, `ev`, `undisputed`, `qual`, `about`/`starts`/`home`, Y1/Y2 coverage, the class rule's candidate-own exception, the absorbed-reading exclusion, never-lost salvage, independence, unknown authorship, retirement/split/retarget and `eff`. Two exceptions:
- "nondeterministic old-content observations defeat (2)" fails for nondeterminism across free backend or precision under the §17.2 reading of configuration (B1);
- the W1/W2 "one reading per frame" stop and the Phase B §4 test-first result are withdrawn for free-environment specifications by (0) (N1). This is restrictive and stakeholder-directed, but its consequences are not surfaced.

**Phase B N2 re-test.** The bounding completeness judgment was taken through `P`, blocked, revoked, superseded, loss-withheld and vetoed by an `INCOMPLETE`. In each case it was tested against two runs:
- a differing old-content run on an alternate tree that differs only outside the recorded regions, including another span of a recorded file: it stays in (2);
- a yielding present-content run: it stays in (4).

Both hold because `on⁻` reads no completeness, structure, analyzer, system version, pin or environment, and (0) only narrows `stale`. The support-cycle clamp (R2) and the corrupt-prefix halt (R3) are specified fail-closed before any current assertion.

**Phase B N1, N3, N4.** N1 remains open and disclosed (§32.2, §32.4). The N3 limits are carried in §31.3. The N4 costs are in §32.3, with a new trigger for (0) that N1 finds understated.

**Both directions.**
- Permissive: B1 hides live failures; B2 lets a D1/D2 gate accept before any revising assessment exists; B3 lets the first intake disposition win by order.
- Restrictive: N1 (reading-discriminated and candidate-own stops withdrawn); N2 (dispatch deadlock under the list reading); N6 (the `QUARANTINE` path lever).

## 6. Out-of-matrix trajectories attempted

**Broke the candidate:**
- B1: CUDA versus CPU (free backend); `float32` versus `float64` (free precision); BLAS CPU dispatch under a fixed image recorded at image granularity; the §17.2 reading of configuration on the adverse side.
- B2: parallel dispatch of the revising review and the gate; a direct human `ACCEPTANCE`.
- B3: `ABSORB` followed by a contrary disposition, and the owner's adjudication after an adoption.
- N1: red-then-green iteration, a tightened check and a test-first case under a free environment.
- N2: a nested-only D2 revision; a re-identifying adoption.
- N4: an `AUTHOR` item classifying uncovered content with no catch-all.
- N7: a both-sides edit inside one multi-line `scope` value.

**Held:**
- **SD-13 guard (ledger inputs):** a normalization or anchor-table system version; a policy change; a structural adoption (byte-preserving refinement, `ignore` change, re-scope); an analyzer-set change; completeness lost six ways; a loss boundary; frames and rebases (`tree(a⁻)` fixed).
- **SD-15 repairs:**
  - two hosts with different header sets give the same `on⁻` and `rev` (pure `symbol` resolution, §14.5);
  - an execution straddling a system-version adoption keeps `on⁻(p, tree(p))`, because the context is recorded at its start;
  - a free-environment failure under image `b1` is never stale whatever `b2` runs show, and nothing is scheduled;
  - under a fixed environment, a run under another image is inadmissible;
  - a fixed declaration coarser than recorded entries (a recorded driver difference) keeps the run out of `on⁺` through `ext`;
  - an unrecorded environment is treated as unpinnable and makes `mech` false;
  - Git LFS pointer reads, symlinks and gitlinks are content-addressed and pure.
- **SD-12:** the c6da678 external-input trajectory and its unpinnable variants.
- **Granularity:** another span of a recorded file, another unit's file in a bounded closure, and an ignored file under a widened directory leave `on⁻` unchanged; a governed file under a widened directory changes it, as the reviewed `on` requires.
- **One representation:** currency (unit, read and widened entries), (1)-(4), `adm`, the floor, the class rule and `mech` all read the one `REALIZATION` record. Every `on⁻` use is adverse and every `on⁺` use permissive.
- **Derivation:** `mech` is an S0 constant, so S2 stays monotone with one least fixed point; the stratification check is unaffected.
- **SD-14 write set:**
  - a concurrent admission outside an `IMPLEMENT` scope never enters the item's write set;
  - in the two-item `ignore` split, the second to integrate is a `VIOLATION`;
  - a `renamed_from`-only change is a `VIOLATION`, and its removal leaves admitted lineage;
  - a concurrent re-declaration of a prefix as D2, met by a new file from the candidate, enters the write set;
  - an `AUTHOR` D2 item with `ssds.manifest` in scope editing a D1 declaration or `ignore` affecting D4 is a `VIOLATION`;
  - a nested D4 change leaves the D2 composite out of the write set, and the gate core says so;
  - Git LFS and anchor-line edits do not escape.
- **SD-16 trigger:** human-authored, absorbed and adopted D2 revisions each derive `REVIEW(s, r)`, and the gate core states absence.
- **R9:** both orders for review, acceptance, conformance, plan acceptance, equivalence, completeness, gate and product scope; peer supersession rejected; an answered obligation is never re-dispatched.
- **Publication, currentness, gates and floors:**
  - two processes sharing one host key (only the appending incarnation publishes);
  - a crash after a successful compare-and-swap (the new incarnation records `PUBLISHED` or fences);
  - a paused publisher against a landed fence (its compare-and-swap fails), or against a fence still pending (`LATE_PUBLICATION`, decided after settlement);
  - a risk override never covers `GATE`;
  - an unqualified gate `ACCEPT` is refused while disputed evidence is listed;
  - floor items cannot be reclassified.
- **Partition and scope identity:** static sibling nesting rejected; crossed anchors resolve to `ABSENT`; byte-preserving refinement keeps `scope_id`, `rev` and tenure.

## 7. Minimum architecture and capability transfer

**Changes since d837363.**
- No component, tier or record kind is added.
- Added: environment entries in the execution basis, the S0 conjunct `mech`, and one obligation trigger (`REVIEW(s, r)`).
- Removed: the `ANALYZER_OUTPUT` scheduling step and its fallback.
- §30 describes the SD-15 changes as removing mechanical stops rather than adding mechanism, which is fair. It does not mention the SD-16 trigger (N8).

**Minimality.** The B1 options are subtractive or class-level, and option (d) removes the §6 stopping machinery entirely. The B2 and B3 repairs add no mechanism.

**Capability transfer.**
- (0) withdraws a reviewed capability, mechanical stops for free-environment specifications. No owner requires it: the evidence owner permits owner adjudication. The withdrawal is stakeholder-chosen, but its consequences are under-disclosed (N1).
- The 1.6.0 transfer in §26.4 is complete.
- PC-001 (`AUTHORITY_BOUND`) was independently resolved at the public source ("When a new profile becomes current, every older supported profile remains frozen and independently testable.") and is preserved: Core imports nothing from SSDS (§26.2); §31.8 tests Core without SSDS; and the frozen 1.6.0 file, `source/` and `dist/` are byte-unchanged.
- Workplan §18 was spot-checked against the Manual. No other capability was found narrowed.

**PEM basis.**
- `origin/main` is `af0455753e20ee54a969c844872e29e270007211`, and the PEM blob `1561797125622f355f84eb27319f87e8fa4227d9` is identical at the candidate.
- `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run in the repository checkout, reports "PEM schema 1 valid: 5 families, 0 notices". Run in the git-archive snapshot, it reports `REVIEW_REQUIRED` binding health because no Git repository is available for route realization. That is an environment artifact, not a PEM defect.
- HAS dispositions: PC-001 applicable and binding; DS-001 applicable as evidence only (it bears on §8); SP-001, SP-002 and FF-001 applicable as evidence only.

## 8. Qualification design

§31 binds claims to real owners and marks every runtime group UNEXECUTED; nothing beyond §31.10 is claimed as executed. Green §31 fixtures can coexist with B1 and B2 (DS-001):
- the §31.3 SD-15 case varies only the runner image, never backend, precision or hardware, and never the configuration reading (B1);
- the §31.5 SD-16 case checks only `ACCEPT` readiness, never gate ordering or a direct human acceptance (B2);
- no case runs a red-then-green iteration or a tightened check under a free environment (N1).

The §31.5 sentence "The same cases run for ... `INTAKE_DISPOSITION`" would detect B3. It therefore contradicts §18.4 rather than missing the defect, which is part of why B3 is a contradiction. The §31.5 `AUTHOR`/`ssds.manifest` sentence is stale (N3).

The discriminators in §1 are required. The §14.7 `HARD` qualification design is adequate as design, with proposed-default values. The diagnostic model was not run; it is unchanged since Phase B and models no free execution attributes, environments, write sets or revision gates.

## 9. Doctrine-realization map and O1

The E0/E1 claims are tied to existing mechanisms, with these exceptions:
- §29.4's revising row claims E0 "before its acceptance", which holds only for dispatched `ACCEPT` (B2);
- §29.5's documentation row is unbounded for human revisions (N8).

The enumeration is complete with its catch-all row, and the disclosed-E3 list (§29.6) is appropriately conservative.

O1 (§0.5) is unchanged: realized record, readers, routine questions, realized-record architecture and marked surfaces. "Beyond the requested deliverable: None" is consistent with the stakeholder record. Technical Review accepts no marked item, product scope or default value.

## 10. What was verified and how; what was not

**Executed** against a `git archive` snapshot of the candidate under `/tmp/ssds80-manual-review-53669a5/`, and against the repository:
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- `git diff --check d83736390938aaca3ea224ac880e0f49b187e019 53669a583aa4858167c891f816756daac7ab7b22`: clean.
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 53669a583aa4858167c891f816756daac7ab7b22`: 16 files, all within the expected set:
  - the Manual and the closure map;
  - five Manual review handoffs and five NO-PASS records;
  - the Phase C handoff;
  - a one-line session-handoff change;
  - fourteen lines in the stakeholder record;
  - two index lines.

  The d837363..53669a5 diff touches the Manual, the closure map, the d837363 handoff and record, and the stakeholder record (SD-15, SD-16).
- `orchestrator/docs/architecture.md` (blob `39e6de7…`), `source/` (tree `fac2238…`) and `dist/` (tree `6bf729e…`) are identical at `fad3ee4…` and the candidate.
- All header blobs match. PEM was validated as in §7.

**Read** at the public source, as listed in the header.

**Not verified:**
- any runtime behavior (none exists); the trajectories are deductions from the specified contracts, not executed probes;
- the diagnostic model (not run);
- empirical costs, including the volume N1 predicts;
- workplan §27 history and the earlier workplan NO-PASS records beyond the Phase B Review's §3-§4 and the Phase C handoff's summaries;
- D1, D2 and specialist entrypoint texts beyond the scientific-checks fragment and the Manual's citations;
- whether real runner classes select backend or CPU kernels at run time as B1's trajectories assume. B1 rests on the Manual permitting it, and §17.1's default makes it ordinary.

## 11. Scientific-checks answers

- **Material findings:** B1-B3 and N1-N9 above. No agents or tools were launched beyond git, the unit test and the PEM validator, which produced no further findings.
- **Realized results:** this Review produced, ran and reviewed no realized scientific results, including through the tools it ran, and it prepared no gate evidence. Its output is D3 review evidence toward G1. Null envelope:
  - *Examined:* the Manual in full; the d837363..53669a5 diff; the closure map; workplan §6.6, §16.2, §17 and §21; the d837363 Review in full; the finding lists of the cc005db, c6da678, b595f2c and 6ff4ed1 Reviews; Phase B Review §3-§4; Phase C handoff §5-§6; the stakeholder record (items 1-12, SD-1 to SD-16); PEM PC-001 and DS-001; the governing owners in the header.
  - *Materially not examined:* workplan §27 and other sections not listed; the earlier workplan NO-PASS records; the diagnostic model's source; D1, D2 and D4 entrypoint texts beyond the scientific-checks fragment; any runtime system.
  - *Materiality basis:* decision relevance to G1 closure and to the Manual's §0.4 invariants.
- **Variants:** no analysis, pipeline, preprocessing, model or parameter variant was evaluated or selected (count 0). Constructed trajectories are review hypotheses. The B1 options are proposals for the stakeholder, not a selected survivor. There was no delegated or resumed work.
- **Tension search:** not triggered. No consequential judgment relied on accepted project D1/D2 authority. The authorities used are SSDP 7.2.1 process owners, the stakeholder record and the reviewed workplan.

## 12. Common-mode note

This reviewer shares the Manual author's model family (Claude). It was launched by the authoring session from the issued handoff, and it shares the corpus, the inherited workplan framing and the toolchain. Fresh context is not epistemic independence. All six Manual reviewers have been of this family; the Phase B reviewer was of the GPT family.

Two facts make the different-family option (B1 option (c)) material:
- B3 entered through a repair that followed the previous same-family Review's non-blocking suggestion (d837363 N3).
- B1 is the unenumerated sibling of the previous same-family Review's B1, which that Review's repair direction did not generalize.

## 13. D4 statement

No D4 is authorized. This NO-PASS accepts no architecture, product scope or default value. A later PASS would be technical evidence for G1 only. G1 also needs explicit stakeholder acceptance, and shadow D4 needs G2.
