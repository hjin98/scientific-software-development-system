"""G2 Stage S step S2: the judgment layer (registers RR-2, RR-3, RR-11; RR-1 is S1's item model).

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

Three mechanism questions, each with the catalogue's reading and the settled replacement:

* RR-2 transformation judged content. Catalogue: `J = Δ(X) ∪ U_X`, `U_X` every unit any same-key
  enactment changed, in any scope, recorded at issue in the envelope (`retained`), checked at
  Admission step 2, and protected by `STALE_RETAINED` (any same-key integration after issue) plus
  ordinary basis currency. Settled: `W` is computed from the transformation itself — its base
  history, its change and its producing task's scope and key — so it needs no envelope field and
  no step-2 check; at integration Admission recomputes `W` over the merged state and refuses when it
  differs from the reviewed `W` (a new iteration). One producing context per transformation
  identity: a result submitting an already-bound `(B, C, A)` joins that enactment only with the same
  scope and key, and is refused otherwise.
* RR-3 review target typing. Catalogue: a review targets a transformation or a subject triple, so a
  joint-invariant or high-consequence review of change X and X's own review share the target
  `id(X)`. Settled: three typed targets; answering, relief and `REFUSED` read the typed target.
* RR-11 route eligibility per state. Catalogue: an owner exception for every kind, and route
  availability read from the actor alone. Settled: the narrow exception (SD-48); a route record is
  eligible in a state only when its judge is independent of the authors of what that record judges
  (the objection's judged content for supersession and adjudication, the relieved target's for
  relief), the record would act in that state (Manual §5.2), and its own basis is admissible there.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from framework import Actor, Enactment, History, Policy
from rules import FAILING_DISPOSITION, independent_general_exception, independent_narrow_exception


# --- RR-2: transformation judged content and integration support -------------------------------

@dataclass(frozen=True)
class Task:
    task_id: str
    key: str
    scope: frozenset[str]


@dataclass(frozen=True)
class Candidate:
    base: int                       # number of history entries in the base B
    delta: tuple[tuple[str, int], ...]
    task: Task
    author: str

    @staticmethod
    def of(base, delta, task, author):
        return Candidate(base, tuple(sorted(delta.items())), task, author)


def _merged(h: History, c: Candidate) -> History:
    return History(h.enactments + (Enactment(c.task.task_id, c.task.key, c.delta, c.author),))


def w_scoped(h: History, c: Candidate, upto: int | None = None) -> frozenset:
    """Settled W: units in the task scope the work changed (same key, base history and the change),
    with their content in the merged state."""
    hist = History(h.enactments[: c.base if upto is None else upto])
    m = _merged(hist, c)
    units = {u for e in m.enactments if e.key == c.task.key for u in e.units() if u in c.task.scope}
    cur = m.current()
    return frozenset((u, cur[u][0], cur[u][1]) for u in units)


def j_catalogue(h: History, c: Candidate) -> frozenset:
    """Catalogue J: the change plus every same-key unit in any scope, at issue."""
    m = _merged(History(h.enactments[: c.base]), c)
    units = {u for e in m.enactments if e.key == c.task.key for u in e.units()}
    cur = m.current()
    return frozenset((u, cur[u][0], cur[u][1]) for u in units)


def supports_settled(h_now: History, c: Candidate) -> bool:
    """Integration on the existing review only while W at integration equals the reviewed W."""
    return w_scoped(h_now, c, upto=len(h_now.enactments)) == w_scoped(h_now, c)


def supports_catalogue(h_now: History, c: Candidate) -> bool:
    """STALE_RETAINED (any same-key integration after issue) plus currency of J's entries."""
    later = h_now.enactments[c.base:]
    if any(e.key == c.task.key for e in later):
        return False
    j = j_catalogue(h_now, c)
    now = _merged(h_now, c).current()
    return all(now[u][0] == content for u, content, _ in j)


def bind_settled(bound: dict, c: Candidate, ident: tuple) -> bool:
    """A result submitting an already-bound transformation joins it only in the same context."""
    if ident not in bound:
        bound[ident] = (c.task.key, c.task.scope)
        return True
    return bound[ident] == (c.task.key, c.task.scope)


def bind_catalogue(bound: dict, c: Candidate, ident: tuple) -> bool:
    """Catalogue §5.2/§7.1: a later identical transformation joins the first task's enactment."""
    bound.setdefault(ident, (c.task.key, c.task.scope))
    return True


# --- RR-3: typed review targets ------------------------------------------------------------------

@dataclass(frozen=True)
class Review:
    purpose: str          # "transformation", "joint_invariant", "high_consequence", "item_level"
    change: str           # the transformation (or deriving change) it concerns
    outcome: str          # "PASS" or "NO_PASS"
    author: str
    subject: str = ""     # invariant id, surface id or item revision for an integrated result


def target_catalogue(r: Review) -> tuple:
    return ("transformation", r.change)


def target_settled(r: Review) -> tuple:
    if r.purpose == "transformation":
        return ("transformation", r.change)
    return ("integrated_result", r.purpose, r.subject, r.change)


def answers(target_of, obligation_target: tuple, reviews: list[Review]) -> bool:
    """An obligation is answered by the first judgment on its exact target."""
    return any(target_of(r) == obligation_target for r in reviews)


def relieves(target_of, relieved_target: tuple, relief: Review) -> bool:
    """Per-target relief exempts only the reliever's exact target."""
    return relief.outcome == "PASS" and target_of(relief) == relieved_target


# --- RR-11: route eligibility per state ----------------------------------------------------------

@dataclass(frozen=True)
class Objection:
    kind: str                         # kind of the disputed judgment
    adverse_authors: frozenset[str]   # authors of W(j⁻)
    passing_authors: frozenset[str]   # authors of W(z), the reached target
    adverse_actor: Actor
    adverse_frame: str                # "admitted" or an enactment id
    passing_frame: str
    state: str                        # "admitted" or an enactment id: where the veto bites
    integrated: frozenset[str]        # enactments that have integrated
    relief_kind: bool                 # the kind has per-target relief (work judgments, plan acceptance)
    relief_basis_holds: bool          # the relieved record's own basis holds in the state
    policy: Policy
    actors: dict = field(default_factory=dict, compare=False, hash=False)
    about_transformation: bool = True  # the disputed judgments are about transformations (Manual §7.5)


def acts(frame: str, state: str, integrated: frozenset[str]) -> bool:
    """Manual §5.2: a record acts in the admitted frame, in an integrated enactment's frames, or in
    its own enactment's frame."""
    return frame == "admitted" or frame in integrated or frame == state


def routes_actor_only(o: Objection) -> list[str]:
    """The catalogue's reading (and S1's enumeration): availability from the actor alone, every
    route measured against W(j⁻), the general owner exception."""
    ind = independent_general_exception
    a, owner, adj = o.adverse_actor, o.actors[o.policy.owner], o.actors[o.policy.adjudicator]
    r = []
    if a.human and ind(a, o.kind, o.adverse_authors, o.policy):
        r.append("1:reassessment")
        if o.relief_kind:
            r.append("3:relief-by-author")
    if ind(owner, o.kind, o.adverse_authors, o.policy):
        r.append("2:owner-supersession")
        if o.relief_kind:
            r.append("3:relief-by-owner")
    if ind(adj, o.kind, o.adverse_authors, o.policy):
        r.append("4:upheld-challenge")
    return r


def routes_per_state(o: Objection) -> list[str]:
    """Settled: independent of what each record judges, acting in the state, basis admissible."""
    ind = independent_narrow_exception
    a, owner, adj = o.adverse_actor, o.actors[o.policy.owner], o.actors[o.policy.adjudicator]
    # Manual §7.5: a judgment about a transformation declares that transformation's frame, so a
    # supersession of j⁻ (about j⁻'s transformation) declares j⁻'s frame and a relief on z declares
    # z's; any other record may be made in the frame of the state where the veto bites.
    sup_frame = o.adverse_frame if o.about_transformation else o.state
    rel_frame = o.passing_frame if o.about_transformation else o.state
    sup_acts = acts(sup_frame, o.state, o.integrated)
    rel_acts = acts(rel_frame, o.state, o.integrated)
    rel_ok = o.relief_kind and rel_acts and o.relief_basis_holds
    r = []
    if a.human and sup_acts and ind(a, o.kind, o.adverse_authors, o.policy):
        r.append("1:reassessment")
    if a.human and rel_ok and ind(a, o.kind, o.passing_authors, o.policy):
        r.append("3:relief-by-author")
    if sup_acts and ind(owner, o.kind, o.adverse_authors, o.policy):
        r.append("2:owner-supersession")
    if rel_ok and ind(owner, o.kind, o.passing_authors, o.policy):
        r.append("3:relief-by-owner")
    if ind(adj, o.kind, o.adverse_authors, o.policy):         # an adjudication acts in the admitted frame
        r.append("4:upheld-challenge")
    return r


def waiting_literal_f(o: Objection) -> bool:
    """Manual §5.10 (f) "No eligible judge" read as written: every qualified actor (the owner, the
    adjudicator, every qualified human) is among the authors of the judged content."""
    ind = independent_narrow_exception
    names = {o.policy.owner, o.policy.adjudicator} | set(o.policy.qualified_humans)
    return not any(ind(o.actors[n], o.kind, o.adverse_authors, o.policy) for n in names if n in o.actors)


def waiting_per_state(o: Objection) -> bool:
    """(h)(4)'s "no eligible independent judge for any of those routes exists there", read per route
    and per state: no route record would be independent, acting and admissible there."""
    return not routes_per_state(o)


S2_RULESETS = {
    "catalogue": dict(supports=supports_catalogue, j=j_catalogue, bind=bind_catalogue,
                      target_of=target_catalogue, routes=routes_actor_only),
    "manual": dict(supports=supports_settled, j=lambda h, c: w_scoped(h, c), bind=bind_settled,
                   target_of=target_settled, routes=routes_per_state),
}

__all__ = ["Task", "Candidate", "Review", "Objection", "S2_RULESETS", "FAILING_DISPOSITION"]
