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
from pathlib import Path
from typing import Any

from ssds.core.api.v1 import canonical_json
from ssds.derivation import (Frame, Support, Transformation, TreeSource, Workflow, adoption_codes, adoption_frame,
                             derive, frame_state, outside_scope, passing, protected_touched, transformation_of, trial,
                             trust_roots)
from ssds.ledger.append import AppendFailed, AppendRefused, append_entry, import_commits, write_checkpoint
from ssds.ledger.qualification import (Checkpoint, FileWitness, HighWaterMark, Qualification, WitnessModel,
                                       checkpoint_body, checkpoint_message, qualify)
from ssds.ledger.read import (LedgerEntry, entry_violations, is_commit, read_chain, record_id, record_violations,
                              submits, verify_sshsig, with_id)

from .authenticate import authenticate, stored_attestations
from .authorize import authorize
from .checks import (content_identity, on_merits, over_bounds, producing_context, record_problems, referenced_objects,
                     referenced_records, referenced_revisions, request_problems, target_references, transformation_named,
                     verified_objects)
from .genesis import AdmissionHome, host_key
from .lifecycle import lifecycle_message, lifecycle_problems
from .currency import Currency
from .legality import Legality, conformance_alone
from .request import REPORT_KINDS, RUNNER_OBSERVATIONS, never_lost, request_id

#: How many times a writer that loses the ledger's compare-and-swap re-reads and revalidates before it halts.
_CAS_ATTEMPTS = 3

#: The validation steps after step 2 that are not realized yet (Phase F steps 3-5).
UNREALIZED_STEPS = ("regression",)  # step 8, deferred by SD-71 and SD-72


def salvageable(record: Mapping[str, Any]) -> bool:
    """A never-lost record is salvaged only when every check it owes is built (Phase F plan §3.1, step 5a): a
    report, a challenge or an adverse judgment, whose own step-3 and step-5 checks now exist (steps 4b-4d; step 6
    exempts them). A failing assessment and a runner's observation owe step 9's realization checks, so they are
    still refused by identity as unsupported (plan review b10018de B1)."""

    return record.get("kind") not in ("EVIDENCE_ASSESSMENT", *RUNNER_OBSERVATIONS)


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
    #: the observed product repository the composition root supplies, from which an absorption imports ``obs``
    #: (§8.6; plan step 6a); without one, a moved head halts Admission, as before
    product: Path | None = None

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
        """The integration head the last entry left, as ``History`` folds it: an accepted admission's admitted
        commit, an absorption's observed head (or its fence commit), else the genesis baseline (step 6a)."""

        expected = None
        for entry in entries:
            body = entry.entry
            if body["entry_kind"] == "ADMISSION" and body["admission"]["decision"] == "ACCEPT":
                expected = body["admission"]["admitted_commit"]
            elif body["entry_kind"] == "ABSORPTION":
                fence = body["absorption"]["fence"]
                expected = fence["fence_commit"] if fence else body["obs"]
            elif body["entry_kind"] == "LIFECYCLE" and body["lifecycle"]["kind"] == "GENESIS":
                expected = body["lifecycle"]["fields"]["baseline_commit"]
        return expected

    def absorb(self, entries: list[LedgerEntry], obs: str) -> None:
        """Append an absorption of the observed head ``obs`` (catalogue §8.6, §8.3 step 9), its commits imported so
        the entry keeps them reachable. Halts instead when there is no product repository to read, or when the
        head entry is an admission whose publication effect is pending: §22.3's procedure governs there, not a
        plain absorption (reading F39), and no integration is accepted in Phase F (SD-70, SD-71)."""

        head = entries[-1]
        body = head.entry
        if not is_commit(obs):  # validated before any Git call (Manual §25.4; review c06f5be N1)
            raise AdmissionHalted(f"the observed head {obs!r} is no commit identity")
        if self.product is None:
            raise AdmissionHalted(f"the observed head {obs} is not the expected head and no product repository is read")
        if body["entry_kind"] == "ADMISSION" and body["admission"]["decision"] == "ACCEPT" \
                and body["admission"]["admitted_commit"] != body["admission"]["base_commit"]:
            raise AdmissionHalted("the head admission's publication effect is pending (§22.3; reading F39)")
        try:
            import_commits(self.repository, self.product, [obs])
        except AppendFailed:
            raise AdmissionHalted(f"the observed head {obs} is not a commit of the product repository") from None
        entry = {"ledger_id": self.ledger_id, "position": body["position"] + 1, "schema": 1, "prev": head.digest,
                 "entry_kind": "ABSORPTION", "host_key_id": self.key.key_id, "incarnation_id": self.incarnation_id,
                 "obs": obs, "absorption": {"fence": None}, "admission": None, "lifecycle": None, "records": []}
        problems = entry_violations(entry)
        if problems:
            raise EntryInvalid(f"the absorption of {obs} would not verify: {problems}")
        self.commit(entry, head, referenced=[obs])  # an absorption is an entry: 6b's commit point (plan check N1)

    @staticmethod
    def recorded(entries: Iterable[LedgerEntry], rid: str) -> LedgerEntry | None:
        return next((e for e in entries if e.entry["entry_kind"] == "ADMISSION"
                     and e.entry["admission"]["request_id"] == rid), None)

    # -- the commit point (catalogue §21.3, §22.4, §23.3-§23.4; plan step 6b) -------------------------------------

    def witness_set(self, chain) -> tuple[WitnessModel, dict[str, FileWitness]]:
        """The genesis witness model and the witnesses this host can write: each ``FILE`` witness at its location.
        Any other kind is unreachable here and answers nothing (fixtures only, F3)."""

        model = WitnessModel.from_json(chain.entries[0].entry["lifecycle"]["fields"]["witnesses"])
        return model, {w.id: FileWitness(Path(w.location)) for w in model.witnesses if w.kind == "FILE"}

    def qualification(self, chain) -> Qualification:
        model, files = self.witness_set(chain)
        reports = {w.id: files[w.id].read(self.ledger_id) if w.id in files else None for w in model.witnesses}
        fields = chain.entries[0].entry["lifecycle"]["fields"]
        host_keys = {k["id"]: k["public_key"] for k in fields["trust_roots"]["admission_keys"]}
        return qualify(chain, reports, model, host_keys, self.home.high_water(self.ledger_id).get())

    def held_head(self):
        """The chain at a qualified head with no provisional entry: Admission appends nothing when the ledger is
        ``UNQUALIFIED``, ``ROLLBACK`` or ``FORK`` (§23.4). A provisional entry this host appended has its checkpoint
        distribution completed first, the crash recovery of §22.4 (its signature is deterministic, so the same
        checkpoint is rebuilt); a request it decided is then found by its identity."""

        chain = self.chain()
        held = self.qualification(chain)
        if held.current and held.provisional is not None:
            self.distribute(chain.entries[held.provisional], chain)
            held = self.qualification(chain)
        if not held.current or held.provisional is not None:
            raise AdmissionHalted(f"the ledger is {held.state} at {held.head}, provisional {held.provisional} (§23.4)")
        self.home.high_water(self.ledger_id).set(HighWaterMark(held.head, held.head_digest))
        return chain

    def distribute(self, appended: LedgerEntry, chain=None) -> None:
        """Write ``appended``'s checkpoint to every witness this host reaches; one that fails holds nothing."""

        body = checkpoint_body(self.ledger_id, appended.entry["position"], appended.digest, appended.commit,
                               appended.entry["host_key_id"])
        if body["host_key_id"] != self.key.key_id:
            raise AdmissionHalted("a provisional entry appended under another host key: its checkpoint is that key's (§22.4)")
        checkpoint = Checkpoint(**body, signature=self.key.sign(checkpoint_message(body)).hex())
        _, files = self.witness_set(chain if chain is not None else self.chain())
        for witness in files.values():
            try:
                write_checkpoint(witness, checkpoint)
            except (OSError, ValueError):
                continue  # the quorum decides below whether enough witnesses hold it

    def commit(self, entry: Mapping[str, Any], head: LedgerEntry, objects: Mapping[str, bytes] | None = None,
               referenced: Iterable[str] = ()) -> Any:
        """Append ``entry`` by the ledger's single-ref compare-and-swap (§21.3; a loss raises ``AppendRefused``),
        distribute its checkpoint, and report it only once a witness quorum holds it, raising the high-water mark
        (§22.4: "only then is the request reported admitted"). An entry not yet held stays provisional: Admission
        halts, and the next start completes its distribution before deciding anything."""

        appended = append_entry(self.repository, entry, self.key, head.commit, objects=objects,
                                referenced=list(referenced))
        chain = self.chain()
        self.distribute(chain.entries[appended.position], chain)
        held = self.qualification(chain)
        if not held.current or held.head != appended.position:
            raise AdmissionHalted(f"entry {appended.position} is appended but not yet held by a witness quorum (§22.4)")
        self.home.high_water(self.ledger_id).set(HighWaterMark(held.head, held.head_digest))
        return appended

    # -- one request --------------------------------------------------------------------------------------------

    def admit(self, request: Any, obs: str) -> Decision:
        """Decide ``request`` at the held head; a writer that loses the ledger's compare-and-swap re-reads and
        revalidates (§21.3; step 6b), a bounded number of times before it halts."""

        for _ in range(_CAS_ATTEMPTS):
            try:
                return self._admit_once(request, obs)
            except AppendRefused:
                continue
        raise AdmissionHalted("the ledger kept moving under this writer (§21.3)")

    def _admit_once(self, request: Any, obs: str) -> Decision:
        chain = self.held_head()
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
        if obs != expected:  # §8.3 step 9: first absorb obs, then revalidate at the new head (step 6a)
            self.absorb(entries, obs)
            chain = self.chain()
            entries = chain.entries[: chain.readable_through + 1]
            expected = self.expected_head(entries)

        reasons, refused, passing, auth, alone, salvage, integrating = self.validate(request, chain, entries)
        decision = "REJECT" if reasons or blocking(refused, alone) else "ACCEPT"
        if decision == "ACCEPT":
            # step 9 first drops what names a record or transformation a later step dropped: an ordinary refusal,
            # so the request is rejected and its never-lost records salvaged (reading F40; review 2981f738 N1)
            kept, drops = self.cascade(passing, chain)
            if drops:
                refused += drops
                passing = kept
                decision = "REJECT"
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
            admitted, drops = self.cascade(admitted, chain)
            refused += drops
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
        refused_x = integrating if decision == "REJECT" and auth is not None and auth.ok and on_merits(reasons) \
            else None  # a refusal of the candidate itself routes a new iteration (F35); nothing else does
        entry = self.admission_entry(head, obs, rid, decision, reasons, admitted, refused, expected, refused_x)
        if decision == "ACCEPT" and request.get("adopted_deltas"):
            # the committed entry is the trial's: a records-only adoption carries its frame's deltas and never
            # integrates (6c; reading F27; plan check of 97d9824 N2)
            frame = adoption_frame(derive(chain, self.trees).s, expected, request["adopted_deltas"])
            entry["admission"]["adopted_deltas"] = frame.entry_deltas()
        problems = entry_violations(entry) + [p for r in admitted for p in record_violations(r)]
        if problems:  # nothing that would break the chain is ever appended
            raise EntryInvalid(f"the entry for {rid} would not verify: {problems}")
        appended = self.commit(entry, head, objects=objects)
        return Decision(rid, decision, tuple(sorted(reasons)), tuple(r["id"] for r in admitted), tuple(refused),
                        appended.position, appended=True)

    def lifecycle_message(self, record: Mapping[str, Any]) -> bytes:
        """The bytes the human gate signs to admit ``record`` as this ledger's next entry (§25.2)."""

        chain = self.chain()
        head = chain.entries[chain.readable_through]
        return lifecycle_message(self.ledger_id, head.entry["position"] + 1, head.digest, record)

    def admission_entry(self, head: LedgerEntry, obs: str, rid: str, decision: str, reasons: Iterable[str],
                        admitted: list[dict], refused: Iterable[tuple[str, tuple[str, ...]]], expected: str,
                        integrates: str | None = None) -> dict:
        """The ``ADMISSION`` entry that records a decision after ``head``: what is appended, and what a trial
        extension derives over (reading F10)."""

        return {"ledger_id": self.ledger_id, "position": head.entry["position"] + 1, "schema": 1, "prev": head.digest,
                "entry_kind": "ADMISSION", "host_key_id": self.key.key_id, "incarnation_id": self.incarnation_id,
                "obs": obs, "absorption": None, "lifecycle": None, "records": list(admitted),
                "admission": {"request_id": rid, "decision": decision, "reasons": sorted(reasons),
                              "base_commit": expected, "admitted_commit": expected, "adopted_deltas": [],
                              "integrates": integrates,
                              "refused": [{"record_id": r, "reasons": list(why)} for r, why in refused]}}

    def trial(self, chain, entry: Mapping[str, Any], objects: Mapping[str, bytes] | None = None, frame=None):
        """The derived state as if ``entry`` were appended to ``chain`` (reading F10), after ``frame``'s
        transformation when given (reading F27); nothing is written."""

        return trial(chain, self.trees, entry, objects, frame)

    def admit_lifecycle(self, record: Mapping[str, Any], signature: str, obs: str) -> int:
        """Admit a human-gated ``KEY_LIFECYCLE`` record (§25.2): its actor is a registered human whose signature over
        the record, for this ledger at this position after this head, verifies; its key object is well formed for
        its action (:mod:`.lifecycle`). The approval is kept in the record's provenance. Returns the position."""

        chain = self.held_head()
        entries = chain.entries[: chain.readable_through + 1]
        expected = self.expected_head(entries)
        if obs != expected:
            # not absorbed here: the human approval names the ledger head it was signed after, which an absorption
            # would move; the lifecycle waits until an admission has absorbed obs (review c06f5be N2)
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
        return self.commit(entry, head).position

    def validate(self, request: Any, chain, entries):
        """Steps 1-3: the request-level reasons, the refused records with theirs, the records that passed their own
        checks, in order, the authentication, the refusals that leave the decision to the rest of the request
        (an ineligible adjudication), and, when the records were judged after the request's own transformation, the
        never-lost records' reading at the head instead: what passes and what is refused there, which a rejection
        salvages from (``None`` otherwise), and the transformation an integrating request names. Every record is
        checked whatever the request's own faults."""

        reasons = set(request_problems(request))
        if over_bounds(request):
            return reasons | {"SCHEMA_BOUND"}, [], [], None, [], None, None  # no per-record work beyond the bounds
        records = request.get("records") if isinstance(request, Mapping) else None
        records = records if isinstance(records, list) else []
        refused: list[tuple[str, tuple[str, ...]]] = []
        alone: list[tuple[str, tuple[str, ...]]] = []  # refused alone: the decision rests on the rest
        passing: list[dict] = []
        salvage = None
        change = None  # the frame of the request's own transformation, when it exists (reading F27)
        integrating = None  # the X an integrating request names, recorded on a rejection on its merits (F35)
        support = derive(chain, self.trees) if records or not reasons else None
        s = support.s if support is not None else None
        if s is not None:
            known = set(s.records)
            revisions = {(u, s.h.view(k).rev(u)) for k in range(s.n + 1) for u in s.h.view(k).structure.units}
            seen_triples: list[set[tuple[str, str, str]]] = []

            def triples() -> set[tuple[str, str, str]]:
                """Every subject triple an admitted position held: computed once, on demand."""

                if not seen_triples:
                    seen_triples.append({(u, s.h.view(k).scope_id(u), s.h.view(k).rev(u)) for k in range(s.n + 1)
                                         for u, unit in s.h.view(k).structure.units.items() if unit.subject})
                return seen_triples[0]
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
                    if record["frame"] == "ADMITTED":  # a frame record's target is its frame's (§7.5)
                        units, pairs, named_triples = target_references(record)
                        if record["kind"] in ("ACCEPTANCE", "LEGACY_ACCEPTANCE"):
                            named_triples = set()  # step 3's own codes judge an acceptance's triple (SD-68)
                        if units - set(s.view.structure.units) or pairs - revisions or named_triples - triples():
                            own.append("REF_TARGET")  # the target exists (§8.3 step 2; review c80fc6a B1)
                        aimed = s.record(target["record"]) if target.get("record") in known else next(
                            (p for p in passing if p["id"] == target.get("record")), None)
                        if record["kind"] == "MATERIALITY_RECLASSIFICATION" and aimed is not None \
                                and aimed["kind"] not in (*REPORT_KINDS, "CHALLENGE"):
                            own.append("REF_TARGET")  # it reclassifies a report or a challenge (§15.2)
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
                if request.get("candidates"):  # an integrating request (§11.5): steps 3-4 on its frame (4c-iii)
                    reasons |= integration_codes(request["candidates"][0], support, request.get("binding"))
                    change = integration_frame(request["candidates"][0], support)
                    found = submitted_with(request["candidates"][0], support.s)
                    integrating = found[0] if len(found) == 1 else None
                elif adopting:
                    change = adoption_frame(support.s, self.expected_head(entries), request.get("adopted_deltas"))
                change = change if isinstance(change, Frame) and change.exists else None
                position = request.get("base_position")
                base = Workflow.historical(support.s.h, position) if "REF_BASE" not in reasons \
                    and isinstance(position, int) and 0 <= position <= s.n else None
                before = passing
                currency = Currency(support, change)
                legality = Legality(support, currency.locate)
                passing, more, ok, alone, last = self.authorized(request, passing, chain, entries, base, auth, change,
                                                                 (currency, legality))
                if ok:  # step 7's request-level checks, over what passed (Phase F steps 5b, 5d)
                    after = last
                    if after is None and request.get("claims"):  # a claim is judged after the request (§8.3 step 7)
                        head = entries[-1]
                        expected = self.expected_head(entries)
                        empty = self.admission_entry(head, expected, request_id(request), "ACCEPT", (), [], (), expected)
                        after = self.trial(chain, empty, auth.objects, change)
                    reasons |= legality.request_codes(request, passing, after)
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
        if not reasons and not blocking(refused, alone) and gated(request, records, support, change):
            reasons.add("SCHEMA_UNSUPPORTED")  # what Phase F does not yet accept: fail closed (§8.3 step 1; 6c)
        return reasons, refused, passing, auth, alone, salvage, integrating

    def cascade(self, records: list[dict], chain) -> tuple[list[dict], list[tuple[str, tuple[str, ...]]]]:
        """Records that name only records existing (admitted before, or kept with them) and only transformations a
        result fixes there (a co-submitted result refused fixes nothing; review 23b487a B1), to a fixed point; the
        rest refused ``REF_RECORD`` or ``REF_TRANSFORMATION`` (§8.3 steps 2, 6 and 9; reading F40)."""

        state = derive(chain, self.trees).s
        known, fixed_before = set(state.records), set(state.submissions)
        kept: list[dict] = list(records)
        drops: list[tuple[str, tuple[str, ...]]] = []
        while True:
            ids = {r["id"] for r in kept}
            dangling = [r for r in kept if referenced_records(r) - known - ids]
            fixed = fixed_before | {r["target"]["transformation"] for r in kept
                                    if r["kind"] == "TASK_RESULT" and submits(r["target"])}
            unfixed = [r for r in kept if r not in dangling
                       and transformation_named(r) is not None and transformation_named(r) not in fixed]
            if not dangling and not unfixed:
                return kept, drops
            kept = [r for r in kept if r not in dangling and r not in unfixed]
            drops += [(r["id"], ("REF_RECORD",)) for r in dangling]
            drops += [(r["id"], ("REF_TRANSFORMATION",)) for r in unfixed]

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

    def authorized(self, request: Mapping[str, Any], passing: list[dict], chain, entries, base, auth, change=None,
                   checks: tuple = ()):
        """Authorize the records in the trial extension of their own request (reading F10), in the state after the
        request's own transformation when ``change`` is its frame (reading F27), with the per-record ``checks`` of
        steps 6-7 (``codes(record, trial)``) joining each round's refusals (reading F10; steps 4e-ii, 5b), removing
        each refused
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
            refusals = dict(result.refused)
            for record in passing:
                more = set().union(*(check.codes(record, last) for check in checks)) if checks else set()
                if more:
                    refusals[record["id"]] = tuple(sorted(set(refusals.get(record["id"], ())) | more))
            later = [] if refusals or result.alone else conformance_alone(passing, last)  # step 7, 5c
            if not refusals and not result.alone and not later:
                break
            gone = set(refusals) | {rid for rid, _ in result.alone + tuple(later)}
            refused += list(refusals.items())
            alone += list(result.alone) + later
            passing = [r for r in passing if r["id"] not in gone]
            last = None
        return passing, refused, True, alone, last


def _absorbs(record: Mapping[str, Any]) -> bool:
    """An ``ABSORB`` disposition of a quarantined delta: an adoption (§18.4)."""

    return record.get("kind") == "INTAKE_DISPOSITION" and record.get("outcome") == "ABSORB" \
        and "delta" in target_type(record)


def target_type(record: Mapping[str, Any]) -> set[str]:
    """The target shape a record uses: ``delta``, ``content_ref`` or ``paths`` for an intake record."""

    target = record.get("target")
    if isinstance(target, Mapping) and {"absorption", "key"} <= set(target):
        return {"delta"}
    if isinstance(target, Mapping) and "paths" in target:
        return {"paths"}
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


#: What Phase F accepts: each kind, with the target shapes whose every reference a built check verifies (step 2's
#: REF_RECORD and REF_TARGET, step 3's acceptance rules, 4c-iv's delta, 5b-iii's decision names). Every other kind
#: or shape fails closed until its checks exist: a TASK_RESULT (SD-70), a runner's evidence or its assessment (step
#: 9), an external, a human decision, an observation, a gate decision, a risk override (whose continuation names
#: subjects and items in its fields), and the rest (plan step 6c; reviews c80fc6a B1, c9c937d).
_ACCEPTED = {
    **{kind: {"units", "records"} for kind in REPORT_KINDS},
    "CHALLENGE": {"record", "triple"}, "ADJUDICATION": {"record"}, "WITHDRAWAL": {"record"},
    "NON_AUTHORSHIP_ATTESTATION": {"record"}, "MATERIALITY_RECLASSIFICATION": {"record"},
    "COORDINATION_DECISION": {"records", "units"}, "ACCEPTANCE": {"triple"}, "LEGACY_ACCEPTANCE": {"triple"},
    "REVIEW": {"triple"}, "EQUIVALENCE": {"equivalence"}, "INTAKE_DISPOSITION": {"delta"},
}


def _shape(target: Any) -> str | None:
    """A target's shape, by its keys."""

    if not isinstance(target, Mapping):
        return None
    keys = set(target)
    for shape, needed in (("triple", {"subject", "scope_id", "rev"}), ("equivalence", {"unit", "from", "to"}),
                          ("delta", {"absorption", "key"}), ("record", {"record"}), ("records", {"records"}),
                          ("units", {"units"})):
        if needed <= keys:
            return shape
    return None


def gated(request: Mapping[str, Any], records: list, support: Any, change: Any) -> bool:
    """What Phase F does not yet accept, though every built check passed (plan step 6c): any record outside
    ``_ACCEPTED``; a request depending on a task result's conformance (candidates, or a claim of an item obligation,
    whose discharge reads conformance), until A10's D4 (SD-70, SD-71); and an adoption while any realization is
    admitted, a stricter form of SD-72's rule (F42), until step 8."""

    if any(not isinstance(r, Mapping) or _shape(r.get("target")) not in _ACCEPTED.get(r.get("kind"), ())
           for r in records) or request.get("candidates"):
        return True
    items = Workflow(support).items if support is not None else None
    if any(items is None or items.of(c) is not None for c in request.get("claims") or []):
        return True
    adopting = isinstance(change, Frame) and change.enactment is None
    return bool(adopting and support.s.of_kind("REALIZATION"))


def submitted_with(candidate: str, s: Any) -> list[str]:
    """The transformations an admitted result submits with candidate ``C``."""

    return sorted(x for x in s.submissions if (t := transformation_of(s, x)) is not None and t.candidate == candidate)


def integration_frame(candidate: str, support: Any) -> Any:
    """The frame of the transformation an admitted result submits with candidate ``C``, built at the head, or the
    code refusing it: none or more than one such ``X``, an enactment already integrated, or a merge conflict."""

    s = support.s
    found = submitted_with(candidate, s)
    if len(found) != 1:
        return "REF_TRANSFORMATION"  # none, or more than one (a rebase frame is unsupported, Q-F6 (iii))
    x = found[0]
    if s.enactment(x) in s.integrated:
        # one enactment, one integration (SD-26; step 5d); OVERTAKEN and fenced integrations are step 6's
        return "OBLIGATION_REENACTED"
    frame = Frame(s.h, s.n, transformation_of(s, x), s.enactment(x))
    if frame.merged is None:
        return "STRUCT_MERGE_CONFLICT"  # no frame, so nothing integrates (§7.4)
    return frame


def _waits(hit: Any) -> bool:
    """A conformance hit that waits on an execution or a runner, not on the candidate (§14.3, §17.5; step 5d):
    tagged where conformance makes it (review c06f5be N3), or unrealized required evidence."""

    return hit.waits or hit.template == "OBLIGATION.required_evidence"


def conformance_codes(conformance: Any) -> set[str]:
    """The exact candidate's conformance at an integration (§8.3 step 7, §14.6; step 5d). Its own defect is
    ``CONFORMANCE_FAILED``, a merit (F35): a violation; a discrepancy other than the outcome being ``COMPLETE``
    while something is still unmet, unless the result's own templates show it (F30); an ``INCOMPLETE`` that was
    evaluated (a ``DOMAIN`` template, a ``HARD`` check reporting only a signal; review b546a2b N1). What waits on an
    execution or a runner is ``CONFORMANCE_INCOMPLETE``, and the candidate stays pending."""

    own = any(h.cls == "VIOLATION" or (h.cls == "DISCREPANCY" and h.template != "FAITHFULNESS.outcome_consistent")
              or (h.cls == "INCOMPLETE" and not _waits(h)) for h in conformance.hits) \
        or any(h.cls in ("DISCREPANCY", "INCOMPLETE") for h in conformance.result_only)
    if own:
        return {"CONFORMANCE_FAILED"}
    return set() if conformance.clean else {"CONFORMANCE_INCOMPLETE"}


def review_codes(x: str, support: Any, workflow: Any) -> set[str]:
    """An integrating request claims together with its current review judgments (§11.5 (3)), read from the
    ledger (reading F32): ``REVIEW(X)`` discharged at the head (``OBLIGATION_PREDICATE_UNMET`` otherwise), by
    reviews whose judged content is what the merged state integrates (§5.10 (b); the judged-content check that
    replaces ``STALE_RETAINED``'s retained units, step 5d)."""

    s = support.s
    review = next((o for o in workflow.binding_index().values()
                   if o.kind == "REVIEW" and o.target == {"transformation": x}), None)
    # the judgments the integration claims with: passing reviews of X acting in its frame, none superseded there,
    # where a frame record's supersession acts (review b546a2b N2)
    framed = support.frame_support(x)
    there = framed.s if framed is not None else s
    reviews = [r for r in s.of_kind("REVIEW") if s.record(r)["target"] == {"transformation": x}
               and passing(s.record(r)) and r in there.records and there.acts(r) and not there.superseded(r)]
    if reviews and not any(support.j.supports_integration(r, s.n) for r in reviews):
        return {"STALE_RETAINED"}  # what was reviewed is not what integrates
    if review is None or workflow.discharge(review) not in ("DISCHARGED", "DISCHARGED_PROVISIONAL"):
        return {"OBLIGATION_PREDICATE_UNMET"}  # no current, qualified, independent passing review yet
    return set()


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
        return {"AUTH_ENVELOPE"}  # §11.5 (3): an integration request is bound to the producing task (step 5d)
    codes = {f.code for f in frame.structural.findings}
    conformance = workflow.conformance(workflow.submitting_result(x))
    codes |= conformance_codes(conformance)
    codes |= review_codes(x, support, workflow)
    contract = conformance.contract[0]
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
