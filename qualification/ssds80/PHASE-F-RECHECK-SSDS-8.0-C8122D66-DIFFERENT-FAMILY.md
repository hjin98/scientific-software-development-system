Governing SSDP version: 7.2.1.

# Independent Phase F re-check — `c8122d66`

**Overall verdict: NO-PASS.** RC-C1 leaves FR-B1 incompletely closed: the classifier accepts incorrect obligation identities and identity-to-target bindings as the exact reserved-leaf repair. RC-D1 lets an interrupted, unfinished re-read comparison report PASS. The committed 11b report's actual observations remain correctly classified.

| Part of this handoff | Verdict | Decision |
|---|---|---|
| A — FR-A1 | **PASS** | Closed at the shared schema and authenticated object-layout owners; every changed site has discriminating evidence. |
| B — D-GRAMMAR-ENDPOINTS | **PASS** | The endpoint repairs preserve legal values; the DOTALL change handles newline-bearing paths correctly. No remaining reachable whole-value `$` endpoint defect was found in the audited source. |
| C — FR-B1 and re-frozen 11b | **NO-PASS** | RC-C1 blocks the fail-closed classifier claim. The population, retained run evidence, unchanged first 308 rows, and all 942 actual classifications pass this re-check. |
| D — retired tools and prepared re-read | **NO-PASS** | The tree containment remedy passes. RC-D1 blocks the prepared re-read's failure handling. This is prospective script review, not execution or closure of revision 72 step 5. |

**No new SERIOUS CHALLENGE.** RC-C1 violates coherent F123/F124 evidence requirements at their classifier owner; RC-D1 violates the re-read window's own completion contract. Existing **SC-U4** remains open at Manual §14.7/§0.6, routed through U4 and the Manual/ruleset acceptance process; it blocks template qualification/adoption and the affected G3 criterion, not this Phase F re-check. The prior review's part C, G2 revision 4, is not reopened.

This record accepts nothing. Acceptance of 11b and Phase F exit remains the stakeholder's. It supplies no authorization for a real-home re-read, campaign, native authority, cutover, publication or release. The disclosed root-regression failure over G2 revision 4's proposed status remains a blocking repository-acceptance check; this narrow review does not waive it.

## Identity and review boundary

- Reviewer: independent Codex/OpenAI-family context, 2026-11-01; no authorship of this candidate and no subagents. Engagement is the stakeholder's standing request for one other-family review per frozen candidate, launched through Codex CLI in the stakeholder's terminal. The author's session supplied only the pointer prompt. Author and same-family conclusions were tested as hypotheses.
- Local branch: `ssds-8.0-graph-native-architecture`. Envelope/HEAD: `23b551506b2d53fb96ba6b03345eb803403f76f4`. Handoff blob: `e22d7750e3dac807adea1288ff38b71a7ab6df95`.
- Re-frozen candidate: `c8122d66edbf7d19320f7b155e0c31033566b854`, tree `ae003285b6f2b6b4c8661ed312bfbcdf534f6ea0`; comparison source: `8cf829c34020ebffb5ad50ad7ba5b03343c005ce`. Independently confirmed `orchestrator/` delta: 14 files, +128/-27; candidate-to-envelope source delta empty.
- Accepted Manual remains blob `438cb113b155c2e79715430338a543615fa7f143`, unchanged across this source interval. Authority was reconstructed from the Manual, applicable G2 settled-register entries, Phase F F123-F125 and revisions 72-74, and stakeholder decisions including SD-93 through SD-95. The repository software-implementation entrypoint and applicable kernel, specification, workflow, testing, evidence, Python and PEM owners were read.
- `PROTOCOL-RELEASE-STATE.yaml` resolves accepted-current SSDP 7.2.1, public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`.
- Evidence/tool review uses the envelope versions. In particular, the re-read script was amended after the semantic candidate: reviewed blob `5896a80f41e69c3fa81dfd4c0c24265a650c59ae`. Its candidate-to-envelope change uses safe lookup for a newly encountered ledger in the diagnostic text; it does not change the program source. The 11b runner differs from its frozen predecessor only in its docstring and candidate constant. The classifier is unchanged since `eb6db6dc`, SHA-256 `ca490718d6b36e1411d9607b10f2cf9000652c9d4c4d084b619a05f353ba1144`.

## Blocker RC-C1 — obligation identities are checked against themselves, not their targets

**Location:** `qualification/ssds80/PHASE-F-DIFFERENCE-STUDY-CLASSIFY.py:55-64`, especially line 59 and the independently sorted target comparison at line 64. **Owner:** the F124 classifier's `repair_consequences`, constrained by F123's identity-preserving consequence report. The real report identity construction is `orchestrator/scripts/difference_study.py:143-145`.

The repair verifies `value.id == item.key` and that the eight `about` targets form the expected set. It never verifies that each identity belongs to its target, or that obligation identities are unique. The report owner defines the identity as:

```text
"s3:" + sha256(canonical_json({"kind": obligation.kind, "about": list(obligation.about)}))
```

**Concrete failure:** take the actual `11ec88e4` consequence row and exchange only the `about` values of its first two added obligations, leaving both map keys and `value.id` values unchanged. This associates the identity of `ssds.policy/subject` with `ssds.manifest/role`, and vice versa. All eight targets are still present and each id still equals its own map key, so `classify` succeeds: **942 observations, 696 (iii), 246 (v)**. It silently labels the altered identity-to-target relation as the exact repair.

Two additional counterexamples also succeed with those totals: replace one key and its matching `value.id` by `s3:` plus 64 zeroes; or give two distinct targets the same key/id. These are mutations of the report in scratch, not observations in the committed historical run. A broken consequence identity construction or identity join could therefore survive this classifier. Stable identities are a required observable under F123, not incidental formatting.

The committed report itself has eight distinct, correctly derived obligation identities, independently recomputed in this review. Its classifications need no reinterpretation on this account. The six tested mutations of discharge, extra fields, missing/duplicate obligations, quarantine values and unexpected integrity consequences correctly stop unclassified; those guards are useful but do not close this remaining relation.

**Closure condition:** bind each allowed obligation key/id to the exact `(kind, about)` identity construction and reject duplicates, while preserving the exact eight targets and other repaired checks. Demonstrate rejection of the three surviving counterexamples and unchanged classification of the actual report. The repair belongs in the classifier; no product-source or historical-report rewrite is warranted by this finding.

## Blocker RC-D1 — an interrupted comparison can return PASS

**Location:** `qualification/ssds80/PHASE-F-FR-A1-REREAD-WINDOW.py:95-110`, especially the result predicate at lines 109-110. **Owner:** the prepared revision-72 step-5 re-read window, not the ledger reader or boundary sensor.

**Concrete failure:** PREFLIGHT-A exits 0 and reports the correct default home. Line 95 initializes `record["differences"] = []`. A `KeyboardInterrupt` arrives while lines 96-100 are still constructing the comparison list. The augmented assignment never completes, so `differences` remains empty. Lines 101-102 catch the interruption and record it. The required product compare runs in `finally` and exits 0. The final predicate checks only read exit 0 and empty differences, ignores `interrupted`, and emits **PASS with exit 0**, although equality with W9 was not established. A ledger difference not yet compared could therefore be hidden by an interruption.

The precise post-exception state `{read_exit: 0, differences: [], interrupted: "KeyboardInterrupt: ...", compare_exit: 0}` was evaluated against the actual final assignment extracted from the script AST: result **PASS**. Only that pure assignment was executed, not the window, its main function, sensor or reader. The interruption path is explicit in the script's `except BaseException`; it does not require malformed data or a changed producer. The 11b runner already excludes an interrupted run from PASS.

**Closure condition:** make interruption/exception imply INCOMPLETE unless the product compare itself requires FAILED, while retaining the compare in `finally`. Demonstrate that interruption before comparison completion cannot pass, ordinary equal completed reads pass, and changed/failed reads do not. This can be qualified without touching a real home. The actual authorized re-read remains unexecuted.

## A and B — grammar repair evidence

FR-A1 is repaired at the common owner used by Admission and authenticated reading. Digest, commit, unit, token, envelope actor, timestamp, run nonce, report nonce and approval actor all use whole-value matching; `verify_chain` also matches the entire object path. SSH signature armour already used `fullmatch` and retains its deliberately permitted terminal newline. No changed grammar includes the previously accidental trailing LF as a legal value. Legal controls and existing producer-shape tests pass.

The other repaired sites cover manifest symbol/anchor terms; plan list patterns, refs, templates, evidence verifiers, obligation/item ids, governing unit and revision, criterion id/evidence; structural unit identity; ignore patterns; Git object identity; UCUM term parsing; and the requirements-file endpoint. `search` is intentionally retained for the path-suffix matcher, with `\Z` enforcing its actual end. The ignore pattern's `fullmatch` rejects `build\n` for literal `build`, while DOTALL lets prefix, `**` and directory-tail wildcards span a newline. **144 controlled path/pattern cases agreed with the installed Git `check-ignore` owner**, including LF in prefix, interior and suffix positions. This is evidence for the endpoint/DOTALL repair, not exhaustive qualification of every Git ignore feature.

The source audit searched regex definitions and consumers throughout `orchestrator/src/ssds`, including `.match`, `.search` and `$` patterns. Remaining cases are bounded as follows:

- `content/spec.py`'s endpoint patterns already use `fullmatch`.
- `core/git.py` strips the remote string before `_SCP_LIKE` matches it.
- `core/canonical.py` consumes split lines; content heading/fence/directive and plan parsers consume LF-free line text. Their anchors do not admit an extra LF in a whole stored value.
- `_QUANTITY_SUFFIX` consumes parsed AST identifiers, which cannot contain LF. Prefix readers and presence scanners do not claim whole-value validation.

Fresh affected regression: **193 tests passed in 56.839 seconds**, no skips reported, covering all six changed test modules and `ContainmentTests`. In an extracted candidate under scratch, every selected test group first passed unchanged. **All 28 individual endpoint mutations were detected**: 10 FR-A1 sites and 18 other repair sites, counting removal of DOTALL separately. Failures were inspected and correspond to the intended final-newline/wildcard discriminators, rather than import/setup failures. These tests exercise production owners, including authenticated chain reading and Admission, with fixture repositories and throwaway keys.

## C — the actual 11b evidence

Git independently yields **1,082 first-parent commits = 740 exclusions + one initialization + 341 evaluated deltas**. Every excluded identity, evaluated identity and row-parent pair agrees. The split at `53d5a22c04f8c8035dfccd4577a3cdd9ece06a2b` is **66/275**. The final **33** rows are exactly the first-parent interval `8cf829c3..c8122d66` in order. The first **308** row objects are equal field for field to the frozen report.

Fresh inspection found 690 excluded commits without a manifest and 50 with a manifest lacking `ssds.unclassified`; the initialization is `09f35057aec00467372aa8fbbda37f540a9bbc1f`. Across those 51 manifest-bearing trees, the real static-structure and reserved-leaf owners agree with the recorded eligibility, exempting only the two permitted leaves. There are two distinct manifest blobs and no newline-bearing unit ids. The prior review's complete `baseline_structure`/scope-resolution check remains applicable: the repaired surface does not change these manifests' prefix/path/heading resolution. This review did not repeat that full content read.

The committed report is `COMPLETE`, expected/evaluated 341, pending `null`, with its own boundary `PASSED`, unchanged true and no differences. Its SHA-256 is `1a9382228067928b9373f213a646407e55950098b3a9c6471f6d5639864b8d06`. The window records a new scratch home, harness exit 0, compare exit 0 and `PASS`, elapsed 1,860 seconds. All three recorded tool hashes match the inspected files. These are verified committed run records; this reviewer did not rerun the harness or observe the historical window's exclusivity.

All **942 observation identities and classes** were reconstructed independently from the report and compared with the classification, whose SHA-256 is `8883364a9dde004a663a5a072590bb810214ae1c4790bb6d708b03cb0f196ac6`. Running the actual classifier over that report also reproduces its observation records exactly.

| Observed reason | Count | Class and warrant |
|---|---:|---|
| Missing reserved leaves before repair | 576 | (iii), the expressly bounded genesis deviation |
| Reserved-leaf repair remains quarantined in scratch | 104 | (iii), scratch has no human adoption; absorption does not adopt structure |
| Eight quarantine keys and eight OPEN INTAKE obligations at repair | 16 | (iii), exact actual consequences of that deviation under Manual §18.2-§18.4 |
| Protected touches with authorship unestablished | 54 | (v), retained unmet agent-authorship predicate |
| Credential-template observations with enablement unestablished | 192 | (v), supplemental template; no current-policy verdict |

Thus **696 (iii), 246 (v)**. No actual observation supplies grounds for class (i) or (iv) within this study's evidence and applicability. The protected-surface owner includes the genesis-named policy path; while its declaration stays quarantined, touching its effective unclassified owner explains the later coarse unit-level observations. The credential owner emits a path-level observation without a matched value; the harness calls it supplementally and preserves the policy-enablement qualification. Credential observations were checked by code and applicability only. No matching source line/value was retrieved for investigation or retained. Check 1's request scan remains empty and check 4 remains vacuous; neither establishes live record-dependent qualification.

## D — containment and prepared re-read

The four retired tools are absent from the candidate tree and recoverable at `7d22f7083b559a189a2f5c17d281844096aa0050`. The staged FR-A1 copies are also gone. All six containment tests pass. An independent AST scan of **511 candidate-tracked Python files outside `orchestrator/`** found no direct program import or literal dynamic import of `ssds`; the tracked-source textual search also found none. This establishes the scoped repository remedy, not absence of arbitrary dynamically synthesized imports in every possible external program.

The prepared re-read extracts PREFLIGHT-A from that pinned commit and enforces SHA-256 `f2fecb328d47ad676f83a119887083c637330cf3489e90aa9aa8323fc582a969`, independently verified. It requires a full candidate id, source equality, clean source, no source bytecode and no linked worktree; it runs the extracted reader with `-I -B`, explicit source tree and all three ledger ids. The extracted script checks imported module origins and uses the real chain, record-violation and qualification owners without constructing Admission or loading a host key.

The environment removes `SSDS_HOME`, so the default home is used and checked in the report. On normal completion, all emitted per-ledger fields, including halt, qualification and violations, are compared with committed W9-c7. The outer product compare is in `finally`; nonzero compare produces FAILED, and nonzero read or an early parse failure produces INCOMPLETE. Pure comparison probes detected changed halt, qualification and violations. RC-D1 prevents a PASS on the overall failure-handling claim. **Neither this runner, PREFLIGHT-A, the boundary sensor nor the historical harness was executed.** Revision 72 step 5 remains required, unexecuted evidence pending repair and its separately authorized real-home window; a future difference reopens 10d's disclosure as the plan requires.

## Notes, evidence limits and custody

**N1 — missing versus null in the re-read comparison.** At `PHASE-F-FR-A1-REREAD-WINDOW.py:96-100`, `.get` equates a missing field with explicit `null`. Removing `ssdp-shadow-3.halt` from a synthetic W9-shaped result produces no difference. Exact dictionary equality, or an explicit key-set check, would express “field for field” more faithfully. Non-blocking for this pinned operation: PREFLIGHT-A unconditionally emits these nullable fields on every successful-chain path; its early failure paths omit other required non-null fields and are detected. No reachable omission from the fixed producer was demonstrated. Reassess if the producer/schema changes.

**N2 — outstanding acceptance and disclosure.** The authorized re-read has not happened; G2 revision 4 acceptance and the disclosed root regression remain outside this review's closure. D-C7-OBJECTS retains its before-new-producer and exit-disclosure obligations. Passing A/B does not close any of these or SC-U4.

Scratch evidence is under `/tmp/ssds80-phase-f-recheck-c8122d66/`: `focused.log`; `mutations.py`, `mutations.json`, selected baseline and 28 mutant logs; `audit.py`/`audit.json`; `probes.py`/`probes.json`; `initialization-structure.json`; and `reread-interruption.json`. Python used bytecode suppression; product tests used Python 3.12.16, scratch temporary directories and explicit scratch SSDS homes. Final source inventory has no new bytecode. Source-delta whitespace checks pass; protocol source/distributions, Core source, Architecture 1.6.0 and the accepted Manual are unchanged across the reviewed candidate interval.

**PEM/HAS:** the G2 workplan pins accepted project state `af0455753e20ee54a969c844872e29e270007211`, independently confirmed as project-designated `main`; accepted PEM is that commit's `PROJECT-ENGINEERING-MEMORY.md`, blob `1561797125622f355f84eb27319f87e8fa4227d9`. Candidate bytes equal the accepted publication; `candidate_overlay_semantic_candidate: NONE`. Schema 1 validates, five families and zero notices. All canonical family metadata was inspected. DS-001 is APPLICABLE to real-owner evidence and claim limits. PC-001 is APPLICABLE to the preserved frozen surfaces under current G2 §2 item 6, independently of memory's force. FF-001, SP-001 and SP-002 are NOT_APPLICABLE to this non-publication, non-package-routing task. Coverage remains PARTIAL, with no absence or recurrence-count claim. No memory update was made.

**Not checked or claimed:** a fresh full 1,911-test run, root-regression rerun, package/build/installed-product qualification, fresh historical harness run, live-ledger equivalence, performance or statistical qualification, exhaustive regex-language or Git-ignore feature enumeration, arbitrary runtime-generated external imports, or actual credential validity. Prior full-suite/build results remain author evidence, not fresh reviewer execution. The historical endpoint comparisons do not prove absence of transient reverted writes; shared production/harness owners retain common-mode limits. No real `~/.ssds` or `~/.ssh` was read and no live record or signature operation was performed.

Only this review record was written in the repository; all review scratch is under the permitted directory. Unrelated workspace files were left untouched. No candidate, evidence input, workplan, release-state file or implementation was edited; nothing was committed or pushed.
