"""Phase E step 5b: partition and the item-level review at the real derivation owner (catalogue §13.7, §10.4).

Carries the S3 item-level cases (``item_level_no_part``, ``item_level_amend_elsewhere_*``,
``item_level_recurrence_human_amend_integrated``, ``partitioned_all_good``), S5 §13
``repartition_keeps_discharged_parts``, and the discriminators 051cce3 N5 (a reopened part of a superseded
PARTITION), 51070e5 N3 (the §13.7 re-partition example) and 63ddf91 N5 / f03b15e N5 (a re-partition after a
discharged part). Expected values are the cases' stated outcomes.
"""

from __future__ import annotations

import hashlib
import json
import unittest

from ssds.ledger.read import with_id

from ._fixtures import record
from ._scenario import HUMAN, OWNER, Scenario, agent, content, fresh, judgment
from .test_lint import FILES, MANIFEST
from .test_routes import PRINCIPAL, SLOTS, Flow

BLOCK = '''item = "work"
kind = "DOCUMENT"
objective = { ref = "#item" }
affected = ["records.md", "notes/"]
[contract]
scientific = "NOT_APPLIES"
budget = 2
[contract.boundaries]
write_scope = ["records.md", "notes/"]
[[contract.obligations]]
id = "o1"
statement = { ref = "#o1" }
verifier = "REVIEW"
[[contract.obligations]]
id = "o2"
statement = { ref = "#o2" }
verifier = "REVIEW"
[[contract.obligations]]
id = "o3"
statement = { ref = "#o3" }
verifier = "REVIEW"
[contract.expectations]
slots = ["claims", "unverified_assumptions", "deviations"]
'''


#: Units for the note files, so their content has known authors once a task writes it (§5.10 (b)).
NOTES = '''
    [[unit]]
    id = "notes.a"
    kind = "EVIDENCE_RECORD"
    scope = [{ path = "notes/a.md" }]
    [[unit]]
    id = "notes.b"
    kind = "EVIDENCE_RECORD"
    scope = [{ path = "notes/b.md" }]
'''


def plan(objective: str = "Adaptive solver.\n") -> str:
    return (f"# Work\n\n## Objective\n\n{objective}\n## Item\n\nDocument the solver in three places.\n\n"
            "### o1\n\nThe records.\n\n### o2\n\nThe first note.\n\n### o3\n\nThe second note.\n\n"
            f"```ssds-item\n{BLOCK}```\n")


class PartFlow(Flow):
    def __init__(self) -> None:
        self.sc = Scenario(MANIFEST + NOTES, {**FILES, "plans/work.md": plan(), "notes/a.md": "a\n", "notes/b.md": "b\n"})
        self.accept_plan()
        self.counter = 0

    def spend(self, obligation, path: str = "records.md") -> None:
        """Two PARTIAL iterations of ``obligation`` (budget 2), writing within its share: its budget is then spent."""

        self.attempt(obligation, path)
        self.attempt(obligation, path)

    def attempt(self, obligation, path: str) -> None:
        self.counter += 1
        task = f"task-{self.counter}"
        base, cand, x, _ = self._candidate({path: f"# attempt {self.counter}\n"})
        result = record("TASK_RESULT", target={"task": task, "candidate": cand, "transformation": x, "base": base},
                        outcome="PARTIAL", actor=agent("maker"), actor_class="AGENT", frame={"transformation": x},
                        fields={"slots": SLOTS})
        result["binding"] = dict(fresh(agent("maker"), task), obligation=obligation.id,
                                 item={"unit": "plan.work.item", "rev": self.sc.rev("plan.work.item")})
        self.sc.admit(with_id(result))

    def partition(self, decision, parts: list[tuple[list[str], list[str]]], actor: str = PRINCIPAL) -> dict:
        self.counter += 1
        spec = json.dumps({"parts": [{"obligations": o, "write_scope": w} for o, w in parts], "order": []},
                          sort_keys=True).encode()
        digest = "sha256:" + hashlib.sha256(spec).hexdigest()
        rec = record("COORDINATION_DECISION", target={"records": [decision.id]}, outcome="PARTITION", actor=actor,
                     actor_class="HUMAN" if actor.startswith("human:") else "AGENT", fields={"tasks": []})
        rec["binding"] = fresh(actor, f"coord-{self.counter}")
        rec["refs"] = [{"store": "LEDGER", "digest": digest, "media_type": "application/json"}]
        rec = with_id(rec)
        self.sc.objects[self.sc.position] = {digest: spec}
        self.sc.admit(rec)
        return rec

    def work_part(self, part, files: dict[str, str], keyed: bool = True) -> tuple[str, str]:
        """A part's task: a clean candidate, an independent passing review, integration (``keyed``: its binding
        carries the item's work key)."""

        self.counter += 1
        task = f"part-{self.counter}"
        base, cand, x, _ = self._candidate(files)
        result = record("TASK_RESULT", target={"task": task, "candidate": cand, "transformation": x, "base": base},
                        outcome="COMPLETE", actor=agent("maker"), actor_class="AGENT", frame={"transformation": x},
                        fields={"slots": SLOTS})
        result["binding"] = dict(fresh(agent("maker"), task), obligation=part.obligation.id,
                                 **({"item_key": part.key} if keyed else {}), write_scope=list(part.share[3]),
                                 item={"unit": "plan.work.item", "rev": self.sc.rev("plan.work.item")})
        self.sc.admit(with_id(result))
        self.review(x, cand, "PASS")
        self.integrate(x, cand)
        return x, cand

    def item_level(self, outcome: str, findings=None, actor: str = agent("integrator")) -> dict:
        item = self.item()
        target = item.item_level_target
        self.counter += 1
        task = f"il-{self.counter}"
        verdict = judgment("REVIEW", target, outcome, actor=actor, actor_class="HUMAN" if actor.startswith("human:") else "AGENT",
                           basis=[content("records", self.sc.rev("records"))], binding=fresh(actor, task))
        result = record("TASK_RESULT", target={"task": task}, outcome="COMPLETE", actor=actor, actor_class="AGENT",
                        fields={"slots": {"claims": [], "findings": findings if findings is not None else {"none": "NONE_FOUND"}}})
        result["binding"] = fresh(actor, task)
        self.sc.admit(verdict, with_id(result))
        return verdict

    def budget_decision(self, holder):
        (d,) = [o for o in holder.route.decisions if o.target.get("condition") == "budget-spent"]
        return d


def partitioned_and_worked() -> PartFlow:
    f = PartFlow()
    f.spend(f.item().obligation)
    f.partition(f.budget_decision(f.item()), [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
    item = f.item()
    a, b = item.parts
    f.work_part(a, {"records.md": "# Records done\n"})
    f.work_part(f.item().parts[1], {"notes/a.md": "a done\n", "notes/b.md": "b done\n"})
    del b
    return f


class Partition(unittest.TestCase):
    def test_partition_hands_the_route_to_the_parts(self) -> None:
        f = PartFlow()
        f.spend(f.item().obligation)
        f.partition(f.budget_decision(f.item()), [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
        item = f.item()
        self.assertEqual(len(item.parts), 2)
        self.assertTrue(item.route.route.startswith("partitioned:"), "budget_partitioned_after_answer")
        self.assertEqual([p.route.route for p in item.parts], ["dispatch", "dispatch"])

    def test_an_invalid_partition_answers_nothing(self) -> None:
        f = PartFlow()
        f.spend(f.item().obligation)
        f.partition(f.budget_decision(f.item()), [(["o1"], ["records"]), (["o1", "o2"], ["notes.a", "notes.b"])])
        self.assertEqual(f.item().parts, ())

    def test_partitioned_all_good(self) -> None:
        f = partitioned_and_worked()
        self.assertEqual(f.route(), "item-level-review", "every part discharged; the item-level review is owed")
        self.assertEqual(len(f.w().of_kind("REVIEW")), 1)
        f.item_level("PASS")
        self.assertEqual(f.route(), "discharged", "partitioned_all_good")

    def test_item_level_no_part_and_its_chain(self) -> None:
        f = partitioned_and_worked()
        f.item_level("NO_PASS")
        self.assertEqual(f.route(), "COORDINATE:item-level-no-part", "item_level_no_part")
        (d,) = [o for o in f.item().route.decisions if o.target.get("condition") == "item-level-no-part"]
        self.assertIsNone(d.target["after"])
        answer, (x, cand) = f.decide(d, "AMEND", plan_change={"plans/work.md": plan("Adaptive solver, again.\n")})
        self.assertEqual(f.route(), f"awaiting-amendment:{answer['id']}", "item_level_amend_elsewhere_waits")
        f.integrate(x, cand)
        self.assertEqual(f.route(), "COORDINATE:item-level-no-part", "item_level_amend_elsewhere_integrated")

    def test_item_level_recurrence_human_amend_integrated(self) -> None:
        f = partitioned_and_worked()
        f.item_level("NO_PASS")
        for n in range(3):
            (d,) = [o for o in f.item().route.decisions if o.target.get("condition") == "item-level-no-part"]
            _, (x, cand) = f.decide(d, "AMEND", plan_change={"plans/work.md": plan(f"Adaptive solver {n}.\n")})
            f.integrate(x, cand)
        (held,) = [o for o in f.item().route.decisions if o.target.get("condition") == "item-level-no-part"]
        self.assertEqual(held.holder, "HUMAN")
        answer, (x, cand) = f.decide(held, "AMEND", actor=HUMAN, plan_change={"plans/work.md": plan("Adaptive solver 9.\n")})
        f.integrate(x, cand)
        self.assertEqual(f.route(), "human-attention:item-level-no-part")
        (next_,) = [o for o in f.item().route.decisions if o.target.get("condition") == "item-level-no-part"]
        self.assertEqual(next_.target["after"], answer["id"])

    def test_an_item_level_objection_naming_a_part_reopens_that_part(self) -> None:
        f = partitioned_and_worked()
        f.item_level("NO_PASS", findings=[{"part": 0, "units": ["records"]}])
        item = f.item()
        self.assertEqual([p.discharge() for p in item.parts], ["OPEN", "DISCHARGED"])
        self.assertTrue(item.route.route.startswith("partitioned:"))


class Repartition(unittest.TestCase):
    def test_the_repartition_example(self) -> None:
        # §13.7's example (51070e5 N3; S5 §13 repartition_keeps_discharged_parts; 63ddf91 N5, f03b15e N5):
        # P1 = a (integrated), b (budget spent); P2 re-partitions b into b1, b2; required = a, b1, b2.
        f = PartFlow()
        f.spend(f.item().obligation)
        f.partition(f.budget_decision(f.item()), [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
        f.work_part(f.item().parts[0], {"records.md": "# Records done\n"})
        b = f.item().parts[1]
        f.spend(b.obligation, "notes/a.md")
        f.partition(f.budget_decision(f.item().parts[1]), [(["o2"], ["notes.a"]), (["o3"], ["notes.b"])])
        item = f.item()
        shares = sorted(tuple(sorted(p.share[2])) for p in item.parts)
        self.assertEqual(shares, [("o1",), ("o2",), ("o3",)], "a stays required; b is replaced by b1 and b2")
        self.assertNotIn(b.obligation.id, [p.obligation.id for p in item.parts], "b is never required again")
        # 051cce3 N5: a later change moves a's outputs: a reopens, still a required part of the item, ready again
        f.sc.absorb({"records.md": "# Records changed by someone else\n"})
        a = next(p for p in f.item().parts if p.share[2] == frozenset({"o1"}))
        self.assertEqual((a.discharge(), a.route.route, a.moved), ("OPEN", "re-dispatch", True))


if __name__ == "__main__":
    unittest.main()
