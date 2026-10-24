# Independent re-Review handoff — SSDS 8 Phase E, repaired candidate 9c7d77d

This is the complete prompt for one independent re-Review of SSDS 8 Stage D Phase E after the repair of the re-Review of `49bebf3`. It is deliberately narrow. Judge whether that re-Review's one remaining blocker, E-R3, is closed at its owner without new defects, and whether anything found closed earlier has regressed. The re-Review accepts nothing. A Phase E PASS lets Phase F's dependent work start (G2 workplan §5.1 item 5); acceptance of the implementation is G3.

**Context.** The re-Review of `49bebf3` (`qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-49BEBF3-DIFFERENT-FAMILY-NO-PASS.md`) judged E-R1, R1 and R2 closed. It left one blocker, E-R3: after an item-level NO-PASS naming no part on a one-part partition, the objection vetoed the part's review and reopened the part. The composite route then returned the partition's route before reading the objection, so the principal's decision (Manual §10.4 route 4) was never derived.

Repairing it took several rounds, each checked by a same-family reviewer (Phase E plan §5, the four records after "The re-Review of 49bebf3"):
- **af327075** reads the no-part condition before the parts. It also derives the item-level review of a newer result beside the open decision, the only review that retires the objection. That checker found **B-1** (a second objection's veto hid the decision again) and **B-2** (a re-partition released the chain early).
- **98c4d9a4** re-derived when the item-level-no-part chain moves past a `PARTITION` answer. That checker found **S-1**: the rule was not monotone.
- **9a00fb78** consolidated it on SD-54's one post-answer rule as it already applies to `AMEND`. A `PARTITION` answering the chain is settled once its work has integrated, and a condition that still holds then derives the next decision. That checker found the rule sound, and one counting error in its walk of re-partitions, **C-1**.
- **d5f21b07** repairs C-1.

The plan judges this line the fifth and sixth defects in one mechanism and records the consolidation as the simplification §8 and G2 §5.6 require. Judge that too.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `9c7d77dc6d9a17769e1e3df5c546edee5888cdbe`. Review exactly this commit.
- **Previous candidate:** `49bebf32ad0ce61785b5e8f63e84f5557f23ecca`. The repair delta is `git diff 49bebf32 9c7d77dc`:
  - the re-Review record (`71bfef2f`);
  - the repairs `af327075`, `98c4d9a4`, `9a00fb78` and `d5f21b07`;
  - the lifecycle record (`9c7d77dc`).

  The handoff of `49bebf3` at `7d660f42` is not part of the candidate's behaviour. Phase E as a whole is `git diff 55c01a83 9c7d77dc`.
- **Manual:** blob `fe43f04f5a698688727f7473a7c2e4d5345ae911`, unchanged since `49bebf3` (accepted A1-A9).
- **Plan:** `workplans/active/SSDS-8.0-G2-PHASE-E-PLAN.md`, blob `1557e3a42cad5d47e4dd9f4ad4e75c50a029c7e8`: readings E15 and E32, §5's records, §6's open findings.
- **Repair owners:**
  - `orchestrator/src/ssds/derivation/items.py`: `ItemObligation.no_part_condition`, `_partition_settled`, `carried_review_owed`, `_composite_route`, and `chain` with its `past` argument.
  - `orchestrator/src/ssds/derivation/workflow.py`: the item-level `REVIEW` derivation.
- **Tests:**
  - `orchestrator/tests/ssds/test_phase_e_review.py`, classes `NoPartObjection` (E-R3) and `SettledPartition` (B-1, B-2, S-1, C-1, a dropped branch);
  - in `orchestrator/tests/ssds/test_step5_review.py`: the route-4 oracle `Lifecycle.route4`, applied in every replay, and the one-part seed `LifecycleOnePart` with `LifecycleOnePartFull` behind `SSDS_SLOW` (its alphabet adds a redone-and-objected partition and a non-answer redo step).

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-implementation/SKILL.md` at the public source and read the owners it routes to. The accepted Manual (A1-A9) and the G2 workplan's register govern. The earlier Reviews' findings, the same-family checks and the author's repair account are hypotheses to test, not authority.

## 3. What to judge

1. **E-R3 closed at its owner.**
   - Rerun the earlier re-Review's three shape controls: one part with no part named, two parts with no part named, one part with part 0 named.
   - Answers through SD-54 continuation and the SD-55 hold.
   - The carried review retiring the objection.
   - The shapes the same-family checks found: B-1, B-2, S-1, C-1, and a branch dropped by a later whole partition.

   Say whether E-R3 is closed, partly closed or open.
2. **The consolidated rule.** Is a `PARTITION` answering the item-level-no-part chain, settled by SD-54's `AMEND` rule, faithful to Manual §10.4, §13.7 and SD-54? Specifically:
   - Is it monotone: can a settled partition become unsettled, or a derived open decision vanish while the condition holds?
   - Can an unsettled partition hold the route with no live work?
   - Can a decision be derived before the partition's work has genuinely integrated?
   - Does the early next decision beside the carried review lose a finding or strand an obligation?

   Judge whether the plan's account (E32) states the rule exactly.
3. **Siblings and new defects.** Reading the no-part condition before the parts changes every partitioned item's route while an objection stands. Partition discovery continues past `PARTITION` answers on that chain structurally. The review derivation now has a second trigger.
   - Look for a regression, a hidden handoff, a lost finding, a stranded obligation, or a false discharge.
   - §6 records open findings the author judges non-blocking: overlapping partitions; an early no-part decision; a late objection, whose only exit runs through the overlap path; reviving a dropped part (Phase F Admission); and the decision brief not naming the objection. Judge whether any is in fact a Phase E blocker.
4. **The replay's discriminating power.** `Lifecycle.route4` judges route 4 from the replay's own history and from the item's objection and subject sets. Judge whether it, the alphabets and the full enumerations (E15) discriminate this line's failures. E15 claims the enumerations at `9a00fb78` apply unchanged to `d5f21b07`; check that claim.
5. **No regression of what passed**: E-R1, R1, R2, E-B2 to E-B4, B2 and B5 as closed, the suites, A9's realization, and the shadow and frozen-Core boundaries. Reuse earlier evidence only where the delta cannot affect it, and say where you did.
6. **Accounting.** Whether E15, E32, §5 and §6 now state what is realized and what is not.

Classify findings as Phase E blockers (with the owner text, minimum repair and a discriminator), findings for a later phase, or non-blocking. If accepted authority itself appears false, contradictory or inadequate, or the mechanism should instead be redesigned more simply, raise a SERIOUS CHALLENGE routed to its owner.

## 4. Method and checks

Reconstruct independently, falsify with counterexamples against the real `ssds` package, and mutate where a test's discriminating power is in doubt. Use Python 3.11 or newer. At the candidate run:

```bash
python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt
python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v
python orchestrator/scripts/run_core_tests.py
python orchestrator/scripts/generate_protocol_snapshot.py --check
python -m unittest discover -s tests -v
git diff --check 49bebf32 9c7d77dc
```

Run the SSDS suite as a non-root user. The full lifecycle enumerations (`SSDS_SLOW=1`; about 30 minutes, 2 hours and 2.5 hours) are optional, since E15 records their runs. Write scratch only under `ssds80-phase-e-rereview-9c7d77d` inside `$TMPDIR`, including any SSDS home; write nothing to `~/.ssds`.

**Scientific checks for this Review.** Answer each of these:
- State your material findings, or that you have none.
- State that you produced, ran or reviewed no realized scientific results, or give a null envelope.
- State any variants evaluated (count, kind, criterion).
- Report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment.
- Report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file. If you are of the author's (Claude) family, name it `qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-9C7D77D-PASS.md` or `-NO-PASS.md`. Otherwise name it `qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-9C7D77D-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`.

It must include:
- a header block: GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, BASELINE, SCOPE, MANUAL blob, REVIEW METHOD, and **REVIEWER**, giving the model family only and how you were engaged;
- `## SERIOUS CHALLENGE`;
- `## Verdict` for the Phase E implementation and exit: PASS or NO-PASS, saying whether the exit or only the implementation passes;
- the disposition of E-R3, the consolidated rule, the replay and the accounting points;
- Phase E blockers, each with owner text, minimum repair and discriminator;
- findings for later phases;
- non-blocking findings;
- what you verified, what you reused and what you could not verify;
- the scientific-checks answers;
- a common-mode note;
- a statement that nothing beyond shadow is authorized.

End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
