# SSDS 8 Architecture Manual — Independent D3 Review, candidate d837363

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout /home/user/scientific-software-development-system)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: d83736390938aaca3ea224ac880e0f49b187e019
    SCOPE: the whole proposed Manual as durable D3 owner: (a) §21 and §16.2 closure; (b) fidelity to the
           Phase B-reviewed workplan, including refinements R1-R9; (c) out-of-matrix adequacy; (d) inheritance
           and capability transfer (Architecture 1.6.0, workplan §18, PEM HAS); (e) qualification design;
           (f) doctrine-realization map; (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob f6d1b5da89405776f3d6b41f37d2df5615010187 (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md, blob 0e8ef6bac67a0645cddb30c9866f01e8b5ca346b (verified)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23;
           Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b97fb8152d2a5742e17fa172e12204756, verified);
           blob at the candidate 91bde236465178f20c7348280e036d2884dfc216 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml)
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS (HYPOTHESIS ONLY): MANUAL-REVIEW-SSDS-8.0-CC005DB-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-C6DA678-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-B595F2C-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-6FF4ED1-NO-PASS.md; WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
    REVIEW METHOD: entry through source/roles/software-design/SKILL.md at the public source (entry contract, governing-version
           step and scientific checks from dist/skills/software-design/SKILL.md); owners read at the public source:
           architecture-and-design, abstraction-and-concretization, workflow-and-workplans (revision gates, product scope,
           Channel C), evidence-evolution-and-dependencies (assessment disagreement), convergence-and-cycle-economy
           (active simplification; review strategy after recurrence), protocol-versioning-and-compatibility (PC-001),
           scientific-checks fragment; full read of the Manual from a git-archive snapshot of the candidate; word diff
           cc005db..d837363; clause comparison of Manual §6 with workplan §6.6; constructed trajectories in the permissive
           and restrictive directions; G1 document checks executed
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session

Governing SSDP version for this Review: 7.2.1. The Manual's refinement table, decision markers, §30 pass and qualification claims, the closure map, commit messages, the handoff's scope text, workplan §0.1/§27 rationale, the diagnostic model's results, the stakeholder record's characterization of options and every prior Review record were treated as hypotheses. Section numbers refer to the Manual at the candidate unless prefixed "workplan".

## SERIOUS CHALLENGE

**None.** No accepted governing authority was found false, contradictory, ambiguous, inadequate or unrealizable. The evidence owner ("When competent evidence assessments materially conflict, preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence"), the workflow owner's D1/D2 revision-gate rule ("A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments, including those marked inapplicable, with their asserters. Acceptance does not ratify an assessment the gate was not shown.") and scientific checks e=5 are coherent and realizable here. SD-13 and SD-14 are realizable as directed: B2 below is a gap in realizing SD-13's guard, and B4 is a statement defect in realizing SD-14, not a defect in either direction. Every blocker is repairable at Manual sections without changing a parent.

## Verdict

**NO-PASS.** Four blockers survive.

- **B1** and **B2** are the eighth successive finding in the matching clause. Both enter through repairs of the cc005db Review's non-blocking findings N2 and N3, which followed that same-family reviewer's suggested directions. B1: reads of the "declared execution environment" were reclassified as configuration, so the environment appears in neither matching predicate, and a failure caused by a free environment attribute (a system BLAS, an interpreter, a compiler) is made stale by a run under another environment. B2: the new step that schedules an `ANALYZER_OUTPUT` before a recorded term counts as unresolvable makes `on⁻` depend on a later, host-dependent ledger record, which contradicts the SD-13 guard in the same paragraph.
- **B3** is new. A D1/D2 revision made by a human or absorbed from a foreign push never passes through an `AUTHOR` item, so its gate receives no revising-duty assessments and is not told that they are absent. §29.4 claims E0 ("only an `AUTHOR` item can change a D1-D3 unit by any route ... so the slot is always triggered"), which is false on these routes.
- **B4** is the fourth successive finding in the D1-D3 change rule. The SD-14 direction held against every route the cc005db Review found. Its statement, however, compares the recorded base `B` with the merged tree `M`, so every change admitted since `B` enters a candidate's write set. It also narrows SD-14's "declarations" to semantic declarations.

This verdict accepts nothing and authorizes no D4.

## 1. Blockers by earliest owner

### B1 — Environment reads escape the construction rule; a failure caused by a free environment attribute is made stale by a run under another environment (§6.3 executed content, §6.5 `ext`/`on⁺`, §6.6 (3), §17.1-§17.2; refinement R1; cc005db N2 repair)

**Mechanism.** §6.3 (new at this candidate): "Reads of the declared execution environment (interpreter, standard and system libraries, compilers and toolchain, which the realization records as configuration and the specification may fix, §17.1-§17.2) are configuration, not reads". §6.5 defines configuration as "its specification unit identity, regime, parameter instance, seed or replicate identity, and every execution attribute the specification fixes". `ext` compares only external pins and unpinnable reads. §17.1 makes the environment free by default ("Precision, backend and environment are fixed only when declared ... the default (free) is the conservative one for disagreement"). A free environment therefore appears in neither `conf(a⁻)` nor `on⁻` nor `on⁺`.

**Trajectory (D4 claim, declarative oracle, environment free; every step locally conforming).**
1. Specification `S` evidences claim `c`, and its `fixed` table declares no environment. The designated runner image links system BLAS `b1`. At admitted tree `T0`, a realization of `S` fails `l2_error` because of a defect in `b1`. The failure is assessed as `a⁻`, it counts, and the owner's adjudication obligation is derived.
2. The rerun obligation produces reproduction `r` on `T0` under the same image, and it fails identically, so (1) holds. No other run on `T0` exists, so (2) holds.
3. The operator updates the runner image to BLAS `b2`. This is operator state, visible only in later realizations' environment fields.
4. An `IMPLEMENT` item refactors a region in the recorded basis and integrates `T1`. The affected-evidence rerun `q` on `T1` under `b2` passes.
   - `on⁻(q, T1)` holds.
   - `ext(q, real(a⁻))` holds, because BLAS and interpreter reads are configuration: neither a pin nor an unpinnable read.
   - `bound(q)` holds, so (3) holds.
   - No yielding run on `T1` exists, so (4) holds.
5. `a⁻` is stale, `undisputed = T`, `ev = T` and `c` is valid. The adjudication obligation disappears. Nothing about content discriminated the failure; only the environment changed. A claim whose environment is free is asserted for every environment of its runner class, so it now has a live counterexample under `b1`, and that counterexample is hidden.

For a D1/D2 claim the floor still fired at step 1 (`adm` holds), but validity becomes `T` and the gate core lists the failure as stale, not disputed. The same dependency treated as an external input (vendored outside the tree, pinned) gives the opposite result under SD-12: `q` fails `ext`, and the failure goes to the owner. The boundary between the two classes ("standard and system libraries") is fixed by no recorded fact, and an unrecorded boundary decides which outcome applies.

**Violated text.**
- Manual §6.5 construction rule: "Every other dimension of "the same content" — external pins, unpinnable reads, completeness standing, the same root tree — appears only in `on⁺`'s further conjuncts. A dimension added later follows the same rule." Also: "An unfixed external input is execution variation (§6.2): ... permissively they are not, ... and a run observed in `G` stands for (3) only if it read the failing realization's pins."
- SD-12.
- The reviewed contract (workplan §6.6): executed content is "everything the realization's execution read ... every read the designated runner observed ... A read outside the governed tree is recorded by content identity where it can be pinned ...; one that cannot be pinned makes the execution's content its own, never `on` any other execution's, so it supports no mechanical stop (fail closed)".
- Phase B closure (BA7F738 U1): "executed content includes runtime inputs/observed reads".
- Evidence owner: "preserve the disagreement and route adjudication ... or obtain discriminating evidence"; "Do not suppress contradictory admissible observations to manufacture a pass".

The reclassification is a semantic change to the reviewed contract, in the permissive direction, and the R1 row of §0.3 does not list it.

**Earliest owner.** Manual §6.3 (the executed-content boundary) with §6.5 `on⁺`; R1.

**Minimum repair direction (subtractive in effect; no new record).** Apply the construction rule to this dimension. Every environment and toolchain attribute that the specification leaves free and the realization records (§17.2) enters `on⁺` as a conjunct (the same value as `real(a⁻)`), and never enters `on⁻`. An execution whose environment identity is not recorded at that granularity is treated as having an unpinnable read. The environment/external boundary then stops being material for soundness. State the classification in R1.

**Required discriminator.** Run the trajectory at the real owners. Expected:
- `a⁻` keeps counting, `undisputed = P`, and the adjudication obligation stays derived.
- A run on `T1` under `b1` can serve (3).
- The result is the same whether the library is classed as environment or as a pinned external input.
- An implementation that keeps a free environment out of `on⁺` must fail.

No §31.3 case varies the environment, so §31 passes with this defect.

### B2 — The SD-13 guard is not realized: re-resolution can depend on host inputs and on a later ledger record, and the record's system version is taken from its submission-time ruleset (§6.3 re-resolution and guard, §5.9, §14.5, §3.2; refinement R1; cc005db N3 repair)

**Mechanism.** The guard reads: "`on⁻(o, K)` is a function of `o`'s record and `K`'s bytes alone". The same paragraph (new at this candidate) reads: "Where a recorded term's frozen analyzer would need host inputs not recorded for `K` (§5.9), the Dispatcher first schedules an R0 `ANALYZER_OUTPUT` of that analyzer on `K`; only where none can be produced does the term count as matching for `on⁻`". §5.9 records as `ANALYZER_OUTPUT` the output of any analyzer "dependent on any input that key does not name (host headers, compilers, the build environment)". §14.5 has C++ preprocessing read host headers, and it delegates the parser choice. Three gaps follow.
- **(i) The pending window.** "Only where none can be produced" is not a ledger fact. Until an output is admitted, `on⁻` is not a function of `L_n` (C8), and an implementer must choose its value.
- **(ii) Host-dependent outputs.** Once an output is admitted, `on⁻` depends on a later record whose content is a function of the producing host, not of `K`'s bytes. No rule selects among several outputs for one key. The same unstated purity assumption reaches S0: `rev(u, T_n)` of a unit with such a term is computed from a recorded output that may not yet exist, or may exist with several values.
- **(iii) The system version's source.** §6.3 takes the system version "named in the record's `ruleset` (§3.2)", which §3.2 defines as "in force when submitted". The terms, however, were hashed "as in force at the realization's position". The two differ for any execution that straddles a system-version adoption, and long executions (up to 168 hours, or longer under external custody) make that ordinary.

**Trajectory for (ii) (D4 claim).**
1. `S` has `EXECUTION_DEPENDS_ON kern.solve = { file = "src/kern.cpp", symbol = "kern::solve" }`, and singleton completeness judgments are current. The C++ analyzer set `A1` resolves symbol spans after preprocessing with host headers, as §14.5 and §6.3 contemplate.
2. Realization `p` on `T0` passes. Its term was hashed from host `H1`'s `A1` output.
3. A human-gated `RULESET_ADOPTION` adopts analyzer set `A2`.
4. A candidate edits `kern::helper` in the same file, giving `T1`. `a⁻` fails on `T1` (a race in `solve`, whose bytes are unchanged).
5. (2) needs `on⁻(p, T1)`, which needs `A1` on `T1`. No output exists, so one is scheduled. Host `H2`, whose system headers have been updated, produces it. A header macro changes `solve`'s resolved extent, or a host-conditional `#if` makes it `ABSENT`. Then `cid ≠ c`, and `p` leaves (2).
6. A reproduction on `T1` fails identically, so (1) and (2) hold. After a later change, (3) and (4) hold, and `a⁻` is stale. A nondeterministic failure of byte-unchanged code has lapsed.

**Trajectory for (iii).** `p` starts at position `m` under system version `V1`. A `RULESET_ADOPTION` of `V2` (a normalization that removes byte-order marks) is admitted at `m+5`. `p` is submitted at `m+20`, so its `ruleset` names `V2`. Re-resolving under `V2` a recorded file that carries a byte-order mark gives `cid ≠ c` even on `tree(p)`, so `p` is `on⁻` of no tree. That is exactly the cc005db B2 consequence; for a failing realization, `adm(a⁻)` turns false and the floor cannot fire.

**Violated text.**
- The guard (above) and "every semantics used to resolve and hash a recorded term is the one named in `o`'s record".
- §6.6: "a run on content that differs from `tree(a⁻)` only in another span of a recorded file ... stays in (2)"; "(1) and (2) need an identical second execution on the content `a⁻` read and no other outcome there, ever".
- C2 and C8 ("one value per predicate for every admitted input").
- Phase B closure: "nondeterministic old-content observations defeat (2)".
- SD-13: "re-resolve each recorded term under the system version named in its own record and state the guard that the adverse predicate depends only on the record and the compared content's bytes".

**Earliest owner.** Manual §6.3 (resolution context, re-resolution and guard), together with the §5.9 analyzer contract and §14.5.

**Minimum repair direction (subtractive).**
- Every scope-term resolver is a pure function of file bytes under the analyzer identity and configuration that the ruleset pins. A `symbol` term whose span would need host inputs is inadmissible; such spans use `anchor`, `heading` or whole-file terms. This is the c6da678 N6 option the cycle did not take, and it also settles S0.
- Delete the scheduling sentence and its fallback.
- Record the resolution context by value in the execution basis, computed together with the terms (system ruleset identity, `ignore`, analyzer set), never inferred from the envelope `ruleset`.

If host-dependent resolution must stay, the deterministic alternative is: such a term always matches for `on⁻`, and matches for `on⁺` and currency only on the same root tree, with the cost disclosed. S0 then still needs a stated rule for revisions.

**Required discriminator.**
- (a) Two hosts with different header sets give the same `on⁻` and the same `rev` for one recorded term on one `K`. An analyzer whose span resolution reads host headers is refused at qualification.
- (b) In the straddling-adoption case, `p` stays `on⁻ tree(p)`.
- (c) Derivation at a position with no output for `K` gives one value, which no later record changes.

§31.2's analyzer-pinning case varies only the installed analyzer version, and §31.3's guard case varies only ledger inputs, so §31 passes with this defect.

### B3 — D1/D2 revisions not made through an `AUTHOR` item reach their gate without the revising duty's assessments and without any visible absence (§12.3 human write scope, §8.6 and §18 absorption, §16.3 injection, §16.6 section 3, §29.4)

**Mechanism.** §12.3 lets the human role write "any content as ordinary change". §18.1 treats a manual edit or foreign push as intake, and §8.6 absorbs it: "foreign semantic content changes revisions". The revising and tension-search duties are injected only for "`AUTHOR` revising D1/D2 authority" (§16.3), and the `revision_assessments` slot exists only on `AUTHOR` items (§13.5). §16.6 section 3 renders "that revision's tension applicability assessments", and it says nothing when there are none.

**Trajectory.**
1. D2 subject `numerics.method` is accepted at `r1`. A recorded tension `t` (an in-repository `CHALLENGES` home) is bound to `numerics.impl`, an accepted concretization of it.
2. A human edits the D2 text directly, or a foreign push carrying such an edit is absorbed. The revision is now `r2`, made by no `AUTHOR` item.
3. `ACCEPT` and `GATE` obligations follow. The `ACCEPT` brief carries the D2 reference owner but not the revising duty.
4. Gate core section 3 is empty, and nothing marks it missing. The relying tension search of section 1 concerns tensions against the authority relied on, not tensions bound to the D2 subject's concretizations, so `t` is never shown.
5. Admission's refusal rule does not fire, so the gate holder may `ACCEPT` unqualified. A D2 revision is accepted, unqualified, by a gate that was never shown `t` and never told that no assessment exists.

Revisions adopted through intake take the same route.

**Violated text.**
- Workflow owner: "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments ... Acceptance does not ratify an assessment the gate was not shown."
- Scientific checks e=5: "In the revision's own record and its gate evidence, record the predecessor identity and, per found tension, a revision-scoped applicability assessment".
- Manual §29.4: "**E0** (only an `AUTHOR` item can change a D1-D3 unit by any route, because the write set is keyed on effect, ... so the slot is always triggered; the gate core renders the assessments, §16.6)". This claim is false for the human, absorption and adoption routes.
- SD-6: "Every realization claim stays bounded to its mechanism and its evidence".

**Earliest owner.** Manual §16.6 (gate core, §21 item 10) and §29.4 (§21 item 27).

**Minimum repair direction.** Bound the E0 claim to agent-produced revisions. For any D1/D2 revision with no `revision_assessments` record, §16.6 section 3 states "no revising-duty assessment recorded" and names the route that produced the revision. That way the gate knows what it was not shown. Stronger treatment is a stakeholder choice:
- **(b)** classify the absence as a missing record of material uncertainty, so that Admission refuses an `UNQUALIFIED` `ACCEPT`;
- **(c)** inject the revising and tension-search duties and the `revision_assessments` slot into the `ACCEPT` obligation of every D1/D2 revision not produced by an `AUTHOR` item, with the assessments marked proposed and attributed to their asserter.

SD-14 declined a gate backstop for the agent route, which the effect-keyed write set now covers; these routes were not before the stakeholder then.

**Required discriminator.** Run a human-authored and an absorbed D2 revision. Expected: section 3 shows the absence, and under (b) or (c) the corresponding refusal or duty follows. An implementation that renders an empty section 3 must fail. §31.5 exercises items only.

### B4 — The effect-keyed write set compares the wrong trees and narrows SD-14's "declarations" (§1.2, §8.3 step 3, §14.1, §14.3 `write_scope`, §13.2; SD-14)

**(a) Comparison endpoints.** §1.2: "The write set of a change from base tree `B` under `Σ_n` to merged tree `M` under `Σ_n ⊕ Δ_Σ(X)`". `B` is `X`'s recorded base (§7.1), and `M` is the merge onto the current head `T_n` (§7.2). When `T_n ≠ B`, the comparison includes every change admitted since `B`, and three readings are available:
- **Literal reading.** An `IMPLEMENT` result whose base predates a concurrent `AUTHOR` admission on a D2 unit has that D2 unit in its write set. Its request is rejected at step 3 (`AUTH_WRITE_SCOPE`, before the step-6 currency check that would route it to revalidation), and conformance reports a `write_scope` `VIOLATION` plus an undisclosed-breach `DISCREPANCY` against its route. Every concurrent admission outside the item's scope does the same. That contradicts §9.1 ("A request whose basis was overtaken is revalidated ... never rejected outright") and makes concurrent work unadmittable.
- **Base-to-candidate reading.** The other reading an implementer can take from "computed by the comparison that computes `Δ(X)`" is `B` against `C`. It misses effects that arise only in combination. Item `i1` removes `numerics/extra/` from `ignore` where `B` holds no file there. Concurrently admitted item `i2` adds ignored files under that directory. Neither write set contains a D2 unit, yet integrating both gives the D2 prefix unit `numerics` new content without an `AUTHOR` item. This is the cc005db B1 trajectory A, split across concurrent items.
- **Head-to-merged reading.** Only `T_n` under `Σ_n` against `M` under `Σ_n ⊕ Δ_Σ(X)`, at the head where the check runs, gives both properties.

**(b) Key coverage.** SD-14 reads "every unit whose owned content, declarations, regions, membership or signature actually differs". §1.2 lists "the semantic declarations it or any of its parts carries". A D1/D2 unit's `renamed_from` (identity lineage, read by §1.11 `locate`, by `ask(tensions)` for predecessors and by evidence-obligation lineage in §10.2) is in no listed category. An `IMPLEMENT` or `DOCUMENT` item with `ssds.manifest` in scope can therefore add or remove it, although the cc005db attribution placed every declaration key in the write set. Scientific checks e=5 lists renaming and merging as revising acts. Adding a lineage merges histories (restrictive). Whether removing one hides predecessor-bound tensions from a later revision's search depends on whether lineage is read from current `Σ` or from ledger history, and §1.11 does not say.

**Violated text.**
- §9.1 (above).
- §13.2: "no change to a D1-D3 unit's owned content, semantic declarations, regions, membership or signature, by whatever route ... can happen except through an `AUTHOR` item".
- SD-14 ("declarations").
- K1.

**Earliest owner.** Manual §1.2.

**Convergence.** This is the fourth successive finding in this family (`b595f2c` B3, `c6da678` B3, `cc005db` B1, this one). SD-14's direction held against every route the previous Review named (`ignore` changes, new parts, moved units, other units' declarations), each checked in §6 below. The present defects are clean local errors in its statement and need no new mechanism.

**Minimum repair direction.**
- Compare `T_n` under `Σ_n` with `M` under `Σ_n ⊕ Δ_Σ(X)` at the head where each check runs, including conformance in `D_n[X]`.
- Include every declaration key of a unit.
- Say that lineage is a fold over admitted history.

**Required discriminator.**
- (a) A concurrent admission outside an `IMPLEMENT` item's scope never enters that item's write set; its result is admitted or revalidated, never refused with `AUTH_WRITE_SCOPE`.
- (b) The two-item `ignore` trajectory is a `VIOLATION` for whichever item integrates second.
- (c) An `IMPLEMENT` item that changes only a D2 unit's `renamed_from` is a `VIOLATION`.

§31.5's cases run single items against an unmoved head, so they pass with both defects.

### Family-level convergence assessment (B1, B2) and options

The matching clause has now produced findings in eight successive reviews: `ef8445a` N2, `552ac01` N2, Phase B N2, `6ff4ed1` B1, `b595f2c` B1, `c6da678` B1, `cc005db` B2, and B1/B2 here. Each finding is a dimension of "what the execution read" that sits outside the rule protecting matching:
- effective structure;
- recording granularity;
- external inputs;
- system-version semantics;
- now the environment and the host inputs of resolvers.

SD-12's construction rule and SD-13's guard are the right family-level invariants. They have held against every attack below that routes through them. Both new defects were introduced by repairs of non-blocking findings (cc005db N2 and N3), and each repair added a carve-out or a mechanism without routing it through those invariants. The cause is local; the recurrence pattern is not. The repair directions above remove mechanism (the scheduling step) or reuse the existing rule (the environment as an `on⁺` conjunct).

**Options for the stakeholder (Phase C handoff §5):**
- **(a) Subtractive (recommended):** the B1 and B2 repairs above, with a rule that any future boundary or resolver classification is stated only through the construction rule and the guard.
- **(b) Subtractive plus restriction:** in addition, mechanical staleness is available only for specifications that fix their environment and whose execution basis holds only host-independent terms; every other failure goes to the owner.
- **(c) A different-family Review before or after the repair:** every Manual reviewer has shared the author's family, and both new defects came from same-family suggestions.
- **(d) Reconsideration above §6.6:** for example, judgment-only staleness for failures whose execution basis carries any unrecorded execution dimension.

## 2. Non-blocking findings

- **N1 — Nested subjects of another domain (§1.2, §1.5, §19.4).**
  - `content(u, T)` and `sem(u, T)` of a composite include its nested subjects' bytes and declarations, but the write set lists "the bytes it owns by innermost ownership". A D1/D2 composite's revision therefore changes, with no `AUTHOR` item, when a nested D4 subject changes, while the same paragraph says the set "is computed by the comparison that computes `Δ(X)`", which is keyed on revision.
  - Under the list reading the D1/D2 gate re-accepts a revision whose own content is unchanged. Under the `Δ(X)` reading no item kind can ever edit the nested subject.
  - State which reading applies, phrase §13.2 and §29.4 as "owned content", and have the gate core say when only nested content changed.
- **N2 — Cross-kind structural changes have no agent item route (§1.2, §13.2, §19.4-§19.5).** Under the effect-keyed set a unit losing bytes or members is in the write set, and an `AUTHOR` scope admits units of one kind only. No item can therefore:
  - nest a D4 subject in a D2 composite;
  - carve a D1/D2 subject out of D4 content;
  - classify `ssds.unclassified` content as D2.

  This is restrictive and may be intended (release by the old owner), but §19.5's bottom-up path names no route. State it (human-authored, or adopted under a disposition qualified for both domains).
- **N3 — `QUARANTINE` effect and intake residue (§5.5 `ok`, §18.4; cc005db N5 residue).**
  - "until a later disposition stands" conflicts with `ok`'s "standing `QUARANTINE`": a later disposition ends nothing unless it supersedes the quarantine as the owner's adjudication.
  - "Under" is undefined for a structural delta and for content later moved or deleted.
  - Admission should restrict `INTAKE_DISPOSITION` targets to intake objects that carry an `INTAKE` obligation; otherwise any reviewer task can invalidate any subject until the owner adjudicates.
  - An adverse disposition that stands first still loses to a later enacting `ABSORB` not bound to the answered obligation. Only the later-adverse order is specified.
- **N4 — A re-identifying system-version adoption also withdraws reading coverage (§6.6 coverage, §27.3).** "While `G`'s reading is the one `d` read under" compares readings by revision identity, so a normalization change resurrects settled assessor-read failures without any content change (restrictive). Disclose it alongside §27.3's re-acceptance burden, or compare readings under the record's system version.
- **N5 — The `ssds.manifest` exclusion (§1.2).** When another unit is in the write set, a manifest change whose only effect falls on the uncovered region (no catch-all declared) is invisible to every write-scope check. Minor.
- **N6 — Stale statements.**
  - The R1 row's first sentence still gives the resolution context as "the `ignore` patterns and the analyzer set"; the rest of the row and §6.3 include the system version.
  - §30's "The §6 family is unchanged in mechanism" omits the scheduling step and the environment classification.
  - §32.2's external-input residual omits the environment (B1).
- **N7 — Slot structure (§13.5, §16.5).** The new definition of a resolved finding ("records it resolved in its `findings` slot") has no field in the `findings` slot. e=5's predecessor identity has no place in `revision_assessments` or gate section 3.
- **N8 — Closure map (aid only).** Item 23 says "declarations", broader than the Manual's "semantic declarations". Items 4-5, 10, 23-24 and 27 rely on text affected by B1-B4.

## 3. Closure audit (§21 items and §16.2 rows)

The closure map was used to locate text only, and its annotations were checked against the Manual.

**Not substantively resolved:**
- items 4 and 5: the executed-content boundary for the environment (B1); re-resolution, the analyzer contract and the guard (B2);
- items 23 and 24: the write-scope rules and domain rule over the write set (B4);
- item 10: gate templates meeting Channel C for D1/D2 revision gates (B3);
- item 27: the §29.4 revising row (B3).

**Resolved with non-blocking defects:**
- item 1 (nested subjects in the write set, N1);
- item 12 (`QUARANTINE` wording and the earlier-adverse `ABSORB`, N3);
- item 13 (cross-kind route, N2);
- item 18 (reading coverage under re-identification, N4);
- item 26 (the finding-resolution slot, N7).

**Resolved:**
- items 2, 3 (the cc005db B3 repair is sound), 6-9, 11, 14-17, 19-22 and 25;
- item 7: `REFUSED` named; three-valued discharge extended by R9 with that change surfaced.

Each decision was located, and each is a decision rather than a route. Delegated D4 space is bounded. Nothing incidental is over-specified to a blocking degree, except that the parser choice is delegated without the purity constraint B2 needs.

**§16.2:** every row of both workplan tables, including every Deferred row (invariants 4, 9, 15, 17 and 26; surfaces §5, §6, §7, §9-§11, §12 and §18), has a final disposition in §26.4, with §26.2-§26.3 for the substance. None found unresolved.

## 4. Refinements R1-R9

| # | Assessment |
|---|---|
| R1 | **Unsound in two dimensions; sound otherwise.** The polarity rule held against every route below: `on⁻` reads only tree-resident terms, pins and unpinnable reads enter only `on⁺`, completeness enters only positively, and `on⁺ ⇒ on⁻` holds. The record-named system version closes cc005db B2 for terms hashed and named consistently. Against the rule itself, the environment classification (B1) is a semantic change that is not surfaced, and the scheduling step contradicts the guard (B2). |
| R2 | **Sound.** Clamping every non-trivial strongly connected component only lowers values, and `vetoed`, `stands⁻` and the new `ok` term are S0/S1 constants. |
| R3 | **Sound.** |
| R4 | **Sound.** The failure points were re-checked at text level, and the VM-snapshot residual is disclosed. |
| R5, R6, R7 | **Sound.** |
| R8 | **Sound.** |
| R9 | **Sound, with residue.** The cc005db B3 repair (the gate holder's own `PRODUCT_SCOPE_ACCEPTANCE`) makes every surface acceptance one kind: both orders veto, derive the owner's adjudication, and leave the gate's revision acceptance untouched. The intake residue is N3. |

## 5. Previous findings, Phase B closures and N1-N4

**cc005db.**
- B1 is **closed** for its three routes. The `ignore`-driven prefix gain or loss, a new part (now carrying its composite's kind) and a moved D4 unit (in the set under both kinds) are all in the write set. The family continues as B4.
- B2 is **closed in mechanism** (re-resolution under the record's system version, so normalization and anchor-table changes no longer alter `on⁻`). Its residues are B2 (iii) and (i)-(ii).
- B3 is **closed**.
- N1 closed. N2 repaired, but the repair introduced B1. N3 repaired, but the repair introduced B2. N4 closed (term-level resolution). N5 partly closed (N3 here). N6 closed (resolution defined; slot residue N7). N7 closed (disclosed in §27.3; residue N4). N8 updated; inherits N8 here.

**c6da678.**
- B1 is **closed** for pins and unpinnable reads; B1 here is its environment sibling.
- B2 is **closed**.
- B3 is **closed** by SD-14, with residue B4.
- N1, N3, N4, N5 and N7-N12 closed. N2 closed (intake and product scope are same-kind), with residue N3. N6 reopened as B2 through the cc005db N3 repair.

**b595f2c.**
- B1 is **closed**: the granularity trajectory holds with Python `symbol` terms (pure resolvers), but not with host-dependent C++ resolution (B2).
- B2 is closed. B3 is closed (`DOCUMENT` scopes), with residue B3 and B4 here. B4 is closed (R9).
- N1-N8 closed: N1 the machinery `COMPLETENESS` producer; N2 host-dependent output recorded, re-resolution being B2; N3 the analyzer set in `RULESET_ADOPTION`; N4 SD-12; N5 the §31.2 list; N6 §13.3 "whatever its kind"; N7 §30; N8 the domain rule's undefined term removed.

**6ff4ed1.**
- B1 is **closed** (frozen terms). B2 is **closed** (prose byte identity). B3 is **closed** for the analyzer version; host inputs lying outside the pin are B2. B4 is **closed**.
- N1-N12 closed as checked against the text.

**Phase B §3 closures.** Clause comparison of §5.3-§6.10 with workplan §6.6 found the predicates restated, and in R1's direction only narrowed permissively or widened adversely: S1 polarity, `cont`, `base`, `ev`, `undisputed`, `qual`, `about`/`starts`/`home`, Y1/Y2 coverage, the class rule's candidate-own exception, absorbed-reading exclusion, never-lost salvage, independence, unknown authorship, retirement/split/retarget and `eff`. Two exceptions:
- "executed content includes runtime inputs/observed reads" is narrowed for environment reads (B1);
- "nondeterministic old-content observations defeat (2)" fails under host-dependent resolution (B2).

**Phase B N2 re-test.** The bounding completeness judgment was taken through `P`, blocked, revoked, superseded, loss-withheld and vetoed by an `INCOMPLETE`, against a differing old-content run on an alternate tree that differs only outside the recorded regions (including another span of a recorded file) and a yielding present-content run. The first stays in (2) and the second in (4), because `on⁻` reads no S2 value, no current `Σ`, `ignore`, analyzer, system version or pin. That holds, except under B2. The support-cycle clamp (R2) and the corrupt-prefix halt (R3) are specified fail-closed before any current assertion.

**Phase B N1, N3, N4.** N1 remains open and disclosed (§32.2). The N3 limits are carried in §31.3. The N4 costs are in §32.3.

**Both directions.**
- Permissive: B1 and B2 hide live failures; B3 lets a D1/D2 gate accept without, and unaware of, the revising assessments; B4 (base-to-candidate reading) misses combined effects.
- Restrictive: B4 (literal reading) blocks concurrent work; N1 (one reading), N2, N3 (the `QUARANTINE` lever) and N4 (coverage withdrawn by an adoption).
- Nothing else resurrected a settled failure or withdrew a stop without cause.

## 6. Out-of-matrix trajectories attempted

**Broke the candidate:**
- B1: a BLAS, interpreter or compiler change between reproduction and the frame run.
- B2: a host-header change under a C++ `symbol` term across an analyzer adoption; an execution straddling a system-version adoption.
- B3: a human-authored or absorbed D2 revision at its gate.
- B4: a concurrent admission outside an item's scope (literal reading); a two-item `ignore` split (base-to-candidate reading); a `renamed_from`-only edit.
- N1: a nested D4 subject in a D2 composite.
- N2: carving or nesting across kinds.
- N3: a reviewer-issued `QUARANTINE` on arbitrary content; adverse-then-`ABSORB`.
- N4: a normalization adoption under a standing discriminating reading.

**Held:**
- **SD-13 guard against ledger inputs:**
  - policy change; structural adoption (byte-preserving refinement, `ignore` change, re-scope); analyzer adoption with a pure resolver;
  - completeness lost six ways; loss boundary; frames and rebases (`tree(a⁻)` fixed);
  - normalization and anchor-table changes for consistently named records.
- **SD-12 rule:** the c6da678 external-input trajectory; unpinnable-read variants (in (2) and (4), never in `on⁺`); a fix that stops reading the locator.
- **Granularity:** another span of a recorded file; another unit's file in a bounded closure; an ignored file under a widened directory (all leave `on⁻` unchanged). A governed file under a widened directory and a prefix gaining a file both change it, as the reviewed `on` requires.
- **One representation:** currency (`execution` entries), (1)-(4), `adm`, the floor and the class rule all read one record. Every `on⁻` use is adverse and every `on⁺` use permissive. Unresolvable-term fallbacks differ by polarity, so `on⁺ ⇒ on⁻` is kept.
- **Derivation:** the veto, `stands⁻` and `ok` read S0/S1 only; the support graph keeps its completeness and `execution` edges; the cycle clamp holds.
- **Effect-keyed write set:** `ignore` moving bytes into or out of a D2 prefix; a new part with or without a semantic table; a D4 unit moved into a D2 composite; another unit's `part_of` naming a D2 composite; a D2 part's own semantic table. Each is a `VIOLATION` for non-`AUTHOR` items, against an unmoved head.
- **R9:** product-scope rejection versus a gate holder's acceptance in both orders; peer supersession rejected; an answered obligation never re-dispatched; a reviewer result without its `TASK_RESULT` or with an empty `bidirectional` slot.
- **Publication, currentness, gates and floors:** the R4 failure points; settlement before human decisions; the ABA residual; a floor item cannot be reclassified; an unqualified gate `ACCEPT` is refused while disputed evidence is listed.

## 7. Minimum architecture and capability transfer

No component, tier or record kind is added. This candidate did add two mechanisms in the §6 family, which §30 does not mention:
- the environment classification;
- the `ANALYZER_OUTPUT` scheduling step.

It also added one input to `ok` (a standing `QUARANTINE`). The recommended repairs remove the scheduling step and reuse the existing construction rule. SD-14 replaced the attribution rule with an existing comparison, which is minimal once B4's endpoints are fixed. The removals (R4, R5) drop no owner-required capability.

**Capability transfer.**
- The 1.6.0 transfer in §26.4 is complete.
- PC-001 (`AUTHORITY_BOUND`) was independently resolved at the public source ("When a new profile becomes current, every older supported profile remains frozen and independently testable."). It is preserved: Core imports nothing from SSDS (§26.2), §31.8 tests Core without SSDS, and the frozen 1.6.0 file, `source/` and `dist/` are byte-unchanged.
- Workplan §18 was spot-checked against the Manual. The only capability narrowed is the Phase B "runtime inputs/observed reads" closure, for environment reads (B1).

**PEM basis.** `origin/main` is `af0455753e20ee54a969c844872e29e270007211`, PEM blob `1561797125622f355f84eb27319f87e8fa4227d9`, identical at the candidate. `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md` reports "PEM schema 1 valid: 5 families, 0 notices". HAS dispositions:
- PC-001: applicable and binding;
- DS-001: applicable as evidence only; it bears on §8 below;
- SP-001, SP-002 and FF-001: applicable as evidence only.

## 8. Qualification design

§31 binds claims to real owners and marks every runtime group UNEXECUTED; nothing beyond §31.10 is claimed as executed. Green §31 fixtures can coexist with all four blockers (DS-001):
- no §31.3 case varies the environment (B1);
- §31.2 varies installed analyzer versions and §31.3's guard case varies only ledger inputs, never host inputs or a straddling adoption (B2);
- §31.5 exercises `AUTHOR` items only, never a human-authored or absorbed D1/D2 revision at its gate (B3);
- §31.5's write-set cases run single items against an unmoved head (B4).

The four discriminators in §1 are required. The new matching-guard case is correct for the dimensions it varies. The §14.7 `HARD` qualification design is adequate as design, with proposed-default values. The diagnostic model was not run; it is unchanged since Phase B and models neither environments, analyzers nor write sets.

## 9. Doctrine-realization map and O1

The E0/E1 claims are tied to existing mechanisms, except:
- §29.4's revising row, which is false on the human, absorption and adoption routes (B3);
- §29.5's documentation row, whose clause "authority text changes only through `AUTHOR`" holds only for agent work (the duty concerns documentation agents, so bounding the clause suffices).

The bidirectional E2 claim has a carrier and an admission check. The disclosed-E3 list (§29.6) is appropriately conservative, and the enumeration is complete with its catch-all row.

O1 (§0.5) states the realized record, readers, routine questions, the realized-record architecture and the marked surfaces. "Beyond the requested deliverable: None" is consistent with the stakeholder record. Technical Review accepts no marked item, product scope or default value.

## 10. What was verified and how; what was not

**Executed** against a `git archive` snapshot of the candidate under `/tmp/ssds80-manual-review-d837363/snap`, and against the repository:
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- `git diff --check cc005dba… d8373639…`: clean.
- `git diff --stat fad3ee41… d8373639…`: 14 files. These are:
  - the Manual and the closure map;
  - four Manual review handoffs and four NO-PASS records;
  - the Phase C handoff;
  - a one-line session-handoff change;
  - ten lines in the stakeholder record (SD-11 to SD-14);
  - two index lines.

  The cc005db..d837363 diff touches the Manual, the closure map, the cc005db handoff and record, and the stakeholder record (SD-13, SD-14).
- `orchestrator/docs/architecture.md` (blob `39e6de7…`), `source/` (tree `fac2238…`) and `dist/` (tree `6bf729e…`) are identical at `fad3ee4…` and the candidate.
- All header blobs match. PEM was validated as in §7.

**Read** at the public source, as listed in the header.

**Not verified:**
- any runtime behavior (none exists); the trajectories are deductions from the specified contracts, not executed probes;
- the diagnostic model (not run);
- empirical costs;
- workplan §27 history and the earlier workplan NO-PASS records beyond the Phase B record's and Phase C handoff's summaries;
- D1, D2 and specialist entrypoint texts beyond the scientific-checks fragment and the Manual's citations;
- whether real C++ analyzers resolve symbol spans host-dependently, which B2 rests on only because the Manual permits it.

## 11. Scientific-checks answers

- **Material findings:** B1-B4 and N1-N8 above. No agents were launched. The tools used (git, the unit test, the PEM validator) produced no further findings.
- **Realized results:** this Review, including the tools it ran, produced, ran and reviewed no realized scientific results, and it prepared no gate evidence. Its output is D3 review evidence toward G1. Null envelope:
  - *Examined:* the Manual in full; the cc005db..d837363 diff; the closure map; workplan §6.6, §7.5-§7.6, §16.2, §18 and §21; the cc005db Review in full and the c6da678, b595f2c and 6ff4ed1 finding lists; the Phase B Review §3-§4; Phase C handoff §5; the stakeholder record (SD-1 to SD-14); PEM identities and PC-001/DS-001; the governing owners in the header.
  - *Materially not examined:* workplan §27 and other sections not listed; the earlier workplan NO-PASS records; the diagnostic model's source; D1, D2 and D4 entrypoint texts beyond the scientific-checks fragment; any runtime system.
  - *Materiality basis:* decision relevance to G1 closure and to the Manual's §0.4 invariants.
- **Variants:** no analysis, pipeline, preprocessing, model or parameter variant was evaluated or selected (count 0). Constructed trajectories are review hypotheses. The repair options are proposals for the stakeholder, not a selected survivor. There was no delegated or resumed work.
- **Tension search:** not triggered. No consequential judgment relied on accepted project D1/D2 authority. The authorities used are SSDP 7.2.1 process owners, the stakeholder record and the reviewed workplan.

## 12. Common-mode note

This reviewer shares the Manual author's model family (Claude). It was launched by the authoring session from the issued handoff, and it shares the corpus, the inherited workplan framing and the toolchain. Fresh context is not epistemic independence. All five Manual reviewers have been of this family; the Phase B reviewer was of the GPT family. B1 and B2 entered through repairs that followed the previous same-family reviewer's non-blocking suggestions (cc005db N2, N3). That is direct evidence of common-mode risk, and it makes the different-family option (c) in §1 material.

## 13. D4 statement

No D4 is authorized. This NO-PASS accepts no architecture, product scope or default value. A later PASS would be technical evidence for G1 only. G1 also needs explicit stakeholder acceptance, and shadow D4 needs G2.
