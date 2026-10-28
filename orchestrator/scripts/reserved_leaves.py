#!/usr/bin/env python3
"""The inputs of SD-69's in-place repair request (Phase F step 10d; plan readings F21, F121, F122).

Once ``admission serve`` has absorbed the observed branch's commit declaring ``ssds.manifest`` and ``ssds.policy``,
their declaration keys are quarantined. This script reads the ledger through the program, only reading, and writes
what ``ssds submit --prepare`` takes: ``records.json``, one ``INTAKE_DISPOSITION`` ``ABSORB`` per quarantined key
of the two reserved leaves, naming that key's current delta (``State.current_delta``), and one ``delta-<n>.json``
per key, the adopted element ``{absorption, key, value}``. It prints the ``--prepare`` command; nothing is
prepared, signed or admitted here:

    python orchestrator/scripts/reserved_leaves.py --ledger ssdp-shadow-2 --repository . --actor <human> --out <dir>

Each record carries the ledger's current ruleset and the genesis record's ``governs``. The absorbed content's
authorship is ``UNKNOWN``, so each ``ABSORB`` is non-independent, disclosed: §18.4 enacts it at S0 regardless.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "orchestrator" / "src"))

from ssds.admission.engine import RESERVED_LEAVES  # noqa: E402
from ssds.cli import Composition  # noqa: E402
from ssds.content import value_to_json  # noqa: E402
from ssds.derivation import derive  # noqa: E402
from ssds.derivation.history import History  # noqa: E402


def repair_inputs(composition: Composition, recorded_at: str) -> tuple[list[dict], list[dict]]:
    """The dispositions (each without ``id``, actor or binding: ``--prepare`` fills them) and the adopted elements,
    in key order."""

    chain = composition.access.chain()
    entries = chain.entries[: chain.readable_through + 1]
    state = derive(chain, composition.trees, ancestry=composition.access.ancestry()).s
    keys = sorted(k for k in state.s0.quarantine if k[0] in RESERVED_LEAVES)
    if not keys:
        raise SystemExit("no declaration key of ssds.manifest or ssds.policy is quarantined at the head: run "
                         "admission serve after the declarations' commit")
    ruleset = dict(History(chain, composition.trees).ruleset(len(entries) - 1))
    governs = chain.entries[0].entry["lifecycle"]["governs"]
    records, deltas = [], []
    for key in keys:
        current = state.current_delta(key)
        if current is None:
            raise SystemExit(f"{key} is quarantined but has no current delta (F21): absorb the head again")
        absorption, value = current
        target = {"absorption": absorption, "key": list(key)}
        deltas.append({**target, "value": value_to_json(key[1], value)})
        records.append({"kind": "INTAKE_DISPOSITION", "schema": 1, "ruleset": ruleset, "frame": "ADMITTED",
                        "target": target, "basis": [], "outcome": "ABSORB", "reason": [], "supersedes": [],
                        "governs": governs, "provenance": None, "refs": [], "recorded_at": recorded_at,
                        "fields": {}})
    return records, deltas


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--repository", type=Path, default=Path("."))
    parser.add_argument("--actor", required=True, help="the human (human:SHA256:...) who will sign")
    parser.add_argument("--out", required=True, type=Path, help="a new directory for the inputs")
    args = parser.parse_args(argv)
    recorded_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    records, deltas = repair_inputs(Composition(args.ledger, args.repository), recorded_at)
    args.out.mkdir(parents=True, exist_ok=False)
    (args.out / "records.json").write_text(json.dumps(records, indent=2, sort_keys=True) + "\n")
    adopt = []
    for n, delta in enumerate(deltas, 1):
        path = args.out / f"delta-{n}.json"
        path.write_text(json.dumps(delta, indent=2, sort_keys=True) + "\n")
        adopt += ["--adopt", str(path)]
    for delta in deltas:
        print(f"ABSORB {delta['key'][0]}.{delta['key'][1]} = {json.dumps(delta['value'])} ({delta['absorption']})")
    print("prepare the request with:\n  ssds submit --ledger " + " ".join(
        [args.ledger, "--prepare", str(args.out / "records.json"), "--actor", args.actor, *adopt]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
