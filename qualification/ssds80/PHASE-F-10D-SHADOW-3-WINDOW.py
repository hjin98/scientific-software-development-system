"""One boundary window of step 10d on ``ssdp-shadow-3`` (Phase F reading F126), run in the stakeholder's terminal:

    python -I -B PHASE-F-10D-SHADOW-3-WINDOW.py --mode rehearsal|real <window> [parameters]

It checks F126's preconditions, takes the boundary snapshot, runs the window's fixed commands (each through
``PHASE-F-10D-SHADOW-3-RUN.py`` under the pinned interpreter), then compares; the compare runs even when a command
crashes or the window is interrupted. It imports no SSDS module and writes only under the mode's window directory,
never in the repository; a window's files are never overwritten (a repeat takes ``--attempt``).

A window is ``PASS`` when every precondition holds, every command exits as expected, every output check of F126's
expected outcome holds and the compare passes. A failed compare is ``FAILED``. A passing compare with a command
exiting otherwise, or an output check failing, is ``INCOMPLETE`` (a refusal in a passing window is one: its
carrier stays on the ledger and is disclosed). ``NOT STARTED``: a precondition failed or the snapshot was refused.
"""

import argparse
import datetime
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tarfile
from pathlib import Path

RUNTIME = "/tmp/claude-1000/ssds-runtime-20261030/bin/python"
REPOSITORY = Path(__file__).resolve().parents[2]
HERE = REPOSITORY / "qualification" / "ssds80"
RUN = HERE / "PHASE-F-10D-SHADOW-3-RUN.py"
HELPER = HERE / "PHASE-F-10D-SHADOW-3-HELPER.py"
PREFLIGHT = HERE / "PHASE-F-RETIREMENT-2-PREFLIGHT-A.py"
PREFLIGHT_SHA256 = "f2fecb328d47ad676f83a119887083c637330cf3489e90aa9aa8323fc582a969"  # F126's pin
GENESIS = REPOSITORY / "orchestrator" / "scripts" / "shadow_genesis.py"
SENSOR = REPOSITORY / "orchestrator" / "scripts" / "shadow_boundary.py"
SOURCE = REPOSITORY / "orchestrator" / "src"
AFTER_C = {"c7": HERE / "PHASE-F-RETIREMENT-2-AFTER-C-C7-aba09fea.json",
           "pre-c7": HERE / "PHASE-F-RETIREMENT-2-AFTER-C-PRE-C7-3ea6d029.json"}
FROZEN = "8cf829c34020ebffb5ad50ad7ba5b03343c005ce"
PRE_C7 = "3ea6d0294916c68852433b69e9fb1ffee2073a22"
PRE_C7_EXTRACT = Path("/tmp/claude-1000/preflight-20261031/prec7")
BRANCH = "ssds-8.0-graph-native-architecture"
REHEARSAL_ROOT = Path("/tmp/claude-1000/ssds-10d-rehearsal")
MODES = {
    "rehearsal": {"ledger": "ssdp-shadow-3-rehearsal", "home": REHEARSAL_ROOT / "home",
                  "out": REHEARSAL_ROOT / "windows", "ledgers": ["ssdp-shadow-3-rehearsal"]},
    "real": {"ledger": "ssdp-shadow-3", "home": None, "out": Path("/tmp/claude-1000/ssds-10d-shadow-3/windows"),
             "ledgers": ["ssdp-shadow-3", "ssdp-shadow-2", "ssdp-shadow"]},
}
WINDOWS = ("G1", "G2", "W1", "W2", "W3", "W4a", "W4b", "W5a", "W5b", "W6", "W7a", "W7b", "W7c", "W8", "W9", "READ")
REQUEST = re.compile(r"^request (sha256:[0-9a-f]{64})$", re.M)
DECIDE_REFUSAL = "a HUMAN_DECISION record: its checks belong to a later phase (F1)"
RETIRED_FACTS = ("entries", "head_commit", "last_digest", "qualification", "halt", "readable_through")


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(REPOSITORY), *args], capture_output=True, text=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def output(text: str):
    """The JSON object a command printed between the wrapper's own lines."""

    return json.loads(text[text.index("{"):text.rindex("}") + 1])


def expect(**wanted):
    """An output check: each named field of the printed object has the wanted value."""

    def check(text: str) -> list[str]:
        got = output(text)
        return [f"{k} is {got.get(k)!r}, not {v!r}" for k, v in wanted.items() if got.get(k) != v]
    return check


def status_check(text: str) -> list[str]:
    got = output(text)
    problems = [f"qualification {got['qualification']}"] if got["qualification"] != "QUALIFIED" else []
    problems += [] if got["current_assertion"] is True else ["no current assertion"]
    problems += [] if got["provisional"] is None else [f"provisional {got['provisional']}"]
    problems += [] if got["critical"] == [] else [f"critical {got['critical']}"]
    return problems


def no_fence(text: str) -> list[str]:
    """W6: after the last ADMISSION, at most one entry, an ABSORPTION (F120: no fence after records-only admissions)."""

    chain = output(text)["chain"]
    last = max(e["position"] for e in chain if e["entry_kind"] == "ADMISSION")
    after = [e["entry_kind"] for e in chain if e["position"] > last]
    return [] if after in ([], ["ABSORPTION"]) else [f"entries after the last admission: {after}"]


def read_back(mode: str, tree: str):
    """W9: the live ledger QUALIFIED with no record violation; in the real run, each retired ledger as after step C."""

    def check(path: Path) -> list[str]:
        report = json.loads(path.read_text())["ledgers"]
        live = report[MODES[mode]["ledger"]]
        problems = [f"live ledger: {k} {live.get(k)!r}" for k, v in
                    (("qualification", "QUALIFIED"), ("halt", None), ("record_violations_by_position", {}))
                    if live.get(k) != v]
        if mode == "real":
            before = json.loads(AFTER_C[tree].read_text())["ledgers"]
            for ledger in ("ssdp-shadow-2", "ssdp-shadow"):
                problems += [f"{ledger}: {k} {report[ledger].get(k)!r}, after step C {before[ledger].get(k)!r}"
                             for k in RETIRED_FACTS if report[ledger].get(k) != before[ledger].get(k)]
        return problems
    return check


def steps(mode: str, window: str, name: str, a: argparse.Namespace) -> list[tuple]:
    """The window's fixed commands: (label, argv or a function of the earlier outputs, expected exit, output check
    or None). An output check reads the command's log, or for W9 its report file. Each window's own files are named
    after it (``name`` carries the attempt), so a repeat overwrites nothing."""

    m = MODES[mode]
    ledger, out = m["ledger"], m["out"]
    wrap = [RUNTIME, "-I", "-B", str(RUN), "--mode", mode, "--ledger", ledger]
    cli = [*wrap, "cli"]
    helper = [*wrap, "script", str(HELPER)]
    where = ["--ledger", ledger, "--repository", str(REPOSITORY)]
    observed = ["--observed-ref", BRANCH]
    home = m["home"] or Path.home() / ".ssds"

    def request_dir(rid: str) -> str:
        return str(home / "state" / ledger / "requests" / rid.removeprefix("sha256:"))

    def need(*names: str) -> None:
        missing = [n for n in names if not getattr(a, n)]
        if missing:
            raise SystemExit(f"{window} needs --{' --'.join(missing)}")

    def prepared(label: str):
        def argv(outputs: dict) -> list:
            found = REQUEST.findall(outputs[label])
            if len(found) != 1:
                raise RuntimeError(f"{label} printed {len(found)} request ids")
            return [*helper, "check", *where, "--request", found[0]]
        return argv

    if window in ("G1", "G2") and mode != "rehearsal":
        raise SystemExit("the scratch genesis windows run only in the rehearsal")
    if window == "G1":
        return [("genesis-prepare", [*wrap, "script", str(GENESIS), "--ledger-id", ledger, "--repository",
                                     str(REPOSITORY), "prepare", "--public-key", str(REHEARSAL_ROOT / "key" / "throwaway.pub"),
                                     "--baseline", FROZEN], 0, None)]
    if window == "G2":
        signature = home / "genesis" / ledger / "approval-message.txt.sig"
        return [("genesis-admit", [*wrap, "script", str(GENESIS), "--ledger-id", ledger, "--repository",
                                   str(REPOSITORY), "admit", "--signature", str(signature)], 0, None)]
    if window == "W1":
        return [("observe", [*cli, "admission", "serve", *where, *observed], 0, expect(absorbed=True, position=1))]
    if window == "W2":
        return [("status", [*cli, "status", *where], 0, status_check), ("inspect", [*cli, "inspect", *where], 0, None),
                ("state", [*helper, "state", *where], 0, expect(problems=[]))]
    if window == "W3":
        before = str(out / f"{name}-operator-state-before.json")
        return [("operator-before", [*helper, "operator-state", *where, "--out", before], 0, None),
                ("dispatcher", [*cli, "dispatcher", "serve", *where], 0, expect(would_issue=[], issued=[])),
                ("operator-after", [*helper, "operator-state", *where, "--out",
                                    str(out / f"{name}-operator-state-after.json"), "--compare", before], 0,
                 expect(changed=[]))]
    if window in ("W4a", "W5a", "W7a"):
        need("actor")
        kind, command = {"W4a": ("finding", "report"), "W5a": ("availability", "submit"),
                         "W7a": ("acknowledge", "decide")}[window]
        records = out / f"{name}-records"
        build = [*helper, "records", *where, "--kind", kind, "--out", str(records)]
        if kind == "finding":
            need("narrative")
            build += ["--narrative", a.narrative]
        if kind == "acknowledge":
            need("finding")
            build += ["--finding", a.finding]
        return [("records", build, 0, None),
                ("prepare", [*cli, command, *where, "--prepare", str(records / f"{kind}.json"),
                             "--actor", a.actor], 0, None),
                ("check", prepared("prepare"), 0, None)]
    if window in ("W4b", "W5b"):
        need("request")
        command = "report" if window == "W4b" else "submit"
        return [("admit", [*cli, command, *where, *observed, "--admit", request_dir(a.request)], 0,
                 expect(decision="ACCEPT", appended=True, refused=[]))]
    if window == "W6":
        return [("serve-1", [*cli, "admission", "serve", *where, *observed], 0, None),
                ("serve-2", [*cli, "admission", "serve", *where, *observed], 0, expect(absorbed=False)),
                ("state", [*helper, "state", *where], 0, no_fence)]
    if window == "W7b":
        need("request", "finding")
        return [("baseline", [*helper, "baseline", *where, "--finding", a.finding, "--out",
                              str(out / f"{name}-decide-baseline.json")], 0, None),
                ("decide-admit", [*cli, "decide", *where, *observed, "--admit", request_dir(a.request)], 1,
                 expect(refused=DECIDE_REFUSAL))]
    if window == "W7c":
        need("request", "baseline_window")
        return [("verify-decide", [*helper, "verify-decide", *where, "--request", a.request, "--baseline",
                                   str(out / f"{a.baseline_window}-decide-baseline.json")], 0, None)]
    if window == "W8":
        return [("candidate", [*helper, "candidate", *where], 0, expect(appended=False))]
    if window == "W9":
        c7, pre = out / f"{name}-c7.json", out / f"{name}-pre-c7.json"
        return [("read-c7", [*wrap, "script", str(PREFLIGHT), "--tree", str(SOURCE), "--out", str(c7),
                             "--ledgers", *m["ledgers"]], 0, (c7, read_back(mode, "c7"))),
                ("read-pre-c7", [RUNTIME, "-I", "-B", str(RUN), "--mode", mode, "--ledger", ledger, "--tree",
                                 str(PRE_C7_EXTRACT / "orchestrator" / "src"), "script", str(PREFLIGHT), "--tree",
                                 str(PRE_C7_EXTRACT / "orchestrator" / "src"), "--out", str(pre),
                                 "--ledgers", *m["ledgers"]], 0, (pre, read_back(mode, "pre-c7")))]
    if window == "READ":  # read-only: what the ledger holds, e.g. after a FAILED window (F126)
        return [("status", [*cli, "status", *where], 0, None), ("state", [*helper, "state", *where], 0, None)]
    raise SystemExit(f"no window {window}")


def preconditions(window: str) -> tuple[list[str], dict]:
    failed, facts = [], {}
    if git("diff", "--quiet", FROZEN, "--", "orchestrator/").returncode != 0:
        failed.append(f"orchestrator/ differs from {FROZEN}")
    untracked = git("status", "--porcelain", "--untracked-files=all", "--", "orchestrator/").stdout
    if untracked.strip():
        failed.append(f"orchestrator/ is not clean: {untracked.strip()}")
    ignored = git("status", "--porcelain", "--ignored", "--", "orchestrator/src/").stdout
    facts["ignored_under_src"] = ignored.splitlines()
    if "__pycache__" in ignored or ".pyc" in ignored:
        failed.append("bytecode is present under orchestrator/src/")
    worktrees = git("worktree", "list", "--porcelain").stdout
    if sum(line.startswith("worktree ") for line in worktrees.splitlines()) != 1:
        failed.append("a linked worktree is registered")
    head = git("rev-parse", "--verify", "refs/heads/" + BRANCH).stdout.strip()
    facts["branch_head"] = head
    # every window, since any Admission command may absorb the moved head (W1's check, review note 6)
    moved = git("diff", "--name-only", FROZEN, head, "--", ".ssds/", "orchestrator/").stdout
    facts["moved_under_ssds_or_orchestrator"] = moved.splitlines()
    if moved.strip():
        failed.append(f"the observed head changes .ssds/ or orchestrator/: {moved.split()}")
    facts["tools_sha256"] = {p.name: sha256(p) for p in (Path(__file__).resolve(), RUN, HELPER, PREFLIGHT, SENSOR,
                                                           GENESIS)}
    if facts["tools_sha256"][PREFLIGHT.name] != PREFLIGHT_SHA256:
        failed.append(f"{PREFLIGHT.name} is not F126's {PREFLIGHT_SHA256}")
    if window == "W9":
        archive = subprocess.run(["git", "-C", str(REPOSITORY), "archive", PRE_C7, "orchestrator/src"],
                                 capture_output=True, check=True)
        differs = []  # file contents only: git archive's owners and times are not the extract's
        with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as tar:
            members = [m for m in tar.getmembers() if m.isfile()]
            for member in members:
                path = PRE_C7_EXTRACT / member.name
                if not path.is_file() or path.read_bytes() != tar.extractfile(member).read():
                    differs.append(member.name)
        extra = sorted({str(p.relative_to(PRE_C7_EXTRACT)) for p in (PRE_C7_EXTRACT / "orchestrator/src").rglob("*")
                        if p.is_file()} - {m.name for m in members})
        facts["pre_c7_extract"] = {"files": len(members), "differs": differs, "extra": extra}
        if differs or extra:
            failed.append(f"the pre-C7 extract differs from {PRE_C7}: {differs[:5]} {extra[:5]}")
    return failed, facts


def run_commands(plan: list, name: str, out: Path, env: dict, record: dict, outputs: dict) -> None:
    for label, argv, expected, check in plan:
        log = out / f"{name}-{label}.log"
        try:
            argv = argv(outputs) if callable(argv) else argv
        except RuntimeError as exc:
            record["commands"].append({"label": label, "error": str(exc)})
            return
        with log.open("x") as f:
            done = subprocess.run([str(x) for x in argv], env=env, stdout=f, stderr=subprocess.STDOUT)
        outputs[label] = log.read_text()
        entry = {"label": label, "argv": [str(x) for x in argv], "exit": done.returncode, "expected": expected,
                 "log_sha256": sha256(log)}
        record["commands"].append(entry)
        if done.returncode != expected:
            return
        if check is not None:
            try:
                entry["check_problems"] = check[1](check[0]) if isinstance(check, tuple) else check(outputs[label])
            except (ValueError, KeyError, TypeError, OSError) as exc:
                entry["check_problems"] = [f"output unreadable: {type(exc).__name__}: {exc}"]
            if entry["check_problems"]:
                return


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--mode", required=True, choices=MODES)
    parser.add_argument("window", choices=WINDOWS)
    parser.add_argument("--attempt", type=int, default=1)
    for option in ("actor", "narrative", "finding", "request"):
        parser.add_argument("--" + option)
    parser.add_argument("--baseline-window", default="W7b", help="the W7b attempt whose baseline W7c reads")
    a = parser.parse_args()
    if sys.executable != RUNTIME or not sys.flags.isolated or not sys.flags.dont_write_bytecode:
        raise SystemExit(f"run under {RUNTIME} -I -B")
    m = MODES[a.mode]
    name = a.window + (f"-{a.attempt}" if a.attempt > 1 else "")
    out = m["out"]
    out.mkdir(parents=True, exist_ok=True)
    env = {k: v for k, v in os.environ.items() if not k.startswith("PYTHON") and k != "SSDS_HOME"}
    if m["home"] is not None:
        env["SSDS_HOME"] = str(m["home"])
    plan = steps(a.mode, a.window, name, a)
    failed, facts = preconditions(a.window)
    record = {"at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "mode": a.mode, "window": name,
              "preconditions": {"failed": failed, **facts}, "commands": []}
    if failed:
        record["result"] = "NOT STARTED"
        print(json.dumps(record, indent=2))
        with (out / "windows.jsonl").open("a") as f:
            f.write(json.dumps(record) + "\n")
        return 1
    before = out / f"{name}-before.json"
    with (out / f"{name}-snapshot.log").open("x") as f:
        take = subprocess.run([RUNTIME, "-I", "-B", str(SENSOR), "snapshot", "--repository", str(REPOSITORY),
                               "--out", str(before)], env=env, stdout=f, stderr=subprocess.STDOUT)
    if take.returncode != 0:
        record["result"] = "NOT STARTED (snapshot refused)"
        print(json.dumps(record, indent=2))
        print((out / f"{name}-snapshot.log").read_text())
        return 1
    outputs: dict[str, str] = {}
    try:
        run_commands(plan, name, out, env, record, outputs)
    except BaseException as exc:  # an interrupted or crashed runner still compares and records (review note 4)
        record["interrupted"] = f"{type(exc).__name__}: {exc}"
    finally:
        with (out / f"{name}-compare.log").open("x") as f:
            compare = subprocess.run([RUNTIME, "-I", "-B", str(SENSOR), "compare", "--repository", str(REPOSITORY),
                                      "--before", str(before)], env=env, stdout=f, stderr=subprocess.STDOUT)
        commands_ok = "interrupted" not in record and len(record["commands"]) == len(plan) and all(
            c.get("exit") == c.get("expected") and not c.get("check_problems") for c in record["commands"])
        record["compare_exit"] = compare.returncode
        record["before_sha256"] = sha256(before)
        record["result"] = "FAILED" if compare.returncode else ("PASS" if commands_ok else "INCOMPLETE")
        with (out / "windows.jsonl").open("a") as f:
            f.write(json.dumps(record) + "\n")
    for label in outputs:
        print(f"===== {name} {label}\n{outputs[label]}")
    print(f"===== {name} compare\n{(out / f'{name}-compare.log').read_text()}")
    print(json.dumps({k: record[k] for k in ("mode", "window", "result", "compare_exit")}
                     | {"commands": [(c["label"], c.get("exit"), c.get("expected"), c.get("check_problems"))
                                     for c in record["commands"]]}))
    return 0 if record["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
