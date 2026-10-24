"""The Dispatcher's operator journal (Manual §8.1, §22.4, §25.2; catalogue §8.1, §25.2).

Private operator state in the SSDS home (``state/<ledger id>/dispatcher-journal.jsonl``, under the SD-59 boundary):
an append-only record of every envelope the Dispatcher issued, and of every request's bytes until its decision is
recorded, so that a provisional entry lost before admission is resubmitted by identity (§8.1, §22.4), and so that
an issue key's retirement can list its outstanding envelopes (§25.2).
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Mapping
from typing import Any

from ssds.admission.request import binding_digest, request_id
from ssds.ledger.qualification import Home

from .home import DispatcherHome


class Journal:
    def __init__(self, home: Home, ledger_id: str) -> None:
        self.home = DispatcherHome(home.root)
        self.home.check(ledger_id)  # Review e6ac009 B7: the Home owner's checked tree
        self.parts = self.home.journal_parts(ledger_id)
        self.path = self.home.path(self.parts)

    def _append(self, item: Mapping[str, Any]) -> None:
        self.home.append_private(self.parts, (json.dumps(dict(item), sort_keys=True, separators=(",", ":")) + "\n")
                                 .encode("utf-8"))

    def entries(self) -> list[dict[str, Any]]:
        data = self.home.read_private(self.parts)
        if data is None:
            return []
        return [json.loads(line) for line in data.decode("utf-8").splitlines() if line.strip()]

    # -- what is recorded ---------------------------------------------------------------------------------------

    def issued(self, task_id: str, binding: Mapping[str, Any]) -> None:
        self._append({"kind": "ISSUED", "task_id": task_id, "envelope": binding_digest(binding),
                      "issue_key_id": binding["envelope"]["issue_key_id"]})

    def submitted(self, request: Mapping[str, Any]) -> str:
        rid = request_id(request)
        self._append({"kind": "REQUEST", "request_id": rid, "request": dict(request)})
        return rid

    def decided(self, rid: str) -> None:
        self._append({"kind": "DECIDED", "request_id": rid})

    # -- what it answers ----------------------------------------------------------------------------------------

    def undecided(self) -> list[dict[str, Any]]:
        """Requests whose decision is not recorded: resubmitted by identity after a lost provisional entry."""

        decided = {e["request_id"] for e in self.entries() if e["kind"] == "DECIDED"}
        return [e["request"] for e in self.entries() if e["kind"] == "REQUEST" and e["request_id"] not in decided]

    def outstanding(self, issue_key_id: str, finished_tasks: Iterable[str]) -> list[str]:
        """The envelopes an issue key signed whose tasks have not finished: what its retirement lists (§25.2)."""

        finished = set(finished_tasks)
        return sorted({e["envelope"] for e in self.entries() if e["kind"] == "ISSUED"
                       and e["issue_key_id"] == issue_key_id and e["task_id"] not in finished})


__all__ = ["Journal"]
