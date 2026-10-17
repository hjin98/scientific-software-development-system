# Independent D3 Review — SSDS 8 Architecture Manual, candidate b365947 (SD-40 confirmation)

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system (full clone, complete history)
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          b365947f33685b3712e7aba1cb2ca20eeff5fbcc (reviewed by git archive snapshot; later commits excluded)
    SCOPE:              the whole Manual as the proposed durable D3 owner, handoff §1 (a)-(g); confirmation of SD-40
    MANUAL blob:        orchestrator/docs/ssds-8.0-architecture.md = df9e40ded5414a8af0199877be0e163f60e9397c (verified)
    CLOSURE MAP blob:   qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md = 132207dced979d241f712c49619c4a8af276fa4f (verified)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md, design revision 23,
                        Phase B candidate e23f14208be869e6a78cfd7b312e447254ee1851 (blob 610f373b..., verified);
                        at the candidate blob 91bde236465178f20c7348280e036d2884dfc216 (verified)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954, recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d
                        (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      every record in qualification/ssds80/ named by the handoff, read as hypotheses only
    REVIEW METHOD:      handoff §3 steps 1-11 with step 6a (family closure after recurrence); falsification by
                        constructed trajectories against the candidate text; routing-model probes; required commands run
    REVIEWER:           Claude family; a fresh-context sub-agent launched by the authoring session

## SERIOUS CHALLENGE

None. No accepted governing authority was found materially false, contradictory, ambiguous, inadequate or unrealizable. SD-40 (stakeholder record item 36) is realizable as stated; both blockers below are in its realization and in its coupling with earlier realizations (SD-34's review reach, SD-38's latest-only reliance). Option 3 of B2 would partly reverse SD-38 and is listed for the stakeholder.

## Verdict

**NO-PASS.** SD-40's core is faithfully realized: no `REVALIDATE` is derived for an integrated enactment's review or task result; §4.1, §10.2, §10.3, §11.5, §13.7, §15.5 and §31.3-§32.3 point to §10.4's list; the R2 "instead" clause is gone; a kept fence's route ends once answered; `DECLINE` is refused for other item decisions; the accepted cost is stated in §10.4 route 6, §31.4 and §32.3. No latch, lowered-state, retirement or `RESOLVED_BY` residue remains. Two blockers remain:

- **B1 (obligation routing; thirteenth round; non-local recurrence).** The list is now ordered and total on its own terms. But four of the objects it reads have no defined lifecycle, so reachable states leave an item `OPEN` with no live route, with two routes, or with a contradictory identity. The four objects are: the item obligation's identity across an R2 amendment, the answered decision of routes 4 and 5, the carrier of an item-level finding that names no part, and the end of a "pending candidate".
- **B2 (judgment disagreement and content identity, coupled with routing).** A re-dispatched enactment's review judges, and discharge relies on, all of `out(o)` (§4.3, §10.4). The transformation-review veto still reaches only reviews with the same *changed-unit* content (§5.10 (b)). An empty or partial re-dispatch after an adverse review is therefore discharged by a peer's pass of the very content the standing objection rejects, with no disagreement derived. An out-of-scope adverse finding is likewise dropped once a pending candidate integrates.

The routing model is green and catches all seven of its mutations. Its unmutated "section claims" are empty in all 38,160 scenarios, though (N1), and it shares the assumptions that hide every B1 sibling and B2 (c).

## Blockers

### B1 — §10.4's list reads four objects whose lifecycle the Manual does not define, so reachable states leave an item obligation with no live route, two routes, or two identities

**Family:** obligation routing (SD-36 to SD-40; the lifecycle family 095ce55 through eb86a71). This is a non-local recurrence: the thirteenth successive round with a blocker in this family. The shared cause is the drift class "two places computing one thing", now in the form "a route keyed on an object whose start, end or identity is stated elsewhere or not at all". (a) and (d) entered with this candidate's own new sentences (the identity sentence and the "pending candidate" definition). (b) is the sibling of eb86a71 N2 that the `DECLINE` refusal did not reach. (c) is the half of eb86a71 B1 (e) that the realization moved but did not give a carrier.

**Earliest owner:** Manual §10.4 (lines 1319-1330). Coupled clauses: §10.2 `COORDINATE(plan)` row (line 1256), §13.4 (line 1497), §13.7 (lines 1545, 1547) and §15.5 (line 1675). These decide workplan §21 items 7 ("obligation rules ..., readiness, three-valued discharge, ... iteration/attempt identity"), 24 ("task-partition checks, budgets") and 26 ("the outcome table for coordination decisions"). Reviewed parents: workplan §7.3, §7.4, §7.8, §7.10. **Status:** open, material.

**(a) Item-obligation identity: the new sentence contradicts itself for every R2 amendment that keeps prose and fixed fields.**

- §10.4, line 1319: "An item obligation's identity is its item and the prose and fixed fields of its accepted revision (§13.4): an R1 tightening keeps it, and an R2 amendment derives a new obligation, so the old one is no longer derived and a candidate bound to it is refused at integration (§8.3 step 7)."
- §13.4, line 1497: "An amendment is control tightening (R1) iff every field of the item and its contract is unchanged or moved only in its tightening direction, and the item's prose is byte-identical; every other change ... is R2." The table orders `write_scope`, `evidence_specs`, `homes`, `budget`, `expectations.slots`, `escalation.triggers` and `scientific`. These are not fixed fields.
- §31.6 (line 2702) uses exactly such a pair: "an R2 amendment to `aQ` incomparable with `a0` ... (`aQ` and `a0` have the same prose and fixed fields)".

Trajectory:

1. `IMPLEMENT(I)` at `ir1` (budget 3, `write_scope {a}`) integrates `X1` and is discharged.
2. The principal widens the write scope to `{a, b}`, or raises the budget to 5. Both are loosenings, so the change is R2, and an independent plan acceptance covers `ir2`. Prose and fixed fields are byte-identical.
3. By the first clause, `I`'s identity is unchanged. The iteration count `k` and `out(I)` carry over, and a pending drift candidate bound to `I` continues. By the second clause, `I` is a new obligation: `k = 0`, nothing is integrated, the pending candidate is refused at integration, and the new obligation is dispatched from scratch.

These are two different routes and two different budgets for one state. An implementer must choose between two statements. The answer also decides whether "raise the budget" or "widen the scope" can answer a route-4 or route-5 decision at all (see (b)).

Under the "new obligation" reading there is a permissive consequence. The new obligation has no integrated enactment. Its natural first candidate is empty, because the content already meets the amended contract. Under the "new obligation" reading it then has `out = ∅` (§10.4: "the set of units its integrated enactments changed") and `subject = ∅` (line 1319: "the union of the subjects every integrated enactment of `o` changed"). Its review carries no output `content` entry (§4.3, line 570: the `out(o)` coverage applies only to "a re-dispatched enactment"). So no later change to the item's content moves anything it reads. The Manual does not say what `status1 of subject(o)`, `ev(subject(o), e)` and `qual(subject(o))` read over an empty subject. Read literally, they are vacuous, and the item stays discharged however its content later changes. This is against workplan §7.4 ("A missing required check is an undischarged obligation; no rule can turn it into PASS").

**(b) An answered route-4 or route-5 decision whose answer leaves the item's identity unchanged strands the item.**

- §10.4, routes 4-5 (lines 1326-1327). Route 4 fires on "a standing adverse review of the latest integrated enactment ... whose findings lie outside the item's write scope or obligations". Route 5 fires on "the budget is spent". Both give `COORDINATE(plan)`.
- §10.2, line 1256: each condition is "one obligation". §15.5, line 1675: for these routes the allowed outcomes are "`AMEND`, `PARTITION` and `ESCALATE`", and "the `COORDINATE(plan)` obligation for it is answered by the first admitted `COORDINATION_DECISION` naming it, like the answered judgment obligations of §10.3". §10.3, line 1299: "An answered obligation is never ready again". §15.5: "`AMEND` | a plan-unit change follows".
- Neither condition can clear by itself. An adverse review is never-lost and "vetoes while it stands" (§8.3 step 6). The count `k` of admitted task results never decreases (§10.3).

Trajectory (route 4):

1. `I` (write scope `{a}`) is integrated. Its reviewer reassesses `X1` as `NO_PASS`, with findings in unit `w` outside `{a}`. Route 4 derives `COORDINATE(plan)`.
2. The principal does the natural thing for a defect outside the item: `AMEND` adding item `J` with scope `{w}`, or amending an existing item that owns `w`. The decision names the route-4 obligation and answers it.
3. `I`'s identity is unchanged, so its route list is re-evaluated. The adverse review still stands, the predicate still fails (no current passing review), and route 4 still precedes route 6. Route 4's obligation is answered and never ready again.
4. After `J` repairs `w`, nothing re-reviews `X1` and nothing re-dispatches `I`. `I` stays `OPEN` forever with only an answered decision. The plan never completes.

The same strand follows a route-5 decision answered by an R1 tightening `AMEND` of `I` (which keeps identity and `k`), or by an `AMEND` of another item (for example the item whose changes keep moving `I`'s outputs). The same holds pre-integration for a pending candidate's `DISCREPANCY` decision. That one is also missing from §15.5's list of decisions with no report: the §10.2 row lists "an out-of-scope NO-PASS finding or a `DISCREPANCY`", while §15.5 lists only "a kept fence, a spent budget, an out-of-scope NO-PASS, an adverse item-level review naming no part". So no outcome set is stated for it.

eb86a71 N2 named this outcome for `DECLINE`, and the repair refuses `DECLINE`. The identical effect of an identity-keeping `AMEND` is untouched. Route 1 ends once its decision is answered ("until a coordination decision answers it"). Routes 4 and 5 have no such end.

**(c) An adverse item-level review whose findings name no part has no carrier.**

- §13.7, line 1545: "their obligation sets partition the item's obligations exactly"; "each part's task is bound to its share's implementer obligation, which the decision derives per part"; "The item is discharged when every part is and an item-level review of the integrated result has passed".
- §10.4 is stated "for an item obligation `o`". Route 2 ("the predicate holds: none, `o` is discharged") precedes route 4's "or, for a partitioned item, an adverse item-level review whose findings name no part: `COORDINATE(plan)`".
- Line 1330: only a review that names a part's outputs makes "each such part's predicate fail[s]". A `REFUSED` item-level review "is handled by the item's own route above".

Trajectory:

1. Item `I` is partitioned into parts `a` and `b`. Both integrate and both are discharged.
2. The item-level review is `NO_PASS` on a joint property, and its findings name neither part's outputs.
3. Neither part's predicate fails, so route 2 gives both parts "none". No whole-item implementer obligation exists to carry the list, because the partition replaced it.
4. The §10.2 trigger derives `COORDINATE(plan)` only for "a route §10.4 gives". No such route is given here, so none is derived.
5. The item-level review obligation is `REFUSED`, the item is never discharged, and no obligation is ready.

eb86a71 B1 (e)'s discriminator "Findings naming no part give `COORDINATE(plan)`" fails at this text.

**(d) A "pending candidate" never stops being pending, so route 3 can select a dead candidate, or several.**

- Line 1319: "A **pending candidate** of `o` is the candidate of a task result admitted for it and neither integrated nor refused."
- Line 1325: route 3, "a pending candidate of `o`: that candidate's ordinary routes above", precedes routes 4-6.
- §11.5, line 1380, and workplan §7.8: "A rejected candidate stays recorded". The Manual and workplan call a NO-PASS'd candidate *rejected*. Admission *refuses* records and requests (§8.3).
- §8.3 step 7: an `INCOMPLETE` or `DISCREPANCY` result's "`TASK_RESULT` ... [is] admitted and the iteration counts". Only its passing judgments are refused.

So a candidate that was NO-PASS'd, `INCOMPLETE`, `PARTIAL` or rebase-conflicted, at any earlier iteration and before or after the first integration, stays pending forever. Route 3 also needs that reading: a re-dispatched candidate's NO-PASS must reach its iteration or `COORDINATE(plan)` through route 3, because route 4 reads only the latest *integrated* enactment.

Trajectory:

1. Iteration 1 of `I` returns `INCOMPLETE`, so candidate `C1` is pending. Iteration 2's `C2` passes and integrates. `C1` is still neither integrated nor refused.
2. Later, the owner upholds a peer's veto of `X2` with findings outside `I`'s scope.
3. Route 3 applies before route 4. It selects `C1`'s ordinary route: "a ... `INCOMPLETE` result ... is the next iteration within budget".
4. The implementer is re-dispatched on a finding it may not fix, and the out-of-scope decision workplan §7.10 requires ("a NO-PASS finding outside the item ... create[s] a `COORDINATE` decision") is not derived until the budget is spent. If `C1` had instead had an out-of-scope NO-PASS or a `DISCREPANCY`, its ordinary route would be a `COORDINATE(plan)` answered long ago, and `I` is stranded (as (b)).

With an iteration in flight there are two pending candidates (the rejected `C_k` and the new `C_{k+1}`), hence two route sets. "That candidate's ordinary routes" is also ambiguous about whether it includes the ordinary "it is dispatched while ready".

**Why the model is green (DS-001).** The routing family represents the four objects so that the defects cannot occur:

- `r2_amend` and `decide_amend` set `retired = True` unconditionally ("an AMEND: an R2 amendment or a withdrawal ends this obligation"). The model has no identity-keeping `AMEND` and no R2 with equal prose and fixed fields.
- I18's "answered decision ends its route" is checked only for `fence == "decided"`.
- `PARTITIONED` is one obligation whose `holds()` includes `parts_adverse is None`. Probe: `rt_derive('PARTITIONED', ('item_review_adverse_none',))` gives `('OPEN', {'COORDINATE:item_review'})`, a carrier the Manual does not have.
- One `cand` slot is replaced on `dispatch` and cleared on `cand_integrate`, so a rejected candidate is never pending beside a later one.
- No revert event exists.

**Violated owner text.**

- **The architecture owner** (`aaeaf8b:source/shared/references/architecture-and-design.md`, line 96): "When an architectural concept carries normative meaning, define it before dependent invariants use it: component/state ownership, allowed/forbidden dependency relations, lifecycle state[s] and transitions". Line 66: "one authoritative representation/state".
- **The workflow owner** (`aaeaf8b:source/shared/references/workflow-and-workplans.md`, line 96): "close each material impact item as resolved, preserved-with-reason, or unavailable/blocking". (b) and (c) leave the item in none of these.
- **The reviewed workplan.** §7.10: "Budget exhaustion, a NO-PASS finding outside the item, and every `DISCREPANCY` create a `COORDINATE` decision"; (d) suppresses this. §7.4: "A missing required check is an undischarged obligation; no rule can turn it into PASS"; the empty-subject reading of (a) breaks this.
- **The Manual's own claims.** Line 1293: "a non-current judgment that a current obligation depends on with neither a ready nor a waiting route" is a defect, and (b) and (c) are that defect for the item obligation itself. Line 1321: "the first of these that applies is `o`'s only route".
- **The handoff's confirmation questions:** "every state of an item obligation (including amendments, pending candidates, fences, budgets, partitions and answered decisions) has exactly one route or is closed".

**Minimum repair direction.** This is a recurrence: the options are for the stakeholder, recommended first. All of them are subtractive or narrowing.

1. **Recommended (narrow, subtractive): define the four objects once in §10.4, and delete the clauses they replace.**
   - **(a):** key identity on what actually changes the route. Either say "an R2 amendment of the item's prose or fixed fields derives a new obligation, and any other amendment keeps it", or say "every R2 amendment derives a new obligation". Pick one, and say whether the new obligation inherits `out(o)`, `subject(o)` and integrated status. Inheriting them removes the empty-subject case. The alternative is to define `subject(o)` for an item obligation as its contract's declared subjects together with the union.
   - **(b):** give routes 4 and 5 the same end as route 1: "until a coordination decision answers it; afterwards the routes below follow" (route 6, with route 5 then reading the budget of the amended revision). Or refuse a `COORDINATION_DECISION` naming a route-4 or route-5 obligation unless its plan-unit change retires, re-keys or partitions `o`. Add `DISCREPANCY` to §15.5's list, or remove it from the §10.2 row.
   - **(c):** carry the no-part clause on each part (route 4 before route 2 for that condition only), or name the carrier (the item-level review's `REFUSED` derives `COORDINATE(plan)` directly, as the event-keyed kinds do in line 1330).
   - **(d):** "a pending candidate is the candidate of `o`'s latest admitted task result after its latest integration (or ever, before it), neither integrated nor refused". Exclude "dispatched while ready" from route 3 explicitly.
2. **Stakeholder alternative (removes mechanism):** drop routes 4-5's separate decisions after integration. Every reopened integrated item is re-dispatched within budget. Out-of-scope findings of integrated enactments become reports routed by §15.3 (a `FINDING` naming the unit), which has its own persistence (§15.2) and closes only by a resolving record. That moves one owed-decision class onto the existing report lifecycle instead of a second one.
3. **Process (do first under either):** extend the routing family with
   - identity-keeping `AMEND` outcomes (R1, another item, an added item);
   - R2 with equal prose and fixed fields;
   - two separate part obligations plus the item-level review as its own obligation;
   - two candidates (a rejected `C_k` beside `C_{k+1}`);
   - a revert;
   - an "answered decision leaves a ready route or a closed state" property over every decision kind, not only the fence.

   Write the section claims as non-empty functions of each section's text (N1).

Given thirteen rounds, the convergence owner's "Review strategy after recurrence" also supports the stakeholder weighing a bounded stop. The routing paragraph would then be accepted with the residual disclosed, and the identity, answered-decision and partition-carrier questions handed to G2 real-owner qualification (§31.5) as named reopen triggers.

**Required discriminator.** Real owners: Derivation (obligation derivation, readiness, discharge), Admission step 7, the Dispatcher's budget check.

- An integrated item R2-amended only in write scope or budget has exactly one stated identity and one route, and the pending candidate's fate is stated.
- An R2 successor whose first candidate is empty is reopened by a later change of the item's output content, or its predicate is stated to read a non-empty subject.
- After a route-4 decision answered by an `AMEND` that adds another item, `I` has a ready route or is closed. The same holds after a route-5 decision answered by an R1 `AMEND`.
- A partitioned item with both parts discharged and an adverse item-level review naming no part derives exactly one `COORDINATE(plan)`.
- An item whose iteration-1 candidate was `INCOMPLETE` and whose iteration-2 candidate integrated takes route 4, never `C1`'s iteration, on a later out-of-scope adverse review.
- The extended routing model fails on this text and passes on the repair.

### B2 — A later enactment's review discharges an item against a standing objection to the same content, because the review veto reaches changed-unit content while discharge relies on all of `out(o)`

**Family:** judgment disagreement / content identity (SD-33, SD-34; the item-31 drift class "a mutable identity versus what was judged", "what is shown versus what is relied on"). It couples with obligation routing. The route entered with SD-38's two clauses (reliance only on the latest integrated enactment's review, and that review covering `out(o)`) together with route 6's "next iteration after an adverse review". It is widened in this candidate by the SD-40 realization: route 6 re-dispatches while a peer's veto still awaits the owner (closure map §5: "an open peer veto of an integrated review re-dispatches the item while its adjudication proceeds", an author choice). This is a sibling in the transformation-review row, not a recurrence in the plan row.

**Earliest owner:** Manual §5.10 (b), the transformation-`REVIEW` and `CONFORMANCE` rows (line 838: reach is "every transformation with the same changed-unit content"). Coupled with §4.3's re-dispatch entry (line 570: "for a review of a re-dispatched enactment of an item obligation `o`, `content` on every unit of `out(o)`") and §10.4 (line 1319: "After integration `o` relies only on its latest integrated enactment's review"; route 6, line 1328). These decide workplan §21 items 3 and 5 (judgment kinds; derivation) and item 7. **Status:** open, material.

**(a) An empty or partial re-dispatch after an in-scope adverse review.**

1. `I` integrates `X1`, changing `u` to `u1` and `v` to `v1`. `R1`'s review passes and `I` is discharged.
2. `R1` reassesses and records `NO_PASS` (the author's supersession, §8.3 step 3), with findings about `u1` within `I`'s scope. Equally, a peer's `NO_PASS` is upheld by the owner. Either way it is a standing adverse review of the latest integrated enactment, so route 6 gives "the next iteration after an adverse review".
3. The implementer disagrees and submits `X2` with no change (`C = B`). Nothing forbids an empty candidate; one is explicitly admissible for drift (line 1330). Alternatively `X2` changes only `v`.
4. Conformance is `CLEAN`. A fresh reviewer `R2` passes `X2`. `R2`'s review carries `content` on `u1` and `v1` (all of `out(I)`), so it judges and is relied on for exactly the content `R1` rejected.
5. The veto check: `R1`'s `NO_PASS` reaches only transformations whose changed-unit content equals `X1`'s (`u1`, `v1`). `X2`'s changed-unit content is empty, or `{v'}`. So `R2`'s pass is not vetoed and no `ADJUDICATE_DISAGREEMENT` is derived (§10.2 trigger: "a standing adverse judgment `x` that vetoes a passing judgment").
6. `X2` integrates. By line 1319 `I` relies only on `X2`'s review, and route 4 reads only "the latest integrated enactment". `I` is `DISCHARGED` on content its own reviewer, or the owner, has standing-rejected.

The §16.5 re-review carry (line 1781) puts `R1`'s findings in `R2`'s brief by default. That is disclosure, not enforcement: "policy may withhold them only where independence of the re-review requires it", and a `RESOLVED` entry by `R2` is a brief rule, not relief. Relief of a review veto is only "the adverse judgment's own author's or the owner's independent passing judgment on that exact target" (§5.10, line 838).

**(b) A peer's veto awaiting the owner (the SD-40 author choice).** A peer `P` records `NO_PASS` on `X1`; `R1`'s pass is vetoed, so `I` reopens and route 6 re-dispatches at once. The steps continue as (a) 3-6 and `I` is discharged on `X2`. The owner then upholds `P`. `P`'s objection stands, but it is not on the latest integrated enactment, so route 4 does not read it and the item stays discharged. The owner's adjudication of the disagreement decides nothing about the item it concerned.

**(c) An out-of-scope finding masked by a pending candidate, then dropped.** While a drift candidate `X2` of `I` is pending, `R1` reassesses `X1` as `NO_PASS` with findings outside `I`'s write scope. Route 3 precedes route 4, so no `COORDINATE(plan)` is derived. `X2` passes on its own diff and integrates. `X1` is no longer the latest enactment, so route 4 never fires, and the finding (about content `X2` did not touch) never reaches the principal. The model reproduces this green:

- `rt_derive('IMPLEMENT', ('move_out','dispatch','adverse_out'))` gives `('OPEN', {'REVIEW:candidate'})`;
- adding `'cand_pass','cand_integrate'` gives `('DISCHARGED', set())`, with `adverse` reset to `None` by `cand_integrate`.

**Violated owner text.**

- **The Manual's own invariants.** §10.4, line 1317: "∃ a passing judgment never discharges against a standing objection, in either order of admission". §5.10 (line 857) and §8.3 step 3: "No qualified peer supersedes another actor's judgment; a contrary peer judgment is a disagreement". §5.10 (a), line 822: "A reach compares what a judgment judged."
- **The reviewed workplan, Admission step 7** (blob 91bde23, line 1427): never-lost records are admitted "so nothing reported or observed adversely is lost and admission order never settles a disagreement". §7.10: "a NO-PASS finding outside the item ... create[s] a `COORDINATE` decision"; (c) breaks this.
- **Stakeholder record item 31** (the author's drift classes, adopted as this Review's method by the handoff): "what is shown versus what is relied on", "a mutable identity versus what was judged".

**Minimum repair direction** (narrowing first):

1. **Recommended (narrow, no new mechanism):** state the transformation-review and conformance reach over what the review's output `content` entries judge, not over its changed units only. A standing `NO_PASS` of `X1` then reaches every review whose output entries include each of `X1`'s changed units at the same content. That covers a re-dispatched review of unchanged `out(o)`. The SD-34 claim ("what a review judged is the change") becomes "what a review judged is the content its output entries name", which equals the change for a first enactment.
2. **Route-level alternative:** give route 6's "next iteration after an adverse review" a precondition that the new enactment changes every unit the standing adverse review's findings name, or route an empty or partial answer to `ADJUDICATE_DISAGREEMENT`. This one adds a rule; mark it as mechanism. For (b), restore the 093164f N4 ordering (an open peer veto routes to the owner's adjudication before any re-dispatch), which the closure map lists as an author choice to confirm. For (c), place route 4 before route 3 for a standing adverse review of the latest integrated enactment.
3. **Stakeholder option (partly reverses SD-38):** make discharge read every integrated enactment's review whose judged outputs are still current, so a standing objection of an earlier enactment keeps the item open until the author, the owner or an upheld challenge ends it.

**Required discriminator.** Real owners: Derivation (`base`, veto reach, discharge), Admission step 3.

- After `R1`'s `NO_PASS` of `X1` and an empty `X2` passed by `R2`, `I` is not discharged, and `ADJUDICATE_DISAGREEMENT` (or `REFUSED`) is derived.
- The same holds for a partial `X2` that does not change the units the findings name.
- After a peer's `NO_PASS` that the owner later upholds, the item reopens or was never discharged in between.
- An out-of-scope `NO_PASS` of `X1` admitted while drift `X2` is pending derives `COORDINATE(plan)` before or at `X2`'s integration.
- A core-family scenario with a re-dispatched review's output entries covering an unchanged unit fails at this text.

## Non-blocking findings

### N1 — The routing family's section claims are empty unless mutated (DS-001; eb86a71 N3 still partly open; SD-40's "each section's trigger written from its own text" not realized)

`RtState.claims()` adds a route only under a named mutation. In all 38,160 unmutated scenarios it returns the empty set (probe run at the candidate). §31.3 (line 2672) says the family "checks §10.4's route list against each section's own route claim (§4.1 and §10.2 `REVALIDATE`, the §10.2 `COORDINATE(plan)` row, §11.5 rebases, §13.7 iterations and budget, §15.5 outcomes, §22.3 fences)". In fact the list is checked against nothing: each section's current text is assumed to coincide with `list_route()`, and I14 can fire only from a mutation's injected claim. SD-40 directed "the routing model is extended first ..., with each section's trigger written from its own text". Write each section's claim unmutated from its own text, and restate §31.3's claim accordingly. The I18 docstring and §31.3 also claim "an answered decision ending its route" generally, but the code checks only the fence (B1 (b)).

### N2 — Peer veto and re-dispatch ordering changed without a stated cost

SD-40's realization deletes eb86a71's route "a peer's or human's adverse review ... whose veto awaits the owner: that `ADJUDICATE_DISAGREEMENT`". It now re-dispatches beside the adjudication, which spends budget on a veto the owner may dismiss. The closure map §5 lists this as an author choice to confirm. §32.3 does not state the cost. See B2 (b) for the permissive consequence.

### N3 — Stale residue in the closure map

Closure map §7 row 7 still lists "§4.1 (a task result re-attests after integration while it is the latest enactment's and `out(o)` has not moved)". §5 still lists the SD-37 author choice "a task result re-attests after integration while its outputs are current". SD-40 removed both. The closure map is a review aid, so this is non-blocking.

### N4 — §31.4 and §32.3 state the R1 cost differently

§31.4 tests "an R1 tightening after integration that the integrated content fails re-dispatches it". By §4.3 (the task result's `EXACT` entry on the item revision) and §32.3, *every* R1 tightening of an integrated item re-dispatches it, including one the content already satisfies. State the cost as §32.3 does, and add the satisfied case to §31.4.

### N5 — Editorial

- The R15 row (line 100) says "with no post-integration revalidation (SD-40)" unqualified. It means only an item obligation's review and task result; acceptances and gate decisions still derive `REVALIDATE` after integration.
- Line 549 has a doubled space ("(§10.4);  a review").
- §13.7 (line 1547) keeps "Budget exhaustion, a NO-PASS finding outside the item, and every `DISCREPANCY` create a `COORDINATE` decision" beside the §10.2 row's list. That is harmless if read as a pointer, but it is a second statement of the trigger (eb86a71 N1, partly closed).

## Closure audit

The closure map was used to navigate. Its claims were checked for every §21 item the delta or the blockers touch. The candidate changes 18 line groups of the Manual relative to `eb86a71` (lines 100, 549, 570, 1190, 1256, 1293, 1319-1330, 1378, 1545, 1547, 1675, 2672, 2678, 2779). Every other line is byte-identical to the `eb86a71` text, whose closure audit this Review takes as a hypothesis and spot-checked.

| Item | Disposition at this candidate |
|---|---|
| 3, 5 (judgment kinds; derivation) | partly open: B2, the transformation-review reach versus the re-dispatched review's judged content |
| 6 (Admission order) | closed; step 8 (line 1190) is unchanged in substance and points to §10.4 |
| 7 (obligation rules, readiness, discharge, iteration identity) | **partly open (B1 (a), (b), (d); B2)**; item-obligation identity is now stated but contradictory for R2 with equal prose and fixed fields |
| 9 (joint invariants) | closed; eb86a71 N5 is answered (line 570 scopes the `validity` and governing-closure entries) |
| 24 (partition, budgets) | **partly open (B1 (b), (c))** |
| 26 (coordination outcome table) | **partly open (B1 (b))**; outcomes for route 4/5 decisions exist but do not all end the route; `DISCREPANCY` has no stated outcome set |
| 1-2, 4, 8, 10-23, 25, 27 | no unresolved architectural decision found in this bounded audit (text unchanged since `eb86a71`) |

The §16.2 rows (§26.4) are unchanged. Each keeps an explicit replacement, retirement or preserved boundary, and none was found unresolved. Material decisions are marked against delegated D4 choices as before. No new over-specification was found.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1-R14 | text byte-identical to `eb86a71` §0.3 (only line 100, the R15 row, changed); sound as assessed in the earlier records. Spot-checked: R9 (an answered obligation is never ready again; this is what makes B1 (b) a strand rather than a re-ask) and R12 (a re-dispatch is a new task and enactment; consistent) |
| R15 | sound as the stakeholder-chosen narrowing of reviewed step 8 to evidence regression (SD-36). SD-40's re-dispatch on read-only, governing and R1 changes goes beyond workplan §7.8's "review is re-requested only where the review's basis no longer holds". It is surfaced (stakeholder record item 36; the R15 row; §32.3), so it is a disclosed change, not an unsurfaced one. The row's claim of "one route statement in §10.4" is not yet true, by B1 |

## Re-verification of earlier findings (family level)

**eb86a71 Review:**

- **B1:**
  - (a) R2 after integration: the "instead" clause and its echoes are deleted. Closed for the two-route defect. Open as B1 (a) for the new identity sentence.
  - (b) pending re-dispatched candidate: closed for a genuinely pending candidate (route 3; I18). Open as B1 (d) for rejected or `INCOMPLETE` earlier candidates, and B2 (c) for the masking.
  - (c) kept fence: closed (`AMEND` or a resuming `DECLINE`; the route ends once answered).
  - (d) re-attestation failing `HARD` templates: closed by removing post-integration re-attestation.
  - (e) adverse item-level review: closed for findings naming a part (line 1330). Open for findings naming no part (B1 (c)).
- **Non-blocking findings:**
  - N1: partly closed (N5).
  - N2: closed for `DECLINE`. Its sibling, an identity-keeping `AMEND`, is open (B1 (b)).
  - N3: partly closed (N1).
  - N4: closed (line 1330 states the disagreement's own obligation is not an item route).
  - N5: closed.
  - N6: closed.

**093164f Review:**

- B1 (a)-(f): closed as eb86a71 recorded, except that (a)'s item-level case is now B1 (c), and (c)'s pending case is now B1 (d).
- N1: superseded by §15.5's new text (B1 (b) for its outcomes).
- N2: the `BLOCKED` result is a blocker report (line 1321). Closed.
- N3: N1 here.
- N4: reversed by the SD-40 realization (N2 and B2 (b) here).
- N5: closed.

**8f4e75d Review, B1 (a)-(f) and N1-N6:** closed by mechanism as 093164f and eb86a71 recorded. The SD-37 waiting route is removed by SD-40, so (a)'s and (e)'s waiting variants are moot. B2 here is a new sibling in the reliance-on-latest clause that those Reviews introduced.

**f185036 Review, B1 (a)-(c) and non-blocking findings:** closed. Event-keyed judgment obligations end in current state with `REFUSED` kept (lines 1256-1271, 1330). `subject(o)` is the union. The drift brief and empty transformation are stated. The empty transformation's interaction with an R2 successor is B1 (a).

**Obligation-lifecycle family (095ce55, c77447b, 3940dbc, 3876473, 494c810, c4e8de7; B1 and N items):** closed by SD-36's removal of the mechanism. A search of the candidate for latch, lowered-state, retirement and `RESOLVED_BY` residue finds only the §6 assessment latches (lines 656, 1087), which predate R15, and the unrelated "retired" key and ref vocabulary. Their non-blocking findings are moot with the mechanism.

**82d618c B1 and N1-N7:** B1 closed by the step 8 narrowing (line 1190). Its three cases (a later item editing an earlier item's outputs, a second change in a joint invariant's scope, a second `AUTHOR` revision) integrate per §31.4 (line 2678). The non-blocking findings are as recorded since.

**edabd81 B1-B2 and N1-N7; 653e88c B1 and N1-N4; d94a293 B1 and N1-N3:** closed as recorded (`standing` mode on the revision assessment; gate `record` only on required premises; `identity` elsewhere). Text unchanged; the gate-basis family is green with its three mutations caught.

**Judgment-disagreement family (§3.4, §5.3, §5.5, §5.10, §6.7, §8.3 step 3, §10.2-§10.4), via closure map §7, 3540d98 through 913db8f:**

- Text is byte-identical to `eb86a71` outside the routing rows.
- The direct-record rules, the plan row's closed form (SD-30 to SD-32), content keying of the review and conformance vetoes (SD-33 to SD-34), the authorship-keyed requirement and the brief carries were not reopened by the delta.
- One new sibling, B2, arises in the review row's key from the routing coupling. It does not reopen the plan row.
- The SD-30 to SD-34 plan-row claim was re-read and is not challenged here.
- The four judgment families' mutations: see "What was verified".

**Different-family Reviews (a6ed164, 9e5a763, d6734c4, both e548472, b46c250):** their findings concern text unchanged since; dispositions are as the intervening records state.

**Assessment-disagreement family (§6), Phase B closures and N1-N4 carry-forward:** §6 is unchanged since many candidates. Phase B N2 (completeness polarity), support cycles, corrupt prefixes and the matching clause were not re-derived trajectory by trajectory in this round, because the delta does not touch them. This is a bounded gap, not a closure claim.

**Every other listed Review (6ff4ed1 through 362af9f):** this Review did not re-derive each finding independently. Their dispositions are as the intervening records state. This is a gap, not a closure claim.

## Out-of-matrix trajectories attempted

Held:

- a fence awaiting its decision with a pending candidate (route 1 only);
- a kept fence answered by `DECLINE` (route 6 drift re-application) or by an R1 `AMEND` (routes below follow);
- the human's "re-apply" (route 1 ends; drift; a new task, consistent with §8.3 step 7 and R12);
- a plain overtake (route 6 drift);
- a read-only change after integration (route 6, a fresh enactment; empty transformation; no `REVALIDATE`);
- a governing change and an R1 tightening (route 6);
- a pending candidate's clean rebase over a read-only change (its `REVALIDATE`, no second re-dispatch);
- a pending candidate whose integrated predecessor's predicate holds again (route 2; the candidate's later integration is refused as a duplicate discharge; wasted review only);
- a spent budget with an R2 `AMEND` that changes prose (new obligation; exits);
- a `PARTITION` answer to a spent budget (new part obligations; exits);
- an adverse item-level review naming one part (that part reopens and is re-dispatched; the item-level review is derived anew);
- a `REFUSED` joint-invariant review (stays derived; its decision lapses once answered);
- the 82d618c cases (integrate).

Failed: B1 (a)-(d), B2 (a)-(c).

## Minimum architecture and capability transfer

The delta removes mechanism: post-integration `REVALIDATE` routes, the R2 "instead" route, the separate peer-veto route and the `DECLINE` outcome for item decisions. No new component or persistent surface is added. No capability an owner requires is dropped by the removal itself. The re-dispatch churn is a disclosed operational cost (§32.3).

Architecture 1.6.0 (`orchestrator/docs/architecture.md`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee4` (verified), so the version-bound Core and frozen profiles are preserved (PEM PC-001). B1's option 2 and B2's option 1 narrow rather than add.

## Qualification-design adequacy

§31.4 lists the SD-40 trajectories at real owners (Derivation, Admission, the Dispatcher). The discriminators in B1 and B2 are absent from it: an identity-keeping `AMEND` after routes 4 and 5, R2 with equal prose and fixed fields, a no-part item-level review with discharged parts, a rejected earlier candidate, and an empty re-dispatch after an adverse review. The diagnostic model is green while B1 and B2 hold (N1), so it cannot close these owner claims (the testing owner: "Ask whether evidence could remain green while that owner is materially broken. If yes, it cannot close that owner claim"). Nothing is claimed as executed that is not, except §31.3's description of what the routing family checks (N1).

## Doctrine-realization map and O1

§29 and §0.5 are unchanged since `eb86a71`. No new duty or E-level assignment is affected by the delta. B2 bears on the reviewer-independence realization (S9 "an agent PASS is a recommendation", and a peer's pass must not settle a disagreement). The map's assignment is unaffected, but the mechanism it relies on is the B2 reach.

## What was verified and how

- **Candidate and inputs.** Snapshot by `git archive b365947f...` into `$TMPDIR/ssds80-manual-review-b365947/snap`. Manual, closure-map and workplan blobs verified with `git rev-parse` / `git hash-object`.
- **Deltas.** Word diff against `eb86a71` (18 Manual line groups; closure map 4 groups; stakeholder record item 36 and the SD-40 row read).
- **Governing owners** read at `aaeaf8b`: `source/roles/software-design/SKILL.md` (entry contract item 4; review routing), `architecture-and-design.md` (lines 66, 96), `workflow-and-workplans.md` (line 96), `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review strategy after recurrence"), `testing-and-validation.md` ("Proxy-proof real-owner evidence").
- **`python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`:** 4 tests, OK.
- **`git diff --check eb86a71... b365947f...`:** clean (exit 0).
- **`git diff --stat fad3ee4 bf23372`:** 73 files, 23269 insertions, 1 deletion (qualification and workplan additions).
- **`git diff --quiet fad3ee4 b365947f -- orchestrator/docs/architecture.md source dist`:** exit 0 (byte-unchanged). `orchestrator/docs/architecture.md` blob `39e6de7...` verified.
- **Diagnostic model** (`judgment_disagreement_model_check.py`), run by importing the module and running each family and each mutation's named families in parallel (equivalent to `--mutations`).
  - Routing family: 38,160 scenarios, no failures. Its seven mutations are caught: `revalidate_after_integration` (I14, I15), `r2_instead_clause` (I14, I15), `rebase_before_first_only` (I14, I18), `pending_ignored` (I18), `kept_fence_persists` (I14, I15, I18), `item_review_parts_discharged` (I14, I15), `decline_allowed_for_items` (I13).
  - Gate-basis family: no failures; its three mutations caught.
  - Completeness-cover family: no failures; its mutations caught.
  - Core, equivalence-chain and plan-coverage families: no failures.
  - Overall: all six families green unmutated, and all 41 mutations caught (none `NOT CAUGHT`).
  - Run under heavy host load, by a scratch driver at `$TMPDIR/ssds80-manual-review-b365947/scripts/par.py`.
- **Probes** (scratch only): unmutated section claims empty in every routing scenario; `PARTITIONED`/no-part routed by a single-obligation model; the pending-candidate masking and the drop at integration (B2 (c)); `decide_amend` always retiring.

Not verified:

- runtime behavior of any real owner (no implementation exists; G2-G4);
- per-trajectory re-derivation of the assessment-disagreement family and of findings from 6ff4ed1 through 362af9f (gaps, as stated);
- whether the empty-subject reading in B1 (a) is the intended one. It is shown to be what the text says, not what the author meant.

## Scientific-checks answers

- **Material findings:** B1 and B2 above; there are no scientific findings, since this is a D3 review of orchestration architecture.
- **Realized results:** none produced, run or reviewed. The diagnostic model's runs are qualification diagnostics of written rules, not scientific results.
- **Variants:** one candidate commit was evaluated. Alternative readings of two sentences (the B1 (a) identity sentence; the B1 (d) "refused") were evaluated, two each, with the criterion "does every reading give one route and preserve the governing invariant".
- **Accepted D1/D2 authority:** none was relied on for a consequential judgment, so no tension search is reported.
- **Gaps:** as listed under "Not verified".

## Common-mode note

This reviewer is of the Claude family, the Manual author's family. It was engaged as a fresh-context sub-agent launched by the authoring session. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family; the others were of the Claude family.

Fresh context does not establish independence. This Review shares with the author and the earlier same-family reviewers:

- the corpus;
- the inherited workplan framing;
- the prior Review records, read as hypotheses (B1 extends eb86a71 B1 and N2, whose framing it inherits);
- the toolchain (git, Python, the diagnostic model, which shares the author's reading of §10.4);
- the model family.

A different-family confirmation of B2 in particular would reduce common-mode risk, since it concerns a reach rule both families have reviewed before.

## D4 statement

This Review authorizes no D4 work. A PASS would have been technical evidence for G1 only, accepting no architecture, product scope or default value. This NO-PASS routes B1 and B2 to the Manual's earliest owners (§10.4; §5.10 (b) with §4.3 and §10.4) and, as a recurrence, their options to the stakeholder.
