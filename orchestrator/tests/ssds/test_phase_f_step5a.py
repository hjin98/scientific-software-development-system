"""Phase F step 5a: step 7-8 codes and the decision model (catalogue §8.3 steps 6-8, §8.4; plan §3.2, readings
F34-F35).

A rejection names the integration's ``X`` only when every reason judges the candidate itself (F35), so the item
takes a new iteration (``Items.refused``) and a rejection for a binding, an unbuilt check or a moved head leaves the
candidate pending. Salvage admits every never-lost record whose own checks exist (steps 4b-4d), and still refuses a
failing assessment and a runner's observation until step 9.
"""

from __future__ import annotations

import unittest
from unittest import mock

from ssds.admission.checks import MERIT_CODES, REASONS, on_merits
from ssds.ledger.read import read_chain, with_id

from ._fixtures import admission_body, record
from ._scenario import Scenario, agent, submit
from .test_phase_f_step4d import FILES, THREE


class Codes(unittest.TestCase):
    def test_step_seven_and_eight_codes_are_closed_members(self) -> None:
        for code in ("OBLIGATION_REENACTED", "OBLIGATION_ANSWERED", "OBLIGATION_REVIEW_OPEN", "STALE_RETAINED",
                     "CONFORMANCE_RESULT", "REGRESSION", "NOT_SETTLED", "HEAD_MOVED", "OBLIGATION_NOT_DERIVED"):
            self.assertIn(code, REASONS)
        self.assertLessEqual(MERIT_CODES, REASONS)
        self.assertFalse({"ENACTMENT_MISSING", "FREEZE_SOURCE", "FREEZE_DESTINATION"} & MERIT_CODES)

    def test_on_merits(self) -> None:
        self.assertTrue(on_merits({"AUTH_WRITE_SCOPE", "STRUCT_SIBLING_OVERLAP", "RELATION_DANGLING"}))
        self.assertFalse(on_merits(set()), "nothing judged")
        self.assertFalse(on_merits({"SCHEMA_UNSUPPORTED"}), "an unbuilt check judges nothing")
        self.assertFalse(on_merits({"AUTH_WRITE_SCOPE", "AUTH_ENVELOPE"}), "a binding fault taints the rejection")
        self.assertFalse(on_merits({"REF_BASE"}))
        self.assertFalse(on_merits({"FREEZE_SOURCE"}), "a freeze is the head's state (review 87b4fa8 B1)")
        self.assertFalse(on_merits({"FREEZE_DESTINATION", "AUTH_WRITE_SCOPE"}))
        self.assertFalse(on_merits({"ENACTMENT_MISSING"}), "the review route records it in X's frame")


class RefusedIntegration(unittest.TestCase):
    """A REJECT naming ``X`` ends its pending candidate and integrates nothing (History's fold reads ACCEPT only)."""

    def test_a_rejection_naming_x_refuses_without_integrating(self) -> None:
        from ssds.derivation import Workflow

        sc = Scenario(THREE, dict(FILES))
        x, candidate, _ = submit(sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        sc.entries.append(admission_body(sc.position, sc.head, sc.head, decision="REJECT", integrates=x))
        d = sc.derive()
        self.assertEqual(d.s.h.head(d.s.n), sc.head, "the head did not move")
        self.assertNotIn(d.s.enactment(x), d.s.integrated)
        self.assertIn(x, Workflow(d).items.refused)


class EngineRejection(unittest.TestCase):
    """The engine names ``X`` on a rejection on the candidate's merits only."""

    def decide(self, codes: set[str], binding_ok: bool = True):
        from ssds.admission.request import request_message

        from ._fixtures import sshsig
        from .test_admission_requests import RequestFixture, finding

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        x = "sha256:" + "7" * 64
        rec = with_id({**finding(), "actor": fixture.human()})
        req = fixture.request([rec], base_position=len(fixture.entries()) - 1, candidates=["0" * 40])
        key = fixture.private if binding_ok else None
        req["binding"] = {"human": {"actor": fixture.human(),
                                    "signature": sshsig(key, request_message(req)) if key else "x"}}
        with mock.patch.multiple("ssds.admission.engine", integration_codes=lambda *a: set(codes),
                                 integration_frame=lambda *a: "REF_TRANSFORMATION",
                                 submitted_with=lambda *a: [x]):
            decision = fixture.admit(req)
        chain = read_chain(fixture.home.ledger_repository("demo"), "demo")
        return decision, chain.entries[chain.readable_through].entry["admission"]["integrates"], x

    def test_a_rejection_on_the_merits_names_x(self) -> None:
        decision, integrates, x = self.decide({"AUTH_WRITE_SCOPE"})
        self.assertEqual(decision.decision, "REJECT")
        self.assertEqual(integrates, x)

    def test_an_unbuilt_check_leaves_the_candidate_pending(self) -> None:
        decision, integrates, _ = self.decide(set())
        self.assertIn("SCHEMA_UNSUPPORTED", decision.reasons)
        self.assertIsNone(integrates)

    def test_a_bad_binding_never_condemns_a_candidate(self) -> None:
        decision, integrates, _ = self.decide({"AUTH_WRITE_SCOPE"}, binding_ok=False)
        self.assertEqual(decision.decision, "REJECT")
        self.assertIsNone(integrates)


class Salvage(unittest.TestCase):
    """Never-lost records whose own checks exist are salvaged; a failing assessment waits for step 9."""

    def test_salvageable_kinds(self) -> None:
        from ssds.admission.engine import salvageable

        for kind in ("FINDING", "CHALLENGE", "REVIEW", "ACCEPTANCE", "GATE_DECISION", "REALIZATION",
                     "EVIDENCE_ASSESSMENT", "CUSTODY_ENUMERATION"):  # 9d (F99)
            self.assertTrue(salvageable({"kind": kind}), kind)
        for kind in ("CHECK_EXECUTION",):
            self.assertFalse(salvageable({"kind": kind}), kind)

    def test_an_adverse_judgment_is_salvaged_through_the_engine(self) -> None:
        from ssds.admission.request import request_message

        from ._fixtures import sshsig
        from .test_admission_requests import RequestFixture
        from .test_phase_f_step4b import derive_state

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        subject, scope, rev = derive_state(fixture).subject_triple("guide")
        content = {"mode": "content", "target": {"unit": "guide", "rev": rev}, "class": "EXACT"}
        adverse = with_id({**record("REVIEW", target={"subject": subject, "scope_id": scope, "rev": rev},
                                    outcome="NO_PASS", basis=[content]), "actor": fixture.human()})
        req = fixture.request([adverse], base_position=len(fixture.entries()) - 1)
        req["binding"] = {"human": {"actor": fixture.human(), "signature": sshsig(fixture.private, request_message(req))}}
        decision = fixture.admit(req)
        self.assertEqual(decision.decision, "ACCEPT", "a records-only adverse judgment is accepted since step 6c")
        self.assertIn(adverse["id"], decision.admitted)


if __name__ == "__main__":
    unittest.main()
