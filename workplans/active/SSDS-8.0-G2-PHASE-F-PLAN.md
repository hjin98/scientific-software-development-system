---
kind: ssds-shadow-phase-plan
workplan_id: SSDS-8.0-G2-PHASE-F-PLAN
protocol_version: 7.2.1
target_system_version: 8.0.0
status: active (revision 13 after the check of ad8daeb6: 4c-iv admits only ABSORB, F1 and §6 amended; revision 12 placed SD-69's schema correction and adoption path as step 4c-iv and the ledger's repair at step 10; revision 11 adds reading F20, the freeze's regions, after the 2aadf33 review; revision 10 reverted revision 9's split and added reading F19, the outermost owner's content; revision 9 split F18's whole-structure checks; revision 8 adds reading F18 and Q-F7, the reserved leaves; revision 7, after the re-check of efa2c450; revision 6, after the same-family plan review of 96e13c0b; revision 5 split step 4c into 4c-i to 4c-iii with readings F14-F17 and Q-F6; revision 4, after the same-family plan review of b10018de; revision 3 split step 4 into 4a-4e with readings F10-F11; revision 2 after the same-family plan reviews of 07284144 and 53e8c119)
created_date: 2026-10-24
governing_workplan: workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md (revision 3, Stage D, §5.2 Phase F row)
governing_architecture: orchestrator/docs/ssds-8.0-architecture.md (accepted at G1, SD-50; amendments A1-A9 accepted, SD-53, SD-55, SD-60, SD-62)
g2_authorization: SD-55 (shadow implementation only)
previous_phase: workplans/active/SSDS-8.0-G2-PHASE-E-PLAN.md (completed; Review PASS at c2b1ec2)
active_serious_challenge: none
---

Governing SSDP version: 7.2.1.

# SSDS 8.0 — Stage D Phase F plan: Admission and Dispatcher in shadow

```text
STATUS: ACTIVE, revision 13 (step 4c in four parts, §3.1); questions Q-F1 to Q-F7 settled (SD-64, SD-67 to SD-69). Companion to the G2 shadow workplan, Stage D (§5.2 Phase F row). It
        concretizes that row into files, modules and test groups. It adds no mechanism beyond the
        settled register (G2 workplan §4.2) and changes no Manual decision.
START:  the Phase E Review PASS at c2b1ec2 lets Phase F's dependent work start (G2 workplan §5.1 item 5):
        qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-C2B1EC2-DIFFERENT-FAMILY-PASS.md.
SHADOW: no SSDS authority over any subject; every subject LEGACY(p) or UNGOVERNED; no cutover. The
        document-controlled 7.2.1 baseline governs. On the real shadow ledger Admission only observes
        the integration ref the stakeholder designates (Q-F2) and publishes nothing; publication and
        fencing run only against integration refs in fixtures and scratch repositories (reading F1).
DONE SO FAR: step 1 (PERF-E1: each historical position derived once per history); step 2
             (requests, steps 1-2, closed reason codes, input bounds, the secret scan, idempotency, the
             never-lost queue order, a minimal commit path; the fitness revision); step 3a (issue keys,
             signed envelopes, launch attestations with per-task credentials, the binding's
             authentication and lineage, AUTH_ENVELOPE, AUTH_VERSION, AUTH_ACTOR for human bindings,
             human-gated KEY_LIFECYCLE); step 3b (the operator journal; the rendered brief's identity
             in the envelope). Steps 4-8 fail closed (SCHEMA_UNSUPPORTED) until built.
DEPENDS:     Q-F1 to Q-F3 settled by SD-64. The stakeholder-signed genesis of `ssdp-shadow-2` is admitted
             (2026-10-25); the old ledger's retirement statement needs step 7.
NEXT ACTION: steps 4b-ii and 4c-i are closed (PASS at c98bb647 and 1a3c262d); step 4c-ii's
             eight blockers are repaired (revision 11) and under narrow re-check; then 4c-iii. A10 is accepted (SD-66);
             ssdp-shadow-2 is admitted and QUALIFIED
             (qualification/ssds80/PHASE-F-SHADOW-GENESIS-2-EVIDENCE-SSDS-8.0.md), ready for step 10;
             its missing reserved leaves are repaired in place by adoption once Q-F6 (i) is built (SD-69).
```

## 1. Scope and authority

The G2 workplan's Phase F row builds:
- **`admission`:** the validation steps, the witness quorum, publication and fencing;
- **`dispatcher`:** scheduling, envelopes, and designated-runner realizations in sandboxed workspaces without push credentials.

Both compute decisions beside document control, realizing register rows §8-§9, §17 and §22-§25. Its exit evidence for G3 has three parts:
- acceptance group 4;
- the admission halves of groups 2, 3 and 5;
- every material difference from document control, classified (SSDS defect, baseline ambiguity or defect, deliberate stronger rule, unresolved judgment) and independently reviewed.

This file decides only D4 placement and order. Every behaviour cites the register row it realizes; a behaviour no row covers returns to Stage S (G2 workplan §5.6). G2 workplan §5.1 applies unchanged:
- expected values come from the register and the Stage S cases as written, never from running `qualification/ssds80/models/`, and production code never imports them (item 3);
- real owners, including ledger-only replay with the integration host disconnected as the oracle for publication classification (item 4);
- Core's suite and the frozen-profile tests pass unchanged (items 1 and 6);
- no live agent run without an authorized campaign (item 7).

The Phase D threat boundary for the SSDS home (SD-59; Phase D plan §2) holds for every operator file Phase F writes. Everything SSDS writes for an operator lives in the one SSDS home (Manual §26.3, A7), Dispatcher workspaces included. The new operator trees are listed in §2. Steps 2-9 create them only in scratch SSDS homes; their layout in the real home is the stakeholder's to confirm before step 10 (Q-F3; §8).

**What Phase F does not build** (each later phase's, with reason):
- intake, the migration path and external units (Phase G), except SD-69's adoption path: an `ABSORB` adopting quarantined declaration keys, built in step 4c-iv so that step 10 can repair `ssdp-shadow-2` in place (Q-F7). Every other §18.3 disposition, and §18.4's effects of `QUARANTINE` and of contrary dispositions, stay Phase G's;
- adversarial, privacy and fault harnesses beyond the failure points group 4 names (Phase H). §24.2's breach protocol stays in Phase F, as the G2 row places §22-§25 there. Its replacement lineage, re-encoding and private pseudonym mapping run on fixture ledgers only;
- any live agent trajectory or measurement spend, including the Dispatcher's harness route with a real model (a campaign, G2 workplan §5.1 item 7);
- moving any subject to `NATIVE` (a cutover, G4).

## 2. Placement

The component table of Phase D plan §2 stands. Phase F fills owners as follows.

| Owner | Gains in Phase F | Register rows |
|---|---|---|
| `admission` | the request model and its content identity, the queue with never-lost priority (§8.1-§8.2); validation steps 1-9 with closed reason codes (§8.3-§8.4, catalogue §8.3-§8.4), including the one-producing-context refusal (§7.1); absorption (§8.6) and the entry-shape rule (§22.1); the commit point with checkpoint distribution to the witness quorum (§22.4, §23.3); the publisher's incarnation, the publication effect, fencing and settlement (§22.3), consuming Derivation's classification; the human-gated recovery and lifecycle entries (§23.6-§23.8, §24.2's records, §25.2); protected surfaces (§25.3); bounded secret checks and input bounds (§24.1, §25.4) | §7.1, §8, §22.1, §22.3-§22.4, §23 (Admission side), §24, §25 |
| `derivation` | the expected head, publication classification `pub(n)` and `late(n)`, and the re-evaluation an `OVERTAKEN` or fenced admission causes (new runs of the `NATIVE` D1/D2 subjects it changed), read from the ledger alone with ancestry facts injected (Manual §26.1; catalogue §22.3); the head Admission validates against, extended by each appended entry and equal to from-scratch derivation; §17.4 admissibility and currency (deferred from Phase D); the §10.2 obligations §17's machinery triggers (`REALIZE`, `ASSESS`, `RERUN`, `READING`); the cited-premise support-graph component check Admission's step 5 calls (Phase D NF2); the loss boundary and `REQUALIFY` | §5-§7, §10.2, §17.4, §22.2, §23.6 |
| `dispatcher` | issue keys, signed task envelopes with lineage classes, launch attestations and per-task submission credentials (§12.2); the operator journal, which an issue key's retirement lists from (§25.2); issue from derived readiness bound to a named `H*`, with serialization surfaces, one coordination task per plan and per-worktree leases (§9.1-§9.2, K2); judge selection outside the authors of `W` in a fresh context, recording lineage, model family, route and toolchain (RR-11, §16.5); suspension and resumption; integration requests and mechanical retry (§26.1); designated-runner execution in a sandboxed workspace (reading F2) and the `REALIZATION` observations it submits (§17.2, §17.3, §17.5), with external custody on fixtures | §9, §12.2, §16.5, §17.5, §26.1 |
| `ledger` | witness checkpoint writing for the witness kinds Phase F uses (append-only Git refs and append-only directories); authenticated retirement statements (Phase D NF3) | §21, §23.3 |
| `interface` | `submit`, `report` and `decide`, which build typed requests for Admission (§16.1); `open(task)` bound to an envelope, read recording, `ask(changed)` and the brief's digest in the envelope (§16.4); the MCP server and the Git-envelope transport (§16.10, Phase E reading E11), the latter writing run refs only in scratch repositories | §16.1, §16.4, §16.10 |
| root module `ssds.cli` | mounts `submit`, `report`, `decide`, and the long-lived processes `admission serve`, `dispatcher serve` and `mcp serve` under the Manual's names (§26.3); wires the tree source into the Dispatcher's runner (the Dispatcher does not import `content`, fitness rule F5) | §26.3 |

**New operator trees**, each inside the SSDS home under the SD-59 boundary, created only in scratch homes until the stakeholder confirms the layout (Q-F3):
- the issue and runner keys, under `keys/`;
- the operator journal and leases, under `state/<ledger id>/`;
- runner workspaces, under a `runs/` root outside every ledger's operator tree. `Home.check` walks only a ledger's operator tree (`ledgers/<id>.git`, `witness`, `keys/admission`, `genesis/<id>`, `state/<id>`), so `runs/` is not refused today. It gets its own containment check (workspaces only under `runs/`; links resolved inside the workspace; nested repositories allowed there).

Admission's host key is already a Phase D tree, and Admission generates it (Phase D reading 12). An Admission incarnation keeps no state on disk (§22.3).

**Fitness (revision of Phase D rule B1).** Phase D's B1 lets only `content` and `ledger` start processes and only `ledger.append` run Git write subcommands. Phase F adds four named exceptions, each with a synthetic violating module in the fitness tests. Each writing exception has a target the composition root supplies and a run-time check that refuses the governed product repository as a target:
- `admission.publish` may run the integration ref's compare-and-swap and write fence commits;
- `interface.envelope` (the Git-envelope transport) may write run refs, in scratch repositories only;
- `dispatcher.runner` may start a runner process, only inside a workspace it materialized under `runs/` (reading F2);
- `dispatcher.harness` may start a harness process, a stub only without a campaign (reading F8).

Two restrictions also hold: only `admission` imports the append path, and only `dispatcher` holds an issue key or a runner key. Admission reads the observed integration ref through a `content` reader the composition root supplies, so it starts no process of its own.

## 3. Steps, in order

| Step | Modules | Realizes register rows | Tests (under `orchestrator/tests/ssds/`) |
|---|---|---|---|
| **1** derivation cost (done) | `derivation`: a workflow at a position is built once per history and shared (`Workflow.historical`, reading F7) | §5, §10.4, §13.7 | `test_phase_e_review.HistoricalDerivationCost`: 5 distinct positions derived once (31 builds without the cache). Measured on the PERF-E1 history: round 7 from 12.5 s to 1.6 s |
| **2** requests, early checks, minimal commit | `admission`: request identity and idempotency (§8.1), the queue with never-lost priority (§8.2), steps 1-2 (schema, secrets, reference, the one-producing-context refusal of §7.1; §8.3), closed reason codes (§8.4), input bounds (§25.4); a minimal commit path (one host, `LOCAL_TRUST`, no publication) so that idempotency and recorded decisions are testable from here on; the fitness revision above, written first | §7.1, §8.1-§8.4, §24.1, §25.4 | an identical request returns the recorded decision and appends nothing; a never-lost-only request is not queued behind one needing revalidation; each reason code from a case that triggers exactly it; `SECRET_DETECTED` on each pattern family and on high entropy, not on digests; oversize inputs refused; the S2 binding cases (a second producing context refused, `REF_*`); the fitness violations |
| **3** envelopes and keys | `dispatcher`: issue keys, envelope signing, lineage classes, launch attestations, per-task submission credentials, the operator journal, the rendered brief's identity in the envelope (§12.2, §16.4, §25.2); `admission`: the binding's authentication, `KEY_LIFECYCLE` registration, rotation, retirement listing outstanding envelopes, compromise from a position (§25.2). `open(task)` and read recording move to step 8, where task routes exist | §12.2, §16.4, §25.1-§25.2 | an envelope under a retired, uncompromised key admits only the never-lost records it lists; a compromised key's later envelopes refused; `UNKNOWN` lineage credits no independence; `AUTH_VERSION` when a record's `governs` differs from its envelope's (Phase E E1) |
| **4** authorization to currency | `admission`: steps 3-6: authorization, including independence and adjudication eligibility (§5.10 (f), RR-11) and supersession authority by the superseded kind; structure on the merged tree; dependency well-formedness with the cited-premise component check; currency with never-lost salvage. Also protected surfaces (§25.3) | §8.3 steps 3-6, §8.5, §25.3 | group 3's admission half: 51070e5 N3 (the adjudication-independence refusal); f03b15e N5 (supersession authority); 6b986de N6 (one definition of each independence input for every record kind, at Admission); S1 objection cases at Admission. Group 2's admission half: 798b2b4 B4, 29da56e N5 and 124b0b7 N2 with the records involved admitted, and never-lost challenges, failing assessments and adjudications admitted whatever the request's fate. `AUTH_PROTECTED` on each protected surface |
| **5** legality and regression | `admission`, and `derivation` for the rebase: once Q-F6 (iii) is settled, step 2's rebase check and §7.6's rebase counting (a frame-`X` record counts for `X'` only where every entry holds there, structural records also needing `Δ_Σ(X') = Δ_Σ(X)`), with `transformation_of` and the enactment learning `X'` from the records carrying it; step 7 (one result per task, result-only `HARD` templates, SD-26 one integration per enactment, answered obligations, revision assessments first, the judged-content support check replacing `STALE_RETAINED`, claimed discharge with conformance at head on the merged tree) and step 8 (no collateral evidence regression, R15). Also lint enforced when a plan unit is admitted (Phase E E5), and the refusals Phase E deferred: answers to decisions not derived, including a dropped part's, and invalid partitions | §8.3 step 2's rebase clause, steps 7-8, §7.6 rebase, §13.3 | group 5's admission half: S5 §8 `rejected_request_salvages_never_lost`, `unclean_result_refuses_passing_judgments`, `clean_request_admits_all`; the refusal of a candidate bound to an obligation no longer derived; `same_key_other_scope_after_issue` and the judged-content cases. The cases that need step 9 run after it: regression that needs §17.4 (a fall from `T` to `P` refused) and claimed discharge with affected evidence rerun on the merged tree. The settled-fence check runs after step 6 |
| **6** commit, publication, fencing | `admission`: step 9; the single-ref compare-and-swap; at most one provisional entry; the checkpoint quorum; absorption (§8.6) and the entry-shape rule (§22.1); the publisher's incarnation, the publication effect, fencing absorption, settlement, the ABA policy and the takeover wait (§0.6, a policy key); crash recovery by request identity (§22.4). `derivation`: publication classification, the expected head, the re-evaluation after `OVERTAKEN` or a fence, and the extended head. `ledger`: witness writing | §8.3 step 9, §8.6, §22, §23.3-§23.4 | group 4 through ledger-only replay with the integration host disconnected and deterministic failpoints: S5 §22 `publication_classification`; S5 §23 `deployment_classes_sound` at genesis and redesignation; 362af9f N6 (re-application of a fenced or `OVERTAKEN` integration); 61cd09b N6 (a kept fence and the D1/D2 re-gating); 441cf5c N7 (a rewind is `ROLLBACK`); 730490d N2 (a foreign return to `B_n` is `LATE_PUBLICATION`); 8a75346 N2 (a crash after the CAS, before the outcome is recorded); the entry-shape barrier; a records-only admission never fenced (reading F1). The five S3 kept-fence cases, with the kept-fence conditions and P7 added to the lifecycle check (Phase E E15). The extended head equals from-scratch derivation over every Phase D and E fixture ledger. Each extension builds a new `History`, never mutating one, so step 1's per-history cache stays sound (it is keyed by position on an immutable `History`). A records-only admission whose observed ref is then rewritten to a commit not descending from `C_n` is `OVERTAKEN`, and `LATE_PUBLICATION` if a later observation reaches it, with expected values from Manual §22.2 (the Stage S model has no fence case) |
| **7** loss and recovery | `admission`: `LEDGER_LOSS`, `FORK_RESOLUTION`, `WITNESS_SET_REDESIGNATION`, `REPLICA_REDESIGNATION` and `LINEAGE_RETIREMENT` with `obs = null` (§22.1); `LINEAGE_MIGRATION`, `REDACTION_NOTICE` and retirement statements (§24.2); `CONTINUITY_ATTESTATION` (§23.7); `derivation`: the loss boundary and `REQUALIFY` obligations | §23.5-§23.8, §24.2 | S5 §23 `loss_bounds` and `qualification_states` at Admission; each §23.8 table row as a fixture history; a stale-consistent restore resurrects nothing; a fresh clone (§23.5); a witness-set redesignation over a provisional entry (§22.4) |
| **8** scheduling and transports | `dispatcher`: issue from derived readiness bound to a named `H*`; serialization surfaces and one coordination task per plan; per-worktree leases (K2); scheduling of the joint-invariant review obligations Derivation already derives (§9.2); judge selection (RR-11, §16.5); suspension and resumption; integration requests and mechanical retry. `interface`: `open(task)` bound to an envelope, read recording (§16.4) and `ask(changed)`; the MCP server and the Git-envelope transport, run only against scratch repositories | §9, §16.5, §16.10, §26.1 | at most one mutating task per serialization surface; lease expiry changes scheduling, never correctness; an overtaken basis revalidated, never silently admitted (§9.1); a judge chosen outside `W`'s authors, its lineage recorded; a Git-envelope round trip in a scratch repository, with no ref written to the product repository |
| **9** runners and evidence | `dispatcher`: a designated runner materializes the exact tree in the content model's representation in a sandboxed workspace (reading F2), records its declared execution attributes and unpinnable reads, enforces the runner class's time bound (the system cap of 168 h), and submits `REALIZATION` observations with canonical outcomes and template parameters (§17.2-§17.3, §17.5; Phase E E6); external custody on fixtures; runner-class designation lint (Phase E E20). `derivation`: §17.4 admissibility and currency, and the realization-triggered obligations | §17 | group 1's runner half: the CRLF, mode, symlink, gitlink, LFS and submodule fixtures materialized by a runner. Group 2: the S5 §6 matching cases with realizations admitted. A fixed-attribute mismatch is inadmissible; an incomplete realization enters no assessment; agent-reported results are never admissible. The sandbox tests of reading F2. Step 5's cases that depend on step 9 rerun |
| **10** shadow operation | first, `ssdp-shadow-2`'s in-place repair (SD-69 Q-F7): the stakeholder commits the `ssds.manifest` and `ssds.policy` declarations to the observed branch's manifest, the absorption quarantines them, and a human R2 records-only request adopts both by `ABSORB`: one disposition per declaration key of the two units, validated together (4c-iv). It is admissible once 4d, 4e and step 5 exist and step 6's commit path holds on the real ledger, meaning its single-ref compare-and-swap and the `LOCAL_TRUST` witness checkpoint (a records-only admission has no publication and is never fenced, F1). `ssds.policy`'s scope is the policy path genesis names. The absorbed content's authorship is `UNKNOWN` and the same human commits it, so the `ABSORB` is non-independent: §18.4 enacts it at S0 regardless, and §8.3 step 3 classifies dispositions without refusing them. After it, `Σ` declares the three reserved leaves; then, on the real shadow ledger, with the observed ref of Q-F2: `admission serve` observe-only (reading F1); `dispatcher serve` issuing nothing and writing no run ref; records-only requests through `submit`, `report` and `decide` | §8.6, §16.1 | after every command: the product repository's refs, reflogs, objects and status unchanged; each observed head absorbed (an absorption records the head, so the commits between become reachable); a restart after a records-only admission appends no fence; a candidate request through the library API, the Dispatcher or a transport refused at Admission's entry, appending nothing |
| **11** difference study | the comparison Q-F1 settles, as a qualification harness calling the real Admission owners outside the ledger (§7) | §5.2 Phase F exit | per Q-F1 |
| **12** exit | assembly of group 4 and the admission halves of groups 2, 3 and 5; the end-to-end shadow run | §5.2 Phase F exit | the groups' results; the shadow boundary checked after every command |

### 3.1 Step 4 in five parts (revisions 3-4)

The step 4 survey and the plan review of b10018de found that nearly every predicate §8.3 steps 3-6 need is computed by a derivation owner, but only for records already admitted. The admitted-only owners are `Judgments.nonind`, `judged_authors` and `root_authors`, `State.status1`, `StructureFacts.well_formed`, `Support.current` and `sat`, the support graph's components, and `Conformance`. Some of these are not yet what the Manual says:
- `nonind` is recomputed in every state, where §5.10 (f) fixes the classification at admission, and it lacks the SD-48 owner exception, which only `RouteEligibility` applies;
- `Conformance.writes` compares base with candidate, where §1.2's one write set compares `T_n` under `Σ_n` with `M_n(X)`.

These predicates have no owner yet:
- supersession authority;
- the §12.3 role-to-kind table;
- the decision class of a challenge chain (§12.4);
- prospective tenure in a frame;
- the challenge freeze;
- the enactment condition;
- the per-key effective-structure classification;
- the discriminating reading's class and contradiction;
- "a consumer of a unit";
- the warrant relations of `CYCLE_WARRANT`;
- the new-or-grown component check;
- the `REISSUE(envelope)` obligation.

Step 4 is built in five parts, 4b and 4c each split further (revisions 5 and 12), each closing with its tests and a same-family review of its delta before the next starts.

**Fail closed, for every request shape and every route.** A check not yet built never admits:
- A request that passes everything built is `SCHEMA_UNSUPPORTED`.
- Never-lost salvage admits a record only when every check that record owes exists, so until 4b only reports with an empty `supersedes` are salvaged. Even these still owe two 4b checks: the envelope's obligation and role, and the lineage closure. The exposure is bounded: a report changes no closure, and its binding's obligation only routes it (`reports.py`). Every other never-lost record (adverse judgments, failing assessments, challenge-tier records, any record whose `supersedes` is not empty) is refused by identity as `SCHEMA_UNSUPPORTED`. The plan review's probe showed that before this, an `IMPLEMENTER`-bound `REVIEW NO_PASS` was salvaged and superseded another task's judgment: a step 3 defect, repaired first in 4a.
- Until 4c-iii, a request with candidates or adopted deltas, and any record declaring a frame other than the admitted one, is `SCHEMA_UNSUPPORTED` at any step after authentication: 4a and 4b handle records-only requests without deltas. Adopted deltas stay so until Q-F6 (reading F16).

**Rejection or refusal.** Every code of steps 3-6 rejects the request; its never-lost records are still salvaged when their own checks pass. The one code that refuses a record alone is the refusal of an ineligible `ADJUDICATION` (catalogue §8.3 step 3, §5.10 (e)): the rest of the request is judged as if the adjudication were absent.

| Part | Owner | Builds | Cases |
|---|---|---|---|
| **4a** salvage restriction, trial extension, derivation repairs | `admission`, `derivation` | the fail-closed salvage above; `trial(chain, entry)` (reading F10) for records-only requests; `nonind` classified from the facts at the record's admission, in the record's frame (its judged content and their authors as the ledger knew them there, a candidate's content authored by its transformation's makers, the policy then in force), with the requirement on every disposition of a failing assessment and the SD-48 owner exception for the owner's reassessment, `IMMATERIALITY` or `UPHELD` adjudication of a challenge against it, and the common-mode dependency shown in the inspector; `UNKNOWN` lineage never disjoint (reading F11) | the review's probe as a regression; a trial equals the state derived after admitting the same entry, except the facts keyed on the trial entry's digest (reading F10); a trial changes no held state; a `COMPLETENESS` non-independent at admission stays so after a member moves (the review's fail-open); an owner disposition under the exception is independent |
| **4b-i** authorization (§8.3 step 3), records-only | `derivation` facts and the §12.3 role templates (`derivation.roles`), `admission.authorize` | the envelope's obligation exists at the request's base and was issued for the role that obligation's kind holds (`AUTH_ENVELOPE`; otherwise nothing under it is salvaged); the §12.3 role templates as data (`AUTH_ROLE_KIND`; schema 1's `TASK_RESULT` outcomes are the §12.3 ones since SD-67, with `INCOMPLETE` permitted by no role until Stage S settles it); the floors of catalogue §3.5 and policy's acceptors through `Support.qualified` (`AUTH_ACTOR`); acceptance targets in the admitted frame: the subject's current triple, never a part, never `REVOKED`, never ill-formed or with a declared term `ABSENT` (`AUTH_TARGET_PART`, `AUTH_TARGET_REVOKED`, `AUTH_ILL_FORMED`); supersession authority by the superseded kind, on catalogue §5.10 (b)'s per-kind supersession target (`derivation.supersession_target`; `AUTH_SUPERSEDES`); the bound record's lineage equal to the attestation closure computed from the attestations of the binding objects admitted records name, empty under `UNKNOWN` (reading F11; `AUTH_ENVELOPE`). Failing closed (`SCHEMA_UNSUPPORTED`): records declaring a candidate's frame, adjudications, discriminating readings, product-scope acceptance (its policy-designated authority), lifecycle-tier records, an acceptance of anything but the current triple (`AUTH_TARGET_NOT_CURRENT`) or of a subject no longer effective (`AUTH_TARGET_NOT_EFFECTIVE`) are refused under SD-68's codes; and supersession of a plan acceptance (its target holds only while its basis does) or of a principal's decision (the plan's identity owner). When salvage is withheld (the envelope's obligation or role, an invalid base, a content request), each never-lost record is recorded as refused. Salvage admits reports, their supersession now authorized | one case per code; each check, reverted alone, fails its test |
| **4b-ii** authorization, the rest | `derivation` facts, `admission` checks | adjudication eligibility (catalogue §5.10 (e), §3.5): an `ADJUDICATION` is admitted only if it is independent of its chain's root authors, by the one classification of 4a, and its class is not lower than the chain's (§12.4: the highest class of any support-tier or adjudication record in the chain, challenges carrying none; a Serious Challenge or a chain holding a human record needs a human). The chain's class has one owner, `Judgments`, which judge selection reads too. An ineligible adjudication is refused alone (`AUTH_ACTOR`): the rest of the request is judged as if it were absent. A never-lost record under a retired, never-compromised issue key's envelope that the retirement does not list is refused by identity (`AUTH_ENVELOPE`), its bytes retained in the entry by content identity (inert: S0 never reads them), and derivation derives `REISSUE(envelope)` for the Dispatcher (R0), open until a record citing that refusal as its provenance is admitted (catalogue §8.3 step 3, §10.2); the Dispatcher's resubmission is step 8's. Moved, failing closed meanwhile: a discriminating reading's class and contradiction (§6.8) to step 9, whose runners produce the realizations those readings read; `HUMAN_ATTESTED_FRESH` through a `LINEAGE_ATTESTATION` to step 8, with the routes it serves | 51070e5 N3, f03b15e N5, 6b986de N6; S1 objection cases whose distinguishing step is an Admission refusal; a refusal alone leaves the rest of its request's decision unchanged; `REISSUE` derived and discharged |
| **4c-i** the frame at the head, and the two shared owners | `derivation` | the frame of an unintegrated transformation built at the admitted head `n`: `M_n(X) = merge3(tree(B), T_n, tree(C))` and `Σ_n ⊕ Δ_Σ(X)` (§7.2), read by `Conformance` (which builds its frame at its result's position today; §7.5: "evaluated in `D_n[X]`: the conformance of `C`"), `REVIEW(X)` derivation and Admission; the tree and structure facts of an integrated enactment's frame fixed at its integrating admission's head, while its frame records' currency is the admitted state's (reading F17). One **write-set owner** on the frame: `T_n` under `Σ_n` against `M_n(X)` under `Σ_n ⊕ Δ_Σ(X)`, with both sides' governance modes (§1.2). `Conformance.writes`, `changed_files` and `uncovered_outside` read it, as Admission's `AUTH_WRITE_SCOPE` will in 4c-iii; every other conformance template states which tree it reads (§14.1 names "the base and candidate trees"): the write-set templates (`outside_scope`, `owners`, `uncovered_outside`, the protected-surface template) resolve regions, owners and scope on the frame's two sides, `T_n` and `M_n(X)`; the artifact and frozen-interface templates keep `tree(B)` and `tree(C)`. One owner of the bound contract's write scope, the item revision's with a part's share restriction (§13.7), that `Conformance.contract` and `AUTH_WRITE_SCOPE` read. One **protected-surface owner** (reading F14) that `Plans.protected`, `Conformance`'s `protected_surfaces` template and Admission's `AUTH_PROTECTED` read. `id(X)` computed by one function exactly as §7.1 states, A included (the `‖` concatenation and `A`'s element form fixed in its docstring; every fixture computing `"ssds.transformation.v1|B|C"` rebuilt); derivation does not recognize a submitting result whose `target.transformation` differs from it | a write a concurrent admission since `B` made, outside scope on `T_n` and absent from the base-to-candidate set, is not in the write set, and an effect arising only where `C` meets it is; conformance of one pending result read at two heads; conformance of an integrated result unchanged by later heads, an overlapping later edit included, with its required-evidence assessment read in the admitted state; each protected surface touched by path and by unit; `id(X)` with and without `A` |
| **4c-ii** the structural validation owner (§8.3 step 4 (a)-(c)) | `derivation` | one function of the head state and `X` returning `Σ_{n+1}`, the per-key classification against `Q_n` and the step 4 codes. **Per key:** a key outside `Q_n` takes `decl(M)[k]` (authored); `decl(M)[k] = Σ_n[k]` realigns; `decl(M)[k] = decl(T_n)[k]` carries the quarantine; any other value of a key in `Q_n` routes to revalidation (`STRUCT_REVALIDATE`). Adoption by `ABSORB` fails closed (reading F16). **Well-formedness, together over `Σ_{n+1}` on `M`:** §1.9's static checks, the resolution of newly declared or changed file and span terms (`TreeView.unresolved_declared_terms`, then genesis's one owner too), scope conservation for a refinement, and the reserved leaves of §1.8 declared, each with its reserved kind, `ssds.unclassified` with the empty prefix (A9, SD-61; one owner that genesis, every admission and `Frame.exists` read, replacing genesis's own check; reading F18) (`STRUCT_*`, reading F15); no membership change mixing governance modes (`STRUCT_MODE_MIXED`; a cutover `X` carries fails closed until Phase G); SDG members kept together; a change of an existing unit's kind or owning domain fails closed (reading F16). **Freeze:** a subject whose signature, scope, regions or membership the change touches while its current triple in the admitted state `D_n` (never the frame's merged revision) is `BLOCKED`, `PROVISIONAL` (an overridden blocking challenge) or `REVOKED` (`State.status1`): `FREEZE_SOURCE` where it loses or changes, `FREEZE_DESTINATION` where it gains. **Semantic structure:** S0 defects that an affected subject has in the frame and not at the head (reading F15), under their `RELATION_*` names, with SDG, cycle and single-definer defects as `STRUCT_*` members. **Where a frame exists, `Σ_n ⊕ Δ_Σ(X)` equals this owner's `Σ_{n+1}`.** A key in `Q_n` that `C` authors to the value a foreign change put on `T_n` would be carried by catalogue §8.3 4 (a) but is a proposal in the frame by Manual §7.2 ("in the frame the proposal's declarations are not quarantined"). That case routes to `STRUCT_REVALIDATE`, so no frame exists and the request is rejected. Read alone, Manual §7.2 and §7.6 would enact the key as authored: the refusal is a fail-closed stronger rule pending Stage S, which takes the catalogue's precedence, and the difference study classifies it so (§6). `Frame.exists` is a clean merge with no code from this owner (§7.4: every step 4 check except enactment); §7.4's cutover source-mode condition moves with cutover to Phase G, since derivation folds every `MODE_TRANSITION` at its own admission | one case per code; a quarantined key carried, realigned and changed, and authored to a foreign change's value (no frame); a foreign absorption that makes an affected subject ill-formed neither refuses the request nor ends the pending frame, while a second same-code defect the request adds there is refused; a reserved leaf dropped or narrowed; a frame that no longer exists derives what a conflict derives |
| **4c-iii** content and structural requests in Admission | `admission`, `derivation` facts | the submitting request (§11.5): records declaring frame `X` judged on the trial in `X`'s frame, with step 2's revision check keyed on each record's frame rather than on `candidates`. **Frame identity:** a record whose declared frame or `target.transformation` names no transformation an admitted or co-submitted result fixes is refused (`REF_TRANSFORMATION`); schema 1's `frame` field is only `{transformation}`, so it cannot carry a rebase's `(B', C', A')` and the transformation rebased (catalogue §8.3 step 2): a record declaring a rebase frame is indistinguishable from one naming an unknown transformation and is refused `REF_TRANSFORMATION` (Q-F6 (iii)); a lifecycle-tier record declaring a frame (a cutover `MODE_TRANSITION`) stays `SCHEMA_UNSUPPORTED`. **Prospective tenure:** every subject of `Σ_n ⊕ Δ_Σ(X)` is read at the frame's triple, so an acceptance in `X`'s frame of a subject `X` creates, restores, rescopes or rekinds is judged against the frame (`AUTH_TARGET_NOT_CURRENT`, `AUTH_TARGET_NOT_EFFECTIVE`; catalogue §8.3 step 3, §7.4, §7.5); the trial of an integrating request with `Σ_{n+1}` and a tree source holding `M_n(X)`; a `renamed_from` whose source unit had another kind is `SCHEMA_UNSUPPORTED` (F16); step 3's `AUTH_WRITE_SCOPE` (the write set within the bound contract's write scope, and plan units, contracts and verification rules outside every role's scope except as §12.3 assigns them) and `AUTH_PROTECTED` from the 4c-i owners; step 4's codes from the 4c-ii owner; the **enactment condition** on an integrating request (`ENACTMENT_MISSING`: every promotion or restoration carries a prospective acceptance that counts for the tenure it starts, read by `Support.binds_tenure`'s conditions 1-4 before admission, so the check does not depend on step 7's `OBLIGATION_REENACTED`; a cutover fails closed until Phase G). `STRUCT_REVALIDATE` rejects the request with its code and derives nothing more until step 5's routing reads it. A request passing steps 1-4 stays `SCHEMA_UNSUPPORTED` (steps 5-8 not built); committing a merged tree that is not `tree(C)` is step 9's | one case per code; an adopting request fails closed; a write outside scope on the merged tree that the base-to-candidate set misses refused `AUTH_WRITE_SCOPE`; an acceptance of a subject the frame creates is not `AUTH_TARGET_NOT_EFFECTIVE`; a frame record naming an unknown transformation refused |
| **4c-iv** intake adoption (SD-69 Q-F6 (i), (iii); §18.3-§18.4) | `ledger` schema 1, `derivation`, `admission` | **The schema-1 correction, in place (SD-69).**<br>- `INTAKE_DISPOSITION` and `INTAKE_CLASSIFICATION` targets become `delta` (`{absorption, key}`) or `content_ref`, with `units` dropped.<br>- The `identity` basis gains the same `delta` type.<br>- The outcomes become §18.3's, and a `QUARANTINE` carries `paths`. Only `ABSORB` of a quarantined delta is admitted in Phase F. Every other §18.3 outcome is `SCHEMA_UNSUPPORTED` until Phase G builds its effects (a `QUARANTINE`'s S2 effect, contrary dispositions and the realignment they derive, §18.4), and the never-lost adverse ones are refused by identity (§3.1).<br>- `frame` gains optional `base`, `candidate`, `adopts` and `rebases`, present together. The rebase they serve is step 5's.<br>Fixtures that build intake records on `units` targets are rebuilt.<br>**The adoption path.**<br>- The `INTAKE` obligation is keyed by the quarantined delta it names.<br>- A transformation's `A` is the set of deltas the request's `ABSORB` dispositions adopt, and §7.1's `id(X)` covers it. Until Stage S fixes the canonical element form (SD-69), each element is `{absorption, key, value}`: the absorption entry's digest, the declaration key and its quarantined value, sorted by canonical JSON. No ledger holds an `X` with a non-empty `A`, so a later Stage S form changes no admitted fact. A records-only adoption is `X = (B, B, A)` and is judged as its own transformation's frame record (catalogue §8.3 step 6).<br>- The 4c-ii owner classifies an adopted key as authored (`Σ_{n+1}[k] := decl(M)[k]`), validated exactly as if authored (§18.4: freezes, mode consistency, SDG integrity). §18.4 also needs "a prospective acceptance bound to the same admission for any promotion". So a records-only adoption that promotes or restores a subject fails closed (`SCHEMA_UNSUPPORTED`) until the enactment condition is built for every admission that changes `Σ`. Step 10's repair adds two new leaves and promotes nothing.<br>- Admission admits an `INTAKE_DISPOSITION` only on an intake object for which an `INTAKE` obligation was derived, and a `QUARANTINE` only naming that object's paths.<br>- Admission refuses an `ABSORB` of a delta on which an adverse disposition stands.<br>- A records-only adoption (`C = B`) changes `Σ` by its `adopted_deltas` alone, recorded `ADOPTED`.<br>Mechanical adoption of governance-neutral deltas (`intake.neutral_auto`) stays off and unbuilt: it is the Dispatcher's (step 8). | one case per refusal; an adopted key validated as authored, a freeze at its destination included; a records-only adoption folding into `Σ`; an `ABSORB` refused under a standing adverse disposition; a non-`ABSORB` outcome refused; a promoting adoption fails closed; `id(X)` with `A` in the interim element form |
| **4d** dependency (§8.3 step 5) | `derivation` | the static support graph (§5.6, items 1-4, the cited premises of item 4 included: Phase D NF2): every non-trivial component of the trial is a subset of some component at the head (`CYCLE_SUPPORT`); warrant cycles over §2.4's relation set `E` that the request's records would close (`CYCLE_WARRANT`); challenge-tier targets strictly earlier and of permitted kinds, a challenge of a challenge only as a counter-challenge of a restrictive adjudication, no `validity` entry on a record's own subject or a part of it, no equivalence relying on a consumer of its unit: these four have no code in catalogue §8.4 (Q-F5), so until Stage S fixes them a challenge-tier record or equivalence that would need them stays `SCHEMA_UNSUPPORTED` | the mutual-acceptance configuration refused on both grounds; a cycle that absorbed content created is reported and blocks no unrelated request |
| **4e** currency (§8.3 step 6) | `derivation` values, `admission` routing | each basis entry of each submitted support-tier record other than a report evaluated entry by entry on the head's `Support` in the record's frame: `D_n`, or the frame state of `X` at the head built directly from `X` as the trial gives it, with frame and roles passed explicitly (reading F10); otherwise `STALE_BASIS`; a request carrying content or structural changes evaluated as a frame record of its own transformation; the never-lost exemption with salvage to a fixed point | group 2's admission half: 798b2b4 B4, 29da56e N5 and 124b0b7 N2 with the records involved admitted; a before-image entry on a unit a concurrent change moved is stale in `D_n[X]` |

After 4e, a request passing steps 1-6 is still `SCHEMA_UNSUPPORTED` until step 5 builds steps 7-8.

Each step closes with its tests, Core's suite, `run_models.py --seeds` (unchanged), the repository suite and `git diff --check` before the next starts. Under the review allocation, each step that changes behaviour ends with a same-family review of its delta. Phase F ends with an independent implementation Review (G2 workplan §5.1 item 5), which the stakeholder asks for.

## 4. Acceptance groups: cases and discriminators carried

Expected results come from the register row and the Stage S case's stated outcome, transcribed into the test as literal data with the case name cited. A group not executed is reported as unexecuted, never as passed (Manual §31.2).

| Group | Stage S cases carried | Review-named discriminators carried in Phase F | Deferred, with reason |
|---|---|---|---|
| **4** admission, publication, currentness, loss | S5 §14-§25: `publication_classification`, `deployment_classes_sound`, `loss_bounds`, `qualification_states` (Admission side; the read side is Phase D's) | 362af9f N6, 61cd09b N6, 441cf5c N7, 730490d N2, 8a75346 N2 (step 6) | faults beyond these named failure points (Phase H) |
| **2** admission half | the records of S5 §6's histories admitted at Admission | 798b2b4 B4, 29da56e N5, 124b0b7 N2 (steps 4 and 9) | none |
| **3** admission half | S1 objection cases whose distinguishing step is an Admission refusal; the RR-11 resolver and Dispatcher half (steps 4 and 8) | 51070e5 N3; f03b15e N5; 6b986de N6 (step 4) | none |
| **5** admission half | S5 §8: `rejected_request_salvages_never_lost`, `unclean_result_refuses_passing_judgments`, `clean_request_admits_all` (step 5); the five S3 kept-fence cases (step 6) | the refusal of a candidate bound to an obligation no longer derived (step 5) | none |
| **1** runner half | the representation discriminators of 3540d98 B1, e2154ac B1, e9e6e9f B1, materialized by a designated runner (step 9) | — | none |

**Carried from Phases D and E** (Phase D plan §8; Phase E plan §1 and §6):
- the cited-premise cycle enforcement (step 4);
- recovery authorization and authenticated witness retirement (steps 6-7);
- designated-runner materialization and custody (step 9);
- `REALIZE`, `ASSESS`, `RERUN` and `READING` (step 9);
- the refusal of answers to non-derived decisions, which closes Phase E §6's "reviving a dropped part" (step 5);
- `report`, `submit` and `decide` (step 10);
- task envelopes, issue keys, launches, lineage attestations, suspension and resumption (steps 3 and 8);
- the transports (step 8);
- PERF-E1 (step 1).

Phase E items that stay at their owners and fail closed (§6 below): the late objection's review identity, the brief functions listed in Phase E §6, overlapping partitions, findings-only discharge (E30), the doctrine pin's public-source resolution (E37), and the digest's acknowledgment boundary (E38).

## 5. Readings

Each reading resolves a point the register leaves to D4. It is revised, never silently changed, when a step or its review falsifies it.

- **F1** *The real shadow ledger observes; it never publishes.*
  - **Observed ref.** The integration ref the real shadow ledger observes is a deployment setting, not a genesis fact: the genesis record names no integration ref. The stakeholder chooses it (Q-F2). `main` cannot serve as it stands: it sits 435 commits behind this branch and does not contain the genesis baseline, so its first observation would absorb a tree going backwards.
  - **Observe-only.** On the real shadow ledger Admission is built observe-only, without a publisher or a fence capability against the product repository (fitness revision, §2). It reads the observed ref as `obs`, records each new head as an absorption (§8.6), and admits records-only requests.
  - **Records-only admissions.** A records-only request has `C_n = B_n` and no effect (§22.2). It is `PUBLISHED` when the observed ref shows `C_n` or a descendant, and is never fenced. The catalogue §22.3 procedure ("fences if the ref shows `B_n`") is read as applying to an admission with an effect. This is a candidate clarification for the next Manual amendment batch, not a change of mechanism.
  - **The shadow boundary's check.** A request with a product effect on `LEGACY` or `UNGOVERNED` subjects is not refused by the Manual (catalogue §19.1: such changes arrive as ordinary commits and are absorbed). On the real shadow ledger, then, the composition root installs an observe-only policy at `admission.request`, before validation, whatever route brought the request (library API, interface, Dispatcher, transports). It refuses:
    - any request whose candidate differs from its base, including a tree-unchanged carrier that would still publish a commit;
    - any record whose checks belong to a later phase, such as `MODE_TRANSITION` (Phase G), so that no records-only route touches modes (G2 workplan §2 item 1). The one exception is SD-69's: a records-only request (`C = B`, no publication) whose only structural effect is adopting quarantined declaration keys by `ABSORB` (step 10's repair, 4c-iv). It moves no governed ref and writes no governed file, and the units it declares take genesis's `LEGACY` or `UNGOVERNED` modes, so the shadow boundary holds (G2 workplan §5.1 item 2).

    Each refusal is logged in operator state. It is a check of the shadow boundary (G2 workplan §5.1 item 2), recorded nowhere in the ledger, so §8.3's "appends or rejects with recorded reasons" is untouched for requests that reach validation. It is not an Admission decision or reason code.
  - **Group 4.** Publication, fencing, settlement and the ABA policy are exercised where Admission does publish: fixture ledgers with integration refs in scratch repositories, two incarnations constructed in one test.
- **F2** *The runner sandbox.* A designated runner's workspace is materialized from the content model's tree representation (§1.5), never as a worktree or checkout of the product repository. Its location is Q-F3; `Home.check` refuses symbolic links and nested repositories inside the SSDS home, which a materialized tree and test fixtures carry, so the workspace root cannot simply sit inside it. A runner process:
  - starts with a scrubbed environment and its own `HOME`;
  - has no SSH agent socket, credential helpers or tokens;
  - cannot read the operator trees (keys, the ledger, the witness, the journal);
  - has network access denied by default, an unpinnable read when a runner class declares it (§17.5).

  Denying reads of operator trees to a process of the same user needs an operating-system sandbox, a runtime dependency the stakeholder decides on (Q-F3). Until then real-runner execution is limited to fixtures that hold no secret. Step 9 tests each property.
- **F3** *Witnesses.* The real shadow ledger keeps its genesis witness model, `LOCAL_TRUST` with one file witness. That witness sits in the same SSDS home, so its "another medium" premise is not established (Phase D Review of 39fe39b); status views say so. `TEAM` and `HARDENED` quorums, read repair and redesignation run on fixture witnesses only.
- **F4** *Keys and incarnations.* Admission generates its own host key (Phase D reading 12). Issue and runner keys are trust roots. On the real shadow ledger `dispatcher serve` issues nothing (F8), so Phase F needs none there. When a campaign does, they come by genesis declaration or a stakeholder-signed `KEY_LIFECYCLE` record (Q-F2). Without envelopes, `submit` and `report` on the real ledger are human-authenticated only. An Admission process takes a random incarnation identity per start (§22.3) and records it in every entry. No incarnation state outlives a process, so a copied home authorizes no publication.
- **F5** *Human gates.* A human-gated record is signed with a registered human key in the SSH signature format, namespace `ssds` (§25.1), as the genesis approval was. Tests use fixture keys and never the stakeholder's key.
- **F6** *Reason codes.* The closed list is catalogue §8.4. A needed refusal with no code returns to Stage S (G2 workplan §5.6).
- **F7** *PERF-E1.* A workflow at a position is a function of the history's prefix (§5), built once per history and shared, never computed from current state. The selector, settlement and lifecycle discriminators stay unchanged, as the re-Review of c2b1ec2 asks.
- **F9** *Bindings and credentials (step 3a).*
  - **Envelope.** It has the catalogue §12.2 fields, without `retained` (dropped, RR-2), and is signed by an issue key under `keys/dispatcher/<ledger id>.ed25519`.
  - **What a bound record names.** Its `binding.envelope` is the digest of the stored binding object: the envelope, its signature and the launch attestation. Admission stores that object with the admitted records, so replay reads the binding from the ledger alone.
  - **The per-task credential.** It is an Ed25519 key whose public half the launch attestation names; it signs the request without its binding. `ATTESTED_FRESH` is proven only by that signature, and no secret enters the ledger.
  - **Human bindings.** A human binding is an SSH signature (namespace `ssds`) over the same message.
  - **Lifecycle approvals.** A human-gated lifecycle record's approval is kept in its provenance and signed over the record without it.
  - **The secret scan.** It exempts whole values whose grammar is an identity or a signature: a human key fingerprint, a key id, an armoured SSH signature.
- **F10** *The trial extension (step 4).* Admission judges a request through the owners derivation already has, not by restating any rule for unadmitted records.
  - **What the trial is.** A new `History` over the readable prefix plus one unsigned **trial entry** (not §22.4's provisional entry), discarded after the decision. The held head, every cached workflow and the ledger are untouched.
  - **What differs from admission.** The trial entry has no signature, so no digest. These facts at its position are keyed on an entry digest and differ from the state after admission:
    - run identities at an event with no enactment (`runs.py`);
    - `SPEC_REVIEW` and `JOINT_INVARIANT` obligation identities (`workflow.py`);
    - item change facts (`items.py`);
    - query listings (`queries.py`).

    No decision of steps 3-6 reads them: step 6 reads values at the head, which has no such position, and steps 3-5 read records' own facts. Every other fact equals the state derived after admission.
  - **What each step reads from it:**
    - steps 3 and 5 read the records' own S0 and S1 facts from the trial, where the records exist: authorship, lineage, `nonind`, targets, status and the support components;
    - step 6 is evaluated entry by entry on the head's `Support` in the record's frame, with the frame and roles passed explicitly (4e). This keeps catalogue §8.3's "at the current admitted head" literal. A co-submitted record is no node at the head, so it never satisfies another record's basis entry. This is narrower than step 7's discharge predicate ("after the request's own records") and disclosed as such: a completeness attested beside the acceptance it bounds, or an assessment submitted with its realization, needs two requests;
    - the obligation's existence and role read the request's base (step 3); the freeze and earlier-target rules read the head.
  - **Fixed point.** A record refused at any of steps 3-6 is removed and the trial rebuilt, at most once per record, with every refusal of a round computed together. Refusals stay within the rejection-or-refusal scope of §3.1, so the result is one entry that accepts or rejects.
- **F11** *Independence inputs come from the authentication (step 4b).* Lineage is what the binding proves (Manual §12.2):
  - **`ATTESTED_FRESH`.** A bound record's `binding.lineage` must equal the **attestation closure**: the attestation's session, then, recursively, each input session and the input sessions of that session's own stored attestation. A superset is refused: derivation reads a producing record's lineage as the authors of what it produces, so extra tokens would plant authors (re-check 6e0fa9e NB-2). The cost is that a record whose closure was computed before an input's attestation was stored is refused, and recorded as such. Admission computes the closure only from the attestations of binding objects that admitted records name, each verified when admitted; no other stored object is read, and a session two bindings attest differently stays open. An input session with no such attestation leaves the closure open, recorded as `UNKNOWN`, which is never disjoint from anything.
  - **Order.** The closure is compared in its one canonical order: the attestation's session, then the other sessions sorted, then `UNKNOWN` when the closure is open.
  - **`UNKNOWN`.** The recorded lineage must be empty.
  - **`HUMAN_ATTESTED_FRESH`.** It stays refused (`AUTH_ENVELOPE`) until its `LINEAGE_ATTESTATION` path is placed.

  A bound record whose lineage differs is refused (`AUTH_ENVELOPE`). Derivation reads lineage both for independence (`nonind`) and for the authors of produced content (`State._makers`), so S0 reads no lineage that Admission did not authenticate.
- **F12** *Attestations are not requalified (NB-3).* A `NON_AUTHORSHIP_ATTESTATION` or `LINEAGE_ATTESTATION` has one effect: the classification of the record it names, fixed at that record's admission, an S0 fact no loss boundary gates (catalogue §5.3, §5.5; §5.10 (a): "a later attestation does not change it"). So derivation derives no `REQUALIFY` for it after a boundary. P5 still holds, because the record it classified is itself withheld and requalified. The catalogue's §3.4 table and §5.4 polarity row read as if attestations were withheld until requalified. But §23.6's requalifying kinds include no attestation, so such an obligation could never be discharged. That textual tension goes to Stage S.
- **F13** *A recorded producer's attestation (step 4b-ii).* Manual §5.10 (f) admits a human as independent when it "must not be one of them or must present a `NON_AUTHORSHIP_ATTESTATION`", and the catalogue's correction for a false attestation is a challenge against the record it credited (§5.10 (a)). So Admission does not refuse an attestation from a human the ledger records as a producer: the attestation is that human's claim, and contesting it goes through the challenge tier.
- **F14** *Protected surfaces in the tree (step 4c).* §25.3's list is: the ledger, the rules registry, the policy unit `ssds.policy`, schemas, trust roots, witness configuration, unit governance state and issued envelopes. Of these, only the policy unit can be in a candidate's tree. The others live outside any product repository: in the SSDS home, the ledger and the system version (§25.3: the registry ships "with the SSDS system, never in a project repository"; A7). Unit governance state is admitted ledger state (catalogue §1.6: "content proposes; admitted records enact"), and the manifest's structural declarations are ordinary content (§25.3). So the in-tree owner covers the `ssds.policy` unit, the policy file and the entries policy lists. A candidate cannot reach the rest. Their only route is a record, which 4b-i's `AUTH_ACTOR` and `AUTH_ROLE_KIND` and the human-gated lifecycle kinds guard, besides the home's containment and the Dispatcher's write path. This repository's own `schema.py` is product source, not the running system's schemas.
- **F15** *Which ill-formedness refuses a request (step 4c).* §2.5 refuses a request "whose merged tree would make an affected subject ill-formed". "Would make" is causal: Admission refuses a request when a subject in its write set has, in the frame, an S0 defect, keyed by code, unit and detail (stable identities: the ascending relation, the defined object, the cycle's component; genesis keys its own check the same way), that it does not have at the head. So a second defect of a code a unit already has is new. A defect the request neither creates nor changes, on an affected subject or not, is left to S2 (`ok = F`), as §2.5 allocates "a violation that reaches the tree otherwise" (an absorption, §8.6). `Frame.exists` reads the same difference, so a foreign absorption that makes a subject ill-formed does not end every pending frame touching it. The static checks of §1.9 run on `Σ_{n+1}` as a whole: an ill-formed structure has no affected/unaffected split. The `STRUCT_*` members are each §1.9 check's error code (`STRUCT_<code>`), with `STRUCT_TERM_UNRESOLVED`, `STRUCT_RESERVED_LEAF`, `STRUCT_MODE_MIXED`, `STRUCT_MANIFEST_UNPARSED` (a fail-closed guard: the merge already refuses an unparsed manifest), `STRUCT_SDG_MALFORMED`, `STRUCT_SDG_NOT_LAMINAR`, `STRUCT_ILLEGAL_CYCLE`, `STRUCT_SINGLE_DEFINER` and `STRUCT_REVALIDATE`. Scope conservation for a refinement has no code of its own: it is §1.9's containment and sibling-disjointness checks (`STRUCT_CONTAINMENT`, `STRUCT_SIBLING_OVERLAP`) with the residual part taking the remainder (§1.4 rule 2). Catalogue §8.4 delegates each family's member list, closed per schema version. `STRUCT_MODE_MIXED` refuses a membership change across modes even when a non-cutover `MODE_TRANSITION` exists, since that record arrives only on its own human-gated entry; this fails closed and is disclosed. So does the detail key: a request that shrinks an existing illegal cycle without removing it changes the defect's detail and is refused.
- **F16** *What schema 1 cannot express fails closed (step 4c).*
  - **Adoption: a schema-1 transcription defect.** A transformation's `A` is "the exact set of quarantined structural deltas its producing request adopts by `ABSORB` dispositions" (§7.1, §18.4). Catalogue §3.4 gives `INTAKE_DISPOSITION` the target "quarantined delta or observed content" and the §18.3 vocabulary (`ABSORB`, `RECONCILE`, `SPLIT`, `ARCHIVE`, `RETAIN_AS_EVIDENCE`, `MARK_GENERATED`, `QUARANTINE`, `REJECT`, `DISPOSABLE`), and its basis "`identity` on the absorption entry and delta key" (catalogue §4 table). Schema 1 instead has the target `units|content_ref` and the outcomes `ADOPT ABSORB REALIGN QUARANTINE REJECT`, and its `identity` basis targets (record, triple, unit revision) cannot name a declaration key. So no disposition can say which delta it adopts, and nothing links a request's `adopted_deltas` to an `ABSORB`: the same class of defect as Q-F4's. A request with a non-empty `adopted_deltas`, and a submitting result whose `target.adopts` is not empty, are `SCHEMA_UNSUPPORTED`. A quarantined key changed to a third value routes to revalidation.
  - **Release by the old domain owner.** §8.3 step 4 (a) needs "a judgment by an actor qualified for its *current* domain" before a unit's kind or owning domain changes. No record kind, target or field says that a judgment releases a unit. A change of an existing unit's kind or owning domain is `SCHEMA_UNSUPPORTED`. A new unit's kind is authored and needs no release.

  The first is the stakeholder's (Q-F6 (i)), the second Stage S's (Q-F6 (ii)). The release check reads units declared on both sides, so a rename by `renamed_from` or a delete-and-recreate escapes it (review 2aadf33 N5). Within one request, a rename removes the old unit, whose former kind then enters the write set, and the domain rule (§13.2) confines that removal to the old domain's `AUTHOR` item for D1-D3. Step 4c-iii also fails closed on a `renamed_from` whose source had a different kind. Stage S's release record must close the route by lineage. Neither arises in agent work in shadow, where no agent submits. Under Q-F1 (a) the difference study will meet observed kind or domain changes refused `SCHEMA_UNSUPPORTED`; those are classified as fail-closed artefacts, not document-control defects.
- **F17** *Where the frame is read (step 4c).* §1.2 computes the write set "at the admitted head `n` where each check runs", and §7.5 evaluates conformance in `D_n[X]`: for an **unintegrated** transformation (a pending candidate, its `REVIEW(X)` derivation, Admission and §7.5's other readers) the frame is built at the current head, so a pending result's conformance changes as the head moves exactly where `M_n(X)` changes. An **integrated** enactment's frame **tree and structure facts** are fixed at its integrating admission's head `k - 1`: `M_{k-1}(X)`, its structure, the write set, the changed files, `Frame.exists` and the conformance templates' tree inputs. Read at a later head, `M_n(X)` of an integrated `X` is `T_n` (an empty write set) or a conflict (no frame), and either would reopen settled work, against §10.4 (an integrated item relies "only on its latest integrated enactment's review") and SD-40 (no `REVALIDATE` for an integrated enactment's review or task result). **Currency is not fixed:** after integration the enactment's frame records take catalogue §7.3's admitted-state column (before-images a fixed fact, output and context entries ordinary currency in the admitted state; `validity`, `record`, challenge-tier and loss-boundary facts in the admitted state), since discharge is not latched (§10.4, SD-36). So `Conformance._current` and `required_evidence` read an integrated result's records in the admitted state, never in a frame rebuilt at the head. `Support.binds_tenure` reads currency at `k - 1` for §7.6 condition 3 alone, which concerns the integrating admission itself. `queries.impact` keeps its own comparison of the workspace under `Σ_n`: it is a query about an uncommitted workspace with no `X`, and it reads no frame.
- **F18** *The reserved leaves (step 4c-ii).* Manual §1.8: "Genesis declares the reserved leaves `ssds.manifest`, `ssds.policy` … and `ssds.unclassified`", and refuses a genesis without `ssds.unclassified` on the empty prefix. §1.9 checks "the reserved leaves of §1.8 declared" on every admission.
  - **The gap.** The program's genesis check enforced only the refusal clause (`genesis_structure_problems`). So `ssdp-shadow-2`'s genesis, signed on 2026-10-25, declares `ssds.unclassified` but neither `ssds.manifest` nor `ssds.policy` (read through the program). Neither unit is supplied implicitly: `Structure` holds only declared units, and the write set's `ssds.manifest` entry is §1.2's rule for manifest bytes, not a declaration.
  - **How 4c-ii applies it.** The owner applies §1.9 as written, to `Σ_{n+1}` as a whole: all three declared, each a top-level leaf subject with no members ("reserved leaves") and its reserved kind (`MANIFEST`, `POLICY`, `UNCLASSIFIED`: catalogue §1.8 and `SYSTEM_UNITS`; Manual §1.8 names no kinds), `ssds.unclassified` on the empty prefix (`STRUCT_RESERVED_LEAF`). A composite `ssds.unclassified` would hide its bytes in its residual part (review 2aadf33 B5). Requiring `ssds.manifest` and `ssds.policy` to be top-level adds to Manual §1.8, which makes only `ssds.unclassified` the outermost owner. It follows catalogue §1.8's "three reserved leaves", and kinds already forbid a reserved leaf from being a part. It fails closed. The genesis check becomes the same owner, so a future genesis without them is refused.
  - **No unit carries it.** The check belongs to Admission and `Frame.exists` only. S0's `well_formed(s)` and S2's `ok` are unchanged, so no subject on `ssdp-shadow-2` becomes invalid in the admitted state through it.
  - **Frames read the same checks.** Manual §7.4: a frame exists only when "the proposed structure is well formed (every structural check except the enactment condition)", so `Frame.exists` reads every finding of the 4c-ii owner. The whole-structure checks apply to `Σ_{n+1}` as at Admission, and S0 defects are read causally as F15 states. Enactment is excluded because frame records satisfy it; no frame record can supply a missing leaf.
  - **Fixtures.** The test fixtures' in-tree manifests declare the three leaves. This makes their inputs conform to §1.8; it is not a change of expected values.
  - **On `ssdp-shadow-2`.** Every request whose `Σ_{n+1}` still lacks the two leaves is refused, and no frame exists there until Q-F7 is settled. A request authoring them passes: they are `⊥` in both `decl(T_n)` and `Σ_n`, so they lie outside `Q_n` and are authored (§8.3 4 (a)). This changes nothing in Phase F, where no agent submits content and absorptions do not run step 4. Under Q-F1 (a) the difference study reports it as this genesis deviation, not as a property of each observed change.
  - **Open.** What to do with `ssdp-shadow-2` is the stakeholder's (Q-F7).
- **F19** *The outermost owner's content (step 4c-ii).* Declaring `ssds.unclassified` (A9) exposed a content-model gap that no fixture had met.
  - **The gap.** Its one empty-prefix term resolves to every governed byte. Today's model hashes a unit's content over its terms' resolutions (`TreeView.content`) and attributes to it the semantic declarations of every unit inside its region (`TreeView.sem`). So its revision changes with every change, and it enters `Δ(X)` of every transformation. Every review's judged content then needs a content entry on it, and `units_in` counted it as touched by every write scope.
  - **The reading.** Manual §1.8 (A9) makes it "the outermost owner of every governed byte no other top-level unit contains", and §1.4 gives "bytes no unit owns" to the uncovered region. So its content is what it owns by innermost ownership (§1.4 rule 3, `TreeView.owned`): its revision hashes exactly those bytes and no other unit's semantic declarations, and a write scope meets it only where it meets those bytes. Every other unit is unchanged. The write set already keys on owned bytes (§1.2).
  - **Effect on admitted facts.** Before this, `ssds.unclassified` appeared only in some genesis JSON. `ssdp-shadow-2` declares it, but no admitted record names its revision.
  - **Its content, in place.** Per file it owns bytes of, its content is the ordered sequence of owners: its own pieces with their bytes, every other owner by identity only, with the file's mode. Moving another unit's bytes past its own is a change; an edit inside another unit is not (review 2aadf33 B4). Every reader of its region (write set, derived `IMPORTS`, write-scope containment, `owners`, protected surfaces, lint) reads those bytes.
  - **For Stage S and the next Manual amendment batch.** Catalogue §1.5's formula (`content(u) = H(cid(t_i))`; `sem` over every unit inside `scope(u)`) does not single out the outermost owner, and Manual §1.5 leaves "its content" undefined for it: a candidate clarification, as F1 records its own.
- **F20** *The freeze's regions (step 4c-ii; review 2aadf33 B6).* §8.3 step 4 (b) freezes "the signature, scope, regions or membership" of a subject whose current revision carries an unresolved blocking challenge or is `REVOKED`. Its regions are read as their terms' resolution status, resolved or `ABSENT`. Bytes, the files under a prefix, and anchor lines are content: an edit of them makes a new revision, which is how a challenge's resolution proceeds, and the freeze concerns structure ("whether it would lose or gain units"). So a file added under a frozen prefix-scoped subject, or an anchor moved within it, is not frozen, while a rescoping, a change of kind, mode or declarations, a term coming to resolve or not, and any unit joining or leaving (nested subjects included) are. This is narrower than §1.2's region difference, which the write set uses: there, a term resolving into other files, or existing bytes entering or leaving under the pinned alignment, also count, so an anchor move or a file moved out of a prefix would freeze. Under either reading the freeze lets content move between subjects, so this is no decision change. The narrower reading goes to Stage S as a candidate clarification of "regions" in §8.3 step 4 (b).
- **F8** *No campaign.* The Dispatcher issues envelopes to fixture executors, and to the manual and Git-envelope routes in scratch repositories, where lineage is `UNKNOWN` unless a human attests it (§12.2). Its harness route is built and tested against a stub harness, never a live model, without a campaign authorization. On the real shadow ledger `dispatcher serve` issues nothing and writes no run ref.

## 6. Fail closed until a later owner

Until the stakeholder settles Q-F1 and Q-F2, steps 10-11 do not run, and the exit reports the difference study as unexecuted.

Until Q-F3, real-runner execution is limited to fixtures that hold no secret.

Until Phase G, a change of unknown provenance on the real shadow ledger is absorbed and goes no further than its §18 intake obligations, which are derived but not routed beyond `INTAKE`. The exception is SD-69's: step 10's human `ABSORB` adoption of the two reserved leaves (F1).

Until Phase H, failure points beyond those group 4 names are untested, and §24.2's replacement-lineage re-encoding is not built.

Until an authorized campaign, no live agent submits to Admission.

Until step 4c-iv builds the schema-1 correction SD-69 adopts for Q-F6 (i), adoption by `ABSORB` is `SCHEMA_UNSUPPORTED`; until Stage S settles Q-F6 (ii), so is a change of an existing unit's kind or owning domain (reading F16). Until Phase G, a cutover an integration carries is too. Until Stage S, a quarantined key that a candidate authors to the value a foreign change put on the observed tree is refused `STRUCT_REVALIDATE` (4c-ii), a stronger rule than Manual §7.2 alone. Until Q-F6 (iii) is settled and step 5 builds the rebase, a record declaring a rebase frame is refused `REF_TRANSFORMATION` (§3.1, 4c-iii).

The Phase E items listed in §4 stay as Phase E §6 states them.

Each fails toward "not supported", never toward support.

## 7. Questions for the stakeholder

**Q-F1. What "computing decisions beside document control" compares.** The Phase F row's exit asks that every material difference from document control be classified and independently reviewed. In shadow, document control's changes reach SSDS as absorptions, which Admission always admits (§8.6). Admission's record-dependent checks (envelopes, judgments, contracts, write scope) have nothing to judge in this repository's history. Its population depends on Q-F2: under a new genesis it is the integrations observed after the genesis baseline. Those are mostly Phase F's own commits by one implementer, a small and self-referential population. (a) can also run retrospectively over earlier history wherever the manifest exists, which widens it.
- **Recommended: (a) with (b), and (c) carried into the campaign plan.**
  - **(a)** A qualification harness, calling the real Admission owners outside the ledger, evaluates each observed integration as if submitted. It uses the checks that need no SSDS-only record: the secret and credential scans (§24.1); structure on the merged tree (§8.3 step 4: effective-structure delta, quarantine, SDG membership); protected surfaces (§25.3); dependency well-formedness (step 5). The hypothetical request authors exactly the integration's delta. With no contract, the write-scope and "exactly what it authors" checks are vacuous, and so is step 8, because this repository has no evidence specifications. The report says so.
  - **(b)** The consequences derivation shows after each absorption: quarantine, ill-formed subjects, drift, reopened obligations, integrity findings. Step 10 produces these anyway.
  - **(c)** The record-dependent comparison, in which agents submit through SSDS beside document control, goes into the campaign plan G2 §5.5 requires for G3 anyway.

  Each difference (a) or (b) finds is classified and independently reviewed.
- **Alternatives:** (b) alone, which is cheaper but never exercises Admission's checks against real changes; or deferring the whole study to (c), which leaves Phase F's exit unexecuted until a campaign runs.

**Q-F2. The genesis parameters for the new shadow ledger under A9.** The new genesis itself is decided (Phase E §7). What is open:
- **(i) The observed ref.** Recommended: this branch, `ssds-8.0-graph-native-architecture`, where Stage D's work integrates, with the genesis baseline taken from its history. `main` is not usable as it stands (reading F1). The considerations:
  - **A rewrite costs a finding.** A working branch can be rewritten. A rewrite past an admitted records-only admission makes it `OVERTAKEN`, and a later re-observation a `CRITICAL` `LATE_PUBLICATION`. So the observed branch must not be rewritten (it is not: no force-push is the branch's rule).
  - **Switching refs has no record.** Moving the observed ref later, for example when the branch merges to `main`, would absorb a commit that need not descend from the current one. A new genesis, or the merged `main` observed from a commit descending from the last observation, is the clean route.
  - **How it is set.** Recommended: a required `--observed-ref` option of `admission serve`, the way Phase E's commands take `--ledger`, with Admission refusing to start when that ref's head does not descend from the ledger's last observed head. That avoids Phase D plan §7 Q5's `[ssds]` section, an additive change to Core configuration. The alternative is to answer Q5 and add that section.
  - **The ledger id.** Proposed: `ssdp-shadow-2`.
- **(ii) Issue and runner keys.** Recommended: declare none now. Phase F issues nothing on the real ledger (F8), and an unused trust root and private key in the real home is exposure with no use. A stakeholder-signed `KEY_LIFECYCLE` record adds them when a campaign needs them. The alternative is to declare them at genesis, which needs the script's key option first (step 3).
- **(iii) The old `ssdp-shadow`.** Recommended: a retirement statement, so that it is `RETIRED`, read-only history. The alternative is to leave it unretired and unused. Either way Phase E reading E33's interim check retires when the new genesis is admitted (SD-61), not with the old ledger.

A dry run of `prepare` (baseline `1e34abef`, throwaway key, scratch SSDS home) validated (`valid: true`, no problems, `ssds.unclassified` declared). The real run waits for (i)-(iii).

**Q-F3. The operator trees and the runner sandbox.** Recommended:
- the layout in §2: issue and runner keys under `keys/`, the journal and leases under `state/<ledger id>/`, and runner workspaces under `runs/` in the SSDS home, outside every ledger's operator tree, with their own containment check. The Manual puts Dispatcher workspaces in the SSDS home (§26.3, A7). A root outside the home would need an A7 amendment, reopening G1, and is not proposed;
- runner processes are confined by `bwrap`, which is installed here (bubblewrap 0.6.1). It denies reads of the operator trees and the network, a runtime dependency for the runner path.

Both the trees in the real home and the dependency are the stakeholder's to approve (§8). Without the sandbox, real-runner execution stays limited to secret-free fixtures (§6).

**Q-F4. The `TASK_RESULT` outcome vocabulary (settled by SD-67: option (a)).** Ledger schema 1 allows `COMPLETE`, `INCOMPLETE` and `PARTIAL`. Catalogue §3.4 gives a task result "the task's allowed outcomes (§12.3)": `COMPLETE`, `PARTIAL`, `BLOCKED`, `INFEASIBLE`, `FOUND`, `NONE_FOUND` and `INCONCLUSIVE`. §13.7 also routes an `INCOMPLETE` result, which no §12.3 template permits, so the catalogue disagrees with itself there. §3.6 makes any change to an enumeration a new schema version adopted by `SCHEMA_MIGRATION`. Until this is settled, a result with an outcome outside schema 1 is refused at step 1, so no task can end with `BLOCKED`, an implementer's task cannot end with `INFEASIBLE`, and an investigator's cannot end at all (`FOUND`, `NONE_FOUND`, `INCONCLUSIVE`).
- Recommended: (a) correct schema 1 in place as a transcription defect. No ledger holds a `TASK_RESULT`; the old `ssdp-shadow` has none and `ssdp-shadow-2` has no genesis yet. Send the `INCOMPLETE` disagreement to Stage S, and keep it permitted by no role until then.
- Alternative: (b) schema 2 through `SCHEMA_MIGRATION`, which needs that lifecycle record's checks first.

**Q-F5. Codes for step 5's non-cycle checks (settled by SD-68: the recommendation; catalogue §8.4 now names them).** Catalogue §8.4 has no code for these:
- challenge-tier targets strictly earlier and of permitted kinds;
- the counter-challenge rule;
- no `validity` entry on a record's own subject;
- no equivalence relying on a consumer of its unit.

Step 3 has two more such refusals (revision 4): an acceptance of a subject revision other than the current one, and of a subject no longer effective (step 3's "current tenure"; `AUTH_TARGET_PART` names a part, not an absent subject).

Reading F6 sends a refusal with no code back to Stage S.
- Recommended: Stage S adds one code per check to §8.4 (for example `DEP_TARGET_ORDER`, `DEP_TARGET_KIND`, `DEP_OWN_SUBJECT`, `DEP_CONSUMER`). Until then a record that would need them fails closed (§3.1, 4d).

**Q-F6. Three structural acts schema 1 cannot express (reading F16; settled by SD-69: (i) and (iii) corrected in place, (ii) to Stage S).** Neither blocks Phase F, since no agent submits in shadow. Both fail closed until settled.
- **(i) The intake disposition's target and outcomes: a schema-1 transcription defect.** Catalogue §3.4 targets "quarantined delta or observed content" with the §18.3 vocabulary, and its basis names "the absorption entry and delta key". Schema 1 has `units|content_ref`, the outcomes `ADOPT ABSORB REALIGN QUARANTINE REJECT`, and no type that names a declaration key. No ledger holds an `INTAKE_DISPOSITION`: read through the program on 2026-10-25, `ssdp-shadow` and `ssdp-shadow-2` each hold only their genesis entry.
  - Recommended: (a) correct schema 1 in place, as SD-67 did for Q-F4:
    - the target becomes catalogue §3.4's "quarantined delta or observed content": a `delta` target (`{absorption, key}`) beside `content_ref`, with `units` dropped, since §3.4 lists no unit target;
    - the `identity` basis grammar gains the same `delta` type, so the basis can carry "`identity` on the absorption entry and delta key" (catalogue §4);
    - the outcomes become §18.3's;
    - a `QUARANTINE` names its observed paths in a `paths` field, as §18.4 requires;
    - `INTAKE_CLASSIFICATION`, which has the same defect (schema 1 `units|content_ref` against §3.4's "observed path set or quarantined delta"), is corrected in the same change, with the test fixtures that build either kind on a `units` target.

    Stage S keeps the residual: the canonical element form of `A` in `JCS(sorted A)`.
  - Alternative: (b) schema 2 through `SCHEMA_MIGRATION`, which needs that lifecycle record's checks first.
- **(ii) The release of a kind or domain change (for Stage S).** §8.3 step 4 (a) needs the old domain owner's judgment, but no record kind or field expresses one.
  - Recommended: Stage S names the kind and its target, evaluable outside the frame. A judgment about the transformation would declare its frame (§7.5), and its currency would then depend on `Frame.exists`, which depends on it (§7.4). The enactment condition is outside §7.4's well-formedness for the same reason.
- **(iii) The rebase frame: a schema-1 transcription defect of the same class.** Catalogue §8.3 step 2 has a record declaring the frame of a rebase `X'` carry `X'`'s `(B', C', A')` and the transformation it rebases. Schema 1's `frame` field holds only `{transformation}`. No ledger holds a frame record.
  - Recommended: (a) as in (i), correct schema 1 in place: `frame` gains optional `base`, `candidate`, `adopts` and `rebases`, present together.
  - Alternative: (b) schema 2 through `SCHEMA_MIGRATION`.
  - Until then a rebase-frame record is refused `REF_TRANSFORMATION`. Machinery rebases (§11.5 step 3) wait with it, so an overtaken candidate takes a new iteration.

**Q-F7. `ssdp-shadow-2`'s genesis lacks two reserved leaves (reading F18; settled by SD-69: the recommendation, (b) with (d2)).** Manual §1.8 has genesis declare `ssds.manifest`, `ssds.policy` and `ssds.unclassified`. The program refused only a genesis without `ssds.unclassified`, so the genesis signed on 2026-10-25 declares neither of the other two.

From step 4c-ii, Admission checks all three on every admission (§1.9), so a request whose new structure still lacks them is refused. Nothing in Phase F needs one: no agent submits content in shadow, and absorptions are unaffected.

The ledger can also be repaired in place, by any admitted structural change that authors the two declarations (§1.6, §8.3 4 (a)). The options:
- **(b) Keep it, re-found before a campaign.** Keep `ssdp-shadow-2` for step 10, record the deviation, and re-found before any campaign or cutover with a baseline manifest declaring the leaves.
  - Costs: a later signing, and a new observation history.
- **(d2) Repair in place by adoption.** Commit the two declarations to the observed branch's manifest; they are absorbed as quarantined deltas, and an R2 `ABSORB` adopts them (§18.4).
  - It is a records-only request (`C = B`), inside the shadow boundary.
  - Costs: none in signings or history, but it waits for Q-F6 (i) and the adoption path.
- **(d1) Repair in place by a content request.** A human content request authors the two declarations.
  - Costs: F1's observe-only check refuses any request whose candidate differs from its base, so the stakeholder would have to relax that boundary for this one request.
- **(a) Re-found now**, as `ssdp-shadow-3`, before step 10.
  - Costs: a signing now, and step 10 observes the new ledger.
- **(c) Read §1.9 as requiring only §1.8's refusal clause.** It contradicts §1.8's first sentence, so it would be a Manual amendment.

Recommended: **(b) with (d2)**. Keep `ssdp-shadow-2` for step 10, and correct the genesis check now (4c-ii). Once Q-F6 (i) is settled and adoption is built, repair the ledger in place by (d2); re-found under (b) only if that is not available before a campaign.

**Resolved by SD-64 (stakeholder decision record item 60):** the recommendations above for Q-F1, Q-F2 (i)-(iii) and Q-F3 are adopted as stated. Step 10 runs on `ssdp-shadow-2` once the stakeholder has signed its genesis, and the old ledger's retirement statement follows step 7.

## 8. Reopen and stop

G2 workplan §5.6 applies:
- a Manual decision failing in practice reopens G1;
- a register row failing at its real owner, or a needed behaviour with no row, returns to Stage S;
- a failure family recurring after a repair triggers simplification before another additive repair;
- any breach of the shadow boundary stops Stage D and goes to the stakeholder.

Specific to Phase F, these come to the stakeholder before they are built:
- a credential for any governed ref;
- a write to the product repository or its `.git`;
- a new operator tree;
- a new runtime dependency;
- any live model call.

## 9. Plan and step review record

**Step 2 same-family review (0933e5db).** NO-PASS with eight blockers and no SERIOUS CHALLENGE:
- **B1, the chain could halt.** A refused record was identified by its claimed `id`, so a malformed one halted the chain. Refused records are now identified by content, and the entry is validated before any append.
- **B2, salvage admitted unchecked material.** Salvage admitted records that were never checked, and objects that were never verified. Every record is now checked whatever the request's faults, references resolve only to records that passed, and only verified objects that admitted records reference are written.
- **B3, objects were not verified.** Each object is now checked against its key: digest grammar, digest of the canonical JSON. Records' `LEDGER` refs must resolve (`REF_OBJECT`).
- **B4, never-lost classes.** They now come from the derivation owner (`derivation.adverse`).
- **B5, secrets under identity key names.** The entropy exemption now goes by the value's grammar, not its key name.
- **B6, untrusted input.** Request fields have their grammar checked, unencodable input gets a deterministic identity, and each request leaves the queue as it is taken.
- **B7, `base_commit`.** It must match the head after `base_position`.
- **B8, test gaps.** The missing tests are added, including the S2 binding cases and the remaining credential forms.

Tests: `test_admission_requests.StepTwoReview` fails on 0933e5db for every behavioural blocker. Non-blocking notes kept for later steps:
- the entropy threshold's weak detection below about 30 characters (a policy calibration);
- paths flagged by the tokenizer;
- whether "challenges" in §8.3 step 6 include adjudications (to settle before step 4);
- the `machinery:` actor prefix standing in for runner authentication until steps 3 and 9.

**Step 2 re-review (e95e770c).** B1, B3, B4, B5 and B7 are closed. NO-PASS on five blockers:
- **S1, B2's dangling reference.** A salvaged record could name a record salvage dropped. Salvage now rechecks references against the records actually admitted, to a fixed point.
- **S2, B6's poisoned queue.** `never_lost` and the ledger schema's membership checks were not total over untrusted values. A list-valued `kind` crashed `record_violations`, a Phase D schema defect the probe reached. Both are now total.
- **S3, bounds.** A request beyond its bounds still got per-record work and salvage. Beyond a count, depth (64, a proposed default) or byte bound, there is now no per-record work and no salvage.
- **S4, a halted request.** A head mismatch dropped the request in hand. It now goes back to the front of the queue.
- **S5, undiscriminated repairs.** Two repaired claims had no discriminating test.

The added tests are `StepTwoRereview`. Non-blocking notes kept:
- the entropy grammar exemption never triggers (hex stays below the threshold);
- the pre-append guard is defence in depth;
- `REPORT_KINDS` duplicates derivation's list;
- two refused records differing only in their claimed `id` share an identity;
- later-step reachability of the position-sensitive base check and of admitted producing contexts (steps 4 and 6).

**Step 2 third check (36497a1c).** S1, S2, S4 and S5 are closed (S2 fuzzed over 9,600 substitutions with no exception). NO-PASS on two:
- **T2, the byte bound failed open.** It read as not exceeded whenever canonical JSON could not encode the request (a float), so an 8.8 MB record could be salvaged. Size is now measured by walking the value, independent of encodability.
- **T1, five repaired behaviours lacked discriminating tests.** These are now added (`StepTwoThirdCheck`): a two-level dangling chain; a salvaged record naming an admitted one, which is kept; requeue order; empty refusals beyond depth; each schema type guard through the queue.

A non-blocking point is taken too: the pre-append guard raises its own `EntryInvalid`, so such a request is not requeued forever.

**Step 3a same-family review (e6ac0091).** NO-PASS with seven blockers and no SERIOUS CHALLENGE. It confirmed the envelope fields (catalogue §12.2 minus `retained`, RR-2), `AUTH_VERSION`, the retired-key rule, the lineage classes, human SSHSIG authentication, step ordering and approval-in-provenance as a D4 placement. The repair:
- **B1, actor impersonation through salvage.** Any valid envelope salvaged a record naming a human or `machinery:` actor. A task binding now covers only its own agent's records, `agent:<task id>/<attempt>` of class `AGENT` (§25.1; `AUTH_ACTOR` otherwise), so machinery and runner observations wait for runner keys (step 9). The salvage tests bind agent records.
- **B2, a binding that tripped the secret scan was stored.** A binding carrying a secret now authenticates nothing (`SECRET_DETECTED`), and nothing of it is stored.
- **B3, unverified attestation material was stored.** A harness binding authenticates only with all three of the attestation, its issue-key signature and the credential's signature over the request, and any other route carries none of them (`AUTH_ENVELOPE`). The attestation's fields are closed to `{task_id, envelope, session, input_sessions, credential_key}`. It names its envelope's digest and the envelope's input sessions, which closes the review's unbound-attestation note and part of its session-list note.
- **B4, untrusted input crashed Admission.** A binding canonical JSON cannot encode (a float) is a recorded `AUTH_ENVELOPE` rejection.
- **B5, lifecycle approvals could be replayed.** The human signs the ledger id, the position the entry takes, the head digest it extends and the record (`admission.lifecycle`), so an approval is spent by its entry. An already-admitted lifecycle record is refused besides; only an identical `COMPROMISED` replay needs that rule.
- **B6, lifecycle key objects were not validated.** Each action has a closed key shape, `{role, id, public_key}` plus `retires` for a rotation, with `id` the public key's own identity. A registration or rotation introduces a never-known key, a retirement names a key in force, and a compromise names a known key at a reached position. Only an issue key's retirement or rotation lists outstanding envelopes. The last human key is rotated, never retired. Admission host keys and runner keys are refused on this path until the engine's key switch and step 9 exist. One convention holds for every role: an action names its key by `key.id`, and a rotation names the replaced key by `key.retires`, in `derivation.trust` and in the host-key reader of `ledger.read`. Both readers are total, never raising.
- **B7, the issue key bypassed the SD-59 `Home` owner.** `dispatcher.home.DispatcherHome` takes the issue key and the journal through `Home`: the ledger-id check, the inside and file helpers, and `Home.check` at construction, with `keys/dispatcher` added to the operator tree. Every later file effect walks from the home root one directory at a time without following a link, and uses only a regular private file of this user. The journal appends only to a file with a single name. A first creation is atomic (a link to the name), so concurrent first use reads the one winning key. The dispatcher already imported `ledger.qualification`, so fitness is unchanged.

Tests: `test_admission_requests.StepThreeReview`, which also covers the surviving mutants M2b, M3b, M4b, M4c, M7b, M11 and M20. Each repair was reverted alone in a scratch copy, and its test fails on every one of 21 reversions. The reviewed commit's own API differs (`Issuer(home_root)`, `lifecycle_message(record)`), so the tests were not run on it unchanged. Non-blocking notes kept:
- compromise backdating by a compromised in-force key;
- the record's `binding.lineage` against the attestation's session, which step 4's independence must not trust;
- the SSH-armour exemption's body length;
- cross-ledger replay of human-signed requests (no ledger domain in `request_message`);
- no secret scan on lifecycle records: an OpenSSH public key line trips the entropy check, so it needs a grammar exemption first;
- no fitness rule that only the dispatcher holds an issue key;
- "`UNKNOWN` lineage credits no independence", untested until step 4;
- the surviving non-blocking mutants M3c, M3d, M6b, M6c, M7c, M10, M13 and M13c.

**Step 3a repair re-check and step 3b review (a71cca2f).** All seven repairs are in place, and their probed behaviour is correct (8 concurrent first uses give one key; a hard-linked journal is refused). NO-PASS on three blockers, with no SERIOUS CHALLENGE. The repair:
- **N1, a second compromise relaxed the first.** It was new in a71cca2f. A later `COMPROMISED` of the same key overwrote its position, so an envelope refused under the first was admitted again, and §25.2 has no path to un-compromise a key. A re-declaration is now admitted only with an earlier position, and both readers keep the minimum. B5's note above was incomplete: a non-identical re-declaration also passed.
- **N2, a torn journal tail (step 3b).** A crash part-way through an append left an unterminated line, and the journal could no longer be read; the next append was glued onto it, losing that envelope from a retirement's listing (catalogue §8.1, §22.4, §25.2). An append now drops an unterminated last line first, under an exclusive lock. That line was never acknowledged. Reading ignores it and refuses any other unreadable line (`JournalCorrupt`).
- **N3, repaired claims without discriminators.** `StepThreeRecheck` adds one for each surviving mutant of the re-check's 45: m1-m8, m14-m16, m18, m21-m24, m26, m28, m29, m31, m32, m35-m38, m46 and m47, plus N1 and N2. Four were claimed equivalent and are not tested:
  - m25, a redundant line, now removed;
  - m40, `_check_paths` for names every operation checks again;
  - m43, the retired key's public key, which the identity check already pins.

  - m48, B5's already-admitted rule: after N1, the state rules refuse every action's identical replay. The rule is kept as the review asked. (Wrong for m48 and m43: see the narrow re-check below.)

  One of the new tests found a defect: `read_private` read a directory before checking its kind. It now checks first. All 45 of the re-check's mutants, the 21 earlier reversions and 7 reversions of this repair are run again. Every one fails a test except the 4 equivalents.

Its non-blocking notes:
- A list-valued `action` or `role` is now refused, not a `TypeError`.
- Kept for later steps:
  - a `COMPROMISED` of the last human key leaves no human gate, and fails closed until a `TRUST_MECHANISM_CHANGE`;
  - the issue key's single-name rule (the journal's applies already);
  - a never-lost record under an unlisted envelope should be refused by identity with its bytes retained and a re-issue obligation raised (catalogue §8.3 step 3, §10.2), which no step places yet; step 4 takes it;
  - `Issuer.issue` does not journal its envelope (write-ahead order is step 8's);
  - the brief-digest formula duplicates `interface.render.Brief.digest`;
  - the journal keeps request bytes indefinitely.

**Narrow re-check of the N1-N3 repair (496311ee).** N1 and N2 are closed at their owners. No code defect in the delta (six writers and two readers in parallel lose no entry). NO-PASS on one test-only blocker, R1, with no SERIOUS CHALLENGE:
- **The append lock had no test.** Without it, concurrent writers overwrite each other's lines, because the append writes at an explicit offset; the re-check kept 108 of 361 entries.
- **m48 and m43 are not equivalent.**
  - m48: an identical `COMPROMISED` of a former human key passes the state rules, and only the already-admitted rule refuses it. The m48 entry above was wrong.
  - m43: a human `RETIRE` whose key line differs from the one in force only in its comment is refused because the comparison is exact.

The repair is `StepThreeThirdCheck`: six concurrent writers keep all 361 entries, plus the m48 and m43 cases. Its notes are taken up too:
- an empty journal line is refused;
- a line that is JSON but not an entry is `JournalCorrupt`, now tested;
- a read opens without blocking, so a FIFO at the journal's name is refused rather than hanging;
- an append makes the directory durable as well.

Each of the six fails its test under reversion. Under the review allocation, a test-only repair of this kind is checked by rerunning the reviewer's own probes and mutants rather than by another full pass. Rerun on the repair:
- 12 of the reviewer's 13 delta reversions and 43 of its 45 mutants fail a test. The survivors are d4 (no truncation: the junk it leaves has no newline, so readers ignore it and the next append drops it) and m40, both equivalent. m25's line no longer exists.
- Its probes r1-r7 hold. r6 now meets the empty-line refusal. One residual stays non-blocking: an append still succeeds onto a journal corrupt before its last line, and the reader refuses that journal afterwards, failing closed.

Steps 3a and 3b are clean under the review allocation.

**Same-family plan review of b10018de (revision 3, the step 4 split).** It found the split and the trial's owner right. NO-PASS on seven blockers, with no SERIOUS CHALLENGE. Revision 4 repairs:
- **B1, a live fail-open in salvage (a step 3 defect).** Never-lost salvage admitted records whose own checks are not built yet. The review's probe salvaged an `IMPLEMENTER`-bound `REVIEW NO_PASS` whose `supersedes` then ended another task's standing judgment. Until 4b, salvage admits only reports with an empty `supersedes`; every other never-lost record is refused by identity (§3.1). The code change and the probe as a regression come first in 4a.
- **B2, F10's step 6 mechanism.** `Support.sat` reads its own state as well as the value function, so a trial-side evaluation would pass a stale before-image and let a co-submitted record satisfy a `standing` entry. Step 6 now runs on the head's `Support` in the record's frame, with frame and roles explicit. The base-versus-head wording is fixed, and each code's scope (rejection, or refusal alone) is stated.
- **B3, F11's lineage.** It is now the §12.2 attestation closure. `UNKNOWN` carries an empty lineage, and `HUMAN_ATTESTED_FRESH` stays refused until placed.
- **B4, the survey's ownership claims.** `nonind` was not fixed at admission and lacked the owner exception; `Conformance.writes` was not §1.2's write set; prospective tenure, chain class, the consumer predicate, the warrant relations and `REISSUE` had no owner. Each is now listed in §3.1 and placed: `nonind` in 4a, the write set in 4c.
- **B5, the `TASK_RESULT` outcome vocabulary.** It goes to the stakeholder as Q-F4, failing closed meanwhile.
- **B6, checks with no code.** The adjudication and class checks are `AUTH_ACTOR`; the envelope's obligation and role are `AUTH_ENVELOPE`; 4c's revalidation is a `STRUCT_*` member; `CYCLE_WARRANT` reads §2.4's relation set. Step 5's four non-cycle checks go to Q-F5, failing closed.
- **B7, 4a's equality claim.** It now excludes the facts keyed on the trial entry's digest, which reading F10 lists, and 4a and 4b are restricted to records-only requests without deltas.

Its non-blocking notes are taken up:
- the co-submission cost, disclosed in F10;
- the component predicate stated as a subset;
- "trial entry", not "provisional entry";
- one owner for protected surfaces;
- `REISSUE` placed.

Kept for 4a's implementation:
- trial cost (a resume from a `History` checkpoint is available);
- the unbounded class-level caches in a long-lived `admission serve`.

**Same-family review of step 4a (409c2f71) with the re-check of plan revision 4.** Revision 4 closes B1-B3 and B5-B7 of the b10018de review. NO-PASS on five blockers in B4's repair, with no SERIOUS CHALLENGE. Classifying "at the admission position" by rebuilding a `State` there was both wrong for frame records and costly. The repair replaces it rather than patching it (G2 workplan §5.6):
- **B1, frame records.** Classified in the admitted state, a candidate's content had `UNKNOWN` authors, so a human author's prospective `ACCEPTANCE` or `COMPLETENESS` stayed independent after the candidate integrated. Classification now reads the record's frame: a candidate's pieces are authored by its transformation's makers (as `_transformation_work` reads them), and a frame `COMPLETENESS` judges the candidate's members.
- **B2, chained dispositions.** The requirement was direct only, so a claim's author could dispose of a failure by reassessing twice. A reassessment now has the requirement when its supersession chain reaches a failing assessment at any depth.
- **B3, the adjudication branch of the owner exception.** It never fired (no domain for an adjudication), and once fixed it covered any outcome and depth. It now covers only an `UPHELD` adjudication of a challenge whose target is the failing assessment, in that claim's domain. Whether a challenge against the assessment's realization also counts (§6.7's wording) is left closed: not covered.
- **B4, cost.** Each record's classification rebuilt a `State` and refolded every view: 10-17 s over 800-1200 admissions, against 0.02-0.14 s before. Authorship is now one fold per `History` (`History.productions`), read as of any position. `State.authors` reads it too, so no consumer refolds. Classification builds no `State` (a test counts them). The review's own script classifies 800 and 1,200 admissions in 0.03 s each.
- **B5, untested branches.** A test now covers each mutant the review left alive: the exception's scope (J19), `UNKNOWN` authors (J20), the `IMMATERIALITY` branch (J4, J5), failing-ness (J6), plus reading authors as of admission (a later re-producer of the same revision).

What the classification reads from the admission position, in full:
- the record's binding;
- its judged content, pinned there (a `COMPLETENESS`'s members included);
- the authors as the ledger knew them there;
- the policy then in force.

Its notes:
- Q-F4's text now names every blocked outcome.
- §3.1 states the salvaged reports' bounded exposure.
- The inspector shows the common-mode dependency (`queries.explain`).
- Kept for Stage S: the catalogue's §5.10 (a) "Owner exception" sentence is broader than the Manual's SD-48 narrowing in §5.10 (f), and the code follows the Manual.
- Kept, as noted: a trial is a fresh `History`, refolding its prefix once (now linear), and resuming from a checkpoint is available if a ledger's size needs it; class-level `lru_cache` retention in a long-lived `admission serve` goes to step 10's operation.

Every repair, reverted alone, fails a test: 12 new reversions and the earlier 7.

**Narrow re-check of the 4a repair (b8a18003).** B1-B4 of 409c2f71 are closed. Classification costs 0.02-0.04 s over 800-1,200 admissions and 0.33 s over 800 frame records. An instrumented full suite found `State.authors` equal to the old per-`State` fold in every call. NO-PASS on two defects and test gaps, with no SERIOUS CHALLENGE:
- **B1, a restored revision's earlier producers (new in b8a18003).** A frame record took the candidate's makers instead of the authors of a revision the candidate restores, so the original author's prospective `ACCEPTANCE` of a restore was independent. The same override was older, in `_transformation_work`. That one owner now unites the makers with every earlier admitted producer of the piece (§5.10 (b): "a revert, restore or re-application that re-produced it included"). Frame records read it, so no second union exists.
- **B2, an `IMMATERIALITY` covering several failures (present since 409c2f71).** The owner exception read only the first covered failure, so list order decided whether the owner disposed of another domain's failure. It now holds only when it holds for every covered failure, each in its own claim's domain against that claim's authors.
- **B3, test gaps.** The exception's unknown-authorship clause (the review's J20) and the policy in force at admission (R12) are now tested. §9's earlier claim that J20 was covered was inaccurate: that test covered the agent-lineage rule.

Each fix, reverted alone, fails its test. Survivors the review judged behaviour-preserving in the suite are kept as notes:
- R17, R19 and R20 (makers bound by position, first producing result);
- R15 and R16 (adjudication-root authors as of admission);
- J22 (the exception for agent judges, which `owner_exception`'s `human:` test already excludes);
- J24 (the route exception disabled, an existing gap).

**Same-family review of 4b-i (8a415395) with the narrow re-check of a406c0b2.** No SERIOUS CHALLENGE. The role templates match §12.3 exactly, and the test-only `SHADOW_MODES` patch is sound. NO-PASS on both deltas.

**4a (a406c0b2): two blockers.** This was the fourth round on independence inputs. The repair replaces case-by-case patches with one rule, not another patch (G2 workplan §5.6).
- **R-B1, producers between a candidate's base and the judgment.** `_earlier_producers` stopped at the base, and work judgments ignored the admission position. Now every kind reads one rule (`_authors_for`): the producers of a piece in every admitted view at or before the judgment's admission, plus the makers of a candidate the record is about, else `UNKNOWN`.
- **R-B2, the per-claim owner exception was untested.** Tests now cover its mutants M5, M7, M10 and M13.
- **Also found and repaired.** §6.7 also disposes of a failure through an `UPHELD` challenge of its realization, which the owner exception and the requirement now cover. An observation at a chain's root now has the authors of the content it ran on (§5.10 (e)); before, it read `UNKNOWN`.

**4b-i (8a415395): six findings.**
- **B1, injected attestations.** `stored_attestations` read every stored object, so a salvaged report could plant an attestation. It now reads only binding objects that admitted records name; a conflict leaves the closure open.
- **B2, supersession targets.** Exact target equality is replaced by catalogue §5.10 (b)'s per-kind supersession target, built where it is one exact thing:
  - the triple, for an acceptance or a subject review;
  - the gate and triple whatever the core, for a gate decision;
  - the realization, obligation and reading, for an assessment (case R);
  - the target, for other kinds.

  Judged-scope kinds and principals' decisions fail closed until their owners exist.
- **B3, current tenure.** An acceptance of any revision but the current triple, or of an absent subject, fails closed and joins Q-F5.
- **B4, product scope.** Product-scope acceptance fails closed until its policy-designated authority is built.
- **B5, never-lost records unrecorded.** When salvage is withheld, each never-lost record is recorded as refused: `AUTH_ENVELOPE`, `REF_BASE` or `SCHEMA_UNSUPPORTED`.
- **B6, untested checks.** Each mutant the review left alive now has a test: lifecycle and discriminating refusals, observation never superseded, the table equality of §12.3, `absent_term`'s subject filter, two-round fixed points and an invalid base.

The review's note 2 is taken up: F11 accepts a lineage containing the closure. Equivalent mutants are kept as notes:
- `absent_term`'s prefix filter (a prefix term never resolves to `ABSENT`);
- E3 (the obligation read at the head instead of the base: no records-only ledger yet derives an agent-held obligation that appears or vanishes between the two).

Notes kept for later steps:
- **Real shadow ledger (step 10).** A production-shaped genesis derives no agent-held obligation, so every agent-bound request there is `AUTH_ENVELOPE`. A test now pins this.
- **Roles.** `WITHDRAWAL` is in no template, and schema 1's `TASK_RESULT INCOMPLETE` is permitted by no role (Q-F4).
- **Undecided.** Whether the acceptance-target rules apply to `LEGACY_ACCEPTANCE` or a gate `ACCEPT`.
- **Cost.** A trial per authorization round costs little; the workflow at the base costs about 57 ms per request at 120 entries and grows.

Every repair, reverted alone, fails a test.

**Narrow re-check of 6e0fa9eb.** No SERIOUS CHALLENGE. R-B1 is closed at admission, and R-B2 and B1-B5 are closed. NO-PASS on three blockers:
- **NB-1, the one authors rule did not reach routing.** Routing (`RouteEligibility`, judge selection) still read the base-fixed `work_authors` and `State.authors`, so a judge could be chosen whose answer admission would classify as non-independent. Every reader now calls one function, `Judgments.piece_authors`: classification as of a record's admission, routing as of the state. `Workflow.judged_authors` reads it through `transformation_authors`.
- **NB-2, the superset lineage planted authors (new in 6e0fa9eb).** The superset rule let a producing record add `UNKNOWN`, human ids or other sessions, which derivation reads as authorship. One probe opened the owner exception that way. Reverted: the lineage is exactly the closure (reading F11 restored, its cost stated).
- **NB-3, a human independent of content of unknown authorship (predates 6e0fa9eb).** Manual §5.10 (f) says "an authenticated human must not be one of them or must present a `NON_AUTHORSHIP_ATTESTATION`", and its summary says "judged content of unknown authorship admits only a human with a non-authorship attestation". The repair is its own commit, after this one: it reverses about 28 Phase D-E test expectations, because a baseline with no admitted producer has unknown authorship, and each needs examining.

The review also corrected the supersession-target rationale. The column says "the target" for transformation reviews, conformance, equivalence, completeness (without the analyzer) and product scope; only plan acceptance's is conditional on its basis. `supersession_target` now builds them all except plan acceptance, which fails closed.

Tests now cover the review's survivors that matter:
- M1 (routing reads the same authors);
- N3 (a maker reviewing its own candidate);
- N20 (conflicting attestations);
- A14 (ill-formed without `ABSENT`).

E3 is recorded as unreachable now, not equivalent: test it once a principal-held obligation exists.

**NB-3 repaired (the stakeholder approved proceeding, 2026-10-25).** A human with an independence requirement is now independent of judged content of unknown authorship only with a `NON_AUTHORSHIP_ATTESTATION` (Manual §5.10 (f): "an authenticated human must not be one of them or must present a `NON_AUTHORSHIP_ATTESTATION`"). This follows the catalogue, too:
- §5.10 (a) makes content with no admitted authoring record unknown-authored: absorbed pushes, legacy imports, restores, a genesis baseline;
- its §31 cases say "a triple with absorbed bytes admits only a human with `NON_AUTHORSHIP_ATTESTATION` or the owner exception".

The two repairs at derivation's owners:
- **Classification.** `Judgments._independent` adds the unknown-authorship condition.
- **Requalification.** A first version also made routing refuse such a human. That stranded every obligation on baseline content, and it was wrong: a human outside the known authors can answer by presenting the attestation, so routing keeps them eligible (`RouteEligibility.independent`, with a comment). Separately, `NON_AUTHORSHIP_ATTESTATION` and `LINEAGE_ATTESTATION` are no longer permissive for `REQUALIFY` (`s3._permissive`). Their one effect is a classification fixed at admission, an S0 fact no boundary withholds (catalogue §5.5). Without this, each attestation left an obligation after a loss boundary that nothing could end.

**Test ripple.** 44 Phase D-F tests had a human judge baseline or absorbed content. Each was examined, and the human judge was given the attestation an independent human would present, through a test helper, `_scenario.attested`. A rewriter flagged any test in which a human is also an author through a lineage, where an attestation would be a false claim; it flagged none. One expectation was restated: `test_s3`'s requalification list, whose exact original expectation holds again once attestations are not requalified. A new test, `OneAuthorshipRule.test_nb3_unknown_authorship_admits_only_an_attested_human`, pins both the classification and routing's eligibility. Each of the three changes, reverted alone, fails a test.

**Consequence, disclosed (Manual §32.2's "broad authorship fails closed").** Until content has an admitted authoring record, every human review, acceptance, plan acceptance, equivalence or completeness of it needs that human's `NON_AUTHORSHIP_ATTESTATION`. On a shadow ledger every subject is `LEGACY` or `UNGOVERNED`, so nothing is owed now. A cutover (G4) meets it for all pre-existing content.

**Same-family re-check of bb92b348 and the NB-3 repair (d0f10442).** No SERIOUS CHALLENGE, and no code defect. The rewrite is clean: an instrumented full suite (8,573 human evaluations in 233 tests) found the helper never attested a human the code counts as an author. NO-PASS on two test-only blockers, repaired:
- **B1, the routing test was vacuous.** Its scenario derived no `REVIEW(X)`, so the check under `if` never ran, and mutant M13 (routing back to the makers) survived. `test_nb1_a_reviewer_dispatched_is_one_admission_would_find_independent` now builds the case: an earlier producer of content a candidate restores is never an eligible judge.
- **B2, NB-3 rested on unpinned conditions.** The attestation must be co-submitted (a later one changes nothing, §5.10 (a)) and must be the judge's own (catalogue §3.4). Both are now tested.

Its notes, taken up:
- a test NB-3 had made vacuous now attests its consumer and asserts that premise (`test_group3_discriminators`);
- the conformance and Phase E plan fixtures attest their plan acceptances, so their plans are accepted again;
- each newly built supersession target is asserted not `None`;
- reading F11 states the closure's canonical order;
- reading F12 makes the requalification exclusion explicit;
- the test helper reads derivation's `REQUIREMENT`;
- the dead `work_authors` is removed, its two tests reading `judged_authors`.

Kept for their steps:
- **Step 8 (briefs, dispatch).** A human dispatched to judge content of unknown authorship must be told the attestation is required, or the answer is predictably non-independent (§5.10 (f), §16.5).
- **Step 4b-ii.** Whether Admission refuses a `NON_AUTHORSHIP_ATTESTATION` from a human the ledger records as a producer: Manual §5.10 (f)'s "must not be one of them or must present" against "an author is never independent". The catalogue reconciles them by a challenge against the credited record. Also: Admission's admission of a co-submitted attestation.
- **To check at the owner (`items.Item.derived`).** Item work is derived from an acting, unsuperseded plan acceptance even when it is `nonind` (M30 survives; §11.2).
- **Unverified.** For an integrated-result review, routing reads the parts' outputs while classification reads `_target_work`'s current content; they could diverge after a replacement.

**Same-family review of step 4b-ii (8d274c4b).** No SERIOUS CHALLENGE; nothing is wrongly admitted at Admission today. NO-PASS on four blockers, repaired:
- **B1, the re-issue branch skipped every check but the envelope signature.** It retained records whose actor, binding, lineage or `governs` failed, and stored unverified harness material. The unlisted case now runs the whole authentication against the retired key; only "listed" differs. The engine then runs step 3's authorization on it. It retains only the never-lost records that pass every check, under the authenticated envelope, and stores nothing when a harness attestation or credential fails. An envelope issued at or after its key's retirement is no outstanding one (`TrustRoots.retired_at`; note N4).
- **B2, a forged `reissue_of` discharged `REISSUE`.** It lost the never-lost record for good, and the shipped test enshrined it. Admission now refuses any record citing `reissue_of` as unsupported until step 8's Dispatcher resubmits. Derivation discharges only on an admitted record that is the retained one apart from its binding and provenance, by the same actor, with the same lineage class (catalogue §8.3 step 3).
- **B3, the refused-alone path was reachable and untested.** A surviving mutant admitted a challenge, and another hung the queue. Both the fail-closed check and the decision now read one rule, `engine.blocking`. A test through a stand-in `authorize` pins it.
  - A challenge co-submitted with its adjudication now fails closed (`SCHEMA_UNSUPPORTED`): step 5's strictly-earlier rule is 4d's (note N3). That made the path unreachable again with real records.
- **B4, a D1/D2 claim's adjudication needed a human.** Catalogue §3.4 says "R2, or R3 (Serious Challenge, D1/D2 claims)", and nothing enforced it. `chain_needs_human` now makes a chain whose root is about a D1 or D2 claim R3. It also stops at the root, the first record that is not challenge-tier (note N1).

Its notes:
- **Taken up.**
  - N7: judge selection reads the chain's class, now tested.
  - N4: a re-issue's record list is a set.
  - Every reversion of these repairs fails a test, and the review's surviving mutants M9, M11, M12, M18 and M30 are killed.
  - M13 (retain every passing record) is now equivalent: a retired key's envelope refuses every non-never-lost record per record.
- **Kept.**
  - N2: "any human record makes the chain R3" over-approximates §3.5's "an R3 human record". It is conservative (it only refuses) but costs liveness; the precise rule is Stage S's.
  - N5, for step 8: "keeping its original actor" under "the re-issued task's envelope" meets §25.1's rule that an envelope authenticates only its own task's agent.

**Narrow re-check of 799d1bac.** No SERIOUS CHALLENGE; nothing is wrongly admitted today. B2, B3 and the B1 code are closed. NO-PASS on two residual blockers, repaired:
- **B1, residual: two checks with no test.** Mutants survived the whole suite after deleting the envelope signature check (every path) or dropping authorization on the re-issue path. Two tests now pin them: a forged envelope signature, on an in-force harness envelope whose attestation still verifies and on a retired key's unlisted envelope, stores nothing; a record that authorization refuses under an unlisted envelope is neither retained nor queued for `REISSUE`.
- **B4, residual: roots whose domain reads `None`.** The root rule read `domain_of`, which is undefined for a completeness, a report, a record target or a multi-domain root, so such a chain over a D1 unit counted as R2. `chain_needs_human` now reads `judged_units`: the policy units, else a completeness's or integrated result's scope, a report's units, or, recursively, what a record target judged. The root is R3 when any of them lies in D1 or D2, and when none can be determined, a unit is undeclared or no root is reached (fail closed). `domain_of` itself is unchanged, because widening it re-routes the owner and adjudicators policy names for record-target kinds. Tests cover a completeness, a report, a record target, a multi-domain root, a root with no units and a challenge made directly on a triple.

Its notes, kept:
- The binding object of a withheld unlisted envelope is stored although nothing under it is retained. It is inert.
- `_resubmitted` is dead until step 8. N5 stays open there.
- **For Stage S, or the domain owner's next change: `domain_of`'s gaps.** It reads no completeness scope, report units or record target, so the owner and adjudicators for those kinds come from the default domain.

**Narrow re-check of c5a6457f.** No SERIOUS CHALLENGE. B1 is closed. NO-PASS on one narrow blocker, repaired:
- **B4, still open for multi-record roots.** `judged_units` returned the policy units whenever they were non-empty, and for an `IMMATERIALITY` those are the first covered failure's alone, so the class depended on list order. `judged_units` is now the union over everything the root judged: a work judgment's units, a plan acceptance's items, a realization's claim, an assessment's realization, every record a record target names (recursively), a scope, a report's units and a subject.
- **Tests added:** both orders of a two-failure `IMMATERIALITY` and of a two-record report, a D2 failure and an undeclared unit. A realization root reads its claim, so a challenge of an agent-run D3 observation is R2 again rather than failing closed (the review's note).

Its answer on `domain_of`: not a blocker. The class reads only `judged_units`; `domain_of` chooses the policy section, and judge selection filters it to humans wherever the chain is R3. The gap costs routing precision, and it stays a Stage S note. Kept: roots with no units (`task`, `obligation`, external and `content_ref` targets) fail closed, which is acceptable because challenges against them are rare.

**Same-family plan review of 96e13c0b (revision 5, 4c's split).** No SERIOUS CHALLENGE: the tensions found lie in the non-authoritative catalogue or in the plan's own readings. It confirmed the plan's code claims, found the order 4c-i → 4c-ii → 4c-iii right, and traced no cycle through `Frame.exists` (the freeze's `status1` reads challenge-tier and loss-boundary records only). NO-PASS on five blockers. Revision 6 repairs:
- **B1, F17 over-generalized.** Read at a later head, an integrated `X`'s frame is `T_n` or a conflict, which would empty or end its conformance and reopen an integrated item, against §7.6, §10.4 and SD-40. Only unintegrated transformations are read at the head; an integrated enactment's frame facts are fixed at its integrating head, as `binds_tenure` reads them. A test pins it.
- **B2, the adoption gap misattributed.** Schema 1's `INTAKE_DISPOSITION` target and outcomes differ from catalogue §3.4 and §18.3: a transcription defect of Q-F4's class. Q-F6 (i) now puts SD-67's two options to the stakeholder; both ledgers hold only genesis.
- **B3, the reserved-leaf check missing.** Manual §1.9 (A9) checks the reserved leaves on every admission. 4c-ii now names one owner for genesis, admission and `Frame.exists`, with `STRUCT_RESERVED_LEAF`.
- **B4, F15 changed §2.5's allocation.** "Would make" is causal. Only a defect an affected subject has in the frame and not at the head refuses; `Frame.exists` reads the same difference, so foreign absorptions leave pending frames alone.
- **B5, frame identity and rebase unplaced.** 4c-iii refuses a record naming an unknown transformation (`REF_TRANSFORMATION`), and rebase-frame records fail closed until step 5, which now builds step 2's rebase check and §7.6's rebase counting.

Its notes, taken up:
- the frame's structure is the 4c-ii owner's `Σ_{n+1}`, and the textual tension in catalogue §7.2 goes to Stage S;
- the cutover source-mode condition moves to Phase G, and a lifecycle record declaring a frame stays unsupported;
- the enactment check reads conditions 1-4;
- prospective tenure covers every subject of the frame's structure;
- the freeze reads the admitted state;
- F14 names the record route;
- each conformance template's tree, and one owner of the bound write scope;
- `STRUCT_REVALIDATE`'s recording;
- line 139's stale "until 4c";
- the `id(X)` fixture migration;
- Q-F6 (ii)'s release must be evaluable outside the frame;
- fail-closed artefacts in the difference study;
- the mode-mixing disclosure.

**Narrow re-check of efa2c450 (revision 6).** No SERIOUS CHALLENGE. B2 and B3 are closed. NO-PASS on four residuals, which revision 7 repairs:
- **R1, what is fixed at `k - 1`.** Only the frame's tree and structure facts. Currency of an integrated enactment's frame records takes catalogue §7.3's admitted-state column, so `Conformance._current` and `required_evidence` no longer read a frame rebuilt at the head; a test pins the assessment in the admitted state.
- **R2, too coarse a defect key.** Keyed by code, unit and detail, as genesis keys its check, so a second same-code defect is new.
- **R3, rebase unbuildable in schema 1.** The `frame` field cannot carry `(B', C', A')`. A rebase-frame record is refused `REF_TRANSFORMATION`, the gap is Q-F6 (iii) with (i)'s two options, and step 5's rebase work waits on it (its row now names §7.6, the rebase clause and `derivation`).
- **R4, revision 6's frame structure against Manual §7.2.** The edge case routes to `STRUCT_REVALIDATE`, so wherever a frame exists `Σ_n ⊕ Δ_Σ(X) = Σ_{n+1}`; the catalogue's precedence goes to Stage S. The reviewer withdrew the note that suggested the revision 6 text.

Its notes, taken up:
- the write-set templates resolve regions, owners and scope on `T_n` and `M_n(X)`;
- §6 names who settles each part of Q-F6;
- Q-F6 (i)'s option (a) now covers the `identity` basis grammar, drops `units`, and gives `QUARANTINE` its paths.

**Narrow re-check of 05c35820 (revision 7).** No SERIOUS CHALLENGE. **PASS:** R1-R4 and notes 2-4 are closed. Its four notes are taken up:
- the R4 refusal is a fail-closed stronger rule pending Stage S, not the Manual's answer, so §6 lists it;
- Q-F6 (i) (a) also corrects `INTAKE_CLASSIFICATION` and the fixtures;
- shrinking an existing cycle is disclosed as refused;
- Q-F6's heading now counts three acts.

**Narrow re-checks of 00fb3cb4, c23f3cee and c98bb647 (step 4b-ii's last repairs).** No SERIOUS CHALLENGE in any. The union of 00fb3cb4 closed B4's semantics but recursed with no memo, so a DAG of reports each targeting the previous two was walked once per path (exponential), and once memoized (c23f3cee) a linear chain of about 400 overflowed the stack. `judged_units` is now one worklist with a visited set (c98bb647): **PASS**. A depth-34 DAG and a 1000-deep chain are tested, and dropping the visited set fails the first. Kept: mutants L5, L6, L9 and L10 (work units, plan items, an unwrapped gate subject, an equivalence's `unit`) fail closed to R3 or are near-equivalent. **Step 4b-ii is closed.**

**Step 4c-i built.**
- **The frame.** `frame_of` builds a pending transformation's frame at the head and an integrated one's at its integrating head (reading F17).
- **The write set.** It and the changed files are the frame's (`T_n` against `M_n(X)`, with modes). `Conformance` reads them, and its write-set templates resolve on the frame's two sides. An integrated enactment's frame records are current in the admitted state.
- **One owner each.** `protected_surfaces` is the one protected-surface owner for lint and conformance. `transformation_id` is §7.1's `id(X)`; a result naming another identity fixes nothing, and every fixture computes it.
- **Mutants.** Nine were run, with two survivors:
  - modes not passed (M7), equivalent while no frame carries a cutover;
  - scope resolved on `tree(C)` (M9), killed by a unit-named write scope that a concurrent file joins.

**Same-family review of step 4c-i (2280eae1).** No SERIOUS CHALLENGE; nothing is wrongly admitted, since content requests stay `SCHEMA_UNSUPPORTED`. NO-PASS on two blockers, repaired:
- **B1, three owners of the first submitting result.** Only `transformation_of` checked §7.1's identity, so a result naming `id(X)` with another candidate became `X`'s enactment and `submitting_result`. One predicate, `state.submits`, now serves `transformation_of`, `State.submissions` and `Workflow.submitting_result`; a test puts the forged result first.
- **B2, the write set's two structures and mode maps untested.** My M7 equivalence claim was wrong: a composite made a subject moves a part to a subject of another mode, and only its governance signature differs. New tests cover that, a new D1 subject over unchanged content, and an effect arising only where `C` meets `T_n` (a concurrent widening of a unit's scope over the file `C` edits).

Its notes, taken up:
- `Conformance.base_view` is the frame's, so the layer-direction template compares one structure;
- `A` in `id(X)` is a set of exactly `{key, value}` elements;
- a historical state reads its frame at its own head (F3).

Kept: the near-equivalent survivors F14 and F21-F25, reachable only through kind changes or deletions, and F15.

**Revision 8 (reading F18, Q-F7).** Before building 4c-ii, a read of `ssdp-shadow-2`'s genesis through the program found it declares only one of §1.8's three reserved leaves, because the genesis check enforced only A9's refusal clause. F18 applies §1.9 as written from 4c-ii, and Q-F7 puts the ledger's disposition to the stakeholder.

**Narrow check of 0f209be6 (revision 8).** No SERIOUS CHALLENGE: the Manual is clear, and the defect is the program's genesis check and the artefact signed under it. F18's reading and the whole-structure application were confirmed. NO-PASS on one blocker: Q-F7 claimed no request could be admitted on the ledger, but one authoring the two leaves passes. It now carries the in-place repairs (d1) and (d2) with their dependencies and costs, and recommends (b) with (d2). Its notes are taken up:
- the kinds' source;
- the check carried by no unit, so S0 and S2 are unchanged;
- a dated note on the genesis evidence;
- NEXT ACTION's reference to Q-F7.

**Narrow re-check of 64a03303 (the 4c-i repair).** No SERIOUS CHALLENGE. B2 is closed. NO-PASS on two blockers, repaired:
- **B1, a fourth owner.** `History._producing_results` still took the first result naming `id(X)`, so a forged earlier result's lineage authored `X`'s content and made the maker's own review independent (an A5 fail-open). Admission's `producing_context` had the same pattern.
- **B3, a crash.** The new predicate indexed `adopts` elements that schema 1 allows to be any object.

`submits` now lives beside `transformation_id` in the ledger schema: total, requiring exactly `{key, value}` elements. History, frames, `State`, the workflow and Admission's producing context all read it. Tests cover a forged first result, which now authors nothing, and a malformed `adopts`, which submits nothing and crashes nothing. Kept: S4, the base view's structure, is reachable only through a concurrent declaration change.

**Narrow re-check of dcae3e90.** No SERIOUS CHALLENGE. B3 and the History and producing-context parts of B1 are closed, and S2's refusal is unweakened: its cases are two submitting results. NO-PASS on one blocker, repaired: `Judgments._binding`, `binding_conflicts`, `_key_of` and `_base_position` still read the first result naming `id(X)`, so a forged bare-id result fixed a review's judged scope `J` (and so its reach) and set derivation's §7.1 check, disagreeing with Admission's. They now read `Judgments._submitting`, the results that `submits`. A test shows `J` and `binding_conflicts` unchanged by a forged result. The reviewer's grep found every other reader of a result's transformation gated by the enactment or `submitting_result`.

**Narrow re-check of 1a3c262d.** No SERIOUS CHALLENGE. **PASS:** `_submitting` is the only route in `Judgments`, and the forged-result probes leave `J`, `binding_conflicts`, `makers` and the maker's own review unchanged. **Step 4c-i is closed.**

**Revision 9 (F18 at frame existence).** While starting 4c-ii, the fixtures were found to declare the reserved leaves only in some genesis JSON, never in their in-tree manifests. Revision 8's F18, read literally into `Frame.exists`, would end every frame in such a ledger (the real shadow ledger included). F18 now splits the two owners. Admission refuses a merged structure failing a whole-structure check. The frame reads only the failures `Σ_n` does not already have, matching catalogue §7.4's "`Δ_Σ(X)` is well-formed" and F15's causal reading of defects.

**Narrow check of b3e94f09 (revision 9).** No SERIOUS CHALLENGE. NO-PASS on one blocker: the split changed Manual §7.4's single exception. §7.4 reads "the proposed structure is well formed (every structural check except the enactment condition)", the catalogue defines `Δ_Σ(X)` well-formed as the full step 4 set, and enactment is excluded only because frame records satisfy it. The readers that treat a frame as integrable but for enactment are conformance, `REVIEW(X)`, the pending route, frame currency and the Dispatcher's integration trigger. Under the split they would spend reviews on an integration Admission must refuse. **Revision 10 reverts the split.** The fixtures declare the leaves instead, and frames on `ssdp-shadow-2` wait for Q-F7.

**Reading F19 (revision 10).** With the reserved leaves injected into every fixture manifest (§1.8), about 50 Phase D-F tests changed. The structural owner raised no finding in them. The cause was `ssds.unclassified`'s revision over the whole tree: it entered every `Δ(X)` and every judged scope, and reviews stopped covering their content. F19 reads its content as the bytes it owns.

**Step 4c-ii built.**
- **The owner.** `derivation.structural.StructuralCheck` is §8.3 step 4 (a)-(c)'s one owner. It covers:
  - `Σ_{n+1}` with each key's class against `Q_n`;
  - the R4 case routed to revalidation;
  - §1.9's static checks, term resolution and the reserved leaves (`baseline.reserved_leaf_problems`, also genesis's check now);
  - mode mixing;
  - the F16 fail-closed cases;
  - the freeze at source and destination, read in `D_n`;
  - S0 defects read causally on affected subjects.

  `Frame.exists` reads every finding (§7.4).
- **Reading F19, in the content model.** `ssds.unclassified`'s region is now the bytes it owns (`TreeView.regions`). So its content, write-set modes and region comparison, and every region reader (`units_in`, `owners`, write-scope containment, protected surfaces), see only those bytes. It contains no other unit, so it carries no other unit's semantic declarations.
- **Fixtures.**
  - Every fixture manifest declares the three leaves; the genesis fixtures also write the policy file.
  - Group 1's content and derivation cases keep their stated inputs, without the leaves.
  - Expected values changed only where the leaves are now real units: subject lists, mode maps, a completeness over every unit, the genesis refusal text.
  - A candidate adding an ascending relation now has no frame (§7.4), so the layer-direction template's case reads the frame's absence.
- **Mutants.** Fourteen on the owner, all killed. The last needed a test that a defect on a subject the request does not affect is S2's.

**Same-family review of step 4c-ii (2aadf331).** No SERIOUS CHALLENGE. **NO-PASS on eight blockers, not yet repaired** (paused 2026-10-25). Probes are in `/tmp/claude-1000/rev/probes/`.
- **B1, a write-scope fail-open on deletion.** `outside_scope` reads only the merged side. Deleting a file owned only by `ssds.unclassified` (a pre-existing gap for ordinary units too) is CLEAN. Repair: a write-set unit lies within the scope on both sides; `AUTH_WRITE_SCOPE` reads the same owner.
- **B2, nested subjects missed by the freeze.** `_members` uses `subj`. Repair: `is_member_of`.
- **B3, parts' defects missed.** A new defect on a part of an affected subject is missed. Repair: also refuse where `subj(d.unit)` is affected.
- **B4, the outermost owner's revision ignores order.** Moving another unit's span past unclassified bytes changes no revision. Repair: hash each path's ordered owner sequence, with unclassified's bytes.
- **B5, reserved leaves not checked to be leaves.** A composite `ssds.unclassified` hides its bytes in its residual. Repair: role leaf, no members, no `part_of`; amend F18.
- **B6, the freeze's region reading.** Path-set changes refuse wrongly, while anchor moves pass. Repair: record a reading (proposed F20: the freeze reads declarations and term resolution status, never bytes or file sets) and implement it consistently.
- **B7, missing cases.** There are none for STRUCT_ILLEGAL_CYCLE, STRUCT_SINGLE_DEFINER, STRUCT_SDG_MALFORMED or STRUCT_SDG_NOT_LAMINAR, none for PROVISIONAL or REVOKED freezes, none for "a frame that no longer exists derives what a conflict derives", and no layer-direction positive case where its frame exists. Mutants V03 and V04 (unclassified's semantic declarations and modes) also survive.
- **B8, revision 9 residue.** `frame_findings`, `WHOLE_STRUCTURE`, `Finding.scope` and stale docstrings in structural.py and frames.py.

Its notes, open:
- N1: `s0` IMPORTS read unclassified's prefix resolution.
- N3: F19 departs from catalogue §1.5's formula (Stage S tension).
- N4: an unparsed `T_n` manifest leaves new keys authored.
- N5: `renamed_from` or delete-and-recreate launders a kind change past F16 (ii).
- N7: brittle fixture injection.

Cost: the full suite is +29% (cache `TreeView.regions`; reuse `frame.view` and the head `s0`).

**SD-69 (item 63, 2026-10-26): Q-F6 and Q-F7 settled as recommended.**
- Q-F6 (i) and (iii) are corrected in schema 1 in place, and (ii) goes to Stage S.
- `ssdp-shadow-2` is kept for step 10 and repaired in place by adoption once Q-F6 (i) is built.
- Placed by revision 12: the schema-1 correction and the adoption path are step 4c-iv. The ledger's in-place repair opens step 10, once steps 5-6 let a records-only adoption commit. Rebase stays in step 5.

**The 2aadf33 repairs (revision 11).** B1-B8 are repaired:
- **B1, write scope.** A write-set unit lies within the scope on both sides of the frame, each side resolved in its own tree. A deletion, of an outermost-owner file or of an ordinary unit's, is now outside.
- **B2, B3, B5.** The freeze counts every unit inside the subject by membership. A new defect on a part of an affected subject refuses. Reserved leaves are top-level leaf subjects with no members (F18 amended).
- **B4, the outermost owner's revision.** It keeps each file's owner order (F19).
- **B6, the freeze's regions.** Recorded as reading F20 (resolution status, never bytes or file sets) and implemented.
- **B7, the named cases.** STRUCT_ILLEGAL_CYCLE, STRUCT_SINGLE_DEFINER, STRUCT_SDG_MALFORMED and STRUCT_SDG_NOT_LAMINAR; BLOCKED, PROVISIONAL and REVOKED freezes; a nested subject; both deletions; a structural and a merge-conflict non-existence deriving the same hit; the layer template judging where its frame exists; and the outermost owner's revision under order, mode, other units' edits and declarations.
- **B8, residue.** Revision 9's split and its prose are deleted.

Taken up:
- N1: derived `IMPORTS` attribute only owned files to the outermost owner;
- cost: `TreeView.regions` cached; the owner reuses `frame.view` and the admitted `s0`.

Kept:
- N4: a `T_n` manifest that does not parse quarantines every key of `Σ`, so a key new in `C` is authored; a strict reading routes it to revalidation. It is an edge case, kept for Stage S.
- N5: in F16.
- N6: the doubled report of a reserved leaf's kind.
- N7: the fixture's textual injection check.

**Narrow check of ad8daeb6 (revisions 11-12).** No SERIOUS CHALLENGE. NO-PASS on four blockers in SD-69's placement. Revision 13 repairs:
- **B1, dispositions with no built effect.** 4c-iv admits only `ABSORB` of a quarantined delta; the rest of §18.3 stays Phase G's, and §1 carves out SD-69's path.
- **B2, the repair against F1 and §6.** Both now name SD-69's exception, and the G2 shadow boundary holds.
- **B3, §18.4's promotion clause.** A promoting adoption fails closed.
- **B4, `A`'s element form.** An interim D4 form is fixed, `{absorption, key, value}`, and marked for Stage S.

Its notes, taken up:
- F20 discloses its narrower "regions" and goes to Stage S;
- F18 cites catalogue §1.8 for "top-level";
- step 10 names one `ABSORB` per key, the genesis policy path and the disclosed non-independence;
- step 10's dependencies are 4d, 4e, step 5, and step 6's compare-and-swap and witness checkpoint;
- F16's rename note names the domain rule, and 4c-iii fails closed on a kind-changing `renamed_from`.

Separately, a test now pins §11.2's requirement that only a current plan acceptance makes an item issuable (the re-check of d0f10442's M30). And `G2-S4-FINDING-INDEX.md` now dispositions A10's Review findings, so `run_models.py --seeds` passes again.

**Same-family plan review of 07284144.** NO-PASS as a plan, with seven blockers and no SERIOUS CHALLENGE. Revision 1 repairs them:
- **B1, the wrong observed ref.** `main` is behind and does not contain the genesis baseline. F1 and Q-F2 (i) now put the observed ref to the stakeholder as a deployment setting, and step 10's absorption test reads observed heads.
- **B2, a boundary resting on one CLI check, and records-only fencing.** The real-shadow Admission is observe-only. Records-only admissions are never fenced. The boundary check sits at Admission's entry for every route. Step 10 tests a restart after a records-only admission and library and Dispatcher routes.
- **B3, the runner sandbox and SD-59.** Reading F2 states the sandbox properties, and Q-F3 puts the workspace root and the sandboxing dependency to the stakeholder.
- **B4, fitness rule B1.** Its revision is stated, with three named exceptions and violation tests.
- **B5, publication classification's owner.** Moved to `derivation`, with group 4 run by ledger-only replay and failpoints.
- **B6, unplaced items.** The transports, Dispatcher functions, task-bound interface, RR-11 judge selection, kept-fence lifecycle conditions, named discriminators and the §7.1 refusal are placed in steps.
- **B7, command names.** The Manual's `admission serve`, `dispatcher serve` and `mcp serve` are used.

**Same-family plan review of 53e8c119 (revision 1).** B1, B2, B5, B6 and B7 are repaired, and B3 and B4 partly. There is one new blocker, and no SERIOUS CHALLENGE. Revision 2 repairs:
- **P1, Q-F3's root outside the home.** It contradicted Manual §26.3 (A7), and its reason misdescribed `Home.check`. Workspaces now go under `runs/` in the home, outside the ledger trees.
- **P2, unowned work under the fitness revision.** Four named exceptions now cover the Git-envelope transport and the stub harness, and Admission reads `obs` through a supplied `content` reader.
- **P3, operator trees.** Steps 2-9 create them only in scratch homes, their layout goes in Q-F3, and the non-existent incarnation tree is dropped.

Its non-blocking findings are taken up:
- N1: a rewritten observed ref, with a step 6 test;
- N2: the boundary check's owner, predicate and later-phase records;
- N3: no keys now;
- N4: Q-F2's considerations, the option rather than Core configuration, and the ledger id;
- N5: Q-F1's population;
- N6: §24.2 kept in Phase F on fixtures, so no deviation from the G2 row;
- N7: step 5's evidence rerun after step 9;
- N8: E20 placed (Phase D NF8 was already repaired in Phase E step 1);
- N9: a new `History` per extension;
- N10: E33 retires at the new genesis.

The first review's non-blocking findings were taken up as well: citations and `LINEAGE_MIGRATION`'s `obs`; F3's witness premise; F4's host key; the keys as a genesis question; step order (a minimal commit path in step 2; dependent tests rerun after steps 6 and 9); external custody, E5, E6 and conformance at head placed; E30, E37 and E38 kept fail-closed; the takeover wait and runner time cap; Phase H taking §24.2's re-encoding. Its reposing of Q-F1 and Q-F2 is adopted.
