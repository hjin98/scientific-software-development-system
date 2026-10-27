"""A realization's facts, read by one owner (catalogue §6.3, §17.2, §17.5; Phase F step 9c-ii-i, readings F78, F88).

``fields.execution`` is schema 1's open object; its members are §17.2's, read here under a closed inner shape: the
recorded basis (``tree``, ``context``, ``units``, ``reads``, ``widened``, ``pins``, ``unpinnable``, ``attributes``,
``bounded_by``), the runner (``{class, key}``, the key equal to the actor's ``@<key id>``), its class's recorded
``class_attributes`` and ``observes_outside_reads`` (recorded by value at realization, §6.3), the ``start`` and
``end`` positions (``start ≤ end``), and ``incomplete``, one of §17.2's reasons, present exactly when the outcome is
``INCOMPLETE``, as ``evaluated`` is exactly when it is ``COMPLETE``. The basis members are typed, ``tree``,
``context``, ``units`` and ``bounded_by`` required (F96), so no consumer indexes an unchecked value. A shape outside
this is not well formed: it serves no permissive use, and its adverse uses are unchanged (F88).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ssds.content import recorded_identity
from ssds.ledger.read import SYSTEM_RULESET, is_commit

INCOMPLETE_REASONS = frozenset({"FAILED_TO_START", "CRASHED", "TIME_BOUND", "MALFORMED_OUTPUT", "CANCELLED"})
_BASIS = frozenset({"tree", "context", "units", "reads", "widened", "pins", "unpinnable", "attributes", "bounded_by"})
_EXECUTION = _BASIS | {"runner", "class_attributes", "observes_outside_reads", "start", "end", "incomplete"}


@dataclass(frozen=True)
class Realization:
    rid: str
    spec: str
    spec_rev: str
    claims: tuple[tuple[str, str], ...]
    outcome: str
    runner_class: str | None
    runner_key: str | None
    class_attributes: tuple[str, ...]
    observes_outside_reads: bool
    attributes: dict[str, Any]
    unpinnable: bool
    incomplete: str | None
    problems: tuple[str, ...]

    @property
    def well_formed(self) -> bool:
        return not self.problems


def _position(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _strings(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(v, str) for v in value)


def _identified(value: Any) -> bool:
    """A list of ``[term, identity]`` pairs."""

    return isinstance(value, list) and all(isinstance(p, list) and len(p) == 2 and isinstance(p[0], dict)
                                           and isinstance(p[1], str) for p in value)


def basis_problems(execution: Any) -> list[str]:
    """Every way an execution basis's members fall outside their types (F96). Empty for a well-typed basis, which
    ``on_minus`` and ``execution_current`` may then index."""

    if not isinstance(execution, dict):
        return ["the execution is an object"]
    problems = []
    if not is_commit(execution.get("tree")):
        problems.append("tree is a commit")
    context = execution.get("context")
    if not (isinstance(context, dict) and set(context) == {"system", "ignore", "analyzers"}
            and isinstance(context["system"], str) and _strings(context["ignore"]) and _strings(context["analyzers"])):
        problems.append("context is {system, ignore, analyzers}")
    units = execution.get("units")
    if not (isinstance(units, list) and all(isinstance(u, dict) and set(u) == {"unit", "rev", "terms"}
                                            and isinstance(u["unit"], str) and isinstance(u["rev"], str)
                                            and _identified(u["terms"]) for u in units)):
        problems.append("units are {unit, rev, terms}")
    bounded = execution.get("bounded_by")
    if not (bounded == "UNBOUNDED" or _strings(bounded)):
        problems.append('bounded_by is "UNBOUNDED" or record ids')
    for key in ("reads", "widened"):
        if key in execution and not _identified(execution[key]):
            problems.append(f"{key} are [term, identity] pairs")
    if "pins" in execution and not (isinstance(execution["pins"], list) and all(
            isinstance(p, list) and len(p) == 2 and all(isinstance(x, str) for x in p) for p in execution["pins"])):
        problems.append("pins are [name, value] pairs")
    if "unpinnable" in execution and not isinstance(execution["unpinnable"], bool):
        problems.append("unpinnable is a boolean")
    pairs = execution.get("attributes", [])
    if not (isinstance(pairs, list) and all(isinstance(p, list) and len(p) == 2 and isinstance(p[0], str)
                                            for p in pairs)):
        problems.append("attributes are [name, value] pairs")
    return problems


def context_available(execution: dict[str, Any], analyzers: Any) -> bool:
    """The host has the recorded context: its ruleset system and every analyzer (§6.3)."""

    context = execution.get("context", {})
    return context.get("system", SYSTEM_RULESET) == SYSTEM_RULESET and set(context.get("analyzers", ())) <= set(analyzers)


def on_minus(execution: dict[str, Any], tree: Any, analyzers: Any) -> bool | None:
    """``on⁻(o, K)`` for a well-typed basis (F97): every recorded tree-resident term re-resolves, under the record's
    own context, to its identity in ``tree``. ``None`` when the host lacks the recorded context, which makes no
    current assertion (§6.3). The one owner Admission and ``Assessments`` both read."""

    if not context_available(execution, analyzers):
        return None
    ignore = tuple(execution["context"]["ignore"])
    terms = [t for entry in execution["units"] for t in entry["terms"]]
    terms += list(execution.get("reads", [])) + list(execution.get("widened", []))
    return all(recorded_identity(tree, term, ignore) == cid for term, cid in terms)


def read(rid: str, record: dict[str, Any]) -> Realization:
    """The facts of ``REALIZATION`` record ``rid``, with every way its execution falls outside the closed shape."""

    fields = record.get("fields") or {}
    execution = fields.get("execution") if isinstance(fields.get("execution"), dict) else {}
    target = record.get("target") or {}
    spec = target.get("spec") or {}
    problems: list[str] = basis_problems(execution)
    if set(execution) - _EXECUTION:
        problems.append(f"unknown execution members {sorted(set(execution) - _EXECUTION)}")
    runner = execution.get("runner")
    if not (isinstance(runner, dict) and set(runner) == {"class", "key"}
            and all(isinstance(runner[k], str) and runner[k] for k in ("class", "key"))):
        problems.append("the runner is {class, key}")
        runner = {}
    actor = record.get("actor")
    if runner and not (isinstance(actor, str) and actor.startswith("machinery:") and actor.endswith("@" + runner["key"])):
        problems.append("the runner's key is the actor's")
    attributes_named = execution.get("class_attributes")
    if not (isinstance(attributes_named, list) and all(isinstance(a, str) for a in attributes_named)):
        problems.append("class_attributes lists the attributes the runner class records")
        attributes_named = []
    observes = execution.get("observes_outside_reads")
    if not isinstance(observes, bool):
        problems.append("observes_outside_reads is recorded")
        observes = False
    for key in ("start", "end"):
        if not _position(execution.get(key)):
            problems.append(f"{key} is a position")
    if _position(execution.get("start")) and _position(execution.get("end")) and execution["start"] > execution["end"]:
        problems.append("start ≤ end")
    outcome = record.get("outcome")
    incomplete = execution.get("incomplete")
    if (outcome == "INCOMPLETE") != (incomplete is not None) or \
            (incomplete is not None and incomplete not in INCOMPLETE_REASONS):
        problems.append("an INCOMPLETE realization records one of §17.2's reasons, a complete one none")
    if (outcome == "COMPLETE") != (fields.get("evaluated") is not None):
        problems.append("a COMPLETE realization, and only one, names its evaluated outcome")
    pairs = execution.get("attributes") or []
    attributes = {}
    if isinstance(pairs, list) and all(isinstance(p, list) and len(p) == 2 and isinstance(p[0], str) for p in pairs):
        attributes = {k: v for k, v in pairs}
    claims = tuple((c.get("unit"), c.get("rev")) for c in target.get("claim") or [] if isinstance(c, dict))
    return Realization(rid, spec.get("unit"), spec.get("rev"), claims, outcome, runner.get("class"), runner.get("key"),
                       tuple(attributes_named), observes, attributes, execution.get("unpinnable", True) is not False,
                       incomplete, tuple(problems))


__all__ = ["INCOMPLETE_REASONS", "Realization", "basis_problems", "context_available", "on_minus", "read"]
