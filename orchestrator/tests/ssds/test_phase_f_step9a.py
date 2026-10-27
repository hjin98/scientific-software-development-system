"""Phase F step 9a: runner identity and designation (catalogue §17.5, §25.1-§25.3; plan §3.6, readings F76-F77).

A designated runner's key, an external custody runner's custody identity included, is a trust root: declared at
genesis (``runner_keys``) or changed through the human-gated ``KEY_LIFECYCLE`` path with role ``RUNNER``; one key
serves one role. A machinery binding, the runner key signing the request, authenticates only that runner's
observations, by ``machinery:<component>@<key id>`` of class ``MACHINERY``; under any other binding a machinery
actor is ``AUTH_ACTOR``, so a runner observation is never salvaged without its key. Policy designates runner classes
(``[runners.<class>]``), and lint finds a verifier naming a class policy does not designate (Phase E E20).
"""

from __future__ import annotations

import unittest

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from ssds.admission.authenticate import authenticate
from ssds.admission.lifecycle import key_identity
from ssds.admission.request import request_message
from ssds.derivation import Policy, RunnerClass, trust_roots
from ssds.ledger.read import with_id

from ._fixtures import record, sshsig
from .test_admission_requests import RequestFixture, _Item, finding
from .test_lint import findings, item_block


class RunnerKey:
    def __init__(self) -> None:
        self.private = Ed25519PrivateKey.generate()
        self.public_hex = self.private.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw).hex()
        self.key_id = key_identity("RUNNER", self.public_hex)

    def trust_root(self) -> dict:
        return {"role": "RUNNER", "id": self.key_id, "public_key": self.public_hex}

    def sign(self, request: dict) -> dict:
        return {**request, "binding": {"runner": {"key": self.key_id,
                                                  "signature": self.private.sign(request_message(request)).hex()}}}


class Fixture(RequestFixture):
    def setUp(self) -> None:
        super().setUp()
        self.runner = RunnerKey()

    def roots(self):
        return trust_roots(self.entries())

    def head(self) -> int:
        return len(self.entries()) - 1

    def target(self) -> dict:
        from .test_phase_f_step4b import derive_state

        _, _, rev = derive_state(self).subject_triple("guide")
        return {"spec": {"unit": "guide", "rev": rev}, "claim": []}

    def observation(self, kind="REALIZATION", component="dispatcher", key=None, **changes) -> dict:
        target = self.target()
        rec = record(kind, target=target, outcome="COMPLETE", actor=f"machinery:{component}@{key or self.runner.key_id}",
                     actor_class="MACHINERY", fields={"execution": {}})
        return with_id({**rec, **changes})

    def signed(self, records, runner=None):
        return (runner or self.runner).sign(self.request(records, base_position=self.head()))

    def authenticated(self, req):
        return authenticate(req, req["records"], self.roots(), self.head())


class Keys(Fixture):
    def test_a_runner_key_is_registered_rotated_retired_and_compromised(self) -> None:
        self.lifecycle("REGISTER", self.runner.trust_root())
        self.assertEqual(self.roots().runners, {self.runner.key_id: self.runner.public_hex}, "B6 closed for runners")
        new = RunnerKey()
        self.lifecycle("ROTATE", {**new.trust_root(), "retires": self.runner.key_id})
        roots = self.roots()
        self.assertEqual((set(roots.runners), roots.former_runners), ({new.key_id}, {self.runner.key_id}))
        self.lifecycle("COMPROMISED", new.trust_root())
        roots = self.roots()
        self.assertEqual(roots.runners, {})
        self.assertIn(new.key_id, roots.compromised)
        self.assertEqual(roots.issue, {self.issuer.key_id: self.issuer.trust_root()["public_key"]}, "issue keys apart")

    def test_one_key_serves_one_role(self) -> None:
        from ssds.admission.engine import EntryInvalid

        self.lifecycle("REGISTER", self.runner.trust_root())
        issue = self.issuer.trust_root()
        cases = [("REGISTER", {**issue, "role": "RUNNER"}, {}),  # an issue key as a runner key
                 ("REGISTER", {**self.runner.trust_root(), "role": "ISSUE"}, {}),  # and the converse
                 ("COMPROMISED", {**self.runner.trust_root(), "role": "ISSUE"}, {}),  # a compromise names its role's key
                 ("RETIRE", {**issue, "role": "RUNNER"}, {}),
                 ("REGISTER", {**self.runner.trust_root(), "role": "ADMISSION"}, {})]
        for action, key, extra in cases:
            with self.subTest(action=action, role=key["role"]), self.assertRaises(EntryInvalid):
                self.lifecycle(action, key, **extra)

    def test_genesis_runner_keys_are_read_and_the_reader_is_total(self) -> None:
        key = self.runner.trust_root()
        genesis = _Item(0, {"kind": "GENESIS", "fields": {"trust_roots": {"runner_keys": [key, 7, {"id": 1}]}}})
        junk = _Item(1, {"kind": "KEY_LIFECYCLE", "fields": {"action": "RETIRE", "key": {"role": "RUNNER"}}})
        self.assertEqual(trust_roots([genesis, junk]).runners, {key["id"]: key["public_key"]})


class Binding(Fixture):
    def setUp(self) -> None:
        super().setUp()
        self.lifecycle("REGISTER", self.runner.trust_root())

    def test_a_runner_authenticates_its_own_observations(self) -> None:
        for kind in ("REALIZATION", "CHECK_EXECUTION", "CUSTODY_ENUMERATION"):
            with self.subTest(kind=kind):
                auth = self.authenticated(self.signed([self.observation(kind)]))
                self.assertEqual((auth.ok, auth.refused), (True, ()))

    def test_only_its_own_observations(self) -> None:
        other = RunnerKey()
        cases = {"another kind": self.observation("FINDING"),
                 "another key's actor": self.observation(key=other.key_id),
                 "no component": self.observation(component=""),
                 "a malformed component": self.observation(component="Bad Name"),
                 "an agent's class": self.observation(actor_class="AGENT"),
                 "a bound record": self.observation(binding={"task": "t"}),
                 "a human": with_id({**finding(), "actor": self.human()})}
        auth = self.authenticated(self.signed(list(cases.values())))
        self.assertTrue(auth.ok)
        refused = dict(auth.refused)
        for name, rec in cases.items():
            with self.subTest(case=name):
                self.assertEqual(refused.get(rec["id"]), ("AUTH_ACTOR",))

    def test_no_key_in_force_authenticates_nothing(self) -> None:
        req = self.signed([self.observation()])
        unknown = RunnerKey()
        cases = {"an unknown key": self.signed([self.observation(key=unknown.key_id)], unknown),
                 "a bad signature": {**req, "binding": {"runner": {**req["binding"]["runner"],
                                                                   "signature": "00" * 64}}},
                 "a malformed binding": {**req, "binding": {"runner": {"key": self.runner.key_id}}}}
        for name, bad in cases.items():
            with self.subTest(case=name):
                self.assertFalse(self.authenticated(bad).ok)
        self.lifecycle("RETIRE", self.runner.trust_root())
        self.assertFalse(self.authenticated(self.signed([self.observation()])).ok, "retired")

    def test_a_compromised_runner_key_authenticates_nothing(self) -> None:
        self.lifecycle("COMPROMISED", self.runner.trust_root())
        self.assertFalse(self.authenticated(self.signed([self.observation()])).ok)

    def test_a_machinery_actor_under_another_binding_is_never_salvaged(self) -> None:
        obs = self.observation()
        req = self.request([obs], base_position=self.head())
        req["binding"] = {"human": {"actor": self.human(), "signature": sshsig(self.private, request_message(req))}}
        decision = self.admit(req)
        self.assertEqual((decision.admitted, dict(decision.refused).get(obs["id"])), ((), ("AUTH_ACTOR",)))

    def test_an_agent_reported_realization_is_refused(self) -> None:
        issued = self.issue("MANUAL")
        reported = self.bind(record("REALIZATION", target=self.target(), outcome="COMPLETE",
                                    fields={"execution": {}}), issued)
        decision = self.admit(super(Fixture, self).signed(issued, [reported]))
        self.assertEqual(decision.admitted, ())
        self.assertIn(reported["id"], dict(decision.refused))

    def test_through_admission_runner_observations_wait_for_step_9d(self) -> None:
        obs = self.observation()
        decision = self.admit(self.signed([obs]))
        self.assertEqual(decision.admitted, ())
        codes = set(decision.reasons) | set(dict(decision.refused).get(obs["id"], ()))
        self.assertEqual(codes, {"SCHEMA_UNSUPPORTED"}, "authenticated; 6c's gate holds evidence kinds until 9d")


class Designation(unittest.TestCase):
    RUNNERS = '[runners.ci]\nkind = "DISPATCHER"\nkeys = ["ed25519:a"]\nattributes = ["python"]\n' \
              'observes_outside_reads = true\n'

    def test_policy_designates_runner_classes(self) -> None:
        policy = Policy.parse(("schema = 1\n" + self.RUNNERS).encode())
        self.assertEqual(policy.runners, {"ci": RunnerClass("DISPATCHER", ("ed25519:a",), ("python",), True)})
        self.assertEqual(Policy.parse(b"schema = 1\n").runners, {})

    def test_a_malformed_designation_is_refused(self) -> None:
        base = {"kind": '"DISPATCHER"', "keys": '["ed25519:a"]', "attributes": "[]", "observes_outside_reads": "false"}
        for change in ({"kind": '"CLOUD"'}, {"keys": "[]"}, {"keys": '["a", "a"]'}, {"keys": '"a"'},
                       {"attributes": '["x", "x"]'}, {"observes_outside_reads": '"yes"'}, {"extra": "1"},
                       {"kind": None}):
            fields = {**base, **change}
            text = "schema = 1\n[runners.ci]\n" + "".join(f"{k} = {v}\n" for k, v in fields.items() if v is not None)
            with self.subTest(change=change), self.assertRaises(ValueError):
                Policy.parse(text.encode())

    def test_lint_finds_a_class_policy_does_not_designate(self) -> None:
        self.assertEqual(findings(item_block()), set())
        self.assertIn(("VERIFIER", "obligation o1 names runner class ci, not designated in policy"),
                      findings(item_block(), designated=False))


if __name__ == "__main__":
    unittest.main()
