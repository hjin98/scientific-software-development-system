"""Revision runs and revision-assessment records (catalogue §10.2; SD-16, SD-19, SD-22, SD-25, SD-26).

These rules apply to every ``NATIVE`` subject of declared kind D1 or D2.

- The **revision run** of ``s`` in state ``G`` is ``rid_G(s) = (s, ι)``: ``ι`` identifies the event
  at which ``cur(s)`` took its current value in ``G`` (or ``s``'s tenure started, if later): an
  integration's enactment (its producing task), and for every other event the admitting entry's
  identity. In a frame ``D_n[X]`` where ``X`` changes ``cur(s)`` or starts ``s``'s tenure, ``ι`` is
  ``X``'s enactment, the event its integration would be; otherwise the run is ``D_n``'s.
- A record **names** the run of ``s`` in the state it declares at its admission: its frame
  ``D_p[X]``, or ``D_p``. Catalogue §10.2 has machinery fill the field and Admission check it; it is
  that function of the record's frame and position, so derivation computes it and the ledger's
  closed schema needs no field for it (Phase E plan, reading E19).
- A record is **in the run** of ``s`` in ``G`` iff it acts in ``G`` and names ``rid_G(s)``.
- A **revision-assessment record** for ``(s, r)`` is an admitted ``TASK_RESULT`` whose
  ``revision_assessments`` slot is complete and holds an entry naming exactly ``s`` and ``r``, from an
  ``AUTHOR`` task whose candidate yields ``r`` or a task bound to the revising review ``REVIEW(s, r)``.
"""

from __future__ import annotations

from typing import Any

from .obligations import obligation_id

Run = tuple[str, str]  # (subject, event)
REVISING_REVIEW = "REVIEW_REVISION"


def revising_review_id(subject: str, rev: str, run: Run) -> str:
    """The identity of ``REVIEW(s, r)`` in run ``run`` (§10.2: the run is among its parameters)."""

    return obligation_id(REVISING_REVIEW, {"subject": subject, "rev": rev}, {"run": list(run)})


def _cache(history: Any) -> dict[Any, Any]:
    cache = history.__dict__.get("_runs_cache")
    if cache is None:
        cache = history.__dict__["_runs_cache"] = {}
    return cache


def admitted_run(history: Any, position: int, subject: str) -> Run | None:
    """``rid_{D_p}(s)``, or None when ``s`` is not a unit at ``p``."""

    from .state import State  # a State imports this module

    key = ("admitted", position, subject)
    cache = _cache(history)
    if key in cache:
        return cache[key]
    run: Run | None = None
    if subject in history.view(position).structure.units:
        changed = 0
        for k in range(position, 0, -1):
            before, after = history.view(k - 1), history.view(k)
            if subject not in before.structure.units or before.rev(subject) != after.rev(subject):
                changed = k
                break
        tenure = State(history, position).tenure(subject)
        event = max(changed, tenure or 0)
        integration = history.integrations.get(event)
        enactment = None
        if integration is not None and integration.transformation:
            at_event = State(history, event)
            enactment = at_event.enactment(integration.transformation)
            if enactment is not None and at_event.integrated.get(enactment) != event:
                enactment = None  # a second integration of one enactment (Admission refuses it) is its own event
        run = (subject, f"enactment:{enactment}" if enactment else f"entry:{history.chain.entries[event].digest}")
    cache[key] = run
    return run


class Runs:
    """The runs of one state (admitted or a frame)."""

    def __init__(self, state: Any) -> None:
        self.s = state

    def rid(self, subject: str) -> Run | None:
        s = self.s
        frame = s.frame
        if frame is not None and frame.enactment:
            admitted = s.h.view(s.n)
            here = s.view.structure.units.get(subject)
            before = admitted.structure.units.get(subject)
            if here is not None and (before is None or s.view.rev(subject) != admitted.rev(subject)
                                     or here.scope != before.scope
                                     or s.view.structure.kind(subject) != admitted.structure.kind(subject)):
                return subject, f"enactment:{frame.enactment}"
        return admitted_run(s.h, s.n, subject)

    def named(self, rid: str, subject: str) -> Run | None:
        """The run of ``subject`` a record names: in the state it declares at its admission."""

        from .frames import frame_state
        from .state import State

        s = self.s
        position = s.position_of(rid)
        frame = s.record(rid)["frame"]
        if frame == "ADMITTED":
            return admitted_run(s.h, position, subject)
        key = ("frame", position, frame["transformation"], subject)
        cache = _cache(s.h)
        if key not in cache:
            declared = frame_state(s.h, position, frame["transformation"], State(s.h, position))
            cache[key] = Runs(declared).rid(subject) if declared is not None else None
        return cache[key]

    def in_run(self, rid: str, subject: str) -> bool:
        run = self.rid(subject)
        return run is not None and self.s.acts(rid) and self.named(rid, subject) == run

    # -- revision-assessment records ---------------------------------------------------------

    def assessment_records(self, subject: str, rev: str) -> tuple[str, ...]:
        """Every admitted revision-assessment record for ``(s, r)``, in position order."""

        out = []
        for rid in self.s.of_kind("TASK_RESULT"):
            record = self.s.record(rid)
            entries = (record.get("fields") or {}).get("slots", {}).get("revision_assessments")
            if not isinstance(entries, list) or not entries or not all(
                    isinstance(e, dict) and isinstance(e.get("subject"), str) and isinstance(e.get("rev"), str)
                    for e in entries):
                continue  # an incomplete slot is no revision assessment (§14.3 slots_filled)
            if not any(e["subject"] == subject and e["rev"] == rev for e in entries):
                continue
            if self._authored(rid, subject, rev) or self._revising_review(rid, subject, rev):
                out.append(rid)
        return tuple(out)

    def _authored(self, rid: str, subject: str, rev: str) -> bool:
        """The result of a task whose candidate yields ``r`` for ``s``."""

        from .frames import Frame, transformation_of

        target = self.s.record(rid)["target"]
        transformation = target.get("transformation")
        if not transformation:
            return False
        x = transformation_of(self.s, transformation)
        if x is None:
            return False
        frame = Frame(self.s.h, self.s.position_of(rid), x, self.s.enactment(transformation))
        return frame.candidate_rev(subject) == rev

    def _revising_review(self, rid: str, subject: str, rev: str) -> bool:
        binding = self.s.record(rid).get("binding") or {}
        run = self.named(rid, subject)
        return run is not None and binding.get("obligation") == revising_review_id(subject, rev, run)

    def counting_premise(self, rid: str, subject: str, rev: str) -> bool:
        """A passing acceptance or gate decision carries a ``standing`` entry on a revision-assessment
        record for ``(s, r)`` in the run (§10.2; whether that record stands is read through the entry)."""

        records = set(self.assessment_records(subject, rev))
        return any(entry["mode"] == "standing" and entry["target"].get("record") in records
                   and self.in_run(entry["target"]["record"], subject)
                   for entry in self.s.record(rid)["basis"])
