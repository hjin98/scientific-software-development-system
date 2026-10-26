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
from dataclasses import dataclass, field, replace
from typing import Any

from ssds.core.api.v1 import canonical_json
from ssds.derivation import (Frame, Support, Transformation, TreeSource, Workflow, adoption_codes, adoption_frame,
                             derive, frame_state, outside_scope, protected_touched, transformation_of, trial,
                             trust_roots)
from ssds.ledger.append import append_entry, write_checkpoint
from ssds.ledger.qualification import FileWitness
from ssds.ledger.read import (LedgerEntry, entry_violations, read_chain, record_id, record_violations, submits,
                              verify_sshsig, with_id)

from .authenticate import authenticate, stored_attestations
from .authorize import authorize
from .checks import (content_identity, over_bounds, producing_context, record_problems, referenced_objects,
                     referenced_records, referenced_revisions, request_problems, transformation_named, verified_objects)
from .genesis import AdmissionHome, host_key
from .lifecycle import lifecycle_message, lifecycle_problems
from .request import REPORT_KINDS, never_lost, request_id

#: The validation steps after step 2 that are not realized yet (Phase F steps 3-5).
UNREALIZED_STEPS = ("authorization", "structure", "currency", "legality", "regression")


def salvageable(record: Mapping[str, Any]) -> bool:
    """A never-lost record is salvaged only when every check it owes is built (Phase F plan §3.1): a report, whose
    supersession step 3 now authorizes. Every other never-lost record (an adverse judgment, a failing assessment,
    a challenge-tier record) still owes checks of steps 4-5 not built yet, so it is refused by identity as
    unsupported (plan review b10018de B1: a salvaged peer judgment ended another's standing one)."""

    return record.get("kind") in REPORT_KINDS  # a report's supersession is authorized at step 3 (step 4b-i)


def blocking(refused: Iterable[tuple[str, tuple[str, ...]]], alone: Iterable[tuple[str, tuple[str, ...]]]) -> list:
    """The refusals that reject their request: all but those refused alone (an ineligible adjudication), which
    leave the decision to the rest of it (catalogue §8.3 step 3; review 8d274c4 B3). The one rule both the
    fail-closed check and the decision read."""

    alone = set(alone)
    return [r for r in refused if r not in alone]


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

        reasons, refused, passing, auth, alone, salvage = self.validate(request, chain, entries)
        decision = "REJECT" if reasons or blocking(refused, alone) else "ACCEPT"
        if decision == "ACCEPT":
            admitted = passing
        elif auth is not None and auth.ok:  # never-lost salvage after the binding authenticated (§8.3 step 6)
            if salvage is not None:  # judged at the head, where the rejecting entry admits them (F27)
                kept, out = salvage
                read = {r["id"] for r in kept} | {rid for rid, _ in out}
                refused = [(rid, why) for rid, why in refused if rid not in read] + list(out)
                passing = [r for r in passing if not never_lost(r)] + list(kept)
            admitted = [r for r in passing if never_lost(r) and salvageable(r)]
            refused += [(r["id"], ("SCHEMA_UNSUPPORTED",)) for r in passing if never_lost(r) and not salvageable(r)]
            state = derive(chain, self.trees).s
            known, fixed_before = set(state.records), set(state.submissions)
            while True:  # a salvaged record names only records that exist: admitted before, or admitted with it
                ids = {r["id"] for r in admitted}
                dangling = [r for r in admitted if referenced_records(r) - known - ids]
                # and only transformations a result fixes there: a co-submitted result refused fixes nothing
                # (review 23b487a B1)
                fixed = fixed_before | {r["target"]["transformation"] for r in admitted
                                        if r["kind"] == "TASK_RESULT" and submits(r["target"])}
                unfixed = [r for r in admitted if r not in dangling
                           and transformation_named(r) is not None and transformation_named(r) not in fixed]
                if not dangling and not unfixed:
                    break
                admitted = [r for r in admitted if r not in dangling and r not in unfixed]
                refused += [(r["id"], ("REF_RECORD",)) for r in dangling]
                refused += [(r["id"], ("REF_TRANSFORMATION",)) for r in unfixed]
        else:
            admitted = []
        good = verified_objects(request.get("objects") if isinstance(request, Mapping) else None)[0]
        objects = {d: good[d] for r in admitted for d in referenced_objects(r) if d in good}
        if admitted and auth is not None:
            objects.update(auth.objects)  # the binding, so derivation reads it from the ledger alone (§12.2)
        if auth is not None and auth.reissue is not None:
            # a never-lost record under an unlisted retired envelope: refused by identity, its bytes and its binding
            # retained by content identity with the refusal, inert (S0 never reads them; §8.3 step 3)
            for record in passing:
                if never_lost(record):
                    body = {k: v for k, v in record.items() if k != "id"}
                    objects[record["id"]] = canonical_json(body)
                    refused.append((record["id"], ("AUTH_ENVELOPE",)))
            objects.update(auth.objects)
        head = entries[-1]
        entry = self.admission_entry(head, obs, rid, decision, reasons, admitted, refused, expected)
        problems = entry_violations(entry) + [p for r in admitted for p in record_violations(r)]
        if problems:  # nothing that would break the chain is ever appended
            raise EntryInvalid(f"the entry for {rid} would not verify: {problems}")
        appended = append_entry(self.repository, entry, self.key, head.commit, objects=objects)
        write_checkpoint(FileWitness(self.home.witness_root), appended.checkpoint)
        return Decision(rid, decision, tuple(sorted(reasons)), tuple(r["id"] for r in admitted), tuple(refused),
                        appended.position, appended=True)

    def lifecycle_message(self, record: Mapping[str, Any]) -> bytes:
        """The bytes the human gate signs to admit ``record`` as this ledger's next entry (§25.2)."""

        chain = self.chain()
        head = chain.entries[chain.readable_through]
        return lifecycle_message(self.ledger_id, head.entry["position"] + 1, head.digest, record)

    def admission_entry(self, head: LedgerEntry, obs: str, rid: str, decision: str, reasons: Iterable[str],
                        admitted: list[dict], refused: Iterable[tuple[str, tuple[str, ...]]], expected: str) -> dict:
        """The ``ADMISSION`` entry that records a decision after ``head``: what is appended, and what a trial
        extension derives over (reading F10)."""

        return {"ledger_id": self.ledger_id, "position": head.entry["position"] + 1, "schema": 1, "prev": head.digest,
                "entry_kind": "ADMISSION", "host_key_id": self.key.key_id, "incarnation_id": self.incarnation_id,
                "obs": obs, "absorption": None, "lifecycle": None, "records": list(admitted),
                "admission": {"request_id": rid, "decision": decision, "reasons": sorted(reasons),
                              "base_commit": expected, "admitted_commit": expected, "adopted_deltas": [],
                              "integrates": None,
                              "refused": [{"record_id": r, "reasons": list(why)} for r, why in refused]}}

    def trial(self, chain, entry: Mapping[str, Any], objects: Mapping[str, bytes] | None = None, frame=None):
        """The derived state as if ``entry`` were appended to ``chain`` (reading F10), after ``frame``'s
        transformation when given (reading F27); nothing is written."""

        return trial(chain, self.trees, entry, objects, frame)

    def admit_lifecycle(self, record: Mapping[str, Any], signature: str, obs: str) -> int:
        """Admit a human-gated ``KEY_LIFECYCLE`` record (§25.2): its actor is a registered human whose signature over
        the record, for this ledger at this position after this head, verifies; its key object is well formed for
        its action (:mod:`.lifecycle`). The approval is kept in the record's provenance. Returns the position."""

        chain = self.chain()
        entries = chain.entries[: chain.readable_through + 1]
        expected = self.expected_head(entries)
        if obs != expected:
            raise AdmissionHalted(f"the observed head {obs} is not the expected head {expected}")
        roots = trust_roots(entries)
        head = entries[-1]
        position = head.entry["position"] + 1
        try:
            message = lifecycle_message(self.ledger_id, position, head.digest, record)
        except (ValueError, TypeError, AttributeError):
            raise EntryInvalid("a lifecycle record is a JSON object canonical JSON encodes") from None
        actor = record.get("actor")
        if record.get("kind") != "KEY_LIFECYCLE" or record.get("actor_class") != "HUMAN" or not isinstance(actor, str) \
                or actor not in roots.humans or not isinstance(signature, str) \
                or not verify_sshsig(roots.humans[actor], message, signature):
            raise EntryInvalid("a lifecycle record needs its named human's verifying approval for this ledger, position "
                               "and head")
        problems = record_violations(record) + lifecycle_problems(record.get("fields"), roots, position)
        identity = record_id({**record, "provenance": None})
        if any(e.lifecycle is not None and record_id({**e.lifecycle, "provenance": None}) == identity for e in entries):
            problems.append("this lifecycle record is already admitted")  # Review e6ac009 B5
        if problems:
            raise EntryInvalid(f"the lifecycle record cannot be admitted: {problems}")
        signed = with_id({**record, "provenance": {"approval": {"actor": actor, "signature": signature}}})
        entry = {"ledger_id": self.ledger_id, "position": position, "schema": 1, "prev": head.digest,
                 "entry_kind": "LIFECYCLE", "host_key_id": self.key.key_id, "incarnation_id": self.incarnation_id,
                 "obs": obs, "admission": None, "absorption": None, "lifecycle": signed, "records": []}
        problems = entry_violations(entry) + record_violations(signed)
        if problems:
            raise EntryInvalid(f"the lifecycle entry would not verify: {problems}")
        appended = append_entry(self.repository, entry, self.key, head.commit)
        write_checkpoint(FileWitness(self.home.witness_root), appended.checkpoint)
        return appended.position

    def validate(self, request: Any, chain, entries):
        """Steps 1-3: the request-level reasons, the refused records with theirs, the records that passed their own
        checks, in order, the authentication, the refusals that leave the decision to the rest of the request
        (an ineligible adjudication), and, when the records were judged after the request's own transformation, the
        never-lost records' reading at the head instead: what passes and what is refused there, which a rejection
        salvages from (``None`` otherwise). Every record is checked whatever the request's own faults."""

        reasons = set(request_problems(request))
        if over_bounds(request):
            return reasons | {"SCHEMA_BOUND"}, [], [], None, [], None  # no per-record work beyond the bounds (§25.4)
        records = request.get("records") if isinstance(request, Mapping) else None
        records = records if isinstance(records, list) else []
        refused: list[tuple[str, tuple[str, ...]]] = []
        alone: list[tuple[str, tuple[str, ...]]] = []  # refused alone: the decision rests on the rest
        passing: list[dict] = []
        salvage = None
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
            fixed = self._fixed_transformations(s, records)
            for record in records:
                own = record_problems(record, record_violations)
                if not own:
                    rid = record["id"]
                    if rid in known or any(p["id"] == rid for p in passing):
                        own.append("REF_DUPLICATE")
                    if referenced_records(record) - known - {p["id"] for p in passing}:
                        own.append("REF_RECORD")
                    named = transformation_named(record)
                    target = record["target"] if isinstance(record["target"], Mapping) else {}
                    if named is not None and named not in fixed or record["kind"] == "TASK_RESULT" and \
                            ("base" in target or "candidate" in target) and not submits(target) or \
                            named is not None and record["frame"] == "ADMITTED" or \
                            isinstance(record["frame"], Mapping) and set(record["frame"]) != {"transformation"}:
                        # §7.5: a record about a transformation declares its frame (review 23b487a N2); a rebase
                        # frame is step 5's (§6; review 193b654 B3)
                        own.append("REF_TRANSFORMATION")  # names no transformation a result fixes (4c-iii)
                    elif record["kind"] == "TASK_RESULT" and (record["target"].get("adopts") or []):
                        own.append("SCHEMA_UNSUPPORTED")  # adoption with a candidate stays unsupported (revision 15)
                    elif record["kind"] == "INTAKE_CLASSIFICATION" or record["kind"] == "INTAKE_DISPOSITION" and (
                            record["outcome"] != "ABSORB" or "delta" not in target_type(record)):
                        own.append("SCHEMA_UNSUPPORTED")  # intake beyond SD-69's adoption is Phase G's (§1)
                    elif record["kind"] == "INTAKE_DISPOSITION" and not adoptable(support, record):
                        own.append("REF_DELTA")  # not the key's current delta, or an adverse one stands (F21)
                    elif referenced_revisions(record) - revisions - (fixed[named] if named is not None else set()):
                        own.append("REF_REVISION")  # a frame record's revisions may also be its frame's
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
            stored = {d: o for e in entries for d, o in e.objects.items()}
            bindings = {f.record["binding"]["envelope"] for f in s.records.values()
                        if isinstance(f.record.get("binding"), Mapping) and f.record["binding"].get("envelope")}
            auth = authenticate(request, passing, trust_roots(entries), s.n, stored_attestations(stored, bindings))
            reasons |= auth.reasons
            covered = {rid for rid, _ in auth.refused}
            refused += list(auth.refused)
            passing = [r for r in passing if r["id"] not in covered]
        if auth is not None and (auth.ok or auth.reissue):  # step 3's authorization (steps 4b-i, 4b-ii)
            withheld = None
            adopting = bool(request.get("adopted_deltas")) or any(_absorbs(r) for r in passing)
            if adopting and request.get("candidates") or len(request.get("candidates") or []) > 1:
                reasons.add("SCHEMA_UNSUPPORTED")  # adoption with a candidate; one integration per request
                withheld = "SCHEMA_UNSUPPORTED"
            else:
                change = None  # the frame of the request's own transformation, when it exists (reading F27)
                if request.get("candidates"):  # an integrating request (§11.5): steps 3-4 on its frame (4c-iii)
                    reasons |= integration_codes(request["candidates"][0], support, request.get("binding"))
                    change = integration_frame(request["candidates"][0], support)
                elif adopting:
                    change = adoption_frame(support.s, self.expected_head(entries), request.get("adopted_deltas"))
                change = change if isinstance(change, Frame) and change.exists else None
                position = request.get("base_position")
                base = Workflow.historical(support.s.h, position) if "REF_BASE" not in reasons \
                    and isinstance(position, int) and 0 <= position <= s.n else None
                before = passing
                passing, more, ok, alone, last = self.authorized(request, passing, chain, entries, base, auth, change)
                refused += more + alone
                if change is not None:
                    # a rejection admits never-lost records at the head (§8.3 step 6), so their own step-3 and step-5
                    # checks are read there, not after a transformation the rejection never applies (F27)
                    kept, out, _, out_alone, _ = self.authorized(request, [r for r in before if never_lost(r)], chain,
                                                                 entries, base, auth)
                    salvage = (kept, out + out_alone)
                if last is not None and last.grows_a_cycle(support):
                    reasons.add("CYCLE_SUPPORT")  # step 5: the static support graph gains or grows a cycle (F24)
                if not ok:
                    reasons.add("AUTH_ENVELOPE")
                    withheld = "REF_BASE" if base is None else "AUTH_ENVELOPE"
                if adopting:  # a records-only adoption (4c-iv; SD-69), judged on what passed step 3 (review 193b654)
                    named = {(r["target"]["absorption"], tuple(r["target"]["key"])) for r in passing if _absorbs(r)}
                    reasons |= adoption_codes(support.s, self.expected_head(entries), request.get("adopted_deltas"),
                                              named, support)
            if withheld is not None:  # no record passes step 3: each never-lost one is recorded as refused (step 6)
                refused += [(r["id"], (withheld,)) for r in passing if never_lost(r)]
                passing = [r for r in passing if not never_lost(r)]
                auth = replace(auth, ok=False)
                salvage = None
        if not reasons and not blocking(refused, alone):
            reasons.add("SCHEMA_UNSUPPORTED")  # steps 4-8 are not realized yet: fail closed (§8.3 step 1)
        return reasons, refused, passing, auth, alone, salvage

    def _fixed_transformations(self, s: Any, records: list) -> dict[str, set[tuple[str, str]]]:
        """Each transformation this request's records name that an admitted or co-submitted result fixes (§7.1),
        with the revisions its frame at the head holds (``B``, ``C`` and ``M_n(X)``, each under the frame's
        structure). A result fixes ``X`` only when it submits it: ``id(X)`` is §7.1's identity of what it names,
        ``B`` an admitted head and ``C`` readable."""

        heads = {s.h.head(k) for k in range(s.n + 1)}
        found: dict[str, Any] = {}
        for rid in s.of_kind("TASK_RESULT"):
            target = s.record(rid)["target"]
            if submits(target):
                found.setdefault(target["transformation"], target)
        for record in records:
            if isinstance(record, Mapping) and record.get("kind") == "TASK_RESULT" and submits(record.get("target")):
                found.setdefault(record["target"]["transformation"], record["target"])
        named = {transformation_named(r) for r in records if isinstance(r, Mapping)} - {None}
        out: dict[str, set[tuple[str, str]]] = {}
        for x, target in found.items():
            if x not in named:
                continue  # only the transformations this request names are judged: frames built lazily (review 23b487a)
            if target["base"] not in heads:
                continue
            try:
                self.trees(target["candidate"])
            except Exception:  # an unreadable candidate fixes nothing
                continue
            adopts = tuple((tuple(a["key"]), a["value"]) for a in target.get("adopts") or [])
            frame = Frame(s.h, s.n, Transformation(x, target["base"], target["candidate"], adopts), None)
            views = [frame.base_view, frame.candidate_view] + ([frame.view] if frame.merged is not None else [])
            out[x] = {(u, v.rev(u)) for v in views for u in v.structure.units}
        return out

    def authorized(self, request: Mapping[str, Any], passing: list[dict], chain, entries, base, auth, change=None):
        """Authorize the records in the trial extension of their own request (reading F10), in the state after the
        request's own transformation when ``change`` is its frame (reading F27), removing each refused
        record and rebuilding the trial until none is refused (at most once per record). Returns the records
        still passing, the refusals, whether the envelope's obligation and role hold, the records refused alone, and
        the final trial, which step 5's request-level check reads (``None`` when no record passes)."""

        refused: list[tuple[str, tuple[str, ...]]] = []
        alone: list[tuple[str, tuple[str, ...]]] = []
        head = entries[-1]
        expected = self.expected_head(entries)
        good = verified_objects(request.get("objects"))[0]
        last = None
        while passing:
            entry = self.admission_entry(head, expected, request_id(request), "ACCEPT", (), passing, (), expected)
            objects = {d: good[d] for r in passing for d in referenced_objects(r) if d in good} | auth.objects
            last = self.trial(chain, entry, objects, change)
            result = authorize(request, passing, last, base)
            if not result.ok:
                return passing, refused, False, alone, last
            if not result.refused and not result.alone:
                break
            gone = {rid for rid, _ in result.refused + result.alone}
            refused += list(result.refused)
            alone += list(result.alone)
            passing = [r for r in passing if r["id"] not in gone]
            last = None
        return passing, refused, True, alone, last


def _absorbs(record: Mapping[str, Any]) -> bool:
    """An ``ABSORB`` disposition of a quarantined delta: an adoption (§18.4)."""

    return record.get("kind") == "INTAKE_DISPOSITION" and record.get("outcome") == "ABSORB" \
        and "delta" in target_type(record)


def target_type(record: Mapping[str, Any]) -> set[str]:
    """The target shape a record uses: ``delta`` or ``content_ref`` for an intake record."""

    target = record.get("target")
    if isinstance(target, Mapping) and {"absorption", "key"} <= set(target):
        return {"delta"}
    return {"content_ref"} if isinstance(target, Mapping) and "digest" in target else set()


def adoptable(support: Any, record: Mapping[str, Any]) -> bool:
    """An adopting ``ABSORB`` names its key's current delta at the head (reading F21; revision 15), on which no
    adverse disposition stands (§18.4)."""

    s = support.s
    target = record["target"]
    current = s.current_delta(tuple(target["key"]))
    if current is None or current[0] != target["absorption"]:
        return False
    return not any(s.record(r)["target"] == target and s.record(r)["outcome"] != "ABSORB" and support.j.stands(r)
                   for r in s.of_kind("INTAKE_DISPOSITION"))


def integration_frame(candidate: str, support: Any) -> Any:
    """The frame of the transformation an admitted result submits with candidate ``C``, built at the head, or the
    code refusing it: none or more than one such ``X``, an enactment already integrated, or a merge conflict."""

    s = support.s
    found = sorted(x for x in s.submissions
                   if (t := transformation_of(s, x)) is not None and t.candidate == candidate)
    if len(found) != 1:
        return "REF_TRANSFORMATION"  # none, or more than one (a rebase frame is unsupported, Q-F6 (iii))
    x = found[0]
    if s.enactment(x) in s.integrated:
        return "SCHEMA_UNSUPPORTED"  # one enactment, one integration is step 7's (step 5)
    frame = Frame(s.h, s.n, transformation_of(s, x), s.enactment(x))
    if frame.merged is None:
        return "STRUCT_MERGE_CONFLICT"  # no frame, so nothing integrates (§7.4)
    return frame


def integration_codes(candidate: str, support: Any, binding: Any) -> set[str]:
    """Steps 3-4 of an integrating request for ``C`` (Phase F 4c-iii), on the frame of the transformation an
    admitted result submits with that candidate, bound to that result's producing task (else fail closed): its
    write set within the bound contract's write scope and clear of plan units and unnamed verification rules
    (``AUTH_WRITE_SCOPE``); no protected surface touched when an agent made the candidate (``AUTH_PROTECTED``); §8.3 step 4's structure on the merged tree; and
    §7.6's enactment condition for every promotion or restoration (``ENACTMENT_MISSING``); and step 5's static
    support graph read in the frame, where changed structure re-routes it (``CYCLE_SUPPORT``, reading F24)."""

    s = support.s
    frame = integration_frame(candidate, support)
    if isinstance(frame, str):
        return {frame}
    x = frame.x.id
    workflow = Workflow(support)
    result = s.record(workflow.submitting_result(x))
    envelope = binding.get("envelope") if isinstance(binding, Mapping) else None
    human = binding.get("human") if isinstance(binding, Mapping) else None
    producing = (isinstance(envelope, Mapping) and envelope.get("task_id") == s.enactment(x)) or (
        isinstance(human, Mapping) and human.get("actor") == result["actor"])
    if not producing:
        # §11.5 (3): the integration request is bound to the producing task; any other binding fails closed
        # until steps 7-8 own the claimed obligation (review 23b487a B2)
        return {"SCHEMA_UNSUPPORTED"}
    codes = {f.code for f in frame.structural.findings}
    contract = workflow.conformance(workflow.submitting_result(x)).contract[0]
    if contract is None or outside_scope(frame, contract.write_scope):
        codes.add("AUTH_WRITE_SCOPE")
    else:
        kinds = {u: frame.structure.kind(u) if u in frame.structure.units else frame.head_view.structure.kind(u)
                 for u in frame.write_set}
        if any(k == "PLAN" for k in kinds.values()) or any(
                k == "EVIDENCE_SPEC" and u not in contract.evidence_specs for u, k in kinds.items()):
            codes.add("AUTH_WRITE_SCOPE")  # plan units and unnamed verification rules (§12.3)
    agent_made = result["actor_class"] == "AGENT" or any(
        str(a).startswith("agent:") for a in (result.get("binding") or {}).get("lineage") or [])
    if agent_made and protected_touched(frame, s.policy, s.h.policy_path):
        codes.add("AUTH_PROTECTED")  # agents cannot modify a protected surface, however it is integrated (§25.3)
    if any(not support.prospectively_accepted(x, uid) for uid in frame.structural.tenure_starts):
        codes.add("ENACTMENT_MISSING")
    framed = frame_state(s.h, s.n, x, s)
    if framed is not None and Support(framed).grows_a_cycle(support):
        codes.add("CYCLE_SUPPORT")  # step 5 read in the frame, where its changes re-route validity (F24)
    return codes

__all__ = ["Admission", "AdmissionHalted", "Decision", "EntryInvalid", "UNREALIZED_STEPS", "integration_codes",
           "integration_frame"]
