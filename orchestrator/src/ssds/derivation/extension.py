"""The trial extension (Phase F reading F10): the derived state as if one more entry were admitted.

Admission judges a request through the owners derivation already has, so it never restates a rule for records
not yet admitted: it builds the entry it would append and asks for the state at ``n+1`` with that entry in
place. The trial is a new :class:`History` over the readable prefix plus that one entry, never a mutation of an
existing one, so every cache keyed on a history stays sound (reading F7) and the held head is untouched.

The trial entry is not signed, so it has no digest; it is given ``trial:`` and the hash of its content. Facts
keyed on an entry's digest therefore differ at the trial position from the state after admission: run identities
at an event with no enactment (``runs``), ``SPEC_REVIEW`` and ``JOINT_INVARIANT`` obligation identities
(``workflow``), item change facts (``items``) and query listings (``queries``). No decision of validation steps
3-6 reads them (reading F10); every other fact equals the state derived after admitting the same entry. Phase F
steps 4a-4b take records-only requests only: a trial of a request with candidates or adopted deltas needs
``Σ_{n+1}`` and the merged tree, which step 4c supplies.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ssds.ledger.read import Chain, LedgerEntry

from .history import History, TreeSource, _digest
from .state import State
from .support import Support


def trial_chain(chain: Chain, entry: Mapping[str, Any], objects: Mapping[str, bytes] | None = None) -> Chain:
    """The readable prefix of ``chain`` with ``entry`` appended as its next position."""

    prefix = chain.entries[: chain.readable_through + 1]
    head = prefix[-1]
    if entry.get("position") != head.position + 1:
        raise ValueError(f"a trial entry takes position {head.position + 1}, not {entry.get('position')!r}")
    body = dict(entry)
    digest = "trial:" + _digest(body)
    item = LedgerEntry(head.position + 1, "trial", (head.commit,), body, b"", b"", digest, dict(objects or {}))
    return Chain(chain.ledger_id, (*prefix, item))


def trial(chain: Chain, trees: TreeSource, entry: Mapping[str, Any],
          objects: Mapping[str, bytes] | None = None) -> Support:
    """``D_{n+1}`` with ``entry`` admitted at ``n+1``: the state Admission reads a request's records in."""

    return Support(State(History(trial_chain(chain, entry, objects), trees)))


__all__ = ["trial", "trial_chain"]
