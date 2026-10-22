# Independent re-Review — SSDS 8.0 Phase E, candidate 89684fb

```text
GOVERNING SSDP: 7.2.1
  public source: aaeaf8b6b2121b9fb8aba31917c8265649c43954
  recovery: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
CANDIDATE: 89684fb93152f87355a84bde1928b8d69218b8b6
PREVIOUS CANDIDATE: b7912159c0db8abeb3323d6a4b44532f18984094
BASELINE: 55c01a8369037465aa4fdb776b115b89041b177e
ENVELOPE: 875a88ab3fd795d08207e2bfb6aaee3fe7c0cafc
SCOPE: the four Phase E repair families E-B1–E-B4, their affected consumers,
  preservation of earlier closure, and the handoff's plan-accounting questions;
  shadow implementation and Phase E exit only
MANUAL blob: fe43f04f5a698688727f7473a7c2e4d5345ae911 (accepted A1–A9)
PLAN: workplans/active/SSDS-8.0-G2-PHASE-E-PLAN.md
  blob: 59d9c9775e6e1c8da18cc77ca6b7cf58e89795a6
REVIEW METHOD: independent owner reconstruction; earlier trajectories rerun;
  retained-history counterexamples through the installed real ssds package;
  consumer, resolution, byte-round-trip and owner-rollback controls;
  required regression, installed-product and snapshot checks
REVIEWER: OpenAI GPT family, different from the Claude-family author.
  Engaged through the Codex CLI in the stakeholder's own terminal at the
  stakeholder's request. The author's session typed only the pointer prompt.
  This reviewing context did not author the candidate.
```

The envelope adds only the named handoff to the candidate. I reviewed the exact candidate in a detached scratch clone, entered `source/roles/software-implementation/SKILL.md` at the pinned public source, and read its applicable kernel, implementation, workflow, evidence, testing, definition, architecture, convergence, Python and project-memory owners. The accepted Manual and G2 register govern; repair accounts and previous verdicts were treated as evidence and hypotheses.

## SERIOUS CHALLENGE

None established. The surviving defect violates the coherent combination of Manual §10.4's retained subject union and non-latching evidence terms, §10.5's scoped provisional continuation, and §13.7's partition of execution without changing the item or its scope. No Manual relaxation or G1 reopening is justified by these counterexamples.

The bounded Challenge/out-of-matrix pass followed retained work across changes of execution ownership, independently of the seven newly added repair tests. It found that passing every currently required part and the item-level review can still counterfeit whole-item closure. This is a D4 owner defect, described below.

## Verdict

**NO-PASS for the Phase E implementation and NO-PASS for the Phase E exit.** Neither passes. One Phase E blocker family remains: E-R1, the retained-history continuation of E-B1. The exact earlier incomplete-scope counterexample is repaired, but the handoff's retained-work/re-partition requirement is not closed. A required subject's failing evidence can disappear from the composite predicate, producing unqualified discharge and releasing dependent work.

E-B2, E-B3 and E-B4 are closed on the requested trajectories and controls. Earlier B2 and B5 remain closed. The required suites pass; they do not discriminate E-R1. This record does not permit Phase F's dependent work to start under G2 §5.1 item 5 and does not accept the implementation at G3.

## Disposition of E-B1–E-B4 and accounting

| Point | Disposition | Executed evidence and limit |
| --- | --- | --- |
| E-B1: partitioned discharge and subjects | **PARTLY CLOSED** | The original incomplete override leaves the whole `OPEN`, with a partitioned route, open-item report coverage and an `OPEN` decision-brief projection. Complete permission yields only `DISCHARGED_PROVISIONAL`. The whole contains all current required parts' subjects. Retained whole-item work and retained work of a replaced part still escape the predicate: E-R1. |
| E-B2: earlier item-level findings | **CLOSED** | Re-integration, a changed transformation target, a prose amendment and replacement partition retain the earlier item-level finding and its reviewer identity in the rendered carry. An author's `TASK_RESULT` claim and a non-independent item-level review do not resolve it; a later independent, acting, unvetoed review explicitly recording `RESOLVED` does. The earlier transformation-review/replacement-part controls also pass. |
| E-B3: entry and newline fidelity | **CLOSED** | Regular, executable and symbolic-link additions expose distinct endpoint types/modes. Deletion, existing mode/type changes, binary identity and ALPHA/BETA controls pass. Terminated and unterminated edits differ. Four actual rendered unified patches apply through Git to reconstruct the exact candidate bytes, covering newline addition, newline removal, and changed text with and without final newlines. |
| E-B4: eligible non-current qualified gates | **CLOSED** | A blocking challenge leaves the qualified decision eligible and visible, with `current: F`, while the production gate term is `F`. Additional unqualified decisions retain its cap/entry; authorized supersession removes it; tenure restart retains it. Eligibility remains owned by `Support.eligible_gate_decisions`, rather than being recomputed by the renderer. |
| E30 | **PARTLY ACCURATE** | Its per-head evidence calls and the new required-part discharge check are real. Its claim that the integrated item's predicate reads every subject's evidence is still false after retained work crosses a partition boundary. Adding subjects to the whole does not ensure that `_composite_predicate` reads them. |
| E38 | **REPAIRED FOR THE REVIEWED CHANGES** | Historical item-level carry, endpoint type/mode and final-newline representation, and eligible qualified entries independent of currency are realized. The earlier B2/B5 evidence/governing-text projections remain honest. The explicit unfinished-work list in §6 remains necessary; this is not a claim that every Manual brief/inspector obligation is implemented. |
| Group 5 count | **TARGETED CORRECTION CORRECT** | Independently counted 31 routing cases, five involving fences, and four separate identity cases. G2 §5.3 now reports that correctly. One other current table still says 32: N1 below. |
| Phase E front matter | **CORRECTED** | The bound plan blob now includes accepted A9/SD-62, consistent with its §7. The new shadow genesis remains a separate human gate. |

## Phase E blockers

### E-R1 — Retained subjects still escape discharge across partition history

**Relationship:** remaining E-B1 family, not a regression of its exact original fixture. Two histories expose the same failure to compose the item's complete retained work with its current required execution parts.

**Owner text.** Manual §10.4 defines an item obligation's subject as the union of subjects changed by every integrated enactment and says a re-dispatch never narrows the terms it reads; discharge is not latched. Its subject evidence and undisputedness are discharge inputs. §10.5 allows provisional discharge only in the permitted scope and forbids unqualified closure through a `P` input. §13.7 partitions the execution, never the item, leaving the item and its scope unchanged. Every required part and the item-level review must hold; this does not waive the item's other discharge terms. E30 repeats the per-head requirement.

**Implementation owners at the candidate.**

- `orchestrator/src/ssds/derivation/items.py:241`, `subjects`, unions the whole's outputs with the **currently required** parts' subjects. It does not retain integrated output subjects from a part that `parts` removes as replaced (`:404`, particularly `:416`).
- `items.py:325`, `predicate`, returns `_composite_predicate` before the subject-term loop at `:335`. `_composite_predicate` (`:501`) reads current parts' predicates and the item-level review, but never the whole's historical subject terms. Thus even a correctly retained subject in the whole's own `subjects` set can be ignored.
- `items.py:513`, the new discharge guard, sees no open required part in these histories. Each new part genuinely passes its own narrowed predicate, so the guard does not prevent false whole-item discharge.

**Executed trajectory A: work integrated by the whole before its first partition.**

1. Use a lint-valid `DOCUMENT` item with obligations `o1`, `o2`, `o3`, budget 2 and write scope `records.md` plus `notes/`. `records` is a D4 subject whose domain requires evidence `health`; the two note subjects are evidence-record homes. The required hard checks include test integrity and write scope.
2. Integrate the whole item's independent-reviewed change to `records.md`; admit a realization about its exact retained revision and a passing `health` assessment. The item is `DISCHARGED`.
3. Admit a counting failing assessment of that realization. The item correctly reopens: `ev(records, health)=P` and `qual(records)=P`. There is no provisional permission.
4. A second, incomplete attempt spends the whole's budget. Partition `o1` to scope `[records, notes.a]` and `o2,o3` to `[notes.b]`.
5. Complete and integrate the first part by changing only `notes.a`, preserving the earlier `records` bytes; complete and integrate the second by changing `notes.b`. Admit an independent passing item-level review. Both parts have clean conformance and current passing reviews. The retained `records` revision is still exactly the realization's claim revision; its failure is still counting.

The whole's subject set correctly includes `records`, but the composite predicate never reads its `P` terms:

```text
whole.subjects = {records, notes.a, notes.b}
part subjects = {notes.a}, {notes.b}
ev(records, health) = P; qual(records) = P
current(item-level PASS) = T; both part predicates = T
whole.predicate = T; whole.discharge = DISCHARGED
whole.route = discharged
```

**Executed trajectory B: work integrated by a subsequently replaced part.**

1. Start with the same item partitioned into `o1` on `[records, notes.a]` and `o2,o3` on `[notes.b]`. Integrate the first part's change to `records`; admit passing `health` evidence; integrate the second part's note change and pass the independent item-level review. The item discharges.
2. Admit the counting failing assessment. The first part and the whole correctly reopen. A further incomplete attempt spends that part's budget.
3. Re-partition only that part into a replacement `o1` part with the same `[records, notes.a]` scope. The discharged sibling stays required. Complete the replacement by changing only `notes.a`, preserving the original `records` bytes, and pass the new independent item-level review.

Now even the whole's subject set loses `records`, because its original producing part is no longer required:

```text
required parts = discharged old sibling, completed replacement part
whole.subjects = {notes.a, notes.b}  # retained records omitted
ev(records, health) = P; qual(records) = P
current(item-level PASS) = T; both part predicates = T
whole.predicate = T; whole.discharge = DISCHARGED
whole.route = discharged
```

**Permission and consumer discriminators.** I ran both histories with no override, with an override listing the item/kind but no subjects, and with complete permission for `[records, notes.a, notes.b]`. All six variants return unqualified `DISCHARGED`. Required results are respectively `OPEN`, `OPEN`, and at most `DISCHARGED_PROVISIONAL`.

These are schema-checked histories through the installed `ssds` derivation, not substituted predicates. Both items in the consumer fixture pass lint; the follow-up item is issuable and depends on `work`. At the failing head:

| Consumer | Observed result |
| --- | --- |
| Whole item route | `discharged` |
| Decision brief's item-state projection | `discharge DISCHARGED` |
| `Reports.open_item_units()` | omits `records` |
| Follow-up item's real readiness | `READY`, no waiting entry |

The suite is green while these final assertions fail: two supplemental methods, six failing subtests, zero errors. Scratch reproduction and full observations are `retained_controls.py` and `retained_controls.log` under `/tmp/ssds80-phase-e-rereview-89684fb/`. The initial simpler reproductions are in `retained.py`/`retained.log`.

**Minimum repair.** Reconcile retained output/subject history and its current per-head discharge terms at the existing item/partition owner. Preserve materially retained work of the whole and of replaced parts, and apply its evidence, undisputedness, challenge and gate terms when composing the item. Keep every required part's own permission check and the independent item-level review. Reconcile the restoring route and dependent consumers as part of that repair: merely forcing the whole `OPEN` while every part and the same already-answered item-level review stay discharged is not route closure. No parallel presentation predicate, registry or weakening of §10.4/§13.7 is needed to establish this requirement.

**Required discriminator.** Replay both histories above. Without permission or with incomplete permission the item must stay `OPEN`, the dependent item must wait, and an applicable restoring route must be ready or visibly waiting. Complete permission must never give unqualified discharge. The whole's retained subject reach must include `records` in both histories. Retain the passing original incomplete/complete-scope cases, the discharged-sibling/re-partition controls, the item-level review requirement and the answer-qualified lifecycle properties. Reconcile E30's completion claim against those real-owner results.

## Findings for later phases

No new later-phase mechanism requirement is established. The earlier boundaries remain: Phase F owns dispatch/attestation, integration and general Admission, runner realization, issued briefs and remaining protocol-source resolution; Phase G owns intake/migration/external pilots; Phase H owns its adversarial/fault qualification. A9's continuing prohibition on removal of the unclassified leaf belongs at Phase F's general structure-change Admission owner. The replacement A9 shadow genesis is a separate authenticated human gate.

The Phase E plan §6 still discloses unfinished merge/upgrade/annotation behavior, the R3-decision floor and review-qualification limitations, confidentiality aggregates, analyzer/relation/coarse-subject notices, specification-change stale-failure review items, unsupported obligation briefs, complete doctrine-source resolution and digest acknowledgment. These remain obligations for the acceptance boundary that requires them; this review neither executes nor waives them. E-R1 is already a Phase E discharge/route/consumer defect and cannot be deferred to those owners. Campaign, burden and doctrine measurements still need their own frozen plan, Review and authorization.

## Non-blocking findings

**N1 — one remaining count residue.** G2 shadow workplan §4.12's RR-5–RR-8 table row still says `S3 routing cases (32)` at line 257. Its §5.3 acceptance-group row has been correctly changed to 31, five fenced, with four separate identity cases. Reconcile that other current summary to the independently counted inventory. This does not establish a missing case or another Phase E blocker.

**N2 — disclosed group 6 sensor limitation remains.** The generic no-stranded property does not establish the existence of every revalidation route. A fresh control derives two revalidations; suppressing `_revalidations` derives zero while that property's answer remains empty. Direct revalidation tests pass in the full suite. Keep the property paired with those direct tests; do not expand its claim. This is the earlier disclosed limitation, not a newly discovered implementation regression.

No additional material scientific finding or new architecture defect was established within this bounded review.

## Verification, reuse and gaps

All scratch, candidate copies, environment/build/dependency caches, temporary directories and SSDS homes used by this review are under `/tmp/ssds80-phase-e-rereview-89684fb/`. The suites used CPython **3.11.15**, UID **1000**, and a newly installed candidate wheel. Independent probes imported `ssds` from that scratch venv's `site-packages`; the repository's Core runner intentionally uses its source path and separately exercises installed wheel/sdist products. No `~/.ssds` operation was performed.

| Required command at the candidate | Final result |
| --- | --- |
| `python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt` | completed; candidate wheel built and installed |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | **462 tests, OK, 2 skips**; only the optional slow lifecycle methods skipped |
| `python orchestrator/scripts/run_core_tests.py` | **393 tests across 13 modules, OK**, including fresh wheel/sdist installed-product tests |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | current snapshot matches canonical source; historical snapshots immutable and coherent |
| `python -m unittest discover -s tests -v` | **435 tests, OK, 3 skips**; optional remote historical fallback realizations not enabled |
| `git diff --check b7912159 89684fb9` | clean |

The first installation attempt could not resolve the network for isolated build dependencies; the same requested installation completed with network access. The first offline Core run could not find a Python-3-compatible `shellingham` wheel because my scratch wheel-cache reconstruction selected its Python-2 tag. Correcting that scratch cache to use the wheel's declared Python-3 tag allowed the unchanged full Core command to pass. No candidate code or test was changed to clear either environment failure.

Additional executed evidence:

- Seven exact earlier constructions were rerun against this candidate, changing only their scratch import root: evidence regression, challenged-evidence projection, historical governing text, carry after amendment, qualified gate visibility, and the two content-distinct diff candidates.
- The earlier review's **14 supplemental methods all pass** on the candidate. These include retained subjects within an unpartitioned obligation, original permission controls, replacement-part transformation carry/resolution, integrated item-level carry, historical item review, diff controls, gate supersession and tenure restart.
- **Seven new supplemental methods pass**: original partition-scope consumer agreement, complete-scope provisional agreement, item-level carry across changed target/amendment/replacement, the explicit resolution/author/non-independence controls, and non-current gate currency/term agreement.
- **Two retained-history methods fail in six final subtests**, as E-R1 records. Every subtest reaches the intended discharge assertion after clean lint/conformance, retained claim-revision identity, independent current item-level review, and live `P` evidence/qualification checks.
- **Four rendered-diff round trips pass** through `git apply`, checking bytes rather than only the presence of a newline marker.
- **Six in-memory owner rollback variants** were evaluated: restoring both old E-B1 owners, old item-level carry, old diff, old gate projection, and the old subject union each produces an assertion failure with zero errors. Restoring only the old discharge method remains green in the original permission fixture while the repaired subject union remains active; this is overlapping protection, not evidence that either isolated test qualifies every retained-history case. The separate N2 revalidation-removal variant confirms the sensor limit above. No installed source file was mutated.
- A9's preparation/admission refusal tests pass in the SSDS suite. A fresh outer-owner control assigns a newly added otherwise-unowned `new-root.txt` to `ssds.unclassified`, and the real write set includes that owner.

**Evidence reused with bounded applicability.** I reuse the earlier reviews' step-3 through step-7 owner audits and historical reversion evidence for unchanged repairs, bounded by the fresh full regression. B2's production evidence/query projection and B5's exact-revision governing-content owner did not change; their original and supplemental trajectories were rerun and remain closed. No prior green result was used to close the changed partition predicate or retained-history surface.

The full `SSDS_SLOW=1` production enumeration was not rerun; it is optional in this handoff. I reviewed E15's recorded post-repair run at `c91b1bb28d0082a4058c3ab7d168b5275ccb8ce5`: 7,254 chains, P1–P6, no violation, 1,435 seconds. The interval from that commit to the candidate changes only the Phase E plan. Fresh standard lifecycle tests pass. This inherited enumeration concerns its budget-spent/item-level-no-part fixtures; it does not cover the retained failing-evidence histories above, and cannot refute them. Fence/P7 remains Phase F's.

**Frozen and shadow boundaries.** The repair delta changes no `source/`, `dist/`, Core implementation/tests/resources, content, ledger, Admission or frozen Architecture 1.6.0 owner. Inspection of the whole Phase E interval against the baseline shows only the already-reviewed additive Core API/profile lookup changes on the Core source boundary. Fresh Core, snapshot and repository tests preserve the accepted behavior. I reuse the recorded private `ssdp-shadow` read-only command run only for its original empty-native-work state: these repairs change neither the qualification/home boundary nor that ledger, and its absence of native work does not exercise these changed item/carry/gate paths. The unchanged command read-only checks also ran in the current SSDS suite. I did not read the private ledger, move its high-water mark, approve a replacement genesis or infer native fitness from it.

**Gaps.** No fresh exhaustive production lifecycle replay, private-ledger run, optional remote fallback realization, live/native trajectory, campaign, exhaustive partition/structural-migration/analyzer qualification or unbuilt later-phase execution is claimed. No required handoff command remains unexecuted after the final successful runs. E-R1 is an executed blocker rather than an evidence-availability gap. Its route-preserving repair remains unverified.

## Project Engineering Memory applicability

The G2 workplan explicitly binds PEM. I independently resolved the project-designated integrated line `main` at `af0455753e20ee54a969c844872e29e270007211`, the exact workplan-bound base. Its PEM blob is `1561797125622f355f84eb27319f87e8fa4227d9`, byte-identical at this candidate; no candidate overlay is composed. Schema validation passes: five families, zero notices. Canonical family metadata, including applicability dimensions beyond temperature/summary visibility, was searched. Coverage remains PARTIAL; missing metadata or absent history cannot prove absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: G2 section 2 and the current Manual/Core boundary independently require frozen-resource preservation; fresh checks retain it.
  - id: DS-001
    disposition: APPLICABLE
    reason: Green modeled or selected histories do not qualify omitted real-owner retention trajectories; E-R1 and the N2 control demonstrate the limit.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No canonical source-to-generated-package routing repair is performed.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No immutable fallback or recovery publication is performed.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: This review creates no bootstrap or fallback designation.
```

No PEM update, recurrence count or promotion is made. The current D3 owners supply the retained-work and preservation requirements. The repeated discharge family calls for reconciliation of complete work history at the existing owner before another additive repair, without preserving an accidental helper or introducing a parallel authority surface.

## Scientific checks and common-mode limits

- **Material findings:** E-R1 is the remaining Phase E blocker; N1 is count residue and N2 is the already-disclosed evidence-sensor limit. No Serious Challenge or scientific finding was established.
- **Realized scientific results:** I produced, ran and reviewed **no realized scientific results**. Null envelope: synthetic ledger histories, derivation/rendering controls, byte reconstruction, regression, installed packaging and snapshot checks only. No empirical scientific, numerical convergence/precision or engineering-outcome-superiority claim was evaluated.
- **Variants evaluated:** seven earlier constructions; fourteen inherited supplemental methods rerun; seven new supplemental methods; two retained-history constructions crossed with three permission regimes, selected to discriminate subject loss and false unqualified closure; four newline patch round trips; six owner rollback variants plus the N2 sensor-removal variant. These counts describe software probes and bounded oracle checks, not independent scientific samples or an exhaustive search. Selection was exploratory and consequence-driven.
- **Tension search:** no consequential judgment relies on accepted D1/D2 scientific authority, so no scientific tension search is claimed. The reviewed predicates are D3 governance semantics exercised by synthetic D4 evidence. The bounded architectural Challenge pass is recorded above.
- **Unanswered parts:** the explicit verification gaps and E-R1's unverified repair remain open. No unexecuted optional/later work is silently converted to a pass.

This context is independent of the Claude-family author but shares the OpenAI GPT family with the preceding different-family reviews. The Manual, catalogue, scenario helpers, Python/Git environment and much of the regression corpus are common dependencies. Reusing the earlier probes reduces construction independence; the retained-history variants, real dependent consumer, exact-byte patch application and explicit rollbacks add distinct discriminators. They do not establish universal adequacy or live operational qualification.

Nothing beyond shadow is authorized. This review accepts no implementation at G3, authorizes no replacement genesis, campaign, live task, authority cutover or G4, and changes no subject's governance. No commit or push was made. The sole repository write is this review record; all scratch is under the handoff's named directory.
