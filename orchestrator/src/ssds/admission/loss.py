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
from ssds.ledger.qualification import HighWaterMark, WitnessModel, lineage_witnesses, loss_status, segments


def _sorted_keys(keys: Mapping[str, str]) -> list[dict[str, str]]:
    return [{"id": k, "public_key": keys[k]} for k in sorted(keys)]


def controls(chain: Any, trees: TreeSource) -> dict[str, Any]:
    """The controls in force at the chain's last readable entry (F56): witness model, trust roots and ruleset. The
    witness model is the last segment's (F59)."""

    entries = chain.entries[: chain.readable_through + 1]
    genesis = chain.genesis["fields"]
    roots = trust_roots(entries)
    # genesis's complete trust-root shape (Manual §25.2; revision 24): the folded dispatcher and human keys, and every
    # other member, human_mechanism and any further key list included, at its genesis value, which no admissible
    # lifecycle path changes yet
    return {
        "witnesses": in_force(chain).to_json(),
        "trust_roots": {**genesis["trust_roots"], "dispatcher_keys": _sorted_keys(roots.issue),
                        "human_keys": _sorted_keys(roots.humans)},
        "ruleset": dict(History(chain, trees).ruleset(len(entries) - 1)),
    }


def in_force(chain: Any) -> WitnessModel:
    """The witness model in force at the chain's end: its last segment's (F59)."""

    found = [m for _, m in segments(chain)]
    if not found or found[-1] is None:
        raise ValueError("no witness model in force")
    return found[-1]


def _segment_model(found: list, position: int) -> WitnessModel:
    """The model of the newest segment ``position`` lies in: a head is counted over its own witnesses (review
    ae5ab38 N1)."""

    return next(m for start, m in reversed(found) if start <= position and m is not None)


def evidence(chain: Any, trees: TreeSource, reports: Mapping[str, Any], host_keys: Mapping[str, str],
             mark: HighWaterMark | None) -> tuple[dict[str, Any], bytes]:
    """The loss's fields and its report object, from the replica's chain, every segment's witnesses' reports (each
    one's checkpoints, or None when it does not respond) and the retained high-water mark (F54-F56). Each head's
    status counts the witnesses of the segment its position lies in."""

    entries = chain.entries[: chain.readable_through + 1]
    last = entries[-1]
    digests = [e.digest for e in entries]
    found = segments(chain)
    declared = [w.id for w in lineage_witnesses(chain)]
    held: dict[str, list[Any]] = {w: sorted((c for c in (reports.get(w) or []) if c.ledger_id == chain.ledger_id
                                             and c.authentic(host_keys)),
                                            key=lambda c: (c.position, c.entry_digest))
                                  for w in declared if reports.get(w) is not None}

    def off_chain(position: int, digest: str) -> bool:
        return position > last.position or digests[position] != digest

    # a head an admitted resolution or loss already abandoned is not abandoned again: qualification no longer reads
    # it (``_abandoned``), and naming it would bar every later fork resolution behind an old loss
    gone = {a.get("digest") for e in entries if (e.lifecycle or {}).get("kind") in ("FORK_RESOLUTION", "LEDGER_LOSS")
            for a in e.lifecycle["fields"]["abandoned"] if isinstance(a, Mapping)}
    heads = {(c.position, c.entry_digest) for cps in held.values() for c in cps
             if off_chain(c.position, c.entry_digest) and c.entry_digest not in gone}
    if mark is not None and off_chain(mark.position, mark.entry_digest) and mark.entry_digest not in gone:
        heads.add((mark.position, mark.entry_digest))

    def status(p: int, d: str) -> str:
        model = _segment_model(found, p)
        own = [w.id for w in model.witnesses]
        h = sum(1 for w in own if any(c.position == p and c.entry_digest == d for c in held.get(w, [])))
        status = loss_status(h, sum(1 for w in own if w not in held), model.f, model.q_a)
        if status == "PROVED_NEVER_ADMITTED" and mark is not None and (p, d) == (mark.position, mark.entry_digest):
            # the mark's head was qualified, so held by q_a: never proved never admitted, even where witnesses lost
            # its checkpoint beyond the fault model (review 8bfaaf0 N2), so no fork resolution abandons it unbounded
            return "POSSIBLY_ADMITTED"
        return status

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
                for name in ("retained", "abandoned", "report") if fields[name] != expected[name]]
    problems += controls_problems(fields["controls"], expected["controls"])
    statuses = [a["status"] for a in expected["abandoned"]]
    if not statuses:
        problems.append("nothing is abandoned: an intact head is a redesignation (§23.8)")
    elif all(s == "PROVED_NEVER_ADMITTED" for s in statuses):
        problems.append("every abandoned head is proved never admitted: a FORK_RESOLUTION with no boundary (§23.6)")
    return problems


def new_model(raw: Any, current: Mapping[str, Any]) -> tuple[WitnessModel | None, list[str]]:
    """A re-established witness model: well formed, ``quorum_sound`` and class-sound (``WitnessModel.validate``, the
    "deployment_classes_sound at redesignation"), and different from the model in force (readings F60, F62)."""

    try:
        model = WitnessModel.from_json(raw)
        model.validate()
    except (KeyError, TypeError, ValueError, AttributeError) as exc:
        return None, [f"the new witness model is not sound: {exc}"]
    if model == WitnessModel.from_json(current):
        return None, ["the new witness model is the one in force"]
    return model, []


def controls_problems(controls: Any, expected: Mapping[str, Any]) -> list[str]:
    """A loss re-establishes the controls in force (F46): equal, except that its witness member may name a new sound
    set, the redesignation it carries (F62)."""

    if not isinstance(controls, Mapping) or set(controls) != set(expected):
        return ["controls is not the recomputed controls (§23.6; readings F54-F56)"]
    problems = [f"controls' {name} is not the one in force (F46)" for name in expected
                if name != "witnesses" and controls[name] != expected[name]]
    if controls["witnesses"] != expected["witnesses"]:
        problems += new_model(controls["witnesses"], expected["witnesses"])[1]
    return problems


def redesignation_problems(fields: Any, head: Any, expected: Mapping[str, Any], unqualified: bool,
                           refs: Any) -> list[str]:
    """Why a ``WITNESS_SET_REDESIGNATION``'s ``fields`` cannot be admitted after ``head`` (reading F60): exactly a
    sound new model and ``continues_from`` the intact head, with no evidence of a later head (any is a loss's, F62);
    under ``UNQUALIFIED`` the record's ``refs`` names the stored report its continuity rests on, and otherwise none."""

    if not isinstance(fields, Mapping) or set(fields) != {"witnesses", "continues_from"}:
        return ["a redesignation carries exactly its witnesses and continues_from"]
    problems = new_model(fields["witnesses"], expected["controls"]["witnesses"])[1]
    if fields["continues_from"] != head.digest:
        problems.append("continues_from is not the intact head it is appended after (§23.8)")
    if expected["abandoned"]:
        problems.append("a later head is in evidence: a LEDGER_LOSS re-establishing the witness set carries it (F62)")
    wanted = [report_ref(expected["report"])] if unqualified else []
    if refs != wanted:
        problems.append("under UNQUALIFIED the record names the report its continuity rests on, and otherwise none "
                        "(§23.8; F60)")
    return problems


def report_ref(digest: str) -> dict[str, str]:
    return {"store": "LEDGER", "digest": digest, "media_type": "application/json"}


def resolution_problems(fields: Any, expected: Mapping[str, Any]) -> list[str]:
    """Why a ``FORK_RESOLUTION``'s ``fields`` cannot be admitted against the loss evidence ``expected``; none if they
    can (§23.6; reading F58). It abandons exactly the heads a loss would name, every one proved never admitted, so it
    sets no boundary: any other abandonment is a ``LEDGER_LOSS``. The replica keeps its own side; choosing the side it
    does not hold needs a ref restore (F47)."""

    if not isinstance(fields, Mapping) or set(fields) != {"abandoned"}:
        return ["a fork resolution carries exactly its abandoned heads"]
    problems = [] if fields["abandoned"] == expected["abandoned"] else \
        ["abandoned is not the recomputed abandoned (§23.6; readings F54, F58)"]
    statuses = [a["status"] for a in expected["abandoned"]]
    if not statuses:
        problems.append("nothing is abandoned: there is no fork to resolve")
    elif any(s != "PROVED_NEVER_ADMITTED" for s in statuses):
        problems.append("a head not proved never admitted is abandoned only by a LEDGER_LOSS (§23.6)")
    return problems


__all__ = ["controls", "controls_problems", "evidence", "in_force", "loss_problems", "new_model",
           "redesignation_problems", "report_ref", "resolution_problems"]
