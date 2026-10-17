# Independent D3 Review — SSDS 8 Architecture Manual, candidate 8f4e75d (SD-37 confirmation)

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          8f4e75df4990ae30387ed51225b9ae13f607737d
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g)), with the
                        SD-37 confirmation questions first; technical evidence for G1 only
    MANUAL blob:        78a76025ae60230aedce13c70373d4baf0214496 (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   69f986e031ff245767de3951d93f91718c80f6d2 (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family f185036
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; f185036..8f4e75d and 82d618c..8f4e75d
                        read sentence by sentence with a sentence-level diff script; an answer-or-route sweep
                        of every post-integration state of every obligation kind of §10.2 (one and several
                        integrated enactments, output, read-only, governing, out-of-scope and absorbed
                        changes, passing and adverse answers, overtake, fence); an independent hand-coded
                        sketch of the §10.2/§10.4 routing over several enactments (scratch, not a repository
                        artefact); the diagnostic model run in full in parallel; structural checks of
                        handoff §3 step 9; family-level recheck of earlier families on the unchanged text
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched by
                        the session that issued this handoff (the authoring session); did not author the
                        candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-8f4e75d/snap`. The later commit adding the handoff (`9194a8f3`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. SD-37 (stakeholder record item 33) fixes three things: re-dispatch only when an enactment's outputs moved, otherwise wait on the review's `REVALIDATE`; current-state ends for event-keyed judgment obligations, `REFUSED` ones kept; `subject(o)` as the union over enactments. Each is realizable. The blocker below lies in how the Manual realizes them (workplan §21 item 7) and can be repaired without reversing SD-37.

One point needs the stakeholder's confirmation because SD-37's wording does not settle it. A revalidation of an integrated item can be answered adversely. The reviewed workplan (§7.3, §7.10) and Manual §13.7 then start the next iteration mechanically. Literally read, SD-37 ("re-dispatch only when the enactment's outputs moved") forbids that. See B1 (c) and the options.

## Verdict

**NO-PASS.** One blocker, in the obligation-lifecycle family. This is its tenth round. The earliest owner is Manual §10.2-§10.4, deciding workplan §21 item 7.

- **B1, post-integration routing keyed on different objects.** SD-37's ending of event-keyed obligations and its single-route rule hold for the case the Manual and the model describe: one item, one integrated enactment, one review, a passing revalidation. They do not hold once the case widens:
  - **Several enactments:** the item has been re-dispatched, so it has several integrated enactments and several reviews.
  - **An adverse answer:** a revalidation answered adversely.
  - **A non-implementer item:** an `INVESTIGATE` item.
  - **An out-of-scope change:** a joint-invariant review whose transformation also changed units outside the invariant's scope.
  - **A plain overtake.**

  Each route is keyed on a different object. The readiness clause is keyed on the item obligation and every one of its enactments. The `REVALIDATE` exclusion is keyed on each review's own transformation. The discharge `∃` ranges over any one review. The `JOINT_INVARIANT` end is keyed on the invariant's scope, while its answer's basis covers all of `Δ(X)`. In the wider cases these keys disagree, and six siblings follow:
  - **(a)** a stranded `REVALIDATE` of an earlier enactment's review;
  - **(b)** two ready routes, or no reopening, after a partial re-dispatch;
  - **(c)** no exit after an adverse revalidation;
  - **(d)** drift and `COORDINATE(plan)` both ready after a plain overtake;
  - **(e)** investigator item obligations falling to generic readiness;
  - **(f)** a stranded `JOINT_INVARIANT` revalidation after an out-of-scope output change.

What SD-37 asked for is otherwise realized:

- `REVIEW(X)` is derived only before integration (line 1258).
- `SPEC_REVIEW(spec, r)` is derived while the specification is at `r` (line 1270).
- `JOINT_INVARIANT(i, k)` and the high-consequence review end at a later change in scope (lines 1226, 1271).
- The item-level review is re-derived over the latest integrations (line 1534).
- `REFUSED` obligations stay derived (line 1319).
- `subject(o)` is the union over enactments (line 1319).
- A read-only change to a once-integrated item waits on its review's `REVALIDATE`, with one route (lines 549, 1261, 1319).

The f185036 N1-N3 and N6 items are answered, and N4 partly (N1 here). The routing family of the diagnostic model is green and catches its eight mutations. Its state has one review, and its revalidation always passes, so it cannot represent any sibling except (d) and (f), and it models neither of those.

## Blockers

### B1 — After integration, the routes of one item obligation are keyed on different objects, so several-enactment, adverse, non-implementer, out-of-scope and overtake cases strand, duplicate or silently skip work

**Family:** the obligation lifecycle after integration (095ce55 through f185036). It is a non-local recurrence. It entered through the realization of SD-37, the previous round's repair.

Its shared cause is drift class "two places computing one thing": readiness, the `REVALIDATE` exclusion, discharge's `∃` and the event-keyed ends are each stated over a different object, and the answer's mechanical minimum (§4.3) is a fifth object. §10.3's own rule ties dispatch to that minimum. These are not lifecycle states added by machinery: the defect is in definitions of existing triggers.

**Earliest owner:** Manual §10.2 (`REVALIDATE` and `JOINT_INVARIANT` rows), §10.4 (readiness, waiting, the event-keyed end), §4.1 (task-result route) and §4.3 (the `REVIEW` minimum for `JOINT_INVARIANT`), deciding workplan §21 item 7. Workplan §7.1, §7.3, §7.4 and §7.10 are the reviewed parents. **Status:** open, material.

**Exact rules at the candidate.**

- **§10.2, line 1261 (`REVALIDATE(x)`):** "a judgment acting in the state (§5.2), no longer current there, that a current obligation depends on: one whose discharge predicate needs `x`'s currency because no other judgment satisfies the term `x` is in … never for the review of an integrated transformation whose outputs have moved since its obligation's latest integration, which is re-dispatched instead (§10.4)".
- **§10.4, line 1319, readiness:** "A reopened implementer obligation is **ready again**, as drift to repair (§8.6), only when a change admitted after its latest integration has moved the output content of one of its integrated enactments; otherwise it **waits** on the routes of its failing terms: `REVALIDATE` of its non-current review …".
- **§10.4, line 1319, discharge and the event-keyed end:** "It is never discharged on a review of outputs that have since moved." And "A judgment obligation keyed on a past event (`REVIEW(X)` and conformance, `JOINT_INVARIANT(i, k)`, `SPEC_REVIEW(spec, r)`, a partitioned item's item-level review) is derived only while what it judged can still be current".
- **§10.4 discharge predicate:** "∃ current judgment j of kind(o) on subject(o) …".
- **§4.1, line 549:** a stale task result derives `REVALIDATE` "while its transformation is unintegrated or, after integration, while its outputs are current (SD-37) … after integration with moved outputs it derives nothing".
- **§10.2, line 1271 (`JOINT_INVARIANT(i, k)`):** "an admitted change touching a joint invariant's scope … until a later admitted change in the same scope derives `JOINT_INVARIANT(i, k')`, or while `REFUSED`".
- **§4.3, line 570 (`REVIEW` on `X`):** "frame-role `content` on every unit of `Δ(X)` (before-image and output …); for a review answering `JOINT_INVARIANT(i, k)`, ctx `content` on every unit of `i`'s scope".
- **§10.3, line 1293:** "a judgment obligation is dispatched only while an answer of its kind with its mechanical minimum basis (§4.3) can hold at Admission step 6 … A ready obligation whose every answer Admission must refuse is a defect, and so is a non-current judgment that a current obligation depends on with neither a ready nor a waiting route".
- **§13.7, line 1536:** "Within budget, an `INCOMPLETE` result or a NO-PASS whose findings all lie within the item's write scope and obligations starts the next iteration mechanically (R0)". Workplan §7.3: "a NO-PASS leaves the obligation undischarged and the next task is a new iteration". Workplan §7.10 says the same as §13.7.
- **§10.2, line 1256:** `COORDINATE(plan)` is triggered by "an `OVERTAKEN` admission (whose item obligation stays `OPEN`, §10.4)". §10.4 makes the item wait only "While a fence or an `OVERTAKEN` admission awaits its human decision (§22.3)". §22.3 raises a human decision only for a fencing absorption or a late publication.
- **§10.2 holders:** `INVESTIGATE` is held by the investigator. §12.3's investigator template holds no `REVALIDATE`. §10.4's readiness clause names only "implementer" obligations.

**(a) Decisive trajectory: a stranded review of an earlier enactment.**

1. `IMPLEMENT(I1)` integrates `X1` (`Δ = {u}`). Review `r0` reads `g`. The obligation is discharged.
2. A later accepted item `I2` edits `u`. `r0` is non-current through its output entry. A change after the latest integration moved `X1`'s output, so `I1` is ready as drift. `REVALIDATE(r0)` is excluded. One route.
3. The drift task produces `X1'` (`Δ = {u}`, re-doing `I1`'s intent on `I2`'s content). Its review `r1` also reads `g`. `X1'` integrates. `I1` is discharged by `r1`.
4. `I3` edits only `g`. Now `r0` and `r1` are both non-current. No output moved after the latest integration (`X1'`), so `I1` waits on `REVALIDATE`.
   - `r0` acts: it is an integrated enactment's review, superseded by nothing, because `r1` judges another target.
   - `I1` depends on `r0`: no current judgment satisfies the `∃` term, so literally "no other judgment satisfies the term".
   - The exclusion does not apply to `r0`: `X1`'s outputs moved at step 2, which is before the latest integration, not after it.
   - So `REVALIDATE(r0)` is derived. Its only answer is a superseding review of `X1`, whose minimum needs `X1`'s output entry `(u, rev(u, C1))`. That entry never holds again, so step 6 refuses every answer.
   - This is §10.3's named defect. `REVALIDATE(r1)` is also derived and is answerable.
5. If `r1`'s revalidation passes, `r0` stops being depended on and its `REVALIDATE` ends: the strand is transient. If it is adverse, see (c): the strand is permanent.

The reviewer's sketch (`scripts/multi_enactment.py`, trajectory T1) reproduces this: "WAITING; REVALIDATE of reviews ['r0', 'r1']; unanswerable ['r0']".

**(b) A partial re-dispatch: two ready routes, or no reopening at all.**

1. `X1` changes `u` and `v`.
2. `I2` moves `u`. Drift produces `X1'` with `Δ = {u}`, the normal drift case, since the brief names only what moved. Its reviewer `r1` reads `v`. `X1'` integrates, and `I1` is discharged.
3. `I4` moves `v`, which is an output of `X1`. Two routes are now ready:
   - **Drift.** "moved the output content of one of its integrated enactments" holds.
   - **`REVALIDATE(r1)`.** `X1'`'s outputs did not move, so the exclusion does not apply, and the route is answerable.

   If the reviewer's superseding review lands first, `I1` is discharged and the drift result is "bound to an already-discharged obligation … routed to revalidation" (§8.3 step 7). The item is closed on a review of `X1'` although `X1`'s output was undone, and "It is never discharged on a review of outputs that have since moved" holds only by its wording.
4. **Variant:** `r1` did not read `v`. `I1` stays `DISCHARGED` after `I4` moves `X1`'s output, and nothing reopens it. This contradicts §32.3 ("a later admitted item's change, to an integrated item's outputs makes its obligation `OPEN` and ready again") and the readiness clause's own range over every enactment.

The sketch's T3 shows both: "READY(drift); REVALIDATE of reviews ['r1'] … TWO ROUTES", and "DISCHARGED".

**Sub-variant: "moved" is defined twice.**

- §4.1 keys the task-result route on state ("while its outputs are current").
- §10.2 and §10.4 key the exclusion and readiness on an event ("have moved since", "a change … has moved").
- After a revert of `u` to `X1`'s bytes while `g` also changed, the event reading makes `I1` ready as drift and excludes `REVALIDATE(r0)`. §4.1 still derives the implementer's `REVALIDATE` of the task result, so two implementer routes run.
- After an empty drift transformation (§10.4, `C_n = B_n`), whether a later change to `u` "moved the output content" of `X1`, whose output bytes were already gone, has no stated answer. One reading gives one route, the other gives two.

**(c) No exit after an adverse post-integration revalidation (single enactment).**

1. `I1` integrates `X1`.
2. `I2` changes a file `g` that `r0` read. `I1` waits on `REVALIDATE(r0)`, as SD-37 requires.
3. `r0`'s author re-reviews under the changed context and finds that `X1` no longer meets the contract. Evidence still passes, since step 8 admitted `I2`. The author records `REVIEW NO_PASS` superseding `r0`, which §8.3 step 3 authorizes as "the record's own author's reassessment". The result is the same if the adverse record does not supersede: it vetoes `r0`, `ADJUDICATE_DISAGREEMENT` follows, and the owner upholds it.
4. `I1` is now `OPEN`:
   - `REVALIDATE(r0)` has ended, because `r0` is superseded or vetoed.
   - No output moved, so by §10.4 `I1` is not ready.
   - `REFUSED` applies only to judgment obligations.
   - No `COORDINATE(plan)` trigger covers an adverse review of an integrated item. Line 1256 lists acceptance and plan-acceptance adverse answers and out-of-scope NO-PASS findings.
5. `I1` therefore waits on no route, permanently. The sketch's T2 shows "OPEN, NO ROUTE".

§13.7 and workplan §7.3/§7.10 instead make an in-scope NO-PASS start the next iteration mechanically. That requires `I1` to be ready, which §10.4 forbids. An implementer must choose between the two statements: §10.4 strands the item, §13.7 re-dispatches without an output move.

**Siblings of (c):**
- the implementer's own re-attestation (§4.1, a new author choice) returns `PARTIAL`/`INFEASIBLE`/`BLOCKED`, because the old candidate no longer satisfies the changed context. A re-attestation cannot change content ("a content change is a new iteration"), and a new iteration needs readiness;
- a `REFUSED` item-level review of a partitioned item whose parts' outputs never moved (§13.7);
- the permanent form of (a).

**(d) Plain overtake.**

1. Admission `n` integrates `X`, then loses its compare-and-swap to a foreign push. No fence is involved. `pub(n) = OVERTAKEN`.
2. The absorption moved `X`'s outputs after the latest integration (an `OVERTAKEN` integration counts, §8.3 step 7). So the item is ready as drift.
3. Line 1256 also derives `COORDINATE(plan)` for the `OVERTAKEN` admission.
4. The §10.4 wait applies only "while … an `OVERTAKEN` admission awaits its human decision". A plain overtake has no human decision (§22.3, §15.4). So both routes are ready.

This is the second bullet of f185036 B1(b), carried unrepaired, and its discriminator ("An overtake: the item does not run drift and `COORDINATE(plan)` together") is unanswered. It is the least severe sibling, since both routes lead to a new enactment, but it is still two routes for one staleness.

**(e) Investigator item obligations.**

1. A findings-only `INVESTIGATE` item is discharged on its review. §13.3 requires a `REVIEW` obligation, and a records-only result is never integrated, so `REVIEW(X)` stays derived (line 1258).
2. A later change to a file the investigator or reviewer read makes the review non-current, and the `INVESTIGATE` obligation reopens, because discharge is current-state for every obligation.
3. §10.4's readiness limit covers only "A reopened implementer obligation". The investigator obligation therefore falls to §10.3's generic readiness and is ready, so it is re-dispatched on a read-only change. That is exactly what SD-37 removes.
4. At the same time `REVALIDATE` of its review is derived and answerable: two routes.
5. The stale investigator task result has no holder. §4.1 names "its implementer", and §12.3's investigator template holds no `REVALIDATE`.

The same applies to an `INVESTIGATE` item that integrates findings into its homes.

**(f) Joint-invariant review after an output change outside the invariant's scope.**

1. `k1` changes `u ∈ scope(i)` and `w ∉ scope(i)`. `JOINT_INVARIANT(i, k1)` is answered `PASS` by `rJ1`, whose minimum carries output entries on all of `Δ(X_k1)`, `w` included (line 570).
2. A later change `k2` edits only `w`. It touches no unit of `i`'s scope, so no `JOINT_INVARIANT(i, k2)` is derived, and by the row (line 1271) `JOINT_INVARIANT(i, k1)` stays derived.
3. `rJ1` is non-current through `w`. One of two things follows:
   - `REVALIDATE(rJ1)` is derived and stranded, since its answer needs `(w, rev(w, C_k1))`;
   - or, if the exclusion is read as covering it, `JOINT_INVARIANT(i, k1)` is `OPEN` with no route.
4. §10.4's general sentence ("derived only while what it judged can still be current") would instead end it, which retires work silently if `JOINT_INVARIANT(i, k1)` was still unanswered: `k1`'s in-scope change is then never reviewed against `i`, since no successor exists.

The row and the sentence disagree. The model's `ji_scope_change` event covers only in-scope changes. The high-consequence review ("ending likewise", line 1226) has the same shape for a transformation that changes units both on and off the marked surface.

**Violated owner text.**

- **The architecture owner** (`aaeaf8b:source/shared/references/architecture-and-design.md`, "D3 formal-contract discipline"): "When an architectural concept carries normative meaning, define it before dependent invariants use it: … lifecycle states and transitions". "Moved", "its review" and the item's set of relied-on reviews are used by the single-route and no-stranded invariants without being defined over several enactments.
- **The D3 entry contract** (`source/roles/software-design/SKILL.md`), item 4: prefer "one authoritative representation/state". Item 6: "state what reopens D3 versus what remains equivalent D4 reconciliation". Here one staleness is computed in four places, and the adverse and investigator exits are unstated.
- **The workflow owner** (`workflow-and-workplans.md`): "close each material impact item as resolved, preserved-with-reason, or unavailable/blocking". (a), (c) and (f) leave items in none of these states, and (b)'s variant closes one silently.
- **The reviewed workplan, §7.3:** "a NO-PASS leaves the obligation undischarged and the next task is a new iteration". **§7.10:** "a NO-PASS whose findings all lie within the item's write scope and obligations, starts the next implementer iteration mechanically (R0)". (c) contradicts both.
- **The Manual's own claims.** §10.3's invariant is quoted above. §10.4 says "none waits on a revalidation that no admissible answer can satisfy". The handoff's confirmation questions (one route, no wait on an unanswerable route, no discharge on a review of moved outputs) are the stated purpose of SD-37's realization.

**Minimum repair direction.** This is a recurrence, so the options are below. The first is recommended and is mostly definitional. Additions are marked.

1. **Recommended: one key per item obligation, stated once in §10.4 and read by §4.1, §10.2 and §13.7.**
   - Define `out(o)`: the units changed by `o`'s integrated enactments, with their revisions just after `o`'s latest integration. Define "moved" as a state condition: some unit of `out(o)` has `cur ≠` that revision. This closes the revert and empty-transformation readings.
   - After integration, `o` relies only on its latest integrated enactment's review. Earlier enactments' reviews are history and are never depended on, so they derive no `REVALIDATE`. This closes (a).
   - **[adds one mechanical-minimum entry]** The review of a re-dispatched enactment carries `content` on every unit of `out(o)`, so that review alone is what discharge reads. This closes (b).
   - Readiness and the exclusion both read "moved" over `out(o)`.
   - The rule applies to every item obligation with a review, investigator obligations included. Name the holder of a stale investigator result's `REVALIDATE`. This closes (e).
   - A plain overtake gets one route: either drift with no `COORDINATE(plan)` trigger (removes a trigger row) or a wait on `COORDINATE(plan)`. This closes (d).
   - Narrow the `JOINT_INVARIANT` (and high-consequence) review minimum to output entries on `Δ(X) ∩ scope(i)` (respectively the surface), plus the ctx entries on the scope. This removes entries, so the row's end condition equals what the answer judged. This closes (f).
2. **For (c), stakeholder-visible:**
   - **(i)** An adverse answer, or a non-`COMPLETE` re-attestation, on the revalidation of an integrated item's review is a NO-PASS iteration under §13.7: the next iteration within budget and scope, otherwise `COORDINATE(plan)`. This keeps workplan §7.3/§7.10. State it as the one non-drift re-dispatch.
   - **(ii)** To keep SD-37's "re-dispatch only when outputs moved" literally, route that adverse answer to `COORDINATE(plan)`. **[adds one trigger clause to an existing kind]**. This narrows reviewed §7.10 for integrated items and needs listing as a refinement.
   - The same choice covers a `REFUSED` item-level review.
3. **Stakeholder alternative (removes mechanism, partly reverses SD-37):** after integration every reopened item obligation is re-dispatched, and no item review's `REVALIDATE` is derived. This is f185036 option 2 without its alternative, and it accepts the read-churn cost. (a)-(c) and (e) vanish because nothing relies on an earlier review. (d) and (f) still need their definitions.

**Required discriminator.** Real owners: Derivation obligation derivation and discharge, then readiness, then Admission steps 6-8.

- **T1:** integrate, output move, drift re-do, then a read-only change. Exactly one review's `REVALIDATE` is derived, and it is answerable.
- **T2:** a read-only change, then an adverse revalidation. `I1` has exactly one ready route: the §13.7 iteration or `COORDINATE(plan)`, as chosen.
- **T3:** a two-unit item, a drift re-doing one unit, then a change to the other. Exactly one route (drift). The item is not discharged before the re-work integrates, whether or not the drift reviewer read the other unit.
- **A plain overtake:** exactly one route.
- **A findings-only `INVESTIGATE` item after a read-only change:** no re-dispatch, and one `REVALIDATE` chain with a named holder for the result.
- **`k1` changing in- and out-of-scope units, then `k2` changing only the out-of-scope unit:** `JOINT_INVARIANT(i, k1)` stays answerable or its answer stays current. It is neither stranded nor retired unanswered.
- **A revert of a moved output while a read also changed:** one route.
- **The diagnostic's routing family** must represent several enactments with their own reviews, adverse revalidation answers, an out-of-scope output change and an investigator item. At present its state collapses every enactment into one `R`. `revalidate_R` always restores currency. `rt_answerable` restates the rule's own answerability.

## Non-blocking findings

### N1 — Step 8's prerequisite-authority exemption names the request's "own records" (f185036 N4, partly closed)

Line 1190 exempts "a request whose own records include the counting acceptance (and every required gate decision) of the D1-D3 revision it integrates". An integration request carries "no new judgment" and only references admitted frame records (§11.5 step 3). Under the literal reading, the exemption never applies to an integration, and §31.6 (Z)'s "accept a real change of `a`" would be refused whenever `a`'s change makes a dependent's evidence fail.

"Counting" is defined for tenure starts (§7.6) and for revision assessments (§10.2), not for a plain revision's prospective acceptance. Say "carries or references a current prospective acceptance in its frame (and every required gate decision)". This is a definition.

### N2 — Step 8 "keeps its value"

Read literally, a request that raises a passing term from `P` to `T` is refused. Write "does not fall (a fall from `T` to `P` counts as failing)". Editorial.

### N3 — A `REFUSED` event-keyed obligation has no derived decision route, and a late adverse answer's effect is implicit

After integration, a `REFUSED` `JOINT_INVARIANT(i, k)`, `SPEC_REVIEW(spec, r)` or high-consequence review stays derived, as SD-37 requires. No trigger derives a decision on it: no `COORDINATE(plan)` row, and no §12.5 standing-plan route for a no-plan one. It is preserved, but it is routed only if its judge also raised a report.

A related ambiguity concerns an adverse answer that arrives from a task already in flight after a successor `JOINT_INVARIANT(i, k')` was derived. It is admitted (never-lost, step 6), but bound to an obligation that has ended. §10.2's "or while `REFUSED`" is a state condition, so it re-derives that obligation as `REFUSED`, which is correct. The text should say so, so that no implementation drops a finding its successor's judge never saw.

### N4 — §31.6 (Z) still tests only the dispatch half of §10.3 (f185036 discriminator, open)

Line 2689 ends "none is dispatched whose every answer Admission must refuse". The second half of §10.3's invariant ("a non-current judgment that a current obligation depends on with neither a ready nor a waiting route") is untested. B1 (a) and (f) are cases of exactly that half.

### N5 — The model's oracle is not independent (DS-001; f185036 N5 carried)

- **The routing family.**
  - I13 calls `rt_answerable`, which encodes the same answerability as the rule.
  - I15's "discharged on a review of outputs that have since moved" reads one `outputs_moved` flag that a re-dispatch resets.
  - There is one review and no adverse revalidation.
  - So every B1 sibling is green by construction.
- **The I8 oracle** still shares the "not superseded" filter (f185036 N5).

§31.3 discloses "it models answer admissibility only as whether the judged content is current". It does not disclose the single-review and passing-only limits.

### N6 — Editorial

- "the routes of its failing terms … and its subjects' own obligations" (line 1319) should name which obligations count as a route for the item (the subjects' `ACCEPT`/`GATE`/evidence obligations), so that the item is not taken to wait on an unrelated obligation.
- §16.3, the brief owner, does not carry the drift brief's content (line 1319 does). Point §16.3 to §10.4.
- "same scope" for the high-consequence review (line 1226) should say "the same marked surface".

## Closure audit

The closure map was used to navigate. I checked its claims for every §21 item the delta or B1 touches against the Manual sections they name. The map's item-7 row claims "re-dispatched as drift only when the outputs of one of its integrated enactments moved …, otherwise waiting on its review's `REVALIDATE`". That claim is the B1 (a)/(b) mismatch: it reads well only for one review.

| Item | Disposition at this candidate |
|---|---|
| 6 (Admission validation order) | step 8 closed as SD-36/SD-37 direct; N1, N2 definitional |
| 7 (obligation rules, readiness, discharge, iteration identity) | **partly open (B1)**: several-enactment routing, adverse revalidation exit, investigator obligations, plain overtake |
| 9 (joint invariants) | partly open (B1 (f)); otherwise closed: `JOINT_INVARIANT(i, k)` ends at a later change in scope (f185036 N2 closed) |
| 24 (budgets, partition) | inherits B1 (c) (§13.7 against §10.4) |
| 1-5, 8, 10-23, 25-27 | no unresolved architectural decision found in this bounded audit; text unchanged since f185036 (sentence diff: only lines 100, 549, 1190, 1226, 1258, 1261, 1270-1271, 1319, 1534, 2112, 2659, 2665, 2766 changed) |

The §16.2 rows are unchanged. §26.4 keeps an explicit replacement, retirement or preserved boundary for every row, and none was found unresolved.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1-R14 | text byte-identical to f185036's and 82d618c's §0.3 rows (only line 100, the R15 row, changed); sound as assessed in the f185036 and 82d618c records; spot-checked R9 ("an answered obligation is never ready again", consistent with SD-37's ends) and R12 (a re-dispatch is a new task and enactment, consistent with §5.2 and §10.4) |
| R15 | sound as the stakeholder-chosen narrowing of reviewed step 8 (evidence regression only), with SD-37's limit on the re-dispatch stated in its row. Its consequences are B1 and N1-N2. The kept author choice that a task result re-attests after integration while its outputs are current (§4.1) is sound in direction (it keeps the review's `REVALIDATE` answerable). It inherits B1 (c) (an adverse re-attestation has no exit) and B1 (e) (no investigator holder) |

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **M** moot (the mechanism it attacked is removed); **D** design/disclosure closure with real-owner execution owed later; **R** retained, disclosed decision or stakeholder option; **P** partly closed; **O** open.

**The f185036 Review, finding by finding:**

| Finding | Disposition |
|---|---|
| B1 (a), stranded event-keyed obligations | **C** for `JOINT_INVARIANT` after an in-scope change, `SPEC_REVIEW` after a move, `REVIEW(X)` after integration, the high-consequence review after a later change on the surface, and the item-level review (lines 1226, 1258, 1270-1271, 1319, 1534); **P**: the same family reappears as B1 (a) (an earlier enactment's review) and B1 (f) (out-of-scope output) |
| B1 (b), duplicate routes | **C** for the read-only change on a once-integrated item (one route, `REVALIDATE`, line 1261) and for the `AUTHOR` triple (the item now waits; in-run re-acceptance and the item's `REVALIDATE` are distinct obligations); **O** for the plain overtake (B1 (d)); new duplicates in B1 (b), (e) |
| B1 (c), `subject(o)` | **C** (union over enactments, line 1319; §31.4 case) |
| N1, accepted drift cost | **C** (§32.3 line 2766 and closure map §5: budget spending, undoing later accepted changes, the read case now waits) |
| N2, redundant joint-invariant re-review | **C** (the earlier obligation ends) |
| N3, drift brief and empty candidate | **C** (line 1319) |
| N4, step 8 exemption | **P** (defined; wording N1 here) |
| N5, I8 oracle | **O**/**R** (carried, N5 here) |
| N6, editorial | R15 row wording **C**; `T`→`P` **C** (wording N2 here); `late(n)` joint-invariant **C** (line 1271); §22.2 duplicate discharge **C** (line 2112) |
| f185036 discriminators | met except the overtake, the (Z) second clause (N4) and the no-op/T3 cases over several enactments |

**Obligation-lifecycle family (095ce55 through c4e8de7, and 82d618c B1).** SD-36 removed R15's latch, lines, lowered and waiting states, retirement, `RESOLVED_BY` and the lifecycle model family. A residue search of the Manual, closure map and model for each found none. "Latch" occurs only in §6.4's unrelated start latch and in the §32.3 disclosure of "failures latched by transient foreign pushes".

| Prior record | Disposition at this candidate |
|---|---|
| C4E8DE7 B1 (a)-(c), N1-N6 | **M** (mechanism removed); its N6 `late(n)` bullet **C** |
| 494C810 B1 (a)-(c), N1-N6 | B1 and N1-N4 **M**; N5, N6 **C** as in the f185036 record |
| 3876473 B1 (a)-(d), N1-N5 | **M** |
| 3940DBC B1 (a)-(d), N1-N5 | **M**; N4 **R** (model limits, N5 here); N5's warning about `REVALIDATE` of an integrated review is now answered by line 1261, except B1 (a) |
| C77447B B1 (a)-(d), N1-N6 | B1, N1, N2 **M**; N3 **C** with its cost removed by SD-37; N4, N6 **C**; N5 **R** |
| 095CE55 B1, N1-N7 | B1 **M**; N1 **C** (`SPEC_REVIEW(spec, r)`, now with an end); N2 **R** (N5 here); N3 **C**; N4 **M**; N5 **C**; N6 **C** by SD-37 (read-based re-dispatch removed for implementer items; investigators B1 (e)); N7 **R** |
| 82D618C B1 and siblings, N1-N7 | B1 refusals **C** (step 8); sibling (d) **P** (N1 here); sibling (e) **C** except B1 (a), (f); N1-N3, N5-N6 **C**; N4 **R**; N7 **C**/**R** |
| EDABD81 B1-B2, N1-N7 | **C**/**R** as in the f185036 record; N5 **P** (N4 here) |

**Judgment-disagreement family (§5.10 and the sections closure map §7 maps to it: §3.4, §5.3, §5.5, §5.10, §6.7, §8.3, §10.2-§10.4).** The §5.10 text is byte-identical to f185036's. Since 82d618c its only changes are the relation-targeted wording in (a) and "not superseded" in (f)/(g)8 (lines 822, 878, 892), which the f185036 record judged restrictive-neutral; I agree. The §10.2-§10.4 changes touch obligations only, not reach, relief, supersession or independence.

| Prior records | Disposition |
|---|---|
| 653E88C, D94A293 (different family), 913DB8F, 5895687, 4C52205 (SC-1 **R**), both E548472 (same-family SC-1 **R**; different-family N1-N3 **R**/**C**), D6734C4, 83A82DF, 0D2B35E, 34803DF, BF23372, A6ED164 | blockers **C**; N items **C/R/D** as the 82d618c and f185036 records give them; the plan-policy items **R** (stakeholder-chosen SD-30 to SD-35); the model's mutations for each are caught (below) |
| 6B986DE, 29DA56E, 51070E5, 9E5A763, 051CCE3, 63DDF91, F03B15E, 61CD09B | independence (`authors`, `nonind`), adjudication root and class, exact supersession targets, relief: **C**, unchanged |
| 362AF9F, F22B4DC, both B46C250, F7419D5, 575DC78 | acting rule, enactment unit, `rid`, gate minimum, one enactment one integration: **C**; drift re-dispatch adds enactments of one obligation consistently with R12 and §5.2, except that B1 (a)/(b) are about how those enactments' reviews are read |

**Matching, content-identity, partition and D1-D3 change-rule families.** §6 text, §1.5, §17.5 and §10.2's revision-run paragraphs are unchanged since f185036 and 82d618c.

| Prior records | Disposition |
|---|---|
| 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC, 3540D98 | **C** |
| 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363, CC005DB, C6DA678, B595F2C, 6FF4ED1 | run-keyed counting, event-keyed run, `tgt` read by every consumer, frozen matching, effect-keyed write set: **C** for each stated blocker; N items as in the 82d618c record |
| Phase B closures and N1-N4 | §6 unchanged; Phase B N2 (polarity and `link⁻` anchoring under a `P`, blocked, revoked or loss-withheld completeness judgment: (2)/(4) stay in, only (1)/(3) narrow) **C/D**; support cycles (§5.6) and corrupt prefixes (§5.7) fail closed **C**; N1 **R**; N3 **R/D**; N4 **R** |

I did not replay the pre-f185036 records item by item. For text unchanged since 82d618c, their dispositions are carried from the 82d618c and f185036 records. The confirmation of unchanged text rests on the sentence-level diff.

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Two sequential items editing one leaf unit | held: integrates; first item drifts; `REVIEW(X1)` not derived after integration; no `REVALIDATE(r0)` |
| Read-only or governing change to a once-integrated item | held: one route, `REVALIDATE`, answerable |
| Output move, drift re-do, then read-only change | **B1 (a)** |
| Two-unit item, partial drift, then the other unit moved | **B1 (b)** |
| Revert of a moved output while a read also changed | **B1 (b)** sub-variant |
| Read-only change, adverse revalidation | **B1 (c)** |
| Adverse or non-`COMPLETE` re-attestation | **B1 (c)** |
| `REFUSED` item-level review | **B1 (c)** sibling |
| Plain overtake | **B1 (d)** |
| Fence, then keep the fence | held: waits, then `COORDINATE(plan)` |
| Findings-only `INVESTIGATE` after a read change | **B1 (e)** |
| Two in-scope changes `k1`, `k2` to a joint invariant | held: `JOINT_INVARIANT(i, k1)` ends; `REFUSED` stays |
| `k1` in- and out-of-scope, `k2` out-of-scope only | **B1 (f)** |
| Two revisions of an evidence specification; revert to `r1` | held: the first ends; a revert re-derives the same identity |
| Absorbed change breaking evidence, then a no-op or other-subject re-dispatch | held (union `subject(o)`) |
| Second `AUTHOR` revision of a D2 subject | held: integrates; first drifts when its outputs moved |
| D1 change governing an accepted D2 subject (§31.6 (Z)) | held for routes (in-run re-acceptance; the `AUTHOR` item waits on `REVALIDATE`); step 8 exemption wording N1 |
| A request making another obligation's passing evidence fail, or `T`→`P` | refused, held |
| `JOINT_INVARIANT(i, k1)` adverse answer arriving after `JOINT_INVARIANT(i, k2)` is derived | held under the state reading of "while `REFUSED`" (N3) |
| Composition, chain and union reach; plan closed form; review re-identification; gate basis | held (unchanged; model green) |

## Minimum architecture and capability transfer

The delta adds no primitive, component, record kind, mode or persistent surface. It adds trigger end conditions (definitions), one readiness condition (SD-37's, stakeholder-chosen) and the task-result post-integration route (an author choice). B1's recommended repair defines one key and removes entries from the joint-invariant review minimum. It adds one minimum entry for a re-dispatched enactment's review, marked. Withdrawing R15 and limiting drift drop no owner-required capability once B1 (c) restores the reviewed NO-PASS iteration (workplan §7.3/§7.10) for integrated items.

Architecture 1.6.0 (blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41` (`git diff --quiet` succeeds). The version-bound Core and frozen profiles are therefore preserved (PEM PC-001).

**PEM.** Activated: this is mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` resolve to `af0455753e20ee54a969c844872e29e270007211`. The PEM blob there and at the candidate is `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no overlay. The repository validator, run in the clone, reports "PEM schema 1 valid: 5 families, 0 notices". Task-local HAS:

- **PC-001:** APPLICABLE (preserved).
- **DS-001:** APPLICABLE (a green routing family coexists with B1).
- **SP-001:** evidence-only (one owner per rule: B1 is four places computing one staleness).
- **SP-002, FF-001:** not material.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 keeps G1 document checks apart from G2-G4 runtime evidence and claims no execution it lacks. §31.4's new positive cases (line 2665) are real discriminators for the single-enactment case. They contain no case with two integrated enactments, an adverse revalidation, an investigator item, an out-of-scope output change or a plain overtake, so an implementation of the literal rules passes them while failing B1. §31.6 (Z) still tests only the dispatch half of §10.3 (N4).

The routing family checks I13-I17 as properties, but over a state that has one review whose revalidation always passes, with answerability restated by `rt_answerable` (N5). A green run therefore coexists with every B1 sibling. The handoff asks whether I13-I17 and `rt_answerable` are the right ones:

- **I13-I17** are the right properties.
- **The scenario space** is too small: it needs per-enactment reviews, adverse answers, out-of-scope changes, investigator items and the overtake.
- **`rt_answerable`** should be derived from the entries each answer's minimum carries (§4.3), not from a flag per route.

## Doctrine-realization map and O1

§29 maps all seven entrypoints. The D4 row's "reconcile every obligation … no collateral regression (§8.3 step 8)" is consistent with step 8. Its "reconcile every obligation" is what B1 leaves open after integration, and the same repair closes it. No other map claim depends on the delta. O1 (§0.5) is unchanged and within the requested deliverable. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

**Verified:**

- the candidate blobs: Manual `78a76025…`, closure map `69f986e0…`, workplan `91bde236…`, Architecture 1.6.0 `39e6de72…`;
- the full clone (`git rev-parse --is-shallow-repository` is `false`) and the governing refs from `PROTOCOL-RELEASE-STATE.yaml`;
- the owner text at `aaeaf8b`: `source/roles/software-design/SKILL.md`, `architecture-and-design.md` ("D3 formal-contract discipline", simplification trigger), `workflow-and-workplans.md` (impact closure), `convergence-and-cycle-economy.md` ("Review strategy after recurrence", family-level sibling discovery);
- the reviewed workplan §7.1-§7.4, §7.8, §7.10, §15.3 and §21 at the candidate;
- every sentence of `git diff f185036..8f4e75d` and `git diff 82d618c..8f4e75d` for the Manual, and the closure map and stakeholder record deltas (SD-37 quoted from item 33);
- the post-integration sweep described above, by hand, and the three central trajectories with a scratch sketch (`$TMPDIR/ssds80-manual-review-8f4e75d/scripts/multi_enactment.py`) that encodes §10.2's `REVALIDATE` row and §10.4's readiness literally. The sketch was written by this reviewer and shares my reading.

**Checks run at the candidate snapshot:**

- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- `git diff --check f185036..8f4e75d`: clean.
- `git diff --stat fad3ee41 bf233728`: 73 files, 23269 insertions, 1 deletion, none under `source/`, `dist/` or `orchestrator/docs/architecture.md`.
- `git diff --quiet fad3ee41 8f4e75d -- orchestrator/docs/architecture.md source dist`: unchanged.
- `python3 -I qualification/ssds80/judgment_disagreement_model_check.py --mutations`, run as its six families and all mutations in parallel by importing the module, as `main()` does (results below).

**Could not verify:**

- any runtime behavior (none exists; G2-G4);
- whether the author intends "its review" to mean the latest enactment's review, since the text is silent;
- earlier families beyond the unchanged-text argument and the spot checks named.

### Diagnostic model run

The model was run from the snapshot with `python3 -I`, through a process pool: each of the six families unmutated, and each mutation re-running only the families it names.

- **Routing family:** 4370 scenarios (every sequence of up to three distinct events from 17), no invariant failure. All eight routing mutations are caught:
  - `review_after_integration`, `ji_never_ends` and `spec_never_ends` by I13;
  - `both_routes` by I13 and I14;
  - `redispatch_on_reads` and `revalidate_after_move` by I15;
  - `subject_last_enactment` by I17;
  - `refused_retired` by I16.
- **Other families:** all five other families report no invariant failure: transformation-review/acceptance/gate (1,856,368 cases), equivalence-chain (299,760), completeness-cover (37,600), plan-coverage (205,800) and gate-basis (1,000). All 42 entries of `MUTATIONS` are caught, each by at least one of I1/I3, I2, I4, I5, I7, I8, I9, I10 or I13-I17. Examples: `plan_revert_exemption` by I1/I3 and I8; `plan_supersession_current_only` by I4; `frame_acts_everywhere` by I5; `gate_basis_record_all` by I1/I3, I9 and I10; `eq_authors_to_side_only` by I1/I3, I7 and I8.

A green run shows only that the written rules satisfy the oracle on the modelled cases. It is not adequacy evidence, and it says nothing about B1 (N5).

## Scientific checks

This task reviews D3 authority for software that mediates scientific evidence. Material findings: B1 and N1-N6 above. I produced, ran or reviewed no realized scientific results: the null envelope is that no data, solver output or evidence assessment was read or produced. The diagnostic model and my sketch are logic enumerations, not scientific results.

I evaluated more than one variant:

- two readings of "moved" (event and state), by whether each gives one route;
- two readings of "depends on" with several non-current reviews (every review, latest only), by whether each strands;
- two readings of the post-integration NO-PASS (§10.4 and §13.7), by whether each leaves a route without contradicting SD-37;
- three repair options, by whether they remove mechanism and whether they retire an unseen finding.

I relied on no accepted D1/D2 authority for a consequential judgment, so no tension search was needed. Unanswered parts are listed under "could not verify".

## Common-mode note

I am of the Claude family, the same as the Manual's author and the same-family reviewers from e2154ac to f185036. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. I was engaged as a fresh-context sub-agent launched by the authoring session.

Fresh context does not make me independent. I share the corpus, the inherited workplan framing, the prior Review records (read as hypotheses, including the f185036 record whose option 1 SD-37 adopted), the model family's reading habits and the toolchain. My sketch is not independent of my own reading. A different-family confirmation, especially of B1 (c) and of the claim that nothing else regressed, would reduce that common mode.

## D4 statement

This Review authorizes no D4 work and accepts no architecture, product scope or default value. NO-PASS is technical evidence for G1 only. B1 is routed to the Manual's author as the D3 owner of workplan §21 item 7. The choice between B1 option 2 (i) and (ii), and option 3 as an alternative, is the stakeholder's.
