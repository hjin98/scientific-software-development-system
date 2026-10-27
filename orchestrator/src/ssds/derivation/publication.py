"""Publication classification and the entry-shape rule (catalogue §22.1-§22.2; Phase F step 6d, reading F43).

An accepted admission ``n`` names its intent ``B_n -> C_n``; a records-only one has ``C_n = B_n``. The first later
entry carrying ``obs`` reconciles it: ``PENDING`` while there is none; ``PUBLISHED`` when that ``obs`` is ``C_n`` or
an equivalent publication of ``n`` (a commit descending from ``B_n`` with ``C_n``'s tree), or when ``C_n`` is
reachable from it; ``OVERTAKEN`` otherwise. ``late(n)`` holds when an ``OVERTAKEN`` admission's ``C_n`` is newly
reached by a later ``obs``: a ``LATE_PUBLICATION`` integrity finding. An entry whose ``obs`` differs from its
expected head ``E``, other than an absorption carrying no records, violates the entry-shape rule, unless ``obs`` is
an equivalent publication of the admission that set ``E`` ("``E`` becomes ``obs``"): derivation treats it as
corrupt, an ``ENTRY_SHAPE`` integrity finding.

Reachability reads ``History.ancestry``. Without it a publication that is not ``obs`` itself is ``UNKNOWN``, and an
equivalence cannot be shown, so the entry-shape rule reads ``obs`` against ``E`` strictly. Reachability of ``C_n``
stands for reachability of an equivalent publication; a deeper equivalent publication is not searched, so such an
admission reads ``OVERTAKEN``, the conservative class (reading F43).
"""

from __future__ import annotations

from functools import cached_property
from typing import Any

PENDING, PUBLISHED, OVERTAKEN, UNKNOWN = "PENDING", "PUBLISHED", "OVERTAKEN", "UNKNOWN"


class Publication:
    """The publication facts of one history."""

    def __init__(self, history: Any) -> None:
        self.h = history
        self.entries = history.chain.entries[: history.last + 1]

    def _accepted(self, position: int) -> tuple[str, str] | None:
        body = self.entries[position].entry
        admission = body.get("admission") if body["entry_kind"] == "ADMISSION" else None
        if not admission or admission["decision"] != "ACCEPT":
            return None
        return admission["base_commit"], admission["admitted_commit"]

    def _reaches(self, obs: str, base: str, candidate: str) -> bool | None:
        """Whether ``obs`` reaches ``C_n`` or is an equivalent publication of it; ``None`` when unknowable."""

        if obs == candidate or self._equivalent(obs, base, candidate):
            return True
        if self.h.ancestry is None:
            return None
        return self.h.ancestry(candidate, obs)  # None when the graph cannot say: UNKNOWN

    def _equivalent(self, obs: str, base: str, candidate: str) -> bool:
        if self.h.ancestry is None or self.h.ancestry(base, obs) is not True:
            return False
        try:
            return self.h.trees(obs) == self.h.trees(candidate)
        except Exception:  # an unreadable commit is no equivalent publication
            return False

    def _next_obs(self, position: int) -> int | None:
        return next((m for m in range(position + 1, len(self.entries)) if self.entries[m].entry.get("obs") is not None),
                    None)

    @cached_property
    def classes(self) -> dict[int, str]:
        """``pub(n)`` of every accepted admission (§22.2)."""

        out = {}
        for n in range(1, len(self.entries)):
            intent = self._accepted(n)
            if intent is None:
                continue
            m = self._next_obs(n)
            if m is None:
                out[n] = PENDING
                continue
            reached = self._reaches(self.entries[m].entry["obs"], *intent)
            out[n] = UNKNOWN if reached is None else PUBLISHED if reached else OVERTAKEN
        return out

    @cached_property
    def late(self) -> tuple[int, ...]:
        """``late(n)``: an ``OVERTAKEN`` admission whose ``C_n`` a later ``obs`` newly reaches (§22.2)."""

        out = []
        for n, cls in self.classes.items():
            if cls != OVERTAKEN:
                continue
            first = self._next_obs(n)
            for m in range(first + 1, len(self.entries)):
                obs = self.entries[m].entry.get("obs")
                if obs is not None and self._reaches(obs, *self._accepted(n)):
                    out.append(n)
                    break
        return tuple(out)

    @cached_property
    def violations(self) -> tuple[int, ...]:
        """Entries breaking the entry-shape rule (§22.1): ``obs`` is neither the expected head nor, for the
        admission that set it, an equivalent publication, and the entry is not an absorption."""

        out = []
        for m in range(1, len(self.entries)):
            body = self.entries[m].entry
            obs = body.get("obs")
            if obs is None or body["entry_kind"] == "ABSORPTION":
                continue
            expected = self.h.head(m - 1)
            if obs == expected:
                continue
            # "E becomes obs" for the admission that set E: the last entry before m that moved the head
            # (review 0ab46e4 N2), never an older admission whose C a later absorption returned to
            setter = next((n for n in range(m - 1, 0, -1) if self.h.head(n) != self.h.head(n - 1)), None)
            if setter is not None and self._accepted(setter) is not None \
                    and self._equivalent(obs, *self._accepted(setter)):
                continue
            out.append(m)
        return tuple(out)


__all__ = ["OVERTAKEN", "PENDING", "PUBLISHED", "Publication", "UNKNOWN"]
