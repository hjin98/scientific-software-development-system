# Independent D3 Review handoff — SSDS 8.0 design revision 21

This is the complete prompt for the independent D3 Review of SSDS 8.0 design revision 21. By stakeholder direction (2026-10-13, decision SD-8), the remaining revise/review cycle runs through fresh-context sub-agent Reviews launched by the authoring session. The sub-agent shares the author's model family, which is a material common-mode dependency that the record must state. The authoring session wrote this handoff. It names the candidate, the governing sources and the method, and gives none of the author's conclusions. Everything below the line is the prompt.

---

You are performing an **independent D3 falsification Review** under the Scientific Software Development Protocol (SSDP), governing version **7.2.1**. You did not author the candidate, and you have none of the authoring conversation. Your job is to try to break the candidate, not to confirm it. Do not modify any file except the one Review record you write. Do not commit or push.

## 1. What you are reviewing

- **Repository (local checkout):** `/home/user/scientific-software-development-system` (GitHub `hjin98/scientific-software-development-system`)
- **Branch:** `ssds-8.0-graph-native-architecture`
- **Candidate commit:** `ef8445a3bafb86086546ceff3eaa8b0171dbdb25` (design revision 21). Review exactly this commit, by `git show ef8445a3bafb86086546ceff3eaa8b0171dbdb25:<path>` or a `git archive` snapshot. Later commits, including the one that adds this handoff, are not part of the candidate.
- **Primary workplan:** `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md` (git blob `9db8178b5894b4518517aaf69819f3e556711916` at the candidate)
- **Also in scope:**
  - `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`, SSDS 8.0 section only
  - `tests/test_protocol_80_orchestrator_consolidation.py`
  - `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md`, the stakeholder's recorded instructions
  - `qualification/ssds80/s1_disagreement_model_check.py`, a bounded diagnostic check

**Scope.** Review the whole architecture as it stands at the candidate:

- **(a)** the changes since the previous Review, `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-947370D-NO-PASS.md`, which revision 21 presents as a simplification pass under the convergence owner:
  - the removal of the pair as a supersession record, together with its Admission authorization, the withdrawal latch, `here`, the reading pair, the Dispatcher run enumeration, the decision-class pair exceptions and the floor deferral (§6.6, §6.8 step 3, §7.5, §7.9, §10);
  - the derived test `stale_G` (§6.6): reproduction, no other outcome on the failure's own content, a standing observation of the frame's content, no observation there yielding the failure under the frame's reading (mechanical verdict or assessor-read identity), and its polarity rule (permissive inputs must stand, restrictive inputs are read whatever their standing); "in force at the base"; the reading ground of `IMMATERIALITY` (R2); the floor as an event on ledger facts; the deliberate change for accepted relaxations under a mechanical oracle;
  - the execution-basis, external-read and attribution changes (§6.6, §6.8 step 3);
  - the bounded model check `qualification/ssds80/s1_disagreement_model_check.py`, which now has mechanical and assessor-read failures with a verdict function per reading, a tightened reading that can be admitted, relaxed and restored, four outcome values, owner-stated P13, Q and Q2, P10 read on the undisputed term, a `--jobs` option, and the `REV20` sensitivity mode.

  Re-verify each one independently. Attack the simplification as a whole, not only on the trajectories that motivated it, and check that every earlier closure the removed mechanisms carried still holds.
- **(b)** the workflow execution and verification layer (§7.5-§7.10, §9.6-§9.8) and the doctrine-realization objective (§1.1);
- **(c)** the persistence, derivation, concurrency and migration design (§5-§6, §8, §10-§16);
- **(d)** the Protocol 7.2.1 inheritance reconciliation (§0.4, §19, §24).

The changes since the previous Review are `git diff 947370d31fbd7bc53272bdbc401244624137c855..ef8445a3bafb86086546ceff3eaa8b0171dbdb25`. Read them to see what changed, but judge the whole candidate.

## 2. Governing authority

The governing protocol is SSDP **7.2.1**. Its accepted-current identities are owned by `PROTOCOL-RELEASE-STATE.yaml`: public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`. Earlier repairs cite SSDP 6.6 at `22f4bdba53795da3a6f13f162529f3a843fc37ae`. Read governing owners **at those immutable commits** with `git show <ref>:<path>`, not from the branch's working tree:

- `source/roles/software-design/SKILL.md`, the D3 role entrypoint: enter it and follow its routing;
- `source/shared/references/architecture-and-design.md`, read first;
- further owners in `source/shared/references/` as their concern is material: `workflow-and-workplans.md`, `scientific-inspectability-and-initiative.md`, `evidence-evolution-and-dependencies.md`, `abstraction-and-concretization.md`, `semantic-definition-and-traceability.md`, `concurrency-and-orchestration.md`, `storage-and-io.md`, `security-and-trust-boundaries.md`, `protocol-versioning-and-compatibility.md`, `testing-and-validation.md`, `convergence-and-cycle-economy.md`, `project-engineering-memory.md`;
- `PROJECT-ENGINEERING-MEMORY.md`: the PEM predicate fires for this replacement of mature machinery; entries are evidence, not authority, except where a current owner binds them.

Treat as **hypotheses to test, never as authority or evidence of adequacy**: the workplan's self-assessment (§0.1 tables, the §27 passes), commit messages, the authority index's prose, this handoff's description of scope, the bounded model check's green result, and the prior Review records in `qualification/ssds80/` (F9D9DE8,  441CF5C,  8A75346,  FFBAD17,  F3608F5,  AC71FA9,  730490D,  FB3E542,  124B0B7,  97E753F,  4C35D92,  644EB72,  62C0B24,  203A42B,  A414588,  6FE1000,  4EC0024,  BA7F738,  947370D, all NO-PASS). Reconstruct independently.

**Stakeholder authority.** The stakeholder decision record holds the stakeholder's instructions verbatim. They accept the revision-5 design principles and hold the doctrine-realization objective as an aspiration whose machine limits must be tested. Treat them as task authority; judge whether the design faithfully and adequately realizes them and whether anything attributed to them exceeds what they say. Acceptance of objectives and product scope belongs to the stakeholder, not to D3 Review.

## 3. Method

1. Enter the D3 role as `software-design/SKILL.md` directs. Cite the exact owner text, at the governing commit, for each owner you rely on.
2. **Falsify; don't read for conformance.** Construct concrete trajectories that obey every local rule of the candidate yet violate a governing invariant (§2: S1-S13, C1-C8, K1-K4, P1-P5, A1-A9, G1-G5, M1-M6, T1-T4, B1-B3), an accepted owner, or the stakeholder's recorded direction. For each claimed guarantee, ask what mechanism enforces it and whether a locally compliant actor, a restrictive operation turned permissive, a recovery path or a cross-stratum interaction can defeat it.
3. Re-derive each blocker and finding of `WORKPLAN-REVIEW-SSDS-8.0-947370D-NO-PASS.md` against the candidate, and confirm that the earlier Reviews' closed findings stay closed. Also check:
   - whether the derivation strata stay well-founded and single-valued;
   - whether every "impossible" claim holds under the declared trust model;
   - whether the architecture is the minimum justified one;
   - whether it is lossless against `workplans/archive/SSDP-8.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-CONSOLIDATED.md`, `workplans/archive/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE-BEFE678-HYPOTHESIS.md` and the frozen `orchestrator/docs/architecture.md` (§16.2, §18);
   - whether §22 could discriminate the defects it targets, or whether green fixtures could coexist with them (PEM DS-001).
4. Run `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`, `git diff --check 947370d31fbd7bc53272bdbc401244624137c855 ef8445a3bafb86086546ceff3eaa8b0171dbdb25`, and the model check at the candidate (`python3 qualification/ssds80/s1_disagreement_model_check.py`, at `--depth 4` and `--depth 5` (`--jobs N` parallelizes without changing the totals), and again at depth 4 with each of `REV20=1`, `REV19=1`, `REV18=1`, `REV17=1`, `REV16=1`, `REV14=1`, `REV13=1`, `REV12=1`, `REV11=1` and `REV10=1`, each of which must report failures on its owner-grounded properties, not only on the oracle). Report results. None of them establishes semantic adequacy.
5. **Convergence review strategy.** Read `source/shared/references/convergence-and-cycle-economy.md` at the governing commit ("Active simplification trigger", "Review strategy after recurrence"). The §6.6 assessment-disagreement family has recurred in every revision since 10. Assess it as a family: whether the candidate's simplification genuinely reduces the failure surface or moves it; whether it is the minimum justified concretization of the evidence owner; which common-mode causes remain (including this handoff's framing and the model check's independence from the rule it tests). Route any finding at family level rather than as one sibling per cycle, and prefer repair directions that remove mechanism.
6. Classify every finding by its **earliest owner** as a **blocker** (must be repaired before a PASS) or **non-blocking**. Give each blocker a concrete trajectory and a minimum repair direction; don't redesign the system. Raise a **SERIOUS CHALLENGE** first if accepted governing authority itself is materially false, contradictory, ambiguous, inadequate or unrealizable. Separate genuine blockers from editorial or Manual-level detail: a blocker is a defect that lets a locally compliant actor violate a governing invariant, or a contradiction an implementer cannot resolve without choosing between two owners.
7. Do not manufacture closure, and do not withhold a PASS for issues that belong to the Architecture Manual (§21) or to later gates (§25). A PASS here authorizes nothing by itself; shadow D4 needs gate G2 (§25).

## 4. Output

Write exactly one Markdown file, `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-EF8445A-PASS.md` or `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-EF8445A-NO-PASS.md`, following the structure of `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-947370D-NO-PASS.md`:

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
