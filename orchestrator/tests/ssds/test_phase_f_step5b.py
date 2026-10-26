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
        self.assertEqual(legality.request_codes({**enveloped(o.id, [o.id]), "candidates": ["0" * 40]}, []), set(),
                         "an integration request claims with its admitted result (§11.5 (3))")

    def test_one_result_per_task(self) -> None:
        legality = Legality(self.sc.derive())
        self.assertEqual(legality.request_codes({}, [result("task-1"), result("task-2")]), set())
        self.assertEqual(legality.request_codes({}, [result("task-1"), {**result("task-1"), "id": "other"}]),
                         {"OBLIGATION_RESULT_DUPLICATE"})
        submit(self.sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        legality = Legality(self.sc.derive())
        self.assertEqual(legality.request_codes({}, [result("task-1")]), {"OBLIGATION_RESULT_DUPLICATE"})
        self.assertEqual(legality.request_codes({}, [result("task-9")]), set())
        bound = {**result("task-9"), "binding": {"task": "task-1"}}
        self.assertEqual(legality.request_codes({}, [bound]), {"OBLIGATION_RESULT_DUPLICATE"},
                         "the bound task, not the target's (review fed5d82 B1)")

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


def step7(sc: Scenario, rec: dict) -> set[str]:
    """``rec``'s step 7 per-record codes at ``sc``'s head, its frame located as step 6 locates it."""

    from ssds.admission.currency import Currency

    from .test_phase_f_step4e import tried

    head = sc.derive()
    return Legality(head, Currency(head).locate).codes(rec, tried(sc, [rec]))


class Answered(unittest.TestCase):
    """Step 5b-ii: once answered (§10.3), a later passing judgment bound to the obligation is refused."""

    def setUp(self) -> None:
        from ._scenario import HUMAN, judgment

        from .test_obligations import content

        self.sc = Scenario(TWO, dict(FILES), policy=HUMANS)
        self.o = make("ACCEPT", self.sc.triple("arch"), holder="HUMAN")
        t = self.sc.triple("arch")
        self.adverse = judgment("ACCEPTANCE", t, "FAIL", actor=HUMAN, basis=[content("arch", t["rev"])])

    def bound(self, supersedes=(), kind="ACCEPTANCE", outcome="PASS", target=None) -> dict:
        from ._scenario import HUMAN_B, judgment

        from .test_obligations import content

        t = self.sc.triple("arch")
        rec = judgment(kind, target or t, outcome, actor=HUMAN_B, basis=[content("arch", t["rev"])],
                       supersedes=supersedes)
        return with_id({**rec, "binding": {"obligation": self.o.id}})

    def test_a_later_passing_judgment_is_refused_once_answered(self) -> None:
        self.assertEqual(step7(self.sc, self.bound()), set(), "nothing answers it yet")
        self.sc.admit(*attested(self.adverse))
        self.assertEqual(step7(self.sc, self.bound()), {"OBLIGATION_ANSWERED"})

    def test_a_supersession_and_a_gate_decision_are_exempt(self) -> None:
        self.sc.admit(*attested(self.adverse))
        self.assertEqual(step7(self.sc, self.bound(supersedes=[self.adverse["id"]])), set())
        gate = self.bound(kind="GATE_DECISION", outcome="ACCEPT",
                          target={"gate": "g", "subject": self.sc.triple("arch"), "core": "sha256:" + "c" * 64})
        self.assertNotIn("OBLIGATION_ANSWERED", step7(self.sc, gate))

    def test_only_a_passing_judgment_is_refused(self) -> None:
        from ._scenario import OWNER, judgment

        self.sc.admit(*attested(self.adverse))
        override = with_id({**judgment("IMMATERIALITY", {"records": [self.adverse["id"]]}, "PENDING", actor=OWNER),
                            "binding": {"obligation": self.o.id}})
        self.assertEqual(step7(self.sc, override), set(), "neither passing nor never-lost")

    def test_an_adverse_judgment_is_never_refused(self) -> None:
        self.sc.admit(*attested(self.adverse))
        self.assertEqual(step7(self.sc, self.bound(outcome="FAIL")), set())


class RevisionAssessmentsFirst(unittest.TestCase):
    """Step 5b-ii: a passing acceptance or gate decision on a NATIVE D1/D2 triple needs a counting revision
    assessment already admitted and a ``standing`` entry on it (§10.2; ``OBLIGATION_REVIEW_OPEN``)."""

    def test_an_acceptance_needs_its_counting_premise(self) -> None:
        from ._scenario import OWNER

        from .test_runs import MANIFEST, NO_GATE, RUN_FILES, accept as run_accept, author, gate

        sc = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        r1 = author(sc, "v1\n", "task-1")
        self.assertEqual(step7(sc, run_accept(sc, r1["id"])), set())
        self.assertEqual(step7(sc, run_accept(sc, None)), {"OBLIGATION_REVIEW_OPEN"}, "no standing entry")
        self.assertEqual(step7(sc, gate(sc, r1["id"], OWNER)), set())
        unrelated = {**run_accept(sc, None), "basis": run_accept(sc, None)["basis"] + [
            {"mode": "standing", "target": {"record": "sha256:" + "9" * 64}, "class": "EXACT"}]}
        self.assertEqual(step7(sc, unrelated), {"OBLIGATION_REVIEW_OPEN"}, "a standing entry on no assessment")

    def test_an_assessment_of_another_revision_counts_for_nothing(self) -> None:
        from .test_runs import MANIFEST, NO_GATE, RUN_FILES, accept as run_accept, author

        sc = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        r1 = author(sc, "v1\n", "task-1")
        author(sc, "v2\n", "task-2")  # a later revision: r1 assesses a revision no longer current
        stale = run_accept(sc, r1["id"])
        self.assertEqual(step7(sc, stale), {"OBLIGATION_REVIEW_OPEN"})

    def test_an_assessment_that_does_not_stand_or_is_out_of_run_counts_for_nothing(self) -> None:
        from ._scenario import challenge

        from .test_runs import MANIFEST, NO_GATE, RUN_FILES, accept as run_accept, author

        sc = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        r1 = author(sc, "v1\n", "task-1")
        sc.admit(*attested(challenge({"record": r1["id"]})))
        self.assertEqual(sc.derive().base(r1["id"]), 0, "a blocking challenge: it does not stand")
        self.assertEqual(step7(sc, run_accept(sc, r1["id"])), {"OBLIGATION_REVIEW_OPEN"})
        reverted = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        first = author(reverted, "v1\n", "task-1")
        author(reverted, "v2\n", "task-2")
        author(reverted, "v1\n", "task-3", obligation="other")  # the bytes are back, in a new run
        self.assertEqual(step7(reverted, run_accept(reverted, first["id"])), {"OBLIGATION_REVIEW_OPEN"},
                         "an earlier run's assessment of the same bytes")

    def test_a_gate_decision_needs_it_too_and_a_legacy_subject_does_not(self) -> None:
        from ._scenario import OWNER, judgment

        from .test_runs import MANIFEST, NO_GATE, RUN_FILES, author

        sc = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE)
        author(sc, "v1\n", "task-1")
        t = sc.triple("numerics")
        bare = judgment("GATE_DECISION", {"gate": "d2-gate", "subject": t, "core": "sha256:" + "c" * 64}, "ACCEPT",
                        actor=OWNER, basis=[{"mode": "content", "target": {"unit": "numerics", "rev": t["rev"]},
                                             "class": "EXACT"}],
                        fields={"adequacy": "ADEQUATE", "qualification": "UNQUALIFIED"})
        self.assertEqual(step7(sc, bare), {"OBLIGATION_REVIEW_OPEN"}, "its triple is the target's subject")
        legacy = Scenario(MANIFEST, RUN_FILES, policy=NO_GATE,
                          modes={"numerics": {"mode": "LEGACY", "ruleset": "ssds-rules/1"}})
        self.assertEqual(step7(legacy, {**bare, "target": {**bare["target"], "subject": legacy.triple("numerics")}}),
                         set(), "a LEGACY subject owes no SSDS acceptance order")

    def test_a_d3_subject_needs_none(self) -> None:
        from ._scenario import HUMAN, judgment

        from .test_obligations import content

        sc = Scenario(TWO, dict(FILES), policy=HUMANS)
        t = sc.triple("arch")
        self.assertEqual(step7(sc, judgment("ACCEPTANCE", t, "PASS", actor=HUMAN, basis=[content("arch", t["rev"])])),
                         set())


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


    def test_a_contract_the_envelope_does_not_name_is_refused(self) -> None:
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
        self.assertEqual(dict(decision.refused).get(stale["id"]), ("AUTH_ENVELOPE",),
                         "the envelope names no contract revision (review fed5d82 B3)")


    def test_a_result_is_bound_to_its_envelopes_contract_and_task(self) -> None:
        """Review fed5d82 B1, B3: the contract revision and the task a result names are the envelope's."""

        from .test_admission_requests import RequestFixture

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        from .test_phase_f_step4b import derive_state

        rev = derive_state(fixture).subject_triple("guide")[2]
        stale = {"unit": "guide", "rev": "sha256:" + "0" * 64}
        head = len(fixture.entries()) - 1
        issued = fixture.issuer.issue(task_id=f"task-{head}-C", obligation_id=fixture.obligation(), role="REVIEWER",
                                      contract_revision=stale, governs={"mode": "LEGACY", "protocol": "7.2.1"},
                                      route="HARNESS", issued_at_position=head)
        task = issued.envelope["task_id"]

        def bound(item, target_task=task):
            rec = fixture.bind(record("TASK_RESULT", target={"task": target_task}, outcome="COMPLETE",
                                      fields={"slots": {}}), issued)
            return with_id({**rec, "binding": {**rec["binding"], "item": item}})

        claimed_current = bound({"unit": "guide", "rev": rev})
        self.assertEqual(dict(fixture.admit(fixture.signed(issued, [claimed_current])).refused).get(
            claimed_current["id"]), ("AUTH_ENVELOPE",), "a self-declared current revision")
        honest = bound(stale)
        self.assertEqual(dict(fixture.admit(fixture.signed(issued, [honest])).refused).get(honest["id"]),
                         ("OBLIGATION_CONTRACT_STALE",))
        elsewhere = bound(stale, "task-other")
        self.assertIn("AUTH_ENVELOPE", dict(fixture.admit(fixture.signed(issued, [elsewhere])).refused).get(
            elsewhere["id"]), "another task's result")


    def test_an_answered_obligation_refuses_a_later_passing_judgment_through_the_engine(self) -> None:
        """A rejection salvages an adverse acceptance (5a), which answers the obligation (§10.3); a passing one
        bound to it afterwards is refused in the authorization loop (5b-ii)."""

        from ssds.admission.request import request_message

        from ._fixtures import sshsig
        from .test_admission_requests import RequestFixture
        from .test_phase_f_step4b import derive_state

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        obligation = fixture.obligation()
        subject, scope, rev = derive_state(fixture).subject_triple("guide")
        triple = {"subject": subject, "scope_id": scope, "rev": rev}
        content = [{"mode": "content", "target": {"unit": "guide", "rev": rev}, "class": "EXACT"}]
        adverse = with_id({**record("ACCEPTANCE", target=triple, outcome="FAIL", basis=content),
                           "actor": fixture.human()})
        req = fixture.request([adverse], base_position=len(fixture.entries()) - 1)
        req["binding"] = {"human": {"actor": fixture.human(), "signature": sshsig(fixture.private, request_message(req))}}
        self.assertIn(adverse["id"], fixture.admit(req).admitted)
        issued = fixture.issue()
        passing_ = fixture.bind(record("ACCEPTANCE", target=triple, outcome="PASS", basis=content), issued)
        self.assertEqual(passing_["binding"]["obligation"], obligation)
        refused = dict(fixture.admit(fixture.signed(issued, [passing_])).refused)
        self.assertIn("OBLIGATION_ANSWERED", refused.get(passing_["id"], ()), refused)


if __name__ == "__main__":
    unittest.main()
