"""Phase F step 4a: the fail-closed salvage and the independence classification at its derivation owner.

The salvage case runs the real Admission engine on a shadow ledger (the plan review of b10018de, B1). The
independence cases build histories with the derivation scenario builder and query ``Judgments.nonind``, the one
owner every consumer reads (catalogue §5.10 (a); plan review b10018de B4).
"""

from __future__ import annotations

import unittest

from ssds.derivation import derive
from ssds.ledger.read import read_chain

from ._fixtures import record
from ._scenario import (HUMAN, HUMAN_B, OWNER, Scenario, adjudication, agent, challenge, fresh, integrate, judgment,
                        submit)
from .test_admission_requests import RequestFixture, finding

DOC = '''
    [[unit]]
    id = "doc"
    kind = "D3"
    scope = [{ path = "doc.md" }]
'''
SUBJECT_DOC = '''
    [[unit]]
    id = "doc"
    kind = "D3"
    subject = true
    scope = [{ path = "doc.md" }]
'''


def owner_policy(*humans: str) -> str:
    return 'schema = 1\n[domains.D3]\nowner = "%s"\nhumans = [%s]\n' % (OWNER, ", ".join(f'"{h}"' for h in humans))


class FailClosedSalvage(RequestFixture):
    """Until step 4b, a never-lost record is salvaged only when it owes no unbuilt check (Phase F plan §3.1)."""

    def state(self):
        return derive(read_chain(self.home.ledger_repository("demo"), "demo"), self.trees).s

    def test_b1_a_peer_judgment_salvaged_never_supersedes_another(self) -> None:
        subject, scope, rev = self.state().subject_triple("guide")
        target = {"subject": subject, "scope_id": scope, "rev": rev}
        req, (first,) = self.bound([record("REVIEW", target=target, outcome="NO_PASS")])
        one = self.admit(req)
        self.assertEqual((one.admitted, one.refused), ((), ((first["id"], ("SCHEMA_UNSUPPORTED",)),)))
        req, (second,) = self.bound([record("REVIEW", target=target, outcome="NO_PASS", supersedes=[first["id"]])])
        two = self.admit(req)
        self.assertEqual(two.admitted, ())
        self.assertNotIn(first["id"], self.state().records)
        self.assertNotIn(second["id"], self.state().records)

    def test_only_reports_superseding_nothing_are_salvaged(self) -> None:
        issued = self.issue()
        report = self.bind(finding(), issued)
        earlier = self.bind(finding(materiality="MATERIAL"), issued)
        self.admit(self.signed(issued, [earlier]))
        issued = self.issue()
        report = self.bind(finding(), issued)
        replacing = self.bind(record("FINDING", target={"units": ["guide"]}, fields={"materiality": "ROUTINE"},
                                     supersedes=[earlier["id"]]), issued)
        challenge = self.bind(record("CHALLENGE", target={"record": earlier["id"]}, fields={"blocking": True}), issued)
        decision = self.admit(self.signed(issued, [report, replacing, challenge]))
        self.assertEqual(decision.admitted, (report["id"],))
        refused = dict(decision.refused)
        self.assertEqual(refused.get(replacing["id"]), ("SCHEMA_UNSUPPORTED",))
        self.assertIn(challenge["id"], refused)


class IndependenceAtAdmission(unittest.TestCase):
    """``nonind`` is fixed at the record's admission (§5.10 (a)), covers every disposition of a failing
    assessment, and applies the owner exception (SD-48) at the one owner the routes also read."""

    def failing_assessment(self, sc: Scenario, rev: str) -> dict:
        realization = judgment("REALIZATION", {"spec": {"unit": "doc", "rev": rev}, "claim": [{"unit": "doc", "rev": rev}]},
                               "COMPLETE", actor="machinery:dispatcher@ed25519:test", actor_class="MACHINERY",
                               fields={"execution": {}})
        failing = judgment("EVIDENCE_ASSESSMENT", {"realization": realization["id"], "obligation": "e"}, "FAIL",
                           actor=HUMAN_B, fields={"mode": "ORDINARY", "reading": {"unit": "doc", "rev": rev}})
        sc.admit(realization, failing)
        return failing

    def test_a_classification_never_changes_after_admission(self) -> None:
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[HUMAN])
        r1 = sc.triple("doc")["rev"]
        completeness = judgment("COMPLETENESS", {"scope": ["doc"], "classes": ["WARRANT"],
                                                 "membership": sc.derive().s.membership_digest(["doc"])},
                                "COMPLETE", actor=HUMAN)
        sc.admit(completeness)
        self.assertTrue(sc.derive().j.nonind(completeness["id"]), "its author's own completeness is not independent")
        sc.integrate({"doc.md": "r2\n"}, agent("other"), "task-2", lineage=[agent("other")])
        r2 = sc.triple("doc")["rev"]
        sc.admit(judgment("EQUIVALENCE", {"unit": "doc", "from": r1, "to": r2, "class": "EDITORIAL"}, "EQUIVALENT",
                          actor=HUMAN_B))
        self.assertTrue(sc.derive().j.nonind(completeness["id"]), "a later move of its member changes nothing")

    def test_a_reassessment_disposing_of_a_failure_has_a_requirement(self) -> None:
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[HUMAN])
        r1 = sc.triple("doc")["rev"]
        failing = self.failing_assessment(sc, r1)
        by_author = judgment("EVIDENCE_ASSESSMENT", failing["target"], "PASS", actor=agent("again"), actor_class="AGENT",
                             supersedes=[failing["id"]], fields=failing["fields"],
                             binding=fresh(agent("again"), lineage=[agent("again"), HUMAN]))
        sc.admit(by_author)
        d = sc.derive()
        self.assertTrue(d.j.nonind(by_author["id"]), "a lineage reaching the claim's author disposes of nothing")
        self.assertTrue(d.j.requirement(by_author))

    def test_the_owner_exception_admits_the_only_qualified_human_as_independent(self) -> None:
        for humans, expected in (([OWNER], False), ([OWNER, HUMAN], True)):
            with self.subTest(humans=humans):
                policy = 'schema = 1\n[domains.D3]\nowner = "%s"\nhumans = [%s]\n' % (
                    OWNER, ", ".join(f'"{h}"' for h in humans))
                sc = Scenario(DOC, {"doc.md": "r0\n"}, policy=policy)
                sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[OWNER])
                failing = self.failing_assessment(sc, sc.triple("doc")["rev"])
                owner = judgment("EVIDENCE_ASSESSMENT", failing["target"], "PASS", actor=OWNER,
                                 supersedes=[failing["id"]], fields=failing["fields"])
                sc.admit(owner)
                d = sc.derive()
                self.assertEqual(d.j.nonind(owner["id"]), expected)
                self.assertEqual(d.j.common_mode(owner["id"]), not expected)

    def test_an_open_lineage_closure_is_never_disjoint(self) -> None:
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1")
        t = sc.triple("doc")
        open_ = judgment("REVIEW", t, "PASS", actor=agent("reviewer"), actor_class="AGENT",
                         binding=fresh(agent("reviewer"), lineage=[agent("reviewer"), "UNKNOWN"]))
        closed = judgment("REVIEW", t, "PASS", actor=agent("second"), actor_class="AGENT",
                          binding=fresh(agent("second"), lineage=[agent("second")]))
        sc.admit(open_, closed)
        d = sc.derive()
        self.assertEqual((d.j.nonind(open_["id"]), d.j.nonind(closed["id"])), (True, False))



class IndependenceRecheck(unittest.TestCase):
    """The same-family review of 409c2f71: frame records (B1), chained dispositions (B2), the adjudication branch
    of the owner exception (B3), the classification's cost (B4) and the exception's scope (B5)."""

    failing_assessment = IndependenceAtAdmission.failing_assessment

    def candidate_by(self, sc: Scenario, lineage: list[str]):
        from ssds.ledger.read import with_id

        sc.integrate({"doc.md": "r1\n"}, agent("other"), "task-0", lineage=[HUMAN_B])
        x, candidate, result = submit(sc, {"doc.md": "r2\n"}, agent("author"), "task-1")
        sc.entries.pop()
        result = dict(result)
        result["binding"] = dict(result["binding"], lineage=lineage)
        result.pop("id")
        sc.admit(with_id(result))
        return x, candidate

    def test_b1_a_frame_record_by_the_candidates_author_is_never_independent(self) -> None:
        for kind in ("ACCEPTANCE", "COMPLETENESS"):
            with self.subTest(kind=kind):
                sc = Scenario(SUBJECT_DOC, {"doc.md": "r0\n"})
                x, candidate = self.candidate_by(sc, [HUMAN])
                frame = {"transformation": x}
                if kind == "ACCEPTANCE":
                    j = judgment("ACCEPTANCE", sc.triple("doc", head=candidate), "PASS", actor=HUMAN, frame=frame)
                else:
                    j = judgment("COMPLETENESS", {"scope": ["doc"], "classes": ["WARRANT"],
                                                  "membership": sc.derive().s.membership_digest(["doc"])},
                                 "COMPLETE", actor=HUMAN, frame=frame)
                sc.admit(j)
                self.assertTrue(sc.derive().j.nonind(j["id"]), "in its frame, before integration")
                integrate(sc, x, candidate)
                self.assertTrue(sc.derive().j.nonind(j["id"]), "and after it")

    def test_b2_a_disposition_through_a_chain_of_reassessments_has_the_requirement(self) -> None:
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[HUMAN])
        failing = self.failing_assessment(sc, sc.triple("doc")["rev"])
        first = judgment("EVIDENCE_ASSESSMENT", failing["target"], "PASS", actor=HUMAN, supersedes=[failing["id"]],
                         fields=failing["fields"])
        sc.admit(first)
        second = judgment("EVIDENCE_ASSESSMENT", failing["target"], "PASS", actor=HUMAN, supersedes=[first["id"]],
                          fields=failing["fields"])
        sc.admit(second)
        d = sc.derive()
        self.assertTrue(d.j.requirement(second))
        self.assertEqual((d.j.nonind(first["id"]), d.j.nonind(second["id"])), (True, True))
        self.assertEqual(d.a.disposition(failing["id"], lambda node: d.values.get(node, 0), d.base, d.j.nonind), 0)

    def test_j6_superseding_a_passing_assessment_disposes_of_nothing(self) -> None:
        sc = Scenario(DOC, {"doc.md": "r0\n"})
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[HUMAN])
        failing = self.failing_assessment(sc, sc.triple("doc")["rev"])
        passing = judgment("EVIDENCE_ASSESSMENT", failing["target"], "PASS", actor=HUMAN_B, fields=failing["fields"])
        sc.admit(passing)
        again = judgment("EVIDENCE_ASSESSMENT", failing["target"], "PASS", actor=HUMAN, supersedes=[passing["id"]],
                         fields=failing["fields"])
        sc.admit(again)
        self.assertFalse(sc.derive().j.requirement(again))

    def test_b3_the_owner_exception_covers_an_upheld_adjudication_of_the_failure_only(self) -> None:
        for outcome, nonind in (("UPHELD", False), ("DISMISSED", True)):
            with self.subTest(outcome=outcome):
                sc = Scenario(DOC, {"doc.md": "r0\n"}, policy=owner_policy(OWNER))
                sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[OWNER])
                failing = self.failing_assessment(sc, sc.triple("doc")["rev"])
                c = challenge({"record": failing["id"]})
                sc.admit(c)
                a = adjudication(c["id"], outcome, actor=OWNER)
                sc.admit(a)
                d = sc.derive()
                self.assertEqual((d.j.nonind(a["id"]), d.j.common_mode(a["id"])), (nonind, not nonind))

    def test_j4_j5_the_owners_immateriality_of_the_failure_takes_the_exception(self) -> None:
        sc = Scenario(DOC, {"doc.md": "r0\n"}, policy=owner_policy(OWNER))
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[OWNER])
        failing = self.failing_assessment(sc, sc.triple("doc")["rev"])
        immaterial = judgment("IMMATERIALITY", {"records": [failing["id"]]}, "IMMATERIAL", actor=OWNER)
        sc.admit(immaterial)
        d = sc.derive()
        self.assertEqual((d.j.nonind(immaterial["id"]), d.j.common_mode(immaterial["id"])), (False, True))
        from ssds.derivation import Workflow, queries

        why = queries.explain(Workflow(d), immaterial["id"])["why"]
        self.assertTrue(any(line.startswith("common-mode") for line in why), "the inspector shows the dependency")

    def test_b5_j19_the_exception_never_covers_a_judgment_that_disposes_of_no_failure(self) -> None:
        sc = Scenario(SUBJECT_DOC, {"doc.md": "r0\n"}, policy=owner_policy(OWNER))
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[OWNER])
        t = sc.triple("doc")
        review = judgment("REVIEW", t, "PASS", actor=OWNER)
        acceptance = judgment("ACCEPTANCE", t, "PASS", actor=OWNER)
        sc.admit(review, acceptance)
        d = sc.derive()
        for rec in (review, acceptance):
            self.assertEqual((d.j.nonind(rec["id"]), d.j.common_mode(rec["id"])), (True, False))

    def test_authors_are_read_as_the_ledger_knew_them_at_admission(self) -> None:
        sc = Scenario(SUBJECT_DOC, {"doc.md": "r0\n"})
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1")
        t = sc.triple("doc")
        review = judgment("REVIEW", t, "PASS", actor=agent("reviewer"), actor_class="AGENT",
                          binding=fresh(agent("reviewer")))
        sc.admit(review)
        sc.integrate({"doc.md": "r2\n"}, agent("other"), "task-2")
        sc.integrate({"doc.md": "r1\n"}, agent("reviewer"), "task-3")  # the reviewer later re-produces r1
        d = sc.derive()
        self.assertIn(agent("reviewer"), d.s.authors("doc", t["rev"]), "a later producer of the same revision")
        self.assertFalse(d.j.nonind(review["id"]), "is no author of what the review judged at its admission")

    def test_j20_unknown_authorship_is_never_disjoint_from_an_agent(self) -> None:
        sc = Scenario(SUBJECT_DOC, {"doc.md": "r0\n"})
        sc.absorb({"doc.md": "r1\n"})  # content no admitted record produced: its authors are UNKNOWN
        review = judgment("REVIEW", sc.triple("doc"), "PASS", actor=agent("reviewer"), actor_class="AGENT",
                          binding=fresh(agent("reviewer")))
        sc.admit(review)
        self.assertTrue(sc.derive().j.nonind(review["id"]))

    def test_b4_classifying_builds_no_state(self) -> None:
        from unittest import mock

        from ssds.derivation.state import State

        sc = Scenario(DOC, {"doc.md": "r0\n"})
        for n in range(30):
            sc.integrate({"doc.md": f"r{n + 1}\n"}, agent(f"a{n}"), f"task-{n}")
            sc.admit(judgment("COMPLETENESS", {"scope": ["doc"], "classes": ["WARRANT"], "membership": "sha256:" + "0" * 64},
                              "COMPLETE", actor=HUMAN))
        d = sc.derive()
        built = []
        original = State.__init__

        def counting(self, *args, **kwargs):
            built.append(args)
            original(self, *args, **kwargs)

        with mock.patch.object(State, "__init__", counting):
            for rid in d.s.of_kind("COMPLETENESS"):
                d.j.nonind(rid)
        self.assertEqual(built, [], "the classification reads the history's one authorship fold")


class IndependenceThirdCheck(unittest.TestCase):
    """The narrow re-check of b8a18003: a restored revision's earlier producers (B1), the owner exception over
    every failure an ``IMMATERIALITY`` covers (B2), and the exception's unknown-authorship clause and the policy
    in force at admission (B3)."""

    failing_assessment = IndependenceAtAdmission.failing_assessment

    def test_b1_a_candidate_restoring_a_revision_keeps_its_earlier_authors(self) -> None:
        sc = Scenario(SUBJECT_DOC, {"doc.md": "r0\n"})
        sc.integrate({"doc.md": "r1\n"}, agent("a"), "task-0", lineage=[HUMAN])
        sc.integrate({"doc.md": "r2\n"}, agent("b"), "task-1", lineage=[HUMAN_B])
        x, candidate, _ = submit(sc, {"doc.md": "r1\n"}, agent("reverter"), "task-2")
        acceptance = judgment("ACCEPTANCE", sc.triple("doc", head=candidate), "PASS", actor=HUMAN,
                              frame={"transformation": x})
        sc.admit(acceptance)
        self.assertTrue(sc.derive().j.nonind(acceptance["id"]), "r1's author accepting its restoration")
        integrate(sc, x, candidate)
        self.assertTrue(sc.derive().j.nonind(acceptance["id"]))

    def test_b2_an_owners_immateriality_takes_the_exception_only_for_every_failure_it_covers(self) -> None:
        units = DOC + '''
    [[unit]]
    id = "spec"
    kind = "D2"
    scope = [{ path = "spec.md" }]
'''
        policy = ('schema = 1\n[domains.D3]\nowner = "%s"\nhumans = ["%s"]\n[domains.D2]\nowner = "%s"\n'
                  'humans = ["%s", "%s"]\n' % (OWNER, OWNER, HUMAN_B, HUMAN_B, OWNER))
        for order in ((0, 1), (1, 0)):
            with self.subTest(order=order):
                sc = Scenario(units, {"doc.md": "d0\n", "spec.md": "s0\n"}, policy=policy)
                sc.integrate({"doc.md": "d1\n", "spec.md": "s1\n"}, agent("author"), "task-1", lineage=[OWNER])
                failures = []
                for unit in ("doc", "spec"):
                    rev = sc.rev(unit)
                    real = judgment("REALIZATION", {"spec": {"unit": unit, "rev": rev}, "claim": [{"unit": unit, "rev": rev}]},
                                    "COMPLETE", actor="machinery:dispatcher@ed25519:test", actor_class="MACHINERY",
                                    fields={"execution": {}})
                    failing = judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": "e-" + unit},
                                       "FAIL", actor=HUMAN_B, fields={"mode": "ORDINARY", "reading": {"unit": unit, "rev": rev}})
                    sc.admit(real, failing)
                    failures.append(failing["id"])
                immaterial = judgment("IMMATERIALITY", {"records": [failures[i] for i in order]}, "IMMATERIAL",
                                      actor=OWNER)
                sc.admit(immaterial)
                d = sc.derive()
                self.assertEqual((d.j.nonind(immaterial["id"]), d.j.common_mode(immaterial["id"])), (True, False),
                                 "the D2 failure has another qualified human")

    def test_b3_j20_unknown_authorship_lets_the_owner_take_the_exception(self) -> None:
        units = DOC + '''
    [[unit]]
    id = "notes"
    kind = "D3"
    scope = [{ path = "notes.md" }]
'''
        sc = Scenario(units, {"doc.md": "r0\n", "notes.md": "n0\n"}, policy=owner_policy(OWNER, HUMAN))
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[OWNER])
        sc.absorb({"notes.md": "n1\n"})  # authored by no admitted record: UNKNOWN
        claim = [{"unit": "doc", "rev": sc.rev("doc")}, {"unit": "notes", "rev": sc.rev("notes")}]
        real = judgment("REALIZATION", {"spec": claim[0], "claim": claim}, "COMPLETE",
                        actor="machinery:dispatcher@ed25519:test", actor_class="MACHINERY", fields={"execution": {}})
        failing = judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": "e"}, "FAIL", actor=HUMAN_B,
                           fields={"mode": "ORDINARY", "reading": claim[0]})
        sc.admit(real, failing)
        owner = judgment("EVIDENCE_ASSESSMENT", failing["target"], "PASS", actor=OWNER, supersedes=[failing["id"]],
                         fields=failing["fields"])
        sc.admit(owner)
        d = sc.derive()
        self.assertEqual((d.j.nonind(owner["id"]), d.j.common_mode(owner["id"])), (False, True),
                         "with an unknown author, another qualified human may be an author too")

    def test_b3_r12_the_exception_reads_the_policy_in_force_at_admission(self) -> None:
        import hashlib

        sc = Scenario(DOC, {"doc.md": "r0\n"}, policy=owner_policy(OWNER))
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[OWNER])
        failing = self.failing_assessment(sc, sc.triple("doc")["rev"])
        owner = judgment("EVIDENCE_ASSESSMENT", failing["target"], "PASS", actor=OWNER, supersedes=[failing["id"]],
                         fields=failing["fields"])
        sc.admit(owner)
        later = owner_policy(OWNER, HUMAN).encode("utf-8")  # a second qualified human, adopted afterwards
        digest = "sha256:" + hashlib.sha256(later).hexdigest()
        sc.objects.setdefault(sc.position, {})[digest] = later
        sc.lifecycle(record("RULESET_ADOPTION", target=None, actor=HUMAN,
                            fields={"system": "ssds-rules/1", "policy": digest, "analyzers": ["ssds.analyzer.python/1"]}))
        d = sc.derive()
        self.assertEqual(d.s.policy.get("D3", "humans", ()), [OWNER, HUMAN])
        self.assertEqual((d.j.nonind(owner["id"]), d.j.common_mode(owner["id"])), (False, True))

if __name__ == "__main__":
    unittest.main()
