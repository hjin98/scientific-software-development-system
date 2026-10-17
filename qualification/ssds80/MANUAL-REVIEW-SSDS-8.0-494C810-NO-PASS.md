# Independent D3 Review — SSDS 8 Architecture Manual, candidate 494c810

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          494c810017249d00967eda633334ba2987f7ff68
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g));
                        technical evidence for G1 only
    MANUAL blob:        16df7dd569f2ab7e5731ea935b7472b1c48a283a (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   054ade87fc16e69ea3974ae9fd8f5142640d7613 (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family 3876473
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; delta-first attack of R15 as
                        restated (every discharged value latches, a latched obligation is never ready
                        again, lowered obligations wait on their event's route or go to the principal,
                        records-only obligations retire on a successor's discharge), in both directions,
                        over every state of an enacted obligation and every exit from it, against
                        reviewed workplan §7.4, §7.9 and §7.10, SD-24, the workflow, evidence and
                        concurrency owners and the Manual's own §4.3, §5.10, §6.7, §7.3, §8.3,
                        §9.2, §10.2-§10.5, §12.4-§12.5, §13.7, §15.5, §16.5, §17.1, §22.2-§22.3,
                        §23.6, §31.3-§31.4 and §32.3; an independent probe of the lifecycle oracle
                        (lc_oracle) for events whose admissibility it states differently from the
                        Manual; drift classes applied to every statement of R15 and its consumers;
                        family-level recheck of earlier families against the delta; the diagnostic
                        model with every family and mutation, in parallel; the structural checks of
                        handoff §3 step 9
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched
                        by the authoring session; did not author the candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-494c810/snap`. The later commit adding the handoff (`ba66f0fa`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. SSDP 7.2.1, the reviewed workplan and the stakeholder's recorded decisions (SD-1 to SD-35, record items 19 and 31) can be realized together. The blocker below lies in R15, an author choice under record item 31 that closure map §5 (line 298) lists for the stakeholder to confirm or reverse, and it is routed against the proposed D3 owner. This is the seventh round in the obligation-lifecycle family (edabd81 N7, 82d618c B1, 095ce55 B1, c77447b B1, 3940dbc B1, 3876473 B1). The question whether R15 should exist, already put to the stakeholder by the 3940dbc and 3876473 records, is repeated below as an option.

## Verdict

**NO-PASS.** One blocker, B1, in the obligation-lifecycle family. The candidate's repair of 3876473 B1 holds at the transitions that record named: a latched obligation is never ready again and cannot be claimed (§8.3 step 7), a continuation and a requalification are admissible only while their content is current, a loss over moved content stands, a provisional value latches as `P`, and dispositions and same-revision failing assessments are lines. What the candidate does not get right is the exits *out of* the lowered state:

- **B1 (a)**, new mechanism: a lowered records-only obligation (`JOINT_INVARIANT(i, k)`, `SPEC_REVIEW(spec, r)`) "is retired when a successor of its kind on the same scope … is discharged" (line 1323). The successor's judge is never shown the standing finding, the successor may have been discharged before the finding existed, and for `SPEC_REVIEW` the successor judges a different change. An upheld finding of an invariant violation, or of an improper specification change, then derives no obligation and reaches no decider. This rule is stated nowhere else (not in the R15 row, closure map line 87 or 298), and it contradicts §31.4's own discriminator for the joint-invariant case.
- **B1 (b)**: a lowered obligation "waits" while its event's route is open. For a veto of a transformation review or a gate decision recorded after the reviewed content moved, the owner's ending routes (supersession, relief) are inadmissible at step 6. §10.3 then puts that `ADJUDICATE_DISAGREEMENT` in the class that "waits by design" on an upheld challenge nobody is dispatched to raise. So the latched obligation waits with no actor and never reaches the principal. The candidate made the parallel loss case stand once content moved; the veto case it left waiting.
- **B1 (c)**: the routed state has no complete set of exits. §15.5 names no allowed outcomes for the new `COORDINATE(plan)` trigger. A records-only obligation with no item (a joint-invariant review of an absorbed change, a specification changed directly by a human) goes to `HUMAN_ATTENTION`, whose answer retires nothing. The exits §10.4 does name, an R2 amendment or a withdrawal, leave no way to record "repaired by item J" (which §32.3's "a deliberate repair is a new item" assumes) or "accepted with reason" other than re-doing the item under a contrived new key or withdrawing delivered work.

The diagnostic model is green on all six families and catches every one of the 46 mutations (lifecycle: 809,812 scenarios; I11 and I12 hold). Its lifecycle family does not model retirement, principal decisions, `SPEC_REVIEW`, no-item routing or the admissibility of owner answers after content moves. Its `adjudicate_R` event ends a veto after `content_change`, and its oracle agrees. So B1 is green by construction (N1).

## Blockers

### B1 — The exits of a lowered latched obligation close a standing finding without a decision, strand it with no actor, or are undefined

**Family:** obligation lifecycle after integration (82d618c B1, 095ce55 B1, c77447b B1, 3940dbc B1, 3876473 B1). It enters through the repair of 3876473 B1: that record's option 1 (route standing lowerings to the principal), plus a mechanism that option did not contain (successor retirement).

**Earliest owner:** Manual §10.4, "A latched obligation is never ready again" (line 1323), and the R15 row (line 100). Workplan §21 item 7 ("obligation rules …, readiness, three-valued discharge, …") and item 9 (joint invariants, §9.2); §15.5 (principal decisions) contributes.

**Status:** open, material, non-local.

**Exact rules at the candidate.**

- §10.4 (line 1323): "When some lowered term has no such line, because a lowering event stands …, the lowered obligation derives `COORDINATE(plan)` for the plan of its item (for a records-only obligation, the item whose enactment derived it), or `HUMAN_ATTENTION` where it has no plan. The principal's decision is the route: an R2 amendment of the item (a new key, so a new obligation, for a repair or a re-application) or its withdrawal, with any further repair or investigation as items of their own. Until then the lowered obligation stays lowered and its plan shows it; the amendment or withdrawal retires it, and **a records-only one is retired when a successor of its kind on the same scope (`JOINT_INVARIANT(i, k')` for a later `k'`, `SPEC_REVIEW(spec, r')` for a later `r'`) is discharged**."
- §10.4 (line 1323): it "**waits** while every lowered term has a line all of whose lowering events have their own route open (`ADJUDICATE(c)` for a challenge, `ADJUDICATE_DISAGREEMENT` for a veto or a counting failing assessment, `REQUALIFY` for a loss, only while the content the withheld record judged is current: once a later admission has changed it, the loss stands for the latched obligation)".
- §10.3 (line 1293): "One class waits by design: an `ADJUDICATE_DISAGREEMENT` for which neither the owner's supersession nor relief is admissible because the bases they need no longer hold (… a transformation review whose frame no longer exists) waits on an upheld challenge, which the owner or any qualified actor may raise, or on the owner's adverse record superseding the vetoed passing judgment …; the vetoed record then blocks no work."
- §9.2 (line 1226): a joint-invariant obligation is "a `REVIEW` of the integrated result against the invariant"; §10.2 (line 1270): `SPEC_REVIEW(spec, r)` is raised by "a change of an evidence specification to revision `r` (each change its own obligation)"; §17.1 (line 1842): its brief "lists the counted failures the change would make stale and the readings it would stop covering".
- §16.5 (line 1772): an acceptance or gate brief carries standing adverse judgments in its reach, "the same carry applies to the brief of the next judge of an equivalence, completeness, intake disposition or product-scope acceptance"; a transformation review carries standing `NO_PASS`/`NONCONFORMANT` on the same changed-unit content. No carry exists for an upheld challenge against a joint-invariant or specification review.
- §31.4 (line 2669): "a latched joint-invariant review revoked after a later change in the invariant's scope derives `COORDINATE(plan)` (or `HUMAN_ATTENTION` outside a plan), never a stranded or unanswerable obligation".
- §15.5 (lines 1657-1666): `COORDINATION_DECISION` outcomes "are a function of the report's kind, reason and target domain"; the table's rows name reports only. §12.4: the principal decides at R1, "never acceptance".
- §4.3 (line 570), §7.3 (line 1122): a `REVIEW` of `X` carries frame-role `content` on every unit of `Δ(X)`, and an output entry has "ordinary currency in the admitted state" after integration; a `GATE_DECISION` carries "`content` on the gated subject revision" (line 579).

**(a) Successor retirement closes an upheld finding without any decision.**

1. Joint invariant `i` constrains units `u` and `v`. Item `I` (plan `P`) changes `u`; its integration is entry `k`. `JOINT_INVARIANT(i, k)` is answered by reviewer `V`'s passing review of the integrated result. It latches `T`.
2. Item `J` changes `v` (an unrelated edit inside `i`'s scope) at `k'`. `JOINT_INVARIANT(i, k')` is answered by reviewer `W`'s passing review. It latches `T`. `W`'s brief contains nothing about `V`'s review: no objection exists yet, and §16.5 has no carry for this kind in any case.
3. Challenger `C` shows that `I`'s change at `k` violates `i`: say, a unit-convention contract between `u` and `v` that `J`'s edit did not touch. `C` declares the challenge `ROUTINE`, and the targets are D3/D4, so no floor raises it. An eligible adjudication upholds it, and `V`'s review is `REVOKED`.
4. `JOINT_INVARIANT(i, k)` is lowered by a standing event. A successor of its kind on the same scope (`JOINT_INVARIANT(i, k')`) is discharged, so it is retired. No `COORDINATE(plan P)` and no `HUMAN_ATTENTION` is derived.
5. The tree carries an invariant violation established by an upheld challenge. Every obligation is discharged or retired, and `P` shows all its items closed. `W`'s pass stands, unchallenged, over the same violating content: it judged that content without seeing the finding.

Sibling orderings and kinds:

- **Finding before successor:** the challenge is upheld first, so `COORDINATE(P)` is derived. `J` then integrates, `W` passes without the finding in its brief, and the retirement removes the `COORDINATE` trigger, possibly while the principal's coordination task is running. The decision owed vanishes with no answer.
- **`SPEC_REVIEW`:**
  1. Revision `r` widens an `ABS_TOL` from `1e-8` to `1e-4`, and the owner's review passes.
  2. Revision `r'` changes the runner class, and its review passes. Its brief lists only what `r'` would make stale.
  3. A challenge that `r`'s widening was fitted to a failing backend is upheld. That is the D2 doctrine row of §29: "tolerances from accepted error semantics, never from a failing backend".
  4. `SPEC_REVIEW(spec, r)` is retired by `SPEC_REVIEW(spec, r')`, a judgment of a different change. The widened tolerance stays, and evidence passing under it keeps supporting the claim. Nothing is derived unless the challenge's own materiality creates human attention, and human attention has no route that re-examines the specification either.
- **§31.4 contradiction:** the discriminator says a joint-invariant review "revoked after a later change in the invariant's scope derives `COORDINATE(plan)`". Under §10.4 that holds only while the later change's `JOINT_INVARIANT(i, k')` is still undischarged, which is the uncommon order. An implementation must break one of the two.
- **The Manual's own retirement principle elsewhere:** "Retirement … never disposes of a failing assessment: `qual` keeps reading it through the lineage, and the owner disposes explicitly" (§10.2, line 1289); "What does not end a disagreement: … retirement, split or retargeting of the obligation" (§6.7, line 1075). Successor retirement does to an upheld judgment finding what those rules forbid for a failing assessment: two places computing one thing differently.

**(b) A lowered obligation waits on a route that no actor is dispatched to take.**

1. Item `I` integrates `X`. Review `R` (by `V`) passes, the gate decision `h1` is unqualified, and `I` latches `T`.
2. A later item `J` edits a unit `u ∈ Δ(X)` (step 8 admits it, R15).
3. A peer reviewer or authenticated human records `NO_PASS` on `id(X)`. It is adverse and never-lost, so it is admitted. It vetoes `R` (§5.10 (b), same changed-unit content), so `R`'s line is `F` and `I` is lowered. Its event's route, `ADJUDICATE_DISAGREEMENT`, is open, so `I` **waits**.
4. The owner's ending routes are the owner's superseding pass and per-target relief (§5.10 (d) routes 2-3). Both are passing `REVIEW` records on `X`, so step 6 refuses them: the output entry on `u` is stale (§4.3, §7.3). §10.3 places exactly this case ("a transformation review whose frame no longer exists"; more generally "the bases they need no longer hold") in the class that "waits by design" on an upheld challenge "which the owner or any qualified actor may raise". No obligation derives that challenge.
5. Outcome: the route is open but never taken, so `I` waits indefinitely. It is not routed to the principal, because no event "stands", and the standing objection to integrated work reaches no decider. The owner may also be dispatched only to record an adverse answer, which ends only one way, so whether the owner is asked at all depends on a dispatch reading §10.3 leaves open (dispatched for the adverse answer, or "waits" undispatched). §10.3's assurance "the vetoed record then blocks no work" no longer holds: under R15 the vetoed record is a line of a latched obligation.

The same holds for a gate `REJECT` on `(g, s, r1)` recorded after `s` moved on. It vetoes `h1` in any run. The rejecter's reassessment and the owner's superseding decision are passing gate decisions needing `content` on `r1`, and gate decisions have no relief. The candidate's own loss rule shows the intended treatment: "once a later admission has changed it, the loss stands for the latched obligation". The veto case was not given it.

**(c) The routed state's exits are incomplete.**

- **No outcomes for the trigger.** §15.5 makes a `COORDINATION_DECISION`'s allowed outcomes "a function of the report's kind, reason and target domain". A lowered latched obligation is not a report, and no row names it. Whether the principal may `ESCALATE`, `DECLINE` or `RESOLVE_LOCAL` is undetermined. If it escalates, the human's judgment discharges `HUMAN_ATTENTION` (A8), but no rule says that judgment retires the lowered obligation.
- **No exit without an item.** A `JOINT_INVARIANT(i, k)` whose `k` is an absorption, or a `SPEC_REVIEW(spec, r)` whose `r` came from a direct human change, goes to `HUMAN_ATTENTION`. §10.4's only decision exits (an R2 amendment or withdrawal "of the item") do not exist for it. Its only exits are a successor (a) or a counter-challenge. Without (a), it stays lowered and `OPEN` for ever once the human has answered. §12.5 meanwhile routes decisions owed on no-plan obligations to the standing plan's principal (line 1277): two statements of one routing that disagree.
- **No "resolved" or "preserved" closure.**
  - §32.3 (line 2770) says "a deliberate repair is a new item". A new repair item retires nothing: only an amendment or withdrawal of the lowered item does. So after the repair integrates, the old item stays lowered unless the principal also withdraws it, and withdrawal is a topology change needing whole-plan R2 review (§11.4). The plan then records as withdrawn an item whose work is integrated and repaired, which misstates what was delivered.
  - A principal or human who judges the standing event immaterial has no exit other than an R2 amendment. That needs a prose or fixed-field change to obtain a new key, since byte-identical prose is the latched key, and then re-integrated work.
  - The workflow owner's closure vocabulary ("resolved, preserved-with-reason, or unavailable/blocking") has no counterpart here.
- **An unlisted exit.** For a partitioned item, a re-partition is an R1 `PARTITION` decision over "its undischarged obligations" (§13.7). It reaches a lowered (`OPEN`) part and re-dispatches it without an R2 amendment, an exit §10.4 does not list.

**Shared cause.** R15 now defines the lowered state's entry well. Its exits were added piecemeal: one automatic exit (successor retirement), one waiting exit whose route's availability it did not check against Admission (b), and one decision exit routed into a decision table that does not know it (c). This is again two places computing one thing (the handoff's drift classes):

- the lowered obligation's exits versus the Manual's rules for closing adverse findings (§6.7, §10.2 retirement, §16.5 carries);
- the waiting condition versus route admissibility (§10.3, step 6);
- the routing versus §15.5 and §12.5.

Discovery stops here. Further variants re-derive (a)-(c): an item-level review of a partitioned item, revoked after a later item; a findings-only `INVESTIGATE` item revoked; a `CONFORMANCE` veto after content moved.

**Controls that hold.**

- A latched obligation is never ready and never claimable (step 7), with re-work refused (`rework` in the model).
- An upheld challenge on the discharging review, an owner's adverse supersession and a rollback route an item obligation to its plan's principal.
- A counter-challenge upheld after routing restores the value, and the trigger disappears.
- A continuation or requalification after the content moved is refused, and the loss stands.
- A provisional value latches as `P` and is lifted by an unqualified continuation while content is current.
- A revoked relied-on disposition, and a new counting failure on the read revision, lower the item.
- A fenced or `OVERTAKEN` admission undoes the latch, and the re-application claims it.
- An open blocking challenge waits on `ADJUDICATE(c)`, whose adjudication is challenge-tier and always admissible.
- A loss boundary with requalification while content is current restores.
- Entry order, later runs and content changes do not lower.
- The derivation stays stratified: the waiting and retirement conditions read other S3 obligations, none of which reads the latched obligation.

**Violated owner text.**

- **Workflow owner** (`aaeaf8b:source/shared/references/workflow-and-workplans.md`, line 96, its impact-closure rule, applied here to the material finding an upheld challenge establishes): "close each material impact item as resolved, preserved-with-reason, or unavailable/blocking". Successor retirement closes an upheld finding with none of these, and (c) offers none of the first two.
- **Reviewed workplan §7.9, Persistence** (Phase B candidate, line 1675): "Every obligation derived from a report or challenge — human attention, coordination, adjudication — … closes only when a resolving record targets the report by `identity` and stays in force … When the report's target or basis moves …, the obligation stays open …, so the decider can answer 'moot' explicitly." The coordination owed after an upheld challenge disappears when an unrelated successor is discharged (a).
- **Evidence owner** (`evidence-evolution-and-dependencies.md`, line 153): "An unresolved material disagreement keeps dependent present guidance/closure visibly qualified" (a), (b).
- **Architecture owner** (`architecture-and-design.md`, line 96): "define it before dependent invariants use it: … lifecycle states and transitions" (b), (c).
- **The Manual's own statements:** §31.4's joint-invariant discriminator (a); §10.3 "the vetoed record then blocks no work" and "No stranded obligation" (b); §32.3 "a deliberate repair is a new item" (c); §10.2 and §6.7 on retirement never disposing of an adverse finding (a); §0.4 S9, "an agent PASS is a recommendation" (in (a), an agent's pass on a different target ends an upheld finding).

**Convergence assessment.** This is a non-local recurrence: the seventh round in this family. It is the first in which the defect sits in transitions the model does not represent (retirement, decisions, route admissibility) rather than in the latched value itself. The value rule now looks sound, and the lifecycle model helped: every value-level sibling I tried agrees with the Manual. The remaining defects lie where R15 meets the rest of the workflow. Each round has found a new coupling of that kind (Admission currency, §10.3 answering, §5.5 dispute terms, now closing rules and decision tables). The active simplification trigger applies ("repeated patches around the same mechanism … patch-on-patch repair"). The repair should delete the automatic exit rather than add a carry.

Options for the stakeholder (Phase C handoff §5):

1. **Recommended: one exit, by decision. Removes successor retirement; adds one §15.5 row.**
   - A lowered latched obligation leaves the lowered state only when its events resolve, or by one deciding record: the principal's `COORDINATION_DECISION` for a plan item, or an authenticated human judgment on `HUMAN_ATTENTION` where there is no item.
   - Name that record's outcomes in §15.5: `AMEND` (a new key, re-work), `RESOLVED_BY` (naming the item or later obligation that dealt with the event) or `PRESERVE` (accepted with reason, R3 where the event is an upheld challenge or veto), and `ESCALATE`. Each but `ESCALATE` retires the lowered obligation.
   - Give the decider's brief the event, and any successor's pass labelled as not having seen it.
   - Treat a veto as standing for the latched obligation once neither the owner's supersession nor relief is admissible, exactly as the loss rule does. Reconcile §10.3's "blocks no work", §12.5, §31.4 and §32.3.
   - This removes one automatic transition and adds one decision row, so it adds mechanism there.
2. **Withdraw R15** and return to the reviewed §7.4 current-state discharge, with step 8 narrowed to evidence regression (82d618c option 2). This re-introduces drift re-dispatch, which R15 exists to remove, but removes the family. Both previous records put this to the stakeholder.
3. **Keep successor retirement, but carry the standing event into the successor's brief** and retire only on a successor whose `findings` slot records it `RESOLVED`, as the §16.5 plan carry does. This adds mechanism, and it still needs (b) and (c) repaired.

**Required discriminator.** At the real owners (Admission steps 6-9 → Derivation discharge → obligation derivation → Dispatcher → principal and human views):

- `JOINT_INVARIANT(i, k)` and `JOINT_INVARIANT(i, k')` both discharged; then a challenge against `k`'s review upheld. Expected: a decision is derived and persists until a deciding record retires it. A discharged `JOINT_INVARIANT(i, k')` alone ends nothing. Repeat in the opposite order (finding first, successor second) and for `SPEC_REVIEW(spec, r)` with a later `r'`.
- A peer `NO_PASS` on `id(X)`, and a gate `REJECT` on the integrated triple, each recorded after a later item moved `Δ(X)` or the subject. Expected: the latched item is routed to the principal (or the owner is dispatched with an admissible answer), never left waiting with no actor.
- A lowered `JOINT_INVARIANT(i, k)` with `k` an absorption. Expected: the human's judgment has a defined effect on it.
- A standing lowering repaired by a new item. Expected: the old item's state after the repair integrates is the one the chosen option defines, never permanently `OPEN` and never "withdrawn" without that being its recorded disposition.
- Negative controls: the 3876473 and 3940dbc discriminators, which must still hold.

§31.4 has none of these, and its joint-invariant case expects what §10.4's retirement prevents (DS-001).

## Non-blocking findings

### N1 — The lifecycle oracle shares two admissibility errors with the model, and omits the exits

§31.3 discloses that the oracle "reads the same event list, so an event the list omits is unchecked", and that "what the principal then decides, and retirement, are not modelled". Beyond those omissions, the model and its oracle agree on two event admissibilities that the Manual states differently. My probe is `$TMPDIR/ssds80-manual-review-494c810/scripts/probe.py`, run on the unmodified snapshot module.

- **`adjudicate_R` after `content_change`.** Both give `(2, 'none')` for `(content_change, veto_R, adjudicate_R)` and `(veto_R, content_change, adjudicate_R)`. The model gates `refresh_*`, `revalidate_R` and `requalify_R` on `moved`, but not the owner's ending of a veto, which needs a passing record with current `Δ(X)` content (B1 (b)). Under the Manual both cases stay at `(0, 'wait')` with no actor.
- **`fail_E` after `content_change`.** Both give `(2, 'none')`, with the comment "on later content it is not an event (item 31)". The event is described as "a new counting failing assessment on the same claim content". After `content_change`, that content is still the revision the predicate read, and the Manual lowers on "a failing assessment that counts against a claim on a revision the predicate read at `D_m`", whether or not a later item has moved the claim. Failing assessments on old content can keep counting (§6).

Omitted cases:

- retirement and the principal's decisions (B1 (a), (c));
- `SPEC_REVIEW`, the item-level review and findings-only `INVESTIGATE`;
- no-item routing;
- a gate veto;
- an `OVERTAKEN` joint-invariant start, which returns `unlatched` with no route checked (N6).

A stronger oracle would decide each event's admissibility from the Manual's Admission rules in the state where it occurs, rather than from the event list. That is diagnostic mechanism, not architecture.

### N2 — A same-triple qualified gate decision after the latch is ignored, unlike a same-revision failing assessment

After the latch, "a minimum such as `gterm` the minimum" is taken over the gate decisions in `gterm` at `D_m`. A later `QUALIFIED` `ACCEPT` by another eligible holder on the same gate and the very triple the item produced is neither a line nor an event:

- in current state it makes `gterm` `P` (§5.5's minimum, SD-24);
- the latched item stays `DISCHARGED`.

The candidate's own principle (closure map line 298: "a new counting failing assessment on a revision it read lowers the item like an adverse event against its gate or review", answering 3876473 B1 (d)) treats same-content disputes as lowering. So the asymmetry should either be removed (a qualifying decision on a triple the predicate read caps the gate line at `P`) or listed with the item-31 evidence choice for confirmation.

### N3 — The disposition line and `IMMATERIALITY` currency

`IMMATERIALITY` "stands at its own currency, since its premise is about the current governing state" (§6.7), so a later content change can make it non-current, and in current state the failure it disposed of counts undisposed again. Under the line rule, the disposition is a line lowered only by "the revocation of a disposition line". But the failing-assessment event, "a failing assessment that counts against a claim on a revision the predicate read at `D_m`, until its disposition", read in current state would fire on that content change. That contradicts "content changes … never lower it". The general clause lets an implementer resolve this, but the rule should say that, for a failure disposed of at `D_m`, the disposition line, not current `disp`, decides.

### N4 — Unstated costs of the decision exits and of a latched `P`

- **Permanently provisional.** A latched `P` (a `QUALIFIED` gate, or an override in scope) is lifted only by a continuation, which is admissible only while the gated content is current. After a later change of the item's outputs, the item stays `DISCHARGED_PROVISIONAL` for good. §31.4's "becomes `DISCHARGED` when the qualification is lifted" holds only before that.
- **Re-work under a new key.** Because the key is the item's prose and fixed fields, a pure re-application (a re-cutover after a rollback) needs a contrived prose change.
- **Partitioned items.** An R2 amendment of a partitioned item drops every part's discharge, not only the lowered part's.
- **Standing is not terminal.** A counter-challenge or a further continuation can restore a line after routing, so a principal's amendment made in between duplicates work by decision.

All four are fail-closed. They belong in closure map §5 with the R15 consequence the stakeholder is asked to confirm.

### N5 — Editorial and drift

- §23.6's requalification kinds ("a fresh acceptance, adjudication, assessment, realization, import or consultation") omit the review and gate decision. R15 relies on `REQUALIFY` of exactly those lines, where the continuation is the requalification.
- Line 656 still says "a re-dispatch of a reopened obligation".
- §10.4's "an accepted late publication (`late(n)`) latches it from that decision" does not say at which state its value and lines are read. That is unchanged from 3876473, but now that the latch is undone at the fence, it decides the value.

### N6 — An `OVERTAKEN` records-only answer

"A fenced or `OVERTAKEN` admission `m` … undoes the latch: the obligation is `OPEN` and unlatched, and its re-application claims it." For `JOINT_INVARIANT(i, k)` answered in an overtaken frame, the re-application is a new entry `k₂` with its own `JOINT_INVARIANT(i, k₂)`. The old obligation stays `OPEN` and unlatched, with no admissible answer (its scope content is absent from the absorbed tree) and no retirement rule, since retirement is stated only for lowered obligations. The same holds for an overtaken records-only admission. Whether the old obligation is derived at all for an overtaken `k` should be stated.

## Closure audit

I used the closure map to navigate and checked its R15 claims against the Manual. The Manual delta since 3876473 is nine hunks:

- 100 (R15 row);
- 1189 (§8.3 step 7);
- 1256 (`COORDINATE(plan)` trigger);
- 1268 (`HUMAN_ATTENTION` trigger);
- 1293 (§10.3);
- 1321-1323 (§10.4);
- 2116 (§22.2);
- 2663 (§31.3);
- 2669 (§31.4).

Closure map lines 87, 298 and 313 changed.

| Item | Disposition at this candidate |
|---|---|
| 7 (obligation rules, readiness, discharge) | **open (B1)**: the lowered state's exits; the value rule itself holds |
| 9 (joint invariants) | **partly open (B1 (a), (c))**: a revoked latched review is retired by any later discharged review of the same invariant, and has no decision exit when its change had no item |
| 6 (Admission validation order) | step 7's "undischarged and unlatched" is sound; step 6's refusal of stale owner answers is what B1 (b) turns into an unrouted wait |
| 15 (reports, escalation, coordination) | **partly open (B1 (c))**: §15.5 does not name outcomes for the new `COORDINATE(plan)` trigger |
| 13 (publication), 18 (migration, cutover) | the latch undone by a fence or `OVERTAKEN` holds for item obligations (N6 for records-only answers); rollback routes to the principal, and re-cutover is an amendment (N4 cost) |
| 1-5, 8, 10-12, 14, 16-17, 19-27 | text byte-unchanged since 3876473 outside the hunks above; no unresolved architectural decision found in this bounded audit (see the re-verification below for its basis) |

§16.2 rows (both tables): byte-unchanged since 3876473. §26.4 keeps an explicit replacement, retirement or preserved boundary for every row; I found none unresolved. Material decisions remain marked `[D3 decision]` and distinguished from `[delegated]` D4 space. Apart from B1, I found no under-specification an implementer would have to settle architecturally.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1 | Sound; unchanged. Phase B N2 closed in text (below) |
| R2, R3 | Sound fail-closed SCC clamp and integrity halt; unchanged |
| R4 | Sound; unchanged. The fence now also undoes an R15 latch (N6 for records-only answers) |
| R5-R8 | Sound; unchanged |
| R9 | Sound. The 3876473 contradiction between "never ready again" and "becomes ready" is removed |
| R10-R14 | Sound; unchanged. The plan row's closed form is a stakeholder-chosen conservative policy (SD-32 to SD-35) |
| R15 | **Sound as a value rule; its lowered-state exits are unsound or incomplete (B1).** Every discharged value latching, with no return to ready, closes 3876473 B1 (a)-(d) at the transitions that record named. Successor retirement is an unsurfaced closure route that ends upheld findings without a decision. The waiting exit ignores route admissibility for vetoes, and the decision exit lacks an outcome set. The change from the reviewed §7.10's mechanical re-iteration (R0) to a principal decision (R1) after a standing lowering is surfaced (closure map line 298) and is a stakeholder trade-off, not a blocker. An author choice under item 31; options to the stakeholder (B1) |

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **D** design or disclosure closure, with real-owner execution owed later; **R** retained as a disclosed decision or stakeholder option; **P** partly closed.

**Basis.**

- I re-derived the delta's mechanisms independently.
- I re-checked families the delta does not touch in three ways:
  - by the full model run (all six families green, all 46 mutations caught);
  - by confirming their text is byte-unchanged since 3876473 (`git diff -U0` lists only the hunks above);
  - by reading their owner sections at the candidate (§4.3, §5.6-§5.7, §5.10, §6.7, §7.3, §8.3, §9.2, §10.2-§10.5, §12.4-§12.5, §13.7, §15.5, §16.5, §17.1, §22.3, §23.6-§23.7).
- I did not replay earlier records item by item. For records before 3876473, the dispositions are those the 3876473 record gives, re-checked at the family owners above and against the unchanged text. Those records are mostly of this reviewer's family, so they are hypotheses carried, not independent confirmation.

**Mechanisms independently checked at this candidate:**

- **3876473 B1.**
  - (a) Standing lowering with no re-discharge: the obligation is never ready; standing goes to the principal, and an R2 amendment makes a new key. **P**: the decision exits are B1 (c) here.
  - (b) Continuations inadmissible after content moved: now stated, and a loss over moved content stands. **P**: the veto analogue is B1 (b) here.
  - (c) Lowered judgment obligations against §10.3: never ready again, and routed. **P**: records-only retirement is B1 (a) here.
  - (d) Dispute terms: dispositions and same-revision failing assessments are lines. **C**, with N2 (gates) and N3 (`IMMATERIALITY` currency).
- **3876473 N1-N5.**
  - N1, "no re-dispatch" against unlatched `P`: `P` latches, so the statements agree. **C**
  - N2, item-level review latch point: now a records-only answer, latched where it first acts. **C**
  - N3, `P` outside permission had no route: now a lowering, and "a qualification outside its permitted scope" stands. **C**
  - N4, the oracle's provisional short-circuit and the omitted events: the short-circuit is removed; re-work, gate revocation, evidence and disposition lines and override expiry were added. **P** (N1 here).
  - N5, `PENDING` window and `k`: the latch now holds from `D_m` and is undone by a fence, so the window concern is moot; `k` is still implicit and harmless. **C**
- **3940dbc, c77447b, 095ce55, 82d618c B1 and N items.**
  - Refresh not a withdrawal, frame answers stale after a rebase do not latch, lines computed by machinery, entry-order independence, no `tgt` after the latch, the prose-and-fixed-fields key, fence and late publication, the enacted class: **C**. Re-checked by the lifecycle family's mutations, each caught, and against the text.
  - 82d618c's drift re-dispatch: **C**, now for `P` items too.
  - 82d618c N4 (history carry for a lineage-less re-identified subject): **R**, still listed in closure map §5.
- **Revising duty and liveness (653e88c, edabd81):** `standing` entries at §4.1, §4.3, §8.3 step 7 and §10.2 are unchanged. **C**
- **Judgment disagreement (§5.10).**
  - The table, the one reach rule and invariants (g) 1-8 are byte-unchanged.
  - §5.10 remains the one owner; other sections point to it.
  - The plan row's closed form is a stated conservative resolution policy, re-read against its claim; the equivalence `authors` input covers both sides and re-producers.
  - **C/R** as in earlier records. The R15 delta interacts with §5.10 only through vetoes as lowering events (B1 (b)).
- **Matching (§6.3-§6.6).** Unchanged.
  - Phase B N2 in text: `link⁻` is an S0 test that reads no completeness. A differing old-content run under (2) and a yielding present-content run under (4) therefore stay in, under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld; only (1) and (3) narrow through `on⁺`.
  - Support cycles (§5.6) and corrupt prefixes (§5.7) fail closed.
  - **C**
- **Content identity, gate qualification (`unq` in `gterm`), equal-region partition, run identity, acting rule.** Unchanged. **C** in their owners.

| Prior record | Disposition at this candidate |
|---|---|
| 3876473 (same family) | B1 (a) **P**, (b) **P**, (c) **P**, (d) **C** (N2, N3 here); N1 **C**; N2 **C**; N3 **C**; N4 **P**; N5 **C** |
| 3940DBC (same family) | B1 (a)-(d) **C**; N1-N3 **C** (N3's evidence choice **R**); N4 **P**; N5 **C** |
| C77447B, 095CE55, 82D618C (same family) | blockers **C**; N items **C**, with 82d618c N4 **R** and the diagnostic-scope items **P** |
| EDABD81 (same family) | B1, B2 **C**; N1-N4 **C/R**; N5, N6 **C**; N7 settled, its lineage is this family |
| 653E88C (same family) | B1 **C**; N1, N2 **C**; N3 **P/R** (model limits); N4 **R** |
| D94A293 (different family) | B1 **C**; N1 **C/R**; N2 **R** (§32.2); N3 **P** (model limits) |
| 913DB8F, 5895687 (B1, B1(b)), 4C52205 (SC-1 **R**), both E548472 (same-family SC-1 **R**; different-family N1-N3), D6734C4, 83A82DF, 0D2B35E, 34803DF, BF23372, A6ED164 | plan, review, equivalence and completeness rows unchanged; blockers **C**; N items **C/R/D** as the earlier records give them; plan-policy items **R** |
| 6B986DE, 29DA56E, 51070E5, 9E5A763, 051CCE3, 63DDF91, F03B15E, 61CD09B | independence, adjudication eligibility, supersession targets and relief: blockers **C**; N items as earlier records |
| 362AF9F, F22B4DC, both B46C250, F7419D5, 575DC78 | acting and enactment, run identity, gate minimum, one integration per enactment: **C** |
| 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC, 3540D98 | matching, content identity, qualification cap in `gterm`, partition: **C**, with R items unchanged |
| 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363, CC005DB, C6DA678, B595F2C, 6FF4ED1 | **C** for each stated blocker (run-keyed counting, event-keyed run, `tgt` read by every consumer, frozen matching, effect-keyed write set); N items as earlier records |
| Phase B closures, N1-N4 | matching-family closures re-verified in text (above); N1 **R** (§32.2); N2 **C/D**; N3 **R/D** (diagnostic limits); N4 **R** (empirical costs) |

Restrictive and permissive attack on the assessment-disagreement family, re-done against the delta: R15 touches §6 only through `ev`, `qual` and the dispute lines.

- **Permissive direction:** a disposed failure whose disposition is revoked now lowers (3876473 B1 (d) closed); N3 is the remaining ambiguity.
- **Restrictive direction:** no settled failure is resurrected by a content change, unless N3 is read against the general clause; a failure on later content reaches only the subject (item 31, disclosed).

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Two joint-invariant reviews discharged; then an upheld challenge on the first | **B1 (a)**: retired by the successor, no decision derived |
| Upheld challenge first, then a later in-scope change reviewed without the finding | **B1 (a)**: the `COORDINATE` trigger vanishes |
| Specification widened at `r`, unrelated `r'` reviewed; upheld challenge on `r` | **B1 (a)** |
| Peer `NO_PASS` on an integrated `X` after a later edit of `Δ(X)` | **B1 (b)**: waits with no actor |
| Gate `REJECT` on the integrated triple after the subject moved | **B1 (b)** |
| Lowered joint-invariant review of an absorbed change | **B1 (c)**: `HUMAN_ATTENTION` with no retiring answer |
| Standing lowering repaired by a new item | **B1 (c)**: the old item stays lowered unless withdrawn |
| Lowered part of a partitioned item, then re-partitioned | **B1 (c)**: an unlisted R1 exit re-dispatches |
| Latched item; upheld challenge on its review; re-integration claim | held: refused (step 7), routed to the principal |
| Rollback, then re-cutover by an amended item | held (N4 cost) |
| Continuation or requalification after the content moved | held: refused, and the event stands |
| Same-triple `QUALIFIED` gate decision by another holder after the latch | N2: ignored |
| `IMMATERIALITY` relied on at `D_m`, its basis moved by a later change | N3: ambiguous |
| `QUALIFIED` gate at integration, permitted; later output edit | held (`P` for good; N4) |
| Risk-overridden challenge on the produced triple; override lapses | held (`F`, waits on `ADJUDICATE(c)`) |
| Open blocking challenge after the content moved | held: adjudication is challenge-tier and admissible |
| Fenced or `OVERTAKEN` item integration, kept or re-applied | held; N6 for records-only answers |
| Counter-challenge upheld after routing | held: restored; amendment in between duplicates by decision (N4) |
| Entry order, second `AUTHOR` revision, absorbed foreign change of a latched item | held |
| Later item breaking an earlier item's required evidence | held: `REGRESSION` |
| Stratification of the new S3 conditions (waiting, routing, retirement) | held: no cycle through the latched obligation |
| Composition, chain and union reach; review re-identification; plan closed form over every tightening shape | held (unchanged; model green) |
| Completeness lapse under a narrow-basis failure (Phase B N2) | held |

## Minimum architecture and capability transfer

The delta adds no primitive, component, record kind, basis mode or persistent surface. It removes two transitions (unlatched `P`, "becomes ready"). It adds two `COORDINATE`/`HUMAN_ATTENTION` triggers and one automatic transition (successor retirement). Option 1 removes the automatic transition and adds one decision-outcome row. Two capabilities an owner requires are not delivered as realized:

- the explicit closure of a material finding (workflow owner, reviewed §7.9 persistence);
- a decider for a standing objection to integrated work once its content has moved.

Architecture 1.6.0 (`orchestrator/docs/architecture.md`, blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41` (`git diff --stat fad3ee41… 494c8100… -- orchestrator/docs/architecture.md source dist`: empty). The version-bound Core and frozen profiles are preserved (PEM PC-001).

**PEM.** Activated: this is mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` both resolve to `af0455753e20ee54a969c844872e29e270007211`. The PEM blob there and at the candidate is `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no overlay. The repository validator (`python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run in the clone, whose `source/` and PEM equal the candidate's) reports "PEM schema 1 valid: 5 families, 0 notices". Task-local HAS:

- **PC-001**: APPLICABLE (frozen profiles; preserved).
- **DS-001**: APPLICABLE. The green lifecycle family and §31.4's cases coexist with B1, and the oracle shares two admissibility errors with the model (N1).
- **SP-001**: evidence-only (one owner per fact; B1 (a) and §10.2's retirement rule state the closing of adverse findings twice, differently).
- **SP-002, FF-001**: evidence-only, not material.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 separates G1 document checks from G2-G4 runtime evidence and claims no execution it lacks. §31.4's R15 cases now discriminate the 3876473 siblings: standing lowering to the principal, refused re-integration, inadmissible continuations, revoked disposition, latched `P`, joint-invariant routing. They do not discriminate B1:

- the joint-invariant case expects the outcome that §10.4's retirement prevents in the common order;
- no case vetoes after the content moved;
- no case covers a no-item records-only lowering or a repair by a new item.

The lifecycle family is a real improvement: it now yields routes and checks I12, and every value-level case I probed agrees with the Manual. But it models no exits beyond "wait" and "coord", and two of its event admissibilities are wrong in the same way on both sides (N1). A green run therefore cannot show B1.

## Doctrine-realization map and O1

§29 maps all seven entrypoints. B1 touches three rows:

- the D4 row's "close each stage with affected regression; reconcile every obligation" (B1 (a): an obligation is reconciled away);
- the D2 row's "tolerances from accepted error semantics, never from a failing backend" (B1 (a), `SPEC_REVIEW` variant: an upheld finding of exactly that is retired by an unrelated specification review);
- the workflow row's explicit closure (B1 (c)).

These are the same defect seen from the map and need no separate repair. O1 (§0.5) is unchanged. The realized record, readers, routine questions, retention and marked surfaces are stated, all within the requested deliverable and none beyond it. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

Executed against the extracted candidate, or in the clone where stated:

- Blob identities above, by `git rev-parse` at the candidate. The model file's blob is `f1021d7258328a6b2b5aabff3b885a6dd6b1ab83`.
- `git diff --check 387647305b91a569493c73e180cf78f04b55c9e6 494c810017249d00967eda633334ba2987f7ff68`: exit 0. The delta is six files:
  - the Manual (9 hunks);
  - the closure map (3 lines);
  - the continuation handoff;
  - the model (+255/−118 lines);
  - the previous handoff and Review record, added.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the snapshot: 4 tests OK (routing and lifecycle structure only).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 bf2337285dfdaba5d535e73cf76af3d5b78978f0`: 73 files, 23,269 insertions, 1 deletion (that historical comparison only).
- `git diff --stat fad3ee41… 494c8100… -- orchestrator/docs/architecture.md source dist`: empty.
- PEM validation as above.
- Diagnostic model at the candidate, with `--mutations` semantics, run in parallel.
  - The driver was a scratch script, `$TMPDIR/ssds80-manual-review-494c810/scripts/par.py`, run with `python3 -I`. It imported the unmodified snapshot module in each worker of a `multiprocessing` pool and cleared and set `MUT` at the start of every job.
  - It ran `run_family(name, verbose=False)` for each of the six families (`CORE`, the three in `FAMILIES`, `GATE_BASIS`, `LIFECYCLE`) with `MUT` empty. Then, for each of the 46 entries of `MUTATIONS`, it set `MUT = {m}` and ran `run_family` on each family that mutation names, exactly as `main()` does: 54 jobs.
  - Results: 54 jobs, exit 0. Zero invariant failures in every base family, with these scenario counts:
    - transformation-review/acceptance/gate: 1,856,368;
    - equivalence-chain: 299,760;
    - completeness-cover: 37,600;
    - plan-coverage: 205,800;
    - gate-basis: 1,000;
    - obligation-lifecycle: 809,812.
  - All 46 mutations are caught in every family they name (48 mutation-family jobs). Single-invariant catches: `plan_supersession_current_only` by I4 only; `frame_acts_everywhere` by I5 only; `obligation_direct_only` by I8 only; `eligibility_support_tier_only` and `challenged_record_authors` by I7 only; every lifecycle mutation by I11, and `lifecycle_non_latched`, `lowered_becomes_ready` and `provisional_not_latched` also by I12.
  - `main()` itself was not called; the driver calls the same functions in the same configuration.
- A separate probe (`scripts/probe.py`) evaluated `lc_value` and `lc_oracle` on nine hand-built cases (N1).
- Governing owners read at `aaeaf8b`:
  - `source/roles/software-design/SKILL.md` (routing, review contract);
  - `architecture-and-design.md` (line 96);
  - `workflow-and-workplans.md` (lines 19, 96, 124, 131);
  - `evidence-evolution-and-dependencies.md` (line 153);
  - `concurrency-and-orchestration.md` (lines 60-65);
  - `convergence-and-cycle-economy.md` ("Active simplification trigger", line 62; "Review strategy after recurrence", line 89; family definition, line 25; review sufficiency, line 85);
  - PEM and testing owners, applied through the validator, the HAS and DS-001.
- Reviewed workplan at the Phase B candidate: §7.1-§7.4 (lines 1494-1541), §7.8-§7.10 (lines 1656-1765), and §21 items 1-27.
- Manual sections read in full:
  - §0.4; §4.3 (review and gate rows); §5.6-§5.7; §5.10; §6.7; §7.3;
  - §8.3 steps 6-9; §9; §10 (all); §11.4-§11.5; §12.4-§12.5; §13.7; §15.5-§15.7; §16.5; §17-§17.4;
  - §22.3; §23.6-§23.7; §31.3 (model text); §31.4;
  - closure map lines 87 and 298.
  - The rest was read by targeted search for latch, retire, lowered, re-dispatch, `SPEC_REVIEW`, joint invariant and prerequisite.
- The stakeholder record's SD-24 row and items 12-31.

Not verified:

- No production SSDS, real gate or runtime was exercised.
- B1 (b) depends on whether a `waits by design` `ADJUDICATE_DISAGREEMENT` is dispatched to the owner for its adverse answer. Either reading leaves an owner who disagrees with the peer no admissible answer, and neither routes the latched obligation to the principal. I did not construct a fourth reading.
- The handoff asked for the six drift classes across the whole Manual. I applied them to every statement of R15 and its consumers (§8.3, §10.2-§10.5, §12.5, §13.7, §15.5, §16.5, §22.2, §23.6, §31.3-§31.4, §32.3, closure map §5) and by targeted search elsewhere. I did not compare pairwise every concept the Manual states twice, so further drift outside these is possible.
- Earlier records' per-item closures were not replayed.

## Scientific checks

Method: one pinned architecture candidate; deductive counterexamples bound to exact owner text; a family-level recheck; structural tests; and the candidate's diagnostic with its prescribed mutations, plus a nine-case probe of its lifecycle oracle.

Material findings: B1 and N1-N6. None concerns a scientific observable, numerical method or realized scientific result. B1 (a)'s `SPEC_REVIEW` variant concerns whether SSDS keeps a decision owed after an upheld finding that a tolerance was widened to fit a failing backend. That is a governance consequence for how scientific evidence specifications are reviewed, not a scientific judgment about any tolerance.

**I produced, ran or reviewed no realized scientific results.**

Variants evaluated: one normative candidate. For B1, three sibling classes:

- (a) two orderings and two kinds;
- (b) two veto kinds and two dispatch readings;
- (c) four exit gaps;

and eleven controls that hold. Twenty-three out-of-matrix trajectory classes, overlapping rather than independent trials. One diagnostic configuration (6 base families, 46 mutations) and nine probe cases. The criterion was to find a material counterexample, not to select a favourable result.

No accepted project D1/D2 scientific authority was relied on for a consequential judgment, so no tension search was triggered. Gaps: real-owner execution, reader adequacy and operating costs.

## Common-mode note

The reviewer is of the **Claude family**, the same family as the Manual's author and as most earlier Manual reviewers. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. This reviewer was engaged as a fresh-context sub-agent launched by the authoring session. It did not receive the authoring conversation, but fresh context is not epistemic independence. Shared dependencies:

- the corpus;
- the inherited workplan and handoff framing (including the handoff's prompt to attack the state set and its exits, which directed the search);
- the prior Review records, read as hypotheses (3876473 option 1 is the source of the routing attacked here; successor retirement is the author's addition to it);
- the Git/Python toolchain;
- the diagnostic's event list, which the rule and its oracle share.

For the fifth consecutive round, this family's blocker entered through the previous same-family Review's recommended option or an addition made while realizing it. Same-family review of same-family repair directions remains a weak check here. A different-family check of B1 and of whichever option is chosen is advisable before G1, together with the stakeholder decision on whether R15 should exist (option 2).

## D4 statement

This Review authorizes **no D4**, cutover, architecture acceptance, product-scope extension or proposed default. The next steps are:

1. Put B1's options to the stakeholder (option 1 recommended, option 2 as the family-removing alternative).
2. Under the chosen option, define the exits of a lowered latched obligation as one closed set:
   - remove or condition successor retirement;
   - make a veto with no admissible owner answer stand;
   - name the deciding record's outcomes in §15.5;
   - reconcile §10.3, §12.5, §31.4, §32.3 and closure map line 298.
3. Add B1's discriminator to §31.4.
4. Correct the lifecycle model's `adjudicate_R` and `fail_E` admissibility and model the exits (N1).
5. Consider N2-N6.
6. Freeze a replacement candidate and obtain an independent Review, preferably a different-family one, before stakeholder G1 acceptance.

G2 still separately requires a reviewed shadow workplan and explicit stakeholder authorization.
