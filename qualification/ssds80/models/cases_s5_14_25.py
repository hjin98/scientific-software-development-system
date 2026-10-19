"""S5 catalogue §14-§25 cases (Manual §14.4, §15.4, §19.5, §22.2, §23.3-§23.6)."""

from __future__ import annotations

from cases_s5_1 import S5Case
from persistence import (conformance, conformance_first_wins, cutover_admissible, effective_materiality,
                         integrable, loss_status, publication, quorum_sound, qualify)

CASES = [
    S5Case("conformance_is_a_set",
           "an undisclosed breach is both VIOLATION and DISCREPANCY; every class contributes, none takes precedence",
           {"VIOLATION", "DISCREPANCY"},
           {"settled": lambda: conformance([("HARD", "VIOLATION"), ("HARD", "DISCREPANCY"), ("HARD", "OK")]),
            "first_wins": lambda: conformance_first_wins([("HARD", "VIOLATION"), ("HARD", "DISCREPANCY")])},
           {"first_wins": "precedence reading (Manual §14.4)"}),
    S5Case("signal_changes_nothing", "a HEURISTIC signal alone leaves the result integrable and discharges nothing",
           (True, {"SIGNAL"}),
           {"settled": lambda: (integrable(conformance([("HEURISTIC", "SIGNAL")])), conformance([("HEURISTIC", "SIGNAL")]))}),
    S5Case("floors_raise_never_lower",
           "a D1/D2 target's MATERIAL floor raises a ROUTINE report; a lower policy value cannot lower a floor",
           ("MATERIAL", "CRITICAL", "CRITICAL"),
           {"settled": lambda: (effective_materiality("ROUTINE", "MATERIAL", None),
                                effective_materiality("ROUTINE", "CRITICAL", "ROUTINE"),
                                effective_materiality("MATERIAL", "MATERIAL", "CRITICAL"))}),
    S5Case("cutover_record_after_carrier_integrated_refused",
           "a cutover record admitted after its carrier integrated would enact an unchecked cutover: refused "
           "(f03b15e B2, 61cd09b B2)", (True, False, False, False),
           {"settled": lambda: (cutover_admissible(False, "MIGRATE", True, "D4", False),
                                cutover_admissible(True, "MIGRATE", True, "D4", False),
                                cutover_admissible(False, "MIGRATE", True, "D2", False),
                                cutover_admissible(False, "AUTHOR", True, "D2", True))}),
    S5Case("publication_classification",
           "no later observation: PENDING; the effect landed or an equivalent is reachable: PUBLISHED; else OVERTAKEN",
           ("PENDING", "PUBLISHED", "PUBLISHED", "OVERTAKEN"),
           {"settled": lambda: (publication(None, "C", False, False), publication("C", "C", False, False),
                                publication("X", "C", True, False), publication("X", "C", False, False))}),
    S5Case("deployment_classes_sound",
           "LOCAL_TRUST (1,1,1,0), TEAM (3,2,2,0) and HARDENED (4,3,3,1) meet q_a + r > N + f; (3,2,1,0) does not",
           (True, True, True, False),
           {"settled": lambda: (quorum_sound(1, 1, 1, 0), quorum_sound(3, 2, 2, 0), quorum_sound(4, 3, 3, 1),
                                quorum_sound(3, 2, 1, 0))}),
    S5Case("loss_bounds",
           "an abandoned entry is proved never admitted iff h + m + f < q_a; known admitted iff h >= q_a",
           ("proved-never-admitted", "possibly-admitted", "known-admitted"),
           {"settled": lambda: (loss_status(0, 1, 0, 2), loss_status(1, 1, 0, 2), loss_status(2, 0, 1, 2))}),
    S5Case("qualification_states",
           "a stale replica below a witnessed checkpoint is ROLLBACK; too few responses UNQUALIFIED; otherwise the "
           "highest quorum-held head extending every checkpoint", ("ROLLBACK", "UNQUALIFIED", "QUALIFIED@5", "FORK"),
           {"settled": lambda: (qualify(4, [5], {4: 2, 5: 2}, 2, 2, 2, 0), qualify(5, [], {5: 2}, 2, 1, 2, 0),
                                qualify(6, [5], {5: 2, 6: 1}, 2, 2, 2, 5), qualify(6, [5], {5: 2}, 2, 2, 2, 0, True))}),
]
