"""Phase F step 6c: accepting (catalogue §8.3 steps 1, 6, 9; plan §3.3, readings F40, F42; SD-70, SD-72).

A request that passes every built check is accepted, except what Phase F does not yet accept (``gated``): a
request carrying a ``TASK_RESULT`` or candidates or claiming an item obligation (SD-70, SD-71), a runner's
evidence or its assessment (step 9), and an adoption while any realization is admitted (SD-72, F42). Step 9's drop
cascade runs on ACCEPT (F40). A records-only ``ABSORB`` adoption is accepted with its frame's deltas and no
integration: the path step 10 repairs ``ssdp-shadow-2`` by.
"""

from __future__ import annotations

import unittest
from types import SimpleNamespace
from unittest import mock

from ssds.admission.engine import Admission, gated
from ssds.derivation import derive
from ssds.ledger.read import read_chain, with_id

from ._fixtures import commit, record
from .test_admission_genesis import MANIFEST
from .test_admission_requests import RequestFixture, finding


class Accepting(RequestFixture):
    def signed_by_human(self, records, **overrides):
        from ssds.admission.request import request_message

        from ._fixtures import sshsig

        req = self.request(records, base_position=len(self.entries()) - 1, **overrides)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return req

    def test_a_records_only_request_is_accepted_and_derived(self) -> None:
        rec = with_id({**finding(), "actor": self.human()})
        decision = self.admit(self.signed_by_human([rec]))
        self.assertEqual((decision.decision, decision.reasons, decision.admitted), ("ACCEPT", (), (rec["id"],)))
        support = derive(read_chain(self.home.ledger_repository("demo"), "demo"), self.trees)
        self.assertIn(rec["id"], support.s.records)
        entry = self.entries()[-1].entry["admission"]
        self.assertEqual((entry["adopted_deltas"], entry["integrates"]), ([], None))

    def test_a_task_result_or_a_runners_evidence_is_not_yet_accepted(self) -> None:
        result = with_id({**record("TASK_RESULT", target={"task": "t"}, outcome="COMPLETE", fields={"slots": {}}),
                          "actor": self.human()})
        self.assertIn("SCHEMA_UNSUPPORTED", self.admit(self.signed_by_human([result])).reasons, "SD-70")

    def test_a_dropped_reference_rejects_the_request(self) -> None:
        """F40: a record naming one a later step refused is dropped, and the request is rejected."""

        from ssds.admission.authorize import Authorization

        ineligible = with_id({**finding(materiality="MATERIAL"), "actor": self.human()})
        naming = with_id({**record("FINDING", target={"records": [ineligible["id"]]}, fields={"materiality": "ROUTINE"}),
                          "actor": self.human()})

        def fake(request, records, trial, base):
            present = {r["id"] for r in records}
            return Authorization(True, frozenset(), (), tuple((rid, ("AUTH_ACTOR",)) for rid in [ineligible["id"]]
                                                             if rid in present))

        with mock.patch("ssds.admission.engine.authorize", fake):
            decision = self.admit(self.signed_by_human([ineligible, naming]))
        self.assertEqual(decision.decision, "REJECT")
        self.assertEqual(dict(decision.refused).get(naming["id"]), ("REF_RECORD",))
        self.assertNotIn(naming["id"], decision.admitted)


class Adoption(RequestFixture):
    """Step 10's repair, rehearsed: a foreign declaration change absorbed, then adopted by a human ``ABSORB``."""

    WIDE = MANIFEST.replace('scope = [{ prefix = "src/" }]', 'scope = [{ prefix = "src/" }, { prefix = "lib/" }]')

    def signed_by_human(self, records, **overrides):
        from ssds.admission.request import request_message

        from ._fixtures import sshsig

        req = self.request(records, base_position=len(self.entries()) - 1, **overrides)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return req

    def test_an_absorb_adoption_is_accepted_with_its_deltas_and_no_integration(self) -> None:
        from ssds.content import decl_to_json

        from .test_phase_f_step4c import _decl_value

        (self.product / ".ssds" / "manifest.toml").write_text(self.WIDE)
        (self.product / "lib").mkdir()
        (self.product / "lib" / "x.py").write_text("x = 1\n")
        obs = commit(self.product, "a foreign declaration change")
        admission = Admission(self.home, "demo", self.trees, product=self.product)
        admission.admit(self.signed_by_human([with_id({**finding(), "actor": self.human()})]), obs)
        before = derive(read_chain(self.home.ledger_repository("demo"), "demo"), self.trees).s
        key = ("code", "scope")
        absorption, value = before.current_delta(key)
        element = {"absorption": absorption, "key": list(key), "value": _decl_value(decl_to_json({key: value}), key)}
        absorb = with_id({**record("INTAKE_DISPOSITION", target={"absorption": absorption, "key": list(key)},
                                   outcome="ABSORB"), "actor": self.human()})
        decision = admission.admit(self.signed_by_human([absorb], adopted_deltas=[element], base_commit=obs), obs)
        self.assertEqual((decision.decision, decision.reasons), ("ACCEPT", ()), decision)
        entry = self.entries()[-1].entry["admission"]
        self.assertEqual(entry["integrates"], None, "an adoption never integrates (plan check N2)")
        self.assertEqual([(d["key"], d["source"]) for d in entry["adopted_deltas"]], [(["code", "scope"], "ADOPTED")])
        after = derive(read_chain(self.home.ledger_repository("demo"), "demo"), self.trees).s
        self.assertEqual(after.h.sigma(after.n)[key], value, "Σ adopts the observed value")
        self.assertEqual(after.integrated, before.integrated)
        self.assertIsNone(after.current_delta(key), "no longer quarantined")


class Gate(unittest.TestCase):
    def test_what_phase_f_does_not_yet_accept(self) -> None:
        items = SimpleNamespace(of=lambda c: object() if c == "item" else None)
        support = SimpleNamespace(s=SimpleNamespace(of_kind=lambda *k: []))
        with mock.patch("ssds.admission.engine.Workflow", lambda s: SimpleNamespace(items=items)):
            self.assertFalse(gated({}, [{"kind": "FINDING"}], support, None))
            self.assertTrue(gated({}, [{"kind": "TASK_RESULT"}], support, None))
            self.assertTrue(gated({"candidates": ["c"]}, [], support, None))
            for kind in ("EVIDENCE_ASSESSMENT", "REALIZATION", "CHECK_EXECUTION"):
                self.assertTrue(gated({}, [{"kind": kind}], support, None), kind)
            self.assertTrue(gated({"claims": ["item"]}, [], support, None), "an item obligation reads conformance")
            self.assertFalse(gated({"claims": ["other"]}, [], support, None))

    def test_an_adoption_waits_while_any_realization_is_admitted(self) -> None:
        from ssds.derivation import Frame

        adoption = mock.create_autospec(Frame, instance=True)
        adoption.enactment = None
        items = SimpleNamespace(of=lambda c: None)
        with mock.patch("ssds.admission.engine.Workflow", lambda s: SimpleNamespace(items=items)):
            none = SimpleNamespace(s=SimpleNamespace(of_kind=lambda *k: []))
            some = SimpleNamespace(s=SimpleNamespace(of_kind=lambda *k: ["sha256:r"]))
            self.assertFalse(gated({}, [], none, adoption))
            self.assertTrue(gated({}, [], some, adoption), "F42, SD-72")
            integration = mock.create_autospec(Frame, instance=True)
            integration.enactment = "task-1"
            self.assertFalse(gated({}, [], some, integration), "not an adoption (integrations are gated by candidates)")


if __name__ == "__main__":
    unittest.main()
