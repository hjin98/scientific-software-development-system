# Independent D3 Review — SSDS 8 Architecture Manual, candidate 3940dbc

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          3940dbc7401c4ee660b332d2c532c31bdafe62e7
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g));
                        technical evidence for G1 only
    MANUAL blob:        f04eac442234bce8123544c3bde9795e8186a9d9 (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   437602473ddf523f2dd6c8325f1193a1ca559030 (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family c77447b
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; delta-first attack of R15 as
                        restated on a fixed reference set L(o), in both directions: what must be in
                        L(o), what a record inside or outside it can do, and every route by which a
                        member of L(o) is withdrawn, refreshed, requalified or lowered (REVALIDATE,
                        gate qualification and its lift, risk override, loss, rebase, fence, frame
                        answers); the drift classes applied to every statement of R15 (R15 row,
                        §4.1, §4.3, §8.3 steps 7-8, §10.2-§10.5, §11.5, §13.7, §22.3, §23.6, §31.4,
                        §32.3, closure map); family-level recheck of earlier families against the
                        delta; diagnostic model run with every family and mutation, in parallel;
                        structural checks of handoff §3 step 9
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched
                        by the authoring session; did not author the candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-3940dbc/snap`. The later commit adding the handoff (`3666ffec`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. SSDP 7.2.1, the reviewed workplan and the stakeholder's recorded decisions (SD-1 to SD-35, record items 19 and 31) can be realized together. The blocker below lies in R15, a refinement the author made under record item 31 and lists for the stakeholder (closure map §5, line 298). It is routed against the proposed D3 owner. Because this is the fifth consecutive round in one family, its options go to the stakeholder.

## Verdict

**NO-PASS.** One blocker, the fifth consecutive round in the obligation-lifecycle family (edabd81 N7, 82d618c B1, 095ce55 B1, c77447b B1). Again it entered through the previous Review's recommended option (c77447b option 1), which this candidate realizes closely.

- **B1**: the latched value is the standing of a fixed set of record identities. That is not the value Admission checked at `D_k`, held fixed. The difference shows in four places.
  - (a) Every route the Manual gives to refresh or restore a member of `L(o)` is a new record (a gate decision's `REVALIDATE` answer, the lift of a qualification, requalification after loss). `superseded` and `cont` treat that new record as withdrawal. So a later content change, through a forced gate re-decision, reopens an integrated item, and a lowered item can never be restored.
  - (b) `base` drops every `P` the `D_k` value carried, except a member's own `PROVISIONAL` status. A `QUALIFIED` gate or a risk-overridden challenge becomes unqualified `DISCHARGED` after publication. This contradicts SD-24, the reviewed §7.4 and the workflow owner's provisional discipline.
  - (c) A records-only obligation now latches at its answer's admission. A `JOINT_INVARIANT` review answered in a frame therefore stays discharged across a clean rebase over a concurrent in-scope change. This reopens 095ce55 B1 (b), nullifies the c77447b N3 repair and contradicts §31.4's own control.
  - (d) `L(o)` is whatever references the Dispatcher puts in the integration request. It is undefined for the item-level review and for findings-only `INVESTIGATE` items.

The c77447b B1 siblings it targeted are closed in text: latch-state order dependence, `tgt` inside `standing`, current-state predicate terms, and the item key. Its N1, N2 (with residue), N4 and N6 are closed. N3's basis entry was added, but sibling (c) defeats it. The diagnostic model is green on all five families and catches all 34 mutations. It models no obligation, latch, integration, qualification or loss boundary, so it cannot see B1.

## Blockers

### B1 — The latched value tracks record identities, not the discharge Admission checked

**Family:** obligation lifecycle after integration (82d618c B1, 095ce55 B1, c77447b B1), now through c77447b option 1.

**Earliest owner:** Manual §10.4 "Enacted obligations latch on a fixed reference set" (lines 1319-1323) and the R15 row (line 100). They decide workplan §21 item 7 and support item 6 (§8.3 step 8, line 1190) and item 9 (joint invariants, §9.2).

**Status:** open, material, non-local. §4.1, §5.5, §8.3 step 7, §10.3-§10.5, §11.5 step 3, §13.7, §23.6 and §31.4 each contribute.

**Exact rules at the candidate.**

- §10.4 (line 1321) fixes `L(o)` "when it is discharged". For an integration-claimed obligation, `L(o)` is "the records the integration request referenced (§11.5 step 3), whose predicate Admission checked at `k`". For a records-only obligation (`JOINT_INVARIANT(i, k)`, `SPEC_REVIEW(spec, r)`), it is "its answering judgment at that judgment's admission". Such an obligation latches "from its answer's admission".
- §10.4: "Once latched, the obligation is `DISCHARGED` while every record of `L(o)` stands, read as `base` without its target condition (`tgt`): it acts, is not superseded, its own `status1` is neither `REVOKED` nor `BLOCKED` (`P` when `PROVISIONAL`), `cont` holds, it is not vetoed or `nonind`. No current-state term is read after the latch". The text continues: "a content change … never reopen[s] it, while a revocation, a veto, an owner's supersession, a loss boundary withholding a record of `L(o)`, or a rollback … do". And: "A lowered latched obligation is shown waiting while an `ADJUDICATE(c)`, `ADJUDICATE_DISAGREEMENT` or `REQUALIFY` of the record that lowered it is open, and becomes ready only when that resolves against the record."
- §11.5 step 3 (line 1369): the integration request is "the candidate plus references to those admitted records" ("clean conformance, current review judgments, required gates").
- §4.1 (line 549): "a gate decision's answer, by a fresh decision on the current core: only its author's or the owner's decision naming it in `supersedes` raises `gterm`".
- §5.5 (line 757): "A non-current decision among them lowers the term and derives `REVALIDATE` for it"; "a qualification lifts only when its own decision is superseded, by its author's reassessment or the owner's adjudication".
- §4.3 `GATE_DECISION` row (line 579): `record` on the required passing assessments.
- §3.4 (line 476): "a `QUALIFIED` `ACCEPT` supports only provisionally (§5.5)". §5.5: `unq(h) = P` for `QUALIFIED`, read by `gterm`, not by `base`.
- §23.6 (line 2227): "**Requalification** uses existing kinds only: a fresh acceptance, adjudication, assessment, realization, import or consultation after the boundary".
- §10.5 (line 1327): "descendants whose support passes through a `P` value are `P` (min-propagation) and can never emit unqualified closure".
- §31.4 (line 2667): "a joint-invariant review answered in a frame and made stale by a clean rebase over a concurrent change in the invariant's scope does not latch, and is revalidated before integration".

**(a) Refresh is read as withdrawal; restoration is impossible.**

1. Item `I` (`IMPLEMENT`) changes D4 subject `s` from `r0` to `r1`. Policy requires human gate `g` on `s`. In `X`'s frame the holder records `h1 = GATE_DECISION ACCEPT` on `(s, σ, r1)`, with a `record` entry on the passing assessment `a1` of a required evidence obligation (§4.3). The integration request references the review, the conformance observations and `h1`. It is admitted as `k`, publishes and latches, so `h1 ∈ L(o)`.
2. A later item `J` changes a shared fixture `f` outside `s` that `a1`'s realization reads. Step 8 reruns the affected evidence on the merged tree. It passes with a new realization and assessment `a1'`, so `J` is admitted. `s` stays at `r1`.
3. `a1`'s realization is stale on the new tree, so `a1` is not current and neither is `h1`. `h1` is still eligible on the same gate obligation, so `gterm(g) = F`, `s` is invalid, and `REVALIDATE(h1)` is derived for its author or the owner (§10.2).
4. The only answer that raises `gterm` is a fresh decision `h2` naming `h1` in `supersedes` (§4.1, §5.5). The holder records it, and `s` is valid again.
5. `h1` is now superseded, so it no longer "stands". The latched `IMPLEMENT(I)` falls to `OPEN`. No `ADJUDICATE`, `ADJUDICATE_DISAGREEMENT` or `REQUALIFY` of `h2` is open, so the "shown waiting" clause does not apply. The item is still covered by its current plan acceptance, so `IMPLEMENT(I)` is ready and `I`'s implementer is re-dispatched against `J`'s tree. Its work is integrated, and `s` is accepted and gated.
6. The re-dispatch has no admissible end. `L(o)` was "fixed when it is discharged", and `h1` "never becomes current again" (§5.5 "Supersession"). One reading: the latched predicate stays `F`, so every integration claiming `IMPLEMENT(I)` fails step 7's "its discharge predicate (§10.4) holds", and the obligation is stranded. That is a defect by §10.3's "A ready obligation whose every answer Admission must refuse is a defect". The other reading: `L(o)` is re-fixed at a second integration, which the Manual never states, and the obligation is a duplicate logical output.

The trigger in step 2 is a content change, so §10.4's "a content change … never reopen[s] it" and §31.4's "a content change does not" are false. The predicate ("is not superseded") also contradicts the prose list ("an owner's supersession"): an author's passing re-decision is not an owner's supersession, yet the predicate lowers on it.

Sibling routes with the same mechanism:

- **Lifting a qualification.** By §5.5 this is only the supersession of the `QUALIFIED` decision, so turning a provisional gate into an unqualified one reopens the item it closed.
- **A later run's decision on the same triple.** A gate decision's supersession target is "the gate and triple, in any run" (§5.10 (b), line 843). A decision in a later run on the same content that names `h1` reopens `I`.
- **Loss.** A loss boundary withholds a review in `L(o)` (`cont = F`). The candidate waits while `REQUALIFY` is open. Requalification is "a fresh … record" (§23.6), which is not in `L(o)`, and `cont` of the withheld record stays `F` unless a continuity attestation holds it. So a successful requalification leaves the item lowered. Once `REQUALIFY` is answered, nothing is open, the item is ready, and every integrated item behind the boundary is re-dispatched. That is the c77447b N2 consequence the candidate says it removed ("becomes ready only when that resolves against the record").

**(b) The latch drops provisionality.**

1. `I` integrates while the frame's subject triple `(s, σ, r1)` carries a blocking challenge under an in-force `RISK_OVERRIDE` whose scope covers `I`'s kind. `status1` of that triple is `PROVISIONAL`, so at `D_k` the predicate is `P` and `I` is `DISCHARGED_PROVISIONAL`, admissible only inside the override's scope (§10.4, §10.5). Equally: the holder recorded `h1` as `QUALIFIED`, so `gterm = P` and `I` is `DISCHARGED_PROVISIONAL` where policy permits it.
2. Publication is reconciled, and `I` latches.
3. Every member of `L(o)` has `status1 = CLEAR`: the challenge targets the subject triple, not the review or `h1`. `unq` is not part of `base`, and the subject's `status1` is no longer read ("not the subject's current revision"). So the latched value is `T`, and `I` is unqualified `DISCHARGED` while the challenge is still open or the gate still `QUALIFIED`.
4. If the override is then withdrawn (the challenge `BLOCKED` again) or expires, the reviewed §7.4 would return `OPEN` ("that value is permitted only inside the declared scope of an in-force risk override …; otherwise the obligation stays OPEN"). The latched item stays `DISCHARGED`.

The candidate's "(`P` when `PROVISIONAL`)" shows that provisionality was meant to survive. As written, it survives only when the challenge happens to target a member of `L(o)`. §31.4's "a risk-overridden challenge later upheld … reopen[s] the obligation" holds only in that case. The common cases (a challenge on the subject or a governing prerequisite, a qualified gate) are not covered.

Taken with (a), the latch inverts the gate qualification. `QUALIFIED` becomes `DISCHARGED`, and lifting the qualification gives `OPEN`.

**(c) Records-only obligations latch before integration.**

1. `joint_invariant i` names units `a` and `b`. `X` changes `a`. In `D_n[X]`, `JOINT_INVARIANT(i, k)` is derived as one of "the obligations `X`'s integration would produce" (§7.5). §31.4 presupposes such a frame answer. A reviewer answers it with review `j`, which carries ctx `content` on `b@r` (the scope entry added for c77447b N3, line 570). By §10.4 the obligation latches "from its answer's admission", with `L(o) = {j}`.
2. `Y` changes `b` and integrates first. `X` is rebased cleanly to `X'`, the same enactment (§5.2). Whether `JOINT_INVARIANT(i, k)` keeps its identity across the rebase depends on what `k` names, which §10.2 does not define. Under the reading the frame derivation needs (`k` known before integration, like `rid`, hence the enactment), it is the same latched obligation. `j` acts in `X'`'s frame and stands, so the obligation is `DISCHARGED`. `j`'s stale scope entry is never read, because the latched value reads no basis.
3. `X'` integrates. No review ever judged `a`'s new content together with `b`'s new content. `Y`'s review saw `a` old and `b` new.

This violates §9.2 ("a `REVIEW` of the integrated result against the invariant") and contradicts §31.4's control quoted above. It reopens 095ce55 B1 (b), which c77447b had closed by requiring the predicate to hold in the latch state, and it makes c77447b N3's added basis entry inert for every frame answer. `SPEC_REVIEW(spec, r)` answered in a frame has the same shape when the specification's context moves under a clean rebase.

**(d) `L(o)` is not defined by the architecture.**

- **The Dispatcher chooses the references.** Step 2 checks only that they exist. Step 7 checks that the discharge predicate "holds after the request's own records", which is an `∃` over the state, not over the references. Two conforming Dispatchers can therefore give one history different `L(o)`. If a request omits the gate decision that actually discharged the item, a later revocation of that decision does not reopen it. That contradicts §10.4's "a revocation … do[es]". If a request includes a non-required record, that record's later refresh reopens the item through (a). Which later events reopen integrated work becomes a D4 choice.
- **The item-level review of a partitioned item** (§13.7) is listed among obligations "claimed by an integration `k`". No integration claims it: it reviews "the integrated result" after the parts integrate. So it has neither an `L(o)` nor a `pub(k)`.
- **A findings-only `INVESTIGATE` item** has no integration (§11.5, "Records-only work … has no integration step"). It is not among the parenthetical records-only obligations. Its latch is undefined, although §32.3 (line 2768) relies on "a `DOCUMENT` or `INVESTIGATE` item's … latch".

**Shared cause.** R15 states the latched value as a property: the discharge Admission checked, which only listed adverse events against what it relied on can lower. It computes that value from the `base` of a fixed set of record identities. Those are two places computing one thing (the handoff's first drift class), and they diverge in both directions:

- **Restrictive:** `superseded` and `cont` cannot tell a refresh from a withdrawal, and every refresh route in the Manual creates a new record.
- **Permissive:** `base` reads none of the `P` sources the predicate read (`unq`, the subject's `status1`, `P` premises), and a records-only answer fixes its set before the state it must hold in exists.
- **Underdetermined:** the set's membership is a D4 choice, and it is undefined for two members of the class.

Discovery stops here. Further variants re-derive (a)-(d): an `EVIDENCE_ASSESSMENT` in `L(o)` superseded by its assessor's reassessment; a frame-answered `SPEC_REVIEW` after a rebase; a prospective acceptance referenced at a promotion and then refreshed.

**Controls that hold.**

- The latch no longer depends on entry order.
- A second `AUTHOR` revision of one D2 subject no longer reopens the first (no `tgt`).
- A foreign absorption that changes `s` does not reopen `I`, since `h1` is not superseded by a decision on a new triple.
- An R1 tightening keeps the item key.
- A fenced or `OVERTAKEN` integration stays `OPEN` and waits on the human, then on `COORDINATE(plan)`.
- A post-latch upheld `NO_PASS` on `X`'s review (a veto) lowers `I` and waits on `ADJUDICATE_DISAGREEMENT`.
- A rollback lowers a `MIGRATE` item.
- A frame-answered joint-invariant review whose frame is never rebased latches correctly after integration.

**Violated owner text.**

- **Stakeholder SD-24** (record line 122): a `QUALIFIED` `GATE_DECISION ACCEPT` "supports validity and discharge only as `P` … until an unqualified gate decision on the same revision". (b) makes discharge `T`, and (a) makes the unqualified decision reopen it.
- **Reviewed workplan §7.4** (Phase B candidate, lines 1526-1541): "result is DISCHARGED_PROVISIONAL when any input above is P; that value is permitted only inside the declared scope of an in-force risk override …; otherwise the obligation stays OPEN". R15 does not surface the loss of provisionality as a narrowing or widening, so this is an unsurfaced semantic change.
- **Workflow owner** (`aaeaf8b:source/shared/references/workflow-and-workplans.md`, line 19): "descendants must not reset that state to accepted-current or emit unqualified Pass/closure while the challenge remains unresolved". Line 124 adds: "dependent outputs remain provisional and cannot close the challenged claim unqualified".
- **Concurrency owner** (`concurrency-and-orchestration.md`, lines 64-65): "Prevent duplicate logical outputs from concurrent/retried attempts unless duplicates are intentional", and "Ensure a resumed stage can distinguish accepted work from partial/stale work". Both are broken by (a).
- **Architecture owner** (`architecture-and-design.md`, line 96): "define it before dependent invariants use it: … lifecycle states and transitions". `L(o)`'s membership, the identity of `k` in `JOINT_INVARIANT(i, k)`, and the latch of the item-level review and of findings-only investigations are not defined (d).
- **The Manual's own statements:** §10.3 "No stranded obligation"; §10.4 "a content change … never reopen[s] it" and "becomes ready only when that resolves against the record"; §10.5 "can never emit unqualified closure"; §9.2's integrated-result review; §31.4's joint-invariant and content-change controls. A conforming implementation must break at least one.

**Convergence assessment.** This is a non-local recurrence: the fifth consecutive round in this family, and the third to enter through the previous same-family Review's recommended option. Sibling (a) comes from that option's "`base` without `tgt`: acting, superseded, `status1`, `cont`, vetoed, `nonind`". Sibling (b) comes from its "Nothing else of the predicate is read again". Sibling (c) comes from its "A records-only answer latches in its own admission's state". The active simplification trigger applies ("repeated patches around the same mechanism … patch-on-patch repair"). Another member-by-member patch, such as exempting passing supersessions, carrying `unq` or re-fixing `L(o)`, would add exceptions to a set-of-identities mechanism whose purpose is a single fact.

Options for the stakeholder (Phase C handoff §5):

1. **Recommended: latch a value, not a set of identities. Narrows; removes `L(o)` as a reading set.**
   - At `D_k`, the integration's own post-admission state, Admission has already evaluated the discharge predicate (§7.6, §8.3 step 7). Record that value `v_k ∈ {T, P}` as the latched value.
   - Lower it only by adverse events against the judgments the predicate read at `D_k`, computed by machinery, not taken from the Dispatcher's references: an upheld challenge (revocation) or blocking challenge, a standing veto, an adverse or owner-adjudicated supersession, a loss boundary not held by attestation, a rollback.
   - Restore it when that event is itself resolved. A passing supersession by the record's author or the owner, or a requalifying record on the same target, continues the record and is not an event.
   - Only `v_k = T` latches. A `DISCHARGED_PROVISIONAL` obligation stays under the reviewed §7.4 predicate (current-state, so provisional work is not closed) until a discharge at `T`. That is the reviewed contract's own rule for provisional values.
   - A records-only obligation answered in a frame latches at its enactment's publication, like an integration-claimed one. One answered in the admitted state latches at its admission.
   - Define `k` in `JOINT_INVARIANT(i, k)`, and the latch of the item-level review and of a findings-only `INVESTIGATE` item.
2. **Total latch at `T` only, with a closed adverse-event list over the predicate's own judgments; no restoration.** Simpler than option 1. A lowered item goes to `COORDINATE(plan)`, never to automatic re-dispatch, and §32.2 discloses that a lowered item needs a principal decision.
3. **Revert R15 and narrow only step 8 (82d618c option 2).** This reintroduces the drift re-dispatch R15 exists to remove. Not recommended.

**Required discriminator.** At the real owners (Admission steps 7-9 → publication → Derivation discharge → obligation derivation → Dispatcher):

- A gated item, then a later change to a file its gate's required evidence reads but not to the gated subject, then the gate holder's `REVALIDATE` answer superseding the old decision: the item stays `DISCHARGED`, and no implementer is dispatched.
- A `QUALIFIED` gate, or a risk-overridden blocking challenge on the produced triple, at integration: the item shows `DISCHARGED_PROVISIONAL` after publication. Withdrawing the override returns it to `OPEN`. Lifting the qualification by supersession makes it `DISCHARGED` without re-dispatch.
- A frame-answered `JOINT_INVARIANT` review, then a clean rebase over a concurrent change of another scope unit, then integration: a fresh review of the integrated result is required before the obligation is `DISCHARGED`.
- A loss boundary withholding an integrated item's review, then a successful `REQUALIFY`: the item is `DISCHARGED`, with no implementer dispatched.
- Two Dispatchers referencing different supersets of the discharging records give the same latched value under every later event.
- Negative controls, which must still lower the item: an owner-upheld `NO_PASS`, an upheld challenge on the discharging review, a rollback, and a fenced integration.

§31.4 has none of the positive cases above. A faithful implementation of R15 as written passes every listed §31.4 R15 case, because none of them refreshes a gate decision, integrates under a qualification or override, rebases a frame-answered review before checking it, or requalifies after loss (PEM DS-001).

## Non-blocking findings

### N1 — "against the record" is ambiguous

§10.4's lowered-obligation clause says "becomes ready only when that resolves against the record". It does not say whether "the record" is the lowering record or the member of `L(o)`. The intended reading seems to be "upheld against the member". Whatever option resolves B1 should state the route in those words.

### N2 — `P` from a member's own `PROVISIONAL` status has no stated scope check

Where a member of `L(o)` is itself `PROVISIONAL`, the latched value is `P`. §10.4 does not repeat that `P` discharges only inside an in-force override's scope (§10.5). If option 1 is chosen, this disappears.

### N3 — Evidence asymmetry after the latch

Revocation of a gate decision in `L(o)` reopens the item. Revocation of the passing assessment that the predicate's `ev` relied on does not: assessments are not referenced (§11.5 step 3), and "Evidence that fails after the latch reaches the claim's subject". This follows the disclosed author choice ("listed for confirmation"). The asymmetry between a gate's evidence and the gate itself should be stated with that choice in closure map §5, so that the stakeholder confirms both together.

### N4 — Diagnostic and qualification scope

The model file is unchanged since 095ce55 (blob `bd3ef8c0449a1120a7fb4ba5e9aaa6983a1a8ce2`). §5.10 (g) states truthfully that it models no integration transition, no qualified gate value and no loss boundary, and those are exactly where B1 lives. §31.4's R15 list gained cases for c77447b B1 but none for B1 here (DS-001).

### N5 — Editorial

- §10.2's `REVALIDATE` row says it "ends when `x` is current again, superseded, or no longer depended on". After R15 a latched obligation never depends on a member's currency. State that explicitly so that no implementation derives `REVALIDATE` for a stale review of an integrated transformation.
- The R15 row lists "owner supersession", while §10.4's predicate says "not superseded". Align them under the B1 repair.

## Closure audit

I used the closure map to navigate. I checked its claims for every §21 item the delta or B1 touches against the Manual sections they name. I evaluated every term of `base` without `tgt` against each route that withdraws, refreshes or requalifies a record (§4.1, §5.5, §5.10 (b)/(d), §23.6). I also evaluated every member of the enacted class against both definitions of `L(o)`.

| Item | Disposition at this candidate |
|---|---|
| 7 (obligation rules, readiness, discharge) | **open (B1)**: latched value, `L(o)` membership, records-only latch point, item-level review and findings-only investigation |
| 6 (Admission validation order) | step 8 is sound in itself; its "enacted obligations stay discharged" depends on B1 (a); step 7's claim check is over the state, not the references (B1 (d)) |
| 9 (joint invariants) | **partly open (B1 (c))**: the c77447b N3 basis entry is present but inert for frame answers |
| 13 (publication), 18 (migration and cutover) | own rules consistent; latch on `pub(k)` and rollback lowering hold |
| 1-5, 8, 10-12, 14-17, 19-27 | no unresolved architectural decision found in this bounded audit; Manual text unchanged by the delta outside §0.3 R15, §4.3's `REVIEW` row, §10.2-§10.4 and §31.4 |

§16.2 rows: unchanged by the delta. §26.4 keeps an explicit replacement, retirement or preserved boundary for every row; I found none unresolved.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1 | Sound; unchanged. Phase B N2 re-tested in text (below) |
| R2, R3 | Sound fail-closed SCC clamp and integrity halt; unchanged |
| R4 | Sound. The fence cost and the waiting route are now stated (c77447b N4) |
| R5-R8 | Sound; unchanged |
| R9 | Sound; unchanged. `REFUSED` agrees with veto lowering |
| R10-R14 | Sound; unchanged. The plan row's closed form is a stakeholder-chosen conservative policy (SD-32 to SD-35) |
| R15 | **Sound in direction, unsound as realized (B1).** Removing current-state reads after the latch is the right narrowing, and it closes c77447b B1 (a)-(d). But a fixed set of identities read by `base` is not the latched discharge. It reopens on refresh, cannot be restored, drops `P`, latches frame answers before rebase, and depends on the Dispatcher's references. It also silently widens the reviewed §7.4 for provisional values, which R15 does not list. It is an author choice under item 31; I would put B1's options to the stakeholder |

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **D** design or disclosure closure, with real-owner execution owed later; **R** retained, as a disclosed decision or stakeholder option; **P** partly closed.

The delta since c77447b touches only the R15 row, §4.3's `REVIEW` row (scope entry), §10.3's route list, §10.4 and §31.4 in the Manual, plus closure map lines 87 and 298 (word diff checked). I re-derived those mechanisms independently. Families the delta does not touch were re-checked at family level in three ways: by the model run, by reading their owner sections at the candidate (§4.1, §4.3, §5.2, §5.5, §5.10, §7, §8.3, §10.2-§10.5, §11.5, §13.7, §22.3, §23.6), and by confirming that the delta leaves them byte-unchanged. I did not replay earlier records item by item. For records before c77447b, the dispositions are those the c77447b record gives, re-checked at the family owners above.

**Mechanisms independently checked at this candidate:**

- **c77447b B1.**
  - (a) Latch state and entry order: `L(o)` is fixed at `D_k`, the latch reads `pub(k)` and no tree. **C**
  - (b) `tgt` in `standing`: removed. **C**
  - (c) Current-state terms: removed. **C** for content drift; the removal opened B1 (b) here.
  - (d) Item key: prose and fixed fields. **C**
- **c77447b N1-N6.**
  - N1, the class: defined by what the obligation is answered for, run parameters excluded. **C**
  - N2, the route after lowering: stated. **P** (B1 (a), N1)
  - N3, the scope entry: added. **P**, inert for frame answers (B1 (c))
  - N4, fence keep and late publication: stated. **C**
  - N5, the diagnostic: unchanged. **P** (N4)
  - N6, editorial: the duplicate `REVALIDATE` is removed and `REVIEW(X)` latches at the integration. **C**
- **095ce55 B1.**
  - (a) fence: **C**
  - (b) frame joint invariant: **reopened** (B1 (c))
  - (c) post-latch revocation, veto and rollback: **C** for members of `L(o)`; **P** for challenges on the subject or prerequisites (B1 (b))
  - (d) class: **C**
- **095ce55 N1-N7, 82d618c B1, N1-N7:** as the c77447b record gives them. The 82d618c drift re-dispatch is closed for direct content changes. It recurs through B1 (a)'s gate refresh. **P**
- **Revising duty and liveness (653e88c, edabd81):** unchanged. `standing` entries at §4.1, §4.3, §8.3 step 7 and §10.2. A gate whose assessment was replaced is answerable by its author's or the owner's superseder, and that answer is what B1 (a) shows the latch mishandles, not a regression of the dependence. **C**
- **Judgment disagreement (§5.10).**
  - The table, the one reach rule and the invariants are byte-unchanged.
  - I re-read the plan, transformation-review, equivalence, completeness and gate rows against their claims. The plan row's closed form (same prose and fixed fields, the current revision not read, route-3 relief by the rejecter or owner, carry by plan subject) is a stated conservative resolution policy. I found no tightening-order shape (chain, incomparable branch, join, revert, R2 amendment, multi-item rejection, objective revision) under which it supports what a standing rejection denies, and no veto it cannot lift where it bites. Its restrictive cost is disclosed.
  - The equivalence `authors` input covers both sides and re-producers, and unknown authorship needs an attestation or the owner.
  - **C/R** as in the earlier records.
- **Matching (§6.3-§6.6).** Unchanged. Phase B N2 re-tested in text: `link⁻` is an S0 test that reads no completeness, so a differing old-content run under (2) and a yielding present-content run under (4) stay in, under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld; only (1)/(3) narrow through `on⁺`. Support cycles (§5.6) and corrupt prefixes (§5.7) fail closed. **C**
- **Content identity, gate qualification (`unq` in `gterm`), equal-region partition, run identity, acting rule.** Unchanged. **C** in their owners. B1 (b) is a loss of `unq` at the latch, not in `gterm`.

| Prior record | Disposition at this candidate |
|---|---|
| C77447B (same family) | B1 (a)-(d) **C**; the repair opened B1 here; N1 **C**; N2 **P**; N3 **P**; N4 **C**; N5 **P**; N6 **C** |
| 095CE55 (same family) | B1 (a) **C**, (b) **reopened** (B1 (c)), (c) **C/P**, (d) **C**; N1-N6 **C**; N7 **P** |
| 82D618C (same family) | B1 **P** (B1 (a) here); N1-N3 **C**; N4 **R**; N5-N7 **C** |
| EDABD81 (same family) | B1, B2 **C**; N1-N4 **C/R**; N5, N6 **C**; N7 settled, its lineage is B1 here |
| 653E88C (same family) | B1 **C**; N1-N2 **C**; N3 **P/R** (model limits); N4 **R** |
| D94A293 (different family) | B1 **C**; N1 **C/R**; N2 **R** (§32.2); N3 **P** (N4) |
| 913DB8F, 5895687, 4C52205 (SC-1 **R**), both E548472 (same-family SC-1 **R**), D6734C4, 83A82DF, 0D2B35E, 34803DF, BF23372, A6ED164 | plan, review, equivalence and completeness rows unchanged; blockers **C**; N items **C/R/D** as the edabd81, d94a293, 095ce55 and c77447b records give them; plan-policy items **R** |
| 6B986DE, 29DA56E, 51070E5, 9E5A763, 051CCE3, 63DDF91, F03B15E, 61CD09B | independence, adjudication eligibility, supersession targets and relief: **C** |
| 362AF9F, F22B4DC, both B46C250, F7419D5, 575DC78 | acting and enactment, run identity, gate minimum, one integration per enactment: **C** |
| 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC, 3540D98 | matching, content identity, qualification cap in `gterm`, partition: **C**, with R items unchanged |
| 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363, CC005DB, C6DA678, B595F2C, 6FF4ED1 | **C** for each stated blocker (run-keyed counting, event-keyed run, `tgt` read by every consumer, frozen matching, effect-keyed write set) |
| Phase B closures, N1-N4 | matching-family closures re-verified (above); N1 **R** (§32.2); N2 **C/D**; N3 **R/D** (diagnostic limits); N4 **R** (empirical costs) |

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Gated item; later change to a file its gate evidence reads; `REVALIDATE` answer supersedes the gate decision | **B1 (a)**: item reopened, implementer re-dispatched, no admissible end |
| Qualification lifted by its author's superseding decision | **B1 (a)** |
| Later run's gate decision on the same triple naming the earlier one | **B1 (a)** |
| Loss boundary withholds an integrated review; `REQUALIFY` answered by a fresh review | **B1 (a)**: item stays lowered, then ready |
| Integration under `QUALIFIED` gate, or under an override of a blocking challenge on the produced triple or a prerequisite | **B1 (b)**: unqualified `DISCHARGED` after publication; override withdrawal does not reopen |
| Frame-answered `JOINT_INVARIANT`, clean rebase over a concurrent in-scope change | **B1 (c)** |
| Integration request omitting, or adding, a gate decision | **B1 (d)** |
| Partitioned item's item-level review; findings-only `INVESTIGATE` | **B1 (d)**: no `L(o)` or latch defined |
| Two items on one leaf unit, any entry order, including an absorption as the reconciling entry | held |
| Second `AUTHOR` revision of a D2 subject; foreign absorption changing a gated subject | held (no `tgt`; no supersession on a new triple) |
| R1 tightening then whole-plan re-acceptance | held (prose and fixed-fields key) |
| Fenced integration, kept or re-applied; late publication accepted | held |
| Post-latch owner-upheld `NO_PASS` on the integrated review; rollback | held (lowered; waits on `ADJUDICATE_DISAGREEMENT`) |
| Later item that breaks an earlier item's required evidence | held: refused at step 8 (`REGRESSION`) |
| Composition, chain and union reach; review re-identification; plan closed form over every tightening shape | held (unchanged; model green) |
| Completeness lapse under a narrow-basis failure (Phase B N2) | held |

## Minimum architecture and capability transfer

The delta adds no primitive, component, record kind, mode or persistent surface. `L(o)` is a derived set read from existing references. Option 1 removes it as a reading set in favour of one recorded value. Two capabilities an owner requires are not delivered as realized:

- the provisional lifecycle state after integration (workflow owner, line 19; SD-24);
- the integrated-result review of joint invariants across a rebase (§9.2).

R15 also still does not deliver the capability it exists for, stable discharge against later content, because a gate refresh reopens the item.

Architecture 1.6.0 (`orchestrator/docs/architecture.md`, blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41` (empty `git diff --stat fad3ee41 3940dbc7 -- orchestrator/docs/architecture.md source dist`). The version-bound Core and frozen profiles are preserved (PEM PC-001).

**PEM.** Activated: this is mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` both resolve to `af0455753e20ee54a969c844872e29e270007211`. The PEM blob there and at the candidate is `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no overlay. The repository validator (`python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run in the clone, whose `source/` and PEM equal the candidate's) reports "PEM schema 1 valid: 5 families, 0 notices". Task-local HAS:

- **PC-001**: APPLICABLE (frozen profiles; preserved).
- **DS-001**: APPLICABLE (the green diagnostic and the §31.4 R15 cases coexist with B1).
- **SP-001**: evidence-only (one owner per fact; B1 is a fact stated as a property in one place and computed from identities in another).
- **SP-002, FF-001**: evidence-only, not material.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 separates G1 document checks from G2-G4 runtime evidence and claims no execution it lacks. §31.4's R15 cases now discriminate c77447b B1: entry order, a second `AUTHOR` revision, an evidence-breaking absorption, R1 re-acceptance. They do not discriminate B1 here. None of them refreshes a member of the reference set, integrates under a qualification or override, checks a frame-answered joint-invariant review after a rebase (the listed case asserts the outcome the text contradicts), requalifies after loss, or varies the request's references. The diagnostic shares claim definitions and helpers with the rules it checks and models no obligations, so green runs say nothing about B1.

## Doctrine-realization map and O1

§29 maps all seven entrypoints. B1 touches two rows:

- The workflow row's provisional discipline ("risk-accepted/provisional" not reset to accepted-current) relies on discharge keeping `P`. B1 (b) breaks that after the latch.
- The D4 row "close each stage with affected regression; reconcile every obligation" relies on stable discharge. B1 (a) breaks that.

These are the same defect seen from the map and need no separate repair.

O1 (§0.5) is unchanged. The realized record, readers, routine questions, retention and marked surfaces are stated, all within the requested deliverable and none beyond it. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

Executed against the extracted candidate:

- Blob identities above, by `git rev-parse` at the candidate. The model file's blob is `bd3ef8c0449a1120a7fb4ba5e9aaa6983a1a8ce2`, the same as at `c77447b`.
- `git diff --check c77447bcac18a626ff4668b72f463fc3e17e89d2 3940dbc7401c4ee660b332d2c532c31bdafe62e7`: exit 0. The delta is 5 files: the Manual (12 lines changed), the closure map (6), the continuation handoff, and the previous handoff and Review record added.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation` in the snapshot: 4 tests OK (routing and lifecycle structure only).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 bf2337285dfdaba5d535e73cf76af3d5b78978f0`: 73 files, 23,269 insertions, 1 deletion (that historical comparison only).
- `git diff --stat fad3ee41… 3940dbc7… -- orchestrator/docs/architecture.md source dist`: empty.
- PEM validation as above.
- Diagnostic model at the candidate, with `--mutations` semantics, run in parallel.
  - The driver was a scratch script under `$TMPDIR/ssds80-manual-review-3940dbc/run/`, run with `python3 -I` (Python 3.10.12). It loaded the unmodified snapshot module by file path in each worker of a 20-worker `multiprocessing` pool, registered it in `sys.modules` (needed for its dataclasses), and cleared and set `MUT` at the start of every job.
  - It ran `run_family(name, verbose=False)` for each of the five families (`CORE`, the three in `FAMILIES`, `GATE_BASIS`) with `MUT` empty. Then, for each of the 34 entries of `MUTATIONS`, it set `MUT = {m}` and ran `run_family` on each family that mutation names. That is 41 jobs, built from the module's own lists.
  - Base results: zero invariant failures in every family. Scenario counts were not printed (`verbose=False`).
  - All 34 mutations are caught. `plan_supersession_current_only` is caught by I4 only, `frame_acts_everywhere` by I5 only, `obligation_direct_only` by I8 only, and `eligibility_support_tier_only` and `challenged_record_authors` by I7 only.
  - `main()` itself was not called; the driver calls the same functions in the same configuration. The longest job took about 18 minutes. An earlier launch of the same driver died with its shell before producing results and was discarded.
- Governing owners read at `aaeaf8b`:
  - `source/roles/software-design/SKILL.md` (routing);
  - `architecture-and-design.md` ("D3 formal-contract discipline", line 96);
  - `concurrency-and-orchestration.md` (lines 64-65);
  - `workflow-and-workplans.md` (lines 13, 19, 124);
  - `convergence-and-cycle-economy.md` ("Active simplification trigger", line 62, and the family definition);
  - PEM and testing owners, applied through the validator, the HAS and DS-001.
- Reviewed-workplan §7.4 read at the Phase B candidate (lines 1522-1544), and stakeholder record SD-24 (line 122).
- Manual sections read in full:
  - §0.3 R9, R12, R15; §4; §5.2-§5.6; §5.10; §7; §8.1-§8.3;
  - §9; §10; §11.2-§11.5; §13.7; §22.3; §23.6 (requalification);
  - §31.4; §32.3 (R15 line).
  - The rest was read by targeted search for R15, latch, `L(o)`, joint invariants, `INVESTIGATE` and requalification.

Not verified:

- No production SSDS, real gate or runtime was exercised.
- B1 (a) step 6 is shown under both readings of whether `L(o)` is re-fixed at a second integration. I did not search for a third.
- B1 (c) rests on `k` in `JOINT_INVARIANT(i, k)` naming the enactment, the reading frame derivation needs. If `k` names the transformation, the rebase derives a new obligation, the trajectory is avoided, and §31.4's "revalidated" wording is then wrong instead. The Manual should state which.
- The handoff asked for the six drift classes across the whole Manual. I applied them to every statement of R15, `standing`, `superseded`, `cont`, `unq`, requalification and the integration request's references, and by targeted search elsewhere. I did not compare pairwise every concept the Manual states twice, so further drift outside these is possible.
- Earlier records' per-item closures were not replayed.

## Scientific checks

Method: one pinned architecture candidate; deductive counterexamples bound to exact owner text; a family-level recheck; structural tests; and the candidate's diagnostic with its prescribed mutations. Material findings: B1 and N1-N5. None concerns a scientific observable, numerical method or realized scientific result. B1 (b) concerns whether SSDS shows provisionally gated or risk-overridden work, possibly on D1/D2 authority, as closed unqualified. That is a governance consequence for how scientific evidence is presented, not a scientific judgment.

**I produced, ran or reviewed no realized scientific results.**

Variants evaluated: one normative candidate. For B1, four sibling classes:

- (a) four refresh routes (gate `REVALIDATE`, qualification lift, a later run's decision, requalification), and two readings of `L(o)` re-fixing;
- (b) two `P` sources (a qualified gate; an override of a challenge on the subject or a prerequisite), plus override withdrawal;
- (c) one frame joint-invariant trajectory under two readings of `k`;
- (d) three definitional cases;

and eight controls that hold. Sixteen out-of-matrix trajectory classes, overlapping rather than independent trials. One diagnostic configuration with 5 base families and 34 mutations. The criterion was to find a material counterexample, not to select a favourable result.

No accepted project D1/D2 scientific authority was relied on for a consequential judgment, so no tension search was triggered. Gaps: real-owner execution, reader adequacy and operating costs.

## Common-mode note

The reviewer is of the **Claude family**, the same family as the Manual's author and as most earlier Manual reviewers. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. This reviewer was engaged as a fresh-context sub-agent launched by the authoring session. It did not receive the authoring conversation, but fresh context is not epistemic independence. Shared dependencies:

- the corpus;
- the inherited workplan and handoff framing (including the handoff's prompt to attack `L(o)`, which directed the search);
- the prior Review records, read as hypotheses (c77447b option 1 is the direct source of B1 (a)-(c));
- the Git/Python toolchain;
- the diagnostic's claim definitions and helpers.

For the third consecutive round, this family's blocker entered through the previous same-family Review's recommended option. Same-family review of same-family repair directions is a weak check in this family. A different-family check of B1 and of whichever option is chosen is advisable before G1. So is a stakeholder decision on whether R15 should exist at all, rather than a further author choice under item 31.

## D4 statement

This Review authorizes **no D4**, cutover, architecture acceptance, product-scope extension or proposed default. The next steps are:

1. Put B1's options to the stakeholder (option 1 recommended). Restate R15's latched value as the recorded `D_k` value at `T`, lowered and restored only by adverse events against the judgments the predicate read, with provisional discharges left unlatched. Define:
   - when a frame-answered records-only obligation latches;
   - `k` in `JOINT_INVARIANT(i, k)`;
   - the item-level review and findings-only `INVESTIGATE` cases.

   Reconcile the R15 row, §10.4, §8.3 step 8, §10.5, §31.4, §32.3 and closure map lines 87 and 298.
2. Add B1's discriminator to §31.4.
3. Consider N1-N5. They are wording the B1 repair touches anyway.
4. Freeze a replacement candidate and obtain an independent Review, preferably a different-family one, before stakeholder G1 acceptance.

G2 still separately requires a reviewed shadow workplan and explicit stakeholder authorization.
