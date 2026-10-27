"""Phase F step 9g-ii: who records ``AVAILABILITY`` (catalogue §3.4, §17.4; SD-82, Q-F22; plan reading F117).

Admission accepts an ``AVAILABILITY`` record on a content reference from a human, under a human binding, and from a
designated runner, under its machinery binding: a key some runner class in force designates, the actor its
``machinery:<component>@<key id>``. Any other actor is ``AUTH_ACTOR``. The Executor's ``report_availability`` submits
one signed by its class's key. Admitted, the latest acting record decides binding health (F92). Expected values are
from §3.4, §17.4 and F117.
"""

from __future__ import annotations

from ssds.derivation import P, T
from ssds.dispatcher.realize import RunnerKey as DispatcherKey
from ssds.ledger.qualification import Home

from ._fixtures import record
from . import test_phase_f_step9d_iii as harness
from .test_phase_f_step9f_ii_iii import GOOD, Fixture

DIGEST = "sha256:" + "6" * 64


class Producers(harness.AdmittedRuns):
    def setUp(self) -> None:
        super().setUp()
        self.stranger = harness.RunnerKey()  # registered, but designated by no class
        self.lifecycle("REGISTER", self.stranger.trust_root())

    def availability(self, outcome="UNAVAILABLE", actor=None, actor_class="MACHINERY", digest=DIGEST) -> dict:
        return record("AVAILABILITY", target={"digest": digest}, outcome=outcome,
                      actor=actor or f"machinery:runner@{self.runner.key_id}", actor_class=actor_class)

    def codes(self, key, rec) -> tuple:
        decision = self.admission.admit(key.sign(self.request([rec])), self.head())
        return tuple(sorted(set(dict(decision.refused).get(rec["id"], ())) | set(decision.reasons)))

    def test_a_human(self) -> None:
        rec = self.availability("AVAILABLE", actor=self.human(), actor_class="HUMAN")
        self.assertEqual(self.admit_human(rec).admitted, (rec["id"],))

    def test_a_designated_runner(self) -> None:
        self.assertEqual(self.codes(self.runner, self.availability()), ())
        self.assertEqual(self.codes(self.custodian, self.availability(actor=f"machinery:custody@{self.custodian.key_id}")),
                         (), "an external custody class's key is a designated runner too")

    def test_another_binding_is_refused(self) -> None:
        self.assertIn("AUTH_ACTOR", self.codes(self.stranger, self.availability(
            actor=f"machinery:runner@{self.stranger.key_id}")), "a registered key no class designates")
        self.assertIn("AUTH_ACTOR", self.codes(self.runner, self.availability(
            actor=f"machinery:runner@{self.custodian.key_id}")), "another key's actor")
        self.assertIn("AUTH_ACTOR", self.codes(self.runner, self.availability(actor=self.human(), actor_class="HUMAN")),
                      "a human's record under a runner's binding")
        rec = self.availability(actor="agent:implementer", actor_class="AGENT")
        req = self.request([rec])
        req["binding"] = {"human": {"actor": self.human(), "signature": harness.sshsig(self.private,
                                                                                   harness.request_message(req))}}
        decision = self.admission.admit(req, self.head())
        self.assertNotIn(rec["id"], decision.admitted, "an agent's record under a human's binding")

    def test_the_records_effect(self) -> None:
        """F92: the latest acting record on a reference the realization needs decides its binding health."""

        real = self.realize(self.tree("T0"), {"x": 2, "x_verdict": "PASS"})
        self.assertTrue(self.derive().a.standing(real["id"]))
        self.assertEqual(self.codes(self.runner, self.availability(digest=real["fields"]["evaluated"])), ())
        self.assertFalse(self.derive().a.standing(real["id"]), "unavailable: not standing (§17.4)")
        self.assertEqual(self.codes(self.runner, self.availability("AVAILABLE", digest=real["fields"]["evaluated"])),
                         ())
        self.assertTrue(self.derive().a.standing(real["id"]), "the latest record restores it")


class Reported(Fixture):
    """The Executor's ``report_availability``: signed by its class's key, admitted, and acting (F117)."""

    def test_report_availability(self) -> None:
        ex = self.executor(GOOD)
        (item,) = [r for r in ex.runs(self.derive()) if r.obligation.kind == "REALIZE"]
        ran = ex.run(self.derive(), item)
        real = self.derive().s.record(ran.admitted[0])
        evaluated = real["fields"]["evaluated"]
        decision = ex.report_availability("ci", evaluated, "UNAVAILABLE")
        self.assertEqual((decision.reasons, decision.refused), ((), ()))
        (rid,) = decision.admitted
        rec = self.derive().s.record(rid)
        self.assertEqual((rec["kind"], rec["target"], rec["actor"]),
                         ("AVAILABILITY", {"digest": evaluated}, f"machinery:runner@{self.runner.key_id}"))
        self.assertFalse(self.derive().a.standing(real["id"]))
        with self.assertRaises(ValueError):
            ex.report_availability("ci", evaluated, "GONE")
        with self.assertRaises(ValueError):
            ex.report_availability("vault", evaluated, "UNAVAILABLE")  # this Dispatcher holds no key it designates
