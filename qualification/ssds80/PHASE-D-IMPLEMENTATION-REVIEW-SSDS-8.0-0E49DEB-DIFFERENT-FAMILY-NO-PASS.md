# Independent Review — SSDS 8.0 Phase D and Manual amendment A7

```text
GOVERNING SSDP: 7.2.1
PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
CANDIDATE: 0e49debe63346e72db69ed8e30c14f5bbd58a083
BASELINE: e88d90dec4143340fffcf5cd53e7de5167d46be0
SCOPE: (A) Phase D implementation and exit, including step 7; (B) Manual A7
MANUAL BLOB: b3a097d32f2757bc1df9a2b19fb0bce87e11dd8d
PHASE D PLAN BLOB: 4c8017d97a087c6ff9d5743a7a7e1742e566c168
G2 WORKPLAN BLOB: 4b188a171ffb9fa6bcb7f1436c36178c428f6950
CATALOGUE BLOB: 31d7a8a3477a9a0c127786f75b698959bc313cd4
REVIEW METHOD: independent reconstruction, bounded Challenge Pass, real-owner
               failure probes, mutation spot-checks, prescribed acceptance checks
REVIEWER: GPT family; engaged through Codex CLI in the stakeholder's own terminal
          at the stakeholder's request. The author's session supplied only the
          pointer prompt and did not frame the candidate otherwise. This context
          did not author the candidate.
```

The named `PHASE-D-IMPLEMENTATION-REVIEW-HANDOFF-SSDS-8.0-0E49DEB.md` governs this Review. The branch tip was `094a87d17d064a6db4acfebbfbe60e9884c9d57e`; neither its newer implementation nor its conclusions substitute for the candidate. Inspection and execution used the pinned archive, subsequently given a separate scratch Git checkout at the candidate. All review-generated execution state is under `/tmp/ssds80-phase-d-review-0e49deb`; no stakeholder private key or private ledger was read. The only authored repository deliverable is this record. No commit or push was performed.

## SERIOUS CHALLENGE

### SC-1 — The settled bounding rule and the accepted genuine-fix case disagree

**Earliest owner:** G2 workplan §4.2, the ACCEPT dispositions for catalogue §6.5 and §6.6, under Manual §6.5–§6.6. Return to Stage S under G2 §5.6; reopen G1 if resolving the meaning requires changing the Manual's architecture. Phase D plan §8 reading 1 is a proposed semantic resolution, not an already-authorized D4 choice.

**Owner text and counterexample.** Catalogue §6.5 defines `bound(o)` using every bounding completeness judgment's currency at `T` **in the frame of evaluation**. Manual §6.5 requires current bounding completeness judgments, and §6.6 requires a permissively matching reproduction on the failing content. The register also ACCEPTs S5 §6 `genuine_fix_is_stale`.

Take a failure on code revision `r0`, an identical second execution on `r0`, and a successful execution on a genuine fix `r1`. The old executions' bounding completeness judgment has `content(code,r0)` in its basis. In the `r1` frame that judgment is non-current. Under the settled literal rule neither old execution can supply condition (1), although the new completeness judgment bounds the execution on `r1`. The genuine-fix case therefore remains non-stale.

The implementation instead checks the bounding judgment's base standing and its content entries against the observation's **matched content K**, rather than requiring its full currency in the evaluation frame (`derivation/assessment.py:bound`). This changes the predicate's evaluation context. It is consequential: the candidate returns `True` for staleness; a mutation implementing the literal rule for these content-only completeness judgments returns `False`, and `Staleness.test_genuine_fix_is_stale` fails. The literal rule was evaluated without recursively invoking the entire support solver.

**Consequence.** A green test establishes that the candidate implements the plan's replacement reading, not that the settled register already authorized that reading. The scope of the bounding judgment's non-content premises also needs an owner decision: `base(c)` plus selected content entries is not generally full `current(c)`.

**Minimum resolution and discriminator.** Reconcile §6.5 and §6.6 at their real owner, explicitly binding which content/frame each premise is evaluated in; update the Stage S case and register disposition and obtain the required Review before dependent implementation is closed. Retain the `r0` reproduction/`r1` fix/revert discriminator, plus loss of bounding completeness through challenge, changed membership, and a non-content premise. Preserve the challenged accepted text as the baseline until resolved. This Review does not choose the new rule.

## Verdict

| Subject | Verdict | Meaning |
|---|---|---|
| (A) Phase D implementation and exit | **NO-PASS** | Neither the implementation nor the Phase D exit passes. SC-1 and A-B1–A-B4 remain open. Phase E's dependent work cannot start on this record. |
| (B) Manual amendment A7 | **NO-PASS** | The central rename/home/first-release text follows SD-56/SD-57, but its current supersession table still asserts the displaced composition and distribution arrangement (B-B1). |

The prescribed positive suites pass. Their results do not close these counterexamples. The recorded stakeholder genesis is evidence of a historical shadow run, not acceptance of A7, G3 acceptance, or native authority.

## Blocking implementation findings

### A-B1 — The step 7 consumer asserts currentness without qualification

**Owners:** Manual §0.4 P4, §5.1, §21.6 and §23.4; G2 §5.1 item 4. Section 5.1 places the choice of current prefix outside pure derivation. Section 23.4 requires a named qualified head for every current-state answer; an unqualified replica supplies historical views only.

**Actual path:** `orchestrator/scripts/shadow_genesis.py:derivation_report` calls `read_chain`, then `consequences` over the entire readable chain, and publishes `view.current_assertion`. It never calls qualification, reads witnesses or the high-water mark, or selects `H*`. `derive` prints that assertion and returns success. Authentication and absence of derivation findings do not qualify a prefix. The fact that `admit_genesis` qualified once does not qualify a later read.

**Executed discriminator:** after a real signed throwaway genesis qualified at position 0, temporarily remove its witness checkpoint. The real qualification owner reports `UNQUALIFIED`; the real `shadow_genesis.py derive` still exits 0 and prints `current assertion: True`. Restore the checkpoint and advance the stored high-water mark beyond the retained chain: qualification reports `ROLLBACK`; the same CLI again asserts currentness and exits 0. These probes changed actual scratch witness/operator state, not just a mock qualification result. State was restored afterward.

**Minimum repair:** make the report consumer qualify with the declared witnesses and high-water mark, derive the selected qualified prefix, and expose qualification, `H*`, provisional suffix and withheld/historical status. Keep witness reads outside derivation. Exercise this actual CLI/report path for missing witnesses, rollback and a provisional successor; none may be represented as a current full head. This is coherent-parent D4 repair, not a reason to defer the existing report's truthfulness to Phase E.

### A-B2 — Qualification counts an undeclared responder as a witness

**Owners:** Manual/catalogue §23.3–§23.4; G2 §4.2's §23 ACCEPT row. Quorums refer to the **declared witness set**, not arbitrary mapping keys. A signed checkpoint authenticates its Admission origin; it does not make every alleged holder a configured witness.

**Actual path:** `ledger/qualification.py:qualify` constructs `responders` from every non-null entry of `reports` and counts those keys for both `r` and `q_a`. It does not restrict them to `model.witnesses`.

**Executed discriminator:** use the real genesis chain and its authentic checkpoint, with the valid `LOCAL_TRUST` model declaring only `local-file`. Supply `{"not-declared": [checkpoint]}` and omit `local-file`. The result is `QUALIFIED` at head 0. The declared witness has supplied no response. In a larger model, relabelled copies can likewise inflate distinct-holder counts.

**Minimum repair:** establish distinct configured responder identities before counting either quorum, reject or disregard foreign identities, and validate witness-set cardinality/uniqueness at the appropriate boundary. Keep authentic-checkpoint validation as a separate requirement. Add this missing-configured/foreign-responder case at `qualify`, then carry it through the future witness consumer; it must yield no current-qualified head. This finding does not assert a presently implemented hostile network transport.

### A-B3 — A rejected ledger ID writes outside the SSDS home

**Owners:** SD-56/SD-57; Manual §25.4 and A7 §26.3; G2 §5.1 item 2; Phase D plan §8 readings 12 and 14. Operator writes must remain in the SSDS home, and input paths must be validated before they can direct writes.

**Actual path:** `admission/genesis.py:Home` joins the unchecked ledger ID into workspace, key, ledger and state paths. `prepare_genesis` computes and uses those paths before the ledger-ID grammar is checked by `record_violations`. Even after validation fails, it unconditionally writes the validation report to the unchecked workspace. The script's `--ledger-id` accepts the raw string.

**Executed discriminator:** invoke the real `prepare_genesis` on otherwise valid candidate content, with a scratch home and ledger ID `../../escaped`. Preparation correctly returns invalid, but creates `report.json` at a resolved path outside that home. The witness and key preparation can also precede the eventual grammar refusal. Every path used by this probe remained inside the review scratch directory.

**Minimum repair:** validate the ledger ID before any path construction or filesystem effect, and enforce resolved containment for operator paths, including the symlink policy. Refuse invalid IDs without creating or overwriting anything outside the home. Test the public CLI as well as the owner with traversal, absolute IDs and a symlink escape. The positive product-ref/object/status snapshots do not discriminate this failure path. No write to the stakeholder's governed files was attempted by this Review.

### A-B4 — Genesis accepts a newly declared file scope that resolves to nothing

**Owners:** Manual §1.9 and §19.9; catalogue §1.9, accepted by G2 §4.2; Phase D steps 2 and 6. Section 1.9 requires newly declared or changed file/span terms to resolve at admission. Section 19.9 requires validation of every declaration/static check before the human gate.

**Actual path:** `derivation/baseline.py:baseline_structure` checks `static_errors(Structure(...))` but does not enforce presence of newly declared file/span terms against the baseline tree. `prepare_genesis` accepts that result. Pure grammar checks cannot establish that the named file exists.

**Executed discriminator:** a real fixture repository contains a manifest declaring subject `docs`, kind D3, scope `[{path="missing.md"}]`, with no such file. Real preparation returns `valid=True`, no problems, no findings, and a digest ready for signature. The failure occurs before the human gate and needs no invalid signature or forged chain.

**Minimum repair:** apply the tree-dependent newly-declared-term check to genesis, through the owning baseline validation path. Cover missing file, missing heading/symbol/anchor and a legitimate empty file. Keep the distinct rules intact: a later disappearance can resolve to `ABSENT`, and a `prefix` declaration is exempt from the presence check. A typo at first declaration must not reach the gate as a valid genesis.

## Blocking A7 finding

### B-B1 — The supersession table still describes SSDS as an extra Core extension/distribution

**Owners:** SD-56, decision record item 52; proposed A7 §26.3–§26.4; handoff §4 items 1–3.

A7 §26.3 replaces two distributions and a Core extension with one distribution and a root module outside Core. Yet §26.4's current frozen-surface table retains:

- the §3 row saying SSDS is **one additional distribution**, citing §26.3;
- the §6 row saying the Core composition SPI is preserved and **SSDS registers through it**.

These are current final-disposition assertions, not quoted historical alternatives. They contradict the adjacent amended packaging/composition rows and the stakeholder's one-program decision. A newcomer following the table would reconstruct a different assembly from `ssds.cli`.

**Minimum repair:** rewrite these two dispositions around the single distribution/root and reserve `ssds.extensions.v1` for other extensions. Review all §26.4 sibling rows after that edit. The discriminator is a reconstruction from the table alone: it must produce the same distribution count, root and extension relationship as §26.3 and SD-56. This is repair to the unaccepted A7 text; it does not challenge the stakeholder's rename decision.

## Non-blocking findings and bounded uncertainties

**N1 — A checkpoint checksum does not authenticate its cached fold.** `History._resume` recomputes the ledger-derived key and an unkeyed body digest, then trusts cached heads/structure/modes and the selected record subset. In an exploratory probe, a checkpoint after an absorption was edited to retain the old accepted head and its body digest recomputed; the same ledger/key was accepted and `valid(impl)` changed from `F` to `T`. The required generated-checkpoint replay tests and ordinary-corruption refusal pass. This stronger perturbation requires coherent alteration of private derived state; applicability to the declared operator-state threat boundary remains a Phase H security question, not an independently established hostile-access path here. Do not describe key/checksum verification as proof that arbitrary cache contents equal the canonical fold. On doubt, discard and rebuild (§21.6); qualify the private-cache trust boundary explicitly.

**N2 — A concrete dependency the fitness sensor misses.** In its clean synthetic tree, replacing derivation's package body with `from ssds.content import read_tree` and a function calling `read_tree(repo, "HEAD")` produces **no fitness violation**. The permitted content facade exposes a live Git reader, so the import allowlist alone cannot prove derivation purity. No such production call was found in the inspected derivation path: trees are supplied by the caller. This is a sensor limitation, not evidence that production currently reads Git. Keep real-owner purity review; narrow a public surface or strengthen the sensor only if justified by the owning contract.

**N3 — Default ledger placement has an operational consequence.** A product clone alone does not carry its default home-resident governance ledger, witness state or high-water marks. §21.5 declares the replica and §23 covers loss/qualification; §32.2 already discloses loss of all retained copies and checkpoints. A short first-day backup/restore explanation would make the new default easier to operate. No predecessor migration or alias is warranted under SD-57. This is not an additional acceptance blocker.

## Judgments requested by handoff §3 — implementation

| # | Judgment |
|---|---|
| 1. Scope and owners | The inspected package follows the seven owners and the read-only Phase D placement. Content resolves representations; derivation consumes supplied trees; Admission uses baseline derivation rather than importing content; ledger append is imported by Admission. Dispatcher/interface remain empty. SC-1 prevents treating every implemented semantic as already covered by the settled register. No separate implementation of the Stage S models was used as an oracle. |
| 2. Sixteen readings | Dispositions are below. Reading 1 requires upstream resolution; reading 14 is incompletely realized. Readings 12–16 do not excuse A-B1/A-B3/A-B4. |
| 3. Fail-closed deferrals | Native D1/D2 passing acceptance/gates are explicitly refused by `State.tgt` pending revision runs. Plan-acceptance reach is deliberately widened pending plan semantics. The inspected assessment path treats unavailable cross-reading verdicts as yielding failure; declarative evaluation remains unqualified for Phase E. Item-obligation S3 views belong to Phase E, and non-genesis Admission/admissibility to Phase F. No deferred discriminator is counted as executed by this Review. These positive observations are bounded inspection, not full qualification of every unsupported input form. |
| 4. Expectations and discriminators | The tests cite fixed register/Stage S outcomes and exercise production owners; the F13 test passes. Spot-checks covered genuine fix/revert and unbounded matching, retained-work independence, gate minimum and cycle behavior. Three controlled mutations below each fail a named real-owner test with a passing base. The full author mutation list was not independently rerun. The plan's explicit unexecuted cases remain unexecuted. |
| 5. Fitness | F0–F13 and B1 run in SSDS acceptance and CI; the clean real tree and synthetic rule-breaking fixtures pass. The closed import-list/facade/root readings fit the amended owner. The checker is a sensor; N2 is a concrete missed live-Git dependency. The static B1 result does not close A-B3. |
| 6. Determinism and exit properties | All supplied determinism, within-entry order, historical-prefix and checkpoint-resume tests pass, over eight seeded generated ledgers exercising F/P/T. Normal checkpoint-key/body corruption is refused. Caching only the S0 fold and recomputing S1–S3 can realize the same state without caching every projection; N1 bounds the stronger cache-integrity claim. |
| 7. Ledger and qualification | Real Git/signature tests pass for authentication, keys in force, prev/commit-chain agreement, schema halt versus unreadable schema, compare-and-swap, fixed metadata, referenced parents and non-overwriting checkpoints; qualification/loss-bound fixtures pass. A-B2 falsifies quorum identity counting. These checks do not exhaust crash, compromised-key or hostile-witness qualification, which remains bounded by the later fault phases. |
| 8. Shadow boundary | Positive genesis tests compare product refs, object inventory and status, and the throwaway ledger has only its ledger ref. Modes are LEGACY/UNGOVERNED. A-B3 disproves general home-write containment on a refusal path. This Review performed no governed publication or native transition. |
| 9. Core behavior | The 393-test Core suite, frozen-profile checks and snapshot check pass. All 22 frozen profile/prompt resource files are R100 renames with zero content changes. Core's changed source is concentrated in names/group discovery, home/configuration, CLI composition/doctor reporting and the additive canonical-JSON implementation/export; source resolution's resource lookup changes package name. Persisted identifiers and schemas remain frozen. A separate exhaustive old/new runtime differential of every possible prompt/configuration was not performed. |
| 10. First release | The exact pip installation succeeds; installed wheel/sdist tests run real `ssds` commands, including help and doctor. Home override/absolute-path/read-only-doctor and first-write cases pass. No predecessor alias/detection/migration was found in the inspected changed paths. The CLI's unchecked ledger-ID input remains a first-day correctness defect (A-B3). Python 3.11+ and interpreter selection are documented. |
| 11. Step 7 | The manifest declares the accepted protocol release tree and Manual as whole legacy subjects with section/component parts, plus the ungoverned program; modes come from genesis and accepted protocol resolution. The evidence record describes a stakeholder-held key and signed human gate at baseline `9bf19912`, with public digests, QUALIFIED genesis and no derivation findings. A separate candidate-baseline throwaway prepare/sign/admit/derive succeeds. The warning suppression is covered by `AnalyzedSourceWarnings`. Historical success is credible within the record's stated scope; it does not cure the currentness consumer or invalid-genesis paths. The Phase D exit therefore does not pass. |

### Disposition of every Phase D plan §8 reading

| Reading | Disposition and reason |
|---|---|
| 1. Bounding currency | **Not an authorized D4 reconciliation:** SC-1. Matched-content currency replaces evaluation-frame currency. |
| 2. Policy schema | Bounded D4 parameter representation; closed tables preserve data-only policy. This is not acceptance of policy values or a rule language. |
| 3. Default mode | Sound explicit genesis parameter: `"*"` prevents newly declared subjects silently acquiring native authority; step 7 chooses UNGOVERNED. |
| 4. Admission body | `integrates` and authored/adopted structural deltas record the transformation/enactment facts required by the frame fold. Their non-genesis admission enforcement remains Phase F. |
| 5. Judgment domain | Sound semantic domain selection from judged content, rather than confusing target representation type with D1–D4 authority. |
| 6. Assessment home | File-overlap widening is conservative for identifying successors; finer matching is not claimed. This judgment does not qualify all future move/rewrite histories. |
| 7. Execution basis | A closed recorded representation is suitable; admissibility/custody truth of those recorded fields remains a separate Phase F boundary. |
| 8. Ordinary forced components | The implementation clamps every forced component to F; its classification follows the §6 support edges and the plan's disclosed over-approximation. Tests distinguish ordinary assessment-related cycles from critical mutual-acceptance cycles. Exact classification for all absorption-extension histories is not independently exhausted here; it must not be represented as such. |
| 9. Requalification | Comparing effect at retained R with withholding now, and answering by a fresh acting/current record of the kind/target, fits the kernel scope. The tests cover retained-current versus already-stale records and a fresh acceptance. Full workflow routing/discharge is deferred. |
| 10. Views | Historical/frame/halt/unreadable/missing-analyzer withholding is exercised in derivation. This internal permission to assert is not external currentness qualification; A-B1 is the missing consumer boundary. |
| 11. Checkpoints | S0 cache plus recomputed S1–S3 is a viable representation of the same derivation; cadence/storage belongs to the Phase E caller. Verified normal resume equals replay. N1 limits tamper claims. |
| 12. Home layout | Delegated layout under the chosen home is reasonable; it does not authorize escaping that home (A-B3). |
| 13. Tree injection | Sound owner-preserving concretization: the caller supplies trees, and baseline structure validation remains with derivation. |
| 14. Genesis refusal | Keeping relation/cycle findings separate from §1.9 static refusal is a defensible distinction, but the required tree-dependent static presence check is missing (A-B4). |
| 15. Human gate | The digest covers the proposal excluding id/approval; registered public keys verify SSHSIG in namespace `ssds`. A generated Admission key is distinct from the human approval key. Changed proposals/objects are checked on admission. The Review used only its own throwaway key. |
| 16. Admission | Fsynced witness checkpoint and read-back QUALIFIED head 0 are exercised before high-water initialization. This establishes the tested genesis admission, not unconditional later currentness; A-B1/A-B2 still apply. |

### Explicitly unexecuted later discriminators

The plan §8 defers to Phase E the D1/D2 revision-run variants of 575dc78 N5, f7419d5 N4 and f22b4dc N5; the amendment/tightening plan half of 63ddf91 N5; and f03b15e N5's human reassessment of an answered non-gate obligation. They require revision runs, plan amendment or answered-obligation semantics. Phase F retains 51070e5 N3's adjudication-independence refusal, f03b15e N5's supersession-authority refusal and the other §8.3 steps 3/7 refusal discriminators, RR-11's resolver/Dispatcher half, and runner materialization/custody cases. S3 re-application/readiness/discharge/drift/impact/brief/conformance/routing queries require the Phase E item/plan owner. None is passed here. General admission, migration/cutover and adversarial/fault qualification are likewise not completed by Phase D.

## Judgments requested by handoff §4 — A7

| # | Judgment |
|---|---|
| 1. Fidelity | The central text states SD-56/SD-57: one program/distribution/import package/command, root `ssds.cli`, Core at `ssds.core`, retired aliases, separate operator home, option (ii) default and a first release. Distribution as a regular package is a sound consequence of that decision. The ledger's optional declared option (i) remains explicitly available in §21.5. |
| 2. Siblings | §0.5 export naming, §16.10 CLI transport, §21.5 and the changed §26.2/§26.3 rows agree. The two unchanged §26.4 final-disposition rows do not: B-B1. |
| 3. Invariants | A7 retains one root, Core independence, version-bound behavior and frozen bytes, option-(i)/(ii) semantics and row 7's prohibition on Core importing components/root. The positive Core evidence supports that preservation. B-B1 must be corrected so the disposition table does not supply competing composition instructions. |
| 4. Cost/risk | No migration or alias cost is imposed on an installed predecessor under the explicit first-release decision. Separate ledger custody/backup and clone incompleteness are real operational costs; existing §23/§32.2 loss disclosures cover the core risk, with N3 a useful documentation improvement. No new architecture decision is inferred from that suggestion. |

## Verification, applicability and limits

Execution used Python 3.11.15 in an isolated virtual environment. The initial archive-only test attempts failed because Git metadata was unavailable; an initial dependency build also lacked network access. Those are environment failures, not candidate findings. After installing dependencies and attaching a separate scratch Git checkout at the candidate, the required commands completed:

| Check at candidate | Result |
|---|---|
| `python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt` | PASS; fresh package/build dependencies confined to scratch |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | PASS, 197 tests |
| `python orchestrator/scripts/run_core_tests.py` | PASS, 393 tests across 13 modules, including installed wheel/sdist acceptance |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | PASS |
| `python -m unittest discover -s tests -v` | PASS, 435 tests, 3 skips |
| `python3 -I qualification/ssds80/models/run_models.py --seeds` (review Python) | PASS, models and seeds; evidence only |
| `git diff --check e88d90de 0e49debe` | PASS |
| Frozen source/distribution/Architecture 1.6.0 | No changed paths under `source/`, `dist/` or `orchestrator/docs/architecture.md` |
| Frozen Core resources | 22 profile/prompt files: rename only, byte-identical |
| PEM schema | PASS, schema 1, 5 families, no notices |
| Canonical package build, independent validation, committed parity | PASS; fresh output under review scratch |
| Real throwaway candidate genesis | PASS for prepare, independent test-key signature, admit, chain read and initial derivation; only `refs/ssds/ledger/ssdp-shadow` in its ledger repository |

The three repository skips are the opt-in remote public-fallback realization checks for Protocol 6.2, 6.3 and 6.4. They are not claimed passed. No source or fallback identity changed in this candidate. The historical stakeholder ledger was judged through the requested public evidence record; its private present-day state was not independently authenticated by this reviewer.

Mutation spot-checks at real production owners, using reversible in-process substitutions outside the repository:

| Wrong variant | Named discriminator | Base / mutant |
|---|---|---|
| Literal evaluation-frame bounding currency | `test_assessment.Staleness.test_genuine_fix_is_stale` | 1 pass / 1 assertion failure |
| Replace existential `link_minus` with direct `on_minus` | `test_assessment.Staleness.test_unbounded_run_still_linked` | 1 pass / 1 assertion failure |
| Remove judgment independence floor | `test_support.TargetConditionsAndIndependence.test_no_actor_accepts_its_own_work` | 1 pass / 1 assertion failure |

Each mutant produced zero test errors. These three discriminators were freshly confirmed; the author's positional/equal-region, clamp, W-scope, adverse-pin, exact owner-exception, S3-classification, requalification, historical-halt and checkpoint-resume mutations were not all independently rerun. Their unmutated tests passed; that is a different claim. Scratch logs and probes are in the directory named above (`*-final.log`, `models.log`, `mutations.log`, `probes.log`, `currentness-boundary.log`, `missing-scope.log`). The counterexamples and expected owner consequences are recorded here so the decision does not depend on scratch retention.

An out-of-matrix adequacy pass started from P3/P4 and the human-gate/shadow boundaries rather than the test matrix. It found the currentness consumer bypass and the write-before-validation path. No scientific upstream contradiction was established. The Review does not exhaust every possible ledger, poisoned operator-state regime, input limit, key-compromise history or fault trajectory; the explicit findings already prevent the governed exit, and later phase obligations remain visible.

## Project Engineering Memory basis and applicability

The G2 workplan independently binds accepted/base memory to project state `af0455753e20ee54a969c844872e29e270007211` on the project-designated integrated publication line `main`, PEM blob `1561797125622f355f84eb27319f87e8fa4227d9`. That state is an ancestor of local `main`. The candidate's PEM blob is identical; there is no new overlay. Schema validation passes. Canonical metadata for all five families was inspected, including entries omitted by salience; partial coverage is not treated as absence of further history.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen resources and version-bound Core behavior are independently required by SD-56, Manual B1 and G2 frozen-surface rules; rename-only bytes and Core acceptance supply the transfer evidence.
  - id: DS-001
    disposition: APPLICABLE
    reason: Synthetic green matrices are bounded evidence; independent consumer and failure-path probes remain necessary.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No source-to-package routing repair or regeneration change is proposed by this Review.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: This task publishes no protocol fallback or successor source identity.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: The memory family's canonical scope is immutable protocol public-fallback publication, which this task does not perform. Genesis validation is judged directly against Manual 19.9, independently of a similar historical label.
```

PC-001's preservation capability transfers to the renamed package through unchanged resource bytes, version/profile resolution and independent Core acceptance; the old package name itself is deliberately retired by SD-56. Evidence-only memory entries add no normative force. No memory update was performed.

## Scientific checks and common-mode limits

- **Material findings:** SC-1, A-B1–A-B4 and B-B1 above; N1–N3 remain explicitly bounded. No additional material scientific finding was established.
- **Realized scientific results:** none produced, run or reviewed. Execution generated engineering qualification fixtures and review counterexamples only; no scientific result acceptance is implied.
- **Variants:** no scientific model/method selection. Engineering exploration evaluated ten perturbed variants: three production-semantic mutations, three qualification-boundary variants (missing witness, high-water rollback, undeclared responder), one rechecksummed cache, one invalid ledger path, one missing-scope genesis and one indirect-Git fitness fixture. Criteria were the named owner invariants and discriminator outcomes, not comparative score optimization. The supplied determinism suite separately uses eight seeded generated ledger histories.
- **Tension search:** no consequential judgment relied on accepted scientific D1/D2 authority, so no D1/D2 tension-search result is claimed. D1/D2 revision-run mechanics remain explicitly deferred.
- **Gaps:** private stakeholder-state reproduction, the three remote bootstrap checks, the remainder of the author's mutation workload, exhaustive cache-threat and fault qualification, and the later discriminators listed above were not performed. None is converted into PASS.

This is a different-family Review from the Claude author, but family diversity alone does not establish epistemic independence. The reviewer still shares the repository's source corpus, Python/Git toolchain and many author-supplied fixtures and expected outcomes. Fresh negative consumer probes, a real signed throwaway ledger and controlled semantic mutations provide distinct evidence routes within those limits. Prior review history and memory were hypothesis/routing aids, not reused verdict authority. Unrelated untracked paths that appeared in the stakeholder worktree during the Review were left untouched; no tracked candidate content was changed.

Nothing beyond the already authorized shadow scope is authorized. This NO-PASS supplies no Phase E dependent-work start, A7 acceptance, G3 acceptance, campaign authorization, G4 cutover or native governance authority.
