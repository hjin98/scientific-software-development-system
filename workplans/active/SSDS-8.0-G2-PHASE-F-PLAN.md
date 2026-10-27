---
kind: ssds-shadow-phase-plan
workplan_id: SSDS-8.0-G2-PHASE-F-PLAN
protocol_version: 7.2.1
target_system_version: 8.0.0
status: active (revision 41 splits 9c-ii into four parts with readings F88-F95; revision 40 repairs F87 (re-check PASS at abcd03de) after the check of 298a12a0, with Q-F23; revision 39 details 9c-i with reading F87; revision 38 repairs Q-F21 item 8 and F84-F86 after the check of db0bf1ce; revision 37 details 9b with readings F84-F86 and widens Q-F21; revision 36 repairs Q-F20-Q-F22 and splits 9c after the check of 09df7c27; revision 35 splits step 9 into 9a-9f-ii with readings F75-F83 and Q-F19-Q-F22; 8f repaired; 8g-i and 8g-ii built; revision 34 repairs F74 after the re-check of 25bd1d0d; revision 33 repairs F73-F74 after the check of 53216046; revision 32 splits step 8g into 8g-i and 8g-ii with readings F73-F74; revision 31 details step 8d with reading F72; revision 30 splits step 8 into 8a-8g with readings F65-F71 and Q-F17-Q-F18; revision 29 repairs F63-F64 after the check of 66ac030b, with Q-F16; revision 28 details steps 7f and 7g with readings F63-F64; revision 27 bounds F59's held test after the re-check of 3b6ebcc0; revision 26 repairs F59 and F62 after the check of c36b278e and withdraws Q-F15; revision 25 splits step 7e into 7e-i and 7e-ii with readings F59-F62 and Q-F15; revision 24 repairs F56 after the check of 8f10d755; revision 23 details step 7c with readings F54-F57; revision 22 repairs F50's table after the check of 31b3ed34; revision 21 details step 7b with readings F50-F53; revision 20 splits step 7 into 7a-7g with readings F44-F48 and Q-F13; revision 19 splits step 6 into 6a-6g with readings F38-F42 and Q-F11; revision 18 splits step 5 into 5a-5f with readings F29-F34 and Q-F9; revision 17 details step 4e with readings F26-F28 and splits it into 4e-i and 4e-ii; revision 16 details step 4d with readings F22-F25; revision 15 after the check of c50eb56c: an adoption names the current delta, SD-69's targets literal, Q-F8; revision 14 detailed step 4c-iv with reading F21, a delta's identity; revision 13 after the check of ad8daeb6: 4c-iv admits only ABSORB, F1 and §6 amended; revision 12 placed SD-69's schema correction and adoption path as step 4c-iv and the ledger's repair at step 10; revision 11 adds reading F20, the freeze's regions, after the 2aadf33 review; revision 10 reverted revision 9's split and added reading F19, the outermost owner's content; revision 9 split F18's whole-structure checks; revision 8 adds reading F18 and Q-F7, the reserved leaves; revision 7, after the re-check of efa2c450; revision 6, after the same-family plan review of 96e13c0b; revision 5 split step 4c into 4c-i to 4c-iii with readings F14-F17 and Q-F6; revision 4, after the same-family plan review of b10018de; revision 3 split step 4 into 4a-4e with readings F10-F11; revision 2 after the same-family plan reviews of 07284144 and 53e8c119)
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
STATUS: ACTIVE, revision 20 (step 5 in six parts, §3.2; step 6, §3.3; step 7, §3.4); questions Q-F1 to Q-F18 settled (SD-64, SD-67 to SD-78; Q-F15 withdrawn). Companion to the G2 shadow workplan, Stage D (§5.2 Phase F row). It
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
NEXT ACTION: steps 4b-ii, 4c (4c-i to 4c-iv) and 4d are closed (last PASS at 85f7fd7b); revision 17
             details 4e (readings F26-F28); step 4e is closed (last PASS at 2d737acf), and with it step 4.
             Revision 18 splits step 5 into 5a-5f (§3.2, readings F29-F34, Q-F9), checked (PASS at
             43e85277); 5a is closed (PASS at 3d125c63); 5a, 5b (5b-i to 5b-iii) and 5c are closed (last PASS at 1acbb8df);
             5d is closed (PASS at b546a2b8, notes taken up); 5e and 5f
             are deferred (SD-71). Step 5 is closed for Phase F. Revision 19 splits step 6 into 6a-6g (§3.3,
             readings F38-F42, Q-F11), checked (PASS at 112d2a40); 6a and 6b are closed (PASS at c06f5be5 and
             e78d0cf7); 6c (accepting) is closed (PASS at ab0b790d). Admission now accepts records-only
             requests in an allowlist of checked kinds and a records-only ABSORB adoption; 6d (publication,
             F43) is closed (PASS at 0ab46e4b); 6e (integration registration) is closed (PASS at 04012289); 6f is
             deferred (SD-73). Step 6 is closed for Phase F. Revision 20 splits step 7 into 7a-7g (§3.4, readings
             F44-F48, Q-F13), checked (PASS at bd515e60); 7a (retirement, reading F49) is closed (PASS at 749b37d3, N2
             taken up). Revisions 21-22 detail 7b (readings F50-F53; re-check PASS at 43b2e4e5); 7b is closed (PASS at 7d2d1c00). Revisions 23-24 detail 7c (`LEDGER_LOSS`, readings F54-F57; re-check PASS at 5636d551); 7c is closed (PASS at 8bfaaf0f, N2 taken up); 7d (`FORK_RESOLUTION`, reading F58) is closed (PASS at 099556e6). Revisions 25-27 split 7e into 7e-i and 7e-ii (readings F59-F62; re-check PASS at b19707d9); 7e-i is closed (PASS at 9f841460, after B1's repair); 7e-ii is closed (PASS at 00b4c1ac); step 7e is closed. `ssdp-shadow` is retired (SD-74; `qualification/ssds80/PHASE-F-SHADOW-RETIREMENT-EVIDENCE-SSDS-8.0.md`). Revisions 28-29 detail 7f and 7g (readings F63-F64, Q-F16; re-check PASS at 2d01eb22); 7f and 7g are closed (PASS at 80222c23, N1 taken up); step 7 is closed for Phase F. Revision 30 splits step 8 into 8a-8g (readings F65-F71, Q-F17, Q-F18), checked (PASS at 5d4a0e26, notes taken up); 8a is closed (PASS at a889ed5e, N2 and N3 taken up). Q-F17 and Q-F18 are settled (SD-77, SD-78); 8b is closed (PASS at c8b78706); 8c is closed (PASS at 455d4880). Revision 31 details 8d (reading F72), checked (PASS at 8f1c948f, notes taken up in 8d). 8e is closed (PASS at 041c6c98); 8d is closed (PASS at 50954f95); 8f's review (4d949827) found B1, repaired with its notes; the repair awaits its re-check. Revision 32 splits 8g (readings F73-F74); its check (53216046) found B1, repaired by revision 33; the re-check (25bd1d0d) passed F73 and found B1 in F74, repaired by revision 34 (re-check PASS at 70cef9cf, note taken up). 8f's repair is re-checked (PASS at 7be4890d, notes taken up). 8g's review (26907956) found B1-B3, repaired (re-check PASS at 4f5caedb; N1 and N2 follow). 9a is closed (re-check PASS at 5f9c7cce, which also passes 8g's N1 at ce988a56; 8g is closed). 9b is closed (re-check PASS at c9af0774). 9c-i's review (09ab5249) found B1, repaired with its notes; the repair awaits its re-check. 9c-i is closed (re-check PASS at 478901d6). 9c-ii-i and 9c-ii-ii are closed (PASS at cb146b5a and 06a20532, notes taken up in 9c-ii-iii). 9c-ii-iii's review (babcbd22) found B1, repaired with its notes; its re-check (9031b16d) found a residual, repaired again; the second repair awaits its re-check. 9c-ii-iv is built and awaits its review. Revision 35 splits step 9 into 9a-9f-ii (§3.6; readings F75-F83; Q-F19-Q-F22); its check (09df7c27) found B1-B2, repaired by revision 36 (re-check PASS at 7a53ad06, notes taken up in Q-F20 and Q-F21). Step 9's parts may be built; 9b's tolerance oracles wait for Q-F21, and 9f-ii's read-observation flag for Q-F20. A10 is accepted (SD-66);
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
- adversarial, privacy and fault harnesses beyond the failure points group 4 names (Phase H). §24.2's breach protocol stays in Phase F, as the G2 row places §22-§25 there. Its rotation branch's `REDACTION_NOTICE` is built in 7g. Its replacement lineage, re-encoding and private pseudonym mapping, and with them `LINEAGE_MIGRATION`'s equal-state qualification, are handed to Phase H (SD-76);
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
| **4** authorization to currency | `admission`: steps 3-6: authorization, including independence and adjudication eligibility (§5.10 (f), RR-11) and supersession authority by the superseded kind; structure on the merged tree; dependency well-formedness with the cited-premise component check; currency with never-lost salvage. Also protected surfaces (§25.3) | §8.3 steps 3-6, §8.5, §25.3 | group 3's admission half: 51070e5 N3 (the adjudication-independence refusal); f03b15e N5 (supersession authority); 6b986de N6 (one definition of each independence input for every record kind, at Admission); S1 objection cases at Admission. Group 2's admission half (798b2b4 B4, 29da56e N5, 124b0b7 N2) runs at step 9, since it needs realizations admitted (revision 17). Never-lost challenges, failing assessments and adjudications admitted whatever the request's fate. `AUTH_PROTECTED` on each protected surface |
| **5** legality and regression, in six parts (§3.2) | `admission`, and `derivation` for the rebase: once Q-F6 (iii) is settled, step 2's rebase check and §7.6's rebase counting (a frame-`X` record counts for `X'` only where every entry holds there, structural records also needing `Δ_Σ(X') = Δ_Σ(X)`), with `transformation_of` and the enactment learning `X'` from the records carrying it; step 7 (one result per task, result-only `HARD` templates, SD-26 one integration per enactment, answered obligations, revision assessments first, the judged-content support check replacing `STALE_RETAINED`, claimed discharge with conformance at head on the merged tree) and step 8 (no collateral evidence regression, R15). Also lint recomputed on `M_n(X)` when a plan unit is admitted, with non-issuability derived (F29; Phase E E5), and the refusals Phase E deferred: answers to decisions not derived, including a dropped part's, and invalid partitions | §8.3 step 2's rebase clause, steps 7-8, §7.6 rebase, §13.3 | group 5's admission half: S5 §8 `rejected_request_salvages_never_lost`, `unclean_result_refuses_passing_judgments`, `clean_request_admits_all`; the refusal of a candidate bound to an obligation no longer derived; `same_key_other_scope_after_issue` and the judged-content cases. The cases that need step 9 run after it: regression that needs §17.4 (a fall from `T` to `P` refused) and claimed discharge with affected evidence rerun on the merged tree. The settled-fence check runs after step 6 |
| **6** commit, publication, fencing, in parts (§3.3) | `admission`: lifting ACCEPT, except for a request carrying a `TASK_RESULT` or depending on a task result's conformance, which stays `SCHEMA_UNSUPPORTED` until A10's D4 (SD-70); `NOT_SETTLED` for a human decision on a fenced admission, never-lost adverse decisions excepted (F41); step 9, which drops every record naming a transformation whose only fixing result a later step dropped (review 8408e05 B2), registers an integration whenever `integrates` is present, so an empty transformation (`admitted_commit` = head) agrees with its trial (F27; plan check of 0d92c731), and first drops every record whose referenced record a later step dropped (review 2981f738 N1); the single-ref compare-and-swap; at most one provisional entry; the checkpoint quorum; absorption (§8.6) and the entry-shape rule (§22.1); the publisher's incarnation, the publication effect, fencing absorption, settlement, the ABA policy and the takeover wait (§0.6, a policy key); crash recovery by request identity (§22.4). `derivation`: publication classification, the expected head, the re-evaluation after `OVERTAKEN` or a fence, and the extended head. `ledger`: witness writing | §8.3 step 9, §8.6, §22, §23.3-§23.4 | group 4 through ledger-only replay with the integration host disconnected and deterministic failpoints: S5 §22 `publication_classification`; S5 §23 `deployment_classes_sound` at genesis and redesignation; 362af9f N6 (re-application of a fenced or `OVERTAKEN` integration); 61cd09b N6 (a kept fence and the D1/D2 re-gating); 441cf5c N7 (a rewind is `ROLLBACK`); 730490d N2 (a foreign return to `B_n` is `LATE_PUBLICATION`); 8a75346 N2 (a crash after the CAS, before the outcome is recorded); the entry-shape barrier; a records-only admission never fenced (reading F1). The five S3 kept-fence cases, with the kept-fence conditions and P7 added to the lifecycle check (Phase E E15). The extended head equals from-scratch derivation over every Phase D and E fixture ledger. Each extension builds a new `History`, never mutating one, so step 1's per-history cache stays sound (it is keyed by position on an immutable `History`). A records-only admission whose observed ref is then rewritten to a commit not descending from `C_n` is `OVERTAKEN`, and `LATE_PUBLICATION` if a later observation reaches it, with expected values from Manual §22.2 (the Stage S model has no fence case) |
| **7** loss and recovery, in parts (§3.4) | `admission`: `LEDGER_LOSS`, `FORK_RESOLUTION`, `WITNESS_SET_REDESIGNATION`, `REPLICA_REDESIGNATION` and `LINEAGE_RETIREMENT` with `obs = null` (§22.1); `LINEAGE_MIGRATION`, `REDACTION_NOTICE` and retirement statements (§24.2); `CONTINUITY_ATTESTATION` (§23.7); `derivation`: the loss boundary and `REQUALIFY` obligations | §23.5-§23.8, §24.2 | S5 §23 `loss_bounds` and `qualification_states` at Admission; each §23.8 table row as a fixture history; a stale-consistent restore resurrects nothing; a fresh clone (§23.5); a witness-set redesignation over a provisional entry (§22.4) |
| **8** scheduling and transports | `dispatcher`: an envelope's `contract_revision` copied into each record's `binding.item`, and a system contract id settled first: authentication compares the two, but the binding schema admits only an item revision (review ccaca71 N1); issue from derived readiness bound to a named `H*`; serialization surfaces and one coordination task per plan; per-worktree leases (K2); scheduling of the joint-invariant review obligations Derivation already derives (§9.2); judge selection (RR-11, §16.5); suspension and resumption; integration requests and mechanical retry. `interface`: `open(task)` bound to an envelope, read recording (§16.4) and `ask(changed)`; the MCP server and the Git-envelope transport, run only against scratch repositories | §9, §16.5, §16.10, §26.1 | at most one mutating task per serialization surface; lease expiry changes scheduling, never correctness; an overtaken basis revalidated, never silently admitted (§9.1); a judge chosen outside `W`'s authors, its lineage recorded; a Git-envelope round trip in a scratch repository, with no ref written to the product repository |
| **9** runners and evidence | `dispatcher`: a designated runner materializes the exact tree in the content model's representation in a sandboxed workspace (reading F2), records its declared execution attributes and unpinnable reads, enforces the runner class's time bound (the system cap of 168 h), and submits `REALIZATION` observations with canonical outcomes and template parameters (§17.2-§17.3, §17.5; Phase E E6); external custody on fixtures; runner-class designation lint (Phase E E20). `derivation`: §17.4 admissibility and currency, and the realization-triggered obligations | §17 | group 1's runner half: the CRLF, mode, symlink, gitlink, LFS and submodule fixtures materialized by a runner. Group 2: the S5 §6 matching cases with realizations admitted. A fixed-attribute mismatch is inadmissible; an incomplete realization enters no assessment; agent-reported results are never admissible. The sandbox tests of reading F2. Step 5's cases that depend on step 9 rerun |
| **10** shadow operation | the composition root wires `ancestry` over the ledger repository into Admission's and the CLI's derivations, or the step's report states that publication is `UNKNOWN` there; operators are told that a force-push rewinding past a records-only admission and moving forward again raises a `CRITICAL` `LATE_PUBLICATION` (review 0ab46e4 N1, N3); first, `ssdp-shadow-2`'s in-place repair (SD-69 Q-F7): the stakeholder commits the `ssds.manifest` and `ssds.policy` declarations to the observed branch's manifest, the absorption quarantines them, and a human R2 records-only request adopts both by `ABSORB`: one disposition per declaration key of the two units, validated together (4c-iv). It is admissible once 4d, 4e and step 5 exist and step 6's commit path holds on the real ledger, meaning its single-ref compare-and-swap and the `LOCAL_TRUST` witness checkpoint (a records-only admission has no publication and is never fenced, F1). `ssds.policy`'s scope is the policy path genesis names. The absorbed content's authorship is `UNKNOWN` and the same human commits it, so the `ABSORB` is non-independent: §18.4 enacts it at S0 regardless, and §8.3 step 3 classifies dispositions without refusing them. After it, `Σ` declares the three reserved leaves; then, on the real shadow ledger, with the observed ref of Q-F2: `admission serve` observe-only (reading F1); `dispatcher serve` issuing nothing and writing no run ref; records-only requests through `submit`, `report` and `decide` | §8.6, §16.1 | after every command: the product repository's refs, reflogs, objects and status unchanged; each observed head absorbed (an absorption records the head, so the commits between become reachable); a restart after a records-only admission appends no fence; a candidate request through the library API, the Dispatcher or a transport refused at Admission's entry, appending nothing |
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
| **4c-i** the frame at the head, and the two shared owners | `derivation` | the frame of an unintegrated transformation built at the admitted head `n`: `M_n(X) = merge3(tree(B), T_n, tree(C))` and `Σ_n ⊕ Δ_Σ(X)` (§7.2), read by `Conformance` (which builds its frame at its result's position today; §7.5: "evaluated in `D_n[X]`: the conformance of `C`"), `REVIEW(X)` derivation and Admission; the tree and structure facts of an integrated enactment's frame fixed at its integrating admission's head, while its frame records' currency is the admitted state's (reading F17). One **write-set owner** on the frame: `T_n` under `Σ_n` against `M_n(X)` under `Σ_n ⊕ Δ_Σ(X)`, with both sides' governance modes (§1.2). `Conformance.writes`, `changed_files` and `uncovered_outside` read it, as Admission's `AUTH_WRITE_SCOPE` will in 4c-iii; every other conformance template states which tree it reads (§14.1 names "the base and candidate trees"): the write-set templates (`outside_scope`, `owners`, `uncovered_outside`, the protected-surface template) resolve regions, owners and scope on the frame's two sides, `T_n` and `M_n(X)`; the artifact and frozen-interface templates keep `tree(B)` and `tree(C)`. One owner of the bound contract's write scope, the item revision's with a part's share restriction (§13.7), that `Conformance.contract` and `AUTH_WRITE_SCOPE` read, and one owner of containment in it, `derivation.writescope`, at frame level. Both sides are checked. A scope entry naming a unit only one side declares resolves to that unit's files there. The outermost owner is judged file by file: in each file whose unclassified content changes, all its pieces in that file lie within the scope (re-check ad8daeb RB2). This is file-granular, not piece-granular, and fails closed when one span of a file is classified (re-check c550803 N1). A unit with no region on either side lies within only when named, which holds because every declaration change writes the manifest. One **protected-surface owner** (reading F14) that `Plans.protected`, `Conformance`'s `protected_surfaces` template and Admission's `AUTH_PROTECTED` read. `id(X)` computed by one function exactly as §7.1 states, A included (the `‖` concatenation and `A`'s element form fixed in its docstring; every fixture computing `"ssds.transformation.v1|B|C"` rebuilt); derivation does not recognize a submitting result whose `target.transformation` differs from it | a write a concurrent admission since `B` made, outside scope on `T_n` and absent from the base-to-candidate set, is not in the write set, and an effect arising only where `C` meets it is; conformance of one pending result read at two heads; conformance of an integrated result unchanged by later heads, an overlapping later edit included, with its required-evidence assessment read in the admitted state; each protected surface touched by path and by unit; `id(X)` with and without `A` |
| **4c-ii** the structural validation owner (§8.3 step 4 (a)-(c)) | `derivation` | one function of the head state and `X` returning `Σ_{n+1}`, the per-key classification against `Q_n` and the step 4 codes. **Per key:** a key outside `Q_n` takes `decl(M)[k]` (authored); `decl(M)[k] = Σ_n[k]` realigns; `decl(M)[k] = decl(T_n)[k]` carries the quarantine; any other value of a key in `Q_n` routes to revalidation (`STRUCT_REVALIDATE`). Adoption by `ABSORB` fails closed (reading F16). **Well-formedness, together over `Σ_{n+1}` on `M`:** §1.9's static checks, the resolution of newly declared or changed file and span terms (`TreeView.unresolved_declared_terms`, then genesis's one owner too), scope conservation for a refinement, and the reserved leaves of §1.8 declared, each with its reserved kind, `ssds.unclassified` with the empty prefix (A9, SD-61; one owner that genesis, every admission and `Frame.exists` read, replacing genesis's own check; reading F18) (`STRUCT_*`, reading F15); no membership change mixing governance modes (`STRUCT_MODE_MIXED`; a cutover `X` carries fails closed until Phase G); SDG members kept together; a change of an existing unit's kind or owning domain fails closed (reading F16). **Freeze:** a subject whose signature, scope, regions or membership the change touches while its current triple in the admitted state `D_n` (never the frame's merged revision) is `BLOCKED`, `PROVISIONAL` (an overridden blocking challenge) or `REVOKED` (`State.status1`): `FREEZE_SOURCE` where it loses or changes, `FREEZE_DESTINATION` where it gains. **Semantic structure:** S0 defects that an affected subject has in the frame and not at the head (reading F15), under their `RELATION_*` names, with SDG, cycle and single-definer defects as `STRUCT_*` members. **Where a frame exists, `Σ_n ⊕ Δ_Σ(X)` equals this owner's `Σ_{n+1}`.** A key in `Q_n` that `C` authors to the value a foreign change put on `T_n` would be carried by catalogue §8.3 4 (a) but is a proposal in the frame by Manual §7.2 ("in the frame the proposal's declarations are not quarantined"). That case routes to `STRUCT_REVALIDATE`, so no frame exists and the request is rejected. Read alone, Manual §7.2 and §7.6 would enact the key as authored: the refusal is a fail-closed stronger rule pending Stage S, which takes the catalogue's precedence, and the difference study classifies it so (§6). `Frame.exists` is a clean merge with no code from this owner (§7.4: every step 4 check except enactment); §7.4's cutover source-mode condition moves with cutover to Phase G, since derivation folds every `MODE_TRANSITION` at its own admission | one case per code; a quarantined key carried, realigned and changed, and authored to a foreign change's value (no frame); a foreign absorption that makes an affected subject ill-formed neither refuses the request nor ends the pending frame, while a second same-code defect the request adds there is refused; a reserved leaf dropped or narrowed; a frame that no longer exists derives what a conflict derives |
| **4c-iii** content and structural requests in Admission | `admission`, `derivation` facts | the submitting request (§11.5): records declaring frame `X` judged on the trial in `X`'s frame, with step 2's revision check keyed on each record's frame rather than on `candidates`. **Frame identity:** a record whose declared frame or `target.transformation` names no transformation an admitted or co-submitted result fixes is refused (`REF_TRANSFORMATION`); schema 1's `frame` field is only `{transformation}`, so it cannot carry a rebase's `(B', C', A')` and the transformation rebased (catalogue §8.3 step 2): a record declaring a rebase frame is indistinguishable from one naming an unknown transformation and is refused `REF_TRANSFORMATION` (Q-F6 (iii)); a lifecycle-tier record declaring a frame (a cutover `MODE_TRANSITION`) stays `SCHEMA_UNSUPPORTED`. **Prospective tenure:** every subject of `Σ_n ⊕ Δ_Σ(X)` is read at the frame's triple, so an acceptance in `X`'s frame of a subject `X` creates, restores, rescopes or rekinds is judged against the frame (`AUTH_TARGET_NOT_CURRENT`, `AUTH_TARGET_NOT_EFFECTIVE`; catalogue §8.3 step 3, §7.4, §7.5); the trial of an integrating request with `Σ_{n+1}` and a tree source holding `M_n(X)` (moved to 4e, whose currency is its first reader: no 4c-iii check reads the integrated state, since the structural owner and the enactment check read the frame at the head); a `renamed_from` whose source unit had another kind is `SCHEMA_UNSUPPORTED` (F16); step 3's `AUTH_WRITE_SCOPE` (the write set within the bound contract's write scope, and plan units, contracts and verification rules outside every role's scope except as §12.3 assigns them) and `AUTH_PROTECTED` from the 4c-i owners; step 4's codes from the 4c-ii owner; a merge that conflicts (`STRUCT_MERGE_CONFLICT`, a `STRUCT_*` member: no frame, §7.4); the **enactment condition** on an integrating request (`ENACTMENT_MISSING`: every promotion or restoration carries a prospective acceptance that counts for the tenure it starts, read by `Support.binds_tenure`'s conditions 1-4 before admission, so the check does not depend on step 7's `OBLIGATION_REENACTED`; a cutover fails closed until Phase G). `STRUCT_REVALIDATE` rejects the request with its code and derives nothing more until step 5's routing reads it. A request passing steps 1-4 stays `SCHEMA_UNSUPPORTED` (steps 5-8 not built); committing a merged tree that is not `tree(C)` is step 9's | one case per code; an adopting request fails closed; a write outside scope on the merged tree that the base-to-candidate set misses refused `AUTH_WRITE_SCOPE`; an acceptance of a subject the frame creates is not `AUTH_TARGET_NOT_EFFECTIVE`; a frame record naming an unknown transformation refused |
| **4c-iv** intake adoption (SD-69 Q-F6 (i), (iii); §18.3-§18.4) | `ledger` schema 1, `derivation`, `admission` | **The schema-1 correction, in place (SD-69).**<br>- `INTAKE_DISPOSITION` and `INTAKE_CLASSIFICATION` targets become `delta` (`{absorption, key}`) or `content_ref`, with `units` dropped.<br>- The `identity` basis gains the same `delta` type.<br>- The outcomes become §18.3's, and a `QUARANTINE` carries `paths`. Only `ABSORB` of a quarantined delta is admitted in Phase F. Every other §18.3 outcome is `SCHEMA_UNSUPPORTED` until Phase G builds its effects (a `QUARANTINE`'s S2 effect, contrary dispositions and the realignment they derive, §18.4), and the never-lost adverse ones are refused by identity (§3.1).<br>- `frame` gains optional `base`, `candidate`, `adopts` and `rebases`, present together. The rebase they serve is step 5's.<br>Fixtures that build intake records on `units` targets are rebuilt.<br>**The adoption path.**<br>- The `INTAKE` obligation is keyed by the quarantined delta it names.<br>- A transformation's `A` is the set of deltas the request's `ABSORB` dispositions adopt, and §7.1's `id(X)` covers it. Until Stage S fixes the canonical element form (SD-69), each element is `{absorption, key, value}`: the absorption entry's digest, the declaration key and `decl(T)[k]` at that absorption (a function of the ledger alone), sorted by canonical JSON. No ledger holds an `X` with a non-empty `A`, so a later Stage S form changes no admitted fact. That stays true after step 10 only because the repair stores no `id(X)`: a human request carries no `TASK_RESULT`, and intake dispositions declare the admitted frame (§7.5), so the identity is computed only during validation. An implementation that would record `id(X)` in a record or an admission needs Stage S's form before step 10, or the stakeholder's acceptance of re-identification. A records-only adoption is `X = (B, B, A)` and is judged as its own transformation's frame record (catalogue §8.3 step 6).<br>- The 4c-ii owner classifies an adopted key as authored (`Σ_{n+1}[k] := decl(M)[k]`), validated exactly as if authored (§18.4: freezes, mode consistency, SDG integrity). §18.4 also needs "a prospective acceptance bound to the same admission for any promotion". So a records-only adoption that promotes or restores a subject fails closed (`SCHEMA_UNSUPPORTED`) until the enactment condition is built for every admission that changes `Σ`. Step 10's repair adds two new leaves and promotes nothing.<br>- Admission admits an `INTAKE_DISPOSITION` only on an intake object for which an `INTAKE` obligation was derived. An adopting `ABSORB` names its key's current delta at the head (F21; else `REF_DELTA`), and a request's `adopted_deltas` are exactly the deltas its `ABSORB` dispositions name (else `REF_ADOPTION`). Only a records-only adoption (`C = B`) is lifted. Adoption with a candidate, a result with a non-empty `adopts`, and `INTAKE_CLASSIFICATION` stay `SCHEMA_UNSUPPORTED`. The rule that a `QUARANTINE` names only that object's paths is Phase G's, with `QUARANTINE` itself.<br>- Admission refuses an `ABSORB` of a delta on which an adverse disposition stands.<br>- A records-only adoption (`C = B`) changes `Σ` by its `adopted_deltas` alone, recorded `ADOPTED`. It writes no manifest bytes, so the write-scope rule that a region-less unit lies within when named (4c-i) is re-examined here: an adopted declaration change to such a unit needs its own authority (re-check c550803 N5).<br>Mechanical adoption of governance-neutral deltas (`intake.neutral_auto`) stays off and unbuilt: it is the Dispatcher's (step 8). | one case per refusal; an adopted key validated as authored, a freeze at its destination included; a records-only adoption folding into `Σ`; an `ABSORB` refused under a standing adverse disposition (on a fixture ledger, since Phase F's Admission admits no adverse disposition); a non-`ABSORB` outcome refused; a superseded delta's `ABSORB` refused (`REF_DELTA`); `adopted_deltas` mismatching the dispositions refused (`REF_ADOPTION`); a promoting adoption fails closed; `id(X)` with `A` in the interim element form |
| **4d** dependency (§8.3 step 5) | `derivation`, `admission` | **The static support graph** (§5.6, items 1-4 with item 4's cited premises; Phase D NF2), read as F24: `CYCLE_SUPPORT` when a non-trivial component of the request's trial is no subset of a component at the head, so the request creates a cycle or grows one. A cycle absorbed content made is reported (`SUPPORT_CYCLE`) and blocks no request that does not grow it. A request changing structure (an integration, a records-only adoption) is read in its frame `D_n[X]`, where the validity endpoints its changes re-route through `subj` and a successor's disposition edges appear. **Challenge-tier targets:** strictly earlier by ledger position (`DEP_TARGET_ORDER`); of the kinds catalogue §3.4 permits (`DEP_TARGET_KIND`): a `CHALLENGE` of a support-tier record, a triple, an adjudication or a risk override; an `ADJUDICATION` or `RISK_OVERRIDE` of a challenge; a `WITHDRAWAL` of a challenge or report its own actor raised (§3.4, §15.2; another actor's: `AUTH_ACTOR`, a step 3 actor check). A `CHALLENGE` of a `CHALLENGE` is `DEP_COUNTER_CHALLENGE` (F25). A `CONTINUITY_ATTESTATION`, and a `CHALLENGE` of one (which §3.4 permits), stay step 7's (`SCHEMA_UNSUPPORTED`). The `ADJUDICATION` fail-closed clause of 4b-ii gives way to these codes. **`DEP_OWN_SUBJECT`:** a `validity` entry whose unit's subject is one of the record's own subjects (F22). **`DEP_CONSUMER`:** an `EQUIVALENCE` whose `validity` entry names a consumer of its unit (F23). **`CYCLE_WARRANT`:** not emitted (F25). Never-lost records owe these checks too, so salvage never writes a target §5.7 calls corruption | one case per code; the mutual-acceptance configuration refused (`CYCLE_SUPPORT`); a cycle absorbed content created blocks no unrelated request; a request growing it is refused; an adjudication of a co-submitted challenge is `DEP_TARGET_ORDER` |
| **4e** currency (§8.3 step 6), in two parts | `derivation` values, `admission` routing | **4e-i, the structure-changing trial (F27).** A request carrying a candidate or adoptions is judged in the state after it. Its trial entry integrates `X` (or adopts `A`): `admitted_commit` names `M_n(X)` through a trial tree source, `adopted_deltas` carries `Σ_n → Σ_{n+1}`, `AUTHORED` for an integration and `ADOPTED` for an adoption, and `integrates` names `X`. Steps 3 and 5 (authorization, `dependency_codes`, `CYCLE_SUPPORT`) then read `Σ_{n+1}`. Salvage reads the head, where a rejection admits never-lost records. Wherever it is judged, a record declaring an unintegrated `X` has its own subjects and consumers read in `X`'s frame, where it acts. Together these close §6's `Σ_n` exception (reviews 2981f738 N2, cab6179a B1). A request whose frame does not exist keeps the head trial: it is already refused at step 4. **4e-ii, `STALE_BASIS` (F26, F28).** Each basis entry of each checked record (F28) is evaluated on the head's `Support` in the record's frame, never in the trial (F10). That frame is: `D_n` for an `ADMITTED` record of a request that changes nothing; `D_n[X]` for a record declaring an unintegrated `X`, or for any record of a request carrying `X` (the request is a frame record of its own transformation, catalogue §8.3 step 6), with in-frame roles. That governs over each record's declared frame because an integrating request carries no new judgment (§11.5 (3)), and a records-only adoption's dispositions have content entries on units that exist only under `Σ_{n+1}`; and, for a record declaring an integrated `X`, the admitted state with §7.3's admitted-state column, as derivation reads an admitted record of that frame. An entry is satisfied when its value is not `F` (F26). A record with an unsatisfied entry is refused `STALE_BASIS`, a refusal removing it before the trial is rebuilt; never-lost records are exempt and salvaged as before. `STALE_BASIS` joins `REASONS`, and `currency` leaves `UNREALIZED_STEPS` | 4e-i: an integrating request's acceptance of a subject `X` moves is judged against `Σ_{n+1}` (`AUTH_TARGET_NOT_CURRENT` on the head triple; none on the frame's); a `validity` entry on a unit `X` moves into the record's own subject is `DEP_OWN_SUBJECT`; an adoption's trial carries its deltas; a request with no frame keeps the head trial. 4e-ii, each on derivation histories and through the engine where a record can be co-submitted: a stale `content` entry; an entry on a revision an `EQUIVALENCE` at the head covers, satisfied; a `validity` entry on an invalid subject; a `record` entry on a co-submitted record, unsatisfied (F10); a `standing` entry on a revoked assessment; a provisional (`P`) basis satisfied; a before-image entry on a unit a concurrent change moved is stale in `D_n[X]`; never-lost records exempt; a report and a challenge never checked. Group 2's admission half (798b2b4 B4, 29da56e N5, 124b0b7 N2) needs realizations admitted, so it runs at step 9, as §4 places it |

After 4e, a request passing steps 1-6 is still `SCHEMA_UNSUPPORTED` until step 5 builds steps 7-8.

Each step closes with its tests, Core's suite, `run_models.py --seeds` (unchanged), the repository suite and `git diff --check` before the next starts. Under the review allocation, each step that changes behaviour ends with a same-family review of its delta. Phase F ends with an independent implementation Review (G2 workplan §5.1 item 5), which the stakeholder asks for.

### 3.2 Step 5 in six parts (revision 18)

A read-only survey of catalogue §8.3 steps 7-8, Manual §8.3 and the code found that most step 7 facts have a derivation owner, but only for admitted records. It also found that `REASONS` holds none of `STALE_RETAINED`, `OBLIGATION_*`, `CONFORMANCE_*`, `REGRESSION` or `NOT_SETTLED`. Every part below is read on the trial or on the head as 4c-4e read them. **ACCEPT stays gated until step 6** (the final `SCHEMA_UNSUPPORTED` stays): step 6's commit path is what writes `integrates`, `adopted_deltas` and the admitted commit, and drops what a later step dropped. So step 5's checks act today only on refusal codes and salvage, and are tested on derivation histories and through the engine as far as records-only requests reach. Each part is built and reviewed alone.

| Part | Builds | Owner(s) reused | Fails closed until |
|---|---|---|---|
| **5a** codes and decision model | The `REASONS` entries for steps 7-8, with the delegated `OBLIGATION_*` members named (F34). A record-alone refusal class for `CONFORMANCE_RESULT`, beside reject and salvage. A rejected integration's entry names `X` (`integrates`), so `Items.refused` routes a new iteration; the entry-shape rule (§22.1) accepts it, and `History`'s fold never reads a REJECT as an integration. Salvage widened to the never-lost kinds whose own checks now exist (challenges, adverse judgments), with failing assessments still needing step 9's realizations | `blocking`, `salvageable`, `admission_entry`, `Items.refused` | — |
| **5b** per-record legality | The bound obligation exists at the head (F34); one `TASK_RESULT` per task; `OBLIGATION_ANSWERED` in the record's frame, with step 3's authorized supersessions and passing `GATE_DECISION`s exempt; revision assessments first (`OBLIGATION_REVIEW_OPEN`): an assessment already admitted counts for the triple, and the judgment carries a `standing` entry on it; a mid-task report request carries no `TASK_RESULT` and claims nothing (4b-i's role and route checks are re-read for it, and a claim is refused); Phase E's deferred refusals (answers to decisions no longer derived, including a dropped part's; invalid partitions) | `Workflow.obligations`, `Workflow.answer`, `Runs.counting_premise`, `Items._answers`, `plans.partition_violations` | — (a result or claim bound to an already-discharged obligation or a non-current contract revision is refused under its `OBLIGATION_*` member, F31) |
| **5c** result conformance | The result-only `HARD` templates (`slots_filled`, `outcome_consistent`, `citations_support`) on the trial, with a result-only owner (F30); `CONFORMANCE_RESULT` refuses every passing judgment and principal decision in the request, and admits the result, adverse judgments and other never-lost records | `derivation/conformance.py` templates | a citation that needs a realization: step 9 |
| **5d** claims and integration legality | `OBLIGATION_REENACTED` (replacing 4c-iii's placeholder); a claimed discharge undischarged at the head and its predicate holding after the request's own records (on the 4e-i trial); clean conformance of the exact candidate; an integrating request claiming with its current review judgments, derived from the ledger (F32); the judged-content support check (`STALE_RETAINED`, through `Judgments.supports_integration`); 4c-iii's producing-task rule made permanent; lint on a plan unit (F29); the routing of `STRUCT_REVALIDATE` and `STALE_BASIS` refusals | `State.enactment`, `Workflow.discharge`, `Items.predicate`, `Workflow.conformance`, `Judgments.supports_integration`, `PlanFacts.lint` | a predicate with an evidence term, or conformance needing required evidence: step 9. `OVERTAKEN` and fenced re-enactments: step 6 |
| **5e** rebase (Q-F6 (iii), SD-69); **deferred by SD-71** | Step 2's pinned-merge check `tree(C') = merge3(tree(B), tree(B'), tree(C))` and `A' = A`; `X'` and its enactment learned from the records carrying it; §7.6's counting of a frame-`X` record in `D_n[X']` (F33), with `Δ_Σ(X') = Δ_Σ(X)` for structural records; `integration_frame` resolving `C'` | `merge3`, `Frame`, `transformation_of` | `A ≠ ∅` (its element form is Stage S's): `REF_TRANSFORMATION`. Producing `C'` is step 8's machinery |
| **5f** no collateral regression (step 8); **deferred by SD-71** | The affected set (realizations whose execution bases or readings read a unit the request changes), refused as unsupported whenever it is non-empty, and the prerequisite-authority exemption's frame | `Assessments.ev`, `qual`, `Support.prospectively_accepted` | the head-versus-merged comparison and reruns: step 9 |

Deferred with their owners: `NOT_SETTLED` and the fenced or `OVERTAKEN` re-enactment cases (step 6); evidence reruns, a fall from `T` to `P`, and citations against realizations (step 9); A10's step 7 clauses (Q-F9).

### 3.3 Step 6 in parts (revision 19)

A read-only survey of catalogue §8.3 step 9, §8.6 and §21-§23 against the code found:
- `append_entry` already does the single-ref compare-and-swap with fsync;
- `write_checkpoint` and `qualify` exist, but Admission writes one hardcoded file witness, never qualifies before appending, never raises the high-water mark, and returns a decision while its entry is provisional;
- Admission never appends an absorption: it halts when `obs` is not the expected head, and its `expected_head` ignores absorption entries;
- an ACCEPT entry never carries the trial's adopted deltas;
- no publication classification exists.

Step 10 needs only records-only admissions and a records-only `ABSORB` adoption, neither of which has a publication effect (F1). Under SD-70 and SD-71 no integration is accepted in Phase F. So step 6 builds the records-only commit path first. The publication effect's writing side is deferred and disclosed.

| Part | Builds | Owner(s) reused | Fails closed / deferred |
|---|---|---|---|
| **6a** head and absorption | The expected head derived from `History` (absorptions and fences included); an observed-ref and ancestry reader in `content` the composition root supplies; Admission appending an absorption of `obs`, with its commits imported, then revalidating (§8.3 step 9, §8.6). An absorption is an entry: once 6b exists it passes 6b's commit point (qualification, checkpoint, high-water mark), and nothing appends on the real ledger before 6b (plan check of 97d9824 N1) | `History`, `append.import_commits`, `_ABSORPTION_SECTION` | an absorption while the head is a pending admission with an effect: refused (§22.3 governs, F39; integration-only) |
| **6b** commit point | Qualify against the genesis witness model before validating, with no append when `UNQUALIFIED`, `ROLLBACK` or `FORK` (§23.4); the ledger compare-and-swap, a losing writer re-reading and revalidating (§21.3); checkpoints written to `q_a` witnesses as `WitnessModel` designates; the high-water mark raised; at most one provisional entry, and crash recovery by request identity completing checkpoint distribution before a decision is reported (§22.4) | `append_entry`, `write_checkpoint`, `qualify`, `HighWaterStore`, `recorded` | `TEAM` and `HARDENED` witness writing on fixtures only (F3) |
| **6c** accepting | ACCEPT lifted, with SD-70's gate (a request carrying a `TASK_RESULT`, candidates, or a claim reading conformance stays `SCHEMA_UNSUPPORTED`). Also gated: an `EVIDENCE_ASSESSMENT` or runner observation, until step 9; an adoption while any admitted realization reads a unit in its write set (step 8, F42). The committed entry equals the trial entry, adoption deltas included. A records-only adoption's entry never carries `integrates`, so it registers no integration (6e; plan check N2). Step 9's drop cascade runs on ACCEPT (F40), and the request is reported admitted only once held | `trial`, `Frame.entry_deltas`, the salvage cascade | — |
| **6d** publication derivation | `pub(n)` (`PENDING`, `PUBLISHED`, `OVERTAKEN`) and the `LATE_PUBLICATION` finding (§22.2); the entry-shape halt in derivation (§8.6: a violating entry is corrupt); the extended head through checkpoint resume | `History`, `s3` | — |
| **6e** integration registration | `History` registers an integration whenever an ACCEPT carries `integrates` (an adoption's never does, 6c), so an empty transformation agrees with its trial (plan check of 0d92c731); a full fixture regression and the checkpoint round trip | `History._fold`, `_resume` | — |
| **6f** fence and settlement derivation; **deferred by SD-73** | Fence classification, `settled(n)`, the fence-attention obligation, the kept-fence conditions (E15) and `NOT_SETTLED`, on hand-built fixture ledgers carrying fencing absorptions | `items.py`'s fence route | which records are "a human decision on a fenced admission" (F41) |
| **6g** deferred | The publisher's attempted set (the per-start incarnation identity every entry records is already built and stays, F4; plan check N3), the integration-ref compare-and-swap, the merge commit for `C_n`, fence-commit writing, the takeover-wait policy key and the ABA policy in action: integration-only, unreachable under SD-70 and SD-71, disclosed at the exit | — | deferred with 5e and 5f |

The step 6 row's `deployment_classes_sound` "at redesignation" needs step 7's `WITNESS_SET_REDESIGNATION`, so it runs at step 7. Group 4's discriminators are placed as follows (plan check N4):
- 441cf5c N7 (a rewind is `ROLLBACK`) and 8a75346 N2 in its ledger compare-and-swap form (a crash before the checkpoint): 6b;
- 730490d N2 in its records-only form (`OVERTAKEN` → `LATE_PUBLICATION`) and S5 §22 `publication_classification`: 6d;
- 362af9f N6, 61cd09b N6, 730490d N2's fence form and the five S3 kept-fence cases: 6f, on hand-built fixture ledgers replayed ledger-only;
- 8a75346 N2's publication compare-and-swap form (a crash after it): 6g's deferral, reported unexecuted at the exit.

### 3.4 Step 7 in parts (revision 20)

A read-only survey of catalogue §22.1, §23-§24 and §25.2 against the code found:
- `admit_lifecycle` admits only `KEY_LIFECYCLE`, with `obs` equal to the expected head;
- recovery entries carry `obs = null` and must be appendable in the states they repair (a `FORK_RESOLUTION` under `FORK`), which 6b's `held_head` refuses;
- Admission's qualification never reads a retirement, so it would keep appending to a retired ledger;
- a retirement statement has no format, signer or verifier: `FileWitness.retired` only tests whether a file exists;
- the witness model in force is read from genesis only.

Step 10 and SD-64 need `ssdp-shadow`'s retirement first, so step 7 builds it first.

| Part | Builds | Fails closed / deferred |
|---|---|---|
| **7a** retirement | A per-kind recovery gate. `LINEAGE_RETIREMENT` is admitted through a generalized lifecycle path, with `obs = null` (§22.1), only when the ledger is `QUALIFIED` with no provisional entry ("settle the old head", §24.2), and only after a trial qualification shows the entry would be held. The authenticated retirement statement (F45): its format, writer and verifier, published to the witnesses. Admission, the CLI and the interface read it (`RETIRED`), and Admission appends nothing to a retired ledger. The old ledger's high-water mark is retired. An operator script prepares and admits it, and the stakeholder signs. The bare-marker expectation is revised | a successor carrying no `LINEAGE_MIGRATION` binding (F44, Q-F13) |
| **7b** recovery skeleton | The per-kind gate generalized (§23.4, §23.8): `LEDGER_LOSS` under `ROLLBACK`, `FORK` or `UNQUALIFIED`; `FORK_RESOLUTION` under `FORK`; a redesignation over a provisional entry. A trial qualification before every recovery append. The witness model in force per position. Injectable fixture witnesses for `TEAM` and `HARDENED` (F3) | — |
| **7c** `LEDGER_LOSS` | `retained` is the replica head. The abandoned set names every witnessed checkpoint beyond it, or conflicting with it, plus the high-water mark's head, each status recomputed from the witnesses' reports. The `report` object is stored. `controls` equal the retained controls: any change fails closed until a control fold exists (F46). Tests: the §23.8 rows, a stale-consistent restore resurrecting nothing, `REQUALIFY`, a fresh clone | a change of controls |
| **7d** `FORK_RESOLUTION` | Only abandoned heads proved never admitted; any other abandonment is a `LEDGER_LOSS` (§24.1) | choosing the side the replica does not hold, and restoring a recoverable suffix, which need a ref restore no owner may write (F47): operator-only, disclosed |
| **7e** `WITNESS_SET_REDESIGNATION` | `continues_from` is the intact head. The new set is `quorum_sound` and class-sound (`deployment_classes_sound` at redesignation, from step 6). Dual quorums are checked where the old set is reachable. A redesignation over a provisional entry is exempt from the critical flag | — |
| **7f** `CONTINUITY_ATTESTATION` | Its target, listed records, evidence and authentication; challenges of it | the policy designation of its actor, which no policy key expresses: still `SCHEMA_UNSUPPORTED` (F48) |
| **7g** the rest | `REPLICA_REDESIGNATION`, `LINEAGE_MIGRATION` and `REDACTION_NOTICE`: field checks on fixtures | the equal-state qualification, which is Phase H's re-encoding, and a redaction's halt: disclosed |

§23.8's rows are placed as follows (plan check note 3):
- **Built earlier.**
  - Crash after append: 6b's recovery.
  - Stale product restore: 6a's absorption.
  - Witnesses below read quorum: 6b's halt.
- **7c, `LEDGER_LOSS`.**
  - Ledger truncated with newer product: 7c's loss; the next entry's absorption is 6a's.
  - Ledger and product restored to one stale snapshot.
  - Ledger objects lost.
- **7d, `FORK_RESOLUTION`.** Only proved-never-admitted entries lost; a fork or conflicting witnesses.
- **7e.** Witnesses lost beyond the fault bound.
- **Partly built.**
  - Authoritative replica lost: 7g's field checks; the restore is F47's deferral.
  - Ledger ref rewound with a recoverable suffix: F47's deferral; Admission halts at `ROLLBACK` (6b).
- **Owned elsewhere.**
  - Abandoned entries later surfacing: never merged, an integrity finding; derivation's existing abandonment reading, with a 7c test.
  - Lost local store: 6b re-establishes the high-water mark by qualification.
  - Corrupted derived state: re-derivation, which is derivation's default.
  - Content objects unavailable: the `UNAVAILABLE` binding health of Phase D's content model.

#### 7b in detail (revision 21)

7b builds the recovery path's machinery and admits no new kind by itself: each of `LEDGER_LOSS`, `FORK_RESOLUTION` and `WITNESS_SET_REDESIGNATION` stays `EntryInvalid` until its own part (7c-7e) supplies its content check.
- **The gate** (F50). `admit_lifecycle` routes a recovery-tier kind through one gate: `obs = null`; the human gate's approval over the ledger, the next position after the replica's last readable entry, that entry's digest and the record identity (§25.2); and the qualification states its kind may be admitted in, from a single table. Nothing is admitted under `INTEGRITY_HALT` or `RETIRED`.
- **The trial** (F51) runs before every recovery append. It replaces 7a's writable-witness stand-in, and the retirement goes through it.
- **Fixture witnesses** (F53) let tests run `TEAM` and `HARDENED` quorums.
- **The witness model per position moves to 7e** (F52).
- **Tests.**
  - the gate table, kind by state, including `INTEGRITY_HALT`, `RETIRED` and an unsupported kind;
  - the trial refusing a record that would leave the ledger unqualified (a retirement under too few writable witnesses), and passing one that holds;
  - the trial run under `TEAM` (3, 2, 2, 0) and `HARDENED` (4, 3, 3, 1) fixture witnesses, with one witness unreachable and with `f` denying;
  - the gate table's cases from the check of 31b3ed34: `FORK_RESOLUTION` under `ROLLBACK`, a redesignation at a settled head, and every kind refused under `INTEGRITY_HALT` (each kind of 7c-7e passes the gate and is then refused by its unbuilt content check);
  - an approval for another position or head digest refused, including one replayed from an earlier position;
  - the compare-and-swap refused when the ref is not at `A`;
  - the composition root never passing the fixture map;
  - 7a's tests unchanged.

#### 7c in detail (revision 23)

Derivation already folds a loss's boundary, `cont`, and `REQUALIFY` (Phase D), and qualification already reads a loss's abandoned digests. 7c is therefore Admission's content check for a `LEDGER_LOSS` and the means to prepare one.
- **`Admission.prepare_loss()`** computes the record's fields from what this host reads (F54-F56): the retained head, the abandoned heads with their statuses, the report object and its digest, and the controls in force. The operator, or a test, puts these fields in the record the human signs.
- **At admission**, the gate (F50) and the trial (F51) run as in 7b. The content check recomputes every field and requires the record's fields to equal it exactly (F57). The report object is stored in the entry by its digest.
- **Tests.**
  - §23.8's three loss rows on fixture ledgers: a truncated ledger with a newer product, the next entry absorbing it (6a); ledger and product restored to one stale snapshot; and ledger objects lost while the witness checkpoints are intact.
  - A stale-consistent restore resurrecting nothing: a permissive record before the boundary is not current after it, and a `REQUALIFY` is derived.
  - A fresh clone with no high-water mark qualifying at the loss.
  - An abandoned chain surfacing later: never merged, the boundary stays, and its integrity obligation is asserted.
  - A loss under `FORK` whose abandoned side holds an admitted entry, and one under `UNQUALIFIED` with evidence of a later head not proved never admitted (§23.8's witness-loss row).
  - A mixed set, one head proved never admitted and one possibly admitted, admitted with both named.
  - A mark's own head is never proved never admitted within the fault model (note 2).
  - §23.8's "authoritative replica lost, none extends the checkpoint" row: with nothing readable there is no `A` to append after. Its restore is F47's, and Admission refuses with no readable genesis. It is disclosed, not tested as a loss.
  - Refusals:
    - each field not equal to its recomputation (a missing or extra abandoned head, a wrong status, a stale report, changed controls);
    - every abandoned head proved never admitted;
    - nothing abandoned;
    - the compare-and-swap refused when the ref is past the readable prefix (plan check of 31b3ed34, note 1; review 7d2d1c0 N2).

#### 7e in two parts (revision 25)

| Part | Builds | Fails closed / deferred |
|---|---|---|
| **7e-i** the witness model per position | The segments of F59. `qualify_segments`, in the Ledger Store's `qualification` API, is the one function Admission, the CLI and the Interface call. Distribution writes a checkpoint to the witnesses of every segment its position lies in, and the retirement statement's quorum is the last segment's. Tests: fixture chains carrying a redesignation entry, built directly, which qualify across segments; a redesignation not yet held by the new set reads as the old segment's provisional entry; truncation to `p` while the new set holds later checkpoints reads `ROLLBACK` (B1); an unreachable new set reads `UNQUALIFIED`; under `HARDENED`, truncation to `p` with one new witness denying still reads `ROLLBACK`, and one partial copy reads the redesignation provisional (R1); an old-set fork after a held redesignation is not read; `RETIRED` under the last segment; distribution writing `p`'s checkpoint to both sets; a fresh clone across segments; the readers agree | nothing admits a redesignation until 7e-ii; F59's fresh-clone residual, beyond the fault model, disclosed |
| **7e-ii** admitting a redesignation | The content check (F60), the dual trial, the redesignation over a provisional entry, including another host's (F61; review 7d2d1c0 N1), and the critical-flag exemption. Tests: a routine redesignation from `LOCAL_TRUST` to `TEAM` fixture witnesses; a redesignation under `UNQUALIFIED` continuing from the intact head, its report referenced; one over a provisional entry; class and quorum soundness; `continues_from`; evidence of a later head refused, naming the loss; a loss re-establishing the witness set admitted under the dual trial, starting a segment (F62); the readers agreeing over another host's provisional entry | — |

#### 7f and 7g in detail (revision 28)

Both are small, and both fail closed where F48 and SD-75 say.
- **7f** (F63).
  - Tests: each of the attestation's codes, asserted beside `SCHEMA_UNSUPPORTED` and not instead of it, on the trial over a fixture loss; a well-formed attestation refused only `SCHEMA_UNSUPPORTED`; a challenge of an attestation, whose target exists only on the trial's derivation facts, permitted.
  - Fails closed: the attestation itself (F48).
- **7g** (F64).
  - Tests: each kind's field problems; a well-formed `REDACTION_NOTICE` admitted with no derived effect; a well-formed replica redesignation refused at the gate; a well-formed migration refused naming Q-F16.
  - Fails closed: `REPLICA_REDESIGNATION` (SD-75); `LINEAGE_MIGRATION` (Q-F16).

Discriminators: S5 §23 `loss_bounds` and `qualification_states` at Admission; each §23.8 row as a fixture history; a stale-consistent restore; a fresh clone; a redesignation over a provisional entry; `deployment_classes_sound` at redesignation; §31.4's retired lineage and stale mirror reading `RETIRED`; and §4's "recovery authorization and authenticated witness retirement".

### 3.5 Step 8 in parts (revision 30)

A read-only survey of the Dispatcher, the Interface and catalogue §9, §16.4-§16.5, §16.10 and §26.1 found:
- of the row's thirteen items, six are partly built (mostly their derivation half) and seven have no code;
- the Dispatcher has only its issuer, journal and home;
- the Interface has no task binding and no transport;
- fourteen plan lines defer work into step 8 (lines 115, 159, 163, 181, 318, 329-330, 386, 817, 966, 973, 986, 994, 1242, 1253 and 1505 at revision 29).

Step 10 needs 8a, and 8f's transports for its refusal of "a candidate request through the library API, the Dispatcher or a transport" at Admission's entry. Nothing is issued on the shadow ledger (F8). (Plan check of 5d4a0e2, note 4.)

| Part | Builds | Fails closed / deferred |
|---|---|---|
| **8a** the Dispatcher at a named `H*` | F65. The ledger's currentness composed through the Ledger Store's one owner, never from a provisional or unqualified head. The would-issue set from derived readiness at `H*`. `dispatcher serve`, with an observe-only mode that issues nothing and writes no run ref (F8). The journal's write-ahead order, intent before effect before outcome, with `Issuer.issue` journaled. Submission to Admission through the journal, and resubmission by identity. Tests: no dispatch from a provisional or unqualified head; the would-issue set equal to readiness; a crash between intent and effect recovered from the journal; observe-only writes nothing | live issuing on the real ledger (F8) |
| **8b** contract binding | F66, after Q-F17. An item task's envelope carries its item revision, and each bound record's `binding.item` copies it. A system task carries the system contract id Q-F17 settles. Admission compares the two (built). One brief-digest formula, shared by the Issuer and the renderer | until Q-F17: system-contract tasks are not issued |
| **8c** scheduling constraints | F67. Serialization surfaces as a policy key, with at most one mutating task per surface. One coordination task per plan. Per-worktree leases (K2), keyed by the Level 0 worktree identity under `state/<ledger id>/`. Scheduling of the joint-invariant reviews derivation derives (§9.2). Suspension and resumption. Tests: one mutating task per surface; lease expiry changes scheduling, never correctness; a suspended task resumed by identity | the joint-invariant reviews' issue, a system-contract task, until Q-F17 |
| **8d** judge selection | F68. The Dispatcher chooses among `eligible_judges`, outside `W`'s authors, in a launch context distinct from the authoring task's. The judge's lineage class, model family, route and toolchain are recorded in the bound record's provenance (`ENVELOPE_FIELDS` is closed). A brief tells a human judging content of unknown authorship that an attestation is required (line 966). Tests: a judge chosen outside `W`'s authors, its lineage recorded | live models (F8): a stub harness only |
| **8e** the task-bound interface | F69. `open(task)` finds the envelope and checks the rendered brief against its digest. Answers are given at the task's basis. Read recording into the task's basis (§16.4), with "reads not observed" on the manual and Git-envelope routes. `ask(changed)` defaulting to the task's basis and units | — |
| **8f** transports | F70. The Git-envelope transport (`interface.envelope`, fitness B1's reserved exception) writes run refs in scratch repositories only, refusing the product repository at run time. The MCP server is JSON-RPC 2.0 over stdio, using the standard library, so no new runtime dependency arises. Tests: a Git-envelope round trip with the product repository's refs unchanged; the MCP operations equal the CLI's | — |
| **8g** retry and resubmission, in two parts (revision 32): **8g-i** retry, integration requests and §9.1 (F73); **8g-ii** the re-issue's resubmission (F74) | F71. Mechanical retry within budget. Integration requests built (the candidate plus references, F32) up to SD-70's `SCHEMA_UNSUPPORTED`. `REISSUE` resubmission (lifting `reissue_of`'s refusal, with F71's reading of N5). The Dispatcher's half of §9.1, where an overtaken basis is re-derived and re-requested. Test: an overtaken basis revalidated, never silently admitted | accepting integration requests (SD-70); `intake.neutral_auto` until Q-F18; a reviewer's re-issue until Q-F17 |

### 3.6 Step 9 in parts (revision 35)

A read-only survey of catalogue §6.5-§6.9, §10.2, §17 and §25, the Manual's §17 and §25, and the code found:
- **Derivation.** It has Phase D's §6 machinery (`Assessments`: `ext`, `stale`, `ev`, `qual`, `execution_current`), with three stubs its docstring names: `admissible` compares only the obligation token (no §17.4); `yields` reads only embedded verdicts (no discriminating-reading coverage); `stale` has no custody-enumeration condition and nothing reads `AVAILABILITY`. `REALIZE`, `ASSESS`, `RERUN` and `READING` are not derived.
- **Admission.** It accepts no evidence kind (`_ACCEPTED` omits `REALIZATION`, `CHECK_EXECUTION`, `EVIDENCE_ASSESSMENT`, `COMPLETENESS`, `IMMATERIALITY`, `AVAILABILITY` and `CUSTODY_ENUMERATION`), has no machinery binding, refuses runner keys on the lifecycle path (B6), and treats any `machinery:` actor as never-lost with no key behind it. `READING_CONTRADICTION` is missing from `REASONS` (catalogue §8.4).
- **Content and the Dispatcher.** Content has no parser for the specification declaration. The Dispatcher has no runner, workspace or `runs/` containment. Policy has no runner-class designations.
- **Reachability.** Under SD-70 most work earlier steps deferred "to step 9" stays unreachable at Admission: realizations of candidates and merged trees, `CHECK_EXECUTION`, conformance's required evidence, 5c's citations through a `TASK_RESULT`, and claimed discharge rerun on the merged tree. Under SD-71, 5f's comparison and a fall from `T` to `P` stay deferred too. What step 9 can close at Admission is evidence over admitted trees: group 2's admission half (S5 §6's cases, 798b2b4 B4, 29da56e N5, 124b0b7 N2), 5d's evidence-term predicate on an admitted claim, and 4b-ii's discriminating readings.

| Part | Builds | Fails closed / deferred |
|---|---|---|
| **9a** runner identity and designation | F76, F77. Runner keys as trust roots (genesis `runner_keys`; `KEY_LIFECYCLE` role `RUNNER` in `lifecycle` and `trust`), closing B6 for runner keys. A machinery binding in `authenticate`: a runner key in force signs the request, its records' actor is `machinery:<component>@<key id>` of class `MACHINERY`, and it may carry only runner observations. An external custody runner is designated with its custody identity (§17.5): that key is a `RUNNER` trust root, and the same binding authenticates its observations and its `CUSTODY_ENUMERATION` (plan check of 09df7c27, note 1). `never_lost` for a runner observation only under that authentication. A policy key designating runner classes (class, key ids, declared execution attributes, read-observation flag), with the designation lint of Phase E E20. Tests: B6 closed for runner keys; a machinery actor with no key refused; an agent-reported realization refused; a retired or compromised runner key refused | live runner keys on the real ledger (F8; SD-64 Q-F2 (ii)) |
| **9b** specification declaration and outcomes (revision 37) | F83-F86. A closed parser for the specification declaration in `content` (F84), with its static checks (§17.1). The evaluated outcome stored in §17.3's shape, `{output name: canonical value}`, with Phase D's derivation and fixtures moved to it (F85). `EXACT` evaluated by derivation (F86). Tests: each key and its refusals; one declaration per specification unit; each canonical form; `EXACT` against stored outcomes, and a reference not canonical under `rounded:<n>`; an embedded verdict read through the declaration; each parameter constraint (a negative tolerance, a non-integer `n`, `lo > hi`, `MONOTONE` naming fewer than two, an undeclared or a non-numeric output); `fixed` linted against the class's attributes; a defective specification deriving no `REALIZE` and admitting no assessment; an undesignated runner class and a Dispatcher class's bound above 168 h found by lint | `ABS_TOL`, `REL_TOL`, `ULP_TOL`, `RANGE` and `MONOTONE` until Q-F21, and `SET_EQUAL` until a collection form is decided (F86; unevaluated: `yields` fails closed) |
| **9c-i** the evidence obligation's identity | F75. The obligation derived from the `EVIDENCES` relation, policy naming only the claim kinds that need evidence; Phase D and E fixtures migrated, their expected values re-derived from the Stage S cases and the authority, never from the new implementation's output (§4; plan check of 09df7c27, answer 2). Reviewed alone | — |
| **9c-ii** §17.4 and the evidence obligations, in four parts (revision 41) | **9c-ii-i** the realization reader, admissibility and the fixtures' migration (F88-F90). **9c-ii-ii** currency and binding health (F91-F92). **9c-ii-iii** completing `stale`: `link⁻`'s range, custody, the "either" clause and renames (F93-F94). **9c-ii-iv** `REALIZE`, `ASSESS`, `RERUN` and `READING`, and the floor (F95). 9c-ii-ii and 9c-ii-iii depend on 9c-ii-i only; 9c-ii-iv on all three. Tests per part as F88-F95 name them; expected values from `cases_s5_6.py` and §6, §10.2, §17, never from the new output | who records `AVAILABILITY` (Q-F22); evidence in a frame (SD-70); the non-`EXACT` templates (Q-F21) |
| **9d** Admission of evidence | F78. `REALIZATION` under a machinery binding, `EVIDENCE_ASSESSMENT` (`ORDINARY`), `COMPLETENESS` and `IMMATERIALITY` accepted; failing assessments and runner observations salvaged; Admission verifying `on⁻(o, tree(o))` and the closed inner shape of `execution`. Tests: group 2's admission half with fixture runner keys; 5d's evidence-term predicate at Admission | evidence on candidates and merged trees, `CHECK_EXECUTION` (SD-70, Q-F19) |
| **9e** discriminating readings | F80. Coverage in `yields`; the R2/R3 class rule; `READING_CONTRADICTION` added to `REASONS`; the inner shape of `observations`; authorize's `DISCRIMINATING` refusal lifted. Tests: 4b-ii's moved items | — |
| **9f-i** materialization | F2. `dispatcher.runner` materializes an exact tree, supplied by the composition root, under `runs/` with its containment check. Tests: group 1's runner half (CRLF, the executable bit, a symbolic link, a gitlink, an LFS pointer, a submodule), byte-exact against the `Tree` | — |
| **9f-ii** sandboxed execution and submission | F2, F79, Q-F20. Execution under `bwrap` (SD-64 Q-F3): a scrubbed environment and its own `HOME`, no agent socket or credential, no network, the operator trees unreadable. The time bound under an injected clock, with `INCOMPLETE` reasons. The execution basis built by `derivation`. Submission signed by the runner key, through the journal. At most one outstanding execution per configuration, required execution attributes and frame (§6.9), a Dispatcher scheduling rule (plan check of 09df7c27, note 2). External custody and `CUSTODY_ENUMERATION` on fixtures. Tests: one per F2 property; a reached time bound giving `INCOMPLETE`; a process's exit never deciding admissibility; a second outstanding execution of one configuration held | real-runner execution on the real ledger (F8); the class's read-observation flag until Q-F20 (declared false meanwhile) |

Order: 9a, 9b, 9c-i, 9c-ii, 9d, 9e, 9f-i, 9f-ii. 9d's group 2 cases need 9a-9c first. Admitting evidence before §17.4 exists would need re-review, so vertical slices were weighed and rejected. 9f-i depends on nothing and may be built earlier.

## 4. Acceptance groups: cases and discriminators carried

Expected results come from the register row and the Stage S case's stated outcome, transcribed into the test as literal data with the case name cited. A group not executed is reported as unexecuted, never as passed (Manual §31.2).

| Group | Stage S cases carried | Review-named discriminators carried in Phase F | Deferred, with reason |
|---|---|---|---|
| **4** admission, publication, currentness, loss | S5 §14-§25: `publication_classification`, `deployment_classes_sound`, `loss_bounds`, `qualification_states` (Admission side; the read side is Phase D's) | 362af9f N6, 61cd09b N6, 441cf5c N7, 730490d N2, 8a75346 N2 (step 6) | faults beyond these named failure points (Phase H) |
| **2** admission half | the records of S5 §6's histories admitted at Admission | 798b2b4 B4, 29da56e N5, 124b0b7 N2 (step 9, which admits the realizations they need; revision 17) | none |
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
    - any record whose checks belong to a later phase, such as `MODE_TRANSITION` (Phase G), so that no records-only route touches modes (G2 workplan §2 item 1). The one exception is SD-69's: a records-only request (`C = B`, no publication) whose only structural effect is adopting quarantined declaration keys by `ABSORB` (step 10's repair, 4c-iv). It moves no governed ref and writes no governed file, and the units it declares, being created after genesis, take the derivation default `UNGOVERNED` (§19.1; `State.mode`), so the shadow boundary holds (G2 workplan §5.1 item 2).

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
- **F20** *The freeze's regions (step 4c-ii; review 2aadf33 B6).* §8.3 step 4 (b) freezes "the signature, scope, regions or membership" of a subject whose current revision carries an unresolved blocking challenge or is `REVOKED`. Its regions are read as the two structures resolve them on one tree: the subject is compared on the merged tree under `Σ_n` and under `Σ_{n+1}` (its declarations, its terms' resolution status, its region, and the bytes it and its members own), so only a declaration can move them (re-check ad8daeb RB1). Bytes, the files under a prefix, and anchor lines are content: an edit of them makes a new revision, which is how a challenge's resolution proceeds, and the freeze concerns structure ("whether it would lose or gain units"). So a file added under a frozen prefix-scoped subject, or an anchor moved within it, is not frozen, being the same on both sides. A rescoping, a change of kind, mode or declarations, a term coming to resolve or not, any unit joining or leaving (nested subjects included), a unit declared to overlap it, an `ignore` entry over its files, and a stranger nested in it taking its bytes are all frozen. So is a re-partition inside it: moving bytes between its own parts changes what its members own, though a byte-preserving refinement keeps its `scope_id` and tenure (§19.3). This fails closed. This is narrower than §1.2's region difference, which the write set uses across two trees: there, existing bytes entering or leaving under the pinned alignment also count, so an anchor move or a file moved out of a prefix would freeze. Under either reading the freeze lets content move between subjects, so this is no decision change. The narrower reading goes to Stage S as a candidate clarification of "regions" in §8.3 step 4 (b).
- **F21** *A quarantined delta's identity (step 4c-iv).* Catalogue §4 gives an `INTAKE_DISPOSITION` "`identity` on the absorption entry and delta key", and SD-69 its `delta` target `{absorption, key}`.
  - **Which absorption.** A delta is the observed value of one declaration key that differs from `Σ` (§1.6). Its `absorption` is the digest of the absorption entry whose observed head first showed that value: the latest absorption at or before `n` at which `decl(T)[k]` became its current value. Before it, the value differed or the key matched `Σ`. A later foreign change to the same key's value is a new delta under a new absorption, and so is the same value returning after an observed manifest that did not parse: an unparsed manifest ends a run as a different value does, for a present value and a deletion alike (review 193b654 N1). A realignment ends the delta (the key leaves `Q`). So a delta's identity is a function of the ledger alone, and the `INTAKE` obligation derived for a quarantined key is keyed by it.
  - **Element value.** The value in `A`'s interim element `{absorption, key, value}` is `decl(T)[k]` at that absorption, so it also names exactly one delta (revision 13).
  - **Targets, as SD-69 enumerates them.** Both intake kinds take `delta` (`{absorption, key}`) or `content_ref`, with `units` dropped. The `identity` basis gains `delta`. Outcomes: the §18.3 vocabulary for dispositions; classification keeps its advisory `PROPOSED`. Catalogue §3.4 gives `INTAKE_CLASSIFICATION` "observed path set or quarantined delta", which has no `content_ref`; whether it takes a `paths` target instead is Q-F8. `INTAKE_CLASSIFICATION` stays unadmitted in Phase F (`SCHEMA_UNSUPPORTED`, intake beyond SD-69's adoption being Phase G's), so the shape is moot until then.
  - **An adoption names the current delta.** §18.4's "at some position" rule concerns the targets of dispositions that judge (contrary dispositions, adjudications), never adoption. An adopting `ABSORB` must name its key's current delta at the head: the key in `Q_n`, with F21's identity at `n`. Otherwise a superseded delta's `ABSORB` would enact a later value no disposition judged (check c50eb56c B1).
- **F22** *A record's own subject (step 4d).* Catalogue §4.1: "A record never holds a `validity` entry on its own subject", with the subject of a record's target. §8.5: "a judgment about part `u` never holds `validity` on `subj(u)`". A record's own subjects are the subjects of the units it judges: `subj(u)` for each unit of `Judgments.judged_units` (a triple's subject, an equivalence's unit, a completeness's scope, a work judgment's `Δ(X)` and retained units, an assessment's claim). A transformation's review may hold `validity` on `gov` of a changed unit "across subjects" (catalogue §4.3): subjects outside that set. The §4.3 minimum checker and `DEP_OWN_SUBJECT` read the one set, so the minimum never requires what the dependency check refuses.
- **F23** *A consumer of a unit (step 4d).* Neither text defines it. Catalogue §2.1 reads reverse relation traversal as impact analysis, and the Stage C workplan's equivalence row says its `validity` entries "must not depend back on a consumer of that unit". A consumer of `u` is a unit `v` from which §2.4's relation set `E` reaches `u` (every authored relation but `CHALLENGES`, and derived relations whose cycle class is not `NEUTRAL`), or a unit of `v`'s subject. `DEP_CONSUMER` refuses an `EQUIVALENCE` whose `validity` entry names a consumer of its unit, or a unit whose subject is one. This is conservative. It refuses the equivalence where, with that subject's acceptance relying on `u`, the static graph would anyway close a cycle and refuse the acceptance for as long as the equivalence existed. Stage S may define it more narrowly.
- **F24** *The support graph Admission keeps acyclic (step 4d).* Catalogue §5.6's static graph has edges "all fixed by admitted records and S0 facts". `Support`'s evaluation graph is narrower: item 2 takes only the current, qualified acceptances in tenure, and item 3 only passing equivalences. A cycle through a non-current acceptance would therefore pass unseen there, and later close when that acceptance became current. Admission reads the static graph: item 1, every basis entry; item 2, every acceptance, gate decision, assessment and disposition record naming the subject, whatever its value; item 3, every equivalence judgment on the unit; item 4, the bounding completeness judgments and their cited premises. An acceptance from an ended tenure is left out: it can never count again (§1.6, §19.4: "An old acceptance cannot become current again because structure changed"), and keeping it would refuse a legitimate reversal of dependency forever. Only an ended tenure's acceptances leave it: a prospective acceptance bound to the current tenure, and one made in a still-pending frame (which can become current when its integration admits), stay in. As built (review 2981f738), item 2's required-kind judgments, assessments and dispositions enter as the evaluation graph has them: on the current triple, passing, and bound to a derived obligation. The edges this leaves out can go live only through an integration, which is read in `D_n[X]`; through an absorption, which is reported; or through a later request, which is then refused. So the gap fails closed. Its only cost is that the later request is blamed for a cycle an earlier record prepared. Stage S may widen item 2's code to every such record. It is an over-approximation of the evaluation graph, built by the same owner (`Support`) from the same node set. The two graphs are named apart: S2's forcing and `s3`'s `SUPPORT_CYCLE` findings read the evaluation graph (sound for the least fixed point), while Admission's acyclicity reads the static graph.
- **F25** *Counter-challenges and warrant cycles (step 4d).*
  - **Counter-challenges.** Catalogue §5.3 defines a counter-challenge as a `CHALLENGE` of a restrictive adjudication, never of a challenge, and §3.4 lets a `CHALLENGE` target an adjudication of either kind. So `DEP_COUNTER_CHALLENGE` refuses exactly a `CHALLENGE` whose target is a `CHALLENGE`; a challenge of any adjudication is permitted.
  - **`CYCLE_WARRANT`.** §2.4's relation set `E` is unit-level relations only. Its illegal cycles are 4c-ii's `STRUCT_ILLEGAL_CYCLE`, the only way a request adds to `E`. Catalogue §5.6 says the mutual-acceptance configuration is rejected on "two independent grounds (support cycle; illegal warrant cycle)", but no text lifts a record's basis into `E`, and the G2 workplan's own case lists only the support cycle. So 4d emits no `CYCLE_WARRANT`. The warrant ground is realized at unit level, as `STRUCT_ILLEGAL_CYCLE` when a request authors or adopts the relations (4c-ii) and as `AUTH_ILL_FORMED` on an acceptance of a subject an absorbed cycle made ill-formed (4b-i). Only the record-level lifting the catalogue implies is open, for Stage S.
  - **Salvage and `CYCLE_SUPPORT`** (review 2981f738 N5). `CYCLE_SUPPORT` is request-level. Catalogue §8.3 step 6 salvages a refused request's never-lost records on their own schema, reference and step-3 checks (4d adds the per-record step-5 codes), so a salvaged record can close a static cycle: a failing assessment about `S` with `validity` on `T`, while `T`'s acceptance relies on `S`. The cycle is then an S3 finding, which §5.6 says arises "only from corrupted input". That tension is for Stage S.
- **F26** *What "satisfied" means at step 6 (step 4e).* Catalogue §8.3 step 6 requires every basis entry "satisfied, in its role, in that record's frame at the current admitted head". The one owner of an entry's value is `Support.sat`, which returns `T`, `P` or `F` from the head's values. Satisfied reads as "not `F`": a provisional value (`P`) propagates by minimum to what relies on it (Stage S `provisional_propagates_by_min`) rather than being forced to `F`, so a record whose basis is provisional is itself provisional, not stale. Manual §5.5 governs: values lie in "`F < P < T`", and "A record is **current** when its base and every basis entry are satisfied in the state", so step 6's stale record is the one whose value is `F`. Manual §10.5 confirms that descendants "whose support passes through a `P` value are `P` (min-propagation)". A node absent at the head (a co-submitted record, an unadmitted subject) has value `F` (F10). `sat` takes the frame explicitly, since the record is no node at the head; its `role_sat` and before-image rules are otherwise unchanged. A record declaring an unintegrated `X` reads `X` as the trial gives it, since a co-submitted result may fix it, and builds `D_n[X]` at the head. When that frame does not exist, a record with basis entries is stale, since nothing in it is satisfied. A record with an empty basis has nothing to satisfy.
- **F27** *The structure-changing trial (step 4e-i).* Steps 3 and 5 read records' own facts "in the state after the integration" (the 4e row), and §1.2 and §7.4 give that state: `Σ_{n+1}` is the frame's structure (R4) and the tree is `M_n(X)`. The trial entry carries what §8.3 step 9's commit would carry: `integrates: X`, `adopted_deltas` with every changed key of `Σ_n → Σ_{n+1}` (`AUTHORED`; `ADOPTED` for a records-only adoption's keys), and an `admitted_commit` naming the merged tree. That tree is no commit, so a trial tree source maps a reserved trial name to `M_n(X)` and every other name to the product trees. Facts keyed on the published commit's identity (the expected head, absorption of `obs`) are not read at steps 3-6 (F10). The frame-level `CYCLE_SUPPORT` of `integration_codes` and `adoption_codes` stays: it judges the change before the request's records, and the trial judges both together.
  - **Salvage reads the head.** A rejected request is no transformation: its entry admits never-lost records at the head (catalogue §8.3 step 6). So a structure-changing request's never-lost records are judged twice. In the frame they are judged for acceptance; at the head, by their own step-3 and step-5 checks, for salvage.
  - **A frame record of the request's own `X`.** In the trial `X` is integrated, so `_in_frame` builds its frame at `n+1`, not at `k - 1` (F17). The two agree: merging `C` onto `M_n(X)` gives `M_n(X)`, and `Σ` is unchanged (review cab6179a N1). `entry_deltas` labels an integration's keys `AUTHORED`, which holds while an adoption with a candidate is `SCHEMA_UNSUPPORTED` (N2).
- **F28** *Which records step 6 checks (step 4e-ii).* Catalogue §8.3 step 6 checks "every submitted support-tier record other than a report", and exempts never-lost records. So the checked records are those whose kind is in `SUPPORT_TIER`, is not a report kind, and which `never_lost` does not classify. Challenge-tier, lifecycle-tier and observation records are not checked; a report's or challenge's basis is provenance (§8.3 step 6).
- **F29** *Lint is not a refusal (step 5d).* The Phase E plan's E5 says "Admission enforces them at plan-unit admission in Phase F", and its next sentence says what that means: a plan failing lint has its changed items non-issuable. Catalogue §11.3 governs: "A plan that fails is admitted as content … its changed items are not issuable", and §8.4 names no lint code. So lint is recomputed on `M_n(X)` and non-issuability stays derived; no request is refused for lint.
- **F30** *`outcome_consistent` at admission is result-only (step 5c).* Catalogue §8.3 step 7 evaluates at admission the `HARD` templates "that read only the result and its contract". §14.3 defines `outcome_consistent` as "`COMPLETE` with an unmet obligation". Evidence obligations are met only after a designated runner runs (§11.5 (1)), so at admission "unmet" counts only what the result and its contract decide: owed slots, declared outputs and the result's own claims, not required evidence. Otherwise every `COMPLETE` result with required evidence would be a `DISCREPANCY` at admission. The full template, required evidence included, still runs in derived conformance, which step 7's claimed discharge reads. A human's unbound `TASK_RESULT` names no contract, so its `slots_filled` is `INCOMPLETE`, and the passing judgments beside it are refused `CONFORMANCE_RESULT`. Whether the result-only templates apply to a human's result at all is a Stage S note. Failing closed matches the rule that a human-produced candidate's integration is `AUTH_WRITE_SCOPE` (review 1acbb8d N1).
- **F31** *A claim on a discharged obligation or a non-current contract (step 5b).* Catalogue §8.3 step 7: such a result or claim "is recorded with that classification and routed to revalidation". Step 6 uses the same phrase for a stale record: "classified stale and routed to revalidation, not admitted". Read in parallel, step 7's is a refusal of that record under a code: a delegated `OBLIGATION_*` member (F34), as step 6's is `STALE_BASIS`. Never-lost records stay exempt (plan check of c88c3bbb). Naming the member is a Stage S note.
- **F32** *"References to those admitted records" (step 5d).* §11.5 (3)'s integrating request is "the candidate plus references to those admitted records", and step 8 accepts a request that "carries or references" a prospective acceptance. The request schema has no reference field. The references are read from the ledger: the current review judgments of `X`, and the current prospective acceptances in `X`'s frame, are those derivation finds there. A request-schema field would be a D3 change, and nothing needs one.
- **F33** *A rebased record's roles (step 5e).* §7.6: a frame-`X` record "counts for `X'` only where every entry holds there". "There" is `D_n[X']`, so each entry's §7.3 role is computed from `X'` (`B'`, `C'`), the frame it is evaluated in. Catalogue §7.6's "in its role, in `D_n[X']`" could also mean the role from `X`. Traced over before-image, output, context and both-sides entries, the two readings agree (plan check of c88c3bbb).
- **F34** *"Exists at the current head" and the delegated codes (step 5).* The bound obligation "exists at the current head" when the head derives it: a dropped part's obligation does not, matching §13.7's "rejected at step 7", since `Items.parts` holds only required parts. §8.4 delegates the `OBLIGATION_*` members. 5a names one per step 7 check (an obligation not derived at the head, a second result for one task, a duplicate discharge, an unmet discharge predicate, plus `OBLIGATION_REENACTED`, `OBLIGATION_ANSWERED` and `OBLIGATION_REVIEW_OPEN`, which the catalogue names), as Stage S notes like SD-68.
- **F35** *Which rejection refuses an integration (step 5a).* `Items.refused` ends a pending candidate on any REJECT naming `X`, and the item takes a new iteration (RR-7). A rejection for a binding fault, an unbuilt check (`SCHEMA_UNSUPPORTED`), a base or a moved head says nothing of the candidate. Naming `X` there would end sound work, and would let a request bound by anyone condemn another task's candidate. So a REJECT names `X` only when the request authenticated and every reason judges the candidate itself: `STRUCT_*`, `RELATION_*`, `CONFORMANCE_FAILED`, `AUTH_WRITE_SCOPE`, `AUTH_PROTECTED`, `CYCLE_*`, `STALE_RETAINED`, `OBLIGATION_REENACTED` or `REGRESSION` (`checks.on_merits`). `CONFORMANCE_INCOMPLETE` (unrealized evidence) and `OBLIGATION_PREDICATE_UNMET` (no current review yet) wait (step 5d). Any other rejection leaves the candidate pending. A freeze (`FREEZE_*`) is the head's state and lifts when its challenge is resolved. A missing enactment acceptance (`ENACTMENT_MISSING`) is the review route's, recorded in `X`'s frame (§11.5 (2)). Neither is the candidate's (review 87b4fa8 B1).
- **F36** *A contract revision that is not current (step 5b).* A result names the item revision whose contract it worked under (`binding.item`, §13.7), which authentication requires to be the envelope's `contract_revision` (§12.2; review fed5d82 B3). Catalogue §8.3 step 7 refuses a result bound to "a non-current contract revision". §13.4 lets some amendments keep a contract's meaning, but whether a result survives one is the revalidation's to judge, not Admission's. So "current" reads as the item's revision at the head: any other revision, or an item no longer declared, is `OBLIGATION_CONTRACT_STALE`. This fails closed. Admitting a result whose contract only tightened is a Stage S note.
- **F37** *"Routed to revalidation" (step 5d).* Catalogue §8.3 step 6's stale record, step 4's `STRUCT_REVALIDATE` and F31's classifications are "routed to revalidation". A refused record is recorded by identity and reason, and never enters `S0`. The obligation it would have answered stays derived and open, so derivation routes it again. A judgment the head holds that is no longer current is already `REVALIDATE`'s (§10.2). No routing beyond the recorded refusal is built.
- **F38** *`HEAD_MOVED` (step 6).* §8.4 lists it, but no text says when it is emitted. Step 9 does not reject a request whose observed head moved: it absorbs `obs` and revalidates. So Phase F emits no `HEAD_MOVED`, as with `CYCLE_WARRANT` (F25), and when it applies is a Stage S note.
- **F39** *An absorption over a pending effect (step 6a).* Step 9 says "otherwise first appends an absorption of `obs`". When the observed head is the base of a pending admission with a publication effect, §22.3 instead requires the publisher's compare-and-swap, or a takeover wait and a fence. §22.3 governs. Such a pending entry needs an accepted integration, which SD-70 and SD-71 keep closed, so 6a refuses that case rather than absorbing.
- **F40** *The drop cascade (step 6c).* Plan review 2981f738 N1 placed at step 9's commit the dropping of every record whose referenced record, or whose transformation's only fixing result, a later step dropped. A dropped record is refused `REF_RECORD` or `REF_TRANSFORMATION`, as salvage's cascade does. It is an ordinary refusal, so it rejects the request (`blocking`). Admitting the rest would let a request land without the records its own records cite.
- **F41** *A human decision on a fenced admission (step 6f).* Step 7 admits one only once that admission is settled (`NOT_SETTLED`), but no record grammar says which records are such decisions. §22.3 ties the rule to the fence's human attention: the re-apply or keep, accept or revert decision. So it is a human record of a decision kind (a support-tier judgment, a `GATE_DECISION`, a principal or coordination decision, or a human lifecycle decision) that names the fenced admission's records or its integration, or answers its fence attention. Challenge-tier records and reports are not decisions (plan check of 97d9824 B1).

  Step 7 also says "Never-lost records are admitted whatever the state of their task". So a never-lost adverse decision is admitted, not refused `NOT_SETTLED`: losing an adverse record is the unsafe direction. This revises the step 6 row's earlier "salvaged adverse ones included" (review 87b4fa8 N1). The tension between the two sentences is a Stage S note.
- **F42** *Step 8 and an adoption (step 6c).* SD-71 deferred 5f because step 8 was taken to judge only integrating requests. But catalogue §8.3 step 8 says "This step concerns the request's content and structural changes", and a records-only adoption changes `Σ`. Until 5f is built, an adoption is `SCHEMA_UNSUPPORTED` while any admitted realization's execution basis or reading reads a unit the adoption changes. Those are the units in its effect-keyed write set: 4c-i's owner, applied to `X = (B, B, A)` with `Σ_n` against `Σ_{n+1}` on `T_n`. They include a unit whose bytes leave it for a newly declared unit, not only the units it re-declares (plan check of 97d9824 B2). That never holds for `ssdp-shadow-2`, which has no realizations, so step 10's repair proceeds. The correction to SD-71's premise is put to the stakeholder (Q-F11).
- **F43** *Publication and the commit graph (step 6d).* §22.2 classifies by reachability ("`C_n` or an equivalent publication is reachable from `obs`"), so derivation needs a commit-graph reader. `History` takes an optional `ancestry`, which the composition root supplies over the ledger repository; that repository keeps every observed commit reachable (§8.6). Without it, a publication that is not `obs` itself is `UNKNOWN`, and the entry-shape rule reads `obs` against `E` strictly, since no equivalence can be shown. Reachability of `C_n` stands for reachability of an equivalent publication. A deeper equivalent publication, below an `obs` that neither is nor reaches `C_n`, is not searched, so such an admission reads `OVERTAKEN`: the conservative class, which re-evaluates it and can raise `LATE_PUBLICATION`. "Derivation treats a violating entry as corrupt" (§8.6) is an `ENTRY_SHAPE` integrity finding with `CRITICAL` attention, like `LATE_PUBLICATION`. Truncating derivation at a corrupt entry is a ledger-level halt, which this reading leaves to Stage S.
- **F44** *A retirement whose successor is no migration (step 7a; Q-F13).* §24.2 defines retirement inside a replacement lineage, whose new genesis carries a `LINEAGE_MIGRATION` and is qualified to derive the same state up to renaming. `ssdp-shadow-2` is no such lineage: SD-61 replaced the shadow by a new genesis with another baseline and structure. Read SD-61 and SD-64 as warranting a non-breach retirement. Its `LINEAGE_RETIREMENT` names its successor (`ledger_id` and genesis digest) for discovery only: no binding, no claim of equal state, and nothing carried over. The old ledger's records stay readable as history and are imported nowhere. This is a candidate for the Manual clarification batch, and the stakeholder confirms it (Q-F13).
- **F45** *The retirement statement and its signers (step 7a).* §24.2: "Publish an authenticated retirement statement to the old witnesses, held by `q_a` of them". The human approves once: the `LINEAGE_RETIREMENT` record, through §25.2's lifecycle gate, signed over the ledger, position, previous entry and record identity. The statement `{ledger_id, kind: RETIREMENT, last_position, last_entry_digest, successor_ledger_id, successor_genesis_digest}` is then signed by the ledger's Admission host key, like a checkpoint. It names that retirement entry as the last, whose human approval the chain carries. A verifier accepts it only when the host key is in the trust roots, its last entry is the chain's `LINEAGE_RETIREMENT` (where the chain is present), and `q_a` witnesses hold it. A participant holding no chain, a mirror that must still read `RETIRED`, takes the trust roots from the genesis it pins: the genesis digest and admission keys in its operator state, as qualification's high-water mark is (plan check note 4). A bare marker file is no retirement.
- **F46** *`LEDGER_LOSS`'s `controls` (step 7c).* §24.1 lets a loss re-establish the witness model, trust roots and ruleset, but derivation folds controls only from genesis, `KEY_LIFECYCLE` and `RULESET_ADOPTION`. Until a control fold exists, a loss's `controls` must equal the controls in force at the retained head, and any change fails closed. The one exception, from 7e-ii, is the witness member (F62). Schema 1 leaves the inner shapes of the recovery fields open, so Admission checks closed shapes for the fields it reads; the schema is unchanged.
- **F47** *Ref restores (step 7d).* Choosing the side of a fork the replica does not hold, or restoring a recoverable suffix, rewrites the ledger ref, which the append-only compare-and-swap cannot do, and fitness B1 confines Git writes to `ledger.append`. The Manual assigns "replica restore" to the Ledger Store (component table), so this defers a `ledger` function, not only an operator convenience. It is deferred to Phase H, with §24.2's re-encoding. When built, it needs a named extension of fitness B1's single Git-writing exception (plan check of bd515e6, note 2). In Phase F a restore is an operator action outside SSDS, disclosed, and Admission qualifies whatever the replica holds.
- **F48** *A continuity attestation's designation (step 7f).* §5.2 and §12.5 have a continuity attestation recorded by "a designated human" (R3), but no policy key designates one, and `Support.qualified` reads only the human floor. It stays `SCHEMA_UNSUPPORTED` until a designation exists. On `ssdp-shadow-2` it would follow only a `LEDGER_LOSS`, which F46 makes rare.
- **F49** *The retired ledger's high-water mark (step 7a).* §24.2's "retire participants' high-water marks for it" sits in the confidentiality path, beside the purge of the old ledger, which needs G5's operation-specific authorization. Read "retired" as frozen, not deleted. A mark rises only when its holder qualifies a head `QUALIFIED`, which `RETIRED` excludes, so after the statement is held no participant raises it again. It stays at the retirement entry, so a replica that later loses the statement and is rewound still reads `ROLLBACK`. Deleting it belongs to that purge.
- **F50** *The recovery gate (step 7b; revision 22 after the check of 31b3ed34).* §23.8 admits recovery records in the states they repair, which 6b's held head refuses. One table states each kind's admissible qualification states:
  - `LINEAGE_RETIREMENT`: `QUALIFIED`, settled (7a).
  - `LEDGER_LOSS`: `ROLLBACK`, `FORK` or `UNQUALIFIED` (7c).
  - `FORK_RESOLUTION`: `FORK` or `ROLLBACK` (7d; B1). An entry that reached fewer than `q_a` witnesses before the replica lost it leaves a witnessed checkpoint beyond the replica head, which reads `ROLLBACK`. §23.6 and §23.8 resolve it by a `FORK_RESOLUTION` with no boundary when it is proved never admitted, which 7d's content check requires of every abandoned head.
  - `WITNESS_SET_REDESIGNATION`: `QUALIFIED`, settled or with one provisional entry, or `UNQUALIFIED` (7e; B3). The routine change of a witness set (§23.8's witness lifecycle) is made at a settled head; §22.4's provisional entry is the exception.

  `REPLICA_REDESIGNATION` stays refused until 7g. Under `RETIRED` every kind is refused, `LEDGER_LOSS` included: §23.6 says "recovery continues in the successor lineage".

  Under `INTEGRITY_HALT`, §5.7 admits a `FORK_RESOLUTION` or `LEDGER_LOSS` abandoning the chain from the faulty position `k`, appended after `k - 1` (B2). The ref then points beyond `k - 1`, so that append moves the ref off its current value: F47's ref restore, a `ledger` function deferred to Phase H. §5.7's route is deferred with it, the gate refuses every kind under `INTEGRITY_HALT` until then, and §6 discloses it.

  A recovery entry through the settled held head (a retirement, or a redesignation at a settled head) is appended after it. Every other recovery entry is appended after the replica's last readable entry `A`; for a loss, that is §23.6's `R + 1`, since 7c's retained head is the replica head. The approval names that position and `A`'s digest, and the entry carries `obs = null` (§22.1). The append is the ledger's compare-and-swap from `A`'s commit. When the ref is not at `A`, the compare-and-swap is refused and Admission halts (note 1): an unreadable suffix, or a corrupt one, would need the ref moved, which is F47's restore again. A held head is otherwise never required, and the high-water mark is raised only by the commit's re-qualification.
- **F51** *The trial qualification (step 7b).* Before any recovery append, Admission builds the entry and signs it. Ed25519 is deterministic, so the digest is the one the append will produce. Admission then qualifies the extended chain: the reachable witnesses' reports, plus the entry's checkpoint at each witness this host can write, under the retained high-water mark. The append proceeds only when that trial is `QUALIFIED` at the new position with no provisional entry. So a recovery record is admitted only if it actually repairs what it claims: its abandonment explains every mark, and a quorum can hold it. The trial is not proof that the writes will succeed. A write that fails leaves a provisional entry, which 6b's recovery completes, and the commit's own re-qualification decides what is reported. For a retirement, the trial is the extended chain still `QUALIFIED`; its statement is published after the commit (7a). A redesignation's trial qualifies under the new set and the old one where reachable, which needs the model per position (F52), so it is 7e's: 7b builds no genesis-only trial for that kind.
- **F52** *The witness model in force per position (moved to 7e).* Only a `WITNESS_SET_REDESIGNATION` changes the model (F46 holds a loss's `controls` to the retained ones), and none can be admitted before 7e. Until then every chain's model in force is its genesis model. The fold, and its dual-quorum admission under old and new sets, are therefore 7e's. 7b keeps qualification on the genesis model, and every reader keeps calling the one owner, `Admission.witness_set` (the Interface reads genesis too), so 7e changes one place per reader.
- **F53** *Fixture witnesses (step 7b; F3).* `TEAM` and `HARDENED` forbid `FILE` witnesses (`WitnessModel.validate`), and this host reaches no `GIT` or `LOG` witness. For tests only, Admission takes an optional map from declared witness id to a fixture witness: a directory, read and written as a file witness, or a file-witness object, so that a test can give a witness that holds a checkpoint and denies it (`f` denying, note 4). The composition root never passes it, and a test guards that, so the real ledger's witnesses are exactly its `FILE` ones (F3).
- **F54** *A loss's retained and abandoned heads (step 7c).* `retained` is `{position, digest}` of the replica's last readable entry `A`: the retained authenticated chain from genesis (§23.6), which F50 appends after. `abandoned` is computed from the witness reports Admission reads and its own high-water mark:
  - every distinct `(position, digest)` of an authentic checkpoint, from a declared witness, that lies beyond `A` or differs from the chain at its position;
  - the mark, when it lies beyond `A` or conflicts with the chain.

  Each head carries `{position, digest, status}`. Its status is `loss_status(h, m, f, q_a)` (§23.6), where `h` counts the responding witnesses holding it and `m` the witnesses not responding.

  The record must name exactly this set, ordered by position and digest. A head known only from another replica cannot be verified here; Phase F has one replica per ledger and one mark per home (F3). Exact equality is Phase F's single-home form (check of 8f10d755, note 1). With several replicas or homes, the record would name a superset of the recomputed set, whose extra heads arrive with authentic evidence.

  A loss is refused in two cases:
  - **Every abandoned head proved never admitted.** That is a `FORK_RESOLUTION` with no boundary (§23.6), which is 7d's.
  - **Nothing abandoned.** An intact head that has lost its witnesses is §23.8's redesignation (7e).
- **F55** *The report (step 7c).* `report` is the content reference of "the qualification report gathering those reports" (§23.6). It is the canonical JSON of:
  - `ledger_id`;
  - the replica head;
  - the retained high-water mark, or null;
  - each declared witness's report: its authentic checkpoints for the ledger, sorted, or null when it does not respond.

  Admission recomputes it at admission, requires the record's digest to match, and stores the object in the entry by its digest. A witness that changes between preparing and admitting changes the report, so the record is refused and is prepared again.
- **F56** *The controls (step 7c; F46 made concrete).* `controls` is `{witnesses, trust_roots, ruleset}` in force at `A`:
  - `witnesses`: the witness model in force, genesis's until 7e (F52);
  - `trust_roots`: the complete trust-root set in force at `A`, in genesis's shape (revision 24, after the check of 8f10d755, B1). That shape covers Manual §25.2's list:
    - every key genesis declares (`admission_keys`, `dispatcher_keys`, `human_keys`, and any further list, such as runner keys);
    - `human_mechanism`.

    The dispatcher, runner and human keys are those in force under the trust-root fold at `A`, each a list of `{id, public_key}` sorted by id. Runner keys change through `KEY_LIFECYCLE` since step 9a, so `runner_keys` follows the fold; it is present when genesis declares it or a lifecycle record has named a runner key, so a ledger that never had one keeps genesis's shape (review of 47612014, B1). Every other member keeps its genesis value, because no admissible lifecycle path changes it yet: host keys are not rotated through `KEY_LIFECYCLE`, and `TRUST_MECHANISM_CHANGE` is not admitted. When a path changes one, the fold is extended there and this form follows it;
  - `ruleset`: the ruleset in force at `A`, read from `History`.

  It must equal the recomputation, so any change fails closed until a control fold exists (F46).
- **F57** *After a loss (step 7c).* Qualification reads the named heads as abandoned through its existing `_abandoned`, once the loss is inside a quorum-held prefix. The trial (F51) therefore shows that the loss explains every mark. Derivation's boundary at the loss's position withholds permissive records and relaxers before it unless they are held, derives `REQUALIFY`, and never revives a record from agreement between product and ledger (§23.6, Phase D). The next ordinary entry absorbs a newer product (6a). An abandoned chain that surfaces later is never merged; the boundary stays.
- **F58** *A fork resolution's abandoned heads (step 7d).* A `FORK_RESOLUTION` carries exactly `{abandoned}`. It is checked against the loss evidence:
  - It must name exactly F54's set: every head off the replica's chain or beyond it that the witnesses or the mark show, each with its recomputed status.
  - Every head must be proved never admitted (§23.6). That gives it no boundary, and derivation folds none, since it folds boundaries only at a `LEDGER_LOSS`.
  - A head possibly or known admitted is abandoned only by a loss.
  - A mark's head is floored at possibly admitted (review 8bfaaf0 N2), so a resolution never abandons it.
  - Nothing to abandon is refused.

  The replica keeps its own side. Choosing the side it does not hold, or restoring a recoverable suffix, needs the ref restore, F47's (Q-F14). This reading follows directly from §3.4's 7d row and F54, so it was not given a separate plan check; 7d's code review judges it.
- **F59** *The witness model in force per position (7e-i).* Genesis's model is in force from position 0. A `WITNESS_SET_REDESIGNATION` at position `p` in the readable chain starts a segment, whose model is its `witnesses` from `p`. Its own entry belongs to both segments: it is admitted under both quorums where the old one is reachable (§23.8).

  Qualification evaluates `qualify` under each segment's model, using that segment's declared witnesses' reports, newest segment first. Revision 26 fixes the order after the check of c36b278e (B1).
  - **Held.** Whether the newer segment may hold its start is decided before any verdict is read, by §23.6's non-admission bound (revision 27, after the re-check of 3b6ebcc0, R1). Let `h` count its witnesses that report an authentic checkpoint at `p` or later, and `m` those that do not respond. Its holding from `p` is *proved never admitted* when `h + m + f < q_a`.
  - **Its verdict governs.** In every other case the segment's verdict is the answer: `FORK`, `ROLLBACK` and `RETIRED` included, and `UNQUALIFIED` when too few respond. So a replica truncated back to `p`, while the new set holds later checkpoints, reads `ROLLBACK`, even with `f` witnesses denying. An unreachable new set never lets an old set present a stale head.
  - **Otherwise.** The holding is proved never admitted: the new set holds nothing from `p`, or under `HARDENED` one partial copy. The redesignation is then the older segment's provisional entry, and the older segment is read. Its result counts when its head lies inside its range: from its start, up to but excluding the next start. A result at or past the next start is read as the redesignation provisional.
  - **Old witnesses.** They are not read once a redesignation is held: the old set was consistent when the redesignation was admitted under it.
  - **Disclosed residual, beyond the fault model.** A fresh clone with no high-water mark, shown a replica rolled back to before `p` by old witnesses returning stale, never learns the new set, because segments come from the readable chain.

  A segment also starts at an admitted `LEDGER_LOSS` whose `controls.witnesses` re-establishes a different model (F62).
  `RETIRED` uses the last segment's model. This is the one change F52 placed in 7e. The Interface's own genesis read moves to the same function, so every reader goes through one owner.
- **F60** *A redesignation's content (7e-ii).* Its fields are exactly `{witnesses, continues_from}`.
  - `witnesses` is a model that passes `WitnessModel.validate` (`quorum_sound` and class-sound, the "`deployment_classes_sound` at redesignation" of step 6's row) and differs from the model in force.
  - `continues_from` is the digest of the entry it is appended after, `A`: the intact head.
  - F54's loss evidence must abandon nothing. Every reachable checkpoint and the mark must end at `A` (§23.8), and any other evidence is F62's.
  - Under `UNQUALIFIED`, "the record states that continuity rests on that evidence": F55's report object is stored with the entry, and the record's `refs` names it (`{store: LEDGER, digest, media_type: application/json}`). Admission recomputes it, as for a loss.

  `prepare_redesignation(model)` gives the operator the fields and the reference.
- **F61** *The dual trial and a provisional entry (7e-ii).* The trial (F51) qualifies the extended chain under the new set, with the entry's checkpoint at every writable new witness. Where the old set reaches its read quorum `r`, it also qualifies the chain under the old set, with the checkpoint at every writable old witness. Both must be `QUALIFIED` at the new position: §23.8's "admitted under both old and new quorums where the old is reachable".

  A redesignation is admitted over a provisional entry (§22.4); its admission settles that prefix.
  - **Own provisional entry.** 6b's completion runs first. If it succeeds the head is settled, and the redesignation is routine.
  - **Another host's provisional entry.** The completion is skipped rather than halting (review 7d2d1c0 N1).

  A provisional entry whose checkpoint reached some witnesses, but fewer than `q_a`, reads `UNQUALIFIED` rather than provisional, since `H*` must extend every observed checkpoint (§23.4). It takes the `UNQUALIFIED` route: the record names its report, and `continues_from` is that entry. The "`QUALIFIED` with a provisional entry" route is the case where no witness holds its checkpoint, as after a crash before distribution. Both routes admit (review 00b4c1a N1).

  Until the redesignation is held, the chain carries two entries beyond `H*`. §23.4 exempts that one case from the critical flag, and qualification exempts it when the newest entry is a redesignation appended directly over the provisional one.
- **F62** *A loss that re-establishes the witness set (7e-ii; revision 26 after the check of c36b278e, B2).* §23.8: "any evidence of a later head not proved never admitted makes the record carry a `LEDGER_LOSS`". Schema 1 expresses that. §23.6's loss carries "the global control facts re-established from its position — witness model and set, ...", and is "admitted under the quorum it re-establishes (and the old one where reachable)". So a `LEDGER_LOSS` whose `controls.witnesses` names a new set is the redesignation that carries a loss. Revision 25's claim that schema 1 could not express it, and Q-F15, are withdrawn.

  7e-ii builds it:
  - F46 is amended for the witness member alone. A loss's `controls.witnesses` may differ from the model in force, when it passes `WitnessModel.validate` like a redesignation's (F60). The trust roots and the ruleset still must equal the retained ones, until their fold exists.
  - A loss with changed witnesses starts a segment at its position (F59).
  - Its trial is F61's dual trial: the new set, and the old set where it reaches `r`.
  - A redesignation with evidence of a later head is still refused, naming the loss as the route.
- **F63** *A continuity attestation's checks (step 7f).* Step 5 (`dependency_codes`) judges the record as §23.7 and §3.4 define it, instead of refusing it outright:
  - `target.loss` names an admitted `LEDGER_LOSS`: `REF_TARGET` when it names no record, `DEP_TARGET_KIND` when it names another kind, and `DEP_TARGET_ORDER` unless the loss is strictly earlier;
  - every `listed` id is a subject of the structure or a known record (`REF_TARGET`). §23.7's scope lists "subject ids, record ids", and a part has no meaning for `exposed` (check of 66ac030b, note 1);
  - every `evidence` digest is a content reference the ledger stores or the request carries (`REF_OBJECT`, the code for an unstored ledger object). This is a conservative choice: §23.7's evidence may live elsewhere, but Phase F requires it stored;
  - its actor is human, under the human floor that `Support` already enforces.

  The record is then `SCHEMA_UNSUPPORTED` anyway, because no policy key designates its actor (F48). Its other codes are reported beside that, so the refusal says what else is wrong.

  A `CHALLENGE` of a continuity attestation is permitted (§3.4: "any qualified actor may challenge it"), so its `SCHEMA_UNSUPPORTED` is lifted. It is unreachable while no attestation can be admitted, and is tested on the trial's derivation facts.
- **F64** *The rest of the recovery kinds (step 7g; revision 29 after the check of 66ac030b, B1).* Each has its field checks, as functions in `admission/lifecycle.py` run by `admit_lifecycle`, and a placement:
  - **`REPLICA_REDESIGNATION`: refused, by SD-75.** `location` is closed to `{repository, ref}`, genesis's own `location` shape, with this ledger's ref and a repository that differs from the location in force. The gate still refuses it in every state. Admitting it would record a new authoritative replica while Admission keeps writing the one in the SSDS home, so the record would be false. §23.8 pairs it with the replica restore, which SD-75 hands to Phase H.
  - **`REDACTION_NOTICE`: built and admitted.** It is §24.2's rotation branch ("keep history; append a `REDACTION_NOTICE`; no guarantee yields"): a recorded, human-gated act with no derived effect. `objects` is a non-empty list of distinct digests the chain stores. It is not a recovery kind (§22.1), so it carries the expected head as `obs` and goes through the held head, as a `KEY_LIFECYCLE` does. Revision 28's "a redaction halts derivation" had no textual basis and is withdrawn: §24.2's halt belongs to the incident, not to the notice.
  - **`LINEAGE_MIGRATION`: refused until Q-F16.** `predecessor` is closed to `{ledger_id, last_position, last_entry_digest}`, naming another ledger. Admitting it needs §24.2's qualification that the replacement derives the same state up to renaming, which is the replacement lineage's re-encoding. The G2 workplan places §24 in Phase F, and §1 says the re-encoding runs on fixture ledgers, while §6 has long said it is not built until Phase H. Moving it is the stakeholder's decision (Q-F16), so until then the kind is refused, naming the question.
- **F65** *The Dispatcher at a named `H*` (step 8a).* The Dispatcher may import only the Interface's renderer (fitness), so it cannot reuse `present()`. The composition of currentness moves into the Ledger Store's `qualification` API as one function: the reports and statements of every segment's witnesses, `retirement_held`, `qualify_segments` and the mark. `present()`, Admission and the Dispatcher all call it, so there are not two copies.

  The Dispatcher issues only at a `QUALIFIED` head with no provisional entry, naming it (`issued_at_position` and the head's digest in the journal). The would-issue set is the obligations that readiness routes "dispatch" or "re-dispatch" at that head.

  The journal records intent, then effect, then outcome (catalogue §9, line 431). An envelope signed but not yet journaled is never handed out, and a restart completes or abandons each intent by its identity. On the real ledger `dispatcher serve` runs observe-only: it computes and reports the would-issue set, and issues nothing (F8).
- **F66** *Contract binding (step 8b; Q-F17).* An item task's envelope carries `contract_revision` = the item's `{unit, rev}` (`Workflow.item_of`), and each record bound to it copies that into `binding.item`. Authentication already compares the two. A system-kind task (§13.6) needs a system contract id: the catalogue names it (line 1419) but defines no form, and schema 1's `binding.item` admits only `{unit, rev}`. Q-F17 settles it. Until then system-contract tasks are not issued, and item tasks are. The brief's digest formula, now written twice (line 818), gets one owner.
- **F67** *Scheduling constraints (step 8c).*
  - **Serialization surfaces** are a policy key with an empty default. At most one mutating task per surface is leased at a time.
  - **Coordination tasks.** At most one coordination task per plan is open.
  - **Leases** live in the Dispatcher's home under `state/<ledger id>/` (SD-64), keyed by the Level 0 worktree identity (K2). An expired lease frees its surface for scheduling only: Admission's checks never read a lease, so correctness never depends on one.
  - **Joint-invariant reviews**, which derivation derives (§9.2), are scheduled like any other judgment.
  - **Suspension and resumption.** A `BLOCKER` suspends a task, whose journal entry is resumed by identity once its coordination decision is admitted.
- **F68** *Judge selection (step 8d).* The Dispatcher chooses among derivation's `eligible_judges`, excluding `W`'s authors (RR-11, §16.5), and launches the judge in a context distinct from the authoring task's: the launch attestation's `input_sessions` exclude it.
  - **Recording.** The judge's lineage class, model family, route and toolchain are recorded in the bound record's `provenance`, which the schema leaves open. `ENVELOPE_FIELDS` is closed and signed, and adding to it is a catalogue §12.2 change.
  - **Harness.** Only the stub harness runs (F8).
  - **`HUMAN_ATTESTED_FRESH`** (line 159) is built in 8d with the routes it serves, the manual and Git-envelope routes. Catalogue §5.10 (a): "The classification is fixed at admission from the binding and any co-submitted attestation; a later attestation does not change it." So a `LINEAGE_ATTESTATION` by an authenticated human (R3), co-submitted in the same request as the judgment it attests, gives that judgment `HUMAN_ATTESTED_FRESH`. A later attestation never does. A `LINEAGE_ATTESTATION` is support-tier, so no strictly-earlier rule bars co-submission (plan check of 5d4a0e2, answer 3 and note 1).
- **F69** *The task-bound interface (step 8e).*
  - **`open(task)`** finds the task's envelope in the Dispatcher's journal, renders the brief, and refuses it if the rendered brief's digest differs from the envelope's `brief`.
  - **Answers** are given at the task's basis (the envelope's `issued_at_position`), not at the presented head.
  - **Reads.** Each `read` call during the task appends `(unit, rev)` or the path's content identity to the task's basis record, in the Dispatcher's journal. The brief and the result's provenance say "reads not observed" on the manual and Git-envelope routes (§16.4).
  - **`ask(changed)`** defaults `since` to the basis and `units` to the task's units.
- **F70** *Transports (step 8f).*
  - **The Git-envelope transport** (§16.10) is `interface.envelope`, fitness B1's reserved exception for a writing Git subcommand. It writes `refs/heads/ssds/run/<task-id>` only in a repository that is not the product repository: at run time it refuses a repository whose root or common directory is the observed product's. Tests run it in scratch repositories only.
  - **The MCP server** is JSON-RPC 2.0 over stdio, built on the standard library, so no new runtime dependency comes to the stakeholder (line 739). It exposes the same operations as the CLI, through the same `Session`. It pins the MCP protocol revision it implements, and its tests cover the initialize/capabilities handshake beside "the MCP operations equal the CLI's", since no SDK checks conformance (plan check of 5d4a0e2, answer 6).
- **F71** *Retry and resubmission (step 8g).*
  - **Mechanical retry** re-dispatches within the item's budget (built in derivation).
  - **An integration request** is built as §11.5 (3)'s candidate plus references read from the ledger (F32). It is submitted, and refused `SCHEMA_UNSUPPORTED` under SD-70, which the test asserts.
  - **`REISSUE`.** The Dispatcher resubmits the retained record under the re-issued task's envelope, with the refusal as provenance, and Admission's refusal of `reissue_of` is lifted for exactly that form. The conflict noted as N5 (line 986) is read as follows. §8.3 step 3's specific rule ("keeping its original actor and lineage class") governs the re-issue, over §25.1's general rule that an envelope authenticates its own task's agent. The re-issued envelope lists the retained record's identity, and authentication accepts the original actor only for that listed identity. The lineage is verified from the retained record's original binding object (F9, F11), whose envelope signature and launch attestation remain verifiable: it was refused only because the retirement did not list it. The class is never taken from the re-issued envelope (plan check of 5d4a0e2, answer 4 and note 2).
  - **§9.1.** When Admission requeues a request at a new head, the Dispatcher re-derives the task's basis there and re-requests; it never resubmits the old basis silently.
- **F72** *Judge selection and a human's attestation of a fresh session (step 8d; revision 31).*
  - **Choosing a judge.** `select_judge(workflow, o)` takes derivation's `eligible_judges(o)`, which already excludes `W`'s authors (§16.5).
    - It prefers a freshly launched agent reviewer, on the harness route, whose launch attestation's `input_sessions` are empty. A judge reads no authoring session, so its context is distinct from the authoring task's.
    - Otherwise it names an eligible human, on the manual route.
    - With none, the task is not issued; readiness already waits ("no eligible judge").
  - **Recording the judge.** `judge_provenance(issued, family, toolchain)` gives the record's `provenance.judge`: `{lineage_class, route, model_family, toolchain}`. The submitting adapter stamps it. Nothing derives from it, and authentication does not read it, so it is an audit fact (§12.2's closed envelope).
  - **The brief's notice.** A judgment task's brief tells its judge, when `authors(x)` holds unknown authorship, that an independent answer then needs a `NON_AUTHORSHIP_ATTESTATION` from a human (§5.10 (f)), or is the owner's (line 966).
  - **`HUMAN_ATTESTED_FRESH`.** §5.10 (a): "fixed at admission from the binding and any co-submitted attestation". A request is bound by a task or by a human, never both. So a manual or Git-envelope task binding may also carry `human: {actor, signature}`: the SSH signature of the human who ran the fresh session, over the request without its binding, as a human binding signs. Authentication then reads it as follows:
    - It verifies the signature against a registered human key, or the whole binding authenticates nothing.
    - Records whose actor is that human are authenticated by it, but only a `LINEAGE_ATTESTATION` (outcome `HUMAN_ATTESTED_FRESH`) targeting a record bound to this task in the same request. Any other human record in a task-bound request is `AUTH_ACTOR`.
    - A bound record may then carry `binding.lineage_class` `HUMAN_ATTESTED_FRESH`, with an empty lineage, only when such an attestation targets it. Otherwise its class stays `UNKNOWN` (F11), and a mismatch is `AUTH_ENVELOPE`.
    - A harness binding never carries a human co-signature, since its lineage is proved by its attestation.
    - A later attestation changes nothing, since derivation reads the class from the binding.
- **F73** *Retry and integration requests (step 8g-i).*
  - **Mechanical retry.** Retry composes what is built: when a task finishes and derivation still routes its item "re-dispatch" within budget, the obligation is `READY` again and `would_issue` gives a new task at the new head. The budget, and the route to coordination once it is spent, are derivation's (§13.7).
  - **Integration requests.** `integration_request` builds §11.5 (3)'s request: the candidate commit plus references to the admitted records, read from the ledger (F32), carrying no record. The task's `TASK_RESULT` is its own records-only request, admitted first (§11.5 (1)): Admission reads the transformation an *admitted* result submits, and a second request carrying the result would be a second result (§8.3 step 7; review of 26907956, B3). Admission refuses the integrating request `SCHEMA_UNSUPPORTED` under SD-70.
  - **§9.1's re-request.** Admission revalidates first: its step 9 absorbs the observation and revalidates the same request at the new head. The Dispatcher acts only on Admission's outcome (plan check of 53216046, answer 3). While that outcome is pending, the old task stays open and no second task is issued for its obligation. Once the outcome is known, `rerequest` finishes the old task and re-derives at the new head:
    - if the request was admitted, its obligation is no longer `READY`;
    - if it was refused stale, derivation's own route governs (a pending candidate derives `REVALIDATE` for the same task; a content change is a new iteration, §4.1, §10.4).

    A new task is issued only where derivation makes the obligation `READY` again; the old basis is never resubmitted. Test: no duplicate task while Admission's revalidation is pending.
- **F74** *A re-issue's resubmission (step 8g-ii; review N5, F71).* The re-issued envelope cannot "list" the retained record: catalogue §12.2 closes the envelope's fields, and `predecessors` means something else. The list is the derived `REISSUE(envelope)` obligation itself, whose parameters name the retained identities (`Workflow._reissue_obligations`). The re-issued task is the original task re-issued by a key in force (catalogue: "under the re-issued task's envelope … keeping its original actor and lineage class"). Its envelope names the original obligation and role, and copies the original `governs`, all read from the retained original envelope (the resubmitted content must equal the retained body, `governs` included, or step 3's `AUTH_VERSION` refuses it). The envelope stays coherent under §12.2, and a resubmitted record's `binding.obligation` keeps naming what it answers, as derivation's binding index and step 7 read it (re-check of 25bd1d0d, B1). Step 3 reads a re-issue as follows (plan check of 53216046, B1):
  - **Existence.** For exactly the identities a `REISSUE(envelope)` obligation derived at the base lists, the existence half of step 3 is met by that obligation. The original obligation need not exist at the base: by the re-issue it may be answered or no longer derived (`REVIEW(X)` once X has a passing review), and a never-lost record must not be lost for that (step 7; F41).
  - **Role and kind.** The original obligation's `role(kind(o))` is judged under the ruleset in force at the original envelope's `issued_at_position`, as at its issue (re-check of 25bd1d0d, note 1).

  A resubmitted record is then authenticated when all of the following hold:
  - its `provenance.reissue_of` names a retained identity that a `REISSUE` obligation derived at the base lists;
  - its content, apart from `id` and `binding`, equals the retained body stored with the refusal, its `provenance` being exactly the retained provenance with `reissue_of` added, and each identity is cited once per request (review of 26907956, B2);
  - its actor and `lineage_class` equal the retained record's;
  - its `binding.lineage` equals the retained binding's, whose lineage was verified from its original stored binding object (F9, F11; plan check of 5d4a0e2, note 2).

  The original actor is accepted only for those identities (§8.3 step 3 over §25.1, F71): an envelope of a task ever refused under an unlisted retired envelope is a re-issue, and carries nothing but such resubmissions, while the original obligation stands and after `REISSUE` is discharged (review of 26907956, B1). A record retained with `HUMAN_ATTESTED_FRESH` is resubmitted only with its co-signer's new `LINEAGE_ATTESTATION` (8d's path), since the original attestation is not retained. Admission's refusal of `reissue_of` is lifted for exactly this form, and derivation's `_resubmitted` then discharges `REISSUE`. This corrects F71's "the re-issued envelope lists": the catalogue never says the envelope lists the record. Test: a retained adverse review is resubmitted after its `REVIEW(X)` obligation is gone, and is admitted. Test: a resubmitted adverse review counts in `REVIEW(X)`'s answering and routing as the original would have.
- **F75** *The evidence obligation's identity (step 9c).* Catalogue §10.2 identifies an evidence obligation by its claim lineage and its specification lineage. Phase D's code uses per-domain policy tokens (`evidence = ["obl"]`), so `admissible` cannot find "the specification revision `e` names". The code diverges from accepted authority, so it is corrected to the catalogue: the obligation is derived from the `EVIDENCES` relation between a claim and a specification, and policy names only the claim kinds that need evidence. Phase D and E fixtures that use tokens are migrated in the same part (9c-i, reviewed alone). Their expected values are re-derived from the Stage S cases and the authority, as §4 requires, never copied from the new implementation's output, so the migration cannot confirm itself (plan check of 09df7c27, answer 2).
- **F76** *Where runner keys live (step 9a).* Catalogue §17.5 says a runner's "identity key registered in policy"; §25.2-§25.3 say trust roots change only by genesis or lifecycle records. Both hold: the key is a trust root (genesis `runner_keys` or `KEY_LIFECYCLE` role `RUNNER`), and policy designates the runner class and names its key ids. The catalogue's wording conflict, and §17.5's lag behind the Manual's A6 wording on attributes the Dispatcher cannot request, go to the Manual clarification batch. The Manual governs.
- **F77** *Who signs a runner observation (step 9a).* §25.1 has the issue key sign "Dispatcher-submitted observations" and runner keys sign for runners. A designated runner's `REALIZATION` is signed by its runner key, whose binding authenticates only `machinery:<component>@<key id>` records of the runner-observation kinds. The Dispatcher transports it and signs nothing in it. In Phase F the issue key signs envelopes only: the Dispatcher submits no observation of its own (plan check of 09df7c27, answer 3). An external custody runner's observations and its `CUSTODY_ENUMERATION` are signed by its custody identity key, a `RUNNER` trust root, under the same binding.
- **F78** *Fields schema 1 lacks (step 9d).* The `INCOMPLETE` reason, the start and end positions, the runner and the unpinnable flag have no fields of their own. §17.2 names them as members of the realization's execution, so they are carried in a closed inner shape of schema 1's open `execution` object, which Admission checks at step 1. A malformed one is `SCHEMA_RECORD`. No schema version changes: this is Admission refusing semantics it does not understand (§8.3 step 1), as F46 did for the recovery fields. The inner shapes are read through one owner in derivation and recorded as notes for the next schema version.
- **F79** *The time bound (steps 9c, 9f-ii).* §6.9 and §17.1 have the specification declare a bound and the system cap it. For a Dispatcher-run class the effective bound is the smaller of the declared bound and 168 h. A declared bound above 168 h on such a class is a static finding. Time runs on the wall clock from the process's start, under an injected clock in tests. Reaching the bound ends the realization `INCOMPLETE` with that reason.
- **F80** *A discriminating reading's shape (step 9e).* Schema 1 has one `outcome`, and §6.6 needs an `(observation, reading, verdict)` pair, with a reason code and a content reference when the readings differ. `outcome` is the target's verdict, and `observations` holds both items in a closed inner shape.
- **F81** *Enumerated custody runs not admitted (step 9c).* §6.9 counts enumerated runs for its conditions (2) and (4), but an unadmitted run has no outcome to compare. It fails closed: the stop is blocked until each enumerated run is admitted.
- **F82** *Where step 5's deferred cases land (step 9c-9d).* Of the cases step 5 sent to step 9, only those over admitted trees are reachable: 5d's evidence-term predicate on an admitted claim. Those on candidates and merged trees stay with SD-70, and the comparison and a fall from `T` to `P` with SD-71 (§6).
- **F83** *The outcome shape (step 9b).* Phase D stores per-output verdicts, which §17.3's `{output name: value}` omits. An embedded oracle's verdicts are declared outputs of the specification, so the stored shape is §17.3's with those outputs named. The derivation reads them through the specification, not through a separate verdict field.
- **F84** *The specification declaration (step 9b).* §17.1's TOML is parsed by one closed parser in `content`, from exactly one fenced `ssds-spec` block in the unit's Markdown or one `*.ssds-spec.toml` file inside its scope; none or more than one is a static error of the unit. Its keys are exactly §17.1's (`oracle`, `runner`, `time_bound_hours`, `outputs`, `verdicts`, `fixed`, `granularity`, `output_renames`); an unknown key fails closed. Static checks: output names distinct; each output's `type` one of `float64`, `int`, `bool`, `enum` (with its values) and `digest`, §17.3's scalar forms; a `float64` output's `canonical` one of `binary64-hex`, `decimal-shortest` and `rounded:<n>`; a `DECLARATIVE` specification's verdicts each naming a declared output and one of the seven templates; an `EMBEDDED` one's verdicts each naming a declared output and the `enum` output with values `PASS` and `FAIL` that carries its verdict (F85; the `embedded` key is a D4 extension of §17.1's syntax, sent to the Manual clarification batch); an `ASSESSOR_READ` one declaring none; `time_bound_hours` a positive number; `granularity` `SINGLE` or `ENSEMBLE` with §17.1's fields; renames naming outputs. A template's parameters are checked now for the obvious constraints (a tolerance finite and non-negative, `ULP_TOL`'s `n` a non-negative integer, `RANGE`'s `lo ≤ hi`, `MONOTONE`'s outputs at least two, declared and numeric), so no later system version invalidates a revision for them; Q-F21's further rules apply once settled, and until then the templates it covers are accepted but never evaluated (plan check of db0bf1ce, note 3). `fixed`'s keys are linted against the runner class's declared attributes: a fixed attribute the class does not record would make every realization inadmissible (note 2). A static error makes the specification unit defective: no `REALIZE` is derived for it, no assessment under it is admissible (§17.4), and lint reports it (note 1). The runner class is checked by the lint against policy (E20, 9a), and a Dispatcher class's bound above 168 h is a lint finding (F79).
- **F85** *Outcomes stored in §17.3's shape (step 9b; F83 made concrete).* The evaluated outcome is the canonical JSON object `{output name: canonical value}` over the declared outputs. An embedded verdict is itself a declared output, an `enum` with values `PASS` and `FAIL` (§17.3's enumerations; plan check of db0bf1ce, answer 1), and the declaration's `verdicts` entry `{output = x, embedded = v}` names which output carries `x`'s verdict. Derivation reads `x`'s value and verdict through the declaration of the specification revision the realization ran under. Phase D's `{"outputs": {x: {value, verdict}}}` shape is retired: `Assessments` and its fixtures move to the new shape, with expected values re-derived from §6 and §17.3, and from the S5 §6 case wherever a case states an outcome, never from the new implementation's output (§4). Identity of outcomes on failing outputs stays byte equality of canonical values (§17.3).
- **F86** *Which oracles 9b evaluates (step 9b).* `EXACT` is byte equality of the canonical value with the declared reference's canonical form. The reference is canonicalized by the same canonicalizer as the output's declared form (a `binary64-hex` or `decimal-shortest` reference parsed to its binary64 and canonicalized); under `rounded:<n>` a reference not already canonical is a static error (plan check of db0bf1ce, answer 3). The other six wait for Q-F21: the three tolerance templates, `RANGE` and `MONOTONE` compare numbers with edge questions. `MONOTONE` is defined over a declared ordered list of scalar outputs named in its parameters, so it needs no collection form (B1). `SET_EQUAL` compares a collection, for which §17.3 lists no canonical form, and waits for one. Until then they are unevaluated, so `yields` fails closed on them (§6.5).
- **F87** *The evidence obligation's identity, concretely (step 9c-i; F75 made concrete).* Today the identity is a policy token (`[domains.D4] evidence = ["obl"]`), read at eight sites (`assessment`, `briefing`, `queries`, `items`, `support`, `workflow`).
  - **One owner.** `State.evidence` (`derivation/evidence.py`) is the one owner of evidence obligations. Every site reads it, none reads the policy token.
  - **Identity.** An evidence obligation is `(claim unit lineage, specification unit lineage)` (§10.2). Each name is the root of its unit's `renamed_from` lineage, folded over the admitted structures (`queries.lineage`; §1.2: removing a `renamed_from` never removes admitted lineage), so a rename keeps the identity. The token is `evidence:` and the SHA-256 hex of the canonical JSON of `[claim root, spec root]`. That is 73 characters whatever the names' lengths, so it always fits schema 1's 200-character token grammar, where a readable `evidence:<claim>@<spec>` would not for long unit identities (plan check of 298a12a0, B1). An `EVIDENCE_ASSESSMENT`'s `target.obligation` carries the token. `State.evidence`, briefs and views keep the readable pair beside it. A unit deleted and later re-created under the same identity with no `renamed_from` gets the same root, so its obligations share the old unit's identity. That is conservative: old failures keep counting, and old passing evidence cannot, since §17.4's currency requires the current claim revision (note 1).
  - **Required.** At a state, subject `s` requires `e = (c, p)` when an authored `EVIDENCES` relation runs from specification unit `p` to a claim unit `c` inside `s` (`c = s` or a unit inside its scope), and policy requires evidence for `s`'s claim kind.
    - The per-domain policy key `evidence` becomes a boolean (`evidence = true`), §25.3's "evidence obligations per claim kind", the claim kind being the subject's domain.
    - The token list was Phase D's own divergence from §10.2, which F75 judged an implementation correction, and no ledger or repository holds a policy with the key, so it is corrected in place under F75 (plan check of 298a12a0, answer 2).
    - A claim of an evidence-requiring domain with no `EVIDENCES` relation requires nothing, and lint reports it as `EVIDENCE` (no specification evidences it). This is the catalogue's model, obligations arising only from relations, and it is the one place this reading is not conservative: such a subject can become valid with no evidence. It is disclosed, and the stronger rule is Q-F23 (note 2).
  - **Lineage.** `e`'s lineage follows the claim's successors: a retarget (the `EVIDENCES` relation now naming a successor claim unit) and a split (several successors). A successor is a unit that received regions of a former claim unit, the same rule `home` uses. Renames are already the identity. A split of a *specification* is not followed: the old obligation retires and its failures keep counting, which is safe (answer 3). `qual` reads a failing assessment of any obligation in the lineage of one the subject requires, and of a retired one (§10.2: retirement, split or retargeting never disposes of a failing assessment; F41).
  - **Expected values.** The Phase D and E fixtures move to relation-derived obligations, their expected values re-derived from the Stage S cases and §6, §10.2, never from the new implementation's output (§4).
  - **Tests.** A rename keeping the identity. A retarget and a split keeping a failing assessment counting. Retirement keeping the disagreement in `qual`. Two specifications evidencing one claim giving two obligations. A passing assessment of one never answering the other ("assessments for different obligations never conflict"). The policy boolean, and the `EVIDENCE` lint.
- **F88** *The realization's one reader (step 9c-ii-i; F78 made concrete).* `derivation/realization.py` owns the closed inner shape of a `REALIZATION`'s `fields.execution`:
  - the basis keys (`tree`, `context`, `units`, `reads`, `widened`, `pins`, `unpinnable`, `attributes`, `bounded_by`);
  - `runner` `{class, key}`, whose key equals the actor's `@<key id>`;
  - the runner class's `class_attributes` and `observes_outside_reads`, recorded by value (§6.3);
  - `start` and `end` positions;
  - `incomplete`, one of §17.2's five reasons, present exactly when the outcome is `INCOMPLETE`, as `evaluated` is exactly when it is `COMPLETE`.

  `fields.configuration` is the instantiated revision's `fixed`, with an `ENSEMBLE`'s replicate count, statistic and seed policy. A malformed shape serves no permissive use, and its adverse matching uses (conditions (2) and (4), `link⁻`) are unchanged. An assessment of it, passing or failing, is not admissible: F89 (d) needs its runner, and 9d's step 1 keeps such a realization out of the ledger (review of d481277f, note 1).
- **F89** *Admissibility (step 9c-ii-i; §17.4, §17.5).* `realization_ok(real, e)` is the one owner, read by `admissible`, by `REALIZE` and `ASSESS`, and by conformance's required evidence.
  - **(a) The obligation.** The realization's specification and a claim unit of its target give `e` (F87), directly or through the claim's lineage. "The revision `e` names" is read as that lineage plus §6.6's reading rule, since F87's identity names no revision.
  - **(b) Fixed attributes.** Each `fixed` attribute of the instantiated revision's declaration (`declaration_at(spec.unit, spec.rev)`) equals the recorded attribute.
  - **(c) Completeness.** The realization is `COMPLETE`, with its evaluated outcome stored.
  - **(d) The designated runner.** It is `MACHINERY`. Its key is a runner trust root at the realization's admission position, designated for the declaration's runner class by the policy in force there (§6.3: decided at realization, recorded by value).
  - **(e) The compromise discount.** An observation admitted at or after its key's compromise position is untrusted.
  - **The two sides.** A passing assessment needs (a)-(e) and a usable declaration (9b-ii). A failing one needs (a)-(d), keeps 9b-ii's narrowing for a defective declaration, and keeps counting under (e): a forged failure is disposed of by the owner, first by an upheld challenge against its realization on the ground that the key was compromised (Manual §6.7), or by `IMMATERIALITY`, so failing evidence is never dropped (§6; F41; plan check of 4432948d, note 1).
  - **Consumers.** `ADJUDICATE_DISAGREEMENT` (`workflow.py`) and the §6.8 disagreement (`reports.py`) read admissibility too, since today they derive from a failing assessment unchecked.
- **F90** *Permissive matching reads the class (step 9c-ii-i; §6.3, §17.5).* `ext` treats a realization as having an unpinnable read when it recorded one, when its class does not observe every read outside the tree, or when it lacks a recorded attribute its class records. `standing` also needs the observation trusted (F89 (d)-(e)) and its references available (F92).
- **F91** *A realization's currency (step 9c-ii-ii; §17.4).* A `REALIZATION`'s support node carries three implicit entries:
  - its recorded execution basis (`execution`, class `CONSUMER:REALIZATION`);
  - `content` on each claim of its target;
  - each bounding completeness judgment being current.

  `execution_current` reads the bounding judgments' currency. Stale passing evidence then never discharges.
- **F92** *Binding health (step 9c-ii-ii; §17.4).* A reference is unavailable when the latest acting `AVAILABILITY` record on its digest says `UNAVAILABLE`. That covers a realization's evaluated outcome and its envelope's references.
  - A passing assessment whose realization needs such a reference contributes at most `P` to `ev` ("not `T`"). `P` is the minimal faithful reading: discharge outside a risk override's scope stays open at `P` (§10.4, §10.5), and `F` would also block a human's risk-override continuation, for which the text gives no warrant (plan check of 4432948d, answer 4).
  - Its observation is not standing, and `REALIZE` treats the realization as not current.
  - Adverse uses are unchanged.
- **F93** *Completing `stale` (step 9c-ii-iii; §6.6, §6.9, §17.5; F81).*
  - **`link⁻`.** Its `o'` ranges over every admitted observation of `conf(a⁻)`, an `INCOMPLETE` one included. Today it omits them, which can make a failure stale wrongly. `INCOMPLETE` observations still serve none of conditions (1)-(4).
  - **Custody.** An observation of an `EXTERNAL_CUSTODY` class serves (1) or (3) only when all of these hold:
    - the latest admitted `CUSTODY_ENUMERATION` of that class exists, signed by one of its keys (the class, not the key, so a rotation is covered);
    - it lists every admitted realization of `conf(a⁻)` by that class;
    - every run it lists is admitted (F81);
    - it lists the observation itself.
- **F94** *The "either" clause and renames (step 9c-ii-iii; §6.5, §6.6).*
  - **The "either" clause.** Where an observation lacks `x`, or G's reading has no verdict on `x`, the failure is yielded only if `a⁻`'s check on `x` was in force at `a⁻`'s base. A defective declaration there counts as in force (fail closed).
  - **Renames.** `output_renames` maps a name one hop, through the later revision's own renames. An unmapped name is not evaluated. `restricted` and `failing_outputs` use the same mapping. Composing renames along the revision lineage would keep a twice-renamed output evaluable; one hop is coarser and safe (such a failure is yielded through the "either" clause), and it is disclosed (note 2).
- **F95** *The evidence obligations (step 9c-ii-iv; §10.2, §6.8-§6.9).* They are derived in the admitted state only: a frame derives none (SD-70).
  - **`REALIZE(e)`, Dispatcher.** Derived for a required `e` with no current, complete realization passing F89 that instantiates the current specification revision on the current claim revision. It is not derived for a defective specification, and waits when the runner class is undesignated. It ends once such a realization exists; an `INCOMPLETE` one never ends it. A target change is reviewed through `REALIZE` and then `ASSESS`, with no new kind.
  - **`ASSESS(realization, e)`, reviewer.** Derived for an admitted, complete realization passing F89 with no acting assessment of it for `e`, whatever its currency, so an unassessed failure is never lost. It is answered by the first acting assessment, of any outcome.
  - **`RERUN(a⁻, on)`, Dispatcher.** Derived for each of conditions (1) and (3) that a counting, admissible, unstale failure without a disposition lacks (§6.9). It is not derived when (2) failed or when no current completeness judgment bounds the configuration's execution closure (§6.9's condition, which also covers a bounded basis whose bounding judgment is no longer current; note 3). It ends once a complete admitted observation of `conf(a⁻)` on that tree with `ext`-equal pins and attributes exists, so an unserving run never loops and the failure then stays with its owner; an `INCOMPLETE` rerun (a crash, a failure to start) does not end it (note 4).
  - **`READING(a⁻)`, reviewer at §6.8's class.** Derived as `RERUN` for an assessor-read failure whose condition (3) observation no standing discriminating reading covers. It is answered by a discriminating reading (9e) or a failing assessment of that outcome.
  - **Retries.** `REALIZE` and `RERUN` stay open after an `INCOMPLETE` run. The Dispatcher bounds its re-attempts operationally, by a budget with backoff journaled per obligation, so a runner that never starts does not loop without limit (9f-ii; note 5).
  - **The floor.** The `INCOMPLETE` trigger of §6.8's floor is subsumed by Phase E's E34 floor, which every disjunct shares; a test pins it.
  - **Expected values.** No Stage S case covers admissibility, custody or these obligations. The expected values of 9c-ii's tests for them come from the cited text alone (§6, §10.2, §17), and the exit lists those cases as authority-derived, not Stage-S-derived (note 6).
- **F8** *No campaign.* The Dispatcher issues envelopes to fixture executors, and to the manual and Git-envelope routes in scratch repositories, where lineage is `UNKNOWN` unless a human attests it (§12.2). Its harness route is built and tested against a stub harness, never a live model, without a campaign authorization. On the real shadow ledger `dispatcher serve` issues nothing and writes no run ref.

## 6. Fail closed until a later owner

Until the stakeholder settles Q-F1 and Q-F2, steps 10-11 do not run, and the exit reports the difference study as unexecuted.

SD-64 settled Q-F3: runner processes are confined by `bwrap` (F2), with workspaces under `runs/` in the SSDS home. Real-runner execution on the real ledger waits for a campaign (F8).

Until Phase G admits intake records, an `INTAKE_*` record's `paths` target uses the token grammar; Phase G gives it a validated, repository-contained relative path (Manual §25.4; review 8230421 N3). Until Phase G, a change of unknown provenance on the real shadow ledger is absorbed and goes no further than its §18 intake obligations, which are derived but not routed beyond `INTAKE`. The exception is SD-69's: step 10's human `ABSORB` adoption of the two reserved leaves (F1).

Until Phase H, failure points beyond those group 4 names are untested. Until Phase H builds it (SD-76), §24.2's replacement-lineage re-encoding is not built and `LINEAGE_MIGRATION` is refused (reading F64; this corrects the older wording, which put the re-encoding in Phase H without a decision).

Until an authorized campaign, no live agent submits to Admission.

Until step 4c-iv builds the schema-1 correction SD-69 adopts for Q-F6 (i), adoption by `ABSORB` is `SCHEMA_UNSUPPORTED`; until Stage S settles Q-F6 (ii), so is a change of an existing unit's kind or owning domain (reading F16). Until Phase G, a cutover an integration carries is too. Until Stage S, a quarantined key that a candidate authors to the value a foreign change put on the observed tree is refused `STRUCT_REVALIDATE` (4c-ii), a stronger rule than Manual §7.2 alone.

Until steps 5-8 (4c-iii; review 23b487a N1), these fail closed:
- an integrating request bound to anything but the producing task of its candidate's submitting result;
- an integration of a human-produced candidate, which has no contract (`AUTH_WRITE_SCOPE`);
- plan units in an integration's write set, even for a planner role (§12.3);
- more than one candidate per request.

Until step 6 builds the commit, an accepted structure-changing request is unreachable, so its frame trial (4e-i) is exercised only on derivation histories and by the engine's wiring. A rejected one salvages its never-lost records by their own step-3 and step-5 reading at the head, where the rejecting entry admits them. A record declaring an unintegrated `X` is read in `X`'s frame there too (F27; review cab6179a B1).

Until heads hold acceptances (steps 6-8), a request-level support cycle among a request's own records is unreachable through the engine. Each record would rely on a subject that no acceptance at the head makes valid, so step 6 refuses it first. `CYCLE_SUPPORT`'s engine reading is therefore tested by driving the trial.

Until Phase H builds F47's ref restore (SD-75, Q-F14), these are unbuilt and disclosed at the exit:
- **§5.7's recovery under `INTEGRITY_HALT`**, a `FORK_RESOLUTION` or `LEDGER_LOSS` appended after the last valid entry. Admission appends nothing under `INTEGRITY_HALT` (reading F50).
- **§23.8's "authoritative replica lost, none extends the checkpoint" row.** With nothing readable there is no entry to append after, and Admission refuses without a readable genesis (7c; re-check of 5636d55, note).
- **§23.8's "abandoned entries later surface" row.** Its integrity obligation is unbuilt, because no derivation or qualification reading of a surfaced authenticated chain exists, contrary to §3.4's "owned elsewhere" placement. With one replica per ledger (F3), no second authenticated chain can surface in Phase F. A witness that still holds an abandoned checkpoint is already read as abandoned, not merged (7c).

Until the phase that lifts SD-70's gate for integrations builds step 6f (SD-73), fences, settlement, the kept-fence route and `NOT_SETTLED` are unbuilt; no fence can arise while no integration is accepted. Until it builds step 5e, the rebase SD-69's Q-F6 (iii) correction allows, a record declaring a rebase frame is refused `REF_TRANSFORMATION` (§3.1, 4c-iii; SD-71). Until it builds step 5f, step 8's no-collateral-regression check is unbuilt. No integration is accepted meanwhile (SD-70), and the Phase F exit discloses both.

Until step 6 lifts ACCEPT, step 5's checks (§3.2) act only on refusal codes and salvage. Until step 9, a discharge predicate with an evidence term, conformance needing required evidence, a citation against a realization, and step 8's comparison all fail closed (§3.2). A10's step 7 clauses and §16.11 (c)'s occasion templates are unbuilt in Phase F (SD-66). When step 6 lifts ACCEPT, a request carrying a `TASK_RESULT`, or one whose acceptance depends on a task result's conformance, stays `SCHEMA_UNSUPPORTED` until A10's D4 (SD-70, Q-F9 (a)). The exit discloses them.

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

**Q-F8. `INTAKE_CLASSIFICATION`'s target (a clarification of SD-69).** SD-69's row gives both intake kinds "a `delta` target … beside `content_ref`". Catalogue §3.4 gives `INTAKE_CLASSIFICATION` "observed path set or quarantined delta", a path set rather than a content reference; Q-F6 (i) had said classification would be corrected to §3.4 in the same change.
- **Recommended:** (a) a `paths` target (`{paths}`) or `delta`, as §3.4 says.
- **Alternative:** (b) keep SD-69's literal `delta|content_ref`, and send the difference to Stage S.

Nothing in Phase F depends on it: classification stays unadmitted until Phase G. The schema-1 correction in 4c-iv follows SD-69 literally until this is answered.

**Resolved by SD-70 (item 64):** (a). Classification's target is `paths` or `delta`, corrected in place in schema 1.

**Q-F9. A10's step 7 clauses in Phase F.** Manual §8.3 step 7, after A10, adds two clauses: a result that states a memory uncertainty no standing human decision accepts has its passing judgments and decisions refused (§16.11 (g)), and clean conformance includes HAS freshness (§16.11 (f)). SD-66 accepted A10 with "D4 for A10 follows Phase F", and derivation has no project-memory owner, so neither clause can be decided in Phase F. ACCEPT stays gated until step 6 either way, so step 5 is unaffected. Step 6 is not: it would lift that gate.
Clause (f) is part of clean conformance, re-derived "at every revalidation of an integration request" (§16.11 (f)), and §16.11 (c)'s occasion templates feed conformance too ("a result without them is `INCOMPLETE`"). So the clauses govern every request whose acceptance depends on a task result's conformance, not only requests carrying a result. Phase F detects no occasion and reads no answer.
- **Recommended:** (a) when step 6 lifts the gate, these stay `SCHEMA_UNSUPPORTED` until A10's D4: a request carrying a `TASK_RESULT`, and a request whose acceptance depends on the clean conformance of a contracted task obligation (an integrating request, or a claimed discharge reading conformance). Records-only judgments, decisions and reports that read no conformance may be accepted. The Phase F exit discloses both clauses and the occasion templates as unbuilt.
- **Alternative:** (b) fail closed only on a result carrying a PEM slot or a `PEM_UNAVAILABLE` answer, and accept the rest. The exit then discloses that occasions which fire from content (a detected revert or restoration, say) go unchecked. Absent publications do not make the clauses vacuous: clause (g) reads what a result states, and occasions fire from content.

**Resolved by SD-70 (item 64):** (a). Step 6 keeps these requests `SCHEMA_UNSUPPORTED` until A10's D4.

**Q-F10. Steps 5e and 5f after SD-70.** Step 5e (rebase) and 5f (no collateral regression) judge only integrating requests: a rebase frame records `X'` for an integration, and step 8 compares the head with the merged tree. Under SD-70 (Q-F9 (a)), every integrating request stays `SCHEMA_UNSUPPORTED` until A10's D4, which follows Phase F. Step 8's comparison also needs step 9's runners. Both already fail closed: a rebase frame is `REF_TRANSFORMATION` (§6), and no integration is accepted.
- **Recommended:** (a) defer 5e and 5f to the phase that lifts SD-70's gate for integrations (A10's D4), keeping both fail-closed rules in §6. Phase F's exit discloses them as unbuilt, and step 6 follows 5d. This spends Phase F's effort where it changes a decision: step 6's commit path, which step 10's records-only operation and `ssdp-shadow-2`'s repair need.
- **Alternative:** (b) build 5e and 5f in Phase F as planned. They would be tested on derivation histories only, and their decisions would stay unreachable until A10's D4.

**Resolved by SD-71 (item 65):** (a). Steps 5e and 5f are deferred, fail-closed and disclosed at the exit; step 6 follows 5d.

**Q-F11. SD-71's premise and adoptions (information; F42).** SD-71 deferred step 5f on the premise that step 8 judges only integrating requests. Catalogue §8.3 step 8 also concerns structural changes, and a records-only `ABSORB` adoption changes `Σ`. Revision 19 closes the gap by failing closed (F42): an adoption is refused while any admitted realization reads a unit in its write set. This is vacuous for `ssdp-shadow-2`, so step 10 is unaffected.
- **Recommended:** (a) confirm F42's fail-closed rule as SD-71's complement, recorded beside it.
- **Alternative:** (b) build 5f's step 8 for adoptions in Phase F.

**Resolved by SD-72 (item 66):** (a). F42's fail-closed rule is SD-71's complement.

**Q-F12. Step 6f after SD-70 and SD-71.** Step 6f derives fences, settlement, the fence-attention obligation, the kept-fence route (E15) and `NOT_SETTLED`, on hand-built fixture ledgers. Every one of these arises only from an integration's publication effect. A records-only admission has no effect and is never fenced (F1), and under SD-70 and SD-71 no integration is accepted in Phase F. So no fence can arise on any Phase F ledger, as with 5e and 5f.
- **Recommended:** (a) defer 6f to the phase that lifts SD-70's gate for integrations, with 6g's publisher side and 5e and 5f. Its discriminators (362af9f N6, 61cd09b N6, 730490d N2's fence form, the five S3 kept-fence cases, and `NOT_SETTLED`) are reported unexecuted at the exit. Step 6 then closes with 6a-6e, and Phase F proceeds to step 7 (loss and recovery), which the old ledger's retirement statement needs.
- **Alternative:** (b) build 6f now, tested on hand-built fixture ledgers only.

**Resolved by SD-73 (item 67):** (a). 6f is deferred with 6g, 5e and 5f, and its discriminators are reported unexecuted at the exit.

**Q-F13. `ssdp-shadow`'s retirement and its successor (F44, F45).** §24.2 defines retirement inside a replacement lineage that carries a `LINEAGE_MIGRATION` and derives the same state. `ssdp-shadow-2` is a new genesis, not a migration.
- **Recommended:** (a) a non-breach retirement naming `ssdp-shadow-2` as successor for discovery only, with no binding or claim of equal state (F44). The stakeholder signs one approval, the `LINEAGE_RETIREMENT` record, and the host key signs the published statement (F45). The reading goes to the Manual clarification batch.
- **Alternative:** (b) a retirement naming no successor at all.

SD-64 already decided that `ssdp-shadow` is retired, so the question is only how its successor is named (plan check of bd515e6, note 1). Also asked with it, from review 749b37d N3: a retirement is approved by any registered human, as `KEY_LIFECYCLE` is. On `ssdp-shadow` that human is the stakeholder alone. Should a later ledger name the role that decides a retirement (recommended: no change in Phase F; put it in the Manual clarification batch with F44)?

**Resolved by SD-74 and SD-75 (item 68):** Q-F13 (a), with N3 to the Manual clarification batch; Q-F14 (a), and the G2 workplan's Phase H row is widened.

**Q-F14. Who builds the ref restore (F47) and §5.7's recovery under `INTEGRITY_HALT` (F50).** F47 deferred the ledger's ref restore to Phase H, and revision 22 deferred §5.7's route with it, because that route must move the ref past a corrupt suffix. The G2 workplan's Phase H row is "adversarial, privacy and fault harnesses", whereas this is a Ledger Store mechanism ("replica restore"), and Phase F's row owns §22-§25 (plan check of 43b2e4e, note).
- **Recommended:** (a) an explicit handoff. Phase F discloses both as unbuilt at its exit, and the stakeholder widens Phase H's row to build the `ledger` restore function, with its named extension of fitness B1, before H's fault harnesses exercise it. Phase H's fault harnesses need that restore anyway.
- **Alternative:** (b) build both in Phase F as a further part of step 7, with a ref-moving `ledger` function and the named B1 extension, operator-gated.

Until it is answered, both stay unbuilt and are disclosed: Admission appends nothing under `INTEGRITY_HALT`, and a restore is an operator action outside SSDS.

**Q-F15 (withdrawn by revision 26).** Revision 25 asked how a redesignation could carry a `LEDGER_LOSS`. The check of c36b278e showed that schema 1 expresses it as a loss whose `controls.witnesses` re-establishes the set (F62). 7e-ii builds it, and there is nothing to ask.

**Resolved by SD-77 and SD-78 (item 70):** Q-F17 (a), the in-place correction admitting `{system, version}`; Q-F18 (a), `intake.neutral_auto` deferred to Phase G.

**Q-F17. The system contract id (F66).** An item task's envelope names its item revision, which each bound record copies into `binding.item`. A system-kind task (§13.6: review, acceptance, adjudication and the other system contracts) has a "system contract id" (catalogue line 1419), but the catalogue defines no form, and schema 1's `binding.item` admits only `{unit, rev}`.
- **Recommended:** (a) an in-place schema-1 correction, as SD-69's. `binding.item` also admits `{system: <obligation kind>, version: <system version>}`. §13.6's system contracts come from the system version's table and the policy's parameters. So the contract a system task binds is that kind's entry in that system version, under the ruleset in force at the envelope's `issued_at_position`. `REVALIDATE`'s and `REQUALIFY`'s "the contract of the original record's task" then resolves deterministically (plan check of 5d4a0e2, note 3). No ledger holds a record bound to a system task, so nothing admitted changes.
- **Alternative:** (b) no schema change. A system task's envelope carries `contract_revision: null`, and its records carry no `binding.item`. `REVALIDATE`'s "contract of the original record's task" (§13.6) is then read from the obligation's kind, which the envelope names. This departs from the catalogue's envelope form.

**Q-F18. Mechanical adoption of governance-neutral deltas (`intake.neutral_auto`).** 4c-iv left it "off and unbuilt: it is the Dispatcher's (step 8)". The catalogue's rule is decided (line 1952), but the scope rule for a machinery adoption (lines 1242, 1253) and the authorization of a `MACHINERY` disposition are not defined, and step 10 does not need it.
- **Recommended:** (a) defer it past Phase F, to the phase that builds intake (Phase G), keeping it off and disclosed.
- **Alternative:** (b) define the scope rule and build it in 8g.

**Q-F23. An evidence-requiring claim with no specification (step 9c-i, F87).** Obligations arise only from `EVIDENCES` relations (§10.2). So a subject of a domain whose policy requires evidence, but which no specification evidences, has no evidence obligation and can become valid with no evidence. Lint reports it (`EVIDENCE`).
- **Recommended:** (a) the catalogue's model, the lint finding and the disclosure. Planning closes the gap (§11.3, §13.3), and the lint makes it visible.
- **Alternative:** (b) a stronger rule: such a subject is not valid until a specification evidences it, as an unsatisfiable requirement. This reads more into "evidence obligations per claim kind" than §10.2's identity carries.
- **Effect in Phase F.** Neither option changes Phase F's behaviour on the shadow ledger, whose policy requires no evidence for any domain. The answer bears on fixtures and on a later cutover to `NATIVE` (re-check of abcd03de, note 1).

**Q-F19. Template parameters on `CHECK_EXECUTION` (step 9).** The step 9 row lists "template parameters", but Phase E's E6 gap is `CHECK_EXECUTION`'s: schema 1 gives it only `{template, tool}`. Adding parameters is a schema-1 change, and `CHECK_EXECUTION` targets a candidate, which SD-70 keeps unreachable.
- **Recommended:** (a) defer it with SD-70, to A10's D4, disclosed at the exit.
- **Alternative:** (b) correct schema 1 in place now, as SD-77 did for `binding.item`, though no admitted request could carry one in Phase F.

**Q-F20. The read-observation flag of Phase F's runner class (step 9f-ii).** §17.5's flag says whether the runner observes every read *outside* the realization's tree (reads inside it are the recorded basis and completeness, §6.3, §4.6). Under `bwrap`, the workspace and only the declared environment components are bound, each recorded as an execution attribute, and the network is denied. So no read outside the tree succeeds unrecorded: a read of anything else is denied. A class that declares the flag false makes every real-runner realization unpinnable, so no stop is ever mechanical for it (§6.9).
- **Recommended:** (b) the class declares the flag true by hermetic confinement: every bound path outside the workspace is a declared environment component recorded as an attribute, and every other outside read is denied. This follows §17.5's own advice to run with hermetic home and cache directories. Pseudo-filesystems and devices are outside reads too: `/proc` and `/sys` are not mounted, and what `/dev` exposes, with any host or hardware fact the execution can read, is declared and recorded as an attribute; entropy the runner does not supply (`/dev/urandom`) remains §6.5's disclosed unrecorded variation (re-check of 7a53ad06, note 3). Send the wording, "observes" read as "admits no unrecorded outside read", to the Manual clarification batch.
- **Alternative:** (a) declare the flag false until a read tracer exists, so real-runner realizations stay unpinnable and stops on them are never mechanical. Group 2 runs on fixture realizations either way, and real-runner execution on the real ledger waits for a campaign (F8).

**Q-F21. The numeric oracles' semantics (step 9b).** `ORACLE.ABS_TOL`, `REL_TOL`, `ULP_TOL`, `RANGE` and `MONOTONE` (§6.5) leave open the exact comparison, its edge cases and how it is computed. This is a numerical contract (plan check of 09df7c27, B1).
- **Recommended:** (a) the following, with `x` the observed output and `r` the declared reference.
  1. **Formulas, bounds inclusive.** `ABS_TOL(t)` passes iff `|x − r| ≤ t`. `REL_TOL(t)` passes iff `|x − r| ≤ t·|r|`, relative to the declared reference, not to `max(|x|, |r|)`; with `r = 0` it is exact equality. `ULP_TOL(n)` passes iff the ULP distance is at most `n`.
  2. **ULP distance.** Defined for `float64` outputs only in Phase F: binary64 bit patterns mapped onto an integer line in sign-magnitude order, `+0` and `−0` the same point, distance the difference of the two integers.
  3. **Non-finite values, an explicit override for every tolerance oracle.** A NaN on either side is `FAIL`. Two equal infinities `PASS`, as under `EXACT`. Any other infinity is `FAIL`, so `+∞` is never within `n` ULP of the largest finite value.
  4. **Exact computation.** Each comparison is evaluated exactly on rationals of the stored canonical values (the exact rational of each binary64, or of a canonical decimal), never in binary64 arithmetic. So boundary cases are decided exactly, nothing overflows (`1e308 − (−1e308)`), and verdicts are deterministic.
  5. **Parameter validity.** A tolerance is finite and non-negative, and `n` a non-negative integer; anything else, `ULP_TOL` on a non-`float64` output, or `ULP_TOL` on an output stored as `rounded:<n>` (which is no binary64 value), is a static error of the specification (§17.1), never a runtime `FAIL` (re-check of 7a53ad06, note 2).
  6. **Rounded outputs.** Outputs stored as `rounded:<n>` or `decimal-shortest` are compared as their canonical decimal values, exactly. `decimal-shortest` and `binary64-hex` round-trip a binary64 exactly, so `ULP_TOL` reads the binary64 they denote.
  7. **Declared parameters.** A declared reference or tolerance is read as the exact rational of its decimal text in the declaration (`1e-8` is exactly 10⁻⁸), never as the binary64 nearest to it, so a verdict at the inclusive boundary follows what was written (re-check of 7a53ad06, note 1).
  8. **The other numeric oracles** (revisions 37-38). `RANGE(lo, hi)` passes iff `lo ≤ x ≤ hi`, bounds inclusive and either bound optional; a declared `lo > hi` is a static error; a non-finite `x` fails unless the declared bound on that side is that same infinity, so an overflow never passes an open bound. `MONOTONE(outputs, order)` names a declared ordered list of scalar numeric outputs and passes iff each consecutive pair satisfies `order` (`INCREASING` strict, `NON_DECREASING`, and their duals); equal infinities satisfy `NON_DECREASING` and not `INCREASING`, a NaN fails, and `−0` and `+0` are equal. Both are exact on rationals (items 4 and 7). `SET_EQUAL` needs a collection, which §17.3's canonical forms lack, so it stays unevaluated until a collection form is decided (plan check of db0bf1ce, B1 and answer 4).
- **Alternative:** (b) send the contract to Stage S and leave these oracles unevaluated in Phase F (`yields` fails closed for them).

**Q-F22. Who records that a referenced artifact is unavailable (step 9c-ii).** An `AVAILABILITY` record is an observation targeting a content reference (§3.4): it records binding health, so that an evidence term needing a referenced log, data set or outcome object that has become unavailable is not `T` (§17.4). (Whether a runner of a class is available is the Dispatcher's operational decision, journal state and never a record, §6.9, §10.3.) 9c-ii builds the derivation side. No producer is defined.
- **Recommended:** (a) in Phase F, accept `AVAILABILITY` from a human, and from a designated runner that finds a referenced artifact missing while materializing or executing (9f-ii, under its machinery binding). A periodic binding-health check of `REPO`, `HOME` and `RUNNER` references is deferred to Phase G, disclosed.
- **Alternative:** (b) accept it from a human only in Phase F, deferring every machinery producer.

**Resolved by SD-76 (item 69):** Q-F16 (a). The replacement lineage goes to Phase H, and the G2 workplan's Phase H row is widened.

**Q-F16. Where §24.2's replacement lineage is built (F64).** The G2 workplan places §24's breach protocol in Phase F, and §1 says its replacement lineage, re-encoding and pseudonym mapping run on fixture ledgers. §6's older wording, and revision 28, put it in Phase H without a decision (check of 66ac030b, B1). The rotation branch's `REDACTION_NOTICE` is built in 7g either way.
- **Recommended:** (a) hand the replacement lineage to Phase H with its privacy harnesses: the re-encoding with sensitive fields replaced, the commit identity mapping, the private pseudonym mapping, and `LINEAGE_MIGRATION`'s equal-state qualification. Do this by an extension of SD-75 that widens the G2 Phase H row. Phase F keeps `LINEAGE_MIGRATION`'s field checks and refuses it meanwhile. The confidentiality incident is privacy work, which Phase H's row already names, and no Phase F step needs it.
- **Alternative:** (b) build it in Phase F, as a further part of step 7 on fixture ledgers, as §1 reads.

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

**Narrow re-check of 3ab26030 (revision 13).** No SERIOUS CHALLENGE. **PASS.** The interim element form is within D4 authority only while the repair stores no `id(X)`, a condition now stated in 4c-iv. F1's exception is within SD-69. Its notes are taken up:
- the mode wording (`UNGOVERNED`);
- `QUARANTINE`'s path rule moved to Phase G;
- the adverse-disposition case built on a fixture ledger;
- the element's value defined as `decl(T)[k]` at the absorption.

**Narrow re-check of ad8daeb6 (the 2aadf33 repairs).** No SERIOUS CHALLENGE. B2-B5, B7, B8, N1 and the cost items are verified. NO-PASS on two blockers and a gap, repaired:
- **RB1, the freeze's comparator.** F20's first comparator (raw resolution status) let declaration-caused region changes through: a unit overlapping a frozen subject, an `ignore` over its files, and a stranger nested in it. These were caught at 2aadf331. The freeze now compares the subject on the merged tree under both structures (its shape, region and owned bytes). F20's text is amended.
- **RB2, a scope naming a unit the request creates.** It was refused on the head side.
- **The gap, the outermost owner at unit granularity.** Writing an unowned file needed a scope over every unowned byte in the repository.

For RB2 and the gap, the write-scope rules are lifted into `derivation.writescope`, one frame-level owner that `Conformance` delegates to and 4c-iii's `AUTH_WRITE_SCOPE` will read. It checks both sides, resolves a one-sided unit name to its files, and judges the outermost owner per changed file.

Its notes, taken up:
- N-a: the write set and the revision compare the outermost owner's content in one form (`TreeView.unclassified_owned`, §1.5);
- N-b: tests for a unit with a region on neither side, each reserved-leaf condition alone, and a term ceasing to resolve by declaration.

The repair's own mutants:
- A declaration-only change of the outermost owner (no byte moved) is judged as any unit's.
- A unit with a region on neither side lies within the scope only when the scope names it: its declarations are what changed.
- Equivalent survivors: the reserved-leaf members condition, deleted because only a composite has members and the role condition refuses those; and resolution status in the freeze shape, which the region comparison subsumes.

**Narrow re-check of c5508035.** No SERIOUS CHALLENGE. **PASS.** RB1's three cases, RB2, the granularity gap and N-a are verified by probe, and 11 of 14 mutants are killed. "A region-less unit within when named" is sound under today's schema, since every declaration change writes the manifest. **Step 4c-ii is closed.**

Its notes, taken up:
- N1: the outermost owner's rule is stated as file-granular in `writescope` and 4c-i;
- N2: tests now pin the one-sided widening's precision (M14) and the nested stranger (case 3);
- N3: F20 names the re-partition case;
- N5: 4c-iv re-examines the region-less rule for adoptions.

Kept: M02 (the region in `_held`, near-equivalent) and M12 (`uncovered_outside`'s widening). The latter is reachable only in a ledger with no `ssds.unclassified`, where no frame exists.

**Step 4c-iii built.**
- **Step 2: frame identity.** A record's frame, or a work judgment's or task result's target, must name a transformation that an admitted or co-submitted result fixes (`REF_TRANSFORMATION`). A result fixes `X` when its target `submits` it, `B` is an admitted head and `C` is readable. A result carrying `B` or `C` that does not submit is refused too. A frame record's revisions may also be its frame's (`B`, `C`, `M_n(X)`). A result with a non-empty `adopts` is `SCHEMA_UNSUPPORTED` (4c-iv).
- **Step 3: frame records.** They are judged in their frame. An acceptance names the frame's triple (prospective tenure, `Support` over `frame_state`), and is not effective where the frame does not exist.
- **Integrating requests** (`engine.integration_codes`, one candidate per request). `X` is the transformation an admitted result submits with that candidate; there must be exactly one, unintegrated. On its frame at the head:
  - `STRUCT_MERGE_CONFLICT`;
  - the 4c-ii owner's codes;
  - `AUTH_WRITE_SCOPE` from `derivation.outside_scope`, the submitting result's bound contract, and plan units and unnamed verification rules;
  - `AUTH_PROTECTED` from `derivation.protected_touched`, which the conformance template now also reads, when an agent's envelope binds the request;
  - `ENACTMENT_MISSING` for each subject the structural owner lists as promoted or restored (`StructuralCheck.tenure_starts`) without an acceptance `Support.prospectively_accepted` counts (`binds_tenure`'s conditions 1-4 before admission).
- **Also.** A `renamed_from` whose source had another kind or domain is `SCHEMA_UNSUPPORTED` (F16).
- **Mutants.** Seventeen on 4c-iii, all killed once tests for a failing, a non-current and an other-structure acceptance, and a restoration, were added.
- **Still fail-closed.** Every request ends `SCHEMA_UNSUPPORTED` until steps 5-8. An adopting request withholds salvage (4c-iv). More than one candidate is unsupported.

**Same-family review of step 4c-iii (23b487af).** No SERIOUS CHALLENGE. NO-PASS on three blockers, repaired:
- **B1, salvage of a frame record whose fixing result was refused** (reachable). Salvage now drops any record naming a transformation that no admitted or salvaged result fixes (`REF_TRANSFORMATION`), as it drops dangling record references.
- **B2, `AUTH_PROTECTED` keyed on the request's binding.** It is keyed on the candidate's producer (an agent's actor or lineage). An integrating request must be bound to the producing task (its envelope's task is `X`'s enactment, or the producing human's own binding); any other binding fails closed until steps 7-8. That also settles which binding the write scope reads.
- **B3, a rename launders a promotion or restoration.** `tenure_starts` counts a subject's `renamed_from` lineage; an ordinary rename of a head subject starts nothing.

Its notes, taken up:
- N1: the three fail-closed rules are in §6.
- N2: a review, conformance or task result about a transformation in the admitted frame is refused (§7.5), and fixtures declare the frame they name.
- Cost: frames are built only for the transformations a request names, and `History.former_subjects` folds restorations once.
- 4e's row now owns the integrating trial's reads.

Recorded reading: before integration, only admitted acceptances count for the enactment condition, since the integrating request carries no new judgment (§11.5 (3)). The enactment-equality condition in `prospectively_accepted` is equivalent, kept for clarity: an acceptance made in another enactment's frame does not act in `X`'s frame (§5.2), so it is never current there.

Tests now cover every surviving mutant:
- one candidate under two bases (ambiguous);
- an integrated enactment;
- plan units and unnamed specifications;
- an acceptance of another enactment or another triple;
- two candidates;
- renamed promotions and restorations;
- the refused-result salvage.

**Revision 14: step 4c-iv's detail (reading F21).** Order of work:
1. **The schema-1 correction (SD-69).** Targets, outcomes and the `identity` basis per F21. A `QUARANTINE` carries a `paths` field. `frame` gains optional `base`, `candidate`, `adopts` and `rebases`, present together, which schema 1 checks and which only step 5's rebase reads. Every fixture building intake records on `units` targets is rebuilt.
2. **Derivation.**
   - Each quarantined key's current delta, `(absorption, key)` per F21.
   - The `INTAKE` obligation keyed by it, discharged by a current `ABSORB` naming it.
   - A records-only adoption's frame `X = (B, B, A)`, built from the request's adopted deltas with `A`'s interim element form.
   - The 4c-ii owner classifying an adopted key as authored.
3. **Admission.**
   - An `INTAKE_DISPOSITION` other than `ABSORB` is `SCHEMA_UNSUPPORTED`, and never-lost ones are refused by identity.
   - An adopting `ABSORB` names its key's current delta at the head (F21; else `REF_DELTA`, a delegated `REF_*` member: a delta is no record). One under a standing adverse disposition is refused, tested on a fixture ledger, and so is a superseded delta's.
   - A request's `adopted_deltas` must be exactly the deltas its `ABSORB` dispositions name, each with its value at its absorption (else `REF_ADOPTION`).
   - Only a records-only adoption (`C = B`) is lifted. An adoption with a candidate, and a result with a non-empty `adopts`, stay `SCHEMA_UNSUPPORTED`; otherwise 4c-ii's per-key classification would meet adopted keys that `C` also changes. `INTAKE_CLASSIFICATION` stays `SCHEMA_UNSUPPORTED` (Phase G).
   - The request is judged as the frame record of `X = (B, B, A)`: step 4's codes from the 4c-ii owner, with a promoting or restoring adoption failing closed.
   - The entry it would append carries the adoptions as `ADOPTED` deltas, so `Σ` folds them. That is step 9's commit; until steps 5-8 the request ends `SCHEMA_UNSUPPORTED`, like every other.
   - The write scope does not bind a human's records-only adoption, which carries no contract (re-check c550803 N5). Its authority is the disposition's qualification (§3.5) and §18.4's R2 requirement for a governance-affecting delta. Independence is classified, not required (§8.3 step 3), which is why step 10's repair can be disclosed as non-independent. A machinery adoption (`intake.neutral_auto`, step 8) will need its own scope rule when built.
   - §25.3's protection binds agents, so a human R2 adoption of `ssds.policy`'s declarations is permitted, and `AUTH_PROTECTED` does not apply to it.

**Narrow check of c50eb56c (revision 14).** No SERIOUS CHALLENGE. F21's identity is sound and a function of the ledger alone: a key enters `Q`, or takes a new quarantined value, only at an absorption. NO-PASS on two blockers, repaired in revision 15:
- **B1, a superseded delta's `ABSORB`.** It would enact a later value. An adoption now names the current delta.
- **B2, the classification target.** It departed from SD-69's row. The row is followed literally, classification stays unadmitted, and `paths` is put to the stakeholder as Q-F8.

Taken up:
- the codes `REF_DELTA` and `REF_ADOPTION` replace `REF_RECORD`;
- adoption with a candidate stays unsupported;
- the authority of a records-only adoption is worded as qualification plus §18.4's R2, with independence classified;
- a machinery adoption's scope rule is left to step 8;
- `AUTH_PROTECTED` does not bind a human adoption of policy declarations.

**Narrow re-check of 113f7832 (revision 15).** No SERIOUS CHALLENGE. **PASS.** Its note is taken up: the 4c-iv row carries the current-delta rule, `REF_DELTA`, `REF_ADOPTION`, the unsupported cases and the superseded-delta test.

**Narrow re-check of 88d9a74d (the 4c-iii repairs).** No SERIOUS CHALLENGE. B1, B2, N1, N2, the cost items and the 4e row are verified. NO-PASS on one remaining case of B3, repaired: a `renamed_from` listing a head subject alongside a part still hid a promotion. A head-subject source now contributes nothing and vetoes no other, and a merge-rename test pins it. Its notes are taken up:
- tests for a passing but unsalvaged result (it fixes nothing) and for an agent lineage on a human-recorded result (`AUTH_PROTECTED`);
- §6's rebase sentence split from the list.

E10 is equivalent.

**Step 4c-iv built (after the schema correction, ae002b63).**
- **Derivation.**
  - `State.current_delta(key)` is F21's delta: the absorption that began the current observed value's run, and that value.
  - The structural owner classifies a key a records-only adoption adopts at its observed value as `ADOPTED`, validated as authored. An adopted value that is not the observed delta revalidates, and an adoption with a candidate is `SCHEMA_UNSUPPORTED`.
  - `adoption_codes` judges a records-only adoption: its elements must be exactly the request's `ABSORB` deltas, each current (`REF_ADOPTION`); then the frame `X = (B, B, A)`'s codes; a promotion or restoration is `SCHEMA_UNSUPPORTED`.
- **Admission, at step 2.**
  - `INTAKE_CLASSIFICATION`, non-`ABSORB` dispositions and an `ABSORB` of content are `SCHEMA_UNSUPPORTED`.
  - An `ABSORB` naming a delta that is not the current one, or one under a standing adverse disposition, is `REF_DELTA` (`adoptable`).
  - An adoption with a candidate fails closed.
- **Not yet built.** The entry that carries the adoptions as `ADOPTED` deltas is step 9's commit. Every request still ends `SCHEMA_UNSUPPORTED`.
- **Mutants.** All nine on 4c-iv are killed.

**193b6548: re-check of 4c-iii's RB1 and same-family review of 4c-iv.** No SERIOUS CHALLENGE. **4c-iii: PASS; step 4c-iii is closed.** 4c-iv: NO-PASS on three blockers, repaired:
- **B1, an `ABSORB` refused at step 3 still counted.** Adoption is now judged after step 3, on what passed.
- **B2, `ABSORB`s with no `adopted_deltas` escaped the equality check.** Adoption is judged whenever either side is non-empty, and the candidate rule reads either.
- **B3, a rebase-frame record passed steps 1-3.** It is refused `REF_TRANSFORMATION` at step 2 until step 5, as §6 says.

Its notes:
- N1: an unparsed manifest ends a delta's run uniformly (F21 amended).
- N3: duplicate `adopted_deltas` are `REF_ADOPTION`.
- N4: the element-value guard is tested alone. The structural owner's value check is equivalent, because R4 covers it.
- F12: the `identity` basis's `delta` target is tested.
- N2 is deferred and recorded here. The `INTAKE` obligation stays keyed by its declaration key (`s3`); Admission reads the delta through `State.current_delta`, which requires the key in `Q` and so its derived obligation. Keying the obligation by delta is for Phase G's intake routing.
- The reviewer could not read `~/.ssds`. The author's read through the program (2026-10-25: both ledgers hold only genesis) stands, and is repeated before step 10.

**Narrow re-check of d54a8d7e (the 4c-iv repairs).** No SERIOUS CHALLENGE. **PASS:** B1-B3, N1 and N3 are verified by the earlier probes, and four new mutants are killed. **Step 4c-iv, and with it step 4c, is closed.** On 2026-10-26, after the schema correction, the author re-read both real ledgers through the program (`read_chain`). `ssdp-shadow` and `ssdp-shadow-2` each hold only their genesis entry, read without a halt, so no intake record exists for the correction to make unreadable.

**Revision 16: step 4d's detail (readings F22-F25).** A read-only survey of the catalogue and code found:
- the four non-cycle checks have had codes since SD-68, so the row's fail-closed clause was stale;
- `REASONS` lacked `CYCLE_SUPPORT` and `CYCLE_WARRANT`;
- "own subject" and "consumer" are defined nowhere;
- `CYCLE_WARRANT` has no record-level definition;
- `Support`'s evaluation graph is narrower than §5.6's static graph.

The row is rewritten, with F22-F25 for the four readings. Manual §8.3 step 5 is the shorter text. The catalogue's equivalence, part and re-route clauses refine it consistently, and 4d builds them.

**Plan check of fee4e674 (revision 16).** No SERIOUS CHALLENGE; F22-F25 are sound and fail closed. Reading a structure-changing request in its frame suffices, since a frame's structure is `Σ_{n+1}` (R4). NO-PASS on one small blocker, repaired: a challenge of a `CONTINUITY_ATTESTATION`, which §3.4 permits, would have been `DEP_TARGET_KIND`; it is now `SCHEMA_UNSUPPORTED` until step 7. Its notes are taken up:
- one own-subject set for the §4.3 minimum and `DEP_OWN_SUBJECT`;
- ended-tenure acceptances left out of the static graph;
- F25's warrant ground restated as realized at unit level;
- the evaluation and static graphs named apart;
- §15.2 cited for withdrawing a report.

**Narrow re-check of 87e908dc.** No SERIOUS CHALLENGE. **PASS.** Its wording note is taken up: an unbound prospective acceptance in a pending frame stays in the static graph.

**Step 4d built.**
- **Derivation.**
  - `Judgments.own_subjects` is F22's set: the subjects of `judged_units`. The §4.3 minimum (`Workflow.covers_outputs`) requires content entries only, so it requires nothing `DEP_OWN_SUBJECT` refuses; a `validity` minimum, when built, reads the same set.
  - `StructureFacts.warrant_edges` is §2.4's `E`, the one set `ILLEGAL_CYCLE` and `consumers` read. `consumers(u)` is F23's.
  - `Support.static_deps` and `static_forced` are F24's static graph, over the evaluation graph's node set. `Support.grows_a_cycle(before)` is the one comparison: a non-trivial component that is no subset of one of `before`'s.
- **Admission.**
  - `admission/dependency.py`'s `dependency_codes` gives the per-record codes: `DEP_TARGET_ORDER`, `DEP_TARGET_KIND`, `DEP_COUNTER_CHALLENGE`, `AUTH_ACTOR` for another actor's withdrawal, `DEP_OWN_SUBJECT`, `DEP_CONSUMER`, and `SCHEMA_UNSUPPORTED` for a `CONTINUITY_ATTESTATION` and a challenge of one. They run in authorization's fixed-point loop, so a refusal removes the record before the trial is rebuilt, and never-lost records owe them too. The 4b-ii `ADJUDICATION` clause is gone.
  - `CYCLE_SUPPORT` is request-level, read three ways: the final trial against the head; an integration's frame `D_n[X]` against the head (`integration_codes`); and a records-only adoption's frame (`adoption_codes`).
  - `REASONS` gains `CYCLE_SUPPORT` and `CYCLE_WARRANT`; the latter is never emitted (F25). `dependency` leaves `UNREALIZED_STEPS`.
- **Not reachable yet.** Every request still ends `SCHEMA_UNSUPPORTED`, so no admitted head holds an acceptance: the engine's comparison is exercised only against an acyclic head, and the frame checks re-route nothing through the engine. `grows_a_cycle`, `adoption_codes` and `integration_codes` are tested on derivation histories with cyclic heads and with a part moved between subjects. An integrating request's own records are read in the trial, not the frame; the trial that combines them is 4e's.
- **Tests.** `test_phase_f_step4d.py`: each code at the decision function; the static graph's equivalence, ended-tenure and pending-frame edges; mutual acceptance, an unrelated record beside an existing cycle, growth and a second cycle; a consumer through its subject; an adoption and an integration whose frame closes a cycle; and through the engine, a co-submitted counter-challenge and a mutual-acceptance request (`CYCLE_SUPPORT`). 4b's n3 case is now `DEP_TARGET_ORDER`, and an adjudication of a report is `DEP_TARGET_KIND`.
- **Mutants.** All 22 are killed. Three survived the first run (the consumer's subject expansion and both frame checks) and are killed by the cases added for them.

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

**Same-family review of 2981f738 (step 4d).** No SERIOUS CHALLENGE. **PASS**, with no blockers. The static graph is a superset of the evaluation graph's edges, and the subset comparison has no evasion: a merge of two components, or a node joining one, is flagged. Its notes are taken up:
- N1: the accepted path has no dangling-reference re-check after step 3's fixed point. §8.3 step 9's commit must drop records whose referenced records were dropped; this is placed with Phase F step 6, which builds that commit.
- N2: never-lost frame records are checked in `Σ_n` until 4e (§6).
- N3: a stale-triple gate decision closing a static cycle is now tested, and its mutant is killed.
- N4: `adoption_codes` reuses the head's `Support`. Indexing acceptances, gate decisions and equivalences by subject or unit, and memoizing `binds_tenure`, wait until a real-sized ledger shows the cost (step 10).
- N5: a salvaged never-lost record can close a static cycle (F25).
- F24's item 2 as built is narrower than its text, and fails closed (F24).

**Narrow re-check of 85f7fd7b (the 2981f738 notes).** No SERIOUS CHALLENGE. **PASS:** N1-N5 and the F24 statement are adequately taken up, and the gate-edge mutant is killed. Its wording note on §6 is taken up: a salvaged never-lost record may be a runner observation, not only an adverse record. **Step 4d is closed.**

**Revision 17: step 4e's detail (readings F26-F28).** A read-only survey found:
- the trial is built at the head, so an integrating or adopting request's records are judged in `Σ_n` (§6; review 2981f738 N2);
- `History` already folds an admission's `adopted_deltas`, `integrates` and `admitted_commit`, so the structure-changing trial needs only a trial entry and a tree source;
- `Support.sat` reads a record's frame through `frame_of(rid)`, which a record absent from the head lacks.

4e is split into 4e-i (the trial) and 4e-ii (`STALE_BASIS`), each built and reviewed alone. F26 reads "satisfied" as "not `F`". F27 gives the trial entry. F28 names the checked records. The group 2 discriminators the row named stay at step 9, where §4 already places them, since they need realizations admitted.

**Plan check of 0d92c731 (revision 17).** No SERIOUS CHALLENGE. **PASS**, with no blockers. F26 to F28 hold. Reading any record of a request carrying `X` in `D_n[X]` is required for step 10's adoption, whose dispositions have content entries only under `Σ_{n+1}`. Its notes are taken up:
- F26 cites Manual §5.5 and §10.5;
- the step 6 row registers an integration whenever `integrates` is present, so an empty transformation agrees with its trial;
- the step 4 row and §4's group 2 row place the group 2 discriminators at step 9;
- the 4e row says why `D_n[X]` governs a request carrying `X`.

**Step 4e-i built.**
- **Derivation.**
  - `Frame.entry_deltas` is `Σ_n → Σ_{n+1}` in an entry's form.
  - `trial(..., frame)` adopts those deltas and, for a frame with an enactment (an integration, even an empty one), integrates `X` with `TRIAL_TREE` naming `M_n(X)`.
  - `adoption_frame` builds a records-only adoption's frame, or `None` for malformed elements; `adoption_codes` uses it.
- **Admission.**
  - `integration_frame` is the one place an integrating request's frame is found. `validate` passes that frame, or the adoption's, to every trial of the authorization loop when the frame exists.
  - A structure-changing request's never-lost records are also judged at the head. A rejection salvages from that reading, which replaces their frame refusals (F27).
- **Tests.** `test_phase_f_step4e.py`:
  - an integration's trial equals the state its admission derives (`Σ`, revisions, triples, tenure, the integrated set);
  - an entry's delta sources;
  - an adoption's trial adopts and keeps the tree; malformed adoption elements give no frame;
  - an acceptance is judged against the frame's triple (`AUTH_TARGET_NOT_CURRENT` on the head's);
  - a `validity` entry on a unit `X` moves into the record's subject is `DEP_OWN_SUBJECT`;
  - the engine passes the frame, none when it does not exist or nothing changes;
  - salvage at the head in both directions.
- **Mutants.** All 13 are killed.

**Same-family review of cab6179a (4e-i).** No SERIOUS CHALLENGE. NO-PASS on one blocker, repaired:
- **B1, salvaged frame-`X` records read in `Σ_n`.** The head reading judged a never-lost record declaring `X` by `Σ_n`'s own subjects, though it acts in `X`'s frame. So the 2981f738 N2 gap stayed open through salvage, and the 4e row wrongly called it closed. `dependency_codes` now reads such a record's own subjects and consumers in `X`'s frame (`Support.frame_support`) in either trial. The row and §6 are corrected, and a case pins the head reading.

Its notes are taken up in F27: N1 (the request's own `X` read at `n+1`, equivalent to `k - 1`) and N2 (`AUTHORED` labels).

**Step 4e-ii built.**
- **Derivation.**
  - `Support.sat` takes an explicit frame.
  - `Support.stale_entries(record, frame)` lists the entries whose value is `F` on that support's values. A node absent there counts `F`.
  - `transformation_frame` and `frame_support` expose the frame owners.
- **Admission.**
  - `admission/currency.py`'s `Currency` picks the support and frame per the 4e row, and refuses `STALE_BASIS` (F26-F28).
  - Its codes join each round of the authorization loop, so a record refused at step 6 is removed before the trial is rebuilt, and its step-3 and step-5 codes stand beside it.
  - `STALE_BASIS` joins `REASONS`, and `currency` leaves `UNREALIZED_STEPS`.
- **Consequence.** 4d's engine mutual-acceptance case is now `STALE_BASIS` for both records (§6). The request-level cycle is driven through a trial double.
- **Tests.** `test_phase_f_step4e.py`:
  - a content entry on a superseded revision;
  - an equivalence covering its class (`EXACT` never);
  - a `validity` entry, invalid, valid, under a blocking challenge, then provisional (`P`, satisfied);
  - a `record` entry on a co-submitted record;
  - a `standing` entry on a superseded record;
  - a before-image a concurrent change moved, and one a change elsewhere did not move;
  - an integrated frame's before-image as a fixed fact;
  - a frame a co-submitted result fixes;
  - never-lost, report, challenge and challenge-tier records unchecked;
  - a request carrying `X` reads every record in `D_n[X]`;
  - an empty basis;
  - step 6's code joined with step 5's through the engine.
- **Mutants.** 13 on 4e-ii and B1: 12 are killed. The record first called the 13th, `values.get(node, F)`'s default, equivalent; review 8408e05 B1 showed it is not (below).

**Same-family re-check and review of 8408e055.** No SERIOUS CHALLENGE. **cab6179a B1: PASS.** 4e-ii: NO-PASS on two blockers, repaired:
- **B1, a wrongly equivalent mutant.** A support-tier record may hold a `record` entry on an admitted record that is no node, such as a report. Derivation reads that entry `F`, so the default matters. A case now pins it, and the mutant is killed.
- **B2, the frame cache outlived its fixing result.** One `Currency` serves every round, but it cached `D_n[X]` by `X`'s name. So a frame record survived the round after its co-submitted fixing result was refused. `X` is now resolved from each round's trial before the cache is read, with no fixing result meaning no frame. The cache is keyed on `X` and its enactment, and a two-round case pins it. Keying on the name alone is an equivalent mutant: the per-round check carries the repair. The enactment could change between rounds only in a contrived request with two results submitting one `X` under different tasks, the first refused; it governs which head records of the same enactment act in `X`'s frame (§5.2). The step 6 row now also drops, at commit, every record naming a transformation whose only fixing result was dropped.

Its answers confirm the frame selection, every entry mode on head values, the union of codes within a round, and the non-existent-frame rule.

**Narrow re-check of 2d737acf (the 8408e055 4e-ii blockers).** No SERIOUS CHALLENGE. **PASS:** B1 and B2 are repaired, and the cache probe now gives `STALE_BASIS` in round 2. The name-keyed mutant is accepted as equivalent in practice, with the record's wording corrected: the enactment governs which head records of the same enactment act in `X`'s frame. **Step 4e is closed, and with it step 4 (4a-4e).**

**Revision 18: step 5's detail (§3.2, readings F29-F34, Q-F9).** A read-only survey mapped catalogue §8.3 steps 7-8 and Manual §8.3 against the code. It found:
- most step 7 facts have a derivation owner, for admitted records only;
- `REASONS` lacks every step 7 and 8 code;
- a rejected integration's entry never names `X`, so `Items.refused` cannot route a new iteration;
- `salvageable` still refuses challenges and adverse judgments, though their step 4 checks now exist;
- the decision model has no record-alone refusal, which `CONFORMANCE_RESULT` needs.

Step 5 is split into 5a-5f. ACCEPT stays gated until step 6. The survey's ambiguities are read as F29 (lint, against the Phase E plan's E5 wording), F30 (`outcome_consistent`), F31 (fails closed), F32, F33 and F34. A10's step 7 clauses are Q-F9: SD-66 placed A10's D4 after Phase F, so this is a disclosed difference, not a challenge.

**Plan check of c88c3bbb (revision 18).** No SERIOUS CHALLENGE: E5's wording is a superseded plan sentence, and A10's gap follows SD-66's sequencing. NO-PASS on one blocker, repaired:
- **B1, Q-F9's options.** Option (a) missed integrating requests: clause (f) is part of clean conformance, and the occasion templates feed it too. Option (b)'s "vacuous" premise did not hold. Option (a) now covers every request whose acceptance depends on a task result's conformance. Option (b) is a narrower fail-closed that discloses unchecked occasions.

Its notes are taken up:
- the step 5 row's lint wording now matches F29;
- 5b adds the `standing` entry rule and the mid-task report rule;
- 5a's REJECT `integrates` keeps the entry-shape rule and the fold;
- F31 reads the classification as a refusal under an `OBLIGATION_*` member, by step 6's parallel;
- F30 and F33 record their notes.

**Narrow re-check of 43e85277.** No SERIOUS CHALLENGE. **PASS:** Q-F9's options now cover every request whose acceptance depends on a task result's conformance, and the notes are taken up as stated. Revision 18 stands.

**Step 5a built.**
- **Codes.** `REASONS` gains the step 7-8 codes:
  - the delegated `OBLIGATION_*` members (`NOT_DERIVED`, `RESULT_DUPLICATE`, `DISCHARGED`, `CONTRACT_STALE`, `PREDICATE_UNMET`, `CLAIM_UNSUPPORTED`; F34, Stage S notes);
  - the catalogue's `OBLIGATION_REENACTED`, `OBLIGATION_ANSWERED`, `OBLIGATION_REVIEW_OPEN`, `STALE_RETAINED`, `CONFORMANCE_RESULT`, `NOT_SETTLED`, `REGRESSION` and `HEAD_MOVED`.
- **Decision model.**
  - The record-alone class `CONFORMANCE_RESULT` needs already exists: the engine's `alone` refusals (an ineligible adjudication's), which leave the decision to the rest of the request. 5c reuses it.
  - A REJECT names `X` only on the candidate's merits (F35).
  - `History`'s fold reads `integrates` on ACCEPT only, and the entry shape already admits it on a REJECT.
- **Salvage.** Widened to every never-lost record but a failing assessment and a runner's observation, which wait for step 9.
- **Tests.** `test_phase_f_step5a.py`:
  - the codes are closed members;
  - `on_merits`;
  - a REJECT naming `X` refuses without integrating;
  - the engine names `X` on the merits only: an unbuilt check and a bad binding leave it pending;
  - salvageable kinds, and an adverse judgment salvaged through the engine.

  4d's counter-challenge case now salvages its target challenge. 4a's B1 case now salvages the first adverse review, and step 3 refuses another task's superseding one (`AUTH_SUPERSEDES`), which was plan review b10018de B1's concern.
- **Mutants.** Seven: six are killed. Dropping the `auth.ok` guard is equivalent: an unauthenticated request never reaches step 3's integration checks, so its reasons are never all merit codes. The guard stays as a defence.

**Same-family review of 87b4fa88 (5a).** No SERIOUS CHALLENGE. NO-PASS on one blocker, repaired:
- **B1, F35's merit set judged more than the candidate.** `FREEZE_*` judges the head's state, which lifts when the challenge is resolved. `ENACTMENT_MISSING` judges the review route, which records the acceptance in `X`'s frame. Naming `X` for either ended sound work and restarted it, only to meet the same freeze or redo the acceptance. Both are dropped from the merit set, with a case each.

Its answers confirm:
- the rest of the merit set; mixed reasons (record refusals are not reasons);
- every newly salvaged kind's checks (steps 3 and 5; step 7's refusals apply to passing judgments only);
- `integrates` on a REJECT, which leaves `History`, the trial and the schema unaffected;
- the `auth.ok` guard's equivalence.

N1 places `NOT_SETTLED` for salvaged adverse human decisions with step 6.

**Narrow re-check of 3d125c63.** No SERIOUS CHALLENGE. **PASS:** the freeze and enactment codes are out of the merit set, with a case each, and N1 is placed. **Step 5a is closed.**

**Step 5b-i built** (5b in two halves: 5b-i the obligation checks, 5b-ii the answered and assessment-first checks and Phase E's refusals).
- **Admission.** `admission/legality.py`'s `Legality`, over the head's workflow:
  - Request-level checks, after the authorization loop:
    - `OBLIGATION_NOT_DERIVED`: the envelope's obligation is not derived at the head (F34);
    - `OBLIGATION_CLAIM_UNSUPPORTED`: a task-bound request claims a discharge without its result;
    - `OBLIGATION_RESULT_DUPLICATE`: a second result for one task, at the head or in the request;
    - `OBLIGATION_DISCHARGED`: a claim of an obligation already discharged, which step 2's `REF_OBLIGATION` already catches for subject obligations, which drop out once discharged.
  - Per-record checks, joining each authorization round as step 6's do: a result bound to a discharged obligation (`OBLIGATION_DISCHARGED`), or naming an item revision not current (`OBLIGATION_CONTRACT_STALE`, F36).
  - `authorized` now takes a tuple of per-record checks (`Currency`, `Legality`).
- **Tests.** `test_phase_f_step5b.py`:
  - each code on derivation histories, with the discharge state driven where only item obligations stay indexed;
  - through the engine: a report request claiming a discharge, and a stale contract refusing a result in the loop.
- **Mutants.** 13: all are killed, the loop's wiring by the added engine case.

**Same-family review of fed5d823 (5b-i).** No SERIOUS CHALLENGE. NO-PASS on three blockers, repaired:
- **B1, the duplicate-result check keyed on an unauthenticated field.** `target.task` was never tied to the envelope. Authentication now refuses an envelope-bound result whose `target.task` is not its envelope's task (`AUTH_ENVELOPE`). That also protects `State.submissions`, which takes `X`'s enactment from it. The check keys on the bound task, or on a human's result's target.
- **B2, every integration request refused.** A §11.5 (3) integration request claims without a result, since its producing task's result was admitted earlier. Requests carrying candidates are now exempt from `OBLIGATION_CLAIM_UNSUPPORTED`, with a case.
- **B3, a self-declared contract revision.** `binding.item` was never compared with the envelope's `contract_revision`. So an agent could name the current revision and pass F36, or choose which contract `Conformance` reads, the write scope included. Authentication now requires them equal (`AUTH_ENVELOPE`). An engine case covers a self-declared current revision, an honest stale one (`OBLIGATION_CONTRACT_STALE`) and another task's result.

Its answers confirm `OBLIGATION_NOT_DERIVED` against the derived set, counting only admitted results, the claims rule's envelope scope, and the request reasons' interplay with salvage. Five new mutants are killed.

**Narrow re-check of ccaca714.** No SERIOUS CHALLENGE. **PASS:** B1-B3 are repaired, and the legitimate paths hold (a records-only envelope with no contract revision and no `binding.item`). N1 is placed in step 8's row: an envelope naming a system contract id cannot yet be matched, since the binding schema admits only an item revision. Nothing issues such an envelope before step 8. **Step 5b-i is closed.**

**SD-70 (item 64): Q-F8 (a) and Q-F9 (a).** The stakeholder accepted both recommendations.
- **Q-F8.** Schema 1's `INTAKE_CLASSIFICATION` target is corrected in place to `paths|delta`. `INTAKE_DISPOSITION` keeps `delta|content_ref`. A case pins both, and classification stays unadmitted.
- **Q-F9.** Step 6's row and §6 carry the A10 gate.

**Step 5b-ii built** (5b now in three parts: 5b-iii takes Phase E's deferred refusals, which need a new partition-validity owner in derivation).
- **Admission.** `Legality`'s per-record codes gain two checks for a passing judgment, read in its frame as step 6 locates it (`Currency.locate`):
  - `OBLIGATION_ANSWERED`: the obligation it is bound to is already answered there (`Workflow.answer`, §10.3). A supersession, which step 3 authorized, and a `GATE_DECISION` are exempt.
  - `OBLIGATION_REVIEW_OPEN`: a passing `ACCEPTANCE` or `GATE_DECISION ACCEPT` on a `NATIVE` D1/D2 triple has no `standing` entry on a revision-assessment record for `(s, r)` that counts there (in the run, standing).
- **Derivation.** `passing` is exported.
- **Tests.** In `test_phase_f_step5b.py`:
  - answered and not; a supersession and a gate decision exempt; adverse and non-passing records not refused;
  - an assessment counting, missing, on no assessment, of another revision, not standing (a blocking challenge), and from an earlier run (a revert);
  - a gate decision's triple; a `LEGACY` subject exempt; a D3 subject exempt;
  - through the engine: an adverse acceptance salvaged by a rejection answers the obligation, and a bound passing acceptance afterwards is refused.
- **Mutants.** Nine: all are killed, five by cases added after a first run.

**Same-family review of 82304212 (5b-ii) and ed5af2fe (SD-70).** No SERIOUS CHALLENGE. **PASS**, with no blockers. **Step 5b-ii is closed.** Its answers confirm:
- "answered" as any answer (§10.3);
- `REVIEW_OPEN`'s reading for a prospective acceptance, a co-submitted assessment and each condition;
- SD-70's schema change.

Its notes are taken up:
- N1: `OBLIGATION_ANSWERED` now reads the frame the judgment declares, so an `ADMITTED` record of a request carrying `X` is read at the head, not in `D_n[X]`. That closes a fail-open in principle: an obligation only the head derives, missing from the frame's index. A case pins it.
- N2 is recorded, not applied. The supersession exemption follows the catalogue's words ("a supersession step 3 authorizes … is not refused"). An author superseding their own earlier judgment on the target while another's adverse answer stands is bounded, since that answer still vetoes.
- N3: `paths` targets get a path validator before Phase G admits intake records (§6).
- N4: the frame workflow cache is a real get-or-create.

**Step 5b-iii built.**
- **A pre-existing defect, repaired.** A `COORDINATION_DECISION` names the decision obligations it answers in `target.records` (Phase E reading E31). Obligation identities have a record's form, so step 2 refused every decision answer `REF_RECORD`, and no decision could pass Admission. For this kind only, step 2 no longer reads those names as record references; step 7 checks them instead.
- **Admission.** `Legality` adds, for a `COORDINATION_DECISION`:
  - `OBLIGATION_NOT_DERIVED` when a name is neither an admitted record (catalogue §3.4: "report(s) or item") nor an obligation the head derives, or when its bound obligation is not derived. This refuses answers to a dropped part's decision, or to one never derived (Phase E plan §6).
  - `OBLIGATION_PARTITION_INVALID` for a `PARTITION` whose split fails partition lint for the holder whose decision it answers. It is read in the trial, where its parts object exists (reading E32).
  - The trial's workflow is cached one slot per round, holding the trial itself, so a rebuilt trial is never served stale.
- **Derivation.** `Items.holder_of_decision` and `ItemObligation.valid_partition` expose the owners.
- **Tests.** `test_phase_f_step5b_iii.py`:
  - step 2's reading; a valid partition and an overlapping one; a partition without its parts object;
  - an answer to a decision never derived, and to one already answered; a bound obligation not derived;
  - a non-partition answer not linted; a decision naming an admitted report;
  - each round reading its own trial;
  - through the engine: a decision naming a derived obligation passes step 2, and a stray name is refused.
- **Mutants.** Eight: all are killed, one by a case added after a first run.

**Same-family review of 1fc9ced8 (5b-iii).** No SERIOUS CHALLENGE. NO-PASS on one blocker, repaired:
- **B1, every re-partition refused.** A `PARTITION` re-partitioning a part (§13.7's own example) was judged on the part's holder looked up in the trial, where the part is no longer required and so not found. `Items.holder` now also finds a part a re-partition replaced, rebuilt from the item's partitions. §13.7's example is a case, valid and invalid.

Its notes are taken up:
- N1: a decision may name a co-submitted report, read from the trial. A named record must be a report, per catalogue §3.4's "report(s) or item" (`REF_RECORD` otherwise).
- N2: an authorized supersession may name, or bind to, what the decision it supersedes named, though that decision has since been answered.

**Step 5c built.**
- **Derivation.** `Conformance.result_only` evaluates catalogue §8.3 step 7's three result-only `HARD` templates (F30). `outcome_consistent` counts only `slots_filled`'s unmet obligations, and `citations_support` reads the result's claims. The full templates still run in `hits`.
- **Admission.** `legality.conformance_alone`: when a co-submitted result's result-only templates yield `INCOMPLETE` or `DISCREPANCY`, every passing judgment and principal decision record (`COORDINATION_DECISION`, `MATERIALITY_RECLASSIFICATION`) is refused alone (`CONFORMANCE_RESULT`). The result, adverse judgments and other never-lost records stand. It runs in the authorization loop once a round has no other refusal, so the rest of the request is judged without the records it refused.
- **Reach.** Under SD-70, a request carrying a `TASK_RESULT` is not accepted in Phase F, so 5c decides refusal codes only. Two 4c cases whose co-submitted result names no contract now expect `CONFORMANCE_RESULT` on their frame acceptance. They still fail if a step 3 code appears.
- **Tests.** `test_phase_f_step5c.py`:
  - unmet evidence is not a result-only discrepancy; an empty slot fails, `COMPLETE` and `PARTIAL`; a citation of no record fails;
  - the refusal set; a clean result refuses nothing; no result, no check;
  - an engine case pinning `CONFORMANCE_RESULT` on a passing frame acceptance beside a contract-less result.
- **Mutants.** Ten across 5c and the 5b-iii repairs: all are killed.

**Same-family re-check and review of 1acbb8df.** No SERIOUS CHALLENGE. **5b-iii's B1 repair: PASS**, re-partitions of re-partitions included. N1 and N2 are confirmed against `reports.py`'s own reading. **5c: PASS**, with the loop placement, the alone class and the principal kinds confirmed. Its note is recorded in F30: a human's contract-less result fails closed. **Steps 5b and 5c are closed.**

**Step 5d built.**
- **Admission, an integrating request** (`integration_codes`):
  - `OBLIGATION_REENACTED` replaces 4c-iii's placeholder for an enactment already integrated (SD-26). `OVERTAKEN` and fenced integrations stay step 6's.
  - Binding to anything but the producing task is now `AUTH_ENVELOPE`.
  - The exact candidate's conformance is clean, read the derived way, at the head (F17). `CONFORMANCE_FAILED` covers a violation, a discrepancy other than `outcome_consistent`'s consequence of something unmet, or a result-only failure (F30). Otherwise, if unclean, it is `CONFORMANCE_INCOMPLETE`, which waits and is no merit (F35).
  - `review_codes` reads the current review judgments from the ledger (F32). `STALE_RETAINED` applies when no passing review of `X` judged the content the merged state integrates (`Judgments.supports_integration`, §5.10 (b)), and `OBLIGATION_PREDICATE_UNMET` while `REVIEW(X)` is not discharged.
- **Admission, every request.** A claimed obligation, resolved at the head, must be discharged in the trial after the request's own records, the integration included (`OBLIGATION_PREDICATE_UNMET`). A claim-only request is judged on an empty trial carrying its change. A predicate with an evidence term fails closed until step 9 realizes it.
- **Not built.** Lint is no refusal (F29), and routing is the recorded refusal (F37).
- **Tests.**
  - `test_phase_f_step5d.py`:
    - unrealized evidence waits and a breach condemns; a result-only failure condemns; the merit split;
    - no review, then a current one;
    - five judged-content histories (`STALE_RETAINED` exactly when the review does not support);
    - the predicate read in the trial;
    - a claim-only request through the engine.
  - 4c's integration cases now expect the new codes, and its clean case is made clean with a realization and an independent review.
- **Mutants.** Eleven: all are killed, one by a case added after a first run.

**Same-family review of b546a2b8 (5d).** No SERIOUS CHALLENGE. **PASS**, with no blockers. **Step 5d is closed.** Its answers confirm:
- review discharge read at the head;
- claims in the trial (F10's "values at the head" governs step 6, not step 7's predicate);
- F37;
- `OBLIGATION_REENACTED` and `AUTH_ENVELOPE` against §8.4.

Its notes are taken up in code, to be read again in 5e's review:
- N1: an `INCOMPLETE` that was evaluated (a `DOMAIN` template, a `HARD` check reporting only a signal) is the candidate's own defect, `CONFORMANCE_FAILED`. Only a required execution missing, a runner template not observed, or required evidence unrealized waits. `conformance_codes` is the one place this is decided.
- N2: `STALE_RETAINED` reads only the passing reviews of `X` that act, unsuperseded, in `X`'s frame, where a frame review's supersession acts. A superseded supporting review no longer masks a current one. Removing the acting filter is an equivalent mutant: a passing review of `X` always declares frame `X` (4c-iii's N2), so it acts there.

**SD-71 (item 65): Q-F10 (a).** Steps 5e and 5f are deferred to the phase that lifts SD-70's gate for integrations. Their fail-closed rules stay in §6, and they are disclosed at the exit. **Step 5 is closed for Phase F**: 5a-5d, with 5e and 5f deferred.

**Revision 19: step 6 in parts (§3.3, readings F38-F42, Q-F11).** A read-only survey of catalogue §8.3 step 9, §8.6 and §21-§23 against the code found the gaps §3.3 lists. Step 6 is split into 6a-6g, the records-only commit path first; the publication effect's writing side is deferred (6g). The survey's ambiguities are read as F38-F41. Its possible challenge to SD-71's premise is F42's fail-closed rule, put to the stakeholder as Q-F11. It is not a SERIOUS CHALLENGE: the rule is vacuous on the shadow ledger, and failing closed keeps SD-71's intent.

**Plan check of 97d98240 (revision 19).** No SERIOUS CHALLENGE: Q-F11 is correctly information, since F42 fails closed and SD-71's deferral stands. NO-PASS on two blockers, repaired:
- **B1, F41 caught challenges and reports.** It is limited to decision kinds tied to the fence's attention. A never-lost adverse decision is admitted, per step 7's own never-lost sentence, and the tension is a Stage S note.
- **B2, F42's predicate was narrower than step 8.** It now reads the adoption's effect-keyed write set, which includes units whose bytes move to a newly declared unit.

Its notes are taken up:
- N1: absorptions pass 6b's commit point, and nothing appends on the real ledger before 6b;
- N2: an adoption never carries `integrates`;
- N3: the incarnation identity is built, and only the publisher's attempted set is deferred;
- N4: group 4's discriminators are placed.

**Narrow re-check of 112d2a40.** No SERIOUS CHALLENGE. **PASS:** B1, B2 and notes 1-4 are closed as stated. Its sync note is taken up: 6c's row reads F42's "a unit in its write set". Revision 19 stands.

**Step 6a built.**
- **Admission.**
  - `expected_head` folds absorptions as `History` does: the observed head, or the fence commit.
  - `Admission` takes the observed product repository its composition root supplies (`product`). When `obs` is not the expected head, it appends an absorption of `obs`, its commits imported and kept reachable from the ledger ref, then revalidates the request at the new head (§8.3 step 9, §8.6).
  - It halts and appends nothing in three cases: with no product repository; when `obs` is no commit there; and when the head entry is an admission with a pending publication effect (F39).
  - A lifecycle admission still halts on a moved head: its human approval names the head it was signed for.
- **Not yet built.** The absorption's commit point is 6b's. Until then it is appended and checkpointed as admissions are today, and nothing appends on the real ledger (plan check N1).
- **Tests.** `test_phase_f_step6a.py`:
  - a moved head absorbed, then the request revalidated (two entries, the request at the new head, derivation folding the same head, `obs` reachable from the ledger ref);
  - no product repository, and an observed head that is no commit, each halting with nothing appended;
  - an unmoved head appending no absorption;
  - a pending effect not absorbed;
  - `expected_head` over genesis, absorptions, a fence and a rejection.
- **Mutants.** Seven: six are killed. Removing the explicit no-product check is equivalent: the import then fails and still halts with nothing appended.

**Same-family review of c06f5be5 (6a) and d34a432e (5d's notes).** No SERIOUS CHALLENGE. **PASS**, with no blockers. **Step 6a is closed**, and 5d's notes are confirmed repaired. Its answers confirm:
- the absorb-then-revalidate order, with `base_position` undisturbed;
- F39's predicate: a pending effect exists only at the head entry;
- not checking ancestry (§8.6 absorbs any movement; 6c and 6d classify it);
- the entry shape and the fold.

Its notes:
- N1, taken up: `obs` is validated as a commit identity before any Git call, so an option-shaped value never reaches Git (Manual §25.4). A case pins it.
- N3, taken up: the conformance hits that wait on an execution or a runner are tagged where conformance makes them (`Hit.waits`), not matched by wording.
- N2, placed with 6b: a lifecycle admission still halts on a moved head. 6b either gives it the same absorb-then-proceed path or records why its human approval pins the head.

**SD-72 (item 66): Q-F11 (a).** F42's fail-closed rule for adoptions is SD-71's complement.

**Step 6b built.**
- **Admission** (`engine.py`, the commit point):
  - `witness_set` reads the genesis witness model: each `FILE` witness at its location, with any other kind answering nothing (F3).
  - `qualification` runs `qualify` with the retained high-water mark.
  - `held_head` runs before every decision and every lifecycle admission, and halts unless the ledger is `QUALIFIED` with no provisional entry (§23.4). A provisional entry this host appended first has its checkpoint distribution completed, rebuilt from its deterministic signature (§22.4 crash recovery). A request it decided is then found by its identity. Another host's provisional entry halts. The high-water mark is raised to the held head.
  - `commit` appends by the compare-and-swap, distributes the checkpoint, and returns only once a quorum holds the entry, raising the high-water mark. Otherwise it halts, leaving the entry provisional for the next start.
  - A lost compare-and-swap re-reads and revalidates, up to three times before halting (§21.3).
  - Absorptions, admissions and lifecycle entries all pass `commit`.
  - A lifecycle admission still halts on a moved head: its human approval names the ledger head it was signed after, which an absorption would move (review c06f5be N2).
- **Tests.** `test_phase_f_step6b.py`:
  - the high-water mark raised by a decision;
  - an unwitnessed head halting with nothing appended;
  - a rewind as `ROLLBACK` (441cf5c N7);
  - a crash before the checkpoint recovered by request identity, the head held and retained (8a75346 N2, ledger form);
  - a lost compare-and-swap revalidated once; a ledger that keeps moving halting;
  - another host's provisional entry not redistributed;
  - a high-water mark beyond the ledger as `ROLLBACK`.
- **Mutants.** Nine: all are killed, one by an assertion added after a first run.

**Same-family review of e78d0cf7 (6b).** No SERIOUS CHALLENGE. **PASS**, with minor notes. **Step 6b is closed.** Its answers confirm:
- the recovery-before-identity order;
- the authoritative qualification (`ROLLBACK`, not `BEHIND`);
- the high-water mark only at a held head, with abandoned entries ignored;
- the retry loop: no double append, and an absorption that won is seen at the head;
- tolerating a failed witness write, since the quorum decides and a conflicting checkpoint surfaces as `FORK`;
- recovery under a rotated key halting, fail-closed.

Its notes are taken up: N1, the halt message names "another host key", not another host; N2, `distribute` reuses the chain already read.

**Step 6c built.**
- **Admission.** The final fail-closed rule becomes `gated`. A request passing every built check is accepted, except:
  - a request carrying a `TASK_RESULT` or candidates, or claiming an item obligation, whose discharge reads conformance (SD-70, SD-71);
  - one carrying a runner's evidence or an evidence assessment (step 9);
  - an adoption while any realization is admitted, a stricter form of SD-72's rule (F42) until step 8.
- **Commit.**
  - On ACCEPT, step 9's drop cascade (`cascade`, shared with salvage) refuses what names a dropped record or transformation, and the request is then rejected and salvaged (F40).
  - An accepted adoption's entry carries its frame's `ADOPTED` deltas and never `integrates`.
  - `UNREALIZED_STEPS` is `("regression",)`.
- **Consequence.** Records-only requests are now accepted. Five earlier cases that expected a fail-closed rejection now expect acceptance.
- **Tests.** `test_phase_f_step6c.py`:
  - a records-only request accepted and derived;
  - a `TASK_RESULT` not yet accepted;
  - a dropped reference rejecting the request;
  - **step 10's repair rehearsed end to end**: a foreign declaration change absorbed, then adopted by a human `ABSORB` with `adopted_deltas`, accepted with the `ADOPTED` delta and no integration, `Σ` updated and the key no longer quarantined;
  - the gate, case by case; an adoption waiting while a realization is admitted.
- **Mutants.** Nine: all are killed.

**Same-family review of c80fc6ad (6c).** No SERIOUS CHALLENGE. NO-PASS on one blocker, repaired:
- **B1, records on targets never checked were accepted.** Before 6c every request ended `SCHEMA_UNSUPPORTED`, which hid two gaps:
  - step 3's acceptance-target rules ran only for `ACCEPTANCE`;
  - step 2 checked record references and basis revisions, but not a record's own target.

  A probe accepted a `LEGACY_ACCEPTANCE` on a part or on a missing subject, and an `EQUIVALENCE`, a `RECONSTRUCTION_PROPOSAL` and an `EXTERNAL_ACCEPTANCE` on missing targets. The repairs:
  - Step 2 checks that a record's target exists (`REF_TARGET`, a new `REF_*` member and a Stage S note; Manual §8.3 step 2): its units (`units`, `unit`, `scope`) are declared at the head, and its `(unit, revision)` pairs (a triple, a gate decision's triple, an item or spec revision) are known revisions. It applies to `ADMITTED` records, since a frame record's target is its frame's. An acceptance's triple stays with step 3's codes (SD-68).
  - Step 3 applies the acceptance-target rules to `LEGACY_ACCEPTANCE`, which "supplies the acceptance for that (subject, scope_id, rev)" (§19.2). A legacy import on a subject not `LEGACY` is `AUTH_VERSION`.
  - `EXTERNAL_ACCEPTANCE`, whose external target has no checker, is gated.

  The probe's cases are tests, and six mutants are killed.

Its answers confirm the rest of the gate, the trial and committed entries agreeing, the cascade, and the adoption path. Its note N1 is answered by Phase E's E31: a records-only `AMEND` with no plan change in the same request is settled at once.

**Narrow re-check of c9c937d6 (6c's B1 repair).** No SERIOUS CHALLENGE. NO-PASS: the repair closed the probe's cases, but other shapes still reached ACCEPT:
- a `HUMAN_DECISION` on an obligation no one derives;
- an `EQUIVALENCE` with made-up `from` and `to`;
- observation kinds recorded by a human (`EXTERNAL_CONSULTATION`, `ANALYZER_OUTPUT`, `AVAILABILITY`, `CUSTODY_ENUMERATION`);
- inconclusively, an `integrated` `REVIEW` and a `GATE_DECISION`'s gate and core.

Repaired by turning the gate into an allowlist, so nothing unchecked can reach ACCEPT. Phase F accepts only these kinds, each in target shapes whose every reference a built check verifies (`engine._ACCEPTED`):
- reports, on units or records;
- `CHALLENGE`, on a record or a triple;
- `ADJUDICATION`, `WITHDRAWAL`, `NON_AUTHORSHIP_ATTESTATION` and `MATERIALITY_RECLASSIFICATION`, on a record;
- `COORDINATION_DECISION`, on records or units;
- `ACCEPTANCE`, `LEGACY_ACCEPTANCE` and `REVIEW`, on a triple;
- `EQUIVALENCE`;
- an `ABSORB` of a delta.

Everything else fails closed until its checks exist. That includes a risk override, whose continuation names subjects and items in its fields. `REF_TARGET` now also reads an equivalence's `from` and `to` and a challenge's `locus`. Cases cover each reported shape, and five mutants are killed.

**Narrow re-check of 4263380e (the allowlist).** No SERIOUS CHALLENGE. The allowlist design is confirmed: every allowlisted kind and shape was traced field by field. NO-PASS on one small blocker, repaired:
- **B1, a challenge's or review's triple was checked without its `scope_id`.** A blocking challenge recorded in advance on a triple that never existed would bind it once a later rescoping produced it. `REF_TARGET` now checks the whole `(subject, scope_id, rev)` against every triple an admitted position held. An acceptance's triple stays with step 3.

Its notes:
- a materiality reclassification must name a report or a challenge (§15.2; `REF_TARGET`), taken up;
- a `COORDINATION_DECISION`'s `fields.tasks` and an `EQUIVALENCE`'s `class` are inert, read by no derivation (an unknown class covers nothing), and left as Stage S notes on closed vocabularies.

Cases pin both repairs, and two mutants are killed.

**Narrow re-check of ab0b790d.** No SERIOUS CHALLENGE. **PASS:** triples are checked whole, past triples stay targetable (§1.6, §19.4), and acceptances stay with step 3. **Step 6c is closed.** Its notes:
- N1, taken up: a reclassification's kind check also reads a co-submitted target;
- N2, recorded with step 10's cost items: `revisions` and the new triple set walk every admitted position each request. On a long ledger, fold both once per `History`, as `former_subjects` is.

**Step 6d built.**
- **Content.** `ancestry(repo)` is a commit-graph reader (`git merge-base --is-ancestor`). It validates both commits before any Git call, and a commit the repository lacks reaches nothing.
- **Derivation.**
  - `History` and `derive`/`consequences` take an optional `ancestry`.
  - `derivation/publication.py`'s `Publication` gives:
    - `classes`: `pub(n)` of every accepted admission, `PENDING`, `PUBLISHED`, `OVERTAKEN`, or `UNKNOWN` without the graph;
    - `late`: an `OVERTAKEN` admission whose `C_n` a later `obs` newly reaches;
    - `violations`: entries breaking §22.1's entry-shape rule, with "`E` becomes `obs`" honoured for an equivalent publication.
  - `s3` raises `LATE_PUBLICATION` and `ENTRY_SHAPE` as `CRITICAL` integrity findings (F43).
- **Not yet wired.** Admission's decisions read no publication class. The composition root that supplies `ancestry` is step 10's.
- **Deferred.** The extended head through checkpoint resume is a cost item, with step 10's.
- **Tests.** `test_phase_f_step6d.py`. Group 4's S5 §22 `publication_classification` rows:
  - `PENDING`, including past an entry with no `obs`;
  - `PUBLISHED`, by `obs = C_n` and by a descendant;
  - `OVERTAKEN` on a rewrite; `UNKNOWN` without the graph.

  Also:
  - integrations: an equivalent publication `PUBLISHED`; the same tree off the base, and a descendant with another tree, `OVERTAKEN`;
  - 730490d N2's records-only form: `OVERTAKEN`, then `LATE_PUBLICATION`;
  - the entry shape: a stray admission corrupt; an absorption with a moved `obs` and an equivalent publication kept; strict without the graph;
  - the real-Git ancestry reader.
- **Mutants.** Ten: eight are killed. Two are equivalent:
  - starting the late scan at the overtaking entry, whose `obs` never reaches `C_n`;
  - removing the ancestry reader's own validation, since Git rejects an option-shaped commit anyway (the validation stays as a defence).

**Same-family review of 0ab46e4b (6d).** No SERIOUS CHALLENGE. **PASS**, with notes. **Step 6d is closed.** Its answers confirm:
- F43's approximation (a false `LATE_PUBLICATION` needs a contrived history);
- the expected head and every entry kind's `obs`;
- a finding rather than a halt;
- the Git reader's validation.

Its notes:
- N2, taken up: "`E` becomes `obs`" excuses an equivalent publication only of the admission that set `E`, the last entry that moved the head. It no longer excuses one of an older admission whose `C` a later absorption returned to.
- N4, taken up: the ancestry reader returns unknown, not `False`, when Git cannot answer (a missing object, a corrupt repository), so an unreadable graph gives `UNKNOWN`, never `OVERTAKEN` or a false `LATE_PUBLICATION`.
- N1 and N3, placed in step 10's row: wire `ancestry` into the composition root or report publication as `UNKNOWN`, and expect `LATE_PUBLICATION` after a force-push rewind and advance.

Cases pin N2 and N4.

**Step 6e built.**
- **Derivation.** `History` registers an integration whenever an accepted admission carries `integrates`, or when the head moves. An empty transformation (`C = B`) therefore agrees with its trial (plan check of 0d92c731). A rejection naming `X` integrates nothing (F35), and an adoption never carries `integrates` (6c).
- **No version change.** No ledger holds an accepted entry carrying `integrates`, since integrations are not accepted in Phase F. Existing histories derive as before, so `DERIVATION_VERSION` is unchanged.
- **Tests.** `test_phase_f_step6e.py`:
  - an empty integration registered, agreeing with its trial;
  - a rejection naming `X`;
  - an admission with neither;
  - the checkpoint round trip.

  The full suite is the fixture regression.
- **Mutants.** One: killed.

**Same-family review of 04012289 (6e) and fa5ce639 (6d's notes).** No SERIOUS CHALLENGE. **PASS.** Every fixture writing an accepted `integrates` already moved the head, and keeping `DERIVATION_VERSION` is sound. 6d's N2 and N4 are confirmed. **Step 6e is closed.**

**SD-73 (item 67): Q-F12 (a).** Step 6f is deferred with 6g, 5e and 5f. **Step 6 is closed for Phase F**: 6a-6e built, 6f and 6g deferred and disclosed.

**Revision 20: step 7 in parts (§3.4, readings F44-F48, Q-F13).** A read-only survey of catalogue §22.1, §23-§24 and §25.2 against the code found the gaps §3.4 lists. Step 7 is split into 7a-7g, with retirement first because step 10 and SD-64 need it. Its possible challenge is §24.2 defining retirement only inside a migration. It is read as F44 and put to the stakeholder as Q-F13, not raised as a SERIOUS CHALLENGE: SD-61 and SD-64 already chose the new genesis, and the reading only names it.

**Plan check of bd515e60 (revision 20).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Its answers:
- F44 is a defensible D4 reading. §23.4 defines `RETIRED` generically, §22.1 lists `LINEAGE_RETIREMENT` among the recovery entries, and SD-64 already decided the retirement.
- F45 is faithful, a host-key statement anchored in the human-approved chain entry.
- 7a's gate, F46-F48 and the ordering are right.

Its notes are taken up:
- Q-F13's option (c) is dropped, since it would reverse SD-64.
- F47 names its deferred `ledger` function and its phase.
- Each §23.8 row is placed.
- F45 says where a chainless verifier gets its trust roots.
- The status line is current.

**Step 7a built (retirement; §3.4, readings F44, F45, F49).**
- **Statement.** The catalogue's form: `{ledger_id, kind: RETIREMENT, last_position, last_entry_digest, successor_ledger_id, successor_genesis_digest, signatures}`. Its `signatures` hold one host-key signature, under the statement's own domain `ssds.retirement.v1`. The reading side is in the Ledger Store's `qualification` API, which is the only ledger API the Interface may import (fitness F11, Manual §26.2):
  - `RetirementStatement`;
  - `FileWitness.statement`;
  - `retirement_verified`, `retirement_statements` and `retirement_held`.

  Signing and writing are in its `append` API, which only Admission imports: `retirement_statement` and `write_retirement`. The statement is written through `retain`, the fsynced append-only write that `write_checkpoint` now shares.
  - **Reading.** `FileWitness.statement` takes only a closed-shape regular file. A bare marker, an extra field or a link is no statement.
  - **Verification.** It needs a signature by a host key of the trust roots and `last_position` at least 1. Where the chain holds `last_position`, the chain's `LINEAGE_RETIREMENT` must be there with that digest. A participant behind the retirement, or one with no chain, verifies by its trust roots alone.
  - **`RETIRED`.** It needs `q_a` declared witnesses holding a verified statement.
- **Readers.** Admission's qualification, the CLI's `HomeAccess` and the Interface's `present` compute `RETIRED` from verified statements. `FileWitness.retired`, the bare-marker test, is removed. `LedgerAccess.witness_reports` now returns each witness's statement instead of a flag.
- **Admission.** `admit_lifecycle` admits `KEY_LIFECYCLE` as before and `LINEAGE_RETIREMENT`; every other lifecycle kind is `EntryInvalid` until 7b-7g. A retirement:
  - carries `obs = null`, and any other `obs` is refused;
  - is admitted only at the held head (`QUALIFIED`, any own provisional entry completed first, §24.2's settled head);
  - passes the trial: at least `q_a` witnesses this host can write. This cannot prove that the write will succeed; one that fails leaves a provisional entry, recovered as in 6b;
  - is approved by a registered human over the ledger, position, head and record identity (§25.2's gate, as `KEY_LIFECYCLE`);
  - has a closed successor `{ledger_id, genesis_digest}`, another ledger (F44).

  After the commit, Admission publishes the statement and halts until `q_a` witnesses hold it. `held_head` halts on any held `LINEAGE_RETIREMENT`; when it is the head, it first completes the statement's publication, the crash recovery of a statement as of a checkpoint. Nothing is appended after it.
- **The successor's genesis digest** is its genesis entry's digest (position 0), which a reader checks against the successor's authenticated chain. It is not the approval digest `prepare` printed.
- **Operator script** `orchestrator/scripts/retire_shadow.py`. `prepare` builds the record (the genesis record's ruleset and `governs`), reads the successor's genesis digest from its own chain in the SSDS home, and writes the record and approval message to the ledger's workspace (two new workspace names). The stakeholder signs. `admit` admits it with `obs = null` and reports `RETIRED`. An entry admitted between the two moves the head the approval names, and `admit` refuses it.
- **Tests.** `test_phase_f_step7a.py`, 16 tests:
  - admission, publication and `RETIRED`;
  - nothing appended after;
  - `obs`, the successor's closed shape and the approver;
  - other recovery kinds refused;
  - an unqualified ledger; the trial, with a witness readable but not writable;
  - a crash before the statement, completed at the next start;
  - a retirement that is not last halts and publishes nothing;
  - the verifier's cases; the closed file; a witness holding another statement;
  - the Interface reading `RETIRED`.

  `test_shadow_genesis_script.py`: the bare marker now presents `QUALIFIED`, a stranger's statement too, and a host-signed one `RETIRED`; the operator script end to end on fixture ledgers `demo` and `demo-2`, the repository only read.
- **Mutants.** All 27 are killed:
  - Admission, ten: the retirement read, the halt after a retirement, publication only at the head, `obs`, the trial, publication after commit, the kind gate, the successor check, the quorum on publication, and writability;
  - the statement, eleven: authenticity, ledger, kind, position 0, a behind chain, digest, kind at the position, `q_a`, closed shape, link, and a boolean position;
  - the successor shape, five;
  - the Interface, one.

  R02-R05 ran before the move into `qualification`; their code is unchanged.
- **Fitness.** The first full run failed F11: a new `ledger.retirement` module is no public ledger API. The move into `qualification` and `append` repairs it, with the fitness table unchanged. The full suite then passes: 1316 tests, 6 skipped.
- **Not run on the real ledger.** Retiring `ssdp-shadow` needs the stakeholder's signature, and Q-F13 first.

**Same-family review of 749b37d3 (7a).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Its answers:
- A participant behind the retirement reads `RETIRED` by the trust roots alone, as §23.4's "from any mirror" and the stale-mirror drill require.
- The writable-witness trial is an adequate stand-in for a trial qualification. The commit's re-qualification decides, so nothing is reported early.
- F49 is faithful.
- The successor's genesis entry digest is the right identity.
- §22.1, §23.4, §24.2's settled head and §25.2's gate are met.

Its notes:
- **N2 (taken up).** `retirement_held` counted verified statements without requiring them to be the same statement, so distinct statements could add up to `q_a` for a chainless participant. It now needs `q_a` witnesses holding one identical statement. A test is added; mutant R12 (count across distinct statements) is killed, and R08's anchor is replaced by it. The SSDS suite passes, 923 tests with 6 skipped.
- **N2's conflict signal (disclosed, to 7b).** Two different authentic statements for one ledger mean that a host key signed conflicting retirements, like two checkpoints at one position. Today each witness holding another statement counts as holding nothing, and no quorum forms; nothing is reported current wrongly. Raising it as an integrity state belongs with 7b's recovery skeleton, which generalizes `FORK` and the critical flag.
- **N1 (recorded).** Statements are verified against the genesis `admission_keys`, as checkpoints are. No path yet retires or compromises an Admission host key: `KEY_LIFECYCLE` refuses that role. The genesis keys are therefore exactly the keys in force. Folding host-key lifecycle into retirement and checkpoint verification, and excluding compromised keys, belongs to the step that builds host-key rotation.
- **N3 (put to the stakeholder with Q-F13).** Any registered human may approve the retirement, as for `KEY_LIFECYCLE`. The ledger has one registered human, the stakeholder, so this is the stakeholder's approval. Whether a later ledger should name the deciding role is asked with Q-F13.

**Step 7a is closed.** 7b (the recovery skeleton) is next.

**Revision 21: step 7b in detail (§3.4, readings F50-F53).** 7b builds the recovery gate and its table (F50), the trial qualification before every recovery append (F51), and fixture witnesses for `TEAM` and `HARDENED` (F53). It admits no new kind: 7c-7e each supply their content check. The witness model in force per position moves to 7e (F52), since only a redesignation can change it.

**Plan check of 31b3ed34 (revision 21).** No SERIOUS CHALLENGE. **NO PASS**, on three gaps in F50's table:
- **B1.** A proved-never-admitted loss reads `ROLLBACK`, not `FORK`, yet §23.6 resolves it by a `FORK_RESOLUTION` with no boundary.
- **B2.** §5.7's route under `INTEGRITY_HALT` was closed without a stated deferral.
- **B3.** A routine redesignation at a settled head was refused.

F51-F53 are judged faithful. Notes 1-5 ask for:
- the compare-and-swap when the ref is not at `A`;
- the redesignation's trial placed in 7e;
- a guard that the composition root never passes the fixture map, and a denying fixture witness;
- approval replay and the new gate cases as tests.

**Revision 22 repairs them.**
- **B1.** `FORK_RESOLUTION` is admissible under `FORK` or `ROLLBACK`.
- **B2.** §5.7's route needs the ref moved past a corrupt suffix, which is F47's restore. It is deferred with that restore to Phase H, and §6 discloses it.
- **B3.** A redesignation is admissible at a settled `QUALIFIED` head, through the held head.
- **Notes.** F50 states that the compare-and-swap is from `A`'s commit and is refused when the ref is elsewhere. F51 places the redesignation's trial in 7e. F53 takes a file-witness object, for a denying witness. 7b's tests add every case the notes name.

**Re-check of 43b2e4e5 (revision 22).** No SERIOUS CHALLENGE. **PASS**: B1-B3 are closed and the notes taken up. Its one note says that F47's ref restore, and §5.7's route with it, has no owner in the G2 workplan's Phase H row, which covers harnesses only. It goes to the stakeholder as **Q-F14** (§7), and Q-F13 now also carries review 749b37d N3.

**Step 7b built (the recovery gate; readings F50-F53).**
- **The gate.** `admit_lifecycle` takes `KEY_LIFECYCLE` and every recovery-tier kind; any other kind is `EntryInvalid` before any state is read.
  - **`obs`.** A recovery record carries `obs = null`.
  - **Settling first.** Admission first completes its own provisional entry (6b's recovery), then reads the qualification.
  - **State.** The kind must be admissible in that state (`RECOVERY_STATES`, `admissible`). A settled `QUALIFIED` head goes through the held head, which raises the mark and halts a retired ledger, completing a retirement's statement. Any other recovery entry follows the replica's last readable entry.
  - **Content.** The approval is checked as before. Each kind's content check is `_content_problems`: `LEDGER_LOSS`, `FORK_RESOLUTION` and `WITNESS_SET_REDESIGNATION` are refused there, naming 7c, 7d and 7e, and `REPLICA_REDESIGNATION` is refused at the gate (7g).
- **The trial.** `Admission.trial_qualification` seals the entry with `ledger.append.seal`, now public and shared with `append_entry`. It extends the chain and qualifies it, with the entry's checkpoint added at every witness this host can write. Every recovery append, the retirement included, needs it `QUALIFIED` at the new position with no provisional entry. It replaces 7a's writable-witness count. `publish_retirement` now asks the qualification itself for `RETIRED`.
- **Fixture witnesses.** `Admission.fixture_witnesses` maps a declared non-`FILE` witness id to a directory or a `FileWitness` object. Statements are read through the same witness set, so a fixture witness holds them too.
- **Tests.** `test_phase_f_step7b.py`, 17 tests:
  - the gate table, kind by state, including `BEHIND`, `RETIRED`, `INTEGRITY_HALT` and kinds outside the path;
  - the guard that only `admission/engine.py` mentions the fixture map;
  - a qualified ledger refusing a loss, a fork resolution and a replica redesignation;
  - under `ROLLBACK`, a loss and a fork resolution passing the gate to their unbuilt checks (B1), and a redesignation refused;
  - a redesignation at a settled head reaching its check (B3);
  - nothing under `INTEGRITY_HALT` (B2);
  - `obs`; an approval for another position or head digest; an approval replayed from an earlier head;
  - an own provisional entry completed before the gate;
  - an unpublished retirement halting every recovery kind;
  - the trial under `TEAM` with one witness unwritable (held) and two unwritable (refused);
  - the trial under `HARDENED` with one witness unreachable (held), and with one unreachable and one denying (refused);
  - a trial appending nothing.

  7a's loss test now expects the gate's refusal.
- **Not testable in 7b.** The compare-and-swap refused when the ref is not at `A` (note 1) needs a recovery kind that passes its content check, so it moves to 7c's tests.
- **Mutants.** Thirteen: twelve are killed. G05, the trial's head-position clause, is equivalent: a trial `QUALIFIED` below the new position always has the new entry provisional. G13, a kind outside the path reaching the state read, survived at first and is killed by the added test.
- **Full suite.** It passes: 1332 tests, 6 skipped (run before G13's test was added; that test then ran alone and passes).

**Same-family review of 7d2d1c00 (7b).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Its answers:
- The gate and the trial are faithful to F50 and F51.
- The placeholder commit is inert, since `qualify` matches by position and digest.
- The entry's abandonment enters `_abandoned` only once the trial holds it.
- A conflicting checkpoint at the new position makes the trial `FORK`, which refuses conservatively.
- Settling an own provisional entry first is right.
- The fixture boundary holds.
- G05 is equivalent.

Its notes:
- **N1 (to 7e).** `distribute` halts over another host's provisional entry. §22.4's one exception, a `WITNESS_SET_REDESIGNATION` appended over a provisional entry, must not be stopped by it, so 7e's redesignation path tolerates that halt.
- **N2 (to 7c).** An append when the ref points past the readable prefix is refused by the compare-and-swap. Note 1 of the plan check already moved that test to 7c, the first part whose kind reaches the commit.

**Step 7b is closed.**

**Revision 23: step 7c in detail (§3.4, readings F54-F57).** A survey found that derivation already folds a loss's boundary, `cont` and `REQUALIFY`, and that qualification reads its abandoned digests. 7c is therefore Admission's content check, and `prepare_loss` computes the fields the human signs:
- the retained head and the exact abandoned set with recomputed statuses (F54);
- the stored qualification report (F55);
- the controls in force, required unchanged (F56).

A loss that abandons only proved-never-admitted heads is a fork resolution (7d), and one that abandons nothing is a redesignation (7e).

**Plan check of 8f10d755 (revision 23).** No SERIOUS CHALLENGE. **NO PASS**, on one blocker.
- **B1.** F56's `trust_roots` form omitted two of Manual §25.2's trust roots: `human_mechanism`, and the runner keys still to come.

Its answers confirm the rest:
- F54's exact set and its two refusals;
- F55's report;
- F57's reliance on derivation.

Its notes:
- Five more test cases.
- Exact equality is the single-home form (note 1).
- A test that a mark's head is never proved never admitted (note 2).

**Revision 24 repairs it.**
- **F56.** `trust_roots` is genesis's complete shape, with the folded dispatcher and human keys.
- **F54.** It records the single-home form.
- **7c's tests.** They add the five cases and note 2, and place the replica-lost row as disclosed.

**Re-check of 5636d551 (revision 24).** No SERIOUS CHALLENGE. **PASS**: B1 is closed and the notes are taken up. Its one note, to list the replica-lost row in §6, is taken up with 7c's record.

**Step 7c built (`LEDGER_LOSS`; readings F54-F57).**
- **`admission/loss.py`.**
  - `evidence` computes, from the replica's chain, the declared witnesses' authentic reports and the retained mark:
    - the retained head;
    - the exact abandoned set with `loss_status`;
    - the canonical report and its digest;
    - the controls in force: witness model, trust roots in genesis's full shape with the folded dispatcher and human keys, and the ruleset from `History`.
  - `loss_problems` requires each field to equal its recomputation. It refuses nothing abandoned (a redesignation) and only proved-never-admitted heads (a fork resolution).
- **Engine.**
  - `Admission.loss_evidence` and `prepare_loss` (what the operator puts in the record).
  - `admit_lifecycle` checks a loss against the recomputation and stores the report object in the entry.
  - The gate (F50) and the trial (F51) apply as in 7b. `LEDGER_LOSS` leaves `_UNBUILT`.
- **Tests.** `test_phase_f_step7c.py`, 14 tests, all on fixture ledgers.
  - **Truncated ledger, newer product.** The loss is admitted with the known-admitted head, the report stored, the boundary folded, `QUALIFIED` at the loss, and the mark raised. The next request absorbs the newer product (6a).
  - **Stale-consistent restore.** A permissive record before the boundary is withheld (`cont` false).
  - **A fork.** The loss names the admitted side, and the controls carry the ruleset at `A`.
  - **The mark's own head** is named and not proved never admitted (note 2). A mark that no witness reports is named too.
  - **A forged checkpoint** names nothing.
  - **Recomputation.** Each field must equal it, as must a status, and the shape is closed.
  - **A witness changed after prepare** changes the report and refuses the record; an unreadable file holds nothing.
  - **A qualified ledger** takes no loss.
  - **The compare-and-swap is refused** when the ref is past the readable prefix (note 1; 7d2d1c0 N2), with nothing appended.
  - **On `TEAM`:**
    - a mixed set, one head known admitted and one proved never admitted, is one loss naming both;
    - only proved-never-admitted heads are refused, as a fork resolution;
    - a loss under `UNQUALIFIED` with a possibly-admitted head passes the gate and is refused by the trial;
    - nothing abandoned is refused.
- **Departures from revision 24's list, each a finding and not a weakening.**
  - **The loss under `UNQUALIFIED` is not admitted.** With two of three witnesses lost, the unchanged witness set (F46) cannot hold any new entry, so the trial refuses it. §23.8 has the redesignation "carry a `LEDGER_LOSS`", so admitting it is 7e's.
  - **`REQUALIFY`'s positive case stays at derivation level** (`test_s3`, `test_support`). The equivalence Phase F's admission accepts is not current at the retained head, so §23.6 owes nothing for it, and the test asserts that. No permissive record Phase F admits is current at a fixture head.
  - **The surfaced-chain row has no reading to test.** It is disclosed in §6.
- **Mutants.** Thirteen, over `loss.py` and the engine's report storage: all are killed. X02 (the mark not named) and X04 (no authenticity filter) survived at first and are killed by the two tests added for them.
- **Full suite.** It passes: 1345 tests, 6 skipped. It ran before the two added tests, which then ran with the step's tests and pass.

**Same-family review of 8bfaaf0f (7c).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Its answers:
- The three departures are faithful and disclosed:
  - the loss under `UNQUALIFIED` goes to 7e's redesignation (§23.6, §23.8);
  - `REQUALIFY` stays at derivation level;
  - the surfaced-chain row has no reading.
- `evidence` is faithful to §23.6.
- The report is deterministic.
- The controls' shape is right.
- Sharing one function between prepare and admit leaves no blind spot beyond the design, given the pinning tests.

Its notes:
- **N2 (taken up).** A head that no witness reports but the mark vouches for was qualified, so held by `q_a` witnesses. Its status is floored at `POSSIBLY_ADMITTED`, and witnesses that lost the checkpoint beyond the fault model can no longer let a fork resolution (7d) abandon it with no boundary. The mark test asserts it, and mutant X14 (no floor) is killed. The SSDS suite passes.
- **N1 (answered).** A human `ACCEPTANCE` or `REVIEW` of the fixture's `NATIVE` subject is accepted, but derives `current = F` at the head under the fixture's empty policy (probe of this step). So no engine-level loss can withhold a current permissive record here. `REQUALIFY`'s positive case stays at derivation level (`test_s3`, `test_support`), as recorded.

**Step 7c is closed.**

**Step 7d built (`FORK_RESOLUTION`; reading F58).**
- **Code.** `admission/loss.py` gains `resolution_problems` (F58). `admit_lifecycle` checks a fork resolution against `loss_evidence`, and `FORK_RESOLUTION` leaves `_UNBUILT`. The gate (F50: `FORK` or `ROLLBACK`) and the trial (F51) apply as before.
- **Tests.** `test_phase_f_step7d.py`, 8 tests. 7c's helpers move into test-free bases (`LossFixture`, `TeamLedger`) that 7d subclasses, so no test runs twice.
  - **On `TEAM`.**
    - §23.8's "only proved-never-admitted entries lost" row: a `KEY_LIFECYCLE` held by one of three witnesses is lost by the replica (`ROLLBACK`), resolved with no boundary, and then the same record is admitted afresh by its identity (§22.4; lifecycle form, since the fixture `TEAM` genesis carries no policy objects for a request's derivation).
    - A fork keeps the replica's side.
    - A head held by `q_a` is a loss's.
    - A mark's head is never resolved away.
    - The set is exact, and so is the shape.
    - `UNQUALIFIED` is refused at the gate.
  - **On `LOCAL_TRUST`.** Any witnessed head is known admitted, so it is a loss's.
- **A 7c defect found and repaired.** Mutant D03 (no refusal of an empty set) survived, and tracing why exposed the defect. `evidence` named heads that an earlier admitted loss or resolution had already abandoned, which qualification no longer reads (`_abandoned`). So after any loss naming a known-admitted head, every later fork resolution would have been refused as "a loss's". `evidence` now excludes those digests, for checkpoints and the mark alike. A test admits a loss, then a resolution of a newer sub-quorum head naming only that head. Mutant D06 (no exclusion) is killed.
- **Mutants.** Six: five are killed. D03 is equivalent under the gate: `FORK` and `ROLLBACK` arise only from an off-chain head not yet abandoned, which `evidence` names, so "nothing abandoned" cannot reach a fork resolution's check. The refusal stays as defence.
- **Fail closed.** Choosing the side the replica does not hold, and restoring a recoverable suffix, wait for the ref restore (F47, Q-F14).
- **Full suite.** It passes on the repaired code: 1355 tests, 6 skipped.

**Same-family review of 099556e6 (7d and reading F58).** No SERIOUS CHALLENGE. **PASS** for both, with no blockers. Its answers:
- **F58** is faithful to §22.4, §23.6 and §23.8.
- **The exclusion over every readable entry** is consistent with `qualify`'s `_abandoned`. The trial holds every earlier recovery entry inside its qualified prefix, so a mismatch can only fail closed.
- **D03** is equivalent under the gate.
- **The lifecycle-form resubmission** is sound.

Its one note: the request-form resubmission waits for a `TEAM` fixture with policy objects, and is added when one exists.

**Step 7d is closed.**

**Revision 25: step 7e in two parts (§3.4, readings F59-F62, Q-F15).**
- **7e-i** builds the witness model per position as segments of the chain. `qualify_segments` is a single owner in the Ledger Store that every reader calls (F59).
- **7e-ii** admits a redesignation: its content (F60); the dual trial and the redesignation over a provisional entry, including another host's (F61, review 7d2d1c0 N1); and the critical-flag exemption.

§23.8's redesignation that "carries a `LEDGER_LOSS`" cannot be expressed in schema 1. It fails closed and goes to the stakeholder as Q-F15 (F62).

**Plan check of c36b278e (revision 25).** No SERIOUS CHALLENGE. **NO PASS**, on two blockers:
- **B1.** F59's "first `QUALIFIED` counts" could let an older segment mask a newer `ROLLBACK`.
- **B2.** Schema 1 does express a redesignation that carries a loss, as a `LEDGER_LOSS` whose `controls.witnesses` re-establishes the set, so F62 and Q-F15 sent a D4 gap to the wrong owner.

It confirmed F60 and F61, the shared boundary at `p`, and skipping another host's provisional distribution. It listed six missing tests.

**Revision 26 repairs them.**
- **F59.** A segment is held, by `q_a` of its witnesses at `p` or later, before any verdict is read. A held segment's verdict governs. A segment below its read quorum is `UNQUALIFIED`, and the older segment is read only while the new set responds and holds nothing from `p`. The fresh-clone residual, beyond the fault model, is disclosed.
- **F62.** 7e-ii builds the loss that re-establishes the witness set, amending F46 for the witness member alone. Q-F15 is withdrawn.
- **Tests.** 7e-i and 7e-ii add the listed cases.

**Re-check of 3b6ebcc0 (revision 26).** No SERIOUS CHALLENGE. **NO PASS**, on one blocker.
- **R1.** Counting "held" as `q_a` reports is not robust to `f` denials. Under `HARDENED`, a truncation with one denying witness would read the older segment and mask the rollback.

B2 is closed.

**Revision 27 repairs it.** The held test is §23.6's bound applied to the segment's start. The older segment is read only when the new set's holding from `p` is proved never admitted (`h + m + f < q_a`); in every other case the newest verdict governs. The read-quorum case is subsumed. 7e-i's tests add the `HARDENED` truncation with a denying witness and the partial copy.

**Re-check of b19707d9 (revision 27).** No SERIOUS CHALLENGE. **PASS**: R1 is closed, and every case traced holds. It names one accepted trade-off: a routine redesignation whose new set becomes unreachable right after its append reads `UNQUALIFIED`, so appends stop, rather than reading as the older segment's provisional entry. That fails closed, as §22.4's "appends stop" asks.

**Step 7e-i built (the witness model per position; reading F59).**
- **The Ledger Store's `qualification` API.**
  - `segments` gives genesis's model from 0, and a segment at each redesignation and at each loss that re-establishes a different set. An unparseable model qualifies nothing.
  - `segment_witnesses` gives the witnesses of every segment a position lies in.
  - `lineage_witnesses` gives every segment's witnesses.
  - `qualify_segments` is F59's rule: newest first, the held test by §23.6's bound, and the older segment's range, up to but excluding `p`, with a result at or past `p` read as the redesignation provisional.
- **Readers.** `Admission.witness_set` returns the last segment's model and every segment's reachable witnesses. `Admission.qualification` reads every segment's reports through `qualify_segments`, with the retirement statements counted under the last segment's model. `distribute` writes a checkpoint to the witnesses of every segment its position lies in. The trial adds its checkpoint only to those witnesses. The Interface's `present` reads through the same functions, and `LedgerAccess.witness_reports` now takes the witnesses to read.
- **Tests.** `test_phase_f_step7e.py`, 12 tests:
  - segments and where a checkpoint goes, including a loss with and without a new set;
  - a held redesignation, and a fresh clone with no mark;
  - a redesignation the new set does not hold, provisional, whether or not the old set holds its copy;
  - truncation to `p` reading `ROLLBACK` (B1);
  - under `HARDENED`, one denying witness still reading `ROLLBACK`, and one partial copy reading provisional (R1);
  - forged new-set checkpoints holding nothing;
  - an unreachable new set reading `UNQUALIFIED`;
  - an old-set fork after a held redesignation not read;
  - the mark read in the governing segment;
  - an unparseable model;
  - Admission and the Interface agreeing across a redesignation on a real fixture ledger (`LOCAL_TRUST` to another file witness), with the old set no longer written after it.
- **Mutants.** Nine: all are killed. S8, the held count without an authenticity filter, survived at first and is killed by the forged-checkpoint test.
- **Full suite.** It passes: 1366 tests, 6 skipped. It ran before the forged-checkpoint test, which then ran with the step's tests and passes.
- **Deferred to 7e-ii.** `RETIRED` under the last segment, on a ledger where a redesignation was admitted. The readers agreeing over another host's provisional entry. The trial's checkpoint going only to the new position's segments (exercised by the dual trial).

**Same-family review of ae5ab380 (7e-i).** No SERIOUS CHALLENGE. **NO PASS**, on one blocker. Its answers otherwise confirm:
- `qualify_segments`' order, bound, mark and authenticity filter;
- reading `segments` over the readable chain rather than the held prefix;
- that no reader is left on the genesis model.

**B1, repaired.** A probe with three segments showed the range conversion running only for the genesis segment. With S2's redesignation unheld, S1's verdict presented position 5 as `QUALIFIED`, instead of provisional over 4.
- **Repair.** Whichever segment governs after a newer one is skipped is converted: a head at or past the skipped segment's start becomes `QUALIFIED` at the position before, with the redesignation provisional.
- **Test.** The three-segment case is added, and it reads `QUALIFIED` at 5 once the third set holds it.
- **Mutants.** S10 (conversion for genesis only) is killed. S4-S6, S8 and S9, re-anchored to the rewritten test, are killed.
- **Suite.** The SSDS suite passes: 975 tests, 6 skipped.

**N1 (to 7e-ii).** `loss_evidence` counts each head's status over the last segment's witnesses only. 7e-ii counts each head over the segment its position lies in, and reports every segment's witnesses, with tests, since it is the first part to admit a loss that changes the set.

**Re-check of 9f841460 (7e-i).** No SERIOUS CHALLENGE. **PASS**: B1 is repaired. The three-segment probe now gives `QUALIFIED` at 4 with 5 provisional. The paths with no segment skipped, one skipped and two skipped all hold. **Step 7e-i is closed.**

**SD-74 and SD-75 (item 68).** The stakeholder accepted both recommendations.
- **Q-F13 (a).** `ssdp-shadow` is retired naming `ssdp-shadow-2` for discovery only, and the stakeholder signs the retirement record through `retire_shadow.py`. Review 749b37d N3 goes to the Manual clarification batch.
- **Q-F14 (a).** The ref restore and §5.7's route under `INTEGRITY_HALT` are handed off to Phase H, whose G2 row is widened.

The real retirement waits for the stakeholder's run of `retire_shadow.py`. Its `prepare` writes to the SSDS home, which this author touches only read-only through the program.

**Step 7e-ii built (admitting a redesignation; readings F60-F62).**
- **`admission/loss.py`.**
  - `new_model`: a sound model (`WitnessModel.validate`) that differs from the one in force.
  - `controls_problems`: F46 amended for the witness member alone (F62).
  - `redesignation_problems`, which requires:
    - closed fields;
    - `continues_from` equal to `A`;
    - no later head in evidence, which names the loss as the route;
    - `refs` naming the stored report under `UNQUALIFIED`, and none otherwise.
  - `in_force`.
  - `evidence` now counts each head over the witnesses of the segment its position lies in, and reports every segment's witnesses (review ae5ab38 N1). The controls' witness member is the model in force.
- **Engine.**
  - A redesignation passes the gate (settled `QUALIFIED`, over a provisional entry, or `UNQUALIFIED`) and its content check. Under `UNQUALIFIED`, its report is stored with the entry.
  - The settling step tolerates another host's provisional entry for a redesignation alone (review 7d2d1c0 N1).
  - `old_set_holds` is the dual trial's second half, for a redesignation and for a loss that changes the set: where the old set reaches `r`, the extended chain must qualify under it at the new position.
  - `prepare_redesignation` gives the operator the fields and `refs`.
  - `qualify` exempts §23.4's one chain, a redesignation directly over a provisional entry, from the critical flag.
- **Tests.** `test_phase_f_step7e.py` now has 23 tests. Added since 7e-i:
  - **The exemption.**
  - **A routine `LOCAL_TRUST` to `TEAM` redesignation.** It is held by both sets, with segments at genesis and at the redesignation. A later admission goes to the new set only.
  - **Retirement and loss evidence.** `RETIRED` is read under the last segment. A lost later head is counted `KNOWN_ADMITTED` over the `TEAM` set; under the old single witness it would read never admitted (N1).
  - **A conflicting head before the redesignation** is counted over the old segment's witnesses (N1).
  - **The old set reachable but unable to hold it.** Refused, for a redesignation and for a loss that changes the set.
  - **Under `UNQUALIFIED`.** The redesignation continues from the intact head with its report referenced, and is refused without the reference.
  - **Content refusals.** The same model, an unsound one, a wrong `continues_from`, a stray field, a stray reference.
  - **On a `TEAM` ledger with two host keys.** A redesignation is admitted over the other host's provisional entry, which has no checkpoint, settling the prefix.
  - **§23.8's witness-loss row with a later head.** The loss under the lost set and a redesignation are both refused. The loss carrying the new `TEAM` set is admitted, `QUALIFIED`, and starts a segment.

  7b's and 7c's two expectations now name the more specific refusals.
- **Mutants.** Thirteen: all are killed. W11 (no dual trial for a loss) and W12 (statuses over the last segment) survived at first and are killed by the two tests added for them.
- **Full suite.** It passes: 1376 tests, 6 skipped. It ran before the two added tests, which then ran with the step's tests and pass.
- **Found while testing.** A provisional entry whose checkpoint reached fewer than `q_a` witnesses reads `UNQUALIFIED`, not provisional, because H* must extend every observed checkpoint (§23.4). So "over a provisional entry" is the case with no checkpoint yet: a crash between the append and the distribution.

**Same-family review of 00b4c1ac (7e-ii).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Its answers:
- The content check, the amended controls and the per-segment evidence are faithful to §22.4, §23.4 and §23.8.
- Skipping the old set below `r` is §23.8's "where the old is reachable".
- Admitting over another host's provisional entry is §22.4's sanctioned exception: the compare-and-swap prevents a race, and that host's later distribution only holds its entry below the redesignation.
- The exemption's condition is exactly §23.4's one case.

Its notes:
- **N1 (taken up).** F61 states that a partly distributed provisional entry takes the `UNQUALIFIED` route.
- **N2 (recorded).** Any registered human may approve a redesignation, as for a retirement. Whether a ledger names the deciding role goes to the Manual clarification batch, consistent with SD-74.

**Step 7e is closed.**

**`ssdp-shadow` retired (SD-74).** The stakeholder ran `retire_shadow.py` and signed in their own shell. The `LINEAGE_RETIREMENT` sits at position 1, naming `ssdp-shadow-2` for discovery only. The host-signed statement is held by the ledger's witness, which reads `RETIRED`. A read-back through the Ledger Store, writing nothing, confirms it, and confirms `ssdp-shadow-2` is unaffected (`QUALIFIED` at 0). Evidence: `qualification/ssds80/PHASE-F-SHADOW-RETIREMENT-EVIDENCE-SSDS-8.0.md`.

**Revision 28: steps 7f and 7g in detail (§3.4, readings F63-F64).**
- **7f.** A continuity attestation's own checks run (target, listed ids, evidence, human actor), and the record stays `SCHEMA_UNSUPPORTED` until a designation exists (F48). A challenge of an attestation is permitted.
- **7g.** Field checks for the replica redesignation, the lineage migration and the redaction notice. Each refusal names its deferral: the replica restore and re-encoding to Phase H (SD-75), and the redaction's halt disclosed.

**Plan check of 66ac030b (revision 28).** No SERIOUS CHALLENGE. **NO PASS**, on one blocker.
- **B1.** SD-75 hands Phase H only the ref restore and §5.7's route. Deferring `LINEAGE_MIGRATION` and `REDACTION_NOTICE` under it moved Phase F work with no decision behind it. Revision 28's "a redaction halts" has no textual basis.

It confirmed F63's codes, keeping `REPLICA_REDESIGNATION` refused under SD-75, and F64's shapes. It noted that listed ids are subjects or records, and that evidence uses `REF_OBJECT`.

**Revision 29 repairs it.**
- **`REDACTION_NOTICE`** is built as §24.2's rotation-branch notice, with no derived effect, and the halt rationale is withdrawn.
- **`LINEAGE_MIGRATION`** keeps its field checks and is refused until Q-F16, a new question on where §24.2's replacement lineage is built. §1 and §6 are reconciled with it.
- **F63** takes both refinements, and 7f's tests assert the attestation's codes beside `SCHEMA_UNSUPPORTED`.

**Re-check of 2d01eb22 (revision 29).** No SERIOUS CHALLENGE. **PASS**: B1 is closed and the notes are taken up. Its notes:
- **1 (recorded).** Any registered human approves a `REDACTION_NOTICE`, though §24.2 places the rotation branch "under the security owner". Whether a later ledger names that role goes to the Manual clarification batch, as SD-74 sent the retirement's.
- **2 (recorded).** In Phase F a notice names ledger objects only. A sensitive value in pinned product content, a repository blob, is not nameable by it; that goes with Q-F16's replacement lineage.

**Steps 7f and 7g built (readings F63, F64).**
- **7f.**
  - **Step 5 (`dependency_codes`).** It judges a continuity attestation's target: an earlier `LEDGER_LOSS` (`DEP_TARGET_KIND`, `DEP_TARGET_ORDER`). It always adds `SCHEMA_UNSUPPORTED` beside them (F48). A `CHALLENGE` of an attestation is permitted.
  - **Step 2 (`attestation_references`).** The loss and every listed id are known records or subjects (`REF_TARGET`), and the evidence is stored or carried (`REF_OBJECT`).
  - **4d's test** is renamed to say the attestation stays unsupported.
- **7g.**
  - **`admission/lifecycle.py`** gains `replica_problems`, `migration_problems` (always naming Q-F16) and `redaction_problems`.
  - **`admit_lifecycle`.** `REDACTION_NOTICE` and `LINEAGE_MIGRATION` join `KEY_LIFECYCLE` as head kinds (`_HEAD_KINDS`): they carry the expected head and go through the held head, with no trial. The notice is admitted when its fields are good, and the migration is always refused. `REPLICA_REDESIGNATION` stays refused at the gate.
- **Tests.** `test_phase_f_step7f.py`, 11 tests, cover:
  - an attestation that is well formed (only `SCHEMA_UNSUPPORTED`), has a wrong target kind, or targets a loss in the same entry;
  - a challenge of an attestation, permitted;
  - the step-2 references (a part is no subject; unstored evidence);
  - a submitted attestation refused with `REF_TARGET`;
  - each kind's field checks;
  - a redaction notice admitted with `obs` and no derived effect (the derived obligations and findings are unchanged), and one naming an unstored object refused;
  - a migration refused naming Q-F16, and a replica redesignation refused at the gate.
- **Mutants.** Fourteen: all are killed. G04 was first written as a text-only change that still named Q-F16; re-run as the real mutation, dropping the refusal, it is killed.
- **The test environment.** After the stakeholder's restart, `/tmp/claude-1000/ssds-venv` was gone. It was recreated from miniconda's Python 3.13 with `pyproject.toml`'s declared dependencies (`requires-python >= 3.11`) and `orchestrator/requirements-dev.txt`. A first full run without the latter failed two Core tests for want of `hypothesis` and `build`. That was an environment gap, not a code defect, and both pass with them. With them, the full suite passes: 1389 tests, 6 skipped.

**Same-family review of 80222c23 (7f and 7g).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Its answers:
- The steps are faithful to §3.4, §22.1, §23.7 and §24.2.
- A notice rightly skips the trial: head kinds are admitted at the held head, and the commit's re-qualification decides.
- The attestation's step-2 and step-5 codes cannot double-report or conflict.

Its notes:
- **N1 (taken up).** `LINEAGE_MIGRATION` is refused before any state is read, still naming its field problems and Q-F16, and it leaves `_HEAD_KINDS`. §24.2's migration binds a new genesis, so its eventual path may not be the held head. The test asserts that the held head is not read. The SSDS suite passes: 996 tests.
- **N2 (recorded).** A `REDACTION_NOTICE`'s approver goes to the Manual clarification batch with SD-74's, as the re-check of 2d01eb22 recorded.
- **N3 (taken up).** A comment says a frame-declaring attestation is refused `REF_TRANSFORMATION`.

**Step 7 is closed for Phase F.**
- **Built:** 7a-7g.
- **Disclosed and handed off:** the ref and replica restore and §5.7's route to Phase H (SD-75).
- **Waiting on Q-F16:** `LINEAGE_MIGRATION` and §24.2's replacement lineage.
- **Unbuilt by F48:** a continuity attestation.

**SD-76 (item 69): Q-F16 (a).** §24.2's replacement lineage (re-encoding, commit identity and pseudonym mapping, and `LINEAGE_MIGRATION`'s equal-state qualification) is handed to Phase H with its privacy harnesses, as an extension of SD-75. The G2 workplan's Phase H row is widened. `LINEAGE_MIGRATION` stays refused in Phase F with its field checks.

**Revision 30: step 8 in parts (§3.5, readings F65-F71, Q-F17, Q-F18).** A read-only survey found that six of step 8's thirteen items are partly built and seven have no code, and that fourteen plan lines defer work into step 8. Step 8 is split into seven parts:
- **8a.** The Dispatcher at a named `H*`, the only part step 10 needs.
- **8b.** Contract binding, after Q-F17.
- **8c.** Scheduling constraints.
- **8d.** Judge selection.
- **8e.** The task-bound interface.
- **8f.** Transports, with the MCP server on the standard library.
- **8g.** Retry and resubmission.

Two readings go to the plan check: `HUMAN_ATTESTED_FRESH` by a co-submitted attestation (F68), and §8.3 step 3 over §25.1 for a re-issue (F71). Two questions go to the stakeholder: Q-F17 (the system contract id) and Q-F18 (deferring `intake.neutral_auto`).

**Plan check of 5d4a0e26 (revision 30).** No SERIOUS CHALLENGE. **PASS**, with no blockers. It confirmed:
- the split and its order;
- F65's owner, `ledger.qualification`, the Ledger Store's currentness function;
- F68's reading, which §5.10 (a) states directly ("any co-submitted attestation");
- F71's reading of N5;
- Q-F17's options;
- a standard-library MCP server as "no new dependency";
- Q-F18's deferral.

Its notes are taken up:
- **1.** `HUMAN_ATTESTED_FRESH` is placed in 8d, with the routes it serves.
- **2.** A re-issue verifies lineage from the retained record's original binding.
- **3.** Q-F17's id is `{system, version}`, the system version with the ruleset in force at issue, not the `governs` protocol.
- **4.** "Until Q-F17" is added to 8c's joint-invariant reviews, 8d's judgment tasks and 8g's re-issue. Step 10 needs 8a and 8f's refusal path.
- **5.** The MCP server pins its protocol revision and tests the handshake.

**Step 8a built (the Dispatcher at a named `H*`; reading F65).**
- **One currentness owner.** `ledger.qualification.currentness` composes a ledger's qualification: every segment's reports, the retirement statements of the set in force counted under its model, `qualify_segments` and the mark. `host_keys` reads the genesis trust roots. Admission's `qualification`, the Interface's `present` and the Dispatcher call it, and the two copies are gone. Admission now passes every segment's statements, as the Interface does, so the one function decides which count.
- **The would-issue set** (`dispatcher/schedule.py`). `would_issue` raises `NotIssuable` unless the head is `QUALIFIED` with no provisional entry. It derives the qualified prefix and lists each obligation held by an agent role (`AGENT_ROLES`, now exported by derivation with `READY`) that is `READY`. Each task carries a stable `task_id` (head and obligation) and whether its contract is an item's or a system's (Q-F17).
- **Write-ahead issuing.**
  - `issue` journals `INTENT` (with the head), signs the envelope, journals `ISSUED`, then `HANDED`. It refuses a task not at its own named head.
  - `Journal.recover` abandons every intent not handed out.
  - `Journal.outstanding` excludes abandoned tasks.
- **`ssds dispatcher serve`** (the CLI's composition root) is observe-only. It reads the chain, witnesses and mark through `HomeAccess`, composes currentness, prints the would-issue set, and writes nothing. It exits 1 when the head is not named.
- **The real ledger.** Run read-only on `ssdp-shadow-2`, it reports `QUALIFIED` at 0 with an empty would-issue set (no `NATIVE` subject, so no agent obligation), and the operator state's timestamps are unchanged.
- **Tests.** `test_phase_f_step8a.py`, 12 tests:
  - one composition for Admission and the Interface, and an empty chain;
  - the would-issue set against derivation's readiness, on a fixture whose policy names a human D3 judge, so the reviewer-held `ACCEPT` is `READY` (the baseline's authorship is unknown, so no fresh agent reviewer is eligible);
  - only `READY` agent-held obligations becoming tasks, on a stubbed workflow mixing holders and states;
  - nothing issued from an unqualified, rolled-back, retired or provisional head;
  - observe-only writing no journal or mark;
  - `dispatcher serve`, including exit 1 when the witness holds nothing;
  - the journal order;
  - a crash before the envelope, and one after it before the hand-out, each abandoned and outstanding nowhere;
  - an envelope outstanding until its task finishes;
  - a task issued only at its own head.

  `test_phase_f_step7e.py` adds that retirement counts only the set in force.
- **Mutants.** Eleven: ten are killed. C11, deriving the whole chain rather than the qualified prefix, is equivalent: a `QUALIFIED` head with no provisional entry is the chain's last. C01, C03, C04 and C08 survived at first and are killed by the added tests and by routing Admission's statements through the one owner.
- **Full suite.** It passes: 1402 tests, 6 skipped.

**Same-family review of 546cc86c and a889ed5e (8a).** No SERIOUS CHALLENGE. **PASS**, with no blockers. It found 8a faithful to F65, catalogue §3.1's journal order and §23.4. It found the fitness boundaries respected and observe-only `serve` right under F8.

Its notes:
- **N1 (recorded).** `READY_PROVISIONAL`, work under a provisional continuation (§10.5), is not dispatched in 8a. That fails closed, and 8c revisits it with the scheduling constraints.
- **N2 (taken up).** `task_id` changes with the head, so a still-`READY` obligation would get a second task while its first is out. `Journal.open_obligations` lists the obligations with a task handed out, and `issue` refuses another for them. Tested.
- **N3 (taken up).** An envelope signed but not recorded as handed may have reached its route. `outstanding` keeps it listed after recovery and drops only intents never signed: over-listing only admits never-lost records, the fail-safe direction. The test now expects it listed. When routes are real (8b, 8f), recovery also observes the route.
- **N4 (recorded).** `currentness`, now the single owner, verifies statements and checkpoints with the genesis host keys. When admission keys gain a lifecycle fold, it folds there (7a N1).

Mutants: C12 (no open-obligation check) and C13 (abandoned envelopes unlisted) are killed. C14's "handed minus abandoned" was dead, since `recover` never abandons a handed task, so it is simplified away. The SSDS suite passes.

**SD-77 and SD-78 (item 70).**
- **Q-F17 (a).** Schema 1 is corrected in place, so `binding.item` also admits `{system, version}`: the system version, under the ruleset in force at issue. That unblocks 8b, and with it 8c's joint-invariant issue, 8d's judgment tasks and 8g's re-issue.
- **Q-F18 (a).** `intake.neutral_auto` is deferred to Phase G, off and disclosed at the exit.

**Step 8b built (contract binding; reading F66, SD-77).**
- **The schema-1 correction, in place (SD-77).** `binding.item` admits `{unit, rev}` or `{system, version}`, each closed. No ledger holds a record bound to a system task.
- **`Workflow.contract_revision(o)`** (derivation owns it):
  - an item obligation gives `{unit, rev}` at the state, the revision F36's staleness check compares;
  - any other gives `{system: o.kind, version: <the ruleset's system in force>}`.
- **The Dispatcher.** A `Task` carries its `contract_revision` from `would_issue`, and `issue` puts it in the envelope; the caller no longer supplies one.
- **Authentication.** Its existing comparison of `binding.item` with the envelope's `contract_revision` now covers both forms.
- **Readers.** Two derivation readers that resolved any dict-valued `binding.item` as an item (`conformance._scientific_review`, `Briefing.work`) now require `{unit, rev}`, so a system id resolves no item. The others already required it, or read with `.get`.
- **One brief-digest owner.** `interface.render.brief_digest` is used by `Brief.digest` and by `Issuer.issue` (line 818's duplicate).
- **Tests.** `test_phase_f_step8b.py`, 9 tests:
  - the schema's two forms and four malformed ones;
  - a system task's id (kind and `ssds-rules/1`) and an item task's;
  - the would-issue set carrying each task's contract;
  - an issued system task's envelope;
  - a bound record authenticating only when it copies the envelope's id (absent, or another kind's, is `AUTH_ENVELOPE`);
  - the digest formula;
  - both readers over a system-bound result.

  8a's tests follow the `Task` change.
- **Mutants.** Seven: all are killed. B6, the briefing guard, survived at first and is killed by the added test.
- **Full suite.** It passes: 1412 tests, 6 skipped.

**Same-family review of c8b78706 (8b).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Its answers:
- `contract_revision` reads the ruleset at exactly the head the task is issued at (`issued_at_position`).
- Every reader of `binding.item` is safe for a system id. Each was traced, and `item_at(None, None)` finds nothing, since a `None` unit is no structure unit (N3).

Its notes:
- **N1 (recorded).** A step-2 check that a contract id agrees with its bound obligation (its kind, or its item) would be defence in depth. Authentication already ties the record to the signed envelope, and derivation never reads the id's fields.
- **N2 (recorded).** F36's staleness covers item revisions only. A system id whose version is no longer in force is unreachable while no path changes the ruleset's system. When ruleset adoption opens, F36 extends to it.

**Step 8c built (scheduling constraints; reading F67).**
- **The principal is an agent role.** 8a's `AGENT_ROLES` omitted it. Catalogue §12.3 gives the principal an R1 role template holding `COORDINATE` and `CONTRACT`, and §9.2 schedules coordination tasks, so `PRINCIPAL` joins the implementer, investigator and reviewer. The human's obligations stay briefs.
- **Serialization surfaces.** A policy key, `[workflow] serialization_surfaces`, lists unit ids and defaults to empty. `Workflow.serialization(o)` gives the surfaces a task's write scope meets, a write unit meeting a surface when one contains the other (`Structure.ancestors`), and a principal's task's plan. A judgment writes nothing.
- **Scheduling.** `issuable` applies, against the journal's open tasks and the batch's earlier tasks:
  - no second task for an obligation with one open;
  - at most one open task per serialization surface;
  - at most one open coordination task per plan.

  `would_issue` takes the open tasks. `ready` is the pre-scheduling set. `issue` checks the same rules and records the task's surfaces and plan in its intent. `observe` reports the held tasks with why.
- **Journal states.** `finished` (the task holds nothing more), `suspend` (it stays open, keeping its obligation and surfaces), `resume` (by identity, under its envelope: no new envelope), `suspended` and `open_tasks` (handed and not finished, suspended included).
- **Leases** (`dispatcher/leases.py`, K2). An append-only lease log in the Dispatcher's home (`state/<ledger id>/dispatcher-leases.jsonl`), keyed by the worktree identity the composition root resolves, with time passed in. A live lease of another task refuses; expiry or release frees the worktree; a task renews its own. Nothing Admission, derivation or the Ledger Store reads imports the Dispatcher, so a lease changes scheduling, never correctness.
- **Joint-invariant reviews** (§9.2) are scheduled as system-contract tasks like any judgment.
- **Tests.** `test_phase_f_step8c.py`, 13 tests:
  - the policy key and its malformed form;
  - the principal as an agent role;
  - one task per surface, per plan's coordination, and per open obligation;
  - a joint-invariant review issued with its system contract;
  - surfaces met by containment either way, and a principal's plan;
  - a finished task freeing its obligation;
  - suspension keeping a task open and refusing a second issue, and resumption by identity;
  - `observe` reporting the held tasks;
  - lease acquisition, refusal, renewal, expiry and release;
  - no Admission, derivation or ledger module importing the Dispatcher.

  8a's fixture now takes its policy as a class attribute.
- **Mutants.** Thirteen: all are killed.
- **Full suite.** It passes: 1425 tests, 6 skipped.
- **Not built in 8c.** Resuming on the coordination decision's admission is the caller's act by identity. The automatic trigger reads a `BLOCKER`'s answer, which 8g's retry loop drives. `READY_PROVISIONAL` stays undispatched (review 546cc86 N1): a provisional continuation's work waits until the step that admits provisional discharge in Phase F, if any; none does yet.

**Revision 31: step 8d in detail (reading F72).** It covers:
- judge selection from derivation's eligible judges, with a fresh agent reviewer's empty `input_sessions` as its distinct context;
- the judge's provenance;
- the brief's notice on unknown authorship;
- `HUMAN_ATTESTED_FRESH`: a manual or Git-envelope task binding may carry the operating human's co-signature, which authenticates only that human's co-submitted `LINEAGE_ATTESTATION` of a record bound to the task. That attestation alone lets the record carry the class.

The co-signature is an addition to Admission's request binding, not to the ledger schema. It goes to the plan check before it is built.

**Same-family review of 455d4880 (8c).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Its answers:
- Scheduling stays out of correctness, and §9.2's three constraints hold.
- `PRINCIPAL` matches §12.3.
- Region-based write units with containment either way catch writes into a surface's parts and surfaces inside a written composite.
- A suspended task rightly keeps its surfaces, with no deadlock, since its resumption is a principal's task, serialized per plan.
- The leases read soundly through expiry, re-acquisition and a late release.

Its notes, recorded:
- **N1.** A surface nested only dynamically inside a written unit, with no membership relation, is not detected. That is acceptable for scheduling.
- **N2.** `Leases.acquire` reads, then appends, unlocked. Phase F runs one Dispatcher process per ledger, and a second process could double-lease, which changes scheduling only.
- **N3.** A joint-invariant review is a judgment, which writes nothing and carries no surfaces, so no surface ever holds it. Its scheduling is that of any judgment, which 8c's joint-invariant test shows.

**Plan check of 8f1c948f (revision 31).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Its answers:
- The co-signature is a faithful D4 realization of §5.10 (a)'s "co-submitted attestation", needing no stakeholder decision. It changes the request binding (F9), not the ledger schema.
- Its authentication rules are tight.
- An empty `input_sessions` is the right fresh context.
- Keeping the judge's facts in provenance is acceptable.

Its notes, taken up in 8d:
- **1.** The co-signature is bound to this task's envelope.
- **2.** The `input_sessions` reading is disclosed and sent to the Manual clarification batch.
- **3.** Unverified judge facts decide nothing, and a model-family requirement fails closed.
- **4.** An attesting human who is an author is stated and tested.
- **5.** The manual-route human judge follows §5.10 (f)'s human rule.

**Step 8e built (the task-bound interface; reading F69).**
- **The Interface.** It gains a `TaskAccess` protocol (`envelope`, `record_read`), which the Dispatcher's `Journal` satisfies, so the Interface imports no Dispatcher module.
  - `Session.open_task(task, tasks)` renders the task's brief at its basis, the envelope's `issued_at_position`, through `Workflow.at`. It refuses a task never handed out, a basis outside the qualified prefix, and a brief whose digest is not the envelope's.
  - `Session.read_task` answers at the basis and records `(unit, rev)` or the path's content digest in the task's basis. A refused read records nothing.
  - `Session.changed_since_basis` is `ask(changed)` from the basis over the task's work's subjects.
- **The renderer.** It takes an issued task's `{task_id, route}`. The brief's status reads `ISSUED task … on route …`, and its reads notice says whether the route observes reads (harness) or not (manual, Git-envelope; §16.4). An unissued brief keeps `NOT ISSUED`.
- **The Dispatcher.**
  - `brief_for` renders a task's brief at its head with the task and route named, so the envelope's digest covers bytes that `open(task)` reproduces.
  - The journal's `ISSUED` entry keeps the public, signed envelope object.
  - `Journal.envelope` returns it only once the task is handed out.
  - `Journal.record_read` and `reads` hold the task's reads.
- **Tests.** `test_phase_f_step8e.py`, 7 tests:
  - the issued brief reproduced at its basis;
  - a brief whose digest differs refused;
  - an unknown task, and one never handed out, refused;
  - answers staying at the basis after the head moves: the product absorbed a change, and a read at the basis returns the old content, with the same brief and `changed` from the basis;
  - unit and path reads recorded, and a refused read recording nothing;
  - the reads notice per route.
- **Mutants.** Six: all are killed. E2, answering at the presented head, survived at first and is killed by the absorption test.
- **Full suite.** It passes: 1432 tests, 6 skipped.

**Same-family review of 041c6c98 (8e).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Its answers:
- 8e is faithful to §16.1 and §16.4.
- `Workflow.at(issued_at_position)` is the task's basis.
- Keeping the public, signed envelope in the private journal is safe.
- The work's subjects are the right default for `ask(changed)`.

Its notes:
- **N1 (taken up with 8d).** `brief_for` defaulted to no doctrine while `open_task` used the Session's reader, so a task pinning doctrine would refuse its own brief. `brief_for`'s doctrine reader is now required, supplied from the source the Session uses. The tests pass one reader to both.
- **N2 (recorded).** An envelope with no `brief` digest is not digest-checked. Every issued task should carry one once issuing always renders its brief (8f's transports issue through `brief_for`).
- **N3 (recorded).** `open`, `read` and `ask` take a task id without a credential. On the local Interface, with the journal in the private SSDS home, that is sound. If the Interface is exposed to agents, task reads bind to the task credential.

**Step 8d built (judge selection and a human's attestation of a fresh session; reading F72).**
- **Judge selection** (`dispatcher.select_judge`). A freshly launched agent reviewer on the harness route is preferred: `Issuer.issue`'s default `input_sessions` are empty, so it reads no authoring session. Otherwise the first eligible human goes on the manual route, and with none, nothing. This rests on derivation's `eligible_judges`, which already excludes the judged authors.
- **The judge's facts** (`judge_provenance`). `{lineage_class, route, model_family, toolchain}` for the record's `provenance.judge`, an unverified audit stamp. Authentication and derivation never read it, and the inspector and briefs show only the binding's verified class (plan check note 3). A policy requiring a model family fails closed until model family is attested.
- **The brief's notice.** A judgment brief over content whose `judged_authors` holds `UNKNOWN` says that an agent's answer is never independent of it, and that a human judge's is independent only with a `NON_AUTHORSHIP_ATTESTATION` (§5.10 (f)'s human rule) or is the owner's (notes 5, line 966). Derivation's facade now exports `UNKNOWN`.
- **The co-signature** (`admission/authenticate.py`). A manual or Git-envelope task binding may also carry `human: {actor, signature}`.
  - The signature is a registered human's over the request, and the request's bound records name this envelope's digest, so a co-signature moved onto another envelope attests nothing (note 1). The binding's stored object and digest exclude it, as they exclude the credential's signature.
  - It authenticates only that human's `LINEAGE_ATTESTATION` (`HUMAN_ATTESTED_FRESH`) of a record bound here in the same request. Any other human record is `AUTH_ACTOR`.
  - A bound record attested so must carry `HUMAN_ATTESTED_FRESH`, and an unattested one must not (`AUTH_ENVELOPE`).
  - On the harness route the co-signature authenticates nothing.
  - Authentication reads no authorship, so an attesting human who is an author is admitted, and its correction is a challenge (F13; note 4).
  - Admission accepts `LINEAGE_ATTESTATION` (`record` target) only when its target is co-submitted (`REF_TARGET` otherwise): a later attestation classifies nothing (§5.10 (a)).
- **`input_sessions`** (note 2). §12.2's launch attestation names "the sessions of the task's inputs (the authoring task of a candidate under review …)". A judge's are empty, because under F11's closure naming the authoring session would make every review non-independent. This reading of a textual tension goes to the Manual clarification batch.
- **Tests.** `test_phase_f_step8d.py`, 11 tests:
  - selection and the audit stamp;
  - an attested record carrying the class;
  - the class without its attestation, and an attested record claiming `UNKNOWN`, refused;
  - only the co-signer's attestation of a record bound here authenticated (a stray human record, another human's attestation, a target not bound here);
  - the harness route and a bad signature authenticating nothing;
  - a co-signature moved to another envelope;
  - an author's attestation;
  - an attestation of a record not co-submitted refused at admission;
  - the brief's notice.

  8e's tests now pass the shared doctrine reader.
- **Mutants.** Eight: all are killed. D3, an attestation of a record not bound here, survived at first and is killed by the added test.
- **Full suite.** It passes: 1443 tests, 6 skipped.

**Same-family review of 50954f95 (8d).** No SERIOUS CHALLENGE. **PASS**, with no blockers. Probed adversarially, the co-signature authenticates nothing but its own attestation of a record bound here. No bound record obtains `HUMAN_ATTESTED_FRESH` without it, and a co-signature cannot be reused across requests or envelopes. Leaving it out of the stored binding object leaves nothing unverifiable, and refusing an attested record that claims `UNKNOWN` is right. 8d is faithful to §5.10 (a) and (f), §12.2 and §16.5.

Its notes are taken up with 8f:
- **N1.** Step 2 accepts a `LINEAGE_ATTESTATION` only when its co-submitted target is task-bound, so a human's attestation of their own record is refused. Tested.
- **N2.** `_attests`' docstring states which checks the co-signature replaces.

**Step 8f built (the transports; reading F70).**
- **The Git-envelope transport** (`interface/envelope.py`, fitness B1's reserved writer).
  - `publish` writes `task.json` (the signed binding object) and `brief.md` on `refs/heads/ssds/run/<task-id>`, creating the ref only if absent (write once).
  - `fetch` reads `result.json` from that one ref.
  - Both refuse any repository whose common Git directory is the product repository's, so a linked worktree or path alias is refused too.
  - `run_ref` refuses names that are not task ids.
  - The commit identity is fixed and the environment's `GIT_*` settings are dropped.
- **The MCP server** (`interface/mcp.py`): JSON-RPC 2.0 over stdio on the standard library, pinned to MCP `2025-06-18`, tools capability only.
  - `initialize`, `ping`, `tools/list`, and `tools/call` for `status`, `ask`, `read`, `open` and `inspect`, the CLI's operations through the same `Session` from the composition root's `connect`.
  - Notifications get no response. A refusal is `isError`. The JSON-RPC error codes are -32700, -32600, -32601 and -32602.
  - `ssds mcp serve` mounts it.
- **The fitness table.** The Interface's public modules gain its two transports, `mcp` and `envelope`, so the composition root may import them.
- **Tests.** `test_phase_f_step8f.py`, 8 tests:
  - a Git-envelope round trip, in which an agent clone writes `result.json` back onto the run ref, with the product repository's refs and files unchanged;
  - the product repository refused directly and through a linked worktree;
  - a run ref written once, and malformed task ids refused;
  - the MCP handshake and its pinned revision, a notification and `ping`;
  - the tools equal to the CLI's command set;
  - a call answering as the `Session` does;
  - the error codes;
  - serving over stdio.
- **Mutants.** Nine: all are killed.
- **Full suite.** It passes: 1451 tests, 6 skipped.
- **What step 10 needs.** Step 10's test, that a candidate request through the library API, the Dispatcher or a transport is refused at Admission's entry, can now be run through these transports.

**Revision 32: step 8g in two parts (readings F73-F74).**
- **8g-i** is composition and Dispatcher functions:
  - mechanical retry through derivation's re-dispatch route and budget;
  - integration requests built and refused under SD-70;
  - §9.1's re-request at a new head.
- **8g-ii** authenticates a re-issued record through the derived `REISSUE` obligation's list, since the envelope's fields are closed. It accepts the original actor and lineage only for those identities, with content equal to the retained body.

8g-ii's authentication exception goes to the plan check before it is built.

**Revision 33: F73-F74 repaired after the plan check of 53216046 (NO PASS on B1).**
- **B1.** A re-issue's existence check reads the derived `REISSUE(envelope)` obligation at the base, not the original obligation, which may be gone by then. Role and kind are read from the retained original envelope. Test: a retained adverse review is resubmitted after its `REVIEW(X)` is gone, and is admitted.
- **Answer 2.** The re-issued envelope copies the original `role` and `governs`.
- **Answer 3.** The Dispatcher's re-request acts only on Admission's outcome; no duplicate task is issued while revalidation is pending (test added).
- **Answer 1.** F74 records that it corrects F71's "lists".

**Revision 34: F74 repaired after the re-check of 25bd1d0d (NO PASS on B1; F73 passed).**
- **B1.** The re-issued envelope names the original obligation and role, copied with `governs` from the retained original envelope, so it is coherent under §12.2 and a resubmitted record's `binding.obligation` keeps naming what it answers. Only the existence half of step 3 is met by the derived `REISSUE(envelope)` obligation, for exactly the identities it lists. Test: a resubmitted adverse review counts in `REVIEW(X)`'s answering and routing as the original would have.
- **Note 1.** The original role is judged under the ruleset in force at the original envelope's `issued_at_position`.

**Same-family review of 4d949827 (8f).** No SERIOUS CHALLENGE. **NO PASS** on one blocker. 8d's N1 and N2 are confirmed taken up.
- **B1. MCP's refusal set differed from the CLI's.** `handle` caught `(Refused, KeyError)`. So a `HomeRefused` (an invalid ledger id) crashed `mcp serve` and left the rest of the stream unanswered, and a `KeyError` fault inside `Session` was reported as a refusal. §16.10 and F70 require the same operations as the CLI.
- **Its answers.**
  - The product guard holds for every way in that was probed: a linked worktree, a symlink alias, a subdirectory, and the `GIT_*` variables. Dropping `GIT_*` is necessary: `GIT_OBJECT_DIRECTORY` alone writes into the product's store while the common-directory check still passes.
  - The fixed identity and dates make the run ref regenerable byte for byte.
  - Create-only `update-ref` is right, but `"0"*40` is SHA-1-specific.
  - The MCP surface is the CLI's.
  - The fitness change is justified.
- **Notes.** `fetch` reads only the tip (N2); a repository nested in the product's working tree is allowed; `run_ref` is weaker than `git check-ref-format`; a non-repository scratch raises the wrong error; the scratch's hooks run; untested conformance points (the client's `protocolVersion`, the `jsonrpc` member, a client response answered, invalid UTF-8 killing `serve`).

**8f repaired after the review of 4d949827.**
- **B1.** A call's arguments are checked against the tool's input schema first: an unknown tool or invalid arguments is the protocol error `-32602`. A refusal is exactly the CLI's, `Refused` or `HomeRefused`, answered with `isError`. Any other exception is a fault, answered `-32603`, and the server keeps serving.
- **Notes taken up.**
  - `update-ref` uses the empty old value, so it creates the ref whatever the hash function. It reports "already exists" only when the ref resolves.
  - The guard also refuses a repository whose common directory lies inside the product's working tree, and anything that is no repository (`TransportRefused`). The scratch's hooks do not run (`core.hooksPath=/dev/null`).
  - `run_ref` checks the full ref with `git check-ref-format` and refuses a `/` in a task id.
  - A client response is not answered. `mcp serve` reads bytes, so a line that is not UTF-8 is a parse error and the server keeps serving.
  - `cli.py`'s duplicate collision check is removed.
- **Not taken up.** `fetch` reading only the tip (N2) stays as is: §16.10 says transport success never implies admissibility, and Admission authenticates against the ledger's issued envelope. A bare `--shared` clone is allowed, since it only borrows reads.
- **Tests.** `test_phase_f_step8f.py`, 14 tests (7 added): a nested repository or no repository refused; no `GIT_*` variable redirecting a write; a SHA-256 scratch repository; malformed ref names; invalid calls as `-32602`; a `HomeRefused` as the CLI's refusal and a fault as `-32603`; a client response unanswered; the pinned revision against a client's other one; serving on after invalid UTF-8 and a refusal.
- **Mutants.** Twelve: all are killed, among them the review's survivors m4, m7 and m8.

**Re-check of 70cef9cf (revision 34).** No SERIOUS CHALLENGE. **PASS**, with one note. B1 is repaired: the re-issued envelope names the original obligation and role, coherent under §12.2, and only step 3's existence half is met by the derived `REISSUE` obligation. Nothing else blocks 8g-ii: once `_resubmitted` discharges `REISSUE`, a second resubmission fails the existence half.
- **Note 1, taken up in 8g-ii.** A resubmission's lineage is checked against the retained record, not the re-issued envelope's launch. The re-issue's route is `MANUAL`: the resubmission launches no session, so no launch is attested for one.

**Step 8g-i built (retry, integration requests and §9.1's re-request; reading F73).**
- **The Dispatcher** (`dispatcher/requests.py`).
  - `integration_request` builds §11.5 (3)'s request: the candidate, the bound `TASK_RESULT`, the base, signed by the task's credential over the request.
  - `rerequest(journal, task, decision, …)` acts only on Admission's outcome. It finishes the old task and returns the new task to issue where derivation finds the obligation `READY` at the new head, else nothing.
- **Mechanical retry** is composition: a finished task whose obligation is still `READY` is issued again at the new head, and none is once derivation stops routing it.
- **Integration under SD-70.** An integration reads the transformation an *admitted* result submits (`integration_frame`), and under SD-70 no `TASK_RESULT` is ever admitted. So the built request, its result bound to its own task and passing authentication, is refused `REF_TRANSFORMATION` before SD-70's own gate. The test asserts that `REJECT`, which admits and integrates nothing, and asserts SD-70's gate at its owner (`gated`): a request carrying a candidate fails closed even when every built check passes, as step 5d's tests do.
- **Tests.** `test_phase_f_step8g_i.py`, 7 tests:
  - retry at the new head, and none once derivation stops routing it;
  - the integrating request built and refused;
  - no second task while Admission's outcome is pending (plan check of 53216046, answer 3);
  - the overtaken basis re-derived and re-issued at the new head;
  - nothing issued when the obligation is no longer ready;
  - only its own obligation re-requested.
- **Mutants.** Seven: all are killed. G03, re-requesting any ready obligation, survived at first and is killed by the last test.

**Step 8g-ii built (a re-issue's resubmission; reading F74).**
- **Admission.**
  - `authenticate.retained` reads, at the request's base, the identities each `REISSUE` obligation lists, each with its retained body, its original envelope (from the binding object stored with the refusal) and its original obligation, derived at the original `issued_at_position`.
  - A record citing a listed identity is authenticated against the retained record, and refused `AUTH_ENVELOPE` unless all of the following hold:
    - the envelope is in force and copies the original's task, obligation, role, contract revision and `governs`;
    - the record's content, apart from `id`, `binding` and `provenance`, equals the retained body;
    - its actor and class equal the retained record's;
    - its binding names the re-issued envelope and otherwise equals the retained binding, so its lineage class and lineage are the original's.
  - Authorization meets the existence half for a request whose every record is a matched resubmission: it judges the role against the original obligation as at its issue. Any other record citing `reissue_of` stays `SCHEMA_UNSUPPORTED`.
- **The Dispatcher.** `reissues` reads the pending `REISSUE` obligations at a named head. `reissue` re-issues the original task by a key in force on the `MANUAL` route. `resubmission` builds the request through `admission.request.resubmitted`, which keeps the body and recomputes the identity.
- **Observation.** When the original obligation is no longer derived, step 7 refuses the request `OBLIGATION_NOT_DERIVED`, and the never-lost record is admitted all the same ("whatever the state of their task", §8.3 step 7). It discharges `REISSUE`, so the adverse report is not lost (F41). No reading is needed: step 7 and step 6's never-lost rule already say so.
- **Tests.** `test_phase_f_step8g_ii.py`, 15 tests:
  - the pending re-issue read;
  - admitted, discharging `REISSUE`, and bound to the original obligation;
  - the same obligations derived as had the original been admitted at the same head;
  - admitted when the original obligation is gone, and a fresh record under the re-issue then refused;
  - a second resubmission not listed;
  - refusals for changed content, actor or lineage, an envelope not copying the original, a key retired before or after it listed the re-issue, a record naming the original envelope, and an unlisted citation;
  - nothing re-issued from an unnamed head.

  The `authorize` stand-ins in four earlier tests take the new optional argument.
- **Mutants.** Sixteen. Fourteen are killed: A05, A06 and D03 survived at first and are killed by the added tests. Two are equivalent:
  - A02, without the actor check: the content comparison covers actor and class;
  - A12, without the original position's range check: an envelope refused at or before the base was issued at or before it.
- **Full suite.** It passes on the tree with 8f's repair, 8g-i and 8g-ii: 1479 tests, 6 skipped.

**Revision 35: step 9 in parts (§3.6, readings F75-F83, Q-F19-Q-F22).** A read-only survey of catalogue §6.5-§6.9, §10.2, §17 and §25 found three derivation stubs (§17.4 admissibility, discriminating-reading coverage, custody in `stale`), no evidence kind accepted at Admission, no machinery binding, runner keys refused, and no runner. It found no SERIOUS CHALLENGE: the evidence obligation's identity is Phase D code diverging from the catalogue (F75), and where runner keys live is a catalogue-internal wording conflict resolved by reading both (F76). Step 9 is split into seven parts, layered so that admissibility exists before Admission accepts evidence. §6's "until Q-F3" residue is corrected, since SD-64 settled it. Four questions go to the stakeholder; none blocks 9a.

**Plan check of 09df7c27 (revision 35).** No SERIOUS CHALLENGE. **NO PASS** on two blockers, both in questions not yet ready to pose. The split and its order are sound. F75 is a faithful implementation correction needing no stakeholder decision. F76-F83 are faithful, and F78's inner shape at step 1 needs no schema change (§8.3 step 1; F46's precedent). F82 is right under SD-70 and SD-71.
- **B1.** Q-F21's numerical contract was incomplete: `REL_TOL`'s formula, `ULP_TOL`'s distance and its infinity override, exact computation, parameter validity and rounded outputs.
- **B2.** Q-F22 confused runner-class availability (the Dispatcher's operational decision) with `AVAILABILITY` records (artifact binding health, §17.4).
- **Answers and notes.** Re-pose Q-F20 without the in-tree tracer point, with (b) sound. Mark 9b's and 9f-ii's dependence on Q-F21 and Q-F20. Split 9c so that F75's migration is reviewed alone, its expected values re-derived from the authority. Name what the issue key signs in Phase F. Cover external custody runners' keys in 9a (note 1). Place one outstanding execution per configuration in 9f-ii (note 2).

**Revision 36: Q-F20-Q-F22 repaired and 9c split after the check of 09df7c27.**
- **B1.** Q-F21's option (a) states the formulas with inclusive bounds, the ULP distance on `float64` only, the non-finite override, exact rational computation, parameter validity as a static error, and rounded outputs compared exactly.
- **B2.** Q-F22 is restated as who records that a referenced artifact is unavailable. 9c-ii builds the derivation side.
- **Answers.**
  - Q-F20 is re-posed on reads outside the tree, recommending (b), hermetic confinement.
  - 9b and 9f-ii name their questions in the fail-closed column.
  - 9c is split into 9c-i (F75's migration, reviewed alone, re-derived from the authority) and 9c-ii.
  - F77 says the issue key signs only envelopes in Phase F, and that external custody keys are `RUNNER` trust roots under the same binding (9a, note 1).
  - F78 records the inner shapes as next-schema notes, read through one owner.
  - 9f-ii holds a second outstanding execution of one configuration (note 2).

**Re-check of 7a53ad06 (revision 36).** No SERIOUS CHALLENGE. **PASS**, with three notes, all taken up before the questions are posed. B1 and B2 are repaired: Q-F21 (a) is a sound contract as numerical method, and Q-F22 concerns artifact binding health. Q-F20's (b) is sound as posed. Nothing blocks 9a.
- **Note 1.** A declared reference or tolerance is read as the exact rational of its decimal text (Q-F21 item 7).
- **Note 2.** `ULP_TOL` on a `rounded:<n>` output is a static error (Q-F21 item 5).
- **Note 3.** Hermetic confinement covers pseudo-filesystems and devices: `/proc` and `/sys` are not mounted, what `/dev` exposes is recorded, and unsupplied entropy is disclosed variation (Q-F20).

**Re-check of 7be4890d (8f's repair).** No SERIOUS CHALLENGE. **PASS**. B1 is repaired and nothing is mis-repaired. Leaving N2 and bare `--shared` clones as they are is accepted.
- **Notes.** The advertised `inputSchema` lacked `"additionalProperties": false`. Two mutants survived: no `core.hooksPath` (f2) and no `/` check in `run_ref` (f5). `json.loads` of bytes also accepts UTF-16 and UTF-32, which is harmless. A product at an ancestor of the scratch is refused, which fails closed.
- **Taken up.** The schema declares `additionalProperties: false`. A planted scratch hook never runs, and `x/y` is refused (both tested).

**Same-family review of 26907956 (8g).** No SERIOUS CHALLENGE. **NO PASS** on three blockers.
- **B1.** A record that was no listed resubmission was admitted under the re-issued envelope as the original actor: in a mixed request while the original obligation stood, and alone after `REISSUE` was discharged.
- **B2.** One retained record could be admitted twice, and provenance was unchecked (`model_family: "forged"` was admitted).
- **B3.** The built integration request carried the `TASK_RESULT`, so the real owner, which reads only an admitted result's transformation, refused it `REF_TRANSFORMATION` whatever SD-70 says.
- **Answers.**
  - Step 7's `OBLIGATION_NOT_DERIVED`, with the never-lost record still admitted and `REISSUE` discharged, is the right reading of §8.3 steps 6-7.
  - The `MANUAL` route is faithful for lineage.
  - A `HUMAN_ATTESTED_FRESH` record was resubmitted with no evidence left for its class.
  - `reissue` bypasses the journal.
  - `rerequest` could check that the decision is its task's.
  - g9, the original position's range check, is equivalent (A12).

**8g repaired after the review of 26907956.**
- **B1.** `authenticate.reissued_tasks` reads, from the refusal entries' stored binding objects, every task ever refused under an unlisted retired envelope. Under an envelope of such a task by a key in force, every record that is not a matched resubmission is `AUTH_ENVELOPE`.
- **B2.**
  - A resubmission's provenance must be exactly the retained provenance with `reissue_of` added, and an identity is cited once per request. Derivation's `_resubmitted` reads the same rule.
  - F74 is tightened to match.
  - A `HUMAN_ATTESTED_FRESH` record is resubmitted only with its co-signer's new attestation.
- **B3.**
  - `integration_request(issued, candidate, base_position, base_commit)` carries no record.
  - F73 is corrected to say so.
  - The test admits the result first, with SD-70's gate lifted for that request alone. The integrating request then reaches the real owner's integration checks: in this fixture, `AUTH_WRITE_SCOPE`, `CONFORMANCE_FAILED` and `OBLIGATION_PREDICATE_UNMET`, since its reviewer task has no contract. It is not `REF_TRANSFORMATION`, and SD-70's gate is asserted at its owner.
- **Not taken up, recorded.** `reissue` signs outside the journal: it is mechanical and immediate, and a key retiring before the resubmission is decided only retains the record again (fail-safe). `rerequest` takes the decision its caller hands it.
- **Tests.**
  - `test_phase_f_step8g_ii.py`, 19 tests: a re-issue carrying only resubmissions; provenance being the retained one, with a citation counted once; a record retained under the original envelope again; the re-attestation of an attested record. Two expectations changed from `SCHEMA_UNSUPPORTED` to `AUTH_ENVELOPE`, because under a re-issue an unlisted citation is B1's.
  - `test_phase_f_step4b.py` gains derivation's provenance case.
  - `test_phase_f_step8g_i.py`'s integration test is rewritten.
- **Mutants.** Ten. Eight are killed, R10 after its test was added. One is equivalent: R03, the once-per-request guard, since with provenance strict, twins are byte-identical and step 2 refuses the duplicate first.
- **Full suite.** It passes: 1484 tests, 6 skipped.

**Re-check of 4f5caedb (8g's repair).** No SERIOUS CHALLENGE. **PASS**. B1-B3 are repaired, nothing is mis-repaired, and the 8f notes are taken up. The scope of `reissued_tasks`, every task ever retained, is right: a later task's id names a later head. The re-attestation is faithful to §5.10 (a) and as strong as 8d.
- **N1.** A record retained as `HUMAN_ATTESTED_FRESH` has no mechanical resubmission: every one is refused, and nothing routes `REISSUE` to a human. The original attester's identity is also lost. Route (i) is chosen: retain the co-signer's verified `LINEAGE_ATTESTATION` with the refusal, and accept the resubmission's class on that retained evidence. It is built as a follow-up to 8g.
- **N2.** Derivation's tightened `_resubmitted` is untested (k4 survives, defence in depth). A direct test is added with N1.

**Step 9a built (runner identity and designation; readings F76-F77).**
- **Trust roots** (`derivation.trust`). Runner keys are read from genesis `runner_keys` and from `KEY_LIFECYCLE` records of role `RUNNER`, with register, rotate, retire and compromise. A runner key retired, rotated away or compromised is in force no more (`former_runners`), and a compromise records its position.
- **The lifecycle path** (`admission.lifecycle`). It admits role `RUNNER` (B6 closed for runner keys). One Ed25519 key serves one role: a key known as an issue key is never registered as a runner key, or the converse. A compromise names a known key of its own role. Admission host keys stay refused.
- **The machinery binding** (`admission.authenticate`), `{"runner": {"key", "signature"}}`.
  - A runner key in force signs the request without its binding.
  - It authenticates only that runner's observations (`REALIZATION`, `CHECK_EXECUTION`, `CUSTODY_ENUMERATION`): unbound, by `machinery:<component>@<key id>` of class `MACHINERY`. Anything else is `AUTH_ACTOR`. An external custody runner's custody identity is such a key.
  - Under any other binding a machinery actor is already `AUTH_ACTOR`, so a runner observation, which is never-lost, is never salvaged without its key. `never_lost` needed no change.
  - Through Admission, a runner's own observation is now refused only by 6c's gate (`SCHEMA_UNSUPPORTED`) until 9d.
- **Designation** (`derivation.state`).
  - `[runners.<class>]` in policy schema 1, closed: `kind` (`DISPATCHER` or `EXTERNAL_CUSTODY`), `keys` (non-empty, distinct), `attributes` (distinct names), and `observes_outside_reads` (boolean). This is a policy key, as 8c's serialization surfaces were.
  - Lint (Phase E E20) finds a verifier naming a runner class policy does not designate. Whether the designated keys are in force is §17.4's admissibility (9c-ii).
- **Fixtures.** The plan fixture's verifiers name runner class `ci`, so its policy designates `ci` (`test_lint.RUNNERS`). Five lint-dependent tests now pass that policy. B6's malformed-key case uses role `ADMISSION`, since `RUNNER` now passes this path.
- **Tests.** `test_phase_f_step9a.py`, 13 tests:
  - keys registered, rotated, retired and compromised;
  - one key, one role;
  - genesis runner keys, with a total reader;
  - a runner authenticating its own observations of each kind, and only those (seven cases);
  - no key in force authenticating nothing (an unknown key, a bad signature, a malformed binding, a retired or compromised key);
  - a machinery actor under a human binding refused;
  - an agent-reported realization refused;
  - through Admission, gated until 9d;
  - designation parsed and its malformed forms refused;
  - the lint.
- **Mutants.** Fourteen. Thirteen are killed. N07 is equivalent: the binding's compromised check, since a compromise already removes the key from those in force.
- **Full suite.** It passes: 1497 tests, 6 skipped (the whole `tests` tree; `tests/ssds` alone holds 1091).

**8g's N1 and N2 built (review of 4f5caedb), with a latent 8d defect found on the way.**
- **N1, route (i).** When a refusal retains a record under an unlisted retired envelope, Admission also retains the co-signer's `HUMAN_ATTESTED_FRESH` attestation of it, which the co-signature authenticated (`authenticate.retained_attestations`). `Retained.attested` reads it back from the refusal entry. A resubmission's class is then accepted on that retained evidence, so the Dispatcher's resubmission stays mechanical (R0) and keeps the original attester. A co-signer's new attestation in the same request remains the fallback.
- **The 8d defect.**
  - Authorization judged the co-signer's `LINEAGE_ATTESTATION` under the task envelope's role, refusing it `AUTH_ROLE_KIND`. So on the co-signed route the bound record was admitted as `HUMAN_ATTESTED_FRESH` while its attestation was refused: the ledger held the class without its evidence. 8d's tests checked authentication only.
  - `authorize` now judges the co-signer's unbound record as the human's own, under no envelope role (`_cosigners`). Authentication admits only that attestation, so nothing else reaches the exemption.
  - A test now takes a co-signed request through Admission and admits both records.
- **N2.** Derivation's tightened `_resubmitted` is pinned by step 4b's provenance case, which kills k4's reversion (R06 above).
- **Tests.**
  - `test_phase_f_step8g_ii.py`, 20 tests: the retained attestation keeping the resubmission mechanical; and, with retention patched out, a new attestation needed.
  - `test_phase_f_step8d.py` gains the co-signed request admitted end to end.
- **Mutants.** Five. Three are killed. Two are equivalent:
  - Q04, the retained attestation's target check: every retained `HUMAN_ATTESTED_FRESH` record was authenticated with its own attestation.
  - Q05, the co-signer check in `retained_attestations`: only the co-signer's attestation survives authentication.
- **Full suite.** It passes: 1499 tests, 6 skipped.

**Same-family review of 47612014 (9a).** No SERIOUS CHALLENGE. **NO PASS** on one blocker.
- **B1.** A ledger loss's `controls` (F56) copied genesis's runner keys instead of the fold, so a loss record could name a compromised runner key as in force and omit one registered since genesis.
- **Answers.**
  - No machinery-actor record is admissible or salvageable without its runner key, by any path (human, task, co-signed, re-issue, candidate).
  - One key per role is sound, and a retired runner key's compromise behaves.
  - `[runners.<class>]` is faithful to §17.5 and §25.3, and a presence-only E20 lint is right, with key state left to §17.4.
- **Notes.**
  - **N1.** Seventeen earlier tests built the plan fixture with `ci` undesignated, so they ran over lint-blocked states.
  - **N2.** A runner's rotation strands its observations in flight, since the actor names the key.
  - **N3.** Two lifecycle rules were untested (n6, n11).
  - Admitted observations at or after a runner key's compromise position must be discounted in 9c-ii.
  - A policy designating key ids that are no runner trust root could show in the ruleset-adoption impact.

**9a repaired after the review of 47612014.**
- **B1.** `loss.controls` folds runner keys: `runner_keys` lists those in force, present when genesis declares it or a lifecycle record has named a runner key, so a ledger that never had one keeps genesis's shape. F56 is reworded.
- **N1.** `accepted_plan`, the budget test and step 4b's `test_nb1` designate `ci`. An instrumented run of the whole suite confirms that only 9a's own lint test now meets the E20 finding.
- **N2, recorded for the runner's runbook (9f-ii).** Before a runner key is retired or rotated away, the runner drains its observations in flight or re-emits them under its new identity. Failures are never-lost, so none may be stranded. No lifecycle listing is needed, since the runner can re-emit.
- **N3.** Tests for an issue-role compromise naming a compromised runner key, and for a later compromise position, both refused.
- **The compromise discount.** It is added to 9c-ii's row.
- **The policy-impact suggestion.** It is left for the ruleset-adoption impact; Phase F does not build that impact.
- **Tests.** `test_phase_f_step9a.py`, 15 tests: the loss controls following the fold (register, rotate, compromise, and a genesis-declared key the fold does not hold), and the compromise rules.
- **Mutants.** Four. All are killed, B03 once its test isolated the role rule from the never-relaxed rule.
- **Full suite.** It passes: 1501 tests, 6 skipped.

**Revision 37: step 9b in detail (readings F84-F86); Q-F21 widened.**
- **F84.** The specification declaration's closed parser and static checks.
- **F85.** Outcomes stored in §17.3's shape, with an embedded verdict as a declared `verdict` output that the declaration names. Phase D's per-output verdict shape is retired and its fixtures re-derived from the authority.
- **F86.** 9b evaluates only `EXACT`. The other six oracles wait for Q-F21, which now also covers `RANGE` and `MONOTONE` (item 8). `SET_EQUAL` waits for a collection form, which §17.3 lacks.

**Plan check of db0bf1ce (revision 37).** No SERIOUS CHALLENGE. **NO PASS** on one blocker. F84's closed parser, its one-declaration rule and the unevaluated templates are faithful. F85 is a faithful reading. Holding `SET_EQUAL` is right.
- **B1.** Q-F21 item 8 evaluated `MONOTONE` over an ordered numeric output, the collection form F86 says §17.3 lacks.
- **Answers.** Use `enum` rather than a new `verdict` type. State how `EXACT`'s reference becomes canonical. `RANGE` must fail a non-finite value at an open bound, and `lo > hi` is a static error. Spell out `MONOTONE`'s orders on infinities, NaN and signed zero. Take S5 §6 cases' stated outcomes as expected values.
- **Notes.** (1) Say what a static error does. (2) Lint `fixed` against the runner class's attributes. (3) Validate the obvious parameter constraints now.

**Revision 38: Q-F21 item 8 and F84-F86 repaired after the check of db0bf1ce.**
- **B1.** `MONOTONE` names a declared ordered list of scalar outputs in its parameters, so it needs no collection form. Item 8, F86 and the 9b row agree.
- **Answers.**
  - An embedded verdict is an `enum` output (`PASS`, `FAIL`), and the `embedded` key goes to the Manual clarification batch.
  - `EXACT`'s reference is canonicalized by the output's canonicalizer, and under `rounded:<n>` must already be canonical.
  - `RANGE` fails a non-finite value unless the bound on that side is that infinity, and `lo > hi` is a static error.
  - `MONOTONE`'s orders are stated.
  - S5 §6 cases' outcomes are expected values.
- **Notes.** A static error makes the specification unit defective: no `REALIZE`, no admissible assessment, a lint finding. `fixed` is linted against the class's attributes. The obvious parameter constraints are checked now.

**Re-check of 93ead500 (revision 38).** No SERIOUS CHALLENGE. **PASS**, with three notes, taken up. B1 is repaired, item 8 is sound as numerical method, and Q-F21 (a) is ready to pose. Nothing blocks 9b.
- **Note 1.** The 9b row's fail-closed cell now holds `SET_EQUAL` for a collection form, not for Q-F21.
- **Note 2.** The 9b row's tests list revision 38's checks.
- **Note 3.** `MONOTONE` names at least two outputs (F84).

**Step 9b-i built (the specification declaration, canonical values and the specification lint; readings F79, F84, F86).** 9b is built in two commits: 9b-i, then 9b-ii (the outcome shape and `EXACT`).
- **`content.spec`.**
  - `spec_declaration(view, unit)` finds exactly one declaration: a fenced `ssds-spec` block in the unit's Markdown regions, or a `*.ssds-spec.toml` file the unit holds whole. None, more than one, or a declaration file held only in part is a failure. `plan.fenced_blocks` is shared with the item parser.
  - `parse_spec` is closed. It checks §17.1's keys, the oracles, the runner, a positive finite bound, outputs of §17.3's scalar forms, and verdicts:
    - an embedded verdict names an `enum` output (`PASS`, `FAIL`) carrying it;
    - a declarative verdict names one of the seven templates, with the obvious parameter constraints (F84);
    - an assessor-read specification declares none.

    It also checks `fixed`, `granularity` and `output_renames`.
  - The canonical texts are an implementation reading of §17.3's forms:
    - `binary64-hex` is `0x` and 16 lower-case hexadecimal digits of the bit pattern;
    - `decimal-shortest` is Python's shortest round-trip `repr`;
    - `rounded:<n>` is the exact decimal value rounded half-even to `n` significant digits, as `Decimal` writes it (`6.67e-1`).

    `is_canonical`, `float_of` and `canonical_reference` read them; `EXACT`'s reference under `rounded:<n>` must already be canonical text.
- **`derivation.specs`** (`State.specs`).
  - It holds each specification unit's declaration, and a revision's declaration from the latest admitted view holding it.
  - `defective` is true for a static error or an unknown revision.
  - `lint` reports `SPEC` (a static error), `RUNNER` (a class policy does not designate), `BOUND` (a Dispatcher class's bound above 168 h) and `FIXED` (a fixed attribute the class does not record).
  - Deriving no `REALIZE` for a defective specification is 9c-ii's, where `REALIZE` is derived. 9b-ii makes no assessment under one admissible.
- **Tests.** `test_phase_f_step9b_i.py`, 9 tests:
  - the three oracles;
  - thirty-four refusals;
  - `ULP_TOL` on a rounded output, and `EXACT`'s reference under rounding;
  - the float forms and their fixed points;
  - each type's canonical values;
  - a block and a file;
  - none, two or a bad declaration being defective;
  - lint against policy, an external custody class excepted from the 168 h bound;
  - an earlier revision's declaration.
- **Mutants.** Sixteen: all are killed. S16, one verdict per output, survived at first and is killed by an added refusal case.
- **Full suite.** It passes: 1510 tests, 6 skipped.

**Re-check of 5f9c7cce (9a's repair) and ce988a56 (8g's N1).** No SERIOUS CHALLENGE. **PASS** on both, with four notes. 9a's B1 and notes are repaired; the reviewer's own E20 instrumentation confirms that only 9a's lint test meets the finding. Route (i) admits no forged evidence: only the co-signature path stores a retained attestation, and `_cosigners` widens nothing beyond the co-signer's authenticated attestation.
- **Note 1.** The genesis-declared runner key case in 9a's loss test patches `Chain.genesis` but not the genesis entry the fold reads, so it does not exercise the case. By reading, a genesis key later compromised is omitted, which is correct. A real test needs a genesis carrying the key, deferred to the step that builds genesis runner keys.
- **Note 2.** A retained attestation is kept as inert bytes with the refusal, not admitted. When the class is shown, the brief and the inspector should point to that refusal entry. Deferred to the interface.
- **Note 3.** q1, q2, q6 and q8 survive, equivalent given authentication (defence in depth).
- **Note 4.** k4 is killed by step 4b's provenance case.

**Step 9b-ii built (outcomes in §17.3's shape, and verdicts through the declaration; readings F83-F86).**
- **`Assessments`** (`derivation.assessment`).
  - The evaluated outcome is read as `{output name: canonical value}`.
  - `declaration(observation)` is the usable declaration of the specification revision it ran under.
  - `failing_outputs` defaults to the outputs the declaration judges, those with a verdict.
  - `restricted` reads the flat outcome.
  - `yields` reads each failing output's verdict through the declaration of the reading in force:
    - an embedded verdict, a declared `enum` output, counts only under the reading the execution ran;
    - `EXACT` is recomputed from the stored outcome under any reading, its reference canonicalized by the output's form;
    - every other template is not computable until Q-F21, so it fails closed;
    - a defective or unknown reading fails closed.
- **Admissibility, and a narrowing of F84's note 1 on the safe side.** A passing assessment under a defective specification revision is not admissible. A failing one still counts, since failing evidence is never dropped by a change (§6) and a specification's defect must not hide adverse evidence. The plan check's note said "no assessment under it is admissible"; this narrowing keeps the adverse side and is put to the review.
- **Phase D's fixture migrated** (`test_assessment.py`). The specification unit holds a `*.ssds-spec.toml` declaration (`EMBEDDED`: output `x`, its verdict carried by `x_verdict`), and `BAD`/`GOOD` are `{x, x_verdict}` outcomes. The expected values are unchanged, still transcribed from `cases_s5_6.py`, so nothing is copied from the new implementation's output. No other test wrote the old shape. The shared fixtures' specification units gain declarations too: `tests.conv` in `test_lint` holds `specs/conv.ssds-spec.toml`, and `test_support`'s `spec.md` carries an `ssds-spec` block. Without one, a specification is defective and its passing assessments no longer count, which thirteen Phase E and support tests showed.
- **Tests.** `test_phase_f_step9b_ii.py`, 5 tests:
  - an embedded verdict counting under the reading it ran (PASS, FAIL, the output missing, another reading);
  - `EXACT` recomputed under any reading, a new reference included;
  - another template and a defective reading failing closed;
  - the judged outputs defaulting to the declared verdicts;
  - a defective specification admitting no passing assessment while a failing one counts.
- **Mutants.** Nine: all are killed. Y07, the declared default, survived at first and is killed once the outcome holds an output with no verdict.
- **Full suite.** It passes: 1515 tests, 6 skipped.

**Revision 39: step 9c-i in detail (reading F87).** The evidence obligation's identity moves to §10.2's `(claim unit lineage, specification unit lineage)`, under one owner (`State.evidence`):
- the token `evidence:<claim root>@<spec root>`;
- required through authored `EVIDENCES` relations where policy's per-domain `evidence = true`;
- a lineage that follows retargets and splits by the region-successor rule, read by `qual` so that no failing assessment is disposed of by change;
- the fixtures re-derived from the authority.

The per-domain `evidence` key changes from a token list to a boolean. No ledger or repository holds one, so it is corrected in place.

**Plan check of 298a12a0 (revision 39).** No SERIOUS CHALLENGE. **NO PASS** on one blocker.
- **B1.** The readable token `evidence:<claim>@<spec>` can exceed schema 1's 200-character token grammar, since unit identities run up to 255 bytes.
- **Answers.**
  - The lineage-root identity is faithful.
  - The boolean is §25.3's reading, and changing it in place is within D4 under F75, not SD-77.
  - The lineage rule is faithful and conservative.
  - The lint matches the catalogue's model.
- **Notes.**
  - A reused name shares identity, which is conservative; say so.
  - Disclose the lint-only choice, and make the stronger rule a question.

**Revision 40: F87 repaired after the check of 298a12a0.**
- **B1.** The token is `evidence:` and the SHA-256 hex of `[claim root, spec root]`, 73 characters, with the readable pair kept beside it.
- **The answers' points.**
  - The in-place correction rests on F75.
  - A specification split is not followed, which is safe.
  - The reused-name case is stated as conservative.
- **Note 2.** The lint-only choice is disclosed, and the stronger rule is Q-F23.

**Re-check of abcd03de (revision 40).** No SERIOUS CHALLENGE. **PASS**, with one note, taken up. B1 is repaired: the 73-character digest token fits schema 1's grammar. Q-F23 is posed correctly. Nothing blocks 9c-i.
- **Note 1.** Q-F23 now says that neither option changes Phase F's behaviour on the shadow ledger.

**Same-family review of a0f2e31b..149d8a9b (9b).** No SERIOUS CHALLENGE. **NO PASS** on two blockers.
- **B1.** An absorbed, never-admitted edit of a specification's `EXACT` reference made a genuine failure stale. `yields` evaluated only the reading in force, missing §6.6's clause: "where the admitted state holds G's specification revision only by absorption, the verdict is also taken under the last revision an admission integrated, and the failure is yielded if either fails".
- **B2.** The canonical texts were not unique:
  - zero under `rounded:<n>` had many texts;
  - `$` let a trailing newline through `_HEX`, `_DIGEST` and `_NAME`;
  - `-NaN` was accepted;
  - `sNaN` crashed `float_of`;
  - `EXACT` and `restricted` compared with Python equality (`1 == True`).
- **Answers.**
  - The parser is faithful apart from B2. `decimal-shortest`'s grammar and its NaN collapse should be written down.
  - `rounded:<n>` must round under an explicit half-even context.
  - `yields` is faithful for computability. Its "either" clause and `output_renames` are unread, both on the safe side.
  - The admissibility narrowing is right, and it differs from 9c-ii's "a fixed-attribute mismatch is inadmissible on either side": that rule is about a declaration that contradicts the run, this one about a declaration that is absent.
  - The fixture migration changed no test's meaning. Every earlier test reaching `yields` takes the embedded path.
- **Notes.** (N1) The specification lint had no consumer. (N2) `declaration_at` was not memoized. An integer reference not exact in binary64 was rounded silently. Two renames could map to one output. The `ENSEMBLE` outcome shape is pending.

**9b repaired after the review of a0f2e31b..149d8a9b.**
- **B1.** `yields` takes the verdict under the reading in force and under `SpecFacts.integrated_rev`, the revision at the last position an admission integrated (genesis's baseline when none has), and yields if either fails. Where the two are equal, this is one reading.
- **B2.**
  - `canonical_float` gives one text per value: every NaN `NaN` under `rounded:<n>`, zero `0.00e+0` with its sign, and half-even under an explicit context.
  - `float_of` accepts a text only if it is exactly the canonicalizer's text for its value, and refuses `sNaN`.
  - Every grammar uses `fullmatch`.
  - `EXACT` requires a canonical stored value and compares canonical JSON bytes, and `restricted` returns canonical JSON text, so identity is type-strict byte equality (§17.3).
- **Notes taken up.**
  - The canonical grammars and the NaN collapse are documented in `content.spec`.
  - An integer reference not exact in binary64 is refused.
  - Two renames to one output are refused.
  - The `ENSEMBLE` outcome shape is named as not built.
  - `declaration_at` is memoized by `(uid, rev)`.
  - `ask(explain)` on a specification unit shows its defect and lint (N1).
  - The "either" clause and `output_renames` stay unread on the safe side, for 9c-ii.
- **Tests.**
  - `test_phase_f_step9b_i.py`, 10 tests: one text per value, two renames to one output, a name with a newline.
  - `test_phase_f_step9b_ii.py`, 10 tests: an absorbed reference edit never making a failure stale, a comment-only absorption changing nothing, an integrated revision relaxing the reference, `EXACT` comparing canonical bytes, and `explain` showing the specification's lint.
- **Mutants.** Fourteen. Twelve are killed. Two are equivalent:
  - R03, `!=` for the byte comparison: `is_canonical` refuses a value of the wrong type first;
  - R12, the NaN branch: `Decimal` drops a float NaN's sign.
- **Full suite.** It passes: 1521 tests, 6 skipped.

**Step 9c-i built (the evidence obligation's identity; readings F75, F87).**
- **One owner** (`derivation/evidence.py`, `State.evidence`).
  - `obligation_token(claim root, spec root)` is `evidence:` and the SHA-256 hex of their canonical JSON (`content.jcs`; derivation imports no Core module).
  - `root` follows `renamed_from` back over every admitted structure.
  - `required(subject)` gives the tokens of the authored `EVIDENCES` relations to claim units inside the subject, when policy's `evidence` is true for its domain.
  - `readable(token)` gives the pair.
  - `required_somewhere` (the latch) and `required_anywhere` (a frame) are also here.
  - `lint` reports `EVIDENCE` (Q-F23).
- **Every site reads the owner.** `Assessments.required_somewhere`, `starts` and `about`, and `briefing`, `queries`, `items`, `support` and `workflow` no longer read a policy token. The per-domain `evidence` key must be a boolean.
- **The brief.** The gate core's required-evidence section shows the readable pair beside the token (`- evidence:… (code evidenced by spec): failing`).
- **Fixtures.**
  - The Phase D, E and later fixtures move to `evidence = true` and the relation-derived token (`test_assessment.OBL`, `test_support.ARCH_CHECK`, `test_phase_e_review.HEALTH`).
  - The Phase E flow's specification declares `# ssds:rel EVIDENCES records`, and the expected values are unchanged.
  - Structure changes in the tests are integrated, not absorbed: an absorbed manifest change is quarantined (§18).
- **Tests.** `test_phase_f_step9c_i.py`, 8 tests:
  - the token bounded and the pair readable;
  - a rename keeping the identity;
  - only the subject a relation reaches requiring it;
  - policy per claim kind, with the token list refused;
  - two specifications giving two obligations that never conflict;
  - retirement keeping the disagreement in `qual`;
  - a retarget to a successor keeping the failure;
  - the `EVIDENCE` lint.
- **Mutants.** Eight. Seven are killed, V03 after its test was added. V06 is equivalent: `about`'s required-obligation clause, since a required obligation's claim lies inside the subject, which `home` already covers.
- **Full suite.** It passes: 1528 tests, 6 skipped, before V03's test was added; that test passes on its own.

**Re-check of 6fedb664 (9b's repair).** No SERIOUS CHALLENGE. **NO PASS**.
- **B2.** Repaired: one text per value, round-trip validation, `fullmatch`, and type-strict byte comparison. t2, the `is_canonical` guard, is equivalent.
- **B1, still open.** Any later unrelated integration made the absorbed revision "the last revision an admission integrated", so the hole reopened on a working ledger. §6.6's revision is per unit: the one an integration that changed the unit produced.
- **B3, new, present since 9b-i.** `parse_spec` raised `OverflowError` on huge TOML integers (a bound, a tolerance, an `EXACT` reference) instead of returning a `SpecFailure`, so any content author could crash every derivation touching `State.specs` (§25.4).
- **Answers and note.**
  - Genesis's baseline is the right fallback, once per unit, with `None` for a unit absent at genesis.
  - In a candidate's frame the second reading is not required, and taking it could deadlock a candidate that legitimately relaxes a specification.

**9b repaired again after the re-check of 6fedb664.**
- **B1.** `SpecFacts.integrated_rev` is per unit. It walks the integrations from the latest back, and returns the revision the first one that changed the unit produced (its view's revision differs from the preceding position's), else genesis's, else `None`. A revision that arrived only by absorption is never taken as integrated.
- **B3.** `parse_spec` returns a `SpecFailure` for any `ArithmeticError`, `ValueError` or `TypeError` a value raises, and `canonical_reference` refuses a reference beyond binary64 as a `ValueError`.
- **The note.** The second reading applies to the admitted state only. In a candidate's frame, the reading in force is the candidate's own.
- **Tests.**
  - `test_phase_f_step9b_i.py` gains three refusals: a huge integer bound, tolerance and reference.
  - `test_phase_f_step9b_ii.py`, 12 tests, adds two: an unrelated integration never making an absorbed edit count, and a candidate relaxing the specification judged under its own reading in its frame (stale there, not in the admitted state).
- **Mutants.** Five. Four are killed, W02 after the frame test was added. W04 is equivalent: `parse_spec`'s backstop catches the overflow.
- **Full suite.** It passes: 1531 tests, 6 skipped.

**Revision 41: step 9c-ii in four parts (readings F88-F95).** A read-only design survey found six things the code does not yet do, each against accepted text and none a SERIOUS CHALLENGE:
- a failing assessment taken as admissible unconditionally, with two consumers that skip the check;
- `ext` ignoring the runner class's read-observation flag;
- `link⁻` leaving out `INCOMPLETE` observations, on the unsafe side;
- currency ignoring the bounding judgments and the realization's target;
- a realization's basis read from whatever its submitter wrote;
- no Stage S case for admissibility, custody or the obligations.

The parts are:
- **9c-ii-i** the reader, admissibility and the migration;
- **9c-ii-ii** currency and binding health;
- **9c-ii-iii** `stale`;
- **9c-ii-iv** the four obligations.

Its proposed readings D1-D8 are F89 (the obligation's revision, the policy at admission, the failing side under a compromise), F92 ("not `T`" as `P`), F93 (custody per class) and F95 (`ASSESS` whatever the currency, a target change through `REALIZE`, the floor subsumed). Each is a reading, put to the plan check.

**Plan check of 4432948d (revision 41).** No SERIOUS CHALLENGE. **PASS**, with six notes, taken up.
- **Faithfulness.** The split and its order are sound. F89 is faithful: its reading of "the revision `e` names" is §17.4's own parenthesis, and the failing side under a compromise is conservative and needs no stakeholder decision. F90-F94 are faithful and safe, and `P` for "not `T`" is right. F95 is faithful.
- **The notes.**
  - The upheld challenge is named first as the route for a forged failure.
  - One-hop renames are disclosed as the coarser, safe choice.
  - `RERUN` takes §6.9's non-derivation condition, ends only on a complete observation, and the Dispatcher bounds retries operationally.
  - 9c-ii's invented cases are marked authority-derived for the exit.

**Re-check of c9af0774 (9b's second repair).** No SERIOUS CHALLENGE. **PASS**. B1 is repaired per unit: an absorbed relaxation stays unstale after one or two unrelated integrations, and an integrated relaxation goes stale. B3 is repaired. The frame note is taken up. Huge-integer `RANGE` bounds parse without crashing, which is acceptable until Q-F21. 9b is closed.

**Same-family review of 09ab5249 (9c-i).** No SERIOUS CHALLENGE. **NO PASS** on one blocker.
- **B1.** The latch `required_somewhere` read the policy in force now at every past position. So a `RULESET_ADOPTION` setting `evidence = false` made `starts` false, and a counted failure stopped counting. This predates 9c-i (Phase D's token code did the same) and survived into the single owner.
- **Answers.** No policy-token reader remains, and every site reads its own subject. The lineage handling is faithful apart from B1, and the fixture migration is mechanical.
- **Notes.**
  - (1) `about`'s second clause (the subject requires the token) is untested; e3 survives.
  - (2) Root collision: after `A` is renamed `B`, a new unit `A` shares `B`'s root while both coexist. That is conservative, and should be disclosed.
  - (3) The tie-break between merged formers is untested.
  - (N4) The `EVIDENCE` lint has no consumer.

**9c-i repaired after the review of 09ab5249.**
- **B1.** `required_somewhere` reads each position under the policy in force there (`h.ruleset(k)`'s policy). A policy that stops requiring evidence retires the obligation and never erases a failure it counted (§10.2).
- **Note 1.** A test moves a claim into a subject that existed at the failure's base: `home` does not add that subject, and the failure counts there through `about`'s second clause.
- **Note 2, disclosed.** While a renamed unit and a new unit of its former name coexist, they share a lineage root and so an obligation token. Failures then count against both, which is conservative. Passing evidence does not leak, since `ev` reads the assessment's realization target and claim.
- **Note 3.** The least-name tie-break among merged formers is deterministic. Its test is left as minor.
- **N4.** `ask(explain)` on a subject shows its `EVIDENCE` lint.
- **Tests.** `test_phase_f_step9c_i.py`, 10 tests: a policy flip keeping a counted failure, a claim moved into an older subject, and the lint shown by `explain`.
- **Mutants.** Three: all are killed, e3 among them (Z02).
- **Full suite.** It passes with 9c-ii-i's working tree: 1546 tests, 6 skipped.

**Step 9c-ii-i built (the realization reader and admissibility; readings F88-F90).**
- **`derivation/realization.py`** reads a `REALIZATION`'s execution under F88's closed inner shape:
  - the basis keys;
  - `runner {class, key}`, with the key the actor's `@<key id>`;
  - `class_attributes` and `observes_outside_reads`, recorded by value;
  - the `start` and `end` positions when recorded;
  - `incomplete` exactly when the outcome is `INCOMPLETE`, as `evaluated` is exactly when it is `COMPLETE`.

  It reports every problem; a realization with one is not well formed.
- **`Assessments.admissible` and `realization_ok`** (F89) are the one owner:
  - (a) the specification and a claim give the obligation, and the assessment's reading shares the specification's root;
  - (b) the instantiated revision's fixed attributes are recorded with their values;
  - (c) the realization is complete, with its outcome stored;
  - (d) the runner class, key and recorded class facts are as the policy and runner trust roots at its admission designate them;
  - (e) its key was not compromised at or before its admission.

  A passing assessment needs all of these. A failing one keeps counting under a defective declaration and under (e).
- **Other readers of admissibility.** Conformance's required evidence reads `realization_ok`, (b)-(e) only: a contract obligation names a specification, not an evidence obligation token. `ADJUDICATE_DISAGREEMENT` and the §6.8 disagreement read admissibility too.
- **`ext`** (F90) treats a realization as having an unpinnable read when it recorded one, when its class does not observe outside reads, when it lacks a recorded class attribute, or when it is not well formed (`Assessments.unpinnable`).
- **Fixtures.**
  - Every scenario genesis declares the runner trust root `ed25519:test` (`_fixtures.RUNNER_ROOT`), and `test_lint.RUNNERS` designates class `ci` for it, observing outside reads.
  - `_scenario.designated` records the runner and class facts by value.
  - The realizations of `test_assessment`, `test_support`, `test_conformance`, `test_phase_f_step4c` and `test_phase_e_review` are by `machinery:…@ed25519:test`, with a stored outcome.
  - The policies of `test_step5_review` and `test_briefs`'s gate designate the class.
  - The expected values are unchanged.
- **Tests.** `test_phase_f_step9c_ii_i.py`, 13 tests: admissibility on both sides; a fixed-attribute mismatch; an incomplete realization; a misfiled obligation; a reading of another specification; an undesignated key or class facts; a compromise dropping passing, never failing, evidence; a retired key's earlier observation still trusted; an agent's realization; the closed shape; the class flag in `ext`; an inadmissible failure deriving no disagreement. `test_conformance` gains an undesignated runner's realization as no required evidence. The expected values are from §6.2, §17.4 and §17.5 (authority-derived).
- **Mutants.** Thirteen. Twelve are killed, X10 and X13 after their tests were added. X12, the assessment's own-obligation check, is equivalent: every caller passes the assessment's own obligation.
- **Full suite.** It passes: 1546 tests, 6 skipped.

**Step 9c-ii-ii built (a realization's currency and binding health; readings F91-F92).**
- **Currency** (`Support.entries`). A `REALIZATION` node has three implicit entries whatever its submitter wrote: its recorded execution basis (`execution`, class `CONSUMER:REALIZATION`), `content` on each claim of its target (`EXACT`), and, through `execution_current`, each bounding completeness judgment's currency. `deps`, `static_deps` and `_evaluate` read `entries`. A realization therefore supports a claim only while its basis holds with its bounding judgments and its target is the claim's revision, and stale passing evidence never discharges (§17.4).
- **Binding health** (`Assessments.unavailable_needed`). A realization needs its evaluated outcome and the references its envelope names, and one of them is unavailable when the latest acting `AVAILABILITY` record on its digest says `UNAVAILABLE`.
  - In `ev`, such a passing assessment contributes at most `P`.
  - Its observation is not standing.
  - Adverse uses are unchanged (`qual` unchanged).
- **Tests.** `test_phase_f_step9c_ii_ii.py`, 8 tests:
  - a current realization;
  - a claim edit making it stale and the evidence not discharging;
  - the target alone making it stale where the basis does not record the claim;
  - a dependency edit;
  - a bounding judgment no longer current;
  - an unavailable outcome held at `P`, its observation not standing, and restored by a later `AVAILABLE`;
  - an unavailable reference leaving adverse use unchanged.

  The expected values are from §17.4 (authority-derived).
- **Mutants.** Six: all are killed. Y2, the claim entry, survived at first and is killed by the target-alone test.
- **Full suite.** It passes: 1553 tests, 6 skipped.

**Re-check of 478901d6 (9c-i's repair).** No SERIOUS CHALLENGE. **PASS**. The policy-flip probe now keeps the failure counted, and the other notes are taken up. A note: `required_somewhere` re-parsed the policy for every position on every call, and a historical policy the current parser refuses would raise. Both are taken up in 9c-ii-i's repair (`state.policy_at`). 9c-i is closed.

**Same-family review of d481277f (9c-ii-i).** No SERIOUS CHALLENGE. **NO PASS** on one blocker.
- **B1.** `standing` did not require the observation trusted and designated (F90's "`standing` also needs the observation trusted (F89 (d)-(e))"). So a reproduction admitted under a key compromised from an earlier position, or under an undesignated key, made a genuine failure stale.
- **Answers.**
  - `admissible` and `realization_ok` are right for assessments.
  - Reading the policy and trust roots at the admission position is right.
  - `ext`'s class rule does not over-narrow.
  - The fixture migration changed no test's meaning: every earlier assessment check stays admissible, 17 passing and 23 failing.
- **Notes.** (1) F88's "adverse uses unchanged" and F89's refusal of a malformed realization disagreed. (2) No test changed the designation after a realization; z5 survived. (3) `observations()` filters nothing, which is right for adverse uses.

**9c-ii-i repaired after the review of d481277f.**
- **B1.** `standing` requires `Assessments.trusted(observation)`: well formed, by `MACHINERY`, under a usable declaration of the revision it instantiated, designated at its admission for that declaration's class, and its key not compromised by then. The adverse conditions still read every observation.
- **Note 1.** F88 says that a malformed realization keeps its adverse *matching* uses and that no assessment of it is admissible.
- **Note 2.** Tests change the designation after a realization in both directions.
- **The 9c-i note.** `state.policy_at(history, position)` parses each policy digest once. An unreadable historical policy designates nothing, and the latch reads it as requiring evidence (each the safe side).
- **Tests.** `test_phase_f_step9c_ii_i.py`, 17 tests, adding four:
  - the control going stale;
  - observations under a key compromised afterwards from an earlier position never making the failure stale;
  - an undesignated runner's observations never making it stale, while the earlier failure stays admissible;
  - a later designation admitting no earlier evidence.
- **Mutants.** Four. All are killed, T2 once the compromise test was made retroactive (a key compromised before an observation is already out of the trust roots there).
- **Full suite.** It passes: 1557 tests, 6 skipped.

**Re-check of cb146b5a (9c-ii-i's repair) and review of 06a20532 (9c-ii-ii).** No SERIOUS CHALLENGE. **PASS** on both. 9c-ii-i and 9c-ii-ii are closed.
- **9c-ii-i.**
  - B1 is repaired: the retroactive compromise keeps the failure unstale, and the failing assessment stays admissible.
  - The notes are taken up.
  - A new note: an unreadable historical policy "designates nothing", which would drop a failing assessment through (d).
- **9c-ii-ii.**
  - F91 is faithful and counts nothing twice.
  - `P` and "latest acting record" are right.
  - No adverse use changes.
- **Notes on 9c-ii-ii.**
  - (1) The implicit entries add static edges, so an equivalence of class `CONSUMER:REALIZATION` that cites the realization by a record entry forms a static cycle, refused `CYCLE_SUPPORT`. This fails closed; a covering equivalence must not cite the realization.
  - (2) `EXACT` content entries still added equivalence edges in `deps`.
  - (3) Ties at one position fell to iteration order.
  - (4) The `acts` filter and the envelope `refs` were untested.
  - A bounding judgment with an `EXACT` basis makes every dependency edit stale its realization, by design, so it needs its own coverage.

**Step 9c-ii-iii built (completing `stale`; readings F93-F94), with the 9c-ii-i and 9c-ii-ii notes.**
- **`link⁻`** (F93). Its anchors range over every admitted observation of the configuration, `INCOMPLETE` ones included. Conditions (2) and (4) compare complete observations. `explain` reads the same anchors.
- **Custody** (F93; `Assessments.custody_ok`). An `EXTERNAL_CUSTODY` class's observation serves conditions (1) and (3) only under all of these:
  - the class's latest acting `CUSTODY_ENUMERATION`, signed by one of its keys;
  - that enumeration lists the observation and every admitted run of the configuration by the class;
  - every run it lists is admitted.

  A `DISPATCHER` class's observation is unaffected.
- **The "either" clause** (F94). Where an observation lacks `x`, or the reading has no verdict on it, the failure is yielded only if `a⁻`'s check on `x` was in force at `a⁻`'s base (the reading's declaration where `a⁻` was admitted). A defective or unknown one counts as in force.
- **Renames** (F94). `_renamed` maps a name one hop through a declaration's `output_renames`. `yields` reads the reading's verdict under its name and the observation's value under its own, and `restricted` reads each observation's own names.
- **The notes taken up.**
  - The adverse side of `realization_ok` treats (d) as met under an unreadable historical policy, so failing evidence is never dropped.
  - `EXACT` content entries add no equivalence edges in `deps`.
  - A tie of `AVAILABILITY` records at one position falls to `UNAVAILABLE`.
  - The `acts` filter and the envelope `refs` are tested.
- **Tests.**
  - `test_phase_f_step9c_ii_iii.py`, 12 tests:
    - an incomplete anchor linking a differing run, and its control;
    - custody: none, the full enumeration, an unlisted run, another run of the class unlisted, an enumerated run not admitted;
    - the "either" clause: a removed admitted check still yielded, an output never checked at the base not yielded;
    - renames: mapped, unmapped, and an outcome read under its own names.
  - `test_phase_f_step9c_ii_ii.py` gains a reference the envelope names and a record not acting.
  - The expected values are from §6.6 and §6.9 (authority-derived).
- **Mutants.** Eleven.
  - Nine are killed: U4 and U7 after their tests were added, and Y7 and Y8 for the notes.
  - U1 and U8 each narrow one condition's anchors and survive. A narrow anchor links symmetrically, so conditions (2) and (4) each catch the case alone. Their joint mutant, U9, is killed.
- **Full suite.** It passes: 1571 tests, 6 skipped.

**Same-family review of babcbd22 (9c-ii-iii).** No SERIOUS CHALLENGE. **NO PASS** on one blocker, a regression this step introduced.
- **B1.** The "either" clause read "the reading does not evaluate x" as "has no declared verdict on x". An assessor-read declaration has no verdicts, so for it every failure fell under the clause, was never yielded, and went stale by mechanics alone. So did a failure on a declared output no verdict checks. §6.6 says a value alone discriminates nothing for an assessor-read oracle, and §6.5 places only an output the reading does not evaluate under the clause. (I had found the assessor-read half while building 9c-ii-iv.)
- **Answers.** The custody rule is faithful, and an unadmitted listed run cannot slip through. "In force at a⁻'s base" should read the base position, which for a frame record is its frame's base. The other changes are sound.
- **Notes.**
  - (1) The enumeration's own trust was not checked.
  - (2) The class-key, latest-enumeration and `acts` checks were untested.
  - (3) The unreadable-policy adverse path was untested.
  - U1 and U8 were not separately covered.

**9c-ii-iii repaired after the review of babcbd22.**
- **B1.** The either clause applies only where G's reading does not declare `x` (after its one-hop rename) or the observation lacks it. It yields only if `x` was a declared output of the reading at `a⁻`'s base, read at `base_position`. Where `x` is declared and present:
  - under an assessor-read reading, it is yielded (until 9e's discriminating readings);
  - under a mechanical reading with no verdict on it, it is not computable and yielded;
  - a defective or unknown reading is yielded.
- **Note 1.** A custody enumeration counts only under the trust a realization needs: `MACHINERY`, under a key the policy and runner trust roots at its own admission designated for the class, and not compromised by then.
- **Tests.** `test_phase_f_step9c_ii_iii.py`, 22 tests, adding:
  - the review's three probes (an assessor-read failure reproduced identically or differently, an unchecked declared output), never stale;
  - a declared output with no verdict yielded, an output removed from the declaration yielded, an output never declared not yielded;
  - an enumeration by a key outside the class, a later partial enumeration deciding, an enumeration not acting;
  - an unreadable historical policy keeping failing evidence and refusing passing;
  - two separating scenarios, condition (2) alone and condition (4) alone, through a narrow incomplete anchor on `other.txt`.
- **Mutants.** Eight. Seven are killed: U1 and U8 now, and E1-E4 and E6 for the notes. E5, the assessor-read branch, is equivalent, since an assessor-read declaration has no verdicts and the no-verdict branch yields; 9e replaces it with the discriminating-reading check.
- **Full suite.** It passes: 1581 tests, 6 skipped.

**Step 9c-ii-iv built (the evidence obligations; reading F95).** `Workflow._evidence_obligations` derives the four in the admitted state only; a frame derives none (SD-70).
- **`REALIZE(e)`, Dispatcher.** Derived for a required `e` (`State.evidence.required`) when no realization serves it. One serves when it is complete, passes `realization_ok`, is current, is not held by an unavailable reference, and covers the current specification and claim revisions. It is not derived for a defective specification. `readiness` waits while the declaration's runner class is undesignated.
- **`ASSESS(realization, e)`, reviewer.** Derived for a complete realization passing `realization_ok` on the adverse side for an obligation latched somewhere, with no acting assessment of it for `e`, whatever its currency.
- **`RERUN(a⁻, on)`, Dispatcher.** Derived for each of `FAILING` and `HERE` whose condition (1) or (3) a counting, admissible, unstale failure without a disposition lacks (`explain`). It is not derived when (2) failed, or when no current completeness judgment bounds the closure: the realization's own bounding judgments, or a current `COMPLETE` judgment of class `EXEC` whose scope covers its basis's units, a fresh one included (§6.9; `_bounded`). It ends on a complete observation of the configuration on that tree with `ext`-equal pins and attributes, whether or not it serves (`_rerun_done`); an `INCOMPLETE` one does not end it.
- **`READING(a⁻)`, reviewer.** Derived for an assessor-read failure that another run observes here, with the class `R3` when a subject it is about is D1 or D2, else `R2`. A failing assessment of that observation's outcome answers it. Its covering discriminating readings are 9e's.
- **Found on the way.** Under an assessor-read reading, the either clause had made every failure stale mechanically. Repaired in 9c-ii-iii's repair (B1 there).
- **Tests.** `test_phase_f_step9c_ii_iv.py`, 16 tests:
  - `REALIZE`: derived and ready; ended and reopened by a claim edit; reopened when its bounding judgment no longer holds; not ended by an incomplete run; none for a defective specification; waiting for an undesignated class.
  - `ASSESS`: until assessed.
  - `RERUN`: both conditions lacking once a fresh completeness judgment bounds the new tree; ended by a complete rerun; ended by an unserving rerun; not ended by an incomplete one; never in a frame; never when it differed or the closure is unbounded.
  - `READING`: answered by a failing assessment, and an assessor-read failure never stale.
  - The floor latched for a D2 failure beside passing evidence, with an incomplete rerun (E34).

  The expected values are from §6.8-§6.9 and §10.2 (authority-derived).
- **Mutants.** Twelve: all are killed. O4, O6 and O8 survived at first and are killed by the added tests.
- **Full suite.** It passes: 1597 tests, 6 skipped.

**Re-check of 9031b16d (9c-ii-iii's repair).** No SERIOUS CHALLENGE. **NO PASS** on one residual in the same predicate.
- **The residual.** A failure whose `failing_outputs` names an output no declaration has (a typo) still went stale. `restricted` read `None` for it everywhere, and the either clause found it undeclared at the base and did `continue`.
- **Answers.** The enumeration trust rule is right. E5 is equivalent. The U1 and U8 separations are adequate.
- **Notes.** The enumeration's trust checks (w1-w3) and the frame base (w5) were untested. Admission (9d) might refuse `failing_outputs` that are no declared output of the reading.

**9c-ii-iii repaired again after the re-check of 9031b16d.**
- **The residual.** `F(a⁻)` is "the declared outputs it found failing" (§6.5). So a failing name that is no declared output of `a⁻`'s own reading, or an own reading that is unusable, yields (fail closed). The earlier test "an output never declared is not yielded" now asserts the reverse.
- **Tests.**
  - An undeclared failing name never stale, under a declarative and an assessor-read reading.
  - An untrusted enumeration: compromised after its admission position, a key that is no runner trust root, an actor that is not `MACHINERY`.
  - A frame record's base being its frame's.

  `test_phase_f_step9c_ii_iii.py` now has 25 tests.
- **Mutants.** Five: all are killed (R1, W1-W3, W5).
- **Routed to 9d.** Admission refuses `failing_outputs` that are no declared output of the assessment's reading, with the record's other shape checks.
- **Full suite.** It passes: 1600 tests, 6 skipped.
