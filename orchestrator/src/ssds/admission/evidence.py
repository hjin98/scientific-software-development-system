"""Validation steps 1 and 2 for evidence: a runner's realization and an ordinary assessment (Manual §8.3 steps 1-2,
§6.3, §6.5, §6.9, §17.2, §17.4; Phase F plan §3.6, steps 9d-i and 9d-ii, readings F96-F97 and F100).

Admission decides here and derivation owns the facts: the realization's closed shape and ``on⁻`` are read through
derivation's one reader (``read_realization``, ``on_minus``; F88), never re-implemented.

- **Step 1.** An execution outside the closed shape is ``SCHEMA_RECORD`` (F78).
- **Step 2.** The record is in the admitted state and ``tree(o)`` is the head of an admitted position ``k``; otherwise
  it is evidence on a candidate or merged tree, ``SCHEMA_UNSUPPORTED`` (SD-70). ``k`` is the latest such position no
  later than ``start``. A late run on an older admitted head is admitted (§6.9). The specification's and every
  claim's revision are ``view(k)``'s (``REF_TARGET``); every recorded
  term re-resolves in ``tree(o)`` (``REF_EXECUTION``), a recorded context the host lacks being ``SCHEMA_UNSUPPORTED``
  (§6.3); each bounding judgment is admitted (``REF_RECORD``); ``k ≤ start ≤ end ≤ n`` (``REF_EXECUTION``); and the
  evaluated outcome is a stored or co-submitted JSON object (``REF_OBJECT``, ``SCHEMA_OBJECT``).
"""

from __future__ import annotations

import json
from collections.abc import Container, Mapping
from typing import Any

from ssds.derivation import is_reading, on_minus, read_reading, read_realization


def realization_shape(record: Mapping[str, Any]) -> list[str]:
    """Step 1: a ``REALIZATION`` outside the closed shape (F78, F96)."""

    if record.get("kind") != "REALIZATION":
        return []
    return ["SCHEMA_RECORD"] if not read_realization(str(record.get("id")), dict(record)).well_formed else []


def realization_references(record: Mapping[str, Any], s: Any, known: Container[str],
                           objects: Mapping[str, bytes]) -> list[str]:
    """Step 2 for a well-formed ``REALIZATION`` in state ``s``: its codes, empty when it is admissible here.
    ``known`` holds the record identities admitted or passing before it, ``objects`` the stored and co-submitted
    ledger objects by digest."""

    if record.get("kind") != "REALIZATION":
        return []
    execution = record["fields"]["execution"]
    if record.get("frame") != "ADMITTED":
        return ["SCHEMA_UNSUPPORTED"]  # frame evidence (SD-70)
    heads = [p for p in range(s.n + 1) if s.h.head(p) == execution["tree"]]
    if not heads:
        return ["SCHEMA_UNSUPPORTED"]  # a candidate's or merged tree's evidence (SD-70)
    # k: the state the run started from, the latest admitted position no later than its start whose head is its
    # tree, so a recurring tree is read under the structure then (review of 885a949c, note 1)
    started = [p for p in heads if p <= execution["start"]]
    k = started[-1] if started else heads[0]
    codes = []
    view = s.h.view(k)
    target = record["target"]
    named = [target["spec"], *target.get("claim", [])]
    if any(not isinstance(n, Mapping) or n.get("unit") not in view.structure.units or view.rev(n["unit"]) != n.get("rev")
           for n in named):
        codes.append("REF_TARGET")  # the revisions it ran on are tree(o)'s (§6.3)
    found = on_minus(execution, s.h.trees(execution["tree"]), s.analyzer_set)
    if found is None:
        codes.append("SCHEMA_UNSUPPORTED")  # a host lacking the recorded context makes no current assertion (§6.3)
    elif not found:
        codes.append("REF_EXECUTION")
    bounded = execution["bounded_by"]
    if isinstance(bounded, list) and any(c not in known for c in bounded):
        codes.append("REF_RECORD")
    if not started or not execution["start"] <= execution["end"] <= s.n:
        codes.append("REF_EXECUTION")  # a run starts on a tree only once it is admitted, and ends by the head
    data = objects.get(record["fields"].get("evaluated"))
    if data is not None:  # an absent one is REF_OBJECT, by referenced_objects
        try:
            parsed = json.loads(data)
        except (ValueError, TypeError):
            parsed = None
        if not isinstance(parsed, dict):
            codes.append("SCHEMA_OBJECT")  # §17.3's {output name: canonical value}
    return codes


def reading_shape(record: Mapping[str, Any]) -> list[str]:
    """Step 1: a discriminating reading outside its closed shape (reading F106)."""

    if not is_reading(dict(record)):
        return []
    return ["SCHEMA_RECORD"] if not read_reading(str(record.get("id")), dict(record)).well_formed else []


def assessment_references(record: Mapping[str, Any], s: Any, passing: Mapping[str, Mapping[str, Any]],
                          a: Any = None) -> list[str]:
    """Step 2 for an ``ORDINARY`` (step 9d-ii; reading F100) or ``DISCRIMINATING`` (step 9e-ii; reading F109)
    ``EVIDENCE_ASSESSMENT`` in state ``s``, with the shape checks that read state. ``passing`` holds the records
    passing before it, by identity; ``a`` is the state's ``Assessments``, which a reading's checks read."""

    mode = (record.get("fields") or {}).get("mode")
    if record.get("kind") != "EVIDENCE_ASSESSMENT" or mode not in ("ORDINARY", "DISCRIMINATING"):
        return []
    if mode == "DISCRIMINATING":
        return _reading_references(record, s, a) or _assessment_references(record, s, passing, ordinary=False)
    return _assessment_references(record, s, passing, ordinary=True)


def _reading_references(record: Mapping[str, Any], s: Any, a: Any) -> list[str]:
    """F109's step 2 for a reading: ``a⁻`` an assessor-read failure for its obligation, ``p`` and ``q`` complete
    runs of ``conf(a⁻)``, the failing item read under ``a⁻``'s reading, and ``q`` showing ``a⁻``'s outcome on
    ``F(a⁻)`` ("``a⁻``'s reproduced outcome"). A reading in a frame is ``SCHEMA_UNSUPPORTED`` (SD-70)."""

    if record.get("frame") != "ADMITTED":
        return ["SCHEMA_UNSUPPORTED"]
    r = read_reading(str(record.get("id")), dict(record))
    failure = s.record(r.failure) if r.failure in s.records else None
    if failure is None or failure["kind"] != "EVIDENCE_ASSESSMENT" or failure.get("outcome") != "FAIL" \
            or failure["target"].get("obligation") != (record.get("target") or {}).get("obligation"):
        return ["REF_TARGET"]
    real = a.real(r.failure)
    reading = failure["fields"].get("reading") or {}
    declared = s.specs.declaration_at(reading.get("unit"), reading.get("rev"))
    if real is None or getattr(declared, "oracle", None) != "ASSESSOR_READ":
        return ["REF_TARGET"]  # a reading discriminates only an assessor-read failure (§6.6)
    if r.fail_reading != (reading.get("unit"), reading.get("rev")):
        return ["REF_TARGET"]  # the failing item reads under a⁻'s reading
    configuration = set(a.observations(r.failure))
    for o in (r.passing, r.failing):
        if o not in configuration or s.record(o).get("outcome") != "COMPLETE":
            return ["REF_TARGET"]  # a complete run of conf(a⁻)
    failing = a.failing_outputs(r.failure)
    if a.restricted(r.failing, failing) != a.restricted(real, failing):
        return ["REF_TARGET"]  # q shows a⁻'s reproduced outcome on F(a⁻)
    return []


def _assessment_references(record: Mapping[str, Any], s: Any, passing: Mapping[str, Mapping[str, Any]],
                           ordinary: bool) -> list[str]:
    codes = []
    target, fields = record.get("target") or {}, record.get("fields") or {}
    real = target.get("realization")
    observed = s.record(real) if real in s.records else passing.get(real)
    if observed is None or observed.get("kind") != "REALIZATION":
        return ["REF_TARGET"]  # it assesses an admitted realization (§3.4)
    if observed.get("outcome") == "INCOMPLETE" and record.get("outcome") in ("PASS", "FAIL"):
        codes.append("REF_TARGET")  # §17.2: an incomplete realization "cannot enter a PASS/FAIL assessment"
    spec = (observed.get("target") or {}).get("spec") or {}
    claims = [c.get("unit") for c in (observed.get("target") or {}).get("claim") or [] if isinstance(c, Mapping)]
    if target.get("obligation") not in {s.evidence.token(c, spec.get("unit")) for c in claims if isinstance(c, str)}:
        codes.append("REF_TARGET")  # the obligation its specification and a claim give (F89 (a))
    reading = fields.get("reading")
    known_revs = {s.h.view(k).rev(spec.get("unit")) for k in range(s.n + 1)
                  if spec.get("unit") in s.h.view(k).structure.units}
    if not (isinstance(reading, Mapping) and reading.get("unit") == spec.get("unit") and reading.get("rev") in known_revs):
        codes.append("REF_TARGET")  # a revision of the realization's specification
        return codes
    if not ordinary:
        return sorted(set(codes))  # a reading's shape is its reader's (F106)
    named = fields.get("failing_outputs")
    if named and record.get("outcome") != "FAIL":
        codes.append("SCHEMA_RECORD")  # only a failure names failing outputs
    declared = s.specs.declaration_at(reading["unit"], reading["rev"])
    if named and hasattr(declared, "output") and any(declared.output(x) is None for x in named):
        codes.append("SCHEMA_RECORD")  # the declared outputs it found failing (§6.5; routed from 9c-ii-iii)
    if fields.get("observations"):
        codes.append("SCHEMA_RECORD")  # an ordinary reading carries no discriminating observations (F80)
    return sorted(set(codes))


def custody_problems(record: Mapping[str, Any]) -> list[str]:
    """A ``CUSTODY_ENUMERATION`` lists each run once (step 9d-iii; reading F102). Its runs need not be admitted (F81):
    derivation blocks the stop until each is, so they are no record references."""

    if record.get("kind") != "CUSTODY_ENUMERATION":
        return []
    runs = (record.get("fields") or {}).get("runs") or []
    return ["SCHEMA_RECORD"] if len(set(runs)) != len(runs) else []


__all__ = ["assessment_references", "custody_problems", "reading_shape", "realization_references",
           "realization_shape"]
