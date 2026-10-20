# Independent D4 Review handoff — SSDS 8 Phase D, repaired candidate 517af45, with Manual amendments A7 and A8

This is the complete prompt for one independent Review of three things together: (A) the Phase D implementation and exit as repaired after the `0e49deb` Review, (B) Manual amendment A7 as corrected, and (C) Manual amendment A8. The Review accepts nothing: a Phase D PASS lets Phase E's dependent work start (G2 workplan §5.1 item 5); acceptance is G3; acceptance of A7's and A8's text is the stakeholder's.

**Context.** The previous Review, `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-0E49DEB-DIFFERENT-FAMILY-NO-PASS.md` (handoff `PHASE-D-IMPLEMENTATION-REVIEW-HANDOFF-SSDS-8.0-0E49DEB.md`), returned NO-PASS on the implementation and on A7, with SERIOUS CHALLENGE SC-1, implementation blockers A-B1 to A-B4, A7 blocker B-B1 and non-blocking N1-N3. Since then:

- A-B1 to A-B4 were repaired with tests (`49ef4e3d`);
- N1-N3 were handled (`ae37d129`);
- the stakeholder resolved SC-1 by SD-58 (stakeholder decision record item 54, verbatim there), adopting the author's recommendation: a completeness judgment that bounds a run is checked on the content that run ran on, its other premises in the state of evaluation. The Manual records it as amendment A8; the catalogue, the G2 register's §6.5 row, the code and tests follow (`517af455`);
- B-B1 was corrected in the Manual's §26.4 (`517af455`).

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `517af4551e0b4ea000bd80fe47b1f1f9b4e0e562`. Review exactly this commit.
- **Previous candidate:** `0e49debe63346e72db69ed8e30c14f5bbd58a083`. The repair delta is `git diff 0e49debe 517af455`; the whole Phase D delta is `git diff e88d90de 517af455` (`e88d90de`: G2 authorized, Manual A1-A6 accepted).
- **Manual:** `orchestrator/docs/ssds-8.0-architecture.md`, blob `6226f323365966bbcf653545f3a35b1fd7d6e060`. A7 is `git diff e88d90de 517af455 -- orchestrator/docs/ssds-8.0-architecture.md` minus A8; A8 is the §6.5 sentence marked **[A8, SD-58]**, the §5 monotonicity sentence, and the front-matter and lifecycle lines naming A8.
- **Decisions:** `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` items 52-54 (SD-56, SD-57, SD-58).
- **Plan:** `workplans/active/SSDS-8.0-G2-PHASE-D-PLAN.md`, especially §8 (readings; reading 1 now binding by SD-58) and §9 (the repairs).
- **Step 7 evidence:** `qualification/ssds80/PHASE-D-STEP7-SHADOW-GENESIS-EVIDENCE-SSDS-8.0.md`.
- **Governing owners:** the accepted Manual, the G2 workplan (`workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md`) and its §4.2 register, the catalogue as that register settles it. The Stage S models under `qualification/ssds80/models/` are evidence, not authority; expected values are transcribed, never computed by them.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-implementation/SKILL.md` at the public source for (A) and `source/roles/software-design/SKILL.md` for (B) and (C), and read the owners they route to. Treat the author's account, the plan's readings and this handoff as hypotheses.

## 3. What to judge

**(A) The implementation and the Phase D exit.**

1. **Each previous finding.** For SC-1, A-B1 to A-B4, B-B1 and N1-N3: is it closed at its owner, with its discriminator kept as a test that fails without the repair? Rerun the previous Review's executed probes where you can (a removed witness checkpoint and a high-water mark past the chain through `scripts/shadow_genesis.py derive`; an undeclared responder at `qualify`; a traversing ledger id; a missing-file scope at genesis).
2. **New defects from the repairs.** In particular: the report consumer derives only the qualified prefix through `H*` and labels everything else historical; `qualify` counts only declared witnesses over a validated model; `Home` checks every path before any filesystem effect, symbolic links included; the genesis term-presence check exempts `prefix` terms and accepts an empty file; the fitness rule added for N2 does not refuse legitimate code.
3. **The A8 implementation.** `derivation/assessment.py:bound` and its callers realize the amended rule exactly: standing (acts, unsuperseded, `CLEAR`, held, independent, not vetoed) with no hidden dependence on the state's own target conditions; membership and content entries checked on the content matched; cited records current at `T` in the state of evaluation, with the support graph's matching edge (catalogue §5.6 item 4) so the clamp still sees every cycle; `validity` and `execution` premises failing closed; completeness still read only positively, so `on⁺ ⇒ on⁻` holds. `test_assessment.BoundingCurrency` and `Staleness` carry the discriminators.
4. **Everything the previous Review judged** (its handoff's §3 items 1-11) still holds at the candidate, and the step 7 exit meets plan §3 step 7 and G2 workplan §5.1 items 2 and 5.

**(B) A7 as corrected.** The previous Review's four A7 judgments (fidelity to SD-56 and SD-57; siblings; invariants; disclosed cost), with B-B1's discriminator: reconstructing the assembly from the §26.4 table alone gives the same distribution count, root module and extension relationship as §26.3.

**(C) A8.**

1. **The gap.** The literal rule ("current completeness judgments", evaluated in the state of evaluation) and the accepted case `genuine_fix_is_stale` do conflict; and SD-58 reaches no further than SC-1 needs.
2. **The amendment.** A8 closes the gap. Its split, the run's content for standing, membership and content entries and the state of evaluation for every other premise, is coherent with §6.3 (the recorded execution basis), §6.6 (conditions (1)-(4)), §5.6 (monotonicity, the support graph and the clamp) and §23.6 (loss boundaries: a withheld bounding judgment no longer bounds).
3. **No new permissive route.** A8 makes no failure stale that the Manual's intent keeps counting: a fix that changes the run's membership, a revoked or vetoed bounding judgment, and an unbounded basis all still serve no permissive use.
4. **Siblings and cost.** Every other Manual or catalogue statement about bounding completeness agrees with A8, or name the one that does not; and whether A8 carries a cost that §32.2 should disclose.

Classify findings as blockers (with the owner text, minimum repair and a discriminator) or non-blocking. If accepted authority is itself false or contradictory, raise a SERIOUS CHALLENGE and route it to its owner.

## 4. Method and checks

Reconstruct independently, falsify, and run a bounded Challenge Pass on the repair delta and the siblings of every changed decision. Use a Python 3.11 or newer interpreter. At the candidate run:

```bash
python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt
python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v
python orchestrator/scripts/run_core_tests.py
python orchestrator/scripts/generate_protocol_snapshot.py --check
python -m unittest discover -s tests -v
python3 -I qualification/ssds80/models/run_models.py --seeds
git diff --check e88d90de 517af455
```

and confirm `source/`, `dist/` and `orchestrator/docs/architecture.md` are byte-unchanged from `e88d90de`, and that the frozen profiles and protocol snapshots moved by the rename only. These are structural and diagnostic checks, not adequacy evidence; mutate where a test's discriminating power is in doubt. Write scratch only under `ssds80-phase-d-review-517af45` inside `$TMPDIR`, including any SSDS home you create; write nothing to `~/.ssds`. The stakeholder's admitted shadow ledger is private operator state outside the candidate: judge the evidence record, and reproduce the path on a throwaway home if you need to.

**Scientific checks for this Review.** State your material findings or that you have none; state that you produced, ran or reviewed no realized scientific results (or give a null envelope); state any variants evaluated (count, kind, criterion); report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment; report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the author's (Claude) family, `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-517AF45-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-517AF45-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Include: a header block (GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, BASELINE, SCOPE, MANUAL blob, REVIEW METHOD, **REVIEWER** with model family only and how you were engaged); `## SERIOUS CHALLENGE`; `## Verdict` for (A), (B) and (C) separately (PASS or NO-PASS each; for (A) say whether the Phase D exit or only the implementation passes); a disposition of every previous finding; new blockers with owner text, minimum repair and discriminator; non-blocking findings; the judgments of §3; what you verified and could not; scientific-checks answers; a common-mode note; a statement that nothing beyond shadow is authorized. End with one trailing newline. Return the record path, the three verdicts and a one-paragraph summary of any blockers.
