"""Phase F step 9d-i: admitting a runner's realization (catalogue §8.3 steps 1-2 and 6, §6.3, §6.9, §17.2-§17.5;
plan §3.6, readings F96-F99).

A realization's execution is read through derivation's one reader: outside its closed shape it is ``SCHEMA_RECORD``.
It is admitted only in the admitted state, on the head of an admitted position ``k`` (else ``SCHEMA_UNSUPPORTED``,
SD-70), with the specification's and claims' revisions ``view(k)``'s (``REF_TARGET``), every recorded term
re-resolving in its tree (``REF_EXECUTION``), its bounding judgments admitted (``REF_RECORD``), ``k ≤ start ≤ end ≤
n`` (``REF_EXECUTION``) and its evaluated outcome a stored JSON object (``REF_OBJECT``, ``SCHEMA_OBJECT``). Only
machinery records one (F98). Expected values are from §8.3, §6.3, §17.2 and SD-70 (no Stage S case covers them).
"""

from __future__ import annotations

import hashlib
import unittest

from ssds.content import recorded_identity
from ssds.ledger.read import with_id

from .test_phase_f_step4b import derive_state
from .test_phase_f_step9a import OUTCOME_DIGEST, OUTCOME_TEXT, Fixture


class Realizations(Fixture):
    def setUp(self) -> None:
        super().setUp()
        self.lifecycle("REGISTER", self.runner.trust_root())

    def realization(self, **execution) -> dict:
        obs = self.observation()
        fields = {**obs["fields"], "execution": {**obs["fields"]["execution"], **execution}}
        return with_id({**obs, "fields": fields})

    def codes(self, rec, objects=None) -> tuple:
        request = self.request([rec], base_position=self.head(),
                               objects={OUTCOME_DIGEST: OUTCOME_TEXT} if objects is None else objects)
        decision = self.admit(self.runner.sign(request))
        return tuple(sorted(set(dict(decision.refused).get(rec["id"], ())) | set(decision.reasons)))

    def term(self):
        s = derive_state(self)
        tree = s.h.trees(s.h.head(s.n))
        path = next(p for p in sorted(tree) if not p.startswith(".ssds/"))
        return {"path": path}, recorded_identity(tree, {"path": path}, ())


class Accepted(Realizations):
    def test_a_realization_on_the_head_is_admitted_and_its_outcome_stored(self) -> None:
        term, identity = self.term()
        s = derive_state(self)
        unit = next(iter(s.view.structure.units))
        rec = self.realization(units=[{"unit": unit, "rev": s.view.rev(unit), "terms": [[term, identity]]}])
        self.assertEqual(self.codes(rec), ())
        d = derive_state(self)
        self.assertIn(rec["id"], d.records)
        self.assertEqual(d.h.objects.get(OUTCOME_DIGEST), OUTCOME_TEXT.encode(), "stored beside it (F97)")

    def test_a_late_run_on_an_older_admitted_head(self) -> None:
        """§6.9: the head it ran on need not be the current one."""

        rec = self.realization()
        self.lifecycle("REGISTER", type(self.runner)().trust_root())  # a later position, the same product tree
        self.assertEqual(self.codes(rec), ())


class Shape(Realizations):
    def test_each_malformed_member_is_schema_record(self) -> None:
        cases = {"no tree": {"tree": None}, "a context not closed": {"context": {"system": "ssds-rules/1"}},
                 "units not typed": {"units": [{"unit": "u"}]}, "bounded_by": {"bounded_by": "SOME"},
                 "no start": {"start": None}, "start after end": {"start": 2, "end": 1},
                 "pins": {"pins": [["a"]]}, "unpinnable": {"unpinnable": "no"}, "reads": {"reads": [["t", "c"]]},
                 "an unknown member": {"extra": 1}, "a runner of another key": {"runner": {"class": "ci",
                                                                                           "key": "ed25519:x"}}}
        for name, change in cases.items():
            with self.subTest(case=name):
                execution = {k: v for k, v in change.items() if v is not None}
                rec = self.realization(**execution)
                if None in change.values():
                    fields = dict(rec["fields"])
                    fields["execution"] = {k: v for k, v in fields["execution"].items() if k not in change
                                           or change[k] is not None}
                    rec = with_id({**rec, "fields": fields})
                self.assertEqual(self.codes(rec), ("SCHEMA_RECORD",))


class References(Realizations):
    def test_a_tree_that_is_no_admitted_head_is_unsupported(self) -> None:
        """SD-70: a candidate's or merged tree's evidence."""

        self.assertEqual(self.codes(self.realization(tree="1" * 40)), ("SCHEMA_UNSUPPORTED",))

    def test_a_target_revision_not_of_its_tree(self) -> None:
        rec = self.observation()
        rec = with_id({**rec, "target": {**rec["target"], "spec": {**rec["target"]["spec"], "rev": "sha256:" + "0" * 64}}})
        self.assertIn("REF_TARGET", self.codes(rec))

    def test_a_revision_of_another_admitted_head(self) -> None:
        """The revision exists, but at another position: the run's tree is ``view(k)``'s (F97)."""

        from ssds.admission.engine import Admission

        from ._fixtures import commit

        old_tree = derive_state(self).h.head(0)
        (self.product / "guide.md").write_text((self.product / "guide.md").read_text() + "\nrevised\n")
        obs = commit(self.product, "a revised guide")
        admission = Admission(self.home, "demo", self.trees, product=self.product)
        admission.absorb(self.entries(), obs)
        new = self.target()  # the guide's revision at the new head
        rec = self.realization(tree=old_tree, start=0)
        rec = with_id({**rec, "target": new})
        request = self.request([rec], base_position=self.head(), base_commit=obs,
                               objects={OUTCOME_DIGEST: OUTCOME_TEXT})
        decision = admission.admit(self.runner.sign(request), obs)
        self.assertEqual(dict(decision.refused).get(rec["id"]), ("REF_TARGET",))

    def test_frame_evidence_is_unsupported(self) -> None:
        """SD-70: a realization in a transformation's frame."""

        rec = with_id({**self.realization(), "frame": {"transformation": "sha256:" + "7" * 64}})
        self.assertIn("SCHEMA_UNSUPPORTED", self.codes(rec))

    def test_a_tampered_term_identity(self) -> None:
        term, identity = self.term()
        s = derive_state(self)
        unit = next(iter(s.view.structure.units))
        tampered = "sha256:" + hashlib.sha256(b"other").hexdigest()
        rec = self.realization(units=[{"unit": unit, "rev": s.view.rev(unit), "terms": [[term, tampered]]}])
        self.assertEqual(self.codes(rec), ("REF_EXECUTION",))

    def test_a_context_the_host_lacks(self) -> None:
        rec = self.realization(context={"system": "ssds-rules/9", "ignore": [], "analyzers": []})
        self.assertEqual(self.codes(rec), ("SCHEMA_UNSUPPORTED",), "§6.3: it makes no current assertion")

    def test_it_ends_by_the_head(self) -> None:
        n = self.head()  # a decision appends: read the head afresh for each request
        self.assertEqual(self.codes(self.realization(end=n + 1, start=n)), ("REF_EXECUTION",))

    def test_it_starts_once_its_tree_is_admitted(self) -> None:
        """``k ≤ start``: the tree is first a head at a later position (plan check of b5364cc3, answer 1)."""

        from ssds.admission.engine import Admission

        from ._fixtures import commit

        (self.product / "notes.md").write_text("observed later\n")
        obs = commit(self.product, "a change of unknown provenance")
        admission = Admission(self.home, "demo", self.trees, product=self.product)
        admission.absorb(self.entries(), obs)
        s = derive_state(self)
        k = s.n
        self.assertEqual((s.h.head(k), s.h.head(k - 1) != obs), (obs, True), "first a head at k")
        for start, expected in ((k - 1, ("REF_EXECUTION",)), (k, ())):
            with self.subTest(start=start):
                rec = self.realization(tree=obs, start=start, end=self.head())
                request = self.request([rec], base_position=self.head(), base_commit=obs,
                                       objects={OUTCOME_DIGEST: OUTCOME_TEXT})
                decision = admission.admit(self.runner.sign(request), obs)
                self.assertEqual(tuple(dict(decision.refused).get(rec["id"], ())) + tuple(decision.reasons), expected)

    def test_a_bounding_judgment_not_admitted(self) -> None:
        self.assertEqual(self.codes(self.realization(bounded_by=["sha256:" + "5" * 64])), ("REF_RECORD",))

    def test_its_outcome_object(self) -> None:
        self.assertEqual(self.codes(self.realization(), objects={}), ("REF_OBJECT",))
        listed = "[1]"
        digest = "sha256:" + hashlib.sha256(listed.encode()).hexdigest()
        rec = self.observation()
        rec = with_id({**rec, "fields": {**rec["fields"], "evaluated": digest}})
        self.assertEqual(self.codes(rec, objects={digest: listed}), ("SCHEMA_OBJECT",), "§17.3's {name: value}")


class Actors(Realizations):
    def test_only_machinery_records_one(self) -> None:
        """F98: the machinery floor, beside the reader's own actor check."""

        from ssds.derivation import Support

        support = Support.__new__(Support)
        support.s = derive_state(self)
        for actor_class in ("HUMAN", "AGENT"):
            with self.subTest(actor_class=actor_class):
                self.assertFalse(support.qualified({"kind": "REALIZATION", "actor_class": actor_class}, None))
        self.assertTrue(support.qualified({"kind": "REALIZATION", "actor_class": "MACHINERY"}, None))

    def test_a_retired_or_compromised_key_admits_nothing(self) -> None:
        for action in ("RETIRE", "COMPROMISED"):
            with self.subTest(action=action):
                fixture = type(self)(self._testMethodName)
                fixture.setUp()
                try:
                    rec = fixture.realization()
                    fixture.lifecycle(action, fixture.runner.trust_root())
                    decision = fixture.admit(fixture.runner.sign(fixture.request(
                        [rec], base_position=fixture.head(), objects={OUTCOME_DIGEST: OUTCOME_TEXT})))
                    self.assertEqual(decision.admitted, ())
                finally:
                    fixture.doCleanups()


class Salvage(Realizations):
    def test_a_realization_is_salvaged_from_a_request_rejected_on_its_merits(self) -> None:
        """§8.3 step 6: a designated runner's observation is never lost (F99)."""

        good = self.realization()
        bad = self.realization(tree="1" * 40, start=0, end=0)
        decision = self.admit(self.runner.sign(self.request([good, bad], base_position=self.head(),
                                                            objects={OUTCOME_DIGEST: OUTCOME_TEXT})))
        self.assertEqual(decision.admitted, (good["id"],))
        self.assertIn(bad["id"], dict(decision.refused))


if __name__ == "__main__":
    unittest.main()
