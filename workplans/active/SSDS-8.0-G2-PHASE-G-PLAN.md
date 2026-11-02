---
kind: ssds-shadow-phase-plan
workplan_id: SSDS-8.0-G2-PHASE-G-PLAN
protocol_version: 7.2.1
target_system_version: 8.0.0
status: draft (revision 3; proposed, not accepted; same-family plan check of revision 1 NO-PASS (B1-B6), narrow re-check of revision 2 NO-PASS (RB1, RB2), both repaired; narrow re-check of revision 3 PASS; questions Q-G1 to Q-G7 open)
created_date: 2026-11-02
governing_workplan: workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md (revision 4, accepted SD-99; Stage D, §5.1 rules, §5.2 Phase G row, §5.3 group 7)
governing_architecture: orchestrator/docs/ssds-8.0-architecture.md (accepted at G1, SD-50; amendments A1-A10 accepted, SD-53, SD-55, SD-60, SD-62, SD-66)
g2_authorization: SD-55 (shadow implementation only)
previous_phase: workplans/active/SSDS-8.0-G2-PHASE-F-PLAN.md (completed; exit accepted at 36b0ab5f, SD-104)
active_serious_challenge: none new (SC-U4 stays open at its owner, G2 workplan §5.7; it blocks no Phase G work)
---

Governing SSDP version: 7.2.1.

# SSDS 8.0 — Stage D Phase G plan: intake and migration pilot

```text
STATUS: DRAFT, revision 3 (2026-11-02). Proposed; not accepted; nothing built. Same-family plan check of
        revision 1 NO-PASS (B1-B6), repaired in revision 2; its narrow re-check NO-PASS (RB1, RB2), repaired
        in revision 3 (§9); its narrow re-check PASS. Companion to the G2 shadow workplan, Stage D
        (§5.2 Phase G row). It concretizes that row into owners, steps and test groups. It
        adds no mechanism beyond the settled register (G2 workplan §4.2) and changes no Manual decision.
START:  Phase F's exit accepted at 36b0ab5f (SD-104) lets Phase G's dependent work start under this plan
        (G2 workplan §5.1 item 5). SD-104 accepts nothing toward G3 and authorizes no campaign, native
        authority, cutover or real-ledger operation beyond SD-55 and SD-59.
SHADOW: no SSDS authority over any subject; every subject LEGACY(p) or UNGOVERNED on every real ledger; no
        cutover. The document-controlled 7.2.1 baseline governs. Cutover cases run on fixture and scratch
        ledgers only, and no subject of a real ledger changes mode (G2 row; reading GR1).
BLOCKERS: none to start steps 1-6, 8 and 9 (fixtures and scratch only).
        - Step 7b (a cutover enacted at its carrier's integration) needs an admitted TASK_RESULT and an
          accepted integration, which SD-70 keeps SCHEMA_UNSUPPORTED until A10's D4 (with SD-71's 5e/5f and
          SD-73's 6f/6g in the phase that lifts that gate). Six of group 7's seven named discriminators sit
          there. Sequencing is Q-G1.
        - Steps 10 (Case B on ssdp-shadow-3) and 11 (Case C/D on an external repository) touch a real ledger
          or an external repository. Each stops for the stakeholder's explicit authorization first
          (Q-G3 to Q-G6). No real-ledger or external-repository access happens under this revision.
OPEN QUESTIONS: Q-G1 cutover sequencing; Q-G2 intake.neutral_auto (Q-F18's continuation); Q-G3 the external
        repository and its owner's permission; Q-G4 the clone and how it is observed; Q-G5 the pilot ledger;
        Q-G6 Case B on ssdp-shadow-3; Q-G7 Q-F6 (ii) and the canonical form of A (§7).
PRECONDITION: D-C7-OBJECTS (Phase F exit evidence §5) before any Phase G field gains a new producer (§1).
NEXT:   the stakeholder's answers to Q-G1 to Q-G7 (Q-G1 also
        confirms GR1); then step 1 (survey). No Serious Challenge identified; reading GR2 (A9 emptied §18.2's
        "uncovered" region) goes to the Manual clarification batch.
```

## 1. Scope and authority

The G2 workplan's Phase G row builds, shadow only:
- **intake** (Manual §18): detection, static classification, the nine dispositions and their effects, structural intake, adoption and realignment, the offered-candidate path;
- **the migration path** (Manual §19) for this repository's legacy documents (genesis Case B) and for **one external scientific repository** (Case C/D) on a read-only clone with its owner's permission;
- **external units** (Manual §20): pins, external acceptance and consultation, another SSDS ledger read-only, multi-repository change.

It realizes register rows §18-§20 (G2 workplan §4.2: §18 accepted by inspection; §20 accepted as data, its pins feeding §6's `ext` with the S5 §6 cases as evidence; §19 accepted with the cutover-carrier window case) and the §7 frame rows group 7 carries. Its exit evidence for G3 is **acceptance group 7**, with cutover cases on shadow ledgers and fixtures only, no subject changing mode.

This file decides only D4 placement and order. Every behaviour cites the register row it realizes; a behaviour no row covers returns to Stage S (G2 workplan §5.6). G2 workplan §5.1 applies unchanged:
- expected values come from the register, the Manual decision behind each row and the Stage S cases as written, never from running `qualification/ssds80/models/`, and production code never imports them (item 3); the catalogue's §31.4-§31.8 tables supply none (§4.2's last rows);
- real owners (item 4); fixtures alone qualify only mechanical properties (DS-001);
- Core's suite and the frozen-profile tests pass unchanged (items 1 and 6);
- no live agent run without an authorized campaign (item 7): every agent-role record in Phase G is a fixture record signed with a fixture key, or a human record signed by the stakeholder.

The Phase D threat boundary for the SSDS home (SD-59) holds for every operator file Phase G writes. Phase F's carried disclosures (exit evidence §5, SD-103) keep their owners. One of them binds Phase G directly: **D-C7-OBJECTS**, the C7 audit of object-typed fields (`fields`, an `execution` basis, lifecycle `controls`, genesis `fields.approval`, `TASK_RESULT` `slots`), "done before any of them gains a new producer" (exit evidence §5; Phase F reading F125). Phase G adds such producers: intake, migration and external-unit records with `fields`, the lifecycle records `MODE_TRANSITION` and `LEGACY_RELEASE` (`controls`), and step 11's new genesis (`fields.approval`). So the audit is a precondition of steps 2, 6, 7a, 8 and 11, each for the fields it gives a new producer.

**Bindings.**

| Binding | Identity at drafting (`e78ece24b6a8f76a3929c7ca342d82578977a197`) |
|---|---|
| governing protocol | SSDP 7.2.1, resolved from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6…`, recovery `efdd1b59…`) |
| accepted architecture | Manual blob `438cb113b155c2e79715430338a543615fa7f143` (A1-A10 applied) |
| governing workplan | G2 workplan blob `5c73256ec58452a3d961e0459fe78e29db5506b0` (revision 4) |
| mechanism input | catalogue blob `90bf3eae031966bc7f2324082428ef33c381fd46` (binds only through the register) |
| discriminator source | `qualification/ssds80/G2-S4-FINDING-INDEX.md` blob `231717f4e4f52073764410fc1ecbee08bb1e980d` (`STAGE-D` rows) |
| stakeholder record | blob `93eca74be2858a57a9c01ab6b5fe5b4dedb8fbfe` (items 1-86, SD-1 to SD-104) |
| Phase F carry | exit evidence blob `7bd4dac5338259fb26d25c0b759dac85dab59bb9` §5; Phase F plan blob `b5e2b2b57c3ae65df324ccbdc896d4d051c0b22b` §6 |
| live real ledger | `ssdp-shadow-3` (genesis `9d404721`, observes `ssds-8.0-graph-native-architecture`); its genesis manifest is `.ssds/manifest.toml` (Case B already: `ssdp.protocol` and `ssds8.manual` `LEGACY(7.2.1)` with section-level parts; `orchestrator.program`, `ssds.unclassified`, `ssds.manifest`, `ssds.policy` `UNGOVERNED`) |
| PEM | cold. The G2 workplan's basis (`main` at `af04557`, HAS PC-001, DS-001, SP-001, SP-002, FF-001) stays the recorded basis; Phase G replaces no mature machinery. Reopen: a step that replaces or consolidates mature Phase D-F machinery, or a recurring failure family (AGENTS.md PEM triggers) |

**What Phase G does not build** (each later owner's, with reason):
- accepted integrations, `TASK_RESULT`s, the rebase, no-collateral regression, fences and the publisher side: the phase that lifts SD-70's gate (A10's D4; SD-70, SD-71, SD-73). Whether step 7b waits for it is Q-G1;
- §24.2's replacement lineage, F47's ref restore, recovery under `INTEGRITY_HALT`, faults beyond group 4's (Phase H; SD-75, SD-76);
- any live agent trajectory, real-runner execution on a real ledger, or measurement (a campaign, G2 workplan §5.1 item 7). Reconstruction proposals, intake classification by an agent and the Investigator role's live work are therefore exercised with fixture records only;
- Dispatcher predictions and anything U1-U4 gate (G2 workplan §5.7);
- moving any real-ledger subject to `NATIVE` (a cutover, G4), or any other mode change on a real ledger (GR1).

## 2. Placement

The component table of Phase D plan §2, as Phase F filled it, stands. Phase G fills owners as follows (Manual §26.1 ownership; dependency direction `Content, Analyzers <- Derivation <- {Admission, Interface, Dispatcher}`).

| Owner | Gains in Phase G | Register rows |
|---|---|---|
| `content` | a validated, repository-contained relative path grammar for `paths` targets (Manual §25.4; Phase F review 8230421 N3); read-only access to an external clone through the existing object readers (GR5) | §18.2, §25.4 |
| `analyzers` | the static classifier (§18.2): a versioned, bounded, non-executing function proposing `(kind, domain, class)` for a path from path and extension, fixed magic bytes and text/binary detection, Git history, known producers and data-only manifest parsers; opaque active content proposed `QUARANTINE`. Reached by the Dispatcher only through a `derivation` query that derived state never consumes (GR3) | §18.2 |
| `derivation` | intake objects and their `INTAKE` obligations per quarantined delta and per foreign or unclassified change, keyed by intake object (Phase F review N2, plan line "keying the obligation by delta is for Phase G"); `QUARANTINE`'s S2 effect (subjects under its paths treated as `UNCLASSIFIED`, `ok = F`, following paths, not content); contrary dispositions (veto of an enacted `ABSORB`'s support, the owner's adjudication, the realignment obligation where upheld); `RECONCILE`'s follow-on, only as an owner defines it (GR4); offered-candidate intake (conservative basis from the merge base, §4.5 widening); non-cutover mode transitions at admission; reconstruction status; the cutover frame's obligations and source-mode existence condition (catalogue §7.4); external-unit currency and consultation supersession | §18.1-§18.5, §19.1-§19.7, §7.4-§7.6, §20 |
| `admission` | `INTAKE_CLASSIFICATION` admitted as an R0 machinery proposal; every §18.3 outcome of `INTAKE_DISPOSITION` admitted with its checks; `MODE_TRANSITION` (non-cutover at admission; cutover record in the carrier's frame within its window), `LEGACY_ACCEPTANCE`'s scope rule, `LEGACY_RELEASE`, `RECONSTRUCTION_PROPOSAL`, `EXTERNAL_ACCEPTANCE`, `EXTERNAL_CONSULTATION` with mandatory supersession; the cutover enactment conditions at the carrier's integration (step 7b, Q-G1) | §18.3-§18.4, §19, §20.2 |
| `dispatcher` | the intake census (submitting classifier proposals and absorption requests, §18.1); advisory re-consultation and newer-external-revision obligations (§20.2, §20.4); the periodic binding-health check of `REPO`, `HOME` and `RUNNER` references (SD-82), with Phase F's carried notes | §18.1, §20, §17 (SD-82) |
| `ledger` | read-only consultation of another SSDS ledger under its own witness model (§20.3), through the existing qualification read path | §20.3, §23 |
| `interface` | intake views (each quarantined delta beside its effective value with the absorption that introduced it, §18.5), intake and migration briefs; no new transport | §16, §18.5 |

**Operator trees.** None new in the real SSDS home. The external pilot's ledger lives where Q-G5 decides; until then every Phase G ledger is a fixture or lives in a scratch SSDS home.

**Fitness.** No new exception to Phase D rule B1 and no new edge in the dependency table (`orchestrator/tests/ssds/fitness.py` `ALLOWED`) is planned:
- the classifier starts no process, and the Dispatcher, which has no edge to `analyzers` (rule F1), reaches it only through `derivation`'s public API (GR3);
- the external clone is read through `content`'s readers, which only `derivation` and `analyzers` import;
- consultation qualifies the other ledger through `ledger.qualification` (an edge the Dispatcher has) and reads its derived status through `derivation`, which reads ledgers (`ledger.read`).

A step that needs a new edge or exception stops and comes to the stakeholder (§8).

## 3. Steps, in order

Steps 1-6, 8 and 9 use fixtures and scratch repositories only. Step 7a needs no integration; 7b does (Q-G1). Steps 10 and 11 each begin only after the stakeholder's explicit authorization for that step (§8). Each step ends with a same-family review; the phase ends with one other-family Review of the frozen candidate (review allocation).

| Step | Modules | Realizes register rows | Tests (under `orchestrator/tests/ssds/`) |
|---|---|---|---|
| **1** survey (read-only) | none: map every Phase D-F intake, mode, frame and external-unit owner; every fail-closed site Phase G lifts (engine `SCHEMA_UNSUPPORTED` sites for `INTAKE_CLASSIFICATION`, non-`ABSORB` outcomes and `MODE_TRANSITION`; reading F1's observe-only allowlist; `STRUCT_MODE_MIXED` for a cutover); and the sites that stay closed (an adoption with a candidate and a non-empty `adopts`, SD-70 and Q-G7; F16 and Q-F6 (ii)). Trace each group 7 case (§4) to an existing test by its cited name, or to the step that adds it. Scope D-C7-OBJECTS for each step's new producers | — | output: plan revision 2 detailing steps 2-9 in parts with readings, checked before any build |
| **2** intake records and paths | precondition: D-C7-OBJECTS for the intake kinds' `fields`, including the outcome fields step 4 adds (such as a `QUARANTINE`'s `paths`) (§1). Also settles which key binding admits an R0 `INTAKE_CLASSIFICATION` from the Dispatcher: Manual §25.1 lets the issue key authenticate "Dispatcher-submitted observations", and Phase F reading F77 binds keys to the kinds they sign, but `INTAKE_CLASSIFICATION` is a judgment kind; if no owner text covers it, it goes to Stage S. `content`: the `paths` grammar (no absolute path, no `..`, no NUL or control character, normalized, inside the governed tree); `admission`: `INTAKE_CLASSIFICATION` admitted as R0 machinery, enacting nothing, target `{paths}` or a quarantined delta (SD-70, Q-F8 (a)); `derivation`: `INTAKE` obligations per intake object, routed beyond `INTAKE` (briefs, views) | §18.2, §18.5, §25.4 | each path-grammar refusal; a classification enacts nothing (derived state unchanged); one obligation per delta and per foreign change; 441cf5c N8 (§4) |
| **3** static classifier | `analyzers`: the classifier, versioned, its identity recorded in each proposal; its Git-history input comes through `content`'s readers, since `analyzers` may start no process (rule B1); `derivation`: the query exposing it (GR3); `dispatcher`: the census submitting proposals through the ordinary request path, under the key binding step 2 settles | §18.2 | per input class (extension, magic bytes, text/binary, history, known producer, data-only manifest) its proposal; opaque active content (binary, archive, notebook with outputs, executable, serialized object, unknown format) proposed `QUARANTINE`; bounded reads (a file over the bound read only to the bound); nothing executed, imported or deserialized (a planted payload fixture leaves its marker untouched) |
| **4** dispositions and their effects | `admission`, `derivation`: all §18.3 outcomes on a delta or observed content; `QUARANTINE`'s path rule (names only its intake object's paths) and S2 effect; contrary dispositions, with the realignment obligation where the owner upholds one (catalogue §18.4); `RECONCILE`'s "an item or obligation follows" only as far as an owner defines its kind, else to Stage S. Every other outcome is classification and its stated effect only, and derives nothing (GR4) | §18.3-§18.5 | per outcome its effect from Manual §18.3-§18.4, and no derived obligation for `SPLIT`, `ARCHIVE`, `RETAIN_AS_EVIDENCE`, `MARK_GENERATED`, `REJECT` or `DISPOSABLE`; 53669a5 B3's case (a contrary disposition and the owner's adjudication after an adoption are admitted; upheld, a realignment obligation follows); an `ABSORB` under a standing adverse disposition refused (existing, re-cited); a `QUARANTINE`d path's subject has `ok = F` and leaves it when the content moves out of the paths |
| **5** offered-candidate intake | `derivation`, `admission`: an offered external branch or workspace content outside a reported result as an intake object, its basis computed conservatively from its merge base (mechanical minimum plus widening, §4.5), provenance recorded (Case E); its integration stays `SCHEMA_UNSUPPORTED` (SD-70) | §18.1, §19.9 Case E | basis widening from the merge base; obligations from touched units; the candidate never reaches the ref |
| **6** migration records | precondition: D-C7-OBJECTS for the migration kinds' `fields` and lifecycle `controls` (§1). `admission`, `derivation`: non-cutover `MODE_TRANSITION` acting at its admission (fixture ledgers only, GR1); a membership change between subjects of different modes needs its record; `LEGACY_ACCEPTANCE`'s scope rule (no whole-document import onto a section) and provisional reliance without an import (§19.2); `RECONSTRUCTION_PROPOSAL` and status accepted through the owner (§19.3); byte-preserving refinement; promotion, demotion, restoration and carve-out with `LEGACY_RELEASE` and the three locks (§19.4, §19.6). A domain change keeps failing closed (Q-G7) | §19.1-§19.4, §19.6 | per rule a case from its Manual sentence; Case D's "a production edit makes non-current exactly the reconstruction judgments whose basis named it" (§19.9) on a fixture |
| **7a** cutover records and frame | precondition: D-C7-OBJECTS for `MODE_TRANSITION`'s `controls` (§1). `admission`: the cutover record's window (a designated authenticated human; the carrier's item of the right kind naming `s`; once per enactment; refused after the carrier integrated; refused declaring the admitted frame); `derivation`: the source-mode existence condition (catalogue §7.4), and `REVIEW(s, r)`, `ACCEPT(s)` and the cutover gate derived in the carrier frame from the ledger alone | §19.5, §7.4-§7.5 | S5 §19 `cutover_record_after_carrier_integrated_refused`; 051cce3 N5, 362af9f N6, 61cd09b N6 (a), (c), 63ddf91 N5, f03b15e N5 (§4). Where a case needs the carrier's admitted `TASK_RESULT`, it runs on a fixture ledger whose earlier entries the test builds, entries Admission itself would refuse today (SD-70). That is a new pattern (Phase F's frame trial ran on derivation histories only, plan §6), so it qualifies the record path's mechanics only (DS-001), and the report says so (GR8) |
| **7b** cutover enactment and rollback | `admission`: conditions 1-6 checked at the carrier's integrating admission with §7.6, quiescence record and human gate; the rollback `MODE_TRANSITION` to `LEGACY(p)` ending tenure; a re-cutover a new enactment and run. **Needs an accepted integration (SD-70): Q-G1** | §19.5, §19.7, §7.6 | 61cd09b N6 (b), f22b4dc N5, and the integration halves of 051cce3 N5, 63ddf91 N5, f03b15e N5 (§4) |
| **8** external units | precondition: D-C7-OBJECTS for the external kinds' `fields` (§1). `content`, `derivation`, `admission`: the §20.1 pin grammar (Git repository identity with full commit and region; package ecosystem, name, exact version and digest; dataset digest and locator; DOI with variant and locator); an `EXTERNAL` unit never stale; external reads pinned; `EXTERNAL_ACCEPTANCE` with a `record` basis on its consultation, provisional without one; consultation supersession (mandatory for no-longer-accepted, `FORK`, `ROLLBACK` or retired; none for `UNQUALIFIED`); `ledger`: another SSDS ledger consulted read-only under its witness model (two scratch ledgers); `dispatcher`: advisory re-consultation and newer-revision obligations; multi-repository change, derivation half (its admissions under SD-70) | §20 | per pin form valid and invalid; supersession by consultation makes the imports relying on it non-current; `UNQUALIFIED` flaps nothing; an unqualified or retired external head is never imported; the external ledger is never written; S5 §6 `differing_pin_goes_to_owner` re-cited (§4) |
| **9** binding-health check | `dispatcher`: the periodic check of `REPO`, `HOME` and `RUNNER` references (SD-82), with Phase F's carried notes: whether a runner's `AVAILABLE` is limited to its own class's store (9g-ii note 1); a measured component digest beside the declared identity, and the exact supplementary group list (9g-iii note 1) | §17 (SD-82) | a missing reference reported `UNAVAILABLE` under the check's machinery binding; a later `AVAILABLE` by the rule note 1 settles |
| **10** Case B pilot on `ssdp-shadow-3` (**authorization-gated**, Q-G6) | the composition root: the observe-only policy (F1) widened kind by kind as authorized; then the authorized records-only requests: `LEGACY_ACCEPTANCE` imports for `ssdp.protocol` and `ssds8.manual` (GR6), classification proposals over the content `ssds.unclassified` owns (GR2) by the actor Q-G6 names, heuristically extracted relations as proposals only | §19.2, §19.9 Case B, §18.2 | after every command the product repository's refs, reflogs, objects and status unchanged (Phase F step 10's check); each import's applicability as GR6 states it; no `MODE_TRANSITION` |
| **11** Case C/D pilot on an external clone (**authorization-gated**, Q-G3 to Q-G5) | precondition: D-C7-OBJECTS for genesis `fields.approval` (§1). A new shadow genesis over the clone (human gate, new human key, GR7), Case C coarse `UNGOVERNED`/`OPAQUE` subjects or `ssds.unclassified`, Case D's mixed `LEGACY`/`UNGOVERNED` modes only if the owner names a legacy process; absorption of the clone's history as Q-G4 decides; classification, intake obligations and analyzers' derived structure; the real-size operations Phase F deferred (`revisions` folding, checkpoint resume) if the pilot's cost shows them needed | §18, §19.9 Cases C-D, §20 | GR5's no-execution checks, including a hostile repository-local Git configuration fixture first; the clone unchanged after every command (refs, objects, config); derivation from scratch equals the incremental result |
| **12** exit | assembly of group 7; each case executed at its real owner, or reported unexecuted with its owner and decision; the unbuilt items disclosed, §6's among them (`RECONCILE`'s follow-on, if no owner defined it) | §5.2 Phase G exit | the group's results; the shadow boundary checked after every real-ledger and clone command |

## 4. Acceptance group 7: cases, discriminators and expected-value sources

Expected results are transcribed into each test as literal data with the case or finding cited, from the source named in the row. A group 7 case not executed is reported as unexecuted, never as passed (G2 workplan §5.5); none is dropped without recording why (Manual §31.2). Where the Manual and the catalogue differ, the Manual governs and the catalogue binds only through the register row.

**Stage S cases carried** (G2 workplan §5.3 group 7):

| Case | Expected value and source | Real owner, step | State at drafting |
|---|---|---|---|
| S5 §7 frames (9): `one_side_change`, `disjoint_lines_merge`, `overlapping_hunk_conflict`, `binary_both_sides_conflict`, `declaration_key_conflict`, `roles`, `later_iteration_needs_its_own_acceptance`, `same_enactment_counts_once`, `structure_changed_does_not_count` | each case's stated outcome in `qualification/ssds80/models/cases_s5_7.py`; register rows §7.2, §7.3-§7.5, §7.6 (Manual §7.2-§7.6, R12, SD-26) | `derivation` frames (Phase D); Admission's frame trial (Phase F) | eight are cited by name in `test_frames.py` (`roles` as `Roles.test_roles`); `same_enactment_counts_once`'s two halves run under other names (`test_same_enactment_counts`, `test_counts_for_at_most_one_tenure`), which step 1 cites by the case name. Group 7 adds a frame carrying a cutover record (step 7a). A frame carrying an adopted delta `A` from a candidate is not added: an adoption with a candidate stays closed (SD-70; Q-G7 (a) leaves `A`'s canonical element form unsettled), so that case waits for the gate lift and Q-G7 (b) |
| S5 §19 `cutover_record_after_carrier_integrated_refused` | (admitted, refused, refused, refused) for: carrier not integrated, `MIGRATE` item for a D4 subject naming `s`, none recorded; the same after the carrier integrated; a `MIGRATE` item for a D2 subject; an `AUTHOR` item for a D2 subject with a cutover record already admitted in that enactment's frames. Source: `cases_s5_14_25.py`; register §19 row; catalogue §19.5 ("admits it only while…") | `admission`, step 7a | not in the test tree |

**Register §20 evidence, carried beside group 7** (not one of G2 §5.3's group 7 Stage S cases; the §20 row cites the S5 §6 `ext` cases):

| Case | Expected value and source | Real owner | State at drafting |
|---|---|---|---|
| S5 §6 `differing_pin_goes_to_owner` (pins feed `ext`) | as stated in `cases_s5_6.py`; register §6.5 and §20 rows | `derivation`, already run (`test_assessment.py`, `test_phase_f_step9d_iii.py`) | re-cited for group 7's §20 half, not re-implemented |

**Review-named discriminators** (G2 workplan §5.3 group 7; each a `STAGE-D` row of the finding index):

| Discriminator | Case | Expected value and source | Step |
|---|---|---|---|
| **051cce3 N5** | the frame of a refused second carrier: carriers `X1`, `X2` of `s`, each with a cutover record in its frame; `X1` integrates | `X2` has no frame (its record's source mode differs from `s`'s admitted mode), nothing in it is current, it never integrates, the work needs a new iteration; `s`'s tenure is not restarted. Catalogue §19.5 ("once another carrier has cut `s` over…") and catalogue §7.4's source-mode clause, accepted by register §19 and §7.3-§7.5; Manual §7.4, §19.5 | 7a (frame existence on a fixture history), 7b (refusal at integration) |
| **362af9f N6** | cutover obligations derivable from the ledger alone | 362af9f's discriminator (B), as written: two derivation hosts with the same `L_n` and different Dispatcher journals derive identical cutover obligations and identical step-2 verdicts; records for a cutover are admissible only after the ledger holds the task identity they name; a re-issued cutover task leaves no record of the first task counting; an implementation reading the journal must fail. With it, `REVIEW(s, r)`, `ACCEPT(s)` and the cutover gate are derived in the carrier frame, equal from scratch. Sources: the 362af9f Review's (B); catalogue §19.5 (the run is `X`'s enactment, "on the ledger with its task's result before any record names it"); Manual §7.5, §10.2, §26.1 (scheduling never influences derived state) | 7a |
| **61cd09b N6** | (a) who may submit the `MODE_TRANSITION`; (b) when conditions 1-6 are checked; (c) the D1-D3 carrier | (a) only an authenticated human the actor policy designates, as a lifecycle record (Manual §3.5): an agent's or an undesignated human's refused; (b) at the carrier's integrating admission, not at the record's: a record admitted while a condition is unmet, and the integration then refused (no retry within the enactment is asserted, since no owner text states one); (c) an `AUTHOR` item for a D1-D3 subject, `MIGRATE` otherwise: an `AUTHOR` record for a D1-D3 subject admitted, an `AUTHOR` record for a D4 subject and a `MIGRATE` record for a D2 subject refused (catalogue §19.5; the S5 §19 case's input 3 for the last; its input 4 is refused for once-per-enactment, not for kind). Catalogue §19.5; Manual §19.5, §7.6 | 7a (a, c); 7b (b) |
| **63ddf91 N5** | (a) an admitted-frame cutover record; (b) two parallel carriers | (a) refused (Manual §19.1: "a cutover record declaring the admitted frame is refused"); (b) as 051cce3 N5, and the second carrier never enacts a second transition. Manual §19.1, §19.5; catalogue §19.5 | 7a (a; b's frame half), 7b (b's integration half) |
| **f03b15e N5** | (a) the carrier integrates before the cutover record exists; (b) the mechanism of its `VIOLATION` | (a) the later record is refused (`ENACTMENT_*`), `s` keeps its mode, and the cutover needs a further iteration of the item (or a new item once discharged); (b) under the settled rule the record never admits, so no `VIOLATION` arises from it: the test asserts the refusal and the absence of any mode effect. If step 1 finds a surviving catalogue clause that still derives a `VIOLATION` here, it goes to Stage S (§8). Catalogue §19.5 ("If the carrier integrates first…"); the S5 §19 case's input 2 | 7a (record refusal on a fixture history), 7b (end to end) |
| **f22b4dc N5** | a re-cutover by the same requester | after a rollback `MODE_TRANSITION` to `LEGACY(p)`, the re-cutover is a new task, enactment and run; the earlier enactment's prospective acceptance counts for no later tenure; pre-cutover legacy imports never revive (a fresh `LEGACY_ACCEPTANCE` is needed). Identity is by enactment, not requester. Catalogue §19.5's last sentence; Manual §7.6, §19.7; S5 §7 `later_iteration_needs_its_own_acceptance` | 7b |
| **441cf5c N8** | a foreign change to structural declarations only, the semantic revision unchanged | absorbed; each changed key is a quarantined delta classified governance-neutral or governance-affecting (catalogue §1.6's algorithm, register §1.6 row); every subject in `aff(Q)` has `ok = F` until adopted or realigned while routing follows admitted structure; one `INTAKE` obligation per delta; the subject's revision, and so its revision assessments, unchanged. Run a governance-neutral and a governance-affecting variant. Manual §18.2, §18.5 | 2 (with 4 for its disposition) |

**Register-row cases with no Stage S model** (§18 accepted by inspection; §20 as data, beyond its `ext` cases): each behaviour of Manual §18.1-§18.5, §19.1-§19.7 and §20.1-§20.4 that step 1 maps gets a case whose expected value is the cited Manual sentence, with the catalogue clause the register accepted where the Manual is silent. These are mechanical properties at their owners, not discriminators a Review named; they add no case count to the G2 group table.

**Carried into group 7 from Phase F** (Phase F plan §6, exit evidence §5): D-C7-OBJECTS, a precondition of steps 2, 6, 7a, 8 and 11 (§1); intake beyond SD-69's `ABSORB` (steps 2-5); the `paths` validator (8230421 N3, step 2); `INTAKE` keyed by intake object (step 2); the cutover's source-mode condition and a cutover carried by an integration (step 7); `STRUCT_MODE_MIXED` for a cutover (step 7); the periodic binding-health check (SD-82, step 9); `revisions` folding and checkpoint resume (step 11, conditional); `intake.neutral_auto` (Q-G2).

## 5. Readings

Each reading resolves a point the register leaves to D4. It is revised, never silently changed, when a step or its review falsifies it.

- **GR1** *Where modes may change.* This reading interprets the shadow invariant itself, so the stakeholder confirms it (Q-G1).
  - **Real ledgers: no mode change at all.** The G2 row's "no subject changes mode" is read as covering every `MODE_TRANSITION` on a real ledger, not only cutovers. §2 item 1 would allow `UNGOVERNED` → `LEGACY(p)`, but the row is narrower, and Case B's modes are already set at `ssdp-shadow-3`'s genesis. Reading F1's observe-only policy keeps refusing `MODE_TRANSITION` there; any widening of its allowlist is per kind and per the stakeholder's authorization (Q-G6).
  - **Fixture and scratch ledgers: cutovers enacted.** G2 workplan §2 item 1 ("no cutover, no `MODE_TRANSITION` to `NATIVE`") and the row's parenthesis are read as binding the subjects SSDS shadows, the real ones, not fixture subjects in test homes. The justification is the row itself: it asks for "cutover cases on shadow ledgers and fixtures", and group 7's own discriminators need a fixture subject to reach `NATIVE` and come back (f22b4dc N5's re-cutover after rollback; 61cd09b N6 (b)'s conditions checked at integration). A fixture cutover governs nothing outside its test.
- **GR2** *"Uncovered" after A9.* Manual §18.2 and §18.5 speak of uncovered paths, but A9 (§1.8) makes the uncovered region empty: `ssds.unclassified` owns every governed byte no other top-level unit contains. The reading: §18.2's "uncovered paths" and §18.5's "uncovered content is `UNCLASSIFIED`" mean bytes whose innermost owner is `ssds.unclassified`, whose kind is `UNCLASSIFIED` (its mode is `UNGOVERNED`; the reading keys on kind, as `derivation/queries.py` already does). The classifier proposes for those paths, and an `INTAKE` obligation arises per foreign change touching them. It changes no decision (A9's own text names that region as the former uncovered one) and goes to the Manual clarification batch. Step 1 checks it against `derivation`'s current reading before step 2 builds on it.
- **GR3** *Where the classifier lives.* The Manual calls the classifier a versioned machinery function and the census a Dispatcher function, but places the function in no component.
  - It is placed in `analyzers`, a pure function of bytes and Git history like derived relations, its version identity recorded in each proposal.
  - `derivation` exposes it in its public API as a query that no stratum consumes, so derived state never depends on it. This is the only route that keeps the fitness table: the Dispatcher has no edge to `analyzers` (rule F1; Manual §26.1's direction).
  - The Dispatcher's census calls that query and submits the proposals as R0 machinery records through the ordinary request path; a proposal enacts nothing.
  - A test asserts that derived state is identical with the classifier replaced by a stub.
- **GR4** *Dispositions are records; only two derive obligations.* Every §18.3 disposition is admitted as a records-only request. Only two owners state a follow-on obligation:
  - an upheld contrary disposition derives a realignment obligation (catalogue §18.4);
  - `RECONCILE` says "an item or obligation follows" (Manual §18.3), but catalogue §10.2 names no obligation kind for it. Step 1 looks for an owner that defines one; if none does, the follow-on goes to Stage S (G2 workplan §5.6) and `RECONCILE` is admitted as classification only meanwhile.

  Every other outcome is classification and its stated effect only. `DISPOSABLE` is "classification only; deletion is a separate authorized change". A revert, a realignment, a `GENERATED` declaration or a deletion is an ordinary integration someone authorizes, and it stays `SCHEMA_UNSUPPORTED` under SD-70 in Phase G.
- **GR5** *An external clone is untrusted input.* The clone is made by the operator as a bare clone, without checkout, submodule recursion or LFS smudge, and SSDS never writes it. SSDS reads it only through `content`'s object readers; their environment sets `GIT_CONFIG_NOSYSTEM` but does not override repository-local configuration, so step 11 first proves that a hostile repository-local configuration (for example `core.fsmonitor` naming a marker script) runs nothing under every read SSDS performs, and fixes the reader if it does. Nothing from the clone is executed (no runner without a campaign); analyzers and the classifier read bounded data. The ledger keeps every content commit it references reachable (§21.2), so the pilot ledger holds a copy of the external repository's objects: the owner's permission must cover that custody (Q-G3).
- **GR6** *A legacy import applies only to the revision its process accepted.* A `LEGACY_ACCEPTANCE` supplies acceptance for exactly `(subject, scope_id, rev)` (§19.2). For `ssdp.protocol` the cited acceptance is the 7.2.1 release (its `PROTOCOL-RELEASE-STATE.yaml` entry and its Review and ratification records at immutable identities); if `source/` at the observed head differs from that release's tree, the import does not apply to the current revision and reliance stays provisional. For `ssds8.manual` the cited acceptance is G1 (SD-50) with the accepted amendments A1-A10. SD-66 directs that A10 be applied "word for word"; the current blob `438cb113b155c2e79715430338a543615fa7f143` is the text its acceptance commit `39ad6f13` applied, and the Manual has not changed since. (SD-66's pre-application blob `fe43f04f5a698688727f7473a7c2e4d5345ae911` is the pre-A10 text, not a candidate.) The import names `438cb113`; whether that word-for-word application counts as the accepted revision for a `LEGACY_ACCEPTANCE` is the stakeholder's call in Q-G6. Either outcome is a real result to report, not to patch.
- **GR7** *Human keys across ledgers.* SD-89 holds: no human key is registered on two live ledgers. The external pilot's genesis uses a new human key the stakeholder generates, not `ssdp-shadow-3`'s.
- **GR8** *Fixture cutovers.* Cutover cases run on fixture ledgers whose carrier `TASK_RESULT`s are signed with fixture keys in test homes; this exercises Admission's record path and derivation without a live agent. Under Q-G1 (b), a case whose distinguishing step is the integrating admission is reported unexecuted, never passed by driving the trial alone.

## 6. Fail closed until a later owner

- Until the stakeholder answers Q-G1, step 7b is not built and its cases are reported unexecuted; accepted integrations, `TASK_RESULT`s and everything SD-70, SD-71 and SD-73 defer stay `SCHEMA_UNSUPPORTED`.
- Until Q-G2 is answered, `intake.neutral_auto` stays off and unbuilt; a machinery `ABSORB` is refused.
- Until D-C7-OBJECTS is done for a field, no Phase G record kind or genesis gives that field a new producer (§1).
- Until SD-70's gate lifts and Q-G7 (b) settles `A`'s canonical element form, an adoption with a candidate and a result with a non-empty `adopts` stay `SCHEMA_UNSUPPORTED` (Phase F 4c-iv), and the adopted-`A` frame case is unexecuted.
- Until an owner defines `RECONCILE`'s follow-on kind, `RECONCILE` derives nothing (GR4).
- Until Q-G7 is answered, a change of an existing unit's kind or owning domain stays `SCHEMA_UNSUPPORTED` (reading F16; Q-F6 (ii)), and so does promotion with a domain change. Until Stage S settles it, a quarantined key that a candidate authors to a foreign change's value stays refused `STRUCT_REVALIDATE` (Phase F 4c-ii).
- Until step 10 is authorized, `ssdp-shadow-3` receives nothing from Phase G, and reading F1's allowlist is unchanged.
- Until step 11 is authorized, no external repository is cloned, read or contacted.
- Until an authorized campaign, no live agent submits and no runner executes on a real ledger.
- Until Phase H, failure points beyond group 4's stay untested; hostile-filesystem cases beyond GR5's stay Phase H's (SD-59).

Each fails toward "not supported", never toward support.

## 7. Questions for the stakeholder

**Q-G1. Sequencing the cutover cases with SD-70's gate.** A cutover is carried by an integration: its record is admissible only once the carrier's `TASK_RESULT` is admitted, and conditions 1-6 are checked at the carrier's integrating admission (catalogue §19.5). SD-70 keeps both `SCHEMA_UNSUPPORTED` until A10's D4, which follows Phase F after the SSDS PEM lineage reconciliation (SD-64 decisions 8-9, SD-66); SD-71 and SD-73 send the rebase, no-collateral regression, fences and the publisher to the same phase. Six of group 7's seven named discriminators need it in part.
- **Recommended: (a)** run A10's D4 and the gate lift as their own planned work, beside Phase G steps 1-6 and 8-9, which do not depend on them; Phase G's step 7b and its exit wait for it. Group 7 then runs end to end at Admission on fixture ledgers. The cost is real: A10's D4 is not a G2 phase, so it needs its own plan, probably a G2 workplan revision with its Review, and first the SSDS PEM lineage reconciliation (SD-63, SD-64 decision 9). The gate lift also brings SD-71's 5e/5f and SD-73's 6f/6g.
- **(b)** Phase G builds step 7a only; step 7b's cases are reported unexecuted at Phase G's exit and carried to the phase that lifts the gate, as Phase F carried SD-73's. Cheaper now; Phase G's exit then leaves most of group 7 at derivation and record level.
- **Either way, confirm GR1:** cutovers are enacted on fixture and scratch ledgers only, and no subject of a real ledger changes mode, so G2 workplan §2 item 1 is read as binding the real subjects.

**Q-G2. `intake.neutral_auto` (Q-F18's continuation, SD-78).** The catalogue decides the rule (default `false`; with it `true`, the Dispatcher may submit an R0 `ABSORB` of a governance-neutral delta, still checked by §8.3 step 4 and challengeable), but neither the scope rule of a machinery adoption nor the authorization of a machinery disposition is defined (Phase F Q-F18).
- **Recommended: (a)** keep it off and unbuilt through G2, disclosed at G3. The Manual makes it optional ("where policy enables it"), no G3 criterion needs it, the real shadow ledger would keep it off, and building it adds mechanism (G2 workplan §2 item 3).
- **(b)** Stage S first defines the scope rule and the machinery authorization (a model case, a register row, a G2 workplan revision and its Review), then Phase G builds it behind the policy flag, off on every real ledger.

**Q-G3. The external repository and its owner's permission.** The G2 row requires one external scientific repository with its owner's permission. The stakeholder chooses the repository and obtains the permission. The author recommends a public repository, and the owner's written permission recorded verbatim under `qualification/ssds80/` before any access, covering:
- (i) a bare clone on the stakeholder's machine that SSDS never writes, fetched once at a named commit (under Q-G4 (a) the operator then moves one local ref in it, within that commit's history);
- (ii) a shadow ledger in an SSDS home that holds copies of the repository's objects (GR5);
- (iii) what this repository's qualification records may contain and push to its remote. Recommended: commit identities, paths, counts and classifications, with no content excerpts unless permitted;
- (iv) retention and deletion of the clone and the ledger after the pilot;
- (v) whether, and how, the owner receives the findings.

**Q-G4. How the clone is observed.**
- **Recommended: (a)** replay. Genesis at a past commit; then the operator, not SSDS, advances one local branch of the operator's own bare clone through the repository's later history, and Admission absorbs each step. This exercises intake on real history without network access. The upstream repository is never written, but the operator does move one ref in the local clone.
- **(b)** Live. Genesis at the clone's head; observation of commits fetched from the owner's remote during the pilot. It needs network access and depends on the repository's activity.
- **(c)** Static. Genesis, derivation and classification at one commit, with no absorption. Weakest for intake.

**Q-G5. The pilot ledger.** A new shadow genesis is a human gate with the stakeholder's signature (G2 workplan §5.1 item 5; SD-57, as for `ssdp-shadow-3` under SD-96). The author recommends:
- a dedicated SSDS home for the pilot (`SSDS_HOME`), outside every repository and apart from the real home's `ssdp-shadow-3`;
- a new human key the stakeholder generates (GR7), and, if step 2 finds that an issue-key binding admits a Dispatcher's `INTAKE_CLASSIFICATION`, a Dispatcher issue key declared at genesis so that the census can submit classification proposals as machinery (Q-G6); if that question goes to Stage S, the key is not needed for the pilot;
- Case C at genesis: coarse `UNGOVERNED`, `OPAQUE` subjects by top-level region plus the reserved leaves. Case D's mixed modes only if the owner names a legacy process for a region; `NATIVE` never.
- Alternative: the real SSDS home, under its threat boundary (SD-59), beside `ssdp-shadow-3`.

**Q-G6. Case B on `ssdp-shadow-3`.** `ssdp-shadow-3`'s genesis already realizes Case B's entry: `ssdp.protocol` and `ssds8.manual` are `LEGACY(7.2.1)` with section-level parts. What is left is on the real ledger. The author recommends authorizing, one request at a time:
- the two `LEGACY_ACCEPTANCE` imports (GR6), each signed by the stakeholder's `ssdp-shadow-3` human key, whose outcome (applicable or provisional) is reported as found. For `ssds8.manual`, the import names `438cb113`, the text SD-66's acceptance commit applied word for word (GR6); the stakeholder confirms that this application counts as the accepted revision;
- classifier proposals over the content `ssds.unclassified` owns (GR2), each enacting nothing. They are R0 machinery records (Manual §18.2), but `ssdp-shadow-3` declares no issue or runner keys (SD-64, Q-F2), so no machinery actor can submit them there. The choice: (i) register a machinery key for the census, a key lifecycle act on the real ledger; or (ii) skip classification on `ssdp-shadow-3` and run it only on the pilot and scratch ledgers. A human-signed proposal would change its actor class and is not proposed. Recommended: (ii);
- reading F1's allowlist widened for exactly those kinds;
- no `MODE_TRANSITION`, and no disposition beyond classification (GR1).
- Alternative: Case B on a scratch clone of this repository with a scratch genesis only, leaving `ssdp-shadow-3` as Phase F left it.

**Q-G7. Q-F6 (ii) and the canonical form of `A` (SD-69, to Stage S).** The old domain owner's release (needed for a kind or domain change, and for a promotion that changes domain) and the canonical element form of an adoption set `A` are still unsettled in Stage S.
- **Recommended: (a)** keep both failing closed through Phase G and disclose them. No group 7 case needs a domain change, and the external pilot does not need one under Case C.
- **(b)** Settle them in Stage S now (a model case, a register row, a G2 workplan revision and its Review), so step 6 builds them.

## 8. Reopen and stop

G2 workplan §5.6 applies:
- a Manual decision failing in practice reopens G1;
- a register row failing at its real owner, or a needed behaviour with no row, returns to Stage S;
- a failure family recurring after a repair triggers simplification before another additive repair;
- any breach of the shadow boundary stops Stage D and goes to the stakeholder.

Specific to Phase G, these come to the stakeholder before they happen:
- **any access to a real ledger** (`ssdp-shadow-3` or the pilot ledger), and any request it would admit;
- **any access to an external repository**: cloning, reading, fetching or contacting its owner's remote;
- a new shadow genesis (a human gate);
- widening reading F1's observe-only allowlist;
- a credential for any governed ref; a write to the product repository or its `.git`; a new operator tree in the real home; a new runtime dependency; a new fitness exception; any live model call.

Two further triggers. If GR2 or GR6 proves false at its owner, the step stops, and the reading is revised before building on it. If the external pilot finds a failure family in content handling (hostile content, cost), it stops for simplification before another additive repair; hostile-filesystem cases go to Phase H.

## 9. Plan and step review record

**Revision 1 (2026-11-02): draft.** Drafted from the G2 workplan revision 4 (§5.1-§5.3), the accepted Manual §7, §18-§20, §26.1, the catalogue §7.4, §18.4 and §19.5 clauses the register accepts, the finding index's `STAGE-D` rows and their Review records (051cce3, 362af9f, 61cd09b, 63ddf91, f03b15e, f22b4dc, 441cf5c), the Stage S case files, the Phase F plan and exit evidence, and the stakeholder record through SD-104. Nothing is built. Questions Q-G1 to Q-G7 are open.

**Same-family plan check of revision 1 (2026-11-02, fresh-context subagent, read-only).** No SERIOUS CHALLENGE. **NO-PASS**, six blockers, each confirmed by the author against its owner:
- **B1, D-C7-OBJECTS not carried.** Phase F's exit evidence §5 requires the C7 audit of object-typed fields before any of them gains a new producer; Phase G adds producers. Repaired: §1 states it as a precondition of steps 2, 6, 7a, 8 and 11; the steps, §4's carried list, §6 and the status block name it.
- **B2, follow-on obligations no owner states.** Step 4 and GR4 had `SPLIT`, `MARK_GENERATED`, `DISPOSABLE` and `REJECT` deriving obligations; Manual §18.3 makes `DISPOSABLE` classification only. Repaired: only the upheld contrary disposition (catalogue §18.4) and `RECONCILE` derive anything, `RECONCILE` only as an owner defines its kind, else to Stage S (GR4, step 4, §6).
- **B3, the classifier's placement broke the fitness table.** The Dispatcher has no edge to `analyzers` (`fitness.py` `ALLOWED`, rule F1). Repaired: the classifier stays in `analyzers` and is reached through a `derivation` query no stratum consumes, with a stub test (GR3, §2).
- **B4, fixture cutovers against "no cutover".** GR1 read §2 item 1 and the row's parenthesis as real-ledger-only without saying so. Repaired: GR1 states the reading with its justification from the row and group 7's discriminators, and Q-G1 asks the stakeholder to confirm it.
- **B5, adoption with a candidate.** Step 1 listed it among sites lifted and §4 added an adopted-`A` frame case, against SD-70 and Q-G7 (a). Repaired: step 1 lists it as staying closed; the case waits for the gate lift and Q-G7 (b) (§4, §6).
- **B6, 362af9f N6 without its discriminator.** "Equal from scratch" does not catch a journal reader. Repaired: §4 transcribes the Review's (B) as written.

Notes taken up: N1 (eight S5 §7 cases cited by name, `same_enactment_counts_once`'s halves under other names); N2 (61cd09b N6 (c)'s positive and kind cases from catalogue §19.5); N3 (S5 §6 labelled register §20 evidence; §1's §20 description corrected); N4 (Q-G1 (a)'s costs); N5 (Q-G6's classifier actor, with a machinery key in Q-G5); N6 (the Manual revision an import names, into Q-G6); N7 (GR2 keyed on kind `UNCLASSIFIED`); N8 (the unexecuted rule cited to G2 workplan §5.5); N9 (the clone's commit and Q-G4 (a)'s ref aligned); N10 (step 7a's test-built entries stated as a new pattern with its DS-001 limit); N11 (no retry asserted in 61cd09b N6 (b)).

The reviewer's checks that held: the blob identities at `e78ece24`; the S5 §19 case's inputs and outputs; the 051cce3, 63ddf91, f03b15e, f22b4dc and 441cf5c N8 expectations; Manual §19.1's quote; Q-G1's dependency on SD-70; GR5's description of `content/git.py`; the shadow boundary, stop-and-ask, SD-59 and SD-89.

**Revision 2 (2026-11-02).** The repairs above.

**Narrow same-family re-check of revision 2 (2026-11-02, the same reviewer, read-only).** No SERIOUS CHALLENGE. B1 and B4-B6 closed; GR3's route consistent with `fitness.py` `ALLOWED` and Manual §26.1; GR4's `RECONCILE` handling fails closed within D4 authority; Q-G6 (i)/(ii) accurate. **NO-PASS** on two blockers, both confirmed by the author:
- **RB1, revision 1's GR2-GR4 left beside the new ones** (an editing error), so B2 and B3 were not closed in the text. Repaired: the stale bullets deleted.
- **RB2, GR6 and Q-G6 misstated the Manual's record.** Blob `438cb113` is the text SD-66's acceptance commit `39ad6f13` applied word for word, unchanged since; `fe43f04f` is the pre-A10 text. Repaired: the import names `438cb113`; only whether that application counts as the accepted revision is left to the stakeholder (GR6, Q-G6).

Notes taken up: N1 (`RECONCILE`'s unrealized follow-on disclosed at the exit, step 12); N2 (step 2 settles which key binding admits a Dispatcher's R0 `INTAKE_CLASSIFICATION`, else Stage S); N3 (§4's §20 wording aligned); N4 (the classifier's Git-history input through `content`'s readers, step 3); N5 (step 2's D-C7-OBJECTS scope covers step 4's outcome fields).

**Revision 3 (2026-11-02).** RB1, RB2 and N1-N5.

**Narrow same-family re-check of revision 3 (2026-11-02, the same reviewer, read-only).** No SERIOUS CHALLENGE. **PASS**: RB1 closed (§5 holds GR1-GR8 once each, consistent with §2, steps 3-4, §6 and step 12); RB2 closed (matches SD-66 and the history of `39ad6f13`); N1-N5 closed; frontmatter, status block and §9 agree. Two wording notes taken up after the PASS: step 2's Stage S route is conditional ("if no owner text covers it"), and Q-G5's issue key depends on step 2's binding outcome. No other-family Review has been run; per the review allocation that is one Codex round per frozen candidate, not a plan draft.
