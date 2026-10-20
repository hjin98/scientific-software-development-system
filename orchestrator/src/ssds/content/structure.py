"""Structure from declaration keys, the governed boundary and the static checks (catalogue §1.1-§1.4, §1.8-§1.9).

A :class:`Structure` is built from a declaration map, whether parsed from a
tree's manifest (``decl(T)``) or folded from admitted entries (``Σ_n``); the
Content Model never decides which of the two is effective.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from functools import cached_property, lru_cache
from typing import Any

from .manifest import GOVERNED_KEY, ID_RE, KINDS, ROLES, UNIT_FIELDS, Term, parse_term

#: Reserved system units (§1.8).
SYSTEM_UNITS = {"ssds.manifest": "MANIFEST", "ssds.policy": "POLICY", "ssds.unclassified": "UNCLASSIFIED"}
UNCLASSIFIED = "ssds.unclassified"
RESIDUAL_SUFFIX = ".~"
UNCOVERED = "UNCOVERED"
DOMAINS = {"D1": "D1", "D2": "D2", "D3": "D3", "D4": "D4", "PLAN": "plan", "EXTERNAL": "external",
           "POLICY": "governance", "MANIFEST": "governance"}

Decl = Mapping[tuple[str, str], Any]


@dataclass(frozen=True)
class Unit:
    id: str
    role: str
    subject: bool
    declared_kind: str | None
    part_of: str | None
    scope: tuple[Term, ...]
    renamed_from: tuple[str, ...]

    @property
    def composite(self) -> bool:
        return self.role == "composite"


@dataclass(frozen=True, order=True)
class StaticError:
    code: str
    unit: str
    detail: str


@lru_cache(maxsize=1024)
def _ignore_regex(pattern: str) -> re.Pattern[str]:
    """Git wildcard semantics, decided once by the system version (catalogue §1.3)."""

    directory = pattern.endswith("/")
    body = pattern.rstrip("/")
    anchored = "/" in body
    body = body.lstrip("/")
    out = []
    i = 0
    while i < len(body):
        if body.startswith("**/", i):
            out.append("(?:.*/)?")
            i += 3
        elif body.startswith("**", i):
            out.append(".*")
            i += 2
        elif body[i] == "*":
            out.append("[^/]*")
            i += 1
        elif body[i] == "?":
            out.append("[^/]")
            i += 1
        else:
            out.append(re.escape(body[i]))
            i += 1
    core = "".join(out)
    lead = "" if anchored else "(?:.*/)?"
    tail = "/.*" if directory else "(?:/.*)?"
    return re.compile(f"^{lead}{core}{tail}$")


def ignored(path: str, patterns: tuple[str, ...]) -> bool:
    return any(_ignore_regex(p).match(path) for p in patterns)


class Structure:
    """Units, membership, kinds and the governed boundary of one declaration map."""

    def __init__(self, decl: Decl) -> None:
        self.decl: dict[tuple[str, str], Any] = dict(decl)
        self.ignore: tuple[str, ...] = tuple(self.decl.get(GOVERNED_KEY, ()))
        ids = sorted({uid for (uid, field) in self.decl if (uid, field) != GOVERNED_KEY})
        self.units: dict[str, Unit] = {
            uid: Unit(
                id=uid,
                role=self.decl.get((uid, "role"), "leaf"),
                subject=self.decl.get((uid, "subject"), True),
                declared_kind=self.decl.get((uid, "kind")),
                part_of=self.decl.get((uid, "part_of")),
                scope=tuple(self.decl.get((uid, "scope"), ())),
                renamed_from=tuple(self.decl.get((uid, "renamed_from"), ())),
            )
            for uid in ids
        }

    def override(self, key: tuple[str, str], value: Any) -> Structure:
        """This structure with one declaration key set (``None`` removes it)."""

        decl = dict(self.decl)
        if value is None:
            decl.pop(key, None)
        else:
            decl[key] = value
        return Structure(decl)

    def keys_of(self, uid: str) -> dict[str, Any]:
        return {field: self.decl[(uid, field)] for field in UNIT_FIELDS if (uid, field) in self.decl}

    def governed(self, path: str) -> bool:
        return not ignored(path, self.ignore)

    @cached_property
    def members(self) -> dict[str, tuple[str, ...]]:
        out: dict[str, list[str]] = {uid: [] for uid in self.units}
        for unit in self.units.values():
            if unit.part_of in out:
                out[unit.part_of].append(unit.id)
        return {uid: tuple(sorted(m)) for uid, m in out.items()}

    def ancestors(self, uid: str) -> tuple[str, ...]:
        """The membership chain above ``uid``, innermost first; stops at a cycle or a missing unit."""

        chain: list[str] = []
        current = self.units[uid].part_of if uid in self.units else None
        while current is not None and current in self.units and current not in chain and current != uid:
            chain.append(current)
            current = self.units[current].part_of
        return tuple(chain)

    def is_member_of(self, inner: str, outer: str) -> bool:
        return outer in self.ancestors(inner)

    def kind(self, uid: str) -> str | None:
        """A subject's declared kind; a part inherits the kind of its nearest subject."""

        subject = self.subj(uid)
        return self.units[subject].declared_kind if subject is not None else None

    def subj(self, uid: str) -> str | None:
        if uid.endswith(RESIDUAL_SUFFIX):
            uid = uid[: -len(RESIDUAL_SUFFIX)]
        if uid not in self.units:
            return None
        for candidate in (uid, *self.ancestors(uid)):
            if self.units[candidate].subject:
                return candidate
        return None

    def domain(self, uid: str) -> str | None:
        kind = self.kind(uid)
        return DOMAINS.get(kind) if kind else None

    def top_level(self) -> tuple[str, ...]:
        return tuple(uid for uid, unit in self.units.items() if unit.part_of is None)


def static_errors(structure: Structure) -> list[StaticError]:
    """The §1.9 checks that need no tree: grammar, kinds, membership, disjointness, containment, lineage."""

    errors: list[StaticError] = []
    units = structure.units

    def err(code: str, uid: str, detail: str) -> None:
        errors.append(StaticError(code, uid, detail))

    for uid, unit in units.items():
        if not ID_RE.match(uid) or len(uid.encode("utf-8")) > 255:
            err("IDENTITY_GRAMMAR", uid, "identity outside the grammar")
        if uid.startswith("ssds.") and uid not in SYSTEM_UNITS:
            err("RESERVED_IDENTITY", uid, "the ssds. prefix is reserved for system units")
        if uid in SYSTEM_UNITS and unit.declared_kind != SYSTEM_UNITS[uid]:
            err("SYSTEM_UNIT_KIND", uid, f"{uid} has kind {SYSTEM_UNITS[uid]}")
        if unit.role not in ROLES:
            err("ROLE", uid, "role is leaf or composite")
        if not isinstance(unit.subject, bool):
            err("SUBJECT_FLAG", uid, "subject is a boolean")
        if unit.subject and unit.declared_kind not in KINDS:
            err("KIND_REQUIRED", uid, "a subject declares a known kind")
        if not unit.subject and unit.declared_kind is not None:
            err("KIND_ON_PART", uid, "a part inherits its subject's kind")
        if not unit.subject and unit.part_of is None:
            err("PART_WITHOUT_COMPOSITE", uid, "a part names its composite")
        if unit.part_of is not None:
            parent = units.get(unit.part_of)
            if parent is None:
                err("MEMBERSHIP", uid, f"part_of names no unit: {unit.part_of}")
            elif not parent.composite:
                err("MEMBERSHIP", uid, f"part_of names a leaf: {unit.part_of}")
            elif uid in structure.ancestors(unit.part_of) or unit.part_of == uid:
                err("MEMBERSHIP_CYCLE", uid, "membership is a forest")
        for term in unit.scope:
            if term.kind == "prefix" and term.file == "" and uid != UNCLASSIFIED:
                err("EMPTY_PREFIX", uid, "only ssds.unclassified uses the empty prefix")
            if term.kind == "symbol" and not term.file.endswith(".py"):
                err("SYMBOL_ANALYZER", uid, "no pinned analyzer resolves symbols in this file type")
        if not unit.scope:
            err("SCOPE_EMPTY", uid, "a unit declares at least one scope term")
        if uid in unit.renamed_from or _lineage_cycle(structure, uid):
            err("RENAMED_FROM_CYCLE", uid, "renamed_from lineage is acyclic")

    siblings: dict[str | None, list[str]] = {}
    for uid, unit in units.items():
        if uid != UNCLASSIFIED:
            siblings.setdefault(unit.part_of, []).append(uid)
    for group in siblings.values():
        group.sort()
        for i, a in enumerate(group):
            for b in group[i + 1 :]:
                for ta in units[a].scope:
                    for tb in units[b].scope:
                        if _statically_overlap(ta, tb):
                            err("SIBLING_OVERLAP", a, f"a term of {a} and of sibling {b} nest or coincide")
    for uid, unit in units.items():
        parent = units.get(unit.part_of) if unit.part_of else None
        if parent is None:
            continue
        for term in unit.scope:
            if not any(_contains(outer, term) for outer in parent.scope):
                err("CONTAINMENT", uid, f"a term of {uid} lies outside composite {parent.id}")
    return sorted(set(errors))


def _lineage_cycle(structure: Structure, start: str) -> bool:
    seen = set()
    stack = list(structure.units[start].renamed_from)
    while stack:
        current = stack.pop()
        if current == start:
            return True
        if current in seen or current not in structure.units:
            continue
        seen.add(current)
        stack.extend(structure.units[current].renamed_from)
    return False


def _covers_file(term: Term, path: str) -> bool:
    if term.kind == "prefix":
        return path.startswith(term.file)
    return term.kind in ("path", "file") and term.file == path


def _statically_overlap(a: Term, b: Term) -> bool:
    """§1.4 rule 1: nested or equal by declaration."""

    if not a.is_span and not b.is_span:
        if a.kind == "prefix" and b.kind == "prefix":
            return a.file.startswith(b.file) or b.file.startswith(a.file)
        if a.kind == "prefix":
            return b.file.startswith(a.file)
        if b.kind == "prefix":
            return a.file.startswith(b.file)
        return a.file == b.file
    if a.is_span and b.is_span:
        if a.file != b.file or a.kind != b.kind:
            return False
        if a.kind == "anchor":
            return a.arg == b.arg
        if a.kind == "heading":
            shorter = min(len(a.arg), len(b.arg))  # type: ignore[arg-type]
            return a.arg[:shorter] == b.arg[:shorter]  # type: ignore[index]
        x, y = str(a.arg), str(b.arg)
        return x == y or x.startswith(y + ".") or y.startswith(x + ".")
    span, whole = (a, b) if a.is_span else (b, a)
    return _covers_file(whole, span.file)


def _contains(outer: Term, inner: Term) -> bool:
    """§1.4 rule 2: a member term lies inside a composite term."""

    if not inner.is_span:
        if outer.kind == "prefix":
            return inner.file.startswith(outer.file)
        if outer.kind in ("path", "file"):
            return inner.kind in ("path", "file") and inner.file == outer.file
        return False
    if _covers_file(outer, inner.file):
        return True
    if not outer.is_span or outer.file != inner.file:
        return False
    if outer.kind != inner.kind:
        return True  # different span kinds on one file: containment is checked when resolved (§1.4 rule 3)
    if inner.kind == "heading":
        return inner.arg[: len(outer.arg)] == outer.arg  # type: ignore[index,arg-type]
    if inner.kind == "symbol":
        return str(inner.arg).startswith(str(outer.arg) + ".")
    return False


# -- the JSON form of structure, as genesis and admission entries carry it -----------------


def value_to_json(field: str, value: Any) -> Any:
    if field == "scope":
        return [t.to_json() for t in value]
    if isinstance(value, tuple):
        return list(value)
    return value


def value_from_json(field: str, value: Any) -> Any:
    if value is None:
        return None
    if field == "scope":
        return tuple(parse_term(t) for t in value)
    if isinstance(value, list):
        return tuple(value)
    return value


def decl_to_json(decl: Decl) -> dict[str, Any]:
    """``{"units": {id: {field: value}}, "governed": {"ignore": [...]}}``."""

    units: dict[str, dict[str, Any]] = {}
    governed: dict[str, Any] = {}
    for (uid, field), value in sorted(decl.items()):
        if (uid, field) == GOVERNED_KEY:
            governed["ignore"] = list(value)
        else:
            units.setdefault(uid, {})[field] = value_to_json(field, value)
    return {"units": units, "governed": governed}


def decl_from_json(raw: Mapping[str, Any]) -> dict[tuple[str, str], Any]:
    decl: dict[tuple[str, str], Any] = {}
    for uid, fields in raw.get("units", {}).items():
        for field, value in fields.items():
            decl[(uid, field)] = value_from_json(field, value)
    if "ignore" in raw.get("governed", {}):
        decl[GOVERNED_KEY] = tuple(raw["governed"]["ignore"])
    return decl
