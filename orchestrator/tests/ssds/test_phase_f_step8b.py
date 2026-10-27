"""Phase F step 8b: contract binding (catalogue §12.2, §13.6; plan §3.5, reading F66; SD-77).

An item task's envelope names the item's ``{unit, rev}``, and a system-kind task's names its system contract id,
``{system: <obligation kind>, version: <system version in force>}``, which schema 1 now admits in ``binding.item``
(SD-77, in place). Each record bound to the task copies the envelope's revision; Admission compares the two. The
brief's digest has one formula, shared by the Issuer and the renderer.
"""

from __future__ import annotations

import unittest
from types import SimpleNamespace

from ssds.derivation import Workflow, derive
from ssds.derivation.conformance import _scientific_review
from ssds.dispatcher import issue, would_issue
from ssds.dispatcher.journal import Journal
from ssds.interface.render import brief_digest
from ssds.ledger.read import with_id
from ssds.ledger.schema import record_violations

from ._fixtures import record
from .test_admission_requests import finding
from .test_phase_f_step8a import Fixture

GOVERNS = {"mode": "LEGACY", "protocol": "7.2.1"}


class Schema(unittest.TestCase):
    def binding(self, item) -> dict:
        rec = record("FINDING", target={"units": ["guide"]}, fields={"materiality": "ROUTINE"})
        return with_id({**rec, "actor": "agent:t/1", "actor_class": "AGENT", "binding": {
            "task": "t", "obligation": "o", "role": "REVIEWER", "lineage": [], "lineage_class": "UNKNOWN",
            "envelope": "sha256:" + "0" * 64, "item": item}})

    def test_binding_item_admits_an_item_or_a_system_contract_id(self) -> None:
        self.assertEqual(record_violations(self.binding({"unit": "guide", "rev": "sha256:" + "1" * 64})), [])
        self.assertEqual(record_violations(self.binding({"system": "ACCEPT", "version": "ssds-rules/1"})), [])
        for bad in ({"system": "ACCEPT"}, {"system": "ACCEPT", "version": "v", "unit": "guide"},
                    {"unit": "guide", "rev": "x"}, "ACCEPT"):
            with self.subTest(item=bad):
                self.assertTrue(record_violations(self.binding(bad)))


class ContractRevision(Fixture):
    def workflow(self) -> Workflow:
        return Workflow(derive(self.chain(), self.trees))

    def test_a_system_task_names_its_kind_and_the_system_version_in_force(self) -> None:
        w = self.workflow()
        accept = next(o for o in w.obligations if o.kind == "ACCEPT")
        self.assertEqual(w.contract_revision(accept), {"system": "ACCEPT", "version": "ssds-rules/1"})

    def test_an_item_task_names_the_items_revision(self) -> None:
        w = self.workflow()
        accept = next(o for o in w.obligations if o.kind == "ACCEPT")
        w.item_of = lambda o: SimpleNamespace(unit="guide")  # an item obligation on the fixture's unit
        self.assertEqual(w.contract_revision(accept), {"unit": "guide", "rev": w.s.view.rev("guide")})

    def test_the_would_issue_set_carries_each_tasks_contract(self) -> None:
        for t in would_issue(self.chain(), self.trees, self.held()):
            self.assertEqual(t.contract_revision, self.workflow().contract_revision(
                next(o for o in self.workflow().obligations if o.id == t.obligation_id)))


class Binding(Fixture):
    """An issued system task: a record copying the envelope's contract id authenticates; one without does not."""

    def issued(self):
        task = would_issue(self.chain(), self.trees, self.held())[0]
        issued = issue(Journal(self.home, "demo"), self.issuer, task, self.held(), governs=GOVERNS, route="HARNESS")
        return task, issued

    def codes(self, issued, item) -> tuple[str, ...]:
        rec = self.bind(with_id({**finding(note=str(item)), "governs": GOVERNS}), issued)
        if item is not None:
            rec = with_id({**rec, "binding": {**rec["binding"], "item": item}})
        decision = self.admit(self.signed(issued, [rec]))
        return tuple(dict(decision.refused).get(rec["id"], ())) + tuple(decision.reasons)

    def test_the_envelope_names_the_system_contract(self) -> None:
        task, issued = self.issued()
        self.assertEqual(issued.envelope["contract_revision"], {"system": task.kind, "version": "ssds-rules/1"})

    def test_a_record_copies_the_envelopes_contract_or_is_refused(self) -> None:
        _, issued = self.issued()
        self.assertNotIn("AUTH_ENVELOPE", self.codes(issued, issued.envelope["contract_revision"]))
        self.assertIn("AUTH_ENVELOPE", self.codes(issued, None), "a record names the contract it works under")
        self.assertIn("AUTH_ENVELOPE", self.codes(issued, {"system": "REVIEW", "version": "ssds-rules/1"}))


class Digest(unittest.TestCase):
    def test_one_brief_digest_formula(self) -> None:
        import hashlib

        self.assertEqual(brief_digest(b"brief"), "sha256:" + hashlib.sha256(b"brief").hexdigest())


class Readers(unittest.TestCase):
    def test_a_system_contract_id_names_no_item(self) -> None:
        """A reader that resolves an item revision passes over a system id (SD-77)."""

        rec = {"binding": {"item": {"system": "REVIEW", "version": "ssds-rules/1"}}}
        w = SimpleNamespace(submitting_result=lambda x: "r", s=SimpleNamespace(
            record=lambda rid: rec, plans=SimpleNamespace(item_at=lambda u, r: self.fail("no item is resolved"))))
        self.assertFalse(_scientific_review(w, SimpleNamespace(target={"transformation": "x"})))


    def test_a_reviews_brief_over_a_system_bound_result(self) -> None:
        """Briefing reads the submitting result's item only when it names one (SD-77)."""

        from ssds.ledger.read import transformation_id

        from ._scenario import Scenario, agent, fresh, tree
        from .test_phase_f_step4d import FILES, THREE

        sc = Scenario(THREE, dict(FILES))
        base = sc.head
        candidate = sc.add_tree(tree({**FILES, "arch.md": "a2\n"}, sc.manifest))
        x = transformation_id(base, candidate)
        result = record("TASK_RESULT", target={"task": "task-1", "candidate": candidate, "transformation": x,
                                               "base": base}, outcome="COMPLETE", actor=agent("a"),
                        actor_class="AGENT", frame={"transformation": x})
        result["binding"] = {**fresh(agent("a"), "task-1"), "item": {"system": "IMPLEMENT", "version": "ssds-rules/1"}}
        sc.admit(with_id(result))
        w = Workflow(sc.derive())
        from ssds.derivation.workflow import make

        review = make("REVIEW", {"transformation": x})  # the obligation a review of ``x`` would answer
        self.assertIsNotNone(w.briefing.work(review))


if __name__ == "__main__":
    unittest.main()
