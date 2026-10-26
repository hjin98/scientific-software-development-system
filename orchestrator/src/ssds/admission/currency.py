"""Validation step 6, currency (Manual §8.3 step 6; catalogue §8.3 step 6; Phase F plan, step 4e-ii, readings
F10, F26-F28).

Each basis entry of each checked record is evaluated on the head's ``Support`` in the record's frame, never in the
trial, and a record with an unsatisfied entry is refused ``STALE_BASIS``. The frame is:
- for any record of a request carrying a transformation ``X`` (an integration or a records-only adoption), ``D_n[X]``
  with in-frame roles: the request is a frame record of its own transformation (catalogue §8.3 step 6);
- otherwise, for an ``ADMITTED`` record, the head ``D_n``;
- for a record declaring an unintegrated ``X``, ``D_n[X]`` with in-frame roles, ``X`` as the trial gives it (a
  co-submitted result may fix it), and for one declaring an integrated
  ``X``, the head with ``X``'s frame fixed at its integration (§7.3's admitted-state column, reading F17).

A support-tier record other than a report is checked; never-lost records are exempt (F28). Derivation owns every
value (``Support.stale_entries``); Admission decides.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ssds.derivation import Frame, State, Support, transformation_of
from ssds.ledger.read import SUPPORT_TIER

from .request import REPORT_KINDS, never_lost


class Currency:
    """Step 6 at one head, with the frame states it builds kept for the request."""

    def __init__(self, head: Any, change: Any = None) -> None:
        self.head = head
        self.change = change
        self._states: dict[Any, Any] = {}

    def codes(self, record: Mapping[str, Any], trial: Any) -> set[str]:
        """``record``'s step 6 code, its transformation read from ``trial``, where a co-submitted result fixes it."""

        kind = record["kind"]
        if kind not in SUPPORT_TIER or kind in REPORT_KINDS or never_lost(record):
            return set()
        if not record.get("basis"):
            return set()  # no entry to satisfy
        located = self.locate(record, trial)
        if located is None:
            return {"STALE_BASIS"}  # its frame does not exist (§7.4): no entry is satisfied there
        support, frame = located
        return {"STALE_BASIS"} if support.stale_entries(dict(record), frame) else set()

    def locate(self, record: Mapping[str, Any], trial: Any) -> tuple[Any, Any] | None:
        """The support a record's entries are read on and the frame giving their roles; ``None`` when that frame
        does not exist. ``X`` is built at the head as the trial gives it (the 4e row)."""

        s = self.head.s
        declared = record["frame"]
        if self.change is None and declared == "ADMITTED":
            return self.head, None
        if self.change is not None:
            key, frame = None, self.change
            if key not in self._states:
                self._states[key] = Support(State(s.h, s.n, frame))
        else:
            transformation = declared["transformation"]
            if s.enactment(transformation) in s.integrated:
                frame = self.head.transformation_frame(transformation)
                return (self.head, frame) if frame is not None else None
            # X as this round's trial gives it: a fixing result refused in an earlier round fixes nothing now
            # (review 8408e05 B2), so the cache is keyed on what fixes X, never on its name alone
            x = transformation_of(trial.s, transformation)
            if x is None:
                return None
            key = (x, trial.s.enactment(transformation))
            if key not in self._states:
                frame = Frame(s.h, s.n, x, key[1])
                self._states[key] = Support(State(s.h, s.n, frame)) if frame.exists else None
        support = self._states[key]
        return (support, support.s.frame) if support is not None else None


__all__ = ["Currency"]
