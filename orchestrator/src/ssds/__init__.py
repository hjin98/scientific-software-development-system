"""SSDS: one program, ``ssds`` (Manual §26.3, A7).

``ssds.core`` is the Level 0 Core, whose version-bound behaviour is unchanged;
each other subpackage is one SSDS 8 component of Manual §26.1, and the
dependency rule between them is Manual §26.2. ``ssds.cli`` is the only
composition root. Public surfaces are ``ssds.api.v1`` and ``ssds.spi.v1``
(Core's are ``ssds.core.api.v1`` and ``ssds.core.spi.v1``).

Shadow implementation only: SSDS holds no authority over any subject.
"""
