# Independent Review — SSDS 8.0 Phase D, candidate 137b763

```text
GOVERNING SSDP: 7.2.1
PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
CANDIDATE: 137b7633945c1a52cc8a590a5fbf07402f57d982
PREVIOUS CANDIDATE: 517af4551e0b4ea000bd80fe47b1f1f9b4e0e562
BASELINE: e88d90dec4143340fffcf5cd53e7de5167d46be0
SCOPE: Phase D implementation and exit; dispositions of the 517af45 findings;
       repair siblings and inherited obligations; catalogue alignment;
       confirmation of unchanged A7/A8 technical verdicts
MANUAL BLOB: 6226f323365966bbcf653545f3a35b1fd7d6e060
PHASE D PLAN BLOB: ca0a97c210a343b0eb1fe41e3fb0b5236ea1ace6
G2 WORKPLAN BLOB: 523464de8ad6ec45379bad7e49660a471868cf49
CATALOGUE BLOB: f4c515bb1c3d7d5cdc3b762a18dcf2f67bbe5341
REVIEW METHOD: independent owner reconstruction; bounded Challenge Pass over
               repair delta and siblings; out-of-matrix consumer trajectories;
               real CLI, signed-ledger and derivation probes; mutations;
               prescribed suites and frozen-resource checks
REVIEWER: GPT family; engaged through Codex CLI in the stakeholder's own terminal
          at the stakeholder's request. The author's session typed only the
          pointer prompt and did not frame the candidate otherwise. This context
          did not author the candidate.
```

The named `PHASE-D-IMPLEMENTATION-REVIEW-HANDOFF-SSDS-8.0-137B763.md` governs this Review. The working branch was at `27abbc80feded27883bb23bd7cf1f578ea02e148`; its only delta from the candidate is that handoff. Execution used an archive of the exact candidate, with independent scratch Git metadata and read access to the original object store. All review scratch, temporary directories, homes and reviewer-generated keys are under `/tmp/ssds80-phase-d-review-137b763`. The stakeholder's private ledger, private keys and `~/.ssds` were not read or written. Existing untracked working-tree files were preserved. This record is the sole authored repository deliverable; no implementation change, commit or push was made.

Implementation and design roles were entered at the pinned public source, with their abstraction/concretization, specification, architecture, workflow, testing, definition, evidence, convergence and applicable PEM owners. Authority was reconstructed from the Manual, SD-56–SD-58 and the G2 register. Prior reports, memory, models, plan readings and author tests were hypotheses/evidence, not authority. The deeper attention went to write containment and qualified-current consumers; unchanged kernel behavior received affected regression and focused semantic checks. Later production qualification was not pulled into this phase.

## SERIOUS CHALLENGE

**None established.** The surviving defects violate coherent existing authority. SD-58 resolves the old SC-1 at its owner; the matched-content/evaluation-state split remains coherent. The implementation's provisional-successor allowance cannot relax the Manual's requirement that H* extend the evaluator's high-water mark. That is a D4 conformance finding below, not a reason to weaken the Manual or reopen A8.

## Verdict

**Phase D implementation and exit: NO-PASS. Neither the implementation nor the Phase D exit passes.** A-B3 remains incompletely repaired at the delegated Git write boundary. New A-B7 permits a current answer below a previously qualified head despite retaining that head's mark. All prescribed positive suites passed, but these executed counterexamples prevent closure and the start of Phase E's dependent work under G2 §5.1 item 5.

**A7 PASS confirmed. A8 PASS confirmed.** The Manual blob is byte-identical to the blob the `517af45` Review passed. The repair delta supplies no basis to withdraw either technical text verdict. Stakeholder acceptance of their text and G3 acceptance remain separate.

## Disposition of every 517af45 finding

| Finding | Disposition at 137b763 |
|---|---|
| **A-B3 retained — leaf workspace symlink** | **Named leaf escapes repaired; family still OPEN.** Workspace-file preflight, `_file` and `O_NOFOLLOW` refuse outside and inside leaf links, including preparation and report consumption, without changing the sentinel. The retained tests pass and fail under repair reversal. However, `Home` checks only the ledger repository's outer path; Git still follows internal directory symlinks and writes outside the home, including into a throwaway product repository. See A-B3 below. |
| **A-B5 — consumer never persisted its qualified head** | **Original omission closed.** The actual CLI presents head 1 and persists its exact position/digest; restoring both ledger and witness to 0 while keeping W=1 yields `ROLLBACK`, false currentness and exit 1. Removing the new update makes the retained test fail. This does not close the qualification family: A-B7 shows that keeping the chain at 1 while restoring only the witness permits H*=0 with W=1. The stronger presentation-order question is answered under NF5. |
| **A-B6 — INCOMPLETE as a bound** | **Closed.** `Assessments.bound` requires kind `COMPLETENESS` and outcome `COMPLETE` before consuming standing/premises. The negative-certificate test passes and fails when that guard is removed. Fresh positive/negative controls and the A8 matrix below retain veto, supersession, revocation, loss and cycle behavior. |
| **NF1 — pure attribute falsely rejected** | **Named false positive closed.** A derivation-local `Snapshot.read_raw: bytes` is accepted. The original direct import, module attribute, dotted module attribute and relative-import routes still produce F8. Restoring the prior checker makes its combined discriminator fail. A scoped-alias detection gap survives as NF4; no forbidden production reader was found. |
| **NF2 — stale catalogue explanations** | **Closed at the applicable semantic owner.** The R1 cell, signature/positive-certificate guard, construction rule, monotonicity/support edges, polarity explanation, stratification and class check agree with SD-58. No passage was found imposing evaluation-state membership/content currency on a bound after applying the explicit definition. Some short phrases still say “current completeness judgment”; they must be read through the amended `bound(o, K)`, not as a second definition. Phase F's cited-premise support-cycle admission check remains unexecuted. |
| **NF3 — retirement not passed to consumer** | **Marker-to-consumer wiring closed.** An existing `RETIREMENT` marker gives `RETIRED`, false currentness and exit 1 at the actual CLI. Removing `retired=retired` makes the retained test fail. Authentication/creation of a retirement statement is still later §24.2 work, not qualified by an arbitrary marker. |

The earlier `0e49deb` dispositions also remain differentiated: SC-1 is resolved by SD-58; B-B1's supersession-table correction is unchanged; A-B2's declared-witness filter/model validation and A-B4's missing-term refusal pass their retained real-owner tests. A-B1's original absence of qualification is repaired, but qualified-current behavior is still blocked by A-B7. N1's checkpoint checksum/authentication limitation and N3's home-ledger backup/requalification disclosure remain applicable; neither is upgraded into runtime qualification. N2's named Git-reader hole is detected, with NF4 limiting the sensor. These are incomplete findings in an unaccepted Phase D review cycle, not a claim of recurrence after accepted repair or new PEM occurrence counts.

## Blocking implementation findings

### A-B3 retained — The ledger directory can still redirect Git writes outside the home

**Owner text.** SD-56 requires everything written for an operator to live in the SSDS home outside repositories. Manual §26.3 says “Everything SSDS writes for an operator lives in one SSDS home outside every repository” and includes ledger repositories. G2 §5.1 item 2 protects governed refs/files in shadow. Phase D plan §9 promises containment of every resolved path before filesystem effects. These requirements apply to delegated subprocess effects as well as Python `open` calls.

**Actual owners.** `admission/genesis.py:Home.ledger_repository` validates only `ledgers/<id>.git`. `Home.check` enumerates workspace/key/high-water paths and the witness directory but never the paths Git will use inside that repository. `admit_genesis` then delegates to `ledger.append:create_ledger_repository`, `import_commits` and `append_entry`. Git follows an internal `objects` or `refs` directory symlink; Python's leaf `O_NOFOLLOW` does not constrain those writes.

**Executed traces, no path-replacement race.** On fresh throwaway fixtures, pre-create an empty bare ledger repository at the designated home path, with no ledger ref:

| Static path configuration before preparation | Actual outcome through prepare, reviewer signature, admit and derive |
|---|---|
| `home/ledgers/demo.git/objects` points to a directory outside that home, still inside review scratch | Preparation/admission succeed; imported and newly created Git objects appear outside the home; derive exits 0, `QUALIFIED`, current assertion true. |
| `home/ledgers/demo.git/refs` points to a scratch directory outside that home | Admission creates `ssds/ledger/demo` in the outside directory; derive exits 0 with currentness true. |
| `home/ledgers/demo.git/refs` points to the **throwaway product repository's `.git/refs`** | `Home.check("demo")` accepts it. Admission creates the product-side file `.git/refs/ssds/ledger/demo`, containing `37b14b4d155a7fd544d0ab3def30b17b434f05da`; the CLI then exits 0 with currentness true. The product ref was absent before the operation. |

The last case directly falsifies the shadow write boundary; no stakeholder repository was targeted. All fixtures and effects were confined to review scratch. The existing positive boundary test compares refs/objects/status only in a ledger layout without these links, so it remains green.

**Consequence.** Constraining the outer ledger directory does not constrain its actual storage or ref updates. The repaired leaf tests are useful but insufficient to close A-B3's governing invariant.

**Minimum repair.** Re-derive containment at the existing Admission/ledger write boundary, including Git's effective repository/storage/ref paths, before preparation offers a proposal or admission performs effects. A simple admissible policy may refuse unsafe pre-existing ledger layouts rather than enumerate a growing list of files. Preserve the chosen home and normal positive genesis path; do not treat subprocess writes as an exception or add a parallel path registry. Evaluate equivalent redirection mechanisms at that owner; this Review does not prescribe a new durable architecture or a complete hostile-filesystem implementation.

**Required discriminator.** Keep the repaired workspace-file and directory controls, and add real prepare/sign/admit refusal tests with ledger `objects` and `refs` symlinks, including `refs` aimed at a throwaway product `.git/refs`. Refuse before outside writes; product refs, object inventory and status and the outside directory must remain unchanged. A clean ledger-home control must still admit and derive. This static counterexample already blocks without deciding a concurrent filesystem-race threat model.

### A-B7 — A qualified answer may precede the evaluator's retained high-water mark

**Owner text.** Manual §23.1: a current-qualified head extends “every checkpoint and high-water mark the evaluator observes.” Manual/catalogue §23.4 requires H* to be held by q_a witnesses **and extend W**. The single provisional successor is not presented as current. G2 §4.2 accepts §23; the new A-B5 persistence repair is useful only if its consumer respects the retained mark.

**Actual owner.** `ledger/qualification.py:qualify` adds W to `marks`, then selects candidates with `p >= floor - 1` and `p >= m or m == p + 1`. This grants the one-position allowance to W as well as witness checkpoints. The report consumer accepts the resulting `Qualification.current` and derives the selected older prefix.

**Executed trace through real signed entries, file witness and CLI.**

1. Prepare/sign/admit genesis at 0. Append a valid signed successor at 1 with the supported ruleset/analyzer and checkpoint it.
2. Run actual `derive`: exit **0**, `qualified_head=1`, `current_assertion=true`; persisted W is the exact digest of head 1.
3. Remove only the position-1 checkpoint from the throwaway witness, retaining its position-0 checkpoint. **Keep the ledger chain through 1 and keep W=1.** No abandonment/retirement record is introduced.
4. Run actual `derive`: exit **0**, `qualification=QUALIFIED`, `qualified_head=0`, derived `position=0`, `provisional=1`, `current_assertion=true`. W still says 1.

The retained A-B5 test instead restores the ledger itself to 0, which triggers the earlier `W.position > top` branch. That test does not reach this candidate-selection defect. W=1 establishes that 1 was previously qualified, so relabelling it provisional cannot justify presenting 0 as current. The probe tests the explicit W guard under stale witness state; it does not claim tolerance of arbitrary failures beyond the deployment class's declared assumptions.

**Minimum repair.** Enforce the Manual's head-extension requirement in the existing qualifier. At minimum, no selected current H* may precede an unabandoned W. If no witnessed head satisfies that condition, withhold currentness (normally `UNQUALIFIED` here, rather than claiming replica rollback while its chain still contains 1). Reconcile the checkpoint/provisional reading in plan §6 and its test oracle against §23.4: allowing a provisional successor in A does not grant an exception for W or automatically waive the stated observed-checkpoint extension condition. Preserve authenticated abandonment semantics and the genuine never-qualified provisional-successor control; do not solve this by deleting/lowering W or adding a second currency mechanism.

**Required discriminator.** Retain the actual CLI sequence above beside the existing restore-both test. With chain=1, W=1 and witnesses confirmable only through 0, require no current assertion, a nonzero exit, and an unchanged W. Pair it with a never-checkpointed/never-qualified successor that legitimately leaves current H*=0, and with restoration of the authentic checkpoint at 1. Assert directly that every successful qualified head extends every applicable retained W.

## Non-blocking findings and bounded answers

**NF4 — F8's flat alias map misses an ordinary scoped import.** The following synthetic derivation module receives **no fitness violation**:

```python
import ssds.content as c

def f(repo):
    return c.read_tree(repo, "HEAD")

def g():
    import collections as c
    return c.Counter()
```

`fitness._git_readers` builds one map from every import found by `ast.walk`; the function-local `collections as c` overwrites the module-level binding even though it does not change `f`'s global `c`. The pure-attribute control is now clean and all five named direct/module/dotted/relative variants are detected. This is a sensor hole, not a discovered production Git read. Narrowly reconcile alias scope at the checker if strengthening this sensor; it remains bounded static evidence, as Manual §26.2 says. Do not restore the pure-attribute false positive.

**NF5 — The mark is stored before successful presentation.** A signed, witnessed successor at 1 adopting an unavailable analyzer qualifies, then derivation withholds the assertion. The CLI exits **1**, `current_assertion=false`, reason `missing analyzers: missing.analyzer/1`, but W has already advanced to 1 in `qualified_chain`, before `consequences` or report writing. Therefore the handoff's stronger “never records a head not presented current” property is **not established and is false in this probe**. This is conservative remembered qualification, not a false-current route: Manual §23.4 calls W the last head *qualified*, so this alone is not a blocker or an upstream contradiction. If presentation-only advancement is intended as a stricter D4 contract, make that sequencing explicit and test both withheld derivation and failed report output. Sequential successful reads did not lower W; simultaneous-reader monotonicity/crash durability was not qualified here.

**Catalogue alignment.** The explicit `bound(o, K)` now requires a positive `COMPLETENESS/COMPLETE` certificate; standing is separate from its target's evaluation-state currency; membership/content are read on K and other premises in the evaluation state. §5.6 item 4 retains subject-to-certificate and cited-record support edges. The stratification rule, R1 cell, §6.5 construction rule, §6.6 polarity and §6.8 class rule refer consistently to that decision. Remaining shorthand “current completeness” in §6.6/qualification examples does not explicitly restore the old evaluation-state content test and is resolved by §6.5/SD-58. No new conflicting applicable bounding definition was found. Prose alignment was checked semantically; no keyword/prose-quality parser or exact-word test was invented.

## Required inherited judgments

### The eleven 0e49deb handoff §3 questions

| Question | Judgment at this candidate |
|---|---|
| **1. Scope and owners** | Content/analyzers consume supplied trees; ledger owns storage/authentication/qualification; derivation owns S0–S3; Admission owns genesis writes; Interface/Dispatcher remain later work. The inspected delta stays at those owners. Containment and currentness still fail as above. |
| **2. Plan readings** | All sixteen are disposed below; SD-58 supplies reading 1's owning decision. Plan §6's qualification reconciliation cannot extend its allowance to a previously qualified W. |
| **3. Fail-closed deferrals** | NATIVE D1/D2 passing acceptance/gates remain unavailable until revision runs; plan reach is conservative; unavailable declarative verdicts fail closed. Item-dependent S3 is Phase E, general admissibility/custody Phase F. No later owner excuses the current containment or qualification defects. |
| **4. Expected values/discriminators** | Expectations in the affected tests are literal register/Stage S outcomes; F13 passes, and no model import into production/test execution was found. Eight main mutations discriminate named repairs or retained A8 semantics; limits/errors are recorded below. Later-phase cases remain unexecuted. Qualification's current test oracle carries the plan's relaxed checkpoint reading and does not test W=1/H*=0. |
| **5. Fitness** | Real-tree and synthetic F0–F13/B1 tests pass. Named reader routes remain detected; pure attribute accepted. NF4 supplies a fresh missed dependency. These are sensors, not proof of purity or subprocess-effect containment. |
| **6. Determinism/replay** | Generated-ledger, within-entry permutation, historical-prefix, checkpoint resume and incremental/from-scratch tests pass, including the supplied eight seeded F/P/T histories. Cache-key/body corruption checks pass; an unkeyed checksum still does not authenticate a coherently rewritten private cache. |
| **7. Ledger/qualification** | Signature/key/prev/Git-chain, schema halt versus unsupported version, CAS, referenced-parent retention and exclusive fsynced witness checks pass. Declared identities/model validation remain enforced. A-B7 violates the selected-head contract despite the repaired mark update. Retirement marker consumption now works; authenticated retirement remains later work. |
| **8. Shadow boundary** | Clean positive genesis compares product refs, objects and status and uses only shadow modes. A-B3 directly breaks that boundary through a pre-existing internal ledger symlink. B1's argv sensor cannot establish filesystem containment. |
| **9. Core preservation** | 393 tests pass across 13 modules, including fresh wheel/sdist installed-product tests and frozen profiles. All 22 frozen profile/prompt resources are R100 renames. `source/`, `dist/` and Architecture 1.6.0 are byte-unchanged from baseline. No exhaustive old/new differential run over every configuration is claimed. |
| **10. First release** | Fresh install succeeds. Installed help/doctor, absolute home override, no-write doctor/first-write and program-composition tests pass. Python 3.11+ is enforced/documented. No predecessor detection/migration/alias was introduced by this delta. Unsafe pre-existing ledger layout remains A-B3. |
| **11. Step 7** | The manifest and evidence describe Case B section-level parts at legacy accepted scope, with protocol/Manual LEGACY and program UNGOVERNED, without rewriting product content. The stakeholder's public evidence binds the old baseline/digest/signature fingerprint and reports. A fresh candidate-history prepare/sign/admit/derive succeeds below. The historical human gate is not retaken by the reviewer and private present-day state is not authenticated here. The positive run cannot close the implementation blockers, so the Phase D exit fails. |

### Every Phase D plan §8 reading

| Reading | Disposition |
|---|---|
| **1. Bound currency** | Accepted decision SD-58; positive certificate guard now correct. Fresh genuine-fix/revert, adverse/veto/revocation/supersession/loss and cited-cycle checks agree with it. |
| **2. Policy schema** | Closed data-only domain tables; no executable policy language or new policy-value authority. |
| **3. Default mode** | Explicit `"*"` default; shadow selects UNGOVERNED. No mode is inferred from absence. |
| **4. Admission body** | Integration/adopted-delta facts feed S0; general admission enforcement remains Phase F. |
| **5. Judgment domain** | Follows judged content, including transformation changes, rather than target representation. |
| **6. Assessment home** | Conservative file-overlap successor widening; exact arbitrary region/move tracking is not claimed. |
| **7. Execution basis** | Closed recorded execution basis is consumed; truth of runner/custody declarations is a separate Phase F boundary. |
| **8. Forced components** | All forced support nodes remain F. Assessment/completeness cycles yield ordinary findings; other support cycles integrity obligations. Fresh cited-cycle case forces a component and prevents the stop. |
| **9. Requalification** | Retained-current/withheld/fresh-record behavior passes retained derivation tests; full item workflow routing remains deferred. |
| **10. Views** | Historical/frame/halt/unsupported-version/missing-analyzer withholding passes tests. The external currentness consumer still fails A-B7. |
| **11. Checkpoints** | S0 cache plus recomputed S1–S3 passes replay/resume; checksum is not authentication. Caller persistence/cadence belongs to Phase E; hostile cache qualification remains Phase H. |
| **12. Home layout** | Delegated layout is acceptable, but its physical containment is incomplete at Git internals (A-B3). |
| **13. Tree injection** | Caller reads content; Admission uses the public baseline derivation boundary. Ownership direction is preserved. |
| **14. Genesis refusal** | Missing file/heading/symbol/anchor terms refused; empty file/prefix accepted; policy/mode/manifest/trust-root checks retained. Does not establish safe physical ledger layout. |
| **15. Human gate** | Whole proposal digest and registered-key SSHSIG verification retained; altered proposal/signature tests pass. Reviewer used only generated throwaway keys. |
| **16. Admission** | Positive genesis gets durable checkpoint, read-back qualification and W=0. Subsequent currentness is separately subject to A-B7; retirement authentication is not completed by the marker test. |

### 517af45 handoff §3(A) and the present handoff §3

The previous-finding dispositions above cover §3(A).1. For §3(A).2, H* prefix selection and historical/unqualified labels pass the supplied tests, declared witnesses are enforced, missing-term/empty-prefix controls pass, and the pure-attribute regression is repaired; A-B3/A-B7 limit containment/currentness. For §3(A).3, A8's standing/context split and positive support dependencies were inspected and exercised; the new COMPLETE guard introduces no surviving permissive bypass in the bounded variants. For §3(A).4, the inherited eleven-question table and step-7 judgment above apply.

For the present handoff: all six `517af45` findings are individually disposed; repair siblings include downstream Git writes, witness-only restore, unavailable-analyzer presentation, scoped imports and the A8 matrix; catalogue passages and immutable Manual identity were checked; inherited implementation/exit duties remain subject to the two blockers. Nothing in this delta changes the basis of the A7 one-program/table/default-home verdict or A8's bounded decision. Their sibling/invariant/cost conclusions stand: no predecessor migration under SD-57; home custody/backup and fail-closed matching/reassessment costs remain disclosed. A7's correct text does not excuse A-B3's implementation behavior.

### Later discriminators remain unexecuted

Phase E retains the D1/D2 revision-run variants of 575dc78 N5, f7419d5 N4 and f22b4dc N5; 63ddf91 N5's plan-amendment/tightening half; f03b15e N5's reassessment of an answered non-gate obligation; and item-dependent readiness/discharge/drift/impact/conformance/brief/routing and re-application views. Phase F retains 51070e5 N3's adjudication-independence refusal, f03b15e N5's supersession-authority refusal, other §8.3 steps 3/7 admission cases, the cited-premise cycle check, RR-11 resolver/Dispatcher behavior, and runner materialization/custody. Migration/cutover, authenticated retirement, hostile transport, crash/resource/security qualification and general Admission are not passed by this Review. These deferrals do not defer the concrete Phase D violations above.

## Verification and evidence limits

Execution used **Python 3.11.15** in an isolated environment. Initial sandbox installation failed on DNS; an offline attempt lacked a compatible dependency wheel. After dependency access was available, installation and every prescribed command completed. Fresh-install Core acceptance used scratch-cached dependencies, not replacements for its package/build owner. These setup failures were not counted as candidate defects or passes.

| Check at exact candidate | Result |
|---|---|
| `python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt` | PASS |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | PASS: **212 tests** |
| `python orchestrator/scripts/run_core_tests.py` | PASS: **393 tests**, 13 modules, including wheel/sdist installed-product acceptance |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | PASS |
| `python -m unittest discover -s tests -v` | PASS: **435 tests, 3 skips** |
| `python3 -I qualification/ssds80/models/run_models.py --seeds` | PASS: seeds; zero settled S1/S2/S3/S5 misses, 14,508 bounded settled answer chains without violations; refuted readings remain detected |
| `git diff --check e88d90de 137b7633` | PASS |
| `source/`, `dist/`, `orchestrator/docs/architecture.md` versus e88d90de | Zero changed paths; byte-identical |
| Frozen profiles/prompts/snapshots | **22 R100 renames**, identical blob contents; snapshot check passes |
| PEM validator | PASS: schema 1, 5 families, 0 notices |
| Canonical package build, independent validation, committed parity | PASS; fresh output under review scratch |
| Fresh repository-history prepare/sign/admit/derive | PASS at candidate baseline; QUALIFIED H*=0, current assertion true, zero findings/obligations, only `refs/ssds/ledger/ssdp-shadow` in its clean ledger |

The three skips are unchanged opt-in remote fallback realizations for Protocol 6.2/6.3/6.4. They are not passed; no fallback identity changed in this delta. Structural/model/package success establishes bounded consistency, not architecture adequacy, G3 acceptance or protection from the executed bypasses.

The reviewer-controlled history run signed genesis digest `sha256:7703acadfc8fddf5b578368974294c65b84e633e79c40dd34a99b0ce466e5a70`; its entry digest was `sha256:f09cec0728194b32fff61dd1161e2e9bd37e344235800828a126bb7c18e783f7`, commit `8844e72cb725fa03a2e4adb8ba5eac59acbe6403`. It reproduced the path on candidate content; it was engineering evidence, not a stakeholder acceptance or a second operator gate.

### Mutation discrimination

Every main mutant had a passing unmutated focused base. Tests executed real candidate owners in scratch copies:

| Wrong variant | Retained test | Result |
|---|---|---|
| Revert preparation's leaf-file repair to 517af45 | `Refusals.test_a_symbolic_link_at_a_file_never_carries_a_write_out_of_the_home` | **3 assertion failures plus 1 fixture cleanup error**; each outside-link subtest first fails because preparation accepts it. The later inside-link setup encounters the leftover `report.json`. Not claimed an error-free mutation result. |
| Revert report/leaf writer repair | `ShadowGenesisScript.test_the_report_is_never_written_through_a_link` | 1 failure, 0 errors |
| Remove high-water update | `ShadowGenesisScript.test_the_consumer_keeps_the_last_head_it_qualified` | 1 failure, 0 errors |
| Permit an adverse completeness certificate | `BoundingCurrency.test_an_incomplete_judgment_never_bounds` | 1 failure, 0 errors |
| Restore overbroad attribute checker | `DependencyRuleDiscriminatorTests.test_derivation_reaches_no_git_reader_through_a_permitted_facade` | 1 failure, 0 errors |
| Ignore witness retirement | `ShadowGenesisScript.test_a_retired_witness_lineage_presents_nothing_current` | 1 failure, 0 errors |
| Evaluate bound content entries on evaluation content | `Staleness.test_genuine_fix_is_stale` | 1 failure, 0 errors |
| Ignore cited-record currency | `BoundingCurrency.test_a_cited_record_premise_holds_in_the_state_of_evaluation` | 1 failure, 0 errors |

Two further exploratory leaf variants were attempted while separating preflight, per-file containment and no-follow opening: one produced four containment errors, the other the same three assertion failures and one cleanup error as above. They add no independent successful discrimination claim. NF2 is prose/semantic alignment and has no invented executable prose oracle. The rest of the author's original mutation inventory was not independently rerun.

The ten-case A8 matrix was re-executed against this candidate through production derivation, using the prior review's inspectable probe as a fixture recipe: clean and standing-premise controls bound and make the genuine fix stale; vetoed, revoked, superseded, loss-withheld, validity-premise, execution-premise, cited-cycle and INCOMPLETE variants do not. Every certificate in the matrix has zero record-syntax violations. The cited-cycle variant forces one support component. Thus the new positive-certificate guard preserves the tested support/clamp behavior; this is not exhaustive Admission qualification.

The out-of-matrix pass reconstructed physical write containment and P4's selected-head invariant without relying on the author's test decomposition. It followed the actual Git subprocess effect boundary and distinguished W from an unqualified provisional entry, finding A-B3 and A-B7. It also tested scope-sensitive import detection and qualification-before-presentation. Further enumeration of hostile layouts, races or later-phase campaigns could not convert these counterexamples into Phase D PASS and was not undertaken.

Scratch evidence: `ssds.log`, `core.log`, `repository.log`, `models.log`, `snapshot.log`, `pem.log`, `build.log`, `validate.log`, `parity.log`, `probes.py`/`probes.log`, `product_ref_probe.py`/`product-ref-probe.log`, `a8_probes.py`/`a8-probes.log`, `mutations.py`/`mutations.log`, leaf-variant logs and `history_genesis.py`/`history-genesis.log`, all under the stated scratch root. Decision-sufficient traces and results are retained here so the verdict does not require temporary-file retention.

## Project Engineering Memory applicability

The workplan binds accepted/base memory to `main` at `af0455753e20ee54a969c844872e29e270007211`, PEM blob `1561797125622f355f84eb27319f87e8fa4227d9`. The independently resolved local `main` matches that state; candidate PEM has the same blob, hence no additional overlay. Schema/publication metadata and canonical metadata for all five families were inspected, including summary-omitted/UNASSESSED material. Coverage is PARTIAL and is not evidence of historical absence. PC-001's frozen-behavior force is independently supplied by SD-56, Manual §26 and G2, not its salience or memory placement.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: Current owners require frozen bytes and version-bound Core behavior; rename-only resources and actual Core acceptance test their preservation.
  - id: DS-001
    disposition: APPLICABLE
    reason: Green supplied matrices do not exercise every physical write or qualified-current consumer; independent real-owner probes materially change closure.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No canonical-source routing repair or generated-route change.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No protocol-successor fallback publication.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: Its immutable fallback-publication mechanism is not this genesis or qualification consumer.
```

No memory update, repair acceptance or lifecycle closeout was performed. The two containment layouts are sibling manifestations of one incomplete boundary, not separate accepted-repair recurrences. Repair should reason at that shared boundary rather than grow another file-specific exception list.

## Scientific checks and common-mode note

- **Material findings:** A-B3 and A-B7 block implementation/exit; NF4 and NF5 bound the sensor and consumer sequencing claims. A-B6/NF1/NF2/NF3 named repairs pass within the stated scope. No scientific-result finding or new upstream SERIOUS CHALLENGE was established.
- **Realized scientific results:** none produced, run or reviewed. This was engineering evidence over synthetic histories, source text, public historical genesis evidence and reviewer-generated throwaway signed ledgers; no physical experiment, scientific dataset, trained model or scientific-result population was evaluated.
- **Variants:** **10 distinct code perturbations** (eight main mutations and two exploratory leaf variants); **10 A8 input cases**; **7 fitness inputs** (pure attribute, scoped alias, direct import, module attribute, dotted attribute, relative import, relative attribute); **5 additional custom boundary perturbations** (outside objects, outside refs, product refs, witness-only restore and unavailable-analyzer presentation). That is **22 custom boundary/fitness/A8 input variants**, plus 10 code perturbations. Positive head-1 controls and clean history genesis are controls, not additional selected designs. Supplied seeded suites and retained test subcases are separately accounted for above. Criteria were the named owner invariants and cheap sibling discriminators; no scientific model/parameter survivor was selected, and prior author exploration was not reconstructed as this reviewer's search history.
- **Tension search:** no consequential judgment relied on accepted scientific D1/D2 authority; no D1/D2 tension-search result is claimed. The specialized lattice, support, matching, content and currentness meanings were resolved at D3 owners.
- **Gaps:** private present-day operator state and gate custody; the three opt-in remote fallbacks; unrerun original mutations; authenticated retirement; simultaneous-reader monotonicity, hostile filesystem/cache/transport and crash/resource qualification; and the named later-phase discriminators. None is converted into PASS.

This is a different-family review from the Claude author, with process independence, not automatic epistemic independence. Repository definitions, Python/Git/cryptography, transcribed Stage S expectations and many supplied fixtures are common dependencies; the A8 matrix recipe also comes from the prior GPT review. Distinct evidence routes here were signed real-CLI trajectories, physical Git writes into throwaway outside/product paths, retained-mark/witness restoration, a scoped-import counterexample and controlled owner mutations. No subagents were used. Memory and prior reports guided hypotheses; exact candidate behavior and current owners determine the verdict.

Nothing beyond the already authorized **shadow** scope is authorized. This NO-PASS grants no Phase E dependent-work start, A7/A8 stakeholder acceptance, G3 acceptance, campaign spend, publication, native governance or cutover authority. The named stakeholder gates remain controlling.
