#!/usr/bin/env python3
"""The shadow genesis of this repository (Phase D step 7; Manual §19.9 Case B).

Three steps, run by the operator in their own terminal; the human gate between
the first two is the stakeholder's SSH signature, made with their own key:

    python orchestrator/scripts/shadow_genesis.py prepare --public-key ~/.ssh/ssds-genesis.pub
    ssh-keygen -Y sign -f ~/.ssh/ssds-genesis -n ssds <approval message printed by prepare>
    python orchestrator/scripts/shadow_genesis.py admit --signature <approval message>.sig

``prepare`` builds and validates the genesis in the SSDS home's isolated
workspace and prints the validation report and the genesis digest; nothing is
published. ``admit`` appends and admits it in the dedicated ledger repository
in the SSDS home, then derives the ledger end to end and writes that report.
``derive`` repeats the end-to-end derivation, reading only. The repository is
only read: every subject is ``LEGACY(p)`` (the accepted protocol, from
``PROTOCOL-RELEASE-STATE.yaml``) or ``UNGOVERNED``.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "orchestrator" / "src"))

from ssds.admission.genesis import GenesisRefused, GenesisSpec, Home, admit_genesis, prepare_genesis  # noqa: E402
from ssds.content import read_tree  # noqa: E402
from ssds.core.config import ssds_home  # noqa: E402
from ssds.derivation import consequences  # noqa: E402
from ssds.ledger.read import read_chain  # noqa: E402

LEDGER_ID = "ssdp-shadow"
PROJECT = "hjin98/scientific-software-development-protocol"
LEGACY_SUBJECTS = ("ssdp.protocol", "ssds8.manual")


def accepted_protocol(repository: Path) -> str:
    """The accepted-current protocol version, resolved from the release-state owner, never assumed."""

    text = (repository / "PROTOCOL-RELEASE-STATE.yaml").read_text(encoding="utf-8")
    match = re.search(r'^accepted_current:\n\s+version:\s*"([^"]+)"', text, re.MULTILINE)
    if not match:
        raise SystemExit("PROTOCOL-RELEASE-STATE.yaml names no accepted_current version")
    return match.group(1)


def resolve_commit(repository: Path, revision: str) -> str:
    result = subprocess.run(["git", "-C", str(repository), "rev-parse", "--verify", "--quiet", revision + "^{commit}"],
                            capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise SystemExit(f"{revision} is not a commit of {repository}")
    return result.stdout.strip()


def prepare(args: argparse.Namespace) -> int:
    repository = Path(args.repository).resolve()
    protocol = accepted_protocol(repository)
    public = Path(args.public_key).expanduser().read_text(encoding="utf-8").strip()
    modes = {s: {"mode": "LEGACY", "protocol": protocol} for s in LEGACY_SUBJECTS}
    modes["*"] = {"mode": "UNGOVERNED"}
    spec = GenesisSpec(project=PROJECT, ledger_id=args.ledger_id, product_repository=repository,
                       baseline_commit=resolve_commit(repository, args.baseline), human_keys=(public,),
                       protocol=protocol, modes=modes)
    prepared = prepare_genesis(spec, Home(ssds_home()), lambda commit: read_tree(repository, commit))
    print(f"validation report: {prepared.report}")
    if not prepared.valid:
        print("genesis refused; nothing was published:")
        for problem in prepared.problems:
            print(f"  - {problem}")
        return 1
    message = prepared.workspace / "approval-message.txt"
    print(f"genesis digest:    {prepared.digest}")
    print(f"approval message:  {message}")
    print(f"sign it with:      ssh-keygen -Y sign -f <your private key> -n ssds {message}")
    return 0


def derivation_report(home: Home, ledger_id: str, repository: Path) -> dict:
    chain = read_chain(home.ledger_repository(ledger_id), ledger_id)
    view = consequences(chain, lambda commit: read_tree(repository, commit))
    structure = view.s.view.structure
    subjects = sorted(u for u, unit in structure.units.items() if unit.subject)
    return {
        "ledger_id": ledger_id,
        "entries": len(chain.entries),
        "head": chain.entries[-1].digest if chain.entries else None,
        "current_assertion": view.current_assertion,
        "assertion_withheld": list(view.assertion_withheld),
        "subjects": {s: {"mode": view.s.mode(s), "rev": view.s.cur(s), "valid": view.support.valid(s),
                         "parts": sorted(u for u in structure.units if structure.subj(u) == s and u != s)}
                     for s in subjects},
        "findings": [[f.code, f.attention, list(f.about), f.detail] for f in view.findings],
        "obligations": [[o.kind, list(o.about), o.detail] for o in view.obligations],
    }


def admit(args: argparse.Namespace) -> int:
    repository = Path(args.repository).resolve()
    home = Home(ssds_home())
    signature = Path(args.signature).expanduser().read_text(encoding="utf-8")
    try:
        admitted = admit_genesis(home, args.ledger_id, signature)
    except GenesisRefused as refused:
        print("genesis refused; nothing was admitted:")
        for problem in refused.problems:
            print(f"  - {problem}")
        return 1
    print(f"admitted:          {admitted.ledger_id} at {admitted.repository}")
    print(f"entry digest:      {admitted.entry_digest}")
    print(f"entry commit:      {admitted.entry_commit}")
    print(f"qualification:     {admitted.qualification}")
    return write_derivation(home, args.ledger_id, repository)


def write_derivation(home: Home, ledger_id: str, repository: Path) -> int:
    report = derivation_report(home, ledger_id, repository)
    path = home.workspace(ledger_id) / "derivation.json"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"derivation report: {path}")
    print(f"current assertion: {report['current_assertion']}")
    return 0 if report["current_assertion"] else 1


def derive(args: argparse.Namespace) -> int:
    return write_derivation(Home(ssds_home()), args.ledger_id, Path(args.repository).resolve())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument("--repository", default=str(REPOSITORY), help="the repository whose history is the baseline")
    parser.add_argument("--ledger-id", default=LEDGER_ID)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("prepare", help="build and validate the genesis; publishes nothing")
    p.add_argument("--public-key", required=True, help="the stakeholder's OpenSSH Ed25519 public key file")
    p.add_argument("--baseline", default="HEAD", help="the baseline commit (default: HEAD)")
    p.set_defaults(run=prepare)
    a = commands.add_parser("admit", help="append and admit the prepared genesis once signed")
    a.add_argument("--signature", required=True, help="the ssh-keygen -Y sign output for the approval message")
    a.set_defaults(run=admit)
    d = commands.add_parser("derive", help="derive the shadow ledger end to end, reading only")
    d.set_defaults(run=derive)
    args = parser.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    raise SystemExit(main())
