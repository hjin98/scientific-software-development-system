"""Repairs of the Phase E step 5 review of 879fa490 (B1-B14, N1, N2, N5), each case failing on the reviewed code.

Expected values are written from the governing clauses each blocker names (Manual §10.3, §10.4, §13.7, §15.2,
§15.4-§15.6, §6.8, A8; catalogue §13.7, §15.5; SD-54, SD-55), never computed by the rule under test. The
lifecycle replay (reading E15) restates the properties of ``qualification/ssds80/models/run_models.py``
(``lifecycle_properties``, P1-P6) and checks them on constructed ledgers through the real owner.
"""

from __future__ import annotations

import hashlib
import itertools
import os
import random
import unittest
from contextlib import contextmanager
from unittest import mock

from ssds.ledger.read import Chain, LedgerEntry, with_id

from . import _scenario
from ._fixtures import admission_body, record
from ._scenario import HUMAN, Scenario, adjudication, agent, content, fresh, judgment, submit
from ._scenario import integrate as integrate_change
from .test_partition import PartFlow, partitioned_and_worked, plan
from .test_reports import FILES, MANIFEST, attention, coordinate, report, wf
from .test_routes import PRINCIPAL, SLOTS, Flow, document_item, objective_change


def escalations(w) -> dict:
    return {o.target["escalated"]: o for o in w.of_kind("HUMAN_ATTENTION") if "escalated" in o.target}


def decisions(item, key: str) -> list:
    return [o for o in item.route.decisions if key in o.target]


def finding_decision(item, review: dict):
    (d,) = [o for o in item.route.decisions if o.target.get("finding") == review["id"]]
    return d


def integrated_then_objected(f: Flow) -> dict:
    x, cand = f.submit("# Records\nDocumented.\n")
    f.review(x, cand, "PASS")
    f.integrate(x, cand)
    return f.review(x, cand, "NO_PASS", findings=[{"units": ["design"]}], actor=HUMAN)


@contextmanager
def hashed_digests():
    """Entry digests as real ledgers have them: hashes, whose order says nothing about position (B4)."""

    original = _scenario.chain_of

    def chain_of(ledger_id, entries, objects=None):
        chain = original(ledger_id, entries, objects)
        out = tuple(LedgerEntry(e.position, e.commit, e.parents, e.entry, e.entry_json, e.signature,
                                "sha256:" + hashlib.sha256(f"entry-{e.position}".encode()).hexdigest(), e.objects)
                    for e in chain.entries)
        return Chain(chain.ledger_id, out)

    with mock.patch.object(_scenario, "chain_of", chain_of):
        yield


def work_part_by(f: PartFlow, part, files: dict[str, str], maker: str) -> None:
    f.counter += 1
    task = f"part-{f.counter}"
    base, cand, x, _ = f._candidate(files)
    result = record("TASK_RESULT", target={"task": task, "candidate": cand, "transformation": x, "base": base},
                    outcome="COMPLETE", actor=maker, actor_class="AGENT", frame={"transformation": x}, fields={"slots": SLOTS})
    result["binding"] = dict(fresh(maker, task), obligation=part.obligation.id, item_key=part.key,
                             write_scope=list(part.share[3]), item={"unit": "plan.work.item", "rev": f.sc.rev("plan.work.item")})
    f.sc.admit(with_id(result))
    f.review(x, cand, "PASS")
    f.integrate(x, cand)


class Partitions(unittest.TestCase):
    def test_b1_a_repartition_keeps_an_undischarged_sibling(self) -> None:
        # §13.7: discharged when every part is; a re-partition of b never drops a, which was never worked
        f = PartFlow()
        f.spend(f.item().obligation)
        f.partition(f.budget_decision(f.item()), [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
        f.spend(f.item().parts[1].obligation, "notes/a.md")
        f.partition(f.budget_decision(f.item().parts[1]), [(["o2"], ["notes.a"]), (["o3"], ["notes.b"])])
        self.assertEqual(sorted(tuple(sorted(p.share[2])) for p in f.item().parts), [("o1",), ("o2",), ("o3",)])
        for share, path in ((frozenset({"o2"}), "notes/a.md"), (frozenset({"o3"}), "notes/b.md")):
            part = next(p for p in f.item().parts if p.share[2] == share)
            f.work_part(part, {path: f"done {path}\n"})
        self.assertEqual(f.item().discharge(), "OPEN", "o1 was never done")
        self.assertTrue(f.route().startswith("partitioned:"))

    def test_b12_an_invalid_partition_answers_nothing(self) -> None:
        f = PartFlow()
        f.spend(f.item().obligation)
        decision = f.budget_decision(f.item())
        f.partition(decision, [(["o1"], ["records"]), (["o1", "o2"], ["notes.a", "notes.b"])])
        item = f.item()
        self.assertEqual((item.route.route, [d.id for d in decisions(item, "condition")]), ("COORDINATE:budget-spent", [decision.id]))
        g = Flow(budget=1)
        g.iterate_adverse()
        (d,) = decisions(g.item(), "condition")
        g.decide(d, "PARTITION")  # no parts object at all
        self.assertEqual((g.route(), [o.id for o in decisions(g.item(), "condition")]), ("COORDINATE:budget-spent", [d.id]))

    def test_b4_the_item_level_target_is_the_latest_integration(self) -> None:
        with hashed_digests():
            f = PartFlow()
            f.spend(f.item().obligation)
            f.partition(f.budget_decision(f.item()), [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
            work_part_by(f, f.item().parts[0], {"records.md": "# Records done\n"}, agent("maker-a"))
            work_part_by(f, f.item().parts[1], {"notes/a.md": "a done\n", "notes/b.md": "b done\n"}, agent("maker-b"))
            item = f.item()
            entries = f.sc.derive().s.h.chain.entries
            latest = max(p.latest_integrated.integrated for p in item.parts)
            self.assertEqual(item.item_level_target["at"], entries[latest].digest)
            target = item.item_level_target
            own = judgment("REVIEW", target, "PASS", actor=agent("maker-b"), actor_class="AGENT",
                           basis=[content(u, f.sc.rev(u)) for u in ("records", "notes.a", "notes.b")],
                           binding=fresh(agent("maker-b"), "il-x"))
            result = record("TASK_RESULT", target={"task": "il-x"}, outcome="COMPLETE", actor=agent("maker-b"),
                            actor_class="AGENT", fields={"slots": {"claims": [], "findings": {"none": "NONE_FOUND"}}})
            result["binding"] = fresh(agent("maker-b"), "il-x")
            f.sc.admit(own, with_id(result))
            w = f.w()
            self.assertTrue(w.d.j.nonind(own["id"]), "a part's author is not independent of the whole item")
            self.assertEqual(w.items.all[0].discharge(), "OPEN")

    def test_b9_an_objection_naming_a_part_stands_until_that_part_is_redone(self) -> None:
        f = partitioned_and_worked()
        f.item_level("NO_PASS", findings=[{"part": 0, "units": ["records"]}])
        f.sc.absorb({"notes/a.md": "someone else\n"})
        f.work_part(f.item().parts[1], {"notes/a.md": "a redone\n", "notes/b.md": "b done\n"})
        self.assertEqual(f.item().parts[0].discharge(), "OPEN", "part 1's redo does not answer an objection to part 0")
        f.work_part(f.item().parts[0], {"records.md": "# Records redone\n"})
        self.assertEqual(f.item().parts[0].discharge(), "DISCHARGED", "the named part re-integrated after the objection")

    def test_b9_an_objection_naming_no_part_keeps_its_decision(self) -> None:
        g = partitioned_and_worked()
        g.item_level("NO_PASS")
        (d,) = decisions(g.item(), "condition")
        g.sc.absorb({"notes/a.md": "someone else\n"})
        g.work_part(g.item().parts[1], {"notes/a.md": "a redone\n", "notes/b.md": "b done\n"})
        item = g.item()
        self.assertEqual(item.route.route, "COORDINATE:item-level-no-part")
        self.assertIn(d.id, {o.id for o in g.w().obligations}, "never retired by a later obligation whose judge did not see it")


class Escalation(unittest.TestCase):
    def test_b2_an_escalated_report_derives_human_attention(self) -> None:
        sc = Scenario(MANIFEST, FILES, policy='schema = 1\n[workflow]\nstanding_plan = "plan.standing"\n')
        blocker = report("BLOCKER", ["arch"], reasons=("ENVIRONMENT",))
        sc.admit(blocker)
        escalate = judgment("COORDINATION_DECISION", {"records": [blocker["id"]]}, "ESCALATE", actor=PRINCIPAL,
                            actor_class="AGENT", fields={"tasks": []})
        sc.admit(escalate)
        o = escalations(wf(sc)).get(escalate["id"])
        self.assertIsNotNone(o, "ESCALATE means human attention (§15.5)")
        self.assertEqual(o.holder, "HUMAN")
        sc.admit(judgment("HUMAN_DECISION", {"obligation": o.id}, "ANSWER", actor=HUMAN))
        self.assertNotIn(escalate["id"], escalations(wf(sc)))

    def test_b2_escalate_and_resolve_local_do_not_answer_an_item_route(self) -> None:
        for outcome in ("ESCALATE", "RESOLVE_LOCAL"):
            with self.subTest(outcome=outcome):
                f = Flow()
                objection = integrated_then_objected(f)
                d = finding_decision(f.item(), objection)
                answer, _ = f.decide(d, outcome)
                self.assertEqual(f.route(), f"COORDINATE:finding:{objection['id']}", "§15.5: ESCALATE does not answer an item route")
                self.assertIn(d.id, {o.id for o in f.w().obligations})
                if outcome == "ESCALATE":
                    self.assertIn(answer["id"], escalations(f.w()))

    def test_b2_a_budget_escalation_derives_human_attention(self) -> None:
        h = Flow(budget=1)
        h.iterate_adverse()
        (d,) = decisions(h.item(), "condition")
        answer, _ = h.decide(d, "ESCALATE")
        self.assertEqual(h.route(), "COORDINATE:budget-spent")
        self.assertIn(answer["id"], escalations(h.w()))


class Routes(unittest.TestCase):
    def test_b3_a_later_candidates_out_of_scope_no_pass_reaches_the_principal(self) -> None:
        f = Flow(budget=5)
        x, cand = f.submit("# Records\nDocumented.\n")
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        f.sc.absorb({"records.md": "# Records\nEdited elsewhere.\n"})
        x2, c2 = f.submit("# Records\nRedone.\n")
        objection = f.review(x2, c2, "NO_PASS", findings=[{"units": ["design"]}])
        self.assertEqual(f.route(), f"COORDINATE:finding:{objection['id']}")

    def test_b13_findings_in_scope_only_within_write_scope_and_obligations(self) -> None:
        for label, findings in (("obligation, unit outside scope", [{"obligation": "o1", "units": ["design"]}]),
                                ("an empty list", []), ("text", ["design.md contradicts the item"]),
                                ("another item's obligation", [{"obligation": "o9"}])):
            with self.subTest(findings=label):
                f = Flow()
                x, cand = f.submit("# Records\nX.\n")
                f.review(x, cand, "NO_PASS", findings=findings)
                self.assertTrue(f.route().startswith("COORDINATE:finding:"), label)
        g = Flow()
        x, cand = g.submit("# Records\nX.\n")
        g.review(x, cand, "NO_PASS", findings=[{"obligation": "o1"}, {"units": ["records"]}])
        self.assertEqual(g.route(), "re-dispatch", "within the item's obligations and write scope: the next iteration")

    def test_b11_a_refused_plan_change_settles_the_amend(self) -> None:
        f = Flow(budget=1)
        f.iterate_adverse()
        (d,) = decisions(f.item(), "condition")
        answer, (x, _) = f.decide(d, "AMEND", plan_change=objective_change(1))
        f.sc.entries.append(admission_body(f.sc.position, f.sc.head, f.sc.head, integrates=x, decision="REJECT"))
        item = f.item()
        (after,) = decisions(item, "condition")
        self.assertEqual((item.route.route, after.target["after"]), ("COORDINATE:budget-spent", answer["id"]))

    def test_b11_an_amend_with_no_plan_change_is_settled(self) -> None:
        f = Flow(budget=1)
        f.iterate_adverse()
        (d,) = decisions(f.item(), "condition")
        answer, _ = f.decide(d, "AMEND")
        (after,) = decisions(f.item(), "condition")
        self.assertEqual((f.route(), after.target["after"]), ("COORDINATE:budget-spent", answer["id"]))


class FindingsSurvive(unittest.TestCase):
    """RR-8 decisions are keyed on the review and survive the item route (A8, §10.4)."""

    def test_b10_across_a_prose_amendment(self) -> None:
        f = Flow()
        objection = integrated_then_objected(f)
        d = finding_decision(f.item(), objection)
        f.sc.absorb({"plans/work.md": document_item(prose="Document the solver fully.\n")})
        f.accept_plan()
        self.assertIn(d.id, {o.id for o in f.w().obligations})

    def test_b10_across_a_partition(self) -> None:
        f = PartFlow()
        x, cand = f.submit("# Records v1\n")
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        objection = f.review(x, cand, "NO_PASS", findings=[{"units": ["design"]}], actor=HUMAN)
        x2, c2 = f.submit("# Records v2\n")
        f.review(x2, c2, "PASS")
        f.integrate(x2, c2)
        d = finding_decision(f.item(), objection)
        f.sc.absorb({"records.md": "# drift\n"})
        f.partition(f.budget_decision(f.item()), [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
        self.assertTrue(f.route().startswith("partitioned:"))
        self.assertIn(d.id, {o.id for o in f.w().obligations})


class Floors(unittest.TestCase):
    def test_b5_the_objective_floor_waits_for_a_human(self) -> None:
        f = Flow()
        f.sc.absorb({"plans/work.md": f.sc.files["plans/work.md"].replace("Adaptive solver.", "A different goal.")})
        sc = f.sc
        o, i = sc.rev("plan.work.objective"), sc.rev("plan.work.item")
        sc.admit(judgment("PLAN_ACCEPTANCE", {"units": ["plan.work"]}, "ACCEPTED", actor=agent("reviewer"), actor_class="AGENT",
                          basis=[content("plan.work.objective", o), content("plan.work.item", i, "PLAN_CONTROL")],
                          fields={"objective": {"unit": "plan.work.objective", "rev": o},
                                  "items": [{"unit": "plan.work.item", "rev": i}]}))
        floors = {k: v for k, v in attention(f.w()).items() if isinstance(k, str) and k.startswith("objective:")}
        self.assertEqual(len(floors), 1, "an agent's acceptance does not retire a CRITICAL floor")
        (floor,) = floors.values()
        sc.admit(judgment("HUMAN_DECISION", {"obligation": floor.id}, "ANSWER", actor=HUMAN))
        self.assertFalse({k for k in attention(f.w()) if isinstance(k, str) and k.startswith("objective:")})

    def test_b5_removing_an_item_removes_its_criteria(self) -> None:
        f = Flow()
        with_criterion = document_item().replace("[contract]", '[[acceptance_criteria]]\nid = "c1"\nevidence = "REVIEW"\n[contract]', 1)
        f.sc.absorb({"plans/work.md": with_criterion})
        f.accept_plan()
        criteria = lambda: {k for k in attention(f.w()) if isinstance(k, str) and k.startswith("criteria:")}  # noqa: E731
        self.assertEqual(criteria(), set(), "adding a criterion changes or removes none")
        f.sc.absorb({"plans/work.md": with_criterion[: with_criterion.index("## Item")]})
        self.assertEqual(len(criteria()), 1, "removing the item removes its criteria")

    def test_b6_a_policy_floor_equal_to_the_declared_level_is_a_floor(self) -> None:
        sc = Scenario(MANIFEST, FILES, policy='schema = 1\n[[workflow.floors]]\nkind = "BLOCKER"\nmateriality = "MATERIAL"\n')
        blocker = report("BLOCKER", ["arch"], materiality="MATERIAL", reasons=("ENVIRONMENT",))
        sc.admit(blocker)
        sc.admit(judgment("MATERIALITY_RECLASSIFICATION", {"record": blocker["id"]}, "ROUTINE", actor=PRINCIPAL, actor_class="AGENT"))
        self.assertEqual(attention(wf(sc))[blocker["id"]].params["materiality"], "MATERIAL", "floor items cannot be reclassified")

    def test_b7_a_floor_outlives_its_target_unit(self) -> None:
        sc = Scenario(MANIFEST, FILES)
        tension = report("FINDING", ["numerics"], reasons=("TENSION",))
        sc.admit(tension)
        self.assertIn(tension["id"], attention(wf(sc)))
        only_arch = '''
            [[unit]]
            id = "arch"
            kind = "D3"
            scope = [{ path = "arch.md" }]
        '''
        x, cand, _ = submit(sc, {}, agent("restructurer"), "t-1", manifest=only_arch)
        integrate_change(sc, x, cand)
        w = wf(sc)
        self.assertNotIn("numerics", w.s.view.structure.units)
        self.assertEqual(attention(w)[tension["id"]].params["materiality"], "MATERIAL", "computed at admission too")

    def test_b8_the_disagreement_floor_latches(self) -> None:
        from . import test_assessment as ta
        from .test_assessment import Runs

        with mock.patch.object(ta, "UNITS", ta.UNITS.replace('kind = "D4"', 'kind = "D2"')), \
                mock.patch.object(ta, "POLICY", 'schema = 1\n[domains.D2]\nevidence = ["obl"]\n'):
            r = Runs()
            t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
            failing = r.fail(r.run(t0, ta.BAD))
            r.run(t0, ta.BAD)
            good = r.run(t1, ta.GOOD)
            view = r.sc.view(t0)
            r.sc.admit(judgment("EVIDENCE_ASSESSMENT", {"realization": good["id"], "obligation": "obl"}, "PASS",
                                actor=agent("assessor"), actor_class="AGENT",
                                basis=[_scenario.on_record(good["id"]), content("spec", view.rev("spec"))],
                                fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": view.rev("spec")}}))

            def floors() -> list:
                return [k for k in attention(wf(r.sc)) if isinstance(k, str) and k.startswith("disagreement:")]

            self.assertEqual(floors(), [f"disagreement:{failing['id']}"])
            r.sc.absorb({"a.py": "v = 2\n"})
            d = r.sc.derive()
            self.assertTrue(d.a.stale(failing["id"], d.base))
            self.assertEqual(floors(), [f"disagreement:{failing['id']}"], "latched until a human decides (§6.8)")


class Index(unittest.TestCase):
    def test_n1_a_result_bound_to_a_part_or_report_decision_has_its_obligation(self) -> None:
        f = PartFlow()
        f.spend(f.item().obligation)
        f.partition(f.budget_decision(f.item()), [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
        f.spend(f.item().parts[1].obligation, "notes/a.md")
        part_decision = f.budget_decision(f.item().parts[1])
        blocker = report("BLOCKER", ["records"], reasons=("ENVIRONMENT",))
        f.sc.admit(blocker)
        report_decision = coordinate(f.w())[blocker["id"]]
        index = f.w().binding_index()
        self.assertIn(part_decision.id, index)
        self.assertIn(report_decision.id, index)

    def test_n2_a_decision_owed_to_the_human_is_answered_only_by_one(self) -> None:
        sc = Scenario(MANIFEST, FILES)
        blocker = report("BLOCKER", ["arch"], reasons=("ENVIRONMENT",))
        sc.admit(blocker)
        self.assertEqual(coordinate(wf(sc))[blocker["id"]].holder, "HUMAN")
        sc.admit(judgment("COORDINATION_DECISION", {"records": [blocker["id"]]}, "DECLINE", actor=agent("anyone"),
                          actor_class="AGENT", fields={"tasks": []}))
        self.assertIn(blocker["id"], coordinate(wf(sc)), "§12.5: the human's decision")

    def test_n5_recurrence_raises_again_after_an_answer(self) -> None:
        f = Flow(budget=5)
        for n in (1, 2):
            f.submit(f"# Records {n}\n", outcome="PARTIAL", slots={"claims": []})
        (found,) = [o for o in f.w().of_kind("COORDINATE") if o.target.get("recurrence") == "template"]
        f.sc.admit(judgment("COORDINATION_DECISION", {"records": [found.id]}, "DECLINE", actor=PRINCIPAL,
                            actor_class="AGENT", fields={"tasks": []}))
        f.submit("# Records 3\n", outcome="PARTIAL", slots={"claims": []})
        again = [o for o in f.w().of_kind("COORDINATE") if o.target.get("recurrence") == "template"]
        self.assertEqual(len(again), 1, "a further failure after the answer is a new recurrence")
        self.assertNotEqual(again[0].id, found.id)


class Identity(unittest.TestCase):
    """N7: SD-52's fixed-field half and out(o) through an amendment."""

    def test_n7_a_fixed_field_change_derives_a_new_obligation(self) -> None:
        f = Flow()
        before = f.item().obligation.id
        changed = document_item().replace('affected = ["records.md"]', 'affected = ["records.md", "arch.md"]')
        self.assertNotEqual(changed, document_item())
        f.sc.absorb({"plans/work.md": changed})
        self.assertNotIn(before, {i.obligation.id for i in f.w().items.all})

    def test_n7_out_survives_a_tightening(self) -> None:
        f = Flow()
        x, cand = f.submit("# Records\nDocumented.\n")
        f.review(x, cand, "PASS")
        f.integrate(x, cand)
        outputs = dict(f.item().outputs)
        self.assertEqual(list(outputs), ["records"])
        f.sc.absorb({"plans/work.md": document_item(budget=2)})
        self.assertEqual(dict(f.item().outputs), outputs)


#: The SD-54 answer alphabet of ``lifecycle_properties``: (outcome, settled, actor).
KINDS = [("AMEND", True), ("AMEND", False), ("PARTITION", True), ("DECLINE", True), ("CHALLENGE", True),
         ("CHALLENGE", False), ("ESCALATE", True)]
ALPHABET = [(o, st, a) for o, st in KINDS for a in ("principal", "human")]
RECURRENCE = 3


def chains(k: int, alphabet=ALPHABET):
    for seq in itertools.product(alphabet, repeat=k):
        if any((not st) or o in ("PARTITION", "DECLINE") for o, st, _ in seq[:-1]):
            continue  # an earlier ending or unsettled answer derives no later decision to answer
        yield seq


class Lifecycle(unittest.TestCase):
    """Reading E15: P1-P6 over answer chains through the real owner, for the budget-spent and the
    item-level-no-part conditions (the kept fence is Phase F's)."""

    def start(self, condition: str):
        if condition == "budget-spent":
            f = PartFlow()
            f.spend(f.item().obligation)
        else:
            f = partitioned_and_worked()
            f.item_level("NO_PASS")
        return f

    def replay(self, condition: str, seq) -> list[str]:
        f = self.start(condition)

        def open_() -> list:
            return [o for o in f.item().route.decisions if o.target.get("condition") == condition]

        counted, answered, n = [], set(), 0
        for outcome, settled, who in seq:
            (d,) = open_() or [None]
            if d is None:
                return self.suspended(f, counted)
            actor = HUMAN if who == "human" else PRINCIPAL
            held = len(counted) >= RECURRENCE
            n += 1
            if outcome == "AMEND":
                rec, (x, cand) = f.decide(d, "AMEND", actor=actor, plan_change=self.amendment(f, n))
                if settled:
                    f.integrate(x, cand)
            elif outcome == "PARTITION":
                rec = f.partition(d, [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])], actor=actor)
            elif outcome == "PARTITION-ELSEWHERE":
                rec = self.partition_elsewhere(f, d, actor, n, held and who != "human")
            elif outcome == "PARTITION-REDONE":
                rec = self.partition_redone(f, d, actor, n, held and who != "human")
            elif outcome == "CHALLENGE":
                f.counter += 1
                cls = "HUMAN" if actor.startswith("human:") else "AGENT"
                rec = judgment("COORDINATION_DECISION", {"records": [d.id]}, "CHALLENGE", actor=actor, actor_class=cls,
                               binding=fresh(actor, f"coord-c{f.counter}"), fields={"tasks": []})
                raised = judgment("CHALLENGE", {"record": rec["id"]}, None, actor=actor, actor_class=cls,
                                  fields={"blocking": False, "serious": False, "inquiry": "CONFIRMATORY"})
                f.sc.admit(rec, raised)
                if settled:
                    f.sc.admit(adjudication(raised["id"], "DISMISSED"))
            else:
                rec, _ = f.decide(d, outcome, actor=actor)
            if not (outcome in ("ESCALATE", "DECLINE") or (outcome == "CHALLENGE" and not held) or (held and who != "human")):
                counted.append((rec["id"], outcome, settled))
                answered.add(d.id)
        item = f.item()
        route = item.route.route
        open_now = open_()
        problems = []
        if not route or (route.startswith(("COORDINATE", "human-attention")) and len(open_now) != 1):
            problems.append("P1")
        if {o.id for o in open_now} & answered:
            problems.append("P2")
        if route.startswith("awaiting-") and not (counted and route.endswith(":" + counted[-1][0]) and not counted[-1][2]):
            problems.append("P3")
        if condition == "budget-spent" and route in ("re-dispatch", "discharged", "dispatch"):
            problems.append("P4")
        if open_now:
            held = len(counted) >= RECURRENCE
            if (route.startswith("human-attention:") and open_now[0].holder == "HUMAN") != held:
                problems.append("P5")
            if open_now[0].target["after"] != (counted[-1][0] if counted else None):
                problems.append("P6")
        if counted and counted[-1][1] == "PARTITION" and not route.startswith("partitioned:") and condition == "budget-spent":
            problems.append("partition")
        problems += self.route4(f, counted)
        return problems

    @staticmethod
    def route4(f, counted) -> list[str]:
        """While a no-part condition holds the route opens its decision, or hands it to a ``PARTITION`` answering that
        chain whose parts the replay has not worked; a ready part never stands in for it, nor a partition whose work
        is done (§10.4; re-Review of 49bebf3, E-R3; same-family check of af327075, B-1 and B-2). The condition is read
        from the standing objections and the uncovered failing subjects, and the work done from the replay's own
        history, never from the route owner, so this oracle does not reuse the code it checks."""

        item = f.item()
        condition = any(not item._named_parts(r) for r in item._objections) or bool(item.uncovered_failing)
        if item.partition is None or not condition or item.discharge() != "OPEN":
            return []
        route = item.route.route
        if counted and counted[-1][1] == "PARTITION":  # an answer whose parts the replay never works
            return [] if route == f"partitioned:{counted[-1][0]}" else ["route4: the unworked partition lost the route"]
        if route.startswith(("COORDINATE:item-level-no-part", "human-attention:item-level-no-part", "awaiting-")):
            return []
        return ["route4: the no-part condition holds without its decision"]

    def suspended(self, f, counted) -> list[str]:
        return ["P1: no open decision to answer"]

    def amendment(self, f, n: int) -> dict[str, str]:
        return {"plans/work.md": plan(f"Adaptive solver, round {n}.\n")}

    def partition_redone(self, f, d, actor: str, n: int, uncounted: bool):
        raise NotImplementedError  # only the one-part seed redoes a partition's work and objects to it again

    def partition_elsewhere(self, f, d, actor: str, n: int, uncounted: bool):
        raise NotImplementedError  # only a condition a part cannot inherit has a partition that leaves it holding

    def test_every_chain_up_to_length_two_and_a_sample_of_length_four(self) -> None:
        rng = random.Random(20261022)
        for condition in ("budget-spent", "item-level-no-part"):
            sample = [s for k in range(3) for s in chains(k)] + rng.sample(list(chains(4)), 12)
            for seq in sample:
                with self.subTest(condition=condition, chain=seq):
                    self.assertEqual(self.replay(condition, seq), [])


class LifecycleOnePart(Lifecycle):
    """Reading E15 for the item-level-no-part condition on a one-part partition, where the objection itself reopens the
    part whose work it judged (re-Review of 49bebf3, E-R3)."""

    def start(self, condition: str):
        f = PartFlow()
        f.spend(f.item().obligation)
        f.partition(f.budget_decision(f.item()), [(["o1", "o2", "o3"], ["records", "notes.a", "notes.b"])])
        f.work_part(f.item().parts[0], {"records.md": "# Records done\n", "notes/a.md": "a done\n", "notes/b.md": "b done\n"})
        f.item_level("NO_PASS")
        assert f.item().route.route == "COORDINATE:item-level-no-part"
        return f

    ALPHABET = ALPHABET + [("PARTITION-REDONE", True, a) for a in ("principal", "human")]

    def partition_redone(self, f, d, actor: str, n: int, uncounted: bool):
        """A ``PARTITION`` into one part, that part's work done and its item-level review a NO-PASS naming no part
        again: the objection reopens the part, and the chain's next decision is owed (B-1)."""

        rec = f.partition(d, [(["o1", "o2", "o3"], ["records", "notes.a", "notes.b"])], actor=actor)
        if not uncounted:
            part = next(p for p in f.item().parts if p.share[0] == rec["id"])
            f.work_part(part, {"records.md": f"# Records, round {n}\n", "notes/a.md": f"a, round {n}\n",
                               "notes/b.md": f"b, round {n}\n"})
            f.item_level("NO_PASS")
        return rec

    def test_every_chain_up_to_length_two_and_a_sample_of_length_four(self) -> None:
        rng = random.Random(20261024)
        sample = [s for k in range(2) for s in chains(k, self.ALPHABET)]
        for k, size in ((2, 24), (3, 12), (4, 12)):  # the full enumeration is LifecycleOnePartFull
            sample += rng.sample(list(chains(k, self.ALPHABET)), size)
        for seq in sample:
            with self.subTest(chain=seq):
                self.assertEqual(self.replay("item-level-no-part", seq), [])


@unittest.skipUnless(os.environ.get("SSDS_SLOW"), "the named slow check of reading E15: set SSDS_SLOW=1")
class LifecycleOnePartFull(LifecycleOnePart):
    def test_every_chain_up_to_length_two_and_a_sample_of_length_four(self) -> None:
        pass

    def test_every_chain_up_to_length_four(self) -> None:
        bad = [(seq, problems) for k in range(5) for seq in chains(k, self.ALPHABET)
               if (problems := self.replay("item-level-no-part", seq))]
        self.assertEqual(bad, [])


@unittest.skipUnless(os.environ.get("SSDS_SLOW"), "the named slow check of reading E15: set SSDS_SLOW=1")
class LifecycleFull(Lifecycle):
    """Reading E15's full enumeration: every chain up to length 4 for both conditions, through the real owner."""

    def test_every_chain_up_to_length_two_and_a_sample_of_length_four(self) -> None:
        pass  # the sample is the suite's; this class runs the whole enumeration

    def test_every_chain_up_to_length_four(self) -> None:
        bad = []
        for condition in ("budget-spent", "item-level-no-part"):
            for k in range(5):
                for seq in chains(k):
                    problems = self.replay(condition, seq)
                    if problems:
                        bad.append((condition, seq, problems))
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
