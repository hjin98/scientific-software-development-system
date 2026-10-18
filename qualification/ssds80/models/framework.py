"""SSDS 8 G2 Stage S design-model framework: histories, provenance and the objection state.

Governing SSDP version: 7.2.1. Design evidence for the G2 shadow workplan (Stage S, step S1;
register RR-10), never production or adequacy evidence (DS-001).

The framework represents a small admitted history explicitly and derives from it, by replay,
the facts the accepted Manual's decisions read:

* the current content of every unit and the actor whose admitted record produced it
  (provenance; Manual §5.10 (b) "authors");
* the judged content of a judgment about work or about an integrated result, under a pluggable
  selection rule (rules.py);
* the independence of a judge, under a pluggable owner-exception rule;
* for a standing objection that vetoes a passing judgment, the set of admissible independent
  records of the four ending routes (Manual §5.10 (e)), and the waiting state when it is empty.

Rules under test live in rules.py; expectations live in cases.py and are written per case from
the Manual's text, not computed by any rule here (the RR-10 requirement). This module holds only
mechanics that every rule set shares: history replay and the route enumeration skeleton.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Enactment:
    """One integrated enactment (or absorbed foreign change) in ledger order.

    owner: the item part, item, copy source or "foreign"; key: the item revision's prose and
    fixed fields (None for a foreign change); delta: unit -> new content; author: the actor whose
    admitted record produced the change.
    """
    owner: str
    key: str | None
    delta: tuple[tuple[str, int], ...]
    author: str

    @staticmethod
    def of(owner: str, key: str | None, delta: dict[str, int], author: str) -> "Enactment":
        return Enactment(owner, key, tuple(sorted(delta.items())), author)

    def units(self) -> set[str]:
        return {u for u, _ in self.delta}


@dataclass(frozen=True)
class History:
    enactments: tuple[Enactment, ...]

    def current(self) -> dict[str, tuple[int, str]]:
        """unit -> (current content, producer of that content), by replay."""
        state: dict[str, tuple[int, str]] = {}
        for e in self.enactments:
            for u, c in e.delta:
                state[u] = (c, e.author)
        return state

    def producers(self, units: set[str]) -> set[str]:
        cur = self.current()
        return {cur[u][1] for u in units if u in cur}


@dataclass(frozen=True)
class ItemTarget:
    """An item-level review's target: the item revision's integrated result (Manual §3.4 type 3)."""
    key: str
    scope: frozenset[str]
    required_parts: tuple[str, ...]


@dataclass(frozen=True)
class Actor:
    name: str
    human: bool
    task_ended: bool = False          # an agent whose task has ended cannot reassess (route 1)
    attested_fresh: bool = True       # agent lineage positively attested fresh and disjoint


@dataclass(frozen=True)
class Policy:
    """Who may act as the owner of the disputed target and who adjudicates its challenges."""
    owner: str
    adjudicator: str
    qualified_humans: frozenset[str]


@dataclass(frozen=True)
class ObjectionState:
    """A standing adverse judgment that vetoes a passing judgment on a reached target.

    kind: the judged record kind (review, conformance, plan acceptance, ..., or
    "failing_assessment_disposition"); authors: the producers of the judged content (from a
    History, or given); adverse_author / passing_author: the two judges.
    """
    kind: str
    authors: frozenset[str]
    adverse_author: Actor
    passing_author: Actor
    policy: Policy
    actors: dict[str, Actor] = field(default_factory=dict, compare=False, hash=False)


@dataclass
class RouteResult:
    admissible: list[str]
    waiting_on: str | None
    human_attention: bool


def ending_routes(state: ObjectionState, independent) -> RouteResult:
    """Enumerate the admissible independent ending records of Manual §5.10 (e).

    `independent(actor, kind, authors, policy)` is the rule under test; `kind` is the kind of what
    the objection disputes, which decides whether an owner exception can apply. Route 1 needs the adverse
    judgment's own author, a human (an agent's task has ended); route 2 the owner's supersession;
    route 3 the author's or the owner's relief on the reached target; route 4 an adjudication
    upholding a challenge, by the policy's adjudicator, independent of the root's authors.
    The waiting state and human attention are what the Manual derives when none is admissible
    (§5.10 (f) No eligible judge, (h)(4)).
    """
    a = state.adverse_author
    owner = state.actors[state.policy.owner]
    adj = state.actors[state.policy.adjudicator]
    routes: list[str] = []
    if a.human and independent(a, state.kind, state.authors, state.policy):
        routes += ["1:reassessment", "3:relief-by-author"]
    if independent(owner, state.kind, state.authors, state.policy):
        routes += ["2:owner-supersession", "3:relief-by-owner"]
    if independent(adj, state.kind, state.authors, state.policy):
        routes.append("4:upheld-challenge")
    if routes:
        return RouteResult(routes, None, False)
    return RouteResult([], "an eligible independent owner or adjudicator", True)
