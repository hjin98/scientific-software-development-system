# Independent Review — SSDS 8.0 Phase D, candidate d8bdfd3

```text
GOVERNING SSDP: 7.2.1
PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY: hjin98/scientific-software-development-system
BRANCH: ssds-8.0-graph-native-architecture
CANDIDATE: d8bdfd3efa233fec8d7fd8a83803bca1ba77584b
PREVIOUS CANDIDATE: 137b7633945c1a52cc8a590a5fbf07402f57d982
BASELINE: e88d90dec4143340fffcf5cd53e7de5167d46be0
SCOPE: Phase D implementation and exit; every 137b763 finding; repair siblings;
       inherited handoff obligations; confirmation of A7 and A8 text verdicts
MANUAL BLOB: 6226f323365966bbcf653545f3a35b1fd7d6e060
PHASE D PLAN BLOB: c1c1923011d567edd8bc5d70f3106263884ffc37
G2 WORKPLAN BLOB: 523464de8ad6ec45379bad7e49660a471868cf49
CATALOGUE BLOB: f4c515bb1c3d7d5cdc3b762a18dcf2f67bbe5341
REVIEW METHOD: independent owner reconstruction; bounded Challenge Pass;
               real prepare/sign/admit/derive trajectories; physical write
               probes; signed-chain quorum probes; controlled mutations;
               prescribed suites, package and frozen-resource checks
REVIEWER: GPT family; engaged through Codex CLI in the stakeholder's own terminal
          at the stakeholder's request. The author's session typed only the
          pointer prompt and did not frame the candidate otherwise. This
          reviewing context did not author the candidate. No subagents used.
```

The governing task is `PHASE-D-IMPLEMENTATION-REVIEW-HANDOFF-SSDS-8.0-D8BDFD3.md`. The requested branch was checked out at `84369491c1ab57e4836f9e834e3c6cb24dc75166`, newer than the candidate. Review execution used an archive of the exact candidate, with scratch Git metadata and read access to the original object store. No newer implementation was substituted. The implementation and design roles were entered at the pinned public source, with the abstraction/concretization, specification, architecture, workflow, testing, definitions, evidence, security, convergence and applicable PEM owners. The Manual, SD-56–SD-58 and the G2 register supplied authority; prior Reviews, tests, models, plan readings and the handoff supplied hypotheses and evidence.

Review exports, fixtures, generated keys, homes, scripts and retained logs are under `/tmp/ssds80-phase-d-review-d8bdfd3`. The stakeholder's private ledger and private keys and `~/.ssds` were neither read nor written. Existing untracked repository files were preserved. This file is the sole authored repository deliverable; no implementation repair, commit or push was made. A setup deviation concerning pip's initial ephemeral temporary directories is disclosed under verification limits.

## SERIOUS CHALLENGE

**None established against accepted authority.** The blockers below violate coherent existing owners. In particular, Manual §23.1 and §23.4 consistently require the qualified head to extend every observed checkpoint as well as the retained mark. The Phase D plan's provisional-checkpoint allowance and its test oracle do not amend that contract. A fresh evaluator's inability to prove that a newer checkpoint has reached a quorum requires withholding currentness or successful read repair, not permission to assert an older head current. Likewise, the stakeholder's no-symlink policy is an admissible restriction; its implementation does not establish the stronger required ownership of every write. These are D4 conformance/adequacy-of-concretization failures, not grounds to weaken A7, A8 or the Manual.

## Verdict

**Phase D implementation and exit: NO-PASS. Neither the implementation nor the Phase D exit passes.** The named symlink and retained-mark counterexamples from `137b763` are repaired. Three independently executed sibling failures remain: hard-linked operator outputs overwrite product files (A-B8); partial-quorum reads qualify an older head despite observing a newer admitted checkpoint (A-B9); and an SSDS home inside the product repository is accepted (A-B10). Positive suite and step-7 results cannot close these boundaries. Phase E's dependent work cannot start under G2 §5.1 item 5 on this record.

**A7 PASS confirmed. A8 PASS confirmed.** The Manual is byte-identical to the blob passed at `517af45` and confirmed at `137b763`. Its one-program/Core/home/supersession statements agree with SD-56/SD-57, and its standing/matched-content/evaluation-state split agrees with SD-58. The implementation failures below supply no basis to withdraw those technical text verdicts. Stakeholder acceptance of the amendment text and G3 acceptance remain separate.

## Disposition of every 137b763 finding

| Finding | Disposition at d8bdfd3 |
| --- | --- |
| **A-B3 — internal Git symbolic links** | **The named static symlink/pre-existing-repository routes are closed. The governing write-containment outcome remains open through A-B8 and A-B10.** Real preparation and admission refuse bare repositories whose `objects` or `refs` point outside the home, including `refs` into a throwaway product's `.git/refs`. Refusal also holds when planted after preparation/signing. Outside directories and product refs, object inventory and status remain unchanged. Existing non-symlink repositories, including one with `objects/info/alternates`, are refused by the fresh-repository rule. Retained tests exercise linked witness/state directories, a nested witness link and leaf files. Removing the tree walk or reverting the complete family repair makes the retained discriminator fail. A clean home reached through a link still prepares, signs, admits and derives. This closes the specified symlink mechanism, not all filesystem aliasing or every possible Git execution environment. |
| **A-B7 — current H* below retained W** | **Named defect closed.** The retained real CLI test runs chain=1/W=1, removes only checkpoint 1, requires exit 1 and `UNQUALIFIED`/no current assertion, checks W is unchanged, then restores checkpoint 1 and gets current head 1 again. The qualifier also preserves mark-past-chain `ROLLBACK`/`BEHIND` and the never-witnessed provisional-successor control. Removing the retained-floor filter makes both the qualifier and CLI tests fail. This is not complete closure of §23: A-B9 concerns an observed checkpoint when W is absent or old. |
| **NF4 — alias overwritten by an unrelated scoped import** | **Named false negative closed; sensor limits remain.** The old module-global `c=ssds.content`, function-local `c=collections` example now reports F8. Reverting the alias map makes its retained discriminator fail. Direct, module, dotted and both relative routes still report F8. The original pure-attribute control remains clean. A new disjoint-scope false positive and a simple assignment-alias hole are NF6 below. |
| **NF5 — mark raised before successful presentation** | **The plan's revised reading is correct.** Manual §23.4 calls W the last head *qualified*, not the last head successfully rendered as a current assertion. A fresh signed/witnessed head 1 adopting an unavailable analyzer qualifies and raises W to 1; derivation then withholds the assertion and exits 1. This conservatively remembers qualification and is not itself a blocker. It does not justify any older current H*. |

The distinction matters: A-B3 and A-B7's original executed discriminators pass, but the corresponding global containment/currentness outcomes are not fully established. These remain findings in an unaccepted Phase D cycle, not claims of recurrence after an accepted repair.

## Blocking implementation findings

### A-B8 — Regular-file hard links redirect operator writes into product files

**Owner text.** SD-56 item 3 and Manual §26.3 require everything SSDS writes for an operator to live in the SSDS home outside product/program repositories. G2 §5.1 item 2 and Phase D step 6 protect governed files in shadow; the plan's step-6 contract says nothing is written to the product. This governs actual file effects, not only the pathname supplied to `open`.

**Actual owners.** `admission/genesis.py:Home._file` and `Home.check` reject symbolic links and escaping resolved paths, but accept multiply linked regular files. `_write_private` at lines 208–214 uses `O_TRUNC | O_NOFOLLOW`, which still truncates the shared regular-file object. `ledger/qualification.py:HighWaterStore.set` at lines 155–166 likewise truncates a predictable existing `high-water.tmp` before replacing the mark. The later `os.replace` does not undo the outside write already performed through that temporary file.

**Executed static trajectories.** All paths and effects below were in reviewer-owned throwaway fixtures. No path was replaced concurrently, no production owner was mocked, and the SSDS home was outside the throwaway product.

| Existing regular-file alias before the operation | Actual candidate result |
| --- | --- |
| Hard-link `home/genesis/demo/report.json` to the product's tracked `guide.md`; then real `prepare_genesis`, reviewer SSH signature, `admit_genesis` and derivation | `Home.check` accepts; preparation is valid; admission is `QUALIFIED`; derivation is current. Preparation replaces the product file's bytes with validation-report JSON. Product state changes. The file has link count 2. |
| After clean genesis, replace `home/genesis/demo/derivation.json` with a hard link to the product's tracked `manual.md`; run the actual `derive` CLI | Exit **0**, `QUALIFIED` at 0, current assertion **true**; the product file is overwritten with derivation-report JSON. |
| After clean genesis, hard-link `home/state/demo/high-water.tmp` to the product's tracked `manual.md`; append a valid signed successor, witness its checkpoint and run the actual `derive` CLI | Exit **0**, `QUALIFIED` at 1, current assertion **true**; the product file is overwritten with high-water JSON. |

Thus the no-symbolic-link rule is satisfied while a governed product file is written. A fresh ledger repository does not protect pre-existing workspace/state file objects. This sibling is not excluded by the handoff's exclusion of concurrent replacement.

**Minimum repair.** Reconcile write ownership in the existing Home/private-output and high-water publication owners. Existing-file identity must not permit truncating an object also named outside the operator tree. A shared safe replacement strategy or conservative refusal of unsafe existing file identities can satisfy this without another output-name exception list. Any replacement must itself create a fresh file safely; retaining a predictable truncating temporary file preserves the demonstrated escape. Preserve ordinary preparation, report updates, high-water monotonicity and a home reached through a link. This Review does not select or implement the repair.

**Discriminator.** Retain all three real-owner/CLI hard-link trajectories. Require refusal before product modification, or safe publication that leaves the outside file byte-identical if that policy is chosen. Compare product bytes, refs, object inventory and status, and an outside sentinel. Pair each with normal single-link preparation/derivation/high-water updates. The candidate fails the protected outcome in every demonstrated hard-link variant.

### A-B9 — An observed newer checkpoint is treated as a provisional exception, permitting stale currentness

**Owner text.** Manual §23.1 says a current-qualified head extends “every checkpoint and high-water mark the evaluator observes.” Section 23.4 defines H* as the highest quorum-held entry that extends every observed checkpoint and W; §23.5 applies this to fresh readers with no W. The accepted catalogue §23 repeats the same contract, and G2 §4.2 accepts it. The soundness argument relies on any read quorum observing at least one honest holder of each admitted head. It does not require that every read quorum itself contain an admission quorum of that head's holders.

**Actual owner.** `ledger/qualification.py:qualify`, lines 241–246, still allows `p >= floor - 1` and `p >= m or m == p + 1` for observed checkpoints. The repair adds a strict filter for the evaluator's own retained mark only. The Phase D plan §6's reconciliation and `test_ledger.Qualification.test_qualification_states` bless the same checkpoint allowance; they are not authority to relax §23.

**Executed trajectory at the real qualifier with a signed Git chain.** A fresh human-signed genesis declares a valid `TEAM` model `(N,q_a,r,f)=(3,2,2,0)` and three declared GIT witnesses `w0,w1,w2`. A valid signed successor gives chain head 1. The chain reads back authenticated, without halt. Witness retention is:

| Witness | Durably retained checkpoint positions |
| --- | --- |
| w0 | 0 and 1 |
| w1 | 0 |
| w2 | 0 and 1 |

Head 1 is admitted by the declared quorum `w0+w2`. All three witnesses are honest; none is rolled back. A read gets `w0+w1`, which is a valid read quorum, while w2 is unavailable. The real `qualify` returns:

```text
W absent: QUALIFIED, head=0, provisional=1, critical=()
W at 0:   QUALIFIED, head=0, provisional=1, critical=()
W at 1:   UNQUALIFIED
all three reports available: QUALIFIED, head=1
```

Checkpoint 1 is authentic and observed. H*=0 does not extend it, and the already admitted entry 1 is wrongly labeled provisional. There is no witness fault, no rollback, no path race and no new deployment-class assumption. The witness sets are explicit inputs at the qualifier's declared read boundary; no future GIT transport is claimed qualified by this probe.

The entry-1 digest in this realization was `sha256:9ccb7ab5c3dbfb1b2e7d80da9bfc7ba8e1833c02d01470ae0e3823887ca04576`, commit `7112812a6aa1e446bf1555fb498e86d8c6df2a7f`. The specific random genesis/signatures are not needed to reproduce the discriminator.

**Consequence and classification.** A fresh evaluator, or one whose W is still 0, can claim stale state current within the declared fault model. The successful A-B7 repair only protects a participant that already remembers 1. This is a newly discovered surviving sibling in the unchanged checkpoint allowance, not a regression introduced by the strict retained-mark filter. The earlier Review's acceptance of that allowance is withdrawn to this extent. The Manual remains coherent: withhold currentness until a confirmable H* extends the observed checkpoint, or perform read repair and qualify again.

**Minimum repair.** Remove the one-position exception for observed, unabandoned checkpoints in the existing qualifier; reconcile plan §6 and the wrong test expectation with the owning contract. Preserve a genuine provisional successor when it has not produced an observed checkpoint requiring a later H*, preserve the repaired W floor and mark-past-chain classifications, and preserve admitted abandonment handling. Read repair may restore availability; an older current answer is not a substitute.

**Discriminator.** Retain the exact three-witness trajectory, with W absent and W=0: require no current head 0 (`UNQUALIFIED` without successful read repair). Then add the newer checkpoint to enough responding declared witnesses and require current head 1. Pair it with an appended successor never witnessed by any responder, which legitimately leaves H*=0/provisional=1, and with W=1 refusing an older answer. Add a property that every successful H* extends every applicable observed checkpoint and W. A scratch corrective perturbation enforcing the observed-checkpoint floor causes the supplied `test_qualification_states` to fail its `QUALIFIED@5` expectation when checkpoint 6 is observed; that exposes an incorrect oracle, not evidence against the Manual's requirement.

### A-B10 — A repository-local SSDS home is accepted

**Owner text.** SD-56/SD-57 and Manual §26.3 place operator data outside every product/program repository. G2 §5.1 item 1 says it is “never in a repository.” Absolute-path configuration is not permission to override this boundary.

**Actual owners and trajectory.** Core's `ssds_home` and `admission/genesis.py:Home` require an absolute root; Home checks descendants relative to that root. They do not establish that the resolved root is outside a product/program repository. On a fresh throwaway product, set `SSDS_HOME` to `<product>/operator-state`. The actual prepare, reviewer signature, admit and derive path succeeds: exit **0**, `QUALIFIED`, current assertion **true**, with **89 operator files/directories** under the product worktree. No symbolic link or pre-existing ledger is involved.

**Minimum repair.** Validate the chosen resolved operator root at the existing configuration/Admission boundary before the first write, against the repository exclusion required by the current owner. A bad configuration must fail actionably without creating operator data in the product/program worktree. Preserve a valid external root and a link that resolves to one; do not add predecessor migration or another configuration authority.

**Discriminator.** With a clean product and no home, choose a home inside its worktree and require refusal before creating any operator artifact; compare product refs, objects, files and status. Pair with an outside home, including a linked path to that outside home, that still admits and derives. This is a separate root-placement defect from A-B8's file-object aliasing; both are pre-existing siblings exposed by the bounded containment pass.

## Non-blocking finding and bounded family answer

**NF6 — The scope-conservative reader map has a new false positive and still is not a complete dependency analysis.** Through the real full fitness checker on its clean synthetic repository, this pure code reports F8 on `c.read_raw`:

```python
def f():
    import ssds.content as c
    return c.TreeView

def g(c):
    return c.read_raw
```

`g`'s parameter is unrelated to `f`'s local module binding. The map deliberately merges those scopes. Therefore the handoff's “no new false positive on pure code” question has a negative answer. The original pure `Snapshot.read_raw` case without that unrelated binding remains clean. Conversely, `import ssds.content as c; reader = c; value = reader.read_tree` receives no violation: assignment aliasing is outside this import map. The named old scoped hole and all five direct/module/dotted/relative routes are detected. No actual forbidden production Git read was found. This remains a sensor finding rather than a failing production dependency/build. Narrow scope resolution at this checker if repaired; do not promote “conservative, never blind” into a purity guarantee.

**The family rule and threat model.** At the inspected owner, the new walk checks each containing component below the home and every descendant of the ledger repository, witness, admission keys, this ledger's workspace and state trees. It does not follow directory symlinks, and refuses the symlink entries themselves. The pre-existing-repository refusal prevents writing through its alternates or repository configuration as well as its internal symlinks. The repeated check precedes the first Git write. The supplied nested/parent/leaf checks, custom internal-Git probes, existing-alternates refusal and linked-home positive control support that bounded static symlink policy. They do not establish ownership of regular-file objects or exclusion of repository-local roots, as the blockers demonstrate.

Concurrent replacement between checking and writing is explicitly outside the handoff's static rule. No concurrent adversary is needed for any blocker here. Protection against such an actor would require a stronger declared filesystem/process boundary than a preflight walk; this Review neither qualifies it nor makes a new Phase D concurrency requirement. Mount/bind aliases, hostile global Git templates/configuration/hooks, permissions preventing a complete tree walk, crash durability and hostile operator-state replacement were not exhaustively qualified. The rule cannot support an unbounded “every redirection route” claim. Phase H's broader security/fault qualification remains separate; it cannot defer the demonstrated static Phase D violations.

## Inherited findings and judgments

### Earlier findings

| Earlier finding | Current disposition |
| --- | --- |
| 0e49deb **SC-1** | Resolved at its owner by SD-58. A8's standing/content/premise split remains coherent; retained genuine-fix/revert, challenged-bound, membership and cited-premise tests pass. |
| 0e49deb **A-B1** | Original missing qualification is repaired: the consumer qualifies first and derives only H*. Complete currentness remains blocked by A-B9. |
| 0e49deb **A-B2** | Declared-identity filtering and model validation remain effective; foreign responders, duplicates and malformed quorum models fail closed in retained tests. Future transport authentication is not qualified here. |
| 0e49deb **A-B3**, 517af45 leaf continuation | Traversal, malformed IDs, escaping directories, leaf links and the 137b763 internal-Git routes are refused. The broader containment outcome remains blocked by A-B8/A-B10. |
| 0e49deb **A-B4** | Missing file/heading/symbol/anchor terms are refused; present empty files and empty prefixes pass. |
| 0e49deb **B-B1** | Corrected supersession-table/default-home statements are unchanged and agree with A7. |
| 0e49deb **N1** | Cache checksum is still accidental-corruption detection, not authentication of a coherently rewritten private cache. Plan reading 11 discloses it; stronger trust qualification remains Phase H. |
| 0e49deb **N2** | Named facade-reader dependency is detected. NF4's named scoped hole is repaired; NF6 bounds the sensor. |
| 0e49deb **N3** | Home-ledger backup/restore/requalification disclosure remains applicable; no disaster-recovery qualification is inferred. |
| 517af45 **A-B5** | The actual consumer retains its last qualified head, including the unavailable-analyzer NF5 case. Restore-both yields `ROLLBACK`; witness-only restore with W=1 now withholds currentness. Fresh/old-W partial-quorum currentness remains A-B9. |
| 517af45 **A-B6** | `COMPLETENESS/COMPLETE` is required before a bound is consumed. The negative-certificate test passes and fails when that guard is removed. |
| 517af45 **NF1** | Original unrelated attribute false positive is repaired; NF6 is the disjoint-scope limitation of the new map. |
| 517af45 **NF2** | Catalogue signature, positive-certificate guard, R1 explanation, matching polarity and cited-premise support edge agree with SD-58. The catalogue blob is unchanged from 137b763. The Phase F cited-premise admission-cycle check remains unexecuted. |
| 517af45 **NF3** | Retirement-marker-to-consumer wiring remains covered by the actual CLI test. Authentication and creation of a retirement statement remain later §24.2 work; an arbitrary marker test does not qualify them. |

### The eleven 0e49deb handoff §3 questions

| Question | Judgment at this candidate |
| --- | --- |
| **1. Scope and owners** | The repair's production delta is confined to Admission's Home/genesis and ledger qualification; the fitness delta stays in tests. Content/analyzers, ledger, derivation S0–S3 and Admission retain the Manual's ownership direction. Dispatcher/Interface remain later work. No new mechanism beyond the register was found in this delta. Its containment/currentness concretizations fail as above. |
| **2. Readings 1–16** | Individually disposed below. The separate plan §6 observed-checkpoint allowance is inconsistent with §23 and must be corrected; no plan prose or earlier Review promotes it into authority. |
| **3. Fail-closed deferrals** | NATIVE D1/D2 acceptance/gates remain unavailable until revision runs; plan reach is conservative; unavailable declarative verdicts do not support. Item-dependent S3 queries remain Phase E, general admissibility/custody Phase F. Their source is unchanged from 137b763 and retained tests pass. |
| **4. Expected values/discriminators** | Affected expectations are literal register/Stage S outcomes; F13 and the no-model-import checks pass. Mutations discriminate named repairs and the support clamp. A-B9 exposes a wrong qualification oracle despite the green suite. Not every original mutation was rerun, and later-phase cases remain unexecuted. |
| **5. Fitness** | F0–F13/B1 real-tree and synthetic suites pass. The alias repair detects every earlier named route. NF6 supplies both a false positive and a missed assignment-alias dependency; sensor success is not proof of purity or write containment. |
| **6. Determinism/replay** | Retained permutation, historical-prefix, checkpoint-key/body refusal, replay and incremental/from-scratch tests pass over the supplied generated histories. Derivation is unchanged by the repair. This does not authenticate a coherently rewritten cache or qualify production-scale performance. |
| **7. Ledger/qualification** | Signed-chain/key/prev/Git-parent/schema/CAS/witness persistence tests pass. W=1 rollback protection is repaired; A-B9 violates the observed-checkpoint half. A signed, verified chain carrying an admitted `FORK_RESOLUTION` naming an old mark is still consumed as abandonment; without it the ahead-of-chain mark gives `ROLLBACK`. Human authorization/admission of general recovery records is Phase F, not established by constructing such a record in this read-boundary test. |
| **8. Shadow boundary** | Clean genesis preserves product refs, objects and status; modes stay LEGACY/UNGOVERNED and the ledger ref is separate. The internal-Git symlink probes now refuse. A-B8 actually changes tracked product bytes; A-B10 writes operator state into the product. The complete boundary fails. |
| **9. Core preservation** | 393 tests across 13 modules pass, including fresh wheel/sdist installed-product acceptance and frozen-profile behavior. All 22 packaged profile/prompt resources are R100 renames with identical blobs. `source/`, `dist/` and Architecture 1.6.0 are byte-unchanged. No exhaustive pre/post-rename differential run over every configuration is claimed. |
| **10. First release** | Isolated Python 3.11 installation succeeds. Help/doctor, no-write doctor, absolute home override, first write, composition and collision tests pass. Python 3.11+ is documented/enforced, with no predecessor detection/migration/alias introduced. A-B10 limits first-day handling of an invalid home location. |
| **11. Step 7** | The manifest declares Case B section-level parts at legacy accepted scope without rewriting content. The public record binds the stakeholder's historical gate and baseline. Fresh candidate-history prepare/sign/admit/derive succeeds, current at 0 with zero findings/obligations and unchanged source-repository refs/objects/status. That positive evidence is adequate for the clean path, but the Phase D exit does not pass while the implementation blockers remain. Private present-day custody was not inspected. |

### Every Phase D plan §8 reading

| Reading | Disposition |
| --- | --- |
| **1. Bounding currency** | SD-58/A8 owns the matched-content and evaluation-state split. The positive-certificate guard and the standing/membership/cited-record tests pass; no new contradictory meaning was found. |
| **2. Policy schema** | Closed data-only per-domain tables are delegated concretization; missing holder data does not manufacture authority. |
| **3. Default mode** | Explicit `"*"` default, chosen UNGOVERNED in shadow; no silent inference of native authority. |
| **4. Admission body** | Integration/adopted-delta facts feed S0. General admission enforcement remains Phase F. |
| **5. Judgment domain** | Follows judged content, including the units changed by a transformation, rather than merely the target representation. |
| **6. Assessment home** | File-overlap successor widening is conservative; exact arbitrary move/region tracking is not claimed. |
| **7. Execution basis** | Closed recorded basis is the one consumer input; truth/custody of runner declarations remains a later boundary. |
| **8. Forced components** | Every forced node is F; ordinary versus integrity classification affects attention, not support. The support-clamp test passes and fails under an F-to-T mutation. |
| **9. Requalification** | Retained/current/withheld/fresh-record behavior passes its derivation tests. Full item workflow remains Phase E. |
| **10. Views** | Historical/frame/halt/unsupported-schema/missing-analyzer withholding remains effective in retained tests. Qualification outside derivation is separately blocked by A-B9. |
| **11. Checkpoints** | S0 cache with recomputed S1–S3 and ledger-derived key passes replay/resume checks. The body checksum is not authentication. Storage/cadence belongs to the later caller; hostile-cache qualification remains open. |
| **12. Home layout** | Layout is delegated and the no-symlink restriction is coherent. Physical file ownership and exclusion of a repository-local root fail A-B8/A-B10. |
| **13. Tree injection** | Caller-supplied content and public baseline-structure derivation preserve the component boundary; no new Admission content import. |
| **14. Genesis refusal** | Missing declaration terms/static errors, modes, manifest/policy/trust/witness validation remain covered; empty file/prefix controls pass. Existing ledger paths now refuse. These tests do not cover the new static alias/root failures. |
| **15. Human gate** | Proposal-digest/registered-key SSHSIG checks and altered-key/message/proposal refusals pass. Only reviewer-generated throwaway keys were used in new executions. |
| **16. Admission** | Clean genesis obtains a durable checkpoint, read-back qualification and W=0. Positive consumer behavior passes. It does not establish general write containment or the newer observed-checkpoint selection contract. |

For the present handoff §3: item 1's four findings are individually disposed; item 2's named static symlink family is repaired but the stronger outcome fails the sibling probes; item 3's retained-W repair passes while its scope-conservative sensor has NF6 and currentness still has A-B9; item 4's NF5 reading is faithful; item 5's inherited obligations stand only with the explicit qualifications above. A7's fidelity/siblings/invariants/cost judgments remain technically PASS on the unchanged Manual; A8's bounded decision remains PASS. Home backup/custody, fail-closed authorship and matching/reassessment costs remain disclosed limits, not new acceptance.

### Later discriminators remain unexecuted

Phase E retains the D1/D2 revision-run variants of 575dc78 N5, f7419d5 N4 and f22b4dc N5; the plan-amendment/tightening half of 63ddf91 N5; f03b15e N5's reassessment of an answered non-gate obligation; and item-dependent readiness/discharge/drift/impact/conformance/brief/routing and re-application views. Phase F retains 51070e5 N3's adjudication-independence refusal, f03b15e N5's supersession-authority refusal, the other §8.3 steps 3/7 admission cases, the cited-premise support-cycle check, RR-11 resolver/Dispatcher behavior, and designated-runner representation/materialization/custody. Migration/cutover, authenticated retirement, general Admission and crash/resource/hostile-transport qualification are not passed. None defers the concrete Phase D read/write defects found here.

## Verification, mutations and evidence limits

Execution used **Python 3.11.15** in an isolated environment, installing the exact candidate distribution with its declared development requirements. The initial host `python3` was 3.10.12 and was not used for accepted results. Its first pip attempt failed to obtain build dependencies; the corrected 3.11 installation succeeded offline using already available dependency wheels. Those dependency wheels were reused as package inputs, not as prior Review results.

**Setup deviation:** the initial pip setup attempts used pip's default ephemeral `/tmp/pip-*` build locations before `TMPDIR` was set to the review-owned `tmp/` directory. Later tests, builds, fixtures and probes used the scoped temporary root. This departed from the handoff's scratch-location instruction during setup; it did not access private SSDS state or change the candidate. The failed setup is not counted as a candidate failure or a successful required check.

| Check at exact candidate | Result |
| --- | --- |
| `python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt` (offline dependency selection added) | PASS on Python 3.11.15 |
| `python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v` | PASS: **215 tests** |
| `python orchestrator/scripts/run_core_tests.py` | PASS: **393 tests**, 13 modules, including installed wheel/sdist acceptance |
| `python orchestrator/scripts/generate_protocol_snapshot.py --check` | PASS: current snapshot canonical, historical snapshots immutable/coherent |
| `python -m unittest discover -s tests -v` | PASS: **435 tests, 3 skips** |
| `python3 -I qualification/ssds80/models/run_models.py --seeds` | PASS: settled cases/seeds, including 14,508 bounded answer chains; intended refuted readings remain detected |
| `git diff --check e88d90de d8bdfd3e` | PASS |
| `source/`, `dist/`, `orchestrator/docs/architecture.md` versus e88d90de | Zero changed paths, byte-identical |
| Frozen packaged profiles/prompts | **22 R100 renames**, identical blobs; snapshot check also passes |
| Release-state and PEM validation | PASS: coherent release state; PEM schema 1, 5 families, 0 notices |
| Fresh canonical skill build, independent validation, committed-distribution parity | PASS, outputs under review scratch |
| Candidate-history prepare/sign/admit/derive with a throwaway human key | PASS: QUALIFIED at 0/current, zero findings/obligations, correct shadow modes, source repository refs/objects/status unchanged |
| Restored-source focused regression after scratch mutations | PASS: **81 tests**; scratch candidate tracked contents match the pinned commit |

The three repository skips are opt-in exact-ref remote fallback realizations for Protocol 6.2, 6.3 and 6.4. They remain unexecuted, not passed; this delta changes no fallback identity. All prescribed commands executed successfully in the corrected environment. Structural/package/model success does not establish semantic adequacy or erase the failed custom boundary probes.

**Controlled code perturbations.** Six distinct known-wrong variants were executed, solely in the scratch candidate and restored afterward:

1. Remove the operator-tree link walk: retained family test fails.
2. Restore the preceding Home/genesis implementation: the retained internal-Git discriminator fails (with additional setup errors after the initial failed subcase); the initial assertion already establishes discrimination.
3. Remove the strict retained-W filter: both the qualifier and actual CLI witness-only-restore tests fail.
4. Restore the old alias map: the 33-test fitness suite has the named scoped-import failure.
5. Remove the COMPLETE-outcome requirement: the INCOMPLETE-bound discriminator fails.
6. Change support-cycle clamping from F to T: the mutual-acceptance discriminator fails.

A **seventh**, separately classified, corrective perturbation enforces extension of every observed checkpoint. It makes the supplied qualification-state oracle fail as described in A-B9; this is not counted as killing a known-wrong implementation. An initial mutation-script edit matched no COMPLETE guard and aborted before applying that variant; the corrected edit was then executed and discriminated. An initial full-checker probe omitted two required arguments and was rerun correctly. Neither setup error is a candidate observation. Not every mutation performed by earlier reviewers was rerun, and no prior mutation score is reused as current evidence.

**Step 7 provenance.** The historical stakeholder record names baseline `9bf199120f7f289f10994189d1bd718690653dfc`, signed genesis digest `sha256:d7514f67a1071f6e008766a57a8c79d7ca88a434eddf19867194546b6b2e9a22` and entry commit `980373b80a9a0af8487bc3fece16d948e9d2ab74`. This Review judged that public evidence record and manifest rather than inspecting private current operator state. The new reviewer-controlled run used the exact candidate baseline, signed digest `sha256:9b10610ef6d0181dd0d967b9764ce51b8a6a1d921a9605640e96c3c138181562`, entry digest `sha256:62aba9d7d9476a49511c13bd18d40fbabf996da2697877220c8284549ad55951` and entry commit `e2dfeff786746916ad3050c404143fef03b68688`. Its only ledger ref is `refs/ssds/ledger/ssdp-shadow`; it does not retake the stakeholder's gate or establish witness-media independence by placing a throwaway witness in scratch.

**Cold reproduction routes.** The retained candidate tests are the durable starting points: `test_admission_genesis.Refusals.test_no_symbolic_link_anywhere_in_the_operator_tree`, `test_shadow_genesis_script.ShadowGenesisScript.test_a_witness_only_restore_never_presents_an_older_head`, `test_ledger.Qualification`, `test_fitness`, `test_assessment.BoundingCurrency` and `test_support.SupportCycles`. Reviewer scripts/logs are `probes.py`/`probes.log` (hard-link effects), `boundary_probes.py`/`boundary.log` (old internal-Git routes, linked home, NF5), `quorum_probe.py`/`quorum.log`, `sibling_probes.py`/`siblings.log` (root placement and abandonment consumption), `fitness_probes.py`/`fitness-probes.log`, `mutations.py`, `mutations_tail.py` and their per-variant logs, and `history_genesis.py`/`history.log`, all under the scratch root named above. Scratch is reproducibility support, not a required permanent repository artifact; the inputs and observed outcomes needed to assess each blocker are stated in this record.

## PEM applicability

PEM activates because the workplan explicitly binds it and this Review examines sibling failures after repeated repairs. The workplan independently selects accepted/base publication `main@af0455753e20ee54a969c844872e29e270007211`; the actual repository's local `main` resolves to that identity. Its PEM blob and the candidate's are both `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no additional branch-memory delta to compose. Schema/publication metadata and canonical metadata for all five families, including summary-omitted/UNASSESSED material, were inspected. Historical front-matter overlay wording does not self-ratify a new overlay; the integrated exact publication is the selected base. Coverage is PARTIAL, not evidence of historical absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: SD-56, the Manual and G2 independently require frozen version-bound behavior; exact resource identity and Core acceptance test preservation.
  - id: DS-001
    disposition: APPLICABLE
    reason: Green matrices miss actual file-object writes and a valid read-quorum trajectory; real-owner counterexamples determine closure.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No canonical routing or generated-route defect is being repaired or accepted.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No protocol successor public-fallback publication is in scope.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: Its premature immutable-fallback publication mechanism is not these filesystem or qualification defects.
```

PC-001's present force comes from the independently resolved current owners, not its memory temperature or old binding. No PEM update, repair acceptance, occurrence count or lifecycle closeout was performed. These probes characterize sibling mechanisms within the still-open Review cycle; they do not manufacture multiple accepted-repair recurrences.

## Scientific checks and common-mode note

- **Material findings:** A-B8, A-B9 and A-B10 block implementation and exit. NF6 limits the fitness sensor. Named 137b763 repairs pass their discriminators; NF5 is the Manual's qualification-based reading. No new accepted-authority SERIOUS CHALLENGE was established.
- **Realized scientific results:** none produced, run or reviewed. Null scientific-result envelope: no physical experiment, scientific dataset, trained model, numerical-estimator result or scientific-result population. These are engineering realizations over source text, synthetic histories, signed throwaway Git ledgers and the public historical genesis record.
- **Variants:** **six known-wrong code perturbations plus one corrective perturbation**; **nine fitness input variants**; **four static ledger-layout variants** (objects link, refs link, product refs link, pre-existing alternates); **four additional containment inputs** (three hard-linked output sites and one repository-local home); **five TEAM qualification input configurations** (full reports, partial reports with no W, partial with W=0, never-witnessed successor, partial with W=1); **two abandonment read configurations** (before/after the admitted resolution); **one unavailable-analyzer NF5 configuration**; and a linked-home positive control. Criteria were exact write ownership/shadow boundaries, extension of observed checkpoints/W, and allowed versus forbidden dependency meaning. Full-history clean genesis is a separate positive control. Supplied suite subcases/seeds are not recounted as reviewer-selected designs. No scientific parameter survivor was selected and no author's search history is claimed reconstructed.
- **Tension search:** no consequential judgment relied on accepted scientific D1/D2 authority; no D1/D2 tension-search result is claimed. Specialized support, matching, identity and qualification meanings were resolved at their D3 owners.
- **Gaps:** private current operator state and historical gate custody were not independently authenticated; remote fallback opt-ins and the explicitly deferred E/F/H cases remain unexecuted; general recovery/retirement human authorization, simultaneous readers, crash durability, hostile Git/filesystem environments, resource/scaling qualification and exhaustive old/new Core differential behavior were not qualified. These limits are not converted into PASS.

This is a different-family Review with process independence, not automatic epistemic independence. Manual/register text, Python, Git, cryptography, the fixture builders and transcribed Stage S cases are common dependencies. The mutation and boundary probes retain actual production owners but share some supplied setup helpers. Distinct evidence routes include physical tracked-file effects, full CLI trajectories, a valid honest-witness quorum-intersection trajectory, independent source-to-generated checks and corrective perturbation of an erroneous test oracle. The fresh-read counterexample specifically rejects a premise the preceding Review accepted; earlier reports and memory did not determine this verdict. The bounded Challenge Pass found D4 violations without a surviving contradiction in accepted A7/A8 authority. Further broad defect hunting cannot change this NO-PASS and has stopped at these decision-sufficient boundaries.

Nothing beyond the already authorized **shadow** scope is authorized. This record grants no Phase E dependent-work start, amendment-text stakeholder acceptance, G3 acceptance, campaign spend, publication, native governance or cutover. The named stakeholder gates remain controlling.
