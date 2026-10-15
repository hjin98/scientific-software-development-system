# SSDS 8 Architecture Manual — Independent D3 Review, candidate 5c55d4b

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 5c55d4b2a741fa10fe499697a5c2fee0f17f0c1e
    SCOPE: whole proposed Manual as the durable D3 owner: (a) §21/§16.2 closure, (b) fidelity and
           refinements R1-R11, (c) out-of-matrix adequacy, (d) inheritance and capability transfer,
           (e) qualification design, (f) doctrine-realization map, (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: 27b1c61f9ce009049dcd36c7d360f9911403b87f (checked)
    CLOSURE MAP BLOB: 79eee92121b1b6755294c8a01afd3e65cabc563a (review aid only; checked)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; Phase B candidate e23f14208be869e6a78cfd7b312e447254ee1851
           (blob 610f373b97fb8152d2a5742e17fa172e12204756, checked); blob at this candidate
           91bde236465178f20c7348280e036d2884dfc216 (checked; unchanged since 27ef339)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
           (both confirmed in PROTOCOL-RELEASE-STATE.yaml at the candidate, accepted_current 7.2.1)
    PRIOR REVIEWS, HYPOTHESIS ONLY: E23F142 Phase B PASS; Manual NO-PASS records 6FF4ED1, B595F2C,
           C6DA678, CC005DB, D837363, 53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98, E2154AC,
           E9E6E9F, A18B544, 0B6C4FA, 27EF339
    REVIEW METHOD: D3 role entered at the governing public source; whole-Manual read at the exact
           candidate (git archive snapshot); deductive counterexamples in both polarities; family-level
           search after recurrence (convergence owner; handoff method step 6a), attacking hardest the
           clauses changed since 27ef339 and the repairs of that round's non-blocking findings;
           prior-finding regression; required structural checks; no implementation or runtime qualification
    REVIEWER: Claude model family (the same family as the Manual's author); a fresh-context
           sub-agent launched by the authoring session from the named handoff; no authoring
           conversation received
    MUTATION BOUNDARY: this record only; no commit or push

Governing SSDP version for this task: 7.2.1.

All Manual section references are to the exact candidate. The checkout HEAD was the later handoff commit `b0a81ce`, which differs from the candidate only by the handoff file. Governing owners were read at `aaeaf8b…`:

- `source/roles/software-design/SKILL.md` and its expanded `dist/skills/software-design/SKILL.md` (entry contract and scientific checks);
- `architecture-and-design.md` and `abstraction-and-concretization.md` ("Feasibility, authority, and delegation", "Verification and Challenge");
- `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review readiness and independent review sufficiency", "Review strategy after recurrence");
- the cited paragraphs of `evidence-evolution-and-dependencies.md`.

The other concern owners were not loaded: no decision below turned on them.

## SERIOUS CHALLENGE

**None against accepted SSDP 7.2.1 or the frozen Architecture 1.6.0 / Level 0 Core.** Both blockers are defects of the proposed D3 concretization. The workplan and the Manual are proposed architecture, so a gap between them, or between the Manual and a stakeholder direction, is not a challenge to accepted authority.

Owner text applied:

- D3 owner, "D3 boundary and feasibility": "A D3 candidate is admissible only when it satisfies every applicable D1/D2 invariant and directly governed security, reliability, compatibility, resource, performance/scaling, deployment and external-interface constraint."
- D3 role entrypoint: "D3 contradictory/ambiguous/inadequate/unrealizable -> SERIOUS CHALLENGE to D3". Applied to proposed D3, it yields blockers, not a challenge to accepted authority.
- Evidence owner: "Do not suppress contradictory admissible observations to manufacture a pass or a positive project-learning pattern."
- Evidence owner: "When competent evidence assessments materially conflict, preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence."
- Convergence owner, "Review strategy after recurrence": "A clean local repair that genuinely closes the cause remains sufficient; recurrence does not automatically force redesign."

## Verdict

**NO-PASS.** Two D3 blockers survive, each stated at family level as method step 6a requires.

- **B1 — matching family (assessment disagreement, recorded execution basis); entered through the repair of 27ef339 N1.**
  - The new disjunct of condition (1) lets a reproduction on the identical tree serve (1) whatever width it recorded.
  - Before it, any stop needed a bounded reproduction, whose narrow record `link⁻` uses to reach every differing run on equivalent content.
  - Now a failure recorded `UNBOUNDED`, reproduced only by `UNBOUNDED` runs on its own tree, has no narrow record of its content anywhere. Its (2) reaches only the identical tree. A differing run on a tree that differs only in a file nobody read is hidden, and the failure is made stale once a later judgment bounds a passing run on fixed content.
  - The cause is the one the last three records named: one recorded width serves both polarities.
- **B2 — D1-D3 change-rule family (effect-keyed write set); residue of 27ef339 B2, a clean local defect.**
  - The byte-attribution clause is repaired. But §1.2 still puts in the write set every unit whose "resolved regions" differ between `T_n` and `M_n(X)`.
  - §1.3 defines regions as byte regions, and §1.2 says the set "is computed like the governance-affecting classification (§1.6)", which compares "the set of governed byte regions".
  - Read literally, a length-changing D4 edit above a D2 span in the same file shifts the D2 region, so the item is a `VIOLATION`. The same holds for a narrowly scoped part followed by a sibling or residual, and for a D2 edit nested in a D3 whole-file composite, whose residual part shifts.
  - §31.2 (C), the composite sentence of §1.2 and SD-14's "actually differs" presuppose a reading in which positions do not count. An implementer must choose.

The 27ef339-round repairs otherwise close what they target:
- `link⁻` closes 27ef339 B1 and its siblings (ii-a), (ii-b) and (ii-c) for every **bounded** failure;
- the frame declaration closes 27ef339 B3 (gated changes can integrate);
- N4, N5 (evasion), N6 and N7 are closed.

The other repaired non-blocking findings leave the residues listed below. This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blockers by earliest owner

### B1 — An unbounded failure reproduced only on its own tree has no narrow record, so (2) cannot see a differing run on equivalent content, and the failure is made stale

**Earliest owner.** Manual §6.6 condition (1) (the disjunct "or with `tree(o) = tree(a⁻)` ∧ `ext(o, real(a⁻))` (an identical tree needs no bound)"), with §6.5's construction rule and `link⁻`, and §6.9 scheduling. These are workplan §21 items 4 and 5. It is a D3 defect and asks for no new D1/D2 rule.

**Owner and contract text.**
- Evidence owner (quoted above): do not suppress contradictory admissible observations to manufacture a pass; preserve material disagreement.
- Workplan §6.6 (reviewed), condition (2): "every admitted observation of the configuration on a-'s executed content has a-'s evaluated outcome on the failing outputs -- otherwise nondeterministic in fact".
- Phase C handoff §5 (N2): "Losing completeness must not raise support by hiding either run".
- Manual §6.5, construction rule: "`link⁻` links an observation to content through any admitted observation of the configuration whose recorded basis matches both trees, so a run recorded at a different width than the failing run is never hidden from the adverse conditions by the width alone (27ef339 B1)."
- Manual §6.6, "Bounded and unbounded bases": "so a failure whose stop would need an unbounded run goes to the owner". It also says an unbounded basis "is not used to stop anything".

**Trajectory.**
1. Setup:
   - a Dispatcher-controlled runner class (Python, image recorded, observes every read outside the tree);
   - specification `S`: declarative oracle on `l2_error`, environment fixed, `EXECUTION_DEPENDS_ON kern`, `EVIDENCES` two claim units `c1` and `c2` (two evidence obligations, one configuration);
   - the solver has a data race and fails about half the time, with no runner-supplied seed (unrecorded variation, §6.10);
   - the claims are D4, so no floor event intervenes;
   - no current `COMPLETENESS(EXEC)` judgment: a newly adopted repository, an analyzer that sees an incompleteness marker, or a lapse (27ef339 B1 (ii-a), (ii-b), (ii-c)).
2. At `T1` the Dispatcher realizes both obligations:
   - `a` (for `c1`) fails and is assessed `a⁻`, which counts;
   - `r''` (for `c2`) fails with the identical outcome.

   Both reached the fallback, so both are recorded `UNBOUNDED`, with the `{ tracked = "*" }` entry. §6.9 schedules nothing, since no judgment bounds the closure.
3. An unrelated admitted edit to `docs/notes.md` gives `T2`. Both realizations are non-current (whole-tree entry) and `REALIZE` is derived. `d` on `T2` passes; it is also `UNBOUNDED`.
4. A reviewer attests `COMPLETENESS({S}, EXEC)` and `COMPLETENESS({kern}, EXEC)` during review of an `IMPLEMENT` item. That item changes `kern` (a refactor that leaves the race) and integrates `T3`. The evidence rerun `e` on `T3` is bounded by the current judgments and passes.
5. Evaluate `stale(a⁻)` in the admitted state at `T3`:
   - **(1)** holds through `r''`: `tree(r'') = tree(a⁻)`, `ext` holds (same class, no external reads, same recorded attributes), it stands, and its outcome is identical;
   - **(2)** holds: `link⁻(d, T1)` needs an observation `o'` of `conf(a⁻)` with `on⁻(o', T1) ∧ on⁻(o', T2)`. The only observations with `on⁻(·, T1)` are `a` and `r''`, which are whole-tree records and match only `T1`. `e` records `kern@T3` and does not match `T1`. So `d` is hidden;
   - **(3)** holds through `e` (`bound(e)`, `ext` holds);
   - **(4)** holds: no yielding run is linked to `T3`.

   `a⁻` is stale, `ev` reaches `T` through `e`, and the claim can be valid and discharge. `d` ran on content identical to `a⁻`'s in everything `S` reaches, as the current judgments themselves attest. The contradiction is suppressed by a difference nobody read.
6. No rerun obligation ever creates a narrow anchor: (1) is satisfied, so §6.9 schedules no reproduction, and (3) is supplied by `e`.

**Why this entered through the 27ef339 N1 repair.** In candidate 27ef339, condition (1) required `on⁺`, hence `bound`: every stop needed a reproduction `r'` recorded **narrow**. With this round's `link⁻`, such an `r'` links every run that agrees with `tree(a⁻)` on `r'`'s basis, including `d`. The identical-tree disjunct removes that guarantee, but only where `real(a⁻)` itself is unbounded. Where `a⁻` is bounded, `link⁻` with `o' = real(a⁻)` still catches `d`, and the 27ef339 N1 case (a fix inside a bounded failure's judgment scope) is unaffected.

**Siblings (family search; same cause: an adverse anchor exists only where some record of `a⁻`'s content is narrow).**
- **(4) side: held.** (3) needs a bounded witness `e` with `on⁻(e, G)`, so `link⁻` through `e` reaches every yielding run on a tree that agrees with `G` on `e`'s basis.
- **Bounded failure, unbounded identical-tree reproduction: held** through `o' = real(a⁻)`.
- **Bounded failure whose bounding judgment is later revoked: restrictive only.** The wrongly narrow record links more, keeping the failure counting (N5).
- **Variants of the primary:**
  - an external-custody CI class that reruns a flaky test on the same commit, with a complete `CUSTODY_ENUMERATION`, in place of the second claim;
  - the 27ef339 lapse route, with the failure itself also realized during the lapse.

Further search (tracer fidelity, per-step bounds) would be implementation-like.

**Surfacing.** Nothing discloses the trajectory:
- §6.6's bullet covers only "a bounded failure's recorded content";
- §32.2 says an unbounded basis "matches adversely only an identical tree; such bases serve no stop", which the new disjunct falsifies;
- the closure map's author-choice list records "a run on the identical tree still reproduces" without its consequence;
- no stakeholder decision accepts it.

**Family assessment.** This is the matching family's fifteenth round, counted as the 27ef339 record counts. It is a recurrence of the family cause, entering through a repair of the previous round's non-blocking suggestion, as the handoff anticipated. It is not evidence that the `link⁻` direction fails: the invariant that closes it is stated in one line. **Every stop requires, among the observations `link⁻` ranges over, a narrow record of `a⁻`'s content.** A local repair that restores this invariant closes the cause; recurrence does not by itself force redesign.

**Options for the stakeholder (Phase C handoff §5).**
- **(a) Subtractive, recommended.** Delete the identical-tree disjunct of (1). Accept the 27ef339 N1 cost (one bounded reproduction after a fix inside the judgment's scope) and state it in §31.3 and §32.3.
- **(b) Narrowing.** Keep the disjunct only when `real(a⁻)`'s basis is bounded. This adds one conjunct but narrows the newest clause. It keeps N1's relief exactly for the case N1 described, because `real(a⁻)` is then the narrow anchor.
- **(c) Disclosure only.** The stakeholder explicitly accepts the residual. Then correct §6.5's width claim, §6.6's "goes to the owner", §32.2 and the closure map, and replace the §31.2 expectations.

Whichever is chosen, state the anchor invariant in §6.6 so that later repairs can be checked against it.

**Required discriminators.** These run at the real Dispatcher → Admission → Derivation (`stale`, `undisputed`) → discharge owners, with nothing seeded resolved:
- **(A)** The primary trajectory: `a⁻` is not stale at `T3`, `undisputed = P`, and the owner's adjudication obligation is derived.
- **(B)** The custody-retry variant.
- **(C)** Contrast: a bounded `a⁻` with an unbounded identical-tree reproduction and the same `d` is not stale (through `real(a⁻)`). Under option (b) only, the same `a⁻` with no `d` becomes stale without a further reproduction.

Under option (a), an implementation that lets an unbounded run serve (1) must fail.

### B2 — "Resolved regions" in the write set compare positions, so ordinary edits shift D1-D3 regions into the write set

**Earliest owner.** Manual §1.2 "Write set [D3 decision; SD-14]", as read by:
- §13.2 (domain rule, whose prose also lists "regions");
- §8.3 step 3 (`AUTH_WRITE_SCOPE`);
- §14.3 `BOUNDARY.write_scope`.

These are workplan §21 items 1, 23 and 25.

**Text.**
- **§1.2:** "It contains every effective unit, in either structure, for which any of these differs between the two: its owned content by innermost ownership … ; any declaration key … ; **its resolved regions**; its membership …; its governance signature." Also: "The set is computed like the governance-affecting classification (§1.6)".
- **§1.3:** "`resolve(t, T)` returns the region the term denotes in `T`'s bytes".
- **§1.4 rule 3:** regions "nest, cross or coincide" and "partially overlap". These tests need positions.
- **§1.6:** "the set of governed byte regions it covers differs". There it is compared within one tree.
- **§31.2 (C) (new):** "an `IMPLEMENT` item … changing only bytes that a D4 symbol span owns, in a file that also holds a D2 span, is not [a `VIOLATION`] (27ef339 B2)".
- **§1.2's composite sentence:** "A composite whose revision changes only because a nested subject of another kind inside its scope changed is not in it by that change".
- **SD-14:** "every unit whose owned content, declarations, regions, membership or signature differs between base and merged tree".

**Trajectory.**
1. `src/solver/core.py` holds D4 `impl.core` (`symbol = "write_output"`, lines 1-40) and then D2 `numerics.flux` (`symbol = "flux_limiter"`, lines 50-90). These are top-level siblings, legal under §1.4 rule 1.
2. An accepted `IMPLEMENT` item with `write_scope = ["impl.core"]` adds three lines inside `write_output`.
3. `numerics.flux` owns none of the changed bytes and its `cid` is unchanged. Its resolved region in `M_n(X)` is the same function at offsets shifted by the inserted bytes, so "its resolved regions" differ. `numerics.flux` is therefore in the write set: `BOUNDARY.write_scope` gives `VIOLATION` and Admission rejects with `AUTH_WRITE_SCOPE`.
4. §31.2 (C) expects the opposite whenever the D4 span precedes the D2 span.

**Siblings (one cause: a cross-tree comparison of byte regions).**
- **Same-kind parts (27ef339 B2 discriminator (D)).** In the §31.3 "Recording granularity" file, `kern.helper` precedes `kern.solve`, or the residual `kern.~` has bytes after `helper`. A length-changing edit by a `kern.helper`-scoped item shifts `kern.solve` and `kern.~` into the write set, so the item is refused.
- **Nested subject (27ef339 B2 discriminator (C)).** A D3 whole-file composite contains a nested D2 heading-span subject. A length-changing D2 `AUTHOR` edit shifts the D3 residual part `.~`, which is a D3 unit, into the write set. That is outside an `AUTHOR` scope, which "contains only units of that kind". The composite sentence does not help, because the residual is its own unit.
- **Prefix units (held).** A file added under a prefix changes the unit's `cid` anyway.

**Family and cause.** This is the D1-D3 change rule, write-set surface (SD-14). 1ffbbf0 N2 raised the location-versus-content reading of this clause in the permissive direction, and no record or text resolved it. 27ef339 B2 assumed the content reading when it described its trajectory. Its repair fixed byte attribution only, and its discriminators (C) and (D) were not carried into §31 (N6). It is a **clean local defect**: the repair is a definition, not mechanism.

**Minimum repair.** Keep SD-14's "regions", but define their difference.
- A unit's resolved regions differ iff:
  - a term's resolution status differs (`ABSENT` or present, or the file it resolves into); or
  - under the pinned diff alignment (§7.2, §14.5), a byte enters or leaves the region.
- A change of position alone is not a difference.
- Make §13.2's "regions" read the same.

A moved anchor that gives a D2 unit different bytes stays in the set.

**Required discriminators** (at Admission step 3 and the conformance view):
- **(A)** The trajectory's item is `CLEAN` and admissible, with the D4 span both before and after the D2 span.
- **(B)** A `kern.helper`-scoped length-changing edit is not refused.
- **(C)** In the nested-subject case, no D3 unit is in the D2 item's write set.
- **(D)** An `IMPLEMENT` item that moves `numerics.flux`'s anchors, so that it owns different bytes, is a `VIOLATION`.
- **(E)** A mode change of `core.py` puts both units in the set.

## 2. Non-blocking findings

- **N1 — Polarity prose that the formulas no longer match (residue of the 27ef339 N1 repair).**
  - §0.3 R1 and §6.5's construction rule say "an `UNBOUNDED` basis serves no permissive use", and "Permissive uses … use `on⁺`". (1)'s identical-tree disjunct is a permissive use that does not use `on⁺`.
  - §6.6 says an unbounded basis "is not used to stop anything; adversely it matches only an identical tree". §32.2 says "such bases serve no stop". §6.9 says "(so no run could serve (1) or (3))".
  - Formulas govern (§0.1), so this is not a separate blocker. But these are the statements B1 falsifies, and the repair of B1 must reconcile them.
- **N2 — The floor's yielding clause is a width-dependent adverse use (sibling consumer of B1's cause).**
  - §6.8's floor fires on "an admitted observation `o` with `on⁻(o, T_m)` … yields it". It does not use `link⁻`, although R1 now says adverse conditions should not depend on recorded width.
  - The owner's adjudication obligation and `qual` still hold, and for D1/D2 the disposition is R3. So no invariant is violated, but the floor can be missed on a non-`adm` failure.
  - Use `link⁻` there, or state why `on⁻` suffices.
- **N3 — The scope of frame gate decisions (27ef339 B3 repair).**
  - **Who must declare a frame.** "a gate decision on a subject in the transformation's prospective state" is over-broad: every subject is in a frame's prospective state. State instead: a `GATE_DECISION` answering a gate obligation derived for `X` (on a subject whose revision `X` changes, or required by `X`'s item).
  - **Standing across frames.** §8.3 step 7 and §5.5 do not say in which frame and run "standing" and "answered" are read. A frame decision of an abandoned candidate on a non-D1/D2 triple can then be the "standing" decision for the same triple's gate in the admitted state or in another candidate's frame. Another holder is refused there, and only its author or the owner can supersede it through `REVALIDATE`. The same holds for a frame decision on a subject the frame leaves unchanged.
  - **Obligation identity.** The frame value of the `run(s)` obligation parameter is undefined. State that `GATE` and `ACCEPT` match by target triple and run membership, not by the identity hash.
  - **Untested discriminators.** §31.6 asserts only the positive case. 27ef339 B3 discriminators (B) and (C) are absent.
- **N4 — S11 residue (27ef339 N3, partly closed).**
  - R10, §5.5, §16.8 and §19.4 now state that gate decisions and required-kind judgments are reused across tenures for subjects that are not `NATIVE` D1/D2.
  - §0.4 S11 still says "across tenures nothing revives".
- **N5 — `link⁻`'s range and its restrictive cost are unstated.**
  - The text does not say whether `o'` ranges over `INCOMPLETE` observations, refused records, abandoned-frame observations, or observations whose bounding judgment was later revoked.
  - A wrongly narrow record links content it omitted, so a fixed failure can keep counting until the owner disposes of it. This is fail-closed and consistent with the reviewed rule that adverse uses ignore completeness standing, but it is not disclosed in §32.2 or §32.3.
- **N6 — Qualification gaps (DS-001).** §31 omits these required discriminators: 27ef339 B2 (C) and (D), and 27ef339 B3 (B) and (C). It also has no case where both the failure and its only reproductions are unbounded (B1). A §31 written to the current text is green with both blockers present.
- **N7 — Accounting.**
  - The closure map's author-choice bullet "a run on the identical tree still reproduces" omits B1's consequence.
  - Row 5's "declared frame per kind … CARRIED + DECIDED" is right in substance but rests on N3's wording.
  - The aid confers no authority.

## 3. Closure audit

Each workplan §21 item and clause was located in the Manual directly; the closure map was used only as an index. "Answered" means a substantive D3 answer exists; it is neither runtime evidence nor stakeholder acceptance. The diff since 27ef339 touches §0.3, §1.2, §1.8, §5.5, §6.3, §6.5, §6.6, §7.5, §10.2, §14.5, §16.8, §19.4, §30, §31.2, §31.3, §31.6 and two closure-map places, so §21 rows outside those sections carry the 27ef339 audit, which I re-checked against my whole-Manual read.

| §21 | Independently located answer | Result |
|---|---|---|
| 1 | §§1.1-1.11 | **Write-set region comparison undefined across trees (B2)**; tracked-path fallback entry now disambiguated (`{ tracked = "*" }`) |
| 2 | §§1.7, 2.1-2.6 | Answered |
| 3 | §§3.1-3.6, 6.8, 17.1 | Answered |
| 4 | §§4.1-4.6, 6.3 | **Not substantively closed for unbounded failures (B1)** |
| 5 | §§5-7, 17, 22.3 | `stale` carries **B1**; declared frame per kind answered (N3 wording); strata, single-valuedness and monotonicity hold (`link⁻` and the new (1) disjunct read only S0/S1 facts; `link⁻` only enlarges adverse matches) |
| 6 | §§8, 21-23 | Answered |
| 7 | §10 | Answered; gate discharge at integration reachable through frame decisions; N3 |
| 8 | §11, §13.2, §13.4 | Answered |
| 9 | §9 | Answered |
| 10 | §16 | Answered |
| 11 | §§17, 6.10 | Answered |
| 12 | §18 | Answered |
| 13 | §§19-20 | Answered; N4 for S11 wording |
| 14-16 | §§21-25 | Answered; runtime unexecuted |
| 17 | §26 (both transfer tables) | Answered |
| 18, 19 | §§27, 28 | Answered |
| 20 | §20 | Answered |
| 21 | §29.7 | Answered |
| 22 | §30 | Present and updated |
| 23 | §12, §1.2, §13.2 | **Domain-rule input contradictory under the position reading (B2)** |
| 24 | §13 | Answered |
| 25 | §14 | Diff-to-unit mapping repaired; write-set region comparison is B2; the rest answered as design; no threshold accepted |
| 26 | §§15-16 | Answered |
| 27 | §29 | Present; see section 9 |

**Workplan §16.2, both tables.** The diff since 27ef339 does not touch §26.4. I re-read §26.3-§26.4 against the workplan's **Deferred** rows. Every one has a final disposition, and none is merely routed:
- invariants 4, 9, 15, 17 and 26;
- the §5 sub-rules;
- §6, §7 and §12;
- §18.

**Material decisions versus delegated D4.** Parsers, the diff implementation, checkpoint encoding, limit values and the file-type table remain correctly `[delegated]`. Two architectural decisions are left implicit or contradictory:
- the adverse anchor for an unbounded failure (B1);
- the meaning of "regions differ" across trees (B2).

## 4. Refinements R1-R11

| # | Assessment |
|---|---|
| R1 | `on⁻`, the guard, set-valued `ext`, `bound` and `on⁺ ⇒ on⁻ ⇒ link⁻` are sound per record. `link⁻` is a sound adverse-only S0 existential: under correct completeness judgments, agreement of `K` and `K'` on a narrow record implies the same content read; under wrong ones it is restrictive only (N5). **The identical-tree disjunct of (1) is unsound for unbounded failures (B1)**; N1 is its prose residue |
| R2 | Sound; unchanged. No new edge: the (1) disjunct reads no completeness |
| R3 | Sound; unchanged |
| R4 | Sound within its crash model; unchanged |
| R5 | Sound as a partition rule. The write set's cross-tree region comparison contradicts its use (B2) |
| R6, R7 | Sound; unchanged |
| R8 | Sound |
| R9 | Sound. The veto's `same` for `GATE_DECISION` is per obligation and run; N3 concerns which frame reads it |
| R10 | Sound, and now names its resolution of the reviewed restoration lock. S11 in §0.4 lags it (N4) |
| R11 | Sound as one standing decision with a `P` cap, now reachable for frame-decided gates. It narrows SD-24 for second holders; this is surfaced as an author choice, which I would confirm with the stakeholder |

## 5. Previous findings and Phase B closures

"Closed" means I re-derived that the present text excludes the named trajectory; it is not runtime evidence.

**Depth.** I re-derived every 27ef339 item in full. For the earlier records, I took the 27ef339 record's re-verification tables as hypotheses. I re-checked every disposition that the 27ef339-to-5c55d4b diff or my findings touch, and I read 1ffbbf0 N2 and 0b6c4fa N5 in full. I did not re-read the earlier records' full prose (section 13).

### 27EF339 (same family)

| ID | Disposition and basis |
|---|---|
| B1 | **Closed for bounded failures.** All three required discriminators, (A) the lapse and restore, (B) a judgment admitted later and (C) analyzer-upgrade gap reruns, now give "not stale" through `link⁻` with `o' = real(a⁻)`. The unbounded-failure sibling opened by the N1 repair is **B1** here |
| B2 | **Partly closed.** Byte attribution now follows innermost ownership. The region-position residue is **B2** here |
| B3 | **Closed.** Gate decisions on a frame declare it, pass step 6 there, are in the prospective run and satisfy discharge after integration. Wording and scope residue is N3 |
| N1 | Closed by the identical-tree disjunct, which **introduced B1** |
| N2 | Closed as surfacing: §31.3 and closure map §5 state the partial reversal of SD-17. The stakeholder decision is pending |
| N3 | **Partly closed** (N4) |
| N4 | Closed: "its author or the owner, whichever answers first" |
| N5 | Closed. A challenge of the subject triple cannot be evaded by supersession, and `decide(gate)` renders a core for a `REJECT`. The SD-24 narrowing is surfaced |
| N6 | Closed (`{ tracked = "*" }`, record-only) |
| N7 | Closed. §30 counts `link⁻`, `bound`, `adm` and §6.9; the map lists B1's residual and N1's cost. New accounting residue is N7 |

### 0B6C4FA, A18B544, E9E6E9F, E2154AC (same family)

| Review | ID | Disposition |
|---|---|---|
| 0B6C4FA | B1 | (i)-(iii) closed. (ii) now closed for bounded failures. **The unbounded-failure side reopens as B1** through the new (1) disjunct |
| 0B6C4FA | B2 | Closed. (a) is now closed, since gate decisions are frame records |
| 0B6C4FA | N1 | Closed as surfacing; stakeholder confirmation pending |
| 0B6C4FA | N2-N4, N6, N7 | Closed; N4's S11 wording residue is N4 here |
| 0B6C4FA | N5 | The repair chain ends in **B2** here |
| A18B544 | B1 | Closed on the passing side; adverse side as 0B6C4FA B1 |
| A18B544 | B2, N2, N4, N5 | Closed |
| A18B544 | N1 | Superseded; residue N4 |
| A18B544 | N3 | Chain ends in **B2** here |
| A18B544 | N6 | Superseded |
| E9E6E9F | B1, B2, N1-N3, N5 | Closed |
| E9E6E9F | N4 | Superseded |
| E2154AC | B1, N1-N5 | Closed (the N2 inspector residue is closed by the §16.8 repair) |

### 3540D98 (different family)

| ID | Disposition |
|---|---|
| B1 | Closed: exact identity |
| B2 | Closed: full external-input set |
| B3 | Closed; the gate family's sixth-round residue is N3 (non-blocking) |
| B4 | Closed: equal regions |
| N1 | Closed for acceptances and gate decisions (prospective run) |
| N2-N4 | Held as disclosures |

### 798B2B4, 71CF9B3, 86AB683

| Review | ID | Disposition |
|---|---|---|
| 798B2B4 | B1-B3 | Closed, now also for gate decisions (frame-declared, prospective run) |
| 798B2B4 | B4, N2-N8 | Closed |
| 798B2B4 | N1 | Closed; the R10/S11 scope residue is N4 |
| 71CF9B3 | B1, B2, N1-N8 | Closed |
| 86AB683 | B1, N1-N7 | Closed |

### 1FFBBF0, 53669A5, D837363

| Review | ID | Disposition |
|---|---|---|
| 1FFBBF0 | B1, B2, N1, N3-N7 | Closed |
| 1FFBBF0 | N2 | The location-versus-content reading of "resolved regions" was never stated. It is **reopened, restrictive direction, as B2** |
| 53669A5 | B1-B3, N2-N9 | Closed |
| 53669A5 | N1 | The SD-17 partial reversal is surfaced for the stakeholder and not decided |
| D837363 | B1-B3, N3-N8 | Closed |
| D837363 | B4 | Closed as effect-keyed; the region comparison is **B2** |
| D837363 | N1, N2 | Nested subjects and cross-kind routes are contradicted by B2's sibling (c) |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

| Review | ID | Disposition |
|---|---|---|
| CC005DB | B1-B3, N1-N8 | Closed |
| C6DA678 | B1-B3, N1-N12 | Closed; N9 (empty prefix) is now closed by `{ tracked = "*" }` |
| B595F2C | B1 | Closed for bounded failures. **The unbounded failure with identical-tree reproductions is B1** |
| B595F2C | B2-B4, N1-N8 | Closed |
| 6FF4ED1 | B1 | Closed: `on⁺ ⇒ on⁻ ⇒ link⁻` with frozen context |
| 6FF4ED1 | B2-B4, N1-N12 | Closed |

### Phase B §3 closures and N1-N4

| Closure or limit | Present reconstruction |
|---|---|
| EF8445A/552AC01 N2: strata, completeness polarity | **Re-tested in both directions.** Take a differing old-content run and a yielding present-content run on an alternate tree that differs only outside a recorded narrow basis, under a judgment that becomes `P`, blocked, revoked or loss-withheld. Results: **held** for runs recorded narrow; **held** for runs recorded unbounded when the failure or a reproduction is narrow (`link⁻`); **B1** when the failure and all its reproductions are unbounded. Restrictive direction: no settled stop is withdrawn except through a narrow record whose own closure omits the change (N5, fail-closed) |
| Fail-closed support cycles; corrupt prefixes | Held. `link⁻` and the (1) disjunct are S0/S1 and add no support-graph edge, and `INTEGRITY_HALT` is unchanged |
| Y1/Y2, X1-X3, candidate-own latch, floor and class | Held; floor sibling N2 |
| Contrary-run retention, nondeterminism | Held for bounded failures; **B1** for unbounded failures |
| U1/U2/W1/W2 executed content | Held for currency |
| Absorbed relaxation; adversity versus currency, challenge, loss; salvage; independence; start latch; effective structure, quarantine, tenure | Held. Gate frames are now coherent (N3 wording) |
| Phase B N1 | Disclosed (§32.2, §32.4) |
| Phase B N3 | Held (§31.3) |
| Phase B N4 | Held as reopen triggers |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | 27ef339 B1 primary: bounded failure, lapse, unbounded differing run on a doc-edited tree, restore, fix | Held (`link⁻` via `real(a⁻)`) |
| 2 | 27ef339 B1 (ii-a) and (ii-b) with a bounded failure | Held |
| 3 | Unbounded failure, unbounded identical-tree reproduction (second claim, or CI retry), unbounded differing run, later judgment and fix | **Violation (B1)** |
| 4 | As 3, but the reproduction is recorded bounded | Held (narrow anchor) |
| 5 | Yielding unbounded run on a variant of `G` | Held through (3)'s bounded witness |
| 6 | 0b6c4fa B1 (i): racing solver, no judgment, one flaky pass on `T2` | Held (cannot serve (3)) |
| 7 | Identical-tree reproduction with a different pin or free attribute | Held (`ext`) |
| 8 | Narrow record bounded by a later-revoked or abandoned-frame judgment linking an old yielding run | Restrictive only (N5) |
| 9 | Non-`adm` D1/D2 failure, yielding run of admitted content recorded at a width that misses `T_m` | Floor clause missed; adjudication stays (N2) |
| 10 | Structure, `ignore`, analyzer or system-version change with the tree fixed | Held (`on⁻` and `link⁻` unchanged) |
| 11 | D4 edit below a D2 span in one file | Held (`CLEAN`) |
| 12 | Length-changing D4 edit above a D2 span | **Contradiction (B2)** |
| 13 | `kern.helper`-scoped edit with `kern.solve` or `kern.~` after it | **Contradiction (B2)** |
| 14 | D2 `AUTHOR` edit of a nested heading span in a D3 whole-file composite | **Contradiction (B2)** |
| 15 | Mode change of a mixed-kind file | Both units in the set; fail-closed |
| 16 | Gated `AUTHOR` D2 revision; frame gate decision; integration | Held (in the prospective run, step 6 in the frame, discharge after admission) |
| 17 | New gated D3 subject; frame gate | Held |
| 18 | Abandoned candidate's frame gate decision; identical bytes absorbed | Not current (its core's frame records are not current); answering and standing scope is N3 |
| 19 | Frame gate decision on a subject the frame leaves unchanged; candidate abandoned | Answered in no admitted run, but "standing" scope is undefined (N3) |
| 20 | Second holder's challenge of the subject triple, then the author's supersession | Held (the block survives) |
| 21 | `REVALIDATE` of a stale gate decision | Held (author or owner) |
| 22 | Non-D1/D2 restoration at an unchanged triple with a `QUALIFIED` gate | Held (reused; the inspector entry stays open) |
| 23 | Support cycle via absorbed `about` or a completeness edge; corrupt authenticated prefix | Held |
| 24 | Publication crash windows, fence chains, ABA | Text unchanged since many rounds; not re-attacked in depth |

## 7. Minimum architecture and capability transfer

No primitive, component, persistent surface or record tier is added. The round added:
- `link⁻`, one S0 existential;
- the identical-tree disjunct of (1);
- an extension of §7.5's frame list;
- write-set and diff-mapping wording;
- the `{ tracked = "*" }` record-only entry.

B1 entered through the disjunct. The recommended repair (a) removes it, and repair (b) narrows it. B2 needs a definition, not mechanism. §30's accounting is current apart from B1's consequence.

**Capability transfer.**
- The §26.4 tables are unchanged and resolve every Deferred §16.2 row.
- Core prompt mode, frozen profiles and the containment root are preserved, and Core never imports SSDS. PC-001 holds.
- PEM was activated, because this is mature-machinery replacement:
  - `PROJECT-ENGINEERING-MEMORY.md` is byte-identical on `main` and at the candidate (`15617971…`);
  - the validator, run from the checkout with `source/` unchanged from the candidate, reports "PEM schema 1 valid: 5 families, 0 notices";
  - `tests.test_protocol_63_engineering_memory` passes (28 tests).
- HAS dispositions:
  - PC-001 applicable, held (§26.4, §28, §31.8);
  - FF-001 applicable to genesis, held (§19.9);
  - SP-002 applicable to self-reference, held (§8.7, G3);
  - SP-001 not materially applicable to this Manual;
  - DS-001 applicable to §31 (N6).
- Absence of a 7.x memory entry proves nothing.

`orchestrator/docs/architecture.md` (blob `39e6de72…`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## 8. Qualification-design adequacy

§31.1 states that no executable SSDS evidence exists at G1 and that every runtime group is `UNEXECUTED`. Nothing is claimed as executed.

Green fixtures could coexist with each blocker (DS-001):
- **B1.** §31.2 "Width-independent adverse matching" uses a **bounded** failure. §31.2 "Unbounded bases" (A) has no later judgment. No case realizes an unbounded failure whose only reproductions are on its own tree, followed by a differing run on an equivalent tree and a later bounded witness.
- **B2.**
  - §31.2 (C) does not fix the span order.
  - The 27ef339 B2 nested-subject and `kern.helper` discriminators are absent.
  - §31.5 tests only cross-kind declarations and D1-D3 edits.
- **Gate frames.** §31.6 states the positive integration case only (N3).

§31.3 "Red then green" now states its premise and its cost honestly.

The diagnostic model was not run (optional). Its file is unchanged since the Phase B candidate, and it models none of these clauses.

## 9. Doctrine-realization map and O1

§29 is unchanged this round. I re-checked §29.2-§29.5 against:
- the 7.2.1 D3 entrypoint and its expanded entry contract;
- the role-contract rows;
- every scientific-checks duty.

Two claims rest on the blockers:
- §29.4's disagreement-survival claim, via §6, rests on B1.
- §29.2's routing row (E0 through the §13.2 domain rule) is over-enforced under B2's literal reading. It blocks legitimate D4 work in mixed-kind files rather than permitting silent mutation.

§29.4's revising-duty row and §29.7's Channel C row are now coherent with frame gates. §29.6's E3 list is adequate.

O1 (§0.5) states the realized record, readers, routine questions and realized-record architecture. It visibly marks the within-deliverable surfaces, and "Beyond the requested deliverable: **None**". I found no unmarked inspectability-driven product requirement and no mark wrongly classed as within the deliverable. Technical Review accepts no marked item; a marked item beyond the deliverable binds only after stakeholder or task acceptance.

## 10. What I verified and how; what I could not verify

**Verified at the exact candidate** (`git archive` snapshot under `$TMPDIR/ssds80-manual-review-5c55d4b/`):
- **Reading.**
  - The whole Manual, sections 0-33. §22-§24 were read for change and consistency, not re-attacked.
  - The diff from 27ef339 (Manual and closure map).
  - Closure-map §1 rows 1-5 and the author-choice list.
  - Workplan §6.6 (`stale`, scheduling).
  - Stakeholder record items 18-19 and SD-14, SD-22 to SD-24.
  - Phase C handoff §5 (N2).
  - The 27ef339 record in full; 1ffbbf0 N2; 0b6c4fa N5.
  - Governing owners as listed.
- **Blobs.** The Manual, closure-map, workplan and Phase B blobs match the handoff.
- **Tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the snapshot: 4 tests, OK.
- **Whitespace.** `git diff --check 27ef339… 5c55d4b…`: clean (exit 0).
- **Additions.** `git diff --stat fad3ee4… 5c55d4b…`: 39 files. All are under `qualification/ssds80/`, plus the Manual and two lines in `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. The workplan, stakeholder record and PEM are unchanged since 27ef339.
- **Frozen surfaces.** `git diff --quiet fad3ee4… 5c55d4b… -- orchestrator/docs/architecture.md source dist`: exit 0.
- **PEM.** As in section 7.

**Not verified:**
- any SSDS runtime behavior (none exists);
- tracer fidelity and G3 costs;
- the full prose of Review records before 27ef339, beyond the findings and dispositions named in section 5;
- deep re-derivation of findings whose cited text is unchanged since 27ef339;
- publication and fencing, which were not re-attacked;
- the diagnostic model, which was not run.

Family search stopped at characterization, as method step 6a allows.

## 11. Scientific-checks answers

This task reviews D3 authority for software that mediates scientific evidence.

1. **Material findings.**
   - Blockers B1 and B2 and non-blocking N1-N7, all D3 architecture or coordination findings.
   - I have no D1/D2 scientific or numerical findings and no out-of-scope scientific findings.
   - I launched no agents. The tools I ran (section 10) produced no finding beyond those stated.
2. **Realized results.** I produced, ran and reviewed no realized scientific results and prepared no gate evidence, so no null envelope is owed. The unit tests, the PEM validator and the PEM tests are software checks on documents, not realized results.
3. **Variants.** Yes, design and interpretation variants only. This was not result selection over data, and no data, held-out set, earlier history or delegated search was involved.
   - **Repair options:** three for B1, (a)-(c); two for B2 (define the region difference by diff alignment, or delete "regions", which SD-14's wording argues against).
   - **Clause readings, kept as findings rather than resolved:** two readings each of three clauses:
     - "resolved regions differ": position or content (B2);
     - which gate decisions declare a frame (N3);
     - the frame in which a gate decision is "standing" (N3).
   - **Selection criterion:** preserve the owner-required property with the least added mechanism (convergence owner). The B1 choice is the stakeholder's.
4. **Tension search.** Not triggered. I relied on no accepted D1/D2 authority for a consequential judgment; no scientific or numerical formulation is accepted for the SSDS product. The judgments rest on:
   - accepted SSDP 7.2.1 protocol owners (D3, evidence, convergence, abstraction);
   - the proposed workplan;
   - the stakeholder record and Phase C handoff.

Gaps: none in these answers.

## 12. Common-mode note

I share the Manual author's model family (Claude). The authoring session launched me from a handoff it wrote. The following are shared dependencies:
- the corpus;
- the inherited workplan framing;
- the prior Review records (fifteen of the sixteen Manual Reviews same-family);
- the toolchain.

The 3540d98 and Phase B reviewers were of another family (GPT).

Both blockers trace to the previous same-family record:
- B1 entered through the repair of its N1 narrowing option, whose interaction with its own B1 option (a) that record did not examine;
- B2 is the reading that record's B2 trajectory assumed but did not ask the repair to state.

Repair directions from candidate 13 onward were chosen by the author under the stakeholder's delegation (item 19), not by the stakeholder. I would put B1's options and the SD-17 partial reversal to the stakeholder before any further same-family round. I would also suggest that the anchor invariant of B1 be stated, so that a different-family confirmation can test it directly. The stakeholder reserves the choice of a final different-family confirmation.

## 13. D4 statement

SSDS 8 D4 is **not authorized**. This NO-PASS accepts no architecture, no proposed default and no product scope. G1 also requires a later independent PASS on a repaired candidate and explicit stakeholder acceptance. G2 requires a reviewed shadow D3->D4 workplan and explicit stakeholder authorization.
