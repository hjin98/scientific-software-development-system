"""What the Dispatcher would issue, and from which head (catalogue §9, §23.4; Phase F step 8a, reading F65).

The Dispatcher issues only at a named head ``H*``: ``QUALIFIED`` with no provisional entry, composed by the Ledger
Store's one function (``ledger.qualification.currentness``) from what the composition root reads. The would-issue
set is every obligation an agent role holds that derivation finds ``READY`` at ``H*``, an item's readiness covering
its "dispatch" and "re-dispatch" routes. Human-held obligations are briefs, not tasks, and the Dispatcher's own
obligations (``REISSUE``) are its mechanical duty (step 8g).
"""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from typing import Any

from ssds.derivation import AGENT_ROLES, READY, Workflow, derive


class NotIssuable(RuntimeError):
    """The head is not a named ``H*``: the Dispatcher issues nothing from it (§23.4)."""


@dataclass(frozen=True)
class Task:
    task_id: str
    obligation_id: str
    kind: str
    holder: str
    contract: str  # "item" or "system": a system contract's id waits on Q-F17 (reading F66)

    def to_json(self) -> dict[str, str]:
        return dataclasses.asdict(self)


def task_id(obligation_id: str, position: int) -> str:
    """One task per obligation per head: its identity, stable across a restart (the journal's intent)."""

    return f"task-{position}-{obligation_id.removeprefix('sha256:')[:16]}"


def would_issue(chain: Any, trees: Any, held: Any) -> tuple[Task, ...]:
    """The tasks the Dispatcher would issue at ``held``'s head, the qualified prefix's workflow read there."""

    if not held.current or held.provisional is not None or held.head is None:
        raise NotIssuable(f"the ledger is {held.state} at {held.head}, provisional {held.provisional}: "
                          f"nothing is issued (§23.4)")
    prefix = dataclasses.replace(chain, entries=chain.entries[: held.head + 1])
    workflow = Workflow(derive(prefix, trees))
    out = []
    for o in workflow.obligations:
        if o.holder in AGENT_ROLES and workflow.readiness(o).state == READY:
            contract = "item" if workflow.item_of(o) is not None else "system"
            out.append(Task(task_id(o.id, held.head), o.id, o.kind, o.holder, contract))
    return tuple(sorted(out, key=lambda t: t.task_id))


def issue(journal: Any, issuer: Any, task: Task, held: Any, *, contract_revision: Any, governs: Any, route: str,
          brief: bytes | None = None) -> Any:
    """Issue ``task`` at ``held``'s head, written ahead (reading F65): the intent, then the signed envelope, then
    its hand-out. A crash before the hand-out leaves an intent that ``Journal.recover`` abandons."""

    if not held.current or held.provisional is not None or task.task_id != task_id(task.obligation_id, held.head):
        raise NotIssuable(f"{task.task_id} is not issued at the named head {held.head} (§23.4)")
    journal.intent(task.task_id, task.obligation_id, held.head, held.head_digest)
    issued = issuer.issue(task_id=task.task_id, obligation_id=task.obligation_id, role=task.holder,
                          contract_revision=contract_revision, governs=governs, route=route,
                          issued_at_position=held.head, brief=brief)
    journal.issued(task.task_id, issued.binding())
    journal.handed(task.task_id)
    return issued


def observe(chain: Any, trees: Any, held: Any) -> dict[str, Any]:
    """``dispatcher serve`` on a shadow ledger: the would-issue set at ``H*``, issuing nothing and writing no run ref
    (reading F8)."""

    report: dict[str, Any] = {"ledger_id": chain.ledger_id, "qualification": held.state, "head": held.head,
                              "head_digest": held.head_digest, "issued": [],
                              "mode": "observe-only: nothing is issued and no run ref is written (F8)"}
    try:
        report["would_issue"] = [t.to_json() for t in would_issue(chain, trees, held)]
    except NotIssuable as refused:
        report["would_issue"], report["withheld"] = [], str(refused)
    return report


__all__ = ["NotIssuable", "Task", "issue", "observe", "task_id", "would_issue"]
