# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 17

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 6fe100073c854b2c81d4d4b6762acbf7b04f39e7
    SCOPE: whole proposed architecture; (a) the revision-17 repairs: removal of every mechanical
           lapse of failing evidence (a failing assessment counts until a disposition stands; the
           configuration rerun and its mechanically authorized supersession as the cheap
           disposition); `about` with immutable anchor sets, `home` successors and additions-only
           terms; `counts` for frame records by recorded premises and lineage integration;
           fail-closed independence on unknown authorship; retired-key envelope commitment;
           salvage of co-submitted realizations; the model check in its no-lapse form with
           `REV16`; (b) workflow execution and verification layer and the doctrine-realization
           objective; (c) persistence, derivation, concurrency and migration; (d) Protocol 7.2.1
           inheritance reconciliation
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: 8cbfcbb5c0fd371f65e4dbe19a8523fa1880e115 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5,
           AC71FA9, 730490D, FB3E542, 124B0B7, 97E753F, 4C35D92, 644EB72, 62C0B24,
           203A42B, A414588; all NO-PASS
    REVIEW METHOD: immutable-owner reconstruction; each revision-17 mechanism (`counts`, the
           three `about` terms, configuration-rerun supersession, fail-closed authorship,
           envelope commitment, realization salvage) attacked as a new input to the two
           decisions "when does a failing assessment start counting" and "what may stop it";
           prior-finding re-derivation; exact-candidate structural tests, whitespace check and
           bounded model check in every requested mode
    REVIEWER: Claude (same model family as the author), a fresh-context sub-agent launched
           by the authoring session from REVIEW-HANDOFF-SSDS-8.0-REVISION-17.md (stakeholder
           SD-8); same model family as the author
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-6FE1000-NO-PASS.md

Candidate section references below mean the [primary workplan at the candidate][wp]. Governing-owner links pin the public source above. This context authored neither the candidate nor any prior Review, received none of the authoring conversation, and treated the handoff's scope description, the workplan's self-assessments (§0.1, §27.28-§27.29), the model check's green result and every prior verdict as hypotheses.

The two blockers below are deductions from the proposed contracts, not observed SSDS runtime failures. Their asserter is the reviewer named above; their disposition is **OPEN** against the exact candidate. This record is their canonical home. Revisit after the D3 owner repairs `counts` (§6.6 with §6.9 and §10) and the configuration-rerun authorization (§6.6 with §6.8 step 3), regenerates §0.1, §22 and §27 from those rules, and freezes a replacement candidate. No accepted project scientific D1/D2 claim is challenged.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The [kernel][kernel] says: “A coherent parent with a wrong child is an ordinary blocker.” The governing [evidence owner][evidence] is coherent and realizable here. It says “A valid failing observation is evidence”, uses `review-required` “when applicability is uncertain”, and for disagreement requires: “preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence. Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position. When a durable representation stores multiple assessments, supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement. An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.” Revision 17's own principle (“An admitted failing assessment counts against the claim until a disposition stands”, capped at `P`, i.e. `review-required`) is a sound concretization of that owner, and it is consistent with “A stale failing observation is not admissible evidence against current authority”, because the candidate never lets a failing assessment refute. Both blockers are places where the candidate does not apply its own principle. They lie in D3.

The stakeholder record (blob `edbf40da…`, unchanged since `a414588`) supports what the workplan attributes to it: SD-5 and SD-6 accept the revision-5 principles and an aspiration that is measured, not claimed; SD-8 directs this same-family sub-agent cycle “until all remaining blocking issues are closed”. Nothing in the candidate claims that a sub-agent PASS accepts the architecture (§25).

## Verdict

**NO-PASS.** Two blockers remain, both in mechanisms that revision 17 added while removing the lapse:

- **A — `counts` decides by proxies narrower than the condition it stands for.** A frame failing assessment whose evidentiary premise lies in `Δ(X)` counts in the admitted state only when “a transformation of a-'s enactment lineage (§6.9) has been integrated”. Lineage is a proxy for “the evaluated content became admitted”, and `Δ(X)` membership is a mechanical applicability decision of exactly the kind §6.6 now says machinery cannot make. The same content can become admitted by another lineage or by absorption, and a frame can change a premise without changing what the failure is about. In each case a competent failing observation never counts, while the content it evaluated is live and accepted.
- **B — configuration-rerun supersession is authorized mechanically without a change or a discriminating observation.** Step 3 authorizes any qualified assessor independent of the claim's authors to supersede a failing assessment with “an assessment of a configuration rerun of `x`'s realization whose configuration Admission verifies”. Nothing requires that an evidentiary premise changed or that the rerun's observation differs. The passing side of an interpretive disagreement, or a rerun of a nondeterministic failure that happens to pass, therefore disposes of a live disagreement by being later.

Revision 17 genuinely closes `a414588` A2, A4 and B, closes A1 and A3 on the trajectories that Review named (subject to the `Δ(X)` granularity in A3 below and the follow term in N2), and closes N3-N5, N8 and N9. The family “what can make a failing assessment stop counting” has now recurred after the mandated simplification. Per the [convergence owner][convergence] (“post-simplification recurrence, or evidence governing abstraction is wrong -> bounded reconsideration of the earliest affected abstraction”), it is routed here as one family-level problem with two members, and the repair direction below is one rule, not two patches.

Requested checks: the four routing tests pass; `git diff --check` is clean; the model check is green at depths 4 and 5 (24/24 discriminators; 76,366 and 1,879,651 transitions, matching §0.1) and red under `REV16=1`, `REV14=1`, `REV13=1`, `REV12=1`, `REV11=1` and `REV10=1`, each failing owner-grounded properties (Q and P7 in all six), not only the oracle. The model contains no frame, lineage, `Δ(X)`, configuration, premise change or supersession authority: any independent passing superseder settles a failing assessment in both its predicates and its oracle. It can therefore see neither blocker. None of these checks establishes semantic adequacy.

## 1. Blockers by earliest owner

### A — `counts` lets a frame failing assessment never count while the content it evaluated is admitted

**Owner text at the candidate.**

- §6.6: `counts(a-) ⇔ a- declares the admitted frame ∨ no evidentiary premise recorded for real(a-) lies in Δ(X), X its transformation ∨ a transformation of a-'s enactment lineage (§6.9) has been integrated`; `adverse(s, e)` and `qual(s)` require `counts(a-)`.
- §6.6 prose: “A frame record about content that its transformation changed counts in the admitted state only once its lineage integrates. A frame record whose realization ran entirely on content unchanged by its transformation is about admitted content, and counts at once, so abandoning the candidate never sheds it”; “No content change, structural change, specification change, frame outcome or challenge ends it by itself. Machinery's part is to make the disposition cheap and to schedule it, never to infer it”; the dimension table: evidentiary premises “also decide whether a frame record concerns admitted content”.
- §6.9: “**Same enactment lineage.** `k` integrates a transformation `X` produced for the same bound obligation as `X0`, as recorded in the signed task envelopes of their results”; “The **content delta** `Δ(X)` is the set of effective units whose revision in `tree(C)` differs from `B`”; Rebase: “It is never dropped because `X` itself was not integrated.”
- §10: a realization's basis has a “**target** (claim unit revision)”.
- §11.1: content “already on the live integration ref is absorbed mechanically”, including “direct push, external merge, force-push, restore from backup, manual conflict resolution”.
- §7.9: a `PARTITION` decision (R1): “Each part's obligations are derived per part”.
- §1.2: “mechanically decidable only conservatively -> deterministic machinery, answered by sound over-approximation (never under-approximation)”.

**Trajectories (every step locally compliant).** Common setup: D3 subject `s` holds claim `c`; specification `σ EVIDENCES c` and names module `m`; `a+` (assessor `X`) passes in the admitted state. An implementer task for obligation `o1` produces candidate `C1` (transformation `X1`) that edits `m` (so `m ∈ Δ(X1)`). In frame `X1`, a designated runner executes `σ`, and assessor `Y` records a failing assessment `a_Y`, either because the edit broke `m` or over a tolerance reading on which `X` and `Y` differ. `a_Y` defeats the discharge of `o1`, and `C1` is not integrated.

1. **A1 — the content is admitted by another route.** (i) A human merges `C1`'s commit onto the integration branch directly; Admission absorbs it. (ii) Alternatively the principal records an R1 `PARTITION` (or an R2 amendment), and a task bound to a new obligation `o2` resubmits `C1`'s content as `X2`, which integrates. In both, `m` in the admitted tree is byte-identical to what `a_Y` evaluated. `counts(a_Y)` stays `F`: it declares frame `X1`, its premise `m` lies in `Δ(X1)`, and no transformation for `o1` ever integrated. `a_Y` is not adverse anywhere in `D_n`, so there is no `disputed` label, no adjudication obligation, no rerun obligation and, for a D1/D2 claim, no floor item. The execution change makes `a+` stale, the Dispatcher reruns `σ`, and whichever assessor is assigned decides the claim. If an `X`-like assessor is assigned, `ev(s, e) = T`. The competent failing assessment of exactly the admitted content is ignored, and the outcome depends on assignment order.
2. **A2 — a premise in `Δ(X)` that does not change what failed.** `X1` also fixes a typo in `c` (claim content `∈ Δ(X1)`) and edits nothing that `a_Y`'s failure depends on: the failure comes from unchanged admitted code that `σ` names. `X1` is abandoned. `counts(a_Y) = F` in the admitted state for ever, although the same observation would arise on admitted content. Deciding mechanically that a failure on changed content “does not concern admitted content” is the revision 15-16 lapse rule (“a change of that content ends bearing … the observation is then about something else”) applied to frames.
3. **A3 — `Δ(X)` granularity is undefined, and one live reading reopens `a414588` A1.** “Lies in `Δ(X)`” is defined neither by content nor by unit, and §10 still records the realization's target as a “claim unit revision”. If premises are recorded as the claim unit's (or subject's) revision, any frame that edits another paragraph of `s`, or the pure restructuring of `a414588` A1 (leaf moved from `s` to `t`, no byte changed, so `rev(s)` and `rev(t)` change), puts the premise in `Δ(X)`. After rejection `counts = F`, and that Review's A1 trajectory returns unchanged. Under the content reading §27.28 is right. Two implementers can therefore build different `counts` from the same text, which C8 forbids.

**What it violates.** The [evidence owner][evidence]: “A valid failing observation is evidence”; “Do not suppress contradictory admissible observations to manufacture a pass”; “Do not resolve material assessment disagreement by … serialized record position”; “An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.” The [architecture owner][architecture]: “When an architectural concept carries normative meaning, define it before dependent invariants use it” (A3). The candidate's §1.2, C8 (A3), its own §6.6 principle (“never to infer it”) and its §6.9 sentence “It is never dropped because `X` itself was not integrated.”

**Earliest owner.** D3 §6.6 (`counts`), with §6.9 (lineage) and §10 (recorded target). Not Manual: the candidate states both the rule and the intended outcome at D3, and §22 requires the defective outcome (“must not qualify the claim at all: … a frame failing assessment whose lineage never integrated and whose realization ran on content its transformation changed”).

**Minimum repair direction.** Apply revision 17's principle to the start of counting as well: *machinery may only make a failing assessment start counting, by a monotone latch on an immutable or admitted fact, and may schedule its disposition; it never decides that a failing observation does not concern admitted content.* The simplest form needs no new record kind: a frame failing assessment counts in the admitted state from its admission. Where its recorded premises differ from admitted content, S3 derives at once the configuration-rerun obligation on admitted content, which is the cheap disposition (as constrained under B). A weaker form that still closes A1: latch `counts` when the recorded premise revisions are current at any admitted position, by any route, not by lineage. That form leaves A2 open, so it needs an explicit argument or the owner's judgment at abandonment. In either form, define premises at content granularity and remove the §10 “claim unit revision” target (A3).

**Required discriminators**, through real Admission, Derivation, discharge and inspection consumers: A1 (i) absorption of the rejected candidate's commit and (ii) the same content through a new obligation, each followed by a passing rerun assessed by another assessor; both must leave the claim qualified, labelled and with an adjudication obligation. A2 with an editorial claim change. A3: a frame that edits only another part of `s`, and a pure leaf move between subjects, each rejected. Contrast: a frame failure on candidate content, followed by a rerun on admitted content that passes and supersedes under B's rule, lifts the qualification.

### B — configuration-rerun supersession resolves a live disagreement by position

**Owner text at the candidate.**

- §6.6: “When an evidentiary premise of an adverse failing assessment changes, S3 derives a rerun obligation … An assessment of that rerun, by a qualified assessor independent of the claim's authors, names the failing assessment in `supersedes`. Admission authorizes that supersession mechanically, after checking that the configurations match. A passing rerun therefore disposes of the failing assessment”; “A realization's **configuration** is its specification unit, regime, parameter instance, seed or replicate identity, and every execution attribute the specification fixes.”
- §6.8 step 3: “a record may name `x` in `supersedes` only as `x`'s own assessor's reassessment, the owner's adjudication or discriminating assessment, or an assessment of a configuration rerun of `x`'s realization whose configuration Admission verifies (§6.6), and in each case only by an actor independent of the claim's authors”.
- §6.6 “What does not end a disagreement”: “A passing assessment of another realization or configuration, on any content”; “A later passing assessment that is not authorized as a supersession.” §10: “A reassessment replaces an earlier one only by explicit, authorized supersession, never by being later.”
- §7.5: R2, “an independent agent or human reviewer”, decides “dispositions of an assessment disagreement (§6.6)”; §6.8 steps 7-8 rerun “affected evidence … on the merged tree” at every integration.
- §22: “These must remove the qualification: an independent passing assessment of a configuration rerun that supersedes the failing assessment”.

**Trajectories (every step locally compliant).** D3 claim `c` in `s`; deterministic specification `σ`; `X` assesses PASS (`a+`), `Y` assesses FAIL (`a_Y`) on the same observation, disagreeing over a tolerance reading. Neither the claim nor any named execution content changes.

1. **B1 — interpretive disagreement.** A designated runner executes `σ`'s configuration again: as part of an unrelated integration's step-7/8 rerun, or on request, since step 3 does not require an obligated rerun. The output is identical. `X`, who is qualified and did not author the claim, assesses the new realization PASS and names `a_Y` in `supersedes`. Admission finds the configurations equal and authorizes the record. `disp(a_Y) = current(a_X2) = T`, `undisputed = T`, and the `disputed` label and the adjudication obligation are gone. `Y`'s reading was never adjudicated by the owner and no discriminating evidence was obtained: the later assessment by the opposing side won. With a cosmetic premise change first (a comment in `m`), the rerun is even obligated, and the result is the same.
2. **B2 — nondeterministic failure.** `σ` exercises code with a race or a nondeterministic reduction. `a_Y` records a genuine failing run at a fixed seed. Reruns of the same configuration are requested until one passes. Its independent assessment supersedes `a_Y`. A failing rerun would “supersede it too and keep the claim disputed”, so the chain ends at the first pass. The valid failing observation, which is evidence of nondeterminism, is suppressed by count.

For a D1/D2 claim the decision class is R3, so a human must record the superseding assessment. That bounds B for D1/D2 claims but does not remove it: the human is any qualified human, not necessarily the owner, and is again re-assessing a non-discriminating observation.

**What it violates.** The [evidence owner][evidence]: “route adjudication to the governing claim/owner or obtain discriminating evidence. Do not resolve material assessment disagreement by majority vote, latest-editor order, … count, … or serialized record position”; “supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement”; “Separate executions sharing one expected-value generator, reference implementation, policy, … or mistaken assumption are correlated”; “Do not suppress contradictory admissible observations to manufacture a pass.” The candidate's §6.6 (“never to infer it”; “A passing assessment of another realization … on any content” does not end a disagreement, although a rerun is another realization) and §10 (“never by being later”).

**Earliest owner.** D3 §6.6 (configuration rerun) and §6.8 step 3 (supersession authority).

**Minimum repair direction.** Keep the configuration rerun as the cheap disposition only where it is discriminating. Admission authorizes a configuration-rerun supersession by an assessor other than `a-`'s own only when (i) a recorded evidentiary premise of `a-` has changed in the evaluating frame (the S0 trigger the obligation already uses), and (ii) the rerun's observation is not identical to the one `a-` assessed. An identical observation re-assessed is the interpretive dispute itself, which `a-`'s assessor, the owner's adjudication or `IMMATERIALITY` settles. Also (iii): for configurations the specification declares nondeterministic, a passing rerun supersedes only under a replicate rule the specification fixes, or by the owner's adjudication. Reconcile the “What does not end a disagreement” bullet with this rule.

**Required discriminators:** B1 with unchanged content, and with a cosmetic premise change, must leave the claim qualified with the adjudication obligation open; B2 must leave it qualified; contrast: a genuine fix of `m`, a rerun whose observation differs, and an independent passing assessment that supersedes, lifts the qualification. The model check needs an authorization predicate for superseders and a premise-change and observation-identity dimension. Without them its oracle certifies B.

## 2. Non-blocking findings

### N1 — historical governing-version adoption remains partly evidenced

Unchanged since `62c0b24` N1 (§0.4; stakeholder record, “Not covered”). The handoff independently binds this Review to 7.2.1, and the release state at the candidate names 7.2.1 accepted-current. Earliest owner: §0.4, pending stakeholder restatement.

### N2 — the content-follow term under-approximates where a claim that left home lives

`about`'s third term adds `s` only when “the evaluated target lies within scope(s) and within no scope of home(a-)”. A claim moved by cut and paste from `s` to `t` is not followed when a byte-identical quotation remains anywhere in a home subject (“formerly: p q”), or when the moved text is edited, and its specification is replaced by a new unit rather than retargeted. The proposition is then accepted in `t`, unqualified, while home `s` stays `P`. The dispute remains visible and routed at `s`, and for D1/D2 the floor item stays, so this is not the inert loss of `a414588` A3. But §6.6's sentence “A claim that leaves home by any route … is also followed to wherever its content now lies” overstates the design, and dependents of `t` are not “visibly qualified”. Separately, anchors are computed “in the admitted state at its base” while `home` folds only changes “after a-'s admission”, so a region transfer between the request's base and its admission is covered only by the content term. Repair: state the guarantee that holds (home is never shed); have the specification term follow the obligation's own retarget, split and rename lineage; fold `home` from the base position. Earliest owner: §6.6; Manual item 5.

### N3 — the specification term over-attaches

“s has a required evidence obligation derived from a-'s specification unit” makes a failing assessment for obligation `e1` (claim `c1`) qualify every subject the same specification unit evidences: `qual(s2)` reads `e1` through `about(a_Y, s2)`. One failing case of a suite-level specification disputes every claim the suite covers, with floor items and adjudication obligations for each. The effect is restrictive. Intended is presumably “the obligation `a-` names, or its retarget successors”. Earliest owner: §6.6.

### N4 — the disagreement floor and decision class are no longer latched

Revision 16's floor read “has borne at some admitted position (immutable once true)”. Revision 17's reads “a failing assessment that counts”, on a subject that `about` makes D1/D2. `counts` is monotone, but `about`'s specification and content terms are not, so D1/D2 status reached through them can be withdrawn by an R2 specification retarget or a copy restored at home. Human attention then disappears without an authenticated human judgment (A8), and the decision class drops from R3 to R2. Repair: latch the floor item, and the highest decision class reached, once true. Earliest owner: §6.6 and §7.9.

### N5 — fail-closed authorship removes agent disposition from absorbed and legacy content

`a414588` B is closed by “an unknown author lineage is never disjoint from an agent's”. Genesis baseline content, legacy imports, Case B/C repositories and every human push are absorbed without an authoring record. For every failing assessment on such a claim, an R2 disposition, including the configuration-rerun supersession, can therefore never be independent. Meanwhile S3 routes the adjudication obligation “to the qualified owner of the claim”, which for R2 is an agent whose disposition is admitted with `eff = F`. No rule escalates the obligation to a human. The effect is restrictive, but it is a liveness gap, and a burden transfer at odds with §1.2 (“reduces, rather than transfers, complexity”) and SD-1/SD-2. Repair: route such obligations to a human (or an attestation request) mechanically, and add the rate to §26. Earliest owner: §6.6, §7.5; Manual item 3.

### N6 — the step-3 supersession sentence can admit an unauthorized `supersedes`

Step 3 says a record may name `x` in `supersedes` only as listed, “and is otherwise admitted as a non-independent judgment that cannot satisfy one”. Read literally, an unauthorized superseder is admitted, and S0's `superseded(x)` (“authorization was checked at admission”) becomes true. A failing `x` is unaffected, since `eff` of a non-independent record is `F`. But any role that may submit judgments can permanently de-currency a passing assessment or an `IMMATERIALITY` disposition by naming it. This is a restrictive denial of service, and it contradicts step 6's “nothing unauthorized enters”. Repair: reject the record, or strip the field, and record the refusal. Earliest owner: §6.8 step 3 (editorial).

### N7 — specification-derived support edges also change on absorption

§6.6 says the disposition edges come from “`home` and specification-derived obligations, which change only when admitted records are added”, with the content-follow term as “the one exception”. Required obligations derive from `EVIDENCES` relations in `T_n`, which an absorbed edit changes. A cycle through such an edge is then classed as “corrupted input” with an integrity obligation. The evaluation is still `F` (restrictive), but the exception list is incomplete. `a414588` N6 is partly closed. Earliest owner: §6.6.

### N8 — residual pre-revision-17 text

- §2.1 S4: “failing evidence whose realization still bears on the claim”.
- §7.4: “capped at P by any bearing failing assessment”.
- §10's table: “`EVIDENCES` -> claim unit”, “**target** (claim unit revision)” and “a bearing failing assessment”. The target entry is material to blocker A3.
- §15.4's table: “adversity follows existence and bearing”.
- §21 item 14 still says envelopes “issued before its retirement record stay verifiable”, the rule §0.1 says was replaced.

§0.1's “N7 … §10 rewritten” is true of the prose only. Earliest owner: those sections.

### N9 — the outstanding-envelope list comes from private operator state

Step 3 now verifies retired-key envelopes against the list in the retirement record. Task issue lives only in the Dispatcher's operator journal (§6.3), which §13 rebuilds after host loss. A retirement caused by host loss can therefore omit live envelopes, and their never-lost records are then refused. The effect is permissive for the claim, but rare and recoverable by re-issue. Name where the list comes from (for example run-branch envelopes and harness observation), and state what happens to an unlisted never-lost record. Earliest owner: §6.8 step 3; Manual item 14.

## 3. Re-verification of previous Reviews' findings

“Closed” means the named deductive trajectory is excluded by the candidate's contract, not executed qualification or acceptance.

### A414588

| Finding | Disposition | Basis |
|---|---|---|
| A1 frame-local anchor; re-iteration to a third subject | **Closed under the content reading of `Δ(X)`; open under §10's claim-unit reading** | Anchors include the admitted base subject; a frame record on unchanged content counts at once (Blocker A3) |
| A2 singular anchor under nesting | **Closed** | All nested subjects are anchors; `ev(P, e) = ev(A, e)` in either order |
| A3 relocation without a region transfer | **Closed** for byte-identical relocation with no home copy, or with specification retarget; **partly** otherwise (N2) | Home is never shed; content and specification terms add the destination |
| A4 execution scope read from S2 | **Closed** | No search scope; no closure is read in S0 |
| A family (“stop counting”) | **Open** | Recurs at `counts` (Blocker A) and at supersession authority (Blocker B) |
| B unknown authorship credited | **Closed** | Fails closed; agent lineage never disjoint from unknown authorship (liveness residue N5) |
| N1 | **Partly closed** | Unchanged |
| N2 retired-key bound | **Closed in step 3**; §21 item 14 stale (N8); list source (N9) | |
| N3 supersession authority in step 3 | **Closed** for the omission; malformed sentence (N6) | |
| N4 co-submitted realization | **Closed** | Step 6 salvages it when it passes its own checks |
| N5 stray execution copies | **Closed (moot)** | No content search |
| N6 step 5 and successor edges | **Partly closed** | Successor edges covered; absorbed specification edges not (N7) |
| N7 residual “claim unit” | **Partly closed** | Prose rewritten; table and other sections retain it (N8), material to Blocker A3 |
| N8 convergence owner miscited | **Closed** | §27.26 corrected |
| N9 mode label | **Closed** | Default mode `REV17` |

### Earlier Reviews

The `a414588..6fe1000` diff touches §0, §0.1, §6.6 (S0 adverse scope, Assessment disagreement, uniqueness, support graph), §6.8 steps 3, 5 and 6, §6.9 Rebase, §7.9 (disagreement floor), §10, §21 item 5, §22 (disagreement group and model-check item), §26, §27.26, §27.28-§27.29 and §28, plus the model check and six lines of the authority index. No `source/`, `dist/`, `orchestrator/`, test, release-state, PEM, stakeholder-record or archived-predecessor path changed (verified with `git diff --stat` and blob identities).

- **203A42B A** (shrink, sibling leaf, split with retarget, `EVIDENCES` removal, D1/D2 floor before the first pass): **closed**; no structural change ends a failing assessment, and an admitted-frame failing assessment counts from admission. **203A42B B: closed**; step 6 still refuses a never-lost record with an unauthorized `supersedes` (N6 is the non-never-lost sibling).
- **62C0B24 A, 644EB72 A and B, 4C35D92 A, 97E753F A, B1 and B2, 124B0B7 A, FFBAD17 A: closed.** `ev`, `undisputed`, `disp`, `eff` and `contested` are unchanged except that bearing is now constant `T`; P1-P8 and Q are green to depth 5.
- **FB3E542 A: closed**; `bind(j)` is unchanged. **FB3E542 B: partly closed**, through blockers A and B.
- **Strata.** S0 now holds `home`, `about` and `counts`, which read only record syntax, `Σ`, `T_n` and ledger facts. S1 is unchanged. S2 remains monotone, with a unique least fixed point. The S0 claim for `counts` is underdefined only through `Δ(X)` granularity (Blocker A3).

The remaining 730490D, AC71FA9, F3608F5, 8A75346, 441CF5C and F9D9DE8 closures do not depend on the changed text and remain **closed**. FFBAD17 N7 (inherited index and whitespace residue) remains outside this scope.

## 4. Out-of-matrix trajectories attempted

| Attempt | Result |
|---|---|
| `a414588` A1 with the content reading of `Δ(X)` | Holds: base anchor `s`; counts at once |
| `a414588` A1 with §10's claim-unit target | **Fails** (A3) |
| Nested promotion, assessment before and after | Holds |
| Cut and paste with retarget; `git mv` across path patterns; uncovered-region detour; bytes identical | Holds (destination added, home kept) |
| Same, with a quotation left at home or an edited move and a replaced specification | Destination not followed; home stays `P` (N2) |
| Specification edit plus fresh completeness judgment | Holds: nothing reads a closure |
| Absorbed claim, disposition by its unrecorded author | Holds: fail-closed; owner exception records common mode |
| Agent disposition on genesis or legacy content | Never independent; obligation routed to an agent (N5) |
| Frame failure, candidate later merged by hand, or re-issued under a new obligation | **Fails** (A1) |
| Frame failure with an editorial claim change, candidate abandoned | **Fails** (A2) |
| Frame failure, later iteration of the same lineage integrates | Holds: counts; the iteration's rerun must supersede first |
| Frame failure on content the frame did not change, candidate rejected | Holds: counts at once |
| Frame rerun supersession, candidate rejected | Holds: the superseder is not current in `D_n`, so `a_Y` stays undisposed |
| Same-configuration rerun on unchanged content assessed PASS by the passing side | **Fails** (B1) |
| Rerun-until-pass of a nondeterministic failure | **Fails** (B2) |
| Genuine fix, rerun, independent passing assessment supersedes | Holds (intended) |
| Specification tolerance loosened, rerun passes and supersedes | Decided by the specification change's accepted judgment at R2/R3; holds |
| Non-independent superseder of a failing assessment | Holds: `eff = F`; the claim stays qualified |
| Unauthorized `supersedes` naming a passing assessment or `IMMATERIALITY` | Restrictive denial of service (N6) |
| Suite-level specification, one failing case | All covered claims qualified (N3, restrictive) |
| D2 status reached through the specification term, then retarget away | Floor item and R3 class lost (N4) |
| Cycle through an absorbed `EVIDENCES` edit | Evaluates `F`; misclassified as corruption (N7) |
| Retired-key envelope after host loss | May be unlisted; never-lost record refused (N9) |
| Workflow layer, publication, frame enactment, intake, migration and recovery trajectories of earlier records | Hold as recorded; their text is untouched by revision 17 |

## 5. Minimum architecture, capability transfer and inheritance

**Minimality.** Revision 17 removes `bears`, `present`, `where`, per-role search scopes and claim-unit membership in derivation, and adds `counts`, two additions-only `about` terms and one Admission authorization rule (§27.29). No primitive, record kind, store or component is added. The removal is the right simplification, and it closes most of the family at once. Both blockers sit in the additions, where machinery still decides that a failing observation does not apply (`counts`) or has been answered (configuration match). The repairs above remove or narrow those two decisions. They add no mechanism, beyond a monotone latch if the weaker form of A's repair is chosen.

**Convergence.** This is post-simplification recurrence. The single rule that should now be stated at D3, and every S0 input to `adverse`, `qual`, `disp`, the floor and the decision class tested against it, is: *machinery may start a failing assessment counting and schedule its disposition; only a judgment that addresses the failing observation, or discriminating evidence, may stop it.* `counts`, step-3 supersession authority, the non-latched floor (N4) and the `about` terms (N2, N3) are the inputs to test.

**Predecessor comparison.** Revision 17 did not touch §16.2 or §18. Blobs verified at the candidate:

| Predecessor | Blob |
|---|---|
| befe678 hypothesis archive | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |
| Consolidated Protocol 8 plan archive | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| Orchestrator Architecture 1.6.0 (equal at public source and candidate) | `39e6de727f6c35402962509d30d947962992eaad` |

The bounded semantic comparison of §16.2 and §18 recorded by earlier Reviews still holds by identity.

**PEM basis and HAS.** Project instructions designate `main` as the integrated publication line. The local tracking ref `origin/main` is `af0455753e20ee54a969c844872e29e270007211`, equal to the workplan's basis. Its `PROJECT-ENGINEERING-MEMORY.md` blob equals the candidate's, `1561797125622f355f84eb27319f87e8fa4227d9`. There is no branch overlay. The uncovered later interval proves no absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: The model check is green in all 24 discriminators while A and B hold; its superseder is always authorized and it has no frame, lineage or premise-change dimension. §22 requires the behaviors behind both blockers.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen profiles required through the versioning owner; preserved by §24; unchanged by revision 17.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy; repair at the owning D3 rules (§6.6 counts, §6.8 step 3) and regenerate §0.1, §22 and §27 from them.
  - id: SP-002
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: Self-reference-safe identity unchanged by revision 17.
  - id: FF-001
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: No immutable publication in scope; remains applicable to later genesis and release.
```

**7.2.1 reconciliation.** The release state at the candidate names 7.2.1 accepted-current, with public source `aaeaf8b6…` and recovery `efdd1b59…`, matching the handoff; `source/PROTOCOL_VERSION` is 7.2.1. The diff changes no §0.4, §19 or §24 text and no `source/`, `dist/`, `orchestrator/`, release-state or PEM path, so the §0.4 obligation table and §19 landing points stand. The inherited evidence doctrine is not yet realized at A and B.

## 6. Qualification-program adequacy

§22's disagreement group lists no-lapse cases, Admission salvage cases, the independence cases of `a414588` B and the removal and non-qualification lists. It cannot discriminate A or B, and in two places it requires the defect:

- “must not qualify the claim at all: … a frame failing assessment whose lineage never integrated and whose realization ran on content its transformation changed”, with no contrast in which that content becomes admitted by another route;
- “must remove the qualification: an independent passing assessment of a configuration rerun that supersedes the failing assessment”, with no premise-change or observation-identity condition.

Every no-lapse case is followed by “a passing rerun of another realization”, and none by a same-configuration rerun on unchanged content. The [testing owner][testing] asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Revision 17 as written is such a concretization for A and B: every listed §22 case and every model-check property stays green. Add the discriminators named in §1. Give the model a supersession-authority predicate, a frame and lineage dimension, and a premise-change and observation-identity dimension, and add a sensitivity mode that reproduces revision 17's rules.

The four consolidation tests establish frontmatter and routing only. HARD-template thresholds, mutation strength, evaluator calibration, custody, blinding, paired baselines and doctrine-realization measurement remain later-gate obligations (§22-§25). No campaign was run and no improvement estimate is asserted.

## 7. What was verified and how

- **Candidate identity.** Resolved the candidate SHA and the workplan blob `8cbfcbb5…`. Extracted a `git archive` of the exact candidate into a scratch directory; later commits, including the handoff commit `012eba7`, were excluded.
- **Owners read** at `aaeaf8b6` with `git show`:
  - the D3 role entrypoint (`software-design/SKILL.md`: routing, D3 design contract, Independent Review and Challenge);
  - architecture (read first: admissibility, “one authoritative representation/state”, “define it before dependent invariants use it”);
  - evidence (target vs execution dependency; applicability and `review-required`; correlated executions; suppression; Assessment disagreement);
  - workflow (Review independence; Optional independent cognitive trajectories: process vs epistemic independence, common-mode recording);
  - testing (smallest plausible wrong concretization; proxy-proof real owner);
  - convergence (core progression including post-simplification recurrence; active simplification trigger; family routing);
  - the kernel's Challenge text.

  Release identities were resolved from `PROTOCOL-RELEASE-STATE.yaml` at the candidate.
- **Candidate read.** §0 and §0.1, §0.3-§0.4, §1-§2, §5, §6.1-§6.9 in full, §7.1-§7.10, §8, §9.1-§9.8, §10, §11, §12, §13, §14, §15.6-§15.7, §21 items 5 and 14, §22 (disagreement group and model-check item), §25 gate table, §26, §27.28-§27.29 and §28; the full `a414588..6fe1000` diff, including the authority index; the stakeholder record; the routing test; and the model-check source.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the archive: **4 passed, 0 failures, 0.025 s**, Python **3.13.16**.
- **Whitespace.** `git diff --check a4145880… 6fe10007…`: **exit 0**, no diagnostics.
- **Model check**, depth 4 (76,366 transitions in every mode):
  - default mode `REV17`: **0 failures, 24/24 discriminators as expected, exit 0**;
  - `REV16=1`: **1,174 failures (P7 64, Q 444, O 666)**; two discriminators differ; **exit 1**;
  - `REV14=1`: **2,440 failures (P7 124, P8 148, Q 864, O 1,304)**; three differ; **exit 1**;
  - `REV13=1`: **12,670 failures (P7 936, Q 4,076, O 7,658)**; five differ; **exit 1**;
  - `REV12=1`: **13,122 failures (P5 81, P7 936, Q 4,245, O 7,860)**; seven differ; **exit 1**;
  - `REV11=1`: **13,078 failures (P7 936, Q 4,234, O 7,908)**; ten differ; **exit 1**;
  - `REV10=1`: **13,608 failures (P1 262, P7 936, Q 3,882, O 8,528)**; seven differ; **exit 1**.

  Each sensitivity mode fails at least one owner-grounded property (P1-P8 or Q), not only the oracle.
- **Model check**, depth 5, default mode: **1,879,651 transitions, 0 failures, 24/24 discriminators, exit 0** (100 s), matching §0.1.
- **A and B.** Deductive, from the quoted contract text, and checked against the model source: the candidate generator offers `ASSESS PASS supersedes=t` as an always-authorized superseder, Q's premise excludes any superseded failing assessment, and the oracle's `settled` accepts any independent superseder. Neither blocker is representable in the model's vocabulary, so no scratch reproduction was attempted.
- **Identities.** Verified the predecessor blobs, the release-state identities, the PEM blob identity and `origin/main`, the stakeholder-record blob and the changed-path list above.
- **Repository untouched.** No candidate, source, distribution, index, release state, PEM or frozen resource was changed. The only repository output is this record. Nothing was committed or pushed.

**Scientific inquiry envelope.** Examined architecture-mediated evidence applicability, frames and lineage, reruns and supersession, independence, disagreement and closure. Materiality here is the ability to change support, closure or the next authorized action. No physical or numerical result is asserted. One pinned candidate was reviewed through multiple deductive trajectories; no variant search over scientific analyses was performed and no delegates were launched. The judgment relies on accepted engineering, evidence and workflow doctrine, not on project D1/D2 authority, so the tension-search duty was not triggered.

## 8. What could not be verified

- **PEM schema validation.** `source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run on the working-tree file whose blob equals the candidate's, failed with `UNAVAILABLE: repository revision is not resolvable as an immutable object` for historical evidence routes (`55c08526…`, `81375d81…`). This checkout is a **shallow clone** (`git rev-parse --is-shallow-repository`: `true`). That is an environment limitation, not a PEM defect and not a pass.
- **Remote state.** `origin/main` is the local tracking ref. No fetch was performed and no remote-state claim is made.
- **Readings and Manual compositions.**
  - A1 (ii) assumes that a `PARTITION` or amendment gives the resubmitted work a different bound obligation. The partition text says “Each part's obligations are derived per part”. The absorption variant (i) does not depend on that assumption.
  - A3 assumes evidentiary premises are recorded at the granularity of §10's realization target, which the candidate does not otherwise define.
  - B1 assumes that a designated runner's execution of the same configuration, for any reason, can be assessed and named as a configuration rerun. Step 3 states no obligation precondition.
  - N5 assumes that genesis, absorption and intake records are not authoring records, as their definitions indicate.
- **Runtime evidence.** No SSDS production owner, witness deployment, harness adapter or Architecture Manual exists. Runtime fidelity, read recording per harness, failure injection, lineage attestation, privacy enforcement, scaling and burden reduction remain unexecuted (§21-§26), and none is counted as a pass.
- **Repository acceptance.** The full repository regression, package build and validation, distribution parity, frozen-resource census and Core snapshot tests were not rerun. This Review changes no protocol source or descendants.

## 9. Common-mode dependency

This reviewer is a fresh-context sub-agent **of the same model family as the author** (Claude), launched by the authoring session from a handoff the author wrote, under stakeholder SD-8. That is a material common-mode dependency: shared blind spots, framing inherited from the handoff's scope list, and the same corpus and toolchain are all plausible. The [workflow owner][workflow] says: “Separate context improves process independence but not epistemic independence when agents share model, source corpus, toolchain or oracle”.

This cycle again gives concrete evidence of that dependency. The `a414588` Review (same family) proposed the content-follow clause (“the evaluated target is absent from every subject in `succ*(anchors(a-))` and present within `scope(s)`”) and the fail-closed authorship clause. Revision 17 adopted both nearly verbatim, and N2 and N5 sit there. The repair directions in this record carry the same risk. A different family might frame the disagreement problem differently, for example by refusing any mechanical disposition at all.

The handoff gave no author conclusions. This record supplies **no different-family corroboration**. The design's own §9.6 lets policy require that for high-consequence surfaces, and the stakeholder has waived it for this cycle. A PASS from this cycle would still need the owner adjudication and production evidence of later gates ([workflow, Optional independent cognitive trajectories][workflow]).

## 10. D4 statement

**D4 remains NOT AUTHORIZED.** Phase B Review is NO-PASS. The next step is the owning D3 repair of `counts` (§6.6 with §6.9 and §10; A) and of the configuration-rerun supersession authority (§6.6 and §6.8 step 3; B). It should be done as one family rule: machinery starts counting and schedules; only addressing judgment or discriminating evidence stops. §0.1, §22, §27 and the model check should be regenerated from that rule, and a replacement immutable candidate frozen. Even a later Phase B PASS authorizes nothing by itself:

- G1 needs the accepted Manual and explicit stakeholder acceptance of the major change.
- G2 needs a separately reviewed shadow workplan and stakeholder authorization.
- G3 needs real-owner implementation evidence.
- G4 adds per-subject cutover, quiescence and rollback (§23-§25).

This Review grants no Manual acceptance, implementation permission, spend release, cutover, ratification or promotion.

[wp]: https://github.com/hjin98/scientific-software-development-system/blob/6fe100073c854b2c81d4d4b6762acbf7b04f39e7/workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
[kernel]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md
[architecture]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/architecture-and-design.md
[workflow]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md
[evidence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/evidence-evolution-and-dependencies.md
[testing]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md
[convergence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md
