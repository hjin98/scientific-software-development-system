"""Cases with expectations written from the accepted Manual's text (G2 Stage S, step S1).

Every expectation below is stated by hand from a named Manual decision and the governing
invariant A5 ("no actor reviews or accepts its own work"), never computed by a rule under test.
`refutes` names the earlier rule sets the case was raised against, with the Review that raised
it; the runner checks that each such rule set fails the case and that the Manual's rules meet it.

Families:
  ITEM   item-level review judged content and its authors (Manual §5.10 (b), §13.7; RR-1)
  OWNER  who may end an objection on content the policy owner authored (§5.10 (e)-(f); RR-11)
  LIFT   whether the liftability invariant holds in the no-eligible-judge state (§5.10 (h)(4))
"""

from __future__ import annotations

from dataclasses import dataclass, field

from framework import Actor, Enactment, History, ItemTarget, ObjectionState, Policy

E = Enactment.of
K = "k"                                  # the item revision's prose and fixed fields
SCOPE = frozenset({"u", "v", "w"})       # the item revision's write scope


@dataclass
class ItemCase:
    name: str
    history: History
    target: ItemTarget
    excluded: set[str]                   # producers a correct item-level review must exclude
    why: str
    refutes: dict[str, str] = field(default_factory=dict)


def _item(name, parts, ints, excluded, why, refutes=None):
    return ItemCase(name, History(tuple(ints)), ItemTarget(K, SCOPE, tuple(parts)), excluded, why,
                    refutes or {})


B1_9431629 = "9431629 B1"
SD46 = "SD-46 history diagnostic"
ITEM_CASES = [
    _item("first_only", ["a", "b"], [E("a", K, {"u": 1}, "A"), E("b", K, {"w": 9}, "D")],
          {"A", "D"}, "each part's output is in the result"),
    _item("empty_redispatch", ["a", "b"],
          [E("a", K, {"u": 1}, "A"), E("b", K, {"w": 9}, "D"), E("a", K, {}, "Q")],
          {"A", "D"}, "u1 is kept by an empty re-dispatch", {"candidate61": B1_9431629 + " (a)"}),
    _item("partial_redispatch", ["a", "b"],
          [E("a", K, {"u": 1}, "A"), E("b", K, {"w": 9}, "D"), E("a", K, {"v": 1}, "C")],
          {"A", "C", "D"}, "u1 is kept beside the new v1", {"candidate61": B1_9431629 + " (b)"}),
    _item("all_empty", ["a", "b"],
          [E("a", K, {"u": 1}, "A"), E("b", K, {"w": 9}, "D"), E("a", K, {}, "Q"), E("b", K, {}, "R")],
          {"A", "D"}, "every part re-dispatched empty", {"candidate61": B1_9431629 + " (c)"}),
    _item("repaired", ["a", "b"],
          [E("a", K, {"u": 1}, "A"), E("b", K, {"w": 9}, "D"), E("a", K, {"u": 2}, "B")],
          {"B", "D"}, "u1 was replaced; its producer judged nothing in the result"),
    _item("kept_part_repartition", ["a", "b1"],
          [E("a", K, {"u": 1}, "A"), E("b1", K, {"w": 9}, "D"), E("a", K, {}, "Q")],
          {"A", "D"}, "a discharged part kept by a re-partition", {"candidate61": B1_9431629 + " (d)"}),
    _item("replaced_part", ["a", "b1"],
          [E("a", K, {"u": 1}, "A"), E("b", K, {"w": 9}, "D"), E("b1", K, {}, "R")],
          {"A", "D"}, "b integrated, was replaced by b1, which kept w9",
          {"candidate61": SD46, "sd46_first": SD46}),
    _item("copy_empty", ["a", "b"],
          [E("src", K, {"u": 1}, "A"), E("a", K, {}, "Q"), E("b", K, {"w": 9}, "D")],
          {"A", "D"}, "a copy under the same prose and fixed fields keeps u1",
          {"candidate61": SD46, "sd46_first": SD46}),
    _item("same_key_other_scope", ["a", "b"],
          [E("tmpl", K, {"x": 3}, "F"), E("a", K, {"u": 1}, "A"), E("b", K, {"w": 9}, "D")],
          {"A", "D"}, "x is outside the item's scope; its producer judged nothing here"),
    _item("foreign_then_drift", ["a", "b"],
          [E("a", K, {"u": 1}, "A"), E("b", K, {"w": 9}, "D"), E("foreign", None, {"u": 3}, "G"),
           E("a", K, {}, "Q")],
          {"G", "D"}, "the drift re-dispatch keeps the foreign u3, which the review judges",
          {"candidate61": "drift sibling of " + B1_9431629}),
    _item("other_item_in_scope", ["a", "b"],
          [E("other", "j", {"v": 7}, "H"), E("a", K, {"u": 1}, "A"), E("b", K, {"w": 9}, "D")],
          {"A", "D"}, "v7 is another item's work, not this item's"),
]


# --- objection states: the f044820 and 8c1f2f2 trajectories, their siblings and controls --------

REVIEW_KINDS = ["transformation_review", "subject_triple_review", "item_level_review",
                "joint_invariant_review", "high_consequence_review", "conformance",
                "plan_acceptance"]
FAILING = "failing_assessment_disposition"

H = Actor("H", human=True)                         # authored the judged content; policy owner
O = Actor("O", human=True)                         # a qualified non-author human
N = Actor("N", human=False, task_ended=True)       # independent agent that objected; task ended
P = Actor("P", human=False)                        # independent agent whose pass is vetoed
U = Actor("U", human=False, attested_fresh=False)  # an agent of unknown lineage
R = Actor("R", human=True)                         # a human reviewer who objected
ACTORS = {a.name: a for a in (H, O, N, P, U, R)}


@dataclass
class ObjectionCase:
    name: str
    state: ObjectionState
    routes: set[str]          # expected admissible route records (prefix "n:")
    waiting: bool             # expected: shown waiting on a missing judge with human attention
    why: str
    refutes: dict[str, str] = field(default_factory=dict)


def _state(kind, owner="H", adjudicator="H", humans=("H",), adverse=N):
    return ObjectionState(kind, frozenset({"H"}), adverse, P,
                          Policy(owner, adjudicator, frozenset(humans)), ACTORS)


F044820 = "f044820 B1"
C8C1F2F2 = "8c1f2f2 B1"
OBJECTION_CASES: list[ObjectionCase] = []
for kind in REVIEW_KINDS:
    OBJECTION_CASES.append(ObjectionCase(
        f"author_owner_{kind}", _state(kind), set(), True,
        "the only policy owner and adjudicator authored the judged content: no route is "
        "independent, so the objection waits on a missing judge (A5; §5.10 (f), (h)(4))",
        {"candidate61": F044820, "candidate62": F044820,
         "candidate63": C8C1F2F2 + " (the stated invariant is false here)"}))
OBJECTION_CASES += [
    ObjectionCase("author_owner_failing_disposition", _state(FAILING),
                  {"2:owner-supersession", "3:relief-by-owner", "4:upheld-challenge"}, False,
                  "the one exception: an owner's disposition of a failing assessment (§5.10 (f))"),
    ObjectionCase("non_author_owner", _state("transformation_review", owner="O", adjudicator="O",
                                             humans=("H", "O")),
                  {"2:owner-supersession", "3:relief-by-owner", "4:upheld-challenge"}, False,
                  "a qualified non-author owner can end the objection"),
    ObjectionCase("policy_names_resolver", _state("transformation_review", owner="O",
                                                  adjudicator="H", humans=("H", "O")),
                  {"2:owner-supersession", "3:relief-by-owner"}, False,
                  "after policy names a non-author owner, owner routes reopen; the author "
                  "adjudicator still cannot uphold a challenge"),
    ObjectionCase("unknown_lineage_owner_agent", _state("transformation_review", owner="U",
                                                        adjudicator="U", humans=()),
                  set(), True, "an unknown-lineage agent never counts as independent",
                  {"candidate61": C8C1F2F2 + " sibling", "candidate62": C8C1F2F2 + " sibling",
                   "candidate63": C8C1F2F2 + " sibling"}),
    ObjectionCase("human_adverse_author", _state("transformation_review",
                                                 adverse=R),
                  {"1:reassessment", "3:relief-by-author"}, False,
                  "a human adverse author outside the authors may reassess or relieve; the author "
                  "owner still may not",
                  {"candidate61": F044820 + " sibling", "candidate62": F044820 + " sibling"}),
]
