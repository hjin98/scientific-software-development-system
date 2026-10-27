"""Phase F step 9c-i: the evidence obligation's identity (catalogue §10.2, §6.2, §25.3; plan §3.6, readings F75, F87;
plan checks of 298a12a0 and abcd03de).

An evidence obligation is ``(claim unit lineage, specification unit lineage)``, its token ``evidence:`` and a digest
of the two lineage roots. A subject requires the obligation of every authored ``EVIDENCES`` relation to a claim unit
inside it when policy requires evidence for its domain. A rename keeps the identity; a retarget, a split or a
retirement never disposes of a failing assessment; assessments for different obligations never conflict.
"""

from __future__ import annotations

import unittest

from ssds.derivation import Policy
from ssds.derivation.evidence import obligation_token

from ._scenario import HUMAN_B, Scenario, agent, content, integrate, judgment, on_record, submit
from .test_assessment import BAD, DECLARATION, GOOD, OBL, POLICY, SPEC, UNITS, Runs

TWO_SPECS = UNITS + '''
    [[unit]]
    id = "spec2"
    kind = "EVIDENCE_SPEC"
    scope = [{ path = "t.py" }, { path = "t.ssds-spec.toml" }]
'''


class Identity(unittest.TestCase):
    def test_the_token_is_bounded_and_the_pair_readable(self) -> None:
        long = "u" * 250
        self.assertEqual(len(obligation_token(long, long)), 73)
        self.assertNotEqual(obligation_token("a", "b"), obligation_token("b", "a"))
        r = Runs()
        s = r.sc.derive().s
        self.assertEqual(s.evidence.required("code"), (OBL,))
        self.assertEqual(s.evidence.readable(OBL), ("code", "spec"))

    def test_a_rename_keeps_the_identity(self) -> None:
        r = Runs()
        renamed = UNITS.replace('id = "code"', 'id = "kernel"\n    renamed_from = ["code"]')
        x, cand, _ = submit(r.sc, {"s.py": SPEC.replace("EVIDENCES code", "EVIDENCES kernel")}, agent("renamer"),
                            "t-rename", manifest=renamed)
        integrate(r.sc, x, cand)  # an admitted structure change (an absorbed one is quarantined, §18)
        s = r.sc.derive().s
        self.assertEqual(s.evidence.required("kernel"), (OBL,), "the root of kernel's lineage is code")

    def test_only_the_subject_a_relation_reaches_requires_it(self) -> None:
        r = Runs()
        lib = Scenario(UNITS + '    [[unit]]\n    id = "lib"\n    kind = "D4"\n    scope = [{ path = "b.py" }]\n',
                       {**r.files, "b.py": "u = 1\n"}, policy=POLICY)
        s = lib.derive().s
        self.assertEqual((s.evidence.required("code"), s.evidence.required("lib")), ((OBL,), ()))

    def test_policy_decides_per_claim_kind(self) -> None:
        r = Runs()
        no_policy = Scenario(UNITS, r.files, policy="schema = 1\n")
        self.assertEqual(no_policy.derive().s.evidence.required("code"), ())
        with self.assertRaises(ValueError):
            Policy.parse(b'schema = 1\n[domains.D4]\nevidence = ["obl"]\n')
        self.assertEqual(Policy.parse(b'schema = 1\n[domains.D4]\nevidence = true\n').get("D4", "evidence"), True)


class TwoSpecifications(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Runs()
        self.r.files.update({"t.py": "# ssds:rel EVIDENCES code\ndef other():\n    return 2\n",
                             "t.ssds-spec.toml": DECLARATION})
        self.r.sc = Scenario(TWO_SPECS, self.r.files, policy=POLICY)
        self.r.trees = {"T0": self.r.sc.head}

    def test_two_obligations_that_never_conflict(self) -> None:
        s = self.r.sc.derive().s
        second = obligation_token("code", "spec2")
        self.assertEqual(set(s.evidence.required("code")), {OBL, second})
        real = self.r.run(self.r.tree("T0"), GOOD)
        view = self.r.sc.view(self.r.trees["T0"])
        self.r.sc.admit(judgment("EVIDENCE_ASSESSMENT", {"realization": real["id"], "obligation": OBL}, "PASS",
                                 actor=HUMAN_B, basis=[on_record(real["id"]), content("spec", view.rev("spec"))],
                                 fields={"mode": "ORDINARY", "reading": {"unit": "spec", "rev": view.rev("spec")}}))
        d = self.r.sc.derive()
        w_value = lambda key: 2  # noqa: E731 - every premise current: only the obligations' bookkeeping is read
        self.assertEqual(d.a.ev("code", OBL, w_value, d.base, d.j.nonind), 2)
        self.assertEqual(d.a.ev("code", second, w_value, d.base, d.j.nonind), 0, "one obligation's pass answers "
                                                                                  "only it")


class FailuresKeepCounting(unittest.TestCase):
    def failing(self):
        r = Runs()
        failing = r.fail(r.run(r.tree("T0"), BAD))
        return r, failing

    def test_retirement_keeps_the_disagreement(self) -> None:
        r, failing = self.failing()
        d = r.sc.derive()
        before = d.a.qual("code", lambda key: 2, d.base, d.j.nonind)
        r.sc.absorb({"s.py": SPEC.replace("# ssds:rel EVIDENCES code\n", "")})
        d = r.sc.derive()
        self.assertEqual(d.s.evidence.required("code"), (), "the relation removed: the obligation retires")
        self.assertEqual(d.a.qual("code", lambda key: 2, d.base, d.j.nonind), before,
                         "retirement is not a disposition (§6.2, §10.2)")
        self.assertLess(before, 2)

    def test_a_retarget_to_a_successor_keeps_the_failure(self) -> None:
        r, failing = self.failing()
        split = UNITS.replace('scope = [{ path = "a.py" }]', 'scope = [{ path = "a.py" }]\n    [[unit]]\n'
                              '    id = "core"\n    kind = "D4"\n    scope = [{ path = "core.py" }]')
        split = split.replace('id = "code"\n    kind = "D4"\n    scope = [{ path = "a.py" }]',
                              'id = "kernel"\n    kind = "D4"\n    scope = [{ path = "a.py" }]')
        x, cand, _ = submit(r.sc, {"core.py": "w = 1\n", "s.py": SPEC.replace("EVIDENCES code", "EVIDENCES kernel")},
                            agent("splitter"), "t-split", manifest=split)
        integrate(r.sc, x, cand)
        d = r.sc.derive()
        self.assertEqual(d.s.evidence.required("kernel"), (obligation_token("kernel", "spec"),))
        self.assertLess(d.a.qual("kernel", lambda key: 2, d.base, d.j.nonind), 2,
                        "the successor that received the claim's regions keeps its failure")


class Lint(unittest.TestCase):
    def test_a_requiring_domain_with_no_specification(self) -> None:
        r = Runs()
        r.sc.absorb({"s.py": SPEC.replace("# ssds:rel EVIDENCES code\n", "")})
        lint = r.sc.derive().s.evidence.lint
        self.assertEqual([f.code for f in lint["code"]], ["EVIDENCE"])
        self.assertEqual(Runs().sc.derive().s.evidence.lint, {})


if __name__ == "__main__":
    unittest.main()
