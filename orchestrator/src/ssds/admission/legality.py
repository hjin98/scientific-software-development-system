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

The last two read the record's frame as step 6 locates it (``Currency.locate``). Phase E's deferred refusals
(step 5b-iii; Phase E plan §6):
- a ``COORDINATION_DECISION`` answers decision obligations the head derives: each name in ``target.records``
  is an admitted record or such an obligation, and its bound obligation is derived (``OBLIGATION_NOT_DERIVED``),
  so an answer to a dropped part's decision, or to one never derived, cannot revive work;
- a ``PARTITION`` answer names a lint-valid split for the holder whose decision it answers, read in the trial
  where its parts object exists (``OBLIGATION_PARTITION_INVALID``, reading E32).
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ssds.derivation import F, Workflow, passing

from .request import REPORT_KINDS, never_lost

#: The discharge states in which a further discharge is a duplicate (§10.4).
_DISCHARGED = frozenset({"DISCHARGED", "DISCHARGED_PROVISIONAL"})


class Legality:
    """Step 7 at one head, its workflow built once for the request."""

    def __init__(self, head: Any, locate: Any = None) -> None:
        self.head = head
        self.w = Workflow(head)
        self._derived = {o.id for o in self.w.obligations}
        self.locate = locate  # step 6's frame locator: (support, frame) for a record, or None
        self._workflows: dict[int, Any] = {}  # the frame supports step 6 keeps alive, by identity
        self._trial: tuple[Any, Any] | None = None

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
        if record["kind"] == "COORDINATION_DECISION":
            codes |= self._decision_codes(record, trial)
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

    def _decision_codes(self, record: Mapping[str, Any], trial: Any) -> set[str]:
        target = record["target"] if isinstance(record["target"], Mapping) else {}
        binding = record.get("binding") if isinstance(record.get("binding"), Mapping) else {}
        named = [n for n in target.get("records") or [] if isinstance(n, str)]
        state = trial.s if trial is not None else self.head.s  # a co-submitted report may be named (review 1fc9ced N1)
        reports = {n for n in named if n in state.records and state.record(n)["kind"] in REPORT_KINDS}
        if any(n in state.records for n in named if n not in reports):
            return {"REF_RECORD"}  # a decision's target is "report(s) or item" (catalogue §3.4)
        # an authorized supersession may name what the decision it supersedes named, answered since (review N2)
        earlier = {n for x in record.get("supersedes") or [] if x in self.head.s.records
                   for n in (self.head.s.record(x)["target"] or {}).get("records") or []}
        allowed = self._derived | earlier
        if any(n not in reports and n not in allowed for n in named) \
                or (binding.get("obligation") and binding["obligation"] not in allowed):
            return {"OBLIGATION_NOT_DERIVED"}  # Phase E plan §6: an answer to a decision no longer derived
        if record.get("outcome") != "PARTITION" or trial is None:
            return set()
        if self._trial is None or self._trial[0] is not trial:
            self._trial = (trial, Workflow(trial))  # one slot per round: a rebuilt trial is never served stale
        tried = self._trial[1].items
        for name in named:
            holder = self.w.items.holder_of_decision(name)
            if holder is None:
                continue
            there = tried.holder(holder.obligation.id)
            if there is None or not there.valid_partition(record["id"]):
                return {"OBLIGATION_PARTITION_INVALID"}  # an invalid partition answers nothing (reading E32)
        return set()

    def _workflow(self, support: Any) -> Any:
        if support is self.head:
            return self.w
        if id(support) not in self._workflows:
            self._workflows[id(support)] = Workflow(support)
        return self._workflows[id(support)]

    def _frame_codes(self, record: Mapping[str, Any], trial: Any) -> set[str]:
        """``OBLIGATION_ANSWERED`` and ``OBLIGATION_REVIEW_OPEN`` for a passing judgment, read in its frame."""

        located = self.locate(record, trial)
        if located is None:
            return set()  # its frame does not exist: step 6 refuses it
        support = located[0]
        s = support.s
        codes: set[str] = set()
        # answered "in the frame a passing judgment declares": an ADMITTED record's is the head, even in a request
        # carrying X, where step 6 reads D_n[X] (review 8230421 N1)
        w = self._workflow(self.head if record["frame"] == "ADMITTED" else support)
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


#: The kinds §8.3 step 7 calls principal decision records, refused with passing judgments (``CONFORMANCE_RESULT``).
PRINCIPAL_DECISIONS = frozenset({"COORDINATION_DECISION", "MATERIALITY_RECLASSIFICATION"})


def conformance_alone(records: list[Mapping[str, Any]], trial: Any) -> list[tuple[str, tuple[str, ...]]]:
    """Catalogue §8.3 step 7 (Phase F step 5c, reading F30): when a co-submitted ``TASK_RESULT``'s result-only
    ``HARD`` templates yield ``INCOMPLETE`` or ``DISCREPANCY``, every passing judgment and every principal decision
    record in the request is refused alone (``CONFORMANCE_RESULT``); the result, adverse judgments and the other
    never-lost records stand, so the iteration counts."""

    results = [r["id"] for r in records if r["kind"] == "TASK_RESULT"]
    if trial is None or not results:
        return []
    w = Workflow(trial)
    failing = any(h.cls in ("INCOMPLETE", "DISCREPANCY") for rid in results for h in w.conformance(rid).result_only)
    if not failing:
        return []
    return [(r["id"], ("CONFORMANCE_RESULT",)) for r in records
            if not never_lost(r) and (passing(dict(r)) or r["kind"] in PRINCIPAL_DECISIONS)]


__all__ = ["Legality", "PRINCIPAL_DECISIONS", "conformance_alone"]
