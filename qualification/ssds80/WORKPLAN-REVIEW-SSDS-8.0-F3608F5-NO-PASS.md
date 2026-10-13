# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 6

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: f3608f586ab7bb13faec4f0a174aa4ae5123a172
    SCOPE: whole proposed architecture, Revision 6 repairs, workflow execution/verification,
           persistence/derivation/concurrency/migration, and 7.2.1 inheritance reconciliation
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: a04e55ea7e77a12574777ae79cbe359fa2b18c1a
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR BASIS: SSDP 6.6 public source 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17 NO-PASS records in qualification/ssds80/
    REVIEW METHOD: immutable-source reconstruction; formula evaluation; locally compliant
                   counterexamples; out-of-matrix adequacy and capability-transfer assessment;
                   qualification-oracle challenge; candidate-pinned routing tests
    REVIEWER: GPT-6 (Codex), AI agent /root; exact serving build/minor version not exposed

All workplan section references below name the primary workplan at the full candidate SHA above. Governing-owner links are pinned to the governing public-source SHA. Findings are this reviewer's interpretations of the specified architecture, supported by deductive trajectories, not observations of an implemented SSDS system. Their status is OPEN until the owning D3 process repairs and independently rechecks them. This record is their canonical review home; revisit them against a replacement candidate.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The accepted 7.2.1 owners and stakeholder objectives do not require an impossible machine judgment. The stakeholder decision record, SD-5 and SD-6, accepts bounded realization and explicitly treats complete doctrine realization as an aspiration to test. The defects below belong to the proposed D3 candidate, which §0 expressly does not promote to accepted-current architecture.

This distinction follows the [kernel, Verification and Challenge](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md): “A coherent parent with a wrong child is an ordinary blocker.”

## Verdict

**NO-PASS.** Four D3 blockers remain:

1. **A — report admission:** a report submitted after its task basis becomes stale can be rejected before its existence creates escalation.
2. **B — candidate evaluation:** records-only review of an unmerged, changed candidate has no currency frame compatible with the specified basis rules.
3. **C — publication:** one host's positive no-attempt log cannot exclude another host's earlier publication and a subsequent deliberate reset.
4. **D — development authorization:** §25 requires implemented shadow evidence before the D4 handoff needed to build the shadow implementation.

The earlier S1 revocation defect and self-certified plan-equivalence defect are repaired on the trajectories examined. The signed binding and fail-closed lineage design also address the earlier authenticity and unknown-lineage defects within the declared trust model (§7.5, §15.6). These closures do not close the four blockers above.

## 1. Blockers by earliest owner

### Blocker A — §6.8 step 6 prevents the report-survival rule from taking effect

**Trajectory.**

1. An implementer is issued a legitimate signed task on item revision `I0`; its brief and recorded reads include `I0` (§7.5, §7.6, §9.2).
2. While it runs, the principal lawfully amends that item to `I1`. The old task is now non-current (§7.2).
3. The implementer submits a `HUMAN_QUESTION`, or a material finding, with its authentic task binding, claiming no discharge. Its mechanical minimum basis includes the supplied contract/context at `I0` (§6.4). Choose a substantive amendment with no equivalence or applicable `PLAN_CONTROL` coverage for this report.
4. Admission step 6 checks **every basis entry of every submitted record** against the current head. The report is records-only and changes no content, so the merged-tree exception does not help. Its `content(I, I0)` entry is unsatisfied; the request routes to revalidation rather than admission.
5. §7.9 says the escalation obligation “opens when the record is admitted.” No admitted report exists. Recording the rejected request preserves an audit trace, but no rule routes its embedded report to the inspector. The agent can disappear before resubmitting.

Thus a correctly reported discovery can miss the deterministic human route without a principal downgrade, forged binding, or human acknowledgment. The same currency gate can reject a report from an unchanged task after other supplied context changes, and after a loss boundary withholds a record-mode premise (§6.4, §6.6).

**Violation and owner text.** A8 requires that a material finding survive; §6.8 step 7 says “Reports and challenges are admitted whatever the state of their task, so nothing reported is lost.” That exception occurs after a step that already rejects the request. The accepted [scientific-inspectability owner, Epistemic initiative / Delegated findings](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/scientific-inspectability-and-initiative.md) requires carry-forward: “It may rank and condense, never drop.” Stakeholder SD-2 requires deterministic discovery flow to the human.

**Earliest owner.** The request/basis admission contract, §6.4 and §6.8 steps 6–7, composed with §7.9 Persistence. This is an ingress defect; existence-keyed persistence works once a report has been admitted.

**Minimum repair direction.** Define a report-preserving admission rule that authenticates the binding and retains the original basis as historical provenance without requiring that basis to be current before routing the report. Do not turn stale reported content into current support or discharge. Specify the treatment of reports inside rejected/stale result requests, and derive their required attention from the retained report identities. Extend §22 to submit a report **after** staleness and verify automatic inspector delivery without resubmission. Editing the target **after** report admission tests a different boundary.

### Blocker B — §6.4/§6.6 currency has no frame for pre-integration candidate review

**Trajectory.**

1. The admitted integration tree contains unit `u` at `r0`.
2. An implementer produces candidate commit `C` with `u` at `r1`, where `r1 ≠ r0`, and the change is substantive. Grant that its phase-1 result record is admitted. §7.8 explicitly keeps `C` unmerged.
3. A trusted runner executes checks on `C`, and a fresh reviewer judges that exact candidate (§7.7–§7.8, §9.6).
4. The review's mechanical minimum includes the **judged revision**, `content(u, r1)`, under §6.4. Its records-only request changes no content.
5. S0 still defines `cur(u) = rev(u, T_n) = r0`, because `T_n` comes from the admitted expected integration head (§6.6). In S2, `sat(content(u, r1)) = F`: no equality, tightening, or equivalence covers this substantive change. Admission step 6 therefore cannot admit the review as current; §7.4 cannot discharge it.
6. Integration requires current review judgments before submitting the integrating request (§7.8). The only stated way to make `cur(u) = r1` is therefore gated by the review that cannot become current first.

This is not resolved by the phrase “on the exact candidate.” That phrase identifies the target but defines neither an alternative `cur` nor the satisfaction of candidate-target basis entries. Likewise, step 6's merged-tree exception applies to content **the request itself changes**; the review request is records-only. A record-mode dependency on a candidate realization with changed execution-content entries faces the same issue (§10). Simply omitting the judged revision would violate the mechanical minimum.

**Violation and owner text.** The path contradicts §7.8's required result → review → integration sequence and prevents A7's reviewer requirement from being fulfilled for ordinary changed work. The accepted [architecture owner, D3 formal-contract discipline](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/architecture-and-design.md) requires normative architectural concepts to be defined before dependent invariants use them. The [semantic-definition owner, Definition order and well-definedness](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/semantic-definition-and-traceability.md) specifically requires material “state/time/concurrency semantics needed to distinguish outcomes.”

**Earliest owner.** Basis target/currency semantics (§6.4, §6.6 S0/S2), the step-6 evaluation frame (§6.8), and their use in §7.8. This predates the binding repair; separating binding from discharge alone cannot close it.

**Minimum repair direction.** Distinguish immutable candidate-target identity and candidate-local evaluation from live prerequisite currency. Define which tree each basis entry is checked against for result, realization, review and integration, including records read through other records. Preserve exact candidate binding, external-dependency validation, and merged-tree rerun/re-review requirements. The real §22 discriminator must execute a changed candidate through the complete production result → runner → review → integration path while the product ref stays at `r0` until integration. A fixture that seeds already-current review records would bypass the defective boundary.

### Blocker C — §15.3's no-attempt exception is not safe across Admission hosts

**Trajectory.**

1. Entry `n` is admitted with publication `PENDING`, intent `B_n → C_n` (§15.3).
2. Hosts H1 and H2 both observe that admitted head. H2's private publication-attempt log positively records that it has made no attempt. No exclusive publication ownership is specified; concurrent Admission hosts are supported (§8.2, §15.3).
3. H1 publishes `C_n` successfully, then crashes before appending any successor.
4. A human deliberately resets the integration ref to exactly `B_n`, for example to remediate a security issue. The ledger still has no publication observation.
5. H2 reads `B_n`. Its own intact log still positively shows no attempt by H2. Following the exception, it performs the CAS `B_n → C_n`, reversing the reset without human disposition.

Ledger CAS does not serialize this effect: it serializes the later reconciliation append. The single-provisional-entry rule also does not establish a sole publication executor for an **already admitted** entry. No key compromise or witness fault is needed. If “no attempt was made” is intended to mean no attempt by **any** host, a private host log is not a warrant for that predicate.

**Violation and owner text.** C4 says ambiguity is reconciled before retry. §15.3's revised ABA paragraph explicitly requires honoring deliberate resets and describes “its own publication-attempt log” as the positive warrant. The accepted [concurrency owner, Idempotency and publication](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/concurrency-and-orchestration.md) requires prevention of duplicate logical outputs from concurrent/retried attempts. The archived consolidated plan §14 requires reconciliation of ambiguous external state before retry; its §18.1 successor mapping claims this is carried.

**Earliest owner.** §15.3's publication-effect authorization and ABA exception, with the multi-host execution contract in §8.2. The ordinary ledger serialization and witness-quorum design are not the faulty owners.

**Minimum repair direction.** Permit the no-attempt branch only with a proof covering **all possible publication executors**, including failover and concurrent hosts, or retain the conservative human-disposition route when such proof is unavailable. A bounded exclusive effect-ownership contract may suffice; the author should choose the minimum mechanism. Extend §22's ABA test to two hosts with intact, mutually different logs and a reset after one host succeeds. Merely testing an absent log on a restart host does not discriminate this case.

### Blocker D — §25 makes authorization depend on the implementation it would authorize

**Trajectory.**

1. Phase B passes a repaired design; Phase C produces an independently reviewed, stakeholder-accepted Architecture Manual (§23).
2. Before Phase D can implement the read-only kernel, the engineer requests the D4 handoff.
3. §25 says “D4 handoff is possible only when” **all** listed criteria hold. Item 9 requires the interface to be “demonstrated by live trajectories in shadow mode.” Item 10 requires qualified `HARD` templates, demonstrated verification/escalation properties, and doctrine-realization measurements.
4. Those require the SSDS mechanisms built in Phases D–F and exercised under §22. No such SSDS implementation exists (§0.4). The bounded shadow implementation cannot be authorized, so it cannot produce the evidence required to authorize it.

Using the existing Core or hand-built proxy trajectories cannot demonstrate the new real owners. Treating the requirements as already met would manufacture closure; starting D4 despite the explicit gate would bypass task authority.

**Violation and owner text.** The stated gate is inconsistent with §23's development sequence. The accepted [workflow owner, Workplans as bounded contracts](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md) requires preservation of task-specific acceptance and dependencies. The [testing owner, Proxy-proof real-owner evidence](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md) says evidence that can remain green while the real owner is broken “cannot close that owner claim.” Notably, archived consolidated-plan §34 places analogous implemented-evidence requirements at **cutover/PASS**, not before the first implementation handoff.

**Earliest owner.** §25's acceptance boundary, composed with §23's phase authorization. This is a workplan sequencing defect, not a request to waive qualification.

**Minimum repair direction.** Separate design/Manual closure and authorization for bounded shadow implementation from functional acceptance and native-cutover qualification. Assign every existing mandatory criterion to its actual boundary and preserve all of them. State which Phase C outcome permits which D4 work; a Phase B PASS alone must still authorize none.

## 2. Non-blocking findings

### N1 — historical adoption provenance remains partial

The stakeholder record now preserves the workflow direction, permission-class approval, principle acceptance and aspirational objective. It explicitly cannot reproduce the 2026-10-12 governing-version adoption instruction. §0.1 nonetheless groups N3 among repairs, and the §0 disposition says N3–N4 were repaired. Report this as **partial**, with the remaining route to stakeholder restatement. It does not prevent this review from using 7.2.1: the user-selected handoff explicitly supplies that governing version. It does limit historical claims that the adoption sequence has been independently verified (§0.4; stakeholder record, Not covered).

Earliest owner: the historical authority claim in §0.4 and its status projections. The accepted versioning owner's [Binding versus adoption](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/protocol-versioning-and-compatibility.md) keeps explicit authorized adoption distinct from compatibility and agent judgment.

### N2 — make compound conformance outcomes explicit in the Manual

An undisclosed boundary breach produces both a boundary `VIOLATION` and a faithfulness `DISCREPANCY` (§7.7; also acknowledged in §27.4). §7.7 presents conformance as a class without defining whether hard classes coexist or which has precedence. Both block integration, so no passing path follows from this ambiguity. Nevertheless, both routing consequences must survive; a “first class wins” implementation could omit the integrity finding or amendment route. Resolve the product type and aggregation rule in §21 item 25 and test a compound failure. This is non-blocking for the prospective design because its mandatory rejection and reporting consequences are stated.

The applicable [semantic-definition owner](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/semantic-definition-and-traceability.md), Definition order and well-definedness, requires material piecewise precedence and types to be recoverable.

## 3. Re-verification of FFBAD17 findings

| Prior finding | Disposition | Independent basis at Revision 6 |
|---|---|---|
| **A — revocation relaxed by open counter-challenge/loss** | **Closed for the named defect** | In §6.6, a challenge targeting restrictive `a0` is syntactically a counter-challenge. Its open blocking state is excluded from suspension of `a0`. Dismissing it leaves `a0` in force; upholding it creates a gated relaxer. Withholding that relaxer after loss restores `a0`. An ordinary blocking challenge against the relaxer also restores the revocation. |
| **B — stale/loss-erased escalation; downgrade as discharge** | **Partly closed** | For an **already admitted** report, §7.9 existence-keying preserves attention after target edits and basis staleness; §15.4 withholds old resolving acknowledgments/reclassifications without erasing the report. FINDING has one support tier and downgrade no longer simulates human discharge. Blocker A exposes the missing pre-admission boundary. |
| **C — binding/discharge contradiction; authenticity; unknown lineage** | **Partly closed** | §6.8 separates binding from discharge; §7.5 signs replayable envelopes; UNKNOWN lineage cannot satisfy independence (§9.6). These repair the stated step-7 and provenance defects. Ordinary completion still encounters the candidate-currency cycle in Blocker B, and stale reports encounter Blocker A. |
| **D — open amendment predicates; self-equivalence; cross-scope decomposition** | **Closed for the named defect** | §7.9's whitelist covers all allowed field moves; unknown fields, added obligations and weakening moves are R2. PLAN_CONTROL is a rule-defined order, not an author judgment. Partition restricts execution of one unchanged item and transfers no acceptance. Holistic item review is required except for explicit policy-waived item kinds. |
| **N1 — overclaims** | **Closed as a claim-bounding repair; guarantees still blocked** | §1.1 binds aspiration to SD-6; A6 limits reads to observable ones; §19.2 supplies version-binding/self-adoption enforcement; §0 bounds role enforcement to authenticated bindings. Report-flow adequacy still fails Blocker A. No empirical improvement is established by these statements. |
| **N2 — ABA default** | **Partly closed** | Absent logs and logs showing prior success now fail closed with human attention (§15.3). The positive no-attempt exception lacks a multi-host warrant: Blocker C. |
| **N3 — stakeholder traceability** | **Partly closed** | Workflow principles and bounded objective are recorded explicitly. The earlier adoption instruction remains paraphrase-only: N1 above. |
| **N4 — bidirectional review** | **Closed** | §9.6 adds the required scientific reverse-direction review slot; §0.4 now gives its landing point. Presence is E2, quality remains judged. |
| **N5 — conflicting rebase** | **Closed** | §7.8 routes a non-clean rebase to a new implementer iteration and forbids machinery resolving it. |
| **N6 — mixed Domain force** | **Closed** | §7.7 separates annotated HARD checks from unannotated HEURISTIC inference; each template has one force. |
| **N7 — stale index and old whitespace** | **Open, outside the bounded repair scope** | The SSDS section routes correctly and keeps D4 unauthorized. The inherited Protocol 7/index residue and historical F9D9DE8 whitespace were not repaired; §0.1 explicitly dispositions them. `ffbad17..f3608f5` itself is whitespace-clean. No frozen review was rewritten. |

## 4. Out-of-matrix trajectories and derivation assessment

| Attack | Result and boundary |
|---|---|
| Report submitted only after its context changes | **Fails** before routing: Blocker A (§6.8 → §7.9). |
| Review of changed, unmerged `r1` while integration remains `r0` | **No specified admissible currency path:** Blocker B (§6.4, §6.6, §7.8). |
| Two publication hosts, one successful CAS, deliberate reset, other host's intact no-attempt log | **Fails:** Blocker C (§15.3). |
| Build the first shadow kernel under the literal D4 gate | **Authorization cycle:** Blocker D (§23–§25). |
| Counter-challenge → successful upholding → ordinary challenge → upholding → another counter-challenge | **Holds on unrolling:** polarity is determined from earlier syntax; open counter-challenges do not relax restrictive upholdings. Successful counter-upholdings are gated relaxers (§6.6 S1). |
| Loss with retained non-blocking challenge/upholding and retained dismissal of its counter-challenge | **Holds:** the restrictive upholding remains; the dismissal of the counter-challenge has no relaxing effect (§6.6, §15.4). |
| Already-admitted critical question, target edit, raiser withdrawal, loss after acknowledgment | **Holds:** attention survives; withdrawal annotates; loss withholds the acknowledgment (§7.9, §15.4). |
| Remove escalation/frozen constraints or flip APPLIES to NOT_APPLIES while adding a check | **Blocked from R1 coverage:** whitelist requires R2 (§7.9). |
| Add and then partly remove controls | **Bounded:** comparison is against the accepted revision. A net weakening below that revision is R2; removing an unaccepted tightening while remaining above it is not acceptance of weaker-than-reviewed work (§7.9). |
| Partition to move acceptance to new subjects or skip the required whole-item review | **Blocked under the stated contract:** unchanged item and explicit review/waiver boundary (§7.9). |
| Forge a reviewer envelope; reuse one without its launch credential; manual self-review | **Blocked within trust model:** signature/credential checks and UNKNOWN lineage prevent independence credit (§7.5, §15.6). Compromised trusted keys/adapters are expressly outside that model. |
| Use CLEAN checks or HEURISTIC signals as semantic acceptance | **Blocked:** current reviewer judgment remains required; heuristic signals have no direct disposition force (§7.7–§7.8). |
| Foreign structural promotion under a blocked parent; demotion/restoration with old acceptance | **Blocked:** effective structure/quarantine, source/destination freeze and tenure exclude promotion by presence or revival of old acceptance (§6.1, §6.8, §11–§12). |
| Stale-consistent ledger/product restore after admitted suffix loss | **Holds within witness assumptions:** intersection reveals the later head; recovery records a loss boundary withholding prior support independently of quarantine (§15.4). |
| Simultaneous definitions used to license circular warrant | **Blocked:** only definitional SIMULTANEOUS cycles inside an SDG are legal; mixed/warrant cycles make the subject ill-formed (§6.2). |

**Strata.** Syntactic polarity first recurses toward earlier target records. Once computed, S1 force/continuity recurses toward later resolvers and attestations. These are two finite evaluations, not a negative fixed-point cycle (§6.6). The uniqueness prose should be read as referring to the latter evaluation, not claiming that polarity itself reads later positions.

`r ⊑ cur(u)` can be an S0 constant for a fixed PLAN_CONTROL basis endpoint: comparing the two item contents by a fixed whitelist requires no current plan-acceptance judgment. It therefore preserves the min/max monotonicity of S2. §16.1 also lists amendment *classes* in S3; this is coherent only if that classification uses the lower-stratum order, not if S2 calls back into it. No reverse dependency is required by the stated rule (§6.4, §6.6, §7.9).

Admission reading S3 readiness/conformance is likewise not intrinsically recursive: it evaluates a specified hypothetical request against a fixed admitted head. These structural arguments do **not** solve the missing candidate evaluation frame in Blocker B. No implemented incremental/from-scratch equality or production replay was executed.

## 5. Minimum architecture and capability transfer

The four primitives, one ledger, derivation-based state and seven component ownership boundaries remain a justified candidate decomposition (§5, §15.1, §16.1). The signed task envelope adds a necessary trust boundary without requiring a task-issue ledger entry. The review found no reason to restore the predecessor's four separately canonical graphs, global epoch, whole-plan stop, or graph-transaction synchronization (§3–§4, §17). Component/surface counts alone do not prove simplicity: basis evaluation across candidate and admitted trees, and exclusive publication-effect ownership, are material contracts still missing.

The bounded transfer assessment compared the archived consolidated plan's semantic/control, replay, effects, transport, migration, qualification and acceptance requirements; the befe678 hypothesis's graph, work, concurrency, context, transaction and migration capabilities; and Architecture 1.6.0's 26 product invariants plus public-boundary, persistence, failure and security requirements. §16.2 and §18 retain discoverable dispositions, including obligations genuinely deferred to the Manual. No additional required capability omission was established in those inspected surfaces. **Realization is not lossless yet:** Blockers A–C defeat claimed successor mechanisms; Blocker D moves implemented-evidence requirements to an impossible earlier boundary.

PEM was independently resolved under the project policy, not from candidate temperature or summary alone:

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen historical profiles remain required by the current versioning owner; preserved by section 24 and scoped supersession in section 16.2.
  - id: SP-002
    disposition: APPLICABLE
    reason: Candidate and ledger publication identities remain outside the objects they identify; sections 6.8 and 15.3.
  - id: FF-001
    disposition: APPLICABLE
    reason: Genesis, cutover and replacement-lineage publication must follow validation; sections 12.5 and 15.5.
  - id: DS-001
    disposition: APPLICABLE
    reason: Positive fixture outcomes can bypass the report, candidate and publication boundaries found defective here; section 22 needs discriminators.
  - id: SP-001
    disposition: APPLICABLE
    reason: Derived views remain regenerable from canonical owners; section 6.6. This is an analogy, not a comparative design mandate.
```

Local `main` resolves to the workplan's exact base. Base, candidate and current PEM blobs are identical; no overlay composition is needed. The canonical file has five families, no notices and explicitly PARTIAL coverage. Its `reconciled_through` horizon does not establish absence of later lessons. This review examined the SSDS prior-review family as additional bounded history; it did not reanalyze the entire later 7.x campaign corpus.

PC-001's current mandatory force was verified against the [7.2.1 versioning owner, Orchestration profiles](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/protocol-versioning-and-compatibility.md): “every older supported profile remains frozen and independently testable.” Other HAS entries remain evidence-only. This follows the [architecture owner's mechanism-to-capability transfer contract](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/architecture-and-design.md), rather than preserving historical machinery as authority.

## 6. Qualification-program adequacy

§22 is substantially stronger than a frontmatter or outcome-label matrix: it requires production owners at persistence boundaries, ledger-only publication replay, real trajectories for HARD-template detection/false-positive rates, independent semantic review, and measured doctrine realization. Those are appropriate evidence classes under the [testing owner, Evidence classes and claim scope](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md).

The current cases can still be green while the new defects survive:

- Escalation staleness cases begin with a report already admitted; add stale **ingress** through real Admission (A).
- Phase-1 result admission and “CLEAN without review never integrates” are insufficient; add a positive changed-candidate path through runner, reviewer and integration without seeded current judgments (B).
- ABA variants vary one log's contents; add different intact logs on simultaneous/failover hosts (C).
- Add a dependency/authorization review of the phases themselves; runtime tests cannot repair a pre-implementation gate cycle (D).

§22's general property-generation requirement does not make these discriminators redundant: an implementation can encode the same missing frame or host-local assumption in its generator and oracle. Synthetic models are diagnostic, not independent adequacy evidence. No production owner exists here to qualify, and no reliability gain, detection rate or usability improvement is claimed.

## 7. What was verified and how

- Extracted the exact candidate and immutable governing/historical sources into temporary snapshots without checking out or altering the working branch. The working HEAD was `4d5d0f80f18422f2e1381dc637e8e1afd6ecf2f9`, **not** the reviewed candidate. The primary blob matches the handoff.
- Read the governing D3 entrypoint, architecture and kernel first; activated workflow, semantic-definition, evidence, testing, scientific-inspectability, concurrency, storage, security, versioning, PEM and convergence owners for their material concerns. Conclusions use the immutable 7.2.1 texts, not the working branch's source.
- Inspected `ffbad17..f3608f5` changes and reconstructed the candidate's normative sections, including §0.4, §19 and §24. Self-assessments and prior review conclusions were hypotheses, not warrants.
- Checked release-state identities and owner changes from the historical 6.6 source to 7.2.1. Kernel and semantic-definition repair bases are unchanged; the inspected architecture/workflow/evidence/concurrency/storage/security/testing/versioning deltas preserve their relevant prior contracts and add the named 7.x duties. §0.4 now lands bidirectional review. No new Phase A mechanism regression was found beyond the disclosed adoption-provenance limit.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` on the **candidate snapshot**: **4 tests, OK**. Their docstring explicitly limits them to frontmatter and placement. Python was 3.10.12; Git was 2.34.1. The handoff's literal `python` command was unavailable; `python3` ran the same unittest module.
- `git diff --check ffbad17 f3608f5`: **PASS**. No source, distribution, Core, frozen profile, release-state or PEM change occurs in the candidate's interval from the integrated base.
- Release-state validation: **coherent**. The checked current file is blob-identical to the candidate (`1ba0135f3d34930867041b01fa48f1130970456a`).
- PEM validation in the Git-backed workspace: **schema 1 valid, five families, zero notices**. An initial validation against the detached temporary copy failed because that directory had no Git repository for route realization; rerunning against the identical Git-backed file resolved that environment error.
- Verified predecessor blobs: Architecture 1.6.0 `39e6de727f6c35402962509d30d947962992eaad`; consolidated archive `cc795f4058f99041c751c97ce46e7bcf5483ec9e`; befe678 archive `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958`.

**Impact closure.** This review changes no semantic source, candidate, generated distribution, profile, accepted architecture or release identity. Package/distribution/Core acceptance is unaffected and was not rerun. The proposed design's semantic impact closure remains OPEN because of A–D. Their repairs need a replacement candidate, affected qualification design and independent re-review; this review does not patch or accept them.

## 8. What could not be verified

No named candidate or governing owner needed for these findings was inaccessible. Local immutable objects supplied the material; no GitHub/network access was needed.

The following are **not verified**:

- SSDS runtime behavior, real Admission/Dispatcher execution, witness deployment, crash recovery, measured HARD-template properties, independent replay, usability or doctrine-realization improvement. These are future implementation/qualification obligations, not existing PASS evidence (§21–§23).
- The original 2026-10-12 adoption conversation. The decision record expressly does not contain it.
- An exhaustive losslessness proof over all historical implementation/API details. The transfer assessment is bounded as stated in §5; the detailed API/SPI reuse/supersession decisions explicitly deferred by §16.2 still require Phase C closure. The nine older amendment records were not independently re-reviewed as a new acceptance; the named consolidated predecessor is the comparison owner.
- Independent reproduction of §19.3's numerical campaign summaries, evaluator calibration or frozen-spend conclusions. They were treated as historical evidence inputs, not a measured result of this review.
- The author's exact serving model/build and independently authenticated model-family difference. The stakeholder/handoff describe a different family; this review does not turn that description into verified provenance.

**Scientific inquiry envelope.** This review examined proposed control of evidence, report retention/escalation, candidate review, loss recovery, gate projection and O1 markings. No new scientific execution or selected scientific survivor was produced; local routing tests are structural diagnostics. No project scientific dataset, numerical result or model sweep was analyzed. The materiality basis was whether a locally compliant trajectory changes required human visibility, evidence applicability, authorization or closure. No scientific-result finding or reverse-direction challenge to accepted D1/D2 authority was established in that envelope; this review relies on no such project authority for its verdict, so a D1/D2 tension search was not triggered. There were no delegates. The four blocker trajectories are exploratory architectural counterexamples, not confirmatory scientific measurements or whole-history variant counts.

§1.4 supplies the material control record, readers, routine questions, retention boundaries and visibly marked inspection surfaces. The marks are consistent with stakeholder SD-1, SD-2 and SD-4 at this design level; they do not establish implemented inspectability. **Technical review does not accept any marked surface beyond the requested deliverable.** Such a surface would bind only after stakeholder/task acceptance under the [scientific-inspectability owner, O1–O3](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/scientific-inspectability-and-initiative.md). No retention/projection product change was made by this review.

## 9. Common-mode dependency

This GPT-6/Codex context did not author the candidate. It used an author-written handoff, shared canonical sources, author-selected prior-review hypotheses and the same repository test/validation instruments. These remain common-mode dependencies even if the author's family differs. The out-of-matrix pass departed from the handoff's repaired examples by attacking stale ingress, the unmerged-candidate evaluation frame, host-local publication evidence and phase authorization. Model diversity is not a proof of epistemic independence, as the [workflow owner, Optional independent cognitive trajectories](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md) requires recognizing. Exact serving-build and author-family provenance limits are recorded above rather than invented.

## 10. D4 statement

**SSDS 8 D4 remains NOT AUTHORIZED.** This NO-PASS leaves Phase B open. Repair A–D at their D3 owners, preserve the closed repairs and explicit limitations, and submit a replacement immutable candidate for independent review. A subsequent Phase B PASS would still require an independently reviewed, stakeholder-accepted Architecture Manual in Phase C and a coherent staged authorization boundary before D4. This record creates no ratification, release, recovery, cutover or accepted-current identity.
