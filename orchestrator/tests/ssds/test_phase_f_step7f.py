"""Phase F steps 7f and 7g: the continuity attestation's checks and the rest of the recovery kinds (catalogue §3.4,
§22.1, §23.7, §23.8, §24.2; plan §3.4, readings F48, F63, F64).

7f: an attestation targets an earlier admitted ``LEDGER_LOSS``, lists subjects or records, and cites stored
evidence; its codes are reported beside ``SCHEMA_UNSUPPORTED``, which stays until a policy designates its actor
(F48). A challenge of an attestation is permitted. 7g: a replica redesignation's and a lineage migration's field
checks, both refused (SD-75; Q-F16); a redaction notice admitted as §24.2's rotation-branch record, with no derived
effect.
"""

from __future__ import annotations

import unittest
from types import SimpleNamespace

from ssds.admission.dependency import dependency_codes
from ssds.admission.engine import AdmissionHalted, EntryInvalid, attestation_references
from ssds.admission.lifecycle import migration_problems, redaction_problems, replica_problems
from ssds.derivation import Consequences, derive
from ssds.ledger.read import ledger_ref, read_chain

from ._fixtures import lifecycle_body, record, sshsig
from ._scenario import HUMAN, HUMAN_B, OWNER, Scenario, attested, challenge, judgment
from .test_admission_requests import RequestFixture
from .test_phase_f_step4d import FILES, THREE

LOSS_FIELDS = {"retained": {"position": 1}, "abandoned": [{"digest": "sha256:" + "a" * 64}],
               "report": "sha256:" + "b" * 64, "controls": {}}


def attestation(loss: str, listed=(), evidence=()) -> dict:
    return judgment("CONTINUITY_ATTESTATION", {"loss": loss}, None, actor=OWNER,
                    fields={"scope_form": "COMPLEMENT", "listed": list(listed), "evidence": list(evidence)})


class Attestation(unittest.TestCase):
    """Step 5's codes on derivation facts (F63)."""

    def setUp(self) -> None:
        self.sc = Scenario(THREE, dict(FILES))
        self.review = judgment("REVIEW", self.sc.triple("arch"), "PASS", actor=HUMAN_B)
        self.sc.admit(*attested(self.review))
        self.loss = record("LEDGER_LOSS", target=None, actor=OWNER, fields=LOSS_FIELDS)
        self.sc.entries.append(lifecycle_body(self.sc.position, self.loss))

    def codes(self, rec: dict) -> set[str]:
        self.sc.admit(rec)
        return dependency_codes(rec, self.sc.derive())

    def test_a_well_formed_attestation_is_only_unsupported(self) -> None:
        self.assertEqual(self.codes(attestation(self.loss["id"])), {"SCHEMA_UNSUPPORTED"})

    def test_its_other_codes_are_reported_beside_unsupported(self) -> None:
        self.assertEqual(self.codes(attestation(self.review["id"])), {"SCHEMA_UNSUPPORTED", "DEP_TARGET_KIND"})

    def test_a_loss_in_the_same_entry_is_not_earlier(self) -> None:
        loss = record("LEDGER_LOSS", target=None, actor=OWNER, fields={**LOSS_FIELDS, "report": "sha256:" + "c" * 64})
        attest = attestation(loss["id"])
        self.sc.admit(loss, attest)
        self.assertEqual(dependency_codes(attest, self.sc.derive()), {"SCHEMA_UNSUPPORTED", "DEP_TARGET_ORDER"})

    def test_a_challenge_of_an_attestation_is_permitted(self) -> None:
        """§23.7: "any qualified actor may challenge it"; the attestation exists here only on derivation facts."""

        attest = attestation(self.loss["id"])
        self.sc.admit(*attested(attest))
        self.assertEqual(self.codes(challenge({"record": attest["id"]}, actor=HUMAN)), set())


class AttestationReferences(unittest.TestCase):
    """Step 2's references (F63): the loss and listed ids exist, subjects or records; evidence is stored."""

    UNITS = {"arch": SimpleNamespace(subject=True), "arch.part": SimpleNamespace(subject=False)}

    def refs(self, rec: dict, known=frozenset({"sha256:" + "1" * 64}), objects=frozenset({"sha256:" + "e" * 64})):
        return attestation_references(rec, set(known), [], self.UNITS, set(objects))

    def test_each_reference(self) -> None:
        loss = "sha256:" + "1" * 64
        self.assertEqual(self.refs(attestation(loss, ["arch", loss], ["sha256:" + "e" * 64])), [])
        self.assertEqual(self.refs(attestation("sha256:" + "9" * 64)), ["REF_TARGET"], "no such loss")
        self.assertEqual(self.refs(attestation(loss, ["arch.part"])), ["REF_TARGET"], "a part is no subject")
        self.assertEqual(self.refs(attestation(loss, ["nowhere"])), ["REF_TARGET"])
        self.assertEqual(self.refs(attestation(loss, [], ["sha256:" + "f" * 64])), ["REF_OBJECT"], "evidence unstored")


class FieldChecks(unittest.TestCase):
    """7g's field checks (F64)."""

    def test_a_replica_redesignation(self) -> None:
        current = {"repository": "ssds-home:ledgers/demo", "ref": ledger_ref("demo")}
        good = {"location": {"repository": "mirror:demo", "ref": ledger_ref("demo")}}
        self.assertEqual(replica_problems(good, "demo", current), [])
        for fields in ({"location": current}, {"location": {"repository": "mirror:demo", "ref": "refs/heads/x"}},
                       {"location": {"repository": "mirror:demo"}}, {"location": {**good["location"], "x": 1}},
                       {"location": good["location"], "note": 1}, {}):
            with self.subTest(fields=fields):
                self.assertTrue(replica_problems(fields, "demo", current))

    def test_a_lineage_migration_is_refused_naming_q_f16(self) -> None:
        good = {"predecessor": {"ledger_id": "old", "last_position": 3, "last_entry_digest": "sha256:" + "3" * 64}}
        self.assertEqual(len(migration_problems(good, "demo")), 1)
        self.assertIn("Q-F16", migration_problems(good, "demo")[0])
        for predecessor in ({**good["predecessor"], "ledger_id": "demo"}, {**good["predecessor"], "last_position": True},
                            {**good["predecessor"], "last_entry_digest": "x"}, {"ledger_id": "old"}):
            with self.subTest(predecessor=predecessor):
                self.assertGreater(len(migration_problems({"predecessor": predecessor}, "demo")), 1)

    def test_a_redaction_notice(self) -> None:
        stored = {"sha256:" + "1" * 64, "sha256:" + "2" * 64}
        self.assertEqual(redaction_problems({"objects": sorted(stored)}, stored), [])
        for fields in ({"objects": []}, {"objects": ["sha256:" + "1" * 64] * 2}, {"objects": ["sha256:" + "9" * 64]},
                       {"objects": sorted(stored), "note": 1}, {}):
            with self.subTest(fields=fields):
                self.assertTrue(redaction_problems(fields, stored))


class Admission(RequestFixture):
    """7g through ``admit_lifecycle`` on the fixture ledger."""

    def lifecycle_record(self, kind: str, fields: dict, obs=None):
        rec = record(kind, target=None, actor=self.human(), fields=fields)
        return self.admission.admit_lifecycle(rec, sshsig(self.private, self.admission.lifecycle_message(rec)),
                                              self.baseline if obs is None else obs)

    def derived(self):
        view = Consequences(derive(read_chain(self.home.ledger_repository("demo"), "demo"), self.trees))
        return ([(o.kind, o.about) for o in view.obligations], [(f.code, f.about) for f in view.findings])

    def test_a_redaction_notice_is_admitted_with_no_derived_effect(self) -> None:
        """§24.2's rotation branch: "keep history; append a REDACTION_NOTICE; no guarantee yields"."""

        stored = sorted(self.entries()[0].objects)
        before = self.derived()
        position = self.lifecycle_record("REDACTION_NOTICE", {"objects": stored[:1]})
        self.assertEqual(self.entries()[-1].lifecycle["kind"], "REDACTION_NOTICE")
        self.assertEqual(self.entries()[-1].entry["obs"], self.baseline, "not a recovery entry: it carries obs")
        self.assertEqual(position, len(self.entries()) - 1)
        self.assertEqual(self.derived(), before)
        with self.assertRaisesRegex(EntryInvalid, "stores"):
            self.lifecycle_record("REDACTION_NOTICE", {"objects": ["sha256:" + "9" * 64]})

    def test_a_submitted_attestation_is_refused_with_its_references(self) -> None:
        from ssds.admission.request import request_message
        from ssds.ledger.read import with_id

        attest = with_id({**attestation("sha256:" + "9" * 64, ["nowhere"]), "actor": self.human()})
        req = self.request([attest], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        decision = self.admit(req)
        self.assertNotEqual(decision.decision, "ACCEPT")
        codes = set(dict(decision.refused).get(attest["id"], ())) | set(decision.reasons)
        self.assertIn("REF_TARGET", codes, "step 2's references run beside the refusal")

    def test_a_lineage_migration_and_a_replica_redesignation_are_refused(self) -> None:
        before = len(self.entries())
        with self.assertRaisesRegex(EntryInvalid, "Q-F16"):
            self.lifecycle_record("LINEAGE_MIGRATION", {"predecessor": {
                "ledger_id": "old", "last_position": 3, "last_entry_digest": "sha256:" + "3" * 64}})
        with self.assertRaisesRegex(AdmissionHalted, "reading F50"):
            rec = record("REPLICA_REDESIGNATION", target=None, actor=self.human(),
                         fields={"location": {"repository": "mirror:demo", "ref": ledger_ref("demo")}})
            self.admission.admit_lifecycle(rec, sshsig(self.private, self.admission.lifecycle_message(rec)), None)
        self.assertEqual(len(self.entries()), before)


if __name__ == "__main__":
    unittest.main()
