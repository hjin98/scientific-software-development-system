"""What a designated runner's execution records, decided by derivation (catalogue §6.3, §6.5, §17.1-§17.3; Phase F
step 9f-ii-i, reading F112).

The Dispatcher runs; derivation decides what the run's record says about the state it started from. A pure builder
returns the part of F96's closed execution shape that is a function of that state:

- ``tree`` and ``context`` (the ruleset system, the structure's ignore patterns, the analyzer set);
- the execution closure of the specification and its claims under completeness class ``EXEC``: each reached unit's
  scope terms with their identities in the tree, and the completeness judgments that bounded it; or, where some unit
  had none, the whole-tree fallback, ``widened`` with ``bounded_by`` ``"UNBOUNDED"`` (§4.6, §6.3);
- ``class_attributes`` and ``observes_outside_reads``, by value from the policy in force (§6.3: decided at
  realization).

The configuration is §6.5's: the specification unit, and every execution attribute it fixes; schema 1's declaration
names no regime or parameter instance (F84), so none is recorded. The Dispatcher adds what only the run observes:
the runner, the attributes it observed, ``pins`` (none: outside reads are denied), ``unpinnable``, ``start``, ``end``
and ``incomplete``. An outcome is checked against the declaration (§17.3): every declared output exactly once, each
canonical; anything else is ``MALFORMED_OUTPUT``. The effective time bound is the declared one, capped at 168 hours
for a Dispatcher-run class (F79). An ensemble specification is not run in Phase F.
"""

from __future__ import annotations

from typing import Any

from ssds.content import SYSTEM_TIME_CAP_HOURS, SpecDeclaration, is_canonical, recorded_identity
from ssds.ledger.read import SYSTEM_RULESET

from .state import F

EXEC = "EXEC"


def execution_basis(support: Any, spec: str, claims: list[str], runner_class: str) -> dict[str, Any] | None:
    """The state-decided part of a run's execution basis for ``spec`` on ``claims`` by ``runner_class`` at this
    state's head, or ``None`` when nothing may run: an unusable or ensemble declaration, or an undesignated class."""

    s = support.s
    structure = s.view.structure
    if spec not in structure.units or any(c not in structure.units for c in claims):
        return None
    declared = s.specs.declaration(spec)
    cls = s.policy.runners.get(runner_class)
    if not isinstance(declared, SpecDeclaration) or (declared.granularity or {}).get("mode") == "ENSEMBLE" \
            or cls is None:
        return None
    tree = s.view.tree
    ignore = tuple(structure.ignore)
    bounding: set[str] = set()

    def complete(scope: frozenset[str], c: str) -> bool:
        for rid in s.of_kind("COMPLETENESS"):
            record = s.record(rid)
            target = record["target"]
            if record["outcome"] == "COMPLETE" and frozenset(target["scope"]) == scope and c in target["classes"] \
                    and support.current(rid) > F:
                bounding.add(rid)  # the closure takes the first complete scope: this judgment bounds it
                return True
        return False

    reached, unbounded = s.s0.closure([spec, *claims], frozenset({EXEC}), complete)
    basis: dict[str, Any] = {
        "tree": s.h.head(s.n),
        "context": {"system": SYSTEM_RULESET, "ignore": list(ignore), "analyzers": sorted(s.analyzer_set)},
        "class_attributes": list(cls.attributes), "observes_outside_reads": cls.observes_outside_reads,
    }
    if unbounded:
        whole = {"tracked": "*"}
        basis |= {"units": [], "widened": [[whole, recorded_identity(tree, whole, ())]], "bounded_by": "UNBOUNDED"}
    else:
        units = []
        for uid in sorted(reached):
            terms = [term.to_json() for term in structure.units[uid].scope]
            units.append({"unit": uid, "rev": s.view.rev(uid),
                          "terms": [[t, recorded_identity(tree, t, ignore)] for t in terms]})
        basis |= {"units": units, "bounded_by": sorted(bounding)}
    return basis


def configuration(support: Any, spec: str) -> dict[str, Any] | None:
    """§6.5's configuration: the specification unit and the execution attributes it fixes."""

    declared = support.s.specs.declaration(spec)
    if not isinstance(declared, SpecDeclaration):
        return None
    return {"spec": spec, "fixed": [[k, declared.fixed[k]] for k in sorted(declared.fixed)]}


def outcome_problems(declared: SpecDeclaration, outcome: Any) -> list[str]:
    """Why ``outcome`` is no evaluated outcome of ``declared`` (§17.3): empty when every declared output is present
    once and canonical, and nothing else is."""

    if not isinstance(outcome, dict):
        return ["the outcome is an object"]
    names = {o.name for o in declared.outputs}
    problems = [f"missing output {n}" for n in sorted(names - set(outcome))]
    problems += [f"undeclared output {n}" for n in sorted(set(outcome) - names)]
    problems += [f"{o.name} is not canonical" for o in declared.outputs
                 if o.name in outcome and not is_canonical(o, outcome[o.name])]
    return problems


def effective_bound_hours(declared: SpecDeclaration, runner_kind: str) -> float:
    """The time bound a run is held to: the declared bound, capped at 168 hours for a Dispatcher-run class (F79)."""

    if runner_kind == "DISPATCHER":
        return min(declared.time_bound_hours, SYSTEM_TIME_CAP_HOURS)
    return declared.time_bound_hours


__all__ = ["configuration", "effective_bound_hours", "execution_basis", "outcome_problems"]
