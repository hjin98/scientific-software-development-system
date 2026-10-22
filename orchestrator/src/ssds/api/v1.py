"""``ssds.api.v1``: logical operations and records (Manual §26.3).

A re-export facade over component public modules; no component imports it. The
API is frozen once, at the G3 implementation review (Manual §26.4, §5.8 row).
"""

from ssds.interface.operations import LedgerAccess, Presented, Session, present

API_MAJOR = 1

__all__ = ["API_MAJOR", "LedgerAccess", "Presented", "Session", "present"]
