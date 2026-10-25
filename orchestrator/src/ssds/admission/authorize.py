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

Not built yet, so refused as ``SCHEMA_UNSUPPORTED`` (fail closed, plan §3.1): records declaring a candidate's frame
(step 4c), adjudications and discriminating readings (step 4b-ii), and lifecycle-tier records, which reach the
ledger only through the human-gated lifecycle path.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ssds.derivation import ROLE_TEMPLATES, role_permits, supersession_target, triple_key
from ssds.ledger.read import LIFECYCLE_TIER, SUPPORT_TIER

from .request import REPORT_KINDS

#: Support-tier kinds only the principal of the same plan supersedes, by a record of the same kind (§12.5).
PRINCIPAL_SUPERSEDED = frozenset({"COORDINATION_DECISION", "MATERIALITY_RECLASSIFICATION"})


@dataclass(frozen=True)
class Authorization:
    ok: bool  # the envelope's obligation and role hold: never-lost salvage may proceed
    reasons: frozenset[str] = frozenset()  # request-level
    refused: tuple[tuple[str, tuple[str, ...]], ...] = ()


def authorize(request: Mapping[str, Any], records: list[dict], trial: Any, base: Any) -> Authorization:
    """``trial`` is the trial extension's ``Support`` with ``records`` admitted; ``base`` the workflow at the
    request's base position, or ``None`` when that position is not valid (``REF_BASE``)."""

    binding = request.get("binding") or {}
    envelope = binding.get("envelope") if "envelope" in binding else None
    obligation = None
    if envelope is not None:
        obligation = next((o for o in base.obligations if o.id == envelope["obligation_id"]), None) if base else None
        if obligation is None or obligation.holder != envelope["role"] or envelope["role"] not in ROLE_TEMPLATES:
            return Authorization(False, frozenset({"AUTH_ENVELOPE"}))
    refused = []
    for record in records:
        codes = _record_codes(record, envelope, trial, base, obligation)
        if codes:
            refused.append((record["id"], tuple(sorted(codes))))
    return Authorization(True, frozenset(), tuple(refused))


def _record_codes(record: dict, envelope: Mapping[str, Any] | None, trial: Any, base: Any, obligation: Any) -> set[str]:
    kind = record["kind"]
    if kind in LIFECYCLE_TIER:
        return {"AUTH_ROLE_KIND"} if envelope is not None else {"SCHEMA_UNSUPPORTED"}
    codes: set[str] = set()
    if envelope is not None and not role_permits(envelope["role"], kind, record.get("outcome")):
        codes.add("AUTH_ROLE_KIND")
    if record["frame"] != "ADMITTED" or kind in ("ADJUDICATION", "PRODUCT_SCOPE_ACCEPTANCE") \
            or (kind == "EVIDENCE_ASSESSMENT" and (record.get("fields") or {}).get("mode") == "DISCRIMINATING"):
        # not built: frames (4c); adjudications and readings (4b-ii); the product-scope authority policy
        # designates (§3.5; plan review 8a41539 B4)
        codes.add("SCHEMA_UNSUPPORTED")
        return codes
    if not trial.qualified(record, trial.j.domain_of(record)):
        codes.add("AUTH_ACTOR")
    if kind == "ACCEPTANCE":
        codes |= _acceptance_target(record, trial)
    if any(not _supersession_authorized(record, x, envelope, trial, base, obligation)
           for x in record.get("supersedes") or []):
        codes.add("AUTH_SUPERSEDES")
    if any(_supersession_unbuilt(x, trial) for x in record.get("supersedes") or []):
        codes.discard("AUTH_SUPERSEDES")
        codes.add("SCHEMA_UNSUPPORTED")
    return codes


def _supersession_unbuilt(superseded: str, trial: Any) -> bool:
    """A supersession whose authority needs an owner not built yet: a conditional supersession target (§5.10 (b))
    or the plan of a principal's decision (plan review 8a41539 B2)."""

    s = trial.s
    if superseded not in s.records:
        return False
    x = s.record(superseded)
    return x["kind"] in PRINCIPAL_SUPERSEDED or (x["kind"] in SUPPORT_TIER and x["kind"] not in REPORT_KINDS
                                                and supersession_target(x) is None)  # a conditional target


def _acceptance_target(record: dict, trial: Any) -> set[str]:
    s = trial.s
    target = record["target"]
    subject = target.get("subject")
    units = s.view.structure.units
    if not isinstance(subject, str) or subject not in units:
        return {"SCHEMA_UNSUPPORTED"}  # not an effective subject: a tenure code is Q-F5's
    if not units[subject].subject:
        return {"AUTH_TARGET_PART"}
    if s.status1(triple_key(subject, target.get("scope_id"), target.get("rev"))) == "REVOKED":
        return {"AUTH_TARGET_REVOKED"}
    if (subject, target.get("scope_id"), target.get("rev")) != tuple(s.subject_triple(subject)):
        # the current tenure, read as the subject's current triple: an earlier revision or another scope has no
        # code in catalogue §8.4 yet (Q-F5), so it fails closed (plan review 8a41539 B3)
        return {"SCHEMA_UNSUPPORTED"}
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
