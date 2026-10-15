---
kind: review-aid
subject: SSDS 8 Architecture Manual (proposed)
manual: orchestrator/docs/ssds-8.0-architecture.md
governing_protocol_version: 7.2.1
governing_workplan: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
phase_b_semantic_candidate: e23f14208be869e6a78cfd7b312e447254ee1851
status: coordination-evidence
---

Governing SSDP version: 7.2.1.

# SSDS 8 Architecture Manual — closure map

This file is a **review aid**. It maps every workplan §21 obligation, every §16.2 row and every §18 capability to the Manual section that owns its answer, with the disposition reached. It is not a runtime registry and not a second owner: where this map and the Manual differ, the Manual governs and the difference is a defect in this map. A route alone is not closure; each row states what the Manual decides. The exact Manual candidate this map was checked against is named by the Review handoff that freezes it.

Disposition codes: **DECIDED** — the Manual fixes the architecture choice; **CARRIED** — the reviewed workplan contract restated without semantic change; **REFINED** — a listed Manual refinement (§0.3 R1-R11); **DELEGATED** — a D4 choice inside a stated contract; **DEFAULT** — a proposed default parameter the stakeholder may change at G1 or by its lifecycle record; **OPEN** — not closable by design work; named with its owner.

## 1. Workplan §21 items

| # | Clause (workplan §21 at the candidate) | Manual | Disposition |
|---|---|---|---|
| 1 | manifest and anchor declaration syntax, governance-affecting declarations only in the manifest | §1.2 (TOML manifest, keys, anchors only delimit spans) | DECIDED |
| 1 | content normalization and boundary-marker rules | §1.5 (one representation: Git entry type, mode and blob bytes, read by identity, the write set and diff mapping, and materialized byte-exact by every designated runner with no fallback; LFS objects as external reads; submodule reads as gitlink read entries; anchor-line removal only for lines the system version's comment classifier marks, which resolution also uses; 3540d98 B1, e2154ac B1, e9e6e9f B1) | DECIDED |
| 1 | scope identity | §1.5 (hash of the subject's own declared terms) | REFINED (R6) |
| 1 | coverage partition and laminarity | §1.4 (partition by construction; membership forest; equal or partially overlapping regions of units not nested by membership resolve to `ABSENT`, 3540d98 B4), §1.9 (resolver purity; newly declared file and span terms must resolve at their admission, 53669a5 N5, 1ffbbf0 N1, 86ab683 N4) | REFINED (R5) |
| 1 | single-definer rule | §1.7 | CARRIED |
| 1 | effective-structure fold; declaration keys | §1.6, §1.2 | DECIDED (keys) / CARRIED (fold) |
| 1 | resolution against observed bytes (`ABSENT`, uncovered region) | §1.3, §1.4 | DECIDED |
| 1 | governance-affecting vs neutral classification algorithm; `aff(Q)` | §1.6 | DECIDED |
| 1 | governance signature and tenure | §1.6 | CARRIED |
| 1 (via §19.1) | tension search keys to unit identity | §1.11, `ask(locate)` §16.2 | DECIDED |
| 2 | every type's direction, role, cycle class, permitted classes, layer constraint, completeness eligibility | §2.2 table | DECIDED |
| 2 | vocabulary adoption checks | §2.3 | CARRIED + DECIDED (`CHALLENGES`/`EVIDENCES` never prerequisites) |
| 2 | SDG declaration syntax and rules | §1.7 (inline and manifest syntax), §2.4 | DECIDED / CARRIED |
| 2 | cycle legality and `well_formed` | §2.4, §2.5 | CARRIED |
| 2 | boundary-completeness semantics; analyzer completeness declarations | §2.6 | CARRIED / DECIDED (marker list, declaration contract) |
| 3 | closed record schemas | §3.2 envelope, §3.4 kinds, §21.2 entry | DECIDED |
| 3 | judgment kinds and tiers, including `IMMATERIALITY` | §3.3, §3.4 (gate `ACCEPT` requires `ADEQUATE`; `QUALIFIED` caps at provisional through the minimum over every eligible unsuperseded decision, §5.5, 3540d98 B3, e9e6e9f B2, a18b544 B2 and SD-24) | DECIDED |
| 3 | decision class and independence of each disposition kind | §3.4, §6.8, §8.3 step 3 | CARRIED |
| 3 | adverse outcomes of judgment kinds and their effect | §5.5 (veto by a standing adverse judgment; `same` independent of item revision, c6da678 B2; standing as in §6.7, intake and product-scope siblings, completeness member revisions, c6da678 N1, N2, N4; a gate's acceptance of a surface is its own `PRODUCT_SCOPE_ACCEPTANCE`, cc005db B3), §8.3 steps 3, 6, 7 | REFINED (R9; b595f2c B4) |
| 3 | which execution attributes each kind of evidence specification fixes | §17.1 (declared `fixed`; default free; ensemble fixes count, statistic, seed policy), §6.5 and §17.2 (one definition of configuration; a realization's free attribute values are its recorded execution attributes, never configuration, 53669a5 B1) | DECIDED |
| 3 | actor qualifications, including product-scope acceptance | §3.5 | DECIDED |
| 3 | outcome vocabularies | §3.4 | DECIDED |
| 3 | challenge inquiry-status attribute | §3.4 `CHALLENGE.inquiry`, §2.2 `CHALLENGES.inquiry` | DECIDED (R7 for the content relation) |
| 3 | compatibility contract | §3.6 | DECIDED |
| 4 | basis composition and mode assignment per kind | §4.1, §4.3 | DECIDED |
| 4 | executed content (execution basis, observed runner reads, whole-tree fallback) and each assessment's reading | §6.3 (recorded once at the reviewed granularity: unit, read, widened and pin entries with a frozen resolution context; read entries over the realization's tree, files absent from it are external reads; residual-part identity; pure resolvers, and no current assertion where a named system version or analyzer set is unavailable, c6da678 N6-N8, SD-15; an execution whose runner class does not observe every read outside the tree recorded as unpinnable, 1ffbbf0 B1 and SD-18; reads through symbolic links record every traversed link and the target, 798b2b4 B4; only a completeness judgment bounds the closure, and the whole-tree fallback covers every tracked path, a18b544 B1), §4.1 `execution` mode, §17.2, §17.5 | CARRIED + DECIDED (recording form; 6ff4ed1 B1, b595f2c B1, SD-11) |
| 4 | subject-boundary rule | §4.1 | CARRIED |
| 4 | consumption classes; equivalence-path composition | §4.4 | DECIDED |
| 4 | widening chain and closure algorithm | §4.5, §4.6 | CARRIED |
| 5 | recorded anchors and assessed content as content identities; `on`; `home`, `about` in S0 | §6.3-§6.5, §6.8 (`adm`) | CARRIED; `on` split REFINED (R1: `on⁺ = on⁻ ∧ …` by construction; one recorded basis read by currency, matching, floor and class; re-resolution under the frozen context; construction rule: `on⁻` compares only tree-resident terms, external pins and unpinnable reads enter only `on⁺`, c6da678 B1 and SD-12; guard: `on⁻` depends only on the record, re-resolved under its own resolution context recorded by value, and the compared bytes, cc005db B2 and SD-13; environment entries only in `on⁺`, pure scope-term resolvers and the resolution context recorded by value, d837363 B1-B2 and SD-15; the permissive conjunct stated over the class of every recorded execution attribute the specification leaves free, and SD-15's restriction of mechanical staleness to fixed-environment specifications withdrawn, 53669a5 B1 and SD-17; a free seed a recorded attribute, and unobserved external reads failing closed, 1ffbbf0 B1 and SD-18; `ext` over the complete external-input record, 3540d98 B2 and SD-23) |
| 5 | configuration matching; evaluated-outcome declarations including canonical numerical forms | §6.5, §17.1, §17.3 | DECIDED |
| 5 | failing-output naming and comparison | §6.5, §17.3 | DECIDED |
| 5 | output identity across specification revisions | §6.5 (`output_renames`) | DECIDED |
| 5 | mechanical-oracle verdict functions per reading | §6.5 (declarative recomputed; embedded not computable -> yielded) | DECIDED |
| 5 | `stale` and the "in force at the base" test | §6.4, §6.6 | CARRIED with R1 polarity labels |
| 5 | discriminating readings (one-record dual reading, contradiction refusal, class rule) | §6.6, §6.8, §8.3 step 3 | CARRIED |
| 5 | execution custody and external-runner run enumeration | §6.9 (reruns with the failing realization's recorded attributes, SD-17), §17.5 (runner classes declare the execution attributes they record; undeclared variation a disclosed residual, SD-17) | DECIDED (runner classes) / CARRIED |
| 5 | system cap on the time bound for `INCOMPLETE` | §6.9 (168 hours) | DECIDED |
| 5 | replicate rules for nondeterministic specifications | §6.10, §17.1, §17.3 (ensemble granularity, seed policy) | DECIDED |
| 5 | admitted and frame anchor sets, lineage, admitted-obligation latch in `starts` | §6.4 | CARRIED |
| 5 | `ev`, `undisputed`, `disp`, `eff` in S2 | §5.5, §6.7 (`ACC` and gate decisions of `NATIVE` D1/D2 subjects current only within the revision run, a `tgt` condition, 71cf9b3 B2, 798b2b4 B2, SD-21 and SD-22; S11 restated as R10) | CARRIED + REFINED (R10) |
| 5 | strata S0-S3 with `Σ`, `Q`, `aff`, `τ`, `well_formed`, `ok`, `E`, `pub` in S0 and `cont` in S1 | §5.2-§5.5, §5.8 | CARRIED |
| 5 | polarity classification of every record kind | §5.4, §3.4 | DECIDED (complete table) |
| 5 | fixed predicate templates and adoption-time stratification check | §5.1 | DECIDED |
| 5 | least-fixed-point evaluation | §5.6 | CARRIED + REFINED (R2 cycle clamp) |
| 5 | transformation identity and frames with the fixed three-way merge | §7.1, §7.2 (a both-sides change of one declaration key is a conflict, 53669a5 N7) | DECIDED (merge semantics) |
| 5 | prospective structure, well-formedness/enactment split, basis-entry roles, prospective tenure, prospective-acceptance rule, declared frame per kind | §7.3-§7.6 with §5.2 (gate decisions answering a frame's gate obligation declare its frame, 27ef339 B3; one rule for which records act in a state: an admitted-frame record everywhere, a frame record in the frames of its own lineage, earlier iterations and rebases included, and in the admitted state only once that lineage integrates; support, supersession, veto relief, disposition, gate eligibility and run membership read only acting records, while adverse records count in every state, SD-25, b46c250 B1) | CARRIED + DECIDED |
| 5 | fence settlement across fence chains | §22.3 | DECIDED |
| 5 | analyzer contract (deterministic vs recorded) | §5.9 (analyzer set pinned by the ruleset, 6ff4ed1 B3; frozen analyzer sets for matching; host-dependent output recorded, b595f2c N2), §14.5, §2.6 and §5.2 `tgt` (analyzer completeness as machinery `COMPLETENESS` records current only while their analyzer is pinned, b595f2c N1), §3.4 and §27.1 (adoption names the analyzer set, b595f2c N3) | CARRIED / DECIDED |
| 5 | derivation checkpoints and recovery-time bounds | §5.9 (1,000-entry interval) | DECIDED + DEFAULT |
| 5 (Phase B N2) | fail-closed handling of support cycles and corrupt prefixes before any current assertion | §5.6, §5.7 | REFINED (R2, R3) |
| 6 | validation order including the structural-delta rule (author, realign, carry, adopt) | §8.3 (supersession authority by kind, own author or owner only: REFINED R8; one `TASK_RESULT` per task with result-only templates at admission: REFINED R9) | CARRIED |
| 6 | source/destination challenge freeze | §8.3 step 4(b) | CARRIED |
| 6 | dependency well-formedness with re-routed support edges | §8.3 step 5 | CARRIED |
| 6 | request identity and idempotency | §8.1 | DECIDED |
| 6 | merge-queue serial order | §8.2 (FIFO; never-lost-only requests not delayed) | DECIDED |
| 6 | single-ref append, quorum admission, single provisional entry | §21.3, §22.4 | CARRIED / DECIDED (append mechanics) |
| 6 | `obs`, entry-shape rule, equivalent publication and reachability classification, reconciliation procedure | §22.1-§22.3 | CARRIED |
| 6 | exclusive per-entry publication with its write-ahead intent | §22.3 (publisher incarnation; no durable log; VM snapshot residual in §32.2) | REFINED (R4) |
| 6 | fencing absorptions and fence commits; late-publication detection | §22.3 (fence commit format) | DECIDED / CARRIED |
| 6 | operational takeover wait | §22.3 (300 s) | DEFAULT |
| 6 | ABA policy | §22.3 | CARRIED |
| 7 | obligation rules, including retirement, split and retargeting of evidence obligations carrying failing assessments | §10.2 (revising review derived in any frame where `ACCEPT` or `GATE` lacks a counting revision-assessment record for exactly its revision; predecessor defined as a machinery-supplied set, 1ffbbf0 B2, N3 and SD-19; a record counts only with the current predecessor and while it stands, 86ab683 B1, N6 and SD-20; 71cf9b3 B1-B2 and SD-21; replaced by the revision run, an S0 target condition every consumer reads, with obligations parameterized by the run and the predecessor a machinery-computed display, 798b2b4 B1-B3, N1-N4 and SD-22; the run is identified by the event that starts it, an integration's enactment lineage, the obligation that requested a cutover or an absorption entry, so a frame names the run its integration starts before any position exists, and a record is in the run when it acts and names it, SD-25, b46c250 B1-C, B1-D) | DECIDED |
| 7 | readiness | §10.3 | CARRIED |
| 7 | three-valued discharge, provisional propagation, risk-override scope (four discharge values; a `QUALIFIED` gate `ACCEPT` caps at `P` through the minimum over eligible decisions, R11, SD-24; eligibility and supersession read in the state at hand through the acting rule, 575dc78 B1, f7419d5 B1, SD-25) | §10.4 (plus `REFUSED` for an adverse answer under the §5.5 `same` test, named in R9, c6da678 N5), §10.5 | CARRIED + REFINED (R9; b595f2c B4) / DECIDED (override scope grammar) |
| 7 | iteration/attempt identity | §10.3 (every task ends in one `TASK_RESULT`; judgment obligations answered once and never re-dispatched) | DECIDED (b595f2c B4) |
| 8 | change-plan structure | §11.1 (plan subject, `ssds-item` blocks), §13.2 (`ref` locality and part-scoped resolution, b595f2c B2, c6da678 N11) | DECIDED |
| 8 | plan acceptance; scoped amendment policy; plan invariants | §11.2-§11.4 | CARRIED / DECIDED (per-plan scoped-review flag) |
| 9 | serialization policy surfaces | §9.2 | DECIDED |
| 9 | generated-unit handling | §9.3 | CARRIED / DECIDED |
| 9 | joint invariants | §9.2 (declaration and derived obligation) | DECIDED |
| 9 | residual-risk disclosure | §9.4 | DECIDED (where it is stated) |
| 10 | interface operations | §16.1 | CARRIED |
| 10 | query classes | §16.2 | DECIDED |
| 10 | brief and gate templates (Channel C; §19.2 activation, injection, delegation schema) | §16.3, §16.5-§16.7, §13.5 (revising review for D1/D2 revisions outside `AUTHOR` items and gate statement of absent assessments, d837363 B3 and SD-16; passing acceptances and gate `ACCEPT`s of a D1/D2 revision, in every frame, refused unless a revision-assessment record for exactly that revision counts (in the revision run, standing; SD-22), and current only within the revision run in which they were made (SD-22), however it was produced; only a record carrying the slot answers the revising review, §10.2, §8.3 step 7, 53669a5 B2, 1ffbbf0 B2 and SD-19) | DECIDED |
| 10 | epistemic labels | §16.2 | CARRIED |
| 10 | read recording | §16.4 | DECIDED |
| 10 | transports and bootstrap locator | §16.10 | DECIDED |
| 11 | evidence realization basis fields (regimes, replicates, environments, precision) | §17.2 (configuration and recorded execution attributes distinct; attribute entries of the one recorded basis, 53669a5 B1) | DECIDED |
| 11 | assessment granularity for stochastic specifications | §17.1, §17.3, §6.10 (a free seed is a recorded attribute: same-seed runs serve (1) and (3), every seed enters (2) and (4); runner-external randomness disclosed as unrecorded variation and the §31.3 ensemble sentence corrected, 86ab683 N2; 1ffbbf0 B1 and SD-18) | DECIDED |
| 11 | realized-record/observation boundary | §17.4 | CARRIED |
| 11 | trusted-runner designation and custody | §17.5 (declared recorded attributes and read observation; requestable attributes; declared-set changes shown, 1ffbbf0 N5) | DECIDED |
| 12 | intake detection | §18.1 | CARRIED |
| 12 | static classification | §18.2 | DECIDED |
| 12 | dispositions; trust/quarantine | §18.3 | CARRIED |
| 12 | structural quarantine views; adoption and realignment requests | §18.4, §18.5 (contrary dispositions in both orders; `QUARANTINE` effect through `ok`; disposition targets, cc005db N5, d837363 N3; targets never timing, so a contrary disposition and the owner's adjudication after an `ABSORB` are admitted, 53669a5 B3; `QUARANTINE` paths within its object, 53669a5 N6, 1ffbbf0 N4, 86ab683 N5) | CARRIED + DECIDED |
| 12 | policy for mechanical adoption of governance-neutral deltas | §18.4 (`intake.neutral_auto`, default false) | DECIDED + DEFAULT |
| 13 | governance modes | §19.1 | CARRIED |
| 13 | legacy and external acceptance import scope | §19.2, §20.2 | CARRIED |
| 13 | external consultation supersession | §20.2 | CARRIED |
| 13 | reconstruction status; structural refinement | §19.3 | CARRIED |
| 13 | promotion, demotion, restoration, carve-out | §19.4, §19.6 | CARRIED / DECIDED (`LEGACY_RELEASE`) |
| 13 | cutover and quiescence | §19.5 (conditions, quiescence record; owner acceptance bound to the cutover admission with its revision-assessment record, 86ab683 N1; trigger stated in §10.2 and §19.5 for any requested cutover, 71cf9b3 N4, 798b2b4 N4) | DECIDED |
| 13 | genesis | §19.9 (contents, FF-001 procedure, shadow genesis) | DECIDED |
| 14 | Git entry format | §21.2 | DECIDED |
| 14 | per-host Admission identity and the publication-attempt record (intactness across processes, copied or restored state, key-preserving host replacement) | §22.3 | REFINED (R4: incarnation; no durable record) |
| 14 | fence-commit format | §22.3 | DECIDED |
| 14 | referenced-object retention; retention of trees holding evaluated content | §21.2 (extra parents), §21.4 | DECIDED |
| 14 | durability (fsync) configuration | §21.3 | DECIDED |
| 14 | ledger location options | §21.5 | DECIDED |
| 14 | authentication scheme and key lifecycle, including retired-key envelope verification | §23.2, §25.2, §8.3 step 3 | DECIDED |
| 14 | witness kinds; witness model and deployment classes | §23.3 | DECIDED + DEFAULT (class parameters) |
| 14 | checkpoint and retirement-statement formats; read repair | §23.3 | DECIDED |
| 14 | qualification procedure and states; fresh-clone procedure | §23.4, §23.5 | CARRIED / DECIDED (`RETIRED`, `INTEGRITY_HALT` states) |
| 14 | replica and witness-set redesignation; the non-admission bound | §23.6, §23.8 | CARRIED |
| 14 | `LEDGER_LOSS` contents and re-established global control facts; recovery procedure | §23.6, §23.8 | CARRIED |
| 14 | continuity-attestation grammar, actor designation and evidence | §23.7 | DECIDED |
| 14 | confidentiality breach procedure; closed-schema secret checks; retention weighed before purge | §24.1, §24.2 | DECIDED (checks, entropy default) / CARRIED |
| 14 | operator-state boundary; derived index | §21.1, §21.6 | CARRIED / DELEGATED (engines) |
| 15 | actor identity and human authentication trust roots | §25.1, §25.2 | DECIDED |
| 16 | protected surfaces; self-governance of rules, schemas, trust roots and witnesses | §25.3 | DECIDED |
| 17 | component boundaries and dependency direction | §26.1, §26.2 | CARRIED / DECIDED (fitness rules) |
| 17 | Dispatcher/Admission separation | §26.1 | CARRIED |
| 17 | executed supersession of Architecture 1.6.0 resolving every Deferred row | §26.4; table in §2 below | DECIDED |
| 18 | ruleset/schema evolution; successor migration | §27 (recorded bases keep their system version; normalization changes disclose their re-acceptance burden, cc005db N7) | CARRIED / DECIDED |
| 19 | system, schema, ruleset (with analyzer set), interface, profile versions distinct | §28 | DECIDED |
| 20 | external units, external acceptance import, cross-repository boundary | §20 | DECIDED (pin grammar) / CARRIED |
| 21 | every Manual decision delegated by §19.1 and §19.2 | §29.7 table | DECIDED |
| 22 | minimum-justified-architecture reassessment of every primitive, component and persistent surface | §30 (statements updated for R1 and R9, b595f2c N7; the SD-16 trigger and the SD-17 class rule, 53669a5 N8) | DECIDED (two removals: R4, R5) |
| 23 | system role templates, obligation kinds, record kinds, outcomes, write-scope rules | §12.3 (reviewer and principal `TASK_RESULT`, b595f2c B4), §10.2 (including `AUTHOR`, `DOCUMENT`; 6ff4ed1 B4), §13.2 domain rule (no D1-D3 unit outside `AUTHOR`, b595f2c B3 and N8), §1.2 effect-keyed write set (every unit whose owned content, declaration keys, semantic declarations, regions, membership or signature differs between the current head and the merged tree, by any route, c6da678 B3, cc005db B1, SD-14, d837363 B4); cross-domain structural changes have no agent route, and a new unit of an `AUTHOR` item's own domain over uncovered content is that item's change (d837363 N2, 53669a5 N4) | DECIDED |
| 23 | separation constraints and context-lineage provenance | §12.2, §12.3 | DECIDED |
| 23 | limits on policy extension; standing-plan designation | §12.3, §12.5 | DECIDED |
| 24 | contract schema; lint rules | §13.1, §13.2 | DECIDED |
| 24 | minimum verifier coverage per item kind | §13.3 (`TEST_INTEGRITY`/`BOUNDARY` for any scope with `D4` or `EVIDENCE_SPEC` units; audit conclusion, b595f2c N6) | DECIDED |
| 24 | closed control-tightening whitelist and its order for every field | §13.4 (item prose byte-identical; 6ff4ed1 B2) | CARRIED + DECIDED (`homes`, `authority`, unknown fields, prose) |
| 24 | task-partition checks; budgets | §13.7 | CARRIED + DEFAULT (3; cap 10) |
| 24 | system contracts for obligation kinds outside any item | §13.6 (slots carried on the reviewer's `TASK_RESULT`; budget spent only while unanswered) | DECIDED |
| 25 | check-template library: families, parameters, force | §14.3 | DECIDED |
| 25 | set-valued aggregation | §14.4 | CARRIED |
| 25 | language analyzers for Python and C++ | §14.5 | DECIDED / DELEGATED (parsers) |
| 25 | mutation-testing configuration and thresholds | §14.5 | DECIDED + DEFAULT (0.70) / DELEGATED (tool) |
| 25 | unit-annotation conventions | §14.5 | DECIDED |
| 25 | qualification thresholds admitting a template as `HARD` | §14.7 | DECIDED + DEFAULT |
| 26 | report kinds, reasons, materiality vocabulary | §15.1 | DECIDED |
| 26 | routing table; escalation floors; coordination outcome table | §15.3-§15.5 | CARRIED |
| 26 | materiality reclassification | §15.6 | CARRIED |
| 26 | review, decision and inspector templates; digest; impact ranking | §16.5, §16.7, §16.8 | DECIDED (ranking key) |
| 27 | doctrine-realization map with E0-E3 per duty of every 7.2.1 role and specialist entrypoint | §29.2-§29.5 (claims re-bound after b595f2c B3, B4 and N6; §29.4 revising row and §29.5 documentation row re-bound after 53669a5 B2 and N8, and §29.4 again after 1ffbbf0 B2, 86ab683 B1, N6, 71cf9b3 B2 and 798b2b4 B1-B3) | DECIDED |
| 27 | disclosed list of duties that stay E3 | §29.6 | DECIDED |

## 2. Architecture 1.6.0 (workplan §16.2)

Both tables are closed in Manual §26.4; this lists each row's final disposition. "Deferred" rows are marked **(was Deferred)**.

| 1.6.0 row | Final disposition (Manual §26.4) |
|---|---|
| inv. 1 progressive usefulness | Replaced for native scopes; preserved for version-bound work via Core |
| inv. 2 four-level ladder | Retired; replaced by §26.1-§26.2 |
| inv. 3 graceful degradation | Replaced (truthful non-closure); no-silent-bypass preserved |
| inv. 4 one CLI and composition root **(was Deferred)** | Preserved and closed: SSDS is Core extension `sdp.ssds` under the single `sdp` root (§26.3) |
| inv. 5 versioned boundaries | Preserved (`ssds.api.v1`, `ssds.spi.v1`) |
| inv. 6 no duplicated workflow authority | Replaced (ledger + Admission) |
| inv. 7 manual operation first-class | Replaced in part |
| inv. 8 recommendation precedes scheduling | Retired as module boundary; substance preserved |
| inv. 9 benchmark context **(was Deferred)** | Preserved and closed: exact fields listed |
| inv. 10 scheduler subordinate | Preserved and strengthened |
| inv. 11 private state | Replaced in part |
| inv. 12 subset acceptance | Preserved for Core; retired for SSDS components |
| inv. 13 stable IDs | Preserved |
| inv. 14 read vs mutation | Preserved |
| inv. 15 long-running execution **(was Deferred)** | Preserved and closed: harness-adapter SPI lifecycle |
| inv. 16 route vocabulary | Preserved |
| inv. 17 capability identity **(was Deferred)** | Preserved and closed: SSDS capability keys listed |
| inv. 18 explicit route not a bypass | Preserved |
| inv. 19 route admission before rendering | Preserved |
| inv. 20 run identity first | Preserved |
| inv. 21 structured manual result seam | Replaced and strengthened |
| inv. 22 version binding | Preserved |
| inv. 23 one mutating run per worktree | Preserved |
| inv. 24 profile-owned routing | Replaced for native scopes |
| inv. 25 uncertain routing stays uncertain | Preserved |
| inv. 26 containment under `orchestrator/` **(was Deferred)** | Preserved and closed: no change of containment root |
| §3 ladder and distributions | Retired; Core preserved; SSDS one distribution |
| §4 layout, packaging, namespace | Preserved and closed (§26.3, §26.4 row) |
| §5 public API standard **(was Deferred)** | Each sub-rule closed: §5.1-§5.7 adopted (with SSDS specifics), §5.8 superseded |
| §6 composition SPI **(was Deferred with inv. 4)** | Preserved; SSDS registers through it |
| §7 shared records **(was Deferred: CandidateRef/StageResultEnvelope mapping)** | Mapped per record; `CandidateRef` and `StageResultEnvelope` explicitly declined with replacements |
| §8 Core/Prompt | Preserved for version-bound work |
| §9-§11 Tracker, Adapters, Scheduler **(detail was Deferred)** | Retired as modules; every function mapped to Ledger/Derivation/Interface or Dispatcher |
| §12 configuration **(was Deferred: layout)** | Preserved and closed: Core config owner with `[ssds]` section; policy is governed content |
| §13 persistence | Replaced by §21 |
| §14 CLI capability behavior | Preserved for Core; replaced for SSDS by `sdp ssds` |
| §15 failure | Replaced by §23.8, §19.7 |
| §16 security/privacy | Preserved |
| §17 benchmark integrity | Preserved |
| §18 fitness **(was Deferred)** | Replaced and closed by §26.2 |
| §19-§20 acceptance ladder | Retired |
| §21 versioning | Preserved principle |
| §22 simplicity/reopen triggers | Preserved where applicable |

The Tracker, Adapter and Scheduler modules had no implemented data to migrate; their **functions** are mapped row by row in Manual §26.4, which is the closure (not the absence of data).

## 3. Inheritance and capability transfer (workplan §18)

**§18.1 consolidated Protocol 8 plan.** Every row the workplan dispositions as Carried, Replaced or Changed lands in the Manual as follows: §1-§2 control plane coordinates, never reproduces semantics, lossless inheritance -> Manual §0.4 (C7, S-invariants), §33; §3 deliberate supersession of 1.6.0 -> §26.4; §4 reducer vs scheduler -> §26.1; §5 planes and semantic/control projection -> §1.7, §2.1, §18; §6 minimal control data -> §3.2; §7 versioned closed schemas -> §3.6; §8 logical identity vs revision -> §1.5; §9 typed relations, scoped completeness -> §2; §10 evidence formalization -> §17; §11 state dimensions -> §5.8; §12 replay -> §5.9, §27; §13 validation layers, single writer -> §8; §14 external effects -> §22; §15 storage (Changed: Git ledger) -> §21; §15.2 durability and recovery -> §21-§23; §16 action registry -> §5.1; §17 schema-valid outputs, no prose parsing -> §13.5, §14.2; §18 envelopes and self-reference -> §12.2, §8.7; §19 agent PASS -> §8.7, §14.4; §20 gates, overrides, Serious Challenge -> §5.3, §16.6; §21 deterministic impact -> §4-§5; §22 workplans after cutover -> §19.8; §23-§24 bootstrap, transports -> §16.10; §25 isolation and stale results -> §9.1; §26 security -> §24-§25; §27 failure semantics -> §19.7, §23.8; §28 baselines, rollback, quiescence -> §19.5, §19.7; §29 phases -> gates (§31.1); §30-§34 -> workplan §21, §22, §25 and this Manual; §35 non-goals -> §33; §36 final target -> Manual §0.2 and §29; §37 version rebind and Protocol 7 inputs -> §29.7.

**§18.2 befe678 capabilities** -> relations with layer direction and SCC handling §2.2-§2.4; derived dependencies with blind spots §2.6, §14.5; evidence applicability §17.4; typed relation classes §2.2; reviewed immutable plans §11.2; modular plans §11.1; iteration vs attempt §10.3; deterministic explainable context §16.2-§16.3; minimum-burden interface §16.1; safe parallelism §9; isolated workspaces §9.1; incremental = full rebuild §5.9, §31.2; structural history §5.8; repository explainability §1.4, §18; progressive migration §19; structural split without false claims §19.3; discovery bottom-up §19.5; mandatory orchestrator after cutover §19.5; atomic publication and recovery §22-§23; private control state §21.1.

**Learned capabilities (PEM).** Basis revalidated for the Manual scope: `main` at `af0455753e20ee54a969c844872e29e270007211` (no later `main` commit), PEM blob `1561797125622f355f84eb27319f87e8fa4227d9`, schema 1 valid (5 families, 0 notices) after deepening the shallow checkout so the immutable evidence revisions resolve; no branch overlay; all five canonical family records searched regardless of temperature. Coverage is partial and has no 7.x entries; absence proves nothing.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: AUTHORITY_BOUND through the 7.2.1 versioning owner (older supported profiles stay frozen and independently testable); the Manual keeps Core standalone and every profile through ssdp-protocol-7.2 frozen (§26.3-§26.4, §28, §31.8).
  - id: DS-001
    disposition: APPLICABLE
    reason: Evidence-only; the Manual's qualification design binds claims to real owners, marks the diagnostic model as transcription, and claims no runtime evidence at G1 (§31.1, §31.3).
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy; every view is regenerated from the ledger and content, never edited (§5.8, §5.9).
  - id: SP-002
    disposition: APPLICABLE
    reason: Evidence-only; records and entries never contain their own commit identity; checkpoints live at witnesses outside the entry (§8.7, §21.2, §23.3).
  - id: FF-001
    disposition: APPLICABLE
    reason: Evidence-only; genesis, replacement lineages and cutover publish nothing before validation (§19.9, §24.2); no head is asserted current before quorum (§22.4).
```

| Capability | Current authority binding | Mechanism in the Manual | Acceptance route |
|---|---|---|---|
| frozen historical profiles independently testable (PC-001) | 7.2.1 versioning owner | Core untouched; SSDS an optional extension; fitness check that Core imports nothing from SSDS | §31.8 Core suite without SSDS installed; repository acceptance |
| synthetic checks bound to their property (DS-001) | evidence and testing owners | qualification design per real owner; model check as diagnostic only | §31 at G3 |
| canonical source, regenerated derivatives (SP-001) | evidence-only | derived views never canonical | §31.2 incremental = from-scratch |
| self-reference-safe publication (SP-002) | evidence-only | §21.2 entry format; checkpoints at witnesses | §31.4 |
| validation before immutable publication (FF-001) | evidence-only | genesis procedure; lineage replacement; quorum before currency | §31.4 confidentiality drill; §31.7 genesis |
| live disagreement distinguishable from resolved reassessment | evidence owner | §6 unchanged in mechanism; R1 polarity explicit, one recorded basis | §31.3 |
| contradictory judgments never resolved by vote, count or order | workflow and evidence owners | R9 veto; answered obligations; own-author or owner supersession only | §31.5 |
| publisher at-most-once with decisions after settlement | concurrency owner (C4) | R4 incarnation publisher, fences | §31.4 |

## 4. Phase B carry-forward

| Finding | Manual disposition |
|---|---|
| N1 historical adoption provenance | Not closable by the Manual. Recorded as an open provenance item in §32.2 and §32.4; only a stakeholder restatement or recovered authentic evidence closes it. The Phase C task (2026-10-15) itself binds 7.2.1 through the handoff the stakeholder directed to be followed. |
| N2 completeness polarity; cyclic prefixes | R1 (`on⁺`/`on⁻` named at every use, §6.5-§6.8; after the 6ff4ed1 Review's B1, `on⁺ ⇒ on⁻` holds by construction and neither predicate reads effective structure; after the b595f2c Review's B1, the execution basis is recorded once at the reviewed granularity with a frozen resolution context, SD-11); R2 (cycle clamp, §5.6); R3 (corrupt prefixes, §5.7); real-owner discriminators with both differing-old-content and yielding-present-content runs and an alternate tree differing only outside the recorded regions (including another span of a recorded file), the b595f2c trajectory with its sibling, ignored-file and prefix-addition variants, the c6da678 external-input trajectory with its unpinnable-read variants, the cc005db system-version trajectory, the d837363 environment and host-resolver trajectories, the 53669a5 free-attribute (backend, precision, instruction set) and red-then-green trajectories, the 1ffbbf0 unobserved-input and free-seed trajectories, plus negative discriminators against global fallback and against discarding observations or staling unrelated passing evidence (§31.3). The global-fallback hypothesis stays rejected. |
| N3 diagnostic and reader limits | §31.3 lists what the model does not cover and moves those cases to real owners; §29.6 and §32.2 disclose the lenient-reader residual. |
| N4 practical cost/applicability | §32.3 keeps every workplan §26 reopen condition and adds those the Manual's decisions create (fence frequency after R4; manifest and scope-term expressiveness; partition rules); §31.9 measures, never claims. |

Prior closures (Y1/Y2 and earlier) are carried unchanged in §6; the convergence boundary is respected: no new latch, exception or persistent mechanism enters the §6 family.

## 5. Items needing a stakeholder decision at G1

- Acceptance of the major architectural change as specified (workplan §25 criterion 12).
- The **[proposed default]** values: derivation checkpoint interval (§5.9), budgets (§13.7), mutation threshold (§14.5), `HARD` qualification thresholds (§14.7), takeover wait (§22.3), deployment-class parameters (§23.3), entropy threshold (§24.1), cutover reconstruction minimum (§19.5). The 168-hour time-bound cap (§6.9) is a D3 decision, not a default; the stakeholder may still ask to change it.
- The decision recorded in §0.3 R4 accepts a human decision after every crash inside the publication window, and discloses VM-level snapshot and resume of a running Admission process as outside the crash model (§32.2).
- The decision recorded in §0.3 R9: a standing adverse judgment (for example one reviewer's `NO_PASS` or one qualified `FAIL`) blocks the contrary passing judgment until its human author reassesses, the owner adjudicates or a challenge against it is upheld (an agent's judgment cannot be reassessed by its author, whose task has ended), which trades some adjudication work for never resolving a disagreement by re-dispatch or order.
- SD-17, which withdrew the SD-15 restriction: a failure becomes stale mechanically only through runs that match the failing realization on its pins and on every execution attribute its runner class records; variation in an attribute no runner class records is a disclosed residual, so a failure it causes can be made stale (§6.5, §17.5, §32.2). Projects choose what each runner class records.
- SD-18: runner classes that do not observe every read outside the tree support no mechanical stop; their failures, red-then-green iterations included, go to the owner (§17.5, §32.2-§32.3).
- SD-24: a gate holder's `QUALIFIED` acceptance lets work continue only provisionally (`P`), and discharge is provisional only where policy permits provisional continuation; an `INADEQUATE` acceptance is refused (§5.5, §16.6).
- Content identity is exact (no line-ending normalization), so a line-ending-only or mode change is a revision change that needs re-acceptance, and for D1/D2 subjects a revising review and gate (§1.5, §32.3). Runners must materialize Git blob bytes, ignoring `.gitattributes` transforms; a runner that cannot is not designated, and Git LFS data is read as a pinned external input (§1.5, §17.5).
- SD-16, SD-19 and SD-22 as realized: no `NATIVE` D1/D2 revision, however produced and in whatever frame, can be gate-accepted or accepted unless a revision-assessment record for exactly that revision counts (in its revision run, standing), and its acceptance and gate decision are current only within that run. A revert of D1/D2 authority, or any other change of its revision, therefore needs a new revising review, acceptance and gate. The predecessor is a machinery-computed display the reviser may extend, not an equality condition (SD-22 replaced SD-20's equality and SD-21's `holds`). A tension recorded later does not invalidate a record; the gate core shows it. No human override exists (§8.3 step 7, §10.2, §5.2); adding one is a stakeholder decision. Every re-identification and nested-only revision also needs its record.
- **Author choices under the stakeholder's delegation (record item 19), to confirm or reverse:**
  - exact content identity with no runner fallback, LFS objects as external reads and submodule reads as gitlink entries (e9e6e9f B1, subtractive);
  - only a completeness judgment bounds a closure, the whole-tree fallback covers every tracked path, and only judgment-bounded runs can stop a failure (a bounded reproduction is required; the identical-tree shortcut was withdrawn after 5c55d4b B1, so a fix inside a judgment's scope can cost a fresh reproduction); unbounded failures go to the owner and, for D1/D2 claims, the floor (a18b544 B1, 0b6c4fa B1, 27ef339 N1). **This partially reverses SD-17's restoration of red-then-green iterations** wherever no analyzer or reviewer completeness judgment bounds the closure, which in scientific code with incompleteness markers is most closures (27ef339 N2). The alternatives are an adverse-only exact read core for runner classes qualified for complete in-tree tracing (adds mechanism, restores red-then-green for them), or judgment-only staleness (removes mechanical stops entirely);
  - conditions (2) and (4) use `link⁻`, one adverse-only existential, so a run's recorded width never hides it (27ef339 B1); this is required by Phase C handoff N2 rather than a free choice;
  - the gate term is the minimum over every eligible unsuperseded passing decision, so a qualification lifts only when its own decision is superseded, whatever order holders or candidate frames decided in (575dc78 B1); any holder's eligible `QUALIFIED` decision caps the gate until it is itself superseded, and only its author or the owner lifts it; a later `UNQUALIFIED` decision by another holder does not lift it (a18b544 B2, 0b6c4fa B2, f7419d5 B1);
  - the gate tenure filter withdrawn, so a restored non-D1/D2 subject at an unchanged triple reuses its earlier gate decision, as the reviewed workplan does (0b6c4fa B2).
- SD-25 as realized: human gate and acceptance decisions stay before integration, and one rule says which records act in each state (§5.2), read by support, supersession, veto relief, disposition, eligibility and run membership; a revision run is identified by the event that starts it (§10.2). Its consequences to confirm: a record in one pending candidate's frame no longer supports a record in another candidate's frame until its lineage integrates (§7.3, §32.3); a frame `REJECT` on a subject the candidate leaves unchanged keeps vetoing in the admitted state after the candidate is abandoned, until its author reassesses or the owner adjudicates (§5.5); gate decisions accumulate as minimum members (§32.3).
- Product scope: the Manual marks **no** inspectability surface beyond the requested deliverable (§0.5); none needs product-scope acceptance.
- N1 restatement, if the stakeholder chooses to close it.

## 6. Unexecuted evidence (blocking only at the gates that require it)

All runtime claims in Manual §31.2-§31.9 are **UNEXECUTED**: no SSDS implementation exists and D4 is not authorized. They block G3 (and G4 per subject), not G1. The depth-5 diagnostic run remains prior-session-reported reuse with missing interpreter and raw-output provenance.
