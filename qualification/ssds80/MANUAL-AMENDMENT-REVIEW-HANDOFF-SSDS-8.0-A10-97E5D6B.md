# Independent D3 re-Review handoff — SSDS 8 Architecture Manual amendment A10 (project memory), revision 1, candidate 97e5d6b

This is the complete prompt for one independent, different-family D3 re-Review of **proposed** amendment A10, revision 1, to the accepted SSDS 8 Architecture Manual. The re-Review accepts nothing: acceptance of A10 is the stakeholder's (as A9 was, SD-61 and SD-62). The run needs the stakeholder's approval.

**Context.** A10 re-derives items A, B, D and E of the SSDP 8.0 Amendment 1 handoff against the accepted Manual under SSDP 7.2.1 (SD-63, decision record item 59). The stakeholder adopted the author's recommendations on its open decisions and approved a Review (SD-64, item 60). The different-family Review of revision 0 at `0368198` (`qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-0368198-A10-DIFFERENT-FAMILY-NO-PASS.md`, committed at `73df3e0a`) returned NO-PASS with five G1 blockers:

- B1, acceptance provenance;
- B2, incomplete freshness dependencies;
- B3, memory-unavailable uncertainty closing without independent judgment;
- B4, non-monotone candidate selection classified as control tightening;
- B5, an owner change lost while memory is unreadable.

It also opened four register entries (A10-R1 to A10-R4). Revision 1 repairs each at its owner and records the repairs in the proposal's §10. A10 remains a standalone proposal file: the Manual is unchanged at the candidate.

## 1. What you are reviewing

- **Repository:** GitHub `hjin98/scientific-software-development-system`, full clone; branch `ssds-8.0-graph-native-architecture`, or the candidate commit itself if it has not yet been carried there (it is authored on a side branch and is carried by cherry-pick, which changes the commit identity but not the blobs below).
- **Candidate commit:** `97e5d6bca20e722c95461ae6f6c889631f738f8e`. Review exactly this commit (`git show 97e5d6bc:<path>` or a `git archive` snapshot). If you receive a cherry-picked commit instead, check that the proposal blob below is identical and review that.
- **Previous candidate:** `0368198210706151c69a4119f6288ce8baa8d884`, proposal blob `871ecb574b7d15e6e860ff171bfb70d75d1394e7`. The A10 delta is `git diff 0368198 97e5d6bc -- qualification/ssds80/MANUAL-AMENDMENT-A10-PROPOSAL-SSDS-8.0-PROJECT-ENGINEERING-MEMORY.md`. Every other difference between the two commits is unrelated Stage D Phase F work, the revision 0 Review handoff and record, and the stakeholder decision record (SD-64): not under review here.
- **Subject:** `qualification/ssds80/MANUAL-AMENDMENT-A10-PROPOSAL-SSDS-8.0-PROJECT-ENGINEERING-MEMORY.md` (blob `e59873254b2fe1b6376446eec3fe380a18ba89e3`): the proposed §16.11 (its §4.1) and the pointer and consequence edits (its §4.2, now including edits 3a-3c to §10.2-§10.4 and 6a to §14.1), judged as if applied to the accepted Manual `orchestrator/docs/ssds-8.0-architecture.md` (blob `fe43f04f5a698688727f7473a7c2e4d5345ae911`, unchanged at the candidate). Its §10 is the author's account of the repairs: a hypothesis to test, not authority.
- **Unchanged and only for consistency:** the item-C proposal `qualification/ssds80/PEM-SCHEMA-PROPOSAL-TYPED-APPLICABILITY-BINDINGS.md` (blob `34594fefd81337ead9473683d40755a60e108696`).
- **Relevant context:** the previous Review record above; the stakeholder decision record `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` (items 57-60; SD-61 to SD-64); the mechanism catalogue (non-authoritative); `orchestrator/src/ssds/interface/render.py` (the realized §16.3 injection events); `PROJECT-ENGINEERING-MEMORY.md` and `source/project_engineering_memory.py`.

## 2. Governing authority

SSDP 7.2.1, identities from `PROTOCOL-RELEASE-STATE.yaml` (public source `aaeaf8b6b2121b9fb8aba31917c8265649c43954`, recovery `efdd1b59a7592b1cecef0a0013c35b54a7a6315d`). Enter `source/roles/software-design/SKILL.md` at the public source and read the owners it routes to; `workflow-and-workplans.md` ("Authority lifecycle, mutation, and impact closure") governs amending accepted authority. PEM meaning is owned by `source/shared/references/project-engineering-memory.md` and `project-engineering-memory-schema.md` at the public source; A10 must not change, narrow or widen it. The accepted Manual (A1-A9) is the baseline.

## 3. What to judge (workplan §25 criterion 11, for the changed decisions)

1. **Closure of each blocker.** For B1-B5, say whether revision 1 closes it at its owner, applying the previous Review's own discriminators (kept as the proposal's §7 cases 15-19). In particular:
   - **B1:** does naming the accepted publication by the PEM subject's latest standing `ACCEPTANCE` or `LEGACY_ACCEPTANCE` (§19.2) keep observation and acceptance apart under §8.6, §19.2, §19.9 and §20.2? Does requiring owner validity (§5.5) for a current binding exclude candidate-only authority?
   - **B2:** is the per-entry dependency identity sufficient for "materially advances", and still selective? Is the §14.1 edit a sound statement of the conformance owner's new input?
   - **B3:** does every result that can carry `PEM_UNAVAILABLE` now have a holder (the work's independent review or a human) before it answers or discharges anything? Is withholding at S3 (§10.3, §10.4, §15.5) enough, or does some permissive effect escape at S2? Is the regress bounded?
   - **B4:** is the R2 classification of `memory.terms`, with bound and owner-bound candidates outside the cap, monotone?
   - **B5:** is staleness over admitted history from the reference position sound? Is the reference position well defined, including for a publication accepted after genesis whose route predates it? Is the pre-genesis residual correctly left to E3?
2. **The register entries.** Whether §10's dispositions of A10-R1 to A10-R4 are adequate, or which must stay register entries for G2.
3. **New defects introduced by the repairs.** The repairs add a history-reading predicate (e), an acceptance-named publication (a), a `HUMAN_ATTENTION` trigger and S3 answer and discharge conditions (g; edits 3a-3c, 8), and a new conformance input (edit 6a). Check them against their siblings: §4.1-§4.3, §5.2's acting rule, §5.5-§5.8 (stratification: (e) reads S2 validity at historical positions; (g) withholds at S3), §7 frames, §10.2-§10.4 (including SD-36's discharge that is not latched), §11.5, §12.5, §13.4, §14.1-§14.4, §15.2-§15.5, §16.5, §19.2, §19.9 and §23.6 (does a loss boundary interact with the history predicate or the acceptance-named publication?).
4. **Fidelity, unchanged parts.** Whether anything the previous Review judged sound has been weakened (the activation qualifiers, the HAS shape, the closeout classes and the migration exclusion, "missing memory is not absence", the item-C independence).
5. **Cost and disclosure.** Whether the new waiting (human attention for unaccepted uncertainty on unreviewed results; review-required bindings to `LEGACY(p)` owners without imported acceptance; no accepted publication until a PEM acceptance is imported, which §8 now states for this repository) is disclosed where the Manual discloses costs.

Classify findings as a G1 blocker (criterion 11: a contradiction, an omitted or unrealizable invariant, or a decision a conforming realization can satisfy while violating upstream meaning), a G2 register entry, or non-blocking. If accepted authority itself (the Manual or the PEM owners) appears false, contradictory or inadequate, raise a SERIOUS CHALLENGE routed to its owner instead of reviewing around it. You need not re-review parts of the Manual or the proposal that revision 1 leaves unchanged, except as item 4 asks.

## 4. Method and checks

Reconstruct independently, falsify, and run a bounded Challenge Pass on the repaired text and its siblings. Re-run the previous Review's counterexample trajectories (its C04-C06 and C09-C13) against revision 1, and write new ones for item 3. At the candidate run:

```bash
python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v
git diff --check 0368198210706151c69a4119f6288ce8baa8d884 97e5d6bca20e722c95461ae6f6c889631f738f8e
git diff --stat 0368198210706151c69a4119f6288ce8baa8d884 97e5d6bca20e722c95461ae6f6c889631f738f8e -- qualification/ssds80/
python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md
```

Confirm that `orchestrator/docs/ssds-8.0-architecture.md`, `orchestrator/docs/architecture.md`, `PROJECT-ENGINEERING-MEMORY.md`, `source/` and `dist/` are byte-unchanged from `0368198`. Report `orchestrator/src/` changes as Phase F work outside this review. These are structural checks, not adequacy evidence. The PEM validator needs a Git repository for route realization; run it in the clone. No executable model exists for A10, so do not treat the proposal's §7 cases as run. Write scratch only under `ssds80-manual-review-a10-97e5d6b` inside `$TMPDIR`.

**Scientific checks for this Review.** State your material findings or that you have none; state that you produced, ran or reviewed no realized scientific results (or give a null envelope); state any variants evaluated (count, kind, criterion); report a tension search only if you relied on accepted D1/D2 authority for a consequential judgment; report unanswered parts as gaps.

## 5. Output

Write exactly one Markdown file: if you are of the amendment author's model family, `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-97E5D6B-A10-PASS.md` or `-NO-PASS.md`; otherwise `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-97E5D6B-A10-DIFFERENT-FAMILY-PASS.md` or `-DIFFERENT-FAMILY-NO-PASS.md`. Include:

- a header block: GOVERNING SSDP, REPOSITORY, BRANCH, CANDIDATE, PREVIOUS CANDIDATE, SCOPE, MANUAL blob, PROPOSAL blob, REVIEW METHOD, and **REVIEWER** with the model family only and how you were engaged;
- `## SERIOUS CHALLENGE`;
- `## Verdict`: PASS or NO-PASS for A10 revision 1 as a D3 change;
- per blocker B1-B5: closed or open, with the trajectory that shows it;
- new G1 blockers, each with its trajectory, the owner text, the minimum repair and a discriminator;
- register entries and non-blocking findings;
- the five judgments of §3;
- what you verified and what you could not;
- the scientific-checks answers;
- a common-mode note;
- a D4 statement: D4 stays not authorized.

End with one trailing newline. Return the record path, the verdict and a one-paragraph summary of any blockers.
