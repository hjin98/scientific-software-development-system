"""Per-worktree leases (catalogue §9.1, K2; Phase F step 8c, reading F67).

One mutating execution per worktree: the Dispatcher leases a worktree, keyed by its physical identity (the Level 0
worktree identity the composition root resolves), to one task until the lease expires or is released. Leases are
private operator state (``state/<ledger id>/dispatcher-leases.jsonl``, append-only), an operational fact: they
schedule, and nothing Admission or derivation reads depends on them, so an expired lease changes scheduling, never
correctness. Time is passed in, as the caller's clock.
"""

from __future__ import annotations

import json
from typing import Any

from ssds.ledger.qualification import Home

from .home import DispatcherHome


class Leases:
    def __init__(self, home: Home, ledger_id: str) -> None:
        self.home = DispatcherHome(home.root)
        self.home.check(ledger_id)
        self.parts = self.home.lease_parts(ledger_id)

    def _entries(self) -> list[dict[str, Any]]:
        data = self.home.read_private(self.parts)
        if data is None:
            return []
        return [json.loads(line) for line in data.split(b"\n")[:-1]]  # an unterminated last line was never written

    def _append(self, item: dict[str, Any]) -> None:
        self.home.append_line(self.parts, (json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n")
                              .encode("utf-8"))

    def holder(self, worktree: str, now: float) -> str | None:
        """The task holding ``worktree``'s live lease at ``now``, or None."""

        current: dict[str, Any] | None = None
        for e in self._entries():
            if e["worktree"] != worktree:
                continue
            if e["kind"] == "ACQUIRED":
                current = e
            elif e["kind"] == "RELEASED" and current is not None and current["task_id"] == e["task_id"]:
                current = None
        return current["task_id"] if current is not None and current["expires"] > now else None

    def acquire(self, worktree: str, task_id: str, now: float, ttl: float) -> bool:
        """Lease ``worktree`` to ``task_id`` until ``now + ttl``: refused while another task holds a live lease."""

        held = self.holder(worktree, now)
        if held is not None and held != task_id:
            return False
        self._append({"kind": "ACQUIRED", "worktree": worktree, "task_id": task_id, "expires": now + ttl})
        return True

    def release(self, worktree: str, task_id: str) -> None:
        self._append({"kind": "RELEASED", "worktree": worktree, "task_id": task_id})


__all__ = ["Leases"]
