"""The effect-keyed write set (catalogue §1.2; SD-14).

The set compares the current observed tree under its structure with the
merged tree under the merged structure. A unit is in it when, between the two,
any of these differs:

- its owned content by innermost ownership in the §1.5 representation (a
  residual part's bytes count for its composite), or the entry mode of a file
  one of its terms resolves into;
- a declaration key, or a semantic declaration it or a part carries;
- its resolved regions: a term's resolution status or the files it resolves
  into, or a byte present in both trees entering or leaving the region under
  the pinned line alignment. A position change alone is no difference, and a
  byte inserted or removed is owned content, never a region change;
- its membership or its governance signature.

``ssds.manifest`` is in it whenever the manifest's bytes change.
"""

from __future__ import annotations

from collections.abc import Mapping
from difflib import SequenceMatcher

from .lines import split_lines
from .resolve import Region
from .structure import RESIDUAL_SUFFIX, UNCLASSIFIED, Structure
from .view import TreeView


def _owned(view: TreeView, uid: str) -> tuple[dict[str, tuple[str, bytes]], dict[str, str]]:
    mine = dict(view.owned.get(uid, {}))
    for path, (mode, data) in view.owned.get(uid + RESIDUAL_SUFFIX, {}).items():
        previous = mine.get(path, (mode, b""))
        mine[path] = (mode, previous[1] + data)
    if uid == UNCLASSIFIED:
        files = set(mine)  # the outermost owner holds only the files it owns bytes of (plan reading F19)
    else:
        files = {span.path for region in view.term_resolutions.get(uid, ()) if region for span in region}
    modes = {path: view.tree[path].mode for path in files}
    return mine, modes


def _semantic(view: TreeView, uid: str) -> list[str]:
    owners = {uid, uid + RESIDUAL_SUFFIX}
    owners.update(m for m in view.structure.units if view.structure.is_member_of(m, uid))
    owners.update(m + RESIDUAL_SUFFIX for m in list(owners))
    return sorted(repr(sorted(d.items())) for d in view.semantic_declarations if d["unit"] in owners)


def _line_membership(data: bytes, spans: list[tuple[int, int]]) -> list[bool]:
    return [any(start < line.end and line.start < end or (start == end == line.start) for start, end in spans)
            for line in split_lines(data)]


def _region_differs(old_view: TreeView, old: Region | None, new_view: TreeView, new: Region | None) -> bool:
    if (old is None) != (new is None):
        return True
    if old is None or new is None:
        return False
    old_files = sorted({s.path for s in old})
    if old_files != sorted({s.path for s in new}):
        return True
    for path in old_files:
        old_data, new_data = old_view.tree[path].data, new_view.tree[path].data
        before = _line_membership(old_data, [(s.start, s.end) for s in old if s.path == path])
        after = _line_membership(new_data, [(s.start, s.end) for s in new if s.path == path])
        old_lines = [line.text for line in split_lines(old_data)]
        new_lines = [line.text for line in split_lines(new_data)]
        matcher = SequenceMatcher(None, old_lines, new_lines, autojunk=False)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag != "equal":
                continue
            for offset in range(i2 - i1):
                if before[i1 + offset] != after[j1 + offset]:
                    return True
    return False


def _signature(view: TreeView, uid: str, mode: str | None) -> tuple[object, ...]:
    unit = view.structure.units[uid]
    return (unit.subject, view.scope_id(uid), view.structure.kind(uid), mode)


def write_set(
    head: TreeView,
    merged: TreeView,
    head_modes: Mapping[str, str] | None = None,
    merged_modes: Mapping[str, str] | None = None,
) -> dict[str, frozenset[str]]:
    """Unit id -> the kinds it has in either structure, for every unit in the write set."""

    head_modes = head_modes or {}
    merged_modes = merged_modes or {}
    a, b = head.structure, merged.structure
    out: dict[str, frozenset[str]] = {}
    for uid in sorted(set(a.units) | set(b.units)):
        kinds = frozenset(k for k in (a.kind(uid) if uid in a.units else None, b.kind(uid) if uid in b.units else None) if k)
        if uid not in a.units or uid not in b.units:
            out[uid] = kinds
            continue
        if _differs(head, merged, uid, a, b, head_modes.get(uid), merged_modes.get(uid)):
            out[uid] = kinds
    manifest = head.manifest_path
    if head.tree.get(manifest) != merged.tree.get(manifest):
        out.setdefault("ssds.manifest", frozenset({"MANIFEST"}))
    return out


def _differs(head: TreeView, merged: TreeView, uid: str, a: Structure, b: Structure,
             head_mode: str | None, merged_mode: str | None) -> bool:
    if a.keys_of(uid) != b.keys_of(uid):
        return True
    if a.members.get(uid) != b.members.get(uid):
        return True
    if _owned(head, uid) != _owned(merged, uid):
        return True
    if _semantic(head, uid) != _semantic(merged, uid):
        return True
    if _signature(head, uid, head_mode) != _signature(merged, uid, merged_mode):
        return True
    if uid == UNCLASSIFIED:  # its region is the bytes it owns, never its empty prefix's resolution (reading F19)
        old_terms, new_terms = (head.regions.get(uid),), (merged.regions.get(uid),)
    else:
        old_terms, new_terms = head.term_resolutions[uid], merged.term_resolutions[uid]
    if any(_region_differs(head, o, merged, n) for o, n in zip(old_terms, new_terms)):
        return True
    return (head.regions.get(uid) is None) != (merged.regions.get(uid) is None)
