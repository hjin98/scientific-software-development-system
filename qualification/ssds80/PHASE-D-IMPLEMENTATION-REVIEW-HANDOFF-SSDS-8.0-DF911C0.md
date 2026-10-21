# Independent D4 Review handoff — SSDS 8 Phase D, repaired candidate df911c0, within the SD-59 threat boundary

This is the complete prompt for one independent Review of the Phase D implementation and exit as repaired after the `b341109` Review, judged within the threat boundary the stakeholder set for the SSDS home (SD-59), with a confirmation that Manual amendments A7 and A8 are unchanged since they passed. The Review accepts nothing: a Phase D PASS lets Phase E's dependent work start (G2 workplan §5.1 item 5); acceptance is G3; acceptance of A7's and A8's text is the stakeholder's.

**Context.** Five Reviews preceded this one, all different-family and recorded in `qualification/ssds80/`: `0e49deb`, `517af45`, `137b763`, `d8bdfd3` and `b341109` (`PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-B341109-DIFFERENT-FAMILY-NO-PASS.md`: judged within SD-59; Phase D NO-PASS, A7 and A8 PASS confirmed, no SERIOUS CHALLENGE; A-B11 an unwitnessed recovery record suppressing observed checkpoints and the mark, A-B12 a repository nested in the operator workspace overwritten, A-B13 a short write published as complete, NF7, and an environment note on an empty `/tmp/.git`). After the fourth, the stakeholder set a threat boundary for the SSDS home and directed structural fixes (SD-59, stakeholder decision record item 55). `df911c04` addresses the `b341109` findings, as Phase D plan §6 (the qualification reading) and §9 ("After the b341109 Review") describe.

**The threat boundary you judge within (SD-59).** The SSDS home is the operator's private state, trusted as the operator's own account is. Phase D guarantees, statically and before any effect: the home lies outside every repository; the operator tree a ledger uses holds no symbolic link; a genesis creates its ledger repository afresh; every replaced operator file is published atomically (a fresh, exclusively created file renamed over the name), never written through; the ledger id is a unit identity and every path stays inside the home. Phase D defends against misconfiguration and accidental aliasing, not against an adversary. Outside Phase D, for Phase H (Manual §24-§25, §31): an actor with write access to the home or the operator's account; concurrent replacement of paths between a check and a write; mount and bind aliases; hostile global Git configuration, templates or hooks; filesystems that defeat these primitives; a coherently rewritten private cache. **Report a case outside the boundary as a Phase H item, not a Phase D blocker.** The boundary does not narrow currentness: qualification (§23) must hold within the declared witness fault model, and a qualification defect there is a Phase D blocker. If you judge the boundary itself inconsistent with the Manual or G2 workplan, say so as a SERIOUS CHALLENGE routed to its owner rather than reviewing around it.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `df911c045920d317f1c81da90e71d14906feecf4`. Review exactly this commit.
- **Previous candidate:** `b341109a6a23340692d0d7cddfd918666c6d2495`. The repair delta is `git diff b341109a df911c04`; the whole Phase D delta is `git diff e88d90de df911c04` (`e88d90de`: G2 authorized, Manual A1-A6 accepted).
- **Manual:** `orchestrator/docs/ssds-8.0-architecture.md`, blob `6226f323365966bbcf653545f3a35b1fd7d6e060`, the blob passed for A7 and A8 at `517af45` and confirmed at `137b763`, `d8bdfd3` and `b341109`. The catalogue is unchanged in this delta.
- **Decisions:** `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` items 52-55 (SD-56 to SD-59).
- **Plan:** `workplans/active/SSDS-8.0-G2-PHASE-D-PLAN.md`: §2 (threat boundary), §6 (the qualification reading, the old allowance withdrawn), §8 (readings), §9 (repairs after each Review).
- **Step 7 evidence:** `qualification/ssds80/PHASE-D-STEP7-SHADOW-GENESIS-EVIDENCE-SSDS-8.0.md`.
- **Governing owners:** the accepted Manual, the G2 workplan (`workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md`) and its §4.2 register, the catalogue as that register settles it. The Stage S models under `qualification/ssds80/models/` are evidence, not authority.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-implementation/SKILL.md` at the public source and read the owners it routes to; for the A7 and A8 confirmation, `source/roles/software-design/SKILL.md`. Treat the author's account, the plan and this handoff as hypotheses; SD-59 is the stakeholder's decision.

## 3. What to judge

1. **Each `b341109` finding.** For A-B11, A-B12, A-B13 and NF7: is it closed at its owner, with the Review's discriminator kept as a test that fails without the repair? Rerun that Review's executed probes: the rewind with an uncheckpointed `LEDGER_LOSS` (and `FORK_RESOLUTION`) over one honest `LOCAL_TRUST` witness, expecting nothing current until the witness holds the recovery entry, then current at it; a committed repository at an operator write location (`genesis/<id>`, `state/<id>` and the directories holding them), expecting refusal before its tracked bytes or state change, with a clean control admitting; the high-water mark and a witness checkpoint under a one-byte `RLIMIT_FSIZE`, expecting a visible failure, the old mark intact, no partial checkpoint held and no temporary left, and a progressing short writer completing; the NF7 order, annotated-local and class-scope cases.
2. **Qualification.** Whether `qualify` meets §23.1, §23.4 and §23.6 within the declared witness fault model: `H*` is the highest quorum-held prefix whose own recovery records explain every observed checkpoint and the retained mark; a recovery record outside that prefix abandons nothing; `ROLLBACK`, `BEHIND`, `FORK`, `RETIRED`, read repair and a genuinely unwitnessed provisional successor are preserved; and the consumer derives only through `H*`. Try further recovery orderings (several recovery records, one inside and one outside the prefix; a recovery record that is itself abandoned).
3. **The structural rules, within SD-59.** Whether atomic publish with complete writes, the home outside every repository and holding none but its ledgers, no symbolic link in the operator tree, and a fresh ledger repository together close write containment for misconfiguration and accidental aliasing at every write path (workspace files, keys, the high-water mark, witness checkpoints, Git writes in the ledger repository), and whether any in-boundary route remains. Classify every route you find as in or out of the boundary. Judge whether the repository marker (a `.git` file, a `.git` directory with `HEAD`, or a bare layout) is the right test, given that an empty `.git` directory is no longer treated as a repository.
4. **New defects from the repairs**, including the checkpoint writer's hard-link naming (no replacement; an existing checkpoint of that name must be byte-identical) and failure cleanup, and the order- and scope-aware fitness rule on ordinary code.
5. **Everything previously judged** (the `0e49deb` handoff's §3 items 1-11, and each earlier finding's disposition) still holds at this candidate, the A7 and A8 verdicts stand on the unchanged Manual blob, and the step 7 exit meets plan §3 step 7 and G2 workplan §5.1 items 2 and 5.

Classify findings as Phase D blockers (with the owner text, minimum repair and a discriminator), Phase H items (outside SD-59's boundary) or non-blocking.

## 4. Method and checks

Reconstruct independently, falsify, and run a bounded Challenge Pass on the repair delta and its siblings. Use a Python 3.11 or newer interpreter. At the candidate run:

```bash
python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt
python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v
python orchestrator/scripts/run_core_tests.py
python orchestrator/scripts/generate_protocol_snapshot.py --check
python -m unittest discover -s tests -v
python3 -I qualification/ssds80/models/run_models.py --seeds
git diff --check e88d90de df911c04
```

and confirm `source/`, `dist/` and `orchestrator/docs/architecture.md` are byte-unchanged from `e88d90de`, and that the frozen profiles and protocol snapshots moved by the rename only. These are structural and diagnostic checks, not adequacy evidence; mutate where a test's discriminating power is in doubt. Write scratch only under `ssds80-phase-d-review-df911c0` inside `$TMPDIR`, including any SSDS home you create; write nothing to `~/.ssds`. The stakeholder's admitted shadow ledger is private operator state outside the candidate: judge the evidence record, and reproduce the path on a throwaway home if you need to.

**Scientific checks for this Review.** State your material findings or that you have none; state that you produced, ran or reviewed no realized scientific results (or give a null envelope); state any variants evaluated (count, kind, criterion); report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment; report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the author's (Claude) family, `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-DF911C0-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-DF911C0-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Include: a header block (GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, BASELINE, SCOPE including the SD-59 boundary, MANUAL blob, REVIEW METHOD, **REVIEWER** with model family only and how you were engaged); `## SERIOUS CHALLENGE`; `## Verdict` for the Phase D implementation and exit (PASS or NO-PASS; say whether the exit or only the implementation passes), and a line confirming or withdrawing the A7 and A8 verdicts; a disposition of every `b341109` finding; Phase D blockers with owner text, minimum repair and discriminator; Phase H items; non-blocking findings; the judgments of §3; what you verified and could not; scientific-checks answers; a common-mode note; a statement that nothing beyond shadow is authorized. End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
