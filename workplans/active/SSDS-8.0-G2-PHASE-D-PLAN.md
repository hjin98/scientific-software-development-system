---
kind: ssds-shadow-phase-plan
workplan_id: SSDS-8.0-G2-PHASE-D-PLAN
protocol_version: 7.2.1
target_system_version: 8.0.0
status: active
created_date: 2026-10-19
governing_workplan: workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md (revision 3, Stage D, §5.2 Phase D row)
governing_architecture: orchestrator/docs/ssds-8.0-architecture.md (accepted at G1, SD-50; amendments A1-A6 accepted, SD-53 and SD-55)
g2_authorization: SD-55 (shadow implementation only)
active_serious_challenge: SC-D1 (Manual §26.3 `sdp ssds` command group; not blocking Phase D, §6)
---

Governing SSDP version: 7.2.1.

# SSDS 8.0 — Stage D Phase D plan: the read-only kernel

```text
STATUS: ACTIVE. Companion to the G2 shadow workplan, Stage D (§5.2 Phase D row). It concretizes
        that row into files, modules and test groups; it adds no mechanism beyond the settled
        register (G2 workplan §4.2) and changes no Manual decision.
SHADOW: no SSDS authority over any subject; every subject LEGACY(p) or UNGOVERNED; no cutover. The
        document-controlled 7.2.1 baseline governs. The shadow genesis human gate is the stakeholder's.
DONE SO FAR: §3 step 1 (package skeleton, extension registration, §26.2 fitness checks).
NEXT ACTION: the stakeholder reads this plan and answers §7; then §3 step 2 (content and analyzers).
```

## 1. Scope and authority

The G2 workplan's Phase D row builds `content`, `analyzers`, `ledger` (schema, chain verification, store, qualification read path), `derivation` (strata S0-S3 and queries), the Manual §26.2 fitness checks, and Admission's genesis path only (Manual §19.9), realizing register rows §1-§7, §19.9, §21, §23 read path and §27-§28. Its exit evidence for G3 is acceptance groups 1, 2 and 3 (derivation halves), determinism and replay, incremental equals from-scratch, and a shadow genesis of this repository's history derived end to end.

This file decides only D4 placement and order. Every behaviour cites the register row it realizes; a behaviour no row covers returns to Stage S (G2 workplan §5.6). Rules of G2 workplan §5.1 apply unchanged, in particular: expected values come from the register and the Stage S cases as written, never from running `qualification/ssds80/models/`, and production code never imports those models (§5.1 item 3); Core's own suite and the frozen-profile tests run unchanged (§5.1 item 6).

## 2. Package layout

One distribution, `sdp-orchestrator-ssds`, at `orchestrator/ssds/` (its own `pyproject.toml`, depending on `sdp-orchestrator-core`; Core's `orchestrator/pyproject.toml` is untouched). Native namespace package `sdp_orchestrator.ssds`, no root `__init__.py` in `sdp_orchestrator`.

| Path under `orchestrator/ssds/src/sdp_orchestrator/ssds/` | Owner (Manual §26.1) | Public modules other components may import |
|---|---|---|
| `content/` | Content Model | the package |
| `analyzers/` | Analyzers | the package |
| `ledger/` | Ledger Store | `ledger.read`, `ledger.qualification`; `ledger.append` for Admission only |
| `derivation/` | Derivation Engine | the package |
| `admission/` | Admission | `admission.request` (the admission request API) |
| `dispatcher/` | Dispatcher (empty until Phase F) | the package |
| `interface/` | Interface (empty until Phase E) | `interface.render` |
| `api/v1.py`, `spi/v1.py` | public surfaces (Manual §26.3) | re-export facades; no component imports them |
| `extension.py` | the one Core extension provider, `sdp.ssds` | none; Core loads it through the entry point |

Any other submodule is private to its component. Phase D fills `content`, `analyzers`, `ledger`, `derivation` and `admission` (genesis path and `request` types only).

**Registration.** `orchestrator/ssds/pyproject.toml` declares exactly one entry point, `sdp.ssds = "sdp_orchestrator.ssds.extension:provider"` in Core's group `sdp_orchestrator.extensions.v1`, and no console script. The provider declares no capability until a component provides one; Phase D adds `ssds.derive`, `ssds.ledger` and `ssds.qualify` (Manual §26.4 row 17) as their services become real.

**Reading of the §26.2 table (D4 reconciliation, no decision changed).** Rows that say "only" (content, analyzers, ledger, derivation) are closed lists, so derivation imports no Core module either. The SSDS-component lists of admission, dispatcher and interface are closed too; those three may also use Core's public API (`core.api.v1`, `core.spi.v1`), since §26.4 reuses Core records (`WorktreeKey`, `DigestRef`, `ProtocolProfileRef`) in them. Nothing imports a Core private module. The api/spi facades depend on components, never the reverse, so the dependency graph stays acyclic.

## 3. Steps, in order

| Step | Modules | Realizes register rows | Tests (under `orchestrator/ssds/tests/`) |
|---|---|---|---|
| **1** skeleton and fitness (done) | the seven component packages, `api.v1`, `spi.v1`, `extension.py` | §26 | `test_fitness.py` (§26.2, §4); `test_installed_extension.py` (Core discovers and activates the installed distribution; Core's suite runs without it) |
| **2** content and analyzers | `content`: data-only manifest parser (`tomllib`), scope-term resolvers (whole file, path prefix, Markdown heading span, symbol span, anchor span, file in composite) returning `ABSENT`, partition by construction, Git-tree-entry content identity with the one anchor normalization, revision and `scope_id`, static structural checks; `analyzers`: a pinned Python `IMPORTS` analyzer with its completeness declaration and incompleteness markers | §1.1-§1.11, §2.6 (analyzer declarations) | group 1 structure cases |
| **3** ledger | `ledger`: closed schema (§3 kinds, envelope, tiers), canonical JSON (RFC 8785, own encoder, since Core's is not public), entry format, digest chain and Ed25519 signature verification, the store reading `refs/ssds/ledger/<id>` by object identity, `read`; `qualification` (§23.4 states from witness checkpoints and a high-water mark; local-trust witness as an append-only directory); `append` (compare-and-swap of the one ledger ref) | §3, §21, §23 read path, §27-§28 | ledger chain and qualification cases, group 4's qualification-state and loss-bound cases as read-path checks only |
| **4** derivation S0-S2 | `derivation`: S0 (ruleset in force, effective structure as a fold, quarantine, tenure, relations, well-formedness, cycle legality, closure), S1 (challenge polarity, force, `cont`), S2 (support fixed point with the support-cycle clamp, gate term, evidence term, early cutoff, acting records, frames `D_n[X]`, the pinned merge), §5.10 judgment disagreement (`W`, typed targets, reach, the four routes with per-state eligibility), §6 matching predicates and staleness | §1.6, §2.4-§2.5, §4.1-§4.6, §5.1-§5.7, §5.10, §6, §7 | groups 1, 2 and 3 derivation halves |
| **5** derivation S3 kernel and determinism | S3 integrity findings, `INTEGRITY_HALT`, `REQUALIFY` and intake obligations, historical views; keyed caches and checkpoints; the query functions Phase E will render | §5.7-§5.9, §23.6 (boundary reads) | determinism and replay; incremental equals from-scratch (property tests over generated ledgers) |
| **6** Admission genesis path | `admission`: build the genesis entry and `Σ_0` in an isolated workspace, validate every declaration, static check, trust root and witness reachability, accept only `LEGACY(p)` or `UNGOVERNED` modes, take the human gate as an authenticated approval of the entry digest, append and admit under its own quorum (`LOCAL_TRUST` allowed); nothing published before admission | §19.9, §21.3, §22.4 (genesis only), §23.3 | genesis validation and refusal cases on fixture repositories; the shadow-boundary check (§4) |
| **7** end to end | derivation of a shadow genesis of this repository's history (Case B: `LEGACY(p)` section-level parts, no file rewritten) | §19.9 Case B | the Phase D exit run, executed only after the stakeholder's genesis gate |

Each step closes with its tests, Core's suite, `run_models.py --seeds` (unchanged) and `git diff --check` before the next starts. Phase D ends with an independent implementation Review (G2 workplan §5.1 item 5).

## 4. Fitness checks (Manual §26.2) and the shadow-boundary sensor

`orchestrator/ssds/tests/fitness.py` is a static checker over the source trees (AST imports with relative imports resolved, string constants, `pyproject.toml` files); `test_fitness.py` runs it on the real tree, expecting no violation, and on synthetic trees, each made to break one rule, expecting exactly that rule's violation. The expected violation of each synthetic tree is written from the Manual's rule, not computed by the checker.

| Code | Rule | Source |
|---|---|---|
| F0 | every SSDS module belongs to one §26.1 component, a facade, the extension module or the top package | §26.1, §26.3 |
| F1 | content and analyzers import only Core public API/SPI and each other's package | §26.2 row 1 |
| F2 | derivation imports only content, analyzers and `ledger.read` | §26.2 row 2 |
| F3 | ledger imports only Core public API/SPI; `ledger.append` is imported only by admission, and the ledger package does not re-export it | §26.2 row 3 |
| F4 | admission imports derivation and ledger among SSDS components; never dispatcher or interface | §26.2 row 4 |
| F5 | dispatcher imports derivation, `ledger.qualification`, `interface.render` and `admission.request` only | §26.2 row 5 |
| F6 | interface imports derivation, `ledger.qualification` and `admission.request` only | §26.2 row 6 |
| F7 | Core imports nothing from SSDS, by import or by module-name string | §26.2 row 7 |
| F8 | derivation imports only an allowlist of pure standard-library modules (no clock, network, environment, process, filesystem or Git access) and calls no dynamic-import or I/O builtin | §26.2 "also enforced" |
| F9 | every SSDS file lives under `orchestrator/` | §26.2 "also enforced" |
| F10 | one extension registration: exactly one entry in group `sdp_orchestrator.extensions.v1` in the repository, `sdp.ssds` in the SSDS distribution, which declares no console script | §26.2, §26.3 |
| F11 | no private cross-module imports: across components only the public modules of §2, no Core module but `core.api.v1` and `core.spi.v1`, no `_`-prefixed module or name, no dynamic import or code execution | §26.2 "also enforced" |
| F12 | no component imports the api/spi facades or the extension module; SSDS source imports only the standard library, `sdp_orchestrator` and its declared dependencies | §26.3 (D4 reading, §2) |
| F13 | nothing under `orchestrator/ssds/` imports `qualification` or the Stage S models | G2 workplan §5.1 item 3 |
| B1 | shadow boundary: only content and ledger start processes, and Git subcommands that write objects, refs or files appear only in `ledger.append` | G2 workplan §5.1 item 2 |

What the checks cannot see: behaviour through data (a string passed to a subprocess built at run time), imports performed by third-party code, and anything outside the parsed trees. They are sensors of the dependency rule, not proof of it (Manual §26.2). B1 is static only; Phase D's genesis tests check at run time that appends touch only `refs/ssds/ledger/`.

## 5. Acceptance groups 1-3: cases and negative discriminators carried

Expected results come from the register row and the Stage S case's stated outcome, transcribed into the test as literal data with the case name cited. The "derivation half" of a group is the part decidable from a ledger and trees alone; the admission halves are Phase F's.

| Group | Stage S cases carried (G2 workplan §5.3) | Review-named discriminators carried in Phase D | Deferred to a later phase, with reason |
|---|---|---|---|
| **1** derivation, structure, relations | S5 §1 (10): `governed_boundary`, `concurrent_admission_not_counted`, `combination_effect`, `new_part_over_existing_bytes`, `span_shift_not_a_change`, `equal_sibling_regions`, `partial_overlap`, `nested_non_member`, `member_outside_composite`, `composite_absent_member_survives`; S5 §2-§4 (13, in `cases_s5_2_4.py`: 6 cycle-legality and 5 closure cases, and the two S5 §5 support cases that group 3 also carries) | 3540d98 B1, e2154ac B1, e9e6e9f B1: one content representation read by every consumer (CRLF, mode, symlink, gitlink, LFS and submodule fixtures through the content model); f22b4dc N5: re-identification of a D1/D2 revision under an analyzer change; b46c250 N4 and f7419d5 N4: an anchor move giving a D2 unit different bytes is a `VIOLATION`, and a case isolating the region criterion from owned content; 5c55d4b N6: 27ef339 B2's discriminators (C) and (D) | the runner half of the representation discriminators (a designated runner materializing the tree entry) is Phase F |
| **2** assessment disagreement | S5 §6 (7): `differing_pin_goes_to_owner`, `differing_free_attribute_goes_to_owner`, `unpinnable_supports_no_stop`, `context_change_keeps_implication`, `unbounded_run_still_linked`, `genuine_fix_is_stale`, `revert_yields_again`; the `s1_disagreement_model_check.py` seed's histories as fixtures | 798b2b4 B4 (each link traversed is recorded in the derived explanation); 29da56e N5 (counter-challenge, observation dismissal, triple dismissal, chain class, support route, adjudication recovery); 5c55d4b N6 (a failure whose only reproductions are unbounded); 124b0b7 N2 (provisional discharge where policy permits it, not only under a risk override) | admission of the records involved (Phase F) |
| **3** judgment disagreement | S1 (23: 11 item-level, 12 objection); S2 (22: 7 transformation, 3 binding, 5 target, 7 route) and `G1_QUESTIONS` (the amended reading); S5 §5 (`provisional_propagates_by_min`, `mutual_acceptance_forced_false`) and S5 §7 (9 frame cases) | 051cce3 N5, 362af9f N6, 51070e5 N3, 61cd09b N6, 63ddf91 N5, 6b986de N6, f03b15e N5, f22b4dc N5, 9e5a763 N1, b46c250 N4, d94a293 N3, 575dc78 N5 and f7419d5 N4, each as listed in G2 workplan §5.3 group 3, as derivation cases over constructed ledgers; RR-1 and RR-2's history-derived item-level and transformation cases at the real derivation owner | the RR-11 resolver and Dispatcher half (per-record eligibility through the resolver and Dispatcher) and every case whose distinguishing step is an admission refusal (the §8.3 step 7 support check) are Phase F |

A discriminator is a case a shallow or proxy implementation passes and a correct one fails (Manual §31.2). A group not executed is reported as unexecuted, never as passed.

## 6. SERIOUS CHALLENGE SC-D1 (not blocking Phase D)

Manual §26.3 says SSDS adds the command group `sdp ssds` under the one `sdp` root, and G2 workplan §5.1 item 1 says no Core change is needed or allowed. Core's CLI (`orchestrator/src/sdp_orchestrator/core/cli.py`) builds its commands at import and has no seam through which an extension adds commands; Core loads extensions only inside `create_application`. So the command group cannot exist without changing Core. Phase D needs no CLI: the genesis path and derivation are library functions, so step 1-6 proceed. The decision belongs to the Manual's owner and the stakeholder before Phase E (§7 Q1).

Two smaller reconciliations, no decision changed: Core's configuration owner holds extension settings under `[extensions."sdp.ssds"]`, which realizes §26.3's "namespaced `[ssds]` section"; Core's canonical-JSON encoder is not public API, so the ledger carries its own RFC 8785 encoder (§3 step 3).

## 7. Questions for the stakeholder

1. **SC-D1, the `sdp ssds` command group.** Options: (a) an additive Core seam letting an extension register a command group, as a separate Core change with its own decision against PC-001; (b) keep Core frozen and run SSDS commands through `python -m sdp_orchestrator.ssds`, which composes through Core's `create_application` (still one composition root) and amend Manual §26.3 to say so; (c) defer until Phase E. Recommendation: (c) now, then (b) for shadow, revisiting (a) before G3.
2. **Ed25519 dependency.** The ledger needs Ed25519 signing and verification (Manual §21.2, §23.2), which the standard library lacks. Proposed: `cryptography` (PyCA) as the SSDS distribution's one added runtime dependency.
3. **Genesis gate for step 7.** The shadow genesis of this repository's history needs your human gate (Manual §19.9). Proposed: the gate is an authenticated approval of the genesis entry's digest, presented with the validation report; the ledger at `refs/ssds/ledger/<ledger_id>` in this repository (§21.5 option (i)), deployment class `LOCAL_TRUST` with one witness directory outside the repository. Confirm the location and witness medium, or choose a dedicated private ledger repository.
4. **Placement of this plan.** This companion file holds the Phase D plan instead of a new section in the reviewed G2 workplan, whose only change is its §8 state row. Say if you prefer it inside the workplan.
