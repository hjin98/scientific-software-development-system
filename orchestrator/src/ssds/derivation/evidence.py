"""Evidence obligations: their identity, which a subject requires, and their lineage (catalogue §10.2, §6.2, §25.3;
Phase F step 9c-i, readings F75, F87).

An evidence obligation is ``(claim unit lineage, specification unit lineage)``. Each name is the root of its unit's
``renamed_from`` lineage, folded over every admitted structure, so a rename keeps the identity. Its token, which an
``EVIDENCE_ASSESSMENT``'s ``target.obligation`` carries, is ``evidence:`` and the SHA-256 hex of the canonical JSON of
``[claim root, spec root]``: bounded, whatever the names' lengths (plan check of 298a12a0, B1). The readable pair is
kept beside it.

A subject requires the obligation of every authored ``EVIDENCES`` relation from a specification unit to a claim unit
inside it, when policy requires evidence for its claim kind, its domain (``evidence = true``, §25.3). A claim of such
a domain that no specification evidences requires nothing, and lint reports it (Q-F23). The lineage that follows
retargets and splits is ``Assessments.about``'s successor rule (``home``); a retired obligation's failures keep
counting in ``qual``, since change never disposes of a failing assessment (§10.2).
"""

from __future__ import annotations

import hashlib
from functools import cached_property
from typing import Any

from ssds.content import jcs

from .plans import LintFinding


def obligation_token(claim_root: str, spec_root: str) -> str:
    """The evidence obligation's token for its lineage roots."""

    return "evidence:" + hashlib.sha256(jcs([claim_root, spec_root])).hexdigest()


class EvidenceFacts:
    def __init__(self, state: Any) -> None:
        self.s = state

    @cached_property
    def _former(self) -> dict[str, frozenset[str]]:
        """Unit -> its former names, folded over every admitted structure (§1.2: an admitted lineage is never
        removed)."""

        edges: dict[str, set[str]] = {}
        for k in range(self.s.n + 1):
            for name, unit in self.s.h.view(k).structure.units.items():
                edges.setdefault(name, set()).update(getattr(unit, "renamed_from", ()) or ())
        return {name: frozenset(formers) for name, formers in edges.items()}

    def root(self, unit: str) -> str:
        """The root of ``unit``'s rename lineage: its formers followed back, the least name first where several."""

        seen = {unit}
        while self._former.get(unit):
            earlier = sorted(self._former[unit] - seen)
            if not earlier:
                break
            unit = earlier[0]
            seen.add(unit)
        return unit

    def token(self, claim: str, spec: str) -> str:
        return obligation_token(self.root(claim), self.root(spec))

    def _relations(self, view: Any) -> list[tuple[str, str]]:
        """(specification unit, claim unit) for every authored ``EVIDENCES`` relation of ``view``."""

        return [(spec, claim) for spec, kind, claim, _ in view.authored_relations() if kind == "EVIDENCES"]

    def _required(self, view: Any, subject: str, policy: Any = None) -> dict[str, tuple[str, str]]:
        structure = view.structure
        policy = self.s.policy if policy is None else policy
        requires = True if policy is False else policy.get(structure.domain(subject), "evidence", False) is True
        if subject not in structure.units or not requires:
            return {}
        inside = set(view.inside(subject))
        return {self.token(claim, spec): (claim, spec) for spec, claim in self._relations(view) if claim in inside}

    def required(self, subject: str) -> tuple[str, ...]:
        """The evidence obligations ``subject`` requires in this state, by token, sorted."""

        return tuple(sorted(self._required(self.s.view, subject)))

    def readable(self, token: str) -> tuple[str, str] | None:
        """The (claim unit, specification unit) a token names in this state, if a relation of it is authored."""

        for spec, claim in self._relations(self.s.view):
            if self.token(claim, spec) == token:
                return claim, spec
        return None

    def required_somewhere(self, token: str, through: int | None = None) -> bool:
        """Some subject required ``token`` at some admitted position up to ``through`` (a latch), each position read
        under the policy in force there, so a policy that later stops requiring evidence retires the obligation and
        never erases a failure it counted (§10.2; review of 09ab5249, B1)."""

        from .state import policy_at

        last = self.s.n if through is None else through
        for k in range(last + 1):
            view = self.s.h.view(k)
            policy = policy_at(self.s.h, k)
            policy = False if policy is None else policy  # unreadable: as requiring evidence, the latch's safe side
            if any(token in self._required(view, u, policy) for u, unit in view.structure.units.items() if unit.subject):
                return True
        return False

    def required_anywhere(self, token: str) -> bool:
        """Some subject of this state requires ``token``."""

        view = self.s.view
        return any(token in self._required(view, u) for u, unit in view.structure.units.items() if unit.subject)

    @cached_property
    def lint(self) -> dict[str, tuple[LintFinding, ...]]:
        """A subject of an evidence-requiring domain that no specification evidences (Q-F23): it requires nothing."""

        view = self.s.view
        claims = {claim for _, claim in self._relations(view)}
        out: dict[str, tuple[LintFinding, ...]] = {}
        for subject, unit in sorted(view.structure.units.items()):
            if unit.subject and self.s.policy.get(view.structure.domain(subject), "evidence", False) is True \
                    and not claims & set(view.inside(subject)):
                out[subject] = (LintFinding("EVIDENCE", subject, "no specification evidences this subject, whose "
                                                                  "domain requires evidence (Q-F23)"),)
        return out


__all__ = ["EvidenceFacts", "obligation_token"]
