"""Phase F step 4e-i: the structure-changing trial (Manual §7.4, §8.3 steps 3-6; catalogue §8.3; plan reading F27).

A request carrying a candidate or adoptions is judged in the state after it: the trial entry integrates ``X`` with
``M_n(X)`` as its tree, or adopts ``A``, and carries ``Σ_n → Σ_{n+1}``. No request is admitted until steps 6-8, so
no head result fixes an ``X`` and no head key is quarantined through the engine: the trial is checked on derivation
histories, against the state a real integration derives, and the engine's wiring by the frame it passes.
"""

from __future__ import annotations

import unittest
from unittest import mock

from ssds.admission.authorize import _acceptance_target
from ssds.admission.dependency import dependency_codes
from ssds.derivation import Frame, adoption_frame, trial
from ssds.derivation.extension import TRIAL_TREE
from ssds.derivation.frames import transformation_of

from ._fixtures import admission_body, chain_of, record
from ._scenario import HUMAN, HUMAN_B, Scenario, agent, content, integrate, judgment, submit, validity
from .test_phase_f_step4d import FILES, MOVED, PARTED, PARTED_FILES, RESCOPED, THREE


def frame_of_candidate(sc: Scenario, x: str) -> Frame:
    s = sc.derive().s
    return Frame(s.h, s.n, transformation_of(s, x), s.enactment(x))


def tried(sc: Scenario, records=(), frame=None):
    """The trial of an entry carrying ``records`` after ``sc``'s head, after ``frame``'s change when given."""

    entry = admission_body(sc.position, sc.head, sc.head, records=list(records))
    return trial(chain_of("demo", sc.entries, sc.objects), sc.trees.__getitem__, entry, None, frame)


class Trial(unittest.TestCase):
    def test_an_integrations_trial_is_the_state_its_admission_derives(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        x, candidate, _ = submit(sc, {"arch2.md": "b\n", "impl.md": "i2\n"}, agent("maker"), "task-1",
                                 manifest=RESCOPED)
        frame = frame_of_candidate(sc, x)
        self.assertTrue(frame.exists)
        a = tried(sc, frame=frame).s
        integrate(sc, x, candidate)
        b = sc.derive().s
        self.assertEqual(a.n, b.n)
        self.assertEqual(dict(a.h.sigma(a.n)), dict(b.h.sigma(b.n)))
        self.assertEqual(a.h.head(a.n), TRIAL_TREE)
        self.assertEqual(a.integrated, b.integrated)
        self.assertEqual({u: a.view.rev(u) for u in a.view.structure.units},
                         {u: b.view.rev(u) for u in b.view.structure.units})
        self.assertEqual(a.subject_triple("arch"), b.subject_triple("arch"))
        self.assertEqual(a.tenure("arch"), b.tenure("arch"))

    def test_the_entry_records_every_changed_key_and_its_source(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        x, _, _ = submit(sc, {"arch2.md": "b\n"}, agent("maker"), "task-1", manifest=RESCOPED)
        deltas = frame_of_candidate(sc, x).entry_deltas()
        self.assertEqual([(d["key"], d["source"]) for d in deltas], [(["arch", "scope"], "AUTHORED")])
        self.assertEqual(frame_of_candidate(sc, submit(sc, {"notes.md": "n2\n"}, agent("maker"), "task-2")[0])
                         .entry_deltas(), [], "a content-only change carries no delta")

    def test_an_adoptions_trial_adopts_and_keeps_the_tree(self) -> None:
        from ssds.content import decl_to_json

        from .test_phase_f_step4c import _decl_value

        sc = Scenario(PARTED, dict(PARTED_FILES))
        sc.manifest = MOVED
        sc.absorb({})
        s = sc.derive().s
        elements = []
        for key in (("p", "part_of"), ("p", "scope")):
            absorption, value = s.current_delta(key)
            elements.append({"absorption": absorption, "key": list(key),
                             "value": _decl_value(decl_to_json({key: value}), key)})
        frame = adoption_frame(s, sc.head, elements)
        self.assertEqual({(tuple(d["key"]), d["source"]) for d in frame.entry_deltas()},
                         {(("p", "part_of"), "ADOPTED"), (("p", "scope"), "ADOPTED")})
        a = tried(sc, frame=frame).s
        self.assertEqual(a.h.head(a.n), sc.head, "no tree change")
        self.assertEqual(a.integrated, s.integrated, "an adoption integrates nothing")
        self.assertEqual(a.view.structure.subj("p"), "impl")
        self.assertEqual(s.view.structure.subj("p"), "notes")

    def test_an_adoption_frame_needs_well_formed_elements(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        s = sc.derive().s
        for elements in (None, [], [{"key": ["arch", "scope"]}], [{"absorption": "a", "key": "arch", "value": 1}],
                         [{"absorption": "a", "key": ["arch", "scope"], "value": "not a scope"}]):
            with self.subTest(elements=elements):
                self.assertIsNone(adoption_frame(s, sc.head, elements))


class StepsReadTheFrame(unittest.TestCase):
    """Steps 3 and 5 read the request's records in ``Σ_{n+1}`` (F27; review 2981f738 N2)."""

    def test_an_acceptance_is_judged_against_the_frames_triple(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        x, _, _ = submit(sc, {"arch2.md": "b\n"}, agent("maker"), "task-1", manifest=RESCOPED)
        frame = frame_of_candidate(sc, x)
        at_head = judgment("ACCEPTANCE", sc.triple("arch"), "PASS", basis=[content("arch", sc.rev("arch"))])
        in_frame_triple = {"subject": "arch", "scope_id": frame.view.scope_id("arch"), "rev": frame.view.rev("arch")}
        in_frame = judgment("ACCEPTANCE", in_frame_triple, "PASS", basis=[content("arch", in_frame_triple["rev"])])
        self.assertEqual(_acceptance_target(at_head, tried(sc, [at_head])), set())
        self.assertEqual(_acceptance_target(at_head, tried(sc, [at_head], frame)), {"AUTH_TARGET_NOT_CURRENT"})
        self.assertEqual(_acceptance_target(in_frame, tried(sc, [in_frame], frame)), set())

    def test_a_validity_entry_on_a_unit_moved_into_the_records_subject_is_its_own(self) -> None:
        sc = Scenario(PARTED, dict(PARTED_FILES))
        x, _, _ = submit(sc, {}, agent("maker"), "task-1", manifest=MOVED)
        frame = frame_of_candidate(sc, x)
        t = sc.triple("impl")
        rec = judgment("REVIEW", t, "PASS", actor=HUMAN, basis=[content("impl", t["rev"]), validity("p", sc.rev("p"))])
        self.assertEqual(dependency_codes(rec, tried(sc, [rec])), set(), "p is notes' part at the head")
        self.assertEqual(dependency_codes(rec, tried(sc, [rec], frame)), {"DEP_OWN_SUBJECT"}, "and impl's after X")


class FrameRecordsActInTheirFrame(unittest.TestCase):
    """Review cab6179a B1: a record declaring an unintegrated ``X`` acts in ``X``'s frame, so step 5 reads its own
    subjects there whichever trial judges it, the head's (salvage) included."""

    def test_at_the_head_too(self) -> None:
        sc = Scenario(PARTED, dict(PARTED_FILES))
        x, _, _ = submit(sc, {}, agent("maker"), "task-1", manifest=MOVED)
        frame = frame_of_candidate(sc, x)
        t = {"subject": "impl", "scope_id": frame.view.scope_id("impl"), "rev": frame.view.rev("impl")}
        framed = judgment("REVIEW", t, "NO_PASS", basis=[content("impl", t["rev"]), validity("p", frame.view.rev("p"))],
                          frame={"transformation": x})
        self.assertEqual(dependency_codes(framed, tried(sc, [framed])), {"DEP_OWN_SUBJECT"})
        admitted = judgment("REVIEW", sc.triple("impl"), "NO_PASS",
                            basis=[content("impl", sc.rev("impl")), validity("p", sc.rev("p"))])
        self.assertEqual(dependency_codes(admitted, tried(sc, [admitted])), set(), "it acts at the head")


class Currency(unittest.TestCase):
    """Step 4e-ii: each basis entry on the head's ``Support`` in the record's frame; satisfied when not ``F`` (F26)."""

    def codes(self, sc: Scenario, rec: dict, change=None, siblings=()) -> set[str]:
        from ssds.admission.currency import Currency as Step6

        return Step6(sc.derive(), change).codes(rec, tried(sc, [*siblings, rec]))

    def review(self, sc: Scenario, *basis, outcome: str = "PASS", **extra) -> dict:
        t = sc.triple("impl")
        return judgment("REVIEW", t, outcome, actor=HUMAN_B, basis=[content("impl", t["rev"]), *basis], **extra)

    def test_a_content_entry_on_a_superseded_revision_is_stale(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        r1 = sc.rev("arch")
        self.assertEqual(self.codes(sc, self.review(sc, content("arch", r1))), set())
        sc.absorb({"arch.md": "a2\n"})
        self.assertEqual(self.codes(sc, self.review(sc, content("arch", r1))), {"STALE_BASIS"})

    def test_an_equivalence_at_the_head_covers_its_class(self) -> None:
        from ._scenario import OWNER, attested

        sc = Scenario(THREE, dict(FILES))
        r1 = sc.rev("arch")
        sc.absorb({"arch.md": "a1 \n"})
        r2 = sc.rev("arch")
        eq = judgment("EQUIVALENCE", {"unit": "arch", "from": r1, "to": r2, "class": "EDITORIAL"}, "EQUIVALENT",
                      actor=OWNER, basis=[{"mode": "identity", "target": {"unit": "arch", "rev": r1}, "class": "EXACT"},
                                          {"mode": "identity", "target": {"unit": "arch", "rev": r2}, "class": "EXACT"}])
        sc.admit(*attested(eq))
        self.assertEqual(self.codes(sc, self.review(sc, content("arch", r1, "EDITORIAL"))), set())
        self.assertEqual(self.codes(sc, self.review(sc, content("arch", r1))), {"STALE_BASIS"}, "EXACT is never covered")

    def test_a_validity_entry_needs_a_valid_subject_and_provisional_suffices(self) -> None:
        from ._scenario import OWNER, attested, challenge

        sc = Scenario(THREE, dict(FILES))
        entry = validity("arch", sc.rev("arch"))
        self.assertEqual(self.codes(sc, self.review(sc, entry)), {"STALE_BASIS"}, "no acceptance: invalid")
        t = sc.triple("arch")
        acc = judgment("ACCEPTANCE", t, "PASS", basis=[content("arch", t["rev"])])
        sc.admit(*attested(acc))
        self.assertEqual(self.codes(sc, self.review(sc, entry)), set())
        c = challenge({"record": acc["id"]})
        sc.admit(*attested(c))
        self.assertEqual(self.codes(sc, self.review(sc, entry)), {"STALE_BASIS"}, "a blocking challenge stands")
        sc.admit(*attested(judgment("RISK_OVERRIDE", {"record": c["id"]}, None, actor=OWNER,
                                    fields={"continuation": {"subjects": ["arch"], "items": [], "kinds": []}})))
        self.assertEqual(sc.derive().valid("arch"), 1)
        self.assertEqual(self.codes(sc, self.review(sc, entry)), set(), "P is satisfied (F26)")

    def test_a_record_entry_on_a_co_submitted_record_is_stale(self) -> None:
        from ._scenario import attested, on_record

        sc = Scenario(THREE, dict(FILES))
        earlier = judgment("REVIEW", sc.triple("arch"), "PASS", actor=HUMAN)
        sibling = judgment("REVIEW", sc.triple("notes"), "PASS", actor=HUMAN)
        self.assertEqual(self.codes(sc, self.review(sc, on_record(sibling["id"])), siblings=[sibling]),
                         {"STALE_BASIS"}, "no node at the head (F10)")
        sc.admit(*attested(earlier))
        self.assertEqual(self.codes(sc, self.review(sc, on_record(earlier["id"]))), set())

    def test_a_record_entry_on_an_admitted_record_that_is_no_node_is_stale(self) -> None:
        """Review 8408e05 B1: a report is admitted but never evaluated, so derivation reads the entry ``F``."""

        from ssds.ledger.read import with_id

        from ._scenario import on_record

        sc = Scenario(THREE, dict(FILES))
        report = with_id({**record("FINDING", target={"units": ["arch"]}, fields={"materiality": "ROUTINE"}),
                          "actor": HUMAN})
        sc.admit(report)
        rec = self.review(sc, on_record(report["id"]))
        sc.admit(rec)
        self.assertEqual(sc.derive().current(rec["id"]), 0, "derivation reads it F")
        sc.entries.pop()
        self.assertEqual(self.codes(sc, rec), {"STALE_BASIS"})

    def test_a_frame_whose_fixing_result_is_gone_is_read_again(self) -> None:
        """Review 8408e05 B2: one ``Currency`` serves every round of the fixed point; a result refused in an earlier
        round fixes nothing in the next, so the frame record is stale there."""

        from ssds.admission.currency import Currency as Step6

        sc = Scenario(THREE, dict(FILES))
        before = sc.rev("impl")
        x, _, result = submit(sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        sc.entries.pop()
        rec = judgment("REVIEW", {"transformation": x}, "PASS", actor=HUMAN, basis=[content("impl", before)],
                       frame={"transformation": x})
        step6 = Step6(sc.derive())
        self.assertEqual(step6.codes(rec, tried(sc, [result, rec])), set(), "round 1: the result fixes X")
        self.assertEqual(step6.codes(rec, tried(sc, [rec])), {"STALE_BASIS"}, "round 2: it was refused")

    def test_a_standing_entry_on_a_superseded_record_is_stale(self) -> None:
        from ._scenario import attested

        sc = Scenario(THREE, dict(FILES))
        first = judgment("REVIEW", sc.triple("arch"), "PASS", actor=HUMAN)
        sc.admit(*attested(first))
        standing = {"mode": "standing", "target": {"record": first["id"]}, "class": "EXACT"}
        self.assertEqual(self.codes(sc, self.review(sc, standing)), set())
        again = judgment("REVIEW", sc.triple("arch"), "PASS", actor=HUMAN, supersedes=[first["id"]])
        sc.admit(*attested(again))
        self.assertEqual(self.codes(sc, self.review(sc, standing)), {"STALE_BASIS"})

    def test_a_before_image_a_concurrent_change_moved_is_stale_in_the_frame(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        before = sc.rev("impl")
        x, _, _ = submit(sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        rec = judgment("REVIEW", {"transformation": x}, "PASS", actor=HUMAN, basis=[content("impl", before)],
                       frame={"transformation": x})
        self.assertEqual(self.codes(sc, rec), set(), "the before-image is the head's revision")
        sc.absorb({"notes.md": "n2\n"})
        self.assertEqual(self.codes(sc, rec), set(), "a change elsewhere moves nothing")
        sc.absorb({"impl.md": "i1 concurrent\n"})
        self.assertEqual(self.codes(sc, rec), {"STALE_BASIS"})

    def test_an_integrated_frames_before_image_is_a_fixed_fact(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        before = sc.rev("impl")
        x, candidate, _ = submit(sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        rec = judgment("REVIEW", {"transformation": x}, "PASS", actor=HUMAN, basis=[content("impl", before)],
                       frame={"transformation": x})
        integrate(sc, x, candidate)
        self.assertEqual(self.codes(sc, rec), set(), "§7.3's admitted-state column (F17)")

    def test_a_frame_a_co_submitted_result_fixes_is_read_at_the_head(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        before = sc.rev("impl")
        x, candidate, result = submit(sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        sc.entries.pop()  # the result is co-submitted, not admitted
        rec = judgment("REVIEW", {"transformation": x}, "PASS", actor=HUMAN, basis=[content("impl", before)],
                       frame={"transformation": x})
        self.assertEqual(self.codes(sc, rec, siblings=[result]), set())
        self.assertEqual(self.codes(sc, rec), {"STALE_BASIS"}, "no result fixes X: no frame")

    def test_never_lost_reports_and_challenges_are_never_checked(self) -> None:
        from ._scenario import challenge

        sc = Scenario(THREE, dict(FILES))
        r1 = sc.rev("arch")
        sc.absorb({"arch.md": "a2\n"})
        stale = content("arch", r1)
        self.assertEqual(self.codes(sc, self.review(sc, stale)), {"STALE_BASIS"})
        self.assertEqual(self.codes(sc, self.review(sc, stale, outcome="NO_PASS")), set(), "adverse: never-lost")
        report = {**record("FINDING", target={"units": ["arch"]}, fields={"materiality": "ROUTINE"}),
                  "basis": [stale]}
        self.assertEqual(self.codes(sc, report), set())
        self.assertEqual(self.codes(sc, {**challenge({"subject": "arch", "scope_id": "s", "rev": r1}), "basis": [stale]}),
                         set())
        c = challenge({"subject": "arch", "scope_id": "s", "rev": r1})
        ruling = judgment("ADJUDICATION", {"record": c["id"]}, "UPHELD", basis=[stale])
        self.assertEqual(self.codes(sc, ruling), set(), "challenge tier: not support tier (F28)")

    def test_a_request_carrying_x_reads_every_record_in_its_frame(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        x, _, _ = submit(sc, {"impl.md": "i2\n"}, agent("maker"), "task-1")
        frame = frame_of_candidate(sc, x)
        rec = judgment("REVIEW", sc.triple("arch"), "PASS", actor=HUMAN, basis=[content("impl", frame.view.rev("impl"))])
        self.assertEqual(self.codes(sc, rec), {"STALE_BASIS"}, "the output does not exist at the head")
        self.assertEqual(self.codes(sc, rec, change=frame), set())

    def test_an_empty_basis_has_nothing_to_satisfy(self) -> None:
        sc = Scenario(THREE, dict(FILES))
        rec = judgment("REVIEW", {"transformation": "sha256:" + "9" * 64}, "PASS", frame={"transformation": "sha256:" + "9" * 64})
        self.assertEqual(self.codes(sc, rec), set())


class EngineWiring(unittest.TestCase):
    """The engine passes the request's own frame to every trial it builds, and none when that frame does not
    exist or the request changes nothing."""

    def frames_passed(self, overrides: dict, patches: dict) -> list:
        from ssds.admission.engine import Admission
        from ssds.admission.request import request_message

        from ._fixtures import sshsig
        from .test_admission_requests import RequestFixture, finding

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        seen = []
        original = Admission.trial

        def spy(admission, chain, entry, objects=None, frame=None):
            seen.append(frame)
            return original(admission, chain, entry, objects)

        rec = with_actor(finding(), fixture.human())
        req = fixture.request([rec, *overrides.pop("records", [])], base_position=len(fixture.entries()) - 1,
                              **overrides)
        req["binding"] = {"human": {"actor": fixture.human(), "signature": sshsig(fixture.private, request_message(req))}}
        with mock.patch.object(Admission, "trial", spy), \
                mock.patch.multiple("ssds.admission.engine", **patches) as made:
            fixture.admit(req)
        for name, value in made.items():
            if isinstance(value, mock.MagicMock):
                value.assert_not_called()  # an unpatched owner the request must never reach
        return seen

    def assert_frame_then_head(self, seen: list, frame) -> None:
        """The records are judged in the frame; the never-lost ones again at the head, for salvage (F27)."""

        self.assertGreaterEqual(len(seen), 2)
        self.assertIs(seen[0], frame)
        self.assertIsNone(seen[-1])
        self.assertEqual({id(f) for f in seen}, {id(frame), id(None)})

    @staticmethod
    def fake(exists: bool):
        frame = mock.create_autospec(Frame, instance=True)
        frame.exists = exists
        return frame

    def test_an_integrating_request_passes_its_frame(self) -> None:
        frame = self.fake(True)
        seen = self.frames_passed({"candidates": ["0" * 40]}, {"integration_codes": lambda *a: set(),
                                                                "integration_frame": lambda *a: frame})
        self.assert_frame_then_head(seen, frame)

    def test_a_frame_that_does_not_exist_is_not_passed(self) -> None:
        seen = self.frames_passed({"candidates": ["0" * 40]}, {"integration_codes": lambda *a: set(),
                                                                "integration_frame": lambda *a: self.fake(False)})
        self.assertEqual(set(map(id, seen)), {id(None)})
        refused = self.frames_passed({"candidates": ["0" * 40]}, {"integration_codes": lambda *a: set(),
                                                                   "integration_frame": lambda *a: "REF_TRANSFORMATION"})
        self.assertEqual(set(map(id, refused)), {id(None)})

    def test_an_adopting_request_passes_its_frame(self) -> None:
        frame = self.fake(True)
        element = {"absorption": "sha256:" + "4" * 64, "key": ["guide", "kind"], "value": "D3"}
        seen = self.frames_passed({"adopted_deltas": [element]}, {"adoption_frame": lambda *a: frame,
                                                                  "adoptable": lambda *a: True,
                                                                  "adoption_codes": lambda *a, **k: set()})
        self.assert_frame_then_head(seen, frame)

    def test_a_request_changing_nothing_passes_none(self) -> None:
        seen = self.frames_passed({}, {"integration_frame": mock.DEFAULT})
        self.assertTrue(seen)
        self.assertEqual(set(map(id, seen)), {id(None)})


class RequestCycle(unittest.TestCase):
    """The engine reads ``CYCLE_SUPPORT`` from the final trial against the head (F24). A cycle among new records
    needs subjects valid at the head, which no admitted request can yet make, so the decision is driven here."""

    def test_a_final_trial_that_grows_a_cycle_is_cycle_support(self) -> None:
        from ssds.admission.authorize import Authorization
        from ssds.admission.engine import Admission
        from ssds.admission.request import request_message

        from ._fixtures import sshsig
        from .test_admission_requests import RequestFixture, finding

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        for grows in (True, False):
            class Tried:
                def grows_a_cycle(self, before) -> bool:
                    return grows

            rec = with_actor(finding(note=str(grows)), fixture.human())
            req = fixture.request([rec], base_position=len(fixture.entries()) - 1)
            req["binding"] = {"human": {"actor": fixture.human(),
                                        "signature": sshsig(fixture.private, request_message(req))}}
            with mock.patch.object(Admission, "trial", lambda *a, **k: Tried()), \
                    mock.patch("ssds.admission.engine.authorize",
                               lambda *a: Authorization(True, frozenset(), (), ())):
                reasons = fixture.admit(req).reasons
            with self.subTest(grows=grows):
                self.assertEqual("CYCLE_SUPPORT" in reasons, grows)


class StaleThroughTheEngine(unittest.TestCase):
    def test_step_six_joins_the_records_other_codes(self) -> None:
        from ssds.admission.request import request_message
        from ssds.ledger.read import with_id

        from ._fixtures import sshsig
        from .test_admission_requests import RequestFixture

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        from .test_phase_f_step4b import derive_state

        subject, scope, rev = derive_state(fixture).subject_triple("guide")
        # its own subject (step 5) and invalid at the head (step 6): both codes, one refusal
        rec = with_id({**record("REVIEW", target={"subject": subject, "scope_id": scope, "rev": rev}, outcome="PASS",
                                basis=[content("guide", rev), validity("guide", rev)]), "actor": fixture.human()})
        req = fixture.request([rec], base_position=len(fixture.entries()) - 1)
        req["binding"] = {"human": {"actor": fixture.human(), "signature": sshsig(fixture.private, request_message(req))}}
        self.assertEqual(dict(fixture.admit(req).refused).get(rec["id"]), ("DEP_OWN_SUBJECT", "STALE_BASIS"))


class SalvageAtTheHead(unittest.TestCase):
    """A rejection admits never-lost records at the head (catalogue §8.3 step 6), so a structure-changing request's
    never-lost records are salvaged by their reading there, not in the frame the rejection never applies."""

    def decide(self, refuse_in: str):
        from ssds.admission.authorize import Authorization
        from ssds.admission.engine import Admission
        from ssds.admission.request import request_message

        from ._fixtures import sshsig
        from .test_admission_requests import RequestFixture, finding

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        rec = with_actor(finding(), fixture.human())
        frame = EngineWiring.fake(True)

        class Tried:
            def __init__(self, framed: bool) -> None:
                self.framed = framed

            def grows_a_cycle(self, before) -> bool:
                return False

        def trial(admission, chain, entry, objects=None, change=None):
            return Tried(change is not None)

        def authorize(request, records, tried, base):
            where = "frame" if tried.framed else "head"
            gone = tuple((r["id"], ("AUTH_ACTOR",)) for r in records if where == refuse_in)
            return Authorization(True, frozenset(), gone, ())

        req = fixture.request([rec], base_position=len(fixture.entries()) - 1, candidates=["0" * 40])
        req["binding"] = {"human": {"actor": fixture.human(), "signature": sshsig(fixture.private, request_message(req))}}
        with mock.patch.object(Admission, "trial", trial), \
                mock.patch.multiple("ssds.admission.engine", integration_codes=lambda *a: set(),
                                    integration_frame=lambda *a: frame, authorize=authorize):
            return fixture.admit(req), rec["id"]

    def test_refused_in_the_frame_but_kept_at_the_head_is_salvaged(self) -> None:
        decision, rid = self.decide("frame")
        self.assertEqual(decision.decision, "REJECT")
        self.assertIn(rid, decision.admitted)
        self.assertNotIn(rid, dict(decision.refused))

    def test_refused_at_the_head_is_refused_there(self) -> None:
        decision, rid = self.decide("head")
        self.assertEqual(decision.decision, "REJECT")
        self.assertNotIn(rid, decision.admitted)
        self.assertEqual(dict(decision.refused).get(rid), ("AUTH_ACTOR",))


def with_actor(rec: dict, actor: str) -> dict:
    from ssds.ledger.read import with_id

    return with_id({**rec, "actor": actor})


if __name__ == "__main__":
    unittest.main()
