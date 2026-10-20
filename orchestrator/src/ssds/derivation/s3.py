"""S3, the consequence tier: integrity findings, the Phase D obligations and views (catalogue §5.7-§5.9, §23.6).

S3 reads S0-S2 and nothing below reads it. Phase D derives the kernel the
read-only system needs: integrity findings (an ``INTEGRITY_HALT`` from the
first authenticated corrupt entry, admitted structure failing its static
checks, and each forced support component of §5.6, ordinary or integrity by
the edges it passes through), the ill-formedness and quarantine that S2
already enforced, explained here, one intake obligation per quarantined
delta, one ``REQUALIFY`` obligation per permissive record or relaxer in effect
at a loss boundary's retained head and withheld now, and whether a view may
make a current assertion. Readiness, discharge, routing and briefs are later
phases' S3 queries over the same strata.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Any

from ssds import analyzers
from ssds.content import Structure, static_errors

from .outcomes import adverse
from .state import F, State
from .support import EVALUATED, Node, Support

CRITICAL = "CRITICAL"
ORDINARY = "ORDINARY"


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    attention: str  # CRITICAL for every integrity finding
    about: tuple[str, ...]
    detail: str

    @property
    def integrity(self) -> bool:
        return self.attention == CRITICAL


@dataclass(frozen=True, order=True)
class Obligation:
    kind: str  # INTEGRITY, INTAKE or REQUALIFY
    about: tuple[str, ...]
    detail: str


class Consequences:
    """The S3 kernel of one derived state."""

    def __init__(self, support: Support) -> None:
        self.support = support
        self.s: State = support.s
        self.h = support.s.h

    # -- views (§5.8, §5.9) ---------------------------------------------------------------------

    @cached_property
    def historical(self) -> bool:
        """A view at a position before the chain's last authenticated entry claims no currentness."""

        return self.s.n < len(self.h.chain.entries) - 1

    @cached_property
    def missing_analyzers(self) -> frozenset[str]:
        """Analyzers the ruleset in force pins that this host does not hold (§5.9)."""

        return frozenset(self.s.analyzer_set) - frozenset(analyzers.ANALYZER_SET.values())

    @cached_property
    def assertion_withheld(self) -> tuple[str, ...]:
        """Why this view makes no current assertion; empty when it may."""

        chain = self.h.chain
        reasons = []
        if chain.halt is not None:
            reasons.append(f"INTEGRITY_HALT from position {chain.halt}")
        if chain.unreadable is not None:
            reasons.append(f"unreadable schema version from position {chain.unreadable}")
        if self.missing_analyzers:
            reasons.append("missing analyzers: " + ", ".join(sorted(self.missing_analyzers)))
        if self.historical:
            reasons.append(f"historical view at position {self.s.n}")
        if self.s.frame is not None:
            reasons.append(f"frame of {self.s.frame.x.id}")
        return tuple(reasons)

    @property
    def current_assertion(self) -> bool:
        return not self.assertion_withheld

    # -- integrity and ordinary findings (§5.6, §5.7) --------------------------------------------

    @cached_property
    def findings(self) -> tuple[Finding, ...]:
        out: list[Finding] = []
        chain = self.h.chain
        if chain.halt is not None:  # raised in every view, historical ones included
            out.append(Finding("INTEGRITY_HALT", CRITICAL, (str(chain.halt),), "; ".join(chain.halt_reasons)))
        for error in static_errors(Structure(dict(self.h.sigma(self.s.n)))):
            out.append(Finding("ADMITTED_STRUCTURE", CRITICAL, (error.unit,), f"{error.code}: {error.detail}"))
        for component in self.support.forced:
            members = tuple(f"{kind}:{key}" for kind, key in sorted(component))
            if self._extensible(component):
                out.append(Finding("SUPPORT_CYCLE", ORDINARY, members, "through absorbed content"))
            else:
                out.append(Finding("SUPPORT_CYCLE", CRITICAL, members, "not reachable from absorbed content"))
        for defect in self.s.s0.defects:
            out.append(Finding("ILL_FORMED", ORDINARY, (defect.unit,), f"{defect.code}: {defect.detail}"))
        for key in sorted(self.s.s0.quarantine):
            out.append(Finding("QUARANTINED", ORDINARY, key, "observed declaration differs from effective structure"))
        return tuple(sorted(set(out)))

    def _extensible(self, component: frozenset[Node]) -> bool:
        """A cycle through an ``about`` term or a bounding completeness edge (§5.6 items 2 and 4).

        Those edges are the support graph's ``valid(s)`` edges that §6 adds
        (assessments, dispositions and the completeness judgments bounding
        their observations); they are the only ones absorbed content can extend
        without a new record. Every other cycle arises only from corrupt input.
        """

        support = self.support
        for kind, key in component:
            if kind != "valid":
                continue
            for target in set(support.a.support_nodes(key)):
                if ("current", target) in component:
                    return True
        return False

    # -- obligations (§5.8, §23.6) -----------------------------------------------------------

    @cached_property
    def obligations(self) -> tuple[Obligation, ...]:
        out = [Obligation("INTEGRITY", f.about, f"{f.code}: {f.detail}") for f in self.findings if f.integrity]
        out += [Obligation("INTAKE", key, "quarantined delta") for key in sorted(self.s.s0.quarantine)]
        out += self.requalify
        return tuple(sorted(set(out)))

    @cached_property
    def requalify(self) -> tuple[Obligation, ...]:
        """One per permissive record or relaxer in effect at a boundary's retained head and withheld now.

        Computed by comparing derivation at the retained head ``R`` with
        derivation now. A fresh record of the same kind on the same target,
        admitted after the boundary and current (a relaxer: in force), is the
        requalification that ends the obligation.
        """

        s = self.s
        out: list[Obligation] = []
        for loss in s.of_kind("LEDGER_LOSS"):
            boundary = s.position_of(loss)
            retained = s.record(loss)["fields"]["retained"].get("position", boundary - 1)
            if not 0 <= retained < boundary:
                continue
            then = Support(State(self.h, retained))
            for rid in then.s.records:
                if s.cont(rid):
                    continue
                record = s.record(rid)
                if self._permissive(record):
                    if then.current(rid) == F or self._requalified(rid, boundary, lambda y: self.support.current(y) > F):
                        continue
                elif then.s.relaxer(rid):
                    if not then.s.in_force(rid) or self._requalified(rid, boundary, s.in_force):
                        continue
                else:
                    continue
                out.append(Obligation("REQUALIFY", (rid,), f"{record['kind']} withheld by the boundary at {boundary}"))
        return tuple(out)

    @staticmethod
    def _permissive(record: dict[str, Any]) -> bool:
        """Polarity (§5.4, §23.6): support-tier and observation records other than adverse outcomes."""

        if record["kind"] not in EVALUATED or adverse(record):
            return False
        return not (record["kind"] == "EVIDENCE_ASSESSMENT" and record["outcome"] != "PASS")

    def _requalified(self, rid: str, boundary: int, holds) -> bool:
        s = self.s
        record = s.record(rid)
        return any(s.position_of(y) > boundary and s.record(y)["target"] == record["target"] and holds(y)
                   for y in s.of_kind(record["kind"]) if y != rid)

    # -- the canonical summary the Interface renders (Phase E) and the determinism tests compare -----

    def snapshot(self) -> dict[str, Any]:
        """Every derived value of this view, as plain data in a fixed order."""

        support = self.support
        return {
            "position": self.s.n,
            "head": self.s.h.head(self.s.n),
            "assertion_withheld": list(self.assertion_withheld),
            "current": {rid: support.current(rid) for rid in sorted(self.s.records)
                        if self.s.record(rid)["kind"] in EVALUATED},
            "valid": {u: support.valid(u) for u in sorted(self.s.view.structure.units)
                      if self.s.view.structure.units[u].subject},
            "forced": sorted(sorted(f"{k}:{v}" for k, v in c) for c in support.forced),
            "findings": [[f.code, f.attention, list(f.about), f.detail] for f in self.findings],
            "obligations": [[o.kind, list(o.about), o.detail] for o in self.obligations],
        }


__all__ = ["CRITICAL", "Consequences", "Finding", "ORDINARY", "Obligation"]
