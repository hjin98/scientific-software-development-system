# Independent D3 Review — SSDS 8 Architecture Manual, candidate 82d618c

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          82d618cd26900f8cb7b0aaa6be7cac3d3a7c030c
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g));
                        technical evidence for G1 only
    MANUAL blob:        fef0e1536f06ec7190ba44d40c5a4ecd12a4a73e (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   73db03c733c8530027834c1dae98cd802d414596 (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family edabd81
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; delta-first attack of the subtractive
                        corrections in both directions; the handoff's six drift classes applied to every
                        place that states the dependence mode, the revalidation route, "counts", answering
                        and the content-versus-identity reach; an admissible-answer-or-route check over every
                        §10.2 obligation kind, including after integration (this settles edabd81 N7);
                        family-level recheck of earlier families; diagnostic model run in full (parallel, all
                        families and mutations); structural checks of handoff §3 step 9
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched
                        by the authoring session; did not author the candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-82d618c/snap`. The later commit adding the handoff (`54d8343a`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. The accepted SSDP 7.2.1 owners and the stakeholder's recorded decisions (SD-1 to SD-35, record items 19 and 31) can be realized together. The blocker below has its root in text the Phase B Review passed (workplan §6.8 step 8 together with the §6.9 role table and §7.4 discharge), which the Manual restates and sharpens (§7.3, §8.3 step 8, §10.4). The Manual owns the decisions that resolve it (workplan §21 items 6 and 7), so it is routed as a blocker against the proposed D3 owner. Any resolution narrows the literal reviewed step 8, so it must be listed in §0.3 as a refinement for the stakeholder to see.

## Verdict

**NO-PASS.** One blocker, in a family no earlier Review established (edabd81 N7 and 653e88c "noticed, not established"):

- **B1**, Admission no-collateral-regression / obligation lifecycle after integration. Obligations keyed on an item revision, a transformation or a change event (`IMPLEMENT`-family item obligations, `REVIEW(X)`, `JOINT_INVARIANT(i, k)`, `SPEC_REVIEW`) stay derived after their work integrates. Their discharge reads review and task-result judgments whose output and read entries have "ordinary currency in the admitted state", and discharge is not latched (§10.4). Admission step 8 refuses any request after which such an obligation is no longer discharged. A conforming Admission therefore refuses every later item that edits a unit an earlier integrated item changed, every second change in a joint invariant's scope, and every change to a file a discharged item's implementer or reviewer read. Step 8's "affected" and "stays discharged" are not defined anywhere else, and the Manual states no lifecycle end for these obligations.

The candidate's own corrections hold for the trajectories that motivated them. edabd81 B1 is closed: Admission step 7 now reads the same `standing` entry as §4.1/§4.3/§10.2. edabd81 B2 is closed in text: the root clause is gone, `REVALIDATE` is derived for every acting non-current judgment a current obligation depends on, and §4.1, §5.5, §10.2, §10.3, §11.5, §12.3 and §31.6 agree. Acceptance and gate objections are back on S10's exact subject triple, which removes edabd81 N2's ambiguity and cost. The diagnostic model is green on all five families and catches all 34 mutations. It cannot see B1, which lies outside every family it models.

## Blockers

### B1 — Admission step 8 refuses legitimate later changes because integrated, event-keyed obligations stay derived and their discharge reads exact-content judgments

**Family:** Admission no-collateral-regression and the obligation lifecycle after integration. It is a "what a basis entry imports after integration" defect, one of the handoff's six drift classes: step 8 states a regression rule, while §10.4's discharge, read through §7.3's post-integration roles, computes something much broader. **Earliest owner:** reviewed workplan §6.8 step 8 with §6.9 (role table: output "ordinary currency in the admitted state: a later edit of `u` makes it stale") and §7.4, as restated in Manual §7.3, §8.3 step 8 and §10.4; the decision belongs to workplan §21 items 6 (Admission validation order) and 7 (obligation rules, readiness, discharge). **Status:** open, material. It is not a recurrence of the judgment-disagreement, matching or change-rule families. It is non-local: §7.3, §8.3 step 8, §10.2 (obligation triggers and identities), §10.4 and §13.7 each contribute.

**Exact rules at the candidate.**

- §8.3 step 8 (line 1189): "every obligation discharged at the current head and affected by the merged tree stays discharged, with affected evidence rerun. The only legal way to reopen others' closures is an accepted change to a prerequisite authority … This step concerns the request's content and structural changes". "Affected" is defined nowhere else in the Manual.
- §10.4 (line 1319): "Discharge is not latched: an obligation discharged at one head is `OPEN` at a later one whose state no longer satisfies the predicate. Admission step 8 keeps admitted requests from doing that to others' closures; an absorbed foreign change can, and then a discharged implementer obligation is ready again, as drift to repair". §13.7 (line 1534) repeats this: "if `a` later drifts, `a` reopens and is dispatched". Both statements are the Manual's own: the workplan has no "not latched" or "drift to repair" text, so the Manual itself made the persistence explicit.
- §10.4 `discharged(o)`: "∃ current judgment j of kind(o) on subject(o) …". §11.5 step 3 and §8.3 step 7: an integrating request claims its obligation "only together with its current review judgments". §14.4: "`REVIEW`-verified obligations stay open until a current review judgment".
- §10.2 triggers. `IMPLEMENT`, `REPAIR`, `MIGRATE`, `AUTHOR` and `DOCUMENT` each fire on "an accepted, issuable item of that kind with a contract". `REVIEW(X)` fires on "a task result whose conformance is `CLEAN`". `JOINT_INVARIANT(i, k)` fires on "an admitted change touching a joint invariant's scope". None names an end: unlike `ACCEPT`/`GATE`, which are keyed on the current triple, these obligations are not re-keyed when content moves. An item stays issuable while a current plan acceptance covers its revision (§11.2), and code changes do not touch that acceptance.
- §4.3: `REVIEW` and `TASK_RESULT` carry frame-role `content` on every unit of `Δ(X)` and on recorded reads (§4.2: "every `read` through the interface during the task"). Target entries are `EXACT` (§4.3 preamble), so no equivalence covers them. §7.3, after the integrating admission: output entries have "ordinary currency in the admitted state", and context entries the same.

**Decisive trajectory (two items, one file).**

1. A plan holds accepted items `I1` and `I2`, both `IMPLEMENT` with write scope `src/solver/`; `I2` `depends_on` `I1`. Leaf unit `u` is `src/solver/step.py`.
2. `I1`'s task produces `X1`, which changes `u` to `rev(u, C1)`. The review `r1` (PASS, frame `id(X1)`) carries output `content (u, rev(u, C1), EXACT)`. `X1` integrates at `k1`. In `D_{k1}`, `r1` is current, the required evidence passes, and `IMPLEMENT(I1)` and `REVIEW(X1)` are `DISCHARGED`.
3. `I2`'s task produces `X2`, which edits `u` again. Conformance is `CLEAN`, the review `r2` passes and the evidence passes. The Dispatcher submits the integration request.
4. Admission step 8. `IMPLEMENT(I1)` is discharged at the current head and affected by the merged tree, because `r1`'s basis names `u`. After the request, `cur(u) = rev(u, C2) ≠ rev(u, C1)`. Then `sat(content(u, rev(u, C1), EXACT)) = F`, so `current(r1) = F` and `discharged(IMPLEMENT(I1)) = F`. The request is refused (`REGRESSION`). The same holds through `I1`'s `TASK_RESULT`, and through `REVIEW(X1)` while its trigger holds.
5. Every later iteration of `I2` that touches `u` is refused the same way, and so is any item of any plan that touches `u`, for as long as `I1` stays an accepted, issuable item. The only exits are outside the written routes. One is removing `I1` from its plan, an R2 topology amendment needing whole-plan review, whose effect on discharged work no rule states. The other is an absorbed foreign push, which skips step 8 and reopens `I1` "as drift to repair", so `I1`'s implementer is re-dispatched against `I2`'s code.

**Siblings (same cause, checked against the written rules).**

| Sibling | Trigger | Result |
|---|---|---|
| (a) read files | a discharged item's implementer or reviewer read file `g`, recorded as frame-role context `content` (§4.2, §7.3); a later item edits `g` | `I1`'s review or task result goes stale, so step 8 refuses the later item. An independent `EQUIVALENCE` for the reader's consumer class must be admitted first, which is a judgment per read file and per earlier item |
| (b) joint invariants | change `k1` touches a joint invariant's scope; `JOINT_INVARIANT(i, k1)` is reviewed and discharged (§9.2); change `k2` touches the scope again | the review of `k1`'s integrated result goes stale, so step 8 refuses `k2`. A joint invariant's scope is frozen after its first reviewed change |
| (c) specification changes | `SPEC_REVIEW(spec)` fires on "a change to an evidence specification"; a later item with that specification in `evidence_specs` changes it again | under either reading of its key (per change, or per specification), the discharged obligation's review names the earlier specification revision, which the later change makes stale, so the later change is refused |
| (d) D1-D3 authority | a second `AUTHOR` item revises the D2 subject `b` an earlier `AUTHOR` item produced | step 8's exception names "an accepted change to a prerequisite authority" and its dependents' impact, not the earlier item's own obligation on `b`; at integration the new revision's acceptance is prospective. Whether the exception applies is unstated |
| (e) after an absorbed change | a foreign push changes `u` after `X1` integrated | `IMPLEMENT(I1)` is ready again "as drift to repair", while `REVALIDATE(r1)` and the new §4.1 `REVALIDATE` of `I1`'s task result are derived too. Their answers carry `X1`'s output entries, which can never hold again, so both wait on a premise no route restores. That is the §10.3 invariant's "waiting" with no end |
| control | the later change is made by an accepted change to a prerequisite authority | step 8 permits it, as stated. **Holds** |
| control | obligations keyed on the current triple (`ACCEPT`, `GATE`, `REVIEW(s, r)`) | a new revision derives a new obligation, so step 8 is not engaged. **Holds** |

Shared cause: **the obligations whose work an integration enacts are never retired, and their discharge keeps reading exact-content judgments against the moving tree. Step 8, written to stop D4 regressions (workplan: "A D4 change that breaks another closure is a regression and is not admitted"), therefore protects the exact bytes an earlier item produced and read.** Discovery stops here. Further variants (`DOCUMENT` items reading code, partition parts, `INVESTIGATE` reviews) re-derive the same composition.

**Violated owner text.** The workflow owner (`aaeaf8b:source/shared/references/workflow-and-workplans.md`, "Authority lifecycle, mutation, and impact closure"): "acceptance -> bounded dependent impact -> reconcretization/revalidation". Its "Evidence, stages, and impact closure": "identify materially affected descendants … preserve unaffected siblings/still-valid evidence, and close each material impact item". Here a correct later change is refused instead of being impact-closed. The architecture owner (`architecture-and-design.md`, "D3 formal-contract discipline"): "define it before dependent invariants use it: … lifecycle states and transitions". The post-integration lifecycle of an item obligation, and what step 8's "affected … stays discharged" protects, are used by the step 8 invariant but never defined. The D3 entry contract item 6: "state what reopens D3 versus what remains equivalent D4 reconciliation". The Manual's own objective (§0.2: SSDS "coordinates reasoning agents and humans over evolving scientific software") and §11.2 ("tasks on unchanged items continue") presuppose that later items can change earlier items' code. Workplan §21 items 6 and 7 remain unresolved for every obligation whose work has integrated. An implementer must choose. Read literally, the rules refuse all subsequent work on judged content. Read as intended (evidence regression only), step 8 is narrowed without text, and earlier implementers are re-dispatched after every later change by §10.4's non-latched discharge.

**Minimum repair direction (narrows mechanism; a §0.3 refinement, stakeholder-visible).** Options:

1. **Recommended (removes mechanism).** An obligation keyed on an enactment or a change is discharged once, by its own integration or judgment, and later content changes do not reopen it. This covers the item obligations, `REVIEW(X)`, `CONFORMANCE`, `JOINT_INVARIANT(i, k)` and `SPEC_REVIEW` of a change. Later changes reach their consumers only through obligations keyed on current state: `ACCEPT`/`GATE` on the new triple, `REVIEW(s, r)`, evidence currency with `ev`/`qual`, and a new `JOINT_INVARIANT(i, k')`. Step 8 then reads, for each other obligation the merged tree affects, only its evidence terms (a passing `ev` or `qual` that the rerun on the merged tree makes non-passing), which is the workplan's "D4 change that breaks another closure". Absorbed drift shows through subject acceptance and the drift view, not by re-dispatching an implementer. This deletes §10.4's "ready again, as drift to repair" path and the stranded `REVALIDATE`s of sibling (e).
2. Keep non-latched discharge and define step 8's "stays discharged" over evidence terms only. Judgment staleness then reopens earlier obligations without refusal. This leaves re-dispatch churn and sibling (e)'s stranded revalidations. Not recommended.
3. Make the output role a fixed fact after integration for the enactment's own records only, like the before-image. This narrows one cell, but siblings (a), (b) and (d) survive, so it is insufficient alone.

**Required discriminator.** At the real owners (Derivation discharge -> obligation derivation -> Admission step 8):

- two sequential accepted `IMPLEMENT` items editing one leaf unit both integrate, the first item's obligations are not re-dispatched, and its required evidence is rerun on the merged tree;
- a candidate that makes another obligation's required evidence fail is refused (`REGRESSION`) — the negative control;
- two successive changes in a joint invariant's scope each get their own `JOINT_INVARIANT` review and both integrate;
- a change to a file a discharged item's reviewer read integrates without a covering equivalence;
- a later `AUTHOR` revision of D2 subject `b` integrates, with its own revision assessment, acceptance and gate;
- an absorbed foreign change still invalidates acceptance and shows as drift, with no stranded `REVALIDATE`.

§31.4's present case ("collateral regression rejected while accepted upstream change reopens dependents") has no positive case for a later D4 change to the same content, so it would stay green under B1. The diagnostic model has no obligations, discharge or step 8.

## Non-blocking findings

### N1 — "depends on" is now load-bearing and undefined

The `REVALIDATE` trigger (§10.2 line 1260), §4.1's route list and the new §10.3 invariant all read "a non-current judgment that a current obligation depends on". The edabd81 B2 repair rests on this predicate, and it is defined nowhere. Agent authors cannot reassess ("an agent's task has ended"), so a stale agent judgment `x` (an acceptance, a review, a task result) is never superseded once a fresh judgment `x'` replaces it. Under a broad reading (`x` appears in some predicate the obligation reads, such as the `∃` in `ACC(s)`), `REVALIDATE(x)` is derived and dispatched indefinitely after `x'` exists. Under a narrow reading (`x`'s currency is needed: no other member satisfies the term), it ends when `x'` is admitted, and the gate case still works because `gterm`'s minimum needs every eligible member. `REVALIDATE` is also absent from §10.3's list of answered judgment obligations and has no stated end. State the narrow reading, and state that `REVALIDATE(x)` ends when `x` is current again, superseded or no longer needed. This is a definition, not new mechanism.

### N2 — The new task-result `REVALIDATE` route leaves three choices open

§4.1 now says "a stale task result derives `REVALIDATE` of that result for its implementer (§12.3), and `COORDINATE(plan)` where it needs re-planning". Three things are left open:

- The answer is a new `TASK_RESULT` from a new task. A transformation then has several task results, while the review minimum (§4.3) names "the task result". §11.5 step 3 implies that the re-review relies on the new one. State that the minimum names the candidate's current task result.
- State whether the revalidating task may change content. If it does, a new transformation is first submitted by a task bound to `REVALIDATE` rather than to the item obligation, which §5.2's enactment rule and §8.3 step 7's integration binding do not anticipate. The simplest statement is that a revalidation re-attests the same candidate, and any content change is a new iteration.
- "Where it needs re-planning" is not a mechanical predicate (§10.2's `COORDINATE` trigger repeats it).

### N3 — §10.3's "one case waits by design" is one instance of a class

The stated exception covers a plan disagreement whose rejection and vetoed acceptance both lack a holding basis. The same structure arises for any kind whose supersession target's basis can no longer hold. One example is an `ACCEPTANCE` `FAIL`/`PASS` pair on a triple after the subject moves to a new revision: the owner's passing superseder fails step 6 on `content (s, r, EXACT)`. Another is a transformation review whose frame no longer exists. For these, route 4 is the only lift, or the owner's adverse record superseding the vetoed passing judgment, which is exempt from step 6 as never-lost. Also, §5.10 (f)'s trigger reads `vetoed(z)`, which does not test `superseded(z)`. An owner who resolves by superseding the passing judgment therefore leaves `ADJUDICATE_DISAGREEMENT` derived. It is answered and not re-dispatched, but it stays shown. State the class, or key (f) on a passing judgment that asserts. This is disclosure; the veto is not weakened.

### N4 — Lineage-less re-identification: the predecessor computation already exists for D1/D2

Returning acceptance and gate objections to the exact subject triple is sound under S10 and the reviewed R9 ("on that judgment's exact target"). It is consistent with SD-33/SD-34, which keyed only plan and review reach on content. The residual — a remove-and-redeclare without `renamed_from` drops the standing `FAIL` or gate `REJECT` from the next judge's brief — is disclosed (§32.2). For `NATIVE` D1/D2 subjects, §10.2's predecessor already computes "the earlier subjects that owned the bytes `s` covers at its tenure's start". Selecting the history carry of §16.5 by that same computation would close the brief-side gap for D1/D2 acceptances and gates with no new mechanism and no veto. This is a stakeholder option, not a defect.

### N5 — Two small drifts introduced or kept by this round's text

- §4.1 says a `REVALIDATE` "is shown waiting until" its premises hold again or are replaced. By §10.3's dispatch rule, a gate `REVALIDATE(h)` whose required assessment was replaced is ready at once. During the gap, a `QUALIFIED` `ACCEPT` or a `REJECT` holds at step 6, because the gap obligation contributes no required premise. The `UNQUALIFIED` refusal of §16.6 caps the result at `P`, so nothing unsafe follows, but the two statements disagree.
- §31.6 (Z) says the gate's `REVALIDATE` is answered by "a fresh decision on the new core". Only the author's or the owner's decision naming `h` in `supersedes` raises `gterm`, and a fresh peer decision enters the minimum beside `h` (§5.5). Say "a superseding decision by its author or the owner".

### N6 — Editorial

- "Counts" (§10.2 line 1285) is now `base ≠ F`, but the parenthetical lists only acting, supersession, `status1` and `cont`. It omits `tgt`, `vetoed` and `nonind`, which hold trivially for a `TASK_RESULT`. Say "base ≠ F, for example …" or list all of them.
- §5.10 (a) calls `PRODUCT_SCOPE_ACCEPTANCE` "relation-targeted". Its target is an item at a revision (§3.4).
- §5.9's early-cutoff sentence for analyzer changes ("non-current only if the output changed") still sits beside §5.2's `tgt` for machinery `COMPLETENESS` (its analyzer identity must be in the set). An analyzer-set change therefore makes every acceptance bounded by a machinery declaration non-current, whatever the output. `REVALIDATE` now routes this (edabd81 B2(a) closed), but §5.9 and §27.3 should state the re-acceptance burden.

### N7 — The diagnostic's scope is unchanged and cannot see B1

The only model change in the delta is the S10 reach for `ACCEPTANCE` and its mutation, renamed `acceptance_reach_by_content`. The model has no obligations, discharge, answering, `REVALIDATE`, Admission step 7 or step 8, and no integration transition (§5.10 (g), §31.3 say so). A green run therefore coexists with B1 (PEM DS-001). §31.6 (Z) is the right real-owner family for the dependence and liveness repairs, and it now carries edabd81's discriminators except the step-6 refusal of an additional declared `record` entry on a stale revision-assessment record, which is worth adding.

## Closure audit

The closure map was used to navigate. I checked its claims for every §21 item the delta or B1 touches, and against the Manual sections they name. I swept every §10.2 obligation kind for an admissible answer or a derived route, in the admitted state, in a frame, and after integration. Other items were taken as dispositioned in the edabd81 and 653e88c records unless a mechanism below reopens them.

| Item | Disposition at this candidate |
|---|---|
| 4 (basis composition and mode per kind) | closed for the revision-assessment mode (`standing` at §4.1, §4.3, §8.3 step 7, §10.2, §16.6, §29.4 alike) and the gate's required premises |
| 5 (derivation) | closed for the delta (in-run D1/D2 re-acceptance; gate member revalidation) |
| 6 (Admission validation order) | **partly open (B1)**: step 8's "affected … stays discharged" is undefined and, read with §10.4 and §7.3, refuses legitimate later changes |
| 7 (obligation rules, readiness, discharge) | **partly open (B1)**: no lifecycle end for obligations whose work integrated; N1 ("depends on") and N2 (task-result revalidation) are definitional gaps |
| 9 (joint invariants) | inherits B1 sibling (b) |
| 10, 26 (templates) | the delta's brief changes (§16.5 evidence section, lineage carry) are consistent; no open decision |
| 1-3, 8, 11-25, 27 | no unresolved architectural decision found in this bounded audit; unchanged by the delta |

§16.2 rows: unchanged by the delta. §26.4 keeps an explicit replacement, retirement or preserved boundary for every row. None found unresolved.

## Refinements R1-R14

| # | Assessment |
|---|---|
| R1 | Sound as stated; unchanged. Phase B N2 re-tested in text (below) |
| R2, R3 | Sound fail-closed SCC clamp and integrity halt; unchanged |
| R4-R7 | Sound; unchanged and not re-derived beyond the text |
| R8 | Sound; the gate supersession target (gate and triple in any run) is restated consistently in §3.4, §5.10 (b) and §8.3 step 3 |
| R9 | Sound; its "on the same target" wording again matches §5.10 for acceptance and gate (edabd81 N2's understatement removed) |
| R10 | Sound: within-run reuse of the revision-assessment record is now stated identically at derivation and Admission (edabd81 B1 closed) |
| R11 | Sound: every stale eligible member derives `REVALIDATE` for its author or the owner, who alone can supersede it (edabd81 B2 closed); N5's wording point aside |
| R12, R13 | Sound; unchanged |
| R14 | Sound as the selected conservative reach policy; its identity sentence now keys review and plan on content and acceptance and gate on the subject, which agrees with S10 and SD-33/SD-34 |
| (missing) | B1's repair narrows workplan §6.8 step 8 and needs a new row |

The item-31 corrections (step 7's mode, removal of the root clause, "counts" through `base`, the S10 reach, the reconciled stale-review statements) are D3 decisions inside §21 items 4, 5 and 7. They are listed in closure map §5 as author choices. None changes the reviewed contract without a row: removing the root clause restores reviewed K1 ("or it is revalidated").

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **D** design/disclosure closure with real-owner execution owed later; **R** retained, disclosed decision or stakeholder option; **P** partly closed. The delta since edabd81 touches §0.3 R14's text, §4.1, §4.3 (review and gate rows), §5.10 (a) and the `ACCEPTANCE`/`GATE_DECISION` rows of (b), §8.3 step 7, §10.2 (`REVALIDATE`, admission and readiness), §10.3, §11.5, §12.3, §16.5, §31.3, §31.6 and §32.2. I re-derived those mechanisms independently. Earlier records' per-item closures are treated as unchanged unless a mechanism below reopens them; earlier Reviews were not replayed item by item.

**Mechanisms independently checked at this candidate:**

- **Revising duty (653e88c B1, edabd81 B1).** §4.1, §4.3, §5.5, §8.3 step 7, §10.2, §16.6 and §29.4 all read standing, both in the run and while standing. An in-run re-acceptance and re-gate of unchanged `b` after a change of `a` is admissible at step 6 (no `record` entry on the stale record) and at step 7 (`standing` present). Negative controls hold: revocation, block and loss withholding make the record's `base` `F`, and a risk override makes it `P`. **C.**
- **Revalidation and liveness (edabd81 B2 with siblings (a)-(c)).**
  - Gate with one replaced assessment: `REVALIDATE(h)` is derived and ready for `H` or the owner, and a superseding `ACCEPT` with `record A2` raises `gterm` (N5 on wording).
  - Gate with two assessments: ready at once.
  - Acceptance via a superseded, revoked or analyzer-dropped completeness judgment: `REVALIDATE(j)` is ready with the wider closure.
  - Review via a stale check execution: §16.5 marks only current runs, so the re-review relies on none of the stale ones.
  - Gate trigger (c): covered by `REVALIDATE(h)`.
  **C**, with N1 and N2 as definitional gaps.
- **Identity versus content (edabd81 N2, N3).** Acceptance and gate stay on the exact triple, and review and plan reach stay content-keyed. Lineage carry now reaches every named kind's next judge (§16.5), and the lineage-less residual is disclosed (§32.2). **C/R** (N4).
- **Judgment disagreement (§5.10).**
  - One reach rule over S0/S1 `asserts`.
  - The plan closed form over chains, incomparable branches, joins, reverts, loosenings, R2 amendments and multi-item rejections; the current revision is unread.
  - Review reach on changed-unit content under any item or plan.
  - Relief and supersession admissibility; `nonind` in `base`; adjudication root and class at Admission; the acting rule for every permissive route.
  Unchanged except the `ACCEPTANCE`/`GATE_DECISION` rows, which return to the exact-triple rows the d94a293 (different-family) and earlier Reviews examined. 362af9f B1-A's cross-run gate veto is still in the gate row ("in any frame, tenure or run"). **C/R** as in edabd81.
- **Matching (§6.3-§6.6).** Phase B N2 was re-tested in text with an alternate tree differing only outside a recorded narrow basis: a differing old-content run under (2) and a yielding present-content run under (4), under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld. Both stay in through `link⁻` anchored on `real(a⁻)`; only (1)/(3) narrow (§6.6 "Completeness and structure polarity"). **C.** Support cycles (§5.6) and corrupt prefixes (§5.7) still fail closed. **C.**
- **Content identity, gate qualification (`unq`), equal-region partition.** Unchanged. **C.**

| Prior record | Disposition at this candidate |
|---|---|
| EDABD81 (same family) | B1 **C**; B2 **C** (siblings (a)-(c) **C**); N1 **C** (editorial residue N6); N2 **C** (S10 restored) / **R** (N4); N3 **C/R**; N4 **C**; N5 **P** (N3 here); N6 **P/R** (N7 here); N7 **settled: B1 here** |
| 653E88C (same family) | B1 **C** at derivation and Admission; N1 **C**; N2 **C**; N3 **P/R** (model limits, N7); N4 **R**; its "noticed" step-8 item is B1 here |
| D94A293 (different family) | B1 **C**; N1 **C** wording / **R**; N2 **R** (cross-plan amended copy, §32.2); N3 **P** (N7) |
| 913DB8F, 5895687, 4C52205 (SC-1 **R**), both E548472 (same-family SC-1 **R**), D6734C4, 83A82DF, 0D2B35E, 34803DF, BF23372, A6ED164 | plan, review, equivalence and completeness rows unchanged by the delta; blockers **C**; N items **C/R/D** as the edabd81 and d94a293 records give them; plan-policy items **R** |
| 6B986DE, 29DA56E, 51070E5, 9E5A763, 051CCE3, 63DDF91, F03B15E, 61CD09B | independence, adjudication eligibility, supersession targets and relief: **C** |
| 362AF9F, F22B4DC, both B46C250, F7419D5, 575DC78 | acting/enactment, run identity, gate minimum: **C**; the gate-minimum liveness they rely on is restored by removing the root clause (**C**, N5 wording) |
| 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC, 3540D98 | matching, content identity, qualification cap, partition: **C**, with R items unchanged; a18b544's "only a completeness judgment bounds a closure" no longer strands acceptances (`REVALIDATE` restored) |
| 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363, CC005DB, C6DA678, B595F2C, 6FF4ED1 | **C** for each stated blocker (run-keyed counting, event-keyed run, `tgt` read by every consumer, frozen matching, effect-keyed write set); 86ab683's restrictive check and 798b2b4's run closures now **C** with step 7 fixed |
| Phase B closures, N1-N4 | matching-family closures re-verified (above); N1 **R** (§32.2); N2 **C/D**; N3 **R/D** (diagnostic limits); N4 **R** (empirical costs) |

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Upstream D1 change, then in-run re-acceptance and re-gate of unchanged `NATIVE` D2 `b`, through Admission steps 6 and 7 | held |
| The same judgment carrying an additional declared `record` entry on the stale record | held: refused at step 6 (N7: add to §31.6 (Z)) |
| Revision-assessment record revoked, blocked, risk-overridden or loss-withheld | held: `base` falls, so the acceptance is non-current or `P`; `REVIEW(s, r)` is derived when none counts |
| Gate with a required assessment replaced after a rerun; with two assessments, one going stale | held: `REVALIDATE(h)` waits or is ready, and its superseding answer is admissible (N5) |
| Acceptance whose completeness premise is superseded, revoked, vetoed-and-lost or loses its analyzer identity | held: `REVALIDATE(j)` with the wider closure (N6 on §5.9) |
| Review whose check execution goes stale in its frame | held: the re-review relies only on current runs |
| Stale agent judgment replaced by a fresh one by another agent | held under the narrow reading of "depends on"; indefinite `REVALIDATE` under the broad one (N1) |
| Task result stale through an item amendment or governing change, before integration | held as a route; underspecified (N2) |
| Two sequential items editing one file | **B1** |
| Later item editing a file a discharged item's reviewer read; second change in a joint invariant's scope; second `AUTHOR` revision of one D2 subject | **B1** siblings (a), (b), (d) |
| Absorbed foreign change after integration | **B1** sibling (e): drift re-dispatch plus stranded revalidations |
| Re-identified subject with byte-identical content and `renamed_from`: peer `PASS` after a `FAIL` | held as designed: not vetoed (S10), carried as history |
| The same without lineage | disclosed residual (§32.2); N4 option |
| `ACCEPTANCE` disagreement on a triple after the subject moved on | route 4, or the owner's adverse superseder, is the only lift; outside §10.3's stated exception (N3) |
| Gate core showing challenges, reports, other enactments' `REJECT`, stale non-required evidence, stale history of a required obligation | held (SD-35, unchanged) |
| Composition, chain and union reach; review re-identification with a one-byte heading edit; plan closed form | held (unchanged; model green) |
| Completeness lapse under a narrow-basis failure (Phase B N2) | held |

## Minimum architecture and capability transfer

The delta is subtractive: it removes the root clause and the cross-subject content keying, and adds no primitive, component, record kind, mode or persistent surface. `standing` stays the minimum mechanism realizing SD-20's "stands". B1's recommended repair removes mechanism: §10.4's drift reopening and the post-integration currency of enacted obligations. It needs a §0.3 row because it narrows reviewed step 8.

Architecture 1.6.0 (`orchestrator/docs/architecture.md`, blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41` (empty `git diff --stat`), so the version-bound Core and frozen profiles are preserved (PEM PC-001). Capability transfer was not re-derived beyond the delta.

**PEM.** Activated: this is mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` both resolve to `af0455753e20ee54a969c844872e29e270007211`. The PEM blob there and at the candidate is `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no overlay. The repository's validator (`source/project_engineering_memory.py`, run in the clone) reports "PEM schema 1 valid: 5 families, 0 notices". Task-local HAS:

- **PC-001**: APPLICABLE (frozen profiles; preserved).
- **DS-001**: APPLICABLE (a green diagnostic and green §31.4 cases coexist with B1).
- **SP-001**: evidence-only (one owner per rule; B1 is one rule, step 8, whose meaning is computed elsewhere).
- **SP-002, FF-001**: evidence-only, not material.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 separates G1 document checks from G2-G4 runtime evidence and claims no execution it lacks. §31.6 (Z) now carries the dependence and liveness discriminators for edabd81 B1/B2, apart from the additional-`record`-entry refusal (N7). §31.4 tests only that collateral regression is rejected; it has no positive case of a later D4 change to content an earlier discharged item produced or read, so a faithful implementation of B1's literal rule passes it (DS-001). B1's discriminator should join §31.4. The diagnostic shares claim definitions and helpers and models no obligations, answering, discharge, Admission step 7 or step 8, or integration, so green runs say nothing about B1 or N1-N3.

## Doctrine-realization map and O1

§29 maps all seven entrypoints. The revising-duty row (line 2539) now agrees with §8.3 step 7 and §10.2. The D4 row (line 2507: "close each stage with affected regression; reconcile every obligation … no collateral regression (§8.3 step 8)") claims E0 for a mechanism that, under B1, refuses legitimate later stages instead of regressing them. This is the same defect seen from the map; it needs no separate repair. No other map claim depends on the delta.

O1 (§0.5) is unchanged: the realized record, readers, routine questions, retention and marked surfaces are stated, all within the requested deliverable and none beyond it. The §16.5 evidence section and the lineage history carry are within-deliverable surfaces. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

Executed against the extracted candidate:

- Blob identities above (`git rev-parse` at the candidate); the model file's blob `8426e67af2381bff85cbb39f8423dd3250ced59b`, re-checked equal to the snapshot with `git hash-object`.
- `git diff --check edabd813838ee7703f6eb6d29496e5704517eba0 82d618cd26900f8cb7b0aaa6be7cac3d3a7c030c`: exit 0. The delta is 6 files: the Manual (34 lines changed), the closure map (8), the model (22), the continuation handoff, and the previous handoff and Review record added.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the snapshot: 4 tests OK (routing and lifecycle structure only).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 bf2337285dfdaba5d535e73cf76af3d5b78978f0`: 73 files, 23,269 insertions, 1 deletion (that historical comparison only).
- `git diff --stat fad3ee41… 82d618cd… -- orchestrator/docs/architecture.md source dist`: empty.
- PEM validation as above.
- Diagnostic model at the candidate: the `--mutations` workload, run in parallel by importing the unmodified module with `python3 -I` from a scratch driver under `$TMPDIR/ssds80-manual-review-82d618c/scripts/` (a 30-worker `multiprocessing` pool, forked workers, with `MUT` cleared and set at the start of every job). The driver ran `run_family` for each of the five families (`CORE`, the three in `FAMILIES`, `GATE_BASIS`) with `MUT` empty. Then, for each of the 34 entries of `MUTATIONS`, it set `MUT = {m}` and ran `run_family` on each family that mutation names. That is 41 jobs, built from the module's own lists. The only memo state is per-`Ledger` instance, so no state crosses jobs.
  - Base results, all with zero invariant failures: transformation-review/acceptance/gate 1,856,368 scenarios; equivalence-chain 299,760; completeness-cover 37,600; plan-coverage 205,800; gate-basis 1,000.
  - All 34 mutations are caught. The renamed `acceptance_reach_by_content` is caught by I1/I3. `plan_supersession_current_only` is caught by I4 only.
  - I did not call `main()` itself; the driver calls the same functions in the same configuration.
- Governing owners read at `aaeaf8b`:
  - `source/roles/software-design/SKILL.md` (routing, D3 design contract, Independent Review and Challenge);
  - `architecture-and-design.md` ("D3 formal-contract discipline");
  - `workflow-and-workplans.md` ("Authority lifecycle, mutation, and impact closure"; "Evidence, stages, and impact closure");
  - `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review readiness and independent review sufficiency", "Review strategy after recurrence", "Finding routing and revision economy");
  - `testing-and-validation.md` (proxy-proof, through PEM DS-001);
  - `project-engineering-memory.md` (activation, HAS), applied through the validator and the HAS above.
- Reviewed-workplan text read at the candidate: §6.8 steps 6-8, the §6.9 role table, §7.4 discharge, §21 items 1-27.
- Manual sections read in full: §0, §3, §4, §5, §6.6, §7, §8, §10, §11, §12, §13, §14, §16.1-§16.8, §31.3, §31.6, §32.2. The rest was read by targeted search for the drift classes and for B1's mechanism.

Not verified:

- No production SSDS, real gate or runtime was exercised.
- The doctrine map was checked only for rows touching the delta and B1.
- Earlier Reviews' per-item closures were not replayed (stated above).
- Whether `SPEC_REVIEW` is keyed per change or per specification, and whether `REVIEW(X)`'s trigger still holds after later changes make `X`'s frame merge conflict, are not stated in the Manual. Sibling (c) holds under both readings; the `REVIEW(X1)` path is conditional, and the decisive trajectory does not depend on it.
- The six drift classes were applied by targeted search over the concepts named in REVIEW METHOD, not by a pairwise comparison of every concept in the Manual. Further drift outside them is possible.

## Scientific checks

Method: one pinned architecture candidate; deductive counterexamples bound to exact owner text; a family-level recheck; structural tests; and the candidate's diagnostic with its prescribed mutations. Material findings: B1 and N1-N7. None concerns a scientific observable, numerical method or realized scientific result.

**I produced, ran or reviewed no realized scientific results.**

Variants evaluated: one normative candidate. For B1, one decisive trajectory, five siblings and two controls, against two readings of step 8 (literal; evidence-only), each found inadequate as written. For the edabd81 repairs, the eight trajectories of that record. Seventeen out-of-matrix trajectory classes (overlapping, not independent trials). One diagnostic configuration with 5 base families and 34 mutations. The criterion was to find a material counterexample, not to select a favourable result.

No accepted project D1/D2 scientific authority was relied on for a consequential judgment, so no tension search was triggered. Gaps: real-owner execution, reader adequacy and operating costs.

## Common-mode note

The reviewer is of the **Claude family**, the same family as the Manual's author and as most earlier Manual reviewers. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. This reviewer was engaged as a fresh-context sub-agent launched by the authoring session. It did not receive the authoring conversation, but fresh context is not epistemic independence. It shares the corpus, the inherited workplan and handoff framing (including the handoff's drift-class diagnosis and its request to settle edabd81 N7, which directed part of the search), the prior Review records (read as hypotheses), the Git/Python toolchain and the diagnostic's claim definitions and helpers.

B1 was found by asking, for every §10.2 obligation kind, whether its target is re-keyed when content moves and what step 8 then protects. It lies in reviewed-workplan text that forty-five Manual Reviews and the Phase B Review did not establish as a defect, so the shared framing is a plausible reason it survived. A different-family check of B1 and of whichever repair is chosen is advisable.

## D4 statement

This Review authorizes **no D4**, cutover, architecture acceptance, product-scope extension or proposed default. The next steps are:

1. Choose and state B1's repair (option 1 recommended) as a §0.3 refinement; reconcile §7.3, §8.3 step 8, §10.2, §10.4, §13.7 and §29.3's D4 row; add B1's discriminator to §31.4.
2. Consider N1-N7. N1 and N2 are definitions the B1 repair will touch anyway.
3. Freeze a replacement candidate and obtain an independent Review, preferably including a different-family check of B1's repair, before stakeholder G1 acceptance.

G2 still separately requires a reviewed shadow workplan and explicit stakeholder authorization.
