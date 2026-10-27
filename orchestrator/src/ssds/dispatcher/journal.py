"""The Dispatcher's operator journal (Manual §8.1, §22.4, §25.2; catalogue §8.1, §25.2).

Private operator state in the SSDS home (``state/<ledger id>/dispatcher-journal.jsonl``, under the SD-59 boundary):
an append-only record of every envelope the Dispatcher issued, and of every request's bytes until its decision is
recorded, so that a provisional entry lost before admission is resubmitted by identity (§8.1, §22.4), and so that
an issue key's retirement can list its outstanding envelopes (§25.2).

Issuing is written ahead (catalogue §9; Phase F step 8a, reading F65): the task's intent (``INTENT``, naming the head
it is issued at), then the envelope's effect (``ISSUED``), then its outcome (``HANDED``, given to its route). An intent
not handed out never reached a route, so a restart abandons it (``ABANDONED``); it is never handed out later.
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Mapping
from typing import Any

from ssds.admission.request import binding_digest, request_id
from ssds.ledger.qualification import Home

from .home import DispatcherHome


class JournalCorrupt(ValueError):
    """A journal line other than an unterminated last one is unreadable: the journal is not trusted."""


class Journal:
    def __init__(self, home: Home, ledger_id: str) -> None:
        self.home = DispatcherHome(home.root)
        self.home.check(ledger_id)  # Review e6ac009 B7: the Home owner's checked tree
        self.parts = self.home.journal_parts(ledger_id)
        self.path = self.home.path(self.parts)

    def _append(self, item: Mapping[str, Any]) -> None:
        self.home.append_line(self.parts, (json.dumps(dict(item), sort_keys=True, separators=(",", ":")) + "\n")
                              .encode("utf-8"))

    def entries(self) -> list[dict[str, Any]]:
        """Every acknowledged entry. An unterminated last line was cut short by a crash and never acknowledged, so
        it is not an entry; any other unreadable line is corruption, refused (re-check a71cca2 N2)."""

        data = self.home.read_private(self.parts)
        if data is None:
            return []
        out = []
        for number, line in enumerate(data.split(b"\n")[:-1], 1):
            try:
                item = json.loads(line)
            except ValueError:
                raise JournalCorrupt(f"{self.path} line {number} is not a journal entry") from None
            if not isinstance(item, dict) or not isinstance(item.get("kind"), str):
                raise JournalCorrupt(f"{self.path} line {number} is not a journal entry")
            out.append(item)
        return out

    # -- what is recorded ---------------------------------------------------------------------------------------

    def intent(self, task_id: str, obligation_id: str, position: int, digest: str) -> None:
        self._append({"kind": "INTENT", "task_id": task_id, "obligation_id": obligation_id, "position": position,
                      "head_digest": digest})

    def handed(self, task_id: str) -> None:
        self._append({"kind": "HANDED", "task_id": task_id})

    def recover(self) -> list[str]:
        """Abandon every intent never handed out: a crash between intent and outcome (reading F65)."""

        entries = self.entries()
        closed = {e["task_id"] for e in entries if e["kind"] in ("HANDED", "ABANDONED")}
        lost = sorted({e["task_id"] for e in entries if e["kind"] == "INTENT"} - closed)
        for task in lost:
            self._append({"kind": "ABANDONED", "task_id": task})
        return lost

    def open_obligations(self) -> frozenset[str]:
        """Obligations with a task handed out: none is issued a second task (review 546cc86 N2). ``recover`` never
        abandons a handed task. A task's finishing is recorded by later parts of step 8; until then it stays open."""

        entries = self.entries()
        handed = {e["task_id"] for e in entries if e["kind"] == "HANDED"}
        return frozenset(e["obligation_id"] for e in entries if e["kind"] == "INTENT" and e["task_id"] in handed)

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

        entries = self.entries()
        signed = {e["task_id"] for e in entries if e["kind"] == "ISSUED"}
        # an abandoned intent whose envelope was never signed is outstanding nowhere; one signed but not recorded as
        # handed may have reached its route, so it stays listed: over-listing only admits never-lost records, the
        # fail-safe direction (review 546cc86 N3)
        finished = set(finished_tasks) | {e["task_id"] for e in entries if e["kind"] == "ABANDONED"
                                          and e["task_id"] not in signed}
        return sorted({e["envelope"] for e in self.entries() if e["kind"] == "ISSUED"
                       and e["issue_key_id"] == issue_key_id and e["task_id"] not in finished})


__all__ = ["Journal", "JournalCorrupt"]
