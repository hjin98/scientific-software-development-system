# Independent D3 Review — SSDS 8 Architecture Manual, candidate f185036 (SD-36 confirmation)

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          f18503688765e6a5693306f84eb8ee880d4d54c5
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g)), with the
                        SD-36 confirmation questions first; technical evidence for G1 only
    MANUAL blob:        fce078298032832f9dacadf23905cb2f10a2b72b (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   69c848012184dd7ccd7a942ba196aa6f719d8004 (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family c4e8de7
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; diffs c4e8de7..f185036 and
                        82d618c..f185036 read paragraph by paragraph; residue search for every R15 term;
                        an answer-or-route sweep over every obligation kind of §10.2 after a later admitted
                        change, a ctx-only change, an absorbed change, a fence and an overtaking push;
                        a dependence check of each correction kept from candidates 46-51 against the
                        withdrawn latch; family-level recheck of earlier families on the unchanged text;
                        diagnostic model run in full (all families and mutations, in parallel);
                        structural checks of handoff §3 step 9
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched
                        by the authoring session; did not author the candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-f185036/snap`. The later commit adding the handoff (`df80ae56`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. SD-36 (stakeholder record item 32) fixes discharge as the reviewed workplan §7.4 current-state predicate and narrows Admission step 8. It says nothing about when an obligation is derived. The defect below lies in the Manual's own obligation triggers and routes (workplan §21 item 7), which the Manual can repair without reversing SD-36. One disclosed cost (N1) is larger than SD-36's wording says, and the stakeholder should see it.

## Verdict

**NO-PASS.** One blocker, in the obligation-lifecycle family (the ninth round; earliest owner Manual §10.2-§10.4, workplan §21 item 7):

- **B1**, the post-integration lifecycle under current-state discharge. The withdrawal of R15 restored the 82d618c text and kept corrections from candidates 46-51 that presuppose a latched end. Three of those presuppositions now fail:
  - **(a) Stranded judgment obligations.** Obligations keyed on a past event (`JOINT_INVARIANT(i, k)`, `SPEC_REVIEW(spec, r)`, the high-consequence integrated-result review, a partitioned item's item-level review, and `REVIEW(X)` under its literal trigger) are derived forever. Once later content moves what they judged, their passing answer is non-current, and the `REVALIDATE` it derives has no admissible answer and no restoring route. §10.3 itself names this state a defect. §31.4 claims it cannot arise.
  - **(b) Duplicate routes.** One post-integration staleness derives both `REVALIDATE` of the review (reviewer) and the drift re-dispatch of the item obligation (implementer). No rule says which one goes first. An overtaking foreign push derives both drift and `COORDINATE(plan)`.
  - **(c) An ambiguous `subject(o)`.** It is defined over "its enactment", but an obligation now has several enactments. Under the natural reading, a re-dispatch that changes nothing, or changes another subject, discharges an item whose required evidence still fails.

What SD-36 asked for is otherwise realized. No latch, lowered state, line, retirement, `RESOLVED_BY`, `REVALIDATE_OVERTAKEN` or lifecycle-family residue remains in the Manual, the closure map or the diagnostic. Step 8 refuses exactly a request that makes another obligation's passing `ev` or `qual` fail. The three 82d618c B1 cases (a later item editing an earlier item's outputs, a second change in a joint invariant's scope, a second `AUTHOR` revision) are no longer refused, so they integrate. The drift re-dispatch of implementer obligations is stated in §0.3, §4.1, §8.3 step 8, §10.4, §13.7, §31.4, §32.3 and the closure map. The corrections kept from candidates 46-51 that answer 82d618c N1-N7 hold, and they are independent of R15. B1 comes from the others, which are not. The diagnostic model is green on all five families and catches every mutation (see "Diagnostic model run"). It has no obligations, so it cannot see B1.

## Blockers

### B1 — After the latch's withdrawal, enacted obligations have no current-state end, and one staleness has several unordered routes

**Family:** the obligation lifecycle after integration (095ce55 through c4e8de7, 82d618c B1 sibling (e)). It is a non-local recurrence. Its shared cause is drift class "two places computing one thing": §10.4 now computes discharge from current state, while the triggers in §10.2, the route list in §4.1/§10.3 and the `subject(o)` sentence still describe a lifecycle in which an enactment's work is fixed after integration. That held only under R15. **Earliest owner:** Manual §10.2 (triggers), §10.3 (routes, R9 "never ready again"), §10.4 (drift, `subject(o)`), deciding workplan §21 item 7; workplan §7.1 ("a judgment no longer current" as a derived obligation) and §7.4 are restated faithfully. **Status:** open, material.

**Exact rules at the candidate.**

- §10.2 line 1258: `REVIEW(X)` is triggered by "a task result whose conformance is `CLEAN`". §14.1 makes conformance "a pure function of the contract at the task's basis, the base and candidate trees, the result record and the observations recorded for that exact candidate", so it stays `CLEAN` after integration. Line 1270: `SPEC_REVIEW(spec, r)` is triggered by "a change of an evidence specification to revision `r` (each change its own obligation)". Line 1271: `JOINT_INVARIANT(i, k)` by "an admitted change touching a joint invariant's scope". §9.2 (line 1226) derives "the same integrated-result review for every change" to a high-consequence surface. None of these triggers names an end.
- §10.3 (line 1299, R9): an answered judgment obligation "is never ready again … A passing answer that later stops being current derives `REVALIDATE`, a separate obligation". §10.2 line 1261: `REVALIDATE(x)` is derived for an acting non-current `x` that "a current obligation depends on … it ends when `x` is current again, superseded, or no longer depended on".
- §4.3 line 570: `REVIEW` on `X` carries "frame-role `content` on every unit of `Δ(X)` (before-image and output)". A review answering `JOINT_INVARIANT(i, k)` also carries ctx `content` on every unit of `i`'s scope. §7.3: after integration, an output entry has "ordinary currency in the admitted state". An entry `(u, r)` with `u ∈ Δ(X)` and `r` neither the before-image nor the output revision is "never" satisfied.
- §10.3 line 1293: "where an entry of that minimum cannot hold, the obligation is shown as waiting on that entry and the route that restores it is derived instead (§4.1: a wider closure, `REALIZE`/`RERUN`/`READING`, `REVALIDATE` (or, for a stale task result, `COORDINATE(plan)`), `REVIEW(s, r)`). A ready obligation whose every answer Admission must refuse is a defect, and so is a non-current judgment that a current obligation depends on with neither a ready nor a waiting route; §31.6 (Z) tests for both." The only class that waits by design is a kind of `ADJUDICATE_DISAGREEMENT`.
- §10.4 line 1319: "Discharge is not latched (SD-36) … For an item obligation, `subject(o)` in the predicate above is each subject its enactment changes … a later admitted request that changes content an obligation's judgments read, and an absorbed foreign change, can reopen it, and then a discharged implementer obligation is ready again, as drift to repair (§8.6). Its re-dispatch is a new task, so a new enactment … While a fence or an `OVERTAKEN` admission awaits its human decision (§22.3), its item obligation waits".
- §31.4 line 2665: "… reopens and is re-dispatched as drift …, with no `REVALIDATE` stranded; … two successive changes in a joint invariant's scope both integrate, each with its own `JOINT_INVARIANT` review, and the first's review, made non-current, derives `REVALIDATE` for its reviewer (§10.2), never a stranded obligation". §32.3 line 2766: "a joint-invariant or specification review of an earlier change reopens the same way when later content makes it non-current".

**(a) Decisive trajectory: a joint invariant, two changes to one file.**

1. Joint invariant `i` has a scope containing leaf `u`. Change `k1` (transformation `X1`) edits `u` to `rev(u, C1)`. `JOINT_INVARIANT(i, k1)` is derived. The reviewer records `rJ1` (`PASS` on `X1` against `i`). Its basis is output `content (u, rev(u, C1))` plus ctx `content` on the scope. The obligation is discharged.
2. A later item's change `k2` edits `u` again and keeps every passing `ev`/`qual`. Step 8 admits it, as SD-36 requires. `JOINT_INVARIANT(i, k2)` is derived and answerable.
3. In `D_{k2}`, `rJ1`'s output entry fails for good: `cur(u) = rev(u, C2)`. `JOINT_INVARIANT(i, k1)` is `OPEN`, answered, so never ready again (R9). It depends on `rJ1`, since no other judgment satisfies its term, so `REVALIDATE(rJ1)` is derived.
4. The only answer to `REVALIDATE(rJ1)` is a `REVIEW` of `X1`. Its mechanical minimum needs the output entry `(u, rev(u, C1))`, which no state without a revert satisfies. An entry `(u, cur(u))` has role "never". A supersession of `rJ1` is a support-tier record and fails step 6 the same way. The owner's adverse record, which is exempt from step 6, would have to falsely reject `k1`.
5. None of the §10.3 routes restores an output entry. Nothing ends the trigger of `JOINT_INVARIANT(i, k1)`, so `rJ1` is "depended on" forever. The result is a non-current judgment that a current obligation depends on, with neither a ready nor a waiting route: §10.3's defect, permanently shown as open work. Every further change to `u` adds another one.

**Siblings of (a):**

- **`SPEC_REVIEW(spec, r1)`, then a change to `r2`.** The review judged `r1`. After the change, `cur(spec) = r2`, so the review is non-current, and its `REVALIDATE` needs `content (spec, r1)`. This is stranded on every second change of every evidence specification. It is certain under any reading of the review's target.
- **The high-consequence integrated-result review (§9.2)** behaves exactly as (a).
- **A partitioned item's item-level review (§13.7)**, after any later change to a part's outputs, is stranded the same way. Its target and obligation identity are also unstated.
- **`REVIEW(X1)` after `I2` edits `X1`'s output `u`.** Under the literal trigger it stays derived, `OPEN` and answered, and its `REVALIDATE(r1)` is stranded. The same `REVALIDATE(r1)` is also derived for `IMPLEMENT(I1)` until the drift re-dispatch integrates. It is then shown "waiting on" `(u, rev(u, C1))`, an entry nothing restores. The real exit is the re-dispatch, which §10.3 does not list. A charitable implementer could stop deriving `REVIEW(X)` once `X` integrates, but no text says so. §31.4's "no `REVALIDATE` stranded" holds only under that unwritten reading.
- **Control, held.** When `k2` touches only other scope units, `rJ1`'s outputs still hold, and a fresh review of `X1` with current context is admissible and ends `REVALIDATE(rJ1)`. This is the only case §31.4 describes, and it is then a duplicate of `JOINT_INVARIANT(i, k2)`'s review of the same integrated state (cost, N2).

**(b) Duplicate routes for one staleness.**

- **A ctx-only change.** A later admitted item edits a file `g` that `I1`'s reviewer read. Nothing `I1` produced changes. `r1` is non-current through its ctx entry on `g`. Two routes follow, and both are ready. `REVALIDATE(r1)` goes to a reviewer, and its answer is admissible because `X1`'s outputs still hold. `IMPLEMENT(I1)` is "ready again, as drift to repair" and goes to an implementer. Neither waits for the other.
  - If the reviewer lands first, the implementer's in-flight result is "bound to an already-discharged obligation … routed to revalidation" (§8.3 step 7).
  - If the implementer lands first with a candidate, it is a new enactment that re-does work nothing required.
  - For an `AUTHOR` item whose reviser read a D1 unit `a`, a change of `a` derives three routes at once: in-run re-acceptance of `b` (§31.6 (Z)), `REVALIDATE` of the review, and a drift re-dispatch of the D2 author. If the re-dispatch revises `b`, it starts a new revision run that competes with the in-run re-acceptance (Z) is designed around.
- **An overtaking foreign push** (compare-and-swap lost, no fence). In `D_{k+1}`, `X`'s outputs are absent, so the item obligation is `OPEN` and ready as drift. §10.2 also derives `COORDINATE(plan)` for the `OVERTAKEN` admission, whose outcomes include re-application. §10.4's "waits" applies only while an admission "awaits its human decision (§22.3)". §22.3 raises human attention only for a fencing absorption, so for a plain overtake both routes run. If the waiting clause is read as also covering the principal's decision, the text does not say so.

**(c) `subject(o)` over several enactments.** An item obligation is now enacted repeatedly: its integration, then each drift re-dispatch, "a new task, so a new enactment". "Each subject its enactment changes" does not say which enactment. Under the natural reading (the enactment being claimed), the predicate's `ev`, `qual` and `status1` terms range only over the latest candidate's subjects. Trajectory:

1. An absorbed foreign change breaks `I1`'s required evidence `e` on subject `s0`.
2. `I1` reopens and is re-dispatched.
3. The re-dispatched candidate changes nothing, or only a unit of another subject `s1`.
4. Step 7 evaluates `discharged(IMPLEMENT(I1))` with `subject(o) = ∅` or `{s1}`, so `e` on `s0` is not read and `I1` is discharged while `e` fails.

§10.4's own rule ("A missing required check is an undischarged obligation; no rule turns it into a pass") and S4 ("stale passing evidence never confirms") are then violated at the item, though `s0` itself stays invalid. The sentence was added under R15, which had one enactment per obligation.

**Violated owner text.**

- The architecture owner (`aaeaf8b:source/shared/references/architecture-and-design.md`, "D3 formal-contract discipline"): "When an architectural concept carries normative meaning, define it before dependent invariants use it: … lifecycle states and transitions". The §10.3 no-stranded invariant uses a lifecycle the triggers do not define.
- The same owner: the simplification trigger names "lifecycle states created mainly by solution machinery". (a) and (c) are such states, left behind when the latch was removed.
- The D3 entry contract item 6 (`source/roles/software-design/SKILL.md`): "state what reopens D3 versus what remains equivalent D4 reconciliation". The Manual states that the item reopens but not what its judgment obligations become.
- The workflow owner (`workflow-and-workplans.md`, "Evidence, stages, and impact closure"): "close each material impact item as resolved, preserved-with-reason, or unavailable/blocking". A stranded obligation is none of these.
- The Manual's own §10.3 invariant and §31.4/§32.3 claims contradict its §10.2-§10.4 rules. An implementer must choose between implementing the triggers as written, which fails (a) and the §31.4 discriminator, and inventing an end the Manual does not state.

**Minimum repair direction (options, because this is a recurrence; the first two remove mechanism).**

1. **Recommended: give event-keyed judgment obligations a current-state end. This is a trigger definition, not a latch.**
   - A judgment obligation keyed on a past event is derived only while what it judged can still be current.
   - `REVIEW(X)` and conformance: while `X` is unintegrated. After integration, the item obligation's discharge reads the review directly, and a non-current review of an integrated `X` derives no `REVALIDATE`, symmetric with §4.1's kept task-result rule: "after integration its staleness reaches the item obligation through current-state discharge".
   - `SPEC_REVIEW(spec, r)`: while `cur(spec) = r`.
   - `JOINT_INVARIANT(i, k)`, the high-consequence review and the item-level review: while no later admitted change in the same scope has derived its own obligation of that kind. The later obligation judges the newer integrated state.
   - Objections are not retired by this: an obligation that is `REFUSED` (a standing adverse answer) stays derived, so no finding is retired by a successor its judge never saw (494c810 B1, c4e8de7 B1). This keeps "appear and disappear as derivation changes" (§10.1, workplan §7.1) and adds no state.
2. **For (b): make the drift re-dispatch the only post-integration route for an item's own review and task result** (option 1's first clause already does this). Disclose that a change to anything the implementer or reviewer read then re-dispatches the implementer (N1).
   - **Stakeholder alternative:** re-dispatch only when the enactment's output content moved, which is SD-36's own wording, and otherwise let the item obligation wait on `REVALIDATE` of its review. This adds one readiness condition, so it is marked as mechanism, but it cuts the churn of reads.
   - For an overtake, state that the item obligation waits on `COORDINATE(plan)`.
3. **For (c), a definition:** `subject(o)` is the union of the subjects changed by every integrated enactment of `o`, so a re-dispatch never narrows what the obligation's terms read.
4. **Disclosure only (not recommended):** list the stranded post-integration states in §10.3 as a second "waits by design" class. This leaves permanent open entries and makes (Z) fail by design.

**Required discriminator** (real owners: Derivation obligation derivation and discharge → readiness → Admission steps 6-8):

- `k1`, `k2` both editing `u` in a joint invariant's scope: both integrate, and afterwards no `JOINT_INVARIANT(i, k1)` is open and no `REVALIDATE(rJ1)` is derived; `JOINT_INVARIANT(i, k2)` is derived and answerable.
- The same with an adverse `rJ1`: the finding stays `REFUSED`/routed and is not retired.
- `SPEC_REVIEW(spec, r1)` then a change to `r2`: no open obligation for `r1`.
- Two sequential items editing `u`: no open `REVIEW(X1)` and no stranded `REVALIDATE(r1)`.
- A ctx-only change: exactly one route is ready for `I1`.
- An overtake: the item does not run drift and `COORDINATE(plan)` together.
- An absorbed change breaking `I1`'s evidence, then a no-op re-dispatch: `I1` stays `OPEN` until `e` passes on `s0`.
- §31.6 (Z) must also test its second clause ("every non-current judgment a current obligation depends on has a ready or waiting route"). At present it tests only that nothing is dispatched unanswerably (line 2689), although §10.3 says it "tests for both".

## Non-blocking findings

### N1 — The accepted drift cost is larger than SD-36's wording, and the disclosure follows the wording (for the stakeholder)

SD-36 accepts drift re-dispatch, describing it as "a later or absorbed change of an integrated item's outputs reopens that item's obligations". Under current-state discharge, the Manual's own rules reopen and re-dispatch an item on more than its outputs:

- any later change to anything its implementer or reviewer *read* (§4.2 recorded reads; §7.3 context role);
- a change of a governing unit through the review's `validity` entries;
- an R1 tightening of the item after integration (§4.1 now revalidates only before integration);
- and, for findings-only `INVESTIGATE` and `DOCUMENT` items, anything they read.

This is the reviewed workplan's semantics (§6.9 roles, §7.4), so it is within "return to §7.4" and not a semantic change. But §32.3 ("to an integrated item's outputs"), the R15 row and closure map §5 describe the output case only. The read case is probably the dominant volume. Each re-dispatch also spends the obligation's iteration budget, because `(o, k)` counts every admitted result (§10.3, §13.7). A long-lived item touched or read by later items therefore reaches `COORDINATE(plan)` after the default three. The re-dispatch can also oscillate: a re-dispatched earlier implementer conforming to its contract may undo a later accepted item's change. Step 8 protects only the later item's evidence, and the oscillation is bounded only by budgets. State all of this in §32.3 and closure map §5. B1 option 2's alternative is the stakeholder's lever.

### N2 — Redundant joint-invariant re-review

The ctx `content` on `i`'s scope, kept from candidate 47 (c77447b N3), makes every earlier `JOINT_INVARIANT(i, k)` review non-current at each later change in the scope. Under current state, each derives an answerable `REVALIDATE` that re-reviews the same integrated state that `JOINT_INVARIANT(i, k')` reviews, which is quadratic re-review. B1 option 1 removes it. Otherwise disclose it.

### N3 — The drift re-dispatch's brief and admissible answer are unstated

§16.3 does not say that a drift task's brief names the change that reopened the item or the later item it came from. It also does not say whether a candidate that changes nothing (a re-attestation on current code) is an admissible integration (§22.2 treats `C_n = B_n` as records-only). Implementers need both to avoid reverting later accepted work (N1). This is a definition, not mechanism.

### N4 — Step 8's "accepted change to a prerequisite authority" is still undefined (82d618c B1 (d), partly closed)

With step 8 reading only evidence, a D1/D2 revision whose integration makes a dependent's passing evidence fail is refused unless the exception applies. Whether an integrating `AUTHOR` request carrying its counting prospective acceptance and gate is "an accepted change" at step 8 is not stated, and (Z)'s "accept a real change of `a`" presupposes that it is. State it, and state that the exemption covers only obligations that depend on the changed authority. This is a definition.

### N5 — The model's I8 oracle is still not independent of (f)'s "not superseded" (095ce55 N2, carried)

The model differs from 82d618c only by adding the same `not superseded` filter to `Ledger` (line 514) and `oracle_disagreement` (line 758). A wrong (f) clause would stay green.

### N6 — Editorial

- The R15 row says "the obligation it supported is then reopened … and re-dispatched as drift" without step 8's "for an implementer obligation". A judgment obligation is never re-dispatched (R9).
- Step 8's "every `ev` and `qual` that passes" leaves open whether a `T` to `P` change is a regression.
- §10.2's `JOINT_INVARIANT` row excludes `OVERTAKEN` admissions. For a late publication the human accepts (`late(n)`, §22.2), the joint-invariant review is presumably the one the absorption reaching `C_n` derives. Say so (c4e8de7 N6, carried).
- §22.2's "its item obligation stays `OPEN`" is false where the overtaking history carries `X`'s output bytes without being an equivalent publication. Its re-application is then a duplicate discharge (rejected). Harmless.

## Closure audit

The closure map was used to navigate. I checked its claims for every §21 item that the delta or B1 touches, against the Manual sections they name. I swept every §10.2 obligation kind for an admissible answer or a derived route after a later admitted change, a ctx-only change, an absorbed change, a fence and an overtake. Other items are carried from the 82d618c record, whose text is unchanged outside the delta, unless a mechanism below reopens them.

| Item | Disposition at this candidate |
|---|---|
| 6 (Admission validation order) | step 8 closed as SD-36 directs (82d618c B1's refusal removed); N4 definitional |
| 7 (obligation rules, readiness, discharge) | **partly open (B1)**: event-keyed judgment obligations have no current-state end; duplicate post-integration routes; `subject(o)` over several enactments |
| 9 (joint invariants) | inherits B1 (a) and N2 |
| 4, 5 | closed (82d618c N1, N2, N5, N6 answered by the kept corrections) |
| 1-3, 8, 10-27 | no unresolved architectural decision found in this bounded audit; unchanged since 82d618c |

The §16.2 rows are unchanged. §26.4 keeps an explicit replacement, retirement or preserved boundary for every row. None was found unresolved.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1-R14 | text byte-identical to 82d618c's §0.3 rows; sound as assessed there; spot-checked R9 (B1 relies on its "never ready again", which is sound; B1 is the missing end of the trigger, not R9), R12 (re-dispatch and re-application as new enactments: consistent with §10.4) and R14 (unchanged reach rule) |
| R15 | sound as the stakeholder-chosen narrowing of reviewed step 8: it keeps the workplan's purpose for evidence ("A D4 change that breaks another closure is a regression") and moves judgment staleness to current-state reopening, as SD-36 says. Its consequences are B1 and N1, and its row wording is N6 |

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **M** moot (the mechanism it attacked was removed by SD-36); **D** design/disclosure closure with real-owner execution owed later; **R** retained, disclosed decision or stakeholder option; **P** partly closed; **O** open.

**Obligation-lifecycle family.** SD-36 removes R15's latch, lines, continuations, lowered and waiting states, retirement, `RESOLVED_BY` and the lifecycle model family. The blockers of 095ce55, c77447b, 3940dbc, 3876473, 494c810 and c4e8de7 attacked that mechanism, so they are **M**, with one exception: their common driver, drift re-dispatch and post-integration staleness, returns as accepted cost (N1). 82d618c B1's refusals are **C** (step 8). Its sibling (e), the stranded revalidations, was predicted by that record for this option ("leaves … sibling (e)'s stranded revalidations"). It is half closed: the task-result half is closed by §4.1, and `IMPLEMENT`'s dependence ends at re-dispatch. The judgment-obligation half is **O** as B1 (a).

| Prior record | Disposition at this candidate |
|---|---|
| C4E8DE7 | B1 (a)-(c) **M**; N1 **M** (lifecycle family removed); N2-N4 **M**; N5 **M** (`RESOLVED_BY` gone; the D1/D2-subject question for `JOINT_INVARIANT` remains a B1 (a) concern); N6 **M**, except the `late(n)` joint-invariant bullet (**P**, N6 here) |
| 494C810 | B1 (a)-(c) **M**; N1-N4 **M**; N5 **C** (§23.6 lists review and gate decision; line 656's "re-dispatch of a reopened obligation" is now intended); N6 **C** (`JOINT_INVARIANT` excludes `OVERTAKEN`/fenced admissions) |
| 3876473 | B1 (a)-(d) **M**; N1-N4 **M**; N5 **M** (no `PENDING` latch window; `JOINT_INVARIANT`'s `k` is the admitted entry, frame instances re-derive) |
| 3940DBC | B1 (a)-(d) **M**; N1-N2 **M**; N3 **M** (no latch asymmetry); N4 **R** (model limits); N5 **M**/**O**: its warning "no implementation derives `REVALIDATE` for a stale review of an integrated transformation" is now false, and is B1 (a) |
| C77447B | B1 (a)-(d) **M**; N1-N2 **M**; N3 **C** (scope ctx entry added), with a current-state cost (N2 here); N4 **C** (fence/keep-fence waits; late publication by current state); N5 **R**; N6 **C** (route list deduplicated) |
| 095CE55 | B1 **M**; N1 **C** (`SPEC_REVIEW(spec, r)`), but now B1 (a)'s sibling; N2 **C** in text, **R** for the model (N5 here); N3 **C** (statement removed); N4 **M**; N5 **C** (mechanical `COORDINATE`; R1 tightening revalidated before integration); N6 reversed: read-based reopening is back, as cost (N1 here); N7 **R** |
| 82D618C | B1 **C** for the refusals; sibling (e) **P** (B1 (a)); sibling (d) **P** (N4); N1 **C** ("depends on" defined); N2 **C** (re-attest same candidate, newest task result, mechanical `COORDINATE`); N3 **C** (waiting class; (f)/(g)8 "not superseded"); N4 **R** (closure map §5); N5 **C** (§4.1 and (Z) wording); N6 **C**; N7 **C** for the (Z) refusal case, **R** for the model scope |
| EDABD81 | B1, B2 **C** (unchanged since 82d618c); N1-N4 **C/R** as in 82d618c; N5 **P**: the invariant now names the route half, but (Z) does not test it (B1 discriminator); N6 **R**; N7 settled (82d618c B1, now **C** by step 8) |
| 653E88C, D94A293 (different family), 913DB8F, 5895687, 4C52205 (SC-1 **R**), both E548472 (same-family SC-1 **R**), D6734C4, 83A82DF, 0D2B35E, 34803DF, BF23372, A6ED164 | §5.10 (b) table, `asserts`, reach, relief and brief carries are byte-identical to 82d618c except (a)'s relation-targeted wording and (f)/(g)8's "not superseded", which are consistent with each other and with §10.2; blockers **C**; N items **C/R/D** as the 82d618c record gives them; plan-policy items **R** |
| 6B986DE, 29DA56E, 51070E5, 9E5A763, 051CCE3, 63DDF91, F03B15E, 61CD09B | independence (`authors`, `nonind`), adjudication root and class, supersession targets, relief: **C**, unchanged |
| 362AF9F, F22B4DC, both B46C250, F7419D5, 575DC78 | acting rule, enactment unit, `rid`, gate minimum, one enactment one integration: **C**; drift re-dispatch adds enactments of one obligation, consistent with R12, except B1 (c) |
| 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC, 3540D98 | matching, content identity, `unq`, partition: **C**, §6 text unchanged since 82d618c |
| 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363, CC005DB, C6DA678, B595F2C, 6FF4ED1 | run-keyed counting, event-keyed run, `tgt` read by every consumer, frozen matching, effect-keyed write set: **C** for each stated blocker; unchanged |
| Phase B closures and N1-N4 | §6 unchanged; Phase B N2 re-read (polarity and `link⁻` anchoring under a `P`, blocked, revoked or loss-withheld completeness judgment: (2)/(4) stay in, only (1)/(3) narrow) **C/D**; support cycles (§5.6) and corrupt prefixes (§5.7) fail closed **C**; N1 **R**; N3 **R/D**; N4 **R** |

**Judgment-disagreement family (§5.10).** Its delta since 82d618c is the relation-targeted wording in (a) and "not superseded" in (f) and (g)8. Both are restrictive-neutral. A superseded vetoed passing judgment is replaced by its superseder, which is itself vetoed and routed if reached. No permissive route opens, and the restrictive direction is unchanged. The model's mutations are all caught (see "Diagnostic model run").

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Two sequential items editing one leaf unit | integrates (C); first item drifts (accepted); `REVIEW(X1)` stranded under the literal trigger (B1 (a)) |
| Second change in a joint invariant's scope touching the first change's output | **B1 (a)** |
| Second change touching only other scope units | held; redundant re-review (N2) |
| Two changes of one evidence specification | **B1 (a)** |
| Later change of a file an earlier reviewer read | integrates; **B1 (b)** duplicate routes; N1 cost |
| Second `AUTHOR` revision of a D2 subject | integrates; first `AUTHOR` drifts; a re-dispatch that reverts needs a new run, revising review and human gate (held) |
| D1 change governing an accepted D2 subject (§31.6 (Z)) | in-run re-acceptance held; also an `AUTHOR` re-dispatch and `REVALIDATE` (B1 (b)); step 8's exemption undefined (N4) |
| Absorbed foreign change of an item's outputs | drift re-dispatch (accepted); intake runs alongside; a re-dispatch may revert a disposed foreign change (N1) |
| Absorbed change breaking an item's evidence, then a no-op re-dispatch | **B1 (c)** under the natural reading |
| Fence, then keep the fence | held: the item waits, then `COORDINATE(plan)` |
| Overtaking foreign push without fence | **B1 (b)**: drift and `COORDINATE(plan)` both |
| Partitioned item, part `a` drifts after re-partition | held for the part (§13.7); the item-level review strands (B1 (a)) |
| A request making another obligation's passing evidence fail | refused (`REGRESSION`), held |
| Re-dispatch counting against the iteration budget | held as a route (`COORDINATE` on exhaustion); undisclosed cost (N1) |
| Search for latch, lowered, lines, continuation, retirement, `RESOLVED_BY`, `REVALIDATE_OVERTAKEN`, I11/I12 | none in Manual, closure map or model (one "latch" is §6.4's unrelated start latch; "retire" hits are key, lineage and run-ref retirement) |
| Composition, chain and union reach; plan closed form; review re-identification | held (unchanged; model green) |

## Minimum architecture and capability transfer

The delta is subtractive. It removes R15's latch and the model's lifecycle family, and adds no primitive, component, record kind, mode or persistent surface. B1's recommended repair defines triggers and removes a route, adding no state. Its stakeholder alternative adds one readiness condition and is marked as mechanism. Withdrawing R15 drops no owner-required capability, because the reviewed §7.4 discharge is restored.

Architecture 1.6.0 (blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41` (`git diff --quiet` succeeds), so the version-bound Core and frozen profiles are preserved (PEM PC-001).

**PEM.** Activated: this is mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` resolve to `af0455753e20ee54a969c844872e29e270007211`, and the PEM blob there and at the candidate is `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no overlay. The repository's validator, run in the clone, reports "PEM schema 1 valid: 5 families, 0 notices". Task-local HAS:

- **PC-001**: APPLICABLE (preserved).
- **DS-001**: APPLICABLE (a green diagnostic and green-looking §31.4 cases coexist with B1).
- **SP-001**: evidence-only (one owner per rule: B1 is two places computing one lifecycle).
- **SP-002, FF-001**: not material.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 keeps G1 document checks apart from G2-G4 runtime evidence and claims no execution it lacks. §31.4 now carries the 82d618c B1 positive cases, but two of its claims are false or unconditioned under the written rules: "no `REVALIDATE` stranded", and "the first's review … never a stranded obligation". An implementation of the literal triggers passes neither, so the case is a real discriminator once B1 is repaired. §31.6 (Z) tests only the dispatch half of §10.3's invariant, so a stranded route stays green there (DS-001). The diagnostic shares claim definitions and helpers with §5.10, as §5.10 (g) discloses, and models no obligations, discharge, triggers or integration, so it says nothing about B1.

## Doctrine-realization map and O1

§29 maps all seven entrypoints. The D4 row (line 2507: "reconcile every obligation … no collateral regression (§8.3 step 8)") is now consistent with step 8's evidence reading. Its "reconcile every obligation" is exactly what B1 (a) leaves open for event-keyed judgment obligations, so the same repair closes it. No other map claim depends on the delta. O1 (§0.5) is unchanged and within the requested deliverable. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

Verified:

- the candidate blobs: Manual `fce07829…`, closure map `69c84801…`, workplan `91bde236…`, Architecture 1.6.0 `39e6de72…`;
- the full clone (`git rev-parse --is-shallow-repository` is `false`) and the governing refs from `PROTOCOL-RELEASE-STATE.yaml`;
- the owner text at `aaeaf8b` (`source/roles/software-design/SKILL.md`; `architecture-and-design.md`; `workflow-and-workplans.md`; `convergence-and-cycle-economy.md`);
- every hunk of `git diff c4e8de7..f185036` and `git diff 82d618c..f185036` for the Manual, closure map and model, through a word-level diff script;
- a residue search for every R15 term;
- the §10.2 sweep described above, by hand.

Checks run at the candidate snapshot:

- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- `git diff --check c4e8de7..f185036`: clean.
- `git diff --stat fad3ee41 bf233728`: 73 files, 23269 insertions, 1 deletion, all additions outside `source/`, `dist/` and Architecture 1.6.0.
- `git diff --quiet fad3ee41 f185036 -- orchestrator/docs/architecture.md source dist`: unchanged.
- `python3 -I qualification/ssds80/judgment_disagreement_model_check.py --mutations`: run as its five families and all mutations in parallel by importing the module (`run_family`, `MUTATIONS`, `MUT`), with results recorded under "Diagnostic model run" below.

Could not verify: any runtime behavior (none exists; G2-G4). Whether the author intends `REVIEW(X)` to stop being derived after integration, since the text is silent. Earlier families beyond the unchanged-text argument and the spot checks named; earlier Reviews were not replayed item by item.

### Diagnostic model run

The model was run from the snapshot with `python3 -I`, through 39 jobs on a process pool: each of the five families unmutated, and each mutation re-running only the families it names, exactly as `main()` does.

- **Unmutated.** All five families report no invariant failure: transformation-review/acceptance/gate, equivalence-chain, completeness-cover, plan-coverage and gate-basis.
- **Mutations.** All 34 in `MUTATIONS` are caught, each by at least one of I1/I3, I2, I4, I5, I7, I8, I9 or I10. Examples: `plan_revert_exemption` by I1/I3 and I8; `obligation_direct_only` by I8; `frame_acts_everywhere` by I5; `gate_basis_record_all` by I1/I3, I9 and I10; `revision_assessment_record_mode` by I1/I3 and I10.
- **No lifecycle family.** None remains, and no lifecycle mutation remains.

A green run shows only that the written §5.10 rules satisfy the oracle on the modelled cases. It is not adequacy evidence. It says nothing about B1 (no obligations, triggers, discharge or integration) or about the I8 oracle's shared "not superseded" filter (N5).

## Scientific checks

This task reviews D3 authority for software that mediates scientific evidence. Material findings: B1 and N1-N6 above. I produced, ran or reviewed no realized scientific results: the null envelope is that no data, solver output or evidence assessment was read or produced. The diagnostic model is a logic enumeration, not a scientific result. I evaluated more than one variant:

- two readings of the `REVIEW(X)` trigger (literal and charitable), by whether each yields a stranded route;
- two readings of `subject(o)` (latest enactment and union), by whether each can discharge with failing required evidence;
- four repair options, by whether they remove mechanism and whether they retire an unseen finding.

I relied on no accepted D1/D2 authority for a consequential judgment, so no tension search was needed. Unanswered parts are listed under "could not verify".

## Common-mode note

I am of the Claude family, the same as the Manual's author and the same-family reviewers from e2154ac to c4e8de7. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. I was engaged as a fresh-context sub-agent launched by the authoring session. Fresh context does not make me independent. I share the corpus, the inherited workplan framing, the prior Review records (read as hypotheses, including the 82d618c record whose option 2 predicted part of B1), the model family's reading habits and the toolchain. A different-family confirmation of B1, and of the claim that nothing else regressed, would reduce that common mode.

## D4 statement

This Review authorizes no D4 work and accepts no architecture, product scope or default value. NO-PASS is technical evidence for G1 only. B1 is routed to the Manual's author as the D3 owner of workplan §21 item 7. The choice between option 1 and option 2's alternative, and the N1 disclosure, are the stakeholder's to confirm.
