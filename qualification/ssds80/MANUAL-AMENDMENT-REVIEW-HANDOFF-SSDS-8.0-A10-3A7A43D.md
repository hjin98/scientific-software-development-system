# Independent D3 re-Review handoff — SSDS 8 Architecture Manual amendment A10 (project memory), revision 2, candidate 3a7a43d

This is the complete prompt for one independent, different-family D3 re-Review of **proposed** amendment A10, revision 2, to the accepted SSDS 8 Architecture Manual. The re-Review accepts nothing: acceptance of A10 is the stakeholder's (as A9 was, SD-61 and SD-62). The run needs the stakeholder's approval.

**Context.** A10 re-derives items A, B, D and E of the SSDP 8.0 Amendment 1 handoff against the accepted Manual under SSDP 7.2.1 (SD-63, decision record item 59; recommendations adopted by SD-64, item 60; revision 1 and its re-Review approved by SD-65, item 61). Two different-family Reviews have run:

- revision 0 at `0368198` (`qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-0368198-A10-DIFFERENT-FAMILY-NO-PASS.md`): NO-PASS, blockers B1-B5;
- revision 1 at `97e5d6b` (`qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-97E5D6B-A10-DIFFERENT-FAMILY-NO-PASS.md`, committed at `7111a3a1`): B1, B2 and B4 closed; NO-PASS with two blockers still open, N1/B3 (S3 waiting did not withhold a judgment's S2 permissive effects) and N2/B5 (a late acceptance import skipped a retained owner-change interval).

Revision 2 repairs N1/B3 and N2/B5 at their owners and records the repairs in the proposal's §10 (its last paragraph). A10 remains a standalone proposal file: the Manual is unchanged at the candidate.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`, or the candidate commit itself if it has not yet been carried there (it is authored on a side branch and is carried by cherry-pick, which changes the commit identity but not the blobs below).
- **Candidate commit:** `3a7a43d6aa6a0f5c913e907af621720b2ecb1e22`. Review exactly this commit (`git show 3a7a43d6:<path>` or a `git archive` snapshot). If you receive a cherry-picked commit instead, check that the proposal blob below is identical and review that.
- **Previous candidate:** `97e5d6bca20e722c95461ae6f6c889631f738f8e`, proposal blob `e59873254b2fe1b6376446eec3fe380a18ba89e3`. The A10 delta is `git diff 97e5d6bc 3a7a43d6 -- qualification/ssds80/MANUAL-AMENDMENT-A10-PROPOSAL-SSDS-8.0-PROJECT-ENGINEERING-MEMORY.md`. Every other difference between the two commits is unrelated Stage D Phase F work, the revision 1 handoff and re-Review record, and the stakeholder decision record (SD-65): not under review here.
- **Subject:** `qualification/ssds80/MANUAL-AMENDMENT-A10-PROPOSAL-SSDS-8.0-PROJECT-ENGINEERING-MEMORY.md` (blob `3de6a9a219f5265a168223295acf95b301b17bbc`): the proposed §16.11 (its §4.1), in particular (e) and (g), and the pointer and consequence edits (its §4.2; edit 3 now also amends §8.3 step 7's refusal, edit 3a also §10.3's waiting rule, and revision 1's edits 3b, 3c and the §15.5 clause of edit 8 are withdrawn), judged as if applied to the accepted Manual `orchestrator/docs/ssds-8.0-architecture.md` (blob `fe43f04f5a698688727f7473a7c2e4d5345ae911`, unchanged at the candidate). Its §10 is the author's account of the repairs: a hypothesis to test, not authority.
- **Unchanged and only for consistency:** the item-C proposal `qualification/ssds80/PEM-SCHEMA-PROPOSAL-TYPED-APPLICABILITY-BINDINGS.md` (blob `34594fefd81337ead9473683d40755a60e108696`).
- **Relevant context:** both previous Review records above; the stakeholder decision record `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` (items 57-61; SD-61 to SD-65); the mechanism catalogue (non-authoritative); `orchestrator/src/ssds/interface/render.py` (the realized §16.3 injection events); `PROJECT-ENGINEERING-MEMORY.md` and `source/project_engineering_memory.py`.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-design/SKILL.md` at the public source and read the owners it routes to; `workflow-and-workplans.md` ("Authority lifecycle, mutation, and impact closure") governs amending accepted authority. PEM meaning is owned by `source/shared/references/project-engineering-memory.md` and `project-engineering-memory-schema.md` at the public source; A10 must not change, narrow or widen it. The accepted Manual (A1-A9) is the baseline.

## 3. What to judge (workplan §25 criterion 11, for the changed decisions)

1. **N1/B3.** Apply the previous re-Review's discriminator (proposal §7 case 21). Does (g)(2), Admission refusing every passing judgment and principal decision of a request whose result states an uncertainty no standing `HUMAN_DECISION` accepts, close every permissive effect: S2 currency, plan coverage (§11.2), subject validity (§5.5) and S3 answering and discharge? Is the citing `standing` basis entry (§4.1) a sound way for S2 to read the acceptance, with the stratum order preserved (§5.1, §5.8)? In (g)(1), does every permissive effect of work under review pass through the review's judgment? Are never-lost records kept, and is the regress bounded (acceptance keyed on obligation and cause)? Does the waiting rule fit §10.3's no-stranded rule, including a reader that recovers before the human decides?
2. **N2/B5.** Apply case 22. Is the reference position now well defined: where the publication took effect in project history, for an import the earliest admitted position whose observed integration head contains the accepted revision, or genesis? Can any import, re-import, requalification, tenure change or loss boundary still reset or skip a retained owner-change interval? Is "review required across a loss boundary" consistent with §23.6? Does keying one decision per owner change (case 23) satisfy register A10-R2?
3. **New defects introduced by the repairs.** Check the changed text against its siblings: §3.5 (who may submit `HUMAN_DECISION`), §4.1-§4.3, §5.2's acting rule, §5.5-§5.8, §8.3 steps 6-9, §10.2-§10.4 (with revision 1's S3 conditions withdrawn), §11.2, §12.5, §15.2-§15.5, §19.2, §19.9, §22.1 (the integration observation) and §23.6.
4. **Closed blockers stay closed.** Whether revision 2 reopens B1, B2 or B4, or weakens anything the previous Reviews judged sound.
5. **Cost and disclosure.** Whether the added cost (a refused judgment or decision redone by a new task after the human accepts; review-required bindings across a loss boundary) is disclosed in §32.2 and §9.

Classify findings as a G1 blocker (criterion 11: a contradiction, an omitted or unrealizable invariant, or a decision a conforming realization can satisfy while violating upstream meaning), a G2 register entry, or non-blocking. If accepted authority itself (the Manual or the PEM owners) appears false, contradictory or inadequate, raise a SERIOUS CHALLENGE routed to its owner instead of reviewing around it. You need not re-review parts that revision 2 leaves unchanged, except as item 4 asks.

## 4. Method and checks

Reconstruct independently, falsify, and run a bounded Challenge Pass on the repaired text and its siblings. Re-run both previous Reviews' counterexample trajectories for B3 and B5 (including the plan-acceptance, subject-acceptance and late-import trajectories) against revision 2, and write new ones for item 3. At the candidate run:

```bash
python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v
git diff --check 97e5d6bca20e722c95461ae6f6c889631f738f8e 3a7a43d6aa6a0f5c913e907af621720b2ecb1e22
git diff --stat 97e5d6bca20e722c95461ae6f6c889631f738f8e 3a7a43d6aa6a0f5c913e907af621720b2ecb1e22 -- qualification/ssds80/
python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md
```

Confirm that `orchestrator/docs/ssds-8.0-architecture.md`, `orchestrator/docs/architecture.md`, `PROJECT-ENGINEERING-MEMORY.md`, `source/` and `dist/` are byte-unchanged from `97e5d6bc`. Report `orchestrator/src/` changes as Phase F work outside this review. These are structural checks, not adequacy evidence. The PEM validator needs a Git repository for route realization; run it in the clone. No executable model exists for A10, so do not treat the proposal's §7 cases as run. Write scratch only under `ssds80-manual-review-a10-3a7a43d` inside `$TMPDIR`.

**Scientific checks for this Review.** State your material findings or that you have none; state that you produced, ran or reviewed no realized scientific results (or give a null envelope); state any variants evaluated (count, kind, criterion); report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment; report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the amendment author's model family, `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-3A7A43D-A10-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-3A7A43D-A10-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Include:

- a header block: GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, SCOPE, MANUAL blob, PROPOSAL blob, REVIEW METHOD, and **REVIEWER** with the model family only and how you were engaged;
- `## SERIOUS CHALLENGE`;
- `## Verdict`: PASS or NO-PASS for A10 revision 2 as a D3 change;
- per blocker N1/B3 and N2/B5: closed or open, with the trajectory that shows it; and whether B1, B2 and B4 stay closed;
- new G1 blockers, each with its trajectory, the owner text, the minimum repair and a discriminator;
- register entries and non-blocking findings;
- the five judgments of §3;
- what you verified and what you could not;
- the scientific-checks answers;
- a common-mode note;
- a D4 statement: D4 stays not authorized.

End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
