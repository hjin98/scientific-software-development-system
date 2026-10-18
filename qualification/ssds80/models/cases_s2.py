"""S2 cases (RR-2, RR-3, RR-11) with expectations written from the accepted Manual.

Each expectation is stated by hand from a named Manual decision: §5.10 (b) (judged content and
"a judgment supports an integration only for the content it judged"), §3.4 (three typed review
targets), §5.10 (e)-(f) and (h)(4) (independent, state-local ending routes; waiting on a missing
judge), §5.2 (acting), and A5. `refutes` names the reading each case discriminates against.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from framework import Actor, Enactment, History, Policy
from judgment import Candidate, Objection, Review, Task

E = Enactment.of
T = Task("t1", "k", frozenset({"u", "v"}))
CAT = "catalogue"


# --- RR-2 ------------------------------------------------------------------------------------------

@dataclass
class TxCase:
    name: str
    history_at_issue: History
    history_at_integration: History
    candidate: Candidate
    excluded: set[str]          # producers the transformation's reviewer must be independent of
    supported: bool             # the existing review supports the integration
    why: str
    refutes: dict[str, str] = field(default_factory=dict)


def _tx(name, issue, later, delta, author, excluded, supported, why, refutes=None):
    h0 = History(tuple(issue))
    h1 = History(tuple(issue) + tuple(later))
    return TxCase(name, h0, h1, Candidate.of(len(issue), delta, T, author), excluded, supported, why,
                  refutes or {})


TX_CASES = [
    _tx("first_enactment", [], [], {"u": 1}, "A", {"A"}, True,
        "a first change: its own producer only"),
    _tx("retained_in_scope", [E("a", "k", {"u": 1}, "A")], [], {}, "Q", {"A"}, True,
        "an empty re-dispatch keeps u1, produced by A"),
    _tx("same_key_other_scope_before_issue", [E("a", "k", {"u": 1}, "A"), E("tmpl", "k", {"x": 3}, "F")],
        [], {}, "Q", {"A"}, True,
        "x is outside the task's scope: F judged nothing here (no over-exclusion)",
        {CAT: "RR-2: U_X unrestricted by scope"}),
    _tx("same_key_other_scope_after_issue", [E("a", "k", {"u": 1}, "A")],
        [E("tmpl", "k", {"x": 4}, "F")], {"v": 1}, "C", {"A", "C"}, True,
        "a same-key integration outside the scope leaves W unchanged, so the review still supports "
        "the integration (STALE_RETAINED was stricter than the Manual)",
        {CAT: "RR-2: STALE_RETAINED refuses any same-key integration"}),
    _tx("same_key_in_scope_after_issue", [E("a", "k", {"u": 1}, "A")],
        [E("copy", "k", {"u": 2}, "B")], {"v": 1}, "C", {"A", "C"}, False,
        "same-key work changed u inside the scope after issue: W differs at integration"),
    _tx("foreign_in_scope_after_issue", [E("a", "k", {"u": 1}, "A")],
        [E("foreign", None, {"u": 3}, "G")], {"v": 1}, "C", {"A", "C"}, False,
        "a foreign change to judged content: W differs at integration"),
    _tx("unrelated_after_issue", [E("a", "k", {"u": 1}, "A")],
        [E("foreign", None, {"z": 5}, "G")], {"v": 1}, "C", {"A", "C"}, True,
        "a change outside the scope and the work changes nothing judged"),
]


@dataclass
class BindCase:
    name: str
    first: Candidate
    second: Candidate
    second_admitted: bool
    why: str
    refutes: dict[str, str] = field(default_factory=dict)


BIND_CASES = [
    BindCase("same_context_joins", Candidate.of(1, {"v": 1}, T, "C"),
             Candidate.of(1, {"v": 1}, Task("t2", "k", frozenset({"u", "v"})), "C"), True,
             "an identical transformation in the same scope and key joins the first enactment"),
    BindCase("different_scope_refused", Candidate.of(1, {"v": 1}, T, "C"),
             Candidate.of(1, {"v": 1}, Task("t3", "k", frozenset({"v", "w"})), "C"), False,
             "one transformation identity, two scopes: W would be ambiguous, so the second is refused",
             {CAT: "RR-2 discriminator (f044820): two producing contexts for one (B, C, A)"}),
    BindCase("different_key_refused", Candidate.of(1, {"v": 1}, T, "C"),
             Candidate.of(1, {"v": 1}, Task("t4", "k2", frozenset({"u", "v"})), "C"), False,
             "one transformation identity, two work keys: refused",
             {CAT: "RR-2 discriminator (f044820): two producing contexts for one (B, C, A)"}),
]


# --- RR-3 ------------------------------------------------------------------------------------------

@dataclass
class TargetCase:
    name: str
    reviews: list[Review]
    obligation_target: tuple
    answered: bool
    relief: Review | None
    relieved: bool | None
    why: str
    refutes: dict[str, str] = field(default_factory=dict)


REVIEW_X = ("transformation", "X")
TARGET_CASES = [
    TargetCase("review_answers_review", [Review("transformation", "X", "PASS", "R1")], REVIEW_X, True,
               None, None, "X's own review answers REVIEW(X)"),
    TargetCase("joint_invariant_does_not_answer", [Review("joint_invariant", "X", "PASS", "R2", "inv1")],
               REVIEW_X, False, None, None,
               "a joint-invariant review of change X judges an integrated result, not X",
               {CAT: "RR-3 / 9431629 N2: target collision"}),
    TargetCase("high_consequence_does_not_answer",
               [Review("high_consequence", "X", "PASS", "R3", "surf1")], REVIEW_X, False, None, None,
               "a high-consequence review of change X judges the marked surface's result",
               {CAT: "RR-3 / e810508 N4: target collision"}),
    TargetCase("relief_stays_on_its_target", [], REVIEW_X, False,
               Review("joint_invariant", "X", "PASS", "O", "inv1"), False,
               "relief exempts only its exact target: a pass on the invariant's result does not relieve "
               "a veto on X's own review",
               {CAT: "RR-3: relief across colliding targets"}),
    TargetCase("relief_on_own_target", [], REVIEW_X, False,
               Review("transformation", "X", "PASS", "O"), True, "relief on X's own review target"),
]


# --- RR-11 -----------------------------------------------------------------------------------------

H = Actor("H", human=True)                       # authored the judged content
O = Actor("O", human=True)                       # a qualified human
A = Actor("A", human=False)                      # an agent that produced content
N = Actor("N", human=False, task_ended=True)     # the objecting agent; task ended
ACTORS = {a.name: a for a in (H, O, A, N)}


@dataclass
class RouteCase:
    name: str
    objection: Objection
    routes: set[str]
    why: str
    refutes: dict[str, str] = field(default_factory=dict)


def _obj(kind, adverse_authors, passing_authors, owner, adjudicator, humans, *, adverse_frame="admitted",
         passing_frame="admitted", state="admitted", integrated=(), relief_kind=True, relief_basis=True,
         about_transformation=None):
    if about_transformation is None:
        about_transformation = kind in ("transformation_review", "conformance")
    return Objection(kind, frozenset(adverse_authors), frozenset(passing_authors), N, adverse_frame,
                     passing_frame, state, frozenset(integrated), relief_kind, relief_basis,
                     Policy(owner, adjudicator, frozenset(humans)), ACTORS, about_transformation)


N4 = "dddfedf N4 / RR-11: route eligibility per state"
ROUTE_CASES = [
    RouteCase("acceptance_fail_in_abandoned_frame",
              _obj("acceptance", {"H"}, {"H"}, "O", "H", {"H", "O"}, adverse_frame="X", relief_kind=False),
              {"2:owner-supersession"},
              "an acceptance is not about a transformation: O supersedes the FAIL on the same triple in "
              "the admitted frame, where the veto bites"),
    RouteCase("abandoned_review_frame",
              _obj("transformation_review", {"A"}, {"A"}, "O", "O", {"H", "O"}, adverse_frame="X",
                   passing_frame="Z", state="Z"),
              {"3:relief-by-owner", "4:upheld-challenge"},
              "X was abandoned: a supersession of its NO_PASS declares X's frame and never acts in Z's; O "
              "may still relieve Z's review and adjudicate a challenge",
              {CAT: N4}),
    RouteCase("reached_larger_judged_set",
              _obj("transformation_review", {"A"}, {"A", "O"}, "O", "O", {"O"}),
              {"2:owner-supersession", "4:upheld-challenge"},
              "O is independent of the objection's content but authored part of the reached review's: "
              "O may supersede the objection, not relieve that target",
              {CAT: N4}),
    RouteCase("relief_basis_moved",
              _obj("plan_acceptance", {"H"}, {"H"}, "O", "O", {"H", "O"}, relief_basis=False),
              {"2:owner-supersession", "4:upheld-challenge"},
              "relief is admitted only while the relieved acceptance's basis holds",
              {CAT: N4}),
    RouteCase("pending_frame_where_it_bites",
              _obj("transformation_review", {"H"}, {"H"}, "O", "O", {"H", "O"}, adverse_frame="X",
                   passing_frame="X", state="X"),
              {"2:owner-supersession", "3:relief-by-owner", "4:upheld-challenge"},
              "in X's own frame every route by O acts"),
    RouteCase("author_owner_waits",
              _obj("transformation_review", {"H"}, {"H"}, "H", "H", {"H"}), set(),
              "the only owner and adjudicator authored the content (f044820 B1 state)",
              {CAT: "f044820 B1"}),
    RouteCase("failing_disposition_exception",
              _obj("failing_assessment_disposition", {"H"}, {"H"}, "H", "H", {"H"}, relief_kind=False),
              {"2:owner-supersession", "4:upheld-challenge"},
              "the one owner exception (SD-48)"),
]


# --- a question for G1 found by S2 (workplan §4.3 stop rule) --------------------------------------

@dataclass
class G1Question:
    name: str
    objection: Objection
    why: str


G1_QUESTIONS = [
    G1Question("abandoned_frame_owner_partly_authored_reached",
               _obj("transformation_review", {"A", "H"}, {"A", "H", "O"}, "O", "H", {"H", "O"},
                    adverse_frame="X", passing_frame="Z", state="Z"),
               "X (the NO_PASS's transformation) was abandoned; O is qualified and independent of the "
               "NO_PASS's judged content, but its supersession must declare X's frame and never acts in "
               "Z's; O authored part of Z's judged content, so cannot relieve Z; the adjudicator H "
               "authored the NO_PASS's content. No route record acts there, yet §5.10 (f)'s "
               "'No eligible judge', read as written, does not hold because O is qualified and not an "
               "author. Read literally, (h)(4) is then false; read per route and per state (eligible "
               "'there'), the objection waits and (h)(4) holds."),
]
