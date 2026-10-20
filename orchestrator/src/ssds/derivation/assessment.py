"""Assessment disagreement: the evidence term, disputes and their dispositions (catalogue §6; Manual §6).

A failing assessment caps validity at ``P`` while it counts and no disposition
stands; it never makes validity ``F``. Its dispositions (§6.7) and their
independence are §5.10's; start, home and staleness are §6.4-§6.6.

Phase D order: this module first carries the evidence term, ``undisputed``,
``qual``, the effective disposition and execution-basis currency, with every
failing assessment counting and none stale; the start latch, ``about`` and the
discriminating-observation stop join it next, and both only narrow what
counts, so the earlier form is the conservative side.
"""

from __future__ import annotations

from collections.abc import Callable
from functools import cached_property
from typing import Any

from ssds.content import recorded_identity

from .state import F, P, State, T


class Assessments:
    def __init__(self, state: State) -> None:
        self.s = state

    # -- records ------------------------------------------------------------------------------

    @cached_property
    def by_obligation(self) -> dict[str, list[str]]:
        out: dict[str, list[str]] = {}
        for rid in self.s.of_kind("EVIDENCE_ASSESSMENT"):
            out.setdefault(self.s.record(rid)["target"]["obligation"], []).append(rid)
        return out

    def realization(self, rid: str) -> dict[str, Any] | None:
        realization = self.s.record(rid)["target"]["realization"]
        return self.s.record(realization) if realization in self.s.records else None

    def claim_subjects(self, rid: str) -> set[str]:
        realization = self.realization(rid)
        if realization is None:
            return set()
        structure = self.s.view.structure
        return {structure.subj(c["unit"]) for c in realization["target"]["claim"]
                if c["unit"] in structure.units and structure.subj(c["unit"])}

    def failing(self, rid: str) -> bool:
        return self.s.record(rid)["outcome"] == "FAIL"

    def passing(self, rid: str) -> bool:
        return self.s.record(rid)["outcome"] == "PASS"

    # -- start, about and stale (§6.4-§6.6) --------------------------------------------------------

    def starts(self, rid: str) -> bool:
        return True

    def about(self, rid: str, subject: str) -> bool:
        return subject in self.claim_subjects(rid)

    def stale(self, rid: str) -> bool:
        return False

    def admissible(self, rid: str, obligation: str) -> bool:
        """Specification admissibility (§17.4) joins in Phase F; here an assessment is admissible for its own obligation."""

        return self.s.record(rid)["target"]["obligation"] == obligation

    def adverse(self, subject: str, obligation: str) -> list[str]:
        return [a for a in self.by_obligation.get(obligation, []) if self.failing(a) and self.admissible(a, obligation)
                and self.starts(a) and self.about(a, subject) and not self.stale(a)]

    # -- disposition (§6.7) ----------------------------------------------------------------------

    def disposition(self, rid: str, value: Callable[[Any], int], base: Callable[[str], int], nonind: Callable[[str], bool]) -> int:
        """``disp(a⁻)``: the best effective disposition."""

        s = self.s
        best = F
        frontier, seen = list(s.supersessions.get(rid, [])), set()
        while frontier:  # supersession, directly or through a chain; the chain's last record must stand
            d = frontier.pop()
            if d in seen:
                continue
            seen.add(d)
            if not s.superseded(d) and not nonind(d):
                best = max(best, base(d))
            frontier.extend(s.supersessions.get(d, []))
        targets = {rid}
        realization = s.record(rid)["target"]["realization"]
        if realization in s.records:
            targets.add(realization)
        for key in targets:
            for c in s.targeting.get(key, []):
                if s.record(c)["kind"] != "CHALLENGE":
                    continue
                for a in s.targeting.get(c, []):
                    record = s.record(a)
                    if record["kind"] == "ADJUDICATION" and record["outcome"] == "UPHELD" and not nonind(a) \
                            and s.in_force(a) and s.cont(a) and not self._contested(a):
                        best = T
        for d in s.of_kind("IMMATERIALITY"):
            if rid in s.record(d)["target"]["records"] and not nonind(d):
                best = max(best, value(("current", d)))
        return best

    def _contested(self, rid: str) -> bool:
        s = self.s
        return any(s.record(c)["kind"] == "CHALLENGE" and s.record(c)["fields"]["blocking"] and s.open(c)
                   for c in s.targeting.get(rid, []))

    def undisputed(self, subject: str, obligation: str, value: Callable[[Any], int], base: Callable[[str], int],
                   nonind: Callable[[str], bool]) -> int:
        result = T
        for a in self.adverse(subject, obligation):
            result = min(result, max(P, self.disposition(a, value, base, nonind)))
        return result

    def ev(self, subject: str, obligation: str, value: Callable[[Any], int], base: Callable[[str], int],
           nonind: Callable[[str], bool]) -> int:
        best = F
        for a in self.by_obligation.get(obligation, []):
            if self.passing(a) and self.admissible(a, obligation) and self.about(a, subject):
                best = max(best, value(("current", a)))
        return min(best, self.undisputed(subject, obligation, value, base, nonind))

    def qual(self, subject: str, value: Callable[[Any], int], base: Callable[[str], int],
             nonind: Callable[[str], bool]) -> int:
        result = T
        for obligation, records in self.by_obligation.items():
            if any(self.failing(a) and self.starts(a) and self.about(a, subject) for a in records):
                result = min(result, self.undisputed(subject, obligation, value, base, nonind))
        return result

    def support_nodes(self, subject: str) -> list[str]:
        """Every assessment and disposition that can enter ``valid(s)``: support-graph edges 2 and 4 (§5.6)."""

        out = [a for records in self.by_obligation.values() for a in records if self.about(a, subject)]
        out += [d for d in self.s.of_kind("IMMATERIALITY")]
        return out

    # -- execution-basis currency (§4.1, §6.3) --------------------------------------------------------

    def execution_current(self, basis: dict[str, Any], content_sat: Callable[[str, str], int],
                          value: Callable[[Any], int]) -> int:
        tree = self.s.view.tree
        ignore = tuple(basis.get("context", {}).get("ignore", ()))
        result = T
        for unit_entry in basis.get("units", []):
            if all(recorded_identity(tree, term, ignore) == cid for term, cid in unit_entry["terms"]):
                continue
            result = min(result, content_sat(unit_entry["unit"], unit_entry["rev"]))
        for term, cid in list(basis.get("reads", [])) + list(basis.get("widened", [])):
            if recorded_identity(tree, term, ignore) != cid:
                return F
        return result
