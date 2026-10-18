# Independent D3 Review — SSDS 8 Architecture Manual, candidate f044820

    GOVERNING SSDP:    7.2.1
    REPOSITORY:        hjin98/scientific-software-development-system
    BRANCH:            ssds-8.0-graph-native-architecture
    CANDIDATE:         f04482003cc46e8bf0d1fddd0cff3099e85e7c5f
    SCOPE:             proposed architecture-level Manual; revision-24 workplan delta;
                       catalogue C.1/C.2 and bounded realizability, inheritance and assurance checks
    MANUAL:            orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB:       b3958a4a3e1e8a7292557b81638573dae3f7a14b
    PARENT WORKPLAN:   workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
                       revision 24; blob 2e1afae196e70d51a98c3daeb1aa2ff22f3be4b6
    PHASE B CANDIDATE: e23f14208be869e6a78cfd7b312e447254ee1851
                       revision 23; blob 610f373b97fb8152d2a5742e17fa172e12204756
    CATALOGUE BLOB:    c73c8c6fa245a76dfe2b34fa7b92d332d0f83bb5
    CLOSURE MAP BLOB:  8d694a726168ba8d32c08dc1093b1c3e4c9d1097; review aid only
    PUBLIC SOURCE:    aaeaf8b6b2121b9fb8aba31917c8265649c43954
    RECOVERY:         efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS:    9431629 B1/N1-N4 and the closure-map lineage; hypotheses only
    REVIEW METHOD:    immutable-owner reconstruction; bounded Challenge and out-of-matrix passes;
                       semantic trajectories and cheap siblings; exact-candidate diagnostics
    REVIEWER:         GPT family; engaged directly by the stakeholder through the named handoff;
                       AI asserter of this record; no delegated reviewer
    MUTATION LIMIT:   this review record only; no implementation, commit or push

The issued handoff is `qualification/ssds80/MANUAL-REVIEW-HANDOFF-SSDS-8.0-F044820.md`. The checkout was at `519574c7566e8dc237b3f35d4ebf2c433c0b9118`; it was not substituted for the candidate. Reads and executions used a full `git archive` of the candidate under `$TMPDIR/ssds80-manual-review-f044820/candidate`. Governing owner reads used the public-source commit above. Root `PROTOCOL-RELEASE-STATE.yaml` independently confirms the accepted-current 7.2.1 public-source and recovery identities. All four candidate blobs above match the handoff.

## SERIOUS CHALLENGE

None against accepted governing SSDP authority or the revision-24 level assignment. Architecture-level G1 and executable mechanism closure at G2 are a defensible division. B1 is a contradiction and unauthorized generalization in the **proposed Manual's independence decision**, requiring D3 repair before acceptance. It does not require weakening the accepted independence requirement or restoring the old mechanism-level G1 bar.

The accepted workplan's special owner disposition of a failing assessment is preserved as the explicit baseline. This review does not challenge that bounded exception. It challenges the Manual's extension of the exception to independent review and acceptance generally.

## Verdict

**NO-PASS. One G1 blocking family: B1 — author-owner substitution for independent judgment.** Section 5.10(f) lets a content author be admitted as independent under its general owner exception. That conflicts with §5.10(h)(9), A5, the independent-review requirement, and the narrower parent exception. A correct implementation of the exception can therefore discharge a review using the author of precisely the content being reviewed.

This is a defect of an architecture decision and authority boundary under workplan §25 criterion 11. It is not a catalogue counterexample, a demand for G3 evidence, or an objection to the level split. The retained-output cases that defeated candidate 61 are addressed at the architecture level by the new work-in-scope rule; their catalogue implementation remains RR-1/RR-2.

The review is bounded technical evidence for G1 only. It accepts no architecture, revision-24 workplan, default or product scope. Later-gate evidence is not treated as missing G1 runtime evidence.

## G1 blockers

### B1 — The general owner exception permits the author to count as the independent judge

**Classification and earliest owner.** G1 blocker; proposed D3, Manual §5.10(f), composed with (e), (g), (h)(9), §3.5 and §8.3. Family: **independence lost by replacing an independent judge with the judged content's owner-author**. Workplan §21 items 3, 23 and 27 are affected. The exact judged-content set can be completely correct: this failure occurs after its authors have been identified correctly.

**Exact owner text.** Manual line numbers below refer to blob `b3958a4a3e1e8a7292557b81638573dae3f7a14b`.

- §5.10(f), line 495, first applies the independence requirement to “every review, conformance, acceptance and plan-acceptance judgment” and the other listed kinds. It then states: “**Owner exception:** where policy names no qualified human outside the authors, one of them may act as owner, admitted as independent with the common-mode dependency recorded and shown.” It states no restriction to failing-assessment dispositions.
- §5.10(h)(9), line 509, requires: “no actor among the authors of `W(j)` is admitted as an independent judge of `j` (A5, A9).” This directly contradicts the exception on its stated domain.
- §3.5 says: “No actor reviews, accepts, conforms or plan-accepts its own work (A5; §5.10).” A5 in §0.4 says “no actor reviews or accepts its own work.” Workplan §2.5 A5 has the same prohibition.
- The parent workplan §6.6, **Decision class and independence**, line 1382, says: “Where policy names no qualified human other than the claim's author, that author may **dispose as the claim's owner**”. Its subject is dispositions of failing assessments. Parent §6.8 step 3, line 1423, introduces its human exception with “for a **disposition** by an authenticated human”. Those clauses do not authorize self-review of a transformation, an integrated result, a contract or an architecture.
- At governing public source `aaeaf8b6…`, `source/shared/references/workflow-and-workplans.md`, **Review, Verification, Stabilization, and Audit**, requires: “Review independence means the reviewing context did not author the candidate and does not inherit author conclusions”. `source/roles/software-design/SKILL.md`, **D3 design contract**, item 7, requires “independent falsification before accepted-current promotion”. Recording common-mode dependency does not make the author a non-authoring reviewer.

**Concrete trajectory: owner relief of a transformation review.** All content authorship is known; no unknown-lineage inference, false attestation or compromised credential is involved.

1. Human H produces content `u1` in candidate transformation X. Its work and scope give `W(REVIEW(X)) = {u1}`, whose admitted producing actor is H. The plan, contract, conformance and required evidence are otherwise sound. X's frame exists.
2. Independent reviewer R records `REVIEW(X) = NO_PASS`. This is a standing adverse judgment, and the judgment obligation is answered adversely. Policy names H as the domain's owner for adjudication and names no qualified human outside the authors. Such a policy satisfies the stated precondition of §5.10(f)'s owner exception; the Manual does not require an outside human to exist.
3. H supplies a passing review on the **same exact target**, explicitly superseding R's adverse judgment as the owner's adjudication, route 2 of §5.10(e). H records the common-mode dependency honestly. H has the required class and all basis entries hold. This is an authenticated human record; it does not require the Dispatcher to launch H as a supposedly fresh agent reviewer.
4. Under §5.10(f), H is **admitted as independent**, despite H being the known author of `W`. Admission §8.3 step 3 delegates independence and supersession authority to that section. Step 7's refusal of later answers expressly excepts an authorized supersession. There is no missing target, stale basis, scope breach, class failure or integration-window mismatch.
5. Under (e), the adverse objection ends. The passing review is not `nonind`, so §5.5 gives it no independence-related `F`; it can be current in its acting state. Under §10.3–§10.4 it can supply the passing judgment and discharge the review when the remaining terms hold. On integration it acts in the admitted state.
6. Thus a review of H's own `u1` supplies independent closure. Reading (h)(9) literally forbids step 4; reading the named exception as overriding it permits step 6 but violates A5 and the upstream independent-review requirement. A mechanism cannot resolve that architecture-level conflict by choosing a schema or evaluation order.

No failing assessment is being disposed of in this trajectory. Its authorization cannot be obtained from the parent's narrowly scoped owner exception. Human authority to decide an issue is distinct from whether that decision constitutes independent falsification.

**Cheap siblings and controls.** I checked six target/kind variants of this same author-owner substitution: transformation review, subject-triple review of authored D3, item-level integrated-result review retaining the author's output, joint-invariant integrated-result review whose changed content the owner authored, `CONFORMANCE`, and `PLAN_ACCEPTANCE` of the author's contract. The generic (f) exception reaches each; none needs a defective computation of `W`. The literal conflict with (h)(9) is shared. Transformation review above is sufficient for the verdict; these are sibling analyses, not six independently executed defects or historical recurrences.

Three controls delimit the finding: a qualified non-author human remains eligible; an agent of unknown lineage remains non-independent; and the parent's specifically authorized human-owner **disposition of a failing assessment** is not this bypass. Human gate decisions and product-scope decisions have their own declared holders and are not asserted to require an independent reviewer by (f).

**Minimum repair direction.** Keep the common judged-content and provenance owner. Narrow the owner exception to the owner decisions its governing contract actually permits; do not classify authorial review as independent falsification. Distinguish an accountable owner disposition from satisfaction of an independent-review obligation. Reconcile (f), (h)(9), §3.5, A5 and the affected doctrine claim once at their real owner, with local routes elsewhere. Where no independent judge exists, keep independent closure unavailable rather than treating a common-mode disclosure as independence. No new registry, retained-set field or target-specific patch is needed.

**Required discriminator.** At the architectural/model boundary, construct known authorship and a policy with no qualified outside human. For all six variants above, the content author must be unable to satisfy independent Review/acceptance/conformance or to end its objection through a self-review presented as independent. In a separate positive case, preserve the narrowly authorized owner disposition of a failing assessment, with the required class and visible common-mode dependency. Also retain ordinary non-author and unknown-lineage controls. At G3 exercise the actual Admission and discharge consumers; a model-only result does not qualify them.

## Register entries for G2

These are **not additional G1 blockers**. B1 must not be placed in this register as though it were merely an implementation question.

| Entry | Review disposition and required continuation |
|---|---|
| RR-1 | Confirmed open mechanism issue. The history probe reproduces latest-delta omission of retained authors. The Manual's work-in-scope decision covers empty, partial and all-empty re-dispatch, kept/replaced partition parts, same-key copying and current replacement producers. G2 must implement that construction at the real item-result consumer. |
| RR-2 | Confirmed open. Catalogue `retained`/`J` and `STALE_RETAINED` must be reconciled with the Manual's scope-limited, target-fixed `W` and integration-support condition. Include same-key integrations inside/outside scope between issue and integration. |
| RR-2, additional discriminator | The transformation identity `(B,C,A)` does not itself name task, item-work key or write scope, while `W` uses those facts. Test two producing tasks proposing the same `(B,C,A)` with different scopes/work histories. G2 must bind one unambiguous producing context or prevent ambiguous reuse. A unique task-to-candidate binding can realize the architecture; this review does not show it impossible. Treat this as a mechanism identity-construction question, not a second G1 defect. |
| RR-3 | Confirmed open catalogue typing mismatch. The Manual's three target types and distinct integrated-result identities are architectural closure; the old target tables still need reconciliation. |
| RR-4–RR-8 | Confirmed carried questions. Identity-keeping R2 amendment, a no-change answer to coordination, unattributed item-level findings, a nonterminating pending candidate, and out-of-scope objections on masked/non-latest integrations remain named. The Manual keeps no-stranded-obligation and findings-survival requirements; G2 cannot claim these closed merely because SD-41 stopped the earlier prose loop. If closure requires changing those decisions, reopen G1. |
| RR-9 | The blanket historical replay obligation is present. This review did not replay every B/N finding from 61 rounds. That work remains explicitly open; the count is not adequacy evidence. |
| RR-10 | Confirmed. The diagnostic shares helpers and uses hand-chosen abstractions. Its core actor table describes O as an independent human owner, so it does not establish the safety of an author-owner exception. Add B1's discriminators after the architecture is reconciled. |

No known mechanism question examined in this review was found wholly absent from C.2's scope. This is a bounded completeness assessment, not certification that RR-9 has already enumerated and closed every historical finding. Catalogue C.1 correctly makes conflicts subordinate to the Manual and keeps G2 free to replace mechanisms.

## Non-blocking findings

**N1 — Changed-work keys require visible semantic review.** The prose/fixed-field reset is expressly disclosed in §5.10(b), §13.4 and §32.2: earlier retained content then lies outside the new work's `W`, and prior findings travel through the re-review carry. A prose amendment is R2 and requires independent plan acceptance; the re-review carries still-open findings on the same plan subject. This is a disclosed architectural limitation, not silently claimed persistence of the old work identity. Cross-plan copying with changed prose and no declared lineage remains outside a guaranteed content-key carry. Preserve that limit in G2/G3 cost and adversarial cases; do not claim universal semantic clone detection. No independent G1 violation was established from this case in the bounded pass.

**N2 — Closure-map detail remains an aid.** Several rows still describe candidate-61 `J`, per-kind entries and subclauses. Its new front rule explains the two-level reading. Use the actual Manual decisions and the register, rather than treating the old parentheses or `DECIDED` labels as architectural proof. Reconcile those details with G2's settled mechanism; no prose-quality pass threshold is proposed here.

**N3 — Full diagnostic evidence is not supplied by this review.** The handoff permits at least core and review-scope execution; the complete `--mutations` command required by Manual §31.10 was not run here. This review supplies only the executed coverage below. Before claiming all G1 document checks complete, identify applicable exact-candidate evidence for the remaining workload or execute it. This gap is not recast as a G3 requirement and is not the basis of B1.

## Workplan revision 24 and the G1 bar

**Sound level assignment, subject to stakeholder acceptance; no Serious Challenge to the revised bar.** I compared the revision-24 delta to `94316298ba0d40831560591c2d2385544b93ea42`, and checked it against stakeholder decision record item 43, including “Try A B C.” The delta is the declared disposition/§0.1/§21/§25 change plus its lifecycle metadata. The Phase B candidate remains identified separately.

The public-source D3 role requires freezing material architecture and delegating replaceable machinery. The convergence owner, **Active simplification trigger**, requires re-derivation before another additive repair; **Finding routing and revision economy** says escalation changes the method, “not the pass threshold.” Revision 24 follows that distinction if applied literally: an inadequate decision, omitted invariant or unrealizability remains G1-blocking; defective catalogue machinery remains open until G2. B1 exercises the architecture side of that boundary. Calling it RR-9 would weaken the bar; this review does not do so.

The authorization sequence is satisfiable without production SSDS evidence at G1: document reconstruction and design diagnostics now; a bounded shadow workplan and executable design models at G2; production-owner qualification at G3; per-subject cutover at G4. Models used to settle a design are diagnostic design evidence, not permission to implement native authority before G2. Criterion 13 must not be read as requiring the production shadow system before authorizing its implementation. The existing “no D4 work ... before G2” boundary remains in force.

The revision remains **proposed**. Technical support for the level assignment does not ratify it, its defaults, its product scope or this Manual. SD-47 does not authorize changing the independence threshold.

## Architecture-level closure audit

I checked the workplan's §21 clauses against the actual Manual sections, using the map only as a retrieval aid. Except for B1's inadequate/conflicting independence decision, **no omitted architecture-level decision was found in this bounded audit**. This is not a blanket mechanism or historical-findings clearance.

| §21 item(s) | Actual architectural decision/owner assessed |
|---|---|
| 1 | §1: manifest-only structure, effect-keyed write set, pure scopes, partition, identity, quarantine and tenure |
| 2 | §2: directed typed roles/cycle classes, adoption checks, SDG legality and boundary completeness |
| 3 | §3 and §5.10: closed kinds/tiers, qualifications and target typing; **B1 prevents closure of independence** |
| 4 | §4, §6.3 and §17: basis modes, mechanical minima principles, shared execution record, classes and widening |
| 5 | §5–§7: strata, support clamp, failure start/stop, deterministic frames and one-use prospective acceptance |
| 6 | §8 and §21–§23: sole writer, validation responsibilities, quorum commit, publication reconciliation and fencing |
| 7 | §10: readiness, current-state discharge, provisional scope and routes; RR-4–RR-8 remain mechanism questions |
| 8 | §11: item-local acceptance, objective basis, invariant lint and mandatory whole-plan amendment review |
| 9 | §9: scheduling advisory, admission-time reliance validation, generated ownership and integrated joint review |
| 10 | §16: logical operations, compiled duties, typed query status, read recording and gate evidence core |
| 11 | §6 and §17: fixed/free execution attributes, ensemble assessment, runner custody and observation boundary |
| 12 | §18: absorption versus proposed import, static classification, structural adoption and no authority by presence |
| 13 | §19: modes, exact legacy scope, refinement/promotion, prospective cutover and quiescence |
| 14 | §21–§24: reachable ledger content, witness assumptions, loss boundary, accountable continuity and breach choices |
| 15–16 | §25: authenticated actors, protected surfaces, lifecycle-only trust/rules changes |
| 17 | §26: seven component owners, dependency direction, single composition root and explicit 1.6.0 transfer |
| 18–20 | §20 and §27–§28: pins, external consultation, evolution and distinct version dimensions |
| 21 | §16, §17, §19 and §29: doctrine inheritance, native/legacy version routing and scientific duties |
| 22 | §30: capability-bearing primitives/stores and simpler alternatives, with empirical claims withheld |
| 23 | §12 and §5.10: role separation and lineage; **B1 prevents independent-judge closure** |
| 24–26 | §13–§16: contracts, verifier coverage, conformance force, reports/floors and human decision views |
| 27 | §29: doctrine map, inline remaining E3 duties and explicit detection limits; B1 affects its independence claim |

For §16.2, the 26 product-invariant rows have corresponding actual dispositions in Manual §26.4; its second table also disposes of the frozen architecture's detailed surfaces. In particular, formerly deferred composition, benchmark context, execution lifecycle, capability identity, containment, packaging/configuration, fitness and public-boundary choices are decided there. I found no still-deferred row routed only to the non-authoritative catalogue. Architectural preservation is not execution of Core/profile regression; those runtime checks remain later implementation acceptance.

## Refinements and SD-47

The following are architectural assessments, not acceptance of catalogue algorithms or stakeholder defaults.

| Refinement | Assessment |
|---|---|
| R1 | One recorded execution basis and adverse/permissive construction preserve the material polarity distinction. Re-resolution context and free attributes remain explicit; no new surviving architecture counterexample found. |
| R2 | Forcing nontrivial support SCCs to `F` is a conservative no-self-support decision; it does not establish the semantic adequacy of other rules. |
| R3 | Authenticated malformed prefixes halt current assertion rather than being partially trusted; unreadable versions stay distinct. |
| R4 | Per-incarnation, once-only publication plus fencing replaces a durable attempt log. Process/OS crash assumptions and the VM-snapshot/ABA residual are explicit; no architecture impossibility found. |
| R5 | Construction-time partition with `ABSENT` on nonlaminar observations preserves exclusive ownership; executable resolver details remain G2. |
| R6 | Scope identity binds declared subject terms rather than current bytes/partition. Term changes end tenure; refinement cannot manufacture acceptance. |
| R7 | Authored evidential `CHALLENGES` does not enter validity/warrant prerequisites; native home and inquiry status remain distinct. |
| R8 | Exact-target supersession and owner/author relief avoid peer overwrite and cross-target erasure. **Their independence predicate is defective under B1.** |
| R9 | Answered judgment obligations and persistent adverse vetoes distinguish a later pass from resolution. **B1 can falsely qualify the resolving judge.** |
| R10 | Tenure and native D1/D2 revision-run rules distinguish restoration from permission to reuse older judgments; revising assessments and gates bind the new run. |
| R11 | Minimum over eligible gate decisions preserves qualified decisions rather than selecting a later favorable holder/frame. |
| R12 | Acting follows one enactment and its clean rebases; a replacement task cannot inherit its predecessor's permissive authority. |
| R13 | A common independence owner is appropriate, but the general owner exception exceeds the parent's failing-assessment exception and contradicts its own author exclusion: **B1**. |
| R14 | Composition-sensitive adverse reach covers equivalence paths and completeness unions; work claims use the shared `W`, with exact-target relief. **B1 affects who may supply relief.** |
| R15 | Collateral evidence regression remains refused while judgment staleness reopens current-state obligations. The five unresolved routing realizations stay visible for G2, not silently passed. |

**SD-47 A.** The work-in-scope construction is one coherent selection principle across the three review target types, and §4.3 binds judgments to that content. It addresses the named 9431629 and SD-46 histories at the architecture level. Current producer substitution excludes the replacement producer rather than every historical producer; a same-key item outside scope and another item's untouched in-scope output do not broaden this work's authors. Drift does include the current producer of a previously changed unit. Cross-plan identical-key work is included; changed prose/fixed fields reset the key with the disclosed limits in N1. These are substantive decisions, not merely catalogue routes. **B1 survives after all of that selection succeeds.**

**SD-47 B/C.** Architecture-level G1 and a subordinate mechanism catalogue faithfully implement the requested method change. I independently compared the catalogue body from `## Part 0. Orientation` onward with candidate 61: it is byte-identical. Its C.1 conflict rule and C.2 closure boundary preserve replaceability without deleting obligations. A judgment supporting an integration only for the content it actually judged is a sound architectural staleness invariant; the identity/history and rebase realization remains RR-2.

## Out-of-matrix trajectories attempted

The distinction below is between semantic desk trajectories and executed diagnostics; none is production SSDS execution.

| Trajectory | Outcome in the architecture-level reconstruction |
|---|---|
| Known content author acts as the only policy-qualified owner and supplies independent relief | **Fails: B1.** Correct `W` and honest provenance do not prevent self-review. |
| Empty/partial/all-empty re-dispatch, replaced partition part and same-key cross-plan copy | Shared work histories keep retained content in `W`; original retained producers remain excluded absent B1. Catalogue construction remains RR-1. |
| A producer is actually replaced; same-key work lies outside scope; another item's untouched work lies inside scope | Current content/producers and scoped work avoid the three requested over-exclusion cases. |
| Same-key integration occurs between issue and integration | Changed judged content cannot be supported by the earlier judgment; refuse/new iteration. Exact retained-field realization remains RR-2. |
| Plan objective alone changes; one rejection names multiple items; controls tighten or become incomparable | Objective is in the acceptance basis; whole-plan review is mandatory for the named semantic amendments. Standing same-key rejections do not lapse by current revision order. No new architecture bypass found. |
| Equivalence diamond or provisional path; completeness assembled from smaller scopes | The objection reaches needed composing judgments, not merely a direct edge or exact scope; non-current hops do not supply reuse. |
| Replaced/pending enactment supplies an earlier pass, gate or disposition | Acting prevents permissive transfer to admitted state until that enactment integrates; adversity remains visible. |
| Restore old bytes after tenure end, or recur at an old D1/D2 revision in one tenure | New tenure/revision run prevents acceptance/gate revival; a new revising record is required for native D1/D2. |
| Restore product and ledger to matching stale snapshots while a later admitted checkpoint remains | Qualification refuses old currentness; continuing through known loss withholds retained permissive effects independently of matching bytes. |
| Crash between append, witness acknowledgment and publication; takeover; foreign return to base | Provisional heads do not authorize dispatch; successor observations reconcile publication; another incarnation fences. Late ABA publication is disclosed rather than claimed prevented. |
| Positive rerun after a counting failure; free seed variation; assessor disagrees on the same outcome/reading | No latest-pass disposal; variation remains adverse; one-record discriminating reading cannot assign both verdicts to the same outcome under one reading. |
| Foreign manifest edit, manual merge or imported whole-document acceptance | Presence cannot enact structure; foreign content produces quarantine/intake; whole-document acceptance cannot be imported onto a section. |
| Confidentiality purge or unknown active artifact | Human-gated retention weighing precedes irreversible purge; static intake does not execute artifacts. No purge was performed. |

The coverage is bounded. I did not prove every historical closure, enumerate the full state space, establish the feasibility of a particular deployment or exercise the future runtime owners. No additional accepted-authority counterexample survived the Challenge Pass.

## Minimum architecture and capability transfer

The four primitives retain distinct necessary roles: content/semantic identity, typed dependency, non-derivable recorded judgment/fact, and applicability. They do not duplicate a mutable workflow database. The component split keeps pure derivation separate from currentness qualification, admission and scheduling. The canonical ledger, witness evidence, derived caches, private operator journal and regenerable transports have distinct authority and recovery roles. Neither a graph database nor another workflow owner is justified by the examined requirements.

The minimum repair for B1 is **narrowing a permission**, not adding a new mechanism. Practical granularity, witness latency, retention, author-set breadth and re-dispatch churn remain empirical costs with reopen triggers; §30's preference is design rationale, not measured superiority.

PEM was activated for mature replacement. The designated integrated publication line is `main`; independently resolved local `main` equals the workplan's bound `af0455753e20ee54a969c844872e29e270007211`. The bound PEM blob and candidate PEM blob both equal `1561797125622f355f84eb27319f87e8fa4227d9`; there is no additional same-branch overlay. The historical metadata inside that integrated publication does not self-ratify a new overlay. Canonical metadata, not only the active summary, contains five families and no notices. Coverage is explicitly PARTIAL and does not establish absence of later lessons.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: Current 7.2.1 versioning owner independently requires frozen version-bound capabilities; Manual 26.4 and 28 preserve them.
  - id: DS-001
    disposition: APPLICABLE
    reason: Catalogue diagnostics and structural checks cannot establish assembled architecture or runtime adequacy.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy for one canonical owner and regenerated subordinate projections; not a required old mechanism.
  - id: SP-002
    disposition: APPLICABLE
    reason: Evidence-only support for self-reference-safe publication and distinct immutable identities.
  - id: FF-001
    disposition: APPLICABLE
    reason: Evidence-only support for validation before genesis or replacement-lineage publication.
```

PC-001's historical 6.5 owner binding was not treated as current force by assertion: I read the current public-source versioning owner's **Capability preservation across versions** and its frozen-artifact rule. The other four remain evidence-only. The bounded historical intake additionally covered the Phase-C handoff's uncovered-7.x warning, §29's 7.x doctrine rationale, the latest review family, SD-46/SD-47, catalogue preservation and frozen Architecture 1.6.0. It is not a new exhaustive historical census or PEM update.

## Qualification-design adequacy

Sections 31.1–31.3 distinguish structural checks, catalogue diagnostics, independent semantic review and production-owner evidence. The acceptance program carries derivation, failure/judgment disagreement, routing residuals, no-stranded obligations, persistence/failpoints, loss, custody, security, Core independence and live doctrine/usability measures to their appropriate gates. Required negative discriminators may be re-derived, not silently dropped. `HARD` template thresholds are proposed parameter bindings, not generic scientific truth.

The diagnostic cannot qualify B1: its actor table assumes O is an independent human owner, and its history probe checks producer selection rather than a policy exception allowing a correctly identified producer to judge. A green run is consistent with this blocker. G2 must model the repaired permission boundary, and G3 must execute Admission and discharge with the real owners. Do not promote synthetic cases or the existing Core to evidence for an unimplemented SSDS consumer.

No runtime qualification is owed at this G1 review. The fuller G1 diagnostic command and the unexecuted future groups remain accurately distinguished below.

## Doctrine-realization map and O1

I compared §29 with all four role and three specialist entrypoints and `source/shared/fragments/scientific-checks.md` at `aaeaf8b6…`, interpreting their shared entry contract through the canonical kernel/versioning owners. The map carries governing-version binding, earliest-owner routing, canonical-source loading, Challenge, evidence applicability, real-owner acceptance, simplification, specialist limits and scientific disclosures. Its catch-all E3 row depends on the actual entrypoint text being carried inline; it is not permission to omit an unlisted duty. Detection, evidence adequacy and semantic judgment are explicitly E3. **B1 prevents the claimed independent-falsification enforcement from being adequate.** No second blocking family was established in the map audit.

The O1 content in §0.5 states material records, retention and breach boundaries, source/projection linkage, readers and routine questions. The within-deliverable surfaces are the required query/brief/gate-core/conformance/inspector/history/export and tool-independent ledger views; no universal scientific observation store is introduced. §16.6 preserves disputed, stale, unavailable, adverse and missing evidence separately from the supporting premises; mere display does not turn a record into a currency prerequisite. Privacy-limited aggregates must state their limits.

No beyond-deliverable surface requiring a separate product decision was found among the examined marks. Technical D3 review would not accept one if proposed. This review changes no product retention or projection contract.

## Verification, provenance and limits

All candidate execution used Python 3.10.12 and the archived candidate, not the later checkout. Scratch is confined to `$TMPDIR/ssds80-manual-review-f044820` (`TMPDIR` was unset, so `/tmp` was used).

| Check | Executed result and claim limit |
|---|---|
| Candidate and four named blobs | Exact full commit/blob identities verified. |
| `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` | 4 tests passed; routing/lifecycle frontmatter only. |
| `git diff --check 94316298ba0d40831560591c2d2385544b93ea42 f04482003cc46e8bf0d1fddd0cff3099e85e7c5f` | Passed, no whitespace diagnostics. Run against the original object store. |
| `python3 -I qualification/ssds80/item_review_history_probe.py` | Exit 0, 11 histories. `work_in_scope` met every expectation; `latest_delta` missed 7, `required_out` 2, `same_key_global` 1. Those intentional counterexamples were retained, not hidden as passing implementations. |
| Judgment model core family | Exit 0: 2,944,064 scenarios, zero invariant failures; unmutated core only. |
| Judgment model review-scope family | 278 unmutated cases, zero invariant failures; all 10 mutations naming this family were detected. |
| PEM schema | Exit 0: schema 1 valid, 5 families, 0 notices. Used candidate `source/project_engineering_memory.py`, original `GIT_DIR` and archive `GIT_WORK_TREE`; accepted/candidate PEM bytes identical. |
| Frozen surfaces | `git diff --exit-code fad3ee410ab9df0d94740cebb6969e161911b126 f044820 -- orchestrator/docs/architecture.md source dist` passed with no output. Frozen architecture blob is `39e6de727f6c35402962509d30d947962992eaad`. The only changed `orchestrator/` paths over that interval are the proposed Manual and catalogue. |
| Catalogue preservation | Body from Part 0 onward exactly equals candidate-61 Manual body. |

The model families were invoked from the unchanged module via `importlib.util.spec_from_file_location`, inserting the module into `sys.modules` before execution, then `MUT.clear(); run_family(CORE)` and `run_family(REVIEW_SCOPE)`. The review-scope mutation loop selected exactly entries of `MUTATIONS` whose family tuple contains `REVIEW_SCOPE`; each began with a cleared mutation set.

Review-scope mutation coverage: `judged_output_role_only` (R1/R2/R3/R5), `adverse_changed_units` (R3/R4), `judged_all_entries` (R1/R2/R3/R4/R5), `retained_at_admission` (R6), `retained_by_obligation` (R1/R2/R3/R5), `integrated_review_no_authors` (R7), `stale_retained_admitted` (R8), `retained_unchecked` (R9), `item_level_no_entries` (R7), `independence_on_delta` (R5). There were no undetected mutations in that executed set.

**Execution corrections preserved.** Initial module-import attempts omitted `sys.modules` registration and failed inside Python's dataclass import handling before any cases ran. Corrected invocations above replaced those attempts; their initial logs remain in scratch. An initial Git check from the archive lacked the original object store and failed to resolve its refs; rerunning from the repository succeeded. These are reviewer invocation errors, not candidate failures.

**Unverified.** The full all-family `--mutations` run, core mutations and other unexecuted families are not claimed. No real SSDS Admission, Dispatcher, Ledger Store, integration consumer, witness deployment, custody runner, migration, security boundary, performance envelope or live doctrine effect was exercised. No complete replay of all earlier review findings or independent statistical qualification of the 7.x study was performed. These limits do not erase B1 or authorize later gates. Required remaining G1 document evidence must be accounted for before G1 closeout; future runtime checks stay at G2–G4.

Scratch logs: `consolidation.log`, `history-probe.log`, `core-corrected.log`, `review-scope-corrected.log`; source snapshot and immutable owner extracts are in the same scratch directory. The decisive blocker is reconstructible from this record's pinned text and trajectory without retaining scratch.

## Scientific checks

- **Material findings:** B1 is material to the independence of governance over scientific software. Register and non-blocking findings are stated above. No realized scientific anomaly or new scientific result is asserted.
- **Realized results / null envelope:** I produced, ran and reviewed **no realized scientific results**. I executed software-design diagnostics and prepared this bounded D3 gate-evidence record. Examined: pinned architecture, revised gate contract, selected historical cases, provenance/independence, frozen inheritance and diagnostic outputs. Materially unexamined: scientific datasets/results, numerical validity of project claims, future SSDS runtime/custody and empirical usability. The materiality basis is whether the architecture can provide false independent closure, not a scientific outcome measured here.
- **Variants:** One Manual candidate was reviewed; none was repaired or selected from alternatives. Six author-owner sibling variants and three delimiting controls were analyzed as stated under B1. Executed diagnostic selection comprised the 11 explicit history cases and their four rule constructions, the core base family, review-scope base family and its 10 applicable mutations. Counts of variants are local review coverage, not a claim about the author's whole design search. Mutation selection came from the candidate's family metadata, not from which results were favorable. No scientific model, pipeline, parameter, preprocessing or held-out-data variant was selected.
- **D1/D2 reliance / tensions:** No accepted scientific D1 or numerical D2 authority was used to make a consequential scientific judgment. The controlling independence and lifecycle claims are D3/protocol authority; merely examining their D1/D2 representations does not adopt a scientific model. A scientific tension search was therefore not triggered. No native issue search or scientific tension disposition is claimed.
- **Delegation and gaps:** No sub-agent was launched. Tools' failures and unexecuted coverage are disclosed above. Historical selection beyond the bounded records is unknown; no exhaustive historical variant count is asserted. No additional unanswered delegated return exists.

## Common-mode note

The reviewer is of the **GPT family**, different from the Manual author's Claude family, engaged directly by the stakeholder through the named handoff. Several earlier reviewers, including the Phase B and 9431629 reviewers, were also GPT-family reviewers; this is not independent-family corroboration of their conclusions. I reconstructed B1 from exact current owner text rather than adopting a prior verdict.

Shared dependencies remain the repository corpus, stakeholder decision record, protocol/workplan framing, local Python/Git toolchain, author-written diagnostic cases and abstractions, and related model-family training. The diagnostic oracle shares helpers with the rules under test; the new history probe has a distinct history-to-author construction but still shares its written invariant and selected examples. No cross-family verdict can turn those dependencies into production qualification or stakeholder acceptance.

## D4 statement

**SSDS 8 D4 remains NOT AUTHORIZED.** This review accepts no Manual, workplan revision, default value or product scope; it closes no stakeholder gate. Repair B1 at the proposed D3 independence owner, preserve the level split and open register, freeze the replacement candidate, and independently review the affected architecture before seeking G1 acceptance. G2 still separately requires its reviewed shadow handoff, mechanism/register closure and explicit stakeholder authorization. No commit or push was performed.
