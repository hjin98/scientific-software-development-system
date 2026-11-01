"""The one entry point of every program-running process of step 10d on ``ssdp-shadow-3`` (Phase F reading F126).

    python -I -B PHASE-F-10D-SHADOW-3-RUN.py --mode rehearsal|real --ledger <id> [--tree <src>] cli <ssds arguments>
    python -I -B PHASE-F-10D-SHADOW-3-RUN.py --mode rehearsal|real --ledger <id> [--tree <src>] script <path> <args>

Before any SSDS module is imported it checks the interpreter, the mode, the resolved SSDS home and the ledger the
process is given: ``rehearsal`` needs ``SSDS_HOME`` inside the fixed scratch root and the rehearsal ledger; ``real``
needs the home to be ``~/.ssds`` and the live ledger. A mismatch exits 2 before any SSDS code reads or writes a
home. ``cli`` calls ``ssds.cli.main``; ``script`` runs one of a fixed set of scripts with ``runpy``. Both put the
tree's ``src`` first on ``sys.path`` (default: this repository's; ``--tree`` is allowed only for W9's pre-C7 read)
and assert, in the same process, that every loaded ``ssds`` module resolves under that tree (exit 3 otherwise).
"""

import os
import pwd
import runpy
import sys
import traceback
from pathlib import Path

RUNTIME = "/tmp/claude-1000/ssds-runtime-20261030/bin/python"
REPOSITORY = Path(__file__).resolve().parents[2]
SOURCE = REPOSITORY / "orchestrator" / "src"
REHEARSAL_ROOT = Path("/tmp/claude-1000/ssds-10d-rehearsal")
PRE_C7_SOURCE = Path("/tmp/claude-1000/preflight-20261031/prec7/orchestrator/src")
LEDGERS = {"rehearsal": "ssdp-shadow-3-rehearsal", "real": "ssdp-shadow-3"}
READ_BACK = {"rehearsal": ["ssdp-shadow-3-rehearsal"], "real": ["ssdp-shadow-3", "ssdp-shadow-2", "ssdp-shadow"]}
GENESIS = REPOSITORY / "orchestrator" / "scripts" / "shadow_genesis.py"
PREFLIGHT = REPOSITORY / "qualification" / "ssds80" / "PHASE-F-RETIREMENT-2-PREFLIGHT-A.py"
HELPER = REPOSITORY / "qualification" / "ssds80" / "PHASE-F-10D-SHADOW-3-HELPER.py"


def refuse(reason: str) -> None:
    print(f"WRAPPER REFUSED: {reason}")
    sys.exit(2)


def values(argv: list[str], option: str) -> list[list[str]]:
    """Every occurrence of ``option`` in ``argv`` with the values that follow it (``--x v`` or ``--x=v``)."""

    found = []
    for i, token in enumerate(argv):
        if token == option:
            run = []
            for value in argv[i + 1:]:
                if value.startswith("--"):
                    break
                run.append(value)
            found.append(run)
        elif token.startswith(option + "="):
            found.append([token.split("=", 1)[1]])
    return found


def one_value(argv: list[str], option: str, expected: str) -> None:
    found = values(argv, option)
    if len(found) != 1 or not found[0] or found[0][0] != expected:
        refuse(f"the process must be given {option} {expected} exactly once, not {found}")


def checked_home(mode: str) -> Path:
    configured = os.environ.get("SSDS_HOME")
    if configured and not Path(configured).expanduser().is_absolute():
        refuse(f"SSDS_HOME {configured!r} is not absolute")
    home = (Path(configured).expanduser() if configured else Path.home() / ".ssds").resolve()
    if mode == "rehearsal":
        root = REHEARSAL_ROOT.resolve()
        if not configured or not home.is_relative_to(root) or home == root:
            refuse(f"rehearsal needs SSDS_HOME set inside {root}; it resolves to {home}")
    else:
        real = (Path(pwd.getpwuid(os.getuid()).pw_dir) / ".ssds").resolve()
        if home != real:
            refuse(f"real needs the SSDS home {real}; it resolves to {home}")
    return home


def main() -> int:
    argv = sys.argv[1:]
    forms = [i for i, token in enumerate(argv) if token in ("cli", "script")]
    if not forms:
        refuse("name a form: cli or script")
    own, form, rest = argv[: forms[0]], argv[forms[0]], argv[forms[0] + 1:]
    options = dict(zip(own[0::2], own[1::2]))
    if len(own) % 2 or set(options) - {"--mode", "--ledger", "--tree"} or len(options) != len(own) // 2:
        refuse(f"wrapper options are --mode, --ledger and --tree, each once: {own}")
    mode, ledger = options.get("--mode"), options.get("--ledger")
    if mode not in LEDGERS:
        refuse("--mode is rehearsal or real")
    if ledger != LEDGERS[mode]:
        refuse(f"--mode {mode} runs ledger {LEDGERS[mode]}, not {ledger}")
    if sys.executable != RUNTIME or not sys.flags.isolated or not sys.flags.dont_write_bytecode:
        refuse(f"run under {RUNTIME} -I -B (got {sys.executable}, isolated={sys.flags.isolated}, "
               f"dont_write_bytecode={sys.flags.dont_write_bytecode})")
    home = checked_home(mode)

    tree = SOURCE
    if form == "cli":
        if "--tree" in options:
            refuse("--tree is allowed only for W9's pre-C7 read")
        one_value(rest, "--ledger", ledger)
    else:
        if not rest:
            refuse("script needs a path")
        script = Path(rest[0]).resolve()
        rest = rest[1:]
        if script == GENESIS:
            if mode != "rehearsal":
                refuse("shadow_genesis.py runs only in the rehearsal")
            one_value(rest, "--ledger-id", ledger)
        elif script == PREFLIGHT:
            options_given = [x.split("=", 1)[0] for x in rest if x.startswith("-")]
            if sorted(options_given) != ["--ledgers", "--out", "--tree"]:
                refuse(f"the read-back takes exactly --tree, --out and --ledgers, not {options_given}")
            found = values(rest, "--ledgers")
            if len(found) != 1 or found[0] != READ_BACK[mode]:
                refuse(f"the read-back names --ledgers {' '.join(READ_BACK[mode])}, not {found}")
            if "--tree" in options:
                tree = Path(options["--tree"]).resolve()
                if tree != PRE_C7_SOURCE.resolve():
                    refuse(f"--tree names only the pre-C7 extract {PRE_C7_SOURCE}")
            trees = values(rest, "--tree")
            if len(trees) != 1 or len(trees[0]) != 1 or Path(trees[0][0]).resolve() != tree:
                refuse(f"the read-back's --tree must be the wrapper's tree {tree}")
        elif script == HELPER:
            if "--tree" in options:
                refuse("--tree is allowed only for W9's pre-C7 read")
            one_value(rest, "--ledger", ledger)
        else:
            refuse(f"{script} is not one of the scripts 10d runs")

    sys.path.insert(0, str(tree))
    print(f"wrapper: mode {mode}, ledger {ledger}, home {home}, tree {tree}, form {form}", flush=True)
    code = 0
    try:
        from ssds.core.config import ssds_home

        if ssds_home().resolve() != home:
            refuse(f"the program resolves the home to {ssds_home().resolve()}, not the checked {home}")
        if form == "cli":
            from ssds.cli import main as ssds_main

            sys.argv = ["ssds", *rest]
            code = ssds_main()
        else:
            sys.argv = [str(script), *rest]
            runpy.run_path(str(script), run_name="__main__")
    except SystemExit as exited:
        code = exited.code if isinstance(exited.code, int) else (0 if exited.code is None else 1)
        if not isinstance(exited.code, int) and exited.code is not None:
            print(exited.code)
    except BaseException:  # reported, and the origin check below still decides the exit (review note 8)
        traceback.print_exc()
        code = 1
    finally:
        loaded = {name: Path(m.__file__).resolve() for name, m in list(sys.modules.items())
                  if (name == "ssds" or name.startswith("ssds.")) and getattr(m, "__file__", None)}
        stray = sorted(name for name, path in loaded.items() if not path.is_relative_to(tree))
        print(f"ssds modules: {len(loaded)} loaded, all from {tree}" if loaded and not stray
              else f"ORIGIN FAILURE: {stray or 'no ssds module loaded'}", flush=True)
        if stray or not loaded:
            code = 3
    return code if isinstance(code, int) else 1


if __name__ == "__main__":
    sys.exit(main())
