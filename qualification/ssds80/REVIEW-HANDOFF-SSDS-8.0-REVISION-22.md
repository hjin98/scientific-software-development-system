# Independent D3 Review handoff — SSDS 8.0 design revision 22

This is the complete prompt for the independent D3 Review of SSDS 8.0 design revision 22. By stakeholder direction (2026-10-13, decision SD-8), the remaining revise/review cycle runs through fresh-context sub-agent Reviews launched by the authoring session. The sub-agent shares the author's model family, which is a material common-mode dependency that the record must state. The authoring session wrote this handoff. It names the candidate, the governing sources and the method, and gives none of the author's conclusions. Everything below the line is the prompt.

---

You are performing an **independent D3 falsification Review** under the Scientific Software Development Protocol (SSDP), governing version **7.2.1**. You did not author the candidate, and you have none of the authoring conversation. Your job is to try to break the candidate, not to confirm it. Do not modify any file except the one Review record you write. Do not commit or push.

## 1. What you are reviewing

- **Repository (local checkout):** `/home/user/scientific-software-development-system` (GitHub `hjin98/scientific-software-development-system`)
- **Branch:** `ssds-8.0-graph-native-architecture`
- **Candidate commit:** `552ac01bb799c22dece5a33d93bd4244bea21d2a` (design revision 22). Review exactly this commit, by `git show 552ac01bb799c22dece5a33d93bd4244bea21d2a:<path>` or a `git archive` snapshot. Later commits, including the one that adds this handoff, are not part of the candidate.
- **Primary workplan:** `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md` (git blob `8970b617b377756523db1ad783d0863383949fa2` at the candidate)
- **Also in scope:**
  - `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`, SSDS 8.0 section only
  - `tests/test_protocol_80_orchestrator_consolidation.py`
  - `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md`, the stakeholder's recorded instructions
  - `qualification/ssds80/s1_disagreement_model_check.py`, a bounded diagnostic check

**Scope.** Review the whole architecture as it stands at the candidate:

- **(a)** the changes since the previous Review, `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-EF8445A-NO-PASS.md`, which revision 22 presents as a clean local repair restoring a capability that revision 21's simplification dropped:
  - the **discriminating reading** for assessor-read failures (§6.6): one independent assessment recording, in one record, PASS for the frame's observed outcome under the frame's reading and FAIL for the failure's reproduced outcome under its own reading; its refusal rule (one outcome read both ways under one reading), its coverage limits (its own content, the reading it was made under), its class rule (R3 for a D1/D2 failure unless it shows the failure to be the candidate's own) and the reading obligation in scheduling; and the removal of the reading-ground `IMMATERIALITY`;
  - the standing of completeness judgments that bound an observation's basis, and how `stale` reads that S2 value; relaxations held only by absorption; the review-brief item for specification changes (§6.6, §9.6); the floor events for assessor-read failures (§6.6, §7.9); the §7.4 and §10 wording;
  - the stakeholder decision record's new item 7 and SD-9 (`qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md`);
  - the bounded model check, which adds discriminating readings (`DUAL` records), makes its owner-stated predicates independent of the mode under test, restates P10 and narrows P11, and adds the `REV21` sensitivity mode.

  Re-verify each one independently. Attack the repair as a new mechanism, check that it restores the capability without reintroducing what revision 21 removed, and check that every earlier closure, including revision 21's mechanical branch, still holds.
- **(b)** the workflow execution and verification layer (§7.5-§7.10, §9.6-§9.8) and the doctrine-realization objective (§1.1);
- **(c)** the persistence, derivation, concurrency and migration design (§5-§6, §8, §10-§16);
- **(d)** the Protocol 7.2.1 inheritance reconciliation (§0.4, §19, §24).

The changes since the previous Review are `git diff ef8445a3bafb86086546ceff3eaa8b0171dbdb25..552ac01bb799c22dece5a33d93bd4244bea21d2a`. Read them to see what changed, but judge the whole candidate.

## 2. Governing authority

The governing protocol is SSDP **7.2.1**. Its accepted-current identities are owned by `PROTOCOL-RELEASE-STATE.yaml`: public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`. Earlier repairs cite SSDP 6.6 at `22f4bdba53795da3a6f13f162529f3a843fc37ae`. Read governing owners **at those immutable commits** with `git show <ref>:<path>`, not from the branch's working tree:

- `source/roles/software-design/SKILL.md`, the D3 role entrypoint: enter it and follow its routing;
- `source/shared/references/architecture-and-design.md`, read first;
- further owners in `source/shared/references/` as their concern is material: `workflow-and-workplans.md`, `scientific-inspectability-and-initiative.md`, `evidence-evolution-and-dependencies.md`, `abstraction-and-concretization.md`, `semantic-definition-and-traceability.md`, `concurrency-and-orchestration.md`, `storage-and-io.md`, `security-and-trust-boundaries.md`, `protocol-versioning-and-compatibility.md`, `testing-and-validation.md`, `convergence-and-cycle-economy.md`, `project-engineering-memory.md`;
- `PROJECT-ENGINEERING-MEMORY.md`: the PEM predicate fires for this replacement of mature machinery; entries are evidence, not authority, except where a current owner binds them.

Treat as **hypotheses to test, never as authority or evidence of adequacy**: the workplan's self-assessment (§0.1 tables, the §27 passes), commit messages, the authority index's prose, this handoff's description of scope, the bounded model check's green result, and the prior Review records in `qualification/ssds80/` (F9D9DE8,  441CF5C,  8A75346,  FFBAD17,  F3608F5,  AC71FA9,  730490D,  FB3E542,  124B0B7,  97E753F,  4C35D92,  644EB72,  62C0B24,  203A42B,  A414588,  6FE1000,  4EC0024,  BA7F738,  947370D,  EF8445A, all NO-PASS). Reconstruct independently.

**Stakeholder authority.** The stakeholder decision record holds the stakeholder's instructions verbatim. They accept the revision-5 design principles and hold the doctrine-realization objective as an aspiration whose machine limits must be tested. Treat them as task authority; judge whether the design faithfully and adequately realizes them and whether anything attributed to them exceeds what they say. Acceptance of objectives and product scope belongs to the stakeholder, not to D3 Review.

## 3. Method

1. Enter the D3 role as `software-design/SKILL.md` directs. Cite the exact owner text, at the governing commit, for each owner you rely on.
2. **Falsify; don't read for conformance.** Construct concrete trajectories that obey every local rule of the candidate yet violate a governing invariant (§2: S1-S13, C1-C8, K1-K4, P1-P5, A1-A9, G1-G5, M1-M6, T1-T4, B1-B3), an accepted owner, or the stakeholder's recorded direction. For each claimed guarantee, ask what mechanism enforces it and whether a locally compliant actor, a restrictive operation turned permissive, a recovery path or a cross-stratum interaction can defeat it.
3. Re-derive each blocker and finding of `WORKPLAN-REVIEW-SSDS-8.0-EF8445A-NO-PASS.md` against the candidate, and confirm that the earlier Reviews' closed findings stay closed. Also check:
   - whether the derivation strata stay well-founded and single-valued;
   - whether every "impossible" claim holds under the declared trust model;
   - whether the architecture is the minimum justified one;
   - whether it is lossless against `workplans/archive/SSDP-8.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-CONSOLIDATED.md`, `workplans/archive/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE-BEFE678-HYPOTHESIS.md` and the frozen `orchestrator/docs/architecture.md` (§16.2, §18);
   - whether §22 could discriminate the defects it targets, or whether green fixtures could coexist with them (PEM DS-001).
4. Run `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`, `git diff --check ef8445a3bafb86086546ceff3eaa8b0171dbdb25 552ac01bb799c22dece5a33d93bd4244bea21d2a`, and the model check at the candidate (`python3 qualification/ssds80/s1_disagreement_model_check.py`, at `--depth 4` and `--depth 5` (`--jobs N` parallelizes without changing the totals), and again at depth 4 with each of `REV21=1`, `REV20=1`, `REV19=1`, `REV18=1`, `REV17=1`, `REV16=1`, `REV14=1`, `REV13=1`, `REV12=1`, `REV11=1` and `REV10=1`, each of which must report failures on its owner-grounded properties, not only on the oracle). Report results. None of them establishes semantic adequacy.
5. **Convergence review strategy.** Read `source/shared/references/convergence-and-cycle-economy.md` at the governing commit ("Active simplification trigger", "Review strategy after recurrence"). The §6.6 assessment-disagreement family has recurred in every revision since 10. Assess it as a family: whether the candidate's simplification and repair genuinely reduce the failure surface or move it, and whether any capability the removed mechanisms carried is still missing (a capability-transfer check); whether it is the minimum justified concretization of the evidence owner; which common-mode causes remain (including this handoff's framing and the model check's independence from the rule it tests). Route any finding at family level rather than as one sibling per cycle, and prefer repair directions that remove mechanism.
6. Classify every finding by its **earliest owner** as a **blocker** (must be repaired before a PASS) or **non-blocking**. Give each blocker a concrete trajectory and a minimum repair direction; don't redesign the system. Raise a **SERIOUS CHALLENGE** first if accepted governing authority itself is materially false, contradictory, ambiguous, inadequate or unrealizable. Separate genuine blockers from editorial or Manual-level detail: a blocker is a defect that lets a locally compliant actor violate a governing invariant, or a contradiction an implementer cannot resolve without choosing between two owners.
7. Do not manufacture closure, and do not withhold a PASS for issues that belong to the Architecture Manual (§21) or to later gates (§25). A PASS here authorizes nothing by itself; shadow D4 needs gate G2 (§25).

## 4. Output

Write exactly one Markdown file, `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-552AC01-PASS.md` or `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-552AC01-NO-PASS.md`, following the structure of `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-EF8445A-NO-PASS.md`:

1. title and an indented header block: GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE (full SHA), SCOPE, PRIMARY WORKPLAN and blob, governing public-source and recovery refs, prior reviews (hypothesis only), REVIEW METHOD, **REVIEWER** (your model family only, never a model name or identifier, and that you are a fresh-context sub-agent launched by the authoring session);
2. `## SERIOUS CHALLENGE`;
3. `## Verdict` (PASS or NO-PASS);
4. blockers, each with trajectory, violated owner text quoted, earliest owner, minimum repair direction and a required discriminator;
5. non-blocking findings;
6. re-verification of the previous Reviews' findings (closed, partly closed, open), with basis;
7. out-of-matrix trajectories attempted, including those that held;
8. minimum-architecture and capability-transfer assessment;
9. qualification-program adequacy;
10. what you verified and how;
11. what you could not verify;
12. family-level convergence assessment (method step 5);
13. common-mode note: you share the author's model family and were launched by the authoring session from this handoff;
14. D4 statement.

End the file with exactly one trailing newline. Return to the caller only the record path, the verdict and a one-paragraph summary of blockers.
