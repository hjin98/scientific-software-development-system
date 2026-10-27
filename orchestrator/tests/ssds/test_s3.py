"""S3 kernel (catalogue §5.6 step (v), §5.7-§5.9, §23.6): integrity, intake and requalification, views.

Expectations are written from the catalogue text cited per test; register rows
§5.7-§5.9 are accepted on inspection with their tests assigned to Phase D.
"""

from __future__ import annotations

import dataclasses
import unittest

from ssds.derivation import F, T, Consequences, consequences, derive

from ._scenario import attested
from ._fixtures import chain_of, lifecycle_body, record
from ._scenario import HUMAN_B, OWNER, Scenario, judgment, validity
from .test_assessment import BAD, OBL, Runs
from .test_support import TWO, accept


def view(sc: Scenario, position: int | None = None, chain=None) -> Consequences:
    return consequences(chain or chain_of("demo", sc.entries, sc.objects), sc.trees.__getitem__, position)


def loss(sc: Scenario, retained: int) -> dict:
    rec = record("LEDGER_LOSS", target=None, actor=OWNER, fields={
        "retained": {"position": retained}, "abandoned": [{"digest": "sha256:" + "a" * 64}],
        "report": "sha256:" + "b" * 64, "controls": {}})
    sc.entries.append(lifecycle_body(sc.position, rec))
    return rec


class IntegrityHalt(unittest.TestCase):
    """§5.7: an authenticated entry violating the closed schema halts every position from it."""

    def setUp(self) -> None:
        self.sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        self.sc.admit(*attested(accept(self.sc, "arch")))
        self.sc.admit(*attested(accept(self.sc, "impl", actor=HUMAN_B)))
        clean = chain_of("demo", self.sc.entries, self.sc.objects)
        self.clean = clean
        self.halted = dataclasses.replace(clean, halt=2, halt_reasons=("record: unknown kind",))

    def test_positions_before_the_halt_are_unaffected_and_historical(self) -> None:
        halted = view(self.sc, chain=self.halted)
        self.assertEqual(halted.s.n, 1, "derivation reads only the prefix before k")
        unaffected = view(self.sc, 1, chain=dataclasses.replace(self.clean, entries=self.clean.entries[:2]))
        for key in ("current", "valid", "forced"):
            self.assertEqual(halted.snapshot()[key], unaffected.snapshot()[key])
        self.assertEqual(halted.support.valid("arch"), T)

    def test_no_current_assertion_at_or_after_k_and_a_critical_obligation_in_every_view(self) -> None:
        for position in (0, 1):
            with self.subTest(position=position):
                c = view(self.sc, position, chain=self.halted)
                self.assertFalse(c.current_assertion)
                self.assertTrue(any(r.startswith("INTEGRITY_HALT from position 2") for r in c.assertion_withheld))
                halts = [f for f in c.findings if f.code == "INTEGRITY_HALT"]
                self.assertEqual(len(halts), 1)
                self.assertTrue(halts[0].integrity and halts[0].attention == "CRITICAL")
                self.assertIn("INTEGRITY", {o.kind for o in c.obligations})

    def test_an_unreadable_schema_version_is_not_corruption(self) -> None:
        c = view(self.sc, chain=dataclasses.replace(self.clean, unreadable=2))
        self.assertFalse(c.current_assertion)
        self.assertFalse([f for f in c.findings if f.integrity])

    def test_a_clean_chain_at_its_head_asserts(self) -> None:
        c = view(self.sc)
        self.assertTrue(c.current_assertion, c.assertion_withheld)
        self.assertFalse(c.findings)
        self.assertFalse(view(self.sc, 1).current_assertion, "an earlier position is a historical view")


class ForcedComponents(unittest.TestCase):
    """§5.6 (v): one S3 finding per forced component, ordinary or integrity by the edges it passes."""

    def test_a_cycle_through_basis_entries_only_is_an_integrity_obligation(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        sc.admit(accept(sc, "arch", extra=[validity("impl", sc.rev("impl"))]),
                 accept(sc, "impl", actor=HUMAN_B, extra=[validity("arch", sc.rev("arch"))]))
        c = view(sc)
        cycles = [f for f in c.findings if f.code == "SUPPORT_CYCLE"]
        self.assertEqual(len(cycles), 1, "one finding per forced component")
        self.assertEqual(cycles[0].attention, "CRITICAL")
        self.assertIn("INTEGRITY", {o.kind for o in c.obligations})

    def test_a_cycle_through_an_about_term_is_an_ordinary_finding(self) -> None:
        r = Runs()
        realization = r.run(r.tree("T0"), BAD)
        failing = r.fail(realization)
        view0 = r.sc.view(r.trees["T0"])
        looped = judgment("EVIDENCE_ASSESSMENT", {"realization": realization["id"], "obligation": OBL}, "FAIL",
                          actor=OWNER, basis=list(failing["basis"]) + [validity("code", view0.rev("code"))],
                          fields=dict(failing["fields"]))
        r.sc.admit(looped)
        c = view(r.sc)
        self.assertEqual(c.support.current(looped["id"]), F)
        cycles = [f for f in c.findings if f.code == "SUPPORT_CYCLE"]
        self.assertEqual([f.attention for f in cycles], ["ORDINARY"])
        self.assertNotIn("INTEGRITY", {o.kind for o in c.obligations})


class IntakeAndExplanation(unittest.TestCase):
    """§5.8: one intake obligation per quarantined delta; quarantine and ill-formedness explained, not enforced."""

    def test_each_quarantined_delta_has_an_intake_obligation(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        sc.manifest = TWO + '''
    [[unit]]
    id = "extra"
    kind = "D3"
    scope = [{ path = "extra.md" }]
'''
        sc.absorb({"extra.md": "x\n"})
        c = view(sc)
        quarantined = sorted(c.s.s0.quarantine)
        self.assertTrue(quarantined, "the unadopted declaration is quarantined")
        self.assertEqual(sorted(o.about for o in c.obligations if o.kind == "INTAKE"), quarantined)
        self.assertEqual({f.code for f in c.findings}, {"QUARANTINED"})
        self.assertFalse([f for f in c.findings if f.integrity], "quarantine is ordinary")


class Requalification(unittest.TestCase):
    """§23.6: one REQUALIFY per permissive record or relaxer in effect at R and withheld now."""

    def test_withheld_records_are_enumerated_and_a_fresh_record_ends_each(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        acc = accept(sc, "arch")
        adverse = judgment("ACCEPTANCE", sc.triple("impl"), "FAIL", actor=HUMAN_B)
        sc.admit(*attested(acc, adverse))  # each human judge presents its non-authorship attestation (§5.10 (f))
        retained = sc.position - 1
        loss(sc, retained)
        c = view(sc)
        self.assertEqual(c.support.valid("arch"), F)
        self.assertEqual([o.about for o in c.obligations if o.kind == "REQUALIFY"], [(acc["id"],)],
                         "the acceptance was current at R; the adverse judgment is unchanged by a boundary, and an "
                         "attestation's classification is an S0 fact no boundary withholds")
        fresh = accept(sc, "arch", actor=HUMAN_B)
        sc.admit(*attested(fresh))
        c = view(sc)
        self.assertEqual(c.support.valid("arch"), T)
        self.assertFalse([o for o in c.obligations if o.kind == "REQUALIFY"], "requalified by a fresh acceptance")

    def test_a_record_not_in_effect_at_r_needs_no_requalification(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        sc.admit(accept(sc, "arch"))
        sc.absorb({"arch.md": "a2\n"})  # the acceptance is not current at R
        loss(sc, sc.position - 1)
        self.assertFalse([o for o in view(sc).obligations if o.kind == "REQUALIFY"])


class AnalyzerPinning(unittest.TestCase):
    """§5.9: a host lacking a pinned analyzer makes no current assertion (finding 6ff4ed1 B3)."""

    def test_missing_analyzer(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a1\n", "impl.md": "i1\n"})
        adoption = record("RULESET_ADOPTION", target=None, actor=OWNER, fields={
            "system": "ssds-rules/1", "policy": "sha256:" + "0" * 64,
            "analyzers": ["ssds.analyzer.python/1", "ssds.analyzer.rust/9"]})
        sc.entries.append(lifecycle_body(sc.position, adoption))
        c = view(sc)
        self.assertEqual(c.missing_analyzers, frozenset({"ssds.analyzer.rust/9"}))
        self.assertFalse(c.current_assertion)
        self.assertTrue(view(sc, 0).support is not None and not view(sc, 0).missing_analyzers,
                        "the earlier position keeps its own analyzer set")


if __name__ == "__main__":
    unittest.main()
