# Independent D4 Review handoff — SSDS 8 Phase D, repaired candidate b341109, within the SD-59 threat boundary

This is the complete prompt for one independent Review of the Phase D implementation and exit as repaired after the `d8bdfd3` Review, judged within the threat boundary the stakeholder set for the SSDS home (SD-59), with a confirmation that Manual amendments A7 and A8 are unchanged since they passed. The Review accepts nothing: a Phase D PASS lets Phase E's dependent work start (G2 workplan §5.1 item 5); acceptance is G3; acceptance of A7's and A8's text is the stakeholder's.

**Context.** Four Reviews preceded this one, all different-family and recorded in `qualification/ssds80/`: `0e49deb`, `517af45`, `137b763` and `d8bdfd3` (`PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-D8BDFD3-DIFFERENT-FAMILY-NO-PASS.md`: Phase D NO-PASS, A7 and A8 PASS confirmed, no SERIOUS CHALLENGE; A-B8 hard-linked operator outputs, A-B9 an observed checkpoint treated as a provisional successor, A-B10 a home inside a repository, NF6). Because each Review's containment findings moved to a new filesystem edge, the stakeholder directed structural fixes and a recorded threat boundary instead of further case-by-case repair (SD-59, stakeholder decision record item 55, verbatim there). `b341109a` implements them, as Phase D plan §2 ("Threat boundary for the SSDS home") and §9 ("After the d8bdfd3 Review") describe.

**The threat boundary you judge within (SD-59).** The SSDS home is the operator's private state, trusted as the operator's own account is. Phase D guarantees, statically and before any effect: the home lies outside every repository; the operator tree a ledger uses holds no symbolic link; a genesis creates its ledger repository afresh; every replaced operator file is published atomically (a fresh, exclusively created file renamed over the name), never written through; the ledger id is a unit identity and every path stays inside the home. Phase D defends against misconfiguration and accidental aliasing, not against an adversary. Outside Phase D, for Phase H (Manual §24-§25, §31): an actor with write access to the home or the operator's account; concurrent replacement of paths between a check and a write; mount and bind aliases; hostile global Git configuration, templates or hooks; filesystems that defeat these primitives; a coherently rewritten private cache. **Report a case outside the boundary as a Phase H item, not a Phase D blocker.** The boundary does not narrow currentness: qualification (§23) must hold within the declared witness fault model, and a qualification defect there is a Phase D blocker. If you judge the boundary itself inconsistent with the Manual or G2 workplan, say so as a SERIOUS CHALLENGE routed to its owner rather than reviewing around it.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `b341109a6a23340692d0d7cddfd918666c6d2495`. Review exactly this commit.
- **Previous candidate:** `d8bdfd3efa233fec8d7fd8a83803bca1ba77584b`. The repair delta is `git diff d8bdfd3e b341109a`; the whole Phase D delta is `git diff e88d90de b341109a` (`e88d90de`: G2 authorized, Manual A1-A6 accepted).
- **Manual:** `orchestrator/docs/ssds-8.0-architecture.md`, blob `6226f323365966bbcf653545f3a35b1fd7d6e060`, the blob passed for A7 and A8 at `517af45` and confirmed at `137b763` and `d8bdfd3`. The catalogue is unchanged in this delta.
- **Decisions:** `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` items 52-55 (SD-56 to SD-59).
- **Plan:** `workplans/active/SSDS-8.0-G2-PHASE-D-PLAN.md`: §2 (threat boundary), §6 (the qualification reading, the old allowance withdrawn), §8 (readings), §9 (repairs after each Review).
- **Step 7 evidence:** `qualification/ssds80/PHASE-D-STEP7-SHADOW-GENESIS-EVIDENCE-SSDS-8.0.md`.
- **Governing owners:** the accepted Manual, the G2 workplan (`workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md`) and its §4.2 register, the catalogue as that register settles it. The Stage S models under `qualification/ssds80/models/` are evidence, not authority.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-implementation/SKILL.md` at the public source and read the owners it routes to; for the A7 and A8 confirmation, `source/roles/software-design/SKILL.md`. Treat the author's account, the plan and this handoff as hypotheses; SD-59 is the stakeholder's decision.

## 3. What to judge

1. **Each `d8bdfd3` finding.** For A-B8, A-B9, A-B10 and NF6: is it closed at its owner, with the Review's discriminator kept as a test that fails without the repair? Rerun that Review's executed probes: the three hard-link trajectories (`report.json` through prepare, sign and admit; `derivation.json` through the CLI; the high-water mark), expecting the product file byte-identical; the three-witness `TEAM` case (head 1 held by `w0` and `w2`, a read reaching `w0` and `w1`) with no mark and a mark at 0, expecting no current head 0, then read repair giving head 1, and a never-checkpointed successor staying provisional; a home inside the product worktree, expecting refusal before anything is created, and a linked home resolving outside, expecting success; the NF6 pure and alias cases.
2. **The structural rules, within SD-59.** Whether the four rules (atomic publish, home outside every repository, no symbolic link in the operator tree, fresh ledger repository) together close write containment for misconfiguration and accidental aliasing at the Admission and ledger write owners, every write path included (workspace files, keys, the high-water mark, witness checkpoints, Git writes in the ledger repository); and whether any in-boundary route remains. Classify every route you find as in or out of the boundary.
3. **Qualification.** Whether `qualify` now meets §23.1 and §23.4 within the declared witness fault model: `H*` extends every observed checkpoint and the retained mark; the provisional successor is only the replica's own entry no responder shows a checkpoint for; `ROLLBACK`, `BEHIND`, `FORK`, `RETIRED` and admitted abandonment are preserved; and the consumer derives only through `H*`. The corrected oracle in `test_ledger.Qualification.test_qualification_states` and the new property check carry it.
4. **New defects from the repairs**, including whether `publish_private` keeps durability (file and directory fsync) and leaves no stale temporaries on failure, and whether the scope-aware fitness rule has a new false positive or negative on ordinary code.
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
git diff --check e88d90de b341109a
```

and confirm `source/`, `dist/` and `orchestrator/docs/architecture.md` are byte-unchanged from `e88d90de`, and that the frozen profiles and protocol snapshots moved by the rename only. These are structural and diagnostic checks, not adequacy evidence; mutate where a test's discriminating power is in doubt. Write scratch only under `ssds80-phase-d-review-b341109` inside `$TMPDIR`, including any SSDS home you create; write nothing to `~/.ssds`. The stakeholder's admitted shadow ledger is private operator state outside the candidate: judge the evidence record, and reproduce the path on a throwaway home if you need to.

**Scientific checks for this Review.** State your material findings or that you have none; state that you produced, ran or reviewed no realized scientific results (or give a null envelope); state any variants evaluated (count, kind, criterion); report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment; report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the author's (Claude) family, `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-B341109-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-B341109-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Include: a header block (GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, BASELINE, SCOPE including the SD-59 boundary, MANUAL blob, REVIEW METHOD, **REVIEWER** with model family only and how you were engaged); `## SERIOUS CHALLENGE`; `## Verdict` for the Phase D implementation and exit (PASS or NO-PASS; say whether the exit or only the implementation passes), and a line confirming or withdrawing the A7 and A8 verdicts; a disposition of every `d8bdfd3` finding; Phase D blockers with owner text, minimum repair and discriminator; Phase H items; non-blocking findings; the judgments of §3; what you verified and could not; scientific-checks answers; a common-mode note; a statement that nothing beyond shadow is authorized. End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
