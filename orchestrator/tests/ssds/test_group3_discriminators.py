"""Group 3 Review-named discriminators carried in Phase D (G2 workplan §5.3), the derivation half.

Each test names the finding it realizes and states its expectation from the
Manual. Discriminators whose distinguishing step is a revision run (§10.2),
plan amendment or tightening (§13.4) or answering (§10.3) are Phase E, and
those whose step is an Admission refusal are Phase F; the Phase D plan lists
them as unexecuted with their reason.
"""

from __future__ import annotations

import unittest

from ssds.derivation import F, P, T
from ssds.derivation.frames import frame_state
from ssds.derivation.judgment import RouteEligibility
from ssds.derivation.support import Support

from ._scenario import attested
from ._scenario import (
    HUMAN,
    HUMAN_B,
    OWNER,
    Scenario,
    agent,
    content,
    fresh,
    integrate,
    judgment,
    on_record,
    submit,
)

TWIN = '''
    [[unit]]
    id = "left"
    kind = "D3"
    scope = [{ path = "left.md" }]
    [[unit]]
    id = "right"
    kind = "D3"
    scope = [{ path = "right.md" }]
'''
GATE_POLICY = '''schema = 1
[domains.D3]
gates = ["design-gate"]
gate_holders = ["human:SHA256:alice", "human:SHA256:bob", "human:SHA256:owner"]
owner = "human:SHA256:owner"
'''


def gate(sc: Scenario, subject: str, outcome: str, actor: str, frame="ADMITTED", basis=None, supersedes=()) -> dict:
    return judgment("GATE_DECISION", {"gate": "design-gate", "subject": sc.triple(subject), "core": "sha256:" + "c" * 64},
                    outcome, actor=actor, basis=basis if basis is not None else [content(subject, sc.rev(subject))],
                    frame=frame, supersedes=supersedes,
                    fields={"adequacy": "ADEQUATE" if outcome == "ACCEPT" else "INADEQUATE", "qualification": "UNQUALIFIED"})


def accept(sc: Scenario, subject: str, actor: str = OWNER) -> dict:
    t = sc.triple(subject)
    return judgment("ACCEPTANCE", t, "PASS", actor=actor, basis=[content(subject, t["rev"])])


class GateDiscriminators(unittest.TestCase):
    def test_no_identical_content_gate_veto(self) -> None:
        # 362af9f N6: a gate REJECT on one subject does not reach another subject with identical bytes
        sc = Scenario(TWIN, {"left.md": "same\n", "right.md": "same\n"}, policy=GATE_POLICY)
        sc.admit(*attested(accept(sc, "left"), accept(sc, "right"), gate(sc, "left", "ACCEPT", HUMAN), gate(sc, "right", "ACCEPT", HUMAN)))
        sc.admit(*attested(gate(sc, "left", "REJECT", HUMAN_B)))
        d = sc.derive()
        self.assertEqual((d.valid("left"), d.valid("right")), (F, T))

    def test_a_frame_supersession_of_an_admitted_reject_has_no_admitted_effect(self) -> None:
        # b46c250 N4: an admitted REJECT keeps vetoing until the superseding frame integrates
        sc = Scenario(TWIN, {"left.md": "a\n", "right.md": "b\n"}, policy=GATE_POLICY)
        sc.admit(*attested(accept(sc, "left"), gate(sc, "left", "ACCEPT", HUMAN)))
        reject = gate(sc, "left", "REJECT", HUMAN_B)
        sc.admit(*attested(reject))
        x, candidate, _ = submit(sc, {"right.md": "b2\n"}, agent("maker"), "task-1")
        lifting = gate(sc, "left", "ACCEPT", OWNER, frame={"transformation": x}, supersedes=[reject["id"]])
        sc.admit(*attested(lifting))
        admitted = sc.derive()
        self.assertEqual(admitted.valid("left"), F, "the frame supersession does not act in the admitted state")
        in_frame = Support(frame_state(admitted.s.h, admitted.s.n, x, admitted.s))
        self.assertEqual(in_frame.valid("left"), T, "in its own frame it acts")
        integrate(sc, x, candidate)
        self.assertEqual(sc.derive().valid("left"), T, "after integration it acts in the admitted state")

    def test_a_cross_run_reject_is_lifted_in_a_later_run_by_its_author_or_the_owner(self) -> None:
        # 61cd09b N6: the admitted REJECT binds every run; in a later run its own author's reassessment
        # or the owner's supersession lifts it there, and a peer's acceptance does not
        for lifter, lifts in ((HUMAN_B, True), (OWNER, True), (HUMAN, False)):
            with self.subTest(lifter=lifter):
                sc = Scenario(TWIN, {"left.md": "a\n", "right.md": "b\n"}, policy=GATE_POLICY)
                sc.admit(*attested(accept(sc, "left"), gate(sc, "left", "ACCEPT", HUMAN)))
                reject = gate(sc, "left", "REJECT", HUMAN_B)
                sc.admit(*attested(reject))
                x, _, _ = submit(sc, {"right.md": "b2\n"}, agent("maker"), "task-1")
                d = sc.derive()
                self.assertEqual(Support(frame_state(d.s.h, d.s.n, x, d.s)).valid("left"), F, "the reject binds the run")
                supersedes = [reject["id"]] if lifts else []
                sc.admit(*attested(gate(sc, "left", "ACCEPT", lifter, frame={"transformation": x}, supersedes=supersedes)))
                d = sc.derive()
                self.assertEqual(Support(frame_state(d.s.h, d.s.n, x, d.s)).valid("left"), T if lifts else F)
                self.assertEqual(d.valid("left"), F, "and nothing changes in the admitted state")

    def test_an_abandoned_iteration_decides_nothing_and_two_integrated_frames_take_the_minimum(self) -> None:
        # 575dc78 N5, f7419d5 N4 (frames' gate decisions; the D1/D2 run variants are Phase E)
        sc = Scenario(TWIN, {"left.md": "a\n", "right.md": "b\n"}, policy=GATE_POLICY)
        sc.admit(*attested(accept(sc, "left")))
        x1, c1, _ = submit(sc, {"right.md": "b1\n"}, agent("maker"), "task-1")
        sc.admit(*attested(gate(sc, "left", "ACCEPT", HUMAN, frame={"transformation": x1})))
        x2, c2, _ = submit(sc, {"right.md": "b2\n"}, agent("maker"), "task-2")
        qualified = judgment("GATE_DECISION", {"gate": "design-gate", "subject": sc.triple("left"), "core": "sha256:" + "d" * 64},
                             "ACCEPT", actor=HUMAN_B, basis=[content("left", sc.rev("left"))],
                             frame={"transformation": x2}, fields={"adequacy": "ADEQUATE", "qualification": "QUALIFIED"})
        sc.admit(*attested(qualified))
        integrate(sc, x2, c2)
        self.assertEqual(sc.derive().valid("left"), P, "only the integrated iteration's decision acts")
        x3, c3, _ = submit(sc, {"right.md": "b3\n"}, agent("maker"), "task-3")
        sc.admit(*attested(gate(sc, "left", "ACCEPT", HUMAN, frame={"transformation": x3})))
        integrate(sc, x3, c3)
        self.assertEqual(sc.derive().valid("left"), P, "two integrated frames' decisions: the minimum")

    def test_gate_basis_from_source_to_consumer(self) -> None:
        # d94a293 N3: a gate decision relies in record mode on its required premise; when it falls, so does the term
        sc = Scenario(TWIN, {"left.md": "a\n", "right.md": "b\n"}, policy=GATE_POLICY)
        premise = accept(sc, "right", actor=HUMAN_B)
        sc.admit(*attested(accept(sc, "left"), premise))
        decision = gate(sc, "left", "ACCEPT", HUMAN, basis=[content("left", sc.rev("left")), on_record(premise["id"])])
        sc.admit(*attested(decision))
        self.assertEqual(sc.derive().valid("left"), T)
        sc.absorb({"right.md": "b changed\n"})
        d = sc.derive()
        self.assertEqual((d.current(premise["id"]), d.current(decision["id"]), d.valid("left")), (F, F, F))


CHAIN = '''
    [[unit]]
    id = "doc"
    kind = "D3"
    scope = [{ path = "doc.md" }]
'''


class CompositionDiscriminators(unittest.TestCase):
    def test_a_non_independent_hop_composed_with_a_vetoed_peer_hop_supports_nothing(self) -> None:
        # 9e5a763 N1
        sc = Scenario(CHAIN, {"doc.md": "r0\n"})
        r0 = sc.rev("doc")
        consumer = judgment("REVIEW", sc.triple("doc"), "PASS", actor=OWNER, basis=[content("doc", r0, "EDITORIAL")])
        sc.admit(*attested(consumer))  # independent of the baseline it reviews (§5.10 (f))
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1")
        r1 = sc.rev("doc")
        sc.integrate({"doc.md": "r2\n"}, agent("other"), "task-2")
        r2 = sc.rev("doc")
        own_hop = judgment("EQUIVALENCE", {"unit": "doc", "from": r0, "to": r1, "class": "EDITORIAL"}, "EQUIVALENT",
                           actor=agent("author"), actor_class="AGENT", binding=fresh(agent("author"), "task-9"))
        peer_hop = judgment("EQUIVALENCE", {"unit": "doc", "from": r1, "to": r2, "class": "EDITORIAL"}, "EQUIVALENT",
                            actor=HUMAN, binding=None)
        veto = judgment("EQUIVALENCE", {"unit": "doc", "from": r1, "to": r2, "class": "EDITORIAL"}, "NOT_EQUIVALENT",
                        actor=HUMAN_B)
        sc.admit(own_hop, peer_hop, veto)
        d = sc.derive()
        self.assertFalse(d.j.nonind(consumer["id"]), "premise: the consumer itself is independent")
        self.assertTrue(d.j.nonind(own_hop["id"]), "the author of the change cannot qualify its equivalence")
        self.assertTrue(d.j.vetoed(peer_hop["id"]))
        self.assertEqual(d.current(consumer["id"]), F)

    def test_completeness_reach_stays_at_the_same_member_revisions(self) -> None:
        # 63ddf91 N5 (the COMPLETENESS half; the plan half is Phase E)
        sc = Scenario(CHAIN, {"doc.md": "r0\n"})
        d0 = sc.derive()
        membership = d0.s.membership_digest(["doc"])
        old = judgment("COMPLETENESS", {"scope": ["doc"], "classes": ["WARRANT"], "membership": membership}, "INCOMPLETE",
                       actor=HUMAN_B, basis=[content("doc", sc.rev("doc"))])
        sc.admit(old)
        sc.absorb({"doc.md": "r1\n"})
        new = judgment("COMPLETENESS", {"scope": ["doc"], "classes": ["WARRANT"], "membership": membership}, "COMPLETE",
                       actor=HUMAN, basis=[content("doc", sc.rev("doc"))])
        same_rev = judgment("COMPLETENESS", {"scope": ["doc"], "classes": ["WARRANT"], "membership": membership}, "COMPLETE",
                            actor=HUMAN, basis=[content("doc", old["basis"][0]["target"]["rev"])])
        sc.admit(new, same_rev)
        d = sc.derive()
        self.assertFalse(d.j.vetoed(new["id"]), "an objection at old member revisions does not reach new ones")
        self.assertTrue(d.j.vetoed(same_rev["id"]))


ONE = '''
    [[unit]]
    id = "u"
    kind = "D4"
    scope = [{ path = "u.md" }]
'''
OWNER_POLICY = 'schema = 1\n[domains.D4]\nowner = "human:SHA256:owner"\nadjudicators = ["human:SHA256:owner"]\n'


class ReliefDiscriminators(unittest.TestCase):
    def _objection(self):
        sc = Scenario(ONE, {"u.md": "0\n"}, policy=OWNER_POLICY)
        x, cx, _ = submit(sc, {"u.md": "1\n"}, agent("maker"), "task-1")
        result = sc.entries[-1]["records"][0]
        result["binding"].update({"write_scope": ["u"], "item_key": "sha256:" + "a" * 64})
        from ssds.ledger.read import with_id

        sc.entries[-1]["records"][0] = with_id(result)
        objection = judgment("REVIEW", {"transformation": x}, "NO_PASS", actor=HUMAN_B, frame={"transformation": x})
        sc.admit(objection)
        return sc, x, cx, objection

    def _redispatch(self, sc, task: str, files: dict) -> str:
        z, cz, result = submit(sc, files, agent("maker2"), task)
        result["binding"].update({"write_scope": ["u"], "item_key": "sha256:" + "a" * 64})
        from ssds.ledger.read import with_id

        sc.entries[-1]["records"][0] = with_id(result)
        return z

    def test_relief_variants_author_owner_and_peer(self) -> None:
        # 51070e5 N3 (relief variants; the adjudication-independence refusal is Admission's, Phase F)
        sc, x, _, objection = self._objection()
        z = self._redispatch(sc, "task-2", {"u.md": "1\n", "extra.md": "e\n"})
        vetoed = judgment("REVIEW", {"transformation": z}, "PASS", actor=agent("P"), actor_class="AGENT",
                          frame={"transformation": z})
        peer = judgment("REVIEW", {"transformation": z}, "PASS", actor=HUMAN, frame={"transformation": z})
        sc.admit(vetoed, peer)
        in_z = Support(frame_state(sc.derive().s.h, sc.position - 1, z, sc.derive().s))
        self.assertTrue(in_z.j.vetoed(vetoed["id"]))
        self.assertFalse(in_z.j.relieved(objection["id"], vetoed["id"]), "a peer's pass is a disagreement, not relief")
        by_owner = judgment("REVIEW", {"transformation": z}, "PASS", actor=OWNER, frame={"transformation": z})
        sc.admit(by_owner)
        in_z = Support(frame_state(sc.derive().s.h, sc.position - 1, z, sc.derive().s))
        self.assertTrue(in_z.j.relieved(objection["id"], vetoed["id"]))
        self.assertFalse(in_z.j.vetoed(vetoed["id"]))

    def test_relief_does_not_survive_a_revert_to_a_new_target(self) -> None:
        # 051cce3 N5 (the transformation half: relief stays on its exact target)
        sc, x, _, objection = self._objection()
        z = self._redispatch(sc, "task-2", {"u.md": "1\n", "extra.md": "e\n"})
        sc.admit(judgment("REVIEW", {"transformation": z}, "PASS", actor=OWNER, frame={"transformation": z}))
        z2 = self._redispatch(sc, "task-3", {"u.md": "1\n", "extra.md": "e2\n"})
        vetoed = judgment("REVIEW", {"transformation": z2}, "PASS", actor=agent("P"), actor_class="AGENT",
                          frame={"transformation": z2})
        sc.admit(vetoed)
        in_z2 = Support(frame_state(sc.derive().s.h, sc.position - 1, z2, sc.derive().s))
        self.assertTrue(in_z2.j.vetoed(vetoed["id"]), "the relief of Z exempts Z only")

    def test_relief_from_a_rejected_iteration_or_a_sibling_acts_nowhere_else(self) -> None:
        # f22b4dc N5 (the acting half; the revision-run half is Phase E)
        sc, x, _, objection = self._objection()
        z1 = self._redispatch(sc, "task-2", {"u.md": "1\n", "extra.md": "e\n"})
        relief_in_z1 = judgment("REVIEW", {"transformation": z1}, "PASS", actor=OWNER, frame={"transformation": z1})
        sc.admit(relief_in_z1)
        z2 = self._redispatch(sc, "task-3", {"u.md": "1\n", "extra.md": "e\n", "more.md": "m\n"})
        vetoed = judgment("REVIEW", {"transformation": z2}, "PASS", actor=agent("P"), actor_class="AGENT",
                          frame={"transformation": z2})
        sc.admit(vetoed)
        admitted = sc.derive()
        self.assertFalse(admitted.s.acts(relief_in_z1["id"]), "a rejected iteration's record never acts in the admitted state")
        in_z2 = Support(frame_state(admitted.s.h, admitted.s.n, z2, admitted.s))
        self.assertFalse(in_z2.s.acts(relief_in_z1["id"]), "nor in a later iteration's frame")
        self.assertTrue(in_z2.j.vetoed(vetoed["id"]))


class IndependenceInputs(unittest.TestCase):
    """6b986de N6: one definition of each independence input, read the same way by every kind."""

    def test_every_requirement_kind_reads_the_authors_of_what_it_judged(self) -> None:
        sc = Scenario(CHAIN, {"doc.md": "r0\n"})
        sc.integrate({"doc.md": "r1\n"}, agent("author"), "task-1", lineage=[HUMAN])
        t = sc.triple("doc")
        r1 = t["rev"]
        d0 = sc.derive()
        realization = judgment("REALIZATION", {"spec": {"unit": "doc", "rev": r1}, "claim": [{"unit": "doc", "rev": r1}]},
                               "COMPLETE", actor="machinery:dispatcher@ed25519:test", actor_class="MACHINERY",
                               fields={"execution": {}})
        failing = judgment("EVIDENCE_ASSESSMENT", {"realization": realization["id"], "obligation": "e"}, "FAIL",
                           actor=HUMAN_B, fields={"mode": "ORDINARY", "reading": {"unit": "doc", "rev": r1}})
        sc.admit(realization, failing)
        by_author = [
            judgment("ACCEPTANCE", t, "PASS", actor=HUMAN, basis=[content("doc", r1)]),
            judgment("REVIEW", t, "PASS", actor=HUMAN),
            judgment("EQUIVALENCE", {"unit": "doc", "from": r1, "to": r1, "class": "EDITORIAL"}, "EQUIVALENT", actor=HUMAN),
            judgment("COMPLETENESS", {"scope": ["doc"], "classes": ["WARRANT"], "membership": d0.s.membership_digest(["doc"])},
                     "COMPLETE", actor=HUMAN, basis=[content("doc", r1)]),
            judgment("PLAN_ACCEPTANCE", {"units": ["doc"]}, "ACCEPTED", actor=HUMAN,
                     fields={"objective": {"unit": "doc", "rev": r1}, "items": [{"unit": "doc", "rev": r1}]}),
            judgment("IMMATERIALITY", {"records": [failing["id"]]}, "IMMATERIAL", actor=HUMAN),
        ]
        sc.admit(*by_author)
        d = sc.derive()
        for record in by_author:
            with self.subTest(kind=record["kind"]):
                self.assertTrue(d.j.nonind(record["id"]), "the author of the judged content is never independent")


if __name__ == "__main__":
    unittest.main()
