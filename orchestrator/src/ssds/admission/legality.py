"""Validation step 7, legality: the checks of Phase F step 5b-i (catalogue §8.3 step 7; Manual §8.3 step 7; plan
§3.2, readings F31, F34, F36).

Admission decides here and derivation supplies every fact, read at the current head:
- the bound obligation exists there: the head derives it (``OBLIGATION_NOT_DERIVED``, F34);
- a request bound to a task claims a discharge only with that task's result, or as its integration request (§11.5
  (3)): a mid-task report request carries none and claims nothing (``OBLIGATION_CLAIM_UNSUPPORTED``);
- one ``TASK_RESULT`` per task, the task its authenticated binding names, over the head and the request
  (``OBLIGATION_RESULT_DUPLICATE``);
- a claimed obligation is undischarged at the head: a duplicate discharge is rejected and recorded
  (``OBLIGATION_DISCHARGED``);
- a ``TASK_RESULT`` bound to an obligation already discharged, or naming a contract revision that is not current,
  is refused under that classification (F31: ``OBLIGATION_DISCHARGED``, ``OBLIGATION_CONTRACT_STALE``);
- once a judgment obligation is answered (§10.3) in the frame a passing judgment is read in, a later passing
  judgment bound to it there is refused, unless it supersedes (step 3 authorized it) or is a ``GATE_DECISION``
  (``OBLIGATION_ANSWERED``; step 5b-ii);
- revision assessments first: a passing ``ACCEPTANCE`` or ``GATE_DECISION ACCEPT`` on a ``NATIVE`` D1/D2 triple
  needs a revision-assessment record for ``(s, r)`` already admitted that counts there (in the run, standing), and
  a ``standing`` entry on it (``OBLIGATION_REVIEW_OPEN``; step 5b-ii).

The last two read the record's frame as step 6 locates it (``Currency.locate``).
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ssds.derivation import F, Workflow, passing

from .request import never_lost

#: The discharge states in which a further discharge is a duplicate (§10.4).
_DISCHARGED = frozenset({"DISCHARGED", "DISCHARGED_PROVISIONAL"})


class Legality:
    """Step 7 at one head, its workflow built once for the request."""

    def __init__(self, head: Any, locate: Any = None) -> None:
        self.head = head
        self.w = Workflow(head)
        self._derived = {o.id for o in self.w.obligations}
        self.locate = locate  # step 6's frame locator: (support, frame) for a record, or None
        self._workflows: dict[int, Any] = {}

    def request_codes(self, request: Mapping[str, Any], records: list[Mapping[str, Any]]) -> set[str]:
        """The request-level codes, over the records still passing."""

        s = self.head.s
        codes: set[str] = set()
        binding = request.get("binding") if isinstance(request.get("binding"), Mapping) else {}
        envelope = binding.get("envelope")
        results = [r for r in records if r["kind"] == "TASK_RESULT"]
        if isinstance(envelope, Mapping):
            if envelope.get("obligation_id") not in self._derived:
                codes.add("OBLIGATION_NOT_DERIVED")  # it exists at the base (step 3) but no longer here
            if request.get("claims") and not results and not request.get("candidates"):
                # a mid-task report request claims nothing; an integration request claims with its producing task's
                # admitted result and carries no new judgment (§11.5 (3); review fed5d82 B2)
                codes.add("OBLIGATION_CLAIM_UNSUPPORTED")
        tasks = [_task(r) for r in results]
        admitted = {_task(s.record(rid)) for rid in s.of_kind("TASK_RESULT")}
        if len(tasks) != len(set(tasks)) or any(t in admitted for t in tasks):
            codes.add("OBLIGATION_RESULT_DUPLICATE")
        index = self.w.binding_index()
        if any(c in index and self.w.discharge(index[c]) in _DISCHARGED for c in request.get("claims") or []):
            codes.add("OBLIGATION_DISCHARGED")  # a duplicate discharge is rejected and recorded
        return codes

    def codes(self, record: Mapping[str, Any], trial: Any = None) -> set[str]:
        """The per-record codes, joining the authorization loop's rounds as step 6's do: F31's for a result, and
        the answered and assessments-first checks for a passing judgment."""

        if never_lost(record):
            return set()
        codes = self._frame_codes(record, trial) if passing(dict(record)) and self.locate is not None else set()
        if record["kind"] != "TASK_RESULT":
            return codes
        binding = record.get("binding") if isinstance(record.get("binding"), Mapping) else {}
        bound = self.w.binding_index().get(binding.get("obligation", ""))
        if bound is not None and self.w.discharge(bound) in _DISCHARGED:
            codes.add("OBLIGATION_DISCHARGED")
        item = binding.get("item")
        if isinstance(item, Mapping) and isinstance(item.get("unit"), str):
            view = self.head.s.view
            if item["unit"] not in view.structure.units or view.rev(item["unit"]) != item.get("rev"):
                codes.add("OBLIGATION_CONTRACT_STALE")  # F36: the item revision it was issued for is not current
        return codes

    def _frame_codes(self, record: Mapping[str, Any], trial: Any) -> set[str]:
        """``OBLIGATION_ANSWERED`` and ``OBLIGATION_REVIEW_OPEN`` for a passing judgment, read in its frame."""

        located = self.locate(record, trial)
        if located is None:
            return set()  # its frame does not exist: step 6 refuses it
        support = located[0]
        s = support.s
        codes: set[str] = set()
        w = self._workflows.setdefault(id(support), Workflow(support) if support is not self.head else self.w)
        binding = record.get("binding") if isinstance(record.get("binding"), Mapping) else {}
        bound = w.binding_index().get(binding.get("obligation", ""))
        if bound is not None and record["kind"] != "GATE_DECISION" and not record.get("supersedes") \
                and w.answer(bound) is not None:
            codes.add("OBLIGATION_ANSWERED")  # answered there already (§10.3); a supersession step 3 authorized is not
        target = record["target"] if isinstance(record["target"], Mapping) else {}
        triple = target.get("subject") if record["kind"] == "GATE_DECISION" else target
        if record["kind"] in ("ACCEPTANCE", "GATE_DECISION") and isinstance(triple, Mapping):
            subject, rev = triple.get("subject"), triple.get("rev")
            if isinstance(subject, str) and subject in s.view.structure.units and s.mode(subject) == "NATIVE" \
                    and s.view.structure.kind(subject) in ("D1", "D2"):
                counted = {r for r in s.runs.assessment_records(subject, rev)
                           if s.runs.in_run(r, subject) and support.base(r) != F}
                if not any(e.get("mode") == "standing" and isinstance(e.get("target"), Mapping)
                           and e["target"].get("record") in counted for e in record.get("basis") or []):
                    codes.add("OBLIGATION_REVIEW_OPEN")  # revision assessments first (§10.2; SD-16, SD-19, SD-22)
        return codes


def _task(result: Mapping[str, Any]) -> Any:
    """The task a result ends: its authenticated binding's, else (a human's) its target's (review fed5d82 B1)."""

    binding = result.get("binding") if isinstance(result.get("binding"), Mapping) else {}
    return binding.get("task") or result["target"].get("task")


__all__ = ["Legality"]
