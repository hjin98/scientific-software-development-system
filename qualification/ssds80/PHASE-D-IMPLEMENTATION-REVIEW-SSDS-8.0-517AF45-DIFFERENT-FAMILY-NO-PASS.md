# Independent Review — SSDS 8.0 Phase D, corrected A7 and A8

```text
GOVERNING SSDP: 7.2.1
PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
CANDIDATE: 517af4551e0b4ea000bd80fe47b1f1f9b4e0e562
PREVIOUS CANDIDATE: 0e49debe63346e72db69ed8e30c14f5bbd58a083
BASELINE: e88d90dec4143340fffcf5cd53e7de5167d46be0
SCOPE: (A) Phase D implementation and exit; (B) corrected Manual A7; (C) Manual A8
MANUAL BLOB: 6226f323365966bbcf653545f3a35b1fd7d6e060
PHASE D PLAN BLOB: 60244394384c4d3d438f8638bc6dfcd02bebf746
G2 WORKPLAN BLOB: 523464de8ad6ec45379bad7e49660a471868cf49
CATALOGUE BLOB: 471e9ea3d44812feba68e64d8e2f22f1bd6cc73d
REVIEW METHOD: independent owner reconstruction; bounded Challenge Pass over repair
               delta and siblings; out-of-matrix trajectories; real CLI, signed
               ledger and derivation probes; semantic mutations; required checks
REVIEWER: GPT family; engaged through Codex CLI in the stakeholder's own terminal
          at the stakeholder's request. The author's session supplied only the
          pointer prompt and did not frame the candidate otherwise. This context
          did not author the candidate.
```

The named `PHASE-D-IMPLEMENTATION-REVIEW-HANDOFF-SSDS-8.0-517AF45.md` governs this Review. The stakeholder worktree was on the requested branch at `27e50740b15b19bdb25d576f2a2558c4a12aa2f7`; that newer tip is not the reviewed subject. Execution used an archive of the exact candidate with separate scratch Git metadata. Review scratch, throwaway keys and every SSDS home used here are confined to `/tmp/ssds80-phase-d-review-517af45`. The stakeholder's private ledger and keys were not read. This record is the sole authored repository deliverable; no implementation change, commit or push was made.

The governing roles were entered at the pinned public source: implementation for A, design for B/C, with their kernel, specification, architecture, workflow, testing, definition, evidence and applicable PEM owners. The accepted Manual and stakeholder decisions, then the G2 register's settled mechanisms, supplied the semantics. Models, author tests, previous conclusions and memory supplied hypotheses or bounded evidence.

## SERIOUS CHALLENGE

**No new SERIOUS CHALLENGE established.** Previous SC-1 was a real conflict: evaluation-state currency of the old runs' bounding judgments loses their old content entries after a genuine fix, preventing condition (1) of staleness. SD-58 resolves that owning decision through the matched-content/state-of-evaluation split. A8 faithfully states it and passes technical Review below. This does not itself accept the author's amendment text.

The surviving findings are violations of coherent D3/settled mechanisms, not reasons to change the stakeholder's decisions. The inherited literal wording and previous NO-PASS remain historical evidence; they are not silently relabelled as passes.

## Verdict

| Subject | Verdict | Consequence |
|---|---|---|
| **A — Phase D implementation and exit** | **NO-PASS** | Neither implementation nor Phase D exit passes. A-B3 remains open; A-B5 and A-B6 below are additional implementation blockers. Phase E's dependent work cannot start on this record. |
| **B — A7 as corrected** | **PASS** | Technical Review of the text, including the table-only reconstruction discriminator. Stakeholder acceptance remains separate. |
| **C — A8** | **PASS** | Technical Review of the amendment's bounded semantic decision. The implementation's misuse of an adverse completeness judgment is A-B6, not permission conferred by A8. Stakeholder acceptance remains separate. |

All prescribed positive suites pass. The counterexamples below prevent their promotion into Phase D closure.

## Disposition of every previous finding

| Previous finding | Disposition at this candidate |
|---|---|
| **SC-1** | **Owning decision resolved by SD-58; amended text technically passes.** Genuine-fix/revert, blocked bound, wrong membership and a cited-record premise have retained real-owner tests. Four A8 mutations below discriminate the changed semantics. Additional probes cover revoked, superseded, vetoed and withheld bounds, forbidden premise modes and a cited-record cycle. A-B6 identifies an additional positive/adverse distinction those tests omit. |
| **A-B1 — no qualification at consumer** | **Original bypass repaired.** The real CLI's missing-checkpoint and ahead-of-chain high-water probes now exit 1, report `UNQUALIFIED`/`ROLLBACK` and withhold currentness. A provisional successor is reported separately and the answer is derived at H*. The wider consumer contract still fails at A-B5. |
| **A-B2 — undeclared responder** | **Closed for Phase D.** `qualify` validates the model and counts only declared witness identities. The foreign-only local case, relabelled TEAM copies and duplicate identities are retained tests. Relabelling the authentic checkpoint from the fresh repository-history genesis as `not-declared` also returns `UNQUALIFIED`. Removing the declared-identity filter makes the named test fail. This is not qualification of a future network witness transport. |
| **A-B3 — home escape** | **PARTIALLY REPAIRED, OPEN.** Traversal/absolute/malformed IDs and an escaping workspace directory are refused before effects; their retained tests pass. A pre-existing workspace **file** symlink still escapes, as reproduced below. |
| **A-B4 — unresolved declaration at genesis** | **Closed.** Missing file, heading, symbol and anchor terms are refused through the baseline/content owner; an empty file and an empty prefix are accepted. Removing the term check produces four assertion failures. |
| **B-B1 — conflicting supersession table** | **Closed.** The §26.4 §3 and §6 rows now reconstruct one distribution, Core inside it, root `ssds.cli`, and extensions for other programs; invariant 11 states the home/default-ledger arrangement. This agrees with §26.3 and SD-56. |
| **N1 — cache checksum** | **Disclosure addressed; residual retained.** `CheckpointInvalid` and plan reading 11 explicitly distinguish accidental-corruption detection from authentication of the cached fold. Checkpoints remain private discardable cache, with the stronger threat boundary left to Phase H. No new cache-integrity guarantee is established here. |
| **N2 — indirect Git reader** | **Named missed dependency detected; sensor remains bounded.** F8 now catches the previously demonstrated permitted-facade reader. NF1 below shows a new false positive on pure code. No production derivation Git read was found. |
| **N3 — home-ledger backup** | **Documentation addressed.** Core user guide §2 explains that a clone omits the home-resident ledger/witness/high-water state and describes backup/restore and requalification. This is documentation evidence, not an executed disaster-recovery qualification. |

These repairs have not previously been accepted as Phase D closure; the remaining home-path defect is incomplete repair within this review cycle, not a claimed PEM recurrence after accepted repair.

## Blocking implementation findings

### A-B3 retained — Checking the workspace directory does not contain its file writes

**Owners and required behavior.** SD-56; Manual §25.4 and §26.3: everything written for an operator belongs in the SSDS home. Phase D plan §9 explicitly promises that `Home` checks every resolved path, following symbolic links, before any filesystem effect. G2 §5.1 item 2 also protects product files from shadow writes.

**Actual owner/path.** `admission/genesis.py:Home.check` checks the ledger, witness root, Admission key, workspace directory and high-water path. It never checks the individual workspace files. `_write_private` opens them with `O_TRUNC` and follows a leaf symlink. `shadow_genesis.py:write_derivation` similarly checks the workspace directory and then writes `derivation.json` beneath it without validating that final path.

**Executed counterexample, no race or outside credential required.** In a valid throwaway product fixture, create an ordinary home and `home/genesis/demo/`. Make `home/genesis/demo/report.json` a symlink to a sentinel file outside that home, but inside review scratch. `Home.check("demo")` accepts it. Run the actual CLI `prepare --public-key <throwaway public key>`. It exits **0**, offers a digest for signature and overwrites the outside sentinel with its validation report. All parent directories remained inside the home. The retained directory-symlink test cannot discriminate this leaf case.

**Consequence.** A path admitted by the repaired validator still directs a truncating write beyond the operator boundary, potentially into a governed file if that is its target. This Review exercised only its own scratch sentinel.

**Minimum repair.** Enforce containment at the existing owner for the **actual files used**, including proposal, objects, approval message, source description, validation/derivation reports and witness descendants, before effects. Preserve the chosen home semantics and use a coherent symlink policy at the write boundary; do not add a parallel path registry. A directory check is insufficient. Race-resistant opening is needed if concurrent path replacement lies within the declared threat model; the demonstrated static escape already blocks without it.

**Required discriminator.** Add leaf-symlink refusal cases through real preparation and report writing. A sentinel outside the home must remain byte-identical; refusal must occur before writes associated with the refused operation. Keep the existing traversal/directory-link controls and positive genesis path.

### A-B5 — The repaired currentness consumer does not retain the last head it qualified

**Owner text.** Manual §23.4: “Every participant that presents current state … keeps a high-water mark: the last head it qualified.” P4 and §23.1 require current answers at a head qualified against the evaluator's observed history. Catalogue §23 is ACCEPTed by G2 §4.2.

**Actual owner/path.** `shadow_genesis.py:qualified_chain` reads `home.high_water(...).get()` and qualifies, but neither it nor `write_derivation` advances that store. Only initial `admit_genesis` sets it, to position 0.

**Executed trace through the real script and signed ledger.**

| Step | Observed result |
|---|---|
| Prepare, independently sign and admit throwaway genesis | Qualified/current at 0; high-water 0 |
| Append a correctly signed position-1 ruleset adoption retaining the supported system, policy and analyzer; write its authentic checkpoint through the real append/witness owner | Readable chain and witness include position 1 |
| Run real CLI `derive` | Exit **0**, `qualified_head = 1`, `current_assertion = true`; stored high-water is still **0** |
| Restore the scratch ledger ref and witness checkpoint set to position 0, preserving the evaluator's high-water file | A second `derive` exits **0**, reports `QUALIFIED` at **0** and asserts currentness |

The first read already violates the last-qualified-head requirement, without assuming any subsequent fault. The restoration then discriminates its consequence: the evaluator forgot a head it had presented as current. This is not a claim of rollback detection beyond the declared witness model; it is failure to preserve the local input that model's qualification procedure requires. No product ref was changed; only the throwaway ledger ref was restored.

**Minimum repair.** Have the existing consumer retain H* through the existing high-water owner as part of successfully qualifying/presenting a current answer, before returning success. Preserve the explicit authenticated abandonment/retirement semantics rather than blindly lowering or resetting the mark. Keep witness and operator-state I/O outside pure derivation.

**Required discriminator.** At the actual CLI, qualify and present head 1, assert persisted high-water 1, then restore the retained chain/witnesses to 0 without restoring that mark. Require `ROLLBACK`, no current assertion and nonzero exit. Retain missing-witness, explicitly ahead-of-chain mark and provisional-prefix tests. An old mark manually advanced by a test does not establish that production maintains it.

### A-B6 — An adverse `INCOMPLETE` judgment can bound a permissive reproduction

**Owners and required behavior.** Manual §2.6 and §4.6 require completeness, with a current **`COMPLETE`** judgment to narrow a closure. Catalogue §3.4 distinguishes `COMPLETE` from `INCOMPLETE`; §5.10 treats `INCOMPLETE` as adverse. SD-58/A8 changes the context of a bounding judgment's premises and standing; it does not turn a denial of completeness into a certificate of it. G2 §4.2's amended §6.5 row retains a **bounded** basis, and an unbounded basis serves no permissive use.

**Actual owner/path.** `derivation/assessment.py:bound` iterates the supplied `bounded_by` IDs, applies `_stands`, membership, analyzer and premise checks, but never requires the record's kind/outcome to be a passing `COMPLETENESS/COMPLETE`. `_stands` does not make that distinction; `Judgments.vetoed` returns false for a non-passing judgment itself.

**Executed discriminator.** Construct the genuine-fix/revert fixture at the real derivation owner. Use a syntactically valid `COMPLETENESS` record with outcome **`INCOMPLETE`**, correct scope/membership and content entries, and no challenge, as the reproduction's sole `bounded_by` record. Supply the old failing execution, a second old-content failure with this bound, and a successful execution on the fix. The record has **zero `record_violations`**. At the fix:

```text
_stands(INCOMPLETE record) = true
bound(reproduction, failing tree) = true
stale(failing assessment) = true
```

The same scope's `COMPLETE` certificate is correctly vetoed by the adverse judgment; the negative record itself is accepted as its replacement certificate. This bypasses the positive/adverse distinction precisely where a permissive stop needs it. A separate probe with an adverse judgment merely vetoing a positive bound correctly yields `bound = false`; that existing behavior does not cover using the adverse record as the bound itself.

**Minimum repair.** At `bound` require a positive completeness certificate of the required kind/outcome before consuming its standing and premises. Keep the amended context split and positive-only support dependencies. Do not postpone this permissive derivation check to general Admission in Phase F, or refuse the adverse judgment's existence: the negative record is valid data and must remain adverse.

**Required discriminator.** Retain this negative-bound fixture beside `BoundingCurrency`, with a positive `COMPLETE` control. The adverse certificate must not satisfy `bound` or make the failure stale. Keep genuine fix/revert, missing/wrong membership, challenged/withheld bounds, cited-record currency and cycle-clamp tests. General malformed `bounded_by` typing/coverage still needs its Phase F admission checks; those future checks are not claimed qualified here.

## Non-blocking findings and limits

**NF1 — F8 also rejects a pure data attribute.** On the checker's clean synthetic tree, add a derivation-local dataclass `Snapshot` with a bytes field named `read_raw` and a pure function returning `snapshot.read_raw`. F8 reports a Git-read violation, although this code performs no I/O. The clean control is clean; the actual forbidden `content.read_tree` fixture is also detected. The new rule tests attribute spelling rather than the object that owns it. This is an overbroad sensor, not an actual forbidden production dependency or current build failure. Narrow it to the forbidden facade imports/references when this sensor is repaired; do not infer purity from it alone. Thus the handoff's “does not refuse legitimate code” question has a negative answer even though the candidate's own code passes.

**NF2 — A8 has stale explanatory siblings in the catalogue.** The §0.3 R1 cell still says a bounding judgment is “current `T`”; §6.6's completeness/structure-polarity explanation still describes losing bounding completeness currency; §8.3 step 5 still permits `stale` to read only “completeness currency,” whereas the amended rule reads the current values of cited records. The displayed signature at §6.5 is still `bound(o)` although its body and use bind `K` and call `bound(o, K)`. These are not all literally updated to A8. They do **not** supply a second applicable meaning: catalogue C.1, the register's §0.3 disposition (expressly read under the Manual/register where candidate-61 wording differs), the explicit amended §6.5 row and SD-58 supply the resolution. Reconcile those explanations/signature locally and carry the cited-premise support constraint into Phase F's admission validation. Do not restore the literal evaluation-frame rule from an old rationale cell.

**NF3 — Retirement consumption remains an uncovered sibling boundary.** The report consumer reads file-witness checkpoints but never consults `FileWitness.retired` or passes `retired` to `qualify`. In scratch, an existing `RETIREMENT` marker makes that API return true while the CLI still reports `QUALIFIED/current`. That marker probe establishes missing wiring; it does **not** qualify authentication or creation of a retirement statement, which belongs to the later security/admission path (§24.2). The helper's explicit `retired=True` test passes. The actual authenticated-retirement-to-consumer path remains unexecuted/unqualified and must be carried forward visibly, not inferred passed from the helper test. A-B5 independently blocks this consumer now.

**A8 cost.** Bounding now checks additional standing/current premises and introduces their support edges. It can withhold a mechanical stop after a cited premise, analyzer, membership or held status is lost; validity/execution premises deliberately fail closed, leaving reassessment/disposition work. These are conservative availability/work costs, not new permissive authority. Existing §32.2 discloses lost continuity and failures remaining for owner disposition when mechanical matching cannot establish a stop. A short A8-specific disclosure would improve navigation; no additional material undisclosed architecture risk was established.

## Judgments required by the current handoff §3

### A — Repairs, A8 implementation and Phase D exit

1. **Every previous finding:** disposed above, with A-B3 explicitly open and the bounds on N1/N2 retained. The old missing-witness, ahead-of-chain mark, foreign-responder, traversal and missing-file probes are preserved in the candidate's real-owner/CLI tests and were rerun in the 207-test suite; selected repairs were also mutated. They are not blanket closure of their families.
2. **Repair siblings:** H* prefix selection and provisional labelling pass their real CLI tests; every other answer is marked historical/withheld in the tested unqualified/rollback regimes. Witness identity/model validation discriminates foreign responses. Home validates IDs/directories but misses leaf files (A-B3). Genesis exempts prefix terms and accepts a present empty file while refusing absent file/span terms. F8 catches the named reader but has the pure-code false positive (NF1). The consumer fails to maintain W (A-B5).
3. **A8 implementation:** `_stands` checks acts, supersession, `CLEAR`, held status, independence and veto separately from the bound's target conditions; it does not use `base(c)` and accidentally reintroduce the evaluation-state membership test. Membership/content are checked on K; cited-record premises require current T from S2 in the evaluation state; standing premises use base T; machinery analyzer membership is checked; validity/execution fail closed. Callers pass S2 values through `stale`, `adverse`, `undisputed` and the support solver. `support_nodes` adds the cited records to subject dependencies. A fresh cited-record cycle is detected/clamped and supplies no bound. Completeness remains a further positive conjunct of `on_plus`, which first requires `on_minus`. **This fidelity is incomplete because of A-B6's missing positive-certificate check.**
4. **Whole Phase D and step 7:** the eleven original questions and sixteen readings are reconciled below. The public stakeholder evidence describes an authentic historical genesis gate and is appropriate evidence of that event. A new throwaway genesis of the exact repository candidate succeeds, but neither run exercises the refusal/currentness/negative-certificate counterexamples. Consequently neither implementation nor Phase D exit passes G2 §5.1 item 5.

### B — Corrected A7

| Judgment | Result |
|---|---|
| Fidelity to SD-56/SD-57 | One program/distribution/import package/command `ssds`; root `ssds.cli`; Core at `ssds.core` retaining version-bound behavior; retired names without alias; one operator home; option (ii) default ledger; first release without predecessor migration. No additional architectural change is inferred. |
| Siblings | Manual §0.5, §16.10, §21.5, §26.1–§26.4, public facade names, home and extension group agree. The corrected §26.4 table alone yields **one distribution containing Core and components, root `ssds.cli`, other extensions through `ssds.extensions.v1`**, exactly the §26.3 assembly. Catalogue candidate-61 packaging is read through the register/amended Manual, not as a second current package contract. |
| Invariants | One composition root; Core imports no components/root; frozen resources unchanged and independently tested; ledger-location semantics unchanged between declared options. PC-001 preserves behavior/resources, not retired executable spellings. A-B3 violates implementation containment without invalidating this coherent text. |
| Cost | No installed-predecessor migration cost under the explicit first-release decision. A clone alone lacks home-resident state; §23/§32.2 and the new backup note disclose custody/loss and restore/requalification costs. No further blocking disclosure gap found. |

### C — A8

| Judgment | Result |
|---|---|
| Gap and reach | Literal evaluation-state content currency conflicts with `genuine_fix_is_stale`. Checking bound content on the matched run content while retaining other evaluation-state premises resolves that exact conflict. SD-58 does not amend ordinary record currency, transfer acceptance across content, authorize stale passing evidence, or weaken adverse matching. |
| Coherence | The recorded basis/context remains immutable (§6.3). Conditions (1)/(3) require bounded permissive matches; conditions (2)/(4) retain adverse links independent of completeness (§6.6). The subject-to-cited-record support edges expose cycles, and losing a positive bound cannot enlarge permissive matches (§5.6). Withheld old judgments supply no stop after a loss boundary (§23.6). Ordinary currency in §2.6/§5.5 and execution support in §17.4 remain distinct from a bound used to compare an old run. |
| No new permissive route in the amendment | Wrong membership has a retained test; revoked, vetoed, superseded and withheld bounds each failed in fresh production-derivation probes; unbounded/changed-pin/free-attribute cases remain negative. An explicit validity or execution premise fails closed. A-B6 is an implementation route from an adverse record, contrary to these positive-certificate semantics. |
| Siblings/cost | NF2 names the stale catalogue statements and their explicit governing resolution; a byte-level claim that every sibling was updated would be false. The actual §6.5 predicate and §5.6 support decision agree with SD-58. Conservative availability/work costs are described above; no further blocker to the amendment text established. |

## The eleven original implementation judgments

| Original question | Current judgment |
|---|---|
| 1. Scope/owners | Content/analyzers resolve supplied content; ledger authenticates/stores; derivation owns S0–S3; Admission owns genesis append; dispatcher/interface remain unimplemented. Inspected placement and fitness checks follow §26. The new reports still require their external qualification/containment duties; those duties cannot be delegated into pure derivation. |
| 2. Plan §8 readings | All sixteen are individually disposed below; reading 1 now has an owning decision. |
| 3. Fail-closed deferrals | Native D1/D2 passing targets remain false pending revision runs; plan-acceptance reach is conservative; unavailable cross-reading/declarative verdicts yield failure. Phase E item/plan/S3 and Phase F general admissibility remain deferred, not passed. A-B6 is already a permissive kernel path and is not excused by those deferrals. |
| 4. Expectations/discriminators | Tests carry fixed register/Stage S outcomes rather than computing expected production values with model rules; F13 passes. Ten finalized semantic mutations below produce assertion failures with passing bases. Cases deferred in plan §8 remain unexecuted. |
| 5. Fitness | F0–F13/B1 pass on the real candidate and synthetic discriminators; the affected named-reader check discriminates its old hole. NF1 bounds legitimate-code acceptance and shows the sensor is not a proof of dependency behavior. |
| 6. Determinism/checkpoints | Historical-prefix, within-entry order, generated-ledger replay and verified-checkpoint resume tests pass, with the supplied eight seeded histories exercising F/P/T. Keys/body corruption are refused. An unkeyed digest does not authenticate a coherently rewritten private cache; N1's limitation remains. |
| 7. Ledger/qualification | Signature/key-in-force/prev/Git-chain, schema-halt versus unreadable-version, CAS, fixed-metadata/reference retention and non-overwriting witness tests pass. Foreign identities are excluded. Maintaining the consumer's high-water state fails (A-B5); authenticated retirement consumption is a gap (NF3). |
| 8. Shadow boundary | Positive genesis tests compare product refs, object inventory and status, with ledger refs only under `refs/ssds/ledger/`. Modes remain LEGACY/UNGOVERNED. A-B3 still falsifies general write containment. No native subject or governed publication was exercised. |
| 9. Core preservation | 393 tests pass, including wheel/sdist installations and frozen profiles. All 22 frozen profile/prompt resources are 100% renames. Source/dist/frozen 1.6.0 Architecture are unchanged. Names/home/discovery and additive canonical JSON are the bounded changes; persisted identifiers stay frozen. Exhaustive old/new differential execution for every possible configuration was not performed. |
| 10. First release | Fresh pip install and installed-product help/doctor/path/first-write tests pass, with no predecessor alias/detection/migration found in the reviewed changed paths. Python 3.11+ and interpreter selection are documented. Home containment remains defective on leaf links. |
| 11. Step 7 | The manifest declares section/component parts of whole legacy protocol/Manual subjects and the ungoverned program without rewriting them. The historical record binds baseline, human signature/digest, public key fingerprint and qualification. A separate throwaway candidate-history run succeeds. Neither grants current private-ledger authentication by this reviewer or closes the implementation blockers. |

### Every Phase D plan §8 reading

| Reading | Disposition |
|---|---|
| 1. Bounding currency | Owning decision supplied by SD-58; text passes; implementation still needs A-B6. |
| 2. Policy schema | Closed data-only per-domain tables; no policy rule language or new policy-value acceptance. |
| 3. Default mode | Explicit `"*"` default prevents silent mode inference; shadow selects UNGOVERNED. |
| 4. Admission body | Integration/adopted-delta facts belong in the fold; general admission enforcement remains Phase F. |
| 5. Judgment domain | Domain follows judged content, not the record-target representation. |
| 6. Assessment home | Conservative file-overlap successor widening adds subjects; does not promise exact arbitrary move/rewrite tracking. |
| 7. Execution basis | Closed recorded basis is the input; admissibility/custody truth is a separate Phase F boundary. |
| 8. Forced-component classification | Every forced component is F; assessment-related/about/completeness cycles are ordinary findings, other support cycles critical integrity obligations. Existing tests and the added cited-premise cycle discriminate value/clamp behavior; all possible absorption histories were not enumerated. |
| 9. Requalification | Retained-current versus withheld-now and fresh acting answers are covered by real derivation tests; full workflow routing remains later. |
| 10. Views | Historical/frame/halt/unreadable/analyzer withholding is retained. The report selects H* but must maintain evaluator state (A-B5). |
| 11. Checkpoints | S0 fold plus recomputed S1–S3 is admissible; replay tests pass; disclosed checksum/private-cache limit remains. |
| 12. Home layout | Layout is delegated within the home; leaf-file containment is missing (A-B3). |
| 13. Tree injection | Caller reads Git; Admission invokes public baseline derivation, preserving the ownership direction. |
| 14. Genesis refusal | Tree-dependent newly declared term presence is now checked, separately from ordinary relation/cycle findings; empty-file/prefix controls pass. |
| 15. Human gate | Proposal digest/SSHSIG/human-public-key checks remain; altered proposal/signature controls pass. Only reviewer-generated throwaway private keys were used here. |
| 16. Admission | Fsynced checkpoint/read-back qualification at genesis precede initialization of W. This does not maintain W for subsequent report reads (A-B5). |

### Later discriminators remain unexecuted

Phase E retains the D1/D2 revision-run variants of 575dc78 N5, f7419d5 N4 and f22b4dc N5; 63ddf91 N5's plan amendment/tightening half; and f03b15e N5's reassessment of an answered non-gate obligation. Item-dependent readiness/discharge/drift/impact/brief/conformance/routing and re-application views remain there. Phase F retains 51070e5 N3's adjudication-independence refusal, f03b15e N5's supersession-authority refusal and other §8.3 steps 3/7 admission discriminators, RR-11 resolver/Dispatcher behavior, and designated-runner materialization/custody. General admission, migration/cutover and authenticated retirement, hostile transport, crash/fault and security qualification are not completed by this kernel Review. None is counted as passed.

## Verification and evidence limits

Execution used Python **3.11.15**, a fresh review virtual environment and the exact candidate. Dependency installation initially failed on sandbox DNS; Core's first runs failed before installed-product tests because fresh build/install environments lacked network/dependency availability. After dependency access was available, the exact required commands completed. These setup failures are not candidate failures, and no required command remains unexecuted.

| Check | Final result |
|---|---|
| `python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt` | PASS, isolated review environment |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | PASS, **207 tests** |
| `python orchestrator/scripts/run_core_tests.py` | PASS, **393 tests across 13 modules**, including actual fresh wheel/sdist installation |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | PASS |
| `python -m unittest discover -s tests -v` | PASS, **435 tests, 3 skips** |
| `python3 -I qualification/ssds80/models/run_models.py --seeds` | PASS, bounded design models/seeds only |
| `git diff --check e88d90de 517af455` | PASS |
| Frozen `source/`, `dist/`, `orchestrator/docs/architecture.md` | Zero changed paths from e88d90de |
| Frozen Core resources | **22 profile/prompt files, R100 renames**, unchanged bytes |
| PEM validation | PASS, schema 1, 5 families, no notices |
| Canonical package build / independent validation / committed parity | PASS, fresh output under review scratch; committed dist matches semantically |
| Real repository-history prepare/sign/admit/derive | PASS at candidate baseline, scratch-only home/key/ledger; `QUALIFIED` H*=0, current assertion true, no findings/obligations |

The three skips are opt-in remote public-fallback realizations for Protocol 6.2/6.3/6.4; they are not passed. No fallback/source identity changed here. The private stakeholder ledger's present state and private signature custody were not independently inspected; the requested historical evidence record was reviewed as such.

The throwaway repository-history genesis signed digest `sha256:2494b2db19ccde924049aafd487e53d895f77b81e1f82117133de4673a951b69`; its entry digest is `sha256:35963a6177ff5c98c859849b5ae32442972beab90471181b4544aea2478bbfd3`, entry commit `27f3194b9dfdae1739798f0de2f38bb912a0c8c6`. Its only ledger ref is `refs/ssds/ledger/ssdp-shadow`. This reviewer-controlled run is engineering reproduction, not another stakeholder approval.

### Mutation discrimination

Each finalized mutant was executed in a separate scratch source copy, with an unmutated passing base. Each produced assertion failure(s), **zero test errors**:

| Wrong variant | Named test | Mutant result |
|---|---|---|
| Bound content entries checked in evaluation state | `Staleness.test_genuine_fix_is_stale` | 1 failure |
| Ignore bound membership | `BoundingCurrency.test_membership_is_checked_on_the_runs_content` | 1 failure |
| Ignore cited-record currency | `BoundingCurrency.test_a_cited_record_premise_holds_in_the_state_of_evaluation` | 1 failure |
| Ignore completeness challenge status | `BoundingCurrency.test_a_challenged_bounding_judgment_bounds_nothing` | 1 failure |
| Count foreign witness IDs | `Qualification.test_only_declared_witnesses_respond` | 1 failure |
| Remove genesis term-presence refusal | `Refusals.test_every_newly_declared_term_resolves` | 4 subtest failures |
| Remove ledger-ID grammar refusal | `Refusals.test_a_ledger_id_never_directs_a_write_outside_the_home` | 6 subtest failures |
| Force the report consumer's qualification to succeed | `ShadowGenesisScript.test_no_current_assertion_without_qualification` | 1 failure |
| Replace adverse linking by direct matching | `Staleness.test_unbounded_run_still_linked` | 1 failure |
| Remove F8's facade-reader name set | `DependencyRuleDiscriminatorTests.test_derivation_reaches_no_git_reader_through_a_permitted_facade` | 3 subtest failures |

An initial extra substitution of `base(c)` for `_stands(c)` did **not** fail the genuine-fix test: base omits content-premise satisfaction, so that substitution alone was not a test of literal evaluation-state content currency. The subsequent content-context mutation above was. Two initial test-name lookup errors were corrected to the actual `Refusals` class before claiming discrimination. Neither the surviving exploratory substitution nor those errors is counted as a killed mutant. The rest of the author's original mutation list was not independently rerun.

Fresh A8 probes additionally observed: clean and standing-premise bounds permit the fix; vetoed/revoked/superseded/withheld bounds and validity/execution premises do not; a cited-record loop produces one forced component and no bound. A valid negative completeness certificate incorrectly permits it (A-B6). These are engineered semantic fixtures through production derivation, not a full scientific validation or exhaustive generated-history proof.

The out-of-matrix pass started from P4, the home-write boundary, and the distinction between a completeness certificate and an objection, temporarily setting aside the test matrix. It found the last-qualified-head trajectory, leaf-link escape and adverse-certificate stop. No additional upstream scientific contradiction or unrealizability of the amended D3 was established. Once these trajectories prevented closure, exhaustive hostile-state/campaign qualification would not change this governed decision and was not undertaken.

Scratch evidence includes `ssds.log`, `core-network-final.log`, `repository.log`, `models.log`, `snapshot.log`, `mutations-final.log`, `probes.log`, `a8-probes.log`, `repository-genesis.log` and the corresponding probe scripts. The findings and outcomes needed to decide are retained above; the decision does not depend on temporary-file retention.

## Project Engineering Memory applicability

The G2 workplan independently binds the accepted/base publication to `main` at `af0455753e20ee54a969c844872e29e270007211`, PEM blob `1561797125622f355f84eb27319f87e8fa4227d9`. Local `main` resolves to that exact state. The candidate PEM has the identical blob, so there is no additional candidate overlay. Schema/publication state and canonical metadata for all five families were inspected; the memory's PARTIAL historical coverage is not treated as absence of other lessons.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: SD-56 and Manual B1 independently require frozen bytes and version-bound Core behavior; unchanged resources and real Core acceptance provide the transfer evidence.
  - id: DS-001
    disposition: APPLICABLE
    reason: Green synthetic matrices cannot close omitted consumer or permissive-owner behavior; fresh negative production-owner probes are required here.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No canonical-source routing repair or regenerated-route change is proposed.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No successor/public-fallback publication occurs.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: Its canonical scope is immutable protocol fallback publication; genesis is judged directly against Manual 19.9 rather than importing the historical label as authority.
```

PC-001's capability transfers through the renamed package without preserving the retired names. No PEM count, salience or lesson supplies authority. No PEM update was made.

## Scientific checks and common-mode note

- **Material findings:** A-B3, A-B5 and A-B6 are the implementation blockers; NF1–NF3 and the disclosed costs/limits are retained. No material scientific-result finding was established.
- **Realized scientific results:** none produced, run or reviewed. This Review prepared engineering gate evidence over program behavior and synthetic histories. It examined the named candidate, repairs, authority texts, public genesis record and fresh throwaway execution; it did not examine a scientific dataset, experiment, trained model or physical-result population.
- **Variants:** no scientific analysis/model/parameter survivor was selected. Engineering exploration included **11 distinct code perturbations** (ten finalized discriminating mutants plus the initial standing/base substitution), **five custom boundary perturbations** (leaf symlink, negative bound, post-qualified-head rollback, retirement marker and pure-data fitness attribute), and a **10-case A8 matrix** (clean, vetoed, revoked, superseded, withheld, validity premise, execution premise, standing premise, cited cycle, negative certificate). The negative-certificate case overlaps between the boundary probes and matrix: **14 distinct custom input variants**, not 15. The authentic-checkpoint foreign-responder replay is a separate additional qualification input, making **15** including that replay. Positive CLI/genesis controls and repeated realizations are not additional selected designs. The supplied eight seeded determinism histories and model seeds are separately reported suite workloads. Selection criteria were the named owner invariants and counterexamples, not score optimization; no held-out scientific data was reused. Earlier author exploration was not reconstructed as this reviewer's search history.
- **Tension search:** no consequential judgment relied on accepted scientific D1/D2 authority, so no D1/D2 tension-search result is claimed. Specialized lattice, matching, continuity and authority meanings were resolved at the named D3 owners.
- **Gaps:** private present-day stakeholder state; the three remote fallback checks; the remainder of the author's mutation list; full cache-tamper, authenticated-retirement, hostile-witness, crash/resource and later-phase qualification; and the deferred discriminators enumerated above. No gap is converted into PASS.

This different-family Review provides process independence from the Claude author, not automatic epistemic independence. It shares repository definitions, Python/Git/cryptography, many supplied fixtures, and transcribed Stage S expectations with the candidate's evidence. Distinct evidence routes were the actual signed throwaway ledger/CLI, outside-home sentinel, persisted high-water restoration, negative-certificate derivation and controlled mutations. No subagents were used. Prior review history and memory were routing/hypothesis aids; current verdicts were reconstructed against this exact candidate.

Nothing beyond the already authorized **shadow** scope is authorized. This record grants no Phase E dependent-work start, acceptance of A7/A8, G3 acceptance, campaign, cutover, native governance or publication authority. Those remain with their named stakeholder gates.
