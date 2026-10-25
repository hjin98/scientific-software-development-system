"""Phase F step 4a: the trial extension (reading F10).

Admission judges a request in the state derivation computes as if the request's entry were appended. These
cases build real shadow ledgers, append real entries through the Admission engine and compare the trial of each
entry, taken before it was appended, with derivation from the ledger after it was.
"""

from __future__ import annotations

import unittest

from ssds.derivation import Workflow, derive, trial
from ssds.ledger.read import read_chain, with_id

from ._fixtures import record
from .test_admission_requests import RequestFixture, finding


class TrialExtension(RequestFixture):
    def chain(self):
        return read_chain(self.home.ledger_repository("demo"), "demo")

    def assert_same_state(self, tried, derived) -> None:
        a, b = tried.s, derived.s
        self.assertEqual(a.n, b.n)
        self.assertEqual({rid: (f.position, f.record) for rid, f in a.records.items()},
                         {rid: (f.position, f.record) for rid, f in b.records.items()})
        self.assertEqual((a.h.head(a.n), dict(a.h.sigma(a.n)), dict(a.h.modes(a.n))),
                         (b.h.head(b.n), dict(b.h.sigma(b.n)), dict(b.h.modes(b.n))))
        self.assertEqual(sorted(o.id for o in Workflow(tried).obligations),
                         sorted(o.id for o in Workflow(derived).obligations))
        self.assertEqual({rid: tried.current(rid) for rid in a.records}, {rid: derived.current(rid) for rid in b.records})

    def test_a_trial_equals_the_state_after_admitting_the_same_entry(self) -> None:
        issued = self.issue()
        first = self.bind(finding(materiality="MATERIAL"), issued)
        second = self.bind(record("FINDING", target={"records": [first["id"]]}, fields={"materiality": "ROUTINE"}),
                           issued)
        before = self.chain()
        decision = self.admit(self.signed(issued, [first, second]))
        self.assertEqual(len(decision.admitted), 2)
        after = self.chain()
        entry = after.entries[-1]
        self.assert_same_state(trial(before, self.trees, entry.entry, entry.objects), derive(after, self.trees))
        tried = self.admission.trial(before, entry.entry, entry.objects)
        self.assert_same_state(tried, derive(after, self.trees))

    def test_a_trial_of_a_human_bound_entry_equals_its_admission(self) -> None:
        from ssds.admission.request import request_message

        from ._fixtures import sshsig

        mine = with_id({**finding(), "actor": self.human()})
        req = self.request([mine], base_position=len(self.entries()) - 1)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        before = self.chain()
        self.assertEqual(self.admit(req).admitted, (mine["id"],))
        after = self.chain()
        self.assert_same_state(trial(before, self.trees, after.entries[-1].entry, after.entries[-1].objects),
                               derive(after, self.trees))

    def test_a_trial_writes_nothing_and_changes_no_held_state(self) -> None:
        before = self.chain()
        held = derive(before, self.trees)
        obligations = sorted(o.id for o in Workflow(held).obligations)
        issued = self.issue()
        rec = self.bind(finding(), issued)
        head = before.entries[before.readable_through]
        entry = self.admission.admission_entry(head, self.baseline, "sha256:" + "0" * 64, "ACCEPT", [], [rec], [],
                                               self.baseline)
        tried = self.admission.trial(before, entry)
        self.assertIn(rec["id"], tried.s.records)
        self.assertNotIn(rec["id"], held.s.records)
        self.assertEqual(sorted(o.id for o in Workflow(held).obligations), obligations)
        self.assertEqual([e.digest for e in self.chain().entries], [e.digest for e in before.entries],
                         "the ledger is unchanged")
        self.assertEqual(len(before.entries), head.position + 1)

    def test_a_trial_entry_takes_the_next_position_only(self) -> None:
        before = self.chain()
        head = before.entries[-1]
        entry = self.admission.admission_entry(head, self.baseline, "sha256:" + "0" * 64, "ACCEPT", [], [], [],
                                               self.baseline)
        for position in (head.position, head.position + 2):
            with self.subTest(position=position), self.assertRaises(ValueError):
                trial(before, self.trees, {**entry, "position": position})


if __name__ == "__main__":
    unittest.main()
