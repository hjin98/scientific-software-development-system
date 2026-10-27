"""Phase F step 9d-iii: acceptance group 2's admission half, and custody enumerations (catalogue §6.5-§6.9, §8.3,
§17.5; plan §3.6, reading F102).

``AdmittedRuns`` mirrors ``test_assessment.Runs`` through Admission: its own genesis (``code`` and an ``EMBEDDED``
specification, policy requiring evidence and designating class ``ci`` for a runner key registered through the
human gate), trees absorbed through the product repository before the runs on them, runs signed by the runner key,
and assessments and completeness judgments by the genesis human. Expected values are transcribed from
``qualification/ssds80/models/cases_s5_6.py`` (named per test), as ``test_assessment`` transcribes them.
"""

from __future__ import annotations

import hashlib
import unittest
from unittest import mock

from ssds.admission.engine import Admission
from ssds.admission.genesis import admit_genesis, prepare_genesis
from ssds.admission.request import request_message
from ssds.content import recorded_identity
from ssds.core.api.v1 import canonical_json
from ssds.derivation import F, derive
from ssds.derivation.evidence import obligation_token
from ssds.ledger.read import read_chain, with_id

from ._fixtures import commit, record, sshsig
from .test_admission_genesis import GenesisFixture
from .test_phase_f_step9a import RunnerKey

MANIFEST = '''schema = 1
[[unit]]
id = "code"
kind = "D4"
scope = [{ path = "a.py" }]
[[unit]]
id = "spec"
kind = "EVIDENCE_SPEC"
scope = [{ path = "s.py" }, { path = "s.ssds-spec.toml" }]
[[unit]]
id = "ssds.manifest"
kind = "MANIFEST"
scope = [{ file = ".ssds/manifest.toml" }]
[[unit]]
id = "ssds.policy"
kind = "POLICY"
scope = [{ file = ".ssds/policy.toml" }]
[[unit]]
id = "ssds.unclassified"
kind = "UNCLASSIFIED"
scope = [{ prefix = "" }]
'''
SPEC = "# ssds:rel EVIDENCES code\ndef check():\n    return 1\n"
DECLARATION = """oracle = "EMBEDDED"
runner = "ci"
time_bound_hours = 24
outputs = [{ name = "x", type = "int" }, { name = "x_verdict", type = "enum", values = ["PASS", "FAIL"] }]
verdicts = [{ output = "x", embedded = "x_verdict" }]
"""
BAD = {"x": 1, "x_verdict": "FAIL"}
GOOD = {"x": 2, "x_verdict": "PASS"}
OBL = obligation_token("code", "spec")
CODE_TERM = {"path": "a.py"}
SPEC_TERM = {"file": "s.py", "symbol": "check"}


class AdmittedRuns(GenesisFixture):
    MODES = {"*": {"mode": "UNGOVERNED"}}
    WORKFLOW = ""
    DECLARATION = DECLARATION

    def setUp(self) -> None:
        super().setUp()
        self.runner, self.custodian = RunnerKey(), RunnerKey()
        self.write({"a.py": "v = 1\n", "s.py": SPEC, "s.ssds-spec.toml": self.DECLARATION, "other.txt": "1\n",
                    ".ssds/manifest.toml": MANIFEST, ".ssds/policy.toml": self.policy()})
        for gone in ("guide.md", "src/tool.py"):
            (self.product / gone).unlink()
        self.baseline = commit(self.product, "the evidence fixture")
        with mock.patch("ssds.admission.genesis.SHADOW_MODES", ("LEGACY", "UNGOVERNED", "NATIVE")):
            prepared = prepare_genesis(self.spec(modes=self.MODES), self.home, self.trees)
            self.assertTrue(prepared.valid, prepared.problems)
            admit_genesis(self.home, "demo", sshsig(self.private, prepared.message))
        self.admission = Admission(self.home, "demo", self.trees, product=self.product)
        self.lifecycle("REGISTER", self.runner.trust_root())
        self.lifecycle("REGISTER", self.custodian.trust_root())
        self.heads = {"T0": self.baseline}
        self.completeness: dict[str, str] = {}
        self.attempts = 0

    def policy(self) -> str:
        return (f'schema = 1\n[domains.D4]\nevidence = true\n[runners.ci]\nkind = "DISPATCHER"\n'
                f'keys = ["{self.runner.key_id}"]\nattributes = []\nobserves_outside_reads = true\n'
                f'[runners.vault]\nkind = "EXTERNAL_CUSTODY"\nkeys = ["{self.custodian.key_id}"]\nattributes = []\n'
                f'observes_outside_reads = true\n'
                f'[runners.local]\nkind = "DISPATCHER"\nkeys = ["{self.custodian.key_id}"]\nattributes = []\n'
                f'observes_outside_reads = true\n'
                f'[runners.elsewhere]\nkind = "EXTERNAL_CUSTODY"\nkeys = ["{self.runner.key_id}"]\nattributes = []\n'
                f'observes_outside_reads = true\n' + self.WORKFLOW)

    def write(self, files: dict[str, str]) -> None:
        for path, text in files.items():
            (self.product / path).parent.mkdir(parents=True, exist_ok=True)
            (self.product / path).write_text(text)

    # -- the ledger -----------------------------------------------------------------------------

    def chain(self):
        return read_chain(self.home.ledger_repository("demo"), "demo")

    def entries(self):
        chain = self.chain()
        return chain.entries[: chain.readable_through + 1]

    def derive(self):
        return derive(self.chain(), self.trees)

    def human(self) -> str:
        from ssds.ledger.read import human_key_id

        return human_key_id(self.public)

    def lifecycle(self, action: str, key: dict) -> None:
        rec = record("KEY_LIFECYCLE", target=None, actor=self.human(), fields={"action": action, "key": key})
        self.admission.admit_lifecycle(rec, sshsig(self.private, self.admission.lifecycle_message(rec)), self.head())

    def head(self) -> str:
        return Admission.expected_head(self.entries())

    def request(self, records, objects=None) -> dict:
        return {"binding": None, "claims": [], "base_position": len(self.entries()) - 1, "base_commit": self.head(),
                "candidates": [], "adopted_deltas": [], "records": list(records), "objects": dict(objects or {})}

    def admit_human(self, *records):
        req = self.request(records)
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        decision = self.admission.admit(req, self.head())
        self.assertEqual((decision.reasons, decision.refused), ((), ()), "admitted as built")
        return decision

    def admit_runner(self, *records, objects=None):
        decision = self.admission.admit(self.runner.sign(self.request(records, objects)), self.head())
        self.assertEqual((decision.reasons, decision.refused), ((), ()), "admitted as built")
        return decision

    # -- trees, runs and assessments ---------------------------------------------------------------

    def tree(self, name: str, **changes: str) -> str:
        """The head ``name``: the product moved to the baseline files with ``changes`` and absorbed (6a)."""

        if name not in self.heads:
            base = self.trees(self.baseline)
            files = {p: e.data.decode() for p, e in base.items()}
            for path in list(files):
                (self.product / path).write_text(files[path])
            self.write(changes)
            self.heads[name] = commit(self.product, name)
            self.admission.absorb(self.entries(), self.heads[name])
        return self.heads[name]

    def at(self, name: str) -> int:
        s = self.derive().s
        return max(p for p in range(s.n + 1) if s.h.head(p) == self.heads[name])

    def bound_judgment(self, head: str) -> str:
        if head not in self.completeness:
            s = self.derive().s
            view = s.h.view(max(p for p in range(s.n + 1) if s.h.head(p) == head))
            c = record("COMPLETENESS", target={"scope": ["code", "spec"], "classes": ["EXEC"],
                                               "membership": view.membership_digest(("code", "spec"))},
                       outcome="COMPLETE", actor=self.human(),
                       basis=[{"mode": "content", "target": {"unit": u, "rev": view.rev(u)}, "class": "EXACT"}
                              for u in ("code", "spec")])
            attestation = record("NON_AUTHORSHIP_ATTESTATION", target={"record": c["id"]}, outcome="NOT_AUTHOR",
                                 actor=self.human())
            self.admit_human(c, attestation)
            self.completeness[head] = c["id"]
        return self.completeness[head]

    def realize(self, head: str, outcome: dict, *, pins=("p1",), attributes=(), unpinnable=False, bounded=True) -> dict:
        s = self.derive().s
        k = max(p for p in range(s.n + 1) if s.h.head(p) == head)
        view, t = s.h.view(k), self.trees(head)
        basis = {"tree": head, "context": {"system": "ssds-rules/1", "ignore": [], "analyzers": sorted(s.analyzer_set)},
                 "pins": [["dataset:input", p] for p in pins], "unpinnable": unpinnable,
                 "attributes": [list(a) for a in attributes]}
        if bounded:
            basis["units"] = [{"unit": "code", "rev": view.rev("code"),
                               "terms": [[CODE_TERM, recorded_identity(t, CODE_TERM, ())]]},
                              {"unit": "spec", "rev": view.rev("spec"),
                               "terms": [[SPEC_TERM, recorded_identity(t, SPEC_TERM, ())]]}]
            basis["bounded_by"] = [self.bound_judgment(head)]
            s = self.derive().s
        else:
            basis["units"] = []
            basis["widened"] = [[{"tracked": "*"}, recorded_identity(t, {"tracked": "*"}, ())]]
            basis["bounded_by"] = "UNBOUNDED"
        text = canonical_json(outcome).decode()
        digest = "sha256:" + hashlib.sha256(text.encode()).hexdigest()
        execution = {**basis, "start": s.n, "end": s.n, "runner": {"class": "ci", "key": self.runner.key_id},
                     "class_attributes": [], "observes_outside_reads": True}
        self.attempts += 1
        real = with_id({**record("REALIZATION", target={"spec": {"unit": "spec", "rev": view.rev("spec")},
                                                        "claim": [{"unit": "code", "rev": view.rev("code")}]},
                                 outcome="COMPLETE", actor=f"machinery:dispatcher@{self.runner.key_id}",
                                 actor_class="MACHINERY",
                                 fields={"execution": execution, "configuration": {"regime": "default"},
                                         "evaluated": digest}),
                        "provenance": {"attempt": self.attempts}})
        self.admit_runner(real, objects={digest: text})
        return real

    def fail(self, realization: dict) -> dict:
        spec = realization["target"]["spec"]
        a = record("EVIDENCE_ASSESSMENT", target={"realization": realization["id"], "obligation": OBL},
                   outcome="FAIL", actor=self.human(),
                   basis=[{"mode": "record", "target": {"record": realization["id"]}, "class": "EXACT"}],
                   fields={"mode": "ORDINARY", "reading": spec, "failing_outputs": ["x"]})
        self.admit_human(a)
        return a

    def stale(self, failing: dict, state: str) -> bool:
        """The failure's staleness with ``state``'s files at the head (absorbed when they are not)."""

        if self.trees(self.head()).items() != self.trees(self.heads[state]).items():
            self.tree(f"{state}@{len(self.heads)}", **{p: e.data.decode() for p, e in self.trees(self.heads[state]).items()})
        d = self.derive()
        return d.a.stale(failing["id"], d.base, lambda node: d.values.get(node, F))


class Staleness(AdmittedRuns):
    """cases_s5_6.py, through Admission."""

    def test_genuine_fix_is_stale(self) -> None:
        t0 = self.tree("T0")
        failing = self.fail(self.realize(t0, BAD))
        self.realize(t0, BAD)
        t1 = self.tree("T1", **{"a.py": "v = 2\n"})
        self.realize(t1, GOOD)
        self.assertTrue(self.stale(failing, "T1"))

    def test_revert_yields_again(self) -> None:
        t0 = self.tree("T0")
        failing = self.fail(self.realize(t0, BAD))
        self.realize(t0, BAD)
        t1 = self.tree("T1", **{"a.py": "v = 2\n"})
        self.realize(t1, GOOD)
        self.assertTrue(self.stale(failing, "T1"), "the fix")
        self.assertFalse(self.stale(failing, "T0"))

    def test_differing_pin_goes_to_owner(self) -> None:
        t0 = self.tree("T0")
        failing = self.fail(self.realize(t0, BAD))
        self.realize(t0, BAD)
        self.realize(t0, GOOD, pins=("p2",))
        t1 = self.tree("T1", **{"a.py": "v = 2\n"})
        self.realize(t1, GOOD)
        self.assertFalse(self.stale(failing, "T1"), "nondeterministic in fact: the owner's")

    def test_differing_free_attribute_goes_to_owner(self) -> None:
        cpu, gpu = (("backend", "cpu"),), (("backend", "gpu"),)
        t0 = self.tree("T0")
        failing = self.fail(self.realize(t0, BAD, attributes=cpu))
        self.realize(t0, BAD, attributes=cpu)
        self.realize(t0, GOOD, attributes=gpu)
        t1 = self.tree("T1", **{"a.py": "v = 2\n"})
        self.realize(t1, GOOD, attributes=cpu)
        self.assertFalse(self.stale(failing, "T1"))

    def test_unpinnable_supports_no_stop(self) -> None:
        t0 = self.tree("T0")
        failing = self.fail(self.realize(t0, BAD, unpinnable=True))
        self.realize(t0, BAD, unpinnable=True)
        t1 = self.tree("T1", **{"a.py": "v = 2\n"})
        self.realize(t1, GOOD, unpinnable=True)
        self.assertFalse(self.stale(failing, "T1"))

    def test_unbounded_run_still_linked(self) -> None:
        w0 = self.tree("T0")
        failing = self.fail(self.realize(w0, BAD, bounded=False))
        self.realize(w0, BAD)
        w0b = self.tree("W0b", **{"other.txt": "2\n"})
        self.realize(w0b, GOOD, bounded=False)
        w1 = self.tree("W1", **{"a.py": "v = 2\n"})
        self.realize(w1, GOOD)
        self.assertFalse(self.stale(failing, "W1"), "the unbounded differing run is linked through the narrow reproduction")

    def test_context_change_keeps_implication(self) -> None:
        """A partial port (review of 03321379, note 1): on⁺ ⇒ on⁻ for every admitted run and head, under unchanged
        contexts. The case's context change (a structure override re-resolving terms) cannot be made through
        Admission in place; it stays in ``test_assessment.Staleness``, and the S5 coverage map counts this half
        only."""

        t0 = self.tree("T0")
        first = self.realize(t0, BAD)
        t1 = self.tree("T1", **{"a.py": "v = 2\n"})
        runs = [first, self.realize(t1, GOOD)]
        failing = self.fail(runs[0])
        d = self.derive()
        for o in runs:
            for head in (t0, t1):
                k = self.trees(head)
                if d.a.on_plus(o["id"], k, failing["target"]["realization"], d.base):
                    self.assertTrue(d.a.on_minus(o["id"], k), "on⁺ ⇒ on⁻")


class Group2Discriminators(AdmittedRuns):
    """G2 workplan §5.3 group 2, the admission half."""

    def test_a_failure_whose_only_reproductions_are_unbounded_stays_counting(self) -> None:
        # 5c55d4b N6
        t0 = self.tree("T0")
        failing = self.fail(self.realize(t0, BAD, bounded=False))
        self.realize(t0, BAD, bounded=False)
        t1 = self.tree("T1", **{"a.py": "v = 2\n"})
        self.realize(t1, GOOD)
        self.assertFalse(self.stale(failing, "T1"))

    def test_each_link_traversed_is_recorded(self) -> None:
        # 798b2b4 B4
        w0 = self.tree("T0")
        failing = self.fail(self.realize(w0, BAD, bounded=False))
        reproduction = self.realize(w0, BAD)
        w0b = self.tree("W0b", **{"other.txt": "2\n"})
        differing = self.realize(w0b, GOOD, bounded=False)
        w1 = self.tree("W1", **{"a.py": "v = 2\n"})
        self.realize(w1, GOOD)
        self.stale(failing, "W1")
        d = self.derive()
        explanation = d.a.explain(failing["id"], d.base)
        self.assertIn(differing["id"], explanation["differed"])
        self.assertIn(("failing-content", differing["id"], reproduction["id"]), explanation["links"])

    def test_an_upheld_challenge_of_the_realization_disposes(self) -> None:
        # 29da56e N5, its first case through Admission (the counter-challenge and the dismissal need further human
        # keys; they stay in test_assessment.Group2Discriminators)
        realization = self.realize(self.tree("T0"), BAD)
        failing = self.fail(realization)
        d = self.derive()
        self.assertEqual(d.a.adverse("code", OBL, d.base), [failing["id"]])
        c = record("CHALLENGE", target={"record": realization["id"]}, actor=self.human(),
                   fields={"blocking": True, "serious": False, "inquiry": "CONFIRMATORY"})
        self.admit_human(c)
        upheld = record("ADJUDICATION", target={"record": c["id"]}, outcome="UPHELD", actor=self.human())
        attestation = record("NON_AUTHORSHIP_ATTESTATION", target={"record": upheld["id"]}, outcome="NOT_AUTHOR",
                             actor=self.human())
        self.admit_human(upheld, attestation)
        d = self.derive()
        self.assertEqual(d.a.disposition(failing["id"], d.values.get, d.base, d.j.nonind), 2,
                         "an upheld challenge of the failing run's realization disposes of the failure")


class Custody(AdmittedRuns):
    """Reading F102: an external custody runner's enumeration, signed by its class's key."""

    def enumeration(self, runner="vault", runs=None) -> dict:
        runs = runs if runs is not None else ["sha256:" + "8" * 64, "sha256:" + "9" * 64]
        return record("CUSTODY_ENUMERATION", target={"runner": runner}, actor=f"machinery:custody@{self.custodian.key_id}",
                      actor_class="MACHINERY", fields={"runs": runs})

    def codes(self, rec) -> tuple:
        decision = self.admission.admit(self.custodian.sign(self.request([rec])), self.head())
        return tuple(sorted(set(dict(decision.refused).get(rec["id"], ())) | set(decision.reasons)))

    def test_its_enumeration_is_accepted_its_runs_unadmitted(self) -> None:
        """F81: listed runs need not be admitted; derivation blocks the stop until each is."""

        self.assertEqual(self.codes(self.enumeration()), ())

    def test_only_its_own_external_custody_class(self) -> None:
        self.assertEqual(self.codes(self.enumeration("ci")), ("AUTH_ACTOR",), "a Dispatcher-run class")
        self.assertEqual(self.codes(self.enumeration("nobody")), ("AUTH_ACTOR",), "no designated class")
        self.assertEqual(self.codes(self.enumeration("local")), ("AUTH_ACTOR",), "its key, but no custody class")
        self.assertEqual(self.codes(self.enumeration("elsewhere")), ("AUTH_ACTOR",), "a custody class, not its key")

    def test_each_run_once(self) -> None:
        self.assertEqual(self.codes(self.enumeration(runs=["sha256:" + "8" * 64] * 2)), ("SCHEMA_RECORD",))


class EvidenceClaims(AdmittedRuns):
    """A human's claim of ``ACCEPT(code)`` with its acceptance in the request (§7.4, §8.3 step 7, §10.4)."""

    MODES = {"code": {"mode": "NATIVE", "ruleset": "ssds-rules/1"}, "*": {"mode": "UNGOVERNED"}}

    def accept(self):
        from ssds.derivation import Workflow

        d = self.derive()
        (o,) = [o for o in Workflow(d).obligations if o.kind == "ACCEPT" and o.target.get("subject") == "code"]
        triple = d.s.subject_triple("code")
        t = {"subject": triple[0], "scope_id": triple[1], "rev": triple[2]}
        acceptance = record("ACCEPTANCE", target=t, outcome="PASS", actor=self.human(),
                            basis=[{"mode": "content", "target": {"unit": "code", "rev": t["rev"]}, "class": "EXACT"}])
        attestation = record("NON_AUTHORSHIP_ATTESTATION", target={"record": acceptance["id"]}, outcome="NOT_AUTHOR",
                             actor=self.human())
        req = self.request([acceptance, attestation])
        req["claims"] = [o.id]
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        return self.admission.admit(req, self.head())

    def passing(self, realization: dict) -> None:
        a = record("EVIDENCE_ASSESSMENT", target={"realization": realization["id"], "obligation": OBL},
                   outcome="PASS", actor=self.human(),
                   basis=[{"mode": "record", "target": {"record": realization["id"]}, "class": "EXACT"}],
                   fields={"mode": "ORDINARY", "reading": realization["target"]["spec"]})
        attestation = record("NON_AUTHORSHIP_ATTESTATION", target={"record": a["id"]}, outcome="NOT_AUTHOR",
                             actor=self.human())
        self.admit_human(a, attestation)

    def disputed(self):
        t0 = self.tree("T0")
        self.passing(self.realize(t0, GOOD))
        self.fail(self.realize(t0, BAD))
        return self.accept()


class EvidenceTerm(EvidenceClaims):
    """5d's evidence-term predicate at Admission: met only once required evidence holds."""

    def test_unmet_with_no_passing_assessment(self) -> None:
        self.assertIn("OBLIGATION_PREDICATE_UNMET", self.accept().reasons)

    def test_met_with_one(self) -> None:
        self.passing(self.realize(self.tree("T0"), GOOD))
        decision = self.accept()
        self.assertEqual((decision.reasons, decision.refused), ((), ()))
        self.assertEqual(len(decision.admitted), 2)


class CountingFailure(EvidenceClaims):
    """124b0b7 N2: a counting failure beside passing evidence leaves the claim unmet."""

    def test_a_counting_failure(self) -> None:
        self.assertIn("OBLIGATION_PREDICATE_UNMET", self.disputed().reasons)


class ProvisionalDischarge(EvidenceClaims):
    """124b0b7 N2: unless policy lets ``ACCEPT`` discharge provisionally (``DISCHARGED_PROVISIONAL``)."""

    WORKFLOW = '[workflow]\nprovisional_kinds = ["ACCEPT"]\n'

    def test_a_counting_failure_discharges_provisionally(self) -> None:
        decision = self.disputed()
        self.assertEqual((decision.reasons, decision.refused), ((), ()))


if __name__ == "__main__":
    unittest.main()
