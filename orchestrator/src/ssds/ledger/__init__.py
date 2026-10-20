"""Ledger Store (Manual §26.1): persistence, authentication and chain verification,
currentness qualification, the non-admission bound and replica restore. Never
interprets records or presents a provisional or unqualified head as current.

Public modules: ``read`` and ``qualification``; ``append`` is imported only by
Admission (Manual §26.2), so this package never re-exports it.
"""
