# Independent D4 Review handoff — SSDS 8 Phase D, repaired candidate 137b763

This is the complete prompt for one independent Review of the Phase D implementation and exit as repaired after the `517af45` Review, with a confirmation that Manual amendments A7 and A8 are unchanged since that Review passed them. The Review accepts nothing: a Phase D PASS lets Phase E's dependent work start (G2 workplan §5.1 item 5); acceptance is G3; acceptance of A7's and A8's text is the stakeholder's.

**Context.** The `517af45` Review, `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-517AF45-DIFFERENT-FAMILY-NO-PASS.md` (handoff `PHASE-D-IMPLEMENTATION-REVIEW-HANDOFF-SSDS-8.0-517AF45.md`), returned (A) NO-PASS, A7 PASS and A8 PASS, with no SERIOUS CHALLENGE. Its implementation blockers were A-B3 retained (a symbolic link at a workspace file escaped the SSDS home), A-B5 (the currentness consumer kept no high-water mark) and A-B6 (an `INCOMPLETE` judgment could bound a reproduction); its non-blocking findings were NF1-NF3. All are addressed in `137b7633`, as Phase D plan §9 ("After the 517af45 Review") describes. The earlier `0e49deb` Review and its dispositions remain part of the history.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `137b7633945c1a52cc8a590a5fbf07402f57d982`. Review exactly this commit.
- **Previous candidate:** `517af4551e0b4ea000bd80fe47b1f1f9b4e0e562`. The repair delta is `git diff 517af455 137b7633`; the whole Phase D delta is `git diff e88d90de 137b7633` (`e88d90de`: G2 authorized, Manual A1-A6 accepted).
- **Manual:** `orchestrator/docs/ssds-8.0-architecture.md`, blob `6226f323365966bbcf653545f3a35b1fd7d6e060`, the blob the `517af45` Review passed for A7 and A8. The mechanism catalogue changed in the delta (NF2).
- **Decisions:** `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` items 52-54 (SD-56, SD-57, SD-58).
- **Plan:** `workplans/active/SSDS-8.0-G2-PHASE-D-PLAN.md`, §8 (readings) and §9 (the repairs after both Reviews).
- **Step 7 evidence:** `qualification/ssds80/PHASE-D-STEP7-SHADOW-GENESIS-EVIDENCE-SSDS-8.0.md`.
- **Governing owners:** the accepted Manual, the G2 workplan (`workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md`) and its §4.2 register, the catalogue as that register settles it. The Stage S models under `qualification/ssds80/models/` are evidence, not authority.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-implementation/SKILL.md` at the public source and read the owners it routes to; for the catalogue alignment and the A7/A8 confirmation, `source/roles/software-design/SKILL.md`. Treat the author's account, the plan and this handoff as hypotheses.

## 3. What to judge

1. **Each `517af45` finding.** For A-B3, A-B5, A-B6 and NF1-NF3: is it closed at its owner, with the Review's discriminator kept as a test that fails without the repair? Rerun that Review's executed probes where you can: a leaf symbolic link at a workspace file through real preparation and through the report consumer, with the outside sentinel byte-identical; qualifying and presenting head 1 through the actual CLI, then restoring the ledger and witness to 0 while keeping the evaluator's mark (expect `ROLLBACK`, no current assertion, non-zero exit); an `INCOMPLETE` completeness judgment as a reproduction's sole bound beside a positive `COMPLETE` control; the NF1 pure-attribute control; a retirement marker at the consumer.
2. **New defects from the repairs.** In particular: whether the high-water mark only rises and never records a head not presented current; whether refusing every symbolic link at a home file is coherent with the home's other paths and leaves the positive genesis path intact; whether `bound`'s `COMPLETE` requirement interacts correctly with vetoes, supersession and the support graph; whether the narrowed fitness rule still catches every route the `0e49deb` N2 probe and its variants use (import, module attribute, dotted module attribute, relative import).
3. **The catalogue alignment (NF2).** The §0.3 R1 cell, `bound(o, K)` with its `COMPLETE` requirement, §5.6, the §6.5 construction rule, the §6.6 polarity note, the stratification check and the class check now state the SD-58 rule, and no catalogue passage still states the literal one. Confirm the Manual blob is the one the `517af45` Review passed, so its A7 and A8 verdicts stand; if anything in the delta changes their basis, say so.
4. **Everything previously judged** (the `0e49deb` handoff's §3 items 1-11, and the `517af45` handoff's §3 (A)) still holds at this candidate, and the step 7 exit meets plan §3 step 7 and G2 workplan §5.1 items 2 and 5.

Classify findings as blockers (with the owner text, minimum repair and a discriminator) or non-blocking. If accepted authority is itself false or contradictory, raise a SERIOUS CHALLENGE and route it to its owner.

## 4. Method and checks

Reconstruct independently, falsify, and run a bounded Challenge Pass on the repair delta and its siblings. Use a Python 3.11 or newer interpreter. At the candidate run:

```bash
python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt
python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v
python orchestrator/scripts/run_core_tests.py
python orchestrator/scripts/generate_protocol_snapshot.py --check
python -m unittest discover -s tests -v
python3 -I qualification/ssds80/models/run_models.py --seeds
git diff --check e88d90de 137b7633
```

and confirm `source/`, `dist/` and `orchestrator/docs/architecture.md` are byte-unchanged from `e88d90de`, and that the frozen profiles and protocol snapshots moved by the rename only. These are structural and diagnostic checks, not adequacy evidence; mutate where a test's discriminating power is in doubt. Write scratch only under `ssds80-phase-d-review-137b763` inside `$TMPDIR`, including any SSDS home you create; write nothing to `~/.ssds`. The stakeholder's admitted shadow ledger is private operator state outside the candidate: judge the evidence record, and reproduce the path on a throwaway home if you need to.

**Scientific checks for this Review.** State your material findings or that you have none; state that you produced, ran or reviewed no realized scientific results (or give a null envelope); state any variants evaluated (count, kind, criterion); report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment; report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the author's (Claude) family, `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-137B763-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-137B763-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Include: a header block (GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, BASELINE, SCOPE, MANUAL blob, REVIEW METHOD, **REVIEWER** with model family only and how you were engaged); `## SERIOUS CHALLENGE`; `## Verdict` for the Phase D implementation and exit (PASS or NO-PASS; say whether the exit or only the implementation passes), and a line confirming or withdrawing the A7 and A8 verdicts; a disposition of every `517af45` finding; new blockers with owner text, minimum repair and discriminator; non-blocking findings; the judgments of §3; what you verified and could not; scientific-checks answers; a common-mode note; a statement that nothing beyond shadow is authorized. End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
