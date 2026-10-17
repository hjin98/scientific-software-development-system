# Independent D3 Review — SSDS 8 Architecture Manual, candidate eb86a71 (SD-39 confirmation)

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          eb86a71159688c9ba640c06cc16dffa5f5cf505b
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g)), with the
                        SD-39 confirmation questions first; technical evidence for G1 only
    MANUAL blob:        3c27c265824c3286fec7233b4f23793a3a4feeaa (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   482fb794a2944338464455c1239cc4368a1d733e (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family 093164f
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; 093164f..eb86a71 read sentence by
                        sentence (13 changed line groups of the Manual: lines 100, 549, 570, 1190, 1256,
                        1261, 1319-1333, 1381, 1548, 1550, 1678-1679, 2675, 2681); a route sweep of every
                        state of an item obligation (pending first candidate, integrated, pending
                        re-dispatched candidate, fenced, amended, partitioned, re-attested) against every
                        section that states a route for it (§4.1, §4.3, §8.3 steps 6-8, §10.2-§10.4,
                        §11.2, §11.5, §13.7, §15.2-§15.5, §22.2-§22.3, §31.4, §32.3); the diagnostic model
                        run in full (six families, all 48 mutations, in parallel by importing the
                        module) and probed on chosen trajectories; structural checks of handoff §3 step 9;
                        family-level recheck of earlier families on the unchanged text
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched by
                        the session that issued this handoff (the authoring session); did not author the
                        candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-eb86a71/snap`. The later commit adding the handoff (`8b489ed9`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. SD-39 (stakeholder record item 35: "Apply the 093164f Review's option 1 (one route statement per item-obligation state owned by §10.4, with its (a)-(f) fixes) and option 3 first (routing model derives routes from every section's triggers). Then a confirmation review.") is realizable and consistent with SD-36 to SD-38 and with reviewed workplan §7.3, §7.4 and §7.10. The blocker below lies in the realization: the list's domain is narrower than the states the item obligation can be in. It can be repaired without reversing any stakeholder decision.

## Verdict

**NO-PASS.** One blocker, in the obligation-routing family (the obligation lifecycle after integration; its twelfth round counting from 095ce55). Earliest owner: Manual §10.4 (the route list, line 1319-1331), deciding workplan §21 items 7, 24 and 26.

What SD-39 asked for is realized for every state the 093164f Review named except two:

- §10.4 now holds one ordered list (lines 1323-1331), and §4.1, §8.3 step 8, the `REVALIDATE` row, §11.5 and §13.7 point to it;
- the `REFUSED` decision trigger is limited to `JOINT_INVARIANT`, `SPEC_REVIEW` and high-consequence reviews (lines 1256, 1333), so an in-scope pre-integration NO-PASS has one route (093164f B1 (a) closed for transformation reviews and conformance);
- the joint-invariant and high-consequence reviews carry `identity` on the task result (line 570; B1 (b) closed);
- "integrated" is defined, findings-only investigations included, and a first-iteration pending candidate keeps the ordinary routes (line 1319, 1321; B1 (c) closed for those two cases);
- a fence awaiting its decision and a spent budget precede drift (routes 1 and 3; B1 (d) awaiting half and (e) closed);
- the NO-PASS iteration is keyed on the state "standing adverse review" (line 1319; B1 (f) closed);
- §15.5 gains a no-report row (line 1678; 093164f N1 closed), `BLOCKED` re-attestation is a blocker report (N2 closed), and route 6 names the owner's adjudication (N4 closed).

The routing family is green and catches all fourteen of its mutations. It does not represent any of the five siblings below, and it cannot: its dispatch event integrates at once, it has no item amendment, no conformance class, no partition, and no answered principal decision for the item.

## Blockers

### B1 — §10.4's route list is total only over the outcomes of the latest integrated enactment's review and task result; five other parts of an item obligation's state still get their routes from other sections, or get a list route no obligation can carry

**Family:** obligation routing (SD-36 to SD-39; the lifecycle family 095ce55 through 093164f). Non-local recurrence. Siblings (b) and (e) are the two 093164f B1 cases whose realization covers only part of the case that Review named; (a), (c) and (d) are conditions the list does not read at all.

**Shared cause** (the drift class "two places computing one thing", now in the form "a pointer whose target is silent"): the list (lines 1323-1331) reads the fence state, the predicate, the budget, `out(o)`, and the review and task result of "its latest integrated enactment" (line 1319). An item obligation's state also includes its item's revision, any pending candidate it has after its first integration, the answer to a decision a route owes, the conformance class of the result the review relies on, and judgments about it that are not on its own latest transformation. For those conditions §10.4 is silent. The sections that read them (§4.1, §10.2, §10.3, §11.5, §13.7, §15.5) say they point to §10.4, but their own clauses still derive routes, so the rule "the first of these that applies is `o`'s only route" (line 1321) is either false or leaves the obligation with no route.

**Earliest owner:** Manual §10.4 (the list and its domain), with the clauses in §4.1 (line 549), §10.2 (`COORDINATE(plan)` and `REVALIDATE` rows, lines 1256, 1261), §10.3 (line 1293), §11.5 (line 1381), §13.7 (lines 1548, 1550) and §15.5 (line 1678) that it must absorb or delete. These decide workplan §21 items 7 ("obligation rules ..., readiness, three-valued discharge, ... iteration/attempt identity"), 24 ("task-partition checks, budgets") and 26 ("the outcome table for coordination decisions"). Reviewed parents: workplan §7.2, §7.3, §7.4, §7.8, §7.9, §7.10. **Status:** open, material.

**(a) An R2 amendment of an integrated item: §4.1 gives `COORDINATE(plan)` "instead" of the list's route 7.**

Exact rules at the candidate:

- §4.1, line 549: "a stale task result derives `REVALIDATE` of that result for its implementer or investigator (§12.3), which re-attests the same candidate ..., where §10.4's routes give it, and `COORDINATE(plan)` instead where the result is stale through an R2 amendment of its item revision or contract, which only re-planning changes (§10.2); one stale only through an R1 tightening is revalidated, with the new checks run".
- §10.2, line 1256 lists "a task result stale through an R2 amendment of its item revision or contract (§4.1)" as a `COORDINATE(plan)` trigger separate from "a route §10.4 gives an item obligation". §10.3, line 1293: "`REVALIDATE` (or, for a stale task result, `COORDINATE(plan)`)". §15.5, line 1678 lists it as a decision with no report.
- §10.4, route 7 (line 1329): "the latest task result is not current: its `REVALIDATE`, answered by the implementer's or investigator's re-attestation". No exception.
- §4.3, line 576: a `TASK_RESULT` carries "`content` on the item revision (`EXACT`)".

Trajectory:

1. `IMPLEMENT(I)` at item revision `ir1` integrates `X1`. Its review `rX1` passes and `I` is discharged.
2. The principal R2-amends `I` to `ir2` (a changed obligation statement, §11.4) and an independent plan acceptance covers `ir2`, so `I` is issuable again (§11.2).
3. `t1`'s `EXACT` entry on `ir1` fails, so `t1` is non-current, and so is `rX1` through its `record` entry. `out(I)` has not moved; there is no fence, no adverse review, and budget is left.
4. By the list, route 7 applies: `REVALIDATE(t1)`, a re-attestation against `ir2` (a `PARTIAL` answer then iterates under route 5). By §4.1, `COORDINATE(plan)` applies "instead".
5. Read as two routes, both are live. Read as §4.1 says, the decision is answered by "the first admitted `COORDINATION_DECISION` naming it" (line 1678). `t1` is still stale, the trigger is the same obligation and already answered, and §4.1 excludes route 7. `I` is then `OPEN` with neither a ready nor a waiting route, which is the defect §10.3 (line 1293) names. "which only re-planning changes" is false here: the re-planning has already happened in step 2.

What `o` is across its item's revisions is also unstated. Part obligations are "identified by the item revision" (line 1548), while §8.3 step 7 (line 1189: a task result "bound to ... a non-current contract revision is recorded with that classification and routed to revalidation") and §4.1 presuppose that the obligation persists across revisions. Under the revision-keyed reading, `I(ir2)` has no integrated enactment and is dispatched afresh, and neither route 7 nor §4.1's R1 clause applies after integration. The routes differ by reading.

**(b) A pending re-dispatched candidate of an integrated obligation is outside both route sets (093164f B1 (c), partly closed).**

- §10.4, line 1319: "An obligation is **integrated** once some enactment of it has integrated"; "After integration `o` relies only on its latest integrated enactment's review and task result". Line 1321: "Before integration, `o` has the ordinary routes: ... a clean rebase that makes the candidate's task result or review non-current derives its `REVALIDATE`".
- §11.5, line 1381: "a clean rebase has its conformance re-derived, and review is re-requested only where the review's basis no longer holds, by the routes §10.4 gives an obligation before its integration".
- `REVALIDATE` row, line 1261: "for an item obligation's review or task result, only where §10.4's routes give it".
- `REVIEW(X)` row, line 1258: derived "while `X` is unintegrated".

Trajectory:

1. `I` integrates `X1` with `out(I) = {u, v}`. An absorbed foreign change moves `u`. Route 4 re-dispatches `I` as drift: task `t2` submits `X2`, conformance is `CLEAN`, and `REVIEW(X2)` is answered by a passing `rX2` that read `g`.
2. Before `X2`'s integration request is admitted, an unrelated admission changes only `g`. The rebase is clean, and `rX2` is non-current through its context entry.
3. `I` is integrated, so the "before integration" routes that §11.5 points to do not apply to it. Routes 7 and 8 read only `X1`'s review and task result. No `REVALIDATE(rX2)` is derived.
4. `out(I)` is still moved (`X2` is not integrated), so route 4 applies again. A new drift task `t3` is dispatched, a new enactment that spends budget. `X2` can never integrate, because integration needs current review judgments (line 1381). SD-37 ("otherwise it waits on `REVALIDATE` of its review") is not realized for `X2`, whose own outputs never moved. Under steady unrelated traffic, every drift candidate is discarded until the budget is spent.
5. `X2`'s other answers have the same gap. An out-of-scope NO-PASS of `X2` gets `COORDINATE(plan)` from §13.7 ("a NO-PASS finding outside the item ... create a `COORDINATE` decision") and from §10.2, while the list gives route 4 (route 5 reads only the latest integrated enactment). That is two routes, or a finding outside the item never reaching the principal, against workplan §7.10. A `DISCREPANCY` in `t2` likewise gets §13.7's decision beside route 4.

093164f B1 (c) named this case ("or a drift candidate while `X1` is the latest integration"). The realization keys "before integration" on the obligation, not on the candidate, so only the first-iteration candidate is covered. The model's `dispatch` event integrates the new enactment immediately (`rt_derive`: `st.integrated = True`), so a pending re-dispatched candidate is not represented.

**(c) A kept fence: the principal's decision has no outcome that re-applies, and route 1 still holds after it is answered.**

- Route 1, line 1323: "a fence the human kept: `COORDINATE(plan)` (re-apply, amend or withdraw the item)".
- §15.5, line 1678: such a decision "allows `AMEND`, `DECLINE` with a reason ..., `CHALLENGE`, `ESCALATE` and, for an item, `PARTITION`", and "is answered by the first admitted `COORDINATION_DECISION` naming it".
- §22.3, line 2138: "the human chooses to re-apply `n` ... or keep the fence".

Trajectory:

1. `I`'s integration `n` is fenced. After settlement the human keeps the fence. Route 1 derives `COORDINATE(plan)`.
2. No §15.5 outcome re-applies `I`, and no rule says what any outcome does to `I`'s route. The kept fence on `I`'s latest integration is a permanent ledger fact. Only a new integration of `I` changes that integration, and that needs a dispatch, which route 1 excludes because it precedes routes 3 and 4.
3. After any answer other than an `AMEND` that removes the item, `I` is `OPEN` forever and its only route is an answered decision. An `AMEND` that keeps the item changes nothing under the reading where `o` persists across revisions. Re-application is reachable only through a contrived single-part `PARTITION`, or, under the revision-keyed reading of (a), through any amendment at all.
4. 093164f B1 (a) step 6 named this gap ("neither an `AMEND` nor a 're-apply' outcome"). The repair added `AMEND` only. Probing the model: the sequence (`fence`, `keep_fence`, `decide`) ends with the item `('OPEN', {'COORDINATE:fence'})`, because `decide` acts only on the joint-invariant obligation. The model does not represent the decision as answered.

**(d) A re-attestation's conformance after integration is read by no route, so the item can discharge on a result that fails its `HARD` checks.**

- §8.3 step 7, line 1189: the result-only `HARD` templates (`slots_filled`, `outcome_consistent`, `citations_support`) are evaluated at admission; "when any yields `INCOMPLETE` or `DISCREPANCY`, every passing judgment and every principal decision record in the request is refused ..., while the `TASK_RESULT` ... [is] admitted and the iteration counts". The same step requires, at integration, that "the derived conformance of the exact candidate has no `VIOLATION`, `INCOMPLETE` or `DISCREPANCY`".
- §4.3, line 570: a review's `record` entry is "on the candidate's current task result (after a revalidation, the newest one for the same candidate ...)".
- §10.4, line 1319: a standing adverse review includes "a re-attestation of the latest task result that is `PARTIAL` or `INFEASIBLE`". Conformance classes are not mentioned.
- §13.7, line 1550: "Within budget, an `INCOMPLETE` result ... starts the next iteration mechanically (R0) ... every `DISCREPANCY` create[s] a `COORDINATE` decision". §10.2's `COORDINATE(plan)` row: "a `DISCREPANCY`".

Trajectory:

1. `I` is integrated and discharged. A later admission changes a file `I`'s implementer read, so `t1` is non-current, and route 7 derives `REVALIDATE(t1)`.
2. The implementer re-attests with outcome `COMPLETE` and an empty required slot (`slots_filled` yields `INCOMPLETE`), or with an outcome its citations do not support (`DISCREPANCY`). The re-attestation `t1'` is admitted, and its entries hold, so it is current.
3. `rX1`'s `record` entry now targets `t1'`, the newest result, and holds, so `rX1` is current. The discharge predicate reads no conformance. Route 2 applies: `I` is `DISCHARGED`.
4. §13.7 meanwhile iterates the `INCOMPLETE` result and derives a decision for the `DISCREPANCY`.

Either the item is discharged and also iterated or owed a decision (two statements), or it is discharged on a relied-on result that fails the checks Admission required at integration. This is the permissive direction: workplan §7.4 says "A missing required check is an undischarged obligation; no rule can turn it into PASS". 093164f N2 split `BLOCKED` from the other outcomes, but the conformance classes were never placed in the list.

**(e) An adverse item-level review: route 5 iterates parts that their own lists hold discharged (093164f B1 (a) step 5, partly closed).**

- §13.7, line 1548: "The item is discharged when every part is and an item-level review of the integrated result has passed ...; an adverse item-level review iterates the parts whose outputs its findings name (§10.4); the item-level review is derived over the parts' latest integrations". Each part has its own implementer obligation and enactment.
- Route 5, line 1327: "for an adverse item-level review, an iteration of the parts whose outputs its findings name".
- Line 1319 defines a standing adverse review as "an adverse `REVIEW` judgment on the latest enactment's transformation that stands". Route 2 ("the predicate holds: none, `o` is discharged") precedes route 5.

Trajectory:

1. Item `I` is partitioned into parts `a` and `b`. Both integrate, and each is discharged on its own review.
2. The item-level review is adverse, with findings naming `a`'s outputs.
3. For part `a`, the item-level review is not a judgment on `a`'s latest transformation: its target is the parts' integrated result. So it is not `a`'s standing adverse review. `a`'s own review is current, so route 2 holds and `a` has no route.
4. The item obligation's own obligations are partitioned (line 1548), so it has no enactment, and "its latest enactment" is undefined for it.
5. The iteration that route 5 and §13.7 prescribe has no `OPEN` carrier. `I` stays undischarged with no ready or waiting route, and the finding produces no work. No route is stated for findings that name no part's outputs (a joint property of the parts' interaction): the "otherwise `COORDINATE(plan)`" clause covers only findings outside the item's write scope.

SD-39's "an adverse item-level review iterates the parts its findings name" is realized in words only.

**Violated owner text.**

- **The architecture owner** (`aaeaf8b:source/shared/references/architecture-and-design.md`, line 96): "When an architectural concept carries normative meaning, define it before dependent invariants use it: component/state ownership, ..., lifecycle states and transitions". Line 66: "Prefer cohesive ownership, direct control flow, one authoritative representation/state".
- **The D3 entry contract** (`aaeaf8b:source/roles/software-design/SKILL.md`), item 4: "prefer cohesive ownership, direct flow, one authoritative representation/state".
- **The workflow owner** (`aaeaf8b:source/shared/references/workflow-and-workplans.md`, line 96): "close each material impact item as resolved, preserved-with-reason, or unavailable/blocking". (a), (c) and (e) leave items in none of these states.
- **The reviewed workplan.** §7.10: "a NO-PASS whose findings all lie within the item's write scope and obligations, starts the next implementer iteration mechanically (R0)", and "Budget exhaustion, a NO-PASS finding outside the item, and every `DISCREPANCY` create a `COORDINATE` decision"; (b) and (d) break these. §7.4: "A missing required check is an undischarged obligation; no rule can turn it into PASS"; (d) breaks this. §7.8: "review is re-requested only where the review's basis no longer holds"; (b) breaks this.
- **The Manual's own claims and SD-37/SD-39.** Line 1319: "This paragraph is the one owner of an item obligation's route; every other section points here". Line 1321: "the first of these that applies is `o`'s only route". Line 1293 calls an obligation with "neither a ready nor a waiting route" a defect. SD-37: re-dispatch "only when ... moved the output content of one of its integrated enactments; otherwise it waits on `REVALIDATE` of its review".
- **The handoff's confirmation questions:** "that no section still derives an item-obligation route outside §10.4's list, that the list's order gives exactly one route in every state, and that every owed decision has an admissible outcome".

**Minimum repair direction.** This is a recurrence: the options are for the stakeholder, recommended first. Every option holds SD-36 to SD-39 fixed unless it says otherwise.

1. **Recommended, mostly subtractive: make the list total over the obligation's state rather than over the latest enactment's outcomes, deleting the clauses it absorbs.**
   - **(a):** delete §4.1's R2 "instead" clause and its echoes in §10.2, §10.3 and §15.5 for integrated obligations. Route 7's re-attestation against the amended revision already answers the case, and `PARTIAL` or `INFEASIBLE` then iterates under route 5. If the R2 route is kept for pending candidates, state it in the "before integration" sentence. State once whether an item obligation's identity persists across its item's revisions.
   - **(b):** key "before integration" on the candidate rather than the obligation: while `o` has a pending candidate (result admitted, neither integrated nor refused), that candidate's ordinary routes are `o`'s route, ahead of route 4. Equivalently, scope route 4 to "no pending candidate of `o`".
   - **(c):** end route 1's "kept" clause once its decision is answered. Routes 3 and 4 then apply: re-application is drift, and withdrawal is an `AMEND`. Drop "re-apply" as a principal outcome.
   - **(d):** in the list, treat a re-attestation whose result-only `HARD` templates yield `INCOMPLETE` as a standing adverse review and one yielding `DISCREPANCY` as `COORDINATE(plan)`. Alternatively, state that the review's `record` entry does not follow to a non-conforming re-attestation, so route 7 continues.
   - **(e):** make an adverse item-level review a standing adverse review of each part whose outputs its findings name, so those parts' predicates fail and route 5 is theirs. Route findings that name no part to `COORDINATE(plan)`.
2. **Stakeholder alternative (removes mechanism; reverses SD-37/SD-38's post-integration waiting routes; the 093164f option 2):** after `o`'s first integration, derive no `REVALIDATE` for its review or task result. Every reopened integrated item is re-dispatched within budget, otherwise `COORDINATE(plan)`. This removes routes 6-8, (d), most of (a) and the rebase half of (b). (c) and (e) still need their sentences. It accepts the read-only churn SD-37 removed.
3. **Process option (do first under either):** extend the routing model with
   - item amendments (R1 and R2);
   - a re-dispatched candidate that stays pending, so that `dispatch` does not integrate at once;
   - conformance classes on re-attestations;
   - an answered principal decision for the item;
   - a two-part partition with an item-level review.

   Also write each section's trigger from that section's own text. Today `t_10_4_drift`, `t_13_7_iterate_and_budget` and `t_10_2_revalidate` each open with §10.4's precedence guards (fence, `review_current()`, budget), so I14 is green by construction for precedence and cannot detect a second route that a section's own clause derives.

   Given twelve rounds in this family, the convergence owner's "Review strategy after recurrence" also supports the stakeholder weighing option 2, or a bounded stop with the residual disclosed, against another round of option 1.

**Required discriminator.** Real owners: Derivation (obligation derivation, readiness, discharge), Admission step 7, the Dispatcher's budget check.

- An integrated item R2-amended and re-accepted has exactly one route, and that route leads to discharge or to an iteration, never to an answered decision with the item `OPEN`.
- A pending re-dispatched candidate whose review's context entry fails after a clean rebase derives that review's `REVALIDATE` and no new drift dispatch. An out-of-scope NO-PASS of such a candidate has exactly one route, `COORDINATE(plan)`.
- After a kept fence and any `COORDINATION_DECISION` other than removing the item, the item has a ready route.
- After integration, a re-attestation with outcome `COMPLETE` whose `slots_filled` yields `INCOMPLETE` does not discharge the item, and the item has exactly one route. The same holds for `DISCREPANCY`.
- A partitioned item with both parts discharged and an adverse item-level review naming part `a`'s outputs: `a` is `OPEN`, with route 5 as its one route. Findings naming no part give `COORDINATE(plan)`.
- The routing model with these events and guard-free section triggers fails on this candidate's text and passes on the repair.

## Non-blocking findings

### N1 — Duplicate `COORDINATE(plan)` triggers

Line 1256 lists "budget exhaustion" and "an out-of-scope NO-PASS finding". It also lists "a route §10.4 gives an item obligation of its items (a kept fence, a spent budget, an out-of-scope NO-PASS)". One condition then has two trigger descriptions. If the rule id enters the obligation identity (line 1247), that is two obligations, each answered only by a decision naming it. List each condition once.

### N2 — `DECLINE` of an item route leaves the item `OPEN` with an answered decision

A `DECLINE` (or `ESCALATE` then nothing) of a spent-budget or out-of-scope decision leaves the item `OPEN` with no further route or display. Nothing then shows it to anyone. State what the item's resulting state is (preserved-with-reason in the inspector, per the workflow owner), or make `DECLINE` of an item route withdraw it. This is related to B1 (c), but here the principal chose the outcome.

### N3 — The routing family still shares §10.4's order (DS-001; 093164f N3, partly closed)

What improved:

- routes are now collected from eight trigger functions named for their sections;
- the review's and task result's entries are explicit;
- fences, budgets, peer and owner adverse reviews and a pending first candidate are modelled;
- all fourteen routing mutations are caught (run below).

What remains:

- each section function embeds §10.4's precedence (see B1, option 3), so I14 tests a transcription of the list;
- I15 still reads the model's own `moved()`;
- the property set lacks "every owed decision, once answered, leaves a ready route or a closed state", which B1 (c) and N2 need;
- the docstring's "I13-I16, I18" still skips I17.

The model omits everything in B1 (a)-(e). §31.3 (line 2675) discloses "no principal decision's effect" but not the rest.

### N4 — The owner's adjudication beside drift

When route 4 applies while a peer's veto of the latest review awaits the owner, the `ADJUDICATE_DISAGREEMENT` obligation (line 1266 trigger) stays derived on a review that becomes history once the drift integrates. It is answerable through §10.3's "waits by design" class (line 1293), so nothing strands. It is, however, a second ready task for one item state, outside the list. State that it is the disagreement's own obligation, not an item route.

### N5 — Joint-invariant review churn outside its scope

The joint-invariant review's output entries are now scoped to `scope(i)` (line 570). Its "ctx `content` on the governing closure" and "`validity` on `gov` of each changed unit across subjects" are not scoped, so a change to a governing unit of a changed unit outside the scope makes it non-current. Its `REVALIDATE` is answerable, so nothing strands, but there is review churn outside the invariant. Scope those entries the same way, or disclose the churn.

### N6 — Editorial

§31.3, line 2675 still introduces the sixth family as "(§10.4, SD-36, SD-37)". It should cite SD-38 and SD-39 (093164f N5, open).

## Closure audit

The closure map was used to navigate. Its claims were checked for every §21 item that the delta or B1 touches.

| Item | Disposition at this candidate |
|---|---|
| 6 (Admission order) | closed; step 8 (line 1190) is unchanged in substance and points to §10.4 |
| 7 (obligation rules, readiness, discharge, iteration identity) | **partly open (B1 (a)-(e))**; item-obligation identity across item revisions is unstated (B1 (a)) |
| 9 (joint invariants) | closed (line 570 `identity` entry; line 1226); N5 is churn, not closure |
| 24 (partition, budgets) | **partly open (B1 (e), and B1 (b) for budget spend)** |
| 26 (coordination outcome table) | **partly open (B1 (c))**; the no-report row (line 1678) closes 093164f N1 otherwise |
| 1-5, 8, 10-23, 25, 27 | no unresolved architectural decision found in this bounded audit; text byte-identical to 093164f outside the 13 changed line groups |

The §16.2 rows (§26.4) are unchanged. Each keeps an explicit replacement, retirement or preserved boundary, and none was found unresolved.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1-R14 | text byte-identical to 093164f's §0.3 (only line 100, the R15 row, changed); sound as assessed in the earlier records; spot-checked R9 (an answered obligation is never ready again, which the `REFUSED` ends respect) and R12 (a re-dispatch is a new task and enactment), both consistent with §10.4 |
| R15 | sound as the stakeholder-chosen narrowing of reviewed step 8 to evidence regression (SD-36). The row's summary ("one route statement in §10.4 (SD-39)") is not yet true, by B1. No further unlisted change to workplan §7.10 was found: the 093164f B1 (a) change is removed |

## Re-verification of earlier findings (family level)

**Obligation-routing family:**

- **093164f B1:**
  - (a): closed for `REVIEW(X)`, conformance and the peer-veto case. Partly open for the item-level review (B1 (e)).
  - (b): closed.
  - (c): closed for first-iteration candidates and findings-only investigations. Open for re-dispatched candidates (B1 (b)).
  - (d): the awaiting half is closed; the kept half is open (B1 (c)).
  - (e), (f): closed.
- **093164f non-blocking findings:** N1 and N2 closed; N3 partly closed (N3 above); N4 closed; N5 partly open (N6 above).
- **8f4e75d B1 (a)-(f):** closed by latest-only reliance, the review of a re-dispatched enactment covering `out(o)`, route 5, route 4, the defined findings-only integration and the scoped joint-invariant minimum. The (e) pending variant is open as B1 (b). N1-N6 remain answered, as 093164f recorded.
- **f185036 B1 (a)-(c):** closed. The current-state end for event-keyed obligations, with `REFUSED` kept, is at lines 1256-1271 and 1333. The list orders drift before revalidation. `subject(o)` is the union (line 1319).

**Obligation-lifecycle family (095ce55, c77447b, 3940dbc, 3876473, 494c810, c4e8de7):**

- Closed by SD-36's removal of the mechanism. A search for latch, lowered-state, retirement and `RESOLVED_BY` residue finds only the §6 assessment-family latches (lines 656, 1086-1087), which predate R15.
- 82d618c B1 is closed by the step-8 narrowing (line 1190). Its cases are tested in §31.4 (line 2681): a later item editing an earlier item's outputs, a second change in a joint invariant's scope, and a second `AUTHOR` revision.
- The non-blocking findings of those Reviews are moot with the mechanism, or carried as the 093164f record states.

**Judgment-disagreement family (§3.4, §5.3, §5.5, §5.10, §6.7, §8.3 step 3, §10.2-§10.4 rows), via closure map §7:**

- Text is byte-identical to 093164f except the routing rows.
- The four judgment families and the gate-basis family are green, and their mutations are caught (run below).
- The family-level closures recorded from 3540d98 through 653e88c (the plan row's closed form, content keying of review and gate vetoes, `identity` versus `record` versus `standing` modes, the gate basis's required premises, revision-assessment standing) were not found reopened by the delta.
- The plan row and §16.5 carries were re-read: unchanged, and the stakeholder-chosen claim (SD-30 to SD-34) is not challenged here.

**Assessment-disagreement family (§6), Phase B closures and N1-N4 carry-forward:**

- §6 is unchanged since 093164f and earlier candidates.
- Phase B N2 (completeness polarity), support cycles, corrupt prefixes and the matching clause were not re-derived trajectory by trajectory in this round. The delta does not touch them. This is stated as a bounded gap below.

**Every other listed Review, 6ff4ed1 through edabd81:** their findings concern text that this delta does not change. Their dispositions are as the intervening records state; this Review did not re-derive each one independently. This is a gap, not a closure claim.

## Out-of-matrix trajectories attempted

Held:

- a revert after an output move (route 2 again);
- an empty drift transformation (`out(o)` reset, route 2);
- a plain overtake (route 4 only);
- a fence awaiting with a spent budget (route 1 only);
- a spent budget with moved outputs (route 3 only);
- a pre-integration in-scope NO-PASS (§13.7 iteration only; no `COORDINATE(plan)`);
- a peer's veto, then the owner upholding it (route 6, then route 5);
- the owner dismissing the veto (supersession, then route 2);
- a findings-only investigation after a read-only change (route 7, then route 8, never route 4);
- a joint-invariant review after a change outside its scope (current; its task-result entry is `identity`);
- a `REFUSED` joint-invariant obligation after a later change in scope (stays derived; decision answered once);
- a route-8 `REVALIDATE` waiting on a cross-subject `validity` entry (shown waiting; answerable when the other subject is re-accepted);
- a `BLOCKED` re-attestation (unanswered `REVALIDATE` plus a blocker decision; no iteration spent).

Failed: B1 (a)-(e).

## Minimum architecture and capability transfer

The delta adds no component, record kind or persistent surface. It deletes the 093164f `REFUSED` trigger for routine reviews. The list is the right minimum shape. B1's options 1 and 2 add no mechanism: they delete clauses or define a domain. The 1.6.0 supersession (§26.4) and the version-bound Core and frozen profiles (PEM PC-001) are unchanged. `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## Qualification-design adequacy

§31.4 (line 2681) states discriminating tests for the closed 093164f cases (in-scope NO-PASS, fence awaiting, spent budget, owner-upheld veto, `BLOCKED`, pending first candidate), against the real owners. None of the B1 (a)-(e) cases is listed. A green G2 run of §31.4 as written could therefore coexist with every sibling in B1 (PEM DS-001). The routing model is diagnostic only, and it shares §10.4's order (N3). Nothing is claimed as executed that is not: §31.10's G1 document checks and the model are the only executed items, and §31.9 marks usability as measured at G3.

## Doctrine-realization map and O1

§29 and §0.5 are unchanged since 093164f. The 7.2.1 entrypoints at `aaeaf8b` are unchanged. No new doctrine claim or O1 inspectability claim is made by the delta. The map's levels and disclosed E3 duties were not re-audited row by row in this round (gap). The B1 routing gaps affect the inspector only through items left `OPEN` with no displayed route (N2).

## What was verified and how

- **Snapshot:** `git archive eb86a71` into scratch. Manual and closure-map blobs match the handoff (`3c27c26…`, `482fb79…`). The workplan blob is `91bde23…`, and `orchestrator/docs/architecture.md` is `39e6de7…`.
- **`python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`:** 4 tests, OK.
- **`git diff --check 093164f eb86a71`:** clean (exit 0).
- **`git diff --stat fad3ee4 bf23372`:** 73 files, 23269 insertions, 1 deletion, as expected for the qualification line. `git diff --quiet fad3ee4 eb86a71 -- orchestrator/docs/architecture.md source dist`: exit 0 (byte-unchanged).
- **Diagnostic model:** all six families and all 48 mutations run in parallel, one process each, by importing the module (`run_family`, `MUTATIONS`, `MUT`). Unmutated, every invariant holds in every family: transformation-review/acceptance/gate 1,856,368 scenarios, equivalence-chain 299,760, plan-coverage 205,800, completeness-cover 37,600, gate-basis 1,000, obligation-routing 18,525. All 48 mutations are caught (none `NOT CAUGHT`); the fourteen routing mutations are caught by I13-I18 as the model reports. A green run bounds only what the model represents (N3; B1 (a)-(e) are outside it).
- **Routing family probes:** (`fence`, `keep_fence`, `decide`) leaves the item `OPEN` with `COORDINATE:fence`. `dispatch` integrates at once.
- **Manual text:** the Manual ends with exactly one newline.

**Could not verify:**

- any runtime behavior (no SSDS implementation exists);
- an independent re-derivation of every pre-093164f finding (family-level only, above);
- the full §29 map row by row;
- whether the author intends item obligations to be keyed on the item or on the item revision (B1 (a)).

## Scientific-checks answers

- **Material findings:** B1 and N1-N6 above.
- **Realized results:** this Review produced, ran and reviewed no realized scientific results. Null envelope: the only executions were the repository unit tests and the diagnostic model, which are qualification diagnostics of architecture text, not scientific results.
- **Variants:** one candidate was evaluated (the candidate commit), with its predecessor `093164f` used only as a diff base. The diagnostic model was run in its unmutated form and in its 48 mutations, judged on its own criterion (every invariant holds unmutated; each mutation caught by at least one invariant). No other variants were evaluated.
- **D1/D2 authority:** no accepted D1/D2 scientific authority was relied on for a consequential judgment, so no tension search applies.
- **Gaps:** as listed above.

## Common-mode note

- **Family:** this reviewer is of the Claude family, the Manual author's family. So were most earlier Manual reviewers (all except the 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review, which were of the GPT family).
- **Engagement:** this reviewer was engaged as a fresh-context sub-agent launched by the authoring session.
- **Shared dependencies:** the corpus (Manual, workplan, stakeholder record), the inherited workplan framing, the prior Review records (read as hypotheses; in particular the 093164f record, whose siblings this Review re-derived), the model family's reading habits, and the toolchain (git, Python, the repository's own diagnostic model, whose oracle shares the author's reading).
- **Limits of independence:** fresh context does not establish epistemic independence. B1 (b) and (e) re-find, in narrower form, cases a same-family Review already named.

## D4 statement

This Review authorizes no D4 work. A PASS would have been technical evidence for G1 only. This NO-PASS accepts no architecture, product scope or default value. Acceptance of the Manual belongs to the stakeholder.
