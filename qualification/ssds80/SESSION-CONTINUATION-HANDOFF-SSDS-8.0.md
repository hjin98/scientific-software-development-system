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

- Workplan: `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md`, design revision 21.
- Candidate under review: `ef8445a3bafb86086546ceff3eaa8b0171dbdb25` (workplan blob `9db8178b5894b4518517aaf69819f3e556711916`).
- Review handoff: `qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-21.md` (includes the convergence review strategy as method step 5).
- Review of revision 21: launched as a fresh-context sub-agent; its record arrives uncommitted as `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-EF8445A-<VERDICT>.md`.
- Reviews, all NO-PASS: F9D9DE8 … 4EC0024, BA7F738, 947370D (`qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-*-NO-PASS.md`).
- Open non-blocking item: N1 (the 2026-10-12 governing-version adoption instruction is paraphrase-only; needs the stakeholder's restatement).

### What revision 21 did

Revision 21 is the simplification pass the convergence owner required after the `947370d` Review (blocker family W, routed as post-simplification recurrence). It removed the pair as a supersession record, together with its Admission authorization, the withdrawal latch, `here`, the reading pair, the run enumeration, the decision-class pair exceptions and the floor deferral. In their place is one derived test, `stale_G` (§6.6): a failing assessment does not count in a frame when it was reproduced identically on its own content, never differed there, and a standing observation of the frame's content does not yield it under the frame's reading. "Yields" means the mechanical verdict for a mechanical oracle and an identical outcome for an assessor-read one. Permissive inputs must stand: held across loss boundaries, with no blocking challenge open, overridden or not. Restrictive inputs are read whatever their standing. Readings are tested by what was in force at the failure's base. The assessor-read reading change is settled by a reading-ground `IMMATERIALITY` judgment (R2). The floor is an event on ledger facts. The start rules are unchanged. One deliberate change: an accepted relaxation can make a mechanical failure stale. Audited in §27.36-§27.37.

### Model check

`qualification/ssds80/s1_disagreement_model_check.py` (default mode REV21; `--jobs N` splits the search by its first record without changing the totals). It has mechanical and assessor-read failures, a verdict function per reading, a tightened reading that can be admitted, relaxed and restored, four outcome values, and owner-stated P13, Q and Q2. Revision 21 results: depth 4, 1,378,642 transitions; depth 5, 81,511,449 transitions (`--jobs 4`, about 49 min); 0 failures and 68/68 discriminators at both. The first depth-5 run found two defects (a risk override on a challenged observation, and P5's statement), now fixed. Sensitivity: `REV20=1` fails P10 and P13; every earlier mode fails owner-grounded properties.

## Loop procedure

1. When a Review record arrives (written uncommitted by the reviewer under `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-<SHORTSHA>-<VERDICT>.md`): read it in full, verify each blocker independently against the candidate text, check the REVIEWER line names only the model family, then commit it ("Add SSDS 8.0 <shortsha> independent sub-agent D3 review (NO-PASS|PASS)") and push.
2. If NO-PASS, repair at the earliest owners as the next design revision, in the D3 role. Apply the convergence owner first (see "Convergence state"): for a blocker in the recurring family, run the simplification/re-derivation pass before any additive repair; prefer removing mechanism to adding it. Update together: frontmatter (`design_revision`, `prior_review`, `prior_reviewed_candidate`, `review_history`), the §0 block (REVISION line, PRIOR REVIEWS, INDEPENDENT D3 REVIEW), §0.1 (new section; demote the previous one to "#### Revision N (prior) record"), affected §6.6/§6.8/§6.9/§7.x/§10 text, §21, §22, §26, a new §27 round and minimum-architecture pass, §28, and the SSDS 8 section of `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. Extend the model check where the blocker is representable; keep the previous mode as a sensitivity mode that must fail owner-grounded properties.
3. Validate: `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`; `git diff --check`; the model check at depth 4 in every mode, and depth 5 in the default mode (run in the background; commit depth-4 figures first, then a follow-up commit recording depth 5).
4. Write the next review handoff (including the convergence review-strategy focus of "Convergence state") by copying `qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-19.md` and updating: revision number, candidate SHA and workplan blob, previous candidate and record, prior-review list, the focus bullets, and the model-check mode list (add the previous mode). Commit and push it.
5. Launch a fresh-context general-purpose sub-agent with: "Read the file <repo>/qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-<N>.md. Everything below its horizontal rule (the line '---') is your complete task prompt. Follow it exactly: review the named candidate commit, write exactly one Review record file where it says, do not commit or push, and return only the record path, the verdict and a one-paragraph summary of blockers. In the REVIEWER line name only your model family." Then wait for it.
6. On PASS: commit the record, update §28 and the index to record it, and report to the stakeholder. Acceptance still needs stakeholder decisions and gates G1-G4; D4 stays NOT AUTHORIZED.

## Latest Review

Pending: the fresh-context sub-agent Review of revision 21, launched from `REVIEW-HANDOFF-SSDS-8.0-REVISION-21.md` against candidate `ef8445a3bafb86086546ceff3eaa8b0171dbdb25`. The previous record, `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-947370D-NO-PASS.md` (blocker family W; N1-N6; family-level convergence assessment), is answered by revision 21's simplification pass (§0.1, §27.36).

Next action after a NO-PASS: read the record's family-level assessment first. If the §6.6 family recurs again after this simplification, that is recurrence after two simplifications, so consider whether the earliest affected abstraction is above §6.6 (for example the stakeholder-accepted objective of mechanical dispositions) and route to the stakeholder rather than revising again. Otherwise revision 22 per the loop procedure, then `REVIEW-HANDOFF-SSDS-8.0-REVISION-22.md` (previous candidate `ef8445a3bafb86086546ceff3eaa8b0171dbdb25`, add `REV21=1` to the sensitivity modes).
