"""The logical operations ``ask`` and ``read`` and the qualified presentation of every answer (Manual §16.1-§16.2).

The Interface owns presenting anything as current (catalogue §26.1): it qualifies
the chain against the declared witnesses, a witness's retirement and the
high-water mark before deriving (witness reads stay outside derivation, Manual
§5.1), derives the qualified prefix through ``H*``, and keeps ``H*`` as the
high-water mark, never lowering it (§23.4; Phase D repairs A-B1, A-B5, A-B7, NF5).
With no current-qualified head every answer is labeled ``UNQUALIFIED`` and is a
historical view; at a qualified head whose derivation withholds the current
assertion the head is ``QUALIFIED`` and ``current_assertion`` is false. Every
answer names the head it was derived at.

The Interface holds no state of its own and reads no Git: its caller (the root
module) supplies a :class:`LedgerAccess` and a tree source. Phase E has no tasks
(reading E1): ``read`` returns content at the answer's basis and records nothing;
``open`` renders a derived obligation's brief, labeled ``NOT ISSUED``, and
``inspect`` the inspector view (``interface.render``). A query naming nothing it
can answer about is :class:`Refused`.
"""

from __future__ import annotations

import dataclasses
import hashlib
from collections.abc import Callable, Iterable, Mapping
import inspect
from dataclasses import dataclass
from typing import Any, Protocol

from ssds import derivation
from ssds.ledger.qualification import HighWaterMark, Qualification, WitnessSpec, currentness, lineage_witnesses

from .render import Doctrine, Renderer


class Refused(ValueError):
    """A request the Interface refuses before presenting anything: an unknown query class, arguments the query
    cannot take, a reference naming nothing, or content that cannot be read."""


class LedgerAccess(Protocol):
    """What the Interface reads of one ledger, supplied by the composition root."""

    ledger_id: str

    def chain(self) -> Any: ...

    def witness_reports(self, witnesses: Iterable[WitnessSpec]) -> tuple[dict[str, Any], dict[str, Any]]:
        """Each witness's report (None when it does not respond), and the retirement statement it holds
        (``FileWitness.statement``; None when it holds none); the witnesses are every segment's (reading F59)."""

    def high_water(self) -> HighWaterMark | None: ...

    def ancestry(self) -> Callable[[str, str], bool | None] | None:
        """The commit-graph reader over the ledger repository that publication classification reads (§22.2;
        reading F119)."""

    def raise_high_water(self, mark: HighWaterMark) -> None: ...


class TaskAccess(Protocol):
    """An issued task's envelope and its recorded reads, supplied by the composition root from the Dispatcher's
    journal (Phase F step 8e, reading F69); the Interface imports no Dispatcher module."""

    def envelope(self, task_id: str) -> Mapping[str, Any] | None: ...

    def record_read(self, task_id: str, read: Mapping[str, Any]) -> None: ...


@dataclass(frozen=True)
class Presented:
    """One ledger presented at its qualified head, or as historical views when none is current."""

    ledger_id: str
    entries: int
    qualification: Qualification | None
    workflow: Any  # a derivation.Workflow over the presented prefix, or None with no readable genesis
    withheld: tuple[str, ...]

    @property
    def state(self) -> str:
        return self.qualification.state if self.qualification is not None else "UNQUALIFIED"

    @property
    def current(self) -> bool:
        return self.workflow is not None and not self.withheld

    @property
    def head(self) -> dict[str, Any]:
        """The head an answer names (§16.2, §23.4)."""

        if self.workflow is None:
            return {"label": "UNQUALIFIED", "position": None, "digest": None}
        s = self.workflow.s
        qualified = self.qualification is not None and self.qualification.current
        label = "QUALIFIED" if qualified else "UNQUALIFIED"
        return {"label": label, "position": s.n, "digest": s.h.chain.entries[s.n].digest, "qualification": self.state}


def present(access: LedgerAccess, trees: Callable[[str], Any]) -> Presented:
    chain = access.chain()
    if not chain.entries or chain.genesis is None:
        return Presented(access.ledger_id, len(chain.entries), None, None, ("no readable genesis",))
    reports, statements = access.witness_reports(lineage_witnesses(chain))
    mark = access.high_water()
    qualification = currentness(chain, reports, statements, mark)  # the Ledger Store's one composition (F65)
    if qualification.current and qualification.head is not None:
        # §23.4: whoever presents current state keeps the last head it qualified; the mark only rises.
        if mark is None or qualification.head > mark.position:
            access.raise_high_water(HighWaterMark(qualification.head, qualification.head_digest))
        prefix = dataclasses.replace(chain, entries=chain.entries[: qualification.head + 1])
        view = derivation.consequences(prefix, trees, ancestry=access.ancestry())
        withheld = tuple(view.assertion_withheld)
    elif chain.readable_through >= 0:
        view = derivation.consequences(chain, trees, ancestry=access.ancestry())
        withheld = (f"qualification {qualification.state}: historical views only", *view.assertion_withheld)
    else:
        return Presented(access.ledger_id, len(chain.entries), qualification, None, ("no readable entry",))
    return Presented(access.ledger_id, len(chain.entries), qualification, derivation.Workflow(view.support), withheld)


_QUERIES = ("governs", "depends", "explain", "evidence", "blocked", "stale", "impact", "verify", "locate", "tensions",
            "history", "search", "changed")


class Session:
    """``ask`` and ``read`` at one presented head (snapshot isolation, §16.1)."""

    def __init__(self, access: LedgerAccess, trees: Callable[[str], Any], doctrine: Doctrine | None = None) -> None:
        self.access = access
        self.trees = trees
        self.doctrine: Doctrine = doctrine or (lambda source, path: None)
        self.presented = present(access, trees)

    def _answer(self, query: str, answer: Any) -> dict[str, Any]:
        return {"query": query, "head": self.presented.head, "answer": answer}

    def status(self) -> dict[str, Any]:
        """The ledger's qualification, the current assertion and the derived subjects and obligations."""

        p = self.presented
        out: dict[str, Any] = {"ledger_id": p.ledger_id, "entries": p.entries, "qualification": p.state, "head": p.head,
                               "current_assertion": p.current, "assertion_withheld": list(p.withheld)}
        if p.qualification is not None:
            out.update(provisional=p.qualification.provisional, critical=list(p.qualification.critical))
        if p.workflow is None:
            return out
        w = p.workflow
        structure = w.s.view.structure
        subjects = sorted(u for u, unit in structure.units.items() if unit.subject and structure.subj(u) == u)
        out["subjects"] = {s: {"mode": w.s.mode(s), "rev": w.s.cur(s), "status": derivation.queries.status(w, s)}
                           for s in subjects}
        out["obligations"] = [{"id": o.id, "kind": o.kind, "holder": o.holder, "plan": o.plan, "target": o.target,
                               "readiness": w.readiness(o).state, "discharge": w.discharge(o)} for o in w.obligations]
        return out

    def ask(self, query: str, *args: Any) -> dict[str, Any]:
        """A typed query of §16.2 at the presented head."""

        if query not in _QUERIES:
            raise Refused(f"unknown query {query!r}; the query classes are {', '.join(_QUERIES)}")
        function = getattr(derivation.queries, query)
        if query == "changed":
            try:
                args = (int(args[0]), list(args[1:]) or None) if args else (0, None)
            except ValueError:
                raise Refused("changed takes a ledger position, then units") from None
        try:
            inspect.signature(function).bind(None, *args)
        except TypeError as exc:
            raise Refused(f"{query}: {exc}") from None
        w = self.presented.workflow
        if w is None:
            return self._answer(query, None)
        if query in ("impact", "verify"):
            args = (*args[:-1], self.trees(args[-1]))  # the last argument is a commit naming the workspace
        try:
            return self._answer(query, function(w, *args))
        except derivation.queries.QueryError as exc:
            raise Refused(str(exc)) from None

    def open(self, obligation: str) -> dict[str, Any]:
        """The brief of a derived obligation at the presented head, labeled ``NOT ISSUED`` (reading E1)."""

        w = self.presented.workflow
        if w is None:
            return self._answer("open", None)
        found = next((o for o in w.obligations if o.id == obligation), None)
        if found is None:
            raise Refused(f"{obligation} is not an obligation derived at the presented head")
        return self._answer("open", Renderer(w, self.presented.head, self.doctrine).brief(found).to_json())

    # -- an issued task (Phase F step 8e, reading F69) ----------------------------------------------------------

    def _task(self, task_id: str, tasks: TaskAccess) -> tuple[Mapping[str, Any], Any, dict[str, Any]]:
        """The task's envelope, the workflow at its basis (``issued_at_position``) and that head, or ``Refused``."""

        envelope = tasks.envelope(task_id)
        if envelope is None:
            raise Refused(f"{task_id} is no task the Dispatcher issued")
        w = self.presented.workflow
        basis = envelope["issued_at_position"]
        if w is None or not isinstance(basis, int) or basis > w.s.n:
            raise Refused(f"{task_id}'s basis {basis} is not within the presented qualified prefix")
        at = w.at(basis)
        head = {"label": "QUALIFIED", "position": basis, "digest": at.s.h.chain.entries[basis].digest}
        return envelope, at, head

    def open_task(self, task_id: str, tasks: TaskAccess) -> dict[str, Any]:
        """The issued task's brief at its basis; refused unless it is the brief the envelope's digest names."""

        envelope, at, head = self._task(task_id, tasks)
        found = next((o for o in at.obligations if o.id == envelope["obligation_id"]), None)
        if found is None:
            raise Refused(f"{envelope['obligation_id']} is not derived at {task_id}'s basis")
        brief = Renderer(at, head, self.doctrine, {"task_id": task_id, "route": envelope["route"]}).brief(found)
        if envelope.get("brief") is not None and brief.digest != envelope["brief"]:
            raise Refused(f"{task_id}'s brief renders to {brief.digest}, not the {envelope['brief']} it was issued")
        return {"query": "open", "task": task_id, "head": head, "answer": brief.to_json()}

    def read_task(self, task_id: str, ref: str, tasks: TaskAccess) -> dict[str, Any]:
        """Content at the task's basis, the read recorded in its basis (§16.4)."""

        _, at, head = self._task(task_id, tasks)
        view = at.s.view
        if ref in view.structure.units:
            region = view.regions.get(ref) or ()
            text = b"".join(view.tree[s.path].data[s.start:s.end] for s in region).decode("utf-8", "replace")
            answer, read = {"unit": ref, "rev": view.rev(ref), "content": text}, {"unit": ref, "rev": view.rev(ref)}
        elif ref in view.tree:
            data = view.tree[ref].data
            answer = {"path": ref, "content": data.decode("utf-8", "replace")}
            read = {"path": ref, "digest": "sha256:" + hashlib.sha256(data).hexdigest()}
        else:
            raise Refused(f"{ref} is neither a unit nor a path at {task_id}'s basis")
        tasks.record_read(task_id, read)
        return {"query": "read", "task": task_id, "head": head, "answer": answer}

    def changed_since_basis(self, task_id: str, tasks: TaskAccess, units: list[str] | None = None) -> dict[str, Any]:
        """``ask(changed)`` for a task: since its basis, over its work's subjects unless ``units`` are named."""

        envelope, at, _ = self._task(task_id, tasks)
        w = self.presented.workflow
        if units is None:
            found = next((o for o in at.obligations if o.id == envelope["obligation_id"]), None)
            units = sorted(at.briefing.work(found).subjects) if found is not None else None
        return self._answer("changed", derivation.queries.changed(w, envelope["issued_at_position"], units))

    def inspect(self) -> dict[str, Any]:
        """The inspector view: open human attention by ``(-w, c, p, id)``, then the digest (§16.8)."""

        w = self.presented.workflow
        if w is None:
            return self._answer("inspect", None)
        return self._answer("inspect", Renderer(w, self.presented.head, self.doctrine).inspector())

    def read(self, ref: str) -> dict[str, Any]:
        """Content by unit identity or path at the answer's basis; nothing is recorded (no task basis, E1)."""

        w = self.presented.workflow
        if w is None:
            return self._answer("read", None)
        view = w.s.view
        if ref in view.structure.units:
            region = view.regions.get(ref) or ()
            text = b"".join(view.tree[s.path].data[s.start:s.end] for s in region).decode("utf-8", "replace")
            return self._answer("read", {"unit": ref, "rev": view.rev(ref), "content": text})
        if ref in view.tree:
            return self._answer("read", {"path": ref, "content": view.tree[ref].data.decode("utf-8", "replace")})
        raise Refused(f"{ref} is neither a unit nor a path at the presented head")


__all__ = ["LedgerAccess", "Presented", "Refused", "Session", "present"]
