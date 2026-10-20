"""SSDS Level 0 Core: configuration, observation, workplan/profile resolution, prompt rendering.

Public surfaces are ``ssds.core.api.v1`` and ``ssds.core.spi.v1``.
Other modules are implementation detail under the API policy; their descriptive
names do not create compatibility paths.
"""

__all__ = ["CORE_DISTRIBUTION", "CORE_API_MAJOR", "CORE_SPI_MAJOR"]

CORE_DISTRIBUTION = "ssds"
CORE_API_MAJOR = 1
CORE_SPI_MAJOR = 1
