"""Rule variants under test (G2 Stage S, step S1).

Each rule set names one candidate's reading of a decision, so the framework can show an earlier
rule failing the case that refuted it and the accepted Manual's rule meeting it. Rule sets:

  candidate61   Manual candidate 61 (the mechanism catalogue body): item-level entries are the
                parts' latest integrated changes; the transformation's retained units are every
                same-key unit in any scope; the owner exception covers every judgment; every
                biting veto is claimed liftable.
  sd46_first    SD-46 as first worded: item-level entries are each required part's out(o);
                otherwise candidate 61.
  candidate62   the SD-47 judged-content rule (the item's work inside the item's scope), still
                with the general owner exception and the unconditional liftability claim.
  candidate63   SD-48: the owner exception narrowed to an owner's disposition of a failing
                assessment; still the unconditional liftability claim.
  manual        the accepted Manual (dddfedf, SD-47 to SD-49): scoped work, narrow exception,
                liftable or waiting.

Only what differs between candidates is parameterized; everything else is framework mechanics.
"""

from __future__ import annotations

from framework import History, ItemTarget, ObjectionState, ending_routes

FAILING_DISPOSITION = "failing_assessment_disposition"


# --- item-level judged content (Manual §5.10 (b); register RR-1) -------------------------------

def item_latest_delta(h: History, t: ItemTarget) -> set[str]:
    units: set[str] = set()
    for p in t.required_parts:
        mine = [e for e in h.enactments if e.owner == p]
        if mine:
            units |= mine[-1].units()
    return units


def item_required_out(h: History, t: ItemTarget) -> set[str]:
    return {u for e in h.enactments if e.owner in t.required_parts for u in e.units()}


def item_work_in_scope(h: History, t: ItemTarget) -> set[str]:
    return {u for e in h.enactments if e.key == t.key for u in e.units() if u in t.scope}


def item_same_key_any_scope(h: History, t: ItemTarget) -> set[str]:
    return {u for e in h.enactments if e.key == t.key for u in e.units()}


# --- independence and the owner exception (§5.10 (f); register RR-11) --------------------------

def _plain_independent(actor, authors) -> bool:
    if actor.human:
        return actor.name not in authors
    return actor.attested_fresh and actor.name not in authors


def independent_general_exception(actor, kind, authors, policy) -> bool:
    """Candidates 61-62: a policy owner among the authors counts as independent for any kind
    when policy names no qualified human outside the authors."""
    if _plain_independent(actor, authors):
        return True
    no_outside = not (policy.qualified_humans - authors)
    return actor.human and actor.name in (policy.owner, policy.adjudicator) and no_outside


def independent_narrow_exception(actor, kind, authors, policy) -> bool:
    """SD-48: the exception only for an authenticated owner's disposition of a failing assessment."""
    if _plain_independent(actor, authors):
        return True
    no_outside = not (policy.qualified_humans - authors)
    return (kind == FAILING_DISPOSITION and actor.human
            and actor.name in (policy.owner, policy.adjudicator) and no_outside)


# --- the liftability invariant (§5.10 (h)(4); 8c1f2f2 B1) --------------------------------------

def liftable_always(state: ObjectionState, independent) -> bool:
    """Candidates 61-63: every biting veto has an admissible independent ending record."""
    return bool(ending_routes(state, independent).admissible)


def liftable_or_waiting(state: ObjectionState, independent) -> bool:
    """SD-49: an ending record exists, or the objection is shown waiting on a named missing judge
    with human attention derived."""
    r = ending_routes(state, independent)
    return bool(r.admissible) or (r.waiting_on is not None and r.human_attention)


RULESETS = {
    "candidate61": dict(item=item_latest_delta, independent=independent_general_exception,
                        invariant=liftable_always),
    "sd46_first": dict(item=item_required_out, independent=independent_general_exception,
                       invariant=liftable_always),
    "candidate62": dict(item=item_work_in_scope, independent=independent_general_exception,
                        invariant=liftable_always),
    "candidate63": dict(item=item_work_in_scope, independent=independent_narrow_exception,
                        invariant=liftable_always),
    "manual": dict(item=item_work_in_scope, independent=independent_narrow_exception,
                   invariant=liftable_or_waiting),
}

# the unscoped same-key construction is the catalogue's U_X read for an item; it is compared as a
# construction only (RR-2 seed), never a rule set of a frozen candidate
EXTRA_ITEM_CONSTRUCTIONS = {"same_key_any_scope": item_same_key_any_scope}
