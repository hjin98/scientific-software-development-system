"""A realization's facts, read by one owner (catalogue §6.3, §17.2, §17.5; Phase F step 9c-ii-i, readings F78, F88).

``fields.execution`` is schema 1's open object; its members are §17.2's, read here under a closed inner shape: the
recorded basis (``tree``, ``context``, ``units``, ``reads``, ``widened``, ``pins``, ``unpinnable``, ``attributes``,
``bounded_by``), the runner (``{class, key}``, the key equal to the actor's ``@<key id>``), its class's recorded
``class_attributes`` and ``observes_outside_reads`` (recorded by value at realization, §6.3), the ``start`` and
``end`` positions when recorded, and ``incomplete``, one of §17.2's reasons, present exactly when the outcome is
``INCOMPLETE``, as ``evaluated`` is exactly when it is ``COMPLETE``. A shape outside this is not well formed: it serves
no permissive use, and its adverse uses are unchanged (F88).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

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


def read(rid: str, record: dict[str, Any]) -> Realization:
    """The facts of ``REALIZATION`` record ``rid``, with every way its execution falls outside the closed shape."""

    fields = record.get("fields") or {}
    execution = fields.get("execution") if isinstance(fields.get("execution"), dict) else {}
    target = record.get("target") or {}
    spec = target.get("spec") or {}
    problems: list[str] = []
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
        if key in execution and not _position(execution[key]):
            problems.append(f"{key} is a position")
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
    else:
        problems.append("attributes are [name, value] pairs")
    claims = tuple((c.get("unit"), c.get("rev")) for c in target.get("claim") or [] if isinstance(c, dict))
    return Realization(rid, spec.get("unit"), spec.get("rev"), claims, outcome, runner.get("class"), runner.get("key"),
                       tuple(attributes_named), observes, attributes, execution.get("unpinnable", True) is not False,
                       incomplete, tuple(problems))


__all__ = ["INCOMPLETE_REASONS", "Realization", "read"]
