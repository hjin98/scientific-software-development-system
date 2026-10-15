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
  frames   adm (admitted frame), pend (a pending enactment's frame), aband (abandoned)
  states   D (the admitted state) and F (the pending enactment's frame)
  records  judgments (pass/adverse, optional supersedes), blocking challenges with a
           raiser, adjudications (UPHELD/DISMISSED) of a challenge, counter-challenges
           of an upholding, and a challenge of a dismissal.

Invariants (Manual §5.10 (g)), each checked against an oracle written from the
protected properties rather than from the §5.10 formulas:
  I1/I3  base(z) equals the oracle in both directions: a passing judgment supports iff it
         acts, is independent, is not withdrawn, and every objection reaching it was ended
         by an independent author/owner record that judged the objection's own target
         (withdrawing it), or, for a transformation review, z's exact target (relief), or by
         an eligible upheld challenge.
  I2     records with nonind and inadmissible adjudications change no derived value.
  I4     every veto can be lifted by an admissible record in the state where it bites.
  I5     passing and superseding records of pending/abandoned frames change nothing in D.
  I6     the admitted set does not depend on admission order.
  I7     no admitted adjudication is below its chain's class or dependent on authors(root).

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
    return kind in ("REV", "ACC")


def reach(j: J, z: J) -> bool:
    if j.kind != z.kind:
        return False
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
    if r.kind == "ACC":
        return r.target == x.target
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

    def vetoed(self, z: J, G: str) -> bool:
        if z.adverse:
            return False
        return any(j.adverse and reach(j, z) and self.stands(j, G) and not self.relieved(j, z, G)
                   for j in self.js)

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
        if j.id in y.supersedes and j.kind == "ACC" and y.target == j.target:
            return True
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


MUTATIONS = {
    "relief_ignores_nonind": "a non-independent owner pass relieves (9e5a763 B1)",
    "wide_review_supersession": "review supersession on same content, any item/base (051cce3 B1)",
    "eligibility_support_tier_only": "eligibility checked only on direct challenges (29da56e B1)",
    "challenged_record_authors": "eligibility against the challenged record, not the root (6b986de B1)",
    "gate_run_veto": "gate veto keyed on the run-parameterized obligation (362af9f B1-A)",
    "frame_acts_everywhere": "frame records act in the admitted state (b46c250 B1)",
    "base_ignores_nonind": "base ignores non-independence (29da56e B1(g))",
    "no_class_check": "adjudication class not checked (51070e5 B1)",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--mutations", action="store_true", help="also check that each mutation is caught")
    args = ap.parse_args()
    MUT.clear()
    res = check_all()
    ok = not res["fails"]
    if ok:
        print("unmutated §5.10 rules: every invariant holds")
    else:
        print("unmutated §5.10 rules: INVARIANT FAILURES", res["fails"])
        for inv, ex in res["examples"].items():
            for msg, recs in ex[:2]:
                print(" ", inv, msg)
                for r in recs:
                    print("     ", r)
    if args.mutations:
        for m, why in MUTATIONS.items():
            MUT.clear()
            MUT.add(m)
            r = check_all(verbose=False)
            caught = sorted(r["fails"])
            print(f"mutation {m}: {'caught by ' + ', '.join(caught) if caught else 'NOT CAUGHT'} ({why})")
            ok = ok and bool(caught)
        MUT.clear()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
