"""The one content representation: the Git tree entry (Manual §1.5).

A tree maps each tracked path to its entry: the entry mode and the blob bytes,
a gitlink's bytes being the commit identity it records. Nothing is converted:
no end-of-line, encoding, filter or sparse transformation.
"""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from dataclasses import dataclass

#: Git entry modes and the entry type each denotes.
MODES = {"100644": "regular", "100755": "executable", "120000": "link", "160000": "gitlink"}


@dataclass(frozen=True)
class Entry:
    mode: str
    data: bytes

    def __post_init__(self) -> None:
        if self.mode not in MODES:
            raise ValueError(f"unsupported Git entry mode {self.mode!r}")

    @property
    def type(self) -> str:
        return MODES[self.mode]

    @property
    def is_text_file(self) -> bool:
        """Span terms resolve only in regular and executable files (§1.5)."""

        return self.mode in ("100644", "100755")


class Tree(Mapping[str, Entry]):
    """An immutable path -> entry map."""

    def __init__(self, entries: Mapping[str, Entry | bytes]) -> None:
        normalized: dict[str, Entry] = {}
        for path, value in entries.items():
            check_path(path)
            normalized[path] = value if isinstance(value, Entry) else Entry("100644", value)
        self._entries = dict(sorted(normalized.items(), key=lambda item: item[0].encode("utf-8")))

    def __getitem__(self, path: str) -> Entry:
        return self._entries[path]

    def __iter__(self) -> Iterator[str]:
        return iter(self._entries)

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        return f"Tree({len(self._entries)} entries)"

    def replace(self, changes: Mapping[str, Entry | bytes | None]) -> Tree:
        """A new tree with ``changes`` applied; ``None`` removes a path."""

        merged: dict[str, Entry | bytes] = dict(self._entries)
        for path, value in changes.items():
            if value is None:
                merged.pop(path, None)
            else:
                merged[path] = value
        return Tree(merged)


def check_path(path: str) -> None:
    """A validated repository-relative path: no absolute, empty, dot or backslash segments."""

    if not path or path.startswith("/") or "\\" in path or "\0" in path:
        raise ValueError(f"not a repository-relative path: {path!r}")
    if any(part in ("", ".", "..") for part in path.split("/")):
        raise ValueError(f"not a repository-relative path: {path!r}")
