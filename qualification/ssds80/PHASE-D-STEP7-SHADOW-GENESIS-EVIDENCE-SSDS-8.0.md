# SSDS 8 Phase D step 7 — shadow genesis of this repository: evidence record

```text
GOVERNING SSDP: 7.2.1 (identities from PROTOCOL-RELEASE-STATE.yaml)
PLAN: workplans/active/SSDS-8.0-G2-PHASE-D-PLAN.md §3 step 7 (Manual §19.9 Case B)
SHADOW: no SSDS authority over any subject; every subject LEGACY(7.2.1) or UNGOVERNED; no cutover
HUMAN GATE: the stakeholder's, taken 2026-10-20T02:52Z UTC in the stakeholder's own terminal
PROGRAM: ssds at 9bf199120f7f289f10994189d1bd718690653dfc (implementation candidate db0e9f42 plus the
         Review handoff and plan state lines), run under Python 3.13
```

This records what was run and what was checked. It holds only public material: digests, the approval
key's fingerprint and the public validation and derivation reports. The approval private key and the
Admission host key stay in the stakeholder's private state and are not copied anywhere.

## 1. What the stakeholder ran

In their own terminal, from the repository root, with a Python 3.13 virtual environment (the system
`python3` on this host is 3.10, below `ssds`'s floor of 3.11):

1. `ssh-keygen -t ed25519 -C "ssds genesis approval" -f ~/.ssh/ssds-genesis` — a new approval key; its
   public half is the genesis trust root for human authentication.
2. `orchestrator/scripts/shadow_genesis.py prepare --public-key ~/.ssh/ssds-genesis.pub --baseline 9bf199120f7f289f10994189d1bd718690653dfc`
3. `ssh-keygen -Y sign -f ~/.ssh/ssds-genesis -n ssds ~/.ssds/genesis/ssdp-shadow/approval-message.txt`
4. `orchestrator/scripts/shadow_genesis.py admit --signature ~/.ssds/genesis/ssdp-shadow/approval-message.txt.sig`

## 2. Identities

| Item | Value |
|---|---|
| ledger id | `ssdp-shadow` |
| ledger location | `ssds-home:ledgers/ssdp-shadow.git`, ref `refs/ssds/ledger/ssdp-shadow` (catalogue §21.5 (ii), in the SSDS home) |
| baseline commit | `9bf199120f7f289f10994189d1bd718690653dfc` |
| genesis digest (signed) | `sha256:d7514f67a1071f6e008766a57a8c79d7ca88a434eddf19867194546b6b2e9a22` |
| approval message | `ssds genesis sha256:d7514f67a1071f6e008766a57a8c79d7ca88a434eddf19867194546b6b2e9a22` + newline, SSH namespace `ssds` |
| approval key | `human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw` (Ed25519, comment "ssds genesis approval") |
| entry digest | `sha256:69a182a6800c144591d6f1d5d6659eca2b09c78ac651d2ab81f05b00fb876ad2` |
| entry commit | `980373b80a9a0af8487bc3fece16d948e9d2ab74` (first parent: the baseline commit; fixed metadata) |
| ruleset | system `ssds-rules/1`, policy object `sha256:da93db77…3ea1` (`schema = 1`), analyzer object `sha256:dd3f77b9…3864` |
| witness model | `LOCAL_TRUST` `(N, q_a, r, f) = (1, 1, 1, 0)`, one file witness in the SSDS home |
| qualification | `QUALIFIED`, head position 0 = the entry digest above |

## 3. Checks

By the stakeholder's session, read-only: the validation report is valid with no problems and no
findings; the approval message names the digest; the proposal carries the stakeholder's public key; the
ledger repository's only ref is `refs/ssds/ledger/ssdp-shadow`; this repository has no `refs/ssds/*`
and no tracked changes.

Independently by the author's session, read-only, through the real owners (`ssds.ledger.read`,
`ssds.ledger.qualification`, `ssds.admission.genesis`, `ssds.derivation`):

- the chain read back from the ledger repository authenticates: 1 entry, no `INTEGRITY_HALT`, no
  unreadable schema version; the entry digest and commit are those above;
- the genesis digest recomputes from the admitted record; `genesis_violations`, the closed-schema record
  checks and the entry checks report nothing;
- the registered human key equals `~/.ssh/ssds-genesis.pub` (public half only; `ssh-keygen -lf` gives the
  fingerprint above) and the recorded SSHSIG verifies over the approval message;
- qualification against the file witness's one checkpoint is `QUALIFIED` at head 0;
- derivation over the admitted chain and this repository's trees makes a current assertion with no
  findings and no obligations, and the three subjects derive as below;
- this repository: no `refs/ssds/*`, no tracked change.

## 4. Validation report (`~/.ssds/genesis/ssdp-shadow/report.json`)

Valid; problems none; findings none. Modes: `ssdp.protocol` and `ssds8.manual` `LEGACY(7.2.1)`, `"*"`
`UNGOVERNED`. Units (20): `orchestrator.program`; `ssdp.protocol` with parts
`ssdp.protocol.role-numerical-algorithm-design`, `.role-scientific-formulation`, `.role-software-design`,
`.role-software-implementation`, `.shared`, `.specialists`; `ssds8.manual` with parts
`ssds8.manual.orientation`, `.primitives`, `.derivation`, `.admission`, `.work`, `.interface`, `.evidence`,
`.migration`, `.persistence`, `.components`, `.assurance`.

## 5. Derivation report (`~/.ssds/genesis/ssdp-shadow/derivation.json`)

| Subject | Mode | Revision | Parts | `valid` |
|---|---|---|---|---|
| `orchestrator.program` | `UNGOVERNED` | `sha256:8dc51191dd0dbec29dadcacceb108d107f1c16209f4da017c4b5ca6ed7f30223` | 0 | `F` |
| `ssdp.protocol` | `LEGACY` | `sha256:0597630d37adb088c58a2c24e0b1402e6853c14e5c9cfbfc73d7f36e73aa27fa` | 6 | `F` |
| `ssds8.manual` | `LEGACY` | `sha256:33ba68a6cb1f507bf8c492890ceb1367c594ff5f5e1bd2c9fdb1ee680f875467` | 11 | `F` |

Current assertion: true; entries 1; findings none; obligations none. `valid = F` throughout is the
expected shadow result: no acceptance of any kind is admitted at genesis (legacy acceptances are imported
by intake, Phase G), and SSDS holds no authority over these subjects.

## 6. Observed during the run

Under Python 3.13, `prepare` and `admit` printed `SyntaxWarning: invalid escape sequence '\w'` three
times: the Python analyzer's `ast.parse` of three archived `logs/mutate.py` files under
`qualification/ssdp70/` let the analyzed sources' compile warnings reach the operator. Repaired after the
run (the analyzer now parses with warnings captured; a test covers it); the archived files are unchanged,
and the warning changed no derived value.
