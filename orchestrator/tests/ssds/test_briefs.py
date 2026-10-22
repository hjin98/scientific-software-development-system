"""Phase E step 7: briefs, duty compilation, version binding and the inspector (Manual §16.3-§16.9, §29).

Each brief is rendered by the real renderer over a state the real derivation owner derived from a constructed
ledger. Expected values are written from the Manual: the section order of §16.3 (task), §16.5 (review), §16.6
(gate) and §16.7 (decision); the injection table of §16.3 (each owner present exactly when its event fires);
§16.5's exclusions; §16.8's ordering key ``(-w, c, p, id)``; §16.9's version binding.
"""

from __future__ import annotations

import hashlib
import re
import unittest

from ssds.derivation import Workflow
from ssds.interface.render import NOT_ISSUED, SLOT_DUTIES, Renderer
from ssds.ledger.read import with_id
from ssds.ledger.schema import record_violations

from ._fixtures import record, tree
from ._scenario import HUMAN, HUMAN_B, Scenario, agent, content, fresh, judgment
from .test_lint import FILES, MANIFEST
from .test_obligations import TWO
from .test_reports import FILES as REPORT_FILES
from .test_reports import MANIFEST as REPORT_MANIFEST
from .test_reports import report
from .test_routes import SLOTS, Flow, document_item

TASK_SECTIONS = ["Header", "1. Objective, obligation kind and workflow role", "2. Allowed outcomes", "3. Governing content",
                 "4. Contract boundaries, constraints, non-goals and delegated space",
                 "5. Obligations, criteria, required evidence and slots", "6. Open challenges, findings and provisional states",
                 "7. Incompleteness notices", "8. Governing version", "9. Escalation triggers, budget, workspace and submission"]
GATE_SECTIONS = ["Header", "1. Evidence core", "2. Consequential-decision disclosure", "3. D1/D2 revision assessments",
                 "4. Interpretation (Channel A)", "5. Allowed outcomes and required fields", "Duties", "Incompleteness notices"]
DOCTRINE_SOURCE = "a" * 40


def renderer(w: Workflow, doctrine=None) -> Renderer:
    return Renderer(w, {"label": "QUALIFIED", "position": w.s.n, "digest": "sha256:" + "e" * 64},
                    doctrine or (lambda source, path: None))


def section(brief, title: str) -> str:
    return dict(brief.sections)[title]


def injected(brief) -> set[str]:
    return {d for d in brief.duties if d.startswith("inject:")}


def adopt_doctrine(sc: Scenario, source: str = DOCTRINE_SOURCE) -> None:
    from ._fixtures import RULESET

    sc.lifecycle(record("RULESET_ADOPTION", target=None, actor=HUMAN,
                        fields={"system": "ssds-rules/1", "policy": RULESET["policy"], "analyzers": ["ssds.analyzer.python/1"],
                                "doctrine": {"version": "7.2.1", "source": source}}))


class PolicyFlow(Flow):
    def __init__(self, policy: str, budget: int = 3) -> None:
        self.sc = Scenario(MANIFEST, {**FILES, "plans/work.md": document_item(budget)}, policy=policy)
        self.accept_plan()
        self.counter = 0


class TaskBriefs(unittest.TestCase):
    def test_sections_header_and_compiled_duties(self) -> None:
        f = Flow()
        brief = renderer(f.w()).brief(f.item().obligation)
        self.assertEqual([t for t, _ in brief.sections], TASK_SECTIONS, "§16.3's order")
        header = section(brief, "Header").splitlines()
        self.assertTrue(header[0].startswith("Governing version: NATIVE: ruleset ssds-rules/1"), "§16.9: first lines")
        self.assertIn(NOT_ISSUED, header[1])
        self.assertEqual(brief.duties, ("role:IMPLEMENTER", "core:specialist:DOCUMENT", "slot:claims", "slot:deviations",
                                        "slot:unverified_assumptions"), "role, specialist core, slots; no event fires")
        slots = section(brief, "5. Obligations, criteria, required evidence and slots")
        for slot in ("claims", "deviations", "unverified_assumptions"):
            self.assertIn(SLOT_DUTIES[slot], slots, "each owed question inline")
        self.assertIn("not rendered: the ruleset pins no doctrine", section(brief, "7. Incompleteness notices"))
        self.assertEqual(renderer(f.w()).brief(f.item().obligation).text, brief.text, "deterministic")

    def test_a_pinned_doctrine_renders_the_cores(self) -> None:
        f = Flow()
        adopt_doctrine(f.sc)
        texts = {(DOCTRINE_SOURCE, "source/specialists/software-documentation/SKILL.md"): b"DOCUMENTATION CORE TEXT\n"}
        brief = renderer(f.w(), lambda source, path: texts.get((source, path))).brief(f.item().obligation)
        self.assertEqual(brief.governs, {"mode": "NATIVE", "ruleset": "ssds-rules/1",
                                         "doctrine": {"version": "7.2.1", "source": DOCTRINE_SOURCE}})
        self.assertIn("DOCUMENTATION CORE TEXT", section(brief, "1. Objective, obligation kind and workflow role"))
        self.assertNotIn("not rendered", brief.text)
        self.assertIn(f"doctrine SSDP 7.2.1 at {DOCTRINE_SOURCE}", section(brief, "8. Governing version"))
        unreadable = renderer(f.w(), lambda source, path: None).brief(f.item().obligation)
        self.assertIn("the pinned doctrine source cannot be read", section(unreadable, "7. Incompleteness notices"))

    def test_a_later_iteration_carries_conformance_and_findings_as_data(self) -> None:
        f = Flow()
        x, cand = f.submit("# Records\nWrong.\n")
        review = f.review(x, cand, "NO_PASS", findings=[{"obligation": "o1", "units": ["records"]}])
        brief = renderer(f.w()).brief(f.item().obligation)
        states = section(brief, "6. Open challenges, findings and provisional states")
        self.assertIn("Previous iteration", states)
        self.assertIn(review["id"], states)


class Injection(unittest.TestCase):
    """§16.3: each owner's text is carried exactly when its event fires."""

    def test_domain_owner_kind_duties_and_a_serious_challenge(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"})
        w = Workflow(sc.derive())
        accept = {o.target["subject"]: o for o in w.of_kind("ACCEPT")}
        arch, impl = renderer(w).brief(accept["arch"]), renderer(w).brief(accept["impl"])
        self.assertEqual(injected(arch), {"inject:domain:D3"})
        self.assertEqual(injected(impl), {"inject:domain:D4"})
        self.assertIn("kind:out-of-matrix", arch.duties, "a substantial authority review")
        self.assertNotIn("kind:out-of-matrix", impl.duties)
        sc.admit(judgment("CHALLENGE", sc.triple("arch"), None, actor=HUMAN_B,
                          fields={"blocking": True, "serious": True, "inquiry": "CONFIRMATORY"}))
        w = Workflow(sc.derive())
        accept = {o.target["subject"]: o for o in w.of_kind("ACCEPT")}
        self.assertIn("inject:kernel-challenge", renderer(w).brief(accept["arch"]).duties)
        self.assertNotIn("inject:kernel-challenge", renderer(w).brief(accept["impl"]).duties)

    def test_budget_exhaustion_and_recurrence(self) -> None:
        f = Flow(budget=1)
        self.assertEqual(injected(renderer(f.w()).brief(f.item().obligation)), set())
        f.iterate_adverse()
        (decision,) = f.item().route.decisions
        self.assertEqual(injected(renderer(f.w()).brief(decision)), {"inject:convergence"})
        g = Flow(budget=5)
        for n in (1, 2):
            g.submit(f"# Records {n}\n", outcome="PARTIAL", slots={"claims": []})
        (found,) = [o for o in g.w().of_kind("COORDINATE") if o.target.get("recurrence")]
        self.assertEqual(injected(renderer(g.w()).brief(found)), {"inject:convergence", "inject:pem"})

    def test_a_concern_tag_on_the_write_scope(self) -> None:
        tagged = PolicyFlow('schema = 1\n[workflow]\nconcern_tags = { security = ["records"] }\n')
        self.assertIn("inject:concern:security", renderer(tagged.w()).brief(tagged.item().obligation).duties)
        elsewhere = PolicyFlow('schema = 1\n[workflow]\nconcern_tags = { security = ["design"] }\n')
        self.assertNotIn("inject:concern:security", renderer(elsewhere.w()).brief(elsewhere.item().obligation).duties)

    def test_a_revising_review_and_a_legacy_subject(self) -> None:
        f = Flow()
        w = f.w()
        (revising,) = w.of_kind("REVIEW_REVISION")
        self.assertIn("inject:revising", renderer(w).brief(revising).duties)
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"},
                      modes={"arch": {"mode": "LEGACY", "protocol": "7.2.1"}})
        w = Workflow(sc.derive())
        self.assertFalse([o for o in w.obligations if w.subject_of(o) == "arch"], "a LEGACY subject owes no native work")
        from ssds.derivation.workflow import make

        brief = renderer(w).brief(make("ACCEPT", sc.triple("arch")))
        self.assertEqual((brief.form, brief.governs["profile"]), ("LEGACY", "ssdp-protocol-7.2"),
                         "§16.9: rendered through p's frozen Core profile")


class ReviewBriefs(unittest.TestCase):
    def submitted(self) -> tuple[Flow, str, str, dict]:
        f = Flow()
        base, cand, x, _ = f._candidate({"records.md": "# Records\nDone.\n"})
        result = record("TASK_RESULT", target={"task": "t-1", "candidate": cand, "transformation": x, "base": base},
                        outcome="COMPLETE", actor=agent("maker"), actor_class="AGENT", frame={"transformation": x},
                        fields={"slots": {**SLOTS, "claims": [{"claim": "AUTHOR-CLAIM-MARKER", "records": []}]}})
        result["binding"] = dict(fresh(agent("maker"), "t-1"), obligation=f.item().obligation.id,
                                 item={"unit": "plan.work.item", "rev": f.sc.rev("plan.work.item")})
        result["refs"] = [{"store": "REPO", "digest": "sha256:" + "9" * 64, "media_type": "text/markdown"}]
        result["provenance"] = {"narrative": "AUTHOR-NARRATIVE-MARKER"}
        f.sc.admit(with_id(result))
        return f, x, cand, result

    def test_contains_and_excludes(self) -> None:
        f, x, cand, result = self.submitted()
        w = f.w()
        (o,) = [o for o in w.of_kind("REVIEW") if o.target.get("transformation") == x]
        brief = renderer(w).brief(o)
        self.assertIn("records.md: changed", section(brief, "Candidate diff and machine-produced facts"))
        self.assertIn("AUTHOR-CLAIM-MARKER", section(brief, "Disclosure slots (the author's claims to test)"))
        self.assertIn("the author's claim, to test", brief.text)
        for excluded in ("AUTHOR-NARRATIVE-MARKER", "9" * 64, result["id"]):
            self.assertNotIn(excluded, brief.text, "§16.5: never the author's narrative or its references")
        self.assertIsNone(re.search(r"(?<![A-Z_])COMPLETE(?![A-Z_])", brief.text), "never the author's outcome")
        self.assertIn("kind:review", brief.duties)

    def test_carries_another_judges_standing_objection(self) -> None:
        f, x, cand, _ = self.submitted()
        objection = f.review(x, cand, "NO_PASS", findings=[{"units": ["design"]}], actor=agent("first-reviewer"))
        w = f.w()
        (o,) = [o for o in w.of_kind("REVIEW") if o.target.get("transformation") == x]
        carried = section(renderer(w).brief(o), "Carried objections (another judge's)")
        self.assertIn(objection["id"], carried)
        self.assertIn(agent("first-reviewer"), carried)


class GateAndDecisionBriefs(unittest.TestCase):
    def test_gate_brief_order(self) -> None:
        sc = Scenario(TWO, {"arch.md": "a\n", "impl.md": "i\n", "spec.toml": "s\n"},
                      policy='schema = 1\n[domains.D3]\ngates = ["g"]\nhumans = ["human:SHA256:alice"]\n')
        w = Workflow(sc.derive())
        (gate,) = w.of_kind("GATE")
        brief = renderer(w).brief(gate)
        self.assertEqual([t for t, _ in brief.sections], GATE_SECTIONS, "§16.6: the evidence core first")
        self.assertIn("decision asked: GATE_DECISION", section(brief, "1. Evidence core"))
        self.assertEqual(section(brief, "3. D1/D2 revision assessments"), "not a D1/D2 revision")
        self.assertIn("adequacy and qualification", section(brief, "5. Allowed outcomes and required fields"))

    def test_decision_brief(self) -> None:
        f = Flow(budget=1)
        f.iterate_adverse()
        (decision,) = f.item().route.decisions
        brief = renderer(f.w()).brief(decision)
        self.assertEqual([t for t, _ in brief.sections][:6],
                         ["Header", "Plan objective and items", "Decisions owed", "Budgets, recurrences and discrepancies",
                          "Open human-attention items of the plan", "What changed since the previous coordination"])
        self.assertIn("plan.work.item (DOCUMENT): route COORDINATE:budget-spent", section(brief, "Plan objective and items"))
        self.assertIn("allowed AMEND, PARTITION, ESCALATE", section(brief, "Decisions owed"))
        self.assertIn("role:PRINCIPAL", brief.duties)


class Inspector(unittest.TestCase):
    def test_ordering_by_weight_consequence_and_age(self) -> None:
        sc = Scenario(REPORT_MANIFEST, REPORT_FILES)
        question = report("HUMAN_QUESTION", ["arch"], reasons=("DECISION_NEEDED",))
        sc.admit(question)
        early = report("FINDING", ["numerics"], materiality="MATERIAL")
        sc.admit(early)
        late = report("FINDING", ["numerics"], materiality="MATERIAL", actor=agent("other"))
        sc.admit(late)
        w = Workflow(sc.derive())
        view = renderer(w).inspector()
        order = [e["evidence_core"].get("record", {}).get("id") or e["evidence_core"]["target"].get("waiting")
                 for e in view["entries"]]
        waiting = [i for i, e in enumerate(view["entries"]) if "waiting" in e["evidence_core"]]
        self.assertTrue(waiting and max(waiting) < order.index(question["id"]),
                        "an entry other obligations wait on comes before one nothing waits on")
        self.assertLess(order.index(question["id"]), order.index(early["id"]), "CRITICAL before MATERIAL")
        self.assertLess(order.index(early["id"]), order.index(late["id"]), "older first")
        entry = view["entries"][order.index(early["id"])]
        self.assertEqual((entry["key"]["w"], entry["key"]["c"], entry["key"]["p"]), (0, "MATERIAL", 2))
        revising = next(e for e in view["entries"] if "REVIEW_REVISION" in e["evidence_core"]["detail"])
        self.assertEqual(view["entries"][0], revising, "ACCEPT(numerics) waits on REVIEW(s, r), which waits on it")
        self.assertGreaterEqual(revising["key"]["w"], 2)

    def test_the_digest_lists_what_agents_settled(self) -> None:
        sc = Scenario(REPORT_MANIFEST, REPORT_FILES)
        blocker = report("BLOCKER", ["arch"], reasons=("ENVIRONMENT",))
        sc.admit(blocker)
        by_agent = judgment("COORDINATION_DECISION", {"records": [blocker["id"]]}, "DECLINE", actor=agent("principal"),
                            actor_class="AGENT", fields={"tasks": []})
        by_human = judgment("COORDINATION_DECISION", {"records": [blocker["id"]]}, "DECLINE", actor=HUMAN, fields={"tasks": []})
        sc.admit(by_agent, by_human)
        digest = renderer(Workflow(sc.derive())).inspector()["digest"]
        self.assertEqual([(d.get("record"), d["item"]) for d in digest], [(by_agent["id"], "declined report")])


class DoctrinePin(unittest.TestCase):
    def test_the_adoption_grammar(self) -> None:
        from ._fixtures import RULESET

        fields = {"system": "ssds-rules/1", "policy": RULESET["policy"], "analyzers": ["ssds.analyzer.python/1"]}
        for doctrine, ok in (({"version": "7.2.1", "source": "a" * 40}, True), ({"version": "7.2.1", "source": "main"}, False),
                             ({"version": "7.2.1"}, False), (None, True)):
            rec = record("RULESET_ADOPTION", target=None, fields={**fields, **({"doctrine": doctrine} if doctrine else {})})
            self.assertEqual(record_violations(rec) == [], ok, doctrine)


if __name__ == "__main__":
    unittest.main()
