"""SSDS 8: graph-native deterministic orchestration, as a Core extension.

Shadow implementation only: SSDS holds no authority over any subject. The
architecture is ``orchestrator/docs/ssds-8.0-architecture.md`` (the Manual);
each subpackage is one component of Manual §26.1, and the dependency rule
between them is Manual §26.2. Public surfaces are ``sdp_orchestrator.ssds.api.v1``
and ``sdp_orchestrator.ssds.spi.v1``.
"""

__all__ = ["SSDS_DISTRIBUTION", "SSDS_SYSTEM_VERSION"]

SSDS_DISTRIBUTION = "sdp-orchestrator-ssds"
SSDS_SYSTEM_VERSION = "8.0.0"
