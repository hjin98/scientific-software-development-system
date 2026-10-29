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
