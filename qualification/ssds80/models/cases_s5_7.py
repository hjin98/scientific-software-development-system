"""S5 catalogue §7 cases: merge, roles and prospective acceptance (Manual §7.2, §7.3, §7.6; R12)."""

from __future__ import annotations

from cases_s5_1 import S5Case
from frames import counts_for_tenure, counts_lineage, merge3, role

B = {"a.py": ("x", "y"), "bin": b"1", "m.toml": ("k=1",)}
CASES = [
    S5Case("one_side_change", "a path changed on one side takes that side", ({"a.py": ("x", "Y"), "bin": b"1", "m.toml": ("k=1",)}, None),
           {"settled": lambda: merge3(B, B, dict(B, **{"a.py": ("x", "Y")}))}),
    S5Case("disjoint_lines_merge", "different lines changed on both sides merge cleanly", ({"a.py": ("X", "Y"), "bin": b"1", "m.toml": ("k=1",)}, None),
           {"settled": lambda: merge3(B, dict(B, **{"a.py": ("X", "y")}), dict(B, **{"a.py": ("x", "Y")}))}),
    S5Case("overlapping_hunk_conflict", "the same line changed differently on both sides: no frame (K3)", True,
           {"settled": lambda: merge3(B, dict(B, **{"a.py": ("x", "Y1")}), dict(B, **{"a.py": ("x", "Y2")}))[1] is not None}),
    S5Case("binary_both_sides_conflict", "binary content changed on both sides is a conflict", True,
           {"settled": lambda: merge3(B, dict(B, bin=b"2"), dict(B, bin=b"3"))[1] is not None}),
    S5Case("declaration_key_conflict",
           "a declaration key changed to different values on both sides is a conflict even where the manifest "
           "lines would merge", True,
           {"settled": lambda: merge3({"key:scope": ("a",)}, {"key:scope": ("b",)}, {"key:scope": ("c",)},
                                      frozenset({"key:scope"}))[1] is not None}),
    S5Case("roles", "before-image, output and context are fixed by B, C and the entry",
           ("before-image", "output", "context", "never"),
           {"settled": lambda: (role("u", 1, {"u": 1, "w": 5}, {"u": 2, "w": 5}),
                                role("u", 2, {"u": 1, "w": 5}, {"u": 2, "w": 5}),
                                role("w", 5, {"u": 1, "w": 5}, {"u": 2, "w": 5}),
                                role("u", 9, {"u": 1, "w": 5}, {"u": 2, "w": 5}))}),
    S5Case("later_iteration_needs_its_own_acceptance",
           "a prospective acceptance made in iteration 1's frame does not count for iteration 2's integration "
           "(R12, SD-26; f22b4dc B1)", False,
           {"settled": lambda: counts_for_tenure({"enactment": "e1", "obligation": "o", "structure": "S", "basis_holds": True},
                                                 {"enactment": "e2", "obligation": "o", "structure": "S"}, False),
            "lineage": lambda: counts_lineage({"enactment": "e1", "obligation": "o", "structure": "S", "basis_holds": True},
                                              {"enactment": "e2", "obligation": "o", "structure": "S"}, False)},
           {"lineage": "f22b4dc B1"}),
    S5Case("same_enactment_counts_once",
           "a prospective acceptance counts for its own enactment's integration, and for at most one tenure",
           (True, False),
           {"settled": lambda: (counts_for_tenure({"enactment": "e1", "structure": "S", "basis_holds": True},
                                                  {"enactment": "e1", "structure": "S"}, False),
                                counts_for_tenure({"enactment": "e1", "structure": "S", "basis_holds": True},
                                                  {"enactment": "e1", "structure": "S"}, True))}),
    S5Case("structure_changed_does_not_count", "a rebase that changes the proposed structure needs a new acceptance", False,
           {"settled": lambda: counts_for_tenure({"enactment": "e1", "structure": "S", "basis_holds": True},
                                                 {"enactment": "e1", "structure": "S2"}, False)}),
]
