# SSDS 8 Phase F: the retirement of `ssdp-shadow` (evidence record)

```text
GOVERNING SSDP: 7.2.1 (identities from PROTOCOL-RELEASE-STATE.yaml)
PLAN: workplans/active/SSDS-8.0-G2-PHASE-F-PLAN.md step 7a, readings F44, F45, F49; §7 Q-F13 (settled by SD-74)
DECISIONS: SD-64 (Q-F2 (iii): the old ledger is retired); SD-74 (Q-F13 (a): ssdp-shadow-2 named for discovery only)
SHADOW: no SSDS authority over any subject; nothing carried over to the successor; nothing imported from either
HUMAN GATE: the stakeholder's, taken 2026-10-27 in the stakeholder's own shell (item 68 of the decision record:
            "I accept your recommendations. Proceed with it.")
PROGRAM: ssds at 7a1a3e228f17c7bb11345e6e1136ac8216fe9996, run under Python 3.11
```

This records what was run and what was checked. It holds only public material: digests, the approval key's
fingerprint and the host key's identity. The approval private key and the Admission host key stay in the
stakeholder's private state and are not copied anywhere.

## 1. What was run

The stakeholder ran all three steps in their own shell:
1. **`prepare`.** It builds the `LINEAGE_RETIREMENT` record for the ledger's next position and writes the record and its approval message to the ledger's workspace. Nothing is appended.
   `orchestrator/scripts/retire_shadow.py prepare --public-key ~/.ssh/ssds-genesis.pub`
2. **The human gate.** The stakeholder signed with their own key:
   `ssh-keygen -Y sign -f ~/.ssh/ssds-genesis -n ssds ~/.ssds/genesis/ssdp-shadow/retirement-message.txt`
3. **`admit`.** It admits the record through Admission's lifecycle path with `obs = null`, then publishes the retirement statement:
   `orchestrator/scripts/retire_shadow.py admit --signature ~/.ssds/genesis/ssdp-shadow/retirement-message.txt.sig`

   Its output was `admitted: LINEAGE_RETIREMENT at 1` and `qualification: RETIRED`.

## 2. Identities

| Item | Value |
|---|---|
| Ledger retired | `ssdp-shadow` (Phase D step 7's shadow genesis) |
| Genesis entry digest | `sha256:69a182a6800c144591d6f1d5d6659eca2b09c78ac651d2ab81f05b00fb876ad2` |
| Retirement entry | position 1, digest `sha256:ef50e86c51f42e9a79cd880ae8e3b3f5475bace4b27c82566fbcbc86d7b8c236`, commit `5b9e3f245f5fbf5b4bbc77cd18424b751307ead9`, `obs = null` |
| Successor (discovery only) | `ssdp-shadow-2`, genesis entry digest `sha256:34e1fc29c357eb1cafa640645e4a168ea7a6d175779e65045cc537a5df0fc25f`, matching `PHASE-F-SHADOW-GENESIS-2-EVIDENCE-SSDS-8.0.md` |
| Approval key | `human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw` (SD-57's key, as for both geneses) |
| Statement signer | the Admission host key `ed25519:fa13fe72299f3e0a219d1840653dde40cc21689b652d0347741c43dac0207ea0`, a trust root of the ledger's genesis |

## 3. What was checked

**Independent read-back.** The author read both ledgers through the program's Ledger Store functions, writing nothing: `read_chain`, `FileWitness.read` and `.statement`, `retirement_verified`, `retirement_held` and `qualify_segments`.

**`ssdp-shadow`.**
- Two entries, no halt: the genesis and the `LINEAGE_RETIREMENT` naming the successor above.
- Its witness, `local-file`, holds checkpoints 0 and 1.
- That witness holds the retirement statement:
  `{ledger_id: ssdp-shadow, kind: RETIREMENT, last_position: 1, last_entry_digest: sha256:ef50e86c…c236, successor_ledger_id: ssdp-shadow-2, successor_genesis_digest: sha256:34e1fc29…c25f}`.
- The statement verifies: it is signed by the host key above, and it names the chain's own `LINEAGE_RETIREMENT` at position 1.
- `q_a = 1` of the witness set holds it, so the ledger reads `RETIRED`. That means historical views only, and Admission appends nothing more (§23.4, §24.2).

**`ssdp-shadow-2`.** It is unaffected: one entry, `QUALIFIED` at 0.

## 4. What follows

- Phase E reading E33's interim check retires with the old ledger (SD-61). The old ledger's records stay readable as history and are imported nowhere (F44).
- The old ledger's high-water mark stays frozen at position 1 (F49). Deleting it belongs to a purge under G5, and none is authorized.
- Phase F step 10 runs on `ssdp-shadow-2` (SD-64).
