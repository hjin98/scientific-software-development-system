"""Validation step 7, legality: the checks of Phase F step 5b-i (catalogue §8.3 step 7; Manual §8.3 step 7; plan
§3.2, readings F31, F34, F36).

Admission decides here and derivation supplies every fact, read at the current head:
- the bound obligation exists there: the head derives it (``OBLIGATION_NOT_DERIVED``, F34);
- a request bound to a task claims a discharge only with that task's result: a mid-task report request carries
  none and claims nothing (``OBLIGATION_CLAIM_UNSUPPORTED``);
- one ``TASK_RESULT`` per task, over the head and the request (``OBLIGATION_RESULT_DUPLICATE``);
- a claimed obligation is undischarged at the head: a duplicate discharge is rejected and recorded
  (``OBLIGATION_DISCHARGED``);
- a ``TASK_RESULT`` bound to an obligation already discharged, or naming a contract revision that is not current,
  is refused under that classification (F31: ``OBLIGATION_DISCHARGED``, ``OBLIGATION_CONTRACT_STALE``).
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ssds.derivation import Workflow

from .request import never_lost

#: The discharge states in which a further discharge is a duplicate (§10.4).
_DISCHARGED = frozenset({"DISCHARGED", "DISCHARGED_PROVISIONAL"})


class Legality:
    """Step 7 at one head, its workflow built once for the request."""

    def __init__(self, head: Any) -> None:
        self.head = head
        self.w = Workflow(head)
        self._derived = {o.id for o in self.w.obligations}

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
            if request.get("claims") and not results:
                codes.add("OBLIGATION_CLAIM_UNSUPPORTED")  # a mid-task report request claims nothing
        tasks = [r["target"].get("task") for r in results]
        admitted = {s.record(rid)["target"].get("task") for rid in s.of_kind("TASK_RESULT")}
        if len(tasks) != len(set(tasks)) or any(t in admitted for t in tasks):
            codes.add("OBLIGATION_RESULT_DUPLICATE")
        index = self.w.binding_index()
        if any(c in index and self.w.discharge(index[c]) in _DISCHARGED for c in request.get("claims") or []):
            codes.add("OBLIGATION_DISCHARGED")  # a duplicate discharge is rejected and recorded
        return codes

    def codes(self, record: Mapping[str, Any], trial: Any = None) -> set[str]:
        """F31's per-record codes, joining the authorization loop's rounds as step 6's do."""

        if record["kind"] != "TASK_RESULT" or never_lost(record):
            return set()
        binding = record.get("binding") if isinstance(record.get("binding"), Mapping) else {}
        codes: set[str] = set()
        bound = self.w.binding_index().get(binding.get("obligation", ""))
        if bound is not None and self.w.discharge(bound) in _DISCHARGED:
            codes.add("OBLIGATION_DISCHARGED")
        item = binding.get("item")
        if isinstance(item, Mapping) and isinstance(item.get("unit"), str):
            view = self.head.s.view
            if item["unit"] not in view.structure.units or view.rev(item["unit"]) != item.get("rev"):
                codes.add("OBLIGATION_CONTRACT_STALE")  # F36: the item revision it was issued for is not current
        return codes


__all__ = ["Legality"]
