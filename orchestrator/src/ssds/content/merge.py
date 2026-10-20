"""The pinned three-way merge of the system version (catalogue §7.2).

Path-level three-way merge with no rename or copy detection: a path changed on
one side takes that side; changed identically on both, takes it; a text path
changed differently on both sides is merged by hunks of a fixed line diff and
succeeds only when no hunk of one side overlaps a hunk of the other; any other
both-sides change (binary content, a file mode, a link target, delete versus
modify, add versus add with different bytes) is a conflict. A declaration key
changed to different values on both sides is a conflict even where the
manifest's lines merge. Repository attributes, merge drivers and rerere never
apply. Changing this implementation is a system-version change (§27.3).
"""

from __future__ import annotations

from difflib import SequenceMatcher
from typing import Any

from .manifest import Manifest, parse_manifest
from .tree import Entry, Tree


def _lines(data: bytes) -> list[bytes]:
    return data.splitlines(keepends=True)


def _hunks(base: list[bytes], side: list[bytes]) -> list[tuple[int, int, tuple[bytes, ...]]]:
    matcher = SequenceMatcher(None, base, side, autojunk=False)
    return [(i1, i2, tuple(side[j1:j2])) for tag, i1, i2, j1, j2 in matcher.get_opcodes() if tag != "equal"]


def _overlap(a: tuple[int, int, Any], b: tuple[int, int, Any]) -> bool:
    (s1, e1, _), (s2, e2, _) = a, b
    if s1 < e1 and s2 < e2:
        return s1 < e2 and s2 < e1
    if s1 == e1 and s2 == e2:
        return s1 == s2
    point, (start, end) = (s1, (s2, e2)) if s1 == e1 else (s2, (s1, e1))
    return start <= point <= end  # an insertion on or inside the other hunk is ambiguous in order


def merge_text(base: bytes, head: bytes, candidate: bytes) -> bytes | None:
    """The line merge, or None when a hunk of one side overlaps a hunk of the other."""

    b = _lines(base)
    hunks = sorted([(*h, "H") for h in _hunks(b, _lines(head))] + [(*h, "C") for h in _hunks(b, _lines(candidate))])
    chosen: list[tuple[int, int, tuple[bytes, ...]]] = []
    i = 0
    while i < len(hunks):
        group = [hunks[i]]
        j = i + 1
        while j < len(hunks) and any(_overlap(g[:3], hunks[j][:3]) for g in group):
            group.append(hunks[j])
            j += 1
        sides = {g[3] for g in group}
        if len(sides) > 1:
            changes = {(g[0], g[1], g[2]) for g in group}
            if len(changes) != 1:
                return None
        chosen.extend(sorted({(g[0], g[1], g[2]) for g in group}))
        i = j
    out: list[bytes] = []
    cursor = 0
    for start, end, lines in chosen:
        out.extend(b[cursor:start])
        out.extend(lines)
        cursor = end
    out.extend(b[cursor:])
    return b"".join(out)


def _text(entry: Entry | None) -> bool:
    return entry is not None and entry.is_text_file and b"\0" not in entry.data


def _decl(tree: Tree, manifest_path: str) -> dict[tuple[str, str], Any] | None:
    entry = tree.get(manifest_path)
    if entry is None:
        return {}
    parsed = parse_manifest(entry.data)
    return dict(parsed.decl) if isinstance(parsed, Manifest) else None


def merge3(base: Tree, head: Tree, candidate: Tree, manifest_path: str) -> tuple[Tree | None, str | None]:
    """``M(X)``: ``candidate`` merged onto ``head`` with merge base ``base``; ``(None, reason)`` on conflict."""

    merged: dict[str, Entry] = {}
    for path in sorted(set(base) | set(head) | set(candidate)):
        b, h, c = base.get(path), head.get(path), candidate.get(path)
        if h == c:
            if h is not None:
                merged[path] = h
            continue
        if h == b:
            if c is not None:
                merged[path] = c
            continue
        if c == b:
            if h is not None:
                merged[path] = h
            continue
        if not (_text(b) and _text(h) and _text(c)) or not (b.mode == h.mode == c.mode):  # type: ignore[union-attr]
            return None, f"{path}: a both-sides change that is not a text merge"
        text = merge_text(b.data, h.data, c.data)  # type: ignore[union-attr]
        if text is None:
            return None, f"{path}: overlapping hunks"
        merged[path] = Entry(b.mode, text)  # type: ignore[union-attr]
    decls = [_decl(t, manifest_path) for t in (base, head, candidate)]
    if any(d is None for d in decls):
        return None, "a manifest that does not parse cannot be merged by key"
    db, dh, dc = decls  # type: ignore[misc]
    for key in set(db) | set(dh) | set(dc):
        if dh.get(key) != db.get(key) and dc.get(key) != db.get(key) and dh.get(key) != dc.get(key):
            return None, f"declaration key {key} changed differently on both sides"
    return Tree(merged), None
