# Independent D4 Review handoff — SSDS 8 Phase D, repaired candidate d8bdfd3

This is the complete prompt for one independent Review of the Phase D implementation and exit as repaired after the `137b763` Review, with a confirmation that Manual amendments A7 and A8 are unchanged since the `517af45` Review passed them and the `137b763` Review confirmed them. The Review accepts nothing: a Phase D PASS lets Phase E's dependent work start (G2 workplan §5.1 item 5); acceptance is G3; acceptance of A7's and A8's text is the stakeholder's.

**Context.** Three Reviews preceded this one, all different-family and all recorded in `qualification/ssds80/`: `0e49deb` (NO-PASS; SC-1, A-B1 to A-B4, B-B1, N1-N3), `517af45` (Phase D NO-PASS, A7 and A8 PASS; A-B3 retained, A-B5, A-B6, NF1-NF3) and `137b763` (`PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-137B763-DIFFERENT-FAMILY-NO-PASS.md`: Phase D NO-PASS, A7 and A8 PASS confirmed, no SERIOUS CHALLENGE; A-B3 retained at Git's internal paths, A-B7, NF4, NF5). The `137b763` findings are addressed in `d8bdfd3e`, as Phase D plan §9 ("After the 137b763 Review") describes. A-B3 is closed as a family by one rule, at the stakeholder's direction, rather than case by case: the operator tree a ledger uses holds no symbolic link anywhere, and a genesis creates its ledger repository afresh.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `d8bdfd3efa233fec8d7fd8a83803bca1ba77584b`. Review exactly this commit.
- **Previous candidate:** `137b7633945c1a52cc8a590a5fbf07402f57d982`. The repair delta is `git diff 137b7633 d8bdfd3e`; the whole Phase D delta is `git diff e88d90de d8bdfd3e` (`e88d90de`: G2 authorized, Manual A1-A6 accepted).
- **Manual:** `orchestrator/docs/ssds-8.0-architecture.md`, blob `6226f323365966bbcf653545f3a35b1fd7d6e060`, the blob the `517af45` Review passed for A7 and A8 and the `137b763` Review confirmed. The catalogue is unchanged in this delta.
- **Decisions:** `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` items 52-54 (SD-56, SD-57, SD-58).
- **Plan:** `workplans/active/SSDS-8.0-G2-PHASE-D-PLAN.md`, §8 (readings) and §9 (the repairs after each Review).
- **Step 7 evidence:** `qualification/ssds80/PHASE-D-STEP7-SHADOW-GENESIS-EVIDENCE-SSDS-8.0.md`.
- **Governing owners:** the accepted Manual, the G2 workplan (`workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md`) and its §4.2 register, the catalogue as that register settles it. The Stage S models under `qualification/ssds80/models/` are evidence, not authority.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-implementation/SKILL.md` at the public source and read the owners it routes to; for the A7 and A8 confirmation, `source/roles/software-design/SKILL.md`. Treat the author's account, the plan and this handoff as hypotheses.

## 3. What to judge

1. **Each `137b763` finding.** For A-B3, A-B7, NF4 and NF5: is it closed at its owner, with the Review's discriminator kept as a test that fails without the repair? Rerun that Review's executed probes: a pre-existing bare ledger repository at the designated path whose `objects` or `refs` link outside the home, or `refs` into a throwaway product's `.git/refs`, through real prepare, sign, admit and derive (expect refusal before any outside or product write; product refs, objects and status unchanged; a clean control still admits and derives); and the chain at 1, the mark at 1, the witness's checkpoint at 1 removed, through the actual CLI (expect no current assertion, a non-zero exit, the mark unchanged; and current again once the checkpoint is restored).
2. **The family rule itself.** Whether "no symbolic link anywhere in the operator tree a ledger uses, checked before any effect and again before the first Git write, and a fresh ledger repository at genesis" closes every redirection route of this family at the Admission and ledger write boundary (internal Git paths, alternates and repository configuration through the fresh-repository rule; links at any depth of the witness, keys, workspace and state trees and the directories holding them), or name a route it leaves open; and whether it is coherent with the home itself being reached through a link and leaves the positive genesis path intact. Concurrent replacement of paths between the check and the write is outside the static rule; say whether the declared threat model needs more.
3. **New defects from the repairs.** In particular: `qualify`'s retained-mark condition (no current `H*` below an unabandoned mark; a mark past the chain still `ROLLBACK`; a never-qualified successor still provisional; authenticated abandonment still honoured); and the scope-conservative alias map of the Git-reader fitness rule (no new false positive on pure code, every earlier route still detected).
4. **NF5 as a reading.** Plan §9 reads the high-water mark as the last head *qualified* (§23.4), raised when qualification is current even where derivation then withholds the assertion. Is that the Manual's meaning?
5. **Everything previously judged** (the `0e49deb` handoff's §3 items 1-11, and each earlier finding's disposition) still holds at this candidate, the A7 and A8 verdicts stand on the unchanged Manual blob, and the step 7 exit meets plan §3 step 7 and G2 workplan §5.1 items 2 and 5.

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
git diff --check e88d90de d8bdfd3e
```

and confirm `source/`, `dist/` and `orchestrator/docs/architecture.md` are byte-unchanged from `e88d90de`, and that the frozen profiles and protocol snapshots moved by the rename only. These are structural and diagnostic checks, not adequacy evidence; mutate where a test's discriminating power is in doubt. Write scratch only under `ssds80-phase-d-review-d8bdfd3` inside `$TMPDIR`, including any SSDS home you create; write nothing to `~/.ssds`. The stakeholder's admitted shadow ledger is private operator state outside the candidate: judge the evidence record, and reproduce the path on a throwaway home if you need to.

**Scientific checks for this Review.** State your material findings or that you have none; state that you produced, ran or reviewed no realized scientific results (or give a null envelope); state any variants evaluated (count, kind, criterion); report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment; report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the author's (Claude) family, `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-D8BDFD3-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-D8BDFD3-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Include: a header block (GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, BASELINE, SCOPE, MANUAL blob, REVIEW METHOD, **REVIEWER** with model family only and how you were engaged); `## SERIOUS CHALLENGE`; `## Verdict` for the Phase D implementation and exit (PASS or NO-PASS; say whether the exit or only the implementation passes), and a line confirming or withdrawing the A7 and A8 verdicts; a disposition of every `137b763` finding; new blockers with owner text, minimum repair and discriminator; non-blocking findings; the judgments of §3; what you verified and could not; scientific-checks answers; a common-mode note; a statement that nothing beyond shadow is authorized. End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
