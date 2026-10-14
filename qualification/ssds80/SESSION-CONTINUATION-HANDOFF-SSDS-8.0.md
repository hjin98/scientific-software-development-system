# SSDS 8.0 revise/review loop — session continuation hand-off

This file lets a new session (any account) continue the stakeholder-directed revise/review cycle for the SSDS 8.0 architecture workplan. It is coordination state, not authority: the workplan, its Review records and `PROTOCOL-RELEASE-STATE.yaml` own everything stated here.

## Standing instruction

Stakeholder (SD-8, 2026-10-13): "Perform the remaining revise / review cycle yourself through the revision and sub-agent review cycle until all remaining blocking issues are closed." D4 remains **NOT AUTHORIZED**; a sub-agent PASS authorizes nothing by itself (gates G1-G4, §25).

Constraints:
- Work and push only on branch `ssds-8.0-graph-native-architecture` (`git push -u origin ssds-8.0-graph-native-architecture`). No pull requests.
- Never put model names or identifiers in repository artifacts or commit messages; Review records name the model family only.
- Commit and push every change; never leave the tree dirty.
- Stakeholder (2026-10-13, after SD-8): read the governing Protocol 7.2.1 owners and work in the software-design (D3) role for every revision and Review, and apply the convergence owner, including the active simplification rule, when issues do not converge or keep resurfacing. The owners are `source/roles/software-design/SKILL.md`, `source/shared/references/architecture-and-design.md`, `evidence-evolution-and-dependencies.md` and `convergence-and-cycle-economy.md`, read at `aaeaf8b6b2121b9fb8aba31917c8265649c43954` with `git show`.

## Convergence state (read before repairing)

The §6.6 assessment-disagreement family ("what a failing assessment's adversity depends on") has recurred in every revision since 10. Revision 17 was a simplification (it removed the mechanical lapse), and the family recurred after it (revisions 18-20 each added stop/standing machinery). The convergence owner classifies this as **post-simplification recurrence**, which calls for **bounded reconsideration of the earliest affected abstraction**. Its **active simplification trigger** applies before any further additive durable repair: "repeated patches around the same mechanism, patch-on-patch repair ... special cases accumulating around one owner ... family closure that does not reduce the failure surface". So:

- do not answer a new blocker in this family with another condition, exception, latch or record field;
- first run a simplification/re-derivation pass. Hold the governing evidence owner (applicability; stale failing evidence is inadmissible; `review-required` when uncertain; disagreement preserved and resolved only by owner adjudication or discriminating evidence, explicitly) and the stakeholder direction fixed, and treat the §6.6 machinery as replaceable;
- prefer removing, narrowing or consolidating mechanisms. Record in §27 what was removed, which owner-required property each removal preserves, and which costs move to judgment or to §26. If the simpler design would change an accepted parent or a stakeholder decision, stop and route it to the stakeholder.

The revision-20 Review was sent this instruction mid-review: assess the family for post-simplification recurrence, the minimum justified concretization, a simpler equivalent and common-mode causes, and route at family level.

## Current state

- Workplan: `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md`, design revision 22.
- Candidate under review: `552ac01bb799c22dece5a33d93bd4244bea21d2a` (workplan blob `8970b617b377756523db1ad783d0863383949fa2`).
- Review handoff: `qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-22.md` (convergence review strategy and capability-transfer check, method step 5).
- Review of revision 22: launched as a fresh-context sub-agent; its record arrives uncommitted as `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-552AC01-<VERDICT>.md`.
- Reviews, all NO-PASS: F9D9DE8 … BA7F738, 947370D, EF8445A.
- Stakeholder instruction SD-9 (D3 role, convergence) is recorded verbatim. Open non-blocking item: N1's 2026-10-12 adoption instruction is still paraphrase-only.

### What revisions 21-22 did

Revision 21 simplified the §6.6 disagreement family under the convergence owner. It removed the pair as a supersession record and its machinery, and replaced them with one derived test, `stale_G`. A failing assessment stops counting in a frame when it was reproduced identically, never differed on its own content, and a standing observation of the frame's content does not yield it under the frame's reading. The `ef8445a` Review found the mechanical branch sound but one capability dropped (blocker X): for an assessor-read oracle only a reading can say that a different outcome no longer shows the failure. Revision 22 restores it as a **discriminating reading**: one independent assessment reads the frame's outcome PASS and the reproduction FAIL in one record. A contradictory reading is refused. The reading is R3 for D1/D2 failures that may belong to admitted content. The reading-ground `IMMATERIALITY` is removed. Audited in §27.36-§27.39.

### Model check

`qualification/ssds80/s1_disagreement_model_check.py` (default mode REV22; `--jobs N`). Revision 22: depth 4, 1,574,464 transitions; depth 5, 99,095,037 transitions (`--jobs 3`, about 98 min); 0 failures; 77/77 discriminators. `REV21=1` fails Q and P7 (X); every earlier mode fails owner-grounded properties.

## Loop procedure

1. When a Review record arrives (written uncommitted by the reviewer under `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-<SHORTSHA>-<VERDICT>.md`): read it in full, verify each blocker independently against the candidate text, check the REVIEWER line names only the model family, then commit it ("Add SSDS 8.0 <shortsha> independent sub-agent D3 review (NO-PASS|PASS)") and push.
2. If NO-PASS, repair at the earliest owners as the next design revision, in the D3 role. Apply the convergence owner first (see "Convergence state"): for a blocker in the recurring family, run the simplification/re-derivation pass before any additive repair; prefer removing mechanism to adding it. Update together: frontmatter (`design_revision`, `prior_review`, `prior_reviewed_candidate`, `review_history`), the §0 block (REVISION line, PRIOR REVIEWS, INDEPENDENT D3 REVIEW), §0.1 (new section; demote the previous one to "#### Revision N (prior) record"), affected §6.6/§6.8/§6.9/§7.x/§10 text, §21, §22, §26, a new §27 round and minimum-architecture pass, §28, and the SSDS 8 section of `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. Extend the model check where the blocker is representable; keep the previous mode as a sensitivity mode that must fail owner-grounded properties.
3. Validate: `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`; `git diff --check`; the model check at depth 4 in every mode, and depth 5 in the default mode (run in the background; commit depth-4 figures first, then a follow-up commit recording depth 5).
4. Write the next review handoff (including the convergence review-strategy focus of "Convergence state") by copying `qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-19.md` and updating: revision number, candidate SHA and workplan blob, previous candidate and record, prior-review list, the focus bullets, and the model-check mode list (add the previous mode). Commit and push it.
5. Launch a fresh-context general-purpose sub-agent with: "Read the file <repo>/qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-<N>.md. Everything below its horizontal rule (the line '---') is your complete task prompt. Follow it exactly: review the named candidate commit, write exactly one Review record file where it says, do not commit or push, and return only the record path, the verdict and a one-paragraph summary of blockers. In the REVIEWER line name only your model family." Then wait for it.
6. On PASS: commit the record, update §28 and the index to record it, and report to the stakeholder. Acceptance still needs stakeholder decisions and gates G1-G4; D4 stays NOT AUTHORIZED.

## Latest Review

Pending: the fresh-context sub-agent Review of revision 22 against candidate `552ac01bb799c22dece5a33d93bd4244bea21d2a`. The previous record, `WORKPLAN-REVIEW-SSDS-8.0-EF8445A-NO-PASS.md` (blocker X; N1-N5), is answered by revision 22 (§0.1, §27.38).

Next action after a NO-PASS: read the family assessment first. A clean local defect that genuinely closes a cause stays local. A recurrence in the §6.6 family that is not a missed capability, after the revision-21 simplification, means the earliest affected abstraction may lie above §6.6, for example the stakeholder-accepted aim of mechanical dispositions. Route that to the stakeholder rather than revising again. Otherwise revision 23, then `REVIEW-HANDOFF-SSDS-8.0-REVISION-23.md` (previous candidate `552ac01bb799c22dece5a33d93bd4244bea21d2a`, add `REV22=1`).
