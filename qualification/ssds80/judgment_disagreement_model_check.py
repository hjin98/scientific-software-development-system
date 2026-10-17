"""Bounded model check of the SSDS 8 Architecture Manual §5.10 judgment-disagreement layer.

Companion to s1_disagreement_model_check.py (which models workplan §6.6 assessment
disagreement). This is a diagnostic transcription of the Manual's written rules, not an
SSDS implementation and not an adequacy oracle (DS-001): it can show that the written
§5.10 predicates contradict the invariants §5.10 (g) states, on small ledgers; it can
never show that the design is right or that a production owner behaves this way.

What is modelled, in four families (the first checked by check_all, the others by check_family):
  kinds    REV   a transformation REVIEW: target (item revision, changed content, base); item
                 revisions i1, i2 (an amendment of item I's contract), k1 (I re-identified as K
                 with i1's prose and contract) and k2 (re-identified with a one-byte heading
                 change); reach = every review whose output content entries name the vetoed
                 change's units at the same content, under any item, revision or plan (SD-34,
                 SD-41), with a re-dispatched review over out(o) that keeps or re-does the content; supersession on the exact target; per-target relief (route 3).
           ACC   an ACCEPTANCE: target = (subject, revision content); s2 re-identifies s1 with
                 identical content; reach = the same subject triple only (S10);
                 supersession on the exact target.
           GATE  a GATE_DECISION: target = (revision, run); reach and supersession
                 target = same revision in any run; no independence requirement;
                 passing decisions aggregate by minimum over the current run.
           EQ    an EQUIVALENCE (equivalence-chain family): target = (r_from, r_to, class) on
                 one unit with revisions r0..r3, cur(u) = r3; classes K, K2 (consumers) and ED
                 (editorial, covering both); judgments compose into every pair of revisions
                 they connect, read in either direction; consumers' sat over paths.
           COMP  a COMPLETENESS (completeness-cover family): target = (scope, class) over units
                 u1..u3 (S1, S2, S3, S12 = the subject, SX = the tree); judgments on sub-scopes
                 compose by union; one analyzer declaration (actor M, no requirement); the
                 consumer is the §4.6 closure bound of each unit.
           PLAN  a PLAN_ACCEPTANCE (plan-coverage family), on field values (SD-32): item A's
                 revisions are (prose, budget, scope), r ⊑ r2 iff same prose, budget not greater
                 and scope a subset; seven revisions, among them an R2 amendment incomparable with
                 the accepted one, tightenings, a loosening and a prose edit, each also current;
                 item B has one revision; item A2 is A re-identified, its one revision byte-identical
                 to one of A's. A rejection of r* reaches every acceptance, in any item, of a revision
                 with a common tightening (same prose and fixed fields); the current revision is
                 not read; the rejecter's or owner's acceptance of a reached target relieves it
                 (route 3). The oracle builds the common tightening from the field values.
                 Supersession on the exact target while its basis holds.
           The one reach rule (SD-29) for the composing kinds: z is reached when some set of
           asserting judgments of the kind, with z, claims what the objection denies and
           without z does not (Ledger.composed_reach with the per-kind Ledger.derives).
           GATE basis (gate-basis family, SD-35): a gate decision whose basis is built from
                 the evidence core shown (required evidence, a revision assessment, a non-required
                 realization, challenges, a standing gate rejection); current() is computed over
                 that basis and must never be asked of a challenge-tier record (I9).
  actors   A  the content's author (human, R3)       H  an independent human (R3)
           O  the owner (human, R3, independent)      P  an attested-fresh agent (R2)
           U  an agent with UNKNOWN lineage (R2; never independent)
           Q  an owner execution with UNKNOWN lineage (R2; never independent)
           M  machinery (an analyzer completeness declaration; no requirement)
  frames   adm (admitted frame), pend (a pending enactment's frame), aband (abandoned)
  states   D (the admitted state) and F (the pending enactment's frame)
  records  judgments (pass/adverse, optional supersedes), blocking challenges with a
           raiser, risk overrides of a challenge (the target becomes PROVISIONAL, base P),
           adjudications (UPHELD/DISMISSED) of a challenge, counter-challenges of an
           upholding, and a challenge of a dismissal.

Invariants (Manual §5.10 (g)), each checked against an oracle written from the
protected properties rather than from the §5.10 formulas. The oracle reuses the model's
helpers for acting, supersession, S1 status (in_force, contested) and the independence
test, so a mistake in one of those can agree on both sides. It is independent in how it
combines them: per-kind claims instead of the generic rule, vertex sequences for chains,
unions reachable by dynamic programming for covers, widest paths by levels for sat:
  I1/I3  base(z) (F, P or T) and every consumer value equal the oracle's: a passing
         judgment supports iff it acts, is independent, is not withdrawn, and every
         objection reaching it was ended by an independent author/owner record that judged
         the objection's own target (withdrawing it), or, for a transformation review,
         z's exact target (relief), or by an eligible upheld challenge.
  I2     records with nonind change no support value (base, sat, bound, issuability,
         gterm); a non-independent contrary pass still derives the owner's obligation.
  I4     every veto can be lifted by an admissible record in the state where it bites.
  I5     passing and superseding records of pending/abandoned frames change nothing in D.
  I6     the admitted set (and, for the composing families, the admitted state's outputs)
         is the same under two sampled reference-respecting permutations per case; not
         every order is tried.
  I7     no admitted adjudication is below its chain's class or dependent on authors(root).
  I9     (gate-basis) current() is never asked of a record outside its domain; a gate decision's
         value reads only its required premises, never what is merely shown.
  I10    (gate-basis) liveness: while the revision assessment counts and the required evidence
         holds, a fresh gate decision is admissible, so a ready gate obligation is answerable.
  I13-I15, I18 (obligation-routing) §10.4's list against every section's own claim (SD-36 to SD-40): every
         OPEN obligation has exactly one route; no REVALIDATE of an integrated review or task result; a
         reopened integrated item is re-dispatched within budget unless a fence, a pending candidate or a
         principal's decision comes first; a pending candidate is never discarded; a kept fence's route
         ends once decided. Section claims enter only under mutations (b365947 N1).
  I8     (composing families) the owner's adjudication obligation is derived exactly when a
         standing objection contradicts a passing judgment acting in the state.

Not modelled: evidence assessments, plan objective sections, intake, product scope,
qualified gate values, integration and rebase transitions, loss boundaries, before-image
bases, changing authorship, request structure (the model gives every equivalence and
completeness the requirement the authorship rule gives it), full Admission, and more
than one resolving record. A green run says nothing about those.

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
    "M": (False, False, False, 0),  # machinery (an analyzer completeness declaration): no requirement
    "C": (True, True, False, 3),    # the human who authored r0's content; never acts in a scenario
}
AUTHORS = frozenset({"A"})  # authors(x) of every modelled content except an equivalence's endpoints
# the authors of each equivalence-family revision's differing content (r0 by C, the later ones by A)
REV_AUTHORS = {"r0": frozenset({"C"}), "r1": frozenset({"A"}), "r2": frozenset({"A"}), "r3": frozenset({"A"})}


def authors_of(z) -> frozenset:
    """§5.10 (a) authors: for an EQUIVALENCE, the content differing between its endpoints, on either side."""
    if getattr(z, "kind", None) == "EQ":
        if "eq_authors_to_side_only" in MUT:  # 34803df B2: only r_to's content that differs from r_from
            return REV_AUTHORS[z.target[1]]
        return REV_AUTHORS[z.target[0]] | REV_AUTHORS[z.target[1]]
    return AUTHORS

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
    basis: tuple = ()  # gate-basis family only: ((mode, record id), ...), mode record | identity


@dataclass(frozen=True)
class C:  # blocking challenge
    id: str
    target: str        # record id (judgment or adjudication)
    raiser: str


@dataclass(frozen=True)
class RO:  # an in-force RISK_OVERRIDE of a blocking challenge (§10.5): the target becomes PROVISIONAL
    id: str
    challenge: str


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
    return kind in ("REV", "ACC", "EQ", "PLAN", "COMP")


def req(z) -> bool:
    """§5.10 (a) Requirement, keyed on authorship (SD-29): machinery records never carry one."""
    if z.actor == "M":
        return False
    if "requirement_request_colocated" in MUT and z.kind in ("EQ", "COMP"):
        return False  # bf23372 B2: only a judgment co-submitted with its change; no modelled one is
    return requirement(z.kind)


# ---- plan items (§11.2, §13.4), on field values (SD-32). An item revision of A is (prose, budget,
# write scope); r ⊑ r2 (r2 tightens r) iff the prose is byte-identical, budget(r2) <= budget(r) and
# scope(r2) ⊆ scope(r). Item B has one revision. A plan judgment's target is a tuple of (item, revision).
AB, ABC, A_ = frozenset("ab"), frozenset("abc"), frozenset("a")
PLAN_REVS = {
    "a10ab": ("P", 10, AB), "a6ab": ("P", 6, AB), "a5ab": ("P", 5, AB), "a5a": ("P", 5, A_),
    "a5abc": ("P", 5, ABC), "a10abc": ("P", 10, ABC), "x10ab": ("Q", 10, AB),  # x10ab: a prose edit
    "b1": ("B", 1, frozenset("z")),
    "a2_10ab": ("P", 10, AB),  # item A2: item A re-identified (or copied), byte-identical content
}
PLAN_CUR = ["a5ab"]  # item A's current revision in the scenario being evaluated; item B's is b1
ITEM_REVS = {"A": ("a10ab", "a6ab", "a5ab", "a5a", "a5abc", "a10abc", "x10ab"), "B": ("b1",),
             "A2": ("a2_10ab",)}


def tight(r: str, r2: str) -> bool:
    (p1, b1, s1), (p2, b2, s2) = PLAN_REVS[r], PLAN_REVS[r2]
    return p1 == p2 and b2 <= b1 and s2 <= s1


def plan_cur(item: str) -> str:
    return PLAN_CUR[0] if item == "A" else ITEM_REVS[item][0]


def plan_reached(rs: str, r: str, it: str) -> bool:
    """§5.10 (b) plan row (SD-32). A rejection of rs denies rs and every tighter revision; an acceptance
    of r claims r and every tighter revision; they contradict exactly when the two have a common
    tightening, which by §13.4 is byte-identical prose and equal fixed fields (here: the prose). The
    current revision is not read. Only the rejecter or the owner relieves a reached target (route 3)."""
    cur = plan_cur(it)
    if "plan_reach_names_only" in MUT:
        return rs == r
    if "plan_reach_any_tighter" in MUT:  # bf23372 N1: preservation alone
        return tight(r, rs)
    if "plan_reach_current_only" in MUT:  # 34803df B1
        return rs == r or (rs == cur and tight(r, cur))
    if "plan_reach_path_only" in MUT:  # 0d2b35e B1: r ⊑ rs ⊑ cur
        return rs == r or (tight(r, rs) and tight(rs, cur))
    if "plan_fresh_acceptance_exempt" in MUT:  # 83a82df B1
        return rs == r or (tight(r, cur) and tight(rs, cur) and not tight(rs, r))
    if "plan_revert_exemption" in MUT:  # e548472 B1 (SD-30's rule)
        return rs == r or (tight(r, cur) and tight(rs, cur))
    if "plan_cur_join" in MUT:  # 4c52205 B1 (SD-31's rule): the join read at the current revision only
        return rs == r or tight(r, rs) or (tight(r, cur) and tight(rs, cur))
    return PLAN_REVS[r][0] == PLAN_REVS[rs][0]  # same prose and fixed fields: a common tightening


def plan_reaches(j, z) -> bool:
    # keyed on what was judged, not on the item's identity (SD-33): any item, any plan
    hits = [any((it2 == it or "plan_reach_same_item_only" not in MUT) and plan_reached(rs, r, it)
                for it2, r in z.target) for it, rs in j.target]
    if "plan_rejection_denies_set" in MUT:  # 34803df B1(b): the named set only as a whole
        return all(hits)
    return any(hits)


# a transformation review's item revision: (plan item, its prose and contract). i2 amends item I's
# contract; k1 re-identifies I as item K with i1's prose and contract; k2 re-identifies it with a
# one-byte heading change (SD-34)
REV_ITEMS = {"i1": ("I", "pc1"), "i2": ("I", "pc2"), "k1": ("K", "pc1"), "k2": ("K2", "pc3")}
# a review's content: (changed entries, output content entries). c1 and c2 are first enactments (their
# output entries are their change); c1v is a re-dispatched enactment that changed only v, so its review's
# output entries name all of out(o) = {u, v} with u still at c1's content; cv2 re-did u (SD-41, b365947 B2)
REV_CONTENT = {"c1": ({("u", 1)}, {("u", 1)}), "c2": ({("u", 2)}, {("u", 2)}),
               "c1v": ({("v", 1)}, {("u", 1), ("v", 1)}), "cv2": ({("u", 2)}, {("u", 2), ("v", 1)})}


def review_reached(j_content: str, z_content: str) -> bool:
    """A transformation review's veto reaches a review whose output content entries name each of the
    vetoed transformation's changed units at the same content (SD-41)."""
    if "review_reach_changed_only" in MUT:  # b365947 B2: the same changed content only
        return j_content == z_content
    return REV_CONTENT[j_content][0] <= REV_CONTENT[z_content][1]


def reach(j: J, z: J) -> bool:
    if j.kind != z.kind:
        return False
    if j.kind == "PLAN":
        return plan_reaches(j, z)
    if j.kind == "REV":
        # the same changed-unit content, under any item, revision or plan (SD-34)
        (ji, jpc), (zi, zpc) = REV_ITEMS[j.target[0]], REV_ITEMS[z.target[0]]
        if "review_reach_same_item_only" in MUT:  # 5895687 B1(b): keyed on the item's identity
            return review_reached(j.target[1], z.target[1]) and ji == zi
        if "review_reach_item_or_prose" in MUT:  # 913db8f B1 (SD-33's rule)
            return review_reached(j.target[1], z.target[1]) and (ji == zi or jpc == zpc)
        return review_reached(j.target[1], z.target[1])
    if j.kind == "ACC":
        # target (subject, revision content): the same subject triple only (S10); s2, s1 re-identified
        # with byte-identical content, is a control the objection does not reach
        if "acceptance_reach_by_content" in MUT:  # edabd81 N2: content keying across subjects
            return j.target[1] == z.target[1]
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
    if r.kind in ("ACC", "EQ", "COMP"):
        return r.target == x.target  # EQ: the exact (endpoints, class); COMP: (scope, class)
    if r.kind == "PLAN":  # the target, while its basis holds (Admission step 6: each named revision ⊑ cur)
        if "plan_supersession_current_only" in MUT:  # 0d2b35e N1: only while every named revision is current
            return r.target == x.target and all(plan_cur(it) == rv for it, rv in x.target)
        return r.target == x.target and all(tight(rv, plan_cur(it)) for it, rv in x.target)
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
        self.ros = [r for r in self.adm.values() if isinstance(r, RO)]
        self._memo: dict = {}

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
        if isinstance(rec, RO):
            return rec.challenge in self.adm
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
                authors = authors_of(root)
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
            if req(rec) and not independent(rec.actor, authors_of(rec)):
                return False
        return True

    # ---- S0
    def nonind(self, z: J) -> bool:
        return req(z) and not independent(z.actor, authors_of(z))

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
        opened = [c for c in cs if self.open(c)]
        if any(not any(o.challenge == c.id for o in self.ros) for c in opened):
            return "BLOCKED"
        if opened:
            return "PROVISIONAL"
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
        if j.kind not in ("REV", "PLAN") or (j.kind == "PLAN" and "plan_no_relief" in MUT):
            return False
        for y in self.js:
            if (not y.adverse and y.kind == j.kind and y.target == z.target
                    and (y.actor == j.actor or ACTORS[y.actor][2]) and self.acts(y, G)
                    and not self.superseded(y, G) and self.status1(y.id) == "CLEAR"
                    and ("relief_ignores_nonind" in MUT or not self.nonind(y))):  # 9e5a763 B1
                return True
        return False

    def reaches(self, j: J, z: J, G: str) -> bool:
        if j.kind in COMPOSING and z.kind == j.kind:
            key = ("reach", j.id, z.id, G)
            if key not in self._memo:
                self._memo[key] = self.composed_reach(j, z, G)
            return self._memo[key]
        return reach(j, z)

    def vetoed(self, z: J, G: str) -> bool:
        if z.adverse:
            return False
        return any(j.adverse and self.reaches(j, z, G) and self.stands(j, G) and not self.relieved(j, z, G)
                   for j in self.js)

    # ---- §5.10 (a) the one reach rule (SD-29): z, alone or composed with asserting judgments of its
    # kind as the kind's row declares, claims what j denies, and the claim needs z
    def asserts(self, q: J, G: str) -> bool:
        st = self.status1(q.id)
        ok = st == "CLEAR" if "asserts_requires_clear" in MUT else st in ("CLEAR", "PROVISIONAL")
        return (not q.adverse and self.acts(q, G) and not self.superseded(q, G) and ok  # bf23372 B1(c)
                and not self.nonind(q))

    def relevant(self, j: J, q: J) -> bool:
        if j.kind == "EQ":
            return "chain_ignores_class" in MUT or covers(q.target[2], j.target[2])
        if j.kind == "COMP":
            if "completeness_reach_analyzer_id" in MUT and (q.actor == "M") != (j.actor == "M"):
                return False  # bf23372 B1(b): the analyzer identity compared as part of the target
            return q.target[1] == j.target[1] and SCOPES[q.target[0]] <= SCOPES[j.target[0]]
        return True

    def derives(self, j: J, S: list) -> bool:
        """The kind's composition (§5.10 (b)): does S claim the proposition j denies?"""
        if j.kind == "EQ":
            a, b = j.target[0], j.target[1]
            if "endpoint_only_equivalence_reach" in MUT:  # a6ed164 B1
                return any(q.target[:2] == (a, b) for q in S)
            directed = "directed_chain_only" in MUT
            adj = {}
            for q in S:
                adj.setdefault(q.target[0], set()).add(q.target[1])
                if not directed:
                    adj.setdefault(q.target[1], set()).add(q.target[0])

            def reach_from(x, y):
                seen, todo = {x}, [x]
                while todo:
                    v = todo.pop()
                    for w in adj.get(v, ()):
                        if w not in seen:
                            seen.add(w)
                            todo.append(w)
                return y in seen
            return reach_from(a, b) or (directed and reach_from(b, a))
        if j.kind == "COMP":
            X = SCOPES[j.target[0]]
            if "completeness_exact_only" in MUT:  # bf23372 B1(a): no composition by union
                return any(SCOPES[q.target[0]] == X for q in S)
            return set().union(*(SCOPES[q.target[0]] for q in S)) >= X if S else False
        if j.kind == "PLAN":
            # a rejection denies each item revision it names; acceptances do not compose
            return any(plan_reaches(j, q) for q in S)
        return False

    def composed_reach(self, j: J, z: J, G: str) -> bool:
        if z.adverse or not self.relevant(j, z):
            return False
        others = [q for q in self.js if q is not z and q.kind == j.kind and self.asserts(q, G)
                  and self.relevant(j, q)]
        for k in range(len(others) + 1):
            for S in itertools.combinations(others, k):
                if self.derives(j, list(S) + [z]) and not self.derives(j, list(S)):
                    return True
        return False

    def adjudicate(self, j: J, G: str) -> bool:
        """§5.10 (f): a standing adverse judgment that vetoes a passing judgment acting in G."""
        if not j.adverse or not self.stands(j, G):
            return False
        for z in self.js:
            if z.adverse or z.kind != j.kind or not self.acts(z, G) or self.superseded(z, G):
                continue
            if "obligation_direct_only" in MUT and j.kind == "EQ" and set(z.target[:2]) != set(j.target[:2]):
                continue
            if self.reaches(j, z, G) and not self.relieved(j, z, G):
                return True
        return False

    def base3(self, z: J, G: str) -> int:
        """§5.5 base: 0 = F, 1 = P, 2 = T."""
        key = ("base", z.id, G)
        if key in self._memo:
            return self._memo[key]
        v = 2
        st = self.status1(z.id)
        if not self.acts(z, G) or self.superseded(z, G) or st in ("REVOKED", "BLOCKED"):
            v = 0
        elif self.vetoed(z, G):
            v = 0
        elif "base_ignores_nonind" not in MUT and self.nonind(z):  # 29da56e B1(g)
            v = 0
        elif st == "PROVISIONAL":
            v = 1
        self._memo[key] = v
        return v

    def base(self, z: J, G: str) -> bool:
        return self.base3(z, G) > 0

    def sat3(self, r: str, k: str, G: str) -> int:
        """§4.4: max over simple equivalence paths r -> cur(u) of the min of the hops' values."""
        if r == CUR:
            return 2
        hops = [(q, self.base3(q, G)) for q in self.js if q.kind == "EQ" and not q.adverse
                and covers(q.target[2], k)]
        hops = [(q, v) for q, v in hops if v > 0]
        best = [0]

        def walk(v, seen, m):
            if v == CUR:
                best[0] = max(best[0], m)
                return
            for q, val in hops:
                if q.target[0] == v and q.target[1] not in seen:
                    walk(q.target[1], seen | {q.target[1]}, min(m, val))
        walk(r, {r}, 2)
        return best[0]

    def bound(self, u: str, G: str) -> str:
        """§4.6: the smallest scope in chain(u) with a COMPLETE of class DEF current with value T."""
        for X in CHAIN[u]:
            if any(q.kind == "COMP" and not q.adverse and q.target == (X, "DEF") and self.base3(q, G) == 2
                   for q in self.js):
                return X
        return CHAIN[u][-1]

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


# ---- completeness scopes (§2.6, §4.6): units u1..u3; S12 is the subject s, SX the whole tree
SCOPES = {"S1": frozenset({"u1"}), "S2": frozenset({"u2"}), "S3": frozenset({"u3"}),
          "S12": frozenset({"u1", "u2"}), "SX": frozenset({"u1", "u2", "u3"})}
CHAIN = {"u1": ["S1", "S12", "SX"], "u2": ["S2", "S12", "SX"], "u3": ["S3", "SX"]}
COMPOSING = ("EQ", "COMP", "PLAN")


# ---- oracle (written from the protected properties, not from §5.10's formulas; it shares the
# model's S1 helpers, acts, superseded and the independence test)
def oracle_req(z: J) -> bool:
    return z.actor != "M" and z.kind in ("REV", "ACC", "EQ", "PLAN", "COMP")


def oracle_authors(z) -> frozenset:
    """Whoever authored content that differs between an equivalence's endpoints, whichever side."""
    if z.kind == "EQ":
        return frozenset().union(*(REV_AUTHORS[r] for r in z.target[:2]))
    return AUTHORS


def oracle_same(L: Ledger, j: J, z: J, G: str) -> bool:
    """Does z, as its kind composes, help claim what j denies?"""
    if j.kind == "EQ":
        return oracle_joins(L, j, z, G)
    if j.kind == "COMP":
        return oracle_covers(L, j, z, G)
    if j.kind == "PLAN":
        # claims: an acceptance of rz asserts every tightening of rz acceptable; a rejection of rj
        # denies every tightening of rj. They contradict iff some revision tightens both: build the
        # candidate meet from the field values and test it against both (not the row's formula)
        for it, rj in j.target:
            for it2, rz in z.target:  # whichever item or plan names it (SD-33)
                (pz, bz, sz), (pj, bj, sj) = PLAN_REVS[rz], PLAN_REVS[rj]
                meet = (pz, min(bz, bj), sz & sj)
                if (meet[0] == pz and meet[1] <= bz and meet[2] <= sz
                        and meet[0] == pj and meet[1] <= bj and meet[2] <= sj):
                    return True
        return False
    if j.kind == "REV":
        # what a review judged is the content its output entries name (SD-41); an adverse review denies
        # its target's change, a passing one asserts every entry it names; the item it was produced for
        # is not part of the claim (SD-34). The claim and the formula coincide here
        denied = REV_CONTENT[j.target[1]][0]
        asserted = REV_CONTENT[z.target[1]][1]
        return all(e in asserted for e in denied)
    if j.kind == "ACC":
        # an acceptance attaches to one exact subject (S10): content identity never transfers it
        return j.target == z.target
    return j.target[0] == z.target[0]


def oracle_base3(L: Ledger, z: J, G: str) -> int:
    if z.adverse or not L.acts(z, G) or L.superseded(z, G):
        return 0
    st = L.status1(z.id)
    if st in ("REVOKED", "BLOCKED"):
        return 0
    if oracle_req(z) and not independent(z.actor, oracle_authors(z)):
        return 0
    for j in L.js:
        if j.adverse and j.kind == z.kind and oracle_same(L, j, z, G) and not oracle_resolved(L, j, z, G):
            return 0
    return 1 if st == "PROVISIONAL" else 2


def oracle_base(L: Ledger, z: J, G: str) -> bool:
    return oracle_base3(L, z, G) > 0


def oracle_resolved(L: Ledger, j: J, z: J, G: str) -> bool:
    def eligible_resolver(y: J) -> bool:
        return (not y.adverse and L.acts(y, G) and not L.superseded(y, G)
                and L.status1(y.id) == "CLEAR"
                and (y.actor == j.actor or ACTORS[y.actor][2])
                and (not oracle_req(y) or independent(y.actor, oracle_authors(y))))
    for y in L.js:
        if not eligible_resolver(y):
            continue
        if j.kind in ("REV", "PLAN") and y.kind == j.kind and y.target == z.target:
            return True  # route 3: the author's or owner's pass of z's exact target
        if j.id in y.supersedes and j.kind in ("REV", "ACC", "EQ", "COMP", "PLAN") and y.target == j.target:
            return True  # routes 1-2: withdrawal by judging the objection's own target
        if j.id in y.supersedes and j.kind == "GATE" and y.target[0] == j.target[0]:
            return True
    # route 4: an eligible upheld challenge, in force and uncontested
    for c in L.cs:
        if c.target != j.id:
            continue
        for a in L.ads:
            if a.challenge == c.id and a.upheld and L.in_force(a) and not L.contested(a):
                if independent(a.actor, oracle_authors(j)) and ACTORS[a.actor][3] >= ACTORS[j.actor][3]:
                    return True
    return False


def oracle_asserts(L: Ledger, q: J, G: str) -> bool:
    """An asserting judgment is one base would let support, ignoring vetoes: provisional included."""
    return (not q.adverse and L.acts(q, G) and not L.superseded(q, G)
            and L.status1(q.id) in ("CLEAR", "PROVISIONAL")
            and not (oracle_req(q) and not independent(q.actor, oracle_authors(q))))


def oracle_joins(L: Ledger, j: J, z: J, G: str) -> bool:
    """Protected property: z helps assert, read in either direction and composed with other
    asserting judgments of a covering class, that j's two revisions are equivalent for j's class.
    Enumerates vertex sequences a, ..., b directly instead of searching edges."""
    a, b, c = j.target
    if not covers(z.target[2], c):
        return False
    pairs = {frozenset(q.target[:2]) for q in L.js
             if q is not z and q.kind == "EQ" and oracle_asserts(L, q, G) and covers(q.target[2], c)}
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


def oracle_covers(L: Ledger, j: J, z: J, G: str) -> bool:
    """Boundary completeness composes by union of sub-scopes (§2.6): z helps claim j's scope complete
    when some union of asserting sub-scope judgments of j's class covers it with z and not without.
    Computes every reachable union by dynamic programming over element sets."""
    X, c = SCOPES[j.target[0]], j.target[1]
    if z.target[1] != c or not SCOPES[z.target[0]] <= X:
        return False
    unions = {frozenset()}
    for q in L.js:
        if (q is not z and q.kind == "COMP" and oracle_asserts(L, q, G) and q.target[1] == c
                and SCOPES[q.target[0]] <= X):
            unions |= {u | SCOPES[q.target[0]] for u in unions}
    zs = SCOPES[z.target[0]]
    return any(u | zs == X and u != X for u in unions)


def oracle_sat3(L: Ledger, r: str, k: str, G: str) -> int:
    """The widest-path value, by levels: the highest t such that cur(u) is reachable over hops >= t."""
    if r == CUR:
        return 2
    for t in (2, 1):
        frontier, seen = [r], {r}
        while frontier:
            v = frontier.pop()
            for q in L.js:
                if (q.kind == "EQ" and not q.adverse and q.target[0] == v and covers(q.target[2], k)
                        and q.target[1] not in seen and oracle_base3(L, q, G) >= t):
                    seen.add(q.target[1])
                    frontier.append(q.target[1])
        if CUR in seen:
            return t
    return 0


def oracle_bound(L: Ledger, u: str, G: str) -> str:
    complete = {q.target[0] for q in L.js if q.kind == "COMP" and not q.adverse and q.target[1] == "DEF"
                and oracle_base3(L, q, G) == 2}
    for X in CHAIN[u]:
        if X in complete:
            return X
    return CHAIN[u][-1]


def oracle_disagreement(L: Ledger, j: J, G: str) -> bool:
    """The owner must be asked whenever a standing objection contradicts an acting passing judgment
    for which it is not resolved (relief is per target, so resolution is asked of each judgment)."""
    return any(not z.adverse and z.kind == j.kind and L.acts(z, G) and not L.superseded(z, G)
               and oracle_same(L, j, z, G) and not oracle_resolved(L, j, z, G) for z in L.js)


# ---- scenario generation
def scenarios():
    tgt = {
        "REV": [("i1", "c1", "b1"), ("i2", "c1", "b2"), ("i1", "c2", "b1"), ("k1", "c1", "b1"), ("k2", "c1", "b1"),
                ("i1", "c1v", "b1"), ("i1", "cv2", "b1")],
        "ACC": [("s1", "r1"), ("s1", "r2"), ("s2", "r1")],
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
                    # the owner's adjudication on the objection's own target withdraws it everywhere,
                    # the re-identified subject included (supersession target: the exact target)
                    adv = [j for j in L.js if j.adverse]
                    fix = J("fix", z.kind, adv[0].target if adv else z.target, False, "O", frame,
                            tuple(j.id for j in adv))
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


# ---- composing kinds (§5.10 (b), SD-29): one generic checker over three families
def endings_for(j: J) -> list:
    out = [()]
    for ra, frames in (("O", ("adm", "pend", "aband")), ("H", ("adm", "pend", "aband")), ("P", ("adm",)),
                       ("Q", ("adm",))):
        for rf in frames:
            for sup in (True, False):
                out.append((J("y", j.kind, j.target, False, ra, rf, ("j",) if sup else ()),))
    if j.kind == "EQ":
        other = j.target[:2] + ("K2" if j.target[2] != "K2" else "K",)
        out.append((J("y", "EQ", other, False, "O", "adm", ("j",)),))
    elif j.kind == "COMP":
        out.append((J("y", "COMP", (j.target[0], "GOV" if j.target[1] == "DEF" else "DEF"), False, "O",
                      "adm", ("j",)),))
    for ua in ("H", "O", "U", "A"):
        for up in (True, False):
            out.append((C("c1", "j", "P"), Adj("a1", "c1", up, ua)))
    return out


def provisional(rid: str) -> list:
    """A blocking challenge against rid under an in-force risk override (§10.5)."""
    return [C(f"ch_{rid}", rid, "P"), RO(f"ro_{rid}", f"ch_{rid}")]


# equivalence chains: one unit u with revisions r0..r3, cur(u) = r3
EQ_HOPS = [("h01", ("r0", "r1", "K")), ("h12", ("r1", "r2", "K")), ("h23", ("r2", "r3", "K")),
           ("h13", ("r1", "r3", "K")), ("h02", ("r0", "r2", "ED")), ("h03", ("r0", "r3", "K2"))]
EQ_CONSUMERS = [("r0", "K"), ("r1", "K"), ("r2", "K"), ("r0", "K2"), ("r0", "ED")]


def eq_scenarios():
    hop_sets = []
    for mask in range(1 << len(EQ_HOPS)):
        chosen = dict(h for i, h in enumerate(EQ_HOPS) if mask >> i & 1)
        plain = [J(hid, "EQ", t, False, "P") for hid, t in chosen.items()]
        hop_sets.append(plain)
        if "h12" in chosen:
            for actor, frame in (("U", "adm"), ("A", "adm"), ("P", "pend")):
                hop_sets.append([J(hid, "EQ", t, False, actor if hid == "h12" else "P",
                                   frame if hid == "h12" else "adm") for hid, t in chosen.items()])
            hop_sets.append(plain + provisional("h12"))
            # the author of r1 records the r0 -> r1 change's equivalence with reversed endpoints
            hop_sets.append(plain + [J("h10", "EQ", ("r1", "r0", "K"), False, "A")])
            if "h01" in chosen:
                hop_sets.append(plain + provisional("h12") + provisional("h01"))
    objections = []
    for a, b in itertools.permutations(REVS, 2):
        for cls in ("K", "K2", "ED"):
            for obj in (("H", "P") if cls == "K" else ("H",)):
                objections.append(J("j", "EQ", (a, b, cls), True, obj))
    for hops in hop_sets:
        yield None, hops
        for j in objections:
            for e in endings_for(j):
                yield None, hops + [j] + list(e)


# completeness covers: the pool's scopes and classes, one analyzer declaration
COMP_POOL = [("c1", ("S1", "DEF"), "P"), ("c2", ("S2", "DEF"), "P"), ("c3", ("S3", "DEF"), "P"),
             ("c12", ("S12", "DEF"), "P"), ("cm", ("S12", "DEF"), "M"), ("cg", ("S1", "GOV"), "P")]


def comp_scenarios():
    sets = []
    for mask in range(1 << len(COMP_POOL)):
        chosen = [c for i, c in enumerate(COMP_POOL) if mask >> i & 1]
        ids = {c[0] for c in chosen}
        plain = [J(cid, "COMP", t, False, a) for cid, t, a in chosen]
        sets.append(plain)
        if "c1" in ids:
            for actor, frame in (("A", "adm"), ("P", "pend")):
                sets.append([J(cid, "COMP", t, False, actor if cid == "c1" else a,
                               frame if cid == "c1" else "adm") for cid, t, a in chosen])
        if "c2" in ids:
            sets.append(plain + provisional("c2"))
    objections = [J("j", "COMP", (X, "DEF"), True, o) for X in ("S1", "S2", "S12", "SX") for o in ("H", "P")]
    objections.append(J("j", "COMP", ("S12", "GOV"), True, "H"))
    for recs in sets:
        yield None, recs
        for j in objections:
            for e in endings_for(j):
                yield None, recs + [j] + list(e)


# plan acceptance coverage: items A (tightening chain) and B; issuable iff a supporting acceptance covers cur
def plan_scenarios():
    accs = [("p10ab", (("A", "a10ab"),)), ("p5abc", (("A", "a5abc"),)), ("p6ab", (("A", "a6ab"),)),
            ("px", (("A", "x10ab"),)), ("pab", (("A", "a10ab"), ("B", "b1"))), ("pA2", (("A2", "a2_10ab"),))]
    rejections = [(("A", r),) for r in ITEM_REVS["A"]] + [(("A", "a10ab"), ("B", "b1")), (("B", "b1"),)]
    for cur in ITEM_REVS["A"]:
        for mask in range(1, 1 << len(accs)):
            chosen = [a for i, a in enumerate(accs) if mask >> i & 1]
            for variant in ("P", "U", "pend"):
                if variant != "P" and len(chosen) > 2:
                    continue
                zs = [J(pid, "PLAN", t, False, "U" if variant == "U" and k == 0 else "P",
                        "pend" if variant == "pend" and k == 0 else "adm") for k, (pid, t) in enumerate(chosen)]
                yield cur, zs
                for rej in rejections:
                    j = J("j", "PLAN", rej, True, "H")
                    fresh = [(J("y", "PLAN", (("A", cur),), False, a, f),)
                             for a, fs in (("H", ("adm", "pend")), ("O", ("adm", "pend")), ("P", ("adm",)),
                                           ("Q", ("adm",))) for f in fs]
                    for e in endings_for(j) + fresh:
                        yield cur, zs + [j] + list(e)


def plan_issuable(item: str):
    def model(L: Ledger, G: str) -> int:
        return max([L.base3(z, G) for z in L.js if z.kind == "PLAN" and not z.adverse
                    and any(it == item and tight(r, plan_cur(it)) for it, r in z.target)] or [0])

    def oracle(L: Ledger, G: str) -> int:
        return max([oracle_base3(L, z, G) for z in L.js if z.kind == "PLAN" and not z.adverse
                    and any(it == item and tight(r, plan_cur(it)) for it, r in z.target)] or [0])
    return model, oracle


FAMILIES = {
    # name: (scenarios, [(consumer label, model value, oracle value)])
    "equivalence-chain": (eq_scenarios, [(f"sat({r},{k})", (lambda r, k: lambda L, G: L.sat3(r, k, G))(r, k),
                                          (lambda r, k: lambda L, G: oracle_sat3(L, r, k, G))(r, k))
                                         for r, k in EQ_CONSUMERS]),
    "completeness-cover": (comp_scenarios, [(f"bound({u})", (lambda u: lambda L, G: L.bound(u, G))(u),
                                             (lambda u: lambda L, G: oracle_bound(L, u, G))(u))
                                            for u in ("u1", "u2", "u3")]),
    "plan-coverage": (plan_scenarios, [(f"issuable({it})",) + plan_issuable(it) for it in ("A", "B", "A2")]),
}


def support(outputs: tuple) -> tuple:
    """Invariant (g)2 concerns support, not obligations: a non-independent contrary pass still asks the owner."""
    return tuple(o for o in outputs if not o[0].startswith("adj"))


def fam_outputs(L: Ledger, G: str, consumers, ids=None) -> tuple:
    out = [(z.id, L.base3(z, G)) for z in sorted(L.js, key=lambda r: r.id)
           if not z.adverse and (ids is None or z.id in ids)]
    out += [(name, m(L, G)) for name, m, _o in consumers]
    out += [(f"adj{j.id}", L.adjudicate(j, G)) for j in L.js if j.adverse]
    return tuple(out)


def check_family(name: str, limit_fail: int = 5, verbose: bool = True) -> dict:
    gen, consumers = FAMILIES[name]
    fails: dict[str, int] = {}
    examples: dict[str, list] = {}
    rng = random.Random(11)
    n = 0
    for cur, recs in gen():
        n += 1
        PLAN_CUR[0] = cur or "a5ab"
        L = Ledger(recs)

        def note(inv, msg):
            fails[inv] = fails.get(inv, 0) + 1
            if len(examples.setdefault(inv, [])) < limit_fail:
                examples[inv].append((f"{name} cur={cur} {msg}", list(recs)))

        for G in ("D", "F"):
            for z in L.js:
                if not z.adverse and L.base3(z, G) != oracle_base3(L, z, G):
                    note("I1/I3", f"{G}: base({z.id})={L.base3(z, G)} oracle={oracle_base3(L, z, G)}")
            for cname, m, o in consumers:
                if m(L, G) != o(L, G):
                    note("I1/I3", f"{G}: {cname}={m(L, G)} oracle={o(L, G)}")
            for j in L.js:
                if j.adverse and L.adjudicate(j, G) != oracle_disagreement(L, j, G):
                    note("I8", f"{G}: adjudication obligation {L.adjudicate(j, G)} oracle "
                               f"{oracle_disagreement(L, j, G)}")
        # I2: non-independent records change no support value
        keep = [r for r in recs if not (isinstance(r, J) and not r.adverse and L.nonind(r))]
        ids = {r.id for r in keep}
        L2 = Ledger(keep)
        for G in ("D", "F"):
            if support(fam_outputs(L, G, consumers, ids)) != support(fam_outputs(L2, G, consumers, ids)):
                note("I2", f"{G}: removing nonind records changed support")
        # I4: liftable where it bites
        for G in ("D", "F"):
            frame = "adm" if G == "D" else "pend"
            for j in L.js:
                if not (j.adverse and L.adjudicate(j, G)):
                    continue
                if j.kind == "PLAN" and not all(tight(rv, plan_cur(it)) for it, rv in j.target):
                    fix = [C("cf", "j", "P"), Adj("af", "cf", True, "O")]
                else:
                    fix = [J("fix", j.kind, j.target, False, "O", frame, (j.id,))]
                L3 = Ledger(recs + fix)
                if any(f.id not in L3.adm for f in fix) or L3.adjudicate(j, G) or any(
                        L3.vetoed(z, G) for z in L3.js if z.id != "fix" and not z.adverse):
                    note("I4", f"{G}: objection {j.id} not liftable where it bites")
        # I5: pending/abandoned passing and superseding records change nothing in D
        local = [r for r in recs if not (isinstance(r, J) and not r.adverse and r.frame != "adm")]
        lid = {r.id for r in local}
        if fam_outputs(L, "D", consumers, lid) != fam_outputs(Ledger(local), "D", consumers, lid):
            note("I5", "pending/abandoned records changed the admitted state")
        # I6: admitted set and admitted outputs under two sampled reference-respecting orders
        for _ in range(2):
            perm = recs[:]
            rng.shuffle(perm)
            perm.sort(key=lambda r: (0 if isinstance(r, J) and not r.supersedes else 1 if isinstance(r, J)
                                     else 2 if isinstance(r, C) else 3))
            Lp = Ledger(perm)
            if set(Lp.adm) != set(L.adm) or fam_outputs(Lp, "D", consumers) != fam_outputs(L, "D", consumers):
                note("I6", "admission order changed the admitted set or outputs")
        # I7
        for a in L.ads:
            if (not independent(a.actor, oracle_authors(L.adm["j"]))
                    or ACTORS[a.actor][3] < ACTORS[L.adm["j"].actor][3]):
                note("I7", f"adjudication {a.id} ineligible but admitted")
    PLAN_CUR[0] = "a5ab"
    if verbose:
        print(f"{name} scenarios: {n}")
    return {"n": n, "fails": fails, "examples": examples}


CORE = "transformation-review/acceptance/gate"
MUTATIONS = {
    # name: (families it changes, what it re-introduces)
    "relief_ignores_nonind": ((CORE,), "a non-independent owner pass relieves (9e5a763 B1)"),
    "wide_review_supersession": ((CORE,), "review supersession on same content, any item/base (051cce3 B1)"),
    "eligibility_support_tier_only": ((CORE,), "eligibility checked only on direct challenges (29da56e B1)"),
    "challenged_record_authors": ((CORE,), "eligibility against the challenged record, not the root (6b986de B1)"),
    "gate_run_veto": ((CORE,), "gate veto keyed on the run-parameterized obligation (362af9f B1-A)"),
    "frame_acts_everywhere": ((CORE,), "frame records act in the admitted state (b46c250 B1)"),
    "base_ignores_nonind": ((CORE,), "base ignores non-independence (29da56e B1(g))"),
    "no_class_check": ((CORE,), "adjudication class not checked (51070e5 B1)"),
    "endpoint_only_equivalence_reach": (("equivalence-chain",),
                                        "equivalence veto reaches only the same endpoints (a6ed164 B1)"),
    "directed_chain_only": (("equivalence-chain",),
                            "an objection blocks only chains read in their recorded direction (a6ed164 B1)"),
    "chain_ignores_class": (("equivalence-chain",),
                            "an objection blocks chains whose hops do not cover its class (a6ed164 B1 controls)"),
    "obligation_direct_only": (("equivalence-chain",), "a blocked chain derives no adjudication (a6ed164 B1)"),
    "plan_reach_names_only": (("plan-coverage",),
                              "a plan rejection reaches only acceptances naming its revision (bf23372 R14 sibling)"),
    "plan_reach_any_tighter": (("plan-coverage",),
                               "a plan rejection reaches only acceptances below it, without inheritance (bf23372 N1)"),
    "asserts_requires_clear": (("equivalence-chain", "completeness-cover"),
                               "asserts stricter than base: provisional hops compose unvetoed (bf23372 B1(c))"),
    "completeness_exact_only": (("completeness-cover",),
                                "an INCOMPLETE reaches only the same scope, not a union of sub-scopes (bf23372 B1(a))"),
    "completeness_reach_analyzer_id": (("completeness-cover",),
                                       "the analyzer identity is compared by the reach (bf23372 B1(b))"),
    "requirement_request_colocated": (("equivalence-chain", "completeness-cover"),
                                      "equivalence/completeness requirement only for a co-submitted change (bf23372 B2)"),
    "plan_reach_current_only": (("plan-coverage",),
                                "a plan rejection reaches only coverage of the current revision (34803df B1)"),
    "plan_rejection_denies_set": (("plan-coverage",),
                                  "a plan rejection denies its named set only as a whole (34803df B1(b))"),
    "plan_reach_path_only": (("plan-coverage",),
                             "a plan rejection reaches only acceptances below it on the path to cur (0d2b35e B1)"),
    "plan_fresh_acceptance_exempt": (("plan-coverage",),
                                     "any acceptance of a revision tighter than the rejected one is exempt (83a82df B1)"),
    "plan_no_relief": (("plan-coverage",), "plan acceptance has no per-target relief (83a82df option 2)"),
    "plan_reach_same_item_only": (("plan-coverage",),
                                  "a plan rejection reaches only acceptances of the same item (5895687 B1)"),
    "gate_basis_record_all": (("gate-basis",),
                              "record mode on every record of the evidence core shown (d94a293 B1)"),
    "revision_assessment_record_mode": (("gate-basis",),
                                        "a decision imports the revision assessment's currency, not its standing (653e88c B1)"),
    "gate_basis_identity_all": (("gate-basis",),
                                "identity mode on the gate's required premises too (d94a293 negative control)"),
    "revalidate_after_integration": (("obligation-routing",),
                                     "REVALIDATE of an integrated review or task result (SD-37/SD-38 waiting route; SD-40)"),
    "r2_instead_clause": (("obligation-routing",),
                          "an R2 amendment of an integrated obligation routed to the principal instead (eb86a71 B1(a))"),
    "rebase_before_first_only": (("obligation-routing",),
                                 "a pending candidate of an integrated obligation re-dispatched over (eb86a71 B1(b))"),
    "pending_ignored": (("obligation-routing",),
                        "the list ignores a pending candidate of an integrated obligation (eb86a71 B1(b))"),
    "kept_fence_persists": (("obligation-routing",),
                            "a kept fence's route outlives its decision (eb86a71 B1(c))"),
    "item_review_parts_discharged": (("obligation-routing",),
                                     "an adverse item-level review iterates parts that stay discharged (eb86a71 B1(e))"),
    "decline_allowed_for_items": (("obligation-routing",),
                                  "a DECLINE answers an item obligation's decision and leaves it OPEN (eb86a71 N2)"),
    "review_reach_changed_only": ((CORE,),
                                  "a review veto reaches only the same changed content, not output entries (b365947 B2)"),
    "acceptance_reach_by_content": ((CORE,),
                                    "an acceptance veto keyed on content across subjects, against S10 (edabd81 N2)"),
    "review_reach_item_or_prose": ((CORE,),
                                   "a review veto reaches re-identified items only with identical prose and contract (913db8f B1)"),
    "review_reach_same_item_only": ((CORE,),
                                    "a review veto reaches only the same plan item, not a re-identified one (5895687 B1(b))"),
    "plan_cur_join": (("plan-coverage",),
                      "a plan rejection reaches incomparable acceptances only while cur joins them (4c52205 B1)"),
    "plan_revert_exemption": (("plan-coverage",),
                              "a revert or loosening below a rejected revision releases it (e548472 B1)"),
    "plan_supersession_current_only": (("plan-coverage",),
                                       "a plan rejection is superseded only while its revisions are current (0d2b35e N1)"),
    "eq_authors_to_side_only": (("equivalence-chain",),
                                "equivalence authors measured on r_to's differing content only (34803df B2)"),
}


# ---- gate basis (§4.3, §5.5, §16.6; SD-35): a gate decision's basis from the evidence core shown
GATE_BASIS = "gate-basis"


class OutOfDomain(Exception):
    """current() asked of a record outside its domain (support-tier and observation records)."""


def gate_basis(core: list) -> tuple:
    """core: [(record id, role)], role required | revision | shown. SD-35: record only on the
    required supporting premises; identity on every other displayed item."""
    out = []
    for rid, role in core:
        if "gate_basis_record_all" in MUT:  # d94a293 B1: record on every record of the core shown
            mode = "record"
        elif "gate_basis_identity_all" in MUT:  # negative control: required support dropped
            mode = "identity"
        elif role == "required":
            mode = "record"
        elif role == "revision":  # §4.1 standing: the decision relies on the assessment standing (item 31)
            mode = "record" if "revision_assessment_record_mode" in MUT else "standing"
        else:
            mode = "identity"
        out.append((mode, rid))
    return tuple(out)


def current3(L: Ledger, x, G: str) -> int:
    """§5.5 current(x) = base(x) ∧ ⋀ sat(e), sat(record y) = current(y), sat(identity y) = T."""
    if not isinstance(x, J):
        raise OutOfDomain(getattr(x, "id", "?"))
    v = L.base3(x, G)
    for mode, rid in x.basis:
        if mode == "identity":
            continue
        y = L.adm.get(rid)
        if not isinstance(y, J):
            raise OutOfDomain(rid)
        v = min(v, L.base3(y, G) if mode == "standing" else current3(L, y, G))  # sat(standing y) = base(y)
    return v


def gate_basis_scenarios():
    for fe, ce, ra, rd, n, cn, r, sup, actor in itertools.product(
            ("adm", "pend"), (False, True), (None, "adm", "pend"), ("adm", "pend"), (None, "adm", "pend"),
            (False, True), (None, "adm", "aband"), (False, True), ("H", "O")):
        if (cn and n is None) or (sup and r is None) or (ra is None and rd == "pend"):
            continue
        recs = [J("e", "EV", ("ev",), False, "P", fe)]
        core = [("e", "required")]
        if ce:
            recs.append(C("c_e", "e", "P"))
            core.append(("c_e", "shown"))
        if ra:
            # the revision assessment is a task result with its own basis: a read the reviser made,
            # which a later governing or read change makes non-current (rd pending: stale in D)
            recs.append(J("rd", "EV", ("read",), False, "P", rd))
            recs.append(J("ra", "RA", ("r1",), False, "P", ra, (), (("record", "rd"),)))
            core.append(("ra", "revision"))
        if n:
            recs.append(J("n", "EV", ("ev2",), False, "P", n))
            core.append(("n", "shown"))
        if cn:
            recs.append(C("c_n", "n", "P"))
            core.append(("c_n", "shown"))
        if r:
            recs.append(J("r", "GATE", ("r1", "p2"), True, "H", r))
            core.append(("r", "shown"))
        recs.append(J("h", "GATE", ("r1", "p2"), False, actor, "adm", ("r",) if sup else (), gate_basis(core)))
        yield core, recs


def oracle_gate(L: Ledger, h: J, core: list, G: str) -> int:
    """The gate supports as its own standing allows, capped by its required premises only;
    what is merely shown never lowers it (the protected property behind SD-35)."""
    v = L.base3(h, G)
    for rid, role in core:
        if role in ("required", "revision"):
            v = min(v, oracle_base3(L, L.adm[rid], G))
    return v


def check_gate_basis(limit_fail: int = 5, verbose: bool = True) -> dict:
    fails: dict[str, int] = {}
    examples: dict[str, list] = {}
    n = 0
    for core, recs in gate_basis_scenarios():
        n += 1
        L = Ledger(recs)

        def note(inv, msg):
            fails[inv] = fails.get(inv, 0) + 1
            if len(examples.setdefault(inv, [])) < limit_fail:
                examples[inv].append((f"gate-basis {msg}", list(recs)))
        h = L.adm.get("h")
        if h is None:
            note("I1/I3", "the gate decision was not admitted")
            continue
        for G in ("D", "F"):
            try:
                got = current3(L, h, G)
            except OutOfDomain as e:
                note("I9", f"{G}: current() of {e} outside its domain")
                continue
            want = oracle_gate(L, h, core, G)
            if got != want:
                note("I1/I3", f"{G}: current(h)={got} oracle={want}")
            # I10 liveness: while the assessment counts and the required evidence holds, a fresh
            # gate decision on the same core is admissible (its basis holds), so GATE is answerable
            premises = min([oracle_base3(L, L.adm[rid], G) for rid, role in core if role in ("required", "revision")])
            if premises > 0 and not any(isinstance(L.adm.get(x), J) and L.adm[x].adverse for x in ("r",)):
                fresh = J("h2", "GATE", ("r1", "p2"), False, "O", "adm", (), gate_basis(core))
                L2 = Ledger(recs + [fresh])
                try:
                    if "h2" in L2.adm and current3(L2, L2.adm["h2"], G) == 0:
                        note("I10", f"{G}: GATE ready but no admissible answer (fresh decision not current)")
                except OutOfDomain:
                    pass
    if verbose:
        print(f"{GATE_BASIS} scenarios: {n}")
    return {"n": n, "fails": fails, "examples": examples}


ROUTING = "obligation-routing"
# Routes of an item obligation (§10.4, SD-36 to SD-40), over a state with an integrated enactment, an
# optional single pending candidate, fences, the iteration budget, amendments, the principal's decisions
# and a two-part partition modelled as one obligation. claims() adds another section's route only under
# a mutation re-introducing an earlier round's defect: unmutated, the list is compared with itself, not
# with the other sections' current text (b365947 N1; SD-41 accepted the routing residual by a bounded stop).
RT_EVENTS = (
    "move_out",          # a later change moves out(o)
    "move_read",         # a later change moves only what the reviews read
    "adverse_in",        # a standing adverse review of the latest integrated enactment, findings in scope
    "adverse_out",       # ... with findings outside the item's write scope or obligations
    "peer_veto",         # a peer's adverse review whose veto awaits the owner
    "r1_tighten",        # an R1 tightening adding a HARD check the integrated content fails
    "r2_amend",          # an R2 amendment: a new key and so a new obligation
    "dispatch",          # the item's route is taken: a new task, whose candidate is then pending
    "cand_pass",         # the pending candidate's result is clean and its review passes
    "cand_nopass",       # ... its review is NO_PASS with findings in scope
    "cand_incomplete",   # ... its result is INCOMPLETE
    "cand_discrepancy",  # ... its conformance has a DISCREPANCY
    "cand_rebase_conflict", "cand_rebase_read",  # a rebase conflicting with its own units / over a read
    "cand_revalidate",   # the candidate's reviewer revalidates it
    "cand_integrate",    # the pending candidate integrates
    "fence", "keep_fence", "reapply_fence",  # the latest integration fenced; the human keeps it / re-applies
    "decide_amend",      # the principal's AMEND answers an owed decision (withdrawal included)
    "decide_decline",    # the principal's DECLINE
    "item_review_adverse_p1", "item_review_adverse_none",  # partitioned: findings naming part 1 / no part
)
RT_BUDGET = 3


def rt_scenarios():
    evs = list(RT_EVENTS)
    for kind in ("IMPLEMENT", "PARTITIONED", "FIRST"):
        yield kind, ()
        for n in (1, 2, 3):
            for seq in itertools.product(evs, repeat=n):
                yield kind, seq


class RtState:
    def __init__(self, kind):
        self.kind = kind
        self.integrated = kind != "FIRST"
        self.discharged_base = self.integrated  # the latest integrated enactment's predicate held
        self.moved = False
        self.read_moved = False
        self.adverse = None        # None | "in" | "out"
        self.veto_open = False
        self.tightened = False
        self.retired = False       # an R2 amendment or a withdrawal ended this obligation
        self.iterations = 1
        self.cand = {"state": "review"} if kind == "FIRST" else None
        self.fence = None          # None | "await" | "kept" | "decided"
        self.coord_answered = set()
        self.declined = set()
        self.parts_adverse = None  # partition: None | "p1" | "none"

    # -- the predicate of the latest integrated enactment (§10.4) --
    def holds(self):
        return self.integrated and self.discharged_base and not self.moved and not self.read_moved \
            and self.adverse is None and not self.veto_open and not self.tightened \
            and self.parts_adverse is None

    def budget_left(self):
        return self.iterations < RT_BUDGET

    def cand_routes(self):
        """A pending candidate's ordinary routes (before integration, §11.5, §13.7, §4.1)."""
        c = self.cand["state"]
        if c == "discrepancy":
            return {"COORDINATE:discrepancy"}
        if c in ("nopass", "incomplete", "conflict"):
            return {"ITERATE"} if self.budget_left() else {"COORDINATE:budget"}
        if c == "stale":
            return {"REVALIDATE:candidate"}
        if c == "review":
            return {"REVIEW:candidate"}
        if c == "clean":
            return {"INTEGRATE:candidate"}
        return set()

    def list_route(self):
        """§10.4's ordered list: the first that applies is the only route."""
        if self.retired:
            return ("RETIRED", set())
        if self.fence == "await":
            return ("OPEN", {"HUMAN_FENCE_DECISION"})
        if self.fence == "kept" and "fence" not in self.coord_answered:
            return ("OPEN", {"COORDINATE:fence"})
        if self.holds():
            return ("DISCHARGED", set())
        if self.cand is not None and "pending_ignored" not in MUT:
            return ("OPEN", self.cand_routes())
        if not self.integrated:
            return ("OPEN", {"DISPATCH"})
        if self.parts_adverse == "none":
            return ("OPEN", set() if "budget" in self.coord_answered and False else {"COORDINATE:item_review"})
        if self.adverse == "out":
            return ("OPEN", {"COORDINATE:out_of_scope"})
        if not self.budget_left():
            return ("OPEN", {"COORDINATE:budget"})
        return ("OPEN", {"REDISPATCH"})

    # -- each section's own claim, as that section states it --
    def claims(self):
        out = set()
        st, route = self.list_route()
        if self.retired:
            return out
        # §10.2 REVALIDATE row and §4.1: none for an integrated obligation's review or task result (SD-40)
        if "revalidate_after_integration" in MUT and self.integrated and (self.read_moved or self.tightened) \
                and self.cand is None:
            out.add("REVALIDATE:integrated")
        # §10.2 COORDINATE row and §4.1: an R2 amendment of an integrated obligation routes to the
        # principal "instead" (the eb86a71 clause), unless deleted
        if "r2_instead_clause" in MUT and getattr(self, "r2_seen", False):
            out.add("COORDINATE:r2")
        # §11.5: a pending candidate's rebase routes, read as applying only before first integration
        if "rebase_before_first_only" in MUT and self.cand is not None and self.integrated:
            out.add("REDISPATCH")
        # §22.3: the human's fence decision and a kept fence's COORDINATE(plan); with "re-apply" as an
        # outcome, a decided kept fence would keep its route (eb86a71 B1 (c))
        if "kept_fence_persists" in MUT and self.fence == "decided":
            out.add("COORDINATE:fence")
        # §13.7: an adverse item-level review iterates the parts it names; without the part's predicate
        # failing, the part's own list holds it discharged (eb86a71 B1 (e))
        if "item_review_parts_discharged" in MUT and self.parts_adverse == "p1":
            out.add("ITERATE:part_without_carrier")
        return out

    def item(self):
        st, route = self.list_route()
        return st, route | self.claims()


def rt_derive(kind, seq):
    st = RtState(kind)
    for e in seq:
        state, routes = st.item()
        if st.retired:
            break
        if e == "move_out" and st.integrated:
            st.moved = True
        elif e == "move_read" and st.integrated:
            st.read_moved = True
            if st.cand is not None and st.cand["state"] in ("review", "clean"):
                st.cand["state"] = "stale"
        elif e == "adverse_in" and st.integrated:
            st.adverse = "in"
        elif e == "adverse_out" and st.integrated:
            st.adverse = "out"
        elif e == "peer_veto" and st.integrated:
            st.veto_open = True
        elif e == "r1_tighten" and st.integrated:
            st.tightened = True
        elif e == "r2_amend":
            st.r2_seen = True
            if "r2_instead_clause" not in MUT:
                st.retired = True  # a new key: this obligation is no longer derived; the new one is dispatched
        elif e == "dispatch":
            if routes & {"REDISPATCH", "DISPATCH", "ITERATE"} and st.cand is None:
                st.cand = {"state": "review"}
                st.iterations += 1
            elif "ITERATE" in routes and st.cand is not None:
                st.cand = {"state": "review"}
                st.iterations += 1
        elif e in ("cand_pass", "cand_nopass", "cand_incomplete", "cand_discrepancy",
                   "cand_rebase_conflict", "cand_rebase_read"):
            if st.cand is not None and st.cand["state"] in ("review", "clean", "stale"):
                st.cand["state"] = {"cand_pass": "clean", "cand_nopass": "nopass", "cand_incomplete": "incomplete",
                                    "cand_discrepancy": "discrepancy", "cand_rebase_conflict": "conflict",
                                    "cand_rebase_read": "stale"}[e]
        elif e == "cand_revalidate":
            if st.cand is not None and st.cand["state"] == "stale":
                st.cand["state"] = "clean"
        elif e == "cand_integrate":
            if st.cand is not None and st.cand["state"] == "clean" and st.fence in (None, "decided"):
                st.cand = None
                st.integrated = True; st.discharged_base = True
                st.moved = st.read_moved = st.tightened = False
                st.adverse = None; st.veto_open = False; st.parts_adverse = None
        elif e == "fence":
            if st.integrated and st.fence is None:
                st.fence = "await"
        elif e == "keep_fence":
            if st.fence == "await":
                st.fence = "kept"; st.moved = True  # the fence restores the earlier tree: out(o) moved
        elif e == "reapply_fence":
            if st.fence == "await":
                st.fence = None  # an ordinary revalidated admission onto the fence: the integration stands
        elif e == "decide_amend":
            if any(r.startswith("COORDINATE") for r in routes):
                if "COORDINATE:fence" in routes:
                    st.coord_answered.add("fence"); st.fence = "decided"
                st.retired = True  # an AMEND: an R2 amendment or a withdrawal ends this obligation
        elif e == "decide_decline":
            if "COORDINATE:fence" in routes:
                st.coord_answered.add("fence"); st.fence = "decided"  # resume: the item's own route follows
            elif any(r.startswith("COORDINATE") for r in routes):
                if "decline_allowed_for_items" in MUT:
                    st.declined |= {r for r in routes if r.startswith("COORDINATE")}
                    st.coord_answered |= {r.split(":")[1] for r in routes if r.startswith("COORDINATE")}
                    if "COORDINATE:fence" in routes:
                        st.fence = "decided"
        elif e in ("item_review_adverse_p1", "item_review_adverse_none"):
            if st.kind == "PARTITIONED" and st.integrated:
                st.parts_adverse = "p1" if e.endswith("p1") else "none"
    state, routes = st.item()
    if "decline_allowed_for_items" in MUT and st.declined and state == "OPEN":
        routes = {r for r in routes if r not in st.declined}  # a declined decision is answered: no route
    return {"ITEM": (state, routes)}, st


def check_routing(limit_fail: int = 5, verbose: bool = True) -> dict:
    """Properties over §10.4's list (and, under a mutation, an earlier round's section claim). I13 every
    OPEN obligation has a route. I14 exactly one route. I15 an integrated
    obligation whose predicate fails is never waiting on a REVALIDATE of its integrated review or task
    result (SD-40), and is re-dispatched within budget unless a fence, a pending candidate or a
    principal's decision comes first. I18 a pending candidate is never discarded, a kept fence's route ends
    once decided, and an adverse item-level review naming a part never leaves the item discharged."""
    fails: dict[str, int] = {}
    examples: dict[str, list] = {}
    n = 0

    def fail(inv, msg):
        fails[inv] = fails.get(inv, 0) + 1
        if len(examples.setdefault(inv, [])) < limit_fail:
            examples[inv].append((msg, []))
    for kind, seq in rt_scenarios():
        n += 1
        obs, st = rt_derive(kind, seq)
        state, routes = obs["ITEM"]
        tag = f"{ROUTING} {kind} {seq}"
        if state == "OPEN" and not routes:
            fail("I13", f"{tag}: OPEN with no route")
        if state == "OPEN" and len(routes) > 1:
            fail("I14", f"{tag}: several routes {sorted(routes)}")
        if any(r == "REVALIDATE:integrated" for r in routes):
            fail("I15", f"{tag}: REVALIDATE of an integrated review or task result")
        if state == "OPEN" and st.integrated and st.cand is None and not st.fence in ("await", "kept") \
                and st.budget_left() and st.adverse != "out" and st.parts_adverse != "none" \
                and routes != {"REDISPATCH"}:
            fail("I15", f"{tag}: a reopened integrated item not re-dispatched {sorted(routes)}")
        if st.cand is not None and "REDISPATCH" in routes:
            fail("I18", f"{tag}: re-dispatched while a candidate is pending, discarding it")
        if st.fence == "decided" and "COORDINATE:fence" in routes:
            fail("I18", f"{tag}: a kept fence's route outlives its decision")
        if st.kind == "PARTITIONED" and st.parts_adverse == "p1" and state == "DISCHARGED":
            fail("I18", f"{tag}: an adverse item-level review naming a part leaves the item discharged")
    if verbose:
        print(f"{ROUTING} scenarios: {n}")
    return {"n": n, "fails": fails, "examples": examples}


def run_family(name: str, verbose: bool = True) -> dict:
    if name == GATE_BASIS:
        return check_gate_basis(verbose=verbose)
    if name == ROUTING:
        return check_routing(verbose=verbose)
    return check_all(verbose=verbose) if name == CORE else check_family(name, verbose=verbose)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--mutations", action="store_true", help="also check that each mutation is caught")
    args = ap.parse_args()
    MUT.clear()
    results = [run_family(f) for f in (CORE,) + tuple(FAMILIES) + (GATE_BASIS, ROUTING)]
    ok = not any(r["fails"] for r in results)
    if ok:
        print("unmutated §5.10 rules: every modelled invariant holds")
    else:
        print("unmutated §5.10 rules: INVARIANT FAILURES", [r["fails"] for r in results])
        for r in results:
            for inv, ex in r["examples"].items():
                for msg, recs in ex[:2]:
                    print(" ", inv, msg)
                    for rec in recs:
                        print("     ", rec)
    if args.mutations:
        for m, (fams, why) in MUTATIONS.items():
            MUT.clear()
            MUT.add(m)
            # a mutation changes only the code of the families it names, so only those are re-run
            caught = sorted({inv for f in fams for inv in run_family(f, verbose=False)["fails"]})
            print(f"mutation {m}: {'caught by ' + ', '.join(caught) if caught else 'NOT CAUGHT'} ({why})")
            ok = ok and bool(caught)
        MUT.clear()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
