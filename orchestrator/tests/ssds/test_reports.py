"""Phase E step 5c: reports, escalation floors, routing, persistence and recurrence (catalogue §15; Manual §15, A8).

Expected values are written from §15.3's routing table, §15.4's floors, §15.2's persistence rule, §15.5's
outcomes, §15.6's reclassification and §15.7's recurrence, not computed by the rule under test.
"""

from __future__ import annotations

import unittest

from ssds.derivation.reports import allowed_outcomes
from ssds.derivation.workflow import Workflow
from ssds.ledger.read import with_id

from ._fixtures import record
from ._scenario import HUMAN, HUMAN_B, OWNER, Scenario, agent, challenge, content, fresh, judgment
from .test_routes import Flow

MANIFEST = '''
    [[unit]]
    id = "numerics"
    kind = "D2"
    scope = [{ path = "numerics.md" }]
    [[unit]]
    id = "arch"
    kind = "D3"
    scope = [{ path = "arch.md" }]
'''
FILES = {"numerics.md": "n\n", "arch.md": "a\n"}


def report(kind: str, units: list[str], materiality: str = "ROUTINE", reasons: tuple[str, ...] = ("ANOMALY",),
           actor: str = agent("worker"), blocking: bool = False, binding: dict | None = None) -> dict:
    rec = record(kind, target={"units": units}, outcome=None, actor=actor, actor_class="AGENT",
                 fields={"materiality": materiality, "blocking": blocking}, reason=list(reasons))
    if binding is not None:
        rec["binding"] = binding
    return with_id(rec)


def attention(w: Workflow) -> dict:
    return {o.target.get("report") or o.target.get("floor") or o.target.get("waiting"): o for o in w.of_kind("HUMAN_ATTENTION")}


def coordinate(w: Workflow) -> dict:
    return {o.target["report"]: o for o in w.of_kind("COORDINATE") if "report" in o.target}


def wf(sc: Scenario) -> Workflow:
    return Workflow(sc.derive())


class Floors(unittest.TestCase):
    def test_serious_challenge_and_human_question_are_critical(self) -> None:
        sc = Scenario(MANIFEST, FILES)
        acc = judgment("ACCEPTANCE", sc.triple("arch"), "PASS", actor=HUMAN, basis=[content("arch", sc.rev("arch"))])
        sc.admit(acc)
        serious = judgment("CHALLENGE", {"record": acc["id"]}, None, actor=HUMAN_B,
                           fields={"blocking": True, "serious": True, "inquiry": "CONFIRMATORY", "materiality": "ROUTINE"})
        question = report("HUMAN_QUESTION", ["arch"], reasons=("DECISION_NEEDED",))
        sc.admit(serious, question)
        w = wf(sc)
        attended = attention(w)
        self.assertEqual(attended[serious["id"]].params["materiality"], "CRITICAL")
        self.assertEqual(attended[question["id"]].params["materiality"], "CRITICAL")
        self.assertIn({"record": serious["id"]}, [o.target for o in w.of_kind("ADJUDICATE")], "a Serious Challenge also needs adjudication")

    def test_the_domain_floor_and_a_policy_floor_raise(self) -> None:
        sc = Scenario(MANIFEST, FILES, policy='schema = 1\n[[workflow.floors]]\nkind = "FINDING"\nreason = "OPPORTUNITY"\nmateriality = "MATERIAL"\n')
        on_d2 = report("FINDING", ["numerics"])
        raised = report("FINDING", ["arch"], reasons=("OPPORTUNITY",))
        plain = report("FINDING", ["arch"])
        sc.admit(on_d2, raised, plain)
        attended = attention(wf(sc))
        self.assertEqual(attended[on_d2["id"]].params["materiality"], "MATERIAL", "a report on a D2 unit is at least MATERIAL")
        self.assertEqual(attended[raised["id"]].params["materiality"], "MATERIAL", "policy raises")
        self.assertNotIn(plain["id"], attended, "a ROUTINE finding is recorded, not escalated")

    def test_a_tension_against_accepted_d2_authority_is_critical(self) -> None:
        sc = Scenario(MANIFEST, FILES, modes={"numerics": {"mode": "LEGACY", "protocol": "7.2.1"}})
        sc.admit(judgment("LEGACY_ACCEPTANCE", sc.triple("numerics"), "IMPORTED", actor="admission:ed25519:test",
                          actor_class="ADMISSION", fields={"legacy": ["7.2.1"]}))
        tension = report("FINDING", ["numerics"], reasons=("TENSION",))
        sc.admit(tension)
        w = wf(sc)
        self.assertGreater(w.d.valid("numerics"), 0)
        self.assertEqual(attention(w)[tension["id"]].params["materiality"], "CRITICAL")

    def test_reclassification_only_of_a_non_floor_material_report(self) -> None:
        sc = Scenario(MANIFEST, FILES)
        material = report("FINDING", ["arch"], materiality="MATERIAL")
        floor = report("FINDING", ["numerics"], materiality="MATERIAL")
        sc.admit(material, floor)
        for target in (material, floor):
            sc.admit(judgment("MATERIALITY_RECLASSIFICATION", {"record": target["id"]}, "ROUTINE", actor=agent("principal"),
                              actor_class="AGENT"))
        attended = attention(wf(sc))
        self.assertNotIn(material["id"], attended, "moved to the digest while the reclassification is in force")
        self.assertIn(floor["id"], attended, "a floor item cannot be reclassified")


class Routing(unittest.TestCase):
    def test_a_request_from_an_item_task_goes_to_its_plans_principal(self) -> None:
        f = Flow()
        item = f.item()
        request = report("AMENDMENT_REQUEST", ["records"], reasons=("SCOPE_DEVIATION",), blocking=True,
                         binding=dict(fresh(agent("maker"), "task-9"), obligation=item.obligation.id))
        f.sc.admit(request)
        decision = coordinate(f.w())[request["id"]]
        self.assertEqual((decision.holder, decision.plan), ("PRINCIPAL", "plan.work"))

    def test_outside_every_plan_the_standing_plan_or_the_human(self) -> None:
        for policy, holder in (("schema = 1\n[workflow]\nstanding_plan = \"plan.standing\"\n", "PRINCIPAL"), ("schema = 1\n", "HUMAN")):
            with self.subTest(holder=holder):
                sc = Scenario(MANIFEST, FILES, policy=policy)
                blocker = report("BLOCKER", ["arch"], reasons=("ENVIRONMENT",))
                sc.admit(blocker)
                self.assertEqual(coordinate(wf(sc))[blocker["id"]].holder, holder)


class Persistence(unittest.TestCase):
    """§15.2: keyed on the report; closed only by a resolving record in force."""

    def test_a_coordination_decision_resolves_and_a_challenge_reopens(self) -> None:
        sc = Scenario(MANIFEST, FILES)
        blocker = report("BLOCKER", ["arch"], reasons=("ENVIRONMENT",))
        sc.admit(blocker)
        decline = judgment("COORDINATION_DECISION", {"records": [blocker["id"]]}, "DECLINE", actor=HUMAN, fields={"tasks": []})
        sc.admit(decline)
        self.assertNotIn(blocker["id"], coordinate(wf(sc)))
        sc.admit(challenge({"record": decline["id"]}))
        self.assertIn(blocker["id"], coordinate(wf(sc)), "the resolving record is no longer in force")

    def test_a_disallowed_outcome_resolves_nothing(self) -> None:
        sc = Scenario(MANIFEST, FILES)
        request = report("AMENDMENT_REQUEST", ["numerics"], materiality="CRITICAL", reasons=("AUTHORITY_DEFECT",))
        sc.admit(request)
        sc.admit(judgment("COORDINATION_DECISION", {"records": [request["id"]]}, "DECLINE", actor=HUMAN, fields={"tasks": []}))
        self.assertIn(request["id"], coordinate(wf(sc)), "DECLINE is not allowed for a floor report")

    def test_only_an_authenticated_humans_decision_discharges_attention(self) -> None:
        sc = Scenario(MANIFEST, FILES)
        question = report("HUMAN_QUESTION", ["arch"], reasons=("DECISION_NEEDED",))
        sc.admit(question)
        o = attention(wf(sc))[question["id"]]
        sc.admit(judgment("HUMAN_DECISION", {"obligation": o.id}, "ANSWER", actor=agent("principal"), actor_class="AGENT"))
        self.assertIn(question["id"], attention(wf(sc)), "an agent cannot discharge human attention (A8)")
        sc.admit(judgment("HUMAN_DECISION", {"obligation": o.id}, "ANSWER", actor=HUMAN))
        self.assertNotIn(question["id"], attention(wf(sc)))

    def test_withdrawal_and_the_target_moving(self) -> None:
        sc = Scenario(MANIFEST, FILES)
        material = report("FINDING", ["arch"], materiality="MATERIAL")
        floor = report("FINDING", ["numerics"], materiality="MATERIAL")
        sc.admit(material, floor)
        for target in (material, floor):
            sc.admit(judgment("WITHDRAWAL", {"record": target["id"]}, None, actor=agent("worker"), actor_class="AGENT"))
        sc.absorb({"numerics.md": "n2\n"})
        attended = attention(wf(sc))
        self.assertNotIn(material["id"], attended, "a non-floor withdrawn report moves to the digest")
        self.assertIn("withdrawn by raiser", attended[floor["id"]].detail)
        self.assertIn("target changed since raised", attended[floor["id"]].detail)


class FloorEvents(unittest.TestCase):
    def test_a_plan_objective_change_and_a_missing_judge(self) -> None:
        f = Flow()
        f.sc.absorb({"plans/work.md": f.sc.files["plans/work.md"].replace("Adaptive solver.", "A different goal.")})
        floors = {k for k in attention(f.w()) if isinstance(k, str) and k.startswith("objective:")}
        self.assertEqual(len(floors), 1, "an amendment changing the objective is a CRITICAL floor event")
        sc = Scenario(MANIFEST, FILES)
        w = wf(sc)
        waiting = [o for o in w.of_kind("HUMAN_ATTENTION") if "waiting" in o.target]
        self.assertTrue(waiting, "ACCEPT(s) with no eligible judge derives human attention naming it")


class Recurrence(unittest.TestCase):
    def test_the_same_hard_template_failing_on_one_obligation_across_iterations(self) -> None:
        # §15.7: detection is mechanical; the decision carries the convergence duty, answered by the principal
        f = Flow(budget=5)
        f.submit("# Records 1\n", outcome="PARTIAL", slots={"claims": []})
        self.assertEqual([o for o in f.w().of_kind("COORDINATE") if o.target.get("recurrence")], [], "once is no recurrence")
        f.submit("# Records 2\n", outcome="PARTIAL", slots={"claims": []})
        (found,) = [o for o in f.w().of_kind("COORDINATE") if o.target.get("recurrence") == "template"]
        self.assertEqual((found.target["of"], found.holder, found.plan), ("OBLIGATION.slots_filled", "PRINCIPAL", "plan.work"))
        f.sc.admit(judgment("COORDINATION_DECISION", {"records": [found.id]}, "DECLINE", actor=agent("principal"),
                            actor_class="AGENT", fields={"tasks": []}))
        self.assertNotIn(found.id, {o.id for o in f.w().obligations})


class RefusedReviews(unittest.TestCase):
    def test_a_refused_joint_invariant_review_derives_a_decision(self) -> None:
        # §10.4: until a coordination decision answers it; outside every plan with no standing plan, the human
        from .test_obligations import HUMANS, TWO

        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        sc.absorb({"impl.md": "i2\n"})
        (joint,) = wf(sc).of_kind("JOINT_INVARIANT")
        sc.admit(judgment("REVIEW", {"integrated": "JOINT_INVARIANT", "of": "arch-impl", "at": joint.target["change"],
                                     "changes": []}, "NO_PASS", actor=HUMAN, basis=[content("impl", sc.rev("impl"))]))
        (decision,) = [o for o in wf(sc).of_kind("COORDINATE") if o.target.get("refused") == joint.id]
        self.assertEqual(decision.holder, "HUMAN")
        sc.admit(judgment("COORDINATION_DECISION", {"records": [decision.id]}, "AMEND", actor=HUMAN, fields={"tasks": []}))
        self.assertNotIn(decision.id, {o.id for o in wf(sc).obligations})


class Outcomes(unittest.TestCase):
    def test_allowed_outcomes(self) -> None:
        self.assertEqual(allowed_outcomes("AMENDMENT_REQUEST", ("AUTHORITY_DEFECT",), "D4"), {"CHALLENGE", "ESCALATE"})
        self.assertNotIn("RESOLVE_LOCAL", allowed_outcomes("AMENDMENT_REQUEST", ("CONTRACT_DEFECT",), "D4"))
        self.assertIn("AMEND", allowed_outcomes("AMENDMENT_REQUEST", ("CONTRACT_DEFECT",), "D4"))
        self.assertNotIn("DECLINE", allowed_outcomes("FINDING", ("ANOMALY",), "D3", floor=True))
        self.assertIn("RESOLVE_LOCAL", allowed_outcomes("BLOCKER", ("ENVIRONMENT",), "D4"))


if __name__ == "__main__":
    unittest.main()
