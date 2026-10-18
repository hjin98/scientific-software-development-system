# Independent D3 Review handoff — SSDS 8 Architecture Manual amendment A1, candidate 3937b92 (delta review)

**Superseded before any review was run** by `MANUAL-AMENDMENT-REVIEW-HANDOFF-SSDS-8.0-A1A2-388CAB2.md`, which reviews A1 together with A2 (SD-52). Do not run this handoff.

This is the complete prompt for an independent D3 Review of one proposed amendment to the **accepted** SSDS 8 Architecture Manual. The stakeholder asked for a GPT-family Review of the delta; the record states its family and how the reviewer was engaged.

**Context.** The Manual was accepted at gate G1 on semantic candidate `dddfedf72ed9711b8fcd46865b5c99eb50771ac5` (SD-50, stakeholder decision record item 46), after a GPT-family G1 Review PASS (`qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-DDDFEDF-DIFFERENT-FAMILY-PASS.md`). G2 work then began (`workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md`). Its Stage S design models (`qualification/ssds80/models/`) found a lawful state in which the accepted §5.10 (h)(4) ("liftable or waiting") is false if §5.10 (f)'s "No eligible judge" is read as written: a NO-PASS recorded in the frame of an abandoned transformation X vetoes the pass of a re-dispatch Z; the owner is qualified and independent of the NO-PASS's judged content, but a supersession of a judgment about X must declare X's frame (§7.5) and never acts in Z's; the owner authored part of Z's judged content and cannot relieve Z; the adjudicator authored the NO-PASS's content. The stakeholder chose SD-51 (record item 47, verbatim there): define eligibility per route and per state. Amendment A1 is that change.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `3937b92b184cdc97872d3f2b1fd07410d62168e8`. Review exactly this commit (`git show 3937b92b184cdc97872d3f2b1fd07410d62168e8:<path>` or a `git archive` snapshot).
- **Subject:** `orchestrator/docs/ssds-8.0-architecture.md` (blob `6a5b2e1289e56890e083deab82019191d40bf43b`), and specifically the delta `git diff dddfedf72ed9711b8fcd46865b5c99eb50771ac5 3937b92b184cdc97872d3f2b1fd07410d62168e8 -- orchestrator/docs/ssds-8.0-architecture.md`: §5.10 (f) (a definition of an eligible judge per route and per state, and "No eligible judge" restated over it), §5.10 (h)(4), §10.2's `HUMAN_ATTENTION` trigger, §10.3's dispatch rule, and lifecycle lines marking A1 proposed. Other differences in that diff are the G1-acceptance lifecycle lines (SD-50).
- **Evidence (realizability only, not authority):** `qualification/ssds80/models/` at the candidate, in particular `judgment.py` (route enumeration per state, the two readings of "No eligible judge"), `cases_s2.py` (`ROUTE_CASES`, `G1_QUESTIONS`) and `run_models.py`; run `python3 -I qualification/ssds80/models/run_models.py --seeds`.
- **Also relevant:** the stakeholder decision record (items 44-47; SD-48 to SD-51), the G2 workplan §4.2, §4.5 and §4.6, and the 8c1f2f2 and dddfedf Review records.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-design/SKILL.md` at the public source and read the owners it routes to; `workflow-and-workplans.md` ("Authority lifecycle, mutation, and impact closure") governs amending accepted authority. The accepted Manual at `dddfedf` is the baseline: A1 must not weaken any of its decisions or invariants beyond what SD-51 states. Treat the models, the workplan, the author's description of the gap and this handoff as hypotheses.

## 3. What to judge (workplan §25 criterion 11, for the changed decisions)

1. **The gap.** Whether the stated state is lawful under the dddfedf text and whether (f) as written and (h)(4) do disagree there; or whether some admissible route the author missed ends the objection (which would make A1 unnecessary, though not wrong).
2. **The amendment.** Whether the per-route, per-state definition of an eligible judge closes the gap; whether each route's independence is measured over the right judged content (objection's for reassessment, supersession and adjudication; relieved target's for relief; answered target's for an answer); whether "would act in that state" and "basis admissible there" are stated consistently with §5.2, §7.5 and §5.10 (e); and whether the definition reaches only what SD-51 says.
3. **Siblings.** Every other statement that quantifies over states or depends on eligibility — §5.10 (e)-(h) invariants 1-9, §10.2, §10.3 (including its "one class waits by design"), §0.3 R9 and R13, §32.2 — is consistent with A1, or name the one that is not. (The 8c1f2f2 round showed a decision that adds a state must be checked against every such statement.)
4. **No new closure route.** That A1 creates no way for work to proceed on a non-independent pass, and no route by which human attention, waiting or a risk override ends an objection.
5. **Cost.** Whether A1's added waiting (an independent, qualified actor whose record cannot act where needed) is disclosed where §32.2 discloses waiting costs, or should be.

Classify findings as a G1 blocker (criterion 11), a G2 register entry, or non-blocking. You need not re-review the unchanged Manual.

## 4. Method and checks

Reconstruct independently, falsify, and run a bounded Challenge Pass on the delta and its siblings. Run at the candidate: `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`; `git diff --check dddfedf72ed9711b8fcd46865b5c99eb50771ac5 3937b92b184cdc97872d3f2b1fd07410d62168e8`; `python3 -I qualification/ssds80/models/run_models.py --seeds`; and confirm `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee410ab9df0d94740cebb6969e161911b126`. These are structural or diagnostic checks, not adequacy evidence. A PASS accepts nothing: acceptance of A1 is the stakeholder's.

**Scientific checks for this Review.** State your material findings or that you have none; state that you produced, ran or reviewed no realized scientific results (or give a null envelope); state any variants evaluated (count, kind, criterion); report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment; report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the Manual author's (Claude) family, `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-3937B92-A1-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-3937B92-A1-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Include: a header block (GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, SCOPE, MANUAL blob, baseline `dddfedf`, REVIEW METHOD, **REVIEWER** with model family only and engagement); `## SERIOUS CHALLENGE`; `## Verdict` (PASS or NO-PASS); G1 blockers with trajectory, owner text, minimum repair and discriminator; register entries; non-blocking findings; the five judgments of §3; what you verified and could not; scientific-checks answers; a common-mode note; a D4 statement (D4 stays not authorized). Write scratch only under `ssds80-manual-review-3937b92` inside `$TMPDIR`. End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
