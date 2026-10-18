# Independent D3 Review handoff — SSDS 8 Architecture Manual, candidate f044820 (G1, architecture level)

This is the complete prompt for the independent D3 Review of the sixty-second candidate of the proposed SSDS 8 Architecture Manual (Phase C, gate G1). It replaces the earlier handoffs' scope. The stakeholder asked for a GPT-family Review; the record states its family and how the reviewer was engaged.

**Why this Review differs from the last sixty-one.** The Manual went through 61 Review rounds without converging: each round closed its blocker and found a close relative, and each repair added mechanism. The stakeholder chose consolidation instead of further repair (SD-47, stakeholder decision record item 43, quoted verbatim there). The candidate therefore makes three changes. (A) One judged-content rule decides what every review and conformance judgment judges and whom its judge must be independent of (Manual §5.10 (b)), with three typed review targets (§3.4). (B) The workplan's G1 bar now judges the architecture: a counterexample to a mechanism that leaves the architecture intact is a residual-register entry closed at G2 at the same no-blocker bar, while an architectural contradiction, an unrealizable or omitted invariant or decision, or an inadequate Manual decision stays a G1 blocker (workplan design revision 24, §25 criterion 11). (C) The exact mechanism moved out of the Manual into a non-authoritative mechanism catalogue carried to G2. Judge the candidate under that bar. Do not lower it, and do not raise it back to mechanism level: where you find a mechanism defect, classify it by the bar and say why.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, a full clone with complete history; paths below are relative to its root.
- **Branch:** `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `f04482003cc46e8bf0d1fddd0cff3099e85e7c5f`. Review exactly this commit, by `git show f04482003cc46e8bf0d1fddd0cff3099e85e7c5f:<path>` or a `git archive` snapshot. Later commits, including the one adding this handoff, are not part of it.
- **Primary subject:** `orchestrator/docs/ssds-8.0-architecture.md` (blob `b3958a4a3e1e8a7292557b81638573dae3f7a14b`), the proposed Manual, now architecture-level. It keeps candidate 61's section numbering; several sections are candidate 61 text unchanged where that text was already architecture.
- **Parent contract, in scope for its delta:** `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md` (blob `2e1afae196e70d51a98c3daeb1aa2ff22f3be4b6`), design revision 24. Revision 23 is the Phase B semantic candidate `e23f14208be869e6a78cfd7b312e447254ee1851` (blob `610f373b97fb8152d2a5742e17fa172e12204756`), reviewed PASS in `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md`. Revision 24 (`git diff 94316298ba0d40831560591c2d2385544b93ea42 f04482003cc46e8bf0d1fddd0cff3099e85e7c5f -- workplans/`) changes only its disposition block, §0.1, the §21 preamble and §25 criteria 2, 4, 11 and 13. It is unreviewed: review it here.
- **Mechanism catalogue, in scope only as stated in §3:** `orchestrator/docs/ssds-8.0-mechanism-catalogue.md` (blob `c73c8c6fa245a76dfe2b34fa7b92d332d0f83bb5`): its front part (C.1 reading rules, C.2 residual register RR-1 to RR-10) and, as its body, the candidate 61 Manual text verbatim.
- **Review aid (not authority):** `qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md` (blob `8d694a726168ba8d32c08dc1093b1c3e4c9d1097`).
- **Previous Manual Review records:** `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-*.md`, 61 NO-PASS records and one PASS (candidate 38, later countered). The latest is the GPT-family `MANUAL-REVIEW-SSDS-8.0-9431629-DIFFERENT-FAMILY-NO-PASS.md` (B1, item-level review independence; N1-N4). Closure map §7 gives the lineage.
- **Stakeholder decisions:** `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` (items 1-43 verbatim; SD-1 to SD-47).
- **Also relevant:** `qualification/ssds80/PHASE-C-HANDOFF-SSDS-8.0.md` (what the Manual owes); `orchestrator/docs/architecture.md` (frozen Architecture 1.6.0, blob `39e6de727f6c35402962509d30d947962992eaad`); `qualification/ssds80/judgment_disagreement_model_check.py` and `qualification/ssds80/item_review_history_probe.py` (diagnostics of the catalogue); `PROJECT-ENGINEERING-MEMORY.md`; `tests/test_protocol_80_orchestrator_consolidation.py`.

## 2. Governing authority

Governing protocol: SSDP **7.2.1**. Accepted-current identities are owned by `PROTOCOL-RELEASE-STATE.yaml`: public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`. Read governing owners at the public-source commit with `git show <ref>:<path>`: the D3 entrypoint `source/roles/software-design/SKILL.md` (expanded in `dist/skills/software-design/SKILL.md`); `source/shared/references/architecture-and-design.md` and `abstraction-and-concretization.md`; `convergence-and-cycle-economy.md` (in particular its rules that simplification comes before another additive repair and that escalation changes the method, never the pass threshold); and further owners as their concern becomes material (workflow, evidence, semantic definition, PEM, storage, concurrency, security, versioning, testing, scientific inspectability). For the doctrine-realization map, every role and specialist entrypoint and `source/shared/fragments/scientific-checks.md`.

Treat as hypotheses to test, never as authority or evidence of adequacy: the previous Review records and their repair directions; the Manual's refinement table, decision markers, minimum-architecture pass and qualification claims; the catalogue and its register; the closure map; commit messages; this handoff; the diagnostics' results. The stakeholder decision record holds instructions verbatim: judge whether the candidate realizes them faithfully and whether anything attributed to them exceeds what they say. Acceptance of the Manual, of workplan revision 24, of default values and of product scope belongs to the stakeholder, not to this Review.

## 3. What to judge

1. **Workplan revision 24 and the G1 bar.** Whether the revision is a sound level assignment (D3 architecture at G1, mechanism with executable models at G2) that keeps every reviewed obligation visible and every gate's criteria satisfiable by work earlier gates authorize (workplan §22 "Authorization boundaries"), or whether it weakens an accepted owner's requirement or a pass threshold. If you find the bar itself defective, raise a SERIOUS CHALLENGE against it with its basis, rather than reviewing under a bar you consider invalid.
2. **Closure at the architecture level.** For each workplan §21 item and clause and each §16.2 row: whether the Manual decides it at the architecture level (owning component, authority boundaries, invariants kept, the decision chosen, why some mechanism realizes it), not merely routes it to the catalogue. A route to the catalogue is closure only where the item's architecture decision is stated here.
3. **Fidelity and refinements.** Whether the Manual restates the reviewed contract without silent semantic change, whether each §0.3 refinement is sound and kept at its architecture meaning, and whether the condensation from candidate 61 lost or changed any architecture decision (compare with the catalogue body, section by section, where you suspect a loss).
4. **The judged-content rule and review targets (SD-47 A).** Whether §5.10 (b), with §3.4's three target types, is one coherent rule read identically by reach, relief and independence; whether it satisfies A5 and A9 on the 9431629 B1 trajectories (empty, partial and all-empty re-dispatch; re-partition) and on the SD-46 diagnostic cases (a part a re-partition replaced; a copy under the same prose and fixed fields); whether it over-excludes judges (a replaced producer, a same-key item in another scope, another item's content in the scope); whether its consequences for drift, cross-plan copies and changed prose are stated (§32.2); and whether "a judgment supports an integration only for the content it judged" is a sound architecture-level form of the catalogue's staleness rules.
5. **Adequacy (out of matrix).** Whether a conforming realization can satisfy every decision here and still violate a governing invariant. This is the main G1 question.
6. **Realizability.** Whether each decision here is realizable by some mechanism. The catalogue body and the diagnostics are evidence for this only: a catalogue clause that disagrees with the Manual, or a catalogue mechanism with a counterexample, is a register entry, not a G1 blocker, unless it shows that no mechanism can realize the Manual's decision.
7. **Register completeness.** Whether catalogue C.2 lists every known open mechanism question the earlier Reviews raised and the candidate has not closed at the architecture level. A missing entry is a non-blocking finding; a register entry that is really an architecture defect is a G1 blocker.
8. **Inheritance and capability transfer** against Architecture 1.6.0, workplan §18 and the PEM Historical Applicability Set; **qualification design** (§31) and the **doctrine-realization map** (§29); **O1** content and product-scope marks (§0.5).

You need not replay each mechanism-level finding of the 61 earlier records: they are register entry RR-9, for G2. Do check that no architecture-level finding of those records is reopened by the condensation.

## 4. Method

1. Enter the D3 role as `software-design/SKILL.md` directs and cite exact owner text for each owner you rely on.
2. Reconstruct independently; falsify rather than read for conformance; run a bounded Challenge Pass.
3. For a blocker, characterize its family with cheap sibling variants and route one family-level problem. Prefer repair directions that remove or narrow mechanism. Classify every finding: **G1 blocker** (the workplan §25 criterion 11 definition, with a concrete trajectory or contradiction and the violated owner text), **register entry** (a mechanism question for G2, naming the RR entry it belongs to or proposing a new one), or **non-blocking**. Never classify by how often a family recurred.
4. Run at the candidate: `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`; `git diff --check 94316298ba0d40831560591c2d2385544b93ea42 f04482003cc46e8bf0d1fddd0cff3099e85e7c5f`; `python3 -I qualification/ssds80/item_review_history_probe.py`; at least the core and `review-scope` families of `python3 -I qualification/ssds80/judgment_disagreement_model_check.py` (the full `--mutations` run takes about eighty minutes serially; its families can be run in parallel by importing the module); and confirm that `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee410ab9df0d94740cebb6969e161911b126`. These are structural or diagnostic checks, never adequacy evidence.
5. Do not manufacture closure, and do not withhold a PASS for evidence that belongs to G2-G4. A PASS here is technical evidence for G1 only: it accepts no architecture, workplan revision, product scope or default value and authorizes no D4.

**Scientific checks for this Review.** This task reviews D3 authority for software that mediates scientific evidence and produces, runs or reviews no realized scientific results. State your material findings or that you have none; state that you produced, ran or reviewed no realized results (or give a null envelope); state whether you evaluated more than one variant of anything and, if so, count, kind and criterion; and, if you relied on accepted D1/D2 authority for a consequential judgment, report your tension search. Report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the Manual author's (Claude) family, `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-F044820-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-F044820-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Structure it as:

1. title and an indented header block: GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE (full SHA), SCOPE, MANUAL blob, PARENT WORKPLAN (revision 24 and the Phase B candidate), public-source and recovery refs, prior reviews (hypotheses only), REVIEW METHOD, **REVIEWER** (model family only, never a model name or identifier, and how you were engaged);
2. `## SERIOUS CHALLENGE`;
3. `## Verdict` (PASS or NO-PASS);
4. G1 blockers, each with trajectory or contradiction, violated owner text quoted, earliest owner, minimum repair direction and a required discriminator;
5. register entries (new or confirmed), each with its RR number or a proposed one;
6. non-blocking findings;
7. the workplan revision 24 assessment (§3 item 1);
8. closure audit at the architecture level: §21 items and §16.2 rows not decided here, or "none found" with the basis;
9. assessment of each §0.3 refinement and of the SD-47 changes (§3 item 4);
10. out-of-matrix trajectories attempted, including those that held;
11. minimum-architecture and capability-transfer assessment;
12. qualification-design adequacy;
13. doctrine-realization map and O1 assessment;
14. what you verified and how; what you could not verify;
15. scientific-checks answers;
16. common-mode note: your model family relative to the Manual author's (Claude) and to earlier reviewers (several, including the Phase B reviewer and the 9431629 reviewer, of the GPT family; most others of the Claude family), how you were engaged, and the dependencies you still share;
17. D4 statement.

Write scratch files only under a directory named `ssds80-manual-review-f044820` inside `$TMPDIR`. End the file with exactly one trailing newline. Return to the caller only the record path, the verdict and a one-paragraph summary of blockers, with each blocker's family.
