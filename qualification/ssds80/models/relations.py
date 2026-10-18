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
