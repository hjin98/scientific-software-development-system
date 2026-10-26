"""One tree under one structure: partition by construction, identities and declarations (catalogue §1.4-§1.7).

A :class:`TreeView` is a pure, memoized function of ``(tree, structure,
manifest path)``. It resolves every term (§1.3), applies the dynamic partition
tests once and without cascade (§1.4 rule 3), assigns each governed byte to its
innermost owner, a residual part ``<id>.~`` or the uncovered region, and
computes the §1.5 identities from the one representation.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from functools import cached_property
from typing import Any

from ssds.core.api.v1 import canonical_json

from .lines import directives, normalized
from .manifest import DEFAULT_MANIFEST_PATH, GOVERNED_KEY, Manifest, Term, parse_manifest, parse_term
from .resolve import Region, Span, resolve
from .structure import RESIDUAL_SUFFIX, UNCLASSIFIED, UNCOVERED, Structure
from .tree import Tree

ABSENT = None


@dataclass(frozen=True, order=True)
class IntegrityFinding:
    code: str  # ANCHOR_MALFORMED | REGION_OVERLAP | MEMBER_OUTSIDE | MANIFEST_UNPARSED
    unit: str
    detail: str


@dataclass(frozen=True)
class Segment:
    start: int
    end: int
    owner: str  # a unit id, a residual part id, or UNCOVERED


def _field(data: bytes) -> bytes:
    return len(data).to_bytes(8, "big") + data


def _hash(*fields: bytes) -> str:
    digest = hashlib.sha256()
    for item in fields:
        digest.update(_field(item))
    return "sha256:" + digest.hexdigest()


def jcs(value: Any) -> bytes:
    """RFC 8785 canonical JSON, the one encoding identities hash (catalogue §1.5, §6)."""

    return canonical_json(value)


_jcs = jcs


def _bytes_of(region: Region) -> int:
    return sum(span.end - span.start for span in region)


def _merge(region: Region) -> Region:
    """Sorted, coalesced spans; an empty span records coverage of a byteless file."""

    out: list[Span] = []
    for span in sorted(region):
        if out and out[-1].path == span.path and span.start <= out[-1].end:
            if span.end > out[-1].end:
                out[-1] = Span(span.path, out[-1].start, span.end)
        else:
            out.append(span)
    return tuple(out)


def _contains(outer: Region, inner: Region) -> bool:
    for span in inner:
        if span.start == span.end:
            if not any(o.path == span.path for o in outer):
                return False
            continue
        if not any(o.path == span.path and o.start <= span.start and span.end <= o.end for o in outer):
            return False
    return True


def _intersects(a: Region, b: Region) -> bool:
    return any(x.path == y.path and x.start < y.end and y.start < x.end for x in a for y in b)


class TreeView:
    def __init__(self, tree: Tree, structure: Structure, manifest_path: str = DEFAULT_MANIFEST_PATH) -> None:
        self.tree = tree
        self.structure = structure
        self.manifest_path = manifest_path

    # -- governed content and resolution -------------------------------------------------

    @cached_property
    def governed_paths(self) -> tuple[str, ...]:
        return tuple(p for p in self.tree if self.structure.governed(p))

    def governed(self, path: str) -> bool:
        return path in self.tree and self.structure.governed(path)

    def term_region(self, term: Term) -> Region | None:
        """One scope term's §1.3 resolution in this tree, before any ownership test; None is ``ABSENT``."""

        return resolve(term, self.tree, self.governed).region

    @cached_property
    def term_resolutions(self) -> dict[str, tuple[Region | None, ...]]:
        """Each unit's terms resolved by §1.3, in declared order."""

        out = {}
        for uid, unit in self.structure.units.items():
            out[uid] = tuple(resolve(t, self.tree, self.governed).region for t in unit.scope)
        return out

    @cached_property
    def _malformed(self) -> frozenset[str]:
        bad = set()
        for uid, unit in self.structure.units.items():
            for term in unit.scope:
                if term.kind == "anchor" and resolve(term, self.tree, self.governed).malformed_anchor:
                    bad.add(uid)
        return frozenset(bad)

    @cached_property
    def initial_regions(self) -> dict[str, Region | None]:
        """A unit's §1.3 region: the union of its resolved terms; ABSENT when none resolves."""

        out: dict[str, Region | None] = {}
        for uid, resolutions in self.term_resolutions.items():
            spans = [s for r in resolutions if r is not None for s in r]
            out[uid] = _merge(tuple(spans)) if any(r is not None for r in resolutions) else ABSENT
        return out

    @cached_property
    def _partition_tests(self) -> tuple[dict[str, Region | None], tuple[IntegrityFinding, ...]]:
        initial = self.initial_regions
        absent: set[str] = set()
        findings: list[IntegrityFinding] = []
        units = sorted(u for u, r in initial.items() if r is not ABSENT and u != UNCLASSIFIED)
        for i, a in enumerate(units):
            for b in units[i + 1 :]:
                if self.structure.is_member_of(a, b) or self.structure.is_member_of(b, a):
                    continue
                ra, rb = initial[a], initial[b]
                assert ra is not None and rb is not None
                equal = ra == rb
                partial = _intersects(ra, rb) and not _contains(ra, rb) and not _contains(rb, ra)
                if equal or partial:
                    absent.update((a, b))
                    findings.append(IntegrityFinding("REGION_OVERLAP", a, f"{a} and {b} {'coincide' if equal else 'partially overlap'}"))
        for uid in units:
            parent = self.structure.units[uid].part_of
            if parent is None or initial.get(parent) is ABSENT or parent not in initial:
                continue
            outer, inner = initial[parent], initial[uid]
            assert outer is not None and inner is not None
            if not _contains(outer, inner):
                absent.add(uid)
                findings.append(IntegrityFinding("MEMBER_OUTSIDE", uid, f"{uid} lies outside composite {parent}"))
        for uid in sorted(self._malformed):
            findings.append(IntegrityFinding("ANCHOR_MALFORMED", uid, "an anchor is ambiguous, unbalanced or crossed"))
        final = {u: (ABSENT if u in absent else r) for u, r in initial.items()}
        return final, tuple(sorted(set(findings)))

    @property
    def regions(self) -> dict[str, Region | None]:
        """Each unit's region after the dynamic partition tests (§1.4 rule 3). The outermost owner's is exactly the
        bytes it owns, those no other unit's region contains (Manual §1.8; plan reading F19): every reader of a
        region, from write-scope containment to ``owners``, sees it so."""

        final = self._partition_tests[0]
        if final.get(UNCLASSIFIED) in (None, ABSENT):
            return final
        owned = tuple(Span(path, seg.start, seg.end) for path, segments in sorted(self.ownership.items())
                      for seg in segments if seg.owner == UNCLASSIFIED)
        return {**final, UNCLASSIFIED: _merge(owned)}

    @cached_property
    def integrity_findings(self) -> tuple[IntegrityFinding, ...]:
        findings = list(self._partition_tests[1])
        if isinstance(self.manifest, tuple):
            findings.append(IntegrityFinding("MANIFEST_UNPARSED", "ssds.manifest", self.manifest[1]))
        return tuple(sorted(set(findings)))

    # -- ownership ------------------------------------------------------------------------

    @cached_property
    def ownership(self) -> dict[str, tuple[Segment, ...]]:
        """Governed path -> owner segments, by innermost ownership, residual and uncovered."""

        regions = {u: r for u, r in self._partition_tests[0].items() if r is not ABSENT}
        depth = {u: len(self.structure.ancestors(u)) for u in regions}
        size = {u: _bytes_of(r) for u, r in regions.items()}  # type: ignore[arg-type]
        by_path: dict[str, list[tuple[str, Span]]] = {}
        for uid, region in regions.items():
            assert region is not None
            for span in region:
                by_path.setdefault(span.path, []).append((uid, span))
        out: dict[str, tuple[Segment, ...]] = {}
        for path in self.governed_paths:
            length = len(self.tree[path].data)
            candidates = by_path.get(path, [])
            cuts = {0, length}
            for _, span in candidates:
                cuts.update((span.start, span.end))
            points = sorted(c for c in cuts if 0 <= c <= length)
            pieces = list(zip(points, points[1:])) or [(0, 0)]
            segments: list[Segment] = []
            for start, end in pieces:
                if start == end and length:
                    continue
                holders = [
                    uid for uid, span in candidates
                    if (span.start <= start and end <= span.end and start < end) or (start == end and span.path == path)
                ]
                owner = UNCOVERED
                if holders:
                    holders.sort(key=lambda u: (u == UNCLASSIFIED, size[u], -depth[u], u))
                    best = holders[0]
                    owner = best + RESIDUAL_SUFFIX if self.structure.units[best].composite else best
                if segments and segments[-1].owner == owner and segments[-1].end == start:
                    segments[-1] = Segment(segments[-1].start, end, owner)
                else:
                    segments.append(Segment(start, end, owner))
            out[path] = tuple(segments)
        return out

    def owner_of_line(self, path: str, offset: int) -> str:
        for segment in self.ownership.get(path, ()):
            if segment.start <= offset < segment.end or (segment.start == segment.end == offset):
                return segment.owner
        return UNCOVERED

    @cached_property
    def owned(self) -> dict[str, dict[str, tuple[str, bytes]]]:
        """Owner -> {path: (entry mode, normalized owned bytes)} in the §1.5 representation."""

        out: dict[str, dict[str, tuple[str, bytes]]] = {}
        for path, segments in self.ownership.items():
            entry = self.tree[path]
            for segment in segments:
                current = out.setdefault(segment.owner, {})
                piece = normalized(path, entry.data, segment.start, segment.end)
                mode, sofar = current.get(path, (entry.mode, b""))
                current[path] = (mode, sofar + piece)
        return out

    # -- identities (§1.5) ----------------------------------------------------------------

    def cid(self, term: Term, region: Region | None) -> str:
        args = _jcs(term.to_json())
        if region is ABSENT:
            entry = self.tree.get(term.file) if term.kind != "prefix" else None
            return _hash(b"ssds.cid.v1", term.kind.encode(), args, (entry.mode if entry else "").encode(), b"ABSENT")
        if term.kind == "prefix":
            files = []
            for span in region:
                entry = self.tree[span.path]
                body = normalized(span.path, entry.data, 0, len(entry.data))
                files.append(_field(span.path.encode("utf-8")) + _field(entry.mode.encode()) + _field(body))
            return _hash(b"ssds.cid.v1", term.kind.encode(), args, b"", b"RESOLVED", b"".join(files))
        entry = self.tree[term.file]
        body = b"".join(normalized(s.path, entry.data, s.start, s.end) for s in region)
        return _hash(b"ssds.cid.v1", term.kind.encode(), args, entry.mode.encode(), b"RESOLVED", body)

    def content(self, uid: str) -> str:
        if uid == UNCLASSIFIED:
            # the outermost owner's content is the bytes it owns, never every governed byte its empty prefix
            # resolves to (Manual §1.8, §1.4 rule 3; plan reading F19)
            owned = self.owned.get(UNCLASSIFIED, {})
            parts = [_jcs([path, mode, data.hex()]) for path, (mode, data) in sorted(owned.items())]
            return _hash(b"ssds.content.v1", b"ssds.unclassified.owned", *parts)
        unit = self.structure.units[uid]
        cids = [self.cid(t, r).encode() for t, r in zip(unit.scope, self.term_resolutions[uid])]
        return _hash(b"ssds.content.v1", *cids)

    def inside(self, uid: str) -> tuple[str, ...]:
        """``uid``, its members (transitively) and every unit whose region lies inside its region."""

        region = self.regions.get(uid)
        found = {uid}
        if uid == UNCLASSIFIED:
            return (uid,)  # it contains no unit: it owns only what no other unit contains (reading F19)
        for other in self.structure.units:
            if other == uid:
                continue
            if self.structure.is_member_of(other, uid):
                found.add(other)
                continue
            other_region = self.regions.get(other)
            if region and other_region and _contains(region, other_region):
                found.add(other)
        return tuple(sorted(found))

    def sem(self, uid: str) -> str:
        owners = set(self.inside(uid))
        owners.update(u + RESIDUAL_SUFFIX for u in list(owners))
        declarations = [d for d in self.semantic_declarations if d["unit"] in owners]
        ordered = sorted(declarations, key=_jcs)
        return "sha256:" + hashlib.sha256(_jcs(ordered)).hexdigest()

    def rev(self, uid: str) -> str:
        return _hash(b"ssds.rev.v1", self.content(uid).encode(), self.sem(uid).encode())

    def scope_id(self, uid: str) -> str:
        return scope_identity(self.structure.units[uid].scope)

    def membership_digest(self, scope: tuple[str, ...] | list[str] | frozenset[str]) -> str:
        """The membership of a completeness scope: ``sha256`` of its sorted ``(id, scope_id)`` pairs (§2.6, §4.3)."""

        pairs = [[u, self.scope_id(u)] for u in sorted(set(scope)) if u in self.structure.units]
        return "sha256:" + hashlib.sha256(_jcs(pairs)).hexdigest()

    # -- semantic declarations (§1.7) -----------------------------------------------------

    @cached_property
    def manifest(self) -> Manifest | tuple[str, str] | None:
        entry = self.tree.get(self.manifest_path)
        if entry is None:
            return None
        parsed = parse_manifest(entry.data)
        return parsed if isinstance(parsed, Manifest) else (parsed.reason, parsed.detail)

    @cached_property
    def semantic_declarations(self) -> tuple[dict[str, Any], ...]:
        """Every semantic declaration, attributed to the unit it belongs to."""

        out: list[dict[str, Any]] = []
        if isinstance(self.manifest, Manifest):
            for uid, items in self.manifest.semantic.items():
                out.extend({**item, "unit": uid} for item in items)
        for path in self.governed_paths:
            entry = self.tree[path]
            if not entry.is_text_file:
                continue
            for directive in directives(path, entry.data):
                item = _inline(directive.verb, directive.args)
                if item is None:
                    continue
                offset = _line_start(entry.data, directive.line)
                out.append({**item, "unit": self.owner_of_line(path, offset)})
        return tuple(out)

    def authored_relations(self) -> tuple[tuple[str, str, str, dict[str, str]], ...]:
        """(subject, type, object, attrs) for every authored relation, the subject being its declaring unit."""

        rels = []
        for d in self.semantic_declarations:
            if d["decl"] == "rel":
                subject = d["unit"][: -len(RESIDUAL_SUFFIX)] if d["unit"].endswith(RESIDUAL_SUFFIX) else d["unit"]
                rels.append((subject, d["type"], d["object"], dict(d["attrs"])))
        return tuple(sorted(rels, key=lambda r: (r[0], r[1], r[2], sorted(r[3].items()))))

    def unresolved_declared_terms(self, previous: Structure | None) -> tuple[str, ...]:
        """Units with a file or span term newly declared or changed since ``previous`` that resolves to ABSENT (§1.9)."""

        out = []
        for uid, unit in self.structure.units.items():
            before = previous.units[uid].scope if previous is not None and uid in previous.units else ()
            for term, region in zip(unit.scope, self.term_resolutions[uid]):
                if term.kind == "prefix" or term in before:
                    continue
                if region is ABSENT:
                    out.append(uid)
                    break
        return tuple(sorted(out))


def scope_identity(scope: tuple[Term, ...]) -> str:
    """``scope_id``: the hash of the declared terms alone, independent of bytes (§1.5, R6)."""

    return _hash(b"ssds.scope.v1", _jcs([t.to_json() for t in scope]))


def _line_start(data: bytes, index: int) -> int:
    position = 0
    for _ in range(index):
        position = data.index(b"\n", position) + 1
    return position


def _inline(verb: str, args: tuple[str, ...]) -> dict[str, Any] | None:
    if verb == "rel" and len(args) >= 2:
        attrs = dict(a.split("=", 1) for a in args[2:] if "=" in a)
        return {"decl": "rel", "type": args[0], "object": args[1], "attrs": attrs}
    if verb == "defines" and len(args) == 1:
        return {"decl": "defines", "object": args[0]}
    if verb == "sdg" and len(args) >= 2:
        return {"decl": "sdg", "id": args[0], "members": sorted(args[1:])}
    if verb == "joint-invariant" and len(args) >= 2:
        return {"decl": "joint_invariant", "id": args[0], "units": sorted(args[1:])}
    return None


def recorded_identity(tree: Tree, term: dict[str, Any], ignore: tuple[str, ...]) -> str:
    """The identity of one recorded term, re-resolved term-level under frozen ``ignore`` patterns (§6.3).

    The overlap rule of §1.4 is not applied: it depends on other units' terms.
    ``{"tracked": "*"}`` is the record-only whole-tree fallback: every tracked
    path, governed or ignored, with its entry mode.
    """

    if term == {"tracked": "*"}:
        files = [_field(p.encode("utf-8")) + _field(tree[p].mode.encode()) + _field(tree[p].data) for p in tree]
        return _hash(b"ssds.cid.v1", b"tracked", b"*", b"RESOLVED", b"".join(files))
    parsed = parse_term(term)
    view = TreeView(tree, Structure({GOVERNED_KEY: tuple(ignore)} if ignore else {}))
    return view.cid(parsed, resolve(parsed, tree, view.governed).region)
