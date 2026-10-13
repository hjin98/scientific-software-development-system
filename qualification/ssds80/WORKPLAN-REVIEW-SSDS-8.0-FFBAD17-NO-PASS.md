# SSDS 8.0 Prospective Architecture Workplan — Independent D3 Review, Design Revision 5 (with the unreviewed Revision 4 and the Phase A 7.2.1 Reconciliation)

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: ffbad17df806d92e2214eafd7e9bdeff448a5694
    HEAD AT REVIEW START: ffbad17df806d92e2214eafd7e9bdeff448a5694
    HEAD AT FINAL RECHECK BEFORE THIS RECORD: ffbad17df806d92e2214eafd7e9bdeff448a5694 (local and origin)
    INTERVENING COMMITS: none
    SCOPE: design revision 5 (git diff edf816a ffbad17); design revision 4 (edf816a0edb4104bfec9525a0d052d1e3c13f901,
           never Reviewed); Phase A 7.2.1 inheritance reconciliation (d11f085eb1b2c54b3e44b0ad7b63a454aeb5954a)
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN GIT BLOB: 10451d0da15bd907d862f608507c9c69541427df
    AUTHORITY INDEX GIT BLOB: 45006ce29b811d165514427cb1d1d7475c3af817
    CONSOLIDATION TEST GIT BLOB: 39ce361e4766ee76a9112056e6ab8e5b8d48e3f3
    GOVERNING PUBLIC-SOURCE REF: aaeaf8b6b2121b9fb8aba31917c8265649c43954 (7.2.1, from PROTOCOL-RELEASE-STATE.yaml)
    GOVERNING RECOVERY REF: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    REPAIR-BASIS REFS (6.6, historical): public 22f4bdba53795da3a6f13f162529f3a843fc37ae, recovery 384666764da4c55b282e6b1595ab97e2f86e1dc4
    PRIOR REVIEWS, HYPOTHESIS ONLY:
      qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-F9D9DE8-NO-PASS.md
      qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-441CF5C-NO-PASS.md
      qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-8A75346-NO-PASS.md
    REVIEW METHOD: software-design role entered at the 7.2.1 public-source ref; owners read with `git show <ref>:<path>`;
                   fresh D3 reconstruction; out-of-matrix abstraction-adequacy pass; workplan self-assessment
                   (§0.1 tables, "defects found by this revision's own pass", §27), commit messages, index prose and
                   prior Reviews treated as hypotheses only

## SERIOUS CHALLENGE

**None.**

The accepted 7.2.1 owners reconstructed at `aaeaf8b6` are coherent for this decision, and the recorded stakeholder direction of 2026-10-13 (§0.1) is realizable when read as quoted. Read literally ("provide the deterministic machinery to reliably achieve them", i.e. all SSDP doctrine), the objective is unrealizable for judgment-level duties (detection, adequacy, equivalence). The same quotation scopes the agent to "semantic analysis, concept handling, and routine decision-making", and §1.1/§1.3 adopt that bounded reading explicitly. That makes the objective consistent, not contradictory. Whether the bounded reading is what the stakeholder wants is an objective-acceptance question for the stakeholder (N3), not a D3 Challenge.

## Verdict

# **NO-PASS**

Revision 4's two repairs of the 8a75346 blockers survive independent attack for the trajectories those blockers named. Successor-entry publication reconciliation is sound. The loss boundary withholds pre-loss support even after a stale-consistent restore. The Phase A bindings are correct against `PROTOCOL-RELEASE-STATE.yaml` and the 7.2.1 owners. Four D3 blockers survive:

- **A** (derivation core, present since revision 3 and missed by the 8a75346 Review). An open blocking challenge against an `UPHELD` adjudication suspends it. That turns a revocation by an upheld non-blocking challenge into `CLEAR`. Filing a challenge therefore un-revokes a triple. Through a withheld pre-loss dismissal, the loss boundary does the same, contradicting revision 4's "restrictive effects survive".
- **B** (revision 5, A8). Whether a human-attention obligation survives depends on the S2 currency of a support-tier report record, which the D3 leaves undefined. Under the natural reading, editing the report's target or recording a loss boundary silently drops a `CRITICAL` human question. The downgrade rule also contradicts itself on who may discharge human attention.
- **C** (revision 5, A5/A9). Admission binds a request to its role through the obligation it *claims*, while step 7 requires every claimed obligation to be dischargeable by that request. The phase-1 result and every mid-task report are therefore inadmissible as written. Task issue and context lineage are non-canonical and unauthenticated, and the independence rule fails open where lineage is unobservable.
- **D** (revision 5, A5/§7.6). The R1 "monotone" and "decomposition" amendment classes are not closed predicates. The principal's self-certified `PLAN_STRENGTHENING` equivalence carries an independent plan acceptance onto content it never saw, including changes to the `scientific` flag, frozen interfaces and escalation triggers, and onto new item units, which §6.7 and §12.2 forbid.

No blocker requires abandoning the four primitives, seven components or six persistent surfaces. Each needs a repair at its D3 owner before a PASS is possible.

---

## 1. Identity and authority reconstruction

### 1.1 Candidate and lineage

`git rev-parse HEAD` returned `ffbad17df806d92e2214eafd7e9bdeff448a5694` at start and immediately before this record; `origin/ssds-8.0-graph-native-architecture` is the same commit. The clone is shallow (`git rev-parse --is-shallow-repository` = true).

The prior Review candidates (`f9d9de8`, `441cf5c`, `8a75346`) are absent from this clone because the branch was rebased (§0.4). The §0.4 commit map was checked by blob identity rather than trusted:

| Reviewed revision | Rebased commit | Workplan blob | Index blob | Test blob |
|---|---|---|---|---|
| f9d9de8 | e62be2f | aba4e967 (= F9D9DE8 record header) | — | — |
| 441cf5c | 25ed4c3 | cb967c15 (= 441CF5C record) | e6115ad5 (=) | 798a7d5f (=) |
| 8a75346 | 6a3d03a | d130da4e (= 8A75346 record) | b00aec69 (=) | 798a7d5f (=) |

The befe678 archive is blob `af9c005b…` (also the active workplan blob at `513da27`). The archived consolidated plan is `cc795f40…`, byte-identical to `workplans/active/…CONSOLIDATED.md` on the rebase basis `af04557`. The "reviewed bytes unchanged" claim therefore holds for the three reviewed revisions.

`PROTOCOL-RELEASE-STATE.yaml` (blob `1ba0135f…`, unchanged by the branch) names `project: hjin98/scientific-software-development-protocol`; the clone's origin is `…-system`. This is recorded as an identity note only.

### 1.2 Governing owners (7.2.1 public source)

These owners were read at `aaeaf8b6`: software-design `SKILL.md`, architecture-and-design (`71e2d7b7`), workflow-and-workplans (`98220992`), scientific-inspectability-and-initiative (`ccbe7680`) and protocol-versioning-and-compatibility (`7e2c7969`). Diffs of evidence, concurrency, storage, security and testing were also read.

§0.4's claim about the repair-basis owners was checked by blob and diff between `22f4bdba` (6.6) and `aaeaf8b6`:

- Unchanged: kernel `c38aa30e`, semantic-definition `94b48b50`, Git `cf493cd9`, PEM `89849eca`, convergence `65737830`.
- Changed additively:
  - workflow: bidirectional scientific Review, Channel C and product-scope acceptance;
  - evidence: RSR overlap and `CHALLENGES` inquiry status;
  - concurrency: one sentence extended;
  - storage: weighing retention before loss;
  - security: inspection and export trust boundaries;
  - versioning: ratification package as Channel C, plus 6.6-7.2 profiles;
  - architecture: O1;
  - testing: projection faithfulness.
- The claim "no repair basis is withdrawn" holds.

The independence rule this Review relies on is the 7.2.1 workflow owner's own: "Review independence means the reviewing context did not author the candidate and does not inherit author conclusions … A subagent that receives the author's conclusions is not independent." The delegated-findings rule is the 7.2.1 inspectability owner's: "material delegated findings must survive to the human"; the delegator "may rank and condense, never drop".

### 1.3 Phase A reconciliation

- **Identities.** §24's 7.2.1 recovery `efdd1b59` and public fallback `aaeaf8b6` match the release state, and the 6.6 identities are correctly historical. The frozen profile `orchestrator/src/sdp_orchestrator/core/resources/protocol/ssdp-protocol-7.2/profile.json` exists (PC-001 binding).
- **Inputs.** All seven 7.2 inputs of archived §37.2a are rowed in §19.2. The archived §36, §37.x and §38 are rowed in §18.1.
- **Adoption sequence.** The versioning owner's sequence (authorized request, then reconcile obligations, then update the binding through its authority process) is followed in form. The authorizing instruction exists in the candidate only as the author's paraphrase (N3).
- **7.2.1 table.** One addition named in §0.4's prose, bidirectional scientific Review, has no "Met at" row (N4).
- **Disposition.** Phase A bindings are correct. Phase A adequacy is PASS, subject to N3 and N4, which are non-blocking.

### 1.4 PEM / HAS

The PEM predicate fires (mature-machinery replacement). `PROJECT-ENGINEERING-MEMORY.md` is blob `1561797125622f355f84eb27319f87e8fa4227d9` at the candidate, at `edf816a`, at `d11f085` and at the rebase basis `af04557`, so there is no overlay. It has schema 1 and `reconciled_through` `23e46543`.

- **PC-001** remains `AUTHORITY_BOUND` through the 7.2.1 versioning owner, which still requires every older profile to stay frozen and independently testable. The candidate preserves this.
- **SP-002, FF-001 and SP-001** remain `EVIDENCE_ONLY` and are not promoted.
- **DS-001** remains `EVIDENCE_ONLY` and is directly applicable. §22 does not discriminate any of the four blockers below.

No local `main` ref exists, so whether `main` has advanced beyond `af04557` could not be checked (§10.3).

---

## 2. Blocking findings by earliest owner

### Blocker A — §6.6 S1: challenging an upholding un-revokes its target; the loss boundary does the same through a withheld dismissal

**Trajectory (ordinary operation).**

1. Triple `z = (s, scope_id, r)` carries a passing acceptance `j`.
2. A qualified actor raises a **non-blocking** challenge `c0` on `z`.
3. Adjudication `a` (`UPHELD`) targets `c0`. Then `upheld(c0)` holds, `status1(z) = REVOKED` and `base(z) = F`. This is the state §6.6 calls "revokes that revision permanently".
4. Any qualified challenger raises a **blocking** challenge `d` targeting `a`, and `d` stays open.
5. By the S1 formula, `in_force(a) ⇔ gate(a) ∧ ¬∃ c: c.target = a ∧ (upheld(c) ∨ (c.blocking ∧ open(c)))`, so `in_force(a) = F`. Then `upheld(c0) = F` and `open(c0) = T`. Because `c0` is non-blocking, `status1(z) = CLEAR` and `base(z) = T`.
6. `j` is unchallenged and its basis is satisfied, so `valid(s) = T`.
7. Admission step 3's "never on a `REVOKED` triple" and step 4(b)'s freeze no longer apply, so new acceptances and re-scoping of `s` are admissible.

**Trajectory (loss boundary, revision 4).** Steps 1-4 occur, and `d` is then `DISMISSED` by adjudication `e`, all before a `LEDGER_LOSS`. After the boundary, `e` is a relaxer with `cont(e) = F`, so it is not in force. `d` reopens as blocking, `a` is suspended, and `z` becomes `CLEAR` again.

**What this violates.**

- S2: Serious Challenge and Challenge stop counterfeit closure.
- §6.6: "an upheld challenge … revokes that revision permanently. Repair requires … a *successful* challenge to the upholding adjudication".
- §6.6: "Effects are conservative in both directions".
- §15.4 polarity table: "`UPHELD` adjudications and the revocations they produce … unchanged (restrictive)".
- §22: "a retained pre-loss *upholding* (including of a non-blocking challenge) keeps its revocation in force after the boundary".

The defect is in the S1 formula itself. The revision-3 formula had the same suspension term, and the 8a75346 Review recorded S1 as coherent.

**Earliest owner.** §6.6 S1, the semantics of `in_force` for `UPHELD` adjudications, together with the §15.4 polarity claim.

**Minimum repair direction.** A challenge against an upholding must never relax the revocation while it is open. Either:

- `in_force` of an `UPHELD` adjudication ignores open challenges and only an upheld counter-challenge removes it; or
- a suspended upholding yields at least `BLOCKED` on the original target, whatever the original challenge's blocking flag.

Then re-derive the loss-boundary polarity argument. A relaxer whose withholding can re-enable a relaxation two levels down must be shown harmless. Add §22 cases for a blocking challenge against an upholding of a non-blocking challenge, with and without a pre-loss dismissal of that challenge.

### Blocker B — §7.9 with §6.3 and §15.4: escalation persistence is undefined against S2 currency and the loss boundary (A8)

**Facts in the candidate.**

- Reports are support-tier judgment records with bases (§6.3). FINDING's tier is itself inconsistent: §6.3 lists "finding or challenge" in the challenge tier, while §7.9 lists FINDING apart from the challenge-tier kinds and the §6.3 support-tier "report" list omits it.
- Routing maps reports to derived S3 obligations that "appear and disappear as derivation changes" (§7.1, §7.9).
- After a `LEDGER_LOSS`, every pre-boundary support-tier record has `base = F` (§6.6 S2). Requalification obligations are derived only for "permissive records and relaxers" (§6.6 S3, §15.4).
- The §15.4 polarity table was not updated for revision 5's kinds: task result, report, coordination decision, materiality reclassification, human acknowledgment and check-execution observation.
- Nothing states whether a human-attention obligation is keyed on the report's existence or on its currency.

**Trajectory 1 (ordinary operation).** An investigator files `HUMAN_QUESTION` `q` (`CRITICAL` floor) targeting plan item `I`, with a content entry on `I`'s revision. The plan's principal, acting within its only write scope, amends `I`. Now `q` is not current. If routing reads current reports, the `CRITICAL` human-attention obligation disappears with no authenticated human judgment. The same happens for a `MATERIAL` finding whose D3 or D4 target any in-scope implementer edits.

**Trajectory 2 (revision 4 × revision 5).** `q` is pending at `R`, and a `LEDGER_LOSS` is admitted. `q` is pre-boundary, so `base(q) = F`. It is not permissive, so no requalification obligation lists it, and the question vanishes from the inspector view.

**Internal contradiction.**

- §7.9 says a principal's materiality-reclassification judgment "discharges that human-attention obligation".
- The same paragraph, A8 and §7.5 (principal "May not … discharge human attention") say only an authenticated human judgment discharges it.
- §1.1 claims a route "no agent can interrupt".

**What this violates.** A8 (a material finding survives to its owner; only a human discharges escalation), the 7.2.1 inspectability owner's survival and carry-forward rule ("never drop"), and the stakeholder direction's "deterministic flow of important discoveries and decisions to the human inspector".

**Earliest owner.** §7.9 routing and escalation semantics, the §6.3 tier assignment of report kinds, and the §15.4 polarity table.

**Minimum repair direction.**

- Key escalation and human-attention obligations on the existence and identity of the escalating record, not on its S2 currency. A stale target may annotate an entry, never erase it.
- Classify escalating report kinds as restrictive for the boundary, or enumerate them explicitly as post-boundary obligations.
- Assign FINDING to one tier.
- Define a principal downgrade as moving a non-floor item to the digest without discharging it, or else drop the "only a human discharges" wording for non-floor items. The text must say one thing.
- Extend the §15.4 table to every revision-5 kind.
- Add §22 discriminators: target edit after a report; a loss boundary with a pending `CRITICAL` question; a principal amendment of a reported plan item.

### Blocker C — §6.8 step 3 and step 7, §7.5, §7.8, §9.6 and §6.3: request-to-task binding is contradictory, non-canonical and fail-open (A5, A9)

**Contradiction.**

- §7.5: "Admission checks a submitted record against `role(kind(o))` … for the obligation `o` the request claims; no task-issue record is needed in the ledger."
- §6.8 step 7: "each obligation the request claims … its discharge predicate (§7.4) holds after the request's own records … the derived conformance of the exact candidate commit has no `VIOLATION`, `INCOMPLETE` or `DISCREPANCY`."
- §7.8 phase 1: the implementer's result is admitted *before* the Dispatcher runs the required executions and before any review exists.

The phase-1 result request has two options, and both fail:

- If it claims its realization obligation `o`, step 7 rejects it. There is no review judgment, and missing executions make conformance `INCOMPLETE`.
- If it claims nothing, step 3 has no role to check. A5's "exactly one workflow role for exactly one task" is unenforced for results.

The same applies to every mid-task `report`, including blocking reports that must suspend the raising task. This is a precondition whose evidence arrives only after the step, the same defect class as 8a75346 Blocker A.

**Binding authenticity.**

- The execution → task → obligation → role → contract revision → context lineage binding lives only in the Dispatcher's private operator journal, which §6.3 says influences "scheduling, never derived workflow state".
- Execution provenance is "observed by the Dispatcher" (§15.6), but no trust root authenticates the Dispatcher's attestation to Admission (T4 covers only human decisions and canonical entries).
- On the Git-envelope transport the result envelope is agent-written (§15.1).

**Independence fail-open.** §9.6: "Admission rejects a review or plan-acceptance judgment whose provenance *shows* it continues the author's context." Manual agent invocation and the Git-envelope route are first-class (§9.5, §16.2 invariant 7). There the Dispatcher cannot observe context lineage. Pasting `Execute SSDS task <id>` into the authoring session yields provenance that shows nothing, so the self-review is admitted. This contradicts A9 ("constructed, not requested"), C5 (unknown required semantics fail closed) and the 7.2.1 workflow owner's definition of independence.

**Earliest owner.** The D3 contract for request binding: §6.8 steps 3 and 7, §7.5, §7.8, §9.6, and the §6.3 operator-state boundary.

**Minimum repair direction.**

- Separate the obligation a request is *bound to* (for role, write scope, suspension and provenance) from the obligation whose *discharge* it claims. Step 7's discharge predicate applies only to claimed discharge: the integration request, and records whose own admission discharges, such as reviews and coordination decisions.
- Make the binding a fact Admission can check without another host's private state, and authenticate it under a declared trust root. The protected issued task envelope or an Admission-recorded issue observation are both candidates.
- Make independence fail closed. A judgment counts as independent only with positively attested fresh-context lineage. Unknown lineage is recorded as non-independent, or needs an authenticated human attestation on manual routes.
- Add §22 cases: phase-1 result and blocking-report admissibility; a forged or absent lineage; the bootstrap executed inside the authoring context.

### Blocker D — §7.9 amendment classes with §6.7 and §7.6: R1 self-certified plan equivalence is not a closed predicate and crosses scopes (A5, §7.6 rule 3)

**Facts in the candidate.**

- *Monotone* is "no existing obligation removed and no statement or verifier changed; write scope not widened; objective, existing acceptance criteria, gates and dependencies unchanged; the only additions are new obligations or new `HARD` checks".
- The predicate mixes forbidden changes with permitted additions. It does not mention the contract fields `scientific`, `frozen`, `dependencies` (the manifest allowance), `evidence_specs`, `expectations`, `escalation` or `budget`.
- *Decomposition* constrains only obligations, write scopes and item dependencies.
- The principal, the amendment's author, admits a `PLAN_STRENGTHENING` `EQUIVALENCE` with independence waived by the ruleset, and through it the existing R2 plan acceptance stays current.

**Trajectory.** Item `I` has `scientific = APPLIES` and an `escalation` trigger. The principal's `AMEND` changes `scientific` to `NOT_APPLIES`, removes an escalation trigger and drops a `frozen` interface. It adds one `HARD` check, so the diff contains an addition.

- No enumerated monotone condition is violated, so lint classifies the diff R1.
- The principal's equivalence is admitted, and `I`'s plan acceptance stays current.
- Lint's slot rule is keyed on the now-`NOT_APPLIES` flag, so the E2 delegate slots disappear.
- The §7.9 delegate floor no longer fires for new tasks, and implementers may change the formerly frozen interface.

The `scientific` flag is "judged at plan acceptance" (§7.6), and boundary adequacy is "an R2 judgment by an execution other than the contract's author" (§7.6 rule 3). Neither judgment happened. Under the strict "additions only" reading the flag change would be non-monotone. The D3 does not say which reading holds, and the §22 "Work contracts" cases do not test any of these fields (DS-001).

**Scope violation.** Decomposition replaces item `I` with new item units. A plan acceptance covers "the item revisions it accepts" (§7.2), and an `EQUIVALENCE` "relates two revisions of one unit … never relates different scopes. Acceptance moves to a new scope only through an acceptance judgment" (§6.7, §12.2). Either the R1 decomposition path cannot exist as described, or it moves acceptance across scopes contrary to S10.

**The equivalence is also semantically false.** Adding an obligation narrows admissible concretization. That is a semantic mutation under the 7.2.1 workflow owner unless it is established as representation-only. Labelling it "equivalence" lets the author self-accept that mutation (A5: "no actor reviews or accepts its own work").

**Sequencing.** The `AMEND` decision "carries" an equivalence between two plan revisions that exists only after the later plan-unit change. The admission path of the principal's plan-unit change is not stated.

**Earliest owner.** §7.9 amendment classes, the §7.6 contract schema and lint, and the use of §6.7 equivalence.

**Minimum repair direction.**

- Define monotone and decomposition as closed whitelists over every contract field, with a permitted direction per field.
- Make any change to `scientific`, `escalation`, `frozen`, `expectations` or `evidence_specs` that weakens it R2.
- Either require scoped R2 review of added obligations, or state precisely what the existing plan acceptance's adequacy conclusion covers after strengthening, and call it something other than equivalence.
- Define decomposition consistently with §6.7 and §12.2. For example, items decompose as parts of the original item unit, or decomposition is R2.
- State the admission sequence of a plan-unit amendment.
- Add §22 cases for every field.

---

## 3. Non-blocking findings (repair before or with the next revision)

- **N1 (medium-high): doctrine-realization and impossibility claims exceed the specified machinery.**
  - §7.7 places "version binding and the self-adoption guard" at E0, and §19.3 says revision 5 "realizes … version ordering at E0". Yet §19.2's version-routing row has no D3 decision; it is left to the Manual.
  - A6 lists "what was read" as machine-produced, but only interface reads and reads a harness adapter can observe are recorded (§6.4; read recording is a §26 reopen trigger).
  - §1.1's route that "no agent can interrupt" ignores raiser-controlled report existence, materiality and target. The domain floor is keyed on the raiser-chosen target, and the principal can `DECLINE` or downgrade.
  - §0's "failure class it makes impossible" for the authority envelope rests on Blocker C.
  - Repair: bound each claim to its mechanism.
- **N2 (medium): the ABA default can reverse a deliberate human reset.** When the optional publication-attempt log is absent (any other Admission host, or a lost local store), §15.3 permits re-applying `B_n -> C_n` after a foreign reset to exactly `B_n`. That reset may have been a security remediation. C4 requires ambiguity to be reconciled before retry. Prefer a fail-closed human disposition, or canonical evidence of the earlier success, over silent re-application. This is disclosed as a residual, but the chosen default is the unsafe branch.
- **N3 (medium): authority traceability.**
  - The 2026-10-12 governing-version adoption and the 2026-10-13 statement that the stakeholder "accepted the decision-class classification (R0-R3)" exist only as the candidate's paraphrase. The 2026-10-13 direction is quoted, and its quotations do not exceed what is attributed to them.
  - The realization of the stakeholder's "basic domain and keyword checks" as non-blocking `HEURISTIC` signals, and the bounded reading of "reliably achieve" all doctrine (§1.1), are design interpretations.
  - These are objective and product-scope matters that need the stakeholder's explicit acceptance; D3 Review cannot accept them. Persist the instructions verbatim, or as stakeholder decision records.
- **N4 (low-medium):** §0.4 names bidirectional scientific Review among the 7.2.1 additions but gives it no landing point. §9.6 review briefs should carry the reverse-direction question for scientific subjects, or state the §9.2 compilation route that does.
- **N5 (low):** the integration rebase (§7.8) does not say how conflicts are handled. Under K3, machinery must not resolve a semantic conflict; a conflicting rebase should route to a new iteration.
- **N6 (low):** the Domain check family is "`HARD` where annotations exist, otherwise `HEURISTIC`", which contradicts "each template declares one force". Split the templates.
- **N7 (low; pre-existing, outside revision 5):**
  - The index front matter is still `protocol_version: 6.6.0`. `current_handoffs.protocol-7.0` and the Protocol 7 status block (e.g. "Stage F PRE-RUN remains STOP/BLOCKED") are stale relative to the closed 7.2.1 cycle; that text is inherited from `af04557`. The SSDS 8 section is accurate.
  - `git diff --check af04557 ffbad17` fails on markdown hard-break trailing whitespace in the F9D9DE8 record. `edf816a..ffbad17` and `d11f085..ffbad17` are clean.

## 4. Recheck of the 8a75346 findings against revision 4

| 8a75346 finding | Disposition | Independent basis |
|---|---|---|
| Blocker A, publication recording cycle | **Closed** | Every entry carries `obs`, Admission's own read. The first later entry carrying `obs` classifies `pub(n)` as a pure function of `B_n`, `C_n`, `obs` and immutable reachable commits. The dependency chain (n admitted -> CAS -> read -> append n+1) has no backward edge. The consistent row leaves S0-S2 unchanged (same tree), so validation at `n` stays sound. Shape rule: an `obs ≠ E` entry must be a record-free absorption. Hosts race through the ledger CAS. Recovery entries carry no `obs` and leave `PENDING` truthful. Residual: N2 |
| Blocker B, coordinated stale restore | **Closed for the named trajectory; restrictive-survival claim false (Blocker A)** | `cont` is S1, reads only later ledger records, and is identically `T` without a boundary; recursion is on strictly later positions. `base ≤ cont` withholds `j_A` whether `Q` is empty or not. `LEDGER_LOSS` re-establishes witness model, trust roots and ruleset. The non-admission bound `h + m + f < q_a` is sound under authenticated checkpoints. Tenure and boundary are independent locks. The indirect relaxation of an upholding through a withheld dismissal is Blocker A |
| N1, intra-subject warrant | **Closed** | §6.4 assigns basis mode by subject boundary; there is no self-validity edge; a positive §22 case exists |
| N2, qualification for A and B | **Closed for A and B; new gaps** | The ledger-only replay oracle and the both-stores-stale loss group are present. They do not discriminate Blockers A-D of this Review |
| N3, missing §36 row | **Closed** | §36 and §38 rows present |
| N4, Manual deferrals | **Still bounded** | D4 is gated by Phase C (§23, §25) |
| N5, quorum inequality | **Re-verified** | `|Q_a ∩ R| ≥ q_a + r − N > f`; holds for `(3,2,2,0)` and `(1,1,1,0)` |

Revision 4's own-pass repairs were checked. The `upheld(c)` term in `in_force` is correct as far as it goes. The re-routed support edge check in step 5 is correct. The witness-count non-admission bound is correct. Quarantine is correctly demoted to a non-defense.

## 5. Out-of-matrix pass (§27 ignored; selected trajectories)

| Attack | Result |
|---|---|
| Challenge an upholding to un-revoke (ordinary, or after loss) | **FAILS**: Blocker A |
| Erase a pending `CRITICAL` question by editing its target, or by a loss boundary | **FAILS under the natural reading**: Blocker B |
| Principal downgrade as human discharge | **Contradictory text**: Blocker B |
| Phase-1 result or mid-task blocking report admitted | **Inadmissible as written**: Blocker C |
| Self-review via bootstrap in the author's own context, or a Git-envelope route without lineage | **FAILS (fail-open)**: Blocker C |
| Flip `scientific`, drop escalation or `frozen` via an R1 amendment | **FAILS**: Blocker D |
| Decomposition carrying acceptance to new items | **Contradicts §6.7/§12.2**: Blocker D |
| Any new S3 classification (conformance, decision/amendment class, escalation, routing) read by S0-S2 | **No path found**: conformance and classes are consumed by Admission legality and S3 only; derivation never reads them; strata stay well-founded |
| Admission legality reading S3 | **Well-founded**: legality is evaluated once at one admitted head over S0-S3 plus the request's records; no derivation input depends on the decision being made |
| Verification standing in for review | **Blocked**: discharge needs a current review judgment; `CLEAN` only makes review ready; heuristic removal changes no mechanical decision (A7). DS-001 note: the signal-inertness replay over recorded judgments cannot detect signal influence through reviewers, which is intended |
| Implementer edits its acceptance test | **Blocked** for unnamed evidence specifications (`HARD`); semantic weakening of tests it authored stays with review (disclosed) |
| Overstep disclosed or undisclosed | **Blocked**: `VIOLATION` never integrable; authenticity of the task binding is subject to Blocker C |
| Two principals amending one plan | **Blocked** by step 6 currency even across Dispatcher hosts; the serialization surface only saves work |
| Domain-floor evasion by under-declaring materiality | **Blocked**; evasion by mis-targeting is an undisclosed residual (N1) |
| Publication: CAS success then crash, foreign force-push, overtaken under quarantine, two hosts, replay without integration host | **Holds** (§4) |
| ABA after CAS on a host without the attempt log | **Holds within disclosed limit; unsafe default** (N2) |
| Stale-consistent restore plus `LEDGER_LOSS`; demotion, restoration, ruleset, evidence and import variants | **Holds**, except the indirect upholding path (Blocker A) |
| Revision-5 kinds after a loss boundary (coordination decision, reclassification, acknowledgment) | **Conservative if escalation is keyed on existence**; undefined otherwise (Blocker B) |
| Version and profile isolation; dual authority; cutover lost in the abandoned interval | **Holds** (§12.1, §24, PC-001) |

## 6. Stakeholder direction (2026-10-13)

The quoted direction asks for four things:

- deterministic machinery as the backbone of doctrine;
- agents limited to semantic work;
- machine-readable obligations, boundaries and expectations;
- machine verification of completion, boundary overstep and faithful reporting, with complex semantics left to reviewers and "basic domain and keyword checks … achievable by machines".

The paraphrased parts add role-based execution with an authoritative principal, implementers without plan authority, clean-context reviewers, and a deterministic flow of discoveries to the human.

The design maps each of these to a mechanism: §7.5-§7.10, §9.6-§9.8 and §1.1. Nothing attributed to the direction exceeds what is quoted or paraphrased. The decision classes are recorded as separately accepted (N3).

The realization is not yet adequate. The backbone guarantees the direction relies on most (enforced roles, clean-context reviewers, non-droppable flow to the human) are each defeated by a locally compliant trajectory (Blockers B-D).

## 7. Minimum justified architecture and capability transfer

- **Nothing unjustified added.** Roles, contracts, conformance, routing, budgets and the inspector view are policy parameters, plan content or S3 derivation. No new primitive, record category, surface or component is added, and the §27.5 rejected additions are well-reasoned.
- **Missing.** One thing the problem does need is absent: an authenticated, canonical execution-to-task binding (Blocker C). Its absence is why A5 and A9 cannot be enforced.
- **Capability transfer.**
  - §16.2 still disposes all 26 Architecture 1.6.0 invariants. The frozen architecture blob is `39e6de72…`.
  - §18.1 rows every archived section, including §36, §37.2a and §38.
  - §18.2's befe678 rows are unchanged.
  - Revision 5 strengthens archived §17-§19 without loss.
  - No material capability loss was found.

## 8. Qualification-program adequacy (DS-001)

§22's revision-5 groups test the intended mechanics. None discriminates the four blockers:

- *Escalation* checks principal operations on floor items but not target staleness or a loss boundary.
- *Workflow roles* tests "provenance shows continuation" but not absent or unattested lineage.
- *Work contracts* classifies widening and verifier weakening but not `scientific`, `frozen`, `escalation`, `expectations`, `evidence_specs` or `budget`.
- The *loss* group asserts the upholding survives, without a counter-challenge.

Green implementations of the current matrix could retain all four defects. The consolidation test (frontmatter and placement only) cannot discriminate any semantic property, as its own docstring says.

## 9. What was verified, and how

Executed during this Review:

- `python -m unittest tests.test_protocol_80_orchestrator_consolidation -v` passed: 4 tests, OK (Python 3.13.16, Git 2.43.0).
- `git diff --check edf816a ffbad17` and `git diff --check d11f085 ffbad17` were clean. `git diff --check af04557 ffbad17` fails on the pre-existing F9D9DE8 record (N7).
- `git diff --name-only af04557 ffbad17` shows that no `source/`, `dist/`, `orchestrator/`, README, CHANGELOG, release-state or PEM file changed. Package build, distribution parity and Orchestrator snapshot/Core checks are therefore not affected surfaces and were not run.
- `python -m unittest discover -s tests` ran 434 tests: 1 failure, 2 errors, 6 skipped. All three trace to commits absent from the shallow clone:
  - release-state refs;
  - `55c08526…` for PEM reconciliation;
  - `2dedcfa` for the 7.2 block-size baseline.
  These are environment limits, not candidate evidence.
- `python source/release_state.py` and `python source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md` both exit 1 for the same shallow-clone reason: historical refs are unresolvable.
- Blob identities, the rebase map, archive identities, owner diffs between `22f4bdba` and `aaeaf8b6`, the 7.2 profile presence and the PEM blob at the rebase basis were checked as recorded in §1.

## 10. What could not be verified

1. Whether `main` has advanced beyond `af04557`, including any PEM write. There is no local `main` ref, so the accepted/base memory is verified only at the rebase basis.
2. The stakeholder instructions of 2026-10-12 and 2026-10-13, beyond the candidate's own text (N3).
3. Release-state realization, PEM binding health and the three history-dependent tests, because of the shallow clone. These remain required checks for any later acceptance, not PASS evidence.
4. Whether the original candidate commits `f9d9de8`, `441cf5c` and `8a75346` are byte-identical to their rebased counterparts beyond the workplan, index and test blobs checked above.

## 11. Common-mode dependency

This Review ran as a fresh-context agent of the same model family as the author of revisions 4 and 5 and of Phase A. It was launched by the authoring session with a neutral handoff that named the scope and the probe areas but carried no author conclusions beyond the candidate text itself. That gives process independence, not epistemic independence. Shared model family, training corpus, toolchain and reading habits are a material common-mode dependency, which the 7.2.1 workflow owner requires to be recorded. The defects found here were missed by the author's own §27 passes and, for Blocker A, by a prior independent Review. A Review by a different model family or a human for the S1 and escalation semantics would materially reduce this risk.

## 12. D4 statement

**SSDS 8 D4 remains NOT AUTHORIZED.** This NO-PASS blocks Phase B. A later PASS would still not authorize D4 before Phase C: an independently reviewed and stakeholder-accepted Architecture Manual resolving §21. This Review creates no release, recovery, adoption or cutover identity.
