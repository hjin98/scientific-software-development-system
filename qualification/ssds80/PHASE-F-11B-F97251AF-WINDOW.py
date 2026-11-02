"""The step-11b run at the candidate re-frozen by plan revision 78 (Phase F reading F123-F124; the XR-C1 to XR-B3
repairs), revision 74's script but for its docstring and candidate: one boundary window, in the stakeholder's
terminal, around the difference-study harness at the frozen candidate, on a new scratch SSDS home. No real ledger is
read or written.

    /tmp/claude-1000/ssds-runtime-20261030/bin/python -I -B PHASE-F-11B-F97251AF-WINDOW.py <out directory>

Preconditions: ``orchestrator/`` equals the frozen candidate and is clean, no bytecode under ``orchestrator/src``,
no linked worktree, and the out directory is new and outside the repository. Then the boundary snapshot, the harness
(``-I -B``, ``SSDS_HOME`` = ``<out>/home``, budget 7,200 s) with progress lines every 30 s that name no finding,
and the compare, which runs even when the harness fails or the window is interrupted. The harness remains the only
owner of the report and of its own final boundary check.
"""

import datetime
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

RUNTIME = "/tmp/claude-1000/ssds-runtime-20261030/bin/python"
REPOSITORY = Path(__file__).resolve().parents[2]
FROZEN = "f97251af91477b9a66ff29bc7d871c326a7dff26"
HARNESS = REPOSITORY / "orchestrator" / "scripts" / "difference_study.py"
SENSOR = REPOSITORY / "orchestrator" / "scripts" / "shadow_boundary.py"
BUDGET = 7200


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(REPOSITORY), *args], capture_output=True, text=True)


def main() -> int:
    if sys.executable != RUNTIME or not sys.flags.isolated or not sys.flags.dont_write_bytecode:
        raise SystemExit(f"run under {RUNTIME} -I -B")
    out = Path(sys.argv[1]).resolve()
    if out.is_relative_to(REPOSITORY) or out.exists():
        raise SystemExit(f"{out} must be new and outside the repository")
    failed = []
    if git("diff", "--quiet", FROZEN, "--", "orchestrator/").returncode:
        failed.append("orchestrator/ differs from the frozen candidate")
    if git("status", "--porcelain", "--untracked-files=all", "--", "orchestrator/").stdout.strip():
        failed.append("orchestrator/ is not clean")
    ignored = git("status", "--porcelain", "--ignored", "--", "orchestrator/src/").stdout
    if "__pycache__" in ignored or ".pyc" in ignored:
        failed.append("bytecode under orchestrator/src/")
    if sum(line.startswith("worktree ") for line in git("worktree", "list", "--porcelain").stdout.splitlines()) != 1:
        failed.append("a linked worktree is registered")
    if failed:
        raise SystemExit(f"NOT STARTED: {failed}")
    out.mkdir(parents=True)
    home = out / "home"
    env = {k: v for k, v in os.environ.items() if not k.startswith("PYTHON") and k != "SSDS_HOME"}
    env["SSDS_HOME"] = str(home)
    record = {"at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "candidate": FROZEN,
              "home": str(home), "ignored_under_src": ignored.splitlines(),
              "tools_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in (Path(__file__).resolve(), HARNESS, SENSOR)}}
    before = out / "before.json"
    with (out / "snapshot.log").open("x") as f:
        if subprocess.run([RUNTIME, "-I", "-B", str(SENSOR), "snapshot", "--repository", str(REPOSITORY),
                           "--out", str(before)], env=env, stdout=f, stderr=subprocess.STDOUT).returncode:
            raise SystemExit("NOT STARTED: snapshot refused")
    argv = ["timeout", str(BUDGET), RUNTIME, "-I", "-B", str(HARNESS), "--repository", str(REPOSITORY),
            "--candidate", FROZEN]
    record["command"] = argv
    started, last = time.monotonic(), None
    try:
        with (out / "harness.log").open("x") as log:
            process = subprocess.Popen(argv, env=env, stdout=log, stderr=subprocess.STDOUT)
            while process.poll() is None:
                time.sleep(30)
                report = home / "difference-study.json"
                try:
                    data = json.loads(report.read_text())
                    info = {"elapsed_seconds": round(time.monotonic() - started),
                            "evaluated": data["summary"]["evaluated"],
                            "expected": data["execution"]["expected_deltas"], "phase": data["execution"]["phase"],
                            "status": data["execution"]["status"]}
                except (OSError, ValueError, KeyError):
                    info = {"elapsed_seconds": round(time.monotonic() - started), "report": "not yet readable"}
                marker = {k: v for k, v in info.items() if k != "elapsed_seconds"}
                if marker != last:
                    print(json.dumps(info), flush=True)
                    last = marker
            record["harness_exit"] = process.returncode
    except BaseException as exc:  # the compare still runs
        record["interrupted"] = f"{type(exc).__name__}: {exc}"
    finally:
        record["elapsed_seconds"] = round(time.monotonic() - started)
        with (out / "compare.log").open("x") as f:
            record["compare_exit"] = subprocess.run(
                [RUNTIME, "-I", "-B", str(SENSOR), "compare", "--repository", str(REPOSITORY), "--before",
                 str(before)], env=env, stdout=f, stderr=subprocess.STDOUT).returncode
        record["result"] = ("FAILED" if record["compare_exit"] else
                            "PASS" if record.get("harness_exit") == 0 and "interrupted" not in record else "INCOMPLETE")
        (out / "window.json").write_text(json.dumps(record, indent=2) + "\n")
    print((out / "harness.log").read_text()[-2000:])
    print((out / "compare.log").read_text())
    print(json.dumps({k: record.get(k) for k in ("result", "harness_exit", "compare_exit", "elapsed_seconds")}))
    return 0 if record["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
