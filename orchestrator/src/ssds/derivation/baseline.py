"""``Σ_0`` from a baseline tree: the structure a genesis records, with its static checks (catalogue §1.9, §19.9).

Admission builds a genesis in an isolated workspace and must validate every
declaration before the human gate. The structure is S0's to read, so the
checks live here and Admission imports them; the tree is supplied, never read.
"""

from __future__ import annotations

from dataclasses import dataclass

from ssds.content import SYSTEM_UNITS, UNCLASSIFIED, Manifest, Structure, Tree, TreeView, decl_from_json, decl_to_json, static_errors

from .history import manifest_decl
from .s0 import StructureFacts


@dataclass(frozen=True)
class BaselineStructure:
    structure: dict | None  # Σ_0 in the ledger's JSON form; None when it cannot be built
    subjects: tuple[str, ...]
    problems: tuple[str, ...]  # refuse the genesis
    findings: tuple[str, ...]  # ordinary S0 findings reported with it (relations, cycles, single definer)


def baseline_structure(tree: Tree, manifest_path: str) -> BaselineStructure:
    view = TreeView(tree, Structure({}), manifest_path)
    manifest = view.manifest
    if manifest is None:
        return BaselineStructure(None, (), (f"no unit manifest at {manifest_path} in the baseline tree",), ())
    if not isinstance(manifest, Manifest):
        reason, detail = manifest
        return BaselineStructure(None, (), (f"the unit manifest does not parse ({reason}): {detail}",), ())
    structure = Structure(dict(manifest.decl))
    errors = static_errors(structure)
    problems = tuple(f"{e.code} {e.unit}: {e.detail}" for e in errors)
    static = {(e.code, e.unit, e.detail) for e in errors}
    subjects = tuple(sorted(u for u, unit in structure.units.items() if unit.subject))
    declared = TreeView(tree, structure, manifest_path)
    # §1.9: at genesis every term is newly declared, so each one naming a file or a span in one must
    # resolve to a present file (possibly empty) or a found span; prefix terms are exempt.
    for uid in sorted(structure.units):
        for term in structure.units[uid].scope:
            if term.kind != "prefix" and declared.term_region(term) is None:
                problems += (f"TERM_ABSENT {uid}: {term.to_json()} resolves to nothing in the baseline tree",)
    problems += genesis_structure_problems(structure)
    facts = StructureFacts(declared, manifest_decl(view))
    findings = tuple(f"{d.code} {d.unit}: {d.detail}" for d in facts.defects if (d.code, d.unit, d.detail) not in static)
    return BaselineStructure(decl_to_json(structure.decl), subjects, problems, findings)


def genesis_structure_problems(structure: Structure | dict) -> tuple[str, ...]:
    """A genesis structure declares the reserved leaves of §1.8, ``ssds.unclassified`` with the empty prefix,
    so every governed byte has an owner and every change is in some effective unit's write set (Manual §1.8,
    §1.9 as amended by A9, SD-61; plan reading F18). Takes a ``Structure`` or the ledger's JSON form of one."""

    if isinstance(structure, dict):
        structure = Structure(decl_from_json(structure))
    return tuple(f"RESERVED_LEAF {unit}: {detail}" for unit, detail in reserved_leaf_problems(structure))


def reserved_leaf_problems(structure: Structure) -> list[tuple[str, str]]:
    """The reserved leaves of §1.8, each declared with its reserved kind, ``ssds.unclassified`` on the empty
    prefix (Manual §1.8, §1.9, A9; reading F18). The one owner genesis, Admission and frames read."""

    out = []
    for uid, kind in sorted(SYSTEM_UNITS.items()):
        unit = structure.units.get(uid)
        if unit is None:
            out.append((uid, f"{uid} is not declared (§1.8)"))
            continue
        if unit.declared_kind != kind:
            out.append((uid, f"{uid} has kind {kind}"))
        # a reserved leaf: a top-level leaf subject with no members, so its bytes stay its own (review 2aadf33 B5)
        if unit.role != "leaf" or unit.part_of is not None or not unit.subject:  # only a composite has members
            out.append((uid, f"{uid} is a top-level leaf subject with no members (§1.8)"))
    unclassified = structure.units.get(UNCLASSIFIED)
    if unclassified is not None and not any(t.kind == "prefix" and t.file == "" for t in unclassified.scope):
        out.append((UNCLASSIFIED, f"{UNCLASSIFIED} is declared with the empty prefix (A9)"))
    return out


__all__ = ["BaselineStructure", "baseline_structure", "genesis_structure_problems", "reserved_leaf_problems"]
