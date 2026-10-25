"""The system role templates (Manual §12.3; catalogue §12.3), as data Admission checks bound records against.

Each agent role lists the record kinds it may submit and, for a kind whose outcomes the role narrows, the outcomes
it may give. Every role may submit reports and challenges, because they are never-lost (§15); content (a
candidate commit) is not a record kind and is the structure and write-scope checks' (§8.3 steps 3-4). The human
role is not a template: an authenticated human records directly, bound by the floors and qualifications of §3.5,
not by a role. Project policy may narrow a template and never widen one (§12.3 "Policy extension limits").
"""

from __future__ import annotations

REPORTS = frozenset({"FINDING", "AMENDMENT_REQUEST", "BLOCKER", "HUMAN_QUESTION"})
CHALLENGES = frozenset({"CHALLENGE"})
EVERY_ROLE = REPORTS | CHALLENGES

#: role -> {record kind: the outcomes the role may give it, or None for any outcome of that kind}
ROLE_TEMPLATES: dict[str, dict[str, frozenset[str] | None]] = {
    "PRINCIPAL": {"TASK_RESULT": frozenset({"COMPLETE", "BLOCKED"}), "COORDINATION_DECISION": None,
                  "MATERIALITY_RECLASSIFICATION": None},
    "IMPLEMENTER": {"TASK_RESULT": frozenset({"COMPLETE", "PARTIAL", "BLOCKED", "INFEASIBLE"})},
    "REVIEWER": {"TASK_RESULT": frozenset({"COMPLETE", "BLOCKED"}),
                 **{kind: None for kind in ("REVIEW", "CONFORMANCE", "ACCEPTANCE", "PLAN_ACCEPTANCE",
                                            "EVIDENCE_ASSESSMENT", "EQUIVALENCE", "COMPLETENESS", "IMMATERIALITY",
                                            "ADJUDICATION", "INTAKE_DISPOSITION")}},
    "INVESTIGATOR": {"TASK_RESULT": frozenset({"FOUND", "NONE_FOUND", "INCONCLUSIVE"}), "INTAKE_CLASSIFICATION": None,
                     "RECONSTRUCTION_PROPOSAL": None},
}
for _template in ROLE_TEMPLATES.values():
    _template.update({kind: None for kind in EVERY_ROLE})


def role_permits(role: str, kind: str, outcome: str | None) -> bool:
    """Whether the template of ``role`` permits a record of ``kind`` with ``outcome`` (§12.3)."""

    template = ROLE_TEMPLATES.get(role)
    if template is None or kind not in template:
        return False
    outcomes = template[kind]
    return outcomes is None or outcome in outcomes


__all__ = ["CHALLENGES", "EVERY_ROLE", "REPORTS", "ROLE_TEMPLATES", "role_permits"]
