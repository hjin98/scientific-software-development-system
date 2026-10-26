"""Phase F step 5b-i: step 7's obligation checks (catalogue §8.3 step 7; plan §3.2, readings F31, F34, F36).

The decisions read the head's workflow; histories come from the derivation scenario builder, and the engine's
wiring is checked on a records-only request, the only kind that reaches step 7 through the engine today.
"""

from __future__ import annotations

import unittest
from unittest import mock

from ssds.admission.legality import Legality
from ssds.derivation.workflow import make
from ssds.ledger.read import with_id

from ._fixtures import record
from ._scenario import Scenario, agent, attested, submit
from .test_obligations import HUMANS, TWO, accept

FILES = {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"}


def enveloped(obligation: str, claims=()) -> dict:
    return {"binding": {"envelope": {"obligation_id": obligation}}, "claims": list(claims)}


def result(task: str, binding=None) -> dict:
    rec = record("TASK_RESULT", target={"task": task}, outcome="COMPLETE", actor=agent("maker"), actor_class="AGENT")
    if binding is not None:
        rec["binding"] = binding
    return with_id(rec)


class RequestLevel(unittest.TestCase):
    def setUp(self) -> None:
        self.sc = Scenario(TWO, dict(FILES), policy=HUMANS)

    def test_the_bound_obligation_exists_at_the_head(self) -> None:
        o = make("ACCEPT", self.sc.triple("arch"), holder="HUMAN")
        derived = Legality(self.sc.derive())
        self.assertIn(o.id, {x.id for x in derived.w.obligations})
        self.assertEqual(derived.request_codes(enveloped(o.id), []), set())
        self.sc.admit(*attested(accept(self.sc, "arch")))
        self.assertEqual(Legality(self.sc.derive()).request_codes(enveloped(o.id), []), {"OBLIGATION_NOT_DERIVED"},
                         "discharged since issue: no longer derived (F34)")

    def test_a_report_request_claims_nothing(self) -> None:
        o = make("ACCEPT", self.sc.triple("arch"), holder="HUMAN")
        legality = Legality(self.sc.derive())
        self.assertEqual(legality.request_codes(enveloped(o.id, [o.id]), []), {"OBLIGATION_CLAIM_UNSUPPORTED"})
        self.assertEqual(legality.request_codes(enveloped(o.id, [o.id]), [result("task-1")]), set())
        self.assertEqual(legality.request_codes({"binding": {"human": {}}, "claims": [o.id]}, []), set(),
                         "a human's request is no task's")

    def test_one_result_per_task(self) -> None:
        legality = Legality(self.sc.derive())
        self.assertEqual(legality.request_codes({}, [result("task-1"), result("task-2")]), set())
        self.assertEqual(legality.request_codes({}, [result("task-1"), {**result("task-1"), "id": "other"}]),
                         {"OBLIGATION_RESULT_DUPLICATE"})
        submit(self.sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        legality = Legality(self.sc.derive())
        self.assertEqual(legality.request_codes({}, [result("task-1")]), {"OBLIGATION_RESULT_DUPLICATE"})
        self.assertEqual(legality.request_codes({}, [result("task-9")]), set())

    def test_a_duplicate_discharge_is_rejected(self) -> None:
        o = make("ACCEPT", self.sc.triple("arch"), holder="HUMAN")
        legality = Legality(self.sc.derive())
        request = {"claims": [o.id]}
        self.assertEqual(legality.request_codes(request, []), set())
        for state, codes in (("DISCHARGED", {"OBLIGATION_DISCHARGED"}),
                             ("DISCHARGED_PROVISIONAL", {"OBLIGATION_DISCHARGED"}), ("REFUSED", set())):
            with self.subTest(state=state), mock.patch.object(legality.w, "discharge", lambda _o, v=state: v):
                self.assertEqual(legality.request_codes(request, []), codes)


class PerRecord(unittest.TestCase):
    """F31: a result bound to a discharged obligation or a contract revision not current is refused."""

    def setUp(self) -> None:
        self.sc = Scenario(TWO, dict(FILES), policy=HUMANS)
        self.o = make("ACCEPT", self.sc.triple("arch"), holder="HUMAN")

    def test_a_result_bound_to_a_discharged_obligation(self) -> None:
        legality = Legality(self.sc.derive())
        bound = result("task-1", {"obligation": self.o.id})
        self.assertEqual(legality.codes(bound), set())
        with mock.patch.object(legality.w, "discharge", lambda _o: "DISCHARGED"):
            self.assertEqual(legality.codes(bound), {"OBLIGATION_DISCHARGED"})
            self.assertEqual(legality.codes(result("task-1")), set(), "bound to nothing")
            review = with_id({**record("REVIEW", target={"subject": "arch"}, outcome="PASS"),
                              "binding": {"obligation": self.o.id}})
            self.assertEqual(legality.codes(review), set(), "results only")

    def test_a_result_naming_a_contract_revision_not_current(self) -> None:
        legality = Legality(self.sc.derive())
        current = {"unit": "impl", "rev": self.sc.rev("impl")}
        self.assertEqual(legality.codes(result("task-1", {"item": current})), set())
        self.assertEqual(legality.codes(result("task-1", {"item": {**current, "rev": "sha256:" + "0" * 64}})),
                         {"OBLIGATION_CONTRACT_STALE"})
        self.assertEqual(legality.codes(result("task-1", {"item": {"unit": "gone", "rev": current["rev"]}})),
                         {"OBLIGATION_CONTRACT_STALE"})


class Engine(unittest.TestCase):
    def test_a_report_request_claiming_a_discharge_is_rejected(self) -> None:
        from .test_admission_requests import RequestFixture, finding

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        issued = fixture.issue()
        claimed = fixture.obligation()
        decision = fixture.admit(fixture.signed(issued, [fixture.bind(finding(), issued)], claims=[claimed]))
        self.assertIn("OBLIGATION_CLAIM_UNSUPPORTED", decision.reasons)
        quiet = fixture.issue()
        plain = fixture.admit(fixture.signed(quiet, [fixture.bind(finding(note="x"), quiet)]))
        self.assertNotIn("OBLIGATION_CLAIM_UNSUPPORTED", plain.reasons)


    def test_a_stale_contract_refuses_the_result_in_the_authorization_loop(self) -> None:
        from .test_admission_requests import RequestFixture

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        issued = fixture.issue()
        task = issued.envelope["task_id"]
        bound = fixture.bind(record("TASK_RESULT", target={"task": task}, outcome="COMPLETE", fields={"slots": {}}),
                             issued)
        stale = with_id({**bound, "binding": {**bound["binding"], "item": {"unit": "guide", "rev": "sha256:" + "0" * 64}}})
        decision = fixture.admit(fixture.signed(issued, [stale]))
        self.assertEqual(dict(decision.refused).get(stale["id"]), ("OBLIGATION_CONTRACT_STALE",))


if __name__ == "__main__":
    unittest.main()
