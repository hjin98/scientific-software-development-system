"""One Admission process for one ledger (Manual §8, §22.4; catalogue §8.1-§8.4).

It holds the admitted head, takes requests in queue order, validates each against that head and appends exactly
one entry recording the decision, then distributes the entry's checkpoint to the witness. A repeated identical
request returns the recorded decision and appends nothing.

Phase F step 2 realizes validation steps 1 and 2. Until steps 3-8 exist, a request that passes steps 1 and 2 is
rejected as unsupported (``SCHEMA_UNSUPPORTED``: unknown required semantics fail closed, §8.3 step 1), and no record
is salvaged, since salvage needs an authenticated task binding (step 3). Publication, absorption, the expected head
and the witness quorum beyond ``LOCAL_TRUST`` are step 6's; until then the observed head must equal the expected
head, or nothing is appended.
"""

from __future__ import annotations

import secrets
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any

from ssds.derivation import TreeSource, Workflow, derive
from ssds.ledger.append import append_entry, write_checkpoint
from ssds.ledger.qualification import FileWitness
from ssds.ledger.read import LedgerEntry, read_chain, record_violations

from .checks import record_problems, referenced_records, referenced_revisions, request_problems
from .genesis import AdmissionHome, host_key
from .request import never_lost, request_id

#: The validation steps after step 2 that are not realized yet (Phase F steps 3-5).
UNREALIZED_STEPS = ("authorization", "structure", "dependency", "currency", "legality", "regression")


class AdmissionHalted(RuntimeError):
    """Admission does not append: the observed head is not the expected head (absorption is step 6's)."""


@dataclass(frozen=True)
class Decision:
    request_id: str
    decision: str  # ACCEPT or REJECT
    reasons: tuple[str, ...]
    admitted: tuple[str, ...]  # record ids
    refused: tuple[tuple[str, tuple[str, ...]], ...]
    position: int
    appended: bool  # False when the decision was already recorded


@dataclass
class Admission:
    home: AdmissionHome
    ledger_id: str
    trees: TreeSource
    incarnation_id: str = field(default_factory=lambda: secrets.token_hex(16))
    authenticated: Callable[[Mapping[str, Any]], bool] = field(default=lambda request: False)

    def __post_init__(self) -> None:
        self.home.check(self.ledger_id)
        self.repository = self.home.ledger_repository(self.ledger_id)
        self.key = host_key(self.home, self.ledger_id)
        self.queue: list[Mapping[str, Any]] = []

    # -- the queue (§8.2) ---------------------------------------------------------------------------------------

    def submit(self, request: Mapping[str, Any]) -> None:
        self.queue.append(request)

    def order(self) -> list[Mapping[str, Any]]:
        """Arrival order, except that a request carrying only never-lost records is never delayed behind one that
        may need revalidation (catalogue §8.2): a stable partition keeps arrival order within each class."""

        def only_never_lost(request: Mapping[str, Any]) -> bool:
            records = request.get("records") if isinstance(request, Mapping) else None
            return bool(records) and isinstance(records, list) and not request.get("candidates") \
                and all(isinstance(r, Mapping) and never_lost(r) for r in records)

        return sorted(self.queue, key=lambda r: 0 if only_never_lost(r) else 1)

    def process(self, obs: str) -> list[Decision]:
        decisions = [self.admit(request, obs) for request in self.order()]
        self.queue.clear()
        return decisions

    # -- the held head ------------------------------------------------------------------------------------------

    def chain(self):
        return read_chain(self.repository, self.ledger_id)

    @staticmethod
    def expected_head(entries: Iterable[LedgerEntry]) -> str:
        """The integration head the last entry left: an admission's admitted commit, else the genesis baseline."""

        expected = None
        for entry in entries:
            body = entry.entry
            if body["entry_kind"] == "ADMISSION" and body["admission"]["decision"] == "ACCEPT":
                expected = body["admission"]["admitted_commit"]
            elif body["entry_kind"] == "LIFECYCLE" and body["lifecycle"]["kind"] == "GENESIS":
                expected = body["lifecycle"]["fields"]["baseline_commit"]
        return expected

    @staticmethod
    def recorded(entries: Iterable[LedgerEntry], rid: str) -> LedgerEntry | None:
        return next((e for e in entries if e.entry["entry_kind"] == "ADMISSION"
                     and e.entry["admission"]["request_id"] == rid), None)

    # -- one request --------------------------------------------------------------------------------------------

    def admit(self, request: Mapping[str, Any], obs: str) -> Decision:
        chain = self.chain()
        entries = chain.entries[: chain.readable_through + 1]
        rid = request_id(request) if isinstance(request, Mapping) else request_id({"malformed": repr(request)})
        found = self.recorded(entries, rid)
        if found is not None:
            section = found.entry["admission"]
            return Decision(rid, section["decision"], tuple(section["reasons"]),
                            tuple(r["id"] for r in found.entry["records"]),
                            tuple((x["record_id"], tuple(x["reasons"])) for x in section["refused"]),
                            found.entry["position"], appended=False)
        expected = self.expected_head(entries)
        if obs != expected:
            raise AdmissionHalted(f"the observed head {obs} is not the expected head {expected}")

        reasons, refused = self.validate(request, chain)
        decision = "REJECT" if reasons or refused else "ACCEPT"
        records = list(request["records"]) if isinstance(request, Mapping) and isinstance(request.get("records"), list) else []
        refused_ids = {rid_ for rid_, _ in refused}
        if decision == "ACCEPT":
            admitted = records
        elif isinstance(request, Mapping) and self.authenticated(request):  # never-lost salvage (§8.3 step 6)
            admitted = [r for r in records if isinstance(r, Mapping) and never_lost(r) and r.get("id") not in refused_ids]
        else:
            admitted = []
        objects = {}
        if isinstance(request, Mapping) and isinstance(request.get("objects"), Mapping):
            objects = {d: t.encode("utf-8") for d, t in request["objects"].items() if isinstance(t, str)}
        head = entries[-1]
        entry = {"ledger_id": self.ledger_id, "position": head.entry["position"] + 1, "schema": 1, "prev": head.digest,
                 "entry_kind": "ADMISSION", "host_key_id": self.key.key_id, "incarnation_id": self.incarnation_id,
                 "obs": obs, "absorption": None, "lifecycle": None, "records": admitted,
                 "admission": {"request_id": rid, "decision": decision, "reasons": sorted(reasons),
                               "base_commit": expected, "admitted_commit": expected, "adopted_deltas": [],
                               "integrates": None,
                               "refused": [{"record_id": r, "reasons": list(why)} for r, why in refused]}}
        appended = append_entry(self.repository, entry, self.key, head.commit, objects=objects if admitted else {})
        write_checkpoint(FileWitness(self.home.witness_root), appended.checkpoint)
        return Decision(rid, decision, tuple(sorted(reasons)), tuple(r["id"] for r in admitted), tuple(refused),
                        appended.position, appended=True)

    def validate(self, request: Any, chain) -> tuple[set[str], list[tuple[str, tuple[str, ...]]]]:
        """Steps 1 and 2: request-level reasons, and refused records with theirs."""

        problems = request_problems(request)
        if problems:
            return set(problems), []
        reasons: set[str] = set()
        refused: list[tuple[str, tuple[str, ...]]] = []
        support = derive(chain, self.trees)
        s = support.s
        if request["base_position"] > s.n or request["base_position"] < 0:
            reasons.add("REF_BASE")
        known = set(s.records)
        revisions = {(u, s.h.view(k).rev(u)) for k in range(s.n + 1) for u in s.h.view(k).structure.units}
        obligations = {o.id for o in Workflow(support).obligations} if request["claims"] else set()
        reasons.update("REF_OBLIGATION" for c in request["claims"] if c not in obligations)
        submitted: set[str] = set()
        for record in request["records"]:
            rid = record.get("id") if isinstance(record, Mapping) else None
            own = record_problems(record, record_violations)
            if not own:
                if rid in known or rid in submitted:
                    own.append("REF_DUPLICATE")
                if referenced_records(record) - known - submitted:
                    own.append("REF_RECORD")
                if not request["candidates"] and referenced_revisions(record) - revisions:
                    own.append("REF_REVISION")
                if self._second_context(record, s):
                    own.append("REF_PRODUCING_CONTEXT")
            if own:
                refused.append((rid if isinstance(rid, str) else "sha256:" + "0" * 64, tuple(sorted(set(own)))))
            if isinstance(rid, str):
                submitted.add(rid)
        if not reasons and not refused:
            reasons.add("SCHEMA_UNSUPPORTED")  # steps 3-8 are not realized yet: fail closed (§8.3 step 1)
        return reasons, refused

    @staticmethod
    def _second_context(record: Mapping[str, Any], s) -> bool:
        """A second producing context for one transformation: a result under another write scope or work key
        (§7.1; the S2 binding cases)."""

        if record.get("kind") != "TASK_RESULT":
            return False
        x = (record.get("target") or {}).get("transformation")
        if not x:
            return False
        mine = (tuple(sorted((record.get("binding") or {}).get("write_scope") or ())), (record.get("binding") or {}).get("item_key"))
        for rid in s.of_kind("TASK_RESULT"):
            other = s.record(rid)
            if other["target"].get("transformation") == x:
                binding = other.get("binding") or {}
                if (tuple(sorted(binding.get("write_scope") or ())), binding.get("item_key")) != mine:
                    return True
        return False


__all__ = ["Admission", "AdmissionHalted", "Decision", "UNREALIZED_STEPS"]
