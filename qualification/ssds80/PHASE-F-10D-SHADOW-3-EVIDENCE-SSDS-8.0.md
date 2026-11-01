Governing SSDP version: 7.2.1.

# SSDS 8 Phase F — step 10d on `ssdp-shadow-3`: evidence

```text
STATUS: tools repaired after their review (plan revision 71); rehearsal 2 from a fresh home is next. No real
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
- `PASS`: every precondition holds, every command exits as expected, every output check of F126's expected outcome holds and the compare passes;
- `FAILED`: the compare failed;
- `INCOMPLETE`: the compare passed but a command exited otherwise or an output check failed (a refusal in a passing window is one);
- `NOT STARTED`: a precondition failed or the snapshot was refused.

| file | role | sha256 |
|---|---|---|
| `PHASE-F-10D-SHADOW-3-RUN.py` | F126's one entry point: interpreter, mode, home and ledger checks before any SSDS import; `cli` and `script` forms; module-origin assertion | `a3f05b3ff88a0a49d9894db41312e14d5c83d7e69b272d024a79bb0d682ef257` |
| `PHASE-F-10D-SHADOW-3-HELPER.py` | the fixed helper: `state` (W2, W6, READ), `records` and `check` (W4a, W5a, W7a), `operator-state` (W3), `baseline` (W7b), `verify-decide` (W7c), `candidate` (W8) | `6cb4e8a6af8114760f6c80e48bc1cf35a83d37da8b028d5b7025bd00cd9bc6a0` |
| `PHASE-F-10D-SHADOW-3-WINDOW.py` | the window runner: preconditions, snapshot, the fixed commands with their output checks, compare | `ec59ce6b38fd5e633cb2cc0b335e9929031b2f0a0cc7a714e5f1065b98aadf32` |
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

## Tool review (plan revision 71)

The same-family review of `16712232` gave **NO-PASS**: two blockers, no Serious Challenge. Both are repaired.
- **B1, the narrative check.** `records --kind finding` now requires the narrative blob to show the ledger id and its
  position-1 head, which is what W2's `inspect` prints. A rehearsal narrative is refused on any other ledger: this
  was checked on the dev ledger. `check` now shows each record's target, outcome, reason, fields, refs, basis and
  `recorded_at` for the review, since `summary.txt` omits them.
- **B2, operator state in W3.** W3 now runs between two `operator-state` fingerprints of `state/<ledger>/`, read
  through the home's checked primitive; a signature, which is the human's public input, is read directly, as
  `read_prepared` does. W3 requires no change and `would_issue: []`.

Notes taken up:
- Output checks per window, in the runner's `steps`:
  - W1: `absorbed` at 1;
  - W2: `QUALIFIED`, a current assertion, no provisional entry or critical finding, and helper `problems: []`;
  - W4b and W5b: `ACCEPT`, appended, nothing refused;
  - W6: the second serve absorbs nothing, and at most one absorption follows the last admission;
  - W7b: the exact F1 refusal;
  - W8: nothing appended;
  - W9: the live ledger is `QUALIFIED` with no violation, and in the real run each retired ledger's entries, head,
    last digest, qualification, halt and readable prefix equal the committed after-step-C reports.
- The compare and the window record run even when a command crashes or the runner is interrupted.
- The helper refuses abbreviated options, and the wrapper gives PREFLIGHT-A exactly `--tree`, `--out` and
  `--ledgers`.
- The `.ssds/` and `orchestrator/` move check runs in every window.
- Each window records the tools' digests and refuses a PREFLIGHT-A that is not F126's `f2fecb32…a969`.
- A read-only `READ` window was added.
- The wrapper reports an uncaught exception and keeps the origin check.

Two notes are worded, not coded. The rehearsal rehearses the same construction code; the record bytes differ
(`recorded_at`, the narrative, the genesis's `ruleset` and `governs`). W6's third process is the helper's
`state`, which supports "the entries are compared".

The first rehearsal below ran on the tools as committed in `0914017a`, and it is superseded. Its files are kept in
`/tmp/claude-1000/ssds-10d-rehearsal/rehearsal-1/`. The rehearsal is re-run from a fresh home with the repaired
tools (rehearsal 2).

## Rehearsal 1 (`--mode rehearsal`, tools of `0914017a`; superseded)

Scratch home `/tmp/claude-1000/ssds-10d-rehearsal/home` (now under `rehearsal-1/`), ledger `ssdp-shadow-3-rehearsal`, throwaway key
`/tmp/claude-1000/ssds-10d-rehearsal/key/throwaway` (the author's, scratch only). Window records are in
`/tmp/claude-1000/ssds-10d-rehearsal/rehearsal-1/windows/windows.jsonl`, and each command's full output is in
`<window>-<label>.log` beside it. Every window ran in the stakeholder's terminal with no other tool running.
Signing happened between windows.

| window | result | what it showed |
|---|---|---|
| G1 | PASS | scratch genesis prepared at the frozen baseline, digest `sha256:70f06595…fcbc` |
| G2 | PASS | admitted: entry `sha256:72c5bcf1…d39f`, `QUALIFIED` at 0 with a current assertion |
| W1 | PASS | the precondition found nothing under `.ssds/` or `orchestrator/` moved since `8cf829c3`; head `0914017a` absorbed at position 1 |
| W2 | PASS | `status`: `QUALIFIED`, current assertion, no provisional entry, no critical finding, no obligation. Helper `state`: the reserved leaves `MANIFEST`, `POLICY` and `UNCLASSIFIED`; empty quarantine; policy digest unchanged; policy object held (11 bytes, digest matches); policy availability `null` (no AVAILABILITY yet, as observed) |
| W3 | PASS | `would_issue: []`, nothing issued, no run ref |
| W4a | PASS | FINDING built at position 1. Narrative: blob `77ac4936…5533` of `a68c725d`, this file, 8,600 bytes, content `sha256:cb920603…8519`. Prepared as request `sha256:a477ab9c…02dd`, record `sha256:916b9043…214c`. Admission's step-1 checks: no request or record problem, provenance `null`, the message matches, no signature yet |
| W4b | PASS | absorbed `a68c725d` at 2, then `ACCEPT` at 3 |
| W5a | PASS | AVAILABILITY of `sha256:da93db77…3ea1`, `AVAILABLE`. Prepared as request `sha256:179c8d6a…8468`, record `sha256:803dc33c…a077`. Checks clean |
| W5b | PASS | `ACCEPT` at 4, with no absorption (head unmoved) |
| W6 | PASS | two `admission serve` runs: `absorbed: false` at 4 both times. Chain: 0 genesis, 1 and 2 absorptions, 3 FINDING, 4 AVAILABILITY; no fence after the records-only admissions. Policy availability `AVAILABLE`; no problems |
| W7a | PASS | ACKNOWLEDGE of the derived `HUMAN_ATTENTION` obligation `sha256:62c76f80…b765` (holder `HUMAN`), basis the FINDING. Prepared as request `sha256:bf0ff55d…07cb2`. Checks clean |
| W7b | PASS | baseline 5 entries, obligation `OPEN`, no human decision. `decide --admit` refused at entry, "a HUMAN_DECISION record: its checks belong to a later phase (F1)", exit 1 as expected |
| W7c | PASS | signature verified independently against the registered key. Nothing appended (5 entries, same last digest). Obligation still `OPEN` and `HUMAN`-held. One new `boundary.jsonl` line, under the signed request's identity |
| W8 | PASS | candidate refused at entry ("the real shadow ledger observes and never publishes (F1)"), nothing appended, one `boundary.jsonl` line |
| W9 | PASS | the `3ea6d029` extract matched by content (133 files, nothing extra). C7 read: 5 entries, `QUALIFIED`, no record violations, 83 modules all from the repository's `src`. Pre-C7 read: the same, 83 modules all from the extract |

Every window's preconditions held: `orchestrator/` equals `8cf829c3` and is clean, no bytecode is present (only
`ssds.egg-info/` is ignored under `src`), and no linked worktree is registered. Every compare reported the
repository unchanged. The rehearsal proves the path, not the real admission; its throwaway signatures are no
evidence of the stakeholder's approval.

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
