"""Phase E step 3c: obligations, answering, readiness and discharge at the derivation owner (catalogue §10.2-§10.5).

Expected values are written from the catalogue's trigger table, answering rule, discharge predicate and
provisional scope, never computed by the rule under test.
"""

from __future__ import annotations

import unittest

from ssds.derivation import F, P, T
from ssds.derivation.workflow import (
    ANSWERED,
    DISCHARGED,
    DISCHARGED_PROVISIONAL,
    HUMAN as HUMAN_ROLE,
    OPEN,
    READY,
    REFUSED,
    WAITING,
    Workflow,
)

from ._scenario import HUMAN, HUMAN_B, OWNER, Scenario, challenge, content, judgment, on_record
from .test_lint import FILES as PLAN_FILES, MANIFEST as PLAN_MANIFEST, item_block, plan_text
from .test_runs import MANIFEST as RUN_MANIFEST, author

TWO = '''
    [[unit]]
    id = "arch"
    kind = "D3"
    scope = [{ path = "arch.md" }]
    [[unit]]
    id = "impl"
    kind = "D4"
    scope = [{ path = "impl.md" }]
    [[unit]]
    id = "spec"
    kind = "EVIDENCE_SPEC"
    scope = [{ path = "spec.toml" }]
    [unit.semantic]
    joint_invariants = [{ id = "arch-impl", units = ["arch", "impl"] }]
'''
HUMANS = 'schema = 1\n[domains.D3]\nhumans = ["human:SHA256:alice", "human:SHA256:bob"]\n'


def wf(sc: Scenario) -> Workflow:
    return Workflow(sc.derive())


def kinds(w: Workflow) -> dict[str, list]:
    out: dict[str, list] = {}
    for o in w.obligations:
        out.setdefault(o.kind, []).append(o)
    return out


def accept(sc: Scenario, subject: str, actor: str = HUMAN, basis=None) -> dict:
    t = sc.triple(subject)
    return judgment("ACCEPTANCE", t, "PASS", actor=actor, basis=basis or [content(subject, t["rev"])])


class Identity(unittest.TestCase):
    def test_deterministic_and_keyed_by_target(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        first = {o.id for o in wf(sc).of_kind("ACCEPT")}
        self.assertEqual(first, {o.id for o in wf(sc).of_kind("ACCEPT")})
        sc.absorb({"arch.md": "a2\n"})
        second = {o.id for o in wf(sc).of_kind("ACCEPT")}
        self.assertEqual(len(first & second), 2, "impl's and spec's targets are unchanged; arch's revision is new")

    def test_a_new_run_derives_a_new_obligation(self) -> None:
        # §10.2: ACCEPT, GATE and REVIEW(s, r) carry the run, so a revert derives new obligations
        sc = Scenario(RUN_MANIFEST, {"numerics.md": "v0\n", "notes.md": "n\n"},
                      policy='schema = 1\n[domains.D2]\nhumans = ["human:SHA256:alice"]\n')
        author(sc, "v1\n", "task-1")
        first = {o.id for o in wf(sc).of_kind("ACCEPT")}
        author(sc, "v2\n", "task-2")
        author(sc, "v1\n", "task-3")
        again = {o.id for o in wf(sc).of_kind("ACCEPT")}
        self.assertEqual(len(first & again), 1, "notes (D3, no run) keeps its identity; numerics' run is new")


class SubjectObligations(unittest.TestCase):
    def test_accept_derived_ready_answered_and_gone(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        w = wf(sc)
        arch = [o for o in w.of_kind("ACCEPT") if o.target["subject"] == "arch"][0]
        self.assertEqual(arch.holder, "REVIEWER")
        self.assertEqual(w.readiness(arch).state, READY, "a named human outside the (unknown) authors may answer")
        sc.admit(accept(sc, "arch"))
        self.assertNotIn("arch", [o.target["subject"] for o in wf(sc).of_kind("ACCEPT")])

    def test_no_eligible_judge_waits(self) -> None:
        # Genesis content has unknown authors (§5.10 (b)): no agent is independent of it, and policy names no human.
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"})
        w = wf(sc)
        arch = [o for o in w.of_kind("ACCEPT") if o.target["subject"] == "arch"][0]
        self.assertEqual(w.readiness(arch), w.readiness(arch).__class__(WAITING, ("no eligible judge",)))

    def test_a_non_current_answer_is_revalidated(self) -> None:
        # 8f4e75d N4 (group 6, the judgment half): a non-current judgment a current obligation depends on has a route.
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        premise = accept(sc, "impl", actor=HUMAN_B)
        sc.admit(premise)
        decision = accept(sc, "arch", basis=[content("arch", sc.rev("arch")), on_record(premise["id"])])
        sc.admit(decision)
        self.assertEqual(sc.derive().current(decision["id"]), T)
        sc.admit(challenge({"record": premise["id"]}))
        w = wf(sc)
        self.assertEqual(w.d.current(decision["id"]), F)
        arch = [o for o in w.of_kind("ACCEPT") if o.target["subject"] == "arch"][0]
        self.assertEqual((w.readiness(arch).state, w.discharge(arch)), (ANSWERED, OPEN))
        revalidations = [o for o in w.of_kind("REVALIDATE") if o.target["record"] == decision["id"]]
        self.assertEqual(len(revalidations), 1)
        self.assertEqual(w.readiness(revalidations[0]).state, READY)

    def test_quarantined_structure_waits(self) -> None:
        # §10.3: an answer's mechanical minimum cannot hold over quarantined structure (§1.6), so ACCEPT waits.
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        sc.manifest = TWO.replace('scope = [{ path = "arch.md" }]', 'scope = [{ path = "arch.md" }, { path = "extra.md" }]')
        sc.absorb({"extra.md": "x\n"})
        w = wf(sc)
        self.assertIn("arch", w.s.s0.affected_subjects)
        (arch,) = [o for o in w.of_kind("ACCEPT") if o.target["subject"] == "arch"]
        self.assertEqual(w.readiness(arch).state, WAITING)

    def test_d2_accept_waits_on_the_revising_review(self) -> None:
        sc = Scenario(RUN_MANIFEST, {"numerics.md": "v0\n", "notes.md": "n\n"},
                      policy='schema = 1\n[domains.D2]\nhumans = ["human:SHA256:alice"]\n')
        w = wf(sc)
        accept_o = [o for o in w.of_kind("ACCEPT") if o.target["subject"] == "numerics"][0]
        self.assertEqual(accept_o.holder, HUMAN_ROLE, "D1/D2 acceptance is R3 by domain")
        self.assertEqual(w.readiness(accept_o).state, WAITING)
        self.assertTrue(any(o.target["subject"] == "numerics" for o in w.of_kind("REVIEW_REVISION")))
        author(sc, "v1\n", "task-1")
        w = wf(sc)
        self.assertFalse(any(o.target["subject"] == "numerics" for o in w.of_kind("REVIEW_REVISION")),
                         "a counting revision-assessment record answers REVIEW(s, r)")
        accept_o = [o for o in w.of_kind("ACCEPT") if o.target["subject"] == "numerics"][0]
        self.assertEqual(w.readiness(accept_o).state, READY)

    def test_gate_derived_for_a_required_gate_and_waits_without_holders(self) -> None:
        policy = 'schema = 1\n[domains.D3]\ngates = ["g"]\nhumans = ["human:SHA256:alice"]\n'
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=policy)
        gate = wf(sc).of_kind("GATE")[0]
        self.assertEqual((gate.holder, wf(sc).readiness(gate).state), (HUMAN_ROLE, WAITING))
        sc2 = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"},
                       policy=policy + 'gate_holders = ["human:SHA256:alice"]\n')
        self.assertEqual(wf(sc2).readiness(wf(sc2).of_kind("GATE")[0]).state, READY)


class Answering(unittest.TestCase):
    def test_a_non_independent_pass_does_not_answer(self) -> None:
        # §10.3: a passing judgment with nonind does not answer an obligation whose discharge requires independence
        from ._scenario import agent, fresh

        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        sc.integrate({"impl.md": "i2\n"}, agent("maker"), "task-1")
        w = wf(sc)
        (impl,) = [o for o in w.of_kind("ACCEPT") if o.target["subject"] == "impl"]
        own = judgment("ACCEPTANCE", sc.triple("impl"), "PASS", actor=agent("maker"), actor_class="AGENT",
                       basis=[content("impl", sc.rev("impl"))], binding=dict(fresh(agent("maker"), "task-2"), obligation=impl.id))
        sc.admit(own)
        w = wf(sc)
        self.assertTrue(w.d.j.nonind(own["id"]))
        self.assertIsNone(w.answer(impl))
        self.assertEqual(w.readiness(impl).state, READY, "it stays dispatchable to an independent judge")
        other = judgment("ACCEPTANCE", sc.triple("impl"), "PASS", actor=agent("checker"), actor_class="AGENT",
                         basis=[content("impl", sc.rev("impl"))], binding=dict(fresh(agent("checker"), "task-3"), obligation=impl.id))
        sc.admit(other)
        self.assertNotIn(impl.id, {o.id for o in wf(sc).obligations})

    def test_an_earlier_runs_acceptance_answers_nothing_in_a_new_run(self) -> None:
        from .test_runs import accept as run_accept

        sc = Scenario(RUN_MANIFEST, {"numerics.md": "v0\n", "notes.md": "n\n"},
                      policy='schema = 1\n[domains.D2]\nhumans = ["human:SHA256:alice"]\n')
        r1 = author(sc, "v1\n", "task-1")
        sc.admit(run_accept(sc, r1["id"]))
        author(sc, "v2\n", "task-2")
        author(sc, "v1\n", "task-3")
        w = wf(sc)
        (numerics,) = [o for o in w.of_kind("ACCEPT") if o.target["subject"] == "numerics"]
        self.assertIsNone(w.answer(numerics))
        self.assertEqual(w.readiness(numerics).state, READY)


class ChallengeAndDisagreement(unittest.TestCase):
    def test_adjudicate_an_open_challenge(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        acc = accept(sc, "arch")
        sc.admit(acc)
        c = challenge({"record": acc["id"]})
        sc.admit(c)
        self.assertEqual([o.target for o in wf(sc).of_kind("ADJUDICATE")], [{"record": c["id"]}])
        sc.admit(judgment("ADJUDICATION", {"record": c["id"]}, "DISMISSED", actor=OWNER))
        self.assertEqual(wf(sc).of_kind("ADJUDICATE"), [])

    def test_a_standing_veto_derives_the_owners_adjudication(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"},
                      policy='schema = 1\n[domains.D3]\nowner = "human:SHA256:owner"\n')
        passing = accept(sc, "arch", actor=HUMAN)
        sc.admit(passing)
        adverse = judgment("ACCEPTANCE", sc.triple("arch"), "FAIL", actor=HUMAN_B, basis=[content("arch", sc.rev("arch"))])
        sc.admit(adverse)
        w = wf(sc)
        found = [o for o in w.of_kind("ADJUDICATE_DISAGREEMENT") if o.target == {"record": adverse["id"]}]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].params, {"vetoes": passing["id"]})
        self.assertEqual(w.readiness(found[0]).state, READY, "the owner may supersede or relieve")


class SpecAndInvariant(unittest.TestCase):
    def test_spec_review_and_joint_invariant_follow_changes(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        w = wf(sc)
        self.assertEqual((w.of_kind("SPEC_REVIEW"), w.of_kind("JOINT_INVARIANT")), ([], []), "nothing changed")
        sc.absorb({"spec.toml": "s2\n"})
        w = wf(sc)
        self.assertEqual([o.target["subject"] for o in w.of_kind("SPEC_REVIEW")], ["spec"])
        self.assertEqual(w.of_kind("JOINT_INVARIANT"), [], "the change does not touch the invariant's scope")
        sc.absorb({"impl.md": "i2\n"})
        first = wf(sc).of_kind("JOINT_INVARIANT")
        self.assertEqual([o.target["invariant"] for o in first], ["arch-impl"])
        sc.absorb({"arch.md": "a2\n"})
        later = wf(sc).of_kind("JOINT_INVARIANT")
        self.assertNotEqual(first[0].id, later[0].id, "a later change in scope derives JOINT_INVARIANT(i, k')")


class Discharge(unittest.TestCase):
    def provisional(self, policy: str, kinds: list[str]) -> str:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=policy)
        acc = accept(sc, "arch")
        sc.admit(acc)
        c = challenge({"record": acc["id"]})
        sc.admit(c)
        sc.admit(judgment("RISK_OVERRIDE", {"record": c["id"]}, None, actor=OWNER,
                          fields={"continuation": {"subjects": ["arch"], "items": [], "kinds": kinds}}))
        w = wf(sc)
        self.assertEqual(w.d.current(acc["id"]), P)
        from ssds.derivation.workflow import make

        o = make("ACCEPT", sc.triple("arch"))
        derived = any(x.id == o.id for x in w.of_kind("ACCEPT"))
        self.assertEqual(derived, w.discharge(o) == OPEN, "outside the scope the obligation stays derived and open")
        return w.discharge(o)

    def test_provisional_only_inside_a_declared_scope(self) -> None:
        self.assertEqual(self.provisional(HUMANS, []), OPEN, "an override with no kinds discharges nothing provisionally")
        self.assertEqual(self.provisional(HUMANS, ["ACCEPT"]), DISCHARGED_PROVISIONAL)
        self.assertEqual(self.provisional(HUMANS + '[workflow]\nprovisional_kinds = ["ACCEPT"]\n', []), DISCHARGED_PROVISIONAL)

    def test_never_for_gates(self) -> None:
        from ssds.derivation.workflow import make

        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        w = wf(sc)
        gate = make("GATE", {"gate": "g", "subject": sc.triple("arch")})
        self.assertFalse(w.provisional_allowed(gate, "arch"))

    def test_discharged_and_refused(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        from ssds.derivation.workflow import make

        o = make("ACCEPT", sc.triple("arch"))
        sc.admit(accept(sc, "arch"))
        self.assertEqual(wf(sc).discharge(o), DISCHARGED)
        sc2 = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        sc2.admit(judgment("ACCEPTANCE", sc2.triple("arch"), "FAIL", actor=HUMAN, basis=[content("arch", sc2.rev("arch"))]))
        self.assertEqual(wf(sc2).discharge(o), REFUSED)


class PlanObligations(unittest.TestCase):
    def plan(self, block: str) -> Scenario:
        return Scenario(PLAN_MANIFEST, {**PLAN_FILES, "plans/work.md": plan_text(block)},
                        policy='schema = 1\n[domains.plan]\nhumans = ["human:SHA256:alice"]\n')

    def acceptance(self, sc: Scenario) -> dict:
        objective, item = sc.rev("plan.work.objective"), sc.rev("plan.work.item")
        return judgment("PLAN_ACCEPTANCE", {"units": ["plan.work"]}, "ACCEPTED", actor=OWNER,
                        basis=[content("plan.work.objective", objective), content("plan.work.item", item, "PLAN_CONTROL")],
                        fields={"objective": {"unit": "plan.work.objective", "rev": objective},
                                "items": [{"unit": "plan.work.item", "rev": item}]})

    def test_plan_accept_then_issuable(self) -> None:
        sc = self.plan(item_block())
        w = wf(sc)
        (pa,) = w.of_kind("PLAN_ACCEPT")
        self.assertEqual((pa.plan, w.readiness(pa).state), ("plan.work", READY))
        self.assertFalse(w.issuable("plan.work.item"))
        sc.admit(self.acceptance(sc))
        w = wf(sc)
        self.assertEqual((w.of_kind("PLAN_ACCEPT"), w.of_kind("CONTRACT")), ([], []))
        self.assertTrue(w.issuable("plan.work.item"))
        sc.absorb({"plans/work.md": plan_text(item_block(write_scope='["src/solver.py"]'))})
        self.assertTrue(wf(sc).issuable("plan.work.item"), "an R1 tightening keeps it issuable")
        sc.absorb({"plans/work.md": plan_text(item_block(budget=5))})
        w = wf(sc)
        self.assertFalse(w.issuable("plan.work.item"), "an R2 amendment waits for a new plan acceptance")
        self.assertEqual(len(w.of_kind("PLAN_ACCEPT")), 1)

    def test_contract_owed_and_lint_waits(self) -> None:
        sc = self.plan(item_block(budget=11))
        w = wf(sc)
        (pa,) = w.of_kind("PLAN_ACCEPT")
        self.assertEqual(w.readiness(pa).state, WAITING, "a plan failing lint waits on its principal")
        sc.admit(self.acceptance(sc))
        w = wf(sc)
        self.assertEqual([o.target["item"] for o in w.of_kind("CONTRACT")], ["plan.work.item"])
        self.assertFalse(w.issuable("plan.work.item"))


if __name__ == "__main__":
    unittest.main()
