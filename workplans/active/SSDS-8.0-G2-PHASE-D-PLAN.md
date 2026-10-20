---
kind: ssds-shadow-phase-plan
workplan_id: SSDS-8.0-G2-PHASE-D-PLAN
protocol_version: 7.2.1
target_system_version: 8.0.0
status: active
created_date: 2026-10-19
governing_workplan: workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md (revision 3, Stage D, §5.2 Phase D row)
governing_architecture: orchestrator/docs/ssds-8.0-architecture.md (accepted at G1, SD-50; amendments A1-A6 accepted, SD-53 and SD-55; A7 decided, SD-56, its text's independent Review pending)
g2_authorization: SD-55 (shadow implementation only)
stakeholder_amendment: SD-56 (one program `ssds`; operator data in the SSDS home; §6-§7 answered); SD-57 (a first release with no predecessor installation; the genesis approval key)
active_serious_challenge: SC-1 of the 0e49deb Phase D Review (catalogue §6.5 bounding currency), at the G2 register's owner (SC-D1 resolved by SD-56)
---

Governing SSDP version: 7.2.1.

# SSDS 8.0 — Stage D Phase D plan: the read-only kernel

```text
STATUS: ACTIVE. Companion to the G2 shadow workplan, Stage D (§5.2 Phase D row). It concretizes
        that row into files, modules and test groups; it adds no mechanism beyond the settled
        register (G2 workplan §4.2) and changes no Manual decision.
SHADOW: no SSDS authority over any subject; every subject LEGACY(p) or UNGOVERNED; no cutover. The
        document-controlled 7.2.1 baseline governs. The shadow genesis human gate is the stakeholder's.
DONE SO FAR: §3 step 1 (package skeleton, §26.2 fitness checks), the SD-56 rename (§2), step 2
             (content and analyzers), step 3 (the ledger), step 4 (derivation S0-S2, §5.10,
             §6, §7 frames), step 5 (S3 kernel, checkpoints, determinism) and step 6 (Admission
             genesis path); readings in §8.
             Step 7: the stakeholder took the genesis gate and admitted the shadow ledger
             `ssdp-shadow` in the SSDS home (`QUALIFIED`; derived with a current assertion, no
             findings, no obligations); evidence in
             `qualification/ssds80/PHASE-D-STEP7-SHADOW-GENESIS-EVIDENCE-SSDS-8.0.md`.
             The Phase D Review of 0e49deb is NO-PASS on both subjects
             (`qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-0E49DEB-DIFFERENT-FAMILY-NO-PASS.md`);
             its implementation blockers A-B1 to A-B4 are repaired (§9).
SERIOUS CHALLENGE: SC-1 of that Review (catalogue §6.5 bounding currency against S5 §6
             `genuine_fix_is_stale`, §8 reading 1) is open at the G2 register's owner; A7 blocker
             B-B1 (two Manual §26.4 rows) waits for the Manual's owner.
NEXT ACTION: the SC-1 decision and the B-B1 text, then a Review of the repaired candidate. §7 Q5
             is needed only when a setting is first read.
```

## 1. Scope and authority

The G2 workplan's Phase D row builds `content`, `analyzers`, `ledger` (schema, chain verification, store, qualification read path), `derivation` (strata S0-S3 and queries), the Manual §26.2 fitness checks, and Admission's genesis path only (Manual §19.9), realizing register rows §1-§7, §19.9, §21, §23 read path and §27-§28. Its exit evidence for G3 is acceptance groups 1, 2 and 3 (derivation halves), determinism and replay, incremental equals from-scratch, and a shadow genesis of this repository's history derived end to end.

This file decides only D4 placement and order. Every behaviour cites the register row it realizes; a behaviour no row covers returns to Stage S (G2 workplan §5.6). Rules of G2 workplan §5.1 apply unchanged, in particular: expected values come from the register and the Stage S cases as written, never from running `qualification/ssds80/models/`, and production code never imports those models (§5.1 item 3); Core's own suite and the frozen-profile tests pass unchanged apart from names (§5.1 items 1 and 6, as amended by SD-56).

## 2. Package layout

One program, `ssds` (SD-56, Manual §26.3 as amended by A7): one distribution built from `orchestrator/pyproject.toml`, one regular import package `ssds` under `orchestrator/src/ssds/`, one console script `ssds = "ssds.cli:main"`. `ssds` is a first release with no predecessor installation (SD-57): no compatibility, detection or migration for earlier names, configuration or data. Identifiers inside frozen profiles and persisted records (`sdp.content.v1` and the other digest schemes, `sdp.stage-result-envelope`, the `SDP_STAGE_RESULT_V1` footer, profile id `sdp-protocol-5.16`) are data and unchanged, as are the snapshot bytes.

| Path under `orchestrator/src/ssds/` | Owner | Public modules other owners may import |
|---|---|---|
| `core/` | Level 0 Core, behaviour unchanged (§26.4) | `core.api.v1`, `core.spi.v1`; the root module also imports `core.cli`, Core's command set |
| `content/` | Content Model (§26.1) | the package |
| `analyzers/` | Analyzers | the package |
| `ledger/` | Ledger Store | `ledger.read`, `ledger.qualification`; `ledger.append` for Admission only |
| `derivation/` | Derivation Engine | the package |
| `admission/` | Admission | `admission.request` (the admission request API) |
| `dispatcher/` | Dispatcher (empty until Phase F) | the package |
| `interface/` | Interface (empty until Phase E) | `interface.render` |
| `api/v1.py`, `spi/v1.py` | public surfaces (§26.3) | re-export facades; no component imports them |
| `cli.py` | the root module, the only composition root | none; nothing imports it |

Any other submodule is private to its owner. Phase D fills `content`, `analyzers`, `ledger`, `derivation` and `admission` (genesis path and `request` types only).

**Composition.** `ssds.cli` mounts one flat command set: Core's registered commands (prompt, the profile stage commands, `projects`, `capabilities`, `doctor`), then the SSDS operations as their owners provide them (none in Phase D; the Interface is Phase E). A name claimed twice raises at composition, so acceptance catches it. Core's command module no longer runs on its own (`python -m` entry removed); the checkout launcher is `orchestrator/bin/ssds`. Core still discovers other programs' extensions through `ssds.extensions.v1`; the SSDS components are not extensions.

**Interpreter.** `ssds` requires Python 3.11 or newer (`requires-python`; `tomllib` and the typing the program uses). A host whose system `python3` is older, as on the stakeholder's machine (3.10), runs `ssds` from a virtual environment made from a newer interpreter; the first-day docs (`orchestrator/README.md`, the Core user guide §1) say how.

**Operator data.** Core reads its configuration from `$SSDS_HOME/config.toml`, `$SSDS_HOME` defaulting to `~/.ssds` and required to be absolute; `ssds doctor` names the home and writes nothing, and the home is created on first write (the ledger, step 3). Ledger repositories (one per project, §21.5 option (ii)), `LOCAL_TRUST` witness stores, the derived index and caches, and later Dispatcher workspaces and journals live in the same home.

**Reading of the §26.2 table (D4 reconciliation, no decision changed).** Rows that say "only" (content, analyzers, ledger, derivation) are closed lists, so derivation imports no Core module either. The SSDS-component lists of admission, dispatcher and interface are closed too; those three may also use Core's public API (`core.api.v1`, `core.spi.v1`), since §26.4 reuses Core records (`WorktreeKey`, `DigestRef`, `ProtocolProfileRef`) in them. Nothing but the root module imports a Core private module. The api/spi facades depend on components, never the reverse, so the dependency graph stays acyclic.

## 3. Steps, in order

| Step | Modules | Realizes register rows | Tests (under `orchestrator/tests/ssds/`) |
|---|---|---|---|
| **1** skeleton and fitness (done; renamed by SD-56) | the seven component packages, `api.v1`, `spi.v1`, the root module `ssds.cli` | §26 | `test_fitness.py` (§26.2, §4); `test_program.py` (the root mounts Core's command set flat, a collision fails, Core loads no component); Core's installed-product suite runs the `ssds` console script |
| **2** content and analyzers | `content`: data-only manifest parser (`tomllib`), scope-term resolvers (whole file, path prefix, Markdown heading span, symbol span, anchor span, file in composite) returning `ABSENT`, partition by construction, Git-tree-entry content identity with the one anchor normalization, revision and `scope_id`, static structural checks; `analyzers`: a pinned Python `IMPORTS` analyzer with its completeness declaration and incompleteness markers | §1.1-§1.11, §2.6 (analyzer declarations) | group 1 structure cases |
| **3** ledger | `ledger`: closed schema (§3 kinds, envelope, tiers), canonical JSON (RFC 8785, Core's `canonical_json`, §6), entry format, digest chain and Ed25519 signature verification (`cryptography`, SD-56, added to the distribution's dependencies here), the store reading `refs/ssds/ledger/<id>` by object identity in a ledger repository in the SSDS home (§21.5 (ii) by default), `read`; `qualification` (§23.4 states from witness checkpoints and a high-water mark; local-trust witness as an append-only directory in the SSDS home); `append` (compare-and-swap of the one ledger ref) | §3, §21, §23 read path, §27-§28 | ledger chain and qualification cases, group 4's qualification-state and loss-bound cases as read-path checks only |
| **4** derivation S0-S2 | `derivation`: S0 (ruleset in force, effective structure as a fold, quarantine, tenure, relations, well-formedness, cycle legality, closure), S1 (challenge polarity, force, `cont`), S2 (support fixed point with the support-cycle clamp, gate term, evidence term, early cutoff, acting records, frames `D_n[X]`, the pinned merge), §5.10 judgment disagreement (`W`, typed targets, reach, the four routes with per-state eligibility), §6 matching predicates and staleness | §1.6, §2.4-§2.5, §4.1-§4.6, §5.1-§5.7, §5.10, §6, §7 | groups 1, 2 and 3 derivation halves |
| **5** derivation S3 kernel and determinism | S3 integrity findings, `INTEGRITY_HALT`, `REQUALIFY` and intake obligations, historical views; keyed caches and checkpoints; the query functions Phase E will render | §5.7-§5.9, §23.6 (boundary reads) | determinism and replay; incremental equals from-scratch (property tests over generated ledgers) |
| **6** Admission genesis path | `admission`: build the genesis entry and `Σ_0` in an isolated workspace, validate every declaration, static check, trust root and witness reachability, accept only `LEGACY(p)` or `UNGOVERNED` modes, take the human gate as an authenticated approval of the entry digest, append and admit under its own quorum (`LOCAL_TRUST` allowed); nothing published before admission; nothing written to a product or program repository | §19.9, §21.3, §22.4 (genesis only), §23.3 | genesis validation and refusal cases on fixture repositories; the shadow-boundary check (§4) |
| **7** end to end | derivation of a shadow genesis of this repository's history (Case B: `LEGACY(p)` section-level parts, no file rewritten), its ledger in the SSDS home | §19.9 Case B | the Phase D exit run, executed only after the stakeholder's genesis gate and approval key (§7 Q3) |

Each step closes with its tests, Core's suite, `run_models.py --seeds` (unchanged) and `git diff --check` before the next starts. Phase D ends with an independent implementation Review (G2 workplan §5.1 item 5).

## 4. Fitness checks (Manual §26.2) and the shadow-boundary sensor

`orchestrator/tests/ssds/fitness.py` is a static checker over the source trees (AST imports with relative imports resolved, string constants, `pyproject.toml` files); `test_fitness.py` runs it on the real tree, expecting no violation, and on synthetic trees, each made to break one rule, expecting exactly that rule's violation. The expected violation of each synthetic tree is written from the Manual's rule, not computed by the checker.

| Code | Rule | Source |
|---|---|---|
| F0 | every program module belongs to Core, one §26.1 component, a facade, the root module or the top package | §26.1, §26.3 |
| F1 | content and analyzers import only Core public API/SPI and each other's package | §26.2 row 1 |
| F2 | derivation imports only content, analyzers and `ledger.read` | §26.2 row 2 |
| F3 | ledger imports only Core public API/SPI; `ledger.append` is imported only by admission, and the ledger package does not re-export it | §26.2 row 3 |
| F4 | admission imports derivation and ledger among SSDS components; never dispatcher or interface | §26.2 row 4 |
| F5 | dispatcher imports derivation, `ledger.qualification`, `interface.render` and `admission.request` only | §26.2 row 5 |
| F6 | interface imports derivation, `ledger.qualification` and `admission.request` only | §26.2 row 6 |
| F7 | `ssds.core` imports nothing from the SSDS components or the root module, by import or by module-name string | §26.2 row 7 (A7) |
| F8 | derivation imports only an allowlist of pure standard-library modules (no clock, network, environment, process, filesystem or Git access) and calls no dynamic-import or I/O builtin | §26.2 "also enforced" |
| F9 | every program file lives under `orchestrator/` (source under `orchestrator/src/ssds/`), and the repository has exactly one `ssds` distribution, at `orchestrator/pyproject.toml` | §26.2 "also enforced" |
| F10 | one composition root: the distribution declares exactly the console script `ssds = "ssds.cli:main"`, no other distribution claims `ssds`, the program registers nothing in `ssds.extensions.v1`, and no program module is runnable on its own (`__main__`) | §26.2, §26.3 (A7) |
| F11 | no private cross-module imports: across owners only the public modules of §2, no Core module but `core.api.v1` and `core.spi.v1` (and `core.cli` for the root), no `_`-prefixed module or name, no dynamic import or code execution | §26.2 "also enforced" |
| F12 | no component imports the api/spi facades, nothing imports the root module, the top package imports nothing; program source imports only the standard library, `ssds` and its declared dependencies | §26.3 (D4 reading, §2) |
| F13 | nothing under `orchestrator/src/` or `orchestrator/tests/` imports `qualification` or the Stage S models | G2 workplan §5.1 item 3 |
| B1 | shadow boundary: only content and ledger start processes, and Git subcommands that write objects, refs or files appear in argv-shaped literals only in `ledger.append` | G2 workplan §5.1 item 2 |

Core's own layout and fitness suite keeps Core's rules (no Tracker/Adapter/Scheduler modules, read-only Git, one entry-point group). What the checks cannot see: behaviour through data (a string passed to a subprocess built at run time), imports performed by third-party code, and anything outside the parsed trees. They are sensors of the dependency rule, not proof of it (Manual §26.2). B1 is static only; Phase D's genesis tests check at run time that appends touch only `refs/ssds/ledger/`.

## 5. Acceptance groups 1-3: cases and negative discriminators carried

Expected results come from the register row and the Stage S case's stated outcome, transcribed into the test as literal data with the case name cited. The "derivation half" of a group is the part decidable from a ledger and trees alone; the admission halves are Phase F's.

| Group | Stage S cases carried (G2 workplan §5.3) | Review-named discriminators carried in Phase D | Deferred to a later phase, with reason |
|---|---|---|---|
| **1** derivation, structure, relations | S5 §1 (10): `governed_boundary`, `concurrent_admission_not_counted`, `combination_effect`, `new_part_over_existing_bytes`, `span_shift_not_a_change`, `equal_sibling_regions`, `partial_overlap`, `nested_non_member`, `member_outside_composite`, `composite_absent_member_survives`; S5 §2-§4 (13, in `cases_s5_2_4.py`: 6 cycle-legality and 5 closure cases, and the two S5 §5 support cases that group 3 also carries) | 3540d98 B1, e2154ac B1, e9e6e9f B1: one content representation read by every consumer (CRLF, mode, symlink, gitlink, LFS and submodule fixtures through the content model); f22b4dc N5: re-identification of a D1/D2 revision under an analyzer change; b46c250 N4 and f7419d5 N4: an anchor move giving a D2 unit different bytes is a `VIOLATION`, and a case isolating the region criterion from owned content; 5c55d4b N6: 27ef339 B2's discriminators (C) and (D) | the runner half of the representation discriminators (a designated runner materializing the tree entry) is Phase F |
| **2** assessment disagreement | S5 §6 (7): `differing_pin_goes_to_owner`, `differing_free_attribute_goes_to_owner`, `unpinnable_supports_no_stop`, `context_change_keeps_implication`, `unbounded_run_still_linked`, `genuine_fix_is_stale`, `revert_yields_again`; the `s1_disagreement_model_check.py` seed's histories as fixtures | 798b2b4 B4 (each link traversed is recorded in the derived explanation); 29da56e N5 (counter-challenge, observation dismissal, triple dismissal, chain class, support route, adjudication recovery); 5c55d4b N6 (a failure whose only reproductions are unbounded); 124b0b7 N2 (provisional discharge where policy permits it, not only under a risk override) | admission of the records involved (Phase F) |
| **3** judgment disagreement | S1 (23: 11 item-level, 12 objection); S2 (22: 7 transformation, 3 binding, 5 target, 7 route) and `G1_QUESTIONS` (the amended reading); S5 §5 (`provisional_propagates_by_min`, `mutual_acceptance_forced_false`) and S5 §7 (9 frame cases) | 051cce3 N5, 362af9f N6, 51070e5 N3, 61cd09b N6, 63ddf91 N5, 6b986de N6, f03b15e N5, f22b4dc N5, 9e5a763 N1, b46c250 N4, d94a293 N3, 575dc78 N5 and f7419d5 N4, each as listed in G2 workplan §5.3 group 3, as derivation cases over constructed ledgers; RR-1 and RR-2's history-derived item-level and transformation cases at the real derivation owner | the RR-11 resolver and Dispatcher half (per-record eligibility through the resolver and Dispatcher) and every case whose distinguishing step is an admission refusal (the §8.3 step 7 support check) are Phase F |

A discriminator is a case a shallow or proxy implementation passes and a correct one fails (Manual §31.2). A group not executed is reported as unexecuted, never as passed.

## 6. SERIOUS CHALLENGE SC-D1 (resolved by SD-56)

Step 1 found that Manual §26.3's `sdp ssds` command group needed a Core CLI seam Core did not have, while G2 workplan §5.1 item 1 forbade a Core change. The stakeholder resolved it by renaming rather than adding a seam (SD-56, decision record item 52): the whole orchestrator is one program `ssds` whose root module composes Core's commands and the SSDS operations (Manual A7; §2 above). SD-56 supersedes §5.1 item 1's "no Core change" and limits §2 item 6 to Core's behaviour.

Reconciliations, no decision changed: RFC 8785 canonical JSON is needed by `content` (the `sem` hash, catalogue §1.5) and by `ledger` (record identity, §3.2), and §26.2 lets each import only Core's public API, so one strict encoder is an additive export of `ssds.core.api.v1` (`canonical_json`), as Core's v1 compatibility rule allows; Core's own frozen `sdp.*` digest schemes are untouched. Qualification reads catalogue §23.4's "`A` is `H*` or `H*`'s single provisional successor" as allowing an observed checkpoint one position beyond `H*` (a checkpoint still being distributed), and nothing further. Git before 2.36 has no reference fsync setting; on such a host the ledger ref update's durability rests on the operating system (a host limit, disclosed in `ledger.append`). Manual §26.3 places SSDS settings in a namespaced `[ssds]` configuration section, but Core's configuration schema is closed (`schema_version`, `core`, `projects`, `protocol_sources`, `extensions`), so that section needs a Core configuration change when the first SSDS setting is needed (§7 Q5).

## 7. Questions for the stakeholder

Answered by SD-56: **Q1** (SC-D1) rename to one program `ssds`; **Q2** `cryptography` accepted for Ed25519; **Q3** everything SSDS writes for an operator lives in the SSDS home (`$SSDS_HOME`, default `~/.ssds`), the ledger by default a dedicated repository there (§21.5 (ii)); by SD-57 the approval key is a new Ed25519 key the stakeholder generates in their own terminal (its public half the genesis trust root for human authentication), and the approval of the genesis digest stays the stakeholder's at step 7; **Q4** the plan stays a companion file.

5. **The `[ssds]` configuration section.** Proposed: when step 3 first needs a setting (ledger and witness locations, key references), add `[ssds]` to Core's configuration owner as a second open section bounded like `[extensions."<ns>"]`: Core validates its size and preserves it, and SSDS interprets it. This is an additive Core configuration change; Core's existing configurations keep their identity.

## 8. Phase D readings and deferrals (steps 4-6)

Where the catalogue leaves a choice to D4 or names a later owner, step 4 reads it as below. Each reading is a Review question in the Phase D implementation Review; none changes a Manual or register decision.

**Readings.**

1. *Bounding currency (catalogue §6.5).* `bound(o)` read literally (currency of the bounding judgment in the frame of evaluation) leaves a genuine fix never stale, contradicting S5 §6 `genuine_fix_is_stale`. Phase D reads it as: the bounding judgment stands, and its `content` entries hold in the matched content `K` of the observation. `test_assessment.py` carries the case and a mutation check showing the literal reading fails it.
2. *Policy schema.* The ruleset's policy object is read as a closed per-domain table: `owner`, `adjudicators`, `acceptors`, `required_judgments`, `gates`, `gate_holders`, `evidence`, `claim_owner`, `humans`, `unattested_agents`. Its digest is in the ruleset; absent keys mean no holder.
3. *Default subject mode.* A genesis `modes` entry `"*"` is the mode of subjects with no entry of their own (so a subject created later is not silently `UNGOVERNED`). The shadow genesis (step 7) sets `"*"` to `UNGOVERNED`.
4. *Admission body.* An admission entry carries `integrates` (the transformation it integrates) and `adopted_deltas` (`{key, value, source}`, `source` `AUTHORED` or `ADOPTED`); the frame's `Δ_Σ(X)` is the candidate's authored manifest delta plus `A`.
5. *Domain of a judgment.* For the routes of §5.10 the domain of a judgment is the domain of the content it judged (for a transformation target, the units it changed), not of the record's target type.
6. *Assessment home.* `home(o)` is the set of units whose scope overlaps a file of the observation's reading, by file overlap; finer regions wait for an analyzer that declares them.
7. *Execution basis.* An execution record's basis is read in the closed `execution` field form the ledger schema states; nothing outside it is an input to `bound`.

**Fail closed until a later owner.** NATIVE D1/D2 targets have no passing acceptance or gate until §10.2's revision runs exist (Phase E); plan-acceptance reach is over-approximated (every item unit) until §13.4's amendment rules (Phase E); declarative verdicts never yield until §14.3's evaluator (Phase E); the admissibility checks of §17.4 are Phase F. Each fails toward "not supported", never toward support.

**Group 3 discriminators not executed in Phase D, with reason.** The D1/D2 revision-run variants of 575dc78 N5, f7419d5 N4 and f22b4dc N5, and the plan half of 63ddf91 N5 (plan relief after amendment or tightening), need §10.2 and §13.4 (Phase E). f03b15e N5's human reassessment of an answered non-gate obligation needs §10.3 (Phase E). 51070e5 N3's adjudication-independence refusal, f03b15e N5's supersession-authority cases (the judgment key of §8.3 step 3) and the other cases whose distinguishing step is an Admission refusal (§8.3 steps 3 and 7) are Phase F. They are reported unexecuted, not passed. The derivation halves are in `test_group3_discriminators.py`, `test_judgment.py` and `test_frames.py`.

**Step 5 readings** (`derivation/s3.py`, `derivation/history.py`; tests `test_s3.py`, `test_determinism.py`).

8. *Which forced components are ordinary (catalogue §5.6 (v)).* A forced component is an ordinary finding when it contains a `valid(s)` edge that §6 adds (an assessment, disposition or bounding completeness judgment about `s`), and an integrity obligation otherwise. This over-approximates the two absorption-extensible `about` terms through `home`, as §5.6 item 2 itself does; every forced node is `F` either way, so the reading changes only the attention, never a value.
9. *Requalification (§23.6).* "In effect at `R`" is `current > F` at the retained head (a relaxer: in force there); "withheld now" is `¬cont`. A fresh record of the same kind on the same target, admitted after the boundary and current now (a relaxer: in force), ends the obligation. Permissive means an evaluated kind with no adverse outcome (failing assessments are unchanged by a boundary).
10. *Views.* A view at a position before the chain's last authenticated entry is historical. No view asserts currentness under an `INTEGRITY_HALT`, an unreadable schema version, a missing pinned analyzer (finding 6ff4ed1 B3), or in a frame; the halt finding and its `CRITICAL` integrity obligation appear in every view.
11. *Checkpoints (§5.9).* A derivation checkpoint caches the S0 fold through a position (per-position head, `Σ`, modes and ruleset, integrations, boundaries, the record index) under the key `(ledger, position, entry digest, ruleset with analyzer set, schema, derivation system version)`, recomputed from the ledger before use, with a body digest; S1-S3 are functions of that fold and the trees, recomputed per view. The encoding is sorted-key JSON (delegated by §5.9). Where checkpoints are stored (the private derived index in the SSDS home) and the write cadence (every 1,000 entries and every lifecycle entry) are the caller's, the Interface in Phase E; derivation writes nothing.

**Deferred from S3.** The re-application obligation of an `OVERTAKEN` admission's open item obligation, readiness, discharge, drift, impact, briefs, conformance and routing views read item obligations and plans (§10, §13), so they are Phase E queries over the same strata.

**Step 6 readings** (`admission/genesis.py`, `derivation/baseline.py`; tests `test_admission_genesis.py`).

12. *Home layout.* Under the SSDS home: `ledgers/<id>.git` (the dedicated ledger repository, §21.5 (ii)), `witness/` (the `LOCAL_TRUST` file witness root), `keys/admission/<id>.ed25519` (the Admission host key, generated by Admission, mode 0600), `genesis/<id>/` (the isolated workspace: proposal, ledger objects, approval message, validation report) and `state/<id>/high-water.json`. The genesis records the ledger location as `ssds-home:ledgers/<id>.git`, relative to the home.
13. *Trees.* §26.2 gives Admission no `content` import, so Admission reads the baseline through a tree source its caller supplies (the composition root wires `content.read_tree`), as derivation does, and validates `Σ_0` through `derivation.baseline_structure`.
14. *What validation refuses.* A missing or unparsable manifest, any §1.9 static error, a mode naming an undeclared subject, a subject with no mode and no `"*"` default, a mode other than `LEGACY(p)` or `UNGOVERNED`, `LEGACY` without `p`, an unparsable policy, no or malformed human key, a witness model failing its class or the quorum inequality, an unreachable witness or one already holding checkpoints for the ledger, and an existing ledger. Other S0 defects of the baseline (relation vocabulary, cycle legality, single definer) are reported in the validation report as ordinary findings: they are §5.7 integrity checks of derivation, not §1.9 static checks.
15. *The gate.* The stakeholder signs the approval message `ssds genesis <digest>` with `ssh-keygen -Y sign -n ssds`; the digest covers the whole genesis record but its id and approval. Admission takes the approval key to be whichever registered human key verifies the signature, re-reads the proposal from the workspace and refuses it if it changed. The genesis record's `governs` is `LEGACY(p)` of the protocol the shadow runs under; its policy object is the baseline's `policy_path` file, or `schema = 1` when there is none; its analyzer object lists the system ruleset's analyzers.
16. *Admitted.* The entry is admitted when the file witness has the fsynced checkpoint (`q_a = 1`) and the read-back chain qualifies `QUALIFIED` at position 0; the high-water mark is then set. Nothing is written to the product repository (checked at run time on its refs, objects and status) and the ledger repository carries only `refs/ssds/ledger/<id>`.

## 9. Repairs after the 0e49deb Review

The Review's implementation blockers are D4 defects at their owners; each repair carries the Review's executed discriminator as a test that fails without it.

- **A-B1** (currentness without qualification). The step 7 report consumer (`scripts/shadow_genesis.py`) now qualifies the chain against the declared witnesses and the high-water mark before deriving (witness reads stay outside derivation, Manual §5.1), derives the qualified prefix through `H*` only, and reports the qualification state, `H*`, any provisional successor and critical obligations. Without a current-qualified head it gives historical views only and exits non-zero. Tests: a removed witness checkpoint (`UNQUALIFIED`), a high-water mark past the chain (`ROLLBACK`), and an appended, never-checkpointed successor (`QUALIFIED` at 0, provisional 1, the answer derived at 0).
- **A-B2** (undeclared responders). `ledger.qualification.qualify` counts only reports keyed by declared witnesses and qualifies nothing over a witness model that fails validation (class, quorum inequality, `N` distinct identities). Test: relabelled copies, a missing declared witness, duplicated identities.
- **A-B3** (writes outside the home). `admission.genesis.Home` checks the ledger id against the unit identity grammar and every resolved path, symbolic links followed, for containment in the resolved home, before any filesystem effect; `prepare_genesis` and `admit_genesis` refuse a bad id having written nothing. Tests: traversal, absolute, slash and upper-case ids at the owner and through the CLI; a symbolic link out of the home.
- **A-B4** (an unresolved term at genesis). `derivation.baseline_structure` requires every non-`prefix` term to resolve in the baseline tree to a present file (possibly empty) or a found span (catalogue §1.9), through `TreeView.term_region`. Tests: missing file, heading, symbol and anchor; an empty file and an empty prefix pass.

The admitted shadow ledger is unaffected: its baseline passes the stricter genesis check, and the repaired consumer qualifies it at head 0 with a current assertion. Not repaired here: SC-1 (an owner decision) and B-B1 (Manual text). The Review's non-blocking N1 (a checkpoint body digest does not authenticate the cached fold) and N2 (the content facade exposes a Git reader the import sensor cannot see) are Phase H and sensor questions, recorded, not changed; N3 (backing up the home-resident ledger) belongs to the first-day docs once the ledger is operated.
