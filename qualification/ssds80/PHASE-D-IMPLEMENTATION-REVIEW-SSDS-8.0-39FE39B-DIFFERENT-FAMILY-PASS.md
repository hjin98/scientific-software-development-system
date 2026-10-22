# Independent Review — SSDS 8.0 Phase D, candidate 39fe39b

```text
GOVERNING SSDP: 7.2.1
PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
CANDIDATE: 39fe39b127dd9d6020086b78dcd3b1e76da46d6a
PREVIOUS CANDIDATE: df911c045920d317f1c81da90e71d14906feecf4
BASELINE: e88d90dec4143340fffcf5cd53e7de5167d46be0
SCOPE: Phase D implementation and exit; A-B12 repair and siblings, inherited
       findings and qualification judgments, unchanged A7/A8 confirmation.
       SD-59: trusted private operator home; static misconfiguration and accidental
       aliasing; repository exclusion, no operator-tree symbolic links, fresh
       genesis repository, complete atomic publication, unit ledger identity and
       path containment. Hostile home/account writers, concurrent path replacement,
       mount/bind aliases, hostile global Git configuration/templates/hooks,
       filesystems defeating the primitives and coherent private-cache rewriting
       are Phase H. Currentness still holds within the declared witness fault model.
MANUAL BLOB: 6226f323365966bbcf653545f3a35b1fd7d6e060
PHASE D PLAN BLOB: c4020877e59796ff2eec24863a3072693a9e018f
G2 WORKPLAN BLOB: 523464de8ad6ec45379bad7e49660a471868cf49
CATALOGUE BLOB: f4c515bb1c3d7d5cdc3b762a18dcf2f67bbe5341
HANDOFF BLOB: e5217d10fdb636be2e6dc838ad99a3441a3204bc
REVIEW METHOD: independent owner reconstruction; bounded Challenge Pass and
               out-of-matrix adequacy search; actual non-root filesystem permission
               trajectories; signed throwaway Git histories and genesis; real-owner
               failure injection and source mutation; prescribed and package checks;
               exact frozen-resource comparison.
REVIEWER: GPT family; engaged through Codex by the stakeholder's explicit request
          to execute the pinned handoff. This reviewing context did not author the
          candidate. No subagents used.
```

The handoff is `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-HANDOFF-SSDS-8.0-39FE39B.md`. The working branch was at `4d62fa6f9b0d49a8cf81768db9ac067e0d109c3f`; its only committed difference from the candidate was that handoff. Execution used an archive of the exact candidate, with isolated Git metadata and read-only object alternates to the original clone. No newer implementation was substituted. The repair's executable delta from `df911c0` is confined to `admission/genesis.py` and its tests; the guide and plan change, and the preceding handoff/Review records, add no runtime mechanism. Manual, catalogue and G2 workplan blobs match the handoff.

The implementation and design entrypoints were entered at the pinned public source. Relevant abstraction/concretization, specification, architecture, workflow, testing, evidence, semantic-definition, PEM/publication, convergence, security, storage and Python concerns were resolved for this review. The accepted Manual, the settled G2 register and stakeholder decisions SD-56–SD-59 govern. Earlier Reviews, author explanations, fixtures, models and memory remain evidence rather than authority.

All reviewer scratch, generated keys, homes, installations, builds, logs and mutations are under `/tmp/ssds80-phase-d-review-39fe39b`. Execution was as uid 1000, not root. Neither `~/.ssds` nor the stakeholder's private ledger or private key was inspected or written. This file is the sole repository deliverable; no implementation repair, commit, push, publication, acceptance or workplan closeout was performed.

## SERIOUS CHALLENGE

**None established.** SD-59 is consistent with the accepted Manual and G2 shadow boundary for the outcome reviewed here. Ordinary permission failures are in scope and must refuse; the candidate now does so. Static certification is adequate against the tested misconfiguration and accidental-aliasing family when the filesystem honors the specified primitives and paths remain fixed during an operation. Stronger hostile-account, race and mount guarantees belong to Phase H under the stakeholder's explicit boundary.

The out-of-matrix pass held the protected outcome fixed—operator writes cannot enter a product repository—and varied whether the validator could observe every relevant entry, whether a marker could be examined without listing its parent, whether a destination had an unexpected type, and whether a legitimate home was reachable without readable ancestors. No tested locally compliant trajectory still violated that outcome. This is bounded falsification, not proof of absence of every filesystem defect.

## Verdict

**Phase D implementation: PASS. Phase D exit: PASS.** The exit passes, not only the implementation. A-B12 is closed at its owner; the original permission-limited nested-product and in-home-link trajectories refuse before effects, and the retained tests discriminate the repair. Earlier repairs continue to hold in the inspected owners and executed regression. The public historical step 7 gate record is sufficient for the requested evidence review, and this candidate's prepare/sign/admit/derive path reproduces on an isolated home without changing the source repository.

**A7: PASS confirmed. A8: PASS confirmed.** The complete Manual blob is unchanged from `517af45` and each intervening candidate. The confirmation preserves the previously reviewed text's meaning; it does not accept either amendment on the stakeholder's behalf.

**NF8 remains non-blocking and unrepaired.** No Phase D blocker remains from this review. The PASS supplies the independent Phase D Review required by G2 §5.1 item 5, permitting dependent Phase E work within the already authorized shadow scope; it accepts nothing at G3.

## A-B12 disposition and rule adequacy

**CLOSED.** The governing text is SD-59, Phase D plan §2 and §9, Manual §26.3 and G2 §5.1 item 2. The real owner is `orchestrator/src/ssds/admission/genesis.py`, specifically `Home.check`, `_mode`, `_listing` and `_is_repository`; preparation and admission call that owner rather than substituting a sensor.

The candidate implements one complete inspection rule:

1. Resolve the home and exclude repositories at it and every resolved ancestor. Inspect repository markers by `lstat`; failures other than absence refuse.
2. For each used tree—`ledgers/<id>.git`, all of `witness/`, `keys/admission/`, `genesis/<id>/`, `state/<id>/`—examine each holding component. A present component must be a directory, not a symbolic link, and must not be a repository except for the ledger root itself. A missing component terminates that nonexistent path; it does not certify an existing unreadable tree.
3. For an existing tree, explicitly list every directory and examine every listed entry. A listing failure, examination failure or vanished entry refuses; only directories and regular files survive classification. Every directory is traversed, with nested repository exclusion. The ledger-root repository exception does not exempt its descendants or entries from inspection.
4. Check ledger identity and resolved containment, including named output files. Preparation checks before filesystem effects; admission checks at entry and again immediately before its first Git write. The report consumer checks before qualification can update W or publish `derivation.json`.

The old `os.walk` omission is absent. `_listing` materializes the complete enumeration inside its error boundary, so even failure after an initial entry refuses. `_mode` does not collapse an inaccessible marker into absence. The temporary disappearance and partial-iteration probes inject faults below the real validator; they test failure propagation, not an adversarial path-replacement guarantee.

### Required trajectories and additional siblings

| Trajectory | Executed result and protected effect |
| --- | --- |
| Committed `witness/demo` product under mode-0300 `witness`, before preparation | Visible invalid preparation, no proposal/workspace, key, state or ledger creation; nested product refs, object inventory and status unchanged. |
| Same product introduced after prepare/sign, before admission | `GenesisRefused` before state or ledger creation; existing prepared workspace/key remain, nested product unchanged. This is a separate stable misconfiguration at the next operation, not a check/write race. |
| In-home link at `witness/demo` under mode-0300 witness | Refuses both before preparation and after the gate. Target product state is unchanged; no checkpoint enters it. |
| Readable nested repository and readable in-home link | Both refuse. Removing the collision admits the same clean signed proposal as `QUALIFIED`. |
| Hidden link under each of the five used trees, modes 0300 and 0600 | All ten refuse at preparation without returning a workspace. The retained permission tests also execute these cases at `Home.check`. |
| Empty listable but unsearchable directory | Refuses because its repository marker cannot be examined; an empty listing alone cannot certify it. |
| Inaccessible `.git` directory in a home ancestor or inside the operator tree | Refuses on marker examination. Mode-000 regular `.git` and bare `HEAD` markers remain observable by `lstat` and are recognized as repository layouts without reading file contents. |
| Regular file at any of nine required layout directories/holding directories | Refuses before preparation effects; the existing file is unchanged. |
| FIFO in a used tree | Refuses as neither regular file nor directory. The same classification excludes sockets/devices by mode; a real socket creation probe was unavailable because the sandbox denied AF_UNIX bind. |
| Listed entry disappears; enumeration fails after its first entry | Both explicitly refuse before workspace creation. |
| Ordinary external home; linked external home; traversable but unlistable ancestor; empty `.git` directories | Each clean control prepares, signs, admits, and passes `Home.check` after admission. No ancestor directory listing is required. |
| Worktree, linked-worktree gitfile and bare repository at nine operator/holding locations | All 27 refuse with recursively compared file bytes unchanged. Nine empty-marker controls prepare successfully. |

The 34 additional cases in `challenge.py` all pass; its socket attempt is separately marked unavailable, not counted as a pass. The 36 placement cases in `probes.py` and retained tests supply additional, overlapping evidence. The retained non-root tests preserve the exact `df911c0` discriminator and its post-gate link sibling, not merely lower-level mocked exceptions. `exact_trajectories.py` independently repeats all four repository/link × preparation/admission combinations, comparing every product file's byte digest as well as refs, object inventory and status; all four refuse unchanged, and both post-gate clean controls admit.

### Repository-marker predicate

The predicate remains appropriate to this static exclusion boundary. A non-directory `.git` is conservatively a marker; a `.git` directory is a marker when any entry is present at `.git/HEAD`; an empty `.git` directory is not a repository. A bare layout requires non-directory `HEAD`, with `objects` and `refs` each a directory or link. Inaccessible evidence refuses. These tests identify a repository layout rather than certify Git's ability to operate it; treating damaged or unusual marker objects conservatively is appropriate to preventing writes into a product. Inside used trees the independent no-link/type rule also applies. The ledger-root exception is necessary and does not permit nested product repositories.

No further in-boundary counterexample survived. No change to the inspection rule or its parent authority is requested.

## Phase D blockers

**None found.** There is no outstanding blocker requiring minimum repair or a new discriminator. A-B12's repair is at its existing semantic owner and replaces incomplete traversal; it does not add a second certification registry or alternate authority. The negative controls below preserve the rule's discriminating evidence.

## No regression of earlier repairs and findings

The unchanged owners were inspected for applicability and exercised by the candidate suite. Qualification and publication additionally received real signed-history/failure probes and selected source mutations. This table does not imply that every historical mutation or later-phase obligation was repeated.

| Earlier finding | Current disposition and evidence |
| --- | --- |
| `0e49deb` SC-1 | Resolved by SD-58/A8; the bounding owner checks standing, matched-content membership/entries and evaluation-state premises. It is not reopened by this repair. |
| `0e49deb` B-B1, A7 supersession table | Closed in the unchanged reviewed Manual: §26.4 describes the root composition, one distribution and home-resident default ledger consistently. |
| A-B1, currentness without qualification | Closed. The real script qualifies first and derives only through H*. Removed-checkpoint, rollback and genuine provisional-successor consumer tests pass. |
| A-B2, undeclared responders | Closed. Only declared witness identities count; duplicate identities and invalid quorum models refuse qualification. |
| A-B3, ledger-id/path/file/internal-Git links | Closed within SD-59. Unit identity, resolved containment, complete no-link inspection and fresh ledger construction apply at preparation and admission; named API/CLI negatives pass. |
| A-B4, unresolved genesis terms | Closed. Missing file/heading/symbol/anchor cases refuse; present empty file and empty prefix controls pass. |
| A-B5, consumer retains no W | Closed. Actual consumer retains its qualified head; stale consistent restore is `ROLLBACK`. |
| A-B6, `INCOMPLETE` used as bound | Closed. The positive `COMPLETENESS/COMPLETE` guard remains; removing it fails the retained test. |
| A-B7, qualified head below W | Closed. Current H* must extend the retained mark; the qualifier and consumer regression pass. |
| A-B8, hard-link write-through | Closed. Replaced files use fresh exclusive temporary objects and atomic rename; retained workspace/high-water/CLI hard-link controls leave product files unchanged. |
| A-B9, observed checkpoint relabeled provisional | Closed. Every qualifying head extends every observed unabandoned checkpoint; observed newer state withholds currentness until read repair. Ninety declared-class holder/read/fault configurations and their repair controls pass. |
| A-B10, home inside repository | Closed. Home and resolved ancestors are excluded before effects, including linked-home cases. External linked-home and empty-marker controls remain usable. |
| A-B11, suffix recovery abandons observed state | Closed. Abandonment is read only from the candidate quorum-held prefix. Real signed `LEDGER_LOSS` and `FORK_RESOLUTION` histories, repeated recovery and abandoned-recovery siblings remain non-current until their required checkpoint/explicit abandonment conditions hold. Whole-chain abandonment mutation fails. |
| A-B12, nested repositories and silent traversal | Closed as detailed above; unreadable trees and markers refuse before effects. |
| A-B13, short writes/checkpoint names | Closed. `write_all` completes progressing writes or fails; checkpoints gain their final names only after complete file write/fsync, by non-overwriting hard link. Real kernel-limit tests and nine publication/failure/name probes pass; single-write mutation fails. |
| `0e49deb` N1 | Accidental cache corruption is detected; coherent private-cache rewriting is outside this Phase D boundary. No authenticity claim is inferred from the body checksum. |
| `0e49deb` N2; `517af45` NF1; `137b763` NF4; `d8bdfd3` NF6 | Named reader/facade/dotted/relative, unrelated attribute, scoped import, parameter and assignment-alias cases remain covered. Actual derivation still takes supplied trees/chains rather than invoking forbidden readers. |
| `0e49deb` N3 | Home-resident ledger/witness/W backup consequences remain disclosed; a product clone alone is insufficient. |
| `517af45` NF2 | Catalogue bounding polarity, membership/content and cited-premise support agree with SD-58. Admission's cited-premise support-cycle enforcement remains Phase F. |
| `517af45` NF3 | Consumer passes file-witness retirement to qualification; actual retirement test passes. Authenticating retirement remains later work. |
| `137b763` NF5 | W is the last qualified head, even if a missing analyzer subsequently withholds derivation. Conservative remembrance does not create a false-current path. |
| `b341109` NF7 | All named binding-order, annotated-local and class/method-scope cases still pass. Restoring the earlier checker fails its retained test. |
| `df911c0` NF8 | Retained as non-blocking, with the four actual sensor mismatches reproduced below. |

Checkpoint publication probes covered progressing one-byte writes, zero progress, write error, file-fsync error, link error, directory-fsync error, existing equal bytes, existing different bytes and existing symbolic-link names. Failures before link publish no checkpoint and clean the temporary. Directory-fsync failure visibly propagates after a complete file is linked; rollback of an already linked name is not claimed. Existing different bytes/link names are preserved and refused.

## Phase H items — outside SD-59

The following remain unqualified here: hostile writers with home/account access; concurrent replacement between inspection and use; mount/bind aliases; hostile global Git configuration, hooks or templates; filesystems that do not honor the required publication/durability primitives; coherent private-cache rewriting. Complete static inspection is not protection against these cases. Crash/concurrent-reader high-water monotonicity and broader resource/scaling qualification also require their appropriate later evidence.

The public step 7 record and this local reproduction do not independently establish another witness medium or separate administrative custody. `LOCAL_TRUST` currentness relies on its declared no-common-rollback premise. This review does not claim that placing a witness under the same home proves that deployment premise. The boundary does not excuse an algorithmic qualification failure within the declared model; those cases remain Phase D blockers if found, and the executed qualifier probes found none.

General recovery authorization/control re-establishment and authenticated witness retirement remain with later Admission/security work. Signed-history qualifier probes exercise the qualification owner and do not qualify those unimplemented authorization paths.

## Non-blocking findings

### NF8 retained — the fitness sensor still has Python binding/order limitations

The checker is byte-unchanged by this repair. The following full-checker probes reproduce `df911c0` NF8:

| Case after `import ssds.content as c` | Expected F8 | Actual F8 |
| --- | --- | --- |
| Module annotation `c: object`, then `x = c.read_tree` | yes | no |
| Class body reads `c.read_tree`, then module rebinds `c = None` | yes | no |
| Define function reading `c.read_tree`, call it, then rebind `c = None` | yes | no |
| Function reads `c.read_tree` before its own local `c = None` | no reachable imported reader; runtime unbound local | yes |

The three named NF7 controls continue to agree with their expected outcomes. Inspection found no corresponding forbidden Git-reader or I/O route in production derivation. Manual §26.2 explicitly limits fitness checks to sensors; these limitations therefore do not independently block Phase D. Future strengthening should repair the checker at ordinary Python binding/evaluation semantics while preserving the pure-code controls. No complete dependency-analysis claim is made.

No additional non-blocking product defect was established by the containment repair.

## Handoff §3 judgments

1. **A-B12:** closed at `Home.check` and `_is_repository`, with direct and retained non-root discriminators. The rule is realized at every Admission safety decision and at report publication; its stated static boundary is adequate for the tested protected outcome.
2. **Earlier repairs:** home placement, complete no-link inspection, ledger exception, fresh repository creation, atomic complete publication, qualification-prefix recovery, checkpoint naming and named NF7 cases hold in the inspected candidate and tests.
3. **Repair-created defects:** no blocker found. Legitimate external/linked homes, traversable but unlistable ancestors and admitted ledger contents remain usable; the real shadow script reproduces through derivation. Conservative refusal of an unexaminable marker is required by the rule, not a regression.
4. **Inherited judgments and exit:** all eleven original questions and sixteen readings are reconciled below. A7/A8 confirmations stand. The public historical gate evidence and fresh candidate-history run meet the requested step 7 review; G2 §5.1 items 2 and 5 are satisfied for this shadow Phase D exit. NF8 remains non-blocking.

### The original handoff's eleven implementation questions

| Question | Judgment |
| --- | --- |
| 1. Scope and owners | Components retain §26.1 ownership; this repair stays within Admission's existing validation owner. Derivation does not gain Git or filesystem access, and models are not imported by production. No new out-of-register mechanism found. |
| 2. Plan §8 readings | All sixteen reconciled below against their Manual/register owners. No reading authorizes incomplete inspection. |
| 3. Fail-closed deferrals | Native D1/D2 revision-run gates, conservative plan reach, unavailable declarative verdicts, general admissibility and item views remain unsupported/deferred as stated; no new support path is introduced. |
| 4. Expected values/discriminators | Group 1–3 tests carry literal register/Stage S expected outcomes, F13 passes, and selected mutations discriminate real production owners. Models remain diagnostics, not the production oracle. Deferred cases are not counted as executed. |
| 5. Fitness | Real source and synthetic acceptance pass. NF7 named cases hold; NF8 limits Python sensor completeness. B1 alone cannot establish destination ownership; actual Home/Admission trajectories supply that evidence. |
| 6. Determinism/replay | Seeded histories cover F/P/T; function-of-input, record permutation, historical-prefix equality, checkpoint key/body negatives and incremental/from-scratch properties pass. No production-scale or hostile-cache qualification inferred. |
| 7. Ledger/qualification | Signature, key-in-force, prev/Git-parent/schema/halt/CAS and loss-bound tests pass. Actual complete publication and signed recovery-prefix probes pass; the 90 quorum configurations preserve declared-class currentness. |
| 8. Shadow boundary | Genesis allows only LEGACY/UNGOVERNED modes, creates only its dedicated ledger ref and preserves source product refs/objects/status. The formerly escaping permission-limited paths now refuse before writes. |
| 9. Core preservation | Core's 393 tests across 13 modules, including independent installed wheel/sdist acceptance, pass. All 22 frozen resource blobs are identical under the rename. Source, dist and frozen Architecture 1.6.0 are unchanged. Exhaustive rendered pre/post-rename behavior differential was not repeated. |
| 10. First release | Python 3.11 install, command composition, help/doctor/no-write home behavior, absolute override and first-write/refusal tests pass. No predecessor migration or alias was added. |
| 11. Step 7 | Case B manifest/public evidence reviewed; actual candidate-history prepare/sign/admit/derive yields current-qualified H*=0, no findings or obligations and correct shadow modes, with source refs/objects/status unchanged. Private historical custody remains uninspected. |

### Phase D plan §8 readings

| Reading | Judgment |
| --- | --- |
| 1. Bounding currency | SD-58/A8's standing, matched-content membership/entries and evaluation-state premise split is preserved. Genuine fix/revert, challenge, membership and cited-premise tests pass. |
| 2. Policy schema | Closed domain tables remain delegated data; missing holders confer no authority. |
| 3. Default subject mode | Explicit `"*"` keeps later subjects UNGOVERNED in shadow. |
| 4. Admission body | Integration/adopted-delta facts feed S0; general admission validation remains Phase F. |
| 5. Judgment domain | Domain follows judged content, including changed transformation units, rather than target syntax. |
| 6. Assessment home | File-overlap widening remains conservative; arbitrary move/fine-region precision is not claimed. |
| 7. Execution basis | Recorded closed fields are consumed; runtime truth and custody are not established by parsing them. |
| 8. Forced components | Every forced node remains F; ordinary/integrity classification affects attention, not value. Support-cycle tests pass. |
| 9. Requalification | Retained/in-effect, withheld and fresh-record cases pass; complete item workflow remains Phase E. |
| 10. Views | Historical, frame, halt, unreadable-schema and missing-analyzer withholding remain. Consumer reads only the qualified prefix. |
| 11. Checkpoints | Keyed S0 fold and accidental body-corruption detection remain bounded cache evidence; S1–S3 are recomputed. Storage/cadence belongs to the later caller, and coherent rewriting remains Phase H. |
| 12. Home layout | Layout remains delegated and coherent; complete inspection now closes the prior refusal gap. Ledger-root exception and atomic file publication preserve the static boundary. |
| 13. Trees | Caller supplies tree reading; Admission validates through public baseline derivation, preserving component ownership. |
| 14. Refusals | Named manifest/static/mode/policy/key/witness/ledger and term negatives pass, including empty-present controls and the newly complete permission/type refusal family. |
| 15. Human gate | Exact proposal digest, namespace and registered SSH key are checked; altered proposal/message/key negatives pass. Only reviewer-generated private keys were used here. |
| 16. Admitted | File witness acknowledges only complete published checkpoint bytes; genesis qualifies at 0 and W is retained. The candidate-history end-to-end path passes. |

**Explicitly unexecuted later obligations:** Phase E retains the D1/D2 revision-run variants of 575dc78 N5, f7419d5 N4 and f22b4dc N5; 63ddf91 N5's plan-amendment/tightening half; f03b15e N5's reassessment of an answered non-gate obligation; and item readiness, discharge, drift, impact, conformance, brief, routing and re-application views. Phase F retains 51070e5 N3's adjudication-independence refusal, f03b15e N5's supersession-authority refusal, other §8.3 steps 3/7 refusals, cited-premise admission-cycle enforcement, RR-11 resolver/Dispatcher behavior, designated-runner materialization/custody, general recovery authorization/control re-establishment and authenticated retirement. Migration/cutover, campaigns and Phase H qualification remain unexecuted. These are later-phase obligations, not missing Phase D checks.

## Verification, mutations and evidence limits

All accepted executions used Python **3.11.15** at the exact candidate, uid **1000**. Installation used local cached distribution wheels supplied under the review scratch root; the candidate package was built and installed. Core independently built and installed wheel and sdist products. No network fallback execution is claimed.

| Required or supporting check | Executed result |
| --- | --- |
| `python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt` with scoped offline inputs | PASS |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | PASS, 230 tests, no skips; both permission tests ran as non-root |
| `python orchestrator/scripts/run_core_tests.py` | PASS, 393 tests / 13 modules |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | PASS |
| `python -m unittest discover -s tests -v` | PASS, 435 tests, 3 opt-in skips |
| `python3 -I qualification/ssds80/models/run_models.py --seeds` using the review interpreter | PASS; zero settled misses, expected refutations and seeds, including 14,508 routing answer chains |
| `git diff --check e88d90de 39fe39b1` | PASS |
| Source, dist, frozen `orchestrator/docs/architecture.md` versus baseline | No changed paths; byte-identical Git objects |
| Complete frozen Core resource inventory | 22 R100 moves, each old/new blob equal; no extra/missing resource path |
| Validation dependencies, release-state and PEM validation | PASS; PEM schema 1, 5 families, 0 notices |
| Fresh canonical package build, independent validation, committed dist parity | PASS |
| Additional containment cases; placement cases; signed recovery; publication failures; quorum/read repair | PASS within the counts/regimes disclosed here |
| Candidate-history signed genesis through real script and derivation | PASS, H*=0 current, no findings/obligations, source state unchanged |
| Known-wrong source variants | All 9 detected; source restored byte-for-byte |
| Restored-source full SSDS suite | PASS, 230 tests, no skips, explicit candidate source imports |

The repository suite's three skips are opt-in exact-ref remote fallback realizations for 6.2/6.3/6.4. They are unexecuted, not passed; their immutable identities and source are unchanged by Phase D. The required non-root SSDS cases were not skipped. The sandbox's denial of a real socket bind limits that optional sibling realization; actual FIFO refusal and mode classification cover the required other-file-type question, without claiming a live socket test.

**Nine source mutations executed:** whole-chain rather than prefix-local abandonment; removal of descendant-repository exclusions; unchecked single write; earlier NF7 fitness map; removal of the COMPLETE guard; restoration of the previous Home validator; listing failure treated as empty; examination failure treated as absent; and allowing special files. Each ran sequentially against explicit candidate source imports, produced its expected test failure and was restored. The old Home validator fails the new retained discriminator set (16 assertion failures and 5 errors across the three selected tests); silently empty enumeration fails six subcases; allowing a FIFO makes the retained preparation-refusal assertion fail.

For the examination-as-absent mutation, the retained tests also detect changed failure diagnostics. To distinguish diagnostic mismatch from an actual unsafe certification, a separate lower-boundary discriminator reused the inaccessible-marker cases: the ancestor `.git/HEAD` case becomes accepted under the mutant and fails `assertRaises(HomeRefused)`. The operator-tree sibling still refuses through its independent listing check. Thus the ancestor probe supplies a behavioral safety discriminator rather than relying only on error-message spelling. The restored candidate passes both marker controls.

**Harness limitations and corrected failures:** a first post-mutation full-suite invocation from the repository root with an extra test-path override resolved the wrong `tests` package and failed to import `tests.ssds`. The source had already been restored. The corrected invocation from `orchestrator/`, with explicit candidate source and `-s tests/ssds -t .`, passed all 230 tests. That failed invocation is not counted as product failure or successful acceptance. The optional socket bind was denied before a socket filesystem entry existed; remaining challenge cases were then run to completion. No required prescribed check remains unavailable.

**Step 7 identities and applicability.** The public historical record binds baseline `9bf199120f7f289f10994189d1bd718690653dfc`, stakeholder-signed genesis digest `sha256:d7514f67a1071f6e008766a57a8c79d7ca88a434eddf19867194546b6b2e9a22`, and entry commit `980373b80a9a0af8487bc3fece16d948e9d2ab74`. Its validation/derivation reports and SSH gate account were reviewed as public evidence. Fresh reproduction used this candidate's actual history, Case B manifest and a new reviewer-generated approval key, producing qualified entry digest `sha256:a6532ff833a0d8b11aa55520ef29c2a99d9c80eed6e7a7b1483078b4b2cb793d`. It derived protocol/manual LEGACY and program UNGOVERNED, all `valid=F`, expected with no admitted acceptances. Source refs, object inventory and status were equal before/after. This does not retake the stakeholder's historical gate or inspect private custody.

Scratch reproduction routes: `run_checks.py`, `checks.json`, `extra_checks.py` and `logs/`; `challenge.py`; `exact_trajectories.py`; `probes.py`; `quorum_probe.py`; `history_genesis.py`; `mutations.py`; `marker_discriminator.py`; and `frozen-identities.json`. These remain cold supporting evidence under the stated scratch root. The identities, counts, outcomes, decisive trajectories and limits needed for the decision are retained in this record.

## PEM applicability

PEM activates through the memory-bound G2 workplan and repeated containment family. Project policy designates integrated `main`; the workplan pins base `af0455753e20ee54a969c844872e29e270007211`, independently matched by local `main`. Its PEM and candidate PEM are byte-identical, blob `1561797125622f355f84eb27319f87e8fa4227d9`; validation reports schema 1, five families, zero notices. Canonical metadata of all five families was inspected regardless of temperature. There is no new branch byte overlay to compose; inherited overlay prose does not self-ratify another memory state. Coverage remains PARTIAL.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: SD-56, Manual 26.4 and G2 independently require frozen resources and version-bound Core preservation; complete blob inventory and Core installed-product checks pass.
  - id: DS-001
    disposition: APPLICABLE
    reason: Fixture success cannot establish complete inspection; actual kernel permissions, real prepare/admit paths, failure propagation and source mutations discriminate this owner.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No canonical router or generated-route repair is under review.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No immutable fallback publication is under review.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: Premature immutable bootstrap publication is not the mechanism under review.
```

PC-001's force comes from independently resolved current owners, not memory placement. No memory update or recurrence-after-accepted-repair count is inferred from these unaccepted Phase D repair rounds.

## Scientific checks and common-mode note

- **Material findings:** no remaining Phase D blocker or accepted-authority Serious Challenge established; A-B12 closes. NF8 remains a non-blocking sensor limitation. A7/A8 technical verdicts stand.
- **Realized scientific results:** none produced, run or reviewed. Null scientific-result envelope: no physical experiment, scientific dataset, trained model, numerical-estimator result or scientific-result population was evaluated. The observations here are engineering evidence: synthetic histories, throwaway signed Git ledgers, ordinary filesystem permissions, publication failures and the public historical shadow gate record.
- **Variants evaluated:** nine known-wrong source variants; four original permission-limited repository/link × preparation/admission trajectories with complete product-byte comparison; 34 additional containment/control cases (plus one unavailable socket attempt); 36 repository-placement/empty-marker configurations; six recovery stages for each of two lifecycle kinds; nine checkpoint publication/failure/name configurations; seven fitness snippets; and 90 holder/read/fault configurations across the three declared deployment classes, each with a read-repair control. These sets overlap and are not summed as independent observations. Marker cases were reused against one existing mutation, not counted as a tenth source variant. Retained-suite subcases and the candidate-history run are reported separately rather than inflated into independent variants. Criteria were pre-effect exclusion and preservation, legitimate-home usability, complete durable publication, currentness under declared witness assumptions and allowed/forbidden dependency discrimination. No scientific parameter survivor was selected, and the author's earlier search history was not reconstructed.
- **Tension search:** no consequential judgment relied on accepted scientific D1/D2 authority; no D1/D2 tension-search result is claimed. Engineering qualification, identity, recovery and containment definitions were resolved at their owners.
- **Gaps:** the three opt-in remote fallback runs; actual socket bind; private historical gate/witness custody; exhaustive Core pre/post-rename behavior differential; complete Python dependency analysis; later E/F/G/H obligations; production-scale/crash/hostile-environment qualification; native cutover and live campaigns. None is reported passed. None is a missing required Phase D execution under this handoff.

Different model family provides process diversity without establishing epistemic independence. This review shares the accepted Manual/register, source, Python/Git/filesystem toolchain and many fixtures with the author and prior Reviews. Earlier scratch harnesses were inspected and adapted to the pinned candidate, then rerun; their prior outcomes were not inherited as current passes. Actual kernel permission cases, additional marker/type/failure trajectories, real signed candidate-history genesis and known-wrong source mutations provide distinct evidence routes, but do not establish exhaustive defect freedom. The PASS is limited to the declared Phase D shadow scope and assumptions.

**Nothing beyond shadow is authorized.** This technical PASS supplies the Phase D implementation/exit Review and permits dependent Phase E shadow work under the existing G2 rule. It is not G3 acceptance, stakeholder acceptance of A7/A8, deployment qualification, native authority/G4, cutover, publication, a live agent campaign or measurement-spend authorization.
