# Phase F difference study — preliminary diagnostics; frozen 11b unexecuted

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
