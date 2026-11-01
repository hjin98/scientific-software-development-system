Governing SSDP version: 7.2.1.

# SSDS 8 Phase F — step 10d on `ssdp-shadow-3`: evidence

```text
STATUS: TOOLS COMMITTED; dev check in scratch done; the rehearsal (G1-W9 in --mode rehearsal) is next. No real
        window has run and nothing is prepared on ssdp-shadow-3.
AUTHORITY: plan reading F126 (revision 69, review PASS); SD-93 (10d closes only on a later clean signed append);
           SD-97 (item 81, Q-F30 (a): the FINDING and the policy object's AVAILABILITY).
SHADOW: no SSDS authority over any subject; nothing is carried from ssdp-shadow-2 (F44).
CANONICAL: this file owns 10d on ssdp-shadow-3: each window's preconditions, commands, output and compare, and the
           pending signatures below. ssdp-shadow-2's 10d history stays in PHASE-F-10D-SHADOW-LEDGER-EVIDENCE-SSDS-8.0.md.
```

## Tools

Each window runs `PHASE-F-10D-SHADOW-3-WINDOW.py` in the stakeholder's terminal, under
`/tmp/claude-1000/ssds-runtime-20261030/bin/python -I -B`. The runner checks F126's preconditions, takes the
boundary snapshot, runs the window's fixed commands and then compares. Its commands are fixed per window and
listed in its `steps`. It imports no SSDS module itself: every process that runs the program is started through
the wrapper. It writes only under the mode's window directory, which is
`/tmp/claude-1000/ssds-10d-rehearsal/windows/` in the rehearsal and `/tmp/claude-1000/ssds-10d-shadow-3/windows/`
for the real run. A repeated window takes `--attempt n`, so no window's files are overwritten. The runner sets
`SSDS_HOME` to `/tmp/claude-1000/ssds-10d-rehearsal/home` in the rehearsal and removes it for the real run, and it
drops every `PYTHON*` variable. Each step's outcome is one of:
- `PASS`: every precondition holds, every command exits as expected and the compare passes;
- `FAILED`: the compare failed;
- `INCOMPLETE`: the compare passed but a command exited otherwise;
- `NOT STARTED`: a precondition failed or the snapshot was refused.

| file | role | sha256 |
|---|---|---|
| `PHASE-F-10D-SHADOW-3-RUN.py` | F126's one entry point: interpreter, mode, home and ledger checks before any SSDS import; `cli` and `script` forms; module-origin assertion | `b0f90f26f44b7d68870960b971f36dd7a71697cbe5122673e1e168b0f351ccdb` |
| `PHASE-F-10D-SHADOW-3-HELPER.py` | the fixed helper: `state` (W2, W6), `records` and `check` (W4a, W5a, W7a), `baseline` (W7b), `verify-decide` (W7c), `candidate` (W8) | `6388c6a87ee5251186de9495745c0b7bebf3e12d3c9b94941db5dbf630361168` |
| `PHASE-F-10D-SHADOW-3-WINDOW.py` | the window runner: preconditions, snapshot, the fixed commands, compare | `7e0ba41d17f43acc0369f95ae3328ebcb9b0ae224c3b92e13aa425cf6b0bb9e2` |
| `PHASE-F-RETIREMENT-2-PREFLIGHT-A.py` | W9's read-back (unchanged) | `f2fecb328d47ad676f83a119887083c637330cf3489e90aa9aa8323fc582a969` |
| `orchestrator/scripts/shadow_boundary.py` | the boundary sensor (frozen source) | `79770bc29f27fe1ba773b7c98270b32c7e82f23cd04b334ae00222a33a757722` |
| `orchestrator/scripts/shadow_genesis.py` | the rehearsal's scratch genesis only (frozen source; refused in `--mode real`) | `50254ac27051f63fbef9aaaab1581e210191dd7135f3feec56736b573208da01` |

**What the wrapper refuses.** Each of these exits 2 before any SSDS import:
- an interpreter other than the pinned runtime, or a run without `-I -B`;
- in the rehearsal, `SSDS_HOME` unset, or resolving outside `/tmp/claude-1000/ssds-10d-rehearsal/` (including the
  root itself, a `..` escape and a symbolic link into `~/.ssds`);
- in the real run, any home but `~/.ssds`, compared after `Path.resolve()` with the account's home from `pwd`;
- a mode with the other mode's ledger;
- a process given another ledger, or the ledger twice, or none;
- `shadow_genesis.py` in the real run, and any script that is not one of the four above;
- `--tree` anywhere but W9's pre-C7 read, or naming any directory but the `3ea6d029` extract;
- a read-back that names other ledgers or another tree.

After the import, the wrapper also requires `ssds_home()` to resolve to the home it checked.

**Dev check (2026-11-01, sandbox, outside any window; not evidence for the rehearsal).** The checks ran from the
author's sandbox, so they are not boundary-checked:
- Each refusal above was exercised, and each exited before any home was created.
- The whole path then ran on a separate scratch home, `/tmp/claude-1000/ssds-10d-rehearsal/dev-home`, with a
  scratch genesis `ssdp-shadow-3-rehearsal` and a throwaway key in `dev-key/`. The run covered genesis, observe,
  `status`, `inspect` and `state`. It then ran the records, prepare, check, sign and admit sequence: the FINDING
  was `ACCEPT` at 2, and a resubmission gave `appended: false`; the AVAILABILITY was `ACCEPT` at 3, after which the
  policy object read `AVAILABLE`. After that came two `admission serve` runs, neither absorbing anything, and an
  ACKNOWLEDGE of the derived `HUMAN_ATTENTION` obligation. That ACKNOWLEDGE was prepared and signed, and its admit
  was refused at entry under F1, with nothing appended and the obligation still `OPEN`. The signature was verified
  independently, and the refusal logged once under the signed request's id. Last came the candidate refusal and
  the read-back on both programs: 4 entries, `QUALIFIED`, no record violations.
- It found and fixed four defects in the tools before the commit:
  - a record must be schema-checked with its computed identity;
  - `boundary.jsonl` logs the signed request's identity, not the prepared one;
  - GNU `tar -d` compares owners, so the pre-C7 extract is compared by content instead;
  - each window's records and baseline now carry the window's name.
- The `3ea6d029` extract's 133 source files match the commit. Its bytecode caches, written by the `-I`-only runs of
  steps A-C, were deleted, and so were those under the repository's `orchestrator/src`. That leaves only
  `ssds.egg-info/` ignored under `src`.

## Rehearsal (`--mode rehearsal`)

Scratch home `/tmp/claude-1000/ssds-10d-rehearsal/home`, ledger `ssdp-shadow-3-rehearsal`, throwaway key
`/tmp/claude-1000/ssds-10d-rehearsal/key/throwaway` (the author's, scratch only). Window records are in
`/tmp/claude-1000/ssds-10d-rehearsal/windows/windows.jsonl`, and each command's full output is in
`<window>-<label>.log` beside it. Every window ran in the stakeholder's terminal with no other tool running.
Signing happened between windows.

| window | result | what it showed |
|---|---|---|
| G1 | PASS | scratch genesis prepared at the frozen baseline, digest `sha256:70f06595…fcbc` |
| G2 | PASS | admitted: entry `sha256:72c5bcf1…d39f`, `QUALIFIED` at 0 with a current assertion |
| W1 | PASS | the precondition found nothing under `.ssds/` or `orchestrator/` moved since `8cf829c3`; head `0914017a` absorbed at position 1 |
| W2 | PASS | `status`: `QUALIFIED`, current assertion, no provisional entry, no critical finding, no obligation. Helper `state`: the reserved leaves `MANIFEST`, `POLICY` and `UNCLASSIFIED`; empty quarantine; policy digest unchanged; policy object held (11 bytes, digest matches); policy availability `null` (no AVAILABILITY yet, as observed) |
| W3 | PASS | `would_issue: []`, nothing issued, no run ref |

### Rehearsal W2: `inspect` output (the rehearsal FINDING's narrative home)

`ssds inspect --ledger ssdp-shadow-3-rehearsal` at position 1 printed, apart from the wrapper's lines:

```json
{
  "answer": {
    "digest": [],
    "entries": [],
    "head": {
      "digest": "sha256:e1d4bb03316ec4862ef945e2584a451c1e6c78b8fc7252165fa29d8a72bfd36f",
      "label": "QUALIFIED",
      "position": 1,
      "qualification": "QUALIFIED"
    }
  },
  "head": {
    "digest": "sha256:e1d4bb03316ec4862ef945e2584a451c1e6c78b8fc7252165fa29d8a72bfd36f",
    "label": "QUALIFIED",
    "position": 1,
    "qualification": "QUALIFIED"
  },
  "query": "inspect"
}
```

The finding: `inspect` names the head and nothing of the effective structure. It shows no units, kinds, reserved
leaves, policy object or quarantine, which the derivation holds (the helper's `state` reads them through the same
owner). That is an inspectability gap on `orchestrator.program` (the command) and on `ssds.manifest` and
`ssds.policy` (what it leaves undisplayed). It is `MATERIAL`, because a human cannot confirm the effective
structure from the inspection surface, and non-blocking. In the real run this section is replaced by
`ssdp-shadow-3`'s own W2 output.

## Real run (`--mode real`, `ssdp-shadow-3`)

Not yet run.

## Pending signatures

None. Each real signature is the stakeholder's, with `ssds-genesis-3`, between windows (W4, W5, W7).
