"""The one write-scope owner of a frame (Manual §1.2, §1.8, §8.3 step 3, §14.3; Phase F plan §3.1, 4c-i).

``Conformance``'s write-scope template and Admission's ``AUTH_WRITE_SCOPE`` (4c-iii) both read it, over the
frame's one write set: ``T_n`` under ``Σ_n`` against ``M_n(X)`` under ``Σ_n ⊕ Δ_Σ(X)``.

- **Both sides.** A write-set unit lies within the write scope on both sides, each side's regions resolved in its
  own tree: a byte that leaves a unit is written as surely as one that enters it (a deletion; review 2aadf33 B1).
  A unit with a region on neither side lies within it only when the scope names it: its declarations are what
  changed, and they are written by naming it.
- **A unit only one side declares.** A scope entry naming a unit the other side lacks (one the request creates,
  or a rename's new name) resolves on that side to the whole files the unit covers where it is declared (re-check
  ad8daeb RB2), as §1.8's "names that content in its write scope" asks.
- **The outermost owner.** ``ssds.unclassified`` holds every byte no other unit owns, so it is judged by the bytes
  it gains or loses, file by file: each of its changed pieces lies within the scope on the side that holds it.
  A write elsewhere in the repository never needs a scope over all of its bytes (re-check ad8daeb).
"""

from __future__ import annotations

from typing import Any

from ssds.content import UNCLASSIFIED, TreeView

from .plans import contained, resolve

Atom = tuple[Any, ...]


def scope_on(view: TreeView, other: TreeView | None, entries: Any) -> list[Atom]:
    """The write scope resolved in ``view``; an entry naming a unit only ``other`` declares resolves to the whole
    files that unit covers there."""

    atoms: list[Atom] = []
    for entry in entries:
        if other is not None and entry not in view.structure.units and entry in other.structure.units:
            region = other.regions.get(entry) or ()
            atoms += [("file", path) for path in sorted({span.path for span in region}) if path in view.tree]
        else:
            found, _ = resolve(view, [entry])
            atoms += found
    return atoms


def _unclassified_pieces(view: TreeView) -> dict[str, list[Atom]]:
    out: dict[str, list[Atom]] = {}
    for path, segments in view.ownership.items():
        pieces = [("span", path, seg.start, seg.end) for seg in segments if seg.owner == UNCLASSIFIED]
        if pieces:
            out[path] = pieces
    return out


def _within(head: TreeView, merged: TreeView, unit: str, entries: Any) -> bool:
    if unit == UNCLASSIFIED:
        before, after = head.unclassified_owned, merged.unclassified_owned  # its one representation (§1.5)
        changed = {p for p in set(before) | set(after) if before.get(p) != after.get(p)}
        sides = ((head, merged, _unclassified_pieces(head)), (merged, head, _unclassified_pieces(merged)))
        for view, other, pieces in sides:
            scope = scope_on(view, other, entries)
            for path in sorted(changed & set(pieces)):
                if not contained(view, pieces[path], scope):
                    return False
        if changed:
            return True
        # no byte moved: a change of its declarations alone, judged as any unit's below
    sides_held = 0
    for view, other in ((head, merged), (merged, head)):
        if unit not in view.structure.units:
            continue
        region = view.regions.get(unit)
        if not region:
            continue
        sides_held += 1
        if not contained(view, [("span", s.path, s.start, s.end) for s in region], scope_on(view, other, entries)):
            return False
    return sides_held > 0 or unit in entries  # with no region, its declarations are written by naming it


def outside_scope(frame: Any, entries: Any) -> list[str]:
    """Units in the frame's write set whose bytes lie outside the write scope ``entries``."""

    if frame is None or frame.merged is None:
        return []
    return [u for u in sorted(frame.write_set) if not _within(frame.head_view, frame.view, u, entries)]


def owners(frame: Any, path: str) -> tuple[str, ...]:
    """The units whose region lies in ``path``, in the merged tree or else the head; ``<path>`` when none."""

    found: set[str] = set()
    if frame is not None:
        for view in (frame.view, frame.head_view):
            for uid, region in view.regions.items():
                if region and any(span.path == path for span in region):
                    found.add(uid)
    return tuple(sorted(found)) or (f"<{path}>",)


def uncovered_outside(frame: Any, entries: Any, manifest_path: str) -> list[str]:
    """Changed files no unit owns, outside the write scope: a write the effect-keyed write set cannot see when a
    ledger declares no ``ssds.unclassified`` (§1.8). §12.3 limits a write to the write scope, so this fails closed
    (step 4 review SC-1)."""

    if frame is None or frame.merged is None:
        return []
    scope = scope_on(frame.view, frame.head_view, entries)
    out = []
    for path in frame.changed_files:
        if owners(frame, path) != (f"<{path}>",) or path == manifest_path:
            continue
        if not contained(frame.view, [("file", path)], scope):
            out.append(path)
    return out


__all__ = ["outside_scope", "owners", "scope_on", "uncovered_outside"]
