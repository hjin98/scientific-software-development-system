Governing SSDP version: 7.2.1.

# SSDS 8 Phase F — retirement of `ssdp-shadow-2` and genesis of `ssdp-shadow-3`: runbook

```text
STATUS: steps A and B EXECUTED 2026-10-31 (execution record below); C and D not executed. Nothing in this
        runbook is signed or appended by the author.
AUTHORITY: SD-92 (item 79): retire ssdp-shadow-2 and start a fresh shadow genesis after C7 enforcement is
           qualified; SD-96 (item 80): ssdp-shadow-3 is approved with a new human key, so SD-89 (one human key
           per live ledger) holds throughout. Plan readings F44-F45 (retirement), F125 (C7), Manual §19.9, §24.2.
SHADOW: no SSDS authority over any subject; no cutover; nothing carried between the ledgers.
```

## Why this order

1. **The successor exists first.** A `LINEAGE_RETIREMENT` names its successor's ledger id and genesis entry digest,
   read from the successor's own chain (F44), so `ssdp-shadow-3` is created before `ssdp-shadow-2` is retired.
2. **Two keys, never one key on two live ledgers.** `ssdp-shadow-3` registers a new key (SD-96). The SD-57 key
   approves only the old ledger's retirement. Between steps B and C both ledgers are live, but no key is
   registered on both, so no signed request can be replayed across them (Q-F29, SD-89).
3. **The retirement runs on the pre-C7 program.** The C7 reader (F125) puts `ssdp-shadow-2` into
   `INTEGRITY_HALT` at position 6, and Admission appends nothing under a halt. Step C therefore runs the pre-C7
   commit `3ea6d0294916c68852433b69e9fb1ffee2073a22` (the last commit before F125's source), extracted with
   `git archive` into a scratch directory (the repository's `.git` is untouched), under the rebuilt Python 3.12
   runtime, never the script's `env python3`. The run asserts that `ssds` loads from the extract (the script puts its
   own tree first on `sys.path`, ahead of the runtime's editable entry) and passes `--repository` explicitly.
   Every other step runs the current program.

## Steps

Each command runs in the stakeholder's terminal. Steps A3, B2 and C2 are the human's; the private keys never
leave `~/.ssh`. Every program step that reads or writes the SSDS home runs in one boundary-checked host window
with no other tool running (SD-93's clean-window discipline).

**A. Preflight (read-only).**
1. The pre-C7 reader reads the whole of `ssdp-shadow-2` (readable through its head); the C7 `record_violations` is
   then run over every record at every position, and must find violations at position 6 alone. The C7 reader
   itself stops at its first halt, which must be 6. Nothing writes.
2. Both readers read the retired `ssdp-shadow`, to learn whether it still reads `RETIRED` under the candidate or
   now halts (its records predate the provenance grammar). Either result is disclosed, not a stop: that ledger is
   already retired and nothing is appended to it.
3. Record every report and each chain's head, entry count and last digest. A result other than the expected one
   stops the runbook and goes to the stakeholder.

**B. Genesis of `ssdp-shadow-3`.**
1. The stakeholder creates the new key: `ssh-keygen -t ed25519 -f ~/.ssh/ssds-genesis-3 -C ssds-genesis-3`.
2. `prepare`: `orchestrator/scripts/shadow_genesis.py --ledger-id ssdp-shadow-3 prepare --public-key ~/.ssh/ssds-genesis-3.pub --baseline <the frozen candidate commit (SD-94)>`.
   It validates the genesis in the home's isolated workspace and prints the report and digest; nothing is published.
   The author reviews the report (units, reserved leaves declared, `ssds.unclassified`, policy object) before the
   signature is requested.
3. The stakeholder signs: `ssh-keygen -Y sign -f ~/.ssh/ssds-genesis-3 -n ssds ~/.ssds/genesis/ssdp-shadow-3/approval-message.txt`.
4. `admit`: `orchestrator/scripts/shadow_genesis.py --ledger-id ssdp-shadow-3 admit --signature ~/.ssds/genesis/ssdp-shadow-3/approval-message.txt.sig`.

**C. Retirement of `ssdp-shadow-2` (pre-C7 program).**
1. `prepare`, from the extracted pre-C7 tree: `<pre-C7>/orchestrator/scripts/retire_shadow.py --ledger-id ssdp-shadow-2 --repository <repository> prepare --public-key ~/.ssh/ssds-genesis.pub --successor ssdp-shadow-3`.
   It builds the `LINEAGE_RETIREMENT` for the next position and prints the message; nothing is appended.
2. The stakeholder signs with the SD-57 key: `ssh-keygen -Y sign -f ~/.ssh/ssds-genesis -n ssds <retirement message>`.
3. `admit`: `<pre-C7>/orchestrator/scripts/retire_shadow.py --ledger-id ssdp-shadow-2 --repository <repository> admit --signature <retirement message>.sig`.
   The ledger then reads `RETIRED` under the pre-C7 program and appends nothing more.

**D. After.**
1. The current (C7) program reads `ssdp-shadow-2` as `INTEGRITY_HALT` at 6 (the disclosed historical effect of the
   C7 finding; its entries, including the retirement, stay as bytes and evidence) and `ssdp-shadow-3` as qualified.
2. 10d is replanned on `ssdp-shadow-3` (SD-93): its genesis already declares the reserved leaves, so the repair
   append is moot; the signed append that closes 10d is the records exercise, in a clean window. That replanning
   is a plan revision with its own review, before any request is prepared.

## Execution record

**A, 2026-10-31: as expected.** One host window in the stakeholder's terminal, no other tool running: boundary
snapshot of the product repository, the pre-C7 read, the C7 read, then the compare. The reader is
`PHASE-F-RETIREMENT-2-PREFLIGHT-A.py` (sha256 `2336c03c…9ba`). For a given program tree, it reads each chain with that
tree's `read_raw` and `verify_chain`; it takes the qualification from `Admission.qualification`, bound without
`__post_init__` so no host key is loaded or created; and it runs that tree's `record_violations` over every record
at every position. It asserts that every `ssds` module loads from the named tree. The full reports are in
`PHASE-F-RETIREMENT-2-PREFLIGHT-A-PRE-C7-3ea6d029.json` (sha256 `362e01cd…1d3`) and
`PHASE-F-RETIREMENT-2-PREFLIGHT-A-C7-46dbcc4b.json` (sha256 `687e2032…7db`).

| ledger | head commit | entries | last entry digest | pre-C7 (`3ea6d029`) | C7 (`46dbcc4b`) |
|---|---|---|---|---|---|
| `ssdp-shadow-2` | `085cd6b4de04acbf2727844ad5c4484643dacafb` | 10 | `sha256:412391b0…1a30` | `QUALIFIED`, readable through 9; sweep finds nothing | `INTEGRITY_HALT` at 6, readable through 5; sweep finds `field provenance outside its grammar` at 6 alone |
| `ssdp-shadow` | `5b9e3f245f5fbf5b4bbc77cd18424b751307ead9` | 2 | `sha256:ef50e86c…c236` | `RETIRED` | `RETIRED`; the candidate does not halt it |

The compare reported the product repository unchanged since the snapshot. The first attempt stopped at the
snapshot, before any ledger was read. The system Git is 2.34.1, which has no `worktree list -z`, and a clean app
worktree (`.claude/worktrees/friendly-euler-4610a1`, whose commit `401d66bb` stays on branch
`claude/friendly-euler-4610a1`) was registered. With the stakeholder's approval it was removed and pruned; the
sensor was not changed. Any linked worktree registered later will stop a window the same way until Git is 2.36 or
newer.

**B, 2026-10-31: `ssdp-shadow-3` admitted, `QUALIFIED` at 0.** The candidate was frozen at
`8cf829c34020ebffb5ad50ad7ba5b03343c005ce` first (plan revision 67). The stakeholder created `ssds-genesis-3`.
`prepare` and `admit` each ran in their own boundary window, and each compare reported the product repository
unchanged.
- `prepare` (current program, `--baseline` the frozen candidate): valid, no findings or problems; genesis digest
  `sha256:3fbf6a91…57a6`, which the program's `genesis_digest` reproduces from the workspace proposal and which binds
  the approval message.
- Author review against `ssdp-shadow-2`'s genesis:
  - The units are the same, plus the reserved leaves `ssds.manifest` and `ssds.policy` (now declared at genesis,
    so SD-69's repair is moot). `ssds.unclassified` is declared.
  - The ruleset (analyzer and policy digests), the policy object (`schema = 1`), the modes (LEGACY 7.2.1, which
    matches `PROTOCOL-RELEASE-STATE.yaml`, and `*` UNGOVERNED) and the witness model are unchanged.
  - The human key is `human:SHA256:gLJS5DKM…xxI`, distinct from the SD-57 key `Xar4qv2h…6lw` (SD-89 holds). The
    Admission host key is new (`ed25519:11992330…`).
  - Provenance is null.
- The stakeholder signed with `ssds-genesis-3`. `admit`: entry commit `9d404721a17748f8cb1ec14c5e20b2cedc33745c`,
  entry digest `sha256:13063316a050b7423cfd77ed9eebb205105eccca28be848f6a3e5acc378020e4`.
- Qualification is `QUALIFIED` at 0, with a current assertion and no findings, critical items or obligations. The
  C7 reader, read back independently, finds 1 entry, no halt and no record violations; the approval key is the new
  human key.

## What stays recorded

The old experiment, its C7 finding, its FAILED original append and every request and signature stay in their
evidence records. Nothing here is a retroactive pass, a waiver, a rewrite or an import.
