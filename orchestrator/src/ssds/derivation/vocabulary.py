"""The relation vocabulary of the system ruleset ``ssds-rules/1`` (catalogue §2.2) and the layer order."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RelationType:
    role: str  # DEFINITIONAL | WARRANT | GOVERNING | EVIDENTIAL | PROVENANCE | LINEAGE | STRUCTURAL
    cycle: str  # SIMULTANEOUS | ACYCLIC | NEUTRAL
    classes: frozenset[str]  # authored | proposed | derived
    layer: str  # NON_ASCENDING | NONE | a subject-kind constraint
    completeness: str | None  # DEF | WARRANT | GOVERNING | EXEC | STRUCT


def _t(role: str, cycle: str, classes: str, layer: str, completeness: str | None) -> RelationType:
    return RelationType(role, cycle, frozenset(classes.split()), layer, completeness)


VOCABULARY: dict[str, RelationType] = {
    "USES_DEFINITION": _t("DEFINITIONAL", "SIMULTANEOUS", "authored proposed", "NON_ASCENDING", "DEF"),
    "DERIVED_FROM": _t("WARRANT", "ACYCLIC", "authored proposed", "NON_ASCENDING", "WARRANT"),
    "ASSUMES": _t("WARRANT", "ACYCLIC", "authored proposed", "NON_ASCENDING", "WARRANT"),
    "DEPENDS_ON": _t("WARRANT", "ACYCLIC", "authored proposed", "NON_ASCENDING", "WARRANT"),
    "CONCRETIZES": _t("GOVERNING", "ACYCLIC", "authored proposed", "NON_ASCENDING", "GOVERNING"),
    "CONSTRAINED_BY": _t("GOVERNING", "ACYCLIC", "authored proposed", "NON_ASCENDING", "GOVERNING"),
    "EVIDENCES": _t("EVIDENTIAL", "ACYCLIC", "authored", "SUBJECT:EVIDENCE_SPEC", None),
    "EXECUTION_DEPENDS_ON": _t("EVIDENTIAL", "ACYCLIC", "authored derived", "SUBJECT:EVIDENCE_SPEC|D4", "EXEC"),
    "CHALLENGES": _t("EVIDENTIAL", "ACYCLIC", "authored", "SUBJECT:EVIDENCE_RECORD", None),
    "GENERATED_FROM": _t("PROVENANCE", "ACYCLIC", "authored derived", "SUBJECT:GENERATED", "EXEC"),
    "SUPERSEDES": _t("LINEAGE", "ACYCLIC", "authored", "SAME_KIND", None),
    "REPLACES": _t("LINEAGE", "ACYCLIC", "authored", "SAME_KIND", None),
    "IMPORTS": _t("STRUCTURAL", "NEUTRAL", "derived", "NONE", "STRUCT"),
    "CALLS": _t("STRUCTURAL", "NEUTRAL", "derived", "NONE", "STRUCT"),
    "BUILD_DEPENDS": _t("STRUCTURAL", "NEUTRAL", "derived", "NONE", "STRUCT"),
    "TESTS": _t("STRUCTURAL", "NEUTRAL", "derived", "NONE", "STRUCT"),
}

#: D1 < D2 < D3 < D4 from higher abstraction to lower concretization (catalogue §2.2).
LAYER = {"D1": 1, "D2": 2, "D3": 3, "D4": 4}
LAYER_FREE = frozenset({"EVIDENCE_RECORD", "EXTERNAL", "POLICY", "MANIFEST", "UNCLASSIFIED"})
#: Kinds that take the layer of their domain.
DOMAIN_LAYERED = frozenset({"PLAN", "EVIDENCE_SPEC", "GENERATED"})
CHALLENGES_INQUIRY = frozenset({"EXPLORATORY", "CONFIRMATORY"})
