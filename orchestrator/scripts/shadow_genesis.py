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
``derive`` repeats the end-to-end derivation; it qualifies the ledger first (declared witnesses, a
witness's retirement, the high-water mark) and makes a current assertion only at a current-qualified
head ``H*``, which it then keeps as the high-water mark (Manual §23.4); else historical views only. The repository is
only read: every subject is ``LEGACY(p)`` (the accepted protocol, from
``PROTOCOL-RELEASE-STATE.yaml``) or ``UNGOVERNED``.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import re
import subprocess
import sys
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "orchestrator" / "src"))

from ssds.admission.genesis import (  # noqa: E402
    GenesisRefused,
    GenesisSpec,
    Home,
    HomeRefused,
    admit_genesis,
    prepare_genesis,
)
from ssds.content import read_tree  # noqa: E402
from ssds.core.config import ssds_home  # noqa: E402
from ssds.derivation import consequences  # noqa: E402
from ssds.ledger.qualification import FileWitness, HighWaterMark, WitnessModel, qualify  # noqa: E402
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
    if prepared.report is not None:
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


def qualified_chain(home: Home, ledger_id: str):
    """The verified chain, its qualification against the declared witnesses and high-water mark (§23.4),
    and the prefix a current answer may be derived from: through the qualified head ``H*``, or None.

    Witness and high-water reads happen here, outside derivation (Manual §5.1). Phase D reads file
    witnesses only; a declared witness of another kind counts as not responding.
    """

    chain = read_chain(home.ledger_repository(ledger_id), ledger_id)
    if not chain.entries or chain.genesis is None:
        return chain, None, None
    fields = chain.genesis["fields"]
    model = WitnessModel.from_json(fields["witnesses"])
    reports = {w.id: FileWitness(Path(w.location)).read(ledger_id) if w.kind == "FILE" else None
               for w in model.witnesses}
    host_keys = {k["id"]: k["public_key"] for k in fields["trust_roots"]["admission_keys"]}
    retired = any(FileWitness(Path(w.location)).retired(ledger_id) for w in model.witnesses if w.kind == "FILE")
    store = home.high_water(ledger_id)
    mark = store.get()
    qualification = qualify(chain, reports, model, host_keys, mark, retired=retired)
    prefix = None
    if qualification.current and qualification.head is not None:
        # §23.4: whoever presents current state keeps the last head it qualified; the mark only rises.
        if mark is None or qualification.head > mark.position:
            store.set(HighWaterMark(qualification.head, qualification.head_digest))
        prefix = dataclasses.replace(chain, entries=chain.entries[: qualification.head + 1])
    return chain, qualification, prefix


def derivation_report(home: Home, ledger_id: str, repository: Path) -> dict:
    chain, qualification, prefix = qualified_chain(home, ledger_id)
    trees = lambda commit: read_tree(repository, commit)  # noqa: E731
    report: dict = {
        "ledger_id": ledger_id,
        "entries": len(chain.entries),
        "qualification": qualification.state if qualification else "UNQUALIFIED",
        "qualified_head": None, "qualified_head_digest": None, "provisional": None,
        "critical": list(qualification.critical) if qualification else [],
    }
    if prefix is not None:
        view = consequences(prefix, trees)
        report.update(qualified_head=qualification.head, qualified_head_digest=qualification.head_digest,
                      provisional=qualification.provisional)
        withheld = list(view.assertion_withheld)
    elif chain.genesis is not None and chain.readable_through >= 0:
        view = consequences(chain, trees)  # historical views only: no head is current-qualified
        withheld = [f"qualification {report['qualification']}: historical views only", *view.assertion_withheld]
    else:
        report.update(current_assertion=False, assertion_withheld=["no readable genesis"], subjects={},
                      findings=[], obligations=[])
        return report
    structure = view.s.view.structure
    subjects = sorted(u for u, unit in structure.units.items() if unit.subject)
    report.update(
        position=view.s.n,
        head=view.s.h.chain.entries[view.s.n].digest,
        current_assertion=not withheld,
        assertion_withheld=withheld,
        subjects={s: {"mode": view.s.mode(s), "rev": view.s.cur(s), "valid": view.support.valid(s),
                      "parts": sorted(u for u in structure.units if structure.subj(u) == s and u != s)}
                  for s in subjects},
        findings=[[f.code, f.attention, list(f.about), f.detail] for f in view.findings],
        obligations=[[o.kind, list(o.about), o.detail] for o in view.obligations],
    )
    return report


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
    home.check(ledger_id)
    report = derivation_report(home, ledger_id, repository)
    path = home.write_workspace(ledger_id, "derivation.json",
                                (json.dumps(report, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    print(f"derivation report: {path}")
    print(f"qualification:     {report['qualification']}"
          + (f" at {report['qualified_head']}" if report["qualified_head"] is not None else "")
          + (f", provisional {report['provisional']}" if report["provisional"] is not None else ""))
    print(f"current assertion: {report['current_assertion']}")
    for reason in report["assertion_withheld"]:
        print(f"  withheld: {reason}")
    return 0 if report["current_assertion"] else 1


def derive(args: argparse.Namespace) -> int:
    try:
        return write_derivation(Home(ssds_home()), args.ledger_id, Path(args.repository).resolve())
    except HomeRefused as refused:
        print(f"refused: {refused}")
        return 1


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
