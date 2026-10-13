# SSDS 8.0 revise/review loop — session continuation hand-off

This file lets a new session (any account) continue the stakeholder-directed revise/review cycle for the SSDS 8.0 architecture workplan. It is coordination state, not authority: the workplan, its Review records and `PROTOCOL-RELEASE-STATE.yaml` own everything stated here.

## Standing instruction

Stakeholder (SD-8, 2026-10-13): "Perform the remaining revise / review cycle yourself through the revision and sub-agent review cycle until all remaining blocking issues are closed." D4 remains **NOT AUTHORIZED**; a sub-agent PASS authorizes nothing by itself (gates G1-G4, §25).

Constraints:
- Work and push only on branch `ssds-8.0-graph-native-architecture` (`git push -u origin ssds-8.0-graph-native-architecture`). No pull requests.
- Never put model names or identifiers in repository artifacts or commit messages; Review records name the model family only.
- Commit and push every change; never leave the tree dirty.

## Current state

- Workplan: `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md`, design revision 20.
- Candidate under review: `947370d31fbd7bc53272bdbc401244624137c855` (workplan blob `40267d35b1ace7d505c0596a786cf8f3fd1d54de`).
- Review handoff: `qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-20.md`.
- Review of revision 20: launched as a fresh-context sub-agent; its record arrives uncommitted as `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-947370D-<VERDICT>.md` (see "Latest Review" below).
- Reviews, all NO-PASS: F9D9DE8 … 6FE1000, 4EC0024, BA7F738 (`qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-*-NO-PASS.md`).
- Open non-blocking item: N1 (the 2026-10-12 governing-version adoption instruction is paraphrase-only; needs the stakeholder's restatement).

### What revision 20 did (the recurring blocker family)

Every blocker since revision 10 has been one family: "what a failing assessment's adversity depends on". Revision 19 stated it as three clauses (start, stop, standing). The `ba7f738` Review found the recurrence at the comparators: start read obligation identity, stop and standing read the named evidentiary premises, and the reading read specification revisions. Revision 20 (§6.6, §10, audited in §27.34) keeps obligation identity for start only (an intended over-approximation) and decides every stop, standing and withdrawal on one notion, the **assessed content**:

- **executed content:** everything the execution read (specification unit, `EXECUTION_DEPENDS_ON` closure widened by §6.5, observed runner reads; the whole governed tree where completeness is not established); `on(o, K)` is the same-content test, and passing currency reads the same basis;
- **reading:** the specification and claim revisions applied. A failure under a never-admitted reading forms a **reading pair** (trial on admitted content, read under the admitted reading, no outcome change needed); it stands under that exact reading, and the trial's own outcome is then another assessed value.

Also: run enumeration in the pair record (by tree), floor deferral ending on admitted (possibly `INCOMPLETE`) observations, R2 class for assessor-read candidate pairs only with the trial on the base, mechanical resubmission of refused never-lost bytes, "admitted" defined once (any route).

### Model check

`qualification/ssds80/s1_disagreement_model_check.py` (default mode REV20). Content is (named, un-named) with reverts; outcomes 0/1/2; failures from a candidate's un-named content (`cand`) and under a never-admitted reading (`tight`, admitted by `ORACLE tight=True`). Revision 20 results: depth 4, 814,450 transitions, 0 failures, 64/64 discriminators; depth 5, 41,742,261 transitions, 0 failures (~52 min). Sensitivity: `REV19=1` fails P13, P14; `REV18=1` … `REV10=1` each fail owner-grounded properties.

## Loop procedure

1. When a Review record arrives (written uncommitted by the reviewer under `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-<SHORTSHA>-<VERDICT>.md`): read it in full, verify each blocker independently against the candidate text, check the REVIEWER line names only the model family, then commit it ("Add SSDS 8.0 <shortsha> independent sub-agent D3 review (NO-PASS|PASS)") and push.
2. If NO-PASS, repair at the earliest owners as the next design revision. Apply the convergence owner: test each repair against the three clauses; prefer removing mechanism to adding it. Update together: frontmatter (`design_revision`, `prior_review`, `prior_reviewed_candidate`, `review_history`), the §0 block (REVISION line, PRIOR REVIEWS, INDEPENDENT D3 REVIEW), §0.1 (new section; demote the previous one to "#### Revision N (prior) record"), affected §6.6/§6.8/§6.9/§7.x/§10 text, §21, §22, §26, a new §27 round and minimum-architecture pass, §28, and the SSDS 8 section of `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. Extend the model check where the blocker is representable; keep the previous mode as a sensitivity mode that must fail owner-grounded properties.
3. Validate: `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`; `git diff --check`; the model check at depth 4 in every mode, and depth 5 in the default mode (run in the background; commit depth-4 figures first, then a follow-up commit recording depth 5).
4. Write the next review handoff by copying `qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-19.md` and updating: revision number, candidate SHA and workplan blob, previous candidate and record, prior-review list, the focus bullets, and the model-check mode list (add the previous mode). Commit and push it.
5. Launch a fresh-context general-purpose sub-agent with: "Read the file <repo>/qualification/ssds80/REVIEW-HANDOFF-SSDS-8.0-REVISION-<N>.md. Everything below its horizontal rule (the line '---') is your complete task prompt. Follow it exactly: review the named candidate commit, write exactly one Review record file where it says, do not commit or push, and return only the record path, the verdict and a one-paragraph summary of blockers. In the REVIEWER line name only your model family." Then wait for it.
6. On PASS: commit the record, update §28 and the index to record it, and report to the stakeholder. Acceptance still needs stakeholder decisions and gates G1-G4; D4 stays NOT AUTHORIZED.

## Latest Review

Pending: the fresh-context sub-agent Review of revision 20, launched from `REVIEW-HANDOFF-SSDS-8.0-REVISION-20.md` against candidate `947370d31fbd7bc53272bdbc401244624137c855`. When its record arrives, follow the loop procedure above. The previous record, `qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-BA7F738-NO-PASS.md` (revision 19: blockers U1, U2; findings N1-N7), is repaired by revision 20 (§0.1).

Next action after a NO-PASS: revision 21 per the loop procedure, then `REVIEW-HANDOFF-SSDS-8.0-REVISION-21.md` (previous candidate `947370d31fbd7bc53272bdbc401244624137c855`, previous record that Review's file, add `REV20=1` to the sensitivity modes).
