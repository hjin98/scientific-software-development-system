# Independent D3 Review — SSDS 8 Architecture Manual, candidate c4e8de7

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          c4e8de7ecd6770020cc36923b8e37321bb82cd74
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g));
                        technical evidence for G1 only
    MANUAL blob:        d36d644e04ad1aaee30de9f606f6ddc26cfaeb49 (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   981627f03f9f2f6f7f857db5347a23f123b289b0 (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family 494c810
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; delta-first attack of the lowered
                        state's exits as restated (events' resolution, or a deciding record AMEND,
                        RESOLVED_BY or the human's judgment after ESCALATE; every lowering stands once
                        its content moved; no-plan obligations by §12.5), in both directions, over every
                        state of an enacted obligation (unlatched, latched, waiting, routed, retired) and
                        every exit, against the reviewed workplan §7.9 and its digest rule, the workflow,
                        evidence and architecture owners, and the Manual's own owners of the records the
                        exits use (§3.4, §3.6, §4.3, §5.4, §8.3, §10.2-§10.4, §12.4-§12.5, §15.2-§15.6,
                        §16.7-§16.8, §23.6, §31.3-§31.4, §32.3); drift classes applied to every statement
                        of the deciding record and its consumers; an independent probe of the lifecycle
                        oracle (lc_oracle) on post-retirement histories; family-level recheck of earlier
                        families against the delta; the diagnostic model with every family and mutation,
                        in parallel; the structural checks of handoff §3 step 9
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched
                        by the authoring session; did not author the candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-c4e8de7/snap`. The later commit adding the handoff (`8daa6005`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. SSDP 7.2.1, the reviewed workplan and the stakeholder's recorded decisions (SD-1 to SD-35, record items 19 and 31) can be realized together. The blocker below lies in R15, an author choice under record item 31 that closure map §5 (line 298) lists for the stakeholder to confirm or reverse, and it is routed against the proposed D3 owner. This is the eighth round in the obligation-lifecycle family (edabd81 N7, 82d618c B1, 095ce55 B1, c77447b B1, 3940dbc B1, 3876473 B1, 494c810 B1). The question whether R15 should exist has now been put to the stakeholder by three records (3940dbc, 3876473, 494c810), and the continuation handoff (`PHASE-C-CONTINUATION-HANDOFF-SSDS-8.0.md`, line 24) says that if this family fails again at a new coupling the stakeholder question "should be raised rather than another repair". It has failed again; I repeat the question below as option 2 and recommend that it be put now.

## Verdict

**NO-PASS.** One blocker, B1, in the obligation-lifecycle family. The candidate's repair of 494c810 B1 holds at the transitions that record named:

- successor retirement is deleted; a later obligation of the same kind on the same scope retires nothing (§10.4, line 1323);
- every lowering event on a line whose content has moved stands, so the post-move veto case no longer waits with no actor (494c810 B1 (b) closed);
- a decision owed has named outcomes (§15.5 lines 1657-1669), re-partition cannot reach a latched obligation (§13.7, line 1538), and the decision brief labels later same-kind obligations as not having seen the events.

What the candidate does not get right is the one state it added, **retired**, and the records that put an obligation into it. The deciding record is defined in two places (§10.4 and the §15.5 table) and is unknown to every owner of the records it uses: the closed schema and record-kind table (§3.4, §3.6), the basis minimum (§4.3), the persistence rule for resolving records (§15.2, §5.4), the human-decision vocabulary (§3.4) and the trigger table (§10.2). And retirement has no exits: it is absorbing for every later event and for the revocation of the record that caused it.

The diagnostic model is green on all six families and catches all 52 mutations (lifecycle: 1,485,256 scenarios; I11 and I12 hold). Its lifecycle family, and its oracle, return `retired` at the first decision and process no later event, model no schema, and give a deciding record no standing. So B1 is green by construction (N1).

## Blockers

### B1 — The retired state has no exits, and the records that enter it are defined only where they are used

**Family:** obligation lifecycle after integration (82d618c B1, 095ce55 B1, c77447b B1, 3940dbc B1, 3876473 B1, 494c810 B1). It enters through the repair of 494c810 B1: that record's option 1 (one exit by decision, with named outcomes), realized in §10.4 and §15.5 but not at the record owners, and with retirement made terminal.

**Earliest owner:** Manual §10.4, "A latched obligation is never ready again" (line 1323), with §15.5 (lines 1657-1669) and §3.4 (lines 473, 475). Workplan §21 item 7 ("obligation rules …, readiness, three-valued discharge"), item 3 ("closed record schemas, judgment kinds and tiers") and item 26 ("the outcome table for coordination decisions") contribute.

**Status:** open, material, non-local.

**Exact rules at the candidate.**

- §10.4 (line 1323): "The lowered state ends only when its events are resolved, or by a deciding record (§15.5): an `AMEND` decision …, a `RESOLVED_BY` decision naming the admitted records or discharged obligations that dealt with its events, or, after `ESCALATE`, the authenticated human judgment answering that attention, which states one of those outcomes or accepts the lowering with its reason. Each **retires** the lowered obligation: no longer required, kept as history with its deciding record. Nothing else retires it". The same paragraph: "once a later admission has changed the content a line's record judged, every lowering event on that line **stands** … Standing decides only the route: a later resolution of the event still restores the line."
- §15.5 (line 1667): "`RESOLVED_BY` | the events lowering a latched obligation were dealt with by the named admitted records or discharged obligations; retires it (§10.4) | a lowered latched obligation whose subjects are not D1 or D2 authority and none of whose lowering events is a floor event (§15.4); otherwise `ESCALATE`". Line 1669: "For a decision owed on a lowered latched obligation, the allowed outcomes are `AMEND`, `RESOLVED_BY` and `ESCALATE` … An `AMEND` decision is followed by a plan-unit change authored by the principal in the same coordination request".
- §3.4 (line 473), the record-kind table, a `[D3 decision]`: "`COORDINATION_DECISION` | report(s) or item; `PARTITION` names tasks | `RESOLVE_LOCAL`, `AMEND`, `CHALLENGE`, `ESCALATE`, `DECLINE`, `PARTITION` | principal; R1 | — | not in force; the report's obligation reopens". Line 475: "`HUMAN_DECISION` | a human-attention obligation | `ACKNOWLEDGE`, `ANSWER`, `ACCEPT`, `REJECT`, `REDIRECT`, `MOOT` | authenticated human; R3 | — | not in force; attention reopens".
- §3.6 (line 532): "The schema is **closed**: Admission rejects a record with … a value outside its grammar (C5)"; §3.2 (line 427): `outcome` is a "per-kind enumeration"; §8.3 step 1 (line 1171) applies it first.
- §4.3 (line 580): "`COORDINATION_DECISION` | `identity` on the reports it resolves; `content` on the plan items it names".
- §5.4 (line 705): "`COORDINATION_DECISION`, `MATERIALITY_RECLASSIFICATION`, `HUMAN_DECISION` (as resolving records) | none | none (S3) | not in force; obligations reopen". §15.2 (line 1630): an obligation "closes only when a **resolving record** targets the report by `identity` and stays in force: not superseded, not `REVOKED` or `BLOCKED`, not withheld by a later loss boundary".
- §12.4 (line 1420): R1 decisions are "coordination decision or plan-unit change; challengeable; never acceptance". §0.4 allocation (line 148): "routine coordination -> the principal role, recorded and challengeable".
- §10.2 (line 1268): `HUMAN_ATTENTION(r)` is triggered by "a report or floor event routed to the human (§15)"; the candidate deleted from this row "a latched obligation outside any plan lowered by a standing event". §12.5 (line 1428): "Decisions owed on obligations that belong to no plan … route to its principal; with no standing plan they route to the human."
- §15.3 (line 1644): a `ROUTINE` finding derives "`COORDINATE` only if it names a unit of an open item". §5.3 (line 695): "Repair of a revoked triple therefore needs a new revision and acceptance".
- §31.4 (line 2670), the Manual's own discriminators: "a lowered obligation repaired by a new item is retired by the principal's `RESOLVED_BY` naming it, never left `OPEN` or recorded as withdrawn"; "a latched joint-invariant review revoked after a later change … derives a decision … that persists until a deciding record retires it".
- Closure map line 298 (not the Manual): "a retired obligation is history and later findings against its records reach only current-state obligations".

**(a) The deciding record is not a record the schema admits.** `RESOLVED_BY` is not in `COORDINATION_DECISION`'s closed outcome enumeration, and "a lowered latched obligation" is not among its target types. A `HUMAN_DECISION` has no `AMEND` or `RESOLVED_BY` outcome, and which of its six outcomes "accepts the lowering with its reason" (and whether `ACKNOWLEDGE` or `REDIRECT` retires) is undefined. The basis minimum gives the decision no entry on the lowering events or on the records it names.

1. Item `I` (plan `P`, a D4 subject) integrates `X`. Reviewer `V`'s `REVIEW` passes and the item latches `T`.
2. A challenge that `X` misses contract criterion `c3` is upheld; `V`'s review is `REVOKED`; the event stands, and `COORDINATE(P)` is owed.
3. The principal plans repair item `J`; `J` integrates and its obligations discharge.
4. The principal submits `COORDINATION_DECISION` with outcome `RESOLVED_BY` naming `J`, as §31.4 expects. A §3.4/§3.6-conforming Admission rejects it at step 1 (`SCHEMA_*`: outcome outside the kind's enumeration; target type not "report(s) or item" for a records-only obligation).
5. The only admissible outcomes left are `AMEND` (re-work under a contrived new key, or withdrawal of delivered work, which §31.4 forbids as the repair route) and `ESCALATE`. After `ESCALATE`, the human's `HUMAN_DECISION` has no outcome meaning "resolved by `J`"; whatever an implementer maps it to is a choice §10.4 does not make.

An implementation that follows §15.5 instead admits the record, with no schema version, no target grammar and no basis entries: two statements of one record, and the implementer must choose. If the human states `AMEND` (line 1323 allows it), the human's judgment retires the obligation at once, but the amendment is "a plan-unit change authored by the principal in the same coordination request" (line 1669), which a `HUMAN_DECISION` is not. Nothing then derives the amendment: re-work decided, never owed.

**(b) Retirement is absorbing, and its deciding record has no standing.** §10.4 retires unconditionally ("kept as history with its deciding record"), while the same record kinds, as resolving records of reports, count only while in force (§5.4, §15.2, §3.4's last column). Three trajectories, each conforming to §10.4 as written:

- **(b1) Decision pre-empts an adjudication.**
  1. An open blocking challenge `c` against `V`'s review (D4, `ROUTINE`, so no floor) is admitted.
  2. A later item edits `Δ(X)`. By line 1323 every lowering event on the line now stands, so a decision is owed, although `ADJUDICATE(c)` is challenge-tier and still admissible (N3).
  3. The principal records `RESOLVED_BY` naming an unrelated admitted record (no admissibility condition relates the named records to the events, N4). The obligation retires.
  4. An independent adjudicator upholds `c`. Upholding is not a "resolution" that restores; the obligation is retired; nothing is derived. The upheld finding was not in existence when the principal decided, and no one decides it.
- **(b2) A later finding against the same work reaches no decider.**
  1. As (b1) step 3, retirement by `RESOLVED_BY` for event `E1` (say a loss over moved content).
  2. A challenge against the produced subject revision `S` (a defect in `X`'s product content, D4, `ROUTINE`) is upheld: `status1(S) = REVOKED`. Had the obligation not been retired, this would lower it and derive `COORDINATE(P)` (as it does with no earlier event: the model gives `(0, 'coord')` for `('revoke_S',)`).
  3. Retired, it derives nothing. The `ROUTINE` finding names a unit of no open item (§15.3), so no `COORDINATE`; no floor applies, so no `HUMAN_ATTENTION`. §5.3 says repair "needs a new revision and acceptance"; I found no current-state obligation that asks anyone to produce that revision for a revoked D3/D4 subject, and closure map line 298's "reach only current-state obligations" names none. Whether an upheld finding against integrated, unchanged content reaches a decider depends on whether an unrelated earlier event was once decided.
- **(b3) Challenging the decision changes nothing.**
  1. As (b1) step 3.
  2. A qualified actor challenges the `RESOLVED_BY` ("`J` does not touch the criterion the upheld challenge found missing"), and an eligible adjudication upholds it.
  3. §10.4 states no in-force condition, so the obligation stays retired. R1's only safeguard, that it is "challengeable" (§12.4, §0.4), has no effect on the one R1 decision that ends an upheld finding against integrated work. A loss boundary withholding the decision is likewise unaddressed (`REQUALIFY` covers "a permissive record or relaxer"; whether a retiring decision is one is unstated).

Probe at the candidate (`scripts/probe.py`, unmodified snapshot module): `lc_value` and `lc_oracle` both give `(0, 'retired')` for `(block_R, content_change, decide_resolved)`, `(block_R, content_change, decide_resolved, revoke_R)` and `(revoke_R, decide_resolved, revoke_S)`; neither has an event for the decision's revocation.

**(c) The direct route to the human has no trigger and no exit.** With no standing plan (§12.5 permits it), a lowered obligation of no plan (a `JOINT_INVARIANT(i, k)` of an absorption, a `SPEC_REVIEW(spec, r)` of a direct human change) is owed a decision that "route[s] to the human". The candidate removed the `HUMAN_ATTENTION` trigger that carried it (line 1268 now names only reports and floor events), and the human-judgment exit is stated only "after `ESCALATE`", which no principal made. Read literally, no obligation carries the decision and no record ends it: the 494c810 B1 (c) "no exit without an item" case, closed for projects with a standing plan and reopened for projects without one.

**Shared cause.** Each round has moved the defect to the next state's exits: return to ready (3876473), waiting and successor retirement (494c810), now retirement itself. The candidate defined retirement as an S3 transition in §10.4 and an outcome row in §15.5, and did not carry it to the owners of the records it reads. This is again two places computing one thing, in three pairs:

- the deciding record in §10.4/§15.5 versus its kind, outcome, target and basis in §3.4, §3.6 and §4.3;
- retirement versus the persistence of every other resolving decision (§15.2, §5.4) and the challengeability of R1;
- the no-plan route in §10.4/§12.5 versus the trigger table (§10.2) and the human-decision vocabulary.

Discovery stops here. Further variants re-derive (a)-(c): a `RESOLVED_BY` naming a discharged obligation later lowered; a withdrawal `AMEND` (content stays integrated, retirement equally absorbing); a lowered partition part.

**Controls that hold.**

- A discharged later obligation of the same kind on the same scope retires nothing, in either order (the 494c810 discriminators for (a)).
- A peer `NO_PASS` or a gate `REJECT` recorded after the content moved stands and derives the decision at once (model `veto_R, content_change` → `coord`).
- `RESOLVED_BY` is refused by §15.5 for D1/D2 subjects and floor-event lowerings (subject to N5).
- No re-partition reaches a latched obligation; re-integration claims are refused at step 7.
- A latched obligation is never ready (I12), a continuation after the content moved is refused, `P` latches as `P`.
- An open blocking challenge whose content is unchanged waits on `ADJUDICATE(c)` and is restored by its dismissal; a dismissal after the content moved still restores the line (model and Manual agree).
- `AMEND` by the principal: the amendment changes the key, so the old obligation is structurally no longer derived and the new one is owed; a rejected amendment derives `COORDINATE(plan)` through the plan-acceptance trigger.
- The derivation stays stratified: retirement and routing read S3 obligations other than the latched one and records below S3.

**Violated owner text.**

- **Reviewed workplan §7.9, Persistence** (Phase B candidate, line 1675): an obligation derived from a report or challenge "closes only when a **resolving record** targets the report by `identity` and stays in force: not superseded, not `REVOKED` or `BLOCKED` (S1), and not withheld by a later loss boundary". Its digest rule (line 1875): "Every digest item is challengeable … an upheld challenge restores whatever it covers." (b3).
- **Reviewed workplan closed schema** (Phase B candidate, line 1048: records "serialized in a canonical versioned **closed schema**"; line 1407, Admission step 1) and **Manual §3.6, C5** ("unknown required semantics fail closed") (a).
- **Workflow owner** (`aaeaf8b:source/shared/references/workflow-and-workplans.md`, line 96): "close each material impact item as resolved, preserved-with-reason, or unavailable/blocking". (b1) and (b2) close an upheld finding with none of these.
- **Architecture owner** (`architecture-and-design.md`, line 96): "define it before dependent invariants use it: … lifecycle states and transitions" (the retired state has no transitions out; its entering record has no definition at its owner).
- **Manual §0.4 A8** (line 129): "a material finding survives to its owner" ((b1), (b2) where the finding is material and below a floor).
- **The Manual's own statements**: §31.4's repair-by-new-item discriminator against §3.4/§3.6 (a); §12.4 and §0.4 "challengeable" against §10.4 (b3); §12.5 "route to the human" against §10.2's trigger row (c).

**Convergence assessment.** A non-local recurrence: the eighth round, and the fourth in which the defect sits in an exit of the state set rather than in the latched value. The value rule has held for two rounds, and this round's controls agree. The active simplification trigger applies ("repeated patches around the same mechanism … patch-on-patch repair"), and the continuation handoff itself names this condition as the point to stop repairing and raise the R15 question. I therefore give options, not a repair.

Options for the stakeholder (Phase C handoff §5):

1. **Make retirement event-scoped and persistent (narrows mechanism: removes the terminal state for every outcome but `AMEND`).**
   - A deciding record that stays in force ends the lowered state *for the events it names*: those events count as resolved for the latched value, and the obligation stays latched (never ready, its lines still computed).
   - A later event not named lowers it again and owes a new decision; a deciding record not in force (revoked, superseded, withheld) re-lowers it. This is §15.2's persistence applied to one more resolving record, so §5.4's row already says it.
   - `AMEND` keeps its structural effect: the key changes, so the old obligation is no longer derived.
   - Carry the record to its owners: `RESOLVED_BY` (and a target "lowered latched obligation", with `identity` basis on the lowering events and on the named records) in §3.4 and §4.3; the human's answer mapped onto `HUMAN_DECISION` (`ACCEPT` with reason codes for "accept the lowering"; `REDIRECT` to return `AMEND`/`RESOLVED_BY` to the principal, who alone authors the plan-unit change); the `HUMAN_ATTENTION` trigger restored for the no-standing-plan route.
   - The schema rows add mechanism; the deleted terminal state removes it. Also consider N3 and N4, which shrink what a principal can pre-empt.
2. **Withdraw R15** and return to the reviewed §7.4 current-state discharge, with step 8 narrowed to evidence regression (82d618c option 2). This re-introduces drift re-dispatch, which R15 exists to remove, and removes the family. This is the fourth record to put it; I recommend that the stakeholder decide it before another candidate.
3. **Keep terminal retirement and disclose it in the Manual** (not only closure map line 298), restricting `RESOLVED_BY` to events whose line content has moved and adding the schema rows of option 1. This keeps (b2) as a stated cost and adds mechanism; I do not recommend it.

**Required discriminator.** At the real owners (Admission steps 1-3 and 6-9 → Derivation discharge → obligation derivation → Dispatcher → principal and human views):

- A lowered item repaired by item `J`; the principal's `RESOLVED_BY` naming `J`. Expected: admitted under a declared schema with its basis, and the obligation's lowered state ended (positive control for (a)).
- The same, followed by an upheld challenge of that `RESOLVED_BY`, and separately a loss boundary withholding it. Expected: under option 1, lowered again with a decision owed.
- `RESOLVED_BY` while a blocking challenge is open (content moved), then the challenge upheld. Expected: a decision is owed on the upheld finding (or, with N3's repair, no decision before the adjudication).
- `RESOLVED_BY` for event `E1`, then an upheld challenge on the produced revision. Expected: a decision owed (option 1) or the Manual-stated current-state route (option 3), never nothing.
- `ESCALATE`, then each `HUMAN_DECISION` outcome. Expected: a defined effect for each; a human `AMEND` derives the principal's amendment rather than retiring with nothing owed.
- No standing plan; a lowered `JOINT_INVARIANT(i, k)` of an absorption. Expected: `HUMAN_ATTENTION` derived, and the human's judgment has a defined effect.
- Negative controls: the 494c810, 3876473 and 3940dbc discriminators, which must still hold.

§31.4 has none of the post-retirement cases, and its repair-by-new-item case expects an outcome the closed schema refuses (DS-001).

## Non-blocking findings

### N1 — The lifecycle model and its oracle share terminal retirement, and omit the decision's standing

Both `lc_value` and `lc_oracle` return `(0, 'retired')` at the first decision event and read no later event; neither has an event for a decision's revocation, supersession or withholding; neither models the record schema, the decision's admissibility or the human's outcomes. Both admit `decide_resolved` while a blocking challenge is open after a content change. §31.3 discloses that "the floor restriction of `RESOLVED_BY`, the effect of an `AMEND` on the item and `SPEC_REVIEW`, item-level-review and findings-only cases are not modelled", and that the oracle "reads the same event list". Further:

- The oracle's docstring states the protected property as "only that decision ends it". That is the candidate's rule, not an owner property: the owners require the decision to stay in force (B1 (b)). A wrong rule shared by both sides is green.
- One global `moved` flag stands for "the content a line's record judged has moved"; the Manual's condition is per line (the evidence line's claim content and the review line's `Δ(X)` can move separately).
- The peer gate decision of 494c810 N2 enters as a floor on the gate line; no event acts on it (N2).

A stronger oracle would decide each event's effect from the owners' rules in the state where it occurs, including events after a decision. That is diagnostic mechanism, not architecture.

### N2 — A later peer gate decision is a full line, so any event against it lowers the item

The repair of 494c810 N2 adds "any later eligible decision on the same gate and triple, which enters the minimum as in §5.5" (line 1321). The line rule then applies to it whole: an open blocking challenge, an upheld challenge or a loss boundary against a decision the item never relied on lowers the latched item to `F`, and once the content has moved it stands and owes a decision (for a D1/D2 subject, `ESCALATE` to the human). This is consistent with current-state `gterm`, where a non-current eligible decision lowers the term, and it fails closed. But 494c810 N2 asked only for the qualification asymmetry ("caps the gate line at `P`"), and the wider consequence is not disclosed in §32.3 or closure map §5. Either restrict the later decision's contribution to `unq` (a `P` cap), or list the consequence with the R15 costs.

### N3 — "Stands" covers open challenges whose adjudication is still admissible

Line 1323 derives "every lowering event on that line stands" from the inadmissibility of support-tier answers after the content moves ("A support-tier answer … is admissible only while the content it judges is current …, so …"). The inference holds for vetoes, losses and failing assessments; it does not hold for an open blocking challenge, whose `ADJUDICATE(c)` is challenge-tier and stays admissible (the 494c810 record's control "adjudication is challenge-tier and admissible"). The result is a principal decision owed while an adjudication is pending, which the principal may pre-empt (B1 (b1)). §32.3 discloses only "a lowering resolved after an `AMEND` leaves the amended re-work". Removing open challenges from the standing set (they wait on `ADJUDICATE(c)` whatever moved) removes an exception and the pre-emption.

### N4 — `RESOLVED_BY` has no admissibility relation to what it resolves

Admission checks only that the named records exist (step 2) and the §15.5 floor and domain restriction. Nothing requires the named records to be admitted after the events, to touch the lowered line's target or scope, or to be independent of the lowered work. An R1 decision ("never acceptance", §12.4) thereby ends the effect of a finding that an R2/R3 adjudication established; the brief's "labelled as not having seen them" is advice to the principal, not a check. With B1 (b) repaired this is bounded by challengeability; without it, it is not. Suggest at least that the named records postdate the events and lie on the lowered line's target or scope.

### N5 — "Floor event (§15.4)" and "subjects … not D1 or D2 authority" are undefined for the obligations that use them

§15.4 defines floors for reports; "floor event" is defined in §6.8 for failing assessments only. Whether a challenge against an `EVIDENCE_SPEC` unit in a D2 domain is under the domain floor ("computed from the target's effective kind and domain") is unclear, and §10.2 says such a unit is not a `NATIVE` D1/D2 subject. So whether the principal may `RESOLVED_BY` an upheld finding that a D2 tolerance was widened to fit a failing backend (the 494c810 `SPEC_REVIEW` variant; §29's D2 row) is undetermined, as are the "subjects" of a `JOINT_INVARIANT(i, k)` whose scope includes D1/D2 units. State both for records-only obligations.

### N6 — Editorial and drift

- §10.3 (line 1293) still says a latched obligation, when lowered, "is routed to the principal"; §10.4 routes no-plan obligations by §12.5, possibly to the human.
- §10.3's "the vetoed record then blocks no work" (asked to be reconciled by 494c810 B1 (b)) is unchanged; under R15 such a veto stands for a latched obligation and owes a decision.
- §16.7's decision brief is still described as "each led by the report's record core"; the brief of a decision on a lowered obligation is stated only in §15.5.
- The §15.5 table allows `AMEND` for "a lowered latched item obligation", the paragraph below it for every lowered latched obligation (records-only ones included).
- The `JOINT_INVARIANT` trigger now excludes `OVERTAKEN` admissions, and `late(n)` keeps `pub(n) = OVERTAKEN`. For an accepted late publication the joint-invariant review is presumably the one the absorption reaching `C_n` derives; say so.

## Closure audit

I used the closure map to navigate and checked its R15 claims against the Manual. The Manual delta since 494c810 is fifteen hunks: 100 (R15 row); 656 (acting records: re-work of an amended item); 1256, 1268, 1271 (triggers); 1321, 1323 (§10.4); 1538 (§13.7); 1657, 1662, 1667, 1669 (§15.5); 2230 (§23.6 requalification kinds); 2664 (§31.3); 2670 (§31.4); 2771 (§32.3). Closure map lines 87, 298 and 313 changed. No other file under the Manual's owners changed (`git diff --stat 494c810 c4e8de7 -- workplans PROJECT-ENGINEERING-MEMORY.md tests` is empty).

| Item | Disposition at this candidate |
|---|---|
| 7 (obligation rules, readiness, discharge) | **open (B1)**: the retired state's exits; the value rule and the waiting rule hold |
| 3 (closed record schemas) | **partly open (B1 (a))**: the deciding record and its target are absent from §3.4's closed enumeration |
| 26 (reports, escalation, coordination outcome table) | **partly open (B1 (a), (c))**: the §15.5 rows are not in the schema; the human-decision mapping and the no-standing-plan trigger are missing |
| 9 (joint invariants) | **partly open (B1 (c))** for a no-item joint-invariant review in a project with no standing plan; the successor case is closed |
| 6 (Admission validation order) | sound, except that step 1 refuses what §15.5 offers (B1 (a)) |
| 13 (publication), 18 (migration, cutover) | the latch undone by a fence or `OVERTAKEN` holds; records-only `OVERTAKEN` answers no longer derive a stranded joint-invariant obligation (494c810 N6 closed); N6 here for `late(n)` |
| 1-2, 4-5, 8, 10-12, 14-17, 19-25, 27 | text byte-unchanged since 494c810 outside the hunks above; no unresolved architectural decision found in this bounded audit (see the re-verification below for its basis) |

§16.2 rows (both tables): byte-unchanged since 494c810. §26.4 keeps an explicit replacement, retirement or preserved boundary for every row; I found none unresolved. Material decisions remain marked `[D3 decision]` and distinguished from `[delegated]` D4 space. Apart from B1, I found no under-specification an implementer would have to settle architecturally.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1 | Sound; unchanged. Phase B N2 closed in text (below) |
| R2, R3 | Sound fail-closed SCC clamp and integrity halt; unchanged |
| R4 | Sound; unchanged. The fence undoes an R15 latch, and the joint-invariant trigger now excludes fenced and `OVERTAKEN` admissions |
| R5-R8 | Sound; unchanged |
| R9 | Sound; "an answered obligation is never ready again" and "a latched obligation is never ready again" agree |
| R10-R14 | Sound; unchanged. The plan row's closed form is a stakeholder-chosen conservative policy (SD-32 to SD-35) |
| R15 | **Sound as a value rule and as a waiting rule; its retired state is unsound (B1).** Deleting successor retirement and making post-move lowerings stand close 494c810 B1 (a)-(b). The decision exit is realized in §10.4 and §15.5 but not in the schema, basis, persistence and trigger owners, and retirement is absorbing. The change from the reviewed §7.10's mechanical re-iteration (R0) to a principal decision (R1) after a lowering is surfaced (closure map line 298) and is a stakeholder trade-off, not a blocker. An author choice under item 31; options to the stakeholder (B1) |

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **D** design or disclosure closure, with real-owner execution owed later; **R** retained as a disclosed decision or stakeholder option; **P** partly closed.

**Basis.**

- I re-derived the delta's mechanisms independently (B1 and controls above).
- I re-checked families the delta does not touch in three ways:
  - by the full model run (all six families green, all 52 mutations caught);
  - by confirming their text is byte-unchanged since 494c810 (`git diff -U0` lists only the hunks above);
  - by reading their owner sections at the candidate where the delta couples to them (§3.4, §4.3, §5.3-§5.5, §8.3, §10.2-§10.4, §12.4-§12.5, §13.7, §15.2-§15.6, §16.7-§16.8, §22.2-§22.3, §23.6).
- I did not replay earlier records item by item. For records before 494c810, the dispositions are those the 494c810 record gives, re-checked at the family owners above and against the unchanged text. Those records are mostly of this reviewer's family, so they are hypotheses carried, not independent confirmation.

**Mechanisms independently checked at this candidate:**

- **494c810 B1.**
  - (a) Successor retirement closing an upheld finding: deleted; "a later obligation of its kind on the same scope does not" retire (line 1323); §31.4 tests both orders. **C**
  - (b) Waiting on a route no actor takes after the content moved: every lowering on a moved line stands and derives the decision. **C** (with N3's over-reach for open challenges)
  - (c) Incomplete routed exits: outcomes named in §15.5, re-partition excluded, no-plan routing by §12.5. **P**: the schema, human mapping, no-standing-plan trigger and the retired state's own exits are B1 here.
- **494c810 N1-N6.**
  - N1 (oracle admissibility of `adjudicate_R` and `fail_E` after a change; omitted exits): the owner's ending of a veto is now refused after a move, and `fail_E` lowers on the read revision in both sides; decisions and successors were added. **P** (N1 here).
  - N2 (same-triple qualified decision ignored): now enters the minimum. **C**, with N2 here on its breadth.
  - N3 (`IMMATERIALITY` currency): "for a failure disposed of at `D_m`, that disposition's line decides, not current `disp`". **C**
  - N4 (unstated costs): `P` for good, re-application key, partition-wide amendment, lowering after `AMEND` listed in §32.3 and closure map §5. **C** (N3 here adds the pre-emption cost).
  - N5 (editorial): §23.6 requalification kinds include review and gate decision; line 656 says "the re-work of an amended item"; `late(n)`'s `D_m` is "the state that decision's admission makes". **C**
  - N6 (`OVERTAKEN` records-only answer): the joint-invariant trigger excludes fenced and `OVERTAKEN` admissions. **C** (N6 here for `late(n)`).
- **3876473, 3940dbc, c77447b, 095ce55, 82d618c B1 and N items.** The value-level rules (refresh not a withdrawal, frame answers stale after a rebase not latched, machinery-computed lines, entry-order independence, no `tgt` after the latch, the prose-and-fixed-fields key, fence and late publication, latched `P`, dispute lines, never ready again) are unchanged in text and re-checked by the lifecycle family's mutations, each caught. **C**; 82d618c N4 **R** (closure map §5).
- **Revising duty and liveness (653e88c, edabd81):** `standing` entries at §4.1, §4.3, §8.3 step 7 and §10.2 are unchanged. **C**
- **Judgment disagreement (§5.10).** The table, the one reach rule and invariants (g) 1-8 are byte-unchanged; §5.10 remains the one owner, other sections point to it; the plan row is a stated conservative resolution policy; the equivalence `authors` input covers both sides and re-producers. **C/R** as in earlier records. The delta couples to §5.10 only through vetoes as lowering events.
- **Matching (§6.3-§6.6).** Unchanged. Phase B N2 in text: `link⁻` is an S0 test that reads no completeness, so a differing old-content run under (2) and a yielding present-content run under (4) stay in under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld; only (1) and (3) narrow through `on⁺`. Support cycles (§5.6) and corrupt prefixes (§5.7) fail closed. **C**
- **Content identity, gate qualification (`unq` in `gterm`), equal-region partition, run identity, acting rule.** Unchanged. **C** in their owners.

| Prior record | Disposition at this candidate |
|---|---|
| 494C810 (same family) | B1 (a) **C**, (b) **C**, (c) **P** (B1 here); N1 **P**; N2 **C** (N2 here); N3 **C**; N4 **C**; N5 **C**; N6 **C** |
| 3876473 (same family) | B1 (a)-(d) **C** at the value and waiting level, (a)'s decision exits **P** (B1 here); N1-N5 **C**, N4's diagnostic scope **P** |
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

- **Permissive direction:** a revoked relied-on disposition, and a new counting failure on a revision the predicate read, lower the item (model and Manual agree); after a `RESOLVED_BY`, a later counting failure on that revision lowers nothing (B1 (b2) applies to it too), though the failure itself still counts in current-state `qual` for the claim's subject, so the claim stays qualified.
- **Restrictive direction:** no settled failure is resurrected by a content change; a failure on later content reaches only the subject (item 31, disclosed).

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Lowered item repaired by a new item; `RESOLVED_BY` naming it | **B1 (a)**: refused by the closed schema, or admitted with no schema, target or basis |
| Human answers an escalated decision with `AMEND` | **B1 (a)**: retired; no amendment owed |
| `RESOLVED_BY` while a blocking challenge is open after a move; challenge then upheld | **B1 (b1)** |
| `RESOLVED_BY` for one event; later upheld challenge on the produced revision | **B1 (b2)**: no decider |
| Upheld challenge, or loss boundary, against the `RESOLVED_BY` | **B1 (b3)**: unstated; terminal by §10.4 as written |
| No standing plan; lowered joint-invariant review of an absorption | **B1 (c)** |
| Two joint-invariant reviews discharged, then an upheld challenge on the first (either order) | held: decision owed, nothing retires it |
| Peer `NO_PASS` on `X`, or gate `REJECT` on the triple, after a later edit | held: stands, decision at once |
| Peer veto while content current; owner dispatched; then content moves | held: waits, then stands |
| Later peer gate decision challenged after the latch | N2: lowers to `F` (fail-closed, undisclosed) |
| `SPEC_REVIEW` tolerance-widening finding upheld; principal's `RESOLVED_BY` | N5: admissibility depends on an undefined floor test |
| Latched item; upheld challenge on its review; re-integration claim | held: refused (step 7), routed to the principal |
| Re-partition including a lowered part | held: excluded (§13.7) |
| Continuation or requalification after the content moved | held: refused, the event stands |
| `IMMATERIALITY` relied on at `D_m`, its basis moved | held: the disposition's line decides |
| `QUALIFIED` gate at integration, permitted; later output edit | held (`P` for good; disclosed) |
| Fenced or `OVERTAKEN` integration, kept or re-applied; records-only `OVERTAKEN` | held |
| Counter-challenge upheld after routing, before any decision | held: restored |
| Entry order, second `AUTHOR` revision, absorbed foreign change of a latched item | held |
| Later item breaking an earlier item's required evidence | held: `REGRESSION` |
| Stratification of retirement, waiting and routing | held: no cycle through the latched obligation |
| Composition, chain and union reach; review re-identification; plan closed form over every tightening shape | held (unchanged; model green) |
| Completeness lapse under a narrow-basis failure (Phase B N2) | held |

## Minimum architecture and capability transfer

The delta adds no primitive, component, record kind, basis mode or persistent surface. It removes one automatic transition (successor retirement) and adds one decision outcome (`RESOLVED_BY`) and one terminal state (retired). Option 1 removes the terminal state for every outcome but `AMEND` and adds schema rows. Two capabilities an owner requires are not delivered as realized:

- the challengeability of a principal decision that ends a finding's effect (reviewed §7.9 persistence and digest rule; Manual §0.4 allocation);
- a decider for a finding against integrated work after an unrelated earlier event was decided (workflow owner's explicit closure).

Architecture 1.6.0 (`orchestrator/docs/architecture.md`, blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41` (`git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 c4e8de7ecd6770020cc36923b8e37321bb82cd74 -- orchestrator/docs/architecture.md source dist`: empty). The version-bound Core and frozen profiles are preserved (PEM PC-001).

**PEM.** Activated: mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` both resolve to `af0455753e20ee54a969c844872e29e270007211`. The PEM blob there and at the candidate is `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no overlay. The repository validator (`python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run in the clone, whose `source/` and PEM equal the candidate's; in the `git archive` snapshot it cannot realize routes without a Git repository) reports "PEM schema 1 valid: 5 families, 0 notices". Task-local HAS:

- **PC-001**: APPLICABLE (frozen profiles; preserved).
- **DS-001**: APPLICABLE. The green lifecycle family and §31.4's cases coexist with B1; the oracle shares terminal retirement with the rule (N1).
- **SP-001**: evidence-only (one owner per fact; B1's deciding record is stated in §10.4 and §15.5 and absent at its owner §3.4).
- **SP-002, FF-001**: evidence-only, not material.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 separates G1 document checks from G2-G4 runtime evidence and claims no execution it lacks. §31.4's R15 cases now discriminate the 494c810 siblings: successor in either order, post-move veto and gate rejection, repair by a new item, the `RESOLVED_BY` floor restriction, the same-triple qualified decision. They do not discriminate B1:

- the repair-by-new-item case expects a record the closed schema refuses;
- no case acts after a retirement, against a deciding record, or for a human outcome;
- no case covers a project with no standing plan.

The lifecycle family is a real improvement: it now yields retirement and decision routes, and every value-level and waiting case I probed agrees with the Manual. But it ends every history at the first decision, and its oracle encodes the candidate's terminality as a protected property (N1). A green run therefore cannot show B1.

## Doctrine-realization map and O1

§29 maps all seven entrypoints. B1 touches three rows:

- the D4 row's "close each stage with affected regression; reconcile every obligation" (B1 (b2): a finding after retirement is reconciled to nothing);
- the workflow row's explicit closure (B1 (b1), (b2));
- the D2 row's "tolerances from accepted error semantics, never from a failing backend" through N5 (whether the principal may close that finding).

These are the same defect seen from the map and need no separate repair. O1 (§0.5) is unchanged. The realized record, readers, routine questions, retention and marked surfaces are stated, all within the requested deliverable and none beyond it. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

Executed against the extracted candidate, or in the clone where stated:

- Blob identities above, by `git rev-parse` at the candidate. The model file's blob is `2797015f19639dbb16677d95aa0451d0b3ccc315`.
- `git diff --check 494c810017249d00967eda633334ba2987f7ff68 c4e8de7ecd6770020cc36923b8e37321bb82cd74`: exit 0. The delta is six files: the Manual (15 hunks), the closure map (3 lines), the continuation handoff, the model (+124/−73 lines), and the previous handoff and Review record, added.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the snapshot: 4 tests OK (routing and lifecycle structure only).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 bf2337285dfdaba5d535e73cf76af3d5b78978f0`: 73 files, 23,269 insertions, 1 deletion (that historical comparison only).
- `git diff --stat fad3ee41… c4e8de7… -- orchestrator/docs/architecture.md source dist`: empty.
- PEM validation as above.
- Diagnostic model at the candidate, with `--mutations` semantics, run in parallel.
  - The driver was a scratch script, `$TMPDIR/ssds80-manual-review-c4e8de7/scripts/par_run.py`, run with `python3 -I`. It imported the unmodified snapshot module in each worker of a `multiprocessing` pool and cleared and set `MUT` at the start of every job.
  - It ran `run_family` for each of the six families (`CORE`, the three in `FAMILIES`, `GATE_BASIS`, `LIFECYCLE`) with `MUT` empty. Then, for each of the 52 entries of `MUTATIONS`, it set `MUT = {m}` and ran `run_family` on each family that mutation names, exactly as `main()` does: 58 jobs.
  - Results: 58 jobs, all returned (wall time 14 min 39 s on 30 workers). Zero invariant failures in every base family, with these scenario counts:
    - transformation-review/acceptance/gate: 1,856,368;
    - equivalence-chain: 299,760;
    - completeness-cover: 37,600;
    - plan-coverage: 205,800;
    - gate-basis: 1,000;
    - obligation-lifecycle: 1,485,256.
  - All 52 mutations are caught in every family they name (54 mutation-family evaluations). Single-invariant catches: `plan_supersession_current_only` by I4 only; `frame_acts_everywhere` by I5 only; `obligation_direct_only` by I8 only; `eligibility_support_tier_only` and `challenged_record_authors` by I7 only; seven core and gate-basis mutations by I1/I3 only; every lifecycle mutation by I11, and `lifecycle_non_latched`, `lowered_becomes_ready` and `provisional_not_latched` also by I12. The lifecycle family and its 18 mutations were also run separately first (16 s).
  - `main()` itself was not called; the driver calls the same functions in the same configuration.
- A separate probe (`scripts/probe.py`) evaluated `lc_value` and `lc_oracle` on twelve hand-built cases, including post-retirement histories (B1 (b), N1).
- Governing owners read at `aaeaf8b`:
  - `source/roles/software-design/SKILL.md` (routing, design contract, independent review);
  - `architecture-and-design.md` (line 96);
  - `workflow-and-workplans.md` (line 96);
  - `evidence-evolution-and-dependencies.md` (line 153);
  - `convergence-and-cycle-economy.md` ("Active simplification trigger", line 62; "Review strategy after recurrence", line 89; family definition, line 25; review sufficiency, line 85);
  - PEM and testing owners, applied through the validator, the HAS and DS-001.
- Reviewed workplan at the Phase B candidate: §7.9 Persistence (line 1675), materiality reclassification (line 1732), the digest rule (line 1875), the decision-class table (line 1570), the allocation line (line 731), the closed schema (lines 1048, 1407), and §21 items 1-27 at the candidate.
- Manual sections read in full: §0.4; §3.2, §3.4, §3.6; §4.3 (coordination row); §5.3-§5.5 (`gterm`, `elig`); §8.3; §10 (all); §12.4-§12.5; §13.7; §15 (all); §16.7-§16.8; §22.2-§22.3; §23.6; §31.3 (model text); §31.4; §32.3; closure map lines 87 and 298. The rest by targeted search for retire, lowered, `RESOLVED_BY`, `REVOKED`, `HUMAN_ATTENTION` and `COORDINATION_DECISION`.

Not verified:

- No production SSDS, real gate or runtime was exercised.
- B1 (a) depends on reading §3.4's outcome and target columns as the closed schema's enumeration (§3.2 "per-kind enumeration", §3.6). An implementer who reads §15.5 as amending §3.4 still meets (b) and (c).
- B1 (b2) states that I found no current-state obligation routing a decision for a revoked D3/D4 produced revision once its item obligation is retired; I did not prove there is none, and the Manual names none.
- The handoff asked for the six drift classes across the whole Manual. I applied them to every statement of the deciding record and its consumers and by targeted search elsewhere; I did not compare pairwise every concept the Manual states twice, so further drift outside these is possible.
- Earlier records' per-item closures were not replayed.

## Scientific checks

Method: one pinned architecture candidate; deductive counterexamples bound to exact owner text; a family-level recheck; structural tests; and the candidate's diagnostic with its prescribed mutations, plus a twelve-case probe of its lifecycle oracle.

Material findings: B1 and N1-N6. None concerns a scientific observable, numerical method or realized scientific result. N5 concerns whether SSDS lets a coordination decision close an upheld finding that a tolerance was widened to fit a failing backend. That is a governance consequence for how scientific evidence specifications are reviewed, not a scientific judgment about any tolerance.

**I produced, ran or reviewed no realized scientific results.**

Variants evaluated: one normative candidate. For B1, three sibling classes: (a) schema, human outcome and human `AMEND`; (b) three post-retirement trajectories; (c) the no-standing-plan route; and eight controls that hold. Twenty-three out-of-matrix trajectory classes, overlapping rather than independent trials. One diagnostic configuration (6 base families, 52 mutations) and twelve probe cases. The criterion was to find a material counterexample, not to select a favourable result.

No accepted project D1/D2 scientific authority was relied on for a consequential judgment, so no tension search was triggered. Gaps: real-owner execution, reader adequacy and operating costs.

## Common-mode note

The reviewer is of the **Claude family**, the same family as the Manual's author and as most earlier Manual reviewers. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. This reviewer was engaged as a fresh-context sub-agent launched by the authoring session. It did not receive the authoring conversation, but fresh context is not epistemic independence. Shared dependencies:

- the corpus;
- the inherited workplan and handoff framing (including the handoff's prompt to attack the exits and the couplings with §12.5 and §15.4-§15.5, which directed the search);
- the prior Review records, read as hypotheses (494c810 option 1 is the source of the decision exit attacked here; terminal retirement and the omission at the schema owner are the realization's);
- the Git/Python toolchain;
- the diagnostic's event list, which the rule and its oracle share.

For the sixth consecutive round, this family's blocker entered through the previous same-family Review's recommended option or its realization. Same-family review of same-family repair directions remains a weak check here. A different-family check of B1, and the stakeholder decision on whether R15 should exist (option 2), are advisable before another candidate.

## D4 statement

This Review authorizes **no D4**, cutover, architecture acceptance, product-scope extension or proposed default. The next steps are:

1. Put B1's options to the stakeholder now, with option 2 (withdraw R15) as the family-removing alternative, as the continuation handoff says to do on a further failure in this family.
2. Under the chosen option, define the retired state's exits and its deciding records at their owners: §3.4 and §4.3 (outcome, target, basis), §15.2/§5.4 persistence, the `HUMAN_DECISION` mapping and the `HUMAN_ATTENTION` trigger; reconcile §10.3, §16.7, §31.4, §32.3 and closure map line 298.
3. Add B1's discriminator to §31.4.
4. Extend the lifecycle model with post-decision events and the decision's standing, and restate its oracle property from the owners rather than from the rule (N1).
5. Consider N2-N6.
6. Freeze a replacement candidate and obtain an independent Review, preferably a different-family one, before stakeholder G1 acceptance.

G2 still separately requires a reviewed shadow workplan and explicit stakeholder authorization.
