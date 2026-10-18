"""G2 Stage S step S5, catalogue §7: the fixed merge, basis-entry roles and one-use prospective acceptance.

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

* Merge (Manual §7.2): path-level three-way merge with no rename detection; a path changed on one side
  takes that side; changed identically on both sides takes it; a text path changed differently on both
  sides merges line-wise only when no hunk overlaps; any other both-sides change, and a declaration key
  changed to different values on both sides, is a conflict, so no frame exists.
* Roles (§7.3): before-image, output, context, from B, C and the entry.
* Prospective acceptance (§7.6): counts for the tenure an integration starts only for its own
  enactment, with the same structure, its basis holding, and not having counted for an earlier tenure.
"""

from __future__ import annotations


def merge3(base: dict, head: dict, cand: dict, decl_keys=frozenset()):
    """Paths map to tuples of lines (text) or bytes objects (binary). Returns (merged, conflict)."""
    out = {}
    for p in set(base) | set(head) | set(cand):
        b, h, c = base.get(p), head.get(p), cand.get(p)
        if h == c:
            if h is not None:
                out[p] = h
            continue
        if h == b:
            if c is not None:
                out[p] = c
            continue
        if c == b:
            if h is not None:
                out[p] = h
            continue
        if p in decl_keys:
            return None, f"declaration key {p} changed differently on both sides"
        if not all(isinstance(x, tuple) for x in (b, h, c)):
            return None, f"{p}: a both-sides change that is not a clean text merge"
        merged = _merge_lines(b, h, c)
        if merged is None:
            return None, f"{p}: overlapping hunks"
        out[p] = merged
    return out, None


def _merge_lines(b, h, c):
    """Equal-length line lists only (no insertions), enough for overlap detection."""
    if not (len(b) == len(h) == len(c)):
        return None
    res = []
    for lb, lh, lc in zip(b, h, c):
        if lh == lc or lc == lb:
            res.append(lh)
        elif lh == lb:
            res.append(lc)
        else:
            return None
    return tuple(res)


def role(unit, rev, base_revs: dict, cand_revs: dict) -> str:
    changed = base_revs.get(unit) != cand_revs.get(unit)
    if not changed:
        return "context"
    if rev == base_revs.get(unit):
        return "before-image"
    if rev == cand_revs.get(unit):
        return "output"
    return "never"


def counts_for_tenure(acc: dict, integration: dict, already_counted: bool) -> bool:
    """acc: {enactment, structure, basis_holds}; integration: {enactment, structure}."""
    return (acc["enactment"] == integration["enactment"]
            and acc["structure"] == integration["structure"]
            and acc["basis_holds"] and not already_counted)


def counts_lineage(acc: dict, integration: dict, already_counted: bool) -> bool:
    """f22b4dc B1's reading: any enactment of the same obligation's lineage carries the acceptance."""
    return (acc["obligation"] == integration["obligation"] and acc["structure"] == integration["structure"]
            and acc["basis_holds"])
