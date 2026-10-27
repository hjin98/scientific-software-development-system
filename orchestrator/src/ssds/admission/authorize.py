"""Validation step 3's authorization (Manual §8.3 step 3; catalogue §8.3 step 3; Phase F plan §3.1, step 4b-i).

Admission decides here and derivation supplies every fact, read from the trial extension (reading F10) or the
workflow at the request's base:
- the envelope names an obligation existing at the request's base, issued for the role that obligation's kind
  holds (``AUTH_ENVELOPE``); otherwise the binding authenticates nothing and nothing under it is salvaged;
- the bound role's template permits each record's kind and outcome (§12.3, ``AUTH_ROLE_KIND``);
- each record's actor meets the floors and policy qualifications of §3.5 (``AUTH_ACTOR``);
- an acceptance targets an effective subject, never a part (``AUTH_TARGET_PART``), never a ``REVOKED`` triple
  (``AUTH_TARGET_REVOKED``), never an ill-formed revision or one with a declared term ``ABSENT``
  (``AUTH_ILL_FORMED``);
- a supersession is authorized by the kind of what it supersedes (``AUTH_SUPERSEDES``).

An ``ADJUDICATION`` is admitted only if eligible: independent of its chain's root authors and of a class not lower
than its chain's (catalogue §5.10 (e), §12.4); an ineligible one is refused alone (``AUTH_ACTOR``), the rest of the
request judged as if it were absent (step 4b-ii).

A record declaring a transformation's frame is judged there: an acceptance against the frame's own structure and
triples (prospective tenure, step 4c-iii).

Step 5's per-record checks (``dependency``, step 4d) run in the same loop, so a refusal of either removes the
record before the trial is rebuilt.

A re-issue's resubmission (step 8g-ii, reading F74): when every record is a resubmission authentication matched to an
identity a ``REISSUE`` obligation at the base lists, the existence half is met by that obligation, and the envelope's
role is judged against the original obligation as derived at the original issue (plan check of 53216046 B1; re-check
of 25bd1d0d, B1 and note 1). Any other record citing ``reissue_of`` stays ``SCHEMA_UNSUPPORTED``.

Not built yet, so refused as ``SCHEMA_UNSUPPORTED`` (fail closed, plan §3.1): discriminating readings (step 9),
product-scope acceptance, and lifecycle-tier records, which reach the ledger only through the human-gated lifecycle
path.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ssds.derivation import ROLE_TEMPLATES, Support, frame_state, role_permits, supersession_target, triple_key
from ssds.ledger.read import LIFECYCLE_TIER, SUPPORT_TIER

from .dependency import dependency_codes
from .request import REPORT_KINDS

#: Support-tier kinds only the principal of the same plan supersedes, by a record of the same kind (§12.5).
PRINCIPAL_SUPERSEDED = frozenset({"COORDINATION_DECISION", "MATERIALITY_RECLASSIFICATION"})


@dataclass(frozen=True)
class Authorization:
    ok: bool  # the envelope's obligation and role hold: never-lost salvage may proceed
    reasons: frozenset[str] = frozenset()  # request-level
    refused: tuple[tuple[str, tuple[str, ...]], ...] = ()
    alone: tuple[tuple[str, tuple[str, ...]], ...] = ()  # refused alone: the request is judged without them


def authorize(request: Mapping[str, Any], records: list[dict], trial: Any, base: Any,
              resubmitted: Mapping[str, Any] | None = None) -> Authorization:
    """``trial`` is the trial extension's ``Support`` with ``records`` admitted; ``base`` the workflow at the
    request's base position, or ``None`` when that position is not valid (``REF_BASE``); ``resubmitted`` the listed
    identities authentication matched (``Authentication.retained``)."""

    binding = request.get("binding") or {}
    envelope = binding.get("envelope") if "envelope" in binding else None
    listed = frozenset(resubmitted or ())
    obligation = None
    if envelope is not None:
        originals = [resubmitted[_cited(r)] for r in records if _cited(r) in listed]
        if base is not None and records and len(originals) == len(records):
            obligation = originals[0].obligation  # one envelope, one original obligation (authentication matched)
        elif base is not None:
            obligation = next((o for o in base.obligations if o.id == envelope["obligation_id"]), None)
        if obligation is None or obligation.holder != envelope["role"] or envelope["role"] not in ROLE_TEMPLATES:
            return Authorization(False, frozenset({"AUTH_ENVELOPE"}))
    refused, alone = [], []
    for record in records:
        # step 5's per-record checks share this fixed point (step 4d): a refusal of either removes the record
        # a co-signer's attestation is the human's own record, authenticated by the co-signature: no role of the
        # envelope governs it (step 8d, reading F72; found building review 4f5caedb's N1)
        own = None if _cosigners(record, binding) else envelope
        codes = _record_codes(record, own, trial, base, obligation, listed) | dependency_codes(record, trial)
        if codes:
            refused.append((record["id"], tuple(sorted(codes))))
        elif record["kind"] == "ADJUDICATION" and not _adjudication_eligible(record, trial):
            alone.append((record["id"], ("AUTH_ACTOR",)))
    return Authorization(True, frozenset(), tuple(refused), tuple(alone))


def _cosigners(record: Mapping[str, Any], binding: Mapping[str, Any]) -> bool:
    """``record`` is the co-signing human's unbound record under a co-signed task binding (authentication admitted
    only its ``LINEAGE_ATTESTATION`` of a record bound here, reading F72)."""

    human = binding.get("human") if "envelope" in binding else None
    return isinstance(human, Mapping) and record.get("actor") == human.get("actor") \
        and record.get("actor_class") == "HUMAN" and record.get("binding") is None


def _cited(record: Mapping[str, Any]) -> Any:
    provenance = record.get("provenance")
    return provenance.get("reissue_of") if isinstance(provenance, Mapping) else None


def _adjudication_eligible(record: dict, trial: Any) -> bool:
    """Catalogue §5.10 (e): independent of the authors at its chain's root, by the one classification (its
    ``nonind``), and of a class not lower than its chain's (a human where the chain is R3, §12.4)."""

    if trial.j.nonind(record["id"]):
        return False
    challenge = (record["target"] or {}).get("record")
    return record["actor_class"] == "HUMAN" or not trial.j.chain_needs_human(challenge)


def _record_codes(record: dict, envelope: Mapping[str, Any] | None, trial: Any, base: Any, obligation: Any,
                  listed: frozenset = frozenset()) -> set[str]:
    kind = record["kind"]
    if kind in LIFECYCLE_TIER:
        return {"AUTH_ROLE_KIND"} if envelope is not None else {"SCHEMA_UNSUPPORTED"}
    codes: set[str] = set()
    if envelope is not None and not role_permits(envelope["role"], kind, record.get("outcome")):
        codes.add("AUTH_ROLE_KIND")
    resubmission = isinstance(record.get("provenance"), dict) and "reissue_of" in record["provenance"] \
        and record["provenance"]["reissue_of"] not in listed  # a listed one is step 8g-ii's (F74)
    if kind == "PRODUCT_SCOPE_ACCEPTANCE" or resubmission \
            or (kind == "EVIDENCE_ASSESSMENT" and (record.get("fields") or {}).get("mode") == "DISCRIMINATING"):
        # not built: discriminating readings (step 9);
        # the product-scope authority policy designates (§3.5; plan review 8a41539 B4); a re-issue's resubmission,
        # other than the listed one step 8g-ii's Dispatcher makes, under the re-issued task's envelope (review 8d274c4
        # B2; reading F74)
        codes.add("SCHEMA_UNSUPPORTED")
        return codes
    if not trial.qualified(record, trial.j.domain_of(record)):
        codes.add("AUTH_ACTOR")
    if record["actor_class"] != "HUMAN" and trial.a.disposition_needs_human(record):
        codes.add("AUTH_ACTOR")  # §6.8: disposing of a D1/D2 failure is R3, a human's (reading F101)
    if kind == "IMMATERIALITY" and not _immateriality_actor(record, trial, obligation):
        codes.add("AUTH_ACTOR")
    if kind in ("ACCEPTANCE", "LEGACY_ACCEPTANCE"):
        # a legacy import "supplies the acceptance for that (subject, scope_id, rev)" (§19.2), so it meets the same
        # target rules, on a subject the protocol it imports governs (review c80fc6a B1)
        codes |= _acceptance_target(record, _in_frame(record, trial))
        subject = (record.get("target") or {}).get("subject")
        if kind == "LEGACY_ACCEPTANCE" and isinstance(subject, str) and trial.s.mode(subject) != "LEGACY":
            codes.add("AUTH_VERSION")
    if any(not _supersession_authorized(record, x, envelope, trial, base, obligation)
           for x in record.get("supersedes") or []):
        codes.add("AUTH_SUPERSEDES")
    if any(_supersession_unbuilt(x, trial) for x in record.get("supersedes") or []):
        codes.discard("AUTH_SUPERSEDES")
        codes.add("SCHEMA_UNSUPPORTED")
    return codes


def _immateriality_actor(record: dict, trial: Any, obligation: Any) -> bool:
    """§3.4's "owner's qualified actor" (reading F101): for each failure it names, the claim domain's policy owner,
    or the actor bound to that failure's ``ADJUDICATE_DISAGREEMENT``, the obligation the owner holds (§10.2)."""

    s = trial.s
    for x in (record.get("target") or {}).get("records") or []:
        if x not in s.records:
            return False
        owner = s.policy.get(trial.j.domain_of(s.record(x)), "owner", None)
        bound = obligation is not None and obligation.kind == "ADJUDICATE_DISAGREEMENT" \
            and obligation.target.get("record") == x
        if record["actor"] != owner and not bound:
            return False
    return True


def _supersession_unbuilt(superseded: str, trial: Any) -> bool:
    """A supersession whose authority needs an owner not built yet: a conditional supersession target (§5.10 (b))
    or the plan of a principal's decision (plan review 8a41539 B2)."""

    s = trial.s
    if superseded not in s.records:
        return False
    x = s.record(superseded)
    return x["kind"] in PRINCIPAL_SUPERSEDED or (x["kind"] in SUPPORT_TIER and x["kind"] not in REPORT_KINDS
                                                and supersession_target(x) is None)  # a conditional target


def _in_frame(record: dict, trial: Any) -> Any:
    """The trial in the record's declared frame: the admitted trial, or ``X``'s frame state in it, read at the
    frame's own structure and triples (prospective tenure, catalogue §7.4-§7.5; 4c-iii). ``None`` when ``X``'s
    frame does not exist, so nothing in it is effective."""

    frame = record["frame"]
    if frame == "ADMITTED":
        return trial
    state = frame_state(trial.s.h, trial.s.n, frame["transformation"], trial.s)
    return Support(state) if state is not None else None


def _acceptance_target(record: dict, trial: Any) -> set[str]:
    if trial is None:
        return {"AUTH_TARGET_NOT_EFFECTIVE"}  # its frame does not exist (§7.4)
    s = trial.s
    target = record["target"]
    subject = target.get("subject")
    units = s.view.structure.units
    if not isinstance(subject, str) or subject not in units:
        return {"AUTH_TARGET_NOT_EFFECTIVE"}  # SD-68
    if not units[subject].subject:
        return {"AUTH_TARGET_PART"}
    if s.status1(triple_key(subject, target.get("scope_id"), target.get("rev"))) == "REVOKED":
        return {"AUTH_TARGET_REVOKED"}
    if (subject, target.get("scope_id"), target.get("rev")) != tuple(s.subject_triple(subject)):
        # the current tenure, read as the subject's current triple (plan review 8a41539 B3; SD-68)
        return {"AUTH_TARGET_NOT_CURRENT"}
    if not s.s0.well_formed(subject) or s.s0.absent_term(subject):
        return {"AUTH_ILL_FORMED"}
    return set()


def _supersession_authorized(record: dict, superseded: str, envelope: Mapping[str, Any] | None, trial: Any,
                             base: Any, obligation: Any) -> bool:
    """Catalogue §8.3 step 3, "supersession authority, by the kind of x": a report only by its raiser; a
    coordination decision or materiality reclassification only by the principal of the same plan, with a record
    of the same kind; every other support-tier record only by a record of the same kind on the same target that
    is its own author's reassessment or the owner's, independent (§5.10 (a)); nothing else is ever superseded."""

    s = trial.s
    if superseded not in s.records:
        return False
    x = s.record(superseded)
    if x["kind"] not in SUPPORT_TIER:  # challenge-tier, observation, admission and lifecycle: never
        return False
    if x["kind"] in REPORT_KINDS:
        return record["actor"] == x["actor"]
    if record["kind"] != x["kind"]:
        return False
    if x["kind"] in PRINCIPAL_SUPERSEDED:
        return False  # the same plan's principal: the plan's identity owner is not built (refused unsupported)
    target = supersession_target(x)
    if target is None or supersession_target(record) != target:
        return False
    if record["actor"] != x["actor"] and record["actor"] != trial.j.owner(x):
        return False
    return not trial.j.nonind(record["id"])


__all__ = ["Authorization", "PRINCIPAL_SUPERSEDED", "authorize"]
