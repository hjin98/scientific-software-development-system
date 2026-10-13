# SSDS 8.0 revise/review loop — session continuation hand-off

This file lets a new session (any account) continue the stakeholder-directed revise/review cycle for the SSDS 8.0 architecture workplan. It is coordination state, not authority: the workplan, its Review records and `PROTOCOL-RELEASE-STATE.yaml` own everything stated here.

## Standing instruction

Stakeholder (SD-8, 2026-10-13): "Perform the remaining revise / review cycle yourself through the revision and sub-agent review cycle until all remaining blocking issues are closed." D4 remains **NOT AUTHORIZED**; a sub-agent PASS authorizes nothing by itself (gates G1-G4, §25).

Constraints:
- Work and push only on branch `ssds-8.0-graph-native-architecture` (`git push -u origin ssds-8.0-graph-native-architecture`). No pull requests.
- Never put model names or identifiers in repository artifacts or commit messages; Review records name the model family only.
- Commit and push every change; never leave the tree dirty.

## Current state

- Workplan: `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md`, design revision 19.
- Candidate under review: `ba7f738065237c26d15e4b7bdaf8e28543c61289` (workplan blob `d38c942d803506a27a835ee2da79a96d8db900d4`).
- Review handoff: `qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-19.md`.
- Review of revision 19: see "Latest Review" below.
- Previous Reviews, all NO-PASS: F9D9DE8 … 6FE1000, 4EC0024 (`qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-*-NO-PASS.md`).
- Open non-blocking item: N1 (the 2026-10-12 governing-version adoption instruction is paraphrase-only; needs the stakeholder's restatement).

### What revision 19 did (the recurring blocker family)

Every blocker since revision 10 has been one family: "what a failing assessment's adversity depends on". Revision 19 states it as three clauses (§6.6, audited in §27.32):

- **start:** a failing assessment counts in its own lineage's frames from admission; in the admitted state and other lineages' frames once its obligation is, or has been, admitted (`starts`, monotone latch; two anchor sets);
- **stop:** only a judgment addressing it, or a discriminating pair (five conditions on the failing outputs: identical reproduction, outcome flip, one reading with FAIL/PASS, a changed evidentiary premise incl. specification content, no disagreeing observation; withdrawal latch; execution custody);
- **standing:** a supersession stands on its own record's standing; a pair, per frame, only where an observation of its configuration on that frame's content shows another outcome and none reproduces the failing one (`here`); `IMMATERIALITY` keeps currency standing.

### Model check

`qualification/ssds80/s1_disagreement_model_check.py` (default mode REV19). Revision 19 results: depth 4, 317,340 transitions, 0 failures, 41/41 discriminators; depth 5, 13,039,519 transitions, 0 failures (~12 min). Sensitivity: `REV18=1` … `REV10=1` each fail owner-grounded properties (REV18 fails P10, P11, P12, Q2).

## Loop procedure

1. When a Review record arrives (written uncommitted by the reviewer under `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-<SHORTSHA>-<VERDICT>.md`): read it in full, verify each blocker independently against the candidate text, check the REVIEWER line names only the model family, then commit it ("Add SSDS 8.0 <shortsha> independent sub-agent D3 review (NO-PASS|PASS)") and push.
2. If NO-PASS, repair at the earliest owners as the next design revision. Apply the convergence owner: test each repair against the three clauses; prefer removing mechanism to adding it. Update together: frontmatter (`design_revision`, `prior_review`, `prior_reviewed_candidate`, `review_history`), the §0 block (REVISION line, PRIOR REVIEWS, INDEPENDENT D3 REVIEW), §0.1 (new section; demote the previous one to "#### Revision N (prior) record"), affected §6.6/§6.8/§6.9/§7.x/§10 text, §21, §22, §26, a new §27 round and minimum-architecture pass, §28, and the SSDS 8 section of `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. Extend the model check where the blocker is representable; keep the previous mode as a sensitivity mode that must fail owner-grounded properties.
3. Validate: `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`; `git diff --check`; the model check at depth 4 in every mode, and depth 5 in the default mode (run in the background; commit depth-4 figures first, then a follow-up commit recording depth 5).
4. Write the next review handoff by copying `qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-19.md` and updating: revision number, candidate SHA and workplan blob, previous candidate and record, prior-review list, the focus bullets, and the model-check mode list (add the previous mode). Commit and push it.
5. Launch a fresh-context general-purpose sub-agent with: "Read the file <repo>/qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-<N>.md. Everything below its horizontal rule (the line '---') is your complete task prompt. Follow it exactly: review the named candidate commit, write exactly one Review record file where it says, do not commit or push, and return only the record path, the verdict and a one-paragraph summary of blockers. In the REVIEWER line name only your model family." Then wait for it.
6. On PASS: commit the record, update §28 and the index to record it, and report to the stakeholder. Acceptance still needs stakeholder decisions and gates G1-G4; D4 stays NOT AUTHORIZED.

## Latest Review

Pending: the revision-19 Review was launched from `REVIEW-HANDOFF-SSDS-8.0-REVISION-19.md`; its record had not arrived when this file was written. If no `WORKPLAN-REVIEW-SSDS-8.0-BA7F738-*.md` is committed, relaunch it (step 5).
