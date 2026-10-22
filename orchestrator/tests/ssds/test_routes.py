"""Phase E step 5a: the one route of an item obligation at the real derivation owner (catalogue §10.4, §15.5).

The S3 routing histories (qualification/ssds80/models/cases_s3.py; G2 workplan §5.4) are replayed as
constructed ledgers through the real derivation, never through ``models/routing.py``: each expected route and
open decision is the case's literal outcome. Fence cases are Phase F's (§22.3) and are not replayed here.
Also carried: the four identity cases (RR-4) as the assembled transition, and b365947 N4.
"""

from __future__ import annotations

import hashlib
import unittest

from ssds.derivation.workflow import READY, WAITING, Workflow
from ssds.ledger.read import with_id

from ._fixtures import admission_body, record, tree
from ._scenario import HUMAN, OWNER, Scenario, agent, content, fresh, judgment
from .test_lint import FILES, MANIFEST, item_block, plan_text

PRINCIPAL = agent("principal")
SLOTS = {"claims": [{"claim": "documented", "records": []}], "unverified_assumptions": {"none": "NONE_MADE"},
         "deviations": {"none": "NO_DEVIATION"}}


def document_item(budget: int = 3, write_scope: str = '["records.md"]', prose: str = "Document the solver.\n") -> str:
    block = item_block(kind="DOCUMENT", write_scope=write_scope, affected='["records.md"]', budget=budget,
                       o1_verifier='"REVIEW"', secondary="[]", dependencies="{}")
    return plan_text(block, prose=prose)


class Flow:
    """An accepted plan with one DOCUMENT item, and the records an item's route reads."""

    def __init__(self, budget: int = 3) -> None:
        self.sc = Scenario(MANIFEST, {**FILES, "plans/work.md": document_item(budget)})
        self.accept_plan()
        self.counter = 0

    def accept_plan(self) -> dict:
        sc = self.sc
        objective, item = sc.rev("plan.work.objective"), sc.rev("plan.work.item")
        acceptance = judgment("PLAN_ACCEPTANCE", {"units": ["plan.work"]}, "ACCEPTED", actor=OWNER,
                              basis=[content("plan.work.objective", objective), content("plan.work.item", item, "PLAN_CONTROL")],
                              fields={"objective": {"unit": "plan.work.objective", "rev": objective},
                                      "items": [{"unit": "plan.work.item", "rev": item}]})
        sc.admit(acceptance)
        return acceptance

    def w(self) -> Workflow:
        return Workflow(self.sc.derive())

    def item(self):
        (item,) = self.w().items.all
        return item

    def route(self) -> str:
        return self.item().route.route

    def _candidate(self, files: dict[str, str]) -> tuple[str, str, str, dict[str, str]]:
        sc = self.sc
        merged = dict(sc.files, **files)
        cand = sc.add_tree(tree(merged, sc.manifest))
        x = "sha256:" + hashlib.sha256(f"ssds.transformation.v1|{sc.head}|{cand}".encode()).hexdigest()
        return sc.head, cand, x, merged

    def submit(self, text: str, outcome: str = "COMPLETE") -> tuple[str, str]:
        self.counter += 1
        task = f"task-{self.counter}"
        base, cand, x, _ = self._candidate({"records.md": text})
        item = self.item()
        result = record("TASK_RESULT", target={"task": task, "candidate": cand, "transformation": x, "base": base},
                        outcome=outcome, actor=agent("maker"), actor_class="AGENT", frame={"transformation": x},
                        fields={"slots": SLOTS})
        result["binding"] = dict(fresh(agent("maker"), task), obligation=item.obligation.id,
                                 item={"unit": "plan.work.item", "rev": self.sc.rev("plan.work.item")})
        self.sc.admit(with_id(result))
        return x, cand

    def review(self, x: str, cand: str, outcome: str, findings: list | None = None, actor: str = agent("checker")) -> dict:
        self.counter += 1
        task = f"review-{self.counter}"
        before, after = self.sc.view(), self.sc.view(cand)
        changed = [u for u in after.structure.units if u not in before.structure.units or before.rev(u) != after.rev(u)]
        verdict = judgment("REVIEW", {"transformation": x}, outcome, actor=actor, actor_class="AGENT",
                           basis=[content(u, after.rev(u)) for u in sorted(changed)]
                           + [content("plan.work.item", self.sc.rev("plan.work.item"))],
                           frame={"transformation": x}, binding=fresh(actor, task))
        result = record("TASK_RESULT", target={"task": task}, outcome="COMPLETE", actor=actor, actor_class="AGENT",
                        fields={"slots": {"claims": [], "findings": findings if findings is not None else {"none": "NONE_FOUND"}}})
        result["binding"] = fresh(actor, task)
        self.sc.admit(verdict, with_id(result))
        return verdict

    def integrate(self, x: str, cand: str) -> None:
        sc = self.sc
        sc.entries.append(admission_body(sc.position, sc.head, cand, integrates=x))
        sc.files = {p: e.data.decode() for p, e in sc.trees[cand].items() if p != ".ssds/manifest.toml"}
        sc.head = cand

    def iterate_adverse(self) -> None:
        """One iteration whose result is PARTIAL (incomplete): within budget it is the next iteration."""

        self.submit(f"# Records attempt {self.counter}\n", outcome="PARTIAL")

    def decide(self, decision, outcome: str, actor: str = PRINCIPAL, plan_change: dict[str, str] | None = None) -> tuple[dict, tuple | None]:
        """A coordination decision naming ``decision``; an AMEND carries its plan change in the same request."""

        self.counter += 1
        task = f"coord-{self.counter}"
        actor_class = "HUMAN" if actor.startswith("human:") else "AGENT"
        record_ = judgment("COORDINATION_DECISION", {"records": [decision.id]}, outcome, actor=actor, actor_class=actor_class,
                           binding=fresh(actor, task), fields={"tasks": []})
        records = [record_]
        change = None
        if plan_change is not None:
            base, cand, x, _ = self._candidate(plan_change)
            result = record("TASK_RESULT", target={"task": task, "candidate": cand, "transformation": x, "base": base},
                            outcome="COMPLETE", actor=actor, actor_class=actor_class, frame={"transformation": x})
            result["binding"] = fresh(actor, task)
            records.append(with_id(result))
            change = (x, cand)
        self.sc.admit(*records)
        return record_, change


def objective_change(n: int) -> dict[str, str]:
    """A plan change elsewhere: the Objective, leaving the item unchanged."""

    return {"plans/work.md": document_item(budget=1).replace("Adaptive solver.", f"Adaptive solver, round {n}.")}


class Routes(unittest.TestCase):
    def test_dispatch_then_pending_then_discharged_then_drift(self) -> None:
        f = Flow()
        self.assertEqual((f.route(), f.item().readiness().state), ("dispatch", READY))
        x, cand = f.submit("# Records\nThe solver adapts.\n")
        self.assertEqual(f.route(), "pending-candidate", "open_candidate_keeps_its_routes")
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        self.assertEqual(f.route(), "discharged", "the predicate holds")
        f.sc.absorb({"records.md": "# Records\nSomeone else edited this.\n"})
        item = f.item()
        self.assertEqual((item.route.route, item.moved), ("re-dispatch", True), "drift: its outputs moved")

    def test_rejected_and_incomplete_candidates_are_not_pending(self) -> None:
        f = Flow()
        x, cand = f.submit("# Records\nWrong.\n")
        f.review(x, cand, "NO_PASS", findings=[{"obligation": "o1", "units": ["records"]}])
        self.assertEqual(f.route(), "re-dispatch", "rejected_candidate_not_pending: an in-scope NO-PASS is the next iteration")
        g = Flow()
        g.submit("# Records\nHalf.\n", outcome="PARTIAL")
        self.assertEqual(g.route(), "re-dispatch", "incomplete_candidate_not_pending")

    def test_an_out_of_scope_no_pass_goes_to_the_principal(self) -> None:
        f = Flow()
        x, cand = f.submit("# Records\nFine here.\n")
        f.review(x, cand, "NO_PASS", findings=[{"units": ["design"]}])
        self.assertTrue(f.route().startswith("COORDINATE:finding:"))


    def test_a_no_pass_stating_no_findings_reaches_the_principal(self) -> None:
        # A8 (reading E30): with no findings stated, the decision is the principal's, so nothing is lost
        f = Flow()
        x, cand = f.submit("# Records\nUnclear.\n")
        f.review(x, cand, "NO_PASS")
        self.assertTrue(f.route().startswith("COORDINATE:finding:"))

    def test_the_implementers_own_pass_does_not_discharge(self) -> None:
        f = Flow()
        x, cand = f.submit("# Records\nSelf-reviewed.\n")
        f.review(x, cand, "PASS", actor=agent("maker"))
        f.integrate(x, cand)
        self.assertNotEqual(f.route(), "discharged")


class BudgetChains(unittest.TestCase):
    """SD-54 and SD-55 at the real owner (S3 budget_* and recurrence_* cases)."""

    def spent(self) -> Flow:
        f = Flow(budget=1)
        f.iterate_adverse()
        return f

    def decision(self, f: Flow):
        (d,) = [o for o in f.item().route.decisions if o.target.get("condition") == "budget-spent"]
        return d

    def test_budget_open(self) -> None:
        f = self.spent()
        self.assertEqual(f.route(), "COORDINATE:budget-spent")
        self.assertIsNone(self.decision(f).target["after"])

    def test_escalate_answers_nothing(self) -> None:
        f = self.spent()
        first = self.decision(f)
        f.decide(first, "ESCALATE")
        self.assertEqual((f.route(), self.decision(f).id), ("COORDINATE:budget-spent", first.id))

    def test_amend_elsewhere_waits_then_a_new_decision_names_it(self) -> None:
        f = self.spent()
        answer, (x, cand) = f.decide(self.decision(f), "AMEND", plan_change=objective_change(1))
        self.assertEqual(f.route(), f"awaiting-amendment:{answer['id']}", "budget_amend_elsewhere_waits")
        f.integrate(x, cand)
        self.assertEqual(f.route(), "COORDINATE:budget-spent", "budget_amend_elsewhere_integrated")
        self.assertEqual(self.decision(f).target["after"], answer["id"])

    def test_partition_hands_the_route_to_the_parts(self) -> None:
        f = self.spent()
        answer, _ = f.decide(self.decision(f), "PARTITION")
        self.assertEqual(f.route(), f"partitioned:{answer['id']}")

    def test_an_amendment_of_the_item_keeping_the_budget_spent_starts_a_fresh_chain(self) -> None:
        # budget_answered_condition_holds: an R1 tightening (one more required slot) gives the item a new revision
        # with the same obligation, so the budget stays spent and a fresh chain starts at the new revision
        f = self.spent()
        first = self.decision(f)
        tightened = document_item(budget=1).replace('"deviations"]', '"deviations", "findings"]')
        self.assertNotEqual(tightened, document_item(budget=1))
        answer, (x, cand) = f.decide(first, "AMEND", plan_change={"plans/work.md": tightened})
        f.integrate(x, cand)
        d = self.decision(f)
        self.assertEqual(f.route(), "COORDINATE:budget-spent")
        self.assertNotEqual(d.target["rev"], first.target["rev"], "a fresh chain at the new revision")
        self.assertIsNone(d.target["after"])

    def chain_of_three(self) -> tuple[Flow, list[str]]:
        f = self.spent()
        answers = []
        for n in range(3):
            answer, (x, cand) = f.decide(self.decision(f), "AMEND", plan_change=objective_change(n + 1))
            f.integrate(x, cand)
            answers.append(answer["id"])
        return f, answers

    def test_recurrence_holds_the_next_decision_for_a_human(self) -> None:
        f, answers = self.chain_of_three()
        self.assertEqual(f.route(), "human-attention:budget-spent", "budget_recurrence")
        held = self.decision(f)
        self.assertEqual((held.target["after"], held.holder), (answers[-1], "HUMAN"))
        f.decide(held, "AMEND", plan_change=objective_change(9))
        self.assertEqual(self.decision(f).id, held.id, "recurrence_principal_answer_does_not_count")

    def test_a_humans_answer_to_a_held_decision_continues_the_chain(self) -> None:
        f, _ = self.chain_of_three()
        held = self.decision(f)
        answer, (x, cand) = f.decide(held, "AMEND", actor=HUMAN, plan_change=objective_change(4))
        self.assertEqual(f.route(), f"awaiting-amendment:{answer['id']}", "recurrence_human_amend_waits")
        f.integrate(x, cand)
        self.assertEqual(f.route(), "human-attention:budget-spent", "recurrence_human_amend_integrated")
        self.assertEqual(self.decision(f).target["after"], answer["id"], "the answered decision is never open again")

    def test_held_partition_challenge_and_escalate(self) -> None:
        f, _ = self.chain_of_three()
        answer, _ = f.decide(self.decision(f), "PARTITION", actor=HUMAN)
        self.assertEqual(f.route(), f"partitioned:{answer['id']}", "recurrence_human_partition")
        g, _ = self.chain_of_three()
        held = self.decision(g)
        g.decide(held, "ESCALATE", actor=HUMAN)
        self.assertEqual(self.decision(g).id, held.id, "recurrence_human_escalate_answers_nothing")
        h, _ = self.chain_of_three()
        challenge_answer, _ = h.decide(self.decision(h), "CHALLENGE", actor=HUMAN)
        self.assertEqual(h.route(), f"awaiting-challenge:{challenge_answer['id']}", "recurrence_human_challenge_waits")


class OutOfScopeFindings(unittest.TestCase):
    """RR-8 at the real owner (S3 oos_* cases)."""

    def integrated_then_objected(self) -> tuple[Flow, dict]:
        f = Flow()
        x, cand = f.submit("# Records\nDocumented.\n")
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        objection = f.review(x, cand, "NO_PASS", findings=[{"units": ["design"]}], actor=HUMAN)
        return f, objection

    def test_oos_latest_and_answered(self) -> None:
        f, objection = self.integrated_then_objected()
        self.assertEqual(f.route(), f"COORDINATE:finding:{objection['id']}", "oos_latest")
        (decision,) = [o for o in f.item().route.decisions if o.target.get("finding") == objection["id"]]
        f.decide(decision, "AMEND")
        self.assertEqual(f.route(), "re-dispatch", "oos_latest_answered: the item's route continues")

    def test_oos_latest_masked_by_pending_still_routes_the_finding(self) -> None:
        f, objection = self.integrated_then_objected()
        f.submit("# Records\nDocumented again.\n")
        item = f.item()
        self.assertEqual(item.route.route, "pending-candidate")
        self.assertIn(objection["id"], [o.target.get("finding") for o in item.route.decisions])

    def test_oos_on_an_earlier_enactment_reaches_the_principal(self) -> None:
        f, objection = self.integrated_then_objected()
        (decision,) = [o for o in f.item().route.decisions if o.target.get("finding") == objection["id"]]
        x, cand = f.submit("# Records\nSecond enactment.\n")
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        self.assertIn(decision.id, [o.id for o in f.item().route.decisions], "oos_on_earlier_enactment")


class Identity(unittest.TestCase):
    """RR-4 (SD-52) as the assembled transition: out(o), iteration count and acceptance wait."""

    def test_tightening_loosening_and_prose(self) -> None:
        f = Flow(budget=3)
        f.iterate_adverse()
        first = f.item()
        self.assertEqual(first.iterations, 1)
        for change, keeps, issuable in (("tighten", True, True), ("loosen", True, False), ("prose", False, None)):
            with self.subTest(change=change):
                g = Flow(budget=3)
                g.iterate_adverse()
                before = g.item().obligation.id
                text = {"tighten": document_item(budget=2), "loosen": document_item(budget=4),
                        "prose": document_item(budget=3, prose="Document the solver fully.\n")}[change]
                g.sc.absorb({"plans/work.md": text})
                w = g.w()
                ids = {i.obligation.id: i for i in w.items.all}
                self.assertEqual(before in ids, keeps)
                if keeps:
                    self.assertEqual(ids[before].iterations, 1, "the iteration count survives (a budget is not reset)")
                    self.assertEqual(w.issuable("plan.work.item"), issuable)
                else:
                    self.assertEqual(ids, {}, "the new work waits for a plan acceptance")
                    self.assertEqual(len(w.of_kind("PLAN_ACCEPT")), 1)

    def test_an_r1_tightening_the_content_already_meets_still_re_dispatches(self) -> None:
        # b365947 N4: the review read the item revision, so a tightening makes it non-current: a fresh enactment
        f = Flow()
        x, cand = f.submit("# Records\nDocumented.\n")
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        self.assertEqual(f.route(), "discharged")
        f.sc.absorb({"plans/work.md": document_item(budget=2)})
        self.assertEqual(f.route(), "re-dispatch")


if __name__ == "__main__":
    unittest.main()
