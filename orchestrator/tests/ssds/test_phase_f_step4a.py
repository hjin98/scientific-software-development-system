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
from ._scenario import HUMAN, HUMAN_B, OWNER, Scenario, agent, fresh, judgment
from .test_admission_requests import RequestFixture, finding

DOC = '''
    [[unit]]
    id = "doc"
    kind = "D3"
    scope = [{ path = "doc.md" }]
'''


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


if __name__ == "__main__":
    unittest.main()
