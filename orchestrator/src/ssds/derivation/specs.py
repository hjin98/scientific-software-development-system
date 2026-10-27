"""Evidence specifications in a state: each declaration, its static errors and its lint (catalogue §17.1, §17.5, §6.9;
Phase F step 9b, readings F79, F84).

A specification unit whose declaration is missing, repeated or outside the grammar is **defective**: no evidence
obligation is derived for it and no assessment under it is admissible (§17.4; plan check of db0bf1ce, note 1). Lint
reports that, and against policy: a runner class policy does not designate (Phase E E20), a Dispatcher class's
declared bound above the system cap of 168 h (F79), and a fixed attribute the class does not record, which would make
every realization inadmissible (plan check of db0bf1ce, note 2). The declaration of a revision the state no longer
holds is read from the history's view at a position holding it.
"""

from __future__ import annotations

from functools import cached_property
from typing import Any

from ssds.content import SYSTEM_TIME_CAP_HOURS, SpecDeclaration, SpecFailure, spec_declaration

from .plans import LintFinding


class SpecFacts:
    def __init__(self, state: Any) -> None:
        self.s = state

    @cached_property
    def units(self) -> tuple[str, ...]:
        structure = self.s.view.structure
        return tuple(sorted(u for u in structure.units
                            if structure.kind(u) == "EVIDENCE_SPEC" and structure.subj(u) == u))

    @cached_property
    def declarations(self) -> dict[str, SpecDeclaration | SpecFailure]:
        return {u: spec_declaration(self.s.view, u) for u in self.units}

    def declaration(self, uid: str) -> SpecDeclaration | SpecFailure | None:
        return self.declarations.get(uid)

    def declaration_at(self, uid: str, rev: str) -> SpecDeclaration | SpecFailure | None:
        """The declaration of ``uid`` at revision ``rev``: the current one, or the latest admitted view holding it."""

        if uid in self.s.view.structure.units and self.s.view.rev(uid) == rev:
            return self.declaration(uid)
        for k in range(self.s.n, -1, -1):
            view = self.s.h.view(k)
            if uid in view.structure.units and view.rev(uid) == rev:
                return spec_declaration(view, uid)
        return None

    def defective(self, uid: str, rev: str | None = None) -> bool:
        found = self.declaration(uid) if rev is None else self.declaration_at(uid, rev)
        return not isinstance(found, SpecDeclaration)

    @cached_property
    def lint(self) -> dict[str, tuple[LintFinding, ...]]:
        policy = self.s.policy
        out: dict[str, tuple[LintFinding, ...]] = {}
        for uid, found in self.declarations.items():
            if isinstance(found, SpecFailure):
                out[uid] = (LintFinding("SPEC", uid, f"{found.code}: {found.detail}"),)
                continue
            findings = []
            runner = policy.runners.get(found.runner)
            if runner is None:
                findings.append(LintFinding("RUNNER", uid, f"runner class {found.runner} is not designated in policy"))
            else:
                if runner.kind == "DISPATCHER" and found.time_bound_hours > SYSTEM_TIME_CAP_HOURS:
                    findings.append(LintFinding("BOUND", uid, f"a Dispatcher class's bound is at most "
                                                              f"{SYSTEM_TIME_CAP_HOURS} h, not {found.time_bound_hours}"))
                for name in sorted(set(found.fixed) - set(runner.attributes)):
                    findings.append(LintFinding("FIXED", uid, f"fixed attribute {name} is not one runner class "
                                                              f"{found.runner} records"))
            if findings:
                out[uid] = tuple(findings)
        return out


__all__ = ["SpecFacts"]
