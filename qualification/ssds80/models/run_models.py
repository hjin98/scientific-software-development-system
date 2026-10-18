"""Run the G2 Stage S design models (step S1): every rule set against every case.

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

Run:  python3 -I qualification/ssds80/models/run_models.py [--seeds]

Exit 0 iff
  1. the framework self-tests pass;
  2. the accepted Manual's rule set ("manual") meets every case's expectation;
  3. every earlier rule set fails every case that names it in `refutes`, so each known
     counterexample (9431629 B1, the SD-46 cases, f044820 B1, 8c1f2f2 B1) is reproduced as a
     failure of the rule it refuted;
  4. with --seeds, the regression seeds still pass: item_review_history_probe.py, and the
     review-scope and obligation-routing families of judgment_disagreement_model_check.py.

What this can discriminate: the selection of judged content from explicit integration histories
and its authors; the owner exception's scope; which ending routes are admissible and independent
for a given policy and authorship; and whether a stated liftability invariant is true in the
no-eligible-judge state. What it cannot: challenge-tier polarity, acting and frames, supersession
chains, basis currency, admission order, routing, evidence disagreement, or any production
consumer. Its expectations are the author's reading of the Manual, so a misreading shared by the
expectations and the Manual's rule set would agree on both sides; independent Review checks that.
"""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from cases import ITEM_CASES, OBJECTION_CASES  # noqa: E402
from framework import Enactment, History, ending_routes  # noqa: E402
from rules import RULESETS  # noqa: E402
import cases_s2  # noqa: E402
from judgment import S2_RULESETS, routes_per_state, waiting_literal_f, waiting_per_state  # noqa: E402


def self_tests() -> list[str]:
    errors = []
    h = History((Enactment.of("a", "k", {"u": 1}, "A"), Enactment.of("b", "k", {"u": 2}, "B"),
                 Enactment.of("a", "k", {}, "Q")))
    if h.current() != {"u": (2, "B")}:
        errors.append("replay: the last change of a unit must give its content and producer")
    if h.producers({"u", "z"}) != {"B"}:
        errors.append("producers: units absent from the history contribute no producer")
    for c in ITEM_CASES:
        if not c.excluded <= {e.author for e in c.history.enactments}:
            errors.append(f"case {c.name}: an expected producer appears nowhere in its history")
    for c in OBJECTION_CASES:
        if c.waiting and c.routes:
            errors.append(f"case {c.name}: an expectation cannot both wait and have routes")
    return errors


def evaluate(rs: dict) -> dict[str, str]:
    """case name -> miss description, for every case the rule set does not meet."""
    misses: dict[str, str] = {}
    for c in ITEM_CASES:
        got = c.history.producers(rs["item"](c.history, c.target))
        if got != c.excluded:
            misses[c.name] = f"excludes {sorted(got)}, expected {sorted(c.excluded)} ({c.why})"
    for c in OBJECTION_CASES:
        r = ending_routes(c.state, rs["independent"])
        waiting = r.waiting_on is not None and r.human_attention
        problems = []
        if set(r.admissible) != c.routes:
            problems.append(f"routes {sorted(r.admissible)}, expected {sorted(c.routes)}")
        if waiting != c.waiting:
            problems.append(f"waiting {waiting}, expected {c.waiting}")
        if not rs["invariant"](c.state, rs["independent"]):
            problems.append("its stated liftability invariant is false in this lawful state")
        if problems:
            misses[c.name] = "; ".join(problems) + f" ({c.why})"
    return misses


def evaluate_s2(rs: dict) -> dict[str, str]:
    """S2 (RR-2, RR-3, RR-11): case name -> miss description."""
    misses: dict[str, str] = {}
    for c in cases_s2.TX_CASES:
        got = {p for _, _, p in rs["j"](c.history_at_issue, c.candidate)}
        sup = rs["supports"](c.history_at_integration, c.candidate)
        probs = []
        if got != c.excluded:
            probs.append(f"excludes {sorted(got)}, expected {sorted(c.excluded)}")
        if sup != c.supported:
            probs.append(f"supports integration {sup}, expected {c.supported}")
        if probs:
            misses[c.name] = "; ".join(probs) + f" ({c.why})"
    for c in cases_s2.BIND_CASES:
        bound: dict = {}
        ident = (c.first.base, c.first.delta)
        rs["bind"](bound, c.first, ident)
        got = rs["bind"](bound, c.second, (c.second.base, c.second.delta))
        if got != c.second_admitted:
            misses[c.name] = f"second admitted {got}, expected {c.second_admitted} ({c.why})"
    for c in cases_s2.TARGET_CASES:
        probs = []
        ans = any(rs["target_of"](r) == c.obligation_target for r in c.reviews)
        if ans != c.answered:
            probs.append(f"answered {ans}, expected {c.answered}")
        if c.relief is not None:
            rel = c.relief.outcome == "PASS" and rs["target_of"](c.relief) == c.obligation_target
            if rel != c.relieved:
                probs.append(f"relieves {rel}, expected {c.relieved}")
        if probs:
            misses[c.name] = "; ".join(probs) + f" ({c.why})"
    for c in cases_s2.ROUTE_CASES:
        got = set(rs["routes"](c.objection))
        if got != c.routes:
            misses[c.name] = f"routes {sorted(got)}, expected {sorted(c.routes)} ({c.why})"
    return misses


def seeds() -> list[str]:
    errors = []
    probe = os.path.join(os.path.dirname(HERE), "item_review_history_probe.py")
    if subprocess.run([sys.executable, "-I", probe], capture_output=True).returncode != 0:
        errors.append("seed item_review_history_probe.py failed")
    path = os.path.join(os.path.dirname(HERE), "judgment_disagreement_model_check.py")
    spec = importlib.util.spec_from_file_location("jdmc", path)
    m = importlib.util.module_from_spec(spec)
    sys.modules["jdmc"] = m
    spec.loader.exec_module(m)
    for fam in (m.REVIEW_SCOPE, m.ROUTING):
        m.MUT.clear()
        r = m.run_family(fam, verbose=False)
        if r["fails"]:
            errors.append(f"seed family {fam} failed: {r['fails']}")
    return errors


def main() -> int:
    ok = True
    errs = self_tests()
    for e in errs:
        print("SELF-TEST", e)
    ok &= not errs
    cases = {c.name: c for c in ITEM_CASES + OBJECTION_CASES}
    print(f"{len(ITEM_CASES)} item cases, {len(OBJECTION_CASES)} objection cases")
    for name, rs in RULESETS.items():
        misses = evaluate(rs)
        print(f"{name}: {len(misses)} miss(es)")
        for case, why in misses.items():
            print(f"    {case}: {why}")
        if name == "manual":
            ok &= not misses
            continue
        unreproduced = [c for c, v in cases.items() if name in v.refutes and c not in misses]
        for c in unreproduced:
            print(f"    NOT REPRODUCED: {c} should refute {name} ({cases[c].refutes[name]})")
        ok &= not unreproduced
    s2 = {c.name: c for c in cases_s2.TX_CASES + cases_s2.BIND_CASES + cases_s2.TARGET_CASES
          + cases_s2.ROUTE_CASES}
    print(f"S2: {len(cases_s2.TX_CASES)} transformation, {len(cases_s2.BIND_CASES)} binding, "
          f"{len(cases_s2.TARGET_CASES)} target, {len(cases_s2.ROUTE_CASES)} route cases")
    for name, rs in S2_RULESETS.items():
        misses = evaluate_s2(rs)
        print(f"S2 {name}: {len(misses)} miss(es)")
        for case, why in misses.items():
            print(f"    {case}: {why}")
        if name == "manual":
            ok &= not misses
            continue
        unreproduced = [c for c, v in s2.items() if name in v.refutes and c not in misses]
        for c in unreproduced:
            print(f"    NOT REPRODUCED: {c} should refute {name} ({s2[c].refutes[name]})")
        ok &= not unreproduced
    for q in cases_s2.G1_QUESTIONS:
        routes = routes_per_state(q.objection)
        lit = bool(routes) or waiting_literal_f(q.objection)
        per = bool(routes) or waiting_per_state(q.objection)
        print(f"Q1 {q.name}: routes {sorted(routes)}; (h)(4) with (f) as at dddfedf: "
              f"{'holds' if lit else 'FALSE'}; with amendment A1 (per route and state): "
              f"{'holds' if per else 'FALSE'}")
        # the dddfedf reading must reproduce the gap, and the amended reading must close it
        ok &= (not lit) and per
    if "--seeds" in sys.argv:
        errs = seeds()
        for e in errs:
            print("SEED", e)
        ok &= not errs
        print("seeds:", "OK" if not errs else "FAILED")
    print("OK" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
