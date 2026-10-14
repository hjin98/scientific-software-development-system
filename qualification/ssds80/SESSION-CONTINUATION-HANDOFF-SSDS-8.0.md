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

## Current state (Phase B closeout)

- Workplan: `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md`, **design revision 23**, frozen for Review at `e23f14208be869e6a78cfd7b312e447254ee1851` (workplan blob `610f373b97fb8152d2a5742e17fa172e12204756`; model at `d379298`, unchanged since). **Independent Phase B D3 Review PASS; architecture remains proposed.**
- Last Review: `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md`, **PASS** on exact candidate `e23f14208be869e6a78cfd7b312e447254ee1851`; committed in `229812de`. No surviving blocker or governing Serious Challenge. Non-blocking N1-N4 and depth-5 provenance limits remain explicit in that record.
- Earlier reviews, all NO-PASS: F9D9DE8 … 947370D, EF8445A, 552AC01.
- Stakeholder decisions recorded verbatim: SD-9 (D3 role, convergence rule) and SD-10 (2026-10-14: "Subtractive repair" chosen after the 552ac01 NO-PASS), both in `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md`. Open non-blocking item: N1's 2026-10-12 adoption instruction is still paraphrase-only.
- Issued review handoff: `qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-23.md`, bound to candidate `e23f14208be869e6a78cfd7b312e447254ee1851` and workplan blob `610f373b97fb8152d2a5742e17fa172e12204756`; the local checkout path is corrected.

### What revisions 21-23 did

- **Revision 21** simplified the §6.6 disagreement family under the convergence owner. It removed the pair as a supersession record, together with the withdrawal latch, `here`, the reading pair, the run enumeration, the class exceptions and the floor deferral. In their place is one derived test, `stale_G`: a failing assessment stops counting in a frame when it was reproduced identically, never differed on its own content, and a standing observation of the frame's content does not yield it under the frame's reading.
- **Revision 22** restored, for assessor-read oracles, the one capability revision 21 had dropped: a **discriminating reading**, one independent assessment that reads the frame's outcome PASS and the reproduction FAIL in one record. Admission refuses a contradictory reading, and the reading is R3 for D1/D2 failures that may belong to admitted content.
- **Revision 23** keys the reading's coverage on the outcome read, under the same reading, on any content, so an identical outcome after a change stays settled. It also stops re-escalating a failure already shown to be the candidate's own (Y), and answers findings N1-N6.

### Model check

`qualification/ssds80/s1_disagreement_model_check.py` (default mode REV23; `--jobs N` splits the search across processes and gives the same totals).
- REV23 at depth 4: 1,574,464 transitions, 0 failures, 80/80 discriminators.
- `REV22=1` fails P11 and P13, so Y is visible.
- The enumeration generates only honest readings, under a materiality partition (outcome 3 shows the same defect as 1) that only the owner-stated `owner_stale` reads.
- **Depth 5 for REV23 is done:** 99,095,037 transitions, 0 failures, 80/80 discriminators (`--jobs 4`, 62 min 52 s), on the model committed at `d379298`, which is unchanged at `d879114`. It is recorded with prior-session provenance and limitations in §27.40. The continuation session also executed default depth 4 (zero failures, 80/80 discriminators) and all twelve sensitivity modes (each fails owner-grounded properties), Python 3.10.12, `--jobs 4`.

## Next steps (in order)

1. The revise/review loop has reached independent Phase B PASS. The Review record, workplan §0/§28 and authority index record it without promoting architecture to accepted-current or changing the reviewed semantic candidate.
2. The next governed work is Phase C: one Architecture Manual resolving §21, independently reviewed and explicitly accepted by the stakeholder under G1. Carry Review N1-N4 forward: historical adoption provenance; positive-only completeness and cyclic-prefix discriminators at real owners; diagnostic/reader limits; empirical cost/reopen conditions. These are not new Phase B blockers.
3. Shadow D4 additionally requires the reviewed shadow workplan and explicit stakeholder authorization under G2. **No D4 is authorized.** Runtime qualification and native cutover remain G3/G4. Do not infer authorization from this PASS or start a campaign.
4. Depth 5 remains prior-session-reported reuse with missing raw output/interpreter. Both continuation and reviewer independently executed depth 4 and the twelve sensitivity modes; they share the instrument, not an independent semantic oracle. Do not rerun unchanged depth 5 merely to accumulate confidence.

## Loop procedure

1. When a Review record arrives (written uncommitted by the reviewer under `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-<SHORTSHA>-<VERDICT>.md`): read it in full, verify each blocker independently against the candidate text, check the REVIEWER line names only the model family, then commit it ("Add SSDS 8.0 <shortsha> independent sub-agent D3 review (NO-PASS|PASS)") and push.
2. If NO-PASS, repair at the earliest owners as the next design revision, in the D3 role. Apply the convergence owner first (see "Convergence state"): for a blocker in the recurring family, run the simplification/re-derivation pass before any additive repair; prefer removing mechanism to adding it. Update together: frontmatter (`design_revision`, `prior_review`, `prior_reviewed_candidate`, `review_history`), the §0 block (REVISION line, PRIOR REVIEWS, INDEPENDENT D3 REVIEW), §0.1 (new section; demote the previous one to "#### Revision N (prior) record"), affected §6.6/§6.8/§6.9/§7.x/§10 text, §21, §22, §26, a new §27 round and minimum-architecture pass, §28, and the SSDS 8 section of `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. Extend the model check where the blocker is representable; keep the previous mode as a sensitivity mode that must fail owner-grounded properties.
3. Validate: `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`; `git diff --check`; the model check at depth 4 in every mode, and depth 5 in the default mode (run in the background; commit depth-4 figures first, then a follow-up commit recording depth 5).
4. Write the next review handoff (including the convergence review-strategy focus of "Convergence state") by copying `qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-19.md` and updating: revision number, candidate SHA and workplan blob, previous candidate and record, prior-review list, the focus bullets, and the model-check mode list (add the previous mode). Commit and push it.
5. Launch a fresh-context general-purpose sub-agent with: "Read the file <repo>/qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-<N>.md. Everything below its horizontal rule (the line '---') is your complete task prompt. Follow it exactly: review the named candidate commit, write exactly one Review record file where it says, do not commit or push, and return only the record path, the verdict and a one-paragraph summary of blockers. In the REVIEWER line name only your model family." Then wait for it.
6. On PASS: commit the record, update §28 and the index to record it, and report to the stakeholder. Acceptance still needs stakeholder decisions and gates G1-G4; D4 stays NOT AUTHORIZED.

## Latest Review

`qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md`: **PASS**. It closes Y1/Y2 and reconstructs earlier closures, attacks live-failure hiding and settled-failure resurrection, and rejects the completeness-polarity counterexample because it violates the explicit permissive-only rule. The full record owns the evidence, limits and N1-N4 dispositions. D4 remains NOT AUTHORIZED.

## Prior Review (historical)

`qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-552AC01-NO-PASS.md` (revision 22, candidate `552ac01`): **NO-PASS**. One blocker:

- **Y:** a reading's coverage and class were keyed on content identity, so settled assessor-read failures resurrected at every change, and for D1/D2 every later reading went to R3.

Findings N1-N6 are non-blocking. Revision 23 answers them all (§0.1). The Review's family assessment found that Y recurs in the "two repairs meet" pattern, with common-mode causes:
- same-family Reviews' repair directions adopted with their blind spots, three cycles running;
- the qualification instrument encoding the rule under test;
- handoff framing;
- verification in one direction only.

The revision-23 handoff now asks for attacks in both directions.

**Convergence guidance for the next session (SD-9, SD-10).** Thirteen consecutive NO-PASS Reviews have fallen on the §6.6 family. If the revision-23 Review finds another §6.6 blocker:
- read its family assessment first;
- a clean local defect that genuinely closes a cause can be repaired locally;
- any other recurrence is the stakeholder's decision: offer the options again (a subtractive repair, removing assessor-read staleness so those failures stop only by judgment, a different-family Review, or a pause to reconsider above §6.6) rather than revising again on your own judgment.

For a PASS, follow loop step 6: acceptance still needs stakeholder decisions and gates G1-G4, and D4 stays NOT AUTHORIZED.
