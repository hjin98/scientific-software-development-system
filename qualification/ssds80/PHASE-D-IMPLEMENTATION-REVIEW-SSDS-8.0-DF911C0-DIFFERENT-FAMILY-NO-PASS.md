# Independent Review — SSDS 8.0 Phase D, candidate df911c0

```text
GOVERNING SSDP: 7.2.1
PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
CANDIDATE: df911c045920d317f1c81da90e71d14906feecf4
PREVIOUS CANDIDATE: b341109a6a23340692d0d7cddfd918666c6d2495
BASELINE: e88d90dec4143340fffcf5cd53e7de5167d46be0
SCOPE: Phase D implementation and exit; every b341109 finding and its repair
       siblings; inherited Phase D judgments; unchanged A7/A8 confirmation.
       SD-59: trusted private operator home; static misconfiguration and accidental
       aliasing; repository exclusion, no operator-tree symlinks, fresh genesis
       repository, complete atomic publication, ledger-id grammar and containment.
       Hostile home/account writers, check/write races, mount/bind aliases, hostile
       global Git configuration/templates/hooks, filesystems defeating the primitives
       and coherent private-cache rewriting remain Phase H. Currentness must hold
       within the declared witness fault model.
MANUAL BLOB: 6226f323365966bbcf653545f3a35b1fd7d6e060
PHASE D PLAN BLOB: 7f4a46309f4dacfa0275c27faedd14561c6f109f
G2 WORKPLAN BLOB: 523464de8ad6ec45379bad7e49660a471868cf49
CATALOGUE BLOB: f4c515bb1c3d7d5cdc3b762a18dcf2f67bbe5341
REVIEW METHOD: independent owner reconstruction; bounded Challenge Pass and
               out-of-matrix containment trajectory; actual signed Git histories,
               prepare/sign/admit/derive, kernel permission and short-write behavior,
               lower-boundary failure injection, retained-test mutations, prescribed
               checks and frozen-resource identity checks.
REVIEWER: GPT family; engaged through Codex CLI in the stakeholder's own terminal
          at the stakeholder's request. The author's session typed only the pointer
          prompt and did not frame the candidate otherwise. This context did not
          author the candidate. No subagents used.
```

The named handoff is `PHASE-D-IMPLEMENTATION-REVIEW-HANDOFF-SSDS-8.0-DF911C0.md` in this directory. The working branch resolved to `f6dc18ade2170f58d6bf8b186a91d9e1b233c22c`; its sole difference from the candidate was that handoff. Execution used an archive of the exact candidate, with isolated Git metadata and read-only object alternates to the original clone. No newer implementation was substituted.

The implementation and design entrypoints were entered at the pinned public source, with the abstraction/concretization, specification, architecture, workflow, testing, evidence, specialized-definition, storage, security, convergence, Python and applicable PEM owners. Release-state identities were independently checked. The accepted Manual, G2 register and stakeholder decisions SD-56–SD-59 govern; plans, handoffs, earlier Reviews, tests and models remain hypotheses/evidence.

All reviewer scratch, keys, homes, installations, logs and mutations are under `/tmp/ssds80-phase-d-review-df911c0`. Neither the stakeholder's private ledger nor `~/.ssds` was inspected or written. This record is the sole repository deliverable. No implementation repair, commit, push, publication, acceptance or lifecycle closeout was performed.

## SERIOUS CHALLENGE

**None established against the accepted Manual, G2 workplan or SD-59 boundary.** The blocker is a D4 violation of coherent static guarantees: the existing tree validator silently ignores a directory-enumeration failure, then treats the unexamined subtree as admissible. Ordinary Unix permissions do not defeat filesystem primitives and require neither an adversary nor a race. Refusing an uninspectable used operator tree satisfies the existing boundary without changing it.

The out-of-matrix pass held the protected outcome fixed—operator writes cannot enter a product repository—and varied whether validation could actually observe its required input. A complete atomic checkpoint write still violates that outcome when its directory is an undiscovered product worktree. Atomic publication and lexical containment do not establish destination ownership.

## Verdict

**Phase D implementation: NO-PASS. Phase D exit: NO-PASS.** A-B11 and A-B13 are closed at their inspected owners, with discriminating retained tests. A-B12's normally readable cases are repaired, but its containment family remains open through silent traversal failure. The clean step 7 path reproduces successfully; that does not close the implementation blocker or authorize Phase E's dependent work.

**A7: PASS confirmed. A8: PASS confirmed.** The Manual blob is exactly the previously reviewed blob, unchanged since `517af45`; the current catalogue also matches the blob confirmed at `b341109`. These text verdicts do not accept either amendment for the stakeholder.

## Disposition of every b341109 finding

| Finding | Disposition at df911c0 |
| --- | --- |
| A-B11, unwitnessed recovery suppresses checkpoints/W | **Closed at the qualification owner within the exercised read contract.** Abandonment is recomputed from each candidate quorum-held prefix. Real G0/E1/rewind/recovery runs for both lifecycle kinds refuse currentness before acknowledgment and qualify the recovery after it. Further recovery orderings pass. Restoring whole-chain abandonment fails the retained discriminator for both kinds. General recovery authorization is not thereby qualified. |
| A-B12, repository at an operator write location | **Named readable cases closed; family retained as a blocker below.** The four supplied locations refuse unchanged, with a clean admitting control. Additional ordinary, gitfile and bare layouts refuse when enumerable. An unreadable but traversable witness root hides a nested repository that Admission subsequently writes into. Removing the new repository checks fails the retained test; that test does not cover incomplete enumeration. |
| A-B13, incomplete writes published as complete | **Closed for the inspected owners.** The shared `write_all` completes progressing short writes and fails on zero progress. The real one-byte `RLIMIT_FSIZE` cases now fail visibly, preserve the old mark, hold no partial checkpoint and leave no temporary. The checkpoint name is linked only after complete file fsync; same-name different bytes refuse. Replacing the loop with one unchecked write fails all three retained test trajectories. |
| NF7, binding order, annotated locals, class/method scope | **All three named cases corrected.** The full checker reports the pre-rebinding read and accepts the annotated pure local and class-local/method-global control. Restoring the preceding map fails the retained discriminator. New ordinary scope/order sensor limitations remain NF8 below. |
| Empty host `/tmp/.git` environment note | **Resolved for this environment.** The actual empty directory no longer blocks scratch homes. Real `.git` directories with HEAD, gitfiles and bare layouts remain refused at inspected locations. No mount namespace or production bypass was needed. |
| Phase H items and explicit later-phase gaps | **Preserved, not passed.** Their classification does not excuse the static traversal failure or qualify general recovery/custody machinery. |

## Phase D blocker

### A-B12 retained — Silent traversal failure bypasses repository and no-symlink validation

**Owner text.** SD-56 and Manual §26.3 place operator data outside product/program repositories; G2 §5.1 item 1 says operator data is “never in a repository,” and item 2 protects the shadow boundary. Phase D plan §2 and SD-59 require the static structural checks **before any effect**, including that the used operator tree holds no symbolic link. The repaired plan §9 and handoff §3 item 3 require exclusion of repositories inside that tree, except the ledger's own repository. This is already-binding placement/validation behavior, not a new security feature.

**Actual owner and cause.** `orchestrator/src/ssds/admission/genesis.py:201`, especially line 217: `Home.check` calls `os.walk(top, followlinks=False)` without an error handler. A directory that cannot be listed is silently omitted. The loop therefore sees neither its descendants' repository markers nor its symbolic links. The final `witness_directory` call checks resolved containment but neither proves enumeration completed nor independently checks that directory's repository ownership. Preparation and admission both reuse the same incomplete check.

**Executed discriminator, ordinary filesystem permissions, effective UID 1000:**

1. Create a private throwaway home outside all repositories and a normal source product, with a fresh ledger destination. Inside the home, create `witness/demo` as an ordinary Git worktree, commit `sentinel.txt`, and retain its refs, object inventory and clean status. **This form uses no symbolic link anywhere in the operator tree.**
2. Set only `home/witness` to mode `0300` (owner write/execute, no directory-read permission). A real `iterdir` raises `PermissionError`; traversal through the known name `witness/demo` still works. No permissions or paths change during execution.
3. Actual `Home.check('demo')` accepts. Actual `prepare_genesis` returns valid with no problems. Sign with the reviewer's throwaway SSH key and run actual `admit_genesis`.
4. Admission returns **`QUALIFIED`** and writes its complete checkpoint into the nested product worktree. The product's tracked sentinel, refs and existing Git objects stay unchanged, but its formerly clean status becomes an untracked SSDS checkpoint:

   ```text
   ?? 000000000000-6981401c02f983031241c06fba10c18e9c40cc37ab99c30cd16f45ec4488a06c.json
   ```

   Genesis, state, keys and ledger directories have also been created. Thus refusal did not precede effects, and operator data entered a product repository.
5. With exactly the same repository layout and normal readable mode `0700`, preparation refuses the nested repository before creating any of those four operator directories; product state remains unchanged.

**Sibling closure of the cause.** A second realization puts `witness/demo` as a symbolic link to another ordinary product directory **inside the same home**. Resolved paths remain inside the home. Readable mode refuses; mode `0300` again prepares and admits `QUALIFIED`, publishing a checkpoint in that product. Separately, an inaccessible used workspace, state, admission-key or ledger tree containing a hidden symbolic link is accepted by `Home.check`; each readable control refuses. These four siblings are validator observations, not claims of four additional demonstrated product overwrites. They establish one shared incomplete-scan cause.

**Boundary classification: in-boundary Phase D blocker.** The first trajectory needs no links, hostile actor, concurrent replacement, mount/bind alias, global Git configuration, cache rewriting or broken filesystem primitive. The operator's static permission/layout misconfiguration suffices. The second demonstrates the same hole in SD-59's no-symlink predicate. A private trusted home can be misconfigured; SD-59 explicitly undertakes to detect this class before effects. Earlier permission-related coverage limits are superseded here by an executed counterexample, not converted into Phase H exclusions.

**Minimum repair.** Make the existing structural validator fail closed when it cannot enumerate or establish the relevant used tree. Propagate enumeration failures as a visible pre-effect refusal; do not certify an unvisited subtree as clean or compensate only at named checkpoint files. Preserve fresh ledger construction, the ledger repository exception, atomic complete publication, normal external homes and the allowed linked-home control. The repair belongs to the existing Home validation owner and does not require a new authority, registry or D3 exception.

**Discriminator to retain.** Keep the real permission-limited `witness/demo` repository and the in-home-link sibling through prepare/sign/admit. Require visible refusal before workspace/key/state/ledger creation and before any nested-product bytes, refs, objects or status change. Include readable collision refusal, a clean admitting control and a scan-error negative for the other used trees. The supplied candidate tests all pass despite the demonstrated defect, so they do not yet discriminate this property.

A bounded lower-boundary experiment made the existing walk raise `HomeRefused` on an enumeration error, without changing any other Home or Admission behavior. Both permission-limited trajectories then refused with no product change and no new workspace/key/state/ledger directory. This is diagnostic evidence for the owning cause and minimum repair, **not an implemented candidate fix**. The experiment used a temporary test patch only; candidate source remains byte-identical.

## Phase H items — outside SD-59

Hostile account/home writers; concurrent check/write path replacement; mount/bind aliases; hostile global Git configuration/templates/hooks; filesystems defeating exclusive-create/link/rename/fsync; coherent private-cache rewriting; exhaustive crash, power-loss and storage-exhaustion qualification; hostile witness transport; and confidentiality/authentication/custody attacks remain Phase H items. None was established qualified here. The kernel file-size-limit cases exercise honoring an ordinary short-write return, not exhaustive fault qualification. The permission blocker above exercises a standard directory-enumeration failure, not an exotic filesystem or an adversarial replacement.

## Non-blocking finding

### NF8 — F8 still conflates some execution order and binding semantics

At `orchestrator/tests/ssds/fitness.py:245`, an annotation without a value is treated as a rebinding. At lines 274–284, all nested scopes, including class bodies, are analyzed against final enclosing bindings. Through the full checker on otherwise clean synthetic repositories:

| Ordinary code after `import ssds.content as c` | Expected F8 | Actual F8 |
| --- | --- | --- |
| `c: object` followed by `x = c.read_tree` | yes; a module annotation with no value leaves the imported binding intact | no |
| `class K: x = c.read_tree`, then module-level `c = None` | yes; the class body runs before the rebinding | no |
| define `f` returning `c.read_tree`, call `f()`, then `c = None` | yes; the earlier call reaches the forbidden reader | no |
| inside `f`, read `c.read_tree` before local `c = None` | no reachable imported reader; Python raises `UnboundLocalError` | yes |

The runtime binding behavior was corroborated with harmless synthetic modules, and the three NF7 controls pass. No forbidden Git reader, filesystem read, dynamic import or equivalent path was found in actual production derivation; its trees remain supplied by callers. The Manual explicitly calls fitness checks sensors. Consequently these are bounded sensor limitations, not a production purity defect or an independent Phase D blocker. Any future strengthening should repair ordinary binding/evaluation handling at this checker, without advertising complete Python dependency analysis or reintroducing the corrected pure-code false positives.

## Handoff §3 judgments

1. **Every b341109 finding:** disposed above. A-B11/A-B13 and named NF7 cases close; A-B12's broader protected outcome remains blocked. Each changed repair's retained discriminator was mutation-tested.
2. **Qualification:** within the exercised static model, H* is the highest quorum-held prefix whose own recovery records explain every observed checkpoint and retained W. Recovery outside H* contributes no abandonment. Both lifecycle kinds were run over real signed Git histories: G0/E1/rewind/uncheckpointed recovery refuses (`FORK`, no current head), then acknowledgment gives current recovery at 1. A later witnessed ordinary entry was lost after the first recovery; a second, uncheckpointed recovery could not borrow its effect into H*=1; acknowledgment qualified at 2. Rewinding past the first recovery and abandoning that recovery did not inherit its explanation of the original E1; explicitly naming all known abandoned heads restored qualification. Ordinary `ROLLBACK` and non-authoritative `BEHIND` controls pass; retained `FORK`, `RETIRED`, read-repair and genuine provisional-successor tests pass. Ninety bounded holder/read/fault configurations across LOCAL_TRUST, TEAM and HARDENED never qualified an older head after an admitted successor; read repair yielded head 1 in all. The actual consumer derives only the qualified prefix. These tests grant the recovery inputs at the qualifier boundary; they do not establish general recovery human authorization, control/witness re-establishment or known-loss classification of a purported `FORK_RESOLUTION`. Those remain later-phase integration obligations, not benefits inferred from these read-path probes.
3. **Structural guarantees:** grammar, resolved containment, ancestor repository exclusion, fresh-ledger refusal and complete atomic publication hold in the inspected named paths. The assembled guarantee fails because repository and no-symlink validation can silently skip a used subtree. Every demonstrated unsafe route is in-boundary; the separate Phase H list names the excluded routes. A `.git` file is a conservative gitfile marker, a `.git` directory with HEAD is a repository marker, and HEAD/objects/refs detects the ordinary bare layout. An empty `.git` directory is not itself a repository and is correctly admitted. Twenty-seven additional readable repository placements (three real forms at nine locations) refused without changing their files; nine empty-marker controls prepared. The marker predicate is suitable for these ordinary layouts; incomplete traversal, rather than its marker vocabulary, is the demonstrated bypass.
4. **Repair-created defects:** no new checkpoint publication blocker found. Complete progressing writes, same-name byte equality, no replacement, and failure cleanup pass at the actual writer. Injected zero progress, write failure, file-fsync failure and link failure publish no checkpoint and leave no temporary. A directory-fsync failure propagates after a complete file has been linked; it is visible failure, not a promise to undo publication. Same bytes retry successfully; different bytes or a symbolic-link checkpoint name refuse unchanged. NF8 records the remaining order/scope issue.
5. **Inherited judgments, A7/A8 and step 7:** reconciled below. The clean exit realization passes; overall implementation and Phase D exit remain NO-PASS due to retained A-B12.

## Inherited findings and obligations

| Earlier finding | Current disposition |
| --- | --- |
| 0e49deb SC-1 and B-B1 | Resolved by SD-58/A8 and corrected A7 supersession/home text; exact Manual blob unchanged. No new upstream contradiction established. |
| 0e49deb A-B1 | Qualification precedes consumer derivation; actual consumer tests cover missing checkpoints, rollback and H*-only current answers. |
| 0e49deb A-B2 | Declared/distinct witness filtering and model validation pass; foreign report keys cannot manufacture a quorum. Transport identity qualification remains later work. |
| 0e49deb A-B3; 517af45/137b763 continuations | Grammar, traversal, named file/parent/internal-Git links and pre-existing ledger layouts refuse; atomic replacement protects existing hard-linked file objects. The no-link family is still subject to the incomplete-enumeration blocker, rather than unconditionally certified closed. |
| 0e49deb A-B4 | Missing file, heading, symbol and anchor terms refuse; present empty files and valid empty prefixes pass. |
| 0e49deb N1 | Cache checksum detects accidental corruption, not coherent private-cache rewriting; discard/rebuild on doubt. Stronger trust qualification remains Phase H. |
| 0e49deb N2; 517af45 NF1; 137b763 NF4; d8bdfd3 NF6 | Named direct/facade/dotted/relative reader, pure-attribute, scoped-import, disjoint-parameter and assignment-alias cases remain corrected. NF7 named cases also close; NF8 bounds sensor adequacy. |
| 0e49deb N3 | Home-resident ledger/witness/W backup and restore consequence remains disclosed in the first-day guide. Product clone alone is insufficient. |
| 517af45 A-B5; 137b763 A-B7 | Consumer retains qualified W; ordinary retained-floor and stale-restore tests pass. Remembered qualification is not conditional on successful rendering. |
| 517af45 A-B6 | Positive `COMPLETENESS/COMPLETE` guard remains; INCOMPLETE cannot bound a permissive reproduction. Removing the guard fails its retained test. |
| 517af45 NF2 | Catalogue `bound(o,K)`, membership, premise support edges and polarity agree with SD-58. Cited-premise admission-cycle enforcement remains Phase F. |
| 517af45 NF3 | File-witness retirement is wired to actual consumer qualification; authenticated creation/retirement custody remains unqualified later work. |
| 137b763 NF5 | W is last head qualified (§23.4), even if a missing analyzer later withholds derivation. Conservative early remembrance is not itself a false-current route. Concurrent-reader/crash monotonicity is not qualified. |
| d8bdfd3 A-B8 | Existing-file hard-link write-through is closed by fresh exclusive temporary plus rename; retained API/CLI controls pass. It does not excuse publication into an undiscovered repository directory. |
| d8bdfd3 A-B9 | No observed-checkpoint lag allowance remains. Observed floor, TEAM read repair and genuine unwitnessed provisional controls pass; the plan's old allowance is withdrawn. |
| d8bdfd3 A-B10 | Home-inside-worktree/bare-repository cases refuse before creation, with linked external-home positive control. Descendant ownership remains blocked by A-B12. |

### All eleven original implementation questions

| 0e49deb handoff §3 question | Judgment |
| --- | --- |
| 1. Scope/owners | Repair production delta is confined to Home/genesis and ledger qualification/publication; sensor changes are tests. Content/analyzers and derivation are unchanged by this repair. Accepted component ownership is preserved; no out-of-register mechanism found. |
| 2. Readings | All sixteen separately reconciled below; no reading supplies permission for incomplete tree validation. |
| 3. Fail-closed deferrals | Native D1/D2 gates await revision runs; plan reach is conservative; unavailable declarative verdicts do not support. General admissibility is Phase F and item views Phase E. No repair makes those pending surfaces supported. |
| 4. Expected values/discriminators | Register/Stage S expectations remain literal inputs rather than model-generated production answers; F13 passes. Repair mutations discriminate. Supplied properties omit unreadable-tree traversal, which the new independent trajectory falsifies. Deferred cases remain unexecuted. |
| 5. Fitness | Real-tree and synthetic acceptance passes. Named NF7 controls close; NF8 limits the sensor. B1 cannot establish destination ownership or scan completeness. |
| 6. Determinism/replay | Seeded generated histories, record permutation, historical-prefix equality, checkpoint-key/body refusal and incremental/from-scratch properties pass, including F/P/T coverage. No hostile-cache or production-scale qualification inferred. |
| 7. Ledger/qualification | Signature/key/prev/Git-parent/schema/halt/CAS and loss-bound tests pass. Recovery-prefix ordering and new publication semantics pass their bounded probes. Broader recovery authorization remains later work. |
| 8. Shadow boundary | Clean runs preserve source product refs/objects/status and use only a dedicated ledger ref with LEGACY/UNGOVERNED modes. Retained A-B12 falsifies unconditional static containment under a permitted permission misconfiguration. |
| 9. Core preservation | 393 Core tests across 13 modules pass, including independently built/installed wheel and sdist acceptance. Twenty-two frozen resource files are R100 renames with identical blobs. Source/dist/Architecture 1.6.0 are unchanged. No exhaustive pre/post-rename behavior differential claimed. |
| 10. First release | Python 3.11 install, help/doctor, no-write doctor, absolute home override, first-write/composition/collision cases pass. No predecessor migration or alias introduced. Misconfigured uninspectable homes must still refuse before effects. |
| 11. Step 7 | Public evidence and Case B manifest reviewed; candidate-history prepare/sign/admit/derive reproduced, current at 0 with zero findings/obligations and correct shadow modes, source refs/objects/status unchanged. This establishes the clean path and recorded historical gate, not global containment or overall exit. Private historical custody was not inspected. |

### Every Phase D plan §8 reading

| Reading | Disposition |
| --- | --- |
| 1. Bounding currency | SD-58/A8's standing/content-at-K/other-premises-in-evaluation split is preserved; genuine-fix/revert, challenge, membership and cited-record tests pass. |
| 2. Policy schema | Closed per-domain data tables remain delegated; absent holders confer no authority. |
| 3. Default subject mode | Explicit `"*"` binding keeps later subjects UNGOVERNED in shadow. |
| 4. Admission body | Integration/adopted-delta facts feed S0; general admission enforcement remains Phase F. |
| 5. Judgment domain | Domain follows judged content, including changed transformation units, rather than target representation. |
| 6. Assessment home | File-overlap widening is conservative; arbitrary fine regions/move tracking are not claimed. |
| 7. Execution basis | Recorded closed execution fields are consumed; their runtime truth/custody is later qualification. |
| 8. Forced components | All forced nodes remain F; ordinary versus integrity classification changes attention only. Retained support/mutual-acceptance tests pass. |
| 9. Requalification | Retained/in-effect, withheld and fresh-record cases pass; complete item workflow remains Phase E. |
| 10. Views | Historical/frame/halt/unreadable-schema/missing-analyzer withholding and actual H*-only consumer tests pass. |
| 11. Checkpoints | Keyed S0 fold plus accidental-corruption detection and recomputed S1–S3 remains bounded private-cache evidence; caller cadence/storage and hostile coherent rewriting are not newly qualified. |
| 12. Home layout | Delegated layout is coherent; scan completeness fails at Home.check, retained A-B12. Complete atomic file publication is separately corrected. |
| 13. Trees | Caller tree injection and public baseline-structure derivation preserve Admission's component boundary. |
| 14. Refusals | Named manifest/static/mode/policy/key/witness/existing-ledger cases pass, including empty-present controls; incomplete subtree enumeration remains a missing refusal. |
| 15. Human gate | Exact proposal digest/SSHSIG/registered-key checks and altered-key/message/proposal negatives pass; only reviewer-generated private keys used. |
| 16. Admitted | Clean genesis durably checkpoints, qualifies at 0 and stores W; complete-write acknowledgment now holds. Clean admission does not establish safe placement for an unscanned witness tree. |

A7's four inherited questions remain satisfied within the unchanged text: SD-56/SD-57 fidelity, sibling naming/configuration/composition/supersession alignment, frozen/Core/dependency invariants and disclosed first-release/home-custody costs. A8 preserves adverse/permissive polarity and the accepted bounding rule; loss of completeness cannot create new permissive support. Technical text Review creates no stakeholder acceptance.

**Explicitly unexecuted later obligations:** Phase E retains the D1/D2 revision-run variants of 575dc78 N5, f7419d5 N4 and f22b4dc N5; 63ddf91 N5's plan-amendment/tightening half; f03b15e N5's reassessment of an answered non-gate obligation; and item readiness/discharge/drift/impact/conformance/brief/routing/re-application views. Phase F retains 51070e5 N3's adjudication-independence refusal, f03b15e N5's supersession-authority refusal, other §8.3 steps 3/7 refusals, cited-premise admission-cycle checks, RR-11 resolver/Dispatcher behavior, designated-runner materialization/custody, general recovery authorization/control re-establishment and authenticated retirement. Migration/cutover, campaigns and Phase H qualification remain unexecuted. None defers the demonstrated pre-effect validation defect.

## Verification and evidence limits

Accepted executions used **Python 3.11.15** and the exact candidate. Dependencies were supplied from locally cached distribution wheels into a review-owned virtual environment; the candidate wheel was built/installed. Core independently built and installed wheel and sdist products. The host's empty `/tmp/.git` remained present throughout.

| Check | Executed result |
| --- | --- |
| `python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt` with scoped offline inputs | PASS |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | PASS, 225 tests; full restored-source rerun also 225 PASS |
| `python orchestrator/scripts/run_core_tests.py` | PASS, 393 tests / 13 modules |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | PASS |
| `python -m unittest discover -s tests -v` | PASS, 435 tests, 3 opt-in skips |
| `python3 -I qualification/ssds80/models/run_models.py --seeds` using the review interpreter | PASS; settled cases/seeds and intended refutations, including 14,508 routing answer chains |
| `git diff --check e88d90de df911c04` | PASS |
| Source/dist/frozen `orchestrator/docs/architecture.md` versus baseline | No changed paths; byte-identical Git blobs |
| Frozen packaged profiles/prompts and snapshots | 22 R100 resource renames, identical blobs; snapshot canonicality PASS |
| Validation dependencies, release-state and PEM schema | PASS; PEM schema 1, 5 families, 0 notices |
| Fresh canonical package build, independent validation, committed distribution parity | PASS; committed dist matches fresh build semantically |
| Candidate-history shadow genesis, real script and reviewer SSH gate | PASS clean path; current H*=0, no findings/obligations; source refs/objects/status unchanged |
| New permission-limited ownership discriminator | **FAIL at candidate**, both direct nested repository and in-home-link forms admit and write product state |
| Mutation/source restoration | Five known-wrong source variants detected; source restored byte-for-byte; isolated candidate tracked diff empty |

The three repository skips are opt-in exact-ref remote fallback realizations for 6.2/6.3/6.4, unexecuted rather than passed. Their identities did not change. Suite success is structural/diagnostic evidence, not proof of semantic adequacy or safe traversal.

**Mutations executed:** whole-chain rather than prefix-local abandonment (two failing recovery subcases); removal of descendant repository exclusions (four failing placement subcases); unchecked single write (all three complete-write tests fail, including real kernel-limit cases); prior fitness map (retained NF7 discriminator fails); and removal of the positive COMPLETE guard (INCOMPLETE discriminator fails). Mutations ran against explicit candidate source imports, sequentially, and were restored after each. The scan-error refusal experiment was a separate sixth behavior variant at the walk boundary, not a candidate repair. Other historical mutation families were not all repeated.

**Step 7 provenance:** the historical public evidence binds baseline `9bf199120f7f289f10994189d1bd718690653dfc`, signed genesis digest `sha256:d7514f67a1071f6e008766a57a8c79d7ca88a434eddf19867194546b6b2e9a22`, and entry commit `980373b80a9a0af8487bc3fece16d948e9d2ab74`. Fresh reproduction used this candidate's history and manifest with a new reviewer key. Its qualified entry digest was `sha256:537ddc4a0b7a38ce56bb917dc20978fc5f4ddb389f2ba502f0041429c0e60817`. The three subjects were protocol/manual LEGACY and program UNGOVERNED; all `valid=F`, expected without admitted acceptances. This reproduces the mechanism and reviews the public historical record; it does not retake the stakeholder's gate or establish independently administered witness-medium custody.

**Setup-only failures, corrected:** offline wheel filename reconstruction initially omitted universal compatibility tags and dependency resolution failed before installation; corrected inputs installed normally. An initial restored-suite invocation resolved the wrong `tests` package from its working directory; rerunning from `orchestrator/` with explicit source imports passed all 225. A scratch probe's final fitness-report print had a duplicate argument name after its recovery/placement/writer probes had completed; the seven fitness cases were rerun in a separate successful script. None is counted as a candidate defect or a successful check before correction. No incomplete required prescribed check remains hidden behind those corrections.

Reproduction routes under the scratch root: `run_checks.py`/`checks.json` and `logs/` (prescribed checks); `extra_checks.py` (package/release/PEM validation); `probes.py` and `logs/probes.log` (signed recovery, readable placement and checkpoint failpoints); `fitness_probes.py`/`logs/fitness.log`; `quorum_probe.py`/`logs/quorum.log`; `mutations.py` and per-mutation logs; `history_genesis.py`/`logs/history.log`; and, decisively, `scan_discriminator.py`/`logs/scan-discriminator.log` plus the first `unreadable_tree_probe.py` realization. Scratch is cold supporting evidence, not another repository deliverable; the decision-changing inputs and outcomes are preserved in this record.

## PEM applicability

PEM activates through the explicitly memory-bound workplan and repeated containment-repair Review. Project policy designates integrated `main`; the workplan independently pins base `af0455753e20ee54a969c844872e29e270007211`, and local `main` resolves there. Its PEM and candidate PEM are byte-identical, blob `1561797125622f355f84eb27319f87e8fa4227d9`. Schema/publication metadata and canonical metadata of all five families were inspected, including UNASSESSED/summary-omitted material. There is no branch-memory byte overlay to compose. Historical overlay prose cannot self-ratify another overlay; coverage remains PARTIAL.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: SD-56, Manual 26.4 and G2 independently require frozen resources and version-bound Core preservation; exact resource blobs and actual Core/package checks pass.
  - id: DS-001
    disposition: APPLICABLE
    reason: All supplied structural and fixture suites pass while a real permission-limited Home and Admission trajectory violates placement; direct owner evidence controls the verdict.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No source router or generated-route repair is in scope.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No immutable protocol fallback publication is in scope.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: Premature immutable bootstrap publication is not the mechanism under review.
```

PC-001 derives force from current independently resolved owners, not memory. No memory update, accepted-repair recurrence count or plan archival was performed. These remain sibling failures within an unaccepted Phase D cycle.

## Scientific checks and common-mode note

- **Material findings:** retained A-B12 blocks implementation and exit; NF8 limits the sensor. No accepted-authority SERIOUS CHALLENGE established. A-B11/A-B13 and named NF7 repairs pass their bounded discriminators.
- **Realized scientific results:** none produced, run or reviewed. Null scientific-result envelope: no physical experiment, scientific dataset, trained model, numerical estimator result or scientific-result population was examined. Engineering evidence comprises synthetic histories, signed throwaway Git ledgers, actual filesystem/permission/short-write operations and public historical gate evidence. This Review prepares engineering gate evidence only.
- **Variants evaluated:** five known-wrong source variants plus one temporary scan-error-refusal behavior variant; two lifecycle kinds over six reported recovery stages each; 90 holder/read/fault configurations across three declared deployment classes, each with a read-repair control; 36 readable placement configurations (three real repository forms and an empty-marker control at nine locations); nine checkpoint publication/failure/existing-name configurations; seven scope/order snippets; two permission-limited repository/link trajectories each with readable and scan-error-refusal controls; and four further unreadable-tree/no-link predicate siblings with readable controls. The initial mode-0333 link realization preceded the final mode-0300 paired discriminator; it is supporting exploration of the same failure, not a separate defect. Kernel-limit and other retained-suite subcases are not recounted as independent reviewer-designed variants. Criteria were admissible currentness, pre-effect repository/link exclusion, complete durable publication and correct allowed/forbidden dependency discrimination. No scientific parameter survivor was selected; earlier author search history was not reconstructed or counted.
- **Tension search:** no consequential judgment relied on accepted scientific D1/D2 authority; no D1/D2 tension-search result is claimed. Qualification, identity, recovery and containment meanings were resolved at their engineering owners.
- **Gaps:** private historical custody and separate witness administration; opt-in remote fallback executions; general recovery authorization/control re-establishment and authenticated retirement; later E/F/G/H obligations, campaigns and native cutover; exhaustive crash/hostile-environment/scaling qualification; exhaustive Core pre/post-rename differential behavior; and complete Python dependency analysis remain unexecuted or unestablished. None is reported passed. The new mandatory static refusal is demonstrably absent, not merely untested.

Different model family strengthens process diversity, not epistemic independence by itself. This Review still shares the candidate source, accepted Manual/register, Python/Git/filesystem and many test fixtures with the author and earlier Reviews. Independent counterexamples, actual source-history genesis, ordinary kernel permission/short-write behavior and known-wrong mutations supply distinct evidence routes, but do not prove absence of all defects. Green suites and the clean historical record cannot override the executed product-write counterexample.

**Nothing beyond shadow is authorized.** This NO-PASS does not permit Phase E's dependent work, G3 acceptance, stakeholder amendment acceptance, native authority/G4, cutover, publication, live agent campaigns or measurement spend. Repair and a fresh independent Review are required for the blocked Phase D outcome.
