# SSDS 8 Architecture Manual — Independent D3 Review, candidate b46c250

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: b46c250aefdb78524ac5153097f559a21b512b24
    SCOPE: whole proposed Manual as the durable D3 owner: (a) §21/§16.2 closure, (b) fidelity and
           refinements R1-R11, (c) out-of-matrix adequacy, (d) inheritance and capability transfer,
           (e) qualification design, (f) doctrine-realization map, (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: ce257698d04a44a9e8eb60f48d755867f6a14b67 (checked)
    CLOSURE MAP BLOB: 7fcd40aa006b8613cbf59831d2104202387ed6c1 (review aid only; checked)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; Phase B candidate e23f14208be869e6a78cfd7b312e447254ee1851
           (blob 610f373b97fb8152d2a5742e17fa172e12204756, checked); blob at this candidate
           91bde236465178f20c7348280e036d2884dfc216 (checked)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS, HYPOTHESIS ONLY: E23F142 Phase B PASS; Manual NO-PASS records 6FF4ED1, B595F2C,
           C6DA678, CC005DB, D837363, 53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98, E2154AC,
           E9E6E9F, A18B544, 0B6C4FA, 27EF339, 5C55D4B, 575DC78, F7419D5
    REVIEW METHOD: D3 role entered at the governing public source; whole-Manual read at the exact
           candidate (git archive snapshot); deductive counterexamples in both polarities; family-level
           search after recurrence (convergence owner; handoff method step 6a), attacking hardest the
           f7419d5-round repairs (prospective `elig_G`, state-scoped supersession, deletion of the
           hygiene rule, the step 7 exemption for passing gate decisions, the §7.5 rewrite and the
           §16.8 entry rule); prior-finding regression; required structural checks; no implementation
           or runtime qualification
    REVIEWER: Claude model family (the same family as the Manual's author); a fresh-context
           sub-agent launched by the authoring session from the named handoff; no authoring
           conversation received
    MUTATION BOUNDARY: this record only; no commit or push

Governing SSDP version for this task: 7.2.1.

All Manual section and line references are to the exact candidate. The checkout HEAD was the later handoff commit `4c95e17`, which differs from the candidate only by the handoff file. Governing owners were read at `aaeaf8b…`:

- `source/roles/software-design/SKILL.md` and its expanded `dist/skills/software-design/SKILL.md` (entry contract, Independent Review and Challenge, scientific checks);
- `architecture-and-design.md` (read first, as the entrypoint directs);
- `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review readiness and independent review sufficiency", "Review strategy after recurrence");
- the "Human gates and closeout learning" and "Gate evidence (Channel C)" paragraphs of `workflow-and-workplans.md`, and the "Assessment disagreement" paragraph of `evidence-evolution-and-dependencies.md`.

The other concern owners were not loaded: no decision below turned on them.

## SERIOUS CHALLENGE

**None against accepted SSDP 7.2.1 or the frozen Architecture 1.6.0 / Level 0 Core.** The blocker is a defect of the proposed D3 concretization. The workplan and the Manual are proposed architecture, so a contradiction inside the Manual is not a challenge to accepted authority.

Owner text applied:

- D3 owner, "D3 boundary and feasibility": "A D3 candidate is admissible only when it satisfies every applicable D1/D2 invariant and directly governed security, reliability, compatibility, resource, performance/scaling, deployment and external-interface constraint."
- D3 owner, "D3 formal-contract discipline": "When an architectural concept carries normative meaning, define it before dependent invariants use it".
- D3 role entrypoint: "D3 contradictory/ambiguous/inadequate/unrealizable -> SERIOUS CHALLENGE to D3". Applied to proposed D3, it yields a blocker.
- Workflow owner, human gates: "Orchestration may represent pending/accepted/rejected state but cannot self-approve it." Channel C: "The gate does not close unqualified when missing realized records could plausibly change its judgment."
- Evidence owner, "Assessment disagreement": "supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement."
- Convergence owner, "Review strategy after recurrence": "A clean local repair that genuinely closes the cause remains sufficient; recurrence does not automatically force redesign." "Active simplification trigger": simplification is "mandatory before another additive durable repair when evidence shows repeated patches around the same mechanism".

## Verdict

**NO-PASS.** One D3 blocker survives, stated at family level as method step 6a requires.

- **B1 — gate-qualification family (frame gate decisions across the frame/admitted boundary), ninth round; entered through the f7419d5 B1 repair (state-scoped supersession and prospective identity stated in `elig` and prose only).**
  - The repair closes the f7419d5 trajectory it targets. Frame gate predicates now include the frame's own lineage, so a stale earlier-iteration or rebase decision derives `REVALIDATE` in the frame before integration, and the hygiene rule is gone.
  - But it states two frame-relative semantics only inside `elig_G` and §5.5/§7.5 prose: the effect of a supersession, and the identity of a frame obligation. The S0 facts every other consumer reads stay global or positional: `superseded(x)` (read by `base`), the supersession clause of `stands⁻` (read by the veto), the positional `run(s)` parameter of obligation identity, and §10.2's run-membership rule.
  - **Concrete result (permissive).** A gate holder's `REJECT` vetoes another holder's `ACCEPT` in the admitted state. The holder then reassesses the gate to `ACCEPT` in a candidate frame whose evidence supplies the missing record. That frame record ends the veto in the admitted state at once. The admitted gate closes `T` through the other holder's decision, and stays `T` when the candidate is abandoned, although the missing record never entered the admitted state. Nothing derives an action.
  - **Concrete result (restrictive).** The same frame supersession of an admitted `QUALIFIED` decision makes that decision non-current in the admitted state and in every other candidate's frame. The admitted gate drops from `P` to `F`, and unrelated lineages that require the gate stall.
  - Two further siblings: D1/D2 frame obligation identity is not computable before integration (a regression of 575dc78 N4), and an item-required gate on a D1/D2 subject the frame leaves unchanged is frame-eligible but excluded from the admitted run after integration.

The f7419d5-round repairs otherwise close what they target:
- f7419d5 B1's primary trajectory and its siblings (i), (iii), (v) and (vii) are closed; (ii), (iv) and (vi) are closed only partly (section 5);
- f7419d5 N1, N2, N3 and N5 are closed; N4 is partly closed; N6 stays a stakeholder matter.

**The matching family (§6) has no blocker this round, and the D1-D3 change-rule family has none of its own.** Its run-membership rule takes part in B1 (iv). This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blockers by earliest owner

### B1 — Frame-relative gate semantics are stated in `elig` but not in the supersession, veto, identity and run facts their consumers read, so a never-integrated frame lifts an admitted veto (Channel C), lowers an admitted gate to `F`, and leaves D1/D2 frame obligations without a computable identity or run

**Earliest owner.** Manual §5.5 (`gterm`, `elig_G`, "Gate term", `base`, `stands⁻`, `vetoed`), read with:
- §5.2 (`superseded(x)`, `tgt`);
- §7.5 (declared frame; "Answered and eligible are read prospectively"; frame obligation identity; "Nothing evaluated in a frame changes the admitted state");
- §8.3 steps 2, 3 and 7 (target existence, supersession authority on "the same target", the passing-gate exemption);
- §10.2 (revision run, "in the run", obligation parameters, `REVALIDATE`), §10.3, §10.4;
- §12.2 (envelope `obligation_id`), §16.8 ("Qualified gates"), §31.6.

These are workplan §21 items 3, 5 (declared frame per kind), 7 (obligation rules and discharge) and 10 (gate templates meeting Channel C). It is a D3 defect and asks for no D1/D2 change.

**Owner and contract text.**
- §5.5 (Gate term): "Invariants: in every state the gate term is a function of every unsuperseded passing decision eligible in that state … and for every frame `X`, every gate predicate evaluated in `D_n[X]` … equals its value in the state `X`'s integration would produce"; "a supersession recorded in a frame takes effect only where that frame's decisions are eligible, so an abandoned frame's supersession lifts nothing".
- §5.5 `elig_G`: "every authenticated passing GATE_DECISION for g that is eligible in G and that no superseder eligible in G supersedes".
- §5.2: "`superseded(x)` ⇔ some admitted record names `x` in `supersedes`". §5.5: "`base(z) = F if superseded(z) ∨ …`"; "A superseded record never becomes current again".
- §5.5: "`stands⁻(j⁻) ⇔ ¬∃ d : d supersedes j⁻ … ∧ ¬superseded(d) ∧ status1(d) = CLEAR ∧ cont(d)`"; "`vetoed(z) ⇔ … ∃ admitted adverse j⁻ … ∧ stands⁻(j⁻)`".
- §7.5: "a `GATE_DECISION` answering a gate obligation derived in `D_n[X]` for a subject whose revision `X` changes or that `X`'s item requires … declare frame `id(X)`"; "frame obligations take the identity the integrated obligation will have (gate and subject triple, and for a `NATIVE` D1/D2 subject the run `X`'s integration starts)"; "This scoping concerns passing decisions only; an adverse decision vetoes as §5.5 states, whatever its frame"; "Nothing evaluated in a frame changes the admitted state" (restating workplan §6.9).
- §8.3 step 3: a support-tier record is superseded "only by a record of the same kind on the same target that is either `x`'s own author's reassessment … or the owner's adjudication … For a `GATE_DECISION`, the target is its gate obligation".
- §10.2: "The revision run of `s` at position `k` starts at `run(s)`, the latest admitted position …"; "`ACCEPT(s)`, `GATE(g)` and `REVIEW(s, r)` carry `run(s)` among their parameters"; "Acceptances and records made in frames that were never integrated, or in a lineage other than the one that started the run, are in no run of the admitted state"; the frame's prospective run: "if `X` leaves `cur(s)` unchanged, `s`'s admitted run".
- §10.2 identity: "`sha256("ssds.obligation.v1" ‖ rule id ‖ JCS(target) ‖ JCS(parameters))`". §12.2: the envelope carries `obligation_id`.

**Primary trajectory (permissive; sibling (ii)).**
1. Setup:
   - `s` is a `NATIVE` D3 subject at revision `r`, validly accepted; policy requires human gate `g` for D3 subjects;
   - `G` is the admitted gate obligation on `(s, σ, r)`.

   A D3 subject is used so that no revision-assessment condition applies. The same holds for a D1/D2 subject whose run is unchanged.
2. Two decisions are recorded in the admitted frame:
   - holder `H_Y` records `h_u`: `ACCEPT`, `ADEQUATE`, `UNQUALIFIED`;
   - holder `H_X` records `j⁻`: `REJECT`, whose core names a missing realized record `m` as material.

   Both are admitted. Step 7 exempts the passing decision, and the `REJECT` is never-lost. Then `vetoed(h_u)` holds (same gate obligation and subject revision, `stands⁻(j⁻)`), so `gterm = F` and `ADJUDICATE_DISAGREEMENT(j⁻)` goes to the owner. Correct so far.
3. Candidate `Z` (an `IMPLEMENT` item adding the evidence specification whose realization `ρ_Z` supplies `m`; its item requires `g`) leaves `s` unchanged. By §7.5, `Z`'s frame gate obligation is `G` itself (same gate, triple and run).
4. `H_X` records `d` in frame `id(Z)`: `ACCEPT`, `ADEQUATE`, `UNQUALIFIED`, `supersedes = [j⁻]`, with a `record` entry on `ρ_Z`. Admission checks:
   - step 3: own author's reassessment, same kind, same target;
   - step 6: `ρ_Z` is current in `D_n[Z]`;
   - step 7: the passing-gate exemption applies, and the §16.6 refusal does not, because the core rendered in `Z` lacks nothing.

   `d` is admitted.
5. In the admitted state `D_n`:
   - `superseded(j⁻)` is an S0 fact, so `stands⁻(j⁻) = F`: `d` is not superseded, is `CLEAR`, and `cont` holds;
   - `vetoed(h_u) = F`, and `elig_{D_n}(G) = {h_u}`, because `d` is not eligible in `D_n`;
   - so `gterm = T` and `valid(s) = T`;
   - `ADJUDICATE_DISAGREEMENT(j⁻)` is no longer derived, and the inspector has no entry: no adverse decision stands and no `QUALIFIED` decision is eligible.
6. `Z` is abandoned (budget exhausted, declined, or superseded by other work). The admitted gate stays `T` indefinitely, on `H_Y`'s decision alone. The only holder who judged `m` material reassessed against content that never integrated, and nothing in any view or obligation reports it. Step 5 holds even before abandonment, while `Z` is pending.

   This violates:
   - Channel C: the gate closes unqualified although a missing realized record could change the judgment;
   - the evidence owner's distinction between resolved reassessment and still-live disagreement, since the disagreement is live in the admitted state;
   - §5.5's "an abandoned frame's supersession lifts nothing";
   - §7.5 / workplan §6.9, "Nothing evaluated in a frame changes the admitted state".

   §31.6 (D) covers only the qualification variant and does not catch it.

**Sibling (i), restrictive: frame supersession of a passing admitted decision.**
- Setup: replace `j⁻` with `h_q` (`H_X`'s `ACCEPT`, `QUALIFIED`), so `gterm = P` and, where policy permits provisional continuation, `s` is valid `P`.
- `H_X` records `h_q'` (`UNQUALIFIED`) in frame `Z`, superseding `h_q`. In `D_n`:
  - `h_q` stays in `elig_{D_n}`, because its superseder is not eligible there;
  - but `base(h_q) = F`, because `superseded(h_q)` is global, so `current(h_q) = F` and `gterm = F`;
  - `valid(s)` falls from `P` to `F`, and every descendant whose support passes through `s` falls with it;
  - obligations gated on `g` go `OPEN`, and `REVALIDATE(h_q)` goes to `H_X` or the owner;
  - in every other lineage's frame `D_n[W]` whose item requires `g`, `gterm = F`, so `W` cannot integrate.
- This lasts until `Z` integrates, or `H_X` re-decides in the admitted frame (a third decision, which then stays `QUALIFIED` and keeps capping after `Z` integrates unless superseded again).
- **Common variant.** Candidate `X` changes D4 content that an admitted decision `h_a`'s evidence core read, and `X`'s item requires `g`. `h_a` is stale in `D_n[X]`, so its author revalidates it in frame `X` by superseding it. The admitted gate drops to `F` immediately, although the admitted content `h_a` judged is unchanged.
- This contradicts:
  - §5.5's first invariant (the admitted term depends on a decision not eligible in `D_n`);
  - "a supersession recorded in a frame takes effect only where that frame's decisions are eligible";
  - §7.5's "Nothing evaluated in a frame changes the admitted state".
- An implementer must choose between the normative formula (`base` with the S0 `superseded`) and the prose. The prose reading needs a frame-relative `superseded` that the Manual never defines.

**Sibling (iii): D1/D2 frame obligation identity is not computable.**
- §10.2 keys `ACCEPT`, `GATE` and `REVIEW(s, r)` on `run(s)`, an admitted position. §7.5 says a frame obligation takes "the identity the integrated obligation will have", including "the run `X`'s integration starts".
- That position does not exist before integration and depends on what is admitted first. The f7419d5 repair deleted the sentence that gave frames the lineage in place of `run(s)`.
- So for every D1/D2 subject a candidate changes (every D1/D2 `AUTHOR` item's frame `ACCEPT`, `GATE` and revising `REVIEW`), there is nothing to put in:
  - the envelope's `obligation_id` (§12.2);
  - Admission step 2's "obligation … exists and matches";
  - step 3's "same target".
- Discriminator (C) of §31.6 (the author's post-integration supersession of a `QUALIFIED` D1/D2 frame decision) therefore rests on an undefined identity: f7419d5 B1 (iv) is restated, not closed.
- This is the residue of 3540d98 N1 ("State how the prospective run is represented before integration and rebound at integration"), 5c55d4b N3 ("State that `GATE` and `ACCEPT` match by target triple and run membership, not by the identity hash") and 575dc78 N4 ("a prospective run has no position"), now reopened by the repair.

**Sibling (iv): item-required gate on an unchanged D1/D2 subject.**
1. Candidate `X` leaves a `NATIVE` D2 subject `s` unchanged, and `X`'s item requires its gate `g`. By §7.5 the human's decision `h_X` declares frame `id(X)`.
2. In `D_n[X]`, the prospective run is "`s`'s admitted run". `h_X` was admitted after `run(s)`, so it is in it, and `elig` includes it. The frame gate term is `T` and the Dispatcher submits.
3. After integration, §10.2 puts `h_X`, "made in … a lineage other than the one that started the run", in "no run of the admitted state". So `tgt(h_X) = F`, `h_X` is not eligible, and the post-admission gate term is `F` (absent another decision). The integration is refused.
4. `GATE(g)` is not answered in `D_n` ("answered only by a judgment in its revision run"). It is re-dispatched, and §7.5 again routes the decision into frame `X`, which repeats the loop.

Under the opposite reading ("admitted at or after `run(s)`" alone), `h_X` is consistent, but that reading contradicts the exclusion sentence written to override it. This is the f7419d5 B1 frame-versus-post-admission stall in a case its repair did not cover. It contradicts the new §5.5 invariant, and also 3540d98 N1's request to settle "an unchanged-tree frame".

**Held** (attempted and not violated):
- f7419d5's primary rebase trajectory: `h_X` is in `elig_{D_n[X']}` with `current = F`, and `REVALIDATE` is derived in the frame;
- its earlier-iteration qualified variant (entry open in the frame);
- an abandoned iteration's decision on a revision its lineage never integrated (not "for the obligation that integration produced");
- a single frame with one `UNQUALIFIED` decision (`T`, integrates);
- the 575dc78 two-lineage state after integration in either order (`P` until superseded by an eligible superseder);
- adverse frame decisions (veto whatever their frame);
- a superseder that is itself adverse (restrictive);
- monotonicity (`elig` is S0, `unq` an S0 constant, `current` positive in S2).

Further search would be implementation-like: how the inspector renders frame states, and which records a gate core renders across rebases.

**Family assessment.** This is the gate family's ninth finding:
- 3540d98 B3;
- e9e6e9f B2;
- a18b544 B2;
- 0b6c4fa B2;
- 27ef339 B3;
- 5c55d4b N3;
- 575dc78 B1;
- f7419d5 B1;
- now B1.

Since 27ef339 B3, a gate decision is made in one state (a frame) and takes effect in another (the admitted state). Each round has made one more consumer state-relative and left the rest:
- this round, eligibility;
- still global: supersession (in `base` and `stands⁻`);
- still positional: obligation identity and run membership.

Siblings (i)-(iv) share that one cause. This is a **non-local recurrence**, and the convergence owner's simplification trigger applies: repair by one state-relative definition at the S0 facts, not by another scope clause in a consumer.

**Options for the stakeholder (Phase C handoff §5).**
- **(a) One state-relative definition at the S0 facts. Recommended; definitional, adds no record, store or latch.**
  - For `GATE_DECISION` only, define `superseded_G(h)`: some superseder eligible in `G` names `h`, directly or through a chain. Read it in `base` and in `stands⁻` (for adverse gate decisions) as well as in `elig`, so a supersession takes effect exactly where its superseder is eligible.
  - Identify a run started by an integration by its enactment lineage, in frames and in the admitted state alike, and any other run by its starting position. Equivalently, match `GATE`, `ACCEPT` and `REVIEW(s, r)` by target triple plus run membership, never by identity hash (5c55d4b N3).
  - State that a frame record of an integrated lineage that left `cur(s)` unchanged is in the run current at that integration.
  - Cost: lifting an adverse gate decision becomes frame-relative, a departure from R9's reuse of the reviewed assessment rule (whose supersession stands on immutable facts). It must be listed in R9/R11 as a refinement.
  - It changes what two S0 predicates read for one record kind. Say so; this is mechanism-changing, though not mechanism-adding.
- **(b) Subtractive narrowing, which I do not recommend.**
  - Admission accepts `supersedes` on a `GATE_DECISION` only where superseder and superseded are eligible in exactly the same states (both admitted-frame, or both of one lineage), and the superseder clause in `elig` is deleted.
  - This removes (i) and (ii) with no new definition, but has a liveness cost. A candidate that stales an admitted decision's core and requires its gate can integrate only through the owner's adjudication, and an admitted `REJECT` whose lifting needs a candidate's records deadlocks that candidate until the owner acts.
  - It still needs the identity and run fixes of (a).
- **(c) Workplan-level subtraction (f7419d5 option (b)).** Withdraw frame gate decisions, and decide gates only in the admitted state on the integrated revision. This removes §7.5's gate clause, lineage eligibility and frame obligation identity. It changes the reviewed integration precondition ("required gates", workplan §7.8), so it must be surfaced as a semantic change.

**Required discriminators.** These run at the real Admission → Derivation (`valid`, discharge) → Dispatcher → inspector owners, with nothing seeded resolved:
- **(A)** The primary trajectory, for a D3 subject and for a D2 subject whose run is unchanged:
  - while `Z` is pending and after `Z` is abandoned, the admitted gate term stays `F`, the veto stands and `ADJUDICATE_DISAGREEMENT` stays derived;
  - in `D_n[Z]` and after `Z` integrates, `T`.
  - An implementation in which the frame superseder ends the admitted veto must fail.
- **(B)** Sibling (i):
  - while `Z` is pending, the admitted gate stays `P` and an unrelated lineage requiring `g` integrates at `P` where policy permits;
  - after `Z` integrates, `T`;
  - if `Z` is abandoned, `P` (never `F`, never `T`).
- **(C)** The common variant: a candidate stales `h_a`'s core and its author re-decides in that frame. The admitted gate term is unchanged until the candidate integrates.
- **(D)** For a D1/D2 `AUTHOR` item, the frame `ACCEPT`, `GATE` and `REVIEW(s, r)` obligations have envelope identities computable before integration that match the admitted obligations after it. Then §31.6 (C) passes through Admission step 3.
- **(E)** Sibling (iv): the frame gate term equals the post-admission term, and the candidate integrates on its frame decision alone.

## 2. Non-blocking findings

- **N1 — How an admitted-frame record is evaluated inside a frame derivation (pre-existing; bears on the new invariant).**
  - §4.1 evaluates a `content` entry "in the record's frame", and §8.3 step 6 "in that record's frame … (the admitted state, or `D_n[X]` for a record about `X`)". Read literally, an admitted-frame decision `h_a` eligible in `D_n[X]` is evaluated against the admitted tree, not `M_n(X)`.
  - Consequence: take a non-D1/D2 revert through a candidate to an earlier gated revision `r'`, where R10 reuses `h_a`. Then `current(h_a)` is `F` in the frame (admitted `cur(s) ≠ r'`) but `T` after integration. The frame gate term (and `ACC`) differs from the post-admission one in the restrictive direction, and the frame derives a needless `REVALIDATE`.
  - Under the other reading (frame records are evaluated against the frame's own tree), the two agree. State which tree an admitted-frame record's entries are evaluated against in `D_n[X]`.
- **N2 — Accumulating minimum members (liveness and human load; disclosure).** With the hygiene rule deleted and passing gate decisions exempt from `OBLIGATION_ANSWERED`, every item that requires the gate of an unchanged non-D1/D2 subject can add a permanent member of `gterm`'s minimum. Each goes stale independently with its own evidence core, and only its own author or the owner can retire it. This is restrictive, not unsafe. Add it to the §32.3 reopen triggers alongside fence frequency and human-attention volume.
- **N3 — Accounting and wording residue.**
  - The closure map row for §21 item 5 (§7.3-§7.6) still says frame gate decisions "are eligible only there until their lineage integrates", and cites the family only through 575dc78 B1.
  - §5.5's "for the obligation that integration produced" reads oddly for gates on subjects the integration did not change (the case B1 (iv) concerns).
  - The aid confers no authority.
- **N4 — Qualification gaps (DS-001).**
  - §31.6 (D) ("lifts no admitted qualification") passes an implementation that drops the admitted gate to `F` (B1 (i)).
  - No case supersedes an admitted adverse gate decision from a frame (B1 (ii)), and none decides an item-required gate on an unchanged D1/D2 subject (B1 (iv)).
  - (C) presupposes an obligation identity the text does not define (B1 (iii)).
  - 5c55d4b B2 discriminator (D) (an anchor move giving a D2 unit different bytes is a `VIOLATION`) and a case that isolates the region criterion from owned content are still absent (575dc78 N5, f7419d5 N4).
  - A §31 written to the current text is green with B1 present.
- **N5 — Stakeholder-level trade-offs, reported as such.** These are listed in closure map §5, and no governing requirement is violated by them:
  - the SD-17 partial reversal (red-then-green needs a bounded reproduction);
  - the SD-24 narrowing (only the decision's own author or the owner lifts a qualification; a later `UNQUALIFIED` decision by another holder does not);
  - the exact-identity cost.

  The author chose the f7419d5 repair direction under item 19's delegation. I would put B1's options to the stakeholder together with these.

## 3. Closure audit

Each workplan §21 item and clause was located in the Manual directly; the closure map was used only as an index, and its claims were checked. "Answered" means a substantive D3 answer exists; it is neither runtime evidence nor stakeholder acceptance.

The diff since f7419d5 touches:
- §0.3 (R11 and the history paragraph);
- §5.5 (`gterm`, `elig_G`, the Gate term paragraph);
- §6.6 (one comma), §7.5, §8.3 step 7, §10.4, §16.8;
- §30, §31.6, §32.2;
- closure-map rows 3 and 7 and one author-choice bullet.

I read the whole Manual (sections 0-33) at the candidate. Rows outside the diff were re-checked against that read, not re-attacked in depth.

| §21 | Independently located answer | Result |
|---|---|---|
| 1 | §§1.1-1.11 | Answered |
| 2 | §§1.7, 2.1-2.6 | Answered |
| 3 | §§3.1-3.6, 5.5, 6.8, 17.1 | **Supersession of a gate decision has two meanings, global in `base`/`stands⁻` and state-relative in `elig` (B1 (i), (ii))**; the rest answered |
| 4 | §§4.1-4.6, 6.3 | Answered (N1 concerns frame evaluation of admitted-frame records) |
| 5 | §§5-7, 17, 22.3 | `stale`, strata, single-valuedness and monotonicity hold (`elig` is S0; `gterm` is a `min` over an S0 set of positive S2 values). **The declared frame of gate decisions, frame obligation identity and run membership carry B1 (iii), (iv)** |
| 6 | §§8, 21-23 | Answered; step 3's "same target" for D1/D2 frame decisions is B1 (iii) |
| 7 | §10 | **`run(s)` has no frame value (B1 (iii)), and run membership excludes integrated lineages that left `s` unchanged (B1 (iv))**; the rest answered |
| 8 | §11, §13.2, §13.4 | Answered; the §11.5 step 3 trigger is consistent with the post-admission check except under B1 (iv) |
| 9 | §9 | Answered |
| 10 | §16 | **Channel C fails for B1 (ii)**; §16.8's entry rule is otherwise answered |
| 11 | §§17, 6.10 | Answered |
| 12 | §18 | Answered |
| 13 | §§19-20 | Answered |
| 14-16 | §§21-25 | Answered; runtime unexecuted |
| 17 | §26 (both transfer tables) | Answered |
| 18, 19 | §§27, 28 | Answered |
| 20 | §20 | Answered |
| 21 | §29.7 | Answered; the Channel C row rests on B1 (ii) |
| 22 | §30 | Present and updated; its gate sentence describes the B1 realization |
| 23 | §12, §1.2, §13.2 | Answered |
| 24 | §13 | Answered |
| 25 | §14 | Answered as design; no threshold accepted |
| 26 | §§15-16 | Answered |
| 27 | §29 | Present; see section 9 |

**Workplan §16.2, both tables.** The diff does not touch §26.4. I re-read §26.3-§26.4 against the workplan's Deferred rows (invariants 4, 9, 15, 17 and 26; the §5 sub-rules; §6, §7, §9-§12 detail and §18). Every one has a final disposition, and none is merely routed. None found unresolved.

**Material decisions versus delegated D4.** Parsers, the diff implementation, checkpoint encoding, limit values and the file-type table remain correctly `[delegated]`. Three architectural decisions are left contradictory or undefined:
- the state in which a gate supersession takes effect (B1 (i), (ii));
- the frame identity of a D1/D2 run-keyed obligation (B1 (iii));
- run membership for an integrated lineage that left the subject unchanged (B1 (iv)).

## 4. Refinements R1-R11

| # | Assessment |
|---|---|
| R1 | **Sound.** The text is unchanged except a comma in the `link⁻` parenthetical. `on⁺ ⇒ on⁻ ⇒ link⁻` holds by construction, and every stop rests on a bounded reproduction (the stated anchor invariant) |
| R2, R3 | Sound; unchanged. `elig` adds no support-graph edge beyond §5.6 item 2 |
| R4 | Sound within its crash model; unchanged |
| R5 | Sound; the line-wise alignment cost is disclosed |
| R6, R7, R8 | Sound; unchanged. R8's authority rule is not at fault in B1; the "same target" it relies on is (B1 (iii)) |
| R9 | **Sound in the admitted state; its veto is lifted across the frame boundary (B1 (ii)).** `stands⁻` ends on a supersession recorded in any frame, while the Manual now promises frame-relative supersession for gate decisions. Option (a) makes that promise true at the cost of a stated departure from the reviewed assessment rule for adverse gate decisions; this needs to be listed |
| R10 | Sound; unchanged (N1 notes that a reverting candidate's frame may not see the reuse) |
| R11 | **Sound as a term; unsound across the frame/admitted boundary (B1).** The minimum over eligible decisions is the right term, and the f7419d5 frame cases it targets now hold. But a qualification can be lowered to `F` by its own author's frame reassessment (B1 (i)). For D1/D2 frame decisions its lift relies on an undefined identity (B1 (iii)), and a frame decision on an unchanged D1/D2 subject never counts after integration (B1 (iv)). The narrowing of SD-24 is surfaced as an author choice; I would put it to the stakeholder with B1's options |

## 5. Previous findings and Phase B closures

"Closed" means I re-derived that the present text excludes the named trajectory; it is not runtime evidence.

**Depth.** I re-derived every f7419d5 item in full. For the gate-family items of every record, I re-read the cited findings and tested them against the new text:
- 3540d98 B3 and N1;
- e2154ac N2;
- e9e6e9f B2, a18b544 B2;
- 0b6c4fa B2 and N2-N4;
- 27ef339 B3, N4 and N5;
- 5c55d4b N3;
- 575dc78 B1 and N4.

For all other items I took the f7419d5 record's dispositions as hypotheses. Their cited text is unchanged since f7419d5 (the diff is listed in section 3), and I spot-checked them during my whole-Manual read; I did not re-read the full prose of those records (section 10).

### F7419D5 (same family)

| ID | Disposition and basis |
|---|---|
| B1 primary | **Closed**: in `D_n[X']`, the earlier rebase decision is in `elig` with `current = F`, so `REVALIDATE` is derived before integration, and the frame term equals the post-admission term for subjects `X'` changes |
| B1 (i) literal `E` | Closed: the frame case is stated in the formula |
| B1 (ii) earlier iterations | Closed for subjects the lineage changes. **Open for item-required gates on unchanged D1/D2 subjects: B1 (iv)** |
| B1 (iii) rebase currency versus frame scoping | Closed: §7.5's "neither eligible nor current … in another frame" is deleted |
| B1 (iv) identity across integration | **Partly closed**: equality of identities is asserted, but the positional `run(s)` makes it uncomputable. **B1 (iii)** |
| B1 (v) hygiene rule | Closed: deleted |
| B1 (vi) cross-frame supersession | Closed in its permissive form for passing decisions (`elig` scopes superseders). **The restrictive inverse is B1 (i), and the adverse-decision analogue is B1 (ii)** |
| B1 (vii) abandoned iteration | Closed: eligibility is "for the obligation that integration produced" |
| B1 qualified variant | Closed: the inspector entry is open in the frame |
| N1 | Closed (`gterm`, `elig`) |
| N2 | Closed for rows 3 and 7 and §31.6; residue in the item-5 row (N3) |
| N3 | Closed (§32.2 corrected, comma added) |
| N4 | **Partly closed**: B1's cases (A)-(F) added; gaps remain (N4) |
| N5 | Closed: a second holder may add a `QUALIFIED` decision in any frame |
| N6 | Surfaced; stakeholder decision pending (N5) |

### 575DC78, 5C55D4B (same family)

| Review | ID | Disposition |
|---|---|---|
| 575DC78 | B1 | Closed after integration in either order: `P` until an eligible superseder. Before integration, a frame superseder lowers it to `F` (B1 (i)) |
| 575DC78 | N1-N3, N6, N7 | Closed |
| 575DC78 | N4 | **Regressed**: the lineage value for `run(s)` in frames was deleted. **B1 (iii)** |
| 575DC78 | N5 | Partly closed (N4) |
| 5C55D4B | B1, B2 | Closed (unchanged text) |
| 5C55D4B | N1, N2, N4-N7 | Closed |
| 5C55D4B | N3 | Its "who must declare a frame" and "standing across frames" bullets are closed for passing decisions. Its obligation-identity bullet is **open as B1 (iii)**, and its unchanged-subject case is **B1 (iv)** |

### 27EF339, 0B6C4FA (same family)

| Review | ID | Disposition |
|---|---|---|
| 27EF339 | B1, B2 | Closed |
| 27EF339 | B3 | Closed for its trajectory; the family recurs as **B1** |
| 27EF339 | N1 | Closed as disclosure |
| 27EF339 | N2 | Surfaced; stakeholder decision pending |
| 27EF339 | N3, N6, N7 | Closed |
| 27EF339 | N4 | Closed (author or owner, whichever answers first) |
| 27EF339 | N5 | Closed: a second holder can qualify |
| 0B6C4FA | B1 | Closed |
| 0B6C4FA | B2 | Closed for its trajectory; family **B1** |
| 0B6C4FA | N1 | Surfaced; stakeholder confirmation pending |
| 0B6C4FA | N2 | Partly closed: the subject-triple challenge and `REJECT` remain unevadable by others. The author can still supersede around an open blocking challenge, and now from a frame (B1 (i)) |
| 0B6C4FA | N3 | Closed |
| 0B6C4FA | N4 | Closed: the entry is keyed on eligibility |
| 0B6C4FA | N5-N7 | Closed |

### A18B544, E9E6E9F, E2154AC (same family)

| Review | ID | Disposition |
|---|---|---|
| A18B544 | B1 | Closed |
| A18B544 | B2 | Closed for its trajectories; family **B1** |
| A18B544 | N1-N5 | Closed (N1 by R10) |
| A18B544 | N6 | Superseded |
| E9E6E9F | B1, N1-N5 | Closed or superseded, as before |
| E9E6E9F | B2 | Closed for its trajectory; family **B1** |
| E2154AC | B1, N1, N3-N5 | Closed |
| E2154AC | N2 | (a) and (c) closed; (b) closed in the admitted state and in frames by the §16.8 eligibility rule |

### 3540D98 (different family)

| ID | Disposition |
|---|---|
| B1 | Closed: exact identity, unchanged |
| B2 | Closed: complete external-input set, unchanged |
| B3 | Closed in the admitted state and in frames for passing decisions. **Reopened across the frame boundary as B1 (ii)**: an admitted gate closes unqualified when a holder's adverse decision is lifted by a never-integrated frame |
| B4 | Closed: equal regions, unchanged |
| N1 | **Open for the frame representation of the prospective run and the unchanged-tree frame**: B1 (iii), (iv). Closed for acceptances on revisions the frame changes |
| N2-N4 | Held as disclosures |

### 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363

| Review | IDs | Disposition |
|---|---|---|
| 798B2B4 | B1-B4, N1-N8 | Closed. The revision run is unchanged; its frame representation is B1 (iii), (iv) |
| 71CF9B3 | B1, B2, N1-N8 | Closed |
| 86AB683 | B1, N1-N7 | Closed |
| 1FFBBF0 | B1, B2, N1-N7 | Closed |
| 53669A5 | B1-B3, N2-N9 | Closed |
| 53669A5 | N1 | The SD-17 partial reversal is surfaced, not decided (N5) |
| D837363 | B1-B4, N1-N8 | Closed |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

| Review | IDs | Disposition |
|---|---|---|
| CC005DB | B1-B3, N1-N8 | Closed |
| C6DA678 | B1-B3, N1-N12 | Closed |
| B595F2C | B1-B4, N1-N8 | Closed |
| 6FF4ED1 | B1-B4, N1-N12 | Closed (`on⁺ ⇒ on⁻ ⇒ link⁻` with a frozen context; the rest unchanged) |

### Phase B §3 closures and N1-N4

| Closure or limit | Present reconstruction |
|---|---|
| EF8445A/552AC01 N2: strata, completeness polarity | **Re-tested in both directions.** Take an alternate tree differing only outside a recorded narrow basis, with a differing old-content run and a yielding present-content run, under a judgment that becomes `P`, blocked, revoked or loss-withheld. **Held:** (2) and (4) read `link⁻`, an S0 existential over admitted observations, so losing the judgment only removes `bound` and narrows (1) and (3). Restrictive direction: a stop is withdrawn only by a newly admitted anchor whose narrower basis links an old differing run. That has a cause, and it is fail-closed when the basis is wrong (disclosed, §32.2) |
| Fail-closed support cycles; corrupt prefixes | Held: the R2 clamp and `INTEGRITY_HALT` are unchanged, and `elig` adds no edge |
| Y1/Y2, X1-X3, candidate-own latch, floor and class | Held (unchanged) |
| Contrary-run retention, nondeterminism, U1/U2/W1/W2 | Held (unchanged) |
| Absorbed relaxation; adversity versus currency, challenge, loss; salvage; independence; start latch; effective structure, quarantine, tenure | Held. Gate decisions across frames: **B1** |
| Phase B N1 | Disclosed (§32.2, §32.4) |
| Phase B N3 | Held (§31.3) |
| Phase B N4 | Held as reopen triggers |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | f7419d5 primary: rebase after the gate is decided; the head change makes the core realization stale | Held: `REVALIDATE` derived in `D_n[X']`; frame and post-admission terms equal |
| 2 | Earlier iteration with a current `QUALIFIED` decision, no provisional continuation | Held: entry open in the frame |
| 3 | Single frame, one `UNQUALIFIED` decision, subject changed | Held: `T`, integrates |
| 4 | 575dc78 two-lineage state, both integration orders | Held after integration: `P` |
| 5 | Admitted `REJECT` by `H_X`, `ACCEPT` by `H_Y`; `H_X` reassesses to `ACCEPT` in candidate `Z` (subject unchanged); `Z` pending, then abandoned | **Violation, permissive (B1 (ii))**: admitted gate `T`, adjudication obligation gone |
| 6 | Admitted `QUALIFIED` decision superseded by its author from candidate `Z` | **Violation, restrictive (B1 (i))**: admitted `P` → `F`; unrelated lineages stall |
| 7 | Candidate stales an admitted decision's core; the author re-decides in the frame | **Violation, restrictive (B1 (i) common variant)** |
| 8 | Envelope identity of frame `ACCEPT`/`GATE`/`REVIEW(s, r)` for a D1/D2 `AUTHOR` item | **Undefined (B1 (iii))** |
| 9 | Author supersedes an integrated `QUALIFIED` D1/D2 frame decision (§31.6 (C)) | **Depends on the undefined identity (B1 (iii))** |
| 10 | Item-required gate on a D1/D2 subject the frame leaves unchanged | **Stall and re-dispatch loop (B1 (iv))** |
| 11 | Non-D1/D2 revert through a candidate to an earlier gated revision | Restrictive mismatch under one reading (N1) |
| 12 | Abandoned iteration's decision; identical bytes arrive later (non-D1/D2 and D1/D2) | Held |
| 13 | Abandoned candidate's passing and adverse frame decisions | Held (never eligible; the adverse one vetoes) |
| 14 | Adverse superseder recorded in a frame (author `ACCEPT` → `REJECT`) | Held, restrictive (veto whatever its frame) |
| 15 | Second holder adds `QUALIFIED`/`UNQUALIFIED` decisions in several frames over time | Held for safety; accumulation cost (N2) |
| 16 | `gterm` monotonicity and stratification (`elig` S0, `unq` S0, `current` positive) | Held |
| 17 | D1/D2 decisions of earlier runs after a revert | Held: excluded by the run clause |
| 18 | `link⁻` with `INCOMPLETE` or partially recorded anchors | Held (adverse only) |
| 19 | Phase B N2 polarity; structure, `ignore`, analyzer or system-version change with the tree fixed | Held (unchanged) |
| 20 | Free seed, backend, external-set and unobserved-read variants | Held (unchanged) |
| 21 | D1/D2 revision by absorption, adoption, revert; acceptance before the revising record | Held (unchanged; `OBLIGATION_REVIEW_OPEN`, run `tgt`) |
| 22 | Support cycle via absorbed `about` or a completeness edge; corrupt authenticated prefix | Held |
| 23 | Publication crash windows, fence chains, ABA | Text unchanged for many rounds; not re-attacked in depth |

## 7. Minimum architecture and capability transfer

**What changed this round.** No primitive, component, persistent surface or record tier is added. The round:
- replaced `E(g)` by `elig_G`, adding the frame case and the eligible-superseder clause;
- deleted the within-frame hygiene rule (subtractive);
- exempted passing gate decisions from `OBLIGATION_ANSWERED`;
- re-keyed frame obligations to the integrated identity.

The deletion is a genuine simplification. The eligible-superseder clause is mechanism that is incomplete without the S0 changes of option (a); the integrated-identity key reintroduced an uncomputable parameter. §30's accounting is current apart from B1's consequences for R9 and R11.

**Capability transfer.**
- The §26.4 tables are unchanged and resolve every Deferred §16.2 row.
- Core prompt mode, frozen profiles and the containment root are preserved, and Core never imports SSDS. PC-001 holds.
- PEM was activated, because this is mature-machinery replacement:
  - `PROJECT-ENGINEERING-MEMORY.md` is byte-identical on `main` and at the candidate (`15617971…`);
  - the validator, run from the checkout (whose `source/` and PEM equal the candidate's), reports "PEM schema 1 valid: 5 families, 0 notices";
  - `tests.test_protocol_63_engineering_memory` passes at the snapshot (28 tests).
- HAS dispositions:
  - PC-001 applicable, held (§26.4, §28, §31.8);
  - FF-001 applicable to genesis, held (§19.9);
  - SP-002 applicable to self-reference, held (§8.7, §21.2);
  - SP-001 an evidence-only analogy, held (§5.8);
  - DS-001 applicable to §31 (N4: green fixtures coexist with B1).
- Absence of a 7.x memory entry proves nothing.

`orchestrator/docs/architecture.md` (blob `39e6de72…`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## 8. Qualification-design adequacy

§31.1 states that no executable SSDS evidence exists at G1 and that every runtime group is `UNEXECUTED`. Nothing is claimed as executed.

Green fixtures could coexist with B1 (DS-001):
- **(D)** accepts an admitted gate of `F` after a frame supersession;
- no case lifts an admitted adverse gate decision from a frame;
- no case covers an item-required gate on an unchanged D1/D2 subject;
- **(C)** assumes an identity the text does not define.

The other new cases, (A), (B), (E) and (F), discriminate the f7419d5 defects they target. The 5c55d4b B2 (D) and region-isolation gaps persist (N4). The §6 cases are unchanged and include the unbounded-failure and width-independence cases that earlier rounds required.

The diagnostic model was not run (optional). Its file is unchanged since the Phase B candidate, and it models none of these clauses.

## 9. Doctrine-realization map and O1

§29 is unchanged this round. I re-checked §29.2-§29.5 against:
- the 7.2.1 D3 entrypoint and its expanded entry contract;
- the role-contract rows;
- every scientific-checks duty.

The §29.7 Channel C row ("refusal of an unqualified accept with known missing evidence") and the human-gate realization rest on **B1 (ii)**:
- an admitted gate closes unqualified on a judgment about content that never integrated;
- the still-live disagreement disappears from every view.

The workflow owner's "Orchestration may represent pending/accepted/rejected state" is then unmet for that state. §29.6's E3 list is adequate.

O1 (§0.5) states the realized record, readers, routine questions and realized-record architecture. It visibly marks the within-deliverable surfaces, and "Beyond the requested deliverable: **None**". I found no unmarked inspectability-driven product requirement and no mark wrongly classed as within the deliverable. The inspector's gate entries are within-deliverable surfaces whose coverage B1 (ii) defeats; that is a D3 defect, not an O1 marking defect. Technical Review accepts no marked item; a marked item beyond the deliverable binds only after stakeholder or task acceptance.

## 10. What I verified and how; what I could not verify

**Verified at the exact candidate** (`git archive` snapshot under `$TMPDIR/ssds80-manual-review-b46c250/`):
- **Reading.**
  - The whole Manual, sections 0-33; §21-§25 were read for change and consistency, not re-attacked.
  - The diff from f7419d5 (Manual and closure map).
  - The closure map rows touched and its §5.
  - Workplan §6.9, §7.4, §7.8, §9.4 and §21.
  - The stakeholder record (item 19, SD-20 to SD-24); Phase C handoff §5.
  - The f7419d5 record in full; the gate-family findings listed in section 5.
  - Governing owners as listed.
- **Blobs.** The Manual, closure-map, workplan, Phase B and Architecture 1.6.0 blobs match the handoff.
- **Tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the snapshot: 4 tests, OK.
- **Whitespace.** `git diff --check f7419d5… b46c250…`: clean (exit 0).
- **Additions.** `git diff --stat fad3ee4… b46c250…`: 45 files, 13,978 insertions, 1 deletion. All are under `qualification/ssds80/`, plus the Manual and two lines in `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. Since f7419d5, only the Manual and the closure map changed, besides the f7419d5 handoff and record.
- **Frozen surfaces.** `git diff --quiet fad3ee4… b46c250… -- orchestrator/docs/architecture.md source dist`: exit 0.
- **PEM.** As in section 7.

**Not verified:**
- any SSDS runtime behavior (none exists);
- tracer fidelity and G3 costs;
- the full prose of Review records other than those named, beyond the dispositions in section 5;
- deep re-derivation of findings whose cited text is unchanged since f7419d5;
- publication and fencing, which were not re-attacked;
- how the inspector renders frame states, and which records a gate core renders across rebases, both implementation-like;
- the diagnostic model, which was not run.

Family search in B1 stopped at characterization, as method step 6a allows.

## 11. Scientific-checks answers

This task reviews D3 authority for software that mediates scientific evidence.

1. **Material findings.**
   - Blocker B1 (gate-qualification family) and non-blocking N1-N5, all D3 architecture or coordination findings.
   - I have no D1/D2 scientific or numerical findings and no out-of-scope scientific findings.
   - I launched no agents. The tools I ran (section 10) produced no finding beyond those stated.
2. **Realized results.** I produced, ran and reviewed no realized scientific results and prepared no gate evidence, so no null envelope is owed. The unit tests, the PEM validator and the PEM tests are software checks on documents and memory schema, not realized results.
3. **Variants.** Yes, design and interpretation variants only. This was not result selection over data, and no data, held-out set, earlier history or delegated search was involved.
   - **Repair options:** three for B1, (a)-(c).
   - **Clause readings, kept as findings rather than resolved:** ten readings in five sets of two:
     - supersession in `base`: global or state-relative;
     - supersession in `stands⁻`: global or state-relative;
     - frame obligation identity: positional hash or membership matching;
     - run membership of an integrated lineage that left the subject unchanged: included or excluded;
     - evaluation of admitted-frame records in a frame: against the admitted tree or against the frame's tree.
   - **Selection criterion:** preserve the owner-required property with the least added mechanism (convergence owner). The B1 choice is the stakeholder's.
4. **Tension search.** Not triggered. I relied on no accepted D1/D2 authority for a consequential judgment; no scientific or numerical formulation is accepted for the SSDS product. The judgments rest on:
   - accepted SSDP 7.2.1 protocol owners (D3, workflow, evidence, convergence, abstraction);
   - the proposed workplan and Manual;
   - the stakeholder record and Phase C handoff.

Gaps: none in these answers.

## 12. Common-mode note

I share the Manual author's model family (Claude). The authoring session launched me from a handoff it wrote. The following are shared dependencies:
- the corpus;
- the inherited workplan framing;
- the prior Review records (eighteen of the nineteen Manual Reviews same-family);
- the toolchain.

The 3540d98 and Phase B reviewers were of another family (GPT).

B1 traces to the previous same-family record's option (a). That option named the state-relative supersession and the integrated identity, but not the S0 facts (`superseded`, `stands⁻`, positional `run(s)`, run membership) they must change. The repair implemented the suggestion in `elig` and prose only.

The gate family has now recurred nine times, the last four through repairs of same-family suggestions. Repair directions from candidate 13 onward were chosen by the author under the stakeholder's delegation (item 19), not by the stakeholder. I would therefore put the following to the stakeholder, together with a different-family confirmation of the invariant stated in §5.5, before any further same-family round:
- B1's options;
- the SD-24 narrowing;
- the SD-17 partial reversal.

## 13. D4 statement

SSDS 8 D4 is **not authorized**. This NO-PASS accepts no architecture, no proposed default and no product scope. G1 also requires a later independent PASS on a repaired candidate and explicit stakeholder acceptance. G2 requires a reviewed shadow D3->D4 workplan and explicit stakeholder authorization.
