---
kind: ssds-shadow-phase-plan
workplan_id: SSDS-8.0-G2-PHASE-F-PLAN
protocol_version: 7.2.1
target_system_version: 8.0.0
status: proposed
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
STATUS: PROPOSED. Companion to the G2 shadow workplan, Stage D (§5.2 Phase F row). It concretizes that
        row into files, modules and test groups. It adds no mechanism beyond the settled register
        (G2 workplan §4.2) and changes no Manual decision.
START:  the Phase E Review PASS at c2b1ec2 lets Phase F's dependent work start (G2 workplan §5.1 item 5):
        qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-C2B1EC2-DIFFERENT-FAMILY-PASS.md.
SHADOW: no SSDS authority over any subject; every subject LEGACY(p) or UNGOVERNED; no cutover. The
        document-controlled 7.2.1 baseline governs. Phase F appends only to the shadow ledger in the
        SSDS home and publishes only to integration refs in fixtures and scratch repositories, never
        to a governed ref (reading F1).
DONE SO FAR: nothing; the plan awaits Q-F1 (§7) for steps 10-11 only. Steps 1-9 do not depend on it.
NEXT ACTION: step 1 (PERF-E1, the derivation cost Admission's hot path inherits).
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
- real owners (item 4);
- Core's suite and the frozen-profile tests pass unchanged (items 1 and 6);
- no live agent run without an authorized campaign (item 7).

The Phase D threat boundary for the SSDS home (SD-59; Phase D plan §2) holds for every operator file Phase F writes: Admission and runner keys, the incarnation identity, witness files, leases and runner workspaces.

**What Phase F does not build** (each later phase's, with reason):
- intake, the migration path and external units (Phase G);
- adversarial, privacy and fault harnesses beyond the failure points group 4 names (Phase H);
- any live agent trajectory or measurement spend, including the Dispatcher's harness route with a real model (a campaign, G2 workplan §5.1 item 7);
- moving any subject to `NATIVE` (a cutover, G4).

## 2. Placement

The component table of Phase D plan §2 stands. Phase F fills owners as follows.

| Owner | Gains in Phase F | Register rows |
|---|---|---|
| `admission` | the request model and its content identity, the queue (§8.1-§8.2); validation steps 1-9 with closed reason codes (§8.3-§8.4, catalogue §8.3-§8.4); absorption (§8.6); the commit point with checkpoint distribution to the witness quorum (§22.4, §23.3); publication classification, the publisher's incarnation, fencing and settlement (§22.1-§22.3); the human-gated recovery and lifecycle entries (§23.6-§23.8, §24.2, §25.2); protected surfaces (§25.3); bounded secret checks and input bounds (§24.1, §25.4) | §8, §22, §23 (Admission side), §24, §25 |
| `dispatcher` | issue keys and signed task envelopes with lineage classes and launch attestations (§12.2); issue from derived readiness with serialization surfaces, one coordination task per plan and per-worktree leases (§9.1-§9.2, K2); designated-runner execution in a workspace the Dispatcher owns, materialized from the content model's tree representation, and the `REALIZATION` observations it submits (§17.2, §17.3, §17.5) | §9, §12.2, §17.5 |
| `derivation` | §17.4 admissibility and currency (deferred from Phase D); the §10.2 obligations §17's machinery triggers (`REALIZE`, `ASSESS`, `RERUN`, `READING`), so required evidence with an admitted realization stops being `UNAVAILABLE`; the cited-premise support-graph component check Admission's step 5 calls (Phase D NF2); the incremental head derivation Admission validates against (PERF-E1) | §5-§7, §10.2, §17.4 |
| `ledger` | witness checkpoint writing for the declared witness kinds Phase F uses (append-only Git refs and append-only directories, `LOCAL_TRUST` on the real shadow ledger); authenticated retirement statements (Phase D NF3) | §21, §23.3 |
| `interface` | `submit`, `report` and `decide`, which build typed requests and hand them to Admission (§16.1); the qualified presentation of Admission's outcomes | §16.1 |
| root module `ssds.cli` | mounts `submit`, `report`, `decide`, `admit` (the Admission process for one ledger) and `dispatch` (the Dispatcher for one ledger) | §26.3 |

**Fitness.** Rule B1 is extended so that only `admission` imports the append path, and only `dispatcher` holds an issue key or runner key. No module other than `admission` writes the shadow ledger or a witness, and no SSDS module holds a credential for a governed ref. The fitness check gains the corresponding import and credential rules first (step 2), as Phase D's did.

## 3. Steps, in order

| Step | Modules | Realizes register rows | Tests (under `orchestrator/tests/ssds/`) |
|---|---|---|---|
| **1** derivation cost | `derivation`: remove the repeated historical evaluation PERF-E1 found (`Items.discharged_at` rebuilding a workflow per part), and the incremental head derivation Admission validates each request against, equal to from-scratch derivation (Phase D's incremental-equals-from-scratch property) | §5, §10.4, §13.7 | the PERF-E1 seven-round history within a stated bound; incremental equals from-scratch over every Phase D and E fixture ledger; the selector, settlement and lifecycle tests unchanged |
| **2** requests and the early steps | `admission`: request identity and idempotency (§8.1), the queue (§8.2), steps 1-2 (schema, secrets, reference; §8.3), closed reason codes (§8.4), input bounds (§25.4); fitness rules for the append path and credentials | §8.1-§8.4, §24.1, §25.4 | an identical request returns the recorded decision and appends nothing; each reason code from a case that triggers exactly it; `SECRET_DETECTED` on each pattern family and on high entropy, not on digests; oversize inputs refused |
| **3** envelopes and keys | `dispatcher`: issue keys, envelope signing, lineage classes and launch attestations (§12.2); `admission`: `KEY_LIFECYCLE` registration, rotation, retirement listing outstanding envelopes, compromise from a position (§25.2) | §12.2, §25.1-§25.2 | an envelope under a retired, uncompromised key admits only never-lost records it lists; a compromised key's later envelopes refused; `UNKNOWN` lineage credits no independence |
| **4** authorization to currency | `admission`: steps 3-6: authorization, including independence and adjudication eligibility (§5.10 (f), RR-11) and supersession authority by the superseded kind; structure on the merged tree; dependency well-formedness with the cited-premise component check; currency with never-lost salvage. Also protected surfaces (§25.3) | §8.3 steps 3-6, §8.5, §25.3 | group 3's admission half: 51070e5 N3's adjudication-independence refusal; f03b15e N5's supersession-authority cases; S1 objection cases at Admission. Group 2's admission half: never-lost challenges, failing assessments and adjudications admitted whatever the request's fate. `AUTH_PROTECTED` on each protected surface |
| **5** legality and regression | `admission`: step 7 (one result per task, result-only `HARD` templates, SD-26 one integration per enactment, answered obligations, revision assessments first, the judged-content support check replacing `STALE_RETAINED`, settled fenced admissions, claimed discharge) and step 8 (no collateral evidence regression, R15). Also the refusals Phase E deferred: answers to decisions not derived, including a dropped part's, and invalid partitions | §8.3 steps 7-8 | group 5's admission half: S5 §8 `rejected_request_salvages_never_lost`, `unclean_result_refuses_passing_judgments`, `clean_request_admits_all`; the refusal of a candidate bound to an obligation no longer derived; `same_key_other_scope_after_issue` and the judged-content cases; a fall from `T` to `P` refused as regression |
| **6** commit, publication, fencing | `admission`: step 9; single-ref compare-and-swap; at most one provisional entry; the checkpoint quorum; absorption (§8.6); publication classification (§22.2); the publisher's incarnation, fencing absorption, settlement and the ABA policy (§22.3); crash recovery by request identity (§22.4); `ledger` witness writing | §8.3 step 9, §8.6, §22, §23.3-§23.4 | group 4: S5 §22 `publication_classification`, S5 §23 `deployment_classes_sound` at genesis and redesignation; 362af9f N6 (re-application of a fenced or `OVERTAKEN` integration); 441cf5c N7 (a rewind is `ROLLBACK`); 730490d N2 (a foreign return to `B_n` is `LATE_PUBLICATION`); 8a75346 N2 (a crash after the CAS, before the outcome is recorded); the five S3 kept-fence cases (Phase E reading E31) |
| **7** loss and recovery | `admission`: `LEDGER_LOSS`, `FORK_RESOLUTION`, `WITNESS_SET_REDESIGNATION`, `REPLICA_REDESIGNATION`, `LINEAGE_RETIREMENT` and `LINEAGE_MIGRATION` entries, human-gated, with `obs = null` (§22.1, §23.6-§23.8, §24.2); `CONTINUITY_ATTESTATION` (§23.7); `derivation`: the loss boundary and `REQUALIFY` obligations | §23.5-§23.8, §24.2 | S5 §23 `loss_bounds` and `qualification_states` at Admission; each §23.8 table row as a fixture history; a stale-consistent restore resurrects nothing |
| **8** scheduling | `dispatcher`: issue from derived readiness bound to a named `H*`; serialization surfaces and one coordination task per plan; per-worktree leases (K2); joint-invariant review obligations (§9.2) | §9 | at most one mutating task per serialization surface; lease expiry changes scheduling, never correctness; an overtaken basis revalidated, never silently admitted (§9.1) |
| **9** runners and evidence | `dispatcher`: a designated runner materializes the exact tree in the content model's representation in a workspace the Dispatcher owns (reading F2), records its declared execution attributes and unpinnable reads, and submits `REALIZATION` observations with canonical outcomes (§17.2-§17.3, §17.5); `derivation`: §17.4 admissibility and currency, and the realization-triggered obligations | §17 | group 1's runner half: the CRLF, mode, symlink, gitlink, LFS and submodule fixtures materialized by a runner. Group 2: the S5 §6 matching cases with realizations admitted. A fixed-attribute mismatch is inadmissible; an incomplete realization enters no assessment; agent-reported results are never admissible |
| **10** shadow operation | `interface`: `submit`, `report`, `decide`; `ssds admit` and `ssds dispatch` on the real shadow ledger (reading F1): absorbing document control's integrations and admitting records-only requests, with nothing published | §8.6, §16.1 | on the real shadow ledger: the product repository's refs, objects and status unchanged after `admit`; every document-control commit since genesis absorbed; `ssds submit` with candidate commits refused by the shadow boundary's check before Admission, appending nothing (reading F1) |
| **11** difference study | the comparison Q-F1 settles (§7): each material difference between document control and what SSDS decides, classified and independently reviewed | §5.2 Phase F exit | per Q-F1 |
| **12** exit | assembly of group 4 and the admission halves of groups 2, 3 and 5; the end-to-end shadow run | §5.2 Phase F exit | the groups' results; the shadow boundary checked after every command |

Each step closes with its tests, Core's suite, `run_models.py --seeds` (unchanged), the repository suite and `git diff --check` before the next starts. Under the review allocation, each step ends with a same-family review of its delta. Phase F ends with an independent implementation Review (G2 workplan §5.1 item 5), which the stakeholder asks for.

## 4. Acceptance groups: cases and discriminators carried

Expected results come from the register row and the Stage S case's stated outcome, transcribed into the test as literal data with the case name cited. A group not executed is reported as unexecuted, never as passed (Manual §31.2).

| Group | Stage S cases carried | Review-named discriminators carried in Phase F | Deferred, with reason |
|---|---|---|---|
| **4** admission, publication, currentness, loss | S5 §14-§25: `publication_classification`, `deployment_classes_sound`, `loss_bounds`, `qualification_states` (Admission side; the read side is Phase D's) | 362af9f N6, 61cd09b N6 (a kept fence and the D1/D2 re-gating), 441cf5c N7, 730490d N2, 8a75346 N2 | the faults beyond these named failure points (Phase H) |
| **2** admission half | the records of S5 §6's histories admitted at Admission | 798b2b4 B4, 29da56e N5 and 124b0b7 N2 where a record's admission is the distinguishing step | none |
| **3** admission half | S1 objection cases where the distinguishing step is an Admission refusal; the RR-11 resolver and Dispatcher half | 51070e5 N3 (adjudication-independence refusal); f03b15e N5 (supersession authority, the judgment key of §8.3 step 3); 6b986de N6 (one definition of each independence input for every record kind, at Admission) | none |
| **5** admission half | S5 §8: `rejected_request_salvages_never_lost`, `unclean_result_refuses_passing_judgments`, `clean_request_admits_all`; the five S3 kept-fence cases | the refusal of a candidate bound to an obligation no longer derived (§8.3 step 7) | none |
| **1** runner half | the representation discriminators of 3540d98 B1, e2154ac B1, e9e6e9f B1, materialized by a designated runner | — | none |

**Carried from Phases D and E** (Phase D plan §8; Phase E plan §6):
- the cited-premise cycle enforcement (step 4);
- recovery authorization and authenticated witness retirement (steps 6-7);
- designated-runner materialization and custody (step 9);
- `REALIZE`, `ASSESS`, `RERUN` and `READING` (step 9);
- the refusal of answers to non-derived decisions, which closes Phase E §6's "reviving a dropped part" (step 5);
- `report`, `submit` and `decide` (step 10);
- PERF-E1 (step 1).

The other Phase E §6 items stay with their owners: the late objection's review identity, the brief functions listed there, and overlapping partitions.

## 5. Readings

Each reading resolves a point the register leaves to D4. It is revised, never silently changed, when a step or its review falsifies it.

- **F1** *The shadow integration ref.* Document control's integration ref (`main`) is a governed ref, and no SSDS process may move it (G2 workplan §5.1 item 2).
  - **Real shadow ledger.** Admission reads `main` as the live integration head (`obs`) and never publishes to it. Document control's integrations reach the ledger as absorptions (§8.6). Records-only requests (`C_n = B_n`), such as designated-runner observations, human reports and decisions, are admitted with no effect. The Manual does not refuse a request with a product effect on `LEGACY` or `UNGOVERNED` subjects (catalogue §19.2: such changes arrive as ordinary commits and are absorbed; a request touching several modes takes the union of their obligations). In a governed deployment Admission would admit and publish one. On the real shadow ledger, then, no such request reaches Admission: `ssds submit` refuses a request with candidate commits against a ledger whose integration ref is governed. That is a check of the shadow boundary (G2 workplan §5.1 item 2), made by the deployment, recorded nowhere in the ledger, and not an Admission decision or reason code.
  - **Group 4.** Publication, fencing, settlement and the ABA policy are exercised where Admission does publish: fixture ledgers with integration refs in scratch repositories, two Admission incarnations constructed in one test.
- **F2** *Runner workspaces.* A designated runner's workspace is materialized from the content model's tree representation (§1.5) into the SSDS home under the SD-59 boundary, never as a worktree or checkout of the product repository, and holds no push credential. Network access is outside the workspace unless a runner class declares it, in which case it counts as an unpinnable read (§17.5).
- **F3** *Witnesses.* The real shadow ledger keeps its genesis witness model (`LOCAL_TRUST`, one witness on another medium). `TEAM` and `HARDENED` quorums, read repair and redesignation run on fixture witnesses only.
- **F4** *Keys and incarnations.* Admission host keys, issue keys and runner keys live in private operator state in the SSDS home, created by the operator. An Admission process takes a random incarnation identity per start (§22.3) and records it in every entry. No incarnation state is persisted beyond a process, so a copied home authorizes no publication.
- **F5** *Human gates.* A human-gated record is signed with a registered human key in the SSH signature format, namespace `ssds` (§25.1), as the genesis approval was. Tests use fixture keys and never the stakeholder's key.
- **F6** *Reason codes.* The closed list is catalogue §8.4. A needed refusal with no code returns to Stage S (G2 workplan §5.6).
- **F7** *PERF-E1.* The fix keeps prefix semantics: `discharged_at` answers for the state at a position, computed from that prefix once and shared, never from the current state. The selector, settlement and lifecycle discriminators stay unchanged, as the re-Review of c2b1ec2 asks.
- **F8** *No campaign.* The Dispatcher issues envelopes to fixture executors and to the manual and Git-envelope routes, where lineage is `UNKNOWN` unless a human attests it (§12.2). Its harness route is built and tested against a stub harness, never a live model, without a campaign authorization.

## 6. Fail closed until a later owner

Until the stakeholder settles Q-F1, step 11 does not run, and the exit reports the difference study as unexecuted.

Until Phase G, a change of unknown provenance on the real shadow ledger is absorbed and goes no further than its §18 intake obligations, which are derived but not routed beyond `INTAKE`.

Until Phase H, failure points beyond those group 4 names are untested.

Until an authorized campaign, no live agent submits to Admission.

Each fails toward "not supported", never toward support.

## 7. Questions for the stakeholder

**Q-F1. What "computing decisions beside document control" compares.** The Phase F row's exit asks that every material difference from document control be classified and independently reviewed. In shadow, every subject is `LEGACY` or `UNGOVERNED`, so document control's changes reach SSDS as absorptions, which Admission always admits (§8.6). Admission's checks that read SSDS-only records (envelopes, judgments, contracts) have nothing to judge in this repository's history. The options:
- **(a) Recommended. Counterfactual record-independent evaluation.** For each document-control integration since genesis, Admission evaluates the change as if submitted, by the checks that need no SSDS-only record:
  - the secret and credential scans (§24.1);
  - structure on the merged tree (§8.3 step 4: effective-structure delta, quarantine, mode mixing, SDG membership);
  - protected surfaces (§25.3);
  - dependency well-formedness (step 5);
  - evidence regression, where evidence specifications exist (step 8).

  It reports each case where SSDS would refuse or route what document control accepted, and the reverse where document control's records show a refusal. Each difference is classified and reviewed. This is computable from this repository and needs no campaign.
- **(b) Absorption consequences only.** Report what derivation shows after each absorption (quarantine, ill-formed subjects, drift, reopened obligations, integrity findings) without evaluating any check counterfactually. It is cheaper, but it never exercises Admission's checks against real changes.
- **(c) Defer the difference study to a campaign** in which agents submit through SSDS beside document control (G2 workplan §5.1 item 7). This is the only route by which Admission's record-dependent checks meet real work. It needs its own frozen plan, Review and authorization, and it leaves Phase F's exit unexecuted until then.

Steps 1-9 do not depend on the answer; steps 10-11 do.

**Q-F2. The shadow genesis under A9.** Step 10 runs on the real shadow ledger. Phase E's plan proposes a new shadow genesis under A9 (ledger id `ssdp-shadow-2`), which the stakeholder approves by their own signature as at Phase D step 7. The old `ssdp-shadow` stays as history, and Phase E reading E33's interim check is retired then. A dry run of `prepare` in a scratch SSDS home at `1e34abef`, with a throwaway key, validated (`valid: true`, no problems, `ssds.unclassified` declared). Step 10 needs the admitted `ssdp-shadow-2`.

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
