"""The one Core extension provider for SSDS, ``sdp.ssds`` (Manual §26.3).

Core discovers it only through the entry point declared in this distribution's
``pyproject.toml``; nothing imports this module. It provides no capability until
a component has a service to register (Manual §26.4 row 17 names the keys).
"""

from __future__ import annotations

from sdp_orchestrator.core.spi.v1 import (
    ExtensionContext,
    ExtensionId,
    ExtensionManifest,
    ExtensionRegistration,
)

from . import SSDS_SYSTEM_VERSION

EXTENSION_ID = "sdp.ssds"


class SSDSExtension:
    def manifest(self) -> ExtensionManifest:
        return ExtensionManifest(
            extension_id=ExtensionId(EXTENSION_ID),
            extension_version=SSDS_SYSTEM_VERSION,
            core_spi_spec=">=1.0.0,<2",
        )

    def activate(self, context: ExtensionContext) -> ExtensionRegistration:
        return ExtensionRegistration(detail="shadow: no capability provided yet")


provider = SSDSExtension()
