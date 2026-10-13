"""Bounded model check of SSDS 8.0 workplan §6.6 S1 polarity and the
assessment-disagreement predicates (design revision 11 and later).

This is a diagnostic transcription of the workplan's equations, not an SSDS
implementation and not an adequacy oracle (DS-001): it can show that the
written predicates contradict their own stated properties on small ledgers,
never that the design is right.

Checked properties, for every ledger L and every appended record r:
  P1  appending an open ordinary challenge never ends a dispute;
  P2  appending a LEDGER_LOSS never ends a dispute;
  P3  appending an open counter-challenge never lifts a revocation;
  P4  appending a LEDGER_LOSS never lifts a revocation.

Sensitivity: with REV10=1 in the environment the dispute predicate reverts to
revision 10's currency-based form, and P1/P2 must fail (the 124b0b7 Review's
Blocker A); a run that stays green under REV10=1 means the check is blind.

Run: python3 qualification/ssds80/s1_disagreement_model_check.py [--depth N]
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass, field
from functools import lru_cache

@dataclass(frozen=True)
class R:
    kind: str  # ASSESS, CHALLENGE, ADJ, WITHDRAW, OVERRIDE, IMMAT, LOSS, ATTEST
    target: int | None = None  # position of target record
    outcome: str | None = None  # PASS/FAIL for ASSESS; UPHELD/DISMISSED for ADJ
    blocking: bool = False
    key: str | None = None
    supersedes: int | None = None
    holds: frozenset = field(default_factory=frozenset)  # ATTEST: positions held


class Ledger:
    def __init__(self, recs: tuple[R, ...]):
        self.r = recs
        self.n = len(recs)

    # ---- S0 syntax -------------------------------------------------------
    def superseded(self, x: int) -> bool:
        return any(y.supersedes == x for y in self.r)

    # ---- S1 polarity (strictly earlier targets) ---------------------------
    @lru_cache(maxsize=None)
    def restrictive(self, a: int) -> bool:
        ra = self.r[a]
        return ra.kind == "ADJ" and ra.outcome == "UPHELD" and not self.counter(ra.target)

    @lru_cache(maxsize=None)
    def counter(self, c: int) -> bool:
        rc = self.r[c]
        return rc.kind == "CHALLENGE" and self.restrictive(rc.target)

    @lru_cache(maxsize=None)
    def relaxer(self, y: int) -> bool:
        ry = self.r[y]
        if ry.kind in ("WITHDRAW", "OVERRIDE", "ATTEST"):
            return True
        if ry.kind == "ADJ":
            if ry.outcome == "DISMISSED":
                return not self.counter(ry.target)
            return self.counter(ry.target)
        return False

    # ---- S1 force and continuity (strictly later resolvers) ---------------
    @lru_cache(maxsize=None)
    def held(self, x: int, b: int) -> bool:
        return any(
            self.r[a].kind == "ATTEST" and self.r[a].target == b and self.in_force(a) and x in self.r[a].holds
            for a in range(b + 1, self.n)
        )

    @lru_cache(maxsize=None)
    def cont(self, x: int) -> bool:
        return all(self.held(x, b) for b in range(x + 1, self.n) if self.r[b].kind == "LOSS")

    def gate(self, y: int) -> bool:
        return self.cont(y) if self.relaxer(y) else True

    @lru_cache(maxsize=None)
    def in_force(self, y: int) -> bool:
        assert self.r[y].kind in ("ADJ", "WITHDRAW", "OVERRIDE", "ATTEST")
        if not self.gate(y):
            return False
        for c in range(y + 1, self.n):
            rc = self.r[c]
            if rc.kind == "CHALLENGE" and rc.target == y:
                if self.upheld(c) or (rc.blocking and self.open(c) and not self.counter(c)):
                    return False
        return True

    @lru_cache(maxsize=None)
    def open(self, c: int) -> bool:
        return not any(
            self.r[y].kind in ("ADJ", "WITHDRAW") and self.r[y].target == c and self.in_force(y)
            for y in range(c + 1, self.n)
        )

    @lru_cache(maxsize=None)
    def upheld(self, c: int) -> bool:
        return any(
            self.r[a].kind == "ADJ" and self.r[a].target == c and self.r[a].outcome == "UPHELD" and self.in_force(a)
            for a in range(c + 1, self.n)
        )

    def overridden(self, c: int) -> bool:
        return self.open(c) and any(
            self.r[o].kind == "OVERRIDE" and self.r[o].target == c and self.in_force(o) for o in range(c + 1, self.n)
        )

    def status1(self, z: int) -> str:
        chs = [c for c in range(z + 1, self.n) if self.r[c].kind == "CHALLENGE" and self.r[c].target == z]
        if any(self.upheld(c) for c in chs):
            return "REVOKED"
        live = [c for c in chs if self.r[c].blocking and self.open(c)]
        if any(not self.overridden(c) for c in live):
            return "BLOCKED"
        if live:
            return "PROVISIONAL"
        return "CLEAR"

    # ---- Assessment disagreement (§6.6) -----------------------------------
    def in_effect(self, d: int) -> bool:
        rd = self.r[d]
        if not self.cont(d):
            return False
        if rd.kind in ("ADJ", "WITHDRAW", "OVERRIDE", "ATTEST"):
            return self.in_force(d)
        return (not self.superseded(d)) and self.status1(d) == "CLEAR"

    def disposed(self, am: int) -> bool:
        for d in range(am + 1, self.n):
            rd = self.r[d]
            if rd.supersedes == am and self.in_effect(d):
                return True
            if (
                rd.kind == "ADJ"
                and rd.outcome == "UPHELD"
                and self.r[rd.target].kind == "CHALLENGE"
                and self.r[rd.target].target == am
                and self.in_effect(d)
            ):
                return True
            if rd.kind == "IMMAT" and rd.target == am and self.in_effect(d):
                return True
        return False

    def disputed(self, k: str) -> bool:
        ass = [i for i, x in enumerate(self.r) if x.kind == "ASSESS" and x.key == k]
        has_pass = any(self.r[i].outcome == "PASS" for i in ass)
        fails = [i for i in ass if self.r[i].outcome == "FAIL"]
        if os.environ.get("REV10"):
            # revision 10: a failing assessment counts only while current
            live = lambda i: (not self.superseded(i) and self.cont(i)
                              and self.status1(i) not in ("BLOCKED", "REVOKED"))
            return has_pass and any(live(i) for i in fails)
        return has_pass and any(not self.disposed(i) for i in fails)


def candidates(prefix: tuple[R, ...]) -> list[R]:
    n = len(prefix)
    out = [R("ASSESS", outcome="PASS", key="K"), R("ASSESS", outcome="FAIL", key="K"), R("LOSS")]
    for t in range(n):
        k = prefix[t].kind
        if k in ("ASSESS", "ADJ", "OVERRIDE", "ATTEST", "IMMAT", "WITHDRAW"):
            out += [R("CHALLENGE", target=t, blocking=True), R("CHALLENGE", target=t, blocking=False)]
        if k == "CHALLENGE":
            out += [
                R("ADJ", target=t, outcome="UPHELD"),
                R("ADJ", target=t, outcome="DISMISSED"),
                R("WITHDRAW", target=t),
                R("OVERRIDE", target=t),
            ]
        if k == "ASSESS" and prefix[t].outcome == "FAIL":
            out += [R("IMMAT", target=t), R("ASSESS", outcome="PASS", key="K", supersedes=t)]
        if k == "LOSS":
            out += [R("ATTEST", target=t, holds=frozenset(range(t)))]
    return out


def revoked_any(L: Ledger) -> set:
    return {z for z in range(L.n) if L.r[z].kind == "ASSESS" and L.status1(z) == "REVOKED"}


def check(depth: int) -> int:
    seen = 0
    failures = 0
    frontier = [()]
    for _ in range(depth):
        nxt = []
        for prefix in frontier:
            for rec in candidates(prefix):
                L0, L1 = Ledger(prefix), Ledger(prefix + (rec,))
                seen += 1
                d0, d1 = L0.disputed("K"), L1.disputed("K")
                ordinary_open = rec.kind == "CHALLENGE" and not L1.counter(L1.n - 1)
                if d0 and not d1 and (ordinary_open or rec.kind == "LOSS"):
                    failures += 1
                    print("DISPUTE ENDED BY", rec.kind, prefix + (rec,))
                lost = revoked_any(L0) - revoked_any(L1)
                if lost and ((rec.kind == "CHALLENGE" and L1.counter(L1.n - 1)) or rec.kind == "LOSS"):
                    failures += 1
                    print("REVOCATION LIFTED BY", rec.kind, prefix + (rec,))
                nxt.append(prefix + (rec,))
        frontier = nxt
    print(f"checked {seen} appended-record transitions up to depth {depth}; failures: {failures}")
    return failures


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--depth", type=int, default=5)
    raise SystemExit(1 if check(ap.parse_args().depth) else 0)
