"""Validation step 5's per-record checks (Manual §8.3 step 5, §8.5; catalogue §8.3 step 5, §8.4, §3.4, §5.3;
Phase F plan §3.1, step 4d, readings F22-F25).

Admission decides here and derivation supplies every fact, read from the trial extension (reading F10), where the
request's records exist:
- a challenge-tier record's target is strictly earlier by ledger position (``DEP_TARGET_ORDER``) and of a kind
  catalogue §3.4 permits (``DEP_TARGET_KIND``): a ``CHALLENGE`` of a support-tier record, a triple, an adjudication
  or a risk override; an ``ADJUDICATION`` or ``RISK_OVERRIDE`` of a challenge; a ``WITHDRAWAL`` of a challenge or
  report its own actor raised (§15.2; another actor's is ``AUTH_ACTOR``). A ``CHALLENGE`` of a ``CHALLENGE`` is
  ``DEP_COUNTER_CHALLENGE`` (F25), and a ``CHALLENGE`` of a ``CONTINUITY_ATTESTATION`` is permitted (§23.7). A
  ``CONTINUITY_ATTESTATION`` targets an earlier ``LEDGER_LOSS`` and stays ``SCHEMA_UNSUPPORTED``: no policy key
  designates its actor (step 7f, readings F48, F63);
- no ``validity`` entry on one of the record's own subjects (``DEP_OWN_SUBJECT``, F22);
- no ``EQUIVALENCE`` with a ``validity`` entry on a consumer of its unit (``DEP_CONSUMER``, F23).

The last two read a record declaring an unintegrated ``X`` in ``X``'s frame, where it acts.

A never-lost record owes these checks too, so salvage never writes a target §5.7 calls corruption. The support
graph's acyclicity (``CYCLE_SUPPORT``, F24) is request-level: the engine compares the final trial's static graph,
and an integration's or adoption's frame, with the head's (``Support.grows_a_cycle``).
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ssds.ledger.read import SUPPORT_TIER

from .request import REPORT_KINDS

CHALLENGE_TIER = frozenset({"CHALLENGE", "ADJUDICATION", "WITHDRAWAL", "RISK_OVERRIDE", "CONTINUITY_ATTESTATION"})


def dependency_codes(record: Mapping[str, Any], trial: Any) -> set[str]:
    """Step 5's codes for one record of the request, in the trial where it exists."""

    s = trial.s
    kind = record["kind"]
    codes: set[str] = set()
    target = record["target"] if isinstance(record["target"], Mapping) else {}
    targeted = target.get("record")
    if kind == "CONTINUITY_ATTESTATION":
        # §23.7: it targets an earlier admitted loss (step 7f, reading F63); and it stays unsupported, since no policy
        # key designates its actor (F48)
        codes.add("SCHEMA_UNSUPPORTED")
        targeted = target.get("loss")
    if kind in CHALLENGE_TIER and isinstance(targeted, str) and targeted in s.records:
        if s.position_of(targeted) >= s.position_of(record["id"]):
            codes.add("DEP_TARGET_ORDER")  # strictly earlier (§8.5): a co-submitted target never is
        aimed = s.record(targeted)
        target_kind = aimed["kind"]
        if kind == "CONTINUITY_ATTESTATION":
            if target_kind != "LEDGER_LOSS":
                codes.add("DEP_TARGET_KIND")
        elif kind == "CHALLENGE":
            if target_kind == "CHALLENGE":
                codes.add("DEP_COUNTER_CHALLENGE")
            elif target_kind not in SUPPORT_TIER and target_kind not in (
                    "ADJUDICATION", "RISK_OVERRIDE", "CONTINUITY_ATTESTATION", "REALIZATION"):
                # §3.4, §23.7: any may challenge it; a realization too (§6.7, Manual §6.7; reading F101)
                codes.add("DEP_TARGET_KIND")
        elif kind in ("ADJUDICATION", "RISK_OVERRIDE"):
            if target_kind != "CHALLENGE":
                codes.add("DEP_TARGET_KIND")
        elif kind == "WITHDRAWAL":
            if target_kind != "CHALLENGE" and target_kind not in REPORT_KINDS:
                codes.add("DEP_TARGET_KIND")
            elif aimed["actor"] != record["actor"]:
                codes.add("AUTH_ACTOR")  # only the raiser withdraws (§3.4, §15.2)
    # a record declaring an unintegrated X acts in X's frame, so its own subjects and consumers are read there,
    # whichever trial judges it: the head's for salvage too (review cab6179a B1)
    declared = record.get("frame")
    x = declared.get("transformation") if isinstance(declared, Mapping) else None
    framed = trial.frame_support(x) if isinstance(x, str) and s.enactment(x) not in s.integrated else None
    if framed is not None:
        trial, s = framed, framed.s
    structure = s.view.structure
    own = trial.j.own_subjects(dict(record))
    validity = [e["target"]["unit"] for e in record.get("basis") or []
                if e.get("mode") == "validity" and isinstance(e.get("target"), Mapping)]
    if any(u in structure.units and structure.subj(u) in own for u in validity):
        codes.add("DEP_OWN_SUBJECT")
    if kind == "EQUIVALENCE" and isinstance(target.get("unit"), str):
        consumers = s.s0.consumers(target["unit"])
        if any(u in consumers for u in validity):
            codes.add("DEP_CONSUMER")
    return codes


__all__ = ["CHALLENGE_TIER", "dependency_codes"]
