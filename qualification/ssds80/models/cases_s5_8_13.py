"""S5 catalogue §8-§13 cases (Manual §8.3, §10.2, §13.2, §13.4, §13.7; SD-22, R9)."""

from __future__ import annotations

from cases_s5_1 import S5Case
from work import (acceptance_current, admit, admit_all_or_nothing, domain_ok, partition_ok, ref_ok,
                  required_after_repartition, tightens, tightens_fields_only)

REQ = [("tr", "task_result", True), ("pass", "passing_judgment", True), ("rep", "report", True),
       ("fail", "failing_assessment", True), ("adv", "adverse_judgment", True), ("bad", "report", False)]
ACC = {"prose": "P", "write_scope": ["a", "b"], "frozen": ["f"], "budget": 3, "kind": "IMPLEMENT",
       "dependencies": ["x"], "affected": ["src/"]}
CASES = [
    S5Case("rejected_request_salvages_never_lost",
           "a request rejected at any step still admits each never-lost record that passes its own checks "
           "(f3608f5 Blocker A, 62c0b24 N2)", {"rep", "fail", "adv"},
           {"settled": lambda: admit(REQ, request_ok=False, result_clean=True),
            "all_or_nothing": lambda: admit_all_or_nothing(REQ, request_ok=False, result_clean=True)},
           {"all_or_nothing": "f3608f5 Blocker A"}),
    S5Case("unclean_result_refuses_passing_judgments",
           "a non-clean result refuses the request's passing judgments; its TASK_RESULT and never-lost records "
           "are admitted (R9)", {"tr", "rep", "fail", "adv"},
           {"settled": lambda: admit(REQ, request_ok=True, result_clean=False)}),
    S5Case("clean_request_admits_all", "a clean accepted request admits every record passing its checks",
           {"tr", "pass", "rep", "fail", "adv"}, {"settled": lambda: admit(REQ, request_ok=True, result_clean=True)}),
    S5Case("revert_starts_a_new_run",
           "after a revert to earlier bytes, an earlier acceptance of those bytes is not current: the run is the "
           "revert's event (SD-22; 798b2b4 B2, 71cf9b3 B2)", False,
           {"settled": lambda: acceptance_current("e1", [("e1", "r1"), ("e2", "r2"), ("e3", "r1")]),
            "reuse_bytes": lambda: acceptance_current("e1", [("e1", "r1"), ("e2", "r2"), ("e3", "r1")], by_run=False)},
           {"reuse_bytes": "798b2b4 B2 / 71cf9b3 B2"}),
    S5Case("in_run_acceptance_current", "an acceptance made in the current run is current", True,
           {"settled": lambda: acceptance_current("e2", [("e1", "r1"), ("e2", "r2")])}),
    S5Case("prose_change_is_not_tightening",
           "any change of the item's prose is R2, whatever the fields do (6ff4ed1 B2)", False,
           {"settled": lambda: tightens(ACC, dict(ACC, prose="P2")),
            "fields_only": lambda: tightens_fields_only(ACC, dict(ACC, prose="P2"))},
           {"fields_only": "6ff4ed1 B2"}),
    S5Case("narrower_scope_is_tightening", "a narrower write scope with byte-identical prose is R1", True,
           {"settled": lambda: tightens(ACC, dict(ACC, write_scope=["a"]))}),
    S5Case("wider_scope_is_not_tightening", "a wider write scope is R2 (a loosening)", False,
           {"settled": lambda: tightens(ACC, dict(ACC, write_scope=["a", "b", "c"]))}),
    S5Case("larger_budget_is_not_tightening", "a larger budget is R2", False,
           {"settled": lambda: tightens(ACC, dict(ACC, budget=5))}),
    S5Case("field_outside_whitelist_is_r2", "a change of a field outside the whitelist (affected) is R2", False,
           {"settled": lambda: tightens(ACC, dict(ACC, affected=["src/", "lib/"]))}),
    S5Case("narrower_dependency_allowance_is_tightening", "a narrower dependency allowance is R1", True,
           {"settled": lambda: tightens(ACC, dict(ACC, dependencies=[]))}),
    S5Case("ref_outside_item_part_rejected",
           "a ref resolving in another part of the plan, outside the item and the Objective, is a lint error "
           "(b595f2c B2)", (True, True, False),
           {"settled": lambda: (ref_ok("item1", "item1"), ref_ok("Objective", "item1"), ref_ok("item2", "item1"))}),
    S5Case("document_item_cannot_touch_authority",
           "an IMPLEMENT or DOCUMENT item's write set may hold no D1-D3 unit (b595f2c B3, c6da678 B3)",
           (False, False, True, True, False),
           {"settled": lambda: (domain_ok("DOCUMENT", None, {"D4", "D2"}), domain_ok("IMPLEMENT", None, {"D3"}),
                                domain_ok("IMPLEMENT", None, {"D4", "MANIFEST"}), domain_ok("AUTHOR", "D2", {"D2", "MANIFEST"}),
                                domain_ok("AUTHOR", "D2", {"D2", "D1"}))}),
    S5Case("partition_lint", "a partition must split the obligations exactly, with disjoint in-scope write scopes "
           "and an acyclic order", (True, False, False, False),
           {"settled": lambda: (partition_ok({"o1", "o2"}, {"a", "b"}, [({"o1"}, {"a"}), ({"o2"}, {"b"})], {(0, 1)}),
                                partition_ok({"o1", "o2"}, {"a", "b"}, [({"o1"}, {"a"}), ({"o1", "o2"}, {"b"})], set()),
                                partition_ok({"o1", "o2"}, {"a", "b"}, [({"o1"}, {"a", "b"}), ({"o2"}, {"b"})], set()),
                                partition_ok({"o1", "o2"}, {"a", "b"}, [({"o1"}, {"a"}), ({"o2"}, {"b"})], {(0, 1), (1, 0)}))}),
    S5Case("repartition_keeps_discharged_parts",
           "a later partition replaces only undischarged parts; a discharged part of the superseded partition "
           "stays required (63ddf91 N2, 051cce3 N2, 9e5a763 N3)", {"a", "b1", "b2"},
           {"settled": lambda: required_after_repartition({"a": 1, "b": 1}, {"a"}, {"b1": 1, "b2": 1})}),
    S5Case("repartition_lint_over_undischarged",
           "a re-partition is checked against the item's obligations undischarged at its admission", True,
           {"settled": lambda: partition_ok({"o1", "o2"}, {"a", "b"}, [({"o2"}, {"b"})], set(), undischarged={"o2"})}),
]
