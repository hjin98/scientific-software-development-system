#!/usr/bin/env python3
"""The retirement of the shadow ledger (Phase F step 7a; catalogue §24.2; plan readings F44-F45, SD-64).

Two steps, run by the operator in their own terminal; the human gate between them is the stakeholder's SSH
signature, made with their own key:

    python orchestrator/scripts/retire_shadow.py prepare --public-key ~/.ssh/ssds-genesis.pub
    ssh-keygen -Y sign -f ~/.ssh/ssds-genesis -n ssds <approval message printed by prepare>
    python orchestrator/scripts/retire_shadow.py admit --signature <approval message>.sig

``prepare`` builds the ``LINEAGE_RETIREMENT`` record for the ledger's next position after its current head and
prints the message the human signs; nothing is appended. Its successor is named for discovery only (F44): the
successor ledger's id and its genesis entry digest, read from the successor's own chain in the SSDS home, with no
binding and no claim of equal state. ``admit`` admits the signed record through Admission's lifecycle path with
``obs = null``, at a settled head, and publishes the retirement statement to the witnesses; the ledger then reads
``RETIRED`` and Admission appends nothing more to it. An entry admitted between the two steps moves the head the
approval names, and ``admit`` refuses it: prepare again. The product repository is only read.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "orchestrator" / "src"))

from ssds.admission.engine import Admission, AdmissionHalted, EntryInvalid  # noqa: E402
from ssds.admission.genesis import AdmissionHome  # noqa: E402
from ssds.content import read_tree  # noqa: E402
from ssds.core.api.v1 import canonical_json, ssds_home  # noqa: E402
from ssds.ledger.qualification import HomeRefused  # noqa: E402
from ssds.ledger.read import human_key_id, read_chain, with_id  # noqa: E402

LEDGER_ID = "ssdp-shadow"
SUCCESSOR = "ssdp-shadow-2"


def admission(home: AdmissionHome, ledger_id: str, repository: Path) -> Admission:
    return Admission(home, ledger_id, lambda commit: read_tree(repository, commit))


def successor_genesis(home: AdmissionHome, successor: str) -> str:
    """The successor's genesis entry digest, from its own authenticated chain; never typed in."""

    chain = read_chain(home.ledger_repository(successor), successor)
    if not chain.entries or chain.genesis is None:
        raise SystemExit(f"{successor} has no readable genesis in {home.root}")
    return chain.entries[0].digest


def prepare(args: argparse.Namespace) -> int:
    home = AdmissionHome(ssds_home())
    repository = Path(args.repository).resolve()
    engine = admission(home, args.ledger_id, repository)
    chain = engine.chain()
    if not chain.entries or chain.genesis is None:
        raise SystemExit(f"{args.ledger_id} has no readable genesis")
    genesis = chain.entries[0].lifecycle
    public = Path(args.public_key).expanduser().read_text(encoding="utf-8").strip()
    record = with_id({
        "kind": "LINEAGE_RETIREMENT", "schema": 1, "ruleset": dict(genesis["ruleset"]), "actor": human_key_id(public),
        "actor_class": "HUMAN", "frame": "ADMITTED", "target": None, "basis": [], "outcome": None, "reason": [],
        "supersedes": [], "binding": None, "governs": dict(genesis["governs"]), "provenance": None, "refs": [],
        "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fields": {"successor": {"ledger_id": args.successor, "genesis_digest": successor_genesis(home, args.successor)}},
    })
    message = engine.lifecycle_message(record)
    home.write_workspace(args.ledger_id, "retirement.json", canonical_json(record))
    path = home.write_workspace(args.ledger_id, "retirement-message.txt", message)
    print(f"retires:           {args.ledger_id} after position {len(chain.entries) - 1}")
    print(f"successor:         {json.dumps(record['fields']['successor'])} (discovery only)")
    print(f"approval message:  {path}")
    print(f"sign it with:      ssh-keygen -Y sign -f <your private key> -n ssds {path}")
    return 0


def admit(args: argparse.Namespace) -> int:
    home = AdmissionHome(ssds_home())
    engine = admission(home, args.ledger_id, Path(args.repository).resolve())
    record = json.loads(home.workspace_file(args.ledger_id, "retirement.json").read_bytes())
    signature = Path(args.signature).expanduser().read_text(encoding="utf-8")
    try:
        position = engine.admit_lifecycle(record, signature, None)
    except (AdmissionHalted, EntryInvalid) as refused:
        print(f"retirement not completed: {refused}")
        return 1
    held = engine.qualification(engine.chain())
    print(f"admitted:          LINEAGE_RETIREMENT at {position}")
    print(f"qualification:     {held.state}")
    return 0 if held.state == "RETIRED" else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument("--repository", default=str(REPOSITORY), help="the product repository, only read")
    parser.add_argument("--ledger-id", default=LEDGER_ID)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("prepare", help="build the retirement record and its approval message; appends nothing")
    p.add_argument("--public-key", required=True, help="the stakeholder's OpenSSH Ed25519 public key file")
    p.add_argument("--successor", default=SUCCESSOR, help=f"the successor ledger id (default: {SUCCESSOR})")
    p.set_defaults(run=prepare)
    a = commands.add_parser("admit", help="admit the signed retirement and publish its statement")
    a.add_argument("--signature", required=True, help="the ssh-keygen -Y sign output for the approval message")
    a.set_defaults(run=admit)
    args = parser.parse_args(argv)
    try:
        return args.run(args)
    except HomeRefused as refused:
        print(f"refused: {refused}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
