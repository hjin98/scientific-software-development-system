"""G2 Stage S step S5, catalogue §2 and §4.6: cycle legality and the closure algorithm.

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

* Cycle legality (Manual §2.4): every cycle among authored relations other than CHALLENGES, and
  derived relations that are not NEUTRAL, lies inside one simultaneous-definition group and uses
  only SIMULTANEOUS edges. Checked by enumerating strongly connected components.
* Closure (Manual §4.6): the least fixed point of following R-prerequisites and, for each reached
  unit, adding the smallest scope of its enclosing-scope chain that a current COMPLETE judgment
  bounds, or the whole tree (UNBOUNDED) where none does. Checked for order independence and for the
  conservative direction (a lost judgment only widens).
"""

from __future__ import annotations

import itertools


def sccs(nodes, edges):
    """Tarjan's strongly connected components; edges: set of (a, b)."""
    index, low, stack, on, out, counter = {}, {}, [], set(), [], [0]
    adj = {n: [b for a, b in edges if a == n] for n in nodes}

    def visit(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        on.add(v)
        for w in adj[v]:
            if w not in index:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = set()
            while True:
                w = stack.pop()
                on.discard(w)
                comp.add(w)
                if w == v:
                    break
            out.append(comp)
    for n in nodes:
        if n not in index:
            visit(n)
    return out


def legal(nodes, relations, sdgs) -> bool:
    """relations: (subject, object, cycle_class, kind) with kind "authored"/"derived" and type name in
    cycle_class position for CHALLENGES; sdgs: list of member sets."""
    edges = {(s, o) for s, o, cc, kind in relations
             if not (cc == "CHALLENGES") and not (kind == "derived" and cc == "NEUTRAL")}
    for comp in sccs(nodes, edges):
        cyc = len(comp) > 1 or any((n, n) in edges for n in comp)
        if not cyc:
            continue
        inside = [r for r in relations if r[0] in comp and r[1] in comp and (r[0], r[1]) in edges]
        if not any(comp <= g for g in sdgs):
            return False
        if any(cc != "SIMULTANEOUS" for _, _, cc, _ in inside):
            return False
    return True


def closure(start, prereqs, chains, complete, tree):
    """prereqs: unit -> set of units; chains: unit -> ordered list of scopes (sets), smallest first,
    ending with the whole tree; complete: set of frozenset scopes with a current COMPLETE judgment."""
    reached, queue = set(start), list(start)
    unbounded = False
    while queue:
        u = queue.pop()
        new = set(prereqs.get(u, set()))
        bound = next((x for x in chains[u] if frozenset(x) in complete), None)
        if bound is None:
            bound, unbounded = tree, True
        new |= set(bound)
        for v in new - reached:
            reached.add(v)
            queue.append(v)
    return frozenset(reached), unbounded


def closure_order_independent(start, prereqs, chains, complete, tree) -> bool:
    results = set()
    for perm in itertools.permutations(sorted(start)):
        results.add(closure(list(perm), prereqs, chains, complete, tree))
    return len(results) == 1


# --- §5.5-§5.6: the support tier as a monotone system with the SCC clamp ---------------------------

ORDER = {"F": 0, "P": 1, "T": 2}
NAME = {0: "F", 1: "P", 2: "T"}


def evaluate_support(nodes, deps, base, clamp=True):
    """nodes: names; deps: node -> list of nodes it needs (all must hold: min); base: node -> F/P/T.
    Settled (Manual §5.6, R2): every node of a non-trivial strongly connected component is forced to
    F before anything else; the rest is evaluated once in dependency order (the least fixed point).
    clamp=False is the reviewed workplan's literal reading, iterating from the top, under which a
    self-supporting cycle can stay above F."""
    edges = {(a, b) for a in nodes for b in deps.get(a, [])}
    val = {}
    if clamp:
        for comp in sccs(nodes, edges):
            if len(comp) > 1 or any((n, n) in edges for n in comp):
                for n in comp:
                    val[n] = 0
    # greatest-from-top iteration for unclamped nodes reproduces the self-support hazard
    cur = {n: val.get(n, ORDER[base[n]]) for n in nodes}
    for _ in range(len(nodes) + 1):
        for n in nodes:
            if n in val:
                continue
            cur[n] = min([ORDER[base[n]]] + [cur[d] for d in deps.get(n, [])])
    return {n: NAME[v] for n, v in cur.items()}
