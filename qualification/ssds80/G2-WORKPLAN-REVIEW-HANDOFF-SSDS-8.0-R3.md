# Independent D3 Review handoff — SSDS 8 G2 shadow workplan revision 3 and Manual amendments A4-A6, candidate afd3be2

This is the complete prompt for one independent D3 Review with two parts:

- **part 1:** the G2 criterion-13 Review of the SSDS 8 shadow D3->D4 workplan, revision 3, as a delta review after the NO-PASS of revision 2 (`qualification/ssds80/G2-WORKPLAN-REVIEW-SSDS-8.0-D8AB75C-DIFFERENT-FAMILY-NO-PASS.md`);
- **part 2:** the delta review of three author-proposed amendments, A4-A6, to the accepted Architecture Manual.

This handoff file is committed after the candidate. Review the candidate commit named below, not the commit that adds this file. The stakeholder arranges the reviewer, and the record states the reviewer's model family and how it was engaged. This Review authorizes and accepts nothing.

**Context.** The d8ab75c Review found two G2 blockers:

- **B1:** recurrence was modelled as a separate decision; after a human answered it, the same key came back open with no continuation.
- **B2:** seven severity-labelled FFBAD17 findings were missing from the index, and the inventory check shared the extractor's punctuation assumption and unioned record identities.

It also raised non-blocking findings: N1, the provenance of the recurrence policy against SD-54's truncated text; N2, the A4 carry; and N3, the invocation's commit locator.

Revision 3 repairs them:

- **B1:** the routing family's third round, so revision 3 removes the special case rather than adding one. Recurrence is folded into SD-54's one answer-qualified chain, with a lifecycle property check over every answer chain (G2 workplan §4.13).
- **B2:** the extractor, the per-record check and its self-test are repaired (§4.12).

A4-A6 were carried by SD-53 (stakeholder decision record item 49) and are proposed by the author; they change no decision.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `afd3be2640b6a6e33a3d744efd76d324c6e5931a`. Review exactly this commit, using `git show` or a `git archive` snapshot.
- **Part 1 subject:** `workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md`, revision 3 (blob `f7ba1940a72bbb3724b95295568b40c0757f27cb`), and the delta `git diff d8ab75ce80daaf0316b70814cde7aae3bd70affd afd3be2640b6a6e33a3d744efd76d324c6e5931a -- workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md qualification/ssds80/models/ qualification/ssds80/G2-S4-FINDING-INDEX.md`. In particular:
  - §4.2's §10.2/§15.5 and §15 rows;
  - §4.11-§4.13;
  - §5.3 group 5;
  - the state and revision notes;
  - `models/routing.py` (`admitted_chain`, the settled reading; the readings `revision1` and `revision2` kept as refuted);
  - `models/cases_s3.py`;
  - `run_models.py`'s `lifecycle_properties`;
  - `models/finding_index.py`;
  - `models/finding_inventory_check.py` and its `--self-test`.
- **Part 2 subject:** `orchestrator/docs/ssds-8.0-architecture.md` (blob `314fa5e6a065868b0bf6176418705894f86c831d`), and the delta `git diff 2a17a8305db5ed312dc453f9d86ccf5faee8ab74 afd3be2640b6a6e33a3d744efd76d324c6e5931a -- orchestrator/docs/ssds-8.0-architecture.md`:
  - **A4:** the owner where a reach crosses items or plans (§5.10 (e));
  - **A5:** waiting with qualified independent people present (§32.2);
  - **A6:** runner-attribute costs (§17.5) and two reopen triggers (§32.3);
  - the lifecycle lines marking them proposed.

  Every other difference in that diff should be a lifecycle line from SD-53.
- **Also relevant:** the stakeholder record (items 49-50, SD-53, SD-54); the d8ab75c and 2a17a83 Review records; catalogue §15.5, §15.7, §17.5 and §32.3 and the owner definition in catalogue §5; Manual §10.3, §10.4, §15.4-§15.7.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-design/SKILL.md` at the public source and read the owners it routes to. `workflow-and-workplans.md` ("Authority lifecycle, mutation, and impact closure") governs amending accepted authority.

The accepted Manual at `2a17a83` is the baseline: A4-A6 must change no decision, invariant or authority boundary. A mechanism in the workplan that needs a Manual change is a G1 reopen, not a mechanism.

Treat the workplan, the models, the index's dispositions, the amendments and this handoff as hypotheses. You may reuse the d8ab75c Review's conclusions on unchanged parts as hypotheses, re-checking anything the delta touches.

## 3. What to judge

**Part 1 (criterion 13):**

1. **B1 repair.** Check that the consolidated chain gives every post-answer state, before and after the recurrence threshold, one of three things: a continuation, the chain's next answer-qualified decision, or a wait naming an outstanding prerequisite. Check that no answered decision is ever emitted as open again, that no budget, fence or finding is bypassed, and that the human hold is consistent with Manual §15.4 and catalogue §15.7. Check whether the lifecycle property check's seven properties are stated independently of the rule, and whether the enumeration's restrictions hide states. Replay the d8ab75c trajectory and your own.
2. **B2 repair.** Check that the index now contains the FFBAD17 findings with recoverable dispositions, that the check keys records by full identity, that its self-test really fails on removed rows, and that no further heading form is missed; audit the forms again over the corpus.
3. **Provenance.** Whether §4.13 and the §10.2/§15.5 row keep SD-54's received text apart from the author's recurrence proposal (d8ab75c N1).
4. **Delta consistency.** Whether anything else changed, and whether §4.11's closure of RR-5, RR-6 and RR-9 now meets the criterion-11 bar.

**Part 2 (A4-A6):**

5. Whether each amendment is a true consequence of accepted decisions and changes no decision: A4 against catalogue §5's owner definition and Manual §5.10 (b)-(e); A5 against §5.10 (f); A6 against catalogue §17.5 and §32.3. Check also whether each is consistent with the rest of the Manual.

Classify each finding as a **G2 blocker**, a **G1 blocker** (for A4-A6, or a G1 reopen; name the Manual owner) or **non-blocking**.

## 4. Method and checks

Reconstruct independently, falsify, and run a bounded Challenge Pass. Run at the candidate:

- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`
- `python3 -I qualification/ssds80/models/run_models.py --seeds`
- `python3 -I qualification/ssds80/models/finding_index.py`, comparing its output with the committed index
- `python3 -I qualification/ssds80/models/finding_inventory_check.py` and `... --self-test`
- `git diff --check d8ab75ce80daaf0316b70814cde7aae3bd70affd afd3be2640b6a6e33a3d744efd76d324c6e5931a`
- confirm `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee410ab9df0d94740cebb6969e161911b126`
- `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`

These are structural or diagnostic checks, not adequacy evidence (DS-001).

**Scientific checks for this Review.** State your material findings or that you have none. State that you produced, ran or reviewed no realized scientific results (or give a null envelope). State any variants evaluated (count, kind, criterion), including how you chose samples and probe states. Report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment. Report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file:

- if you are of the author's (Claude) family: `qualification/ssds80/G2-WORKPLAN-REVIEW-SSDS-8.0-AFD3BE2-PASS.md` or `-NO-PASS.md`;
- otherwise: `qualification/ssds80/G2-WORKPLAN-REVIEW-SSDS-8.0-AFD3BE2-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`.

The verdict covers part 1; state part 2's verdict (PASS or NO-PASS for A4-A6) separately inside.

Include:

- a header block: GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, SCOPE, WORKPLAN blob, MANUAL blob and baseline `2a17a83`, REVIEW METHOD, and **REVIEWER** with model family only and engagement;
- `## SERIOUS CHALLENGE`;
- `## Verdict`;
- blockers, each with its trajectory or evidence, owner text, minimum repair and discriminator;
- non-blocking findings;
- the five judgments of §3;
- your samples and probe states;
- what you verified and could not;
- scientific-checks answers;
- a common-mode note;
- a D4 statement: D4 stays not authorized; a PASS supplies criterion 13's Review and A4-A6 review evidence only, and accepts nothing.

Write scratch only under `/tmp/ssds80-g2-review-afd3be2`. End with one trailing newline. Return the record path, the verdicts and a one-paragraph summary of any blockers.
