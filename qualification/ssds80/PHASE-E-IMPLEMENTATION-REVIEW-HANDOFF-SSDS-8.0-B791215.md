# Independent re-Review handoff — SSDS 8 Phase E, repaired candidate b791215

This is the complete prompt for one independent re-Review of SSDS 8 Stage D Phase E after the repairs of the different-family Review of `09f3505`. It is deliberately narrower than that Review: judge whether its six blockers are closed at their owners without new defects, and whether anything that passed there has regressed. The re-Review accepts nothing: a Phase E PASS lets Phase F's dependent work start (G2 workplan §5.1 item 5); acceptance of the implementation is G3.

**Context.** The Review of `09f3505` (`qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-09F3505-DIFFERENT-FAMILY-NO-PASS.md`) found no SERIOUS CHALLENGE, passed Manual amendment A9 (since accepted by the stakeholder, SD-62), and returned Phase E NO-PASS with six blockers: B1, an integrated item kept fully discharged after its subject's evidence became disputed; B2, a non-current assessment presented as a holding gate premise; B3, unresolved review findings lost from a re-review brief after a prose amendment; B4, a path summary in place of the candidate diff; B5, current text substituted for the governing revision named; B6, a qualified gate `ACCEPT` missing from the inspector without supersession. It also noted N1 (step 5's blocker count), the S3 case count, and N2 (group 6's generic property does not itself detect lost revalidation routes). The Phase E plan's Review record (§5, "The Phase E Review of 09f3505") states each repair.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `b7912159c0db8abeb3323d6a4b44532f18984094`. Review exactly this commit.
- **Previous candidate:** `09f35057aec00467372aa8fbbda37f540a9bbc1f`. The repair delta is `git diff 09f35057 b7912159` (the Review record, the repairs at `51d35771`, A9's acceptance at `b7912159`). Phase E as a whole is `git diff 55c01a83 b7912159`.
- **Manual:** blob `fe43f04f5a698688727f7473a7c2e4d5345ae911`; since `09f3505` only its lifecycle header and status lines changed, to record A9's acceptance (SD-62). Confirm that.
- **Plan:** `workplans/active/SSDS-8.0-G2-PHASE-E-PLAN.md`, blob `5ad72f49cf2c9c90cde0a93859f5f8681e2234ba`: readings E30, E36, E38 (revised), §6 (now the whole list of what is not realized), §5's record of the `09f3505` Review and its repairs.
- **Repair owners:** `orchestrator/src/ssds/derivation/items.py` (`ItemObligation.predicate`), `queries.py` (`evidence`, `content_at`), `briefing.py` (`required_evidence`, `_unresolved_reviews`, `qualified_gates`), `support.py` (`eligible_gate_decisions`, which `gterm` now uses), `orchestrator/src/ssds/interface/render.py` (`_candidate_diff`, `_governing_inline`, `inspector`). Tests: `orchestrator/tests/ssds/test_phase_e_review.py`.
- **Decisions:** `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md`, items 57-58 (SD-61, SD-62).

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-implementation/SKILL.md` at the public source and read the owners it routes to. The accepted Manual (A1-A9) and the G2 workplan's register govern; the earlier Review's findings and the author's repair account are hypotheses to test, not authority.

## 3. What to judge

1. **Each of B1-B6 closed at its owner.** Rerun the earlier Review's executed trajectories and discriminators against the candidate, including those it named beyond the recorded tests: for B1, a failure on a subject changed by an earlier retained enactment and a partitioned item, and `DISCHARGED_PROVISIONAL` only with applicable provisional permission; for B2, provisional and superseded-assessment controls and the query and gate projections agreeing; for B3, a replacement partition and a later qualifying `RESOLVED` record, with an author's claim alone never resolving; for B4, deletion and mode or type changes and binary content; for B5, historical-item review briefs and a missing revision; for B6, an unqualified decision that does not supersede, an authorized supersession, and the tenure-restart case. Say for each whether it is closed, partly closed or open.
2. **Siblings and new defects.** The repairs touch shared owners: `gterm` now goes through `eligible_gate_decisions`; item discharge now reads `ev` and `qual`, which can change routes, partition composites, the item-level review and every consumer of discharge (readiness of dependent items, reports, briefs, the inspector); `evidence` statuses changed for every caller; the diff renderer reads candidate and base trees. Look for a regression or a new way to lose a finding, strand an obligation, or present something as holding or current that is not.
3. **No regression of what passed.** The suites, A9's realization, the shadow and frozen-Core boundaries, and the step reviews' closures the earlier Review confirmed. Reuse its evidence only where the delta cannot affect it, and say where you did.
4. **The plan's accounting.** Whether E30, E36, E38 and §6 now state honestly what is realized and what is not, and whether the N1 and S3 count corrections are right.

Classify findings as Phase E blockers (with the owner text, minimum repair and a discriminator), findings for a later phase, or non-blocking. If accepted authority itself appears false, contradictory or inadequate, raise a SERIOUS CHALLENGE routed to its owner.

## 4. Method and checks

Reconstruct independently, falsify with counterexamples against the real `ssds` package, and mutate where a test's discriminating power is in doubt. Use Python 3.11 or newer. At the candidate run:

```bash
python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt
python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v
python orchestrator/scripts/run_core_tests.py
python orchestrator/scripts/generate_protocol_snapshot.py --check
python -m unittest discover -s tests -v
git diff --check 09f35057 b7912159
```

Run the SSDS suite as a non-root user. The full lifecycle enumeration (`SSDS_SLOW=1`) is optional here; if you do not run it, judge whether the B1 change to discharge can affect the replayed routes. Write scratch only under `ssds80-phase-e-rereview-b791215` inside `$TMPDIR`, including any SSDS home; write nothing to `~/.ssds`.

**Scientific checks for this Review.** State your material findings or that you have none; state that you produced, ran or reviewed no realized scientific results (or give a null envelope); state any variants evaluated (count, kind, criterion); report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment; report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the author's (Claude) family, `qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-B791215-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-B791215-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Include: a header block (GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, BASELINE, SCOPE, MANUAL blob, REVIEW METHOD, **REVIEWER** with model family only and how you were engaged); `## SERIOUS CHALLENGE`; `## Verdict` for the Phase E implementation and exit (PASS or NO-PASS; say whether the exit or only the implementation passes); the disposition of B1-B6, N1, N2 and the S3 count; Phase E blockers with owner text, minimum repair and discriminator; findings for later phases; non-blocking findings; what you verified, what you reused and what you could not verify; scientific-checks answers; a common-mode note; a statement that nothing beyond shadow is authorized. End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
