"""S5 catalogue §2 and §4.6 cases: cycle legality and closure (expectations from Manual §2.4, §4.6)."""

from __future__ import annotations

from cases_s5_1 import S5Case
from relations import closure, closure_order_independent, legal

N = ["a", "b", "c"]
CASES = [
    S5Case("definitional_cycle_in_one_sdg", "a USES_DEFINITION cycle inside one SDG is legal", True,
           {"settled": lambda: legal(N, [("a", "b", "SIMULTANEOUS", "authored"),
                                          ("b", "a", "SIMULTANEOUS", "authored")], [{"a", "b"}])}),
    S5Case("warrant_cycle_illegal", "a DERIVED_FROM cycle is illegal even inside one SDG", False,
           {"settled": lambda: legal(N, [("a", "b", "ACYCLIC", "authored"),
                                          ("b", "a", "ACYCLIC", "authored")], [{"a", "b"}])}),
    S5Case("mixed_cycle_illegal", "a cycle mixing a definitional and a warrant edge is illegal", False,
           {"settled": lambda: legal(N, [("a", "b", "SIMULTANEOUS", "authored"),
                                          ("b", "a", "ACYCLIC", "authored")], [{"a", "b"}])}),
    S5Case("cycle_across_sibling_sdgs", "a definitional cycle spanning two sibling SDGs is illegal", False,
           {"settled": lambda: legal(N, [("a", "b", "SIMULTANEOUS", "authored"),
                                          ("b", "a", "SIMULTANEOUS", "authored")], [{"a"}, {"b"}])}),
    S5Case("code_recursion_neutral", "mutual imports are derived NEUTRAL: legal and inert", True,
           {"settled": lambda: legal(N, [("a", "b", "NEUTRAL", "derived"), ("b", "a", "NEUTRAL", "derived")], [])}),
    S5Case("challenges_excluded", "a CHALLENGES relation is excluded from cycle legality", True,
           {"settled": lambda: legal(N, [("a", "b", "CHALLENGES", "authored"),
                                          ("b", "a", "ACYCLIC", "authored")], [])}),
]

T = frozenset({"a", "b", "c", "d"})
CH = {"a": [{"a"}, {"a", "b"}, T], "b": [{"b"}, {"a", "b"}, T], "c": [{"c"}, T], "d": [{"d"}, T]}
PRE = {"a": {"b"}, "b": set(), "c": set(), "d": set()}
CASES += [
    S5Case("closure_bounded_by_judgments",
           "with current singleton judgments on a and b, the closure is exactly {a, b}, bounded", (frozenset({"a", "b"}), False),
           {"settled": lambda: closure(["a"], PRE, CH, {frozenset({"a"}), frozenset({"b"})}, T)}),
    S5Case("closure_widens_to_composite",
           "with a judgment only on the composite {a, b}, the closure widens to it", (frozenset({"a", "b"}), False),
           {"settled": lambda: closure(["a"], PRE, CH, {frozenset({"a", "b"})}, T)}),
    S5Case("closure_unbounded_without_judgments",
           "with no judgment the closure is the whole tree, marked UNBOUNDED (missing knowledge never "
           "proves independence)", (T, True),
           {"settled": lambda: closure(["a"], PRE, CH, set(), T)}),
    S5Case("closure_order_independent", "the least fixed point does not depend on visiting order", True,
           {"settled": lambda: closure_order_independent(["a", "c"], PRE, CH, {frozenset({"a"}), frozenset({"b"})}, T)}),
    S5Case("losing_a_judgment_only_widens",
           "removing a completeness judgment never shrinks the closure (conservative direction)", True,
           {"settled": lambda: closure(["a"], PRE, CH, {frozenset({"a"})}, T)[0]
            >= closure(["a"], PRE, CH, {frozenset({"a"}), frozenset({"b"})}, T)[0]}),
]
