# Phase F difference study — preliminary attempt; frozen 11b unexecuted

Governing SSDP: 7.2.1; Phase F revision 57, F123–F124; SD-55, SD-64.
Asserter: AI implementing agent, Codex family, 2026-10-29. Infrastructure evidence only.

**Final frozen-candidate study, complete classification and independent other-family review remain unexecuted.**
This record retains preliminary diagnostics and cannot support step-11b or exit acceptance. The real-ledger
original append qualification gap remains in `PHASE-F-10D-SHADOW-LEDGER-EVIDENCE-SSDS-8.0.md`.

## Attempt A: original production source; timed out

Candidate: `6d43121b440743a3b6e9f78b7600a40e4fc5ba7a` (production source unchanged from `11ec88e4`).
Real baseline: `53d5a22c04f8c8035dfccd4577a3cdd9ece06a2b`. This was a preliminary immutable HEAD, not the final
frozen semantic candidate. The requested population has 290 first-parent deltas after candidate initialization
`09f35057aec00467372aa8fbbda37f540a9bbc1f`; initialization and exact exclusions still require a completed report.

```bash
PATH=/home/samjin/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/fallback:$PATH \
PYTHONDONTWRITEBYTECODE=1 SSDS_HOME=/tmp/ssds-phase-f-preliminary-6d43121b-20261029 \
timeout 3600 /tmp/ssds-phase-f-20261029/bin/python orchestrator/scripts/difference_study.py \
  --repository /home/samjin/agent-skills/scientific-software-development-system \
  --candidate 6d43121b440743a3b6e9f78b7600a40e4fc5ba7a
```

Exit **124**, no stdout/stderr and no `difference-study.json`. The process was allowed its one-hour bound, with
no concurrent restricted filesystem or agent probes during its boundary window. Because timeout prevented its
final comparison/report, no study boundary PASS is claimed. It never opened a real ledger or human private key;
its signing key is a new throwaway fixture key in the scratch home.

After termination the SSDS verified chain reader found 67 entries, `readable_through:66`, `halt:null`, with last
observed commit exactly the real baseline. An absorption entry proves progress to that tree, not completed
projection/classification of its consequences. No missing per-commit results are reconstructed from counts.

## Diagnostic and bounded repair

A focused `cProfile`/30-second traceback probe of `consequence_state` at that scratch position loaded the verified
chain and initial derivation in under one second, then timed out at 240 seconds without a completed consequence
projection. Repeated samples locate large `ssds.unclassified` revision serialization from empty judgment queries
in `Support`. The acceptance-only and three-query intermediate variants subsequently completed but retained
the same eager work in `_valid`. The final local repair removes that work at the existing owners: without
candidate records, acceptance/required-judgment/gate-decision lists are empty; without an acceptance, validity's
best term is F regardless of the remaining conjuncts (§5.5). It changes no identity or record semantics and adds
no cache, alternative deriver or bypass of a required nonempty path.

The final focused projection completed with empty quarantine, ill-formedness, drift, obligations and integrity
maps at position 66. This is one workload result, not a completed historical study or a scientific conclusion.
The intermediate completed probes agree on those five maps. Timings were not a controlled benchmark (some
probes overlapped), so no speedup ratio is asserted. Four implementation variants were examined: original,
acceptance-only guard, three empty-query guards, and those guards plus no-acceptance validity cutoff. Selection
used unchanged-contract correctness and elimination of observed redundant work, not scientific outcomes.

Repair qualification passed: 65 focused tests, fresh Codex code/plan Review, and the complete suite (1,886
tests, 10 skipped, exit 0). Post-update real-program checks also passed. No full historical retry has yet completed. A later completed retry must bind the repaired immutable commit and regenerate exact population,
initialization/exclusion accounting, every finding and every consequence change. Conditional credential-policy
and protected-authorship observations remain counterfactual; record-dependent check 4 remains vacuous.


## Attempt B: eeb870c0; timed out

The qualified repair was committed as `eeb870c007a906c91dc7943b7c8ee4f8124f10e5`. A new native
harness run used `SSDS_HOME=/tmp/ssds-phase-f-preliminary-eeb870c0-20261029`, the same repository and
baseline, that full candidate ID, bundled Git 2.53 and `timeout 1800`. Native output was redirected to
`/tmp/ssds-10d-20261029/preliminary-retry.log`. Exit **124**, empty log and no report. No concurrent
restricted filesystem/agent probes ran during the study window. Its final endpoint comparison was unexecuted;
no boundary PASS or per-commit results are inferred. The verified retained scratch chain has 70 entries,
readable through 69, no integrity halt; last observed `dbd8b92ea460e7ee864e7522bb6d5813ee05141a`.

The requested first-parent population is now 291 deltas after candidate initialization; this count alone
is not a completed initialization/exclusion audit or a difference study. Final frozen 11b remains unexecuted.

## Remaining iteration cost and string-encoding repair

A 90-second cProfile/traceback probe held that scratch parent and evaluated its next child
`8d274c4b7f73faa6269efd231d7deceac4ce620c` through the actual `checks` function. Exit 124. Samples
locate `core.jcs._string` on large unclassified revision strings during `Structural._freeze`. The earlier
Support short circuits remain lawful and useful; they did not eliminate this other required owner's work.

The proposed owning-layer repair replaces the Python character loop in `_string` with standard-library
`json.dumps(text, ensure_ascii=False)` after the same surrogate-code-point refusal. The closed value-domain,
integer, float-refusal, UTF-16 key-ordering and UTF-8 rules remain in their original owners. No identity format,
structural check, frozen Core architecture, cache or alternative serialization path is introduced.

A pre-edit prototype compared predecessor encoding with the replacement over all **1,112,064 Unicode scalar
values** in bounded chunks, and checked refusal of all **2,048 surrogate code points**; exact byte parity passed.
The production regression retains that comparison plus contextual/pair surrogate refusals and existing RFC
vectors. **107 focused tests pass** (canonical JSON, group 1, frames, step 4c). The same complete-iteration probe
now completes with its original real checks; its collection-length diagnostic is not a finding count or classification (checks 1 and 4 are objects).

This is a second local encoding implementation variant (predecessor/replacement), selected for exact byte
compatibility and the observed cost, not scientific results. The probe's final output labels its last stage
`consequences` because the temporary harness was adapted from the prior probe; here that stage actually calls
`study.checks`, as its retained source shows. No speedup ratio is asserted. Code Review and full-suite acceptance
passed before the serialization-repair commit; a complete native historical retry is still owed.

Fresh Codex serialization-repair Review: **PASS**, no blocker or Serious Challenge. Independent checks:
48 affected tests, 1,000 seeded nested-record comparisons against pinned `eeb870c0`, and exhaustive Unicode
scalar parity with the standard-library Python fallback all passed. Reviewed JCS SHA-256:
`0c82c2b4d34dead66c80374ea1b418199725fe41c2ea64db4c977a6feeb521ab`. The complete suite passed: **1,888 tests in 598.721 seconds, 10 skipped, exit 0**, no FAIL/ERROR cases. Source stayed fixed. The post-update real SSDS status and prepared-request reports exactly match steps 24/25; both new endpoint comparisons passed.


## Attempt C and final resumable state

Validated encoding-repair commit: `1abf37cf9e0ef6de445aefce27d386cb3d2a003d`. Native invocation used
`SSDS_HOME=/tmp/ssds-phase-f-preliminary-1abf37cf-20261029`, bundled Git, `PYTHONDONTWRITEBYTECODE=1`,
`timeout 1800`, and the same script/repository/baseline, with that full candidate ID. Output:
`/tmp/ssds-10d-20261029/preliminary-jcs-retry.log`. The log is empty; exit **124**. No concurrent restricted
filesystem or agent probes ran during the study window. No final report or endpoint comparison completed.

Verified scratch progress after termination:

```json
{
  "candidate": "1abf37cf9e0ef6de445aefce27d386cb3d2a003d",
  "exit": 124,
  "timeout_seconds": 1800,
  "entries": 155,
  "readable_through": 154,
  "halt": null,
  "last_observed": "bd515e60609841e8d2478858ceb8c6a7e08a4173",
  "report_exists": false,
  "native_log": ""
}
```

This is progress, not 154 completed projections, zero differences, classification or acceptance. All three
bounded attempts remain incomplete. The latest requested population is 292 deltas after candidate initialization;
the full native initialization/exclusion audit and per-commit output remain owed. The code's exact-byte and
real-owner regression passed; no remaining bottleneck is diagnosed by this timeout alone.

Next agent action: inspect the retained scratch state through SSDS and profile the complete iteration at the
last held parent, including absorption/consequence projection. Choose a sufficiently bounded continuation or
rerun strategy with durable partial-progress visibility before another broad run; do not infer missing results
from absorption counts or bypass any real owner. Final frozen 11b/classification/other-family review and exit
remain unexecuted. No further repair, campaign or authority change is implied.
