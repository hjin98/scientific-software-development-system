"""Runbook step A: a read-only preflight of the shadow ledgers through one program tree's own readers.

Run with ``python -I preflight.py --tree <orchestrator/src of the program> --out <report.json>``. It reads each
ledger's chain (``read_raw`` + ``verify_chain``), its qualification (``Admission.qualification``, bound without
``__post_init__`` so no host key is loaded or created), and sweeps the tree's ``record_violations`` over every
record at every position. Nothing is written except the report file.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

LEDGERS = ("ssdp-shadow-2", "ssdp-shadow")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tree", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    tree = args.tree.resolve()
    sys.path.insert(0, str(tree))

    import ssds
    from ssds.admission.engine import Admission
    from ssds.core.config import ssds_home
    from ssds.ledger import read as reader
    from ssds.ledger.qualification import Home
    from ssds.ledger.schema import record_violations

    origin = Path(ssds.__file__).resolve()
    assert origin.is_relative_to(tree), f"ssds loaded from {origin}, not {tree}"
    for name in ("ssds.admission.engine", "ssds.ledger.read", "ssds.ledger.schema", "ssds.ledger.qualification"):
        module = Path(sys.modules[name].__file__).resolve()
        assert module.is_relative_to(tree), f"{name} loaded from {module}"

    home = Home(ssds_home())
    report = {"tree": str(tree), "ssds": str(origin), "home": str(home.root), "ledgers": {}}
    for ledger_id in LEDGERS:
        out: dict = {}
        report["ledgers"][ledger_id] = out
        repository = home.ledger_repository(ledger_id)
        head = reader.ledger_head(repository, ledger_id) if repository.is_dir() else None
        out["head_commit"] = head
        if head is None:
            out["error"] = "no ledger ref"
            continue
        raws = reader.read_raw(repository, head)
        out["entries"] = len(raws)
        try:
            chain = reader.verify_chain(ledger_id, raws)
        except reader.ChainRejected as rejected:
            out["chain_rejected"] = str(rejected)
            continue
        out.update(halt=chain.halt, halt_reasons=list(chain.halt_reasons), unreadable=chain.unreadable,
                   readable_through=chain.readable_through, last_digest=chain.entries[-1].digest,
                   last_lifecycle=(chain.entries[-1].lifecycle or {}).get("kind"))
        sweep = {}
        for entry in chain.entries:
            records = list(entry.records) + ([entry.lifecycle] if entry.lifecycle is not None else [])
            found = [v[:200] for record in records for v in record_violations(record)]
            if found:
                sweep[str(entry.position)] = found
        out["record_violations_by_position"] = sweep
        shell = object.__new__(Admission)  # the real owner's qualification, without loading a host key
        shell.home, shell.ledger_id, shell.fixture_witnesses = home, ledger_id, {}
        try:
            out["qualification"] = shell.qualification(chain).state
        except Exception as failed:  # disclosed, not hidden
            out["qualification_error"] = f"{type(failed).__name__}: {failed}"[:300]

    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for ledger_id, out in report["ledgers"].items():
        print(ledger_id, json.dumps({k: out.get(k) for k in ("entries", "halt", "readable_through", "qualification",
                                                             "record_violations_by_position", "chain_rejected",
                                                             "qualification_error", "error")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
