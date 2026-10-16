# Independent D3 Review — SSDS 8 Architecture Manual, candidate 4c52205 (NO-PASS)

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system (full clone, complete history)
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          4c522057e1b45100eece6e7c0caa316c4868612f
    SCOPE:              the whole proposed Manual as durable D3 owner, handoff §1 (a)-(g); confirmation Review
                        after SD-31
    MANUAL blob:        01d76866ba072d8a799910d27283a4298c00005d (orchestrator/docs/ssds-8.0-architecture.md), verified
    CLOSURE MAP blob:   7ba2133775ff98c07293991bacaf8e9553e252f8 (review aid, not authority), verified
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851
                        (blob 610f373b97fb8152d2a5742e17fa172e12204756); blob at the candidate
                        91bde236465178f20c7348280e036d2884dfc216, verified
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954; recovery
                        efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml, accepted_current)
    PRIOR REVIEWS:      every record in qualification/ssds80/ through both e548472 Reviews, read as hypotheses
                        only; the two e548472 records were read after the plan-row analysis below was formed
    REVIEW METHOD:      handoff steps 1-11 and 6a; the candidate read from a `git archive` snapshot under
                        $TMPDIR/ssds80-manual-review-4c52205/snap; falsification concentrated on the clauses SD-31
                        changed (the §5.10 (b) plan row, §0.3 R14, §13.4, §16.5, §31.6 (V)) and on the plan-row
                        family in both directions, then on the newest model extension; the diagnostic model run
                        in full (§13) plus two probes that import it unmodified
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched by the
                        authoring session

## SERIOUS CHALLENGE

**SC-1 (to the stakeholder; SD-31's disjunct list does not realize SD-31's stated purpose).** SD-31 (stakeholder record item 26 and the decisions table) chose: "drop SD-30's revert exemption: a plan rejection of `r*` also reaches every acceptance naming `r` with `r ⊑ r*` (the reviewed §7.9 claim that an acceptance's conclusion still applies under tighter controls), besides `r* = r` and `r ⊑ cur ∧ r* ⊑ cur`". The Manual realizes that list exactly (§5.10 (b)), and states the purpose as a property: "whatever the item's revision now is: a revert or loosening releases nothing (SD-30, SD-31)" (§5.10 (b)); "so a revert or loosening releases nothing" (§0.3 R14); closure map §1 item 8 repeats it.

The list does not have that property. The third disjunct still reads `cur`, so wherever an acceptance and a rejection are of **incomparable** item revisions and the veto bit only because `cur` was a common tightening of both, a later revert or loosening of `cur` to a revision above the accepted one but not above the rejected one releases the acceptance, with no judgment, no `PLAN_ACCEPT`, no brief and no owner routing. That is exactly the harm SD-31 was chosen to remove (the e548472 same-family SC-1: "the plan's author released a standing rejection with no judgment"), on a sibling shape. The same reviewed claim SD-31 cites settles it: the acceptance of `r` claims every tighter revision, the join included, and the rejection of `r*` denies every tighter revision of `r*`, the join included, so the two judgments contradict each other whatever `cur` is. The Manual's own claims column says this, and the one reach rule of §5.10 (a) ("`z` … claims what `j⁻` denies") then reaches the acceptance; the row's derived formula does not. Two simultaneously applicable statements of one rule disagree (B1).

Owner and scope: the stakeholder's SD-31 direction, then the Manual §5.10 (b) plan row and every restatement of it. Basis: B1's trajectory and the probes in §13. Consequence: the plan-row family is not closed by SD-31; a conforming implementation of the row's formula lets the plan's principal dissolve a vetoing independent rejection by an R1 control edit. Discriminating evidence: B1's discriminator. The challenged decision stays the explicit baseline; the options are in B1. I found no other Serious Challenge: nothing I checked suggests that the reviewed workplan, SD-1 to SD-30 as SD-31 leaves them, or the governing 7.2.1 owners are themselves contradictory or unrealizable.

## Verdict

**NO-PASS.** One blocker, B1 (judgment-disagreement layer, plan-coverage reach family; the sixth finding in a row on the `PLAN_ACCEPTANCE` row), tied to SC-1 and needing a stakeholder decision. The candidate's other SD-31 changes (the brief-carry termination and the (g)6 restatement) hold for what they claim; non-blocking findings N1-N7 follow.

## Blockers

### B1 — A loosening below the join of incomparable revisions releases a vetoing plan rejection (family: plan-coverage reach; sibling of e548472 B1 and 0d2b35e B1)

**Text.** §5.10 (b), `PLAN_ACCEPTANCE` row, third column: "a rejection of item revision `r*`, under any objective revision, denies `r*` and every tighter revision (§13.4) … one acceptance naming `r` claims `r`, every revision tighter than `r` (its conclusion "still applies under tighter controls", workplan §7.9, §13.4) and, through coverage, the item's current revision `cur`. So a rejection of `r*` reaches an acceptance naming `r` when `r* = r`, when `r ⊑ r*` (the acceptance claims `r*`), or when `r ⊑ cur` and `r* ⊑ cur` (`cur` keeps the rejected controls), whoever recorded the acceptance and whenever, and whatever the item's revision now is: a revert or loosening releases nothing (SD-30, SD-31)." §5.10 (a): "`same(j⁻, z)` … is every passing judgment `z` of `j⁻`'s kind for which some set `S` …, together with `z`, **claims** what `j⁻` denies … every other kind states what one judgment claims, so for it `S` is empty and `z` alone decides." §13.4: `⊑` "is always checked against the **accepted** revision"; "a standing rejection of a revision reaches every acceptance of a looser revision, which claims it, and every acceptance covering a current revision that tightens it". §11.4: "control tightening keeps the existing plan acceptance current (R1)". §10.2: `PLAN_ACCEPT(items)` only for "an item revision not covered by a current plan acceptance"; `ADJUDICATE_DISAGREEMENT` only for a standing adverse judgment "that vetoes a passing judgment of its kind acting in the state".

**The logical gap.** Under the column's own claims, an acceptance of `r` and a rejection of `r*` contradict each other exactly when the up-sets `{x : r ⊑ x}` and `{x : r* ⊑ x}` meet (or `r* ⊑ r`, a special case). The formula tests that meeting at only two points, `x = r*` (disjunct 2; disjunct 1 is its reflexive case) and `x = cur` (disjunct 3). When `r` and `r*` are incomparable, their meeting points are their common tightenings; the formula sees one only while it is the current revision. By §13.4 a common tightening exists for any two revisions with byte-identical item prose and equal values of every field §13.4 marks "unchanged" (subset fields meet by intersection, superset fields by union, `budget` by minimum, `scientific` by `APPLIES`, `HARD` secondaries by union), so the gap is not exotic: it is every pair of control-only variants that tighten different fields.

**Trajectory (conforming at every step).**

1. Item A at `r = (budget 10, write_scope {a, b})`. An independent agent `P` records `PLAN_ACCEPTANCE ACCEPTED (o, A@r)`. A is issuable.
2. The principal widens the write scope: `r* = (budget 5, write_scope {a, b, c})`, same prose. Against the accepted `r` this is R2 (a superset scope), so `PLAN_ACCEPT(A@r*)` is derived. An authenticated independent human `H` answers it `REJECTED (o, A@r*)`, finding, say, that A's objective prose, shared byte for byte by every revision here, contradicts the governing D2 contract. `r` and `r*` are incomparable. Nothing reaches `P`'s acceptance (it does not cover `r*`), correctly.
3. The principal amends to `j = (budget 5, write_scope {a, b})`. Against the accepted `r` this is R1 (5 ≤ 10, same scope), so `P`'s acceptance covers `j`; and `r* ⊑ j`. Disjunct 3 holds: `P`'s acceptance is vetoed, A is not issuable, `ADJUDICATE_DISAGREEMENT` is derived. Correct so far.
4. The principal amends to `r' = (budget 6, write_scope {a, b})` (or reverts to `r`). Against the accepted `r` this is R1 again: no `PLAN_ACCEPT`, no brief. `r ⊑ r*` is false, `r* ⊑ r'` is false (6 > 5): no disjunct holds. `P`'s acceptance is unvetoed, covers `r'`, A is issuable, and `ADJUDICATE_DISAGREEMENT` is no longer derived.
5. A is issued under prose that a standing, unrelieved independent rejection denies. The owner, who held an adjudication obligation at step 3, is no longer asked; no one who saw the rejection judged anything after it; the release was the plan principal's control edit.

The Manual's own qualification case is this trajectory: §31.6 (V) "a rejection of `a0`, an R2 amendment to `aQ` incomparable with `a0` accepted independently, then an R1 tightening to `a3 ⊒ a0`: not issuable, `ADJUDICATE_DISAGREEMENT` derived; contrast: a tightening of `aQ` to `a3' ⋣ a0` is issuable". Taken after `a3` (a loosening from `a3` to `a3'`, R1 against the accepted `aQ`), the contrast certifies the release as expected behaviour.

**Probes (on the candidate's own model, imported unmodified).** `probe_join.py`: with `ACCEPTED(i1)` by `P` and `REJECTED(iQ)` by `H` (`i1` and `iQ` incomparable, `i3` their common tightening), `cur = i3` gives `base(p1) = F`, issuable `F`, adjudication derived; `cur = i2` (a loosening below `i3`, R1 against the accepted `i1`) gives `base(p1) = T`, issuable `T`, no adjudication, and the model's oracle agrees in both states. Over the model's seven item revisions and seven current revisions, the formula and the column's claim (read over the model's revisions) disagree on 104 (current, rejected, accepted) triples, 14 of them where the acceptance covers `cur`, so that issuance differs; all 14 go through the join `i3` of `iQ` with the chain. `probe_claim_oracle.py` re-runs the plan family with only the oracle's plan reach replaced by that claim: with the candidate's model otherwise unchanged, the plan family (119,560 scenarios) then reports 143,516 I1/I3 and 34,814 I8 disagreements (first example: `cur = i0`, `ACCEPTED(i0)` by `P`, `REJECTED(iQ)` by `H`; the model makes A issuable, the claim does not). The model has no history, so this count measures the whole claim/formula gap, never-joined branches included, not B1's released cases alone. The model is green on B1 by construction: its oracle restates the formula (`rz == rj or claims_rj or (covers_cur and cur in denied)`), not the claim, which §5.10 (g) discloses only as sharing "the same table column".

**Why it is a defect, not a disclosed trade-off.**

- SD-31's chosen purpose and the Manual's stated property are "a revert or loosening releases nothing"; step 4 is a loosening that releases. §32.2 discloses that an R2 amendment can be a new target outside the veto; it does not disclose that an R1 edit can lift a veto that already bit. Here the vetoed acceptance is the original one, not an R2 target.
- It is the e548472 SC-1 harm on a sibling shape, which SD-31 adopted as a defect: release by "latest-editor order" (evidence owner), a contradiction "erased" without adjudication (workflow owner), and the principal, not the rejecter or the owner, deciding that a rejection no longer applies, contrary to SD-30's "judging that an amendment cured a rejection is the rejecter's or the owner's, never a peer's".
- §5.10 (a) and the row's formula disagree on the same input, and both are normative in the one owner section: an implementer must choose. Read with §5.10 (a), the claims column reaches `P`'s acceptance in every state from step 2 on; read with the formula, it reaches it only at step 3.

**Violated owner text.** Evidence owner (`source/shared/references/evidence-evolution-and-dependencies.md` at the public-source commit, line 153): "Do not resolve material assessment disagreement by majority vote, latest-editor order, … or serialized record position. … An unresolved material disagreement keeps dependent present guidance/closure visibly qualified." Workflow owner (`workflow-and-workplans.md`, line 104): "A synthesizer reconciles findings through evidence and owner adjudication; it cannot erase unresolved contradictory material evidence by vote." Reviewed workplan §7.9 (line 1726): "It claims only that the acceptance's conclusion about *what is asked* still applies under tighter controls." Manual §0.4 allocation principle ("decidable only conservatively -> machinery, sound over-approximation, never under-approximation") and C5. Stakeholder SD-31's stated purpose ("drop SD-30's revert exemption").

**Earliest owner.** The stakeholder (SD-31's disjunct list), then Manual §5.10 (b) plan row; §0.3 R14, §13.4, §31.6 (V), §32.2, closure map §1 item 8 and §5, and the model's `plan_reached` and `oracle_same` follow it.

**Family assessment (convergence owner, "Review strategy after recurrence").** This is a non-local recurrence with one shared cause across 34803df B1, 0d2b35e B1, 83a82df B1, e548472 B1 and this finding: the row's reach is written as a formula over `⊑` and `cur` and patched by a disjunct per round, while the claim it is said to be "derived" from is a cur-free intersection of up-sets. Each repair added a disjunct for the shape the last Review exhibited. Siblings I checked: `r* ⊑ r` (the rejection denies the accepted revision itself; the formula reaches it exactly while the acceptance covers `cur`, so no release: held); `r ⊑ r*` with revert or loosening (SD-31's case: held); incomparable with a common tightening, before it is ever current (unreached; no consumer bites; it is unrouted but nothing is released); incomparable with a common tightening that was current and then left (this blocker); prose-different R2 targets (no common tightening; the disclosed new-target residual, unchanged); multi-item and objective-only rejections (per-item denial, under any objective: held). I stopped there: the remaining variants are the same intersection test.

**Options for the stakeholder (Phase C handoff §5).**

- **(1) Recommended, subtractive: derive the reach from the claim, without `cur`.** A rejection of `r*` reaches every acceptance naming `r` such that `r` and `r*` have a common tightening; by §13.4 that is: byte-identical item prose and equal values of every field §13.4 marks "unchanged" (equivalently the e548472 same-family B1 option (1)). One test replaces the three disjuncts and the `⊑`/`cur` reads; it is monotone in the item's history, so "a revert or loosening releases nothing" becomes true. Cost, beyond SD-31: an acceptance of a control-only branch incomparable with a rejected one is vetoed from the rejection's admission, even if the branches are never joined; route 3 lifts it with one record by the rejecter or the owner. R2 prose amendments stay new targets carried in the brief, as today. This partly reverses SD-31's choice of option 2 over option 1, which is why it is the stakeholder's.
- **(2) Minimal, keeps SD-31's reach for never-joined branches (adds mechanism).** Replace `cur` in disjunct 3 by "some revision of the item that has been current in the state's admitted history, `cur` included (in a frame, the frame's)". Once a join has been current the veto stays, so a later revert or loosening releases nothing; an S0 fold over admitted history is added to the reach.
- **(3) Keep the formula knowingly.** Delete "a revert or loosening releases nothing" from §5.10 (b), §0.3 R14 and the closure map; state in §32.2 that an R1 revert or loosening of `cur` below the common tightening of an accepted revision and an incomparable rejected one lifts the veto with no judgment, `PLAN_ACCEPT`, brief or owner routing; record that this departs from SD-31's purpose and the evidence owner's rule; keep §31.6 (V)'s contrast as an expected outcome. No mechanism, but it accepts the violation.

**Required discriminator.** §31.6 (V) gains B1's trajectory twice, with step 4 as the one-field loosening and as the exact revert to `r`: under (1) or (2), A is not issuable, `ADJUDICATE_DISAGREEMENT` stays derived, and `H`'s or the owner's `ACCEPTED (o, A@r')` (or `A@r`) restores issuance; the `a3 -> a3'` contrast is rewritten accordingly. An implementation whose plan reach reads `cur` only must fail. In the model, the plan oracle must state the claim (an intersection of up-sets) rather than the formula; `probe_claim_oracle.py`'s replacement is one way. Under (1) the scenario space needs no history; under (2) it needs a "has been current" set per scenario.

## Non-blocking findings

**N1 — Citation drift (editorial).** §0.3's closing paragraph says "the stakeholder decisions SD-11 to SD-30 are cited where they apply", and the §5.10 heading lists "SD-24, … SD-30", although SD-31 now governs the plan row and is cited in R14, §5.10 (b) and §16.5. Update both.

**N2 — A redundant disjunct (editorial).** `⊑` is reflexive (§13.4), so `r* = r` is a case of `r ⊑ r*`. Harmless; under B1 option (1) the whole list goes.

**N3 — The brief carry ends on a resolving acceptance that is itself vetoed (§16.5; family: carried-finding termination).** "It stays carried until a later plan acceptance of the item, admitted as independent and acting in the state (§5.2), records it `RESOLVED` … a `RESOLVED` entry in a non-independent, superseded or non-acting record ends nothing." A peer's independent acceptance that the standing rejection itself reaches and vetoes (for example a fresh `ACCEPTED(i3)` after a further tightening) is acting, independent and unsuperseded, so its `RESOLVED` ends the carry for every later acceptor's brief, although the derivation has just judged its conclusion contradicted. This is faithful to SD-31's wording ("an independent, acting resolution") and only affects disclosure, since the veto stands. Narrowing repair: a `RESOLVED` entry ends the carry only from a record with `base ≠ F` (not vetoed), or only from the rejecter's or the owner's record, matching SD-30's "never a peer's".

**N4 — Route-3 relief of a looser acceptance also relieves it for the rejected revision (disclosure).** After a revert to `r` below a rejected `r*`, the rejection cannot be superseded (its basis `r* ⊑ cur` fails), so its author ends the veto by relief: an `ACCEPTED (o, A@r)`. That relief judges `r`'s exact target, but by §7.9 an acceptance of `r` claims `r*`; if the principal later re-tightens to exactly `r*`, the relieved acceptance covers it and A is issuable on the very revision the still-standing rejection denies, with no adjudication derived. This is defensible as the rejecter's own later judgment, and the prior same-family Review held rejecter self-relief; but neither the relief rule nor the plan-acceptance brief tells the reliever that relieving a looser acceptance also clears every tightening of it, the rejected revision included. Suggested: state it in §5.10 (d) route 3 and in the `PLAN_ACCEPT` brief (no mechanism).

**N5 — The diagnostic model cannot see B1, and the disclosure understates why (§5.10 (g), §31.3; testing owner's proxy-proof rule; PEM DS-001).** §5.10 (g) says the oracle "reads what each kind claims and denies from the same table column". For the plan family it reads the column's *formula*, not its claim (`oracle_same`: `rz == rj or claims_rj or (covers_cur and cur in denied)`), so a gap between the column's claim and its formula is green by construction even though the scenario space contains the case (`cur = i2`, `p1`, a rejection of `iQ`, with `i3` the join). The model's plan scenarios also have no history, so they cannot express "a join that was current". `probe_claim_oracle.py` shows the cheap fix to the oracle; under B1 option (2) the scenario space would also need history.

**N6 — (g)6's parenthetical understates order-dependent admission (editorial).** "where admission itself depends on order (a reference not yet present), the derived values follow the admitted set". Admission also depends on order through basis currency at the head (step 6, including a plan supersession admitted only while its basis holds) and through `OBLIGATION_ANSWERED` (step 7). The rule stated ("the derived values follow the admitted set") is right; drop or widen the parenthetical so it does not read as the only case.

**N7 — Retained trade-offs (stakeholder options, not blockers), all disclosed in §0.3, §32.2-§32.3 or closure map §5:** bounded-only reproduction (partly narrowing SD-17); SD-24's provisional cap and the gate minimum; fresh D1/D2 re-gating after fences, overtaken re-application and replacement iterations (R4, R12); withheld cross-pending-frame support; adverse frame judgments surviving abandonment; the fenced-cutover half state; context-revert reuse after supersession; party exclusion from adjudication left to policy; two-sided, re-producer and unknown-authorship `authors` sets and their migration cost; an `INCOMPLETE` on a large scope widening every closure inside it; fixed `sat` hop direction; R2 plan amendments as new targets carried only in the brief; and the paraphrase-only 2026-10-12 adoption instruction.

## Closure audit

**None found beyond B1.** Basis: the Manual differs from `e548472` in seven hunks only (`git diff e548472 4c52205 -- orchestrator/docs/ssds-8.0-architecture.md`: §0.3 R14, the §5.10 (b) plan row, §13.4, §16.5, (g)6, §31.3, §31.6 (V)), all in the plan-row family; I re-checked §21 item 8 (plan structure, acceptance, amendment policy, invariants) against §11.1-§11.4, §13.4, §5.10 (b) and §16.5: substantively decided except B1's clause. I spot-checked items 3, 4, 7 and 22 against §3.4, §4.1-§4.4, §10.2-§10.4 and §30. I did not independently re-locate every §21 subordinate clause and every §16.2 row in this round; that is a gap (§13), mitigated only by the fact that no other normative text changed since candidates whose Reviews audited them.

## Refinements R1-R14

- **R1-R8, R10-R12:** text unchanged since `d6734c4`. I re-read R1 against §6.3 and §6.5 (one recorded execution basis, `on⁻` a function of the record and `K`'s bytes, `on⁺ ⇒ on⁻ ⇒ link⁻` by construction) and R12 against §5.2 and §7.3-§7.6 (the acting rule, the enactment unit, frame `record` entries). I found no unsoundness; R4 and R12 carry disclosed liveness costs.
- **R9:** sound as the exact-target base rule; its plan consequence is R14's.
- **R13:** sound; the authorship-keyed requirement and `nonind` read only S0 facts, and `base`, `stands⁻`, `relieved` and `eff` read them.
- **R14:** sound for the `EQUIVALENCE` and `COMPLETENESS` rows (composition read in either direction within covering classes; boundary completeness composes by union of sub-scopes, which I re-derived from §2.6's definition, and a superset's completeness claims nothing about a subset), for `asserts` (the conjuncts of `base` less vetoes) and for stratification (the reach reads `⊑`, `cur` and S1 status, all S0/S1). **The plan row needs different treatment (B1, SC-1):** its claim is the reviewed §7.9 claim, but its reach is not derived from it, and the property R14 states for it ("a revert or loosening releases nothing") is false.

## Re-verification of earlier findings (family level)

| Reviews | Findings | State | Basis |
|---|---|---|---|
| e548472 same family | SC-1, B1 | **partly closed**: the `r ⊑ r*` shape (revert or loosening below a rejected tightening of the accepted revision) is reached and liftable by route 3; the family **recurs** for incomparable revisions joined by `cur` (B1, SC-1 here) | §5.10 (b) disjunct 2; §31.6 (V); `plan_revert_exemption` caught; probes |
| e548472 same family | N1 (carry ends on any `RESOLVED`) | **closed** for non-independent, superseded and non-acting records; a vetoed record still ends it (N3 here) | §16.5 |
| e548472 same family | N2 ((g)6 over the admitted set) | **closed** in substance; parenthetical understated (N6) | §5.10 (g)6 |
| e548472 same family | N3 (two statements of the claim) | **closed** for the claim (§13.4 and §5.10 (b) both state §7.9's); the claim/formula gap is B1 | §5.10 (b), §13.4 |
| e548472 same family | N4 (model scenario space), N5 (trade-offs) | N4 **partly closed** (`cur` ranges over every revision, `i0L` added, mutation added; the oracle still shares the formula, N5 here); N5 retained (N7) | model source; §32.2 |
| e548472 different family | N1-N3 | retained as disclosed trade-offs, historical provenance and diagnostic scope (N7, N5 here) | §32.2-§32.4; §5.10 (g) |
| d6734c4 (different family) | B1 (brief selector), N1-N3 | B1 **closed** (every standing rejection naming an asked item, any revision, any objective, multi-item whole); N1 **closed** ((g)5 states the adverse exception); N2-N3 retained | §16.5; §5.10 (g)5 |
| 83a82df | B1 (a), (a′), (b), (c); N1-N5 | B1 (a), (a′), (c) **closed** (fresh peer acceptances reached; route 3); (b) **closed as disclosure** (R2 brief carry); N1-N5 closed or retained as recorded | §5.10 (b), (d); §16.5; §32.2 |
| 0d2b35e | B1 (a)-(c); N1-N5 | **closed** for an incomparable branch while joined (disjunct 3); open for the same branch after the join is left (B1 here); N1 closed (supersession while the basis holds); others closed or disclosed | model `plan_reach_path_only`, `plan_supersession_current_only` caught; text |
| 34803df, bf23372, a6ed164 | B1-B2 with siblings; N items | **closed** at family level for equivalence chains (either-direction reach, class cover), completeness unions, analyzer identity out of the reach, provisional-hop `asserts`, the authorship-keyed requirement and two-sided `authors`; per-item plan denial closed; the plan reach as above | §5.10 (a)-(b), §4.4; model mutations caught (§13) |
| 6b986de, 29da56e, 51070e5, 9e5a763, 051cce3, 63ddf91, f03b15e, 61cd09b | one `authors`; independence at Admission and in `base`; class rule; exact supersession targets; per-target relief; `COMPLETENESS` member revisions; cutover carriers | **closed** as far as re-derived: (e) refuses non-independent or under-class adjudications measured at the chain root; `nonind ⇒ base = F`; relief requires `acts`, `CLEAR`, `¬nonind`; §19.5 carrier rule unchanged | §5.10 (a), (d), (e); §8.3 step 3; model I2/I7 mutations caught |
| 362af9f, f22b4dc, both b46c250, f7419d5, 575dc78 | acting rule; enactment unit; `rid`; gate veto across runs; `gterm` | **closed** as far as re-read; not re-derived case by case this round | §5.2, §5.5, §7.6, §10.2; text unchanged since `d6734c4` |
| 5c55d4b, 27ef339, 0b6c4fa, a18b544, e9e6e9f, e2154ac, 3540d98 | `link⁻`, bounded reproduction, `UNBOUNDED` bases, content identity, gate qualification, equal-region partition | **closed** as far as spot-read (§6.5 construction rule, §1.4-§1.5 one representation, §1.4 rule 3 equal regions) | text unchanged since candidates whose Reviews recorded closure |
| 798b2b4, 71cf9b3, 86ab683, 1ffbbf0, 53669a5, d837363, cc005db, c6da678, b595f2c, 6ff4ed1 | the matching clause; the D1-D3 change rule and revising duty | **closed** as far as spot-read: `on⁻` reads only the record and `K`'s bytes; the revision-assessment record is a target condition in the run (`tgt`, §5.2, §10.2, §8.3 step 7), and the run is an S0 fact, so stratification is unchanged | as above |
| Phase B | §3 closures; N1-N4 carry-forward | N2 (completeness polarity) **holds**: a completeness judgment becoming `P`, blocked, revoked or loss-withheld removes only `bound` (permissive uses), never a `link⁻` match, so a differing old-content run stays in (2) and a yielding present-content run in (4) whatever width it recorded; support cycles are forced `F` (R2); corrupt prefixes halt (R3); N1 (paraphrase-only adoption) retained | §6.5-§6.6, §5.6-§5.7, §32.2 |

These rows record what I re-derived or re-read this round; for families whose text is unchanged since `d6734c4` I did not re-run every earlier trajectory individually.

## Out-of-matrix trajectories attempted

**Broke (B1):** incomparable accepted and rejected revisions joined by a tightening, then a one-field loosening below the join; the same with an exact revert to the accepted revision; the same on §31.6 (V)'s own `aQ`/`a0`/`a3`/`a3'` case.

**Weakened a disclosure:** a vetoed peer acceptance's `RESOLVED` ending the brief carry (N3); rejecter relief of a looser acceptance clearing a later re-tightening to the rejected revision (N4).

**Held:**

- revert, or a one-field loosening, below a rejected tightening of the accepted revision (reached by disjunct 2; route 3 lifts it with one record);
- a rejection of a revision looser than the accepted one (`r* ⊑ r`): reached exactly while the acceptance covers `cur`, so nothing is released;
- a fresh peer acceptance of a further tightening (reached);
- a multi-item rejection against a single-item acceptance (per-item denial), and a rejection under objective `o1` against an acceptance under `o2` (reached);
- the plan supersession admitted only while its basis holds, against route 3 (liftable where it bites, (g)4);
- an agent rejecter, relieved only by the owner;
- a frame-declared reliever in a pending candidate (does not act in `D`);
- `asserts`/`base` alignment for provisional judgments in the equivalence and completeness families;
- an `EDITORIAL` `NOT_EQUIVALENT` against a chain of `K` hops (not reached, correctly: editorial non-equivalence does not deny `K`-equivalence) and a `K` objection against an `EDITORIAL` hop (reached);
- a `COMPLETE` on a superset scope beside an `INCOMPLETE` on a subset (not reached, correctly: boundary completeness of a superset claims nothing about a subset);
- stratification of the plan reach (S0 `⊑`, `cur`) and of `stands⁻`/`relieved` (S0/S1 only).

## Minimum architecture and capability transfer

No primitive, component or persistent surface was added in this candidate; SD-31 removed an exemption. B1 option (1) removes the `cur` read and two `⊑` tests from one reach rule; option (2) would add an S0 history fold (marked as adding mechanism). Nothing the candidate removes drops an owner-required capability. §26.4's 1.6.0 supersession, the version-bound Core and the frozen profiles (PC-001) are textually unchanged; `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## Qualification design

§31.6 (V) now discriminates the e548472 B1 shape (revert or loosening below a rejected tightening), but its incomparable-branch contrast ("a tightening of `aQ` to `a3' ⋣ a0` is issuable") would certify B1 when taken after `a3`. Green fixtures can coexist with B1, as the model's do (N5). Nothing is claimed as executed beyond the G1 document checks and the diagnostic model, and the Manual marks the model as non-adequacy evidence (DS-001, §5.10 (g), §31.3).

## Doctrine-realization map and O1

§29's E0-E3 levels and the entrypoint rows are unchanged since `d6734c4`; I re-read the D3 role-contract rows against `source/roles/software-design/SKILL.md` at the public-source commit (D3 design contract items 1-7) and found them consistent as far as checked. §0.5 states the O1 content (the material realized record, readers, routine questions, product surfaces marked, none beyond the deliverable, and the realized-record architecture). Not re-derived row by row for every role and specialist this round.

## What I verified and how; what I could not verify

**Verified:**

- the Manual, closure map and workplan blobs at the candidate (`git rev-parse 4c52205:<path>`);
- `git diff --check e548472 4c52205`: clean (exit 0);
- `git diff --stat fad3ee4 4c52205 -- orchestrator/docs/architecture.md source dist`: empty, so those paths are byte-unchanged;
- `git diff --stat fad3ee4 bf23372`: 73 files changed, 23,269 insertions, 1 deletion, all under `orchestrator/docs/ssds-8.0-architecture.md`, `qualification/ssds80/` and the workplan authority index;
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the snapshot: 4 tests, OK;
- owner text quoted above, read with `git show aaeaf8b:<path>`: `source/roles/software-design/SKILL.md`; `source/shared/references/architecture-and-design.md` (line 66 "one authoritative representation/state"; line 88, Serious Challenge to D3); `abstraction-and-concretization.md` (line 51, the Serious Challenge predicate); `evidence-evolution-and-dependencies.md` (line 153); `workflow-and-workplans.md` (line 104); `convergence-and-cycle-economy.md` (lines 85, 87-89); `testing-and-validation.md` (proxy-proof real-owner evidence).

**Diagnostic model.** `qualification/ssds80/judgment_disagreement_model_check.py` from the snapshot, run with `--mutations` semantics in parallel: a driver imported the module (`python3 -I`) to read `CORE`, `FAMILIES` and `MUTATIONS`, then ran each job in its own process, which imported the module, cleared `MUT`, added at most one mutation and called `run_family`. There were 4 unmutated jobs, one per family, and one job per (mutation, family it names): 28 mutation jobs for the 26 entries (`asserts_requires_clear` and `requirement_request_colocated` name two families), 32 jobs in all. This is the set `main()` runs.

**Unmutated** (exit status 0 for every job):

| Family | Cases | Invariant failures |
|---|---|---|
| transformation-review/acceptance/gate | 789,396 | none |
| equivalence-chain | 299,760 | none |
| completeness-cover | 37,600 | none |
| plan-coverage | 119,560 | none |

**Mutations.** Every one of the 26 was caught in every family it names:

| Caught by | Mutations |
|---|---|
| I1/I3 and I2 | `relief_ignores_nonind` |
| I1/I3 | `wide_review_supersession`, `gate_run_veto`, `base_ignores_nonind`; `asserts_requires_clear` in completeness-cover |
| I7 | `eligibility_support_tier_only`, `challenged_record_authors` |
| I7 and I1/I3 | `no_class_check` |
| I5 | `frame_acts_everywhere` |
| I8 | `obligation_direct_only` |
| I4 | `plan_supersession_current_only` |
| I1/I3 and I8 | `endpoint_only_equivalence_reach`, `directed_chain_only`, `chain_ignores_class`, `asserts_requires_clear` (equivalence-chain), `completeness_exact_only`, `completeness_reach_analyzer_id`, `requirement_request_colocated` (both families), `plan_reach_names_only`, `plan_reach_any_tighter`, `plan_reach_current_only`, `plan_rejection_denies_set`, `plan_reach_path_only`, `plan_fresh_acceptance_exempt`, `plan_no_relief`, `plan_revert_exemption` |
| I7, I1/I3 and I8 | `eq_authors_to_side_only` |

A green run is a diagnostic of the written rules inside the modelled envelope; by N5 it does not bear on B1.

**Probes** (scratch, importing the module unmodified): `probe_join.py` (B1's model trajectory and the 104/14 divergence count) and `probe_claim_oracle.py` (the plan family with the oracle's plan reach replaced by the column's claim), reported in B1.

**Not verified:**

- an independent re-location of every §21 subordinate clause and §16.2 row this round;
- an individual re-derivation of every pre-`a6ed164` finding (families re-checked at the level stated in §8);
- PEM schema and publication state (I read DS-001 and PC-001 in the candidate's `PROJECT-ENGINEERING-MEMORY.md` as hypothesis sources only);
- runtime behaviour (no implementation exists) and G2-G4 evidence.

## Scientific checks

- **Material findings:** SC-1, B1 and N1-N7, all about D3 judgment-disagreement rules and their qualification; none about D1/D2 content.
- **Realized results:** I produced, ran or reviewed none. The model runs and probes are software diagnostics of the Manual's written rules, envelope stated in §13.
- **Variants:** I evaluated more than one variant of one thing: three plan-reach rules (the candidate's formula, B1 option (1) and option (2)) against one criterion, agreement with the column's §7.9 claim and with the property "a revert or loosening releases nothing", over B1's trajectory and the siblings listed in B1; and two plan oracles (the model's and the claim-reading replacement) over the model's own plan scenarios.
- **D1/D2 authority:** I relied on none for a consequential judgment, so no tension search was needed.
- **Gaps:** as listed in §13.

## Common-mode note

**Family and engagement.** I am of the Claude family, the Manual author's, launched in fresh context by the authoring session. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4 and e548472 Reviews and the Phase B Review were of the GPT family; the others, including the same-family e548472 Review whose SC-1 SD-31 answered, were of the Claude family.

**Shared dependencies.** I share with the author and the earlier Reviews the corpus, the inherited workplan framing, the prior Review records (read as hypotheses; I read the two e548472 records after forming the B1 analysis, and B1 is a sibling of the same-family record's B1, so that record's framing is a shared dependency), the toolchain, and the candidate's own diagnostic model, whose oracle shares the plan formula. The two e548472 Reviews disagreed on whether a revert release is a defect; SD-31 settled that for one shape, and B1 applies SD-31's own settlement to another. A different-family reviewer may weigh the release case as the e548472 different-family Review did ("older acceptable controls are reusable"); the stakeholder should read B1 as an application of SD-31's purpose, not as a new principle.

## D4 statement

This Review authorizes no D4 and accepts no architecture, product scope or default value. A PASS would have been technical evidence for G1 only. SSDS 8 D4 remains NOT AUTHORIZED.
