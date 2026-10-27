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

    def test_a_kind_phase_f_does_not_check_is_not_yet_accepted(self) -> None:
        """Review c9c937d: a human decision on an obligation no one derives, an observation recorded by a human."""

        for kind, target, outcome in (("HUMAN_DECISION", {"obligation": "sha256:" + "6" * 64}, "ACCEPT"),
                                      ("AVAILABILITY", {"digest": "sha256:" + "6" * 64}, "AVAILABLE")):
            rec = with_id({**record(kind, target=target, outcome=outcome), "actor": self.human()})
            decision = self.admit(self.signed_by_human([rec]))
            with self.subTest(kind=kind):
                self.assertNotEqual(decision.decision, "ACCEPT")
                self.assertNotIn(rec["id"], decision.admitted)

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

        def fake(request, records, trial, base, resubmitted=None):
            present = {r["id"] for r in records}
            return Authorization(True, frozenset(), (), tuple((rid, ("AUTH_ACTOR",)) for rid in [ineligible["id"]]
                                                             if rid in present))

        with mock.patch("ssds.admission.engine.authorize", fake):
            decision = self.admit(self.signed_by_human([ineligible, naming]))
        self.assertEqual(decision.decision, "REJECT")
        self.assertEqual(dict(decision.refused).get(naming["id"]), ("REF_RECORD",))
        self.assertNotIn(naming["id"], decision.admitted)


class Targets(RequestFixture):
    """Review c80fc6a B1: with ACCEPT lifted, a record's target exists (§8.3 step 2: ``REF_TARGET``), and a legacy
    import meets the acceptance target rules, on a subject its protocol governs (§19.2)."""

    def signed_by_human(self, records):
        from ssds.admission.request import request_message

        from ._fixtures import sshsig

        req = self.request(records, base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return req

    def refused(self, kind, target, outcome, **fields):
        rec = with_id({**record(kind, target=target, outcome=outcome, fields=fields or None), "actor": self.human()})
        decision = self.admit(self.signed_by_human([rec]))
        return decision, dict(decision.refused).get(rec["id"])

    def test_a_target_that_does_not_exist(self) -> None:
        from .test_phase_f_step4b import derive_state

        rev = derive_state(self).subject_triple("guide")[2]
        _, codes = self.refused("EQUIVALENCE", {"unit": "nowhere", "from": rev, "to": rev, "class": "EDITORIAL"},
                                "EQUIVALENT")
        self.assertEqual(codes, ("REF_TARGET",))
        _, codes = self.refused("RECONSTRUCTION_PROPOSAL", {"units": ["nowhere"]}, "PROPOSED")
        self.assertEqual(codes, ("REF_TARGET",))
        _, codes = self.refused("REVIEW", {"subject": "guide", "scope_id": "sha256:" + "0" * 64,
                                           "rev": "sha256:" + "0" * 64}, "PASS")
        self.assertEqual(codes, ("REF_TARGET",), "a revision that never existed")

    def test_a_target_that_exists_is_accepted(self) -> None:
        decision, codes = self.refused("FINDING", {"units": ["guide"]}, None, materiality="ROUTINE")
        self.assertEqual((decision.decision, codes), ("ACCEPT", None))

    def test_an_equivalence_names_known_revisions_and_a_challenge_a_known_locus(self) -> None:
        """Review c9c937d: an equivalence's ``from`` and ``to``; a challenge's ``locus``."""

        from .test_phase_f_step4b import derive_state

        subject, scope, rev = derive_state(self).subject_triple("guide")
        made_up = "sha256:" + "0" * 64
        _, codes = self.refused("EQUIVALENCE", {"unit": "guide", "from": made_up, "to": rev, "class": "EDITORIAL"},
                                "EQUIVALENT")
        self.assertEqual(codes, ("REF_TARGET",))
        _, codes = self.refused("CHALLENGE", {"subject": subject, "scope_id": scope, "rev": rev}, None,
                                blocking=True, serious=False, inquiry="EXPLORATORY", locus="nowhere")
        self.assertEqual(codes, ("REF_TARGET",))

    def test_a_triple_is_checked_whole_and_a_reclassification_names_a_report(self) -> None:
        """Review 4263380 B1: a triple's ``scope_id`` too, so no challenge binds a triple before it exists."""

        from .test_phase_f_step4b import derive_state

        subject, scope, rev = derive_state(self).subject_triple("guide")
        _, codes = self.refused("CHALLENGE", {"subject": subject, "scope_id": "sha256:" + "0" * 64, "rev": rev}, None,
                                blocking=True, serious=False, inquiry="EXPLORATORY")
        self.assertEqual(codes, ("REF_TARGET",))
        decision, codes = self.refused("CHALLENGE", {"subject": subject, "scope_id": scope, "rev": rev}, None,
                                       blocking=True, serious=False, inquiry="EXPLORATORY")
        self.assertEqual(codes, None, "the triple that exists")
        challenge_id = decision.admitted[0]
        _, codes = self.refused("MATERIALITY_RECLASSIFICATION", {"record": challenge_id}, "ROUTINE")
        self.assertNotIn("REF_TARGET", codes or ())
        attestation = with_id({**record("NON_AUTHORSHIP_ATTESTATION", target={"record": challenge_id},
                                        outcome="NOT_AUTHOR"), "actor": self.human()})
        self.assertIn(attestation["id"], self.admit(self.signed_by_human([attestation])).admitted)
        _, codes = self.refused("MATERIALITY_RECLASSIFICATION", {"record": attestation["id"]}, "ROUTINE")
        self.assertEqual(codes, ("REF_TARGET",), "an attestation is neither a report nor a challenge")

    def test_a_legacy_import_meets_the_acceptance_rules(self) -> None:
        from .test_phase_f_step4b import derive_state

        subject, scope, rev = derive_state(self).subject_triple("guide")
        _, codes = self.refused("LEGACY_ACCEPTANCE", {"subject": "guide.intro", "scope_id": scope, "rev": rev},
                                "IMPORTED", legacy=["x"])
        self.assertIn("AUTH_TARGET_PART", codes)
        _, codes = self.refused("LEGACY_ACCEPTANCE", {"subject": "nowhere", "scope_id": scope, "rev": rev},
                                "IMPORTED", legacy=["x"])
        self.assertIn("AUTH_TARGET_NOT_EFFECTIVE", codes)
        _, codes = self.refused("LEGACY_ACCEPTANCE", {"subject": subject, "scope_id": scope, "rev": rev},
                                "IMPORTED", legacy=["x"])
        self.assertEqual(codes, ("AUTH_VERSION",), "this fixture's guide is NATIVE: no legacy protocol governs it")

    def test_an_external_import_is_not_yet_accepted(self) -> None:
        decision, _ = self.refused("EXTERNAL_ACCEPTANCE", {"external": "some-body"}, "IMPORTED")
        self.assertIn("SCHEMA_UNSUPPORTED", decision.reasons)


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
            finding_ = {"kind": "FINDING", "target": {"units": ["guide"]}}
            self.assertFalse(gated({}, [finding_], support, None))
            self.assertTrue(gated({}, [{"kind": "FINDING"}], support, None), "no target shape: not accepted")
            self.assertTrue(gated({}, [{"kind": "TASK_RESULT", "target": {"task": "t"}}], support, None))
            self.assertTrue(gated({"candidates": ["c"]}, [], support, None))
            for kind, target in (("EVIDENCE_ASSESSMENT", {"realization": "r", "obligation": "o"}),
                                 ("HUMAN_DECISION", {"obligation": "o"}),
                                 ("AVAILABILITY", {"digest": "d"}), ("CUSTODY_ENUMERATION", {"runner": "r"}),
                                 ("EXTERNAL_CONSULTATION", {"external": "e"}), ("RISK_OVERRIDE", {"record": "r"}),
                                 ("GATE_DECISION", {"gate": "g", "subject": {}, "core": "c"}),
                                 ("REVIEW", {"integrated": "ITEM", "of": "k"}),
                                 ("RECONSTRUCTION_PROPOSAL", {"units": ["guide"]})):
                self.assertTrue(gated({}, [{"kind": kind, "target": target}], support, None), kind)
            self.assertFalse(gated({}, [{"kind": "REALIZATION", "target": {"spec": {}, "claim": []}}], support, None),
                             "step 9d-i (F99)")
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
