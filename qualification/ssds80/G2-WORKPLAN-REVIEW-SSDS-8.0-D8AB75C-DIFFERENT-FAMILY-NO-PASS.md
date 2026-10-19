# SSDS 8 G2 shadow workplan revision 2 — independent D3 Review

    GOVERNING SSDP: 7.2.1
    PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: d8ab75ce80daaf0316b70814cde7aae3bd70affd
    SCOPE: G2 criterion 13; revision-1-to-revision-2 workplan, models and finding-index delta;
           B1/B2 repair, N1/N2 repair, residual closure, Stage D consistency and affected prior judgments
    BASELINE: 13d67be9f935e5cf7c2a5befa0c981026553d4ea
    WORKPLAN: workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md, revision 2
    WORKPLAN BLOB: 9a2ab7f2e10a74202faee29f1b87e0db7bd4695c
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: 0c1775d61b01d6c3898b93099a3100d00448e9cf
    MANUAL SEMANTIC CANDIDATE: 2a17a8305db5ed312dc453f9d86ccf5faee8ab74
           accepted A1-A3 text, blob e90c1a4db68e9410e81eefafdcfcff92b888c57b
    REVIEW METHOD: pinned-owner reconstruction; delta review; bounded lifecycle and inventory
           falsification; original-record witness sampling; required candidate checks; Challenge Pass
    REVIEWER: GPT model family, different from the workplan author's Claude family; launched through
           the Codex CLI in the stakeholder's own terminal at the stakeholder's request; the author's
           session typed only the handoff pointer. This context did not author the candidate and did
           not receive the authoring conversation. No delegated reviewers were used.
    DATE: 2026-10-19
    MUTATION BOUNDARY: this record only; scratch /tmp/ssds80-g2-review-d8ab75c; no commit or push

Governing SSDP version: **7.2.1**, independently resolved from the candidate release-state file. Section references below mean the exact candidate unless another record or source is named.

## SERIOUS CHALLENGE

**None established against accepted SSDP 7.2.1 or the accepted Manual. No G1 reopen.** The surviving findings concern incomplete G2 mechanism settlement and historical-closure evidence. Manual §10.3, §10.4 and §15.2-§15.7 permit a coherent repair without changing their architecture. The accepted Manual remains the baseline; this Review does not resolve a mechanism defect by weakening it.

The pinned software-design entrypoint and the shared abstraction, architecture, workflow, testing, semantic-definition, evidence, convergence, PEM, PEM-schema/publication and versioning owners were loaded where applicable. In particular, the testing owner states that green tests do not establish omitted obligations; workflow requires a substantial authority Review to attempt a trajectory outside the author's matrix; convergence requires sibling inspection and simplification before further additive repair. Architecture-workplan §25 criteria 11 and 13 apply the same no-blocker bar to residual mechanisms while preserving the G1/G2 distinction.

## Verdict

**NO-PASS. Two G2 blockers remain.** Revision 2 fixes the three concrete stranded states from the 13d67be Review, but its recurrence handoff does not settle what follows an answer to the recurrence decision. The historical index still omits seven explicitly numbered findings while its inventory check reports zero misses. Consequently RR-5/RR-6 and RR-9 cannot all be closed at criterion 13's bar. Every required check completed successfully; those results do not close these counterexamples.

The review envelope is separately identified: the requested R2 handoff does **not** exist at d8ab75c. It was added at the initial checkout HEAD `d05d1170e864ad35298a0765d628a0aca08473db`, blob `6607b6aebaa6f8a3b1d32479067c6920346cac7d`. The entire candidate-to-initial-HEAD diff is that one handoff addition. Its explicit subject and candidate match the user's request, so it was used as the issued review envelope, while every candidate artifact and executable check came from an archive of d8ab75c. No later semantic changes were substituted.

## G2 blockers

### B1 — the recurrence decision loses the answer-qualified identity and has no settled post-answer continuation

**Owner:** workplan §4.2's §10.2/§15.5 row, its §15 row, §4.11 and §4.13; `models/routing.py:85-102` and the S3 recurrence evidence. This is the common post-answer family, now at the handoff into recurrence, not a new architecture contradiction.

**Owner text.** The register requires a decision keyed on “(condition, item revision, the answer it follows)” and sends the next decision after the proposed count to recurrence, held for human attention. Manual §15.5 says a no-report coordination obligation is answered by the first admitted decision naming it. Catalogue §15.5 permits `AMEND`, non-floor `DECLINE`, `CHALLENGE` and `ESCALATE` for detected recurrence. Manual §15.6 reserves discharge of human attention to an authenticated human judgment. These provide a waiting route while the human decision is outstanding; they do not make an already answered decision open again. Manual §10.3's answered-obligation rule and §10.4's single-route rule still apply.

**Trajectory.** Keep item I at r1 with its budget spent. Three answers d1-d3 each amend a different item, integrate, and leave I unchanged and its budget spent. The settled model now returns recurrence key K = `('recurrence', 'budget-spent', 'r1')`, with a human-attention route. That is a legitimate place to wait for the required human response. Now let that human response occur, and let the recurrence coordination decision receive the allowed `AMEND` answer d4, again changing another item and integrating without changing I or its spent budget. The common rule owes a continuation or a new decision naming that answer. Instead, the model again returns K as an **open** decision, with exactly the same human-attention label. It has neither an answer-qualified successor nor a representation of the human response that releases the wait.

The reviewer replayed this boundary under all three conditions:

| Condition, unchanged r1 | After d1-d3, all integrated `AMEND` | After the recurrence answer d4, integrated `AMEND` |
|---|---|---|
| spent budget | `human-attention:recurrence:budget-spent`, `{('recurrence','budget-spent','r1')}` | identical route and key |
| kept fence | `human-attention:recurrence:kept-fence`, `{('recurrence','kept-fence','r1')}` | identical route and key |
| adverse item-level review naming no part | `human-attention:recurrence:item-level-no-part`, `{('recurrence','item-level-no-part','r1')}` | identical route and key |

The input is the module's ordered answer chain, extended from three to four `(answer_id, 'AMEND', True)` entries for the same `(condition, 'r1')`. At lines 98-100 the recurrence branch discards `aid`; every chain length at or above three produces the same key. The module contains no separate answered-recurrence or discharged-human-attention transition. If the model intentionally omits the human response and the recurrence answer, that is an unmodelled required continuation, rather than evidence closing this part of the residual. Merely waiting forever after a human has answered is not the promised meaningful continuation.

This does **not** refute the initial recurrence wait, require automatic budget renewal, or permit dispatch through a kept fence or unresolved finding. It refutes the claim that the common lifecycle has been settled through its post-answer states. A consumer must either try to dispatch an already answered key, suppress it and lack a newly defined continuation, or invent a release/reset rule the register never settled.

**Why the supplied evidence misses it.** `budget_recurrence` stops at the first recurrence. `run_models.py:200-208` compares a route prefix and decision set and asks whether the route is literally `none`; it does not replay the next answer or distinguish an outstanding human obligation from a discharged one. A nonempty label therefore passes. The additional ordinary post-answer cases are useful but do not test this boundary.

**Minimum repair.** Settle the post-recurrence lifecycle within the existing common rule: identify what the human answers, when its wait ends, and how an allowed recurrence answer either changes the route or derives a successor with a new identity. Preserve the permitted outcomes, human floors, budget, fence and findings. Prefer using the existing answer-qualified identity over a second terminal latch or condition-specific patch. If materially different response policies remain possible, obtain the stakeholder's direction under §4.3; do not describe an inferred policy as an already verbatim SD-54 choice.

**Discriminator.** Replay each of the three chains through the threshold, the authenticated human response, and an `AMEND` elsewhere before and after integration. Contrast unresolved human attention, a new item revision, `PARTITION`, a lawful non-floor recurrence `DECLINE`, `CHALLENGE` and `ESCALATE`. Assert admissibility and progress, not only a route prefix: an answered target is never emitted as a new open decision; any remaining wait names an actually outstanding prerequisite; no spent-budget dispatch or fence/finding bypass occurs. Carry these histories into Stage D group 5. RR-5 and RR-6 remain unclosed pending that settlement and Review.

### B2 — the revised inventory still omits seven original findings, and its checker shares the exclusion

**Owner:** workplan §4.1 S4, §4.9, §4.11 RR-9 and §4.12; `models/finding_index.py:512-519`; `models/finding_inventory_check.py:35-69`.

**Owner text.** S4 is done when “every finding is in the index” and none lacks a disposition with evidence. Section 4.12 claims a complete per-finding witness repair and an independent inventory with zero misses. The Lossless Representation Rule does not allow a mandatory finding to disappear because its Markdown punctuation differs. The new checker may use a separate implementation, but its observed zero must actually discriminate the inventory claim.

**Concrete omissions.** `WORKPLAN-REVIEW-SSDS-8.0-FFBAD17-NO-PASS.md:246-263` has the following seven findings under “Non-blocking findings (repair before or with the next revision)”. The index contains only that record's four lettered blockers; none of N1-N7 appears:

| Missing ID | Original concern | Current reconciliation route to examine; not a closure granted here |
|---|---|---|
| N1 | doctrine/impossibility claims exceed version routing, observed reads, escalation and envelope machinery | Manual §16.3, §16.9, §29 and §31.9; current claim bounds and live measurement obligations |
| N2 | ABA default can reverse a deliberate human reset | Manual §22.3; current fencing and `LATE_PUBLICATION` residual, including the Stage D foreign-reset discriminator |
| N3 | governing-version/R0-R3 provenance and stakeholder acceptance of interpretations | stakeholder record; Manual §32.5 and Phase B's retained historical-provenance limit |
| N4 | bidirectional scientific Review has no brief-compilation landing point | Manual §16.3 duty compilation and the scientific result slots |
| N5 | conflicting rebase must not be resolved mechanically | Manual §7.2, §7.4 and the next-iteration route |
| N6 | one template assigned both `HARD` and `HEURISTIC` force | Manual §14.2-§14.3's single-force templates |
| N7 | inherited authority-index release/status residue and historical whitespace | present authority index and bounded clerical/historical dispositions; Phase B explicitly did not accept unrelated residue |

The first line is `- **N1 (medium-high): ...**`; the others also put a severity annotation in parentheses between the identifier and title. `HEAD` does not accept a list-item prefix. `HEAD2` accepts that prefix but requires the dash immediately after the ID. The inventory checker initially recognizes N1, but line 65 discards its remainder because it starts with `(medium-high)` rather than the permitted title punctuation. Thus it reports **zero misses while all seven are absent**. Their lower severity changes investigation effort, not S4's closure condition. The established inventory is at least 704 findings, not 697; this is a lower bound, not a fresh exhaustive certification.

**Second independence counterfactual.** The candidate index correctly distinguishes `B46C250/DF` and `E548472/DF` from the corresponding first records. The checker does not: `index_ids()` strips `/DF` and unions finding IDs by candidate alone. In a scratch copy, removing all three E548472/DF rows and B46C250/DF's B1 and N1-N5, while retaining its unique N6, deletes **nine distinct record/finding pairs**. Running the unchanged candidate checker against that projection still returns exit 0 and “0 finding heading(s) absent”. This is an evidence-instrument counterexample; those nine rows are present in the actual candidate. It shows that record separation is not qualified by this check.

The independent reviewer scan retained full source filenames and examined Markdown title-bearing lines without importing either author's finding regex. It recovered the severity-labelled findings above. Its broad candidate list also contains labels and references to earlier findings; that list is a search aid, not a replacement semantic inventory. The supplied line scan is a separate code path, but shares the decisive punctuation assumption with the extractor and additionally loses record identity. Its exclusions therefore fail the requested independent discrimination.

**Minimum repair.** Reconcile these seven source findings individually, preserving historical gaps and Stage D obligations as such. Audit actual title forms and exclusions over the bounded corpus, rather than adding a blanket Phase B disposition or trusting the zero tally. Key both generation and checking by the complete review-record identity plus finding identity. Existing per-finding witnesses and `/DF` output keys can be retained; no new registry is needed.

**Discriminator.** Require the inventory check to fail for the current seven omissions, severity-labelled list titles, and each missing row of either second review record even when another record has the same candidate and finding ID. Retain controls for genuine earlier-finding summaries and protocol/refinement labels. Regenerate and compare the index, then semantically verify the newly recovered dispositions. RR-9 remains open; the 13d67be B2 closure is incomplete.

## Non-blocking findings

**N1 — SD-54's received text and the proposed recurrence policy must stay distinct.** Item 50 ends at “kept-fence DECLINE resumes the item's r”. The SD-54 row explicitly identifies the remainder as the author's reading of the option, and the workplan marks the count of three as a proposed default for G2. The received text directly supports the answer-qualified key and wait-for-integration rule; it does not independently prove stakeholder selection of that recurrence count or its precise human-release behavior. A recurrence detector and raised human attention are compatible with Manual §15.4/§15.7 in principle: policy may raise floors, and attention cannot be discharged by the principal. Preserve this proposal/acceptance distinction at the eventual G2 decision. B1 concerns the mechanism's missing continuation regardless of this provenance limit.

**N2 — A4 and the accepted A1-A3 Review's disclosure findings remain carried.** The cross-plan owner clarification, per-route/state missing-judge costs, and runner-attribute/reproduction costs and reopen considerations remain visible in §4.10 and the index. No new counterexample established a G1 blocker there. Stage D must keep the catalogue considerations the register accepts; this Review supplies no missing Manual amendment or historical acceptance.

**N3 — correct the invocation's handoff commit locator.** The handoff is at d05d117, reviewing candidate d8ab75c. The envelope-only descendant relationship was verified, so the locator mismatch did not prevent this review or change its subject. Future invocation text should distinguish the envelope commit from the candidate commit.

## The five requested judgments

1. **B1 repair: partial.** The original spent-budget `AMEND` elsewhere, kept-fence `DECLINE`, and item-level-no-part `AMEND` elsewhere states now continue correctly. Pending amendments wait visibly; integrated amendments derive a key naming the answer; a changed revision starts a fresh chain; `PARTITION` yields the part route; `ESCALATE` leaves the item-route decision unanswered. A kept-fence `DECLINE` still meets a spent budget rather than bypassing it, and the independent out-of-scope finding routes remain present. Initial recurrence waiting does not waive a floor. Its answered lifecycle remains unsettled under B1. SD-54's truncated text cannot establish the inferred remainder as verbatim authority.
2. **B2 repair: substantial but incomplete.** The lettered examples from revision 1 now have explicit Phase B witnesses, and the old unmatched-workplan blanket closure has been removed. Both candidates' second records are separately represented; E548472/DF has its own hand dispositions. B2 above refutes completeness and the inventory check's independence at the decisive boundaries. Sampled closure witnesses are mostly recoverable, with the qualifications below; regeneration parity is not semantic closure.
3. **N1/N2 repair: met.** Section 5.5 now explicitly makes criteria 9/10's live reports necessary for G3; separate campaign authorization controls when/how, not whether evidence is required. The §26 row now places fitness checks in Phase D, every later change, and attack/fault exercise in Phase H. Neither repair changes G2 into campaign authorization.
4. **Delta consistency: otherwise preserved in the reviewed surface.** The register changes are the common coordination row, its item-level application, the §15 recurrence note, and §26 fitness evidence. Sections 4.9/4.11/4.12/4.13, lifecycle notes and the six changed Stage D discriminator rows reflect the repair work. Groups 1, 2, 3, 4, 5 and 7 gain the recovered discriminators; groups 6 and 8, delivery, phase ownership and shadow boundaries are unchanged. The added Stage D cases do not weaken existing negative discriminators. RR-5/RR-6 and RR-9 nevertheless fail criterion 11's same no-blocker bar for G2 residuals. No Manual body change occurred in this delta.
5. **Remaining criterion 13 elements: unchanged judgments survive only to their applicable scope.** The seven revision-1 judgments reconcile as follows:

| Revision-1 judgment | Revision-2 assessment |
|---|---|
| 1 derivation | Unchanged W, typed targets, scoped integration support, narrow exception and accepted A1/A2 bindings remain applicable. The recurrence continuation cannot be inherited as settled. |
| 2 mechanism settlement | Catalogue coverage and reasoned inspection of formats/procedures remain applicable; common routing settlement is incomplete under B1. |
| 3 residual closure | No new delta defect established for RR-1/2/3/4/7/8/10/11 in the checked scope. RR-5/6 and RR-9 remain unclosed. Assembled identity/budget effects and real-owner replay remain Stage D obligations. |
| 4 historical findings | Previous conclusions on unchanged sampled mechanisms remain hypotheses corroborated by current owners. Seven omitted findings and the weak inventory check prevent complete historical closure. |
| 5 Stage D | One distribution/namespace, Core extension registration, Admission-only shadow append from human-gated genesis, no NATIVE subject, no governed write/push credentials, external-owner permission and read-only pilot remain intact. Campaign and real-owner gates are preserved. The table now has 27 `STAGE-D` rows; these carry obligations, not completed executions. |
| 6 simplicity | Reusing one answer chain improves the former three early-return branches. B1 requires completing that common lifecycle before adding condition-specific compensation. The index repair replaces a blanket disposition with recoverable evidence; its parser weakness does not justify another authority surface. |
| 7 checklist | Shadow scope is met; successful complete mechanism settlement/residual closure is not. This NO-PASS is a Review record, not successful criterion 13 closure; criterion 14 remains a separate stakeholder act. |

## Witness sample and probe states

The semantic sample was purposive: emphasize the requested later-Review, removed-mechanism, revision-23, Phase B and new hand-disposition classes, plus the two same-candidate record pairs. **Twenty-four indexed findings** were checked against their original statements and the relevant witness/current owner. This is not a statistical sample or certification of all dispositions. The seven missing FFBAD17 findings were additional inventory challenges, not counted among those 24.

| Original finding | Candidate disposition | Result of source/witness check |
|---|---|---|
| Manual 0B6C4FA N5 | CLOSED-LATER-REVIEW, 27EF339: “Repair introduced B2” | This is a carry, not a clean historical repair. 27EF339 B2 and current §1.2/§1.4's ownership rule supply the onward route; S5 write-set evidence is bounded. |
| Manual 27EF339 N2 | CLOSED-LATER-REVIEW, 575DC78: “Closed as surfacing; the stakeholder decision is pending” | The quotation alone proves surfacing only. Current bounded-stop costs are disclosed in §6.6/§32.2 and the accepted G1 package; historical pending wording is not present acceptance evidence by itself. |
| Manual 27EF339 N5 | CLOSED-LATER-REVIEW, 575DC78: “Closed within one frame; across frames, B1” | Residue is explicitly in 575DC78 B1 and the later frame family; current §5.2/§7.5 own locality. It is not an assertion that the old across-frame counterexample passed then. |
| Manual 1FFBBF0 N1 | CLOSED-LATER-REVIEW, 3540D98, partly closed | Full witness carries later disappearance to its N2. Current §1.9 and §32.2 retain the narrow ABSENT/no-specific-finding limit. The shortened index quote is only a route to the full witness. |
| Manual 53669A5 N6 | CLOSED-LATER-REVIEW, 1FFBBF0, residue N4 | Full route continues through 1FFBBF0 N4 and 3540D98's verification; current §18.4 defines the quarantine paths and ending routes, with moved-out content a bounded limit. |
| Workplan F9D9DE8 N2 | CLOSED-LATER-REVIEW, 441CF5C N10 | Current consolidation tests parse frontmatter for state/routing and preserve structural file-placement guards; they disclaim semantic adequacy. No prose-truth oracle is inferred from their PASS. |
| Workplan 203A42B N4 | NA-REMOVED, `present` | The arbitrary-copy presence predicate is superseded by §6.4's anchors/home/start and §6.6's observation discrimination. Historical copies do not by themselves establish current matching. |
| Workplan 947370D N4 | NA-REMOVED, reading pairs/floor | The old existence veto on future pairs is absent; current §6.6/§6.8 defines discriminating readings, coverage and class. This does not abolish all current human floors. |
| Workplan BA7F738 N6 | NA-REMOVED, withdrawal latch | The old withdrawal/exception combination is superseded; §6.4 states the start event and retained consequence, including the admitted-history cost. That cost survives visibly rather than being declared nonexistent. |
| Workplan 6FE1000 N2 | NA-REV23 | Current §6.4 preserves home and states the bounded content-follow rule; §32.2 discloses moved/rewritten limitations. It does not promise universal tracking of semantic copies. |
| Workplan 644EB72 N5 | NA-REV23 | §17.4 binds admissibility to the instantiated realization/specification, rather than allowing the assessor's arbitrary specification choice. |
| Workplan 203A42B A | CLOSED-PHASE-B, E23F142 §3 | The witness explicitly names A and the anchors/home repair. Current §6.4 preserves adversity across the named structural and retirement changes. |
| Workplan 203A42B B | CLOSED-PHASE-B, E23F142 §3 | The witness names B; §8.3 requires each salvaged record's own checks and refuses unauthorized supersedes. No salvage-based authority is granted. |
| Workplan 124B0B7 A | CLOSED-PHASE-B, E23F142 §3 | The witness names A; §6.7 explicitly excludes challenge/loss/positive-only requalification as disposal. |
| Workplan 4EC0024 C1 | CLOSED-PHASE-B, E23F142 §3 | The witness names C1; current supersession standing and outcome/reading coverage distinguish renewed evidence from resurrection of every old disagreement. |
| Workplan 124B0B7 N2 | STAGE-D, group 2 | Original concern was policy-permitted provisional continuation, not only overrides. §5.3 now carries that precise discriminator; no execution claimed. |
| Workplan 441CF5C N7 | STAGE-D, group 4 | Rewind must produce `ROLLBACK`, not expected success; explicit in §5.3. |
| Workplan 730490D N2 | STAGE-D, group 4 | Foreign return to B_n requires detection/escalation as `LATE_PUBLICATION`; the plan preserves the disclosed residual instead of promising that reversal never occurred. |
| Manual 575DC78 N5 | STAGE-D, group 3 | Two-frame and fresh iteration/rebase gate cases are added; anchor/region siblings continue through group 1 and B46C250 N4/F7419D5 N4. |
| Workplan A414588 N2 | CLOSED-ARCH | Current §12.2/§25.2 and catalogue §8.3 bind retired-key salvage to the retirement record's outstanding-envelope list; issue-position prose alone is not the bound. |
| Manual B46C250/DF N6 | CLOSED-S2-S3 | Unique second-record finding; current §1.4 gives innermost ownership precedence over residual/uncovered fallback, with S5 nested cases. |
| Manual B46C250 N4 | STAGE-D | Original frame/minimum, unchanged-D1/D2 and anchor/region discriminators are carried in groups 1/3; shared ID in the second record is not a substitute source. |
| Manual E548472/DF N2 | COST | Historical adoption provenance remains partial; current binding does not manufacture its missing transcript. |
| Manual E548472 N2 | CLOSED-ARCH | This is instead the fixed-admitted-set order claim, now stated by §5.10(h)(6). The different subject confirms why `/DF` separation matters. |

The candidate's later-Review quotes preserve partial-closure language, but are often truncated. Their full named source, successor finding and current owner must be followed before reuse; neither a quoted “partly closed” nor an old pending decision alone establishes current closure. No further blocker was established from these 24 sampled dispositions.

**Routing variants.** Twenty-six primary reviewer states were evaluated: for each of spent budget, kept fence and item-level-no-part, `AMEND` before/after integration, `PARTITION`, `ESCALATE`, and integrated-answer chain lengths two/three/four (21 states); plus holding-predicate, open-candidate, awaiting-fence, kept-fence `DECLINE`, and that decline meeting a spent budget (five controls). Three additional changed-item-revision controls derive fresh keys. The three original 13d67be states were separately replayed under `revision1` and `settled`: formerly `none`, now respectively new coordination, re-dispatch, and new coordination. Three paired recurrence comparisons reuse the threshold/fourth-answer states and demonstrate B1. The outcome probes establish the model's declared route only; `partitioned:<answer>` alone does not qualify production partition execution.

**Inventory variants.** Original committed index versus regenerated bytes; the candidate's separate inventory scan; a reviewer filename-preserving broad title scan; and one scratch projection removing nine overlapping second-record findings. Selection varied punctuation, record identity, partial closure and current-owner route rather than optimizing the number of green rows. The broad scan's 249 candidate lines include references and non-finding labels; it is not an independently certified total. The seven concrete omissions and nine-row negative fixture suffice to refute the complete-inventory claim without claiming exhaustive discovery.

## Checks, applicability and gaps

All required checks ran on or against the exact candidate archive:

| Check | Result and scope |
|---|---|
| `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` | PASS, five tests. Structured state/routing and placement guards only. |
| `python3 -I qualification/ssds80/models/run_models.py --seeds` | PASS, exit 0. S1 23 cases; S2 22 plus Q1 readings; S3 23 routing and four identity cases; S5 63 cases. Settled readings have zero supplied misses; revision1 fails the nine expected Q3 cases; seeds pass. This is not a full mutation campaign. |
| `python3 -I qualification/ssds80/models/finding_index.py` and byte comparison | PASS, generated output byte-identical to committed index. It reproduces the omissions in B2. |
| `python3 -I qualification/ssds80/models/finding_inventory_check.py` | PASS as implemented, exit 0, zero reported misses. Independently falsified as a complete inventory under B2. |
| `git diff --check 13d67be9f935e5cf7c2a5befa0c981026553d4ea d8ab75ce80daaf0316b70814cde7aae3bd70affd` | PASS. |
| Frozen surfaces versus `fad3ee410ab9df0d94740cebb6969e161911b126` | `git diff --exit-code` found no byte changes in `orchestrator/docs/architecture.md`, `source/` or `dist/`. |
| Manual versus `2a17a8305db5ed312dc453f9d86ccf5faee8ab74` | Lifecycle/status lines only: amendment acceptance labels, accepted-candidate bookkeeping and A3 labels. No decision/body-semantic change. |
| `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md` | PASS, schema 1, five families, zero notices, using candidate source/environment and original repository Git context. |

Archive Git-dependent validation used `GIT_DIR=/home/samjin/agent-skills/scientific-software-development-system/.git` and `GIT_WORK_TREE=/tmp/ssds80-g2-review-d8ab75c/candidate`. Reviewer programs, candidate/source archives, sample extracts and counterfactual output are confined to the named scratch directory. `probes.py`, `routing-probes.txt`, `probes-output.txt`, `inventory-suspects.json`, `index-without-second-records.md`, `generated-index.md` and `sample-*.txt` retain the auxiliary evidence; the decision-changing inputs and observations are reproduced above so this record does not depend on scratch retention.

At final workspace verification, another session had advanced HEAD to `12a4d345f53d4bcee30489aeb300ee58a2b1c6e4`, proposing Manual amendments A4-A6. Its sole changed path from the initial checkout is the Manual. That external change was preserved and was not used as the candidate or accepted authority in this review. Tracked working-tree differences remained empty; the only reviewer-created repository path is this untracked record, alongside the pre-existing untracked environment files.

No production SSDS component, live trajectory, external scientific-repository pilot, distributed fault qualification, confidentiality execution, campaign, G3 outcome measurement or cutover was executed. Those remain Stage D/G3/G4 work, not evidence demanded before the implementation that would create the owners. No unavailable required command is being counted as passed. Unanswered semantic coverage includes unsampled historical dispositions, further possible inventory forms, the full recurrence response matrix in B1 and assembled production behavior. The present defects are already decision-changing; further broad mutation runs or full historical re-review were not needed to determine NO-PASS.

## PEM basis and task-local HAS

PEM is activated by this memory-bound workplan. The project's explicit policy designates main as the integrated publication line. Independent local resolution found main at `af0455753e20ee54a969c844872e29e270007211`; its PEM blob and the candidate's PEM blob both equal the workplan's `1561797125622f355f84eb27319f87e8fa4227d9`. Thus there is no additional candidate byte overlay. The published file retains older-cycle metadata; that is historical publication data, not a new branch acceptance. Schema/routes validate and coverage remains explicitly partial. All five canonical families' identity/applicability metadata were searched, independently of temperature or summary inclusion; there are no current notices.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: hjin98/scientific-software-development-system@af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md (blob 1561797125622f355f84eb27319f87e8fa4227d9)
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: Model and generated-inventory claims must be limited to discriminated cases; independently enforced by the pinned testing owner.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen-resource preservation is independently required by the pinned versioning owner, Manual section 26 and workplan section 2; byte parity was checked.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: This review publishes no immutable public-source fallback; the historical bootstrap failure is not evidence of this routing defect.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No source-router/package regeneration repair is undertaken.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: No public-source/recovery publication or self-reference transaction is undertaken.
```

PC-001's historical capability transfers through unchanged frozen surfaces and the current versioning/workplan constraints, with direct Git parity as evidence. No historical implementation is retained merely because memory names it, and no PEM entry supplies a new pass threshold. No PEM change is proposed.

## Scientific checks, Challenge Pass and common mode

**Material findings:** B1 and B2; no upstream scientific or numerical finding. **Realized scientific results:** none produced, run or reviewed. All executions here are protocol design/inventory diagnostics; there is no scientific-result envelope to populate. **Variants:** supplied readings/refutations, 26 primary routing states plus three new-revision controls, three original regression replays, the three paired recurrence comparisons, 24 indexed semantic samples, seven omitted findings and the nine-row inventory counterfactual as detailed above. No scientific parameter tuning, model selection or measurement campaign occurred.

No accepted project D1/D2 authority was used for a consequential scientific judgment, so no D1/D2 tension search is claimed. Mentions of D1/D2 in the protocol's routing and floor contracts are architectural scope, not reliance on a scientific formulation. The reverse-direction question was applied to the evidence method: a green route label and green inventory coexist with omitted required states/findings.

**Bounded Challenge Pass.** Temporarily ignoring the author's case partition, reconstructing “one meaningful route, no repeated answered target” exposed the recurrence boundary; reconstructing “every source finding has a recoverable disposition under its own record identity” exposed the severity-label omission and record-union weakness. Shadow authority, sole-writer genesis, real-owner qualification and independent-judgment boundaries were checked for affected regression; no surviving G1 contradiction or hidden implementation/campaign authorization was established. These are exploratory falsifications, not a preregistered statistical study.

**Common mode.** Author and reviewer share the accepted Manual, repository history, Python runtime and several earlier diagnostics. The author supplied both rule interpretations and expected examples; an agreement can share the same omission. Different model family and a separate reviewing context improve process diversity, not epistemic independence. Prior review summaries and retained memory were hypotheses; consequential identities, owner text, examples and sample witnesses were checked against the pinned source. The separate original-record scan and answered-lifecycle reconstruction add distinct evidence routes but do not prove the absence of other defects. No conclusion rests on vote, review count or a majority of PASS records.

## D4 statement

**D4 stays not authorized.** This NO-PASS leaves criterion 13 unmet and G2 open. A repaired-workplan PASS would supply criterion 13's Review only; criterion 14 still requires the stakeholder's explicit authorization of shadow implementation. Live campaigns retain their separate reviewed-plan/authorization boundary, G3 needs its live evidence, and native authority remains per-subject G4. This review record is the sole repository file written; no implementation, commit, push, acceptance, release-state change, campaign or cutover was performed.
