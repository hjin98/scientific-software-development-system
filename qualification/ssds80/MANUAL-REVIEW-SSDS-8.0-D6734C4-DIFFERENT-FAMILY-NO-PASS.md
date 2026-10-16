# Independent D3 falsification Review — SSDS 8 Architecture Manual, d6734c4

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: d6734c48ad3b3b4411ab84b50b850f4965da257c
    SCOPE: whole proposed Manual; SD-30 plan rejection, relief and brief carry;
           judgment disagreement and earlier closures; inheritance, qualification,
           doctrine realization, minimum architecture and O1
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: ba0b5887cc9c319a64b060633b8fb912adf6defd
    CLOSURE MAP BLOB: f82a03fd7ed49162d10a8dc1de9435bb2d1b8271
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PARENT DESIGN REVISION: 23
    PARENT PHASE B CANDIDATE: e23f14208be869e6a78cfd7b312e447254ee1851
    PARENT PHASE B BLOB: 610f373b97fb8152d2a5742e17fa172e12204756
    PARENT BLOB AT MANUAL CANDIDATE: 91bde236465178f20c7348280e036d2884dfc216
    PHASE B REVIEW: qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    FROZEN ARCHITECTURE BLOB: 39e6de727f6c35402962509d30d947962992eaad
    PRIOR REVIEWS: those enumerated in the D6734C4 handoff, hypotheses only;
                   6ad34e6 was not reviewed
    REVIEW METHOD: immutable-owner reconstruction; family-level, bidirectional
                   falsification; closure and capability-transfer audit; independent
                   challenge of the diagnostic claim envelope; candidate checks
    REVIEWER: GPT family; reviewer engaged by the stakeholder; did not author
              the candidate; launched no reviewing sub-agents

All Manual line numbers below are one-based lines of the pinned candidate blob. Candidate content was read from an extracted `git archive` of that commit. The working checkout was on the named branch at `6ee8d48edd0c3aad8419ae6c96c7cc9cfa7076a4`; that later commit was not reviewed as the candidate. Release state independently confirms the public-source and recovery identities above. Only this Review record was added to the repository. No commit or push was performed. Scratch and the extracted snapshot are under `$TMPDIR/ssds80-manual-review-d6734c4-df` (`/tmp/ssds80-manual-review-d6734c4-df` in this execution).

## SERIOUS CHALLENGE

None against accepted governing authority. The governing D3, evidence, workflow, definition and convergence requirements are jointly realizable. B1 is an incomplete realization of an explicit stakeholder instruction in the proposed Manual's brief-selection rule. It does not show that SD-30's rejection claim or the accepted evidence owner is unsound.

The governing D3 owner requires definition of architecture-bearing lifecycle/interface semantics before their use and a single owner per material claim. The workflow owner requires decision-sufficient handoffs and says an unresolved contradictory material assessment cannot be erased by synthesis. Those constraints do not require another disagreement mechanism here.

## Verdict

**NO-PASS for the exact candidate. One narrow blocker survives: B1, the plan-rejection disclosure family.** An objective-only amendment requires another whole-plan acceptance while leaving the item revision unchanged. Section 16.5 requires carry of rejections of an *earlier item revision*, so a literal conforming brief renderer may omit the standing rejection of that unchanged item under the old objective. This leaves the SD-30 brief obligation, and the relevant part of workplan §21 item 10, incomplete.

The plan veto and per-target relief repair itself held in the attempted trajectories. In particular, this finding is **not** a peer-acceptance escape from the veto: a contrary peer pass remains vetoed. Its consequence is a required review being conducted without the prior objection that the stakeholder expressly required its brief to supply. The distinction matters to the repair and to convergence.

The four routing tests, both diagnostics and every prescribed judgment-model mutation pass their respective checks. None tests plan-brief construction or closes B1. G1 remains open; stakeholder acceptance and D4 authorization do not follow from this Review.

## 1. Blocker

### B1 — Plan-rejection carry is keyed on an earlier item revision, although a new acceptance target can arise from the objective alone

**Family:** incomplete disclosure of standing plan objections after a change of acceptance target. This is the brief-carry part of the previous `83a82df` B1(b)/(c) family, with an objective-coordinate sibling. The reach/relief part of that Review's blocker is closed. **Earliest owner:** proposed Manual §16.5, line 1761, consumed by the Interface's plan-acceptance brief; workplan §21 item 10, with item 26's review templates. No D1/D2 change is requested.

**Exact relevant meanings.** An item's revision and the plan objective's revision are separate. Section 11.1 makes the objective a separately scoped `Objective` part; §1.5 hashes a unit's own terms and semantic declarations inside its scope. Section 4.3 gives a plan acceptance an `EXACT` content entry on the objective and `PLAN_CONTROL` entries on its named items. Its target (§3.4 and §5.10(b)) contains **both** the objective revision and the item revisions. Consequently an objective-only edit can change the acceptance target and invalidate the old acceptance while preserving the item's revision.

Section 11.4, line 1352, expressly requires whole-plan review for a change to the plan objective. Section 16.5, line 1761, selects:

> every standing `PLAN_ACCEPTANCE` rejection of an earlier revision of the item, under any objective revision

“Under any objective revision” ranges over objectives **after** restricting to earlier item revisions; it does not include the unchanged current item revision.

**Concrete trajectory, with a locally conforming renderer.**

1. Declare plan `P` with separately scoped parts `P.objective` and `P.A`. Let their revisions be `o1` and `a1`. A qualified independent actor records `j = PLAN_ACCEPTANCE(o1, {A:a1}, REJECTED)`. It is admitted, has no standing resolution and remains a standing objection. A prior acceptance can also exist; it is vetoed. No argument requires deleting a finding or hiding a recorded assessment.
2. The principal changes only the plan's `Objective` prose, producing `o2`. The item section, its contract, its own prose and semantic declarations remain byte-identical, so `cur(A) = a1`. The objective amendment is an allowed plan amendment; the required human attention to that amendment is not an adjudication disposing of `j`.
3. The old plan acceptance has an unsatisfied `EXACT(o1)` basis. A whole-plan acceptance of `(o2, {A:a1})` is required by §11.4. The next acceptor is a fresh reviewer and receives the prescribed brief.
4. Implement the new carry rule exactly: select standing rejections for the same item whose named item revision is an **earlier revision** than the one asked. `j` names `a1`, equal to the asked `a1`, so it is not selected. Render the remaining §16.3/§16.5 inputs. No clause requires turning `j` into a separate `FINDING` record, and the gate-brief rule in §16.6 does not impose its full adverse-judgment core on this R2 plan-acceptance brief. The renderer may therefore omit `j` while satisfying the candidate's specific carry rule. It may include it voluntarily, but that is not an architectural guarantee.
5. The reviewer is asked to judge the new objective/item target without the standing rejection the stakeholder required the next acceptor to receive. The rejection is still discoverable through history or a separate owner obligation; discoverability does not satisfy a requirement to carry it in this brief.
6. If that reviewer passes, §5.10(b) still reaches it because `r* = r = a1`. A peer cannot relieve it; the item stays non-issuable until the prescribed owner/rejecter resolution. Thus the veto is safe, while the required disclosure has failed. A refusal after review cannot retroactively supply the omitted input to that review.

**Cheap siblings and controls.**

- Objective-only change with one unchanged rejected item: omission as above.
- Whole-plan review after an objective change plus an edit to **another** item: the unchanged rejected item's rejection is still excluded.
- A multi-item rejection `{A:a1, B:b1}`, followed by an objective-only amendment with both item revisions unchanged: neither item passes the earlier-item-revision filter, so the rejection can be omitted altogether. Changing an unmentioned third item does not cure the omission.
- Control: if B itself changes to `b2`, selecting the rejection through B and presenting the complete rejection record supplies it to a whole-plan reviewer, even though A is unchanged. That case is not a second omission; selection should be a union over the named items, without requiring the complete target set to match.
- An ordinary R2 prose change of A from `a1` to `a2`: the current rule does carry `j`; this is why the existing §31.6(V) prose-edit discriminator does not detect the objective-only case.
- Changing only the objective does **not** end `stands⁻(j)`; it closes ordinary supersession through the old exact objective basis, while route 3 on the new exact target and route 4 remain available. The defect does not require weakening those rules.

**Violated requirement and significance.** Stakeholder decision record item 25/SD-30 selects:

> carry standing rejections into the next acceptor's brief

The selected instruction does not restrict carry to changed item revisions. Workplan §21 item 10 requires the brief templates and their activation/injection inputs to be decided; item 26 requires the review templates. Manual A4 says:

> a duty a task owes is carried in its brief or enforced mechanically

The mechanical veto enforces refusal of an unresolved contrary pass. It does not enforce delivery of the rejection to the next acceptor, which is the additional SD-30 duty. The workflow owner's decision-sufficient-handoff contract requires recovery of material unresolved blockers and findings without hidden history. This is a missing mandatory input in a defined interface, rather than optional editorial polish or missing G3 runtime evidence.

**Minimum repair direction.** Remove the “earlier revision” restriction from the existing selector: carry each unresolved standing rejection naming the item at **any** revision, including its currently asked revision under another objective, subject to the already declared resolution/withholding rules. Select against every item named by a multi-item rejection. This broadens one existing brief query; it adds no record kind, veto, latch, registry or new decision route. Keep the exact-target, independence and acting guards of relief unchanged.

**Required discriminator.** At the Interface's real plan-brief constructor, admit `j(o1,{A:a1})`; amend only the objective to `o2`; request the new whole-plan acceptance. Assert that the rendered brief contains `j`'s identity, outcome and native finding/rationale route, labeled as another reviewer's, although A's revision is still `a1`. Repeat with a second amended item and a multi-item rejection. Preserve two independent controls: a peer pass on the new target remains vetoed, and the rejecter's/owner's independent exact-target pass relieves it. A selector restricted to `rejected_item_revision != current_item_revision` must fail the brief test. Execution of that production discriminator belongs to G3; its specified result belongs to G1.

**Convergence and stop.** This is an incomplete projection of a two-coordinate target, not another unsound definition of what a tightening preserves. Do not reopen the working reach/relief rules to repair it. The cheapest option is the selector broadening above. If the stakeholder instead wants an intentionally narrower disclosure, that is an explicit change to SD-30 to put to the stakeholder, not an author-selected interpretation. A third option is to reconsider plan-brief composition at its single existing owner if the sibling test reveals more omissions. Further discovery here stopped after the objective-only, other-item and multi-item variants: expanding into a universal brief checker would be implementation work and would not change this verdict.

## 2. Non-blocking findings and retained decisions

### N1 — The state-locality invariant omits the explicit adverse-record exception

Section 5.10(g)5, line 883, says a record of a pending, abandoned or replaced enactment changes no admitted veto “in either direction.” Sections 5.2 and 5.10(c) explicitly make an adverse frame judgment object in every state, and §5.5/§32.3 expressly disclose that a pending frame `REJECT` can veto admitted support. An admitted peer pass plus a never-integrated frame rejection is the counterexample to the unqualified invariant sentence.

The operative rules, the loss/pending-effect disclosures and the required real-owner negative case all agree about the intended adverse exception; I found no unresolved implementation choice between them. Treat this as an over-broad invariant statement, not a new frame-state safety blocker. Narrow (g)5 to permissive/superseding/relieving frame records and state the adverse exception beside it. Likewise, (g)6's universal order-independence aspiration must not be described as proved by the model's two sampled reference-respecting permutations. The surrounding model envelope correctly limits the evidence.

### N2 — Preserve the stakeholder decisions and empirical costs as decisions and limits

The following remain live, rather than newly closed by this Review: bounded-only reproductions partly narrowing SD-17 availability; SD-24's provisional cap and author/owner-controlled gate minimum; exact-representation and fence-induced D1/D2 re-gating; replacement-enactment decisions under R12; withheld cross-pending-frame support; adverse frame judgments surviving abandonment; accumulating gate minimum members; fenced cutover leaving native mode over legacy bytes; context-relative supersession and context-revert reuse; party exclusion from adjudication remaining policy-configurable; broad two-sided/re-producer authorship and unknown-authorship attestations; large-scope `INCOMPLETE` widening; directed `sat` hop costs; and R2 changes producing new plan targets outside part of the old rejection's reach.

Sections 32.2-32.4 and closure-map §5 expose these costs and the author's delegated choices. They are stakeholder acceptance options and G3 measurements, not separate blockers. In particular, SD-30's claim that tightening preserves what was rejected is conservative rather than a claim that no tightening can cure a defect: only the rejecter or owner may judge that cure through exact-target relief. The revert exemption avoids forcing rejection of controls that the reverted item no longer contains.

### N3 — Historical adoption provenance and diagnostic coverage remain bounded

The 2026-10-12 adoption instruction remains paraphrase-only. This task directly binds 7.2.1; it does not recover that historical transcript. Only authentic recovered evidence or stakeholder restatement closes the historical gap. Neither diagnostic establishes reader quality, practical burden reduction, runtime utility, scientific adequacy or independent production behavior. Those limits remain prominent at G1.

## 3. Closure audit — every workplan §21 item and both §16.2 tables

I located the decisions in the Manual directly, using the closure map as an index and comparing its assertions to the owning sections. “Answered” below means an architectural contract is present, with the stated refinements; it does not mean implemented, independently runtime-qualified or stakeholder-accepted.

| §21 item, including subordinate clauses | Candidate answer and disposition |
|---|---|
| 1 unit/manifest/anchor model; representation, partition, scope, structure, quarantine, tenure | §§1.1-1.11; answered. Effect-keyed write set, single-pass dynamic overlap, frozen term-level matching and exact Git-entry representation were checked separately. |
| 2 relation attributes, adoption, SDGs, cycles, boundary completeness and analyzers | §§1.7, 2.1-2.6; answered. No warrant from definitional condensation; analyzer identity is a currency condition. |
| 3 schemas, kinds, tiers, dispositions, classes, independence, actors, inquiry, fixed attributes, compatibility | §§3, 5.10, 6.8, 17.1; answered as D3 schema/semantics; serialized implementation remains D4. |
| 4 basis modes, execution/reading, subject boundary, classes, paths, widening/closure | §§4, 6.3-6.5; answered. Completeness-union reach and unbounded permissive exclusion were re-derived. |
| 5 complete derivation/disagreement, frames, prospective tenure/enactment, analyzer/recovery/fence semantics | §§5-7, 10.2, 17, 22.3; answered subject to N1's invariant wording. Lower-stratum inputs and fail-closed SCC/corrupt-prefix behavior are explicit. |
| 6 Admission, structure/freeze/support, queue/idempotency, append/quorum, observation/publication/fence/ABA | §§8, 21-23; answered, with the listed R4 removal of a durable attempt log. |
| 7 obligations, readiness/discharge, provisional/risk scope, iteration/attempt | §10; answered with R9/R10/R12/R13. |
| 8 plans, acceptance, amendments and invariants | §11 and §13.4; veto and relief answered; associated disclosure defect is B1 under items 10/26. |
| 9 serialization, generated units, joint invariants, residual risk | §9; answered. |
| 10 operations, queries, briefs/Channel C, duties, labels, read recording, transports/bootstrap | §16; **not fully closed: B1's plan-acceptance brief selector**. Gate cores, version binding and other brief inputs have substantive answers. |
| 11 scientific realization basis, ensembles, observation boundary, runners/custody | §§6.10, 17; answered, with fixed/free attribute and external-custody limits disclosed. |
| 12 intake/classification/dispositions, trust/quarantine/adoption/realignment and neutral auto-adoption | §18; answered. Path-bound quarantine is not content-following. |
| 13 modes/import scope/reconstruction, refinement/promotion/demotion/restoration, carve-out/cutover/quiescence/genesis | §19; answered. Prospective cutover is carried by a pending, typed transformation and checked at integration. |
| 14 ledger/storage/identity/publication intent, fences/retention/fsync, witnesses/currentness/loss/recovery, confidentiality and operator/index boundary | §§21-25; answered with R4's explicit specialization. Quorum and non-admission conditions are stated; breach handling weighs retention before loss. |
| 15 actors/authentication/trust roots | §25.1-§25.2; answered. |
| 16 protected surfaces/self-governance | §25.3; answered under prior-rule adoption and human gates. |
| 17 component boundaries, separation and Architecture 1.6.0 supersession | §26; answered; both transfer tables audited below. |
| 18 rules/schema/successor evolution | §27; answered; historical interpretation and current re-derivation are distinguished. |
| 19 independent version dimensions | §28; answered. |
| 20 external units, consultation/import and cross-repository boundary | §20; answered; no atomic multi-repository admission is claimed. |
| 21 all §19.1/§19.2 inherited Manual decisions | §§1.11, 13, 16, 29.7; substantive answers, with B1 limiting plan-brief realization. |
| 22 minimum justified architecture | §30, checked against §§21/26 and the parent constraints; present, with empirical caveats. |
| 23 role templates, task/record/write boundaries, lineage, policy narrowing, standing plan | §12; answered. |
| 24 contract schema/lint/coverage/order/partition/budgets/system contracts | §13; answered. Parts have separate obligation identities and enactments; replaced pending parts are distinguished from completed parts. |
| 25 templates, forces/aggregation, analyzers, mutation/annotations/HARD qualification | §14; answered as design; proposed thresholds are not accepted or executed qualification. |
| 26 reports/routing/floors/coordination/reclassification/review and inspector templates | §§15-16; **B1 leaves the plan-review projection incomplete**; other routing/floor contracts answered. |
| 27 every role/specialist duty mapped to E0-E3 and remaining E3 duties disclosed | §29; map present with full domain cores and a remaining-duty E3 route. Its presence claim is bounded by B1 for plan-rejection disclosure. |

**Workplan §16.2 first table: all invariants 1-26 have final dispositions in Manual §26.4.** Deferred invariants 4 (one CLI/root), 9 (benchmark context), 15 (execution lifecycle), 17 (capability keys) and 26 (containment) are concretely decided in §26.3-§26.4, not merely routed. Preserved functions include structured manual transport, resource admission after explicit route selection, route-before-render privacy, identity-before-dispatch, K2 leases and truthful uncertain routing. Retired ladder/module boundaries are explicitly replaced rather than silently dropped.

**Second table:** capability/distribution ladder, Core prompt behavior and composition SPI; API/SPI separation, compatibility, public records, pagination, structured errors, mutation idempotency, sync/async behavior and freeze policy; shared record mappings including declined `CandidateRef`/`StageResultEnvelope`; Tracker history/projection/export; Adapter routes/execution/benchmarking; Scheduler resources/reservations/failover; configuration/secrets; persistence; failure/degradation; security/privacy; benchmark integrity; fitness checks; acceptance ladder; versioning; and simplicity/reopen triggers all have final dispositions in §26.4. The frozen layout/namespace and CLI surfaces also have explicit rows. No Deferred transfer row was found still merely deferred.

Material D3 decisions are separated from delegated parser libraries, diff implementation, mutation tool, storage engines, checkpoint encoding, limit values and reason-code members. I found no additional incidental D4 machinery whose specification itself blocks G1. B1 is an unresolved interface-content obligation, not a delegated implementation choice.

## 4. Refinements R1-R14

| Refinement | Independent assessment against the reviewed contract |
|---|---|
| R1 | Sound conservative construction at its declared scope: one recorded execution basis, frozen resolution semantics; `on+` adds conjuncts to `on-`; `link-` only enlarges adverse matches; complete external record and recorded free attributes compared permissively. Unknown/unbounded inputs cannot earn a stop. Availability and unrecorded-variation limits remain. |
| R2 | Sound fail-closed narrowing: clamp every non-trivial support SCC to F before evaluation, then evaluate the remainder. |
| R3 | Sound fail-closed corrupt-prefix treatment; earlier historical positions remain readable. Witness qualification, not S0, owns provisional-chain checks. |
| R4 | Sound explicit specialization: incarnation-local at-most-once publication and mandatory fencing after loss of the incarnation replace uncertain durable-log intactness. Costs and VM/ABA limits are disclosed. |
| R5 | Sound partition construction in the tested static/dynamic cases, including equal resolved regions and one-pass non-cascading ABSENT. |
| R6 | Sound subject-owned scope identity; byte-preserving part refinement does not itself rebind subject acceptance. |
| R7 | Sound non-warrant tension relation: CHALLENGES is excluded from cycle legality and validity/warrant prerequisites. |
| R8 | Sound per-kind authorization with exact supersession targets; gate triple reach is the stated exception; cross-target review relief is not supersession. |
| R9 | Sound non-voting disagreement extension in the tested kinds; answered/REFUSED and TASK_RESULT slots are explicit. Its new plan brief safeguard is incomplete through B1. |
| R10 | Explicit, coherent kind/tenure/run distinction; unchanged non-native-D1/D2 triples can reuse the judgments the formula permits, while native D1/D2 acceptance/gates require the current run. |
| R11 | Sound conservative minimum over eligible gate decisions; qualification cannot be hidden by another holder's unqualified decision or a stale/superseded fallback. |
| R12 | Explicit narrowing to one producing-task enactment with clean rebases; second integration refused; replacement iterations and overtaken/fenced re-applications require new enactments. No pending sibling records are silently promoted. |
| R13 | Sound two-point independence enforcement: Admission refuses ineligible adjudications at any chain depth; base excludes nonind support; root authors and class are defined once, with machinery/import distinctions and owner exception disclosed. |
| R14 | Reach/claim composition and SD-30's plan veto/relief are sound in the attempted cases. No fresh-peer exemption remains; revert, incomparable branches, multi-item and objective changes preserve the veto. B1 concerns the accompanying brief projection, not a reason to replace this working reach rule. Directed-hop and conservative widening costs remain explicit. |

These are assessments of a proposal. Review does not ratify its defaults, author-selected trade-offs or product scope. No other unsurfaced material change to the reviewed parent was found in the bounded reconstruction.

## 5. Previous findings re-verified at family level

**Status meanings:** closed = the current text excludes the named trajectory; partly closed = some demanded current behavior/disclosure remains incomplete; retained = an explicitly disclosed decision, empirical limit or historical gap, not executed closure. A later repair's new sibling is not evidence that the old concrete trajectory remains open.

### 5.1 Most recent records, including every named N finding

| Review / finding | Disposition and current basis |
|---|---|
| 83a82df B1(a), (a-prime): fresh acceptance of tightened/current revision | Closed by removing the exemption; `r* = r` or both revisions below cur reaches fresh peer passes. Route 3 only for rejecter/owner, exact target, independent and acting. |
| 83a82df B1(b), (c): new-target disclosure, multi-item/objective siblings | **Partly closed:** item-changing R2 briefs now carry prior rejections; objective-only/unchanged-item carry remains B1 here. Mechanical veto across objective and item-set changes is closed. |
| 83a82df N1 | Closed: the judge-dependent exemption is deleted, eliminating the sentence/formula discrepancy. |
| 83a82df N2 | Closed as specified behavior: objective EXACT basis is now in the supersession cell; route 3 supplies relief at new objective/item targets without requiring false reassessment of the old target. |
| 83a82df N3 | Closed as disclosure: directed-hop cost now appears in §32.2 as well as R14. |
| 83a82df N4 | Closed as accounting/envelope: two-item wording and mutations agree; shared claim definitions remain an explicit diagnostic limit. Brief carry is expressly not modeled. |
| 83a82df N5 | Retained decisions/costs, N2-N3 here. Revert leaves the old rejection correct and can leave an adjudication obligation requiring a challenge; this is disclosed liveness cost. |
| 0d2b35e B1(a)-(c) | Closed mechanically: common upper tightening of incomparable accepted/rejected revisions is reached; per-item denial survives objective and other-item changes. The brief sibling remains B1 here. |
| 0d2b35e N1 | Closed for further-tightening supersession and new-target relief; old-objective/multi-item target supersession still obeys its basis. That restriction no longer removes all ordinary relief at a newly judged target. |
| 0d2b35e N2 | Closed as disclosure; direction is retained, not removed. |
| 0d2b35e N3 | Closed for the missing incomparable scenario; oracle/common-helper and fixed-authorship limits retained. |
| 0d2b35e N4 | Closed for the identified stale map/formula/discriminator and unowned inspector wording. |
| 0d2b35e N5 | Retained as N2-N3 here. |
| 34803df B1(a)-(b), B2(a)-(c) | Closed: plan rejection reaches beyond current-only coverage and denies each named item; equivalence authors cover differing content on both sides, re-producers included; `sat` hop direction explicit. |
| 34803df N1 | Closed as disclosure, not oracle independence: common claims column is now explicit. |
| 34803df N2 | Closed attribution: item 24 distinguishes stakeholder direction from author-selected concretizations. |
| 34803df N3 | Closed: analyzer identity is a currency condition in §2.6 as well as the table; SD-29/30 references updated. |
| 34803df N4 | Closed as disclosure of composite/part equivalence granularity; no universal cross-granularity veto was inferred. |
| 34803df N5 | Retained as N2-N3 here. |
| bf23372 B1(a)-(c), B2 | Closed: union completeness reach, analyzer-neutral target, provisional asserting hops, and request-independent authorship requirements. |
| bf23372 N1 | Closed for revert/excess reach; R2-item disclosure added, with the objective-coordinate sibling B1 here. |
| bf23372 N2, N3 | Closed as disclosures of re-scoping/promotion and partition-composition limits, with item-level review retained. |
| bf23372 N4 | Closed as honest model envelope, not independent semantic validation; extra families/mutations exercise the repaired mechanics. |
| bf23372 N5 | Closed for R14 numbering/cost/accounting residue. |
| bf23372 N6 | Retained as N2-N3 here. |
| a6ed164 B1 | Closed: either-direction equivalence connectivity reaches every contributing asserting hop; directed consumers cannot compose around the objection. |
| a6ed164 N1 | Closed as narrowed mechanical evidence claim; N1 here notes the remaining invariant-language exception. |
| a6ed164 N2 | Closed: third-column route, analyzer condition/target distinction, current owner routes and removed shorthand. No separate normative content loss found from moving Review identifiers cold. |
| a6ed164 N3, N4 | Retained decisions/provenance/empirical limits, N2-N3 here. |

### 5.2 Earlier recurring judgment, gate and enactment findings

| Review(s) / findings | Disposition and independently traced mechanism |
|---|---|
| 6b986de B1, all record/root/input siblings | Closed: one `authors`, one requirement list, fixed record-level `nonind`; every adjudication checks root independence and maximum chain class. |
| 6b986de N1-N6 | Closed for redispatch, classification/attestation disclosure, broad-author costs, challenge class definition and named qualification additions; model coverage remains bounded. |
| 6b986de N7-N9 | Retained party-exclusion, trade-off, provenance and empirical limits. |
| 29da56e B1, chain/support-route siblings | Closed: no support-tier-only or immediate-target-only escape; all adjudications are checked at Admission; nonind support never answers an independence-requiring obligation. |
| 29da56e N1-N5 | Closed for unanswered/refused adjudication, human non-authorship attestation, R3 floor, root/disposition definitions and document-level discriminators. |
| 29da56e N6-N8 | Retained policy/operational/provenance limits. |
| 51070e5 B1 | Closed: challenge upholding, dismissal and counter-chain routes have the same root/class eligibility floor. |
| 51070e5 N1-N5 | Closed for requirement/root definition, dispatchability, identified discrimination cases and stale routes; future execution remains unexecuted. |
| 51070e5 N6-N7; 9e5a763 N4-N5 | Retained costs and limits. |
| 9e5a763 B1; N1-N3 | Closed: nonind relief cannot lift a peer veto; real-owner discriminator is specified; partition example distinguishes completed, replaced pending and later-reopened parts. |
| 051cce3 B1 | Closed: transformation review supersession stays on id(X); widened reach is handled only by exact-target author/owner relief. |
| 051cce3 N1-N5 | Closed for exact-target wording, partition selection, cutover timing and specified discrimination cases; no runtime evidence inferred. |
| 051cce3 N6-N7 | Retained context-relative supersession and stakeholder costs. |
| 63ddf91 B1; N1-N5 | Closed for member-revision completeness target, plan relief, partition selection, cutover and named qualification/wording defects. |
| 63ddf91 N6 | Retained costs. |
| f03b15e B1-B2; N1-N5 | Closed: targets defined per kind; a late or wrong-kind cutover carrier is refused; authorized reassessment bypasses answered refusal; partition identity includes decision id; fenced-native half state is disclosed. |
| f03b15e N6 | Retained costs. |
| 61cd09b B1-B2; N1-N6 | Closed: exact relief targets, human pending-carrier MODE_TRANSITION, full adverse gate core, fence cost, partition obligation binding, first-submitter rule and qualification cases. |
| 61cd09b N7 | Retained costs. |
| 362af9f B1-A/B1-B; N1-N6 | Closed: gate veto key excludes run, cutover identity is recorded before use, re-application is new work, partition bindings/first submitter/rebase registration are explicit. |
| 362af9f N7 | Retained costs. |
| f22b4dc B1-A through B1-F | Closed: task enactment rather than obligation lineage; each partition has its own event; entry identities cover absorption/adoption/re-identification; unchanged subjects retain the admitted run. |
| f22b4dc N1-N5 | Closed for the observation exception, explicit R12 narrowing, gate pending/adverse disclosure, non-latching implementer obligations and named cases. N1 here corrects a remaining summary-level overclaim. |
| f22b4dc N6 | Retained costs. |
| b46c250 different-family B1-A through B1-D; same-family B1 | Closed: one acting state for support/supersession/relief/gates; pre-computable event identity; frame/admitted equality includes unchanged subjects. |
| b46c250 different-family N1-N4 and same-family N1-N4 | Closed for evaluation-state precision, accumulation disclosure, stale accounting and named real-owner design cases; runtime/diagnostic coverage remains limited. |
| b46c250 different-family N5-N6; same-family N5 | Retained trade-offs and historical/empirical limits. |
| f7419d5 B1 and its eligibility/supersession/obligation/integration siblings; N1-N6 | Closed by acting/enactment/rid plus gate minimum and explicit qualification/owner routes; no prospective per-consumer projection remains. |
| 575dc78 B1; N1-N7 | Closed for multi-holder/frame aggregation, floor link, frame declaration, S11 scope, representation/accounting and named discriminators; disclosed costs remain costs. |

### 5.3 Representation, matching, scope and revising-duty findings

These findings were re-derived through their actual current consumers: effect-keyed write scope, current/execution basis, both matching polarities, floor/class, validity, run-aware gate/acceptance, discharge and inspector. The following N ranges close their concrete design/wording defects; any empirical or stakeholder item within a range remains a disclosure rather than an observed success.

| Review / findings | Disposition and mechanism |
|---|---|
| 5c55d4b B1-B2; N1-N7 | Closed: no identical-tree unbounded reproduction shortcut; region comparisons ignore positional shifts; gate frame/tenure/accounting and partial-SD-17 cost are explicit. |
| 27ef339 B1-B3; N1-N7 | Closed: width-independent adverse `link-`; innermost changed bytes plus every affected entry-mode owner; gates declare candidate frame; record-only whole-tree term and owner revalidation route explicit. |
| 0b6c4fa B1-B2; N1-N7 | Closed: UNBOUNDED supports no permissive match and is conservative for floor/class; no isolated valid-only tenure filter; no earlier decision fallback. |
| a18b544 B1-B2; N1-N6 | Closed: observed reads never bound a closure; fallback includes ignored tracked paths; no independent qcap identity; single representation and gate minimum; costs remain disclosed. |
| e9e6e9f B1-B2; N1-N5 | Closed: byte-exact runners without fallback; LFS external pins, gitlink reads, empty/type/mode ownership; cap cannot disappear with a qualified decision's ordinary currency. |
| e2154ac B1; N1-N5 | Closed: Git-entry representation shared by hashing, write set, mapping and every runner; anchor classifier/resolver agree; prospective-run and absence/incidental-read costs explicit. |
| 3540d98 B1-B4; N1-N4 | Closed: exact content/type/mode; complete locator/pin/attribute comparison; qualified gate propagates through minimum; equal conflicting regions become ABSENT; named precision and qualification limits retained. |
| 798b2b4 B1-B4; N1-N8 | Closed: admitted-only predecessor display; run is universal target condition; lineage/region predecessor inputs not positional; every traversed symlink plus target recorded. |
| 71cf9b3 B1-B2; N1-N8 | Closed: run rather than predecessor equality; validity/readiness/discharge share it; supplied seed, links, absent declarations and qualification scope explicit. |
| 86ab683 B1; N1-N7 | Closed: assessment record must count in the run, with status and continuity; per-subject slots/display and native-kind scope; retained costs as above. |
| 1ffbbf0 B1-B2; N1-N7 | Closed: free seed is an attribute, unobserved outside reads fail closed, target-based revising condition precedes every passing native D1/D2 acceptance/gate. |
| 53669a5 B1-B3; N1-N9 | Closed: class of recorded free attributes, acceptance/gate order, intake targets independent of timing; cross-domain routes, declaration-key merge, resolver-result distinction and path quarantine explicit. |
| d837363 B1-B4; N1-N8 | Closed: environment variation only permissive, pure pinned byte resolvers, by-value start context, effect comparison against current head and target-keyed revision assessments. |
| cc005db B1-B3; N1-N8 | Closed: effect-keyed write set covers governance boundary/member/semantic effects; frozen system semantics; separate product-scope acceptance record and veto. |
| c6da678 B1-B3; N1-N12 | Closed: external inputs do not narrow adverse matching; review reach not item-revision keyed; manifest semantic/structural effects reach their real domain owners; exact targets, residual identities, local refs and disclosure routes explicit. |
| b595f2c B1-B4; N1-N8 | Closed: region-level frozen recording, ref locality, documentation domain boundary, non-voting adverse judgments with result carrier; machinery completeness, nondeterministic analyzer outputs, analyzer set and author scopes explicit. |
| 6ff4ed1 B1-B4; N1-N12 | Closed: implication by construction; prose byte identity in tightening; pinned analyzers; AUTHOR/DOCUMENT obligation/role route; schema/consultation/report supersession, witness-owned provisional check, CHALLENGES exclusion, doctrine/transfer/O1 coverage. |

This is a bounded family-level reconstruction, not a claim to have replayed every historical candidate or every original review's investigation. The individual finding ranges above are reconciled through current mechanisms; historical conclusions and later reviewers' “closed” labels were not substitutes for those mechanisms. No previous runtime result was upgraded by this table.

### 5.4 Phase B §3 and N1-N4

The preserved closures were checked in both directions: immutable observations and explicit supersession; existence-keyed adverse scope with admitted/frame anchors and monotone home; no disposition by provenance change, retirement or ordinary peer PASS; starts through admitted-obligation lineage; dual reading keyed on outcome and reading; no absorption-only reading shortcut; candidate-own class rule; authorized independent dispositions; no loss/override/open-counter effect that erases revocation; salvage only after each never-lost record's own authentication/schema/reference checks; source/destination structural freezes; pre-acceptance frame existence and exact enactment binding; publisher settlement and known-loss continuity.

For Phase B N2 specifically, a differing old-content run or yielding current-content run on an alternate tree differing only outside a recorded narrow region remains in (2)/(4) when completeness becomes P, blocked, revoked, superseded or loss-withheld: `on-` reads frozen terms, and `link-` only adds adverse matches. The same changes can remove a permissive reproduction/current observation from (1)/(3). Restoring completeness cannot hide the contrary run. In the restrictive direction, an earned dual reading covers the identical outcome after a content change while the reading remains fixed; a revert yielding the failed outcome restores qualification; a genuinely new outcome needs another reading. R2/R3 supply explicit all-F SCC handling and authenticated-corrupt-prefix halt before current presentation.

Phase B N1 remains historically open (N3 here); N2 is closed at the architecture-design level with required future real-owner cases; N3 remains the diagnostic/reader-quality limit; N4 remains empirical cost/applicability uncertainty.

## 6. Out-of-matrix trajectories and sufficiency

The surviving trajectory is B1. The following additional attempts held against the current operative rules:

- **Plan order:** chains, incomparable branches with a common tighter current revision, fresh peer acceptance of current/tighter revisions, original and reverse admission order, and multi-item rejection. The same-name or common-current reach vetoes; no acceptance-count or fresh-judge exemption survives.
- **Plan resolution in both directions:** independent rejecter/owner exact-target relief permits a genuine cure without accepting the old rejected revision; a peer, wrong target, unknown lineage, blocked/provisional reliever, pending unrelated frame or loss-withheld reliever does not. After revert below rejected controls, the earlier acceptable revision is reusable; later re-tightening is reached again.
- **Equivalence/completeness composition:** indirect and converging chains, reversed objection endpoints, covering versus non-covering classes, provisional hops, singleton covers versus a large-scope INCOMPLETE, analyzer declaration versus human objection, different membership/member revisions and unrelated units. Asserts mirrors base except veto; independent requirements apply outside the change request and to both endpoint authors.
- **State/enactment:** pending supersession cannot remove admitted rejection or qualification; abandoned and replaced-task frame records never become permissive through a later iteration; clean rebases retain one enactment only while entries/structure hold; partitions and re-dispatch are separate; second integration is refused. Adverse frame records are the explicit exception (N1).
- **Runs/cutover:** unchanged gated subject retains admitted run; changed/restored/re-identified native D1/D2 subject obtains a new event identity; prospective run is known before integration; late/wrong-kind/duplicate cutover records are refused; mode transition cannot be enacted after an already completed carrier.
- **Representation/partition:** binary/line-ending/type/mode changes, empty files/gitlinks, symlink retargeting, anchor-looking string data, equal and crossing dynamic regions, non-cascading ABSENT and byte-preserving refinement. The one representation or fail-closed region result prevents the earlier bypasses.
- **Publication/currentness/loss:** paused publisher versus fence, fence chains, human decision only after settlement, losing ledger CAS, single provisional entry, stale-consistent product/ledger restore, withheld relaxers and restrictive adjudications. Quorum/currentness are outside derivation; loss cannot make retained passing evidence current through agreement of bytes alone. VM-image duplication, ABA and loss beyond all witnesses remain declared limits.
- **Roles/floors:** principal cannot accept its amendment; unknown-lineage support does not answer independence-requiring work; refusal keeps adjudication dispatchable; low-class counter-adjudication is refused; reports persist by existence and floor attention needs a human decision; qualified gate remains P through descendants and inspector state.

These are deductions from the candidate, supplemented by the diagnostics below; they are not observed production SSDS executions. Search stopped at high-information sibling closure rather than implementing another model of the whole architecture. Discovery was not stopped because of a review count or a desire to produce a PASS.

## 7. Minimum architecture, inheritance and PEM capability transfer

The four primitives remain sufficient representations of the governed concepts; derived graphs, working state, obligations and views are not new canonical stores. Admission owns all canonical appends/publication; Dispatcher operator state does not determine derived governance. The ledger, content store, witness checkpoints, derived cache and private operator state have distinct necessary roles. R4 removes a durable attempt log; R5 avoids maintaining a mutable partition repair registry. The single disagreement owner and the table reduce competing definitions. B1 calls for changing an existing selection predicate, not adding machinery.

The parent §18 capability inventory and frozen Architecture 1.6.0 were compared to §26's transfer decisions. Relation/layer/SDG fidelity, declared analyzer blind spots, basis-local invalidation, immutable accepted judgments, item-local planning, deterministic explainable version-bound context, integration beyond textual merge, direct isolated workspace edits, incremental/full equality, structural history, artifact trust/intake, progressive migration, top-down authority acceptance, scope conservation, pinned legacy work, publication/recovery, and private telemetry all have replacement or preservation routes. Frozen Core remains standalone and is not subordinated to SSDS acceptance. There is no implemented Tracker/Adapter/Scheduler state to migrate; their required functions still have owners.

PEM was activated for mature replacement and recurrence. Project policy designates main as the integrated publication line, while the workplan binds its exact integrated base. `main` independently resolves to that base; the candidate's PEM blob is byte-identical and no branch overlay is present. Its internal older candidate-overlay wording is retained historical file content, not evidence of an SSDS overlay or self-ratification. The validator confirmed schema/publication-route consistency using the original Git object store. Coverage is PARTIAL and does not cover all later 7.x history.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen version-bound resources required through the governing versioning owner; not through PEM frequency.
  - id: DS-001
    disposition: APPLICABLE
    reason: Diagnostic and structural checks cannot close assembled Manual or production-owner adequacy.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy for canonical owners and regenerated views, not a required historical mechanism.
  - id: SP-002
    disposition: APPLICABLE
    reason: Evidence-only self-reference-safe entries/checkpoints and descendant publication.
  - id: FF-001
    disposition: APPLICABLE
    reason: Evidence-only validation before genesis/replacement immutable publication.
```

All five canonical metadata records were searched, regardless of summary temperature. PC-001's old recorded owner binding was independently remapped for this task to the governing 7.2.1 versioning owner's “Capability preservation across versions”; §26.4/§28 preserve it and the unchanged-tree check corroborates current non-mutation. DS-001 informs §31 real-owner boundaries and this Review's model criticism; SP-001 maps to regenerated S3 views; SP-002 to references to earlier commits and external witness checkpoints; FF-001 to validation-before-genesis/lineage publication. Required runtime acceptance remains G3/G4. No PEM entry was updated or promoted, and the uncovered history was not treated as absence.

## 8. Qualification-design adequacy

The §31 program names production owners/consumers, deterministic failpoints, seeded negative discriminators, ledger-only replay, full-versus-incremental comparison, actual role/envelope admission, scientific reading quality, live usability and doctrine measurements. It correctly places runtime implementation evidence at G3/G4. G1 cannot be withheld merely because the system it would authorize is not implemented.

The judgment model now distinguishes the earlier direct, composition, nonind, class, frame, plan-coverage and relief defects. Its generic reach and per-kind oracle are different calculations, but share the meanings of claims/denials and several S1/acting/independence helpers. It samples two reference-respecting orders per case, fixes authorship, has at most one resolver, and omits plan objectives, brief rendering, qualified gate values, integration transitions, loss boundaries, request structure and real assessors. All-green output can therefore coexist with B1; the Manual expressly says brief carry is not modeled. This is DS-001's limit in a concrete case, not a reason to discard the useful diagnostic.

Section 31.6(V)'s new brief case edits the **item's** prose, so its item revision changes and the deficient selector passes it. Add B1's objective-only and unchanged-item sibling to the same real-owner Interface qualification group. No universal prose-semantic validator or new testing service is warranted. Neither the green routing tests nor the old S1 model observes this boundary.

## 9. Doctrine-realization map and O1

The governing seven entrypoints were inspected at the public-source commit, using their generated expanded entry contracts/scientific checks to check what §29 promises. The common kernel and scientific duties, four domain contracts, documentation ownership/reader duties, maintenance-audit conclusion/routing and hygiene's conservative boundaries have E0/E1/E2/E3 routes. E0 is limited to typed facts, authorization, presence/routing and boundaries that machinery can actually enforce; semantic adequacy, detection, truthful interpretation, recognizing an upstream defect, independence quality and scientific reader judgment remain E3. Required slots do not establish the truth of their contents. B1 limits the asserted mechanical completeness of the plan-brief projection, not the feasibility of the whole doctrine map.

Section 0.5 states the material admitted record and bases; native scientific homes versus retained canonical outcome objects; intended stakeholder/reviewer/agent readers; routine authority/evidence/provenance questions; retention and the confidentiality exception; canonical/derived linkage, drill-down, restart, pending execution visibility and privacy boundaries. Query/read, task/gate briefs, conformance, inspector/digest, historical views, export and tool-independent canonical JSON inspection are visibly marked within the requested architecture. No beyond-deliverable product surface is declared. I found no additional unmarked scope extension. Technical Review accepts no product item beyond the deliverable; such an item would still need the stakeholder/task scope owner's acceptance.

## 10. Verification, exact evidence and limits

| Check, executed on pinned candidate unless stated | Result and claim limit |
|---|---|
| Full clone / branch / candidate and four subject blobs | Not shallow; named branch; all handoff blob identities match. |
| Release state | Governing 7.2.1 public source/recovery match the handoff; no source adoption inferred from branch position. |
| `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` | **4/4 PASS.** Routing/frontmatter/lineage checks only. |
| `git diff --check 83a82df69555b3a5817799455d6e51e1ffdd80af d6734c48ad3b3b4411ab84b50b850f4965da257c` | Exit 0, no whitespace diagnostics. |
| `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 bf2337285dfdaba5d535e73cf76af3d5b78978f0` | Inspected: 73 files, 23,269 insertions, 1 deletion; includes Manual, reviews/handoffs/model/coordination. This is the specifically requested historical interval, not the final candidate's entire delta. |
| Frozen architecture plus all `source/` and `dist/` against fad3ee4 through d6734c4 | No changed paths; byte-unchanged. |
| PEM validator in the archive, original `GIT_DIR`/candidate `GIT_WORK_TREE` | **PASS:** schema 1, 5 families, 0 notices. Accepted-base and candidate PEM both resolve to blob 1561797…; no SSDS overlay. |
| `python3 -I qualification/ssds80/s1_disagreement_model_check.py` | **PASS:** 1,574,464 transitions at default depth 4, zero failures, all 80 named discriminators pass. This unchanged Phase B diagnostic does not model the new brief rule. |
| Judgment-disagreement `--mutations` workload, split by `run_family`/MUT into independent processes as the handoff permits | **PASS:** all 31 expected family/variant jobs completed; four unmutated families have no failures; all 25 mutations caught. No candidate model code was edited. |

Judgment-model unmutated scenario counts: transformation-review/acceptance/gate **789,396**; equivalence-chain **299,760**; completeness-cover **37,600**; plan-coverage **75,945**; total **1,202,701**. Including mutation family re-runs, **10,374,149** scenario evaluations were executed; that is not a count of independent experiments or scientific variants. Raw diagnostic output/results are scratch artifacts at the directory named in the header; the durable evidence summary and claim limits are this record. Execution used the candidate modules, not an owner replacement, and the archive's Git-dependent validation used the original repository object store.

I did not run production SSDS, witness/host failpoints, actual plan-brief rendering, runtime Admission, real scientific assessors, live harnesses, scale/usability studies, statistical doctrine qualification, shadow implementation or cutover. They do not exist as candidate G1 execution evidence and are not claimed passed. B1 is a source-level conforming-renderer counterexample, not an observed production bug. The prior depth-5 S1 result remains prior-session-reported with missing original provenance; it was not re-executed or upgraded here. No package rebuild or source acceptance suite was needed for this review-record-only mutation.

## 11. Scientific checks

- **Findings:** B1 is the material D3 finding; N1-N3 preserve precision, acceptance and evidence limits. No material scientific-result finding was found, and no scientific claim was evaluated from realized data.
- **Realized results:** produced, ran or reviewed no realized scientific results. The local runs above are software predicate diagnostics. The review artifact prepares technical G1 evidence: its examined envelope is pinned Manual/parents/owners, identified prior-finding families, transfer, doctrine/O1 and the specified diagnostics; its materially unexamined envelope is production behavior, empirical reader quality, cost/scaling and live qualification. Materiality follows the explicit G1 contract and paths to missing review inputs, false closure or authority misuse. No delegated-return gap exists; no reviewing agents were launched.
- **Variants:** one unmodified candidate. The prescribed judgment-model workload evaluated one base rule variant and 25 deliberately defective variants, over four model families (31 family/variant jobs). All were retained in the accounting; selection criterion was detection of the named invariant failures, not selection of a favorable design. The unchanged default S1 transcription was also run. No scientific model, dataset, preprocessing, parameter or held-out selection was performed. Earlier author search is not bounded by these local counts and is not claimed independently reproduced.
- **D1/D2 tensions:** no accepted project D1/D2 scientific/numerical authority was used to warrant a consequential scientific judgment. The relevant governing owners are protocol/D3 authority; a project D1/D2 native-issue tension search was not triggered. The historical adoption-provenance gap remains explicit rather than reported as none.
- **Choices/retention:** no product/scientific pipeline, retention or projection contract was changed. The only durable addition is this authorized review record; it does not amend accepted authority or memory.

## 12. Common-mode dependencies

The reviewer is of the **GPT family**, engaged directly by the stakeholder, and did not author this candidate. The Manual author and most prior Manual reviewers are of the **Claude family**. The Phase B reviewer and the 3540d98, different-family b46c250, 9e5a763 and a6ed164 reviewers are of the **GPT family**; those records are not independent-family corroboration of this Review.

The issued handoff, current corpus, inherited workplan framing, prior review records, diagnostic claim definitions, Git snapshot/toolchain and project-memory lessons are shared dependencies. Fresh context and a different family from the author improve process diversity but do not establish epistemic independence or a probability of completeness. The concrete source-level brief counterexample is stated so another reviewer can falsify it without accepting this reviewer's framing.

## 13. D4 statement

**SSDS 8 D4 remains NOT AUTHORIZED.** This record neither accepts the Manual nor closes G1. Repair B1 at the existing brief owner, specify the objective-only/unchanged-item discriminator, obtain affected independent Review of the new exact candidate, and obtain explicit stakeholder G1 acceptance. G2 then separately requires a reviewed shadow D3-to-D4 workplan and explicit shadow authorization. G3 runtime qualification and G4 per-subject cutover remain separate boundaries. No live campaign, publication, commit, push or accepted-current promotion was performed.

## Governing owner locators

All following routes are at `aaeaf8b6b2121b9fb8aba31917c8265649c43954`; the root release-state check independently bound that commit. These are exact owner locators, not floating branch authority:

- `source/roles/software-design/SKILL.md`, expanded at `dist/skills/software-design/SKILL.md`: entry/version contract, D3 contract, Review/Challenge and scientific checks.
- `source/shared/references/architecture-and-design.md`: “D3 formal-contract discipline,” “Review and Stabilization,” “Mechanism-to-capability transfer,” “Realized-record architecture (O1).”
- `source/shared/references/abstraction-and-concretization.md`: feasibility, authority/Challenge and Lossless Representation Rule.
- `source/shared/references/workflow-and-workplans.md`: “Decision-sufficient handoffs and working state,” “Review, Verification, Stabilization, and Audit,” “Human gates and closeout learning.”
- `source/shared/references/evidence-evolution-and-dependencies.md`: “Applicability, immutable observation, and superseding assessment,” “Assessment disagreement,” bounded absence and evidence independence.
- `source/shared/references/semantic-definition-and-traceability.md`: “Definition order and well-definedness,” parameter/default binding and Review reconstruction.
- `source/shared/references/convergence-and-cycle-economy.md`: “Active simplification trigger,” “Review readiness and independent review sufficiency,” “Review strategy after recurrence.” No count forces acceptance.
- `source/shared/references/testing-and-validation.md`: “Evidence classes and claim scope,” “Proxy-proof real-owner evidence,” required-check and oracle-integrity rules.
- `source/shared/references/project-engineering-memory.md` and `project-engineering-memory-schema.md`: exact integrated base, overlay, canonical metadata/HAS, binding and publication discipline.
- `source/shared/references/storage-and-io.md`, `concurrency-and-orchestration.md`, `security-and-trust-boundaries.md`: real-owner failure/recovery, effect and trust boundaries, retention before irreversible loss.
- `source/shared/references/protocol-versioning-and-compatibility.md`: “Capability preservation across versions,” explicit binding/adoption and distinct Review/ratification/publication.
- `source/shared/references/scientific-inspectability-and-initiative.md`: O1/O2/O3 and gate/report/product-scope distinctions.
- `source/roles/{scientific-formulation,numerical-algorithm-design,software-design,software-implementation}/SKILL.md`, `source/specialists/{software-documentation,software-maintenance-audit,repository-hygiene}/SKILL.md`, `source/shared/fragments/scientific-checks.md`, and their `dist/skills/*/SKILL.md` expansions: doctrine-map source, not additional domain activation for an unrelated scientific problem.
