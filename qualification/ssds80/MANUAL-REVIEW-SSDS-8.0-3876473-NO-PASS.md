# Independent D3 Review — SSDS 8 Architecture Manual, candidate 3876473

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          387647305b91a569493c73e180cf78f04b55c9e6
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g));
                        technical evidence for G1 only
    MANUAL blob:        8388f8c7adae0425c1edeccddbdf09c8c7c62964 (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   cebc17c6fa1af8c09c721a186ffb59cddd1cba12 (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family 3940dbc
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; delta-first attack of R15 as
                        restated over lines (latched value, continuations, adverse events, restoration,
                        per-term combination, P not latching), in both directions, against reviewed
                        workplan §7.4, SD-24, the workflow and concurrency owners and the Manual's own
                        §8.3, §10.2-§10.5, §11.5, §13.7, §23.6, §31.3-§31.4 and §32.3; independent
                        reading and probing of the lifecycle oracle (lc_oracle) for events the shared
                        event table omits; drift classes applied to every statement of R15; family-level
                        recheck of earlier families against the delta; the diagnostic model run with
                        every family and mutation, in parallel; the structural checks of handoff §3 step 9
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched
                        by the authoring session; did not author the candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-3876473/snap`. The later commit adding the handoff (`73c52311`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. SSDP 7.2.1, the reviewed workplan and the stakeholder's recorded decisions (SD-1 to SD-35, record items 19 and 31) can be realized together. The blocker below lies in R15, an author choice under record item 31 that closure map §5 (line 298) lists for the stakeholder to confirm or reverse. It is routed against the proposed D3 owner. This is the sixth consecutive round in the obligation-lifecycle family and the fourth in a row to enter through the previous same-family Review's recommended option, so its options go to the stakeholder, together with the question the 3940dbc record already raised: whether R15 should exist at all.

## Verdict

**NO-PASS.** One blocker, B1, in the obligation-lifecycle family (edabd81 N7, 82d618c B1, 095ce55 B1, c77447b B1, 3940dbc B1). The line rule closes the 3940dbc siblings it targeted: a refresh is no longer a withdrawal, provisional values no longer latch unqualified, a frame answer made stale by a rebase does not latch, and lines are computed by machinery rather than taken from the Dispatcher's references. What it does not define is the obligation's life after a lowering that stands, and what a line is for the evidence-dispute terms.

- **B1 (a)**: a latched obligation lowered by an event that stands (an upheld challenge or veto, an owner's adverse supersession, a rollback, an unrequalifiable loss) "becomes ready", but nothing says how it is discharged again. Its value stays the minimum over the lines of `D_m`, the state where it was *first* discharged, and new work creates no line. So the re-dispatched implementer's integration is either refused for ever (stranded) or admitted without discharging (a duplicate output, re-dispatched until budget exhaustion). §31.4's "a rollback before re-cutover" and §32.3's "a deliberate repair is a new item" presuppose a re-discharge that §10.4 never states.
- **B1 (b)**: the restoring routes the rule names (a continuation, a requalification) are inadmissible exactly where R15 is meant to apply. A continuation of a review of `X` needs `X`'s output entries current, and a gate continuation needs the gated revision current; Admission step 6 refuses both once later content moved. So after any later edit, a lowering stands by default and falls into (a).
- **B1 (c)**: for judgment obligations (`REVIEW(X)`, `JOINT_INVARIANT(i, k)`, `SPEC_REVIEW(spec, r)`), "becomes ready" contradicts §10.3's "An answered obligation is never ready again". Their only fresh answers (a new review of an integrated result whose units have since moved) fail step 6. A conforming implementation has to choose between a stranded ready obligation and a lowered obligation with no route.
- **B1 (d)**: the line definition does not cover the dispute terms `undisputed` and `qual` (§5.5), whose inputs are failing assessments and their dispositions rather than passing records. Whether revoking an `IMMATERIALITY` disposition after the latch, or a new counting failure on the same unchanged content, lowers the item is undetermined. Under the reviewed §7.4 both do. The disclosed item-31 exemption covers only failures "on later content".

The diagnostic model is green on all six families and catches every one of the 42 mutations (lifecycle: 54,500 scenarios, I11 holds). Its lifecycle oracle reads the same event table as the rule. The table has no re-work-after-lowering event, no event on the gate or evidence lines, no disposition, and no override withdrawal. The oracle also short-circuits every provisional start before reading any event. So B1 is green by construction, and so is a second error the model and oracle share (N4).

## Blockers

### B1 — A latched obligation lowered by a standing event has no defined route back to discharge, and lines are undefined for the dispute terms

**Family:** obligation lifecycle after integration (82d618c B1, 095ce55 B1, c77447b B1, 3940dbc B1). It enters through 3940dbc option 1, whose text also says nothing of re-discharge after a standing lowering.

**Earliest owner:** Manual §10.4, "Enacted obligations latch a value" (lines 1319-1321), and the R15 row (line 100). They decide workplan §21 item 7 ("obligation rules …, readiness, three-valued discharge, provisional propagation and risk-override scope, iteration/attempt identity") and support items 6 (§8.3 steps 7-8) and 9 (§9.2 joint invariants).

**Status:** open, material, non-local. §8.3 steps 6-7, §10.3, §23.6, §31.4 and §32.3 each contribute.

**Exact rules at the candidate.**

- §10.4 (line 1321): "An enacted obligation **latches the value** `v_m` that the predicate above has in the state `D_m` where it is first discharged". "Once latched, the value is computed by machinery over the **lines** of what the predicate read at `D_m`". "A line is that record with its **continuations**, the passing records of its kind on its target by its author or the owner that supersede it, and requalifications of it". "An `∃` term takes the best line among the records satisfying it at `D_m`". "No current-state term is read".
- §10.4 (line 1321): "A lowered latched obligation is shown waiting while an `ADJUDICATE(c)`, `ADJUDICATE_DISAGREEMENT` or `REQUALIFY` of the event that lowered it is open; it becomes ready only when that route leaves the event standing against the line, and the line is restored when the route resolves the event."
- §10.3 (line 1293): "A ready obligation whose every answer Admission must refuse is a defect"; (line 1299) "An answered obligation is never ready again, so it is never dispatched again."
- §8.3 step 6 (line 1188): every basis entry of a submitted support-tier record "is satisfied, in its role, in that record's frame at the current admitted head", otherwise the record is "classified stale and routed to revalidation, not admitted"; §7.3 (line 1122): an output entry after the integrating admission has "ordinary currency in the admitted state"; §4.3 (line 570): a `REVIEW` carries "frame-role `content` on every unit of `Δ(X)` (before-image and output)"; a `GATE_DECISION` carries "`content` on the gated subject revision" (line 579).
- §8.3 step 7 (line 1189): "Each obligation whose discharge the request claims is undischarged at the current head …, and its discharge predicate (§10.4) holds after the request's own records".
- §23.6 (line 2227): "**Requalification** uses existing kinds only: a fresh acceptance, adjudication, assessment, realization, import or consultation after the boundary".
- §5.5 (lines 759-761): `ev(s, e) = (⋁ current(a)) ∧ undisputed(s, e)`; `undisputed(s, e) = ⋀_{a⁻ ∈ adverse(s, e)} (P ∨ disp(a⁻))`; `qual(s) = ⋀_{e named by a failing assessment a⁻ …} undisputed(s, e)`.
- §31.4 (line 2667): "after the latch, a `NO_PASS` upheld by the owner, a risk-overridden challenge later upheld, a rollback before re-cutover and a loss boundary each reopen the obligation".

**(a) A standing lowering has no defined re-discharge.**

1. Item `I` (`IMPLEMENT`) changes D4 subject `s` from `r0` to `r1` by transformation `X`. Review `R` by reviewer `V` passes, the gate decision `h1` is unqualified, and `X` is integrated at `m` and published. `IMPLEMENT(I)` latches `T` over the lines `{R, h1, s@r1, evidence}`.
2. A challenge `c` against `R` (say, `R` missed a contract violation) is upheld by an eligible adjudication. The line of `R` is `F`, so `IMPLEMENT(I)` is lowered to `OPEN`. While `ADJUDICATE(c)` is open it is shown waiting. Once that route "leaves the event standing", it "becomes ready". Its plan item is still covered, so the Dispatcher issues iteration `k+1` to `I`'s implementer.
3. The implementer produces `X2` (a new task and enactment, R12). `X2` is reviewed by `R2`, gated and integrated at `m2`, claiming `IMPLEMENT(I)`.
4. `IMPLEMENT(I)` is latched and was "first discharged" at `D_m`. Its value is the minimum over `D_m`'s lines. `R`'s line is still `F`: `c` stands, and `R2` is on target `X2`, so it is not a continuation of `R`. Step 7 must read either the code-block predicate or the latched value:
   - **Latched value:** every claim is refused. A ready obligation whose every answer Admission refuses is §10.3's defect (stranded).
   - **Code-block predicate:** `m2` is admitted, but discharge stays `F` afterwards, so the obligation is ready again. It is re-dispatched, and integrates again, until the iteration budget sends it to `COORDINATE`. Each integration is a real change to the tree with no effect on discharge: the concurrency owner's duplicate logical outputs.
   - **Re-latch at `m2`:** not stated, and contradicted by "first discharged".

Sibling triggers with the same end:

- an owner-upheld peer `NO_PASS` vetoing `X`, once `ADJUDICATE_DISAGREEMENT` closes leaving the veto standing;
- the owner's adverse supersession of `R` or `h1` (no route is open, so the obligation is ready at once);
- an upheld challenge against `s@r1`;
- a gate `REJECT` on `(s, σ, r1)` upheld by the owner;
- a rollback `MODE_TRANSITION`, after which "every line is `F`". A later re-cutover is new work whose records are not lines, yet §31.4 lists the rollback "before re-cutover", presupposing that re-cutover closes the `MIGRATE` item again.

**(b) The named restorations are inadmissible after later content changes, so lowerings stand by default.**

1. As (a) step 1. A later item `J` edits a unit `u ∈ Δ(X)`, and step 8 admits it (a judgment it makes non-current "is not a regression").
2. Challenge `c` against `R` is raised and upheld, or a loss boundary withholds `R`.
3. The rule names two restorations:
   - a continuation of `R` (its author's or the owner's passing review of `X`);
   - a requalification.

   Both are fresh support-tier records about `X`, carrying an output entry `(u, rev(u, C))` (§4.3). After `J`, `rev(u, T_n) ≠ rev(u, C)`, so step 6 refuses them as stale. §23.6's requalification kinds do not include a review at all. A gate continuation needs `content` on `s@r1`, which fails the same way once `s` has moved.
4. The only routes left are resolving the event itself (a counter-challenge or a dismissal). When those are not available, the lowering stands, and the obligation falls into (a).

This is the common case, not an edge: R15 exists for the world in which later items edit earlier items' outputs. §31.4's "a gate's author refreshing it, a reviewer's passing reassessment and a requalification reopen nothing" holds only while the integrated content is still current.

**(c) Lowered judgment obligations contradict §10.3.**

`REVIEW(X)`, `JOINT_INVARIANT(i, k)` and `SPEC_REVIEW(spec, r)` are judgment obligations, and they are answered (§10.3, R9). After a standing lowering:

- §10.4 makes them "ready". §10.3 says an answered obligation "is never ready again".
- If dispatched, a fresh review of the integrated result whose units have since moved fails step 6, or is refused as `OBLIGATION_ANSWERED` unless it is the author's or the owner's supersession (§8.3 step 7).

Concrete case: `JOINT_INVARIANT(i, k)` latched, then its review is revoked by an upheld challenge, after a later change `k'` touched `i`'s scope. The obligation is either ready with no admissible answer (a defect by §10.3), or not ready and with no route. Meanwhile the invariant violation the challenge found has no derived route at `k`'s integrated result. Any further protection depends on `JOINT_INVARIANT(i, k')` happening to examine it.

**(d) Lines are undefined for the dispute terms.**

1. `I` integrates while a failing assessment `a⁻` on `s`'s claim content counts. An R2-class `IMMATERIALITY` judgment `im` disposes of it, so `disp(a⁻)` holds, and `undisputed`, `ev` and `qual` are `T`. `I` latches `T`.
2. A challenge against `im` is upheld. `s` is unchanged.
3. The reviewed §7.4 gives `qual(s) = F`: `I` is `OPEN`.
4. Under the line rule, nothing settles which records are lines:
   - `im` is not "a judgment satisfying its judgment term", "an assessment", "a gate decision" or plainly "an evidence record behind its `ev` terms".
   - `a⁻`'s line has a failing latest record, for which "`T` otherwise" is meaningless.
   - `adverse(s, e)` is a current-state set, which "no current-state term is read" freezes at `D_m`.

   One conforming implementation keeps `I` unqualified `DISCHARGED` with an undisposed failure counting on the very content it produced. Another lowers it.

The same holds for a new counting failing assessment on the same, unchanged content after the latch, for example a discriminating re-run. The disclosed item-31 choice covers only evidence that "goes stale or fails on later content". Closure map line 298 says "an adverse event against an evidence record the predicate read (an upheld challenge, a loss) lowers the item", which suggests `im` is meant to be a line, but §10.4 does not make it one.

**Shared cause.** R15 now defines how a latched value is lowered and restored, but only as a closed state machine over a fixed state `D_m` whose transitions are events against records that existed there. It defines no transition for new work, which creates no line. It assumes that continuations and requalifications are always admissible, which step 6 denies once content moves. And it defines lines only for passing records, not for the failing-assessment and disposition terms the predicate also reads. This is again two places computing one thing (the handoff's drift classes): the lifecycle the rule states versus Admission's currency rule (b), §10.3's answered-obligation rule (c), and §5.5's dispute terms (d).

Discovery stops here. Further variants re-derive (a)-(d): a `SPEC_REVIEW` revoked after its specification moved; a qualified refresh lowering to `P` outside policy, which then has neither a ready route nor a waiting one (N3); a `DOCUMENT` item's review revoked.

**Controls that hold.**

- An author's or owner's passing refresh of a gate or review while content is current restores or keeps `T`.
- A qualified gate at integration does not latch, and lifting the qualification latches `T` at publication.
- A risk-overridden challenge on the produced triple keeps `P`, and withdrawing the override gives `F`.
- A frame-answered `JOINT_INVARIANT` review made stale by a clean rebase does not latch.
- A fenced or `OVERTAKEN` integration stays `OPEN`.
- Entry order and run changes do not reopen.
- An upheld challenge on one of two reviews satisfying the `∃` term does not lower.
- A veto of the target reaches the continuation.
- A loss with a continuity attestation holding the record does not lower.
- Lines no longer depend on the Dispatcher's references.

**Violated owner text.**

- **Architecture owner** (`aaeaf8b:source/shared/references/architecture-and-design.md`, line 96): "define it before dependent invariants use it: … lifecycle states and transitions". The transition from a standing lowering back to discharge is undefined (a), and so are lines for the dispute terms (d).
- **Concurrency owner** (`concurrency-and-orchestration.md`, lines 64-65): "Prevent duplicate logical outputs from concurrent/retried attempts unless duplicates are intentional"; "Ensure a resumed stage can distinguish accepted work from partial/stale work" (a).
- **Reviewed workplan §7.4** (Phase B candidate, lines 1526-1541): `qual(subject(o))`, "no failing assessment that counts here … is left without a standing disposition". R15 surfaces the "later content" narrowing but not the same-content one in (d).
- **The Manual's own statements:**
  - §10.3 "No stranded obligation" and "An answered obligation is never ready again" (a), (c);
  - §31.4's "a rollback before re-cutover" and "a reviewer's passing reassessment and a requalification reopen nothing" (a), (b);
  - §32.3's "a deliberate repair is a new item" (line 2768), which no rule makes the route of a lowered item;
  - §9.2's "a `REVIEW` of the integrated result against the invariant" (c).

  A conforming implementation must break at least one.

**Convergence assessment.** This is a non-local recurrence: the sixth consecutive round in this family, the fourth to enter through the previous same-family Review's recommended option, and the second since the author began fitting the rule to a model. Each round has closed the previous round's siblings and opened one in a transition the rule had not modelled. The active simplification trigger applies ("repeated patches around the same mechanism … patch-on-patch repair"). Another additive clause, such as re-latching, admitting stale continuations or a disposition line, would extend a state machine whose completeness no one has yet shown. A repair should remove a transition rather than add one.

Options for the stakeholder (Phase C handoff §5):

1. **Recommended: a standing lowering ends the latch's automatic life; the principal routes the repair. Removes the "becomes ready" transition; adds no mechanism.**
   - A latched obligation lowered by an event that stands (its route closed leaving the event against the line, or no route) is never ready again. It derives `COORDINATE(plan)` for item obligations, and the owner's attention for records-only ones. It stays visibly lowered (not `DISCHARGED`).
   - The principal's decision is the route: withdraw, R2-amend (a new key, hence a new obligation), or issue a repair item. That is what §32.3 already says ("a deliberate repair is a new item") and what the fence-keep route already does (§10.4, `COORDINATE(plan)`).
   - Define the dispute-term lines once:
     - every disposition record `qual` and `undisputed` relied on at `D_m` is a line, and its revocation lowers;
     - a new counting failure on unchanged content either lowers or is explicitly disclosed with the item-31 evidence choice.
   - State that a continuation restores only while it is admissible, and that otherwise the event stands.
2. **Unlatch on a standing lowering.** The obligation returns to the current-state predicate and latches again at its next `T` discharge over that state's lines. This is narrower in wording, but it re-exposes the lowered item to drift re-dispatch, and it does not answer (c): a lowered `JOINT_INVARIANT(i, k)` would need a current review of an integrated result that no longer exists. It therefore needs a separate rule for records-only obligations.
3. **Withdraw R15** and return to the reviewed §7.4 current-state discharge, with step 8 narrowed to evidence regression only (82d618c option 2). This reintroduces the drift re-dispatch R15 exists to remove, but removes the whole family. The 3940dbc record's common-mode note already put this question to the stakeholder.

**Required discriminator.** At the real owners (Admission steps 6-9 → publication → Derivation discharge → obligation derivation → Dispatcher):

- An integrated, latched item whose review is then revoked by an upheld challenge after a later item edited one of its output units. Expected: the obligation is not dispatched to its implementer; the outcome is the principal's route (option 1), or one defined re-latch on the next integration (option 2), never repeated integrations that leave it `OPEN`.
- A rollback of a cutover, then a re-cutover. Expected: the `MIGRATE` item's state after re-cutover is the one the chosen option defines.
- A latched `JOINT_INVARIANT(i, k)` whose review is revoked after a later change in `i`'s scope. Expected: a derived, admissible route exists.
- An `IMMATERIALITY` disposition relied on at integration and later revoked, with content unchanged. Expected: the item lowers (or the stated exemption applies, disclosed).
- Negative controls: the 3940dbc discriminators, which must still hold.

§31.4 has none of these. Each listed R15 case either ends at the lowering or restores while content is current (DS-001).

## Non-blocking findings

### N1 — Unconditional "no re-dispatch" statements contradict the unlatched `P` rule

§10.4 says that a `P` discharge "stays under the predicate …, and a later change of its outputs reopens it as before R15 (listed for confirmation)". Four other places state the opposite without that exception:

- §10.4's last sentences: "An absorbed foreign change re-dispatches no implementer";
- §8.3 step 8: "enacted obligations stay discharged (§10.4)";
- §32.3 (line 2768): "an absorbed foreign change to an integrated item's outputs reopens no implementer obligation";
- closure map line 298's "Consequence".

For every provisionally closed item (a `QUALIFIED` gate under SD-24, an override in scope), a later or absorbed change of its outputs re-dispatches its implementer against later code: the 82d618c drift re-dispatch. The specific clause governs, so an implementer can resolve this. But the stakeholder should confirm the `P` choice knowing that its cost is the drift re-dispatch for every provisional item, and the general statements should carry the exception.

### N2 — The latch point of the item-level review

§10.4 latches a partitioned item's item-level review at "the integration of its last part". §13.7 makes it "an item-level review of the integrated result", which in the ordinary flow is recorded after that integration, in the admitted state. At the stated `D_m` the predicate is then `F`, so as written the review never latches unless it was recorded in the last part's frame. State that its `D_m` is where its answer first acts in the admitted state, as for other records-only answers.

### N3 — A latched value at `P` outside permission has no route

A post-latch qualified refresh (the gate holder's `REVALIDATE` answer after a fixture change) gives the item `P`. Outside an override's scope or policy, that is `OPEN`. §10.4's lowered-obligation clause names only `ADJUDICATE(c)`, `ADJUDICATE_DISAGREEMENT` and `REQUALIFY`. A qualification is none of these, so the obligation is neither shown waiting on the lift nor given a ready route, and `REVALIDATE` does not apply ("a latched enacted obligation … depends on none"). Option 1 above covers it. Otherwise, name the gate holder's or owner's lift as its waiting route.

### N4 — The lifecycle oracle shares an error with the model

The table omits events, so B1 is green by construction. Beyond that, `lc_oracle` returns `0 if content_change or run_change else 1` for every provisional start before reading any event, and `lc_value` returns `vk` the same way. Both therefore give `P` for a provisional item after an upheld challenge on its review (`revoke_R`), after a revoked produced triple (`revoke_S`), and even after a `rollback`. §10.4 says a `P` value "stays under the predicate, read in current state", which gives `F` in all three cases. My probe (`$TMPDIR/ssds80-manual-review-3876473/scripts/probe.py`) confirms that model and oracle agree on `1` in all three cases.

Event-table omissions:

- re-work after a standing lowering;
- any event on the gate line other than refreshes (revocation, veto, loss);
- evidence and disposition lines;
- override withdrawal or expiry;
- events in the `PENDING` window;
- a non-continuing peer re-review;
- the item-level review, `SPEC_REVIEW` and findings-only `INVESTIGATE` cases.

§31.3 discloses that the oracle "reads the same event table". It does not disclose the provisional short-circuit.

### N5 — The `PENDING` window and editorial

- While `pub(m)` is `PENDING` "the obligation has its value at `D_m`", so an upheld challenge admitted in the window leaves the item `DISCHARGED` until reconciliation. The window is one entry, so the effect is bounded, but it should be stated as intended.
- `k` in `JOINT_INVARIANT(i, k)` is now "the admitted entry `k`" (line 1319). How a frame-derived instance relates to it across a rebase is still implicit. The rule is safe either way, because the latch reads the predicate at integration (3940dbc's unverified point, now harmless).

## Closure audit

I used the closure map to navigate and checked its R15 claims against the Manual. For every §21 item the delta or B1 touches, I checked against the sections the map names. The Manual delta since 3940dbc is seven lines:

- 100 (R15 row);
- 883 (§5.10 (g) scope sentence);
- 1261 (`REVALIDATE` row);
- 1319 and 1321 (§10.4);
- 2661 (§31.3 model text);
- 2667 (§31.4 R15 cases).

Closure map lines 87, 298 and 313 also changed.

| Item | Disposition at this candidate |
|---|---|
| 7 (obligation rules, readiness, discharge) | **open (B1)**: no transition from a standing lowering to discharge; lowered judgment obligations against §10.3; dispute-term lines undefined |
| 6 (Admission validation order) | step 8 is sound in itself; step 7's "its discharge predicate (§10.4) holds" is ambiguous for a lowered latched obligation (B1 (a)); step 6 refuses the continuations R15 relies on (B1 (b)) |
| 9 (joint invariants) | the frame-rebase case closes (3940dbc B1 (c)); **partly open** for a lowered latched review (B1 (c)) |
| 13 (publication), 18 (migration, cutover) | latch on publication holds; the rollback lowering holds, re-cutover after it falls under B1 (a) |
| 1-5, 8, 10-12, 14-17, 19-27 | text byte-unchanged since 3940dbc outside the lines above; no unresolved architectural decision found in this bounded audit (see the re-verification below for its basis) |

§16.2 rows (both tables): byte-unchanged since 3940dbc. §26.4 keeps an explicit replacement, retirement or preserved boundary for every row; I found none unresolved. Material decisions remain marked `[D3 decision]` and distinguished from `[delegated]` D4 space. Apart from B1, I found no under-specification an implementer would have to settle architecturally.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1 | Sound; unchanged. Phase B N2 is closed in text (below) |
| R2, R3 | Sound fail-closed SCC clamp and integrity halt; unchanged |
| R4 | Sound; the fence cost and the fence-keep route to `COORDINATE(plan)` are stated |
| R5-R8 | Sound; unchanged |
| R9 | Sound in itself. B1 (c) is a contradiction between R9's "never ready again" and R15's "becomes ready", owned by R15 |
| R10-R14 | Sound; unchanged. The plan row's closed form is a stakeholder-chosen conservative policy (SD-32 to SD-35) |
| R15 | **Sound in direction, still incomplete as realized (B1).** The line rule is a real improvement: it closes all four 3940dbc siblings and states one value-preserving lifecycle for continuations, provisional values and frame answers. It is incomplete in three ways: after a standing lowering (no defined re-discharge), wherever restoration needs currency that later content has removed, and for the dispute terms. It also narrows the reviewed §7.4 for same-content evidence disputes without saying so (B1 (d)). It is an author choice under item 31; its options go to the stakeholder (B1) |

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **D** design or disclosure closure, with real-owner execution owed later; **R** retained as a disclosed decision or stakeholder option; **P** partly closed.

**Basis.**

- I re-derived the delta's mechanisms independently.
- I re-checked families the delta does not touch in three ways: by the full model run (all six families green, all 42 mutations caught), by confirming their text is byte-unchanged since 3940dbc (`git diff -U0` lists only the lines above), and by reading their owner sections at the candidate (§4.1, §4.3, §5.2, §5.5, §5.10 (g), §7, §8.3, §10.2-§10.5, §11.5, §13.7, §23.6).
- I did not replay earlier records item by item. For records before 3940dbc, the dispositions are those the 3940dbc record gives, re-checked at the family owners above and against the unchanged text. Those records share this reviewer's family, so they are hypotheses carried, not independent confirmation.

**Mechanisms independently checked at this candidate:**

- **3940dbc B1.**
  - (a) Refresh read as withdrawal: continuations by author or owner and requalifications extend the line. **C** while content is current; restoration after later content changes is B1 (b) here.
  - (b) Latch drops provisionality: only `T` latches, and lines carry `P`. **C**, with the dispute-term gap in B1 (d).
  - (c) Frame answers latch before the rebase: the latch reads the predicate at the frame's integration. **C**
  - (d) `L(o)` undefined: lines are computed from what the predicate read, and the item-level review and findings-only `INVESTIGATE` are defined. **C**, with N2 for the item-level review's latch point.
  - Step 6 of its (a), "no admissible end", recurs through standing events (B1 (a) here).
- **3940dbc N1-N5.**
  - N1, route wording: "leaves the event standing against the line". **C**
  - N2, `P` scope: "`DISCHARGED_PROVISIONAL` only where the predicate's rule permits it". **C**
  - N3, evidence asymmetry: stated in closure map line 298 for confirmation. **C/R**; the same-content case is B1 (d).
  - N4, diagnostic scope: lifecycle family added. **P** (N4 here).
  - N5, editorial: `REVALIDATE` exclusion stated; R15 row aligned. **C**
- **c77447b B1 (a)-(d), N1-N6; 095ce55 B1 (a)-(d), N1-N7; 82d618c B1, N1-N7.**
  - Entry-order independence, no `tgt` after the latch, no current-state terms, the prose-and-fixed-fields key, fence and late publication, the enacted class and the item-level review: **C**.
  - 095ce55 B1 (b), the frame joint invariant: **C** again.
  - 82d618c's drift re-dispatch: **C** for latched `T` items; **R** for `P` items (N1); **P** after standing lowerings (B1 (a)).
  - 82d618c N4 (history carry for a lineage-less re-identified subject): **R**, still listed in closure map §5.
- **Revising duty and liveness (653e88c, edabd81):** `standing` entries at §4.1, §4.3, §8.3 step 7 and §10.2 are unchanged. **C**
- **Judgment disagreement (§5.10).**
  - The table, the one reach rule and invariants (g) 1-8 are byte-unchanged; only (g)'s scope sentence gained the lifecycle family.
  - §5.10 remains the one owner; other sections point to it.
  - The plan row's closed form (same prose and fixed fields, current revision not read, route-3 relief by the rejecter or owner, carry by plan subject) is a stated conservative resolution policy, re-read against its claim.
  - The equivalence `authors` input covers both sides and re-producers; unknown authorship needs an attestation or the owner.
  - **C/R** as in earlier records.
- **Matching (§6.3-§6.6).** Unchanged.
  - Phase B N2 in text: `link⁻` is an S0 test that reads no completeness. A differing old-content run under (2) and a yielding present-content run under (4) therefore stay in, under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld; only (1) and (3) narrow through `on⁺`.
  - Support cycles (§5.6) and corrupt prefixes (§5.7) fail closed.
  - **C**
- **Content identity, gate qualification (`unq` in `gterm`), equal-region partition, run identity, acting rule.** Unchanged. **C** in their owners.

| Prior record | Disposition at this candidate |
|---|---|
| 3940DBC (same family) | B1 (a) **C/P** (B1 (a), (b) here), (b) **C**, (c) **C**, (d) **C**; N1 **C**; N2 **C**; N3 **C/R**; N4 **P**; N5 **C** |
| C77447B (same family) | B1 (a)-(d) **C**; N1 **C**; N2 **P** (B1 (b)); N3 **C**; N4 **C**; N5 **P** (N4); N6 **C** |
| 095CE55 (same family) | B1 (a)-(d) **C**; N1-N6 **C**; N7 **P** |
| 82D618C (same family) | B1 **C/R/P** as above; N1-N3 **C**; N4 **R**; N5-N7 **C** |
| EDABD81 (same family) | B1, B2 **C**; N1-N4 **C/R**; N5, N6 **C**; N7 settled, its lineage is this family |
| 653E88C (same family) | B1 **C**; N1, N2 **C**; N3 **P/R** (model limits); N4 **R** |
| D94A293 (different family) | B1 **C**; N1 **C/R**; N2 **R** (§32.2); N3 **P** (model limits) |
| 913DB8F, 5895687 (B1, B1(b)), 4C52205 (SC-1 **R**), both E548472 (same-family SC-1 **R**; different-family N1-N3), D6734C4, 83A82DF, 0D2B35E, 34803DF, BF23372, A6ED164 | plan, review, equivalence and completeness rows unchanged; blockers **C**; N items **C/R/D** as the edabd81, d94a293, 095ce55, c77447b and 3940dbc records give them; plan-policy items **R** |
| 6B986DE, 29DA56E, 51070E5, 9E5A763, 051CCE3, 63DDF91, F03B15E, 61CD09B | independence, adjudication eligibility, supersession targets and relief: blockers **C**; N items as earlier records |
| 362AF9F, F22B4DC, both B46C250, F7419D5, 575DC78 | acting and enactment, run identity, gate minimum, one integration per enactment: **C** |
| 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC, 3540D98 | matching, content identity, qualification cap in `gterm`, partition: **C**, with R items unchanged |
| 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363, CC005DB, C6DA678, B595F2C, 6FF4ED1 | **C** for each stated blocker (run-keyed counting, event-keyed run, `tgt` read by every consumer, frozen matching, effect-keyed write set); N items as earlier records |
| Phase B closures, N1-N4 | matching-family closures re-verified in text (above); N1 **R** (§32.2); N2 **C/D**; N3 **R/D** (diagnostic limits); N4 **R** (empirical costs) |

Restrictive and permissive attack on the assessment-disagreement family, re-done against the delta: R15 interacts with §6 only through `ev` and `qual`. In the permissive direction, B1 (d) shows a disposed failure whose disposition is revoked after the latch, which the line rule may hide. In the restrictive direction, no settled failure is resurrected, because the line rule reads no `adverse` set after the latch.

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Latched item; upheld challenge against its review; implementer re-dispatched; re-integration | **B1 (a)**: refused for ever, or admitted without discharge and re-dispatched |
| Owner-upheld peer `NO_PASS`; owner's adverse supersession; upheld challenge on the produced triple; owner-upheld gate `REJECT` | **B1 (a)** |
| Rollback, then re-cutover | **B1 (a)** |
| Later edit of an output unit, then a revocation or loss of the review; continuation or requalification attempted | **B1 (b)**: refused stale at step 6 |
| Latched `JOINT_INVARIANT(i, k)`; its review revoked after a later in-scope change | **B1 (c)** |
| `IMMATERIALITY` disposition revoked after the latch; new counting failure on unchanged content | **B1 (d)** |
| `QUALIFIED` gate at integration; then lift, or a later output edit | held (latch at lift); output edit re-dispatches (N1, disclosed) |
| Post-latch qualified refresh outside policy | N3: no route named |
| Gate author's refresh after a fixture change, content of `s` unchanged | held (continuation; `T`) |
| Risk-overridden challenge on the produced triple; override withdrawn | held (`P`, then `F`) |
| Frame-answered joint-invariant review, clean rebase over an in-scope change | held (no latch; `REVALIDATE` before integration) |
| Two reviews on the `∃` term, one revoked | held |
| Veto of the reviewed transformation after an author's reassessment | held (reaches the continuation) |
| Fenced or `OVERTAKEN` integration, kept or re-applied; late publication | held |
| Entry order, second `AUTHOR` revision, absorbed foreign change of a latched `T` item | held |
| Later item breaking an earlier item's required evidence | held: `REGRESSION` |
| Upheld challenge admitted while `pub(m)` is `PENDING` | N5 (bounded window) |
| Composition, chain and union reach; review re-identification; plan closed form over every tightening shape | held (unchanged; model green) |
| Completeness lapse under a narrow-basis failure (Phase B N2) | held |

## Minimum architecture and capability transfer

The delta adds no primitive, component, record kind, basis mode or persistent surface. Lines are a derived reading over existing records; they replace `L(o)` and remove the Dispatcher's references as a reading set. Option 1 removes a transition ("becomes ready" after a standing lowering) and adds none. Two capabilities an owner requires are not delivered as realized:

- the protection against duplicate logical outputs and the distinction between accepted and stale work after a lowering (concurrency owner);
- a defined route for an invariant violation found after a joint-invariant review latched (§9.2).

Architecture 1.6.0 (`orchestrator/docs/architecture.md`, blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41` (`git diff --quiet fad3ee41… 38764730… -- orchestrator/docs/architecture.md source dist`: exit 0). The version-bound Core and frozen profiles are preserved (PEM PC-001).

**PEM.** Activated: this is mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` both resolve to `af0455753e20ee54a969c844872e29e270007211`. The PEM blob there and at the candidate is `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no overlay. The repository validator (`python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run in the clone, whose `source/` and PEM equal the candidate's) reports "PEM schema 1 valid: 5 families, 0 notices". In the bare snapshot it needs the Git repository and cannot realize routes. Task-local HAS:

- **PC-001**: APPLICABLE (frozen profiles; preserved).
- **DS-001**: APPLICABLE. The green lifecycle family and the §31.4 R15 cases coexist with B1, and the oracle shares an error with the model (N4).
- **SP-001**: evidence-only (one owner per fact; B1 is a lifecycle stated in §10.4 and contradicted by step 6 and §10.3).
- **SP-002, FF-001**: evidence-only, not material.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 separates G1 document checks from G2-G4 runtime evidence and claims no execution it lacks. §31.4's R15 cases now discriminate the 3940dbc siblings: refresh, qualification, frame rebase, and loss with requalification. They do not discriminate B1. Every listed case either stops at the lowering or restores while content is current. None re-dispatches after a standing lowering, requalifies after an output edit, revokes a joint-invariant review after a later in-scope change, or revokes a disposition.

The lifecycle family is an honest step toward model-first design, but it cannot see B1. The oracle reads the same event table as the rule, and that table omits the transitions B1 lives in. It also shares the provisional short-circuit error (N4). A stronger oracle would derive the expected value from the reviewed §7.4 predicate evaluated in current state on an explicit ledger, rather than from a narrative over the same events, and would include a re-work event. That suggestion adds diagnostic mechanism, not architecture.

## Doctrine-realization map and O1

§29 maps all seven entrypoints. B1 touches two rows:

- The D4 row's "close each stage with affected regression; reconcile every obligation" relies on a lowered obligation having a defined route.
- The workflow row's provisional discipline is preserved by the `P`-does-not-latch rule (3940dbc B1 (b) closed).

These are the same defect seen from the map and need no separate repair.

O1 (§0.5) is unchanged. The realized record, readers, routine questions, retention and marked surfaces are stated, all within the requested deliverable and none beyond it. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

Executed against the extracted candidate, or in the clone where stated:

- Blob identities above, by `git rev-parse` at the candidate. The model file's blob is `e8d57a21646e6daffaf310c005e7939512fe0ba7`.
- `git diff --check 3940dbc7401c4ee660b332d2c532c31bdafe62e7 387647305b91a569493c73e180cf78f04b55c9e6`: exit 0. The delta is six files: the Manual (7 lines changed), the closure map (3), the continuation handoff, the model (+188/−1 lines: the lifecycle family and eight mutations), and the previous handoff and Review record added.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the snapshot: 4 tests OK (routing and lifecycle structure only).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 bf2337285dfdaba5d535e73cf76af3d5b78978f0`: 73 files, 23,269 insertions, 1 deletion (that historical comparison only).
- `git diff --quiet fad3ee41… 38764730… -- orchestrator/docs/architecture.md source dist`: exit 0.
- PEM validation as above.
- Diagnostic model at the candidate, with `--mutations` semantics, run in parallel.
  - The driver was a scratch script, `$TMPDIR/ssds80-manual-review-3876473/scripts/par.py`, run with `python3 -I`. It loaded the unmodified snapshot module by file path in each worker of a `multiprocessing` pool, registered it in `sys.modules`, and cleared and set `MUT` at the start of every job.
  - It ran `run_family(name, verbose=False)` for each of the six families (`CORE`, the three in `FAMILIES`, `GATE_BASIS`, `LIFECYCLE`) with `MUT` empty. Then, for each of the 42 entries of `MUTATIONS`, it set `MUT = {m}` and ran `run_family` on each family that mutation names, exactly as `main()` does.
  - Results: 50 jobs, exit 0. Zero invariant failures in every base family, with these scenario counts:
    - transformation-review/acceptance/gate: 1,856,368;
    - equivalence-chain: 299,760;
    - completeness-cover: 37,600;
    - plan-coverage: 205,800;
    - gate-basis: 1,000;
    - obligation-lifecycle: 54,500.
  - All 42 mutations are caught in every family they name (44 mutation-family jobs). Single-invariant catches: `plan_supersession_current_only` by I4 only; `frame_acts_everywhere` by I5 only; `obligation_direct_only` by I8 only; `eligibility_support_tier_only` and `challenged_record_authors` by I7 only; every lifecycle mutation by I11 only.
  - `main()` itself was not called; the driver calls the same functions in the same configuration.
- A separate probe (`scripts/probe.py`) evaluated `lc_value` and `lc_oracle` on six hand-built cases outside the scenario generator's intent (N4).
- Governing owners read at `aaeaf8b`:
  - `source/roles/software-design/SKILL.md` (routing, review contract);
  - `architecture-and-design.md` (line 96);
  - `concurrency-and-orchestration.md` (lines 64-65);
  - `workflow-and-workplans.md` (lines 19, 124);
  - `convergence-and-cycle-economy.md` ("Active simplification trigger", line 62; "Review strategy after recurrence", line 89; family definition, line 25);
  - PEM and testing owners, applied through the validator, the HAS and DS-001.
- Reviewed-workplan §7.4 read at the Phase B candidate (lines 1522-1544), and §21 items 1-27.
- Manual sections read in full:
  - §0.3 R15; §4.3; §5.5 (validity, `gterm`, `ev`, `qual`); §5.10 (g); §7;
  - §8.3; §9.2; §10.2 (`REVALIDATE`, joint-invariant and item rows), §10.3, §10.4, §10.5;
  - §11.5; §13.7; §23.6; §31.3 (model text); §31.4; §32.3 (R15 line);
  - closure map line 298 and §7.
  - The rest was read by targeted search for latch, lowering, continuation, requalification, joint invariant and `INVESTIGATE`.

Not verified:

- No production SSDS, real gate or runtime was exercised.
- B1 (a) is shown under the three readings of step 7 I could construct. I did not search for a fourth.
- Whether an `IMMATERIALITY` disposition is meant to be an "evidence record behind its `ev` terms" (B1 (d)) cannot be settled from the text. That is the finding.
- The handoff asked for the six drift classes across the whole Manual. I applied them to every statement of R15 and its consumers (§8.3 steps 6-8, §10.2-§10.5, §23.6, §31.4, §32.3, closure map §5) and by targeted search elsewhere. I did not compare pairwise every concept the Manual states twice, so further drift outside these is possible.
- Earlier records' per-item closures were not replayed.

## Scientific checks

Method: one pinned architecture candidate; deductive counterexamples bound to exact owner text; a family-level recheck; structural tests; and the candidate's diagnostic with its prescribed mutations, plus a six-case probe of its lifecycle oracle.

Material findings: B1 and N1-N5. None concerns a scientific observable, numerical method or realized scientific result. B1 (d) concerns whether SSDS keeps showing an integrated item as closed unqualified after the disposition of a failing scientific-evidence assessment on its content is revoked. That is a governance consequence for how scientific evidence is presented, not a scientific judgment.

**I produced, ran or reviewed no realized scientific results.**

Variants evaluated: one normative candidate. For B1, four sibling classes:

- (a) six standing-event triggers and three readings of step 7;
- (b) two restoration routes (continuation, requalification) against step 6;
- (c) three judgment-obligation kinds;
- (d) two dispute-term cases;

and ten controls that hold. Twenty out-of-matrix trajectory classes, overlapping rather than independent trials. One diagnostic configuration (6 base families, 42 mutations) and six probe cases. The criterion was to find a material counterexample, not to select a favourable result.

No accepted project D1/D2 scientific authority was relied on for a consequential judgment, so no tension search was triggered. Gaps: real-owner execution, reader adequacy and operating costs.

## Common-mode note

The reviewer is of the **Claude family**, the same family as the Manual's author and as most earlier Manual reviewers. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. This reviewer was engaged as a fresh-context sub-agent launched by the authoring session. It did not receive the authoring conversation, but fresh context is not epistemic independence. Shared dependencies:

- the corpus;
- the inherited workplan and handoff framing (including the handoff's prompt to attack the line definition, which directed the search);
- the prior Review records, read as hypotheses (3940dbc option 1 is the direct source of the rule attacked here);
- the Git/Python toolchain;
- the diagnostic's event table, which the rule and its oracle share.

For the fourth consecutive round, this family's blocker entered through the previous same-family Review's recommended option, which also omitted the transition found here. Same-family review of same-family repair directions remains a weak check in this family. A different-family check of B1 and of whichever option is chosen is advisable before G1, together with a stakeholder decision on whether R15 should exist (option 3).

## D4 statement

This Review authorizes **no D4**, cutover, architecture acceptance, product-scope extension or proposed default. The next steps are:

1. Put B1's options to the stakeholder (option 1 recommended, option 3 as the family-removing alternative).
2. Under the chosen option, define the life of a latched obligation after a standing lowering, the admissibility condition on continuations and requalifications, and the dispute-term lines. Reconcile §10.3, §10.4, §8.3 steps 7-8, §31.4, §32.3 and closure map line 298.
3. Add B1's discriminator to §31.4.
4. Fix the lifecycle oracle's provisional short-circuit and add the omitted events (N4).
5. Consider N1-N3 and N5.
6. Freeze a replacement candidate and obtain an independent Review, preferably a different-family one, before stakeholder G1 acceptance.

G2 still separately requires a reviewed shadow workplan and explicit stakeholder authorization.
