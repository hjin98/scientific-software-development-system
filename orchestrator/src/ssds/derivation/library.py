"""The system check library of ``ssds-rules/1`` as data: templates, families, forces, parameters (catalogue §14.3).

Each template has exactly one force. ``HARD`` templates may yield
``VIOLATION``, ``INCOMPLETE`` or ``DISCREPANCY``; ``HEURISTIC`` templates yield
``SIGNAL`` only, and never serve as a contract verifier (§13.2). ``ORACLE``
templates are declarative oracles of evidence specifications (§6.5), not
contract checks. Lint reads this catalogue; conformance (Phase E step 5)
evaluates it.
"""

from __future__ import annotations

from dataclasses import dataclass

HARD = "HARD"
HEURISTIC = "HEURISTIC"
ORACLE = "ORACLE"


@dataclass(frozen=True)
class Template:
    name: str  # FAMILY.template
    force: str
    required: frozenset[str] = frozenset()
    optional: frozenset[str] = frozenset()

    @property
    def family(self) -> str:
        return self.name.split(".", 1)[0]


def _t(name: str, force: str = HARD, required: tuple[str, ...] = (), optional: tuple[str, ...] = ()) -> Template:
    return Template(name, force, frozenset(required), frozenset(optional))


TEMPLATES: dict[str, Template] = {t.name: t for t in (
    _t("BOUNDARY.write_scope"),
    _t("BOUNDARY.protected_surfaces"),
    _t("BOUNDARY.frozen_interface", optional=("symbols",)),
    _t("BOUNDARY.dependency_allowance", optional=("allowance",)),
    _t("BOUNDARY.generated_untouched"),
    _t("BOUNDARY.credential_values", optional=("patterns",)),
    _t("TEST_INTEGRITY.no_deletions", optional=("selectors",)),
    _t("TEST_INTEGRITY.no_skips", optional=("selectors",)),
    _t("TEST_INTEGRITY.no_xfail", optional=("selectors",)),
    _t("TEST_INTEGRITY.evidence_specs_untouched"),
    _t("TEST_INTEGRITY.fewer_assertions", HEURISTIC),
    _t("TEST_INTEGRITY.widened_tolerance", HEURISTIC),
    _t("OBLIGATION.required_artifact", required=("artifact",)),
    _t("OBLIGATION.required_evidence", required=("spec",)),
    _t("OBLIGATION.evidence_basis_fields"),
    _t("OBLIGATION.slots_filled"),
    _t("OBLIGATION.no_new_stubs", optional=("language",)),
    _t("OBLIGATION.mutation_strength", optional=("threshold",)),
    _t("FAITHFULNESS.outcome_consistent"),
    _t("FAITHFULNESS.deviations_declared"),
    _t("FAITHFULNESS.citations_support"),
    _t("FAITHFULNESS.governing_at_basis"),
    _t("FAITHFULNESS.prose_numbers", HEURISTIC),
    _t("FAITHFULNESS.certainty_vocabulary", HEURISTIC),
    _t("DOMAIN.dimensional_consistency"),
    _t("DOMAIN.tolerance_declared"),
    _t("DOMAIN.layer_direction"),
    _t("DOMAIN.unit_inference", HEURISTIC),
    *(_t(f"ORACLE.{name}", ORACLE) for name in ("EXACT", "ABS_TOL", "REL_TOL", "ULP_TOL", "RANGE", "SET_EQUAL", "MONOTONE")),
)}

#: The mutation-strength threshold's proposed default (§14.5).
MUTATION_THRESHOLD = 0.70


def check_problems(template: str, params: dict[str, object]) -> list[str]:
    """Why ``template`` with ``params`` cannot be a contract check: unknown, not ``HARD``, or bad parameters."""

    spec = TEMPLATES.get(template)
    if spec is None:
        return [f"{template} is not a template of ssds-rules/1"]
    if spec.force == HEURISTIC:
        return [f"{template} is HEURISTIC and cannot verify an obligation"]
    if spec.force == ORACLE:
        return [f"{template} is an oracle of evidence specifications, not a contract check"]
    problems = []
    unknown = set(params) - spec.required - spec.optional
    if unknown:
        problems.append(f"{template} has no parameter {sorted(unknown)}")
    missing = spec.required - set(params)
    if missing:
        problems.append(f"{template} needs parameter {sorted(missing)}")
    threshold = params.get("threshold")
    if template == "OBLIGATION.mutation_strength" and threshold is not None and not (
            isinstance(threshold, (int, float)) and not isinstance(threshold, bool) and 0 < threshold <= 1):
        problems.append("mutation_strength threshold is a fraction in (0, 1]")
    return problems
