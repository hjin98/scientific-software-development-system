---
kind: ssds-shadow-phase-plan
workplan_id: SSDS-8.0-G2-PHASE-F-PLAN
protocol_version: 7.2.1
target_system_version: 8.0.0
status: active (revision 2, after the same-family plan reviews of 07284144 and 53e8c119)
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
STATUS: ACTIVE, revision 2; questions settled by SD-64. Companion to the G2 shadow workplan, Stage D (§5.2 Phase F row). It
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
             never-lost queue order, a minimal commit path; the fitness revision). Steps 3-8 fail
             closed (SCHEMA_UNSUPPORTED) until built.
DEPENDS:     Q-F1 to Q-F3 settled by SD-64. Step 10 needs the stakeholder-signed genesis of
             `ssdp-shadow-2`; the old ledger's retirement statement needs step 7.
NEXT ACTION: step 3 (envelopes and keys).
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
- intake, the migration path and external units (Phase G);
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
| **3** envelopes and keys | `dispatcher`: issue keys, envelope signing, lineage classes, launch attestations, per-task submission credentials, the operator journal (§12.2, §25.2); `admission`: `KEY_LIFECYCLE` registration, rotation, retirement listing outstanding envelopes, compromise from a position (§25.2); `interface`: `open(task)`, read recording, the brief's digest in the envelope (§16.4) | §12.2, §16.4, §25.1-§25.2 | an envelope under a retired, uncompromised key admits only the never-lost records it lists; a compromised key's later envelopes refused; `UNKNOWN` lineage credits no independence; `AUTH_VERSION` when a record's `governs` differs from its envelope's (Phase E E1) |
| **4** authorization to currency | `admission`: steps 3-6: authorization, including independence and adjudication eligibility (§5.10 (f), RR-11) and supersession authority by the superseded kind; structure on the merged tree; dependency well-formedness with the cited-premise component check; currency with never-lost salvage. Also protected surfaces (§25.3) | §8.3 steps 3-6, §8.5, §25.3 | group 3's admission half: 51070e5 N3 (the adjudication-independence refusal); f03b15e N5 (supersession authority); 6b986de N6 (one definition of each independence input for every record kind, at Admission); S1 objection cases at Admission. Group 2's admission half: 798b2b4 B4, 29da56e N5 and 124b0b7 N2 with the records involved admitted, and never-lost challenges, failing assessments and adjudications admitted whatever the request's fate. `AUTH_PROTECTED` on each protected surface |
| **5** legality and regression | `admission`: step 7 (one result per task, result-only `HARD` templates, SD-26 one integration per enactment, answered obligations, revision assessments first, the judged-content support check replacing `STALE_RETAINED`, claimed discharge with conformance at head on the merged tree) and step 8 (no collateral evidence regression, R15). Also lint enforced when a plan unit is admitted (Phase E E5), and the refusals Phase E deferred: answers to decisions not derived, including a dropped part's, and invalid partitions | §8.3 steps 7-8, §13.3 | group 5's admission half: S5 §8 `rejected_request_salvages_never_lost`, `unclean_result_refuses_passing_judgments`, `clean_request_admits_all`; the refusal of a candidate bound to an obligation no longer derived; `same_key_other_scope_after_issue` and the judged-content cases. The cases that need step 9 run after it: regression that needs §17.4 (a fall from `T` to `P` refused) and claimed discharge with affected evidence rerun on the merged tree. The settled-fence check runs after step 6 |
| **6** commit, publication, fencing | `admission`: step 9; the single-ref compare-and-swap; at most one provisional entry; the checkpoint quorum; absorption (§8.6) and the entry-shape rule (§22.1); the publisher's incarnation, the publication effect, fencing absorption, settlement, the ABA policy and the takeover wait (§0.6, a policy key); crash recovery by request identity (§22.4). `derivation`: publication classification, the expected head, the re-evaluation after `OVERTAKEN` or a fence, and the extended head. `ledger`: witness writing | §8.3 step 9, §8.6, §22, §23.3-§23.4 | group 4 through ledger-only replay with the integration host disconnected and deterministic failpoints: S5 §22 `publication_classification`; S5 §23 `deployment_classes_sound` at genesis and redesignation; 362af9f N6 (re-application of a fenced or `OVERTAKEN` integration); 61cd09b N6 (a kept fence and the D1/D2 re-gating); 441cf5c N7 (a rewind is `ROLLBACK`); 730490d N2 (a foreign return to `B_n` is `LATE_PUBLICATION`); 8a75346 N2 (a crash after the CAS, before the outcome is recorded); the entry-shape barrier; a records-only admission never fenced (reading F1). The five S3 kept-fence cases, with the kept-fence conditions and P7 added to the lifecycle check (Phase E E15). The extended head equals from-scratch derivation over every Phase D and E fixture ledger. Each extension builds a new `History`, never mutating one, so step 1's per-history cache stays sound (it is keyed by position on an immutable `History`). A records-only admission whose observed ref is then rewritten to a commit not descending from `C_n` is `OVERTAKEN`, and `LATE_PUBLICATION` if a later observation reaches it, with expected values from Manual §22.2 (the Stage S model has no fence case) |
| **7** loss and recovery | `admission`: `LEDGER_LOSS`, `FORK_RESOLUTION`, `WITNESS_SET_REDESIGNATION`, `REPLICA_REDESIGNATION` and `LINEAGE_RETIREMENT` with `obs = null` (§22.1); `LINEAGE_MIGRATION`, `REDACTION_NOTICE` and retirement statements (§24.2); `CONTINUITY_ATTESTATION` (§23.7); `derivation`: the loss boundary and `REQUALIFY` obligations | §23.5-§23.8, §24.2 | S5 §23 `loss_bounds` and `qualification_states` at Admission; each §23.8 table row as a fixture history; a stale-consistent restore resurrects nothing; a fresh clone (§23.5); a witness-set redesignation over a provisional entry (§22.4) |
| **8** scheduling and transports | `dispatcher`: issue from derived readiness bound to a named `H*`; serialization surfaces and one coordination task per plan; per-worktree leases (K2); scheduling of the joint-invariant review obligations Derivation already derives (§9.2); judge selection (RR-11, §16.5); suspension and resumption; integration requests and mechanical retry. `interface`: `ask(changed)`; the MCP server and the Git-envelope transport, run only against scratch repositories | §9, §16.5, §16.10, §26.1 | at most one mutating task per serialization surface; lease expiry changes scheduling, never correctness; an overtaken basis revalidated, never silently admitted (§9.1); a judge chosen outside `W`'s authors, its lineage recorded; a Git-envelope round trip in a scratch repository, with no ref written to the product repository |
| **9** runners and evidence | `dispatcher`: a designated runner materializes the exact tree in the content model's representation in a sandboxed workspace (reading F2), records its declared execution attributes and unpinnable reads, enforces the runner class's time bound (the system cap of 168 h), and submits `REALIZATION` observations with canonical outcomes and template parameters (§17.2-§17.3, §17.5; Phase E E6); external custody on fixtures; runner-class designation lint (Phase E E20). `derivation`: §17.4 admissibility and currency, and the realization-triggered obligations | §17 | group 1's runner half: the CRLF, mode, symlink, gitlink, LFS and submodule fixtures materialized by a runner. Group 2: the S5 §6 matching cases with realizations admitted. A fixed-attribute mismatch is inadmissible; an incomplete realization enters no assessment; agent-reported results are never admissible. The sandbox tests of reading F2. Step 5's cases that depend on step 9 rerun |
| **10** shadow operation | on the real shadow ledger, with the observed ref of Q-F2: `admission serve` observe-only (reading F1); `dispatcher serve` issuing nothing and writing no run ref; records-only requests through `submit`, `report` and `decide` | §8.6, §16.1 | after every command: the product repository's refs, reflogs, objects and status unchanged; each observed head absorbed (an absorption records the head, so the commits between become reachable); a restart after a records-only admission appends no fence; a candidate request through the library API, the Dispatcher or a transport refused at Admission's entry, appending nothing |
| **11** difference study | the comparison Q-F1 settles, as a qualification harness calling the real Admission owners outside the ledger (§7) | §5.2 Phase F exit | per Q-F1 |
| **12** exit | assembly of group 4 and the admission halves of groups 2, 3 and 5; the end-to-end shadow run | §5.2 Phase F exit | the groups' results; the shadow boundary checked after every command |

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
    - any record whose checks belong to a later phase, such as `MODE_TRANSITION` (Phase G), so that no records-only route touches modes (G2 workplan §2 item 1).

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
- **F8** *No campaign.* The Dispatcher issues envelopes to fixture executors, and to the manual and Git-envelope routes in scratch repositories, where lineage is `UNKNOWN` unless a human attests it (§12.2). Its harness route is built and tested against a stub harness, never a live model, without a campaign authorization. On the real shadow ledger `dispatcher serve` issues nothing and writes no run ref.

## 6. Fail closed until a later owner

Until the stakeholder settles Q-F1 and Q-F2, steps 10-11 do not run, and the exit reports the difference study as unexecuted.

Until Q-F3, real-runner execution is limited to fixtures that hold no secret.

Until Phase G, a change of unknown provenance on the real shadow ledger is absorbed and goes no further than its §18 intake obligations, which are derived but not routed beyond `INTAKE`.

Until Phase H, failure points beyond those group 4 names are untested, and §24.2's replacement-lineage re-encoding is not built.

Until an authorized campaign, no live agent submits to Admission.

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
