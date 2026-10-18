# Independent D3 Review — SSDS 8 Architecture Manual, candidate e810508

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          e810508ad5a5d244616f2e9dc7e00f3e297151c6
    SCOPE:              whole proposed Manual, handoff scope (a)-(g); SD-42 to SD-44 confirmation (retained
                        units recorded at issue and keyed on prose and fixed fields; independence of
                        integrated-result reviews; the routing stop and its five named triggers)
    MANUAL:             orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB:        4b7971886d4ea4218195a88d5074d21807250b3a (verified at the candidate)
    CLOSURE MAP BLOB:   f08749492a22c0278b91dfd9730fb34a7bb10a8a (verified; review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at the candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    PUBLIC SOURCE:      aaeaf8b6b2121b9fb8aba31917c8265649c43954 (PROTOCOL-RELEASE-STATE.yaml accepted_current 7.2.1)
    RECOVERY:           efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS:      every record the handoff names, 6ff4ed1 through 47b9f77; hypotheses only
    REVIEW METHOD:      owner reconstruction at the public-source commit; bidirectional family-level falsification
                        (handoff method 6a); exact-candidate git archive; prescribed commands and model run;
                        scratch probes against the unchanged model module
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched by the
                        authoring session; did not author the candidate. The handoff was written for a GPT-family
                        reviewer; this is a same-family Review and does not satisfy SD-42's, SD-43's or SD-44's
                        request for a different-family (GPT-family) confirmation Review
    MUTATION BOUNDARY:  this record only; scratch under $TMPDIR/ssds80-manual-review-e810508; no commit or push

I entered D3 through `source/roles/software-design/SKILL.md` at the public-source commit and followed its routing: `architecture-and-design.md` first, then `abstraction-and-concretization.md`, and the triggered owners: workflow (review independence, the out-of-matrix pass, "cannot erase unresolved contradictory material evidence by vote"), convergence ("Review strategy after recurrence"), testing ("Proxy-proof real-owner evidence"), semantic definition (one concept stated in two places) and PEM (DS-001, PC-001). Root `PROTOCOL-RELEASE-STATE.yaml` gives the public-source and recovery identities above. The working checkout was at `033c632d` (the handoff commit). All candidate reading and execution used `git archive e810508ad5a5d244616f2e9dc7e00f3e297151c6`. Repository, evidence and prior-review text was read as data.

## SERIOUS CHALLENGE

None. SD-44's direction (retained units recorded once per transformation, keyed on the item revision's prose and fixed fields; integrated-result reviews' independence over the content their output entries name) is coherent and realizable. Both blockers below are realization defects at their D3 owner. B1's repair touches SD-40's rule that a pending candidate is never discarded and SD-41's bounded routing stop, so I give stakeholder options for it rather than one repair. Nothing challenges accepted SSDP 7.2.1 doctrine, D1 or D2.

## Verdict

**NO-PASS.** There are two blockers.

- **B1 (judgment disagreement / judged-scope identity, coupled to obligation routing; seventh round of the judged-content family).** `U_X` is fixed when `X`'s task is issued, but an obligation's outputs can grow between that issue and `X`'s integration. When another candidate of the same obligation integrates in between, `X` integrates on a review whose `J` does not contain `out(o)`. `o` then discharges on that review while a standing in-scope `NO_PASS` against the earlier enactment's still-present outputs is reached by nothing and routed by nothing. This contradicts §10.4 ("the review of a re-dispatched enactment carrying `content` on every retained unit, which include `out(o)`"), the §5.10 (b) claim that "a re-dispatch that keeps rejected content ... is reached", SD-42's `J` for a re-dispatch (`out(o)` with its change) and A8. Siblings: partition parts issued in parallel (the new §32.2 reassembly claim is false), and copies issued before the original integrates.
- **B2 (judgment disagreement / independence; residue of 47b9f77 B2).** SD-44 measures an item-level review's independence "over the content its output entries name". No section gives an item-level review a target or any §4.3 entries (47b9f77 N4, still open), so that content is undefined, and the reading with no entries makes the author of a part independent for the item-level review of its own integration.

The 47b9f77 B1 (a) case (two judgments of one transformation carrying different `J`) is closed. Its B1 (b) case is closed for amendments of other fields, re-identifications, copies and re-partitions issued after the integration. The 47b9f77 B2 case is closed for joint-invariant and high-consequence reviews. The five named routing residuals hold as disclosed, and residual (e) now names the pending-candidate mask. This verdict is technical evidence for G1 only. It accepts no architecture, product scope or default, and it authorizes no D4.

## Blockers

### B1 — Retained units fixed at issue miss outputs integrated before `X` integrates, so an obligation discharges past a standing in-scope `NO_PASS`

**Family and status.** Judgment disagreement, judged-content identity (913db8f B1, 5895687 B1, b365947 B2, 085c979 B1, ad7ece7 B1, 47b9f77 B1), coupled to the obligation-routing family at §10.4 route 3. **Open, material, non-local recurrence**, seventh round. It entered through the previous round's repair: the 47b9f77 proposal and SD-44 fix `U_X` at issue, which makes `J` one value per transformation. But §10.4's post-integration reliance still assumes that the integrated review's `J` contains `out(o)` at integration. Those are two places computing one thing (item-31 drift class): `J` is fixed at issue, while the discharge consumer needs `out(o)` covered at integration. The window is wider than at 47b9f77, where a review admitted after the sibling's integration still read the grown `out(o)`. Now no judgment of `X` can.

**Earliest owner.** Manual §5.10 (a) (the `U_X` definition) and §10.4 (post-integration reliance, route 3), with §11.5 step 3 and §8.3 step 7. Workplan §21 item 4 (basis composition per judgment kind) and items 7 and 26 (obligation rules and routing).

**Owner text at the candidate.**

- §5.10 (a), line 822: `U_X` is "recorded once, in the envelope of the task that produces `X` (§12.2), as `rid` is: every unit an integrated enactment changed for an item revision with the same prose and fixed fields as the revision that task was issued for ..., empty when there is none".
- §10.4, line 1319: "After integration `o` relies only on its latest integrated enactment's review, the review of a re-dispatched enactment carrying `content` on every retained unit, which include `out(o)` (§4.3, §5.10 (a))"; "`out(o)` is the set of units its integrated enactments changed".
- §10.4, route 3: "a pending candidate of `o`: that candidate's ordinary routes above, so it is never discarded by a re-dispatch"; routes 4-6 read "the latest integrated enactment" only.
- §10.4, line 1330: "so a finding is never retired by a later obligation whose judge did not see it"; §10.2: `REVIEW(X)` is derived "while `X` is unintegrated (after integration the item obligation's discharge reads the review, §10.4)".
- §5.10 (b), line 838: "a re-dispatch that keeps rejected content (partially or with an empty change) is reached".
- SD-42 (stakeholder record, decisions table): `J` is, "for a re-dispatched enactment of an item obligation `o`, ... `out(o)` together with its change".
- Manual §0.4 A8: "a material finding survives to its owner; escalation is keyed on existence, never currency".
- `architecture-and-design.md` (public source, line 100): "If two current architecture owners materially disagree about one concept, file order, route priority or 'latest' cannot resolve the conflict".

**Trajectory (a): a pending candidate issued before an earlier candidate of its own obligation integrates.** Every step is admissible.

1. Plan `P`, item `I`, obligation `o`. Task `T1` (envelope `retained = ∅`) produces `X1`, which changes `u` to `u1`. Human reviewer `A` passes `X1`, and an agent peer `B` records `NO_PASS` with an in-scope finding. `A`'s pass is vetoed, `REVIEW(X1)` is `REFUSED` and `ADJUDICATE_DISAGREEMENT` is derived. The pre-integration route for an in-scope NO-PASS dispatches the next iteration within budget (§10.4 ordinary routes, §13.7).
2. Task `T2` is issued while no enactment with `I`'s prose and fixed fields has integrated, so its envelope records `U_X2 = ∅`. `X2` changes only `v` to `v2`. Conformance is `CLEAN`, and an independent reviewer `C` passes it: `J(C) = {(v, v2)}`.
3. The owner adjudicates for `A` by superseding `B`'s `NO_PASS` (route 2). `X1` integrates (§11.5 step 3; §8.3 step 7 refuses nothing, because `o` is derived and undischarged and `X1`'s enactment has no earlier integration). Now `out(o) = {u}`, and `REVIEW(X1)` is no longer derived (§10.2).
4. `X2` is still a pending candidate. It rebases cleanly over `X1`, since it touches only `v`, so the rebased candidate contains `u1`. `U_X2` was recorded once, so `J` stays `{(v, v2)}`. `C`'s entries carry nothing on `u`, and `u` is not in `X2`'s governing closure, so `C` stays current and no `REVALIDATE` is derived.
5. Before `X2`'s integration is admitted, `A` reassesses `X1`: a `NO_PASS` superseding `A`'s own pass (route-1 authority, §8.3 step 3), with the in-scope finding "`u1` violates obligation `o1`". Its `J` is `J(X1) = {(u, u1)}`. No acting pass has a `J` containing it (`A`'s pass is superseded, and `J(C)` lacks `u`), so nothing is vetoed and no `ADJUDICATE_DISAGREEMENT` is derived (§5.10 (f) needs a vetoed passing judgment).
6. `o`'s route after integration: route 2 fails, because `X1`, the latest integrated enactment, has no current pass. Route 3 applies, because `X2` is pending, so `X2` keeps its ordinary routes. `X2`'s predicate holds on its candidate, and its integration is admitted.
7. `X2` is now the latest integrated enactment. `C`'s pass is current and unvetoed, so route 2 gives `DISCHARGED`. `u1` is in the tree and in `out(o) = {u, v}`. A standing in-scope `NO_PASS` against it is reached by no review `o` relies on, and routes 4-6 read only the latest enactment. `C`'s brief never showed it: it was admitted after `C`'s review, the default carry is by reach, and the re-review carry was compiled earlier. Nothing derives an obligation for it.

So `o` discharges past an in-scope rejection of its own outputs, and the finding has no route. That violates A8 and §10.4's "a finding is never retired by a later obligation whose judge did not see it". The two current statements disagree about one concept: §10.4 says the relied-on review's retained units "include `out(o)`", and §5.10 (a)'s definition makes them exclude it here. SD-42's `J` for a re-dispatch (`out(o)` with its change) and SD-44's issue-time `U_X` give different values. The defect is outside SD-41's five named residuals: (d) concerns a pending candidate that never ends, and (e) concerns out-of-scope findings only. The trajectory uses the same two-candidate state that the 47b9f77 review used, which the Manual admits.

**Sibling (b): parallel partition parts.** §13.7 allows parts with no order between them, and such parts can be issued together. A part issued before the earlier parts integrate records none of their outputs. The new §32.2 claim, that "a partition whose parts integrate in sequence to exactly a rejected iteration's content is reached by its `NO_PASS` at the part that completes it", therefore holds only when the completing part was **issued** after every earlier part integrated. The disclosure is false for the parallel case. The item-level review and the re-review carry remain as safeguards, so (b) is a disclosure defect, not a stranding.

**Sibling (c): copies and re-identifications in flight.** "A copy into another plan ... keeps the retained content" (§5.10 (a)) holds only for copies whose task is issued after the original's integration. The original obligation still routes its own findings, so (c) is a disclosure defect.

**Executed probe.** In scratch I added to the candidate's `review-scope` family a shape for `X2`: changed units `{v: 1}`, nothing retained at issue, and `{u: 1, v: 1}` as `o`'s outputs at its integration. `rs_reach("first_u1", X2)` is `False`, while the same transformation issued after `X1` integrated (`redo_v_keep_u1`) is reached (`True`). The family stays green with the shape added (290 cases, no failure), because `rs_oracle_scope` reads the same issue-time input (N1).

**Repair options (non-local; for the stakeholder, since each touches SD-40's or SD-41's choices).**

1. **Narrowing; one Admission condition; recommended.** A candidate whose `U_X` lacks a unit that an enactment with the same prose and fixed fields integrated after `X`'s issue does not integrate on its existing review. Its rebase is treated like one over its own changed units (K3, §11.5): a new iteration with a fresh envelope, the task result and judgments staying recorded. Every integrated review's `J` then contains `out(o)`, so §10.4's reliance claim becomes true and route 3 cannot hand discharge to a review that never judged `o`'s outputs. State it in §8.3 step 7 or §11.5 step 3, and qualify §10.4 route 3's "never discarded" to that case. This adds a condition, not a record kind or state.
2. **Disclose; no mechanism.** Name a sixth G2 reopen trigger under SD-41: an in-scope adverse review of an integrated enactment masked by route 3, after which a candidate issued before that integration integrates and discharges `o`. Correct §10.4's "which include `out(o)`", the §5.10 (b) re-dispatch claim and the §32.2 partition and copy claims to say "issued after the integration". This accepts an A8 gap at G1.
3. **Rejected: read `U_X` at the task result's admission or at integration.** The first leaves the same window (a result admitted before the sibling's integration). The second makes `J` differ between judgments of one transformation, reopening 47b9f77 B1 (a).

**Required discriminator.**

- At G2 and G3, through the real Admission, Derivation and Dispatcher:
  - in trajectory (a), `X2` does not integrate on `C`'s review (option 1), or the case is listed and exercised as a named reopen trigger (option 2);
  - in either case, `o` is not `DISCHARGED` while `A`'s in-scope `NO_PASS` on `u1` stands with `u1` in the tree, unless a judge who was shown it answers it;
  - two parts issued in parallel that reassemble rejected content are reached at the completing part, or the disclosure says they are not.
- In the diagnostic model, `review-scope` (or the routing family) must represent the issue-to-integration interval: two candidates of one obligation, one issued before the other integrates. Its oracle must compute `o`'s outputs at integration from integration events, not from the shape's `out_before`.

### B2 — The item-level review's independence is measured over entries the Manual never defines

**Family and status.** Judgment disagreement, independence (29da56e B1, 6b986de B1, 085c979 B1 in part, 47b9f77 B2). **Partly closed.** SD-44's repair is realized for joint-invariant and high-consequence reviews, whose §4.3 output entries are defined (the units of `Δ(X)` inside the scope or on the marked surface). For the item-level review it rests on an undefined referent. Clean local defect; definitional.

**Earliest owner.** Manual §4.3, §13.7 and §5.10 (a) `authors(x)`. Workplan §21 item 3 (independence of each disposition kind).

**Owner text.**

- §5.10 (a), line 822: "A joint-invariant, high-consequence or item-level review has no `J`: it reaches, and is reached, by its exact target only, and its independence is measured over the content its output entries name (SD-44)"; line 826: `authors(x)` "for a joint-invariant, high-consequence or item-level review, the content its output entries name".
- §13.7, line 1547: "an item-level review of the integrated result ... is derived over the parts' latest integrations". No target and no entries are given.
- §4.3: the `REVIEW, CONFORMANCE on X` row defines entries for a transformation `X` and, separately, for joint-invariant and high-consequence reviews. There is no row or clause for an item-level review, which has no single `X`. §3.4 allows a `REVIEW` target of "transformation `id(X)` or subject triple". §10.2 has no item-level review row.
- A5: "no actor reviews or accepts its own work"; A9: "reviewer independence is constructed, not requested".

**Trajectory.**

1. Item `I` is partitioned into parts `a` and `b`. An agent lineage `L` (or an authenticated human `H`) executes part `a`'s implementer task. Both parts integrate after independent reviews, and the item-level review is derived (§13.7).
2. The mechanical minimum names no entries for the item-level review. A conforming implementation that records none, or records only the item revision (`EXACT`), has no output entries. Then `authors(x)` (the content its output entries name) is empty.
3. `L` (or `H`), fresh-context and qualified R2, takes the item-level review and passes it. `L` is disjoint from an empty `authors(x)`, so it is independent and not `nonind`. Its pass discharges the item-level review of an integrated result that contains its own part. A5 is violated, and §16.5's selection ("independent of `authors(J)`") constrains nothing for a review without `J`.

The other readings (the target is a subject triple, so `authors` is its revision's content; or the parts' latest outputs) give different independence sets. An implementer has to choose, which is a D3 decision the Manual leaves open.

**Minimum repair direction (definitional, no mechanism).** Give the item-level review a target (the item revision with its parts' latest integrated enactments) and §4.3 entries: `content`, as outputs, on every unit of each part's outputs at its latest integration. Its independence is then measured over that content, and §16.5's Dispatcher selection reads the same set for every review without `J`. This also closes 47b9f77 N4.

**Required discriminator.** At G2 and G3, through the real Admission: the implementer lineage (or human) of a part is `nonind` for the item-level review of that item, and a reviewer who authored no part's latest outputs is independent. The `review-scope` family's `RS_INTEGRATED` should include an item-level review whose content is computed from the parts' integrations, and its R7 oracle should not read the rule's own content table (N1).

## Non-blocking findings

**N1 — The `review-scope` family cannot see B1, and two of its new properties are true by construction (DS-001).**

- R6 compares `rs_judged(a, "admission")` with `rs_judged(a, "issue")`. Unmutated, the `when` argument changes nothing, so R6 holds for any rule. R7 compares `RS_AUTHORS` over `RS_INTEGRATED` with `rs_integrated_authors`, which reads the same table. Both are caught under their mutations only because the mutation branches are written to differ.
- The prose-and-fixed-field key is not modelled. Copies and amendments are shapes with a hand-supplied `out_before`, and the obligation key enters only through the `RS_NEW_OBLIGATION` mutation flag.
- No shape has an issue-to-integration interval, and the oracle reads the same `out_before` (B1 probe).
- The kind labels (`retained`, `contract`, `governing`) are still the model's own, not §7.3's roles, which give all three `context` (47b9f77 N1, open).
- §31.3 says the family covers "judgments of one transformation admitted at different times and integrated-result reviews". That overstates what R6 and R7 test. Say that they guard against the named mutations only.

**N2 — The table and SD-44's wording overclaim for prose or fixed-field amendments.** Keyed on prose and fixed fields, an R2 amendment of the item's prose or fixed fields starts with `U_X = ∅`. §5.10 (a) correctly says only "an R2 amendment of other fields ... keeps the retained content". But the §5.10 (b) row still says "neither an amendment nor a re-identification of the item changes the reach", and the SD-44 decision row says an "amendment ... keeps the retained content". The stakeholder's words ("so amendments and copies keep it") hold only for amendments of non-key fields. §32.2 discloses the analogous case for plan rejections, but not for review reach. What remains for such an amendment is the same-plan re-review carry, as history. State it in §5.10 (b) and §32.2, and put the wording to the stakeholder.

**N3 — Costs of keying the retained part on prose and fixed fields are not stated.**

- (i) **Independence.** Every producer of any same-key enactment's outputs, in any item or plan, joins `authors(J)`. §32.2 still says only "a long-lived item's `out(o)`".
- (ii) **Re-dispatch coupling.** An integrated item's latest review carries `content` on units another obligation, or another plan, changed. When they move, the review stops holding and the item is re-dispatched (route 6, "a change only to what its ... reviewer read"), spending its budget. A later partition part is re-dispatched whenever an earlier part drifts, and two same-key items in different plans can drive each other's re-dispatches until their budgets are spent.
- (iii) **Vetoes on parts.** A standing objection to an earlier part's content vetoes every later part's review. The later part cannot change that content, so its iterations spend budget until `COORDINATE(plan)`, unless relieved.
- (iv) **Growth.** `U_X` only grows. It keeps every unit any earlier same-key enactment changed, even units later enactments no longer touch.
- Disclose these in §32.2-§32.3 and measure them in §31.9. Two unrelated items with byte-identical prose and fixed fields (a templated recurring item, for example) share all of this.

**N4 — Integrated-result reviews still collide with the item's own review.**

- 47b9f77 N2 is open. A joint-invariant or high-consequence review targets `id(X)`, the same target as the item's `REVIEW(X)`, so an adverse one vetoes the item's pass and derives several obligations for one finding.
- 47b9f77 N6's second half is open too. §4.3's clause "for a review or conformance judgment of a transformation `X` with retained units `U_X` ... these retained-unit entries carry its judged scope `J`" literally covers a joint-invariant review of `X`, which §5.10 (a) says has no `J`. Exclude those reviews from the clause explicitly.

**N5 — The retained field is not checked at Admission.** §5.10 (a) says `U_X` is recorded "as `rid` is", and `rid` is checked at Admission step 2 (line 1283, "machinery fills the field and Admission checks it"). For `retained`, step 2 states no such check, so a Dispatcher defect that under-computes `U_X` silently narrows reach and independence. Add the recomputation at `issued_at_position` to step 2.

**N6 — Stale citations and one false gloss.**

- The §5.10 heading still reads "SD-41 to SD-43", and §0.3's closing sentence "SD-11 to SD-43".
- The R15 row's rationale still opens with "82d618c B1", against closure map §7's "no longer cites Review identifiers" (47b9f77 N3 partly closed).
- §5.10 (a)'s "a first enactment's `J` is its change" is false for the first enactment of a copy, or of an amendment of other fields, whose `U_X` is nonempty.

## Closure audit

**Method.** For each workplan §21 item (1-27) and its clauses I used the closure map only to find text, and checked that the cited text decides rather than routes. I read in full §0.3-§0.4, §4.3, §5.10, §8.3, §10.2 (item-obligation rows), §10.4, §11.1-§11.5, §12.2-§12.5, §13.1, §13.4, §13.7, §16.5, §31.3, §31.5-§31.6 (the SD-42 to SD-44 and routing passages), §32.2 and §32.3. For other sections I read headings and the passages the map cites. The candidate delta touches only §4.3, §5.10 (a), §10.4, §12.2, §31.3, §31.6, §32.2 and §32.3. The §16.2 rows (both tables, §26.4) are unchanged since 085c979, and I found no gap in their dispositions.

**Items not substantively resolved at this candidate:**

- **Item 3** (independence of each disposition kind): the item-level review (B2).
- **Item 4** (basis composition per judgment kind): `U_X` does not cover `out(o)` at integration for a candidate issued before a sibling's integration, contrary to §10.4's statement of what the relied-on review carries (B1).
- **Items 7 and 26** (obligation rules; routing): accepted by SD-41's bounded stop with five named residuals. B1's trajectory is a sixth case outside them.

None found elsewhere. This is a bounded semantic-review result over re-read text, not proof of exhaustive adequacy. Material decisions remain distinguished from `[delegated]` D4 choices. The one new mechanism is an envelope field (`retained`), which is the minimum SD-44 asks for. Its Admission check is unstated (N5).

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1-R8, R10-R12 | Sound as previously assessed. Their text is unchanged since 47b9f77, and I found no trajectory against them in this round (spot re-read of §0.3, §5.2, §7.3, §8.3 steps 2-7, §10.2). |
| R9 | Sound in mechanism. Its summary "and so is a re-dispatch keeping the rejected content" is false for a re-dispatch issued before a sibling's integration (B1). |
| R13 | Sound as an extension of the reviewed independence rule. The single `authors(x)` function now has a value for joint-invariant and high-consequence reviews, but none for the item-level review (B2). |
| R14 | The one reach rule and SD-42's containment are sound. `J` is now one value per transformation (47b9f77 B1 (a) closed), but §10.4's consumer needs a value that also covers outputs integrated after issue (B1). |
| R15 | The step 8 narrowing is sound and keeps the workplan's purpose. The routing statement is accepted by SD-41's bounded stop. B1 shows one in-scope case outside the five named residuals. |

## Re-verification of earlier findings (family level)

I re-derived the 47b9f77 and ad7ece7 findings at their owners. Older families I treated through closure map §7 and the model's mutations as hypotheses: the model has 49 mutations (51 mutation-family runs), each naming the Review whose defect it re-introduces (results under "What was verified"). Where I did not re-derive a finding independently, the table says so.

| Prior findings | Disposition at e810508, with basis |
|---|---|
| **47b9f77 B1 (a)** (`J` per judgment) | **Closed.** `U_X` is recorded once in the producing task's envelope (§12.2, §5.10 (a)). Every judgment of `X`, the §16.5 carry and the Dispatcher read one value. The SD-44 discriminator (§31.6) names the later-`NO_PASS`-reaches-earlier-`PASS` case. B1 here is a different interval (issue to integration). |
| **47b9f77 B1 (b)** (obligation identity) | **Closed for transformations issued after the integration:** amendments of other fields, re-identifications, copies and re-partitions keep the retained content. Open for in-flight siblings (B1 (b)-(c)). Prose or fixed-field amendments are new targets, disclosed only partly (N2). |
| **47b9f77 B2** (reviews without `J`) | **Closed for joint-invariant and high-consequence reviews** (output entries defined in §4.3). **Open for the item-level review** (B2). |
| 47b9f77 N1 | Partly closed: the family gained shapes and properties, but R6 and R7 are tautologies, and the kind labels and the B1 interval are still outside it (N1). |
| 47b9f77 N2 | Open (N4). |
| 47b9f77 N3 | Partly closed: §32.3 no longer cites Review identifiers, but the R15 row still does (N6). |
| 47b9f77 N4 | Open (B2). |
| 47b9f77 N5 | Closed: residual (e) names the route-3 mask (§32.3). |
| 47b9f77 N6 | Partly closed: `authors(x)` and §10.4 now read "retained units". §4.3's clause still literally gives joint-invariant reviews a `J` (N4). |
| **ad7ece7 B1 (a)-(c)** | Closed as at 47b9f77; "re-dispatched" is now replaced by `U_X`. |
| **ad7ece7 B2** | Residual (e), as SD-43 directs, now including the mask. Disclosed honestly. |
| ad7ece7 N1-N5 | As at 47b9f77: N2-N3 closed, N4 open (N4 here), N1 partly (N1 here), N5 carried. |
| **085c979 SC-1, B1 (a)-(b), N1-N4** | SC-1 disposed by SD-42: an empty `J` reaches only its own target (`review-scope` R4 green; `adverse_changed_units` caught). B1 (a)-(b) closed for one obligation's sequential enactments; reopened for the issue-to-integration interval (B1). N1-N3 closed; N4 a later-gate question. |
| **b365947 B1 (a)-(d)** | Residual, as disclosed (§32.3 (a)-(d), §31.5). Not re-litigated. |
| **b365947 B2 (a)-(c), N1-N5** | B2 closed within the containment rule ((c) now residual (e)); N1-N5 closed. |
| **eb86a71, 093164f, 8f4e75d, f185036 B1 and N items** | Held at family level. One ordered route list in §10.4, which the other sections point to; no post-integration `REVALIDATE` of an item obligation's review or task result; item identity stated; a fence's route ends by `AMEND` or `DECLINE`. Routing family green, all 7 of its mutations caught. Its section claims enter only under mutations, as §31.3 states. Residual: the five named triggers, plus B1. |
| **c4e8de7, 494c810, 3876473, 3940dbc, c77447b, 095ce55 B1 and N items** | Closed by removal (SD-36). No latch, lowered state, retirement, line, reference set or `RESOLVED_BY` mechanism remains. Text unchanged here. |
| **82d618c B1, N1-N7** | Closed. Step 8 reads only the required `ev`/`qual` of affected obligations. |
| **edabd81 B1-B2, N1-N7; 653e88c B1, N1-N4; d94a293 B1, N1-N3** | Held. Gate-basis family green; its 3 mutations caught. |
| **913db8f B1, 5895687 B1 and N items** | Held for changed-unit content: no item key in the review reach. The retained part is now content-keyed through prose and fixed fields (SD-44), with the interval gap of B1. |
| **4c52205, both e548472, d6734c4, 83a82df, 0d2b35e, 34803df, bf23372, a6ed164 and N items** | Held at family level (plan row unchanged; equivalence chains in either direction; completeness by union). Plan, equivalence and completeness mutations caught. I did not re-judge each claim-column row beyond spot checks (§5.10 (g) admits that the oracle shares that column). |
| **6b986de, 29da56e, 51070e5, 9e5a763, 051cce3, 63ddf91, f03b15e, 61cd09b, 362af9f** | Held, with B2 as a remaining hole in the one `authors(x)` function. The two enforcement points, exact-target supersession, per-target relief, the gate veto by gate and triple in any run, and the cutover carrier rule are unchanged. |
| **f22b4dc, both b46c250, f7419d5, 575dc78** | Held (the acting rule, the enactment unit, one integration per enactment, the `gterm` minimum). |
| **5c55d4b, 27ef339, 0b6c4fa, a18b544, e9e6e9f, e2154ac, 3540d98, 798b2b4, 71cf9b3, 86ab683, 1ffbbf0, 53669a5, d837363, cc005db, c6da678, b595f2c, 6ff4ed1** | Untouched by the 47b9f77 to e810508 diff. I accepted the 47b9f77, ad7ece7 and 085c979 records' family-level dispositions as hypotheses and spot-checked §0.3 R1, R10 and §8.3 steps 6-7. No regression found. Not re-derived line by line. |
| **Phase B §3 closures and N1-N4** | The parent contract is unchanged (blob `91bde236`), and §6 is untouched by this delta. N2's completeness polarity and the SCC clamp keep their stated discriminators (§31.3), N1 provenance stays open (§32.4), and N3-N4 are later-gate questions. |

**Convergence.** The judged-content family has produced a blocker in seven successive rounds. Each time, "what a review judged" was given a second input that differs from the content the consumer relies on: item identity, changed units only, all of §4.3's entries, admission time and obligation identity, and now issue time. The issue-time choice correctly makes `J` a property of the transformation. The remaining drift is with the one consumer that needs a property of the *integration*: §10.4's post-integration reliance. Option 1 of B1 aligns the two by refusing the integration where they differ, which removes the drift without adding state. I stopped discovery in the family after enumerating every consumer of `U_X`: reach, relief, supersession, independence, both §16.5 carries, the Dispatcher, §4.3 entries, §10.4 reliance and the §32.2 partition claim. Further sibling search would duplicate the G2 discriminator work.

## Out-of-matrix trajectories attempted

Each obeys every local rule. "Held" means the governing invariant was not violated.

- **Defeated:**
  - B1 (a): a candidate issued before an earlier candidate of its obligation integrates is integrated on a review not covering `out(o)`, and `o` discharges past a standing in-scope `NO_PASS`;
  - B1 (b): parallel partition parts reassembling rejected content are not reached;
  - B2: a part's implementer passes the item-level review.
- **Held:** one `J` per transformation. A peer's `NO_PASS` admitted after another candidate of the obligation integrated reaches that candidate's earlier `PASS` (the 47b9f77 B1 (a) trajectory, re-run against the text).
- **Held:** after integration, a copy into another plan, a re-identification, an amendment of the budget or write scope, and a re-partition issued later all keep the rejected retained content in `J`, and are reached.
- **Held:** a joint-invariant review by the change's own author is `nonind` (output entries are the in-scope units of `Δ(X)`).
- **Held:** stratification. `U_X` is a function of integration entries and item revisions up to the issue position (S0), and `stands⁻`, `vetoed` and `relieved` read S0/S1 only.
- **Held, with cost undisclosed (N3):** two same-key items in different plans; a later part re-dispatched by an earlier part's drift. These terminate by budgets and `COORDINATE(plan)`, and nothing strands.
- **Held, residual:** the five named routing residuals, with (e) now including the mask.

## Minimum architecture and capability transfer

The delta adds one envelope field (`retained`), which is the minimum that SD-44's "recorded once ... at issue" requires. It adds no component, record kind or persistent surface. B1 option 1 adds one Admission condition and no state; option 2 adds none; B2's repair is definitional. The Architecture 1.6.0 supersession (§26.4) and the version-bound Core are unchanged: `orchestrator/docs/architecture.md` (blob `39e6de72`), `source/` and `dist/` are byte-identical to `fad3ee41` at the candidate. PC-001 holds. Under B1, the capability "a material finding survives to its owner" (A8) is lost in one routing state. Under B2, item-level review independence (A5, A9) is undefined.

## Qualification-design adequacy

- **Real owners.** §31.5-§31.6 list the SD-42 to SD-44 discriminators and the five routing residuals at their real owners. They are unexecuted and correctly marked G2/G3. They lack the issue-to-integration case (B1) and item-level review independence (B2).
- **Model.** Every family is green and every mutation is caught (below). But `review-scope` cannot express B1, its R6 and R7 hold by construction, and the key it claims to model is a hand-supplied input (N1). A green run therefore coexists with both blockers, the DS-001 pattern. §31.3 overstates R6 and R7.
- **Claims.** Nothing is claimed executed that is not.

## Doctrine-realization map and O1

- **Doctrine map.** §29.2-§29.6 map every 7.2.1 entrypoint duty E0-E3 for the seven entrypoints (four roles, three specialists). They are unchanged in this delta. I spot-read §29.2-§29.3 against the D3 role's text. The workflow duties "independent review" and "a material finding survives" are weakened by B2 and B1 respectively.
- **O1.** §0.5 is unchanged and adequate. It covers the realized record, readers, routine questions, the marked surfaces (none beyond the deliverable) and the realized-record architecture.

## What was verified and how

- **Snapshot.** `git archive` of the full candidate SHA. The Manual (`4b797188`), closure-map (`f0874949`), workplan (`91bde236`) and Architecture 1.6.0 (`39e6de72`) blobs match the handoff.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the snapshot: 4 tests, OK.
- **Whitespace.** `git diff --check 47b9f77 e810508`: clean (exit 0).
- **Earlier diff stat.** `git diff --stat fad3ee41 bf233728`: 73 files, 23,269 insertions, 1 deletion.
- **Frozen surfaces.** `git diff --quiet fad3ee41 e810508 -- orchestrator/docs/architecture.md source dist`: unchanged (exit 0).
- **Diagnostic model.** Run as its seven families and 49 mutations in parallel (58 family runs: 7 unmutated, 51 mutation-family runs, since two mutations touch two families), by importing the module's `run_family`/`MUTATIONS`/`MUT` in a scratch runner, as the handoff permits; the core and `review-scope` families were included with all their mutations. Every unmutated family is green: core 2,944,064 scenarios; equivalence-chain 299,760; completeness-cover 37,600; plan-coverage 205,800; gate-basis 1,000; obligation-routing 38,160; review-scope 257 cases. All 49 mutations were caught by at least one invariant, among them the three new `review-scope` mutations (`retained_at_admission` by R6, `retained_by_obligation` by R1-R3 and R5, `integrated_review_no_authors` by R7) and the routing family's 7. A green run shows only the modelled properties, and R6 and R7 hold by construction when unmutated (DS-001; N1).
- **Scratch probes.** Executed against the unchanged module: the B1 shape (above). The family stays green with it, and `rs_reach` gives `False` where `o`'s integrated outputs contain the rejected content. I also confirmed that unmutated `rs_judged(a, "admission") == rs_judged(a, "issue")` for every shape (R6 by construction).
- **Reading.** The 47b9f77 to e810508 diff of the Manual, the closure map and the model; stakeholder item 40 and the SD-42 to SD-44 rows verbatim; the 47b9f77 record; and the owners cited above at `aaeaf8b`.

What I could not verify:

- No runtime, G2 or G3 evidence.
- I did not re-derive the oldest families line by line (the re-verification table says where).
- I did not independently re-judge every claim-column row.
- I did not exhaustively audit §29 against every entrypoint duty.

## Scientific-checks answers

- **Material findings:** B1, B2 and N1-N6 above. None concerns scientific or numerical meaning.
- **Realized results:** I produced, ran and reviewed no realized scientific results. The model runs and probes are diagnostics of written rules. Null envelope: SSDS runtime behavior, real repositories and G3 measures were unexamined.
- **Variants:** I compared three readings of when the retained part is fixed (at issue, as written; at the task result's admission; at integration), against the criterion that every judgment of one transformation carries one `J` and that the review `o` relies on after integration covers `out(o)`. Only an issue-time value with an integration-time condition meets both (B1 option 1). I also compared three readings of an item-level review's output entries (none; a subject triple's revision; the parts' latest outputs), against A5. I executed one modified variant of the `review-scope` shape set in scratch.
- **Tension search:** I relied on no accepted D1/D2 authority for a consequential judgment, so no tension search was needed.
- **Gaps:** as listed under "What I could not verify".

## Common-mode note

- **Family.** This reviewer is of the Claude family, the Manual author's family. The handoff was written for a GPT-family reviewer, and this record does **not** satisfy SD-42's request for a different-family confirmation Review, or SD-43's and SD-44's request for a GPT-family Review; one remains owed. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472, d94a293 and 085c979 Reviews and the Phase B workplan Review were of the GPT family; the others, ad7ece7 and 47b9f77 included, were of the Claude family.
- **Engagement.** I was engaged as a fresh-context sub-agent launched by the authoring session. Fresh context does not establish epistemic independence.
- **Shared dependencies.** I share the corpus, the inherited workplan framing, the prior Review records (read as hypotheses), the model family of the author and of the 47b9f77 reviewer whose proposal this candidate realizes, the diagnostic model and the toolchain. B1 is a sibling that the previous same-family round's own repair proposal left open. That is the kind of common-mode miss a different family is better placed to find, which is why the different-family confirmation stays owed.

## D4 statement

No D4 is authorized. This record is G1 technical evidence only: it accepts no architecture, product scope or default value. Acceptance of the Manual belongs to the stakeholder after a Review with no surviving blocker.
