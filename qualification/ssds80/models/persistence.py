"""G2 Stage S step S5, catalogue §14-§25: conformance, floors, cutover carriers, publication,
currentness qualification and known loss.

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

* Conformance (Manual §14.4): set-valued; every failed HARD template contributes; SIGNAL changes no
  disposition; CLEAN discharges nothing.
* Escalation floors (§15.4): policy may raise, never lower; floor items cannot be reclassified.
* Cutover carrier (§19.5): the cutover record is admitted only while its carrier's enactment has not
  integrated, once per enactment, for a carrier item of the right kind naming the subject.
* Publication (§22.2): PENDING, PUBLISHED, OVERTAKEN from the first later observation; late publication.
* Witness quorums (§23.3-§23.4): q_a + r > N + f means every read quorum holds an honest witness of
  every admitted head; the qualified head; FORK and ROLLBACK.
* Known loss (§23.6): proved never admitted iff h + m + f < q_a; known admitted iff h >= q_a.
"""

from __future__ import annotations

import itertools


def conformance(results: list) -> set:
    """results: (template force, outcome) with outcome in VIOLATION/INCOMPLETE/DISCREPANCY/SIGNAL/OK."""
    out = {o for force, o in results if force == "HARD" and o in ("VIOLATION", "INCOMPLETE", "DISCREPANCY")}
    out |= {o for force, o in results if o == "SIGNAL"}
    return out or {"CLEAN"}


def conformance_first_wins(results: list) -> set:
    """A precedence reading: the first failed class hides the others."""
    for force, o in results:
        if force == "HARD" and o in ("VIOLATION", "INCOMPLETE", "DISCREPANCY"):
            return {o}
    return {"CLEAN"}


def integrable(classes: set) -> bool:
    return not classes & {"VIOLATION", "INCOMPLETE", "DISCREPANCY"}


LEVEL = {"ROUTINE": 0, "MATERIAL": 1, "CRITICAL": 2}


def effective_materiality(declared: str, system_floor: str, policy_floor: str | None) -> str:
    floors = [LEVEL[declared], LEVEL[system_floor]] + ([LEVEL[policy_floor]] if policy_floor else [])
    return {v: k for k, v in LEVEL.items()}[max(floors)]


def cutover_admissible(carrier_integrated: bool, carrier_kind: str, names_subject: bool,
                       subject_kind: str, already_recorded: bool) -> bool:
    right_kind = (carrier_kind == "AUTHOR") if subject_kind in ("D1", "D2", "D3") else (carrier_kind == "MIGRATE")
    return (not carrier_integrated) and right_kind and names_subject and not already_recorded


def publication(obs_first_later, c_n, equivalents_reachable: bool, reached_c_n: bool) -> str:
    if obs_first_later is None:
        return "PENDING"
    if obs_first_later == c_n or reached_c_n or equivalents_reachable:
        return "PUBLISHED"
    return "OVERTAKEN"


def quorum_sound(N: int, qa: int, r: int, f: int) -> bool:
    """Every admission quorum and every read quorum share more than f witnesses (brute force)."""
    W = range(N)
    for A in itertools.combinations(W, qa):
        for R in itertools.combinations(W, r):
            if len(set(A) & set(R)) <= f:
                return False
    return True


def loss_status(h: int, m: int, f: int, qa: int) -> str:
    if h + m + f < qa:
        return "proved-never-admitted"
    if h >= qa:
        return "known-admitted"
    return "possibly-admitted"


def qualify(replica_head: int, checkpoints_seen: list, witness_holds: dict, qa: int, r_responses: int, r: int,
            high_water: int, chain_conflict: bool = False) -> str:
    """Heads are positions on one chain unless chain_conflict. witness_holds: position -> holders."""
    if r_responses < r:
        return "UNQUALIFIED"
    if chain_conflict:
        return "FORK"
    if any(cp > replica_head for cp in checkpoints_seen) or high_water > replica_head:
        return "ROLLBACK"
    held = [p for p, n in witness_holds.items() if n >= qa and p <= replica_head
            and all(p >= cp for cp in checkpoints_seen) and p >= high_water]
    return f"QUALIFIED@{max(held)}" if held else "UNQUALIFIED"
