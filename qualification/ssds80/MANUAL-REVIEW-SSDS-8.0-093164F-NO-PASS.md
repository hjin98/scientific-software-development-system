# Independent D3 Review — SSDS 8 Architecture Manual, candidate 093164f (SD-38 confirmation)

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          093164f5deb56e18160c6dcca3200b042e103460
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g)), with the
                        SD-38 confirmation questions first; technical evidence for G1 only
    MANUAL blob:        270e69e1b74b367e1546c307635bf16b98dbd9fe (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   4b4a7fe4334f5ae62bd90539b5b1ededec487afa (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family 8f4e75d
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; 8f4e75d..093164f read line by line and
                        sentence by sentence (15 changed lines of the Manual); a route sweep of every
                        post-integration and pre-integration state of the item and event-keyed obligations
                        against every section that derives a route for them (§4.1, §4.3, §8.3, §10.2-§10.4,
                        §11.5, §13.7, §15.5, §22.2-§22.3, §31, §32.3); the diagnostic model run in full
                        (six families, all mutations, in parallel); structural checks of handoff §3 step 9;
                        family-level recheck of earlier families on the unchanged text
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched by
                        the session that issued this handoff (the authoring session); did not author the
                        candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-093164f/snap`. The later commit adding the handoff (`00c25922`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. SD-38 (stakeholder record item 34) is realizable and its parts are mutually consistent: an adverse revalidation or re-attestation of an integrated item is a §13.7 NO-PASS iteration (workplan §7.3, §7.10); one key `out(o)` with "moved" a state; reliance on the latest enactment's review only; investigator items alike; one overtake route; the joint-invariant minimum inside its scope. The blocker below lies in the realization and in one repair of a previous non-blocking finding, and can be repaired without reversing SD-36, SD-37 or SD-38.

## Verdict

**NO-PASS.** One blocker, in the obligation-routing family (the obligation lifecycle after integration; its eleventh round counting from 095ce55). Earliest owner: Manual §10.2-§10.4, deciding workplan §21 items 7, 9, 24 and 26.

What SD-38 asked for is realized for the case its model represents (an integrated `IMPLEMENT` item with one or more enactments, its reviewer's own revalidation, a plain overtake, a joint-invariant review whose only reliance is output and scope content):

- `out(o)` and "moved" as a state are defined once (line 1319) and read by §4.1 (line 549), the `REVALIDATE` row (line 1261), §8.3 step 8 (line 1190) and §13.7 (line 1536);
- only the latest integrated enactment's review is relied on, and a re-dispatched enactment's review covers `out(o)` (lines 570, 1261, 1319), which closes 8f4e75d B1 (a) and (b);
- the reviewer's adverse revalidation and a non-`COMPLETE` re-attestation start the §13.7 iteration (lines 1319, 1536), which closes the single-enactment trajectory of 8f4e75d B1 (c);
- a plain overtake has one route and no `COORDINATE(plan)` trigger (lines 1256, 1319), closing 8f4e75d B1 (d) for the overtake;
- the joint-invariant review's output entries are limited to `Δ(X) ∩ scope(i)` (line 570);
- the 8f4e75d N1, N2, N4 and N6 items are answered.

The routing family is green and catches all its mutations. It does not represent any of the six siblings below; one of them is literally its own `ji_full_delta_minimum` mutation, which the Manual's text still prescribes through another entry.

## Blockers

### B1 — Routes for one obligation state are still derived in several sections that disagree: the N3 repair gives every routine NO-PASS a second, principal route, and the post-integration key is not reconciled with the task-result entry, never-integrated items, pending rebases, fences, budgets and other adverse answers

**Family:** obligation routing (SD-36 to SD-38; the lifecycle family 095ce55 through 8f4e75d). Non-local recurrence. Sibling (a) entered through the repair of 8f4e75d N3, the previous round's non-blocking finding; (b)-(f) are cases the SD-38 realization stated over a narrower domain than the sections it is coupled with.

**Shared cause** (drift class "two places computing one thing"): which route an obligation has in a state is written where each case is discussed (§4.1, §10.2 rows, §10.4 prose, §11.5, §13.7, §22.3, §32.3) rather than derived once from the obligation's state; each new clause is written for its own case with its domain left implicit, so the other sections' routes for the same state stay in force. The model computes routes only from its own `RtState.item()`, so a route derived by another section is invisible to it.

**Earliest owner:** Manual §10.2 (`COORDINATE(plan)` and `REVALIDATE` rows), §10.4 (the key, readiness, the event-keyed end), §4.3 (`REVIEW` minimum), §13.7, §15.5, deciding workplan §21 items 7 (readiness, discharge, iteration identity), 9 (joint invariants), 24 (budgets, partition) and 26 (the coordination outcome table). Reviewed parents: workplan §7.3, §7.4, §7.9, §7.10. **Status:** open, material.

**(a) Every routine NO-PASS now owes a principal decision as well as its mechanical iteration (entered through the 8f4e75d N3 repair).**

Exact rules at the candidate:

- §10.4, line 1319: "A judgment obligation keyed on a past event (`REVIEW(X)` and conformance, `JOINT_INVARIANT(i, k)`, `SPEC_REVIEW(spec, r)`, a partitioned item's item-level review) … one whose answer is a standing adverse judgment (`REFUSED`) stays derived … and it derives a decision for the principal (§10.2)."
- §10.2, line 1256, new `COORDINATE(plan)` trigger: "a `REFUSED` event-keyed judgment obligation derived from an enactment of its items (§10.4)".
- §10.3, line 1299: an adverse answer "closes it undischarged" (that is `REFUSED`, line 1303); the `REVIEW(X)` row (line 1258) keeps `REVIEW(X)` derived "while `X` is unintegrated", which for a rejected iteration's transformation is forever.
- §13.7, line 1536: "Within budget, an `INCOMPLETE` result or a NO-PASS whose findings all lie within the item's write scope and obligations … starts the next iteration mechanically (R0) … Budget exhaustion, a NO-PASS finding outside the item, and every `DISCREPANCY` create a `COORDINATE` decision." Line 1534 (new): "an adverse item-level review is a NO-PASS of the item under the budget rule below".
- §15.5, lines 1653-1662: "A coordination task decides each routed report … The allowed outcomes are a function of the report's kind, reason and target domain"; `RESOLVE_LOCAL`, `AMEND` and `DECLINE` are allowed only for named report kinds; only `CHALLENGE`, `ESCALATE` ("any") and `PARTITION` ("items") remain for a decision with no report.

Trajectory:

1. `IMPLEMENT(I)` iteration 1 submits `X1`; conformance `CLEAN`; `REVIEW(X1)` is answered by an independent `NO_PASS` whose findings all lie in `I`'s write scope.
2. `REVIEW(X1)` is `REFUSED`. By §13.7 iteration 2 starts mechanically (R0). By line 1319 and the line 1256 trigger, `COORDINATE(plan)` is also derived for the principal: two routes for one NO-PASS.
3. The principal's decision has no outcome §15.5 defines for this trigger. It is not a report, so `RESOLVE_LOCAL`, `AMEND` and `DECLINE` are not allowed. The admissible answers are `CHALLENGE` (against the reviewer), `ESCALATE` (human attention) or `PARTITION`. So every in-scope NO-PASS of every item must be challenged or escalated to the human, or the plan carries an owed decision. `REVIEW(X1)` stays derived and `REFUSED` forever, so the trigger never lapses (§15.2 closes only report-derived obligations).
4. The same holds for a `CONFORMANCE` NO-PASS, and for the peer-veto case §31.5 tests (line 2683), which now has three routes: the R0 iteration, `ADJUDICATE_DISAGREEMENT` and `COORDINATE(plan)`.
5. For a partitioned item, an adverse item-level review is "a NO-PASS of the item under the budget rule" (line 1534), but no item-level implementer obligation exists to iterate: the parts' obligations partition the item's and are each discharged by their own reviews. The mechanical route has no carrier, and the principal route has no admissible repair outcome (`AMEND` is not allowed). 8f4e75d B1 (c) named this sibling ("The same choice covers a `REFUSED` item-level review"); it is unresolved.
6. For the post-integration cases N3 targeted (`JOINT_INVARIANT`, `SPEC_REVIEW`, high-consequence review), the decision the principal owes is a repair, but `AMEND` is not an admissible outcome for a non-report trigger. Only `ESCALATE` or `CHALLENGE` can answer it. The new kept-fence trigger has the same gap: the `COORDINATE(plan)` it waits on ("re-apply, amend or withdraw the item", line 1319) has neither an `AMEND` nor a "re-apply" outcome in §15.5.

This changes reviewed workplan §7.10, which routes an in-scope NO-PASS to R0 alone and lists exactly three `COORDINATE` triggers: budget exhaustion, an out-of-scope finding and a `DISCREPANCY`. The change is not listed in §0.3. It also contradicts the Manual's own §13.7 and §10.2's deliberate split, where adverse acceptance and plan-acceptance answers go to the principal and adverse reviews iterate.

**(b) A joint-invariant review still relies on outputs outside the invariant's scope, through its `record` entry on the task result (8f4e75d B1 (f), partly closed).**

- §4.3, line 570: the joint-invariant clause narrows only "the output `content` entries". The same row still gives every `REVIEW` on `X`, this one included, "`record` on the candidate's current task result".
- §4.3, line 576: a `TASK_RESULT` carries "frame-role `content` on reads and on `Δ(X)`", so its output entries cover every changed unit, inside or outside `scope(i)`.
- §4.1, line 549: after integration a stale task result derives `REVALIDATE` only "while it is its obligation's latest enactment's task result and `out(o)` has not moved … after integration it derives nothing otherwise".

Trajectory:

1. Change `k1` (item `I`) changes `u ∈ scope(i)` and `w ∉ scope(i)`. `JOINT_INVARIANT(i, k1)` is answered `PASS` by `rJ1`, whose minimum carries `record` on `k1`'s task result `t1`.
2. A later item edits only `w`. No `JOINT_INVARIANT(i, k2)` is derived (§9.2), so `JOINT_INVARIANT(i, k1)` stays derived (line 1271).
3. `t1`'s output entry on `w` fails, so `t1` is non-current, and with it `rJ1`.
4. `out(I)` has moved, so `t1` derives no `REVALIDATE`, and `I` is re-dispatched as drift. That drift re-does only `w`, outside the scope, so no successor joint-invariant obligation is derived. After the drift integrates, `t1` is no longer the latest enactment's task result either.
5. `REVALIDATE(rJ1)` is derived (line 1261: `rJ1` acts, is non-current, and `JOINT_INVARIANT(i, k1)` depends on it). Every answer's minimum needs a current task result for `k1`'s candidate, which can never exist again, so step 6 refuses every answer. This is the defect §10.3 (line 1293) names.
6. On the other reading, line 1319's "derived only while what it judged can still be current" ends `JOINT_INVARIANT(i, k1)`. If `rJ1` was still in flight, `k1`'s in-scope change is then never reviewed against `i`, a finding retired unseen.

The model's `ji_full_delta_minimum` mutation, a joint-invariant minimum covering an output outside the scope, is caught by I13. That is the configuration this row prescribes through the task-result entry, so the model transcribes §4.3 without that entry. The high-consequence review has the same shape.

**(c) The post-integration key has no stated domain: never-integrated item obligations and pending candidates fall outside it or under its exclusion (8f4e75d B1 (e), partly closed).**

- `REVALIDATE` row, line 1261: "never for an item obligation's review other than its latest integrated enactment's". The previous text was scoped to "the review of an integrated transformation"; the new text is not scoped to integration at all.
- §10.4, line 1319, opens with "One key after integration" for "an item obligation `o` (implementer or investigator)".
- §11.5, line 1369: "Records-only work (reviews, investigations whose output is findings) has no integration step." Line 1367: after a clean rebase, "a stale review derives `REVALIDATE`".

Trajectory, findings-only investigation:

1. A findings-only `INVESTIGATE` item `J` is discharged on its review `r`. It never integrates (§11.5).
2. A later change edits a file the investigator and the reviewer read. `r` is non-current, and `J` reopens (current-state discharge).
3. `J` has no integrated enactment, so either:
   - by the row's literal text, `r` is "other than its latest integrated enactment's" and `REVALIDATE(r)` is never derived. §10.4's waits and its NO-PASS iteration, both keyed on "after integration", do not apply. Only the task result's `REVALIDATE` exists (line 549, "while its transformation is unintegrated"). After the re-attestation, `r` stays non-current with no route;
   - or `J` falls to generic §10.3 readiness (line 1295) and is ready. A new investigation is then dispatched on a read-only change beside the task-result `REVALIDATE`: two routes, and the re-dispatch SD-38 forbids for investigator items.
4. §31.4 (line 2665) requires "waits on one `REVALIDATE` chain whose holder is the investigator". No section derives that. The model reaches it only by representing the investigation as an integrated enactment with an empty delta (`RtState.__init__`), an assumption the Manual does not state.

Trajectory, pending candidate: a first-iteration candidate `X` of `o`, or a drift candidate while `X1` is the latest integration, has a passing review whose context entry fails after a clean rebase. The row's text excludes its `REVALIDATE`, since no integrated enactment of `o` is `X`'s. §11.5 line 1367 derives it. An implementer must choose.

**(d) A fence moves `out(o)`, so the drift rule and the fence wait both apply.**

- Line 1319: "ready again only in two cases: as drift to repair (§8.6) while `out(o)` has moved, the one route then". Later in the same paragraph: "While a fence awaits its human decision (§22.3), its item obligation waits; after a decision to keep the fence it waits on the principal's `COORDINATE(plan)`".
- A fenced integration is an admitted integration of `o` (§8.3 step 7, line 1189: "even when that integration was `OVERTAKEN` or fenced"). The fence restores `tree(B_n)` (§22.3, lines 2118, 2120), so `out(o)` has moved.
- So the first sentence makes drift ready while the human's `CRITICAL` decision (§15.4: re-apply or keep) is pending. Drift would re-apply `n`'s work as a new task before the human decides, which §22.3 reserves to the human. After "keep", drift and `COORDINATE(plan)` are both live.
- If the fence sentence is read as an exception, "the one route then" is false as stated, and the precedence must be written.
- The model has no fence event.

**(e) Budget exhaustion with moved outputs.**

- §10.4 makes drift "the one route" while `out(o)` has moved, with no budget condition. Its NO-PASS case alone says "within budget and scope, otherwise `COORDINATE(plan)`".
- §13.7 derives `COORDINATE` on "Budget exhaustion".
- §32.3, line 2766, says each re-dispatch spends "the item's iteration budget (after which it goes to `COORDINATE(plan)`)".
- After exhaustion, then, either drift stays ready beside the budget-exhaustion decision (two routes), or drift is unbudgeted. In the second case the disclosed drift ping-pong between two items editing one unit ("bounded only by budgets") is unbounded.
- The model has no budget.

**(f) The NO-PASS iteration is keyed on the reviewer's revalidation event, not on the state of the latest enactment's transformation (8f4e75d B1 (c) variant, open).**

- Line 1319: the item is ready as a NO-PASS iteration only "when … its latest review's revalidation is adverse or the … re-attestation … is not `COMPLETE`".
- Line 1536 says, more broadly, "a NO-PASS … (after integration including an adverse revalidation …)".

Trajectory:

1. After integration, an authenticated human, or a never-lost adverse record from a task in flight, records `REVIEW NO_PASS` on the latest enactment's `X1`. It vetoes `r`.
2. `REVALIDATE(r)` is never derived for a vetoed judgment (line 1261). `ADJUDICATE_DISAGREEMENT` goes to the owner. §10.4's wait list does not name it.
3. The owner agrees and records the adverse record superseding `r`, which §10.3 names as an answer. `ADJUDICATE_DISAGREEMENT` ends, and `REVALIDATE(r)` would end anyway ("superseded").
4. `out(o)` has not moved, and no revalidation answered `REVALIDATE(r)`. By §10.4 `I` is `OPEN` with no ready route. By §13.7 it iterates.

8f4e75d B1 (c) stated this variant ("The result is the same if the adverse record does not supersede: it vetoes `r0`, `ADJUDICATE_DISAGREEMENT` follows, and the owner upholds it"). The model's `revalidate_adverse` event is only the author's own supersession.

**Violated owner text.**

- **The architecture owner** (`aaeaf8b:source/shared/references/architecture-and-design.md`, "D3 formal-contract discipline"): "When an architectural concept carries normative meaning, define it before dependent invariants use it: … lifecycle states and transitions". Also line 66: "one authoritative representation/state".
- **The D3 entry contract** (`aaeaf8b:source/roles/software-design/SKILL.md`), item 4: "prefer cohesive ownership, direct flow, one authoritative representation/state".
- **The workflow owner** (`aaeaf8b:source/shared/references/workflow-and-workplans.md`): "close each material impact item as resolved, preserved-with-reason, or unavailable/blocking". (b), (c) and (f) leave items in none of these states.
- **The reviewed workplan, §7.10:** "Within it, an `INCOMPLETE` result, or a NO-PASS whose findings all lie within the item's write scope and obligations, starts the next implementer iteration mechanically (R0)", and "Budget exhaustion, a NO-PASS finding outside the item, and every `DISCREPANCY` create a `COORDINATE` decision". (a) adds a principal route to the first, unlisted in §0.3. **§7.9:** "The outcomes allowed are a function of the report's kind, reason and target domain". (a) adds triggers that have no outcomes.
- **The Manual's own claims:** §10.3 (line 1293) calls "A ready obligation whose every answer Admission must refuse … and … a non-current judgment that a current obligation depends on with neither a ready nor a waiting route" defects. §10.4 says "the one route then" and "none waits on a revalidation that no admissible answer can satisfy".
- **The handoff's confirmation questions:** "every item and event-keyed obligation has exactly one defined route in every state, including after several enactments, partial moves, reverts, empty transformations and adverse answers".

**Minimum repair direction.** This is a recurrence: the options are for the stakeholder, recommended first. Every option holds SD-36 to SD-38 fixed.

1. **Recommended, mostly subtractive: one route statement per item obligation state, owned by §10.4, which every other section only points to.**
   - **(a):** restrict the new `COORDINATE(plan)` trigger to event-keyed obligations whose adverse answer arrives after integration and whose kind has no mechanical iteration (`JOINT_INVARIANT`, `SPEC_REVIEW`, high-consequence review). Remove `REVIEW(X)` and conformance from it, which removes a trigger case. Make an adverse item-level review a NO-PASS iteration of the parts whose outputs its findings name (otherwise `COORDINATE(plan)`). Give §15.5 one row for non-report triggers, allowing `AMEND` (and `DECLINE` with a reason outside the floors); this adds one row to an existing table.
   - **(b):** for a review answering `JOINT_INVARIANT(i, k)` or a high-consequence review, replace the `record` entry on the task result by `identity`, or drop it. The review judges the integrated result, not the implementer's attestation. This removes an entry, so the row's end equals what the answer judged.
   - **(c):** state the key's domain once. An item obligation with no integrated enactment (every obligation before its first integration, and every findings-only investigation) keeps the pre-integration routes, including the `REVALIDATE` of its current candidate's review. Scope the row's exclusion to "after `o`'s first integration". For findings-only investigations, either define the admission of the reviewed result as the enactment's integration for this key, or state that they keep the pre-integration `REVALIDATE` and are never re-dispatched on a read-only change.
   - **(d)-(e):** in the same sentence, state that a fence awaiting or kept, and budget exhaustion, take precedence over drift.
   - **(f):** key the NO-PASS iteration on the state "the latest enactment's transformation carries a standing adverse `REVIEW` judgment, or its task result's latest re-attestation is not `COMPLETE`", not on the revalidation event.
2. **Stakeholder alternative (removes mechanism; partly reverses SD-37/SD-38's waiting route):** after `o`'s first integration, derive no `REVALIDATE` for item reviews or task results. Every reopened item obligation is re-dispatched (drift), budget-limited, or goes to `COORDINATE(plan)` past its budget. This is 8f4e75d option 3. (c) pending-candidate, (f) and most of (b) vanish. (a), (d) and the findings-only half of (c) still need their statements. It accepts the read-churn cost SD-37 removed.
3. **Process option:** before the next candidate, make the routing model derive routes from every section's triggers, the §10.2 `COORDINATE(plan)` row, §11.5, §13.7 budgets and §22.3 fences included. Give its reviews the full §4.3 minimum, task-result entry included. Add events for the cases above. The model then cannot be green by construction for a route another section derives.

**Required discriminator.** Real owners: Derivation (obligation derivation, readiness, discharge), Admission steps 6-8, the Dispatcher's budget check.

- An in-scope `REVIEW NO_PASS` before integration derives the R0 iteration and no `COORDINATE(plan)`. The same holds for `CONFORMANCE`. The §31.5 peer-veto case derives the owner's adjudication and the iteration only.
- An adverse item-level review of a partitioned item has exactly one route, with a named carrier obligation.
- `k1` changing `u` in `i`'s scope and `w` outside it, then a change to `w` only, then the drift integrating: `JOINT_INVARIANT(i, k1)`'s review stays current, or its `REVALIDATE` has an admissible answer. It is neither stranded nor retired unanswered.
- A findings-only `INVESTIGATE` after a read-only change: one `REVALIDATE` chain (task result, then review) and no re-dispatch, derived from the Manual's text with no integration assumed.
- A pending first-iteration candidate whose review's context entry fails after a clean rebase derives `REVALIDATE` of that review.
- A fenced integration awaiting its human decision: no drift dispatched. After "keep": exactly one route.
- Budget exhausted with `out(o)` moved: exactly one route.
- A human's `REVIEW NO_PASS` on an integrated item's latest transformation, upheld by the owner's superseding adverse record: exactly one ready route, the §13.7 iteration.
- The routing model with the full §4.3 minimum and the §10.2 `COORDINATE(plan)` triggers must fail on today's text and pass on the repair.

## Non-blocking findings

### N1 — §15.5 has no outcomes for `COORDINATE(plan)` triggers that are not reports (inherited, widened)

Budget exhaustion, recurrence (§15.7), a task result stale through an R2 amendment (§4.1) and the kept fence are all `COORDINATE(plan)` triggers. Workplan §7.9 and §15.5 key outcomes on a report's kind, reason and domain, so only `CHALLENGE`, `ESCALATE` and `PARTITION` are formally admissible for these triggers, and `AMEND` is not. The workplan shares the gap for budget exhaustion and recurrence. B1 (a) widens it.

How such an obligation closes is also undefined: §15.2 closes only report-derived obligations, and `COORDINATE` is not in R9's list of answered judgment obligations (line 1299). Repair with B1 (a)'s one row.

### N2 — A `BLOCKED` re-attestation is treated as a NO-PASS

Line 1319 makes any re-attestation "not `COMPLETE`" a NO-PASS iteration. That spends an iteration and re-implements the item on an environment or prerequisite blocker. Elsewhere `BLOCKED` leaves a judgment obligation unanswered and dispatchable (line 1299), and a blocker report goes to `COORDINATE` (§15.3). Say "`PARTIAL` or `INFEASIBLE`", or route `BLOCKED` as a blocker.

### N3 — The routing family's properties share the rule's definitions, and its state assumes facts the Manual does not state (DS-001; 8f4e75d N5, partly closed)

What improved: the family now has units, revisions, several enactments, per-review basis entries and adverse answers, and its I13 answerability is computed from the entries rather than from a restated rule.

What remains:

- I15's `moved_state` is the unmutated `moved()`.
- I13's entry test equals `answerable()`.
- Every route it checks comes from `RtState.item()`. Routes derived by §10.2's `COORDINATE(plan)` row, §11.5, §13.7 or §22.3 cannot appear in it.
- It represents a findings-only investigation as integrated (an assumption, B1 (c)).
- It gives the joint-invariant review no task-result entry (B1 (b)).
- It has no fence, budget, principal decision, peer or owner adverse review, or pending rebase. §31.3 (line 2659) discloses only "no specification review, no several-subject evidence and no principal decision".

I13-I16 and I18 are the right local properties. Two properties are missing:

- "one route per state across all sections' triggers";
- "every owed decision has an admissible outcome".

I17 is absent from the numbering ("I13-I18" in the docstring).

### N4 — §10.4's wait list omits `ADJUDICATE_DISAGREEMENT`

When the latest review is vetoed, the item waits on the owner's adjudication. That route is not named in line 1319's list ("on `REVALIDATE` of its latest review …, on its required evidence's routes, and on its subjects' `ACCEPT` and `GATE` obligations"). Editorial, tied to B1 (f).

### N5 — Editorial

- §31.3 (line 2659) introduces the sixth family as "(§10.4, SD-36, SD-37)"; it should cite SD-38.
- The routing-family docstring's "I13-I18" omits I17.
- Closure map item 7's "investigator items alike" claim reads well only under the model's assumption (B1 (c)).

## Closure audit

The closure map was used to navigate. Its claims were checked for every §21 item that the delta or B1 touches.

| Item | Disposition at this candidate |
|---|---|
| 6 (Admission order) | step 8 closed as SD-36 to SD-38 direct; 8f4e75d N1 and N2 closed (line 1190) |
| 7 (obligation rules, readiness, discharge, iteration identity) | **partly open (B1)**: (a), (c), (d), (e), (f) |
| 9 (joint invariants) | **partly open (B1 (b))**; otherwise closed (line 1226: "same marked surface") |
| 24 (budgets, partition) | **partly open (B1 (a) item-level review, B1 (e))** |
| 26 (coordination outcome table) | **partly open (B1 (a); N1)**; the map's "CARRIED" for §15.3-§15.5 does not cover the new triggers |
| 1-5, 8, 10-23, 25, 27 | no unresolved architectural decision found in this bounded audit; text unchanged since 8f4e75d (sentence diff: only lines 100, 549, 570, 1190, 1226, 1256, 1261, 1319, 1534, 1536, 1727, 2659, 2665, 2689, 2766 changed) |

The §16.2 rows are unchanged (§26.4). Every row keeps an explicit replacement, retirement or preserved boundary, and none was found unresolved.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1-R14 | text byte-identical to 8f4e75d's §0.3 rows (only line 100, the R15 row, changed); sound as assessed in the 8f4e75d and earlier records; spot-checked R9 ("an answered obligation is never ready again"), which is consistent with the REFUSED ends, and R12 (a re-dispatch is a new task and enactment), consistent with §5.2 and §10.4 |
| R15 | sound as the stakeholder-chosen narrowing of reviewed step 8 (evidence regression only), with SD-37/SD-38's routing stated in its row. Its consequences are B1. The step-8 exemption is now well defined (8f4e75d N1 closed). The R15 row's summary ("an item obligation being re-dispatched as drift while `out(o)` has moved, iterating on an adverse revalidation, and otherwise waiting") inherits B1 (d)-(f). B1 (a) is a change to workplan §7.10 that §0.3 does not list |

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **M** moot (mechanism removed); **D** design/disclosure closure with real-owner execution owed later; **R** retained, disclosed decision or stakeholder option; **P** partly closed; **O** open.

**The 8f4e75d Review, finding by finding:**

| Finding | Disposition |
|---|---|
| B1 (a), stranded earlier-enactment review | **C** (lines 1261, 1319: latest enactment only; earlier reviews history) |
| B1 (b), partial re-dispatch, two routes or none; "moved" twice | **C** (one `out(o)`, a state; re-dispatched review covers `out(o)`, line 570; revert and empty-transformation readings closed) |
| B1 (c), no exit after an adverse revalidation | **C** for the reviewer's own adverse supersession and a non-`COMPLETE` re-attestation; **O** for the peer- or owner-adverse variant (B1 (f)) and the partitioned item-level review (B1 (a) step 5) |
| B1 (d), plain overtake | **C** (one route, drift; the `OVERTAKEN` trigger removed from line 1256); the fence variant **O** (B1 (d)) |
| B1 (e), investigator items | **P**: included in the key and the holder named (line 549); never-integrated findings-only investigations outside the key (B1 (c)) |
| B1 (f), joint invariant after an out-of-scope output change | **P**: output entries narrowed; the task-result `record` entry still covers all of `Δ(X)` (B1 (b)) |
| N1, step-8 exemption | **C** (line 1190) |
| N2, "keeps its value" | **C** (line 1190) |
| N3, `REFUSED` decision route; late adverse answer | late answer **C** (line 1319); decision route over-broadened: **O** as B1 (a) |
| N4, §31.6 (Z) second half | **C** (line 2689) |
| N5, model independence | **P** (N3 here) |
| N6, editorial | all three **C** (lines 1319, 1727, 1226) |
| 8f4e75d discriminators | T1, T3, overtake, revert and the out-of-scope joint invariant are met as the model represents them. T2 is met for the author's revalidation only. The investigator case is met only under the model's assumption |

**f185036 B1 (a)-(c), N1-N6:** dispositions as in the 8f4e75d record, re-checked on the changed lines. B1 (a) and (b) are now **C** except where B1 (b) and (d) here reopen them; B1 (c) **C**; N4 **C** (8f4e75d N1); N5 **P** (N3 here).

**Obligation-lifecycle family (095ce55, c77447b, 3940dbc, 3876473, 494c810, c4e8de7 B1 and their N items; 82d618c B1):** **M**. SD-36 removed the latch, lines, lowered and waiting states, retirement and `RESOLVED_BY`. A residue search of the Manual, the closure map and the model found none: "latch" occurs only in §6.4's start latch and in §32.3's disclosure of transient-push failures, and `RESOLVED_BY` occurs nowhere. 82d618c B1 is **C** by the step-8 narrowing; §31.4 (line 2665) states its three cases as integrating. The non-blocking items of these records keep the dispositions of the 8f4e75d record (re-adopted as hypotheses; their text is unchanged). 494c810 B1 (c)'s "owed decision had no outcomes" recurs in shape as N1 and B1 (a) step 6.

**Judgment-disagreement family (3540d98 onward, closure map §7 to §5.10 and its pointing sections):** §5.10, §3.4, §5.3, §5.5, §6.7 and §8.3 steps 3 and 6 are byte-unchanged since 8f4e75d. The earlier per-record dispositions (a6ed164, bf23372, 34803df, 0d2b35e, 83a82df, d6734c4, both e548472, 4c52205, 5895687, 913db8f, d94a293, 653e88c, edabd81 B1-B2 and N1-N7, and the 6b986de-to-3540d98 chain) carry from the 8f4e75d record unchanged. The four judgment families, the gate-basis family and every one of their mutations were rerun green and caught (results under "What I verified"). The SD-30 to SD-34 plan and review rows were not re-derived over every tightening-order shape in this round, since their text is unchanged; that is a stated limit, not a closure claim. The new `COORDINATE(plan)` trigger (B1 (a)) is the only delta touching a consumer of §5.10's `REFUSED`.

**Earlier families (matching clause, D1-D3 change rule, content identity, gate qualification, equal-region partition, enactment unit, run identity; 6ff4ed1 through e2154ac, both b46c250, f22b4dc, 362af9f, 61cd09b, f03b15e, 63ddf91, 051cce3, 9e5a763, 51070e5, 29da56e, 6b986de):** no Manual line owning these families changed. §1.5, §5.2, §5.5, §6, §7, §10.2's revision-run block, §17.5 and §19.5 are byte-identical to 8f4e75d. Dispositions are as recorded there. Phase B closures and N1-N4 carry-forward: §6 is unchanged, and Phase B N2 (completeness polarity) was not re-run by trajectory in this round, which is a stated limit. The restrictive-direction attack in this round found B1 (a): a mechanical stop turned into a principal decision.

## Out-of-matrix trajectories attempted

- Held:
  - several enactments with a read-only change after a drift (one `REVALIDATE`, answerable);
  - partial re-do then a move of the other unit (drift only, not discharged before re-work);
  - revert of a moved output with a concurrent read change (one route);
  - empty drift transformation (`out(o)` rebased, not moved);
  - plain overtake (drift only);
  - two items sharing an output (ping-pong disclosed, bounded only if budgets bound drift; B1 (e));
  - deletion of an output unit (drift, conflict to the principal);
  - in-scope second change ending `JOINT_INVARIANT(i, k1)`;
  - `REFUSED` joint invariant from an in-flight task after its successor (re-derived);
  - the drift result of an obligation discharged meanwhile by a revert (step 7 routes it to revalidation).
- Failed: B1 (a)-(f) above.
- Not attempted at depth this round: the unchanged §5.10 plan-row shapes, §6 matching edge cases and loss boundaries (text unchanged since the 8f4e75d record, which attempted them).

## Minimum architecture and capability transfer

The delta adds one trigger to an existing kind (B1 (a), to be narrowed), one entry to the re-dispatched review's minimum (as 8f4e75d option 1 marked), and the `out(o)` definition. It removes the `OVERTAKEN` trigger and the joint-invariant review's out-of-scope output entries. No primitive, component or persistent surface was added. The B1 repair directions remove or narrow an entry or a trigger, except one §15.5 row (marked).

`orchestrator/docs/architecture.md` and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41`. 1.6.0 supersession §26.4 is unchanged, so PC-001 holds (the version-bound Core and frozen profiles are untouched). No capability an owner requires is dropped by the delta. B1 (a) instead adds an unrequired decision.

## Qualification adequacy

§31.4 (line 2665) and §31.6 (Z) (line 2689) now state the 8f4e75d discriminators. They would discriminate B1 (b) and the findings-only half of B1 (c) at real owners, provided the fixtures use the full §4.3 minimum and a never-integrated investigation. No §31 case tests:

- that an in-scope NO-PASS derives no `COORDINATE(plan)`;
- the item-level review's route;
- a fence awaiting decision;
- budget exhaustion with moved outputs;
- a peer- or owner-adverse review after integration.

Green fixtures could therefore coexist with B1 (a), (d), (e) and (f) (DS-001). Nothing is claimed executed that is not: §31 marks real-owner cases as required and unexecuted, and §31.10's G1 document checks are the only executable ones.

## Doctrine-realization map and O1

§29, §0.5 and the O1 surfaces are unchanged since 8f4e75d. No new duty or mark was introduced. The 8f4e75d dispositions stand. The convergence row (§29.3, line 2504: recurrence creates a `COORDINATE` carrying the convergence duty) is unaffected. B1 (a) makes ordinary NO-PASS coordination indistinguishable in kind from recurrence coordination, which dilutes that duty's signal.

## What I verified and how; what I could not verify

- **Candidate identity:** blob `270e69e1…` (Manual) and `4b4a7fe4…` (closure map) match the handoff; workplan blob `91bde236…`.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the snapshot: 4 tests, OK.
- `git diff --check 8f4e75d 093164f`: clean (exit 0).
- `git diff --stat fad3ee41 bf233728`: 73 files, 23269 insertions, 1 deletion, all additions as expected (Manual, qualification records, model).
- `git diff --quiet fad3ee41 093164f -- orchestrator/docs/architecture.md source dist`: unchanged (exit 0).
- **Diagnostic model** (`python3 -I`, families and mutations run in parallel through a scratch driver that imports the module by path and calls `run_family` with `MUT` set per mutation): every family green unmutated. Scenario counts:
  - transformation-review/acceptance/gate: 1,856,368;
  - equivalence-chain: 299,760;
  - completeness-cover: 37,600;
  - plan-coverage: 205,800;
  - gate-basis: 1,000;
  - obligation-routing: 43,346.

  All 43 mutations are caught. The ten routing mutations are caught by I13-I16 and I18 (`ji_full_delta_minimum` by I13). This shows only that the model's transcription of the rules agrees with its oracle on its scenarios. B1's siblings lie outside its state space (N3).
- PEM read at the candidate; byte-identical to `main` (`af045575`), the designated publication line. HAS:
  - DS-001 applicable and applied (N3, Qualification);
  - PC-001 applicable, holds;
  - others not materially applicable.
- **Could not verify:** any real-owner behavior (no implementation exists); the unchanged §5.10 plan and review rows over every tightening-order shape; Phase B N2 by trajectory; the 1.6.0 transfer rows beyond confirming they are unchanged.

## Scientific-checks answers

- **Material findings:** B1 (a)-(f), N1-N5, all architectural. None concerns a scientific result.
- **Realized results:** I produced, ran or reviewed no realized scientific results (null envelope). The only executions were the repository's structural test, git checks and the diagnostic model, none of which is a scientific result.
- **Variants:** I evaluated more than one variant only of review readings. Each sibling was read under the two textual readings an implementer could take, and the criterion was whether either reading yields exactly one defined route.
- **D1/D2 authority:** I relied on no accepted D1/D2 authority for a consequential judgment, so no tension search applies.
- **Gaps:** as listed under "could not verify".

## Common-mode note

I am of the Claude family, the Manual author's family, as were the reviewers of 8f4e75d, f185036 and most earlier rounds. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 reviewers and the Phase B reviewer were of the GPT family. I was engaged as a fresh-context sub-agent launched by the authoring session.

Shared dependencies: the corpus, the inherited workplan framing, the prior Review records (read as hypotheses; three of this round's siblings were seeded by naming in the 8f4e75d record), the diagnostic model and the toolchain. Fresh context does not establish epistemic independence. Because the obligation-routing family has now recurred through realizations that followed same-family Reviews' option 1, a different-family Review of the repaired candidate is advisable.

## D4 statement

This NO-PASS authorizes no D4 work and accepts no architecture, product scope or default value. A PASS would be technical evidence for G1 only.
