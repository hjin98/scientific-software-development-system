"""The Dispatcher's operator journal (Manual §8.1, §22.4, §25.2; catalogue §8.1, §25.2).

Private operator state in the SSDS home (``state/<ledger id>/dispatcher-journal.jsonl``, under the SD-59 boundary):
an append-only record of every envelope the Dispatcher issued, and of every request's bytes until its decision is
recorded, so that a provisional entry lost before admission is resubmitted by identity (§8.1, §22.4), and so that
an issue key's retirement can list its outstanding envelopes (§25.2).
"""

from __future__ import annotations

import json
import os
import stat
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

from ssds.admission.request import binding_digest, request_id


class JournalRefused(RuntimeError):
    """The journal is not private operator state (SD-59)."""


class Journal:
    def __init__(self, home_root: Path, ledger_id: str) -> None:
        self.path = Path(home_root) / "state" / ledger_id / "dispatcher-journal.jsonl"

    def _check(self) -> None:
        for part in (self.path.parent.parent, self.path.parent, self.path):
            if part.is_symlink():
                raise JournalRefused(f"{part} is a symbolic link")
        if self.path.exists() and stat.S_IMODE(self.path.stat().st_mode) & 0o077:
            raise JournalRefused(f"{self.path} is readable by others")

    def _append(self, item: Mapping[str, Any]) -> None:
        self._check()
        self.path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        fd = os.open(self.path, os.O_WRONLY | os.O_CREAT | os.O_APPEND | os.O_NOFOLLOW, 0o600)
        with os.fdopen(fd, "a", encoding="utf-8") as handle:
            handle.write(json.dumps(dict(item), sort_keys=True, separators=(",", ":")) + "\n")
            handle.flush()
            os.fsync(handle.fileno())

    def entries(self) -> list[dict[str, Any]]:
        self._check()
        if not self.path.exists():
            return []
        return [json.loads(line) for line in self.path.read_text(encoding="utf-8").splitlines() if line.strip()]

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


__all__ = ["Journal", "JournalRefused"]
