"""Bounded model check of SSDS 8.0 workplan §6.6 S1 polarity and assessment
disagreement (design revision 17 and later).

This is a diagnostic transcription of the workplan's equations, not an SSDS
implementation and not an adequacy oracle (DS-001): it can show that the
written predicates contradict their own stated properties on small ledgers,
never that the design is right.

The model has one claim and one evidence obligation. Each ASSESS record is an
assessment of its own realization. Premises move by events:
  MOVE   execution content moves (an evidentiary premise), with or without an
         admitted equivalence judgment;
  ORACLE the oracle/specification moves (an interpretive premise);
  CTX    a context unit moves, read only by assessments with reads=True
         (provenance);
  GMOVE  the governing subject an IMMATERIALITY judgment relies on moves;
  COMPL  a completeness judgment; each assessment relies on the latest one
         before it (provenance, record mode);
  REPART the claim unit's scope changes with no content byte changed (a
         boundary move, merge or adopted governance-neutral delta): its unit
         revision changes, the evaluated content does not;
  RETIRE the evidence obligation stops being required (a specification
         change accepted on its own merits).
An equivalence-covered MOVE is itself the equivalence judgment: it can be
challenged, and it supports currency only while it stands, but it counts for
bearing once admitted. A superseder may be non-independent of the claim's
author (indep=False).

The checked value is V, the claim's evidence conjunct: ev while the
obligation is required, and in every case qual, the undisputed term over
every obligation an admitted failing assessment names (revision 14).

Revision 17 has no mechanical lapse: no move of any kind ends a failing
assessment; only a disposition does (a superseder, typically the assessment
of a configuration rerun, an upheld challenge, or IMMATERIALITY).

Properties, for every ledger L and every appended record r:
  P1  appending any challenge never raises the evidence term;
  P2  appending a LEDGER_LOSS never raises the evidence term;
  P3  appending an open counter-challenge never lifts a revocation;
  P4  appending a LEDGER_LOSS never lifts a revocation;
  P5  moving a premise that is not evidentiary (ORACLE, CTX, GMOVE) never
      raises the evidence term;
  P6  upholding a challenge against a completeness judgment never raises the
      evidence term;
  P7  retiring the evidence obligation never makes the evidence term T while
      a bearing failing assessment has nothing recorded against it;
  P8  a structural-only change (REPART) never raises the evidence term;
  Q   a failing assessment that has no superseder, no challenge against it
      or its realization and no IMMATERIALITY judgment keeps the evidence term
      at most P, whatever moved (stated syntactically);
  O   the evidence term is T exactly when an oracle says the claim is
      unqualified. The oracle is written separately and does not call the
      bearing, disposer or effectiveness predicates it checks.

Named discriminators (the 97e753f and 4c35d92 Reviews' trajectories and
their contrasts) are evaluated separately and printed.

Sensitivity: REV16=1 (content-based lapse, revisions 15-16), REV14=1, REV13=1, REV12=1, REV11=1 and REV10=1 evaluate the earlier forms. Each
must report failures on P1-P6 or Q, not only on O; a run that stays green
there means the check is blind.

Run: python3 qualification/ssds80/s1_disagreement_model_check.py [--depth N]
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass, field

F, P, T = 0, 1, 2
MODE = next((m for m in ("REV10", "REV11", "REV12", "REV13", "REV14", "REV16") if os.environ.get(m)), "REV17")


@dataclass(frozen=True)
class R:
    kind: str  # ASSESS CHALLENGE ADJ WITHDRAW OVERRIDE IMMAT LOSS ATTEST MOVE ORACLE CTX GMOVE COMPL
    target: int | None = None
    outcome: str | None = None  # PASS/FAIL for ASSESS; UPHELD/DISMISSED for ADJ
    blocking: bool = False
    supersedes: int | None = None
    equiv: bool = False  # MOVE: covered by an admitted equivalence judgment
    reads: bool = False  # ASSESS: the assessor read the context unit
    on_real: bool = False  # CHALLENGE: targets the realization of ASSESS `target`
    holds: frozenset = field(default_factory=frozenset)  # ATTEST
    indep: bool = True  # superseder: independent of the claim's author


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

    def later(self, x: int, kind: str) -> list[int]:
        return [y for y in range(x + 1, self.n) if self.kind(y) == kind]

    # ---- S0 -----------------------------------------------------------------
    def superseders(self, x: int) -> list[int]:
        return [y for y in range(x + 1, self.n) if self.r[y].supersedes == x]

    def superseded(self, x: int) -> bool:
        return bool(self.superseders(x))

    def exec_bears(self, x: int) -> bool:
        """The evaluated content is still present: every later content MOVE is equivalence-covered."""
        return all(self.r[y].equiv for y in self.later(x, "MOVE"))

    def unit_bears(self, x: int) -> bool:
        """Revisions 13-14: a scope change of the claim unit also ends bearing."""
        return self.exec_bears(x) and not self.later(x, "REPART")

    def exec_current(self, x: int) -> int:
        if self.later(x, "REPART"):  # currency follows the unit revision, which a scope change moves
            return F
        return min([T] + [self.base(m) if self.r[m].equiv else F for m in self.later(x, "MOVE")])

    def retired(self) -> bool:
        return any(self.kind(y) == "RETIRE" for y in range(self.n))

    def exec_rev(self, x: int) -> int:
        return sum(1 for y in range(x) if self.kind(y) == "MOVE")

    def compl_of(self, x: int) -> int | None:
        cs = [c for c in range(x) if self.kind(c) == "COMPL"]
        return cs[-1] if cs else None

    # ---- S1 polarity (strictly earlier targets) -----------------------------
    @memo
    def restrictive(self, a: int) -> bool:
        ra = self.r[a]
        return ra.kind == "ADJ" and ra.outcome == "UPHELD" and not self.counter(ra.target)

    @memo
    def counter(self, c: int) -> bool:
        rc = self.r[c]
        return rc.kind == "CHALLENGE" and not rc.on_real and self.restrictive(rc.target)

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
            self.r[a].target == b and self.in_force(a) and x in self.r[a].holds for a in self.later(b, "ATTEST")
        )

    @memo
    def cont(self, x: int) -> bool:
        return all(self.held(x, b) for b in self.later(x, "LOSS"))

    def gate(self, y: int) -> bool:
        return self.cont(y) if self.relaxer(y) else True

    def challenges_on(self, z: int, on_real: bool = False) -> list[int]:
        return [c for c in self.later(z, "CHALLENGE") if self.r[c].target == z and self.r[c].on_real == on_real]

    @memo
    def in_force(self, y: int) -> bool:
        assert self.kind(y) in ("ADJ", "WITHDRAW", "OVERRIDE", "ATTEST")
        if not self.gate(y):
            return False
        for c in self.challenges_on(y):
            if self.upheld(c) or (self.r[c].blocking and self.open(c) and not self.counter(c)):
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
            self.r[a].target == c and self.r[a].outcome == "UPHELD" and self.in_force(a) for a in self.later(c, "ADJ")
        )

    def overridden(self, c: int) -> bool:
        return self.open(c) and any(self.r[o].target == c and self.in_force(o) for o in self.later(c, "OVERRIDE"))

    @memo
    def status1(self, z: int, on_real: bool = False) -> str:  # positional args only (memo)
        chs = self.challenges_on(z, on_real)
        if any(self.upheld(c) for c in chs):
            return "REVOKED"
        live = [c for c in chs if self.r[c].blocking and self.open(c)]
        if any(not self.overridden(c) for c in live):
            return "BLOCKED"
        return "PROVISIONAL" if live else "CLEAR"

    def contested(self, d: int) -> bool:
        return any(self.r[c].blocking and self.open(c) for c in self.challenges_on(d))

    # ---- S2 (no cycles in the model, so direct evaluation is the LFP) -------
    @staticmethod
    def lvl(status: str) -> int:
        return F if status in ("REVOKED", "BLOCKED") else P if status == "PROVISIONAL" else T

    def base(self, z: int) -> int:
        if self.superseded(z) or not self.cont(z):
            return F
        return self.lvl(self.status1(z))

    @memo
    def current(self, z: int) -> int:
        b = self.base(z)
        k = self.kind(z)
        if k in ("COMPL", "MOVE"):
            return b
        if k == "IMMAT":
            return F if self.later(z, "GMOVE") else b
        assert k == "ASSESS"
        parts = [b, self.lvl(self.status1(z, True))]
        parts.append(self.exec_current(z))
        parts.append(F if self.later(z, "ORACLE") else T)
        parts.append(F if (self.r[z].reads and self.later(z, "CTX")) else T)
        c = self.compl_of(z)
        if c is not None:
            parts.append(self.current(c))
        return min(parts)

    def assessments(self, outcome: str) -> list[int]:
        return [i for i in range(self.n) if self.kind(i) == "ASSESS" and self.r[i].outcome == outcome]

    def upholdings(self, challenges: list[int]) -> list[int]:
        return [d for c in challenges for d in self.later(c, "ADJ") if self.r[d].target == c and self.r[d].outcome == "UPHELD"]

    def supersession_closure(self, x: int) -> list[int]:
        out, todo = [], list(self.superseders(x))
        while todo:
            y = todo.pop()
            out.append(y)
            todo += self.superseders(y)
        return out

    def immat_on(self, x: int) -> list[int]:
        return [d for d in self.later(x, "IMMAT") if self.r[d].target == x]

    # ---- revision 13 ---------------------------------------------------------
    def bears(self, a: int) -> bool:
        if MODE == "REV12":  # revision 12: every basis entry, context and interpretive ones included
            return (
                self.exec_bears(a)
                and not self.later(a, "ORACLE")
                and not (self.r[a].reads and self.later(a, "CTX"))
            )
        if MODE in ("REV13", "REV14"):
            return self.unit_bears(a)
        if MODE == "REV16":
            return self.exec_bears(a)  # revisions 15-16: lapse when evaluated content changes
        return True  # revision 17: no mechanical lapse

    def disposers(self, am: int) -> list[int]:
        out = self.supersession_closure(am) + self.upholdings(self.challenges_on(am))
        out += self.upholdings(self.challenges_on(am, on_real=True)) + self.immat_on(am)
        if MODE == "REV12":  # revision 12: an upheld challenge against any record premise disposes
            c = self.compl_of(am)
            if c is not None:
                out += self.upholdings(self.challenges_on(c))
        return out

    def eff(self, d: int) -> int:
        if self.kind(d) == "ASSESS" and not self.r[d].indep and MODE in ("REV14", "REV16", "REV17"):
            return F
        if self.kind(d) in ("ASSESS", "IMMAT"):
            return self.current(d)
        return T if (self.in_force(d) and self.cont(d) and not self.contested(d)) else F

    def undisputed(self) -> int:
        adverse = [a for a in self.assessments("FAIL") if self.bears(a)]
        return min([T] + [max([P] + [self.eff(d) for d in self.disposers(a)]) for a in adverse])

    # ---- revision 11 (sensitivity) -------------------------------------------
    def in_effect11(self, d: int) -> bool:
        if not self.cont(d):
            return False
        if self.kind(d) == "ADJ":
            return self.in_force(d)
        return (not self.superseded(d)) and self.status1(d) == "CLEAR"

    def disputed11(self, key: int) -> bool:
        ass = [i for i in range(self.n) if self.kind(i) == "ASSESS" and self.exec_rev(i) == key]
        has_pass = any(self.r[i].outcome == "PASS" for i in ass)

        def disposed(am: int) -> bool:
            direct = self.superseders(am) + self.upholdings(self.challenges_on(am)) + self.immat_on(am)
            return any(self.in_effect11(d) for d in direct)

        return has_pass and any(not disposed(i) for i in ass if self.r[i].outcome == "FAIL")

    # ---- revision 10 (sensitivity) -------------------------------------------
    def disputed10(self) -> bool:
        live = lambda i: (not self.superseded(i) and self.cont(i) and self.status1(i) not in ("BLOCKED", "REVOKED"))
        return bool(self.assessments("PASS")) and any(live(i) for i in self.assessments("FAIL"))

    # ---- the evidence term ---------------------------------------------------
    def ev(self) -> int:
        best = max([F] + [self.current(a) for a in self.assessments("PASS")])
        if MODE == "REV11":
            return max(
                [F]
                + [min(self.current(a), P if self.disputed11(self.exec_rev(a)) else T) for a in self.assessments("PASS")]
            )
        if MODE == "REV10":
            return min(best, P if self.disputed10() else T)
        return min(best, self.undisputed())

    def V(self) -> int:
        """The claim's evidence conjunct."""
        required = T if self.retired() else self.ev()
        if MODE in ("REV14", "REV16", "REV17"):
            return min(required, self.undisputed())
        return required


# ---- independent oracle: plain loops over the raw records ---------------------
def oracle_unqualified(L: Ledger) -> bool:
    recs, n = L.r, L.n

    def after(x, kind):
        return [y for y in range(x + 1, n) if recs[y].kind == kind]

    def standing_s1(x, on_real=False):
        """No upheld challenge and no open blocking challenge (overridden or not) on x."""
        for c in after(x, "CHALLENGE"):
            if recs[c].target == x and recs[c].on_real == on_real:
                if L.upheld(c) or (recs[c].blocking and L.open(c)):
                    return False
        return True

    def fully_current(x):
        rx = recs[x]
        if any(recs[y].supersedes == x for y in range(n)) or not L.cont(x) or not standing_s1(x):
            return False
        if rx.kind in ("COMPL", "MOVE"):
            return True
        if rx.kind == "IMMAT":
            return not after(x, "GMOVE")
        if not standing_s1(x, on_real=True):
            return False
        if any(not (recs[m].equiv and fully_current(m)) for m in after(x, "MOVE")) or after(x, "ORACLE") or after(x, "REPART"):
            return False
        if rx.reads and after(x, "CTX"):
            return False
        cs = [c for c in range(x) if recs[c].kind == "COMPL"]
        return fully_current(cs[-1]) if cs else True

    def descends_from(y, x):
        while recs[y].supersedes is not None:
            if recs[y].supersedes == x:
                return True
            y = recs[y].supersedes
        return False

    def settled(f):
        for y in range(f + 1, n):
            ry = recs[y]
            if ry.kind == "ASSESS" and ry.indep and descends_from(y, f) and fully_current(y):
                return True
            if ry.kind == "IMMAT" and ry.target == f and fully_current(y):
                return True
            if ry.kind == "ADJ" and ry.outcome == "UPHELD":
                c = recs[ry.target]
                if c.kind == "CHALLENGE" and c.target == f:  # the failing assessment or its realization
                    if L.in_force(y) and L.cont(y) and not any(
                        recs[k].target == y and recs[k].blocking and L.open(k) for k in after(y, "CHALLENGE")
                    ):
                        return True
        return False

    retired = any(r.kind == "RETIRE" for r in recs)
    if not retired and not any(
        fully_current(a) for a in range(n) if recs[a].kind == "ASSESS" and recs[a].outcome == "PASS"
    ):
        return False
    for f in range(n):
        if recs[f].kind == "ASSESS" and recs[f].outcome == "FAIL":
            if not settled(f):  # nothing but a disposition ends a failing assessment
                return False
    return True


def untouched_bearing_failure(L: Ledger) -> bool:
    """Q's premise: a failing assessment with nothing recorded against it."""
    for f in L.assessments("FAIL"):
        if L.superseded(f) or L.immat_on(f):
            continue
        if L.challenges_on(f) or L.challenges_on(f, on_real=True):
            continue
        return True
    return False


def candidates(prefix: tuple[R, ...]) -> list[R]:
    out = [
        R("ASSESS", outcome="PASS"),
        R("ASSESS", outcome="FAIL"),
        R("ASSESS", outcome="PASS", reads=True),
        R("ASSESS", outcome="FAIL", reads=True),
        R("LOSS"),
        R("MOVE", equiv=True),
        R("MOVE", equiv=False),
        R("ORACLE"),
        R("CTX"),
        R("GMOVE"),
        R("COMPL"),
        R("REPART"),
    ]
    if not any(r.kind == "RETIRE" for r in prefix):
        out.append(R("RETIRE"))
    for t, rt in enumerate(prefix):
        k = rt.kind
        if k in ("ASSESS", "ADJ", "OVERRIDE", "ATTEST", "IMMAT", "WITHDRAW", "COMPL") or (k == "MOVE" and rt.equiv):
            out += [R("CHALLENGE", target=t, blocking=True), R("CHALLENGE", target=t, blocking=False)]
        if k == "ASSESS":
            out.append(R("CHALLENGE", target=t, blocking=True, on_real=True))
            out.append(R("ASSESS", outcome="PASS", supersedes=t))
            out.append(R("ASSESS", outcome="PASS", supersedes=t, indep=False))
            if rt.outcome == "FAIL":
                out.append(R("IMMAT", target=t))
        if k == "CHALLENGE":
            out += [
                R("ADJ", target=t, outcome="UPHELD"),
                R("ADJ", target=t, outcome="DISMISSED"),
                R("WITHDRAW", target=t),
                R("OVERRIDE", target=t),
            ]
        if k == "LOSS":
            out.append(R("ATTEST", target=t, holds=frozenset(range(t))))
    return out


def revoked_any(L: Ledger) -> set:
    return {z for z in range(L.n) if L.kind(z) == "ASSESS" and L.status1(z) == "REVOKED"}


PASS_, FAIL_ = R("ASSESS", outcome="PASS"), R("ASSESS", outcome="FAIL")
FAIL_READS, PASS_READS = R("ASSESS", outcome="FAIL", reads=True), R("ASSESS", outcome="PASS", reads=True)
UPHOLD = lambda t: R("ADJ", target=t, outcome="UPHELD")
BCH = lambda t: R("CHALLENGE", target=t, blocking=True)
DISCRIMINATORS = [
    ("base: live pass and fail", (PASS_, FAIL_), P),
    ("97e753f A: equivalence move, passing rerun", (PASS_, FAIL_, R("MOVE", equiv=True), PASS_), P),
    ("97e753f A contrast (revision 17): non-equivalent move, passing rerun of another realization", (PASS_, FAIL_, R("MOVE", equiv=False), PASS_), P),
    ("configuration rerun passes and supersedes the failing assessment", (PASS_, FAIL_, R("MOVE", equiv=False), R("ASSESS", outcome="PASS", supersedes=1)), T),
    ("97e753f B1: IMMATERIALITY whose prerequisite moved", (PASS_, FAIL_, R("IMMAT", target=1), R("GMOVE")), P),
    ("97e753f B1 contrast: prerequisite unchanged", (PASS_, FAIL_, R("IMMAT", target=1)), T),
    ("97e753f B2: open blocking counter-challenge on the upholding", (PASS_, FAIL_, BCH(1), UPHOLD(2), BCH(3)), P),
    ("97e753f B2 contrast: counter-challenge dismissed",
     (PASS_, FAIL_, BCH(1), UPHOLD(2), BCH(3), R("ADJ", target=4, outcome="DISMISSED")), T),
    ("97e753f B2 contrast: non-blocking counter-challenge", (PASS_, FAIL_, BCH(1), UPHOLD(2),
                                                            R("CHALLENGE", target=3)), T),
    ("open challenge against the failing assessment", (PASS_, FAIL_, BCH(1)), P),
    ("loss with both assessments retained", (PASS_, FAIL_, R("LOSS"), PASS_), P),
    ("superseder chain disposes", (PASS_, FAIL_, R("ASSESS", outcome="PASS", supersedes=1),
                                   R("ASSESS", outcome="PASS", supersedes=2)), T),
    ("4c35d92 A1: unit read only by the failing assessor moves", (PASS_, FAIL_READS, R("CTX")), P),
    ("4c35d92 A1 contrast: unit read only by the passing assessor moves", (PASS_READS, FAIL_, R("CTX")), F),
    ("4c35d92 oracle move, passing realization reassessed first",
     (PASS_, FAIL_, R("ORACLE"), R("ASSESS", outcome="PASS", supersedes=0)), P),
    ("4c35d92 oracle move, failing realization then reassessed",
     (PASS_, FAIL_, R("ORACLE"), R("ASSESS", outcome="PASS", supersedes=0), R("ASSESS", outcome="PASS", supersedes=1)), T),
    ("4c35d92 A2: upheld challenge against a completeness premise",
     (R("COMPL"), PASS_, FAIL_, BCH(0), UPHOLD(3), R("COMPL"), PASS_), P),
    ("4c35d92 A2 contrast: upheld challenge against the failing realization",
     (PASS_, FAIL_, R("CHALLENGE", target=1, blocking=True, on_real=True), UPHOLD(2)), T),
    ("644eb72 B: obligation retired with a live disagreement", (PASS_, FAIL_, R("RETIRE")), P),
    ("644eb72 B contrast: disposition, then retirement", (PASS_, FAIL_, R("IMMAT", target=1), R("RETIRE")), T),
    ("644eb72 N3: non-independent superseder disposes of nothing",
     (PASS_, FAIL_, R("ASSESS", outcome="PASS", supersedes=1, indep=False)), P),
    ("62c0b24 A: boundary move of the claim unit, passing rerun", (PASS_, FAIL_, R("REPART"), PASS_), P),
    ("62c0b24 A contrast (revision 17): content edit, passing rerun of another realization", (PASS_, FAIL_, R("MOVE"), PASS_), P),
    ("challenged equivalence: failing evidence still bears, passing support provisional at most",
     (FAIL_, R("MOVE", equiv=True), PASS_, BCH(1)), P),
]


def run_discriminators() -> int:
    bad = 0
    for name, recs, want in DISCRIMINATORS:
        got = Ledger(recs).V()
        ok = got == want
        bad += 0 if ok else 1
        print(f"  [{'ok' if ok else 'DIFFERS'}] {name}: ev={'FPT'[got]} (revision 17 expects {'FPT'[want]})")
    return bad


def check(depth: int) -> int:
    seen = 0
    counts = dict.fromkeys(("P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "Q", "O"), 0)
    frontier = [()]
    for _ in range(depth):
        nxt = []
        for prefix in frontier:
            L0 = Ledger(prefix)
            e0, rv0 = L0.V(), revoked_any(L0)
            for rec in candidates(prefix):
                L1 = Ledger(prefix + (rec,))
                seen += 1
                e1 = L1.V()
                raised = e1 > e0
                if rec.kind == "CHALLENGE" and raised:
                    counts["P1"] += 1
                if rec.kind == "LOSS" and raised:
                    counts["P2"] += 1
                lost = rv0 - revoked_any(L1)
                if lost and rec.kind == "CHALLENGE" and L1.counter(L1.n - 1):
                    counts["P3"] += 1
                if lost and rec.kind == "LOSS":
                    counts["P4"] += 1
                if rec.kind in ("ORACLE", "CTX", "GMOVE") and raised:
                    counts["P5"] += 1
                if (rec.kind == "ADJ" and rec.outcome == "UPHELD" and prefix[rec.target].kind == "CHALLENGE"
                        and prefix[prefix[rec.target].target].kind == "COMPL" and raised):
                    counts["P6"] += 1
                if rec.kind == "REPART" and raised:
                    counts["P8"] += 1
                if rec.kind == "RETIRE" and e1 == T and untouched_bearing_failure(L0):
                    counts["P7"] += 1
                if untouched_bearing_failure(L1) and e1 == T:
                    counts["Q"] += 1
                if (e1 == T) != oracle_unqualified(L1):
                    counts["O"] += 1
                nxt.append(prefix + (rec,))
        frontier = nxt
    failures = sum(counts.values())
    print(f"mode {MODE}: checked {seen} appended-record transitions up to depth {depth}; failures: {failures} {counts}")
    return failures


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--depth", type=int, default=4)
    print(f"named discriminators (mode {MODE}):")
    d = run_discriminators()
    f = check(ap.parse_args().depth)
    raise SystemExit(1 if (f or d) else 0)
