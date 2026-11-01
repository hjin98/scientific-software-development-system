# Phase F difference study — preliminary diagnostics and the frozen 11b run

Governing SSDP: 7.2.1; Phase F revision 57, F123–F124; SD-55, SD-64.
Asserter: AI implementing agent, Codex family, 2026-10-29 (preliminary attempts); Claude family, 2026-11-01 (frozen
11b). Infrastructure evidence only.

**Frozen 11b ran COMPLETE at `8cf829c3` (2026-11-01), and its classification is done.** It is below the preliminary
attempts. The independent other-family review of the classification at the frozen candidate (SD-95) is still
required before step 11b is accepted. The preliminary attempts below stay diagnostics and support no acceptance.
The original append qualification gap on `ssdp-shadow-2` stays in
`PHASE-F-10D-SHADOW-LEDGER-EVIDENCE-SSDS-8.0.md`.

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

## Resumed diagnostic: progress retention at the existing harness owner

The prior temporary scratch ledgers/logs disappeared across the usage interruption. Their verified positions
above remain historical reports, not currently re-readable evidence. The earlier instruction to profile the
retained last parent is therefore unavailable on those stores. Do not reconstruct their missing projections.

Local D4 repair planned within F123: publish the existing `difference-study.json` atomically at initialization
and each checks/absorption/consequence boundary. Explicit INCOMPLETE status, pending phase/commit and expected
population prevent partial output from looking like a completed study. Only a fully projected commit enters
the completed rows/counts; an absorbed but unprojected commit stays pending. Product-boundary status remains
UNEXECUTED until the actual final comparison; only a complete successful run can report COMPLETE/unchanged.
This adds visibility to the existing report, no resume engine, alternate semantic owner, skipped check or cache.
It preserves every F123 owner, conditional observation, identity and final F124 review obligation. A sufficiently
bounded preliminary run on an immutable reviewed source can then retain useful partial results without claiming
frozen-candidate acceptance. Tests must discriminate interruption before checks and after absorption, including
row/count identity, expected population and absent boundary/complete claims. Fresh code Review precedes commit.

Progress-retention implementation is now in the existing harness. Focused final regression: **8 tests in
4.363s, OK**; independent fresh Codex review: **PASS**, no blocker or Serious Challenge, with the same eight
tests independently passing in 5.555s and four additional adversarial fixture probes in 2.528s. Those probes
cover initial-projection interruption, failed atomic replace preserving prior whole JSON, final snapshot failure
leaving INCOMPLETE/UNEXECUTED, and pending credential findings excluded from completed counts. No real ledger or
human key was accessed; scratch fixture credentials only. Source SHA256:
`3035fd1d5b768bee2c005b7540e3a73226f96564d8ec81c682efc0d70a27dde6`;
tests SHA256 `9d15ba665d546283789690170a2773f9d98d653f7781cdca86c315920401be0d`.

The first focused launch found a test-only JSON tuple/list round-trip comparison error; the assertion was
corrected to compare JSON values, not Python-only tuple representation. Its failed log is retained separately.
The first full-suite launch had a mislocated requirements-file argument and was deliberately terminated (143)
before acceptance, without changing source. It is not a suite PASS. The requirements were then installed from
the actual `orchestrator/requirements-dev.txt`; a separate full suite is running over fixed source. No commit
or historical run acceptance is inferred while that result is pending.

Review claim limit: setup, scratch genesis and first derivation precede the first report write; interruption
there can still produce no report. Atomic replacement protects process-interruption inspectability, not
power-loss durability. New checkpoints are not resumable execution, complete classification, another-family
review, real-ledger qualification or frozen 11b. F123's exact report JSON shape was delegated; the additional
execution/boundary fields change no accepted semantic contract or review threshold.

<details>
<summary>Independent progress-retention probe output</summary>

```text
test_final_snapshot_failure_never_claims_complete_or_unchanged (__main__.Probe.test_final_snapshot_failure_never_claims_complete_or_unchanged) ... ok
test_initial_projection_interruption_is_explicit (__main__.Probe.test_initial_projection_interruption_is_explicit) ... ok
test_pending_credential_findings_are_not_completed_counts (__main__.Probe.test_pending_credential_findings_are_not_completed_counts) ... ok
test_publication_failure_preserves_previous_whole_document (__main__.Probe.test_publication_failure_preserves_previous_whole_document) ... ok

----------------------------------------------------------------------
Ran 4 tests in 2.528s

OK
```

</details>

Recreated-runtime identities: Python 3.12.14, Git 2.53.0, typer 0.27.3, pydantic 2.14.2, cryptography 50.0.2,
hypothesis 6.170.13 and build 1.6.1. Runtime dependencies came from `pyproject.toml`; acceptance dependencies
from `requirements-dev.txt`. These describe this execution environment, not new supported-version policy.

**Progress-retention final assembled acceptance: PASS.** Full suite over fixed source: **1,892 tests in
604.170s, OK (10 skipped), exit 0**, no FAIL/ERROR cases. The source/test hashes above remain unchanged.
Command, from `orchestrator`: `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 timeout 3000
/tmp/ssds-phase-f-20261029/bin/python -m unittest discover -s tests -t .`; raw final log
`/tmp/ssds-10d-20261029/full-suite-study-progress-final.log`. The earlier terminated launch is not substituted
for this completed run. No frozen protocol/source, profiles/snapshots, Manual/catalogue, Core architecture or
PEM bytes changed. Next: commit this reviewed harness, bind its immutable identity and run one bounded preliminary
study in a new scratch home. Final frozen 11b/other-family review/exit remain unexecuted.


## Attempt D: a1dddd32 — retained partial results, not frozen 11b

Immutable candidate/implementation: `a1dddd329912c6825a6bb95910f4e0c11941e4e6`. The native run used the
installed Python 3.12.14 environment, bundled Git 2.53.0, `PYTHONDONTWRITEBYTECODE=1`, scratch home
`/tmp/ssds-phase-f-preliminary-a1dddd32-20261029`, and `timeout 3600`. No real ledger or human key was opened.
One host-context window contained the before snapshot, progress-only observer, actual harness and after
comparison, with no concurrent restricted tools/agent probes. Native timeout: **124**. Outer product endpoint
comparison: **0, unchanged**. This differs from the original report's own final comparison, which was **not
executed**: its boundary status stays UNEXECUTED, unchanged:null. No internal boundary or completed-study PASS.

The report is retained byte-for-byte in
`PHASE-F-DIFFERENCE-STUDY-PRELIMINARY-a1dddd32.json` (541,220 bytes), SHA256
`4d063c5a0e37a1673bf4571abb696beb9286a80c5b5adac992ab6d30de4c88cd`. It has the complete initialization,
740 excluded first-parent identities/reasons, initial consequences, and **255 completed rows of 298 expected**:
66 through the real baseline, 189 after it. Initialization is `09f35057aec00467372aa8fbbda37f540a9bbc1f`;
it is not counted as an evaluated delta. Last completed row: `cc02814673752b6ad53575e9ca509eada8a71bbd`.
Pending CHECKS: `cee55f617a7837461ecb86ba10d123f5edc9fbf0` with that last commit as parent. **43 deltas remain
unevaluated in this report.** No missing row is inferred from absorption state.

Recount of the retained rows: 510 STRUCT_RESERVED_LEAF observations, exactly the missing ssds.manifest and
ssds.policy on each of 255 evaluated trees; 113 conditional credential-values template observations. Protected
check (3) has no retained touch; check (4) is explicitly vacuous. All five consequence-change maps contain no
additions/removals/changes on these completed rows. This is a bounded scratch-chain observation, not a claim
that omitted records, later commits or scientific behavior cannot change consequences. The template observations
retain only path/code/owners/applicability, no matched lines or values; they establish neither real credentials
nor a current-policy refusal. No raw secret line was retrieved to characterize them.

### Preliminary classification, not other-family/frozen acceptance

`PHASE-F-DIFFERENCE-STUDY-PRELIMINARY-a1dddd32-CLASSIFICATION.json`, SHA256
`e0452bc5b7a0b3d0ffd0f332352756a4354f1cc76c64adcaba5a0ae6508e4abd`, maps every one of the **623** retained
observations to its immutable source report, commit, check and observation index. Agent interpretations under
F124: 510 class (iii), reserved-leaf genesis deviation; 113 class (v), informational counterfactual with unmet
policy enablement. Each class's reason and all applicability limits are retained. This establishes no class
(i) document-control defect or class (iv) SSDS defect. The incomplete final population, genuine frozen 11b run,
complete classification and required independent other-family review remain open. A same-family consistency
check of this partial artifact cannot replace them.

### Supplementary pending-iteration profile

After Attempt D ended, a separate isolated window profiled one real iteration on its scratch ledger through
held-head verification, parent derivation/checks/consequences, actual absorption and after derivation/consequences.
This diagnostic appended only in that throwaway scratch home: entries 256 -> 257, last readable position 256,
no halt. The original report remains byte-identical and INCOMPLETE at255/298. The supplementary result is
`PHASE-F-DIFFERENCE-STUDY-PROFILE-a1dddd32.json`; it is not spliced into the incomplete population or reported
as a resumed study. Native exit0, endpoint comparison0. Exact profiled parent/commit and stage timings are in it.

Profile observations: 98,199,582 calls (97,974,597 primitive) in36.008s under cProfile. Cumulative costs overlap:
structural findings15.590s, derived Python import facts12.441s (2,872 calls), and three read_chain/read_raw paths
12.433/12.108s, involving3,089 Git launches. These are diagnostic timings, not a controlled benchmark, measured
speedup or production SLA. Checks and verification remain required. The remaining cost has shifted to actual
analysis and repeated Git process setup; no further encoding repair is inferred from the timeout alone.

Next discriminating agent action: bound reuse of immutable analyzer facts at their existing owner and/or batch
Git object reads at ledger.read.read_raw, preserving all authenticated verification and exact bytes/order/error
semantics. First compare cost, memory lifetime and complexity; prefer removing repeated work before adding
caches, alternate derivers or resume state. No such source change was made or accepted here. Another broad run
should follow a justified cost/budget strategy rather than blindly repeating the same bounded run. The present
report is intentionally not resumable; its incomplete status and pending stage remain visible.

Original real append failure and R-PROVENANCE-C7 remain unchanged. The real ledger was last observed at
6b8331eb/position9 with10 entries; it was not aligned to these later documentation/harness commits while the
C7 deployment/historical-data decision is pending. Signed-refusal exercise is complete; no signature remains.
No scientific results, scientific gate evidence, scientific variants, native cutover or live campaign occurred.

#### 46-preliminary-progress-study

```json
{
  "at": "2026-10-30T03:54:31.850601+00:00",
  "step": "46-preliminary-progress-study",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/watch_study.py",
    "a1dddd329912c6825a6bb95910f4e0c11941e4e6",
    "/tmp/ssds-phase-f-preliminary-a1dddd32-20261029",
    "3600"
  ],
  "command_exit": 124,
  "comparison_exit": 0,
  "before_sha256": "f124a96a52bd89acdee1aee21284b5a6f25f7018fed0dec61dc6497246e0d915"
}
```

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/46-preliminary-progress-study-before.json
```

#### 47-profile-pending-iteration

```json
{
  "at": "2026-10-30T03:57:15.400119+00:00",
  "step": "47-profile-pending-iteration",
  "command": [
    "timeout",
    "180",
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/profile_pending_iteration.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0,
  "before_sha256": "6b8fae52a8e79f7132bf07c6c5b22f5676ced5770361dd357e6d70870363b786"
}
```

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/47-profile-pending-iteration-before.json
```

<details>
<summary>Supplementary profile output and execution-helper sources</summary>

```text
         98199582 function calls (97974597 primitive calls) in 36.008 seconds

   Ordered by: cumulative time
   List reduced from 976 to 35 due to restriction <35>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        8    0.000    0.000   37.137    4.642 profile_pending_iteration.py:18(stage)
   131/12    0.002    0.000   23.801    1.983 functools.py:982(__get__)
        1    0.000    0.000   15.886   15.886 profile_pending_iteration.py:25(<lambda>)
        1    0.000    0.000   15.886   15.886 difference_study.py:118(checks)
        1    0.000    0.000   15.590   15.590 structural.py:132(findings)
        4    0.000    0.000   14.503    3.626 s0.py:237(defects)
        4    0.000    0.000   14.501    3.625 s0.py:170(relations)
        4    0.206    0.051   12.826    3.206 s0.py:176(derived_relations)
     2872    1.833    0.001   12.441    0.004 python.py:107(imports)
        3    0.000    0.000   12.433    4.144 engine.py:185(chain)
        3    0.000    0.000   12.433    4.144 read.py:289(read_chain)
        3    0.014    0.005   12.108    4.036 read.py:261(read_raw)
     3089    0.017    0.000   12.086    0.004 read.py:245(_git)
     3101    0.018    0.000   11.987    0.004 subprocess.py:506(run)
        1    0.000    0.000   10.942   10.942 structural.py:259(_semantic)
     3101    0.009    0.000   10.931    0.004 subprocess.py:1165(communicate)
     3101    0.065    0.000   10.920    0.004 subprocess.py:2062(_communicate)
    15462    0.026    0.000   10.563    0.001 selectors.py:402(select)
    15462   10.531    0.001   10.531    0.001 {method 'poll' of 'select.poll' objects}
        2    0.000    0.000    8.426    4.213 engine.py:330(held_head)
        2    0.000    0.000    8.184    4.092 difference_study.py:139(consequence_state)
        4    0.000    0.000    8.180    2.045 s3.py:97(findings)
        2    0.000    0.000    8.179    4.090 s3.py:144(obligations)
  3618336    1.227    0.000    7.096    0.000 ast.py:369(walk)
    20596    0.086    0.000    6.700    0.000 lines.py:150(directives)
    10261    0.101    0.000    6.605    0.001 lines.py:58(comment_bodies)
  3615464    0.884    0.000    5.573    0.000 {method 'extend' of 'collections.deque' objects}
        3    0.007    0.002    5.534    1.845 view.py:351(semantic_declarations)
        1    0.000    0.000    4.971    4.971 profile_pending_iteration.py:32(<lambda>)
  7228056    2.375    0.000    4.688    0.000 ast.py:269(iter_child_nodes)
        1    0.000    0.000    4.617    4.617 frames.py:113(write_set)
        1    0.000    0.000    4.617    4.617 writeset.py:85(write_set)
       21    0.000    0.000    4.617    0.220 writeset.py:110(_differs)
        1    0.000    0.000    4.556    4.556 structural.py:209(_freeze)
        4    0.000    0.000    4.556    1.139 state.py:326(subject_triple)


```

### run_stream_step.py

```python
"""Sequential host-only snapshot/command/comparison window; no concurrent probes."""
import datetime,hashlib,json,os,subprocess,sys
from pathlib import Path
root=Path('/home/samjin/agent-skills/scientific-software-development-system')
out=Path('/tmp/ssds-10d-20261029'); name=sys.argv[1]; argv=sys.argv[2:]
assert argv and '/' not in name
before=out/(name+'-before.json'); assert not before.exists(), 'never overwrite a window'
env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':str(root/'orchestrator/src'),
     'PATH':'/home/samjin/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/fallback:'+os.environ['PATH']}
sensor=[sys.executable,str(root/'orchestrator/scripts/shadow_boundary.py')]
with (out/(name+'-snapshot.log')).open('x') as f:
    take=subprocess.run(sensor+['snapshot','--repository',str(root),'--out',str(before)],env=env,stdout=f,stderr=subprocess.STDOUT)
assert take.returncode==0, 'snapshot failed; command not executed'
with (out/(name+'-command.log')).open('x') as f:
    command=subprocess.Popen(argv,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    for line in command.stdout:
        f.write(line); f.flush(); print(line,end='',flush=True)
    command.wait()
with (out/(name+'-compare.log')).open('x') as f:
    compare=subprocess.run(sensor+['compare','--repository',str(root),'--before',str(before)],env=env,stdout=f,stderr=subprocess.STDOUT)
record={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'step':name,'command':argv,
        'command_exit':command.returncode,'comparison_exit':compare.returncode,
        'before_sha256':hashlib.sha256(before.read_bytes()).hexdigest()}
with (out/'steps.jsonl').open('a') as f: f.write(json.dumps(record)+'\n')
print(json.dumps(record,indent=2))
print((out/(name+'-command.log')).read_text())
print((out/(name+'-compare.log')).read_text())
raise SystemExit(0 if command.returncode==compare.returncode==0 else 1)
```

### watch_study.py

```python
"""Same-host progress-only observer around one bounded native scratch study.

The harness remains the only report/semantic owner. This prints no finding values, keys or credentials.
"""
import json,os,subprocess,sys,time
from pathlib import Path
candidate,scratch,budget=sys.argv[1:]
root=Path('/home/samjin/agent-skills/scientific-software-development-system')
log=Path('/tmp/ssds-10d-20261029/preliminary-progress-native.log')
argv=['timeout',budget,sys.executable,str(root/'orchestrator/scripts/difference_study.py'),
      '--repository',str(root),'--candidate',candidate]
assert not log.exists(), 'never overwrite a native run'
env={**os.environ,'SSDS_HOME':scratch,'PYTHONDONTWRITEBYTECODE':'1'}
started=time.monotonic(); last=None
with log.open('x') as output:
    process=subprocess.Popen(argv,env=env,stdout=output,stderr=subprocess.STDOUT)
    while True:
        status=process.poll()
        report=Path(scratch)/'difference-study.json'
        if report.exists():
            data=json.loads(report.read_text())
            info={'elapsed_seconds':round(time.monotonic()-started),'completed':data['summary']['evaluated'],
                  'expected':data['execution']['expected_deltas'],'phase':data['execution']['phase'],
                  'status':data['execution']['status'],'pending':data['execution']['pending']}
            marker=(info['completed'],info['phase'],json.dumps(info['pending']),info['status'])
            if marker!=last or status is not None:
                print(json.dumps(info),flush=True); last=marker
        if status is not None:
            print(json.dumps({'native_exit':status,'native_log':str(log),'command':argv}),flush=True)
            print(log.read_text(),flush=True)
            raise SystemExit(status)
        time.sleep(30)
```

### profile_pending_iteration.py

```python
"""Supplementary real-owner iteration diagnostic, not a resumed or completed study."""
import cProfile,hashlib,importlib.util,io,json,pstats,sys,time
from functools import lru_cache
from pathlib import Path
root=Path('/home/samjin/agent-skills/scientific-software-development-system')
sys.path.insert(0,str(root/'orchestrator/scripts'))
spec=importlib.util.spec_from_file_location('study',root/'orchestrator/scripts/difference_study.py')
study=importlib.util.module_from_spec(spec);spec.loader.exec_module(study)
home=study.AdmissionHome(Path('/tmp/ssds-phase-f-preliminary-a1dddd32-20261029'))
path=home.root/'difference-study.json'; raw=path.read_bytes(); report=json.loads(raw)
assert report['execution']['status']=='INCOMPLETE' and report['execution']['phase']=='CHECKS'
assert hashlib.sha256(raw).hexdigest()=='4d063c5a0e37a1673bf4571abb696beb9286a80c5b5adac992ab6d30de4c88cd'
pending=report['execution']['pending']; timings={}; profile=cProfile.Profile()
@lru_cache(maxsize=8)
def trees(commit): return study.read_tree(root,commit)
graph=study.ancestry(home.ledger_repository(study.LEDGER))
admission=study.observe_only(home.root,study.LEDGER,trees,root,graph,study.shadow_boundary)
def stage(name,call):
    start=time.monotonic(); result=call();timings[name]=time.monotonic()-start;return result
profile.enable()
chain=stage('held_head_before',admission.held_head)
assert chain.halt is None and chain.readable_through==len(chain.entries)-1
assert len(chain.entries)==256 and study.expected_head(chain.entries)==pending['parent']
support=stage('derive_parent',lambda:study.derive(chain,trees,ancestry=graph))
found=stage('checks',lambda:study.checks(support,pending['parent'],pending['commit']))
previous=stage('parent_consequences',lambda:study.consequence_state(support))
assert previous==report['initialization']['consequences']  # original report has no consequence changes
stage('absorb',lambda:admission.absorb(list(chain.entries),pending['commit']))
after=stage('held_head_after',admission.held_head)
assert after.halt is None and len(after.entries)==257 and after.readable_through==256
current=stage('derive_after',lambda:study.derive(after,trees,ancestry=graph))
consequences=stage('after_consequences',lambda:study.consequence_state(current))
profile.disable()
assert path.read_bytes()==raw, 'original partial study report stays untouched'
result={'candidate':report['candidate'],'original_report_sha256':hashlib.sha256(raw).hexdigest(),
 'scope':'one supplementary pending iteration on the scratch ledger; not a resumed/completed historical study',
 'parent':pending['parent'],'commit':pending['commit'],'before_entries':256,'after_entries':257,
 'timings_seconds':timings,'checks':found,'consequence_changes':study.changes(previous,consequences),
 'limit':'original report remains INCOMPLETE at255/298; remaining43 rows/final harness boundary/classification unexecuted'}
out=Path('/tmp/ssds-10d-20261029/pending-iteration-profile-result.json')
assert not out.exists();out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
stream=io.StringIO();pstats.Stats(profile,stream=stream).strip_dirs().sort_stats('cumulative').print_stats(35)
Path('/tmp/ssds-10d-20261029/pending-iteration-profile.txt').write_text(stream.getvalue())
print(json.dumps({k:v for k,v in result.items() if k not in ('checks','consequence_changes')},indent=2))
print(stream.getvalue())
```

### classify_partial.py

```python
import collections,hashlib,json
from pathlib import Path
q=Path('/home/samjin/agent-skills/scientific-software-development-system/qualification/ssds80')
p=q/'PHASE-F-DIFFERENCE-STUDY-PRELIMINARY-a1dddd32.json';d=json.loads(p.read_text())
sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='4d063c5a0e37a1673bf4571abb696beb9286a80c5b5adac992ab6d30de4c88cd'
rows=[]
for row in d['commits']:
    assert row['checks']['3']==[] and all(not items for c in row['consequence_changes'].values() for items in c.values())
    assert len(row['checks']['2'])==2 and {f['unit'] for f in row['checks']['2']}=={'ssds.manifest','ssds.policy'}
    for check,findings in [('2',row['checks']['2']),('1.credential_template',row['checks']['1']['credential_template'])]:
        for index,finding in enumerate(findings):
            if check=='2':
                assert finding['code']=='STRUCT_RESERVED_LEAF'
                cls='iii';reason='reserved_leaf_genesis_deviation'
            else:
                assert finding['code']=='credential_values'
                assert finding['applicability']=='if policy enabled it; supplemental template, no current-policy verdict'
                cls='v';reason='unmet_policy_enablement'
            source={'commit':row['commit'],'check':check,'index':index}
            identity=hashlib.sha256(json.dumps({'source':source,'finding':finding},sort_keys=True,separators=(',',':')).encode()).hexdigest()
            rows.append({'id':'sha256:'+identity,'source':source,'code':finding['code'],'class':cls,'reason':reason})
result={'schema':1,'status':'PRELIMINARY_NOT_FROZEN_ACCEPTANCE','asserter':'AI implementing agent, Codex family',
 'governing_protocol':'7.2.1','authority':'Phase F F123/F124; class reasons are preliminary agent interpretations, not other-family acceptance',
 'candidate':d['candidate'],'source_report':p.name,'source_sha256':sha,'completed_deltas':255,'expected_deltas':298,
 'reasons':{
  'reserved_leaf_genesis_deviation':{'class':'iii','meaning':'The bounded historical genesis exempts only ssds.manifest and ssds.policy. Post-genesis structural checks retain their absence on each evaluated tree; these observations concern the declared genesis deviation, not a newly established document-control defect.'},
  'unmet_policy_enablement':{'class':'v','meaning':'The report labels this the supplemental credential-values template if policy enabled it, with no current-policy verdict. Policy/contract enablement is not established by these observations. No credential value or actual defect is inferred; matched lines/values are neither retained nor reconstructed.'}},
 'summary':dict(collections.Counter(r['class'] for r in rows)),'observations':rows,
 'limits':['43 deltas remain unevaluated in the original report, including its pending commit',
           'supplementary profiled iteration is separate and is not spliced into that report',
           'original report final boundary is UNEXECUTED; outer isolated run-window endpoint comparison passed',
           'no class i or iv defect established by this preliminary classification',
           'checks1/3 are conditional, check4 vacuous; record-dependent effects require the later authorized campaign',
           'complete frozen 11b/classification and independent other-family review remain required']}
out=q/'PHASE-F-DIFFERENCE-STUDY-PRELIMINARY-a1dddd32-CLASSIFICATION.json'
assert not out.exists();out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'observations':len(rows),'classes':result['summary'],'classification_sha256':hashlib.sha256(out.read_bytes()).hexdigest()},indent=2))
```

</details>

**Fresh Codex partial-artifact/classification review: PASS**, no blocker or Serious Challenge. Independent
read-only Git/data audit reconciled1,039 first-parent commits =740 exclusions+one initialization+298 deltas,
all255 completed rows/parents and baseline split66+189. Static Git/TOML checks found690 excluded trees without
a manifest and50 with the earlier manifest lacking ssds.unclassified; initialization and all255 evaluated trees
contain it while lacking the two exempted leaves. Every623 classification identity and source mapping was
recomputed, as were class counts and zero consequence changes. Step46/47 exits and separation of profile versus
original report matched raw evidence. No real/scratch native operation or private-home access by the reviewer.

Review limits: no rerun of genesis/structural/derivation owners, independent initialization-sufficiency proof,
scratch-state check or repeated boundary probe. Both artifacts and review share the harness/production owners;
common-mode limitations remain. Same-family recorded-consistency/classification Review cannot substitute for
frozen11b, omitted rows, complete classification or independent other-family Review. DONE PROBING.


## Final bounded repetition measurement — no cache introduced

Step48 replayed only the supplementary iteration's checks and parent/after consequence projection on historical
positions255/256 of the existing scratch chain. Every imports call executed the original pure analyzer; the
wrapper counted path/content-hash input identities and asserted identical repeated facts. Checks and consequence
changes exactly matched the earlier profile result. No source, scratch append or original report write occurred.
Native exit0/comparison0 in one isolated host window; source hash remains the reviewed a1dddd32 harness.

Measured2,872 imports calls over718 distinct path/content inputs:2,154 repeats. Input-byte sum across calls:
21,881,284; distinct-input bytes:5,470,321; largest single input:209,606 bytes. Repeated facts disagreed0 times.
Retained artifact `PHASE-F-DIFFERENCE-STUDY-IMPORT-REUSE-a1dddd32.json`, SHA256 `17a30e320045690aff30af3f25a5f9db3011ccdd15b1a938c7a5abdc3a54b091`.
This is one iteration's duplication/memory-input observation, not a global cache capacity/memory bound,
a controlled benchmark, a measured speedup or proof that all analyzer consumers are correct. The wrapper
retains only digest/size/count metadata; it does not reuse returned facts or retain/print source values.

Concrete next local experiment: compare bounded reuse of the immutable import facts at the existing analyzer
owner, keyed by the pinned analyzer implementation, path and exact content, with unmodified results and all
failure/incompleteness markers. Choose a lifetime and memory bound using the real workload before production
adoption; a count-only cache limit is not a global byte bound. Do not cache mutable ASTs, collapse different paths
(relative-import meaning depends on path), skip an analysis, or infer full-study conformance from this one sample.
Prefer the smallest existing-owner change; repeated Git process setup is a separately measured remaining cost,
not a reason to bypass chain authentication. Any eventual source candidate still owes independent code review,
affected tests and full acceptance before another appropriately budgeted preliminary run.

```json
{
  "at": "2026-10-30T04:07:31.241372+00:00",
  "step": "48-count-import-reuse",
  "command": [
    "timeout",
    "120",
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/count_import_reuse.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0,
  "before_sha256": "4b182f5b6366e979211c1e114b75df61c11732b965527436550f8e360c762dc8"
}
```

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/48-count-import-reuse-before.json
```

<details>
<summary>Exact read-only repetition-counter source</summary>

```python
"""Count identical pure-owner inputs; always execute the original analyzer. No cache or source change."""
import hashlib,importlib.util,json,sys,time
from dataclasses import asdict
from functools import lru_cache
from pathlib import Path
from unittest.mock import patch
root=Path('/home/samjin/agent-skills/scientific-software-development-system')
sys.path.insert(0,str(root/'orchestrator/scripts'))
spec=importlib.util.spec_from_file_location('study',root/'orchestrator/scripts/difference_study.py')
study=importlib.util.module_from_spec(spec);spec.loader.exec_module(study)
from ssds import analyzers
from ssds.ledger.read import read_chain
home=study.AdmissionHome(Path('/tmp/ssds-phase-f-preliminary-a1dddd32-20261029'))
report_path=home.root/'difference-study.json';raw=report_path.read_bytes();report=json.loads(raw)
assert hashlib.sha256(raw).hexdigest()=='4d063c5a0e37a1673bf4571abb696beb9286a80c5b5adac992ab6d30de4c88cd'
chain=read_chain(home.ledger_repository(study.LEDGER),study.LEDGER)
assert chain.halt is None and len(chain.entries)==257 and chain.readable_through==256
expected=json.loads(Path('/tmp/ssds-10d-20261029/pending-iteration-profile-result.json').read_text())
owner=analyzers.python.imports;seen={};calls=0;total_bytes=0
@lru_cache(maxsize=8)
def trees(commit):return study.read_tree(root,commit)
def counted(path,data):
    global calls,total_bytes
    result=owner(path,data)  # never reuse/replace its result
    key=(path,hashlib.sha256(data).hexdigest())
    value=hashlib.sha256(json.dumps(asdict(result),sort_keys=True).encode()).hexdigest()
    if key in seen:
        assert seen[key]['result']==value
        seen[key]['calls']+=1
    else:seen[key]={'bytes':len(data),'calls':1,'result':value}
    calls+=1;total_bytes+=len(data)
    return result
started=time.monotonic();graph=study.ancestry(home.ledger_repository(study.LEDGER))
with patch.object(analyzers.python,'imports',counted):
    parent=study.derive(chain,trees,position=255,ancestry=graph)
    checks=study.checks(parent,expected['parent'],expected['commit'])
    before=study.consequence_state(parent)
    after=study.consequence_state(study.derive(chain,trees,position=256,ancestry=graph))
assert json.loads(json.dumps(checks))==expected['checks']
assert json.loads(json.dumps(study.changes(before,after)))==expected['consequence_changes']
assert report_path.read_bytes()==raw
result={'scope':'read-only supplementary repetition count; original import analyzer executes on every call',
 'candidate':report['candidate'],'parent':expected['parent'],'commit':expected['commit'],
 'original_report_sha256':hashlib.sha256(raw).hexdigest(),'same_checks_and_changes_as_profile':True,
 'imports_calls':calls,'unique_path_content_inputs':len(seen),'repeated_identical_inputs':calls-len(seen),
 'sum_input_bytes_all_calls':total_bytes,'sum_unique_input_bytes':sum(v['bytes'] for v in seen.values()),
 'largest_unique_input_bytes':max(v['bytes'] for v in seen.values()),
 'repeated_input_fact_disagreements':0,'elapsed_seconds_unprofiled_with_counting':time.monotonic()-started,
 'limits':['one pending iteration only, not a global cache capacity bound','no cache introduced or measured speedup claimed',
 'no source, original report or scratch ledger append','original historical study stays incomplete255/298',
 'prospective reuse needs bounded lifetime/key/memory and exact semantic-equivalence validation']}
out=Path('/tmp/ssds-10d-20261029/import-reuse-count-result.json');assert not out.exists()
out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');print(json.dumps(result,indent=2))
```

</details>


Fresh Codex final counter/evidence review: **PASS**, no blocker, unexplained closure or Serious Challenge.
The artifact matches the raw result/native log; exact helper source, identity bindings, arithmetic, report
SHA/INCOMPLETE255/298 and command0/comparison0 agree. The helper always calls/returns the original analyzer,
checks repeated-fact fingerprints and exactly reproduces prior checks/changes; it contains no ledger append,
original-report write or production-source edit. Review did not execute owners or boundary probes, inspect
scratch state, or reconstruct a per-call event trace (none retained). Execution/source/log evidence and shared
harness-owner common modes bound the claim. All prior omitted/frozen/other-family/exit/C7/original-gap duties
remain. Reviewer DONE PROBING. Final continuation opening merely projects these reviewed factual states.


## Cost repairs R-COST-IMPORTS and R-COST-CHAIN-READ (2026-10-30)

Asserter: AI implementing agent, Claude family (Opus 5.5), resuming from the Codex-family handoff; governing SSDP 7.2.1.
Stakeholder direction recorded at the start of this resume: C7 route **held, decide later**; original append gap
**left open**; boundary-checked scratch windows may run in the user's terminal (the agent's Bash sandbox masks
repository-root dotfiles with `/dev/null` character devices, and `shadow_boundary.py` correctly refuses them as
unsupported entries — step 49 snapshot failed and executed no command; the sensor was not weakened).

Both measured costs of the supplementary profile were repaired at their existing owners, with no new deriver,
resume state or skipped analysis:

- **R-COST-IMPORTS** — `analyzers/python.py`. `imports(path, data)` reuses earlier facts from a process-wide LRU
  keyed by the path (relative imports depend on it) and the SHA-256 of the exact bytes; the analysis itself is
  unchanged in `_imports`. Facts are immutable and keep every incompleteness marker. The bound is the summed
  `sys.getsizeof` of retained keys/facts (8 MiB), not an entry count; an oversized result is returned exactly and
  not retained. This accounting is approximate (dict nodes and the `(facts, size)` tuple are not counted; shared
  strings are counted more than once), not an RSS guarantee.
- **R-COST-CHAIN-READ** — `ledger/read.py`. `read_raw` reads every commit, tree and blob through one
  `git cat-file --batch` process and walks raw tree objects with an explicit stack in `ls-tree -r` order, instead
  of `cat-file commit` + `ls-tree -r -z` + `cat-file blob` per file. `verify_chain` and every authentication step
  are unchanged. A missing object, wrong type, empty entry name, non-octal mode, truncated tree or abbreviated tree
  line rejects the chain (`ChainRejected`) as the per-object reads did. Deliberate strict difference: a head
  containing NUL is `ChainRejected` (formerly a plain `ValueError` from `subprocess`).

### Measured effect (read-only replay, equal results)

Steps 49c (pre-review source) and **49d (final source)** each ran in one host window (`compare_costs.py`;
command 0, comparison 0, repository unchanged). They replayed the profiled iteration's derivation at positions
255/256, checks and parent/after consequences on the read-only a1dddd32 scratch chain, alternating old source
`7e9649d1` and the new working source twice each. Chain digest, entry bytes, object count, checks and consequence
changes were asserted equal across all four runs and to the step-47 profile result, and every loaded `ssds`
module was asserted to come from the variant under test. Final (49d) figures:

| | old 7e9649d1 | new (final) |
|---|---|---|
| replay total | 15.04 s, 15.11 s | 7.61 s, 7.77 s |
| `read_chain` of 257 entries | 3.89 s, 1,031 process launches | 0.11 s, 2 launches |
| parent / after consequences | 1.23 s / 2.03-2.09 s | 0.01 s / 0.87-0.89 s |
| checks | 7.66-7.67 s | 6.37-6.56 s |
| retained import facts | — | 718 entries, 814,123 accounted bytes |

49c on the pre-review source measured the same shape (14.7 s vs 7.5 s). One iteration, one host, unprofiled
wall-clock; not a controlled benchmark, an SLA or a global memory bound. Cross-iteration reuse inside one long
study process is expected but not measured here. Checks (structural semantics, line directives) now dominate.
Earlier attempts are retained: step 49's snapshot was refused inside the agent sandbox (no command ran); 49b's
first replay stopped on its own module-identity assertion because the harness prepends the repository `src`
(fixed by importing the variant first); comparison 0 in 49b.

### Review and qualification

Same-family review (Claude subagent) of the first version: **NO-PASS**, three blockers in the batched tree walk,
all reproduced by its differential probe against the real old `read_raw` in sha1 and sha256 repositories:
B1 empty entry name accepted (would turn whole-chain rejection into a positional halt); B2 mode digits 8/9 raised
`ValueError`; B3 nesting beyond ~1,000 levels raised `RecursionError`. Notes: NUL in head accepted; two tree lines
rejected; width taken from commit text; several surviving test mutants; oracle not exactly the old code.
Analyzer memo, fitness rules, architecture (§26) and scientific-checks questions: no finding.

Repairs: explicit-stack walk; empty name and non-octal mode rejected; width from the batch-reported identity; tree
line must be a full 40/64-hex first header line; NUL rejected; oracle given the old environment and JSON guard.
The reviewer's probe then reported SAME for every case in both formats except the deliberate NUL rejection.
New tests: `BatchedChainRead`, `StoredObjectEdges` (sha1+sha256 differential incl. tag peeling, interleaved order,
odd directory mode, directory-entry-to-blob, 1,101-level nesting), `ImportFactReuse`. Mutants killed: cache key
without path or content, no bound, no tree recursion, no blob/commit peel, no type check, width 20,
subtrees-last ordering, equality instead of directory mask, no empty-name check, digit-only mode check, no NUL
check. Equivalent mutant: taking any `tree` line (Git's own `^{commit}` peel rejects a commit not starting with it).

Narrow same-family re-check of the repair: **PASS**, no blocker. Its second differential probe (35 further cases per
object format: empty/only-subtree trees, malformed nested entries after valid siblings, trailing garbage, tag
chains, gitlinks in nested directories, extreme directory modes, junk in commit headers, missing parents, bad or
non-object JSON, a 300 KB blob, depth 3,000) reported SAME throughout; a cleanup probe under `-X dev` with
ResourceWarning as error reaped the process with all pipes closed on every exception path. Its notes were taken
up: the tree-identity regex was removed (it alone rejected an uppercase-hex tree line Git accepts, and was
otherwise redundant with the peel), and truncated-entry and empty-mode cases were added (both mutants now
killed). Untested-but-correct by inspection: the `_environment()` argument and the `finally` close.
Final probes: SAME for every case in both formats except the deliberate NUL rejection.

The first complete suite over the pre-re-check source passed (1,901 tests, 521.6 s, OK, 10 skipped);
the final complete suite over the fixed final source passed: **1,901 tests in 519.492 s, OK (10 skipped),
exit 0**, no FAIL/ERROR lines (log `full-suite-cost-repair-final.log`). Hashes of the tested files:
`analyzers/python.py` `61073075ea6e109c71887197b17b28751847a8a12bab47883b4eba59acb6b74c`; `ledger/read.py` `11f1264a4b1e1afba8fbcdda9025cb98846a78e7a578b3216d7f37fca12f79e6`; `test_phase_f_step11a.py` `4c96d812759ed865e1fcc880a57709c67de8f71ba3466da33d6eba841312525c`. Orchestrator protocol-snapshot check
passed; Core is unchanged. Protocol source, `dist/`, profiles, snapshots, Manual/catalogue, frozen Core
architecture and PEM are untouched; PEM stayed cold (a clean local cost repair; no history-dependent decision).

### Window records (raw evidence under `/tmp/claude-1000/ssds-phase-f-cost-20261030`)

```json
{"at": "2026-10-30T16:09:16.096399+00:00", "step": "49b-cost-comparison", "command": ["/tmp/ssds-phase-f-20261029/bin/python", "/tmp/claude-1000/ssds-phase-f-cost-20261030/compare_costs.py", "/tmp/claude-1000/ssds-phase-f-cost-20261030"], "command_exit": 1, "comparison_exit": 0, "before_sha256": "a171a5bcd1268cf55a18f153bcdd4416f98121cb7a68380f78a10c8cb496c346"}
{"at": "2026-10-30T16:10:38.670391+00:00", "step": "49c-cost-comparison", "command": ["/tmp/ssds-phase-f-20261029/bin/python", "/tmp/claude-1000/ssds-phase-f-cost-20261030/compare_costs.py", "/tmp/claude-1000/ssds-phase-f-cost-20261030"], "command_exit": 0, "comparison_exit": 0, "before_sha256": "1dd2a614c90729eb9cabb2da718c9555e95c177b3cb709f0e126ce611a1e246e"}
{"at": "2026-10-30T16:47:41.162334+00:00", "step": "49d-cost-comparison-final", "command": ["/tmp/ssds-phase-f-20261029/bin/python", "/tmp/claude-1000/ssds-phase-f-cost-20261030/compare_costs_final.py", "/tmp/claude-1000/ssds-phase-f-cost-20261030", "cost-comparison-final-result.json"], "command_exit": 0, "comparison_exit": 0, "before_sha256": "5cfb80bb7f3c9779a0e1f360448f76c17699c771caee6a5fbe7dcc51001c0161"}
```

Step 49 (no record): `unsupported filesystem entry in boundary snapshot: <repository>/.bash_profile` inside the agent sandbox.

Result `cost-comparison-final-result.json`, SHA256 `3de9c32b5c6cf5e6a0367e37c1871c6289cd9b42215bd12d835856f53c05c82a`.

<details>
<summary>replay.py (SHA256 0c107f00b4c53a86d67aee93efc7d57c011f0f7fcd6a88e1cb93697eb9da93be)</summary>

```python
"""Read-only replay of the profiled iteration's checks and consequences over one source variant. No append."""
import hashlib,importlib.util,json,subprocess,sys,time
from functools import lru_cache
from pathlib import Path
src=Path(sys.argv[1]);sys.path.insert(0,str(src))
root=Path('/home/samjin/agent-skills/scientific-software-development-system')
import ssds;assert Path(ssds.__file__).resolve().is_relative_to(src.resolve()),ssds.__file__  # before the harness pins the repository src
sys.path.insert(1,str(root/'orchestrator/scripts'))
spec=importlib.util.spec_from_file_location('study',root/'orchestrator/scripts/difference_study.py')
study=importlib.util.module_from_spec(spec);spec.loader.exec_module(study)
from ssds import analyzers
from ssds.ledger.read import read_chain
launches=0;real=subprocess.Popen.__init__
def counted(self,*a,**k):
    global launches;launches+=1;return real(self,*a,**k)
subprocess.Popen.__init__=counted
home=study.AdmissionHome(Path('/tmp/ssds-phase-f-preliminary-a1dddd32-20261029'))
report=home.root/'difference-study.json';raw=report.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='4d063c5a0e37a1673bf4571abb696beb9286a80c5b5adac992ab6d30de4c88cd'
expected=json.loads(Path('/tmp/ssds-10d-20261029/pending-iteration-profile-result.json').read_text())
@lru_cache(maxsize=8)
def trees(commit):return study.read_tree(root,commit)
times={};counts={}
def stage(name,call):
    global launches;before=launches;start=time.monotonic();result=call()
    times[name]=time.monotonic()-start;counts[name]=launches-before;return result
chain=stage('read_chain',lambda:read_chain(home.ledger_repository(study.LEDGER),study.LEDGER))
assert chain.halt is None and len(chain.entries)==257 and chain.readable_through==256
graph=study.ancestry(home.ledger_repository(study.LEDGER))
parent=stage('derive_parent',lambda:study.derive(chain,trees,position=255,ancestry=graph))
checks=stage('checks',lambda:study.checks(parent,expected['parent'],expected['commit']))
before=stage('parent_consequences',lambda:study.consequence_state(parent))
after=stage('after_consequences',lambda:study.consequence_state(study.derive(chain,trees,position=256,ancestry=graph)))
assert json.loads(json.dumps(checks))==expected['checks']
assert json.loads(json.dumps(study.changes(before,after)))==expected['consequence_changes']
assert report.read_bytes()==raw
foreign=[n for n,m in sys.modules.items() if n.split('.')[0]=='ssds' and getattr(m,'__file__',None) and not Path(m.__file__).resolve().is_relative_to(src.resolve())]
assert not foreign,foreign
memo=getattr(analyzers.python,'_imports_retained',None)
print(json.dumps({'source':str(src),'chain_digest':hashlib.sha256(''.join(e.digest for e in chain.entries).encode()).hexdigest(),
 'entry_bytes_sha256':hashlib.sha256(b''.join(e.entry_json+e.signature for e in chain.entries)).hexdigest(),
 'objects':sum(len(e.objects) for e in chain.entries),'seconds':times,'total_seconds':sum(times.values()),
 'process_launches':counts,'checks_and_changes_match_profile':True,
 'retained_import_facts':None if memo is None else len(memo),
 'retained_import_bytes':None if memo is None else analyzers.python._imports_size},sort_keys=True))
```

</details>

<details>
<summary>compare_costs_final.py (SHA256 8469af15a9ecc7bcc51629de1d618ed474d0dee3ff87a2e3b4af255b00a3649b)</summary>

```python
"""Alternate old/new source variants of the read-only replay; equal results required."""
import json,os,subprocess,sys
from pathlib import Path
out=Path(sys.argv[1]);root=Path('/home/samjin/agent-skills/scientific-software-development-system')
variants={'old-7e9649d1':out/'old/orchestrator/src','new-working':root/'orchestrator/src'}
runs=[]
for round_ in range(2):
    for name,src in variants.items():
        env={k:v for k,v in os.environ.items() if k!='PYTHONPATH'};env['PYTHONDONTWRITEBYTECODE']='1'
        done=subprocess.run([sys.executable,str(out/'replay.py'),str(src)],env=env,capture_output=True,text=True,timeout=900)
        if done.returncode:print(done.stdout,done.stderr);raise SystemExit(f'{name} failed')
        runs.append({'variant':name,'round':round_,**json.loads(done.stdout.strip().splitlines()[-1])})
keys=('chain_digest','entry_bytes_sha256','objects','checks_and_changes_match_profile')
assert len({tuple(r[k] for k in keys) for r in runs})==1,'variants disagree'
result={'scope':'read-only replay of the profiled iteration at positions255/256; no append, no report write',
 'runs':runs,'equal_across_variants':list(keys)}
target=out/sys.argv[2];assert not target.exists()
target.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
for r in runs:print(r['variant'],r['round'],round(r['total_seconds'],2),r['seconds'],r['process_launches'],r['retained_import_facts'],r['retained_import_bytes'])
```

</details>


## Attempt E: 6ae91c3d — COMPLETE preliminary study, not frozen 11b

Step 50 ran one host window (user's terminal; no agent tool ran during it) around the existing harness through a
progress-only watcher identical to step 46's except its log path. Candidate **`6ae91c3d733365246018fe18f49dd4fadddc6db8`**
(the cost-repair commit), new scratch home `/tmp/claude-1000/ssds-phase-f-preliminary-6ae91c3d-20261030`,
budget 7,200 s. Native exit **0** after about 1,650 s; outer window comparison **0** (repository unchanged).
The report's own final boundary comparison **executed and PASSED** (`unchanged: true`), status **COMPLETE**.

Population: 1,042 first-parent commits = 740 exclusions + initialization `09f35057` + **301 evaluated deltas**
(the a1dddd32 population plus `82ad1bd3`, `7e9649d1`, `6ae91c3d`); 66 through the real baseline and 235 after.
Findings by code: STRUCT_RESERVED_LEAF 600, credential_values 154, AUTH_PROTECTED 14; one row with consequence
changes. Retained report `PHASE-F-DIFFERENCE-STUDY-PRELIMINARY-6ae91c3d.json`, 630,251 bytes, SHA256
`a6d4943e66bace0b6da6b88f60b986807ac39b73ba98c59313e55d2fd5061cd0`.

**Regression evidence for the cost repairs.** All 255 rows shared with the a1dddd32 partial report (old source)
are identical, as are initialization and exclusions, and the old row order is a prefix of the new. The repairs
changed no study result on that common population.

**Rows beyond the earlier partial report.** Commit `11ec88e4` (row 288) declares the reserved leaves and creates
`.ssds/policy.toml` (`schema = 1`, no listed surfaces). On the scratch ledger its absorption quarantines the eight
declaration keys and derives eight INTAKE obligations ("quarantined delta"): absorption never changes the effective
structure and Admission never adopts on its own (Manual §8.6, §18), and the scratch genesis has no counterpart of
the human `ABSORB` adoption the real ledger admitted at position 2 (SD-69). Effective structure therefore keeps the
reserved-leaf deviation on rows 289-300. The genesis-named policy path is always protected (`protected_surfaces`);
the manifest is not. Row 288 touches the policy file and authors the `ssds.policy` unit; afterwards the quarantined
file belongs to `ssds.unclassified`, so `protected_touched` (unit granularity) flags every later write to that unit
although rows 289-300 never change the policy file. In any structure the Manual accepts, `ssds.policy` is its own
leaf and unit- and path-level detection coincide; this is a conservative consequence of the class (iii) deviation.

### Preliminary classification, not other-family/frozen acceptance

`PHASE-F-DIFFERENCE-STUDY-PRELIMINARY-6ae91c3d-CLASSIFICATION.json` maps all **784** observations to source
report, commit, check and index. Preliminary F124 classes: **616 (iii)** (576 genesis deviation before 11ec88e4;
24 reserved-leaf repair quarantined in scratch; 16 row-288 quarantine keys and INTAKE obligations of the absorbed
repair), **168 (v)** (14 protected touches, authorship unestablished; 154 credential templates, policy enablement
absent). No class (i) or (iv) defect is established.
No matched line or value was retrieved or retained. Classification SHA256
`03c353d4e40b126e7b75099fb56cfd3b793a831c53066581dc8b6fdd4bf37900`; generator `classify_complete.py` SHA256
`1223aa2f7a3e6767173509ac64d989e165b61c870fc5d6b59a6b687be5ab57ad` (raw evidence directory).

Same-family classification review: **NO-PASS** on one reason text (it wrongly said the committed policy protects
the manifest and policy files); corrected as above. It independently rebuilt all 784 identities and sources,
confirmed the 255-row identity, the contiguous parent chain, the baseline split and every count, and found the
protected-touch behaviour consistent with the Manual (§1.2/SD-14 effective-unit write set, §1.8-§1.9, §8.3,
§25.3; F14): not class (iv), no Serious Challenge. Its note that the 16 row-288 consequences are not a refusal was
taken up (reclassified from (ii) to (iii); decision-neutral). Open presentation note for the derivation owner: the
detail "ssds.unclassified is a protected surface" (`writescope.py`) means the unit *contains* one.

Limits: this candidate is not frozen — R-PROVENANCE-C7 keeps step 2 reopened, so source may still change, and a
preliminary result is not promoted into 11b by completing. Checks 1 and 3 are conditional, check 4 vacuous;
record-dependent behaviour needs an authorized campaign. Consequences belong to the scratch ledger. Frozen 11b,
its classification and independent other-family review remain required, as do step 12, C7 and the original gap.

#### 50-preliminary-study-6ae91c3d

```json
{
  "at": "2026-10-30T17:16:35.990049+00:00",
  "step": "50-preliminary-study-6ae91c3d",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/claude-1000/ssds-phase-f-cost-20261030/watch_study.py",
    "6ae91c3d733365246018fe18f49dd4fadddc6db8",
    "/tmp/claude-1000/ssds-phase-f-preliminary-6ae91c3d-20261030",
    "7200"
  ],
  "command_exit": 0,
  "comparison_exit": 0,
  "before_sha256": "8ac063c8ff03620841862264f0045b4208d08ae16f863459b438c71a47e2c8ff"
}
```

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/claude-1000/ssds-phase-f-cost-20261030/50-preliminary-study-6ae91c3d-before.json
```

Watcher `watch_study.py` SHA256 `fa3ccfd56e9aab9c6f7afd9e48c51886f02239551399c9b39ae488c272f2fb5a` (step 46 source with its log path changed); window helper `run_step.py` SHA256 `ca88b7f1deeb16b163f8ed14f8b8f01d02326195c31ad35004c6b15c857c1abe` (step-46 helper with its output directory changed).

<details>
<summary>classify_complete.py</summary>

```python
"""Preliminary F124 classification of the complete 6ae91c3d preliminary report. Retains no matched line/value."""
import collections,hashlib,json
from pathlib import Path
q=Path('/home/samjin/agent-skills/scientific-software-development-system/qualification/ssds80')
p=q/'PHASE-F-DIFFERENCE-STUDY-PRELIMINARY-6ae91c3d.json';raw=p.read_bytes();d=json.loads(raw)
sha=hashlib.sha256(raw).hexdigest();assert sha=='a6d4943e66bace0b6da6b88f60b986807ac39b73ba98c59313e55d2fd5061cd0'
assert d['execution']['status']=='COMPLETE' and d['boundary']['status']=='PASSED' and len(d['commits'])==301
repair=[i for i,r in enumerate(d['commits']) if r['commit'].startswith('11ec88e4')];assert len(repair)==1;repair=repair[0]
rows=[]
def add(row,check,index,finding,cls,reason):
    source={'commit':row['commit'],'check':check,'index':index}
    identity=hashlib.sha256(json.dumps({'source':source,'finding':finding},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    rows.append({'id':'sha256:'+identity,'source':source,'code':finding.get('code',finding.get('kind')),'class':cls,'reason':reason})
for i,row in enumerate(d['commits']):
    c=row['checks']
    assert c['4']['status']=='vacuous'
    if i==repair: assert c['2']==[]
    else: assert {f['unit'] for f in c['2']}=={'ssds.manifest','ssds.policy'} and len(c['2'])==2
    for n,f in enumerate(c['2']):
        assert f['code']=='STRUCT_RESERVED_LEAF'
        add(row,'2',n,f,'iii','reserved_leaf_genesis_deviation' if i<repair else 'reserved_leaf_repair_quarantined_in_scratch')
    for n,f in enumerate(c['3']):
        assert f['code']=='AUTH_PROTECTED' and f['applicability']=='would be refused if agent-made; authorship not established' and i>=repair
        add(row,'3',n,f,'v','protected_touch_authorship_unestablished')
    for n,f in enumerate(c['1']['credential_template']):
        assert f['code']=='credential_values' and f['applicability']=='if policy enabled it; supplemental template, no current-policy verdict'
        add(row,'1.credential_template',n,f,'v','unmet_policy_enablement')
    for field,change in row['consequence_changes'].items():
        for kind in ('added','removed','changed'):
            for n,item in enumerate(change[kind]):
                assert i==repair and field in ('obligations','quarantine') and kind=='added'
                v=item['value']
                if field=='obligations':
                    assert v['kind']=='INTAKE' and v['detail']=='quarantined delta' and v['about'][0] in ('ssds.manifest','ssds.policy')
                else:
                    assert v[0] in ('ssds.manifest','ssds.policy')
                add(row,f'consequences.{field}.{kind}',n,item,'iii','reserved_leaf_repair_absorbed_as_foreign_change')
result={'schema':1,'status':'PRELIMINARY_NOT_FROZEN_ACCEPTANCE','asserter':'AI implementing agent, Claude family',
 'governing_protocol':'7.2.1','authority':'Phase F F123/F124; class reasons are preliminary agent interpretations, not other-family acceptance',
 'candidate':d['candidate'],'source_report':p.name,'source_sha256':sha,'completed_deltas':301,'expected_deltas':301,
 'reasons':{
  'reserved_leaf_genesis_deviation':{'class':'iii','meaning':'Before the reserved-leaf repair commit 11ec88e4 the bounded historical genesis exempts only ssds.manifest and ssds.policy; their absence on each evaluated tree is the declared genesis deviation.'},
  'reserved_leaf_repair_quarantined_in_scratch':{'class':'iii','meaning':'From 11ec88e4 the trees declare the leaves, but the scratch genesis has no counterpart of the human ABSORB adoption that SD-69 makes the exception and that the real ledger admitted at position 2; the declaration delta stays quarantined, so effective structure keeps the genesis deviation. Scratch-genesis rule, not a document-control or SSDS defect.'},
  'protected_touch_authorship_unestablished':{'class':'v','meaning':'11ec88e4 creates .ssds/policy.toml, the genesis-named policy path that protected_surfaces always protects (the committed policy itself lists no surfaces; the manifest is not protected). Row 288 touches it by path and by authoring the ssds.policy unit. While ssds.policy stays quarantined in scratch, the file belongs to ssds.unclassified, so protected_touched flags every later write-set touch of that unit (unit granularity), although rows 289-300 never change the policy file. In any structure the Manual accepts ssds.policy is its own leaf and unit- and path-level detection coincide; this is a conservative consequence of the class iii deviation, not an SSDS defect. The agent-authorship predicate is not established; no current-policy refusal or defect follows.'},
  'unmet_policy_enablement':{'class':'v','meaning':'Supplemental credential-values template if policy enabled it; enablement not established. No credential value or actual defect is inferred; matched lines/values are neither retained nor reconstructed.'},
  'reserved_leaf_repair_absorbed_as_foreign_change':{'class':'iii','meaning':'Absorbing 11ec88e4 quarantines its eight reserved-leaf declaration keys and derives their INTAKE obligations (Manual 8.6, 18.2, 18.5): absorption never changes the effective structure and Admission never adopts on its own. The real ledger received the same quarantine and then the human ABSORB adoption at position 2 (SD-69); the scratch genesis has no counterpart. Consequence of the scratch genesis rule, not a refusal or defect.'}},
 'summary':dict(sorted(collections.Counter(r['class'] for r in rows).items())),
 'by_reason':dict(sorted(collections.Counter(r['reason'] for r in rows).items())),'observations':rows,
 'limits':['preliminary run on a non-frozen candidate: R-PROVENANCE-C7 keeps step 2 reopened, so source may still change',
           'no class i or iv defect established by this preliminary classification',
           'checks 1/3 are conditional, check 4 vacuous; record-dependent effects require the later authorized campaign',
           'consequences belong to the scratch ledger, which lacks the real ledger human adoption records',
           'frozen 11b, its classification and independent other-family review remain required']}
out=q/'PHASE-F-DIFFERENCE-STUDY-PRELIMINARY-6ae91c3d-CLASSIFICATION.json'
assert not out.exists();out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'observations':len(rows),'classes':result['summary'],'by_reason':result['by_reason'],'classification_sha256':hashlib.sha256(out.read_bytes()).hexdigest()},indent=2))
```

</details>

## Frozen 11b: `8cf829c3` — COMPLETE (2026-11-01)

**The window.** One host window ran in the stakeholder's terminal, with no other tool running; the author only
read the terminal. It ran `PHASE-F-11B-FROZEN-WINDOW.py` (sha256 `14a5c116…c937`, committed in `1dd18468`) around
the frozen harness `orchestrator/scripts/difference_study.py`.
- Candidate `8cf829c34020ebffb5ad50ad7ba5b03343c005ce` (SD-94), on a new scratch home
  `/tmp/claude-1000/ssds-phase-f-frozen-11b-8cf829c3/home`.
- Runtime `/tmp/claude-1000/ssds-runtime-20261030/bin/python -I -B`, rebuilt after the host reboot (see the 10d
  evidence for `ssdp-shadow-3`; CPython 3.12.16, typer 0.27.3).
- Preconditions held: `orchestrator/` equals `8cf829c3` and is clean, there is no bytecode under `src`, and no
  linked worktree is registered.
- The result was **PASS**: harness exit 0 after about 1,650 s (budget 7,200 s), the window's own compare 0 (the
  repository unchanged), and the report's own final boundary `PASSED` (`unchanged: true`). The status is
  **COMPLETE**, 308 of 308.
- The window record is `PHASE-F-DIFFERENCE-STUDY-FROZEN-8cf829c3-WINDOW.json`.

**The population.** There are 1,049 first-parent commits, matching `git rev-list --first-parent --count`. They are
740 exclusions, the initialization `09f35057` and **308 evaluated deltas**: 66 up to and including the real baseline
and 242 after it. The parent chain is contiguous from `09f35057` to `8cf829c3`. Findings by code:
`STRUCT_RESERVED_LEAF` 614, `credential_values` 163, `AUTH_PROTECTED` 21. Only row `11ec88e4` has consequence
changes. The retained report is `PHASE-F-DIFFERENCE-STUDY-FROZEN-8cf829c3.json`, sha256
`8ec603a8a2005377088006f500f2ee76f27ee820a7b942964e11d8c9f73a2ee1`.

**Against the preliminary 6ae91c3d report:**
- The initialization and the exclusions are identical.
- The preliminary's 301 rows are a prefix of the frozen report's rows, in the same order.
- 288 of those rows are byte-identical. The other 13 (`11ec88e4` and the 12 rows after it) differ only in one check-3
  detail text: "… is a protected surface" became "… contains a protected surface" (`writescope.py`). That is the
  presentation note the preliminary classification review raised, taken up in the frozen source. Codes, owners,
  applicability and every other field are unchanged.
- The 7 new rows (`da93dd07`, `e4a2590d`, `b5f811d5`, `35f20c56`, `3ea6d029`, `46dbcc4b`, `8cf829c3`) each carry the
  two reserved-leaf findings, which stay quarantined in scratch, and one protected touch of `ssds.unclassified`.
  Five of them carry nine credential-template hits in all (none in `e4a2590d` or `8cf829c3`). None has a
  consequence change.

**Classification (F124).** The file is `PHASE-F-DIFFERENCE-STUDY-FROZEN-8cf829c3-CLASSIFICATION.json` (sha256
`aea9f477f965530886f79f1a0d99ee7bc3c8876ae1d1e4288c0717440bf9d901`), status
`FROZEN_PENDING_OTHER_FAMILY_REVIEW`. It was generated by `PHASE-F-DIFFERENCE-STUDY-CLASSIFY.py` (sha256
`e37a1d14…be85` as first committed in `d059bbb0`). It states the preliminary classification's rules as code:
- the same observation identity (sha256 of the canonical `{source, finding}`);
- the same five reason keys and classes. Three reason texts were updated to name commits instead of row numbers
  and `ssdp-shadow-2` instead of "the real ledger".
- any observation outside them stops the run unclassified.

Run on the preliminary report, it reproduces all 784 preliminary observations exactly (identity, class, reason,
source, code). On the frozen report it gives **814 observations: 630 (iii), 184 (v), no (i) or (iv)**:

| reason | class | count |
|---|---|---|
| reserved-leaf genesis deviation (the rows before `11ec88e4`, which itself has no check-2 finding) | iii | 576 |
| reserved-leaf repair quarantined in scratch (after `11ec88e4`) | iii | 38 |
| repair absorbed as a foreign change (`11ec88e4`: 8 quarantine keys, 8 INTAKE obligations) | iii | 16 |
| protected touch, authorship unestablished | v | 21 |
| credential template, policy enablement unestablished | v | 163 |

No matched line or credential value was read, retained or reconstructed.

**Same-family check of the run and classification: PASS**, no blockers, no Serious Challenge. It recomputed
independently, read-only:
- the population, from Git: 740 exclusions (690 without a unit manifest, then 50 lacking `ssds.unclassified` from
  `db0e9f42`), the earliest admissible `G`, the contiguous parents and the 66/242 split;
- every comparison claim above;
- all 814 observations, both with the classifier and with an independent rebuild under stricter guards.

It confirmed that no row after `11ec88e4` touches `.ssds/`, and that the 19 later protected touches are the
unit-level consequence of the class (iii) deviation, not class (iv). It confirmed the window's preconditions, the
digests and the byte identity of the committed copies.

Its notes are taken up:
- the classifier's fail-closed guards are restored and strengthened (sha256 now `911cd375…f2ef`):
  - check keys and the request scan;
  - exactly the two exempted leaves per row, with an empty check 2 at `11ec88e4`;
  - protected touches only from `11ec88e4` on, with their owners;
  - quarantine keys of the two reserved leaves.

  It reproduces both the 784 preliminary and the 814 frozen observations exactly. Three mutations stop it
  unclassified: an unknown check-2 code, a protected touch before `11ec88e4`, and an integrity consequence.
- Two wording points in this section are corrected.

**Limits:**
- Checks 1 and 3 are conditional, and check 4 is vacuous. Record-dependent effects need the authorized campaign.
- The consequences are the scratch ledger's, whose genesis lacks the human reserved-leaf adoption.
- Q-F1 (b) on the real ledger comes from 10d on `ssdp-shadow-3`, whose own genesis declares the leaves.
- The rows share the harness and production owners with the program they study, so a common-mode limitation
  remains.
- The other-family review of this classification at the frozen candidate (SD-95) is required and not yet done.

### Other-family review of the frozen candidate (SD-95): NO-PASS on A and B, PASS on C

The record is `PHASE-F-FROZEN-REVIEW-SSDS-8.0-8CF829C3-DIFFERENT-FAMILY.md` (Codex family, 2026-11-01, from the
handoff at `26f34516`). For this study (part B) it independently reproduced:
- the population, from Git and the real `baseline_structure`;
- every comparison claim;
- all 814 identities, reasons and classes.

It found nothing to convert to class (i) or (iv). Its blocker **FR-B1** concerns the classifier, not the run or the
observations. The consequence rule checked only the kind, detail and first `about` element of an intake obligation
and the unit of a quarantine key. So a discharged obligation, an unknown declaration field or an unrelated key
value would still have been classed (iii).

**FR-B1 repaired** (classifier sha256 `ca490718…1144`). The rule now accepts consequence changes only at
`11ec88e4`, and only in their exact shape:
- the eight declaration keys `{ssds.manifest, ssds.policy} x {kind, role, scope, subject}` quarantined, each once,
  each with its value equal to its key;
- one `OPEN` INTAKE "quarantined delta" obligation per key, whose id is its key;
- no other group or change.

Anything else stops the run unclassified. The repaired classifier reproduces the 784 preliminary and 814 frozen
observations exactly. Seven mutations stop it unclassified: the reviewer's three counterexamples, a missing
obligation, an unknown check-2 code, an early protected touch and an integrity change.

Part A's FR-A1, a source defect (`NONCE_RE` with `match`), is routed in the Phase F plan. A source repair changes
the frozen candidate, so 11b is re-run at the repaired candidate and this classification is re-made there. The
present run and classification stay recorded as the run at `8cf829c3`.
