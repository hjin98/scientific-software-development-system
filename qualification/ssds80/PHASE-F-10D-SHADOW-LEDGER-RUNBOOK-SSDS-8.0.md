# SSDS 8 Phase F — step 10d on `ssdp-shadow-2`: runbook

```text
GOVERNING SSDP: 7.2.1 (identities from PROTOCOL-RELEASE-STATE.yaml)
PLAN: workplans/active/SSDS-8.0-G2-PHASE-F-PLAN.md §3.7 row 10d, reading F122 (revision 53); SD-69 Q-F7; F1; F8
SHADOW: no SSDS authority over any subject; observe-only; nothing is published, issued or executed
AUTHORITY: the stakeholder's. The ledgers under ~/.ssds are read-only to the implementing agent; every step that
           appends to ssdp-shadow-2 runs in the stakeholder's own shell, or with their explicit authorization
REHEARSED: orchestrator/tests/ssds/test_phase_f_step10d.py runs these steps on a fixture ledger of the same shape
```

The run is recorded in `PHASE-F-10D-SHADOW-LEDGER-EVIDENCE-SSDS-8.0.md`: each command, its output and each
boundary comparison.

## 0. Settings

Run from the repository root, which is the product repository the ledger observes.

```bash
cd /home/samjin/agent-skills/scientific-software-development-system
export PYTHONPATH="$PWD/orchestrator/src"
SSDS="python -m ssds.cli"
LEDGER=ssdp-shadow-2
BRANCH=ssds-8.0-graph-native-architecture
ACTOR='human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw'
WORK=/tmp/ssds-10d && mkdir -p "$WORK"          # outside the repository: the boundary script refuses otherwise
snap() { python orchestrator/scripts/shadow_boundary.py snapshot --repository . --out "$WORK/before.json"; }
check() { python orchestrator/scripts/shadow_boundary.py compare --repository . --before "$WORK/before.json"; }
```

Wrap every SSDS command from step 2 on as `snap; <command>; check`. Any `CHANGED` stops the run. Make no commit,
checkout or fetch in this repository while a snapshot is open.

## 1. The declarations and the policy file (a product change, before the comparison starts)

Done by the stakeholder, or by the author at their direction. Append to `.ssds/manifest.toml`:

```toml
# The reserved leaves (Manual §1.8; SD-69's in-place repair). UNGOVERNED.
[[unit]]
id = "ssds.manifest"
kind = "MANIFEST"
scope = [{ file = ".ssds/manifest.toml" }]

[[unit]]
id = "ssds.policy"
kind = "POLICY"
scope = [{ file = ".ssds/policy.toml" }]
```

Create `.ssds/policy.toml` holding exactly `schema = 1` and one newline:

```bash
printf 'schema = 1\n' > .ssds/policy.toml
sha256sum .ssds/policy.toml    # da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1
```

This file is required. Without it, `ssds.policy`'s `file` term resolves to nothing, and the adoption is rejected
`STRUCT_TERM_UNRESOLVED`. The bytes are genesis's default policy, whose digest is the policy digest in the ledger's
genesis ruleset. So the file equals the policy object the ledger already uses, and derivation's policy does not
change.

Commit the two files on `$BRANCH`. That commit is the observed head the next step absorbs.

## 2. Absorb (keys quarantined)

```bash
snap; $SSDS admission serve --ledger $LEDGER --repository . --observed-ref $BRANCH; check
```

Expect `"absorbed": true`. The first use records `$BRANCH` as the observed ref.

## 3. The author prepares the `ABSORB` request

```bash
snap; python orchestrator/scripts/reserved_leaves.py --ledger $LEDGER --repository . --actor "$ACTOR" --out "$WORK/inputs"; check
snap; $SSDS submit --ledger $LEDGER --prepare "$WORK/inputs/records.json" --actor "$ACTOR" --adopt "$WORK/inputs/delta-1.json" ...; check
```

Run the `submit` line exactly as `reserved_leaves.py` prints it: one `--adopt` per key. `--prepare` prints the
workspace `~/.ssds/state/ssdp-shadow-2/requests/<digest>/` and the commands that follow. Each `ABSORB` is
non-independent: the absorbed content's authorship is `UNKNOWN`. This is disclosed; §18.4 enacts it at S0.

## 4. The stakeholder reads, signs and admits

Read `summary.txt` in the workspace: one `INTAKE_DISPOSITION ABSORB` per declaration key of `ssds.manifest` and
`ssds.policy`, and the same deltas listed as adopted. Then:

```bash
ssh-keygen -Y sign -f ~/.ssh/ssds-genesis -n ssds ~/.ssds/state/ssdp-shadow-2/requests/<digest>/request-message.txt
snap; $SSDS submit --ledger $LEDGER --repository . --observed-ref $BRANCH --admit ~/.ssds/state/ssdp-shadow-2/requests/<digest>; check
```

Expect `"decision": "ACCEPT"`, with `submitted` repeating the summary that was signed. A `STALE_BASIS` or `REF_DELTA`
refusal means the branch moved the declarations: go back to step 3. Sign only inside the private workspace: what
`--admit` submits is `request.json`, and the signature covers exactly that.

## 5. `Σ` declares the three reserved leaves

```bash
snap; $SSDS inspect --ledger $LEDGER --repository .; check
```

Expect `ssds.manifest` (MANIFEST), `ssds.policy` (POLICY) and `ssds.unclassified` (UNCLASSIFIED) declared, and
none of their keys quarantined.

## 6. The restart check

```bash
snap; $SSDS admission serve --ledger $LEDGER --repository . --observed-ref $BRANCH; check
snap; $SSDS admission serve --ledger $LEDGER --repository . --observed-ref $BRANCH; check
```

The second pass appends nothing: compare the ledger's entry count in each report's `position`. A records-only
admission is never fenced (F1).

## 7. `dispatcher serve`, a report and a submit, a decide refused

```bash
snap; $SSDS dispatcher serve --ledger $LEDGER --repository .; check
```

It issues nothing and writes no run ref (F8).

The records-only `report` and `submit` use records the stakeholder chooses. They are permanent ledger entries,
so they should state something true. A template for `report` (`$WORK/report.json`):

```json
[{"kind": "FINDING", "schema": 1, "frame": "ADMITTED", "target": {"units": ["orchestrator.program"]},
  "basis": [], "outcome": null, "reason": [], "supersedes": [], "provenance": null, "refs": [],
  "governs": "<copy from $WORK/inputs/records.json>", "recorded_at": "<UTC now, YYYY-MM-DDTHH:MM:SSZ>",
  "ruleset": "<copy from $WORK/inputs/records.json>", "fields": {"materiality": "ROUTINE"}}]
```

Copy `ruleset` and `governs` from the records `reserved_leaves.py` wrote: they are the ledger's current ruleset
and the genesis record's `governs`, read through the program.

Each follows steps 3 and 4: `--prepare`, sign, then `--admit` with `report` or `submit`. Then a `decide`, which is
prepared, signed and refused at entry. Phase F accepts no gate or human decision (F1), and nothing is appended.

## 8. One candidate request through the library API, refused at entry

```bash
snap; python - <<'EOF'
from pathlib import Path
from ssds.cli import Composition
from ssds.admission.request import BoundaryRefused, expected_head
c = Composition("ssdp-shadow-2", Path("."))
chain = c.access.chain(); entries = chain.entries[: chain.readable_through + 1]
head = expected_head(entries)
req = {"binding": None, "claims": [], "base_position": len(entries) - 1, "base_commit": head,
       "candidates": ["0" * 40], "adopted_deltas": [], "records": [], "objects": {}}
try:
    c.admission().admit(req, head); print("NOT REFUSED: stop and report")
except BoundaryRefused as exc:
    print("refused at entry:", exc)
EOF
check
```

It is refused before validation, logged in `~/.ssds/state/ssdp-shadow-2/boundary.jsonl`, and nothing is appended.
The transports' and the Dispatcher's routes are step 10b's fixture tests.

## Notes for the operator

- **Never rewrite `$BRANCH`.** A force-push that rewinds it makes `admission serve` refuse until the branch again
  descends from the last observation (SD-64).
- **A signed records-only request has no expiry.** A record with no basis is admissible at any later head. Keep
  request workspaces private, and delete a workspace you no longer mean to admit.
- **A signed request names no ledger (Q-F29).** Do not register the same human key on a second live ledger while
  signed requests exist for this one.
- **`--prepare` puts no `objects` in a request.** A record that references `LEDGER`-store objects cannot be
  prepared this way.
- **The signature's armor is canonicalized before it is attached.** A re-wrapped or CRLF copy of the same
  `.sig` returns the recorded decision rather than making a new request.
