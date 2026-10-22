"""One derivation state: S0 record facts and S1 (catalogue §5.2-§5.4).

A :class:`State` is the admitted state ``D_n`` at a position, or a frame
``D_n[X]`` (§7). It holds the S0 facts that every later stratum reads: which
records act, supersession, target conditions, authorship of content, and the
policy in force; and S1, the challenge tier, computed by recursion on strictly
earlier targets.
"""

from __future__ import annotations

import tomllib
from collections.abc import Iterable
from dataclasses import dataclass, field
from functools import cached_property, lru_cache
from typing import Any

from ssds import analyzers
from ssds.content import Structure, TreeView, scope_identity

from .history import History, RecordFact, manifest_decl
from .s0 import StructureFacts, tenure_start

F, P, T = 0, 1, 2
UNKNOWN = "UNKNOWN"  # authorship with no admitted producing record (catalogue §5.10 (a))

#: Kinds whose acceptance counts in ACC(s), per governance mode (catalogue §5.5, §19.2).
ACCEPTANCE_KINDS = {"NATIVE": ("ACCEPTANCE",), "LEGACY": ("LEGACY_ACCEPTANCE",), "UNGOVERNED": ()}
#: System floors: kinds that need an authenticated human, whatever policy says (catalogue §3.5).
HUMAN_FLOOR = frozenset({"GATE_DECISION", "RISK_OVERRIDE", "CONTINUITY_ATTESTATION", "PRODUCT_SCOPE_ACCEPTANCE",
                         "HUMAN_DECISION", "LINEAGE_ATTESTATION", "NON_AUTHORSHIP_ATTESTATION"})


def triple_key(subject: str, scope_id: str, rev: str) -> str:
    return f"triple:{subject}:{scope_id}:{rev}"


def target_key(target: Any) -> str | None:
    """The key a challenge-tier record targets: a record id or a subject triple."""

    if isinstance(target, dict):
        if "record" in target:
            return target["record"]
        if {"subject", "scope_id", "rev"} <= set(target):
            return triple_key(target["subject"], target["scope_id"], target["rev"])
    return None


@dataclass(frozen=True)
class Policy:
    """Project policy parameters (catalogue §25.3; closed schema 1).

    ``[domains.<D>]`` holds the per-domain table of Phase D reading 2. ``[workflow]`` holds the keys the
    Manual leaves to project policy for the workflow layer (Phase E reading E10); an absent key takes the
    system default, and a value weaker than its system floor is a static error.
    """

    domains: dict[str, dict[str, Any]]
    workflow: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def parse(cls, data: bytes | None) -> Policy:
        if not data:
            return cls({})
        raw = tomllib.loads(data.decode("utf-8"))
        if raw.get("schema") != 1 or not set(raw) <= {"schema", "domains", "workflow"}:
            raise ValueError("policy schema 1 has only schema, [domains.<D>] and [workflow]")
        allowed = {"owner", "adjudicators", "acceptors", "required_judgments", "gates", "gate_holders", "evidence",
                   "claim_owner", "humans", "unattested_agents"}
        for name, table in raw.get("domains", {}).items():
            if not set(table) <= allowed:
                raise ValueError(f"unknown policy key in domain {name}")
        return cls(dict(raw.get("domains", {})), _workflow(raw.get("workflow", {})))

    def get(self, domain: str | None, key: str, default: Any = ()) -> Any:
        return self.domains.get(domain or "", {}).get(key, default)

    def flow(self, key: str) -> Any:
        """A ``[workflow]`` value, or its system default."""

        return self.workflow.get(key, WORKFLOW_DEFAULTS[key])


#: System budget cap and the default a policy may lower (catalogue §13.7).
BUDGET_CAP = 10
#: Obligation kinds no risk override or policy lets discharge provisionally (§10.5).
NEVER_PROVISIONAL = frozenset({"GATE", "HUMAN_ATTENTION", "ADJUDICATE", "INTEGRITY"})
CONCERNS = frozenset({"security", "storage", "concurrency", "performance", "configuration", "release"})
MATERIALITY = ("ROUTINE", "MATERIAL", "CRITICAL")
ITEM_KINDS = frozenset({"IMPLEMENT", "REPAIR", "MIGRATE", "INVESTIGATE", "AUTHOR", "DOCUMENT"})
WORKFLOW_DEFAULTS: dict[str, Any] = {
    "standing_plan": None,  # §12.5: with none, decisions outside every plan go to the human
    "budget": 3,  # §13.7 [proposed default]
    "provisional_kinds": (),  # §10.3, §10.4: kinds policy lets continue provisionally
    "protected_surfaces": (),  # §25.3: units and paths no agent write scope may hold
    "concern_tags": {},  # §16.3: concern -> units whose write-scope intersection injects that owner
    "waive_item_level_review": (),  # §13.7: item kinds whose item-level review policy waives
    "floors": (),  # §15.4: raise-only entries {kind, reason, domain, materiality}
}


def _workflow(raw: Any) -> dict[str, Any]:
    if not isinstance(raw, dict) or not set(raw) <= set(WORKFLOW_DEFAULTS):
        raise ValueError(f"unknown [workflow] key {sorted(set(raw) - set(WORKFLOW_DEFAULTS)) if isinstance(raw, dict) else raw}")

    def strings(key: str, allowed: frozenset[str] | None = None) -> tuple[str, ...]:
        value = raw[key]
        if not isinstance(value, list) or not all(isinstance(v, str) and v for v in value):
            raise ValueError(f"[workflow] {key} is a list of strings")
        if allowed is not None and not set(value) <= allowed:
            raise ValueError(f"[workflow] {key} outside {sorted(allowed)}")
        return tuple(value)

    out: dict[str, Any] = {}
    if "standing_plan" in raw:
        if not isinstance(raw["standing_plan"], str) or not raw["standing_plan"]:
            raise ValueError("[workflow] standing_plan names a plan subject")
        out["standing_plan"] = raw["standing_plan"]
    if "budget" in raw:
        budget = raw["budget"]
        if not isinstance(budget, int) or isinstance(budget, bool) or not 1 <= budget <= BUDGET_CAP:
            raise ValueError(f"[workflow] budget is an integer from 1 to the system cap {BUDGET_CAP}")
        out["budget"] = budget
    if "provisional_kinds" in raw:
        kinds = strings("provisional_kinds")
        if set(kinds) & NEVER_PROVISIONAL:
            raise ValueError(f"[workflow] provisional_kinds may not name {sorted(NEVER_PROVISIONAL)}")
        out["provisional_kinds"] = kinds
    if "protected_surfaces" in raw:
        out["protected_surfaces"] = strings("protected_surfaces")
    if "waive_item_level_review" in raw:
        out["waive_item_level_review"] = strings("waive_item_level_review", ITEM_KINDS)
    if "concern_tags" in raw:
        tags = raw["concern_tags"]
        if not isinstance(tags, dict) or not set(tags) <= CONCERNS:
            raise ValueError(f"[workflow] concern_tags keys are {sorted(CONCERNS)}")
        out["concern_tags"] = {name: tuple(units) for name, units in sorted(tags.items())
                               if isinstance(units, list) and all(isinstance(u, str) for u in units)}
        if len(out["concern_tags"]) != len(tags):
            raise ValueError("[workflow] concern_tags values are lists of units")
    if "floors" in raw:
        floors = []
        for entry in raw["floors"] if isinstance(raw["floors"], list) else [None]:
            if (not isinstance(entry, dict) or not {"kind", "materiality"} <= set(entry)
                    or not set(entry) <= {"kind", "reason", "domain", "materiality"}
                    or entry["materiality"] not in MATERIALITY or not all(isinstance(v, str) for v in entry.values())):
                raise ValueError("[[workflow.floors]] is {kind, materiality[, reason, domain]}, raising only")
            floors.append(dict(sorted(entry.items())))
        out["floors"] = tuple(floors)
    return out


class State:
    """The admitted state at ``position`` (default: the last readable one), or a frame when ``frame`` is given."""

    def __init__(self, history: History, position: int | None = None, frame: Any = None) -> None:
        self.h = history
        self.n = history.last if position is None else position
        if not 0 <= self.n <= history.last:
            raise ValueError("position outside the readable prefix")
        self.frame = frame
        self.view: TreeView = frame.view if frame is not None else history.view(self.n)
        self.s0 = StructureFacts(self.view, manifest_decl(self.view))
        self.records: dict[str, RecordFact] = {
            rid: fact for rid, fact in history.records.items() if fact.position <= self.n
        }

    # -- basic record facts ---------------------------------------------------------------

    def record(self, rid: str) -> dict[str, Any]:
        return self.records[rid].record

    def position_of(self, rid: str) -> int:
        return self.records[rid].position

    @cached_property
    def by_kind(self) -> dict[str, list[str]]:
        out: dict[str, list[str]] = {}
        for rid, fact in sorted(self.records.items(), key=lambda item: (item[1].position, item[0])):
            out.setdefault(fact.record["kind"], []).append(rid)
        return out

    def of_kind(self, *kinds: str) -> list[str]:
        return [rid for kind in kinds for rid in self.by_kind.get(kind, [])]

    @cached_property
    def targeting(self) -> dict[str, list[str]]:
        """Target key -> challenge-tier records targeting it, in position order."""

        out: dict[str, list[str]] = {}
        for rid in self.of_kind("CHALLENGE", "ADJUDICATION", "WITHDRAWAL", "RISK_OVERRIDE"):
            key = target_key(self.record(rid)["target"])
            if key:
                out.setdefault(key, []).append(rid)
        return out

    @cached_property
    def policy(self) -> Policy:
        digest = self.h.ruleset(self.n)["policy"]
        return Policy.parse(self.h.objects.get(digest))

    def mode(self, subject: str) -> str:
        return self.h.mode(self.n, subject).get("mode", "UNGOVERNED")

    # -- enactments and the acting rule (§5.2) ---------------------------------------------

    @cached_property
    def submissions(self) -> dict[str, str]:
        """Transformation id -> the task whose result first submitted it (its enactment)."""

        out: dict[str, str] = {}
        for rid in self.of_kind("TASK_RESULT"):
            target = self.record(rid)["target"]
            if "transformation" in target:
                out.setdefault(target["transformation"], target["task"])
        return out

    def enactment(self, transformation: str) -> str | None:
        return self.submissions.get(transformation)

    @cached_property
    def integrated(self) -> dict[str, int]:
        """Enactment (task) -> the position at which it integrated, at or before n."""

        out: dict[str, int] = {}
        for position, integration in self.h.integrations.items():
            if position <= self.n and integration.transformation:
                task = self.enactment(integration.transformation)
                if task is not None:
                    out.setdefault(task, position)
        return out

    def acts(self, rid: str) -> bool:
        frame = self.record(rid)["frame"]
        if frame == "ADMITTED":
            return True
        task = self.enactment(frame["transformation"])
        if task is not None and task in self.integrated:
            return True
        return self.frame is not None and task is not None and task == self.frame.enactment

    @cached_property
    def supersessions(self) -> dict[str, list[str]]:
        """Record id -> the acting records naming it in ``supersedes``."""

        out: dict[str, list[str]] = {}
        for rid, fact in self.records.items():
            for old in fact.record["supersedes"]:
                if self.acts(rid):
                    out.setdefault(old, []).append(rid)
        return out

    def superseded(self, rid: str) -> bool:
        return bool(self.supersessions.get(rid))

    # -- structure facts in this state -----------------------------------------------------

    def cur(self, unit: str) -> str:
        return self.view.rev(unit)

    def subject_triple(self, subject: str) -> tuple[str, str, str]:
        return subject, self.view.scope_id(subject), self.cur(subject)

    def tenure(self, subject: str) -> int | None:
        """``τ(s)``: the first position of the current run with an unchanged governance signature."""

        signatures = []
        for k in range(self.n + 1):
            structure = Structure(self.h.sigma(k))
            unit = structure.units.get(subject)
            if unit is None or not unit.subject:
                signatures.append(None)
                continue
            scope_id = scope_identity(unit.scope)
            signatures.append((scope_id, structure.kind(subject), tuple(sorted(self.h.mode(k, subject).items()))))
        return tenure_start(signatures)

    def tgt(self, rid: str) -> bool:
        """Target conditions (§5.2)."""

        record = self.record(rid)
        kind = record["kind"]
        if kind == "COMPLETENESS":
            target = record["target"]
            if self.membership_digest(target["scope"]) != target["membership"]:
                return False
            if record["actor_class"] == "MACHINERY":
                return target.get("analyzer") in self.analyzer_set
            return True
        if kind in ("ACCEPTANCE", "GATE_DECISION") and record["outcome"] in ("PASS", "ACCEPT"):
            target = record["target"]["subject"] if kind == "GATE_DECISION" else record["target"]
            subject = target["subject"]
            if self.mode(subject) == "NATIVE" and self.view.structure.kind(subject) in ("D1", "D2"):
                # §10.2: current only in its revision run, and only with its counting premise (reading E19)
                return self.runs.in_run(rid, subject) and self.runs.counting_premise(rid, subject, target["rev"])
        return True

    @cached_property
    def plans(self) -> Any:
        """Plans, lint and amendment classes in this state (§11, §13)."""

        from .plans import PlanFacts

        return PlanFacts(self)

    @cached_property
    def runs(self) -> Any:
        """The revision runs of this state (§10.2)."""

        from .runs import Runs

        return Runs(self)

    def membership_digest(self, scope: Iterable[str]) -> str:
        return self.view.membership_digest(tuple(scope))

    @cached_property
    def analyzer_set(self) -> frozenset[str]:
        """The analyzer set the ruleset in force pins (§5.9): an adoption's list, else the system ruleset's."""

        adopted = self.h.ruleset(self.n).get("analyzers")
        if isinstance(adopted, list):
            return frozenset(adopted)
        return frozenset(analyzers.ANALYZER_SET.values())

    # -- authorship (§5.10 (b)) --------------------------------------------------------------

    @cached_property
    def producers(self) -> dict[tuple[str, str], frozenset[str]]:
        """(unit, revision) -> every actor whose admitted record produced that revision; UNKNOWN when unrecorded."""

        out: dict[tuple[str, str], set[str]] = {}
        previous: TreeView | None = None
        for k in range(self.n + 1):
            current = self.h.view(k)
            if previous is current:
                continue
            integration = self.h.integrations.get(k)
            makers: set[str] = {UNKNOWN}
            if integration is not None and integration.transformation:
                makers = set(self._makers(integration.transformation)) or {UNKNOWN}
            for unit in current.structure.units:
                rev = current.rev(unit)
                before = previous.rev(unit) if previous is not None and unit in previous.structure.units else None
                if before != rev:
                    out.setdefault((unit, rev), set()).update(makers)
            previous = current
        return {key: frozenset(value) for key, value in out.items()}

    def _makers(self, transformation: str) -> list[str]:
        for rid in self.of_kind("TASK_RESULT"):
            record = self.record(rid)
            if record["target"].get("transformation") == transformation:
                binding = record["binding"] or {}
                return list(binding.get("lineage") or [record["actor"]])
        return []

    def authors(self, unit: str, rev: str) -> frozenset[str]:
        return self.producers.get((unit, rev), frozenset({UNKNOWN}))

    # -- S1: the challenge tier (§5.3) -----------------------------------------------------

    def _rec(self, rid: str) -> dict[str, Any] | None:
        fact = self.records.get(rid)
        return fact.record if fact else None

    @lru_cache(maxsize=None)  # noqa: B019
    def restrictive(self, rid: str) -> bool:
        a = self._rec(rid)
        return bool(a and a["kind"] == "ADJUDICATION" and a["outcome"] == "UPHELD"
                    and not self.counter(a["target"]["record"]))

    @lru_cache(maxsize=None)  # noqa: B019
    def counter(self, rid: str) -> bool:
        c = self._rec(rid)
        if not c or c["kind"] != "CHALLENGE":
            return False
        key = target_key(c["target"])
        return key is not None and key in self.records and self.restrictive(key)

    @lru_cache(maxsize=None)  # noqa: B019
    def relaxer(self, rid: str) -> bool:
        y = self._rec(rid)
        if not y:
            return False
        if y["kind"] in ("WITHDRAWAL", "RISK_OVERRIDE", "CONTINUITY_ATTESTATION"):
            return True
        if y["kind"] == "ADJUDICATION":
            target = y["target"]["record"]
            return (y["outcome"] == "DISMISSED" and not self.counter(target)) or \
                (y["outcome"] == "UPHELD" and self.counter(target))
        return False

    def boundaries_after(self, rid: str) -> list[int]:
        position = self.position_of(rid) if rid in self.records else -1
        return [b for b in self.h.boundaries if b <= self.n and position < b]

    @lru_cache(maxsize=None)  # noqa: B019
    def cont(self, rid: str) -> bool:
        """``cont(x)``: held across every later loss boundary (§5.3, §23.7)."""

        return all(self.held(rid, b) for b in self.boundaries_after(rid))

    def held(self, rid: str, boundary: int) -> bool:
        loss_ids = [r for r in self.of_kind("LEDGER_LOSS") if self.position_of(r) == boundary]
        for attestation in self.of_kind("CONTINUITY_ATTESTATION"):
            record = self.record(attestation)
            if record["target"].get("loss") not in loss_ids or not self.in_force(attestation):
                continue
            listed = set(record["fields"]["listed"])
            covered = self._exposed(rid, listed)
            if (record["fields"]["scope_form"] == "COMPLEMENT" and not covered) or \
                    (record["fields"]["scope_form"] == "EXPLICIT" and covered):
                return True
        return False

    def _exposed(self, rid: str, listed: set[str]) -> bool:
        seen: set[str] = set()
        current: str | None = rid
        while current and current not in seen:
            if current in listed:
                return True
            seen.add(current)
            record = self._rec(current)
            if record is None:
                return False
            target = record["target"]
            if isinstance(target, dict) and target.get("subject") in listed:
                return True
            current = target_key(target) if isinstance(target, dict) else None
        return False

    def gate(self, rid: str) -> bool:
        return self.cont(rid) if self.relaxer(rid) else True

    @lru_cache(maxsize=None)  # noqa: B019
    def in_force(self, rid: str) -> bool:
        if not self.gate(rid):
            return False
        for c in self.targeting.get(rid, []):
            record = self.record(c)
            if record["kind"] != "CHALLENGE":
                continue
            if self.upheld(c) or (record["fields"]["blocking"] and self.open(c) and not self.counter(c)):
                return False
        return True

    @lru_cache(maxsize=None)  # noqa: B019
    def open(self, cid: str) -> bool:
        return not any(self.record(y)["kind"] in ("ADJUDICATION", "WITHDRAWAL") and self.in_force(y)
                       for y in self.targeting.get(cid, []))

    @lru_cache(maxsize=None)  # noqa: B019
    def upheld(self, cid: str) -> bool:
        return any(self.record(a)["kind"] == "ADJUDICATION" and self.record(a)["outcome"] == "UPHELD"
                   and self.in_force(a) for a in self.targeting.get(cid, []))

    def overridden(self, cid: str) -> bool:
        return self.open(cid) and any(self.record(o)["kind"] == "RISK_OVERRIDE" and self.in_force(o)
                                      for o in self.targeting.get(cid, []))

    @lru_cache(maxsize=None)  # noqa: B019
    def status1(self, key: str) -> str:
        """``REVOKED``, ``BLOCKED``, ``PROVISIONAL`` or ``CLEAR`` for a record id or triple key (§5.3)."""

        challenges = [c for c in self.targeting.get(key, []) if self.record(c)["kind"] == "CHALLENGE"]
        if any(self.upheld(c) for c in challenges):
            return "REVOKED"
        blocking_open = [c for c in challenges if self.record(c)["fields"]["blocking"] and self.open(c)]
        if any(not self.overridden(c) for c in blocking_open):
            return "BLOCKED"
        if blocking_open:
            return "PROVISIONAL"
        return "CLEAR"
