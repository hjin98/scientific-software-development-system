"""Bounded model check of SSDS 8.0 workplan §6.6 S1 polarity and assessment
disagreement (design revision 20 and later).

This is a diagnostic transcription of the workplan's equations, not an SSDS
implementation and not an adequacy oracle (DS-001): it can show that the
written predicates contradict their own stated properties on small ledgers,
never that the design is right.

The model has one claim and one evidence obligation. Each ASSESS record is an
assessment of its own realization. Content is a pair: the content the
specification names (p, moved only forward by MOVE) and execution content
outside it (q, toggled by UMOVE, so a revert is representable). Premises move
by events:
  MOVE   named execution content moves, with or without an admitted
         equivalence judgment;
  UMOVE  execution content the specification does not name moves or is
         restored (a runtime parameter file, data read by path, a plugin);
  ORACLE the admitted oracle/specification reading moves (an interpretive
         premise); ORACLE with tight=True admits the never-admitted reading
         that the tight failing assessments applied;
  CTX    a context unit moves, read only by assessments with reads=True
         (provenance);
  GMOVE  the governing subject an IMMATERIALITY judgment relies on moves;
  COMPL  a completeness judgment; each assessment relies on the latest one
         before it (provenance, record mode);
  REPART the claim unit's scope changes with no content byte changed (a
         boundary move, merge or adopted governance-neutral delta): its unit
         revision changes, the evaluated content does not;
  RETIRE the evidence obligation stops being required (a specification
         change accepted on its own merits);
  EXEC   a designated-runner execution of a failing assessment's
         configuration, on that assessment's executed content (old=True), on
         the current admitted content, or on a candidate's content that differs
         from it only outside the named content (cand=True), with an evaluated
         outcome 0, 1 or 2 (1 is the default failing outcome; 0 and 2 are two
         different other outcomes);
  ADMIT  the obligation of the frame-only failing assessments (newobl=True)
         is admitted at some position, by any route.
An equivalence-covered MOVE is itself the equivalence judgment: it can be
challenged, and it supports currency only while it stands, but every MOVE,
covered or not, changes an evaluated premise (a cosmetic change is still a
change of content identity). A superseder may be non-independent of the
claim's author (indep=False); revision 19 refuses such a superseder at
Admission, as it refuses every unauthorized one.

Every assessment carries the evaluated outcome it read (obs; a failing
assessment of outcome 0 is an interpretive failure). A failing assessment may
have been made on a candidate whose executed content differs from the admitted
content only outside the named content (cand=True; ba7f738 U1a), or under a
reading (a tightened tolerance or a revised claim) that was never admitted, on
an otherwise admitted content with an unchanged outcome (tight=True; U2). A discriminating-pair
assessment (pair=True) is a passing assessment of its trial that names a
failing assessment in `supersedes` and carries the reproduction's outcome
(ro) and the trial's outcome (to); its two executions are admitted
observations whether or not its supersession is authorized. Pair
authorization is computed from the recorded observations, never asserted.
The model evaluates the admitted state only; candidate frames and their
lineages, and the mechanical/assessor-read split of decision classes, are
not modelled.

The checked value is V, the claim's evidence conjunct: ev while the
obligation is required, and in every case qual, the undisputed term over
every obligation an admitted failing assessment names (revision 14).

Revision 17 has no mechanical lapse: no move of any kind ends a failing
assessment; only a disposition does (a superseder, an upheld challenge, or
IMMATERIALITY). Revision 18 authorizes a superseder only as the failing
assessor's own reassessment (own=True) or with a discriminating pair, and
refuses any other superseder at Admission (the record is not admitted).
Revision 19 makes the pair discriminate in the observations (the trial's
outcome differs from the reproduction's, which equals the failing one, and
no admitted observation of the configuration on either content disagrees),
withdraws a pair that a later observation contradicts, lets a supersession
stand on its own record's standing instead of its basis currency (a pair,
in addition, only where an observation of its configuration on the
current content differs from the failing outcome and none reproduces it),
and
starts counting a frame-only failing assessment in the admitted state only
once its obligation is admitted.
Revision 20 decides every stop, standing and withdrawal on one content notion,
the assessed content: everything the execution read (here p and q together)
plus the reading the assessment applied. A pair may therefore be formed against
admitted content whenever a failure's assessed content differs from it, and a
failure under a never-admitted reading forms a reading pair whose trial is read
under the admitted reading; while the admitted reading is the one its trial was
read under, any observation on the current content shows another assessed
value. Revision 19 compared the named content only
(p), and is kept as REV19=1.

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
  P9  a superseder that is neither the failing assessor's own nor a pair
      never raises the evidence term;
  P10 a pair that does not discriminate in the observations (reproduction
      differs from the failing observation, trial outcome equals the
      reproduction's, no evaluated premise changed, or an admitted
      observation of the configuration on either content disagrees) never
      raises the evidence term;
  P11 a content move followed by an execution of the configuration on the
      new content with another outcome leaves the undisputed term where it
      was before the move, for a ledger with one failing assessment: a
      disagreement resolved by a pair is not presented as live again;
  P12 a failing assessment on an obligation that has never been admitted
      never lowers the evidence term of the admitted state;
  Q   a failing assessment that has no superseder, no challenge against it
      or its realization and no IMMATERIALITY judgment keeps the evidence term
      at most P, whatever moved (stated syntactically);
  P13 a pair that discriminates in the owner's sense on the assessed content
      (executed content and reading), appended to a ledger whose only failing
      assessment is its target, leaves the undisputed term T: discriminating
      evidence that a failure is not the admitted content's disposes of it;
  P14 an observation of a candidate's content that differs from every content
      a pair of its target compared never changes the evidence term of the
      admitted state;
  Q2  a failing assessment whose only dispositions are pairs, each
      contradicted by an admitted observation of the configuration, or whose
      failing outcome an execution on the current content reproduces under
      the same reading, keeps the evidence term at most P;
  O   the evidence term is T exactly when an oracle says the claim is
      unqualified. The oracle is written separately and does not call the
      bearing, disposer or effectiveness predicates it checks.

Named discriminators (the Reviews' trajectories and their contrasts) are
evaluated separately and printed.

Sensitivity: REV19=1 (stops, standing and withdrawal compared on the named
content only, no reading pair, un-named execution content outside passing
currency), REV18=1 (pair conditions as revision 18 wrote them, basis-
currency standing, counting from admission everywhere), REV17=1 (any
superseder), REV16=1 (content-based lapse, revisions 15-16), REV14=1,
REV13=1, REV12=1, REV11=1 and REV10=1 evaluate the earlier forms. Each must
report failures on at least one of P1-P14, Q or Q2, not only on O; a run
that stays green there means the check is blind.

Run: python3 qualification/ssds80/s1_disagreement_model_check.py [--depth N]
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass, field

F, P, T = 0, 1, 2
MODE = next((m for m in ("REV10", "REV11", "REV12", "REV13", "REV14", "REV16", "REV17", "REV18", "REV19")
             if os.environ.get(m)), "REV20")
LATE = ("REV14", "REV16", "REV17", "REV18", "REV19", "REV20")
STRICT = ("REV19", "REV20")  # independence is part of a supersession's authorization


def key(c: tuple[int, int]) -> tuple[int, ...]:
    """The content a mode compares: revision 20 the executed content, earlier modes the named content."""
    return c if MODE == "REV20" else (c[0],)


@dataclass(frozen=True)
class R:
    kind: str  # ASSESS CHALLENGE ADJ WITHDRAW OVERRIDE IMMAT LOSS ATTEST MOVE UMOVE ORACLE CTX GMOVE COMPL EXEC ADMIT
    target: int | None = None
    outcome: str | None = None  # PASS/FAIL for ASSESS; UPHELD/DISMISSED for ADJ; "0"/"1"/"2" for EXEC
    blocking: bool = False
    supersedes: int | None = None
    equiv: bool = False  # MOVE: covered by an admitted equivalence judgment
    reads: bool = False  # ASSESS: the assessor read the context unit
    on_real: bool = False  # CHALLENGE: targets the realization of ASSESS `target`
    holds: frozenset = field(default_factory=frozenset)  # ATTEST
    indep: bool = True  # superseder: independent of the claim's author
    own: bool = False  # superseder: the failing assessor's own reassessment
    obs: int | None = None  # ASSESS: evaluated outcome read (default 0 for PASS, 1 for FAIL)
    pair: bool = False  # ASSESS PASS: the trial assessment of a discriminating pair
    ro: int = 1  # pair: the reproduction's evaluated outcome
    to: int = 0  # pair: the trial's evaluated outcome
    old: bool = False  # EXEC: on the target failing assessment's content
    newobl: bool = False  # ASSESS FAIL: for an obligation that exists only in its frame
    cand: bool = False  # ASSESS FAIL, EXEC: on a candidate differing from admitted content outside the named content
    tight: bool = False  # ASSESS FAIL: under a never-admitted reading; ORACLE: that reading is admitted

    def ob(self) -> int:
        return self.obs if self.obs is not None else (0 if self.outcome == "PASS" else 1)


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
    def rev(self, i: int) -> int:
        """Revision of the named content at position i (every MOVE changes it)."""
        return sum(1 for y in range(i) if self.kind(y) == "MOVE")

    def content(self, i: int) -> tuple[int, int]:
        """Admitted executed content at position i: (named content, un-named execution content)."""
        return (self.rev(i), sum(1 for y in range(i) if self.kind(y) == "UMOVE") % 2)

    def xc(self, f: int) -> tuple[int, int]:
        """The content an assessment's execution read: a candidate's differs outside the named content."""
        p, q = self.content(f)
        return (p, 1 - q) if self.r[f].cand else (p, q)

    def reading(self, i: int):
        """The admitted reading at position i: the last ORACLE before i, or the tight one."""
        last = [y for y in range(i) if self.kind(y) == "ORACLE"]
        if last and self.r[last[-1]].tight:
            return "TIGHT"
        return last[-1] if last else -1

    def rd(self, f: int):
        """The reading a failing assessment applied."""
        return "TIGHT" if self.r[f].tight else self.reading(f)

    def reading_pair(self, y: int) -> bool:
        """Revision 20: the target's reading was never admitted before y, so y's trial is read under the
        admitted reading at y."""
        f = self.r[y].supersedes
        return MODE == "REV20" and self.r[f].tight and not any(
            self.kind(k) == "ORACLE" and self.r[k].tight for k in range(y)
        )

    def observations(self, f: int) -> list[tuple[int, tuple[int, int], int]]:
        """Admitted observations (position, executed content, outcome) of f's configuration."""
        out = []
        for i in range(f + 1, self.n):
            ri = self.r[i]
            if ri.kind == "EXEC" and ri.target == f:
                c = self.xc(f) if ri.old else ((self.rev(i), 1 - self.content(i)[1]) if ri.cand else self.content(i))
                out.append((i, c, int(ri.outcome)))
            if ri.kind == "ASSESS" and ri.pair and ri.supersedes == f:
                out += [(i, self.xc(f), ri.ro), (i, self.content(i), ri.to)]
        return out

    def contradicted(self, d: int, before: int | None) -> bool:
        """An observation other than d's own disagrees with d's pair (positions < before, or all)."""
        rd, f = self.r[d], self.r[d].supersedes
        old, trial = key(self.xc(f)), key(self.content(d))
        for i, c, o in self.observations(f):
            if i == d or (before is not None and i >= before):
                continue
            if key(c) == old and o != self.r[f].ob():
                return True
            if MODE != "REV18" and key(c) == trial and o != rd.to:
                return True
        return False

    @memo
    def authorized(self, y: int) -> bool:
        """Admission's step-3 check on y's supersedes field, over the prefix before y."""
        ry = self.r[y]
        if ry.supersedes is None or MODE not in ("REV18",) + STRICT:
            return True
        if MODE in STRICT and not ry.indep:  # revision 19: independence is part of the authorization
            return False
        if ry.own:
            return True
        if not ry.pair:
            return False
        f = ry.supersedes
        if self.kind(f) != "ASSESS" or self.r[f].outcome != "FAIL":
            return False
        if ry.ro != self.r[f].ob():
            return False
        if self.reading_pair(y):  # revision 20: the reading differs; the outcome need not
            pass
        elif key(self.xc(f)) == key(self.content(y)):  # no assessed content changed
            return False
        elif MODE in STRICT and ry.to == ry.ro:
            return False
        return not self.contradicted(y, y)

    def withdrawn(self, d: int) -> bool:
        """Revision 19: a later admitted observation contradicts the pair (monotone)."""
        return MODE in STRICT and self.r[d].pair and self.contradicted(d, None)

    def admitted(self, x: int) -> bool:
        """A refused record is not in the ledger: no rule reads it."""
        return self.r[x].kind != "ASSESS" or self.authorized(x)

    def superseders(self, x: int) -> list[int]:
        return [y for y in range(x + 1, self.n) if self.r[y].supersedes == x and self.r[y].kind == "ASSESS" and self.authorized(y)]

    def counted(self, f: int) -> bool:
        """Revision 19: a frame-only failing assessment counts here once its obligation is admitted."""
        if MODE not in STRICT or not self.r[f].newobl:
            return True
        return any(self.kind(y) == "ADMIT" for y in range(self.n))

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
        if MODE == "REV20" and self.content(x)[1] != self.content(self.n)[1]:
            return F  # revision 20: the execution basis is everything the execution read
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
        return [i for i in range(self.n) if self.kind(i) == "ASSESS" and self.r[i].outcome == outcome and self.admitted(i)]

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
        return True  # revisions 17-18: no mechanical lapse

    def disposers(self, am: int) -> list[int]:
        out = self.supersession_closure(am) + self.upholdings(self.challenges_on(am))
        out += self.upholdings(self.challenges_on(am, on_real=True)) + self.immat_on(am)
        if MODE == "REV12":  # revision 12: an upheld challenge against any record premise disposes
            c = self.compl_of(am)
            if c is not None:
                out += self.upholdings(self.challenges_on(c))
        return out

    def pair_here(self, d: int) -> bool:
        """Revision 19: on the current content, an admitted observation of the configuration has an
        outcome other than the failing one, and none has the failing one. Revision 20: compared on the
        executed content; for a reading pair, while the admitted reading is the one its trial was read
        under, every outcome is another assessed value."""
        f = self.r[d].supersedes
        cur, fo = key(self.content(self.n)), self.r[f].ob()
        outs = [o for _, c, o in self.observations(f) if key(c) == cur]
        if key(self.xc(f)) == cur:
            outs.append(fo)
        if self.reading_pair(d) and self.reading(self.n) == self.reading(d):
            return bool(outs)  # under the trial's reading, no outcome is the failing assessed value
        return bool(outs) and all(o != fo for o in outs)

    def chain_withdrawn(self, d: int, am: int) -> bool:
        """Some pair on the supersession chain from d down to am is withdrawn, or does not stand here."""
        y = d
        while y != am:
            if self.withdrawn(y) or (self.r[y].pair and not self.pair_here(y)):
                return True
            y = self.r[y].supersedes
        return False

    def eff(self, d: int, am: int) -> int:
        if self.kind(d) == "ASSESS" and not self.r[d].indep and MODE in LATE:
            return F
        if self.kind(d) == "ASSESS" and MODE in STRICT:
            # a supersession stands on its own record's standing, not its basis currency
            if self.chain_withdrawn(d, am):
                return F
            return min(self.base(d), self.lvl(self.status1(d, True)))
        if self.kind(d) in ("ASSESS", "IMMAT"):
            return self.current(d)
        return T if (self.in_force(d) and self.cont(d) and not self.contested(d)) else F

    def undisputed(self) -> int:
        adverse = [a for a in self.assessments("FAIL") if self.bears(a) and self.counted(a)]
        return min([T] + [max([P] + [self.eff(d, a) for d in self.disposers(a)]) for a in adverse])

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
        if MODE in LATE:
            return min(required, self.undisputed())
        return required


# ---- independent oracle: plain loops over the raw records ---------------------
def oracle_unqualified(L: Ledger) -> bool:
    recs, n = L.r, L.n
    rev20 = MODE == "REV20"
    rev19, rev18 = MODE in ("REV19", "REV20"), MODE == "REV18"

    def after(x, kind):
        return [y for y in range(x + 1, n) if recs[y].kind == kind]

    def named(i):
        return len([y for y in range(i) if recs[y].kind == "MOVE"])

    def unnamed(i):
        return len([y for y in range(i) if recs[y].kind == "UMOVE"]) % 2

    def revision(i):
        """What the mode compares as 'the same content' at admitted position i."""
        return (named(i), unnamed(i)) if rev20 else named(i)

    def executed(f):
        """The content the failing assessment f's execution read."""
        if not rev20:
            return named(f)
        return (named(f), 1 - unnamed(f)) if recs[f].cand else (named(f), unnamed(f))

    def reading_at(i):
        oracles = [y for y in range(i) if recs[y].kind == "ORACLE"]
        if not oracles:
            return -1
        return "TIGHT" if recs[oracles[-1]].tight else oracles[-1]

    def by_reading(y):
        """Revision 20: y's target applied a reading never admitted before y."""
        f = recs[y].supersedes
        return rev20 and recs[f].tight and not any(recs[k].kind == "ORACLE" and recs[k].tight for k in range(y))

    def outcome_of(x):
        r = recs[x]
        if r.obs is not None:
            return r.obs
        return 0 if r.outcome == "PASS" else 1

    def obs_list(f):
        """Every admitted observation of f's configuration: (position, content, outcome)."""
        res = []
        for i in range(n):
            r = recs[i]
            if r.kind == "EXEC" and r.target == f:
                if r.old:
                    c = executed(f)
                elif r.cand and rev20:
                    c = (named(i), 1 - unnamed(i))
                else:
                    c = revision(i)
                res.append((i, c, int(r.outcome)))
            elif r.kind == "ASSESS" and r.pair and r.supersedes == f:
                res.append((i, executed(f), r.ro))
                res.append((i, revision(i), r.to))
        return res

    def disagrees(y, upto):
        f = recs[y].supersedes
        for i, c, o in obs_list(f):
            if i == y or (upto is not None and i >= upto):
                continue
            if c == executed(f) and o != outcome_of(f):
                return True
            if not rev18 and c == revision(y) and o != recs[y].to:
                return True
        return False

    def auth(y):
        r = recs[y]
        if r.supersedes is None or not (rev18 or rev19):
            return True
        if rev19 and not r.indep:
            return False
        if r.own:
            return True
        if not r.pair:
            return False
        f = r.supersedes
        if recs[f].kind != "ASSESS" or recs[f].outcome != "FAIL":
            return False
        if r.ro != outcome_of(f):
            return False
        if not by_reading(y):
            if executed(f) == revision(y):
                return False
            if rev19 and r.to == r.ro:
                return False
        return not disagrees(y, y)

    def present(x):
        return recs[x].kind != "ASSESS" or auth(x)

    def standing_s1(x, on_real=False):
        """No upheld challenge and no open blocking challenge (overridden or not) on x."""
        for c in after(x, "CHALLENGE"):
            if recs[c].target == x and recs[c].on_real == on_real:
                if L.upheld(c) or (recs[c].blocking and L.open(c)):
                    return False
        return True

    def superseded_raw(x):
        return any(recs[y].supersedes == x and recs[y].kind == "ASSESS" and auth(y) for y in range(x + 1, n))

    def fully_current(x):
        rx = recs[x]
        if superseded_raw(x) or not L.cont(x) or not standing_s1(x):
            return False
        if rx.kind in ("COMPL", "MOVE"):
            return True
        if rx.kind == "IMMAT":
            return not after(x, "GMOVE")
        if not standing_s1(x, on_real=True):
            return False
        if any(not (recs[m].equiv and fully_current(m)) for m in after(x, "MOVE")) or after(x, "ORACLE") or after(x, "REPART"):
            return False
        if rev20 and unnamed(x) != unnamed(n):
            return False
        if rx.reads and after(x, "CTX"):
            return False
        cs = [c for c in range(x) if recs[c].kind == "COMPL"]
        return fully_current(cs[-1]) if cs else True

    def here(z):
        """An observation of the configuration on the current content differs from the failing
        outcome, and none equals it; under a reading pair's own admitted reading, any observed outcome."""
        f, cur = recs[z].supersedes, revision(n)
        outs = [o for _, c, o in obs_list(f) if c == cur]
        if executed(f) == cur:
            outs.append(outcome_of(f))
        if by_reading(z) and reading_at(n) == reading_at(z):
            return len(outs) > 0
        return len(outs) > 0 and outcome_of(f) not in outs

    def stands(y):
        """Revision 19: a supersession's own standing, read from S1 and S0 only."""
        return not superseded_raw(y) and L.cont(y) and standing_s1(y) and standing_s1(y, on_real=True)

    def chain_to(y, f):
        """The supersession chain from y down to f, or None."""
        path = [y]
        while recs[path[-1]].supersedes is not None and auth(path[-1]):
            nxt = recs[path[-1]].supersedes
            if nxt == f:
                return path
            path.append(nxt)
        return None

    def settled(f):
        for y in range(f + 1, n):
            ry = recs[y]
            if ry.kind == "ASSESS" and ry.indep and present(y):
                path = chain_to(y, f)
                if path is not None:
                    if rev19:
                        if stands(y) and not any(recs[z].pair and (disagrees(z, None) or not here(z)) for z in path):
                            return True
                    elif fully_current(y):
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

    def counts_here(f):
        if not rev19 or not recs[f].newobl:
            return True
        return any(r.kind == "ADMIT" for r in recs)

    retired = any(r.kind == "RETIRE" for r in recs)
    if not retired and not any(
        fully_current(a) for a in range(n) if recs[a].kind == "ASSESS" and recs[a].outcome == "PASS" and present(a)
    ):
        return False
    for f in range(n):
        if recs[f].kind == "ASSESS" and recs[f].outcome == "FAIL" and present(f) and counts_here(f):
            if not settled(f):  # nothing but a disposition ends a failing assessment
                return False
    return True


def untouched_bearing_failure(L: Ledger) -> bool:
    """Q's premise: a counted failing assessment with nothing recorded against it."""
    for f in L.assessments("FAIL"):
        if not L.counted(f):
            continue
        if L.superseded(f) or L.immat_on(f):
            continue
        if L.challenges_on(f) or L.challenges_on(f, on_real=True):
            continue
        return True
    return False


def only_contradicted_pairs(L: Ledger) -> bool:
    """Q2's premise: a failing assessment whose only dispositions are pairs, each contradicted or
    reproduced on the current content."""
    for f in L.assessments("FAIL"):
        if not L.counted(f):
            continue
        sups = L.superseders(f)
        if not sups or L.immat_on(f) or L.challenges_on(f) or L.challenges_on(f, on_real=True):
            continue
        if any(L.superseders(y) for y in sups):
            continue
        cur = key(L.content(L.n))
        unadmitted_reading = L.r[f].tight and L.reading(L.n) != "TIGHT"
        reproduced_here = not unadmitted_reading and any(
            r.kind == "EXEC" and r.target == f and not r.old and not r.cand and int(r.outcome) == L.r[f].ob()
            and key(L.content(i)) == cur
            for i, r in enumerate(L.r)
        )
        if all(L.r[y].pair and (L.contradicted(y, None) or reproduced_here) for y in sups):
            return True
    return False


def candidates(prefix: tuple[R, ...]) -> list[R]:
    out = [
        R("ASSESS", outcome="PASS"),
        R("ASSESS", outcome="FAIL"),
        R("ASSESS", outcome="FAIL", obs=0),
        R("ASSESS", outcome="FAIL", newobl=True),
        R("ASSESS", outcome="FAIL", cand=True),
        R("ASSESS", outcome="FAIL", tight=True),
        R("ASSESS", outcome="PASS", reads=True),
        R("ASSESS", outcome="FAIL", reads=True),
        R("LOSS"),
        R("MOVE", equiv=True),
        R("MOVE", equiv=False),
        R("UMOVE"),
        R("ORACLE"),
        R("CTX"),
        R("GMOVE"),
        R("COMPL"),
        R("REPART"),
    ]
    if not any(r.kind == "RETIRE" for r in prefix):
        out.append(R("RETIRE"))
    if not any(r.kind == "ADMIT" for r in prefix):
        out.append(R("ADMIT"))
    if not any(r.kind == "ORACLE" and r.tight for r in prefix):
        out.append(R("ORACLE", tight=True))
    for t, rt in enumerate(prefix):
        k = rt.kind
        if k in ("ASSESS", "ADJ", "OVERRIDE", "ATTEST", "IMMAT", "WITHDRAW", "COMPL") or (k == "MOVE" and rt.equiv):
            out += [R("CHALLENGE", target=t, blocking=True), R("CHALLENGE", target=t, blocking=False)]
        if k == "ASSESS":
            out.append(R("CHALLENGE", target=t, blocking=True, on_real=True))
            out.append(R("ASSESS", outcome="PASS", supersedes=t))
            out.append(R("ASSESS", outcome="PASS", supersedes=t, own=True))
            out.append(R("ASSESS", outcome="PASS", supersedes=t, own=True, indep=False))
            if rt.outcome == "FAIL":
                out.append(R("IMMAT", target=t))
                for o in (0, 1, 2):
                    out.append(R("EXEC", target=t, outcome=str(o)))
                    out.append(R("EXEC", target=t, outcome=str(o), cand=True))
                for o in (0, 1):
                    out.append(R("EXEC", target=t, outcome=str(o), old=True))
                    for o2 in (0, 1):
                        out.append(R("ASSESS", outcome="PASS", supersedes=t, pair=True, ro=o, to=o2))
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
FAIL_INTERP, FAIL_NEW = R("ASSESS", outcome="FAIL", obs=0), R("ASSESS", outcome="FAIL", newobl=True)
FAIL_CAND, FAIL_TIGHT = R("ASSESS", outcome="FAIL", cand=True), R("ASSESS", outcome="FAIL", tight=True)
UPHOLD = lambda t: R("ADJ", target=t, outcome="UPHELD")
BCH = lambda t: R("CHALLENGE", target=t, blocking=True)
OWN = lambda t: R("ASSESS", outcome="PASS", supersedes=t, own=True)
PAIR = lambda t, ro=1, to=0: R("ASSESS", outcome="PASS", supersedes=t, pair=True, ro=ro, to=to)
EXEC = lambda t, o, old=False, cand=False: R("EXEC", target=t, outcome=str(o), old=old, cand=cand)
MOVE, CMOVE, UMOVE = R("MOVE", equiv=False), R("MOVE", equiv=True), R("UMOVE")
ORACLE, ADMIT_TIGHT = R("ORACLE"), R("ORACLE", tight=True)
DISCRIMINATORS = [
    ("base: live pass and fail", (PASS_, FAIL_), P),
    ("97e753f A: equivalence move, passing rerun", (PASS_, FAIL_, CMOVE, PASS_), P),
    ("97e753f A contrast (revision 17): non-equivalent move, passing rerun of another realization", (PASS_, FAIL_, MOVE, PASS_), P),
    ("genuine fix: content move, pair whose outcome flips", (PASS_, FAIL_, MOVE, PAIR(1)), T),
    ("97e753f B1: IMMATERIALITY whose prerequisite moved", (PASS_, FAIL_, R("IMMAT", target=1), R("GMOVE")), P),
    ("97e753f B1 contrast: prerequisite unchanged", (PASS_, FAIL_, R("IMMAT", target=1)), T),
    ("97e753f B2: open blocking counter-challenge on the upholding", (PASS_, FAIL_, BCH(1), UPHOLD(2), BCH(3)), P),
    ("97e753f B2 contrast: counter-challenge dismissed",
     (PASS_, FAIL_, BCH(1), UPHOLD(2), BCH(3), R("ADJ", target=4, outcome="DISMISSED")), T),
    ("97e753f B2 contrast: non-blocking counter-challenge", (PASS_, FAIL_, BCH(1), UPHOLD(2),
                                                            R("CHALLENGE", target=3)), T),
    ("open challenge against the failing assessment", (PASS_, FAIL_, BCH(1)), P),
    ("loss with both assessments retained", (PASS_, FAIL_, R("LOSS"), PASS_), P),
    ("own-reassessment chain disposes", (PASS_, FAIL_, OWN(1), OWN(2)), T),
    ("4c35d92 A1: unit read only by the failing assessor moves", (PASS_, FAIL_READS, R("CTX")), P),
    ("4c35d92 A1 contrast: unit read only by the passing assessor moves", (PASS_READS, FAIL_, R("CTX")), F),
    ("4c35d92 oracle move, passing realization reassessed first", (PASS_, FAIL_, R("ORACLE"), OWN(0)), P),
    ("4c35d92 oracle move, failing realization then reassessed", (PASS_, FAIL_, R("ORACLE"), OWN(0), OWN(1)), T),
    ("4c35d92 A2: upheld challenge against a completeness premise",
     (R("COMPL"), PASS_, FAIL_, BCH(0), UPHOLD(3), R("COMPL"), PASS_), P),
    ("4c35d92 A2 contrast: upheld challenge against the failing realization",
     (PASS_, FAIL_, R("CHALLENGE", target=1, blocking=True, on_real=True), UPHOLD(2)), T),
    ("644eb72 B: obligation retired with a live disagreement", (PASS_, FAIL_, R("RETIRE")), P),
    ("644eb72 B contrast: disposition, then retirement", (PASS_, FAIL_, R("IMMAT", target=1), R("RETIRE")), T),
    ("644eb72 N3: non-independent superseder disposes of nothing",
     (PASS_, FAIL_, R("ASSESS", outcome="PASS", supersedes=1, own=True, indep=False)), P),
    ("62c0b24 A: boundary move of the claim unit, passing rerun", (PASS_, FAIL_, R("REPART"), PASS_), P),
    ("6fe1000 B1: unauthorized superseder is refused", (PASS_, FAIL_, MOVE, R("ASSESS", outcome="PASS", supersedes=1)), F),
    ("6fe1000 B1: pair on unchanged content", (PASS_, FAIL_, PAIR(1)), P),
    ("6fe1000 B1 contrast: the failing assessor's own reassessment", (PASS_, FAIL_, OWN(1)), T),
    ("6fe1000 B2: differing old-content execution before the pair", (PASS_, FAIL_, EXEC(1, 0, old=True), MOVE, PAIR(1)), F),
    ("4ec0024 B'1: interpretive failure, cosmetic change, identical trial outcome", (PASS_, FAIL_INTERP, CMOVE, PAIR(1, ro=0, to=0)), P),
    ("4ec0024 B'1 (deterministic failure form): trial outcome equals the reproduction's", (PASS_, FAIL_, CMOVE, PAIR(1, ro=1, to=1)), P),
    ("4ec0024 B'2: unassessed failing trial-content execution before the pair", (PASS_, FAIL_, MOVE, EXEC(1, 1), PAIR(1)), F),
    ("4ec0024 B'2: differing old-content execution after the pair withdraws it", (PASS_, FAIL_, MOVE, PAIR(1), EXEC(1, 0, old=True)), P),
    ("4ec0024 B'2: differing trial-content execution after the pair withdraws it", (PASS_, FAIL_, MOVE, PAIR(1), EXEC(1, 1)), P),
    ("4ec0024 B'2 contrast: agreeing executions on both contents", (PASS_, FAIL_, MOVE, EXEC(1, 1, old=True), EXEC(1, 0), PAIR(1)), T),
    ("4ec0024 C1: pair disposition, unrelated edit, passing rerun of the configuration", (PASS_, FAIL_, MOVE, PAIR(1), MOVE, EXEC(1, 0), PASS_), T),
    ("4ec0024 C1 contrast: the edit reintroduces the failing outcome, unassessed", (PASS_, FAIL_, MOVE, PAIR(1), MOVE, EXEC(1, 1), PASS_), P),
    ("4ec0024 C1 contrast: the edit reintroduces the failure, assessed", (PASS_, FAIL_, MOVE, PAIR(1), MOVE, PASS_, FAIL_), P),
    ("4ec0024 C1 contrast: no rerun of the configuration on the new content yet", (PASS_, FAIL_, MOVE, PAIR(1), MOVE, PASS_), P),
    ("4ec0024 C1 contrast: the pair's trial assessment is challenged", (PASS_, FAIL_, MOVE, PAIR(1), MOVE, EXEC(1, 0), PASS_, BCH(3)), P),
    ("4ec0024 C2a: failing assessment on an obligation never admitted", (PASS_, FAIL_NEW), T),
    ("4ec0024 C2a contrast: the obligation is later admitted", (PASS_, FAIL_NEW, R("ADMIT")), P),
    ("4ec0024 C2a contrast: admitted, then disposed by a pair", (PASS_, FAIL_NEW, R("ADMIT"), MOVE, PAIR(1), PASS_), T),
    ("challenged equivalence: failing evidence still bears, passing support provisional at most",
     (FAIL_, CMOVE, PASS_, BCH(1)), P),
    ("ba7f738 U1a: candidate failure from un-named execution content, pair against admitted content",
     (PASS_, FAIL_CAND, PAIR(1)), T),
    ("ba7f738 U1a contrast: no pair yet, the failure counts at once", (PASS_, FAIL_CAND), P),
    ("ba7f738 U1a contrast (6fe1000 A2 kept): admitted content reproduces the outcome",
     (PASS_, FAIL_CAND, PAIR(1, ro=1, to=1)), P),
    ("ba7f738 U1a contrast: the candidate's content is later absorbed", (PASS_, FAIL_CAND, PAIR(1), UMOVE, PASS_), P),
    ("ba7f738 U1: admitted failure fixed outside the named content, pair", (PASS_, FAIL_, UMOVE, PAIR(1), PASS_), T),
    ("ba7f738 U1 revert: the un-named fix is reverted", (PASS_, FAIL_, UMOVE, PAIR(1), PASS_, UMOVE, PASS_), P),
    ("ba7f738 U1b: a candidate's run on un-named-different content does not withdraw a pair",
     (PASS_, FAIL_, MOVE, PAIR(1), EXEC(1, 1, cand=True)), T),
    ("ba7f738 U1b, passing other outcome", (PASS_, FAIL_, MOVE, PAIR(1), EXEC(1, 2, cand=True)), T),
    ("ba7f738 U1b contrast: another outcome on the trial's own executed content withdraws",
     (PASS_, FAIL_, MOVE, PAIR(1), EXEC(1, 2)), P),
    ("ba7f738 U1: un-named change after a pair, configuration not yet rerun", (PASS_, FAIL_, MOVE, PAIR(1), UMOVE, PASS_), P),
    ("ba7f738 U1: un-named change after a pair, rerun with a third outcome",
     (PASS_, FAIL_, MOVE, PAIR(1), UMOVE, EXEC(1, 2), PASS_), T),
    ("ba7f738 U2: failure under a never-admitted reading, reading pair against admitted content",
     (PASS_, FAIL_TIGHT, PAIR(1, ro=1, to=1)), T),
    ("ba7f738 U2 contrast: no pair yet, the failure counts at once", (PASS_, FAIL_TIGHT), P),
    ("ba7f738 U2: reading pair, then an execution-basis change before the configuration reruns",
     (PASS_, FAIL_TIGHT, PAIR(1, ro=1, to=1), UMOVE, PASS_), P),
    ("ba7f738 U2: reading pair, execution-basis change, rerun with the same outcome",
     (PASS_, FAIL_TIGHT, PAIR(1, ro=1, to=1), UMOVE, EXEC(1, 1), PASS_), T),
    ("ba7f738 U2 contrast: the tightened reading is later admitted", (PASS_, FAIL_TIGHT, PAIR(1, ro=1, to=1), ADMIT_TIGHT, PASS_), P),
    ("ba7f738 U2 contrast: admitted after the pair, then fixed with an outcome flip",
     (PASS_, FAIL_TIGHT, PAIR(1, ro=1, to=1), ADMIT_TIGHT, MOVE, PAIR(1, ro=1, to=0), PASS_), T),
    ("ba7f738 U2: another admitted reading change brings it back", (PASS_, FAIL_TIGHT, PAIR(1, ro=1, to=1), ORACLE, PASS_), P),
    ("ba7f738 U2: re-paired under the new admitted reading",
     (PASS_, FAIL_TIGHT, PAIR(1, ro=1, to=1), ORACLE, PAIR(1, ro=1, to=1), PASS_), T),
    ("ba7f738 U2 contrast (4ec0024 B'1 kept): an admitted-reading failure with an identical outcome",
     (PASS_, FAIL_, ORACLE, PAIR(1, ro=1, to=1), PASS_), P),
]


def run_discriminators() -> int:
    bad = 0
    for name, recs, want in DISCRIMINATORS:
        got = Ledger(recs).V()
        ok = got == want
        bad += 0 if ok else 1
        print(f"  [{'ok' if ok else 'DIFFERS'}] {name}: ev={'FPT'[got]} (revision 20 expects {'FPT'[want]})")
    return bad


def discriminates(L: Ledger, y: int) -> bool:
    """The owner's sense, stated plainly on the assessed content (everything the execution read, and
    the reading applied): the failure reproduces identically on the content it evaluated; on changed
    executed content the trial's outcome differs, or the failure applied a reading never admitted and
    the trial passes under the admitted one; and no admitted observation of the configuration on
    either content disagrees, at any position."""
    ry, recs = L.r[y], L.r
    f = ry.supersedes
    if recs[f].kind != "ASSESS" or recs[f].outcome != "FAIL":
        return False
    moves = lambda i: len([k for k in range(i) if recs[k].kind == "MOVE"])
    flips = lambda i: len([k for k in range(i) if recs[k].kind == "UMOVE"]) % 2
    here = lambda i: (moves(i), flips(i))
    old = (moves(f), 1 - flips(f)) if recs[f].cand else here(f)
    fo = recs[f].obs if recs[f].obs is not None else 1
    unadmitted = recs[f].tight and not any(recs[k].kind == "ORACLE" and recs[k].tight for k in range(y))
    if ry.ro != fo:
        return False
    if not unadmitted and (ry.to == ry.ro or old == here(y)):
        return False
    for i in range(L.n):
        r = recs[i]
        if i == y:
            continue
        seen = []
        if r.kind == "EXEC" and r.target == f:
            c = old if r.old else ((moves(i), 1 - flips(i)) if r.cand else here(i))
            seen.append((c, int(r.outcome)))
        if r.kind == "ASSESS" and r.pair and r.supersedes == f:
            seen += [(old, r.ro), (here(i), r.to)]
        for c, o in seen:
            if (c == old and o != fo) or (c == here(y) and o != ry.to):
                return False
    return True


def sole_target_clear(L: Ledger, y: int) -> bool:
    """P13's premise: y's target is the only failing assessment, and nothing but y stands against or
    for it; y has just been appended."""
    f = L.r[y].supersedes
    if L.assessments("FAIL") != [f] or not L.counted(f):
        return False
    if L.immat_on(f) or L.challenges_on(f) or L.challenges_on(f, on_real=True):
        return False
    return L.r[y].indep and not any(L.kind(k) == "LOSS" for k in range(L.n))


def inert_candidate_run(L: Ledger, i: int) -> bool:
    """P14's premise: i is a candidate-content observation whose executed content differs from every
    content a pair of its target compared."""
    r = L.r[i]
    if r.kind != "EXEC" or not r.cand:
        return False
    f, recs = r.target, L.r
    moves = lambda k: len([j for j in range(k) if recs[j].kind == "MOVE"])
    flips = lambda k: len([j for j in range(k) if recs[j].kind == "UMOVE"]) % 2
    c = (moves(i), 1 - flips(i))
    old = (moves(f), 1 - flips(f)) if recs[f].cand else (moves(f), flips(f))
    trials = [(moves(k), flips(k)) for k in range(L.n) if recs[k].kind == "ASSESS" and recs[k].pair and recs[k].supersedes == f]
    return c != old and c not in trials


def check(depth: int) -> int:
    seen = 0
    counts = dict.fromkeys(
        ("P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12", "P13", "P14", "Q", "Q2", "O"), 0
    )
    frontier = [()]
    for level in range(depth):
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
                if rec.kind == "ASSESS" and rec.supersedes is not None and not rec.own and not rec.pair and raised:
                    counts["P9"] += 1
                if rec.kind == "ASSESS" and rec.pair and raised and not discriminates(L1, L1.n - 1):
                    counts["P10"] += 1
                if (rec.kind == "EXEC" and not rec.old and not rec.cand and prefix and prefix[-1].kind == "MOVE"
                        and int(rec.outcome) != L1.r[rec.target].ob() and len(L1.assessments("FAIL")) == 1
                        and L1.undisputed() < Ledger(prefix[:-1]).undisputed()):
                    counts["P11"] += 1
                if (rec.kind == "ASSESS" and rec.newobl and e1 < e0
                        and not any(r.kind == "ADMIT" for r in prefix)):
                    counts["P12"] += 1
                if (rec.kind == "ASSESS" and rec.pair and discriminates(L1, L1.n - 1)
                        and sole_target_clear(L1, L1.n - 1) and L1.undisputed() != T):
                    counts["P13"] += 1
                if rec.kind == "EXEC" and inert_candidate_run(L1, L1.n - 1) and e1 != e0:
                    counts["P14"] += 1
                if rec.kind == "REPART" and raised:
                    counts["P8"] += 1
                if rec.kind == "RETIRE" and e1 == T and untouched_bearing_failure(L0):
                    counts["P7"] += 1
                if untouched_bearing_failure(L1) and e1 == T:
                    counts["Q"] += 1
                if only_contradicted_pairs(L1) and e1 == T:
                    counts["Q2"] += 1
                if (e1 == T) != oracle_unqualified(L1):
                    counts["O"] += 1
                if level < depth - 1:  # the last level's ledgers are checked, never extended
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
