"""Run the G2 Stage S design models (step S1): every rule set against every case.

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

Run:  python3 -I qualification/ssds80/models/run_models.py [--seeds]

Exit 0 iff
  1. the framework self-tests pass;
  2. the accepted Manual's rule set ("manual") meets every case's expectation;
  3. every earlier rule set fails every case that names it in `refutes`, so each known
     counterexample (9431629 B1, the SD-46 cases, f044820 B1, 8c1f2f2 B1) is reproduced as a
     failure of the rule it refuted;
  4. with --seeds, the finding index's independent inventory check passes (finding_inventory_check.py)
     and the regression seeds still pass: item_review_history_probe.py, and the
     review-scope and obligation-routing families of judgment_disagreement_model_check.py, and
     s1_disagreement_model_check.py at depth 3.

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
import cases_s3  # noqa: E402
S5_MODULES = ["cases_s5_1", "cases_s5_2_4", "cases_s5_6", "cases_s5_7", "cases_s5_8_13", "cases_s5_14_25"]
from routing import findings_survive, issuable_after, keeps_obligation, route, stranded  # noqa: E402
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


def lifecycle_properties(max_len: int = 4, reading: str = "settled", quiet: bool = False) -> list:
    """Every answer chain up to max_len, for the three item-route conditions (and a kept fence with and
    without a spent budget), checked against properties stated from Manual §10.3, §10.4, §15.4-§15.7
    and SD-54, not against the rule's own output (d8ab75c B1 discriminator):
      P1 never stranded; P2 an answered decision is never open again; P3 a wait names the last counted
      answer, which is unsettled; P4 no re-dispatch or discharge while the budget is spent; P5 the open
      decision is held for human attention exactly when RECURRENCE answers already count; P6 the open
      decision names the last counted answer; P7 the fence is passed only after a counted DECLINE.
    Which answers count is the SD-54 admission statement, restated here: ESCALATE never; DECLINE only for
    a kept fence; CHALLENGE only on a held decision; on a held decision only a human's answer."""
    import itertools
    from routing import ItemState, RECURRENCE
    kinds = [("AMEND", True), ("AMEND", False), ("PARTITION", True), ("DECLINE", True), ("CHALLENGE", True),
             ("CHALLENGE", False), ("ESCALATE", True)]
    alphabet = [(o, st, a) for o, st in kinds for a in ("principal", "human")]
    conds = [("budget-spent", dict(budget_spent=True)), ("kept-fence", dict(fence="kept")),
             ("kept-fence", dict(fence="kept", budget_spent=True)),
             ("item-level-no-part", dict(partitioned=True, parts_discharged=True, predicate_holds=True,
                                         item_level_adverse_no_part=True))]
    bad, n = [], 0
    for cond, kw in conds:
        for k in range(max_len + 1):
            for seq in itertools.product(alphabet, repeat=k):
                # only the last answer may be unsettled or end the chain (PARTITION, DECLINE): an earlier
                # one would have derived no later decision to answer
                if any((not st) or o in ("PARTITION", "DECLINE") for o, st, a in seq[:-1]):
                    continue
                raw = [(f"d{i + 1}", o, st, a) for i, (o, st, a) in enumerate(seq)]
                counted = []
                for aid, o, st, a in raw:
                    held = len(counted) >= RECURRENCE
                    if o == "ESCALATE" or (o == "DECLINE" and cond != "kept-fence") or (o == "CHALLENGE" and not held):
                        continue
                    if held and a != "human":
                        continue
                    counted.append((aid, o, st))
                answered = {(cond, "r1", None)} | {(cond, "r1", c[0]) for c in counted[:-1]} if counted else set()
                st = ItemState(answers={(cond, "r1"): raw}, **kw)
                r, d = route(st, reading)
                n += 1
                item = {x for x in d if x[0] == cond}
                probs = []
                if stranded(st, r, d):
                    probs.append("P1")
                if item & answered:
                    probs.append("P2")
                if r.startswith("awaiting-") and not (counted and r.endswith(":" + counted[-1][0]) and not counted[-1][2]):
                    probs.append("P3")
                if kw.get("budget_spent") and r in ("re-dispatch", "discharged"):
                    probs.append("P4")
                if item:
                    held = len(counted) >= RECURRENCE
                    if r.startswith("human-attention:") != held:
                        probs.append("P5")
                    if item != {(cond, "r1", counted[-1][0] if counted else None)}:
                        probs.append("P6")
                if cond == "kept-fence" and not (counted and counted[-1][1] == "DECLINE") and not (
                        r.startswith("COORDINATE:kept-fence") or r.startswith("human-attention:kept-fence")
                        or r.startswith("awaiting-") or r.startswith("partitioned:")):
                    probs.append("P7")
                if probs:
                    bad.append((cond, kw.get("budget_spent", False), [x[:2] + (x[3],) for x in raw], r, sorted(d), probs))
    if not quiet:
        print(f"S3 lifecycle properties ({reading}): {n} answer chains (length <= {max_len}); "
              f"{len(bad)} violation(s)")
        for b in bad[:8]:
            print("    ", b)
    return bad


def seeds() -> list[str]:
    errors = []
    s1 = os.path.join(os.path.dirname(HERE), "s1_disagreement_model_check.py")
    if subprocess.run([sys.executable, "-I", s1, "--depth", "3"], capture_output=True).returncode != 0:
        errors.append("seed s1_disagreement_model_check.py --depth 3 failed")
    probe = os.path.join(os.path.dirname(HERE), "item_review_history_probe.py")
    if subprocess.run([sys.executable, "-I", probe], capture_output=True).returncode != 0:
        errors.append("seed item_review_history_probe.py failed")
    inv = os.path.join(HERE, "finding_inventory_check.py")
    if subprocess.run([sys.executable, "-I", inv], capture_output=True).returncode != 0:
        errors.append("finding_inventory_check.py found a Review finding heading absent from the index")
    if subprocess.run([sys.executable, "-I", inv, "--self-test"], capture_output=True).returncode != 0:
        errors.append("finding_inventory_check.py --self-test: the check missed a removed finding")
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
    print(f"S3: {len(cases_s3.S3_CASES)} routing cases")
    def keyed(ks, reading):
        # revision 1 keyed item-route decisions on (condition, revision); compare it on that much
        return {k[:2] if reading == "revision1" and len(k) == 3 and k[0] != "recurrence" else k for k in ks}

    ok &= not lifecycle_properties()
    # the properties must discriminate: revision 2's separate recurrence key violates them (d8ab75c B1)
    r2bad = lifecycle_properties(reading="revision2", quiet=True)
    kinds = sorted({p for b in r2bad for p in b[-1]})
    print(f"S3 lifecycle properties (revision2): {len(r2bad)} violation(s), properties {kinds}")
    ok &= bool(r2bad) and "P6" in kinds        # an open decision that does not name the last counted answer
    for reading in ("catalogue", "revision1", "revision2", "settled"):
        misses = {}
        for c in cases_s3.S3_CASES:
            r, d = route(c.state, reading)
            probs = []
            if not r.startswith(c.route_prefix):
                probs.append(f"route {r}, expected {c.route_prefix}")
            if keyed(d, reading) != keyed(c.decisions, reading):
                probs.append(f"open decisions {sorted(d)}, expected {sorted(c.decisions)}")
            if stranded(c.state, r, d):
                probs.append("stranded (no route, no open decision)")
            if not findings_survive(c.state, r, d):
                probs.append("an out-of-scope finding reaches no decision")
            if probs:
                misses[c.name] = "; ".join(probs) + f" ({c.why})"
        print(f"S3 {reading}: {len(misses)} miss(es)")
        for case, why in misses.items():
            print(f"    {case}: {why}")
        if reading == "settled":
            ok &= not misses
        else:
            unrep = [c.name for c in cases_s3.S3_CASES if reading in c.refutes and c.name not in misses]
            for c in unrep:
                print(f"    NOT REPRODUCED: {c}")
            ok &= not unrep
    for reading in ("catalogue", "settled"):
        misses = {c.name: c for c in cases_s3.IDENTITY_CASES
                  if keeps_obligation(c.change, reading) != c.keeps or issuable_after(c.change) != c.issuable}
        print(f"S3 identity {reading}: {len(misses)} miss(es) {sorted(misses)}")
        if reading == "settled":
            ok &= not misses
        else:
            unrep = [c.name for c in cases_s3.IDENTITY_CASES if reading in c.refutes and c.name not in misses]
            ok &= not unrep
            for c in unrep:
                print(f"    NOT REPRODUCED: {c}")
    for mod_name in S5_MODULES:
        mod = importlib.import_module(mod_name)
        misses = {}
        refuted_missing = []
        for c in mod.CASES:
            for reading, fn in c.compute.items():
                got = fn()
                if reading == "settled" and got != c.expected:
                    misses[c.name] = f"settled gives {got!r}, expected {c.expected!r} ({c.why})"
                if reading in c.refutes and got == c.expected:
                    refuted_missing.append(f"{c.name} ({reading})")
            for reading in c.refutes:
                if reading not in c.compute:
                    refuted_missing.append(f"{c.name} ({reading} not computed)")
        print(f"S5 {mod_name}: {len(mod.CASES)} cases; settled misses {len(misses)}; "
              f"refuted readings not reproduced {len(refuted_missing)}")
        for k, v in misses.items():
            print(f"    {k}: {v}")
        for k in refuted_missing:
            print(f"    NOT REPRODUCED: {k}")
        ok &= not misses and not refuted_missing
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
