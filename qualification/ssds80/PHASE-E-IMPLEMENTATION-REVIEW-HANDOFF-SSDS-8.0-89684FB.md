# Independent re-Review handoff — SSDS 8 Phase E, repaired candidate 89684fb

This is the complete prompt for one independent re-Review of SSDS 8 Stage D Phase E after the repairs of the re-Review of `b791215`. It is deliberately narrow: judge whether that re-Review's four blockers are closed at their owners without new defects, and whether anything it found closed has regressed. The re-Review accepts nothing: a Phase E PASS lets Phase F's dependent work start (G2 workplan §5.1 item 5); acceptance of the implementation is G3.

**Context.** Two different-family Reviews preceded this one. The Review of `09f3505` passed Manual amendment A9 (accepted since, SD-62) and found six Phase E blockers (B1-B6). The re-Review of `b791215` (`qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-B791215-DIFFERENT-FAMILY-NO-PASS.md`) judged B2 and B5 closed and B1, B3, B4 and B6 partly closed, with four remaining blockers: E-B1, a partitioned item discharged provisionally around an open required part (its own subject set empty); E-B2, earlier item-level review findings missing from an item-level re-review; E-B3, a diff that lost added entries' types and modes and final-newline edits; E-B4, an eligible but non-current qualified gate dropped from the inspector. It also noted the G2 workplan's stale group 5 count and the Phase E plan's front matter. The Phase E plan records each repair (§5, "The re-Review of b791215").

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`.
- **Candidate commit:** `89684fb93152f87355a84bde1928b8d69218b8b6`. Review exactly this commit.
- **Previous candidate:** `b7912159c0db8abeb3323d6a4b44532f18984094`. The repair delta is `git diff b7912159 89684fb9` (the re-Review record, the repairs at `c91b1bb2`, the lifecycle result at `89684fb9`; the handoff of `b791215` at `937c5bf4` is not part of the candidate's behaviour). Phase E as a whole is `git diff 55c01a83 89684fb9`.
- **Manual:** blob `fe43f04f5a698688727f7473a7c2e4d5345ae911`, unchanged since `b791215` (accepted A1-A9).
- **Plan:** `workplans/active/SSDS-8.0-G2-PHASE-E-PLAN.md`, blob `59d9c9775e6e1c8da18cc77ca6b7cf58e89795a6`: readings E15, E30 and E38, §5's records of both earlier Reviews.
- **Repair owners:** `orchestrator/src/ssds/derivation/items.py` (`ItemObligation.subjects`, `ItemObligation.discharge`), `briefing.py` (`_unresolved_reviews`, `_of_plan`, `qualified_gates`), `orchestrator/src/ssds/interface/render.py` (`_candidate_diff`, `_entry`). Tests: `orchestrator/tests/ssds/test_phase_e_review.py`, class `ReReview` (the earlier re-Review's own probe constructions, ported).

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-implementation/SKILL.md` at the public source and read the owners it routes to. The accepted Manual (A1-A9) and the G2 workplan's register govern; the earlier Reviews' findings and the author's repair account are hypotheses to test.

## 3. What to judge

1. **E-B1 to E-B4 closed at their owners.** Rerun the earlier re-Review's trajectories and the discriminators it named: for E-B1, the incomplete override leaving the whole `OPEN` with its route and consumers agreeing, complete permission giving only provisional discharge, and the same after retained work and a re-partition; for E-B2, a re-integration, a changed target, a prose amendment and a replacement partition each leaving the finding carried, a later qualifying `RESOLVED` removing it, an author's claim or a non-independent review not; for E-B3, the regular, executable and link additions, the newline pair, and the deletion, mode, type and binary controls; for E-B4, the challenged decision retained with its currency shown and the gate term `F`, with the extra-decision, supersession and tenure-restart controls. Say for each whether it is closed, partly closed or open.
2. **Siblings and new defects.** The repairs touch shared owners: an item's subject set now includes its parts' (read by its predicate, provisional scope, briefs and reports); a partitioned item's discharge now reads its parts' discharge (read by its route, the readiness of dependent items, the inspector and the lifecycle routes; the full enumeration was rerun, E15); the carry now reads results bound by work key; the diff headings changed. Look for a regression, a recursion, a new way to lose a finding or strand an obligation, or a claim of holding or discharge that is false.
3. **No regression of what passed.** B2 and B5 as closed by the earlier re-Review, the suites, A9's realization, and the shadow and frozen-Core boundaries. Reuse earlier evidence only where the delta cannot affect it, and say where you did.
4. **Accounting.** Whether E30 and E38 now state what is realized, and whether the count and front-matter corrections are right.

Classify findings as Phase E blockers (with the owner text, minimum repair and a discriminator), findings for a later phase, or non-blocking. If accepted authority itself appears false, contradictory or inadequate, raise a SERIOUS CHALLENGE routed to its owner.

## 4. Method and checks

Reconstruct independently, falsify with counterexamples against the real `ssds` package, and mutate where a test's discriminating power is in doubt. Use Python 3.11 or newer. At the candidate run:

```bash
python -m pip install ./orchestrator -r orchestrator/requirements-dev.txt
python -m unittest discover -s orchestrator/tests/ssds -t orchestrator -v
python orchestrator/scripts/run_core_tests.py
python orchestrator/scripts/generate_protocol_snapshot.py --check
python -m unittest discover -s tests -v
git diff --check b7912159 89684fb9
```

Run the SSDS suite as a non-root user. The full lifecycle enumeration (`SSDS_SLOW=1`) is optional; the plan records its rerun at `c91b1bb2`. Write scratch only under `ssds80-phase-e-rereview-89684fb` inside `$TMPDIR`, including any SSDS home; write nothing to `~/.ssds`.

**Scientific checks for this Review.** State your material findings or that you have none; state that you produced, ran or reviewed no realized scientific results (or give a null envelope); state any variants evaluated (count, kind, criterion); report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment; report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the author's (Claude) family, `qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-89684FB-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-89684FB-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Include: a header block (GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, BASELINE, SCOPE, MANUAL blob, REVIEW METHOD, **REVIEWER** with model family only and how you were engaged); `## SERIOUS CHALLENGE`; `## Verdict` for the Phase E implementation and exit (PASS or NO-PASS; say whether the exit or only the implementation passes); the disposition of E-B1 to E-B4 and of the accounting points; Phase E blockers with owner text, minimum repair and discriminator; findings for later phases; non-blocking findings; what you verified, what you reused and what you could not verify; scientific-checks answers; a common-mode note; a statement that nothing beyond shadow is authorized. End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
