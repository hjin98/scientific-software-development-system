"""Change plans: the Objective part, item declarations and work contracts (catalogue §11.1, §13.1).

A plan is a ``PLAN`` subject whose manifest declares its parts. The part whose
region opens with the heading ``Objective`` is the objective part; every other
part holding a fenced ``ssds-item`` block is an item, its block a data-only
TOML document under a closed schema. Parsing never executes content (T2) and
never resolves units in ``Σ``: write scopes, affected units and verifiers are
kept as written, and lint (an S3 function of derivation) judges them. A part
whose block is missing, repeated, unparsable or outside the grammar yields an
:class:`ItemFailure`, which lint reports.
"""

from __future__ import annotations

import re
import tomllib
from dataclasses import dataclass
from functools import cached_property
from typing import Any

from .lines import directives, split_lines
from .manifest import ID_RE, SEGMENT_RE
from .resolve import ATX_HEADING, FENCE_OPEN, Span
from .structure import Structure
from .view import ABSENT, TreeView

ITEM_INFO = "ssds-item"
OBJECTIVE = "Objective"
ITEM_KINDS = frozenset({"IMPLEMENT", "REPAIR", "MIGRATE", "INVESTIGATE", "AUTHOR", "DOCUMENT"})
AUTHORITIES = frozenset({"D1", "D2", "D3"})
SPECIALISTS = frozenset({"MAINTENANCE_AUDIT", "REPOSITORY_HYGIENE"})
SCIENTIFIC = frozenset({"APPLIES", "NOT_APPLIES"})
#: The result-slot vocabulary (catalogue §13.5).
SLOTS = frozenset(
    {"deviations", "unverified_assumptions", "claims", "findings", "null_envelope", "variant_search", "tension_search",
     "choices", "retention", "delegate_returns", "bidirectional", "o1_content", "revision_assessments",
     "audit_conclusion"}
)
REVIEW = "REVIEW"
_TOKEN = re.compile(r"^[A-Z][A-Z0-9_]{0,62}$")
_TEMPLATE = re.compile(r"^[A-Z][A-Z_]*\.[A-Za-z][A-Za-z_]*$")
_REVISION = re.compile(r"^sha256:[0-9a-f]{64}$")
_ITEM_KEYS = frozenset(
    {"item", "kind", "authority", "specialist", "objective", "governing", "acceptance_criteria", "affected", "gates",
     "depends_on", "contract"}
)
_CONTRACT_KEYS = frozenset({"scientific", "budget", "boundaries", "obligations", "expectations", "escalation"})
_BOUNDARY_KEYS = frozenset({"write_scope", "frozen", "dependencies", "evidence_specs", "homes"})
_OBLIGATION_KEYS = frozenset({"id", "statement", "verifier", "secondary"})
_EXPECTATION_KEYS = frozenset({"artifacts", "evidence", "slots"})


@dataclass(frozen=True)
class Ref:
    """A ``{ ref = "#name" }`` prose reference, resolved only in the item's part and the Objective (§13.2)."""

    name: str


@dataclass(frozen=True)
class Check:
    template: str  # FAMILY.template
    params: tuple[tuple[str, Any], ...] = ()


@dataclass(frozen=True)
class EvidenceVerifier:
    spec: str
    runner: str


Verifier = Check | EvidenceVerifier | str  # str: REVIEW


@dataclass(frozen=True)
class ContractObligation:
    id: str
    statement: Ref
    verifier: Verifier
    secondary: tuple[Check, ...] = ()


@dataclass(frozen=True)
class Contract:
    scientific: str
    budget: int
    write_scope: tuple[str, ...]
    frozen: tuple[str, ...]
    dependencies: tuple[tuple[str, tuple[str, ...]], ...]
    evidence_specs: tuple[str, ...]
    homes: tuple[str, ...]
    obligations: tuple[ContractObligation, ...]
    artifacts: tuple[str, ...]
    evidence: tuple[str, ...]
    slots: tuple[str, ...]
    triggers: tuple[str, ...]


@dataclass(frozen=True)
class Item:
    id: str
    kind: str
    objective: Ref
    governing: tuple[tuple[str, str], ...]  # (unit, revision)
    acceptance_criteria: tuple[tuple[str, str], ...]  # (id, evidence specification or REVIEW)
    affected: tuple[str, ...]
    gates: tuple[str, ...]
    depends_on: tuple[str, ...]
    contract: Contract | None  # None: no contract yet, a CONTRACT obligation (§10.2)
    authority: str | None = None
    specialist: str | None = None

    @property
    def refs(self) -> tuple[Ref, ...]:
        found = [self.objective]
        if self.contract is not None:
            found.extend(o.statement for o in self.contract.obligations)
        return tuple(found)


@dataclass(frozen=True)
class ItemFailure:
    reason: str  # NO_BLOCK | BLOCKS | PARSE | GRAMMAR
    detail: str


class _Grammar(ValueError):
    pass


@dataclass(frozen=True)
class ItemPart:
    """One item part: its unit, the parsed item or failure, its block and the prose outside it."""

    unit: str
    path: str
    span: Span
    block: Span | None
    parsed: Item | ItemFailure

    def prose(self, data: bytes) -> bytes:
        """Every byte of the part outside its ``ssds-item`` block (the tightening comparison, §13.4)."""

        if self.block is None:
            return data[self.span.start : self.span.end]
        return data[self.span.start : self.block.start] + data[self.block.end : self.span.end]


class Plan:
    """The parts of one ``PLAN`` subject in one tree view."""

    def __init__(self, view: TreeView, subject: str) -> None:
        self.view = view
        self.subject = subject
        structure: Structure = view.structure
        self.parts = tuple(sorted(u for u in structure.units if u != subject and structure.is_member_of(u, subject)))

    def _single_span(self, uid: str) -> Span | None:
        region = self.view.regions.get(uid)
        if region is ABSENT or region is None or len(region) != 1:
            return None
        return region[0]

    def _data(self, path: str) -> bytes:
        return self.view.tree[path].data

    @cached_property
    def objective(self) -> str | None:
        """The one part whose region opens with the heading ``Objective``; None when none or several."""

        found = []
        for uid in self.parts:
            span = self._single_span(uid)
            if span is None:
                continue
            first = split_lines(self._data(span.path)[span.start : span.end])
            match = ATX_HEADING.match(first[0].text.decode("utf-8", "replace")) if first else None
            if match and (match.group(2) or "").strip() == OBJECTIVE:
                found.append(uid)
        return found[0] if len(found) == 1 else None

    @cached_property
    def items(self) -> dict[str, ItemPart]:
        """Item part unit -> its parse. A part with no block that is not the objective is not an item."""

        out: dict[str, ItemPart] = {}
        for uid in self.parts:
            if uid == self.objective:
                continue
            span = self._single_span(uid)
            if span is None:
                continue
            data = self._data(span.path)
            blocks = _item_blocks(data, span)
            if not blocks:
                continue
            if len(blocks) > 1:
                out[uid] = ItemPart(uid, span.path, span, None, ItemFailure("BLOCKS", f"{len(blocks)} {ITEM_INFO} blocks"))
                continue
            fence, body = blocks[0]
            out[uid] = ItemPart(uid, span.path, span, fence, parse_item(data[body.start : body.end]))
        return out

    def resolve_ref(self, item_unit: str, ref: Ref) -> tuple[Span, ...]:
        """Every span ``ref`` names inside the item's own part and the objective part, nothing else (§13.2).

        ``#name`` names an inline anchor ``name`` or a heading whose slug is ``name`` (Phase E plan, E16).
        Lint requires exactly one.
        """

        found: list[Span] = []
        for uid in (item_unit, self.objective):
            if uid is None:
                continue
            span = self._single_span(uid)
            if span is None:
                continue
            found.extend(_named_spans(span.path, self._data(span.path), span, ref.name))
        return tuple(sorted(found))


def plans(view: TreeView) -> dict[str, Plan]:
    """Every top-level ``PLAN`` subject of the view, by unit."""

    structure = view.structure
    return {
        uid: Plan(view, uid)
        for uid in structure.units
        if structure.kind(uid) == "PLAN" and structure.units[uid].composite and structure.subj(uid) == uid
    }


def _item_blocks(data: bytes, span: Span) -> list[tuple[Span, Span]]:
    """The fenced ``ssds-item`` blocks inside ``span``: (whole fence, body)."""

    found: list[tuple[Span, Span]] = []
    fence: tuple[str, int, bool] | None = None  # marker, start offset, is an item block
    body_start = 0
    for line in split_lines(data[span.start : span.end]):
        text = line.text.decode("utf-8", "replace")
        marker = FENCE_OPEN.match(text)
        if fence is None:
            if marker:
                info = text.strip()[len(marker.group(1)) :].strip()
                fence = (marker.group(1), span.start + line.start, info == ITEM_INFO)
                body_start = span.start + line.end
            continue
        closes = marker and marker.group(1)[0] == fence[0][0] and len(marker.group(1)) >= len(fence[0])
        if closes and text.strip() == marker.group(1):
            if fence[2]:
                found.append((Span(span.path, fence[1], span.start + line.end), Span(span.path, body_start, span.start + line.start)))
            fence = None
    return found


def _slug(title: str) -> str:
    lowered = title.strip().lower()
    kept = "".join(ch for ch in lowered if ch.isalnum() or ch in " -_")
    return re.sub(r" ", "-", kept)


def _named_spans(path: str, data: bytes, within: Span, name: str) -> list[Span]:
    """Spans named ``name`` inside ``within`` only: one per anchor pair or matching heading.

    An unbalanced or repeated anchor of that name inside ``within`` yields more than one entry, so
    lint never finds exactly one; markers and headings outside ``within`` are never read.
    """

    lines = [line for line in split_lines(data) if within.start <= line.start and line.end <= within.end]
    found: list[Span] = []
    marks = [d for d in directives(path, data) if d.verb in ("begin", "end") and d.args == (name,)]
    by_index = {line.index: line for line in split_lines(data)}
    begins = [d.line for d in marks if d.verb == "begin" and within.start <= by_index[d.line].start < within.end]
    ends = [d.line for d in marks if d.verb == "end" and within.start <= by_index[d.line].start < within.end]
    if len(begins) == len(ends) == 1 and begins[0] < ends[0]:
        found.append(Span(path, by_index[begins[0]].end, by_index[ends[0]].start))
    elif begins or ends:
        found.extend([Span(path, within.start, within.start)] * 2)  # malformed: never exactly one
    fence: str | None = None
    headings: list[tuple[int, int]] = []  # position in ``lines``, level
    for position, line in enumerate(lines):
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
        if match and _slug(match.group(2) or "") == name:
            headings.append((position, len(match.group(1))))
    for position, level in headings:
        end = within.end
        for later in lines[position + 1 :]:
            match = ATX_HEADING.match(later.text.decode("utf-8", "replace"))
            if match and len(match.group(1)) <= level:
                end = later.start
                break
        found.append(Span(path, lines[position].start, end))
    return found


# -- the closed item schema (§11.1, §13.1) ---------------------------------------------------------


def parse_item(body: bytes) -> Item | ItemFailure:
    try:
        raw = tomllib.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as exc:
        return ItemFailure("PARSE", str(exc))
    try:
        return _item(raw)
    except _Grammar as exc:
        return ItemFailure("GRAMMAR", str(exc))


def _keys(table: Any, allowed: frozenset[str], required: frozenset[str], what: str) -> dict[str, Any]:
    if not isinstance(table, dict):
        raise _Grammar(f"{what} is a table")
    unknown = set(table) - allowed
    if unknown:
        raise _Grammar(f"unknown {what} key {sorted(unknown)}")
    missing = required - set(table)
    if missing:
        raise _Grammar(f"missing {what} key {sorted(missing)}")
    return table


def _strings(value: Any, what: str, pattern: re.Pattern[str] | None = None) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(isinstance(v, str) and v for v in value):
        raise _Grammar(f"{what} is a list of strings")
    if pattern is not None and not all(pattern.match(v) for v in value):
        raise _Grammar(f"{what} outside its grammar")
    if len(set(value)) != len(value):
        raise _Grammar(f"{what} repeats an entry")
    return tuple(value)


def _ref(value: Any, what: str) -> Ref:
    table = _keys(value, frozenset({"ref"}), frozenset({"ref"}), what)
    ref = table["ref"]
    if not isinstance(ref, str) or not ref.startswith("#") or not SEGMENT_RE.match(ref[1:]):
        raise _Grammar(f"{what} is a ref '#name'")
    return Ref(ref[1:])


def _check(value: Any, what: str) -> Check:
    table = _keys(value, frozenset({"check", "params"}), frozenset({"check"}), what)
    if not isinstance(table["check"], str) or not _TEMPLATE.match(table["check"]):
        raise _Grammar(f"{what} names a template FAMILY.template")
    params = table.get("params", {})
    if not isinstance(params, dict):
        raise _Grammar(f"{what} params is a table")
    return Check(table["check"], tuple(sorted(params.items())))


def _verifier(value: Any) -> Verifier:
    if value == REVIEW:
        return REVIEW
    if isinstance(value, dict) and "check" in value:
        return _check(value, "verifier")
    table = _keys(value, frozenset({"evidence", "runner"}), frozenset({"evidence", "runner"}), "verifier")
    if not isinstance(table["evidence"], str) or not ID_RE.match(table["evidence"]):
        raise _Grammar("an evidence verifier names a specification unit")
    if not isinstance(table["runner"], str) or not table["runner"]:
        raise _Grammar("an evidence verifier names a runner class")
    return EvidenceVerifier(table["evidence"], table["runner"])


def _contract(raw: Any) -> Contract:
    table = _keys(raw, _CONTRACT_KEYS, frozenset({"scientific", "budget", "boundaries", "obligations"}), "contract")
    if table["scientific"] not in SCIENTIFIC:
        raise _Grammar("scientific is APPLIES or NOT_APPLIES")
    budget = table["budget"]
    if not isinstance(budget, int) or isinstance(budget, bool) or budget < 1:
        raise _Grammar("budget is a positive integer")
    bounds = _keys(table["boundaries"], _BOUNDARY_KEYS, frozenset({"write_scope"}), "contract.boundaries")
    dependencies = bounds.get("dependencies", {})
    if not isinstance(dependencies, dict):
        raise _Grammar("dependencies is a table of languages")
    deps = tuple(sorted((lang, _strings(reqs, f"dependencies.{lang}")) for lang, reqs in dependencies.items()))
    obligations_raw = table["obligations"]
    if not isinstance(obligations_raw, list) or not obligations_raw:
        raise _Grammar("a contract has at least one obligation")
    obligations = []
    for raw_obligation in obligations_raw:
        ob = _keys(raw_obligation, _OBLIGATION_KEYS, frozenset({"id", "statement", "verifier"}), "obligation")
        if not isinstance(ob["id"], str) or not SEGMENT_RE.match(ob["id"]):
            raise _Grammar("an obligation id follows the segment grammar")
        secondary = ob.get("secondary", [])
        if not isinstance(secondary, list):
            raise _Grammar("secondary is a list of checks")
        obligations.append(ContractObligation(ob["id"], _ref(ob["statement"], "statement"), _verifier(ob["verifier"]),
                                              tuple(_check(c, "secondary check") for c in secondary)))
    if len({o.id for o in obligations}) != len(obligations):
        raise _Grammar("obligation ids are unique")
    expect = _keys(table.get("expectations", {}), _EXPECTATION_KEYS, frozenset(), "contract.expectations")
    slots = _strings(expect.get("slots", []), "slots")
    if not set(slots) <= SLOTS:
        raise _Grammar(f"unknown slot {sorted(set(slots) - SLOTS)}")
    escalation = _keys(table.get("escalation", {}), frozenset({"triggers"}), frozenset(), "contract.escalation")
    return Contract(
        scientific=table["scientific"],
        budget=budget,
        write_scope=_strings(bounds["write_scope"], "write_scope"),
        frozen=_strings(bounds.get("frozen", []), "frozen"),
        dependencies=deps,
        evidence_specs=_strings(bounds.get("evidence_specs", []), "evidence_specs", ID_RE),
        homes=_strings(bounds.get("homes", []), "homes"),
        obligations=tuple(obligations),
        artifacts=_strings(expect.get("artifacts", []), "artifacts"),
        evidence=_strings(expect.get("evidence", []), "evidence", ID_RE),
        slots=slots,
        triggers=_strings(escalation.get("triggers", []), "triggers", _TOKEN),
    )


def _item(raw: dict[str, Any]) -> Item:
    table = _keys(raw, _ITEM_KEYS, frozenset({"item", "kind", "objective"}), "item")
    if not isinstance(table["item"], str) or not SEGMENT_RE.match(table["item"]):
        raise _Grammar("an item id follows the segment grammar")
    kind = table["kind"]
    if kind not in ITEM_KINDS:
        raise _Grammar(f"item kind {kind!r} outside {sorted(ITEM_KINDS)}")
    authority = table.get("authority")
    if (kind == "AUTHOR") != (authority is not None) or (authority is not None and authority not in AUTHORITIES):
        raise _Grammar("an AUTHOR item, and only one, declares one authority domain D1, D2 or D3")
    specialist = table.get("specialist")
    if specialist is not None and (kind != "INVESTIGATE" or specialist not in SPECIALISTS):
        raise _Grammar("only an INVESTIGATE item declares a specialist, MAINTENANCE_AUDIT or REPOSITORY_HYGIENE")
    governing = []
    for entry in _strings(table.get("governing", []), "governing"):
        unit, sep, revision = entry.partition("@")
        if not sep or not ID_RE.match(unit) or not _REVISION.match(revision):
            raise _Grammar("a governing entry is '<unit>@sha256:<revision>'")
        governing.append((unit, revision))
    criteria = []
    for raw_criterion in table.get("acceptance_criteria", []):
        criterion = _keys(raw_criterion, frozenset({"id", "evidence"}), frozenset({"id", "evidence"}), "acceptance criterion")
        if not isinstance(criterion["id"], str) or not SEGMENT_RE.match(criterion["id"]):
            raise _Grammar("an acceptance criterion id follows the segment grammar")
        evidence = criterion["evidence"]
        if not isinstance(evidence, str) or not (evidence == REVIEW or ID_RE.match(evidence)):
            raise _Grammar("an acceptance criterion names an evidence specification or REVIEW")
        criteria.append((criterion["id"], evidence))
    if len({c for c, _ in criteria}) != len(criteria):
        raise _Grammar("acceptance criterion ids are unique")
    return Item(
        id=table["item"],
        kind=kind,
        objective=_ref(table["objective"], "objective"),
        governing=tuple(governing),
        acceptance_criteria=tuple(criteria),
        affected=_strings(table.get("affected", []), "affected"),
        gates=_strings(table.get("gates", []), "gates"),
        depends_on=_strings(table.get("depends_on", []), "depends_on", SEGMENT_RE),
        contract=_contract(table["contract"]) if "contract" in table else None,
        authority=authority,
        specialist=specialist,
    )
