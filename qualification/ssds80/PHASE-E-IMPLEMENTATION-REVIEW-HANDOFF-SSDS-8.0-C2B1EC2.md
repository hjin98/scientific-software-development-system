# Independent re-Review handoff — SSDS 8 Phase E, repaired candidate c2b1ec2

This is the complete prompt for one independent re-Review of SSDS 8 Stage D Phase E after the repair of the re-Review of `9c7d77d`. It is deliberately narrow. Judge whether that re-Review's two blockers, E-R4 and E-R5, are closed at their owners, together with the blockers same-family checks of their repairs found, without new defects; and whether anything found closed earlier has regressed. The re-Review accepts nothing. A Phase E PASS lets Phase F's dependent work start (G2 workplan §5.1 item 5); acceptance of the implementation is G3.

**Context.** The re-Review of `9c7d77d` (`qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-9C7D77D-DIFFERENT-FAMILY-NO-PASS.md`) closed E-R3 and the consolidated settlement rule. It left two blockers:
- **E-R4.** The no-part decision brief omitted the standing adverse review's identity, outcome, target and findings (Manual §16.7).
- **E-R5.** An unresolved part selector counted as naming a part, so the principal decision was lost and the item returned to an already answered review.

The repairs and the same-family checks that followed:
- **`17b22d71`** repaired E-R4 and E-R5. A same-family check of it found:
  - **N-1**: a late review naming a part that a later whole partition dropped left the item `DISCHARGED`;
  - **N-2**: a finding without a selector, beside a valid one, was ignored;
  - **P2**: an objection on a replaced part retired when one descendant was redone.
- **`eccd24bd`** repaired N-1, N-2 and P2. A same-family check of it found:
  - **B-S8**, predating this line: an objection naming no part retired on a later review of an *older* result;
  - **N-a**: a partly dropped named branch retired the objection.
- **`c2b1ec27`** repaired B-S8 and N-a.

The Phase E plan records each step: §5, the records from "The re-Review of 9c7d77d" on; E32; §6.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `c2b1ec278e4517778da98cec630b6569228d6173`. Review exactly this commit.
- **Previous candidate:** `9c7d77dc6d9a17769e1e3df5c546edee5888cdbe`. The repair delta is `git diff 9c7d77dc c2b1ec27`:
  - the re-Review record (`cb1ce395`);
  - the repairs `17b22d71`, `eccd24bd` and `c2b1ec27`.

  The handoff of `9c7d77d` at `07747138` is not part of the candidate's behaviour. Phase E as a whole is `git diff 55c01a83 c2b1ec27`.
- **Manual:** blob `fe43f04f5a698688727f7473a7c2e4d5345ae911`, unchanged since `9c7d77d` (accepted A1-A9).
- **Plan:** `workplans/active/SSDS-8.0-G2-PHASE-E-PLAN.md` at the candidate: readings E15 and E32, §5's records, §6's open findings.
- **Repair owners:**
  - `orchestrator/src/ssds/derivation/items.py`:
    - selector resolution: `ItemObligation._named_parts`, `_branch`, `_all_parts`;
    - objections: `_result_at`, `_objections`, `_objections_naming`, `no_part_objections`, `no_part_condition`;
    - `Items.entry_positions`.
  - `orchestrator/src/ssds/interface/render.py`: `Renderer._no_part_triggers`, read by the decision brief.
- **Tests:** in `orchestrator/tests/ssds/test_phase_e_review.py`, the classes `NoPartTriggers` (E-R4, E-R5), `SelectorNaming` (N-1, N-2, P2) and `ObjectionRetirement` (B-S8, N-a and selector edges).

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-implementation/SKILL.md` at the public source and read the owners it routes to. The accepted Manual (A1-A9) and the G2 workplan's register govern. The earlier Reviews' findings, the same-family checks and the author's repair account are hypotheses to test, not authority.

## 3. What to judge

1. **E-R4 and E-R5 closed at their owners.** Rerun the earlier re-Review's discriminators:
   - the brief at the first decision, after an answer, at the SD-55 hold, with no-part adversity plus failing uncovered work, and a control with no objection;
   - selectors absent, 0, 99, Boolean, and a repeated index across retained and replacement partitions;
   - the route never returning to the answered review.

   Say for each whether it is closed, partly closed or open.
2. **The selector and retirement rules.** E32 states them:
   - a review names parts only when every adverse finding resolves to exactly one judged part, every unreplaced part of whose branch is still required;
   - a part-naming objection retires only when every required descendant has re-integrated;
   - a no-part objection retires only on a later review of a newer result.

   Judge whether these are faithful to Manual §10.3-§10.4, §13.7 and §16.5, and whether the implementation states them exactly. Specifically:
   - Can a finding now be lost, an objection stand with no live route, or a decision owed be retracted?
   - Whether a review names a part can change after it is admitted, from part to no part, when a later partition drops the part. Is that admissible?
   - The §6 items "a retired objection returning" and "reviving a dropped part": are either Phase E blockers?
3. **Siblings and new defects.** These are shared owners: the settled-partition rule, `carried_review_owed`, the veto through `_objections_naming`, the decision brief, and the route-4 oracle, which reads `_named_parts`. Look for regressions, a recursion, or a performance cliff.
4. **Evidence applicability.** E15 claims the full lifecycle enumerations recorded at `9a00fb78` apply unchanged to this delta. Its reasons: no replay admits a part selector, and every replay requests an item-level review only of the current result just after new work integrates. Check that claim.
5. **No regression of what passed:** E-R3 and the consolidated rule, E-R1, R1, R2, E-B2 to E-B4, B2 and B5 as closed, the suites, A9's realization, and the shadow and frozen-Core boundaries. Reuse earlier evidence only where the delta cannot affect it, and say where you did.
6. **Accounting.** Whether E15, E32, §5 and §6 state what is realized and what is not.

Classify findings as Phase E blockers (with the owner text, minimum repair and a discriminator), findings for a later phase, or non-blocking. If accepted authority itself appears false, contradictory or inadequate, or the mechanism should be redesigned more simply, raise a SERIOUS CHALLENGE routed to its owner.

## 4. Method and checks

Reconstruct independently, falsify with counterexamples against the real `ssds` package, and mutate where a test's discriminating power is in doubt. Use Python 3.11 or newer. At the candidate run:

```bash
python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt
python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v
python orchestrator/scripts/run_core_tests.py
python orchestrator/scripts/generate_protocol_snapshot.py --check
python -m unittest discover -s tests -v
git diff --check 9c7d77dc c2b1ec27
```

Run the SSDS suite as a non-root user. The full lifecycle enumerations (`SSDS_SLOW=1`) are optional. Write scratch only under `ssds80-phase-e-rereview-c2b1ec2` inside `$TMPDIR`, including any SSDS home; write nothing to `~/.ssds`.

**Scientific checks for this Review.** Answer each of these:
- State your material findings, or that you have none.
- State that you produced, ran or reviewed no realized scientific results, or give a null envelope.
- State any variants evaluated (count, kind, criterion).
- Report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment.
- Report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file. If you are of the author's (Claude) family, name it `qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-C2B1EC2-PASS.md` or `-NO-PASS.md`. Otherwise name it `qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-C2B1EC2-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`.

It must include:
- a header block: GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, BASELINE, SCOPE, MANUAL blob, REVIEW METHOD, and **REVIEWER**, giving the model family only and how you were engaged;
- `## SERIOUS CHALLENGE`;
- `## Verdict` for the Phase E implementation and exit: PASS or NO-PASS, saying whether the exit or only the implementation passes;
- the disposition of E-R4, E-R5, N-1, N-2, P2, B-S8, N-a, the evidence applicability and the accounting points;
- Phase E blockers, each with owner text, minimum repair and discriminator;
- findings for later phases;
- non-blocking findings;
- what you verified, what you reused and what you could not verify;
- the scientific-checks answers;
- a common-mode note;
- a statement that nothing beyond shadow is authorized.

End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
