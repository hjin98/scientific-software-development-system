# SSDS 8 Architecture Manual — Independent D3 Review, candidate cc005db

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout /home/user/scientific-software-development-system)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: cc005dba7eb6885f2c683cdf8d0387ba88fa0eab
    SCOPE: the whole proposed Manual as durable D3 owner: (a) §21 and §16.2 closure; (b) fidelity to the
           Phase B-reviewed workplan, including refinements R1-R9; (c) out-of-matrix adequacy; (d) inheritance
           and capability transfer (Architecture 1.6.0, workplan §18, PEM HAS); (e) qualification design;
           (f) doctrine-realization map; (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob 474c11e4c466c20d719d4420a21ee63c6670414d (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md, blob 679497dcc722d04b31019b06311c83af05797cde (verified)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23;
           Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b97fb8152d2a5742e17fa172e12204756, verified);
           blob at the candidate 91bde236465178f20c7348280e036d2884dfc216 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml)
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS (HYPOTHESIS ONLY): MANUAL-REVIEW-SSDS-8.0-C6DA678-NO-PASS.md; MANUAL-REVIEW-SSDS-8.0-B595F2C-NO-PASS.md;
           MANUAL-REVIEW-SSDS-8.0-6FF4ED1-NO-PASS.md; WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
    REVIEW METHOD: entry through source/roles/software-design/SKILL.md at the public source (expanded entry contract and
           scientific checks from dist/skills/software-design/SKILL.md); owner reconstruction (architecture-and-design,
           abstraction-and-concretization, convergence, evidence, workflow, versioning, scientific-checks fragment);
           full read of the Manual from a git-archive snapshot; clause comparison of Manual §6 with workplan §6.6 and §10;
           diff review c6da678..cc005db; constructed trajectories in the permissive and restrictive directions;
           G1 document checks executed
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session

The Manual's refinement table, decision markers, §30 pass and qualification claims, the closure map, commit messages, the handoff's scope text, workplan §0.1/§27 rationale, the diagnostic model's results, the stakeholder record's characterization of options and every prior Review record were treated as hypotheses. Section numbers refer to the Manual at the candidate unless prefixed "workplan".

## SERIOUS CHALLENGE

**None.** No accepted governing authority was found false, contradictory, ambiguous, inadequate or unrealizable. The 7.2.1 evidence owner ("A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority."; "When competent evidence assessments materially conflict, preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence."), the scientific-checks revising duty (e=5) and the workflow owner's D1/D2 revision-gate rule are coherent and realizable here. SD-11 and SD-12 are realizable; B2 below is a gap in realizing SD-11's "resolution context frozen at realization", not a defect in the direction. Every blocker is repairable at Manual sections without changing a parent.

## Verdict

**NO-PASS.** Three blockers survive.

- **B1** reopens the domain-rule family for the third successive review: the write set that the domain rule, the write-scope check and the `AUTHOR` triggers read still misses changes that alter a D1-D3 subject's revision without touching its own bytes or keys (the governed boundary, a newly declared part). A non-`AUTHOR` item can therefore revise D1/D2 authority without the revising duties.
- **B2** is the seventh successive finding in the assessment-disagreement matching clause. The frozen resolution context names the `ignore` patterns and the analyzer set but not the system version's resolution semantics, which the Manual itself lets change (normalization, term grammar, wildcard semantics). After such a change, re-resolution under the current semantics removes adverse recorded matches, so a live nondeterministic disagreement lapses mechanically. SD-12's construction rule held under every other attack below.
- **B3** is a clean local contradiction in the R9 repair: the veto formula requires the same kind, while its prose makes a product-scope rejection veto a gate acceptance of another kind.

This verdict accepts nothing and authorizes no D4.

## 1. Blockers by earliest owner

### B1 — The write set misses D1-D3 revisions made through the governed boundary or through new parts; a non-`AUTHOR` item revises D1/D2 authority without the revising duties (§1.2 write attribution, §13.2 domain rule, §14.3 `write_scope`; previous B3 partly reopened)

**Mechanism.** §1.2 attributes manifest bytes "to every unit whose declaration keys or `[unit.semantic]` table they change (a newly declared unit with its declared kind, a removed unit with its effective kind), and to `ssds.manifest` only where they change no unit's keys (`schema`, `[governed]`)". §13.2 then claims: "its write set (§1.2) may contain none, so neither a unit's text nor its manifest declarations (semantic table, scope, membership, kind) can change except through an `AUTHOR` item". But a unit's revision depends on more than its own bytes and keys: a `prefix` term denotes "every governed file whose path starts with the prefix" (§1.3), and `sem(u, T)` covers "semantic declarations of u and of every unit inside scope(u)" (§1.5).

**Trajectory A (governed boundary; every step locally conforming).**
1. D2 subject `numerics` has scope `{ prefix = "numerics/" }` and a current R3 acceptance. Plan item `i1` (`IMPLEMENT`, D4) has `ssds.manifest` in its write scope, a normal arrangement for adjusting `ignore` (for example `build/`).
2. `numerics/notes/` is already ignored. Item `i1` adds a note file there. The bytes are not governed content, so they belong to no unit and the write set is unchanged. `write_scope` and the domain rule pass.
3. Item `i2` (`IMPLEMENT`, same scope) removes `numerics/notes/` from `ignore` (or, in the removal variant, adds a pattern that ignores part of the D2 text). The only changed bytes are in `[governed]`, attributed to `ssds.manifest` (kind `MANIFEST`). The domain rule and `write_scope` pass. §8.3 step 4 has no check on authored governed-boundary changes beyond well-formedness.
4. On integration, `content(numerics)` changes, so the D2 subject loses validity and an R3 `ACCEPT` is derived. Neither task was an `AUTHOR` item, so no `revision_assessments` or `o1_content` slot exists, and no tension-search injection or revising duty fires (§16.3 injects them only for "`AUTHOR` revising D1/D2 authority"). The §16.6 gate core section 3 has nothing to render and marks nothing missing. A human accepts the new D2 revision, which now includes implementer-authored text, without the assessments.

**Trajectory B (new part).** An `IMPLEMENT` item declares a new part of a D2 composite whose `[unit.semantic]` table carries `defines` or a `USES_DEFINITION` relation. `kind` is "forbidden on parts" (§1.2), so the new unit's "declared kind" is empty. Read literally, the attribution gives the write set no D1-D3 unit. Yet `sem` of the D2 subject changes, so its revision does. A unit moved into a D2 composite by its own `part_of` and scope keys has the same gap: whether its kind in the write set is the old (D4) or the new inherited (D2) one is unstated, and the receiving subject's revision changes without any key of its own changing.

**Violated text.** Scientific checks e=5: "When revising, renaming, splitting, merging or replacing D1/D2 authority, also search recorded tensions bound to its accepted concretizations. In the revision's own record and its gate evidence, record the predecessor identity and, per found tension, a revision-scoped applicability assessment". Workflow owner: "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments". Manual §13.2 (quoted above) and §29.4: "**E0** (only an `AUTHOR` item can change D1-D3 units, in their text or their manifest declarations, §1.2 and §13.2, so the slot is always triggered ...)". §29.5's documentation E0 row is false on the same routes.

**Earliest owner.** Manual §1.2 write attribution, read by §13.2, §14.3 `write_scope` and the §13.5/§16.3 `AUTHOR` triggers.

**Convergence assessment.** This is the third successive finding in one family: b595f2c B3 (`DOCUMENT` scopes), c6da678 B3 (manifest declarations) and this one. Each repair added a syntactic attribution rule (by owning bytes, then by changed keys), while the protected property is semantic: a D1-D3 subject's revision, regions or structure changed. That is a non-local recurrence with an evident simpler mechanism already in the Manual: Derivation computes `Δ(X)` ("the set of effective units whose revision in `tree(C)` differs from `B`", §7.1) and the structural comparison of §1.6.

**Options for the stakeholder.**
- **(a) Effect-keyed write set (recommended; removes the attribution special case).** The write set is every effective unit, and every subject containing one, whose revision, resolved regions, membership or signature differs between the base and the merged tree under `Σ_n` and `Σ_n ⊕ Δ_Σ(X)`, plus newly declared and removed units with their effective kinds. The domain rule, `write_scope` and the `AUTHOR` triggers read that set.
- **(b) Additive:** attribute `[governed]` changes and new-part declarations to the affected units. This closes the two routes found but keeps the enumeration.
- **(c) Backstop at the effect:** any `ACCEPT` or gate for a changed D1/D2 revision carries the revising duty and requires the `revision_assessments` slot, whatever item produced the change. The §16.6 core then marks absent assessments as missing.
- **(d) A different-family Review before the next repair.**

**Required discriminator.**
- An `IMPLEMENT` or `DOCUMENT` item with `ssds.manifest` in scope that changes `ignore` so that a D2 `prefix` unit gains or loses a file is a `VIOLATION` (or is refused).
- So is one that declares a new part of a D2 composite carrying a semantic table, or one that moves a D4 unit into a D2 composite.
- An `AUTHOR` item for that D2 subject may do all three, and its brief carries the revising and tension-search duties.
- An implementation that computes the write set from changed bytes and keys alone must fail.
- §31.5 (c6da678 B3 case) tests only a D2 unit's own semantic table, scope and membership and a new D2 subject, so it passes with this defect.

### B2 — The frozen resolution context omits the system version's resolution semantics; a system-version adoption removes adverse recorded matches and a live disagreement lapses (§6.3 re-resolution, §6.5 construction rule, §1.5, §27.3; refinement R1)

**Mechanism.** §6.3: "`resolve_o(t, K)` re-resolves a recorded term in content `K` under `o`'s frozen resolution context and the system version's normalization (§1.5), never under the current `Σ`, `ignore` or analyzers". The resolution context is only "the `ignore` patterns of `Σ` and the analyzer set of `ρ` at the realization's position". Yet §1.5 says "A future normalization is a system-version change (§27)". §27.3 places "Derivation semantics, normalizations (§1.5), the merge implementation (§7.2), check-template functions and the canonical encodings" in the system version, adopted by `RULESET_ADOPTION` from a position on. Term-resolution semantics (heading spans, the fnmatch semantics of `ignore`, prefix hashing) and the anchor comment-leader table ("**[delegated]** The file-type table and its extension within the same rule"; anchor lines are removed by normalization) are likewise system-version semantics. Current derivation runs the current system version. So `cid(resolve_o(t, K))` for a pre-adoption observation is computed under semantics other than those its recorded `c` was computed under, and it can differ with `K` byte-identical to `tree(o)`. `on⁻` is then false for an observation that ran on exactly that content.

**Trajectory (D4 claim; every step locally conforming).**
1. Specification `S` (declarative oracle; thread scheduling free) evidences claim `c`. At admitted tree `T0`, realization `p` passes.
2. A run on `T0` fails (`solve` races) and is assessed `a⁻`. (2) fails, because `p` is `on⁻ tree(a⁻)` with another outcome. `undisputed = P`, and the owner's adjudication obligation is derived. The owner has not yet acted.
3. A human-gated `RULESET_ADOPTION` adopts a ruleset of a new system version. It adds a normalization, for example removing a byte-order mark, or extends the anchor file-type table to a file type `S`'s closure covers, or simply re-tags `cid`. A recorded term's `cid` over `T0` bytes changes. The adoption gate is shown ill-formed subjects and reopened obligations (§27.1), not lapsing disagreements.
4. Under the current semantics, `p` and `real(a⁻)` are no longer `on⁻ T0`. The rerun obligation produces reproduction `r` on `tree(a⁻)`, which happens to fail identically, so (1) holds. (2) now ranges only over post-adoption runs on `tree(a⁻)`, here `r`, so (2) holds.
5. An item changes a recorded region and integrates `T1`. The affected-evidence run `q` passes. (3) and (4) hold in `T1`, `a⁻` is stale, `undisputed = T` and `c` is valid. Nothing disposed of the disagreement; machinery stopped reading `p`.

For a D1/D2 claim, `adm(a⁻) = on⁻(real(a⁻), T_b)` becomes false for every pre-adoption failure. A later discriminating reading is then admitted at R2 as "candidate-own" for a failure of admitted content (§6.8 class rule), and the floor's `adm` clause cannot fire after the adoption.

**Violated text.** Manual §6.1: "No content change, structural change, specification change, frame outcome, challenge or ledger order ends it by itself"; §6.6: "(1) and (2) need an identical second execution on the content `a⁻` read and no other outcome there, ever"; R1's stated property, "never removes an adverse recorded match"; the construction rule's "`on⁻` reads no ... current structure, `ignore` or analyzer". Evidence owner: "preserve the disagreement and route adjudication ... or obtain discriminating evidence". Phase B closure "nondeterministic old-content observations defeat (2)". SD-11: "the resolution context frozen at realization".

**Earliest owner.** Manual §6.3 (resolution context, re-resolution) with §6.5's construction rule and the R1 row.

**Convergence assessment.** This is the seventh successive finding in the matching clause (`ef8445a` N2, `552ac01` N2, Phase B N2, `6ff4ed1` B1, `b595f2c` B1, `c6da678` B1, this one). At family level each finding is one dimension of "the same content" that either was not frozen or entered `on⁻` with the wrong polarity. SD-12's polarity rule closes the second kind, and it held here. This finding is of the first kind: the frozen context is defined by enumeration (structure, `ignore`, analyzers), and an unlisted input to `resolve` and `cid` stays current. The immediate cause is local, and the repair is subtractive: every record already carries its system ruleset (`ruleset: {system, policy, analyzers}`, §3.2), and hosts must already reproduce historical semantics for historical views (§5.8, §27.3). What lets the family recur is the enumeration itself. A family-level guard removes the class: "`on⁻(o, K)` is a function of `o`'s record and `K`'s bytes alone; every semantics used to resolve and hash a recorded term is the one named in `o`'s record", with qualification that changes each ledger-named input (ruleset, system version, policy, structure, analyzer set, completeness standing, loss boundary) while holding `K` fixed and checks that `on⁻` does not change.

**Options for the stakeholder (Phase C handoff §5).**
- **(a) Subtractive (recommended):** `resolve_o` and `cid` use the system version named in `o`'s own record. State the guard above, and add the discriminator below. No new field, latch or exception.
- **(b) Subtractive + drop narrow match:** this does not by itself fix `on⁻`, so (a) is still needed.
- **(c) A different-family Review before or after the repair:** every Manual reviewer so far shares the author's family, and the last two matching findings concerned dimensions outside the enumerated frozen ones.
- **(d) Reconsideration above §6.6:** for example, adverse matching at raw-byte granularity independent of versioned resolution semantics.

**Required discriminator.** Run the trajectory above at the real owners, with a system-version adoption that changes normalization, and separately one that extends the anchor file-type table. Expected:
- `p` stays `on⁻ tree(a⁻)`, (2) fails, `undisputed = P`, and the adjudication obligation stays derived.
- For a D1/D2 claim, `adm(a⁻)` is unchanged by the adoption, the class stays R3, and the floor clause still fires.
- An implementation that re-resolves recorded terms under the current system version must fail.
- No §31.2 or §31.3 case changes the system version, so §31 passes with the defect.

### B3 — The veto formula and its prose contradict each other for product-scope rejections (§5.5 `vetoed`/`same`, §3.5, §10.2, §10.4; refinement R9)

**Text.** §5.5: "`vetoed(z) ⇔ z has a passing outcome ∧ ∃ admitted adverse j⁻ : kind(j⁻) = kind(z) ∧ same(j⁻, z) ∧ stands⁻(j⁻)`". The next paragraph: "`PRODUCT_SCOPE_ACCEPTANCE`, the same item at the same revision, and its `REJECTED` also vetoes a `GATE_DECISION` `ACCEPT` naming that surface (§3.5)". §3.5 lets a D1/D2 gate's `GATE_DECISION` accept the surface. `ADJUDICATE_DISAGREEMENT` (§10.2) and `REFUSED` (§10.4) both key on an adverse judgment "of its kind".

**Trajectory.** The product-scope owner records `PRODUCT_SCOPE_ACCEPTANCE REJECTED` for marked surface `m` in D1 unit `u` at revision `r`. Later the D1 gate holder records `GATE_DECISION ACCEPT` for `u`'s revision, naming `m`.
- **Formula reading:** the gate `ACCEPT` stands, `m` binds D4 although its owner rejected it, and no adjudication is derived. The disagreement is resolved by kind and order.
- **Prose reading:** the whole `GATE_DECISION` is vetoed, which also withholds the D1 revision's gate. The gate obligation is answered, so it is never re-dispatched and a later passing gate decision bound to it is refused (§8.3 step 7). No `ADJUDICATE_DISAGREEMENT` is derived, because the veto is cross-kind. The D1 subject stays invalid with no derived route to resolution.

An implementer must choose between the two statements, and each choice has a defect.

**Violated text.** Manual §0.4 S12: "A marked product inspectability surface beyond the requested deliverable is accepted only by the product-scope owner". Scientific checks: "a marked item beyond the requested deliverable binds only after the stakeholder or task authority accepts it". Workflow owner: "it cannot erase unresolved contradictory material evidence by vote". R9's own property: "a review or acceptance disagreement is never resolved by re-dispatch, count or order".

**Earliest owner.** Manual §5.5 (R9), with §3.5. A clean local defect introduced by the c6da678 N2 repair.

**Minimum repair direction (subtractive).** A gate that accepts a surface records that acceptance as its own `PRODUCT_SCOPE_ACCEPTANCE` (same kind), co-submitted with the `GATE_DECISION`. The existing same-kind veto, adjudication and `REFUSED` rules then apply to the surface alone, the gate's acceptance of the revision is untouched, and the cross-kind clause is deleted.

**Required discriminator.** Both orders of `REJECTED` and a gate `ACCEPT` naming `m`. Expected: `m` does not bind D4; the owner's adjudication obligation is derived; the D1 revision's gate acceptance is unaffected. An implementation that follows either current statement alone must fail.

## 2. Non-blocking findings

- **N1 — Residual read classification (§4.2, §20.1 versus §6.3; c6da678 N7 residue).** §6.3 records "every file of the realization's tree ... whether or not the file is governed" as a read entry. §4.2 and §20.1 still say "A read outside the governed tree is recorded by content identity where it can be pinned", which places ignored tracked files on the external side. §6.3 is the single recording rule, so the conflict is resolvable. But the §4.2 reading has a permissive branch: realization currency ignores pins, so a passing realization would stay current after an ignored tracked file it read changed. Replace "outside the governed tree" with "absent from the tree" in both places.
- **N2 — The environment/external boundary decides whether any mechanical stop exists (§6.3, §20.1, §17.2).** "A read of a file absent from the realization's tree is an external read". A runner that observes all reads sees interpreter, standard-library, system-library and compiler files, and files the execution itself wrote (build products, bytecode caches). Most are not pinnable by the §20.1 grammar. If they are unpinnable, every such observation is out of every permissive use, so no failure ever stops mechanically. That fails closed, but it is an architectural choice an implementer must make. State which reads are recorded execution environment (configuration fields) and which are external inputs, and that self-written files are outputs, not inputs. §32.2's "A failure caused by an unfixed external input" understates the effect: any failure whose run read an external locator stops only through runs with the same pins.
- **N3 — The per-polarity fail-closed value for unresolvable frozen-analyzer terms is permanent (§6.3; c6da678 N6 repair).** "Counts as matching for `on⁻`" places such an observation in (2) and (4) for every `K` whose other terms match, for as long as the ledger exists. After an analyzer adoption, every later same-region failure of that configuration therefore goes to the owner, and for D1/D2 to the floor. Prefer scheduling an R0 `ANALYZER_OUTPUT` of the frozen analyzer on `K` before declaring a term unresolvable, or list the cost as a reopen trigger.
- **N4 — Structure-dependent `ABSENT` versus structure-free re-resolution (§1.3, §1.4 rule 3, §1.5, §6.3).** §1.4 rule 3 makes partially overlapping regions of distinct units "resolve to `ABSENT`", which depends on sibling terms, but the frozen context holds none. If `cid` at recording uses rule 3, re-resolution on the same tree disagrees: `on⁻(o, tree(o))` is false, and `o` leaves (2) and (4) (permissive, integrity-finding edge). State that `cid` is term-level (§1.3) only, or record the sibling terms as for residual parts.
- **N5 — Intake dispositions (§5.5, §8.3 step 4, §18.3; c6da678 N2 residue).** Adoption enacts `Σ` at admission (S0), so a later standing adverse disposition vetoes only the `ABSORB` record's S2 currency, never the adoption. First-come enactment remains; answered-obligation refusal mitigates it only for bound dispositions. Non-`ABSORB` dispositions (for example `QUARANTINE` versus `RETAIN_AS_EVIDENCE`) can contradict each other with no veto, and the S2 effect of `QUARANTINE` ("excluded from governing context, evidence and acceptance basis") is not derived anywhere. State the effect of an adverse disposition on an enacted adoption (realignment and adjudication obligations) and the derivation of `QUARANTINE`.
- **N6 — R9 reach (§5.5 `same`, §16.5; c6da678 N10 residue).** Now that `same` covers "the same plan item at any of its revisions", an R2 amendment that changes what the item asks keeps a `NO_PASS` vetoing a `PASS` on identical content. This is restrictive, and owner adjudication resolves it. In the other direction, any byte change to a changed unit escapes the veto; the re-review then receives earlier "findings that no later judgment resolved" by default, but "resolved" is undefined and policy may withhold them. Define resolution of a review finding.
- **N7 — A normalization change re-identifies every revision (§1.5, §27.3).** Under the current semantics, every recorded `rev` and every acceptance's `content` entry becomes non-current after a normalization change. That is restrictive, but it means mass re-acceptance, including D1/D2 human gates, and neither §27.3 nor §32.3 discloses it. The B2 repair (record-named semantics) also gives a mechanical bridge, because machinery "decides only byte identity and §1.5 normalization".
- **N8 — Closure map (aid only).** Item 23's DECIDED relies on the §1.2 attribution (B1), and item 5's REFINED relies on R1's frozen context (B2). The R9 bullet's product-scope sibling inherits B3.

## 3. Closure audit (§21 items and §16.2 rows)

The closure map was used to locate text only; its annotations were checked against the Manual.

- **Not substantively resolved:**
  - item 5 (`on` and assessed content: the frozen resolution context omits system-version semantics, B2);
  - items 23-24 (write-scope rules and the domain rule over a syntactic write set, B1);
  - item 3 (adverse outcomes and their effect: the cross-kind contradiction, B3);
  - item 27 (the §29.4 revising row and §29.5 documentation row E0 claims depend on B1).
- **Resolved with non-blocking defects:** item 4 (read classification and the environment boundary, N1-N2; the residual-part `cid` is now defined); items 5 and 19 (analyzer fail-closed permanence, N3); item 1 (overlap `ABSENT`, N4); item 12 (intake disagreement and `QUARANTINE` effect, N5); item 7 (`REFUSED` now named and keyed on `same`, closing c6da678 N5); item 18 (normalization evolution, N7).
- **Resolved:** items 2, 6, 8 (`ref` resolution now part-scoped), 9, 10, 11, 13, 14 (with R4), 15-17, 20-22, 25 and 26. Each decision was located and is a decision, not a route. Delegated D4 space is bounded, and nothing incidental is over-specified to a blocking degree. The anchor file-type table is delegated although it changes normalization, which touches B2.
- **§16.2:** every row of both workplan tables, including every Deferred row, has a final disposition in §26.4 (with §26.3 for invariant 4, §4, §5, §6, §7, §9-§12, §14 and §18). None found unresolved.

## 4. Refinements R1-R9

| # | Assessment |
|---|---|
| R1 | **Sound in polarity, incomplete in its frozen context.** The SD-12 construction rule holds in both directions (§9 of this record): `on⁻` reads only tree-resident terms, pins and unpinnable reads enter only `on⁺`, every use names its predicate, and `on⁺ ⇒ on⁻` holds, including for the unresolvable-analyzer case. Relative to workplan §6.6, the adverse side is a superset and the permissive side a subset, which is a sound refinement except where the frozen context fails to freeze (B2). |
| R2 | **Sound.** Clamping every non-trivial strongly connected component to `F` only lowers values; the veto is an S0/S1 constant inside `base`. |
| R3 | **Sound.** |
| R4 | **Sound** (failure points re-checked at text level; the VM-snapshot residual is disclosed). |
| R5, R6, R7 | **Sound.** |
| R8 | **Sound.** Peer supersession is excluded; "own author's reassessment" is now stated as human-only in practice. |
| R9 | **Partly sound.** The carrier, answered obligations, the item-revision-independent `same`, `stands⁻` with `¬superseded`, completeness member revisions and the named `REFUSED` value close c6da678 B2, N1, N3, N4 and N5. The cross-kind product-scope clause contradicts the formula (B3); intake vetoes are inert against enacted adoptions (N5). |

## 5. Previous findings, Phase B closures and N1-N4

**c6da678 blockers.**
- B1 **closed**: `on⁻` compares tree-resident terms only. `ext` makes `on⁺` require equal pins on shared locators and no unpinnable read on either side, and (1), (3) and the class rule read `on⁺`. The c6da678 trajectory now leaves `p` in (2), with `q` excluded from (3). The unpinnable variants keep (2) failing, and `adm` holds for an unchanged-region candidate (R3). The matching family itself is not closed (B2).
- B2 **closed**: `same` for transformation reviews and conformance now reads "the same plan item at any of its revisions and the same candidate content". The R1-tightening trajectory is vetoed and `REFUSED`, with adjudication derived.
- B3 **partly closed**: manifest keys and semantic tables of a D1-D3 unit are attributed to it. The governed-boundary and new-part routes remain open (B1).

**c6da678 non-blocking.** N1 closed (`¬superseded(d)`). N2 partly closed (intake and product-scope added; B3, N5). N3 closed. N4 closed. N5 closed. N6 closed as specified, with residue N3. N7 partly closed (§6.3 fixed; §4.2 and §20.1 residue, N1). N8 closed. N9 closed. N10 partly closed (findings by default; N6). N11 closed. N12 closed in §30; the map is current except as N8.

**b595f2c blockers.** B1 closed (SD-11 recording; the c6da678 review's checks re-verified for the span-sibling, sibling-file, ignored-file and prefix-addition variants). B2 closed. B3 partly closed, the same family as B1 here. B4 closed by R9, with residue B3 and N6.

**b595f2c non-blocking.** N1, N2, N3, N5, N6, N7 and N8 closed as checked against the text. N4 closed by SD-12.

**6ff4ed1 blockers.** B1 closed for effective structure (frozen terms; `on⁺ := on⁻ ∧ …`); its sibling dimension, the system version, is B2. B2, B3 and B4 closed.

**6ff4ed1 non-blocking.** N1-N12 closed as checked against the text (N1 "not computable" vs "either"; N3 `qualification` field; N4 "no new component and no existing one grows"; N5 machinery `COMPLETENESS`; N6 `CHALLENGES` excluded from cycle legality; N7 disjointness, empty prefix and `EVIDENCE_RECORD` layer-free; N8 qualification-owned; N9 and N10 rows added; N11 export listed; N12 defaults marked).

**Phase B §3 closures.** Clause comparison of §5.3-§6.10 with workplan §6.6 and §10 found restated, and in R1's direction only narrowed permissively or widened adversely: S1 polarity, `cont`, `base`, `ev`, `undisputed`, `qual`, `about`/`starts`/`home`, Y1/Y2 coverage, the class rule's candidate-own exception, absorbed-reading exclusion, never-lost salvage, independence and unknown authorship, retirement/split/retarget and `eff`. **Exception:** "nondeterministic old-content observations defeat (2)" fails across a system-version adoption (B2).

**Both directions.** Permissive: B2 hides a live failure and lowers a D1/D2 class; B1 lets authority change without the revising duty; B3 (formula reading) resolves a product-scope disagreement by kind; N1 and N4 are narrow. Restrictive: B3 (prose reading) stalls a D1 gate with no route; N3 makes analyzer-unresolvable observations permanent adverse matches; N6 vetoes across R2 amendments; N7 mass invalidation. Unpinnable-read observations now in (2) and (4) are restrictive with cause. Nothing else resurrected a settled failure or withdrew a stop without cause.

**Phase B N2 re-test.** Take a bounding completeness judgment that becomes `P`, blocked, revoked, superseded, loss-withheld or vetoed by an `INCOMPLETE`. A differing old-content run on an alternate tree differing only outside the recorded regions (including another span of a recorded file) stays in (2), and a yielding present-content run stays in (4), because `on⁻` reads no S2 value, no current `Σ`, `ignore` or analyzer and no pin. That holds, except across a system-version adoption that changes resolution semantics (B2). The support-cycle clamp (R2) and the corrupt-prefix halt (R3) are specified fail-closed before any current assertion. Phase B N1 remains open and disclosed (§32.2). The N3 limits are carried in §31.3. The N4 costs are in §32.3, including unpinnable inputs, analyzer retention and veto stalls.

## 6. Out-of-matrix trajectories attempted

**Broke the candidate:**
- B1: an `ignore` change moving bytes into or out of a D2 `prefix` unit; a new part with a semantic table; a D4 unit moved into a D2 composite.
- B2: normalization change, anchor file-type extension or `cid` re-tag under a live nondeterministic disagreement; the D1/D2 `adm` and class consequence.
- B3: product-scope `REJECTED` against a gate `ACCEPT` naming the surface, in both orders.
- N4: overlapping-anchor `ABSENT`.
- N5: adverse intake disposition after an enacted adoption.

**Held:**
- **Matching polarity (SD-12):** the c6da678 external-input trajectory; a passing run on `tree(a⁻)` differing only by an unpinnable read (stays in (2)); an unpinnable failing realization with an unchanged-region candidate (`adm` true, R3, floor); a reproduction under another pin (not (1)); a fix that stops reading the locator (`ext` vacuous, (3) can hold); real `a⁻` with an unpinnable read (never stale; owner).
- **Every consumer reading one record:** currency (`execution` mode plus `record` entries on bounding completeness), (1)-(4), `adm`, the floor and the class rule. Each `on⁻` occurrence sits in a restrictive position, and each `on⁺` occurrence in a permissive one.
- **Matching invariance with unchanged content:** byte-preserving refinement; `ignore` adoption; analyzer adoption (fail-closed per polarity); a unit removed after realization; completeness lost in six ways; loss boundary (standing only); frames and rebases (`tree(a⁻)` fixed; lineage frames count).
- **Content changes matching must see:** another span of a recorded file (not seen, as the reviewed `on` requires); a recorded region; a prefix gaining a file; a widened directory gaining a governed file; the manifest semantic table of a bounded unit (bounding completeness goes non-current through `rev`, so currency and `on⁺` fall while `on⁻` stays adverse); observed whole-file reads (consistent with the reviewed `on`, since the execution read the whole file).
- **Derivation and stratification:** the veto reads S0/S1 only; `stands⁻` chains; the support graph with `execution` and completeness edges.
- **Roles, envelopes and R9:** the c6da678 B2 trajectory; contrary judgments in both orders; peer supersession rejected; an answered obligation not re-dispatched; a reviewer result without its `TASK_RESULT` or with an empty `bidirectional` slot; adverse judgments across a loss boundary; an unbound adverse judgment (restrictive; disclosed stall trigger).
- **Domain rule:** a D2 unit's own semantic table, scope or membership edited from an `IMPLEMENT` item (now a `VIOLATION`).
- **Publication and currentness:** the R4 failure points; settlement before human decisions; the ABA residual.
- **Gates and floors:** a floor item cannot be reclassified; an unqualified gate `ACCEPT` is refused while disputed evidence is listed.

## 7. Minimum architecture and capability transfer

No component, tier or record kind is added. R9 adds a derived rule, an obligation state and a discharge value. R1 adds a per-realization resolution context and an operational duty to keep analyzer sets, disclosed as a reopen trigger. All three B-repairs remove or reuse mechanism rather than adding it:
- B1 replaces an attribution rule with the existing `Δ(X)` and structure comparison;
- B2 reads the record's existing `ruleset.system`;
- B3 replaces a cross-kind clause with a same-kind record.

The removals (R4, R5) drop no owner-required capability.

1.6.0 transfer is complete in §26.4. PC-001 (`AUTHORITY_BOUND`) was independently resolved at the public source ("When a new profile becomes current, every older supported profile remains frozen and independently testable.") and is preserved: Core imports nothing from SSDS (§26.2), §31.8 tests Core without SSDS, and the frozen 1.6.0 file, `source/` and `dist/` are byte-unchanged.

PEM basis: `origin/main` = `af0455753e20ee54a969c844872e29e270007211`, PEM blob `1561797125622f355f84eb27319f87e8fa4227d9`, identical at the candidate. The validator (identical blob) reports "PEM schema 1 valid: 5 families, 0 notices" in the working tree; run against the Git-less snapshot it reports route unavailability, as expected. HAS dispositions: PC-001 applicable and binding; DS-001, SP-001, SP-002 and FF-001 applicable as evidence only. DS-001 bears on §8 of this record.

## 8. Qualification design

§31 binds claims to real owners and marks every runtime group UNEXECUTED; nothing beyond §31.10 is claimed as executed. Green §31 fixtures can coexist with all three blockers (DS-001):
- §31.5's c6da678 B3 case never changes `[governed]` or declares a part (B1);
- no §31.2 or §31.3 case changes the system version or the anchor table under a live disagreement (B2);
- §31.5's R9 cases run `GATE_DECISION` and `PRODUCT_SCOPE_ACCEPTANCE` only within one kind (B3).

The three discriminators in §1 are required. §31.3's external-input group now asserts the SD-12 behavior correctly. The §14.7 `HARD` qualification design is adequate as design, with proposed-default values. The diagnostic model was not run; it is unchanged since Phase B and models neither pins, system versions nor vetoes.

## 9. Doctrine-realization map and O1

E0/E1 claims are tied to existing mechanisms except two, both false on the B1 routes:
- §29.4 "revising D1/D2 ... **E0** (only an `AUTHOR` item can change D1-D3 units ...)";
- §29.5 documentation "never self-approve semantic changes ... **E0**".

The bidirectional E2 claim has a carrier and an admission check. The disclosed-E3 list (§29.6) is appropriately conservative, and the enumeration is complete with its catch-all row.

O1 (§0.5) states the realized record, readers, routine questions, realized-record architecture and marked surfaces, including the export and tool-independent ledger routes. "Beyond the requested deliverable: None" is consistent with the stakeholder record. Technical Review accepts no marked item, product scope or default value. B3 concerns the product-scope rule for projects SSDS governs, not SSDS's own marks.

## 10. What was verified and how; what was not

Executed against a `git archive` snapshot of the candidate under `/tmp/ssds80-manual-review-cc005db/cand`:
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- `git diff --check c6da678… cc005db…`: clean.
- `git diff --stat fad3ee4… cc005db…`: 12 files. These are the Manual, the closure map, three Manual review handoffs and three NO-PASS records, the Phase C handoff, a one-line session-handoff change, six lines in the stakeholder record (SD-11 and SD-12) and two index lines. The c6da678..cc005db diff touches the Manual, the closure map, the c6da678 handoff and record, and the stakeholder record (SD-12).
- `orchestrator/docs/architecture.md` (blob `39e6de7…`), `source/` (tree `fac2238…`) and `dist/` (tree `6bf729e…`) are identical at `fad3ee4…` and the candidate.
- All header blobs match. PEM validated as in §7.
- Owners read at the public source: the D3 entrypoint (source and expanded dist), architecture-and-design, abstraction-and-concretization, convergence (active simplification trigger; review strategy after recurrence), evidence, workflow (review and gate rules), versioning (PC-001), and the scientific-checks fragment (e=5, e=7).

Not verified:
- any runtime behavior (none exists); the trajectories are deductions from the specified contracts, not executed probes;
- the diagnostic model (not run);
- empirical costs;
- workplan §27 history and the earlier workplan NO-PASS records, beyond the Phase B record's and Phase C handoff's summaries;
- D1, D2, D4 and specialist entrypoint texts beyond the scientific-checks fragment and the Manual's citations.

## 11. Scientific-checks answers

- **Material findings:** B1-B3 and N1-N8 above. No agents were launched. The tools used were git, the unit test and the PEM validator; they produced no further findings.
- **Realized results:** this Review, including the tools it ran, produced, ran and reviewed no realized scientific results and prepared no gate evidence; its output is D3 review evidence toward G1. Null envelope:
  - *Examined:* the Manual in full; the c6da678..cc005db diff; the closure map; workplan §6.6, §10 and §21; the c6da678 Review record in full and the b595f2c and 6ff4ed1 finding lists; the Phase C handoff §5; the stakeholder record (SD-8 to SD-12); PEM identities; the governing owners listed in §10.
  - *Materially not examined:* workplan §27 and other sections not listed; the earlier workplan NO-PASS records; the diagnostic model's source; D1, D2 and D4 entrypoint texts beyond the scientific-checks fragment; any runtime system.
  - *Materiality basis:* decision relevance to G1 closure and to the Manual's §0.4 invariants.
- **Variants:** no analysis, pipeline, preprocessing, model or parameter variant was evaluated or selected (count 0). Constructed trajectories are review hypotheses. The repair options in §1 are proposals for the stakeholder, not a selected survivor. There was no delegated or resumed work.
- **Tension search:** not triggered. No consequential judgment relied on accepted project D1/D2 authority; the authorities used are SSDP 7.2.1 process owners, the stakeholder record and the reviewed workplan.

## 12. Common-mode note

This reviewer shares the Manual author's model family (Claude). It was launched by the authoring session from the issued handoff, and it shares the corpus, the inherited workplan framing and the toolchain. Fresh context is not epistemic independence. All four Manual reviewers were of the same family; the Phase B reviewer was of the GPT family. B2 is a dimension that the previous same-family review of R1's frozen context did not name, which makes the Phase C option of a different-family Review material.

## 13. D4 statement

No D4 is authorized. This NO-PASS accepts no architecture, product scope or default value. A later PASS would be technical evidence for G1 only. G1 also needs explicit stakeholder acceptance, and shadow D4 needs G2.
