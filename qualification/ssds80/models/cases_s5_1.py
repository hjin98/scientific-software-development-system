"""S5 catalogue §1 cases: partition by construction and the effect-keyed write set.

Expectations are written from the accepted Manual §1.2 and §1.4 (refinement R5, SD-14): no byte is
owned twice; equal or partially overlapping regions of units not nested by membership resolve to
ABSENT; innermost ownership comes before residual and uncovered; the write set is computed at the head
where the check runs, from the current observed tree to the merged tree, by owned content and
declarations, never by position. `refutes` names the reading each case was raised against.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from structure import (PARTITION_READINGS, Unit, WUnit, span_write_set, write_set_changed_paths,
                       write_set_settled)


@dataclass
class S5Case:
    name: str
    why: str
    expected: object
    compute: dict                      # reading -> zero-argument callable giving the result
    refutes: dict = field(default_factory=dict)


def _partition(units, size):
    u = {x.name: x for x in units}
    return {r: (lambda f=f: f(u, size)) for r, f in PARTITION_READINGS.items()}


S = Unit("S", (0, 10), composite=True)
CASES = [
    S5Case("equal_sibling_regions",
           "a symbol term and an anchor term of two parts resolve to the same bytes: both ABSENT, the "
           "bytes fall to the subject's residual (3540d98 B4)",
           ["S.~"] * 10,
           _partition([S, Unit("a", (2, 6), "S"), Unit("b", (2, 6), "S")], 10),
           {"partial_only": "3540d98 B4"}),
    S5Case("partial_overlap", "partially overlapping parts both resolve to ABSENT", ["S.~"] * 10,
           _partition([S, Unit("a", (2, 6), "S"), Unit("b", (4, 8), "S")], 10)),
    S5Case("nested_non_member",
           "a top-level unit nested in a composite's region without membership owns its bytes; the "
           "residual receives only bytes still unowned (b46c250 N6)",
           ["A.~", "m", "m", "A.~", "A.~", "B", "B", "A.~", "A.~", "A.~"],
           _partition([Unit("A", (0, 10), composite=True), Unit("m", (1, 3), "A"), Unit("B", (5, 7))], 10),
           {"member_residual": "b46c250 N6"}),
    S5Case("member_outside_composite", "a member region outside its composite's resolves to ABSENT",
           ["A.~"] * 5 + ["UNCOVERED"] * 5,
           _partition([Unit("A", (0, 5), composite=True), Unit("m", (4, 8), "A")], 10)),
    S5Case("composite_absent_member_survives",
           "no cascade: a member keeps its resolution when its composite is ABSENT; other bytes are uncovered",
           ["UNCOVERED", "UNCOVERED", "m", "m"] + ["UNCOVERED"] * 6,
           _partition([Unit("A", None, composite=True), Unit("m", (2, 4), "A")], 10)),
]

D2 = WUnit("numerics", "D2", "numerics/")
D4 = WUnit("impl", "D4", "src/")
MAN = WUnit("ssds.manifest", "MANIFEST", ".ssds/")
U = (D2, D4, MAN)


def _ws(head, hi, merged, mi, base=None, bi=None, candidate=None, uh=U, um=U):
    out = {"settled": lambda: write_set_settled(head, frozenset(hi), merged, frozenset(mi), uh, um)}
    if base is not None:
        out["base_to_merged"] = lambda: write_set_settled(base, frozenset(bi), merged, frozenset(mi), uh, um)
    if candidate is not None:
        out["changed_paths"] = lambda: write_set_changed_paths(base, candidate, uh, frozenset(bi))
    return out


_T0 = {"numerics/a": 1, "numerics/notes/n": 1, "src/x": 1, ".ssds/manifest": 1}
CASES += [
    S5Case("governed_boundary",
           "removing an ignore pattern exposes a file under the D2 prefix: the D2 unit is in the write "
           "set though no D2 byte changed (cc005db B1 A)",
           {"numerics", "ssds.manifest"},
           _ws(_T0, {"numerics/notes/"}, dict(_T0, **{".ssds/manifest": 2}), set(),
               base=_T0, bi={"numerics/notes/"}, candidate=dict(_T0, **{".ssds/manifest": 2})),
           {"changed_paths": "cc005db B1"}),
    S5Case("concurrent_admission_not_counted",
           "a D2 change admitted since the base is not the request's: the write set compares the head, "
           "not the base, with the merged tree (d837363 B4 (a))",
           {"impl"},
           _ws({"numerics/a": 2, "src/x": 1}, set(), {"numerics/a": 2, "src/x": 2}, set(),
               base={"numerics/a": 1, "src/x": 1}, bi=set()),
           {"base_to_merged": "d837363 B4 (a)"}),
    S5Case("combination_effect",
           "the request removes an ignore pattern; concurrently admitted work added an ignored file "
           "there: the combination reaches the D2 unit (d837363 B4, cc005db B1 split)",
           {"numerics", "ssds.manifest"},
           _ws({"numerics/a": 1, "numerics/extra/f": 1, ".ssds/manifest": 1}, {"numerics/extra/"},
               {"numerics/a": 1, "numerics/extra/f": 1, ".ssds/manifest": 2}, set(),
               base={"numerics/a": 1, ".ssds/manifest": 1}, bi={"numerics/extra/"},
               candidate={"numerics/a": 1, ".ssds/manifest": 2}),
           {"changed_paths": "d837363 B4"}),
    S5Case("new_part_over_existing_bytes",
           "declaring a new part over a D2 subject's bytes changes that subject's ownership: both are in "
           "the write set (cc005db B1 B)",
           {"numerics", "numerics.p"},
           _ws({"numerics/p/f": 1}, set(), {"numerics/p/f": 1}, set(), base={"numerics/p/f": 1}, bi=set(),
               candidate={"numerics/p/f": 1}, um=(D2, D4, MAN, WUnit("numerics.p", "D2", "numerics/p/"))),
           {"changed_paths": "cc005db B1"}),
    S5Case("span_shift_not_a_change",
           "a D4 edit lengthens its span and shifts the D2 span after it in the same file; the D2 span's "
           "content is unchanged, so it is not in the write set (5c55d4b B2)",
           {"impl.core"},
           {"settled": lambda: span_write_set((("impl.core", "AAAA"), ("numerics.flux", "FFFF")),
                                              (("impl.core", "AAAAAAA"), ("numerics.flux", "FFFF")), False),
            "positions": lambda: span_write_set((("impl.core", "AAAA"), ("numerics.flux", "FFFF")),
                                                (("impl.core", "AAAAAAA"), ("numerics.flux", "FFFF")), True)},
           {"positions": "5c55d4b B2"}),
]
