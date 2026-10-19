"""S3 cases (RR-5 to RR-8) with expectations written from the accepted Manual (§10.3, §10.4, A8).

Each case states the route the item obligation must take and which decision obligations must be
open, from the Manual's principles: every undischarged item has a route or an open decision (no
stranded obligation); a material finding reaches its owner (A8) and is never retired by a later
obligation whose judge did not see it; a pending candidate keeps its own routes; drift re-dispatches.
Residual (a) (RR-4) is a G1 question (S3_G1_QUESTIONS), not a case.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from routing import ItemState

CAT = "catalogue"
R1 = "revision1"
B1 = "13d67be B1 (SD-54)"


@dataclass
class RoutingCase:
    name: str
    state: ItemState
    route_prefix: str              # the item's route must start with this
    decisions: set                 # decision keys that must be open (settled keying)
    why: str
    refutes: dict = field(default_factory=dict)


S3_CASES = [
    # (d) RR-7: a pending candidate that never ends
    RoutingCase("rejected_candidate_not_pending",
                ItemState(candidates=[(2, "adverse")]), "re-dispatch", set(),
                "the latest iteration's candidate was rejected: it is not pending, so the item's drift "
                "re-dispatches instead of following a dead candidate's routes forever",
                {CAT: "RR-7 (SD-41 d)"}),
    RoutingCase("incomplete_candidate_not_pending",
                ItemState(candidates=[(2, "incomplete")]), "re-dispatch", set(),
                "an INCOMPLETE or PARTIAL result is closed by its own iteration route", {CAT: "RR-7 (SD-41 d)"}),
    RoutingCase("open_candidate_keeps_its_routes",
                ItemState(candidates=[(3, "open")]), "pending-candidate:open", set(),
                "an open candidate of the latest iteration is never discarded by a re-dispatch"),
    # (b) RR-5: an answered decision that changes nothing
    RoutingCase("budget_answered_condition_holds",
                ItemState(item_rev="r2", budget_spent=True,
                          answers={("budget-spent", "r1"): [("d1", "AMEND", True)]}),
                "COORDINATE:budget-spent", {("budget-spent", "r2", None)},
                "the principal answered the spent-budget decision on r1 with an amendment that kept the "
                "budget spent (r2): the condition still holds on r2, so a new decision is owed",
                {CAT: "RR-5 (SD-41 b)"}),
    RoutingCase("budget_open", ItemState(budget_spent=True), "COORDINATE:budget-spent",
                {("budget-spent", "r1", None)}, "a spent budget goes to the principal"),
    # SD-54 (G2 question Q3, 13d67be B1): what follows an answer that leaves the item unchanged
    RoutingCase("budget_amend_elsewhere_waits",
                ItemState(budget_spent=True, answers={("budget-spent", "r1"): [("d1", "AMEND", False)]}),
                "awaiting-amendment:d1", set(),
                "the principal answered with an AMEND of another item: until it integrates the item waits, "
                "visibly, for it; no re-dispatch above budget", {R1: B1}),
    RoutingCase("budget_amend_elsewhere_integrated",
                ItemState(budget_spent=True, answers={("budget-spent", "r1"): [("d1", "AMEND", True)]}),
                "COORDINATE:budget-spent", {("budget-spent", "r1", "d1")},
                "the amendment integrated and the budget is still spent at r1: a new decision naming d1",
                {R1: B1}),
    RoutingCase("budget_partitioned_after_answer",
                ItemState(budget_spent=True, answers={("budget-spent", "r1"): [("d1", "PARTITION", True)]}),
                "partitioned:d1", set(), "a PARTITION answer hands the item's route to its parts", {R1: B1}),
    RoutingCase("budget_escalate_answers_nothing",
                ItemState(budget_spent=True, answers={("budget-spent", "r1"): [("d1", "ESCALATE", True)]}),
                "COORDINATE:budget-spent", {("budget-spent", "r1", None)},
                "ESCALATE does not answer an item route: the first decision stays open"),
    RoutingCase("budget_recurrence",
                ItemState(budget_spent=True, answers={("budget-spent", "r1"): [
                    ("d1", "AMEND", True), ("d2", "AMEND", True), ("d3", "AMEND", True)]}),
                "human-attention:recurrence", {("recurrence", "budget-spent", "r1")},
                "the condition persisted through three answers that left the item unchanged: a recurrence "
                "decision (catalogue §15.7) held for human attention", {R1: B1}),
    RoutingCase("kept_fence_decline_resumes",
                ItemState(fence="kept", answers={("kept-fence", "r1"): [("d1", "DECLINE", True)]}),
                "re-dispatch", set(),
                "a kept-fence DECLINE resumes the item's own route (catalogue §15.5)", {R1: B1}),
    RoutingCase("kept_fence_decline_then_budget",
                ItemState(fence="kept", budget_spent=True,
                          answers={("kept-fence", "r1"): [("d1", "DECLINE", True)]}),
                "COORDINATE:budget-spent", {("budget-spent", "r1", None)},
                "the resumed route meets the spent budget: resuming bypasses neither budget nor fence",
                {R1: B1}),
    RoutingCase("kept_fence_amend_elsewhere_integrated",
                ItemState(fence="kept", answers={("kept-fence", "r1"): [("d1", "AMEND", True)]}),
                "COORDINATE:kept-fence", {("kept-fence", "r1", "d1")},
                "the fence is still kept after an amendment elsewhere: a new decision naming d1", {R1: B1}),
    # (c) RR-6: an item-level review whose findings name no part
    RoutingCase("item_level_no_part",
                ItemState(partitioned=True, parts_discharged=True, predicate_holds=True,
                          item_level_adverse_no_part=True),
                "COORDINATE:item-level-no-part", {("item-level-no-part", "r1", None)},
                "every part is discharged, but the item-level review is adverse and names no part: the "
                "partitioned item's own (composite) obligation carries the decision",
                {CAT: "RR-6 (SD-41 c)"}),
    RoutingCase("item_level_amend_elsewhere_waits",
                ItemState(partitioned=True, parts_discharged=True, predicate_holds=True,
                          item_level_adverse_no_part=True,
                          answers={("item-level-no-part", "r1"): [("d1", "AMEND", False)]}),
                "awaiting-amendment:d1", set(),
                "an AMEND elsewhere leaves the item-level review adverse: wait for the change", {R1: B1}),
    RoutingCase("item_level_amend_elsewhere_integrated",
                ItemState(partitioned=True, parts_discharged=True, predicate_holds=True,
                          item_level_adverse_no_part=True,
                          answers={("item-level-no-part", "r1"): [("d1", "AMEND", True)]}),
                "COORDINATE:item-level-no-part", {("item-level-no-part", "r1", "d1")},
                "the adverse item-level review still stands after the amendment: a new decision", {R1: B1}),
    RoutingCase("partitioned_all_good",
                ItemState(partitioned=True, parts_discharged=True, predicate_holds=True),
                "discharged", set(), "parts and the item-level review pass"),
    # (e) RR-8: out-of-scope findings on earlier or masked enactments
    RoutingCase("oos_on_earlier_enactment",
                ItemState(oos_adverse=[("rv1", "e1", False)]), "re-dispatch", {("finding", "rv1")},
                "an out-of-scope NO-PASS on an earlier integrated enactment still reaches the principal "
                "as a routed finding; the item's own route continues",
                {CAT: "RR-8 (SD-43, SD-41 e)"}),
    RoutingCase("oos_latest_masked_by_pending",
                ItemState(candidates=[(3, "open")], oos_adverse=[("rv2", "e2", True)]),
                "pending-candidate:open", {("finding", "rv2")},
                "a pending candidate keeps its routes and the latest enactment's out-of-scope finding is "
                "still routed (no masking)",
                {CAT: "RR-8 (SD-43, SD-41 e)"}),
    RoutingCase("oos_latest", ItemState(oos_adverse=[("rv3", "e3", True)]), "COORDINATE",
                {("finding", "rv3")}, "route 4: the latest enactment's out-of-scope objection"),
    RoutingCase("oos_latest_answered",
                ItemState(oos_adverse=[("rv3", "e3", True)], answered={("finding", "rv3")}),
                "re-dispatch", set(), "an answered finding decision lets the item's route continue"),
    # controls
    RoutingCase("fence_awaiting", ItemState(fence="awaiting"), "human-decision:fence", set(),
                "a fence awaiting the human comes first"),
    RoutingCase("discharged", ItemState(predicate_holds=True), "discharged", set(), "the predicate holds"),
]


@dataclass
class IdentityCase:
    name: str
    change: str              # "tighten", "loosen", "prose", "fixed_field"
    keeps: bool              # the obligation (out(o), subjects, iteration count) survives
    issuable: str
    why: str
    refutes: dict = field(default_factory=dict)


IDENTITY_CASES = [
    IdentityCase("tightening_keeps", "tighten", True, "issuable",
                 "an R1 tightening keeps the obligation and the plan acceptance"),
    IdentityCase("loosening_keeps_and_waits", "loosen", True, "waits for plan acceptance",
                 "A2: the key governs, so a wider write scope or a larger budget keeps the obligation and "
                 "its iteration count (a budget cannot be reset by loosening); the R2 change needs a new "
                 "plan acceptance before the item is issuable",
                 {CAT: "RR-4 (SD-41 a) / Q2"}),
    IdentityCase("prose_change_new", "prose", False, "waits for plan acceptance",
                 "a prose change starts new work and a new obligation"),
    IdentityCase("fixed_field_change_new", "fixed_field", False, "waits for plan acceptance",
                 "a fixed-field change starts new work and a new obligation"),
]


@dataclass
class RoutingG1Question:
    name: str
    why: str


# Q2, resolved by amendment A2 (SD-52); kept as the record of the question
S3_RESOLVED_QUESTIONS = [
    RoutingG1Question(
        "r2_amendment_keeping_prose_and_fixed_fields",
        "RR-4 (SD-41 a). Manual §10.4 says an item obligation's identity is 'its item and the prose and "
        "fixed fields of its accepted revision' and that 'an R1 tightening keeps it and an R2 amendment "
        "derives a new one'. An amendment that only loosens a tightenable field (a wider write scope, a "
        "larger budget) is R2 (§13.4) yet keeps the prose and fixed fields, so the two statements "
        "disagree there: one keeps the obligation, its out(o) and its budget count; the other derives a "
        "new obligation with an empty out(o) and a fresh budget. No routing mechanism can satisfy both; "
        "the Manual must say which."),
]
