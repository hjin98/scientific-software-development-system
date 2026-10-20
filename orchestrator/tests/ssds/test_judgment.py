"""Acceptance group 3 (derivation half): judged content, reach, relief and ending routes (Manual §5.10).

Expected values are transcribed by hand from ``cases.py`` (S1: item-level and
objection cases) and ``cases_s2.py`` (S2: transformation, binding, target and
route cases, and ``G1_QUESTIONS`` under amendment A1), each named per test.
The model histories become real ledger histories: an enactment is an agent's
integrated candidate whose binding carries its item key and write scope; an
author's name becomes that execution's actor.

Route labels: ``1``-``4`` are §5.10 (e)'s routes; a failing assessment's owner
disposition by ``IMMATERIALITY`` (§6.7) is ``immateriality-by-owner``, which
the S1 model lists as the owner's per-target route.
"""

from __future__ import annotations

import hashlib
import unittest

from ssds.derivation.judgment import Judgments, RouteEligibility
from ssds.derivation.frames import frame_state
from ssds.derivation.support import Support

from ._scenario import Scenario, agent, content, integrate, judgment, on_record, submit

UNITS = "".join(f'''
    [[unit]]
    id = "{u}"
    kind = "D4"
    scope = [{{ path = "{u}.md" }}]
''' for u in ("u", "v", "w", "x", "z")) + '''
    [[unit]]
    id = "plan"
    kind = "PLAN"
    scope = [{ path = "plan.md" }]
'''
FILES = {f"{u}.md": f"{u}0\n" for u in ("u", "v", "w", "x", "z")} | {"plan.md": "item k\n"}


def key(name: str | None) -> str | None:
    return None if name is None else "sha256:" + hashlib.sha256(name.encode()).hexdigest()


def actor(name: str) -> str:
    return f"human:SHA256:{name}" if name in ("H", "O", "R") else agent(name)


class History:
    """Enactments as real integrations."""

    def __init__(self, policy: str | None = None) -> None:
        self.sc = Scenario(UNITS, FILES, policy=policy)
        self.count = 0

    def enact(self, owner: str, item: str | None, delta: dict[str, int], author: str, scope=None) -> str | None:
        self.count += 1
        if not delta:
            return None
        files = {f"{u}.md": f"{u}{value}\n" for u, value in delta.items()}
        extra = {"write_scope": sorted(scope or delta)}
        if item is not None:
            extra["item_key"] = key(item)
        x, _ = self.sc.integrate(files, actor(author), f"{owner}-{self.count}", lineage=[actor(author)], binding_extra=extra)
        return x

    def candidate(self, delta: dict[str, int], author: str, item: str, scope, task: str = "t1") -> str:
        files = {f"{u}.md": f"{u}{value}\n" for u, value in delta.items()}
        x, c, result = submit(self.sc, files, actor(author), task)
        result["binding"].update({"write_scope": sorted(scope), "item_key": key(item), "lineage": [actor(author)]})
        from ssds.ledger.read import with_id

        fixed = with_id(result)
        self.sc.entries[-1]["records"] = [fixed]
        return x

    def derive(self):
        return self.sc.derive()


SCOPE = ["u", "v", "w"]


class ItemLevelJudgedContent(unittest.TestCase):
    """cases.py ITEM_CASES: the authors of an item-level review's judged content (RR-1)."""

    CASES = {
        "first_only": ([("a", "k", {"u": 1}, "A"), ("b", "k", {"w": 9}, "D")], {"A", "D"}),
        "empty_redispatch": ([("a", "k", {"u": 1}, "A"), ("b", "k", {"w": 9}, "D"), ("a", "k", {}, "Q")], {"A", "D"}),
        "partial_redispatch": ([("a", "k", {"u": 1}, "A"), ("b", "k", {"w": 9}, "D"), ("a", "k", {"v": 1}, "C")],
                               {"A", "C", "D"}),
        "all_empty": ([("a", "k", {"u": 1}, "A"), ("b", "k", {"w": 9}, "D"), ("a", "k", {}, "Q"), ("b", "k", {}, "R")],
                      {"A", "D"}),
        "repaired": ([("a", "k", {"u": 1}, "A"), ("b", "k", {"w": 9}, "D"), ("a", "k", {"u": 2}, "B")], {"B", "D"}),
        "kept_part_repartition": ([("a", "k", {"u": 1}, "A"), ("b1", "k", {"w": 9}, "D"), ("a", "k", {}, "Q")],
                                  {"A", "D"}),
        "replaced_part": ([("a", "k", {"u": 1}, "A"), ("b", "k", {"w": 9}, "D"), ("b1", "k", {}, "R")], {"A", "D"}),
        "copy_empty": ([("src", "k", {"u": 1}, "A"), ("a", "k", {}, "Q"), ("b", "k", {"w": 9}, "D")], {"A", "D"}),
        "same_key_other_scope": ([("tmpl", "k", {"x": 3}, "F"), ("a", "k", {"u": 1}, "A"), ("b", "k", {"w": 9}, "D")],
                                 {"A", "D"}),
        "foreign_then_drift": ([("a", "k", {"u": 1}, "A"), ("b", "k", {"w": 9}, "D"), ("foreign", None, {"u": 3}, "G"),
                                ("a", "k", {}, "Q")], {"G", "D"}),
        "other_item_in_scope": ([("other", "j", {"v": 7}, "H"), ("a", "k", {"u": 1}, "A"), ("b", "k", {"w": 9}, "D")],
                                {"A", "D"}),
    }

    def test_each_case(self) -> None:
        for name, (enactments, excluded) in self.CASES.items():
            with self.subTest(name):
                h = History()
                for owner, item, delta, author in enactments:
                    h.enact(owner, item, delta, author)
                n = h.sc.position
                review = judgment("REVIEW", {"integrated": "ITEM", "of": key("k"), "at": f"sha256:{n - 1:064x}",
                                             "changes": [], "scope": SCOPE}, "PASS", actor="human:SHA256:reviewer")
                h.sc.admit(review)
                j = h.derive().j
                self.assertEqual(j.work_authors(review["id"]), frozenset(actor(a) for a in excluded))


class TransformationJudgedContent(unittest.TestCase):
    """cases_s2.py TX_CASES: W of a transformation at issue, and whether a review supports the integration (RR-2)."""

    CASES = {
        "first_enactment": ([], [], {"u": 1}, "A", {"A"}, True),
        "retained_in_scope": ([("a", "k", {"u": 1}, "A")], [], {}, "Q", {"A"}, True),
        "same_key_other_scope_before_issue": ([("a", "k", {"u": 1}, "A"), ("tmpl", "k", {"x": 3}, "F")], [], {}, "Q",
                                              {"A"}, True),
        "same_key_other_scope_after_issue": ([("a", "k", {"u": 1}, "A")], [("tmpl", "k", {"x": 4}, "F")], {"v": 1}, "C",
                                             {"A", "C"}, True),
        "same_key_in_scope_after_issue": ([("a", "k", {"u": 1}, "A")], [("copy", "k", {"u": 2}, "B")], {"v": 1}, "C",
                                          {"A", "C"}, False),
        "foreign_in_scope_after_issue": ([("a", "k", {"u": 1}, "A")], [("foreign", None, {"u": 3}, "G")], {"v": 1}, "C",
                                         {"A", "C"}, False),
        "unrelated_after_issue": ([("a", "k", {"u": 1}, "A")], [("foreign", None, {"z": 5}, "G")], {"v": 1}, "C",
                                  {"A", "C"}, True),
    }

    def test_each_case(self) -> None:
        for name, (issue, later, delta, author, excluded, supported) in self.CASES.items():
            with self.subTest(name):
                h = History()
                for owner, item, d, a in issue:
                    h.enact(owner, item, d, a)
                x = h.candidate(delta, author, "k", ["u", "v"])
                review = judgment("REVIEW", {"transformation": x}, "PASS", actor="human:SHA256:reviewer",
                                  frame={"transformation": x})
                h.sc.admit(review)
                for owner, item, d, a in later:
                    h.enact(owner, item, d, a)
                j = h.derive().j
                self.assertEqual(j.work_authors(review["id"]), frozenset(actor(a) for a in excluded))
                self.assertEqual(j.supports_integration(review["id"], h.sc.position - 1), supported)


class Binding(unittest.TestCase):
    """cases_s2.py BIND_CASES: one producing context per (B, C, A)."""

    def test_each_case(self) -> None:
        cases = {"same_context_joins": (["u", "v"], "k", False), "different_scope_refused": (["v", "w"], "k", True),
                 "different_key_refused": (["u", "v"], "k2", True)}
        for name, (scope, item, conflict) in cases.items():
            with self.subTest(name):
                h = History()
                h.enact("a", "k", {"u": 1}, "A")
                x = h.candidate({"v": 1}, "C", "k", ["u", "v"], task="t1")
                again = h.candidate({"v": 1}, "C", item, scope, task="t2")
                self.assertEqual(again, x, "one (B, C, A), one transformation identity")
                d = h.derive()
                self.assertEqual(d.s.enactment(x), "t1", "the first result fixes the enactment")
                self.assertEqual(d.j.binding_conflicts(x), conflict)


class TypedTargets(unittest.TestCase):
    """cases_s2.py TARGET_CASES: three disjoint review target types; relief stays on its exact target (RR-3)."""

    def setUp(self) -> None:
        self.h = History(policy='schema = 1\n[domains.D4]\nowner = "human:SHA256:O"\n')
        self.h.enact("a", "k", {"u": 1}, "A")
        self.x = self.h.candidate({"v": 1}, "C", "k", ["u", "v"])
        self.joint = {"integrated": "JOINT_INVARIANT", "of": "inv1", "at": f"sha256:{self.h.sc.position - 1:064x}",
                      "changes": [self.x], "scope": ["u", "v"]}

    def test_a_joint_invariant_or_high_consequence_review_is_not_a_review_of_x(self) -> None:
        own = judgment("REVIEW", {"transformation": self.x}, "PASS", actor=agent("P"), frame={"transformation": self.x})
        joint = judgment("REVIEW", self.joint, "NO_PASS", actor=agent("N"))
        surface = judgment("REVIEW", {**self.joint, "integrated": "HIGH_CONSEQUENCE", "of": "surf1"}, "NO_PASS", actor=agent("N"))
        self.h.sc.admit(own, joint, surface)
        j = self.h.derive().j
        self.assertNotEqual(own["target"], joint["target"])
        self.assertFalse(j.same(joint["id"], own["id"]), "an integrated-result objection does not reach X's own review")
        self.assertFalse(j.same(surface["id"], own["id"]))

    def test_relief_stays_on_its_target(self) -> None:
        objection = judgment("REVIEW", {"transformation": self.x}, "NO_PASS", actor=agent("N"), frame={"transformation": self.x})
        vetoed = judgment("REVIEW", {"transformation": self.x}, "PASS", actor=agent("P"), frame={"transformation": self.x})
        other_target = judgment("REVIEW", self.joint, "PASS", actor="human:SHA256:O")
        self.h.sc.admit(objection, vetoed, other_target)
        j = self.h.derive().j
        self.assertFalse(j.relieved(objection["id"], vetoed["id"]), "a pass on the invariant's result relieves nothing")
        own_target = judgment("REVIEW", {"transformation": self.x}, "PASS", actor="human:SHA256:O", frame={"transformation": self.x})
        self.h.sc.admit(own_target)
        frame = Support(frame_state(self.h.sc.derive().s.h, self.h.sc.position - 1, self.x, self.h.sc.derive().s))
        self.assertTrue(frame.j.relieved(objection["id"], vetoed["id"]), "relief on X's own review target")


def policy(owner: str, adjudicator: str, humans, unattested=()) -> str:
    humans_list = ", ".join(f'"{actor(x)}"' for x in humans)
    unattested_list = ", ".join(f'"{actor(x)}"' for x in unattested)
    table = (f'owner = "{actor(owner)}"\nadjudicators = ["{actor(adjudicator)}"]\n'
             f"humans = [{humans_list}]\nunattested_agents = [{unattested_list}]\n")
    return f"schema = 1\n[domains.D4]\n{table}[domains.plan]\n{table}"


class Objection:
    """A standing objection by N (an agent whose task has ended) vetoing P's pass, on content H authored."""

    def __init__(self, kind: str, owner="H", adjudicator="H", humans=("H",), adverse="N", unattested=()):
        self.h = History(policy=policy(owner, adjudicator, humans, unattested))
        self.kind = kind
        sc = self.h.sc
        adverse_actor, adverse_class = actor(adverse), ("HUMAN" if adverse in ("H", "O", "R") else "AGENT")
        if kind in ("transformation_review", "conformance"):
            self.h.enact("a", "k", {"u": 1}, "H")
            x = self.h.candidate({"u": 2}, "H", "k", ["u"])
            target = {"transformation": x} if kind == "transformation_review" else \
                {"transformation": x, "item": {"unit": "plan", "rev": sc.rev("plan")}}
            record_kind = "REVIEW" if kind == "transformation_review" else "CONFORMANCE"
            outcomes = ("NO_PASS", "PASS") if record_kind == "REVIEW" else ("NONCONFORMANT", "CONFORMANT")
            frame = {"transformation": x}
            self.adverse = judgment(record_kind, target, outcomes[0], actor=adverse_actor, actor_class=adverse_class, frame=frame)
            self.vetoed = judgment(record_kind, target, outcomes[1], actor=agent("P"), actor_class="AGENT", frame=frame)
            integrate(sc, x, sc.entries[-1]["records"][0]["target"]["candidate"])
        elif kind in ("subject_triple_review",):
            self.h.enact("a", "k", {"u": 1}, "H")
            t = sc.triple("u")
            self.adverse = judgment("REVIEW", t, "NO_PASS", actor=adverse_actor, actor_class=adverse_class)
            self.vetoed = judgment("REVIEW", t, "PASS", actor=agent("P"), actor_class="AGENT")
        elif kind in ("item_level_review", "joint_invariant_review", "high_consequence_review"):
            x = self.h.enact("a", "k", {"u": 1}, "H")
            at = f"sha256:{sc.position - 1:064x}"
            name = {"item_level_review": "ITEM", "joint_invariant_review": "JOINT_INVARIANT",
                    "high_consequence_review": "HIGH_CONSEQUENCE"}[kind]
            target = {"integrated": name, "of": key("k") if name == "ITEM" else "inv", "at": at, "changes": [x],
                      "scope": ["u", "v", "w"]}
            self.adverse = judgment("REVIEW", target, "NO_PASS", actor=adverse_actor, actor_class=adverse_class)
            self.vetoed = judgment("REVIEW", target, "PASS", actor=agent("P"), actor_class="AGENT")
        elif kind == "plan_acceptance":
            self.h.enact("plan-author", "planning", {"plan": 1}, "H")
            item = {"unit": "plan", "rev": sc.rev("plan")}
            fields = {"objective": item, "items": [item]}
            self.adverse = judgment("PLAN_ACCEPTANCE", {"units": ["plan"]}, "REJECTED", actor=adverse_actor,
                                    actor_class=adverse_class, fields=fields)
            self.vetoed = judgment("PLAN_ACCEPTANCE", {"units": ["plan"]}, "ACCEPTED", actor=agent("P"), actor_class="AGENT",
                                   fields=fields)
        elif kind == "failing_assessment_disposition":
            self.h.enact("a", "k", {"u": 1}, "H")
            realization = judgment("REALIZATION", {"spec": {"unit": "z", "rev": sc.rev("z")},
                                                   "claim": [{"unit": "u", "rev": sc.rev("u")}]}, "COMPLETE",
                                   actor="machinery:dispatcher@ed25519:test", actor_class="MACHINERY", fields={"execution": {}})
            sc.admit(realization)
            fields = {"mode": "ORDINARY", "reading": {"unit": "z", "rev": sc.rev("z")}}
            self.adverse = judgment("EVIDENCE_ASSESSMENT", {"realization": realization["id"], "obligation": "e"}, "FAIL",
                                    actor=adverse_actor, actor_class=adverse_class, fields=fields)
            self.vetoed = judgment("EVIDENCE_ASSESSMENT", {"realization": realization["id"], "obligation": "e"}, "PASS",
                                   actor=agent("P"), actor_class="AGENT", fields=fields)
        sc.admit(self.adverse, self.vetoed)

    def routes(self, state=None, basis_holds=None) -> set[str]:
        d = state or self.h.derive()
        return set(RouteEligibility(d.j if hasattr(d, "j") else Judgments(d)).routes(
            self.adverse["id"], self.vetoed["id"], basis_holds).admissible)


REVIEW_KINDS = ["transformation_review", "subject_triple_review", "item_level_review", "joint_invariant_review",
                "high_consequence_review", "conformance", "plan_acceptance"]


class ObjectionRoutes(unittest.TestCase):
    """cases.py OBJECTION_CASES: who may end an objection on content the policy owner authored (RR-11)."""

    def test_author_owner_waits_for_every_review_kind(self) -> None:
        for kind in REVIEW_KINDS:
            with self.subTest(kind):
                self.assertEqual(Objection(kind).routes(), set(), "waiting on a missing judge (A5; §5.10 (f), (h)(4))")

    def test_author_owner_failing_disposition(self) -> None:
        self.assertEqual(Objection("failing_assessment_disposition").routes(),
                         {"2:owner-supersession", "immateriality-by-owner", "4:upheld-challenge"})

    def test_non_author_owner(self) -> None:
        self.assertEqual(Objection("transformation_review", owner="O", adjudicator="O", humans=("H", "O")).routes(),
                         {"2:owner-supersession", "3:relief-by-owner", "4:upheld-challenge"})

    def test_policy_names_resolver(self) -> None:
        self.assertEqual(Objection("transformation_review", owner="O", adjudicator="H", humans=("H", "O")).routes(),
                         {"2:owner-supersession", "3:relief-by-owner"})

    def test_unknown_lineage_owner_agent(self) -> None:
        self.assertEqual(Objection("transformation_review", owner="U", adjudicator="U", humans=(), unattested=("U",)).routes(),
                         set())

    def test_human_adverse_author(self) -> None:
        self.assertEqual(Objection("transformation_review", adverse="R").routes(), {"1:reassessment", "3:relief-by-author"})


class StateRoutes(unittest.TestCase):
    """cases_s2.py ROUTE_CASES and G1_QUESTIONS: eligibility per route and per state (A1, SD-51)."""

    def test_author_owner_waits(self) -> None:
        self.assertEqual(Objection("transformation_review").routes(), set())

    def test_failing_disposition_exception(self) -> None:
        routes = Objection("failing_assessment_disposition").routes()
        self.assertEqual(routes & {"1:reassessment", "2:owner-supersession", "3:relief-by-author", "3:relief-by-owner",
                                   "4:upheld-challenge"}, {"2:owner-supersession", "4:upheld-challenge"})

    def test_relief_basis_moved(self) -> None:
        o = Objection("plan_acceptance", owner="O", adjudicator="O", humans=("H", "O"))
        self.assertEqual(o.routes(basis_holds=lambda rid: False), {"2:owner-supersession", "4:upheld-challenge"})

    def test_acceptance_fail_in_abandoned_frame(self) -> None:
        h = History(policy=policy("O", "H", ("H", "O")))
        h.enact("a", "k", {"u": 1}, "H")
        x = h.candidate({"v": 1}, "A", "k", ["v"])
        t = h.sc.triple("u")
        adverse = judgment("ACCEPTANCE", t, "FAIL", actor=agent("N"), actor_class="AGENT", frame={"transformation": x})
        vetoed = judgment("ACCEPTANCE", t, "PASS", actor=agent("P"), actor_class="AGENT", basis=[content("u", t["rev"])])
        h.sc.admit(adverse, vetoed)
        d = h.derive()
        self.assertEqual(set(RouteEligibility(d.j).routes(adverse["id"], vetoed["id"]).admissible), {"2:owner-supersession"})

    def _abandoned_and_redispatched(self, owner: str, adjudicator: str, humans, x_lineage, z_lineage, z_extra=None):
        h = History(policy=policy(owner, adjudicator, humans))
        h.enact("a", "k", {"u": 1}, "A")
        x = h.candidate({"v": 1}, x_lineage[0], "k", ["u", "v", "w"])
        h.sc.entries[-1]["records"][0]["binding"]["lineage"] = [actor(a) for a in x_lineage]
        from ssds.ledger.read import with_id

        h.sc.entries[-1]["records"][0] = with_id(h.sc.entries[-1]["records"][0])
        adverse = judgment("REVIEW", {"transformation": x}, "NO_PASS", actor=agent("N"), actor_class="AGENT",
                           frame={"transformation": x})
        h.sc.admit(adverse)
        z = h.candidate({"v": 1, **(z_extra or {})}, z_lineage[0], "k", ["u", "v", "w"], task="t2")
        h.sc.entries[-1]["records"][0]["binding"]["lineage"] = [actor(a) for a in z_lineage]
        h.sc.entries[-1]["records"][0] = with_id(h.sc.entries[-1]["records"][0])
        vetoed = judgment("REVIEW", {"transformation": z}, "PASS", actor=agent("P"), actor_class="AGENT",
                          frame={"transformation": z})
        h.sc.admit(vetoed)
        admitted = h.derive().s
        in_z = Support(frame_state(admitted.h, admitted.n, z, admitted))
        return adverse, vetoed, in_z

    def test_abandoned_review_frame(self) -> None:
        adverse, vetoed, in_z = self._abandoned_and_redispatched("O", "O", ("H", "O"), ["A"], ["A"], {"w": 1})
        self.assertNotEqual(in_z.s.frame.x.id, adverse["target"]["transformation"], "Z is a distinct re-dispatch")
        self.assertTrue(in_z.j.same(adverse["id"], vetoed["id"]), "a re-dispatch keeping rejected content is reached")
        self.assertEqual(set(RouteEligibility(in_z.j).routes(adverse["id"], vetoed["id"]).admissible),
                         {"3:relief-by-owner", "4:upheld-challenge"})

    def test_g1_question_waits_under_amendment_a1(self) -> None:
        adverse, vetoed, in_z = self._abandoned_and_redispatched("O", "H", ("H", "O"), ["H"], ["H", "O"], {"w": 1})
        routes = RouteEligibility(in_z.j).routes(adverse["id"], vetoed["id"])
        self.assertTrue(in_z.j.same(adverse["id"], vetoed["id"]))
        self.assertEqual(set(routes.admissible), set())
        self.assertTrue(routes.waiting, "no eligible judge for any route here: the objection waits, with human attention")

    def test_pending_frame_where_it_bites(self) -> None:
        h = History(policy=policy("O", "O", ("H", "O")))
        x = h.candidate({"u": 1}, "H", "k", ["u"])
        adverse = judgment("REVIEW", {"transformation": x}, "NO_PASS", actor=agent("N"), actor_class="AGENT",
                           frame={"transformation": x})
        vetoed = judgment("REVIEW", {"transformation": x}, "PASS", actor=agent("P"), actor_class="AGENT",
                          frame={"transformation": x})
        h.sc.admit(adverse, vetoed)
        admitted = h.derive().s
        in_x = Support(frame_state(admitted.h, admitted.n, x, admitted))
        self.assertEqual(set(RouteEligibility(in_x.j).routes(adverse["id"], vetoed["id"]).admissible),
                         {"2:owner-supersession", "3:relief-by-owner", "4:upheld-challenge"})

    def test_reached_larger_judged_set(self) -> None:
        h = History(policy=policy("O", "O", ("O",)))
        x = h.enact("a", "k", {"u": 1}, "A")
        adverse = judgment("REVIEW", {"transformation": x}, "NO_PASS", actor=agent("N"), actor_class="AGENT",
                           frame={"transformation": x})
        h.sc.admit(adverse)
        z = h.enact("b", "k", {"v": 1}, "O", scope=["u", "v"])
        vetoed = judgment("REVIEW", {"transformation": z}, "PASS", actor=agent("P"), actor_class="AGENT",
                          frame={"transformation": z})
        h.sc.admit(vetoed)
        d = h.derive()
        self.assertTrue(d.j.same(adverse["id"], vetoed["id"]))
        self.assertEqual(set(RouteEligibility(d.j).routes(adverse["id"], vetoed["id"]).admissible),
                         {"2:owner-supersession", "4:upheld-challenge"})


class VetoAndSupport(unittest.TestCase):
    """A standing objection supports nothing in its reach; ending it by an eligible route restores support."""

    def test_a_reached_pass_is_vetoed_until_the_owner_supersedes(self) -> None:
        o = Objection("transformation_review", owner="O", adjudicator="O", humans=("H", "O"))
        d = o.h.derive()
        self.assertTrue(d.j.vetoed(o.vetoed["id"]))
        supersession = judgment("REVIEW", o.adverse["target"], "PASS", actor=actor("O"), supersedes=[o.adverse["id"]],
                                frame=o.adverse["frame"])
        o.h.sc.admit(supersession)
        self.assertFalse(o.h.derive().j.vetoed(o.vetoed["id"]))


if __name__ == "__main__":
    unittest.main()
