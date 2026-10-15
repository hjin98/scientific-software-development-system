# SSDS 8 Architecture Manual — Independent D3 Review, candidate f7419d5

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: f7419d5d05114bf670788d2bc6b53499827bcd82
    SCOPE: whole proposed Manual as the durable D3 owner: (a) §21/§16.2 closure, (b) fidelity and
           refinements R1-R11, (c) out-of-matrix adequacy, (d) inheritance and capability transfer,
           (e) qualification design, (f) doctrine-realization map, (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: f891383629b4a077aae890c660e799c4d85ed05a (checked)
    CLOSURE MAP BLOB: ad73903113d83ab36d259eff9f7cfd3e505910d1 (review aid only; checked)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; Phase B candidate e23f14208be869e6a78cfd7b312e447254ee1851
           (blob 610f373b97fb8152d2a5742e17fa172e12204756, checked); blob at this candidate
           91bde236465178f20c7348280e036d2884dfc216 (checked)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS, HYPOTHESIS ONLY: E23F142 Phase B PASS; Manual NO-PASS records 6FF4ED1, B595F2C,
           C6DA678, CC005DB, D837363, 53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98, E2154AC,
           E9E6E9F, A18B544, 0B6C4FA, 27EF339, 5C55D4B, 575DC78
    REVIEW METHOD: D3 role entered at the governing public source; whole-Manual read at the exact
           candidate (git archive snapshot); deductive counterexamples in both polarities; family-level
           search after recurrence (convergence owner; handoff method step 6a), attacking hardest the
           575dc78-round repairs (the gate term `gate(g)` over `E(g)`, §7.5 lineage eligibility, the
           lineage-keyed frame obligation identity, the retained hygiene rule) and the repairs of that
           round's non-blocking findings; prior-finding regression; required structural checks;
           no implementation or runtime qualification
    REVIEWER: Claude model family (the same family as the Manual's author); a fresh-context
           sub-agent launched by the authoring session from the named handoff; no authoring
           conversation received
    MUTATION BOUNDARY: this record only; no commit or push

Governing SSDP version for this task: 7.2.1.

All Manual section references are to the exact candidate. The checkout HEAD was the later handoff commit `d27f66a`, which differs from the candidate only by the handoff file. Governing owners were read at `aaeaf8b…`:

- `source/roles/software-design/SKILL.md` and its expanded `dist/skills/software-design/SKILL.md` (entry contract, Independent Review and Challenge, scientific checks);
- `architecture-and-design.md` (read first, as the entrypoint directs);
- `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review readiness and independent review sufficiency", "Review strategy after recurrence");
- the human-gate and Channel C paragraphs of `workflow-and-workplans.md`, and the assessment-disagreement paragraph of `evidence-evolution-and-dependencies.md`.

The other concern owners were not loaded: no decision below turned on them.

## SERIOUS CHALLENGE

**None against accepted SSDP 7.2.1 or the frozen Architecture 1.6.0 / Level 0 Core.** The blocker is a defect of the proposed D3 concretization. The workplan and the Manual are proposed architecture, so a contradiction inside the Manual is not a challenge to accepted authority.

Owner text applied:

- D3 owner, "D3 boundary and feasibility": "A D3 candidate is admissible only when it satisfies every applicable D1/D2 invariant and directly governed security, reliability, compatibility, resource, performance/scaling, deployment and external-interface constraint."
- D3 owner, "D3 formal-contract discipline": "When an architectural concept carries normative meaning, define it before dependent invariants use it: component/state ownership, … lifecycle states and transitions, …"
- D3 role entrypoint: "D3 contradictory/ambiguous/inadequate/unrealizable -> SERIOUS CHALLENGE to D3". Applied to proposed D3, it yields a blocker.
- Workflow owner, human gates: "Orchestration may represent pending/accepted/rejected state but cannot self-approve it." Channel C: "The gate does not close unqualified when missing realized records could plausibly change its judgment."
- Convergence owner, "Review strategy after recurrence": "A clean local repair that genuinely closes the cause remains sufficient; recurrence does not automatically force redesign."

## Verdict

**NO-PASS.** One D3 blocker survives, stated at family level as method step 6a requires.

- **B1 — gate-qualification family (frame gate decisions), eighth round; entered through the 575dc78 B1 repair (lineage eligibility of frame decisions) and the 575dc78 N4 repair (lineage-keyed frame obligation identity).**
  - The `gate(g)` minimum closes 575dc78 B1 in the post-integration state: with two integrated frames, the term is `P` until the `QUALIFIED` decision is itself superseded, in either integration order.
  - But a gate decision now answers, becomes eligible, is superseded and is revalidated in different states. §5.5's `E(g)` names only admitted-frame decisions and decisions of an integrated lineage. §7.5 makes a passing frame decision "neither eligible nor current … in another frame" until its lineage integrates. Integration's discharge is checked in the post-admission state (§7.6, §8.3 step 7), while the Dispatcher submits only when discharge "would hold on the candidate" (§11.5 step 3).
  - **Concrete result.** After a routine rebase or iteration, an earlier frame's gate decision first enters `E(g)` in the post-admission state of the very integration it then refuses. No actual state ever contains it in `E(g)`, so neither `REVALIDATE` (§5.5, §10.2) nor the §16.8 entry is derived. The lineage cannot integrate unless the decision's author or the owner acts with nothing asking them to.
  - Siblings: the `E` formula excludes a frame's own decisions in that frame; lineage-keyed frame obligations differ from run-keyed admitted ones; the retained hygiene rule still presupposes one decision; and a frame-scoped superseder removes an admitted qualification at once (a Channel C violation).

The 575dc78-round repairs otherwise close what they target:
- 575dc78 N1, N2 and N3 are closed;
- N4 is closed for computability, and its repair is a B1 entry point;
- N5, N6 and N7 are partly closed.

**The matching family (§6) and the D1-D3 change-rule family have no blocker this round.** This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blockers by earliest owner

### B1 — Frame gate decisions are answered, eligible, superseded and revalidated in different states, so routine rebases and iterations stall integration with no derived action, and a frame-scoped supersession closes an admitted qualification

**Earliest owner.** Manual §5.5 (`gate(g)`, `E(g)`, "Gate term"), read with:
- §7.5 (declared frame; "Answered and eligible are read in the frame of the obligation"; lineage-keyed frame obligations);
- §7.6 ("Its discharge predicate is evaluated in the post-admission state"; "Rebase … A frame-`X` record counts for `X'`");
- §8.3 steps 2, 3 and 7 (target existence, supersession on the same target, the hygiene rule, post-admission discharge);
- §10.2 (`REVALIDATE` trigger and holder; `run(s)` parameter; revision-run membership of earlier iterations and rebases);
- §10.3 (answering), §10.4 (the gate term of discharge), §11.5 step 3 (integration request), §16.8 ("Qualified gates"), §31.6.

These are workplan §21 items 3, 5 (declared frame per kind), 7 (discharge) and 10 (gate templates meeting Channel C). It is a D3 defect and asks for no D1/D2 change.

**Owner and contract text.**
- §5.5: "`E(g)`: every authenticated passing GATE_DECISION for g that is not superseded and is eligible in this state: an admitted-frame decision, or a frame decision of a transformation whose enactment lineage has integrated (§7.5)"; "A non-current decision among them lowers the term and derives `REVALIDATE` for it"; "Invariant: in every state the gate term is a function of every unsuperseded passing decision eligible in that state"; "a qualification lifts only when its own decision is superseded, by its author's reassessment or the owner's adjudication".
- §7.5: "a passing frame-`X` decision answers only the frame's obligation, and until a transformation of `X`'s enactment lineage (`X`, a later iteration or a rebase) integrates, it is neither eligible (§5.5 `E`) nor current in the admitted state or in another frame"; "In a frame, obligations carry the transformation's enactment lineage in place of the `run(s)` parameter".
- §7.6 (rebase): "A frame-`X` record counts for `X'` only if every one of its entries holds, in its role, in `D_n[X']`".
- §11.5 step 3: "Once the claimed obligation's discharge predicate would hold on the candidate — clean conformance, current review judgments, required gates — the Dispatcher submits an integration request".
- §10.2: `REVALIDATE(x)`: "an admitted judgment no longer current that a current obligation depends on"; "`ACCEPT(s)`, `GATE(g)` and `REVIEW(s, r)` carry `run(s)` among their parameters".
- §8.3 step 3: "only by a record of the same kind on the same target … For a `GATE_DECISION`, the target is its gate obligation". Step 7: "within one frame, a passing `GATE_DECISION` on a gate obligation that already has an unsuperseded passing decision there … is admitted only as a supersession of that decision".
- §16.8: "A `QUALIFIED` gate `ACCEPT` in `E(g)` keeps an entry open".
- §31.6: "for a D1/D2 subject, an earlier iteration's or rebase's frame decision is eligible after the lineage integrates".
- §0.4 A8: "a material finding survives to its owner; escalation is keyed on existence, never currency"; K1: "a result is admitted only if everything it relied on is current, or it is revalidated"; §9.1: an overtaken request "is revalidated … never rejected outright".

**Primary trajectory (rebase; under the most favourable reading, in which a frame's own decisions are eligible in that frame).**
1. Setup:
   - an `AUTHOR` item (authority D2) carries the default human gate `g` on `NATIVE` D2 subject `s`;
   - its candidate `X = (B, C, ∅)` changes `s` from `r0` to `r'`;
   - evidence specification `e` evidences `s`. Its designated-runner realization `ρ` on `C` read `s` and a D4 file `f` (unit `u_f`, context role, unchanged by `X`).
2. In `D_n[X]`:
   - conformance is `CLEAN`, `REVIEW(X)` passes, and the `AUTHOR` result's `revision_assessments` entry for `(s, r')` counts in the prospective run;
   - holder `H` records `h_X`: `GATE_DECISION ACCEPT`, `ADEQUATE`, `UNQUALIFIED`, frame `id(X)`;
   - its §4.3 basis is `content (s, r')` (output role) plus `record` on every core record, including `ρ`.
3. Before integration, another item's admission changes `f`. The head moved, so `X` is rebased cleanly to `X' = (B', C', ∅)`, the same lineage (§11.5 step 3). The Dispatcher reruns `e` on `C'` (`ρ'`, passing), and the review is re-requested because its basis named `ρ`.
4. In `D_n[X']`:
   - `h_X` is "neither eligible nor current … in another frame" (§7.5), so `GATE(g)` there is not answered by it (§7.5: "answers only the frame's obligation");
   - `H2` (or `H`) records `h_X'` on the `X'` core: `ACCEPT`, `UNQUALIFIED`;
   - the hygiene rule does not apply, because frame `X'` holds no other passing decision. Nothing asks for `h_X` to be named in `supersedes`, and `H2` could not supersede it anyway (§8.3 step 3);
   - `E(g)` in the frame is `{h_X'}`, so the gate term is `T`, and the Dispatcher submits the integration request.
5. Admission evaluates discharge in the post-admission state (§7.6, §8.3 step 7):
   - the lineage has now integrated, so `h_X` is eligible: it is a frame decision of a rebase of the lineage whose integration starts `run(s)`, so it is in the run (§10.2);
   - its `record` entry on `ρ` fails, because `ρ`'s unit entry for `u_f` no longer re-resolves in the admitted tree, so `current(h_X) = F`;
   - `gate(g) = min(F, T) = F`. The `AUTHOR` obligation's discharge is `F`, and the request is refused.
6. No state that exists ever contains `h_X` in `E(g)`:
   - in the pre-integration admitted state, `h_X` is not eligible and `(s, σ, r')` has no gate obligation;
   - in `D_n[X']`, `h_X ∉ E(g)`;
   - the post-admission state is never admitted.

   So `REVALIDATE(h_X)` is never derived, and `h_X` has no §16.8 entry. The frame still shows the integration as ready, and every retry or later iteration meets the same `h_X`.
7. The lineage integrates only if `H` or the owner happens to supersede `h_X`, which no obligation, brief or view asks for. Otherwise the item must be abandoned and re-planned as new work, discarding its reviews.

   This contradicts:
   - §5.5's promise that a non-current member "derives `REVALIDATE`";
   - §9.1 and K1 (rejection with no revalidation route);
   - A8 for the qualified variant below.

**The other readings do not escape:**
- **Literal §5.5 formula.** Own-frame decisions are excluded in the frame, and an admitted-frame decision on changed content is refused (§31.6). So the frame gate term is `F` for every gated change, and the Dispatcher never submits. If it instead computes the post-admission hypothetical, it sees `F` from `h_X`, and again nothing is derived.
- **Identity-based answering (§10.3).** The frame obligations of `X` and `X'` share one identity, because §7.5 keys both by the lineage. By §10.3 the obligation is "answered by the first admitted judgment … bound to it", here `h_X`, and for D1/D2 `h_X` is in the prospective run. Then `GATE(g)` is never dispatched in `X'`, and `E(g)` in `X'` is empty. The gate term is `F` before any staleness at all.
- **Qualified variant.** `h_X` is current but `QUALIFIED`, and policy does not permit provisional continuation for the item's kind:
  - the frame view of `X'` shows `T`, the post-admission value is `P`, discharge is `OPEN`, and the request is refused;
  - `h_X` has no §16.8 entry, because it is in `E(g)` of no existing state.

  `H`'s recorded material limitation therefore blocks integration and is surfaced nowhere: escalation is keyed on eligibility, not existence. This resurfaces e2154ac N2(b) and 0b6c4fa N4 in the frame configuration.

The iteration path behaves the same way: a review `NO_PASS` within the item's scope starts the next iteration mechanically (§13.7), and a rebase that conflicts routes to one (§11.5). Both are ordinary.

**Siblings (family search; one cause: frame gate decisions take effect in states other than the one their eligibility, answering, identity and supersession are defined for).**
- **(i) `E` in a frame.** §5.5's formula names no case for the evaluated frame's own decisions; only §7.5 implies them. An implementer who follows §0.1 ("Formulas are normative") gets a frame gate term of `F` for every gated change.
- **(ii) Earlier iterations and rebases.** This is the primary trajectory. Eligibility flips at the integrating admission, so the frame view and Admission's post-admission check disagree.
- **(iii) Rebase currency against frame scoping.** §7.6 says a frame-`X` record "counts for `X'`" when its entries hold, while §7.5 says it is "neither eligible nor current … in another frame". This is the 575dc78 B1 sibling (iii), still open before integration. Under per-frame answering every rebase of a gated candidate needs a fresh human decision; under identity-based answering it stalls.
- **(iv) Obligation identity across integration (575dc78 N4 repair).** For a `NATIVE` D1/D2 subject the frame obligation is lineage-keyed, but the admitted obligation is `run(s)`-keyed (§10.2). Several rules key on "the gate obligation":
  - `E`'s "for g";
  - §8.3 step 3's "same target" for supersession;
  - §8.3 step 2's existence check;
  - the `same` test of §5.5.

  After integration, the author's or owner's superseder of a frame decision targets the run-keyed obligation, which is not `h`'s target, so step 3 rejects it. The alternative is to target the lineage-keyed obligation by recording in the integrated transformation's frame, which nothing states. Literally, a `QUALIFIED` D1/D2 frame decision can then never be lifted within its run, contrary to §5.5 and SD-24.
- **(v) Hygiene rule presupposes uniqueness.** Step 7's "a supersession of that decision" is singular. Once two lineages integrate (575dc78 B1), the admitted frame holds two unsuperseded passing decisions. If the rule requires superseding every existing decision, `H_X`'s own reassessment of `h_q` is refused, because `H_X` cannot supersede `H_Y`'s decision. The lift that §5.5 promises then needs the owner.
- **(vi) Permissive: supersession is global, eligibility is frame-scoped.**
  - Start from the 575dc78 two-lineage state: `E(g) = {h_u (H_Y, UNQUALIFIED), h_q (H_X, QUALIFIED)}`, gate `P`.
  - Candidate `Z`'s item requires `g`, and `Z` supplies the realized record whose absence `h_q` named. `H_X` records `h_q'` in frame `Z`: `UNQUALIFIED`, superseding `h_q`.
  - `superseded(h_q)` is an S0 fact, so `h_q` leaves `E(g)` in every state at once. `h_q'` is not eligible until `Z` integrates. The admitted gate becomes `T` through `h_u`.
  - If `Z` is abandoned, the admitted gate stays `T`, while the record that `H_X` judged could change the decision never integrated.

  This violates Channel C. The Manual's invariant holds literally (the decision was superseded), but the supersession was a judgment about other content.
- **(vii) Abandoned iteration, non-D1/D2.** An earlier iteration's decision on a revision that its lineage never integrated becomes eligible once the lineage integrates elsewhere, with no run restriction. When identical bytes later arrive (by absorption or another lineage), it counts:
  - permissively when current and `UNQUALIFIED`;
  - restrictively (`F`, or `P` liftable only by its author) otherwise.

  This contradicts §31.6: "a frame gate decision of an abandoned candidate never becomes current or standing … even when identical bytes arrive by absorption".
- **Held:**
  - the 575dc78 B1 trajectory and its reverse order after integration (`P` until `H_X`'s supersession);
  - a vetoed member (`F`, routed to `ADJUDICATE_DISAGREEMENT`, never `REVALIDATE`);
  - D1/D2 decisions of earlier runs (excluded from `E` by the run clause, so they do not hold the term at `F`);
  - revoked, stale or loss-withheld admitted-frame members (`REVALIDATE` or `REQUALIFY` to the author or the owner);
  - adverse frame decisions (veto whatever their frame);
  - a single frame with one decision and no rebase, under the §7.5 reading.

Further search (which records a gate core renders across rebases, inspector rendering of frame states) would be implementation-like.

**Surfacing.** Nothing discloses these trajectories:
- §31.6's new case covers only "eligible after the lineage integrates";
- closure-map row 5 says decisions "are eligible only there until their lineage integrates";
- §30 calls the realization the minimum over eligible decisions "with a within-frame supersession rule kept as hygiene".

**Family assessment.** This is the gate family's eighth finding:
- 3540d98 B3;
- e9e6e9f B2;
- a18b544 B2;
- 0b6c4fa B2;
- 27ef339 B3 (gates required before integration but decidable only after it, a stall);
- 5c55d4b N3;
- 575dc78 B1;
- now B1.

Since 27ef339 B3, gate decisions have been made in one state (the candidate frame) and must take effect in another (the admitted state after integration). Each round has fixed one consumer's state and left the others: standing, eligibility, answering, identity, supersession, `REVALIDATE` and the inspector. The 575dc78 repair correctly removed the uniqueness premise from the term, but not from its consumers. This is a **non-local recurrence**, and the convergence owner's simplification trigger applies: repair by one definition, not by another scope rule.

**Options for the stakeholder (Phase C handoff §5).**
- **(a) One prospective definition. Recommended; definitional, adds no record, state or latch.** In a frame `D_n[X]`, every gate rule reads the set that `X`'s integration would make eligible: the admitted state's eligible decisions plus every frame decision of `X`'s enactment lineage (`X`, its earlier iterations and rebases). This is the §10.2 prospective-run construction. Then:
  - frame obligations take the identity the integrated obligation will have, so matching is by gate and subject triple (and, for D1/D2, the run that `X`'s integration starts), never by a frame-only hash;
  - a supersession of a gate decision takes effect in a state only where its superseder is eligible;
  - the hygiene rule is deleted, which is subtractive: the term does not need it, and its singular "that decision" is now false;
  - the frame check, Admission's post-admission check, `REVALIDATE` and the §16.8 entry then read one set;
  - restrictive cost: a stale earlier-iteration decision must be revalidated, in the frame, before integration (the cost the 575dc78 record already accepted for option (a)).
- **(b) Subtractive, needs a contract decision.** Withdraw frame gate decisions and remove human gates from the integration precondition (workplan §7.8 "required gates"). A gate is then decided only in the admitted state, on the integrated revision, and the revision supports nothing (invalid, dependents not ready) until its gate passes. This removes §7.5's gate clause, lineage eligibility and frame obligation identity. It changes the reviewed flow, because ungated D1/D2 revisions would land on the integration ref, so it must be surfaced as a semantic change.
- **(c) Narrowing.** A frame gate decision is eligible only in its own frame and, after integration, only if its own transformation integrated. There is no lineage carry. A later frame's gate core renders the lineage's earlier gate decisions and their qualifying records as findings, so Channel C is met by display. Restrictive cost: a human gate decision after every rebase or iteration. It also needs the supersession scoping of (a).

Whichever is chosen, state the invariant once in §5.5 so that later repairs can be checked against it: **for every frame `X`, every gate predicate evaluated in `D_n[X]` equals its value in the state `X`'s integration would produce, and every decision that can affect the gate term in some state is reachable by `REVALIDATE` and the §16.8 entry in a state that precedes that effect.**

**Required discriminators.** These run at the real Admission → Derivation (`valid`, discharge) → Dispatcher → inspector owners, with nothing seeded resolved:
- **(A)** The primary rebase trajectory, for a D2 subject and for a D3 subject. Before integration is attempted, either `h_X` is in the frame's eligible set with `REVALIDATE(h_X)` derived, or it is excluded in both the frame and the post-admission state. The frame gate term equals Admission's post-admission gate term. An implementation in which they differ must fail.
- **(B)** The iteration variant with a current `QUALIFIED` earlier decision, under a policy without provisional continuation. The qualification has an open inspector entry before integration is attempted, and no integration request is refused for a gate input absent from every view.
- **(C)** A `QUALIFIED` D1/D2 frame decision, integrated, then superseded by its author's `UNQUALIFIED` reassessment through its inspector entry: the gate term becomes `T`. An implementation that rejects the reassessment as a different target must fail.
- **(D)** The 575dc78 two-lineage state (`P`), then `H_X` supersedes `h_q` from candidate frame `Z`, which is later abandoned: the admitted gate term never becomes `T` through `h_u`.
- **(E)** A single frame, a single `UNQUALIFIED` decision, no rebase: the frame gate term is `T` and the Dispatcher submits. An implementation that literally applies the current `E` formula must fail.
- **(F)** Non-D1/D2: an earlier iteration's decision on a revision its lineage never integrated never counts when identical bytes arrive later, matching §31.6's abandoned-candidate case.

## 2. Non-blocking findings

- **N1 — Symbol collisions (entered through the 575dc78 B1 repair).**
  - S1 already defines `gate(y) = cont(y) if relaxer(y); T otherwise` (§5.3, read by `in_force`), and S2 now defines `gate(g)` for human gates (§5.5, §10.4).
  - `E` also names the expected head (`E_n`, §8.3 step 9, §22.1) and the relation set of §2.4.
  - The argument types differ, so this is not a material ambiguity. Rename one of each (for example `gterm(g)` and `elig(g)`).
- **N2 — Accounting residue of the withdrawn premise.**
  - Closure-map row 3 (item 3) still says the cap is realized "through one standing decision per gate obligation".
  - Row 7 still says "through the standing decision's own qualification … one supersession-only Admission rule".
  - §31.6 still says "never becomes current or standing".
  - The aid confers no authority.
- **N3 — 575dc78 N6 residue and an editorial slip.**
  - §32.2's exact-identity bullet still says "An unbounded basis matches adversely only an identical tree", which understates `link⁻`. §6.6 is corrected.
  - The new `link⁻` parenthetical lacks a comma ("of `conf(a⁻)` `INCOMPLETE` ones"). Its meaning is clear: a partially recorded basis only links more, so the effect is adverse only.
- **N4 — Qualification gaps (DS-001).**
  - §31.6 has none of B1's cases: a rebase or iteration with a stale or qualified earlier decision, post-integration supersession of a D1/D2 frame decision, cross-frame supersession, the literal frame `E`, and the abandoned iteration.
  - 5c55d4b B2 discriminator (D) (an anchor move giving a D2 unit different bytes is a `VIOLATION`) and a case that isolates the region criterion from owned content are still absent (575dc78 N5, partly closed).
  - A §31 written to the current text is green with B1 present.
- **N5 — Frame-dependent second-holder qualification (stakeholder-level trade-off, not a blocker).**
  - Within one frame, a second holder's `QUALIFIED` decision is refused unless it is the owner's supersession (hygiene rule). In another frame, the same decision is admitted and caps after integration.
  - Whether a second holder can add a qualification therefore depends on where they decided, despite §5.5's "no order of admission or integration between holders or candidate frames decides". It only ever restricts, and the holder keeps the `REJECT` and challenge routes.
  - With SD-24's narrowing (a later `UNQUALIFIED` decision by another holder does not lift a qualification, closure map §5), put it to the stakeholder. Repair option (a) removes it.
- **N6 — Stakeholder-level trade-offs, reported as such.** These are listed in closure map §5, and no governing requirement is violated by them:
  - the SD-17 partial reversal (red-then-green needs a bounded reproduction);
  - the SD-24 narrowing (only the decision's own author or the owner lifts a qualification);
  - the exact-identity cost.

## 3. Closure audit

Each workplan §21 item and clause was located in the Manual directly; the closure map was used only as an index, and its claims were checked. "Answered" means a substantive D3 answer exists; it is neither runtime evidence nor stakeholder acceptance.

The diff since 575dc78 touches §0.3 (R11 and the history paragraph), §5.5, §6.6 (the `link⁻` range and one bullet), §7.5, §8.3 step 7, §10.4, §16.8, §30, §31.6, §32.2, closure-map row 5 and the author-choice list. I read the whole Manual (sections 0-33) at the candidate. Rows outside the diff were re-checked against that read, not re-attacked in depth.

| §21 | Independently located answer | Result |
|---|---|---|
| 1 | §§1.1-1.11 | Answered; the line-wise alignment residual is now disclosed (§32.2) |
| 2 | §§1.7, 2.1-2.6 | Answered |
| 3 | §§3.1-3.6, 5.5, 6.8, 17.1 | **The gate decision's effect states are inconsistent (B1)**; the rest answered |
| 4 | §§4.1-4.6, 6.3 | Answered |
| 5 | §§5-7, 17, 22.3 | `stale`, strata, single-valuedness and monotonicity hold (`E` and `unq` are S0; `gate` is a `min` over an S0 set of S2 values, so it stays monotone). **The declared frame per kind for gate decisions, frame obligation identity and rebase currency carry B1** |
| 6 | §§8, 21-23 | Answered; the step 7 hygiene rule is B1 (v) |
| 7 | §10 | **Discharge of gated task obligations differs between the frame and the post-admission state (B1)** |
| 8 | §11, §13.2, §13.4 | Answered; the §11.5 step 3 trigger is B1 |
| 9 | §9 | Answered |
| 10 | §16 | **The §16.8 qualified-gate entry is keyed on `E(g)` of actual states (B1)**; the rest answered |
| 11 | §§17, 6.10 | Answered |
| 12 | §18 | Answered |
| 13 | §§19-20 | Answered |
| 14-16 | §§21-25 | Answered; runtime unexecuted |
| 17 | §26 (both transfer tables) | Answered |
| 18, 19 | §§27, 28 | Answered |
| 20 | §20 | Answered |
| 21 | §29.7 | Answered; the Channel C row rests on B1 (vi) |
| 22 | §30 | Present and updated; its gate sentence describes the B1 realization |
| 23 | §12, §1.2, §13.2 | Answered |
| 24 | §13 | Answered |
| 25 | §14 | Answered as design; no threshold accepted |
| 26 | §§15-16 | Answered |
| 27 | §29 | Present; see section 9 |

**Workplan §16.2, both tables.** The diff does not touch §26.4. I re-read §26.3-§26.4 against the workplan's Deferred rows (invariants 4, 9, 15, 17 and 26; the §5 sub-rules; §6, §7, §9-§12 detail and §18). Every one has a final disposition, and none is merely routed. None found unresolved.

**Material decisions versus delegated D4.** Parsers, the diff implementation, checkpoint encoding, limit values and the file-type table remain correctly `[delegated]`. One architectural decision is left contradictory: in which state a frame gate decision answers, is eligible, is superseded and is revalidated (B1).

## 4. Refinements R1-R11

| # | Assessment |
|---|---|
| R1 | **Sound.** The text is unchanged except the `link⁻` range, where "a partially recorded basis only links more" is correct, since `on⁻` over fewer recorded terms holds more often and is used adversely only. `on⁺ ⇒ on⁻ ⇒ link⁻` holds by construction, and every stop rests on a bounded reproduction (the stated anchor invariant) |
| R2, R3 | Sound; unchanged. `E(g)` adds no support-graph edge beyond §5.6 item 2 |
| R4 | Sound within its crash model; unchanged |
| R5 | Sound; the line-wise alignment cost is disclosed |
| R6, R7, R8 | Sound; unchanged. R8 is engaged by B1 (iv) only through the gate obligation's identity, not through its authority rule |
| R9 | Sound. The adverse frame scoping is now explicit (§7.5). The `same` test for `GATE_DECISION` keys on "the same gate obligation", which inherits B1 (iv)'s identity split for D1/D2 across runs; for D1/D2, a new run is intended to be a new target |
| R10 | Sound; unchanged |
| R11 | **Sound in the admitted state; unsound across the frame-integration boundary (B1).** The minimum is the right term, and 575dc78 B1 is closed after integration. But its stated property, "a human's bounded, qualified decision stays visibly provisional", fails for frame decisions before integration (invisible), after integration for D1/D2 (not liftable under the literal identity rule), and under cross-frame supersession (closed unqualified). It also narrows SD-24; this is surfaced as an author choice that I would put to the stakeholder with B1's options |

## 5. Previous findings and Phase B closures

"Closed" means I re-derived that the present text excludes the named trajectory; it is not runtime evidence.

**Depth.** I re-derived every 575dc78 item in full. For the gate-family items of every record (3540d98 B3, e2154ac N2, e9e6e9f B2, a18b544 B2, 0b6c4fa B2, N2-N4, 27ef339 B3, N4-N5, 5c55d4b N3), I re-read the cited findings and tested them against the new term. For the other items, I took the 575dc78 record's dispositions as hypotheses. Their cited text is unchanged since that candidate (the diff is listed in section 3), and I spot-checked them in my whole-Manual read. I did not re-read the full prose of those records (section 10).

### 575DC78 (same family)

| ID | Disposition and basis |
|---|---|
| B1 | **Closed for its trajectory and sibling (i) after integration**: with `E(g) = {h_u, h_q}`, `gate(g) = min(T, P) = P` in either integration order, until `h_q` is superseded by `H_X` or the owner. Sibling (ii) is closed after integration (§31.6), but its pre-integration side is **B1 (ii)** here. Sibling (iii) (rebase currency against frame scoping) is **still open before integration**, as B1 (iii) |
| N1 | Closed: the undefined qualifier is deleted. Editorial residue in N3 |
| N2 | Closed: §7.5 scopes the frame rule to passing decisions, and §31.6 adds the abandoned candidate's `REJECT` |
| N3 | Closed as disclosure (§32.2) |
| N4 | **Closed for computability** (lineage in place of `run(s)`). The repair splits frame and admitted obligation identities: **B1 (iv)** |
| N5 | **Partly closed**: two-frame integration in both orders and D1/D2 earlier-iteration eligibility are added. 5c55d4b B2 (D), an isolating region case and B1's cases are absent (N4) |
| N6 | **Partly closed**: §6.6 is corrected, §32.2 is not (N3) |
| N7 | **Partly closed**: row 5 and the author-choice bullet are updated, rows 3 and 7 are not (N2) |

### 5C55D4B (same family)

| ID | Disposition |
|---|---|
| B1 | Closed (unchanged text: every stop needs a bounded reproduction, which anchors `link⁻`) |
| B2 | Closed (content-based regions, unchanged) |
| N1, N2, N4, N5, N7 | Closed |
| N3 | Closed in its restrictive direction; its successors were 575dc78 B1 and now **B1** |
| N6 | Closed (27ef339 B2 (C)/(D), 27ef339 B3 (B)/(C) and the unbounded case are in §31.2 and §31.6) |

### 27EF339, 0B6C4FA (same family)

| Review | ID | Disposition |
|---|---|---|
| 27EF339 | B1, B2 | Closed |
| 27EF339 | B3 | Closed for its trajectory (frame-declared gate decisions integrate). The family recurs as **B1**, again as an integration stall, now through iterations and rebases |
| 27EF339 | N1 | Closed as disclosure |
| 27EF339 | N2 | Surfaced; stakeholder decision pending (N6) |
| 27EF339 | N3, N6, N7 | Closed |
| 27EF339 | N4 | Closed for the holder ("author or the owner, whichever answers first"). For D1/D2 frame decisions after integration, the superseder's target is **B1 (iv)** |
| 27EF339 | N5 | Surfaced as an author choice; the frame-dependence of the second holder's qualification is N5 here |
| 0B6C4FA | B1 | Closed |
| 0B6C4FA | B2 | Closed for its trajectory; family **B1** |
| 0B6C4FA | N1 | Surfaced; stakeholder confirmation pending |
| 0B6C4FA | N2 | As in 27ef339 N5: the subject-triple challenge and `REJECT` routes are not evadable |
| 0B6C4FA | N3 | Closed for admitted-state members; **B1** for members that enter `E` only at integration |
| 0B6C4FA | N4 | Closed for the admitted state (entry kept while in `E(g)`). It **resurfaces as B1's qualified variant**, because no actual state holds the frame decision in `E(g)` before integration |
| 0B6C4FA | N5-N7 | Closed |

### A18B544, E9E6E9F, E2154AC (same family)

| Review | ID | Disposition |
|---|---|---|
| A18B544 | B1 | Closed |
| A18B544 | B2 | Closed for trajectories (a) and (b); family **B1** |
| A18B544 | N1-N5 | Closed (N1 by R10's reuse across tenures) |
| A18B544 | N6 | Superseded |
| E9E6E9F | B1, N1-N5 | Closed or superseded, as before |
| E9E6E9F | B2 | Closed for its trajectory; family **B1** |
| E2154AC | B1, N1, N3-N5 | Closed |
| E2154AC | N2 | (a) closed by the minimum (no latest-wins); (c) closed; (b) closed for the admitted state, **resurfaces in B1** for frame decisions |

### 3540D98 (different family)

| ID | Disposition |
|---|---|
| B1 | Closed: exact identity, unchanged |
| B2 | Closed: complete external-input set, unchanged |
| B3 | Closed in the admitted state, including several integrated frames. **Reopened across the frame boundary as B1 (vi)**: an admitted qualification can be closed by a frame-scoped supersession |
| B4 | Closed: equal regions, unchanged |
| N1 | Closed for acceptances. Obligation identity across integration is **B1 (iv)** |
| N2-N4 | Held as disclosures |

### 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363

| Review | IDs | Disposition |
|---|---|---|
| 798B2B4 | B1-B4, N1-N8 | Closed. The revision run is unchanged, and `E`'s run clause keeps earlier runs' decisions from holding the term at `F` |
| 71CF9B3 | B1, B2, N1-N8 | Closed |
| 86AB683 | B1, N1-N7 | Closed |
| 1FFBBF0 | B1, B2, N1-N7 | Closed |
| 53669A5 | B1-B3, N2-N9 | Closed |
| 53669A5 | N1 | The SD-17 partial reversal is surfaced, not decided (N6) |
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
| EF8445A/552AC01 N2: strata, completeness polarity | **Re-tested in both directions.** Take an alternate tree differing only outside a recorded narrow basis, with a differing old-content run and a yielding present-content run, under a judgment that becomes `P`, blocked, revoked or loss-withheld. **Held:** (2) and (4) read `link⁻`, an S0 existential over admitted observations, so losing the judgment only removes `bound` and narrows (1) and (3). Restrictive direction: a stop is withdrawn only by a newly admitted anchor whose narrower basis links an old differing run. That has a cause, and it is fail-closed when the judgment is wrong (disclosed, §32.2) |
| Fail-closed support cycles; corrupt prefixes | Held: the R2 clamp and `INTEGRITY_HALT` are unchanged, and `E` adds no edge |
| Y1/Y2, X1-X3, candidate-own latch, floor and class | Held (unchanged) |
| Contrary-run retention, nondeterminism, U1/U2/W1/W2 | Held (unchanged) |
| Absorbed relaxation; adversity versus currency, challenge, loss; salvage; independence; start latch; effective structure, quarantine, tenure | Held. Gate frames: **B1** |
| Phase B N1 | Disclosed (§32.2, §32.4) |
| Phase B N3 | Held (§31.3) |
| Phase B N4 | Held as reopen triggers |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | 575dc78 B1: two lineages change a non-D1/D2 gated subject identically; `UNQUALIFIED` then `QUALIFIED`; both integrate in either order | Held: `P` until `h_q` is superseded |
| 2 | `gate(g)` monotonicity and stratification (`E` and `unq` S0; `current` S2, positive) | Held |
| 3 | Empty `E(g)`; vetoed member; revoked, stale or loss-withheld admitted member | Held (`F`; `GATE`, `ADJUDICATE_DISAGREEMENT`, `REVALIDATE` or `REQUALIFY` routed) |
| 4 | D1/D2 decisions of earlier runs after a revert | Held: excluded by `E`'s run clause, so no permanent `F` |
| 5 | Non-D1/D2 tenure restart with a stale old decision in `E` | Held, restrictive and routed (`REVALIDATE` to the author or the owner) |
| 6 | Rebase after the gate is decided; the head change makes the core realization stale | **Violation (B1, primary)** |
| 7 | Iteration after a `NO_PASS`, with a stale or `QUALIFIED` earlier decision | **Violation (B1 (ii), qualified variant)** |
| 8 | Literal `E` in a single frame | **Contradiction (B1 (i))** |
| 9 | Identity-keyed answering of lineage-keyed frame obligations | **Stall (B1)** |
| 10 | Post-integration supersession of a `QUALIFIED` D1/D2 frame decision by its author | **Contradiction (B1 (iv))** |
| 11 | Author reassessment after two integrations, under the singular hygiene rule | **Contradiction (B1 (v))** |
| 12 | Cross-frame supersession, then candidate abandoned | **Violation, permissive (B1 (vi))** |
| 13 | Earlier iteration on an un-integrated revision; identical bytes arrive later (non-D1/D2 and D1/D2) | **Contradiction for non-D1/D2 (B1 (vii))**; held for D1/D2 (run clause) |
| 14 | Abandoned candidate's passing and adverse frame decisions | Held (never eligible; the adverse one vetoes as stated) |
| 15 | `link⁻` with `INCOMPLETE` or partially recorded anchors | Held (adverse only) |
| 16 | Phase B N2 polarity; structure, `ignore`, analyzer or system-version change with the tree fixed | Held (unchanged) |
| 17 | Free seed, backend, external-set and unobserved-read variants | Held (unchanged) |
| 18 | D4 edit on a line shared with a D1-D3 symbol | Fail-closed `VIOLATION`, now disclosed |
| 19 | Support cycle via absorbed `about` or a completeness edge; corrupt authenticated prefix | Held |
| 20 | Publication crash windows, fence chains, ABA | Text unchanged for many rounds; not re-attacked in depth |

## 7. Minimum architecture and capability transfer

**What changed this round.** No primitive, component, persistent surface or record tier is added. The round:
- replaced "the one standing decision" by `E(g)`, an S0 set, and a `min`;
- extended frame eligibility to the enactment lineage;
- keyed frame obligations by lineage;
- retained the supersession rule as "hygiene".

The last three are B1's entry points. The retained hygiene rule is now mechanism that the term does not need and whose wording contradicts multi-decision states, so repair option (a) deletes it. §30's accounting is current apart from B1's consequence for R11.

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
  - SP-002 applicable to self-reference, held (§8.7, §21.2);
  - SP-001 an evidence-only analogy, held (§5.8);
  - DS-001 applicable to §31 (N4: green fixtures coexist with B1).
- Absence of a 7.x memory entry proves nothing.

`orchestrator/docs/architecture.md` (blob `39e6de72…`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## 8. Qualification-design adequacy

§31.1 states that no executable SSDS evidence exists at G1 and that every runtime group is `UNEXECUTED`. Nothing is claimed as executed.

Green fixtures could coexist with B1 (DS-001):
- **Gate frames.** §31.6 integrates two frames' decisions, and states earlier-iteration eligibility after integration. It never compares the frame gate term with the post-admission term. It has no rebase or iteration with a stale or qualified earlier decision, no post-integration supersession of a D1/D2 frame decision, and no cross-frame supersession.
- **Regions.** 5c55d4b B2 (D) and an isolating region case are absent (N4).

The §6 cases are unchanged and include the unbounded-failure and width-independence cases that earlier rounds required.

The diagnostic model was not run (optional). Its file is unchanged since the Phase B candidate, and it models none of these clauses.

## 9. Doctrine-realization map and O1

§29 is unchanged this round. I re-checked §29.2-§29.5 against:
- the 7.2.1 D3 entrypoint and its expanded entry contract;
- the role-contract rows;
- every scientific-checks duty.

The §29.7 Channel C row ("refusal of an unqualified accept with known missing evidence") and the human-gate realization rest on **B1**:
- B1 (vi) closes an admitted gate unqualified through a judgment about other content;
- B1's qualified variant keeps a recorded material limitation out of every view while it blocks work. The workflow owner's "Orchestration may represent pending/accepted/rejected state" is then unmet for that state.

§29.6's E3 list is adequate.

O1 (§0.5) states the realized record, readers, routine questions and realized-record architecture. It visibly marks the within-deliverable surfaces, and "Beyond the requested deliverable: **None**". I found no unmarked inspectability-driven product requirement and no mark wrongly classed as within the deliverable. The inspector's qualified-gate entry is a within-deliverable surface whose coverage B1 defeats; that is a D3 defect, not an O1 marking defect. Technical Review accepts no marked item; a marked item beyond the deliverable binds only after stakeholder or task acceptance.

## 10. What I verified and how; what I could not verify

**Verified at the exact candidate** (`git archive` snapshot under `$TMPDIR/ssds80-manual-review-f7419d5/`):
- **Reading.**
  - The whole Manual, sections 0-33; §21-§25 were read for change and consistency, not re-attacked.
  - The diff from 575dc78 (Manual and closure map).
  - The closure map in full.
  - Workplan §6.9, §7.4 and §7.8 (the reviewed frame, discharge and integration contracts) and §21's structure.
  - The stakeholder record (instructions 1-19 and SD-1 to SD-24).
  - Phase C handoff §5.
  - The 575dc78 record in full; 27ef339 B3; the gate-related non-blocking findings of 0b6c4fa, 27ef339 and e2154ac.
  - Governing owners as listed.
- **Blobs.** The Manual, closure-map, workplan and Phase B blobs match the handoff.
- **Tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the snapshot: 4 tests, OK.
- **Whitespace.** `git diff --check 575dc78… f7419d5…`: clean (exit 0).
- **Additions.** `git diff --stat fad3ee4… f7419d5…`: 43 files, 13,336 insertions, 1 deletion. All are under `qualification/ssds80/`, plus the Manual and two lines in `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. Since 575dc78, only the Manual and the closure map changed, besides the 575dc78 handoff and record.
- **Frozen surfaces.** `git diff --quiet fad3ee4… f7419d5… -- orchestrator/docs/architecture.md source dist`: exit 0.
- **PEM.** As in section 7. The validator needs a Git repository, so at the snapshot it reports `REVIEW_REQUIRED` for route realization; from the checkout it is valid.

**Not verified:**
- any SSDS runtime behavior (none exists);
- tracer fidelity and G3 costs;
- the full prose of Review records other than those named, beyond the dispositions in section 5;
- deep re-derivation of findings whose cited text is unchanged since 575dc78;
- publication and fencing, which were not re-attacked;
- how a gate core renders across rebases, and whether an inspector renders frame states, both implementation-like;
- the diagnostic model, which was not run.

Family search in B1 stopped at characterization, as method step 6a allows.

## 11. Scientific-checks answers

This task reviews D3 authority for software that mediates scientific evidence.

1. **Material findings.**
   - Blocker B1 and non-blocking N1-N6, all D3 architecture or coordination findings.
   - I have no D1/D2 scientific or numerical findings and no out-of-scope scientific findings.
   - I launched no agents. The tools I ran (section 10) produced no finding beyond those stated.
2. **Realized results.** I produced, ran and reviewed no realized scientific results and prepared no gate evidence, so no null envelope is owed. The unit tests, the PEM validator and the PEM tests are software checks on documents and memory schema, not realized results.
3. **Variants.** Yes, design and interpretation variants only. This was not result selection over data, and no data, held-out set, earlier history or delegated search was involved.
   - **Repair options:** three for B1, (a)-(c).
   - **Clause readings, kept as findings rather than resolved:** eleven readings in five sets:
     - three readings of the frame gate set (the literal §5.5 formula, the §7.5 implication, the prospective construction);
     - two readings of answering (per frame, by obligation identity);
     - two readings of the supersession target (obligation hash, gate and triple);
     - two readings of the hygiene rule's "that decision" (every existing decision, any one);
     - two readings of the Dispatcher's "would hold on the candidate" (frame, post-admission hypothetical).
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
- the prior Review records (seventeen of the eighteen Manual Reviews same-family);
- the toolchain.

The 3540d98 and Phase B reviewers were of another family (GPT).

B1 traces to the previous same-family record's suggestions:
- its option (a) for B1 named eligibility "in the state" without saying how a frame's state relates to the post-integration state;
- its N4 offered the lineage as the frame value of `run(s)`.

Both repairs followed those suggestions and entered this defect. Repair directions from candidate 13 onward were chosen by the author under the stakeholder's delegation (item 19), not by the stakeholder. Because the gate family has now recurred eight times, I would put these to the stakeholder before any further same-family round:
- B1's options, in particular (b), which changes the reviewed integration precondition;
- the SD-24 narrowing;
- the SD-17 partial reversal.

A different-family confirmation, which the stakeholder reserves, could test the invariant stated under B1 directly.

## 13. D4 statement

SSDS 8 D4 is **not authorized**. This NO-PASS accepts no architecture, no proposed default and no product scope. G1 also requires a later independent PASS on a repaired candidate and explicit stakeholder acceptance. G2 requires a reviewed shadow D3->D4 workplan and explicit stakeholder authorization.
