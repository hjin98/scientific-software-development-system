# Independent Review — SSDS 8.0 Phase D, candidate b341109

```text
GOVERNING SSDP: 7.2.1
PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
CANDIDATE: b341109a6a23340692d0d7cddfd918666c6d2495
PREVIOUS CANDIDATE: d8bdfd3efa233fec8d7fd8a83803bca1ba77584b
BASELINE: e88d90dec4143340fffcf5cd53e7de5167d46be0
SCOPE: Phase D implementation and exit; d8bdfd3 findings and repair siblings;
       inherited Phase D judgments; unchanged A7/A8 text confirmation.
       SD-59: trusted private operator home; static misconfiguration/accidental
       aliasing, repository exclusion, no operator-tree symlinks, fresh genesis
       repository, atomic replacement, ledger-id grammar and path containment.
       Hostile account/home writers, check/write races, mount/bind aliases,
       hostile global Git configuration/templates/hooks, filesystems defeating
       the primitives and coherent private-cache rewriting are Phase H.
       Qualification remains unconditional within the declared witness model.
MANUAL BLOB: 6226f323365966bbcf653545f3a35b1fd7d6e060
PHASE D PLAN BLOB: 76c09ecd09873bebca7599889f3d2da5fe8485c8
G2 WORKPLAN BLOB: 523464de8ad6ec45379bad7e49660a471868cf49
CATALOGUE BLOB: f4c515bb1c3d7d5cdc3b762a18dcf2f67bbe5341
REVIEW METHOD: independent owner reconstruction, bounded Challenge Pass,
               actual prepare/sign/admit/derive and filesystem effects,
               authenticated Git chains and witness reports, kernel short-write
               realization, controlled mutations, prescribed acceptance checks
REVIEWER: GPT family; engaged through Codex CLI in the stakeholder's own terminal
          at the stakeholder's request. The author's session typed only the
          pointer prompt and did not frame the candidate otherwise. This context
          did not author the candidate. No subagents used.
```

The named handoff is `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-HANDOFF-SSDS-8.0-B341109.md`. The checked-out branch was at `a7cc8a7288c4fbf959be4002fa31da00362dab12`; execution used an archive of the exact candidate, subsequently supplied with isolated Git metadata and read-only access to the original object store. Newer implementation was not substituted. SSDP implementation and design entrypoints were entered at the public source, with the abstraction/concretization, specification, architecture, workflow, testing, evidence, definitions, security, storage, convergence, Python and applicable PEM owners. The accepted Manual, G2 register and SD-56–SD-59 govern; handoffs, earlier Reviews, plan readings, tests and models were treated as hypotheses/evidence.

Scratch, throwaway keys, homes, mutations and logs are under `/tmp/ssds80-phase-d-review-b341109`. The stakeholder's private ledger, keys and `~/.ssds` were not inspected or written. Existing repository work was preserved. This record is the sole repository deliverable; no implementation repair, commit, push, publication or stakeholder acceptance was performed.

## SERIOUS CHALLENGE

**None established against the accepted Manual, G2 contract or SD-59 boundary.** The three blockers below violate coherent existing requirements. SD-59 permits a bounded static defense and does not authorize writing a product file merely because a misconfigured repository is below the home. The existing write owner can refuse that collision without changing the boundary. Likewise, an authenticated but unwitnessed recovery entry is not admitted authority for discarding observed history, and a successful low-level write need not have written the entire buffer. None requires an adversary, a race, a mount alias or a filesystem violating its primitives.

The out-of-matrix pass held the protected outcomes fixed and ignored the supplied test decomposition: actual repository-file effects, recovery authority before witness admission, and the bytes actually retained by successful persistence calls were the discriminators. No surviving upstream contradiction was needed to explain the results.

## Verdict

**Phase D implementation and exit: NO-PASS. Neither the implementation nor the exit passes.** The named A-B8/A-B9/A-B10 counterexamples are repaired, and NF6's two named cases are corrected. Three sibling defects remain: an unwitnessed recovery record can make an older head current; a nested repository in an operator workspace can have tracked content overwritten; and short writes are published/acknowledged as complete durable state. Passing suites and clean step-7 reproduction do not close those defects. Phase E's dependent work cannot start on this record under G2 §5.1 item 5.

**A7 PASS confirmed. A8 PASS confirmed.** The Manual is the exact previously passed blob, unchanged since `517af45` and the subsequent confirmations. A7's composition/name/home/first-release and supersession statements still agree with SD-56/SD-57; A8's standing, matched-content membership/content and evaluation-state premise split still agrees with SD-58. Implementation defects do not withdraw those technical text verdicts. Stakeholder acceptance of their text and G3 acceptance remain separate.

## Disposition of every d8bdfd3 finding

| Finding | Disposition at b341109 |
| --- | --- |
| A-B8, hard-linked outputs | **Named mechanism closed.** Real prepare/sign/admit with `report.json` hard-linked to tracked product content preserves bytes, refs, object inventory and status. The actual CLI also preserves the product through linked `derivation.json`, the old `high-water.tmp` trajectory and an additional link at the actual `high-water.json` while advancing to head 1. All CLI controls return 0/current. Fresh exclusive creation plus replacement breaks the output name's link without writing through the shared object. Retained Admission and CLI tests discriminate the repair; the atomic-writer mutation fails the retained test. This does not close A-B12's repository placement collision or A-B13's incomplete publication. |
| A-B9, observed newer checkpoint | **Named floor defect closed.** On a real signed TEAM chain, head 1 held by w0+w2 and read w0+w1 yields `UNQUALIFIED` with W absent and W=0; read repair gives head 1; a genuinely unwitnessed successor leaves head 0/provisional 1. The corrected oracle and property test pass, and relaxing the floor kills the retained discriminator. A-B11 exposes a separate premature-abandonment path that removes checkpoints/W before this correct floor is computed. |
| A-B10, home inside a repository | **Named ancestor-placement defect closed.** Worktree-local, Git-directory-local and bare-repository-local homes refuse before the proposed home exists. A linked home resolving outside prepares successfully. Retained API/CLI tests pass; removing the root check fails the retained discriminator. A-B12 concerns a repository nested below an otherwise valid home, not an ancestor of it. |
| NF6, disjoint scopes and assignment alias | **Both named cases corrected.** The disjoint pure parameter case has no F8, and `reader = c; reader.read_tree` reports F8, including through the full checker. Reverting the map fails the retained NF6 discriminator. NF7 below shows remaining ordinary Python scope/order limitations; no production derivation Git access was found. |

## Phase D blockers

### A-B11 — An unwitnessed recovery record suppresses observed admitted history and W

**Owner text and scope.** Manual §23.1 requires H* to extend every observed checkpoint and high-water mark. Section 23.4 permits an **admitted abandonment record**, labels the single provisional successor non-current, and forbids assertions beyond H*. Section 23.6 makes a known-admitted abandonment a `LEDGER_LOSS`. These same requirements are in catalogue §23 and the settled G2 register. The handoff expressly keeps currentness and admitted abandonment in Phase D's read-path Review. General recovery authorization is later work; consuming its purported effect before witness admission is already a read-path defect.

**Actual owner.** `ledger/qualification.py:202–210,241–266`: `_abandoned(chain, top)` consumes lifecycle records through the replica's entire authenticated suffix **before** identifying a quorum-held head. It removes their named digests from both observed checkpoints and the retained mark. Its docstring calls these records admitted, but chain signature verification alone does not establish admission.

**Executed discriminator, using real Git and signed checkpoints, one honest LOCAL_TRUST witness `(1,1,1,0)`:**

1. Append genesis G0 and checkpoint it. Append ordinary entry E1, checkpoint it at the same witness, qualify at 1, retain W=(1,E1).
2. Rewind the reviewer-owned replica to G0 while retaining both witness checkpoints and W. Qualification is `ROLLBACK`, as required.
3. Append a host-signed, schema-valid `LEDGER_LOSS` L1 over G0, naming retained G0 and abandoned E1. Its actor is the genesis human identity. Do **not** checkpoint L1. Read back the chain: no halt. The witness still honestly holds G0 and E1; it has never acknowledged L1.
4. Candidate result: **`QUALIFIED`, head 0, provisional 1, no critical obligation**. The unwitnessed L1 has suppressed E1's checkpoint and W, and the old prefix becomes current.
5. Now durably checkpoint L1 at the witness, retaining E1's checkpoint too. Candidate result: `QUALIFIED` at L1/head 1. This is the positive admitted-recovery control; this Review does not establish the later general human-gate/report-admissibility machinery.

The realization's G0 digest was `sha256:831091122e8ddab4173a69447914a3827b94c8a2fddb5f3e753d1dcff0910668`, E1 `sha256:617295a2ca35215f699412308827426f7cb30b420e9475819a4af948d1b74441`, and L1 `sha256:22c339a0a5dede5c83428a2cffb9e8eb5873a092f92ea0eeac90c42ed8687e6c` (commit `393cb3e7bbba9e422fd851ae8462e6795aaf6178`). Simpler signed read-boundary variants with both lifecycle kinds likewise suppress an ahead-of-chain mark from an uncheckpointed suffix. The full trajectory above avoids depending on an invented historical checkpoint.

**Classification:** in-boundary Phase D blocker. No witness faults, hostile account actor, cache rewrite or filesystem redirection is involved. Even granting perfect human authorization of L1 does not make it witnessed/admitted. The qualifying H*=0 does not contain the resolution on which its qualification depends.

**Minimum repair.** Re-derive the existing qualifier's recovery/admission ordering: only a recovery record established admitted at the selected qualified prefix may justify disregarding old checkpoints/W. Do not infer admission from signature, suffix presence or the very abandonment exception being justified. Preserve admitted recovery and ordinary floor/read-repair/provisional/FORK/ROLLBACK/BEHIND/RETIRED behavior; do not add a second currentness authority.

**Retained discriminator needed.** Keep the complete G0/E1/rewind/uncheckpointed-L1 trajectory at the real qualifier. Require no current answer at G0 before L1's quorum acknowledgment, then current L1 after acknowledgment. Pair both `LEDGER_LOSS` and `FORK_RESOLUTION` read cases with legitimate admitted-abandonment controls and a property excluding a recovery outside H* from H*'s qualification premises. The supplied floor property is too narrow: it never varies abandonment authority.

### A-B12 — A repository nested in the operator workspace is overwritten

**Owner text and scope.** SD-56 and Manual §26.3 separate operator state from product/program repositories; G2 §5.1 items 1–2 require operator data never in a repository and protect governed files in shadow. Phase D step 6 says nothing is written to the product. SD-59 includes static misconfiguration; it excludes hostile actors and races, not a repository accidentally placed at an operator workspace path.

**Actual owner.** `admission/genesis.py:Home.outside_repositories` checks the resolved **home and its ancestors** for repository markers. `Home.check` checks descendants for symbolic links and containment, but does not exclude a product repository occupying a workspace/state/key/witness write location. `write_workspace` then safely replaces a name that is itself a tracked product file. Atomic file-object isolation does not establish repository ownership of the destination name.

**Executed static trajectory:** choose a home outside all repositories; create an ordinary Git worktree at `home/genesis/demo`, with a committed `report.json` sentinel; retain a separate normal source product and a fresh ledger destination. `Home.check('demo')` accepts. Real preparation is valid, the reviewer signs its message, and real admission returns `QUALIFIED`. The nested repository's tracked `report.json` is overwritten by validation-report JSON; its working-tree state changes. There are **no symbolic links anywhere in the used operator tree**, no existing ledger repository, no hard link, mount alias, concurrent replacement, hostile hook or hostile global configuration. All four structural rules as presently implemented pass. This is an existing location collision, not an adversary modifying trusted state during execution.

**Classification:** in-boundary Phase D blocker. The repair fixes the named root-inside-product trajectory but does not close the protected repository-write outcome. SD-59 remains an admissible boundary: the missing exclusion belongs to the existing D4 destination-placement owner.

**Minimum repair.** Validate actual operator write locations against repository ownership, including a repository nested below the home, before the first effect. Preserve the deliberately fresh ledger repository as the ledger's own destination, normal external homes and a link resolving to such a home. Prefer one ownership rule over a list of special output names. This Review does not prescribe a new layout or implement the repair.

**Retained discriminator needed.** Put a pre-existing ordinary repository at a used operator subtree, commit a colliding output, and require refusal before its tracked bytes/refs/objects/status change. Include a product actually located at the colliding workspace and a clean external-home positive control. The executed unrelated-product collision already falsifies the rule's “every repository” scope; the selected source need not own the damaged file.

### A-B13 — Persistence treats a short write as complete success

**Owner text and scope.** Manual §23.4 requires retention of the last qualified head; §23.3 says witness acknowledgment means durable retention. SD-59's one atomic-publish writer replaces operator state with the intended new file, and the handoff §3 item 4 specifically asks whether `publish_private` preserves durability and failure cleanup. SSDP's storage/security owners require transactional publication of complete important state. Atomic rename of an incomplete buffer does not satisfy that contract.

**Actual owners.** `ledger/qualification.py:174` ignores `os.write`'s returned byte count, then fsyncs and replaces the old file. All workspace reports/proposals, generated host keys and high-water replacements delegate here. The sibling new-file witness writer, `ledger/append.py:write_checkpoint`, also performs one unchecked `os.write`, fsyncs, and returns success.

**Executed, without mocking the writer or kernel:** in a child interpreter on the ordinary scratch filesystem, set `RLIMIT_FSIZE=(1,1)` immediately before `HighWaterStore.set`. The old file is complete JSON. The real `os.write` writes one byte into the fresh temporary; fsync and rename succeed. **`set` returns normally, child exit 0, and the old mark has been replaced by exactly `{`.** Repeating at the real witness writer likewise returns normally/exit 0, leaves a one-byte `{` checkpoint file and yields **zero readable held checkpoints**. These are permitted short returns from the primitive, not a filesystem defeating it. The [Python `os.write` contract](https://docs.python.org/3.11/library/os.html#os.write) reports the actual byte count; it does not promise the whole buffer was retained.

A separate controlled one-byte write failpoint at the same lower boundary publishes `n` for requested `new-complete`, corroborating the path. In contrast, injected write, file-fsync and rename exceptions preserve the old destination and leave no temporary. The successful call order is file fsync → replace → directory fsync. A directory-fsync exception propagates after replacement, with no stale temporary; this is a visible durability failure, not a rollback guarantee.

**Classification:** in-boundary Phase D implementation blocker for successful publication/acknowledgment of incomplete state. The test changes an ordinary operator resource limit; it supplies no hostile writer, race or broken filesystem primitive. Exhaustive crash/power-loss/resource qualification remains Phase H. This finding requires honoring the primitive's normal return contract, not bringing that entire later qualification phase forward.

**Minimum repair.** In the existing complete-write/publish owners, account for the number of bytes actually written; finish the buffer or fail without publishing incomplete replacement state. Preserve file/directory fsync, exclusive creation, hard-link isolation and failure cleanup. Reconcile the same unchecked-write cause in witness creation so an incomplete immutable checkpoint is not acknowledged or stranded behind the existing-file early return.

**Retained discriminator needed.** Exercise a progressing short write and a short write followed by failure/zero progress at the production writers. Require either exact complete new bytes or a visible failure preserving the old mark; never successful one-byte JSON. For a checkpoint, success requires the complete authenticated checkpoint to read back. Keep the kernel file-size-limit case or an equivalent deterministic lower-boundary failpoint, and the existing hard-link/cleanup/fsync controls.

## Phase H items — outside SD-59, not Phase D blockers

The following remain Phase H's adversarial/fault qualification: hostile home/account writers, check/write path races, mount/bind aliases, hostile global Git configuration/templates/hooks, filesystems defeating exclusive-create/rename/fsync, coherent rewriting of private derivation caches, exhaustive crash/power-loss and storage-exhaustion behavior, and hostile transport/authentication/retirement/recovery custody. They were not claimed qualified here. The review's private filesystem view used mount namespaces only to remove a host test-environment marker; no blocker relies on a mount-alias attack.

Existing `write_checkpoint` files are trusted private state under SD-59; replacing them coherently by an actor is not a new Phase D attack claim. Recovery admission and loss-bound computation, however, remain subject to §23's read contract even under entirely honest witness reports, as A-B11 demonstrates.

## Non-blocking findings

**NF7 — The repaired fitness map still mishandles ordinary binding order and some Python scopes.** Through the full checker on clean synthetic repositories:

- `import ssds.content as c; x = c.read_tree; c = None` produces **no F8**, although the forbidden reader was reached before the rebinding. The checker applies all assignments before inspecting all attributes.
- With the same module import, `def f(snapshot): c: Snapshot = snapshot; return c.read_raw` produces **F8**, although the annotated local is a pure object, not the module. `AnnAssign` is not included in its local-binding map.
- A class-local module import is inherited into method analysis although unqualified names in a Python method resolve through enclosing function/global scopes, not the class namespace. A pure global object's `read_raw` therefore also gets F8 in the exercised class variant.

The named disjoint-scope, plain-assignment-alias and original pure cases now pass their intended positive/negative expectations. No forbidden reader was found in actual production derivation. The Manual calls these checks sensors; NF7 is a bounded sensor limitation, not grounds to declare the otherwise correct production dependency graph impure. Refine ordinary scope/order handling if repaired; do not advertise the map as complete analysis.

**Environment conservatism, non-blocking:** the host exposes an empty, read-only `/tmp/.git` directory. The lexical repository-marker check treats that as a repository despite the absence of Git metadata. This initially rejected every scratch home. Successful runs used a private filesystem view hiding that marker; no production code was bypassed or patched. Conservative refusal of an ambiguous marker is distinct from A-B12's acceptance of an actual nested repository.

## Inherited findings and handoff judgments

### Earlier findings

| Earlier finding | Current disposition |
| --- | --- |
| 0e49deb SC-1; B-B1 | Resolved by SD-58/A8 and the corrected A7 supersession/home text. Unchanged Manual and catalogue; no new upstream contradiction found. |
| 0e49deb A-B1 | Consumer qualifies first and derives only H*. Retained/current-prefix CLI tests pass. A-B11 means qualification can still select the wrong H* under premature recovery. |
| 0e49deb A-B2 | Declared witness identity filtering, distinct identities and model validation pass; foreign responder keys do not create a quorum. Future transport identity is not qualified. |
| 0e49deb A-B3; 517af45 and 137b763 continuations | Grammar/traversal, leaf/parent/nested/internal-Git symlinks and existing ledger repositories refuse. Retained family test passes and fails with its tree walk removed. Fresh repository construction prevents accidental pre-existing Git alternates/configuration/hard-link layouts from being written through. Global product-write containment remains blocked by A-B12. |
| 0e49deb A-B4 | Missing declared file/heading/symbol/anchor terms refuse; empty present file/prefix controls pass. |
| 0e49deb N1, N3 | Private-cache checksum is accidental-corruption evidence, not authentication; backup/restore/requalification disclosure remains. Stronger trust/recovery qualification is Phase H. |
| 0e49deb N2; 517af45 NF1; 137b763 NF4 | Named direct/facade/scoped-import/pure-attribute cases are corrected; NF6's named cases now corrected too. NF7 bounds current sensor adequacy. |
| 517af45 A-B5; 137b763 A-B7 | Consumer retains W; no older H* can pass the ordinary retained-floor path. CLI restore tests pass. A-B11 is the recovery-exception bypass of that protection. |
| 517af45 A-B6 | Only a standing `COMPLETENESS/COMPLETE` judgment bounds permissive use; the INCOMPLETE discriminator passes and fails with its outcome guard removed. |
| 517af45 NF2 | Catalogue's `bound(o,K)`, membership, premise support edge and matching polarity agree with SD-58. Later cited-premise admission-cycle refusal remains Phase F, unexecuted. |
| 517af45 NF3 | Actual CLI retirement-marker wiring remains covered. Authentication/creation of retirement statements remains later §24.2 work, not proven by an arbitrary marker fixture. |
| 137b763 NF5 | W means last head qualified, including qualification followed by derivation withholding for an unavailable analyzer. This conservative reading remains correct; successful rendering is not its trigger. |

### All eleven 0e49deb handoff §3 questions

| Question | Judgment |
| --- | --- |
| 1. Scope/owners | Production repair delta stays in Admission Home/genesis and ledger qualification/append; fitness changes stay in tests. Content/analyzers and S0–S3 are unchanged by this repair. No new out-of-register mechanism found. Defects are at current persistence/qualification/placement owners. |
| 2. Readings | All sixteen individually disposed below. Plan §6 correctly withdraws the old observed-checkpoint exception. |
| 3. Fail-closed deferrals | Native D1/D2 acceptance/gates await revision runs; plan reach remains conservative; unavailable declarative verdicts do not support. General admissibility/custody is Phase F; item-dependent queries are Phase E. No repair changes those paths. |
| 4. Oracles/discriminators | Expectations are literal register/Stage S outcomes, with no model import (F13). Named repair mutations discriminate once executed against source. Supplied properties miss provisional recovery and short-write publication. Later-phase cases are unexecuted, not passed. |
| 5. Fitness | Real-tree and synthetic suites pass; named NF6 cases close. NF7 demonstrates remaining false positives/negative through the complete checker. Static B1 does not prove destination ownership. |
| 6. Determinism/replay | Retained generated-history, record-permutation, prefix/historical, checkpoint-key/body and incremental/from-scratch tests pass. No production-scale or hostile-cache qualification inferred. |
| 7. Ledger/qualification | Signature/key/prev/Git-parent/schema/halt/CAS and ordinary qualification/loss-bound tests pass. Newer-checkpoint floor and ordinary states preserve their named cases. A-B11 violates admitted-abandonment ordering; A-B13 violates witness retention on permitted short writes. |
| 8. Shadow boundary | Normal genesis preserves product refs/objects/status; shadow modes and separate ledger ref hold. Named links/root cases close. A-B12 overwrites a tracked repository file under static misconfiguration; the complete boundary fails. |
| 9. Core preservation | 393 tests/13 modules pass, including fresh wheel/sdist installed-product acceptance. All 22 profile/prompt files are R100 moves with identical blobs. Frozen source/dist/Architecture 1.6.0 are unchanged. No exhaustive pre/post-rename behavioral differential claimed. |
| 10. First release | Python 3.11 installation, actual installed help/doctor, no-write doctor, home override, composition/collision and first-write tests pass. No predecessor migration/alias is introduced. Invalid ancestor placement now refuses; nested placement and incomplete writes still block reliability. |
| 11. Step 7 | Public record and Case B manifest reviewed; candidate-history prepare/sign/admit/derive reproduced with reviewer key, current at 0, zero findings/obligations, correct LEGACY/UNGOVERNED modes and source refs/objects/status unchanged. This closes the clean positive path, not the implementation blockers or Phase D exit. Private historical custody was not inspected. |

### Every Phase D plan §8 reading

| Reading | Disposition |
| --- | --- |
| 1. Bounding currency | Accepted SD-58/A8 split, including COMPLETE, standing, membership/content in K and other premises in evaluation state. Genuine-fix/revert and premise/membership tests pass. No reopened Challenge. |
| 2. Policy schema | Closed data-only per-domain tables are delegated; absent holders do not manufacture authority. |
| 3. Default mode | Explicit `"*"`, UNGOVERNED in shadow, preserves later-subject binding without implicit native authority. |
| 4. Admission body | Integration/adopted-delta facts feed S0; general admission enforcement remains Phase F. |
| 5. Judgment domain | Derived from judged content, including changed transformation units, rather than target representation. |
| 6. Assessment home | Conservative file-overlap widening; arbitrary fine region/move tracking not claimed. |
| 7. Execution basis | Closed recorded execution field is consumed; runtime truth/custody of declarations remains later work. |
| 8. Forced components | All forced support nodes remain F; ordinary/integrity classification changes attention only. Retained mutual-acceptance/support tests pass. |
| 9. Requalification | Retained/in-effect, withheld and fresh-record derivation cases pass; complete item workflow remains Phase E. A-B11 precedes this at currentness qualification. |
| 10. Views | Historical/frame/halt/unreadable-schema/missing-analyzer withholding remains. Consumer uses H*, whose recovery exception is blocked by A-B11. |
| 11. Checkpoints | S0 fold/key/body validation plus recomputed S1–S3 remains sound for accidental corruption; coherent cache rewriting stays Phase H. Caller storage/cadence remains later work. |
| 12. Home layout | Delegated structure and no-symlink restriction remain coherent. Named alias/root checks pass; destination repository ownership and complete durable publication fail A-B12/A-B13. |
| 13. Tree injection | Caller-provided trees and public baseline-structure derivation preserve Admission's component boundary. |
| 14. Refusals | Manifest/declaration/static/mode/policy/key/model/witness/existing-ledger cases pass, including empty-scope controls. They omit the nested-repository collision. |
| 15. Human gate | Exact proposal digest/SSHSIG/registered key checks and changed-key/message/proposal refusals pass. Only throwaway reviewer private keys used. |
| 16. Admission | Clean genesis checkpoints, qualifies and stores W=0; end-to-end control passes. Partial-write acknowledgment and premature abandonment remain blockers; normal success is not proof of those paths. |

A7's four inherited questions remain answered: decision fidelity; sibling composition/name/configuration/supersession consistency; unchanged frozen/Core/dependency invariants; and disclosed home backup/custody/first-release costs. A8's unchanged bounded rule preserves adverse/permissive polarity rather than silently treating a negative certificate as permission. Neither text verdict creates stakeholder acceptance.

### Explicitly unexecuted later obligations

Phase E retains D1/D2 revision-run variants of 575dc78 N5, f7419d5 N4 and f22b4dc N5; 63ddf91 N5's plan-amendment/tightening half; f03b15e N5's reassessment of an answered non-gate obligation; and item-dependent readiness/discharge/drift/impact/conformance/brief/routing/re-application views. Phase F retains 51070e5 N3's adjudication-independence refusal, f03b15e N5's supersession-authority refusal, other §8.3 steps 3/7 refusals, cited-premise admission-cycle checks, RR-11 resolver/Dispatcher behavior, designated-runner representation/materialization/custody, general recovery authorization and authenticated retirement. Migration/cutover and Phase H qualification remain unexecuted. None defers a Phase D qualifier or writer defect exercised above.

## Verification and evidence limits

Final accepted executions used **Python 3.11.15**. Declared dependencies were reused as offline package inputs from available wheels; the candidate distribution was rebuilt/installed, and Core independently built and installed wheel and sdist products. No prior Review result was substituted for a new realization.

| Check at exact restored candidate | Result |
| --- | --- |
| `python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt` with offline wheel selection | PASS |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | PASS, 220 tests; also rerun against restored source after mutations, 220 PASS |
| `python orchestrator/scripts/run_core_tests.py` | PASS, 393 tests across 13 modules, including installed wheel/sdist acceptance |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | PASS |
| `python -m unittest discover -s tests -v` | PASS, 435 tests, 3 opt-in skips |
| `python3 -I qualification/ssds80/models/run_models.py --seeds` using the 3.11 interpreter | PASS, settled seeds/cases, including 14,508 routing answer chains; intended refuted readings remain detected |
| `git diff --check e88d90de b341109a` | PASS |
| `source/`, `dist/`, frozen `orchestrator/docs/architecture.md` versus baseline | No changed paths; identical bytes |
| Frozen packaged profiles/prompts | 22 R100 renames, identical blobs; snapshot canonicality check passes |
| Release-state / PEM schema validation | PASS; PEM schema 1, 5 families, 0 notices |
| Fresh canonical skill build / independent validation / committed-dist comparison | PASS; fresh bundles/ZIPs structurally valid and committed distribution matches canonical build semantically |
| Real candidate-history genesis and derivation | PASS clean path, current head 0, zero findings/obligations, no product refs/objects/status change |
| Mutation restoration | Production/test source restored byte-for-byte to candidate; no implementation diff |

The three repository skips are opt-in exact-ref remote fallback realizations for 6.2/6.3/6.4, unexecuted rather than passed. No fallback identity changes in this delta.

**Environment/setup deviations, excluded from candidate verdicts.** Initial setup selected host Python 3.10 and failed dependency acquisition; it was replaced with 3.11 before accepted runs. That initial pip attempt used default ephemeral `/tmp/pip-*` paths before scoped TMPDIR was established, a scratch-location deviation. All subsequent setup/build/test/probe writes used the named review root. Initial archive-only Core/Git checks failed without local Git metadata, and repository tests failed with inherited `GIT_DIR` leaking into fixture repositories. The isolated archive was given its own metadata/object alternates and fixture Git discovery was restored. The empty host `/tmp/.git` marker was hidden using `bwrap` with the review-owned tmp view; the real Home checks then ran unchanged. Core's initial isolated build could not reach the package index; scoped offline wheels allowed the full build/install acceptance to execute successfully. These setup failures are not candidate failures or passes.

**Mutations:** six distinct known-wrong source variants were executed, restored and detected by retained tests: write through the old output object instead of atomic replacement; remove home ancestor-repository exclusion; relax the observed-checkpoint floor; restore the preceding scope map; remove the operator-tree walk; remove the COMPLETE-outcome guard. The first attempt mistakenly ran production mutations against the already installed unmodified package, so those apparent survivals were discarded. Corrected runs explicitly imported mutated source and every variant failed its intended assertion. A final full SSDS source run passed after restoration. A package install overlapping the initial scratch mutations was also discarded and rerun after byte restoration; no result from a mutated package is counted. Other original mutation families were not all repeated.

**Step 7 provenance:** the public record binds historical baseline `9bf199120f7f289f10994189d1bd718690653dfc`, genesis digest `sha256:d7514f67a1071f6e008766a57a8c79d7ca88a434eddf19867194546b6b2e9a22`, and entry commit `980373b80a9a0af8487bc3fece16d948e9d2ab74`. The fresh run used candidate `b341109a` as baseline, the candidate script/manifest and a new reviewer key, with operator home wholly in scratch. It reproduces the mechanism and shadow modes; it does not retake or authenticate the stakeholder's historical gate, inspect private custody or establish separate witness-medium administration.

Cold reproduction routes under the scratch root: `probes.py`/`probes.log` (hard links, nested repository, TEAM and simplified recovery, helper-scope probes, publication failpoints); `recovery_probe.py`/`recovery.log` (real admitted-history recovery discriminator); `extra_probes.py`/`extra.log` (kernel high-water short write, fsync/cleanup and home controls); `checkpoint_short.py`/`checkpoint-short.log`; `fitness_probes.py`/`fitness.log` (full-checker cases); `mutations.py` and six per-mutation logs; `history_genesis.py`/`history.log`; and the named acceptance logs. These are reviewer scratch support, not additional repository deliverables. Decision-changing inputs/outcomes are stated above so the record does not depend on retaining scratch.

## PEM applicability

PEM activates through the explicitly bound workplan and repeated sibling-repair Review. Project policy designates the integrated publication line, and the workplan selects exact base `af0455753e20ee54a969c844872e29e270007211`; local `main` independently resolves there. Its PEM blob and candidate PEM are both `1561797125622f355f84eb27319f87e8fa4227d9`. Schema/publication metadata and canonical metadata of all five families, including UNASSESSED and summary-omitted material, were inspected. There is no branch-memory byte delta to compose. Historical overlay prose does not self-ratify another overlay. Coverage stays PARTIAL and does not establish historical absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: SD-56, Manual 26.4 and G2 independently require frozen resources and version-bound Core preservation; exact blobs and actual Core tests checked.
  - id: DS-001
    disposition: APPLICABLE
    reason: Green fixture and floor properties omit real destination ownership, provisional recovery premises and actual complete persistence.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No canonical routing or generated-route repair is in scope.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No immutable protocol fallback publication is in scope.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: Premature public-source bootstrap publication is not the mechanism under review.
```

PC-001's force comes from current independently resolved owners, not memory. No memory update, accepted-repair recurrence count or lifecycle closeout was performed. These are sibling defects within an unaccepted Phase D cycle.

## Scientific checks and common-mode note

- **Material findings:** A-B11/A-B12/A-B13 block implementation and exit; NF7 limits the sensor. No accepted-authority SERIOUS CHALLENGE established. Named d8bdfd3 repair trajectories pass.
- **Realized scientific results:** none produced, run or reviewed. Null scientific-result envelope: no physical experiment, scientific dataset, trained model, numerical estimator result or scientific-result population. Engineering executions used synthetic histories, real signed throwaway Git ledgers/filesystem operations and public historical evidence.
- **Variants evaluated:** six known-wrong code perturbations; four hard-link output-site trajectories (report, derivation, old temporary and actual mark); four ancestor/link home-placement controls plus one nested-repository collision; four TEAM read configurations; three recovery input forms (two simplified lifecycle-kind cases and one real prior-admission/rewind/loss trajectory, with provisional/admitted controls); nine distinct scope/order snippets across helper/full-checker probes; and nine publication configurations (controlled short write, real high-water and checkpoint short writes, write/file-fsync/rename failures, successful fsync order, directory-fsync failure and normal complete publication through the positive controls). Criteria were protected write ownership, extension of observed history/W with admitted exception authority, complete durable bytes/visible failure and allowed versus forbidden dependencies. Suite seeds/subcases are not recounted as reviewer-selected designs. No scientific parameter survivor was selected; no author's search history is claimed reconstructed.
- **Tension search:** no consequential judgment relied on accepted scientific D1/D2 authority; no D1/D2 tension-search result claimed. Specialized qualification, admission, matching, identity and support meanings were resolved at their engineering owners.
- **Gaps:** opt-in remote fallbacks, private historical custody, general recovery human authorization, later E/F/G/H obligations, full crash/resource/hostile-environment qualification, production scaling and exhaustive old/new Core differential behavior remain unexecuted or unestablished. No gap is converted into a pass. Required prescribed local commands did execute successfully after environment correction.

This is a different-family Review with process independence, not automatic epistemic independence. Common dependencies include the Manual/register, Python, Git, cryptography, fixture builders and Stage S case transcriptions. Prior scratch scripts were inspected as reproduction scaffolding and adapted; their earlier results were not reused as candidate evidence. Distinct evidence routes include actual tracked-file effects, actual CLI reports, real authenticated witness histories and kernel-generated short returns; injected failures stay below the actual persistence owner. The initial wrong import target in mutation testing illustrates why execution identity matters and was corrected before accepting mutation evidence. Further speculative defect hunting cannot change this NO-PASS; the bounded family pass stops with the decisive owner-level defects and explicit limits.

Nothing beyond already authorized **shadow** work is authorized. This record grants no Phase E dependent-work start, amendment-text stakeholder acceptance, G3 acceptance, campaign spend, native governance, publication or cutover. The stakeholder's gates remain controlling.
