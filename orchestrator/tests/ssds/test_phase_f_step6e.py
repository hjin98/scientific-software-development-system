"""Phase F step 6e: integration registration (plan §3.3; plan check of 0d92c731; reading F27).

``History`` registers an integration whenever an accepted admission carries ``integrates``, so an empty
transformation (``C = B``, the head unmoved) agrees with its trial; a rejection naming ``X`` integrates nothing
(F35); the checkpoint round trip keeps the registration.
"""

from __future__ import annotations

import unittest

from ssds.derivation import trial
from ssds.derivation.frames import Frame, transformation_of
from ssds.derivation.history import History

from ._fixtures import admission_body, chain_of
from ._scenario import Scenario, agent, submit
from .test_phase_f_step4d import FILES, THREE


def history(sc: Scenario, checkpoint=None) -> History:
    return History(chain_of("demo", sc.entries, sc.objects), sc.trees.__getitem__, checkpoint)


class Registration(unittest.TestCase):
    def setUp(self) -> None:
        self.sc = Scenario(THREE, dict(FILES))
        self.x, self.candidate, _ = submit(self.sc, {}, agent("maker"), "task-1")  # an empty transformation
        self.assertEqual(self.sc.trees[self.candidate], self.sc.trees[self.sc.head])

    def test_an_empty_integration_is_registered_and_agrees_with_its_trial(self) -> None:
        s = self.sc.derive().s
        frame = Frame(s.h, s.n, transformation_of(s, self.x), s.enactment(self.x))
        tried = trial(chain_of("demo", self.sc.entries, self.sc.objects), self.sc.trees.__getitem__,
                      admission_body(self.sc.position, self.sc.head, self.sc.head), None, frame).s
        self.sc.entries.append(admission_body(self.sc.position, self.sc.head, self.sc.head, integrates=self.x))
        admitted = self.sc.derive().s
        self.assertIn(s.enactment(self.x), admitted.integrated, "C = B, yet the entry integrates X")
        self.assertEqual(admitted.integrated, tried.integrated, "the admission agrees with its trial (F27)")

    def test_a_rejection_naming_x_integrates_nothing(self) -> None:
        self.sc.entries.append(admission_body(self.sc.position, self.sc.head, self.sc.head, integrates=self.x,
                                              decision="REJECT"))
        self.assertNotIn(self.sc.derive().s.enactment(self.x), self.sc.derive().s.integrated)

    def test_an_admission_without_integrates_and_an_unmoved_head_integrates_nothing(self) -> None:
        before = dict(history(self.sc).integrations)
        self.sc.entries.append(admission_body(self.sc.position, self.sc.head, self.sc.head))
        self.assertEqual(dict(history(self.sc).integrations), before)

    def test_the_checkpoint_round_trip_keeps_it(self) -> None:
        self.sc.entries.append(admission_body(self.sc.position, self.sc.head, self.sc.head, integrates=self.x))
        full = history(self.sc)
        position = self.sc.position - 1
        resumed = history(self.sc, full.checkpoint(position))
        self.assertEqual(resumed.integrations, full.integrations)


if __name__ == "__main__":
    unittest.main()
