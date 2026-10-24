# Independent re-Review — SSDS 8.0 Phase E, candidate 9c7d77d

```text
GOVERNING SSDP: 7.2.1
  public source: aaeaf8b6b2121b9fb8aba31917c8265649c43954
  recovery: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
CANDIDATE: 9c7d77dc6d9a17769e1e3df5c546edee5888cdbe
PREVIOUS CANDIDATE: 49bebf32ad0ce61785b5e8f63e84f5557f23ecca
BASELINE: 55c01a8369037465aa4fdb776b115b89041b177e
ENVELOPE: 07747138b1b09c852929f050bb6e80823a64b604
SCOPE: the envelope's complete handoff; E-R3 and its consolidated owner,
  siblings, replay discrimination, earlier closure, accounting, Phase E exit;
  shadow only
MANUAL blob: fe43f04f5a698688727f7473a7c2e4d5345ae911 (accepted A1–A9)
PLAN blob: 1557e3a42cad5d47e4dd9f4ad4e75c50a029c7e8
REVIEW METHOD: independent Manual/register reconstruction; real installed
  package, admitted-history fixtures and rendered-consumer probes;
  partition-shape and completion-order controls; historical-owner mutation;
  required acceptance suites and snapshot/whitespace checks
REVIEWER: OpenAI GPT family, different from the Claude-family author.
  Launched through the Codex CLI in the stakeholder's own terminal at the
  stakeholder's request; the author's session typed only the pointer prompt.
  This reviewing context did not author the candidate.
```

The committed handoff governs this Review. The envelope adds only that handoff to the candidate. Candidate, previous candidate, baseline, Manual and plan identities were checked. Release identities were resolved from `PROTOCOL-RELEASE-STATE.yaml`. I entered the Software Implementation skill at the pinned public source and loaded the applicable kernel, D4, workflow, evidence, testing, definition, architecture, convergence, versioning and PEM owners. Earlier Reviews and the repair account were hypotheses and bounded evidence, not acceptance authority.

## SERIOUS CHALLENGE

None established. The bounded Challenge pass tested whether a live route could still omit information required by its consumer, whether a recursive partition could settle before all replacement work integrated, and whether settlement could revoke a decision while its condition stood. The surviving defects are D4 nonconformance to coherent Manual §16.7 and to the finding-preservation/routing contract of §10.3–§10.4 as concretized by E32. It does not warrant relaxing the Manual or reopening G1.

## Verdict

**NO-PASS for the Phase E implementation and NO-PASS for the Phase E exit. Neither passes.**

**E-R3 is CLOSED at its routing owner within the tested, derivable histories.** The three shape controls, SD-54 continuation, SD-55 hold, carried review, B-1, B-2, S-1, C-1 and dropped-branch cases pass. The consolidated rule is a faithful, simpler concretization within the accepted post-answer rule; no surviving settlement or false-discharge counterexample was established. A distinct selector-resolution sibling, E-R5 below, remains at the condition owner.

Two Phase E blockers remain. **E-R4: the no-part decision brief omits the standing review's identity, outcome and findings.** This reclassifies the disclosed §6 decision-brief finding. The principal receives the name of a condition and permitted answers, but not the adverse judgment that makes the decision necessary. The same omission survives continuation to the human hold. A route's existence does not satisfy its required information contract. **E-R5: an unresolved part selector suppresses the principal decision and returns the item to an already answered review.** This is a sibling at the condition/selector owner, not a failure of the recursive settlement rule.

The required suites pass. Phase F's dependent work cannot start under G2 §5.1 item 5 on this Review. This record accepts nothing at G3.

## Dispositions

| Point | Judgment | Evidence and limit |
| --- | --- | --- |
| E-R3 | **CLOSED** | One-part/no-part and two-part/no-part derive the principal decision immediately; one-part/part-0-named retains the part's route. The real veto remains in force. An actual unfinished partition answer retains the route until its work settles. |
| SD-54 and SD-55 | **PASS on examined histories** | Unchanged-item `AMEND` answers continue with `after` bound to the answer. After three counted answers the next decision is human-held. A principal answer there does not advance it; an authenticated human answer does. |
| Carried review | **PASS on examined histories** | A newer integrated result derives its review beside the still-open decision. The real review briefing carries the earlier review identity and exact findings. A subsequent independent passing review retires the objection and permits discharge when the other terms hold. |
| B-1, B-2, S-1 | **CLOSED** | Repeated no-part adversity, redo, answered continuation, two-part redo and unfinished re-partition controls pass. Historical-owner mutations are detected. |
| C-1 | **CLOSED** | Both replacement depths pass; six independent completion orders of a three-leaf replacement tree hold the answer until the last leaf integrates. The old any-descendant rule fails the direct discriminator. |
| Dropped branch | **PASS on examined history** | A later whole partition dropping the earlier branch does not leave the old answer holding a route to absent work. This does not imply the replacement whole partition has finished. |
| E15 and replay | **Boundedly adequate, not exhaustive** | Route-4 discrimination improves materially; it shares the owner's objection/subject sets and omits part-decision answers. Direct tests, rather than its alphabets, discriminate C-1. Recorded full-enumeration applicability is valid as bounded evidence. |
| E32 | **Accurate for settlement; selector fallback not realized** | The recursive definition agrees with the candidate. Monotonicity is scoped to one item revision and admissible histories; non-derived answers remain the Phase F boundary. It is not a proof that all replacement work has finished when an earlier branch was dropped. Its fail-safe treatment of ambiguous part naming is not implemented by the bare integer collection (E-R5). |
| §5 and §6 accounting | **PARTLY ACCEPTED** | Repair chronology and the specified limits are recoverable. The decision-brief omission is accurately disclosed but wrongly classified as non-blocking. E32 also overstates selector resolution (E-R5). The claim that Phase E implementation is complete is therefore premature. |

## Phase E blockers

### E-R4 — The no-part decision brief hides the adverse review it asks the principal to address

**Owner text and scope.** Manual §16.7 requires the decision obligations owed, their target identities and revisions, and the **relevant conformance and review outcomes**, and says that the decision brief is the plan's working state because the principal keeps no memory between invocations. Manual §10.4 and the G2 §4.2 route-4 row require this coordination specifically because an item-level adverse review names no part. Rendering decision briefs is Phase E step 7, not a Phase F Admission or Dispatcher feature. The current plan §6 acknowledges that the no-part brief does not name the standing objection.

**Real owner and cause.** `orchestrator/src/ssds/interface/render.py:617`, `Renderer.decision`, renders item route/discharge/iteration summaries and, for this decision, only `x.detail` plus allowed outcomes. The detail is `item-level-no-part on plan.work.item`. The condition-keyed target contains the plan, item, revision and preceding answer, but no review record. Neither the item summary nor the other sections supplies the triggering review. The renderer already handles uncovered failing retained subjects explicitly; it does not handle the objection branch of the same condition.

**Executed counterexample.** `probes.py` constructs an accepted, lint-valid two-part item, independently reviews and integrates both parts, then admits the derived item-level review as `NO_PASS`, with findings:

```json
[{"id":"JOINT-FAILURE-777","units":["records","notes.a"],"status":"OPEN"}]
```

No part is named. The real installed package derives `COORDINATE:item-level-no-part`; both parts are discharged and the whole is `OPEN`. The decision is actually in the derived obligation set. Rendering that decision through the production renderer gives:

```text
standing review: sha256:ebe040c3cb1f20cf5ddd74907604f336d18fba3b40b8a28d7352ed06ebf72f1f
review identity present in complete decision brief: false
NO_PASS outcome present in complete decision brief: false
JOINT-FAILURE-777 finding present in complete decision brief: false
```

The full rendered artifact is scratch `decision-brief.md`. `siblings.py` independently reproduces the omission for a late no-part objection and, after three counted unchanged-item answers, its human-held continuation: the review identity, outcome and finding are still absent. Both examples use real derivation and rendering, not replacement decision logic. The late-objection example is supplemental; the first example arises on the ordinary first derived item-level review and is sufficient by itself.

**Consequence.** The principal cannot identify which joint failure to cover, distinguish the obligation's objection trigger from its uncovered-subject trigger using the brief, or inspect the relevant review outcome without reconstructing state outside the required working-state projection. At the human hold the same missing context reaches a consequential decision. A queryable ledger and a correctly carried later review do not repair this consumer contract. No lost ledger record, false discharge or permanent deadlock is claimed.

**Minimum repair.** At the existing decision-brief owner, project the actual standing no-part review records and their outcomes, exact targets and available findings into the decision's relevant record core. Preserve all standing triggers if several apply, including failing uncovered subjects. Keep narrative by reference; do not add a new registry or alter the decision identity, objection veto or settlement rule. Reconcile §6's classification and the completion account.

**Discriminator.** Render the ordinary initial no-part decision with a distinctive finding and require the exact admitted review identity, `NO_PASS`, target identity and finding data. Repeat after an answer, at the SD-55 hold, and with both no-part adversity and uncovered failing retained work. A control with no standing objection must not invent one. Retain the existing routing, carried-review and disclosure-exclusion tests. Green liveness and lifecycle tests alone cannot discriminate this renderer omission.

### E-R5 — An unresolved part selector loses the required coordination route

**Owner text.** Manual §10.4 requires coordination when an item-level adverse review names no part, preserves findings rather than retiring them through an unseen later obligation, and §10.3 prohibits redispatch of an answered judgment obligation. Phase E E32 promises that an item-level finding naming a part ambiguously fails safe to the principal. These are Phase E condition/routing obligations; future refusal of answers to non-derived decisions does not resolve them.

**Executed counterexample and controls.** `named_findings.py` starts from two independently reviewed, integrated parts and selects the actually derived item-level `REVIEW` obligation. Unlike the generic fixture helper, it explicitly binds both the reviewer judgment and its task result to that obligation, with reviewer role and fresh attested lineage. Its adverse finding is `{"part":99,"units":["records"],"id":"PART-SELECTOR-FINDING"}`. The closed record schema accepts the record; there are only parts 0 and 1. The review is independent and its adversity stands.

```text
no_part_condition = false
whole = OPEN; route = item-level-review
both real parts = DISCHARGED
all derived COORDINATE obligations = []
same target REVIEW = REFUSED; readiness = ANSWERED
Lifecycle.route4 = []; group-6 stranded sensor = []
```

The admitted adverse review is `sha256:28d06c4283258dde3cd721ac72d6d0b075c6604bf69065a48daadebbf5e6f072`; its answered obligation is `sha256:482744d8a3bd21ad73ec9164370c9b38b294b36607e727a9dcb957e993b1b898`. The `part: 0` control correctly reopens real part 0 and uses its route. A strict-type sibling, `part: true`, incorrectly selects part 1 because Python treats `bool` as an `int`, although its finding names `records`, the other part's output. The nonexistent-selector case alone suffices for the blocker; the Boolean result bounds the same parsing cause.

**Cause and consequence.** `items.py:556`, `_named_parts`, collects every `isinstance(value, int)` without resolving it against the actual parts of the judged integrated result. `no_part_condition` then interprets any nonempty set as a resolved part assignment. No real part 99 receives the adverse finding, so every part remains discharged and `_composite_route` falls through to the same item-level review already answered adversely. This is not a new target or an admissible repeat dispatch. Generic author reassessment or adjudication may still end adversity; no global deadlock is claimed. The specifically required principal route is missing, as in the original E-R3's distinction between some live route and the mandated route.

**Minimum repair.** Resolve finding selectors at the existing item-level finding owner against the parts and partition identities of the judged result, preserving strict integer typing and scope. A missing, invalid or ambiguous real-part referent must fail safe to the principal rather than count as a successful assignment. Preserve named-part reopening for valid references, every finding, and the consolidated settlement rule. If Admission also rejects such malformed annotations, that later defense does not justify treating unresolved admitted finding data as a resolved selector in the current derivation.

**Discriminator.** Bind the first item-level NO-PASS to its real derived review obligation. Compare absent selector, valid part 0, nonexistent part 99, Boolean selector, and repeated indices across retained/replacement partitions. An unresolved/ambiguous selector must derive coordination; a valid unambiguous one must reopen the correct part. The same answered review must never stand in for the next route. Test the condition independently of `_named_parts`: the current lifecycle oracle shares this defect and returns success on the counterexample. Reconcile E32 and §6 accounting without weakening the no-stranded/finding-preservation contract.

## Consolidated-rule and simplification assessment

The implementation derives settlement from the admitted integration/replacement history rather than maintaining a latch or asking whether the parts happen to discharge now. For each original part, `done` holds if it integrated; otherwise every child of each replacing re-partition must be done; otherwise the part must no longer be required. The outer operation requires every original part. This removes the latest-integration/raised-again comparison and fixes the existential-descendant counting error.

Within an unchanged item revision and admissible history, an integrated part keeps that witness through later adversity or redo. An unfinished replacement leaf holds the answer; every leaf is required by the recursion. A branch dropped by a later whole partition supplies no remaining work for that old answer to wait on. A fresh continuation decision can therefore appear beside the carried review without discharging either the whole or an unfinished part. The supplied dropped-branch test and the six completion-order histories support these distinctions. The candidate's C-1 discriminator also covers a sibling not yet integrated at depths one and two.

I found no unsettled answer with neither required work nor the disclosed later-owner refusal boundary, and no admissible tested case in which settlement revoked a still-required open decision. This is bounded executable and source reasoning, not an exhaustive proof over arbitrary admitted records. In particular, admitting answers to decisions no longer derived can revive dropped work; the handoff expressly assigns refusal to Phase F. An R1 tightening starts a fresh revision-keyed chain, so same-decision monotonicity is not claimed across that change.

Manual §13.7 permits later whole partitions to replace undischarged parts while retaining discharged obligations. SD-54 requires answer-qualified continuation rather than an unanswered or silently abandoned persistent condition. The consolidated rule satisfies both in the examined states. Its early continuation after an earlier branch is dropped does not mean that the later whole partition has integrated; required parts remain open and keep their own routes. These are distinguishable claims in E32.

The simplification obligation in plan §8/G2 §5.6 is met for this repair: one ledger-derived recursive notion replaces the unstable discharge/raised-again notions, without a second state owner. The historical fifth/sixth-defect wording is a repair-round account, not evidence of that many independent post-acceptance recurrence episodes. E-R4 is a separate projection defect. E-R5 is a selector-resolution defect sharing the condition input, not evidence against the recursive settlement construction. Reconcile selector interpretation at its one real owner before adding compensating route exceptions; neither finding establishes a need for broader architecture replacement.

## Replay discrimination and enumeration applicability

`Lifecycle.route4` is stronger than the previous existential liveness hook. On a standing condition it demands the no-part decision/wait, except for the replay's last unworked partition answer. It no longer accepts an arbitrary ready part as a substitute. Applying the old composite route after constructing a valid one-part seed makes the oracle report `route4: the no-part condition holds without its decision`.

The oracle obtains the condition from production `_objections`, `_named_parts` and `uncovered_failing`, and guards on production discharge. Thus defects erasing the condition or falsely discharging the item can defeat both the oracle and the owner; it is independent of route selection, not an independent objection, retained-subject or discharge oracle. E15 now states the objection/subject dependency. E-R5 realizes this common-mode weakness: the direct oracle and group-6 sensor both return no problem on the unresolved-selector state. The direct retained-work, predicate, selector and consumer controls remain necessary.

The alphabets cover ordinary SD-54 outcomes and actors, unsettled answers, the retained non-covering partition, repeated one-part partition/adversity and a non-answer redo step. They do not answer a part's decision and cannot construct the C-1 replacement tree, every overlap, late-review timing or arbitrary review findings. Group 6's existing collection also does not automatically cover every state in the new review module. No complete-liveness claim follows from either sensor.

I independently counted the current filtered enumerations through length four:

| Enumeration | Counts by length 0–4 | Total |
| --- | --- | --- |
| Ordinary, both conditions | 1, 14, 84, 504, 3024 per condition | 7,254 |
| One-part | 1, 17, 153, 1377, 12393 | 13,941 |
| Retained | 1, 16, 128, 1024, 8192 | 9,361 |

E15's recorded full runs at `9a00fb78` apply unchanged to `d5f21b07` for those alphabets. I inspected the production delta: the difference is the recursive all-child settlement of re-partitioned parts, plus removal of a vacuous integration-position comparison. With no part replacement, the two rules reduce to the same integration-or-no-longer-required test; an integration bound to a partition's part necessarily follows that partition. No replay answers a part's decision, so no replay creates the differing topology. Later changes through the candidate add accounting only. This validates applicability, not the recorded wall times or a fresh execution of the full enumerations.

Process-local historical-owner mutations provided these discriminators:

| Reintroduced behavior | Final result |
| --- | --- |
| `49bebf32` composite ordering | Three-shape test: one failing subtest, no errors; exact missing route reproduced. |
| `af327075` settlement by current discharge | Seven settlement methods: seven failing subtests, no errors. |
| `98c4d9a4` nonmonotone raised-again rule | Two selected S-1 methods: two failures, no errors. |
| `9a00fb78` any-descendant completion | Seven settlement methods: two failing depth subtests, no errors. |
| Same C-1 mutant, one-part lifecycle sample | One method passes, confirming this alphabet's topology gap. |
| Old route applied after seed construction, direct `route4` call | Oracle rejects it with the required missing-decision diagnostic. |

These mutations changed in-process methods only. Initial broader mutation selections also produced missing-decision unpacking errors; the final selected discriminators above isolate ordinary assertion failures. Candidate files were not patched. The unmutated focused group passes all ten methods.

## Earlier closure, accounting and boundaries

**E-R1, R1 and R2 remain closed on their required histories.** The candidate suite reruns whole-before-partition and replaced-part retention, provisional-permission variants, dependent blocking, revision tightening with and without the optional result work key, non-covering/covering partition continuation and its decision projection. The shared route changed, so I relied on current execution rather than merely inheriting their previous PASS. No new subject loss or false discharge was established.

**E-B2, E-B3, E-B4, B2 and B5 remain closed.** Current tests rerun item-level earlier-finding carry, diff mode/type/newline distinctions, non-current eligible qualified-gate visibility, challenged evidence projection and exact-revision/unavailable governing text. The additional probe verifies that a real newly derived carried review contains the exact earlier no-part findings, and its passing answer can retire the objection. E-R4 concerns the principal's decision projection, not regression of the review's carry.

**Preserved evidence reused.** The previous review's additional unified-patch round trips, stronger evidence/gate controls and independent evidence-disposition probe are reused only for their unchanged owners: this repair changes production `items.py` and `workflow.py` only. Its end-to-end read-only run on the admitted position-zero shadow ledger is likewise reused as historical integration evidence: that ledger has no native item, so this route delta does not execute there. No operator ledger was opened or replacement genesis attempted in this Review.

**A9 and frozen Core.** A9's genesis realization and shadow/read-only fitness tests rerun in the SSDS suite; its Manual and genesis validation owners are unchanged by this repair. Source, distribution, Core and frozen-resource paths are unchanged across `49bebf32..9c7d77dc`; Core acceptance and snapshot checks nevertheless reran. Across Phase E as a whole, Core has the previously reviewed read-only `profile_for_protocol` lookup and API exports; it would be inaccurate to call every Core file byte-identical to `55c01a83`. No frozen-profile behavior change is inferred from those exports. General structure-change refusal and the replacement A9 genesis remain later Admission and separate human-gate work respectively.

**Accounting.** E15's enumeration counts, samples and changed-oracle limits are accurate at the specified scope; the retained/one-part test method names still mention length two although those implementations exhaust only lengths zero and one, which E15 correctly says. E32 states the implemented recursive settlement rule exactly at the examined boundary, but its fail-safe part-naming claim is not realized (E-R5). §5's repair lineage, C-1 limitation and no-repartition explanation are sound. §6 correctly exposes the remaining mechanisms, but disclosure cannot defer E-R4 past the brief's own Phase E acceptance boundary, and E-R5 is an additional omitted condition-owner gap. The earlier generic group-6/revalidation limit and older register count residue are not newly cured by this delta.

## Findings for later phases

- **Phase F Admission:** refuse answers to non-derived decisions, including a dropped part's obsolete decision; that is the boundary excluding revival that can unsettle an earlier partition. Refuse invalid partitions and implement the declared Admission halves, task/envelope authorization, lineage, Dispatcher and runner/§17 machinery. Structural counting here is not proof of authorized admission.
- **Separate human gate:** admit a replacement shadow genesis under A9 with the stakeholder's signature; retain the earlier ledger as history. This Review performs or authorizes no such action.
- **Later qualification:** the Phase G intake/migration work and Phase H fault/adversarial work, including SD-59's out-of-scope threats, remain unexecuted. Campaigns and burden/doctrine measurements still require their own frozen plan, Review and authorization.
- **Previously disclosed functions:** merged/annotated attention entries, R3 floors not yet realized, review qualification beyond independence, confidentiality/incompleteness projections, specification-change review items, unsupported S3 briefs, doctrine source resolution and digest acknowledgment stay at their declared owners. This Review neither supplies nor waives them. SD-63's amendment and PEM-lineage work remain separately governed.

## Non-blocking findings

**Overlaps and kept/new parts.** Successive whole partitions can retain discharged parts and create overlapping required work that reopens by drift. This remains a simplification/efficiency concern, not an established loss of obligations or false discharge in the examined trajectories. A part's live route can eventually reach its budget decision. I do not claim arbitrary overlap convergence.

**Early no-part decision.** An objection can take the whole-item route while a partition answering another chain has parts mid-work. Dropping an earlier unfinished branch then settles the old answer without integrating that abandoned work. The replacement parts remain required and open; no early whole discharge was established. The distinct old/new work claims must remain visible. This is waste and a bounded coordination choice, not a demonstrated violation of the accepted route/discharge rule.

**Late objection.** Independently reproduced: after a newer integrated result already has its item-level review, a late no-part adversity on the older result derives coordination and keeps the item `OPEN`, but derives no fresh review of the already-reviewed current target. Its target-keyed review has already been answered. Further work can create a new review target, while whole-partition work can encounter the overlap path above. Improving this requires reconciling carried-review/obligation identity; it is not evidence that the current item has falsely discharged or lacks the mandated coordination route. The decision-brief omission affecting that route is E-R4 and is blocking now.

**Fresh passing evidence.** The previous review independently established that a fresh pass alone does not dispose of the old counting failure, as Manual §6.6–§6.10 require, and that a current independent disposition restores the evidence terms. Those owners are unchanged; no defect or automatic-disposal requirement is inferred here.

## Verification, reuse and gaps

Final executions used Python 3.11.15 and non-root UID 1000. Tests ran against an extracted candidate with its own scratch Git metadata, using a wheel freshly built from that candidate. All retained scratch, scripts, virtual environments, test temporary directories and SSDS home are under `/tmp/ssds80-phase-e-rereview-9c7d77d`. No SSDS state was written to `~/.ssds`.

| Required check | Result |
| --- | --- |
| Package plus `orchestrator/requirements-dev.txt` installation | PASS offline with local dependency wheels, `--no-index --no-build-isolation`; candidate wheel rebuilt and installed. |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | 483 tests, OK, six optional slow-class method skips. |
| `python orchestrator/scripts/run_core_tests.py -j 4` | 393 tests across all 13 modules, OK, including installed-product wheel/sdist checks. |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | PASS; current snapshot matches and frozen snapshots remain coherent. |
| `python -m unittest discover -s tests -v` | 435 tests, OK, three opt-in remote-fallback checks skipped. |
| `git diff --check 49bebf32 9c7d77dc` | PASS. |
| Focused `NoPartObjection` and `SettledPartition` | Ten methods, OK. |
| Supplemental real-owner probes | Three shape controls, continuation/hold, exact carry/discharge, six leaf orders, late objection and initial/held decision omissions reproduced; three exactly bound selector controls expose E-R5. |
| PEM/schema and task-local HAS validation | No errors; five families, no notices. |

The initial default `python` command was absent; the first available-interpreter install attempt could not obtain isolated build dependencies over the unavailable network. Final execution used the local Python 3.11 runtime and copied dependency wheels; the old SSDS wheel was excluded and the candidate package rebuilt. The initial supplemental replacement probe accidentally used unchanged note contents, aliasing empty fixture transformations; changing those scratch inputs to distinct new contents produced the six successful final completion-order checks. Neither environment/setup attempt was treated as candidate failure or pass.

**Unexecuted evidence:** the three optional full slow enumerations were not rerun. Their recorded outcomes are reused with the exact applicability argument above; their full run output and timings were not independently authenticated here. The three remote-fallback realizations were not enabled. No live campaign, scientific result, runtime/native qualification, real Dispatcher trajectory, new shadow genesis or operator-ledger write occurred. These are explicit limits, not passes. All mandatory handoff commands completed after environment adaptation.

Evidence is retained in scratch `logs/ssds.log`, `core.log`, `root.log`, `snapshot.log`, `diff-check.log`, `install311.log`, `focused.log`, `probes.log`, `siblings-final.log`, `named-findings-final.log`, the per-mutant final logs and `pem.log`; scripts are `probes.py`, `siblings.py`, `mutations.py`, `named_findings.py`, `pem_check.py`, and the rendered omission is `decision-brief.md`. Earlier scratch attempts remain separately named. Only this review record is an authored repository change; no tracked candidate file was changed and no commit or push was made. Runtime-visible untracked empty configuration placeholders were left untouched.

## Historical applicability and common mode

The active G2 plan binds accepted/base PEM to designated integrated `main` at `af0455753e20ee54a969c844872e29e270007211`, blob `1561797125622f355f84eb27319f87e8fa4227d9`, with no overlay. The local integration ref and candidate PEM bytes match that binding. Canonical family metadata was searched independently of temperature/summary prominence and validated. Task-local HAS:

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: 1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: Evidence-only warning about proxy/oracle overclaim; test real owners and projections.
  - id: PC-001
    disposition: APPLICABLE
    reason: G2 and current versioning independently require frozen Core preservation.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No source-to-package router repair.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No release or self-reference publication.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: No bootstrap or fallback publication.
```

The inherited protocol-project PEM has partial coverage and unreconciled SSDS lineage; neither schema success nor a missing entry proves absence of an SSDS lesson. The bounded intake used the pinned earlier review, repair history and disclosed findings. No PEM was changed or promoted into authority.

Different-family execution improves process independence, not epistemic independence. Tests and supplemental probes share Python, the package, ledger schema, some fixture constructors, local dependency wheels and the Manual/register reading. Expected route and brief requirements were reconstructed from the accepted owners, and historical mutations plus a real rendered-consumer counterexample reduce but do not eliminate common mode. Reused earlier evidence is explicitly bounded above; no reviewer vote substitutes for owner behavior.

## Scientific checks

- **Material findings:** E-R4 and E-R5 are the two blocking software findings. E-R3 and its routing siblings close within the stated bounds; overlap, late-objection and sensor limitations remain visible. No material scientific or numerical finding was established.
- **Realized scientific results:** I produced, ran and reviewed no realized scientific results. Executions are deterministic software-state fixtures, acceptance tests and mutations, not a scientific campaign or empirical protocol-effectiveness measurement.
- **Variants:** Fifteen final supplemental history constructions: three shape/finding controls, one SD-54/55 hold history, one exact-findings carry/discharge history, six three-leaf completion orders, one late-objection/held-projection history, and three part-selector controls bound to the actual derived review obligation. Four preliminary selector/binding probes and two preliminary no-op replacement attempts are not counted again as final histories. Four distinct historical production perturbations were evaluated, with additional replay and direct-oracle observations of those same perturbations, not independent mutants. Candidate suites add their enumerated fixtures and seeded samples. Selection criterion was falsification of required routing, complete replacement integration, finding preservation and decision sufficiency. The preliminary no-op fixture and broader mutation attempts are disclosed above; no scientific model, dataset, held-out reuse or statistical selection claim is involved. This is a local review count, not the author's full development search history.
- **Tension search:** Not triggered. No accepted D1/D2 authority was relied on for a consequential judgment; the operative authorities are D3 routing, partition and interface contracts. No scientific tension search is claimed.
- **Gaps:** Optional full runs, remote realization, live/native/runtime qualification and later-phase execution remain unexecuted as itemized above. The supplied and executed evidence does not establish exhaustive history coverage or arbitrary overlap convergence.

Nothing beyond shadow is authorized. This Review grants no G3 acceptance, campaign, publication, cutover, native subject authority or operator action, and it does not authorize Phase F's dependent work while E-R4 or E-R5 remains open.
