# SSDS Level 0 Core — user guide

The `ssds` program's Level 0 Core (`ssds.core`) turns “which Protocol prompt do I need right now, filled
in correctly for this repository?” into one command. It resolves mechanically
knowable repository, candidate, workplan, Protocol-profile, and prompt context,
while leaving genuine semantic decisions to the user or receiving agent.

Core works alone. It has no history database, agent runner, model catalog, quota
meter, or scheduler, and it does not need them.

The current default is **Scientific Software Development Protocol 6.2** using
profile `ssdp-protocol-6.2` and profile schema v2. Frozen Protocol 6.1 and 6.0
profiles remain packaged under schema v2, while `sdp-protocol-5.16` remains
packaged under schema v1 for older workplans. Core selects workflow semantics
from the compatible profile; it does not reinterpret an older workplan through
6.2 merely because the installed Core is newer.

---

## 1. Install

`ssds` needs Python 3.11 or newer, on both paths below. Check with
`python3 --version`. Where the system `python3` is older, create a virtual
environment from a newer interpreter you have (for example `python3.13`, or one
from a conda or `uv` installation) and use that environment's `python` and
`pip` for every command here:

```bash
python3.13 -m venv ~/.venvs/ssds
~/.venvs/ssds/bin/pip install ./orchestrator
~/.venvs/ssds/bin/ssds doctor
```

Checkout development does not require installing the package. The zero-install
path uses the same CLI owner from the current checkout:

```bash
python3 orchestrator/bin/ssds --help
python3 orchestrator/bin/ssds doctor --config /path/to/config.toml
python3 orchestrator/bin/ssds software-implementation --config /path/to/config.toml --prompt-mode local
```

`orchestrator/bin/ssds` only places the checkout's `src/` tree first and delegates
to the program's composition root, `ssds.cli:main`; it contains no command or product logic.
It still needs the distribution's dependencies in the interpreter that runs it.

For an installed console script:

```bash
pip install ./orchestrator                 # from a checkout of this repository
pip install "./orchestrator[clipboard]"    # optional --copy support
ssds doctor
```

`ssds doctor` reports readiness without importing extension code, touching the
network, or modifying a target repository. Its `packaged_profiles` field shows
the shipped Protocol 6 and Protocol 5.16 profile identities, schema versions,
and stage sets.

---

## 2. Configure

Configuration is one TOML file, `config.toml` in the SSDS home: `$SSDS_HOME` if set
(an absolute path), otherwise `~/.ssds`. `--config` overrides it. Everything SSDS
writes for an operator lives in that home, outside every repository. The home is
created the first time SSDS writes there; `ssds doctor` names it and, until a
configuration exists, says where to create one. Before writing, SSDS reads every
directory it uses in the home in full. It refuses, writing nothing, if one of
them cannot be listed, contains a symbolic link or anything other than plain
files and directories, or contains a repository other than the ledger's own.

**Back up the SSDS home.** It holds what no repository clone carries: each
project's ledger repository (`ledgers/`), the local witness's checkpoints
(`witness/`), high-water marks (`state/`) and the Admission host keys (`keys/`).
Copy the whole directory, with its permissions, to a medium that is not rolled
back together with the machine; keep the copy as private as the keys in it. A
restored copy that is older than a witnessed checkpoint is reported as a rollback,
never silently treated as current.

A normal current Protocol 6 project needs only the project entry. Explicitly
naming the current profile is useful for clarity but optional because Protocol 6
is the Core default:

```toml
schema_version = 1

[core]
default_project = "mdstats"      # optional
default_prompt_mode = "web"      # optional; built-in default is web

[projects.mdstats]
repo = "/absolute/path/to/mdstats"
protocol_profile = "ssdp-protocol-6.2"   # optional; this is the current default
default_prompt_mode = "web"      # optional, per project
remote_name = "origin"           # optional; a remote name, never a credential URL

[extensions."some.extension"]
# extension-owned data; Core preserves it but does not interpret it
```

With no `[protocol_sources.*]` entry, Core uses the exact packaged snapshot for
the selected profile. To use a compatible local Protocol checkout instead:

```toml
[protocol_sources."ssdp-protocol-6.2"]
local_root = "/path/to/software-development-protocol"
```

The checkout must actually contain compatible Protocol 6 canonical source. A
source whose version and prompt/profile content disagree is rejected rather than
mixed.

Remote Protocol reads are opt-in and require both an explicit repository and an
explicit ref. They are bounded, read-only source reads; the ref is resolved to
one immutable commit and revalidated. Do not use `main`/latest as a substitute
for historical version identity.

```toml
[protocol_sources."ssdp-protocol-6.2"]
allow_remote = true
remote_repository = "<credential-free compatible Git repository>"
remote_ref = "<explicit evidence-backed ref>"
```

Core-owned sections are **closed**: an unrecognized key is rejected. API tokens
and passwords therefore have no normal field in this file; use established Git
credential mechanisms instead. A `repo` or `remote_repository` URL containing
embedded credentials is rejected.

`[extensions."<ns>"]` is the one open section. Configuration for extensions that
are not installed is preserved and reported by `ssds doctor` as inactive. It does
not affect Core project, preparation, or prompt identity.

### Which project?

When `--project` is omitted:

```text
the unique configured project whose worktree contains the current directory
  -> [core].default_project
  -> the sole configured project
  -> core.project.ambiguous / core.project.not_found
```

There is no fuzzy matching. Ambiguity is reported, never guessed.

---

## 3. Protocol 6 workflow and commands

Protocol 6 represents four semantic domains plus review/verification/maintenance
operations:

```text
intake
  -> D1 scientific-formulation
  -> D2 numerical-algorithm-design
  -> D3 software-design
  -> D4 software-implementation
  -> review / verification / stabilization / alignment / health-audit / closeout
```

This is not a requirement to execute every domain for every task. The profile
supports reduced routes: start at the highest potentially affected domain and
skip unaffected upstream domains when that exclusion is justified.

Typical current commands:

```bash
ssds intake --task "add a new scientific capability"
ssds scientific-formulation --task "define the observable and governing model"
ssds numerical-algorithm-design --task "choose and bound the numerical method"
ssds software-design --task "map the accepted method into software architecture"
ssds software-implementation --workplan workplans/active/MY-WORKPLAN.md
ssds review --workplan workplans/active/MY-WORKPLAN.md
ssds verification --input VERIFICATION_SCOPE="the release-critical numerical claims"
ssds stabilization --input STABILIZATION_SCOPE="the affected architecture"
ssds health-audit --input AUDIT_SCOPE="the long-lived subsystem"
ssds prompt closeout --workplan workplans/active/MY-WORKPLAN.md
```

For common software-only work, `design` remains an alias for Protocol 6
`software-design`, and `implementation` remains an alias for
`software-implementation`. These names also match the frozen Protocol 5.16 stage
keys, which makes them convenient when an older workplan may bind the legacy
profile:

```bash
ssds design --task "split the ingest pipeline from the storage layer"
ssds implementation --workplan workplans/active/MY-WORKPLAN.md
```

Profile-specific aliases such as `d1`, `science`, `d2`, and `numerics` are always
available through the generic form:

```bash
ssds prompt d1 --task "review the scientific formulation"
ssds prompt d2 --task "review the numerical method"
```

The prompt goes to **stdout only**, and only after the complete artifact exists.
Diagnostics go to stderr as redacted JSON with a nonzero exit status, so piping
is safe:

```bash
ssds implementation | pbcopy
ssds implementation > prompt.txt
ssds implementation --copy          # additive; clipboard failure does not invalidate stdout
```

Exit statuses: `0` success, `2` a structured Core problem, `1` an unexpected
internal failure.

### Command families

| Command | Purpose |
| --- | --- |
| `ssds <stage-key>` | render a registered stage command when the selected profile defines or aliases it |
| `ssds prompt <stage-or-alias>` | render by selected profile stage key or alias |
| `ssds projects [--workplans]` | list configured projects and their observable workplans |
| `ssds capabilities` | capability status; metadata-only discovery by default |
| `ssds doctor` | readiness report with no hidden loading, network, or repository mutation |

The executable stage-command set is the union needed for the supported Protocol
6 and frozen 5.16 profiles. The selected profile still owns the meaning of a
name; Core does not maintain a second workflow definition in the CLI.

### Common options

| Option | Meaning |
| --- | --- |
| `--project <key>` | configured project key |
| `--workplan <id-or-path>` | exact workplan id or exact repository-relative path |
| `--prompt-mode local\|web` | where the prompt will be consumed |
| `--config <path>` | explicit configuration file |
| `--remote-mode <mode>` | `local_only`, `use_cached_remote` (CLI default), `refresh_remote` |
| `--task <text>` | task description for intake/D1/D2/D3 entry stages |
| `--input NAME=VALUE` | a declared profile INPUT; repeatable |
| `--copy` | additionally copy the completed prompt to the clipboard |

---

## 4. Workplans, profile binding, and required inputs

Core resolves workplans according to the **selected profile's stage policy**.
Selection is exact—by workplan id or repository-relative path, by a
`target_branch` binding matching the current branch, or because exactly one
eligible active workplan exists where the stage permits resolution. Filename
similarity and modification time are never authority.

Protocol 6 stage policies are:

| Protocol 6 stage | Workplan policy | Required user input |
| --- | --- | --- |
| `intake` | optional explicit only | `--task` |
| `scientific-formulation` | optional explicit only | `--task` |
| `numerical-algorithm-design` | optional explicit only | `--task` |
| `software-design` | optional explicit only | `--task` |
| `software-implementation` | optional explicit only | — |
| `review` | required/resolved | — |
| `verification` | optional explicit only | `VERIFICATION_SCOPE` |
| `stabilization` | optional explicit only | `STABILIZATION_SCOPE` |
| `alignment` | exact selector required | `UPSTREAM_ACCEPTED_WORK` |
| `health-audit` | workplan disallowed | `AUDIT_SCOPE` |
| `closeout` | optional exact binding | `COMPLETED_WORK` unless the selected plan supplies it |

A genuinely local Protocol 6 D4-only implementation may omit `--workplan`; Core renders `CHANGE_PLAN = NONE` and the receiving agent must still perform the protocol's proportionate upstream-impact exclusion. When a change plan/workplan materially governs D4, pass it explicitly with `--workplan`; its declared `protocol_version` still binds the compatible profile. Review remains plan-governed.

An explicitly supplied Protocol 6 D4 change plan must be active, lifecycle-consistent, and semantically complete. Core rejects archived or incomplete explicit plans instead of treating them as governing authority; this validation does not affect the plan-free local D4-only route.

A new D3 design task with no `--workplan` does **not** adopt an unrelated sole
active workplan. A workplan passed to a stage that disallows one fails rather
than being ignored.

### Version binding is part of workplan identity

A governing workplan for a stage that requires one must declare a supported
`protocol_version`. That version can bind the final workflow profile even when
the project default points elsewhere. Core then resolves the stage and workplan
again under that final profile before rendering, so preparation cannot contain a
half-5.16/half-6.2 interpretation.

For example, a 5.16 workplan remains renderable through the frozen
`sdp-protocol-5.16` package. Use a stage name meaningful to both versions (for
example `implementation`, `review`, or `verification`) when selecting such a
legacy workplan. A missing or unsupported required version fails; Core never
silently upgrades it to Protocol 6.

Documents sharing a `workplan_id` are collapsed only through explicit
`parent_workplan` / `supersedes_revision` evidence. If that evidence does not
identify one current candidate, Core reports `core.workplan.ambiguous`; the
exact path remains available.

---

## 5. Two different kinds of “mode”

**`--prompt-mode` (`local` / `web`)** answers *where the prompt will be
consumed*. It changes only the repository context Core renders into the prompt.

**`EXECUTION_MODE` (`AUTO_EXECUTE` / `REPORT_ONLY` / …)** is a canonical
Protocol input. It answers *what the receiving agent is authorized to do*.

Changing one never changes the other:

```bash
ssds implementation --prompt-mode web
ssds implementation --input EXECUTION_MODE=REPORT_ONLY
```

There is a second separation. Core's **render source** is where Core read the
canonical prompt/profile material: a packaged snapshot, configured compatible
local checkout, or explicitly permitted remote source. Canonical
**`PROTOCOL_SOURCE`** is agent-facing and defaults to `AUTO_LOCAL_FIRST`.
Consequently a local render-source path does not leak into a web prompt merely
because Core read from it. `PROTOCOL_REF` is mechanically bound to the governing
Protocol contract and cannot be overridden.

---

## 6. Local vs web prompt truth

**Local mode** may reference the authorized worktree: absolute path, branch or
detached HEAD, commit, and working-tree state.

**Web mode** renders only sanitized remote repository context, target branch,
and exact candidate commit—and only when those claims can be established.
Core refuses rather than guessing or silently downgrading when:

| Situation | Reported as |
| --- | --- |
| worktree has uncommitted changes | `core.prompt.mode_invalid` |
| local and remote are known to diverge | `core.remote.stale` |
| no evidence establishes target existence | `core.remote.target_unavailable` |
| branch is absent on the selected remote | `core.remote.target_unavailable` |
| HEAD is detached | `core.remote.target_unavailable` |
| selected remote is a path or `file://` URL | `core.remote.local_only` |
| several remotes exist and none can be selected | `core.remote.ambiguous` |

Target *existence* must be known. Only *freshness* may be cached, and cached
freshness is labelled as such.

Web prompts never automatically carry local paths, credential-bearing remote
URLs, ambient environment values, credential-helper output, or private
orchestrator state. Text explicitly supplied through `--task` or `--input` is
intentional prompt content and is rendered as written; Core is not a general
secret scanner for user-authored text.

### Remote observation

Observation is non-mutating with respect to the target repository: no fetch,
pull, checkout, ref update, or opportunistic index refresh.

| `--remote-mode` | Behaviour |
| --- | --- |
| `local_only` | inspect repository configuration only; collect no remote-side evidence |
| `use_cached_remote` | read existing remote-tracking refs; no network |
| `refresh_remote` | one bounded noninteractive read-only `git ls-remote` |

The CLI defaults to `use_cached_remote`; the programmatic API defaults to
`local_only`. If `max_remote_staleness_seconds` is set through the API, cached
evidence whose age is unknown cannot satisfy that explicit freshness bound.
`refresh_remote` provides timestamped query evidence. Core performs no hidden
network refresh.

---

## 7. Profile schemas and result footer are different contracts

Protocol 6 uses **workflow profile schema v2**. Frozen Protocol 5.16 uses
**workflow profile schema v1**. Core supports both explicitly; it does not
reinterpret v1 fields as v2 semantics.

The terminal **StageResultEnvelope remains v1**. That result schema is a separate
version dimension from the workflow profile schema. Every rendered prompt asks
for an ordinary human-readable response followed by exactly one terminal,
uniquely marked JSON footer:

```text
<<<SDP_STAGE_RESULT_V1
{ "schema_version": 1, "run_id": "...", "prompt_fingerprint": "sha256:...",
  "stage": "software-implementation", "outcome": "complete", ... }
SDP_STAGE_RESULT_V1>>>
```

There must be exactly one exact begin marker and one exact end marker; only
whitespace may follow the end marker. Ordinary prose may precede the footer.
Unrecognized additional JSON fields are tolerated.

Declared scalar inputs use structure-safe encoding so quotes, newlines, and
backslashes remain data rather than changing prompt control structure.
`Problem.retryable` is advisory metadata; Core performs no automatic retry.

The prompt never requests hidden reasoning. Core renders the request but does
not parse or persist the returned result; that belongs to the later Tracker
module.

With a fixed `run_id` and unchanged material state, output identity is
reproducible. Wall-clock timestamps and unrelated extension configuration do not
perturb the prompt fingerprint.

---

## 8. Serious Challenge routing in Protocol 6

Protocol 6 profiles recognize `serious_challenge` at material governed stages.
A Serious Challenge is not an ordinary “failed test” outcome: it means accepted
authority itself may be materially wrong, contradictory, ambiguous, inadequate,
or unrealizable and requires designated human adjudication.

Core does not decide whether a challenge is epistemically correct. It only
renders and exposes the profile-owned routing contract. In the Protocol 6
profile, Serious Challenge transitions are terminal with respect to automatic
routing; downstream normal release/Pass must not be inferred from them.

This preserves the architectural invariant that the orchestrator is subordinate
to Protocol authority rather than becoming scientific or design authority.

---

## 9. Extensions

Extensions are discovered through exactly one Python entry-point group,
`ssds.extensions.v1`. There is no directory scanning or
repository-loaded plugin path.

Installed extension code is trusted in-process code; Core does not sandbox it.
`ssds doctor` and `ssds capabilities` default to metadata-only discovery, so they
do not import provider code and do not claim unobserved provider health. Use
`--load-extensions` when provider activation is actually wanted.

A failed or incompatible optional extension disables itself and dependents;
healthy Core services keep working. Prompt-containing events are delivered only
to sinks that subscribed to that event type, and sink failure cannot invalidate
a successful primary render.

---

## 10. What Core deliberately does not do

Core itself has no run history or status/next/ingest/graph commands; no agent
execution or worktree leases; no model/backend/benchmark catalog; no quota meter
or scheduler; no daemon; and no repository-local private orchestrator state.
Those capabilities belong to later Tracker, Adapter, and Scheduler modules.

The orchestrator architecture remains profile-owned and version-neutral: the
Protocol 6 schema-v2 profile extends workflow semantics without making Core a
second source of scientific, numerical, or architecture truth.

---

## 11. Repository layout and development

Every orchestrator-owned implementation, test, fixture, script, package, and
documentation file lives under `orchestrator/`. Protocol source under `source/`
and Protocol workplans under `workplans/` are external inputs/authorities, not
alternate homes for orchestrator code.

```text
orchestrator/
  docs/          architecture.md, core-user-guide.md
  pyproject.toml   the one distribution, ssds
  bin/ssds         zero-install checkout launcher
  src/ssds/        cli.py (the composition root), core/ (Level 0 Core), the SSDS components
  tests/           Core's suite; tests/ssds/ for the SSDS components
  scripts/       snapshot generation, test runner
```

Useful development checks:

```bash
python3 orchestrator/bin/ssds --help
python3 orchestrator/scripts/run_core_tests.py
python3 orchestrator/scripts/generate_protocol_snapshot.py --check
```

An editable installation is optional convenience:

```bash
python3 -m pip install -e orchestrator -r orchestrator/requirements-dev.txt
```

The packaged Protocol snapshots under
`orchestrator/src/ssds/core/resources/protocol/` are generated or
frozen version-bound artifacts and are never hand-edited. Current Protocol 6 is
generated from `source/shared/references/development-workflow-prompts.md`;
Protocol 5.16 remains an immutable compatibility snapshot. The repository build
checks verify both identities.
