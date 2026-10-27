"""Validation steps 1 and 2 for a runner's realization (Manual §8.3 steps 1-2, §6.3, §6.9, §17.2; Phase F plan §3.6,
step 9d-i, readings F96-F97).

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

from ssds.derivation import on_minus, read_realization


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


__all__ = ["realization_references", "realization_shape"]
