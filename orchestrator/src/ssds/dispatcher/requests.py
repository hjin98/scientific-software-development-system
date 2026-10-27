"""The Dispatcher's requests: integration requests and the re-request of an overtaken basis (catalogue §9.1, §11.5;
Phase F step 8g-i, reading F73).

An integrating request is §11.5 (3)'s: "the candidate plus references to those admitted records", carrying no new
judgment. The task's ``TASK_RESULT`` is its own records-only request, admitted first (§11.5 (1)); the integrating
request carries no record, and Admission reads the transformation that admitted result submits, with its judgments,
from the ledger (F32), signed by the producing task's credential. Under SD-70 Admission refuses it
``SCHEMA_UNSUPPORTED`` until A10's D4 (review of 26907956, B3).

A request whose basis is overtaken is revalidated, never silently admitted (§9.1). Admission revalidates first: its
step 9 absorbs the observed head and revalidates the same request there. The Dispatcher acts only on that outcome:
while it is pending the task stays open, so no second task is issued for its obligation (``issuable``). Once it is
known, the old task is finished and derivation's own route at the new head governs: a new task is issued only where
the obligation is ``READY`` again, and the old basis is never resubmitted (reading F73; plan check of 53216046).

A ``REISSUE(envelope)`` obligation is the Dispatcher's mechanical duty (R0; step 8g-ii, reading F74): the original
task is re-issued by a key in force, its envelope copying the original's task, obligation, role, contract revision and
``governs``, and each retained record is resubmitted unchanged but for its binding and a provenance citing the
refusal, keeping its original actor and lineage. The re-issue's route is ``MANUAL``: the resubmission launches no
session, so no launch is attested for one; authentication checks the records' lineage against the retained record.
"""

from __future__ import annotations

import dataclasses
import json
from typing import Any

from ssds.admission.request import binding_digest, resubmitted
from ssds.derivation import Workflow, derive

from .schedule import NotIssuable, Task, ready


def integration_request(issued: Any, candidate: str, base_position: int, base_commit: str) -> dict[str, Any]:
    """The integrating request for ``candidate``, which the producing task ``issued``'s admitted result submits
    (§11.5 (3)): no record, the references read from the ledger."""

    request: dict[str, Any] = {"binding": None, "claims": [], "base_position": base_position, "base_commit": base_commit,
                               "candidates": [candidate], "adopted_deltas": [], "records": [], "objects": {}}
    request["binding"] = issued.binding(request)
    return request


def rerequest(journal: Any, task: Task, decision: Any, chain: Any, trees: Any, held: Any) -> Task | None:
    """§9.1, on Admission's outcome ``decision`` for ``task``'s request: finish ``task``; if derivation at ``held``'s
    head finds its obligation ``READY`` again, the new task to issue there (the caller issues it through ``issue``),
    else None."""

    if decision is None:
        raise ValueError("the Dispatcher acts only on Admission's outcome (reading F73)")
    journal.finished(task.task_id)
    return next((t for t in ready(chain, trees, held) if t.obligation_id == task.obligation_id), None)


def reissues(chain: Any, trees: Any, held: Any) -> list[tuple[dict[str, Any], dict[str, dict[str, Any]]]]:
    """Each ``REISSUE`` obligation derived at ``held``'s head: the original envelope, read from the binding object
    stored with the refusal, and the retained records it lists (refused identity -> retained body)."""

    if not held.current or held.provisional is not None or held.head is None:
        raise NotIssuable(f"the ledger is {held.state} at {held.head}: nothing is re-issued (§23.4)")
    prefix = dataclasses.replace(chain, entries=chain.entries[: held.head + 1])
    objects = {d: o for e in prefix.entries for d, o in e.objects.items()}
    out = []
    for o in Workflow(derive(prefix, trees)).obligations:
        if o.kind == "REISSUE":
            original = json.loads(objects[o.target["envelope"]])["envelope"]
            out.append((original, {rid: json.loads(objects[rid]) for rid in o.params["records"]}))
    return out


def reissue(issuer: Any, original: dict[str, Any], held: Any) -> Any:
    """The original task re-issued by ``issuer``'s key, in force, at the named head ``held`` (reading F74)."""

    if not held.current or held.provisional is not None or held.head is None:
        raise NotIssuable(f"the ledger is {held.state} at {held.head}: nothing is re-issued (§23.4)")
    return issuer.issue(task_id=original["task_id"], obligation_id=original["obligation_id"], role=original["role"],
                        contract_revision=original["contract_revision"], governs=original["governs"], route="MANUAL",
                        issued_at_position=held.head, predecessors=original.get("predecessors"))


def resubmission(issued: Any, retained: dict[str, dict[str, Any]], base_position: int, base_commit: str) -> dict[str, Any]:
    """The request resubmitting ``retained`` (refused identity -> retained body, as a ``REISSUE`` obligation lists
    them) under the re-issued task ``issued``."""

    digest = binding_digest(issued.binding())
    request: dict[str, Any] = {"binding": None, "claims": [], "base_position": base_position, "base_commit": base_commit,
                               "candidates": [], "adopted_deltas": [], "objects": {},
                               "records": [resubmitted(body, rid, digest) for rid, body in sorted(retained.items())]}
    request["binding"] = issued.binding(request)
    return request


__all__ = ["integration_request", "reissue", "reissues", "rerequest", "resubmission"]
