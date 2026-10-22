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
(reading E1): ``read`` returns content at the answer's basis and records nothing.
``open``, which renders a derived obligation's brief labeled ``NOT ISSUED``, is
step 7's. A query naming nothing it can answer about is :class:`Refused`.
"""

from __future__ import annotations

import dataclasses
from collections.abc import Callable
import inspect
from dataclasses import dataclass
from typing import Any, Protocol

from ssds import derivation
from ssds.ledger.qualification import HighWaterMark, Qualification, WitnessModel, qualify


class Refused(ValueError):
    """A request the Interface refuses before presenting anything: an unknown query class, arguments the query
    cannot take, a reference naming nothing, or content that cannot be read."""


class LedgerAccess(Protocol):
    """What the Interface reads of one ledger, supplied by the composition root."""

    ledger_id: str

    def chain(self) -> Any: ...

    def witness_reports(self, model: WitnessModel) -> tuple[dict[str, Any], bool]:
        """Each declared witness's report (None when it does not respond), and whether one declares retirement."""

    def high_water(self) -> HighWaterMark | None: ...

    def raise_high_water(self, mark: HighWaterMark) -> None: ...


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
    fields = chain.genesis["fields"]
    model = WitnessModel.from_json(fields["witnesses"])
    reports, retired = access.witness_reports(model)
    host_keys = {k["id"]: k["public_key"] for k in fields["trust_roots"]["admission_keys"]}
    mark = access.high_water()
    qualification = qualify(chain, reports, model, host_keys, mark, retired=retired)
    if qualification.current and qualification.head is not None:
        # §23.4: whoever presents current state keeps the last head it qualified; the mark only rises.
        if mark is None or qualification.head > mark.position:
            access.raise_high_water(HighWaterMark(qualification.head, qualification.head_digest))
        prefix = dataclasses.replace(chain, entries=chain.entries[: qualification.head + 1])
        view = derivation.consequences(prefix, trees)
        withheld = tuple(view.assertion_withheld)
    elif chain.readable_through >= 0:
        view = derivation.consequences(chain, trees)
        withheld = (f"qualification {qualification.state}: historical views only", *view.assertion_withheld)
    else:
        return Presented(access.ledger_id, len(chain.entries), qualification, None, ("no readable entry",))
    return Presented(access.ledger_id, len(chain.entries), qualification, derivation.Workflow(view.support), withheld)


_QUERIES = ("governs", "depends", "explain", "evidence", "blocked", "stale", "impact", "verify", "locate", "tensions",
            "history", "search", "changed")


class Session:
    """``ask`` and ``read`` at one presented head (snapshot isolation, §16.1)."""

    def __init__(self, access: LedgerAccess, trees: Callable[[str], Any]) -> None:
        self.access = access
        self.trees = trees
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
