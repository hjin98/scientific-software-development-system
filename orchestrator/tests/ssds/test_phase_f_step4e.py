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
from ._scenario import HUMAN, Scenario, agent, content, integrate, judgment, submit, validity
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
