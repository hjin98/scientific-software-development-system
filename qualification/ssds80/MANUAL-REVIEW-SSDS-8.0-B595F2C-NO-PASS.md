# SSDS 8 Architecture Manual — Independent D3 Review, candidate b595f2c

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout /home/user/scientific-software-development-system)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: b595f2c5794ad906cb3b9b89ba15fe2c5be1e784
    SCOPE: the whole proposed Manual as durable D3 owner: (a) §21 and §16.2 closure; (b) fidelity to the
           Phase B-reviewed workplan, including refinements R1-R8; (c) out-of-matrix adequacy; (d) inheritance
           and capability transfer (Architecture 1.6.0, workplan §18, PEM HAS); (e) qualification design;
           (f) doctrine-realization map; (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob 08270e2a6fc5bb015d793021f3933a9bafcf623c (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md, blob f6568e50a04a7b42634f40b886351375d2611887 (verified)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23;
           Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b97fb8152d2a5742e17fa172e12204756, verified);
           blob at the candidate 91bde236465178f20c7348280e036d2884dfc216 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml)
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS (HYPOTHESIS ONLY): MANUAL-REVIEW-SSDS-8.0-6FF4ED1-NO-PASS.md; WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md;
           the earlier workplan NO-PASS records
    REVIEW METHOD: entry through source/roles/software-design/SKILL.md at the public source; owner reconstruction
           (architecture-and-design, abstraction-and-concretization, convergence, evidence, workflow, versioning,
           scientific-checks fragment); independent §21/§16.2 audit; clause comparison of Manual §1-§17 and §26-§31
           with workplan §6-§7 and §16.2; diff review 6ff4ed1..b595f2c; constructed trajectories in permissive and
           restrictive directions; G1 document checks executed at a git-archive snapshot of the candidate
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session

The Manual's refinement table, decision markers, §30 pass and qualification claims, the closure map, commit messages, the handoff's scope text, workplan §0.1/§27 rationale, the diagnostic model's results and every prior Review record were treated as hypotheses. Section numbers refer to the Manual at the candidate unless prefixed "workplan".

## SERIOUS CHALLENGE

**None.** No accepted governing authority was found false, contradictory, ambiguous, inadequate or unrealizable. The 7.2.1 evidence owner ("A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority."; "Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position."), the workflow owner ("A synthesizer reconciles findings through evidence and owner adjudication; it cannot erase unresolved contradictory material evidence by vote."), the scientific-checks e=5 revising duty and the D3 owner's "one authoritative representation/state" are coherent and realizable here. Every blocker is a defect of the proposed Manual. Each can be repaired at its own sections without changing a parent.

## Verdict

**NO-PASS.** Four blockers survive. B1 is a non-local recurrence in the assessment-disagreement family: the repair of the previous B1 changed the granularity of the matching predicates, so a live failure can again be hidden. B2 and B3 are partial closures of the previous B2 and B4 with clean local residues. B4 is a pre-existing defect in review/acceptance discharge that earlier reviews did not find. This verdict accepts nothing and authorizes no D4.

## 1. Blockers by earliest owner

### B1 — Recording the execution basis as whole Git objects narrows the adverse predicates below the reviewed contract; a nondeterministic failure of unchanged content is hidden and misattributed (§6.3, §6.5, §6.6, §6.8, §17.2; refinement R1)

**Change.** The reviewed contract (workplan §6.6) says: "`on(o, K)` holds when content `K` (a tree, or a frame's content) has, on every unit and widened scope of execution `o`'s recorded execution basis, the content identity and membership `o` recorded." It also says: "A passing realization's currency reads the same execution basis (§10), so a change that makes passing evidence stale is exactly a change that a pair must see." The 6ff4ed1 Manual kept that granularity. The candidate records the executed content "as **Git object identities at paths** ... the blob identity of every file containing any region the closure or the observed reads reached" (§6.3). `on⁻` compares those whole-file blobs (§6.5). §17.2 now records the executed content "twice, for two consumers": unit-revision `content` entries for realization currency, and Git objects for `on⁺`/`on⁻`, the floor and the class rule. Wherever a unit is a span (a `symbol`, `heading` or `anchor` term), `on⁻` is now *stricter* than the reviewed `on`: a byte change anywhere else in the same file breaks the match. In the adverse conditions (2) and (4), a stricter predicate is the permissive direction, because fewer observations keep the failure counting.

**Trajectory (every step locally conforming).**
1. `src/kern/f.py` holds `solve` and `helper`. Composite `kern` (D4) has parts `kern.solve` (`symbol = "kern.f.solve"`) and `kern.helper` (`symbol = "kern.f.helper"`). Specification `S` (declarative oracle; thread scheduling is a free attribute) declares `EXECUTION_DEPENDS_ON kern.solve`. Current singleton `COMPLETENESS(EXEC)` judgments on `{S}` and `{kern.solve}` bound the closure. The designated runner reports no observed reads. Claim `c` is evidenced by `S`. `solve` has a race: about half its runs fail `l2_error`.
2. At admitted tree `T0` a realization `p` passes and is assessed `PASS`. Its recorded basis is `blob(f.py@T0)` and `blob(S)`.
3. An `IMPLEMENT` item changes only `helper`. Its contract requires `S` on the exact candidate `C`. The run on `C` fails, and an independent assessor records `a⁻` (frame record, `F(a⁻) = {l2_error}`). The obligation is admitted, so `a⁻` starts counting in the admitted state at once. Its recorded basis is `blob(f.py@C)` ≠ `blob(f.py@T0)`.
4. In the admitted state `G` (tree `T0`), `(1)` lacks a reproduction, so §6.9 schedules one on `C`. It fails, which happens about half the time: (1) holds. (2): `p` has `on⁻(p, C) = F` (different blob), so only failing runs are on `tree(a⁻)`; (2) holds. (3): `p` has `on⁺(p, T0)`. (4): only `p` matches `T0` under `on⁻`, and it passes. Therefore `stale_G(a⁻)`, `undisputed = T`, `ev = T`, and `c` stays valid. Nothing is scheduled for the owner.
5. Under the reviewed contract, `p` is `on` `C` (`kern.solve` and `S` are unchanged), so it enters (2) with another outcome. (2) fails, which means nondeterministic in fact, and the failure goes to the owner. If `c` is or was D1/D2, the floor (§6.8) fires at once, because "`a⁻`'s assessed content was the admitted content at its base". Under the candidate, the assessed content is compared as blobs, so that clause is false. (2) does not fail and no observation of admitted content yields, so **no floor event occurs** and no human sees the failure. A discriminating reading's class (§6.8, `on⁺(p, base(a⁻))` with "assessed content not the admitted content") is likewise lowered to R2.

The same effect follows from a change to another unit's file inside a recorded directory tree, or to an ignored tracked file under one. In the restrictive direction, if "directory scope" in §6.3 does not cover a non-widened `prefix` unit, then a file added under that prefix changes the unit's content without changing `on⁻`. An old yielding run then keeps (4) false against content it never read, and the failure can never become stale mechanically. Under the evidence owner's rule that is a stale failing observation counted against current authority.

**Violated text.** The evidence owner: "A valid failing observation is evidence." and "Do not suppress contradictory admissible observations to manufacture a pass". The Manual's own §6.6: "**Nondeterminism goes to the owner.** (1) and (2) need an identical second execution on the content `a⁻` read and no other outcome there, ever." Here `p` is an execution on the content `a⁻` read, as §6.3 defines executed content, with another outcome, yet (2) excludes it. Also Manual §0.4 S4, and the workplan's alignment sentence quoted above, which §17.2's two recordings drop without saying so. R1's stated property, "never removes an adverse recorded match", holds only relative to the candidate's own recording, not to the reviewed contract. The Phase B closures 6FE1000 B2 and 4EC0024 B′2 ("nondeterministic old-content observations defeat (2)") no longer hold for span-granular content.

**Earliest owner.** Manual §6.3/§6.5/§17.2 (R1 recording decision).

**Convergence assessment.** This is a **non-local recurrence**. The matching clause has now produced findings in five successive reviews: `ef8445a` N2, `552ac01` N2, Phase B N2, `6ff4ed1` B1, and this one. The mechanism is not a missing condition. Each repair redefines "the same content" for some consumers while others keep a different notion, and this candidate now persists **two representations of one executed content** (§17.2). The convergence owner names that as an active simplification trigger ("duplicated/synchronized authoritative state"), and the D3 owner prefers "one authoritative representation/state". Do not add a latch or an exception. Phase C handoff §5 binds the next step for further non-local recurrence: present the stakeholder's options (subtractive repair, judgment-only assessor-read staleness, different-family Review, reconsideration above §6.6) instead of choosing silently.

**Minimum repair direction (subtractive).** Record the execution basis **once**, at the reviewed granularity: the recorded scope terms with the identities of their resolved regions, plus directory or root-tree identities only where the closure actually widened to them. Fix the resolution context (the `ignore` patterns and the analyzer pinned at the realization's own position) at recording time, and use it whenever a recorded term is re-resolved in `K`. Then `on⁻` never reads the current `Σ` or analyzer, which keeps the previous B1 closed. Keep `on⁺ := on⁻ ∧ (bound ∨ same root tree)`. Realization currency, (1)-(4), the floor and the class rule must all read that one recorded basis. A further simplification is to drop narrow permissive matching altogether (`on⁺ := on⁻ ∧ same root tree`). That removes `bound`, the S2 read inside `stale`, support-graph edge 4 and the §5.1 exception. It costs reruns that §6.9 already schedules, and it is a choice for the author and stakeholder.

**Required discriminator.** The trajectory above, plus sibling-file-in-directory and ignored-file variants, at the real owners. Expected: `p` stays in (2) on `tree(a⁻)`, `undisputed = P`, the owner adjudication obligation is derived, and for a D1/D2 claim the floor fires at the first position. A prefix-addition variant: a non-yielding run on the new content makes the failure stale. An implementation that compares whole-file blobs, or that uses different recorded bases for currency and matching, must fail. The §31.3 cases as written ("an alternate tree that differs ... only outside the recorded narrow basis") are satisfied by the defect, because the recorded basis is now whole files.

### B2 — Item prose behind a `ref` outside the item's part changes without plan acceptance (§11.1, §13.1, §13.4, §4.3; previous B2 partly closed)

**Trajectory.** The candidate makes an amendment R2 unless "the item's prose is byte-identical", including "every span a `ref` names" (§13.4). That classification runs only when the item part's revision changes. Nothing requires a `ref` to resolve inside the item's own part. §11.1 and §13.1 say so only in comments inside example blocks, which §0.1 makes non-normative, and lint (§13.2) and the plan invariants (§11.3) check unit references only. Suppose a principal writes `statement = { ref = "#appendix-o1" }`, pointing into a plan appendix that sits in the plan composite's residual part, or into another item. `PLAN_ACCEPTANCE` names in its basis only the objective section and the item revisions (§4.3). The principal edits the appendix, which is within its write scope, "its plan's units". The item's revision is unchanged, so `sat(content)` holds by `cur(u) = r` and no amendment class is ever computed. The item stays issuable. Every later brief renders the new statement, and `REVIEW`-verified obligations are judged against it.

**Violated text.** Workplan §7.9: "**Every other change is R2** ... That includes ... changing any statement or primary verifier". The workflow owner: "Orchestration may represent pending/accepted/rejected state but cannot self-approve it." Manual §0.4 A5.

**Earliest owner.** Manual §13.2 lint / §11.1. A clean local defect.

**Minimum repair direction.** Lint rejects any `ref` that does not resolve inside the item's own part. The plan `Objective` part is the one allowed exception, because it is `EXACT` in the plan acceptance's basis. Alternatively, the `PLAN_ACCEPTANCE` mechanical minimum takes `EXACT` content entries on every unit a `ref` resolves to.

**Required discriminator.** An item whose statement `ref` resolves outside its part is rejected at lint, or editing the referenced span makes the item non-issuable and derives `PLAN_ACCEPT`. An implementation that computes coverage from the item part's revision alone must fail.

### B3 — `DOCUMENT` items may revise D1-D3 authority without the revising, tension-search and O1 duties (§13.2 domain rule, §13.3, §13.5, §16.3, §16.6; previous B4 repair)

**Trajectory.** The new domain rule lets a `DOCUMENT` write scope "contain any non-protected unit". A change to a D1-D3 unit only "needs that domain's acceptance" before anything relies on it. The duties owed when D1/D2 authority is revised are triggered only by item kind `AUTHOR`: the `revision_assessments` slot ("`AUTHOR` items revising D1/D2 authority"), the `o1_content` slot, the injection event "`AUTHOR` revising D1/D2 authority", and the §13.3 minimum ("an `ACCEPT` obligation at the domain's class, and the `o1_content` slot"). A plan item of kind `DOCUMENT` rewrites a section of an accepted D2 method unit. Lint passes, the task's brief carries the documentation core only, no slot asks for the tension search or the per-tension applicability assessments, and the D2 gate's §16.6 section 3 renders nothing. No rule marks that section as missing, so the gate looks complete. The human accepts the revision without the assessments the owner says the gate receives.

**Violated text.** Scientific checks e=5: "When revising ... D1/D2 authority, also search recorded tensions bound to its accepted concretizations. In the revision's own record and its gate evidence, record the predecessor identity and, per found tension, a revision-scoped applicability assessment". The workflow owner: "A gate accepting a D1/D2 revision receives the revising duty's tension applicability assessments". Manual §0.4 A4 ("a duty a task owes is carried in its brief or enforced mechanically; activation is deterministic"). The §29.4 claim "E2 (`revision_assessments`) + **E0** (the gate core renders them)".

**Earliest owner.** Manual §13.2 domain rule with §13.5/§16.3 triggers. A clean local defect introduced by the B4 repair.

**Minimum repair direction.** A `DOCUMENT` write scope contains no D1, D2 or D3 unit, so authority text changes only through `AUTHOR`. Alternatively, key the slots, injection and §13.3 minimum on "write scope contains a unit of that domain" instead of on item kind.

**Required discriminator.** A `DOCUMENT` item whose scope contains a D2 unit is rejected at lint, or its brief carries the D2 revising and tension-search duties and both slots, and the D2 gate core renders the assessments. A trigger keyed on `AUTHOR` alone must fail.

### B4 — An adverse review or acceptance can be outvoted by re-dispatch; reviewer tasks have no result record (§10.2-§10.4, §12.3, §13.5-§13.6, §8.3 step 3 R8 catch-all)

**Trajectory.** Reviewer A records `REVIEW NO_PASS` on candidate `X`, with material findings in its review. Discharge (§10.4) needs only "∃ current judgment ... with outcome in passing(o)", so a `NO_PASS` has no effect on discharge. `REVIEW(X)`'s trigger, "a task result whose conformance is `CLEAN`", still holds. The obligation therefore stays derived and ready, and dispatching ready obligations is the Dispatcher's operational choice (§10.3). The budget does not stop re-dispatch. The `REVIEW` system contract has "budget 1", but iterations are "`k` counts the admitted `TASK_RESULT` records bound to `o`", and the reviewer template (§12.3) may not submit `TASK_RESULT` at all. A review obligation's iteration count therefore never advances. Reviewer B, fresh and independent, records `PASS`; `REVIEW(X)` discharges and §11.5 integrates `X`. `ACCEPT(s)` has the same shape: a `FAIL` leaves `s` without a valid acceptance, `ACCEPT(s)` is re-issued, and a later `PASS` makes `s` valid. R8's catch-all lets "any other support-tier record" be superseded "by a record of the same kind on the same target, by an actor qualified for that kind". In the other direction, a later qualified `FAIL` can therefore permanently supersede an earlier `ACCEPTANCE PASS`. Both directions resolve a judgment disagreement by order. The same gap leaves the required review slots (`claims`, `findings`, `bidirectional`, §13.6 and §16.5) without a carrier. Slots live on `TASK_RESULT` (§13.5), conformance and `slots_filled` evaluate only task results (§14.1), and reviewers cannot submit one. So "an empty slot is `INCOMPLETE`" is unenforceable for review tasks, and the §29.3 E2 claim for bidirectional Review has no mechanism.

**Violated text.** The workflow owner: "it cannot erase unresolved contradictory material evidence by vote". The convergence owner: "No recurrence count, review count, cycle budget, or convergence target can force acceptance". The evidence owner's disagreement rule against "latest-editor order". The contradiction between §13.5/§13.6 and §12.3 is one an implementer cannot resolve without choosing between them.

**Earliest owner.** Manual §10.2-§10.4 (discharge and iteration identity, §21 item 7), §12.3/§13.5-§13.6 (items 23-24), and the §8.3 step 3 R8 catch-all. The discharge formula is inherited from workplan §7.4. The iteration rule (TASK_RESULT counting) and the reviewer template are Manual decisions.

**Minimum repair direction.** Every task ends in one result record carrying its slots, which counts its iteration; reviewer tasks submit it alongside their judgment. A `REVIEW` or `ACCEPT` obligation is answered by its first admitted judgment, and a `NO_PASS`/`FAIL` closes it negatively. The next attempt is a new candidate or revision. Re-judging the same candidate or triple happens only through supersession by the same judge or owner/human adjudication, which extends the reviewed assessment rule to these kinds. That rule also replaces R8's peer catch-all.

**Required discriminator.** A `NO_PASS` on `X` followed by an independent `PASS` on the same `X` does not integrate `X` without an adjudication. `FAIL` then `PASS` on one triple leaves `s` invalid without one. An empty `bidirectional` slot on a scientific review discharges nothing. An implementation that discharges on ∃`PASS`, or that re-dispatches an answered review, must fail.

## 2. Non-blocking findings

- **N1 — Analyzer completeness records (§2.6, §3.4).** A `MACHINERY` R0 `COMPLETENESS` record conflicts with §3.4's producer column ("qualified actor; R2"). Its "pinned analyzer identity" basis has no basis-entry mode (§4.1), so whether it stays current after an analyzer `RULESET_ADOPTION` is undecided. That is a permissive input. Recommend defining the entry (satisfied iff the identity is in `ρ_n`'s set) and amending §3.4.
- **N2 — Analyzer inputs beyond the pinned identity (§5.9, §14.5).** C++ interface extraction "after preprocessing under the declared build configuration" reads host headers, which are not ledger-named. State that any host-dependent analyzer output is recorded as `ANALYZER_OUTPUT`.
- **N3 — Ruleset text not updated.** The §3.4 `RULESET_ADOPTION` row and §27.1 still name only "system ruleset version plus policy digest". §5.2, §5.9 and §28 include the analyzer set.
- **N4 — External pins in matching (§6.3, §6.5).** `on⁻` is defined over tree paths only, so a recorded external pin cannot be compared with `K`. Runs reading different pinned external inputs therefore match as the same content. The effect is restrictive only. It is inherited from the workplan.
- **N5 — Single-provisional residue.** §31.2 "Corrupt prefixes (R3)" still lists the single-provisional rule as an `INTEGRITY_HALT` cause. §5.7 and §23.4 moved it to qualification (previous N8).
- **N6 — Doctrine-map overclaims (§29).** The D4 "never weaken tests ... **E0**" claim holds only for `IMPLEMENT`/`REPAIR` items. `MIGRATE` and `DOCUMENT` items changing D4 test units have no mandatory `TEST_INTEGRITY` minimum (§13.3). The maintenance-audit row cites "the audit item's result outcome", but no template has `HEALTHY`/`WATCH`/`ACTION REQUIRED` outcomes (investigator outcomes are `FOUND`/`NONE_FOUND`/`INCONCLUSIVE`). The bidirectional E2 claim depends on B4.
- **N7 — §30 statements are stale.** "R1 names two existing uses' polarity" and "no new persistent surface". The candidate R1 changes the recorded representation and persists a second copy of the executed content (B1).
- **N8 — "the item's own document units"** in the `AUTHOR` domain rule (§13.2) is undefined; plan units are outside every implementer scope.

## 3. Closure audit (§21 items and §16.2 rows)

The closure map was used to locate text only. Its B1-B4/N1-N12 annotations were checked against the text.

- **Not substantively resolved:** item 7 (discharge and iteration identity let adverse judgments be outvoted; B4); items 23-24 (review-task result carrier and system contracts; B4; `DOCUMENT` write-scope rule; B3).
- **Resolved with blocking defects:** items 4-5 (executed-content recording and `on`; B1); item 8 (plan structure and amendment; B2); item 27 (doctrine map; claims in §29.3/§29.4 depend on B3/B4; N6).
- **Resolved with non-blocking defects:** item 2 (analyzer completeness; N1); items 5/19 (analyzer pinning; N2, N3).
- **Resolved:** items 1, 3, 6, 9-22, 25 and 26. Each decision was located and is a decision, not a route. Delegated D4 space is bounded, and nothing incidental is over-specified to a blocking degree.
- **§16.2:** every row of both tables, including every Deferred row and the 1.6.0 §4 and §14 rows added for the previous N10, has a final disposition in §26.4. None found unresolved.

## 4. Refinements R1-R8

| # | Assessment |
|---|---|
| R1 | **Sound in its implication, unsound in its recording.** `on⁺ ⇒ on⁻` now holds by construction and is independent of `Σ`, which closes the previous B1. The switch to whole Git objects is a semantic change to the reviewed matching granularity that the R1 row does not disclose, and it defeats nondeterminism detection and the floor (B1). It needs different treatment. |
| R2 | **Sound.** Clamping every non-trivial SCC to `F` only lowers values. Edge 4 is included. |
| R3 | **Sound.** The fail-closed halt is defined. Moving the single-provisional check to qualification is correct; see N5. |
| R4 | **Sound** (independently re-checked). A restart after a successful CAS, two processes on one key, a copied operator state and a paused publisher against a fence all keep at-most-once execution and decision-after-settlement. The VM snapshot residual is disclosed. |
| R5 | **Sound.** The extended rule 1 and the outermost-owner treatment of `ssds.unclassified` keep the partition. |
| R6 | **Sound.** |
| R7 | **Sound.** Excluding `CHALLENGES` from cycle legality and well-formedness now makes "adds no S2 input" exact. |
| R8 | **Partly sound.** The assessment, report and consultation rows reconcile workplan §7.9/§11.4 with step 3. The catch-all for "any other support-tier record" widens the reviewed rule ("own assessor's reassessment or the owner's adjudication") to any qualified peer, which permits resolution by order (B4). It needs different treatment. |

## 5. Previous findings, Phase B closures and N1-N4

**6ff4ed1 blockers.** B1 is **closed for its trajectory**: after refinement, `ignore` or re-scope adoption with an identical tree, `on⁻` is unchanged, `bound` fails, `on⁺` needs the same root tree, `o_r` and `r2` keep (4) false, and `undisputed = P`. **The family is not closed** (B1 above). B2 is **partly closed**: in-part prose is closed, but a `ref` outside the item's part is open (B2). B3 is **closed**: the analyzer set is pinned by `ρ_n`, a host lacking it makes no current assertion, historical views keep their set, and §27.3/§28 agree (residues N2, N3). B4 is **closed for its trajectory**: obligation kinds, holder, §13.3 minimum, injection and the domain rule exist. The `DOCUMENT` branch of the new rule opens B3.

**6ff4ed1 non-blocking.** Closed: N1 ("not computable" restricted to outputs `G`'s reading evaluates), N3 (`qualification` field), N4 (no new or grown SCC), N6, N7, N10, N11 and N12. The map's default list and the R4 residual were checked. N2 is closed by R8, apart from the catch-all (B4). N5 is closed in intent, with gaps (N1). N8 is closed in §5.7 with a residue in §31.2 (N5). N9 is closed with overclaims (N6).

**Phase B §3 closures.** Clause-by-clause comparison of §5.3-§6.10 with workplan §6.6 found the S1 polarity, `cont`, `base`, `ev`, `undisputed`, `qual`, `about`/`starts`/`home`, Y1/Y2 coverage, the class rule's candidate-own exception, absorbed-reading exclusion, never-lost salvage, independence and unknown authorship, retirement/split/retarget and the identity floor restated. **Exception:** the 6FE1000 B2 and 4EC0024 B′2 closure ("nondeterministic old-content observations defeat (2)"), with the immediate floor and the R3 class depending on "assessed content was the admitted content", no longer holds for span-granular content (B1).

**Both directions.** Permissive: B1 hides a live failure. Overridden challenges, loss boundaries, absorbed readings, unauthorized supersessions and test-first cases (the previous N1 repaired) held. Restrictive: B1's prefix-addition sibling keeps a stale failure counting. N4 does the same for external inputs. R8's catch-all permits peer withdrawal of acceptances. Nothing else resurrected a settled failure.

**Phase B N2 re-test.** For completeness becoming `P`, blocked, revoked, superseded or loss-withheld, and for structural changes, the differing old-content run and the yielding present-content run stay in (2) and (4) relative to the candidate's recorded basis, because `on⁻` reads no S2 value and no `Σ`. That holds. They do **not** stay when the alternate tree differs only outside the recorded regions but inside a recorded file (B1), a granularity failure independent of completeness. The support-cycle clamp (R2) and the corrupt-prefix halt (R3) are specified fail-closed. Phase B N1 remains open and disclosed (§32.2). N3 limits are carried in §31.3, and N4 costs are carried in §32.3.

## 6. Out-of-matrix trajectories attempted

Broke the candidate: B1 (sibling-span edit plus a flaky run; prefix addition), B2 (out-of-part `ref`), B3 (`DOCUMENT` revision of D2), B4 (review/acceptance re-dispatch; peer supersession).

Held:
- **Derivation:** monotonicity of `stale` through `bound`; the clamp with edge 4; the stratification check; analyzer adoption mid-dispute (adverse use unchanged, permissive use narrowed); historical views across an analyzer adoption.
- **Partition and scope:** `ssds.unclassified` with other top-level units; `prefix`-versus-span siblings; byte-preserving refinement keeps `scope_id` and tenure; freeze escape by re-scope.
- **Publication and currentness:** the R4 cases in §4; the provisional-chain check now in qualification; loss boundary withholding observations' permissive standing.
- **Roles and envelopes:** an `IMPLEMENT` scope containing a D2 unit is rejected; `AUTHOR` lineage self-acceptance is blocked by independence; a `DOCUMENT` edit leaves a D1 unit invalid until accepted; an in-part prose amendment is R2.
- **Gates and floors:** a `GATE_DECISION ACCEPT` with `UNQUALIFIED` refused while disputed evidence is listed; floor items not reclassifiable; human attention not closable by agents.

## 7. Minimum architecture and capability transfer

No new component, tier or record kind was added. The candidate adds one persistent duplicated representation, the second recording of the executed content (§17.2). That is the convergence trigger behind B1, and §30's "no new persistent surface" is inaccurate (N7). The removals (R4, R5) drop no owner-required capability.

1.6.0 transfer is complete in §26.4. PC-001 (`AUTHORITY_BOUND`) was independently resolved at the public source ("every older supported profile remains frozen and independently testable") and is preserved: Core imports nothing from SSDS, §31.8 tests Core without SSDS, and the frozen 1.6.0 file, `source/` and `dist/` are byte-unchanged. The PEM basis was verified: `main` = `af04557…`, PEM blob `1561797…` identical at the candidate, schema 1 valid, 5 families, 0 notices. HAS dispositions as inherited: PC-001 applicable, binding; DS-001, SP-001, SP-002 and FF-001 applicable as evidence only. DS-001 bears directly on §8 below.

## 8. Qualification design

§31 binds claims to real owners and marks every runtime group UNEXECUTED. Nothing is claimed as executed beyond §31.10. Green §31 fixtures can coexist with all four blockers (DS-001):
- §31.3's alternate trees differ only outside the recorded *files*, so B1 passes them.
- §31.5 tests prose-only amendments inside the item part only (B2).
- §31.5 checks that a `DOCUMENT` change leaves a D1-D3 unit unaccepted, not that the revising duties are carried (B3).
- No case re-judges an answered review or acceptance (B4).

The four discriminators in §1 are required. The §14.7 HARD-qualification design is adequate as design, and its values are proposed defaults.

## 9. Doctrine-realization map and O1

E0/E1 claims are tied to existing mechanisms except as noted. The overclaims are §29.3 D4 test integrity, the audit outcomes and the bidirectional E2 claim (N6, B4), and §29.4 revision assessments for the `DOCUMENT` path (B3). The disclosed-E3 list (§29.6) is appropriately conservative. Enumeration is complete with the new catch-all row.

O1 (§0.5) states the realized record, readers, routine questions, realized-record architecture and marked surfaces. The export surface is now listed (previous N11). "Beyond the requested deliverable: None" is consistent with SD-2. Technical Review accepts no marked item, product scope or default value.

## 10. What was verified and how; what was not

Executed against a `git archive` snapshot of the candidate under `/tmp/ssds80-manual-review-b595f2c/`:
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- `git diff --check 6ff4ed1… b595f2c…`: clean.
- `git diff --stat fad3ee4… b595f2c…`: the Manual, the closure map, the 6ff4ed1 handoff and NO-PASS record, the Phase C handoff, a one-line session-handoff change and two index lines.
- `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4…`.
- All header blobs match.
- PEM validator: schema 1 valid, 5 families, 0 notices. It ran in the working tree, because the archive lacks Git; the PEM and validator files are identical to the candidate's.

Owners were read at the public-source commit.

Not verified: any runtime behavior (none exists). The diagnostic model was not run; it is unchanged and models neither structural scopes nor recording granularity. Empirical costs were not assessed. The blockers are deductions from the specified contracts, not executed probes.

## 11. Scientific-checks answers

- **Material findings:** B1-B4 and N1-N8 above. No agents were launched. Tools were limited to git, the unit test and the PEM validator, and they produced no further findings.
- **Realized results:** this work, including the tools it ran, produced, ran and reviewed no realized scientific results and prepared no gate evidence. Its output is D3 review evidence toward G1. Null envelope, examined: the Manual in full; the 6ff4ed1..b595f2c diff; the closure map; workplan §6.6, §7.1-§7.4, §7.8-§7.10, §16.2, §21 and §25; the Phase B and 6ff4ed1 Review records; the Phase C handoff; the stakeholder record; PEM; 1.6.0 headings; the governing D3 entrypoint, the architecture, abstraction, convergence, evidence and workflow owners, and the scientific-checks fragment. Materially not examined: workplan §27 history and the earlier NO-PASS records beyond their summaries, the diagnostic model's source, specialist and D1/D2/D4 entrypoint texts beyond the Manual's citations, and any runtime system. Materiality basis: decision relevance to G1 closure and to the Manual's §0.4 invariants.
- **Variants:** none evaluated or selected. Constructed trajectories are review hypotheses, not analysis variants. There was no delegated or resumed work.
- **Tension search:** not triggered. No consequential judgment relied on accepted project D1/D2 authority. The authorities used are SSDP 7.2.1 process owners and the reviewed workplan.

## 12. Common-mode note

This reviewer shares the Manual author's model family (Claude). The authoring session launched it from the issued handoff, and it shares the corpus, the inherited workplan framing and the toolchain. Fresh context is not epistemic independence. The previous Manual reviewer was of the same family, and the Phase B reviewer was of the GPT family. Given B1's recurrence, the Phase C handoff's option of a different-family Review is material.

## 13. D4 statement

No D4 is authorized. This NO-PASS accepts no architecture, product scope or default value. A later PASS would be technical evidence for G1 only. G1 also needs explicit stakeholder acceptance, and shadow D4 needs G2.
