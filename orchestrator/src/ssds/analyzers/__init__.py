"""Analyzers (Manual §26.1): derived relations, interface extraction, diff-to-unit
mapping and completeness declarations (§14.5). Never claims completeness it does
not have.

The analyzer set is pinned by the ruleset (Manual §5.9); a host's installation
never supplies one.
"""

from . import python
from .python import (
    Definition,
    ImportFacts,
    TestFacts,
    UnitFacts,
    declared_requirements,
    imports,
    is_requirements_file,
    is_test_file,
    module_names,
    parses,
    public_interface,
    requirement_name,
    stubs,
    test_facts,
    unit_comments,
    unit_facts,
)
from .units import dimension

#: Analyzer identity per file extension in the system ruleset's analyzer set.
ANALYZER_SET = {".py": python.ANALYZER_ID}


def analyzer_for(path: str) -> str | None:
    """The pinned analyzer identity for a file, or None when no analyzer covers its language."""

    for extension, identity in ANALYZER_SET.items():
        if path.endswith(extension):
            return identity
    return None


def resolve_symbol(path: str, data: bytes, symbol: str) -> tuple[int, int] | None:
    if analyzer_for(path) == python.ANALYZER_ID:
        return python.resolve_symbol(path, data, symbol)
    return None


__all__ = [
    "ANALYZER_SET", "Definition", "ImportFacts", "TestFacts", "analyzer_for", "declared_requirements", "imports",
    "is_requirements_file", "is_test_file", "module_names", "parses", "public_interface", "python", "requirement_name", "resolve_symbol",
    "stubs", "test_facts", "UnitFacts", "dimension", "unit_comments", "unit_facts",
]
