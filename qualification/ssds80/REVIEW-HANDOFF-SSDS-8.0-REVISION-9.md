# Independent D3 Review handoff — SSDS 8.0 design revision 9

This is the complete prompt for the independent D3 Review of SSDS 8.0 design revision 9. The stakeholder chose a different model family for this Review (stakeholder decision SD-7). Use a fresh context that wrote none of the prior Reviews. If the reviewer is the same model family as an earlier reviewer (the `f3608f5`, `ac71fa9` and `730490d` Reviews were GPT-6/Codex), record that as a common-mode dependency. The authoring session wrote this handoff. It names the candidate, the governing sources and the required method, and gives none of the author's conclusions. Everything below the line is the prompt.

---

You are performing an **independent D3 falsification Review** under the Scientific Software Development Protocol (SSDP), governing version **7.2.1**. You did not author the candidate. Your job is to try to break it, not to confirm it.

## 1. What you are reviewing

- **Repository:** https://github.com/hjin98/scientific-software-development-system
- **Branch:** `ssds-8.0-graph-native-architecture`
- **Candidate commit:** `fb3e542a4430b50efba0b7674d75c93c11fd7d55` (design revision 9). Review exactly this commit. Later commits on the branch, including the one that adds this handoff, are not part of the candidate.
- **Primary workplan:** `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md` (git blob `a3f5369f6139f6f50181f0f0d8500c50824764d0` at the candidate)
- **Also in scope:**
  - `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`, SSDS 8.0 section only
  - `tests/test_protocol_80_orchestrator_consolidation.py`
  - `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md`, the stakeholder's recorded instructions

**Scope.** Review the whole architecture as it stands at the candidate. In particular:

- **(a)** Design revision 9's completion of the transformation contract that `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-730490D-NO-PASS.md` found defective:
  - transformation identity `X = (B, C, A)`;
  - the separation of frame inspection (well-formedness) from enactment (the integrating admission's acceptance condition);
  - the prospective-acceptance rule in `ACC`.

  See §6.9, with §6.3, §6.6, §6.8 steps 3-4, §7.8, §11.2 and §12.2. Revision 9 also defines fence settlement (§15.3) and splits the publication test oracle (§22).

  Check also the continued closure of the earlier Reviews' findings (`AC71FA9`, `F3608F5`, `FFBAD17`), including the revision-8 before-image/output/context roles and ref fencing. Re-verify each one independently, and attack each new mechanism in its own right, not only on the trajectories that motivated it.
- **(b)** The workflow execution and verification layer (§7.5-§7.10, §9.6-§9.8) and the doctrine-realization objective (§1.1).
- **(c)** The persistence, derivation, concurrency and migration design that earlier revisions built (§5-§6, §8, §10-§16).
- **(d)** The Protocol 7.2.1 inheritance reconciliation (§0.4, §19, §24).

The changes since the last Review are the diff `730490db881fa78d6bfd31ba11406e28dc2399ac..fb3e542a4430b50efba0b7674d75c93c11fd7d55`. Read it to see what changed, but judge the whole candidate.

**How to read the files.** If you can clone, run `git clone https://github.com/hjin98/scientific-software-development-system && git checkout fb3e542a4430b50efba0b7674d75c93c11fd7d55`. Otherwise read files pinned to commits, for example:

- `https://github.com/hjin98/scientific-software-development-system/blob/fb3e542a4430b50efba0b7674d75c93c11fd7d55/<path>`
- `https://raw.githubusercontent.com/hjin98/scientific-software-development-system/fb3e542a4430b50efba0b7674d75c93c11fd7d55/<path>`
- the diff: `https://github.com/hjin98/scientific-software-development-system/compare/730490db881fa78d6bfd31ba11406e28dc2399ac...fb3e542a4430b50efba0b7674d75c93c11fd7d55`

If the repository is private and you have no GitHub access, say so and stop. Do not review from memory or from a summary. Record every file you could not read.

## 2. Governing authority

The governing protocol is SSDP **7.2.1**. Its accepted-current identities are owned by `PROTOCOL-RELEASE-STATE.yaml`:

- public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`
- recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`

Earlier design repairs cite SSDP 6.6 at public source `22f4bdba53795da3a6f13f162529f3a843fc37ae`. Read the governing owners **at those immutable commits**, not from the candidate branch's working tree:

- `source/roles/software-design/SKILL.md`, the D3 role entrypoint. Enter it and follow its routing.
- `source/shared/references/architecture-and-design.md`. Read it first, as the entrypoint requires.
- These owners, read when their concern is material:
  - `workflow-and-workplans.md` (review independence, workplans, human gates, Channel C)
  - `scientific-inspectability-and-initiative.md` (delegated findings, tensions, inspection surfaces)
  - `evidence-evolution-and-dependencies.md`
  - `abstraction-and-concretization.md` (authority, Challenge, Lossless Representation)
  - `semantic-definition-and-traceability.md`
  - `concurrency-and-orchestration.md`
  - `storage-and-io.md`
  - `security-and-trust-boundaries.md`
  - `protocol-versioning-and-compatibility.md`
  - `project-engineering-memory.md`

  All are under `source/shared/references/`.
- `PROJECT-ENGINEERING-MEMORY.md`. The Project Engineering Memory (PEM) predicate fires for this replacement of mature machinery. Entries are evidence, not authority, except where a current owner binds them.

Treat the following as **hypotheses to test, never as authority or as evidence of adequacy**:

- the workplan's own self-assessment: §0.1 change tables, "defects found by this revision's own pass", the §27 adequacy and minimum-architecture passes;
- commit messages;
- the authority index's prose;
- this handoff's description of the scope;
- the seven prior Review records in `qualification/ssds80/` (F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5, AC71FA9, 730490D, all NO-PASS).

Reconstruct independently.

**Stakeholder authority.** The stakeholder's 2026-10-13 instructions are recorded verbatim in the stakeholder decision record. They accept the revision-5 design principles and hold the doctrine-realization objective as an aspiration whose machine limits must be tested. Treat those as task authority. Judge two things:

- whether the design faithfully and adequately realizes them;
- whether anything attributed to them exceeds what they say.

Acceptance of objectives and product scope belongs to the stakeholder, not to D3 Review. The 2026-10-12 governing-version adoption exists only as the workplan's paraphrase; the decision record says so.

## 3. Method

1. Enter the D3 role as `software-design/SKILL.md` directs. For each owner you rely on, cite the exact text at the governing commit.
2. **Falsify; don't read for conformance.** Construct concrete trajectories that obey every local rule of the candidate yet violate a governing invariant (§2: S1-S13, C1-C8, K1-K4, P1-P5, A1-A9, G1-G5, M1-M6, T1-T4, B1-B3), the accepted owners, or the stakeholder's recorded direction. For every claimed guarantee, ask what mechanism enforces it, and whether a locally compliant actor can defeat it.
3. At minimum, re-derive each `730490d` blocker (A-B) and finding (N1-N4), and each `ac71fa9`, `f3608f5` and `ffbad17` blocker, against the candidate. Attack each repair as a new mechanism, not only on the trajectory that motivated it. Also check:
   - whether the derivation strata stay well-founded and single-valued with the revision-6 changes: syntactic polarity in S1; the `PLAN_CONTROL` order inside S2 `sat`; transformation frames `D_n[X]` with hypothetical tree and structure beside `D_n`, frame existence without acceptance, and the prospective-acceptance clause of `ACC`; S3 classifications consumed by Admission;
   - whether every claim to make a failure class "impossible" holds under the declared trust model;
   - whether the architecture is the **minimum justified** one (anything added that the problem does not need, or missing that it does);
   - whether it is **lossless** against its archived predecessors: `workplans/archive/SSDP-8.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-CONSOLIDATED.md`, `workplans/archive/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE-BEFE678-HYPOTHESIS.md`, and the frozen `orchestrator/docs/architecture.md` (Architecture 1.6.0), per workplan §16.2 and §18;
   - whether the §22 qualification program could discriminate the defects it targets, or whether green fixtures could coexist with them (PEM entry DS-001).
4. If you can execute: run `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` and `git diff --check 730490d fb3e542`. Report results, or report that you could not run them. A frontmatter test cannot establish semantic adequacy.
5. Classify every finding by its **earliest owner** (the workplan section, or an accepted SSDP owner) as one of:
   - **blocker:** must be repaired before a PASS;
   - **non-blocking:** should be repaired in or before the next revision.

   Give each blocker a concrete trajectory and a minimum repair direction; don't redesign the system for the author. If accepted governing authority itself is materially false, contradictory, ambiguous, inadequate or unrealizable for this decision, raise a **SERIOUS CHALLENGE** first and route it to the earliest affected owner.
6. Do not manufacture closure. A PASS here authorizes nothing by itself. Under the candidate's §25, shadow implementation (D4) needs gate G2: an accepted Architecture Manual, a reviewed shadow workplan and stakeholder authorization. Judge whether those gates are themselves coherent.

## 4. Output

Produce exactly one Markdown document, the Review record, named `WORKPLAN-REVIEW-SSDS-8.0-FB3E542-PASS.md` or `WORKPLAN-REVIEW-SSDS-8.0-FB3E542-NO-PASS.md`. Return its full content so the stakeholder can commit it to `qualification/ssds80/`. Follow the structure of `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-730490D-NO-PASS.md`:

1. Title.
2. An indented header block:
   - GOVERNING SSDP 7.2.1
   - REPOSITORY
   - BRANCH
   - CANDIDATE (full SHA)
   - SCOPE
   - PRIMARY WORKPLAN and its blob, if you can verify it
   - governing public-source and recovery refs
   - prior reviews (hypothesis only)
   - REVIEW METHOD
   - **REVIEWER: your model name and version**
3. `## SERIOUS CHALLENGE`.
4. `## Verdict` (PASS or NO-PASS).
5. Blockers, each with:
   - its trajectory;
   - what it violates, with the owner text quoted;
   - its earliest owner;
   - a minimum repair direction.
6. Non-blocking findings.
7. Re-verification of each `730490d`, `ac71fa9`, `f3608f5` and `ffbad17` finding: closed, partly closed, or open, with your basis.
8. Out-of-matrix trajectories attempted, including those that held.
9. Minimum-architecture and capability-transfer assessment.
10. Qualification-program adequacy.
11. What you verified and how.
12. What you could not verify. Be explicit about anything you could not open or run.
13. Common-mode note: you are a different model family from the author, reviewing from a handoff the author wrote; state any dependency that remains, such as shared sources or the handoff's framing.
14. D4 statement.

Be decision-sufficient and lossless, without padding. Every claim about the candidate should cite its section. Every claim about governing doctrine should cite the owner file at the governing commit.
