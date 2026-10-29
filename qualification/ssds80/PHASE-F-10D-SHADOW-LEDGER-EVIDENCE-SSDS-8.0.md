# SSDS 8 Phase F 10d — real shadow-ledger evidence (partial; qualification gap)

Governing SSDP: 7.2.1. Plan: revision 57, F122, SD-69; stakeholder authorization is item 72 of
`STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` (2026-10-29).
Asserter: AI implementing agent, Codex family. This is infrastructure execution evidence, not scientific gate evidence.

**Status: signed adoption ACCEPTED at position 2; 10d remains incomplete.** Eight `INTAKE_DISPOSITION ABSORB`
records are admitted; all three reserved leaves are effective, quarantine is empty, and the policy digest is unchanged.
The ledger is QUALIFIED with three entries and no provisional entry or critical finding. No native authority or campaign.

**Qualification gap:** the first actual append's command returned ACCEPT/exit 0, but its endpoint comparison failed
(exit 1), reporting repository-root modification/change metadata. Concurrent restricted tool calls were launched by
the implementing agent during that escalated-host command window. Restricted tools expose `.agents`, `.codex` and
`.aws` as read-only tmpfs mounts; their setup/removal changes root metadata. Snapshot history confirms the execution
views differ. No SSDS-caused product write was established. The original window remains FAILED/contaminated and
cannot support an unqualified unchanged claim. Independent review identified no Serious Challenge; it permitted
independent state/restart checks with this gap retained. A clean isolated no-op, idempotent replay, inspection,
restarts, Dispatcher observation and candidate refusal do not retroactively qualify that original append path.

The later report/submit records remain unchosen and unexecuted; the signed decide-refusal exercise, frozen study,
classification and exit review also remain pending. Unqualified 10d/exit closure requires disposition of the gap.

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
