"""G2 Stage S step S5, catalogue §8-§13: admission salvage, revision runs, tightening, lint, partition.

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

* Admission (Manual §8.3 steps 6-7): never-lost records (reports, challenges, failing assessments,
  adverse judgments, designated-runner observations) are admitted whatever the request's fate when they
  pass their own checks; a non-clean result refuses the request's passing judgments and principal
  decisions while its TASK_RESULT and never-lost records are admitted.
* Revision run (§10.2, SD-22): a NATIVE D1/D2 subject's run is identified by the event that gave its
  current revision; an acceptance or gate decision is current only in its run; any change of the
  revision, a revert included, starts a new run needing a new revision-assessment record.
* Control tightening (§13.4): r ⊑ r' iff the prose is byte-identical and every field moved only in its
  tightening direction, checked against the accepted revision.
* Lint (§13.2): ref locality; the domain rule.
* Partition (§13.7): obligation sets partition the item's (undischarged, for a re-partition), write
  scopes are disjoint subsets of the item's, order acyclic; discharged part obligations of a superseded
  partition stay required.
"""

from __future__ import annotations

NEVER_LOST = {"report", "challenge", "failing_assessment", "adverse_judgment", "observation"}


def admit(records: list, request_ok: bool, result_clean: bool) -> set:
    """records: (name, kind, own_checks_pass). Returns the admitted names."""
    out = set()
    for name, kind, own in records:
        if not own:
            continue
        if kind in NEVER_LOST:
            out.add(name)
        elif not request_ok:
            continue
        elif kind == "task_result":
            out.add(name)
        elif kind in ("passing_judgment", "principal_decision"):
            if result_clean:
                out.add(name)
        else:
            out.add(name)
    return out


def admit_all_or_nothing(records: list, request_ok: bool, result_clean: bool) -> set:
    """A rejected request admits nothing (the f3608f5 Blocker A / 62c0b24 reading)."""
    return {n for n, k, own in records if own and request_ok and (result_clean or k not in ("passing_judgment", "principal_decision"))}


# --- revision run ------------------------------------------------------------------------------------

def run_id(events: list) -> str:
    """events: ordered (event id, revision) that set the subject's current revision; the run is the last."""
    return events[-1][0]


def acceptance_current(acc_run: str, events: list, by_run: bool = True) -> bool:
    if by_run:
        return acc_run == run_id(events)
    # 798b2b4 / 71cf9b3 reading: an earlier acceptance of the same revision bytes is reused
    rev_now = events[-1][1]
    return any(ev == acc_run and rev == rev_now for ev, rev in events)


# --- control tightening -----------------------------------------------------------------------------

TIGHTEN = {"write_scope": "subset", "dependencies": "subset", "evidence_specs": "subset", "homes": "subset", "frozen": "superset", "budget": "not_greater", "slots": "superset",
           "secondary": "superset", "scientific": "on_only"}
FIXED = {"kind", "objective", "governing", "acceptance_criteria", "obligations", "gates", "depends_on"}


def tightens(accepted: dict, current: dict) -> bool:
    if accepted["prose"] != current["prose"]:
        return False
    for f in set(accepted) | set(current):
        if f == "prose":
            continue
        a, c = accepted.get(f), current.get(f)
        if f in FIXED:
            if a != c:
                return False
        elif f in TIGHTEN:
            d = TIGHTEN[f]
            if d == "subset" and not set(c) <= set(a):
                return False
            if d == "superset" and not set(c) >= set(a):
                return False
            if d == "not_greater" and not c <= a:
                return False
            if d == "on_only" and (a and not c):
                return False
        elif a != c:
            return False            # a field outside the whitelist: R2
    return True


def tightens_fields_only(accepted: dict, current: dict) -> bool:
    """6ff4ed1 B2's reading: prose is not compared, so prose can change under R1."""
    a = dict(accepted, prose=None)
    c = dict(current, prose=None)
    return tightens(a, c)


# --- lint -------------------------------------------------------------------------------------------

def ref_ok(ref_target_part: str, item_part: str, objective_part: str = "Objective") -> bool:
    """§13.2 ref locality: a ref resolves only in the item's own part or the plan's Objective."""
    return ref_target_part in (item_part, objective_part)


def domain_ok(item_kind: str, item_authority: str | None, write_set_kinds: set) -> bool:
    """§13.2 domain rule over the effect-keyed write set."""
    authority_kinds = {"D1", "D2", "D3"}
    if item_kind in ("IMPLEMENT", "REPAIR", "MIGRATE", "DOCUMENT"):
        return not (write_set_kinds & authority_kinds)
    if item_kind == "AUTHOR":
        others = (write_set_kinds & authority_kinds) - {item_authority}
        return not others
    return True


def partition_ok(item_obligations: set, item_scope: set, parts: list, order: set, undischarged=None) -> bool:
    """parts: (obligations, write_scope); order: set of (before, after) part indices."""
    target = item_obligations if undischarged is None else undischarged
    obls = [p[0] for p in parts]
    if set().union(*obls) != target or sum(len(o) for o in obls) != len(target):
        return False
    scopes = [p[1] for p in parts]
    if any(not s <= item_scope for s in scopes):
        return False
    if any(scopes[i] & scopes[j] for i in range(len(scopes)) for j in range(i + 1, len(scopes))):
        return False
    from relations import sccs
    nodes = list(range(len(parts)))
    return all(len(c) == 1 for c in sccs(nodes, order)) and not any((a, a) in order for a in nodes)


def required_after_repartition(p1_parts: dict, discharged_at_p2: set, p2_parts: dict) -> set:
    """Discharged parts of a superseded partition stay required; its undischarged parts are replaced."""
    return {k for k in p1_parts if k in discharged_at_p2} | set(p2_parts)
