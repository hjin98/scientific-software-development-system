"""Bounded model check of SSDS 8.0 workplan §6.6 S1 polarity and assessment
disagreement (design revision 12 and later).

This is a diagnostic transcription of the workplan's equations, not an SSDS
implementation and not an adequacy oracle (DS-001): it can show that the
written predicates contradict their own stated properties on small ledgers,
never that the design is right.

The model has one claim and one evidence obligation. Execution content moves
by MOVE events, each with or without an admitted equivalence judgment; the
governing subject that an IMMATERIALITY judgment relies on moves by GMOVE
events. Equivalence judgments are taken as current.

Checked properties, for every ledger L and every appended record r:
  P1  appending any challenge never raises the evidence term;
  P2  appending a LEDGER_LOSS never raises the evidence term;
  P3  appending an open counter-challenge never lifts a revocation;
  P4  appending a LEDGER_LOSS never lifts a revocation;
  O   the evidence term is T exactly when the plain-language rule says the
      claim is unqualified: a current passing assessment exists, and every
      failing assessment that may still apply has a disposition that stands
      (current, uncontested, not withheld).

Named discriminators (the 97e753f Review's A, B1 and B2, and their contrasts)
are evaluated separately and printed.

Sensitivity: REV11=1 evaluates revision 11's keyed, currency-blind form and
REV10=1 revision 10's currency-based form. Each must report failures; a run
that stays green under either means the check is blind.

Run: python3 qualification/ssds80/s1_disagreement_model_check.py [--depth N]
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass, field

F, P, T = 0, 1, 2
MODE = "REV10" if os.environ.get("REV10") else "REV11" if os.environ.get("REV11") else "REV12"


@dataclass(frozen=True)
class R:
    kind: str  # ASSESS, CHALLENGE, ADJ, WITHDRAW, OVERRIDE, IMMAT, LOSS, ATTEST, MOVE, GMOVE
    target: int | None = None
    outcome: str | None = None  # PASS/FAIL for ASSESS; UPHELD/DISMISSED for ADJ
    blocking: bool = False
    supersedes: int | None = None
    equiv: bool = False  # MOVE: an admitted equivalence judgment covers the move
    holds: frozenset = field(default_factory=frozenset)  # ATTEST: positions held


def memo(fn):
    name = fn.__name__

    def wrapper(self, *args):
        key = (name, args)
        if key not in self._m:
            self._m[key] = fn(self, *args)
        return self._m[key]

    return wrapper


class Ledger:
    def __init__(self, recs: tuple[R, ...]):
        self.r = recs
        self.n = len(recs)
        self._m: dict = {}

    def kind(self, x: int) -> str:
        return self.r[x].kind

    # ---- S0 -----------------------------------------------------------------
    def superseders(self, x: int) -> list[int]:
        return [y for y in range(x + 1, self.n) if self.r[y].supersedes == x]

    def superseded(self, x: int) -> bool:
        return bool(self.superseders(x))

    def exec_rev(self, x: int) -> int:
        return sum(1 for y in range(x) if self.kind(y) == "MOVE")

    def applicable(self, x: int) -> bool:
        """S0: every later execution move is linked by an admitted equivalence."""
        return all(self.r[y].equiv for y in range(x + 1, self.n) if self.kind(y) == "MOVE")

    def gov_moved(self, x: int) -> bool:
        return any(self.kind(y) == "GMOVE" for y in range(x + 1, self.n))

    # ---- S1 polarity (strictly earlier targets) -----------------------------
    @memo
    def restrictive(self, a: int) -> bool:
        ra = self.r[a]
        return ra.kind == "ADJ" and ra.outcome == "UPHELD" and not self.counter(ra.target)

    @memo
    def counter(self, c: int) -> bool:
        rc = self.r[c]
        return rc.kind == "CHALLENGE" and self.restrictive(rc.target)

    @memo
    def relaxer(self, y: int) -> bool:
        ry = self.r[y]
        if ry.kind in ("WITHDRAW", "OVERRIDE", "ATTEST"):
            return True
        if ry.kind == "ADJ":
            if ry.outcome == "DISMISSED":
                return not self.counter(ry.target)
            return self.counter(ry.target)
        return False

    # ---- S1 force and continuity (strictly later resolvers) -----------------
    @memo
    def held(self, x: int, b: int) -> bool:
        return any(
            self.kind(a) == "ATTEST" and self.r[a].target == b and self.in_force(a) and x in self.r[a].holds
            for a in range(b + 1, self.n)
        )

    @memo
    def cont(self, x: int) -> bool:
        return all(self.held(x, b) for b in range(x + 1, self.n) if self.kind(b) == "LOSS")

    def gate(self, y: int) -> bool:
        return self.cont(y) if self.relaxer(y) else True

    @memo
    def in_force(self, y: int) -> bool:
        assert self.kind(y) in ("ADJ", "WITHDRAW", "OVERRIDE", "ATTEST")
        if not self.gate(y):
            return False
        for c in range(y + 1, self.n):
            rc = self.r[c]
            if rc.kind == "CHALLENGE" and rc.target == y:
                if self.upheld(c) or (rc.blocking and self.open(c) and not self.counter(c)):
                    return False
        return True

    @memo
    def open(self, c: int) -> bool:
        return not any(
            self.kind(y) in ("ADJ", "WITHDRAW") and self.r[y].target == c and self.in_force(y)
            for y in range(c + 1, self.n)
        )

    @memo
    def upheld(self, c: int) -> bool:
        return any(
            self.kind(a) == "ADJ" and self.r[a].target == c and self.r[a].outcome == "UPHELD" and self.in_force(a)
            for a in range(c + 1, self.n)
        )

    def overridden(self, c: int) -> bool:
        return self.open(c) and any(
            self.kind(o) == "OVERRIDE" and self.r[o].target == c and self.in_force(o) for o in range(c + 1, self.n)
        )

    def challenges_on(self, z: int) -> list[int]:
        return [c for c in range(z + 1, self.n) if self.kind(c) == "CHALLENGE" and self.r[c].target == z]

    @memo
    def status1(self, z: int) -> str:
        chs = self.challenges_on(z)
        if any(self.upheld(c) for c in chs):
            return "REVOKED"
        live = [c for c in chs if self.r[c].blocking and self.open(c)]
        if any(not self.overridden(c) for c in live):
            return "BLOCKED"
        if live:
            return "PROVISIONAL"
        return "CLEAR"

    def contested(self, d: int) -> bool:
        """An open blocking challenge against d, counter-challenge or not."""
        return any(self.r[c].blocking and self.open(c) for c in self.challenges_on(d))

    # ---- S2 (no cycles in the model, so direct evaluation is the LFP) -------
    def base(self, z: int) -> int:
        if self.superseded(z) or self.status1(z) in ("REVOKED", "BLOCKED") or not self.cont(z):
            return F
        return P if self.status1(z) == "PROVISIONAL" else T

    def basis(self, z: int) -> int:
        if self.kind(z) == "ASSESS":
            return T if self.applicable(z) else F
        if self.kind(z) == "IMMAT":
            return F if self.gov_moved(z) else T
        raise AssertionError(z)

    @memo
    def current(self, z: int) -> int:
        return min(self.base(z), self.basis(z))

    def assessments(self, outcome: str) -> list[int]:
        return [i for i in range(self.n) if self.kind(i) == "ASSESS" and self.r[i].outcome == outcome]

    def upholdings_on(self, x: int) -> list[int]:
        return [
            d
            for c in self.challenges_on(x)
            for d in range(c + 1, self.n)
            if self.kind(d) == "ADJ" and self.r[d].target == c and self.r[d].outcome == "UPHELD"
        ]

    def supersession_closure(self, x: int) -> list[int]:
        out, todo = [], list(self.superseders(x))
        while todo:
            y = todo.pop()
            out.append(y)
            todo += self.superseders(y)
        return out

    # ---- revision 12 ---------------------------------------------------------
    def eff(self, d: int) -> int:
        if self.kind(d) in ("ASSESS", "IMMAT"):
            return self.current(d)
        return T if (self.in_force(d) and self.cont(d) and not self.contested(d)) else F

    def disposers(self, am: int) -> list[int]:
        return (
            self.supersession_closure(am)
            + self.upholdings_on(am)
            + [d for d in range(am + 1, self.n) if self.kind(d) == "IMMAT" and self.r[d].target == am]
        )

    def disp(self, am: int) -> int:
        return max([F] + [self.eff(d) for d in self.disposers(am)])

    def undisputed(self) -> int:
        adverse = [a for a in self.assessments("FAIL") if self.applicable(a)]
        return min([T] + [max(P, self.disp(a)) for a in adverse])

    # ---- revision 11 (sensitivity) -------------------------------------------
    def in_effect11(self, d: int) -> bool:
        if not self.cont(d):
            return False
        if self.kind(d) == "ADJ":
            return self.in_force(d)
        return (not self.superseded(d)) and self.status1(d) == "CLEAR"

    def disposed11(self, am: int) -> bool:
        direct = self.superseders(am) + self.upholdings_on(am)
        direct += [d for d in range(am + 1, self.n) if self.kind(d) == "IMMAT" and self.r[d].target == am]
        return any(self.in_effect11(d) for d in direct)

    def disputed11(self, key: int) -> bool:
        ass = [i for i in range(self.n) if self.kind(i) == "ASSESS" and self.exec_rev(i) == key]
        fails = [i for i in ass if self.r[i].outcome == "FAIL"]
        has_pass = any(self.r[i].outcome == "PASS" for i in ass)
        return has_pass and any(not self.disposed11(i) for i in fails)

    # ---- revision 10 (sensitivity) -------------------------------------------
    def disputed10(self) -> bool:
        live = lambda i: (not self.superseded(i) and self.cont(i) and self.status1(i) not in ("BLOCKED", "REVOKED"))
        return bool(self.assessments("PASS")) and any(live(i) for i in self.assessments("FAIL"))

    # ---- the evidence term ---------------------------------------------------
    def ev(self) -> int:
        passes = self.assessments("PASS")
        if MODE == "REV12":
            return min(max([F] + [self.current(a) for a in passes]), self.undisputed())
        if MODE == "REV11":
            return max([F] + [min(self.current(a), P if self.disputed11(self.exec_rev(a)) else T) for a in passes])
        return min(max([F] + [self.current(a) for a in passes]), P if self.disputed10() else T)

    # ---- plain-language oracle (written independently of the lattice) --------
    def stands(self, d: int) -> bool:
        if self.kind(d) == "ADJ":
            return self.in_force(d) and self.cont(d) and not self.contested(d)
        return (
            not self.superseded(d)
            and self.status1(d) == "CLEAR"
            and self.cont(d)
            and not (self.kind(d) == "ASSESS" and not self.applicable(d))
            and not (self.kind(d) == "IMMAT" and self.gov_moved(d))
        )

    def oracle_unqualified(self) -> bool:
        fully_current_pass = any(
            not self.superseded(a) and self.status1(a) == "CLEAR" and self.cont(a) and self.applicable(a)
            for a in self.assessments("PASS")
        )
        if not fully_current_pass:
            return False
        for am in self.assessments("FAIL"):
            if self.applicable(am) and not any(self.stands(d) for d in self.disposers(am)):
                return False
        return True


def candidates(prefix: tuple[R, ...]) -> list[R]:
    n = len(prefix)
    out = [
        R("ASSESS", outcome="PASS"),
        R("ASSESS", outcome="FAIL"),
        R("LOSS"),
        R("MOVE", equiv=True),
        R("MOVE", equiv=False),
        R("GMOVE"),
    ]
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
        if k == "ASSESS":
            out.append(R("ASSESS", outcome="PASS", supersedes=t))
            if prefix[t].outcome == "FAIL":
                out.append(R("IMMAT", target=t))
        if k == "LOSS":
            out.append(R("ATTEST", target=t, holds=frozenset(range(t))))
    return out


def revoked_any(L: Ledger) -> set:
    return {z for z in range(L.n) if L.kind(z) == "ASSESS" and L.status1(z) == "REVOKED"}


def is_challenge_append(L1: Ledger) -> bool:
    return L1.kind(L1.n - 1) == "CHALLENGE"


# ---- named discriminators: (name, ledger, expected ev under revision 12) ----
PASS_, FAIL_ = R("ASSESS", outcome="PASS"), R("ASSESS", outcome="FAIL")
DISCRIMINATORS = [
    ("base: live pass and fail", (PASS_, FAIL_), P),
    ("A: equivalence move, passing rerun in new execution", (PASS_, FAIL_, R("MOVE", equiv=True), PASS_), P),
    ("A contrast: non-equivalent move, passing rerun", (PASS_, FAIL_, R("MOVE", equiv=False), PASS_), T),
    ("B1: IMMATERIALITY whose prerequisite moved", (PASS_, FAIL_, R("IMMAT", target=1), R("GMOVE")), P),
    ("B1 contrast: IMMATERIALITY, prerequisite unchanged", (PASS_, FAIL_, R("IMMAT", target=1)), T),
    (
        "B2: open blocking counter-challenge against the upholding",
        (PASS_, FAIL_, R("CHALLENGE", target=1, blocking=True), R("ADJ", target=2, outcome="UPHELD"),
         R("CHALLENGE", target=3, blocking=True)),
        P,
    ),
    (
        "B2 contrast: counter-challenge dismissed",
        (PASS_, FAIL_, R("CHALLENGE", target=1, blocking=True), R("ADJ", target=2, outcome="UPHELD"),
         R("CHALLENGE", target=3, blocking=True), R("ADJ", target=4, outcome="DISMISSED")),
        T,
    ),
    (
        "B2 contrast: non-blocking counter-challenge, open",
        (PASS_, FAIL_, R("CHALLENGE", target=1, blocking=True), R("ADJ", target=2, outcome="UPHELD"),
         R("CHALLENGE", target=3, blocking=False)),
        T,
    ),
    ("open challenge against the failing assessment", (PASS_, FAIL_, R("CHALLENGE", target=1, blocking=True)), P),
    ("loss with both assessments retained", (PASS_, FAIL_, R("LOSS"), PASS_), P),
    (
        "superseder chain disposes",
        (PASS_, FAIL_, R("ASSESS", outcome="PASS", supersedes=1), R("ASSESS", outcome="PASS", supersedes=2)),
        T,
    ),
]


def run_discriminators() -> int:
    bad = 0
    for name, recs, want in DISCRIMINATORS:
        got = Ledger(recs).ev()
        ok = got == want
        bad += 0 if ok else 1
        print(f"  [{'ok' if ok else 'DIFFERS'}] {name}: ev={'FPT'[got]} (revision 12 expects {'FPT'[want]})")
    return bad


def check(depth: int) -> int:
    seen = 0
    failures = 0
    frontier = [()]
    counts = {"P1": 0, "P2": 0, "P3": 0, "P4": 0, "O": 0}
    for _ in range(depth):
        nxt = []
        for prefix in frontier:
            L0 = Ledger(prefix)
            e0, rv0 = L0.ev(), revoked_any(L0)
            for rec in candidates(prefix):
                L1 = Ledger(prefix + (rec,))
                seen += 1
                e1 = L1.ev()
                if rec.kind == "CHALLENGE" and e1 > e0:
                    counts["P1"] += 1
                if rec.kind == "LOSS" and e1 > e0:
                    counts["P2"] += 1
                lost = rv0 - revoked_any(L1)
                if lost and rec.kind == "CHALLENGE" and L1.counter(L1.n - 1):
                    counts["P3"] += 1
                if lost and rec.kind == "LOSS":
                    counts["P4"] += 1
                if (e1 == T) != L1.oracle_unqualified():
                    counts["O"] += 1
                nxt.append(prefix + (rec,))
        frontier = nxt
    failures = sum(counts.values())
    print(f"mode {MODE}: checked {seen} appended-record transitions up to depth {depth}; failures: {failures} {counts}")
    return failures


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--depth", type=int, default=5)
    print(f"named discriminators (mode {MODE}):")
    d = run_discriminators()
    f = check(ap.parse_args().depth)
    raise SystemExit(1 if (f or d) else 0)
