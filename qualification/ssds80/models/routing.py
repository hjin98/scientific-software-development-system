"""G2 Stage S step S3: routing of an item obligation after integration (registers RR-4 to RR-8).

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

The accepted Manual (§10.4) fixes the identity key, the order of the post-integration routes, and
three principles every route must keep: no stranded obligation (§10.3), a finding is never retired
by a later obligation whose judge did not see it (§10.4), and a material finding survives to its
owner (A8). It leaves five residual cases of the catalogue's route list to G2 (SD-41). This module
models a post-integration state and derives the decision obligations and the item's route under two
readings:

  catalogue  body §10.4 as written: a pending candidate is any admitted, unintegrated, unrefused one;
             a COORDINATE(plan) decision is keyed on its condition; a partitioned item has only its
             part obligations; route 4 reads the latest enactment's adverse review, after route 3.
  settled    the realization proposed for G2:
             (d) the pending candidate is the latest iteration's candidate while it is open (its
                 result complete, not integrated or refused, no adverse answer to its review);
             (b) a COORDINATE(plan) decision for an item route follows one post-answer rule
                 (SD-54, G2 question Q3, repairing 13d67be B1): it is keyed on (condition, item
                 revision, the answer it follows); an answer that changes the item (a new revision)
                 starts a fresh chain; an AMEND that leaves the item unchanged makes the item wait,
                 visibly, until that plan change integrates, after which a condition that still holds
                 derives a new decision naming that answer; a PARTITION hands the route to the parts;
                 a kept-fence DECLINE resumes the item's own route below the fence; ESCALATE answers
                 nothing. Recurrence (catalogue §15.7) is not a separate decision: once a chain holds
                 RECURRENCE answers, each further decision of the same chain, keyed the same way, is
                 held for human attention (its brief carries the convergence duty) and only an
                 authenticated human answer counts; that answer continues the chain exactly as any
                 other (d8ab75c B1). A CHALLENGE answer (allowed on a held decision) waits for its
                 adjudication as an AMEND waits for its integration;
             (c) a partitioned item's own obligation is the composite of its parts and the
                 item-level review, and carries route 4 for an item-level review naming no part;
             (e) a standing out-of-scope adverse review of any integrated enactment is a routed
                 finding (Manual §15) with its own COORDINATE(plan), keyed on that review, beside the
                 item's single route, so no route masks it.

The reading "revision2" is revision 2's rule, which gave recurrence its own key: after a human answer
the same key came back open (d8ab75c B1). The reading "revision1" is the rule G2 workplan revision 1 settled, keyed on (condition, item
revision) only, which the 13d67be Review refuted: an answered key returns no route while the condition
holds and the item is unchanged.

Residual (a), an R2 amendment that keeps the prose and fixed fields, is not a routing mechanism: the
Manual's identity key and its "an R2 amendment derives a new one" disagree there. It is reported as
a question for G1, not settled here.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ItemState:
    item_rev: str = "r1"
    predicate_holds: bool = False
    fence: str = "none"                       # "none", "awaiting", "kept"
    candidates: list = field(default_factory=list)   # (iteration, status): "open", "adverse", "incomplete"
    budget_spent: bool = False
    partitioned: bool = False
    parts_discharged: bool = False
    item_level_adverse_no_part: bool = False
    oos_adverse: list = field(default_factory=list)  # out-of-scope standing adverse reviews: (review id, enactment, latest?)
    answered: set = field(default_factory=set)       # keys of finding decisions already answered
    # answers to the item-route decisions: (condition, item revision) -> ordered (answer id, outcome,
    # settled?[, actor]), outcome AMEND, PARTITION, DECLINE, CHALLENGE or ESCALATE, actor "principal"
    # (default) or "human"; settled means integrated (AMEND) or adjudicated (CHALLENGE); an AMEND here
    # leaves the item unchanged (an AMEND of the item gives it a new revision, so a new chain)
    answers: dict = field(default_factory=dict)


RECURRENCE = 3          # proposed default: answers in one chain before the recurrence decision

def _pending(s: ItemState, reading: str):
    if not s.candidates:
        return None
    if reading == "catalogue":
        return s.candidates[-1] if s.candidates else None   # any admitted unintegrated one stays pending
    it, status = max(s.candidates)
    return (it, status) if status == "open" else None


def admitted_chain(cond: str, raw: list) -> list:
    """The answers that count, in order: ESCALATE answers nothing; a DECLINE counts only for a kept fence;
    a CHALLENGE only on a held decision; on a held decision (the chain already has RECURRENCE answers)
    only a human's answer counts."""
    chain = []
    for a in raw:
        aid, outcome, settled = a[0], a[1], a[2]
        actor = a[3] if len(a) > 3 else "principal"
        held = len(chain) >= RECURRENCE
        if outcome == "ESCALATE" or (outcome == "DECLINE" and cond != "kept-fence"):
            continue
        if outcome == "CHALLENGE" and not held:
            continue
        if held and actor != "human":
            continue
        chain.append((aid, outcome, settled))
    return chain


def route(s: ItemState, reading: str) -> tuple[str, set]:
    """Return (the item obligation's single route, the set of open COORDINATE(plan) decision keys)."""
    decisions: set = set()
    # (e) out-of-scope findings
    for rid, enactment, latest in s.oos_adverse:
        if reading in ("settled", "revision1", "revision2"):
            key = ("finding", rid)
            if key not in s.answered:
                decisions.add(key)
    def coord(cond):
        raw = s.answers.get((cond, s.item_rev), [])
        if reading == "settled":
            chain = admitted_chain(cond, raw)
            prev = chain[-1][0] if chain else None
            if chain:
                aid, outcome, settled = chain[-1]
                if outcome == "DECLINE":
                    return "resume"
                if outcome == "PARTITION":
                    return f"partitioned:{aid}"
                if not settled:
                    return f"awaiting-{'challenge' if outcome == 'CHALLENGE' else 'amendment'}:{aid}"
            decisions.add((cond, s.item_rev, prev))
            held = len(chain) >= RECURRENCE
            return f"human-attention:{cond}" if held else f"COORDINATE:{cond}"
        chain = [a for a in raw if a[1] != "ESCALATE"]
        if reading == "revision2":
            if not chain:
                decisions.add((cond, s.item_rev, None))
                return f"COORDINATE:{cond}"
            aid, outcome, integrated = chain[-1][:3]
            if outcome == "DECLINE" and cond == "kept-fence":
                return "resume"
            if outcome == "PARTITION":
                return f"partitioned:{aid}"
            if not integrated:
                return f"awaiting-amendment:{aid}"
            if len(chain) >= RECURRENCE:
                decisions.add(("recurrence", cond, s.item_rev))
                return f"human-attention:recurrence:{cond}"
            decisions.add((cond, s.item_rev, aid))
            return f"COORDINATE:{cond}"
        if reading == "revision1":
            key = (cond, s.item_rev)
            answered = bool(chain)
        else:                     # keyed on the condition alone: any earlier answer to it counts
            key = (cond,)
            answered = any(k[0] == cond for k in s.answers) or any(k[0] == cond for k in s.answered)
        if not answered:
            decisions.add(key)
            return f"COORDINATE:{cond}"
        return None
    # the item's own route, in the Manual's order
    if s.partitioned and reading == "catalogue":
        # only the parts carry routes; a discharged part has none
        if s.parts_discharged:
            # discharged when the item-level review passes; otherwise no part obligation carries it
            return ("discharged" if not s.item_level_adverse_no_part else "none", decisions)
    if s.fence == "awaiting":
        return ("human-decision:fence", decisions)
    if s.fence == "kept":
        r = coord("kept-fence")
        if r != "resume":
            return (r or "none", decisions)
    holds = s.predicate_holds and not (s.partitioned and s.item_level_adverse_no_part)
    if holds:
        return ("discharged", decisions)
    p = _pending(s, reading)
    if p is not None:
        return (f"pending-candidate:{p[1]}", decisions)
    latest = [x for x in s.oos_adverse if x[2]]
    if latest and reading == "catalogue":
        r = coord("out-of-scope-adverse")
        return (r or "none", decisions)
    if latest and reading in ("settled", "revision1", "revision2"):
        # route 4: the latest enactment's out-of-scope objection is the item's route, carried by the
        # same finding decision derived above (one decision, not two)
        open_ = [rid for rid, _, l in latest if ("finding", rid) not in s.answered]
        if open_:
            return (f"COORDINATE:finding:{open_[0]}", decisions)
        # an answered finding decision lets the item's route continue below
    if s.partitioned and s.item_level_adverse_no_part:
        r = coord("item-level-no-part")
        return (r or "none", decisions)
    if s.budget_spent:
        r = coord("budget-spent")
        return (r or "none", decisions)
    return ("re-dispatch", decisions)


def stranded(s: ItemState, r: str, decisions: set) -> bool:
    """No stranded obligation (Manual §10.3): an undischarged item has a route or an open decision."""
    return r == "none" and not decisions


def findings_survive(s: ItemState, r: str, decisions: set) -> bool:
    """A8 and §10.4: every standing out-of-scope adverse review has an open or answered decision."""
    for rid, enactment, latest in s.oos_adverse:
        keys = {("finding", rid), ("out-of-scope-adverse",), ("out-of-scope-adverse", s.item_rev)}
        if not (keys & (decisions | s.answered)):
            return False
    return True


# --- RR-4: item-obligation identity under an amendment (Manual §10.4 as amended by A2, SD-52) ----

def amendment_class(change: str) -> str:
    """§13.4: tightening is R1; every other change (a loosening, a prose or fixed-field change) is R2."""
    return "R1" if change == "tighten" else "R2"


def keeps_obligation(change: str, reading: str) -> bool:
    """Whether the amended item keeps its obligation (out(o), subjects, iteration count).

    settled (A2): the identity key (item, prose, fixed fields) governs, so only a prose or
    fixed-field change derives a new obligation. catalogue / dddfedf R2 clause: every R2 amendment
    derives a new one."""
    if reading == "settled":
        return change in ("tighten", "loosen")
    return amendment_class(change) == "R1"


def issuable_after(change: str) -> str:
    """§11.2, §11.4: an R1 tightening keeps the plan acceptance; any R2 needs a new one first."""
    return "issuable" if amendment_class(change) == "R1" else "waits for plan acceptance"
