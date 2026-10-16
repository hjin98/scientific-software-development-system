"""Bounded model check of the SSDS 8 Architecture Manual §5.10 judgment-disagreement layer.

Companion to s1_disagreement_model_check.py (which models workplan §6.6 assessment
disagreement). This is a diagnostic transcription of the Manual's written rules, not an
SSDS implementation and not an adequacy oracle (DS-001): it can show that the written
§5.10 predicates contradict the invariants §5.10 (g) states, on small ledgers; it can
never show that the design is right or that a production owner behaves this way.

What is modelled (one subject, one gate, one plan item):
  kinds    REV   a transformation REVIEW: target (item revision, changed content, base);
                 reach = same changed content at any item revision and base;
                 supersession on the exact target; per-target relief (route 3).
           ACC   an ACCEPTANCE: target = subject revision; reach = same revision;
                 supersession on the exact target.
           GATE  a GATE_DECISION: target = (revision, run); reach and supersession
                 target = same revision in any run; no independence requirement;
                 passing decisions aggregate by minimum over the current run.
  actors   A  the content's author (human, R3)       H  an independent human (R3)
           O  the owner (human, R3, independent)      P  an attested-fresh agent (R2)
           U  an agent with UNKNOWN lineage (R2; never independent)
           Q  an owner execution with UNKNOWN lineage (R2; never independent)
           EQ    an EQUIVALENCE (second family, check_eq): target = (r_from, r_to, class) on one
                 unit with revisions r0..r3, cur(u) = r3; classes K, K2 (consumers) and ED
                 (editorial, covering both); reach = every passing judgment on a chain joining
                 the objection's two revisions, read in either direction, every hop covering
                 its class, the other hops asserting (R14); supersession on the exact target.
           PLAN  a PLAN_ACCEPTANCE (third family, check_plan): one item, revisions i0 ⊑ i1 ⊑ i2
                 by the tightening order and an incomparable i1x; reach = every passing
                 acceptance naming or covering the rejected revision (R14); supersession on
                 the exact target only while that revision is current.
  frames   adm (admitted frame), pend (a pending enactment's frame), aband (abandoned)
  states   D (the admitted state) and F (the pending enactment's frame)
  records  judgments (pass/adverse, optional supersedes), blocking challenges with a
           raiser, adjudications (UPHELD/DISMISSED) of a challenge, counter-challenges
           of an upholding, and a challenge of a dismissal.

Invariants (Manual §5.10 (g)), each checked against an oracle written from the
protected properties rather than from the §5.10 formulas. The oracle reuses the model's
helpers for acting, supersession, S1 status (in_force, contested) and the independence
test, so a mistake in one of those can agree on both sides; it is independent only in how
it combines them (and, for EQ, in enumerating vertex sequences instead of searching edges):
  I1/I3  base(z) equals the oracle in both directions: a passing judgment supports iff it
         acts, is independent, is not withdrawn, and every objection reaching it was ended
         by an independent author/owner record that judged the objection's own target
         (withdrawing it), or, for a transformation review, z's exact target (relief), or by
         an eligible upheld challenge.
  I2     records with nonind and inadmissible adjudications change no support value (base, sat,
         issuability, gterm); a non-independent contrary pass still derives the owner's obligation.
  I4     every veto can be lifted by an admissible record in the state where it bites.
  I5     passing and superseding records of pending/abandoned frames change nothing in D.
  I6     the admitted set (and, for EQ, the admitted state's outputs) is the same under two
         sampled reference-respecting permutations per case; not every order is tried.
  I7     no admitted adjudication is below its chain's class or dependent on authors(root).
  I8     (EQ) the owner's adjudication obligation is derived exactly when a standing objection
         contradicts a passing judgment acting in the state, directly or through a chain.

Not modelled: evidence assessments, completeness, plan acceptance, intake, product scope,
qualified or provisional values, integration and rebase transitions, loss boundaries,
before-image bases, changing authorship, full Admission, and more than one resolving record.
A green run says nothing about those.

Sensitivity: --mutations re-introduces earlier defects one at a time; each must be caught
by at least one invariant, or the check reports the model insensitive to it.

Usage:  python3 judgment_disagreement_model_check.py [--mutations]
Exit status 0 when the unmutated rules hold every invariant and (with --mutations)
every mutation is caught; 1 otherwise.
"""
from __future__ import annotations

import argparse
import itertools
import random
import sys
from dataclasses import dataclass, field

ACTORS = {
    #  name: (human, attested_fresh, owner, class)
    "A": (True, True, False, 3),
    "H": (True, True, False, 3),
    "O": (True, True, True, 3),
    "P": (False, True, False, 2),
    "U": (False, False, False, 2),
    "Q": (False, False, True, 2),
}
AUTHORS = frozenset({"A"})  # authors(x) of every modelled content

MUT: set[str] = set()


@dataclass(frozen=True)
class J:  # judgment
    id: str
    kind: str          # REV | ACC | GATE
    target: tuple      # REV: (item, content, base); ACC: (rev,); GATE: (rev, run)
    adverse: bool
    actor: str
    frame: str = "adm"  # adm | pend | aband
    supersedes: tuple = ()


@dataclass(frozen=True)
class C:  # blocking challenge
    id: str
    target: str        # record id (judgment or adjudication)
    raiser: str


@dataclass(frozen=True)
class Adj:
    id: str
    challenge: str
    upheld: bool
    actor: str


def independent(actor: str, authors=AUTHORS) -> bool:
    human, fresh, _owner, _cls = ACTORS[actor]
    if actor in authors:
        return False
    return human or fresh


def requirement(kind: str) -> bool:
    return kind in ("REV", "ACC", "EQ", "PLAN")  # EQ: every modelled equivalence is about the change


# ---- plan items (§11.2, §13.4): i0 ⊑ i1 ⊑ i2; i1x (a prose change of i0) is comparable with nothing
TIGHT = {("i0", "i1"), ("i1", "i2"), ("i0", "i2")}
PLAN_CUR = ["i2"]  # the item's current revision in the scenario being evaluated


def tight(r: str, r2: str) -> bool:
    return r == r2 or (r, r2) in TIGHT


def reach(j: J, z: J) -> bool:
    if j.kind != z.kind:
        return False
    if j.kind == "PLAN":
        if "plan_reach_names_only" in MUT:  # the a6ed164 rule: revisions both name
            return z.target == j.target
        return tight(z.target[0], j.target[0])  # z names or covers the rejected revision
    if j.kind == "REV":
        return j.target[1] == z.target[1]
    if j.kind == "ACC":
        return j.target == z.target
    if "gate_run_veto" in MUT:  # 362af9f B1-A: veto keyed on the run-parameterized obligation
        return j.target == z.target
    return j.target[0] == z.target[0]


def supersession_target_ok(r: J, x: J) -> bool:
    if r.kind != x.kind:
        return False
    if r.kind == "REV":
        if "wide_review_supersession" in MUT:  # 051cce3 B1: same changed content, any item/base
            return r.target[1] == x.target[1]
        return r.target == x.target
    if r.kind in ("ACC", "EQ"):
        return r.target == x.target  # EQ: the exact (endpoints, class) target
    if r.kind == "PLAN":  # the target, only while the rejected revision is current
        return r.target == x.target and PLAN_CUR[0] == x.target[0]
    return r.target[0] == x.target[0]  # GATE: same revision, any run


class Ledger:
    def __init__(self, order: list):
        self.adm: dict[str, object] = {}
        for rec in order:
            if self._admit(rec):
                self.adm[rec.id] = rec
        self.js = [r for r in self.adm.values() if isinstance(r, J)]
        self.cs = [r for r in self.adm.values() if isinstance(r, C)]
        self.ads = [r for r in self.adm.values() if isinstance(r, Adj)]

    # ---- Admission (§5.10 (e), §8.3 step 3)
    def _root_and_class(self, adj: Adj):
        cls = ACTORS[adj.actor][3]
        chain_cls = 0
        c = self.adm.get(adj.challenge)
        if c is None:
            return None, None
        t = self.adm.get(c.target)
        depth = 0
        while isinstance(t, Adj):
            chain_cls = max(chain_cls, ACTORS[t.actor][3])
            c2 = self.adm.get(t.challenge)
            if "challenged_record_authors" in MUT and depth == 0:  # 6b986de B1(b)
                return ("raiser", c2.raiser), chain_cls
            t = self.adm.get(c2.target)
            depth += 1
        if isinstance(t, J):
            chain_cls = max(chain_cls, ACTORS[t.actor][3])
        return t, chain_cls

    def _admit(self, rec) -> bool:
        if isinstance(rec, C):
            return rec.target in self.adm
        if isinstance(rec, Adj):
            if rec.challenge not in self.adm:
                return False
            root, chain_cls = self._root_and_class(rec)
            if root is None:
                return False
            c = self.adm[rec.challenge]
            direct = isinstance(self.adm.get(c.target), J)
            if "eligibility_support_tier_only" in MUT and not direct:  # 29da56e B1
                return True
            if isinstance(root, tuple):  # mutated reference set: the raiser
                authors = frozenset({root[1]})
            else:
                authors = AUTHORS
            if not independent(rec.actor, authors):
                return False
            if "no_class_check" not in MUT and ACTORS[rec.actor][3] < chain_cls:
                return False
            return True
        # judgment
        for xid in rec.supersedes:
            x = self.adm.get(xid)
            if not isinstance(x, J) or not supersession_target_ok(rec, x):
                return False
            if not (rec.actor == x.actor or ACTORS[rec.actor][2]):
                return False
            if requirement(rec.kind) and not independent(rec.actor):
                return False
        return True

    # ---- S0
    def nonind(self, z: J) -> bool:
        return requirement(z.kind) and not independent(z.actor)

    def acts(self, r: J, G: str) -> bool:
        if r.frame == "adm":
            return True
        if r.frame == "pend":
            return G == "F" or "frame_acts_everywhere" in MUT  # b46c250 B1
        return "frame_acts_everywhere" in MUT

    def superseded(self, x: J, G: str) -> bool:
        return any(x.id in r.supersedes and self.acts(r, G) for r in self.js)

    # ---- S1 (§5.3), blocking challenges only
    def is_counter(self, c: C) -> bool:
        t = self.adm.get(c.target)
        return isinstance(t, Adj) and t.upheld

    def in_force(self, a: Adj, seen=()) -> bool:
        if a.id in seen:
            return False
        for c in self.cs:
            if c.target == a.id:
                if self.upheld(c, seen + (a.id,)):
                    return False
                if not self.is_counter(c) and self.open(c, seen + (a.id,)):
                    return False
        return True

    def open(self, c: C, seen=()) -> bool:
        return not any(a.challenge == c.id and self.in_force(a, seen) for a in self.ads)

    def upheld(self, c: C, seen=()) -> bool:
        return any(a.challenge == c.id and a.upheld and self.in_force(a, seen) for a in self.ads)

    def status1(self, rid: str) -> str:
        cs = [c for c in self.cs if c.target == rid]
        if any(self.upheld(c) for c in cs):
            return "REVOKED"
        if any(self.open(c) for c in cs):
            return "BLOCKED"
        return "CLEAR"

    def contested(self, a: Adj) -> bool:
        return any(c.target == a.id and self.open(c) for c in self.cs)

    # ---- §5.10 (e)
    def stands(self, j: J, G: str) -> bool:
        def chain(x: J, seen):
            for d in self.js:
                if x.id in d.supersedes and d.id not in seen and self.acts(d, G):
                    last_ok = (not self.superseded(d, G) and self.status1(d.id) == "CLEAR"
                               and not self.nonind(d))
                    if last_ok or chain(d, seen | {d.id}):
                        return True
            return False
        if chain(j, {j.id}):
            return False
        for c in self.cs:
            if c.target == j.id:
                for a in self.ads:
                    if a.challenge == c.id and a.upheld and self.in_force(a) and not self.contested(a):
                        return False
        return True

    def relieved(self, j: J, z: J, G: str) -> bool:
        if j.kind != "REV":
            return False
        for y in self.js:
            if (not y.adverse and y.kind == "REV" and y.target == z.target
                    and (y.actor == j.actor or ACTORS[y.actor][2]) and self.acts(y, G)
                    and not self.superseded(y, G) and self.status1(y.id) == "CLEAR"
                    and ("relief_ignores_nonind" in MUT or not self.nonind(y))):  # 9e5a763 B1
                return True
        return False

    def reaches(self, j: J, z: J, G: str) -> bool:
        if j.kind == "EQ" and z.kind == "EQ":
            return self.eq_reach(j, z, G)
        return reach(j, z)

    def vetoed(self, z: J, G: str) -> bool:
        if z.adverse:
            return False
        return any(j.adverse and self.reaches(j, z, G) and self.stands(j, G) and not self.relieved(j, z, G)
                   for j in self.js)

    # ---- §5.10 (a) equivalence chains (R14)
    def asserts(self, q: J, G: str) -> bool:
        return (q.kind == "EQ" and not q.adverse and self.acts(q, G) and not self.superseded(q, G)
                and self.status1(q.id) == "CLEAR" and not self.nonind(q))

    def eq_reach(self, j: J, z: J, G: str) -> bool:
        """z lies on a chain joining j's two revisions whose other hops assert, every hop covering j's class."""
        a, b, c = j.target
        if "endpoint_only_equivalence_reach" in MUT:  # a6ed164 B1: the same endpoints only
            return z.target[:2] == (a, b) and covers(z.target[2], c)
        ignore_class = "chain_ignores_class" in MUT
        if not ignore_class and not covers(z.target[2], c):
            return False
        edges = [(z.target[0], z.target[1], True)] + [
            (q.target[0], q.target[1], False) for q in self.js
            if q is not z and self.asserts(q, G) and (ignore_class or covers(q.target[2], c))]
        directed = "directed_chain_only" in MUT  # a path reading: hops only in their recorded direction

        def walk(v, goal, seen, used):
            if v == goal:
                return used
            for x, y, isz in edges:
                for s_, t_ in (((x, y),) if directed else ((x, y), (y, x))):
                    if s_ == v and t_ not in seen and walk(t_, goal, seen | {t_}, used or isz):
                        return True
            return False
        return walk(a, b, {a}, False) or (directed and walk(b, a, {b}, False))

    def adjudicate(self, j: J, G: str) -> bool:
        """§5.10 (f): a standing adverse judgment that vetoes a passing judgment acting in G."""
        if not j.adverse or not self.stands(j, G):
            return False
        for z in self.js:
            if z.adverse or z.kind != j.kind or not self.acts(z, G):
                continue
            if "obligation_direct_only" in MUT and set(z.target[:2]) != set(j.target[:2]):
                continue
            if self.reaches(j, z, G) and not self.relieved(j, z, G):
                return True
        return False

    def sat(self, r: str, k: str, G: str) -> bool:
        """§4.4: an equivalence path of supporting hops from r to cur(u) covering class k."""
        if r == CUR:
            return True
        hops = [q for q in self.js if q.kind == "EQ" and not q.adverse and covers(q.target[2], k)
                and self.base(q, G)]

        def walk(v, seen):
            if v == CUR:
                return True
            return any(q.target[0] == v and q.target[1] not in seen and walk(q.target[1], seen | {q.target[1]})
                       for q in hops)
        return walk(r, {r})

    def base(self, z: J, G: str) -> bool:
        if not self.acts(z, G) or self.superseded(z, G):
            return False
        if self.status1(z.id) in ("REVOKED", "BLOCKED"):
            return False
        if self.vetoed(z, G):
            return False
        if "base_ignores_nonind" not in MUT and self.nonind(z):  # 29da56e B1(g)
            return False
        return True

    # ---- outputs
    def outputs(self, G: str, run_cur: str) -> tuple:
        out = []
        for z in sorted(self.js, key=lambda r: r.id):
            if not z.adverse:
                out.append((z.id, self.base(z, G)))
        elig = [z for z in self.js if z.kind == "GATE" and not z.adverse and self.acts(z, G)
                and not self.superseded(z, G) and z.target == ("r1", run_cur)]
        gterm = bool(elig) and all(self.base(z, G) for z in elig)
        out.append(("gterm", gterm))
        return tuple(out)


# ---- equivalence classes (§4.4)
REVS = ("r0", "r1", "r2", "r3")
CUR = "r3"


def covers(c: str, k: str) -> bool:
    return k not in ("EXACT", "PLAN_CONTROL") and (c == k or c in ("ED", "REP"))


# ---- oracle (written from the protected properties, not from §5.10's formulas)
def oracle_base(L: Ledger, z: J, G: str) -> bool:
    if z.adverse or not L.acts(z, G) or L.superseded(z, G):
        return False
    if L.status1(z.id) != "CLEAR":
        return False
    if requirement(z.kind) and not independent(z.actor):
        return False
    for j in L.js:
        if not j.adverse or j.kind != z.kind:
            continue
        if j.kind == "EQ":
            same = oracle_joins(L, j, z, G)
        elif j.kind == "PLAN":
            # z's conclusion holds for every revision its order covers; a rejection of one contradicts it
            same = j.target[0] in {r for r in ("i0", "i1", "i2", "i1x") if tight(z.target[0], r)}
        else:
            same = (j.target[1] == z.target[1]) if j.kind == "REV" else (
                j.target == z.target if j.kind == "ACC" else j.target[0] == z.target[0])
        if not same:
            continue
        if not oracle_resolved(L, j, z, G):
            return False
    return True


def oracle_resolved(L: Ledger, j: J, z: J, G: str) -> bool:
    def eligible_resolver(y: J) -> bool:
        return (not y.adverse and L.acts(y, G) and not L.superseded(y, G)
                and L.status1(y.id) == "CLEAR"
                and (y.actor == j.actor or ACTORS[y.actor][2])
                and (not requirement(y.kind) or independent(y.actor)))
    for y in L.js:
        if not eligible_resolver(y):
            continue
        if j.kind == "REV" and y.target == z.target:
            return True  # route 3: the author's or owner's pass of z's exact target
        if j.id in y.supersedes and j.kind == "REV" and y.target == j.target:
            return True  # routes 1-2: withdrawal by judging the objection's own target
        if j.id in y.supersedes and j.kind in ("ACC", "EQ") and y.target == j.target:
            return True
        if j.id in y.supersedes and j.kind == "PLAN" and y.target == j.target:
            return True  # admitted only while j's revision was current
        if j.id in y.supersedes and j.kind == "GATE" and y.target[0] == j.target[0]:
            return True
    # route 4: an eligible upheld challenge, in force and uncontested
    for c in L.cs:
        if c.target != j.id:
            continue
        for a in L.ads:
            if a.challenge == c.id and a.upheld and L.in_force(a) and not L.contested(a):
                if independent(a.actor) and ACTORS[a.actor][3] >= ACTORS[j.actor][3]:
                    return True
    return False


def oracle_asserts(L: Ledger, q: J, G: str) -> bool:
    return (q.kind == "EQ" and not q.adverse and L.acts(q, G) and not L.superseded(q, G)
            and L.status1(q.id) == "CLEAR" and independent(q.actor))


def oracle_joins(L: Ledger, j: J, z: J, G: str) -> bool:
    """Protected property: z helps assert, read in either direction and composed with other
    asserting judgments of a covering class, that j's two revisions are equivalent for j's class.
    Enumerates vertex sequences a, ..., b directly instead of searching edges."""
    a, b, c = j.target
    if not covers(z.target[2], c):
        return False
    pairs = {frozenset(q.target[:2]) for q in L.js
             if q is not z and oracle_asserts(L, q, G) and covers(q.target[2], c)}
    zp = frozenset(z.target[:2])
    inner = [r for r in REVS if r not in (a, b)]
    for n in range(len(inner) + 1):
        for mid in itertools.permutations(inner, n):
            seq = (a,) + mid + (b,)
            steps = [frozenset(seq[i:i + 2]) for i in range(len(seq) - 1)]
            for i, st in enumerate(steps):
                if st == zp and all(t in pairs for m, t in enumerate(steps) if m != i):
                    return True
    return False


def oracle_sat(L: Ledger, r: str, k: str, G: str) -> bool:
    frontier, seen = [r], {r}
    while frontier:
        v = frontier.pop()
        if v == CUR:
            return True
        for q in L.js:
            if (q.kind == "EQ" and not q.adverse and q.target[0] == v and covers(q.target[2], k)
                    and q.target[1] not in seen and oracle_base(L, q, G)):
                seen.add(q.target[1])
                frontier.append(q.target[1])
    return False


def oracle_disagreement(L: Ledger, j: J, G: str) -> bool:
    """The owner must be asked whenever a standing objection contradicts an acting passing judgment."""
    if oracle_resolved(L, j, j, G):
        return False
    return any(not z.adverse and z.kind == "EQ" and L.acts(z, G) and oracle_joins(L, j, z, G)
               for z in L.js)


# ---- scenario generation
def scenarios():
    tgt = {
        "REV": [("i1", "c1", "b1"), ("i2", "c1", "b2"), ("i1", "c2", "b1")],
        "ACC": [("r1",), ("r2",)],
        "GATE": [("r1", "p1"), ("r1", "p2"), ("r2", "p2")],
    }
    objectors = {"REV": ["H", "P"], "ACC": ["H", "P"], "GATE": ["H"]}
    passers = {"REV": ["P", "U"], "ACC": ["P", "U", "A"], "GATE": ["H", "O"]}
    resolvers = ["H", "O", "P", "U", "A", "Q"]
    for kind in ("REV", "ACC", "GATE"):
        T = tgt[kind]
        for obj in objectors[kind]:
            j = J("j", kind, T[0], True, obj)
            for zt, zp, zf in itertools.product(T, passers[kind], ("adm", "pend")):
                z = J("z", kind, zt, False, zp, zf)
                res_opts = [None]
                for rt, ra, rf, sup in itertools.product(T, resolvers, ("adm", "pend", "aband"), (False, True)):
                    if kind == "GATE" and ra not in ("H", "O", "A"):
                        continue
                    res_opts.append(J("y", kind, rt, False, ra, rf, ("j",) if sup else ()))
                chal_opts = [()]
                for ua in resolvers:
                    for up in (True, False):
                        chal_opts.append((C("c1", "j", "P"), Adj("a1", "c1", up, ua)))
                        for ca in resolvers:
                            for cup in (True, False):
                                c2t = C("c2", "a1", "H")
                                chal_opts.append((C("c1", "j", "P"), Adj("a1", "c1", up, ua), c2t,
                                                  Adj("a2", "c2", cup, ca)))
                for y in res_opts:
                    for ch in chal_opts:
                        recs = [j, z] + ([y] if y else []) + list(ch)
                        yield kind, recs


def run_cur_for(kind: str) -> str:
    return "p2"


def check_all(limit_fail: int = 5, verbose: bool = True) -> dict:
    fails: dict[str, int] = {}
    examples: dict[str, list] = {}
    rng = random.Random(7)
    n = 0
    for kind, recs in scenarios():
        n += 1
        L = Ledger(recs)
        rc = run_cur_for(kind)

        def note(inv, msg):
            fails[inv] = fails.get(inv, 0) + 1
            if len(examples.setdefault(inv, [])) < limit_fail:
                examples[inv].append((msg, [r for r in recs]))

        for G in ("D", "F"):
            for z in L.js:
                if not z.adverse and L.base(z, G) != oracle_base(L, z, G):
                    note("I1/I3", f"{G}: base({z.id})={L.base(z, G)} oracle={oracle_base(L, z, G)}")
        # I2: nonind records and refused adjudications change nothing
        keep = [r for r in recs if not (isinstance(r, J) and r.id != "z" and L.nonind(r))]
        L2 = Ledger(keep)
        for G in ("D", "F"):
            if L.outputs(G, rc)[-1:] != L2.outputs(G, rc)[-1:] or \
               [o for o in L.outputs(G, rc) if o[0] == "z"] != [o for o in L2.outputs(G, rc) if o[0] == "z"]:
                note("I2", f"{G}: removing nonind records changed outputs")
        # I4: liftable where it bites
        for G in ("D", "F"):
            for z in L.js:
                if z.adverse or not L.vetoed(z, G) or L.nonind(z):
                    continue
                frame = "adm" if G == "D" else "pend"
                if z.kind == "REV":
                    fix = J("fix", z.kind, z.target, False, "O", frame)
                elif z.kind == "ACC":
                    fix = J("fix", z.kind, z.target, False, "O", frame, tuple(j.id for j in L.js if j.adverse))
                else:
                    fix = J("fix", z.kind, z.target, False, "O", frame, tuple(j.id for j in L.js if j.adverse))
                L3 = Ledger(recs + [fix])
                if "fix" not in L3.adm or L3.vetoed(z, G):
                    note("I4", f"{G}: veto of {z.id} not liftable by an independent owner record")
        # I5: pending/abandoned passing and superseding records change nothing in D
        local = [r for r in recs if not (isinstance(r, J) and not r.adverse and r.frame != "adm")]
        L4 = Ledger(local)
        o1 = [o for o in L.outputs("D", rc) if o[0] in [r.id for r in local] or o[0] == "gterm"]
        o2 = [o for o in L4.outputs("D", rc) if o[0] in [r.id for r in local] or o[0] == "gterm"]
        if o1 != o2:
            note("I5", "pending/abandoned records changed the admitted state")
        # I6: order independence (any order respecting references)
        for _ in range(2):
            perm = recs[:]
            rng.shuffle(perm)
            perm.sort(key=lambda r: (0 if isinstance(r, J) and not r.supersedes else
                                     1 if isinstance(r, J) else
                                     2 if isinstance(r, C) and r.id == "c1" else
                                     3 if r.id == "a1" else 4 if r.id == "c2" else 5))
            if set(Ledger(perm).adm) != set(L.adm):
                note("I6", "admitted set depends on order")
        # I7: class and authors(root)
        for a in L.ads:
            if not independent(a.actor):
                note("I7", f"adjudication {a.id} by a member of authors(root) or unknown lineage admitted")
            c = L.adm[a.challenge]
            t = L.adm[c.target]
            cls = ACTORS[L.adm['j'].actor][3]
            if isinstance(t, Adj):
                cls = max(cls, ACTORS[t.actor][3])
            if ACTORS[a.actor][3] < cls:
                note("I7", f"adjudication {a.id} below its chain's class admitted")
    if verbose:
        print(f"scenarios: {n}")
    return {"n": n, "fails": fails, "examples": examples}


# ---- equivalence chains (R14): one unit u with revisions r0..r3, cur(u) = r3
EQ_HOPS = [("h01", ("r0", "r1", "K")), ("h12", ("r1", "r2", "K")), ("h23", ("r2", "r3", "K")),
           ("h13", ("r1", "r3", "K")), ("h02", ("r0", "r2", "ED")), ("h03", ("r0", "r3", "K2"))]
EQ_CONSUMERS = [("r0", "K"), ("r1", "K"), ("r2", "K"), ("r0", "K2"), ("r0", "ED")]


def eq_scenarios():
    hop_sets = []
    for mask in range(1 << len(EQ_HOPS)):
        chosen = [h for i, h in enumerate(EQ_HOPS) if mask >> i & 1]
        variants = [[J(hid, "EQ", t, False, "P") for hid, t in chosen]]
        if any(hid == "h12" for hid, _ in chosen):
            for actor, frame in (("U", "adm"), ("A", "adm"), ("P", "pend")):
                variants.append([J(hid, "EQ", t, False, actor if hid == "h12" else "P",
                                   frame if hid == "h12" else "adm") for hid, t in chosen])
        hop_sets.extend(variants)
    objections = [None]
    for a, b in itertools.permutations(REVS, 2):
        for cls in ("K", "K2", "ED"):
            for obj in (("H", "P") if cls == "K" else ("H",)):
                objections.append(J("j", "EQ", (a, b, cls), True, obj))
    for hops in hop_sets:
        for j in objections:
            if j is None:
                yield hops
                continue
            endings = [()]
            for ra, rf, sup in itertools.product(("O", "H", "P", "Q"), ("adm", "pend", "aband"), (True, False)):
                endings.append((J("y", "EQ", j.target, False, ra, rf, ("j",) if sup else ()),))
            other = "K2" if j.target[2] != "K2" else "K"
            endings.append((J("y", "EQ", j.target[:2] + (other,), False, "O", "adm", ("j",)),))
            for ua in ("H", "O", "U", "A"):
                for up in (True, False):
                    endings.append((C("c1", "j", "P"), Adj("a1", "c1", up, ua)))
            for e in endings:
                yield hops + [j] + list(e)


def support(outputs: tuple) -> tuple:
    """Invariant (g)2 concerns support, not obligations: a non-independent contrary pass still asks the owner."""
    return tuple(o for o in outputs if not o[0].startswith("adj"))


def eq_outputs(L: Ledger, G: str, ids=None) -> tuple:
    out = [(z.id, L.base(z, G)) for z in sorted(L.js, key=lambda r: r.id)
           if not z.adverse and (ids is None or z.id in ids)]
    out += [(f"sat{r}{k}", L.sat(r, k, G)) for r, k in EQ_CONSUMERS]
    out += [(f"adj{j.id}", L.adjudicate(j, G)) for j in L.js if j.adverse]
    return tuple(out)


def check_eq(limit_fail: int = 5, verbose: bool = True) -> dict:
    fails: dict[str, int] = {}
    examples: dict[str, list] = {}
    rng = random.Random(11)
    n = 0
    for recs in eq_scenarios():
        n += 1
        L = Ledger(recs)

        def note(inv, msg):
            fails[inv] = fails.get(inv, 0) + 1
            if len(examples.setdefault(inv, [])) < limit_fail:
                examples[inv].append((msg, list(recs)))

        for G in ("D", "F"):
            for z in L.js:
                if not z.adverse and L.base(z, G) != oracle_base(L, z, G):
                    note("I1/I3", f"{G}: base({z.id})={L.base(z, G)} oracle={oracle_base(L, z, G)}")
            for r, k in EQ_CONSUMERS:
                if L.sat(r, k, G) != oracle_sat(L, r, k, G):
                    note("I1/I3", f"{G}: sat({r},{k})={L.sat(r, k, G)} oracle={oracle_sat(L, r, k, G)}")
            for j in L.js:
                if j.adverse and L.adjudicate(j, G) != oracle_disagreement(L, j, G):
                    note("I8", f"{G}: adjudication obligation {L.adjudicate(j, G)} oracle "
                               f"{oracle_disagreement(L, j, G)}")
        # I2: nonind records change nothing
        keep = [r for r in recs if not (isinstance(r, J) and not r.adverse and L.nonind(r))]
        L2 = Ledger(keep)
        ids = {r.id for r in keep}
        for G in ("D", "F"):
            if support(eq_outputs(L, G, ids)) != support(eq_outputs(L2, G, ids)):
                note("I2", f"{G}: removing nonind records changed outputs")
        # I4: liftable where it bites
        for G in ("D", "F"):
            frame = "adm" if G == "D" else "pend"
            for j in L.js:
                if not (j.adverse and L.adjudicate(j, G)):
                    continue
                L3 = Ledger(recs + [J("fix", "EQ", j.target, False, "O", frame, (j.id,))])
                if "fix" not in L3.adm or L3.adjudicate(j, G) or any(
                        L3.vetoed(z, G) for z in L3.js if z.id != "fix" and not z.adverse):
                    note("I4", f"{G}: objection {j.id} not liftable by the owner's adjudication")
        # I5: pending/abandoned passing and superseding records change nothing in D
        local = [r for r in recs if not (isinstance(r, J) and not r.adverse and r.frame != "adm")]
        if eq_outputs(L, "D", {r.id for r in local}) != eq_outputs(Ledger(local), "D", {r.id for r in local}):
            note("I5", "pending/abandoned records changed the admitted state")
        # I6: admitted set and admitted outputs under two sampled reference-respecting orders
        for _ in range(2):
            perm = recs[:]
            rng.shuffle(perm)
            perm.sort(key=lambda r: (0 if isinstance(r, J) and not r.supersedes else 1 if isinstance(r, J)
                                     else 2 if isinstance(r, C) else 3))
            Lp = Ledger(perm)
            if set(Lp.adm) != set(L.adm) or eq_outputs(Lp, "D") != eq_outputs(L, "D"):
                note("I6", "admission order changed the admitted set or outputs")
        # I7
        for a in L.ads:
            if not independent(a.actor) or ACTORS[a.actor][3] < ACTORS[L.adm["j"].actor][3]:
                note("I7", f"adjudication {a.id} ineligible but admitted")
    if verbose:
        print(f"equivalence-chain scenarios: {n}")
    return {"n": n, "fails": fails, "examples": examples}


# ---- plan acceptance coverage (R14 sibling): one item, issuable iff a supporting acceptance covers cur
def plan_scenarios():
    accs = [("p0", "i0"), ("p1", "i1"), ("p2", "i2")]
    for cur in ("i1", "i2", "i1x"):
        for mask in range(1, 1 << len(accs)):
            chosen = [a for i, a in enumerate(accs) if mask >> i & 1]
            for variant in ("P", "U", "pend"):
                if variant != "P" and len(chosen) > 2:
                    continue
                zs = [J(pid, "PLAN", (r,), False, "U" if variant == "U" and k == 0 else "P",
                        "pend" if variant == "pend" and k == 0 else "adm") for k, (pid, r) in enumerate(chosen)]
                for rej in (None, "i0", "i1", "i2", "i1x"):
                    if rej is None:
                        yield cur, zs
                        continue
                    j = J("j", "PLAN", (rej,), True, "H")
                    endings = [()]
                    for ra, rf, sup in itertools.product(("O", "H", "P", "Q"), ("adm", "pend", "aband"), (True, False)):
                        endings.append((J("y", "PLAN", (rej,), False, ra, rf, ("j",) if sup else ()),))
                    for ua in ("H", "O", "U", "A"):
                        for up in (True, False):
                            endings.append((C("c1", "j", "P"), Adj("a1", "c1", up, ua)))
                    for e in endings:
                        yield cur, zs + [j] + list(e)


def plan_issuable(L: Ledger, G: str) -> bool:
    return any(z.kind == "PLAN" and not z.adverse and tight(z.target[0], PLAN_CUR[0]) and L.base(z, G)
               for z in L.js)


def oracle_issuable(L: Ledger, G: str) -> bool:
    return any(z.kind == "PLAN" and not z.adverse and tight(z.target[0], PLAN_CUR[0]) and oracle_base(L, z, G)
               for z in L.js)


def plan_outputs(L: Ledger, G: str, ids=None) -> tuple:
    out = [(z.id, L.base(z, G)) for z in sorted(L.js, key=lambda r: r.id)
           if not z.adverse and (ids is None or z.id in ids)]
    out.append(("issuable", plan_issuable(L, G)))
    out += [(f"adj{j.id}", L.adjudicate(j, G)) for j in L.js if j.adverse]
    return tuple(out)


def check_plan(limit_fail: int = 5, verbose: bool = True) -> dict:
    fails: dict[str, int] = {}
    examples: dict[str, list] = {}
    rng = random.Random(13)
    n = 0
    for cur, recs in plan_scenarios():
        n += 1
        PLAN_CUR[0] = cur
        L = Ledger(recs)

        def note(inv, msg):
            fails[inv] = fails.get(inv, 0) + 1
            if len(examples.setdefault(inv, [])) < limit_fail:
                examples[inv].append((f"cur={cur} {msg}", list(recs)))

        for G in ("D", "F"):
            for z in L.js:
                if not z.adverse and L.base(z, G) != oracle_base(L, z, G):
                    note("I1/I3", f"{G}: base({z.id})={L.base(z, G)} oracle={oracle_base(L, z, G)}")
            if plan_issuable(L, G) != oracle_issuable(L, G):
                note("I1/I3", f"{G}: issuable={plan_issuable(L, G)} oracle={oracle_issuable(L, G)}")
            for j in L.js:
                if not j.adverse:
                    continue
                want = not oracle_resolved(L, j, j, G) and any(
                    not z.adverse and L.acts(z, G) and j.target[0] in
                    {r for r in ("i0", "i1", "i2", "i1x") if tight(z.target[0], r)} for z in L.js)
                if L.adjudicate(j, G) != want:
                    note("I8", f"{G}: adjudication obligation {L.adjudicate(j, G)} oracle {want}")
        keep = [r for r in recs if not (isinstance(r, J) and not r.adverse and L.nonind(r))]
        ids = {r.id for r in keep}
        for G in ("D", "F"):
            if support(plan_outputs(L, G, ids)) != support(plan_outputs(Ledger(keep), G, ids)):
                note("I2", f"{G}: removing nonind records changed outputs")
        for G in ("D", "F"):
            for j in L.js:
                if j.adverse and L.adjudicate(j, G):
                    L3 = Ledger(recs + [C("cf", "j", "P"), Adj("af", "cf", True, "O")])
                    if "af" not in L3.adm or L3.adjudicate(j, G):
                        note("I4", f"{G}: objection {j.id} not liftable by an upheld challenge")
        local = [r for r in recs if not (isinstance(r, J) and not r.adverse and r.frame != "adm")]
        lid = {r.id for r in local}
        if plan_outputs(L, "D", lid) != plan_outputs(Ledger(local), "D", lid):
            note("I5", "pending/abandoned records changed the admitted state")
        for _ in range(2):
            perm = recs[:]
            rng.shuffle(perm)
            perm.sort(key=lambda r: (0 if isinstance(r, J) and not r.supersedes else 1 if isinstance(r, J)
                                     else 2 if isinstance(r, C) else 3))
            Lp = Ledger(perm)
            if set(Lp.adm) != set(L.adm) or plan_outputs(Lp, "D") != plan_outputs(L, "D"):
                note("I6", "admission order changed the admitted set or outputs")
        for a in L.ads:
            if not independent(a.actor) or ACTORS[a.actor][3] < ACTORS[L.adm["j"].actor][3]:
                note("I7", f"adjudication {a.id} ineligible but admitted")
    PLAN_CUR[0] = "i2"
    if verbose:
        print(f"plan-coverage scenarios: {n}")
    return {"n": n, "fails": fails, "examples": examples}


MUTATIONS = {
    "relief_ignores_nonind": "a non-independent owner pass relieves (9e5a763 B1)",
    "wide_review_supersession": "review supersession on same content, any item/base (051cce3 B1)",
    "eligibility_support_tier_only": "eligibility checked only on direct challenges (29da56e B1)",
    "challenged_record_authors": "eligibility against the challenged record, not the root (6b986de B1)",
    "gate_run_veto": "gate veto keyed on the run-parameterized obligation (362af9f B1-A)",
    "frame_acts_everywhere": "frame records act in the admitted state (b46c250 B1)",
    "base_ignores_nonind": "base ignores non-independence (29da56e B1(g))",
    "no_class_check": "adjudication class not checked (51070e5 B1)",
    "endpoint_only_equivalence_reach": "equivalence veto reaches only the same endpoints (a6ed164 B1)",
    "directed_chain_only": "an objection blocks only chains read in their recorded direction (a6ed164 B1 siblings)",
    "chain_ignores_class": "an objection blocks chains whose hops do not cover its class (a6ed164 B1 controls)",
    "obligation_direct_only": "a blocked chain derives no adjudication obligation (a6ed164 B1 routing)",
    "plan_reach_names_only": "a plan rejection reaches only acceptances naming its revision, not covering it",
}
PLAN_MUTATIONS = {"plan_reach_names_only"}
EQ_MUTATIONS = {"endpoint_only_equivalence_reach", "directed_chain_only", "chain_ignores_class",
                "obligation_direct_only"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--mutations", action="store_true", help="also check that each mutation is caught")
    args = ap.parse_args()
    MUT.clear()
    res = check_all()
    res_eq = check_eq()
    res_plan = check_plan()
    ok = not res["fails"] and not res_eq["fails"] and not res_plan["fails"]
    if ok:
        print("unmutated §5.10 rules: every modelled invariant holds")
    else:
        print("unmutated §5.10 rules: INVARIANT FAILURES", res["fails"], res_eq["fails"], res_plan["fails"])
        for inv, ex in (list(res["examples"].items()) + list(res_eq["examples"].items())
                        + list(res_plan["examples"].items())):
            for msg, recs in ex[:2]:
                print(" ", inv, msg)
                for r in recs:
                    print("     ", r)
    if args.mutations:
        for m, why in MUTATIONS.items():
            MUT.clear()
            MUT.add(m)
            # a mutation changes only its own family's code, so only that family is re-run
            r = (check_eq(verbose=False) if m in EQ_MUTATIONS else
                 check_plan(verbose=False) if m in PLAN_MUTATIONS else check_all(verbose=False))
            caught = sorted(r["fails"])
            print(f"mutation {m}: {'caught by ' + ', '.join(caught) if caught else 'NOT CAUGHT'} ({why})")
            ok = ok and bool(caught)
        MUT.clear()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
