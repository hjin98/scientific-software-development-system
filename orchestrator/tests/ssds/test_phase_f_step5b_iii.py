"""Phase F step 5b-iii: Phase E's deferred refusals at Admission (Phase E plan §6; reading E32; catalogue §8.3
steps 2 and 7).

A ``COORDINATION_DECISION`` names the decision obligations it answers in ``target.records``: step 2 no longer reads
them as record references, and step 7 refuses an answer to a decision the head does not derive (a dropped part's,
or one never derived) and a ``PARTITION`` whose split fails partition lint for the holder whose decision it answers.
"""

from __future__ import annotations

import hashlib
import json
import unittest

from ssds.admission.checks import referenced_records
from ssds.admission.currency import Currency
from ssds.admission.legality import Legality
from ssds.derivation import trial
from ssds.ledger.read import with_id

from ._fixtures import admission_body, chain_of, record
from ._scenario import fresh
from .test_partition import PRINCIPAL, PartFlow


def partition(f: PartFlow, decision_id: str, parts) -> tuple[dict, dict[str, bytes]]:
    spec = json.dumps({"parts": [{"obligations": o, "write_scope": w} for o, w in parts], "order": []},
                      sort_keys=True).encode()
    digest = "sha256:" + hashlib.sha256(spec).hexdigest()
    rec = record("COORDINATION_DECISION", target={"records": [decision_id]}, outcome="PARTITION", actor=PRINCIPAL,
                 actor_class="HUMAN", fields={"tasks": []})
    rec["binding"] = fresh(PRINCIPAL, "coord-x", obligation=decision_id)  # a principal bound to the decision
    rec["refs"] = [{"store": "LEDGER", "digest": digest, "media_type": "application/json"}]
    return with_id(rec), {digest: spec}


def step7(f: PartFlow, rec: dict, objects=None) -> set[str]:
    sc = f.sc
    head = sc.derive()
    entry = admission_body(sc.position, sc.head, sc.head, records=[rec])
    tried = trial(chain_of("demo", sc.entries, sc.objects), sc.trees.__getitem__, entry, objects)
    return Legality(head, Currency(head).locate).codes(rec, tried)


class Decisions(unittest.TestCase):
    def setUp(self) -> None:
        self.f = PartFlow()
        self.f.spend(self.f.item().obligation)
        self.decision = self.f.budget_decision(self.f.item())

    def test_step_two_reads_a_decisions_names_as_obligations(self) -> None:
        rec, _ = partition(self.f, self.decision.id, [(["o1"], ["records"])])
        self.assertEqual(referenced_records(rec), set())
        other = record("FINDING", target={"records": [self.decision.id]}, fields={"materiality": "ROUTINE"})
        self.assertEqual(referenced_records(other), {self.decision.id}, "other kinds still name records")

    def test_a_valid_partition_passes_and_an_invalid_one_is_refused(self) -> None:
        good, objects = partition(self.f, self.decision.id, [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
        self.assertEqual(step7(self.f, good, objects), set())
        bad, objects = partition(self.f, self.decision.id, [(["o1"], ["records"]), (["o1", "o2"], ["notes.a", "notes.b"])])
        self.assertEqual(step7(self.f, bad, objects), {"OBLIGATION_PARTITION_INVALID"})

    def test_a_partition_without_its_parts_object_is_invalid(self) -> None:
        rec, _ = partition(self.f, self.decision.id, [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
        self.assertEqual(step7(self.f, rec, None), {"OBLIGATION_PARTITION_INVALID"})

    def test_each_round_reads_its_own_trial(self) -> None:
        """One ``Legality`` serves every round of the fixed point: a rebuilt trial is never read stale."""

        sc = self.f.sc
        head = sc.derive()
        legality = Legality(head, Currency(head).locate)
        good, objects = partition(self.f, self.decision.id, [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])

        def round_(objs):
            entry = admission_body(sc.position, sc.head, sc.head, records=[good])
            return trial(chain_of("demo", sc.entries, sc.objects), sc.trees.__getitem__, entry, objs)

        self.assertEqual(legality.codes(good, round_(objects)), set())
        self.assertEqual(legality.codes(good, round_(None)), {"OBLIGATION_PARTITION_INVALID"}, "its object gone")

    def test_an_answer_to_a_decision_not_derived_is_refused(self) -> None:
        stray, objects = partition(self.f, "sha256:" + "6" * 64, [(["o1"], ["records"])])
        self.assertEqual(step7(self.f, stray, objects), {"OBLIGATION_NOT_DERIVED"})
        good, objects = partition(self.f, self.decision.id, [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
        self.f.sc.objects[self.f.sc.position] = objects
        self.f.sc.admit(good)
        again, objects = partition(self.f, self.decision.id, [(["o1", "o2", "o3"], ["records", "notes.a", "notes.b"])])
        self.assertEqual(step7(self.f, again, objects), {"OBLIGATION_NOT_DERIVED"}, "answered: no longer derived")

    def test_a_bound_decision_obligation_must_be_derived(self) -> None:
        rec, objects = partition(self.f, self.decision.id, [(["o1"], ["records"]), (["o2", "o3"], ["notes.a", "notes.b"])])
        stray = with_id({**rec, "binding": {**rec["binding"], "obligation": "sha256:" + "7" * 64}})
        self.assertEqual(step7(self.f, stray, objects), {"OBLIGATION_NOT_DERIVED"})

    def test_a_decision_may_name_an_admitted_report(self) -> None:
        """Catalogue §3.4: a decision's target is "report(s) or item"."""

        from ._scenario import HUMAN

        report = with_id({**record("FINDING", target={"units": ["records"]}, fields={"materiality": "ROUTINE"}),
                          "actor": HUMAN})
        self.f.sc.admit(report)
        rec, _ = partition(self.f, report["id"], [])
        resolve = with_id({**rec, "outcome": "RESOLVE_LOCAL", "refs": [], "binding": {**rec["binding"], "obligation": None}})
        self.assertEqual(step7(self.f, resolve), set())

    def test_a_non_partition_answer_is_not_linted(self) -> None:
        rec, _ = partition(self.f, self.decision.id, [])
        amend = with_id({**rec, "outcome": "AMEND", "refs": []})
        self.assertEqual(step7(self.f, amend), set())


class Engine(unittest.TestCase):
    def test_a_decision_naming_an_obligation_passes_step_two(self) -> None:
        from ssds.admission.request import request_message

        from ._fixtures import sshsig
        from .test_admission_requests import RequestFixture

        fixture = RequestFixture("setUp")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)

        def decide(name: str):
            rec = with_id({**record("COORDINATION_DECISION", target={"records": [name]}, outcome="DECLINE",
                                    fields={"tasks": []}), "actor": fixture.human()})
            req = fixture.request([rec], base_position=len(fixture.entries()) - 1)
            req["binding"] = {"human": {"actor": fixture.human(),
                                        "signature": sshsig(fixture.private, request_message(req))}}
            return dict(fixture.admit(req).refused).get(rec["id"], ())

        self.assertNotIn("REF_RECORD", decide(fixture.obligation()))
        self.assertEqual(decide("sha256:" + "6" * 64), ("OBLIGATION_NOT_DERIVED",))


if __name__ == "__main__":
    unittest.main()
