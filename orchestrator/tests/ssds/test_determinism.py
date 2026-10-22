"""Determinism, replay and incremental-equals-from-scratch (catalogue §5.9; Phase D exit evidence).

Property tests over generated ledgers: a seeded generator builds histories of
acceptances, reviews, challenges, adjudications, equivalences, absorptions,
integrations, loss boundaries and attestations over a small manifest, and every
property is checked at every position. The generator is test data; the values
compared are the real derivation owner's.
"""

from __future__ import annotations

import dataclasses
import random
import unittest

from ssds.derivation import CheckpointInvalid, Consequences, History, State, Support

from ._fixtures import chain_of, lifecycle_body, record
from ._scenario import HUMAN, HUMAN_B, OWNER, Scenario, agent, adjudication, challenge, content, judgment, validity

UNITS = '''
    [[unit]]
    id = "arch"
    kind = "D3"
    scope = [{ path = "arch.md" }]
    [[unit]]
    id = "impl"
    kind = "D4"
    scope = [{ path = "impl.md" }]
    [[unit]]
    id = "test"
    kind = "D4"
    scope = [{ path = "test.md" }]
'''
FILES = {"arch.md": "a\n", "impl.md": "i\n", "test.md": "t\n"}
ACTORS = (HUMAN, HUMAN_B, OWNER)
SEEDS = range(8)


def generate(seed: int, steps: int = 22) -> Scenario:
    rng = random.Random(seed)
    sc = Scenario(UNITS, dict(FILES))
    subjects = ["arch", "impl", "test"]
    made: list[dict] = []
    revisions: dict[str, list[str]] = {u: [sc.rev(u)] for u in subjects}
    for step in range(steps):
        op = rng.choice(["accept", "accept", "review", "challenge", "adjudicate", "absorb", "integrate",
                         "equivalence", "loss", "attest", "fail", "override", "override"])
        subject = rng.choice(subjects)
        actor = rng.choice(ACTORS)
        if op == "accept":
            extra = [validity(o, sc.rev(o)) for o in subjects if o != subject and rng.random() < 0.3]
            t = sc.triple(subject)
            made += sc.admit(judgment("ACCEPTANCE", t, "PASS", actor=actor, basis=[content(subject, t["rev"]), *extra]))
        elif op == "fail":
            made += sc.admit(judgment("ACCEPTANCE", sc.triple(subject), "FAIL", actor=actor))
        elif op == "review":
            made += sc.admit(judgment("REVIEW", sc.triple(subject), rng.choice(["PASS", "NO_PASS"]), actor=actor,
                                      basis=[content(subject, sc.rev(subject))]))
        elif op == "challenge" and made:
            accepted = [r for r in made if r["kind"] == "ACCEPTANCE" and r["outcome"] == "PASS"]
            target = rng.choice(accepted if accepted and rng.random() < 0.7 else made)
            made += sc.admit(challenge({"record": target["id"]}, blocking=rng.random() < 0.7, actor=actor))
        elif op == "adjudicate":
            open_ = [r for r in made if r["kind"] == "CHALLENGE"]
            if open_:
                made += sc.admit(adjudication(rng.choice(open_)["id"], rng.choice(["UPHELD", "DISMISSED"])))
        elif op == "override":
            blocking = [r for r in made if r["kind"] == "CHALLENGE" and r["fields"]["blocking"]]
            if blocking:
                made += sc.admit(judgment("RISK_OVERRIDE", {"record": rng.choice(blocking)["id"]}, None, actor=OWNER,
                                          fields={"continuation": {"subjects": list(subjects), "items": [], "kinds": []}}))
        elif op == "absorb":
            sc.absorb({f"{subject}.md": f"{subject} {step}\n"})
            revisions[subject].append(sc.rev(subject))
        elif op == "integrate":
            sc.integrate({f"{subject}.md": f"{subject} by agent {step}\n"}, agent(f"maker{step % 2}"), f"task-{step}")
            revisions[subject].append(sc.rev(subject))
        elif op == "equivalence" and len(revisions[subject]) > 1:
            a, b = revisions[subject][-2:]
            made += sc.admit(judgment("EQUIVALENCE", {"unit": subject, "from": a, "to": b, "class": "EDITORIAL"},
                                      rng.choice(["EQUIVALENT", "NOT_EQUIVALENT"]), actor=actor))
        elif op == "loss" and sc.position > 2 and rng.random() < 0.4:
            rec = record("LEDGER_LOSS", target=None, actor=OWNER, fields={
                "retained": {"position": sc.position - 1}, "abandoned": [{"digest": "sha256:" + f"{step:064x}"}],
                "report": "sha256:" + "b" * 64, "controls": {}})
            sc.entries.append(lifecycle_body(sc.position, rec))
            made.append(rec)
        elif op == "attest":
            losses = [r for r in made if r["kind"] == "LEDGER_LOSS"]
            if losses:
                listed = [r["id"] for r in rng.sample(made, k=min(2, len(made)))]
                made += sc.admit(judgment("CONTINUITY_ATTESTATION", {"loss": losses[-1]["id"]}, None, actor=OWNER,
                                          fields={"scope_form": rng.choice(["COMPLEMENT", "EXPLICIT"]),
                                                  "listed": listed, "evidence": []}))
    return sc


def snapshot(chain, trees, position: int, checkpoint: bytes | None = None) -> dict:
    return Consequences(Support(State(History(chain, trees, checkpoint), position))).snapshot()


class Determinism(unittest.TestCase):
    def test_generated_ledgers_are_nontrivial(self) -> None:
        kinds = set()
        for seed in SEEDS:
            sc = generate(seed)
            kinds |= {r["kind"] for e in sc.entries for r in e["records"]}
            kinds |= {e["lifecycle"]["kind"] for e in sc.entries if e["lifecycle"]}
        self.assertLessEqual({"ACCEPTANCE", "REVIEW", "CHALLENGE", "ADJUDICATION", "EQUIVALENCE", "LEDGER_LOSS",
                              "TASK_RESULT", "RISK_OVERRIDE", "CONTINUITY_ATTESTATION"}, kinds)
        values = set()
        for seed in SEEDS:
            sc = generate(seed)
            chain = chain_of("demo", sc.entries, sc.objects)
            for n in range(len(sc.entries)):
                values |= set(snapshot(chain, sc.trees.__getitem__, n)["valid"].values())
        self.assertEqual(values, {0, 1, 2}, "every value of F < P < T occurs")

    def test_derivation_is_a_function_of_the_ledger_and_content(self) -> None:
        for seed in SEEDS:
            sc = generate(seed)
            chain = chain_of("demo", sc.entries, sc.objects)
            with self.subTest(seed=seed):
                for n in range(len(sc.entries)):
                    self.assertEqual(snapshot(chain, sc.trees.__getitem__, n),
                                     snapshot(chain_of("demo", sc.entries, sc.objects), dict(sc.trees).__getitem__, n))

    def test_independent_of_record_order_within_an_entry(self) -> None:
        for seed in SEEDS:
            sc = generate(seed)
            shuffled = [dict(e, records=list(reversed(e["records"]))) for e in sc.entries]
            a, b = chain_of("demo", sc.entries, sc.objects), chain_of("demo", shuffled, sc.objects)
            with self.subTest(seed=seed):
                n = len(sc.entries) - 1
                self.assertEqual(snapshot(a, sc.trees.__getitem__, n), snapshot(b, sc.trees.__getitem__, n))


class Replay(unittest.TestCase):
    def test_a_historical_view_equals_derivation_of_the_prefix(self) -> None:
        """§5.8: derivation at ``m ≤ n`` is ``derive(L_m, …)``, labeled historical."""

        for seed in SEEDS:
            sc = generate(seed)
            full = chain_of("demo", sc.entries, sc.objects)
            with self.subTest(seed=seed):
                for m in range(len(sc.entries)):
                    prefix = chain_of("demo", sc.entries[: m + 1], sc.objects)
                    historical = snapshot(full, sc.trees.__getitem__, m)
                    replayed = snapshot(prefix, sc.trees.__getitem__, m)
                    self.assertEqual(replayed["assertion_withheld"], [])
                    if m < len(sc.entries) - 1:
                        self.assertEqual(historical["assertion_withheld"], [f"historical view at position {m}"])
                    historical.pop("assertion_withheld"), replayed.pop("assertion_withheld")
                    self.assertEqual(historical, replayed)


class Incremental(unittest.TestCase):
    def test_resuming_from_a_checkpoint_equals_from_scratch_at_every_later_position(self) -> None:
        for seed in SEEDS:
            sc = generate(seed)
            full = chain_of("demo", sc.entries, sc.objects)
            trees = sc.trees.__getitem__
            last = len(sc.entries) - 1
            with self.subTest(seed=seed):
                for m in range(0, last + 1, 3):
                    written = History(chain_of("demo", sc.entries[: m + 1], sc.objects), trees).checkpoint(m)
                    for n in range(m, last + 1):
                        self.assertEqual(snapshot(full, trees, n, written), snapshot(full, trees, n), (m, n))
                    self.assertEqual(snapshot(full, trees, 0, written), snapshot(full, trees, 0))

    def test_a_checkpoint_is_verified_before_use(self) -> None:
        sc = generate(3)
        chain = chain_of("demo", sc.entries, sc.objects)
        trees = sc.trees.__getitem__
        written = History(chain, trees).checkpoint(4)
        tampered = written.replace(b'"boundaries":[', b'"boundaries":[1,', 1) if b'"boundaries":[]' in written \
            else written.replace(b'"boundaries":[', b'"boundaries":[999,', 1)
        forked_entries = list(chain.entries)
        forked_entries[4] = dataclasses.replace(forked_entries[4], digest="sha256:" + "f" * 64)
        forked = dataclasses.replace(chain, entries=tuple(forked_entries))
        other_ledger = dataclasses.replace(chain, ledger_id="other")
        for name, target, data in (("altered body", chain, tampered), ("forked at its position", forked, written),
                                   ("another ledger", other_ledger, written), ("not a checkpoint", chain, b"{}"),
                                   ("beyond the readable prefix", dataclasses.replace(chain, halt=3), written)):
            with self.subTest(name):
                with self.assertRaises(CheckpointInvalid):
                    History(target, trees, data)

    def test_a_ruleset_change_invalidates_checkpoints_from_its_position(self) -> None:
        sc = generate(5)
        adoption = record("RULESET_ADOPTION", target=None, actor=OWNER,
                          fields={"system": "ssds-rules/1", "policy": "sha256:" + "0" * 64,
                                  "analyzers": ["ssds.analyzer.python/1"]})
        sc.entries.append(lifecycle_body(sc.position, adoption))
        chain = chain_of("demo", sc.entries, sc.objects)
        n = len(sc.entries) - 1
        key = History(chain, sc.trees.__getitem__).checkpoint_key(n)
        self.assertEqual(key["ruleset"]["analyzers"], ["ssds.analyzer.python/1"])
        self.assertNotEqual(key["ruleset"], History(chain, sc.trees.__getitem__).checkpoint_key(n - 1)["ruleset"])


if __name__ == "__main__":
    unittest.main()
