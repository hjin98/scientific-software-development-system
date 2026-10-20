"""The unit manifest: a data-only TOML parse into declaration keys (catalogue §1.2, §1.3).

Parsing never instantiates objects or executes content (T2). A manifest that
does not parse, or does not meet the closed grammar, yields a
:class:`ManifestFailure`, which leaves every declaration key quarantined
against admitted structure (§1.6).
"""

from __future__ import annotations

import re
import tomllib
from dataclasses import dataclass, field
from typing import Any

from .tree import check_path

MANIFEST_SCHEMA = 1
DEFAULT_MANIFEST_PATH = ".ssds/manifest.toml"

ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,62}(?:\.[a-z0-9][a-z0-9_-]{0,62})*$")
SEGMENT_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,62}$")
KINDS = frozenset(
    {"D1", "D2", "D3", "D4", "EVIDENCE_SPEC", "EVIDENCE_RECORD", "PLAN", "GENERATED", "EXTERNAL",
     "POLICY", "MANIFEST", "UNCLASSIFIED"}
)
ROLES = frozenset({"leaf", "composite"})
#: Structural declaration fields per unit (§1.2); ("governed", "ignore") is the one global key.
UNIT_FIELDS = ("kind", "role", "subject", "part_of", "scope", "renamed_from")
GOVERNED_KEY = ("governed", "ignore")
_UNIT_KEYS = frozenset({"id", *UNIT_FIELDS, "semantic"})
_SEMANTIC_KEYS = frozenset({"defines", "relations", "sdg", "joint_invariants"})


@dataclass(frozen=True)
class Term:
    """One scope term of the closed grammar (§1.3)."""

    kind: str  # path | prefix | heading | symbol | anchor | file
    file: str  # the path, the prefix, or the file a span term names
    arg: tuple[str, ...] | str | None = None  # heading path, symbol name or anchor name

    def to_json(self) -> dict[str, Any]:
        if self.kind == "path":
            return {"path": self.file}
        if self.kind == "prefix":
            return {"prefix": self.file}
        if self.kind == "file":
            return {"file": self.file}
        value: Any = list(self.arg) if isinstance(self.arg, tuple) else self.arg
        return {"file": self.file, self.kind: value}

    @property
    def is_span(self) -> bool:
        return self.kind in ("heading", "symbol", "anchor")


@dataclass(frozen=True)
class Manifest:
    schema: int
    decl: dict[tuple[str, str], Any]
    semantic: dict[str, tuple[dict[str, Any], ...]] = field(default_factory=dict)


@dataclass(frozen=True)
class ManifestFailure:
    reason: str  # PARSE | GRAMMAR
    detail: str


class _Grammar(ValueError):
    pass


def parse_term(raw: Any) -> Term:
    if not isinstance(raw, dict):
        raise _Grammar("a scope term is a table")
    keys = set(raw)
    if keys == {"path"}:
        _path(raw["path"])
        return Term("path", raw["path"])
    if keys == {"prefix"}:
        prefix = raw["prefix"]
        if not isinstance(prefix, str) or (prefix and (not prefix.endswith("/") or prefix.startswith("/"))):
            raise _Grammar("a prefix ends with '/' or is empty")
        if prefix:
            _path(prefix[:-1])
        return Term("prefix", prefix)
    if keys == {"file"}:
        _path(raw["file"])
        return Term("file", raw["file"])
    if len(keys) == 2 and "file" in keys:
        _path(raw["file"])
        (kind,) = keys - {"file"}
        value = raw[kind]
        if kind == "heading":
            if not isinstance(value, list) or not value or not all(isinstance(v, str) and v for v in value):
                raise _Grammar("a heading path is a non-empty list of headings")
            return Term("heading", raw["file"], tuple(value))
        if kind == "symbol":
            if not isinstance(value, str) or not re.match(r"^[A-Za-z_][\w]*(?:\.[A-Za-z_][\w]*)*$", value):
                raise _Grammar("a symbol is a dotted qualified name")
            return Term("symbol", raw["file"], value)
        if kind == "anchor":
            if not isinstance(value, str) or not SEGMENT_RE.match(value):
                raise _Grammar("an anchor name follows the segment grammar")
            return Term("anchor", raw["file"], value)
    raise _Grammar(f"unknown scope term {sorted(keys)}")


def _path(value: Any) -> None:
    if not isinstance(value, str):
        raise _Grammar("a path is a string")
    try:
        check_path(value)
    except ValueError as exc:
        raise _Grammar(str(exc)) from None


def _ids(value: Any, what: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
        raise _Grammar(f"{what} is a list of identities")
    return tuple(value)


def _semantic(raw: Any) -> tuple[dict[str, Any], ...]:
    if not isinstance(raw, dict) or not set(raw) <= _SEMANTIC_KEYS:
        raise _Grammar("unknown [unit.semantic] key")
    out: list[dict[str, Any]] = []
    for name in _ids(raw.get("defines", []), "defines"):
        out.append({"decl": "defines", "object": name})
    for rel in raw.get("relations", []):
        if not isinstance(rel, dict) or not {"type", "object"} <= set(rel):
            raise _Grammar("a relation has a type and an object")
        attrs = {k: v for k, v in rel.items() if k not in ("type", "object")}
        if not all(isinstance(v, str) for v in attrs.values()):
            raise _Grammar("relation attributes are strings")
        out.append({"decl": "rel", "type": rel["type"], "object": rel["object"], "attrs": attrs})
    for group in raw.get("sdg", []):
        if not isinstance(group, dict) or set(group) != {"id", "members"}:
            raise _Grammar("an sdg has an id and members")
        out.append({"decl": "sdg", "id": group["id"], "members": sorted(_ids(group["members"], "sdg members"))})
    for inv in raw.get("joint_invariants", []):
        if not isinstance(inv, dict) or set(inv) != {"id", "units"}:
            raise _Grammar("a joint invariant has an id and units")
        out.append({"decl": "joint_invariant", "id": inv["id"], "units": sorted(_ids(inv["units"], "invariant units"))})
    return tuple(out)


def parse_manifest(data: bytes) -> Manifest | ManifestFailure:
    try:
        raw = tomllib.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as exc:
        return ManifestFailure("PARSE", str(exc))
    try:
        return _manifest(raw)
    except _Grammar as exc:
        return ManifestFailure("GRAMMAR", str(exc))


def _manifest(raw: dict[str, Any]) -> Manifest:
    if not set(raw) <= {"schema", "governed", "unit"}:
        raise _Grammar("unknown top-level manifest key")
    if raw.get("schema") != MANIFEST_SCHEMA:
        raise _Grammar("unsupported manifest grammar version")
    decl: dict[tuple[str, str], Any] = {}
    governed = raw.get("governed", {})
    if not isinstance(governed, dict) or not set(governed) <= {"ignore"}:
        raise _Grammar("unknown [governed] key")
    if "ignore" in governed:
        patterns = governed["ignore"]
        if not isinstance(patterns, list) or not all(isinstance(p, str) and p for p in patterns):
            raise _Grammar("ignore is a list of patterns")
        decl[GOVERNED_KEY] = tuple(patterns)
    semantic: dict[str, tuple[dict[str, Any], ...]] = {}
    units = raw.get("unit", [])
    if not isinstance(units, list):
        raise _Grammar("[[unit]] is an array of tables")
    for unit in units:
        if not isinstance(unit, dict) or not set(unit) <= _UNIT_KEYS or "id" not in unit:
            raise _Grammar("a unit has an id and only grammar keys")
        uid = unit["id"]
        if not isinstance(uid, str):
            raise _Grammar("a unit id is a string")
        if (uid, "role") in decl:
            raise _Grammar(f"unit {uid} is declared twice")
        if "kind" in unit:
            decl[(uid, "kind")] = unit["kind"]
        decl[(uid, "role")] = unit.get("role", "leaf")
        decl[(uid, "subject")] = unit.get("subject", True)
        if "part_of" in unit:
            decl[(uid, "part_of")] = unit["part_of"]
        terms = unit.get("scope", [])
        if not isinstance(terms, list):
            raise _Grammar("scope is a list of terms")
        decl[(uid, "scope")] = tuple(parse_term(t) for t in terms)
        if "renamed_from" in unit:
            decl[(uid, "renamed_from")] = _ids(unit["renamed_from"], "renamed_from")
        if "semantic" in unit:
            semantic[uid] = _semantic(unit["semantic"])
    return Manifest(MANIFEST_SCHEMA, decl, semantic)
