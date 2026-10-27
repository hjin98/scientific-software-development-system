"""A discriminating reading's facts, read by one owner (catalogue §6.6; Phase F step 9e, readings F80, F106).

A ``DISCRIMINATING`` ``EVIDENCE_ASSESSMENT`` records ``PASS`` for an execution's outcome under the reading in force
there and ``FAIL`` for ``a⁻``'s reproduced outcome under ``a⁻``'s reading, in one record. Schema 1's
``fields.observations`` carries both, read here under a closed inner shape: exactly two items, the passing item
``{observation: p, reading: {unit, rev}, verdict: "PASS"}`` (``p`` the record's ``target.realization``, its reading
``fields.reading``) and the failing item ``{observation: q, reading: {unit, rev}, verdict: "FAIL", assessment: a⁻}``,
with ``reason`` (a token) and ``reference`` (a ``LEDGER`` digest) present exactly when the two readings differ. ``p``
may be ``q``. The record's outcome is ``PASS`` and it names no failing outputs. Naming ``a⁻`` in the failing item
is a member F80's triple lacks, and the reason vocabulary is undefined: both are Stage S notes. A shape outside this
is not well formed: it covers nothing, and Admission refuses it.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

_DIGEST = re.compile(r"sha256:[0-9a-f]{64}")
_PASS_KEYS = frozenset({"observation", "reading", "verdict"})
_FAIL_KEYS = _PASS_KEYS | {"assessment"}
_DIFFERENCE = frozenset({"reason", "reference"})


@dataclass(frozen=True)
class Reading:
    rid: str
    passing: str | None  # p
    pass_reading: tuple[str, str] | None
    failing: str | None  # q
    fail_reading: tuple[str, str] | None
    failure: str | None  # a⁻
    reason: str | None
    reference: str | None
    problems: tuple[str, ...]

    @property
    def well_formed(self) -> bool:
        return not self.problems


def _unit_rev(value: Any) -> tuple[str, str] | None:
    if isinstance(value, dict) and set(value) == {"unit", "rev"} and all(isinstance(value[k], str) for k in value):
        return value["unit"], value["rev"]
    return None


def is_reading(record: dict[str, Any]) -> bool:
    return record.get("kind") == "EVIDENCE_ASSESSMENT" and (record.get("fields") or {}).get("mode") == "DISCRIMINATING"


def read(rid: str, record: dict[str, Any]) -> Reading:
    """The facts of reading ``rid``, with every way it falls outside the closed shape."""

    fields = record.get("fields") or {}
    target = record.get("target") or {}
    problems: list[str] = []
    if record.get("outcome") != "PASS":
        problems.append("a reading's outcome is PASS")
    if fields.get("failing_outputs"):
        problems.append("a reading names no failing outputs")
    items = fields.get("observations")
    if not (isinstance(items, list) and len(items) == 2 and all(isinstance(i, dict) for i in items)):
        return Reading(rid, None, None, None, None, None, None, None, ("observations are exactly two items",))
    passes = [i for i in items if i.get("verdict") == "PASS"]
    fails = [i for i in items if i.get("verdict") == "FAIL"]
    if len(passes) != 1 or len(fails) != 1:
        return Reading(rid, None, None, None, None, None, None, None, ("one PASS item and one FAIL item",))
    good, bad = passes[0], fails[0]
    if set(good) != _PASS_KEYS:
        problems.append("the PASS item is {observation, reading, verdict}")
    if not (_FAIL_KEYS <= set(bad) <= _FAIL_KEYS | _DIFFERENCE):
        problems.append("the FAIL item is {observation, reading, verdict, assessment} with an optional difference")
    pass_reading, fail_reading = _unit_rev(good.get("reading")), _unit_rev(bad.get("reading"))
    if pass_reading is None or fail_reading is None:
        problems.append("each reading is {unit, rev}")
    p, q, failure = good.get("observation"), bad.get("observation"), bad.get("assessment")
    if not all(isinstance(x, str) and _DIGEST.fullmatch(x) for x in (p, q, failure)):
        problems.append("observations and the failure are record identities")
    if p != target.get("realization"):
        problems.append("the PASS item's observation is the record's target")
    if pass_reading is not None and pass_reading != _unit_rev(fields.get("reading")):
        problems.append("the PASS item's reading is the record's reading")
    differ = pass_reading != fail_reading
    present = _DIFFERENCE & set(bad)
    reason, reference = bad.get("reason"), bad.get("reference")
    if differ and present != _DIFFERENCE or not differ and present:
        problems.append("a reason and a reference exactly when the readings differ")
    if "reason" in bad and not (isinstance(reason, str) and reason):
        problems.append("the reason is a token")
    if "reference" in bad and not (isinstance(reference, str) and _DIGEST.fullmatch(reference)):
        problems.append("the reference is a LEDGER digest")
    return Reading(rid, p if isinstance(p, str) else None, pass_reading, q if isinstance(q, str) else None,
                   fail_reading, failure if isinstance(failure, str) else None,
                   reason if isinstance(reason, str) else None, reference if isinstance(reference, str) else None,
                   tuple(problems))


__all__ = ["Reading", "is_reading", "read"]
