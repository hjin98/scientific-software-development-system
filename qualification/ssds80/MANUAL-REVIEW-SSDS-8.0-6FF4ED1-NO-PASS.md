# SSDS 8 Architecture Manual — Independent D3 Review, candidate 6ff4ed1

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout /home/user/scientific-software-development-system)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 6ff4ed1eeb91db5aff262eda8c85693dd50f0360
    SCOPE: the whole proposed Manual as durable D3 owner: (a) §21 and §16.2 closure; (b) fidelity to the
           Phase B-reviewed workplan, including refinements R1-R7; (c) out-of-matrix adequacy; (d) inheritance
           and capability transfer (Architecture 1.6.0, workplan §18, PEM HAS); (e) qualification design;
           (f) doctrine-realization map; (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob f754be55ab65ade52a9c1920ca3fa66a8a296e2c (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md, blob c4ed80c10d9e6a745cbc2304b083e8c43bca9fa2 (verified)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23;
           Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b...);
           blob at the candidate 91bde236465178f20c7348280e036d2884dfc216 (verified; delta is coordination text only)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (from PROTOCOL-RELEASE-STATE.yaml at the candidate)
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS (HYPOTHESIS ONLY): WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md and the 21 earlier NO-PASS records
    REVIEW METHOD: entry through source/roles/software-design/SKILL.md at the public source; owner reconstruction
           (architecture-and-design, abstraction-and-concretization, evidence, workflow, convergence, PEM,
           concurrency, storage, versioning); independent §21/§16.2 closure audit; clause-by-clause comparison of
           Manual §1-§7, §8, §10-§13, §22 with workplan §6-§7 and §15.3; constructed trajectories in both
           permissive and restrictive directions; minimum-architecture, qualification and doctrine-map audit;
           G1 document checks executed at the candidate
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session

The author's refinement table, decision markers, §30 pass, qualification claims, the closure map, commit messages, the handoff's scope description, workplan §0.1/§27 rationale, the diagnostic model's results and every prior Review record were treated as hypotheses. Section references are to the Manual at the candidate unless prefixed "workplan".

## SERIOUS CHALLENGE

**None.** No accepted governing authority was found materially false, contradictory, ambiguous, inadequate or unrealizable. The 7.2.1 evidence owner's rules ("A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority."; "An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.") and the D3 owner's "Each material current architecture claim has one semantic owner" are coherent and realizable here. Every blocker below is a defect of the proposed Manual (D3 candidate), repairable at its own sections without changing a parent.

## Verdict

**NO-PASS.** Four blockers survive. One (B1) is in the assessment-disagreement family and defeats the polarity property that refinement R1 asserts; three (B2-B4) are clean local defects in decisions the Manual itself introduces. None requires a parent change. This verdict accepts nothing and authorizes no D4.

## 1. Blockers by earliest owner

### B1 — `on⁺ ⇒ on⁻` is false under an effective-structure change with an unchanged tree; a live failure is hidden (Manual §6.5, refinement R1)

**Claim tested.** §6.5 defines `on⁻(o, K)` as "K has, on every unit and widened scope of o's recorded execution basis, the content identity and membership o recorded" and `on⁺(o, K)` as `on⁻(o, K)` when every bounding completeness judgment is current `T`, "K equals o's tree on the whole governed tree otherwise". It then asserts "`on⁺ ⇒ on⁻` always". §6.6's "Completeness polarity" bullet and R1's stated property ("it can never remove an adverse recorded match") rest on that implication.

**Why it fails.** The fallback branch of `on⁺` is not conjoined with `on⁻`, and the two depend on effective structure `Σ` differently. Membership digests and unit content identities are functions of `Σ` (§1.5, §2.6, §4.3, §5.2 `tgt`); "whole governed tree" depends on the `ignore` boundary in `Σ`. `Σ` can change while the tree does not: an `ABSORB` adoption of an already-absorbed quarantined delta in a records-only request (§8.3 step 4(a)), including the R0 machinery adoption of governance-neutral deltas (§18.4, `intake.neutral_auto`). After such a change, an observation recorded under the old `Σ` can have `on⁺ = T` (bounding completeness lost through `tgt`, identical tree) and `on⁻ = F` (membership or unit identity differs). It then serves the permissive conditions (1)/(3) and is excluded from the adverse conditions (2)/(4).

**Trajectory (every step locally conforming).**
1. Specification `S` with a declarative oracle; claim in subject `K` (D3 or D4, so no floor). Execution content: `S` plus composite `kern` (prefix `src/kern/`, part `kern.a`, residual). A current `COMPLETENESS` judgment `J` (EXEC) bounds the scope `X` = units of `kern` plus `S`.
2. A foreign push adds only a byte-preserving refinement of `kern.a` into parts `kern.a1`, `kern.a2` to the manifest; it is absorbed (tree `T1`). The delta is governance-neutral and stays quarantined; `J` stays current because `X`'s membership under `Σ1` is unchanged.
3. Evidence runs on `T1` under `Σ1`, narrow basis `X`/membership `m1` bounded by `J`: realization `r1` (seed 1) is assessed `PASS` (`p`); realization `r2` (seed 2, a different configuration) is assessed `FAIL` (`a⁻`). The failure is a real defect of admitted content. `a⁻` counts, and the Dispatcher's rerun obligation produces a reproduction `o_r` on `T1` with the identical outcome.
4. The neutral delta is adopted, mechanically (R0) or by an R2 reviewer: `Σ2`, tree still `T1`. `X` now has members `kern.a1`, `kern.a2`, so `J` fails `tgt` and is `F`. For `r2`, `o_r`: `on⁻(·, T1) = F` (membership `m2 ≠ m1`), `on⁺(·, T1) = T` (whole-tree equality).
5. `stale(a⁻)`: (1) `o_r` holds; (2) no observation has `on⁻` against `tree(a⁻)`, so it holds vacuously; (3) `r2` or `o_r` holds; (4) no observation has `on⁻` against `G`, so it holds vacuously. `a⁻` is stale and `undisputed = T`. `r1`'s currency is unaffected (refinement leaves every unit revision unchanged, and a `REALIZATION`'s mechanical minimum has no `record` entry on `J`), so `ev = T`, `valid(K) = T` and discharge is `DISCHARGED`. No rerun of seed 2 is derived, because a stale failure owes none (§6.9) and `REALIZE` is satisfied by `r1`.

The only observations of present content yield the failure, yet the failure stops counting. The stop came from a structural change, not from a judgment or discriminating evidence. Variants: an adopted `ignore` change that excludes a file the execution read (whole-governed-tree equality ignores it; the recorded unit identity changes), and an adopted governance-affecting re-scope run between absorption and adoption. For D1/D2 claims the §6.8 floor latched in step 3 still holds human attention, but S2 validity and discharge are wrong. The same `Σ` dependence can also remove a differing old-content run from (2) when the runs were recorded under different structures. That breaks the Phase B N2 property through a fifth way of losing completeness that §31.3 does not test.

**Violated owner text.** Evidence owner: "A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority." and "An unresolved material disagreement keeps dependent present guidance/closure visibly qualified." Manual §0.4 S4: "a failing assessment that counts keeps its claim qualified until a judgment addressing it, or discriminating evidence, disposes of it". Manual §6.1 stop clause: "only a judgment that addresses it, or evidence that discriminates in the observations, stops it".

**Earliest owner.** Manual §6.5 (R1 predicate definitions). The latent form is inherited from the workplan revision 23 standing clause, but the Manual states the false implication explicitly and owns the definition on acceptance.

**Convergence assessment.** This is the same family and the same clause as `ef8445a` N2, `552ac01` N2 and Phase B N2 (completeness polarity of observation matching). That is a recurrence signal under the convergence owner's "Review strategy after recurrence". It is not a reason for redesign, but it is a reason not to add another condition. The defect comes from defining the two polarities independently and asserting their relation instead of constructing it.

**Minimum repair direction (subtractive, no new latch or record).** Define one `Σ`-independent base predicate: `on⁻` compares the recorded region identities (terms and content identities as recorded at realization), never recomputed under a later `Σ`. Define `on⁺(o, K) := on⁻(o, K) ∧ (every bounding completeness judgment current T ∨ tree(K) = tree(o) as raw Git tree identity)`, so that `on⁺ ⇒ on⁻` holds by construction and the fallback cannot read the `ignore` boundary. A simpler option that removes more mechanism: drop completeness from permissive matching altogether (permissive uses require raw tree identity). `stale` then reads no S2 value, and support-graph edge 4 and the §5.1 completeness exception disappear, at the cost of more reruns. That is a cost choice for the author and stakeholder.

**Required discriminator.** The trajectory above with real owners: refinement adoption (R0 and R2), `ignore` adoption and re-scope adoption, each with an identical tree. Expected: `a⁻` keeps counting (`undisputed = P`), and differing old-content runs stay in (2). An implementation that evaluates `on⁻` under the current `Σ`, or uses an unconjoined whole-tree fallback for `on⁺`, must fail. Add these to §31.3 next to the four completeness-status variants.

### B2 — Plan-item prose can change under R1 "control tightening"; independent plan acceptance is bypassed (Manual §11.1, §13.1, §13.4)

**Trajectory.** §11.1 represents the item objective as `objective = { ref = "#objective-of-item" }` ("the prose objective for judgment is the item's own text"). §13.1 represents each obligation statement as `statement = { ref = "#o1" }` ("prose in the item section, for judgment"). §13.4 classifies an amendment R1 "iff every field of the item and its contract is unchanged or moved only in its tightening direction" and defines `r ⊑ r'` "iff every field of `r'` is reached from `r` by its direction". Prose is not a field. A principal (the contract's author) rewrites the prose behind `#o1` ("energy drift below 1e-8 over 10^6 steps" becomes "below 1e-3"), or the item's objective, constraints or non-goals, and leaves every TOML value unchanged. Lint computes R1. The `PLAN_ACCEPTANCE` entry (class `PLAN_CONTROL`, §4.3) stays satisfied through `r ⊑ cur(u)`, so the items stay issuable. Implementer and reviewer briefs (§16.3 item 5) now carry the new statement, and a `REVIEW`-verified obligation is judged against it. No independent plan acceptance ever saw it.

**Violated owner text.** Workplan §7.9 (reviewed contract): "Every other change is R2 ... That includes ... changing any statement or primary verifier"; and "Objective, governing units, acceptance criteria ... are unchanged". Workflow owner: a durable mutation follows "proposal -> independent falsification where required -> ... acceptance"; and "Orchestration may represent pending/accepted/rejected state but cannot self-approve it." Manual §3.5 / A5: "No actor reviews, accepts, conforms or plan-accepts its own work".

**Earliest owner.** Manual §11.1/§13.4 (a D3 decision on item representation and the tightening order). This is a clean local defect introduced by concretization.

**Minimum repair direction.** R1 additionally requires that every byte of the item part outside its `ssds-item` block, including every referenced prose span, is identical to the accepted revision. Any prose change is R2 (scoped or whole-plan per §11.4).

**Required discriminator.** An amendment that changes only referenced or unreferenced item prose, with byte-identical TOML, is classified R2. The plan acceptance stops covering the item, the item becomes non-issuable, and an independent `PLAN_ACCEPT` obligation is derived. A field-only comparator must fail. Add this to §31.5 "control-tightening classification", which currently generates diffs "over every field" only.

### B3 — The analyzer version in force is not bound to the ledger; derivation is not a function of `(L_n, content)` (Manual §1.3, §5.1, §5.9, §14.5, §27.3, §28)

**Trajectory.** Analyzer output feeds S0: `symbol` scope-term resolution ("as resolved by the language analyzer of the file", §1.3) and so `cid`, `rev` and `cur`; derived non-`NEUTRAL` relations (`EXECUTION_DEPENDS_ON`, `GENERATED_FROM`) and so cycle legality, `well_formed`, `ok` and `valid`; and diff-to-unit mapping for write-scope and conformance. Analyzer identity is not pinned by the ruleset or the system version. §27.3 lists what "belong[s] to the SSDS system version" (derivation semantics, normalizations, the merge implementation, check-template functions, canonical encodings) and omits analyzers. §14.5 delegates "Parser libraries and their versions, recorded in the analyzer identity". §5.9 keys derivation checkpoints by "(…, ruleset, schema, analyzer versions, system version)", treating the analyzer version as an input separate from the ruleset and system version. §31.2 expects divergence "under an analyzer-version change". Two conforming hosts at the same `L_n` with different installed parser versions therefore compute different `cur(u)` for symbol-scoped units and different derived-relation cycles. Admission validates on one derived state while the Interface presents another. A historical view at `m` recomputed after an upgrade differs from the one computed before it.

**Violated contract.** Manual §0.4 C2 ("same canonical inputs and ruleset give one derived state") and C8; §5.1 ("The ruleset and effective structure are read from `L_n`; nothing is supplied from outside. Derivation is a pure function."); §5.8 (historical views "reproducible with the ruleset in force at m"); workplan §6.6 determinism claim. This is an architectural decision an implementer would otherwise have to make.

**Earliest owner.** Manual §27.3/§28 with §5.1/§5.9.

**Minimum repair direction.** Pin every analyzer identity (id, version, configuration, parser identities) through the ruleset in force (`RULESET_ADOPTION`, human-gated as §27.3 already requires for the merge implementation), and add analyzers to the §27.3 list. Derivation at position `m` uses the analyzers pinned at `m`. A host lacking them makes no current assertion, as with an unreadable schema (§3.6).

**Required discriminator.** Two derivation hosts with different installed analyzer versions over the same `L_n` give identical `D_n`, or the mismatched host refuses. A historical view at `m` is byte-identical before and after an analyzer upgrade. An implementation that derives with the installed analyzer must fail.

### B4 — `AUTHOR` and `DOCUMENT` items have no obligation kind, holder role or system contract (Manual §11.1, §10.2, §12.3, §13.3, §13.5, §16.3)

**Trajectory.** §11.1 introduces item kinds `AUTHOR` and `DOCUMENT`. §13.3 sets their minimum verifier coverage. §13.5 triggers `o1_content` and `revision_assessments` on `AUTHOR` items. §16.3 injects owner text when the "obligation is `ACCEPT`, `REVIEW` or `AUTHOR`". §29.3-§29.5 realize the D1 recovery duty, the 7.2.1 authority-content (O1) duty, the D1/D2 revision duty and the documentation duties through `AUTHOR`/`DOCUMENT` briefs. Yet the closed obligation table (§10.2) derives work only from items of kinds `IMPLEMENT`, `REPAIR`, `MIGRATE` and `INVESTIGATE`. No §12.3 role template holds an `AUTHOR` or `DOCUMENT` obligation, and §13.6 gives them no contract. An accepted `AUTHOR` item therefore derives no obligation and is never issued. The alternative is that an implementer improvises a holder. That is an authority decision (A5): the principal may not write authority units, the investigator may not, and the implementer's template neither holds the kind nor states that its write scope may include D1-D3 authority units. §29.3 also claims "write scope excludes higher-domain units" as an E0 mechanism.

**Violated contract.** Workplan §21 item 23 ("the system role templates, their obligation kinds, record kinds, outcomes and write-scope rules") and item 24 ("minimum verifier coverage per item kind ... and the system contracts"), under §25 criterion 2. Scientific checks e=7 ("When authoring or materially revising D1/D2/D3 authority ... state the material realized record ..."), whose E2 realization the Manual places on tasks that cannot exist. Internal contradiction: §16.3 names an obligation kind that §10.2's closed list does not have.

**Earliest owner.** Manual §10.2/§12.3/§13.6.

**Minimum repair direction.** Add `AUTHOR` and `DOCUMENT` obligation kinds with triggers. Assign their holder (an implementer-template narrowing whose write scope may contain only the item's authority or document units, never protected surfaces), and state the separation from the `ACCEPT` and `REVIEW` holders. Give them system contracts. Reconcile the §29.3 E0 claim.

**Required discriminator.** An accepted `AUTHOR` item for a D2 unit derives exactly one authoring obligation held by the stated role. Its brief carries the D2 core, the revising and tension-search duties and the `o1_content`/`revision_assessments` slots. The result cannot be accepted by the authoring lineage. A role outside the template is rejected writing the D2 unit.

## 2. Non-blocking findings

- **N1 — "not computable" versus a test-first case (§6.5, §6.6).** The mechanical "yields" clause treats a verdict that is "FAIL, or not computable" as yielding. A candidate's test-first case `x` is not evaluated by the admitted reading. Read literally as "not computable", `x` would never become stale in the admitted state, which would also fire the D1/D2 floor. That contradicts the "either" clause and §6.6's "test-first case is stale in the admitted state as soon as the admitted reading passes the admitted outcome". The specific clause controls under ordinary interpretation, so this is not a blocker. Restrictive direction. Recommend: "not computable" applies only to an `x` that `G`'s reading evaluates. Add an embedded-oracle test-first case to §31.3.
- **N2 — Supersession authorization is stated only for assessments (§8.3 step 3).** Read literally, the rule ("a record may name `x` in `supersedes` only as `x`'s own assessor's reassessment or the owner's adjudication") forbids §20.2's mandatory consultation supersession and §15.2's raiser supersession of reports. Read narrowly, it leaves supersession of other support records (acceptances, completeness, gate decisions) unauthorized-by-default unspecified. This is inherited from workplan §6.8. Recommend a per-kind supersession authority table.
- **N3 — `GATE_DECISION.qualification` is missing from the closed schema.** §16.6 requires a `qualification` field and refuses `ACCEPT` with `qualification = UNQUALIFIED` under stated conditions; §3.4 lists only `adequacy`.
- **N4 — Admission "stays acyclic" with a pre-existing absorbed cycle (§8.3 step 5, §5.6).** Read literally, once absorption creates a support cycle, every non-repair request fails `CYCLE_SUPPORT`. Recommend "introduces no new non-trivial component". Liveness only.
- **N5 — Analyzer completeness versus closure (§2.6, §4.6, §6.3).** §2.6 lets an analyzer "supply boundary completeness"; §4.6 narrows only on `COMPLETENESS` judgments, and `on⁺` consults only judgments. State whether analyzer declarations narrow recorded bases. If they do, they are permissive inputs with no revocable record (this interacts with B1/B3).
- **N6 — R7 claim.** An authored `CHALLENGES` edge is `ACYCLIC` and so enters cycle legality, `well_formed`, `ok` and `valid`. "Adds no S2 input" holds only for warrant. A writable tension home could, in contrived configurations (D4 code reading that home by path), place an authority on an illegal cycle. Recommend excluding `CHALLENGES` from cycle legality, or saying so.
- **N7 — Static disjointness and `prefix = ""`.** §1.4 rule 1 omits sibling `prefix`-versus-span terms (rule 3 handles them dynamically, so the partition holds). §1.8's `ssds.unclassified` uses `prefix = ""`, which violates §1.3 ("must end in `/`") and conflicts with every other top-level unit. EVIDENCE_RECORD's layer is undefined for layer constraints.
- **N8 — The single-provisional rule as a derivation-time halt (§5.7).** Provisional versus admitted is witness state, which §5.1 keeps out of derivation. Assign the check to qualification.
- **N9 — Doctrine map completeness (§29; §21 item 27).** Several entrypoint duties have no row: D1/D2 independent evidence routes for common-mode risk; D2 correlated tests; D3 "Priority changes investigation effort, not the pass threshold" and Stabilization; D4 obsolete or duplicate ownership and documentation impact; documentation reader and terminology duties; the audit HEALTHY/WATCH/ACTION REQUIRED output. §16.3 carries the full entrypoint text, so these are E3 in substance. Add a catch-all row or the rows.
- **N10 — 1.6.0 coverage.** §4 (layout, packaging, namespace) and §14 (CLI capability behavior) of Architecture 1.6.0 have no disposition row in workplan §16.2 or Manual §26.4. §26.3 covers their substance; record the dispositions.
- **N11 — O1 surface list.** `sdp ssds export` snapshot export (§26.3, §26.4 Tracker row) projects realized records but is not listed among §0.5's within-deliverable surfaces.
- **N12 — Closure map inaccuracies (aid only).** The map lists the 168-hour cap and the cutover reconstruction minimum among proposed defaults; the Manual marks the cap a D3 decision and does not mark the minimum `[proposed default]`. R4's VM-snapshot residual is disclosed in §32.2 and absent from the map's R4 rows.

## 3. Closure audit (§21 items and §16.2 rows)

The closure map was used only to locate text. Each item was checked against the Manual's own decision.

- **Not substantively resolved:** item 23 and item 24 for the `AUTHOR`/`DOCUMENT` item kinds (B4). Items 5 and 19 are incomplete with respect to analyzer identity as part of the versioned derivation (B3). Item 27 is substantively resolved with incomplete enumeration (N9).
- **Resolved with defects found:** item 5 (`on` matching, B1; "not computable", N1); item 8/24 (control-tightening order, B2); item 3 (gate schema field, N3); item 13 (consultation supersession versus step 3, N2).
- **Resolved:** items 1, 2, 4, 6, 7, 9, 10, 11, 12, 14 (with R4; see §4), 15, 16, 17, 18, 20, 21, 22, 25 and 26. Each decision was located in the cited sections and is a decision, not a route. Material decisions are marked and delegated D4 space is bounded (merge diff implementation, parser libraries, mutation tool, storage engines, reason-code members, limit values). No incidental D4 machinery was found over-specified to a degree that blocks.
- **§16.2:** every row of both tables, including all Deferred rows (invariants 4, 9, 15, 17 and 26; §5 sub-rules; §6; the §7 CandidateRef/StageResultEnvelope mapping; §9-§11 functions; §12 layout; §18 fitness), has a final disposition in §26.4/§26.3. The only gap is 1.6.0 §4/§14 without rows (N10).

## 4. Refinements R1-R7

| # | Assessment |
|---|---|
| R1 | **Unsound as stated** (B1). The polarity labels at each use site are correct and close Phase B N2 for the four named completeness states. The asserted `on⁺ ⇒ on⁻` fails under a `Σ` change with an unchanged tree. Repair: construct the implication. |
| R2 | **Sound.** Forcing every non-trivial SCC to `F` before evaluation makes the workplan's promised `F` explicit and only lowers values (S2 monotone). Restrictive cost: over-approximated edges (2 and 4) can force `F` on subjects whose real support is acyclic; disclosed as a finding. See N4 for the Admission wording. |
| R3 | **Sound fail-closed narrowing.** `INTEGRITY_HALT` is a defined state; positions before it stay derivable. Never-lost records arriving during a halt wait in the Dispatcher journal, and those in an abandoned interval are lost and disclosed (§15.2). The single-provisional check belongs to qualification (N8). |
| R4 | **Sound specialization.** Every Manual behavior is one the workplan procedure already allowed: a restart is treated as "log lost", and "log lost" leads to a fence. At-most-once holds per incarnation, and decision-after-settlement is unchanged. Process-image cloning (VM snapshot/restore, fork) duplicates an incarnation and only matters in the ABA case; it is disclosed in §32.2. Cost: a human decision after every crash inside the publication window, a reopen trigger in §32.3. It answers §21 item 14 by removal, surfaced in §0.3 and §30. |
| R5 | **Sound** (partition holds by rules 1-4 together). Editorial gaps are noted in N7. |
| R6 | **Sound.** Byte-preserving refinement keeps `scope_id`, `rev` and tenure. A governed-boundary change alters covered regions without changing `scope_id`; the workplan already distinguishes "scope_id or the byte regions it covers", and `rev` captures the bytes. |
| R7 | **Sound for warrant.** The "adds no S2 input" claim is inexact (N6). |

## 5. Phase B closures and N1-N4

Manual §5.3-§5.6 and §6.1-§6.10 were compared clause by clause with workplan §6.6. S1 polarity, `cont`, `base`, `ev`, `undisputed`, `qual`, `about`/`starts`/`home`, reading coverage (Y1), the class rule (Y2, X3), the identity floor (N4 of `552ac01`), the absorbed-reading exclusion, never-lost salvage, authorized supersession, the independence and unknown-authorship rules, and the retirement/split/retarget rules restate the reviewed text. The changes are the `on⁺`/`on⁻` labels, "not computable", the explicit `INCOMPLETE` exclusion and the 168-hour cap. Every Phase B §3 closure therefore still holds in text, except where B1 reaches it.

Both directions of the family were attacked. In the permissive direction, B1 hides a live failure. Overridden challenges, loss boundaries, absorbed readings, perturbed outcomes, retargeted obligations and unauthorized supersessions held. In the restrictive direction, N1 (literal reading) would keep test-first failures counting and fire floors. R2's over-approximation can invalidate genuinely valid subjects after absorption (disclosed). Nothing else resurrected a settled failure or withdrew a stop without cause.

Phase B N2: the differing old-content run and the yielding present-content run on an alternate tree that differs only outside the narrow basis stay counted under completeness `P`, blocked, revoked, superseded and loss-withheld, because `on⁻` reads no S2. **They do not stay counted under a `Σ` change (B1).** The support-cycle clamp (R2) and corrupt-prefix halt (R3) are specified. N1 remains open and is correctly disclosed (§32.2). N3 limits are carried into §31.3. N4 costs are carried into §32.3.

## 6. Out-of-matrix trajectories attempted

Trajectories that broke the Manual: B1 (structure adoption with an identical tree), B2 (prose-only amendment), B3 (analyzer upgrade across hosts and historical views), B4 (accepted `AUTHOR` item).

Trajectories that held:
- **R4 publication:** paused publisher versus takeover fence; two processes sharing a host key; restart after a successful CAS; fence chains and settlement; ABA after a fence (detected).
- **Partition and scope (R5/R6):** foreign files under a prefix; crossed and moved anchors (`ABSENT`, residual); escape from a challenge freeze by re-scope, membership change or boundary change (frozen); `ignore`-pattern tenure.
- **Prefixes and S1:** corrupt authenticated prefix; unreadable newer schema; loss boundary with `COMPLEMENT`/`EXPLICIT` attestation; counter-challenge across a boundary.
- **Admission and roles:** never-lost salvage in rejected requests; an unauthorized `supersedes` sibling; forged or absent envelopes; a `governs` mismatch; principal tightening to infeasibility; partition with overlapping write scopes; risk-override scope excluding `GATE`/`HUMAN_ATTENTION`/`ADJUDICATE`/`INTEGRITY`.
- **Disagreement family:** provisional discharge only inside override scope or policy; discriminating readings under absorbed readings; embedded oracle under absorption (fail closed); ensemble rerun-to-pass.

Non-blocking issues found along the way: N1-N8.

## 7. Minimum architecture and capability transfer

§30's keep/remove table is accurate. No new primitive, component, persistent surface or disagreement-family mechanism is added. Both removals (publication-attempt log, dynamic partition check) drop no owner-required capability: the log's only unique capability was restart without a human decision, a liveness convenience. B1's preferred repair would remove a further mechanism (the S2 read inside `stale`).

Capability transfer from 1.6.0 is complete except for N10. PC-001 (AUTHORITY_BOUND; owner independently resolved to the 7.2.1 versioning owner, "every older supported profile remains frozen and independently testable") is preserved: Core is untouched, Core imports nothing from SSDS (§26.2), §31.8 tests Core without SSDS installed, and the frozen 1.6.0 file is byte-unchanged. The PEM basis was verified: `main` = `af04557…`, PEM blob `1561797…`, schema valid with 5 families and 0 notices. All five families were dispositioned; DS-001, SP-001, SP-002 and FF-001 apply as evidence-only, as the map states. Workplan §18.1/§18.2 rows land in the Manual as mapped; spot checks found no dropped capability.

## 8. Qualification design

§31 binds claims to real owners, keeps the diagnostic model diagnostic (DS-001), and marks every runtime group UNEXECUTED. Nothing is claimed as executed beyond §31.10. However, green §31 fixtures can coexist with all four blockers:
- §31.3's polarity cases vary only completeness status, not `Σ` (B1).
- §31.5 generates tightening diffs over fields only (B2).
- §31.2's analyzer discriminator tests cache keys, not version pinning (B3).
- No case issues an `AUTHOR` or `DOCUMENT` item (B4).

The four discriminators in §1 should be added. The §14.7 HARD-qualification design (frozen thresholds, Wilson bounds, real trajectories) is adequate as a design, and its values are proposed defaults.

## 9. Doctrine-realization map and O1

Every duty that appears in §29 is classified honestly. E0 claims are tied to mechanisms that exist in the Manual, with two exceptions: §29.3's "write scope excludes higher-domain units" depends on B4, and the O1 and D1/D2-revision E2 slots depend on `AUTHOR` tasks existing (B4). The §29.6 disclosed-E3 list is appropriately conservative, including detection. Enumeration gaps are in N9.

O1 (§0.5) has a realized record, readers, routine questions and realized-record architecture. Surfaces are marked within the deliverable, and "beyond: None" is consistent with the stakeholder's direction (SD-2 inspector flow), with the export surface left unmarked (N11). Technical Review accepts no marked item, product scope or default value.

## 10. What was verified and how; what was not

Executed at the candidate (`git archive` snapshot under `/tmp/ssds80-manual-review-6ff4ed1/`):
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests OK.
- `git diff --check e23f142… 6ff4ed1…`: clean.
- `git diff --stat fad3ee4… 6ff4ed1…`: the Manual and closure map added, plus the Phase C handoff, a one-line session-handoff change and two index lines.
- `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4…`.
- All blobs in the header match.
- The workplan delta since Phase B is coordination text only.
- PEM validator: schema 1 valid, 5 families. This ran in the working tree; the sources are identical to the candidate's.
- Diagnostic model, default mode (optional): REV23 depth 4, 1,574,464 transitions, 0 failures. It does not model any Manual clause, structural scopes or per-observation completeness, so it bears on none of the findings.

Owners were read at the public-source commit.

Not verified: any runtime behavior (none exists); the depth-5 report; the stakeholder's 2026-10-12 instruction (N1); empirical costs. B1-B4 are deductions about the specified contracts, not observed behavior. B1 was derived from the predicate text without an executed probe.

## 11. Scientific-checks answers

- **Material findings:** B1-B4 and N1-N12 above. No tools or agents were launched beyond the listed scripts.
- **Realized results:** this work produced, ran and reviewed no realized scientific results. Its only output is D3 review evidence toward G1, an architecture gate rather than a scientific-results gate. Null envelope, examined: the Manual in full, the closure map, workplan §2, §6, §7, §15.3, §16-§18, §21, §25 and §26, the Phase B review, the Phase C handoff, the stakeholder record, PEM, Architecture 1.6.0 headings, and the governing role, specialist and owner texts. Materially not examined: the workplan §27 history in detail, the 21 earlier NO-PASS records beyond the Phase B summary, the diagnostic model's source, and any runtime system. Materiality basis: decision relevance to G1 closure and to the invariants of Manual §0.4.
- **Variants:** none evaluated or selected. The existing diagnostic model was run once in its default mode, with no change after seeing results. Constructed trajectories are review hypotheses, not analysis variants. No delegated or resumed work.
- **Tension search:** not triggered. No consequential judgment relied on accepted project D1/D2 scientific authority. The governing authorities used are SSDP 7.2.1 process owners and the reviewed workplan.

## 12. Common-mode note

This reviewer shares the Manual author's model family (Claude). It was launched from the issued handoff by the authoring session, and it shares the corpus, the inherited workplan framing and the toolchain. Fresh context does not establish epistemic independence. The Phase B reviewer was of the GPT family. A different-family review of the repaired candidate would reduce this common-mode risk.

## 13. D4 statement

No D4 is authorized. This NO-PASS accepts no architecture, product scope or default value. Even a later PASS would be technical evidence for G1 only. G1 additionally requires explicit stakeholder acceptance; shadow D4 requires G2.
