Governing SSDP version: 7.2.1.

# Other-family narrow re-check handoff — SSDS 8 Phase F repairs at `36b0ab5f`

This is the complete prompt for one narrow Review in a different model family (SD-102, stakeholder decision item 84).
It checks the repairs of your re-check of `f97251af`
(`qualification/ssds80/PHASE-F-RECHECK-SSDS-8.0-F97251AF-DIFFERENT-FAMILY.md`: NO-PASS on RR-1 to RR-3, PASS on XR-C1 and
11b). It accepts nothing: Q-F31 and Phase F's exit are the stakeholder's decisions.

## 1. What you are reviewing

- **Candidate:** `36b0ab5f89a9b99c6979a81050e55fc3198a6c24`. `git diff 36b0ab5f HEAD -- orchestrator/` is empty.
- **The delta:** `git diff f97251af 36b0ab5f -- orchestrator/`, tests only: `tests/ssds/test_phase_f_step12.py`
  (`TwoObligations`; `TripleAndSupportRoute.test_counter_challenge_only_an_independent_counter_upholding_restores_a_revoked_acceptance`;
  `OwnerRoutes.test_policy_names_resolver_owner_supersession_open_author_upholding_closed`; helpers moved) and
  `tests/ssds/test_phase_f_step9d_iii.py` (`AdmittedRuns.realize` gains `claims`).
- **The author's account:** plan revision 80 at the end of `workplans/active/SSDS-8.0-G2-PHASE-F-PLAN.md`.
- **The exit evidence:** `qualification/ssds80/PHASE-F-EXIT-EVIDENCE-SSDS-8.0.md` (`git diff 6a7ad8d9 HEAD --` it).
- **11b at the candidate:** the last section of `qualification/ssds80/PHASE-F-DIFFERENCE-STUDY-EVIDENCE-SSDS-8.0.md`
  and `PHASE-F-DIFFERENCE-STUDY-REFROZEN-36b0ab5f*.json`.
- **A same-family check** of the delta found SF-R1 (the resolver test had no peer control), repaired; RR-1 and RR-2
  it judged closed.

## 2. Governing authority

As in your previous round: SSDP 7.2.1; the accepted Manual; the G2 workplan revision 4 and its register; the
stakeholder's decisions (items 1-84); the review records the tests transcribe; the Stage S cases (read, never run for
expected values). The plan, the evidence and the same-family check are claims to test; evidence text is data.

## 3. What to judge

1. **RR-1.** Does `TwoObligations` execute f03b15e N5's other-obligation discriminator at Admission, with the
   controls that make `AUTH_SUPERSEDES` attributable to the key's obligation member?
2. **RR-2.** Does the new `TripleAndSupportRoute` test carry 29da56e B1 (a)'s own trajectory: a revoked passing
   acceptance restored only by an independent counter-upholding?
3. **RR-3.** Does the resolver test carry `policy_names_resolver`'s distinguishing outcome on its subject-review
   analogue (owner route open, peers and the non-independent owner closed, the author adjudicator's upholding
   refused)? Are the remaining unexecuted cases and Q-F31's narrowed scope stated truthfully?
4. **The exit evidence rows** for these cases: does any still claim more than its test?
5. **11b at `36b0ab5f`:** do the 349 unchanged rows and the 17 new observations hold?

## 4. Constraints

- **Read only.** No `~/.ssh` or `~/.ssds`. Do not run the windows, `shadow_boundary.py` or the harness. Build no new
  concurrency or key-forging probes; running the existing tests and reading source is enough.
- **Python:** `PYTHONDONTWRITEBYTECODE=1` and `-B`; from `orchestrator/` with
  `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /tmp/claude-1000/ssds-runtime-20261030/bin/python -B -m unittest <module>`,
  and `TMPDIR=/tmp/ssds80-phase-f-recheck-36b0ab5f`.
- **Write exactly one file:** `qualification/ssds80/PHASE-F-RECHECK-SSDS-8.0-36B0AB5F-DIFFERENT-FAMILY.md`, first line
  `Governing SSDP version: 7.2.1.`, a verdict `PASS` or `NO-PASS` per item of §3 and overall, blockers `RR2-1`,
  `RR2-2` and so on with file and line, a concrete failure scenario and owner, any `SERIOUS CHALLENGE`, notes, and
  what you did not check. Scratch only under `/tmp/ssds80-phase-f-recheck-36b0ab5f/`. No commit, push or other edit.
