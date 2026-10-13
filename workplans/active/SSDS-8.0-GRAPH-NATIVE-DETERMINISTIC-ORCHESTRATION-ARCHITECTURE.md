---
kind: ssds-major-architecture-workplan
workplan_id: SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE
protocol_version: 7.2.1
target_system_version: 8.0.0
status: proposed
created_date: 2026-10-01
revised_date: 2026-10-13
design_revision: 13
baseline_reconciliation: protocol-7.2.1 (2026-10-12; section 0.4)
governing_version_adoption: 6.6.0 -> 7.2.1 by stakeholder instruction 2026-10-12 (section 0.4)
stakeholder_direction: workflow execution and verification layer, 2026-10-13 (section 0.1; qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md)
source_branch_basis: af0455753e20ee54a969c844872e29e270007211
source_branch: main
prior_source_branch_basis: f96b7ccf90dede4150d0efa17264fff07ec12d0d (ssdp-7.0-scientific-epistemic-closure; design revisions 1-4 before the 2026-10-12 rebase)
design_basis: befe6782e7c8fe038bf7cb764646d133ca167855
prior_review: qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-4C35D92-NO-PASS.md
prior_reviewed_candidate: 4c35d92d2c75c9961d4d3b97c35c6dfad04c6336
review_history:
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-F9D9DE8-NO-PASS.md
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-441CF5C-NO-PASS.md
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-8A75346-NO-PASS.md
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-FFBAD17-NO-PASS.md
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-F3608F5-NO-PASS.md
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-AC71FA9-NO-PASS.md
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-730490D-NO-PASS.md
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-FB3E542-NO-PASS.md
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-124B0B7-NO-PASS.md
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-97E753F-NO-PASS.md
  - qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-4C35D92-NO-PASS.md
design_review_state: pending-fresh-independent-d3-review
d3_architecture_state: proposed
implementation_handoff: not-authorized
active_serious_challenge: none
supersedes:
  - SSDP-8.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-CONSOLIDATED
  - SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE-BEFE678-HYPOTHESIS
---

# SSDS 8.0 — Deterministic Orchestration Architecture: Basis-Stamped Judgments over Content-Addressed Units — Prospective Workplan

The workplan ID keeps the historical `GRAPH-NATIVE` lexeme for routing stability. The architecture it carries is not graph-native in the sense of its predecessor hypothesis (§3): graphs are derived views over one typed relational substrate.

## 0. Disposition

```text
GOVERNING DESIGN PROTOCOL: SSDP 7.2.1 (adopted from 6.6.0 by stakeholder instruction 2026-10-12, §0.4;
            release identities owned by PROTOCOL-RELEASE-STATE.yaml)
TARGET: SSDS 8.0.0, the system-level successor to the document-controlled SSDP line
THIS FILE: single current prospective SSDS 8 architecture handoff, design revision 13; proposed, not accepted-current;
           not an Architecture Manual
REVISION 13: derives adverse evidence from the evidence owner's applicability dimensions (evidentiary premises) after
           the 4c35d92 Review (blocker A; findings N2-N7; §0.1); N1 remains partial
REVISION 12: re-derived assessment disagreement as applicable adverse evidence and effective disposition after the
           97e753f Review
REVISION 11: re-derived assessment disagreement as existence-keyed S1 predicates after the 124b0b7 Review
REVISION 10: bound prospective acceptances to one enactment after the fb3e542 Review
REVISION 9: completed the transformation contract after the 730490d Review
REVISION 8: re-derived the candidate-currency and publication contracts after the ac71fa9 Review, per the
           convergence owner's simplification trigger
REVISION 7: repaired the f3608f5 Review's blockers A-D and finding N2; N1 recorded as partial
REVISION 6: repaired the ffbad17 Review's blockers A-D and findings N1-N6 at their owners; N7 dispositioned
REVISION 5: added the workflow execution and verification layer (workflow roles and decision classes, work contracts,
           conformance verification, report routing and non-droppable escalation; §7.5-§7.10, §9.6-§9.8) and the
           doctrine-realization objective (§1.1), by stakeholder direction 2026-10-13, whose principles the stakeholder
           accepted (qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md)
PRIOR REVIEWS: f9d9de8 NO-PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-F9D9DE8-NO-PASS.md), repaired by revision 2;
           441cf5c NO-PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-441CF5C-NO-PASS.md), repaired by revision 3;
           8a75346 NO-PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-8A75346-NO-PASS.md), repaired by revision 4;
           ffbad17 NO-PASS, four blockers A-D and findings N1-N7, covering revisions 4-5 and Phase A
           (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-FFBAD17-NO-PASS.md), repaired by revision 6;
           f3608f5 NO-PASS (GPT-6/Codex), four blockers A-D and findings N1-N2
           (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-F3608F5-NO-PASS.md), repaired by revision 7;
           ac71fa9 NO-PASS (GPT-6/Codex, fresh context), three blockers A-C and findings N1-N2
           (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-AC71FA9-NO-PASS.md), re-derived by revision 8;
           730490d NO-PASS (GPT-6/Codex, fresh context), two blockers A-B and findings N1-N4
           (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-730490D-NO-PASS.md), repaired by revision 9;
           fb3e542 NO-PASS (GPT-6/Codex, fresh context), two blockers A-B and findings N1-N2
           (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-FB3E542-NO-PASS.md), repaired by revision 10;
           124b0b7 NO-PASS (GPT-6/Codex, fresh context), blocker A and findings N1-N2
           (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-124B0B7-NO-PASS.md), re-derived by revision 11;
           97e753f NO-PASS (fresh-context sub-agent of the author's model family), blockers A-B and findings N1-N7
           (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-97E753F-NO-PASS.md), re-derived by revision 12;
           4c35d92 NO-PASS (fresh-context sub-agent of the author's model family), blocker A and findings N1-N7
           (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-4C35D92-NO-PASS.md), re-derived here
SUPERSEDES: the consolidated Protocol 8 plan (archived byte-identically, with its nine-file lineage)
            and the befe678 graph-native hypothesis (archived byte-identically as ...-BEFE678-HYPOTHESIS.md)
SERIOUS CHALLENGE: NONE (§1.3 records why the governing goals are judged consistent)
PROTOCOL 7: closed at 7.2.1 (accepted with conditions); inheritance RECONCILED (Phase A executed, §0.4, §19, §24);
            the ffbad17 through 4c35d92 Reviews found its bindings correct; the 2026-10-12 adoption instruction
            remains paraphrase-only (f3608f5 N1, partial; routed to stakeholder restatement)
INDEPENDENT D3 REVIEW: ready for a fresh independent falsification Review of design revision 13; the stakeholder
            directed (2026-10-13) that the remaining revise/review cycle run through fresh-context sub-agent
            Reviews (same model family as the author: a recorded common-mode dependency); this
            revision is refinement, not acceptance, and awards itself nothing; a PASS authorizes nothing by itself:
            shadow D4 needs gate G2 (accepted Manual, reviewed shadow workplan, stakeholder authorization; §25)
SSDS 8 D4: NOT AUTHORIZED
```

**What the architecture is.** Four primitives (§5): content-addressed **units** (leaf regions grouped into acceptance **subjects**), typed **relations**, immutable **records** in one append-only ledger, and the **basis** each record relied on. Everything else — validity, currency, obligations, readiness, impact, context, views — is a pure stratified derivation (§6.6). One Admission writer serializes every canonical change (§6.8). The ledger is a Git object chain on one authoritative ref, appended by single-ref compare-and-swap, admitted only once a witness quorum holds the new head, and published to the product integration ref as an effect whose outcome the next entry records (§15.3). A known loss of admitted history is itself a ledger fact that bounds which retained authority can still be current (§15.4).

**Four separations carry the design.** Each removes a class of failure rather than one example:

| Separation | Rule | Failure class it makes impossible |
|---|---|---|
| observed repository state vs admitted governance state | content proposes; admitted records enact. Ruleset, structural roles, membership, scope and acceptance change only by admission (S11, §6.1) | authority, routing or acceptance arising from repository presence, foreign pushes, restores or merges |
| definitional dependency vs warrant dependency | every relation type has a closed semantic role and cycle class; cycles are legal only among definitional edges inside a declared simultaneous-definition group (§6.2) | circular warrant, authority, evidence, provenance or lineage, inside or across subjects |
| appended ledger state vs current-qualified state | an append is provisional until a witness quorum holds its exact head; only admitted state is ever asserted current (P4, §15.3-§15.4) | a historical prefix or an unwitnessed append presented as the current head |
| retained history vs known-lost admitted history | abandoning admitted history is a recorded loss boundary; effects recorded before it that could only add support or relax a block are withheld after it until requalified or attested unaffected; restrictive effects survive (P5, §15.4) | authority, support or relief reviving across admitted history known to be lost, even when ledger and product are restored to the same stale snapshot |

**How agents work on top of it (revision 5).** Every task is executed in one **workflow role** (principal, implementer, reviewer, investigator) whose contract — what it may write, submit and decide — is enforced by Admission, never by instruction text. Each plan item carries a machine-readable **work contract**: boundaries, obligations, and how each obligation is verified. The machine produces every factual part of a result; the agent supplies only judgment, in typed slots. **Conformance verification** is a derived classification over the contract, the candidate and recorded executions: it can reject, return or point, but never pass anything a reviewer must judge. Reports route deterministically; material findings reach the human through obligations that no agent can discharge (§7.5-§7.10, §9.6-§9.8). Two further separations carry this layer:

| Separation | Rule | Failure class it makes impossible |
|---|---|---|
| authority envelope vs instruction | a workflow role, bound to each request by an authenticated task envelope, constrains which proposals Admission considers; brief text only informs (A5, §7.5) | on authenticated bindings within the declared trust model (§15.6): an agent mutating plans, contracts, verifiers or out-of-scope content because a prompt was misread, ignored or absent |
| mechanical conformance vs semantic acceptance | verification is necessary, never sufficient; heuristic checks only point (A7, §7.7) | a passing check, a keyword lint or an agent's own claim standing in for a reviewer's judgment |

### 0.1 Revision 13: what changed and why

The `4c35d92` Review (a fresh-context sub-agent of the author's model family, under stakeholder direction SD-8; `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-4C35D92-NO-PASS.md`) returned NO-PASS with one blocker family and seven findings, and no Serious Challenge. It recorded the `97e753f` blockers as closed and the effective-disposition half of revision 12 (`eff`, `contested`) as sound.

The blocker was confirmed. Revision 12's `applicable` tested every entry of the failing assessment's basis, and §6.4 puts the assessor's reads, declared reliance and widened closure there. An edit to a unit that only the failing assessor had read therefore removed the failing evidence while its realization stayed current (A1). An upheld challenge against any record premise, such as a completeness judgment, disposed of it (A2). This was the third successive proxy for "failing evidence that may still apply" to fail permissively: currency (revision 10), a key (revision 11), the whole basis (revision 12). Revision 13 drops the proxy. It derives adversity from the 7.2.1 evidence owner's own applicability dimensions, each with one fixed role.

| Finding | Repair (earliest owner) |
|---|---|
| **A1** adversity lapsed with the assessor's context; siblings: implementer iteration, `UNBOUNDED` basis, step-6 rejection, interpretive move with order-dependent reassessment | **Evidentiary premises** (§6.6). Each owner dimension has a fixed role: obligation, admissibility, execution variation, evidentiary premise (claim revision and named execution content), interpretive premise (specification, oracle, tolerance), frame, or provenance (everything else). `bears(a-)` tests only the evidentiary premises of the failing realization. An interpretive move keeps the failing assessment adverse (`review-required`) until its realization is reassessed or judged immaterial. An incomplete closure's fallback is provenance. Admission step 6 admits failing assessments whatever the currency of their context |
| **A2** disposal through an unrelated premise | Only an upheld challenge against the failing assessment or its realization disposes of it (§6.6) |
| N1 adoption provenance | Unchanged; still partial |
| N2 the model check's oracle reused the predicates it checked | Rewritten. The oracle is independent, and owner-grounded properties are added: P5 (a move of a non-evidentiary premise never raises the evidence term), P6 (an upholding against a completeness premise never raises it) and Q (a bearing failing assessment with nothing recorded against it caps it). The sensitivity modes must fail on these, not only on the oracle |
| N3 independence of self-supersession | Every disposition must be independent of the claim's author; a non-independent one has `eff = F` (§6.6, §6.8 step 3) |
| N4 disposition reliance on the failing assessment | Identity mode, so a challenge against the failing assessment never changes the disposition (§6.6) |
| N5 D1/D2 floor on stale failures | Scoped to failing assessments that bore when admitted, an immutable fact (§6.6, §7.9) |
| N6 edit-and-rerun sampling | Manual item 11: ensemble acceptance that does not depend on the latest single replicate (§21) |
| N7 "conservative" claimed in the wrong direction | Wording replaced. `bears` under-approximates which moves remove adversity; currency still over-approximates which moves remove support |

The model check at depth 5 checks 920,081 transitions with no failures, and all 17 named discriminators give their expected values. `REV12=1` fails P5, P6, Q and the oracle; `REV11=1` fails Q and the oracle; `REV10=1` fails P1, Q and the oracle. §22 and round 13 (§27.20-§27.21) record the rest.

#### Revision 12 (prior) record

The `97e753f` Review (a fresh-context sub-agent of the author's model family, under stakeholder direction SD-8; `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-97E753F-NO-PASS.md`) returned NO-PASS with two blockers and seven findings, and no Serious Challenge. It recorded the `124b0b7` trajectories as closed and the restored monotone S2 as sound.

Both blockers were confirmed against the candidate text. Revision 11 approximated "stale" by "different key", but an equivalence judgment keeps a failing assessment current across exactly the change that splits the key (A). It also let a disposition count regardless of its own currency (B1), and while a blocking counter-challenge against an upholding was open (B2), contrary to its own prose. The family recurred after a simplification pass, so under the convergence owner revision 12 reconsiders the abstraction as a whole instead of adding exceptions. Revision 11 used one existence-keyed predicate for two questions of different kind. Revision 12 answers them separately. **Applicable adverse evidence** asks which failing evidence may still bear on a claim; it is a conservative S0 over-approximation per claim and evidence obligation. **Effective disposition** asks whether a disposition stands; it is an S2 value read only positively. The assessment key is removed.

| Finding | Repair (earliest owner) |
|---|---|
| **A** a failing assessment kept current by equivalence sat outside the key of a later pass; §6.6 and §7.4 computed disputedness differently | **Applicable adverse evidence** (§6.6, §7.4, §10, §22). Admissibility decides whether two assessments concern the same evidence: the evidence specification fixes the claim-defining regime, parameter instance and any execution attribute it constrains, and whatever it leaves free is execution variation. Applicability decides staleness: `applicable(x)` is `x`'s basis test with equivalence judgments counted by existence, validity entries by their content revision, and record entries by applicability. An applicable failing assessment conflicts with every passing one for the same obligation. One term, `ev(s, e)`, serves both validity and discharge |
| **B1** a disposition counted after its own basis moved | **Effective disposition** (§6.6). A support-tier disposition counts at `current(d)`, read positively in S2 |
| **B2** an upholding counted while a blocking counter-challenge against it was open | An upholding counts as a disposition only while in force, held across any loss boundary, and not contested by an open blocking challenge of either polarity. Its revocation keeps S1 polarity |
| N1 adoption provenance | Unchanged; still partial |
| N2 §15.4 supersession row; double supersession | Row corrected; dispositions may be re-recorded after a boundary, and supersession chains dispose (§6.6, §15.4) |
| N3 "S4 by construction" overstated | Applicability follows every content entry, so a moved oracle or tolerance subject makes the failing assessment inapplicable. An upheld challenge against a record in its record-mode basis disposes of it (§6.6) |
| N4 D1/D2 human attention keyed on a predicate | Keyed on the failing assessment's existence, as a floor item (§6.6, §7.9) |
| N5 decision class and independence of dispositions | R2 with independence from the claim's author; R3 for D1/D2 claims (§6.6, §6.8 step 3, §7.5) |
| N6 step 8 overbroad | Scoped to the request's content and structural changes; admitted evidence and challenges are never collateral regression (§6.8 step 8) |
| N7 per-replicate assessment | Manual item 11 fixes assessment granularity; reopen trigger added (§21, §26) |

The model check (`qualification/ssds80/s1_disagreement_model_check.py`) was rewritten. It adds execution moves with and without equivalence, prerequisite moves, supersession chains and an oracle written in plain-language form, and it evaluates the Review's discriminators by name. It is green for revision 12. Under `REV11=1` it reproduces A, B1 and B2, and under `REV10=1` the `124b0b7` trajectories. §22 and round 12 (§27.18-§27.19) record the rest.

The review route is unchanged: fresh-context sub-agent Reviews launched from a neutral handoff, with the shared model family recorded as a common-mode dependency (SD-8).

#### Revision 11 (prior) record

The `124b0b7` Review (GPT-6/Codex, fresh context; `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-124B0B7-NO-PASS.md`) returned NO-PASS with one blocker family and two findings. It recorded the one-enactment binding and the plain live-pass/live-fail case as closed, and the acyclicity-based uniqueness argument as mathematically sound.

The blocker was confirmed. Revision 10's `undisputed` read the *currency* of failing assessments. That made filing a challenge against the failing assessment, or withholding it at a loss boundary, permissive for the claim: the disagreement vanished without being resolved. Under the convergence trigger, revision 11 removes that dependence rather than adding a guard.

| Finding | Repair (earliest owner) |
|---|---|
| **A** challenging or loss-withholding a failing assessment lifted the disagreement cap | **Existence-keyed disagreement** (§6.6, §7.4, §10, §15.4). `disputed(K)` is an S1 predicate. It holds while a passing and a failing assessment of key `K` exist and some failing one has no in-effect disposition: a supersession by its assessor or the owner, an upheld challenge, or an `IMMATERIALITY` judgment. Each disposition counts only while not challenged, not superseded and not withheld by a loss boundary. The key gains execution identity, without seed or replicate, so stale failing evidence never conflicts by construction. Revision 10's inhibition edges and non-monotone S2 are removed, and the least-fixed-point uniqueness is restored. A bounded model check (`qualification/ssds80/s1_disagreement_model_check.py`) confirms the stated properties and detects revision 10's defect in sensitivity mode |
| N1 adoption provenance | Unchanged; still partial |
| N2 §22 provisional-discharge oracle narrower than §7.4 | Aligned: risk override *or* policy permitting provisional continuation |

**Review route.** On 2026-10-13 the stakeholder directed the author to "perform the remaining revise / review cycle yourself through the revision and sub-agent review cycle until all remaining blocking issues are closed". Subsequent Reviews are therefore fresh-context sub-agents of the author's model family, each launched from a neutral handoff. The shared family is recorded in every record as a material common-mode dependency.

#### Revision 10 (prior) record


The `fb3e542` Review (GPT-6/Codex in a fresh context, the fourth consecutive review from that family; `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-FB3E542-NO-PASS.md`) returned NO-PASS with two blockers and two findings. It recorded the revision-9 bootstrap, identity, settlement and oracle repairs as closed. Both blockers were confirmed: the §6.9 counting rule never limited an acceptance to its first enactment, and S2 and discharge chose an existing pass without regard to a live competent fail, contrary to the 7.2.1 evidence owner.

| Finding | Repair (earliest owner) |
|---|---|
| **A** a prospective acceptance could count again after demotion and identical restoration | **One-enactment binding** (§6.9, `ACC` §6.6). It counts only for work produced for the same bound obligation, with equal structure and a holding basis, and only for the first tenure it starts (`bind(j)`); afterwards it leaves `ACC` permanently. Rebase reuse before enactment is preserved |
| **B** a current pass could be selected while a current competent fail of the same evidence was live | **Assessment disagreement in S2** (§6.6, §7.4, §10, §9.3). A live conflict on an assessment key caps the evidence term at `P`, so validity and discharge stay visibly provisional. Resolution is only by the owner's authorized supersession or an `IMMATERIALITY` judgment. An adjudication obligation is derived, with human attention for D1/D2 claims. **Material change:** S2 uniqueness now rests on acyclicity of the combined support-and-inhibition graph that Admission maintains (step 5), not on monotonicity alone |
| N1 adoption provenance | Unchanged; still partial |
| N2 `D_n[C]` spelling in §22 | Fixed to `D_n[X]` |

§22 adds the Review's discriminators for both blockers and the uniqueness change. Round 10 (§27.14-§27.15) records the pass.

#### Revision 9 (prior) record


The `730490d` Review (GPT-6/Codex in a fresh context; `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-730490D-NO-PASS.md`) returned NO-PASS with two blockers and four findings. It recorded the revision-8 re-derivation as closing the input-read and paused-publisher trajectories. Both blockers are at the transformation owner and were confirmed from the text: step 4's promotion condition was a precondition of the frame that the acceptance needed, and frames were named by commit alone.

| Finding | Repair (earliest owner) |
|---|---|
| **A** frame existence required the prospective acceptance that only a reviewer in the frame can supply | **Inspection vs enactment** (§6.9, §6.8 step 4). A frame exists when the merge is clean and the structural delta is *well-formed*: every step-4 check, freezes included, except the *enactment condition*. Only the integrating admission requires a counting prospective acceptance. The proposed subject is in prospective tenure and invalid in the frame until accepted |
| **B** frames were named by commit, though the structure depends on the request's adoption set | **Transformation identity** `X = (B, C, A)`, fixed by the task result (§6.9, §6.3, §7.8, §11.2). Frames are `D_n[X]`. A prospective acceptance counts for a tenure only when the integrated transformation has the same structural delta and the acceptance's basis holds there (`ACC`, §6.6). Rebases follow the same rule |
| N1 adoption provenance | Unchanged; still partial |
| N2 §22 oracle contradicted the disclosed residual | Split: decisions stand without a foreign return to `B_n`; with one, the reversal must be detected and escalated (§22) |
| N3 repeated fences | A decision waits until a later `obs` shows the ref away from `B_n`; a non-`PENDING` classification is not enough (§15.3, §6.8 step 7, §22) |
| N4 trailing blank line in the `ac71fa9` Review record | Removed by a whitespace-only commit at the stakeholder's instruction |

Round 9 (§27.12-§27.13) records the pass. Nothing is added: identity hashes existing result fields, and the split partitions existing checks.

#### Revision 8 (prior) record


The `ac71fa9` Review (GPT-6/Codex in a fresh context; `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-AC71FA9-NO-PASS.md`) returned NO-PASS with three blockers and two findings. It recorded the stale-report ingress, the gate cycle and compound conformance as closed. All three blockers were confirmed by re-deriving them from the cited text. The Review also invoked the convergence owner's active simplification trigger, correctly: candidate currency had now failed three rounds (`f3608f5` B, `ac71fa9` A and B) and publication four (`8a75346` A, `ffbad17` N2, `f3608f5` C, `ac71fa9` C). Revision 8 therefore replaces each contract instead of adding another exception.

| Finding | Re-derivation (earliest owner) |
|---|---|
| **A** an implementer's recorded read of the unit it edits made its result stale in the frame | **Transformation frames** (§6.9). Each `content` entry of a frame record has a mechanically computed role. A *before-image* entry (base revision of a changed unit) is satisfied while the head keeps that revision and becomes a fixed fact after integration. An *output* entry is satisfied in the merged tree. A *context* entry is checked live. Step 6 and §6.4 now state roles; the revision-4 merged-tree exception is the same rule |
| **B** frames kept the admitted structure, so a promotion could not be judged as proposed; the integration carried no judgment while §12.2 required same-request acceptance | The frame also applies the candidate's structural delta, after step-4 validation. An independent reviewer records a **prospective acceptance** in the frame, which counts only for the tenure that the candidate's integrating admission starts (`ACC`, §6.6). Promotion and acceptance take effect in one admission; the integration still carries no new judgment. Restoration and adoption use the same path (§6.8 steps 3-4, §11.2, §12.2) |
| **C** a publisher paused after its ledger check could reverse a human's "keep `B_n`" | **Revocation by moving the ref** (§15.3). Any host that is not the publisher on its first attempt appends a *fencing absorption* and moves the ref to a no-content fence commit `F_n`, so no outstanding effect from `B_n` can apply. Human decisions are admissible only after the fence settles. A later return of the ref to exactly `B_n` by a foreign writer is detected as `LATE_PUBLICATION` with `CRITICAL` attention: a disclosed residual (§6.6 S0, §6.8, §7.9, §13) |
| N1 adoption provenance | Unchanged and still partial; it needs the stakeholder's restatement |
| N2 attempt-log integrity and host identity | §15.3 defines an intact log as monotonic for the publisher's identity; restored, copied, shared or inherited logs are not intact. Manual item 14 owns the realization |

§22 adds the discriminators the Review specified: a genuine `read(u@r0)` retained through the full production path, prospective promotion, restoration and adoption through the ordinary pipeline, and failpoints after the publisher's last step with a human decision admitted before release. Round 8 (§27.10-§27.11) records the re-derivation pass. No primitive, store or component is added, and four mechanisms are removed.

#### Revision 7 (prior) record


The `f3608f5` Review (GPT-6/Codex, a different model family; `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-F3608F5-NO-PASS.md`) returned NO-PASS with four blockers and two findings. It recorded the revision-6 repairs of the S1 revocation defect and the self-certified plan equivalence as closed. Each new blocker was re-derived from the cited text before repair, and all four were confirmed: step 6 checked reports' currency before step 7 could exempt them; a review of an unmerged candidate had no frame in which its basis could be current; one host's log was trusted about every host; and §25 required shadow evidence before authorizing the shadow build.

| Finding | Repair (earliest owner) |
|---|---|
| **A** a report submitted after its context moved was rejected at step 6 before it could be routed | Reports and challenges are **exempt from step 6**. Their basis is provenance, never consumed by any rule. The entry that rejects a stale request still admits the reports it carries (§6.8 steps 6-7) |
| **B** no currency frame for reviewing an unmerged candidate, so result → review → integration deadlocked | **Candidate frames** (new §6.9). Records about a candidate are evaluated in `D_n[C]`, the same derivation over the deterministic merge of `C` onto the observed tree. Integration admits exactly that tree, so the review is current after integration. Rebase and conflict rules follow (§6.4, §6.6, §7.7, §7.8) |
| **C** a non-publishing host's intact no-attempt log could re-publish after a deliberate reset | **Exclusive publication.** Each entry's publisher is the Admission host that appended it (per-host keys). It attempts at most once, behind a write-ahead intent, and checks the ledger head first. Every other `L = B_n` is ambiguous and goes to the human (§15.3, §15.6, §8.2, §13) |
| **D** §25 required shadow evidence before the D4 handoff that builds the shadow system | **Staged gates G1-G4** (§25, §23). Architecture accepted; shadow D4 authorized; implementation functionally accepted; per-subject cutover. Every criterion is kept and assigned to the boundary where its evidence can exist; criteria 13-16 are added |
| N1 adoption provenance partial | Recorded as partial in §0 and above. The 2026-10-12 instruction still needs the stakeholder's restatement; nothing claims the adoption sequence is independently verified |
| N2 compound conformance | Conformance is a set of classes; every routing applies; the Manual defines aggregation (§7.7, §21 item 25) |
| Strata note (§4 of the Review) | §6.6 uniqueness now states the two evaluations: polarity by earlier targets, force and continuity by later resolvers |

§22 adds discriminators that run through real Admission and production paths, for report ingress, candidate frames end to end, two-host ABA, and a non-runtime gate-dependency review. Round 7 (§27.8-§27.9) re-ran the Review's trajectories and attacked the repairs. It adds no primitive, store or component.

#### Revision 6 (prior) record


The `ffbad17` Review (fresh-context agent of the author's model family) returned NO-PASS with four blockers and seven findings. Each was re-derived against the owner it cites, not adopted as stated. All four blockers were confirmed: Blocker A by evaluating the S1 formula on the Review's trajectory, B-D by reading the cited text against itself. The stakeholder answered N3 and N1 on 2026-10-13. Their verbatim instructions, with acceptance of the revision-5 design principles and the aspirational reading of the doctrine-realization objective, are now in `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md`.

| Finding | Repair (earliest owner) |
|---|---|
| **A** an open challenge against an upholding un-revoked its target; a withheld pre-loss dismissal did the same (present since revision 3) | **Syntactic polarity** in §6.6 S1. A challenge against a restrictive upholding is a *counter-challenge* with no effect while open. Its successful upholding is a relaxer: challengeable, suspendable, and withheld by a loss boundary. No ungated record can relax anything, so withholding at any depth only restores blocks and revocations. §15.4 polarity table and §22 cases follow |
| **B** escalation persistence depended on undefined report currency; downgrade "discharged" human attention | **Existence-keyed obligations** (§7.9 Persistence). Every report-derived obligation closes only by an in-force resolving record; staleness only annotates. Raiser withdrawal of a floor item does not close it. Reclassification moves a non-floor item to the digest and is never a discharge (A8 reworded). `FINDING` is support-tier only. The §15.4 table covers every revision-5 kind |
| **C** results and reports were inadmissible under step 7; task binding was private and unauthenticated; independence failed open | **Authenticated task binding** (§7.5). The Dispatcher signs task envelopes with an issue key registered as a trust root, and records carry them. Binding is separated from discharge (§6.8 steps 3 and 7, §7.8). Lineage classes make independence fail closed: `UNKNOWN` lineage is never credited (§9.6, §15.6) |
| **D** monotone and decomposition classes were open predicates; the self-certified plan equivalence carried acceptance across content and scopes | **Closed control-tightening whitelist** over every contract field, with a direction per field. Anything else, including added obligations and unknown fields, is R2. Coverage is a rule-defined `PLAN_CONTROL` order (§6.4, §6.6, §6.7), not an equivalence or a judgment by the principal. Decomposition is replaced by **task partition** over one unchanged item. The plan-unit admission sequence is stated (§7.9) |
| N1 realization claims exceeded mechanisms | §1.1 restated as the stakeholder's tested aspiration (SD-6). Version binding made a D3 decision (§19.2), so E0 holds. A6 bounded to observable reads. §0 separation scoped to authenticated bindings. §19.3 claims bounded |
| N2 ABA default could silently reverse a deliberate reset | The default fails closed: `OVERTAKEN` plus human attention unless the attempt log positively shows no attempt (§15.3, §7.9 floor) |
| N3 authority traceability | Stakeholder decision record (above). The 2026-10-12 adoption instruction remains paraphrase-only; this session cannot reproduce it, and the record says so |
| N4 bidirectional scientific Review unlanded | Required review slot for scientific subjects (§9.6); §0.4 table row |
| N5 rebase conflicts | A conflicting rebase routes to a new iteration; machinery never resolves it (§7.8, K3) |
| N6 domain check force | Split into separate `HARD` and `HEURISTIC` templates (§7.7) |
| N7 index front matter and Protocol 7 status block; trailing whitespace in the F9D9DE8 record | **Not changed.** The index's `protocol_version` and Protocol 7 section belong to the closed Protocol 7 line and its own owner, not to this handoff. The F9D9DE8 record is an immutable historical Review record. Both are pre-existing and outside revision 6 |

The round-6 pass (§27.6) re-ran every `ffbad17` trajectory and attacked the repairs. It added one requirement: an item-level review after a task partition, unless policy waives it for named item kinds. The minimum-architecture pass (§27.7) adds one trust root and no component.

#### Revision 5 (prior) record


**Authority.** Stakeholder direction, 2026-10-13, given while this revision-4 handoff awaited Review. The stakeholder, who owns this line, observed that real execution never follows the initial plan; proposed role-based workflow execution with a principal executor that holds authority over the workflow and offloads work to other roles, implementers without authority to modify or redefine the workplan, and reviewers handed a clean context; required a deterministic flow of important discoveries and decisions to the human inspector; and directed:

> "the deterministic machinery should be the backbone for all the doctrine and functionality claimed by SSDP, and provide the deterministic machinery to reliably achieve them, as the latest qualification evidence already suggests that pure-language driven SSDP cannot reliably achieve all the functionality and improvements it claims. [...] Offload as much work as possible to deterministic machinery and let agent only handle things only it can handle, like semantic analysis, concept handling, and routine decision-making."

> "Work obligations, boundaries, and expectations be written by agents into machine-readable form. Then the implementer would implement, but the deterministic verification machine would verify whether all job obligations are complete and any over-stepping of boundaries. The machine should basically add an additional layer of check to make sure that each agents are within it's authorized boundaries, executed obligations, and reported as faithful. Complex semantic and logic are the job of the reviewer, but basic domain and keyword checks, and basic logic and mechanical verification should be achievable by the machines."

The stakeholder then accepted the decision-class classification (R0-R3, §7.5) as the design direction and instructed this revision to be drafted. That direction adds the doctrine-realization objective to §1.1; the editing agent added no objective on its own judgment. Everything else here is design under that direction and is open to the fresh independent Review.

**Diagnosis of revision 4 against the direction.** The revision-4 substrate (ledger, basis, derived obligations, item-level plan amendment, deterministic briefs, Admission authorization) could carry the direction without a new primitive, but the layer itself was absent or deferred: (1) no actor was qualified to reshape a plan, and §9.1 only forbade agents from declaring plan patches; (2) actor qualification was per judgment kind, with no per-task authority envelope, so "implementers may not edit the plan" had no enforcement point, and write scope was a §19.2 Manual decision while §8.1 treated intended affected units as an advisory prediction; (3) `report` had no routing, suspension or decision semantics; (4) a review brief could carry the author's own findings, contrary to the 7.2.1 workflow owner's independence rule; (5) nothing kept a material delegated finding alive on its way to the human, which the 7.2.1 scientific-inspectability owner requires and the 7.x study showed language cannot secure; (6) rigor was concentrated on ledger durability while the agent-facing workflow, where every 7.x failure occurred, was specified in about fifty lines. None of these is a Serious Challenge: the goals were consistent; the handoff was inadequate for them.

| Change | Where | Why |
|---|---|---|
| Doctrine-realization objective; allocation lines for routine coordination and mechanical conformance; two apparent conflicts dissolved | §1.1-§1.3 | stakeholder direction; §1.3 records why the new objective does not conflict with the others |
| Invariants A5-A9: typed role authority, machine-produced facts, verification necessary but never sufficient, non-droppable escalation, constructed reviewer independence | §2.5 | earliest owner for the new guarantees |
| Workflow roles, decision classes R0-R3, the principal as an obligation holder (not a daemon) | §7.5 | gaps 1-2 |
| Work contracts: typed plan-item sections with total verifier assignment, lint, adequacy by plan acceptance, frozen at issue; write scope as enforced authorization, separate from the advisory footprint | §7.6, §8.1 | gaps 1-2; stakeholder: obligations, boundaries, expectations in machine-readable form |
| Conformance verification: fixed check templates with declared force; four outcome classes; derived, not stored; executions by trusted runners | §7.7 | stakeholder: boundaries, obligations, faithful reporting checked by machine |
| Result handling in two ordinary admissions: result records first, integration after review | §7.8, §6.8, §9.1 | revision 4 left the order of implementation result, review and integration implicit |
| Typed reports, amendment requests, principal decisions with kind-restricted outcomes, monotone amendment and decomposition rules, escalation floors, recorded downgrades | §7.9 | gaps 3 and 5 |
| Iteration budgets and mechanical recurrence detection | §7.10 | convergence-and-cycle-economy owner: detection is mechanical, the response is judgment |
| Role briefs, reviewer-brief independence, decision brief, inspector view | §9.2, §9.4, §9.6-§9.8 | gaps 4-5; A4 activation without wording |
| Admission step 3 (role and write scope) and step 7 (contract conformance) | §6.8 | enforcement points |
| Record kinds named; protected surfaces extended; components unchanged | §6.3, §15.7, §16.1 | minimum architecture (§27.5) |
| §19.2 inputs decided at D3 where they are architecture; doctrine-realization levels E0-E3 | §19.2, §7.7 | 7.x lesson 5 |
| Non-goals, Manual items 23-27, qualification groups, Phase E scope, acceptance criterion, reopen triggers, round-5 passes | §20-§23, §25-§27 | — |

**Defects found by this revision's own pass (§27.4) and repaired before handoff:** an authority-defect request could be "resolved locally" by the principal (decision outcomes are now restricted by request kind and target domain, §7.9); a raiser could escape escalation by under-declaring materiality (a domain floor now makes every report targeting D1/D2 authority at least `MATERIAL`, §7.9); two concurrent coordination tasks could amend one plan from different bases (a change plan is a serialization surface for coordination, §7.5); an implementer could weaken the acceptance tests that verify its own work (evidence-specification units outside the contract are outside its write scope, and test-integrity checks are `HARD`, §7.6-§7.7).

#### Revision 4 (prior) record

The 8a75346 Review returned NO-PASS with two blockers. Both were treated as falsification hypotheses and reconstructed independently from the accepted 6.6 owners at the public-source commit named by `PROTOCOL-RELEASE-STATE.yaml` (`22f4bdba…`), in particular the concurrency owner (publication and retry are idempotent or transactionally reconciled; completion is never inferred from ref presence) and the storage owner (recovery must distinguish current, stale and historical state and must not make an older state look current). Both were confirmed. Neither repair adopts the Review's suggested mechanism as stated; each was re-derived for the smallest abstraction that closes the whole failure family.

| Finding | Verified against | Repair (earliest owner) |
|---|---|---|
| **A** a publication outcome could not legally enter the ledger | 6.6 concurrency owner; C3, C4. Revision 3 §15.3 required a recorded observation to resolve publication and forbade the append that would record it | **Successor-entry reconciliation.** Every entry records `obs`, the integration head Admission read immediately before appending it; for an admission `obs` is its base `B_n`. Admission entry `n` is the complete intent of its effect (`B_n -> C_n`). The first later entry carrying `obs` *is* the reconciliation: `PUBLISHED` or `OVERTAKEN` is a pure function of `(B_n, C_n, obs)` and immutable commits; `PENDING` means no such entry exists yet. The rule constrains the successor's *shape*, never requires a prior step: if `obs` is the expected head, the successor may be any entry, including the next ordinary admission; otherwise it must be an absorption of `obs` carrying no submitted records. No new state, record category, privileged path or extra entry in ordinary operation (§6.3, §6.6 S0, §6.8, §15.3) |
| **B** coordinated stale restore plus `LEDGER_LOSS` revived pre-loss authority | 6.6 storage owner; 6.6 workflow owner (restoration promotes nothing). Confirmed for every variant the Review lists | **Loss boundary.** A human-gated `LEDGER_LOSS` names the retained head, every known abandoned head with its witnessed admission status, and its evidence, and re-establishes the global control facts the lost interval could have changed (witness model, trust roots, ruleset). Its position is a continuity boundary. An S1 predicate `cont` withholds every *permissive* effect recorded before it — record currentness in S2, and the force of dismissals, withdrawals and risk overrides — unless a post-boundary record requalifies it or an in-force continuity attestation holds it. Restrictive effects (challenges, upholdings, supersessions, tenure ends, degradations) survive. The predicate reads only ledger records, so a product tree that agrees with the stale ledger cannot defeat it. Abandoning a provably never-admitted entry creates no boundary (P5, §6.6 S1, §13, §15.4) |
| N1 warrant validity inside one subject | 6.6 semantic-definition owner: acyclic warrant is legitimate; no self-support | Basis mode by subject boundary: prerequisites inside the record's own subject are `content`-mode, because the authored relation is part of that subject's accepted revision; `validity` only across subject boundaries (§6.4); positive discriminator (§22) |
| N2 qualification did not discriminate A or B | DS-001 | §22 publication-reconciliation and known-loss failpoint groups, written after the owners were repaired |
| N3 archived Protocol 8 §36 row missing | archived consolidated plan §36 (and §38, also unrowed) | §18.1 rows added; no mechanism |
| N4 Manual deferrals acceptable only while D4 stays gated | — | unchanged; D4 remains gated by Phases A and C |
| N5 quorum inequality sound | — | re-verified after the repairs (§27.2) |

**Where this revision departs from the Review's suggested repairs.**

- *A.* The Review hypothesized a privileged reconciliation successor, appended while normal admissions are blocked. Taken literally that adds a second entry and a second quorum round to every publishing admission, plus a special path. The derivation here shows the missing piece was not a state or a path but a *carrier*: Admission already reads the integration head to set `B`, so recording that read on every entry lets the next ordinary admission carry its predecessor's outcome. A dedicated entry appears only when the ref moved (the absorption that was always required) or to record an outcome while idle. The separate "publication outcome" and "live-ref movement" observations collapse into that one field. The Git ABA case (a foreign reset to exactly `B_n` after a successful compare-and-swap) is handled explicitly.
- *B.* The Review suggested a recovery epoch. No identifier is added: the `LEDGER_LOSS` position is the boundary. A tenure restart was rejected because tenure scopes only acceptance and would miss dismissals, evidence, completeness, equivalence, imports and consultations; a new ledger lineage was rejected as maximal disruption with the same requalification. The default reset is global because nothing mechanical can prove a retained effect unaffected; narrowing is an accountable, challengeable judgment, never an inference from product/ledger agreement.

**Defects found by this revision's own pass (§27.1) and repaired:**

- *S1 upholding defect.* `in_force` ignored upheld challenges: upholding a challenge against a dismissal closed the challenge and so silently re-enabled the dismissal, contradicting the stated "restores the block". An upheld challenge now removes its target's force permanently (§6.6 S1).
- *Re-routed support edges.* A structural change that alters `subj` changes the endpoints of existing `validity` entries; Admission step 5 now recomputes those edges before the acyclicity check (§6.8).
- *"Survives nowhere, never admitted".* Revision 3 inferred non-admission from absence of copies. An entry is admitted iff `q_a` witnesses held it; non-admission is now decided by a witness-count bound, and an entry that may have been admitted is a loss (§15.4).
- *Quarantine as loss defense.* Revision 3 described quarantine as what stops a truncated history reviving an acceptance. Quarantine only detects disagreement between product and ledger; the boundary is the defense, and quarantine is additional when the product is newer (§13).

#### Revision 3 (prior) record

The 441cf5c Review returned NO-PASS with three blockers. Each was treated as a falsification hypothesis, not as authority, and was reconstructed independently from the accepted 6.6 owners at the public-source commit named by `PROTOCOL-RELEASE-STATE.yaml` (`22f4bdba…`; the branch's evolving `source/` was not used as 6.6 authority). All three were confirmed. In each case the repair adopted here is stronger than the Review's minimum, and the out-of-matrix pass (§27) found and closed three further defects of the same families.

| Finding | Verified against | Repair (earliest owner) |
|---|---|---|
| **A** same-subject SCC admitted circular warrant | 6.6 semantic-definition owner: mutual *definitions* use an explicit simultaneous node; circular claim warrant is invalid; a dependency graph never warrants its endpoints. Evidence owner: lineage is acyclic | Closed, versioned relation vocabulary: each type has a semantic role and a cycle class. A **simultaneous-definition group** (SDG) is a *semantic* declaration, accepted with its subject's revision. Every relation cycle must lie inside one SDG and use only definitional edges. Unknown types fail closed. Condensation is representation only. Legality is checked at Admission and is also an S0 well-formedness fact that S2 consumes (§6.2, §6.6) |
| **B** foreign structural declarations took effect in S0 while quarantine lived in S3 | 6.6 workflow owner: repository presence promotes nothing. Evidence owner: restoring old content restores no validity. Risk-override rule: descendants never reset to accepted-current | **Observed vs effective structure.** Effective structure `Σ` is a fold of admitted structural changes. Absorption sets only the observed tree. Quarantine `Q` and the affected subjects `aff(Q)` are S0 facts, which S2 consumes (`ok(s)`). Acceptance belongs to a **subject tenure** and never revives. The challenge freeze applies to source and destination subjects. Adopting a foreign declaration means re-authoring it through Admission (§6.1, §6.6, §6.8, §11, §12.2) |
| **C** anchoring lag contradicted P4 | 6.6 storage and concurrency owners: partial or older state must not look valid; do not claim a commit before publication completes. The Review's L99/L100 world | **Strong P4.** An append is *provisional*; a witness-quorum checkpoint of the exact head *admits* it, and that is the commit point for every external effect. Read/write quorum intersection lets every qualifying evaluator see every admitted head. Publication, dispatch and current assertions follow admission. The bounded-lag mode and the multi-ref publication optimization are withdrawn (§2.4, §15.3-§15.4) |
| N6 same-subject circular-warrant discriminator | — | §22 relation-cycle trajectories |
| N7 anti-rollback expectation normalized the defect | — | §22 anchoring expectations rewritten to discriminate the strong contract |
| N8 structural-only foreign trajectories | — | §22 structural intake and tenure trajectories |
| N9 Manual deferrals acceptable only while D4 stays gated | — | unchanged; D4 remains gated by Phases A and C |
| N10 routing test respects DS-001 | — | unchanged; the test still reads frontmatter only |

**Where the repair exceeds the Review's minimum.**

- *A.* The Review asked for a semantic-role field. This revision also makes simultaneity itself semantic content, so declaring an SDG needs acceptance. It puts legality in S0, so a ruleset reclassification or an absorbed violation fails closed in validity, not only at Admission. It rejects self-relations, so single-object recursion stays the unit's own content.
- *B.* Of the Review's two options, this revision takes the observed/effective separation. It is the same rule already used for the ruleset (content proposes, an adoption record enacts), it adds no store (`Σ` is derived from the ledger), and it makes quarantine a lower-stratum fact by construction. It adds the tenure lifecycle the Review asked for. It also closes two paths the Review did not name: re-scoping a challenged *destination* subject, and an acceptance revived by `LEDGER_LOSS` truncation (§27.3; that quarantine-based defense proved partial and is superseded by the revision-4 loss boundary).
- *C.* "Synchronous" anchoring alone is not enough: a fresh clone that reaches only witnesses lacking the newest checkpoint would still accept the older head. This revision therefore makes read/write quorum intersection part of the contract (`q_a + r > N + f`). It withdraws the multi-ref publication optimization, which published before anchoring. It adds lineage-retirement checkpoints, so a purged lineage cannot be presented as current from a stale mirror (§15.5).

#### Revision 2 (prior) record

Design revision 1 (`f9d9de8`) re-derived the problem from the governing objectives, independently of the befe678 vocabulary. It replaced the four-graph, event-sourced, epoch and frozen-plan design with a smaller one (§3, §17), and restored lineage routes that befe678 had dropped from the authority index. Design revision 2 (`441cf5c`) kept that core and repaired the f9d9de8 Review's findings, reconstructed against the same 6.6 owners; two further recursion defects were found while repairing B2. Rows below record what revision 2 did; where revision 3 changed the mechanism, the row says so.

| Finding | Verified against | Repair (earliest owner) |
|---|---|---|
| **B1** byte-preserving split manufactured child acceptance | 6.6 kernel: a lower mechanism gains no authority; workflow owner: a clarification that narrows admissible interpretation is a semantic mutation unless established representation-only. The f9d9de8 rule also regressed befe678's "structural split requires no false semantic claims" | Acceptance is of an exact `(subject, scope, revision)`. Refinement creates **parts** of the unchanged subject; acceptance never moves by rule. A part becomes its own subject only through a qualified acceptance judgment (§6.1, §12.2) |
| **B2** currency/validity recursion admitted two fixed points | 6.6 semantic-definition owner: mutual definitions use an explicit composite node; circular warrant is invalid | Derivation is four strata with a monotone least fixed point in the support tier and well-founded challenge recursion. Admission keeps the support dependency graph acyclic (§6.6). *Revision 2 also made simultaneous groups composite subjects and licensed any same-subject relation cycle; revision 3 replaced that with SDGs and role-based cycle legality (Blocker A)* |
| B2 (additional) derived `acc(policy)` fed derivation of the rules that compute `acc` | same | The ruleset in force is a ledger fact named by a human-gated adoption record (§6.6 S0) |
| B2 (additional) discharge required "every triggered obligation discharged" — a negation over currency inside validity | same | Removed from discharge; collateral impact is an Admission legality check (§6.8 step 8, §7.4) |
| **B3.1** remote multi-ref atomicity assumed | Git `atomic` push is a server-advertised capability | Single-ref append everywhere; integration publication is a reconciled effect (§15.3). *Revision 2 kept atomic multi-ref push as an optional optimization; revision 3 withdrew it because it would publish before admission* |
| **B3.2** hash-valid rewind invisible to fresh clone | 6.6 storage owner: recovery must not make partial/older state appear valid | Declared threat model; signed checkpoints held by witnesses outside the replica's control plus participant high-water marks; fresh clone without a witness is never current. *Revision 2 still allowed an undetectable rewind inside the anchoring lag; revision 3 re-specified currentness as quorum admission (Blocker C, §15.4)* |
| **B3.3** new lineage does not remove a leaked secret | 6.6 security owner: exposure needs rotation/history remediation; deleting the latest copy is insufficient. Git owner: `main` history is never discarded | Closed no-free-text schema, bounded Admission checks, breach protocol with rotation, replica invalidation, sanctioned purge or new repository, explicit yielded guarantees (§15.5) |
| **N1** Architecture 1.6.0 transfer incomplete | the 26 frozen invariants and frozen surfaces, plus implemented Core | Per-invariant table (§16.2). Two f9d9de8 "preserved" claims (inv. 2, 26) were inaccurate and are corrected |
| **N2** routing test parsed prose | test inspected | Test now parses frontmatter: lineage closure via `supersedes`, routing via the index's `current_handoffs`. Semantic adequacy stays with Review |
| **N3** index reassigned Stage H itself | index and Protocol 7 Stage H text | Index and §0.2 phrase the relationship prospectively; only Protocol 7's owning closeout can retarget its obligation |
| **N4** widening not executable | §6.4 of f9d9de8 | Exact scope chain, boundary-completeness judgment, relation class, whole-tree fallback (§6.5) |
| **N5** `Change` primitive and cross-repository scope | primitive audit | `Change` demoted to a typed Admission request (§6.8); external units and the cross-repository boundary specified (§11.4) |
| N6 befe678 archival identity | blob re-checked locally | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` at `befe678` and in the archive; unchanged |

Revision 2's out-of-matrix and minimum-architecture passes (§27) repaired four further abstraction defects: carve-out cutover vs holistic legacy acceptance; completeness surviving scope-membership change; direct push to the ledger ref; challenge escape by re-scoping unchanged content (the ordinary-Admission path; revision 3 closed the foreign path).

### 0.2 Protocol 7 Stage H routing (discharged)

The Protocol 7 consolidated workplan (Stage H) assigned its closeout "the Protocol 8 inheritance reconciliation" of `SSDP-8.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-CONSOLIDATED`, which this file supersedes. Protocol 7 closed at 7.2.1 (stakeholder ratification 2026-10-12, `qualification/ssdp70/STAKEHOLDER-RATIFICATION-2026-10-12-PROTOCOL-7.2.1.md`) without authoring that reconciliation; its 7.2 cycle appended only an inputs list (§37.2a, workplan `SSDP-7X-SKILLS-ONLY-RELIABILITY-AND-QUALIFICATION-V2` O-10) to the then-active consolidated plan. On 2026-10-12 the stakeholder, who owns both lines, directed that this branch be rebased onto the accepted 7.2.1 base and this handoff aligned to it. §0.4 is that reconciliation, against the successor target the index already named. It advances the pre-cutover baseline, binds the final Protocol 7 inputs, adopts the governing version only because the stakeholder instructed it, selects no new architecture, and authorizes no D4. The closed Protocol 7 workplan is a historical handoff and is not rewritten; the authority index records the discharge.

### 0.3 Project Engineering Memory basis

This is replacement/migration design for mature machinery, so the PEM predicate fires. Accepted/base memory, re-resolved for the 7.2.1 reconciliation: `PROJECT-ENGINEERING-MEMORY.md` on `main` at `af0455753e20ee54a969c844872e29e270007211`, blob `1561797125622f355f84eb27319f87e8fa4227d9` (`memory_schema_version` 1, `reconciled_through` `23e46543c174a8451bbadc402df63538105eab10`). The blob is the one design revisions 1-4 used (then on `main` at `2585b73f00420daca185a4fbb9ac42a79473eda1`). `main` has since absorbed the 6.6 Stage F and the 7.0-7.2.1 cycles without a memory write, so that interval is uncovered: the absence of a 7.x entry proves nothing. The 7.x qualification lessons live in qualification evidence and enter this design as evidence-only inputs through §19, not as memory. This branch carries no overlay. Historical Applicability Set (unchanged):

| Entry | Binding | Disposition for this design |
|---|---|---|
| PC-001 frozen historical profiles | `AUTHORITY_BOUND` (versioning owner) | Applicable and mandatory through its owner: every version-bound profile/resource stays independently preserved (§24, §16.2). |
| SP-002 self-reference-safe identity | `EVIDENCE_ONLY` | Applicable: admission records reference commits and ledger heads, never the object that contains them; the checkpoint that admits entry `n` lives at witnesses, outside entry `n` (§6.8, §15.4). |
| FF-001 premature immutable publication | `EVIDENCE_ONLY` | Applicable to genesis, cutover, replacement lineages after a confidentiality incident, and SSDS release: no immutable identity is published before every required route and record validates (§12.5, §15.5, §23). Applicable by analogy to currentness: no ledger head is published or asserted current before the durability condition that makes the claim true holds (§15.3). |
| DS-001 synthetic fixtures do not discriminate real-owner defects | `EVIDENCE_ONLY` | Applicable to qualification (§22) and to the routing regression test (N2): synthetic/string checks bound only mechanical properties. |
| SP-001 repair canonical source, regenerate derivatives | `EVIDENCE_ONLY` | Applicable by analogy: derived views are regenerated from ledger and content, never patched (§6.6). |

### 0.4 Protocol 7.2.1 inheritance reconciliation and governing-version adoption (2026-10-12)

**Authority.** Stakeholder instruction, 2026-10-12: rebase SSDS 8.0 onto `main` after the 7.2.1 merge so that it points at the current SSDP 7.2.1 base, and align this workplan to that baseline. Under the versioning owner's binding-versus-adoption rule, that instruction is the authorized adoption request of the authority owning this workplan. The editing agent identified the bindings, reconciled the obligations and recorded the result; it adopted nothing on its own judgment.

**Rebase.** The eight branch commits were replayed unchanged onto `main` at `af0455753e20ee54a969c844872e29e270007211`, whose `PROTOCOL-RELEASE-STATE.yaml` names 7.2.1 accepted-current. The replay was conflict-free, and branch-only content stays confined to this workplan, its archived predecessors, `qualification/ssds80/`, the authority index and the routing test. Rebasing rewrote commit identities but no reviewed bytes: at every replayed commit this workplan, the three Review records, the befe678 archive (`af9c005b…`), the index and the test are byte-identical to the original. The Review records and §0.1 keep citing the original identities, which map as follows:

| Original | Rebased | Content |
|---|---|---|
| `befe678` | `513da27` | graph-native hypothesis (design basis) |
| `f9d9de8` | `e62be2f` | design revision 1 (Reviewed: NO-PASS) |
| `9d51f01` | `1cd2766` | f9d9de8 Review record |
| `441cf5c` | `25ed4c3` | design revision 2 (Reviewed: NO-PASS) |
| `d9720e1` | `c6bc328` | 441cf5c Review record |
| `8a75346` | `6a3d03a` | design revision 3 (Reviewed: NO-PASS) |
| `a88f270` | `0b3093d` | 8a75346 Review record |
| `9475e8d` | `edf816a` | design revision 4 |

The one tree difference is intended. The archived consolidated Protocol 8 plan is byte-identical to its last active version on `main` (blob `cc795f4058f99041c751c97ce46e7bcf5483ec9e`, previously `c229202f…`). That version adds §37.2a, the 7.2 inputs appended after the old basis, which §18.1 now dispositions.

**Adoption, 6.6.0 to 7.2.1.** Protocol 7 keeps every accepted 6.6 capability. Between `22f4bdba` (6.6) and `aaeaf8b6` (7.2.1), the owners that a §0.1 repair was verified against either did not change (kernel, semantic-definition, Git) or changed only additively (workflow, evidence, concurrency, storage, security, versioning). The additions are scientific-inspectability routing, Channel C gate evidence, product-scope acceptance, bidirectional scientific Review, the realized-record/observation overlap with CHALLENGES inquiry status, inspection and export trust boundaries, weighing retention before loss, and the frozen 6.6-7.2 profiles. No repair basis is withdrawn, so `[6.6]` tags keep their meaning as doctrine carried unchanged into 7.2.1, and no design-revision-4 mechanism changes. The newly applicable obligations, and where each is met:

| 7.x obligation (7.2.1 owner) | Why it applies here | Met at |
|---|---|---|
| D3 authority content (O1): realized record, intended reader, routine questions, visibly marked product inspectability surfaces (architecture, scientific-inspectability) | this is D3 authority for software that mediates retained evidence and human-gate evidence | §1.4 |
| Channel C gate evidence: a separable non-narrative core first; disclosure for consequential decisions; tension assessments at D1/D2 revision gates; no unqualified closure when missing records could change the judgment; adequacy is semantic (workflow) | SSDS renders gate briefs | §9.4, §21 item 10 |
| Product-scope acceptance only by the stakeholder or task authority, never technical D3 Review alone (workflow, scientific-inspectability O3) | SSDS records judgments that could accept a marked surface | §14, §2.1 S12 |
| A tension's canonical home is an evidence record or native issue; one canonical home per finding; no universal discovery database (scientific-inspectability) | the ledger references findings and evidence | §2.1 S13, §10, §19 |
| Realized-record/observation overlap; inquiry status (exploratory or confirmatory) as a separate attribute on `CHALLENGES` (evidence) | SSDS represents observations and challenges | §10, §21 items 3 and 11 |
| Inspection and export surfaces, and tension or disposition homes that non-owners can write, are trust boundaries (security) | SSDS exposes derived views and references such homes | §15.7 |
| Weigh later scientific judgment before irreversibly discarding or aggregating retained evidence (storage) | ledger purge and breach procedures, retention of referenced objects | §21 item 14 |
| Profiles 6.6, 7.0, 7.1 and 7.2 frozen and independently testable (versioning, PC-001) | SSDS coexists with document-controlled profiles | §24, §2.9 B1 |
| Bidirectional scientific Review: faithfulness to authority, and whether realized behavior challenges or qualifies it (workflow) | SSDS renders review briefs for scientific subjects | §9.6 (required review slot) |
| Search for recorded tensions before relying on accepted D1/D2 authority (entrypoint Tensions duty) | does not apply to this workplan, which relies on no accepted project D1/D2 authority; it applies to agents SSDS briefs, as an input to brief design | §19 |

**Evidence re-evaluated.** The three NO-PASS Review records stay applicable as history, because their verification basis (the 6.6 owners at `22f4bdba`) means the same at 7.2.1. No executed SSDS evidence exists to go stale. The fresh independent Review covers design revision 4 and this reconciliation together; since 2026-10-13 it covers design revision 5, which carries revision 4 unchanged and adds the workflow layer (§0.1).

**Bound inputs and baseline.** The final Protocol 7 inputs are in §19. The pre-cutover baseline is in §24.

## 1. Problem, objective and allocation

### 1.1 The engineering problem

SSDS 8 coordinates stochastic reasoning agents and humans over evolving scientific software while preserving SSDP's hierarchy of semantic authority. Wherever an answer is mechanically decidable, it must answer mechanically: what is authoritative; what depends on what; what changed; what is stale; what work is legal now; what may proceed concurrently; what context a task needs; what an agent modified; whether a result still applies to the state it was produced against; and what genuinely needs semantic judgment or human authority. It must absorb manual, external and legacy change without corrupting canonical state. It must let an old repository become governed progressively without stopping production. It must let history be reconstructed after failures, migrations, rollback attempts and schema evolution.

**Doctrine realization (stakeholder objective, 2026-10-13; `STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` SD-5, SD-6).** The deterministic machinery is meant to be the backbone through which SSDP's doctrine and claimed functionality are realized, not a bookkeeping aid beside a language protocol whose compliance is probabilistic (§19.3). The stakeholder holds this as an aspiration whose limits must be tested: "a hope and realistically the limit to what a machine can do must be tested. I do not expect perfection any time soon, but working toward it as we discover challenges". SSDS therefore claims, for each duty, only what its mechanism and its evidence establish. Every SSDP duty is assigned a realization level (§7.7): enforced mechanically, detected mechanically and routed to judgment, carried as a required typed answer whose presence is checked, or left to judgment and Review. Work proceeds by typed roles whose authority Admission enforces on authenticated task bindings (§6.8, §7.5). Obligations, boundaries and expectations are machine-readable and mechanically verified (§7.6-§7.7). A material discovery that is reported reaches the human inspector through a route on which no agent can close a floor item, and from which a non-floor item leaves only by a recorded, visible, challengeable reclassification (§7.9, §9.8). Agents do what only they can do: semantic analysis, concept handling, creative concretization and routine decisions. Machinery can guarantee that a duty's mechanical part was performed and that a recorded outcome survives. It cannot guarantee that a judgment was good, that an agent noticed what it did not report, that a raiser named the right target, or that reads it could not observe were recorded (§8.4, §27.4, §27.6). Doctrine realization is measured against the 7.2.1 baseline (§22), and its results decide what is claimed.

### 1.2 Allocation principle

```text
mechanically decidable question                  -> deterministic machinery, answered exactly
mechanically decidable only conservatively       -> deterministic machinery, answered by sound
                                                    over-approximation (never under-approximation)
precision beyond the conservative answer         -> a focused semantic judgment that narrows it
judgment already made, basis still current       -> reused mechanically; never re-asked
mechanically checkable conformance               -> verification; necessary, never sufficient (§7.7)
unresolved semantic question                     -> agent, in the role the obligation kind selects (§7.5)
routine coordination decision                    -> principal role; recorded and challengeable (§7.5, §7.9)
designated authority decision                    -> human gate
canonical state change                           -> single serialized admission
```

*Machines over-approximate; judgment narrows; recorded judgment is reused until its basis moves.* Byte identity is a mechanical fact; what a set of bytes is accepted *as* is a semantic fact (§6.1). The agent is a semantic reasoning resource, never a bookkeeper. SSDS 8 succeeds only if added deterministic machinery reduces, rather than transfers, complexity to agents and humans.

### 1.3 Consistency of the governing goals (Serious Challenge check)

Six apparent conflicts dissolve under the architecture rather than being engineered around:

- *Mandatory deterministic control vs never stopping production.* Production commits remain ordinary Git; non-closure blocks canonical governance status, not execution (§11, §12).
- *Minimal agent context vs "absence of an edge is not independence".* Context is minimal only within judged-complete scopes; elsewhere the basis widens conservatively and the brief says so (§6.5, §9).
- *Single canonical writer vs multi-host teams.* One writer per ledger is enforced by compare-and-swap on one authoritative ref (§15.3).
- *Append-only audit vs confidentiality.* Prevention makes sensitive ledger content structurally unlikely. When confidentiality and append-only continuity truly conflict, a human-gated breach protocol lets confidentiality win and states which audit guarantees yield (§15.5).
- *Autonomous agent execution vs human control of what matters.* Decision classes are fixed by system semantics and policy, never chosen by the agent (§7.5): agents settle routine decisions, and the human sees exactly the decisions and discoveries the escalation floors route, plus a digest of the rest (§7.9, §9.8).
- *Mechanical verification vs semantic adequacy (S9).* Verification can reject, return or point, but no mechanical outcome discharges an obligation a judgment must discharge (A7, §7.7). The machine removes the checkable part of the reviewer's burden; it never replaces the review.

Four residual limitations are real but not contradictions:

- Semantic dependencies an agent uses without the machinery observing them cannot be captured by any read-set scheme (§8.4).
- Circular reasoning stated only in prose, without declared relations, can be found only by semantic review (§6.2).
- No architecture can infer the existence of a state whose every copy and checkpoint has been destroyed, or reconstruct the content of admitted history known to be lost. SSDS therefore asserts currentness only for durably witnessed state, under a declared witness model, and makes a known loss a boundary that retained authority cannot silently cross (§15.4).
- Machinery cannot make an agent notice what it did not notice, nor make a judgment good. The 7.x study found that detection did not respond to protocol text in any arm (§19.3), and enforcement does not change that. SSDS guarantees instead that whatever is detected, by agent or check, survives to its owner, and that the review step is never skipped (§7.9, §27.4).

The design bounds and discloses each; none weakens a stated invariant. No Serious Challenge is raised.

### 1.4 Scientific inspectability (O1)

SSDS 8 produces no scientific results of its own. It does decide which realized results count as current evidence, what human gates receive and what is retained, so the 7.2.1 authority-content duty applies to it. Stated proportionately:

- **Material realized record (of SSDS itself).**
  - *Contents:* admitted records and their bases (judgments; realizations with their execution basis; assessments; challenges with their inquiry status; gate decisions; risk overrides; loss boundaries and continuity attestations), publication outcomes, and intake and quarantine dispositions.
  - *Retention and destructive boundaries:* the ledger is append-only except under the human-gated breach protocol (§15.5). Raw data, logs and narrative findings stay in native project homes, referenced by content identity (§10). An unavailable referenced artifact degrades binding health but erases no history.
- **Intended readers.** Stakeholders and human-gate holders; independent reviewers; agents, only through briefs (§9).
- **Routine questions.**
  - What governs this subject, and at which revision?
  - Is this result still current against its basis, and if not, what moved?
  - Which evidence supports or challenges this claim, and which is stale or unavailable?
  - What did a gate decide, on which evidence core, and with which findings and tensions visible?
  - What is withheld by quarantine or a loss boundary, and why?
  - What did each agent do, in which role and within which boundaries; what did verification find; and which reported findings were escalated, merged or downgraded, by whom?
- **Product inspectability surfaces (marked).**
  - *Within the requested deliverable (this architecture):* S3 derived views and `ask`/`read` answers that name their qualified head (§6.6, §9.1, §9.3); task briefs with incompleteness notices (§9.2); gate briefs led by a separable non-narrative core (§9.4); the conformance view of each result (§7.7); the inspector view and its digest (§9.8).
  - *Beyond the requested deliverable:* None. Projection of project scientific records, exploration interfaces and discovery stores stay with project products. SSDS references their homes and adds no universal observation database (§10, §20).

## 2. Reconstructed invariants

Source tags: **[6.6]** accepted 6.6 SSDP doctrine, carried unchanged into accepted-current 7.2.1 (§0.4); **[7.x]** doctrine added by Protocol 7.0-7.2.1; **[7.x-E]** evidence from the 7.x qualification study (a design input, not doctrine); **[P8]** consolidated Protocol 8 proposal (reviewed under 6.1, never accepted-current); **[S8]** SSDS 8 objective from stakeholder/task authority. Tags show where a requirement comes from; they do not make P8 or 7.x-E items accepted authority.

### 2.1 Semantic

- **S1** D1-D4 semantic authority; one current owner per material normative claim; current ownership acyclic; D1-D4 is a layered DAG, not a waterfall; a higher abstraction never depends on a lower concretization. Mutual *definition* is legitimate only through an explicit simultaneous-definition declaration. A definition, a definitional dependency or a graph condensation never warrants a claim. Circular warrant, authority, evidence, provenance or lineage is invalid. [6.6]
- **S2** Concretization fidelity and abstraction adequacy are distinct; Serious Challenge stops counterfeit closure; a risk override leaves dependents visibly provisional. [6.6]
- **S3** Authority mutation: proposal -> independent falsification where required -> required human ratification -> acceptance -> bounded impact -> reconcretization. Repository presence promotes nothing. A clarification that narrows admissible interpretation is a semantic mutation unless established representation-only. [6.6]
- **S4** Evidence: specification -> realization -> observation -> assessment; observations immutable, assessments superseding; target vs execution dependency; stale passing evidence never confirms, stale failing evidence never refutes, and failing evidence whose realization still bears on the claim keeps it qualified until disposed of, whatever else in its assessor's context moved; binding health tracked separately from historical existence. [6.6]
- **S5** Absence of a relation establishes independence only inside a scope explicitly reviewed complete for that relation family. [6.6]
- **S6** Specialized substantive inference requires the exact canonical meaning; definitions establish no truth, existence or adequacy; conflicting simultaneous meanings are adjudicated by their owner, never by order or recency. [6.6]
- **S7** Version-bound interpretation; no retroactive reinterpretation; no self-adoption; capability, not wording, is the compatibility oracle. [6.6]
- **S8** PEM is non-authoritative project learning; HAS is task-local. [6.6]
- **S9** A machine-control vocabulary never converts a semantic judgment into a deterministic fact; agent PASS is a recommendation. [6.6][P8]
- **S10** Acceptance attaches to an exact semantic subject, in one tenure, at an exact scope and revision. Content identity, scope identity, subject role and tenure, lineage, dependency coverage, semantic equivalence and acceptance are distinct facts; no mechanism infers a later one from an earlier one. [6.6, derived from S1, S3, S6]
- **S11** Effective governance is admitted, never observed. Repository presence changes no ruleset, structural role, membership, scope, kind or coverage boundary, and promotes no acceptance; declarations found in content are proposals until admitted. An acceptance belongs to one subject tenure and never revives once that tenure ends; restoring old bytes or old declarations restores no validity. [6.6 workflow: repository presence promotes nothing; 6.6 evidence: restoration does not restore validity; derived from S3, S10]
- **S12** Gate evidence is decision-sufficient, with a non-narrative core separable from agent interpretation, and its adequacy is a semantic judgment. A marked product inspectability surface beyond the requested deliverable is accepted only by the product-scope owner (stakeholder or task authority), never by technical D3 Review alone. [7.x workflow, scientific-inspectability]
- **S13** A persisted finding has exactly one canonical home; a tension's home is a project evidence record or native issue, never accepted authority text. No universal discovery database exists. [7.x scientific-inspectability]

### 2.2 Control

- **C1** Exactly one serialization point for canonical state changes per governed ledger. [P8]
- **C2** Same canonical inputs and rule version give exactly one derived state. [P8]
- **C3** Nondeterministic facts (time, filesystem, Git remote, resources, model output, human judgment) enter only as recorded typed records. [P8]
- **C4** External effects follow intent -> idempotent/reconcilable effect -> observed outcome; ambiguity is reconciled before retry. [P8]
- **C5** Unknown required semantics fail closed; unknown optional fields follow the declared compatibility contract. [P8]
- **C6** A disagreement between semantic content and its control representation is an integrity defect that blocks dependent transitions. [P8]
- **C7** Control data is the minimum needed to select, validate, serialize, replay or audit a transition. [P8]
- **C8** C2's derivation is well-founded: every predicate has one value for every admitted input, with no self-supporting acceptance and no negation through recursion. [6.6 S1 + P8 C2]

### 2.3 Concurrency and isolation

- **K1** A result is admitted only if everything it relied on is still current, or it is revalidated. [P8][S8]
- **K2** No two mutating executions share one working tree. [P8]
- **K3** A clean textual merge is not semantic orthogonality. [S8]
- **K4** Correctness never depends on predictions being complete; predictions may only reduce wasted work. [derived here]

### 2.4 Provenance and replay

- **P1** Every canonical change records what, who, against which basis, under which rules. [P8]
- **P2** Historical decisions are never recomputed under newer rules, resources or interpretations. [P8]
- **P3** Derived state is rebuildable; canonical records win any disagreement. [P8]
- **P4** Currentness is asserted only for durably witnessed state. A ledger head is *current-qualified* only when a witness quorum holds its exact identity and it extends every checkpoint and high-water mark the evaluator observes, and every current-state assertion names its qualified head. A valid historical prefix, an appended-but-unadmitted entry and an unverifiable head are never presented as current. Rollback, fork, loss, provisional and unqualified states are distinguished and fail closed. The guarantee is exact under the declared witness model (§15.4); there is no lag window. [6.6 storage/concurrency/security owners + P8 §15.2]
- **P5** Known loss of admitted history is a continuity boundary. Restoring an older state — of the ledger, the product or both — never makes authority current across admitted history known to have existed and to be unrecoverable. After the loss is recorded, every effect recorded before it that could only add support or relax a block is withheld until requalified after it, or held unaffected by an accountable, challengeable human attestation; restrictive effects survive. Abandoning entries provably never admitted creates no boundary and costs no requalification. [6.6 storage owner: recovery must not make older state appear current; 6.6 workflow owner: restoration promotes nothing; derived from P4, S11]

### 2.5 Agent interface and context

- **A1** Routine work never requires reading machine records, decoding history, maintaining edges or reconstructing Git topology. [S8]
- **A2** Context is version-bound, explains why each item is present, labels its epistemic status, and states known incompleteness. [S8]
- **A3** One logical task/result contract across harnesses and transports; a zero-context agent can locate its task from a minimal bootstrap. [P8]
- **A4** A duty a task owes is either carried in that task's brief or enforced mechanically. Activation and selection are deterministic, never left to wording, and mandatory depth is never reached through conditional "read X when Y" routing. Briefs carry only the duties that are triggered, because surplus duty text causes narration nobody owed. [7.x-E, ratification lessons 1-4]
- **A5** Every execution acts in exactly one workflow role for exactly one task. What it may write, which record kinds and outcomes it may submit, and which decisions it may make are fixed by the role and the task's work contract and are checked at Admission; a role confers no authority, it bounds which proposals are considered. No agent role other than the principal of a plan may change that plan's items or contracts, no agent role may change verification rules, and no actor reviews or accepts its own work. [S8; 6.6 workflow: independence; derived from T1, S9]
- **A6** The factual content of a result (what changed, what ran, what it returned, and what was read through the interface or observed by a harness adapter) is produced by machinery. Reads machinery cannot observe are a disclosed residual (§6.4, §8.4). An agent supplies judgment in typed slots, and any factual claim it still makes cites the record that establishes it. [S8; 7.x-E lesson 5; P8 §17]
- **A7** Verification is necessary, never sufficient. A mechanical check can reject, return work or point a reviewer at something; it never discharges an obligation that a judgment must discharge, and a heuristic check never changes a disposition. No control decision depends on parsing prose. [S9; P8 §17; derived here]
- **A8** A material finding survives to its owner. Escalation to the human is a derived obligation keyed on the escalating record's existence, never its currency, and only an authenticated human judgment discharges it. An intermediate role may annotate, merge or upgrade it. It may move a non-floor item out of the human's open list into the digest only by a recorded, visible and challengeable reclassification, and never a floor item. [7.x scientific-inspectability: material delegated findings survive to the human ("may rank and condense, never drop"); S8]
- **A9** Reviewer independence is constructed, not requested: a review brief excludes the author's narrative and conclusions, the reviewing execution differs from the author's, and material common-mode dependencies are recorded. [6.6 workflow: a subagent that receives the author's conclusions is not independent]

### 2.6 Repository and Git

- **G1** Git is content, isolation, transport and history substrate, never workflow authority. [P8]
- **G2** Transport artifacts are not merged into product history. [P8]
- **G3** No record must contain the identity of the commit that contains it. [P8][6.6, SP-002]
- **G4** Secrets and private telemetry never enter project repositories; a suspected exposure requires rotation and history remediation, not deletion of the latest copy. [P8][6.6]
- **G5** `main` is never deleted or force-moved to discard reachable history; destructive history operations need explicit operation-specific authorization. [6.6 Git owner]

### 2.7 Migration and recovery

- **M1** One route admits every change of unknown provenance — agent overstep, manual edit, collaborator branch, legacy import, drift. [S8]
- **M2** Adoption is progressive and coexists with production. [S8]
- **M3** A governed region never has two simultaneously current authorities or governing processes. [P8][S8]
- **M4** Discovery may run bottom-up; acceptance runs top-down. [S8]
- **M5** Unknown remains visibly unknown; migration never invents certainty or alters behavior silently. [S8]
- **M6** In-flight older-version work is drained, pinned or explicitly migrated, never scraped. [P8]

### 2.8 Trust and security

- **T1** Agent outputs are untrusted proposals until admitted. [P8]
- **T2** Unknown artifacts are never executed or deserialized to classify them. [S8]
- **T3** External, evidence and memory text is data, never instruction. [6.6]
- **T4** Human decisions and canonical entries are authenticated through a declared trust mechanism; no guarantee is claimed beyond what is implemented. [P8]

### 2.9 Backward compatibility

- **B1** Older version-bound work stays governed by its declared version and immutable source; frozen orchestration profiles stay independently testable (PC-001). [6.6]
- **B2** Rollback is version rollback to an immutable baseline, never simultaneous dual authority. [P8]
- **B3** Protocol 7 inheritance is final at 7.2.1 and is bound in §0.4 and §19. The pre-cutover baseline is the 7.2.1 recovery (§24). [7.x][task authority]

### 2.10 Conveniences that had been masquerading as architecture

These do not follow from §2.1-§2.9: four canonical graph families; a global authority epoch; whole-plan freezing with a global replanning stop; event-sourced storage of state transitions and stored lifecycle FSMs; a hand-authored work graph with many node kinds; pre-declared write claims as the concurrency-correctness mechanism; a separate write-side graph transaction engine with dirty flags; separate context-resolver and semantic-projection components; a dedicated ingestion engine; legacy aggregates as a special node type; a mandatory refactor of all authority documents into per-node files; MCP as the interface definition; a first-class change primitive; and same-repository multi-ref atomicity. Each is replaced (§17) or retained only as a delegated D4 option.

## 3. Diagnosis of the befe678 hypothesis

The befe678 hypothesis correctly identified the need for machine-readable relations, derived code dependencies, context retrieval, isolation, reconciliation and progressive migration. Its weaknesses are structural:

1. **Synchronization burden by construction.** Four canonical graph families with independent lifecycles share identities and cross-family edges (EVIDENCES, CONCRETIZES from code, work claims over authority). Keeping them consistent required a GraphTransaction, a candidate overlay, GraphDelta and dirty-flag machinery. The decomposition created that machinery; the problem did not need it.
2. **Global coupling where the problem is local.** AuthorityEpoch totally orders independent authority changes, so unrelated acceptances advance the epoch every task is bound to. Whole-plan PlanRevision plus a conservative stop on new mutating tasks during replanning turns a local amendment into a project-wide barrier.
3. **Parallel staleness systems.** Staleness of tasks (epoch/plan binding), context (ContextBundle), evidence (EvidenceGraph status) and graphs (DIRTY) were separate mechanisms. All four answered one question: *did anything this conclusion relied on change?*
4. **Stored state that is really derived.** Execution/outcome/validity/authority/evidence FSMs were stored and reduced from events, although almost all of them are functions of content plus recorded judgments.
5. **Correctness resting on predictions.** WorkClaims declared before execution were the parallelism-safety mechanism; they are necessarily incomplete for semantic conflicts across disjoint files, generated outputs and dynamic dependencies.
6. **Fragile canonical history.** Canonical history lived only in a private local SQLite store; loss of that store with intact repositories lost all accepted decisions, and clone/fork/move had no history path.
7. **Interface leakage.** Agents were asked to propose PlanPatch node/edge operations, maintain WorkClaims, call `change.reconcile`, and choose among seventeen operations.
8. **Migration as a special subsystem.** LegacyAggregate, an ingestion engine with four modes, and a separate repository-explainability rule duplicated what one coverage partition with adaptive granularity provides.
9. **Lossless-representation defect.** It declared supersession of the consolidated Protocol 8 plan while omitting material inherited guarantees (semantic/control projection rule, forward compatibility, transport-artifact and self-reference rules, bootstrap locator, human-gate/risk-override propagation, cutover quiescence, pre-cutover baseline identities, Protocol 7 inputs, versioning preservation, most failure qualifications).

Two befe678 capabilities were sound and are reinstated after later revisions lost them: *structural split into sub-aggregates requires no false semantic claims* (lost at f9d9de8; §12.2), and *the authority order is a DAG after explicit condensation of legitimate simultaneous definitions, while circular warrant stays invalid* (blurred at 441cf5c; §6.2).

## 4. Alternatives considered

| Candidate | Core idea | Verdict |
|---|---|---|
| **H0** befe678 | Four canonical graphs, event-sourced reducer, epochs, frozen plan revisions, graph transactions, legacy aggregates | Rejected as a whole for §3. Retained capabilities are mapped in §18.2. |
| **H1** verified incremental computation | Content-addressed units; an immutable ledger of judgments and observations; everything else derived by versioned rules; staleness = basis change (build-system "early cutoff") | **Selected core.** One mechanism answers staleness, readiness, impact and context; locality is natural. |
| **H2** logic knowledge base | All facts, authored and derived, in a Datalog/relational store with an event log of assertions/retractions | Hybridized. Kept: derivation is stratified, with a monotone least-fixed-point support tier (§6.6). Rejected: a general rule language as architecture. Rules are parameters of fixed predicate templates. |
| **H3** Git-only documents-as-state | Plans, judgments and statuses as repository files; CI as gate | Rejected as primary: anyone can push a PASS file, concurrent status edits conflict, and status-in-documents is exactly what SSDS 8 removes. Kept: Git as content store, isolation, replication and transport, including the ledger's object chain (§15). |
| **H4** hosted service | Central database plus durable-workflow engine | Rejected: operational cost, not local or lightweight, polling-first violated, no benefit for the single-team scale that must work first. |

Comparison of the serious candidates (H0, H1+H2+H3 hybrid):

| Criterion | H0 | Selected hybrid |
|---|---|---|
| Authority integrity | relations in separate graph store can drift from content | authored relations live inside the content they belong to; drift impossible by construction |
| Determinism | reducer over events | stratified pure derivation over ledger + content; fewer stored states |
| Duplication | four graphs + control state + caches | one content store, one ledger, derived index |
| Implementation complexity | high (sync, overlays, dirty tracking) | moderate (derivation engine with memoization) |
| Agent burden | many operations, plan/claim maintenance | six logical operations; no bookkeeping |
| Recovery | local store loss is fatal | ledger replicated as Git objects; currentness only for quorum-witnessed heads |
| Concurrency | claim-based, incomplete | optimistic validation at admission; claims advisory |
| Migration | separate subsystem | refinement of coverage; acceptance moves only by judgment |
| Evolution | reducer versioning | ruleset versioning; admissions never re-derived |
| Lightweight/local | yes | yes |
| Harness independence | MCP-shaped | transport-neutral logical interface |
| Scientific fit | generic | basis carries regime, parameter instance, seed, backend, precision (§10) |

## 5. Architecture overview

```text
                         agents / humans
                               |
              Interface  (open · ask · read · report · submit · decide)
                 |                                   |
          (queries, read-only)              (typed admission requests)
                 v                                   v
         Derivation Engine  <-------------------  Admission  ---- sole ledger writer -----+
   S0 observed content · effective structure ·  validate · append (single-ref CAS) ·     |
   S1 challenges · S2 support ·                 anchor (witness quorum) · publish        |
   S3 obligations, readiness, impact, context   (outcome: next entry)                    v
          |            |                               Ledger Store: Git object chain on one authoritative
   Content Model    Analyzers                          ref; verification; current-head qualification
   observed declarations  derived relations             (quorum checkpoints, high-water marks)
   authored relations                                   Integration ref (product branch): published projection
          \            /                                                                 ^
           Git content store  <-- workspaces (isolated) -- Dispatcher                    |
                                                       scheduling · execution effects · harness adapters
                                                       (operator state: private, local; never canonical)
```

Four primitives:

1. **Unit** — a governed region of repository content with stable identity and a content-addressed revision; leaf units partition content; composite units group leaves into one acceptance **subject**; structure is effective only as admitted (§6.1).
2. **Relation** — a typed, directed fact between units, classed as authored, derived or proposed, whose type carries a closed semantic role and cycle class (§6.2).
3. **Record** — an immutable ledger entry: a judgment, an observation, an admission or a lifecycle record (§6.3).
4. **Basis** — the exact typed set of unit revisions and records a record relied on; currency is computed from it (§6.4).

A **change** is not a primitive. It is a typed Admission request (§6.8) whose identity and audit trail live in the admission record. Everything else — lifecycle states, validity, obligations, readiness, staleness, impact sets, context bundles, graph views, diffs, dashboards — is **derived**.

## 6. Primitives and derivation

### 6.1 Unit, scope and subject

A **unit** `u` has: a stable logical identity; a kind and owning domain (D1, D2, D3, D4, plan, evidence specification, generated, external, unclassified); a **scope** (the repository regions it covers: paths, or anchored spans within files); a declaration source; and a role: **leaf** or **composite**.

- **Leaves partition content.** For every admitted tree, leaf scopes partition all governed content. That is every tracked path outside declared ignore patterns, and every span of a sectioned file; each belongs to exactly one leaf. Genesis may declare a single catch-all `UNCLASSIFIED` leaf. Partition validity is checked at every admission.
- **Subjects.** A **composite** declares its members (leaves or nested composites); its scope is the union of its members' scopes. Composites form a laminar family: any two are nested or disjoint. Every unit, leaf or composite, is either a **subject** (the default) or a declared **part** of an enclosing composite. `subj(u)` is `u` if `u` is a subject, else the nearest enclosing composite that is a subject; laminarity makes it unique. It is a function of *effective* structural declarations only (below). A subject may contain nested subjects (a carve-out, §12.2); its scope, and so its revision, still covers their content. A subject has one acceptance; its parts have none of their own.
- **Composite subjects are not simultaneous definitions.** A composite subject groups content for one acceptance: a refinement parent whose holistic acceptance has not been divided (§12.2), a legacy document, a carve-out container. It licenses nothing about relations. Mutual definition is licensed only by a **simultaneous-definition group** declaration (§6.2), which is semantic content of one enclosing subject. Revision 2 used one construct for both, and that conflation admitted circular warrant inside a subject (441cf5c Blocker A).
- **Declaration.** Structural declarations live only in the repository-owned **unit manifest** (path patterns, heading paths, symbol sets, kinds and domains, roles, memberships, identity and rename lineage, the governed-content boundary). Inline **anchors** may only delimit leaf spans inside a manifest-declared unit, and they inherit its kind, domain and enclosing composite. An anchor never declares role, membership, kind, domain or scope. Semantic declarations live inline in content or in the semantic part of a manifest entry. External declaration is mandatory for immutable or version-pinned artifacts, which are never rewritten to acquire anchors. Confining governance-affecting declarations to the manifest keeps the observed/effective distinction on one small, identifiable surface.
- **Revision.** `rev(u, T)` = hash(content identity of `scope(u)` in tree `T`, semantic declarations within `scope(u)`). **Content identity** hashes the scope's bytes in declared order after rule-defined conservative normalizations; pure structural boundary markers carry no relation payload and are normalized out. **Semantic declarations** are the authored relations, defined-object declarations, simultaneous-definition declarations and joint-invariant declarations of the unit and of every unit inside its scope. **Structural declarations** are excluded from `rev`, but they determine scope, `subj` and tenure. They are therefore exactly the declarations that could reroute governance without changing any revision, so they take effect only as admitted (below). Revisions are computed from Git content; no separate hash graph is stored. Granularity is adaptive: a file, a section, a symbol set, or an entire legacy subtree.
- **Scope identity.** `scope_id(u)` identifies the set of regions independently of their bytes. Changing what a subject covers is a scope change, not a revision change.
- **Observed and effective structure.** `decl(T)` is the set of structural declarations parsed from tree `T`, keyed by declaration (unit identity plus field). The **effective structure** `Σ_n` is the set of structural declarations in force at ledger position `n`. It is a fold over admitted entries: genesis admits `Σ_0`, and an ordinary or intake admission changes `Σ` exactly by the structural changes it authored or explicitly adopted (§6.8 step 4). **Absorption never changes `Σ`.** `Σ_n` is derived from the ledger and the trees its records name; it is not a second stored copy.
  - *Resolution.* Effective scopes are resolved against the bytes of the observed tree `T_n` (§6.6 S0). A region that no longer resolves has content identity `ABSENT`. Governed observed content outside every effective leaf belongs to the reserved **uncovered region**, which has status `UNCLASSIFIED`.
  - *Quarantine.* `Q_n = { k : decl(T_n)[k] ≠ Σ_n[k] }` holds the **quarantined structural deltas**: what the repository declares but governance has not admitted.
  - *Governance-affecting deltas.* A quarantined delta is **governance-affecting** iff adopting it would change, for some unit, its identity, kind, domain, role or enclosing composite; for some subject, its `scope_id` or the byte regions it covers; or the governed-content boundary. Otherwise it is **governance-neutral**: a re-partition of leaves inside one subject's unchanged regions into parts of that subject with its kind and domain.
  - *Affected subjects.* `aff(Q_n)` is computed by comparing `Σ_n` with `Σ_n` overridden by `decl(T_n)`. It contains every effective subject that is, or contains, a unit named by a governance-affecting quarantined delta, plus every effective subject whose signature or regions such a delta would change. A foreign declaration that would carve a part out of `P` as a nested subject therefore affects `P`, even though `P`'s own regions would not change.
- **Subject tenure.** A subject's **governance signature** is `(role = subject, scope_id, kind/domain, governance mode)`. Its **tenure** `τ(s)` is the first ledger position of the current uninterrupted run over which `s` has been an effective subject with an unchanged signature.
  - A tenure ends when `s` is demoted to a part, its `scope_id` changes, its kind or domain changes, or its governance mode changes. A later restoration starts a new tenure.
  - Acceptance belongs to a tenure (§6.6 `ACC`). Challenges, revocations and supersessions target exact triples and records, and they survive tenure changes.
  - Byte-preserving refinement of `s`, and carve-out promotion of one of its parts, leave `s`'s tenure unchanged.
- **Single definer.** A unit may declare that it defines a named semantic object. Two current units defining the same object is an integrity conflict that blocks dependent use until the owner adjudicates (S6).
- **Status lives in the ledger.** Acceptance, governance mode, reconstruction status, lifecycle and effective structure are derived from records (§6.6), never enacted by editable fields in unit content.

The facts that S10 keeps distinct, and what establishes each:

| Fact | Established by | Never implies |
|---|---|---|
| content identity | hashing (mechanical) | any of the facts below |
| scope identity | effective unit declarations | that bytes or meaning are unchanged |
| subject role and tenure | effective structure, changed only by admission (S11) | acceptance; a past tenure's acceptance; anything from a repository declaration alone |
| lineage / provenance | refinement and rename declarations, ledger history | acceptance or equivalence |
| simultaneous definition | an SDG declaration, accepted with its subject's revision (§6.2) | warrant of any member claim |
| dependency and completeness coverage | relations; `COMPLETENESS` judgments; analyzer completeness declarations | equivalence or acceptance; widening only adds context |
| semantic-subject equivalence | `EQUIVALENCE` judgment by a qualified actor (byte identity and rule normalizations only mechanically) | acceptance of any new subject |
| acceptance | acceptance judgment on exact `(subject, scope_id, rev)` in the subject's current tenure under the owning domain's contract | anything about another subject, scope or tenure |

Units rather than files or Git blobs give locality: per-file identity would make any edit to a long authority document invalidate every conclusion that relied on any part of it. Adaptive granularity keeps the declaration cost proportional to need. Locality of *acceptance* is never cheaper than one semantic judgment (§12.2).

### 6.2 Relation

A **relation** is `(subject, type, object, class, provenance)`.

- **Authored** relations are declared inside the subject unit's scope (or its manifest declaration) and are therefore part of every enclosing subject's revision. They take effect when that subject's revision is accepted, and change only by changing content. Semantic relations and their meaning cannot drift apart, and a human editing a document edits its relations in the same act.
- **Derived** relations are computed by a versioned analyzer from content (imports, calls, build edges, generated-from, test-to-code). They are never edited and never stored as canonical; they are cached under their derivation key.
- **Proposed** relations are records (from search, analyzers with semantic uncertainty, or agents) awaiting acceptance. A proposal is accepted only by an admitted content change to the subject's authored relations.
- **Record-level relations** (challenge targets, adjudication, supersession of assessments) are properties of records, not edits to their targets: a challenger never owns the challenged unit.

Stored direction is subject -> prerequisite, following the evidence and definition owners; reverse traversal is impact analysis, not a second relation. A generic "related-to" supports no closure (S5).

**Semantic roles and cycle classes.** The relation vocabulary is part of the ruleset in force (`ρ_n`, §6.6 S0). It is closed and versioned. Every type carries mandatory attributes: direction, **semantic role**, **cycle class**, permitted classes (authored or derived), layer constraint, and completeness eligibility. Cycle legality is decided by the cycle class, never by common subject identity.

| Role | Representative types | Cycle class | What the relation can do |
|---|---|---|---|
| `DEFINITIONAL` | `USES_DEFINITION` | `SIMULTANEOUS` | fixes meaning; never warrants (6.6: a dependency graph does not warrant its endpoints) |
| `WARRANT` | `DERIVED_FROM`, `ASSUMES`, `DEPENDS_ON` | `ACYCLIC` | carries claim support or prerequisite order |
| `GOVERNING` | `CONCRETIZES`, `CONSTRAINED_BY` | `ACYCLIC`, plus layer direction | carries authority |
| `EVIDENTIAL` | `EVIDENCES` (evidence specification -> claim), `EXECUTION_DEPENDS_ON` | `ACYCLIC` | binds evidence to target and execution |
| `PROVENANCE` | `GENERATED_FROM` | `ACYCLIC` | regeneration order |
| `LINEAGE` | `SUPERSEDES`, `REPLACES` | `ACYCLIC` (6.6: lineage is acyclic) | replacement history |
| `STRUCTURAL` | analyzer-derived imports, calls, build edges, test-to-code | `NEUTRAL` | context, impact and widening only |

These constraints on the vocabulary are checked when a ruleset is adopted:

- `SIMULTANEOUS` is permitted only for `DEFINITIONAL` types.
- `NEUTRAL` is permitted only for derived `STRUCTURAL` types; no authored type is `NEUTRAL`.
- No rule may name a `NEUTRAL` type as a validity-mode or warrant prerequisite. Code-level recursion (mutually importing modules, recursive calls) is therefore legal and inert: it cannot carry warrant.
- A type with an attribute missing cannot be adopted.

A ruleset adoption that removes, renames or reclassifies a type declares, for existing uses in content, `READ` (alias to a defined type), `MIGRATE` (ordinary content changes through Admission) or `REJECT`. The adoption gate is shown the derived impact: the subjects that would become ill-formed. Historical views keep the vocabulary in force at their position. Relations in `LEGACY(p)` content that SSDS extracted heuristically are proposed, not authored, so vocabulary evolution never invalidates a legacy subject. A type absent from `ρ_n` has unknown required semantics (C5). Admission rejects any authored relation of that type, inside or outside a cycle. In absorbed content, such a relation makes its subject ill-formed (below). A future type therefore fails closed until a ruleset adoption defines its role and cycle class.

**Simultaneous-definition group (SDG).** An SDG is a *semantic* declaration, made inline or in the semantic part of a manifest entry, naming a set of units whose meanings are defined together. Being semantic, it is part of the enclosing subject's revision: adding, removing or changing an SDG is a semantic change that needs acceptance, so simultaneity is never asserted by structure or presence. Rules:

- all members of an SDG have one common `subj`, the declaration itself lies inside that subject's scope, and an SDG never contains a subject;
- SDGs are laminar;
- no relation is a self-relation: recursion inside one object's definition (a recurrence, a fixed-point equation) is that unit's own content.

An SDG is a declaration, not a unit and not a primitive.

**Cycle legality.** Let `E` be every authored relation and every derived relation whose cycle class is not `NEUTRAL`, over effective units in the observed tree. `E` is legal iff **every cycle of `E` lies inside the member set of one SDG and uses only `SIMULTANEOUS` edges**. Equivalently, every strongly connected component with more than one unit is contained in one SDG and contains no edge of another class. Consequences:

- a `DERIVED_FROM` or `DEPENDS_ON` cycle is illegal, even inside one subject or one SDG;
- a mixed cycle (definitional plus warrant) is illegal;
- a cycle spanning two sibling SDGs is illegal unless an enclosing SDG is declared;
- nested SDGs are permitted.

Contracting each SDG yields the acyclic order used for layer checks, ordering and impact. **The contraction is a representation, not a warrant.** The contracted node has no warrant of its own. Definitional edges fix meaning only. Every claim inside an SDG still needs `ACYCLIC`-class warrant, none of which can lie on a cycle, and its subject's acceptance.

Structural rules checked at admission (§6.8 step 4) on the merged tree:

- referenced units exist;
- every relation type is known in `ρ_n`;
- no authored dependency runs from a higher abstraction to a lower concretization;
- cycle legality and the SDG rules hold;
- plan items do not depend on lower-layer work in a way that inverts the authority order.

The same rules define the S0 predicate `well_formed(s)` (§6.6). `well_formed(s)` is false when any unit of `s` lies on an illegal cycle, carries a relation of unknown type or inverted layer direction, belongs to a malformed SDG, or conflicts with the single-definer rule. A violation that reaches the tree without Admission — absorbed content, or a ruleset that reclassifies a type — therefore invalidates every involved subject in S2, not only an S3 report.

Machinery checks *declared* relations. Circular reasoning stated only in prose, with no declared relation, is a semantic defect that acceptance review and Challenge must find (residual risk, §8.4).

**Completeness is a judgment.** `COMPLETENESS(X, R)` asserts, for a scope `X` (a set of units) and a relation class `R`: *every `R`-prerequisite of a unit in `X` that lies outside `X` is declared* (boundary completeness). For a singleton scope `{u}` this is the outgoing completeness of `u`, typically attested during `u`'s acceptance review. Its mechanical minimum basis is content-mode entries on every unit in `X` plus the identity of `X`'s membership, so adding, removing or editing a member makes it non-current. An analyzer may supply boundary completeness only for derived classes, only within the scope and constructs its version declares complete, and never where it detected an incompleteness marker (reflection, plugins, dynamic registration, generated code, runtime configuration, external consumers). Completeness never transfers through refinement or scope change.

### 6.3 Record and ledger

The **ledger** is the single canonical store of everything that cannot be derived from content. It is append-only, totally ordered, authenticated (§15.4), and serialized in a canonical versioned **closed schema** (§15.5). Every record carries: identity, kind, actor and actor class, subject, basis, outcome, schema and ruleset version, provenance, and content-identity references to any substantive report artifact. A record submitted for a task also carries its task binding: the issued envelope's fields and signature, and the lineage class of the execution (§7.5), so the binding is replayable from the ledger alone. It also declares its evaluation frame: the admitted state, or a transformation identity `id(X)` (§6.9). Records contain no free text, essays, equations, patches or raw logs (C7).

| Record kind | Produced by | Examples |
|---|---|---|
| **Judgment** (support tier) | agent, human, or semantic-role tool | acceptance; conformance; equivalence; completeness; evidence assessment; plan acceptance; intake classification and disposition, including adoption of a quarantined structural delta; legacy or external acceptance import; reconstruction proposal; task result (outcome classification, typed slots, claim references, §7.8); report (finding, amendment request, blocker, human question, §7.9); coordination decision, including task partition, and materiality reclassification (§7.9); human acknowledgment (§9.8); human lineage attestation (§7.5) |
| **Judgment** (challenge tier) | qualified actors per policy | challenge (blocking or not); Serious Challenge; adjudication; withdrawal; risk override; continuity attestation after a loss boundary (human-gated, §15.4) |
| **Observation** | machinery | evidence realization from a trusted runner (§10); consultation of an external ledger's qualified head (§11.4); analyzer output recorded because the analyzer is nondeterministic or expensive; artifact availability; check execution by a trusted runner (test runs, mutation testing, static analysis over a candidate, §7.7) |
| **Admission** | Admission only | accept or reject of an admission request with reason codes, validated basis, ruleset version, request identity, base commit (its `obs`), resulting admitted (merged) commit and adopted structural deltas; absorption of an observed integration head (§15.3) |
| **Lifecycle** | Admission, human-gated where required | genesis (project identity, ledger location, authoritative replica, trust roots, witness set and quorums, initial effective structure, baseline commit); ruleset adoption; schema migration; governance-mode transition; project fork; replica redesignation; witness-set redesignation; ledger loss (a continuity boundary, §15.4); ledger fork resolution; confidentiality-incident lineage migration and old-lineage retirement; redaction notice |

Every record enters through Admission. A ledger entry is *provisional* when appended and *admitted* once a witness quorum holds its head (§15.3); a judgment is *recorded* when its entry is admitted; whether it is *current* is derived (§6.6). Rejections are recorded too, so provenance includes what was refused and why. Every entry except a human-gated recovery lifecycle entry also records `obs`, the live integration head Admission read immediately before appending it. That one field is how publication outcomes and foreign movement of the integration ref enter canonical history (§15.3); no separate publication-outcome or live-ref observation kind exists.

The ledger holds only what derivation consumes or audit requires. Purely operational facts — task issue, reservations, leases, worktree creation, agent launch, retries — live in the Dispatcher's durable operator journal under the same intent -> effect -> observed-outcome discipline (C4). They influence scheduling, never derived workflow state. Execution provenance that matters for audit (route, harness, model, attempt) travels inside submitted records.

### 6.4 Basis

A **basis entry** is `(mode, target, consumption class)`. The mode is fixed by the rule for the record's kind when the record is admitted, and it is never inferred at evaluation.

| Mode | Target | Satisfied when (§6.6) | Used for |
|---|---|---|---|
| `content` | unit revision `(u, r)` | evaluated in the record's frame and, for a candidate frame, in the entry's before-image, output or context role (§6.9): `cur(u) = r`, or an equivalence path from `r` to `cur(u)` for the entry's consumption class, or, for the plan-acceptance class `PLAN_CONTROL` only, `cur(u)` reached from `r` by the rule-defined control-tightening order (§7.9) | everything the actor saw: the judged revision, context supplied or read, change base, content behind evidence; governing or warrant prerequisites inside the record's own subject (below) |
| `validity` | unit revision `(u, r)` | the content condition holds and `subj(u)` is valid | **direct** governing or warrant prerequisites in **another** acceptance subject only, as the rule names them by relation role; never a `NEUTRAL` relation (§6.2) |
| `record` | an earlier record `x` | `x` is current | premises that are themselves judgments: completeness, evidence realization/assessment, plan acceptance |
| `identity` | a record, or `(subject, scope_id, rev)` | always (immutable fact) | targets of challenge-tier records and supersession; equivalence endpoints |

**Mode by subject boundary.** Let `S_x` be the subject of a record's target: the subject itself for an acceptance, `subj(u)` for a judgment about part `u`. A governing or warrant prerequisite `v` with `subj(v) ≠ S_x` gets a `validity` entry where the rule requires validity. A prerequisite with `subj(v) = S_x` gets a `content` entry. The authored relation that makes `v` a prerequisite — for example `b DERIVED_FROM a` between parts of subject `G` — is a semantic declaration inside `S_x`'s scope, so `S_x`'s own acceptance already covers it, and any edit to `v` changes both `rev(v)` and `rev(S_x)`. A record therefore never holds a `validity` entry on its own subject. This gives the required properties together: no acceptance supports itself, because no edge runs from `S_x`'s support to `valid(S_x)`; no warrant is circular, because warrant relations are acyclic inside and across subjects (§6.2); an edit to the relied-on part makes the record stale through its `content` entry; and an `EQUIVALENCE` judgment on that part for the record's consumption class restores it without re-review (early cutoff, §6.7). Modes are fixed at admission. If a part is later promoted, records admitted earlier keep their `content` entries, which stay exactly as strong, because the former subject's frozen scope still covers the promoted bytes (§12.2); records admitted afterwards use `validity` on the new subject.

Transitive governing authority is reached through the validity of direct prerequisites, not listed separately; this is what makes early cutoff predictable (§6.7). A unit the actor actually saw also gets a `content` entry, so backdating reaches a record only through units it did not see. A rule may declare consumption classes that let an `EQUIVALENCE` judgment cover a `content` entry; the default class is exact.

The basis of a record is the union of:

- the **mechanical minimum** computed by the rule for its kind: direct governing subjects (validity), the judged revision and supplied context (content), the dependency closure over the relation classes the rule requires (§6.5), the completeness judgments that closure used (record), and the change base;
- **recorded reads** made through the interface, plus harness-observed reads where an adapter can observe them;
- **declared reliance** the actor adds at submission.

An actor can add to the mechanical minimum, never remove from it.

### 6.5 Conservative widening

Widening solves dependency uncertainty only. It never establishes equivalence, completeness or acceptance, and a widened basis never makes a part valid (§12.2).

**Enclosing-scope chain.** For a unit `u`, `chain(u) = X_0 ⊂ X_1 ⊂ ... ⊂ X_m`, built deterministically:

```text
X_0 = {u}
then each effective composite containing u, smallest first   (laminar, so nested)
then the directory containing u's declaration source, then each ancestor directory
X_m = every effective unit in the governed tree, plus the uncovered region
each step: X_{i+1} = X_i ∪ units(next scope); skip steps that add nothing
```

The chain is built from effective structure `Σ_n`, never from quarantined declarations. Uncovered observed content has no judged completeness, so it is reachable only through the whole-tree fallback, where the brief lists it as `UNCLASSIFIED`.

**Closure algorithm.** For seed set `S` and relation class `R` (the rule's class; a union class needs completeness covering each member class):

```text
closure(S, R):
  reached := S; queue := S
  while queue not empty:
    u := pop(queue)                                     -- order irrelevant to the result
    for v in declared R-prerequisites(u) (authored + derived): enqueue v if new
    if not exists X_i in chain(u) with current COMPLETENESS(X_i, R) for every member class:
        W := X_m                                        -- whole governed tree
    else:
        W := the smallest such X_i                      -- undeclared prerequisites lie inside it
    for v in W: enqueue v if new
  return reached                                        -- a least fixed point; finite
```

The result is the smallest set containing `S` that is closed under declared prerequisites and the widening rule, so it is independent of traversal order. Exact closure (no widening beyond `{u}`) needs a current singleton completeness judgment on every reached unit. **Fallback** when no judgment exists anywhere in `u`'s chain: the whole governed tree. The brief marks it `UNBOUNDED` and lists declared external units; undeclared external dependencies cannot be enumerated and are stated as such. *Missing dependency knowledge never proves independence.*

### 6.6 Derivation

The **Derivation Engine** computes, as a pure function,

```text
derive(L_n, content of trees referenced in L_n) -> exactly one derived state D_n
```

where `L_n` is the ledger prefix through position `n` (its observations included). The ruleset and the effective structure are read from `L_n` (S0 below), not supplied from outside. Derivation is defined for every authenticated prefix. *Which* prefix may be presented as current is decided outside derivation by currentness qualification (§15.4), so witness reads never enter `D_n`.

Derivation has four strata. A stratum reads only lower strata. Within S1 and S2 recursion is permitted only in the forms proved unique below. The SSDS system version fixes the derivation semantics. Project policy only parameterizes fixed predicate templates: judgment kinds, actor qualifications, mechanical-minimum composition, consumption classes, passing outcomes, required gates, and obligation triggers. A ruleset whose parameters would make a lower stratum read a higher one is rejected at adoption. There is no general rule language.

**S0 — observed content, effective structure and ledger syntax.**

- *Ruleset in force* `ρ_n`, including the relation vocabulary of §6.2: the latest admitted `RULESET_ADOPTION` record at or before `n`, naming an exact system ruleset version and an exact policy content hash.
- *Expected integration head and observed tree.* `E_n` is the integration commit governance evaluates at `n`: genesis's baseline commit; `C_k` after an admission `k` (`C_k = B_k` for a records-only request); `obs_k` after a plain absorption `k`; `F_k` after a fencing absorption `k`, whose tree equals `obs_k`'s (§15.3); unchanged after any other entry. The observed tree is `T_n = tree(E_n)`. For a publishing admission that is its admitted merged tree from its own position onward, before any publication is observed.
- *Publication classification* (§15.3). For an admission `k` with `C_k ≠ B_k`, and for a fencing absorption `k` (with `B_k = obs_k` and `C_k = F_k`), `pub(k)` is `PENDING` while no later entry carries `obs`; otherwise it is `PUBLISHED` or `OVERTAKEN`, a function of `B_k`, `C_k`, the `obs` of the first later entry that carries one, and the immutable commits reachable from that `obs`. `late(k)` holds when `pub(k) = OVERTAKEN` and a later `obs` newly reaches `C_k` or an equivalent publication.
- *Loss boundaries and exposure* (§15.4). Every admitted `LEDGER_LOSS` record is a boundary at its own position. `exposed(x, X)`, for a record `x` before the boundary and a set `X` of subjects and records, holds if `x ∈ X`, `x` targets a subject or record in `X`, or `x` targets an exposed record; subjects are resolved in the effective structure at the boundary.
- *Effective structure* `Σ_n`: the fold of admitted structural changes (§6.1, §6.8 step 4). From it come the units, leaves, composites, `scope_id`, `subj`, kind/domain, coverage and tenure `τ(s)`.
- *Quarantine* `Q_n` and *affected subjects* `aff(Q_n)` (§6.1).
- *Revisions:* `rev(u, T)` and `cur(u) = rev(u, T_n)`, over effective scopes resolved in the observed bytes.
- *Relations and well-formedness:* authored and derived relations read from `T_n`; `well_formed(s)` (§6.2).
- *Record syntax:* record targets, and `superseded(x)` ⇔ some admitted record names `x` in its `supersedes` field (authorization was checked at admission).
- *Bearing:* `bears(a)` for a failing assessment, tested over its evidentiary premises against the observed tree and admitted equivalence judgments (Assessment disagreement, below).

Policy and structure follow one rule: **content proposes; admitted records enact.** The project policy unit is ordinary content, and an edit to it takes effect only through a human-gated adoption record that Admission validated under the previous ruleset. A structural declaration takes effect only through an admission that authored or adopted it. Derivation never reads a derived acceptance of policy or a derived validity of structure, so S0 depends on nothing above it.

**S1 — challenge tier.** Records of kinds CHALLENGE (with `blocking` flag; Serious Challenge is always blocking), ADJUDICATION (target a challenge; outcome `UPHELD` or `DISMISSED`), WITHDRAWAL (target the raiser's own challenge), RISK_OVERRIDE (target a challenge; declared continuation scope) and CONTINUITY_ATTESTATION (target a `LEDGER_LOSS`; human-gated; names the retained scope it holds unaffected, §15.4). A challenge may target a support-tier record, a subject revision `(s, scope_id, r)`, an adjudication, a risk override or a continuity attestation, never another challenge. Targets carry no tenure, so a challenge or revocation on a triple binds every tenure in which that triple recurs. A challenge raised against a part targets its subject's current revision and records the part as its locus. To contest a challenge, a qualified actor requests adjudication. Every target is strictly earlier in the ledger (Admission step 5).

**Polarity** is syntactic, decided by kind, outcome and target alone. A **restrictive** adjudication is an `UPHELD` adjudication of an ordinary challenge; its effect is a revocation. A challenge whose target is a restrictive adjudication is a **counter-challenge**: it contests a revocation, so its effect, if it succeeds, is permissive. **Relaxers** are the records whose only effect is to remove or soften a block, a revocation or a withholding: a withdrawal; a risk override; a continuity attestation; a `DISMISSED` adjudication of an ordinary challenge; and an `UPHELD` adjudication of a counter-challenge. A `DISMISSED` adjudication of a counter-challenge has no effect, because an open counter-challenge already has none. Every challenge that is not a counter-challenge, including one against a relaxer, is ordinary and restrictive.

```text
restrictive(a)   ⇔ a ∈ ADJUDICATION ∧ a.outcome = UPHELD ∧ ¬counter(a.target)
counter(c)       ⇔ c ∈ CHALLENGE ∧ restrictive(c.target)
relaxer(y)       ⇔ y ∈ WITHDRAWAL ∪ RISK_OVERRIDE ∪ CONTINUITY_ATTESTATION
                   ∨ (y ∈ ADJUDICATION ∧ y.outcome = DISMISSED ∧ ¬counter(y.target))
                   ∨ (y ∈ ADJUDICATION ∧ y.outcome = UPHELD ∧ counter(y.target))
                   -- each refers only to strictly earlier records: syntactic and well-founded

held(x, b)       ⇔ ∃ a ∈ CONTINUITY_ATTESTATION : a.target = b ∧ in_force(a) ∧ a holds x   (§15.4)
cont(x)          ⇔ ⋀ { held(x, b) : b a loss boundary with pos(x) < pos(b) }          -- T if there is none

gate(y)          = cont(y) if relaxer(y);  T otherwise
in_force(y), y ∈ ADJUDICATION ∪ WITHDRAWAL ∪ RISK_OVERRIDE ∪ CONTINUITY_ATTESTATION
                 ⇔ gate(y) ∧ ¬∃ c ∈ CHALLENGE : c.target = y
                                  ∧ (upheld(c) ∨ (c.blocking ∧ open(c) ∧ ¬counter(c)))
open(c)          ⇔ ¬∃ y ∈ ADJUDICATION ∪ WITHDRAWAL : y.target = c ∧ in_force(y)
upheld(c)        ⇔ ∃ a ∈ ADJUDICATION : a.target = c ∧ a.outcome = UPHELD ∧ in_force(a)
overridden(c)    ⇔ open(c) ∧ ∃ o ∈ RISK_OVERRIDE : o.target = c ∧ in_force(o)

unresolved blocking challenge on z  ⇔  ∃ c : c.target = z ∧ c.blocking ∧ open(c)

status1(z) = REVOKED      if ∃ c : c.target = z ∧ upheld(c)
             BLOCKED      else if ∃ unresolved blocking c on z with ¬overridden(c)
             PROVISIONAL  else if ∃ unresolved blocking c on z
             CLEAR        otherwise
```

*Uniqueness.* Polarity (`restrictive`, `counter`, `relaxer`) is computed first, by recursion on strictly *earlier* target records. It is purely syntactic and finite. The force and continuity predicates are then evaluated. In them, every right-hand side refers only to records whose position is strictly greater than the record on the left (a resolver is later than what it resolves; a challenge is later than its target; a loss boundary is later than every record it covers, and an attestation is later than its boundary). The definitions are therefore a recursion on a finite, strictly increasing chain of positions, evaluated once in decreasing ledger order. Each value is unique even though negation appears; no negative cycle can exist. Non-blocking challenges have no S1 effect while open; they create S3 obligations. Effects are conservative in both directions:

- An open blocking challenge against any relaxer (a dismissal, an override, an attestation, a successful counter-challenge's upholding) suspends it while open, and an upheld one removes its force permanently. An open blocking challenge against a dismissal therefore restores the original block.
- A counter-challenge has no effect while open, whatever its `blocking` flag. A revocation ends only when a counter-challenge is *upheld*, and that upholding is a relaxer: challengeable, suspended by an open blocking challenge, and withheld by a later loss boundary. Repair of a revoked triple therefore requires a successful challenge to the upholding, as the supersession paragraph below states, and never merely a filed one.

Revision 3's `in_force` omitted the `upheld(c)` term, so upholding a challenge against a dismissal closed that challenge and re-enabled the dismissal; revision 4 added it. Revisions 3-5 also let an open blocking challenge suspend an upholding, so filing a challenge un-revoked a triple whose revocation came from a non-blocking challenge, and a loss boundary could do the same by withholding a pre-loss dismissal of that challenge (`ffbad17` Blocker A). Revision 6 makes polarity syntactic and exempts counter-challenges from suspension.

*Loss boundary in S1.* `cont(x)` is false for a record admitted before a `LEDGER_LOSS` unless an in-force continuity attestation of that boundary holds it (§15.4). It gates exactly the permissive effects: a relaxer before the boundary loses force (`gate`), and a record before it cannot be current (S2 `base`). Ordinary challenges, counter-challenges, restrictive adjudications (so revocations), supersessions and every S0 fact are not gated; gating a restrictive adjudication would turn a revocation back into a block or, for a non-blocking challenge, into `CLEAR`. A successful counter-challenge's upholding is a relaxer, so a loss boundary withholds it and the revocation it lifted returns. Because no ungated record can relax a block or a revocation, withholding a relaxer at any depth of a challenge chain can only restore a block or a revocation, never lift one. Supersessions and upholdings can also dispose of an assessment disagreement, which is permissive for the claim. That effect is not an S1 effect: S2 reads it through `eff`, which includes `cont`, so a pre-boundary disposition is withheld and the disagreement returns (Assessment disagreement, below). With no `LEDGER_LOSS` in the ledger, `cont` is identically `T`.

**S2 — support tier.** Values in the three-point lattice `F < P < T` (non-current/invalid < provisional < current/valid), with `∧ = min`, `∨ = max`, empty `∨ = F`, empty `∧ = T`. S0 and S1 are constants here.

```text
base(z)  = F if superseded(z) or status1(z) ∈ {REVOKED, BLOCKED} or ¬cont(z);  P if status1(z) = PROVISIONAL;  else T
           (cont(z) = T for a subject-revision triple z)

current(x)  = base(x) ∧ ⋀_{e ∈ basis(x)} sat(e)                         -- x a support-tier record

sat(content (u, r, k))   = T                         if cur(u) = r, or k = PLAN_CONTROL and r ⊑ cur(u)
                                                     (rule-defined control tightening, an S0 fact, §7.9)
                         = ⋁_{paths r = r_0 -> ... -> r_m = cur(u)} ⋀_i current(q_i)
                                                     over EQUIVALENCE judgments q_i on u, class k
sat(validity (u, r, k))  = sat(content (u, r, k)) ∧ valid(subj(u))
sat(record x)            = current(x)
sat(identity z)          = T

ok(s)    = T if well_formed(s) and s ∉ aff(Q_n), else F                 -- S0 constant (§6.1, §6.2)

valid(s) = base((s, scope_id(s), cur(s))) ∧ ok(s)
           ∧ ⋁_{j ∈ ACC(s)} ( current(j)
                              ∧ ⋀_{required kind/actor q of ρ_n for s} ⋁_{j' passing, by q, on the same triple} current(j')
                              ∧ ⋀_{required human gate g} ⋁_{authenticated human judgment h for g} current(h)
                              ∧ ⋀_{required evidence obligation e} ev(s, e) )
  where ACC(s) = admitted passing acceptance judgments on exactly (s, scope_id(s), cur(s)),
                 admitted at or after τ(s), or prospective acceptances j with bind(j) = τ(s) under §6.9
                 (same enactment lineage and structural delta, basis holding, first enactment only),
                 by actors qualified for them (checked at admission)

valid(part u) is not a variable: every use routes to valid(subj(u))

ev(s, e)         = ( ⋁_{passing assessment a admissible for e} current(a) ) ∧ undisputed(s, e)
undisputed(s, e) = ⋀_{a- ∈ adverse(s, e)} ( P ∨ disp(a-) )     -- T when adverse(s, e) is empty
disp(a-)         = ⋁_{d disposing a-} eff(d)                    -- Assessment disagreement, below
```

**Assessment disagreement (`fb3e542` Blocker B; re-derived after `124b0b7` Blocker A, `97e753f` Blockers A-B and `4c35d92` Blocker A).** The 7.2.1 evidence owner requires that "an unresolved material disagreement keeps dependent present guidance/closure visibly qualified". It says "a valid failing observation is evidence", uses `review-required` when applicability is uncertain, forbids resolving the disagreement by vote, count or serialized record position, and forbids suppressing contradictory admissible observations to manufacture a pass. Revisions 10-12 each decided whether failing evidence still bears on the claim through a proxy: the failing assessment's currency, then a key, then satisfaction of its whole basis. Each proxy was permissive somewhere (`124b0b7` A, `97e753f` A, `4c35d92` A). Revision 13 uses no proxy. It takes the owner's own applicability dimensions — "evidence-spec revision, subject/candidate, governed-claim revision, input/validity regime, oracle semantics, environment/backend/precision/configuration, stochastic replicate identity and protocol obligation" — and gives each one fixed role. Whether a disposition currently stands is a separate question, answered in S2 with positive polarity only.

| Owner dimension | Role | Effect of a difference or move |
|---|---|---|
| protocol obligation | the evidence obligation `e` | assessments for different obligations never conflict |
| input/validity regime; any environment, backend, precision or configuration attribute the specification fixes | **admissibility** (§10), decided against the specification revision the assessment named, so an immutable fact | an assessment outside them is inadmissible for `e` and enters neither side |
| stochastic replicate identity; any execution attribute the specification leaves free | **execution variation** | admissible assessments that differ only here conflict |
| governed-claim revision (the realization's target); execution content the specification positively names (declared or derived `EXECUTION_DEPENDS_ON`, configuration held as content included) | **evidentiary premise** | a move ends bearing unless an admitted equivalence links the revisions: the observation is then about something else |
| evidence-specification revision; oracle and tolerance semantics | **interpretive premise** | none on adversity: the observation still stands and its meaning is uncertain, so it stays adverse (`review-required`) until its realization is reassessed or judged immaterial |
| subject/candidate | **frame** | bearing is evaluated in the evaluating frame, in the entries' roles (§6.9) |
| everything else in the assessment's basis: context and harness-observed reads, declared reliance, the widening closure and its completeness judgments, other record premises | **provenance** | ends the assessment's *currency*, and so raises a reassessment obligation, but never its adversity |

Admission computes the evidentiary premises mechanically from the realization record and the specification, as §6.9 computes entry roles; no agent labels them. The fallback of an incomplete execution closure (the governed tree, §6.5) is provenance, not an evidentiary premise, so missing dependency knowledge never removes adversity.

```text
bears(a-)     ⇔ every evidentiary premise (u, r, k) of real(a-) passes, in its role and frame:
                   r = cur(u), or r reaches cur(u) through admitted EQUIVALENCE judgments on u of class k
adverse(s, e) = { failing assessments a- admissible for e on s's claim unit : bears(a-) }
```

`bears` reads only the observed tree, the effective structure and record syntax, so it is S0. An equivalence judgment counts once admitted, whatever its later status, so challenging an equivalence never removes adverse evidence. `bears` ignores the failing assessment's own currency, supersession, challenges and `cont`. A failing assessment therefore stops counting only when an evidentiary premise moves without equivalence, or by disposition. The two predicates are deliberately asymmetric: currency over-approximates which moves remove *support*, and `bears` under-approximates which moves remove *adversity*.

- **Effective disposition** (S2). A record `d` *disposes of* a failing assessment `a-` when:
  - `d` supersedes `a-`, directly or through a chain of supersessions: an explicit reassessment of the realization by `a-`'s own assessor, or the owner's adjudication or discriminating new assessment;
  - `d` is an `UPHELD` adjudication of a challenge targeting `a-` or its realization `real(a-)`, the only premises whose revocation discredits the observation itself. An upheld challenge against any other premise, such as a completeness judgment or a context record, disposes of nothing;
  - `d` is an `IMMATERIALITY` judgment covering `a-`. This is also how the owner records that an interpretive change has made the observation irrelevant.

  ```text
  eff(d) = current(d)                                          d support-tier (a superseder, IMMATERIALITY)
         = T if in_force(d) ∧ cont(d) ∧ ¬contested(d), else F    d an UPHELD adjudication
  contested(d) ⇔ ∃ c ∈ CHALLENGE : c.target = d ∧ c.blocking ∧ open(c)    -- counter-challenge or not
  ```

  A disposition relaxes a qualification on the claim, so it counts only while it stands. A support-tier disposition stands at its own currency. Its basis must still hold in the evaluating frame, and an open blocking challenge, a supersession or a loss boundary removes it (a risk override caps it at `P`, which keeps the qualification). An upholding has no basis, so it stands while it is in force, held across any loss boundary, and uncontested. An open blocking challenge against it suspends its disposing effect even though, as a counter-challenge, it leaves the revocation in place. The two effects of one record keep their own polarities: a superseded record never becomes current again (below), and an upholding's revocation follows S1 alone. A disposition names the failing assessment in `identity` mode (§6.4), so a challenge against the failing assessment never changes the disposition's currency.
- **What does not end a disagreement.**
  - An open challenge against the failing assessment, overridden or not: only an *upheld* one disposes of it.
  - A loss boundary: the failing assessment still exists, and a disposition recorded before the boundary is withheld (`cont`), so the conflict returns until the owner disposes of it again.
  - A positive-only requalification, or a continuity attestation that holds only positive records.
  - A passing assessment on a new execution or claim revision while an equivalence keeps the failing one bearing.
  - A move of anything in the failing assessment's provenance, or of its specification, oracle or tolerance.
  - An upheld challenge against a premise other than the failing assessment or its realization.
  - A later passing assessment that is not authorized as a supersession.
  - A disposition whose basis has moved, or an upholding under an open blocking challenge.
  - Ledger order.
- **Re-disposal.** After a disposition stops standing, the owner disposes of the failing assessment again with existing records: a new `IMMATERIALITY` judgment, a further supersession of the failing assessment (a record may be named by more than one superseder), or a supersession of the stale superseder, which disposes of it through the chain.
- **Decision class and independence.** Every disposition, including the failing assessor's own reassessment, must be independent of the claim's author. A disposition admitted as non-independent (§6.8 step 3) has `eff = F`. `IMMATERIALITY` judgments, and supersessions or adjudications that dispose of another actor's failing assessment, are R2 (§7.5); for a claim unit that is D1 or D2 authority they are R3.
- **Where the effects go.** A live disagreement makes `undisputed(s, e) = P`, so `ev(s, e)`, validity and discharge are visibly provisional (§7.4), and briefs and gate views label the evidence `disputed` (§9.3). S3 derives an adjudication obligation for each adverse assessment with no standing disposition, routed to the qualified owner of the claim. Where the claim unit is D1 or D2 authority, a failing assessment that bore when it was admitted (an immutable fact), for an evidence obligation that also has an admitted passing assessment, is a floor item. Its human attention is keyed on the failing assessment's existence and closes only by an authenticated human judgment, which may record it moot (§7.9, A8).

**Uniqueness.** The right-hand sides are built from `min` and `max` over S2 variables and constants (`bears` and the S1 predicates inside `eff` are constants, and `current(d)` enters `undisputed` only positively, through `P ∨ ·` and `max`), so the system is monotone on a finite lattice and has exactly one **least fixed point**. That fixed point is the S2 state. Revision 10 had made S2 antitone in failing assessments' currency and rested uniqueness on acyclicity instead; revision 11 removed that non-monotonicity, together with the defect it caused, and revisions 12-13 keep it removed while letting dispositions' currency in positively. An ungrounded cycle evaluates to `F`: no acceptance can support itself. For the f9d9de8 review's counterexample (`current(j_a)` ← `valid(b)` ← `current(j_b)` ← `valid(a)` ← `current(j_a)`), the least fixed point is all-`F`, never all-`T`. The configuration is also inadmissible on two independent grounds. Mutual validity reliance between subjects is a support cycle (below). Mutual authored warrant between `a` and `b` is an illegal relation cycle (§6.2) whether or not `a` and `b` share a subject. The two checks are distinct because they guard different graphs: the support graph guards record currentness, and cycle legality guards declared semantic warrant (441cf5c Blocker A).

`ok(s)`, `τ(s)` and `cont` are how lower-stratum governance constrains S2 without reading S3. A subject touched by an unadmitted governance-affecting declaration, or carrying an illegal relation structure, cannot be valid. An acceptance from an earlier tenure cannot count. A record from before a loss boundary cannot count unless held. All three are functions of the ledger and the observed tree; `cont` adds no S2 variable, no support edge and no fixed-point interaction.

Admission maintains the stronger invariant that the **support dependency graph** is acyclic. Its nodes are `valid(s)` and `current(x)`. Its edges come from three sources: each basis entry; each subject to every acceptance, gate and assessment judgment naming it and to every record that disposes of a failing assessment for one of its evidence obligations (a static over-approximation that ignores applicability); and the static over-approximation of equivalence coverage, in which `x` depends on every equivalence judgment on `u` reachable from `r` for each `content` entry `(u, r)`. Edges change only when admitted records are added. Absorption adds none. A one-pass topological evaluation therefore computes the least fixed point. A cycle found at derivation can arise only from corrupted input; it still evaluates to `F` and raises an integrity obligation.

**S3 — consequence tier.** Non-monotone functions of S0-S2 that nothing below reads: open obligations (including intake of each quarantined delta, revalidation of each `OVERTAKEN` admission, and requalification of each record or relaxer withheld by a loss boundary that was in effect at the retained head), discharge (§7.4), readiness (§7.3), blockers, drift (`cur(s)` differs from `acc(s)`, the latest revision with a passing acceptance judgment, which is a display view only), impact sets for hypothetical changes, context answers, briefs, graph, diff and history views, and integrity findings. Provisional values and risk-override scopes are interpreted here. The requalification set is computed by comparing derivation at the retained head with derivation now; with no loss boundary it is empty. S3 explains and schedules quarantine and ill-formedness; it never enforces them, because S2 already did.

**Determinism claim.** For every authenticated `(L_n, content)`, S0 is a function, S1 is a well-founded recursion, S2 is the unique least fixed point, and S3 is a function. The same holds for each transformation frame `D_n[X]` (§6.9), which is the same derivation over a hypothetical tree and structure fixed by the transformation's identity `(B, C, A)`. `D_n` is therefore single-valued and independent of evaluation order, wall clock, live refs, witness reachability, operator state and search indexes (C2, C3, C8). Qualification is in §22.

**Supersession and risk override.** Supersession is purely syntactic (S0). A superseded record never becomes current again, even if its superseder later goes stale. Supersession withdraws a record; it does not reverse its admitted history. A risk override never resolves a challenge. It turns `BLOCKED` into `PROVISIONAL` for the challenged target; `P` then propagates by `min`, and S3 permits provisional discharge only inside the override's declared scope. An upheld challenge on a subject revision revokes that revision permanently. Repair requires a new revision and acceptance, or a successful challenge to the upholding adjudication.

**Analyzers** produce derived relations keyed by `(analyzer identity, version, configuration, input revisions)`. A deterministic analyzer's output is cache. A nondeterministic or expensive analyzer's output is recorded as an observation, so replay uses what was observed. **Caching** is memoization keyed by inputs. There is no dirty state, because nothing is cached without its content key. Incremental derivation must equal from-scratch derivation. **Integrity checks** run on every derivation: effective coverage partition, laminarity, single definer, relation cycle legality and vocabulary, support-graph acyclicity, the observed/effective structure comparison, the entry shape required by the integration observation (§15.3), and ledger authentication. Currentness qualification (§15.4) runs before any derivation is presented as current.

### 6.7 Early cutoff and equivalence

When upstream D2 subject `a` changes, the D3 subject `b` whose acceptance relied on `a` (validity mode) becomes invalid, and D4 judgments relying on `b` become non-current. If a re-review of `b` against the new `a` passes *without changing `b`*, `b` is valid again. Every D4 judgment whose basis named `b`'s unchanged revision, and did not itself see `a`'s text (§6.4), becomes current again with no further work. Staleness propagates exactly as far as meaning moved.

**Equivalence is semantic unless trivial.** Machinery decides equivalence only for byte identity and rule-defined conservative normalizations. The one rule-defined coverage relation that is not an equivalence is the `PLAN_CONTROL` tightening order on plan items (§7.9): it is an order, not a sameness claim, and it serves only plan-acceptance coverage. It may use derived interface fingerprints only for consumers of derived structure — never for behavioral conformance, evidence or semantic acceptance. Everything else is an `EQUIVALENCE` judgment by a qualified actor, scoped to consumption classes: "editorial only", "representation-preserving split", "does not affect this consumer". An equivalence judgment relates two revisions of one unit. Its `validity` entries must not depend back on a consumer of that unit; Admission's acyclicity check (§6.8 step 5) rejects any that would. It never creates acceptance of a different subject or scope. Where the rule requires independence, the author of a change cannot be the sole qualifier of an equivalence or completeness judgment about that change. A self-declared one is recorded as a proposal and backdates nothing.

This one mechanism replaces epoch binding, plan-revision binding, context staleness, stale-result detection, evidence staleness, dirty-graph tracking and the freeze frontier.

### 6.8 Admission requests and Admission

An **admission request** is the typed result of `submit`. It contains: a request identity (idempotency key); its **task binding**, the authenticated issued envelope of the task that produced it (§7.5), which fixes the bound obligation, role and contract revision; the obligations whose *discharge* it claims, possibly none; the base admitted position and base commit, candidate commit(s) on isolated refs (or none, for records-only requests such as a review, ratification or challenge of admitted content), any quarantined structural deltas it adopts, and the records it submits. The admission record that accepts or rejects it carries the request identity, the decision, reason codes, the admitted records and the resulting admitted commit. This is the complete identity and audit trail a change needs, so no separate change primitive exists. A repeated request identity returns the recorded decision.

Admission is the **sole writer** of the ledger. Other actors can still move the integration ref: humans pushing to legacy scopes, an external merge button, a force-push, a restore from backup. Such movement carries no admitted status. Admission observes it before its next append and absorbs it as a foreign change (§11, §15.3). An absorption record sets the expected head `E` to the observed head, and so the observed tree `T_n`, and changes nothing else. Every touched unit whose content now differs from its accepted revision shows drift. Every structural declaration that differs from effective structure is quarantined. Production is never blocked by this; governance validity is.

Admission validates against the admitted head it holds, after reconciling the integration head (step 9, §15.3), in order, and either appends or rejects with recorded reasons:

1. **schema** — records well-formed under the closed schema; bounded secret/sensitive-value checks (§15.5); unknown required semantics fail closed (C5);
2. **reference** — every identity, revision, task, obligation and target exists and matches;
3. **authorization** — actor class qualified for each judgment kind; acceptance judgments only on subjects effective in the record's frame: in their current tenure (after the request's own structural changes), or, for a frame-`X` acceptance, in the prospective tenure of `Σ_n ⊕ Δ_Σ(X)` (§6.9); never on parts, never on a `REVOKED` triple and never on an ill-formed revision; the task binding verifies against a Dispatcher issue key in force (§15.6), names an obligation that exists at the request's base, and was issued for the role `role(kind(o))` under `ρ_n`; independence requirements for equivalence/completeness about the request's own change, and for every review, acceptance and plan-acceptance judgment and every disposition of a failing assessment (§6.6): such a judgment satisfies an independence requirement only when its lineage class is `ATTESTED_FRESH` or `HUMAN_ATTESTED_FRESH` and its lineage is disjoint from the author's, and is otherwise admitted as a non-independent judgment that cannot satisfy one (fail closed, C5; A9, §9.6); the bound role permits each record kind and outcome (§7.5); the request's write set lies within the bound contract's write scope, and plan units, contracts and verification rules lie outside every role's scope except as §7.5 assigns them (§7.6); protected surfaces untouched without their own authority (§15.7);
4. **structure** — on the merged tree `M`, in three parts:
   - *(a) effective-structure delta.* For every declaration key `k`:
     - if `k ∉ Q_n`, then `Σ_{n+1}[k] := decl(M)[k]`: an authored change, or no change;
     - if `k ∈ Q_n` and `decl(M)[k] = Σ_n[k]`, the request *realigns* the repository with governance and `Σ` is unchanged;
     - if `k ∈ Q_n` and the request carries an intake disposition adopting `k`, then `Σ_{n+1}[k] := decl(M)[k]`, validated exactly as if authored;
     - if `k ∈ Q_n` and `decl(M)[k] = decl(T_n)[k]`, the quarantine is carried unchanged;
     - any other value routes the request to revalidation.

     Authored and adopted changes are validated together: leaf coverage partition, laminar composites, scope conservation for refinement, no membership change that mixes governance modes without the mode-transition record (§12.1), SDG members never separated, and no change of a unit's kind or owning domain without a judgment by an actor qualified for its *current* domain (a unit never leaves its owner's authority by redeclaration). These are the **well-formedness** checks. An admission that integrates a transformation must also meet the **enactment condition**: every promotion or restoration carries a prospective acceptance that counts for the tenure it starts (§6.9, §12.2). A frame for inspection needs well-formedness only, so a promotion can be reviewed before it is accepted, but it can never be enacted unaccepted. Admission never creates new quarantine, and repository presence never enters `Σ` except through an adopting disposition.
   - *(b) challenge freeze.* No change to the signature, scope, regions or membership of any subject is admitted, whether that subject would lose or gain units, while its current revision carries an unresolved blocking challenge (overridden or not) or is `REVOKED`. A challenge therefore cannot be escaped by re-scoping unchanged content at the source subject or at the destination subject.
   - *(c) semantic structure.* Known relation types of `ρ_n`, relation direction and layer order, cycle legality and the SDG rules (§6.2), and single definer;
5. **dependency well-formedness** — challenge-tier targets strictly earlier and of permitted kinds; no `validity` entry naming the record's own subject or a part of it (prerequisites inside it are `content`-mode, §6.4); after the request's edges are added — basis entries, equivalence coverage, and the edges of existing records whose `validity` endpoints the request's structural changes re-route through `subj` — the support dependency graph remains acyclic (§6.6);
6. **currency** — every basis entry of every submitted support-tier record other than a report is satisfied, in its role, in that record's frame at the current admitted ledger head. That is the admitted state for a record about admitted content, or the transformation frame `D_n[X]` for a record about a transformation `X`, with before-image, output and context roles (§6.9). A request that itself carries content or structural changes (an integration, a principal's plan-unit change) is evaluated as a frame record of its own transformation, so revision 4's merged-tree exception is now the same rule. (Optimistic concurrency: Admission holds that head by compare-and-swap, and it is admitted because at most one provisional entry exists, §15.3.) Otherwise the record is classified stale and routed to revalidation rather than admitted. **Reports and challenges are exempt** (`f3608f5` Blocker A), and so are failing assessments (`4c35d92` Blocker A): a failing assessment's adversity is decided by `bears` over its evidentiary premises (§6.6), never by its context's currency, so one whose context moved during its task is admitted rather than lost, and S2 decides its currency. Their basis records what the raiser saw, as provenance; it is never checked for currency and never consumed by any rule, since resolving records reference reports by identity (§7.9). A report raised after its context moved is therefore still admitted and routed. When a request is routed to revalidation, the admission record that rejects it still admits the report and challenge records it carries, bound to the same task, so nothing reported is lost with the rejected work;
7. **legality** — the bound obligation exists at the current head. A task result or discharge claim bound to an obligation already discharged, or to a contract revision that is no longer current, is recorded with that classification and routed to revalidation; it is not admitted as current work. Reports and challenges are admitted whatever the state of their task, so nothing reported is lost. A human decision on a fenced admission is admissible only once that admission is settled: a later `obs` shows the ref away from its base (§15.3). Each obligation whose *discharge* the request claims is undischarged at the current head (a duplicate discharge is rejected and recorded), and its discharge predicate (§7.4) holds after the request's own records, including affected evidence rerun on the merged tree. Requests that claim no discharge (a task result, a mid-task report) are subject only to the binding checks. For a claimed task obligation carrying a work contract, the derived conformance of the exact candidate commit has no `VIOLATION`, `INCOMPLETE` or `DISCREPANCY` (§7.7), and an integrating request claims it only together with its current review judgments (§7.8);
8. **no collateral regression** — every obligation discharged at the current head and affected by the merged tree stays discharged, with affected evidence rerun. The only legal way to reopen others' closures is an accepted change to a prerequisite authority, whose derived impact obligations are the intended consequence. A D4 change that breaks another closure is a regression and is not admitted. This step concerns the request's content and structural changes: an admitted assessment, report or challenge that qualifies another closure (for example a competent failing assessment that makes it provisional, §6.6) is evidence, never collateral regression, and is not rejected here;
9. **commit and admit** — Admission reads the live integration head `obs`. The request is appended only if `obs` is the head entry's expected head `E` (or an equivalent publication of it, §15.3); otherwise Admission first appends an absorption of `obs` and revalidates the request at the new head. One ledger entry carrying `obs` and all records is appended by single-ref compare-and-swap (§15.3); it also reconciles the publication of the previous admission if that was pending. The appended entry is *provisional*. It is *admitted* when a witness quorum holds its exact checkpoint (§15.4), and that is the commit point for every external effect. Only then is the request reported admitted, the integration ref published as an effect, work dispatched from the new state, and the next entry appended; the next entry records this publication's outcome.

**Absorption** of a foreign change already on the integration ref records what happened, so it cannot be stale or illegal. It skips the validation steps and is itself appended and admitted like any entry. It is a pure integration observation: its only content is `obs` and, for a fencing absorption, the fence effect `obs -> F` (§15.3), and an entry whose `obs` differs from the expected head must be an absorption carrying no submitted records (Admission rejects any other shape; derivation treats a violating entry as an integrity defect). It sets the observed tree and changes nothing else: effective structure, ruleset and acceptance stay as admitted. When the previous admission's publication is pending, the absorption is also its reconciliation (§15.3). Three things follow:

- foreign structural declarations become quarantined deltas (§6.1);
- foreign semantic content changes revisions, so acceptances and content reliance on it stop being current;
- foreign relation violations make the involved subjects ill-formed (§6.2).

All three take effect in S0 and S2. The S3 obligations that follow — intake, drift, broken closures, integrity findings — only schedule and explain the disposition work (§11).

**Self-reference.** Records reference the candidate commit; they are never stored inside it. Task and result envelopes on run branches are transport, ingested into the ledger, never merged (G2, G3).

**Agent PASS is a proposal.** An admitted PASS judgment is a recorded fact about what the actor concluded; closure is a derived discharge (§7.4).

### 6.9 Transformation frames: judging a proposed transformation

Work is judged before it is integrated. A record about unintegrated work therefore needs a defined currency, both before and after integration. The frame was re-derived twice, and the reasons explain its shape:

- **Revision 7** substituted the candidate's tree and evaluated every basis entry against it. That conflated three different reliances, so an implementer's own read of the content it edited made its result stale (`ac71fa9` Blocker A).
- **Revision 8** separated those reliances. But it named the frame by candidate commit alone, although the proposed structure also depends on which quarantined deltas the request adopts (`730490d` Blocker B). It also made the frame's existence require the promotion acceptance that only a reviewer inside the frame can supply (`730490d` Blocker A).

Revision 9 keeps one idea: **a transformation is a proposed change, identified completely, and a record about it relies on what was transformed, what it became, and everything else.** Inspecting a proposal and enacting it are different steps with different preconditions. Nothing here adds state, a store or a primitive.

- **Transformation.** A transformation is `X = (B, C, A)`:
  - `B` is the recorded base, an admitted integration commit;
  - `C` is an immutable candidate commit on an isolated ref;
  - `A` is the exact set of quarantined structural deltas its producing request adopts by `ABSORB` dispositions (§11.2), possibly empty.

  Its **identity** `id(X)` is a content hash of `(B, C, A)`, so the same commit offered with two adoption sets gives two transformations. `id(X)` is fixed by the task result that first submits the candidate; a later request cannot change what that result's transformation adopts. The **content delta** `Δ(X)` is the set of effective units whose revision in `tree(C)` differs from `B`. The **structural delta** `Δ_Σ(X)` is the set of structural-declaration changes `C` authors relative to `B`, together with `A`.
- **Frame state.** At admitted head `n`, the frame `D_n[X]` is `derive` (§6.6) over the same ledger prefix `L_n` with two hypothetical inputs:
  - the observed tree `T_n` is replaced by `M_n(X)`, the deterministic three-way merge of `C`'s content changes since `B` onto `T_n`, with an algorithm fixed by the system version;
  - the effective structure `Σ_n` is replaced by `Σ_n ⊕ Δ_Σ(X)`.
- **Frame existence: inspection, not enactment.** The frame exists when the merge is clean and the structural delta is **well-formed**. Well-formed means every step-4 check except the enactment condition:
  - leaf coverage, laminarity and scope conservation;
  - governance-mode consistency;
  - source and destination challenge freezes;
  - simultaneous-definition-group integrity;
  - release by the old domain owner for a domain change;
  - relation and cycle legality.

  The **enactment condition** is that every promotion or restoration carries a current prospective acceptance. It is checked only when an admission integrates `X` (§6.8 step 4). In the frame, a subject that `Δ_Σ(X)` creates or restores exists in a **prospective tenure** and is simply not yet valid, because nothing has accepted it. That is the state a reviewer must be able to inspect. Without a clean merge or well-formedness there is no frame, no record in it can be current, and §7.8 routes a new iteration: machinery never resolves a conflict (K3). `D_n[X]` is single-valued for the same reasons `D_n` is. It is never presented as current state, and nothing in `D_n` reads it. In the frame, the declarations in `Δ_Σ(X)` are not quarantined, because they are the proposal under judgment; every other quarantined delta stays quarantined.
- **Basis-entry roles.** Every `content` entry `(u, r)` of a frame-`X` record has exactly one role, computed mechanically from `B`, `C` and the entry. No agent labels it.

  | Role | When | Satisfied before integration (in `D_n[X]`) | After the integrating admission `k` |
  |---|---|---|---|
  | **before-image** | `u ∈ Δ(X)` and `r = rev(u, B)` | while the live head still has it: `rev(u, T_n) = r`. Otherwise the transformed content has moved underneath the work; rebase or re-review | a fixed fact about what admission `k` transformed: satisfied, like an `identity` entry |
  | **output** | `u ∈ Δ(X)` and `r = rev(u, C)` | `rev(u, M_n(X)) = r` (a unit both sides changed is judged at its merged revision) | ordinary currency in the admitted state: a later edit of `u` makes it stale |
  | **context** | `u ∉ Δ(X)` | ordinary currency in `D_n[X]`: a moved prerequisite makes it stale | ordinary currency in the admitted state |
  | — | `u ∈ Δ(X)` and `r` is neither | never; the record relied on a revision that is neither the base nor the result | — |

  `validity`, `record`, challenge-tier and loss-boundary facts are evaluated in `D_n[X]` before integration and in the admitted state after. A `record` entry on another frame-`X` record is evaluated in the same frame. A `record` entry on a record of a different transformation is satisfied only if that record's basis holds in this frame; no frame designation transfers currency.
- **Declared frame.** A task result, a check execution, and a review, conformance, assessment or **acceptance** judgment about a transformation declare frame `id(X)`. Every other record declares the admitted frame. An acceptance in frame `X` must name a subject that is effective in `Σ_n ⊕ Δ_Σ(X)`, at its frame `scope_id` and revision (§6.8 step 3). It is a **prospective acceptance**: it counts only for a prospective tenure, under the rule in *Integration* below.
- **What frames decide.** These are all evaluated in `D_n[X]`:
  - the conformance of `C` (§7.7);
  - the readiness and discharge of review and acceptance obligations on `X`;
  - Admission step 6 for frame-`X` records.

  Nothing evaluated in a frame changes the admitted state. In `D_n`, a review or prospective acceptance of `X` is admitted but not current, and a proposed promotion is still a quarantined proposal.
- **Integration enacts the frame.** The integrating admission `k` of transformation `X` admits exactly `M_n(X)` as the observed tree and `Σ_n ⊕ Δ_Σ(X)` as the effective structure, in one entry. It checks the full step-4 validation including the enactment condition, so a promotion without a current prospective acceptance is rejected (§6.8 step 4, §12.2). Its discharge predicate (step 7) is evaluated in the post-admission state. There, before-image entries are fixed facts, and output and context entries hold exactly as they held in the frame.
  - **Prospective-acceptance rule (`fb3e542` Blocker A).** A prospective acceptance `j` made in the frame of `X0` counts for the tenure that admission `k` starts exactly when all four conditions hold:
    1. **Same enactment lineage.** `k` integrates a transformation `X` produced for the same bound obligation as `X0`, as recorded in the signed task envelopes of their results (§7.5). That is `X0` itself or a later iteration or rebase of the same work. A restoration after a demotion is new work under a new obligation, so it is never the same lineage.
    2. **Same structure.** `Δ_Σ(X) = Δ_Σ(X0)`.
    3. **Basis holds.** `j`'s basis holds, in its roles, in `D_n[X]` at `k`.
    4. **First enactment.** `j` has not counted for any earlier tenure. `bind(j)`, the first admission at which conditions 1-3 held and that started a tenure, is a function of the ledger.

    `j` therefore counts for at most one tenure, the one starting at `bind(j)`. When that tenure ends, `j` leaves `ACC` permanently, as §12.2 states for every acceptance, and no later restoration can reuse it. Equal structure plus a holding basis is necessary for reuse across a rebase, but never sufficient for lifecycle continuity.
  - Promotion and acceptance therefore take effect together in `k`, although the acceptance was recorded earlier by an independent reviewer. The integration request carries no new judgment.
- **Rebase.** A rebase produces a new transformation `X' = (B', C', A')` for the same bound obligation. A frame-`X` record counts for `X'` only if every one of its entries holds, in its role, in `D_n[X']`. A record that concerns structure, such as a prospective acceptance or a structural review, counts for `X'` only if, in addition, `Δ_Σ(X') = Δ_Σ(X)`. Records never move between frames by assertion.

## 7. Work: obligations, change plans, roles and verification

### 7.1 Two sources of work

The befe678 WorkGraph conflated two different things.

- **Derived obligations** follow from rules and state: a subject without a valid acceptance; a judgment no longer current; an evidence specification without a current admissible realization for its claim; an open challenge awaiting adjudication; a pending human gate; a foreign change awaiting intake, including each quarantined structural delta; a scope deviation awaiting disposition; an admitted change overtaken before publication (§15.3); a record or relaxer withheld by a loss boundary and awaiting requalification (§15.4); an integrity finding. They are never authored; they appear and disappear as derivation changes (S3). Their deterministic identities are derived from `(rule, subject)`.
- **Authored intents** carry creative direction: implement this, investigate that, migrate this region. They live in **change plans**: plan units (documents) whose sections are **items**. Each item has an objective, governing units, acceptance criteria, intended affected units, required gates and dependencies on other items or units. Before it can be issued, the item also carries a **work contract** (§7.6) that types these fields and adds boundaries, verifiers, expectations and a budget.

### 7.2 Plan acceptance and local amendment

A `PLAN_ACCEPTANCE` judgment (independent where policy requires) names in its basis the plan's objective section and the item revisions it accepts. An item is issuable only while some current plan-acceptance judgment covers its current revision. Item-level revisions give locality:

- an amendment is an ordinary change to the plan unit; tasks whose basis names a changed item become non-current; tasks on unchanged items continue;
- the plan's principal (§7.5) is the only agent role whose write scope includes the plan's units; a human may also edit a plan, as ordinary content that enacts nothing until accepted;
- whole-plan invariants are rechecked mechanically on every amendment: referenced units exist, dependencies are acyclic and respect authority order, gates required by policy are present, acceptance criteria name resolvable evidence, and every changed contract passes lint (§7.6);
- an amendment's acceptance class is decided mechanically from the plan diff: a control-tightening change keeps the existing plan acceptance current through the rule-defined `PLAN_CONTROL` coverage order; every other amendment, including any added or removed obligation, needs independent plan acceptance (§7.9). Splitting an item's execution is a task partition, not an amendment (§7.9);
- the plan's policy states whether an amendment may be accepted by a scoped review of the changed items plus their derived impact set, or needs whole-plan review. Changes to the plan objective, acceptance criteria, topology or gates always need whole-plan review. A scoped reviewer always receives the whole-plan objective and may escalate;
- running tasks remain bound to their basis; no revision pretends an old task saw new requirements.

No global planning/working phase and no global stop exist; an unaccepted amendment only makes its own items non-issuable. Plan lifecycle fields in documents are non-authoritative or generated (§12.6).

### 7.3 Readiness, iteration and attempts

An obligation is **ready** when every prerequisite it names is valid (or provisional, where policy permits provisional continuation; the result is then provisional) and its plan item (if any) is accepted. Readiness is derived from the ledger and content alone (S3). This is the whole "freeze frontier": readiness through the authority DAG, not a waterfall, with no extra state. Whether a ready obligation is *dispatched now* is the Dispatcher's operational decision: resources, routes, serialization surfaces already held (§8.3). That decision never feeds back into derived state.

An **iteration** is the sequence of judgments recorded against one obligation; a NO-PASS leaves the obligation undischarged and the next task is a new iteration. An **attempt** is one execution of one task, owned by the Dispatcher; a failed attempt is recorded in the operator journal and does not touch derived workflow state.

### 7.4 Discharge (canonical closure)

Discharge is an S3 classification with three values: `DISCHARGED`, `DISCHARGED_PROVISIONAL`, `OPEN`.

```text
discharged(o) <=> exists current judgment j of kind(o) on subject(o)
                   by an actor qualified for kind(o), with outcome in passing(o)
              AND status1 of subject(o)'s current revision is not BLOCKED or REVOKED
              AND ev(subject(o), e) for every evidence obligation e of o: a current passing
                  assessment admissible for e, capped at P by any bearing failing assessment
                  with no standing disposition (§6.6; the same term that validity reads)
              AND every human gate of o is discharged by a current authenticated human judgment
result is DISCHARGED_PROVISIONAL when any input above is P; that value is permitted only
  inside the declared scope of an in-force risk override or where policy permits provisional
  continuation; otherwise the obligation stays OPEN
```

The impact a change triggers on *other* subjects is not a discharge condition: those are separate obligations on the dependents, and Admission step 8 forbids collateral regression. A missing required check is an undischarged obligation; no rule can turn it into PASS.

### 7.5 Workflow roles and decision classes

A **workflow role** is an authority envelope: what an execution may write, which record kinds and outcomes it may submit, and which decisions it may make. It is distinct from SSDP's D1-D4 domain roles (scientific formulation, numerical algorithm design, software design, software implementation), which are *content*: the epistemic procedure a brief carries for its subject's domain (§9.2, §12.6). A brief composes the two. The principal *role* is not a principal in the authentication sense of §15.6: like every agent role, its records are proposals attributed to an execution identity.

Role templates are fixed by the SSDS system version and parameterized by project policy, like judgment kinds (§6.6): obligation kinds held, operations, record kinds and outcomes, write-scope rule, decision class, brief template and context policy, separation constraints. The obligation kind determines the role.

**Authenticated task binding.** The Dispatcher issues every task as an **envelope**: task identity, bound obligation, role, contract revision (the task's basis), route, and the launch's lineage class. The envelope is signed with a Dispatcher **issue key** that genesis registers as a trust root and that changes only by a human-gated lifecycle record (§15.6). Every request carries the envelope of the task it was produced for. Admission verifies the signature and checks role, write scope and record kinds against the envelope (§6.8 step 3), and the admitted records carry it, so derivation and replay read the binding from the ledger without any host's private state. Binding and discharge are separate: a request is always *bound* to one task, and only some requests *claim discharge* of an obligation (§6.8 step 7, §7.8).

**Lineage classes.** On a route where the Dispatcher's harness adapter launches the execution, it starts a new harness session for the task. It hands that session alone a per-task submission credential, and it signs a launch attestation naming the session identity and the sessions of the task's inputs: the authoring task of a candidate under review, the author of a contract under plan acceptance. Requests authenticated by that credential carry the lineage class `ATTESTED_FRESH`. On manual and Git-envelope routes, the Dispatcher cannot observe the session. A judgment from such a route is `UNKNOWN` unless an authenticated human attests that it ran in a fresh context that did not receive the author's conclusions (`HUMAN_ATTESTED_FRESH`, an R3 judgment). Anyone holding an envelope can submit within its role and contract, because authority lives in the role, not in the session. Independence, however, is credited only to positively attested lineage. An `UNKNOWN` judgment is recorded but satisfies no independence requirement (A9).

| Role | Holds | May | May not |
|---|---|---|---|
| **Principal** | coordination obligations of one change plan (`COORDINATE`, below) | author and amend the plan's items and contracts (its plan units are its only write scope); decide reports routed to it, within the outcomes their kind allows (§7.9); partition an item's execution into tasks (§7.9); frame human questions; annotate, merge and upgrade escalations; downgrade non-floor materiality by recorded judgment | write product, authority or evidence units; submit review, conformance, acceptance or plan-acceptance judgments; submit any judgment that keeps its own amendment covered; discharge human attention; change verification rules |
| **Implementer** | realization obligations of one item (implement, repair, migrate) | write within its contract's write scope; submit a task result with typed slots (§7.8); report (§7.9); run advisory verification (`ask(verify)`, §7.7) | edit plan units, contracts, evidence specifications its contract does not name, verification rules or protected surfaces; submit any judgment about its own work |
| **Reviewer** | review, conformance and acceptance-recommendation obligations; plan-acceptance reviews of contracts | records only: judgments on the exact target, findings, challenges | write content; judge work or a contract its own execution authored; receive the author's narrative or conclusions (A9, §9.6) |
| **Investigator** | investigation obligations: diagnosis, reconstruction proposals, intake classification, exploratory analysis | write only to scratch workspaces and to the native finding or evidence homes its contract designates; submit findings, proposals and reports | write product or authority units; submit acceptance |
| **Human** | gates and every decision R3 owns, including human attention (§7.9) | `decide` (§9.4, §9.8); edit any content, plans included, as ordinary change that enacts nothing until admitted or accepted | — |

Project policy may add roles and narrow any role. It may not widen a role beyond its system template, combine principal and reviewer in one execution, or give an agent role an R3 decision. Every execution the Dispatcher launches runs in a fresh context for one task, and the separation constraints are enforced from the authenticated binding and lineage class above (A9, §6.8 step 3).

**Decision classes.** The class of every decision is a function of its kind, its target's domain and policy. No agent selects it. An agent may move a decision up by escalating; it can never move one down.

| Class | Decided by | Decisions | Recorded as |
|---|---|---|---|
| **R0** | machinery | readiness; dispatch, suspension and resumption; staleness; evidence and check executions; iteration retry within budget (§7.10); report routing (§7.9); integration requests (§7.8); recurrence detection | derived state or operator journal; never a judgment |
| **R1** | principal | task partitions and ordering within the plan; responses to findings inside an item's scope; local resolutions inside delegated space; control-tightening amendments; merging, upgrading, framing; downgrading non-floor materiality | coordination decision or plan-unit change; challengeable; never acceptance |
| **R2** | an independent agent or human reviewer (A9) | plan acceptance of new contracts and of every amendment that is not control tightening; review, conformance and acceptance judgments; adjudications that policy assigns to agents; dispositions of an assessment disagreement (§6.6) | support- or challenge-tier judgment |
| **R3** | authenticated human | gates; D1/D2 acceptance where policy requires it; Serious Challenge adjudication; risk overrides; product-scope acceptance (S12); continuity attestations; human attention; dispositions of a disagreement on a D1/D2 claim (§6.6) | authenticated human judgment |

**The principal is an obligation holder, not a daemon.** `COORDINATE(plan)` obligations are derived (S3) whenever a decision is owed on a plan: a report routed to it (§7.9); an exhausted budget, an out-of-scope NO-PASS finding or detected recurrence (§7.10); an item awaiting a contract; an `OVERTAKEN` admission or a stale result that needs re-planning. Each coordination task is a fresh execution whose decision brief (§9.7) is rendered from derived state. Nothing a principal execution remembers is canonical, so any execution can replace it at any decision point, and context compaction cannot lose workflow state. Each change plan is a serialization surface for coordination (§8.3): at most one coordination task per plan runs at a time, so two principal executions never amend one plan from different bases; the Dispatcher batches the plan's pending decisions into it. Obligations that belong to no plan (intake, integrity, requalification) are held by the roles their kinds name; a decision owed on them goes to the principal of the plan that policy designates as standing, or to the human where policy names none.

### 7.6 Work contracts

A **work contract** is the typed, machine-readable section of a plan item. It is plan content: authored by the plan's principal, revisioned with the item, accepted by the item's `PLAN_ACCEPTANCE` judgment, and bound into every task's basis through the item revision. It adds no primitive, store or record category. Obligations that belong to no item (review, rerun, intake, requalification) receive the system contract of their obligation kind, so every task has exactly one contract.

```text
contract(item @ revision)
  objective, governing      the item's fields (prose objective for judgment; governing units at revisions)
  scientific                Protocol 7 obligation predicate: APPLIES | NOT_APPLIES, judged at plan acceptance
  boundaries
    write_scope             units or path patterns resolved in Σ       -- authorization (§6.8 step 3)
    frozen                  interfaces and symbols that must not change (by language analyzer)
    dependencies            permitted additions to declared dependency manifests
    evidence_specs          evidence-specification units the item may change (default: none)
  obligations               id, statement, verifier
    verifier                CHECK(template, parameters) | EVIDENCE(specification, runner class) | REVIEW
  expectations              required artifacts; required evidence; required result slots (§7.8)
  escalation                triggers that route a report to the principal or the human (§7.9)
  budget                    iterations before mechanical retry yields to the principal (§7.10)
```

1. **Total verifier assignment.** Every obligation names exactly one primary verifier. `REVIEW` is a legitimate and explicit choice. An obligation without a verifier fails lint, so what the machine checks is decided where the work is defined and is visible to the reviewer of the contract.
2. **Lint is mechanical and runs at every contract admission,** with the plan invariants of §7.2:
   - fields typed under the schema; units and patterns resolve in `Σ_n`;
   - the write scope lies within the item's intended affected units and contains no protected surface, no plan unit and no evidence-specification unit outside `evidence_specs`;
   - every `CHECK` names a `HARD` template of `ρ_n` with valid parameters (a `HEURISTIC` template cannot be a primary verifier, §7.7); every `EVIDENCE` names an existing specification and a designated runner class;
   - the required slots include every slot the obligation kind, the subject domain and the `scientific` flag trigger (§9.2);
   - policy-declared minimum verifier coverage holds (for example, an item that changes D4 code carries at least one `EVIDENCE` obligation);
   - a budget is present.
3. **Adequacy is judged.** Lint establishes form only. Whether the contract captures the item — the right obligations, a sufficient verifier for each, a boundary neither too narrow nor too loose, the right `scientific` flag — is part of `PLAN_ACCEPTANCE`, an R2 judgment by an execution other than the contract's author. A strong verifier over a weak contract proves only what the contract asked.
4. **Frozen at issue.** A task's basis names its item revision, so the contract it executes is fixed. An amendment makes running tasks on that item non-current (§7.2); it never changes what a running task was asked.
5. **Write scope is authorization; footprint is prediction.** The write scope is enforced at Admission (§6.8 step 3) and in conformance (§7.7). The Dispatcher's footprint prediction (§8.1) may be computed from the same field but stays advisory. K4 holds unchanged: correctness rests on enforced authorization and admission-time proof, never on a prediction being complete. Work that needs more scope requests an amendment (§7.9) instead of taking it.
6. **No implementer grades its own exam.** Evidence-specification units not named in `evidence_specs` are outside the write scope, so acceptance tests cannot be edited by the work they judge. Tests an implementer writes to meet an obligation are authored artifacts like any other: their adequacy is reviewed and their strength measured (§7.7). A change to a named evidence specification raises its owner's specification-review obligation (§10).

### 7.7 Conformance verification

**Conformance** of a task result is an S3 classification, evaluated in the candidate's frame (§6.9): a pure function of the contract at the task's basis, the base and candidate trees, the result record, and the observations recorded for that exact candidate. It is not stored; like every derived view it is recomputed, and it is shown as the result's **conformance view**. Expensive or nondeterministic checks (test execution, mutation testing, static analyzers with recorded versions) are executed by a designated runner on the exact candidate and recorded as observations (§6.3, §10). Deterministic checks are memoized like analyzers (§6.6). No component is added: Derivation evaluates, the Dispatcher executes, Admission enforces (§6.8 steps 3 and 7).

**Check templates** are fixed, versioned functions of the ruleset `ρ_n`. A contract only parameterizes them and can never carry executable check code, just as project policy carries no rule language (§6.6). A project-specific template enters only by human-gated ruleset adoption after the qualification of §22. Each template declares one **force**, fixed by the template and never by a contract:

- `HARD` templates may yield `VIOLATION`, `INCOMPLETE` or `DISCREPANCY`. A template is adopted as `HARD` only with qualified detection and false-positive rates on real trajectories (§22).
- `HEURISTIC` templates yield `SIGNAL` only. Every check that reads prose is `HEURISTIC` by system rule, so no control decision depends on parsing prose (A7).

| Family | Checks | Force |
|---|---|---|
| Boundary | candidate diff mapped to units, against the write scope; protected surfaces; frozen interfaces by language analyzer (public symbols and signatures); dependency-manifest additions against the allowance; hand edits to generated units; credential-like values in content | `HARD` |
| Test integrity | tests deleted, skipped or marked expected-to-fail; evidence specifications changed outside `evidence_specs` | `HARD` |
| | fewer assertions; widened tolerances or loosened comparisons in tests | `HEURISTIC` |
| Obligation | required artifact present and linked to its target by a derived test-to-code relation; required evidence realized by the designated runner on the exact candidate with a passing outcome; evidence basis fields (regime, precision, backend, seed, replicate) matching the specification (§10); required slots filled, or empty with a typed reason; new stub markers (placeholder bodies, `NotImplementedError`) in written units; test strength by seeded mutation testing over changed lines at the contract's threshold | `HARD` |
| Faithfulness | outcome classification consistent with the derived facts (a `COMPLETE` outcome with an unmet obligation); declared deviations equal to detected boundary breaches; every cited record exists and supports the slot citing it (a failing realization cited as passing); cited governing units at their basis revisions | `HARD` |
| | numbers or factual phrasing in prose that disagree with records; certainty vocabulary ("verified", "proven", "equivalent") without a cited record | `HEURISTIC` |
| Domain | dimensional consistency of quantities that carry machine-readable units; declared tolerance and precision present for numerical claims in annotated units; declared references respecting layer direction | `HARD` |
| | unit or tolerance inference for unannotated quantities | `HEURISTIC` (separate templates; each template has one force) |

| Class | Meaning | Routing (R0) |
|---|---|---|
| `VIOLATION` | a `HARD` boundary or test-integrity check failed | the candidate can never be integrated (§6.8 steps 3 and 7); a breach the result disclosed becomes an amendment request (§7.9); an undisclosed breach is also an integrity finding to the principal, shown to the reviewer of any later attempt |
| `INCOMPLETE` | a `HARD` obligation check failed, or a required execution is missing | a new implementer iteration within the budget; beyond it, the principal (§7.10) |
| `DISCREPANCY` | a `HARD` faithfulness check failed: the result says something the records contradict | integrity finding to the principal and the reviewer; repetition by one route or model is recurrence (§7.10) and appears in the digest (§9.8) |
| `SIGNAL` | a `HEURISTIC` hit | attached to the review brief as a pointer; changes no disposition |
| `CLEAN` | none of the first three (signals may be present) | the review obligation on that candidate becomes ready (§7.8) |

**Compound outcomes.** Conformance is a set of classes, not one class. Every failed `HARD` template contributes its class with its own finding, and every routing of every contributed class applies; no class takes precedence over another. An undisclosed breach, for example, is both `VIOLATION` and `DISCREPANCY`, and both its rejection and its integrity finding follow (`f3608f5` N2).

**A clean conformance view discharges nothing.** Obligations whose verifier is `REVIEW` stay open until a current review judgment, and every task obligation still requires the review its kind requires (A7, §7.4). Removing every `HEURISTIC` template from the ruleset must leave every admission decision and every discharge unchanged; §22 qualifies that property.

**Disclosed and undisclosed breaches.** The result's deviation slot is compared with the detected breaches. A disclosed breach is a legitimate request for more scope, decided by the principal. An undisclosed one is a faithfulness failure. Neither is integrated; only the second is a finding against the route that produced it.

**Advisory pre-flight.** `ask(verify)` runs the pure templates, and any executions the workspace itself can perform, inside the implementer's workspace before submission. The answer is labeled advisory. It never stands in for the designated runner, and an agent's report of it is a finding, never evidence (§10).

**Doctrine-realization levels.** Every duty SSDP 7.2.1 places on an agent is realized at one level, assigned in the Manual's realization map (§21 item 27):

| Level | Realization | Examples |
|---|---|---|
| **E0** | enforced mechanically; no agent action | write scope and protected surfaces; version binding and the self-adoption guard (S7, §19.2); agent PASS never canonical; stale evidence never confirms; facts produced by machinery (A6) |
| **E1** | detected mechanically, routed to judgment | drift; quarantine; recurrence; test-weakening signals; discrepancies; analyzer conflicts |
| **E2** | a required typed slot whose presence is checked and whose content is judged | owed delegate returns (material findings, variant-search disclosure, null envelope); the tension-search envelope; consequential-choice provenance; claims with their record references |
| **E3** | judgment only, covered by review and challenge | adequacy; equivalence; scientific interpretation; whether a finding is material; detection itself |

The realization map is a design artifact of the Manual, not a runtime registry mirroring doctrine (§20). An E2 slot makes an answer's presence nearly certain, not its quality. The 7.x evidence that inline structured checklists raised uptake from 28% to 92% is why typed slots are the default form for owed questions; the reviewer still judges what they say.

### 7.8 Results, review and integration

Implementation work enters canonical state through two ordinary admissions. No new path exists.

1. **Result.** `submit` by an implementer or investigator produces a records-only request, bound to its task and claiming no discharge: a task result record (an outcome from the task's allowed set, typed slots, claim references, reports) naming the candidate commit on its isolated ref and the contract revision in its basis. The result fixes the transformation `X = (B, C, A)` and its identity, including the exact set `A` of quarantined deltas the request adopts (§6.9). Machinery, not the agent, attaches the factual part: the diff mapped to units, touched relations, reads (A6). The request is admitted as records; the candidate is not merged. The Dispatcher then runs the contract's required executions on the exact candidate through a designated runner and submits them as observations. Conformance is derived (§7.7).
2. **Review.** Once conformance is `CLEAN`, the review obligation on that exact candidate becomes ready (R0). Result, executions, review and conformance judgments all declare the candidate frame, so their currency is defined before integration (§6.9). A reviewer task (§9.6) submits its review and conformance judgments as a records-only request bound to the review task, claiming discharge of the review obligation only. When the candidate promotes, restores or adopts a subject, a qualified reviewer also records the prospective acceptance in the candidate's frame (§6.9, §12.2).
3. **Integration.** Once the claimed obligation's discharge predicate would hold on the candidate — clean conformance, current review judgments, required gates — the Dispatcher submits an **integration request**: the candidate commit plus references to those admitted records, bound to the task that produced the candidate (through its result record) and claiming that task's obligation. It carries no new judgment. Admission validates it through steps 1-9 like any request. If the head has moved, the candidate is rebased. A rebase that does not apply cleanly is never resolved by machinery (K3): it routes to a new implementer iteration. A clean rebase has its conformance re-derived on the rebased candidate, and review is re-requested only where the review's basis no longer holds (§8.2, §6.7).

Every other request follows the same split. A mid-task report is bound to its task and claims nothing; a blocking report suspends that task (§7.9). A coordination task's request is bound to its `COORDINATE` obligation and claims discharge of the decision obligations for the reports it resolves; its plan-unit changes follow §7.9.

A rejected candidate stays recorded with its conformance view and its reports, so nothing an agent reported is lost because its work was rejected. Records-only work (reviews, investigations whose output is findings) has no integration step.

### 7.9 Reports, amendment requests and escalation

Every communication from an agent that can change what happens next is a typed **report** record, not a message. Narrative stays in its canonical home: the project evidence record or native issue for a finding or tension (S13), the result envelope for a task report (§9.5). The record carries the report kind, its subject (target units or records), raiser and role, declared materiality, a blocking flag, inquiry status for a challenge (§10), and a content-identity reference to the home.

- **Kinds.** Challenge tier (§6.6 S1): `CHALLENGE` and `SERIOUS_CHALLENGE`, which can block and, if upheld, revoke their target. Support tier (§6.3): `FINDING`, which records what was found and never blocks or revokes (a tension, an anomaly, an opportunity, a defect not yet raised as a challenge); `AMENDMENT_REQUEST`, with reason `SCOPE_DEVIATION`, `MISSING_PREREQUISITE`, `INFEASIBLE_CRITERION`, `CONTRACT_DEFECT` or `AUTHORITY_DEFECT`; `BLOCKER`; `HUMAN_QUESTION`. Each kind has exactly one tier.
- **Materiality:** `ROUTINE`, `MATERIAL` or `CRITICAL`, declared by the raiser and raised, never lowered, by the floors below.

**Persistence.** Every obligation derived from a report or challenge — human attention, coordination, adjudication — is keyed on that record's existence and identity. It opens when the record is admitted and closes only when a **resolving record** targets the report by `identity` and stays in force: not superseded, not `REVOKED` or `BLOCKED` (S1), and not withheld by a later loss boundary (`cont`). The report's own currency never closes it. When the report's target or basis moves (for example, the principal amends the item a question was about), the obligation stays open and its entry is annotated "target changed since raised", so the decider can answer "moot" explicitly. Only the raiser may supersede or withdraw its own report. Withdrawal or supersession of a floor item does not close human attention: the entry shows "withdrawn by raiser" and still needs a human acknowledgment. For a non-floor item, it moves the entry to the digest. A loss boundary changes nothing about a report that survives it (§15.4); a resolving record from before the boundary is withheld, so the obligation reopens. Reports inside an abandoned interval are lost with it, and the `LEDGER_LOSS` gate brief states that open human-attention items there cannot be enumerated.

**Routing (R0).** A routing table of the ruleset maps `(kind, reason, materiality, target domain)` to derived S3 obligations:

| Report | Derived obligation | Holder |
|---|---|---|
| amendment request, blocker (including a disclosed breach, §7.7) | `COORDINATE` decision | the plan's principal |
| any blocking report | the raising task is also suspended, its workspace and basis preserved; it resumes as a new attempt after the decision | Dispatcher |
| challenge | adjudication under S1 | the qualified actor policy names |
| Serious Challenge | adjudication and human attention | human |
| human question | human attention | human |
| `MATERIAL` or `CRITICAL` report | human attention, plus a `COORDINATE` decision if it bears on the plan | human; principal |
| `ROUTINE` finding | recorded; a `COORDINATE` decision only if it names a unit of an open item | principal |

**Escalation floors.** System semantics fix the floors; policy may raise them, never lower them.

- `CRITICAL`, always creating human attention: a Serious Challenge; a tension or challenge against accepted D1 or D2 authority; a human question; an amendment that changes a plan's objective or changes or removes an existing acceptance criterion (computed from the plan diff); an authority-defect request targeting D1 or D2; an admission fenced after an ambiguous publication, raised when the fence is admitted and decidable once it settles, and every `LATE_PUBLICATION` (§15.3); any decision R3 owns.
- *Domain floor:* every report whose target includes a D1 or D2 unit is at least `MATERIAL`, whatever the raiser declared. The floor is computed from the target's effective kind and domain (§6.1), so under-declaring materiality cannot keep a report from the human.
- *Disagreement floor:* where a claim unit is D1 or D2 authority, a failing assessment that bore when admitted, for an evidence obligation that also has an admitted passing assessment creates human attention, keyed on the failing assessment's existence and identity like a report's (§6.6).
- *Delegate floor:* when a task's contract has `scientific = APPLIES`, every material finding in its E2 slots creates human attention. The 7.2.1 duty that material delegated findings survive to the human is thereby realized mechanically rather than by each intermediate agent's compliance.

**Principal decisions.** A coordination task decides each routed report with a coordination-decision record. The outcomes allowed are a function of the report's kind, reason and target domain, never the principal's choice:

| Outcome | Meaning | Allowed for |
|---|---|---|
| `RESOLVE_LOCAL` | decided inside the item's delegated space; the raising task resumes | blockers, scope questions, routine findings; never an authority-defect or contract-defect request |
| `AMEND` | a plan-unit change follows (below) | amendment requests; blockers; contract defects |
| `CHALLENGE` | a challenge-tier record against the earliest affected owner | any; the required route for an authority-defect request targeting D3 or D4 |
| `ESCALATE` | human attention | any |
| `DECLINE` | no action, with a reason code; the raising task resumes or ends | non-floor reports only; a report that already created human attention keeps it |

**Amendment classes.** An `AMEND` decision is followed by an ordinary plan-unit change authored by the principal. The coordination request carries both the decision records and the plan-unit candidate. It is bound to the `COORDINATE` obligation and claims discharge of the decision obligations it resolves. Admission checks the binding and role (the principal's write scope is its plan units), runs lint (§7.6) with the plan invariants (§7.2), and integrates the plan-unit change, which enacts nothing by itself. Whether each changed item stays issuable is then derived from its plan acceptance. The class is computed by lint from the diff between the accepted item revision and the current one; the principal cannot assert it.

- **Control tightening (R1).** Every field of the item and its contract is either unchanged or moved only in its tightening direction:

  | Field | Tightening direction |
  |---|---|
  | `write_scope`, `dependencies` allowance, `evidence_specs` | subset |
  | `frozen` | superset |
  | each obligation | id, statement and primary verifier unchanged; it may gain secondary `HARD` checks |
  | required result slots; `escalation` triggers | superset |
  | `budget` | not greater |
  | `scientific` | `NOT_APPLIES` to `APPLIES` only |

  Objective, governing units, acceptance criteria, the obligation set, required evidence and artifacts, gates and item dependencies are unchanged.
- **Every other change is R2**: independent plan acceptance, scoped or whole-plan as §7.2 requires. That includes adding or removing an obligation; changing any statement or primary verifier; any move of a field against its direction (widening a scope, unfreezing an interface, removing an escalation trigger, `APPLIES` to `NOT_APPLIES`); and any field the whitelist does not name, including fields that later schema versions add (closed, C5).

A control-tightening change keeps the existing plan acceptance current by a rule-defined coverage order, not by an equivalence judgment and not by any judgment of the principal. The plan-acceptance kind's basis entry on an item uses the consumption class `PLAN_CONTROL`, which is satisfied when the current item revision is reached from the accepted one by the tightening order above (§6.4). The order is mechanical, reflexive and transitive, and it is always checked against the accepted revision, so tightening and then loosening is caught. It claims only that the acceptance's conclusion about *what is asked* still applies under tighter controls. It does not claim the work is still feasible: a scope narrowed too far surfaces as an `INFEASIBLE_CRITERION` or `SCOPE_DEVIATION` request. Adding an obligation narrows what is admissible and is therefore a semantic change (§7.2), so it always goes to R2.

**Task partition (decomposition without amendment).** The principal splits the *execution* of an item, never the item. A `PARTITION` coordination decision names tasks over one item revision:

- Their obligation sets partition the item's obligations exactly.
- Their write scopes are pairwise disjoint subsets of the item's write scope.
- Their order is acyclic.

Lint checks all three. Each task's contract is the item contract restricted mechanically to its share. The item, its plan acceptance and its scope are unchanged, and no acceptance moves to a new unit (§6.7, §12.2). Each part's obligations are derived per part and discharged as §7.8 describes. The item is discharged when every part is, and when an item-level review of the integrated result has passed, because parts reviewed separately can still violate a joint property (§8.4). Policy may waive the item-level review only for named item kinds. A later partition supersedes an earlier one only for obligations not yet discharged.

**Annotate, merge, upgrade, downgrade.** The principal may annotate any human-attention obligation; its framing is Channel A interpretation, rendered apart from the evidence core (§9.8). It may merge duplicates, and the merged item lists every member. It may upgrade materiality. It may reclassify a non-floor `MATERIAL` report to `ROUTINE`. The reclassification is a support-tier judgment that counts only while in force (Persistence, above). It moves the item from the inspector's open list to the digest (§9.8). It is challengeable: an upheld challenge, or a later loss boundary, returns the item to the open list. It is not a discharge: no human judgment is simulated, and the item stays visible. Floor items cannot be reclassified. Human attention on an item is discharged only by an authenticated human judgment (A8).

### 7.10 Iterations, budgets and recurrence

- Each contract carries an iteration budget. Within it, an `INCOMPLETE` result, or a NO-PASS whose findings all lie within the item's write scope and obligations, starts the next implementer iteration mechanically (R0). The new brief carries the conformance view and the review findings as data, not the previous attempt's narrative.
- Budget exhaustion, a NO-PASS finding outside the item, and every `DISCREPANCY` create a `COORDINATE` decision.
- **Recurrence** is detected mechanically: the same `HARD` template failing on the same obligation across iterations; the same finding family (template, target unit or relation family) across items; repeated discrepancies by one route. Detection creates a `COORDINATE` decision whose brief carries the convergence-and-cycle-economy duty to consider the shared owner and simplification before another local repair, and to route a Challenge where the contract or its governing authority may be at fault. Detection is mechanical; the response is judgment.
- An attempt that fails operationally (crash, timeout, lost harness) is a Dispatcher retry (§7.3) and spends no iteration.

## 8. Concurrency

### 8.1 What is decided where

| When | What can be established | Mechanism |
|---|---|---|
| Before issue (prediction) | probable footprint: intended affected units, derived impact closure, serialization surfaces | Dispatcher avoids issuing overlapping work; advisory only (K4) |
| Before issue (authorization) | the write scope of the task's work contract, which is not a prediction | enforced in conformance and at Admission (§7.6-§7.7, §6.8 step 3); more scope only by amendment |
| At admission (proof) | everything the change relied on is current; actual write set; structural validity of the merged tree; dependency well-formedness | basis currency (§6.6), diff mapped to units, structural checks |
| After merge (evidence) | behavior of the combined tree | evidence currency recomputed on the merged tree; affected realizations rerun |
| Never mechanically | joint validity of independently valid changes where no relation, invariant or evidence covers the interaction | judgment: declared joint-invariant units, review of integrated results, residual risk stated |

### 8.2 Optimistic admission (serializable by validation)

Concurrent tasks work from recorded bases in isolated workspaces. Admission applies requests one at a time to the admitted head, as a merge queue. Speculative batching is delegated to D4 and must preserve this serial order. A request whose basis was overtaken is revalidated — rebased, re-derived, affected judgments re-requested. It is not rejected outright and never silently admitted. Two requests conflict when one modifies a unit or record in the other's basis. This catches write-skew among recorded reliances, including across disjoint files. A losing compare-and-swap between two Admission hosts is the same case. So is a race between hosts reconciling one pending publication: only the entry's publisher ever performs the publication compare-and-swap, and the ledger compare-and-swap admits exactly one reconciling successor (§15.3).

A very late result whose basis is still current is admissible regardless of age; a fresh result with a stale basis is not. Lease expiry affects scheduling, never correctness.

### 8.3 Serialization policy

Some surfaces make speculative concurrency wasteful or unsafe to merge mechanically: shared schemas and public contracts, build configuration, D1-D3 subjects in one dependency neighborhood, and generated outputs. A unit may carry a policy-declared serialization attribute; the Dispatcher then issues at most one mutating task on it at a time. Every change plan is such a surface for coordination: at most one coordination task per plan runs at a time (§7.5). Generated units are never hand-merged: they declare `GENERATED_FROM` their generator and inputs and are reproduced by regeneration, with conflicts resolved by regenerating.

### 8.4 Residual risk

Semantic dependencies an agent uses without the machinery observing them cannot be captured. Mitigation is layered. The mechanical minimum basis already includes the governing closure. Integration reruns affected evidence. Units may declare cross-cutting **joint invariants**: any change touching their scope re-derives their conformance obligation. Reviews of integrated results are triggered where policy marks a surface high-consequence. The remaining risk is stated in briefs and Review records rather than hidden.

## 9. Agent and human interface

### 9.1 Logical operations

The interface is defined independently of transport.

| Operation | Purpose |
|---|---|
| `open(task)` | returns the task brief (§9.2) and workspace locator |
| `ask(query)` | typed questions: what governs X; what X depends on / what depends on X (per relation class); explain a unit, record or obligation; evidence for a claim; why is this blocked or stale; impact of this workspace diff or proposed edit; advisory verification of the workspace against the task's contract (`ask(verify)`, §7.7); text/semantic search; history of X (PEM-gated) |
| `read(ref)` | content by unit identity or path; recorded into the basis |
| `report(item)` | a typed report (§7.9): finding, challenge, Serious Challenge, amendment request (scope deviation, missing prerequisite, infeasible criterion, contract defect, authority defect), blocker, question for a human; or a proposed relation |
| `submit(result)` | outcome classification from the task's allowed set, the typed result slots its contract requires, plus the workspace. Machinery builds the typed admission request (§6.8) and supplies the facts: diff, touched units, changed authored relations, reads, basis and derived consequences (A6). For a candidate this admits the result records, not the candidate (§7.8); the response then reports conformance as it is derived. The response is `ADMITTED` only after the entry is admitted (§15.3); before that it is `PROVISIONAL`, and a provisional entry lost before admission is resubmitted by request identity (§15.4) |
| `decide(gate)` | human only: a gate brief (§9.4) and an authenticated decision |

Within a task, `ask` and `read` answer at the task's basis (snapshot isolation), so an agent never sees a mixture of states. `ask("what changed since my basis")` reports admitted changes that intersect the task, letting the agent stop early instead of discovering staleness at submission.

The agent never declares write claims, revisions, edges (other than by writing authored relations as part of semantic content), subject roles, epochs, plan patches, lifecycle states, reconciliation steps, its own conformance or the decision class of anything. A principal changes a plan by editing its plan unit as ordinary content, which takes effect only when accepted (§7.2, §7.9); a reviewer and a principal submit their judgments and decisions through `submit`.

### 9.2 Task brief

A task brief contains, in this order:

1. objective, obligation kind and workflow role;
2. allowed outcomes;
3. **governing content inline**: the exact text of governing units at the basis revisions;
4. the work contract's boundaries (write scope, frozen interfaces, dependency allowance), constraints, non-goals and delegated space;
5. obligations with their verifier class, acceptance criteria, required evidence and the required result slots;
6. open challenges, findings and provisional states touching the subject; for a later iteration, the previous conformance view and review findings, as data (§7.10);
7. **incompleteness notices**: where the basis was widened or `UNBOUNDED`, where analyzers are incomplete, where relations are only proposed, where a relied-on unit is a part whose validity comes from a coarser subject, where the repository declares structure that governance has not admitted (quarantine), where relied-on records are withheld by a loss boundary pending requalification, whether the head admission's publication outcome is not yet recorded, and the qualified ledger head the brief was derived at;
8. escalation triggers, budget, workspace and submission instructions.

It is rendered deterministically from derived state by version-bound templates; no model is needed to translate machine state. The duties a brief carries are compiled, never selected by wording (A4): workflow role template × obligation kind × subject domain (the core of the matching SSDP D1-D4 role entrypoint) × contract flags (`scientific`, triggered slots). A duty that is not triggered is not carried. Reviewer and principal briefs follow §9.6 and §9.7.

### 9.3 Epistemic status of context

Every context item is labeled:

| Class | Meaning |
|---|---|
| `GOVERNING` | authority the task's subject concretizes or is constrained by; mandatory |
| `IMPLIED` | reached by accepted authored relations inside a judged-complete scope |
| `ADJACENT` | reached by derived structural relations; completeness per analyzer declaration |
| `EVIDENTIAL` | evidence for the subject's claims, with current/stale/unavailable status |
| `HISTORICAL` | PEM entries and Git history; offered only when the PEM predicate fires or on explicit request |
| `CANDIDATE` | search or embedding hits and unaccepted proposals; never authority, never closure support |

Each item also carries its acceptance status (valid, provisional, disputed, challenged, stale, drift, quarantined, ill-formed, loss-withheld, unclassified) and its inclusion path. Every answer names the qualified ledger head it was derived at (§15.4); with no qualified head, answers are labeled historical (`UNQUALIFIED`) and claim no currentness. Answers are deterministic for identical basis, query and policy version. Search indexes record their versions, and nondeterministic search contributes only `CANDIDATE` items outside the determinism guarantee. A search hit can lead to a proposed relation, but never by itself to an accepted one.

### 9.4 Human gates

A gate brief presents the non-narrative evidence core first: identities, coverage, key data and trajectories, findings as data. Agent interpretation, alternatives, anomalies, uncertainty, variant-search disclosure and unresolved findings follow separately. A gate accepting a D1/D2 revision also receives that revision's tension applicability assessments, including any marked inapplicable, with their asserters, and a gate cannot close unqualified while missing realized records could plausibly change its judgment (7.2.1 Channel C). Gate-evidence adequacy is a semantic judgment, not a presence predicate: the human's decision records whether the evidence was adequate, and that record can itself be challenged. Agents and machinery may request a gate; they cannot synthesize a human judgment. Every gate is an entry of the inspector view (§9.8). A risk override is a distinct judgment kind that authorizes bounded continuation and leaves dependents provisional (S2, §6.6).

### 9.5 Transports and harnesses

Transports expose the same logical operations. There are three: an MCP server; a CLI; and a Git-envelope transport for zero-context web agents (an immutable task envelope on an isolated run branch, a result envelope plus candidate commits written back, and polling-first fetch of the specific run branch). Harness adapters (Claude Code, Codex, OMP, Pi or others) only map these operations and launch/observe executions. The bootstrap is `Execute SSDS task <id>` plus the minimum locator the environment does not already bind (repository, run ref, envelope path, protocol/profile source). It fails truthfully when protocol material cannot be resolved. Transport and process success never imply evidence admissibility or task success.

### 9.6 Review briefs and constructed independence

A review brief is rendered for independence (A9). It **contains**:

- the governing content inline;
- the contract;
- the candidate diff and the machine-produced facts;
- the conformance view, with every `SIGNAL` as a labeled pointer;
- the evidence with its status;
- the result's disclosure slots (deviations, unverified assumptions, variant-search disclosure, tensions found), labeled as the author's claims to be tested;
- for a scientific subject (`scientific = APPLIES`), the 7.2.1 bidirectional Review question as a required review slot: does realized behavior reveal evidence that should challenge, qualify or motivate investigation of the governing authority or its framing? An explicit "no reverse-direction finding survives" is a valid answer; an empty slot is `INCOMPLETE` (E2).

It **excludes**:

- the author's outcome classification, rationale and narrative report;
- commit messages and transcripts;
- the principal's annotations and expectations;
- any earlier conclusion by the author.

In a re-review of a later iteration, policy may supply the previous review's findings, labeled, because they are another reviewer's findings, not the author's.

The Dispatcher launches every review in a fresh context distinct from the authoring task's context and from the contract author's, and records the lineage class, model family, route and toolchain in the execution provenance. Independence fails closed: a review or plan-acceptance judgment satisfies an independence requirement only with an `ATTESTED_FRESH` or `HUMAN_ATTESTED_FRESH` lineage disjoint from the author's (§7.5, §6.8 step 3). Pasting a review bootstrap into the authoring session therefore yields an `UNKNOWN`, non-independent judgment, never an independent one. Where a claim relies on independence, the review judgment records material common-mode dependencies (shared model family, source corpus, toolchain or oracle), as the workflow owner requires; policy may require a different model family or a distinct evidence route for high-consequence surfaces.

*Residual:* the artifact under review can itself carry its author's framing in code comments and docstrings. That is content to be reviewed, and it cannot be stripped.

### 9.7 Decision briefs

A coordination task (§7.5) receives a **decision brief** rendered at the qualified head. It contains:

- the plan objective, and each item with its state (awaiting contract, ready, running, suspended, under review, discharged, open);
- the decision obligations owed, each led by the report's record core, the target's identities and revisions, and the relevant conformance and review outcomes, followed by the outcomes allowed for that report (§7.9);
- budgets, recurrence detections and discrepancies;
- the plan's open human-attention items and their state;
- what changed since the previous coordination.

Narrative reports and transcripts are reached only by reference.

The decision brief *is* the plan's working state. It is derived, version-bound and reproducible, so the principal keeps no memory between invocations, and a context limit, crash or change of model loses nothing that governs the workflow (A2).

### 9.8 The inspector view

The human interface for everything R3 owns is the **inspector view**, an S3 view rendered deterministically.

- **Ordering.** Open human-attention obligations are ranked by derived impact: how many obligations' readiness or discharge waits on each (§7.3), and by consequence class; age breaks ties. The human sees first the decisions that unblock the most work.
- **Each entry, in order:**
  1. the evidence core: the report record, target identities and revisions, conformance and review outcomes, cited evidence with its status;
  2. the principal's framing, labeled as interpretation (Channel A);
  3. the allowed outcomes.

  Merged entries list their members, and one human judgment may answer a merged entry as a whole. Gate briefs (§9.4) are entries of this view.
- **Answering.** `decide` records an authenticated judgment: acknowledge, answer, accept, reject, redirect, or override where policy allows. The judgment propagates mechanically: suspended tasks resume, amendments follow, obligations discharge or reopen.
- **Digest.** Below the open entries is a cold digest of what agents settled since the human's last acknowledgment: R1 decisions, materiality downgrades, declined reports, discrepancies and recurrences. Every digest item is challengeable. Reading the digest is never required for work to proceed; an upheld challenge restores whatever it covers.

The view is an inspection surface and a trust boundary (§15.7): where content is confidential it gives the strongest safe aggregate and states the limitation. Human unavailability leaves human-attention obligations open. Dependent work stays not ready, and independent work proceeds (truthful non-closure, §24).

## 10. Evidence

| SSDP evidence concept | SSDS 8 representation |
|---|---|
| specification | evidence unit with `EVIDENCES` -> claim unit and declared or derived `EXECUTION_DEPENDS_ON` |
| realization | observation record whose basis has two parts: **target** (claim unit revision) and **execution** (code units, data identity, environment, backend, precision, configuration, parameter instance, regime, seed and replicate identity) |
| observation | the realization record's outcome plus references to native artifacts (logs, data) by content identity where possible |
| assessment | judgment record. A reassessment replaces an earlier one only by explicit, authorized supersession, never by being later; a bearing failing assessment and a passing assessment for the same evidence obligation are a disagreement, which counts until a standing disposition: a supersession, an upheld challenge or an `IMMATERIALITY` judgment (§6.6) |

A realization supports a claim at revision `c` only while its execution basis is current and its target is `c`, or an equivalence judgment covers the change. An execution-dependency change triggers a rerun obligation; a target change triggers an assessment-review obligation. Stale passing evidence never discharges. Failing evidence whose evidentiary premises (the claim revision and the execution content the specification names) moved without an admitted equivalence never qualifies the current claim; any other failing evidence does, until it is disposed of (§6.6). Unavailable artifacts degrade binding health through availability observations: the historical record survives, and present use becomes `UNAVAILABLE`. Process exit or harness success is never evidence admissibility. A realization with incomplete or malformed evidence is recorded as such and cannot enter a PASS/FAIL assessment. Raw data stays in native stores; the ledger stores identities and bounded classifications. A realized-record item is an observation only when an evidence realization produced it; retaining it neither assesses nor re-identifies it. A challenge record carries the finding's inquiry status (exploratory or confirmatory) as its own attribute, separate from evidence strength, applicability and disposition (7.2.1 evidence owner). Findings and tensions keep their one canonical home in project evidence records or native issues; the ledger references that home by identity and never becomes it (S13, §15.5).

**Who may realize evidence.** A realization can discharge an evidence obligation only in two cases: a runner that project trust policy designates for that specification executed it (normally Dispatcher-controlled execution on the exact candidate or merged tree), or a designated runner reproduced it. Results an agent reports from its own workspace are findings: useful for direction, never admissible for discharge. Policy may let expensive scientific realizations (long simulations, HPC campaigns) run under recorded custody outside the Dispatcher; the realization record then names the custody evidence. Conformance check executions (§7.7) follow the same custody: only a designated runner's execution on the exact candidate counts, and a check execution is evidence for a scientific claim only where an evidence specification names it.

## 11. Intake: one route for every change of unknown provenance

### 11.1 Detection and entry

Intake is not a separate engine. It is a set of derivation rules plus judgment kinds that treat any content not produced by an admitted request as a change with an **unknown basis**.

Recorded observations detect it:

- the live integration ref has moved away from the expected head (direct push, external merge, force-push, restore from backup, manual conflict resolution, or overtaking an unpublished admission). Admission observes this before every append (§15.3); a Dispatcher census that notices it requests an absorption;
- a submitted workspace contains changes outside its reported result;
- an external branch is offered for import;
- content differs from accepted revisions (drift);
- the observed structural declarations differ from effective structure (quarantine);
- a scheduled census finds untracked or unexpected material.

Two entry paths share one rule set. Content **already on the live integration ref** is absorbed mechanically (§6.8): the observed tree advances, nothing governing changes, and its consequences become obligations. Content **offered as a candidate** is a change whose basis is computed conservatively from its merge base: mechanical minimum plus widening. That covers an external or foreign-agent branch and agent work outside its reported result. It reaches the integration ref only through ordinary Admission, after its intake obligations are discharged.

### 11.2 Processing and dispositions

```text
preserve exact identity (commit/ref/tree; nothing executed)
 -> diff against the last admitted observed tree; map changed paths to effective leaves
 -> structural declarations: compare decl(T_n) with Σ_n; each differing key is a quarantined
    delta, classified governance-affecting or governance-neutral (§6.1)
 -> uncovered paths: proposed new units, statically classified
    (path, type, Git history, known producers, build manifests, parsers, provenance)
 -> mechanical consequences (S0/S2): changed revisions make dependent records non-current;
    aff(Q) and ill-formed subjects are invalid
 -> obligations (S3): classification and disposition judgments; equivalence/materiality
    judgments; conformance or acceptance reviews for touched authority; adoption or
    realignment of each quarantined delta; quarantine for untrusted or opaque active content
```

**Dispositions** are judgment outcomes:

| Disposition | Meaning |
|---|---|
| `ABSORB` | accept the content as it stands; for a quarantined structural delta, **adopt** it (below) |
| `RECONCILE` | needs rework |
| `SPLIT` | divide into separately classified parts |
| `ARCHIVE` | keep as historical material |
| `RETAIN_AS_EVIDENCE` | keep as evidence, not authority |
| `MARK_GENERATED` | regenerate rather than edit |
| `QUARANTINE` | isolate untrusted or opaque content |
| `REJECT` | revert by an ordinary change; for a structural delta, a change that **realigns** the declaration with effective structure |
| `DISPOSABLE` | classification only; deletion is a separate authorized change |

**Structural intake.** A quarantined delta becomes effective in exactly one way: an admission request carries an `ABSORB` disposition adopting it, which makes the delta part of its transformation's identity (§6.9), and Admission validates the adopted change exactly as if the requester had authored it now (§6.8 step 4). This includes the challenge freeze at source and destination, an acceptance bound to the same admission for any promotion (§6.9), mode consistency and SDG integrity. Adoption is therefore re-authoring under current rules and authority, never ratification of presence. It is validated under the ruleset in force when it is admitted, not the one in force when the foreign change appeared. A ruleset adoption never changes `Σ` or `Q`, and the governance-affecting/neutral classification is fixed by system semantics, not by policy. A governance-neutral delta (re-partition of leaves inside one subject) cannot change any subject or acceptance, so where policy permits, Admission may adopt it by a mechanical intake request; it still passes step 4.

### 11.3 Effect on governance

Foreign content affects governance only through lower-stratum facts, never through S3:

1. **Changed bytes or semantic declarations** change revisions, so acceptances and content reliance on them stop being current (S2).
2. **Changed structural declarations** are quarantined. They do not enter `Σ`, and every subject in `aff(Q)` has `ok = F`. Until the delta is adopted or realigned, such a subject cannot serve as validity prerequisite, governing context or acceptance basis. Routing (`subj`, scope, tenure) continues to follow admitted structure.
3. **Uncovered content** is `UNCLASSIFIED` and excluded from governing use.
4. **Illegal relation structure** makes its subjects ill-formed (`ok = F`).

The S3 intake obligations only schedule and explain disposition work. Unqualified authority therefore cannot arise from repository presence, because no S0 input that S2 consumes is changed by presence alone.

**Inspectable and recoverable while non-authoritative.** Foreign content is never hidden or discarded. The observed tree *is* the product: foreign commits remain in Git and can be built and released. The absorption record and the ledger keep the observed tree reachable. Views show each quarantined delta beside its effective value, with the absorption entry that introduced it and its provenance. Every disposition is an ordinary admitted change that a later admitted change can reverse. Production is not blocked; what remains open is governance closure. Agent overstep, manual edits, collaborator branches, foreign-agent work, repository restores, manual merges, legacy import and corruption repair all use this one route.

### 11.4 External units and cross-repository projects

Scientific code, data and evidence often span repositories. SSDS 8 governs one ledger per project; it does not provide atomic admission across repositories (§20). It supports cross-repository projects through immutable pins:

- An **external unit** is identified by an immutable source identity: a repository identity plus an immutable commit/tree and region, a package version with digest, a dataset hash or a DOI with variant/locator. Its content never changes, so `content` entries on it never go stale. A change of pin is an ordinary local content change, and its impact is derived locally.
- **External acceptance.** An `EXTERNAL_ACCEPTANCE` judgment imports the fact that the external project's own process accepted that exact revision and scope, citing its evidence, in the same way as legacy acceptance (§12.1). Without one, native reliance on the external unit is provisional. The judgment's basis names, in `record` mode, the consultation observation it relied on. An external correction or retraction is a binding/applicability event under the 6.6 semantic-definition owner. When a later consultation observes that the pinned triple is no longer accepted by its owner, or finds the external ledger `FORK`, `ROLLBACK` or retired, Admission records it with mandatory supersession of the earlier consultation, so every import relying on that consultation becomes non-current mechanically. A merely unreachable (`UNQUALIFIED`) external ledger supersedes nothing, which keeps network loss from flapping imports. A qualified actor may additionally raise a challenge on the importing subject. External status is only as fresh as the latest consultation. Re-consultation is an advisory Dispatcher obligation, and briefs show the consulted position.
- **Another SSDS project's ledger** may be consulted read-only. The consultation qualifies that ledger's head under its own witness model (§15.4); an unqualified external head is never imported. An observation records the qualified head consulted, the checkpoints used and the derived status read. The external ledger is never written, never merged and never treated as local authority.
- **Multi-repository change** is a sequence of admissions: the producer first, then the consumer pinning the producer's admitted commit. Intermediate states are visible and legitimate: the consumer stays on its older pin until its own admission.
- **Reconciliation.** The Dispatcher may observe that a newer external revision exists; that creates an advisory obligation, never a block.
- **Supported project class:** coupling through immutable pins (submodules, lock files, package versions, dataset hashes, DOIs). Scopes that must co-evolve atomically belong in one repository and one ledger; otherwise their transient cross-repository inconsistency is visible as provisional or advisory state, never hidden.

## 12. Migration and live coexistence

### 12.1 Governance modes

Every subject is in exactly one governance mode at any ledger position, and its parts share it (M3):

| Mode | Meaning |
|---|---|
| `NATIVE` | SSDS-governed: acceptance, conformance and evidence obligations derived and enforced by Admission |
| `LEGACY(p)` | governed by a declared legacy process bound to protocol version `p` (for example document-controlled SSDP 6.6); SSDS records and derives but does not adjudicate or reinterpret |
| `UNGOVERNED` | production content with no authority system yet (Case C); changes are recorded, mechanical consequences derived, no conformance claims made |
| `UNCLASSIFIED` | unknown content; excluded from governing context, evidence and acceptance basis until classified |

Mode transitions are admitted lifecycle records, and each ends the subject's tenure (§6.1). A version rollback that returns a subject to `LEGACY(p)` therefore needs a fresh `LEGACY_ACCEPTANCE` import; an import from before cutover never revives. A loss boundary is orthogonal to tenure (§15.4): tenure decides which acceptances count for a subject's current signature, and the boundary decides whether a record from before a known loss counts at all. A rollback after a loss therefore needs a fresh import on both counts. A cutover lost inside an abandoned interval leaves the retained mode in force, with every retained import withheld until requalified. A membership change that would move a unit between subjects of different modes is a mode transition for that unit and needs its lifecycle record (§6.8 step 4). Neither an ordinary request nor an adopted foreign declaration can do it silently. A change touching subjects in several modes receives the union of their obligations. Changes confined to `LEGACY(p)` or `UNGOVERNED` subjects may arrive as ordinary commits. They are absorbed mechanically (§6.8, §11), and derive only intake classification for uncovered paths plus whatever the mode's policy requires.

**Relying on legacy authority.** SSDS never adjudicates a `LEGACY(p)` subject, but native work often depends on legacy authority that its own process did accept (for example SSDP source accepted through `PROTOCOL-RELEASE-STATE.yaml`). A `LEGACY_ACCEPTANCE` judgment imports that fact. It cites the legacy process's acceptance evidence for an exact revision of an exact scope, and supplies the acceptance judgment for that `(subject, scope_id, rev)` without claiming SSDS reviewed it. The imported scope is the scope the legacy process actually accepted. A legacy acceptance of a whole document or release cannot be imported onto a section: that would be B1's projection. Native work relying on a legacy subject without an imported acceptance is provisional.

### 12.2 Reconstruction status, refinement and subject promotion

Authority-bearing subjects carry a reconstruction status: `OPAQUE` (internal semantic structure unknown), `PARTIAL`, `RECONSTRUCTED`.

**Structural refinement** is an admitted change that partitions a leaf's scope into new leaves declared as **parts** of the original unit, which becomes (or remains) a composite subject. Scope conservation is checked mechanically: the children's scopes are disjoint and their union is the parent's scope. Structural refinement makes no semantic claim. A byte-preserving refinement leaves the subject's scope identity, content identity, signature and tenure unchanged, and its semantic declarations unchanged unless relations are redirected. The subject's revision is therefore unchanged and its acceptance remains valid; nothing is copied or carried. The parts hold no acceptance of their own: every `validity` reliance on a part routes to the subject (§6.6). `content` reliance on a part is local to its bytes. Refinement enables locality of reading, context and parallel reconstruction without touching authority. Coarse relations stay on the subject until redirected to parts by authored relations. Redirection is a change to semantic declarations and therefore a new subject revision that needs acceptance.

**Subject promotion** makes a part `A` of subject `P` into its own subject. It is a semantic act and needs both:

1. an admitted declaration change marking `A` as a subject, so `subj(A) = A` and a new tenure of `A` begins — authored by the request, or adopted from a quarantined foreign declaration (§11.2); and
2. an acceptance judgment on `(A, scope_id(A), rev(A))` in that new tenure, by an actor qualified for `A`'s domain under its owner's acceptance contract. If the request also changes `A`'s domain, the old domain's owner must release it as well (§6.8 step 4(a)), so promotion cannot route `A` to a weaker reviewer. The judgment records the actor's conclusion that `A`, read with its own declared relations, is a self-standing subject whose meaning the holistic acceptance of `P` supports. Its basis names `P`'s acceptance (`record` mode) and widens to `P`'s former scope until a completeness judgment narrows it (§6.5). For a `LEGACY(p)` subject, only the legacy process can accept `A` separately; SSDS does not.

Promotion and its acceptance take effect in one admission. The acceptance is recorded beforehand, by an independent reviewer, as a prospective acceptance in the frame of the promoting candidate, and it counts only for the tenure that the integrating admission starts (§6.9). A promotion without such an acceptance is rejected; one whose acceptance is no longer current in the frame leaves `A` invalid rather than silently valid. Promotion is rejected while `P` or `A` carries an unresolved blocking challenge or a revoked revision (§6.8 step 4). The judgment may conclude that `A` is not self-standing — for example, because `A` relies on a convention stated only in a sibling part. In that case `A` stays a part, or the owner first makes the coupling explicit as an authored relation (`A USES_DEFINITION B`). Members of a simultaneous-definition group are promoted together, as one composite subject whose scope also contains the SDG declaration, or not at all. Every legal cycle lies inside one SDG (§6.2), so no promotion can split a cycle. Neither conservative widening, byte identity nor an unchanged relation set can substitute for this judgment.

**Demotion and restoration.** Demoting a subject `A` into a part of composite `P` ends `A`'s tenure. `A`'s acceptance judgments leave `ACC(A)` permanently: they stay in the ledger as history, unsuperseded, but no future tenure counts them. Validity reliance on `A` now routes to `P`, which needs its own acceptance if it is new or its scope grew.

Restoring `A` to subject status later, by an ordinary request or by adopting a foreign declaration, is a promotion and starts a new tenure. It needs a new acceptance bound to the same admission (§6.9). No separate reinstatement kind exists: a reinstatement is an ordinary acceptance whose basis may cite the earlier tenure's judgments, reviews and evidence by `identity`. Prior evidence counts only where it is currently admissible: its target and execution bases are current, and stale passing evidence never confirms.

An old acceptance therefore cannot become current again because structure changed, and the protection has three independent locks:

1. repository presence never changes `Σ` (S11);
2. even an admitted restoration starts a tenure that excludes every earlier judgment;
3. after a recorded loss of admitted history, every earlier acceptance is withheld whatever the restored structure says, until requalified or attested (§15.4).

Challenges, revocations and supersessions target exact triples and records without tenure, so they bind the restored subject exactly as before. Demotion, restoration and every other signature change are frozen while any affected subject's current revision is under unresolved blocking challenge or revoked (§6.8 step 4(b)). A challenge thus constrains a role transition rather than following the unit out of it.

**After promotion.** `P` keeps its frozen scope, which still includes `A`'s bytes, and so keeps its tenure. `P`, and validity reliance on its remaining parts, therefore stays valid only while that whole scope is byte-identical to `P`'s accepted revision. Once `A` evolves, reliance on the remaining parts needs one of three things: a scoped `EQUIVALENCE` judgment for their consumers; acceptance of a residual subject (a new scope); or, for `LEGACY(p)`, a new legacy acceptance. A **carve-out** is a promotion after which `A` leaves `P`'s governance mode (for example, cutover of one section, §12.4); the same rule applies.

**Equivalence across scopes.** An equivalence judgment relates revisions of one unit; it never relates different scopes. Acceptance moves to a new scope only through an acceptance judgment on that scope (promotion). Everything else stays historical lineage.

This replaces LegacyAggregate: a legacy aggregate is a coarse `OPAQUE` subject, and "digestion" is structural refinement followed, where wanted, by qualified promotion.

### 12.3 Discovery bottom-up, acceptance top-down

Agents may propose candidate D3, D2 and D1 units reconstructed from D4 behavior, papers, comments, tests and history (reconstruction judgments). A proposed upstream unit is accepted only through its owner's acceptance (human-gated where policy requires). Until then, descendants that rely on it are provisional, and no D4 behavior creates accepted authority. Reconstruction that cannot recover intent records `PROVISIONAL` or `UNKNOWN` explicitly (M5).

### 12.4 Cutover

A transition of a subject from `LEGACY(p)` or `UNGOVERNED` to `NATIVE` requires:

1. adequate reconstruction status under policy;
2. a migration-equivalence judgment that representation changed but behavior and meaning did not (or a separately governed change if they did);
3. owner acceptance of the native revision of that exact subject;
4. for a carve-out from a legacy subject: the subject promoted first, and a human-gated record by the legacy process owner releasing that scope from the legacy process (§12.2);
5. disposition of every in-flight legacy run on that subject: drained, pinned to its version in an isolated workspace, or explicitly migrated (M6);
6. an admitted cutover record.

After cutover only Admission governs the subject. Legacy-side edits to it are foreign changes (§11), and the legacy representation is historical. A part cannot cut over apart from its subject. Interrupted migration leaves no half state: each refinement, promotion and cutover is one admission.

### 12.5 Deployment cases

| Case | How it enters | What is special |
|---|---|---|
| A native project | genesis with fine subjects; all `NATIVE` | nothing |
| B SSDP 7 or earlier documents | manifest declares section-level **parts** of each legacy subject (the scope its process accepted: a document, or a release tree) without rewriting files; mode `LEGACY(p)`; relations extracted heuristically are `CANDIDATE`/proposed | version-pinned workplans stay governed by their protocol; section locality serves reading and context, while validity of a section routes to its legacy subject; promotion and scope-local cutover per §12.2-§12.4 |
| C mature repository without authority | a few coarse `UNGOVERNED`/`OPAQUE` subjects by top-level region; analyzers give derived structure early | bottom-up reconstruction proposals, top-down acceptance; production continues |
| D live partial migration | mixed modes | a production edit to a unit makes non-current exactly the reconstruction judgments whose basis named it; unrelated migration work is unaffected — no special rule |
| E external or foreign-agent branch | intake of a change with unknown basis | provenance recorded; obligations derived from touched units |
| F drift or corruption | intake; derived state rebuilt; ledger integrity and currentness qualification checked | §13 |

Genesis for an existing repository records project identity, ledger location, the authoritative ledger replica, trust roots, witness set and quorums, ruleset version, the initial effective structure and coverage, and the baseline commit. Per FF-001, no genesis or cutover identity is published as immutable before every required declaration and record exists and validates.

### 12.6 Documents, workplans and skills after cutover

Change plans and authority documents remain semantic artifacts. In natively governed documents, lifecycle fields (`status:`) and directory placement (`active/`, `archive/`) are either removed or generated from derived state and marked non-authoritative; a manual edit to them enacts nothing. Skills remain epistemic procedures and stop owning workflow transitions represented by rules. Historical pre-cutover workplans and records stay immutable under their original semantics.

## 13. Failure, recovery and long-horizon evolution

| Failure | Detection | Repair |
|---|---|---|
| Corrupted derived state | integrity checks, mismatch with re-derivation | discard and re-derive |
| Corrupted ledger entry | authentication, hash chain, schema validation | restore from a replica whose chain qualifies (§15.4); else human-gated `LEDGER_LOSS` (§15.4). Its position is a continuity boundary: every permissive effect recorded before it is withheld until requalified or attested, and S3 lists each as a requalification obligation. Prose or reports may inform new judgments by qualified actors but never restore old records. Repository declarations newer than the retained ledger also appear as quarantine, but that is not the loss defense: the boundary holds when product and ledger were restored to the same stale snapshot and `Q` is empty |
| Ledger ref rewound (force-push, hosting restore, backup older than the admitted head, mistaken or malicious reset) | head is a strict ancestor of a checkpoint observed in a read quorum (every admitted head is visible there, §15.4) or of a high-water mark | fail closed (`ROLLBACK`); restore the later chain from any replica or clone that holds it (no boundary); if none does, human-gated `LEDGER_LOSS` with its boundary; Admission halted until resolved |
| Ledger and product restored together to one stale snapshot after a later admitted head existed | `ROLLBACK` from the witnessed later checkpoint, although the restored tree agrees with the retained ledger (`Q` empty) | as above; if the suffix is unrecoverable, `LEDGER_LOSS`: the boundary withholds every pre-loss acceptance, support and relief regardless of the agreement, and `LEDGER_LOSS` re-establishes witness model, trust roots and ruleset (§15.4) |
| Ledger fork, or witnesses holding checkpoints on conflicting chains | qualification | fail closed (`FORK`); human-gated fork resolution choosing one lineage and naming the abandoned head; key rotation if compromise is suspected; never auto-merged |
| Crash after append, before admission | provisional entry on the ledger ref | on restart Admission completes anchoring of the surviving entry (idempotent; nothing else could append in between). If no copy survives, the witness count decides (§15.4): when the non-admission bound proves it never reached `q_a`, a human-gated fork resolution abandons it with no boundary, nothing admitted is lost, and its request is resubmitted by identity; otherwise it may have been admitted, and abandoning it is a `LEDGER_LOSS` |
| Crash after admission, before publication | admitted head entry; publication `PENDING` (no later entry carries `obs`) | §15.3: the entry's publisher performs the compare-and-swap once, behind a write-ahead intent, if the head still shows `B_n`; every other host, or a publisher whose log holds an intent or is lost, appends a fencing absorption and moves the ref to a fence commit, after which the outstanding effect cannot apply; human attention is decided only after the fence settles |
| Crash after the publication compare-and-swap, before any later entry | admitted head; integration ref shows `C_n` or has moved on | restart reads the head: `C_n` or an equivalent publication gives a consistent successor (`PUBLISHED`), ordinarily the next admission; later foreign movement gives an absorption (`PUBLISHED` if `C_n` is still reachable, else `OVERTAKEN`); a reset to exactly `B_n` is the ABA case (§15.3) |
| Reconciling entry appended, not admitted | provisional successor | complete its anchoring; if it vanished (and was provably never admitted), re-read the integration head and append a new successor |
| Witnesses below read quorum (unreachable or lost) | qualification cannot complete | `UNQUALIFIED`: historical views only, no current assertion, Admission halted, production continues; permanent loss beyond the fault bound needs human-gated witness-set redesignation (§15.4) |
| Witnesses lost beyond the fault bound, ledger objects intact | `UNQUALIFIED` | human-gated witness-set redesignation continuing from the intact head when every reachable checkpoint, replica and high-water mark ends there; the record states that continuity rests on that evidence (an assumption beyond the fault model). Any reachable evidence of a later head not provably never-admitted makes it a `LEDGER_LOSS` |
| Ledger objects lost, witness checkpoints intact | `ROLLBACK`: witnesses hold checkpoints beyond every recoverable entry | `LEDGER_LOSS` naming the retained head and the abandoned heads the witnesses hold; boundary |
| Abandoned entries later surface | an authenticated chain conflicting with an admitted abandonment record | never merged; recorded as evidence with an S3 integrity obligation; may ground a challenge to a continuity attestation; the boundary stays |
| Authoritative replica lost | unreachable or empty | restore from any replica extending the highest observed checkpoint; human-gated replica redesignation record; if no replica extends it, `LEDGER_LOSS` |
| Fresh clone (with or without a historical prefix) | no high-water mark | qualify against a read quorum; fetch the missing suffix (`BEHIND`) or detect `ROLLBACK`; with no read quorum, views are `UNQUALIFIED` and Admission refuses to append |
| Lost local store, intact repository | absent operator state | ledger is in Git; operator journal rebuilt; running executions reconciled by observing harnesses and workspaces; stale leases released; high-water mark re-established by qualification |
| Foreign structural change (manual manifest edit, force-push, restore from stale backup, manual conflict resolution) | observed declarations differ from `Σ` | absorbed; bytes remain buildable; deltas quarantined; `aff(Q)` invalid until adopted or realigned (§11.2-§11.3); no tenure restarts and no acceptance revives |
| Content objects referenced by the ledger unavailable | object lookup | binding health `UNAVAILABLE` for affected derivations; fail closed for dependent closure; restore objects from any replica (the ledger keeps referenced commits reachable) |
| Repository move, clone | — | project identity is in genesis, not in paths |
| Project fork (intentional) | fork lifecycle record | new project identity; cross-fork work enters by intake; ledgers never merge automatically |
| Analyzer version change | derivation key change | re-derive; judgments whose basis named analyzer output become non-current only if the output changed (early cutoff) |
| Relation or record schema change | schema version | explicit READ/MIGRATE/REJECT; migration is an admitted lifecycle record; old records retained |
| Ruleset change | ruleset adoption record | admissions are never re-adjudicated; current derivation uses the adopted ruleset; a previously discharged obligation that the new ruleset no longer considers discharged becomes an open obligation, never rewritten history; a relation reclassification that makes an accepted structure illegal makes its subjects ill-formed until repaired; effective structure and quarantine are unchanged; historical views are reproducible with the ruleset in force at their position |
| Interrupted migration | — | refinement, promotion and cutover are atomic admissions |
| Very old task returns | basis check | current basis: admissible; stale basis: recorded as observation and routed to revalidation |
| Check template found defective (false positive or false negative) | a finding, challenge or qualification result against the template | a corrected template enters by human-gated ruleset adoption; admissions are never re-adjudicated (P2); current conformance is re-derived under the adopted ruleset, so a candidate wrongly blocked becomes integrable and an integrated result that the corrected template would flag gets an integrity obligation, never a silent revocation |
| Coordination task lost mid-decision (crash, context limit, model change) | the `COORDINATE` obligation stays open | a new coordination task from a freshly rendered decision brief; nothing the lost execution held was canonical (§9.7) |
| Human unavailable | human-attention obligations stay open | dependent work stays not ready; independent work proceeds; nothing is closed on the human's behalf (§9.8) |
| Concurrent results from stale bases | currency at admission | first admitted; others revalidated only where their basis intersects |
| External evidence artifact disappears | availability observation | binding health degraded; present use `UNAVAILABLE`; rerun or remap obligation |
| Manual edit of authority | drift | intake; every reliant record non-current; acceptance of the edited revision (a light representation-only acceptance when editorial) plus an independent equivalence judgment restores reliant records without re-reviewing them; otherwise normal impact closure |
| Migration under a wrong interpretation | later challenge against the reconstruction or promotion judgment | upheld challenge revokes it; dependents non-current or provisional; blast radius computed from bases |
| Completeness claim proves false | challenge to the completeness judgment | every inference that used it becomes non-current |
| Crash before the append | no entry with the request identity | nothing happened; request retried idempotently |
| Sensitive value found in a ledger entry or pinned content | Admission checks, audit, report | §15.5 breach protocol |
| SSDS 9 migrates SSDS 8 | — | ledger is self-describing and versioned; SSDS 9 either reads it compatibly or starts a new lineage with a migration record naming the SSDS 8 last admitted head; no reinterpretation of admissions |

Recovery-time objective: derivation of current state must not require replaying an unbounded history. Derived checkpoints keyed by `(ledger position, ruleset, schema, analyzer versions)` bound restart cost and are verified against the ledger before use. They cache the derivation of a position, including `Σ`; they carry no currentness, which belongs only to the qualified head (§15.4). They are unrelated to the witness checkpoints of §15.4.

## 14. Where machinery must stop

Deterministic machinery prepares, but never decides:

- whether two scientific or numerical formulations mean the same thing, and whether a change is editorial or semantic beyond byte/normalization identity;
- whether an acceptance of one subject supports a newly scoped subject (promotion, carve-out, restoration);
- whether a foreign structural declaration expresses intended governance (adoption of a quarantined delta), and whether a set of objects is genuinely simultaneously defined;
- whether an observed discrepancy is a D4 defect or exposes inadequate D3, D2 or D1;
- whether evidence actually supports a governed claim, and whether gate evidence is adequate;
- whether an inferred or searched-for relationship is materially real; whether a relation scope is complete;
- how an ambiguous legacy region decomposes and what its upstream intent was;
- whether an architectural change preserves its parent abstraction;
- whether a Serious Challenge is warranted, how it is adjudicated, and whether a risk override is acceptable;
- whether a marked product surface is accepted (only by the product-scope owner, the stakeholder or task authority, at an existing gate; technical D3 Review alone never accepts it);
- whether a confidentiality incident requires destructive remediation.

For each, the machinery produces a **focused question**: the exact subject, scope and revisions; the distinctions already resolved; the evidence and its status; what the answer will change; and the allowed outcomes. The answer is a recorded judgment that then propagates mechanically.

## 15. Persistence, publication, trust and security

### 15.1 Stores

| Store | Content | Canonical? | Location | Sole writer | Recovery |
|---|---|---|---|---|---|
| Content store | all repository content including authored relations, unit manifests and anchors (the *observed* state) | yes, for meaning; structural declarations are proposals until admitted | the project's Git repository | humans and tools through Git; Admission only by publication CAS | Git replication; foreign movement absorbed (§11); referenced commits kept reachable by the ledger |
| Ledger | records (§6.3) under the closed schema, from which effective structure, ruleset and acceptance derive | yes, for everything not derivable | one authoritative ref in a Git repository designated at genesis: the project repository's reserved namespace, or a dedicated (for example private) ledger repository | Admission | any replica extending the highest observed checkpoint; else human-gated `LEDGER_LOSS`, a continuity boundary (§15.4) |
| Witness checkpoints | authenticated `(ledger id, position, head)` statements and lineage-retirement statements; hashes only | no; evidence that admits entries and detects rollback | declared witnesses outside the authoritative replica's administrative control | Admission (checkpoints); any participant may relay an existing authenticated checkpoint (read repair) | redundancy by quorum; loss beyond the fault bound by human-gated witness-set redesignation |
| Derived index | derived state, effective structure and derivation checkpoints | no | local, rebuildable (SQLite or equivalent, delegated) | Derivation | discard and re-derive |
| Operator state | leases, reservations, account and quota telemetry, harness sessions, raw prompts and transcripts, signing keys and secret references, high-water marks | no project authority | private user-local root outside repositories | Dispatcher (journal); each participant's Ledger Store (its high-water mark); Admission (its keys and its publication-attempt log, which informs the ABA choice of §15.3 and is never read by derivation) | journal rebuilt by observing harnesses and workspaces; high-water mark re-established by qualification; keys by trust-root lifecycle |
| Transport | task and result envelopes on run branches | no | isolated run refs; retired by policy, never merged | Dispatcher and Interface (envelopes); agents (results) | regenerated from the ledger and obligations; results ingested only through Admission |

### 15.2 Storage decision

The consolidated Protocol 8 plan defaulted canonical history to a private local store. It permitted in-repository non-secret control state only when a later D3 adoption resolved concurrency, privacy, history and ownership. The f9d9de8 revision declared that adoption prematurely (B3). The candidates were re-evaluated on total fitness:

| Option | Commit atomicity | Machine loss | Multi-host | Rollback detection | Privacy | Authoritative representations |
|---|---|---|---|---|---|---|
| (a) private transactional store (SQLite) + governed repository export | local transaction | export lag is a loss window; restore needs the export | needs a hosted service, or the export becomes the authority | still needs anchoring of the export | private by default | two; after loss the export is the de facto authority |
| (b) f9d9de8: Git ledger with same-repository multi-ref atomic update | depends on a negotiated server capability | replicated | compare-and-swap | absent | in-repository; break-glass undefined | one |
| **(c) selected**: Git ledger, single-ref append, quorum admission, reconciled publication | single-ref compare-and-swap on every Git host, admitted by witness quorum | replicated with ordinary fetch/push | compare-and-swap | currentness only for quorum-witnessed heads; read/write quorum intersection; high-water marks | closed schema; optional private ledger repository; breach protocol | one, plus a small checkpoint witness set |

**Decision.** Retain a Git-replicated canonical ledger, re-specified as (c). Option (a) needs a second authoritative representation to survive machine loss, or a hosted service, and still needs the same anchoring. Option (b) rests correctness on a capability many deployments lack. Option (c) resolves the predecessor's four conditions explicitly: ownership and concurrency (§15.3), history (§15.3-§15.4), and privacy (§15.5). It adds only a checkpoint witness set, which P4 requires anyway: currentness cannot be proven by the replica it is meant to check. The D3 contract is complete at this level; deployment realizations listed in §21 item 14 remain Architecture Manual closure obligations, not open D3 choices. Reopen triggers are in §26. If the Manual finds a counterconstraint to Git-hosted storage, replacing it reopens D3, and any replacement must keep these requirements: append-only authenticated history; a single-writer append; currentness only for quorum-witnessed state; reconciled publication after admission; replication independent of any one machine; and the closed schema.

### 15.3 Commit point and publication

**Ledger representation.** Each admission or lifecycle entry is one Git commit on the authoritative ledger ref, whose parent is the previous entry. Git's commit chain is the ledger's hash chain. Each entry is authenticated under the declared trust mechanism (§15.4). The ledger keeps every content commit it references reachable from its own history, so product-ref force-pushes or deletions cannot make history underivable. When the ledger lives in a dedicated repository, that repository holds those objects.

**Append (one semantics, local and remote).** The append is a compare-and-swap of the single ledger ref from the expected previous head to the new entry:

- *local authoritative repository:* a local reference transaction with expected old value, under a declared durability configuration (object and ref fsync) sufficient for the claimed crash model;
- *remote authoritative replica:* a push of the single ledger ref with expected old value, which the server rejects if the ref moved. This needs no multi-ref capability.

A losing writer re-validates against the new head (§8.2).

**Commit point: admission by witness quorum.** An appended entry is **provisional**. It becomes **admitted** — current-qualified, and the commit point for every external effect — at the moment `q_a` witnesses have durably acknowledged its exact checkpoint (§15.4). The ordering is fixed:

```text
append (CAS, durable)  ->  PROVISIONAL
checkpoint acknowledged by q_a witnesses  ->  ADMITTED
then: submit response ADMITTED; integration-ref publication; dispatch from the new state;
      current-state answers at the new head; next append
```

Admission keeps **at most one provisional entry**: it appends entry `n+1` only after entry `n` is admitted. The single exception is a human-gated witness-set redesignation, which may be appended over a provisional entry and whose admission settles that prefix (§15.4). Because of this rule, the head Admission validates against (§6.8 step 6) is always admitted. A provisional entry never influences derivation that anyone relies on.

After a crash, the request identity tells Admission what happened. If no entry carries it, nothing happened and the request is retried. If a provisional entry carries it, Admission completes the idempotent checkpoint distribution; nothing else could have appended in between, so the validation still holds. If an admitted entry carries it, Admission proceeds to publication. A provisional entry whose every copy is lost is resubmitted by identity when qualification proves it never admitted; otherwise its loss is a `LEDGER_LOSS` (§15.4).

**Publication: intent, effect and observed outcome (C4).** An admission entry `n` names its admitted commit `C_n` and its base `B_n`. `B_n` is not an assumption: it is the integration head Admission read immediately before appending `n`. Entry `n` is therefore the complete, admitted **intent** of the effect — compare-and-swap the integration ref from `B_n` to `C_n` — and no separate intent record exists. A records-only request has `C_n = B_n` and no effect. Publication starts only after `n` is admitted, so no product ref ever shows provisional state.

The **observed outcome** enters through a field every entry carries: `obs`, the live integration head Admission read immediately before appending that entry (for an admission, `obs = B`). The exception is a human-gated recovery lifecycle entry (`LEDGER_LOSS`, fork resolution, witness-set or replica redesignation, lineage retirement), which carries no `obs`, so recovery never waits for the integration host. Derivation tracks the expected head `E` (§6.6 S0): `C_k` after admission `k`, `obs_k` after an absorption, unchanged otherwise. An **equivalent publication** of admission `n` is a commit, reachable from `obs` or equal to it, that descends from `B_n` and has `C_n`'s tree (a squash, rebase or merge-button result of exactly that content).

**Reconciliation rule.** Publication of admission `n` is reconciled by the first later entry that carries `obs`. The rule constrains that entry's *shape*; it never requires a step before it:

| `obs` of the first later entry | That entry may be | `pub(n)` (derived, §6.6 S0) |
|---|---|---|
| no such entry yet | — | `PENDING` |
| `E_n = C_n`, or an equivalent publication equal to `obs` | any entry, including the next ordinary admission; `E` becomes `obs` (same tree) | `PUBLISHED` |
| anything else | only an **absorption** of `obs`: a pure observation carrying no submitted records; `E` becomes `obs` | `PUBLISHED` if `C_n` or an equivalent publication is reachable from `obs`; otherwise `OVERTAKEN` |

The same shape rule governs every entry, so foreign movement after any entry is absorbed the same way. In the consistent row nothing in S0-S2 changes (`E` keeps its tree, so `T` is unchanged) and no S3 fact that validation reads changes, so a request validated at head `n` stays valid when its own entry also reconciles `n`. An entry whose `obs` differs from `E` and that carries submitted records is rejected by Admission and is an integrity defect in derivation. An `OVERTAKEN` admission keeps `C_n` recorded and reachable; its records are re-evaluated against the absorbed tree; an obligation to revalidate its request is derived (§8.2). Its structural changes are already in `Σ` but absent from the absorbed tree, so they appear as quarantine until the revalidated request publishes and realigns the repository (§6.8 step 4).

**Effect authority is revoked by moving the ref (`ac71fa9` Blocker C).** Every product-ref effect is a compare-and-swap from an expected head, and Git checks nothing else. An effect authorized by entry `n` therefore stays performable for as long as the ref shows `B_n`, whatever the ledger or a human has decided since. Revision 7 tried to revoke that authority by having the publisher check the ledger first, which only narrows the race: a publisher paused between its check and its compare-and-swap could reverse a human's "keep `B_n`". Revision 8 revokes authority the only way the ref enforces: it moves the ref.

- **One executor, at most once.** Each admission entry `n` has exactly one **publisher**: the Admission host whose per-host key authenticated `n` (§15.6). Only the publisher performs `B_n -> C_n`, at most once, after durably writing an intent for `n` to its write-ahead attempt log. That log must be monotonic for the publisher's identity. A log restored from a backup, copied from another host, shared by concurrent processes, or inherited by a replacement host that reuses the key is not intact, and an intact log is the only evidence of "no attempt" (§21 item 14).
- **Fencing.** A **fence commit** `F_n` has `tree(B_n)` and parent `B_n`, so it changes no content. A host that finds `L = B_n` and is not the publisher making its first attempt never waits on, trusts or second-guesses the publisher. After any operational wait (a liveness choice, never a correctness one), it appends a **fencing absorption** `k`: an absorption of `B_n` (`obs_k = B_n`, classifying `n` as `OVERTAKEN`) that carries the effect `B_n -> F_n` as its own publication, performed by its own publisher. "Not the publisher's first attempt" covers another host, a publisher whose log holds an intent for `n`, and a publisher whose log is lost. Exactly one of the two compare-and-swaps from `B_n` can succeed. If the fence lands, `n`'s outstanding effect can never apply from this ref state, because the ref no longer shows `B_n`. If `C_n` lands first, the next entry observes it.
- **Decisions only after settlement.** Human attention for an ambiguous `n` is raised by derivation when the first fencing absorption is admitted. A human decision on it is admissible only once `n` is **settled**: some later entry's `obs` shows the ref no longer at `B_n` (step 7). A non-`PENDING` classification is not enough. With several fences in a row, a later fencing absorption can classify an earlier fence `OVERTAKEN` while the ref still shows `B_n` and neither fence nor `C_n` has landed. Only an observation away from `B_n` proves that the outstanding effect can no longer apply (`730490d` N3). If the fence landed, the choices are to re-apply `n` (an ordinary revalidated admission onto `F_n`) or to keep `F_n`, and no outstanding effect can reverse either. If `C_n` landed first, `n` was published late. That is a `CRITICAL` integrity finding (§7.9), and the human chooses with the product already showing `C_n`: accept it, or revert by an ordinary admission.
- **Late publication.** For any admission classified `OVERTAKEN`, a later observation whose `obs` newly reaches `C_n` (or an equivalent publication) is a derived `LATE_PUBLICATION` integrity finding with `CRITICAL` human attention. After a fence, this can happen only if a foreign writer returns the ref to exactly `B_n` and a stale publisher then resumes. That is a deliberate foreign write to a superseded commit, outside SSDS's control, so the case is detected and escalated, never prevented: a disclosed residual.

**Admission's procedure** at an admitted head `n` whose publication is `PENDING` (it reads only the qualified ledger, the live ref and, for the publisher only, its own attempt log):

```text
read L
L = B_n, this host is n's publisher, its attempt log is intact and holds no intent for n
                              -> write intent for n durably; compare-and-swap B_n -> C_n; read L again
L = B_n, any other case       -> (after any operational wait) append a fencing absorption of B_n whose effect is
                                 B_n -> F_n; once admitted, its publisher performs that effect; read L again
L = C_n, or an equivalent publication equal to L
                              -> append the next entry with obs = L: the next ordinary admission if one is
                                 ready, otherwise an absorption with obs = L (records PUBLISHED; E keeps its tree)
anything else                 -> append an absorption of L: PUBLISHED if C_n or an equivalent publication is
                                 reachable from L, else OVERTAKEN
```

Recording an idle outcome is optional. A canonical `PENDING` with no successor is truthful: the governed tree is already `T_n`, and the next entry of any kind records the outcome.

**Every failure point.**

- *Crash before the compare-and-swap:* the publisher restarts and reads `L = B_n`. If its log holds no intent for `n`, it performs the effect. If the log holds an intent, it cannot tell a failed attempt from a success followed by a reset, so it fences. If the publisher never returns, a takeover host fences.
- *The compare-and-swap loses to a foreign push:* `L` is foreign; the next entry is its absorption; `OVERTAKEN` unless the foreign history contains `C_n` or an equivalent publication.
- *The compare-and-swap succeeds, then a crash before any successor:* restart reads `L`; `L = C_n` gives a consistent successor (`PUBLISHED`), ordinarily the next admission; later foreign movement gives an absorption, `PUBLISHED` if `C_n` is still reachable, else `OVERTAKEN` (an immediate force-push removed it from the product).
- *The successor is appended but not admitted:* it is the single provisional entry; restart completes its anchoring. If it vanished and is provably never admitted, nothing relied on it: read `L` again and append a new successor.
- *The successor is admitted but the response is lost:* `submit` by request identity returns the recorded decision.
- *Foreign movement between the compare-and-swap and the read:* the successor records what is live; classification is by reachability.
- *Repeated or replayed reconciliation:* only the first later entry carrying `obs` classifies `n`; any later observation concerns the then-expected head. Two hosts racing are serialized by the ledger compare-and-swap; the loser re-derives from the winner's entry, whose `obs` is canonical even if the loser read a different value.
- *Restart on another Admission host:* the procedure needs no operator state. Without the publisher's log, the only outcomes are observation and fencing; another host never performs `n`'s effect.
- *Publisher paused, takeover fences, human decides, publisher resumes:* the fence moved the ref to `F_n`, so the resumed compare-and-swap from `B_n` fails, and the human's decision stands. If the publisher's compare-and-swap won the race instead, the fence fails, the next entry observes `C_n`, and the human decides only after that observation.
- *Fence publisher paused:* another host fences again with a new fence commit; every fence moves the ref away from `B_n`, so every stale effect from `B_n` fails.
- *ABA:* a foreign reset of the integration ref to exactly `B_n` after a successful compare-and-swap is indistinguishable, from the ref alone, from a publication not yet applied. The reset may be a deliberate remediation, and C4 requires ambiguity to be reconciled before retry. Every `L = B_n` that is not the publisher's first attempt is fenced, and the human decides only after the fence settles. Every path is a recorded, replayable entry; the attempt log informs only the publisher's own choice and never derivation. Revisions 4-5 allowed silent re-application without the log (`ffbad17` N2). Revision 6 trusted one host's log about every host (`f3608f5` Blocker C). Revision 7 relied on a ledger check that a paused publisher could outlive (`ac71fa9` Blocker C).

**Idempotency.** The effect identity `(ledger id, n, B_n, C_n)` is fixed by entry `n`; a compare-and-swap from the exact expected predecessor is idempotent and never overwrites foreign work. The reconciliation is identified by its position `n+1`, made unique by the ledger compare-and-swap. Request identity keeps `submit` idempotent.

**Replay uses recorded facts only.** Classification reads `B_n`, `C_n`, `obs` and the immutable commits reachable from `obs`, which the ledger keeps reachable (ledger representation, above). It never reads the live ref, so a replay explains, from the ledger alone, which entry resolved the publication and why.

**No hidden cycle.** The dependency order is: `n` admitted -> effect (needs only `n`) -> read `L` -> append `n+1` (needs only that read) -> admission of `n+1`. Nothing on that chain waits for `n+1`. Revision 3's defect was a precondition ("resolve before appending") whose evidence could arrive only by appending; here the evidence *is* the append.

**No second writer or authority.** Admission alone reads `L` for canonical purposes and alone appends; the reconciling entry is an ordinary entry under the same compare-and-swap and quorum admission. A Dispatcher census may request an absorption; it records nothing itself.

**Cost.** In ordinary operation each admission is still one entry and one quorum round, because the next admission carries its predecessor's outcome. A separate entry appears only when the ref moved (an absorption, needed in any design) or when Admission chooses to record an idle outcome.

**Three derived states suffice.** Revision 3 had the right states but no transition carrier. A fourth `RECONCILING` state would describe Admission's in-flight procedure, which is operational and leaves no canonical trace until the successor exists. Being provisional is a property of the ledger entry, and publication is never attempted for a provisional entry.

Admission never moves the integration ref except by compare-and-swap from the exact expected predecessor, so it never overwrites foreign work. Revision 2 allowed updating the ledger and integration refs in one multi-ref transaction as an optimization; that is withdrawn, because it would publish an entry before admission. If the authoritative replica, the integration host or a witness read quorum is unreachable, admissions stop (fail closed) while production continues; recovery lifecycle entries need only the replica and witnesses.

### 15.4 Currentness qualification and anti-rollback

**Contract (P4).** Currentness is asserted only for durably witnessed state. A head is *current-qualified* only when a witness quorum holds its exact identity and it extends every checkpoint and high-water mark the evaluator observes. Every current-state assertion names its qualified head. Revision 2 claimed this while also permitting an undetectable rewind inside a bounded anchoring lag. That mode is withdrawn, and the claim now holds without exception under the declared witness model.

**Witness model.** Genesis declares `N` witnesses outside the authoritative replica's administrative control, an admission quorum `q_a`, a read quorum `r`, and a fault bound `f`, with

```text
q_a + r > N + f        (any admission quorum and any read quorum share more than f witnesses)
```

A faulty witness may be lost, rolled back or adversarial. Genesis and every witness-set redesignation reject parameters that violate the inequality. The declared single-user local-trust mode is the instance `N = 1, q_a = r = 1, f = 0`, with the witness on another medium under the same user. It is the same contract under a stated premise (that witness is not rolled back together with the replica), and status views show the mode.

**Threat and trust model.**

- *Defended against:* mistaken force-push or deletion of the ledger ref; hosting restore from an older backup; a compromised push credential for the authoritative replica; replica divergence after failover; direct pushes of crafted entries; crashes at any point; loss, rollback or misbehaviour of at most `f` witnesses.
- *Trusted:* Admission signing keys declared in genesis trust roots and held only in private operator state; at most `f` faulty witnesses; each participant's own high-water mark.
- *Not defended:* more than `f` faulty witnesses acting with control of the replica; forgery by a holder of an Admission key (such forgery shows up as a fork if any honest copy exists); the information-theoretic case below.

**Mechanism.**

1. **Authentication.** Every ledger entry is authenticated: signed by an Admission key in the trust roots, or protected by local access control in declared local-trust mode. Derivation rejects any chain containing an unauthenticated entry; this is how a direct push to the ledger ref is detected.
2. **Admission by quorum.** After each append, Admission sends an authenticated checkpoint `(ledger id, position, head)` to every witness. The entry is admitted when `q_a` witnesses have acknowledged durable retention (§15.3). Witnesses retain every checkpoint they receive, append-only per ledger id. Any participant may relay an authenticated checkpoint it has seen to further witnesses (read repair); relaying can complete a quorum but cannot forge one.
3. **High-water marks.** Every participant that presents current state (Admission, Dispatcher, Interface hosts, clones) keeps the last head it qualified, in private operator state.
4. **Qualification.** An evaluator with authoritative-replica head `A` and high-water mark `W` collects checkpoint sets from at least `r` witnesses, then classifies:
   - `FORK` — two observed checkpoints, or `A` and an observed checkpoint, lie on conflicting chains, with no authenticated human-gated resolution record in `A`'s chain naming the abandoned side;
   - `ROLLBACK` — `A` is a strict ancestor of an observed checkpoint or of `W`, with no admitted abandonment record (`LEDGER_LOSS`, fork resolution) in `A`'s chain naming it. For a non-authoritative copy that can fetch the missing suffix from a replica, the state is `BEHIND`: fetch, then re-qualify;
   - otherwise, the **qualified head** `H*` is the highest entry of `A`'s chain that the evaluator observes held by `q_a` witnesses (after read repair if needed) and that extends every observed checkpoint and `W`. `A` is either `H*` or `H*`'s single provisional successor, which is labeled `PROVISIONAL` and never presented as current;
   - `UNQUALIFIED` — fewer than `r` witnesses respond, or no head can be confirmed at `q_a`. Only historical views are available, no current assertion is made, and Admission does not append.
5. **Use.** Every current-state answer, task brief, readiness decision for dispatch, snapshot export, external consultation and publication is bound to a named `H*`. Admission's own validation uses the head it holds by compare-and-swap, which is admitted by construction (§15.3). Every other participant's assertion is "current as of `H*`". Nothing irreversible depends on a non-Admission participant's notion of currency: results are revalidated at Admission (K4).

**Why the contract is sound, and where information runs out.**

- *Every admitted head is seen.* An admitted head is held by `q_a` witnesses. Any `r` responses include more than `f` of them, so at least one honest holder. Every qualifying evaluator therefore observes every admitted head, and an older prefix cannot qualify. This is what defeats the Review's L99/L100 world: if L100 was admitted, a fresh clone that sees replica head L99 also sees the L100 checkpoint and reports `ROLLBACK`; if L100 was not admitted, L99 *is* the current head and saying so is true.
- *An unadmitted entry was never relied on.* No effect, publication, dispatch or answer depended on an entry that never reached `q_a`.
- *The limit.* If every copy and every checkpoint of such an entry disappears, nothing distinguishes it from never having been appended, and no architecture can infer it. SSDS needs no such inference, because it never granted that entry currentness; its request is resubmitted by identity.
- *A partial trace.* If a checkpoint of a vanished entry survives, evaluators that see it report `FORK` or `ROLLBACK` and fail closed until a human-gated record names it abandoned. When the non-admission bound below proves it never reached `q_a`, abandoning it loses no admitted judgment; otherwise the abandonment is a `LEDGER_LOSS`.

The architecture thus aligns the definition of provable currentness with the durable evidence that proves it.

**Known loss of admitted history (P5).**

*Abandonment versus loss.* A human-gated record may abandon a head that is not in the retained chain. Whether that abandons admitted history is decided from witness reports, never asserted. Let `h` be the number of responding witnesses that hold the abandoned checkpoint and `m` the number not responding. Checkpoints are authenticated, so no witness can claim one it never received, but up to `f` responding witnesses may deny one they hold. The entry is **proved never admitted** iff `h + m + f < q_a`, and **known admitted** iff `h ≥ q_a`; otherwise it is **possibly admitted**. Abandoning only proved-never-admitted entries is a fork resolution with no boundary: nothing admitted is lost and nothing is requalified. Abandoning a known or possibly admitted head is a `LEDGER_LOSS`, whichever lifecycle record carries it; a fork resolution or witness-set redesignation that does so embeds one. When the bound is inconclusive because witnesses are unreachable, waiting for them is always an alternative to a boundary.

*What `LEDGER_LOSS` names.*

- the **retained head** `R`: position and hash of the highest entry of the retained, authenticated chain from genesis;
- every **abandoned head** known from witnesses, replicas or high-water marks, each with position, hash and witnessed admission status; the highest gives `h_max`, and the lost interval is at least `(R, h_max]` — later unknown entries may also have existed;
- the **evidence**: the content identity of the qualification report that gathered those reports;
- the **global control facts** in force from its position: witness model `(N, q_a, r, f)` and witness set, trust roots, and ruleset (system version and policy hash). Each may equal its retained value. The human gate re-establishes them because the lost interval may have changed any of them, and their effect is project-wide, so no scope can narrow it;
- the human gate's authenticated decision.

It is appended on the retained chain at position `R + 1`, carries no `obs`, and is admitted under the quorum it re-establishes (and under the old one where reachable). Once admitted, it names the abandoned heads, so qualification classifies them as abandoned rather than `ROLLBACK` or `FORK` (rule 4). A lineage whose old witnesses hold a retirement statement (§15.5) cannot take a `LEDGER_LOSS`; recovery continues in the successor lineage.

*The boundary.* The `LEDGER_LOSS` position is a continuity boundary; no epoch or generation identifier exists. Its effect is the S1 predicate `cont` (§6.6): a record admitted before the boundary has no permissive effect after it unless held. Polarity decides what is withheld:

| Retained fact | After the boundary |
|---|---|
| acceptance, conformance, plan acceptance, completeness, equivalence, evidence assessment, legacy and external acceptance imports, reconstruction and intake judgments | not current (S2 `base = F`) until requalified or held |
| evidence realizations, external consultations and other observations cited in `record` mode | not current until requalified (a fresh realization or consultation) or held |
| relaxers (§6.6 S1): `DISMISSED` adjudications of ordinary challenges, withdrawals, risk overrides, attestations of earlier boundaries, `UPHELD` adjudications of counter-challenges | not in force: their challenges reopen, their blocks return, and a revocation lifted by a successful counter-challenge returns |
| ordinary challenges and counter-challenges, restrictive adjudications and the revocations they produce, `DISMISSED` adjudications of counter-challenges, supersessions | unchanged (never gated by `cont`; none of them relaxes a block or a revocation; their effect as dispositions of a disagreement is in the row below) |
| task results and check executions (§7.7-§7.8) | not current until requalified: a new iteration or a fresh execution on the candidate |
| reports, findings and the escalation, coordination and adjudication obligations derived from them (§7.9) | unchanged: those obligations are keyed on the report's existence and identity, never its currency |
| failing assessments in a disagreement, and the disagreement itself (§6.6) | unchanged: adversity follows existence and bearing, never currency |
| dispositions of a disagreement (a supersession, an upheld challenge or an `IMMATERIALITY` judgment that disposed of a failing assessment) | withheld *as dispositions* (`eff` includes `cont`): the disagreement returns until disposed of again after the boundary; their other effects (removal from support, revocation) survive |
| coordination decisions, materiality reclassifications and human acknowledgments that resolved a report (§7.9, §9.8) | not in force: the report's obligation reopens and is decided again, by the principal or the human |
| effective structure `Σ`, tenure, quarantine, admitted trees and content | unchanged: they route and restrict, and validity still needs a current acceptance |
| availability degradations, adverse consultations | unchanged (restrictive) |
| witness model, trust roots, ruleset | as re-established by the `LEDGER_LOSS` |
| derivation at positions before the boundary (historical views) | unchanged: deriving an earlier prefix never reads later records |

*Requalification* uses existing kinds only: a fresh acceptance, adjudication, assessment, realization, import or consultation after the boundary, whose basis may cite the withheld records by `identity`, as reinstatement already does (§12.2). S3 derives one requalification obligation for each permissive record or relaxer that was in effect at `R` and is withheld now, so recovery work is enumerated rather than rediscovered, and readiness orders it top-down.

*Narrowing.* Nothing mechanical can prove a retained effect unaffected: witnesses hold only hashes, the product holds content but no judgments, and a stale-consistent restore shows no difference at all. The only sound narrowings are recovering the lost entries themselves (then nothing is lost and no boundary is needed) and an accountable judgment. A **continuity attestation** is a human-gated challenge-tier judgment by an actor that policy designates. It targets one `LEDGER_LOSS` and names the retained scope it holds unaffected, either as the complement of a possibly-affected set of subjects and records or as an explicit set, citing its out-of-band evidence (hosting history, notifications, CI artifacts, operator journals, an abandoned chain if one is available) by content identity. A record is covered according to `exposed` (§6.6 S0). While in force the attestation holds what it covers, and dependents follow through S2. Any qualified actor may challenge it; an upheld challenge withdraws it permanently, and a later boundary withholds it like any relaxer unless that boundary's attestation holds it. It is the only way a pre-boundary record becomes current again without a fresh record, and it is an accountable act, never an inference from agreement between product and ledger.

*Why a stale-consistent restore cannot resurrect authority.* While any read quorum shows a later checkpoint, qualification refuses to present the stale ledger as current (`ROLLBACK`). Continuing therefore requires an admitted `LEDGER_LOSS`, which is a ledger fact independent of product content. The boundary reads only ledger records, so agreement between the restored tree and the retained ledger is irrelevant: `Q` may be empty and nothing revives. At every position at or after the boundary, `current(x) ≤ base(x) ≤ cont(x)` for every earlier record `x`, and every earlier relaxer is in force only if `cont` holds. Every `T` or `P` support therefore rests only on records after the boundary or on records held by an in-force attestation. Tenure is not needed for this argument, and the boundary is not needed for tenure's: the two locks are independent (§12.2).

*The five recovery situations.*

| Situation | Recognized by | Boundary |
|---|---|---|
| rollback with a recoverable suffix | `ROLLBACK` or `BEHIND`; some replica holds the suffix | none: restore it |
| stale product restore, ledger intact | the next entry's `obs` differs from `E` | none: absorption, drift and quarantine |
| ledger-only truncation, newer product still observable | `ROLLBACK`; suffix unrecoverable | yes; the next entry also absorbs the newer product, adding drift and quarantine |
| admitted history known lost, product equally stale | `ROLLBACK`; suffix unrecoverable; `Q` empty | yes; the boundary alone protects |
| only provably never-admitted entries lost | the non-admission bound holds | none: fork resolution; no requalification |

*Where information runs out.* If every copy, checkpoint and high-water mark of an admitted head is lost — more than `f` witnesses failing together with every replica — and the product is restored stale as well, nothing distinguishes that world from one in which the head never existed, and no architecture can infer it. A witness-set redesignation that continues from an intact head after losing more than `f` witnesses records that assumption explicitly (witness lifecycle, below). A continuity attestation can be wrong: it is accountable and challengeable, not infallible. A holder of recovery authority who abandons a recoverable suffix can withhold admitted history from continuity until the abandoned chain surfaces; it is then evidence, never silently merged (§13).

**Distinctions.**

| Term | Definition | Consequence |
|---|---|---|
| valid historical prefix | an authenticated chain from genesis to some entry | historical views only |
| provisional entry | appended, not yet held by `q_a` witnesses; at most one exists | never current; completed or resubmitted |
| admitted (qualified) head `H*` | §15.4 rule 4 | the only input to current assertions |
| `BEHIND` | a non-authoritative copy lacking a fetchable admitted suffix | fetch, then re-qualify |
| `ROLLBACK` | the authoritative head is a strict ancestor of an observed checkpoint or high-water mark, with no abandonment record | fail closed; restore |
| `FORK` | conflicting authenticated chains or checkpoints from one genesis | fail closed; human-gated fork resolution naming the abandoned head; never auto-merged |
| loss | a known or possibly admitted entry unavailable from every replica | human-gated `LEDGER_LOSS`: a continuity boundary withholding pre-loss permissive effects until requalified or attested (P5) |
| abandoned provisional | a checkpoint whose entry survives nowhere, proved never admitted by the non-admission bound | human-gated fork resolution; no boundary; nothing admitted is lost |
| `UNQUALIFIED` | no read quorum, or no head confirmable at `q_a` | historical views only; Admission halted |
| retired lineage | the old lineage's witnesses hold a retirement statement naming a successor (§15.5) | historical views only, from any mirror |
| recovery | restoring a replica whose chain qualifies; redesignating the authoritative replica by a human-gated lifecycle record | resume |

**Witness lifecycle.** The witness set and quorums are declared in genesis and change only through a human-gated `WITNESS_SET_REDESIGNATION` lifecycle record. Where the old quorum is reachable, the record is admitted under both the old and the new quorum. Where it is not, the human gate gathers every reachable checkpoint, replica head and high-water mark and names the head the new set continues from. If any of that evidence names a later head that is not proved never admitted, the record carries a `LEDGER_LOSS` and its boundary. If none does, the record states that continuity rests on that evidence being complete: an assumption beyond the fault model, disclosed rather than hidden. Witness admission latency sits on the Admission critical path; it is a reopen trigger (§26), not a reason to restore a lag window.

A project fork is different: an intentional lifecycle record creates a new project identity (§13).

### 15.5 Privacy and confidentiality

**Prevention.**

1. **Closed, reference-oriented schema.** Ledger fields are identifiers with declared grammars, enumerations, content hashes, integers, recorded observation times, validated repository-relative paths, and content-identity references. There are no free-text fields. Reasons are enumerated codes. Rationale and reports are referenced by content identity: they live in repository content under ordinary hygiene, or in a private store.
2. **Bounded Admission checks.** Grammar validation, known-credential patterns and high-entropy detection over every string-valued field. Where policy enables it, the same scan runs over the candidate diff. A hit rejects the request with a reason code. These checks are preventive help, not a confidentiality guarantee.
3. **Operator secrets** (signing keys, tokens, prompts, transcripts, account telemetry) live only in private operator state.
4. **Visibility separation.** When governance records must be more private than the product, genesis places the ledger in a dedicated private repository; semantics are unchanged (§15.3).

**Breach protocol.** This applies when a sensitive value is found in a replicated ledger entry, or in product content that the ledger pins.

1. Treat it as a human-gated security incident under the security owner; halt Admission for the affected ledger.
2. **Rotate or revoke** every exposed credential immediately. For credentials, rotation is the remedy that restores security, and it does not wait for any purge.
3. **Inventory replicas**: authoritative replica, other remotes, clones, mirrors, forks, CI and harness caches, hosting retention and backups. Checkpoints contain hashes only.
4. **Choose remediation by confidentiality need** (human decision):
   - *Rotation suffices* (the value is useless after rotation): keep history; append a `REDACTION_NOTICE`; no guarantee yields.
   - *Confidentiality required:* create a replacement ledger lineage in a new or private repository.
     - **Settle the old head.** Settle any provisional entry of the old lineage first: admit it (always possible while its witnesses are reachable), or abandon it only if the non-admission bound proves it never admitted (§15.4). The old lineage then has one last admitted head.
     - **Re-encode.** Re-encode records with the sensitive fields replaced, and map commit identities if product history moves to a new repository; any pseudonym mapping is held privately.
     - **Bind the new genesis.** The replacement's genesis carries a migration record naming the old lineage's last admitted head *hash* (a commitment, not content). Qualify that the replacement derives the same state, effective structure included, up to the renaming.
     - **Retire the old lineage.** Publish an authenticated **retirement statement** for the old ledger id to the old witnesses, naming the successor lineage by hash. It is held by `q_a` of them like a checkpoint, so every read quorum observes it. Evaluators that observe it treat the old lineage as historical only. A stale mirror, an old clone or a restored backup paired with the old witnesses therefore cannot present the purged lineage as current, even though its chain still qualifies cryptographically. Retire participants' high-water marks for the old lineage.
     - **Purge.** Purge the old ledger ref and objects on every controlled replica; this is a destructive history operation and needs explicit operation-specific authorization (G5). Declare old clones and mirrors invalid for SSDS use. Request host garbage collection and backup purge.
     - **Protected `main`.** If the value sits in product history on a protected `main`, SSDP 6.6 forbids discarding `main`'s reachable history. Confidentiality then requires a new repository, with the old one archived or access-restricted, never an in-place rewrite. Effective structure is ledger-derived, so moving product history does not move governance structure. The new repository's declarations are compared with the re-encoded `Σ` like any observed tree.
     - **Publish last.** Per FF-001, the replacement lineage is not published until it validates.
5. **Disclose what yields**, in the incident record:
   - append-only continuity: the old lineage is abandoned or purged;
   - reproducibility of the affected records: only their hashes, and the private mapping, survive;
   - checkpoint continuity: the replacement lineage starts new checkpoints; old checkpoints and the retirement statement remain only as commitments (witnesses never held content);
   - confidentiality of copies outside controlled replicas: it cannot be guaranteed.

A new logical lineage alone never removes leaked data, and SSDS never claims it does.

### 15.6 Actors and authentication

Agents are not principals with authority. Their records are proposals attributed to an execution identity (harness, route, model, task, attempt) observed by the Dispatcher, and bound to the issued task envelope that the Dispatcher's issue key signs (§7.5). Issue keys are trust roots of the same kind as Admission keys. A compromised issue key or harness adapter can forge bindings and lineage; that is outside the declared trust model and its remedy is key rotation through the human-gated lifecycle record. Admission keys are per host, so every entry names the host that appended it and therefore its publisher (§15.3). Humans are authenticated through a trust mechanism declared in genesis and changeable only by a human-gated lifecycle record — for example signed records with registered keys, or an explicitly declared single-user local trust. Admission keys are trust roots of the same kind. No guarantee beyond the implemented mechanism is claimed.

### 15.7 Protected surfaces and untrusted input

Agents cannot modify the ledger, rules registry, project policy, schemas, trust roots, witness configuration, unit governance state or issued task envelopes. The rules registry and policy include the workflow role templates, check templates and their force, the report routing table, escalation floors, decision-class assignments and the contract schema (§7.5-§7.9); no agent role can edit them, and plan units lie outside every agent role's write scope except that of the plan's principal (§7.5). Agents may propose structural declarations in the unit manifest as ordinary content; those take effect only through Admission (§6.8 step 4). Changes to rules, policy, schemas, trust roots and witnesses are their own governed changes requiring a human gate. Admission detects any touch of a protected surface. Agent branches and result envelopes are untrusted until validated. Malformed or adversarial records cannot inject actions, and agent-reported test results are never admissible evidence (§10). Unknown executable or binary content is classified statically and never executed or deserialized to classify it. Paths are repository-contained. Evidence, memory and external text are data. Inspection and export views over realized records, and tension or disposition homes that non-owners can write, are data-exposure and trust boundaries (7.2.1 security owner): views give the strongest safe aggregate and state the limitation, and content written to such a home stays a claim by its native asserter.

## 16. Components and ownership

### 16.1 Components

| Component | Owns | Never does |
|---|---|---|
| Content Model | parsing observed declarations (manifest, anchors, semantic declarations), resolving effective scopes against observed bytes, authored relation extraction, revisions and scope identities | store status; decide which structure is effective |
| Analyzers | derived relations and their incompleteness/completeness declarations | claim completeness they do not have |
| Ledger Store | ledger persistence, authentication and hash-chain verification, currentness qualification (read quorum, read repair, high-water marks, `FORK`/`ROLLBACK`/`BEHIND`/`UNQUALIFIED`), the non-admission bound for abandoned checkpoints, replica restore | interpret records; present a provisional or unqualified head as current; decide what was lost |
| Derivation Engine | the four strata and every query over them, including the effective-structure fold, quarantine, tenure, well-formedness, expected integration head and publication classification in S0, and loss-boundary continuity in S1 (§6.6); in S3, conformance classification, report routing, escalation and coordination obligations, decision classes and amendment classes (§7.5-§7.10) | write canonical state; choose which prefix is current; read the live integration ref |
| Admission | validation (including structural deltas and adoption), the integration-head observation before every append and publication reconciliation, the only ledger appends (including human-gated recovery records), admission by witness quorum (checkpoint distribution), canonical publication effects (integration ref) by the entry's single publisher, fencing absorptions and fence commits (§15.3), and enforcement of task binding, role, write scope, lineage-based independence and conformance (§6.8 steps 3 and 7) | judge semantics, including what a lost interval contained; perform agent work; publish or report before admission |
| Dispatcher | scheduling among obligations ready at the qualified head (resource/account/model feasibility, route selection, reservations), workspaces, harness adapters, execution effects including trusted-runner evidence and conformance check executions, issue of signed task envelopes, task launch in fresh harness sessions with per-task submission credentials and signed launch attestations (§7.5), task suspension and resumption, mechanical iteration retry, integration requests (§7.8), operator journal | decide readiness, conformance or completion; choose a decision class; act as a second admission; move canonical refs; dispatch from a provisional head |
| Interface | logical operations, transports, version-bound rendering of task, review, decision and gate briefs and of the inspector view and digest (§9.2, §9.6-§9.8), advisory `ask(verify)` | hold state of its own |

Dependency direction: Content Model and Analyzers <- Derivation <- {Admission, Interface, Dispatcher}; Ledger Store is read by Derivation and written only by Admission. Ledger Store qualification is consulted by Admission, Interface and Dispatcher before anything is presented as current; Derivation itself never consults witnesses. No component was added for the three revision-3 separations: effective structure and well-formedness are S0 derivation, quarantine is S0/S3 derivation plus an intake judgment, and quorum admission is Admission's existing checkpoint effect plus Ledger Store's existing verification. None was added in revision 4 either: publication reconciliation is a field of Admission's existing append plus an S0 classification, and the loss boundary is a lifecycle record Admission already appended, given S1 semantics, plus one human-gated challenge-tier judgment kind. None was added in revision 5: roles, contracts, routing and escalation are policy parameters, plan content and S3 derivation; conformance is an S3 classification whose expensive inputs are Dispatcher executions recorded as observations; enforcement is two existing Admission steps (§27.5). Revision 6 adds a trust root (the Dispatcher issue key) and a signed envelope that records carry; it adds no component (§27.7). The Dispatcher submits trusted-runner realizations and execution outcomes through Admission. Scheduling decisions never influence derived workflow state. The route, harness, model and attempt provenance they produce travels in submitted records and is replayed as recorded fact, never recomputed against current resources.

### 16.2 Transfer of frozen Orchestrator Architecture 1.6.0

Architecture 1.6.0 (`orchestrator/docs/architecture.md`, frozen) is superseded **for SSDS-governed scopes only**, and only when the accepted Architecture Manual performs the supersession explicitly. It is not layered beneath SSDS. For version-bound older work, the implemented Level 0 Core keeps its accepted behavior (PC-001): one composition root, version/profile-separated source resolution, frozen historical profiles, versioned JSON records, no cross-version source substitution. SSDS does not make Core's standalone acceptance depend on SSDS. The Tracker, Adapter and Scheduler levels were never implemented, so no Level 1-3 data needs migration.

Classification: **Preserved** (binding on SSDS with unchanged meaning); **Replaced** (by the named mechanism, equal or stronger); **Retired** (with rationale); **Deferred** (to the Architecture Manual with the stated closure requirement).

| # | 1.6.0 product invariant | Disposition |
|---|---|---|
| 1 | Progressive usefulness; Core alone complete | **Replaced** for native scopes by staged usefulness: read-only derivation and interface are useful without Admission (§23); document-only operation is not complete for native scopes (§24). **Preserved** for version-bound older work through Core prompt mode |
| 2 | `core <- tracker <- adapters <- scheduler`, no reverse/lateral dependencies | **Retired** (the four-level ladder) with the ladder itself; **Replaced** by the acyclic SSDS component dependency order (§16.1). f9d9de8 wrongly listed this as preserved |
| 3 | Graceful degradation without silent policy bypass | **Replaced**: degradation is truthful non-closure plus read-only derivation, labeled `UNQUALIFIED` or historical when currentness cannot be established (§15.4, §24); the no-silent-bypass clause is **Preserved** |
| 4 | One CLI and one composition root; extensions via versioned SPIs | **Preserved** as a principle (one composition root per installation); **Deferred**: the Manual decides whether SSDS reuses the `sdp` CLI/Core root or defines a successor, and must not produce two roots for one installation |
| 5 | Versioned public boundaries (`api.vN`/`spi.vN`) | **Preserved** |
| 6 | No duplicated workflow authority; Tracker is evidence | **Replaced**: ledger + Admission is the single workflow authority for native scopes; workplans and profiles stop owning transitions there and keep them for `LEGACY(p)` |
| 7 | Manual operation is first-class | **Replaced** in part: manual agent invocation and the Git-envelope route stay first-class (§9.5), and manual results enter by admission; manual document control is not complete for native scopes |
| 8 | Capability recommendation precedes resource scheduling (Adapter/Scheduler split) | **Retired** as a module boundary; both functions consolidate in the Dispatcher. **Preserved** substance: recommendation evidence never acts as quota/resource authority |
| 9 | Benchmark observations preserve context | **Preserved** for Dispatcher route recommendation; **Deferred**: exact fields to the Manual. Never derived workflow state |
| 10 | Scheduler subordinate to workflow intent | **Preserved and strengthened**: the Dispatcher acts only on derived-ready obligations and cannot affect derived state |
| 11 | Private state outside project repositories | **Replaced** in part: operator state stays private; the closed-schema ledger lives in a Git repository designated at genesis, which may be private (§15) |
| 12 | Subset acceptance is permanent | **Preserved** for Core (SSDS never makes Core acceptance depend on it); **Retired** as a ladder rule for SSDS components, which are accepted as one system (§25) |
| 13 | Stable IDs cross modules, implementation objects do not | **Preserved** across SSDS components |
| 14 | Read-only query and durable mutation are visibly distinct | **Preserved**: `ask`/`read` and Derivation are pure; Admission alone mutates canonical state |
| 15 | Long-running execution is explicit (admit, start, events, control, cancel, result) | **Preserved** as the Dispatcher harness-adapter contract; **Deferred**: lifecycle detail to the Manual |
| 16 | Manual and direct routes share one route vocabulary | **Preserved** (§9.5) |
| 17 | Capability identity independent of API version | **Preserved**; **Deferred**: capability keys for transports/adapters to the Manual |
| 18 | Explicit route choice is not a resource-admission bypass | **Preserved** in the Dispatcher ("resource admission" there is distinct from SSDS Admission) |
| 19 | Route admission precedes final prompt rendering | **Preserved**: the Dispatcher selects the route before route-specific brief rendering (privacy exposure differs by route) |
| 20 | Run identity precedes scheduling and rendering | **Preserved**: task and attempt identity precede dispatch and travel in submitted records |
| 21 | Manual result tracking has a structured seam | **Replaced and strengthened** by the typed admission request (§6.8) |
| 22 | Protocol version binding is explicit | **Preserved** (S7, B1, §24) |
| 23 | One mutating run owns one local worktree | **Preserved** (K2) |
| 24 | Workflow routing authority is profile-owned | **Replaced** by the rules registry for native scopes; profiles remain for version-bound rendering |
| 25 | Uncertain routing remains uncertain | **Preserved**: ambiguity and unknown outcomes surface as explicit S3 states or fail closed (C5); no guessed transition |
| 26 | Orchestrator code contained under `orchestrator/` | **Preserved** as the default; **Deferred**: the Manual may change containment only by explicit supersession declaring one SSDS containment root. f9d9de8 listed this as unconditionally preserved |

| 1.6.0 frozen surface | Disposition |
|---|---|
| §3 capability ladder and distributions | **Retired** for SSDS scopes; Level 0 Core **Preserved** for version-bound work |
| §5 public API standard (compatibility, records, pagination, problems/errors, idempotency, sync/async, two-stage freeze) | **Deferred**: the Manual adopts or explicitly supersedes each sub-rule for the Interface and component boundaries |
| §6 Core composition SPI | **Preserved** for Core; **Deferred** with invariant 4 |
| §7 Core shared records (IDs, DigestRef, ProtocolProfileRef, WorkplanRef, CandidateRef, ProjectDescriptor, EventEnvelope, StageResultEnvelope) | **Preserved** for Core; **Deferred**: the Manual maps CandidateRef/StageResultEnvelope onto the admission request, or explicitly declines reuse |
| §8 Core/Prompt module | **Preserved** for version-bound work |
| §9 Tracker; §10 Adapters; §11 Scheduler | **Retired** as modules (never implemented); their functions are replaced by Ledger/Derivation (Tracker history/projection) and the Dispatcher (routes, execution, benchmarks, metering, reservations, prediction, failover), with detail **Deferred** to the Manual |
| §12 configuration ownership; secrets as references | **Preserved** principle (one config owner; secrets never in snapshots/history); **Deferred**: SSDS configuration layout |
| §13 persistence/event ownership | **Replaced** by §15 stores; "persisted state is not repository authority" is **Retired** for native scopes, where the ledger is authority |
| §15 failure/degradation | **Replaced** by §13 and §24 |
| §16 security/privacy (untrusted pasted output, no tokens in prompts/caches/repositories, no local paths or telemetry in web context, no transcript auto-injection, restrictive permissions) | **Preserved** (§15.5-§15.7) |
| §17 benchmark integrity | **Preserved** for Dispatcher recommendation |
| §18 executable architecture fitness | **Deferred**: the Manual defines static dependency-direction checks for SSDS components |
| §19-§20 module acceptance ladder and module-workplan derivation | **Retired**; **Replaced** by §23 phases and Manual-derived D4 workplans |
| §21 versioning/evolution | **Preserved** principle; SSDS versions are distinct per §24 |
| §22 active simplicity/reopen triggers | **Preserved** where applicable (separate mutable workflow authority, duplicated resolution, hidden preview writes, private objects in public API, process execution outside its owner) |

## 17. Mechanisms deliberately removed

| Removed | Replaced by |
|---|---|
| AuthorityGraph, WorkGraph, CodeGraph, EvidenceGraph as canonical families | units + authored/derived/proposed relations; graphs are views |
| AuthorityEpoch | per-record basis |
| Whole-plan PlanRevision freeze, planning/working phases, global replanning stop | item-level plan revisions, plan acceptance judgments, scoped amendment |
| Freeze frontier as a concept | readiness rule over validity |
| Event-sourced control state and stored lifecycle FSMs | immutable ledger of judgments/observations/admissions; stratified pure derivation |
| WorkGraph node kinds (barrier, router, integration gate, review/qualification gate) | obligations typed by required judgment kind and actor qualification |
| WorkClaims as safety mechanism | optimistic admission; advisory footprints; declared serialization surfaces |
| GraphTransaction, candidate overlay, GraphDelta, DIRTY marking | Git candidate + derivation keyed by content; diffs derived on demand |
| Context Resolver and Semantic Projection Layer as components | derivation queries + interface templates |
| Project Ingestion and Reconciliation Engine (four modes) | intake rules over changes with unknown basis |
| LegacyAggregate | coarse `OPAQUE` subjects; structural refinement; qualified promotion |
| "UNKNOWN_BUT_ACTIVE is invalid" | total coverage with explicit `UNCLASSIFIED` status and restricted use |
| Graph history/diff subsystem | derived diff between two ledger positions |
| Mandatory refactor of D1-D3 into per-node documents | adaptive unit granularity, inline or manifest declaration |
| Seventeen MCP operations | six logical operations, transport-neutral |
| f9d9de8: `Change` as a primitive | typed admission request; identity in the admission record |
| f9d9de8: acceptance carried to refined children by rule | parts route to the unchanged subject; promotion by qualified acceptance |
| f9d9de8: same-repository multi-ref atomicity | single-ref append; reconciled publication |
| f9d9de8: derived `acc(policy)` feeding derivation | ruleset named by adoption record |
| 441cf5c: any relation cycle licensed by a common subject; one composite construct for refinement parents and simultaneous definitions | relation roles and cycle classes; SDG as semantic declaration; cycle legality in Admission and S0 (§6.2) |
| 441cf5c: structural declarations effective on repository presence (including absorbed foreign ones) | effective structure as a fold of admitted changes; quarantine in S0; tenure-scoped acceptance (§6.1, §11) |
| 441cf5c: append as commit point; bounded-lag anchoring mode; optional multi-ref publication in one transaction | provisional append, admission by witness quorum with read/write intersection; publication after admission (§15.3-§15.4) |
| 8a75346: publication resolved as a precondition of the next append, with outcome and live-ref movement as separate observations | `obs` on every entry; the first later entry is the reconciliation; one integration observation replaces both kinds (§15.3) |
| 8a75346: quarantine described as the defense against resurrection after ledger truncation; non-admission inferred from absence of copies | loss boundary with S1 continuity (P5); witness-count non-admission bound (§15.4) |

## 18. Inheritance and capability transfer

### 18.1 Consolidated Protocol 8 plan

Every section of `workplans/archive/SSDP-8.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-CONSOLIDATED.md` is disposed below. That plan itself carried these archived records (`workplans/archive/<id>.md`) as one composition:

1. `SSDP-7.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-MIGRATION`
2. `SSDP-7.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-MIGRATION-REVISION-1-SECOND-REVIEW-CLOSURE`
3. `SSDP-7.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-MIGRATION-REVISION-2-DETERMINISM-AND-RECOVERY-CLOSURE`
4. `SSDP-7.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-MIGRATION-REVISION-3-PROTOCOL-6.2-INHERITANCE-RECONCILIATION`
5. `SSDP-7.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-MIGRATION-REVISION-4-PROTOCOL-6.3-INHERITANCE-RECONCILIATION`
6. `SSDP-7.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-MIGRATION-REVISION-5-PROTOCOL-6.4-INHERITANCE-RECONCILIATION`
7. `SSDP-7.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-MIGRATION-REVISION-6-PROTOCOL-6.5-INHERITANCE-RECONCILIATION`
8. `SSDP-7.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-MIGRATION-REVISION-7-PROTOCOL-6.6-INHERITANCE-AND-D3-REASSESSMENT`
9. `SSDP-8.0-DETERMINISTIC-ORCHESTRATOR-VERSION-REBIND`

Their historical inheritance dispositions (6.2-6.6 reconciled; D3 reopen required; D4 not authorized) remain true and are carried here. "Carried" means binding here with unchanged meaning; "Replaced" means an equal-or-stronger mechanism; "Changed" means a deliberate D3 decision with reason.

| Predecessor | Disposition |
|---|---|
| §1 control plane coordinates and indexes, never reproduces semantics | Carried (§6.3, C7) |
| §2 lossless inheritance of all accepted doctrine incl. 6.2 representation and 6.3 PEM; no mirror registries; inadequacy reopens D3 | Carried (§2, §20) |
| §3.1 deliberate supersession of Architecture 1.6.0; no hidden layer | Carried and made per-invariant (§16.2) |
| §3.2 Protocol 6.6 reassessment input | Carried; this revision is a proposed reassessment, adjudicated only by independent D3 Review (§21) |
| §4 reducer vs Scheduler; scheduling decisions recorded and replayed as facts | Carried and strengthened as Admission/Derivation vs Dispatcher: scheduling cannot affect derived workflow state at all; its provenance is recorded fact (§7.3, §16) |
| §5 planes; §5.4 semantic owner vs control projection, mismatch blocks, classification provenance | Carried and strengthened: authored relations inside content remove one mismatch class; drift detection covers the rest (§6.2, §11) |
| §6 minimal control data; four anti-duplication rules | Carried (§6.3, §12.6) |
| §7 versioned formal schemas, canonical interchange, forward compatibility, fail-closed unknown required semantics | Carried (§6.3, §6.8 step 1), with the schema now closed (§15.5) |
| §8 logical identity vs revision; prefer Git identity; no universal per-claim hash graph without need | Carried; revisions computed from Git content, with scope identity separated (§6.1) |
| §9 typed relations; completeness scoped; absence not independence | Carried and strengthened: relation types carry closed semantic roles and cycle classes; completeness is a boundary judgment in the basis; widening is exact (§6.2, §6.5) |
| §10 evidence formalization without bulk migration | Carried (§10) |
| §11 composed state dimensions | Replaced: S3 derived classifications (§6.6) |
| §12.1 version-bound replay; no silent reinterpretation; explicit migration | Replaced by the derivation property plus never-re-adjudicated admissions (§6.6, §13) |
| §12.2 reducer purity and observation boundary | Carried (§6.6, C3) |
| §12.3 snapshots derived and verified | Carried (§13) |
| §13 seven validation layers; single canonical writer; humans decide meaning, writer serializes | Carried as nine steps (§6.8, §9.4) |
| §14 external effects | Carried (C4, §15.3); intent is the admitted entry, the outcome is recorded by the successor entry's integration observation |
| §15.1 private canonical store by default; in-repository only by explicit D3 adoption resolving concurrency, privacy, history and ownership | **Changed**: Git-replicated ledger adopted with the four conditions resolved (§15.2-§15.5); operator state stays private |
| §15.2 durability and recovery contract (atomic publication boundary, corruption detection, durable flush, backup/restore, identity mapping, compatibility on restore, retention) | Carried and strengthened (§13, §15.3-§15.5): the atomic publication boundary is quorum admission of a durable append; anti-rollback added as quorum-qualified currentness; restore after unrecoverable admitted loss bounded by the continuity boundary (P5) |
| §16 formal action registry | Replaced by the rules registry of fixed predicate templates (§6.6) |
| §17 schema-valid agent outputs; no prose parsing | Carried and strengthened: results are typed slots and machine-produced facts (A6, §7.8); every prose-reading check is `HEURISTIC`, so no control decision parses prose (A7, §7.7) |
| §18.1-18.2 TaskEnvelope / ResultEnvelope | Carried: envelope = obligation + role + contract + basis + brief; result = typed admission request with typed slots (§6.8, §7.6, §7.8, §9) |
| §18.3 candidate identity without self-reference | Carried (§6.8) |
| §18.4 transport artifacts not merged; protected surfaces | Carried (§15.7) |
| §19 agent PASS is not canonical PASS | Carried and strengthened: a clean mechanical conformance view is not PASS either (A7, §7.4, §7.7) |
| §20 human gates, risk override, Serious Challenge preservation | Carried and formalized (§6.6 S1, §9.4, §7.4) |
| §21 deterministic impact; materiality by judgment | Carried and made central (§6.4-§6.7) |
| §22 workplans/skills after cutover; lifecycle metadata non-authoritative | Carried (§12.6) |
| §23 minimal activation and bootstrap locator | Carried (§9.5) |
| §24 one logical protocol, multiple transports; polling first | Carried (§9.5) |
| §25 isolation, atomic publication, stale/duplicate/partial results | Carried and strengthened by basis currency and request identity (§6.8, §8.2, §15.3) |
| §26 security | Carried (§15) |
| §27 failure semantics; no implicit document fallback; manual work is non-canonical until admitted | Carried (§12, §24) |
| §28.1 pre-cutover baseline identities from release state; public fallback and recovery distinct | Carried (§24) |
| §28.2 rollback is version rollback; no dual-current control | Carried (§24) |
| §28.3 cutover quiescence: drain, pin or migrate | Carried, per subject (§12.4) |
| §29 migration phases incl. shadow comparison and difference classification | Replaced by §23, classification carried |
| §30 D3 obligations 1-15 | Carried into §21 |
| §31-§32 failure and semantic/adversarial qualification | Carried into §22 |
| §33 versioning and historical preservation | Carried (§24) |
| §34 acceptance criteria | Carried into §25 |
| §35 non-goals | Carried (§20) |
| §36 final target: semantic artifacts carry meaning; agents investigate and reason; evidence supports or challenges governed claims; schemas communicate bounded control facts; rules validate legal transitions; the orchestrator alone commits workflow state; replay determinism is a control guarantee, not deterministic scientific reasoning | Carried without a new mechanism: meaning stays in content and authored relations (§6.1-§6.2, §20); agents reason and judge, never bookkeep (§1.2, §9); evidence supports or challenges through realizations, assessments and challenges (§10, §6.6 S1); the closed schema carries only control facts (§6.3, §15.5, C7); fixed predicate templates and Admission's validation order decide legal transitions (§6.6, §6.8); Admission is the sole canonical writer (C1, §6.8); C2/C8 make derivation, not reasoning, deterministic, and semantic judgment propagates only once admitted as a typed record (§6.6, §14) |
| §37 version rebind, Protocol 7 inputs and reconciliation contract | Carried and executed: the reconciliation contract is discharged by §0.4 under stakeholder instruction (§0.2) |
| §37.2 known Protocol 7 inputs | Bound at their final 7.2.1 meaning (§19.1) |
| §37.2a known Protocol 7.2 inputs (mandatory activation; event-triggered owner injection; typed delegation schema; mechanical write-scope and persistence-home enforcement; in-loop version routing and self-adoption guard; typed choice-provenance and claim records; exact package-access provenance) | Bound as design inputs with landing points (§19.2); none selects a mechanism by itself |
| §38 handoff state | Replaced by §28 |

### 18.2 befe678 hypothesis capabilities

| Capability | Where preserved |
|---|---|
| Machine-readable D1-D3 relations with layer direction and SCC handling (condensation of legitimate simultaneous definitions only; circular warrant invalid) | §6.2 roles, cycle classes and SDGs |
| Derived code dependencies with explicit blind spots | §6.6 analyzers, §6.2 |
| Evidence applicability metadata | §10 |
| Typed, non-flattened relation classes | §6.2 |
| Reviewed plans; immutable accepted plan content; no retroactive requirements | §7.2 |
| Modular plans with structure separate from runtime state | §7.1, §12.6 |
| Iteration vs attempt vs plan vs authority revision | §7.3, §6.1 |
| Deterministic, explainable, version-bound context with explicit gaps | §9.2-§9.3 |
| Minimum-semantic-burden interface | §1.2, §9 |
| Safe parallelism and integration checks beyond textual merge | §8 |
| Direct writes allowed in isolated workspaces | §6.8, §11 |
| Incremental maintenance equal to full rebuild | §6.6, §22 |
| Structural history and diffs | §6.6 S3 views |
| Repository explainability, artifact trust, classification, dispositions | §6.1 coverage, §11 |
| Progressive migration, scope conservation, coarse boundary edges, uncertainty | §12 |
| Structural split requires no false semantic claims (lost at f9d9de8, reinstated) | §12.2 |
| Discovery bottom-up, authority top-down | §12.3 |
| Mandatory orchestrator after scope-local cutover, legacy envelopes | §12.1, §12.4 |
| Atomic accepted-event publication, integrity, backup/restore, crash recovery | §15.3-§15.4 (quorum admission, successor-entry reconciliation, loss boundary), §13 |
| Private control state and secrets kept out of repository transport | §15.1, §15.5 |

## 19. Protocol 7 inheritance (final at 7.2.1)

Protocol 7 closed at 7.2.1, accepted with conditions on 2026-10-12 (`qualification/ssdp70/STAKEHOLDER-RATIFICATION-2026-10-12-PROTOCOL-7.2.1.md`). The stakeholder concluded the 7.x semantic line there, and stated as direction, not as a plan, that further reliability requires the deterministic machinery of SSDS 8.0+. The exact release identities are resolved from `PROTOCOL-RELEASE-STATE.yaml` (§24). The inputs below bind this design at their final 7.2.1 meaning. Doctrine inputs bind; evidence inputs inform. None selects a mechanism by itself, and each landing point remains open to the fresh independent Review.

### 19.1 Doctrine inputs (accepted 7.2.1 owners; earlier prospective rows resolved)

| Input | Landing point | Resolution |
|---|---|---|
| Gate-evidence adequacy is semantic, not a presence predicate; non-narrative core separable and read first | §9.4, S12 | Final Channel C contract adds consequential-decision disclosure, revision-gate tension assessments and the no-unqualified-closure rule; the gate template obligations are a Manual item (§21 item 10) |
| Realized scientific record and feedback persistence live in existing project artifacts; no universal discovery database | §10, §1.4 | Resolved: the ledger is not a canonical home for findings or tensions. A tension's home is an evidence record or native issue; the ledger references it by identity, and the closed schema (§15.5) forbids narrative content |
| One canonical home per finding; tension binding to authority identity and earlier revisions; native attribution as asserter | §6.3, §10, §11, S13 | Tension search keys (owner/path and heading, anchor or object ID, exact revision, earlier revisions, former names, recorded predecessors) map to unit identity, scope identity and refinement lineage. Mapping them exactly is a Manual item (§21 item 1) |
| Marked product inspectability surfaces accepted only by the product-scope owner | §14, S12 | Resolved: the stakeholder or task authority, at an existing gate. An applicable D1/D2 human gate that considers the surface also accepts it, and technical D3 Review alone never does. A distinct judgment kind with that actor qualification (§21 item 3) |
| Claim-integrity floor on agent assertions | §9 report/submit | unchanged; no architecture-level change |
| Realized-record/observation overlap; `CHALLENGES` inquiry status | §10, §21 items 3 and 11 | new at 7.0; bound |
| Inspection/export surfaces and writable tension homes are trust boundaries | §15.7 | new at 7.0; bound |
| D3 O1 authority content | §1.4 | new at 7.0; met by this workplan |
| Pre-cutover baseline advances to the Protocol 7 recovery and public fallback (distinct) | §24 | Resolved: 7.2.1 |

### 19.2 The 7.2 inputs delegated to deterministic machinery (archived plan §37.2a; 7.2 design §7)

Each input is a duty that 7.x could state only in prose, because prose cannot make an indeterministic executor comply.

| Input | Landing point | Decision (revision 5 at D3, where architecture; then the Manual) |
|---|---|---|
| Mandatory role activation and selection | §7.5 workflow roles, §9.2 brief, §9.5 bootstrap, A4 | **D3:** the obligation kind selects the workflow role; duties are compiled from role × kind × domain × contract flags (§9.2). **Manual:** the compilation tables |
| Event-triggered injection of owner depth at the situations where it matters | §9.2 governing content inline, §9.3 | which observed events (judgment kind, gate, authority revision) add owner text to a brief |
| Typed delegation request and return schema | §7.6 contracts, §7.8 results, §9.1 | **D3:** the delegation request is the work contract; the return is the task result with required typed slots; an empty slot without a typed reason is `INCOMPLETE` (§7.7). **Manual:** slot vocabulary per obligation kind |
| Mechanical write-scope (O3) and persistence-home enforcement | §7.6 write scope, §6.8 steps 3 and 7, §7.7 boundary checks, §15.7 | **D3:** the contract write scope is enforced authorization (E0); an investigator's persistence homes are named in its contract and checked like a write scope. **Manual:** pattern syntax and the analyzers that map diffs to units |
| In-loop version routing and self-adoption guard | §6.6 S0 ruleset in force, §12.1 `LEGACY(p)`, §7.5 envelope, S7 | **D3:** the issued envelope binds the governing version of the task's subject (the ruleset `ρ_n` for `NATIVE`, protocol `p` for `LEGACY(p)`), and the brief renders that version; Admission rejects a record whose declared governing version differs from its envelope's, and no agent record can adopt a version (adoption is a human-gated ruleset or mode record). That is E0. **Manual:** the version fields and their rendering |
| Typed choice-provenance and claim records | §6.3 closed schemas, §7.8 results, §7.7 faithfulness checks | **D3:** facts are machine-produced (A6); remaining claims cite records and are checked (`HARD` faithfulness); choice provenance is an E2 slot. **Manual:** which fields are typed control facts and which stay narrative in native homes |
| Exact package-access provenance | §9.1 `read` recording, §8.4 | whether consumed-package accounting is needed beyond read recording (the 7.1 ledger was retired as more provenance than the decision needed) |

### 19.3 Evidence inputs (7.x qualification study; inform, do not bind)

From `qualification/ssdp70/PROTOCOL-7X-QUALIFICATION-STUDY-EVIDENCE-AND-LESSONS-2026-10-12.md`, as summarized in the ratification record:

- Compliance with language-based duties is probabilistic and model-dependent at every layer: activation, loading further text, answering each owed question. Only text in context acts. Conditional "read the owner when …" instructions hit 37%, and inline structured checklists raised uptake from 28% to 92%. This supports inline governing content (§9.2) and A4.
- Errors run in both directions: more inline duty text produced narration where none was owed. Briefs should carry only the duties that are triggered (A4).
- Detection, claim integrity, unauthorized mutation and version ordering did not respond to protocol text in any arm, 6.6 included. These are the strongest cases for enforcement over instruction (§19.2 rows 4-6). Revisions 5-6 realize unauthorized mutation and version binding at E0 on authenticated task bindings (§7.5, §19.2), claim integrity at E0 for the facts machinery observes and E1 for claims (A6, §7.7), and leave detection at E3 with mechanical survival of whatever is reported (§7.9). They do not claim to make agents notice more, and every realization claim awaits the §22 measurement.
- Measurement: absolute floors measure the model, and paired, calibrated comparisons measure the protocol. The LLM evaluator's unassessable tail set the power of both campaigns. Validate oracles and instruments before runs, and simulate operating characteristics before spending. Frozen rules, custody, blinding and independent review caught real defects. These bind the design of the §22 usability qualification.

## 20. Non-goals

SSDS 8.0 does not:

- convert scientific reasoning or evidence into machine JSON, or encode scientific truth in rules;
- provide a general rule or theorem language;
- require a graph database, network database, hosted service or distributed consensus;
- infer independence outside judged-complete scope;
- transfer acceptance by byte identity, scope arithmetic or widening;
- let agents write canonical state, let derived relations override source, or let D4 behavior create accepted D1-D3 authority;
- treat Git branches, commits or PRs as workflow semantics;
- depend on server-negotiated multi-ref atomicity;
- assert currentness for state that a witness quorum does not hold, claim rollback detection beyond the declared witness model, or claim that lineage migration erases leaked data;
- let repository presence, a foreign push, a restore or a merge change effective structure, ruleset or acceptance;
- reconstruct or guess the content of lost admitted history, or let retained authority cross a known loss without requalification or an accountable attestation;
- license a relation cycle by common subject identity, or let a definition or a condensation warrant a claim;
- require every write to pass through an interface;
- expose machine records as routine agent UX;
- use search as an authority resolver;
- execute unknown artifacts to classify them;
- force all-at-once migration, or stop valid production for incomplete migration;
- allow two current authorities or processes over one subject;
- use migration as a hidden redesign channel;
- keep document-controlled workflow as a dual-current fallback for native scopes;
- add webhooks, brokers or hosted services before polling and local operation prove insufficient;
- add registries, wrappers or fields solely to mirror inherited doctrine (the doctrine-realization map of §7.7 is a Manual design artifact, not a runtime registry);
- treat a clean mechanical conformance view, a passing check or an agent's own claim as discharge of an obligation that a judgment must discharge;
- let a heuristic check, or any check that reads prose, block or pass work;
- let a contract carry executable check code, or an agent role edit check templates, roles, routing or escalation floors;
- let any agent role choose a decision's class, lower a report's materiality below a floor, or discharge human attention;
- make a principal a long-lived process whose memory or conversation is workflow state;
- use a model judgment as a mechanical check (a model's verdict is an R2 judgment, never a `HARD` template);
- provide atomic admission across multiple repositories (§11.4 states the supported cross-repository semantics).

## 21. Architecture Manual closure obligations (before D4)

The SSDS 8 Architecture Manual, independently reviewed and accepted, SHALL decide and document:

1. unit model: manifest and anchor declaration syntax (governance-affecting declarations confined to the manifest), content normalization and boundary-marker rules, scope identity, coverage partition and laminarity rules, single-definer rule; effective-structure fold, declaration keys, resolution of effective scopes against observed bytes (`ABSENT`, uncovered region), governance-affecting vs neutral classification algorithm, `aff(Q)`, governance signature and tenure;
2. relation vocabulary with every type's direction, semantic role, cycle class, permitted classes, layer constraint and completeness eligibility; vocabulary adoption checks; SDG declaration syntax and rules; cycle legality and `well_formed`; boundary-completeness judgment semantics and analyzer completeness declarations;
3. closed record schemas, judgment kinds and tiers (including `IMMATERIALITY`, the decision class and independence of each disposition kind, and which execution attributes each kind of evidence specification fixes as claim-defining), actor qualifications (including product-scope acceptance of a marked surface), outcome vocabularies, the challenge inquiry-status attribute, compatibility contract;
4. basis composition and mode assignment per judgment kind, the mechanical computation of each assessment's evidentiary premises, including the subject-boundary rule (`content` inside the record's subject, `validity` across), consumption classes, equivalence-path composition, the widening chain and closure algorithm;
5. derivation: assessment disagreement (evidentiary premises and `bears` in S0; `ev`, `undisputed`, `disp` and `eff` in S2); strata S0-S3 (including `Σ`, `Q`, `aff`, `τ`, `well_formed`, `ok`, `E` and `pub` in S0, and `cont` in S1), the polarity classification of every record kind, the fixed predicate templates and the adoption-time stratification check, least-fixed-point evaluation, transformation identity and frames with the fixed three-way merge algorithm, prospective structure, the well-formedness/enactment split, basis-entry roles, prospective tenure, the prospective-acceptance rule and each record kind's declared frame (§6.9), fence settlement across fence chains (§15.3), analyzer contract (deterministic vs recorded), derivation checkpoints and recovery-time bounds;
6. Admission validation order including the structural-delta rule (author, realign, carry, adopt), source/destination challenge freeze, dependency well-formedness with re-routed support edges, request identity and idempotency, merge-queue serial order, single-ref append, quorum admission and the single provisional entry; the integration observation `obs`, the entry-shape rule, the equivalent-publication and reachability classification, the reconciliation procedure, exclusive per-entry publication with its write-ahead intent, fencing absorptions and fence commits, late-publication detection, and the operational takeover wait, and its ABA policy;
7. obligation rules, readiness, three-valued discharge, provisional propagation and risk-override scope, iteration/attempt identity;
8. change-plan structure, plan acceptance, scoped amendment policy, plan invariants;
9. serialization policy surfaces, generated-unit handling, joint invariants, residual-risk disclosure;
10. interface operations, query classes, brief and gate templates (gate templates meeting the 7.2.1 Channel C contract; briefs realizing the §19.2 activation, injection and delegation-schema inputs), epistemic labels, read recording, transports, bootstrap locator;
11. evidence realization basis fields for scientific regimes, stochastic replicates, environments and precision; assessment granularity for stochastic specifications (for example ensemble assessment), so that replicate variation does not make disagreement and `IMMATERIALITY` routine and acceptance never depends on the latest single replicate (edit-and-rerun is not a route to a pass); the realized-record/observation boundary; trusted-runner designation and custody for expensive external realizations;
12. intake detection, static classification, dispositions, trust/quarantine, structural quarantine views, adoption and realignment requests, policy for mechanical adoption of governance-neutral deltas;
13. governance modes, legacy and external acceptance import scope, external consultation supersession, reconstruction status, structural refinement, subject promotion, demotion and restoration, carve-out, cutover, quiescence, genesis;
14. ledger storage realization: Git entry format, per-host Admission identity and the monotonic write-ahead publication-attempt record (what makes it intact across concurrent processes, copied or restored operator state and key-preserving host replacement; `ac71fa9` N2), fence-commit format, referenced-object retention, durability (fsync) configuration, ledger location options, authentication scheme and key lifecycle, witness kinds, the witness model `(N, q_a, r, f)` and its deployment classes, checkpoint and retirement-statement formats, read repair, the qualification procedure and its states, fresh-clone procedure, replica and witness-set redesignation, the non-admission bound, `LEDGER_LOSS` contents and re-established global control facts, the recovery procedure, continuity-attestation grammar, actor designation and evidence, confidentiality breach procedure and the closed-schema secret checks, with retention weighed before any irreversible purge (7.2.1 storage owner); operator-state boundary; derived index;
15. actor identity and human authentication trust roots;
16. protected surfaces and SSDS self-governance of rules, schemas, trust roots and witnesses;
17. component boundaries and dependency direction; Dispatcher/Admission separation; executed supersession of Architecture 1.6.0 resolving every **Deferred** row of §16.2;
18. ruleset/schema evolution and SSDS-to-successor migration;
19. versioning: system, schema, ruleset, interface and profile versions kept distinct;
20. external units, external acceptance import and the cross-repository boundary (§11.4);
21. the Manual decisions that §19.1 and §19.2 assign, under the 7.2.1 inheritance bound in §0.4 and the pre-cutover baseline of §24;
22. a minimum-justified-architecture reassessment against the then-current accepted baseline, including whether every primitive in §5, component in §16.1 and persistent surface in §15.1 is still needed;
23. workflow roles: the system role templates, their obligation kinds, record kinds, outcomes and write-scope rules, separation constraints and context-lineage provenance, the limits on policy extension, and the standing-plan designation for obligations outside any plan (§7.5);
24. work contracts: schema, lint rules, minimum verifier coverage per item kind, the closed control-tightening whitelist and its order for every field, task-partition checks, budgets, and the system contracts of obligation kinds that belong to no item (§7.6, §7.9);
25. the check-template library: families, parameters and force, the set-valued aggregation of conformance outcomes, the language analyzers for Python and C++ (diff-to-unit mapping, public interface, test-to-code), mutation-testing configuration and thresholds, unit-annotation conventions, and the qualification thresholds that admit a template as `HARD` (§7.7, §22);
26. reports and escalation: report kinds, reasons and materiality vocabulary, the routing table, escalation floors, the outcome table for coordination decisions, materiality reclassification, and the review, decision and inspector templates, digest and impact ranking (§7.9, §9.6-§9.8);
27. the doctrine-realization map: every duty of the SSDP 7.2.1 role and specialist entrypoints assigned E0-E3 with its mechanism, slot or review route, and a disclosed list of duties that stay E3 (§7.7).

## 22. Qualification program

Qualification binds every claim to the property its method can discriminate (DS-001). Synthetic fixtures and model cases establish mechanical properties only; semantic adequacy (promotion, equivalence, completeness, gate adequacy) needs real-owner cases and independent Review. Material persistence and recovery claims use deterministic failpoints with the production owner executing, per the 6.6 storage and concurrency owners. The publication-reconciliation and known-loss groups below test executable mechanics of the repaired owners; whether those owners are adequate remains for independent semantic Review, and no fixture result can stand in for it. Required, at minimum:

- **Derivation model cases (well-foundedness).**
  - *One input, one state:* property-based generation of admissible ledgers and trees. Derived state is identical across evaluation orders, incremental vs from-scratch evaluation, repeated runs and hosts.
  - *Illegal per-member acceptance:* acceptance judgments on parts are rejected.
  - *Illegal positive recursion:* the f9d9de8 review's four-predicate configuration is rejected at Admission; a fixture-injected ledger evaluates to all-`F` with an integrity obligation, never all-`T`. Mutual validity reliance between subjects in different domains is rejected. An equivalence judgment relying on a consumer of the compared unit is rejected.
  - *Negative/challenge recursion:* a challenge targeting a later record or another challenge is rejected. The chain challenge -> adjudication -> challenge -> adjudication evaluates uniquely. A challenge against a dismissal restores the block, and upholding that challenge keeps it restored permanently (the revision-3 formula re-enabled the dismissal). A challenged risk override or continuity attestation stops being in force, permanently once the challenge is upheld. Demoting, promoting or re-scoping units of a subject with an unresolved blocking challenge (including an overridden one) or a revoked revision is rejected, at the source and at the destination subject.
  - *Counter-challenge (`ffbad17` Blocker A):* a triple revoked by an upheld non-blocking challenge stays `REVOKED` while a blocking counter-challenge against the upholding is open, and after that counter-challenge is dismissed. It becomes un-revoked only when the counter-challenge is upheld. A blocking challenge against that second upholding (a relaxer) restores the revocation while open, and permanently once upheld. Polarity of every record in chains up to depth four is computed syntactically and matches the expected table.
  - *Supersession:* a superseded acceptance stays non-current after its superseder goes stale.
  - *Risk override:* `BLOCKED` becomes `PROVISIONAL`; `P` propagates; discharge outside the override scope stays `OPEN`; no unqualified closure.
  - *Ruleset:* a ruleset whose parameters make a lower stratum read a higher one is rejected at adoption. An unadopted policy edit has no effect. Historical views reproduce under the ruleset in force at their position.
- **Relation-cycle legality (441cf5c Blocker A).** Each case runs at Admission (authored) and as an injected absorbed tree (S0 `well_formed`, S2 `ok`):
  - *Valid simultaneous recursive definition:* parts `a`, `b` of subject `G` with `a USES_DEFINITION b`, `b USES_DEFINITION a`, inside a declared SDG `{a, b}`. Admitted; `G` is accepted once; both are valid through `G`; an edit to either, or removal of the SDG declaration, changes `G`'s revision and invalidates both.
  - *Same-subject circular `DERIVED_FROM`:* `a DERIVED_FROM b`, `b DERIVED_FROM a` inside one subject, with or without an SDG. Rejected; when absorbed, `G` is ill-formed and invalid, even though the S2 support graph is acyclic.
  - *Same-subject circular `DEPENDS_ON`:* the same, for `DEPENDS_ON`. Rejected or ill-formed.
  - *Mixed SCC:* `a USES_DEFINITION b`, `b DERIVED_FROM a` inside an SDG. Rejected: the cycle contains an `ACYCLIC`-class edge.
  - *Unknown future type:* a cycle through a type absent from `ρ_n` (and the same type outside any cycle). Rejected at Admission; ill-formed when absorbed; becomes legal only after a ruleset adoption defines its role and cycle class, and then only per that class.
  - *Undeclared simultaneity:* the valid case without the SDG declaration is rejected; the SDG declaration alone, without acceptance of the new revision, validates nothing.
  - *Nested and sibling groups:* nested SDGs with a cycle spanning inner and outer members are legal; a cycle spanning two sibling SDGs is illegal until an enclosing SDG is declared; overlapping (non-laminar) SDGs are rejected.
  - *Group boundaries:* an SDG whose members have different subjects, or that contains a subject, is rejected; promotion of one SDG member alone is rejected; promotion of all members as one composite whose scope contains the declaration is admissible with acceptance.
  - *Code recursion stays legal:* mutually importing modules and recursive calls (derived `STRUCTURAL`, `NEUTRAL`) are admitted, carry no warrant, and are traversed by widening.
  - *Self-relation:* any self-relation is rejected.
  - *Legitimate intra-subject warrant (8a75346 N1, positive):* subject `G` with parts `a`, `b` and the acyclic authored relation `b DERIVED_FROM a`. `G` is accepted once. A judgment about `b`'s claim is admitted with a `content` entry on `a` and no `validity` entry on `G`; Admission rejects a `validity` entry on `G` from any record about `G`. Editing `a` makes the judgment and `G`'s acceptance non-current; an editorial `EQUIVALENCE` on `a` for the judgment's consumption class restores the judgment without re-review, while `G` still needs acceptance of its new revision. Adding `a DERIVED_FROM b` is an illegal cycle. After `a` is promoted with acceptance, new judgments about `b` use `validity` on `a`, and judgments admitted before keep their `content` entries.
  - *Re-routed support edge:* a demotion that would move an existing record's `validity` endpoint onto the subject whose acceptance consumes that record is rejected by the recomputed acyclicity check.
  - *Condensation carries no warrant:* a claim inside an SDG with no `ACYCLIC`-class warrant leaving the SDG is reported unwarranted by the brief, and the SDG's acceptance remains the only acceptance.
  - *Ruleset reclassification:* a new ruleset that reclassifies an admitted `SIMULTANEOUS` type to `ACYCLIC` makes the affected subjects ill-formed (S2 `F`) without re-adjudicating history; historical views at earlier positions are unchanged.
  - *Vocabulary adoption:* a ruleset declaring a `SIMULTANEOUS` warrant type, an authored `NEUTRAL` type, a type missing an attribute, or a rule naming a `NEUTRAL` type in validity mode, is rejected at adoption.
- **Structural intake and tenure (441cf5c Blocker B).** Each foreign case is a structural-only change (bytes and semantic declarations unchanged, so no revision changes) absorbed from the integration ref, then dispositioned. In every case the foreign tree stays buildable, the quarantined delta is visible beside its effective value, and no S0 input to S2 changes by presence.
  - **Required counterexample.** (1) `A` accepted as subject at `R` (`j_A`, tenure `τ1`). (2) `A` lawfully demoted into part of composite `P` (tenure `τ1` ends). (3) `P` accepted. (4) `P` receives an unresolved blocking challenge. (5) A foreign structural-only change declares `A` a subject again. Expected: `Σ` unchanged, so `subj(A) = P` and validity reliance on `A` is `F` through blocked `P`; `P` is in `aff(Q)` (it contains `A`), so it stays `F` even after its challenge is dismissed, until the delta is dispositioned; `j_A` is not in any `ACC`; adoption of the delta is rejected while `P`'s challenge is unresolved. (6) After the challenge is dismissed, adoption without a new acceptance is rejected; adoption with a qualified prospective acceptance bound to the same admission starts tenure `τ2`, and only that judgment counts. (7) Variant: `P` under risk override instead of open challenge; result stays at most `P`, never `T`. (8) Variant: a later challenge upholding against `A`'s triple `(A, S, R)` revokes it in `τ2` as well.
  - *Part to subject:* quarantined; `aff` invalid; adoption is a promotion with acceptance.
  - *Subject to part:* quarantined; the subject keeps effective status but is invalid while affected (`aff`); adoption ends its tenure.
  - *Composite membership mutation:* moving a unit between composites, into a subject of another governance mode, or into a challenged subject, is quarantined; adoption follows mode-transition and destination-freeze rules.
  - *Partition boundary mutation:* a cross-subject boundary move changes subject bytes and also quarantines the declaration; an intra-subject re-partition is governance-neutral, leaves validity unchanged and may be adopted mechanically where policy permits.
  - *Kind or domain reclassification* of a unit, and *governed-content boundary* (ignore) changes: quarantined and governance-affecting.
  - *Challenge-bearing subject reparenting:* a challenged subject declared a part of an unchallenged composite: quarantined; adoption rejected while the challenge is unresolved; the challenge remains on its triple.
  - *Destination freeze (ordinary Admission):* re-scoping a challenged composite by adding or removing members is rejected.
  - *Restoration after repository rewind or manual conflict resolution:* the integration ref is force-moved to an older commit, or a manual merge resolves manifest conflicts arbitrarily. Old declarations are quarantined; no tenure restarts; no old acceptance revives; realignment by an ordinary change clears the quarantine.
  - *Ledger truncation with newer product:* after `LEDGER_LOSS` drops the admission that demoted `A`, the repository still declares `A` a part, so the difference is quarantined. `j_A` is withheld by the loss boundary in any case; the quarantine is additional, not the defense (known-loss group below).
  - *Lawful demotion then restoration without foreign change:* the restoring request must carry a new acceptance; `j_A` from `τ1` never counts; prior evidence counts only where its bases are current.
  - *Ruleset evolution during quarantine:* adopting a new ruleset leaves `Σ` and `Q` unchanged; the later adoption of the delta is validated under the ruleset then in force.
  - *Overtaken admission:* an `OVERTAKEN` structural admission shows as quarantine against the absorbed tree until the revalidated request publishes.
  - *Deleted manifest:* a foreign deletion of the unit manifest quarantines every declaration; effective scopes still resolve from `Σ`; governance is invalid until realignment; production is unaffected.
- **Determinism and replay.** Independence from wall clock and live external state; checkpoint corruption detected and rebuilt; schema evolution fixtures; historical admissions never re-adjudicated.
- **Currency.** Upstream change makes exactly the reliant records non-current. Re-review without content change backdates descendants that did not see the upstream text. Equivalence judgments scope correctly by consumption class. A falsified completeness judgment invalidates every inference that used it. Drift blocks dependent use.
- **Conservative widening.** The scope chain is deterministic. Boundary completeness at the smallest qualifying scope is used. With no judgment anywhere, the result is the whole tree, flagged `UNBOUNDED`. Adding or editing a member of a judged scope makes the judgment non-current. The closure is independent of traversal order. A widened basis never makes a part valid.
- **Admission and concurrency.**
  - Disjoint bases admit concurrently; intersecting bases revalidate.
  - Write-skew across disjoint files is caught through recorded reliance.
  - A clean Git merge with a semantic conflict is blocked.
  - Stale, duplicate (same request identity), partial and very late results are handled.
  - Unauthorized protected-surface edits and agent-modified envelopes are rejected.
  - A duplicate discharge is rejected.
  - A D4 change that breaks another closure on the merged tree is rejected, while an accepted upstream authority change legitimately reopens dependents.
  - Live-ref movement is absorbed as drift without blocking production.
  - A self-declared equivalence backdates nothing.
  - Concurrent Admission hosts: the compare-and-swap loser revalidates.
- **Admission, publication and crash windows** (deterministic failpoints; production owner executing):
  - *clean synchronous admission:* append, `q_a` acknowledgments, `ADMITTED` response, publication `PUBLISHED`; no answer, dispatch or publication observed between append and admission;
  - crash before the ledger append (nothing happened; request retried idempotently);
  - *crash before admission:* the provisional entry survives locally; restart completes checkpoint distribution; no publication, dispatch or `ADMITTED` response occurred before;
  - *crash after admission:* restart finds `q_a` checkpoints, proceeds to publication;
  - *append survives locally but witness admission fails:* the entry stays `PROVISIONAL`; Admission halts further appends; current answers stay at the previous qualified head; when witnesses return, admission completes; on permanent loss, witness-set redesignation settles the prefix;
  - *admitted, publication pending:* derivation at the admitted head gives `pub = PENDING` and `T_n = tree(C_n)`; the next entry records the outcome (see the reconciliation group below);
  - foreign push between admission and the compare-and-swap (`OVERTAKEN`: absorbed, request revalidated, foreign work never overwritten);
  - force-push of the integration ref in the window (`OVERTAKEN`);
  - integration host unreachable (fail closed for appends that need `obs`; recovery lifecycle entries still possible; production continues);
  - an external squash, rebase or merge-button result with the admitted tree and descending from `B_n` (`PUBLISHED` as an equivalent publication);
  - no configuration publishes a provisional entry (the multi-ref optimization is absent).
- **Publication reconciliation (8a75346 Blocker A).** Deterministic failpoints in the real Admission owner after admission, after the compare-and-swap, after the integration read, after the append and after quorum. The oracle for every case is a **ledger-only replay**: derivation runs with the integration host disconnected and must reproduce the classification and name the entry and `obs` that caused it; a fixture that asserts an outcome label without that replay is insufficient.
  - *Compare-and-swap succeeds, crash before any successor:* before restart, ledger-only derivation gives `PENDING`; after restart the successor carries `obs = C_n` and replay gives `PUBLISHED` from that entry. Variant: the successor is the next ordinary admission, and its validation result and derived S0-S2 state equal those computed at head `n`.
  - *Compare-and-swap loses to a foreign push:* the successor is an absorption; `OVERTAKEN`; a revalidation obligation; `n`'s structural changes quarantined against the absorbed tree; the foreign commit intact.
  - *Successor appended but lacking quorum:* it stays `PROVISIONAL`; no further append; current answers stay at `n` with `pub(n) = PENDING`; restart completes anchoring; if the provisional successor is lost and provably never admitted, a new successor is appended after a fresh read.
  - *Successor admitted, response lost:* resubmission by request identity returns the recorded decision; no second entry.
  - *Restart on another Admission host* without the first host's operator state reaches a replayable ledger and never performs the earlier entry's publication.
  - *Duplicate reconciliation:* two hosts race with different reads; exactly one successor is admitted; the loser's append fails the ledger compare-and-swap; classification follows the winner's `obs`.
  - *Foreign movement after the compare-and-swap:* a foreign descendant of `C_n` gives an absorption with `PUBLISHED`; a force-push that drops `C_n` gives `OVERTAKEN`.
  - *Overtaken under structural quarantine:* `n` carried a structural change and the foreign tree both lacks it and declares a foreign delta; both are quarantined, `aff(Q)` is invalid, and the revalidated request publishes and realigns.
  - *Publication after a human decision (`ac71fa9` Blocker C), deterministic failpoints in the real Admission owner:* publisher H1 writes its intent and pauses immediately before its compare-and-swap; H2 appends a fencing absorption and lands the fence; the human's "keep" decision is admitted after the fence settles; H1 is released. Its compare-and-swap fails, and the product stays at `F_n`. Variants:
    - H1's compare-and-swap is released *before* the fence: the fence fails, `C_n` is observed, and a human decision is inadmissible until that observation is recorded;
    - a human decision submitted while the fence is pending is rejected;
    - a foreign writer returns the ref to exactly `B_n` after the fence, then H1 resumes: `LATE_PUBLICATION` with `CRITICAL` attention (the residual is detected, not prevented);
    - two hosts with intact, different logs, as in revision 7: no non-publisher ever performs `n`'s effect;
    - a restored, copied or shared attempt log is treated as lost.

    - two fence publishers paused in turn: the second fencing absorption classifies the first fence `OVERTAKEN` while the ref still shows `B_n`, and a human decision stays inadmissible until an entry observes the ref away from `B_n` (`730490d` N3).

    Two separate expectations apply (`730490d` N2). *Without* a foreign return of the ref to exactly `B_n`, the human's decision is never reversed by an outstanding effect from `B_n`. *With* such a return, a reversal can occur. That reversal must be detected as `LATE_PUBLICATION` with `CRITICAL` attention; it is a disclosed residual, and no oracle may assert it cannot happen.
  - *Barrier discriminators:* an ordinary admission whose `obs` differs from `E` is rejected; an absorption carrying submitted records is rejected; a fixture-injected ledger containing either is an integrity defect in derivation; an absorption changes no effective structure, ruleset, acceptance or obligation discharge except through `T`.
  - *Recovery entries:* a `LEDGER_LOSS` or witness-set redesignation appended while a publication is pending carries no `obs` and leaves `pub = PENDING`; the next entry carrying `obs` reconciles it.
- **Currentness qualification and recovery** (witness model `(N, q_a, r, f)` with `q_a + r > N + f`, exercised at least with `N = 3, q_a = 2, r = 2, f = 0` and the local-trust instance):
  - *Review's L99/L100 world:* L100 admitted, then every replica rewound to L99 and every high-water mark lost. A fresh clone reaching any read quorum observes the L100 checkpoint and reports `ROLLBACK`; L99 is never presented as current.
  - *Total loss of an unadmitted newest entry:* L100 appended, no checkpoint reached any witness, every copy lost. Qualified head is L99, which is true; L100's request is resubmitted by identity; nothing had depended on L100.
  - *Sub-quorum trace:* L100 reached one witness only, then every copy was lost. Evaluators that see the checkpoint report `FORK` and fail closed until a human-gated record names it abandoned; when the non-admission bound holds, the abandonment creates no boundary and no admitted judgment is lost.
  - *Fresh clone from a valid historical prefix:* `BEHIND`, fetch, re-qualify; if the authoritative replica is also behind, `ROLLBACK`.
  - *Forked repository plus witness disagreement:* conflicting authenticated chains, or witnesses holding checkpoints on conflicting chains: `FORK`, fail closed, human-gated resolution, never auto-merged.
  - *Malicious or accidental rewind* of the authoritative ref, including with a compromised push credential: `ROLLBACK` from any read quorum.
  - *Witness loss below read quorum:* `UNQUALIFIED`; no current assertion; Admission halted; production continues; read repair completes a quorum when enough witnesses return.
  - *Faulty witnesses within the bound:* `f` witnesses rolled back or withholding checkpoints cannot hide an admitted head; with `f + 1`, the declared limit is reached and documented, never silently exceeded.
  - *Restoration from a backup older than the admitted head:* `ROLLBACK`; restore from any replica holding the suffix (no boundary); otherwise human-gated `LEDGER_LOSS` (known-loss group below).
  - Two authenticated chains: `FORK`, fail closed.
  - An unauthenticated entry pushed directly is rejected.
  - Authoritative replica lost: restored from a clone extending the highest observed checkpoint.
  - Content objects missing: `UNAVAILABLE`.
  - Snapshots and derived checkpoints at a provisional position are never served as current; answers always name their qualified head.
  - External consultation of another SSDS ledger qualifies its head; an unqualified or retired external head is never imported.
- **Known admitted-history loss (8a75346 Blocker B).** Real Ledger Store qualification and real Derivation, witness model `N = 3, q_a = 2, r = 2, f = 0` and the local-trust instance. Common trajectory: subject `A` in tenure `τ1` with passing `j_A` at L10; L11 admitted (held by `q_a` witnesses) changes authority state; every copy of L11 and of the newer product objects is lost; ledger **and** product are restored to the same L10 snapshot, so `Q` is empty; a read quorum observes the L11 checkpoint (`ROLLBACK`, never current); a human-gated `LEDGER_LOSS` names `R = L10` and L11 as known admitted; current state is derived afterwards, first without and then with a continuity attestation. Variants for L11's content:
  - *demotion:* L11 demoted `A` into part of `P`. `j_A` is not current; no `ACC` counts it; `A` requalifies only by a fresh acceptance after the boundary (which may cite `j_A` by identity).
  - *demotion then restoration:* L11 demoted `A` and L12 restored it with a new acceptance, both lost. `j_A` and nothing else is in the retained ledger, and it stays withheld.
  - *challenge or revocation:* L11 raised a blocking challenge on, or upheld one against, `(A, S, R)`. `j_A` is not current. A retained pre-loss dismissal of an older challenge on `A` loses force, so that challenge reopens and freezes `A`'s structure until re-adjudicated. Conversely, a retained pre-loss *upholding* (including of a non-blocking challenge) keeps its revocation in force after the boundary.
  - *ruleset change:* L11 adopted a stricter ruleset. The `LEDGER_LOSS` re-establishes the ruleset by human gate; retained acceptances are withheld; requalified acceptances must satisfy the re-established ruleset.
  - *evidence invalidation:* L11 superseded a passing assessment. The retained assessment and realization are withheld; the evidence obligation reopens; a fresh realization or assessment after the boundary discharges it.
  - *external import:* a retained external consultation and import are withheld until re-consulted.
  - *attestation:* an attestation holding everything except `A` makes an unrelated subject's acceptance current and leaves `j_A` withheld; an upheld challenge against the attestation withholds the unrelated acceptance again; a second boundary withholds the first attestation unless its own attestation holds it.
  - *counter-challenge across the boundary:* before the loss, a non-blocking challenge on `(A, S, R)` is upheld; a blocking counter-challenge against that upholding is dismissed (variant: upheld). After the boundary, the triple is `REVOKED` in both variants: the dismissal changes nothing, and the counter-challenge's upholding is a relaxer that the boundary withholds.
  - *escalation across the boundary:* a `CRITICAL` human question and a `MATERIAL` finding are pending at `R`; one was acknowledged by a human, one was reclassified by the principal, both before the boundary. After the boundary, all are open in the inspector view, because the resolving records are withheld and the reports themselves are not.
  - *product newer:* the same trajectory with the product still at L11: the next entry absorbs it, adding drift and quarantine; the authority outcome is identical.
  - *history visible, not current:* derivation of the L10 prefix still shows `j_A` current as a historical view; no current answer does.
  - *requalification set:* S3 lists exactly the permissive records and relaxers in effect at L10 that are now withheld.
  - *version rollback after loss:* a later rollback to `LEGACY(p)` needs a fresh import; neither the pre-loss nor the pre-cutover import revives.
  - *retired lineage:* a `LEDGER_LOSS` on a lineage whose old witnesses hold a retirement statement is rejected.
  - *abandoned chain surfaces later:* never merged; an integrity obligation; usable as evidence for a challenge to the attestation.
  - **Contrast — provisional only:** L11 appended, its checkpoint reached one witness of three, and all three respond (`1 + 0 + 0 < 2`): proved never admitted; a fork resolution abandons it with no boundary; `j_A` stays current; the requalification set is empty. Variant with one witness unreachable (`1 + 1 + 0 = 2`): not proved; only a `LEDGER_LOSS` may abandon it, or the evaluator waits.
  - *witness loss beyond `f`, ledger intact:* redesignation continuing from the intact head creates no boundary and records its assumption; if a high-water mark shows a later head, the redesignation must carry a `LEDGER_LOSS`.
- **Confidentiality.**
  - A credential-like or high-entropy value in a record field is rejected at Admission.
  - A fixture-forced sensitive value runs the incident drill: a provisional entry settled first; rotation recorded; replacement lineage derives the same state, effective structure included, up to renaming; old-lineage retirement statement published, so a stale mirror plus the old witnesses yields only historical views; old-lineage high-water marks retired; yielded guarantees recorded.
  - Restoration of a backup containing the purged lineage presents it as retired, never current.
  - A sensitive value in `main` history is routed to a new repository, never an in-place rewrite.
- **Effects and dispatch.** Crash after intent before start; after start before outcome; scheduler decisions replayed as facts; Dispatcher cannot discharge or ready anything; unavailable network, Git remote or harness; interrupted harness; cancellation.
- **Interface.** Same brief for same basis. Inclusion reasons and epistemic labels are correct. Incompleteness is surfaced, including part-to-subject routing. Candidate items cannot support closure. A zero-context web agent locates its task from the bootstrap. Local and Git-envelope transports give identical admissions for identical submissions. Verbose or alternative prose cannot change outcomes when structured content is identical.
- **Evidence.** Execution change forces rerun; target change forces reassessment; specification survives concretization replacement; stale passing and stale failing evidence inadmissible; unavailable artifact degrades binding health; transport success without complete evidence cannot enter assessment; agent-reported results never discharge evidence obligations; proxy evidence cannot close the real owner.
- **Intake.** Manual edit, untracked generated file, opaque binary (quarantined, never executed), external branch, authority-like document, agent overstep, foreign manifest edit — each through the one route; unclassified and quarantined content excluded from governing context and evidence by S0/S2 facts, not by S3 obligations.
- **Migration and refinement.**
  - A whole repository can start as a single opaque subject.
  - Byte-preserving structural refinement of accepted `P` into parts `A`, `B`: `P`'s revision and validity are unchanged; no acceptance record is created for `A` or `B`; validity reliance on `A` routes to `P`; content reliance on `A` survives an edit to `B`; validity reliance on `A` does not survive it unless a scoped equivalence judgment covers it.
  - **Holistic counterexample (required).** A D2 document `P` states in section `A` "all quantities in Gaussian units unless stated" and gives in section `B` equations without unit annotations. `P` is accepted holistically, and the bytes partition cleanly into `A` and `B`. Expected:
    - after refinement, `B` is a part, not an accepted subject;
    - promotion of `B` by rule, by self-declaration or by widening is rejected;
    - a qualified promotion review either rejects promotion or requires `B USES_DEFINITION A` first;
    - `B`'s promotion basis widens to `A` until completeness is judged.
  - Legacy Case B: a whole-document `LEGACY_ACCEPTANCE` cannot be imported onto a section, and native reliance on a section routes to the document subject.
  - Carve-out cutover: requires promotion plus legacy-owner release; the residual stays valid only while carved-out bytes are unchanged.
  - Coarse relations are redirected only by a new subject revision with acceptance.
  - A version rollback of a cut-over subject to `LEGACY(p)` needs a fresh legacy acceptance import; the pre-cutover import does not revive.
  - Production edits invalidate only intersecting reconstruction.
  - No dual-current mode.
  - Bottom-up proposals never self-accept.
  - Per-subject cutover with drained, pinned or migrated in-flight work.
  - Final disappearance of `OPAQUE`/`UNGOVERNED` material closes migration coverage.
- **Cross-repository.** A pinned external unit never goes stale by external movement; a pin change derives local impact; reliance without external acceptance is provisional; a producer-then-consumer admission sequence leaves visible intermediate states; a consulted external ledger is never written; a later consultation finding the pinned triple no longer accepted supersedes the earlier consultation and makes reliant imports non-current.
- **Semantic and adversarial.** A coherent-D3 D4 defect stays D4. A downstream observation can challenge D3, D2 or D1 and blocks dependent closure. Machinery never auto-resolves scientific ambiguity. A missing required check never becomes PASS. Documents' lifecycle fields enact nothing. Historical reasoning remains reachable. No second authority emerges.
- **Security and privacy.** No secrets or private telemetry in the ledger or repository by default; adversarial records cannot inject actions; human decisions require the declared trust mechanism.
- **Workflow roles and decision classes.** Every role attempts every record kind, outcome and write outside its template: rejected at Admission. *Binding (`ffbad17` Blocker C):* a phase-1 result and a mid-task blocking report are admitted bound to their task and claiming nothing; a blocking report suspends exactly that task; a request with a forged, absent or revoked-key envelope is rejected; a request bound to a discharged obligation or to a non-current contract revision is recorded and routed to revalidation. Replay of the ledger alone reproduces every binding. *Fail-closed independence:* a review bootstrap pasted into the authoring session, a Git-envelope review without a human lineage attestation, and a review whose launch attestation names the author's session each yield a non-independent judgment that discharges no review obligation; an `ATTESTED_FRESH` review from a distinct session does. An implementer edit to a plan unit, a contract, a check template or an evidence specification its contract does not name: `VIOLATION`, never integrated. A review whose provenance continues the author's context, and a plan acceptance by the contract's author: rejected. No agent operation lowers a decision's class; a principal cannot submit acceptance, conformance or human judgments. Two coordination tasks on one plan are never concurrent.
- **Work contracts.** Lint rejects an obligation without a verifier, a `HEURISTIC` primary verifier, a write scope containing a protected surface, a plan unit or an unnamed evidence specification, missing triggered slots and missing minimum coverage. Control-tightening classification on generated diffs over every contract field (`ffbad17` Blocker D): each field moved in its tightening direction stays covered by the existing plan acceptance; each field moved against it, every added or removed obligation, every statement or primary-verifier change, and every field outside the whitelist (including a field injected by a newer schema) is R2. In particular, `scientific` `APPLIES` to `NOT_APPLIES`, a removed escalation trigger, an unfrozen interface and a widened `evidence_specs` are R2. Tightening then loosening is R2 against the accepted revision. A task partition whose obligation sets do not partition the item's, or whose write scopes overlap or leave the item's, is rejected; an accepted partition moves no acceptance and discharges the item only when every part, and any required item-level review, is discharged. An amendment makes running tasks on its item non-current, and their late results are routed to revalidation.
- **Conformance verification (DS-001: mechanics only).** Each `HARD` template is qualified on seeded violations inserted into real trajectories (detection rate) and on clean real trajectories (false-positive rate), against thresholds frozen before the runs; a template that misses either stays `HEURISTIC`. *Signal inertness:* replaying a corpus with every `HEURISTIC` template removed yields identical admission decisions and discharges. *Never sufficient:* a candidate with clean conformance and no current review judgment is never integrated, and no `REVIEW` obligation is discharged by any check. *Disclosure:* the same breach disclosed and undisclosed yields an amendment request and a `DISCREPANCY` respectively, and neither is integrated. *Faithfulness:* fixture results claiming completion with an unmet obligation, or citing a failing realization as passing, yield `DISCREPANCY`. *Test integrity:* deleting, skipping or expected-failure-marking a test, and editing an unnamed acceptance test, yield `VIOLATION`; a weakened assertion yields `SIGNAL` and a mutation-strength shortfall `INCOMPLETE`. *Advisory pre-flight:* `ask(verify)` results never enter discharge. *Determinism:* identical contract, trees and observations give identical conformance on every host.
- **Escalation and inspector flow.** *Persistence (`ffbad17` Blocker B):* after a report's target is amended or edited, after its basis goes stale, and after a loss boundary, its human-attention, coordination and adjudication obligations stay open and are annotated, never closed; a raiser's withdrawal of a floor item leaves human attention open; a principal reclassification moves a non-floor item to the digest without a human discharge record and returns it if challenged and upheld. For every floor kind, every principal operation (decline, resolve locally, merge, downgrade) leaves the human-attention obligation open until an authenticated human judgment; a merged item lists every member. A raiser's `ROUTINE` report targeting a D1 or D2 unit is raised to `MATERIAL`. A downgrade of a non-floor item appears in the digest and an upheld challenge restores it. An authority-defect request cannot be resolved locally. A blocking report suspends exactly the raising task and resumption follows the decision. Inspector ranking is a deterministic function of derived impact. The 7.2.1 delegate floor: a material finding in an E2 slot of a `scientific = APPLIES` task reaches the inspector view through any number of intermediate roles.
- **Prospective-acceptance lifecycle (`fb3e542` Blocker A), through real owners.** Part -> prospective acceptance `j` -> integration (tenure `τ1`, `bind(j)`) -> lawful demotion -> identical restoration with new work. Reusing `j` for the restoration is rejected at the enactment condition, and a fresh, independently qualified acceptance succeeds. Contrasts: a clean rebase of the original work *before* enactment keeps `j` usable; a structural-only promotion and a quarantined-adoption restoration behave the same way; `ACC` never contains `j` for any tenure but `τ1`.
- **Assessment disagreement (`fb3e542` Blocker B; `124b0b7` Blocker A; `97e753f` Blockers A-B; `4c35d92` Blocker A), through real Admission, Derivation, discharge and inspection consumers.** Nothing is seeded resolved. Base case: an admitted passing and an admitted failing assessment for one evidence obligation. Then `valid` is at most `P`, and §7.4 discharge reads the same `ev` value: `OPEN`, or `DISCHARGED_PROVISIONAL` where an in-force risk override or policy permitting provisional continuation applies. The evidence is labelled `disputed`, an adjudication obligation goes to the claim's owner, and for a D1/D2 claim human attention is keyed on the failing assessment's existence. Each of the following must leave the claim qualified:
  - a blocking challenge filed against the failing assessment, with no adjudication; also with a risk override on that challenge;
  - a dismissal of that challenge that is itself under an open blocking challenge;
  - an `IMMATERIALITY` judgment under an open blocking challenge, or under a risk override;
  - an `IMMATERIALITY` judgment whose prerequisite moves while the failing assessment still bears; the same for a superseder whose basis moves;
  - an upheld challenge against the failing assessment, with the upholding under an open blocking counter-challenge (the failing assessment stays `REVOKED`);
  - an equivalence judgment covering an execution change, followed by a passing rerun in the new execution; the claim-side variant with an editorial claim revision, with reassessment order varied;
  - a known loss with both assessments retained, followed by positive-only requalification, or by a continuity attestation holding only positive records;
  - a disposition recorded before a loss boundary and not re-recorded after it;
  - an edit, without equivalence, of a unit that only the failing assessor read; contrast: the same edit to a unit only the passing assessor read makes the passing assessment stale;
  - an implementer iteration, end to end, that touches only a unit the failing frame reviewer read: never integrated unqualified;
  - an `UNBOUNDED` assessment or execution closure with an unrelated admitted change, with reassessment order varied;
  - a failing assessment submitted after a context unit it read moved: admitted, and the claim stays qualified;
  - an oracle, tolerance or specification move with the passing realization reassessed first: qualified until the failing realization is reassessed or judged immaterial;
  - an upheld challenge against a completeness judgment or other non-realization premise of the failing assessment;
  - a reassessment of the failing realization by the claim's author.

  These must remove the qualification: a standing supersession of the failing assessment by its assessor or by the owner, directly or through a chain; an upheld, uncontested challenge against it or against its realization (and only those premises); a standing `IMMATERIALITY` judgment; dismissal of a counter-challenge that had suspended an upholding. An upheld challenge against an `IMMATERIALITY` judgment restores the qualification.

  These must not qualify the claim at all: a failing assessment whose claim revision or named execution content moved with no admitted equivalence; an assessment inadmissible for the specification (another regime, or an environment the specification excludes); ordinary uncontested passing evidence. Replicates that differ only in seed *do* conflict, and so do executions that differ only in an attribute the specification leaves free.

  On every generated ledger, `valid` and §7.4 discharge agree on `ev`. Reversing the ledger order of the assessments, and varying evaluation order, changes nothing.
- **S1 and disagreement predicates, bounded enumeration.** `qualification/ssds80/s1_disagreement_model_check.py` must stay green. No challenge, loss boundary, non-evidentiary premise move or upholding against a completeness premise raises the evidence term; no open counter-challenge and no loss boundary lifts a revocation; a bearing failing assessment with nothing recorded against it keeps the term at most `P`; the term agrees with an oracle written without the predicates under test; and the named `97e753f` and `4c35d92` discriminators give their expected values. It must report failures on those owner-grounded properties, not only on the oracle, under `REV12=1`, `REV11=1` and `REV10=1` (sensitivity). It is a diagnostic transcription of the equations, not a production-owner test (DS-001).
- **Report ingress (`f3608f5` Blocker A), through real Admission.** A `HUMAN_QUESTION` and a material finding are submitted *after* the raising task's item was amended and after a context unit changed. Both are admitted and appear in the inspector view without resubmission. A stale task result that carries a report is routed to revalidation while its report is admitted from the same rejecting entry. A report whose record-mode premise is withheld by a loss boundary is admitted.
- **Candidate frames (`f3608f5` Blocker B; `ac71fa9` Blockers A-B), production path end to end.** The implementer genuinely calls `read(u@r0)` through the interface, so the read is recorded in its basis, and then substantively edits `u` to `r1`. The run goes result -> designated-runner executions -> independent review -> integration while the product ref stays at `r0` until integration, with no seeded current judgments and the read retained. The read is a before-image entry: satisfied in the frame, and a fixed fact after integration. Sibling cases: widened context that contains the edited unit (before-image again); a concurrent change to an external prerequisite (stale context, re-review); a concurrent change to the edited unit (stale before-image, rebase). *Prospective structure:* an effective part `A` becomes a newly accepted subject through the ordinary pipeline. The candidate changes only its role declaration; the reviewer records a prospective acceptance in the frame, where `A` is a subject in prospective tenure; the integration carries no new judgment; promotion and acceptance take effect in that one admission. Before integration, `A` is still a part and quarantined in `D_n`. The same path runs for restoration of a demoted subject and for adoption of a quarantined foreign promotion. Negative cases: a prospective acceptance never counts if its transformation is not integrated, or if a transformation with a different structural delta starts the tenure; a frame whose structural delta violates a challenge freeze does not exist. *Bootstrap (`730490d` Blocker A):* the positive promotion path must start from an effective part with **no** prospective acceptance. The first result is admitted in a frame that exists (the delta is well-formed); trusted executions run; the independent reviewer then records the prospective acceptance in that existing frame; integration enacts both. Integration without the acceptance is rejected. The case runs through real owners, with nothing seeded, for promotion, for restoration, for adoption of a foreign promotion, and for an SDG promoted as one composite. *Identity (`730490d` Blocker B):* the same candidate commit offered by two requests, one adopting a quarantined promotion and one carrying it, yields two transformation identities with different frames. An acceptance in one never counts for the other's promotion. An unrelated clean rebase that preserves the structural delta and the promoted subject's bytes and scope keeps the prospective acceptance; a rebase that changes the structural delta does not. The review is admitted, current in `D_n[X]` and not current in `D_n`. After integration it is current, and the task obligation is discharged. Variants: the head moves a unit the review read (stale, re-review); a rebase leaving `u`'s revision unchanged (review kept); a rebase changing it (re-review); a non-clean merge (new iteration, no frame); a unit changed on both sides that merges cleanly (judged at the merged revision).
- **Iteration and recurrence.** `INCOMPLETE` within budget re-issues mechanically; exhaustion, out-of-scope findings and discrepancies create coordination decisions; repeated template failures and repeated finding families are detected; operational retries spend no budget.
- **Usability.** Live trajectories on real tasks, in shadow mode, showing that agents complete bounded work without reading machine records and with less context than the document-controlled baseline. Claims stay bounded to the trajectories, harnesses and models actually exercised, consistent with the Protocol 6.6 stochastic robustness boundary. Following the 7.x lessons (§19.3), comparisons are paired against the document-controlled 7.2.1 baseline on the same executors and fixtures, gates are calibrated from simulated operating characteristics before any spend, evaluator and oracle instruments are validated first, and rules, custody and blinding are frozen before runs. **Doctrine realization** is measured the same way: the 7.x qualification panel, rerun with SSDS role briefs, contracts, conformance verification and escalation in shadow against the 7.2.1 baseline, for unauthorized mutation, claim integrity, owed-duty presence, narration where none was owed, and survival of material delegated findings to the human. Claims stay bounded to the duties and models exercised, and detection is reported separately, because enforcement is not expected to improve it.
- **Authorization boundaries (`f3608f5` Blocker D).** Not a runtime test. Before each gate, a review of §23-§25 confirms that every criterion of that gate is satisfiable by work the earlier gates authorize, and that no gate can be passed by evidence from fixtures or the existing Core standing in for SSDS owners.
- **Repository acceptance.** The inherited repository workflow (regression, PEM checks, package build/validation, distribution parity, whitespace, frozen-resource integrity, Orchestrator Core snapshot/tests) for every affected surface.

## 23. Development sequence

- **Phase A — Protocol 7 reconsolidation.** Executed 2026-10-12 (§0.4): the exact identities and inputs are bound (§19), the pre-cutover baseline is advanced (§24), and the governing version is adopted by stakeholder instruction. Phase A closes when the Phase B Review passes it.
- **Phase B — independent D3 falsification of this architecture**, including the Phase A reconciliation. Its PASS authorizes nothing by itself (§25).
- **Phase C — SSDS 8 Architecture Manual** resolving §21, independently reviewed, with explicit stakeholder acceptance of this major change. Closing Phases B and C is gate G1; the shadow D4 workplan and the stakeholder's authorization of shadow implementation are gate G2, which opens Phases D-H (§25).
- **Phase D — read-only kernel (shadow, no authority).** Content Model, Analyzers, ledger schema and Derivation over this repository, with a shadow genesis from existing history. Value: currency, impact and "what governs" answers with no control change.
- **Phase E — read-only interface and workflow layer in shadow.** `open/ask/read` offered to agents working under the document-controlled baseline; role briefs, contract lint, conformance views, report routing, decision briefs and the inspector view computed beside document control with no authority. Measure burden reduction and doctrine realization by live trajectories on the 7.x panel (§22). This is the earliest point at which the stakeholder's reliability question gets evidence, and it needs neither Admission nor witnesses.
- **Phase F — Admission and Dispatcher in shadow.** Compute admission decisions beside document control. Classify every material difference as an SSDS defect, a baseline ambiguity or defect, a deliberate stronger rule, or an unresolved semantic judgment, and independently review each.
- **Phase G — intake and migration pilot.** This repository's legacy documents (Case B) and one external scientific repository (Case C/D) without disturbing production.
- **Phase H — adversarial and fault qualification** (§22).
- **Phase I — scope-local native cutover** after accepted architecture, implementation acceptance, shadow qualification, independent Review, required human/project approval and demonstrated rollback: gate G3 for the system, then G4 for each subject (§25).

## 24. Cutover, rollback and versioning

- The pre-cutover baseline is the accepted document-controlled protocol resolved from `PROTOCOL-RELEASE-STATE.yaml`: currently Protocol 7.2.1 (resolved 2026-10-12), with recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d` and public fallback `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, kept distinct. It advances only by an explicit inheritance reconciliation. Protocol 6.6 (recovery `384666764da4c55b282e6b1595ab97e2f86e1dc4`, public fallback `22f4bdba53795da3a6f13f162529f3a843fc37ae`) and older versions are historical baselines under `historical` in the release state.
- Older version-bound work stays under its declared version and immutable source; every supported orchestration profile, through `ssdp-protocol-7.2`, stays frozen and independently testable (PC-001); migration never reinterprets old records as authored under SSDS 8.
- Native cutover is per subject; after cutover no document-controlled process governs that subject. Shadow comparison is permitted only while one side is explicitly non-authoritative.
- Orchestrator unavailability yields truthful non-closure for native scopes, never implicit document-control fallback. Exploratory or report-only work may proceed but claims no canonical closure until admitted.
- Rollback is version rollback to the immutable pre-cutover baseline: stop Admission for the affected scope, resume the pinned baseline process there, repair SSDS separately. The mode change ends each affected subject's tenure, so pre-cutover legacy acceptance imports never revive; a fresh import is needed (§12.1). Ledger rollback (§15.4) is an integrity incident, not a version rollback; an unrecoverable admitted loss adds a continuity boundary, which composes with a later version rollback because the mode change ends tenure and the boundary withholds every pre-loss import independently.
- System, schema, ruleset, interface and profile versions are distinct and never conflated with protocol semantic version.

## 25. Acceptance criteria and authorization boundaries

Each criterion is assigned to the earliest boundary at which its evidence can exist. No criterion is dropped, and none requires the implementation it would authorize (`f3608f5` Blocker D: revisions 4-6 required shadow-mode evidence before the D4 handoff that builds the shadow system). Each gate includes every earlier gate.

1. the Protocol 7 inheritance reconciliation (Phase A, §0.4) has passed independent Review;
2. one accepted Architecture Manual resolves every §21 obligation;
3. exactly one canonical writer exists per ledger, and no document, profile, tracker, scheduler, index or derived view can enact a transition;
4. the four primitives and their derived semantics are fully specified, including subjects, scope identity, effective structure, quarantine and tenure, relation roles and cycle legality, the four strata, loss-boundary continuity, currency, validity, three-valued discharge and provisional propagation, with the uniqueness argument of §6.6 independently checked;
5. every §16.2 and §18 inherited guarantee and capability is carried, replaced with equal-or-stronger evidence, retired with accepted reason, or closed by the Manual;
6. concurrency correctness rests on admission-time validation, with residual risk stated;
7. intake is the single route for unknown-provenance change, and migration is coverage refinement plus qualified promotion with per-subject cutover;
8. persistence, quorum admission and currentness qualification, publication and its successor-entry reconciliation, known-loss recovery, confidentiality recovery and evolution are specified, survive loss of any one machine, assert currentness only for quorum-witnessed state, and never let retained authority cross a recorded loss without requalification or accountable attestation;
9. the agent interface meets the minimum-semantic-burden invariant, demonstrated by live trajectories in shadow mode;
10. the workflow execution and verification layer (§7.5-§7.10, §9.6-§9.8) is specified by the Manual; every `HARD` template is qualified; signal inertness, never-sufficient verification and non-droppable escalation are demonstrated; and doctrine realization on the 7.x panel is reported against the 7.2.1 baseline, with its limits stated;
11. independent D3 Review/Challenge finds no blocker or active governing Serious Challenge;
12. stakeholder acceptance of this major architectural change is explicit;
13. a D3->D4 workplan for the shadow phases, derived from the accepted Manual and independently reviewed, bounds its scope to shadow operation: no SSDS authority over any subject, no cutover, and the document-controlled baseline keeps governing (§24);
14. the stakeholder explicitly authorizes that shadow implementation;
15. an independent implementation Review of the shadow components passes, with the §22 groups executed against the production owners, not fixtures alone (DS-001);
16. for each subject, the cutover conditions of §12.4, demonstrated rollback (§24) and the required human and project approval hold.

| Gate | Effect | Criteria |
|---|---|---|
| **G1** architecture accepted | closes Phases B and C | 1-8, 11, 12 (criterion 2 includes the workflow-layer Manual items 23-27) |
| **G2** shadow D4 authorized | opens Phases D-H, shadow only | G1, 13, 14 |
| **G3** implementation functionally accepted | closes Phases D-H | G2, 9, 10, 15 |
| **G4** native cutover of a subject | Phase I, one subject at a time | G3, 16 |

A Phase B PASS satisfies criterion 11 only and authorizes nothing. No D4 work of any kind is authorized before G2, and SSDS holds no authority over any subject before G4 for that subject.

## 26. Reopen triggers and open uncertainties

Reopen this architecture if:

- conservative widening makes too much work non-current to be useful on real repositories;
- part-to-subject routing makes validity locality too coarse and promotion judgments too frequent to sustain;
- read recording proves infeasible across target harnesses, so bases are systematically too weak;
- unit declaration cost outweighs locality benefit at practical granularity;
- Git-hosted ledgers cannot meet single-ref compare-and-swap, durability, privacy, scale or hosting constraints;
- no practical independent witness set satisfying `q_a + r > N + f` exists for the target deployment class, or witness admission latency on the Admission critical path proves unacceptable;
- structural quarantine produces so much governance invalidity on real repositories (frequent manifest edits, restores, merges) that intake cost outweighs its protection;
- simultaneous-definition groups prove so frequent or large that subjects become too coarse, or real owners need a sound recursive-warrant exception that the closed vocabulary cannot express;
- the confidentiality breach protocol proves operationally unrealizable;
- requalification after a loss boundary proves too costly in practice, so that a mechanical narrowing (for example authenticated per-entry scope commitments held outside the ledger's failure domain) becomes worth its ordinary-path and witness-privacy cost, or continuity attestations prove to be used as routine shortcuts rather than accountable exceptions;
- integration-head reconciliation proves unworkable on a target host (for example repeated foreign resets producing ABA contention), or publisher takeovers and fence commits become frequent enough that fencing decisions burden the human routinely;
- the fixed predicate templates cannot express a required project policy without breaking stratification;
- a later accepted protocol version requires the ledger to be a canonical home for findings or tensions (7.2.1 resolves this as reference-only, §19.1);
- an accepted successor protocol version changes doctrine that §19.1 binds, until its own inheritance reconciliation is done;
- live trajectories show agents still doing bookkeeping;
- contract authoring and lint cost more than the verification they buy, or write scopes prove so narrow on real work that amendment requests dominate coordination;
- `HARD` templates block legitimate work often enough on real trajectories that they are routinely amended away, or agents learn to satisfy checks while defeating their purpose;
- coordination becomes a bottleneck (decision obligations backlog behind one principal per plan), or principal decisions are routinely overturned by challenge;
- human-attention volume exceeds what the inspector can sustain, so the escalation floors are too broad, or downgrades are used routinely to hide material findings;
- constructed independence proves illusory in practice (common-mode failures shared by author and reviewer dominate review misses);
- disagreement becomes routine (stochastic specifications assessed per replicate, or equivalence judgments that keep stale failing evidence bearing), or interpretive changes leave so many failing assessments `review-required` that reassessment dominates evidence work, so that dispositions and `IMMATERIALITY` judgments are recorded as a matter of course rather than as accountable resolutions;
- any inherited guarantee proves unpreservable under §6.

Uncertainties that cannot close by design work alone:

- **Formerly Protocol 7 dependent (resolved at 7.2.1, §19.1):** finding and tension canonical home; product-surface acceptance actor; pre-cutover baseline. **Still open, for the Manual:** exact gate-template obligations; the mapping of tension search keys to unit identity; the §19.2 decisions. The Stage F portable execution-profile semantics did not become 7.x doctrine (7.2 replaced them with the consolidated qualification harness); the Dispatcher keeps only its evidence-only lesson that transport success is not evidence admissibility (§9.5, §10).
- **Empirical:** rate of false staleness under conservative widening and part-to-subject routing; frequency and cost of promotion judgments in Case B; analyzer completeness for real Python and C++ scientific code; feasibility of read recording per harness; practical unit granularity; derivation cost and checkpoint sizing on large repositories; ledger growth over years; witness availability and admission latency in practice; frequency of structural quarantine and of SDG declarations; agent context and success compared with the document-controlled baseline; contract authoring cost; detection and false-positive rates of check templates on real Python and C++ scientific code; amendment, escalation and downgrade rates; human-attention load per unit of work; whether doctrine realization on the 7.x panel improves over 7.2.1 on the behaviours that did not respond to text.

## 27. Adequacy and minimum-architecture passes (rounds 2-13)

These passes are design rationale, not evidence of adequacy. The next Review must falsify independently, and nothing here awards a PASS. Round 5 (§27.4-§27.5) covers the revision-5 workflow layer; the `ffbad17` Review falsified parts of it, and round 6 (§27.6-§27.7) records the repairs and governs where the two disagree. The `f3608f5` Review falsified parts of revision 6; round 7 (§27.8-§27.9) records those repairs and governs over round 6 where they disagree. The `ac71fa9` Review falsified the candidate-frame and publication contracts again; round 8 (§27.10-§27.11) records their re-derivation and governs over earlier rounds on those two contracts. Round 9 (§27.12-§27.13) completes the transformation contract after the `730490d` Review and governs on it. Round 10 (§27.14-§27.15) binds prospective acceptances to one enactment and realizes assessment disagreement in S2; it governs on the first. Round 11 (§27.16-§27.17) re-derives assessment disagreement and governs on it. Round 4 (§27.1-§27.2) still governs the rest, except where §27.6, §27.8 and §27.10 repair it (S1 counter-challenges, candidate currency, publication and ABA).

### 27.1 Round 4: fresh out-of-matrix pass against revision 4

This pass was run after the repairs and did not reuse the revision-3 dispositions (§27.3). Each attack tried to obey every local rule while violating a governing invariant; the expected response to a failure is a repaired abstraction at the earliest owner, not a new test.

| Attack | Trajectory attempted | Result (revision 4) |
|---|---|---|
| Publication outcome never recorded | admitted `n`; compare-and-swap succeeds; Admission dies and no request arrives for weeks | Holds: canonical `pub(n) = PENDING` is truthful (`T_n` is already the governed tree); the next entry of any kind, from any host, records it from its `obs` (§15.3) |
| Foreign force-push right after publication | compare-and-swap succeeds; a force-push drops `C_n` before the next read | Holds: the successor must be an absorption; `C_n` unreachable, so `OVERTAKEN`; revalidation obligation; foreign work intact |
| `OVERTAKEN` absorption under structural quarantine | `n` adopts a structural delta; the foreign tree lacks it and adds another | Holds: both deltas are in `Q`; `aff(Q)` is invalid in S2; the revalidated request realigns; no structure takes effect by presence |
| Two Admission hosts recovering one publication | both read, both compare-and-swap, both append | Holds: the publication compare-and-swap is idempotent; the ledger compare-and-swap admits one successor; the loser re-derives |
| Duplicate observation or reconciliation | a second observation entry for `n`; a replayed request identity | Holds: only the first later entry carrying `obs` classifies `n`; request identity returns the recorded decision |
| Reconciliation hidden in a privileged path | an absorption that also carries a judgment or discharge | Holds: rejected by Admission; an integrity defect if injected |
| Reconciliation depending on ambient Git state | replay with the integration host unreachable or since moved | Holds: classification reads only `B_n`, `C_n`, `obs` and immutable commits the ledger keeps reachable |
| ABA on the integration ref | foreign reset to exactly `B_n` after a successful compare-and-swap | Holds within a disclosed limit: indistinguishable from the ref alone; both permitted choices are recorded and replayable; no foreign content is lost |
| Admitted suffix lost, product newer | ledger restored to L10, product still at L15 | Holds: `ROLLBACK`, then `LEDGER_LOSS` boundary; the next entry absorbs the newer product |
| **Admitted suffix lost, product equally stale** (the 8a75346 trajectory) | both stores restored to L10; `Q` empty | **Repaired**: the boundary is a ledger fact; `cont` withholds `j_A` and every other permissive pre-loss effect (§15.4) |
| Lost challenge, revocation or ruleset adoption | the lost interval held them | Holds: support withheld; retained relaxers lose force; `LEDGER_LOSS` re-establishes the ruleset, trust roots and witness model |
| Stale backup, then witness redesignation | redesignation used to step over a later witnessed head | Holds: a redesignation that abandons a head not proved never-admitted is a `LEDGER_LOSS` |
| Resurrection through boundary and tenure interplay | after the loss, demote and restore `A` with the same bytes; or reuse `j_A` in an unchanged tenure | Holds: tenure restarts on restoration, and `cont` withholds `j_A` within the unchanged tenure; either lock suffices |
| Loss then version rollback | rollback to `LEGACY(p)` after a loss | Holds: the mode change ends tenure and the boundary withholds every pre-loss import |
| Redesignation over a provisional entry | old quorum lost while `n+1` is provisional | Holds: the redesignation settles `n+1` through the hash chain; if `n+1` publishes, its outcome is recorded by the next entry carrying `obs` |
| Witnesses lost beyond `f`, ledger intact | more than `f` witnesses lost; every replica agrees | Holds within a disclosed limit: redesignation continues from the intact head, recording the assumption; any evidence of a later head forces `LEDGER_LOSS` |
| Ledger objects lost, witness hashes intact | witnesses hold L11's checkpoint, no replica holds L11 | Holds: known admitted; `LEDGER_LOSS` names it; boundary |
| Never-admitted entry abandoned as if admitted, or the reverse | label a possibly admitted entry provisional to skip requalification | Holds: the non-admission bound decides; an inconclusive bound cannot be abandoned without a boundary |
| Abandoning a recoverable suffix to escape a challenge | recovery authority abandons a reachable chain, then attests broadly | Holds within a disclosed limit: the surfaced chain is evidence and an integrity obligation, and the attestation is challengeable; recovery authority is trusted (T4) |
| Attestation laundering | attest a subject unaffected that the lost interval revoked | Holds within a disclosed limit: accountable, evidence-citing, challengeable; an upheld challenge withdraws it permanently |
| **Upheld challenge re-enabling a relaxer** (found in this pass) | uphold a challenge against a dismissal; the challenge closes | **Repaired**: `in_force` excludes upheld challenges (§6.6 S1) |
| Intra-subject acyclic warrant | `b DERIVED_FROM a` inside `G`; judgment about `b` | Holds: `content` entry on `a`; no self-validity; staleness and early cutoff as required (§6.4) |
| **Support edge re-routed by structure** (found in this pass) | demote a subject whose `validity` reliance then points at its own consumer | **Repaired**: step 5 recomputes re-routed edges (§6.8) |
| Cross-subject warrant cycle | `x1 CONCRETIZES y1`, `y2 CONSTRAINED_BY x2` with validity both ways | Holds: support cycle rejected; least fixed point `F` if injected |
| Legitimate simultaneous definition | mutually recursive equations in an SDG | Holds: legal; no warrant inferred |
| Same-subject circular warrant | `a DERIVED_FROM b`, `b DERIVED_FROM a` in one subject | Holds: illegal cycle at Admission and in S0 |
| Challenge escape by re-scoping | source or destination re-scoping under challenge, including after a loss reopens a dismissed challenge | Holds: the freeze applies to every affected subject |
| Governance-neutral repartition under challenge | foreign leaf repartition inside a challenged subject | Holds: revision unchanged, so the challenge still binds; mechanical adoption changes membership and is frozen until resolved |
| Deleted manifest and inline anchors | delete the manifest; keep anchors | Holds: everything quarantined; effective scopes resolve from `Σ`; anchors declare nothing |
| Widening with incomplete knowledge | no completeness judgment anywhere in the chain | Holds: whole-tree `UNBOUNDED` fallback |
| Stale evidence after role, tenure or boundary change | reuse a pre-loss realization for a fresh assessment | Holds: the realization is withheld; a fresh realization, or an attestation, is needed |
| Ruleset or vocabulary change during quarantine | adopt a ruleset while deltas are quarantined | Holds: `Σ` and `Q` unchanged; adoption validated under the then-current ruleset |
| Historical profile isolation after recovery | `LEDGER_LOSS`, then schema evolution, then a historical view | Holds: earlier prefixes derive unchanged; `LEGACY(p)` interpreted by `p` |
| Legacy and native dual authority | cutover lost in the abandoned interval | Holds: one mode in `Σ`; the retained import is withheld until requalified |
| External authority stale, forked or retired | consultation before a loss; external retraction afterwards | Holds: withheld by the boundary and superseded by adverse consultations |
| Confidentiality retirement, then stale backup | restore the purged lineage; or try `LEDGER_LOSS` on it | Holds: retired lineage is historical only; `LEDGER_LOSS` on it is rejected |
| Agent output treated as authority | agent PASS, `PROVISIONAL` response, self-declared SDG, equivalence or completeness, a self-supplied `obs`, an agent attestation | Holds: proposals only; `obs` is Admission's own read; attestations are human-gated |

**Failing trajectories in this round.** Four, all found before this revision was committed and repaired at their owners: the two 8a75346 blockers, the S1 upholding defect and the re-routed support edge. A fifth defect class was textual: revision 3's "survives nowhere, never admitted" and its description of quarantine as the truncation defense; both are corrected (§13, §15.4). No trajectory in the table fails against revision 4.

**Residuals carried**, because no architecture removes them: undeclared semantic dependencies (§8.4); circular reasoning stated only in prose (§6.2); foreign edits that reduce governance validity, but never production, until dispositioned (§11.3); the information-theoretic limits of §15.4 (an entry, or an admitted head, whose every copy, checkpoint and high-water mark is gone); continuity beyond the fault model resting on recorded assumptions; the correctness of continuity attestations, which are accountable but not infallible; trust in recovery authority; and Git ABA on the integration ref.

### 27.2 Minimum-justified-architecture pass (round 4)

The question for revision 4 was whether publication reconciliation or known-loss recovery needs a new primitive, record category, persistent surface, component, state machine or identifier.

- **Primitives:** four, unchanged. Reconciliation is a field of a record; the boundary is a record's position.
- **Record categories:** five, unchanged. One challenge-tier judgment kind is added (continuity attestation), because narrowing a loss is an accountable judgment that must be challengeable, and that is exactly what the challenge tier's relaxers are. Two observation kinds (publication outcome, live-ref movement) are removed in favour of the `obs` field, so the kind count does not grow.
- **Persistent surfaces:** six, unchanged. Admission's publication-attempt log lives in existing operator state, is optional and is never canonical.
- **Components:** seven, unchanged (§16.1).
- **State machines:** publication keeps three derived states; there is no reconciliation phase. The boundary is an S1 predicate, not a state machine.
- **Identifiers:** none added. The boundary is the `LEDGER_LOSS` position.
- **Ordinary-path cost:** one integration read per append, which setting `B` already required; no extra entry or quorum round for publication; `cont` is identically `T` and the requalification set empty when no loss exists.
- **Quorum-currentness proof:** unchanged. Every entry, including `LEDGER_LOSS` and reconciliation entries, is single-ref appended and admitted by `q_a` witnesses; `|Q_a ∩ R| ≥ q_a + r − N > f` still gives an honest intersecting witness; a `LEDGER_LOSS` that re-establishes the witness model is checked against the inequality like genesis and redesignation.
- **Composition:** the boundary is orthogonal to tenure (§12.1), to challenges (relaxers are withheld, restrictive records kept), to rulesets (re-established at the gate; historical views unchanged), to evidence (realizations and assessments withheld), to migration and version rollback (mode change and boundary are independent locks), and to quarantine (additional when the product is newer).
- **Capability transfer:** §16.2 and §18 rechecked; §18.1 now rows archived §36 and §38; no capability is lost, and §14 external effects and §15.2 durability are strengthened.
- **Removed or demoted in revision 4:** the "resolve before the next append" precondition; separate publication-outcome and live-ref-movement observations; quarantine as a loss defense; non-admission inferred from absence of copies.
- **Rejected additions** (carried from earlier rounds, then new):
  - a general rule language;
  - a separate refinement or reinstatement judgment kind;
  - a merge-and-publish reconciliation path;
  - a cross-repository coordinator;
  - a stored copy of effective structure;
  - automatic, non-human-gated abandonment of sub-quorum checkpoints (its safety would depend on witness counts that read repair can change);
  - a fifth primitive for simultaneous definition;
  - a dedicated, privileged reconciliation successor while normal admissions are blocked (the Review's hypothesis): an extra entry and quorum round per publishing admission, and a special path, with no gain over the `obs` field;
  - a fourth `RECONCILING` publication state: it would record an operational phase that leaves no canonical trace;
  - publication outcomes kept only in operator state: breaks audit and replay;
  - a recovery epoch or generation identifier: the boundary position already is one;
  - a global tenure restart on loss: covers only acceptance;
  - a new ledger lineage after loss: maximal disruption, same requalification;
  - reusing ruleset generations: a ruleset change never invalidates acceptance, so the semantics differ;
  - authenticated per-entry scope commitments at witnesses as a mechanical narrowing: ordinary-path cost and witness-privacy exposure to optimize a rare catastrophe (a reopen trigger, §26);
  - provisional continuation of withheld authority after a loss: would silently degrade unknown lost negatives to provisional project-wide;
  - automatically applying restrictive records from a surfaced abandoned chain: abandoned chains are evidence, never merged;
  - inferring loss scope from agreement between product and ledger.

### 27.3 Rounds 2-3 record (historical)

The table below is the round 2-3 record as dispositioned against design revision 3. Round 4 (§27.1) re-attacked every family; where the two disagree, §27.1 governs, and superseded cells are marked.

| Attack | Trajectory attempted | Result (revision 3) |
|---|---|---|
| Authority transfer in migration | byte-preserving split, then reliance on a child as accepted | Blocked by subject routing (§6.1, §12.2); qualification counterexample in §22 |
| Same, via legacy import | import a whole-document legacy acceptance onto a section | Blocked: import scope equals accepted scope (§12.1) |
| Same, via carve-out cutover (round 2) | cut a section over to `NATIVE` while its legacy document's holistic acceptance keeps validating the rest | Repaired in round 2 by frozen subject scope and carve-out rules (§12.2, §12.4) |
| Self-supporting acceptance | mutual validity reliance; equivalence relying on a consumer; member-level judgments in a group | Rejected at Admission; least fixed point is `F` if forced (§6.6) |
| **Circular warrant hidden inside one composite** (round 3, Blocker A) | `DERIVED_FROM`/`DEPENDS_ON`/`SUPERSEDES` cycle among parts of one accepted subject; mixed definitional-plus-warrant cycle inside an SDG; cycle through an unknown type; cycle produced by absorbed content or a ruleset reclassification | **Repaired**: role-based cycle legality at Admission and in S0 `well_formed`, which S2 consumes (§6.2, §6.6). Circular reasoning stated only in prose remains a semantic-review residual |
| Cross-subject warrant cycle with an acyclic unit graph | `x1 CONCRETIZES y1` and `y2 CONSTRAINED_BY x2`, with validity entries both ways | Support cycle; second admission rejected (§6.6) |
| Nested simultaneous-definition groups (round 3) | cycle spanning nested groups; spanning sibling groups; SDG straddling subjects; promoting one member | Nested legal; sibling illegal without an enclosing SDG; straddling rejected; members promoted together only (§6.2, §12.2) |
| Legitimate recursion banned by accident (round 3) | mutually recursive equations; recursive functions; mutually importing modules | Legal: SDG with `USES_DEFINITION`; single-object recursion is unit content; code recursion is `NEUTRAL` derived structure (§6.2) |
| Ruleset self-reference (round 2) | edit policy so derived acceptance of policy changes the rules that derive it | Repaired in round 2 by adoption record (§6.6 S0) |
| Negation inside validity (round 2) | an obligation-existence condition (negative in currency) feeding discharge and back into validity | Repaired in round 2 by S3 placement and Admission step 8 (§7.4) |
| Challenge recursion | challenge chains, counter-challenge to unblock, override under challenge | Well-founded; conservative in both directions (§6.6 S1) |
| Challenge escape by ordinary re-scoping (round 2) | demote a challenged subject into an unchallenged composite, or promote a part out of a challenged one | Repaired in round 2 at the source subject (§6.8 step 4) |
| **Challenge escape at the destination** (round 3) | re-scope a challenged composite by adding or removing members so its challenged triple is no longer current | **Repaired**: the freeze covers every subject whose scope, regions or membership change, before or after (§6.8 step 4(b)) |
| **Structural foreign change under unresolved challenge** (round 3, Blocker B) | foreign structural-only change restores a demoted part as subject while its composite is challenged | **Repaired**: `Σ` unchanged, `aff(Q)` invalid, adoption frozen, tenure excludes the old judgment (§6.1, §11, §12.2); required counterexample in §22 |
| **Old acceptance resurrection after demotion and restoration** (round 3) | lawful demotion, then lawful promotion with the same bytes and scope; or `scope_id`, domain or mode oscillation | **Repaired** by tenure-scoped `ACC` (§6.1, §6.6) |
| **Resurrection through ledger truncation** (round 3, not in the Review) | `LEDGER_LOSS` drops the admission that demoted `A`; `Σ` again says subject | **Repaired** by the observed/effective comparison: the repository still declares the demotion, so `A` is quarantined (§13). *Superseded in round 4: partial, since a stale-consistent restore leaves `Q` empty; the loss boundary is the defense* |
| **Domain laundering** (round 3, not in the Review) | reclassify a part's owning domain, then promote it so a weaker reviewer accepts it | **Repaired**: a kind or domain change needs a judgment by an actor qualified for the current domain (§6.8 step 4(a), §12.2) |
| Ruleset evolution during quarantined intake | adopt a ruleset while a structural delta is quarantined; reclassify relation types | `Σ` and `Q` unchanged; adoption validated under the ruleset then in force; reclassification makes affected subjects ill-formed with visible impact; history unchanged (§11.2, §6.2, §13) |
| **Vocabulary evolution invalidating accepted content** (round 3, not in the Review) | rename or remove a relation type in a new ruleset | **Repaired**: adoption declares `READ`/`MIGRATE`/`REJECT` for existing uses and shows the derived impact before the gate; legacy relations are proposed and unaffected (§6.2) |
| Incomplete dependency knowledge (round 2) | add a unit to a judged-complete scope with an outside dependency; foreign file added beside a judged scope | Repaired in round 2 (completeness basis includes membership). Quarantined structure never enters the scope chain; uncovered content is reachable only in the `UNBOUNDED` fallback (§6.2, §6.5) |
| Stale evidence reuse after role change (round 3) | after demotion and restoration, reuse assessments from the earlier tenure | Evidence binds to content and execution, not role. It counts only when its bases are current and only under a current-tenure acceptance (§12.2) |
| Stale evidence reuse | merged-tree change in an undeclared execution dependency | Widening via analyzer incompleteness; residual stated (§8.4, §10) |
| Historical profile isolation after schema evolution | new record schema or relation vocabulary while version-bound work continues | Frozen Core profiles untouched (PC-001); `LEGACY(p)` interpreted by `p`; historical views use the ruleset and schema of their position; current derivation fails closed only through declared vocabulary impact (§6.2, §13, §24) |
| **Crash between ledger append and currentness qualification** (round 3, Blocker C) | append L100, crash before any witness holds it | **Repaired**: L100 is provisional; nothing depended on it; anchoring completes on restart, or the request is resubmitted (§15.3) |
| Crash between qualification and publication | admitted, integration CAS not done | `PENDING`, then `PUBLISHED`/`OVERTAKEN` (§15.3). *Superseded in round 4: revision 3 had no legal append to record the outcome (8a75346 Blocker A); repaired by successor-entry reconciliation* |
| **Stale or rewound canonical state** (round 3, Blocker C) | the Review's L99/L100 world; fresh clone reaching only witnesses lacking the newest checkpoint | **Repaired**: quorum admission plus `q_a + r > N + f`; every admitted head is visible to every qualifying evaluator (§15.4) |
| Witness disagreement | conflicting checkpoints; sub-quorum checkpoint of a vanished entry; relayed old checkpoints | `FORK` until human-gated resolution; relaying an old checkpoint is harmless; relaying can complete a quorum but never forge one (§15.4) |
| Repository restoration from stale backup | product ref and ledger restored to an older state | Product: absorbed, bytes drift, declarations quarantined, `Σ` unaffected. Ledger: `ROLLBACK` from any read quorum (§13) |
| Foreign force-push or manual merge | force-push of the integration ref; manual manifest conflict resolution | Absorbed; foreign work never overwritten; structural deltas quarantined (§11, §15.3) |
| Forged canonical entry (round 2) | direct push of a well-formed entry to the ledger ref | Repaired in round 2 by entry authentication (§15.4) |
| Legacy and native authority simultaneously present | legacy edit to a cut-over section; foreign move of a native unit into a legacy subject; legacy `status:` field | Foreign change and drift; mode-mixing membership needs a mode-transition record; lifecycle fields enact nothing (§12.1, §12.6) |
| Cross-repository imported authority becoming stale | external retraction, fork or rollback after import; external head consulted while provisional | Consultation qualifies the external head; an adverse later consultation supersedes the earlier one and makes reliant imports non-current; unreachability does not flap (§11.4) |
| Purged lineage presented from a stale mirror (round 3, not in the Review) | after a confidentiality lineage migration, a restored backup plus the old witnesses still qualify cryptographically | **Repaired**: retirement statement admitted at the old witnesses (§15.5) |
| Agent proposal or PASS mistaken for authority | agent submits PASS, equivalence about its own change, promotion of a part, a self-declared SDG, a manifest demotion of a challenged subject, or reports a provisional submission as admitted | Proposal only; authorization, freeze and acceptance rules reject; SDGs need acceptance; responses say `PROVISIONAL` until admission; discharge is derived (§6.8, §7.4, §9.1) |

Residuals carried rather than repaired, because no architecture removes them: undeclared semantic dependencies (§8.4); circular reasoning stated only in prose (§6.2); foreign edits that reduce governance validity, but never production, until dispositioned (§11.3); and the information-theoretic limit of §15.4.

Rounds 2-3 minimum-justified-architecture record (superseded by §27.2, which carries its conclusions and rejected additions):

- **Primitives:** four, unchanged since round 2, when `Change` became an admission request. Round 3 adds none. The SDG is a semantic declaration. Effective structure and tenure are S0 derivations. Provisional versus admitted is a property of a ledger entry decided by witness quorum.
- **Constructs:** round 2 used one composite subject for both refinement parents and simultaneous groups. Round 3 separates them, because the conflation was Blocker A; the separation adds a declaration, not a primitive. One boundary-completeness judgment serves per-unit and per-scope completeness. `acc(·)` is a display view.
- **Paths:** one append, admission and publication semantics for local and remote deployments. The multi-ref publication optimization is removed, so there is one path fewer. Policy acceptance is merged into ruleset adoption, and structural adoption reuses ordinary Admission validation: one rule, "content proposes, admitted records enact", now covers both. Reinstatement reuses the acceptance kind.
- **Persistent surfaces:** none added in round 3. The witness set gains quorum parameters and stores retirement statements. `Σ` lives in the derived index and is rebuilt from the ledger. Each surface has one writer and an explicit recovery path (§15.1).
- **Components:** seven, unchanged. The new responsibilities fall to existing owners: Derivation (S0 facts), Admission (structural validation, quorum admission), Ledger Store (qualification) and Content Model (observed declarations).
- **Rejected additions:**
  - a general rule language;
  - a separate refinement or reinstatement judgment kind;
  - a fourth publication state (provisional is an entry property, and publication never sees it);
  - a merge-and-publish reconciliation path;
  - a cross-repository coordinator;
  - a stored copy of effective structure;
  - automatic, non-human-gated abandonment of sub-quorum checkpoints (rare, and its safety would depend on witness counts that read repair can change);
  - a fifth primitive for simultaneous definition.

### 27.4 Round 5: out-of-matrix pass against the workflow layer

This pass covers only what revision 5 adds and its interaction with the revision-4 mechanisms. §27.1 still governs the rest. Each attack tried to obey every local rule of §7.5-§7.10 while violating A5-A9, S9 or the doctrine-realization objective.

| Attack | Trajectory attempted | Result (revision 5) |
|---|---|---|
| Overstep with disclosure | implementer edits a unit outside its write scope and reports it as a deviation | Holds: `VIOLATION`, never integrated; the disclosure becomes an amendment request for the principal; no silent widening (§7.7) |
| Overstep without disclosure | the same, unreported | Holds: `VIOLATION` plus `DISCREPANCY`; integrity finding; visible to every later reviewer of the item (§7.7) |
| **Grading its own exam** (found in this pass) | implementer loosens or deletes the acceptance test that judges its work, inside a `tests/**` write scope | **Repaired**: evidence specifications outside `evidence_specs` are outside every implementer write scope by lint, and test deletion, skipping and expected-failure marking are `HARD` test-integrity checks; loosened assertions are signals, and mutation strength catches tests that test nothing (§7.6 rule 6, §7.7). Semantic weakening inside a test the implementer legitimately authored stays with review |
| Weak contract | principal writes a contract whose obligations are all `REVIEW`, or trivially checkable, to ease the work | Lint enforces policy minimum coverage per item kind; adequacy is an R2 plan acceptance by another execution (§7.6 rule 3). Residual: an adequate-looking but weak contract passing a weak review is a semantic failure, as in any review |
| **Local resolution of an authority defect** (found in this pass) | an implementer reports that D3 is unrealizable; the principal records `RESOLVE_LOCAL` and amends the item to work around it | **Repaired**: allowed outcomes are a function of the report's kind, reason and target domain; an authority-defect request admits only `CHALLENGE` or `ESCALATE` (and, for D1/D2 targets, always creates human attention) (§7.9) |
| **Materiality under-declaration** (found in this pass) | a raiser files a finding about a D2 estimator as `ROUTINE` | **Repaired**: the domain floor raises every report targeting a D1 or D2 unit to at least `MATERIAL` from the target's effective domain (§7.9) |
| Systematic downgrading | the principal downgrades every non-floor material finding | Each downgrade is a recorded judgment shown in the digest, challengeable, and countable per plan; floor items cannot be downgraded (§7.9, §9.8). Residual: a human who never reads the digest; downgrade rate is a reopen trigger (§26) |
| Escalation flooding | agents mark every report `CRITICAL` to avoid responsibility | Merging, impact ranking and the digest bound the cost; the floors are minimums, not the only route. Residual: human load is an empirical question and a reopen trigger (§26) |
| **Two principals, one plan** (found in this pass) | two coordination tasks for one plan run concurrently and amend it from different bases | **Repaired**: a change plan is a serialization surface for coordination (§7.5, §8.3). Even without it, the second amendment's basis would be stale at Admission step 6; the surface prevents the wasted work |
| Self-review under a new identity | the principal's model, in a new task, reviews the contract it authored | Rejected only when provenance shows context continuation; a fresh context of the same model passes A9's process-independence test, and the common-mode dependency is recorded; policy can require another model family for high-consequence surfaces (§9.6). Residual: epistemic independence across one model is limited, as the 6.6 workflow owner states |
| Author framing leaks to the reviewer | conclusions placed in commit messages, result narrative or code comments | Commit messages, narrative and outcome are excluded from the review brief; code comments are content under review and cannot be stripped (residual, §9.6) |
| Keyword gaming | agent rephrases prose to avoid certainty vocabulary | Gains nothing: prose checks are `HEURISTIC` and decide nothing; facts are machine-produced, so there is no factual claim to launder (A6, A7) |
| Stale contract | the principal amends an item while its implementer runs | The running task's basis names the old item revision; its result's conformance is computed against the contract it was given; integration fails currency (step 6) and routes to revalidation (§7.2, §7.6 rule 4) |
| Check template wrong | a `HARD` template has a false positive that blocks legitimate work | Challengeable; corrected by human-gated ruleset adoption; current conformance re-derived; history not re-adjudicated (§13). Qualification of `HARD` templates bounds the rate (§22) |
| Undetected discovery | the agent never notices the anomaly it should report | **Not repairable by machinery** and not claimed (§1.1, §1.3, §19.3). Mitigations are independent bidirectional review, signals, and evidence reruns; whatever is detected survives (A8) |
| Verification as PASS | a clean conformance view on a candidate with no review | Never integrated: discharge needs the current review judgments (§7.4, §7.8, §6.8 step 7) |
| Production blocked by verification | a human needs to ship while governance is not closed | Production commits remain ordinary Git and are absorbed as foreign change (§1.3, §11); verification blocks governance closure, never production |

Residuals carried: semantic adequacy of contracts and reviews; detection itself; independence limits within one model family; artifact-embedded framing; human attention capacity.

### 27.5 Minimum-justified-architecture pass (round 5)

The question for revision 5 was whether the workflow layer needs a new primitive, record category, persistent surface, component, state machine or identifier.

- **Primitives:** four, unchanged. A contract is plan content; a role is a policy parameter; conformance is derived.
- **Record categories:** five, unchanged. New judgment kinds in the support tier (task result, report, coordination decision, materiality reclassification, human acknowledgment) and one observation kind (check execution). Challenges and Serious Challenges keep their tier.
- **Persistent surfaces:** six, unchanged. Contracts live in plan units, and role templates, check templates, routing and floors in the ruleset and policy content.
- **Components:** seven, unchanged (§16.1). Derivation gains S3 classifications, Admission two checks inside existing steps, the Dispatcher check executions, suspension and integration requests, the Interface three renderings.
- **State machines:** none added. Conformance, decision class, amendment class and escalation are derived. Task suspension is Dispatcher operational state.
- **Ordinary-path cost:** one contract per item (authored once, accepted with the item); check executions on each candidate; one review per candidate, which revision 4 already required; one integration request per candidate, which replaces the implicit one.
- **Rejected additions:**
  - a separate Verifier component or service: it would be a second admission, and the checks are pure functions plus recorded executions;
  - a general workflow engine (BPMN, a DAG executor): readiness and routing are already derivation;
  - a long-lived principal process with canonical memory: the decision brief makes it unnecessary and its loss harmless;
  - agent-authored check scripts, or checks embedded in contracts: the verifier would stop being protected, and a rule language would return by the back door;
  - a model-as-verifier for mechanical classes: nondeterministic, and it would turn a judgment into an apparent fact (S9);
  - blocking keyword checks: they would parse prose for control and invite gaming;
  - storing conformance reports: derived;
  - a universal finding or discovery database: S13 keeps one canonical home per finding;
  - a separate message bus between agents: typed reports and derived obligations already carry every communication that changes what happens next.

### 27.6 Round 6: repair verification against the `ffbad17` Review

This pass re-runs every trajectory of the `ffbad17` Review against revision 6, and then attacks the repairs themselves. Like every pass here, it is the author's own rationale and awards nothing.

| Trajectory | Result (revision 6) |
|---|---|
| Blocker A, ordinary: a blocking challenge against the upholding of a non-blocking challenge | Holds: a counter-challenge has no effect while open; the triple stays `REVOKED` (§6.6 S1) |
| Blocker A, loss: a pre-loss dismissal of that counter-challenge, then `LEDGER_LOSS` | Holds: the dismissal of a counter-challenge is not a relaxer and changes nothing; the revocation is ungated |
| Successful counter-challenge, then loss | Holds conservatively: the upholding of the counter-challenge is a relaxer; the boundary withholds it and the revocation returns |
| Challenge against a successful counter-challenge's upholding | Holds: it is an ordinary challenge against a relaxer; while open and blocking it suspends the relaxer and the revocation returns |
| Blocker B, ordinary: the principal amends the item a `CRITICAL` question targets | Holds: obligations are keyed on the report's existence; the entry is annotated "target changed since raised" and stays open until a human answers (§7.9 Persistence) |
| Blocker B, loss: a pending `CRITICAL` question at `R` | Holds: the report survives and its obligation stays open; a pre-boundary acknowledgment is withheld, so the item reopens |
| Downgrade as discharge | Repaired: a reclassification moves a non-floor item to the digest; it is never a human discharge, and A8 now says so (§2.5, §7.9) |
| Blocker C: phase-1 result and mid-task blocking report | Holds: bound to the task, claiming no discharge; step 7 applies only to claimed discharge (§6.8, §7.8) |
| Blocker C: binding authenticity | Holds within the declared trust model: signed envelope verified at Admission and carried in records; replay needs no private state (§7.5, §15.6) |
| Blocker C: self-review by bootstrap in the author's session, or by a Git-envelope route | Holds: lineage is `UNKNOWN`, so the judgment is non-independent and discharges nothing (fail closed) |
| Blocker D: flip `scientific`, drop an escalation trigger, unfreeze an interface, plus one added check | Holds: each field moves against its direction, and the added obligation or check is outside the whitelist unless it is a secondary `HARD` check; R2 |
| Blocker D: decomposition onto new item units | Removed: decomposition is a task partition over one unchanged item; no acceptance moves (§7.9) |
| N2: ABA without the attempt log | Holds: absorbed as `OVERTAKEN`, human attention, no silent re-application (§15.3) |
| N5: conflicting rebase at integration | Holds: routes to a new iteration; machinery resolves nothing (K3, §7.8) |

**Attacks on the repairs.**

| Attack | Result |
|---|---|
| Counter-challenge flood: raise many counter-challenges against upholdings | No effect on status; each creates an adjudication obligation, so the cost is work, not safety. Policy may restrict who is qualified to counter-challenge |
| Stale-report pile-up: identity-keyed obligations never close by themselves | Intended (A8). The principal may `DECLINE` a non-floor report as moot; floor items need a human answer, and a merged entry lets the human answer a set at once (§9.8). Load is a §26 trigger |
| Envelope reuse: an author session submits with a reviewer's envelope | Within the role it may submit, but without the launch credential its lineage is `UNKNOWN`, so no independence is credited |
| Compromised harness adapter or issue key | Outside the declared trust model; forged bindings and lineage are possible until the key is rotated by the human-gated lifecycle record (§15.6). Disclosed, not repaired |
| Manual-route review burden | Independence on manual routes needs a human lineage attestation. This is a deliberate cost: unknown independence is not independence |
| Tightening to infeasibility: the principal narrows a write scope or sets the budget to zero | A liveness cost only. Nothing weaker is admitted; infeasibility surfaces as amendment requests and escalations, and every R1 decision is in the digest |
| Partition to avoid holistic review | The item-level review of the integrated result is required unless policy waives it for named item kinds |
| Plan edits outside items (objective section) | Every item's plan acceptance names the objective section in its basis (§7.2), so all items lose coverage and need R2; an objective change is a `CRITICAL` floor item |
| False `OVERTAKEN` when the CAS never happened and the log was lost | A rare human-attention cost, accepted to avoid silently reversing a deliberate reset |

Residuals carried: those of §27.4, plus forged bindings under a compromised issue key or adapter, and human load from fail-closed independence on manual routes.

### 27.7 Minimum-justified-architecture pass (round 6)

- **Primitives:** four, unchanged.
- **Record categories:** five, unchanged. `FINDING` moves wholly to the support tier. One human support-tier judgment kind is added (lineage attestation), and one coordination outcome (`PARTITION`). The `PLAN_STRENGTHENING` equivalence class is removed.
- **Persistent surfaces:** six, unchanged. The issue key lives in operator state with the other keys; envelopes travel in transport and inside admitted records.
- **Components:** seven, unchanged. The Dispatcher signs envelopes and launch attestations; Admission verifies them.
- **Trust roots:** one added, the Dispatcher issue key, because the Review showed that the execution-to-task binding is something the problem needs (`ffbad17` §7).
- **Removed in revision 6:** suspension of revocations by open counter-challenges; the monotone and decomposition amendment classes; the self-certified plan equivalence; currency-keyed escalation; downgrade as discharge; silent ABA re-application.
- **Rejected additions:**
  - a ledger entry per task issue: it would add a quorum round per task, and a signed envelope carried in records gives the same replayable binding;
  - an epoch or generation for challenge polarity: polarity is syntactic;
  - making every challenge against an upholding inert, including after it is upheld: that would make revocations unrepairable, which §6.6 rejects;
  - letting a human-attested lineage be inferred from route metadata alone.

### 27.8 Round 7: repair verification against the `f3608f5` Review

| Trajectory | Result (revision 7) |
|---|---|
| Blocker A: a `HUMAN_QUESTION` submitted after the item was amended | Holds: reports are exempt from step 6 and admitted; existence-keyed routing then applies (§6.8, §7.9) |
| A stale task result that carries a material finding | Holds: the result is routed to revalidation, and the rejecting entry admits the finding |
| Blocker B: changed candidate `r1`, product at `r0`, review before integration | Holds: the review declares frame `C` and is current in `D_n[C]`; the integration's discharge predicate holds in the post-state where `T = M_n(C)` (§6.9) |
| Head moves a unit the review read | Holds: stale in `D_n[C']`, re-review |
| Unit changed on both sides with a clean textual merge | Holds: judged at the merged revision, so a review of `C`'s revision is stale (K3) |
| Blocker C: H1 publishes and crashes, human reset, H2 with an intact no-attempt log | Holds: H2 is not the publisher and never performs the effect; ambiguous route (§15.3) |
| Publisher restart after intent logged | Holds: ambiguous route; at most one attempt per entry |
| Blocker D: building the first shadow kernel | Holds: G2 needs only design acceptance, a reviewed shadow workplan and stakeholder authorization; shadow evidence belongs to G3 (§25) |
| N2: undisclosed breach | Holds: conformance is a set; rejection and integrity finding both follow (§7.7) |

**Attacks on the repairs.**

| Attack | Result |
|---|---|
| Use the report exemption to smuggle support: file a "report" whose stale basis is later cited | No rule consumes a report's basis or currency; resolving records reference reports by identity; a report supports nothing (§6.8 step 6, §7.9) |
| Flood reports from a stale task to bypass suspension or budgets | Reports are admitted but only create obligations; they cannot discharge or integrate anything. Volume is the §26 human-load trigger |
| Make frame records current in the admitted state | Impossible by construction: the frame's tree is hypothetical, and nothing in `D_n` reads `D_n[C]`. Only integration makes `M_n(C)` the admitted tree |
| Choose a favourable merge to get a frame | The merge algorithm is fixed by the system version, and a non-clean merge has no frame |
| A frame record citing records from another candidate's frame | Its `record` entries are evaluated in its own frame; another frame's records are current there only if their bases hold in `M_n(C)`. Nothing transfers by assertion |
| Two candidates both current in their frames, integrated in sequence | The second integration is evaluated at the new head: its frame is recomputed on the new `T`, and stale records go to re-review (§8.2) |
| Publisher host permanently lost while publication is pending | Liveness only: a takeover host records `OVERTAKEN` with human attention, and the human re-applies or keeps `B_n` |
| Slow publisher races a takeover | Bounded residual: at most one compare-and-swap by the only authorized host, which, if it lands after the takeover absorption, is absorbed as foreign movement while human attention is already open (§15.3) |
| Gate-skipping: start Phase D work under a Phase B PASS | §25: no D4 work before G2 |

Residuals carried: those of §27.6, plus the slow-publisher window and the liveness cost of a lost publisher.

### 27.9 Minimum-justified-architecture pass (round 7)

- **Primitives:** four, unchanged. A candidate frame is a derivation over a hypothetical tree, not a new kind of state.
- **Record categories:** five, unchanged. Records gain a declared frame field.
- **Persistent surfaces:** six, unchanged. The publisher's write-ahead attempt log is the existing operator-state log, now required for the publisher's own attempt and never read by derivation.
- **Components:** seven, unchanged. Admission keys become per host.
- **Gates:** §25 gains a staged structure, G1-G4, and four criteria (13-16), so the authorizing evidence is never produced after the authorization it needs.
- **Removed in revision 7:** the step-6 currency check on reports; the unscoped "no attempt" exception for any host; the single D4 gate.
- **Rejected additions:**
  - a candidate ledger or staging ledger: frames give currency without a second store;
  - a publication-lease record in the ledger: the per-entry publisher already names the only executor, and a lease adds a quorum round per publication;
  - automatic re-application by takeover hosts: it would reintroduce Blocker C;
  - admitting frame records as current in the admitted state: it would let unintegrated work count as governing (P4, S11).

### 27.10 Round 8: re-derivation pass against the `ac71fa9` Review

The `ac71fa9` Review invoked the convergence owner's active simplification trigger: the candidate-currency contract had failed three Review rounds and the publication contract four. Revision 8 therefore replaces both contracts instead of adding exceptions. Candidate currency now rests on one idea: a candidate is a transformation, and every basis entry relies on its before-image, its output or its context. Publication now rests on one idea: an effect authorized from an expected head is revoked only by moving the ref. This pass re-runs the Review's trajectories, then attacks the replacements.

| Trajectory | Result (revision 8) |
|---|---|
| Blocker A: `read(u@r0)`, then a substantive edit to `r1`, with no concurrency | Holds: the read is a before-image entry, satisfied while the head still has `r0` and a fixed fact after integration (§6.9) |
| Widened context that includes the edited unit | Holds: also a before-image entry |
| A concurrent change to the edited unit | Holds conservatively: the before-image is stale, so the work is rebased (K1) |
| Blocker B: promoting a part through the ordinary pipeline | Holds: the frame applies the proposed structure; the reviewer records a prospective acceptance; integration admits promotion and acceptance together; the tenure starts there (§6.9, §12.2) |
| Restoration, and adoption of a quarantined promotion | Holds through the same path; `Δ_Σ(C)` includes adopted keys |
| Blocker C: publisher pauses after its check, takeover, human keep, publisher resumes | Holds: the fence moved the ref, so the resumed compare-and-swap fails (§15.3) |
| Publisher's compare-and-swap wins the race against the fence | Holds: the fence fails, `C_n` is observed, and only then is a human decision admissible |

**Attacks on the replacements.**

| Attack | Result |
|---|---|
| Label a stale read as a before-image to keep it current | Impossible: roles are computed from `B`, `C` and the entry. A before-image entry is satisfied only while the head still has the base revision of a unit the candidate changes |
| Rely on a revision that is neither base nor output of a changed unit | Never satisfied |
| Use a prospective acceptance without integrating its candidate | It counts only when `τ(s)` is the admission that integrated that candidate |
| Integrate a different candidate with the same promotion, reusing another frame's acceptance | It does not count: the integrating admission must be that frame's own candidate |
| A promotion frame that would break a challenge freeze | The frame does not exist, because step 4's checks apply in the frame |
| Make proposed structure effective early | Only in the hypothetical frame. `D_n` keeps the declaration quarantined until the integrating admission |
| Fence flooding by an aggressive takeover policy | Liveness and noise only: each fence is a no-content commit plus a human decision. The operational wait bounds it, and frequent fencing is a §26 trigger |
| A foreign writer returns the ref to exactly `B_n` after a fence | Detected, not prevented: `LATE_PUBLICATION` with `CRITICAL` attention (disclosed residual) |
| A restored or copied attempt log claims "no attempt" | Not intact by definition; the host fences (§15.3, §21 item 14) |
| A paused fence publisher | Another host fences again; any fence moves the ref away from `B_n` |

Residuals carried: those of §27.8, minus the slow-publisher window, plus the detected-not-prevented return of the ref to exactly `B_n`.

### 27.11 Minimum-justified-architecture pass (round 8)

- **Primitives:** four, unchanged. Frames are derivations over hypothetical inputs; basis-entry roles are a computed classification, not a field an agent writes.
- **Record categories:** five, unchanged. A fencing absorption is an absorption carrying one effect. `LATE_PUBLICATION` is a derived integrity finding.
- **Persistent surfaces:** six, unchanged. Fence commits live on the product ref like any other commit.
- **Components:** seven, unchanged.
- **Removed:** revision 7's all-entries-in-the-frame rule; the revision-4 merged-tree exception in step 6, now subsumed by the frame rule; same-request acceptance as a request-shape requirement, replaced by acceptance bound to the integrating admission; the publisher's ledger head check as a safety mechanism; the claim that late effects never silently reverse a reset.
- **Rejected additions:**
  - a staging ledger for candidates;
  - a conditional-acceptance record kind: a prospective acceptance is an ordinary acceptance in a frame;
  - a ledger lease or epoch for publication authority: Git cannot check it, and only moving the ref revokes;
  - multi-ref atomic push of fence and ledger: a server capability revision 3 already declined;
  - agent-declared basis roles.

### 27.12 Round 9: transformation identity and enactment against the `730490d` Review

Both `730490d` blockers sit at the transformation owner that §27.10 re-derived, so this round completes that contract rather than adding beside it. It adds two missing distinctions: a transformation's full identity, and inspection versus enactment.

| Trajectory | Result (revision 9) |
|---|---|
| Blocker A: promote a part starting with no prospective acceptance | Holds: the frame needs well-formedness only. The first result is admitted, executions run, the reviewer accepts in the existing frame, and integration enforces the enactment condition (§6.9, §6.8 step 4) |
| Integration of a promotion without an acceptance | Rejected at the enactment condition |
| Restoration, foreign-promotion adoption, SDG promoted as one composite | Holds through the same path |
| Blocker B: same commit with two adoption sets | Holds: two identities `id(B, C, A)` and two frames; an acceptance in one does not satisfy the prospective-acceptance rule for the other |
| A clean rebase preserving the structural delta | The acceptance carries if its basis holds and `Δ_Σ` is equal; otherwise it is re-requested |
| N3: two paused fence publishers | Holds: no decision until an observation away from `B_n` |
| N2: foreign return to `B_n` after a decision | Split oracle: detected and escalated, not claimed impossible |

**Attacks on the completion.**

| Attack | Result |
|---|---|
| Accept a subject in the frame of a well-formed but challenge-frozen promotion | No frame: freezes are well-formedness checks, so the attack never reaches enactment |
| Make the prospective subject valid in the frame without acceptance | It has no acceptance in its prospective tenure, so it is invalid in the frame. Inspection does not grant validity |
| Change the adoption set after the result | The transformation identity is fixed by the result; a different set is a different transformation, with new records |
| Reuse a prospective acceptance across a rebase that changes another subject's structure | `Δ_Σ` differs, so it does not count |
| A frame record of `X` cited from the frame of `X'` | Satisfied only if its basis holds in `D_n[X']` (§6.9) |
| An inspection frame exists for a promotion that is never accepted | Nothing is enacted; the quarantined proposal remains in `D_n` |

Residuals carried: those of §27.10.

### 27.13 Minimum-justified-architecture pass (round 9)

- **Primitives:** four, unchanged.
- **Record categories, persistent surfaces and components:** five, six and seven, unchanged.
- **Added:** none. Transformation identity is a hash of fields the result already carries. The well-formedness/enactment split partitions existing step-4 checks.
- **Removed:** commit-only frame naming; the frame-existence dependency on the acceptance; the over-strong §22 oracle.
- **Rejected:**
  - a separate conditional-acceptance kind;
  - a frame registry: identity is derived from the result;
  - making the proposed subject effective early for review.

### 27.14 Round 10: lifecycle binding and assessment disagreement against the `fb3e542` Review

| Trajectory | Result (revision 10) |
|---|---|
| Blocker A: promote, demote, identically restore, reuse the first prospective acceptance | Holds: the restoration is new work, so not the same lineage, and `j` already counted for `τ1`; rejected at enactment (§6.9) |
| A rebase of the original work before enactment | `j` stays usable: same lineage, same structure, basis holds, not yet bound |
| A purported "rebase" by unrelated work with equal structure | Not the same bound obligation, so not the same lineage |
| Blocker B: current pass and current fail of one key, either order | Holds: `undisputed = P`; validity and discharge are visibly provisional; adjudication obligation to the claim's owner (§6.6, §7.4) |
| Stale failing assessment; different regime | No conflict |
| Owner supersession or `IMMATERIALITY` judgment | Conflict resolved; an upheld challenge to the `IMMATERIALITY` judgment restores it |

**Attacks on the repairs.**

| Attack | Result |
|---|---|
| Suppress a pass by filing a failing assessment | Not possible: only an admissible assessment by an actor qualified for that evidence kind counts; the effect is a provisional cap, not a block; the conflict goes to the owner. Spurious adverse filing is an R2 abuse handled by challenge |
| Declare immateriality to clear an awkward fail | Only an actor qualified for the claim's owning domain may; the judgment is challengeable and visible; D1/D2 claims also get human attention |
| Create a cycle through inhibition edges | Rejected at Admission (step 5); a corrupted one evaluates to `F` with an integrity obligation |
| Resolve by posting a later pass | A later pass is not supersession unless authorized as such; the conflict stays |
| Bind `j` twice by racing two integrations of the same lineage | The ledger orders admissions; only the first starts a tenure, and the second is stale (its obligation is discharged) |

Residuals carried: those of §27.12.

### 27.15 Minimum-justified-architecture pass (round 10)

- **Primitives, record categories, persistent surfaces and components:** four, five, six and seven, unchanged.
- **Added:**
  - one support-tier judgment kind (`IMMATERIALITY`), because a non-positional resolution must be accountable;
  - inhibition edges in the acyclicity check, which are the price of realizing the inherited disagreement rule inside S2;
  - `bind(j)`, which is derived from the ledger, not stored.
- **Changed:** S2 uniqueness now rests on graph acyclicity, not monotonicity alone. This is the material change of this revision, and it is stated for independent attack.
- **Rejected alternatives:**
  - qualifying only discharge in S3, which would leave dependents seeing `T`;
  - computing conflicts from S0/S1 facts, which would let stale failing evidence qualify claims and so violate S4;
  - latest-record selection;
  - requiring every disagreement to become a Serious Challenge.

### 27.16 Round 11: existence-keyed disagreement against the `124b0b7` Review

The `124b0b7` Review invoked the convergence trigger again. The defect was in revision 10's own repair: an inhibitory dependence on the *currency* of failing assessments let restrictive operations (filing a challenge, withholding at a loss boundary) become permissive for the claim. Revision 11 removes that dependence instead of patching around it. Disagreement is keyed on the existence of the records, and only explicit, in-effect dispositions end it. S2 is monotone again.

| Trajectory | Result (revision 11) |
|---|---|
| Blocking challenge against the failing assessment, no adjudication | Holds: an open challenge disposes of nothing; still `disputed` |
| Known loss, positive-only requalification or attestation | Holds: the failing assessment still exists and the conflict stays |
| Pre-loss disposition, not re-recorded | Holds: withheld by `cont`; the conflict returns |
| Challenge of a dismissal; challenge of `IMMATERIALITY` | Holds: the disposition is not in effect while challenged |
| Stale failing assessment after an execution change; different regime | No conflict: different key |
| Replicates differing only in seed | Conflict: seed and replicate are excluded from the key |

**Deterministic check.** `qualification/ssds80/s1_disagreement_model_check.py` enumerates every ledger up to a bounded length over the record kinds involved and checks:

- an open ordinary challenge or a `LEDGER_LOSS` never ends a dispute;
- an open counter-challenge or a `LEDGER_LOSS` never lifts a revocation.

At depth 5 it checks 23,933 transitions with no failures. With `REV10=1` it reverts to revision 10's currency-based predicate and reports the `124b0b7` Blocker A trajectories, so the check can tell the two apart. It transcribes the workplan's equations: it can falsify their stated properties, but it cannot establish that the design is adequate (DS-001).

**Attacks on the re-derivation.**

| Attack | Result |
|---|---|
| File spurious failing assessments to keep a claim provisional | Only actors qualified for that evidence kind can file admissible assessments; the effect is a provisional cap plus an obligation to the owner, and abusive filing is answerable by challenge, whose *upholding* disposes |
| Dispose by a self-supersession of the failing assessment by someone else | Admission authorizes supersession only by the assessor or the claim's owner |
| Collapse keys so stale failing evidence keeps conflicting | The key includes execution identity, so movement of code or claim creates a new key |
| Split keys so real disagreement never conflicts | Seed and replicate are excluded; regime and parameter instance are part of the claim being assessed |

Residuals carried: those of §27.14.

### 27.17 Minimum-justified-architecture pass (round 11)

- **Removed:** revision 10's inhibition edges and the non-monotone S2. S2's least-fixed-point argument is restored unchanged.
- **Added:** the S1 predicates `disputed` and `disposed`, which use only existing facts. The assessment key gains execution identity.
- **Primitives, record categories, persistent surfaces and components:** unchanged.
- **Kept:** the `IMMATERIALITY` judgment kind.

### 27.18 Round 12: applicable adverse evidence and effective disposition against the `97e753f` Review

The `97e753f` Review placed the family at post-simplification recurrence. Its two blockers had one cause: revision 11 used a single existence-keyed predicate for two questions of different kind. Revision 12 answers *which failing evidence may still bear on the claim* syntactically and conservatively, and *whether a disposition stands* by currency read positively.

| Trajectory | Result (revision 12) |
|---|---|
| PASS and FAIL at `u@r0`; equivalence `r0 → r1`; passing rerun at `r1` (`97e753f` A) | Holds: the failing assessment is applicable through the admitted equivalence; `ev = P` |
| The same change without equivalence | No conflict: both earlier assessments are inapplicable; the rerun alone gives `T` |
| Editorial claim revision with equivalence, either reassessment order | Holds: one obligation, one `undisputed`; order cannot matter |
| Two concurrently admissible environments | Conflict if the specification leaves the environment free; otherwise the other assessment is inadmissible |
| `IMMATERIALITY` whose prerequisite moves (`97e753f` B1); stale superseder | Holds: `eff = current(d) = F`; the qualification returns until re-disposal |
| Upholding under an open blocking counter-challenge (`97e753f` B2) | Holds: `contested`; the claim is qualified and the failing assessment stays `REVOKED`; dismissing the counter-challenge restores the disposition |
| Open challenge, loss, positive-only requalification (`124b0b7` A) | Holds as in revision 11 |
| Failing assessment whose oracle subject moved (`97e753f` N3) | Not adverse: applicability follows every content entry |
| §6.6 versus §7.4 | One term, `ev(s, e)`, read by both |

**Deterministic check.** The rewritten model check adds execution moves with and without equivalence, governing-subject moves, supersession chains and an oracle written in plain-language form. At depth 5 it checks 81,171 transitions with no failures, and every named discriminator gives its expected value. `REV11=1` reproduces the `97e753f` A, B1 and B2 trajectories. It also shows a supersession chain that revision 11 failed to count as a disposition, a restrictive gap. `REV10=1` reproduces the `124b0b7` trajectories. As before, the check can falsify the equations' stated properties but never establish adequacy (DS-001).

**Attacks on the re-derivation.**

| Attack | Result |
|---|---|
| Record a spurious equivalence to keep stale failing evidence adverse | Restrictive only: the claim stays provisional and the owner disposes of it; equivalence judgments themselves need a qualified, independent actor (§6.7) |
| Record an equivalence to *escape* failing evidence | Impossible: an equivalence can only add applicability, never remove it |
| Challenge the equivalence so that the failing evidence drops out | It does not drop out: applicability counts admitted equivalences whatever their status |
| Dispose of the failing assessment with a self-authored `IMMATERIALITY` | Not independent: R2 with independence from the claim's author, R3 for D1/D2 (§6.8 step 3) |
| A disposition whose validity basis leads back to the claim | Rejected by step 5: dispositions are static support edges of the claim |
| Frame-only failing evidence against the admitted claim | Not applicable: outside its frame an output entry on unintegrated content fails; after integration it is ordinary currency |

Residuals carried: those of §27.14, and two restrictive residues. A failing assessment linked to the present by an equivalence that is later challenged, or whose realization premise is challenged but not yet revoked, stays adverse until the owner disposes of it.

### 27.19 Minimum-justified-architecture pass (round 12)

- **Removed:** the assessment key; the S1 predicates `disputed`, `disposed` and `in_effect`; the two readings of disputedness in §6.6 and §7.4.
- **Added:** the S0 predicate `applicable`, a relaxation of `sat`; the S2 terms `ev`, `undisputed`, `disp` and `eff`; dispositions as static support edges.
- **Primitives, record kinds, persistent surfaces and components:** unchanged. No new judgment kind; `IMMATERIALITY` is kept.
- **Simplification:** the key's composition, which the Manual would have had to fix by hand, is replaced by two rules that already existed: admissibility to the specification (§10) and basis satisfaction (§6.6).

### 27.20 Round 13: owner applicability dimensions against the `4c35d92` Review

Three successive proxies (currency, key, whole basis) failed permissively. Revision 13 takes the evidence owner's applicability dimensions as the definition and assigns each one role. Revision 12's effective-disposition half is kept unchanged.

| Trajectory | Result (revision 13) |
|---|---|
| A unit only the failing assessor read is edited without equivalence (`4c35d92` A1) | Holds: provenance; the failing assessment stays adverse; `ev = P`; the adjudication obligation stays open |
| The same edit to a unit only the passing assessor read | The passing assessment goes stale; `ev = F` |
| Implementer iteration touching only a unit the failing reviewer read | Holds: the failing realization's evidentiary premises are unchanged in `D_n[X']`, so the candidate stays qualified |
| `UNBOUNDED` closure, unrelated change, reassessment order varied | Holds: the fallback is provenance; only the claim revision and named execution content end bearing |
| Failing assessment whose context moved during its task | Admitted under the step-6 exemption; adverse |
| Oracle, tolerance or specification move; passing realization reassessed first | Holds: the failing assessment stays adverse until its own realization is reassessed or judged immaterial; order-independent |
| Upheld challenge against a completeness premise (`4c35d92` A2) | Disposes of nothing. Contrast: an upheld challenge against the failing realization disposes of it |
| Execution edit without equivalence | Not adverse: the observation is about other code; the rerun obligation remains |
| `97e753f` A, B1, B2 and `124b0b7` A | Hold as in revision 12 |

**Deterministic check.** The model check was rewritten again. It models evidentiary moves (execution, with or without equivalence), interpretive moves (oracle), context reads and moves, completeness premises, challenges against realizations, and governing-subject moves. Its oracle is written in separate code that does not call the bearing, disposer or effectiveness predicates. Beyond P1-P4 and the oracle it checks three owner-grounded properties: P5, P6 and Q (§0.1). At depth 5 it checks 920,081 transitions with no failures, and all 17 named discriminators give their expected values. `REV12=1` fails P5, P6, Q and the oracle; `REV11=1` fails Q and the oracle; `REV10=1` fails P1, Q and the oracle. The check can falsify the equations' stated properties but never establish adequacy (DS-001).

**Attacks on the re-derivation.**

| Attack | Result |
|---|---|
| Declare an extra execution dependency, then edit it, to make failing evidence lapse | Declarations are admitted structure under the specification's owner, not the assessor's choice. The move also makes the passing evidence stale, and each stale realization raises a rerun obligation. Ensemble granularity (Manual item 11) decides whether one passing rerun suffices |
| Change the specification so that the failing realization becomes inadmissible | Admissibility is decided against the specification revision the assessment named, so it is immutable. The change is interpretive: the failing assessment stays adverse until reassessed or judged immaterial |
| Record or challenge an equivalence | Restrictive only, as in revision 12: equivalences count by existence |
| Reassess the failing realization as the claim's author | Not independent: `eff = F` |
| Challenge the failing assessment to destabilize a disposition | No effect: dispositions name it in `identity` mode |

Residuals carried: those of §27.18. One restrictive residue is added: every interpretive change creates reassessment work for each bearing failing assessment on the affected obligations (§26 trigger).

### 27.21 Minimum-justified-architecture pass (round 13)

- **Removed:** the S0 predicate `applicable`, a relaxation over the whole basis; disposal through arbitrary record premises.
- **Added:** a fixed role for each of the evidence owner's applicability dimensions; the S0 predicate `bears` over evidentiary premises, computed mechanically at admission; failing assessments join the step-6 exemption.
- **Primitives, record kinds, persistent surfaces and components:** unchanged. The S2 terms `ev`, `undisputed`, `disp` and `eff` are unchanged.

## 28. Handoff state

```text
GOVERNING DESIGN PROTOCOL: SSDP 7.2.1 (adopted from 6.6.0 by stakeholder instruction 2026-10-12, §0.4)
TARGET: SSDS 8.0.0
ARCHITECTURE: basis-stamped judgments over content-addressed units grouped into acceptance subjects;
              stratified pure derivation (S0 observed content, admitted effective structure and publication
              classification; S1 challenges and loss-boundary continuity; S2 least-fixed-point support;
              S3 consequences); relation roles and cycle classes with simultaneous-definition groups;
              tenure-scoped acceptance; single Admission writer; single-ref append admitted by witness quorum;
              currentness only for quorum-witnessed heads; publication reconciled by the successor entry's
              integration observation; known admitted loss as a continuity boundary; Git-replicated ledger;
              optimistic concurrency; one intake route with structural quarantine; refinement plus qualified
              promotion for migration; workflow layer (revisions 5-6): workflow roles and decision classes R0-R3
              enforced on authenticated task envelopes, machine-readable work contracts with a closed
              control-tightening order, derived conformance verification (necessary, never sufficient), typed
              reports with existence-keyed routing and non-droppable escalation to an inspector view, fail-closed
              reviewer independence; syntactic challenge polarity with inert open counter-challenges;
              transformation frames keyed by full identity (B, C, A), with before-image, output and context roles,
              prospective structure, one-enactment prospective acceptance, and inspection separated from enactment
              for pre-integration review; assessment disagreement over bearing adverse evidence, provisional
              until a standing disposition; single-publisher effects revoked by ref fencing; staged gates G1-G4
OBJECTIVE: §1.1, including the doctrine-realization objective, held by the stakeholder as a tested aspiration
           (STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md SD-5, SD-6)
SOURCE BASIS: main af0455753e20ee54a969c844872e29e270007211 (7.2.1 accepted-current); rebased 2026-10-12 from
             f96b7ccf90dede4150d0efa17264fff07ec12d0d with reviewed bytes unchanged (§0.4 commit map)
DESIGN BASIS: befe6782e7c8fe038bf7cb764646d133ca167855 (befe678 hypothesis archived byte-identically)
PRIOR REVIEWS: f9d9de8 NO-PASS (repaired by revision 2); 441cf5c NO-PASS (repaired by revision 3);
               8a75346 NO-PASS (repaired by revision 4); ffbad17 NO-PASS covering revisions 4-5 and Phase A
               (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-FFBAD17-NO-PASS.md), repaired by revision 6;
               f3608f5 NO-PASS by a different model family
               (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-F3608F5-NO-PASS.md), repaired by revision 7;
               ac71fa9 NO-PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-AC71FA9-NO-PASS.md), re-derived by revision 8;
               730490d NO-PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-730490D-NO-PASS.md), repaired by revision 9;
               fb3e542 NO-PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-FB3E542-NO-PASS.md), repaired by revision 10;
               124b0b7 NO-PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-124B0B7-NO-PASS.md), re-derived by revision 11;
               97e753f NO-PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-97E753F-NO-PASS.md), re-derived by revision 12;
               4c35d92 NO-PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-4C35D92-NO-PASS.md); re-derived here (§0.1)
THIS WORKPLAN: design revision 13 with the 7.2.1 inheritance reconciliation; proposed; not accepted-current;
             not an Architecture Manual; no self-awarded PASS
SSDP 7: closed at 7.2.1; inheritance RECONCILED (§0.4, §19); Stage H obligation discharged under stakeholder
        instruction (§0.2); pre-cutover baseline Protocol 7.2.1 recovery (§24)
D3: ready for fresh independent falsification Review (Phase B, covering Phase A); D4 (shadow only) requires gate G2 (§25)
D4: NOT AUTHORIZED
SERIOUS CHALLENGE: none
NEXT ACTION: fresh-context sub-agent D3 Review of design revision 13 (stakeholder direction 2026-10-13), from
             qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-13.md; then Phase C.
```
