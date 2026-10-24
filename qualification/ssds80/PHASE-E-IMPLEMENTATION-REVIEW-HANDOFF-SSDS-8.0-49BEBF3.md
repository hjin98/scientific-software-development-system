# Independent re-Review handoff — SSDS 8 Phase E, repaired candidate 49bebf3

This is the complete prompt for one independent re-Review of SSDS 8 Stage D Phase E after the repair of the re-Review of `89684fb`. It is deliberately narrow. Judge whether that re-Review's one remaining blocker, E-R1, is closed at its owner, together with the two blockers (R1, R2) a same-family check of the first repair found, without new defects; and whether anything found closed earlier has regressed. The re-Review accepts nothing. A Phase E PASS lets Phase F's dependent work start (G2 workplan §5.1 item 5); acceptance of the implementation is G3.

**Context.** The re-Review of `89684fb` (`qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-89684FB-DIFFERENT-FAMILY-NO-PASS.md`) judged E-B2 to E-B4 closed. It left one blocker, E-R1: retained work escaped discharge across partition history. This happened when the whole item integrated the work before its first partition, and when a part integrated it and a re-partition then replaced that part. In both cases the item was discharged and dependent work released while the work's evidence was disputed.

The author repaired E-R1 at `c5d2cbc4`. A same-family reviewer then checked that repair (100c8ae8) and found two more blockers:
- **R1**, the same family as E-R1: after an R1 tightening gave the item a new revision, the partition's chain was left and the part's earlier work dropped out of discharge.
- **R2**, new with the repair: a lint-valid `PARTITION` answering the `item-level-no-part` chain without covering the failing subject left the item `OPEN` with every part done and no decision.

Both are repaired at `6992d118`. The lifecycle replay's live-wait hook is corrected at `9bec3111`. The Phase E plan records each step (§5: "The re-Review of 89684fb", "Same-family check of the E-R1 repair"). Stakeholder decision SD-63 (`78cb701a`) routes an unrelated PEM handoff to a later amendment proposal; it changes no Phase E behaviour.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `49bebf32ad0ce61785b5e8f63e84f5557f23ecca`. Review exactly this commit.
- **Previous candidate:** `89684fb93152f87355a84bde1928b8d69218b8b6`. The repair delta is `git diff 89684fb9 49bebf3`:
  - the re-Review record (`16ee1a98`);
  - the E-R1 repair (`c5d2cbc4`) and its lifecycle record (`100c8ae8`);
  - the R1 and R2 repairs (`6992d118`);
  - the replay hook (`9bec3111`);
  - SD-63 (`78cb701a`);
  - the lifecycle record (`49bebf3`).

  The handoff of `89684fb` at `875a88ab` is not part of the candidate's behaviour. Phase E as a whole is `git diff 55c01a83 49bebf3`.
- **Manual:** blob `fe43f04f5a698688727f7473a7c2e4d5345ae911`, unchanged since `89684fb` (accepted A1-A9).
- **Plan:** `workplans/active/SSDS-8.0-G2-PHASE-E-PLAN.md`, blob `678a7cf1a5de14fac5795b203d613b06ec9f45d7`: readings E15, E30 and E32, §5's records, §6's open findings.
- **Repair owners:**
  - `orchestrator/src/ssds/derivation/items.py`:
    - `ItemObligation.subjects`, `retained_subjects`, `_work_obligations`, `_retained_in`, `uncovered_subjects`, `uncovered_failing`;
    - `_composite_predicate`, `_composite_route`, `discharge`;
    - `chain` with its `past` argument, and the continuation in `partitions`;
    - `Items.partition_sizes`.
  - `orchestrator/src/ssds/interface/render.py`: the decision brief's item lines.
- **Tests:**
  - `orchestrator/tests/ssds/test_phase_e_review.py`, classes `RetainedWork` (E-R1), `RetainedAcrossRevisions` (R1, R2), `LifecycleRetained` and `LifecycleRetainedFull` (behind `SSDS_SLOW`);
  - the replay hooks in `test_step5_review.Lifecycle`;
  - the `keyed` argument of `test_partition.PartFlow.work_part`.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-implementation/SKILL.md` at the public source and read the owners it routes to. The accepted Manual (A1-A9) and the G2 workplan's register govern. The earlier Reviews' findings, the same-family check and the author's repair account are hypotheses to test, not authority.

## 3. What to judge

1. **E-R1, R1 and R2 closed at their owners.** Say for each whether it is closed, partly closed or open.
   - **E-R1.** Rerun the earlier re-Review's two histories (whole before partition, replaced part) and its permission variants. The item must be `OPEN` with a live restoring route and the dependent item waiting; complete provisional permission gives at most `DISCHARGED_PROVISIONAL`.
   - **R1.** Partition, a part's integrated work, passing then failing evidence, an R1 tightening, the same partition at the new revision, then new parts done without touching the failing subject. The item must stay `OPEN`, the part holding the subject must reopen, and the follow-up must wait. Repeat with a part result that omits the optional `item_key`.
   - **R2.** Failing retained work no part covers, then a non-covering partition whose part is done. The chain must derive its next decision naming that partition. A covering answer to it must be found and hand the subject to a part. The SD-55 hold must count across the continuation. The decision brief must name the failing subjects.
2. **Siblings and new defects.** The repairs touch shared owners:
   - **Subject set.** An item's subject set is now derived from the admitted history, partitioned or not. It is read by its predicate, provisional scope, briefs, reports, the readiness of dependent items and the inspector.
   - **Chain continuation.** On the `item-level-no-part` chain the chain continues past a finished partition, and partition discovery follows that continuation. Look for recursion, a chain that never ends, double-counted answers, or a partition found that should not be.
   - What to look for overall: a regression, a new way to strand an obligation or lose a finding, a subject that blocks discharge with no route to resolve it, or a false claim of discharge.
   - **Disclosed limits.** §6 lists open findings the author judges non-blocking: overlapping partitions reopening each other by drift until a budget sends one to the principal; redone work not restoring `ev`/`qual`; a single-part partition reopening on a no-part NO-PASS; answers to never-derived continuation decisions counted structurally. Judge whether any is in fact a Phase E blocker.
3. **The replay's discriminating power.** `Lifecycle.suspended` now accepts a state with no open decision when the item is partitioned and an open part is live: READY, holding decisions, or waiting only on plan re-acceptance while a `PLAN_ACCEPT` obligation is open. Judge whether that hook could hide a strand, and whether the alphabet's non-covering partition exercises R2 fairly. E15 records the full enumerations.
4. **No regression of what passed.** That covers E-B2 to E-B4 and B2 and B5 as closed, the suites, A9's realization, and the shadow and frozen-Core boundaries. Reuse earlier evidence only where the delta cannot affect it, and say where you did.
5. **Accounting.** Whether E15, E30, E32 and §6 now state what is realized and what is not.

Classify findings as Phase E blockers (with the owner text, minimum repair and a discriminator), findings for a later phase, or non-blocking. If accepted authority itself appears false, contradictory or inadequate, raise a SERIOUS CHALLENGE routed to its owner.

## 4. Method and checks

Reconstruct independently, falsify with counterexamples against the real `ssds` package, and mutate where a test's discriminating power is in doubt. Use Python 3.11 or newer. At the candidate run:

```bash
python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt
python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v
python orchestrator/scripts/run_core_tests.py
python orchestrator/scripts/generate_protocol_snapshot.py --check
python -m unittest discover -s tests -v
git diff --check 89684fb9 49bebf3
```

Run the SSDS suite as a non-root user. The full lifecycle enumerations (`SSDS_SLOW=1`; about 25 minutes and 2 hours) are optional, since the plan records their runs at the candidate's code. Write scratch only under `ssds80-phase-e-rereview-49bebf3` inside `$TMPDIR`, including any SSDS home; write nothing to `~/.ssds`.

**Scientific checks for this Review.** Answer each of these:
- State your material findings, or that you have none.
- State that you produced, ran or reviewed no realized scientific results, or give a null envelope.
- State any variants evaluated (count, kind, criterion).
- Report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment.
- Report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file. If you are of the author's (Claude) family, name it `qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-49BEBF3-PASS.md` or `-NO-PASS.md`. Otherwise name it `qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-49BEBF3-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`.

It must include:
- a header block: GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, BASELINE, SCOPE, MANUAL blob, REVIEW METHOD, and **REVIEWER**, giving the model family only and how you were engaged;
- `## SERIOUS CHALLENGE`;
- `## Verdict` for the Phase E implementation and exit: PASS or NO-PASS, saying whether the exit or only the implementation passes;
- the disposition of E-R1, R1, R2, the replay hook and the accounting points;
- Phase E blockers, each with owner text, minimum repair and discriminator;
- findings for later phases;
- non-blocking findings;
- what you verified, what you reused and what you could not verify;
- the scientific-checks answers;
- a common-mode note;
- a statement that nothing beyond shadow is authorized.

End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
