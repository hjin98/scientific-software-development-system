# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 7

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: ac71fa92fb16207f4f7bf278ea0573928494d778
    SCOPE: whole prospective architecture; Revision 7 repairs; continued Revision 6 closure;
           workflow execution/verification; persistence, derivation, concurrency, migration;
           Protocol 7.2.1 inheritance; capability transfer and qualification adequacy
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: 8654b3bc4f1aa1dc9f2ca3d8b410f4e704c2320b
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5
           NO-PASS records in qualification/ssds80/
    REVIEW METHOD: immutable-owner reconstruction; formula substitution; concrete
           trajectories; sibling/composition attacks; capability-transfer comparison;
           qualification-oracle challenge; candidate-pinned structural checks
    REVIEWER: GPT-6 (Codex), AI agent /root; exact serving build/minor version not exposed
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-AC71FA9-NO-PASS.md

All workplan section references below identify the primary workplan at the full candidate SHA above. Governing-owner links identify exact SSDP 7.2.1 source at its public-source commit. The observations are facts about the specified contracts; the failure trajectories are deductive architectural counterexamples, not observed SSDS runtime failures. Findings are asserted by this AI reviewer, remain OPEN pending owning D3 disposition, and have this record as their canonical review home. Revisit them against a replacement immutable candidate.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The stakeholder decision record, SD-5 and SD-6, accepts bounded machinery and treats complete doctrine realization as an aspiration to test. The accepted owners do not require machinery to decide arbitrary semantic adequacy. The defects below concern the proposed architecture, which remains unaccepted under §0.

This follows the [kernel, Verification and Challenge](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md): “A coherent parent with a wrong child is an ordinary blocker.” This review neither adopts a different protocol nor challenges stakeholder ownership of product scope.

## Verdict

**NO-PASS.** Three D3 blockers remain:

1. **A — input versus output currency:** an ordinary implementer read of the content it edits makes its result stale in the new candidate frame, even without concurrent change.
2. **B — prospective structure:** candidate frames retain admitted structure, while promotion requires an acceptance in the structural admission. The specified records-only review and subsequent references-only integration do not provide a coherent automatic path for that acceptance.
3. **C — publication after human disposition:** the disclosed head-check/CAS window can extend past takeover and the human’s “keep the base” decision. The original publisher then reverses that decision while its attention item is already discharged.

Revision 7 closes the named stale-report ingress trajectory and the pre-implementation gate cycle. Exclusive publication closes the prior second-host retry defect, but does not close C. Candidate frames supply a review target, but their composition with retained input reads and prospective structure remains inadequate.

## 1. Blockers by earliest owner

### A — §6.4 and §6.9 conflate retained input reads with candidate-output currency

**Trajectory.**

1. At admitted head `n`, subject/unit `u` has revision `r0`. An implementer receives a current contract authorizing a substantive edit of `u`. No other actor changes the head.
2. The implementer reads `u@r0` through `read` to understand the code it will edit. This is an observed read, not an unobservable residual (§9.1).
3. It produces candidate `C` with `u@r1`, `r1 ≠ r0`. Choose a behavioral change with no equivalence between these revisions.
4. The result’s basis necessarily retains `content(u, r0, exact)`: §6.4 assigns content mode to “everything the actor saw,” including read context and change base; recorded reads are unioned into the mechanical minimum, and the actor cannot remove them.
5. The task result declares frame `C` (§6.9, §7.8). Because the head has not moved, `M_n(C) = tree(C)`. In that frame, `cur(u) = r1`.
6. Substitution into §6.6 S2 gives:

   ```text
   sat(content(u, r0, exact)) = F
   current(result) ≤ sat(content(u, r0, exact)) = F
   ```

7. Admission step 6 rejects/routes the result to revalidation. No designated-runner/reviewer/integration sequence can start from a current result. Retrying the same legitimate edit reproduces the failure (§6.8, §7.8).

If the result also carries candidate-target `content(u, r1)`, that entry is satisfied; the original input-read entry still makes their conjunction false. Checking entries against the request’s merged tree gives the same result. An equivalence cannot repair an intentionally substantive change. Omitting the observed read would weaken §6.4 and K1.

**Violation and owner text.** §6.9 says “All of a record’s basis entries are evaluated in its frame,” while §6.4 requires the original read to remain. This defeats ordinary result → review → integration (§7.8) and the minimum-semantic-burden objective (§1.2, A1/A6): legitimate editing cannot require agents to suppress provenance.

The [architecture owner, D3 formal-contract discipline](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/architecture-and-design.md) requires: “define it before dependent invariants use it.” The [semantic-definition owner, Definition order and well-definedness](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/semantic-definition-and-traceability.md) requires material “frame conventions” and “state/time/concurrency semantics needed to distinguish outcomes.” A deterministic value of `F` is not an adequate currency contract for an authorized transformation.

**Earliest owner.** §6.4’s basis purposes and satisfaction semantics, composed with §6.6 S2 and §6.9’s all-entries frame rule. This is D3, not a missing D4 helper.

**Minimum repair direction.** Distinguish the immutable input/base actually consumed, the live prerequisite whose concurrent movement requires revalidation, and the candidate/merged target actually judged or executed. Define their satisfaction before submission and after integration. Preserve recorded reads, exact target identity, external-prerequisite checks and K1; do not simply remove original reads or relabel every stale input as identity. A typed purpose or an equally precise owner-local distinction may suffice without a new store.

The §22 positive production trajectory must include a genuine `read(u@r0)` followed by a substantive edit, and must demonstrate the entire path with that read retained. Sibling cases should include widened context containing the edited unit and a concurrent external prerequisite change.

### B — §6.9 has no prospective effective structure for the promotion/acceptance sequence

**Trajectory.** Grant A repaired; this is an independent problem.

1. Accepted composite subject `P` contains part `A`; `subj(A) = P`. There is no challenge, loss boundary or domain change. The owner proposes a legitimate promotion of `A` to its own subject (§12.2).
2. A candidate changes only the manifest’s role declaration. Its bytes and semantic declarations are unchanged. Promotion must preserve the distinction between a proposal and admitted structure.
3. The independent reviewer follows §7.8: a records-only request on the candidate, before integration. §6.9 defines `D_n[C]` by replacing `T_n` with the merged tree over the **same ledger**. It does not apply a prospective structural delta to `Σ_n`.
4. Therefore `A` is still an effective **part** in that frame. The candidate role declaration differs from `Σ_n`, so it is also a quarantined governance-affecting delta affecting `P` (§6.1, §6.6 S0).
5. An acceptance judgment on `A` is rejected by Admission step 3: acceptance is “only on effective subjects … never on parts.” Its “after the request’s own structural changes” exception cannot help a records-only reviewer request.
6. A review judgment about the part’s content can be recorded, but it is not the required acceptance on `A` in its new tenure.
7. The later §7.8 integration request carries references to admitted records and “no new judgment.” Yet §12.2 and step 4 require promotion and its qualified acceptance **in that same structural admission**. The acceptance needed there could not be admitted through the prescribed preceding reviewer step.

The same gap affects restoration of a demoted subject and adoption of a foreign promotion (§11.2, §12.2). It is not permission to make repository declarations effective early.

The declared-frame whitelist also names review, conformance and assessment judgments, but not acceptance judgments: “Every other record declares the admitted frame” (§6.9). Calling the needed new-subject acceptance a candidate review therefore does not by itself supply its acceptance type, scope or tenure.

**Violation and owner text.** §12.2 requires “Promotion and its acceptance are admitted in one request”; §7.8 says “Every other request follows the same split.” The tree-only frame preserves S11’s safety separation but does not realize the migration path promised by M2/M4 and §12.2.

A combined structural-plus-independent-acceptance admission is suggested by §12.2 and the step-3 exception. It could be the intended solution. The candidate does not reconcile that path with the reviewer’s records-only/write-free role, each record’s authenticated task binding, the references-only integration request, or candidate-frame tenure/subject semantics (§6.8, §7.5–§7.8). A human may be able to assemble a special combined request under its broad permissions; that possibility does not specify the automatic role-relay path, and is not proof that the contracts compose.

The [architecture owner, Current architecture vs cycle decisions](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/architecture-and-design.md) requires the owning acceptance process, “including independent falsification before accepted-current promotion where required.” The [workflow owner, Decision-sufficient handoffs](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md) requires recovery of material acceptance obligations “without hidden chat or unavailable history.”

**Earliest owner.** The structural-acceptance transaction in §6.8 steps 3–4 and §12.2, and its composition with §6.9 and §7.8. This is a material D3 transition-contract conflict.

**Minimum repair direction.** Specify one coherent path for independent judgment of prospective structure and atomic admission of that structure with its acceptance. State the hypothetical scope, `subj`, tenure and quarantine treatment used for the judgment; when its judgment becomes admitted; which task binding carries it; and what the integration request may contain. Retain admitted-only structure, no acceptance of parts, same-admission promotion acceptance, and source/destination challenge freezes. A bounded prospective evaluation/conditional judgment may suffice; no staging ledger is justified by this finding.

Add a production-path discriminator that begins with an effective part and ends with a newly accepted subject, without pre-seeding its acceptance or silently activating its manifest declaration. Exercise restoration and quarantined adoption through the same path.

### C — §15.3’s slow-publisher window can outlive the human’s “keep B” decision

**Trajectory.** This needs neither a forged key nor a second publication attempt.

1. Entry `n` is admitted with intent `B_n → C_n`. H1 is its sole publisher. It durably writes its intent and checks that the ledger head is still `n` (§15.3).
2. H1 pauses immediately after that check, before the product-ref CAS. The candidate expressly permits this residual window.
3. Following its operational takeover policy, H2 observes product head `B_n`, appends and admits absorption `n+1`, classifies `n` as `OVERTAKEN`, and opens human attention. H2 performs no publication CAS.
4. The authenticated human chooses **keep `B_n`**. The judgment is admitted in a subsequent entry and resolves the attention item (§15.3 procedure; §7.9; §9.8). The product ref remains `B_n`.
5. H1 resumes. The procedure specifies no fence or revalidation between the completed head check and its CAS. Its first and only `B_n → C_n` CAS succeeds.
6. The product now contains `C_n` after the human explicitly chose to keep `B_n`. Attention is already discharged. Until another append observes the movement, the ledger still evaluates the kept base. A later absorption can describe the movement but cannot prevent this reversal (§15.3).

H2 may regard H1 as unavailable while H1 is paused or partitioned; operational liveness judgment is not proof that its delayed effect cannot resume. The trajectory obeys the sole-publisher and at-most-once rules. It extends the candidate’s disclosed “publisher slow, takeover appends first” case by allowing the human to answer before H1 resumes.

**Violation and owner text.** The residual defense in §15.3 says the late effect occurs while “the human attention item is already open” and is “never a silent reversal of a reset.” The item need not remain open. The procedure explicitly offers “keep `B_n`” as a disposition, but supplies no condition that makes that decision stable against the known outstanding publisher. Sole ownership and at-most-once execution establish neither revocation of stale effect authorization nor safe completion of that human disposition.

The [concurrency owner, Define the execution state machine](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/concurrency-and-orchestration.md) requires “what state is safe to resume” and “which transitions are durable.” Its Hard rules say: “Do not let task completion race with artifact publication or manifest/state transition.” The [workflow owner, Human gates](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md) says orchestration “cannot self-approve” human adjudication. Recording a human decision is insufficient when the trusted publication path can subsequently perform the effect that decision rejected.

**Earliest owner.** §15.3’s effect-authorization/takeover boundary, composed with the resolving human judgment in §7.9/§9.8. Ledger serialization and quorum mathematics are not the failed owners.

**Minimum repair direction.** Either make a superseded publisher unable to perform the effect, or make a “keep B” disposition non-final until the outstanding publisher’s effect is conclusively settled or fenced. State the linearization/settlement condition and unavailable-publisher behavior. Another ordinary head read only narrows the same race. Choose the minimum mechanism that preserves the human decision; this review does not prescribe a distributed transaction or new ledger lease.

Add deterministic production failpoints **after** H1’s last head check, then perform takeover and admit the human’s keep-base decision before releasing H1. Verify the protected decision remains effective, not merely that a later replay notices foreign movement.

## 2. Non-blocking findings

### N1 — historical adoption provenance remains partial

Revision 7 now prominently states that the 2026-10-12 adoption instruction is paraphrase-only (§0, §0.1). That repairs the earlier overstatement of closure. The stakeholder record’s “Not covered” section still requests restatement; historical adoption provenance remains **OPEN**, non-blocking for this review because the user-selected hand-off explicitly binds it to 7.2.1.

Earliest owner: §0.4’s historical authority claim and its index/status projections. Preserve the limit until the stakeholder supplies the missing decision. The [versioning owner, Binding versus adoption](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/protocol-versioning-and-compatibility.md) requires an “authorized adoption request/decision”; compatibility and agent paraphrase cannot establish that historical event independently.

### N2 — make publication-log integrity and host identity assumptions explicit in the Manual

§15.3 requires an intact write-ahead attempt log and at-most-once execution by one per-host key. §15.6 identifies keys per host, but §21 does not yet spell out same-host concurrent processes, copied/restored operator state, key-preserving host replacement, or what makes a restored log trustworthy as evidence of no attempt.

These are bounded realization obligations, not an additional current blocker: the at-most-once contract is explicit, and the lost-log route already fails closed. Before G1, the Manual should define how the publisher identity and durable attempt reservation satisfy that contract under its actual deployment/crash model (§21 items 6, 14–16). Qualification should distinguish an intact authenticated file from a monotonic record of all prior attempts. Do not claim at-most-once after restoring an older log unless the chosen realization establishes it.

The [storage owner, Crash consistency and integrity](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/storage-and-io.md) requires: “coordinate concurrent writers explicitly.” This note does not duplicate C’s independent cross-host authorization race.

## 3. Re-verification of prior findings

“Closed” below means the stated defect is closed by the proposed contract on the examined trajectory; it does not establish runtime qualification or acceptance of the architecture.

### F3608F5

| Finding | Disposition | Independent basis at Revision 7 |
|---|---|---|
| A — stale report rejected before routing | **Closed for the named defect** | Step 6 explicitly exempts reports/challenges; rejecting a stale result still admits its attached reports. Existence-keyed routing opens attention without resubmission (§6.8, §7.9). The original basis cannot become current support through this exemption. |
| B — no pre-integration currency frame | **Partly closed** | A reviewer can evaluate changed target bytes in `D_n[C]`; the unchanged unit-only example works if its basis contains only candidate-target and unchanged prerequisites. Ordinary retained reads and prospective structure expose A/B above (§6.4, §6.9, §7.8, §12.2). |
| C — another host’s no-attempt log retries a reset | **Closed for the named trajectory; publication family partly closed** | H2 cannot publish H1’s entry. H1’s intent routes a restart at B to the human. The first-attempt delayed-publisher trajectory remains C above (§15.3). |
| D — shadow evidence required before shadow authorization | **Closed** | G1 uses design/Manual evidence; G2 adds a reviewed shadow workplan and explicit authorization; G3 owns live shadow and implementation evidence; G4 owns subject cutover (§23–§25). No shadow implementation is needed to satisfy G2. |
| N1 — historical adoption provenance | **Partly closed** | Status now truthfully says partial; the source conversation/restatement remains absent (§0, §0.4; stakeholder record). |
| N2 — compound conformance | **Closed** | Classes form a set, every routing applies, and §21 item 25 requires aggregation detail (§7.7). An undisclosed breach retains both VIOLATION rejection and DISCREPANCY integrity routing. |

### FFBAD17

| Finding | Disposition | Independent basis at Revision 7 |
|---|---|---|
| A — counter-challenge/loss un-revokes | **Closed for the named defect** | Syntactic counter-challenges do not suspend restrictive adjudications while open. Their successful upholdings are gated relaxers; loss withholds the relief and restores revocation (§6.6 S1, §15.4). |
| B — stale/loss-erased escalation; downgrade as discharge | **Closed for the named defect** | Report-derived attention is keyed to existence; target edits annotate it. Pre-loss acknowledgments/reclassifications lose force. A principal downgrade moves a non-floor report to the visible digest, without simulating human discharge (§7.9, §15.4). Revision 7 also repairs stale ingress. |
| C — binding/discharge contradiction; authenticity; unknown lineage | **Closed for those defects; ordinary work path still blocked** | Signed replayable bindings are distinct from claimed discharge; a result/report may claim none. UNKNOWN lineage cannot satisfy independence (§7.5, §6.8, §9.6). A/B above concern a different composition of that repaired path. |
| D — open amendment predicates; self-equivalence; cross-scope decomposition | **Closed for the named defect** | The whitelist gives a direction for each permitted field; unknown fields and added/removed obligations are R2. PLAN_CONTROL is an order, not an author judgment. Task partition preserves one item and its acceptance; required holistic review addresses joint effects (§7.9). |
| N1 — realization/impossibility overclaims | **Closed as claim bounding, with C still open** | §1.1 records SD-6’s aspiration; A6 limits observable reads; §19.2 specifies version binding; target misclassification and compromised adapters remain disclosed limits. The new late-publication claim is independently inadequate. |
| N2 — unsafe ABA default | **Closed for repeated-attempt ABA** | Non-publisher, attempted or lost-log cases fail closed to human disposition. Delayed first-attempt publication is C, not the original silent retry (§15.3). |
| N3 — stakeholder authority traceability | **Partly closed** | SD-1–SD-7 preserve the workflow principles, permission classes, heuristic interpretation and aspirational objective. The 2026-10-12 adoption event remains N1 above. |
| N4 — bidirectional scientific Review missing landing | **Closed** | §0.4 now rows it, and §9.6 requires the reverse-direction answer for scientific subjects. |
| N5 — rebase conflict handling | **Closed** | Non-clean merges produce no frame and route a new implementer iteration; machinery resolves no semantic conflict (§6.9, §7.8). |
| N6 — Domain force contradiction | **Closed** | Annotated HARD checks and unannotated HEURISTIC inference are separate templates (§7.7). |
| N7 — old index/Protocol 7 status and historical whitespace | **Open, outside this repair scope** | The SSDS 8 index section is correctly proposed/unauthorized. The older index sections and frozen review record were not rewritten. `git diff --check f3608f5 ac71fa9` is clean; that does not attest every historical record. |

## 4. Out-of-matrix trajectories and derivation assessment

| Attempt | Result and boundary |
|---|---|
| Read original content, then edit it without concurrency | **Fails:** A; the frame rejects its retained input read (§6.4, §6.9). |
| Promote or restore a part through the normal independent-review pipeline | **Unclosed:** B; hypothetical structure/tenure and same-admission judgment are not composed (§6.8, §6.9, §12.2). |
| Takeover and human keep-base decision after publisher’s final check | **Fails:** C; the delayed first effect can resume (§15.3). |
| File a human question after its item/context changed | **Holds for authenticated valid report shape:** admission exemption precedes existence-keyed routing (§6.8, §7.9). |
| Carry a material report in a stale rejected result | **Holds:** the rejection still admits the report (§6.8 step 6). |
| Use stale report basis as evidence support | **Blocked by the specified contract:** no rule consumes report basis/currency; resolving records target identity (§6.8, §7.9). |
| File a blocking counter-challenge against a revocation | **Revocation holds:** open counter-challenge cannot suspend the restrictive upholding (§6.6 S1). |
| Withhold a pre-loss counter-challenge upholding | **Revocation returns:** the upholding is a relaxer; cont gates it (§6.6, §15.4). |
| Escape challenge by foreign promotion/reparenting | **Blocked:** Σ stays admitted; aff(Q) invalidates affected subjects; adoption respects both freezes (§6.1, §6.8, §11). This safety result does not establish B’s legal promotion path. |
| Restore identical bytes after a tenure ends | **Old acceptance cannot count:** ACC excludes the earlier tenure (§6.1, §6.6, §12.2). |
| Restore ledger and product to the same stale snapshot after known admitted loss | **Support remains withheld:** quorum detects the later checkpoint; LEDGER_LOSS gates retained permissive records even when Q is empty (§15.4). |
| Cross-subject support cycle or mixed definitional/warrant cycle | **Blocked:** separate support-graph and relation-cycle checks; no warrant from SDG condensation (§6.2, §6.6). |
| Flip scientific flag, remove escalation, add obligation under R1 | **Blocked:** weakening and obligation-set change are R2 (§7.9). |
| Partition to avoid joint review | **Blocked absent an explicit policy waiver:** item-level review is required (§7.9). A policy waiver is visible authority, not the principal’s choice. |
| Pass mechanical checks without semantic review | **Blocked:** CLEAN makes review ready and discharges nothing (§7.7–§7.8). |
| Remove every heuristic signal | **No mechanical disposition changes by contract:** semantic reviewer influence is not claimed inert (§7.7, §22). |
| Reuse a review after both sides changed its judged unit | **Stale target:** merged revision differs; re-review is required (§6.9). This holds independently of A. |
| Manual/Git-envelope review with unknown lineage | **Non-independent:** no discharge of an independence requirement (§7.5, §9.6). |
| Advance versions or rules from repository presence | **Blocked:** admitted S0 adoption/mode facts own those changes; envelope rejects a different declared version (§6.6, §19.2). |
| Restore a retired confidentiality lineage | **Historical only under the stated witness model:** retirement is seen by each read quorum (§15.5). |

**Strata.** S1 polarity follows strictly earlier targets; force/continuity follows strictly later challenges, resolvers, boundaries and attestations. These are two finite evaluations, not a negative fixed-point cycle (§6.6). S2’s min/max system is monotone on the finite F/P/T lattice; PLAN_CONTROL compares immutable item content by the closed whitelist as an S0 constant. Neither amendment classification nor report routing introduces S3 feedback into S2 (§6.6, §7.9).

For a defined merged tree and fixed effective structure, the tree-substitution frame retains that well-foundedness. A concerns the wrong currency result, and B concerns missing prospective structural semantics, not multiple fixed points. Candidate records may be examined under another candidate’s tree only with their actual bases satisfied; no frame designation alone establishes evidence admissibility (§6.9, §10). The Manual must make that contextual evaluation explicit rather than recursively evaluating each dependency in whichever declared frame favors it (§21 items 4–5).

Admission may read S3 once at a fixed head and evaluate a proposed post-state. That is not a derivation cycle provided the proposed state and its structural/record bindings are defined before the decision. B is precisely a missing composition at that boundary (§6.8).

**Impossibility claims.** Observed/effective structure, typed relation-cycle checks and quorum-qualified currentness exclude their stated mechanically represented failures within the trust model (§0, §6.1–§6.2, §15.4). They cannot exclude undeclared prose warrant, incorrect judgments, compromised issue keys/adapters, excessive witness faults or unobservable reads (§1.1, §8.4, §15.6). Those limits are disclosed. Exclusive publisher identity excludes another host’s repeat attempt; it does not make a later human decision stable against a previously authorized effect (C). No runtime implementation was used to substantiate an absolute guarantee.

## 5. Minimum architecture, capability transfer and inheritance

The four primitives remain justified at this design level: unit identity/scope, typed relations, non-derivable records and basis provenance answer distinct governed questions (§5–§6). The seven component responsibilities and canonical/derived/private store separation avoid the predecessor’s competing graph/state owners (§15.1, §16.1–§17). Candidate evaluation needs a hypothetical view; it does not evidently need another canonical ledger. Role binding, verified lineage and exclusive effect ownership also address real requirements (§7.5, §15.3).

Counting unchanged primitives/components does not prove minimum complexity. The repeated currency and publication repairs warrant re-deriving the shared transition contracts before adding further exceptions. This follows the [convergence owner, Active simplification trigger](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md): “simplification/re-derivation is mandatory before another additive durable repair.” No finding here demonstrates that all Git-ledger or witness machinery should be discarded; a smaller owner-local currency/transaction contract may close A–C.

**Capability comparison.** The following pinned predecessor blobs were verified:

| Predecessor | Blob |
|---|---|
| Architecture 1.6.0 | `39e6de727f6c35402962509d30d947962992eaad` |
| Consolidated Protocol 8 archive | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| befe678 hypothesis archive | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |

§16.2 disposes all 26 Architecture 1.6.0 invariants and its named frozen surfaces. The intentional retirement of the ladder, native document completeness and private canonical-store default is explicit; Core/version-bound behavior remains protected. API/SPI, composition-root, containment and Dispatcher detail marked Deferred must still close through the Manual, not by this review (§21, §25 G1).

§18.1 includes consolidated §§36, 37.2a and 38; §18.2 preserves the befe678 distinction between byte-preserving refinement and semantic promotion. No additional capability omission was identified in the inspected transfer surfaces. However, **naming a successor mechanism does not establish equal-or-stronger transfer**: A defeats ordinary stale-result handling, B leaves legal promotion unclosed, and C defeats durable takeover disposition. The corresponding §18 “Carried” claims remain unproven.

**PEM basis and task-local HAS.** Project policy designates integrated main for accepted/base memory. Local main resolves to `af0455753e20ee54a969c844872e29e270007211`, the workplan-bound base. Its PEM and the candidate’s PEM share blob `1561797125622f355f84eb27319f87e8fa4227d9`; there is no SSDS overlay. The validator accepts schema 1, five families and zero notices. Canonical family metadata was inspected, including summary-omitted applicability fields; coverage remains PARTIAL, with no claim that the later 7.x interval is memory-covered (§0.3).

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md
  candidate_overlay_semantic_candidate: NONE
has:
  - id: PC-001
    disposition: APPLICABLE
    reason: Version-bound profiles remain mandatory through the current versioning owner; sections 16.2 and 24 preserve them.
  - id: SP-002
    disposition: APPLICABLE
    reason: Candidate, ledger and checkpoint identity stays outside the object being identified; sections 6.8 and 15.3.
  - id: FF-001
    disposition: APPLICABLE
    reason: Genesis, cutover and replacement-lineage publication follow required validation; sections 12.5 and 15.5.
  - id: DS-001
    disposition: APPLICABLE
    reason: Fixtures can omit retained reads, pre-seed promotion acceptance or miss post-check publisher races; section 22.
  - id: SP-001
    disposition: APPLICABLE
    reason: Derived views are rebuilt from canonical inputs; section 6.6. This is evidence-only analogy, not a preference mandate.
```

PC-001’s mandatory force was independently resolved from the [versioning owner, Orchestration profiles](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/protocol-versioning-and-compatibility.md): “every older supported profile remains frozen and independently testable.” The other HAS entries remain evidence-only. The [PEM owner, Retrieval and HAS](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/project-engineering-memory.md) requires independently resolving accepted/base memory and says “Missing memory is not absence.” No PEM mutation or promotion is performed here.

**7.2.1 reconciliation.** The candidate release-state owner binds the public source and distinct recovery exactly as the header states. Kernel and semantic-definition source are unchanged between the historical 6.6 and governing 7.2.1 refs; the inspected workflow/evidence/concurrency/storage/security/versioning deltas preserve the relevant prior contracts and add the identified 7.x duties. §0.4, §19 and §24 correctly distinguish doctrine, evidence inputs, the pre-cutover baseline and frozen historical versions. The seven archived §37.2a inputs have landing rows in §19.2. Historical adoption provenance remains N1; this review’s explicit 7.2.1 binding needs no inferred adoption.

**Stakeholder/O1.** §1.4 identifies retained control records, readers, routine questions, destructive boundaries and marked inspection surfaces. §9.4 preserves a separable evidence core and semantic gate adequacy; §9.6 lands bidirectional scientific Review. These match SD-1–SD-6 at the intended architectural level, subject to the blockers in their realization. The stakeholder record expressly leaves architecture/Manual acceptance for later. Technical review accepts no marked surface beyond the requested deliverable; such an item binds only through stakeholder/task acceptance under the [scientific-inspectability owner, O1–O3](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/scientific-inspectability-and-initiative.md). No product retention/projection change was made.

## 6. Qualification-program adequacy

§22 appropriately separates mechanical qualification, independent semantic adequacy and measured engineering outcomes. Production-owner failpoints, ledger-only replay, real HARD-template false-positive/detection qualification, signal inertness and calibrated shadow comparisons are materially stronger than frontmatter checks.

Its candidate-frame end-to-end requirement should expose A **if faithfully executed with the required actual read basis**. No such execution exists yet. A generator that omits pre-edit reads/change-base consumption could produce a green proxy while implementing the wrong basis contract. Make that discriminator explicit.

The migration positives can also be green if they directly inject the same-request acceptance, without producing it through authenticated independent review. Exercise B’s entire role/binding/structural transaction, including quarantine adoption and restoration.

The ABA group tests a takeover **before** the publisher’s head check. It does not test takeover and completed human disposition **after** that check. The latter is C’s necessary production failpoint.

The [testing owner, Oracle strength and counterfactuals](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md) asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Its [Proxy-proof real-owner evidence](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md) states that evidence which can stay green while the actual owner is broken “cannot close that owner claim.” DS-001 supports this warning as project evidence, not authority.

The new authorization-boundary review discriminates the old gate cycle: G2’s inputs can exist before D4, and live criteria belong to G3/G4 (§23–§25). Preserve that repair.

## 7. What was verified and how

- Used `git archive` snapshots of the candidate, governing public source and historical repair source in temporary directories. Working HEAD was `806a842cd24d0a8a4444a4c984cdada692361942`; it was not substituted for the candidate.
- Verified the full candidate SHA and primary-workplan blob, release-state public-source/recovery refs, integrated PEM basis/blob and predecessor blobs.
- Entered the pinned D3 role and architecture owner; loaded kernel, workflow, definitions, evidence, testing, scientific-inspectability, concurrency, storage, security, versioning, PEM and convergence owners for the concerns used above.
- Inspected `f3608f5..ac71fa9`, normative candidate sections and the SSDS 8 authority-index section. Prior reviews and self-assessment tables supplied attack hypotheses, not adequacy evidence.
- Executed `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the extracted candidate: **4 tests, OK**. They check frontmatter, file placement and lineage routing only.
- Executed `git diff --check f3608f5 ac71fa9`: **PASS**, no whitespace errors.
- Executed the candidate’s PEM validator with its snapshot as working tree and the existing read-only Git object database: **schema 1 valid, five families, zero notices**.
- Executed the candidate’s release-state validator using the same Git-backed snapshot: **release state coherent**.
- Environment: Python **3.10.12**, Git **2.34.1**.
- Checked changed-path scope from integrated base to candidate: workplans, archives, SSDS qualification records and the routing test. No semantic `source/`, generated `dist/`, Core code/profile, root README/CHANGELOG, release-state or PEM mutation occurs.

**Impact closure.** This review adds only this evidence record. It changes no proposed design semantics, accepted architecture, generated package, profile or release identity. Source/package/distribution/Core acceptance is unaffected and was not rerun. Candidate D3 impact closure remains **OPEN** on A–C. Their repair needs a replacement candidate, reconciled qualification design and independent re-review; the closed historical repairs remain preservation obligations.

## 8. What could not be verified

No required named candidate artifact or governing owner was inaccessible. Immutable local objects supplied the reviewed material; GitHub access was unnecessary. There was no failure to run either hand-off-requested command.

Not established by this review:

1. **Runtime qualification:** real Admission/Dispatcher behavior, witness deployment, crash recovery, publication fencing, measured HARD-template rates, usability and doctrine-realization gains. These are future §21–§23/G3 obligations.
2. **Historical adoption conversation:** the 2026-10-12 instruction remains paraphrase-only, as the stakeholder record says.
3. **An exhaustive historical API/implementation losslessness proof:** transfer assessment covered the named predecessor capability/acceptance surfaces. Detailed Deferred API/SPI and Dispatcher decisions still belong to Phase C. The nine amendment files were not re-reviewed as separate current authorities.
4. **Campaign numerical reproduction:** §19.3’s uptake percentages and calibration/spend history were treated as historical design inputs; this review did not reproduce their raw campaign analyses.
5. **Remote publication currentness:** no remote branch or main fetch was performed. The review is exact-candidate and the PEM base remains the workplan-pinned local integrated identity.
6. **Authenticated model-family/build provenance:** exact serving minor/build and the author’s independently verified model identity are unavailable. No family-diversity proof is inferred from the hand-off.

**Scientific inquiry envelope.** Examined evidence currency, report survival, human decisions, promotion, loss recovery, gate projection and O1 markings. Materiality was whether a compliant path could change retained evidence applicability, required visibility, authorized action or closure. No scientific dataset, numerical output or model sweep was run or analyzed; structural tests are diagnostic. No scientific-result finding or reverse-direction challenge to accepted project D1/D2 was established in that envelope. The verdict relies on no accepted project D1/D2 scientific meaning, so its tension-search predicate did not fire. There were no delegates.

This review prepares architecture-gate evidence and preserves its material findings here. Architectural counterexamples were searched adaptively and are exploratory. No scientific survivor was selected from alternative analyses/models; this is not a whole-history variant count. Earlier campaign selection history was not reconstructed, so no comparative scientific-performance claim is made. No findings or retained evidence were discarded.

## 9. Common-mode dependency

This context did not author the candidate and did not inherit the authoring conversation. It did not reuse the context that wrote F3608F5. It read that record during this review because the hand-off requires independent re-verification.

The stakeholder/handoff describes ChatGPT as a different family from the author. This reviewer is GPT-6/Codex, also the family label in F3608F5; consequently this is **not corroboration by a distinct family from that prior reviewer**. Exact author-family and serving-build provenance was not independently authenticated.

Remaining dependencies include the author-written hand-off’s framing, shared canonical sources, prior-review hypotheses, repository validators and common model/tool assumptions. The new attacks leave the author’s named examples by retaining original reads, testing prospective structure and completing the human decision inside the publication window. That improves the search route but does not establish epistemic independence. The [workflow owner, Optional independent cognitive trajectories](https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md) says: “Separate context improves process independence but not epistemic independence.”

## 10. D4 statement

**SSDS 8 D4 remains NOT AUTHORIZED.** This NO-PASS leaves Phase B open. Repair A–C at their D3 owners, retain the closed report/gate/polarity/amendment repairs, and submit a replacement immutable candidate for independent review.

A future Phase B PASS satisfies only §25 criterion 11. G2 still requires an accepted Architecture Manual, an independently reviewed bounded shadow workplan and explicit stakeholder authorization. G3 needs implementation/production-owner qualification; G4 needs subject-specific cutover and rollback conditions. This record supplies no ratification, release, recovery, cutover or accepted-current identity.
