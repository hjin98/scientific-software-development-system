"""A ``LEDGER_LOSS``'s fields, recomputed from what this host reads (catalogue §23.6; Phase F step 7c, readings F54-F56).

The human gate signs a loss whose fields Admission can recompute exactly: the retained head, the replica's last
readable entry ``A``; every abandoned head the witnesses and the high-water mark show beyond ``A`` or off its chain,
each with its witnessed admission status; the content reference of the qualification report gathering those reports,
stored with the entry; and the controls in force at ``A``, which a loss re-establishes unchanged until a control fold
exists (F46). A loss abandoning only proved-never-admitted heads is a ``FORK_RESOLUTION`` with no boundary, and one
abandoning nothing is a redesignation (§23.6, §23.8): both are refused here.
"""

from __future__ import annotations

import hashlib
from collections.abc import Mapping
from typing import Any

from ssds.core.api.v1 import canonical_json
from ssds.derivation import History, TreeSource, trust_roots
from ssds.ledger.qualification import HighWaterMark, WitnessModel, loss_status


def _sorted_keys(keys: Mapping[str, str]) -> list[dict[str, str]]:
    return [{"id": k, "public_key": keys[k]} for k in sorted(keys)]


def controls(chain: Any, trees: TreeSource) -> dict[str, Any]:
    """The controls in force at the chain's last readable entry (F56): witness model, trust roots and ruleset."""

    entries = chain.entries[: chain.readable_through + 1]
    genesis = chain.genesis["fields"]
    roots = trust_roots(entries)
    # genesis's complete trust-root shape (Manual §25.2; revision 24): the folded dispatcher and human keys, and every
    # other member, human_mechanism and any further key list included, at its genesis value, which no admissible
    # lifecycle path changes yet
    return {
        "witnesses": dict(genesis["witnesses"]),  # in force at every position until 7e (F52)
        "trust_roots": {**genesis["trust_roots"], "dispatcher_keys": _sorted_keys(roots.issue),
                        "human_keys": _sorted_keys(roots.humans)},
        "ruleset": dict(History(chain, trees).ruleset(len(entries) - 1)),
    }


def evidence(chain: Any, trees: TreeSource, model: WitnessModel, reports: Mapping[str, Any],
             host_keys: Mapping[str, str], mark: HighWaterMark | None) -> tuple[dict[str, Any], bytes]:
    """The loss's fields and its report object, from the replica's chain, the witnesses' reports (each declared
    witness's checkpoints, or None when it does not respond) and the retained high-water mark (F54-F56)."""

    entries = chain.entries[: chain.readable_through + 1]
    last = entries[-1]
    digests = [e.digest for e in entries]
    declared = [w.id for w in model.witnesses]
    held: dict[str, list[Any]] = {w: sorted((c for c in (reports.get(w) or []) if c.ledger_id == chain.ledger_id
                                             and c.authentic(host_keys)),
                                            key=lambda c: (c.position, c.entry_digest))
                                  for w in declared if reports.get(w) is not None}

    def off_chain(position: int, digest: str) -> bool:
        return position > last.position or digests[position] != digest

    heads = {(c.position, c.entry_digest) for cps in held.values() for c in cps if off_chain(c.position, c.entry_digest)}
    if mark is not None and off_chain(mark.position, mark.entry_digest):
        heads.add((mark.position, mark.entry_digest))
    silent = len(declared) - len(held)

    def status(p: int, d: str) -> str:
        found = loss_status(sum(1 for cps in held.values() if any(c.position == p and c.entry_digest == d for c in cps)),
                            silent, model.f, model.q_a)
        if found == "PROVED_NEVER_ADMITTED" and mark is not None and (p, d) == (mark.position, mark.entry_digest):
            # the mark's head was qualified, so held by q_a: never proved never admitted, even where witnesses lost
            # its checkpoint beyond the fault model (review 8bfaaf0 N2), so no fork resolution abandons it unbounded
            return "POSSIBLY_ADMITTED"
        return found

    abandoned = [{"position": p, "digest": d, "status": status(p, d)} for p, d in sorted(heads)]
    report = canonical_json({
        "ledger_id": chain.ledger_id,
        "replica_head": {"position": last.position, "digest": last.digest},
        "high_water": {"position": mark.position, "entry_digest": mark.entry_digest} if mark is not None else None,
        "witnesses": {w: ([c.to_json() for c in held[w]] if w in held else None) for w in declared},
    })
    fields = {"retained": {"position": last.position, "digest": last.digest}, "abandoned": abandoned,
              "report": "sha256:" + hashlib.sha256(report).hexdigest(), "controls": controls(chain, trees)}
    return fields, report


def loss_problems(fields: Any, expected: Mapping[str, Any]) -> list[str]:
    """Why a loss's ``fields`` cannot be admitted against their recomputation ``expected``; none if they can."""

    if not isinstance(fields, Mapping) or set(fields) != {"retained", "abandoned", "report", "controls"}:
        return ["a loss carries exactly retained, abandoned, report and controls"]
    problems = [f"{name} is not the recomputed {name} (§23.6; readings F54-F56)"
                for name in ("retained", "abandoned", "report", "controls") if fields[name] != expected[name]]
    statuses = [a["status"] for a in expected["abandoned"]]
    if not statuses:
        problems.append("nothing is abandoned: an intact head is a redesignation (§23.8)")
    elif all(s == "PROVED_NEVER_ADMITTED" for s in statuses):
        problems.append("every abandoned head is proved never admitted: a FORK_RESOLUTION with no boundary (§23.6)")
    return problems


__all__ = ["controls", "evidence", "loss_problems"]
