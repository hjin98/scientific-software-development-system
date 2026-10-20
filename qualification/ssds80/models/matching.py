"""G2 Stage S step S5, catalogue §6: the two matching predicates and mechanical staleness.

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

A run records its execution basis once (Manual §6.3, R1): the tree-resident terms it read with
their content identities under its own resolution context, its external pins, whether it read an
unpinnable input, its recorded execution attributes, and whether its basis is bounded. The settled
predicates (catalogue §6.5):

  on⁻(o, K)   every recorded tree-resident term re-resolves in K, under o's own context, to its
              recorded identity                                        (adverse uses)
  ext(o, x)   neither read an unpinnable input, same complete pin set, same recorded attributes
  bound(o)    o's basis is bounded by completeness judgments that hold for the content matched (SD-58);
              abstracted here as one boolean per observation, so the bounding currency itself is
              exercised at the real derivation owner, not in this model
  on⁺(o, K)   on⁻(o, K) ∧ ext(o, real) ∧ bound(o)                      (permissive uses)
  link⁻(o, K) some admitted run o' of the configuration has on⁻(o', K) and on⁻(o', tree(o))

and staleness for a mechanical oracle (§6.6): (1) a standing run o ≠ real with on⁺(o, tree(real))
reproduced the outcome; (2) every run linked to tree(real) had that outcome; (3) a standing run has
on⁺ on the state's content; (4) no run linked to the state's content yields the failure.

Readings the Reviews refuted are parameters: adverse predicates that also compare pins or free
attributes (c6da678 B1, 53669a5 B1, d837363 B1), an unpinnable read treated as matching (1ffbbf0 B1),
re-resolution under the current context (6ff4ed1 B1, cc005db B2), and adverse uses without the
linking predicate (0b6c4fa B1, 5c55d4b B1).
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Run:
    name: str
    tree: tuple[tuple[str, int], ...]           # path -> content
    reads: tuple[str, ...]                      # tree-resident paths recorded (all paths if unbounded)
    pins: frozenset = frozenset()
    unpinnable: bool = False
    attrs: tuple = ()
    bounded: bool = True
    outcome: str = "bad"                        # "bad" yields the failure, "good" does not
    context: str = "ctx1"                       # resolution context recorded by value
    standing: bool = True

    def t(self) -> dict:
        return dict(self.tree)


def cid(path, tree, ctx):
    """Content identity of a recorded term under a context: a context change alters how some paths
    resolve (an analyzer re-resolving a symbol), modelled by suffixing the content."""
    v = tree.get(path)
    return None if v is None else (v, ctx if path.endswith(".sym") else "")


@dataclass
class Reading:
    adverse_compares_pins: bool = False
    adverse_compares_attrs: bool = False
    unpinnable_matches: bool = False
    current_context: str | None = None          # re-resolve under this context instead of the run's
    use_link: bool = True


SETTLED = Reading()


def on_minus(o: Run, K: dict, r: Reading, real: Run | None = None) -> bool:
    ctx_now = r.current_context or o.context
    ok = all(cid(p, K, ctx_now) == cid(p, o.t(), o.context) for p in o.reads)
    if real is not None and r.adverse_compares_pins:
        ok = ok and o.pins == real.pins
    if real is not None and r.adverse_compares_attrs:
        ok = ok and o.attrs == real.attrs
    return ok


def ext(o: Run, x: Run, r: Reading) -> bool:
    if (o.unpinnable or x.unpinnable) and not r.unpinnable_matches:
        return False
    return o.pins == x.pins and o.attrs == x.attrs


def on_plus(o: Run, K: dict, real: Run, r: Reading) -> bool:
    ctx_now = o.context                          # permissive use always reads the record's own context
    terms = all(cid(p, K, ctx_now) == cid(p, o.t(), o.context) for p in o.reads)
    return terms and ext(o, real, r) and o.bounded


def link_minus(o: Run, K: dict, runs: list, real: Run, r: Reading) -> bool:
    if not r.use_link:
        return on_minus(o, K, r, real)
    return any(on_minus(p, K, r, real) and on_minus(p, o.t(), r, real) for p in runs)


def stale(real: Run, runs: list, state: dict, r: Reading = SETTLED) -> bool:
    ta = real.t()
    others = [o for o in runs if o.name != real.name]
    c1 = any(o.standing and on_plus(o, ta, real, r) and o.outcome == real.outcome for o in others)
    c2 = all(o.outcome == real.outcome for o in runs if link_minus(o, ta, runs, real, r))
    c3 = any(o.standing and on_plus(o, state, real, r) for o in runs)
    c4 = not any(o.outcome == "bad" for o in runs if link_minus(o, state, runs, real, r))
    return c1 and c2 and c3 and c4


def implication_holds(runs: list, trees: list, real: Run, r: Reading) -> bool:
    """on⁺ ⇒ on⁻ for every run and content (R1, 'by construction')."""
    return all((not on_plus(o, K, real, r)) or on_minus(o, K, r) for o in runs for K in trees)
