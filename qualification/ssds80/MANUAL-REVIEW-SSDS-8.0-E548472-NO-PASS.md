# Independent D3 Review — SSDS 8 Architecture Manual, candidate e548472 (NO-PASS)

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system (full clone)
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          e54847244f6a8c24acc0220e204fb4accd398807
    SCOPE:              the whole proposed Manual as durable D3 owner, handoff §1 (a)-(g)
    MANUAL blob:        74e3f705f02a348c9091361305624bdc0e55ac97 (orchestrator/docs/ssds-8.0-architecture.md), verified
    CLOSURE MAP blob:   9f15adf5c76e6116dc07fd1795d42dc7f2e70128 (review aid, not authority), verified
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; Phase B semantic candidate e23f14208be869e6a78cfd7b312e447254ee1851
                        (blob 610f373b97fb8152d2a5742e17fa172e12204756); blob at the candidate
                        91bde236465178f20c7348280e036d2884dfc216, verified
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954; recovery
                        efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      every record in qualification/ssds80/ up to the d6734c4 different-family NO-PASS,
                        read as hypotheses only. The different-family e548472 PASS record was not read
                        before this verdict was formed (see §15).
    REVIEW METHOD:      handoff steps 1-11 and 6a; candidate read by `git archive` snapshot under
                        $TMPDIR/ssds80-manual-review-e548472/snap; falsification focused on the newest
                        clauses (§5.10 (g)5-(g)6, §16.5 brief carry) and on the plan-coverage row SD-30 fixed,
                        attacked in both directions; probes on the candidate's own diagnostic model
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched by
                        the authoring session

## SERIOUS CHALLENGE

**SC-1 (to the stakeholder; SD-30's "keep the revert exemption").** SD-30 (stakeholder record item 25: "Option 1: delete the r* ⋢ r exemption, give PLAN_ACCEPTANCE per-target relief by the rejecter or the owner (route 3), keep the revert exemption, and carry standing rejections into the next acceptor's brief") retains a clause that, as written and as realized, lets the author of a plan dissolve a standing independent rejection by editing a control field, with no judgment by the rejecter, the owner or any reviewer who saw the rejection, no derived `PLAN_ACCEPT`, no brief carry and no derived `ADJUDICATE_DISAGREEMENT`. The trajectory is B1 below. The clause conflicts with three accepted owners or decisions that apply simultaneously:

- the evidence owner at the governing commit (`source/shared/references/evidence-evolution-and-dependencies.md`): "Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position. … An unresolved material disagreement keeps dependent present guidance/closure visibly qualified." (R9 and R14 apply this rule to every judgment kind; R14 quotes the last sentence as its governing text);
- the reviewed workplan §7.9 (line 1726), which says what a plan acceptance claims: "It claims only that the acceptance's conclusion about *what is asked* still applies under tighter controls." Under SD-29's one reach rule ("an adverse judgment vetoes every passing judgment of its kind that … claims what the adverse judgment denies"), an acceptance of `r` claims every tightening of `r`, the rejected `r*` included when `r ⊑ r*`, whatever the current revision is; the revert exemption is reachable only by restating that claim more narrowly (§5.10 (b): "claims `r` and, through coverage, the item's current revision `cur`");
- SD-30's own premise, realized in the row as "whoever recorded the acceptance and whenever": the revert exemption makes the veto depend instead on a fact the plan's principal controls (`cur`).

Because SD-30 is stakeholder-chosen direction, the Review cannot repair it; it routes it. The options are in B1. New information since SD-30 was chosen: SD-30's own route-3 relief now makes the restrictive cost that motivated the exemption liftable by one record of the rejecter or the owner, and SD-30's brief carry never fires on this path because no plan acceptance is asked.

No other Serious Challenge. I found no evidence that the reviewed workplan, SD-1 to SD-29 or the governing 7.2.1 owners are themselves contradictory or unrealizable beyond SC-1.

## Verdict

**NO-PASS.** One blocker (B1, judgment-disagreement layer, plan-coverage row), tied to SC-1 and needing a stakeholder decision. The candidate's own repairs since d6734c4 (the §16.5 brief selector and the restatement of (g)5-(g)6) hold for what they claim; non-blocking findings N1-N5 follow.

## Blockers

### B1 — A plan rejection is dissolved by its plan author's control edit (revert exemption; family: plan-coverage reach, sibling of 83a82df B1)

**Text.** §5.10 (b), `PLAN_ACCEPTANCE` row: "a rejection of item revision `r*`, under any objective revision, denies `r*` and every tighter revision (§13.4) … one acceptance naming `r` claims `r` and, through coverage, the item's current revision `cur`. So a rejection of `r*` reaches an acceptance naming `r` when `r* = r`, or when `r ⊑ cur` and `r* ⊑ cur`, whoever recorded the acceptance and whenever (SD-30). … A revert below `r*` (`r* ⋢ cur`) leaves it reaching only acceptances naming `r*`". §11.4: "An amendment's class is computed by lint from the diff between the accepted item revision and the current one (§13.4): control tightening keeps the existing plan acceptance current (R1)". §13.4: `⊑` "is always checked against the **accepted** revision". §4.4: `sat(content (u, r, PLAN_CONTROL)) = T if … r ⊑ cur(u)`. §10.2: `PLAN_ACCEPT(items)` is derived only for "an item revision not covered by a current plan acceptance"; `ADJUDICATE_DISAGREEMENT(x)` only for "a standing adverse judgment `x` that vetoes a passing judgment of its kind acting in the state". §16.5: the rejection is carried only into "a plan-acceptance brief (`PLAN_ACCEPT`)". §31.6 (V) states the intended outcome: "after the principal reverts to `i1`, the acceptance of `i1` makes the item issuable again with the rejection still standing".

**Trajectory (conforming at every step).**

1. Item A at `i0` (objective `o`); an independent agent `P` records `PLAN_ACCEPTANCE ACCEPTED (o, A@i0)`. A is issuable.
2. The principal tightens A's `budget` from 10 to 5 (R1): `i1`, `i0 ⊑ i1`. `P`'s acceptance covers `i1`; no plan acceptance is asked.
3. An authenticated independent human `H` (a domain owner reading the plan) records `PLAN_ACCEPTANCE REJECTED (o, A@i1)`, finding that A's objective prose, byte-identical in `i0` and `i1`, contradicts the governing D2 contract. A human may record a judgment on a target unbidden (§10.3, "or recorded on its target by an authenticated human"). Reach: `r = i0 ⊑ cur = i1` and `r* = i1 ⊑ cur`, so `P`'s acceptance is vetoed, A is not issuable, `ADJUDICATE_DISAGREEMENT` is derived. Correct so far.
4. The principal (an agent; A5 only it changes the plan) changes A's `budget` to 6: `i1'`. Against the accepted revision `i0` this is a tightening (6 ≤ 10, prose byte-identical), so it is R1 and derives no `PLAN_ACCEPT` and no brief. `i1 ⋢ i1'` (6 > 5). Reach: `r* = r` is false; `r* ⊑ cur` is false. `P`'s acceptance is no longer reached, covers `i1'` and makes A issuable; `ADJUDICATE_DISAGREEMENT` is no longer derived. An exact revert to `i0` (step 4′) gives the same result.
5. A is issued and implemented under prose that a standing, unrelieved independent rejection denies; no one who saw the rejection has accepted anything since; the owner is not asked; the human's finding is shown only in inspector history.

Probe on the candidate's own model (scratch `probe_revert.py`, importing the candidate's module, not modifying it): with `ACCEPTED(i0)` by `P` and `REJECTED(i1)` by `H`, `cur = i1` gives `base(p0) = F`, `issuable = F`, adjudication derived (model and oracle agree); `cur = i0` gives `base(p0) = T`, `issuable = T`, no adjudication (model and oracle agree). The model's plan scenarios never set `cur` to `i0` and contain no revision above `i0` but not above `i1`, and its oracle reads the same inheritance claim, so the case is green by construction (§5.10 (g) discloses that the claims column is shared).

**Why it is a defect, not only a disclosed trade-off.**

- The rejected and the released revisions differ only in whitelisted control values: §13.4 requires the item prose to be byte-identical and `kind`, `objective`, `governing`, `acceptance_criteria`, the obligation set, `gates` and `depends_on` to be unchanged. A rejection of a tightening is therefore about content the looser revision shares (what is asked), about the tightened controls being too loose (which the looser revision makes worse), or about them being too tight. Only in the third case is release correct, and in that case the rejection never contradicted `P`'s claim, because the reviewed §7.9 claim "does not claim the work is still feasible". Machinery cannot tell the three apart; the row resolves the unknown permissively. The Manual's own allocation principle (§0.4) says "decidable only conservatively -> machinery, sound over-approximation, never under-approximation", and C5 says "unknown required semantics fail closed".
- The row is the only one in §5.10 (b) whose reach reads the current content state. The transformation-review row reaches "the same plan item at any of its revisions with the same changed-unit content", and §31.6 (P) requires that "after a revert to `i1`, an agent's `PASS` on `X1` is still vetoed"; §31.6 (R) requires the same of `COMPLETENESS` ("after a revert to `v1` an agent's `COMPLETE` at `v1` stays vetoed"). SD-30's repair aligned the plan row with the transformation-review row (83a82df B1 option 1) except here.
- It is 83a82df B1's pattern again: there, "any fresh peer's acceptance override[s] a standing rejection"; here an earlier peer acceptance overrides it, once the plan's author moves `cur`. The SD-30 sentence "judging that an amendment cured a rejection is the rejecter's or the owner's, never a peer's" is defeated by the author, who is not even a reviewer.
- The safeguards named for the escape do not apply. §32.2 names the brief carry as the safeguard for R2 amendments; a revert or loosening is R1 against the older acceptance, so no brief is built. Closure map §5 and R14 describe the clause as "a revert below the rejected revision releases the old acceptance". By the row's own definition (`r* ⋢ cur`) it is broader: any amendment taking the current revision out of the rejected revision's up-set, including a one-field loosening within an older acceptance's bounds. No disclosure says that no judgment, brief or owner routing follows.
- The restrictive reason for the exemption (R14: a rule reaching every tighter revision "kept a correct rejection vetoing an acceptance after the rejected tightening was reverted") predates SD-30's route 3. Under route 3 that veto is lifted by one record: the rejecter's (a human's) or the owner's acceptance of the reached exact target, e.g. `(o, A@i0)`. My probe with the module's existing `plan_reach_any_tighter` reach: `H`'s `ACCEPTED(i0)` makes `base(p0) = T` with no adjudication left. Invariant (g)4 (liftable where it bites) therefore holds without the exemption.

**Violated owner text.** Evidence owner, quoted in SC-1 ("latest-editor order"; "keeps dependent present guidance/closure visibly qualified"); workflow owner (`workflow-and-workplans.md`): "A synthesizer reconciles findings through evidence and owner adjudication; it cannot erase unresolved contradictory material evidence by vote"; reviewed workplan §7.9's statement of what an acceptance claims; Manual §0.4 allocation principle and C5.

**Earliest owner.** The stakeholder (SD-30's retained clause), then the Manual §5.10 (b) plan row, with §13.4's sentence, R14, §31.6 (V), §32.2 and closure map §5 following it.

**Options for the stakeholder (Phase C handoff §5).**

- **(1) Recommended, subtractive.** Remove `cur` from the plan reach. A rejection reaches every acceptance naming a revision of the same item with the same non-control content as the rejected revision (byte-identical item prose and every field §13.4 marks "unchanged"), under any objective revision, whoever recorded it and whenever. Relief stays route 3, and an R2 prose amendment stays a new target carried in the next acceptor's brief. This mirrors the transformation-review row, keeps every case SD-30 intended (fresh peer acceptance, incomparable branch, further tightening, multi-item, objective-only), reaches revert and loosening, and needs no `⊑` test in the reach. Cost: a too-tight rejection keeps vetoing the older acceptance after a revert until the rejecter or the owner relieves it (one record).
- **(2) Minimal conjunct.** Keep SD-30's formula and add the disjunct `r ⊑ r*` (the acceptance claims `r*`, by §7.9). This closes revert and loosening; an acceptance of a branch incomparable with `r*` whose coverage does not reach `r*`'s up-set stays unreached.
- **(3) Keep the exemption knowingly.** State in §32.2 and closure map §5 that any amendment leaving `r*`'s up-set, including the plan author's one-field loosening within an older acceptance's bounds, makes that acceptance count again with no judgment, no `PLAN_ACCEPT`, no brief and no owner routing, although the prose is identical; record that this departs from the evidence owner's rule; and add the §31.6 case. This adds no mechanism but accepts the violation.
- A typed reason distinguishing an over-tight rejection, with release only for it, would **add mechanism** (a reason vocabulary read by the reach) and is not recommended.

**Required discriminator.** §31.6 (V) gains B1's trajectory, run twice: once with step 4 (the one-field loosening) and once with step 4′ (the exact revert). Under (1) or (2): A is not issuable, `ADJUDICATE_DISAGREEMENT` is derived, and `H`'s or the owner's `ACCEPTED (o, A@i0)` restores issuance. An implementation whose plan reach reads `cur` must fail. The diagnostic's plan scenarios need `cur = i0` and a revision `⊒ i0`, `⋣ i1`, and its plan oracle must state the chosen claim independently. Today `plan_reach_any_tighter` is listed as a re-introduced defect, so the model would report option (2)'s half as a failure.

## Non-blocking findings

**N1 — The brief carry ends on any later record's `RESOLVED`, including a non-independent, non-acting or peer record (§16.5; family: carried-finding termination).** "It stays carried until a later plan acceptance of the item records it `RESOLVED` in its `findings` slot or the owner's adjudication disposes of it." Nothing says that later acceptance must act in the state, be independent (`nonind` false) or stand. Trajectory: after an R2 amendment, an `UNKNOWN`-lineage agent records `ACCEPTED` marking `H`'s rejection `RESOLVED`. That acceptance supports nothing, so `PLAN_ACCEPT` stays dispatchable, but the next independent acceptor's brief no longer shows the rejection, and §32.2 names that carry as the only safeguard for R2 amendments. The re-review rule for transformation findings in the same paragraph has the same shape, inherited from earlier candidates. Repair (narrows): a carried item ends only on a `RESOLVED` from a record that acts in the state, is not `nonind` and is not superseded. A further question for the stakeholder: whether a peer's `RESOLVED` may end the carry at all, given SD-30's "never a peer's".

**N2 — (g)6 is stated over "the same records", but whether a record is admitted depends on order.** Admission step 6 admits a plan supersession only "while its basis holds", and every record only while its basis is current (K1). So the rejecter's supersession admitted before a loosening is refused after it, and re-tightening then gives different derived values. The claim holds for a fixed admitted set evaluated position-independently, which is also what the model checks (`set(Lp.adm) == set(L.adm)` under permutations of judgments only). Reword it to say so (editorial; non-blocking because the rule itself is clear).

**N3 — Two statements of what a plan acceptance claims.** §13.4 (following workplan §7.9) says "the acceptance's conclusion about what is asked still applies under tighter controls"; §5.10 (b) says it "claims `r` and, through coverage, … `cur`". §5.10 governs by its own precedence clause, so an implementer is not left choosing; but the row's claim is not the reviewed claim, and R14's "Restrictive only against the reviewed text" is true of the reach, not of this restatement. This is part of B1's cause; under option (1) or (2) both texts can state the reviewed claim.

**N4 — Diagnostic model: the plan family's scenario space omits the release cases, and one mutation encodes a stakeholder choice as a defect.** `plan_scenarios` uses `cur ∈ {i1, i2, i3, iQ, i1x}`. `plan_reach_any_tighter` ("bf23372 N1 / 0d2b35e option C: the preservation reading") is counted as a re-introduced defect only because the oracle shares the row's claim. A green run therefore says nothing about B1 (testing owner's proxy-proof rule; PEM DS-001). §5.10 (g) discloses the shared claims column honestly; the scenario-space gap is not disclosed.

**N5 — Retained trade-offs (stakeholder options, not blockers):**

- bounded-only reproduction, which partly narrows SD-17;
- SD-24's provisional cap, and the gate minimum that only its author or the owner controls;
- fresh D1/D2 re-gating after fences, overtaken re-application and replacement iterations (R4, R12);
- withheld cross-pending-frame support;
- adverse frame judgments surviving abandonment;
- gate minima accumulating members;
- the fenced-cutover half state;
- context-revert reuse after supersession;
- party exclusion from adjudication, still configurable by policy;
- broad two-sided, re-producer and unknown-authorship `authors` sets, which cost migration throughput;
- an `INCOMPLETE` on a large scope widening every closure inside it;
- fixed `sat` hop direction;
- part and composite equivalences not reaching each other;
- R2 amendments as new plan targets, carried in the brief only;
- the paraphrase-only 2026-10-12 adoption instruction.

All are disclosed in §32.2, §32.3 or closure map §5.

## Closure audit

None found beyond B1. Basis: the candidate differs from d6734c4 in three hunks only: (g)5-(g)6, the §16.5 plan brief selector and its §31.6 (V) discriminator, and the corresponding closure-map row and §7.2 line (`git diff d6734c4 e548472`). I re-checked closure map §1 item 8 (plan acceptance, amendment policy, plan invariants) against §11.2-§11.4, §13.4, §5.10 (b) and §16.5. It is substantively decided except for B1's clause. I spot-checked items 7, 9 and 21-22 and the §16.2 tables' dispositions against §10.4-§10.5, §9.2-§9.3, §29.7 and §30. In this round I did not re-locate every §21 subordinate clause independently; that is a gap (§13), mitigated only by the fact that no other normative text changed.

## Refinements R1-R14

- **R1-R8, R10-R12:** text unchanged since d6734c4. I re-read R1 against §6.5 (the construction rule, `on⁺ ⇒ on⁻` by construction, `ext` over the whole class) and R12 against §5.2 and §7.3-§7.6 (the acting rule, the enactment unit, frame `record` entries). I found no unsoundness. R4 and R12 carry disclosed liveness costs.
- **R9:** sound as the exact-target base rule. Its plan consequence is R14's.
- **R13:** sound; the authorship-keyed requirement and `nonind` read only S0 facts.
- **R14:** sound for the `EQUIVALENCE` and `COMPLETENESS` rows, for `asserts` (the same conjuncts as `base` less vetoes) and for stratification: the plan reach reads `⊑` and `cur`, both S0. **The plan row needs different treatment (B1, SC-1).** Its acceptance claim narrows the reviewed §7.9 claim, and its revert exemption is permissive in a case its cost cell and §32.2 do not disclose.

## Re-verification of earlier findings (family level)

| Reviews | Findings | State | Basis |
|---|---|---|---|
| d6734c4 (different family) | B1 (brief selector), N1 ((g)5-(g)6), N2-N3 | B1 **closed** for what it asked; N1 **partly closed** (N2 here); N2-N3 retained or disclosed | §16.5 now carries every standing rejection naming an asked item, at any revision and under any objective revision, a multi-item rejection carried whole; (g)5 now states the adverse-judgment exception. The carry's termination is N1 here; the revert path, which never builds a brief, is B1. |
| 83a82df | B1 (a), (a′), (b), (c); N1-N5 | B1(a), (a′), (c) **closed** (fresh peer acceptances reached; route 3); B1(b) **closed as disclosure** (R2 brief carry); the family **recurs** through the revert exemption (B1 here); N3 closed (§32.2 hop line); N5 retained | §5.10 (b), §5.10 (d) route 3, §16.5, §32.2 |
| 0d2b35e | B1 (a)-(c); N1-N5 | B1 **closed** for incomparable branches (the `r ⊑ cur ∧ r* ⊑ cur` disjunct); its option (C) analysis of the revert exemption is the substance of B1 here, now with route 3 available; N1 closed (supersession while the basis holds); N2 disclosed; N4 residue closed | model `plan_reach_path_only` caught; text |
| 34803df, bf23372, a6ed164 | B1-B2 and siblings; N items | **closed** at family level for equivalence chains (either-direction reach, class cover), completeness unions, analyzer identity outside the reach, the provisional-hop `asserts`, the authorship-keyed requirement and two-sided `authors`; the plan-row pieces as above | §5.10 (a)-(b), §4.4; model mutations caught (§13) |
| 6b986de, 29da56e, 51070e5, 9e5a763, 051cce3, 63ddf91, f03b15e, 61cd09b | independence at Admission and in `base`; one `authors`; class rule; exact supersession targets; per-target relief; member revisions in `COMPLETENESS` targets; cutover carriers | **closed** as far as re-derived: (e) Admission refuses non-independent or under-class adjudications measured at the chain root; `nonind ⇒ base = F`; relief requires `¬nonind`, `acts`, `CLEAR` | §5.10 (a), (d), (e); model I2/I7 mutations caught |
| 362af9f, f22b4dc, both b46c250, f7419d5, 575dc78 | acting rule; enactment unit; `rid`; gate veto across runs; `gterm` | **closed** as far as re-checked; not every case re-derived this round | §5.2, §5.5, §7.6, §10.2; text unchanged since d6734c4 |
| 5c55d4b, 27ef339, 0b6c4fa, a18b544, e9e6e9f, e2154ac, 3540d98 | `link⁻`, bounded reproduction, `UNBOUNDED` bases, content identity, gate qualification, equal-region partition | **closed** as far as spot-checked (§6.5 construction rule, §1.4-§1.5 one representation); not individually re-derived this round | text unchanged since candidates whose Reviews recorded closure; spot reading |
| 798b2b4, 71cf9b3, 86ab683, 1ffbbf0, 53669a5, d837363, cc005db, c6da678, b595f2c, 6ff4ed1 | the matching clause and the D1-D3 change rule | **closed** as far as spot-checked: `on⁻` reads only the record and `K`'s bytes; revision-assessment records are a target condition in the run (§10.2, §8.3 step 7); not individually re-derived this round | as above |
| Phase B | closures; N1-N4 carry-forward | N2 (completeness polarity) **holds**: `on⁻` reads frozen terms, so a completeness judgment becoming `P`, blocked, revoked or loss-withheld removes only permissive uses (`bound` false), never an adverse match; support cycles forced `F` (R2); corrupt prefixes halt (R3) | §6.5-§6.6, §5.6-§5.7 |

## Out-of-matrix trajectories attempted

**Broke (B1):**

- plan rejection of a tightening, then an exact revert;
- plan rejection of a tightening, then a one-field loosening within the older acceptance's bounds.

**Weakened a disclosure (N1):** an R2 amendment followed by a non-independent `RESOLVED` that ends the brief carry.

**Held:**

- a fresh peer acceptance of a further tightening (reached);
- an incomparable branch joined by a tightening (reached);
- a multi-item rejection against a single-item acceptance (per-item denial);
- an objective-only amendment, item revision unchanged (reached: `r* = r`, under any objective revision);
- rejecter self-relief, i.e. the rejecter's own acceptance of a reached target (relieves itself and the peer's exact target);
- an agent rejecter, relieved only by the owner (liftable);
- a frame-declared reliever in a pending candidate (does not act in `D`);
- challenge-tier relaxers in candidate frames (they declare the admitted frame by §7.5, so route 4 needs no `acts`);
- the plan supersession admitted only while its basis holds, against relief (liftable where it bites);
- `asserts`/`base` alignment for provisional judgments;
- stratification of the plan reach (S0 `⊑`, `cur`).

## Minimum architecture and capability transfer

No added primitive, component or persistent surface in this candidate. Option (1) of B1 removes a state-dependent term from one reach rule. Nothing the candidate removes drops an owner-required capability. §26.4's 1.6.0 supersession, the version-bound Core and the frozen profiles (PC-001) are textually unchanged. `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## Qualification design

§31.6 (V) now discriminates the d6734c4 selector case. It asserts the revert release as an expected outcome, so it would certify B1's defect. Green fixtures can coexist with B1 (N4). Nothing is claimed as executed beyond the G1 document checks and the diagnostic model, and the Manual marks the model as non-adequacy evidence (DS-001).

## Doctrine-realization map and O1

§29's E0-E3 levels and the 7.2.1 entrypoint rows read consistently with the entrypoints at the governing commit, as far as I checked: the entry contract, the D3 role contract and the scientific-checks rows. §0.5 states the O1 content, i.e. the material realized record, readers, routine questions, the marked product surfaces (none beyond the deliverable) and the realized-record architecture. Not re-derived row by row this round.

## What I verified and how; what I could not verify

**Verified:**

- the blobs (Manual, closure map, workplan);
- `git diff --check d6734c4 e548472`: clean (exit 0);
- `git diff fad3ee4 e548472 -- orchestrator/docs/architecture.md source dist`: empty;
- `git diff --stat fad3ee4 bf23372`: 73 files, all under `orchestrator/docs/ssds-8.0-architecture.md`, `qualification/ssds80/` and the workplan authority index;
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the snapshot: 4 tests, OK.

**Diagnostic model.** `qualification/ssds80/judgment_disagreement_model_check.py` was run with `--mutations` semantics, in parallel, by importing the module from the snapshot (`python3 -I`, a 28-process pool, scratch `par.py`). There were 31 jobs of `run_family`: each of the four families unmutated, and each of the 25 `MUTATIONS` entries on exactly the families it names (two entries name two families), each job in its own process with `MUT` holding only that mutation. This is the set of runs `main()` performs.

**Unmutated:**

| Family | Cases | Invariant failures |
|---|---|---|
| transformation-review/acceptance/gate | 789,396 | none |
| equivalence-chain | 299,760 | none |
| completeness-cover | 37,600 | none |
| plan-coverage | 75,945 | none |

**Mutations.** Every one of the 25 was caught.

| Caught by | Mutations |
|---|---|
| I1/I3 and I2 | `relief_ignores_nonind` |
| I1/I3 | `wide_review_supersession`, `gate_run_veto`, `base_ignores_nonind` |
| I7 | `eligibility_support_tier_only`, `challenged_record_authors` |
| I5 | `frame_acts_everywhere` |
| I1/I3 and I7 | `no_class_check` |
| I1/I3 and I8 | `endpoint_only_equivalence_reach`, `directed_chain_only`, `chain_ignores_class`, `plan_reach_names_only`, `plan_reach_any_tighter`, `asserts_requires_clear`, `completeness_exact_only`, `completeness_reach_analyzer_id`, `requirement_request_colocated`, `plan_reach_current_only`, `plan_rejection_denies_set`, `plan_reach_path_only`, `plan_fresh_acceptance_exempt`, `plan_no_relief` |
| I8 | `obligation_direct_only` |
| I4 | `plan_supersession_current_only` |
| I1/I3, I7 and I8 | `eq_authors_to_side_only` |

Wall time per job ranged from 42 s to 503 s; exit status 0. A green run is a diagnostic of the written rules within the modelled envelope; it does not bear on B1 (N4). I also ran the B1 probe (`probe_revert.py`), reported above.

**Not verified:**

- an independent re-location of every §21 subordinate clause and §16.2 row;
- an individual re-derivation of every pre-a6ed164 finding (the families were re-checked at the level stated in §8);
- runtime behaviour (no implementation exists);
- G2-G4 evidence.

## Scientific checks

- **Material findings:** B1 (with SC-1) and N1-N5, all about D3 judgment-disagreement and plan-coverage rules; none about D1/D2 content.
- **Realized results:** I produced, ran or reviewed none. The model runs and probes are software diagnostics of the Manual's written rules, with the envelope stated in §13.
- **Variants:** I evaluated more than one variant of one thing. Three plan-reach rules (the candidate's, option (1) and option (2)) were compared against one criterion: agreement with the reviewed §7.9 claim and with liftability under route 3, across SD-30's intended cases and B1's two trajectories. Option (2)'s reach half was run on the model through its existing `plan_reach_any_tighter`.
- **D1/D2 authority:** I relied on none for a consequential judgment, so no tension search was needed.
- **Gaps:** as listed in §13.

## Common-mode note

**Family and engagement.** I am of the Claude family, the Manual author's, launched in fresh context by the authoring session. The 3540d98, different-family b46c250, 9e5a763, a6ed164 and d6734c4 Reviews and the Phase B Review were of the GPT family; the others were of the Claude family.

**Shared dependencies.** I share with the author and the earlier Reviews:

- the corpus;
- the inherited workplan framing;
- the prior Review records (read as hypotheses; I read the 0d2b35e, 83a82df and d6734c4 records' plan-row passages before forming this verdict);
- the toolchain;
- the candidate's own diagnostic model, whose oracle shares the claims column.

**The different-family e548472 PASS.** I did not read `MANUAL-REVIEW-SSDS-8.0-E548472-DIFFERENT-FAMILY-PASS.md` before forming this verdict; I read its plan-row and brief passages afterwards. It judged that "The revert exemption releases controls no longer present" and found no governing requirement violated. It did not consider:

- a rejection whose grounds lie in the prose and fixed fields, which the released revision shares byte for byte;
- the plan author's one-field loosening, as opposed to an exact revert;
- the absence of any brief or owner routing on that path.

It also noted that a `RESOLVED` entry does not end a veto, which N1 here agrees with, but not that such an entry ends the brief carry. My verdict is unchanged and is my own; the two records disagree on B1, and the stakeholder should read both. **PEM:** I read DS-001 and PC-001 in the candidate's `PROJECT-ENGINEERING-MEMORY.md` as hypothesis sources. I did not independently validate its schema or publication state this round.

## D4 statement

This Review authorizes no D4 and accepts no architecture, product scope or default value. A PASS would have been technical evidence for G1 only. SSDS 8 D4 remains NOT AUTHORIZED.
