# Independent re-Review — SSDS 8.0 Phase E, candidate 49bebf3

```text
GOVERNING SSDP: 7.2.1
  public source: aaeaf8b6b2121b9fb8aba31917c8265649c43954
  recovery: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
CANDIDATE: 49bebf32ad0ce61785b5e8f63e84f5557f23ecca
PREVIOUS CANDIDATE: 89684fb93152f87355a84bde1928b8d69218b8b6
BASELINE: 55c01a8369037465aa4fdb776b115b89041b177e
ENVELOPE: 7d660f42b7550eee599a150277082657e041503a
SCOPE: handoff's E-R1, R1 and R2 repairs, shared owners and consumers,
  disclosed limits, replay discrimination, preservation and accounting;
  shadow implementation and Phase E exit only
MANUAL blob: fe43f04f5a698688727f7473a7c2e4d5345ae911 (accepted A1–A9)
PLAN blob: 678a7cf1a5de14fac5795b203d613b06ec9f45d7
REVIEW METHOD: independent authority and owner reconstruction; real-package
  history/consumer probes; partition-shape controls; executable mutation;
  required suites, installed wheel/sdist and snapshot checks
REVIEWER: OpenAI GPT family, different from the Claude-family author.
  Engaged through the Codex CLI in the stakeholder's own terminal at the
  stakeholder's request; the author's session typed only the pointer prompt.
  This reviewing context did not author the candidate.
```

The handoff at the envelope governs this Review. Candidate release-state identities, Manual and plan blobs were verified. I entered `source/roles/software-implementation/SKILL.md` at the pinned public source and loaded its applicable kernel, D4, workflow, evidence, testing, definition, architecture, convergence, versioning and PEM owners. The accepted Manual and G2 register constrain the judgment; earlier Reviews and repair accounts were hypotheses and bounded evidence.

## SERIOUS CHALLENGE

None established. The remaining failure is a D4 routing violation of coherent accepted authority, not evidence requiring a Manual relaxation or G1 reopening. The bounded Challenge pass varied the shape of execution ownership while holding the required no-part decision fixed. It found a disclosed limit that a generic liveness criterion incorrectly treats as sufficient closure.

## Verdict

**NO-PASS for the Phase E implementation and NO-PASS for the Phase E exit. Neither passes.** E-R1, R1 and R2 are closed on the required trajectories and controls. One other Phase E blocker remains: **E-R3, a one-part partition hides the principal's required decision after an item-level NO-PASS naming no part**. This is the plan §6 single-part finding, reclassified as blocking. It was already disclosed; it is not claimed to be newly introduced by these repairs.

The item remains `OPEN`, but its implementer part becomes `READY` for re-dispatch and the required `COORDINATE:item-level-no-part` obligation is absent. A different live route and an evidence-disagreement adjudication do not satisfy the accepted route requirement. No false discharge or permanent deadlock is claimed for this counterexample.

The required suites pass. They and the lifecycle hook do not discriminate E-R3. Phase F's dependent work cannot start under G2 §5.1 item 5 on this Review. This record accepts nothing at G3.

## Repair and accounting dispositions

| Point | Disposition | Evidence and bounds |
| --- | --- | --- |
| E-R1 | **CLOSED** | Both earlier histories—whole work before partition and work of a replaced part—retain `records`. No permission and empty-subject permission give `OPEN`, an open restoring part with a live route, and a waiting dependent. Complete permission gives only `DISCHARGED_PROVISIONAL`. Reports retain the open item's scope; the decision projection says `OPEN`. |
| R1 | **CLOSED** | Tightening retains the subject before the replacement partition and afterward. The new part that covers it reopens; the follow-up waits. The unkeyed result exercises the obligation-identity path, not merely `binding.item_key`. Supplemental incomplete-permission controls pass both with and without that optional key. |
| R2 | **CLOSED** | The completed non-covering partition yields a derived next decision naming its answer. A covering answer is discovered and assigns `records` to a part. The brief names the uncovered failing subject. A non-covering partition followed by two settled unchanged-item answers reaches SD-55's human hold; a principal's covering answer then counts for nothing, while the human's counts. The held decision appears in the inspector. |
| Replay hook | **BOUNDEDLY ADEQUATE FOR R2; INCOMPLETE FOR ROUTE CORRECTNESS** | It rejects a finished-parts strand and accepts actual live part work and the documented plan-reacceptance wait. It also accepts E-R3: a ready part is sufficient for its existential check even when the required principal decision is missing. |
| E15 | **Mechanics and recorded coverage substantially accurate, limited oracle** | The current alphabets reproduce 7,254 ordinary and 9,361 retained chains through length four. The suite samples run here; the full enumerations were not rerun. They do not cover every partition shape or establish every required route. The retained test's inherited method name says length two although its implementation, correctly disclosed in E15, exhausts only lengths zero and one and samples lengths two through four. |
| E30 | **Repair account accurate within tested histories** | The subject union now comes from integrated admitted history. Parts read retained subjects within their scopes; the whole reads uncovered subjects, and per-part permission remains required. No new subject-loss or false discharge survived the bounded probes. |
| E32 | **PARTLY ACCURATE** | Retention and non-covering continuation are realized. Its no-part-to-principal statement is not realized for the one-part counterexample. |
| §6 | **Disclosed, but one classification rejected** | Single-part reopening is genuinely present, but being live and fail-closed is insufficient to make it non-blocking. Redone evidence without disposition and the other boundaries are assessed below. |

## Phase E blocker

### E-R3 — A one-part no-part NO-PASS loses the principal's required route

**Authority and owner text.** Manual §10.4 requires that an item-level review naming no part go to `COORDINATE(plan)`. G2 workplan §4.2's row “§10.4 route 4 for an item-level review naming no part; §13.7 partition” is explicit: the partitioned item “carries route 4's `COORDINATE(plan)` for findings naming no part”; a part whose outputs are named takes its own route. Phase E reading E32 repeats this distinction. This is already Phase E's routing owner and group-5 obligation, not an Admission or Dispatcher feature deferred to Phase F.

**Executed discriminator.** `single_part.py` under the scratch root constructs three schema-checked histories through the installed real package, with no replacement of the derivation or routing owner:

1. An accepted, lint-valid `DOCUMENT` item has `o1`, `o2`, `o3`, budget two, and scope `records` plus two note subjects. Spend its whole-item budget, then partition all three obligations into one part with that full scope.
2. Complete, independently review and integrate that part's change to the three subjects. The whole now correctly routes to `item-level-review`, and its review obligation is derived.
3. Admit that first item-level review as an independent `NO_PASS`, with `NONE_FOUND` in its reviewer's findings slot: no part is named. This does not depend on an unsolicited second review of an already discharged item-level obligation.
4. Derive the whole, part, obligation set and both liveness sensors.

Observed at the candidate:

```text
item-level NO-PASS nonind = false; its objection stands
whole.discharge = OPEN
whole.route = partitioned:<original partition>
whole.route.decisions = []
sole part: OPEN, route re-dispatch, readiness READY
required no-part decision derived = false
ADJUDICATE_DISAGREEMENT = present
group-6 stranded(workflow) = []
LifecycleRetained.suspended(flow) = []
```

The expected initial no-part decision in this fixture is `sha256:08f526fb38d033dc88697ce874f2ad91d4b8556ec3aeeaa55305d5dc2a3ab0ef`. It is absent from the actual obligation set. The supplemental test fails its exact expected route assertion. Two controls pass: the same no-part review with **two parts** derives that decision, while a **one-part review explicitly naming part 0** correctly reopens the part. All three reviews are independent.

**Cause.** At `orchestrator/src/ssds/derivation/items.py:762`, `_composite_route` returns the partitioned route whenever a part is open, before inspecting the standing no-part objection at lines 764–770. With one part the whole item's judged work coincides with the part's work. The standing item-level adversity consequently vetoes the part's earlier passing review through the real judgment owner, reopening that part. The early return then hides the root no-part decision. The generic disagreement route remains visible, but does not replace the principal decision the register requires. Waiting until further implementer iterations exhaust a budget is likewise not the prescribed SD-54 condition/answer chain.

**Minimum repair.** Reconcile no-part objection routing and required-part state at the existing item/composite-route owner. Derive the no-part principal decision when this objection arises, preserving the real judgment veto, every part obligation, and independent item-level review. Preserve the handoff of an actual partition answer to its unfinished parts and continue past it only when appropriate; do not blindly bypass unfinished parts or weaken the veto to keep their old reviews current. No new registry or presentation-only substitute is needed.

**Acceptance discriminator.** Retain the three shape/finding controls above. The one-part no-part case must remain `OPEN` and derive the no-part decision immediately, keyed by condition, revision and answer; the explicitly named-part case must retain its part route. Exercise its answers through SD-54 continuation and SD-55 hold, and preserve E-R1/R1/R2, including live unfinished partitions. Strengthen the replay or pair it with a direct route assertion so this case cannot pass merely because some part is ready. Reconcile E32 and §6's completion/classification claims.

## Replay discrimination and shared-owner examination

`chain` follows answer identities; partition discovery records seen partitions and advances the no-part chain's `past` set. The inspected admitted histories and continuation probes terminate, do not double-count the covering answer, and preserve the human hold. No candidate recursion or nontermination was established. Structural discovery of answers to never-derived decisions remains the explicitly disclosed Phase F Admission boundary, not proof that such an answer was authorized.

The retained alphabet's `PARTITION-ELSEWHERE` is a fair R2 discriminator: its split is lint-valid, assigns all contract obligations, omits the failing retained subject, completes its part and passes the item-level review. The next answer must therefore be offered on a real continuation decision. It does not replace an owner with a model.

Four completed scratch mutation configurations gave these results:

| Perturbation | Result |
| --- | --- |
| Remove a part's inherited retained-subject scope | `RetainedWork`: five failing subtests, zero errors. |
| Remove historical part-obligation discovery, leaving the whole obligation only | R1 unkeyed variant fails the retained-subject assertion, zero errors. |
| Make the composite route stop at the earlier no-part partition instead of continuing past it | Direct R2 plus retained lifecycle sample: 17 failing assertions/subtests, zero errors. |
| Same broken composite route plus an always-successful suspended hook | Retained lifecycle sample becomes green. This is an oracle-negative control, not candidate evidence. |

The unmutated repair groups pass five test methods with zero failures/errors. One preliminary mutation discarded `past` inside `chain` itself; this also destroyed partition discovery's progress invariant and was interrupted. It is not evidence of a candidate hang and is not counted as a successful detector. All mutations were process-local; candidate files and installed package bytes were not patched.

The actual hook is stronger than that vacuous mutant and detects R2. Its remaining limitation is shown without mutation by E-R3. Group 6 is also green on that state: its route-vocabulary and partition-existence checks are not an oracle for the mandated choice among otherwise live routes. The earlier disclosed limitation concerning missing revalidation routes remains; neither sensor is represented here as a complete liveness proof.

## Findings for later phases

No new later-phase mechanism requirement is established. Phase F still owns Admission refusals and decision/task authorization, Dispatcher/lineage, integration, runners and §17 realization machinery; Phase G owns intake/migration/external pilots, and Phase H its adversarial/fault qualification. The disclosed structural counting of an answer to a never-derived continuation decision must be refused at Phase F's actual Admission boundary.

The earlier deferred merge/upgrade/annotation, R3 floor, review qualification, confidentiality and incompleteness projections, specification-change review items, unsupported obligation briefs, doctrine-source resolution and digest acknowledgment obligations remain visible in §6. This Review neither waives nor realizes them. A9's continuing no-removal constraint belongs at general structure-change Admission; the replacement A9 shadow genesis is a separate human gate. SD-63's PEM amendment work remains separately proposed and gated.

## Non-blocking findings and disclosed limits

**Redone work and fresh passing evidence.** A fresh passing realization alone correctly leaves the old counted failure undisposed: in the executed repaired-work history `ev=qual=P`, and the item is `OPEN`. Manual §6.6–§6.7 and §6.10 explicitly reject edit-and-rerun or a later pass as automatic disposal. Adding an independent current `IMMATERIALITY` disposition through the real evidence owner gives `ev=qual=T` and `DISCHARGED`. Thus this disclosed observation does not establish an irreversible evidence strand or a need to weaken evidence persistence. Full runner and discriminating-reading scheduling remains a later-phase boundary.

**Overlapping successive partitions and kept/new parts.** The reproduced overlap reopens an earlier part by drift, leaves a live part route and eventually a budget decision; after an objective amendment the part visibly waits on plan reacceptance with a `PLAN_ACCEPT` obligation open. This is wasteful delegated machinery, not a demonstrated false discharge or missing route in the tested history. Keep the simplification concern visible; do not treat this result as proof of eventual convergence for arbitrary overlapping histories. It is distinct from E-R3's missing specifically required decision.

**Accounting residue.** G2 §4.12's previous 32-case summary is corrected to 31, five fenced; other older register narrative still contains a 32-case parenthetical. The independently identified case inventory and phase allocation are unchanged. This is a non-blocking wording/count residue, not another missing-case finding.

## Verification, reuse and gaps

All final commands ran against the exact candidate in a scratch archive given its own Git context. Python was 3.11.15 and UID 1000. `TMPDIR`, `SSDS_HOME` and Hypothesis storage were within `/tmp/ssds80-phase-e-rereview-49bebf3`; no operator state was written to `~/.ssds`.

| Check | Final result |
| --- | --- |
| Package plus `orchestrator/requirements-dev.txt` installation | PASS, offline with `--no-index --no-build-isolation`; candidate wheel built and installed. |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | 470 tests, OK, four optional slow-class method skips. |
| `python orchestrator/scripts/run_core_tests.py -j 4` | 393 tests across all 13 modules, OK, including real wheel/sdist build and clean-environment installation. |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | PASS. |
| `python -m unittest discover -s tests -v` | 435 tests, OK, three gated remote-fallback checks skipped. |
| `git diff --check 89684fb9 49bebf3` | PASS. |
| Supplemental consumer/continuation/hook probes | Five methods pass; six E-R1 permission/history combinations and two extra R1 incomplete-permission histories included. |
| Supplemental partition-shape discriminator | Three methods: one expected governing-route failure, two passing controls; zero errors. |

Initial environment attempts failed because the archive lacked Git metadata, an inherited Git override interfered with fixture repositories, and isolated builds attempted unavailable network access. These were corrected using an independent scratch Git context and a scratch wheelhouse assembled from locally installed/cached dependencies; no candidate test or product source was weakened. The first root-suite attempt created empty fixture files in the original checkout; those test-created files and one generated bytecode file were removed, restoring its clean state before this record. Final reruns above supersede those environment failures. Early supplemental API/fixture mistakes were corrected in scratch; the final named logs distinguish executed results from those attempts.

**Preserved earlier closure.** The candidate suites rerun E-B2's earlier item-level finding carry, E-B3's mode/type/newline diff distinctions, E-B4's eligible non-current qualified gate visibility, B2's evidence projections and B5's exact-revision/unavailable governing content, together with A9 genesis and shadow/read-only boundary tests. Only `items.py` and the decision renderer changed in production since 89684fb. The earlier review's additional unified-patch round trips and stronger finding/gate controls are reused only for their unchanged owner paths; they were not independently recreated here. Frozen Core, source, distribution, Manual and assessment-owner files are unchanged across the repair delta; Core and snapshot checks were nevertheless rerun.

**Optional/unavailable evidence.** Neither full slow lifecycle enumeration was rerun. E15's recorded runs at 6992d118 and 9bec3111 are reused as reported bounded evidence: the intervening delta through this candidate changes no production code. Their timings and complete run outputs were not independently established here. The three opt-in historical remote-fallback realizations were not executed; no current fallback/publication change depends on them in this delta. No live campaign, operator-ledger run, replacement genesis, native qualification, burden/doctrine measurement or Phase F functionality was performed or inferred. There is no missing mandatory handoff command; these limitations do not conceal or close E-R3.

Scratch scripts/logs: `single_part.py`/`.log` (decisive counterexample and controls), `probes.py`/`probes-final3.log`, `limits.py`/`.log`, `mutations.py`/`mutations-final.log` and the per-mutant logs, `ssds-final.log`, `core-final2.log`, `root-rerun.log`, `snapshot.log`, `install311.log`, and `pem.log`, all under the prescribed scratch root.

## Historical applicability and common mode

The G2 workplan independently binds accepted/base PEM to `main` at `af0455753e20ee54a969c844872e29e270007211`, blob `1561797125622f355f84eb27319f87e8fa4227d9`, with no overlay. Both the local designated integration ref and candidate PEM bytes match that binding. Schema validation succeeds for five families and zero notices. Canonical family metadata was searched independently of temperature and summary visibility. Task-local HAS:

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: 1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: Evidence-only warning about proxy/oracle overclaim; challenge real owners and sensors.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen Core preservation independently required by G2 and current 7.2.1 versioning owner.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No source-to-package routing or generation repair.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No self-reference or release publication.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: No bootstrap or fallback publication.
```

The HAS validator returns no errors. PEM's inherited protocol-project identity and partial historical coverage are not promoted into exhaustive SSDS history; SD-63 explicitly leaves lineage reconciliation to its later amendment prerequisite. Bounded local history was instead available through the pinned Reviews, repair delta and disclosed findings. No PEM update was made or authorized.

Different-family execution strengthens process independence, not epistemic independence. The author tests and supplemental probes share the package, Python/Git toolchain, schema and some fixture constructors. Expected routes came independently from the Manual/register; partition-shape controls, real consumer projections and owner mutations reduce but do not eliminate that common mode. No agent vote or author PASS substitutes for the observed owner behavior.

## Scientific checks

- **Material findings:** E-R3 is the one blocking D4 finding. The inherited-partition efficiency concern and bounded sensor/accounting limits are reported above. No material scientific or numerical result finding was established.
- **Realized scientific results:** I produced, ran and reviewed no realized scientific results. The executions here are software-state fixtures and acceptance tests, not a scientific campaign or empirical protocol-effectiveness result.
- **Variants:** Six E-R1 history/permission combinations; R1's three supplied combinations plus two incomplete-permission/key variants; R2's non-covering/covering history and the explicit partition-plus-two-answer hold; three partition-shape/finding controls; fresh-pass versus explicit-disposition evidence states; ready/reacceptance/finished-parts hook controls; four completed mutation configurations and the interrupted preliminary mutation disclosed above. Selection criterion: change retained-work identity, scope, decision continuation or route choice while preserving the governing requirement. This is bounded falsification, not exhaustive trajectory coverage.
- **Tension search:** Not triggered. No accepted D1/D2 authority was used for a consequential judgment; the consequential owner is D3 workflow/routing. No scientific tension search is claimed.
- **Gaps:** Optional full enumerations, opt-in historical remote realization, live/runtime qualification and later-phase behavior remain unexecuted as itemized above. They do not supply a PASS for the missing route.

Nothing beyond shadow is authorized. This Review grants no implementation acceptance, campaign, publication, cutover, native authority or operator action; it does not authorize Phase F's dependent work while E-R3 remains open.
