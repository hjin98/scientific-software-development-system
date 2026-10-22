"""Scope-term resolution as a pure function of tree bytes (catalogue §1.3).

``resolve`` returns the region a term denotes, or ``None`` for ``ABSENT``: the
file is missing or not governed, the heading path, symbol or anchor does not
occur or occurs more than once, or anchors are unbalanced or crossed. A span
term in a file that is not a regular or executable file is ``ABSENT``.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass

from ssds import analyzers

from .lines import Line, directives, split_lines
from .manifest import Term
from .tree import Tree

ATX_HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*$")
FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})")


@dataclass(frozen=True, order=True)
class Span:
    path: str
    start: int
    end: int


Region = tuple[Span, ...]


@dataclass(frozen=True)
class Resolution:
    region: Region | None  # None is ABSENT
    malformed_anchor: bool = False


def resolve(term: Term, tree: Tree, governed: Callable[[str], bool]) -> Resolution:
    if term.kind == "prefix":
        paths = [p for p in tree if p.startswith(term.file) and governed(p)]
        return Resolution(tuple(Span(p, 0, len(tree[p].data)) for p in paths))
    entry = tree.get(term.file)
    if entry is None or not governed(term.file):
        return Resolution(None)
    if term.kind in ("path", "file"):
        return Resolution((Span(term.file, 0, len(entry.data)),))
    if not entry.is_text_file:
        return Resolution(None)
    if term.kind == "heading":
        span = _heading(term.file, entry.data, term.arg)  # type: ignore[arg-type]
        return Resolution(None if span is None else (Span(term.file, *span),))
    if term.kind == "symbol":
        span = analyzers.resolve_symbol(term.file, entry.data, str(term.arg))
        return Resolution(None if span is None else (Span(term.file, *span),))
    span, malformed = _anchor(term.file, entry.data, str(term.arg))
    return Resolution(None if span is None else (Span(term.file, *span),), malformed)


def _heading(path: str, data: bytes, wanted: tuple[str, ...]) -> tuple[int, int] | None:
    lines = split_lines(data)
    headings: list[tuple[Line, int, tuple[str, ...]]] = []
    stack: list[tuple[int, str]] = []
    fence: str | None = None
    for line in lines:
        text = line.text.decode("utf-8", "replace")
        marker = FENCE_OPEN.match(text)
        if fence is not None:
            if marker and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence):
                fence = None
            continue
        if marker:
            fence = marker.group(1)
            continue
        match = ATX_HEADING.match(text)
        if not match:
            continue
        level = len(match.group(1))
        title = (match.group(2) or "").strip()
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, title))
        headings.append((line, level, tuple(t for _, t in stack)))
    matches = [i for i, (_, _, chain) in enumerate(headings) if chain[-len(wanted) :] == wanted]
    if len(matches) != 1:
        return None
    index = matches[0]
    line, level, _ = headings[index]
    end = len(data)
    for later, later_level, _ in headings[index + 1 :]:
        if later_level <= level:
            end = later.start
            break
    return line.start, end


def _anchor(path: str, data: bytes, name: str) -> tuple[tuple[int, int] | None, bool]:
    marks = [d for d in directives(path, data) if d.verb in ("begin", "end") and len(d.args) == 1]
    begins = [d.line for d in marks if d.verb == "begin" and d.args[0] == name]
    ends = [d.line for d in marks if d.verb == "end" and d.args[0] == name]
    if not begins and not ends:
        return None, False
    if len(begins) != 1 or len(ends) != 1 or begins[0] >= ends[0]:
        return None, True
    begin, end = begins[0], ends[0]
    for other in {d.args[0] for d in marks} - {name}:
        other_begins = [d.line for d in marks if d.verb == "begin" and d.args[0] == other]
        other_ends = [d.line for d in marks if d.verb == "end" and d.args[0] == other]
        if len(other_begins) == 1 and len(other_ends) == 1:
            b, e = other_begins[0], other_ends[0]
            if (begin < b < end < e) or (b < begin < e < end):
                return None, True
    lines = split_lines(data)
    return (lines[begin].end, lines[end].start), False
