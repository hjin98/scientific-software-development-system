"""Outcome vocabularies and consumption-class coverage, shared by the support and judgment owners."""

from __future__ import annotations

#: The passing outcome of each judgment kind that can support (catalogue §3.4).
PASSING = {"ACCEPTANCE": "PASS", "LEGACY_ACCEPTANCE": "IMPORTED", "EXTERNAL_ACCEPTANCE": "IMPORTED", "REVIEW": "PASS",
           "CONFORMANCE": "CONFORMANT", "EQUIVALENCE": "EQUIVALENT", "COMPLETENESS": "COMPLETE",
           "EVIDENCE_ASSESSMENT": "PASS", "PLAN_ACCEPTANCE": "ACCEPTED", "GATE_DECISION": "ACCEPT",
           "PRODUCT_SCOPE_ACCEPTANCE": "ACCEPTED", "INTAKE_DISPOSITION": "ABSORB", "IMMATERIALITY": "IMMATERIAL"}
#: Adverse outcomes (Manual §5.10 (a)); every INTAKE_DISPOSITION other than ABSORB is adverse too.
ADVERSE = {"ACCEPTANCE": "FAIL", "REVIEW": "NO_PASS", "CONFORMANCE": "NONCONFORMANT", "PLAN_ACCEPTANCE": "REJECTED",
           "EQUIVALENCE": "NOT_EQUIVALENT", "COMPLETENESS": "INCOMPLETE", "GATE_DECISION": "REJECT",
           "PRODUCT_SCOPE_ACCEPTANCE": "REJECTED"}


def passing(record: dict) -> bool:
    return PASSING.get(record["kind"]) == record["outcome"]


def adverse(record: dict) -> bool:
    if record["kind"] == "INTAKE_DISPOSITION":
        return record["outcome"] != "ABSORB"
    return ADVERSE.get(record["kind"]) == record["outcome"]


def covers(judgment_class: str, entry_class: str) -> bool:
    """An ``EQUIVALENCE`` of class ``c`` covers a content entry of class ``k`` (catalogue §4.4)."""

    if entry_class in ("EXACT", "PLAN_CONTROL"):
        return False
    if entry_class == "MIGRATION":
        return judgment_class == "MIGRATION"
    return judgment_class == entry_class or judgment_class in ("EDITORIAL", "REPRESENTATION")
