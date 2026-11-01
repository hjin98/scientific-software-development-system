"""Plan revision 72, step 5 after W9: re-read the three shadow ledgers with the FR-A1-repaired reader, in one boundary
window in the stakeholder's terminal, and compare with what the frozen 8cf829c3 reader read in W9.

    /tmp/claude-1000/ssds-runtime-20261030/bin/python -I -B PHASE-F-FR-A1-REREAD-WINDOW.py --candidate <commit> <out>

Preconditions: ``orchestrator/`` equals the re-frozen candidate and is clean, no bytecode under ``orchestrator/src``,
no linked worktree, PREFLIGHT-A is F126's pin, and the out directory is new and outside the repository. Then the
boundary snapshot, W9's C7 read (PREFLIGHT-A over the repository's ``src``, ``--ledgers ssdp-shadow-3 ssdp-shadow-2
ssdp-shadow``, home the default ``~/.ssds``) and the compare, which runs even when the read fails. PREFLIGHT-A is
retired from the tracked tree (it imports the program, which the containment fitness rule allows only under
``orchestrator/``); it is extracted from 10d's last commit into the out directory and must carry F126's pin. The
window is ``PASS`` only when the read exits 0, reports the default home, its ``ledgers`` equal W9's committed
``W9-c7.json`` field for field, and the compare passes. Read only: nothing is appended, and no SSDS module is
imported here.
"""

import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

RUNTIME = "/tmp/claude-1000/ssds-runtime-20261030/bin/python"
REPOSITORY = Path(__file__).resolve().parents[2]
HERE = REPOSITORY / "qualification" / "ssds80"
TOOLS_COMMIT = "7d22f708"  # 10d complete; the last commit that tracks the 10d tools
PREFLIGHT_PATH = "qualification/ssds80/PHASE-F-RETIREMENT-2-PREFLIGHT-A.py"
PREFLIGHT_SHA256 = "f2fecb328d47ad676f83a119887083c637330cf3489e90aa9aa8323fc582a969"  # F126's pin
FROZEN_READ = HERE / "PHASE-F-10D-SHADOW-3-WINDOWS" / "W9-c7.json"  # the 8cf829c3 reader's result
SENSOR = REPOSITORY / "orchestrator" / "scripts" / "shadow_boundary.py"
SOURCE = REPOSITORY / "orchestrator" / "src"
LEDGERS = ["ssdp-shadow-3", "ssdp-shadow-2", "ssdp-shadow"]


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(REPOSITORY), *args], capture_output=True, text=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--candidate", required=True)
    parser.add_argument("out", type=Path)
    a = parser.parse_args()
    if sys.executable != RUNTIME or not sys.flags.isolated or not sys.flags.dont_write_bytecode:
        raise SystemExit(f"run under {RUNTIME} -I -B")
    out = a.out.resolve()
    if out.is_relative_to(REPOSITORY) or out.exists():
        raise SystemExit(f"{out} must be new and outside the repository")
    candidate = git("rev-parse", "--verify", a.candidate + "^{commit}").stdout.strip()
    failed = [] if candidate == a.candidate else [f"{a.candidate} is not a full commit id"]
    if not failed and git("diff", "--quiet", candidate, "--", "orchestrator/").returncode:
        failed.append(f"orchestrator/ differs from {candidate}")
    if git("status", "--porcelain", "--untracked-files=all", "--", "orchestrator/").stdout.strip():
        failed.append("orchestrator/ is not clean")
    ignored = git("status", "--porcelain", "--ignored", "--", "orchestrator/src/").stdout
    if "__pycache__" in ignored or ".pyc" in ignored:
        failed.append("bytecode under orchestrator/src/")
    if sum(line.startswith("worktree ") for line in git("worktree", "list", "--porcelain").stdout.splitlines()) != 1:
        failed.append("a linked worktree is registered")
    preflight_bytes = subprocess.run(["git", "-C", str(REPOSITORY), "show", f"{TOOLS_COMMIT}:{PREFLIGHT_PATH}"],
                                     capture_output=True).stdout
    if hashlib.sha256(preflight_bytes).hexdigest() != PREFLIGHT_SHA256:
        failed.append(f"PREFLIGHT-A at {TOOLS_COMMIT} is not F126's {PREFLIGHT_SHA256}")
    tools = {p.name: sha256(p) for p in (Path(__file__).resolve(), SENSOR, FROZEN_READ)}
    if failed:
        raise SystemExit(f"NOT STARTED: {failed}")
    out.mkdir(parents=True)
    preflight = out / "preflight-a.py"
    preflight.write_bytes(preflight_bytes)
    tools[preflight.name] = sha256(preflight)
    env = {k: v for k, v in os.environ.items() if not k.startswith("PYTHON") and k != "SSDS_HOME"}
    report = out / "reread.json"
    argv = [RUNTIME, "-I", "-B", str(preflight), "--tree", str(SOURCE), "--out", str(report), "--ledgers", *LEDGERS]
    record = {"at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "candidate": candidate,
              "ignored_under_src": ignored.splitlines(), "tools_sha256": tools, "command": argv}
    before = out / "before.json"
    with (out / "snapshot.log").open("x") as f:
        if subprocess.run([RUNTIME, "-I", "-B", str(SENSOR), "snapshot", "--repository", str(REPOSITORY),
                           "--out", str(before)], env=env, stdout=f, stderr=subprocess.STDOUT).returncode:
            raise SystemExit("NOT STARTED: snapshot refused")
    try:
        with (out / "reread.log").open("x") as log:
            record["read_exit"] = subprocess.run(argv, env=env, stdout=log, stderr=subprocess.STDOUT).returncode
        if record["read_exit"] == 0:
            read = json.loads(report.read_text())
            now, then = read["ledgers"], json.loads(FROZEN_READ.read_text())["ledgers"]
            record["home"], record["ssds"] = read["home"], read["ssds"]
            record["differences"] = [] if read["home"] == str(Path.home() / ".ssds") else [f"home {read['home']}"]
            record["differences"] += [f"{ledger}.{k}: {now.get(ledger, {}).get(k)!r}, at 8cf829c3 {then[ledger].get(k)!r}"
                                     for ledger in sorted(set(now) | set(then))
                                     for k in sorted(set(now.get(ledger, {})) | set(then.get(ledger, {})))
                                     if now.get(ledger, {}).get(k) != then.get(ledger, {}).get(k)]
    except BaseException as exc:  # the compare still runs
        record["interrupted"] = f"{type(exc).__name__}: {exc}"
    finally:
        with (out / "compare.log").open("x") as f:
            record["compare_exit"] = subprocess.run(
                [RUNTIME, "-I", "-B", str(SENSOR), "compare", "--repository", str(REPOSITORY), "--before",
                 str(before)], env=env, stdout=f, stderr=subprocess.STDOUT).returncode
        record["before_sha256"] = sha256(before)
        record["result"] = ("FAILED" if record["compare_exit"] else
                            "PASS" if record.get("read_exit") == 0 and record.get("differences") == [] else
                            "INCOMPLETE")
        (out / "window.json").write_text(json.dumps(record, indent=2) + "\n")
    print((out / "reread.log").read_text())
    print((out / "compare.log").read_text())
    print(json.dumps({k: record.get(k) for k in ("result", "read_exit", "differences", "compare_exit")}))
    return 0 if record["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
