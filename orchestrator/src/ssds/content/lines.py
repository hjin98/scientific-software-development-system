"""Lines, the fixed comment classifier, anchors and inline semantic markers (catalogue §1.2, §1.5, §1.7).

The classifier belongs to the system version. In a classified file type an
anchor or marker is recognized only on a line the classifier calls a comment,
and an anchor line is the one normalization removed from identity. In a type
with a comment leader but no classifier the line is recognized syntactically
and kept in identity. Other types carry no anchors or markers.
"""

from __future__ import annotations

import io
import re
import tokenize
from dataclasses import dataclass
from functools import lru_cache
from posixpath import splitext

_PYTHON = {".py"}
_C_LIKE = {".c", ".h", ".cc", ".cpp", ".cxx", ".hh", ".hpp", ".hxx"}
_MARKDOWN = {".md", ".markdown"}
_HTML = {".html", ".htm"}
#: Comment leaders of types without a classifier: recognized syntactically, kept in identity.
_LEADER_ONLY = {".toml": "#", ".yaml": "#", ".yml": "#", ".sh": "#", ".tex": "%"}

_DIRECTIVE = re.compile(r"^ssds:(begin|end|rel|defines|sdg|joint-invariant)(?:\s+(.*?))?\s*$")


@dataclass(frozen=True)
class Line:
    index: int
    start: int  # byte offset of the line's first byte
    end: int  # byte offset just after its terminator
    text: bytes  # without the LF and one trailing CR


def split_lines(data: bytes) -> list[Line]:
    lines: list[Line] = []
    position = 0
    index = 0
    while position < len(data):
        newline = data.find(b"\n", position)
        end = len(data) if newline < 0 else newline + 1
        text = data[position : newline if newline >= 0 else len(data)]
        if text.endswith(b"\r"):
            text = text[:-1]
        lines.append(Line(index, position, end, text))
        position = end
        index += 1
    return lines


def classified(path: str) -> bool:
    ext = splitext(path)[1].lower()
    return ext in _PYTHON | _C_LIKE | _MARKDOWN | _HTML


@lru_cache(maxsize=4096)
def comment_bodies(path: str, data: bytes) -> dict[int, str]:
    """Line index -> comment body, for lines that are wholly a comment of the file's type."""

    ext = splitext(path)[1].lower()
    lines = split_lines(data)
    if ext in _PYTHON:
        return _python_comments(data, lines)
    if ext in _C_LIKE:
        return _c_comments(lines)
    if ext in _MARKDOWN:
        return _markdown_comments(lines, fenced_code=True)
    if ext in _HTML:
        return _markdown_comments(lines, fenced_code=False)
    leader = _LEADER_ONLY.get(ext)
    if leader is None:
        return {}
    out = {}
    for line in lines:
        stripped = _decode(line.text).strip()
        if stripped.startswith(leader):
            out[line.index] = stripped[len(leader) :].strip()
    return out


def _decode(text: bytes) -> str:
    return text.decode("utf-8", "replace")


def _python_comments(data: bytes, lines: list[Line]) -> dict[int, str]:
    out: dict[int, str] = {}
    try:
        tokens = list(tokenize.tokenize(io.BytesIO(data).readline))
    except (tokenize.TokenError, SyntaxError, IndentationError):
        return out
    for token in tokens:
        if token.type != tokenize.COMMENT:
            continue
        row = token.start[0] - 1
        if row < len(lines) and _decode(lines[row].text)[: token.start[1]].strip() == "":
            out[row] = token.string[1:].strip()
    return out


def _c_comments(lines: list[Line]) -> dict[int, str]:
    out: dict[int, str] = {}
    in_block = False
    for line in lines:
        stripped = _decode(line.text).strip()
        if in_block:
            if "*/" in stripped:
                in_block = False
            continue
        if stripped.startswith("//"):
            out[line.index] = stripped[2:].strip()
        elif stripped.startswith("/*"):
            if stripped.endswith("*/") and len(stripped) >= 4:
                out[line.index] = stripped[2:-2].strip()
            elif "*/" not in stripped:
                in_block = True
    return out


def _markdown_comments(lines: list[Line], fenced_code: bool) -> dict[int, str]:
    out: dict[int, str] = {}
    fence: str | None = None
    for line in lines:
        text = _decode(line.text)
        stripped = text.strip()
        if fenced_code:
            marker = re.match(r"^ {0,3}(`{3,}|~{3,})", text)
            if fence is not None:
                if marker and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence):
                    fence = None
                continue
            if marker:
                fence = marker.group(1)
                continue
            if text.startswith("    ") or text.startswith("\t"):
                continue  # indented code
        if stripped.startswith("<!--") and stripped.endswith("-->") and len(stripped) >= 7:
            out[line.index] = stripped[4:-3].strip()
    return out


@dataclass(frozen=True)
class Directive:
    line: int
    verb: str  # begin | end | rel | defines | sdg | joint-invariant
    args: tuple[str, ...]


def directives(path: str, data: bytes) -> list[Directive]:
    """Every ``ssds:`` anchor or semantic marker line of the file, in order."""

    out = []
    for index, body in sorted(comment_bodies(path, data).items()):
        match = _DIRECTIVE.match(body)
        if match:
            out.append(Directive(index, match.group(1), tuple((match.group(2) or "").split())))
    return out


def anchor_line_indices(path: str, data: bytes) -> frozenset[int]:
    """Anchor lines removed by normalization: only in a classified type (§1.5)."""

    if not classified(path):
        return frozenset()
    return frozenset(d.line for d in directives(path, data) if d.verb in ("begin", "end"))


def normalized(path: str, data: bytes, start: int, end: int) -> bytes:
    """The bytes of ``[start, end)`` with classified anchor lines removed."""

    removed = anchor_line_indices(path, data)
    if not removed:
        return data[start:end]
    pieces = []
    cursor = start
    for line in split_lines(data):
        if line.index in removed and line.start >= start and line.end <= end:
            pieces.append(data[cursor : line.start])
            cursor = line.end
    pieces.append(data[cursor:end])
    return b"".join(pieces)
