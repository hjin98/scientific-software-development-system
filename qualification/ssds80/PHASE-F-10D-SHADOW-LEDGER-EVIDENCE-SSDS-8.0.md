# SSDS 8 Phase F 10d — real shadow-ledger evidence (partial; qualification gap)

Governing SSDP: 7.2.1. Plan: revision 57, F122, SD-69; stakeholder authorization is item 72 of
`STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` (2026-10-29).
Asserter: AI implementing agent, Codex family. This is infrastructure execution evidence, not scientific gate evidence.

**Status: signed adoption ACCEPTED at position 2; 10d remains incomplete.** Eight `INTAKE_DISPOSITION ABSORB`
records are admitted; all three reserved leaves are effective, quarantine is empty, and the policy digest is unchanged.
The original repair verification found the ledger QUALIFIED with three entries and no provisional entry or critical finding. The scheduled continuation later absorbed the evidence commit at position 3 (four entries); see below. No native authority or campaign.

**Qualification gap:** the first actual append's command returned ACCEPT/exit 0, but its endpoint comparison failed
(exit 1), reporting repository-root modification/change metadata. Concurrent restricted tool calls were launched by
the implementing agent during that escalated-host command window. Restricted tools expose `.agents`, `.codex` and
`.aws` as read-only tmpfs mounts; their setup/removal changes root metadata. Snapshot history confirms the execution
views differ. No SSDS-caused product write was established. The original window remains FAILED/contaminated and
cannot support an unqualified unchanged claim. Independent review identified no Serious Challenge; it permitted
independent state/restart checks with this gap retained. A clean isolated no-op, idempotent replay, inspection,
restarts, Dispatcher observation and candidate refusal do not retroactively qualify that original append path.

Latest signed pair: original FINDING refused at 5 (SECRET_DETECTED); AVAILABILITY program-ACCEPTED at 6;
corrected typed FINDING ACCEPTED at 8. Its derived human-attention obligation is OPEN. The pending-requests
record owns the proposed unsigned decide-refusal exercise and its human-review route. **Additional D4 conformance gap: accepted AVAILABILITY carries narrative provenance contrary to
Manual §3.2/C7.** Program qualification is not blanket architecture conformance. Signed decide-refusal, frozen
study, classification and exit remain pending. Unqualified 10d/exit closure requires disposition of the gap.

## Identity and prerequisite evidence

- Product branch: `ssds-8.0-graph-native-architecture`, declarations commit `11ec88e4105124d70e3b1e606f2ec370ef1cc841`.
- Prior real-ledger baseline: `53d5a22c04f8c8035dfccd4577a3cdd9ece06a2b`; only genesis before this operation.
- Policy bytes: exactly `schema = 1\n`, digest `sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1`.
- Code/plan/operation reviews passed. Full suite: 1,879 tests in 634.733 s, OK (10 skipped), exit 0.
- Runtime: temporary Python 3.12.14 environment; actual installed `ssds` console entry point.
- Boundary: Git 2.53.0, two registered worktrees and two Git-storage roots; bytecode writes disabled.
  Old Git 2.34.1 refused linked-worktree inventory; that preflight is not an unchanged certificate.
- All suite/build/product edits and the declarations commit finished before the command windows below.
  The initial program read was preliminary, before step 1, and is not boundary-certified step-2+ evidence.

## Preparation commands (before the stakeholder signed)

Every command below has its own before snapshot and after comparison. All command and comparison exits were zero.
The snapshots include ignored content, raw Git storage and write metadata; access times and transient reverted writes
are excluded. The source/runbook read-only-path review remains separate evidence. Detailed transient logs live under
`/tmp/ssds-10d-20261029/`; the request itself is durable in the checked SSDS home.

### 02-observe

Command arguments:

```json
[
  "/tmp/ssds-phase-f-20261029/bin/ssds",
  "admission",
  "serve",
  "--ledger",
  "ssdp-shadow-2",
  "--repository",
  "/home/samjin/agent-skills/scientific-software-development-system",
  "--observed-ref",
  "ssds-8.0-graph-native-architecture"
]
```

Command exit: 0; comparison exit: 0.

```text
{
  "absorbed": true,
  "expected": "53d5a22c04f8c8035dfccd4577a3cdd9ece06a2b",
  "ledger_id": "ssdp-shadow-2",
  "mode": "observe-only: nothing is published (F1)",
  "obs": "11ec88e4105124d70e3b1e606f2ec370ef1cc841",
  "observed_ref": "ssds-8.0-graph-native-architecture",
  "position": 1
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/02-observe-before.json
```

Before-snapshot digest: `sha256:095a48534cf2f42ea87bfe1efcf51269909979e6c7dc9a4d3495ae2436631004`.

### 03-inputs

Command arguments:

```json
[
  "/tmp/ssds-phase-f-20261029/bin/python",
  "/home/samjin/agent-skills/scientific-software-development-system/orchestrator/scripts/reserved_leaves.py",
  "--ledger",
  "ssdp-shadow-2",
  "--repository",
  "/home/samjin/agent-skills/scientific-software-development-system",
  "--actor",
  "human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw",
  "--out",
  "/tmp/ssds-10d-20261029/inputs"
]
```

Command exit: 0; comparison exit: 0.

```text
ABSORB ssds.manifest.kind = "MANIFEST" (sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734)
ABSORB ssds.manifest.role = "leaf" (sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734)
ABSORB ssds.manifest.scope = [{"file": ".ssds/manifest.toml"}] (sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734)
ABSORB ssds.manifest.subject = true (sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734)
ABSORB ssds.policy.kind = "POLICY" (sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734)
ABSORB ssds.policy.role = "leaf" (sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734)
ABSORB ssds.policy.scope = [{"file": ".ssds/policy.toml"}] (sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734)
ABSORB ssds.policy.subject = true (sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734)
prepare the request with:
  ssds submit --ledger ssdp-shadow-2 --prepare /tmp/ssds-10d-20261029/inputs/records.json --actor human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw --adopt /tmp/ssds-10d-20261029/inputs/delta-1.json --adopt /tmp/ssds-10d-20261029/inputs/delta-2.json --adopt /tmp/ssds-10d-20261029/inputs/delta-3.json --adopt /tmp/ssds-10d-20261029/inputs/delta-4.json --adopt /tmp/ssds-10d-20261029/inputs/delta-5.json --adopt /tmp/ssds-10d-20261029/inputs/delta-6.json --adopt /tmp/ssds-10d-20261029/inputs/delta-7.json --adopt /tmp/ssds-10d-20261029/inputs/delta-8.json
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/03-inputs-before.json
```

Before-snapshot digest: `sha256:e6e4bb9429dcd68e216c1f03d5e9262638f493504af27a23e5d9a4f606d25186`.

### 03-prepare

Command arguments:

```json
[
  "/tmp/ssds-phase-f-20261029/bin/ssds",
  "submit",
  "--ledger",
  "ssdp-shadow-2",
  "--repository",
  "/home/samjin/agent-skills/scientific-software-development-system",
  "--prepare",
  "/tmp/ssds-10d-20261029/inputs/records.json",
  "--actor",
  "human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw",
  "--adopt",
  "/tmp/ssds-10d-20261029/inputs/delta-1.json",
  "--adopt",
  "/tmp/ssds-10d-20261029/inputs/delta-2.json",
  "--adopt",
  "/tmp/ssds-10d-20261029/inputs/delta-3.json",
  "--adopt",
  "/tmp/ssds-10d-20261029/inputs/delta-4.json",
  "--adopt",
  "/tmp/ssds-10d-20261029/inputs/delta-5.json",
  "--adopt",
  "/tmp/ssds-10d-20261029/inputs/delta-6.json",
  "--adopt",
  "/tmp/ssds-10d-20261029/inputs/delta-7.json",
  "--adopt",
  "/tmp/ssds-10d-20261029/inputs/delta-8.json"
]
```

Command exit: 0; comparison exit: 0.

```text
request sha256:9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8
ledger ssdp-shadow-2 at position 1, integration head 11ec88e4105124d70e3b1e606f2ec370ef1cc841
signed by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw
records:
  INTAKE_DISPOSITION sha256:e08093331454609c881774b8aaba79225dfb1e4f853c19a20d4afa15ae5e3e24
    target  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.manifest", "kind"]}
    outcome "ABSORB"
  INTAKE_DISPOSITION sha256:18961b125e7847721bb363e2cac28e7e2da5ad856c3f6717c2adf52678b48cd7
    target  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.manifest", "role"]}
    outcome "ABSORB"
  INTAKE_DISPOSITION sha256:d6fe2a9f50182dc3c7dc1f68178566a84130339729e43ac3e7ef73036f252e5f
    target  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.manifest", "scope"]}
    outcome "ABSORB"
  INTAKE_DISPOSITION sha256:01b87352fd923f32d9fbc2154cc3dfe2d07a830fccbbb749847f259a7658a7ef
    target  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.manifest", "subject"]}
    outcome "ABSORB"
  INTAKE_DISPOSITION sha256:135bec77bc8eff1d0ab752fd66bff572e2a98b36060c3ffc413df1783084d662
    target  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.policy", "kind"]}
    outcome "ABSORB"
  INTAKE_DISPOSITION sha256:b7e323c895e712827b1c9e1065c39fffc8d57a764cf63e4ab1d967e612d20aa2
    target  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.policy", "role"]}
    outcome "ABSORB"
  INTAKE_DISPOSITION sha256:a98c5dac51ea27082c215905d046950bbed99acac99e82f415a998c49fcb7f8a
    target  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.policy", "scope"]}
    outcome "ABSORB"
  INTAKE_DISPOSITION sha256:c7f9ea6ecfe8f18e02839bac93a458ad29cfa3790c1e40f2b1cbf453a579c842
    target  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.policy", "subject"]}
    outcome "ABSORB"
adopted deltas:
  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.manifest", "kind"], "value": "MANIFEST"}
  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.manifest", "role"], "value": "leaf"}
  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.manifest", "scope"], "value": [{"file": ".ssds/manifest.toml"}]}
  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.manifest", "subject"], "value": true}
  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.policy", "kind"], "value": "POLICY"}
  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.policy", "role"], "value": "leaf"}
  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.policy", "scope"], "value": [{"file": ".ssds/policy.toml"}]}
  {"absorption": "sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734", "key": ["ssds.policy", "subject"], "value": true}

prepared in /home/samjin/.ssds/state/ssdp-shadow-2/requests/9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8
sign it with your own key:
  ssh-keygen -Y sign -f <your key> -n ssds /home/samjin/.ssds/state/ssdp-shadow-2/requests/9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8/request-message.txt
then admit it:
  ssds submit --ledger ssdp-shadow-2 --repository <repository> --observed-ref <branch> --admit /home/samjin/.ssds/state/ssdp-shadow-2/requests/9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/03-prepare-before.json
```

Before-snapshot digest: `sha256:f583aed5eb66d763d1554bd296081c502d954e3a5d014935db86f3dd0480a220`.

### 03-verify

Command arguments:

```json
[
  "/tmp/ssds-phase-f-20261029/bin/python",
  "/tmp/ssds-10d-20261029/verify_request.py"
]
```

Command exit: 0; comparison exit: 0.

```text
{
  "request_id": "sha256:9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8",
  "records": 8,
  "adopted_keys": 8,
  "signature_present": false,
  "ledger_entries": 2,
  "summary": "/home/samjin/.ssds/state/ssdp-shadow-2/requests/9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8/summary.txt",
  "message": "/home/samjin/.ssds/state/ssdp-shadow-2/requests/9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8/request-message.txt",
  "message_text": "ssds request sha256:9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8"
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/03-verify-before.json
```

Before-snapshot digest: `sha256:d87bc8fbb9003d5f0488a8d308acd11ad9537b66cc1529e322e0c6867d057fd1`.

## Historical prepared request (before the stakeholder signed)

Prepared request: `sha256:9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8`.
Workspace: `/home/samjin/.ssds/state/ssdp-shadow-2/requests/9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8/`.
The program verified the stored message equals the rebuilt request message; eight records and eight adopted deltas
match exactly `{ssds.manifest,ssds.policy} × {kind,role,scope,subject}` and the current-delta identities/values.
At preparation time no signature was present. The absorbed content's authorship is UNKNOWN, so this ABSORB is non-independent as F122 discloses.
The prepared display's “signed by” names the proposed human actor; it is not evidence of an actual signature.

The stakeholder subsequently replied **"Signed."** Admission verified the signature and accepted the request.
Prepared payload identity: `sha256:9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8`.
Authenticated admission request identity: `sha256:a61ea1a6432236fb82d88592bba66a0f0401fe4c91fee7daa74c120495f3c064`.
Accepted head digest: `sha256:1fdc0aa75b977b9cbae9b1a51c01865d746ba3b23634f967bedb4c5320dec21f`.
The agent did not access the stakeholder's private signing key. The eight dispositions are non-independent as F122
already disclosed; they enact at S0 under that rule, not by independent-review authority.

## Post-signature execution

The first boundary failure stopped the governed run. Read-only diagnosis exposed different sandbox filesystem views.
An isolated no-op then passed. Subsequent command windows ran in single escalated-host processes, with no restricted
filesystem probes or agent processes during them. The failure below is preserved unchanged. Detailed transient logs
are under `/tmp/ssds-10d-20261029/`; current state is retained in the real ledger through its owning program.

### 04-admit

Command exit: 0; comparison exit: 1.

```json
[
  "/tmp/ssds-phase-f-20261029/bin/ssds",
  "submit",
  "--ledger",
  "ssdp-shadow-2",
  "--repository",
  "/home/samjin/agent-skills/scientific-software-development-system",
  "--observed-ref",
  "ssds-8.0-graph-native-architecture",
  "--admit",
  "/home/samjin/.ssds/state/ssdp-shadow-2/requests/9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8"
]
```

```text
{
  "admitted": [
    "sha256:e08093331454609c881774b8aaba79225dfb1e4f853c19a20d4afa15ae5e3e24",
    "sha256:18961b125e7847721bb363e2cac28e7e2da5ad856c3f6717c2adf52678b48cd7",
    "sha256:d6fe2a9f50182dc3c7dc1f68178566a84130339729e43ac3e7ef73036f252e5f",
    "sha256:01b87352fd923f32d9fbc2154cc3dfe2d07a830fccbbb749847f259a7658a7ef",
    "sha256:135bec77bc8eff1d0ab752fd66bff572e2a98b36060c3ffc413df1783084d662",
    "sha256:b7e323c895e712827b1c9e1065c39fffc8d57a764cf63e4ab1d967e612d20aa2",
    "sha256:a98c5dac51ea27082c215905d046950bbed99acac99e82f415a998c49fcb7f8a",
    "sha256:c7f9ea6ecfe8f18e02839bac93a458ad29cfa3790c1e40f2b1cbf453a579c842"
  ],
  "appended": true,
  "decision": "ACCEPT",
  "ledger_id": "ssdp-shadow-2",
  "observed_ref": "ssds-8.0-graph-native-architecture",
  "position": 2,
  "reasons": [],
  "refused": [],
  "request_id": "sha256:a61ea1a6432236fb82d88592bba66a0f0401fe4c91fee7daa74c120495f3c064",
  "submitted": "request sha256:9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8\nledger ssdp-shadow-2 at position 1, integration head 11ec88e4105124d70e3b1e606f2ec370ef1cc841\nsigned by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw\nrecords:\n  INTAKE_DISPOSITION sha256:e08093331454609c881774b8aaba79225dfb1e4f853c19a20d4afa15ae5e3e24\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"kind\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:18961b125e7847721bb363e2cac28e7e2da5ad856c3f6717c2adf52678b48cd7\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"role\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:d6fe2a9f50182dc3c7dc1f68178566a84130339729e43ac3e7ef73036f252e5f\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"scope\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:01b87352fd923f32d9fbc2154cc3dfe2d07a830fccbbb749847f259a7658a7ef\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"subject\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:135bec77bc8eff1d0ab752fd66bff572e2a98b36060c3ffc413df1783084d662\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"kind\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:b7e323c895e712827b1c9e1065c39fffc8d57a764cf63e4ab1d967e612d20aa2\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"role\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:a98c5dac51ea27082c215905d046950bbed99acac99e82f415a998c49fcb7f8a\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"scope\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:c7f9ea6ecfe8f18e02839bac93a458ad29cfa3790c1e40f2b1cbf453a579c842\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"subject\"]}\n    outcome \"ABSORB\"\nadopted deltas:\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"kind\"], \"value\": \"MANIFEST\"}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"role\"], \"value\": \"leaf\"}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"scope\"], \"value\": [{\"file\": \".ssds/manifest.toml\"}]}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"subject\"], \"value\": true}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"kind\"], \"value\": \"POLICY\"}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"role\"], \"value\": \"leaf\"}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"scope\"], \"value\": [{\"file\": \".ssds/policy.toml\"}]}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"subject\"], \"value\": true}\n"
}
worktrees /home/samjin/agent-skills/scientific-software-development-system: . changed
/home/samjin/agent-skills/scientific-software-development-system: CHANGED since /tmp/ssds-10d-20261029/04-admit-before.json
```

Before-snapshot digest: `sha256:1d9c12cb1e8b468c48ee082574b53859ed785e7198324ec7b2fbe21c876a993d`.

### 04-isolated-control

Command exit: 0; comparison exit: 0.

```json
[
  "/tmp/ssds-phase-f-20261029/bin/python",
  "-c",
  "pass"
]
```

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/04-isolated-control-before.json
```

Before-snapshot digest: `sha256:7addf7f479d003d9038db750f54d1d89e0582ce59cd171b6949fef0f97c78660`.

### 04-isolated-replay

Command exit: 0; comparison exit: 0.

```json
[
  "/tmp/ssds-phase-f-20261029/bin/ssds",
  "submit",
  "--ledger",
  "ssdp-shadow-2",
  "--repository",
  "/home/samjin/agent-skills/scientific-software-development-system",
  "--observed-ref",
  "ssds-8.0-graph-native-architecture",
  "--admit",
  "/home/samjin/.ssds/state/ssdp-shadow-2/requests/9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8"
]
```

```text
{
  "admitted": [
    "sha256:e08093331454609c881774b8aaba79225dfb1e4f853c19a20d4afa15ae5e3e24",
    "sha256:18961b125e7847721bb363e2cac28e7e2da5ad856c3f6717c2adf52678b48cd7",
    "sha256:d6fe2a9f50182dc3c7dc1f68178566a84130339729e43ac3e7ef73036f252e5f",
    "sha256:01b87352fd923f32d9fbc2154cc3dfe2d07a830fccbbb749847f259a7658a7ef",
    "sha256:135bec77bc8eff1d0ab752fd66bff572e2a98b36060c3ffc413df1783084d662",
    "sha256:b7e323c895e712827b1c9e1065c39fffc8d57a764cf63e4ab1d967e612d20aa2",
    "sha256:a98c5dac51ea27082c215905d046950bbed99acac99e82f415a998c49fcb7f8a",
    "sha256:c7f9ea6ecfe8f18e02839bac93a458ad29cfa3790c1e40f2b1cbf453a579c842"
  ],
  "appended": false,
  "decision": "ACCEPT",
  "ledger_id": "ssdp-shadow-2",
  "observed_ref": "ssds-8.0-graph-native-architecture",
  "position": 2,
  "reasons": [],
  "refused": [],
  "request_id": "sha256:a61ea1a6432236fb82d88592bba66a0f0401fe4c91fee7daa74c120495f3c064",
  "submitted": "request sha256:9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8\nledger ssdp-shadow-2 at position 1, integration head 11ec88e4105124d70e3b1e606f2ec370ef1cc841\nsigned by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw\nrecords:\n  INTAKE_DISPOSITION sha256:e08093331454609c881774b8aaba79225dfb1e4f853c19a20d4afa15ae5e3e24\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"kind\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:18961b125e7847721bb363e2cac28e7e2da5ad856c3f6717c2adf52678b48cd7\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"role\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:d6fe2a9f50182dc3c7dc1f68178566a84130339729e43ac3e7ef73036f252e5f\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"scope\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:01b87352fd923f32d9fbc2154cc3dfe2d07a830fccbbb749847f259a7658a7ef\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"subject\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:135bec77bc8eff1d0ab752fd66bff572e2a98b36060c3ffc413df1783084d662\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"kind\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:b7e323c895e712827b1c9e1065c39fffc8d57a764cf63e4ab1d967e612d20aa2\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"role\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:a98c5dac51ea27082c215905d046950bbed99acac99e82f415a998c49fcb7f8a\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"scope\"]}\n    outcome \"ABSORB\"\n  INTAKE_DISPOSITION sha256:c7f9ea6ecfe8f18e02839bac93a458ad29cfa3790c1e40f2b1cbf453a579c842\n    target  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"subject\"]}\n    outcome \"ABSORB\"\nadopted deltas:\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"kind\"], \"value\": \"MANIFEST\"}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"role\"], \"value\": \"leaf\"}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"scope\"], \"value\": [{\"file\": \".ssds/manifest.toml\"}]}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.manifest\", \"subject\"], \"value\": true}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"kind\"], \"value\": \"POLICY\"}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"role\"], \"value\": \"leaf\"}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"scope\"], \"value\": [{\"file\": \".ssds/policy.toml\"}]}\n  {\"absorption\": \"sha256:d6906be0741604f9d95a1436317ea743dac2d0fc8049d84c242b9d72576ea734\", \"key\": [\"ssds.policy\", \"subject\"], \"value\": true}\n"
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/04-isolated-replay-before.json
```

Before-snapshot digest: `sha256:7addf7f479d003d9038db750f54d1d89e0582ce59cd171b6949fef0f97c78660`.

### 05-inspect

Command exit: 0; comparison exit: 0.

```json
[
  "/tmp/ssds-phase-f-20261029/bin/ssds",
  "inspect",
  "--ledger",
  "ssdp-shadow-2",
  "--repository",
  "/home/samjin/agent-skills/scientific-software-development-system"
]
```

```text
{
  "answer": {
    "digest": [],
    "entries": [],
    "head": {
      "digest": "sha256:1fdc0aa75b977b9cbae9b1a51c01865d746ba3b23634f967bedb4c5320dec21f",
      "label": "QUALIFIED",
      "position": 2,
      "qualification": "QUALIFIED"
    }
  },
  "head": {
    "digest": "sha256:1fdc0aa75b977b9cbae9b1a51c01865d746ba3b23634f967bedb4c5320dec21f",
    "label": "QUALIFIED",
    "position": 2,
    "qualification": "QUALIFIED"
  },
  "query": "inspect"
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/05-inspect-before.json
```

Before-snapshot digest: `sha256:7addf7f479d003d9038db750f54d1d89e0582ce59cd171b6949fef0f97c78660`.

### 06-restart-one

Command exit: 0; comparison exit: 0.

```json
[
  "/tmp/ssds-phase-f-20261029/bin/ssds",
  "admission",
  "serve",
  "--ledger",
  "ssdp-shadow-2",
  "--repository",
  "/home/samjin/agent-skills/scientific-software-development-system",
  "--observed-ref",
  "ssds-8.0-graph-native-architecture"
]
```

```text
{
  "absorbed": false,
  "expected": "11ec88e4105124d70e3b1e606f2ec370ef1cc841",
  "ledger_id": "ssdp-shadow-2",
  "mode": "observe-only: nothing is published (F1)",
  "obs": "11ec88e4105124d70e3b1e606f2ec370ef1cc841",
  "observed_ref": "ssds-8.0-graph-native-architecture",
  "position": 2
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/06-restart-one-before.json
```

Before-snapshot digest: `sha256:7addf7f479d003d9038db750f54d1d89e0582ce59cd171b6949fef0f97c78660`.

### 06-restart-two

Command exit: 0; comparison exit: 0.

```json
[
  "/tmp/ssds-phase-f-20261029/bin/ssds",
  "admission",
  "serve",
  "--ledger",
  "ssdp-shadow-2",
  "--repository",
  "/home/samjin/agent-skills/scientific-software-development-system",
  "--observed-ref",
  "ssds-8.0-graph-native-architecture"
]
```

```text
{
  "absorbed": false,
  "expected": "11ec88e4105124d70e3b1e606f2ec370ef1cc841",
  "ledger_id": "ssdp-shadow-2",
  "mode": "observe-only: nothing is published (F1)",
  "obs": "11ec88e4105124d70e3b1e606f2ec370ef1cc841",
  "observed_ref": "ssds-8.0-graph-native-architecture",
  "position": 2
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/06-restart-two-before.json
```

Before-snapshot digest: `sha256:7addf7f479d003d9038db750f54d1d89e0582ce59cd171b6949fef0f97c78660`.

### 07-dispatcher

Command exit: 0; comparison exit: 0.

```json
[
  "/tmp/ssds-phase-f-20261029/bin/ssds",
  "dispatcher",
  "serve",
  "--ledger",
  "ssdp-shadow-2",
  "--repository",
  "/home/samjin/agent-skills/scientific-software-development-system"
]
```

```text
{
  "head": 2,
  "head_digest": "sha256:1fdc0aa75b977b9cbae9b1a51c01865d746ba3b23634f967bedb4c5320dec21f",
  "held": [],
  "issued": [],
  "ledger_id": "ssdp-shadow-2",
  "mode": "observe-only: nothing is issued and no run ref is written (F8)",
  "qualification": "QUALIFIED",
  "would_issue": []
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/07-dispatcher-before.json
```

Before-snapshot digest: `sha256:7addf7f479d003d9038db750f54d1d89e0582ce59cd171b6949fef0f97c78660`.

### 05-status

Command exit: 0; comparison exit: 0.

```json
[
  "/tmp/ssds-phase-f-20261029/bin/ssds",
  "status",
  "--ledger",
  "ssdp-shadow-2",
  "--repository",
  "/home/samjin/agent-skills/scientific-software-development-system"
]
```

```text
{
  "assertion_withheld": [],
  "critical": [],
  "current_assertion": true,
  "entries": 3,
  "head": {
    "digest": "sha256:1fdc0aa75b977b9cbae9b1a51c01865d746ba3b23634f967bedb4c5320dec21f",
    "label": "QUALIFIED",
    "position": 2,
    "qualification": "QUALIFIED"
  },
  "ledger_id": "ssdp-shadow-2",
  "obligations": [],
  "provisional": null,
  "qualification": "QUALIFIED",
  "subjects": {
    "orchestrator.program": {
      "mode": "UNGOVERNED",
      "rev": "sha256:b14a3bc958830e5b4982adfb872af4ac7852f18c5414e066c7af0abe6c36db63",
      "status": "unclassified"
    },
    "ssdp.protocol": {
      "mode": "LEGACY",
      "rev": "sha256:0597630d37adb088c58a2c24e0b1402e6853c14e5c9cfbfc73d7f36e73aa27fa",
      "status": "stale"
    },
    "ssds.manifest": {
      "mode": "UNGOVERNED",
      "rev": "sha256:fb77e7dedb294322d49d4f99d3c157fbe52080aaff08833444fecf29f254e3ee",
      "status": "unclassified"
    },
    "ssds.policy": {
      "mode": "UNGOVERNED",
      "rev": "sha256:a0c4b3794237c0a5a73ed364ac23b2f63275c0d0c63b5f81aae2c6e623fa1fa4",
      "status": "unclassified"
    },
    "ssds.unclassified": {
      "mode": "UNGOVERNED",
      "rev": "sha256:26f8e870291207e8948fc33f4d642b3529004e983773ddfac1e18b646479232b",
      "status": "unclassified"
    },
    "ssds8.manual": {
      "mode": "LEGACY",
      "rev": "sha256:c5090340091ca7c72257d48b6ff327c1a0703d86b88bc1097d81d90a88374b23",
      "status": "stale"
    }
  }
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/05-status-before.json
```

Before-snapshot digest: `sha256:a89d4b482a0464f311db18d20024ee722e7a1ffb0e8877dda44011cca0d150f7`.

### 05-effective

Command exit: 0; comparison exit: 0.

```json
[
  "/tmp/ssds-phase-f-20261029/bin/python",
  "/tmp/ssds-10d-20261029/verify_effective.py"
]
```

```text
{
  "position": 2,
  "entries": 3,
  "reserved_leaves": {
    "ssds.manifest": "MANIFEST",
    "ssds.policy": "POLICY",
    "ssds.unclassified": "UNCLASSIFIED"
  },
  "quarantine": [],
  "policy_unchanged": true,
  "dispositions_non_independent": true,
  "admitted_records": 8
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/05-effective-before.json
```

Before-snapshot digest: `sha256:a89d4b482a0464f311db18d20024ee722e7a1ffb0e8877dda44011cca0d150f7`.

### 08-candidate-refusal

Command exit: 0; comparison exit: 0.

```json
[
  "/tmp/ssds-phase-f-20261029/bin/python",
  "/tmp/ssds-10d-20261029/candidate_refusal.py"
]
```

```text
{
  "refused_at_entry": "a candidate: the real shadow ledger observes and never publishes (F1)",
  "appended": false,
  "position": 2
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/08-candidate-refusal-before.json
```

Before-snapshot digest: `sha256:a89d4b482a0464f311db18d20024ee722e7a1ffb0e8877dda44011cca0d150f7`.

## Assessment and remaining work

- Admission accepted all eight records with no refused record or rejection reason. The isolated replay returned the
  same authenticated request identity, `appended: false`, position 2.
- `inspect` establishes the QUALIFIED head and empty attention view; it does not display effective structure.
  `status` confirms current assertion and three entries. The explicit program-owner check (`05-effective`) confirms
  MANIFEST/POLICY/UNCLASSIFIED kinds, empty quarantine, unchanged policy, and non-independent dispositions.
- Both restarts stayed at position 2 and absorbed nothing. Dispatcher issued nothing and wrote no run ref.
- The candidate probe was refused at entry and logged, with no new ledger entry. All these isolated endpoint checks passed.
- The original actual-append boundary gap is not closed by those results. No finding of SSDS-caused mutation, and no
  claim that the original product endpoint was unchanged. It remains qualified evidence pending governing disposition.
- Two true permanent `report`/`submit` records still require stakeholder choice and signatures. The `decide` refusal
  also needs a prepared signed request. No dummy record, new key registration, campaign or native authority was introduced.
- 11b/frozen-candidate classification and exit review remain open. No scientific results or scientific gate evidence
  were produced; execution evidence here concerns governance infrastructure.

All evidence-file edits occurred after command windows closed. The temporary restricted-view diagnostic snapshot
must not be treated as a same-filesystem-view after-snapshot of the original escalated command. Repository persistence
of this record does not advance the observed ledger head; a later observation will record any descendant commit.

## Retained diagnostic and verification data

These are different execution-context views, not a valid matched before/after pair. The original host-view
comparison already recorded only root metadata changing. Independent AI review (Codex family) reported the
three restricted-only paths as read-only tmpfs mounts from its namespace mount information; raw mountinfo output
was not retained, so that mount-type statement remains reviewer-reported evidence.

```json
{
  "host_before_root": {
    "ctime_ns": 1793253045624091736,
    "device": 66309,
    "inode": 35524891,
    "mode": 16893,
    "mtime_ns": 1793253045624091736
  },
  "restricted_diagnostic_root": {
    "ctime_ns": 1793253276353107364,
    "device": 66309,
    "inode": 35524891,
    "mode": 16893,
    "mtime_ns": 1793253276353107364
  },
  "restricted_only_entries": {
    ".agents": {
      "ctime_ns": 1793253276352107360,
      "device": 124,
      "inode": 1,
      "mode": 16749,
      "mtime_ns": 1793253276352107360
    },
    ".codex": {
      "ctime_ns": 1793253276352107360,
      "device": 125,
      "inode": 1,
      "mode": 16749,
      "mtime_ns": 1793253276352107360
    },
    ".aws": {
      "ctime_ns": 1793253276353107364,
      "device": 128,
      "inode": 1,
      "mode": 16749,
      "mtime_ns": 1793253276353107364
    }
  }
}
```

<details>
<summary>Exact sources of the temporary read-only verification/probe scripts</summary>

These scripts are retained as inert execution evidence, not program authority. Their assertions support only
the bounded checks described above. Native command output and the independent source review remain separate.

### verify_request.py

Source digest: `sha256:7490481aa06c3ba9dd264e3f2323eba2fcf6764c3bdafd02196a8784ec77d7c4`.

```python
import json
from pathlib import Path
from ssds.cli import Composition
from ssds.admission.request import expected_head,request_id,request_message
from ssds.content import value_to_json
from ssds.derivation import derive
rid='sha256:9e8843c0de459bbffaa0b7f37183729086beaf2f20ff57d0abc4ae030c55edc8'
c=Composition('ssdp-shadow-2',Path('/home/samjin/agent-skills/scientific-software-development-system'))
operator=c.state()
request=json.loads(operator.read_private(c.request_parts(rid,'request.json')))
message=operator.read_private(c.request_parts(rid,'request-message.txt'))
summary=operator.read_private(c.request_parts(rid,'summary.txt')).decode()
chain=c.access.chain()
entries=chain.entries[:chain.readable_through+1]
s=derive(chain,c.trees,ancestry=c.access.ancestry()).s
expected={(u,f) for u in ('ssds.manifest','ssds.policy') for f in ('kind','role','scope','subject')}
assert chain.halt is None and len(entries)==2 and request['base_position']==1
assert request['base_commit']==expected_head(entries)=='11ec88e4105124d70e3b1e606f2ec370ef1cc841'
assert request_id(request)==rid and request_message(request)==message
assert request['binding'] is None and request['candidates']==[] and request['objects']=={} and request['claims']==[]
assert len(request['records'])==len(request['adopted_deltas'])==8
assert {tuple(r['target']['key']) for r in request['records']}==expected
assert {tuple(d['key']) for d in request['adopted_deltas']}==expected
assert all(r['kind']=='INTAKE_DISPOSITION' and r['outcome']=='ABSORB' and r['actor_class']=='HUMAN' and r['basis']==[]
           for r in request['records'])
assert {(r['target']['absorption'],tuple(r['target']['key'])) for r in request['records']}=={
    (d['absorption'],tuple(d['key'])) for d in request['adopted_deltas']}
for delta in request['adopted_deltas']:
    current=s.current_delta(tuple(delta['key']))
    assert current is not None and delta['absorption']==current[0]
    assert delta['value']==value_to_json(delta['key'][1],current[1])
assert summary.startswith('request '+rid+'\n')
assert operator.read_private(c.request_parts(rid,'request-message.txt.sig')) is None
result={'request_id':rid,'records':8,'adopted_keys':8,'signature_present':False,'ledger_entries':len(entries),
        'summary':str(operator.path(c.request_parts(rid,'summary.txt'))),
        'message':str(operator.path(c.request_parts(rid,'request-message.txt'))),
        'message_text':message.decode().strip()}
print(json.dumps(result,indent=2))
```

### verify_effective.py

Source digest: `sha256:ebe8dd19baeea6e9b5326e6bd816835be06675b5bd9d83fec7f5f1102eb3bc66`.

```python
import json
from pathlib import Path
from ssds.cli import Composition
from ssds.derivation import derive
from ssds.admission.request import expected_head
c=Composition('ssdp-shadow-2',Path('/home/samjin/agent-skills/scientific-software-development-system'))
chain=c.access.chain(); entries=chain.entries[:chain.readable_through+1]
d=derive(chain,c.trees,ancestry=c.access.ancestry()); s=d.s
expected={'ssds.manifest':'MANIFEST','ssds.policy':'POLICY','ssds.unclassified':'UNCLASSIFIED'}
assert chain.halt is None and len(entries)==3
assert entries[-1].entry['admission']['decision']=='ACCEPT'
assert len(entries[-1].entry['records'])==8
assert expected_head(entries)=='11ec88e4105124d70e3b1e606f2ec370ef1cc841'
for uid,kind in expected.items():
    assert uid in s.view.structure.units and s.view.structure.kind(uid)==kind
    assert not any(key[0]==uid for key in s.s0.quarantine)
assert s.h.ruleset(s.n)['policy']=='sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1'
assert all(d.j.nonind(r['id']) for r in entries[-1].entry['records'])
print(json.dumps({'position':s.n,'entries':len(entries),'reserved_leaves':expected,'quarantine':[list(k) for k in sorted(s.s0.quarantine)],
                  'policy_unchanged':True,'dispositions_non_independent':True,'admitted_records':8},indent=2))
```

### candidate_refusal.py

Source digest: `sha256:e5cd85000f20536148a46fef66712aa7856fe4c39b2e9f4d4f5d9b3b2ca8f63c`.

```python
import json
from pathlib import Path
from ssds.cli import Composition
from ssds.admission.request import BoundaryRefused,expected_head
c=Composition('ssdp-shadow-2',Path('/home/samjin/agent-skills/scientific-software-development-system'))
chain=c.access.chain(); entries=chain.entries[:chain.readable_through+1]
head=expected_head(entries)
request={'binding':None,'claims':[],'base_position':len(entries)-1,'base_commit':head,
         'candidates':['0'*40],'adopted_deltas':[],'records':[],'objects':{}}
try:
    c.admission().admit(request,head)
except BoundaryRefused as exc:
    after=c.access.chain()
    assert len(after.entries)==len(chain.entries) and after.entries[-1].digest==chain.entries[-1].digest
    print(json.dumps({'refused_at_entry':str(exc),'appended':False,'position':len(entries)-1},indent=2))
else:
    raise SystemExit('NOT REFUSED: stop and report')
```

</details>

**Independent closeout review: PASS for evidence/plan/runbook consistency only.** The reviewer matched all 14
step sections to native command records, output and snapshot digests; no real-store/key access or new execution
was performed by that reviewer. No 10d/exit acceptance is inferred from this documentation check.


## Scheduled continuation: position 3 and unsigned remaining requests

Asserter: AI implementing agent, Codex family, 2026-10-29. Governing scope remains SSDP 7.2.1, F121–F122.
The user authorized preparation of the proposed FINDING/AVAILABILITY pair and a scheduled resume.
Steps below ran sequentially in isolated escalated-host windows; no agent probes or restricted tools ran
concurrently. Each command and comparison exited 0. These passes qualify only their own endpoint windows.
The original position-2 append comparison stays FAILED/contaminated.

### 15-resume-observe

```json
{
  "at": "2026-10-29T10:35:36.898343+00:00",
  "step": "15-resume-observe",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "admission",
    "serve",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system",
    "--observed-ref",
    "ssds-8.0-graph-native-architecture"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

Native command output:

```text
{
  "absorbed": true,
  "expected": "11ec88e4105124d70e3b1e606f2ec370ef1cc841",
  "ledger_id": "ssdp-shadow-2",
  "mode": "observe-only: nothing is published (F1)",
  "obs": "6d43121b440743a3b6e9f78b7600a40e4fc5ba7a",
  "observed_ref": "ssds-8.0-graph-native-architecture",
  "position": 3
}
```

Endpoint comparison:

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/15-resume-observe-before.json
```

### 16-policy-object

```json
{
  "at": "2026-10-29T10:35:54.065287+00:00",
  "step": "16-policy-object",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/verify_policy_object.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

Native command output:

```text
{
  "ledger": "ssdp-shadow-2",
  "position": 3,
  "entries": 4,
  "head": "6d43121b440743a3b6e9f78b7600a40e4fc5ba7a",
  "ruleset": {
    "analyzers": "sha256:dd3f77b9bb229bce543e97388fc8cb70ac5b8e3d8315142b0db490e753e73864",
    "policy": "sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1",
    "system": "ssds-rules/1"
  },
  "policy_object": {
    "store": "LEDGER",
    "digest": "sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1",
    "bytes": 11,
    "text": "schema = 1\n",
    "matches_committed_default": true
  },
  "quarantine": []
}
```

Endpoint comparison:

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/16-policy-object-before.json
```

### 17-build-record-proposals

```json
{
  "at": "2026-10-29T10:37:18.707740+00:00",
  "step": "17-build-record-proposals",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/build_remaining_records.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

Native command output:

```text
{
  "position": 3,
  "actor": "human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw",
  "files": [
    "remaining-finding.json",
    "remaining-availability.json"
  ],
  "evidence": {
    "store": "REPO",
    "digest": "sha256:8d29d152af813ad6942dd272c7b8bfb52da332f91af2b605d0efa50ad7ef98a5",
    "media_type": "text/markdown",
    "locator": "6d43121b440743a3b6e9f78b7600a40e4fc5ba7a:qualification/ssds80/PHASE-F-10D-SHADOW-LEDGER-EVIDENCE-SSDS-8.0.md"
  },
  "policy": "sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1",
  "schema_violations": []
}
```

Endpoint comparison:

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/17-build-record-proposals-before.json
```

### 18-rebuild-record-proposals

```json
{
  "at": "2026-10-29T10:39:45.743088+00:00",
  "step": "18-rebuild-record-proposals",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/build_remaining_records.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

Native command output:

```text
{
  "position": 3,
  "actor": "human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw",
  "files": [
    "remaining-finding.json",
    "remaining-availability.json"
  ],
  "evidence": {
    "store": "REPO",
    "digest": "sha256:8d29d152af813ad6942dd272c7b8bfb52da332f91af2b605d0efa50ad7ef98a5",
    "media_type": "text/markdown",
    "locator": "6d43121b440743a3b6e9f78b7600a40e4fc5ba7a:qualification/ssds80/PHASE-F-10D-SHADOW-LEDGER-EVIDENCE-SSDS-8.0.md"
  },
  "policy": "sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1",
  "schema_violations": []
}
```

Endpoint comparison:

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/18-rebuild-record-proposals-before.json
```

### 19-prepare-finding

```json
{
  "at": "2026-10-29T10:40:03.678589+00:00",
  "step": "19-prepare-finding",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "report",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system",
    "--prepare",
    "/tmp/ssds-10d-20261029/remaining-finding.json",
    "--actor",
    "human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

Native command output:

```text
request sha256:324bd39ebcf696b22fa1991ec870f8d7a0d046ef243c05d309be0cd74709d8c6
ledger ssdp-shadow-2 at position 3, integration head 6d43121b440743a3b6e9f78b7600a40e4fc5ba7a
signed by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw
records:
  FINDING sha256:cd4939aad706b25c35de25228d8cce49ef9fe20161f8636179cc1c5ba4d84345
    target  {"units": ["orchestrator.program", "ssds.manifest", "ssds.policy"]}
    outcome null
adopted deltas: none

prepared in /home/samjin/.ssds/state/ssdp-shadow-2/requests/324bd39ebcf696b22fa1991ec870f8d7a0d046ef243c05d309be0cd74709d8c6
sign it with your own key:
  ssh-keygen -Y sign -f <your key> -n ssds /home/samjin/.ssds/state/ssdp-shadow-2/requests/324bd39ebcf696b22fa1991ec870f8d7a0d046ef243c05d309be0cd74709d8c6/request-message.txt
then admit it:
  ssds report --ledger ssdp-shadow-2 --repository <repository> --observed-ref <branch> --admit /home/samjin/.ssds/state/ssdp-shadow-2/requests/324bd39ebcf696b22fa1991ec870f8d7a0d046ef243c05d309be0cd74709d8c6
```

Endpoint comparison:

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/19-prepare-finding-before.json
```

### 20-final-record-proposals

```json
{
  "at": "2026-10-29T10:40:31.228106+00:00",
  "step": "20-final-record-proposals",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/build_remaining_records.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

Native command output:

```text
{
  "position": 3,
  "actor": "human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw",
  "files": [
    "remaining-finding.json",
    "remaining-availability.json"
  ],
  "evidence": {
    "store": "REPO",
    "digest": "sha256:8d29d152af813ad6942dd272c7b8bfb52da332f91af2b605d0efa50ad7ef98a5",
    "media_type": "text/markdown",
    "locator": "6d43121b440743a3b6e9f78b7600a40e4fc5ba7a:qualification/ssds80/PHASE-F-10D-SHADOW-LEDGER-EVIDENCE-SSDS-8.0.md"
  },
  "policy": "sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1",
  "schema_violations": []
}
```

Endpoint comparison:

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/20-final-record-proposals-before.json
```

### 21-prepare-final-finding

```json
{
  "at": "2026-10-29T10:40:55.602694+00:00",
  "step": "21-prepare-final-finding",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "report",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system",
    "--prepare",
    "/tmp/ssds-10d-20261029/remaining-finding.json",
    "--actor",
    "human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

Native command output:

```text
request sha256:75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a
ledger ssdp-shadow-2 at position 3, integration head 6d43121b440743a3b6e9f78b7600a40e4fc5ba7a
signed by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw
records:
  FINDING sha256:6b2dbc477713971c7011ce485b93317d2183dce8e6f4b3c39e9e26e5e61ef014
    target  {"units": ["orchestrator.program", "ssds.manifest", "ssds.policy"]}
    outcome null
adopted deltas: none

prepared in /home/samjin/.ssds/state/ssdp-shadow-2/requests/75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a
sign it with your own key:
  ssh-keygen -Y sign -f <your key> -n ssds /home/samjin/.ssds/state/ssdp-shadow-2/requests/75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a/request-message.txt
then admit it:
  ssds report --ledger ssdp-shadow-2 --repository <repository> --observed-ref <branch> --admit /home/samjin/.ssds/state/ssdp-shadow-2/requests/75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a
```

Endpoint comparison:

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/21-prepare-final-finding-before.json
```

### 22-prepare-final-availability

```json
{
  "at": "2026-10-29T10:40:58.828412+00:00",
  "step": "22-prepare-final-availability",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "submit",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system",
    "--prepare",
    "/tmp/ssds-10d-20261029/remaining-availability.json",
    "--actor",
    "human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

Native command output:

```text
request sha256:bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34
ledger ssdp-shadow-2 at position 3, integration head 6d43121b440743a3b6e9f78b7600a40e4fc5ba7a
signed by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw
records:
  AVAILABILITY sha256:2716f8c4df47515c93b6304a2e1bf96b03c13955102aa4820f4d9925a1ebf9e6
    target  {"digest": "sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1"}
    outcome "AVAILABLE"
adopted deltas: none

prepared in /home/samjin/.ssds/state/ssdp-shadow-2/requests/bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34
sign it with your own key:
  ssh-keygen -Y sign -f <your key> -n ssds /home/samjin/.ssds/state/ssdp-shadow-2/requests/bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34/request-message.txt
then admit it:
  ssds submit --ledger ssdp-shadow-2 --repository <repository> --observed-ref <branch> --admit /home/samjin/.ssds/state/ssdp-shadow-2/requests/bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34
```

Endpoint comparison:

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/22-prepare-final-availability-before.json
```

### 23-report-compatibility

```json
{
  "at": "2026-10-29T11:47:37.822719+00:00",
  "step": "23-report-compatibility",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/verify_report_compatibility.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

Native command output:

```text
{
  "entries": 4,
  "readable_through": 3,
  "record_kinds": {
    "INTAKE_DISPOSITION": 8
  },
  "report_records": 0,
  "historical_report_grammar_migration_needed": false,
  "limit": "This verified ledger only; other deployments with nonconforming historical reports may halt."
}
```

Endpoint comparison:

```text
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/23-report-compatibility-before.json
```

The final requests supersede the earlier unsigned `324bd39e…` preparation, which appended nothing.
The pre-rollout compatibility check verified all four real entries and eight INTAKE_DISPOSITION records,
with no historical report record affected by the stricter vocabulary guard. This says nothing about other
deployments. A new signed request and its actual Admission effects still require human signatures and execution.

## Post-update real-program checks

After the 1,886-test complete-suite PASS (10 skipped), the repaired program verified the exact prepared
requests and current state. Both signatures were absent. All three reserved leaves remain effective,
quarantine is empty, the real ledger is QUALIFIED at position 3 (four entries), with no provisional entry,
critical finding or obligations. This is ledger qualification, not operational/10d/exit acceptance.

### 24-postupdate-prepared-pair

```json
{
  "at": "2026-10-29T12:04:13.060029+00:00",
  "step": "24-postupdate-prepared-pair",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/verify_prepared_pair.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "position": 3,
  "entries": 4,
  "reserved_leaves": {
    "ssds.manifest": "MANIFEST",
    "ssds.policy": "POLICY",
    "ssds.unclassified": "UNCLASSIFIED"
  },
  "quarantine": [],
  "prepared_requests": [
    {
      "request": "sha256:75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a",
      "kind": "FINDING",
      "record": "sha256:6b2dbc477713971c7011ce485b93317d2183dce8e6f4b3c39e9e26e5e61ef014",
      "schema_valid": true,
      "message_matches": true,
      "signature_present": false
    },
    {
      "request": "sha256:bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34",
      "kind": "AVAILABILITY",
      "record": "sha256:2716f8c4df47515c93b6304a2e1bf96b03c13955102aa4820f4d9925a1ebf9e6",
      "schema_valid": true,
      "message_matches": true,
      "signature_present": false
    }
  ]
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/24-postupdate-prepared-pair-before.json
```

### 25-postupdate-status

```json
{
  "at": "2026-10-29T12:04:32.842487+00:00",
  "step": "25-postupdate-status",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "status",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "assertion_withheld": [],
  "critical": [],
  "current_assertion": true,
  "entries": 4,
  "head": {
    "digest": "sha256:3196ae9b755527c66a62dc4ee5691bed9c4fdcbbb59128db668289b258cda8b1",
    "label": "QUALIFIED",
    "position": 3,
    "qualification": "QUALIFIED"
  },
  "ledger_id": "ssdp-shadow-2",
  "obligations": [],
  "provisional": null,
  "qualification": "QUALIFIED",
  "subjects": {
    "orchestrator.program": {
      "mode": "UNGOVERNED",
      "rev": "sha256:b14a3bc958830e5b4982adfb872af4ac7852f18c5414e066c7af0abe6c36db63",
      "status": "unclassified"
    },
    "ssdp.protocol": {
      "mode": "LEGACY",
      "rev": "sha256:0597630d37adb088c58a2c24e0b1402e6853c14e5c9cfbfc73d7f36e73aa27fa",
      "status": "stale"
    },
    "ssds.manifest": {
      "mode": "UNGOVERNED",
      "rev": "sha256:fb77e7dedb294322d49d4f99d3c157fbe52080aaff08833444fecf29f254e3ee",
      "status": "unclassified"
    },
    "ssds.policy": {
      "mode": "UNGOVERNED",
      "rev": "sha256:a0c4b3794237c0a5a73ed364ac23b2f63275c0d0c63b5f81aae2c6e623fa1fa4",
      "status": "unclassified"
    },
    "ssds.unclassified": {
      "mode": "UNGOVERNED",
      "rev": "sha256:dbc260165f64a0e9b4acc0cdc18e9e8df6da2774ff1d587f6b618519fe327355",
      "status": "unclassified"
    },
    "ssds8.manual": {
      "mode": "LEGACY",
      "rev": "sha256:c5090340091ca7c72257d48b6ff327c1a0703d86b88bc1097d81d90a88374b23",
      "status": "stale"
    }
  }
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/25-postupdate-status-before.json
```

## Canonical-string repair: real identity regression

After full-suite PASS (1,888 tests, 10 skipped), isolated SSDS reads with the byte-preserving string repair
returned exactly the same parsed status and prepared-request reports as steps 24/25. Native signatures and
record/message identities still verify; both requests remain unsigned. This qualifies only these read windows.

### 26-jcs-prepared-pair

```json
{
  "at": "2026-10-29T12:53:19.018302+00:00",
  "step": "26-jcs-prepared-pair",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/verify_prepared_pair.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "position": 3,
  "entries": 4,
  "reserved_leaves": {
    "ssds.manifest": "MANIFEST",
    "ssds.policy": "POLICY",
    "ssds.unclassified": "UNCLASSIFIED"
  },
  "quarantine": [],
  "prepared_requests": [
    {
      "request": "sha256:75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a",
      "kind": "FINDING",
      "record": "sha256:6b2dbc477713971c7011ce485b93317d2183dce8e6f4b3c39e9e26e5e61ef014",
      "schema_valid": true,
      "message_matches": true,
      "signature_present": false
    },
    {
      "request": "sha256:bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34",
      "kind": "AVAILABILITY",
      "record": "sha256:2716f8c4df47515c93b6304a2e1bf96b03c13955102aa4820f4d9925a1ebf9e6",
      "schema_valid": true,
      "message_matches": true,
      "signature_present": false
    }
  ]
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/26-jcs-prepared-pair-before.json
```

### 27-jcs-status

```json
{
  "at": "2026-10-29T12:53:26.968077+00:00",
  "step": "27-jcs-status",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "status",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "assertion_withheld": [],
  "critical": [],
  "current_assertion": true,
  "entries": 4,
  "head": {
    "digest": "sha256:3196ae9b755527c66a62dc4ee5691bed9c4fdcbbb59128db668289b258cda8b1",
    "label": "QUALIFIED",
    "position": 3,
    "qualification": "QUALIFIED"
  },
  "ledger_id": "ssdp-shadow-2",
  "obligations": [],
  "provisional": null,
  "qualification": "QUALIFIED",
  "subjects": {
    "orchestrator.program": {
      "mode": "UNGOVERNED",
      "rev": "sha256:b14a3bc958830e5b4982adfb872af4ac7852f18c5414e066c7af0abe6c36db63",
      "status": "unclassified"
    },
    "ssdp.protocol": {
      "mode": "LEGACY",
      "rev": "sha256:0597630d37adb088c58a2c24e0b1402e6853c14e5c9cfbfc73d7f36e73aa27fa",
      "status": "stale"
    },
    "ssds.manifest": {
      "mode": "UNGOVERNED",
      "rev": "sha256:fb77e7dedb294322d49d4f99d3c157fbe52080aaff08833444fecf29f254e3ee",
      "status": "unclassified"
    },
    "ssds.policy": {
      "mode": "UNGOVERNED",
      "rev": "sha256:a0c4b3794237c0a5a73ed364ac23b2f63275c0d0c63b5f81aae2c6e623fa1fa4",
      "status": "unclassified"
    },
    "ssds.unclassified": {
      "mode": "UNGOVERNED",
      "rev": "sha256:dbc260165f64a0e9b4acc0cdc18e9e8df6da2774ff1d587f6b618519fe327355",
      "status": "unclassified"
    },
    "ssds8.manual": {
      "mode": "LEGACY",
      "rev": "sha256:c5090340091ca7c72257d48b6ff327c1a0703d86b88bc1097d81d90a88374b23",
      "status": "stale"
    }
  }
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/27-jcs-status-before.json
```


## Signed remaining-record pair: actual results and corrected report

Authority: stakeholder record item 73, exact instruction "Signed. Proceed." Asserter: AI implementing agent,
Codex family. Actual program results are bounded; neither accepted signatures nor green boundary comparisons
waive the original append gap or establish full Manual conformance.

- Position 4 absorbed observed HEAD `425c92581c0431efd0d4084a9e13bdde93175506`.
- Position 5: original signed FINDING request `sha256:75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a`
  was REJECTED, record not admitted, code SECRET_DETECTED. Authenticated carrier request id:
  `sha256:f78c8d1b2dfa83006995de494e727f6bbdc5cb29b1b7af7afa47feea49e4a20b`.
- Position 6: signed AVAILABILITY request `sha256:bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34`
  was ACCEPTED with one record, no refusal. Authenticated carrier id:
  `sha256:e248396b25fd761756adcf3411c6890d24ca1be767a42e402084141d412446ac`.
  The real derivation owner reports latest policy-object availability AVAILABLE. Three reserved leaves remain
  effective, quarantine empty. Program status reports QUALIFIED at position 6 (seven entries), no critical or
  provisional entry. This describes the implemented reader, subject to the C7 gap below.

**Preparation defect and bounded correction.** Initial preparation checked schema but did not rehearse the full
Admission scan. Metadata-only diagnosis located the entropy hit solely in refs[0].locator: 67 characters,
4.7729 bits/character, no known-credential-pattern match. No matched secret material was printed. The corrected
locator is the native Git blob `9f6d5616f995b04d62c2a87e777005df903347ef`, independently verified to hold exactly
the original immutable evidence bytes (SHA-256 `8d29d152af813ad6942dd272c7b8bfb52da332f91af2b605d0efa50ad7ef98a5`).
Its containing commit `6d43121b` remains reachable in the ledger. Catalogue §3.2's REPO reference is a blob in
a commit kept reachable; no scanner exemption or policy was added, and no source code changed.

**R-PROVENANCE-C7 — MATERIAL D4 blocker; no Serious Challenge.** Full-record review found that both original
proposals used observation/claim_limit/next_question and preparation narrative in provenance. Accepted Manual
§3.2/C7 forbids free-text record fields; §15.1 routes report narrative to its canonical home. The catalogue's
execution-provenance examples need not be an exhaustive key grammar to establish that restriction. The current
`ledger/schema.py` common-envelope validator accepts any dict, and the request fixture explicitly permits a
free-form note; those are implementation facts, not authority. The already admitted AVAILABILITY record has
provenance keys claim_limit, observation, prepared_by, status. It remains an authenticated program-accepted
observation with a real C7 conformance gap, not a conformant record by inference from its ACCEPT result.

Route this to the existing D4 envelope validator and preparation owners. Resolve enforcement and safe treatment
of already admitted nonconforming data through the governing schema/lifecycle owners before deploying a fix.
Do not rewrite the record, silently grandfather it, claim schema conformance, or retroactively deploy a stricter
reader that halts this ledger without governed handling. No source/schema/authority change was made in this turn.
This reopens step 2's affected provenance-enforcement closure; 10d/exit remain incomplete.

The corrected FINDING has provenance:null: all narrative stays in the exact same referenced evidence blob and
readable signing brief. Other changes are locator and informational timestamp only. Target units, materiality,
non-blocking flag, INSPECTABILITY_GAP reason and supersedes:[] are unchanged. The new request is
`sha256:785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd`, record
`sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307`, at base position 6.
It is unsigned and unsubmitted; the old signature is not valid for changed bytes and is not reused.

Fresh Codex review: locator-only intermediate NO-PASS on inherited provenance; final typed replacement PASS
for unsigned preparation. Final validation log explicitly lists all three changed fields; final scratch real-
Admission rehearsal ran one test in 0.688 seconds, OK: old locator refused, typed blob-reference report ACCEPTED.
The scratch used a new throwaway human key and fixture guide target; it proves the exercised scanner/Admission
path, not actual future signed admission. Final checked-home verification confirms exact request/message id,
no signature, provenance:null, schema valid and scanner false. Production source remains at validated `1abf37cf`;
the prior 1,888-test execution remains source-applicable but does not prove C7 conformance. No new scientific
results, scientific gate evidence or scientific selection occurred; infrastructure proposal variants are retained.

### Native commands and endpoint comparisons

Command 28 intentionally retains exit 1/REJECT; comparison exit 0 is not command success. All later commands
and comparisons below exited 0. Each complete window ran in one host context without concurrent restricted
filesystem or agent probes. These windows qualify only themselves, not the original contaminated append.

#### 28-admit-signed-finding

```json
{
  "at": "2026-10-29T20:46:29.596741+00:00",
  "step": "28-admit-signed-finding",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "report",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system",
    "--observed-ref",
    "ssds-8.0-graph-native-architecture",
    "--admit",
    "/home/samjin/.ssds/state/ssdp-shadow-2/requests/75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a"
  ],
  "command_exit": 1,
  "comparison_exit": 0
}
```

```text
{
  "admitted": [],
  "appended": true,
  "decision": "REJECT",
  "ledger_id": "ssdp-shadow-2",
  "observed_ref": "ssds-8.0-graph-native-architecture",
  "position": 5,
  "reasons": [],
  "refused": [
    [
      "sha256:6b2dbc477713971c7011ce485b93317d2183dce8e6f4b3c39e9e26e5e61ef014",
      [
        "SECRET_DETECTED"
      ]
    ]
  ],
  "request_id": "sha256:f78c8d1b2dfa83006995de494e727f6bbdc5cb29b1b7af7afa47feea49e4a20b",
  "submitted": "request sha256:75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a\nledger ssdp-shadow-2 at position 3, integration head 6d43121b440743a3b6e9f78b7600a40e4fc5ba7a\nsigned by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw\nrecords:\n  FINDING sha256:6b2dbc477713971c7011ce485b93317d2183dce8e6f4b3c39e9e26e5e61ef014\n    target  {\"units\": [\"orchestrator.program\", \"ssds.manifest\", \"ssds.policy\"]}\n    outcome null\nadopted deltas: none\n"
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/28-admit-signed-finding-before.json
```

#### 29-admit-signed-availability

```json
{
  "at": "2026-10-29T20:47:59.082358+00:00",
  "step": "29-admit-signed-availability",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "submit",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system",
    "--observed-ref",
    "ssds-8.0-graph-native-architecture",
    "--admit",
    "/home/samjin/.ssds/state/ssdp-shadow-2/requests/bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "admitted": [
    "sha256:2716f8c4df47515c93b6304a2e1bf96b03c13955102aa4820f4d9925a1ebf9e6"
  ],
  "appended": true,
  "decision": "ACCEPT",
  "ledger_id": "ssdp-shadow-2",
  "observed_ref": "ssds-8.0-graph-native-architecture",
  "position": 6,
  "reasons": [],
  "refused": [],
  "request_id": "sha256:e248396b25fd761756adcf3411c6890d24ca1be767a42e402084141d412446ac",
  "submitted": "request sha256:bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34\nledger ssdp-shadow-2 at position 3, integration head 6d43121b440743a3b6e9f78b7600a40e4fc5ba7a\nsigned by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw\nrecords:\n  AVAILABILITY sha256:2716f8c4df47515c93b6304a2e1bf96b03c13955102aa4820f4d9925a1ebf9e6\n    target  {\"digest\": \"sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1\"}\n    outcome \"AVAILABLE\"\nadopted deltas: none\n"
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/29-admit-signed-availability-before.json
```

#### 30-prepare-corrected-finding

```json
{
  "at": "2026-10-29T20:56:18.791970+00:00",
  "step": "30-prepare-corrected-finding",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "report",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system",
    "--prepare",
    "/tmp/ssds-10d-20261029/replacement-finding-v2.json",
    "--actor",
    "human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
request sha256:785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd
ledger ssdp-shadow-2 at position 6, integration head 425c92581c0431efd0d4084a9e13bdde93175506
signed by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw
records:
  FINDING sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307
    target  {"units": ["orchestrator.program", "ssds.manifest", "ssds.policy"]}
    outcome null
adopted deltas: none

prepared in /home/samjin/.ssds/state/ssdp-shadow-2/requests/785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd
sign it with your own key:
  ssh-keygen -Y sign -f <your key> -n ssds /home/samjin/.ssds/state/ssdp-shadow-2/requests/785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd/request-message.txt
then admit it:
  ssds report --ledger ssdp-shadow-2 --repository <repository> --observed-ref <branch> --admit /home/samjin/.ssds/state/ssdp-shadow-2/requests/785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/30-prepare-corrected-finding-before.json
```

#### 31-verify-signed-record-effects

```json
{
  "at": "2026-10-29T20:56:22.295500+00:00",
  "step": "31-verify-signed-record-effects",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/verify_signed_record_effects.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "position": 6,
  "entries": 7,
  "observed_head": "425c92581c0431efd0d4084a9e13bdde93175506",
  "entry_kinds": {
    "LIFECYCLE": 1,
    "ABSORPTION": 3,
    "ADMISSION": 3
  },
  "finding_admitted": false,
  "availability_admitted": true,
  "latest_policy_availability": "AVAILABLE",
  "reserved_leaves": {
    "ssds.manifest": "MANIFEST",
    "ssds.policy": "POLICY",
    "ssds.unclassified": "UNCLASSIFIED"
  },
  "quarantine": [],
  "evidence_commit_reachable_in_ledger": true
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/31-verify-signed-record-effects-before.json
```

#### 32-status-after-signed-pair

```json
{
  "at": "2026-10-29T20:56:30.427702+00:00",
  "step": "32-status-after-signed-pair",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "status",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "assertion_withheld": [],
  "critical": [],
  "current_assertion": true,
  "entries": 7,
  "head": {
    "digest": "sha256:ff0d3e37811f46dfa98a7d725e48115e750102d32f4097d1729daf95f5a62f7d",
    "label": "QUALIFIED",
    "position": 6,
    "qualification": "QUALIFIED"
  },
  "ledger_id": "ssdp-shadow-2",
  "obligations": [],
  "provisional": null,
  "qualification": "QUALIFIED",
  "subjects": {
    "orchestrator.program": {
      "mode": "UNGOVERNED",
      "rev": "sha256:b0a1898f4cbcad5c134e1274ae2bd752137052a1d823c8952d18d19c2f12f8c2",
      "status": "unclassified"
    },
    "ssdp.protocol": {
      "mode": "LEGACY",
      "rev": "sha256:0597630d37adb088c58a2c24e0b1402e6853c14e5c9cfbfc73d7f36e73aa27fa",
      "status": "stale"
    },
    "ssds.manifest": {
      "mode": "UNGOVERNED",
      "rev": "sha256:fb77e7dedb294322d49d4f99d3c157fbe52080aaff08833444fecf29f254e3ee",
      "status": "unclassified"
    },
    "ssds.policy": {
      "mode": "UNGOVERNED",
      "rev": "sha256:a0c4b3794237c0a5a73ed364ac23b2f63275c0d0c63b5f81aae2c6e623fa1fa4",
      "status": "unclassified"
    },
    "ssds.unclassified": {
      "mode": "UNGOVERNED",
      "rev": "sha256:320739ca3300644e9aba0e4829624cd1aaeae73a27305490f644ab55cfbbcf21",
      "status": "unclassified"
    },
    "ssds8.manual": {
      "mode": "LEGACY",
      "rev": "sha256:c5090340091ca7c72257d48b6ff327c1a0703d86b88bc1097d81d90a88374b23",
      "status": "stale"
    }
  }
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/32-status-after-signed-pair-before.json
```

#### 33-verify-corrected-finding

```json
{
  "at": "2026-10-29T20:58:17.359166+00:00",
  "step": "33-verify-corrected-finding",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/verify_corrected_finding.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "replacement_request": "sha256:785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd",
  "record": "sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307",
  "message_matches": true,
  "signature_present": false,
  "schema_valid": true,
  "secret_detected": false,
  "provenance": null,
  "same_narrative_home": true,
  "non_null_admitted_provenance": [
    {
      "kind": "AVAILABILITY",
      "record": "sha256:2716f8c4df47515c93b6304a2e1bf96b03c13955102aa4820f4d9925a1ebf9e6",
      "provenance_keys": [
        "claim_limit",
        "observation",
        "prepared_by",
        "status"
      ]
    }
  ],
  "limit": "Program acceptance is not Manual C7 conformance; old AVAILABILITY is preserved."
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/33-verify-corrected-finding-before.json
```

#### replacement-locator-validation-final.log

```text
{
  "blob": "9f6d5616f995b04d62c2a87e777005df903347ef",
  "content_digest": "sha256:8d29d152af813ad6942dd272c7b8bfb52da332f91af2b605d0efa50ad7ef98a5",
  "changed_fields": [
    "refs[0].locator",
    "recorded_at",
    "provenance"
  ],
  "same_evidence_bytes": true,
  "same_claim": true,
  "schema_valid": true,
  "secret_detected": false
}
```

#### replacement-locator-rehearsal-final.log

```text
.
----------------------------------------------------------------------
Ran 1 test in 0.688s

OK
{"rehearsal": "fresh throwaway-key fixture, target guide", "old_locator": "SECRET_DETECTED", "blob_locator": "ACCEPT", "real_home_access": false, "production_changes": false}
```


## Corrected FINDING accepted; proposed signed decide-refusal

Authority: stakeholder "Done. Proceed." after signing the exact corrected request; stakeholder record item 74.
Corrected FINDING request `sha256:785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd`
was ACCEPTED at **position 8**, record `sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307`,
authenticated carrier `sha256:766a297e57a060d1b2f21344961cb3818386a87aa394b04b7b7a8510132a4b01`.
Position 7 absorbed product HEAD `43e9af64e232e35ff4d6b026e32b490b057e8221`. No other record was admitted.
The actual append comparison passed. The original repair's FAILED/contaminated window stays unchanged.

The real derivation owner confirms the corrected record has provenance:null, expected target/materiality/
non-blocking flag and exact narrative blob. It derives the OPEN, HUMAN-held attention obligation
`sha256:a6dfe322ed404619dfef8b48d39eb45f2daa93a3e26196f5bab9e0cbfbbe5875`. Program state is QUALIFIED at
position 8, nine entries, no provisional/critical finding, empty quarantine, policy availability AVAILABLE.
The accepted AVAILABILITY provenance-C7 conformance gap remains; this implemented status is not full Manual
conformance or 10d/exit acceptance. No source, policy, authority or historical record was changed.

### Proposed ACKNOWLEDGE carrier, not yet a human decision

F122 still requires a genuinely signed `decide` request refused at entry. The agent proposes ACKNOWLEDGE on
the actual attention obligation, with identity basis on the admitted FINDING, provenance:null, refs:[], fields:{},
no candidates/adoption and no narrative fields. This is an unsigned proposal for human review, not a choice
already made by the stakeholder. Its request is `sha256:11c18b81ea93d1eae3e084ce6ce79268995209d821ea89cdca535d35ac446be8`,
record `sha256:1ae2a28268b3bfd24cdf6cb451ec3cd0d95d824d63683ecb1c0a16abc12386fd`, prepared at position 8.

If admitted, a HUMAN_DECISION on this obligation would resolve its attention (§15.2; Reports._resolved_by_human),
regardless of outcome. It would not establish technical qualification of the original append or fix C7. The
current Phase F boundary instead refuses this kind before validation/authentication; expected rejection must
leave both the entry count and attention OPEN. The preview string alone is not actual signed-refusal evidence.

Before the future real test, independently verify the human signature with the registered in-force public key
through the SSDS signature API; boundary refusal itself cannot prove authentication. Observe/absorb any moved
branch first in its own bounded window, then capture the no-append baseline. Submit native `ssds decide --admit`
in an isolated window: native exit 1 is expected only with the specific boundary-refusal result, comparison 0,
verified no entry appended and the exact attention still OPEN. An unexpected admission or other outcome fails
the test; preserve and route it rather than silently correcting data. Do not infer actual disposition or waiver
from this proposal or its expected refusal. A signed/endorsed intent must be recorded separately in the stakeholder
home because a refused request is not an admitted decision.

Fresh Codex review: PASS for unsigned preparation, no blocker or Serious Challenge, with the above limits.
Final scratch rehearsal: one test in 1.105 seconds, OK. It first admitted a MATERIAL finding, derived its real
fixture attention, prepared this typed shape against that identity, signed with a fresh fixture key, independently
verified SSHSIG, then exercised the real composition boundary. Entries stayed 4 -> 4 and attention OPEN.
The rehearsal uses its own fixture product, ruleset, code target and fresh key; only its home resolver is mocked. No real home/key or live model was used. This proves
the exercised fixture path, not the still-unexecuted real signed test. Schema/scanner and checked-home message
checks pass; the actual proposed workspace has no signature and no decision was submitted. Infrastructure only:
no scientific results, scientific gate evidence or scientific outcome/parameter selection.

### Native windows

All steps 34–38 exited command 0/comparison 0, sequentially in one host context per window, with no concurrent
restricted filesystem or agent probes. Preparation and verification appended nothing.

#### 34-admit-corrected-finding

```json
{
  "at": "2026-10-29T21:06:22.023454+00:00",
  "step": "34-admit-corrected-finding",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "report",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system",
    "--observed-ref",
    "ssds-8.0-graph-native-architecture",
    "--admit",
    "/home/samjin/.ssds/state/ssdp-shadow-2/requests/785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "admitted": [
    "sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307"
  ],
  "appended": true,
  "decision": "ACCEPT",
  "ledger_id": "ssdp-shadow-2",
  "observed_ref": "ssds-8.0-graph-native-architecture",
  "position": 8,
  "reasons": [],
  "refused": [],
  "request_id": "sha256:766a297e57a060d1b2f21344961cb3818386a87aa394b04b7b7a8510132a4b01",
  "submitted": "request sha256:785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd\nledger ssdp-shadow-2 at position 6, integration head 425c92581c0431efd0d4084a9e13bdde93175506\nsigned by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw\nrecords:\n  FINDING sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307\n    target  {\"units\": [\"orchestrator.program\", \"ssds.manifest\", \"ssds.policy\"]}\n    outcome null\nadopted deltas: none\n"
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/34-admit-corrected-finding-before.json
```

#### 35-verify-corrected-finding-effects

```json
{
  "at": "2026-10-29T21:09:31.096458+00:00",
  "step": "35-verify-corrected-finding-effects",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/verify_corrected_finding_effects.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "position": 8,
  "entries": 9,
  "finding_admitted": true,
  "finding_record": "sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307",
  "finding_provenance": null,
  "quarantine": [],
  "latest_policy_availability": "AVAILABLE",
  "attention": {
    "kind": "HUMAN_ATTENTION",
    "target_json": "{\"report\": \"sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307\"}",
    "params_json": "{\"materiality\": \"MATERIAL\"}",
    "id": "sha256:a6dfe322ed404619dfef8b48d39eb45f2daa93a3e26196f5bab9e0cbfbbe5875",
    "holder": "HUMAN",
    "plan": null,
    "detail": ""
  },
  "attention_discharge": "OPEN",
  "limit": "This is implemented-state evidence; original boundary and provenance-C7 gaps remain open."
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/35-verify-corrected-finding-effects-before.json
```

#### 36-status-after-corrected-finding

```json
{
  "at": "2026-10-29T21:09:40.032643+00:00",
  "step": "36-status-after-corrected-finding",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "status",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "assertion_withheld": [],
  "critical": [],
  "current_assertion": true,
  "entries": 9,
  "head": {
    "digest": "sha256:243dd9205d993d2c2b083e88bf4d78c784ef2cf53458e0f3145e79ddc83772f1",
    "label": "QUALIFIED",
    "position": 8,
    "qualification": "QUALIFIED"
  },
  "ledger_id": "ssdp-shadow-2",
  "obligations": [
    {
      "discharge": "OPEN",
      "holder": "HUMAN",
      "id": "sha256:a6dfe322ed404619dfef8b48d39eb45f2daa93a3e26196f5bab9e0cbfbbe5875",
      "kind": "HUMAN_ATTENTION",
      "plan": null,
      "readiness": "READY",
      "target": {
        "report": "sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307"
      }
    }
  ],
  "provisional": null,
  "qualification": "QUALIFIED",
  "subjects": {
    "orchestrator.program": {
      "mode": "UNGOVERNED",
      "rev": "sha256:b0a1898f4cbcad5c134e1274ae2bd752137052a1d823c8952d18d19c2f12f8c2",
      "status": "unclassified"
    },
    "ssdp.protocol": {
      "mode": "LEGACY",
      "rev": "sha256:0597630d37adb088c58a2c24e0b1402e6853c14e5c9cfbfc73d7f36e73aa27fa",
      "status": "stale"
    },
    "ssds.manifest": {
      "mode": "UNGOVERNED",
      "rev": "sha256:fb77e7dedb294322d49d4f99d3c157fbe52080aaff08833444fecf29f254e3ee",
      "status": "unclassified"
    },
    "ssds.policy": {
      "mode": "UNGOVERNED",
      "rev": "sha256:a0c4b3794237c0a5a73ed364ac23b2f63275c0d0c63b5f81aae2c6e623fa1fa4",
      "status": "unclassified"
    },
    "ssds.unclassified": {
      "mode": "UNGOVERNED",
      "rev": "sha256:8dec81f5e79811598cacb623b622c689fea6cd68149f6c513077da0ed7b3b9bc",
      "status": "unclassified"
    },
    "ssds8.manual": {
      "mode": "LEGACY",
      "rev": "sha256:c5090340091ca7c72257d48b6ff327c1a0703d86b88bc1097d81d90a88374b23",
      "status": "stale"
    }
  }
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/36-status-after-corrected-finding-before.json
```

#### 37-prepare-proposed-decide

```json
{
  "at": "2026-10-29T21:14:29.575021+00:00",
  "step": "37-prepare-proposed-decide",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/ssds",
    "decide",
    "--ledger",
    "ssdp-shadow-2",
    "--repository",
    "/home/samjin/agent-skills/scientific-software-development-system",
    "--prepare",
    "/tmp/ssds-10d-20261029/proposed-decide-acknowledge.json",
    "--actor",
    "human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
request sha256:11c18b81ea93d1eae3e084ce6ce79268995209d821ea89cdca535d35ac446be8
ledger ssdp-shadow-2 at position 8, integration head 43e9af64e232e35ff4d6b026e32b490b057e8221
signed by human:SHA256:Xar4qv2hBwt+ulw0qzilYWzp5ckynnyWMLYm+kZl6lw
records:
  HUMAN_DECISION sha256:1ae2a28268b3bfd24cdf6cb451ec3cd0d95d824d63683ecb1c0a16abc12386fd
    target  {"obligation": "sha256:a6dfe322ed404619dfef8b48d39eb45f2daa93a3e26196f5bab9e0cbfbbe5875"}
    outcome "ACKNOWLEDGE"
adopted deltas: none

prepared in /home/samjin/.ssds/state/ssdp-shadow-2/requests/11c18b81ea93d1eae3e084ce6ce79268995209d821ea89cdca535d35ac446be8
sign it with your own key:
  ssh-keygen -Y sign -f <your key> -n ssds /home/samjin/.ssds/state/ssdp-shadow-2/requests/11c18b81ea93d1eae3e084ce6ce79268995209d821ea89cdca535d35ac446be8/request-message.txt
then admit it:
  ssds decide --ledger ssdp-shadow-2 --repository <repository> --observed-ref <branch> --admit /home/samjin/.ssds/state/ssdp-shadow-2/requests/11c18b81ea93d1eae3e084ce6ce79268995209d821ea89cdca535d35ac446be8
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/37-prepare-proposed-decide-before.json
```

#### 38-verify-proposed-decide

```json
{
  "at": "2026-10-29T21:16:01.026029+00:00",
  "step": "38-verify-proposed-decide",
  "command": [
    "/tmp/ssds-phase-f-20261029/bin/python",
    "/tmp/ssds-10d-20261029/verify_proposed_decide.py"
  ],
  "command_exit": 0,
  "comparison_exit": 0
}
```

```text
{
  "request": "sha256:11c18b81ea93d1eae3e084ce6ce79268995209d821ea89cdca535d35ac446be8",
  "record": "sha256:1ae2a28268b3bfd24cdf6cb451ec3cd0d95d824d63683ecb1c0a16abc12386fd",
  "position": 8,
  "entries": 9,
  "message_matches": true,
  "signature_present": false,
  "schema_valid": true,
  "secret_detected": false,
  "provenance": null,
  "proposed_outcome": "ACKNOWLEDGE",
  "actual_attention": "sha256:a6dfe322ed404619dfef8b48d39eb45f2daa93a3e26196f5bab9e0cbfbbe5875",
  "attention_discharge": "OPEN",
  "entry_policy_preview": "a HUMAN_DECISION record: its checks belong to a later phase (F1)",
  "human_endorsement": "not yet given",
  "real_signed_refusal": "unexecuted"
}
/home/samjin/agent-skills/scientific-software-development-system: unchanged since /tmp/ssds-10d-20261029/38-verify-proposed-decide-before.json
```

#### proposed-decide-validation.log

```text
{
  "status": "proposed-for-human-review-not-yet-endorsed",
  "outcome": "ACKNOWLEDGE",
  "obligation": "sha256:a6dfe322ed404619dfef8b48d39eb45f2daa93a3e26196f5bab9e0cbfbbe5875",
  "finding": "sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307",
  "provenance": null,
  "schema_valid": true,
  "secret_detected": false,
  "intended_use": "signed Phase-F boundary-refusal exercise; no admitted resolution expected"
}
```

#### proposed-decide-rehearsal.log

```text
.
----------------------------------------------------------------------
Ran 1 test in 1.105s

OK
{"fixture_signature_verified": true, "boundary_refused": true, "entries_before": 4, "entries_after": 4, "attention_discharge": "OPEN", "real_home_access": false}
```

#### Future read-only signature verifier

Not executed while the proposal is unsigned. Run through the same isolated SSDS wrapper after the human signs.
It prints only verification metadata, no key/signature contents.

```python
"""Run only after the human signs; read through SSDS, print no signature/key material."""
import json
from pathlib import Path
from ssds.admission.request import request_id, request_message
from ssds.cli import Composition, canonical_signature
from ssds.derivation import trust_roots
from ssds.ledger.signatures import verify_sshsig

rid = 'sha256:11c18b81ea93d1eae3e084ce6ce79268995209d821ea89cdca535d35ac446be8'
c = Composition('ssdp-shadow-2',Path('/home/samjin/agent-skills/scientific-software-development-system'))
chain = c.access.chain()
assert chain.halt is None
state = c.state()
req = json.loads(state.read_private(c.request_parts(rid,'request.json')))
assert request_id(req) == rid and req['binding'] is None and len(req['records']) == 1
message = request_message(req)
assert state.read_private(c.request_parts(rid,'request-message.txt')) == message
raw_signature = state.read_private(c.request_parts(rid,'request-message.txt.sig'))
assert raw_signature is not None, 'human signature is still required'
actor = req['records'][0]['actor']
public = trust_roots(chain.entries[:chain.readable_through+1]).humans[actor]
assert verify_sshsig(public,message,canonical_signature(raw_signature.decode('ascii'))), 'invalid signature'
print(json.dumps({'request':rid,'actor':actor,'signature_verified':True,'namespace':'ssds',
                  'limit':'Read-only authentication evidence; no submission, append or resolution.'},indent=2))
```
