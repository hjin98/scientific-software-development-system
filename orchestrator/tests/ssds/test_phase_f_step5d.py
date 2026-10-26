"""Phase F step 5d: claims and integration legality (catalogue §8.3 step 7, §11.5 (3), §14.6, SD-26; plan §3.2,
readings F32, F35, F37).

Under SD-70 neither an integrating request nor a claim reading conformance is accepted in Phase F, and no
integrating request reaches the engine with an admitted result, so the decisions are tested at their owners on
derivation histories, and the claim path through the engine by a claim-only request.
"""

from __future__ import annotations

import unittest

from ssds.admission.engine import integration_codes, review_codes
from ssds.admission.legality import Legality
from ssds.derivation import Workflow
from ssds.derivation.workflow import make

from ._scenario import HUMAN, attested, content, judgment
from .test_conformance import accepted_plan, realize, submit
from .test_obligations import HUMANS, TWO
from .test_phase_f_step4e import tried

SOLVED = {"src/solver.py": "def step():\n    return 2\n"}


def integrating(sc, cand) -> set[str]:
    support = sc.derive()
    tasks = {support.s.enactment(x) for x in support.s.submissions}
    return integration_codes(cand, support, {"envelope": {"task_id": next(iter(tasks))}})


class Conformance(unittest.TestCase):
    def test_unrealized_evidence_waits_and_a_breach_condemns(self) -> None:
        sc = accepted_plan()
        _, cand, _ = submit(sc, SOLVED)
        self.assertIn("CONFORMANCE_INCOMPLETE", integrating(sc, cand), "pending: not the candidate's defect")
        self.assertNotIn("CONFORMANCE_FAILED", integrating(sc, cand))
        breach = accepted_plan()
        _, cand2, _ = submit(breach, {**SOLVED, "records.md": "# Records changed\n"})
        realize(breach, cand2)
        codes = integrating(breach, cand2)
        self.assertIn("CONFORMANCE_FAILED", codes, "an undisclosed breach: VIOLATION and DISCREPANCY")
        self.assertNotIn("CONFORMANCE_INCOMPLETE", codes)

    def test_only_the_candidates_own_failure_is_a_merit(self) -> None:
        """F35: a rejection for CONFORMANCE_FAILED ends the candidate; one for CONFORMANCE_INCOMPLETE leaves it
        pending, as unrealized evidence is no defect of the candidate."""

        from ssds.admission.checks import on_merits

        self.assertTrue(on_merits({"CONFORMANCE_FAILED"}))
        self.assertFalse(on_merits({"CONFORMANCE_INCOMPLETE"}))
        self.assertFalse(on_merits({"OBLIGATION_PREDICATE_UNMET"}), "no current review yet")
        self.assertTrue(on_merits({"STALE_RETAINED", "OBLIGATION_REENACTED"}))

    def test_a_result_only_failure_condemns_even_beside_unrealized_evidence(self) -> None:
        from .test_conformance import SLOTS

        sc = accepted_plan()
        _, cand, _ = submit(sc, SOLVED, slots=dict(SLOTS, unverified_assumptions=[]))
        self.assertIn("CONFORMANCE_FAILED", integrating(sc, cand), "an empty slot is the result's own (F30)")


class Reviews(unittest.TestCase):
    def test_reviews_are_current_and_judged_the_merged_content(self) -> None:
        from ._scenario import agent, fresh

        sc = accepted_plan()
        x, cand, _ = submit(sc, SOLVED)
        realize(sc, cand)
        support = sc.derive()
        self.assertEqual(review_codes(x, support, Workflow(support)), {"OBLIGATION_PREDICATE_UNMET"}, "no review")
        (review,) = Workflow(support).of_kind("REVIEW")
        sc.admit(judgment("REVIEW", {"transformation": x}, "PASS", actor=agent("checker"), actor_class="AGENT",
                          basis=[content("src", sc.view(cand).rev("src"))], frame={"transformation": x},
                          binding=dict(fresh(agent("checker"), "task-r"), obligation=review.id)))
        support = sc.derive()
        self.assertEqual(review_codes(x, support, Workflow(support)), set())

    def test_stale_retained_reads_the_judged_content(self) -> None:
        from .test_judgment import History, TransformationJudgedContent

        for name in ("first_enactment", "same_key_other_scope_after_issue", "same_key_in_scope_after_issue",
                     "foreign_in_scope_after_issue", "unrelated_after_issue"):
            issue, later, delta, author, _, supported = TransformationJudgedContent.CASES[name]
            with self.subTest(name):
                h = History()
                for owner, item, d, a in issue:
                    h.enact(owner, item, d, a)
                x = h.candidate(delta, author, "k", ["u", "v"])
                h.sc.admit(judgment("REVIEW", {"transformation": x}, "PASS", actor="human:SHA256:reviewer",
                                    frame={"transformation": x}))
                for owner, item, d, a in later:
                    h.enact(owner, item, d, a)
                support = h.derive()
                codes = review_codes(x, support, Workflow(support))
                self.assertEqual("STALE_RETAINED" in codes, not supported, codes)


class ClaimedDischarge(unittest.TestCase):
    """A claimed obligation's discharge predicate holds after the request's own records (§8.3 step 7)."""

    def test_the_predicate_is_read_in_the_trial(self) -> None:
        from ._scenario import Scenario

        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}, policy=HUMANS)
        o = make("ACCEPT", sc.triple("arch"), holder="HUMAN")
        legality = Legality(sc.derive())
        t = sc.triple("arch")
        acceptance = judgment("ACCEPTANCE", t, "PASS", actor=HUMAN, basis=[content("arch", t["rev"])])
        with_it = tried(sc, attested(acceptance))
        self.assertEqual(legality.request_codes({"claims": [o.id]}, [], with_it), set())
        self.assertEqual(legality.request_codes({"claims": [o.id]}, [], tried(sc, [])), {"OBLIGATION_PREDICATE_UNMET"})
        self.assertEqual(legality.request_codes({"claims": [o.id]}, []), set(), "no trial: nothing to read")

    def test_a_claim_only_request_is_judged_after_it_through_the_engine(self) -> None:
        from ssds.admission.request import request_message

        from ._fixtures import sshsig
        from .test_admission_requests import RequestFixture

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        req = fixture.request([], base_position=len(fixture.entries()) - 1, claims=[fixture.obligation()])
        req["binding"] = {"human": {"actor": fixture.human(), "signature": sshsig(fixture.private, request_message(req))}}
        self.assertIn("OBLIGATION_PREDICATE_UNMET", fixture.admit(req).reasons)


if __name__ == "__main__":
    unittest.main()
