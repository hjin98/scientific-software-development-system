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
    contract_revision: dict[str, str]  # the item's {unit, rev}, or the system contract id (SD-77, reading F66)
    surfaces: tuple[str, ...] = ()  # the serialization surfaces its write scope meets (§9.2, reading F67)
    plan: str | None = None  # a principal's coordination task: its plan, at most one at a time (§9.2, §12.5)

    def to_json(self) -> dict[str, Any]:
        return dataclasses.asdict(self)


def task_id(obligation_id: str, position: int) -> str:
    """One task per obligation per head: its identity, stable across a restart (the journal's intent)."""

    return f"task-{position}-{obligation_id.removeprefix('sha256:')[:16]}"


def would_issue(chain: Any, trees: Any, held: Any, open_tasks: Any = ()) -> tuple[Task, ...]:
    """The tasks the Dispatcher would issue at ``held``'s head, the qualified prefix's workflow read there, after
    the scheduling constraints against the tasks still open (``held_back``)."""

    return issuable(ready(chain, trees, held), open_tasks)[0]


def ready(chain: Any, trees: Any, held: Any) -> tuple[Task, ...]:
    """Every ``READY`` agent-held obligation at ``held``'s head, as a task, before scheduling."""

    if not held.current or held.provisional is not None or held.head is None:
        raise NotIssuable(f"the ledger is {held.state} at {held.head}, provisional {held.provisional}: "
                          f"nothing is issued (§23.4)")
    prefix = dataclasses.replace(chain, entries=chain.entries[: held.head + 1])
    workflow = Workflow(derive(prefix, trees))
    out = []
    for o in workflow.obligations:
        if o.holder in AGENT_ROLES and workflow.readiness(o).state == READY:
            surfaces, plan = workflow.serialization(o)
            out.append(Task(task_id(o.id, held.head), o.id, o.kind, o.holder, workflow.contract_revision(o),
                            surfaces, plan))
    return tuple(sorted(out, key=lambda t: t.task_id))


def issuable(tasks: Any, open_tasks: Any) -> tuple[tuple[Task, ...], tuple[tuple[Task, str], ...]]:
    """Scheduling (§9.1-§9.2, reading F67; scheduling only, never correctness): no second task for an obligation
    with one open; at most one open task per serialization surface its write scope meets; at most one open
    coordination task per plan. ``open_tasks`` are the journal's open intents; a task this batch admits counts as
    open for the ones after it. Returns the issuable tasks and the held ones with why."""

    obligations = {t["obligation_id"] for t in open_tasks}
    surfaces = {s: t["task_id"] for t in open_tasks for s in t.get("surfaces") or ()}
    plans = {t["plan"]: t["task_id"] for t in open_tasks if t.get("plan")}
    out, held = [], []
    for task in tasks:
        if task.obligation_id in obligations:
            held.append((task, "its obligation has a task open"))
            continue
        busy = [s for s in task.surfaces if s in surfaces]
        if busy:
            held.append((task, f"serialization surface {busy[0]} is held by {surfaces[busy[0]]}"))
            continue
        if task.plan is not None and task.plan in plans:
            held.append((task, f"plan {task.plan} has coordination task {plans[task.plan]} open"))
            continue
        out.append(task)
        obligations.add(task.obligation_id)
        surfaces.update((s, task.task_id) for s in task.surfaces)
        if task.plan is not None:
            plans[task.plan] = task.task_id
    return tuple(out), tuple(held)


def issue(journal: Any, issuer: Any, task: Task, held: Any, *, governs: Any, route: str,
          brief: bytes | None = None) -> Any:
    """Issue ``task`` at ``held``'s head, written ahead (reading F65): the intent, then the signed envelope, then
    its hand-out. A crash before the hand-out leaves an intent that ``Journal.recover`` abandons. The envelope carries
    the task's contract revision, which each record bound to it copies (step 8b, reading F66; SD-77)."""

    if not held.current or held.provisional is not None or task.task_id != task_id(task.obligation_id, held.head):
        raise NotIssuable(f"{task.task_id} is not issued at the named head {held.head} (§23.4)")
    allowed, refused = issuable((task,), journal.open_tasks())
    if not allowed:
        raise NotIssuable(f"{task.task_id} is held: {refused[0][1]} (review 546cc86 N2; reading F67)")
    journal.intent(task.task_id, task.obligation_id, held.head, held.head_digest, task.surfaces, task.plan)
    issued = issuer.issue(task_id=task.task_id, obligation_id=task.obligation_id, role=task.holder,
                          contract_revision=task.contract_revision, governs=governs, route=route,
                          issued_at_position=held.head, brief=brief)
    journal.issued(task.task_id, issued.binding())
    journal.handed(task.task_id)
    return issued


def brief_for(chain: Any, trees: Any, held: Any, task: Task, route: str, doctrine: Any) -> bytes:
    """The rendered brief a task is issued with (§16.4; reading F69): its obligation's brief at the head it is
    issued at, naming the task and its route, so ``open(task)`` reproduces these bytes at the task's basis."""

    from ssds.interface.render import Renderer

    prefix = dataclasses.replace(chain, entries=chain.entries[: held.head + 1])
    workflow = Workflow(derive(prefix, trees))
    o = next(o for o in workflow.obligations if o.id == task.obligation_id)
    head = {"label": "QUALIFIED", "position": held.head, "digest": held.head_digest}
    renderer = Renderer(workflow, head, doctrine, {"task_id": task.task_id, "route": route})
    return renderer.brief(o).text.encode("utf-8")


@dataclass(frozen=True)
class Judge:
    name: str  # "agent:fresh-reviewer" or a human's actor id
    route: str  # HARNESS for a freshly launched agent, MANUAL for a human


#: A freshly launched agent reviewer, as derivation names it among the eligible judges.
FRESH_REVIEWER = "agent:fresh-reviewer"


def select_judge(workflow: Any, o: Any) -> Judge | None:
    """The judge a judgment task goes to (§16.5, RR-11; step 8d, reading F72): among derivation's eligible judges,
    which already exclude what the answer judges' authors are, a freshly launched agent reviewer on the harness route,
    whose launch names no input session, so it reads no authoring session; otherwise an eligible human on the manual
    route, whose independence is §5.10 (f)'s human rule; with none, nothing (readiness waits)."""

    eligible = workflow.eligible_judges(o)
    if FRESH_REVIEWER in eligible:
        return Judge(FRESH_REVIEWER, "HARNESS")
    humans = sorted(e for e in eligible if e.startswith("human:"))
    return Judge(humans[0], "MANUAL") if humans else None


def judge_provenance(issued: Any, model_family: str | None, toolchain: str | None) -> dict[str, Any]:
    """What the submitting adapter stamps into a judge's record's ``provenance.judge`` (§12.2, §16.5): lineage class,
    route, model family and toolchain. An unverified audit fact: authentication and derivation never read it, the
    binding's verified class is what counts, and a policy asking for a model family fails closed (reading F72)."""

    envelope = issued.envelope
    return {"judge": {"lineage_class": envelope["lineage_class"], "route": envelope["route"],
                      "model_family": model_family, "toolchain": toolchain}}


def observe(chain: Any, trees: Any, held: Any) -> dict[str, Any]:
    """``dispatcher serve`` on a shadow ledger: the would-issue set at ``H*``, issuing nothing and writing no run ref
    (reading F8)."""

    report: dict[str, Any] = {"ledger_id": chain.ledger_id, "qualification": held.state, "head": held.head,
                              "head_digest": held.head_digest, "issued": [],
                              "mode": "observe-only: nothing is issued and no run ref is written (F8)"}
    try:
        allowed, deferred = issuable(ready(chain, trees, held), ())
        report["would_issue"] = [t.to_json() for t in allowed]
        report["held"] = [{**t.to_json(), "because": why} for t, why in deferred]
    except NotIssuable as refused:
        report["would_issue"], report["held"], report["withheld"] = [], [], str(refused)
    return report


__all__ = ["FRESH_REVIEWER", "Judge", "NotIssuable", "Task", "brief_for", "issuable", "issue", "judge_provenance",
           "observe", "ready", "select_judge", "task_id", "would_issue"]
