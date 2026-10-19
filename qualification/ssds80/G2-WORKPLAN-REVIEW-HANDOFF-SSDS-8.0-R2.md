# Independent D3 Review handoff — SSDS 8 G2 shadow D3->D4 workplan, revision 2, candidate d8ab75c

This is the complete prompt for the independent D3 Review that gate G2 requires of the SSDS 8 shadow D3->D4 workplan (architecture workplan §25 criterion 13). It follows the NO-PASS of revision 1 (`qualification/ssds80/G2-WORKPLAN-REVIEW-SSDS-8.0-13D67BE-DIFFERENT-FAMILY-NO-PASS.md`) and supersedes the handoff `G2-WORKPLAN-REVIEW-HANDOFF-SSDS-8.0-R1.md`. The stakeholder arranges the reviewer; the record states the reviewer's model family and how it was engaged. This Review authorizes nothing.

**Context.** The 13d67be Review found two G2 blockers and three non-blocking findings:

- **B1:** S3's routing stranded an item after a coordination decision was answered while the condition still held and the item was unchanged.
- **B2:** the finding index omitted lettered and list-item findings and closed unmatched workplan findings by a blanket rule.
- **N1:** §5.5 could be read as making the G3 live measurements optional.
- **N2:** the §26 register row's fitness evidence was imprecise.
- **N3:** the A4 carry.

The author confirmed both blockers. B1's repair direction differed materially between options, so it went to the stakeholder as G2 question Q3, and the stakeholder chose one post-answer rule (SD-54, stakeholder decision record item 50, verbatim there; the message arrived truncated, and the record says how the author read the remainder). B2 was repaired by the author (G2 workplan §4.12).

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `d8ab75ce80daaf0316b70814cde7aae3bd70affd`. Review exactly this commit, not the branch head.
- **Subject:** `workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md`, revision 2 (blob `9a2ab7f2e10a74202faee29f1b87e0db7bd4695c`), and specifically the delta from revision 1: `git diff 13d67be9f935e5cf7c2a5befa0c981026553d4ea d8ab75ce80daaf0316b70814cde7aae3bd70affd -- workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md qualification/ssds80/models/ qualification/ssds80/G2-S4-FINDING-INDEX.md`. In particular:
  - §4.2's §10.2/§15.5 row, its item-level row and its §15 and §26 rows;
  - §4.9 and §4.11-§4.13;
  - §5.3 (group 1, 2, 3, 4, 5 and 7 discriminators) and §5.5;
  - the state and revision notes.
- **Evidence (design evidence, never authority):**
  - `models/routing.py` (the SD-54 settled reading; revision 1's rule kept as the reading `revision1`);
  - `models/cases_s3.py` (23 routing cases, ten for Q3);
  - `models/finding_index.py` and its output `G2-S4-FINDING-INDEX.md` (697 findings from 89 records, each with a disposition and witness);
  - `models/finding_inventory_check.py` (the independent inventory check, run by `run_models.py --seeds`).
- **Governing architecture:** `orchestrator/docs/ssds-8.0-architecture.md` at the candidate. Its semantic text is that of accepted candidate `2a17a8305db5ed312dc453f9d86ccf5faee8ab74`; confirm that the candidate differs from it in lifecycle lines only.
- **Also relevant:** the stakeholder decision record (items 49-50, SD-53, SD-54), the 13d67be record, catalogue §15.5 and §15.7, and Manual §10.3, §10.4, §15.4 and §15.5.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-design/SKILL.md` at the public source and read the owners it routes to.

The accepted Manual (with A1-A3) owns every architecture decision. SD-54 is a mechanism decision within Manual §10.3, §10.4 and §15.5. If it needs a Manual change or contradicts the Manual, report a G1 reopen and do not accept it as mechanism.

Treat the workplan, the register, the models, the index's dispositions, the author's reading of the truncated SD-54 message and this handoff as hypotheses. You may reuse the 13d67be Review's conclusions on unchanged parts as hypotheses, re-checking any that the delta touches.

## 3. What to judge (criterion 13)

1. **B1 repair.** Whether the SD-54 rule, as the §10.2/§15.5 row states it and `routing.py` realizes it, gives every post-answer state a meaningful continuation, a newly identified decision or a visible waiting route; this covers each allowed outcome (`AMEND` of the item or of another item, `PARTITION`, kept-fence `DECLINE`, `ESCALATE`) and each condition (spent budget, kept fence, item-level review naming no part). Check that it does so without silently bypassing the budget, unresolved findings or the fence decision, and without an unbounded loop of identical decisions. Check whether the recurrence step (a recurrence decision held for human attention after a proposed-default count) is consistent with Manual §15.4 and catalogue §15.7, and whether it is what SD-54 chose. Replay the 13d67be states and your own.
2. **B2 repair.** Whether the index is now complete for the Review corpus and whether each disposition has a recoverable witness. Sample, weighted to `CLOSED-LATER-REVIEW` (the later Review's quoted words), `NA-REMOVED`, `NA-REV23`, `CLOSED-PHASE-B` and the hand dispositions of §4.12. Check that `finding_inventory_check.py` is a genuinely different method from the extractor and that its exclusions hide no finding. Also check how the index separates a candidate's two Review records (B46C250, E548472).
3. **N1 and N2.** Whether §5.5 and the §26 row now say what the Review asked.
4. **Delta consistency.** Whether the delta changed any other register row, closure or Stage D element, and whether §4.11's closure of RR-5, RR-6 and RR-9 is at the criterion 11 bar.
5. **Remaining criterion 13 elements.** Whether anything in the 13d67be Review's judgments 1-7 that held at revision 1 no longer holds at revision 2.

Classify each finding as a **G2 blocker**, a **G1 reopen** (name the Manual owner), or **non-blocking**.

## 4. Method and checks

Reconstruct independently, falsify, and run a bounded Challenge Pass. Run at the candidate:

- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`
- `python3 -I qualification/ssds80/models/run_models.py --seeds`
- `python3 -I qualification/ssds80/models/finding_index.py`, comparing its output with the committed index
- `python3 -I qualification/ssds80/models/finding_inventory_check.py`
- `git diff --check 13d67be9f935e5cf7c2a5befa0c981026553d4ea d8ab75ce80daaf0316b70814cde7aae3bd70affd`
- confirm that `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee410ab9df0d94740cebb6969e161911b126`
- `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`

These are structural or diagnostic checks, not adequacy evidence. The models qualify only what their method discriminates (DS-001).

**Scientific checks for this Review.** State your material findings, or that you have none. State that you produced, ran or reviewed no realized scientific results (or give a null envelope). State any variants evaluated (count, kind, criterion), including how you chose sampled findings and probe states. Report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment. Report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file:

- if you are of the workplan author's (Claude) family: `qualification/ssds80/G2-WORKPLAN-REVIEW-SSDS-8.0-D8AB75C-PASS.md` or `-NO-PASS.md`;
- otherwise: `qualification/ssds80/G2-WORKPLAN-REVIEW-SSDS-8.0-D8AB75C-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`.

Include:

- a header block: GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, SCOPE, WORKPLAN blob, MANUAL blob and semantic candidate, REVIEW METHOD, and **REVIEWER** with model family only and engagement;
- `## SERIOUS CHALLENGE`;
- `## Verdict` (PASS or NO-PASS);
- G2 blockers and G1 reopens, each with its trajectory or evidence, owner text, minimum repair and discriminator;
- non-blocking findings;
- the five judgments of §3;
- your samples and probe states, and what each showed;
- what you verified and what you could not;
- scientific-checks answers;
- a common-mode note;
- a D4 statement: D4 stays not authorized, and a PASS supplies criterion 13's Review only.

Write scratch only under `ssds80-g2-review-d8ab75c` inside `$TMPDIR`. End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
