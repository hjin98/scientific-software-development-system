"""Content Model (Manual §26.1): the manifest, anchors and semantic declarations;
effective scopes resolved against observed bytes; authored relations; revisions
and scope identities. Never stores status or decides which structure is effective.
"""

from .git import GitReadError, read_tree
from .manifest import (
    DEFAULT_MANIFEST_PATH,
    GOVERNED_KEY,
    ID_RE,
    KINDS,
    Manifest,
    ManifestFailure,
    Term,
    parse_manifest,
    parse_term,
)
from .resolve import Region, Span
from .structure import (
    RESIDUAL_SUFFIX,
    SYSTEM_UNITS,
    UNCLASSIFIED,
    UNCOVERED,
    StaticError,
    Structure,
    Unit,
    decl_from_json,
    decl_to_json,
    ignored,
    static_errors,
    value_from_json,
    value_to_json,
)
from .tree import MODES, Entry, Tree
from .view import ABSENT, IntegrityFinding, Segment, TreeView
from .writeset import write_set

__all__ = [
    "ABSENT", "DEFAULT_MANIFEST_PATH", "Entry", "GOVERNED_KEY", "GitReadError", "ID_RE", "IntegrityFinding",
    "KINDS", "MODES", "Manifest", "ManifestFailure", "RESIDUAL_SUFFIX", "Region", "SYSTEM_UNITS", "Segment",
    "Span", "StaticError", "Structure", "Term", "Tree", "TreeView", "UNCLASSIFIED", "UNCOVERED", "Unit",
    "decl_from_json", "decl_to_json", "ignored", "parse_manifest", "parse_term", "read_tree", "static_errors",
    "value_from_json", "value_to_json", "write_set",
]
