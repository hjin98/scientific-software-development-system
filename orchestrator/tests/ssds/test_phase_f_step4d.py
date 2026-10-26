"""Phase F step 4d: validation step 5, dependency well-formedness (Manual §8.3 step 5, §8.5; catalogue §8.3 step 5,
§8.4, §3.4, §5.6; plan readings F22-F25).

The per-record decision (``dependency_codes``) is checked over histories the derivation scenario builder makes,
where a record's target can be admitted earlier; the request path runs the real Admission engine, where every
target a request can name is co-submitted until steps 6-8 let records through. ``CYCLE_SUPPORT`` is checked on the
static support graph's owner (``Support.grows_a_cycle``) and through the engine.
"""

from __future__ import annotations

import unittest

from ssds.admission.dependency import dependency_codes

from ._scenario import HUMAN, HUMAN_B, OWNER, Scenario, attested, challenge, content, judgment, validity
from .test_admission_requests import RequestFixture

THREE = '''
    [[unit]]
    id = "arch"
    kind = "D3"
    scope = [{ path = "arch.md" }]
    [[unit]]
    id = "impl"
    kind = "D4"
    scope = [{ path = "impl.md" }]
    [[unit]]
    id = "notes"
    kind = "D4"
    scope = [{ path = "notes.md" }]
'''

RESCOPED = THREE.replace('scope = [{ path = "arch.md" }]', 'scope = [{ path = "arch.md" }, { path = "arch2.md" }]')

#: ``p`` is a part of ``notes``; ``MOVED`` makes it a part of ``impl``, re-routing a ``validity`` entry on ``p``.
PARTED = THREE.replace('kind = "D4"\n    scope = [{ path = "impl.md" }]',
                       'kind = "D4"\n    role = "composite"\n    scope = [{ path = "impl.md" }]').replace(
    'kind = "D4"\n    scope = [{ path = "notes.md" }]',
    'kind = "D4"\n    role = "composite"\n    scope = [{ path = "notes.md" }]') + '''
    [[unit]]
    id = "p"
    subject = false
    part_of = "notes"
    scope = [{ file = "notes.md", heading = ["P"] }]
'''
MOVED = PARTED.replace('part_of = "notes"\n    scope = [{ file = "notes.md", heading = ["P"] }]',
                       'part_of = "impl"\n    scope = [{ file = "impl.md", heading = ["P"] }]')
PARTED_FILES = {"arch.md": "a1\n", "impl.md": "# I\ni\n# P\np\n", "notes.md": "# N\nn\n# P\np\n"}

FILES = {"arch.md": "a1\n", "impl.md": "i1\n", "notes.md": "n1\n"}


def accept(sc: Scenario, subject: str, actor: str = HUMAN, extra=(), outcome: str = "PASS") -> dict:
    t = sc.triple(subject)
    return judgment("ACCEPTANCE", t, outcome, actor=actor, basis=[content(subject, t["rev"]), *extra])


class TargetRules(unittest.TestCase):
    """A challenge-tier record's target: strictly earlier, of a kind §3.4 permits (F25)."""

    def setUp(self) -> None:
        self.sc = Scenario(THREE, dict(FILES))
        self.review = judgment("REVIEW", self.sc.triple("arch"), "PASS", actor=HUMAN_B)
        self.sc.admit(*attested(self.review))

    def codes(self, rec: dict, *earlier: dict) -> set[str]:
        """``rec``'s codes once admitted after ``earlier`` (each in its own entry)."""

        for e in earlier:
            self.sc.admit(e)
        self.sc.admit(rec)
        return dependency_codes(rec, self.sc.derive())

    def test_a_target_in_the_same_entry_is_not_strictly_earlier(self) -> None:
        c = challenge({"record": self.review["id"]})
        a = judgment("ADJUDICATION", {"record": c["id"]}, "UPHELD", actor=OWNER)
        self.sc.admit(c, a)
        self.assertEqual(dependency_codes(a, self.sc.derive()), {"DEP_TARGET_ORDER"})
        self.assertEqual(dependency_codes(c, self.sc.derive()), set(), "a support-tier target, earlier")

    def test_a_target_admitted_earlier_passes(self) -> None:
        c = challenge({"record": self.review["id"]})
        self.assertEqual(self.codes(judgment("ADJUDICATION", {"record": c["id"]}, "UPHELD", actor=OWNER), c), set())

    def test_a_target_admitted_later_is_out_of_order(self) -> None:
        c = challenge({"record": self.review["id"]})
        a = judgment("ADJUDICATION", {"record": c["id"]}, "UPHELD", actor=OWNER)
        self.sc.admit(a)
        self.sc.admit(c)
        self.assertEqual(dependency_codes(a, self.sc.derive()), {"DEP_TARGET_ORDER"})

    def test_a_challenge_of_a_challenge_is_a_counter_challenge(self) -> None:
        c = challenge({"record": self.review["id"]})
        self.assertEqual(self.codes(challenge({"record": c["id"]}, actor=OWNER), c), {"DEP_COUNTER_CHALLENGE"})

    def test_a_challenge_may_target_an_adjudication_or_override_but_not_a_withdrawal(self) -> None:
        c = challenge({"record": self.review["id"]})
        a = judgment("ADJUDICATION", {"record": c["id"]}, "UPHELD", actor=OWNER)
        self.assertEqual(self.codes(challenge({"record": a["id"]}, actor=HUMAN), c, a), set())
        r = judgment("RISK_OVERRIDE", {"record": c["id"]}, None, actor=OWNER,
                     fields={"continuation": {"subjects": ["arch"], "items": [], "kinds": []}})
        self.assertEqual(self.codes(challenge({"record": r["id"]}, actor=HUMAN), r), set())
        w = judgment("WITHDRAWAL", {"record": c["id"]}, None, actor=HUMAN_B)
        self.assertEqual(self.codes(challenge({"record": w["id"]}, actor=HUMAN), w), {"DEP_TARGET_KIND"})

    def test_an_adjudication_or_override_targets_a_challenge(self) -> None:
        self.assertEqual(self.codes(judgment("ADJUDICATION", {"record": self.review["id"]}, "UPHELD", actor=OWNER)),
                         {"DEP_TARGET_KIND"})
        override = judgment("RISK_OVERRIDE", {"record": self.review["id"]}, None, actor=OWNER,
                            fields={"continuation": {"subjects": ["arch"], "items": [], "kinds": []}})
        self.assertEqual(self.codes(override), {"DEP_TARGET_KIND"})

    def test_a_withdrawal_targets_its_own_actors_challenge(self) -> None:
        c = challenge({"record": self.review["id"]})  # raised by HUMAN_B
        self.assertEqual(self.codes(judgment("WITHDRAWAL", {"record": c["id"]}, None, actor=HUMAN_B), c), set())
        self.assertEqual(self.codes(judgment("WITHDRAWAL", {"record": c["id"]}, None, actor=HUMAN)), {"AUTH_ACTOR"},
                         "only the raiser withdraws")
        self.assertEqual(self.codes(judgment("WITHDRAWAL", {"record": self.review["id"]}, None, actor=HUMAN_B)),
                         {"DEP_TARGET_KIND"}, "a review is neither a challenge nor a report")

    def test_a_continuity_attestation_and_a_challenge_of_one_are_step_7s(self) -> None:
        attest = judgment("CONTINUITY_ATTESTATION", {"loss": "sha256:" + "a" * 64}, None, actor=OWNER,
                          fields={"scope_form": "COMPLEMENT", "listed": [], "evidence": []})
        self.assertEqual(dependency_codes(attest, self.sc.derive()), {"SCHEMA_UNSUPPORTED"})


class SubjectRules(unittest.TestCase):
    """``DEP_OWN_SUBJECT`` (F22) and ``DEP_CONSUMER`` (F23)."""

    REL = "<!-- ssds:rel DERIVED_FROM arch -->\n"

    def test_no_validity_entry_on_an_own_subject(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        own = accept(sc, "arch", extra=[validity("arch", sc.rev("arch"))])
        other = accept(sc, "arch", actor=HUMAN_B, extra=[validity("impl", sc.rev("impl"))])
        sc.admit(own, other)
        d = sc.derive()
        self.assertEqual(dependency_codes(own, d), {"DEP_OWN_SUBJECT"})
        self.assertEqual(dependency_codes(other, d), set())

    def test_an_own_subject_through_a_judged_record(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        review = judgment("REVIEW", sc.triple("arch"), "PASS", actor=HUMAN_B)
        sc.admit(*attested(review))
        c = judgment("CHALLENGE", {"record": review["id"]}, None, actor=HUMAN, basis=[validity("arch", sc.rev("arch"))],
                     fields={"blocking": True, "serious": False, "inquiry": "CONFIRMATORY"})
        sc.admit(c)
        self.assertEqual(dependency_codes(c, sc.derive()), {"DEP_OWN_SUBJECT"},
                         "a challenge judges what its target judges")

    def test_no_equivalence_relies_on_a_consumer_of_its_unit(self) -> None:
        sc = Scenario(THREE, {**FILES, "impl.md": self.REL + "i1\n"})
        r1 = sc.rev("arch")
        sc.absorb({"arch.md": "a2\n"})
        target = {"unit": "arch", "from": r1, "to": sc.rev("arch"), "class": "EDITORIAL"}
        consumer = judgment("EQUIVALENCE", target, "EQUIVALENT", basis=[validity("impl", sc.rev("impl"))])
        unrelated = judgment("EQUIVALENCE", target, "EQUIVALENT", actor=HUMAN_B,
                             basis=[validity("notes", sc.rev("notes"))])
        sc.admit(consumer, unrelated)
        d = sc.derive()
        self.assertEqual(d.s.s0.consumers("arch"), frozenset({"impl"}))
        self.assertEqual(dependency_codes(consumer, d), {"DEP_CONSUMER"})
        self.assertEqual(dependency_codes(unrelated, d), set())

    def test_a_unit_of_a_consumers_subject_is_a_consumer(self) -> None:
        files = {**PARTED_FILES, "notes.md": "# N\nn\n# P\n" + self.REL + "p\n"}
        sc = Scenario(PARTED, files)
        r1 = sc.rev("arch")
        sc.absorb({"arch.md": "a2\n"})
        target = {"unit": "arch", "from": r1, "to": sc.rev("arch"), "class": "EDITORIAL"}
        on_subject = judgment("EQUIVALENCE", target, "EQUIVALENT", basis=[validity("notes", sc.rev("notes"))])
        sc.admit(on_subject)
        d = sc.derive()
        self.assertEqual(d.s.s0.consumers("arch"), frozenset({"p", "notes"}))
        self.assertEqual(dependency_codes(on_subject, d), {"DEP_CONSUMER"}, "a validity entry relies on valid(subj)")


class StaticCycles(unittest.TestCase):
    """``CYCLE_SUPPORT`` (F24): the static graph's components may not appear or grow; one already there blocks
    nothing else."""

    def mutual(self) -> tuple[Scenario, dict, dict]:
        sc = Scenario(THREE, dict(FILES))
        ja = accept(sc, "arch", extra=[validity("impl", sc.rev("impl"))])
        jb = accept(sc, "impl", actor=HUMAN_B, extra=[validity("arch", sc.rev("arch"))])
        return sc, ja, jb

    def test_a_mutual_acceptance_makes_a_cycle(self) -> None:
        sc, ja, jb = self.mutual()
        before = sc.derive()
        sc.admit(ja, jb)
        after = sc.derive()
        self.assertEqual(len(after.static_forced), 1)
        self.assertTrue(after.grows_a_cycle(before))
        self.assertFalse(after.grows_a_cycle(after), "the same graph grows nothing")

    def test_an_existing_cycle_blocks_no_unrelated_record(self) -> None:
        sc, ja, jb = self.mutual()
        sc.admit(ja, jb)
        before = sc.derive()
        sc.admit(accept(sc, "notes", extra=[validity("arch", sc.rev("arch"))]))
        self.assertFalse(sc.derive().grows_a_cycle(before), "it relies on the cycle without joining it")

    def test_a_record_joining_the_cycle_grows_it(self) -> None:
        sc, ja, jb = self.mutual()
        sc.admit(ja, jb)
        before = sc.derive()
        sc.admit(accept(sc, "arch", actor=OWNER, extra=[validity("impl", sc.rev("impl"))]))
        after = sc.derive()
        self.assertTrue(after.grows_a_cycle(before))
        self.assertEqual(len(after.static_forced), 1, "one larger component")

    def test_a_second_disjoint_cycle_appears(self) -> None:
        sc, ja, jb = self.mutual()
        sc.admit(ja)
        before = sc.derive()
        sc.admit(jb)
        self.assertTrue(sc.derive().grows_a_cycle(before))

    def test_the_static_graph_keeps_what_evaluation_drops(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        failing = accept(sc, "arch", extra=[validity("impl", sc.rev("impl"))], outcome="FAIL")
        jb = accept(sc, "impl", actor=HUMAN_B, extra=[validity("arch", sc.rev("arch"))])
        sc.admit(failing, jb)
        d = sc.derive()
        self.assertEqual(d.forced, (), "a failing acceptance makes no evaluation edge")
        self.assertEqual(len(d.static_forced), 1, "an acceptance, whatever its value, is a static edge (§5.6)")

    def test_a_gate_decision_on_a_stale_triple_is_a_static_edge(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        stale = sc.triple("arch")
        decision = judgment("GATE_DECISION", {"gate": "design-gate", "subject": stale, "core": "sha256:" + "c" * 64},
                            "ACCEPT", basis=[content("arch", stale["rev"]), validity("impl", sc.rev("impl"))],
                            fields={"adequacy": "ADEQUATE", "qualification": "UNQUALIFIED"})
        sc.absorb({"arch.md": "a2\n"})
        jb = accept(sc, "impl", actor=HUMAN_B, extra=[validity("arch", sc.rev("arch"))])
        sc.admit(decision, jb)
        d = sc.derive()
        self.assertEqual(d.forced, (), "a decision on a stale triple makes no evaluation edge")
        self.assertEqual(len(d.static_forced), 1, "every gate decision naming the subject (§5.6 item 2)")

    def test_every_equivalence_on_a_named_unit_is_a_static_edge(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        r1 = sc.rev("impl")
        sc.absorb({"impl.md": "i2\n"})
        ja = accept(sc, "arch", extra=[content("impl", sc.rev("impl"))])
        refused = judgment("EQUIVALENCE", {"unit": "impl", "from": r1, "to": sc.rev("impl"), "class": "EDITORIAL"},
                           "NOT_EQUIVALENT", actor=HUMAN_B, basis=[validity("arch", sc.rev("arch"))])
        sc.admit(ja, refused)
        d = sc.derive()
        self.assertEqual(d.forced, (), "a refused equivalence satisfies nothing, so evaluation has no edge to it")
        self.assertEqual(len(d.static_forced), 1, "every equivalence judgment on a named unit (§5.6)")

    def test_an_ended_tenures_acceptance_is_no_static_edge(self) -> None:
        from ._scenario import agent, integrate, submit

        sc, ja, jb = self.mutual()
        sc.admit(ja, jb)
        self.assertEqual(len(sc.derive().static_forced), 1)
        x, candidate, _ = submit(sc, {"arch2.md": "b\n"}, agent("maker"), "task-1", manifest=RESCOPED)
        integrate(sc, x, candidate)
        self.assertEqual(sc.derive().static_forced, (), "arch's tenure restarted after ja: it can never count again")

    def test_a_pending_frames_acceptance_stays_a_static_edge(self) -> None:
        from ssds.derivation.frames import Frame, transformation_of

        from ._scenario import agent, integrate, submit

        sc = Scenario(THREE, dict(FILES))
        jb = accept(sc, "impl", actor=HUMAN_B, extra=[validity("arch", sc.rev("arch"))])
        sc.admit(jb)
        x1, _, _ = submit(sc, {"notes.md": "n2\n"}, agent("maker"), "task-1")
        state = sc.derive().s
        view = Frame(state.h, state.n, transformation_of(state, x1), state.enactment(x1)).view
        rev = view.rev("arch")
        j = judgment("ACCEPTANCE", {"subject": "arch", "scope_id": view.scope_id("arch"), "rev": rev}, "PASS",
                     basis=[content("arch", rev), validity("impl", view.rev("impl"))], frame={"transformation": x1})
        sc.admit(j)
        x2, candidate, _ = submit(sc, {"arch2.md": "b\n"}, agent("maker"), "task-2", manifest=RESCOPED)
        integrate(sc, x2, candidate)
        d = sc.derive()
        self.assertGreater(d.s.tenure("arch"), d.s.position_of(j["id"]))
        self.assertEqual(len(d.static_forced), 1, "x1 may yet integrate, so j may yet count (check 87e908d)")
        self.assertIn(("current", j["id"]), d.static_forced[0])


class FrameCycles(unittest.TestCase):
    """A request changing structure is read in its frame, where ``subj`` re-routes ``validity`` entries (F24): ``p``
    moving from ``notes`` to ``impl`` closes ``arch -> impl -> arch``."""

    def setUp(self) -> None:
        self.sc = Scenario(PARTED, dict(PARTED_FILES))
        self.sc.admit(self.accept("arch", HUMAN, "p"), self.accept("impl", HUMAN_B, "arch"))

    def accept(self, subject: str, actor: str, unit: str) -> dict:
        return accept(self.sc, subject, actor=actor, extra=[validity(unit, self.sc.rev(unit))])

    def test_a_records_only_adoption_that_re_routes_into_a_cycle(self) -> None:
        from ssds.content import decl_to_json
        from ssds.derivation import adoption_codes

        from .test_phase_f_step4c import _decl_value

        self.assertEqual(self.sc.derive().static_forced, ())
        self.sc.manifest = MOVED
        self.sc.absorb({})
        d = self.sc.derive()
        elements = []
        for key in (("p", "part_of"), ("p", "scope")):
            absorption, value = d.s.current_delta(key)
            elements.append({"absorption": absorption, "key": list(key),
                             "value": _decl_value(decl_to_json({key: value}), key)})
        named = {(e["absorption"], tuple(e["key"])) for e in elements}
        self.assertEqual(d.static_forced, (), "Σ is unchanged until the adoption")
        self.assertEqual(adoption_codes(d.s, self.sc.head, elements, named), {"CYCLE_SUPPORT"})

    def test_an_integration_that_re_routes_into_a_cycle(self) -> None:
        from ssds.admission.engine import integration_codes

        from ._scenario import agent, submit

        _, candidate, _ = submit(self.sc, {}, agent("maker"), "task-1", manifest=MOVED)
        binding = {"envelope": {"task_id": "task-1"}}
        self.assertIn("CYCLE_SUPPORT", integration_codes(candidate, self.sc.derive(), binding))
        _, other, _ = submit(self.sc, {"notes.md": "# N\nn2\n# P\np\n"}, agent("maker"), "task-2")
        self.assertNotIn("CYCLE_SUPPORT", integration_codes(other, self.sc.derive(), {"envelope": {"task_id": "task-2"}}),
                         "a frame that re-routes nothing")


class Requests(RequestFixture):
    """Step 5 through the engine: a refusal removes the record before the trial is rebuilt."""

    def human_request(self, records):
        from ssds.admission.request import request_message

        from ._fixtures import sshsig

        req = self.request(records, base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return req

    def challenge_of(self, target: dict) -> dict:
        from ssds.ledger.read import with_id

        from ._fixtures import record

        return with_id({**record("CHALLENGE", target=target, fields={
            "blocking": True, "serious": False, "inquiry": "EXPLORATORY", "materiality": "MATERIAL"}),
            "actor": self.human()})

    def test_a_co_submitted_counter_challenge_is_refused(self) -> None:
        from .test_phase_f_step4b import derive_state

        subject, scope, rev = derive_state(self).subject_triple("guide")
        c = self.challenge_of({"subject": subject, "scope_id": scope, "rev": rev})
        counter = self.challenge_of({"record": c["id"]})
        refused = dict(self.admit(self.human_request([c, counter])).refused)
        self.assertEqual(refused.get(counter["id"]), ("DEP_COUNTER_CHALLENGE", "DEP_TARGET_ORDER"))
        self.assertEqual(refused.get(c["id"]), ("SCHEMA_UNSUPPORTED",),
                         "its target passes step 5; a never-lost record still fails closed at steps 6-8")

    def test_a_mutual_acceptance_request_is_stale_at_an_empty_head(self) -> None:
        """Each acceptance relies on a subject no acceptance at the head makes valid, so step 6 refuses both before
        their cycle can form (step 4e-ii); the request-level reading is driven in test_phase_f_step4e."""

        from ssds.ledger.read import with_id

        from ._fixtures import record
        from .test_phase_f_step4b import derive_state

        state = derive_state(self)
        guide, policy = state.subject_triple("guide"), state.subject_triple("ssds.policy")

        def acceptance(triple, other) -> dict:
            subject, scope, rev = triple
            return with_id({**record("ACCEPTANCE", target={"subject": subject, "scope_id": scope, "rev": rev},
                                     outcome="PASS", basis=[content(subject, rev), validity(other[0], other[2])]),
                            "actor": self.human()})

        pair = [acceptance(guide, policy), acceptance(policy, guide)]
        decision = self.admit(self.human_request(pair))
        self.assertNotIn("CYCLE_SUPPORT", decision.reasons, decision)
        self.assertEqual({rid: why for rid, why in decision.refused}, {r["id"]: ("STALE_BASIS",) for r in pair})


if __name__ == "__main__":
    unittest.main()
