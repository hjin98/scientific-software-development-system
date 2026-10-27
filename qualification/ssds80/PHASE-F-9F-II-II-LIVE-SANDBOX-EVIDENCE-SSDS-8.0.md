# Phase F step 9f-ii-ii: live sandbox evidence

The live tests of reading F113 need unprivileged user namespaces, which the implementing agent's own sandbox denies.
They were run on the host, in the operator's terminal session, as plan check of 23d2f5f2 (answer 3) requires. A
review checks that the commit below is the one it reviews.

## Current run (after the review of cc028146)

| Field | Value |
|---|---|
| Commit under test | `79b09de505b36b866dcb3253a3f75041cb52c3fd` (worktree clean under `src` and `tests`) |
| Command | `SSDS_LIVE_SANDBOX=1 PYTHONPATH=src python -m unittest tests.ssds.test_phase_f_step9f_ii_ii_live -v` (in `orchestrator/`) |
| Date | 2026-10-27T20:43:59Z |
| Run by | the implementing agent, through the operator's terminal session (user `samjin`); not the stakeholder |
| Host | Linux 6.8.0-138-generic x86_64; Ubuntu 22.04.5 LTS |
| `bubblewrap` | 0.6.1-1ubuntu0.3 (the CVE-2026-87766 fix dropped; Q-F26) |
| Python | 3.13.13 |

| Test | Result |
|---|---|
| `Live.test_the_f2_properties` | ok |
| `Live.test_a_reached_time_bound` (the child shown gone: its tick stops) | ok |

Exit status 0; 2 tests in 2.057 s.

### What the sandbox observed (the same probe, at the same commit)

- environment variables: `AGENT`, `CANARY` and `PORT` (the probe's own), `HOME`, `LANG`, `PATH`, `PWD`, `TMPDIR`;
  `SSH_AUTH_SOCK` absent;
- the real agent socket's path (present outside): absent inside;
- network interfaces: only `lo`; a listener on the host's `127.0.0.1`: `ConnectionRefusedError`; `1.1.1.1:53`:
  `OSError`;
- a canary under the real home (`~/.cache`, a directory of its own, removed afterwards), outside the sandbox's own
  `/tmp`: `FileNotFoundError`;
- a write to `/work/written`: `EROFS`;
- `HOME` `/home/runner`, working directory `/work`, `/work/a.txt` `hello\n` (the materialized tree).

## Earlier run (cc028146), superseded

The first run, at `cc02814673752b6ad53575e9ca509eada8a71bbd` (2026-10-27T20:19:22Z), passed both tests, but its review
found four checks that could pass for the wrong reason: the network (any unreachable address), the agent socket (only
the variable), the operator tree (a canary under `/tmp`, which the sandbox replaces with its own tmpfs), the workspace
(any `OSError`). The current run replaces it.

## Host probe of `bwrap` behaviour (before the build)

Run from a scratch script outside the repository: unprivileged namespaces are created; a read-only bind refuses
writes (`Read-only file system`); `/proc`, `/sys` and `/run` are absent; `--clearenv` leaves only what is set;
`--ro-bind-fd` binds the descriptor's directory; Python runs without `/proc`; `--json-status-fd` reports `child-pid`
and the exit code; a missing bind source exits 1 with no `child-pid`.
