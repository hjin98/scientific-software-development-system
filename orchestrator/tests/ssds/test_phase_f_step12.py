"""Phase F step 12: the repairs the other-family exit Review of c8122d66 asked for (plan revision 78).

XR-C1: after an absorption Admission revalidates from the held head (catalogue §8.3 step 9), so a second writer that
appends, retires the ledger or leaves a provisional entry between the absorption and the revalidation is seen there.
Nothing is appended after a ``LINEAGE_RETIREMENT`` (§24.2) or over a provisional entry (§22.4, §23.4).

XR-B1: group 2's 29da56e N5 cases through Admission (G2 workplan §5.3), with a second human registered by the real
lifecycle path. Expected values are from catalogue §5.10 (f): Admission refuses an ``ADJUDICATION`` that is not
independent of the authors of its challenge chain's root, alone (``AUTH_ACTOR``); derivation gives every other
non-independent record base ``F``, so it supports and disposes of nothing. The trees here are absorbed, so their
authorship is unknown and a human is independent only with a ``NON_AUTHORSHIP_ATTESTATION`` (§5.10 (f)).
"""

from __future__ import annotations

import unittest
from unittest import mock

from ssds.admission.engine import Admission, AdmissionHalted
from ssds.ledger.append import AppendRefused
from ssds.admission.request import shadow_boundary
from ssds.derivation import F, T
from ssds.derivation.evidence import obligation_token
from ssds.ledger.read import with_id

from ._fixtures import human_key, record, sshsig
from .test_admission_requests import RequestFixture, finding
from . import test_phase_f_step6a, test_phase_f_step9d_iii
from .test_phase_f_step9d_iii import BAD, GOOD, OBL


class PostAbsorption(RequestFixture):
    """Review XR-C1: writer A absorbs the moved head; writer B acts before A revalidates."""

    moved, human_request = test_phase_f_step6a.Absorption.moved, test_phase_f_step6a.Absorption.human_request

    def writers(self) -> tuple[Admission, Admission]:
        return tuple(Admission(self.home, "demo", self.trees, product=self.product, entry_policy=shadow_boundary)
                     for _ in range(2))

    def interleaved(self, a: Admission, obs: str, between) -> tuple[dict, object]:
        """A admits a FINDING at ``obs``; ``between`` runs right after A's absorption. Returns what A saw at its commit
        and A's decision, or the halt it raised."""

        seen: dict = {}
        absorb, commit = a.absorb, a.commit

        def absorb_then(entries, observed):
            absorb(entries, observed)
            between(observed)

        def commit_seeing(entry, head, *args, **kwargs):
            if entry["entry_kind"] == "ADMISSION":  # A's decision, not its absorption
                seen.setdefault("held", a.qualification(a.chain()))
                seen.setdefault("position", entry["position"])
            return commit(entry, head, *args, **kwargs)

        req = self.human_request([with_id({**finding(note="A"), "actor": self.human()})])
        with mock.patch.object(a, "absorb", side_effect=absorb_then), \
                mock.patch.object(a, "commit", side_effect=commit_seeing):
            try:
                outcome = a.admit(req, obs)
            except AdmissionHalted as exc:
                outcome = exc
        return seen, outcome

    def test_nothing_is_appended_after_a_retirement_admitted_since_the_absorption(self) -> None:
        obs = self.moved()
        a, b = self.writers()
        retirement = record("LINEAGE_RETIREMENT", target=None, actor=self.human(),
                            fields={"successor": {"ledger_id": "demo-2", "genesis_digest": "sha256:" + "2" * 64}})
        retired = {}

        def retire(_observed):
            retired["position"] = b.admit_lifecycle(retirement, sshsig(self.private, b.lifecycle_message(retirement)),
                                                    None)
            retired["length"] = len(self.entries())

        seen, outcome = self.interleaved(a, obs, retire)
        self.assertIsInstance(outcome, AdmissionHalted)
        self.assertIn("RETIRED", str(outcome))
        self.assertEqual(seen, {}, "A reaches no commit")
        entries = self.entries()
        self.assertEqual(len(entries), retired["length"], "nothing after the retirement (§24.2)")
        self.assertEqual(entries[-1].entry["position"], retired["position"])
        self.assertEqual(entries[-1].entry["lifecycle"]["kind"], "LINEAGE_RETIREMENT")

    def test_another_writers_provisional_entry_is_settled_before_anything_is_appended(self) -> None:
        obs = self.moved()
        a, b = self.writers()
        left = {}

        def leave_provisional(observed):
            other = self.human_request([with_id({**finding(note="B"), "actor": self.human()})])
            with mock.patch("ssds.admission.engine.write_checkpoint", side_effect=OSError("checkpoint lost")):
                with self.assertRaises(AdmissionHalted):
                    b.admit(other, observed)
            held = b.qualification(b.chain())
            self.assertEqual((held.state, held.provisional), ("QUALIFIED", len(self.entries()) - 1))
            left["position"] = held.provisional

        seen, decision = self.interleaved(a, obs, leave_provisional)
        self.assertEqual((seen["held"].head, seen["held"].provisional), (left["position"], None),
                         "B's entry is held before A's commit (§22.4)")
        self.assertEqual(seen["position"], left["position"] + 1)
        self.assertEqual((decision.decision, decision.position, decision.appended), ("ACCEPT", left["position"] + 1,
                                                                                    True))

    def test_an_absorption_spends_no_compare_and_swap_retry(self) -> None:
        # a lost compare-and-swap re-reads and revalidates up to three times (plan §3.3 step 6b), absorption or not
        obs = self.moved()
        a, _ = self.writers()
        commit, lost = a.commit, []

        def lose_twice(entry, head, *args, **kwargs):
            if entry["entry_kind"] == "ADMISSION" and len(lost) < 2:
                lost.append(entry["position"])
                raise AppendRefused("a stand-in for another writer's append")
            return commit(entry, head, *args, **kwargs)

        req = self.human_request([with_id({**finding(note="A"), "actor": self.human()})])
        with mock.patch.object(a, "commit", side_effect=lose_twice):
            decision = a.admit(req, obs)
        self.assertEqual((len(lost), decision.decision, decision.appended), (2, "ACCEPT", True))

    def test_the_same_request_admitted_since_the_absorption_is_found_not_appended_again(self) -> None:
        obs = self.moved()
        a, b = self.writers()
        req = self.human_request([with_id({**finding(note="A"), "actor": self.human()})])
        first = {}

        def admit_same(observed):
            first["decision"] = b.admit(req, observed)

        absorb = a.absorb
        with mock.patch.object(a, "absorb", side_effect=lambda e, o: (absorb(e, o), admit_same(o))):
            decision = a.admit(req, obs)
        self.assertEqual((decision.position, decision.appended), (first["decision"].position, False))
        self.assertEqual(len(self.entries()), first["decision"].position + 1)


class Objections(test_phase_f_step9d_iii.AdmittedRuns):
    """Review XR-B1: 29da56e N5 at Admission, the records ending an objection signed by the genesis human or a second
    one."""

    def second_human(self) -> tuple[str, object]:
        from ssds.ledger.read import human_key_id

        private, public = human_key(self.root, "second-human")
        actor = human_key_id(public)
        self.lifecycle("REGISTER", {"role": "HUMAN", "id": actor, "public_key": public})
        return actor, private

    def send(self, signer: tuple[str, object], *records):
        from ssds.admission.request import request_message

        actor, private = signer
        req = self.request(records)
        req["binding"] = {"human": {"actor": actor, "signature": sshsig(private, request_message(req))}}
        return self.admission.admit(req, self.head())

    def genesis_human(self) -> tuple[str, object]:
        return self.human(), self.private

    @staticmethod
    def challenge(target: str, actor: str, blocking: bool = True) -> dict:
        return record("CHALLENGE", target={"record": target}, actor=actor,
                      fields={"blocking": blocking, "serious": False, "inquiry": "CONFIRMATORY"})

    @staticmethod
    def adjudication(challenge: dict, outcome: str, actor: str, attested: bool) -> list[dict]:
        a = record("ADJUDICATION", target={"record": challenge["id"]}, outcome=outcome, actor=actor)
        return [a] + ([record("NON_AUTHORSHIP_ATTESTATION", target={"record": a["id"]}, outcome="NOT_AUTHOR",
                              actor=actor)] if attested else [])

    def disposition(self, failing: dict) -> int:
        d = self.derive()
        return d.a.disposition(failing["id"], d.values.get, d.base, d.j.nonind)

    def adjudicate_open(self, challenge: dict) -> bool:
        from ssds.derivation import Workflow

        return any(o.kind == "ADJUDICATE" and o.target == {"record": challenge["id"]}
                   for o in Workflow(self.derive()).obligations)

    def refused_alone(self, decision, rec: dict) -> None:
        self.assertEqual((decision.decision, decision.reasons), ("ACCEPT", ()), "the rest of the request decides")
        self.assertIn((rec["id"], ("AUTH_ACTOR",)), decision.refused)
        self.assertNotIn(rec["id"], decision.admitted)



class CounterChallengeAndDismissal(Objections):
    """29da56e B1 (a), (b) and (d), and N1's recovery."""

    def disposed(self):
        """A failing assessment disposed of by an independent upholding of a challenge of its realization."""

        realization = self.realize(self.tree("T0"), BAD)
        failing = self.fail(realization)
        c1 = self.challenge(realization["id"], self.human())
        self.admit_human(c1)
        upheld = self.adjudication(c1, "UPHELD", self.human(), attested=True)
        self.admit_human(*upheld)
        self.assertEqual(self.disposition(failing), 2)
        return failing, upheld[0]

    def test_counter_challenge_only_an_independent_counter_upholding_restores_the_dispute(self) -> None:
        # 29da56e B1 (a): a non-blocking counter-challenge of the upholding that disposed of the failure; a
        # non-independent upholding of it is refused and restores nothing, an independent one overturns the upholding
        failing, upheld = self.disposed()
        second = self.second_human()
        c2 = self.challenge(upheld["id"], second[0], blocking=False)
        self.assertEqual(self.send(second, c2).admitted, (c2["id"],))
        self.assertEqual(self.disposition(failing), 2, "a non-blocking counter-challenge contests nothing yet")
        (a2,) = self.adjudication(c2, "UPHELD", second[0], attested=False)
        self.refused_alone(self.send(second, a2), a2)
        self.assertEqual(self.disposition(failing), 2, "the disposal stands")
        self.assertTrue(self.adjudicate_open(c2), "29da56e N1: a refused adjudication answers nothing")
        decision = self.send(second, *self.adjudication(c2, "UPHELD", second[0], attested=True))
        self.assertEqual((decision.decision, decision.refused), ("ACCEPT", ()))
        self.assertEqual(self.disposition(failing), 0, "the upholding is overturned: the dispute is live again")
        self.assertFalse(self.adjudicate_open(c2))

    def test_contested_resolution_only_an_independent_dismissal_ends_the_objection(self) -> None:
        # 29da56e B1 (d): a blocking counter-challenge contests the upholding that disposed of the failure; a
        # non-independent dismissal of it is refused and lifts nothing, an independent one restores the disposal
        failing, upheld = self.disposed()
        second = self.second_human()
        c2 = self.challenge(upheld["id"], second[0])
        self.send(second, c2)
        self.assertEqual(self.disposition(failing), 0, "the resolution is contested")
        (dismissal,) = self.adjudication(c2, "DISMISSED", self.human(), attested=False)
        self.refused_alone(self.send(self.genesis_human(), dismissal), dismissal)
        self.assertEqual(self.disposition(failing), 0, "still contested")
        self.assertTrue(self.adjudicate_open(c2), "29da56e N1: a refused adjudication answers nothing")
        decision = self.send(self.genesis_human(), *self.adjudication(c2, "DISMISSED", self.human(), attested=True))
        self.assertEqual((decision.decision, decision.refused), ("ACCEPT", ()))
        self.assertEqual(self.disposition(failing), 2, "the objection to the resolution has ended")
        self.assertFalse(self.adjudicate_open(c2))

    def test_observation_dismissal_a_non_independent_dismissal_leaves_it_not_standing(self) -> None:
        # 29da56e B1 (b), and N1's recovery: ADJUDICATE(c) stays to be answered
        realization = self.realize(self.tree("T0"), BAD)
        second = self.second_human()
        c = self.challenge(realization["id"], second[0])
        self.send(second, c)
        self.assertFalse(self.derive().a.standing(realization["id"]), "a blocking challenge: not standing")
        (dismissal,) = self.adjudication(c, "DISMISSED", self.human(), attested=False)
        self.refused_alone(self.send(self.genesis_human(), dismissal), dismissal)
        self.assertFalse(self.derive().a.standing(realization["id"]))
        self.assertTrue(self.adjudicate_open(c))
        decision = self.send(self.genesis_human(), *self.adjudication(c, "DISMISSED", self.human(), attested=True))
        self.assertEqual((decision.decision, decision.refused), ("ACCEPT", ()))
        self.assertTrue(self.derive().a.standing(realization["id"]), "an independent dismissal: it stands again")
        self.assertFalse(self.adjudicate_open(c))


class NativeCode(Objections):
    """The ``NATIVE`` subject ``code``, its required evidence passing first (§10.4)."""

    MODES = test_phase_f_step9d_iii.EvidenceClaims.MODES
    OWNED = False  # policy names the genesis human the domain's owner (§5.10 (f), SD-48)

    def policy(self) -> str:
        text = super().policy()
        return text.replace("evidence = true", f'evidence = true\nowner = "{self.human()}"') if self.OWNED else text

    def setUp(self) -> None:
        super().setUp()
        test_phase_f_step9d_iii.EvidenceClaims.passing(self, self.realize(self.tree("T0"), GOOD))
        subject, scope, rev = self.derive().s.subject_triple("code")
        self.triple = {"subject": subject, "scope_id": scope, "rev": rev}

    def content(self) -> list[dict]:
        return [{"mode": "content", "target": {"unit": "code", "rev": self.triple["rev"]}, "class": "EXACT"}]

    def assessment(self, realization: dict, outcome: str, actor: str, *, reading=None, obligation=OBL,
                   supersedes=()) -> dict:
        fields = {"mode": "ORDINARY", "reading": reading or realization["target"]["spec"]}
        if outcome == "FAIL":
            fields["failing_outputs"] = ["x"]
        return record("EVIDENCE_ASSESSMENT", target={"realization": realization["id"], "obligation": obligation},
                      outcome=outcome, actor=actor, supersedes=supersedes, fields=fields,
                      basis=[{"mode": "record", "target": {"record": realization["id"]}, "class": "EXACT"}])

    def attested(self, rec: dict) -> list[dict]:
        return [rec, record("NON_AUTHORSHIP_ATTESTATION", target={"record": rec["id"]}, outcome="NOT_AUTHOR",
                            actor=rec["actor"])]

    def codes(self, decision, rec: dict) -> tuple:
        return dict(decision.refused).get(rec["id"], ())


class TripleAndSupportRoute(NativeCode):
    """29da56e B1 (c) and (g)."""

    def acceptance(self, attested: bool):
        a = record("ACCEPTANCE", target=self.triple, outcome="PASS", actor=self.human(), basis=self.content())
        attestation = record("NON_AUTHORSHIP_ATTESTATION", target={"record": a["id"]}, outcome="NOT_AUTHOR",
                             actor=self.human())
        decision = self.send(self.genesis_human(), *([a, attestation] if attested else [a]))
        self.assertEqual((decision.decision, decision.refused), ("ACCEPT", ()), "admitted either way (§5.10 (f))")
        return a

    def accept_derived(self) -> bool:
        from ssds.derivation import Workflow

        return any(o.kind == "ACCEPT" and o.target.get("subject") == "code"
                   for o in Workflow(self.derive()).obligations)

    def test_support_route_a_non_independent_acceptance_supports_nothing(self) -> None:
        # 29da56e B1 (g): the revision's unknown author's direct ACCEPTANCE PASS is kept as data; ACCEPT(code) stays
        a = self.acceptance(attested=False)
        d = self.derive()
        self.assertTrue(d.j.nonind(a["id"]))
        self.assertEqual(d.valid("code"), F)
        self.assertTrue(self.accept_derived())

    def test_triple_dismissal_only_an_independent_dismissal_lifts_the_block(self) -> None:
        # 29da56e B1 (c): a blocking challenge of the accepted triple, dismissed by the revision's unknown author
        a = self.acceptance(attested=True)
        self.assertEqual((self.derive().j.nonind(a["id"]), self.derive().valid("code")), (False, T))
        self.assertFalse(self.accept_derived())
        second = self.second_human()
        c = record("CHALLENGE", target=self.triple, actor=second[0],
                   fields={"blocking": True, "serious": False, "inquiry": "CONFIRMATORY"})
        self.assertEqual(self.send(second, c).admitted, (c["id"],))
        self.assertEqual(self.derive().valid("code"), F, "the triple is blocked")
        self.assertTrue(self.accept_derived())
        (dismissal,) = self.adjudication(c, "DISMISSED", self.human(), attested=False)
        self.refused_alone(self.send(self.genesis_human(), dismissal), dismissal)
        self.assertEqual(self.derive().valid("code"), F, "the block stays")
        self.assertTrue(self.adjudicate_open(c), "29da56e N1: a refused adjudication answers nothing")
        decision = self.send(self.genesis_human(), *self.adjudication(c, "DISMISSED", self.human(), attested=True))
        self.assertEqual((decision.decision, decision.refused), ("ACCEPT", ()))
        self.assertEqual(self.derive().valid("code"), T, "an independent dismissal lifts it")
        self.assertFalse(self.adjudicate_open(c))


class RejectedRequestSalvage(NativeCode):
    """Review XR-B2 (3): S5 §8 ``rejected_request_salvages_never_lost``, expected ``{rep, fail, adv}``."""

    def test_rejected_request_salvages_never_lost(self) -> None:
        # REQ's "tr" is left out: a TASK_RESULT is SCHEMA_UNSUPPORTED until A10's D4 (SD-70), and an unclean one would
        # refuse the passing judgment on its own (CONFORMANCE_RESULT), so "pass" would no longer discriminate
        h = self.human()
        passing = record("ACCEPTANCE", target=self.triple, outcome="PASS", actor=h, basis=self.content())
        rep = with_id({**finding(units=("code",), note="rep"), "actor": h})
        fail = self.assessment(self.realize(self.tree("T0"), BAD), "FAIL", h)
        adv = record("REVIEW", target=self.triple, outcome="NO_PASS", actor=h, basis=self.content())
        bad = with_id({**finding(units=("code",), note="bad", carrying="ghp_" + "a1B2" * 9), "actor": h})
        decision = self.send(self.genesis_human(), passing, rep, fail, adv, bad)
        self.assertEqual(decision.decision, "REJECT")
        self.assertEqual(set(decision.admitted), {rep["id"], fail["id"], adv["id"]})
        self.assertEqual(self.codes(decision, bad), ("SECRET_DETECTED",), "a record failing its own checks")
        self.assertEqual(self.codes(decision, passing), (), "it passes its own checks; the rejection keeps it out")


class AssessmentSupersession(NativeCode):
    """Review XR-B2 (2): f03b15e N5's required discriminators. An assessment is superseded only on its own key, the
    realization, obligation and reading (§8.3 step 3; §5.10 (b)), by its assessor or the owner."""

    OWNED = True

    def setUp(self) -> None:
        super().setUp()
        self.second = self.second_human()
        self.bad = self.realize(self.tree("T0"), BAD)
        self.failing = self.assessment(self.bad, "FAIL", self.second[0])
        self.assertEqual(self.send(self.second, self.failing).admitted, (self.failing["id"],))

    def test_the_assessors_own_reassessment_is_admitted_and_disposes(self) -> None:
        again = self.assessment(self.bad, "PASS", self.second[0], supersedes=[self.failing["id"]])
        decision = self.send(self.second, *self.attested(again))
        self.assertEqual((decision.decision, decision.refused), ("ACCEPT", ()))
        self.assertEqual(self.disposition(self.failing), 2)

    def test_the_owners_adjudicating_assessment_is_admitted_and_disposes(self) -> None:
        owners = self.assessment(self.bad, "PASS", self.human(), supersedes=[self.failing["id"]])
        decision = self.send(self.genesis_human(), owners)
        self.assertEqual((decision.decision, decision.refused), ("ACCEPT", ()), "the owner exception (SD-48)")
        self.assertEqual(self.disposition(self.failing), 2)

    def test_another_reading_is_refused(self) -> None:
        self.tree("T1", **{"s.py": test_phase_f_step9d_iii.SPEC + "# revised\n"})
        reading = {"unit": "spec", "rev": self.derive().s.h.view(self.at("T1")).rev("spec")}
        self.assertNotEqual(reading, self.bad["target"]["spec"])
        rec = self.assessment(self.bad, "PASS", self.second[0], reading=reading, supersedes=[self.failing["id"]])
        decision = self.send(self.second, *self.attested(rec))
        self.assertIn("AUTH_SUPERSEDES", self.codes(decision, rec))
        self.assertNotIn(rec["id"], decision.admitted)
        self.assertEqual(self.disposition(self.failing), 0, "the failure stands: keyed on the realization alone, "
                                                           "the reassessment would have disposed of it")

    def test_another_obligation_is_refused(self) -> None:
        # this fixture's realization serves one obligation, so another one is no target of it (REF_TARGET): the
        # rejection is executed, the key's obligation member only at the owner (step 4b SupersessionTargets)
        rec = self.assessment(self.bad, "PASS", self.second[0], obligation=obligation_token("code", "other"),
                              supersedes=[self.failing["id"]])
        decision = self.send(self.second, *self.attested(rec))
        self.assertIn("REF_TARGET", self.codes(decision, rec))
        self.assertNotIn(rec["id"], decision.admitted)
        self.assertEqual(self.disposition(self.failing), 0)

    def test_plan_acceptance_supersession_fails_closed(self) -> None:
        # f03b15e N5's overlap case is not executed: in Phase F a PLAN_ACCEPTANCE's supersession is refused as
        # unsupported whatever its items (its conditional target has no built owner, plan review 8a41539 B2), so this
        # shows only that the kind fails closed
        view = self.derive().s.h.view(self.at("T0"))
        items = [{"unit": u, "rev": view.rev(u)} for u in ("code", "spec")]
        rejected = record("PLAN_ACCEPTANCE", target={"units": ["code", "spec"]}, outcome="REJECTED",
                          actor=self.second[0], fields={"objective": items[0], "items": items})
        self.assertEqual(self.send(self.second, *self.attested(rejected)).refused, ())
        overlap = record("PLAN_ACCEPTANCE", target={"units": ["code"]}, outcome="ACCEPTED", actor=self.human(),
                         fields={"objective": items[0], "items": items[:1]}, supersedes=[rejected["id"]])
        decision = self.send(self.genesis_human(), *self.attested(overlap))
        self.assertEqual(self.codes(decision, overlap), ("SCHEMA_UNSUPPORTED",))
        self.assertNotIn(overlap["id"], decision.admitted)

    def test_equivalence_class_supersession_is_refused(self) -> None:
        r0 = self.triple["rev"]
        self.tree("T1", **{"a.py": "v = 2\n"})
        r1 = self.derive().s.h.view(self.at("T1")).rev("code")
        target = {"unit": "code", "from": r0, "to": r1}
        not_equivalent = record("EQUIVALENCE", target={**target, "class": "CONSUMER:k"}, outcome="NOT_EQUIVALENT",
                                actor=self.second[0])
        self.assertEqual(self.send(self.second, *self.attested(not_equivalent)).refused, ())
        migration = record("EQUIVALENCE", target={**target, "class": "MIGRATION"}, outcome="EQUIVALENT",
                           actor=self.human(), supersedes=[not_equivalent["id"]])
        decision = self.send(self.genesis_human(), *self.attested(migration))
        self.assertIn("AUTH_SUPERSEDES", self.codes(decision, migration), "the class is part of the key")
        self.assertNotIn(migration["id"], decision.admitted)
        same_class = record("EQUIVALENCE", target={**target, "class": "CONSUMER:k"}, outcome="EQUIVALENT",
                            actor=self.human(), supersedes=[not_equivalent["id"]])
        decision = self.send(self.genesis_human(), *self.attested(same_class))
        self.assertEqual((decision.refused, decision.admitted[0]), ((), same_class["id"]), "the owner, on the key")


class OwnerRoutes(NativeCode):
    """Review XR-B2 (1): three of S1's ``OWNER`` cases (``qualification/ssds80/models/cases.py``) at their
    ``4:upheld-challenge`` route, through the real ``authorize``: ``author_owner_failing_disposition``,
    ``non_author_owner``, and ``author_owner``'s shape on a subject review. The genesis human is the owner, of unknown
    authorship unless attested. ``policy_names_resolver`` and ``unknown_lineage_owner_agent`` are reachable but not
    run here: with every root of unknown authorship, an attested-fresh agent is refused with the same ``AUTH_ACTOR``,
    so neither case can discriminate without a known author (an admitted integration, SD-70)."""

    OWNED = True

    def setUp(self) -> None:
        super().setUp()
        self.second = self.second_human()

    def objection(self, rec: dict) -> dict:
        self.assertEqual(self.send(self.second, rec).refused, ())
        c = self.challenge(rec["id"], self.second[0])
        self.send(self.second, c)
        return c

    def test_author_owner_failing_disposition_the_one_exception(self) -> None:
        # author_owner_failing_disposition: routes include 4:upheld-challenge
        failing = self.assessment(self.realize(self.tree("T0"), BAD), "FAIL", self.second[0])
        c = self.objection(failing)
        (upheld,) = self.adjudication(c, "UPHELD", self.human(), attested=False)
        decision = self.send(self.genesis_human(), upheld)
        self.assertEqual((decision.decision, decision.refused, decision.admitted), ("ACCEPT", (), (upheld["id"],)))
        self.assertEqual(self.disposition(failing), 2)
        self.assertTrue(self.derive().j.common_mode(upheld["id"]), "its common-mode dependency recorded (SD-48)")

    def test_author_owner_review_no_route_and_the_objection_waits(self) -> None:
        # author_owner_transformation_review's shape on a subject review: no route; the objection waits
        adverse = record("REVIEW", target=self.triple, outcome="NO_PASS", actor=self.second[0], basis=self.content())
        c = self.objection(adverse)
        (upheld,) = self.adjudication(c, "UPHELD", self.human(), attested=False)
        self.refused_alone(self.send(self.genesis_human(), upheld), upheld)
        self.assertTrue(self.adjudicate_open(c))

    def test_non_author_owner_ends_the_objection(self) -> None:
        # non_author_owner: routes include 4:upheld-challenge
        adverse = record("REVIEW", target=self.triple, outcome="NO_PASS", actor=self.second[0], basis=self.content())
        c = self.objection(adverse)
        decision = self.send(self.genesis_human(), *self.adjudication(c, "UPHELD", self.human(), attested=True))
        self.assertEqual((decision.decision, decision.refused), ("ACCEPT", ()))
        self.assertFalse(self.adjudicate_open(c))


if __name__ == "__main__":
    unittest.main()
