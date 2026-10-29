# Phase F continuation — scheduled 2026-10-29 work

Governing SSDP: 7.2.1. Authority: Phase F revision 58, SD-55 shadow scope, SD-69, stakeholder item 72,
and the user's instruction to resume at 5:30 am America/Chicago after the usage refresh. Asserter: AI
implementing agent, Codex family. This checkpoint is decision support, not operational acceptance.

**10d remains incomplete.** The original signed repair was accepted, but its actual-append boundary comparison
remains FAILED/contaminated. No SSDS-caused writer was established. Later isolated checks do not qualify that
original append. Frozen-candidate 11b, complete classification, other-family review, step 12 and acceptance
remain open. No native authority, cutover, live model campaign, PR, merge or push occurred.

## Current product and evidence

- Branch: `ssds-8.0-graph-native-architecture`; starting HEAD `6d43121b440743a3b6e9f78b7600a40e4fc5ba7a`,
  three local unpushed commits ahead of tracking. Production source at `11ec88e4` had passed 1,879 tests,
  10 skipped. The new source repairs below passed their own complete suite: 1,886 tests, 10 skipped.
- Real shadow ledger: `ssdp-shadow-2`, four entries through position 3 after absorbing `6d43121b`.
  The program verified three effective reserved leaves, empty quarantine and the retained policy object's
  exact bytes/digest. The source-compatibility probe found eight INTAKE_DISPOSITION records and no historical
  report record affected by the new report guard. Other deployments may hold nonconforming historical records.
- Two reviewed unsigned requests are prepared. Their complete meaning, immutable identities, actual signing
  links and human duties are in `PHASE-F-10D-PENDING-HUMAN-REQUESTS-SSDS-8.0.md`. No unsigned request was
  submitted. Exact commands/outputs/comparisons are retained in the canonical 10d evidence's continuation.
- Preliminary historical study at `6d43121b` timed out after one hour, exit 124, with no report. Its scratch
  ledger reached the real baseline at position 66; that does not establish completed projections or classification.
  `PHASE-F-DIFFERENCE-STUDY-EVIDENCE-SSDS-8.0.md` owns the attempt and its limits.

## D4 defects and repairs

**R-REPORT-15.1: accepted report vocabulary was not enforced.** The accepted Manual and catalogue §15.1
say FINDING cannot block and prescribe reasons for five kinds. A fresh reviewer reproduced real Admission
ACCEPT/retention for a blocking FINDING, an unknown reason and a BLOCKER-only reason on FINDING. This is a
D4 schema defect, not a Serious Challenge; actual unintended task suspension was not demonstrated.

`ledger/schema.py`, the existing owner used by Admission and verified reading, now constrains supplied reasons
for CHALLENGE, FINDING, AMENDMENT_REQUEST, BLOCKER and HUMAN_QUESTION, and refuses `FINDING blocking:true`.
Empty reasons and optional flags remain representable; the bounded repair infers no cardinality rule. Reader
fail-closed behavior is unchanged: an authenticated violating historical record halts at its position. No history
is rewritten or silently grandfathered. The pre-rollout real-chain compatibility check passed in isolation.

**R-EMPTY-REVISION: empty judgment queries serialized large irrelevant revisions.** Timed-out preliminary work
and focused traceback samples locate the cause in Support's empty queries. Existing acceptance, required-judgment
and gate-decision methods now return empty lists before revision calculation when they have no candidate records;
validity returns F before its other conjuncts when no acceptance can contribute (§5.5 empty disjunction). Nonempty
filtering, static support edges, independently derived S3 findings and identity encodings remain at their owners.
No new cache, proxy deriver or state machinery was added. Four implementation variants and their limits are retained
in the study evidence; no controlled speedup ratio or scientific improvement is claimed.

Fresh Codex code Review: **PASS**, no blockers or Serious Challenge. Reviewed production SHA-256:
schema `07caebdb081a010dd897264805f0b739f7e5cce8cba587aaedcab713c84cabac`;
support `7fddf8b38429e3ea6744da3dad8ed767baf6f57dc03df77e52ab82191fb862ef`.
The independent reviewer ran 112 affected tests plus 68 further executions over assessments and steps 4d–4e,
all passing. Parent focused regression: 65 tests pass, including actual Admission refusal and authenticated
historical halt. An initial wrong targeted test-class selector ran no test; the corrected targeted reader test
passed and the complete test remains in discovery. No failed selector is acceptance evidence.

The complete suite passed over fixed production source: **1,886 tests in 605.604 seconds, OK (10 skipped), exit 0**;
no FAIL/ERROR cases. Command, with cwd `orchestrator`:

```bash
PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 timeout 3000 \
  /tmp/ssds-phase-f-20261029/bin/python -m unittest discover -s tests -t . \
  > /tmp/ssds-10d-20261029/full-suite-resume-repairs.log 2>&1
```

The negative CLI test prints an expected argparse error; it is not a unittest ERROR. Core and installed-product
checks are included. Skips remain skips. Fresh Codex plan/evidence check also passed. Post-update real SSDS
reads then confirmed exact request/message identities, both signatures absent, effective reserved leaves and
empty quarantine; status is QUALIFIED at position 3, four entries, no critical/provisional/obligation. Both
endpoint comparisons passed. No required unexecuted duty is converted to a pass.

## Historical applicability and preserved surfaces

PEM activated by the governing workplan and the measured scaling issue. Independently verified integrated base:
`main` `af0455753e20ee54a969c844872e29e270007211`, PEM blob
`1561797125622f355f84eb27319f87e8fa4227d9`; working bytes match, no overlay. Schema validation passed:
five families, zero notices. Canonical metadata search across all five families found no additional performance
lesson. HAS: DS-001 applicable to real-owner/claim-bounded qualification; PC-001 relevant preservation evidence,
with force supplied by the actual current frozen-surface instructions; FF-001/SP-002 public bootstrap publication
and SP-001 router regeneration inapplicable to these changes. Coverage remains partial, not proof of absence.

Protocol source, generated distributions/profiles/snapshots, accepted Manual/catalogue, frozen Core architecture
and project PEM remain untouched. No human key or `~/.ssh` access; real `~/.ssds` use was exclusively through SSDS
within the authorized shadow operation. Only named task files may be staged. Commit trailer remains the user's
standing `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` convention; artifacts identify family only.

## Human duties and next resumable actions

1. Review/sign the two exact prepared requests, using the links in the pending-requests record. The agent then
   verifies signatures and actual report/submit effects in isolated before/command/after host windows.
2. Disposition the original append qualification gap. Preserve its failure; any revised closure requirement needs
   explicit governing approval. Later clean windows support their own claims only.
3. After FINDING admission yields a real obligation identity, endorse a truthful direction for the signed decide
   refusal. Proposed intent: keep the gap open, defer resolution, continue independent shadow qualification.
   No decision is fabricated. Its expected refusal would admit no resolution; retain human direction separately.
4. Use the qualified repair commit for preliminary diagnostics if meaningful, then bind the eventual
   frozen candidate for the prescribed full 11b/classification and independent other-family review. Step 12 and
   stakeholder acceptance follow their actual prerequisites; do not self-close or archive the active plan.
5. Push through the prescribed user-terminal route. It is unavailable here; no substitute credential route is used.

Usage was checked at wakeup and major checkpoints. Preserve enough allowance for this checkpoint and final
responsibility report; do not spend on filler or wait for another usage window. The one-time resume automation
must be removed when this scheduled run concludes.

Scientific scope: governance/qualification infrastructure only, no realized scientific results, scientific gate
evidence, scientific pipeline/model selection or accepted D1/D2 judgment. Infrastructure proposal/code variants
and failed/unexecuted checks are disclosed above and in the canonical study/10d records. No new product
inspectability surface or retention contract is asserted.
