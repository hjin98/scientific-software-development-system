# Independent D3 Review — SSDS 8 Architecture Manual, candidate 47b9f77

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          47b9f7756510de36e902289f9dce35683ff7086c
    SCOPE:              whole proposed Manual, handoff scope (a)-(g); SD-42 and SD-43 confirmation (one judged
                        scope J; fifth named routing reopen trigger)
    MANUAL:             orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB:        b42f64a7ff21f80e812b5ee968a79163c8c97517 (verified at the candidate)
    CLOSURE MAP BLOB:   ec097a4e2d835a944239a82e64ee0d7fd0a817f2 (verified; review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at the candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    PUBLIC SOURCE:      aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml accepted_current 7.2.1)
    RECOVERY:           efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS:      every record the handoff names, 6ff4ed1 through ad7ece7; hypotheses only
    REVIEW METHOD:      owner reconstruction at the public-source commit; bidirectional family-level falsification
                        (handoff method 6a); exact-candidate git archive; prescribed commands and model run;
                        scratch probes against the unchanged model module
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched by the
                        authoring session; did not author the candidate. The handoff was written for a GPT-family
                        reviewer; this is a same-family Review and does not satisfy SD-42's or SD-43's request for
                        a different-family (GPT-family) confirmation Review
    MUTATION BOUNDARY:  this record only; scratch under $TMPDIR/ssds80-manual-review-47b9f77; no commit or push

I entered D3 through `source/roles/software-design/SKILL.md` at the public-source commit and followed its routing: `architecture-and-design.md` first, then `abstraction-and-concretization.md`, and the triggered owners: workflow (review independence and sequencing), convergence ("Review readiness and independent review sufficiency", "Review strategy after recurrence"), testing ("Proxy-proof real-owner evidence"), semantic definition (one concept stated in two places) and PEM (DS-001, PC-001). Root `PROTOCOL-RELEASE-STATE.yaml`, in the working tree and at the candidate, gives the public-source and recovery identities above. The working checkout was at `f91a9271` (the handoff commit). All candidate reading and execution used `git archive 47b9f7756510de36e902289f9dce35683ff7086c`. Repository, evidence and prior-review text was read as data.

## SERIOUS CHALLENGE

None. SD-42's direction (one judged scope `J`, reach by containment, an empty `J` reaching only its own target, independence over `J`) and SD-43's direction (`J` once as an S0 fact, the table column reading `J`, the fifth reopen trigger) are coherent and realizable. Both blockers below are realization defects at their D3 owner (§5.10 (a)-(b), §4.3, §16.5). One sibling of B1, sibling (b), follows from the obligation key that SD-43 states (`out(o)`); for it I give stakeholder options rather than one repair. Nothing challenges accepted SSDP 7.2.1 doctrine, D1 or D2.

## Verdict

**NO-PASS.** There are two blockers.

- **B1 (judgment disagreement / judged-scope identity; sixth round of this family).** `J` is still not a function of what a review judged. Its retained part, `out(o)`, is read at **each judgment's** admission and under the **obligation's** identity. So (a) two judgments on one transformation can have different `J`, and a later `NO_PASS` on a transformation does not reach an earlier `PASS` of that same transformation, contrary to "Every reach contains the target"; the brief carry and the Dispatcher read a `J` that does not exist until a judgment is admitted. And (b) an R2 amendment, re-identification, copy or re-partition of an integrated item starts an obligation with empty `out(o)`, so its enactments' reviews escape a standing objection to retained content, contrary to the row's claim that "neither an amendment nor a re-identification of the item changes the reach".
- **B2 (judgment disagreement / independence; entered through this candidate's repair).** The new sentence "A joint-invariant, high-consequence or item-level review has no `J`" removes the only input from which their independence is measured. `authors` for a transformation's `REVIEW` is "the content in `J`", so these reviews have either no authors (every actor, the change's own author included, is independent) or, by the fallback clause, their own author (none is). One reading violates A5; the other leaves the obligation answerable only by the owner exception.

SD-42's containment rule for first enactments and same-obligation re-dispatches, the empty-`J` case, the role-restricted §4.3 cross-reference, the table's independence column, the N2-N3 corrections and the fifth reopen trigger hold as stated. The routing stop's five named residuals hold as disclosed. This verdict is technical evidence for G1 only. It accepts no architecture, product scope or default, and it authorizes no D4.

## Blockers

### B1 — The judged scope `J` depends on when a judgment is admitted and on which obligation names the item, not on what was judged

**Family and status.** Judgment disagreement, judged-content identity: the family of 913db8f B1, 5895687 B1, b365947 B2, 085c979 B1 and ad7ece7 B1. **Open, material, non-local recurrence**, sixth round. One cause: `J`'s retained part is `out(o)`, a mutable state of a mutable identity, read at the judgment's admission. This is the item-31 drift class "a mutable identity versus what was judged" and "two places computing one thing" (the reach reads a per-judgment `J`; the brief carry and Dispatcher read a per-candidate one).

**Earliest owner.** Manual §5.10 (a)-(b), with §4.3 and §16.5. Workplan §21 items 3 (independence of each disposition kind) and 4 (basis composition per judgment kind).

**Owner text at the candidate.**

- §5.10 (a), line 822: `J` "is an S0 fact fixed at the judgment's admission: the post-state content `(u, rev(u, C))` of every unit of `Δ(X) ∪ out(o)`, with `out(o)` (§10.4) as it stands at that admission and empty before `o`'s first integration".
- §4.3, line 570: "for a review or conformance judgment of a transformation of an item obligation `o` after `o`'s first integration, `content` on every unit of `out(o)`".
- §5.10 (a), line 824 (Reach): "Every reach contains the target; reaching further is what keeps amendment, rebase, re-dispatch, a new run or a composition of judgments from escaping an objection."
- §5.10 (b), line 838, `REVIEW` of a transformation: reach is "every transformation whose judgment's judged scope `J` ... contains the adverse judgment's `J` at the same content ... when that `J` is nonempty ...: what a review judged is its `J`, so neither an amendment nor a re-identification of the item changes the reach, a re-dispatch that keeps rejected content (partially or with an empty change) is reached".
- §10.4, line 1319: "An item obligation's identity is its item and the prose and fixed fields of its accepted revision (§13.4): an R1 tightening keeps it, and an R2 amendment derives a new obligation"; "`out(o)` is the set of units its integrated enactments changed"; "A **pending candidate** of `o` is the candidate of a task result admitted for it and neither integrated nor refused."
- §16.5, line 1781: the review brief carries "every standing transformation `NO_PASS` or `NONCONFORMANT` whose reach includes the candidate"; line 1783: the Dispatcher "selects a transformation reviewer independent of `authors(J)`".
- §0.3 R9 (line 94): an adverse judgment, "while it stands, vetoes every passing judgment of its kind on the same target, whatever their order".
- SD-43 (stakeholder record item 39, verbatim): "Fix B1 as the review proposes (J once as an S0 fact at admission; out(o) empty before first integration; §4.3 cross-reference by role; table column)". The ad7ece7 record's proposal read: "`J` = the post-state `(u, rev(u, C))` of `Δ(X) ∪ out(o)`, with `out(o)` taken **at the enactment's issue** and empty before `o`'s first integration". The candidate reads `out(o)` at the judgment's admission instead.

**(a) Sibling: admission time. Two judgments on one target have different `J`.**

Trajectory (a conforming implementation, every step admissible):

1. Item `I`, obligation `o`. Implementer task 1 produces `X1` (changes `u` to `u1`). Reviewer `A` passes `X1` (answering `REVIEW(X1)`); a peer `B` records `NO_PASS`. `REVIEW(X1)` is `REFUSED`, `ADJUDICATE_DISAGREEMENT` is derived, and the pre-integration route for an in-scope NO-PASS dispatches the next iteration (§10.4 ordinary routes; §13.7 budgets).
2. Task 2 produces `X2` (changes only `v` to `v2`). Its result is admitted, conformance is `CLEAN`, and reviewer `C` passes it. `o` has not integrated, so `J(C) = {(v, v2)}`. `X1`'s task result is still admitted and neither integrated nor refused, so `X1` and `X2` are both pending candidates.
3. The owner adjudicates the disagreement on `X1` for `A`, superseding `B`'s `NO_PASS`. `A`'s pass is unvetoed, the predicate holds on `X1`, the Dispatcher submits its integration (§11.5 step 3) and `X1` integrates. Nothing in §8.3 step 7 refuses it: its obligation is derived and its enactment has no earlier integration. Now `out(o) = {u}`.
4. A later admitted item `K` changes `u` to `u5`. `out(o)` has moved, `A`'s output entry no longer holds, and `o` is `OPEN`. Route 3 applies because `X2` is a pending candidate, so `X2` keeps its ordinary routes rather than being re-dispatched (§10.4). `X2` rebases cleanly (it changes only `v`). `C`'s entries carry no `out(o)` unit, because `C` was admitted before the first integration, so they stay satisfied and no `REVALIDATE` is derived.
5. A human reviewer `D` records a `NO_PASS` on `X2` with a finding about `v2`. Adverse judgments are always admitted (§8.3 step 7). `D`'s judgment is admitted after `o`'s first integration, so §4.3 requires `out(o)` entries and `J(D)` contains `(v, v2)` and a `u` entry.
6. By the table, `D` reaches a passing judgment only if its `J` contains `J(D)`. `J(C) = {(v, v2)}` does not. So `C`'s pass of `X2` is not vetoed, no `ADJUDICATE_DISAGREEMENT` is derived, and `REVIEW(X2)` is not `REFUSED`. `X2` integrates on `C`'s pass. After integration, route 4 reads only an author's or owner's adverse review or an upheld peer veto, and `D` is neither. So route 2 discharges `o` against a standing `NO_PASS` on the very transformation it relies on.

By "Every reach contains the target" and R9, `D` vetoes `C`. The two statements in the one owner give opposite discharge values. The violated owners are §10.4's "∃ a passing judgment never discharges against a standing objection, in either order of admission", invariant (g)1, workplan §7.4 discharge as R9 restates it, and `architecture-and-design.md`: "If two current architecture owners materially disagree about one concept, file order, route priority or 'latest' cannot resolve the conflict". The trajectory needs two pending candidates of one obligation, which the Manual admits and which §32.3 residual (d) already names for routing. The defect here is the reach, which SD-41's bounded stop does not cover.

Further consumers of the same per-judgment value:

- **Brief carry (§16.5).** The default review carry selects objections "whose reach includes the candidate". The reviewer's `J` is fixed only when its judgment is admitted, so the brief is built from a value that does not exist yet and can change before admission (an integration of `o` in between).
- **Dispatcher selection (§16.5).** "Independent of `authors(J)`" names the same not-yet-fixed value.
- **§10.4 (line 1319)** still says that after integration `o` relies on "the review of a re-dispatched enactment carrying `content` on every unit of `out(o)`". In step 5 it relies on `C`'s review, which carries none, because it was admitted before the first integration.

I executed the trajectory's core against the candidate's own `review-scope` family in scratch. I added two shapes for one transformation (`{v: 1}` with `out(o)` empty, and with `out(o) = {u: 1}`). `rs_reach` returns `False` for the later adverse against the earlier pass. The family stays green with the shapes added, because its oracle reads the same `out_before` (N1).

**(b) Sibling: obligation identity. A re-identified, copied, amended or re-partitioned integrated item escapes.**

Trajectory:

1. Plan `P`, item `I`, obligation `o`. `X1` changes `u` to `u1`, an independent pass follows, and `X1` integrates. `out(o) = {u}`.
2. `X1`'s reviewer, an authenticated human, reassesses it as `NO_PASS` (route 1 supersession of its own pass), with an in-scope finding "`u1` violates clause c". Under `o`, every re-dispatch keeping `u1` is reached: an empty one has `J = {(u, u1)}`, one changing only `v` has `J = {(u, u1), (v, v3)}`. This is the guarantee SD-42 added.
3. Instead, the principal amends the plan: removes `I` and adds `I'` with byte-identical prose and fixed fields (a topology change, so a whole-plan R2 acceptance, §11.4), or copies `I` into plan `Q`. `o` is no longer derived. `I'`'s obligation `o'` has never integrated, so `out(o') = ∅`.
4. `o'`'s first enactment `X3` changes only `v`, or nothing, and keeps `u1`. `J(X3) = {(v, v3)}` or `∅`. Neither contains `{(u, u1)}`, so a peer's pass of `X3` is not reached, and `X3` integrates and discharges `o'`.
5. For the copy into `Q`, `X3`'s brief does not carry `X1`'s finding either. The default carry is by reach, and the re-review carry is by the plan subject (`P`). The plan acceptor's brief carries only `PLAN_ACCEPTANCE` rejections.

The same holds for an R2 amendment with changed prose. It holds for a re-partition (§13.7) that replaces an integrated, reopened part by new part obligations, which are keyed on the `PARTITION` record. In each case the table's claim "neither an amendment nor a re-identification of the item changes the reach" is false for retained content. That claim restates stakeholder record items 28-29 (SD-33, SD-34: "re-identifying or copying an item does not escape"), which SD-42 extended to retained content. A8 ("a material finding survives to its owner") fails for the cross-plan copy: the in-scope finding loses its route with `o`, and no judge is shown it. The same probe confirms the cut: `first_u1` reaches `{v: 1}` with `out(o) = {u: 1}` and `{}` with `out(o) = {u: 1}`, but not the same transformations with `out(o)` empty.

**Minimum repair direction.**

- **(a), narrowing, no mechanism beyond one recorded value.** Make `J` a function of the transformation, as the ad7ece7 proposal SD-43 adopted reads it: `out_X` is `out(o)` as it stands when `X`'s task is issued (or when `X`'s task result is admitted, which fixes `X`, §11.5), and is empty before `o`'s first integration. Machinery records it with the task envelope, as it records `rid`, and Admission checks it. Every judgment on `X`, the §16.5 carry and the Dispatcher's selection then read one value, and every reach contains its target. §4.3's clause becomes "for a review or conformance judgment of a transformation whose recorded `out_X` is nonempty". §10.4's "re-dispatched enactment" wording follows.
- **(b), stakeholder options (non-local; SD-43 keys `out(o)` on the obligation):**
  1. *Disclose, no mechanism.* Correct the row's claim to say that an R2 amendment, re-identification, copy or re-partition of an integrated item starts an obligation with empty `out(o)`, whose enactments' reviews a standing objection to retained content does not reach. Carry such an objection into the first review brief of the new obligation, in any plan, as history. Name it in §32.2-§32.3.
  2. *Key the retained part on what was judged, small mechanism.* `out_X` is the units changed by every integrated enactment of any item obligation whose item revision has the same prose and fixed fields as `X`'s, in any item or plan. This is SD-33's content key, already used by the plan row and by `PLAN_ACCEPT` carries. R2 amendments with changed prose stay new targets, as for plan rejections, and are then disclosed as in option 1.
  3. *Keep the claim and extend `out(o)` through a declared item lineage.* This needs a plan-item lineage the Manual does not have, so it is the most mechanism.

  This review recommends option 2 for re-identification and copies and option 1 for genuine R2 amendments and re-partitions. Whichever is chosen, the row's "so" clause must state the result.

**Required discriminator.**

- At G2 and G3, through the real Derivation and Admission:
  - a peer's `NO_PASS` on a pending candidate admitted after another enactment of its obligation integrated vetoes that candidate's earlier pass and derives `ADJUDICATE_DISAGREEMENT`; the candidate does not integrate on that pass;
  - the review brief and the Dispatcher's independence selection read the same `J` the judgment will carry;
  - a re-identified or cross-plan-copied integrated item whose first enactment keeps rejected retained content either is vetoed (option 2) or shows the objection in its first review brief, with the residual listed (option 1).
- In the diagnostic model, `review-scope` must separate the transformation from the judgment. Give each judgment its own admission time, and give each shape an obligation identity that an amendment, re-identification or re-partition can change. Its oracle must assert that every adverse judgment reaches every passing judgment on its own target, without reading `out_before`. At the candidate, both added cases stay green (N1).

### B2 — Reviews without `J` have no independence measure

**Family and status.** Judgment disagreement, independence (the family of 29da56e B1, 6b986de B1 and 085c979 B1's independence part). **Open, material, entered through this candidate's repair** of ad7ece7 B1's last repair bullet ("Say explicitly what `J` is for joint-invariant, high-consequence and item-level reviews, or that their reach is by target only"). A clean local defect, but at the same drift class: removing a value one consumer needed (reach) also removed it from another consumer (independence).

**Earliest owner.** Manual §5.10 (a) `authors(x)` and the per-kind table's `Requirement; authors of` column, with §9.2 and §13.7. Workplan §21 items 3 and 9 (joint invariants).

**Owner text.**

- §5.10 (a), line 822 (new): "A joint-invariant, high-consequence or item-level review has no `J`: it reaches, and is reached, by its exact target only".
- §9.2, line 1226: a joint-invariant obligation is "a `REVIEW` of the integrated result against the invariant"; §4.3's `REVIEW, CONFORMANCE on X` row gives its entries, so its target is `id(X)` and it is a `REVIEW` of a transformation (§3.4: `REVIEW` targets "transformation `id(X)` or subject triple").
- §5.10 (a), line 826: `authors(x)` "for a transformation's `REVIEW` or `CONFORMANCE`, the content in its judged scope `J`"; otherwise "for any other record, `authors` of its target, recursively, or its own author where its target is not a record or content". Line 827: "every review ... judgment" carries a requirement. Line 828: independent only when "its lineage is disjoint from `authors(x)` for its target `x`; for an authenticated human, when the human is not in `authors(x)`".
- §5.10 (b), line 838: `REVIEW` of a transformation, "Requirement; `authors` of": "yes; the content in `J`".
- §16.5, line 1783: the Dispatcher "selects a transformation reviewer independent of `authors(J)`".
- Workplan A5 (line 833): "no actor reviews or accepts its own work"; A9 (line 837): "Reviewer independence is constructed, not requested".

**Trajectory.**

1. An authenticated human `H` executes item `I`'s implementer task. `X` changes unit `u`, which lies in a declared joint invariant `i`'s scope. An independent reviewer passes `X`, and `X` integrates. `JOINT_INVARIANT(i, k)` is derived (§10.2).
2. `H` takes the joint-invariant review, a qualified R2 reviewer in a fresh context (§16.5 only requires a context distinct from the authoring task's).
3. The literal reading: the review is a transformation `REVIEW` whose `authors` is "the content in `J`", and it has no `J`, so `authors = ∅`. `H` is "not in `authors(x)`", the review is not `nonind`, and `H`'s `PASS` answers `JOINT_INVARIANT(i, k)` on `H`'s own change. A5 is violated. The Dispatcher's "independent of `authors(J)`" also selects nothing out.
4. The fallback reading: the clause for "any other record" gives "its own author where its target is not a record or content", if a transformation identity is read as neither. Then no reviewer is ever independent. The obligation is answerable only through the owner exception, so every joint-invariant and high-consequence review becomes an owner-exception review. That is a liveness and independence-quality failure the Manual does not state (compare §5.10 (g)4 and the I10 liveness property the Manual adopts for gates).

At ad7ece7 these reviews had a `J` by formula, so the defect is new in this candidate. The item-level review of a partitioned item (§13.7) has the same gap. Its target is not stated anywhere, though the new sentence reaches "by its exact target only" (N4).

**Minimum repair direction (narrowing, no mechanism).** State what these reviews' independence is measured over, separately from their reach. For a joint-invariant or high-consequence review: the post-state content of the units of `Δ(X)` inside the scope or on the marked surface, which are exactly the output entries §4.3 requires of it. For an item-level review: the parts' latest integrated outputs. Add them to the `authors(x)` clause and the table's column ("the content in `J`, or for a review without `J`, the content its output entries name"), and let §16.5's selection read the same.

**Required discriminator.**

- At G2 and G3, through the real Admission:
  - the authenticated human author of `X` recording the joint-invariant `PASS` on `X` is `nonind` and does not answer `JOINT_INVARIANT(i, k)`;
  - a reviewer who authored none of `Δ(X)`'s in-scope content is independent;
  - the same pair for a high-consequence review and for an item-level review of a partitioned item.
- The `review-scope` family should include a review without `J`, with R5 asserted for it.

## Non-blocking findings

**N1 — The `review-scope` family still cannot see either B1 sibling (DS-001).**

- Its shapes are transformations with one fixed `out_before`, so "a judgment admitted before and after an integration of `o`" and "an obligation identity change" are unrepresentable.
- Its oracle `rs_oracle_scope` reads the same `out_before`, so with the B1 shapes added the family stays green (scratch probe).
- Its `kind` labels (`retained`, `contract`, `governing`) are the model's own, not §7.3's roles: §7.3 gives all three the role `context`. So "selects `J` from it by role" (§31.3) selects by the model's taxonomy, which is the Manual's unit-membership rule, not §7.3's role function.
- It omits the joint-invariant scope-context entries that §31.3 says "the whole row" includes, has no conformance judgment and no review without `J`, and its comment cites an `RS_BEFORE` that does not exist.
- §31.3 is otherwise honest that the family is "independently of the reach rule but not of the Manual author's reading of `J`".

**N2 — ad7ece7 N4 persists, now explicit.** A joint-invariant or high-consequence review targets `id(X)`, and by the new sentence it "reaches, and is reached, by its exact target". So an adverse joint-invariant review vetoes the item's own passing review of `X`. One finding then derives the `REFUSED` `COORDINATE(plan)` (§10.4), an item route (route 4 or 6) and, for a peer, `ADJUDICATE_DISAGREEMENT`. That is several obligations for one finding, and a re-dispatch of an item whose contract the finding may not concern. State it in §32.3, or key these reviews on a target of their own (the invariant and change), when B2 is repaired.

**N3 — Review identifiers remain in normative text.** §32.3 cites "Manual Review `b365947` B1" and "Manual Review `ad7ece7` B2", and the R15 row's rationale opens "82d618c B1". Closure map §7 says "The Manual's normative text no longer cites Review identifiers." Move them to closure map §7, or correct the map's claim.

**N4 — The item-level review's target is unstated.** §13.7 derives "an item-level review of the integrated result ... over the parts' latest integrations", and §5.10 (a) now says it reaches "by its exact target only", but no section names that target (§3.4's `REVIEW` row allows a transformation or a subject triple). State it with B2's repair.

**N5 — Residual (e)'s wording omits the pending-candidate mask.** An out-of-scope `NO_PASS` on the latest integrated enactment admitted while a pending candidate exists is masked by route 3. It becomes (e) once the candidate integrates, or route 4 again if it is refused. So it is delayed, not lost, and is within the spirit of (e). Name it in (e) for completeness.

**N6 — Stale "re-dispatched" wording.** `authors(x)` (line 826: "retained outputs of a re-dispatched enactment included") and §10.4 (line 1319: "the review of a re-dispatched enactment carrying `content` on every unit of `out(o)`") still use the term that §4.3 and §5.10 (a) replaced by "after `o`'s first integration". §4.3's new clause also literally covers a joint-invariant review of a transformation of `o` after its first integration, then says "these retained-unit entries carry its judged scope `J`" of a review that, by §5.10 (a), has none. Both resolve with B1 (a) and B2.

## Closure audit

**Method.** For each workplan §21 item (1-27) and its subordinate clauses I located the Manual section the closure map names and checked that it decides rather than routes. I read in full §0.3-§0.4, §4.1-§4.3, §5.10, §7.3, §8.3 steps 3 and 7, §9.2, §10.2-§10.4, §11.4-§11.5, §13.7, §16.5, §29.3, §31.3, §31.5, §32.2 and §32.3. For other sections I read headings and the passages the map cites. The candidate delta touches only §0.3 (R9 and the SD range), §4.3, §5.10 (a)-(b), §16.5, §29.3, §31.3, §31.5, §31.9, §32.2 and §32.3. The §16.2 rows (both tables, §26.4) are unchanged since 085c979, and I found no gap in their dispositions.

**Items not substantively resolved at this candidate:**

- **Item 3** ("the decision class and independence of each disposition kind"): the independence of joint-invariant, high-consequence and item-level reviews is undefined (B2). For transformation reviews, `J` is not one value per target (B1 (a)).
- **Item 4** ("basis composition and mode assignment per judgment kind"): §4.3's retained-unit entries depend on the judgment's admission time and the obligation's identity (B1).
- **Item 9** (joint invariants): the joint-invariant review's independence (B2).
- **Items 7 and 26** (obligation rules; routing): accepted by SD-41's bounded stop with five named residuals, (e) now among them. I found no routing state outside them. B1 (a)'s trajectory passes through a two-candidate state that residual (d) names for routing, but its defect is in the reach.

None found elsewhere. This is a bounded semantic-review result over re-read text, not proof of exhaustive adequacy. Material decisions remain distinguished from `[delegated]` D4 choices. I found no new over-specification: the delta adds no component, record kind or persistent surface.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1-R8, R10-R12 | Sound as previously assessed. Their text is unchanged since ad7ece7, and I found no trajectory against them in this round (spot re-read in §0.3, §5.2, §7.3, §8.3, §10.2). |
| R9 | Sound in mechanism (veto by existence on reach, four routes, `REFUSED`). Its summary sentence is now consistent with SD-42. Its "vetoes every passing judgment of its kind on the same target, whatever their order" is contradicted by the per-judgment `J` (B1 (a)). |
| R13 | Sound as an extension of the reviewed independence rule to every route that ends an objection. Its single `authors(x)` function has no value for reviews without `J` (B2). |
| R14 | The one reach rule is sound, and the SD-42/SD-43 containment is sound as a rule over a per-transformation `J`. Its definitional input is per-judgment and obligation-keyed (B1). The cost list now includes SD-42's independence cost. |
| R15 | The step 8 narrowing is sound and keeps the workplan's purpose. The single route statement in §10.4 is accepted by SD-41's bounded stop. The out-of-scope route's restriction to the latest enactment is now disclosed as residual (e) (SD-43), which is the treatment the stakeholder chose for that narrowing of workplan §7.10. |

## Re-verification of earlier findings (family level)

I re-derived the latest rounds at the owners. I treated older families through closure map §7 and the model's mutations as hypotheses: the model has 46 mutations, each naming the Review whose defect it re-introduces (see "What was verified" for which were caught). Where I did not independently re-derive a finding, I say so.

| Prior findings | Disposition at 47b9f77, with basis |
|---|---|
| **ad7ece7 B1 (a)** (table column) | **Closed.** Both rows read "yes; the content in `J`" (line 838-839). |
| **ad7ece7 B1 (b)** (`J` equated with every §4.3 entry) | **Closed.** §5.10 (a) names the carrying entries (outputs of `Δ(X)`, retained `out(o)` units) and excludes before-images, the contract item, the governing closure and scope context; §4.3 gives conformance the same `out(o)` entries. The `judged_all_entries` mutation is caught. |
| **ad7ece7 B1 (c)** ("re-dispatched" undefined; state of `out(o)`) | **Partly closed.** §4.3 and §5.10 (a) now key on "after `o`'s first integration", with `out(o)` "as it stands at that admission". That answer makes `J` per-judgment (B1 (a)), and the old term survives in `authors(x)` and §10.4 (N6). |
| ad7ece7 B1 last bullet (reviews without a `J`) | Realized as "no `J`; exact target only", which opens B2 and makes N2 explicit. |
| **ad7ece7 B2** (out-of-scope NO-PASS on a non-latest enactment) | **Residual, as SD-43 directs.** Named as trigger (e) in §32.3 and §31.5, and §29.3's E0 claim corrected. Disclosed honestly; the pending-candidate mask is worth naming (N5). |
| ad7ece7 N1 | Partly closed: the family transcribes the row and the description is accurate about its shared reading; the B1 siblings are outside it (N1). |
| ad7ece7 N2 | Closed: R9 (line 94), §32.2 (lines 2758, 2761), "SD-11 to SD-43" (line 102), the §5.10 heading, and the closure-map "the the" typo are corrected. |
| ad7ece7 N3 | Closed: §32.2 (line 2753), §32.3 (line 2779), §31.9 (line 2714) and §16.5 (line 1783) state or measure the cost. §16.5's selection reads a value that is not yet fixed (B1 (a)). |
| ad7ece7 N4 | Open, non-blocking (N2 here). |
| ad7ece7 N5 (085c979 N1-N4) | Unchanged: N1-N3 closed, N4 a later-gate question. |
| **085c979 SC-1** | Disposed by SD-42; the empty-`J` case reaches only its own target (`review-scope` R4 green; `adverse_changed_units` caught). |
| **085c979 B1 (a)-(b)** | Closed for one obligation's first enactment and same-obligation re-dispatches. Reopened for two-candidate and identity-change trajectories (B1). |
| **b365947 B1 (a)-(d)** | Residual, as disclosed (§32.3, §31.5). Not re-litigated. |
| **b365947 B2 (a)-(b)** | Closed within one obligation; (c) is now residual (e). |
| b365947 N1-N5 | As at ad7ece7: closed. |
| **eb86a71, 093164f, 8f4e75d, f185036 B1 and N items** | Held at family level. There is one ordered route list in §10.4 that §4.1, §8.3, §10.2, §11.5, §13.7 and §15.5 point to; no post-integration `REVALIDATE` of an item obligation's review or task result; item identity is stated; the fence route ends by `AMEND` or `DECLINE`. The routing family is green over 38,160 cases, and its 7 mutations are caught. Its unmutated section claims remain empty by design (stated in §31.3). The residual is the five named triggers. |
| **c4e8de7, 494c810, 3876473, 3940dbc, c77447b, 095ce55 B1 and N items** | Closed by removal (SD-36). No latch, lowered state, retirement, line, reference set or `RESOLVED_BY` mechanism remains. The text is unchanged here since ad7ece7's search. |
| **82d618c B1, N1-N7** | Closed. Step 8 reads only the required `ev`/`qual` of affected obligations. |
| **edabd81 B1-B2, N1-N7; 653e88c B1, N1-N4; d94a293 B1, N1-N3** | Held. The gate-basis family (1,000 cases) is green, and its 3 mutations are caught. |
| **913db8f B1, 5895687 B1 and N items** | Held for changed-unit content: there is no item key in the review reach. The SD-42 extension to retained content reintroduces an identity dependence through `out(o)` (B1 (b)). |
| **4c52205, both e548472, d6734c4, 83a82df, 0d2b35e, 34803df, bf23372, a6ed164 and their N items** | Held at family level (plan row unchanged: common-tightening claim, route-3 relief, whole multi-item carry; equivalence chains in either direction for reach; completeness by union). The plan, equivalence and completeness mutations are caught in the run below. I did not re-judge each claim-column row beyond spot checks (§5.10 (g) admits that the oracle shares that column). |
| **6b986de, 29da56e, 51070e5, 9e5a763, 051cce3, 63ddf91, f03b15e, 61cd09b, 362af9f** | Held, with B2 as a new hole in the one `authors(x)` function. Two enforcement points, exact-target supersession, per-target relief, the gate veto by gate and triple in any run, and the cutover carrier rule are unchanged. |
| **f22b4dc, both b46c250, f7419d5, 575dc78** | Held (the acting rule, the enactment unit, one integration per enactment, the `gterm` minimum). |
| **5c55d4b, 27ef339, 0b6c4fa, a18b544, e9e6e9f, e2154ac, 3540d98, 798b2b4, 71cf9b3, 86ab683, 1ffbbf0, 53669a5, d837363, cc005db, c6da678, b595f2c, 6ff4ed1** | Not touched by the ad7ece7 to 47b9f77 diff. I accepted the ad7ece7 and 085c979 records' family-level dispositions as hypotheses and spot-checked §0.3 R1, R10 and §8.3 step 7 against them. No regression found. Not re-derived line by line. |
| **Phase B §3 closures and N1-N4** | The parent contract is unchanged, and §6 is untouched by this delta. N2's completeness polarity and SCC clamp keep their stated discriminators (§31.3), N1 provenance stays open (§32.4), and N3 and N4 are later-gate questions. |

**Convergence.** The judged-content family has produced a blocker in six successive rounds: 913db8f, 5895687, b365947 B2, 085c979 B1, ad7ece7 B1 and B1 here. Each entered where "what a review judged" was given a second input that is not the judged content: item identity, then changed units only, then §4.3's whole entry set, and now admission time and obligation identity. Under the convergence owner's "Review strategy after recurrence", the family-level cause is that the retained part of `J` is not content. Option 2 of B1 (b), with B1 (a)'s per-transformation recording, defines it by content once. I stopped discovery in the family after enumerating every consumer of `J`: reach, relief, supersession, independence, both §16.5 carries, the Dispatcher and §10.4 reliance. Further sibling search would duplicate the G2 discriminator work.

## Out-of-matrix trajectories attempted

Each obeys every local rule. "Held" means the governing invariant was not violated.

- **Defeated:**
  - B1 (a): a later peer `NO_PASS` on a pending candidate does not reach that candidate's earlier pass after another enactment of its obligation integrated;
  - B1 (b): re-identification, cross-plan copy, R2 amendment or re-partition of an integrated item drops retained content from `J`;
  - B2: the human author of a change passes its joint-invariant review.
- **Held:** within one obligation, an adverse first-enactment `J` reaches every later re-dispatch keeping the rejected content, empty or partial, and none that repairs it (`review-scope` R2-R3; my own enumeration of the ad7ece7 B1 cases).
- **Held:** before-images, the contract item and governing entries are outside `J`, so an R1 tightening or a governing change does not let a re-dispatch escape, and a repair is not vetoed by its own before-image.
- **Held:** an empty `J` (an empty first enactment) reaches only its own target and cannot shield a nonempty adverse review.
- **Held:** stratification. `J` reads S0 facts only (integration entries and envelopes), and `stands⁻`, `vetoed` and `relieved` read S0/S1 only. Fixing `J` per transformation (B1's repair) keeps that.
- **Held:** relief and supersession stay on exact targets. A reliever's pass on a reached target judges that target's own `J`. Invariant (g)4 holds where the veto bites, given B1 (a)'s repair.
- **Held, by design:** a trivial edit to rejected content (`u1` to `u1'`) escapes the veto (R9's new target). §16.5's carry is the safeguard.
- **Held, residual:** the five named routing residuals. An out-of-scope finding on a non-latest enactment is listed (e). Its masked form while a candidate is pending resolves into (e) or route 4 (N5).

## Minimum architecture and capability transfer

The delta adds no component, record kind or persistent surface. B1 (a)'s repair records one value per task envelope (mechanism of the `rid` kind). B1 (b) option 1 adds none, and option 2 changes a definition without adding state. B2's repair is definitional. The Architecture 1.6.0 supersession (§26.4) and the version-bound Core are unchanged: `orchestrator/docs/architecture.md` (blob `39e6de72`), `source/` and `dist/` are byte-identical to `fad3ee41` at the candidate. PC-001 holds. No capability an owner requires is dropped by SD-43. The joint-invariant review's independence capability (A5, A9) is lost under the literal reading (B2).

## Qualification-design adequacy

- **Real owners.** §31.3-§31.5 list the SD-42/SD-43 discriminators and the five routing residuals at their real owners (Derivation, Admission, Dispatcher, briefs). They are unexecuted and correctly marked G2/G3.
- **Model.** Every family is green and every mutation is caught. But the `review-scope` family cannot express B1 (a) or (b) (N1). The core family's objector is still a first enactment, as §31.3 states. No family has a review without `J` (B2). A green run therefore coexists with both blockers, the DS-001 pattern the convergence owner warns of. §31.3's description is accurate about the family's shared reading, apart from "whole row" and "by role" (N1).
- **Additions needed.** The B1 and B2 discriminators above.
- **Claims.** Nothing is claimed executed that is not.

## Doctrine-realization map and O1

- **Doctrine map.** §29.2-§29.6 map every 7.2.1 entrypoint duty E0-E3. There are seven entrypoints: four roles and three specialists. I spot-read §29.2 and §29.3 against them and read the D3 role's text in full. The only changed row is §29.3's findings row, which now limits its E0 claim to the delegate floor for `scientific = APPLIES` contracts and names residual (e). That correction is accurate. The workflow duty "independent review" for joint-invariant reviews is weakened by B2.
- **O1.** §0.5 is unchanged and adequate. It covers the realized record, readers, routine questions, the marked surfaces (none beyond the deliverable) and the realized-record architecture.

## What was verified and how

- **Snapshot.** `git archive` of the full candidate SHA. The Manual blob (`b42f64a7`), closure-map blob (`ec097a4e`) and workplan blob (`91bde236`) match the handoff.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- **Whitespace.** `git diff --check ad7ece7 47b9f77`: clean (exit 0).
- **Earlier diff stat.** `git diff --stat fad3ee41 bf233728`: 73 files, 23,269 insertions, 1 deletion.
- **Frozen surfaces.** `git diff --quiet fad3ee41 47b9f77 -- orchestrator/docs/architecture.md source dist`: unchanged (exit 0).
- **Diagnostic model.** Run as its seven families and 46 mutations in parallel, by importing the module's `run_family`/`MUTATIONS`/`MUT` in a scratch runner, as the handoff permits; the core, `review-scope` and every other family were included. Every unmutated family is green: core 2,944,064 scenarios; equivalence-chain 299,760; completeness-cover 37,600; plan-coverage 205,800; gate-basis 1,000; obligation-routing 38,160; review-scope 160. All 46 mutations were caught by at least one invariant, over 48 mutation-family runs (two mutations touch two families each). This includes `judged_all_entries` (R1-R5) and the routing family's 7 mutations. A green run shows only the modelled properties (DS-001; N1).
- **Scratch probes.** Executed against the unchanged module: the B1 (a) and (b) shapes. `rs_reach` returns `False` for the later adverse against the earlier pass on one transformation. It returns `False` for `first_u1` against a `v`-only or empty first enactment of a re-identified obligation, and `True` for the same transformations under the original obligation. The family stays green with the shapes added.
- **Reading.** The ad7ece7 to 47b9f77 diff of the Manual, the closure map and the model; stakeholder items 38-39 and the SD-41 to SD-43 rows verbatim; the ad7ece7 record; and the owners cited above at `aaeaf8b`.

What I could not verify:

- No runtime, G2 or G3 evidence.
- I did not re-derive the oldest families line by line (the re-verification table says where).
- I did not independently re-judge every claim-column row.
- I did not exhaustively audit §29 against every entrypoint duty.

## Scientific-checks answers

- **Material findings:** B1, B2 and N1-N6 above. None concerns scientific or numerical meaning.
- **Realized results:** I produced, ran and reviewed no realized scientific results. The model runs and probes are diagnostics of written rules. Null envelope: SSDS runtime behavior, real repositories and G3 measures were unexamined.
- **Variants:** I evaluated two readings of when `out(o)` is read (the judgment's admission, as written, against the transformation's issue, as the ad7ece7 proposal adopted by SD-43 reads it) and two readings of a review without `J`'s `authors` (empty set; own author by the fallback clause). The criterion was agreement with SD-42/SD-43's text, A5 and the reach and independence discriminators. I executed one modified variant of the `review-scope` shape set in scratch.
- **Tension search:** I relied on no accepted D1/D2 authority for a consequential judgment, so no tension search was needed.
- **Gaps:** as listed under "What I could not verify".

## Common-mode note

- **Family.** This reviewer is of the Claude family, the Manual author's family. The handoff was written for a GPT-family reviewer, and this record does **not** satisfy SD-42's request for a different-family confirmation Review or SD-43's request for a GPT-family Review; one remains owed. The earlier reviewers of 3540d98, the different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472, d94a293 and 085c979 Reviews and the Phase B workplan Review were of the GPT family; the others, ad7ece7 included, were of the Claude family.
- **Engagement.** I was engaged as a fresh-context sub-agent launched by the authoring session. Fresh context does not establish epistemic independence.
- **Shared dependencies.** I share the corpus, the inherited workplan framing, the prior Review records (read as hypotheses), the model family of the author and of the ad7ece7 reviewer whose proposal this candidate realizes, the diagnostic model and the toolchain. Both blockers are of a kind a same-family reviewer can miss as well as find, which is why the different-family confirmation stays owed.

## D4 statement

No D4 is authorized. This record is G1 technical evidence only: it accepts no architecture, product scope or default value. Acceptance of the Manual belongs to the stakeholder after a Review with no surviving blocker.
