# SSDS 8 Architecture Manual — Independent D3 Review, candidate 575dc78

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 575dc78dccbce098710a2d11caa59b03677010c5
    SCOPE: whole proposed Manual as the durable D3 owner: (a) §21/§16.2 closure, (b) fidelity and
           refinements R1-R11, (c) out-of-matrix adequacy, (d) inheritance and capability transfer,
           (e) qualification design, (f) doctrine-realization map, (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: df1a4678b1e38999b93ee29716b099c4d36dd4f8 (checked)
    CLOSURE MAP BLOB: fe6478a271c5e1680a6e7d747e2d9fe6905e4a83 (review aid only; checked)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; Phase B candidate e23f14208be869e6a78cfd7b312e447254ee1851
           (blob 610f373b97fb8152d2a5742e17fa172e12204756, checked); blob at this candidate
           91bde236465178f20c7348280e036d2884dfc216 (checked)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
           (both confirmed in PROTOCOL-RELEASE-STATE.yaml at the candidate, accepted_current 7.2.1)
    PRIOR REVIEWS, HYPOTHESIS ONLY: E23F142 Phase B PASS; Manual NO-PASS records 6FF4ED1, B595F2C,
           C6DA678, CC005DB, D837363, 53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98, E2154AC,
           E9E6E9F, A18B544, 0B6C4FA, 27EF339, 5C55D4B
    REVIEW METHOD: D3 role entered at the governing public source; whole-Manual read at the exact
           candidate (git archive snapshot); deductive counterexamples in both polarities; family-level
           search after recurrence (convergence owner; handoff method step 6a), attacking hardest the
           clauses changed since 5c55d4b and the repairs of that round's non-blocking findings;
           prior-finding regression; required structural checks; no implementation or runtime qualification
    REVIEWER: Claude model family (the same family as the Manual's author); a fresh-context
           sub-agent launched by the authoring session from the named handoff; no authoring
           conversation received
    MUTATION BOUNDARY: this record only; no commit or push

Governing SSDP version for this task: 7.2.1.

All Manual section references are to the exact candidate. The checkout HEAD was the later handoff commit `588bf75`, which differs from the candidate only by the handoff file. Governing owners were read at `aaeaf8b…`:

- `source/roles/software-design/SKILL.md` and its expanded `dist/skills/software-design/SKILL.md` (entry contract and scientific checks);
- `architecture-and-design.md`;
- `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review readiness and independent review sufficiency", "Review strategy after recurrence");
- the cited paragraphs of `evidence-evolution-and-dependencies.md`, `workflow-and-workplans.md` (human gates and Channel C) and `abstraction-and-concretization.md` (Challenge).

The other concern owners were not loaded: no decision below turned on them.

## SERIOUS CHALLENGE

**None against accepted SSDP 7.2.1 or the frozen Architecture 1.6.0 / Level 0 Core.** The blocker is a defect of the proposed D3 concretization. The workplan and the Manual are proposed architecture, so a contradiction inside the Manual, or between it and a stakeholder direction, is not a challenge to accepted authority.

Owner text applied:

- D3 owner, "D3 boundary and feasibility": "A D3 candidate is admissible only when it satisfies every applicable D1/D2 invariant and directly governed security, reliability, compatibility, resource, performance/scaling, deployment and external-interface constraint."
- D3 role entrypoint: "D3 contradictory/ambiguous/inadequate/unrealizable -> SERIOUS CHALLENGE to D3". Applied to proposed D3, it yields a blocker, not a challenge to accepted authority.
- Workflow owner, human gates: "Orchestration may represent pending/accepted/rejected state but cannot self-approve it." Channel C: "The gate does not close unqualified when missing realized records could plausibly change its judgment."
- Evidence owner: "Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position."
- Convergence owner, "Review strategy after recurrence": "A clean local repair that genuinely closes the cause remains sufficient; recurrence does not automatically force redesign."

## Verdict

**NO-PASS.** One D3 blocker survives, stated at family level as method step 6a requires.

- **B1 — gate-qualification family ("one standing decision"), seventh round; entered through the repair of 5c55d4b N3, on the frame-gate mechanism added for 27ef339 B3.**
  - §7.5 now reads "answered" and "standing" per frame, so each candidate frame admits its own first passing decision for a gate obligation, and a frame decision becomes standing when its candidate integrates.
  - Integration admits no judgment, so the §8.3 step 7 uniqueness check never runs at that moment. After two candidates that change a gated subject to the same revision both integrate, the admitted state holds two unsuperseded passing decisions on one gate obligation.
  - §5.5's "the gate obligation's one passing decision not superseded" then does not denote. Under the formula as written (`⋁` over standing decisions), an earlier `UNQUALIFIED` decision by one holder closes a later `QUALIFIED` decision by another holder as `T`. That is contrary to the workflow owner's Channel C rule, to stakeholder entry 18 ("until a later unqualified gate decision") and to the Manual's own R11, §5.5 and §31.6.

The 5c55d4b-round repairs otherwise close what they target:
- withdrawing the identical-tree disjunct closes 5c55d4b B1, and the anchor invariant is now stated;
- the content-based region definition closes 5c55d4b B2;
- N1, N2, N4, N5 and N7 are closed;
- N3 is closed in its restrictive direction, and its repair is B1's entry point;
- N6 is partly closed.

**The matching family (§6) and the D1-D3 change-rule family have no blocker this round.** This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blockers by earliest owner

### B1 — Frame-scoped gate decisions accumulate at integration, so one gate obligation can have two standing passing decisions, and an earlier unqualified one closes a later qualified one

**Earliest owner.** Manual §7.5, the new sentence "Answered and standing are read in the frame of the obligation …", read with:
- §5.5 ("One standing gate decision" and `standing h` in the `valid` block);
- §8.3 step 7 (the supersession-only rule for a second passing gate decision);
- §10.2 (run membership of earlier iterations and rebases);
- §10.4 (the gate term of discharge);
- §11.5 step 3 (the integration request carries no new judgment);
- §16.8 ("Qualified gates").

These are workplan §21 items 3 (gate outcome vocabulary), 5 (declared frame per kind), 7 (three-valued discharge, provisional propagation) and 10 (gate templates meeting Channel C). It is a D3 defect and asks for no D1/D2 change.

**Owner and contract text.**
- Workflow owner, Channel C (7.2.1): "The gate does not close unqualified when missing realized records could plausibly change its judgment."
- SD-24, verbatim: a `QUALIFIED` `GATE_DECISION ACCEPT` "supports validity and discharge only as `P` … until an unqualified gate decision on the same revision". Stakeholder entry 18: "so the subject and its dependents stay visibly qualified until a later unqualified gate decision".
- Manual §5.5: "Each gate obligation has at most one standing passing decision … a second holder can therefore block or veto but not qualify. The gate term reads that one decision"; in the formula block, "standing h: the gate obligation's one passing decision not superseded".
- Manual §7.5 (new): "Answered and standing are read in the frame of the obligation: a frame-`X` decision answers only the frame's obligation, and until `X` integrates it is neither the standing decision nor current in the admitted state or in another frame".
- Manual §8.3 step 7: "a passing `GATE_DECISION` on a gate obligation that already has a standing passing decision … is admitted only as a supersession of that decision".
- Manual §11.5 step 3: the integration request is "the candidate plus references to those admitted records … carrying no new judgment".
- Manual §31.6: "only a supersession by its own author's `UNQUALIFIED` `ACCEPT` or the owner's adjudication ends the qualification"; "a second holder's passing decision on an answered gate is refused unless it supersedes the standing one as owner".

**Trajectory.**
1. Setup:
   - project policy requires human gate `g` on subject `s`, which is not a `NATIVE` subject of kind D1 or D2, so no revision run applies (§10.2). Two natural cases: a D3 subject under a D3 gate, or an `EVIDENCE_SPEC` unit in a D2 domain under the D2 owner's gate (§10.2 excludes such units from the run rule);
   - `s` is at `r0` at admitted head `n`, base `B`.
2. Two candidates both change `s` from `r0` to the same `r'`:
   - `X`, for item `I_X`;
   - `Y`, for a different item `I_Y`, stacked on `X`'s commit (`tree(C_Y)` holds `X`'s change to `s` plus other work), with recorded base `B`.

   Both frames exist, and `s ∈ Δ(X)` and `s ∈ Δ(Y)` (§7.1 computes `Δ` against `B`). `GATE(g)` on `(s, scope_id(s), r')` is derived in each frame. For a subject outside the run rule its identity is the same in both frames and in the admitted state.
3. At position `p1`, holder `H_Y` records, in frame `Y`, `GATE_DECISION ACCEPT` with `adequacy = ADEQUATE` and `qualification = UNQUALIFIED`. It is the first passing decision in frame `Y`, so step 7 admits it.
4. A later realization shows a material limitation. At position `p2 > p1`, holder `H_X` records, in frame `X`, `ACCEPT`, `ADEQUATE`, `QUALIFIED`, naming the qualifying records. By §7.5, `H_Y`'s frame-`Y` decision is "neither the standing decision nor current … in another frame", so this is the first passing decision in frame `X`, and step 7 admits it.
5. `X` integrates at `p3`. `h_q` (from `H_X`) stands in the admitted state; the gate term is `P`, `valid(s) ≤ P`, and the §16.8 entry is open. Correct so far.
6. `Y` integrates at `p4`:
   - the merge is clean, because the change to `s` is identical on both sides (§7.2);
   - `h_u` (from `H_Y`) is a frame record of the integrating transformation, its `content (s, r')` entry holds in its output role, and its core's records are `Y`'s own;
   - Admission checks nothing about it, because the integration request carries no new judgment.

   By §7.5, `h_u` now stands as well.
7. The admitted state holds two unsuperseded passing decisions on one gate obligation. "The one passing decision not superseded" does not denote, and the implementer must choose:

   | Reading | Gate term | Result |
   |---|---|---|
   | the formula as written, `⋁` over standing decisions | `max(P, T) = T` | `valid(s)` and every descendant `T`; discharge `DISCHARGED`, though `h_q` is never superseded, no unqualified decision is later than it, and the §16.8 entry stays open claiming the decision "caps validity" |
   | the first by ledger position | `h_u` | `T` |
   | the first to become standing | `h_q` | `P` |
   | `min` | `P` | `P` |

8. Under the first two readings, `H_X`'s recorded material limitation is closed unqualified by another holder's earlier decision, which was rendered on a core that could not show that limitation (it did not exist at `p1`). That contradicts:
   - the Channel C rule;
   - entry 18's "later";
   - §5.5 ("a second holder can … not qualify");
   - §31.6 (only supersession ends a qualification).

   The single-frame route forbids exactly this outcome: there `H_X`'s decision would have been a refused second decision, and `H_X` would have challenged or recorded a `REJECT`.

**Siblings (family search; one cause: uniqueness of the standing decision is checked once, when a decision is admitted, in its own frame, while the set of decisions that stand in a state grows later).**
- **(i) Reverse integration order.** `Y` integrates first, so `h_u` stands and the gate term is `T`. When `X` integrates, `h_q` stands too and the term stays `T` under `⋁`. The qualification never takes effect.
- **(ii) Iterations of one lineage, `NATIVE` D1/D2 (the default gates).** `H1` records a `QUALIFIED` decision in iteration 1's frame `X1`. In iteration 2's frame `X2`, with `s` still at `r'`:
  - §7.5 says `h1` is not standing ("another frame"), so `GATE(g)` is ready again and `H2` records `UNQUALIFIED`;
  - but §10.2 puts "the frame records of `X` and of earlier iterations and rebases of its enactment lineage" in `X2`'s prospective run. On that reading `h1` answers in `X2`, and `H2`'s decision is refused unless it is a supersession.

  After `X2` integrates, `h1` is in the run. Whether it stands depends on whether a later iteration's integration counts as "`X1` integrates", as §7.6 rule 1 lets an enactment lineage do for prospective acceptances. If it does, the primary trajectory recurs for D1/D2 gates. If it does not, §10.2's inclusion of earlier iterations' gate decisions is dead text. Either way the text contradicts itself.
- **(iii) Rebase of one lineage, any subject.** §7.6 says a frame-`X` record "counts for `X'`" when its entries hold. A second holder who decided in `X'`'s frame under §7.5 gives two standing decisions at `X'`'s integration if "counts for" includes standing.
- **Held:**
  - `NATIVE` D1/D2 across lineages: `Y`'s frame records belong to "a lineage other than the one that started the run", so they are never current, and after `X` integrates `Y`'s prospective run is the admitted run;
  - abandoned candidates, which never integrate (§31.6 tests this);
  - non-D1/D2 restoration with a reused admitted decision, which stands in the restoring frame, so a second frame decision is refused there;
  - the single-frame second holder, who is refused.
- **Adverse side (non-blocking, N2).** §7.5's "a frame-`X` decision" also literally covers a `REJECT`, while §5.5's `vetoed` counts "∃ admitted adverse `j⁻`" in any frame. The formula governs (§0.1), but the sentence should be scoped to passing decisions.

Further search, such as which gate cores render which qualifying records across frames, would be implementation-like.

**Surfacing.** Nothing discloses the trajectory:
- §31.6's new cases cover only abandoned candidates and admitted-frame decisions before integration;
- the closure map row 5 reads "gate decisions answering a frame's gate obligation declare its frame and stand only there until integration";
- the author-choice bullet ("a second holder can block or veto but not qualify") states the property B1 falsifies.

**Family assessment.** This is the gate family's seventh finding:
- 3540d98 B3 (no propagation);
- e9e6e9f B2 (cap followed currency);
- a18b544 B2 (cap keyed and lifted on other identities);
- 0b6c4fa B2 (tenure filter only in `valid`);
- 27ef339 B3 (gates derived in frames but decided only in the admitted frame);
- 5c55d4b N3 (standing scope across frames);
- now B1.

Since a18b544, every round has kept one presupposition: a gate obligation has exactly one standing passing decision, enforced by an Admission-time supersession rule. Each repair then changed which states a decision counts in: runs, tenures, frames, and now frame-scoped standing. Each such change creates a new way for several decisions to come to stand without passing that check. This is a **non-local recurrence**, so the convergence owner's simplification trigger applies. The repair should remove the uniqueness presupposition rather than add another scope rule.

**Options for the stakeholder (Phase C handoff §5).**
- **(a) Subtractive, recommended.** The gate term reads every unsuperseded passing decision on the obligation that is eligible in the state, by `min`: `⋀_{h passing, unsuperseded, eligible, for g} (current(h) ∧ unq(h))`, which is `F` when there is none.
  - A qualification then lifts only when its own decision is superseded, by its author's reassessment or the owner's adjudication, whatever another frame decided.
  - A non-current decision lowers the term and derives `REVALIDATE` for it, which matches §5.5's "nothing earlier remains to fall back on".
  - The §8.3 step 7 supersession rule can stay as hygiene. It is no longer a correctness premise, and §5.5's uniqueness sentence and "the one" go.
  - No record, state or latch is added. The restrictive cost: a stale decision from another frame or an earlier iteration must be revalidated or superseded before the gate is `T`.
  - It also avoids resolving the holders' disagreement by "serialized record position" (evidence owner).
- **(b) Narrowing.** A frame decision stands after integration only if it is in the integrating transformation's own frame and the obligation has no standing passing decision in the admitted state at that admission. Otherwise it never stands, like an abandoned candidate's. State also whether a later iteration's or rebase's integration integrates an earlier frame's gate decision.
  - This adds one S0 condition.
  - A later-integrated `QUALIFIED` decision then becomes inert, and must still be surfaced (an inspector entry), which adds visibility mechanism. It keeps an order-based choice between holders.
- **(c) Not recommended.** Withdraw the author's narrowing of SD-24 (closure map §5) and return to the reviewed workplan's existential gate term with a per-decision cap. This is the `⋁` reading. It needs the stakeholder to accept that an earlier unqualified decision may close a later qualification, contrary to entry 18's "later".

Whichever is chosen, state the invariant once in §5.5 so later repairs can be checked against it: **in every state, the gate term is a function of every unsuperseded passing decision eligible in that state, and a `QUALIFIED` one among them caps it until it is itself superseded.**

**Required discriminators.** These run at the real Admission → Derivation (`valid`, discharge) → inspector owners, with nothing seeded resolved:
- **(A)** The primary trajectory, with `s` a D3 subject and, separately, a D2-domain `EVIDENCE_SPEC`. After both integrations the gate term is `P`, discharge is `DISCHARGED_PROVISIONAL` or `OPEN` per policy, and the §16.8 entry is open. Only `H_X`'s own `UNQUALIFIED` supersession, or the owner's adjudication, gives `T`.
- **(B)** Sibling (i), the reverse integration order: the same expectations.
- **(C)** Sibling (ii), with a `NATIVE` D2 subject (`QUALIFIED` in iteration 1's frame, `UNQUALIFIED` in iteration 2's): after iteration 2 integrates, the value is the one the repaired rule states, never `T` through an unsuperseded `QUALIFIED` decision in the run.
- **(D)** Contrast: one frame decision, `QUALIFIED`, then integration gives `P` (existing §31.6).

An implementation that takes `⋁`, or the first decision by position, over several unsuperseded passing decisions must fail (A).

## 2. Non-blocking findings

- **N1 — `link⁻`'s range uses an undefined qualifier.**
  - The new parenthetical says `o'` "ranges over every admitted observation of `conf(a⁻)` with a complete recorded basis, `INCOMPLETE` ones and those of never-integrated frames included". "Complete recorded basis" is defined nowhere.
  - The natural meaning is "fully recorded". It could be misread as "completeness-bounded", which would exclude `o' = o` for an unbounded `o`, against the same parenthetical's "`o' = o` gives `on⁻(o, K)`".
  - No stop is affected, because every stop has a bounded anchor (the stated invariant). But the floor's yielding clause, which now reads `link⁻`, would lose an unbounded yielding run on the identical tree under the misreading.
  - Define the qualifier, or delete it: a partially recorded basis only links more.
- **N2 — The frame scope of adverse gate decisions** (B1's adverse sibling).
  - §7.5's sentence about "a frame-`X` decision" literally covers a `REJECT`, while §5.5's `vetoed` reads any admitted adverse judgment, and R9 says "whatever their order".
  - The formula governs, so an abandoned candidate's `REJECT` of revision `r'` vetoes a later passing decision on the identical triple.
  - State that the frame scoping concerns passing decisions only.
- **N3 — Line-granular diff alignment in the region test (5c55d4b B2 repair).**
  - "Bytes enter or leave it under the pinned diff alignment (§7.2)" inherits §7.2's line-wise algorithm.
  - Where a D1-D3 symbol span shares a line with D4 bytes (C or C++ one-line definitions, minified files), a D4 edit on that line realigns the whole line. The D1-D3 region then counts as changed, so the item is a `VIOLATION`.
  - The failure is fail-closed and rare, but undisclosed. State byte-level alignment inside changed hunks, or list the residual in §32.2.
- **N4 — Residue of 5c55d4b N3 (obligation identity).** "In a frame, `run(s)` is the frame's prospective run" still gives the `run(s)` parameter no value, because a prospective run has no position.
  - Answering is by run membership (§10.3), so derivation is unaffected.
  - But an envelope's `obligation_id` for a frame `ACCEPT` or `REVIEW(s, r)` must be computable. Name the parameter's frame value (for example, the enactment lineage), or state that frame obligations match by membership and not by identity hash.
- **N5 — Qualification gaps (DS-001).**
  - §31 has no case in which two frames' gate decisions integrate (B1), and none for iterations or rebases deciding a gate afresh.
  - 5c55d4b B2 discriminator (D) (moving `numerics.flux`'s anchors so that it owns different bytes is a `VIOLATION`) was not carried.
  - No case isolates the region criterion from owned content.
  - A §31 written to the current text is green with B1 present.
- **N6 — Editorial residue of the 5c55d4b B1 repair.** §6.6's bullet and §32.2 say an unbounded basis "matches adversely only an identical tree". That is true of its own `on⁻`, but through `link⁻` an unbounded run is linked to any tree that agrees with a narrow anchor. The understatement is harmless, but it is not what consumers read.
- **N7 — Accounting.**
  - Closure map row 5 now records B1's mechanism as `CARRIED + DECIDED`.
  - The author-choice bullet on "one standing decision per gate obligation" states the property B1 falsifies.
  - The aid confers no authority.

## 3. Closure audit

Each workplan §21 item and clause was located in the Manual directly; the closure map was used only as an index, and its claims were checked. "Answered" means a substantive D3 answer exists; it is neither runtime evidence nor stakeholder acceptance.

The diff since 5c55d4b touches §0.3 (the history paragraph), §0.4 S11, §1.2, §6.6, §6.8, §7.5, §30, §31.2, §31.3, §31.6, §32.2, closure-map row 5 and the author-choice list. Rows outside those sections carry the 5c55d4b audit, which I re-checked against my whole-Manual read.

| §21 | Independently located answer | Result |
|---|---|---|
| 1 | §§1.1-1.11 | Answered. The write-set region comparison is now by content (5c55d4b B2 closed); N3 is a disclosed-cost residue |
| 2 | §§1.7, 2.1-2.6 | Answered |
| 3 | §§3.1-3.6, 5.5, 6.8, 17.1 | **Gate qualification is not single-valued across frames (B1)** |
| 4 | §§4.1-4.6, 6.3 | Answered. Every stop rests on a bounded reproduction (5c55d4b B1 closed) |
| 5 | §§5-7, 17, 22.3 | `stale` answered. Strata, single-valuedness and monotonicity hold (`link⁻` reads only S0; the floor's `link⁻` only enlarges adverse matches). **The declared frame per kind for gate decisions carries B1** |
| 6 | §§8, 21-23 | Answered; the step 7 gate rule is an admission-time check only (B1) |
| 7 | §10 | **Three-valued discharge reads B1's ambiguous gate term** |
| 8 | §11, §13.2, §13.4 | Answered |
| 9 | §9 | Answered |
| 10 | §16 | Answered; the §16.8 qualified-gate entry inherits B1 |
| 11 | §§17, 6.10 | Answered |
| 12 | §18 | Answered |
| 13 | §§19-20 | Answered; S11 is now reconciled with R10 |
| 14-16 | §§21-25 | Answered; runtime unexecuted |
| 17 | §26 (both transfer tables) | Answered |
| 18, 19 | §§27, 28 | Answered |
| 20 | §20 | Answered |
| 21 | §29.7 | Answered; the Channel C row rests on B1 |
| 22 | §30 | Present and updated (the identical-tree route has been removed from the accounting) |
| 23 | §12, §1.2, §13.2 | Answered; the domain-rule input is now consistent |
| 24 | §13 | Answered |
| 25 | §14 | Answered as design; no threshold accepted |
| 26 | §§15-16 | Answered |
| 27 | §29 | Present; see section 9 |

**Workplan §16.2, both tables.** The diff does not touch §26.4. I re-read §26.3-§26.4 against the workplan's **Deferred** rows. Every one has a final disposition, and none is merely routed:
- invariants 4, 9, 15, 17 and 26;
- the §5 sub-rules;
- §6, §7 and §12;
- §18.

**Material decisions versus delegated D4.** Parsers, the diff implementation, checkpoint encoding, limit values and the file-type table remain correctly `[delegated]`. One architectural decision is left contradictory: which passing gate decisions stand once several frames' decisions have integrated (B1). The diff alignment's granularity (N3) is a delegated detail with an architectural cost that should be disclosed.

## 4. Refinements R1-R11

| # | Assessment |
|---|---|
| R1 | **Sound.** With the identical-tree disjunct withdrawn, every permissive use reads `on⁺`, and an unbounded basis serves none. The anchor invariant ("every stop rests on a narrow record of the failing run's content") holds: (1) requires a bounded `r'` with `on⁺(r', tree(a⁻))`, and `o' = r'` links every run on content that agrees with `tree(a⁻)` on `r'`'s basis; likewise for (4) through (3)'s bounded witness. `on⁺ ⇒ on⁻ ⇒ link⁻` holds. A wrong completeness judgment is restrictive only for the adverse conditions (now disclosed, §32.2). N1 is editorial |
| R2 | Sound; unchanged. `link⁻` adds no support-graph edge |
| R3 | Sound; unchanged |
| R4 | Sound within its crash model; unchanged |
| R5 | Sound. The write set's region comparison is now by content and consistent with partition by construction (N3 is a disclosed-cost residue) |
| R6, R7, R8 | Sound; unchanged |
| R9 | Sound. The veto's `same` for `GATE_DECISION` is per obligation and revision in every frame; N2 asks that §7.5 not be read against it |
| R10 | Sound, and now consistent with S11 in §0.4 |
| R11 | **Unsound across frames (B1).** Its stated property, "a human's bounded, qualified decision stays visibly provisional instead of closing as unqualified", fails once two frames' decisions integrate. It also narrows SD-24 for second holders; this is surfaced as an author choice, which I would put to the stakeholder together with B1's options |

## 5. Previous findings and Phase B closures

"Closed" means I re-derived that the present text excludes the named trajectory; it is not runtime evidence.

**Depth.** I re-derived every 5c55d4b item in full. For the earlier records, I took the 5c55d4b record's re-verification tables as hypotheses. I re-checked every disposition that the 5c55d4b-to-575dc78 diff or B1 touches, and I read the gate-family blockers (a18b544 B2, 27ef339 B3) and 27ef339 N1 in full. I did not re-read the full prose of the earlier records (section 10).

### 5C55D4B (same family)

| ID | Disposition and basis |
|---|---|
| B1 | **Closed.** (1) no longer has the identical-tree disjunct, so every stop needs a bounded reproduction, which anchors `link⁻`. In the primary trajectory `a⁻` is not stale at `T3`, because (1) fails until a bounded reproduction exists, and that reproduction then links `d`. Discriminator (B) holds likewise. Discriminator (C) holds: a bounded `a⁻` links `d` through `real(a⁻)`. The invariant is stated in §6.6; §31.2 adds the case |
| B2 | **Closed.** §1.2 now defines a region difference by resolution status and by bytes entering or leaving under the pinned alignment, never by position. All three trajectories are `CLEAN` (D4 above a D2 span; `kern.helper`; a nested D2 edit, where the residual gains no bytes and the composite sentence exempts the composite). A moved anchor that gives the D2 unit different bytes stays in the set through owned content. Residues: N3 and N5 |
| N1 | Closed: R1, §6.5, §6.6, §6.9 and §30 now match the formulas. Residual understatement: N6 |
| N2 | Closed: the floor's yielding clause reads `link⁻` |
| N3 | **Closed in its restrictive direction** (an abandoned candidate's decision never stands; frame decisions declare their frame). **Its repair introduced B1.** Obligation-identity residue: N4 |
| N4 | Closed: §0.4 S11 now states R10's reuse across tenures |
| N5 | Closed: the range and the fail-closed cost are stated (§6.6, §32.2). Editorial residue: N1 |
| N6 | **Partly closed.** 27ef339 B2 (C) and (D) and 27ef339 B3 (B) and (C) are now in §31.2 and §31.6, and the unbounded-failure case is added. 5c55d4b B2 (D) and any B1 case are missing (N5) |
| N7 | Closed for its items; the new accounting residue is N7 |

### 27EF339 (same family)

| ID | Disposition |
|---|---|
| B1 | Closed for bounded and, now, for unbounded failures (`link⁻` through the required bounded reproduction) |
| B2 | Closed (byte attribution, and now position-free regions) |
| B3 | Closed (frame-declared gate decisions integrate). The family recurs as **B1** through the 5c55d4b N3 repair |
| N1 | Closed as disclosure: the extra bounded reproduction after a fix inside the judgment's scope is stated in §31.3 and closure map §5, and the narrowing disjunct is withdrawn |
| N2 | Closed as surfacing; the stakeholder decision is pending |
| N3 | Closed (S11) |
| N4 | Closed ("its author or the owner, whichever answers first") |
| N5 | Closed within one frame; across frames, B1 |
| N6, N7 | Closed |

### 0B6C4FA, A18B544, E9E6E9F, E2154AC (same family)

| Review | ID | Disposition |
|---|---|---|
| 0B6C4FA | B1 | Closed: (i) and (iii) as before, (ii) through `link⁻`; the unbounded side is now closed too |
| 0B6C4FA | B2 | Closed for its trajectory; the gate family recurs as B1 |
| 0B6C4FA | N1 | Closed as surfacing; stakeholder confirmation pending |
| 0B6C4FA | N2 | Closed within one frame; B1 across frames |
| 0B6C4FA | N3, N4, N6, N7 | Closed |
| 0B6C4FA | N5 | Closed (the chain ended in 5c55d4b B2, now closed) |
| A18B544 | B1 | Closed |
| A18B544 | B2 | Closed for its trajectories (a) and (b); its family recurs as B1 |
| A18B544 | N1, N2, N4, N5 | Closed or superseded as in the 5c55d4b record |
| A18B544 | N3 | Closed (chain ended in 5c55d4b B2) |
| A18B544 | N6 | Superseded |
| E9E6E9F | B1, N1-N5 | Closed or superseded as before |
| E9E6E9F | B2 | Closed for its trajectory; family B1 |
| E2154AC | B1, N1-N5 | Closed |

### 3540D98 (different family)

| ID | Disposition |
|---|---|
| B1 | Closed: exact identity, unchanged |
| B2 | Closed: full external-input set, unchanged |
| B3 | **Closed within one frame; reopened across frames as B1.** A qualified gate decision is defeated by another frame's unqualified decision |
| B4 | Closed: equal regions, unchanged |
| N1 | Closed for acceptances and gate decisions (prospective run); see N4 for obligation identity |
| N2-N4 | Held as disclosures |

### 798B2B4, 71CF9B3, 86AB683

| Review | ID | Disposition |
|---|---|---|
| 798B2B4 | B1-B3 | Closed: the revision run is unchanged, and D1/D2 gate decisions of other lineages are outside it. The iteration sibling of B1 concerns gate standing, not run membership |
| 798B2B4 | B4, N1-N8 | Closed |
| 71CF9B3 | B1, B2, N1-N8 | Closed |
| 86AB683 | B1, N1-N7 | Closed |

### 1FFBBF0, 53669A5, D837363

| Review | ID | Disposition |
|---|---|---|
| 1FFBBF0 | B1, B2, N1, N3-N7 | Closed |
| 1FFBBF0 | N2 | **Closed** (content reading of "resolved regions" now stated) |
| 53669A5 | B1-B3, N2-N9 | Closed |
| 53669A5 | N1 | The SD-17 partial reversal is surfaced, with its cost restated after the 5c55d4b B1 withdrawal; not decided |
| D837363 | B1-B4, N3-N8 | Closed (B4's region comparison now content-based) |
| D837363 | N1, N2 | Closed (the nested-subject and cross-kind routes are consistent with the region definition) |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

| Review | ID | Disposition |
|---|---|---|
| CC005DB | B1-B3, N1-N8 | Closed |
| C6DA678 | B1-B3, N1-N12 | Closed |
| B595F2C | B1 | **Closed** (bounded and unbounded failures) |
| B595F2C | B2-B4, N1-N8 | Closed |
| 6FF4ED1 | B1 | Closed: `on⁺ ⇒ on⁻ ⇒ link⁻` with frozen context |
| 6FF4ED1 | B2-B4, N1-N12 | Closed |

### Phase B §3 closures and N1-N4

| Closure or limit | Present reconstruction |
|---|---|
| EF8445A/552AC01 N2: strata, completeness polarity | **Re-tested in both directions.** Take a differing old-content run and a yielding present-content run on an alternate tree that differs only outside a recorded narrow basis, under a judgment that becomes `P`, blocked, revoked or loss-withheld. **Held** for every recorded width. For a bounded failure the anchor is `real(a⁻)`. For an unbounded failure no stop exists until a bounded reproduction exists, and that reproduction then anchors. Losing the judgment only removes `bound`, so (1) and (3) fail and nothing adverse is removed. Restrictive direction: a stop is withdrawn only by a newly admitted anchor whose narrower basis links an old differing run. That has a cause (the newer judgment says the difference was not read), and it is fail-closed when the judgment is wrong (disclosed, §32.2) |
| Fail-closed support cycles; corrupt prefixes | Held. `link⁻` and the floor change are S0 and add no edge, and `INTEGRITY_HALT` is unchanged |
| Y1/Y2, X1-X3, candidate-own latch, floor and class | Held; the floor now reads `link⁻`, which only adds floor events |
| Contrary-run retention, nondeterminism | Held for bounded and unbounded failures |
| U1/U2/W1/W2 executed content | Held for currency |
| Absorbed relaxation; adversity versus currency, challenge, loss; salvage; independence; start latch; effective structure, quarantine, tenure | Held. Gate frames: **B1** |
| Phase B N1 | Disclosed (§32.2, §32.4) |
| Phase B N3 | Held (§31.3) |
| Phase B N4 | Held as reopen triggers |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | 5c55d4b B1 primary: unbounded failure, unbounded identical-tree reproductions, differing run after a doc edit, later judgment and fix | Held: no bounded reproduction means no stop; a later bounded reproduction links `d` |
| 2 | Bounded failure, unbounded identical-tree reproduction, differing unbounded run | Held (`real(a⁻)`) |
| 3 | Fresh bounded reproduction on `tree(a⁻)` bounded by a post-fix judgment that omits a file the failing run read | Restrictive only: `r'` links more |
| 4 | New narrow anchor admitted later linking an old differing run (withdrawn stop) | Withdrawn with cause, or fail-closed |
| 5 | Floor for a candidate-own bounded failure under the `link⁻` floor clause | Held: anchors that match `T_m` are admitted-content runs, so a yield there is genuine |
| 6 | `INCOMPLETE` or never-integrated-frame observations as anchors | Restrictive only (N1 is editorial) |
| 7 | Structure, `ignore`, analyzer or system-version change with the tree fixed | Held (`on⁻`, `link⁻` unchanged) |
| 8 | Free seed, free backend, external-set variants | Held (unchanged since earlier rounds) |
| 9 | Length-changing D4 edit above a D2 span; `kern.helper`; nested D2 edit in a D3 composite | Held (`CLEAN`) |
| 10 | D4 edit moving a D2 anchor so the D2 unit owns different bytes | Held (`VIOLATION` by owned content) |
| 11 | D4 edit on a line shared with a D1-D3 symbol span | Fail-closed `VIOLATION` (N3) |
| 12 | Prefix D2 unit gaining a file, a nested D4 file, or an `ignore` change | Held (bytes enter; the composite sentence for a nested subject; the governed boundary) |
| 13 | Two lineages change a non-D1/D2 gated subject identically; `UNQUALIFIED` then `QUALIFIED` frame decisions; both integrate | **Violation (B1)** |
| 14 | As 13, reverse integration order | **Violation (B1 (i))** |
| 15 | As 13 with a `NATIVE` D2 subject across lineages | Held (run membership) |
| 16 | `NATIVE` D2 iterations: `QUALIFIED` in iteration 1, `UNQUALIFIED` in iteration 2 | **Contradiction (B1 (ii))** |
| 17 | Rebase with a second holder deciding in the rebased frame | **Contradiction (B1 (iii))** |
| 18 | Abandoned candidate's frame decision; identical bytes absorbed | Held |
| 19 | Abandoned candidate's frame `REJECT` on the identical revision | Vetoes by §5.5 (N2 asks that §7.5 not suggest otherwise) |
| 20 | Non-D1/D2 restoration reusing an admitted `QUALIFIED` decision; second decision in the restoring frame | Held (refused) |
| 21 | Second holder's challenge of the subject triple, then supersession; `REVALIDATE` of a stale gate decision | Held |
| 22 | Support cycle via absorbed `about` or a completeness edge; corrupt authenticated prefix | Held |
| 23 | Publication crash windows, fence chains, ABA | Text unchanged for many rounds; not re-attacked in depth |

## 7. Minimum architecture and capability transfer

**What changed this round.** No primitive, component, persistent surface or record tier is added. The round:
- removed the identical-tree disjunct (subtractive);
- stated the anchor invariant;
- changed the floor's predicate (`on⁻` to `link⁻`);
- defined region difference by content (a definition, not a mechanism);
- scoped frame gate decisions.

B1 entered through the last change. Its recommended repair (a) removes the uniqueness presupposition from derivation instead of adding a further scope rule. §30's accounting is current apart from B1's consequence for R11.

**Capability transfer.**
- The §26.4 tables are unchanged and resolve every Deferred §16.2 row.
- Core prompt mode, frozen profiles and the containment root are preserved, and Core never imports SSDS. PC-001 holds.
- PEM was activated, because this is mature-machinery replacement:
  - `PROJECT-ENGINEERING-MEMORY.md` is byte-identical on `main` and at the candidate (`15617971…`);
  - the validator, run from the checkout (whose `source/` and PEM are identical to the candidate's), reports "PEM schema 1 valid: 5 families, 0 notices";
  - `tests.test_protocol_63_engineering_memory` passes at the snapshot (28 tests).
- HAS dispositions:
  - PC-001 applicable, held (§26.4, §28, §31.8);
  - FF-001 applicable to genesis, held (§19.9);
  - SP-002 applicable to self-reference, held (§8.7, G3);
  - SP-001 not materially applicable to this Manual;
  - DS-001 applicable to §31 (N5: green fixtures coexist with B1).
- Absence of a 7.x memory entry proves nothing.

`orchestrator/docs/architecture.md` (blob `39e6de72…`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## 8. Qualification-design adequacy

§31.1 states that no executable SSDS evidence exists at G1 and that every runtime group is `UNEXECUTED`. Nothing is claimed as executed.

Green fixtures could coexist with B1 (DS-001):
- **Gate frames.** §31.6 runs:
  - one frame integrating;
  - an abandoned candidate;
  - an admitted-frame decision before integration.

  No case integrates two frames whose decisions answer one gate obligation, and none decides a gate afresh in a later iteration or rebase.
- **Regions.** 5c55d4b B2 (D) is absent, and no case isolates the region criterion from owned content (N5).

The §6 family's cases now include the unbounded-failure case that 5c55d4b B1 required, and §31.3 "Red then green" states the restored cost honestly.

The diagnostic model was not run (optional). Its file is unchanged since the Phase B candidate, and it models none of these clauses.

## 9. Doctrine-realization map and O1

§29 is unchanged this round. I re-checked §29.2-§29.5 against:
- the 7.2.1 D3 entrypoint and its expanded entry contract;
- the role-contract rows;
- every scientific-checks duty.

Status of the claims affected by this round:
- §29.4's disagreement-survival claim, via §6, now holds.
- §29.2's routing row (E0 through the §13.2 domain rule) is now coherent with the content-based write set, with the N3 fail-closed edge.
- §29.7's Channel C row ("refusal of an unqualified accept with known missing evidence") and the human-gate realization rest on **B1**: across frames, closure can be unqualified while a standing qualified decision records a known material limitation. The §16.6 refusal rule is never consulted for the earlier, already admitted, unqualified decision.

§29.6's E3 list is adequate.

O1 (§0.5) states the realized record, readers, routine questions and realized-record architecture. It visibly marks the within-deliverable surfaces, and "Beyond the requested deliverable: **None**". I found no unmarked inspectability-driven product requirement and no mark wrongly classed as within the deliverable. Technical Review accepts no marked item; a marked item beyond the deliverable binds only after stakeholder or task acceptance.

## 10. What I verified and how; what I could not verify

**Verified at the exact candidate** (`git archive` snapshot under `$TMPDIR/ssds80-manual-review-575dc78/`):
- **Reading.**
  - The whole Manual, sections 0-33. §21-§25 were read for change and consistency, not re-attacked.
  - The diff from 5c55d4b (Manual and closure map).
  - Closure-map §1 (first rows), row 5 and the author-choice list.
  - Workplan §21 and its gate term (§7.4).
  - Stakeholder record items 18-19 and SD-14, SD-23 and SD-24.
  - The 5c55d4b record in full; a18b544 B2, 27ef339 B3 and 27ef339 N1.
  - Governing owners as listed.
- **Blobs.** The Manual, closure-map, workplan and Phase B blobs match the handoff.
- **Tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the snapshot: 4 tests, OK.
- **Whitespace.** `git diff --check 5c55d4b… 575dc78…`: clean (exit 0).
- **Additions.** `git diff --stat fad3ee4… 575dc78…`: 41 files, 12,703 insertions, 1 deletion. All are under `qualification/ssds80/`, plus the Manual and two lines in `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. Since 5c55d4b, only the Manual and the closure map changed, besides the 5c55d4b handoff and record.
- **Frozen surfaces.** `git diff --quiet fad3ee4… 575dc78… -- orchestrator/docs/architecture.md source dist`: exit 0.
- **PEM.** As in section 7.

**Not verified:**
- any SSDS runtime behavior (none exists);
- tracer fidelity and G3 costs;
- the full prose of Review records before 5c55d4b, beyond the findings and dispositions named in section 5;
- deep re-derivation of findings whose cited text is unchanged since 5c55d4b;
- publication and fencing, which were not re-attacked;
- which records a gate core renders across frames (implementation-like);
- the diagnostic model, which was not run.

Family search in B1 stopped at characterization, as method step 6a allows.

## 11. Scientific-checks answers

This task reviews D3 authority for software that mediates scientific evidence.

1. **Material findings.**
   - Blocker B1 and non-blocking N1-N7, all D3 architecture or coordination findings.
   - I have no D1/D2 scientific or numerical findings and no out-of-scope scientific findings.
   - I launched no agents. The tools I ran (section 10) produced no finding beyond those stated.
2. **Realized results.** I produced, ran and reviewed no realized scientific results and prepared no gate evidence, so no null envelope is owed. The unit tests, the PEM validator and the PEM tests are software checks on documents, not realized results.
3. **Variants.** Yes, design and interpretation variants only. This was not result selection over data, and no data, held-out set, earlier history or delegated search was involved.
   - **Repair options:** three for B1, (a)-(c).
   - **Clause readings, kept as findings rather than resolved:** four readings of the gate term over two standing decisions (`⋁`, first by position, first to stand, `min`; B1), and two readings each of four clauses:
     - whether a later iteration's or rebase's integration integrates an earlier frame's gate decision (B1 (ii), (iii));
     - whether §7.5's frame scoping covers adverse decisions (N2);
     - "complete recorded basis" (N1);
     - line- versus byte-level diff alignment (N3).
   - **Selection criterion:** preserve the owner-required property with the least added mechanism (convergence owner). The B1 choice is the stakeholder's.
4. **Tension search.** Not triggered. I relied on no accepted D1/D2 authority for a consequential judgment; no scientific or numerical formulation is accepted for the SSDS product. The judgments rest on:
   - accepted SSDP 7.2.1 protocol owners (D3, workflow, evidence, convergence, abstraction);
   - the proposed workplan;
   - the stakeholder record and Phase C handoff.

Gaps: none in these answers.

## 12. Common-mode note

I share the Manual author's model family (Claude). The authoring session launched me from a handoff it wrote. The following are shared dependencies:
- the corpus;
- the inherited workplan framing;
- the prior Review records (sixteen of the seventeen Manual Reviews same-family);
- the toolchain.

The 3540d98 and Phase B reviewers were of another family (GPT).

B1 traces to the previous same-family record: it entered through the repair of that record's N3. That record noted the restrictive direction (an abandoned frame's decision standing elsewhere) and asked to state where standing is read. The repair chose frame-scoped standing without examining what happens when several frames integrate.

Repair directions from candidate 13 onward were chosen by the author under the stakeholder's delegation (item 19), not by the stakeholder. Because the gate family has now recurred seven times around one presupposition, I would put these to the stakeholder before any further same-family round:
- B1's options;
- the author's narrowing of SD-24 ("a second holder can block or veto but not qualify");
- the SD-17 partial reversal.

I would also suggest that the gate invariant stated under B1 be written into §5.5, so that a different-family confirmation can test it directly. The stakeholder reserves the choice of a final different-family confirmation.

## 13. D4 statement

SSDS 8 D4 is **not authorized**. This NO-PASS accepts no architecture, no proposed default and no product scope. G1 also requires a later independent PASS on a repaired candidate and explicit stakeholder acceptance. G2 requires a reviewed shadow D3->D4 workplan and explicit stakeholder authorization.
