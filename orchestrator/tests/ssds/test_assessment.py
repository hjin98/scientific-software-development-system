"""Acceptance group 2 (derivation half): the matching predicates and staleness (catalogue §6.5-§6.6; Manual §6.5-§6.6).

Expected values are transcribed from ``cases_s5_6.py`` (named per test). A model
run becomes a ``REALIZATION`` whose execution basis records, under its own
resolution context, the content identities of the terms it read on the tree it
ran on, with its pins, attributes and bound.
"""

from __future__ import annotations

import unittest

from ssds.content import Tree, recorded_identity

from ._scenario import attested
from ._fixtures import manifest, tree
from ssds.derivation import F
from ssds.derivation.evidence import obligation_token

from ._scenario import HUMAN_B, Scenario, challenge, content, judgment, on_record, store

UNITS = '''
    [[unit]]
    id = "code"
    kind = "D4"
    scope = [{ path = "a.py" }]
    [[unit]]
    id = "spec"
    kind = "EVIDENCE_SPEC"
    scope = [{ path = "s.py" }, { path = "s.ssds-spec.toml" }]
'''
SPEC = "# ssds:rel EVIDENCES code\ndef check():\n    return 1\n"
#: The specification's declaration (catalogue §17.1; Phase F step 9b): one output judged by an embedded verdict, a
#: declared enum output (F85).
DECLARATION = """oracle = "EMBEDDED"
runner = "ci"
time_bound_hours = 24
outputs = [{ name = "x", type = "int" }, { name = "x_verdict", type = "enum", values = ["PASS", "FAIL"] }]
verdicts = [{ output = "x", embedded = "x_verdict" }]
"""
POLICY = 'schema = 1\n[domains.D4]\nevidence = true\n'
#: The evidence obligation the specification's EVIDENCES relation to ``code`` derives (§10.2; Phase F reading F87).
OBL = obligation_token("code", "spec")
CODE_TERM = {"path": "a.py"}
SPEC_TERM = {"file": "s.py", "symbol": "check"}
#: Evaluated outcomes in §17.3's shape: {output name: canonical value} (F85).
BAD = {"x": 1, "x_verdict": "FAIL"}
GOOD = {"x": 2, "x_verdict": "PASS"}


class Runs:
    def __init__(self, other: bool = False) -> None:
        self.files = {"a.py": "v = 1\n", "s.py": SPEC, "s.ssds-spec.toml": DECLARATION}
        if other:
            self.files["other.txt"] = "1\n"
        self.sc = Scenario(UNITS, self.files, policy=POLICY)
        self.trees: dict[str, str] = {"T0": self.sc.head}
        self.completeness: dict[str, str] = {}

    def tree(self, name: str, **changes: str) -> str:
        if name not in self.trees:
            files = dict(self.files, **changes)
            self.trees[name] = self.sc.add_tree(tree(files, UNITS))
        return self.trees[name]

    def bound_judgment(self, head: str) -> str:
        if head not in self.completeness:
            view = self.sc.view(head)
            c = judgment("COMPLETENESS", {"scope": ["code", "spec"], "classes": ["EXEC"],
                                          "membership": view.membership_digest(("code", "spec"))}, "COMPLETE",
                         actor=HUMAN_B, basis=[content("code", view.rev("code")), content("spec", view.rev("spec"))])
            self.sc.admit(*attested(c))
            self.completeness[head] = c["id"]
        return self.completeness[head]

    def run(self, head: str, outcome: dict, *, pins=("p1",), attributes=(), unpinnable=False, bounded=True,
            bounded_by: list[str] | None = None) -> dict:
        t: Tree = self.sc.trees[head]
        view = self.sc.view(head)
        basis = {"tree": head, "context": {"system": "ssds-rules/1", "ignore": [], "analyzers": ["ssds.analyzer.python/1"]},
                 "pins": [["dataset:input", p] for p in pins], "unpinnable": unpinnable,
                 "attributes": [list(a) for a in attributes]}
        if bounded:
            basis["units"] = [{"unit": "code", "rev": view.rev("code"), "terms": [[CODE_TERM, recorded_identity(t, CODE_TERM, ())]]},
                              {"unit": "spec", "rev": view.rev("spec"), "terms": [[SPEC_TERM, recorded_identity(t, SPEC_TERM, ())]]}]
            basis["bounded_by"] = bounded_by if bounded_by is not None else [self.bound_judgment(head)]
        else:
            basis["units"] = []
            basis["widened"] = [[{"tracked": "*"}, recorded_identity(t, {"tracked": "*"}, ())]]
            basis["bounded_by"] = "UNBOUNDED"
        digest = store(self.sc, outcome)
        realization = judgment("REALIZATION", {"spec": {"unit": "spec", "rev": view.rev("spec")},
                                               "claim": [{"unit": "code", "rev": view.rev("code")}]}, "COMPLETE",
                               actor="machinery:dispatcher@ed25519:test", actor_class="MACHINERY",
                               fields={"execution": basis, "configuration": {"regime": "default"}, "evaluated": digest})
        from ssds.ledger.read import with_id

        self.attempts = getattr(self, "attempts", 0) + 1
        realization = with_id({**realization, "provenance": {"attempt": self.attempts}})  # distinct executions
        self.sc.admit(realization)
        return realization

    def fail(self, realization: dict) -> dict:
        view = self.sc.view(self.trees["T0"])
        a = judgment("EVIDENCE_ASSESSMENT", {"realization": realization["id"], "obligation": OBL}, "FAIL", actor=HUMAN_B,
                     basis=[on_record(realization["id"]), content("spec", view.rev("spec"))],
                     fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": view.rev("spec")}, "failing_outputs": ["x"]})
        self.sc.admit(a)
        return a

    def stale(self, failing: dict, state: str) -> bool:
        self.sc.absorb({k: v.data.decode() for k, v in self.sc.trees[self.trees[state]].items() if k != ".ssds/manifest.toml"})
        d = self.sc.derive()
        return d.a.stale(failing["id"], d.base)


class Staleness(unittest.TestCase):
    """cases_s5_6.py."""

    def test_genuine_fix_is_stale(self) -> None:
        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(t0, BAD))
        r.run(t0, BAD)
        r.run(t1, GOOD)
        self.assertTrue(r.stale(failing, "T1"))

    def test_revert_yields_again(self) -> None:
        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(t0, BAD))
        r.run(t0, BAD)
        r.run(t1, GOOD)
        self.assertFalse(r.stale(failing, "T0"))

    def test_differing_pin_goes_to_owner(self) -> None:
        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(t0, BAD))
        r.run(t0, BAD)
        r.run(t0, GOOD, pins=("p2",))
        r.run(t1, GOOD)
        self.assertFalse(r.stale(failing, "T1"), "nondeterministic in fact: the owner's")

    def test_differing_free_attribute_goes_to_owner(self) -> None:
        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        cpu, gpu = (("backend", "cpu"),), (("backend", "gpu"),)
        failing = r.fail(r.run(t0, BAD, attributes=cpu))
        r.run(t0, BAD, attributes=cpu)
        r.run(t0, GOOD, attributes=gpu)
        r.run(t1, GOOD, attributes=cpu)
        self.assertFalse(r.stale(failing, "T1"))

    def test_unpinnable_supports_no_stop(self) -> None:
        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(t0, BAD, unpinnable=True))
        r.run(t0, BAD, unpinnable=True)
        r.run(t1, GOOD, unpinnable=True)
        self.assertFalse(r.stale(failing, "T1"))

    def test_unbounded_run_still_linked(self) -> None:
        r = Runs(other=True)
        w0 = r.tree("T0")
        w0b = r.tree("W0b", **{"other.txt": "2\n"})
        w1 = r.tree("W1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(w0, BAD, bounded=False))
        r.run(w0, BAD)
        r.run(w0b, GOOD, bounded=False)
        r.run(w1, GOOD)
        self.assertFalse(r.stale(failing, "W1"), "the unbounded differing run is linked through the narrow reproduction")

    def test_context_change_keeps_implication(self) -> None:
        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        runs = [r.run(t0, BAD), r.run(t1, GOOD)]
        failing = r.fail(runs[0])
        d = r.sc.derive()
        for o in runs:
            for head in (t0, t1):
                k = r.sc.trees[head]
                if d.a.on_plus(o["id"], k, failing["target"]["realization"], d.base):
                    self.assertTrue(d.a.on_minus(o["id"], k), "on⁺ ⇒ on⁻")
        before = d.a.on_minus(runs[0]["id"], r.sc.trees[t1])
        r.sc.structure = r.sc.structure.override(("governed", "ignore"), ("a.py",))
        self.assertEqual(r.sc.derive().a.on_minus(runs[0]["id"], r.sc.trees[t1]), before,
                         "on⁻ reads only the record's own context, never the current structure")


class DisputeEffects(unittest.TestCase):
    def test_a_stale_failure_no_longer_caps_validity(self) -> None:
        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(t0, BAD))
        r.run(t0, BAD)
        r.run(t1, GOOD)
        r.stale(failing, "T1")
        d = r.sc.derive()
        self.assertEqual(d.a.adverse("code", OBL, d.base), [])
        r2 = Runs()
        failing2 = r2.fail(r2.run(r2.tree("T0"), BAD))
        d2 = r2.sc.derive()
        self.assertEqual(d2.a.adverse("code", OBL, d2.base), [failing2["id"]], "with no reproduction it counts")



class BoundingCurrency(unittest.TestCase):
    """SD-58 (Manual A8): a bounding judgment is checked on the content the run ran on.

    The discriminators the 0e49deb Review (SC-1) asked to keep: the genuine fix and its revert
    (``Staleness``), the bounding judgment challenged, its membership not that of the run's content,
    and a premise other than content, which holds in the state of evaluation.
    """

    def setUp(self) -> None:
        self.r = Runs()
        self.t0, self.t1 = self.r.tree("T0"), self.r.tree("T1", **{"a.py": "v = 2\n"})

    def completeness(self, head: str, membership: str | None = None, extra=()) -> dict:
        view = self.r.sc.view(head)
        c = judgment("COMPLETENESS", {"scope": ["code", "spec"], "classes": ["EXEC"],
                                      "membership": membership or view.membership_digest(("code", "spec"))},
                     "COMPLETE", actor=HUMAN_B,
                     basis=[content("code", view.rev("code")), content("spec", view.rev("spec")), *extra])
        self.r.sc.admit(*attested(c))
        return c

    def stale(self, failing: dict) -> bool:
        files = {k: v.data.decode() for k, v in self.r.sc.trees[self.t1].items() if k != ".ssds/manifest.toml"}
        self.r.sc.absorb(files)
        d = self.r.sc.derive()
        return d.a.stale(failing["id"], d.base, lambda node: d.values.get(node, F))

    def scenario(self, bounding: dict) -> dict:
        failing = self.r.fail(self.r.run(self.t0, BAD))
        self.r.run(self.t0, BAD, bounded_by=[bounding["id"]])
        self.r.run(self.t1, GOOD)
        return failing

    def test_a_challenged_bounding_judgment_bounds_nothing(self) -> None:
        bounding = self.completeness(self.t0)
        failing = self.scenario(bounding)
        self.r.sc.admit(challenge({"record": bounding["id"]}))
        self.assertFalse(self.stale(failing))

    def test_an_incomplete_judgment_never_bounds(self) -> None:
        """Review 517af45 A-B6: a denial of completeness is not a certificate of it."""

        view = self.r.sc.view(self.t0)
        denial = judgment("COMPLETENESS", {"scope": ["code", "spec"], "classes": ["EXEC"],
                                           "membership": view.membership_digest(("code", "spec"))},
                          "INCOMPLETE", actor=HUMAN_B,
                          basis=[content("code", view.rev("code")), content("spec", view.rev("spec"))])
        self.r.sc.admit(denial)
        failing = self.scenario(denial)
        self.assertFalse(self.stale(failing), "the adverse judgment stays adverse")

    def test_membership_is_checked_on_the_runs_content(self) -> None:
        failing = self.scenario(self.completeness(self.t0, membership="sha256:" + "0" * 64))
        self.assertFalse(self.stale(failing), "a judgment over other membership does not bound this run")

    def test_a_cited_record_premise_holds_in_the_state_of_evaluation(self) -> None:
        cited = judgment("ACCEPTANCE", self.r.sc.triple("spec"), "PASS", actor=HUMAN_B,
                         basis=[content("spec", self.r.sc.rev("spec"))])
        self.r.sc.admit(*attested(cited))
        failing = self.scenario(self.completeness(self.t0, extra=[on_record(cited["id"])]))
        self.assertTrue(self.stale(failing), "the cited acceptance is current: the run is bounded")
        r = self.r
        r.sc.admit(*attested(challenge({"record": cited["id"]})))
        d = r.sc.derive()
        self.assertFalse(d.a.stale(failing["id"], d.base, lambda node: d.values.get(node, F)),
                         "the cited record is blocked now: the premise fails in the state of evaluation")
        self.assertFalse(d.a.stale(failing["id"], d.base), "without S2 values a record premise fails closed")

if __name__ == "__main__":
    unittest.main()


class Group2Discriminators(unittest.TestCase):
    """G2 workplan §5.3 group 2, the derivation half."""

    def test_a_failure_whose_only_reproductions_are_unbounded_stays_counting(self) -> None:
        # 5c55d4b N6
        r = Runs()
        t0, t1 = r.tree("T0"), r.tree("T1", **{"a.py": "v = 2\n"})
        failing = r.fail(r.run(t0, BAD, bounded=False))
        r.run(t0, BAD, bounded=False)
        r.run(t1, GOOD)
        self.assertFalse(r.stale(failing, "T1"))

    def test_each_link_traversed_is_recorded(self) -> None:
        # 798b2b4 B4
        r = Runs(other=True)
        w0, w0b, w1 = r.tree("T0"), r.tree("W0b", **{"other.txt": "2\n"}), r.tree("W1", **{"a.py": "v = 2\n"})
        failing_run = r.run(w0, BAD, bounded=False)
        failing = r.fail(failing_run)
        reproduction = r.run(w0, BAD)
        differing = r.run(w0b, GOOD, bounded=False)
        r.run(w1, GOOD)
        r.stale(failing, "W1")
        d = r.sc.derive()
        explanation = d.a.explain(failing["id"], d.base)
        self.assertIn(differing["id"], explanation["differed"])
        self.assertIn(("failing-content", differing["id"], reproduction["id"]), explanation["links"],
                      "the differing run is linked through the narrow reproduction, and the link is shown")

    def test_challenges_on_a_disputed_claim(self) -> None:
        # 29da56e N5: an upheld challenge against the realization disposes; a counter-challenge restores the dispute
        from ._scenario import adjudication, challenge

        r = Runs()
        realization = r.run(r.tree("T0"), BAD)
        failing = r.fail(realization)
        d = r.sc.derive()
        self.assertEqual(d.a.adverse("code", OBL, d.base), [failing["id"]])
        c = challenge({"record": realization["id"]})
        upheld = adjudication(c["id"], "UPHELD", actor="human:SHA256:adjudicator")
        r.sc.admit(*attested(c, upheld))
        d = r.sc.derive()
        self.assertEqual(d.a.disposition(failing["id"], d.values.get, d.base, d.j.nonind), 2,
                         "an upheld challenge of the failing run's realization disposes of the failure")
        counter = challenge({"record": upheld["id"]}, actor="human:SHA256:carol")
        r.sc.admit(*attested(counter, adjudication(counter["id"], "UPHELD", actor="human:SHA256:dave")))
        d = r.sc.derive()
        self.assertEqual(d.a.disposition(failing["id"], d.values.get, d.base, d.j.nonind), 0,
                         "the upholding is itself overturned: the dispute is live again")
        dismissed = challenge({"record": failing["id"]}, actor="human:SHA256:erin")
        r.sc.admit(*attested(dismissed, adjudication(dismissed["id"], "DISMISSED", actor="human:SHA256:frank")))
        d = r.sc.derive()
        self.assertEqual(d.a.disposition(failing["id"], d.values.get, d.base, d.j.nonind), 0,
                         "a dismissed challenge disposes of nothing")
