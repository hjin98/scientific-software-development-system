"""Content Model (Manual §26.1): the manifest, anchors and semantic declarations;
effective scopes resolved against observed bytes; authored relations; revisions
and scope identities. Never stores status or decides which structure is effective.
"""

from .git import GitReadError, ancestry, read_tree
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
from .merge import merge3, merge_text
from .plan import (
    ITEM_KINDS,
    REVIEW,
    SLOTS,
    Check,
    Contract,
    ContractObligation,
    EvidenceVerifier,
    Item,
    ItemFailure,
    ItemPart,
    Plan,
    Ref,
    named_spans,
    parse_item,
    plans,
)
from .resolve import Region, Span
from .spec import (SYSTEM_TIME_CAP_HOURS, Output, SpecDeclaration, SpecFailure, Verdict, canonical_float,
                   canonical_reference, float_of, is_canonical, parse_spec, spec_declaration)
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
from .view import ABSENT, IntegrityFinding, Segment, TreeView, jcs, recorded_identity, scope_identity
from .writeset import write_set

__all__ = [
    "SYSTEM_TIME_CAP_HOURS", "Output", "SpecDeclaration", "SpecFailure", "Verdict", "canonical_float",
    "canonical_reference", "float_of", "is_canonical", "parse_spec", "spec_declaration",
    "ABSENT", "Check", "Contract", "ContractObligation", "DEFAULT_MANIFEST_PATH", "Entry", "EvidenceVerifier",
    "ITEM_KINDS", "Item", "ItemFailure", "ItemPart", "Plan", "REVIEW", "Ref", "SLOTS", "named_spans", "parse_item", "plans", "GOVERNED_KEY", "GitReadError", "ID_RE", "IntegrityFinding",
    "KINDS", "MODES", "Manifest", "ManifestFailure", "RESIDUAL_SUFFIX", "Region", "SYSTEM_UNITS", "Segment",
    "Span", "StaticError", "Structure", "Term", "Tree", "TreeView", "UNCLASSIFIED", "UNCOVERED", "Unit",
    "decl_from_json", "decl_to_json", "ignored", "jcs", "merge3", "merge_text", "parse_manifest", "parse_term", "read_tree", "ancestry", "recorded_identity", "scope_identity", "static_errors",
    "value_from_json", "value_to_json", "write_set",
]
