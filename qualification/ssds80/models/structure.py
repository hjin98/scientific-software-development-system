"""G2 Stage S step S5, catalogue §1: partition by construction and the effect-keyed write set.

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

Two small models, each with the earlier readings the Reviews refuted and the catalogue's settled one:

* Partition (catalogue §1.4; Manual §1.4, R5). A file is a sequence of byte positions; each unit's
  declared term resolves to an interval or ABSENT; membership is a forest. Settled: innermost
  ownership is decided first over every non-ABSENT region, whether or not the units are related by
  membership; regions of units not nested by membership that coincide or partially overlap both
  resolve to ABSENT, as does a member region outside its composite's, in one pass without cascade;
  residual parts and the uncovered region receive only bytes still unowned.
* Write set (catalogue §1.2; Manual §1.2, SD-14). A tree is a set of paths with content; units own
  paths under prefix or path terms, minus ignored paths. Settled: the write set compares the current
  observed tree with the merged tree, at the head where the check runs, by owned content (never by
  position) and declarations, so a governed-boundary change, a new part, or the combination of a
  change with concurrently admitted work counts against the unit it reaches, and concurrent work does
  not.
"""

from __future__ import annotations

from dataclasses import dataclass


# --- partition -----------------------------------------------------------------------------------

@dataclass(frozen=True)
class Unit:
    name: str
    region: tuple[int, int] | None      # resolved [start, end) or None for ABSENT
    parent: str | None = None           # membership (part_of)
    composite: bool = False


def _ancestors(units: dict, name: str) -> set:
    out, p = set(), units[name].parent
    while p is not None:
        out.add(p)
        p = units[p].parent
    return out


def _contains(a, b) -> bool:
    return a[0] <= b[0] and b[1] <= a[1]


def resolve_absent(units: dict, equal_absent: bool = True) -> dict:
    """Settled one-pass ABSENT rule (no cascade): equal or partially overlapping regions of units
    not nested by membership, and a member region outside its composite's, resolve to ABSENT.
    equal_absent=False is 3540d98 B4's reading, in which only partial overlap is ABSENT."""
    absent = set()
    names = [n for n, u in units.items() if u.region is not None]
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            ra, rb = units[a].region, units[b].region
            related = a in _ancestors(units, b) or b in _ancestors(units, a)
            if related:
                continue
            overlap = ra[0] < rb[1] and rb[0] < ra[1]
            if not overlap:
                continue
            if (ra == rb and equal_absent) or not (_contains(ra, rb) or _contains(rb, ra)):
                absent |= {a, b}
    for n in names:
        p = units[n].parent
        if p is not None and units[p].region is not None and not _contains(units[p].region, units[n].region):
            absent.add(n)
    return {n: (None if n in absent else u.region) for n, u in units.items()}


def owners_settled(units: dict, size: int, equal_absent: bool = True) -> list:
    regions = resolve_absent(units, equal_absent)
    out = []
    for pos in range(size):
        holders = [n for n, r in regions.items() if r is not None and r[0] <= pos < r[1]]
        if not holders:
            out.append("UNCOVERED")      # includes bytes of a composite set to ABSENT no member owns
            continue
        inner = min(holders, key=lambda n: regions[n][1] - regions[n][0])
        smallest = [n for n in holders if regions[n] == regions[inner]]
        if len(smallest) > 1:            # cannot happen after resolve_absent; kept as a self-check
            out.append(("CONFLICT", tuple(sorted(smallest))))
            continue
        # innermost ownership first; a composite that is innermost holds the byte in its residual part
        out.append(inner + ".~" if units[inner].composite else inner)
    return out


def owners_partial_only(units: dict, size: int) -> list:
    """3540d98 B4's reading: only partial overlap is ABSENT, so equal sibling regions have two owners."""
    return owners_settled(units, size, equal_absent=False)


def owners_member_residual(units: dict, size: int) -> list:
    """b46c250 N6's literal reading: a composite's residual subtracts only its members, so a strictly
    nested non-member's bytes stay in the residual too (owned twice)."""
    out = []
    regions = resolve_absent(units)
    for pos in range(size):
        holders = [n for n, r in regions.items() if r is not None and r[0] <= pos < r[1]]
        claims = set()
        for n in holders:
            u = units[n]
            if u.composite:
                members = [c for c, cu in units.items() if cu.parent == n and regions[c] is not None
                           and regions[c][0] <= pos < regions[c][1]]
                if not members:
                    claims.add(n + ".~")
            else:
                claims.add(n)
        out.append(("CONFLICT", tuple(sorted(claims))) if len(claims) > 1 else
                   (claims.pop() if claims else "UNCOVERED"))
    return out


PARTITION_READINGS = {"settled": owners_settled, "partial_only": owners_partial_only,
                      "member_residual": owners_member_residual}


# --- write set -----------------------------------------------------------------------------------

@dataclass(frozen=True)
class WUnit:
    name: str
    kind: str
    prefix: str                         # owns governed paths starting with it (innermost owner wins)


def owned(tree: dict, ignore: frozenset, units: tuple) -> dict:
    """unit -> frozenset of (path, content) it owns by innermost prefix, governed paths only."""
    out = {u.name: set() for u in units}
    for path, content in tree.items():
        if any(path.startswith(i) for i in ignore):
            continue
        cands = [u for u in units if path.startswith(u.prefix)]
        if cands:
            inner = max(cands, key=lambda u: len(u.prefix))
            out[inner.name].add((path, content))
    return {k: frozenset(v) for k, v in out.items()}


def write_set_settled(head: dict, head_ignore, merged: dict, merged_ignore, units_head, units_merged):
    """Head-to-merged, by owned content and declarations."""
    a = owned(head, head_ignore, units_head)
    b = owned(merged, merged_ignore, units_merged)
    names = {u.name for u in units_head} | {u.name for u in units_merged}
    decl_a = {u.name: u for u in units_head}
    decl_b = {u.name: u for u in units_merged}
    return {n for n in names if a.get(n) != b.get(n) or decl_a.get(n) != decl_b.get(n)}


def write_set_changed_paths(base: dict, candidate: dict, units: tuple, ignore) -> set:
    """cc005db B1 / d837363 B4's base-to-candidate reading: the owners of changed governed paths."""
    changed = {p for p in set(base) | set(candidate) if base.get(p) != candidate.get(p)}
    out = set()
    for p in changed:
        if any(p.startswith(i) for i in ignore):
            continue
        cands = [u for u in units if p.startswith(u.prefix)]
        if cands:
            out.add(max(cands, key=lambda u: len(u.prefix)).name)
    return out


# --- write set over spans (positions versus content; 5c55d4b B2) --------------------------------

def span_layout(spans: tuple) -> dict:
    """spans: ordered (unit, content) pieces of one file -> unit -> (start, end, content)."""
    out, pos = {}, 0
    for unit, content in spans:
        out[unit] = (pos, pos + len(content), content)
        pos += len(content)
    return out


def span_write_set(before: tuple, after: tuple, by_position: bool) -> set:
    a, b = span_layout(before), span_layout(after)
    key = (lambda v: v) if by_position else (lambda v: v[2])
    return {u for u in set(a) | set(b) if (key(a[u]) if u in a else None) != (key(b[u]) if u in b else None)}
