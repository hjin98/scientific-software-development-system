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
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any

from ssds.derivation import TreeSource, Workflow, derive, trust_roots
from ssds.ledger.append import append_entry, write_checkpoint
from ssds.ledger.qualification import FileWitness
from ssds.ledger.read import LedgerEntry, entry_violations, read_chain, record_violations

from .authenticate import authenticate
from .checks import (content_identity, over_bounds, producing_context, record_problems, referenced_objects,
                     referenced_records, referenced_revisions, request_problems, verified_objects)
from .genesis import AdmissionHome, host_key
from .request import never_lost, request_id

#: The validation steps after step 2 that are not realized yet (Phase F steps 3-5).
UNREALIZED_STEPS = ("authorization", "structure", "dependency", "currency", "legality", "regression")


class AdmissionHalted(RuntimeError):
    """Admission does not append: the observed head is not the expected head (absorption is step 6's)."""


class EntryInvalid(RuntimeError):
    """Admission does not append an entry that would not verify; the request is set aside, not requeued."""


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
        """Decide every queued request in order; each leaves the queue as it is taken, so one request's fault
        never blocks the next (§8.2: FIFO bounds starvation)."""

        decisions = []
        for request in self.order():
            self.queue.remove(request)
            try:
                decisions.append(self.admit(request, obs))
            except AdmissionHalted:
                self.queue.insert(0, request)  # nothing was appended: it is revalidated at the next head (§8.3 step 9)
                raise
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

    def admit(self, request: Any, obs: str) -> Decision:
        chain = self.chain()
        entries = chain.entries[: chain.readable_through + 1]
        rid = request_id(request)
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

        reasons, refused, passing, auth = self.validate(request, chain, entries)
        decision = "REJECT" if reasons or refused else "ACCEPT"
        if decision == "ACCEPT":
            admitted = passing
        elif auth is not None and auth.ok:  # never-lost salvage after the binding authenticated (§8.3 step 6)
            admitted = [r for r in passing if never_lost(r)]
            known = set(derive(chain, self.trees).s.records)
            while True:  # a salvaged record names only records that exist: admitted before, or admitted with it
                ids = {r["id"] for r in admitted}
                dangling = [r for r in admitted if referenced_records(r) - known - ids]
                if not dangling:
                    break
                admitted = [r for r in admitted if r not in dangling]
                refused += [(r["id"], ("REF_RECORD",)) for r in dangling]
        else:
            admitted = []
        good = verified_objects(request.get("objects") if isinstance(request, Mapping) else None)[0]
        objects = {d: good[d] for r in admitted for d in referenced_objects(r) if d in good}
        if admitted and auth is not None:
            objects.update(auth.objects)  # the binding, so derivation reads it from the ledger alone (§12.2)
        head = entries[-1]
        entry = {"ledger_id": self.ledger_id, "position": head.entry["position"] + 1, "schema": 1, "prev": head.digest,
                 "entry_kind": "ADMISSION", "host_key_id": self.key.key_id, "incarnation_id": self.incarnation_id,
                 "obs": obs, "absorption": None, "lifecycle": None, "records": admitted,
                 "admission": {"request_id": rid, "decision": decision, "reasons": sorted(reasons),
                               "base_commit": expected, "admitted_commit": expected, "adopted_deltas": [],
                               "integrates": None,
                               "refused": [{"record_id": r, "reasons": list(why)} for r, why in refused]}}
        problems = entry_violations(entry) + [p for r in admitted for p in record_violations(r)]
        if problems:  # nothing that would break the chain is ever appended
            raise EntryInvalid(f"the entry for {rid} would not verify: {problems}")
        appended = append_entry(self.repository, entry, self.key, head.commit, objects=objects)
        write_checkpoint(FileWitness(self.home.witness_root), appended.checkpoint)
        return Decision(rid, decision, tuple(sorted(reasons)), tuple(r["id"] for r in admitted), tuple(refused),
                        appended.position, appended=True)

    def admit_lifecycle(self, record: Mapping[str, Any], signature: str, obs: str) -> int:
        """Admit a human-gated ``KEY_LIFECYCLE`` record (§25.2): its actor is a registered human whose signature over
        the record verifies; the approval is kept in the record's provenance. Returns the entry's position."""

        from ssds.ledger.read import verify_sshsig, with_id

        chain = self.chain()
        entries = chain.entries[: chain.readable_through + 1]
        expected = self.expected_head(entries)
        if obs != expected:
            raise AdmissionHalted(f"the observed head {obs} is not the expected head {expected}")
        roots = trust_roots(entries)
        actor = record.get("actor")
        if record.get("kind") != "KEY_LIFECYCLE" or record.get("actor_class") != "HUMAN" or actor not in roots.humans \
                or not verify_sshsig(roots.humans[actor], lifecycle_message(record), signature):
            raise EntryInvalid("a lifecycle record needs a registered human's verifying approval")
        signed = with_id({**record, "provenance": {"approval": {"actor": actor, "signature": signature}}})
        head = entries[-1]
        entry = {"ledger_id": self.ledger_id, "position": head.entry["position"] + 1, "schema": 1, "prev": head.digest,
                 "entry_kind": "LIFECYCLE", "host_key_id": self.key.key_id, "incarnation_id": self.incarnation_id,
                 "obs": obs, "admission": None, "absorption": None, "lifecycle": signed, "records": []}
        problems = entry_violations(entry) + record_violations(signed)
        if problems:
            raise EntryInvalid(f"the lifecycle entry would not verify: {problems}")
        appended = append_entry(self.repository, entry, self.key, head.commit)
        write_checkpoint(FileWitness(self.home.witness_root), appended.checkpoint)
        return appended.position

    def validate(self, request: Any, chain, entries):
        """Steps 1 and 2: the request-level reasons, the refused records with theirs, and the records that passed
        their own checks, in order. Every record is checked whatever the request's own faults."""

        reasons = set(request_problems(request))
        if over_bounds(request):
            return reasons | {"SCHEMA_BOUND"}, [], [], None  # no per-record work beyond the bounds (§25.4)
        records = request.get("records") if isinstance(request, Mapping) else None
        records = records if isinstance(records, list) else []
        refused: list[tuple[str, tuple[str, ...]]] = []
        passing: list[dict] = []
        support = derive(chain, self.trees) if records or not reasons else None
        s = support.s if support is not None else None
        if s is not None:
            known = set(s.records)
            revisions = {(u, s.h.view(k).rev(u)) for k in range(s.n + 1) for u in s.h.view(k).structure.units}
            stored = {d for e in entries for d in e.objects}
            good = verified_objects(request.get("objects") if isinstance(request, Mapping) else None)[0]
            admitted_contexts = {}
            for rid_ in s.of_kind("TASK_RESULT"):
                context = producing_context(s.record(rid_))
                if context is not None:
                    admitted_contexts.setdefault(context[0], set()).add(context[1:])
            candidates = isinstance(request, Mapping) and bool(request.get("candidates"))
            for record in records:
                own = record_problems(record, record_violations)
                if not own:
                    rid = record["id"]
                    if rid in known or any(p["id"] == rid for p in passing):
                        own.append("REF_DUPLICATE")
                    if referenced_records(record) - known - {p["id"] for p in passing}:
                        own.append("REF_RECORD")
                    if not candidates and referenced_revisions(record) - revisions:
                        own.append("REF_REVISION")
                    if referenced_objects(record) - stored - set(good):
                        own.append("REF_OBJECT")
                    context = producing_context(record)
                    if context is not None:
                        earlier = admitted_contexts.get(context[0], set()) | {
                            producing_context(p)[1:] for p in passing if (producing_context(p) or (None,))[0] == context[0]}
                        if earlier - {context[1:]}:
                            own.append("REF_PRODUCING_CONTEXT")  # a second producing context for one transformation (§7.1)
                if own:
                    refused.append((content_identity(record), tuple(sorted(set(own)))))
                else:
                    passing.append(dict(record))
        if not reasons and s is not None:  # step 2 at the request level, after step 1 passed
            position = request["base_position"]
            if not 0 <= position <= s.n or request["base_commit"] != self.expected_head(entries[: position + 1]):
                reasons.add("REF_BASE")
            if request["claims"]:
                obligations = {o.id for o in Workflow(support).obligations}
                reasons.update("REF_OBLIGATION" for c in request["claims"] if c not in obligations)
        auth = None
        if isinstance(request, Mapping) and s is not None:  # step 3's authentication of the binding
            auth = authenticate(request, passing, trust_roots(entries), s.n)
            reasons |= auth.reasons
            covered = {rid for rid, _ in auth.refused}
            refused += list(auth.refused)
            passing = [r for r in passing if r["id"] not in covered]
        if not reasons and not refused:
            reasons.add("SCHEMA_UNSUPPORTED")  # steps 4-8 are not realized yet: fail closed (§8.3 step 1)
        return reasons, refused, passing, auth


def lifecycle_message(record: Mapping[str, Any]) -> bytes:
    """What the human gate signs for a lifecycle record: its identity without the provenance that carries the
    approval (Phase F reading F5)."""

    from ssds.ledger.read import record_id

    return b"ssds lifecycle " + record_id({**record, "provenance": None}).encode("ascii") + b"\n"


__all__ = ["Admission", "AdmissionHalted", "Decision", "EntryInvalid", "UNREALIZED_STEPS"]
