"""Acceptance group 6 (derivation half): no stranded obligation, over every constructed state of groups 3 and 5.

Manual §10.3: in every state an obligation is ready, answered, or shown waiting on the failing entry with the
route that restores it derived; "a non-current judgment a current obligation depends on with no ready or waiting
route" is a defect (8f4e75d N4). The property is stated from §10.3 and §10.4, not from the rule under test:

- every undischarged obligation is ready, answered or waiting on at least one named entry;
- each entry it waits on has its route: a named obligation is derived; a missing judge has human attention;
  an invalid governing unit's subject, when native, has its own obligation that is not itself stranded; an item
  dependency is derived; an issuability wait has a plan-acceptance obligation for the plan;
- every undischarged item or part obligation has a route of §10.4's vocabulary; a decision route has its open
  decision derived; a wait names a recorded answer; a partitioned route has required parts.

The states are every ``Scenario.derive`` result the group 3 and group 5 tests construct, collected by running
those tests against the real owner; the lifecycle replay's chains are checked by its own properties.
"""

from __future__ import annotations

import re
import unittest
from unittest import mock

from ssds.derivation import Workflow

from . import _scenario

GROUPS = ("tests.ssds.test_group3_discriminators", "tests.ssds.test_routes", "tests.ssds.test_partition",
          "tests.ssds.test_reports", "tests.ssds.test_obligations", "tests.ssds.test_conformance_review",
          "tests.ssds.test_step5_review.Partitions", "tests.ssds.test_step5_review.Escalation",
          "tests.ssds.test_step5_review.Routes", "tests.ssds.test_step5_review.FindingsSurvive",
          "tests.ssds.test_step5_review.Floors", "tests.ssds.test_step5_review.Index")
ROUTES = re.compile(r"^(dispatch|re-dispatch|pending-candidate|discharged|resume|item-level-review|"
                    r"COORDINATE:.+|human-attention:.+|awaiting-(amendment|challenge):.+|partitioned:.+)$")
OBLIGATION_ID = re.compile(r"sha256:[0-9a-f]{64}")
SETTLED = ("DISCHARGED", "DISCHARGED_PROVISIONAL")


def stranded(w: Workflow) -> list[str]:
    """Every violation of §10.3's no-stranded-obligation rule in one state."""

    problems: list[str] = []
    obligations = {o.id: o for o in w.obligations}
    attention = {o.target.get("waiting") for o in obligations.values() if o.kind == "HUMAN_ATTENTION"}
    plan_accepts = {o.plan for o in obligations.values() if o.kind == "PLAN_ACCEPT"}
    structure = w.s.view.structure

    def unstranded(o) -> bool:
        readiness = w.readiness(o)
        return readiness.state != "WAITING" or bool(readiness.waiting_on)

    for o in obligations.values():
        if w.discharge(o) in SETTLED:
            continue
        readiness = w.readiness(o)
        if readiness.state == "WAITING" and not readiness.waiting_on:
            problems.append(f"{o.kind} {o.id[:19]} waits on nothing named")
        for reason in readiness.waiting_on:
            if ROUTES.match(reason):
                continue  # an item's route, checked below
            named = [i for i in OBLIGATION_ID.findall(reason) if i != o.id]
            if reason == "no eligible judge":
                if o.id not in attention:
                    problems.append(f"{o.kind} {o.id[:19]} waits on a missing judge with no human attention")
            elif named:
                problems += [f"{o.kind} {o.id[:19]} waits on {i[:19]}, not derived" for i in named if i not in obligations]
            elif reason.startswith("governing unit "):
                unit = reason.split()[2]
                subject = structure.subj(unit) if unit in structure.units else None
                if subject is not None and w.s.mode(subject) == "NATIVE":
                    routes = [x for x in obligations.values() if w.subject_of(x) == subject and x.id != o.id]
                    if not any(unstranded(x) for x in routes):
                        problems.append(f"{o.kind} {o.id[:19]} waits on {unit}, whose subject has no route")
            elif reason.startswith("not issuable") and o.plan not in plan_accepts and not w.plan_acceptances:
                problems.append(f"{o.kind} {o.id[:19]} is not issuable and no plan acceptance is owed")
    for item in w.items.all:
        for holder in (item, *item.parts):
            if holder.discharge() in SETTLED:
                continue
            route = holder.route
            if not ROUTES.match(route.route):
                problems.append(f"{holder.unit} has no route ({route.route!r})")
                continue
            if route.route.startswith(("COORDINATE:", "human-attention:")) and not route.decisions:
                problems.append(f"{holder.unit} routes to a decision with none open")
            if route.route.startswith("awaiting-") and route.route.split(":", 1)[1] not in w.s.records:
                problems.append(f"{holder.unit} waits on an answer not recorded")
            if route.route.startswith("partitioned:") and holder is item and not item.parts:
                problems.append(f"{holder.unit} is partitioned into no parts")
            for decision in route.decisions:
                if decision.id not in obligations:
                    problems.append(f"{holder.unit}'s decision {decision.id[:19]} is not derived")
    return problems


class NoStrandedObligation(unittest.TestCase):
    def test_every_constructed_state_of_groups_3_and_5(self) -> None:
        states = []
        original = _scenario.Scenario.derive

        def derive(scenario, position=None):
            support = original(scenario, position)
            states.append(support)
            return support

        suite = unittest.defaultTestLoader.loadTestsFromNames(GROUPS)
        with mock.patch.object(_scenario.Scenario, "derive", derive):
            result = unittest.TestResult()
            suite.run(result)
        self.assertEqual((result.errors, result.failures), ([], []), "the groups themselves pass")
        self.assertGreater(len(states), 100)
        found = {}
        for support in states:
            for problem in stranded(Workflow(support)):
                found.setdefault(problem, 0)
                found[problem] += 1
        self.assertEqual(found, {}, f"stranded obligations in {len(states)} states")

    def test_the_check_sees_a_stranded_state(self) -> None:
        """The property bites: a decision route whose decision is not derived is reported."""

        from .test_routes import Flow

        f = Flow(budget=1)
        f.iterate_adverse()
        w = f.w()
        self.assertEqual(stranded(w), [])
        item = w.items.all[0]
        derived = Workflow.obligations.func
        with mock.patch.object(Workflow, "obligations", new=property(lambda self: tuple(
                o for o in derived(self) if o.kind != "COORDINATE"))):
            w = f.w()
            self.assertIn(f"{item.unit}'s decision", " ".join(stranded(w)))


if __name__ == "__main__":
    unittest.main()
