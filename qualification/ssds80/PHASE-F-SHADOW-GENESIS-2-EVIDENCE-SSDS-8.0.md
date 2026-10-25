# SSDS 8 Phase F — the shadow genesis `ssdp-shadow-2`: evidence record

```text
GOVERNING SSDP: 7.2.1 (identities from PROTOCOL-RELEASE-STATE.yaml)
PLAN: workplans/active/SSDS-8.0-G2-PHASE-F-PLAN.md §7 Q-F2 (settled by SD-64); Manual §19.9 Case B under A9
SHADOW: no SSDS authority over any subject; every subject LEGACY(7.2.1) or UNGOVERNED; no cutover
HUMAN GATE: the stakeholder's, taken 2026-10-25 in the stakeholder's own shell (item 62 of the decision
            record asked for it: "Bring me the link for me to sign.")
PROGRAM: ssds at 53d5a22c04f8c8035dfccd4577a3cdd9ece06a2b (the genesis baseline), run under Python 3.11
```

This records what was run and what was checked. It holds only public material: digests, the approval key's
fingerprint and the public reports. The approval private key and the Admission host key stay in the
stakeholder's private state and are not copied anywhere.

## 1. What was run

1. **`prepare`.** The author ran it in the stakeholder's terminal, at the stakeholder's request. It builds and validates the genesis in the SSDS home's isolated workspace and publishes nothing:
   `orchestrator/scripts/shadow_genesis.py --ledger-id ssdp-shadow-2 prepare --public-key ~/.ssh/ssds-genesis.pub --baseline 53d5a22c04f8c8035dfccd4577a3cdd9ece06a2b`
2. **The human gate.** The stakeholder signed, in their own shell, with their own key:
   `ssh-keygen -Y sign -f ~/.ssh/ssds-genesis -n ssds ~/.ssds/genesis/ssdp-shadow-2/approval-message.txt`
3. **`admit`.** The stakeholder ran it:
   `orchestrator/scripts/shadow_genesis.py --ledger-id ssdp-shadow-2 admit --signature ~/.ssds/genesis/ssdp-shadow-2/approval-message.txt.sig`

## 2. Identities

| Item | Value |
|---|---|
| Ledger id | `ssdp-shadow-2` (SD-64, Q-F2 (i)) |
| Ledger repository | `~/.ssds/ledgers/ssdp-shadow-2.git` (the SSDS home, A7) |
| Baseline commit | `53d5a22c04f8c8035dfccd4577a3cdd9ece06a2b` on `ssds-8.0-graph-native-architecture` |
| Genesis digest (signed) | `sha256:11dca045082fa38d05a567208a78a827dcb9d8dced0efa8b39e295297280ddb8` |
| Entry digest | `sha256:34e1fc29c357eb1cafa640645e4a168ea7a6d175779e65045cc537a5df0fc25f` |
| Entry commit | `8b6616c758e28ca3ff0cfe132a447ec78ce07850` |
| Approval key | `human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw` (the same key as Phase D step 7's genesis, SD-57) |
| Issue and runner keys | none (SD-64, Q-F2 (ii)) |

## 3. What was checked

- **Validation (`prepare`).** `valid: true`; no problems and no findings. The 21 declared units include the mandatory `ssds.unclassified` (A9, SD-61).
  - *Note, 2026-10-25, after admission:* that validation enforced only Manual §1.8's refusal clause (`ssds.unclassified` on the empty prefix). The structure declares neither of §1.8's other reserved leaves, `ssds.manifest` and `ssds.policy`. The Phase F plan's reading F18 and question Q-F7 carry this. The ledger's `QUALIFIED` state (§23) is unaffected.
- **Admission (`admit`).** `qualification: QUALIFIED`, `QUALIFIED at 0`, `current assertion: True`. The derivation report is in the genesis workspace.
- **Independent read-back.** The author read the ledger with `ssds.ledger.read.read_chain` and derived it with `ssds.derivation.derive` over the repository's trees, writing nothing. The results:
  - one entry, readable through position 0, no halt;
  - the baseline and ledger id as above;
  - modes only `LEGACY` and `UNGOVERNED` (Manual §19.9: shadow genesis);
  - the approval key as above;
  - the entry digest matching `admit`'s output;
  - no derived obligation, as a shadow ledger with no `NATIVE` subject derives none.

## 4. What follows

- Phase F step 10 runs `admission serve` observe-only on this ledger, with `--observed-ref ssds-8.0-graph-native-architecture` (reading F1, Q-F2 (i)).
- The old `ssdp-shadow` is retired by a retirement statement once Phase F step 7 can produce one (Q-F2 (iii)); Phase E reading E33's interim check retires with it (SD-61).
- The baseline predates Manual amendment A10's application (`39ad6f13`). That change, and every later commit on the branch, reaches this ledger as observed integrations.
