"""Acceptance group 1 (content half): partition, write set, one representation, normalization, static checks.

Expected values are transcribed by hand from the Stage S §1 cases
(``cases_s5_1.py``, named in each test) and from the Review discriminators the
G2 workplan §5.3 assigns to group 1. The real owner exercised is the Content
Model (``ssds.content``); nothing here imports the Stage S models.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ssds.content import (
    UNCOVERED,
    Entry,
    ManifestFailure,
    Structure,
    TreeView,
    parse_manifest,
    read_tree,
    static_errors,
    write_set,
)

from ._fixtures import git, init_repo, manifest, structure_of, tree, view


def owners(v: TreeView, path: str) -> list[str]:
    """The owner of each line of a governed file."""

    data = v.tree[path].data
    starts = [0] + [i + 1 for i, b in enumerate(data) if b == 0x0A and i + 1 < len(data)]
    return [v.owner_of_line(path, s) for s in starts]


def ws(head, merged) -> set[str]:
    return set(write_set(view(head), view(merged)))


class PartitionCases(unittest.TestCase):
    """cases_s5_1.py partition cases: no byte owned twice; equal or partial overlaps resolve ABSENT."""

    def test_equal_sibling_regions(self) -> None:
        # equal_sibling_regions: a symbol and an anchor of two parts resolve to the same bytes -> all S.~
        text = "x = 0\n# ssds:begin b\ndef a():\n    return 1\n# ssds:end b\ny = 1\n"
        t = tree({"f.py": text}, '''
            [[unit]]
            id = "s"
            kind = "D4"
            role = "composite"
            scope = [{ path = "f.py" }]
            [[unit]]
            id = "a"
            subject = false
            part_of = "s"
            scope = [{ file = "f.py", symbol = "a" }]
            [[unit]]
            id = "b"
            subject = false
            part_of = "s"
            scope = [{ file = "f.py", anchor = "b" }]
        ''')
        v = view(t)
        self.assertIsNone(v.regions["a"])
        self.assertIsNone(v.regions["b"])
        self.assertEqual(set(owners(v, "f.py")), {"s.~"})
        self.assertIn("REGION_OVERLAP", {f.code for f in v.integrity_findings})

    def test_partial_overlap(self) -> None:
        # partial_overlap: partially overlapping parts both resolve to ABSENT -> all S.~
        text = "# Doc\ntext\n## A\na1\n<!-- ssds:begin b -->\na2\n## B\nb1\n<!-- ssds:end b -->\ntail\n"
        t = tree({"f.md": text}, '''
            [[unit]]
            id = "s"
            kind = "D3"
            role = "composite"
            scope = [{ path = "f.md" }]
            [[unit]]
            id = "a"
            subject = false
            part_of = "s"
            scope = [{ file = "f.md", heading = ["Doc", "A"] }]
            [[unit]]
            id = "b"
            subject = false
            part_of = "s"
            scope = [{ file = "f.md", anchor = "b" }]
        ''')
        v = view(t)
        self.assertIsNone(v.regions["a"])
        self.assertIsNone(v.regions["b"])
        self.assertEqual(set(owners(v, "f.md")), {"s.~"})

    def test_nested_non_member(self) -> None:
        # nested_non_member: a top-level unit nested in a composite without membership owns its bytes;
        # the residual receives only bytes still unowned (b46c250 N6)
        text = ("# Top\n<!-- ssds:begin m -->\nm1\nm2\n<!-- ssds:end m -->\n"
                "<!-- ssds:begin bb -->\nb1\nb2\n<!-- ssds:end bb -->\ntail\n")
        t = tree({"f.md": text}, '''
            [[unit]]
            id = "top"
            kind = "D3"
            role = "composite"
            scope = [{ file = "f.md", heading = ["Top"] }]
            [[unit]]
            id = "m"
            subject = false
            part_of = "top"
            scope = [{ file = "f.md", anchor = "m" }]
            [[unit]]
            id = "bb"
            kind = "D3"
            scope = [{ file = "f.md", anchor = "bb" }]
        ''')
        got = owners(view(t), "f.md")
        expected = ["top.~"] * 10
        expected[2:4] = ["m", "m"]
        expected[6:8] = ["bb", "bb"]
        self.assertEqual(got, expected)

    def test_member_outside_composite(self) -> None:
        # member_outside_composite: a member region outside its composite's resolves to ABSENT
        text = "# Top\nt1\nt2\n<!-- ssds:begin m -->\nt3\n# Next\nn1\n<!-- ssds:end m -->\nn2\nn3\n"
        t = tree({"f.md": text}, '''
            [[unit]]
            id = "top"
            kind = "D3"
            role = "composite"
            scope = [{ file = "f.md", heading = ["Top"] }]
            [[unit]]
            id = "m"
            subject = false
            part_of = "top"
            scope = [{ file = "f.md", anchor = "m" }]
        ''')
        v = view(t)
        self.assertIsNone(v.regions["m"])
        self.assertEqual(owners(v, "f.md"), ["top.~"] * 5 + [UNCOVERED] * 5)

    def test_composite_absent_member_survives(self) -> None:
        # composite_absent_member_survives: no cascade; other bytes are uncovered
        text = "x\n<!-- ssds:begin m -->\nm1\nm2\n<!-- ssds:end m -->\ny\nz\n"
        t = tree({"f.md": text}, '''
            [[unit]]
            id = "top"
            kind = "D3"
            role = "composite"
            scope = [{ file = "f.md", heading = ["Missing"] }]
            [[unit]]
            id = "m"
            subject = false
            part_of = "top"
            scope = [{ file = "f.md", anchor = "m" }]
        ''')
        got = owners(view(t), "f.md")
        self.assertEqual(got, [UNCOVERED, UNCOVERED, "m", "m", UNCOVERED, UNCOVERED, UNCOVERED])

    def test_unclassified_owns_only_what_no_other_top_level_unit_contains(self) -> None:
        t = tree({"a/x": "1\n", "b/y": "2\n"}, '''
            [[unit]]
            id = "ssds.unclassified"
            kind = "UNCLASSIFIED"
            scope = [{ prefix = "" }]
            [[unit]]
            id = "a"
            kind = "D4"
            scope = [{ prefix = "a/" }]
        ''')
        v = view(t)
        self.assertEqual(owners(v, "a/x"), ["a"])
        self.assertEqual(owners(v, "b/y"), ["ssds.unclassified"])


THREE_UNITS = '''
    [[unit]]
    id = "numerics"
    kind = "D2"
    scope = [{ prefix = "numerics/" }]
    [[unit]]
    id = "impl"
    kind = "D4"
    scope = [{ prefix = "src/" }]
    [[unit]]
    id = "ssds.manifest"
    kind = "MANIFEST"
    scope = [{ path = ".ssds/manifest.toml" }]
'''


class WriteSetCases(unittest.TestCase):
    """cases_s5_1.py write-set cases: compared at the head, by owned content and declarations, never by position."""

    def test_governed_boundary(self) -> None:
        # governed_boundary: removing an ignore pattern exposes a file under the D2 prefix (cc005db B1 A)
        files = {"numerics/a": "1", "numerics/notes/n": "1", "src/x": "1"}
        head = tree(files, '[governed]\nignore = ["numerics/notes/"]\n' + THREE_UNITS)
        merged = tree(files, THREE_UNITS)
        self.assertEqual(ws(head, merged), {"numerics", "ssds.manifest"})

    def test_concurrent_admission_not_counted(self) -> None:
        # concurrent_admission_not_counted: the head, not the base, is compared with the merged tree (d837363 B4 (a))
        head = tree({"numerics/a": "2", "src/x": "1"}, THREE_UNITS)
        merged = tree({"numerics/a": "2", "src/x": "2"}, THREE_UNITS)
        self.assertEqual(ws(head, merged), {"impl"})

    def test_combination_effect(self) -> None:
        # combination_effect: the request removes an ignore; concurrently admitted work added an ignored file there
        files = {"numerics/a": "1", "numerics/extra/f": "1"}
        head = tree(files, '[governed]\nignore = ["numerics/extra/"]\n' + THREE_UNITS)
        merged = tree(files, THREE_UNITS)
        self.assertEqual(ws(head, merged), {"numerics", "ssds.manifest"})

    def test_new_part_over_existing_bytes(self) -> None:
        # new_part_over_existing_bytes: declaring a new part over a D2 subject's bytes (cc005db B1 B).
        # The case abstracts the manifest; declaring the part also changes the manifest's bytes.
        files = {"numerics/p/f": "1"}
        head = tree(files, THREE_UNITS)
        merged = tree(files, THREE_UNITS.replace('id = "numerics"\n    kind = "D2"',
                                                 'id = "numerics"\n    kind = "D2"\n    role = "composite"') + '''
            [[unit]]
            id = "numerics.p"
            subject = false
            part_of = "numerics"
            scope = [{ prefix = "numerics/p/" }]
        ''')
        self.assertEqual(ws(head, merged) - {"ssds.manifest"}, {"numerics", "numerics.p"})
        self.assertIn("ssds.manifest", ws(head, merged))


SHARED = '''
    [[unit]]
    id = "impl.core"
    kind = "D4"
    scope = [{ file = "core.py", symbol = "write_output" }]
    [[unit]]
    id = "numerics.flux"
    kind = "D2"
    scope = [{ file = "core.py", symbol = "flux_limiter" }]
'''


class WriteSetDiscriminators(unittest.TestCase):
    """27ef339 B2 (A)-(D) and 5c55d4b B2 (A)-(E), the write-set half (the conformance class is Phase E)."""

    def _shared(self, first: str, second: str) -> tuple[str, str]:
        out = "def write_output():\n    return 1\n" if first == "out" else "def flux_limiter():\n    return 2\n"
        flux = "def flux_limiter():\n    return 2\n" if first == "out" else "def write_output():\n    return 1\n"
        return out + "\n" + flux, second

    def test_span_shift_not_a_change_in_both_orders(self) -> None:
        # span_shift_not_a_change and 5c55d4b B2 (A): a D4 edit that shifts the D2 span is not a D2 change
        out = "def write_output():\n    return 1\n"
        longer = "def write_output():\n    a = 1\n    b = 2\n    c = 3\n    return a + b + c\n"
        flux = "def flux_limiter():\n    return 2\n"
        for before, after in ((out + "\n" + flux, longer + "\n" + flux), (flux + "\n" + out, flux + "\n" + longer)):
            with self.subTest(d4_first=before.startswith("def write")):
                self.assertEqual(ws(tree({"core.py": before}, SHARED), tree({"core.py": after}, SHARED)), {"impl.core"})

    def test_same_kind_part_edit_is_only_that_part(self) -> None:
        # 27ef339 B2 (D), 5c55d4b B2 (B): a kern.helper length-changing edit touches neither kern.solve nor kern
        units = '''
            [[unit]]
            id = "kern"
            kind = "D4"
            role = "composite"
            scope = [{ path = "kern.py" }]
            [[unit]]
            id = "kern.helper"
            subject = false
            part_of = "kern"
            scope = [{ file = "kern.py", symbol = "helper" }]
            [[unit]]
            id = "kern.solve"
            subject = false
            part_of = "kern"
            scope = [{ file = "kern.py", symbol = "solve" }]
        '''
        before = "def helper():\n    return 1\n\ndef solve():\n    return helper()\n\nTAIL = 1\n"
        after = "def helper():\n    x = 1\n    y = 2\n    return x + y\n\ndef solve():\n    return helper()\n\nTAIL = 1\n"
        self.assertEqual(ws(tree({"kern.py": before}, units), tree({"kern.py": after}, units)), {"kern.helper"})

    def test_nested_subject_edits_stay_on_their_side(self) -> None:
        # 27ef339 B2 (C), 5c55d4b B2 (C): the composite sentence, in both directions
        units = '''
            [[unit]]
            id = "arch"
            kind = "D3"
            role = "composite"
            scope = [{ path = "doc.md" }]
            [[unit]]
            id = "method"
            kind = "D2"
            part_of = "arch"
            scope = [{ file = "doc.md", heading = ["Doc", "Method"] }]
        '''
        base = "# Doc\nintro\n## Method\nstep one\n## Design\nlayers\n"
        d2_edit = "# Doc\nintro\n## Method\nstep one revised\nstep two\n## Design\nlayers\n"
        d3_edit = "# Doc\nintro, longer\nmore intro\n## Method\nstep one\n## Design\nlayers\n"
        self.assertEqual(ws(tree({"doc.md": base}, units), tree({"doc.md": d2_edit}, units)), {"method"})
        self.assertEqual(ws(tree({"doc.md": base}, units), tree({"doc.md": d3_edit}, units)), {"arch"})

    def test_anchor_move_giving_a_d2_unit_other_bytes_is_in_the_set(self) -> None:
        # 5c55d4b B2 (D), b46c250 N4, f7419d5 N4: a moved anchor gives the D2 unit different bytes
        units = '''
            [[unit]]
            id = "impl.core"
            kind = "D4"
            scope = [{ file = "core.py", anchor = "impl" }]
            [[unit]]
            id = "numerics.flux"
            kind = "D2"
            scope = [{ file = "core.py", anchor = "flux" }]
        '''
        before = "# ssds:begin impl\na = 1\n# ssds:end impl\n# ssds:begin flux\nf = 1\ng = 2\n# ssds:end flux\n"
        after = "# ssds:begin impl\na = 1\n# ssds:end impl\n# ssds:begin flux\nf = 1\n# ssds:end flux\ng = 2\n"
        self.assertIn("numerics.flux", ws(tree({"core.py": before}, units), tree({"core.py": after}, units)))

    def test_region_criterion_isolated_from_owned_content(self) -> None:
        # b46c250 N4 / f7419d5 N4: the region grows over bytes another unit owns; owned content is unchanged
        units = '''
            [[unit]]
            id = "outer"
            kind = "D2"
            scope = [{ file = "m.py", anchor = "outer" }]
            [[unit]]
            id = "inner"
            kind = "D4"
            scope = [{ file = "m.py", anchor = "inner" }]
        '''
        before = "# ssds:begin outer\no1 = 1\n# ssds:end outer\n# ssds:begin inner\ni1 = 2\n# ssds:end inner\nz = 3\n"
        after = "# ssds:begin outer\no1 = 1\n# ssds:begin inner\ni1 = 2\n# ssds:end inner\n# ssds:end outer\nz = 3\n"
        head, merged = tree({"m.py": before}, units), tree({"m.py": after}, units)
        self.assertEqual(view(head).owned["outer"], view(merged).owned["outer"], "owned content is unchanged")
        self.assertEqual(ws(head, merged), {"outer"})

    def test_mode_change_reaches_every_unit_of_the_file(self) -> None:
        # 27ef339 B2 (B), 5c55d4b B2 (E)
        text = "def write_output():\n    return 1\n\ndef flux_limiter():\n    return 2\n"
        head = tree({"core.py": Entry("100644", text.encode())}, SHARED)
        merged = tree({"core.py": Entry("100755", text.encode())}, SHARED)
        self.assertEqual(ws(head, merged), {"impl.core", "numerics.flux"})


WHOLE = '''
    [[unit]]
    id = "data"
    kind = "D4"
    scope = [{ path = "data/value.bin" }]
'''


def rev_of(entry: Entry, units: str = WHOLE, path: str = "data/value.bin", uid: str = "data") -> str:
    return view(tree({path: entry}, units)).rev(uid)


class OneRepresentation(unittest.TestCase):
    """3540d98 B1, e2154ac B1, e9e6e9f B1: identity is the Git tree entry, exactly (Manual §1.5)."""

    def test_every_representation_dimension_changes_identity(self) -> None:
        base = rev_of(Entry("100644", b"\x0d"))
        self.assertNotEqual(base, rev_of(Entry("100644", b"\x0a")), "a binary byte change (trajectory A)")
        self.assertNotEqual(rev_of(Entry("100644", b"a\r\n")), rev_of(Entry("100644", b"a\n")), "line endings")
        self.assertNotEqual(rev_of(Entry("100644", b"x")), rev_of(Entry("100755", b"x")), "the executable bit")
        self.assertNotEqual(rev_of(Entry("100644", b"payload.bin")), rev_of(Entry("120000", b"payload.bin")),
                            "a regular file replaced by a link with the same bytes (trajectory B)")
        self.assertNotEqual(rev_of(Entry("160000", b"a" * 40)), rev_of(Entry("160000", b"b" * 40)), "a gitlink's commit")

    def test_reading_a_commit_applies_no_attribute_filter_or_line_ending_conversion(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp) / "repo")
            git(repo, "config", "core.autocrlf", "true")
            (repo / ".gitattributes").write_text("*.txt text eol=crlf\n*.bin filter=lfs diff=lfs merge=lfs -text\n")
            (repo / "a.txt").write_bytes(b"one\ntwo\n")
            pointer = b"version https://git-lfs.github.com/spec/v1\noid sha256:" + b"0" * 64 + b"\nsize 3\n"
            (repo / "big.bin").write_bytes(pointer)
            (repo / "run.sh").write_bytes(b"#!/bin/sh\n")
            (repo / "run.sh").chmod(0o755)
            (repo / "link").symlink_to("a.txt")
            git(repo, "add", "-A")
            git(repo, "update-index", "--add", "--cacheinfo", f"160000,{'c' * 40},sub")
            git(repo, "commit", "--quiet", "-m", "fixture")
            head = git(repo, "rev-parse", "HEAD")
            t = read_tree(repo, head)
            stored = git(repo, "cat-file", "-p", f"{head}:a.txt").encode() + b"\n"
            self.assertEqual(t["a.txt"].data, stored, "the stored blob, not a checkout conversion")
            self.assertNotIn(b"\r", t["a.txt"].data)
            self.assertEqual(t["big.bin"].data, pointer, "an LFS pointer is read as its pointer bytes")
            self.assertEqual((t["run.sh"].mode, t["link"].mode, t["link"].data), ("100755", "120000", b"a.txt"))
            self.assertEqual((t["sub"].mode, t["sub"].data), ("160000", b"c" * 40))
            with self.assertRaises(ValueError):
                read_tree(repo, "main")


class Normalization(unittest.TestCase):
    """The one normalization: classified anchor comment lines leave identity (Manual §1.5), and nothing else does."""

    UNIT = '''
        [[unit]]
        id = "mod"
        kind = "D4"
        scope = [{ path = "mod.py" }]
    '''

    def rev(self, text: str, path: str = "mod.py") -> str:
        return rev_of(Entry("100644", text.encode()), self.UNIT.replace("mod.py", path), path, "mod")

    def test_adding_or_moving_anchors_in_a_classified_type_keeps_identity(self) -> None:
        plain = self.rev("a = 1\nb = 2\n")
        self.assertEqual(plain, self.rev("# ssds:begin x\na = 1\n# ssds:end x\nb = 2\n"))
        self.assertEqual(plain, self.rev("a = 1\n# ssds:begin x\nb = 2\n# ssds:end x\n"))

    def test_an_anchor_looking_data_line_is_neither_anchor_nor_removed(self) -> None:
        data = 's = """\n# ssds:begin x\n"""\n'
        self.assertNotEqual(self.rev('s = """\n"""\n'), self.rev(data))
        units = self.UNIT + '''
            [[unit]]
            id = "x"
            kind = "D4"
            subject = true
            scope = [{ file = "mod.py", anchor = "x" }]
        '''
        self.assertIsNone(view(tree({"mod.py": data}, units)).term_resolutions["x"][0])

    def test_without_a_classifier_anchors_are_recognized_but_kept_in_identity(self) -> None:
        self.assertNotEqual(self.rev("a = 1\n", "conf.toml"), self.rev("# ssds:begin x\na = 1\n# ssds:end x\n", "conf.toml"))
        units = '''
            [[unit]]
            id = "x"
            kind = "D4"
            scope = [{ file = "conf.toml", anchor = "x" }]
        '''
        v = view(tree({"conf.toml": "# ssds:begin x\na = 1\n# ssds:end x\n"}, units))
        self.assertIsNotNone(v.term_resolutions["x"][0])

    def test_trailing_whitespace_and_encoding_are_content(self) -> None:
        self.assertNotEqual(self.rev("a = 1\n"), self.rev("a = 1 \n"))

    def test_scope_identity_ignores_bytes_and_parts(self) -> None:
        units = '''
            [[unit]]
            id = "s"
            kind = "D2"
            role = "composite"
            scope = [{ path = "s.md" }]
        '''
        refined = units + '''
            [[unit]]
            id = "s.part"
            subject = false
            part_of = "s"
            scope = [{ file = "s.md", heading = ["A"] }]
        '''
        a = view(tree({"s.md": "# A\nx\n"}, units))
        b = view(tree({"s.md": "# A\ny\n"}, refined))
        self.assertEqual(a.scope_id("s"), b.scope_id("s"))
        self.assertEqual(view(tree({"s.md": "# A\nx\n"}, refined)).rev("s"), a.rev("s"),
                         "a byte-preserving refinement keeps the revision")


class SemanticDeclarations(unittest.TestCase):
    def test_semantic_declarations_are_part_of_the_revision(self) -> None:
        units = '''
            [[unit]]
            id = "a"
            kind = "D2"
            scope = [{ path = "a.py" }]
        '''
        plain = view(tree({"a.py": "x = 1\n"}, units))
        inline = view(tree({"a.py": "# ssds:rel USES_DEFINITION physics.units\nx = 1\n"}, units))
        listed = view(tree({"a.py": "x = 1\n"}, units + '[unit.semantic]\ndefines = ["a.thing"]\n'))
        self.assertEqual(plain.content("a"), listed.content("a"))
        self.assertNotEqual(plain.rev("a"), listed.rev("a"))
        self.assertNotEqual(plain.rev("a"), inline.rev("a"))
        self.assertEqual(inline.authored_relations(), (("a", "USES_DEFINITION", "physics.units", {}),))


class StaticChecks(unittest.TestCase):
    def errors(self, units: str) -> set[str]:
        return {e.code for e in static_errors(Structure(parse_manifest(manifest(units)).decl))}

    def test_each_static_rule(self) -> None:
        cases = {
            "SIBLING_OVERLAP": '[[unit]]\nid = "a"\nkind = "D4"\nscope = [{ prefix = "src/" }]\n'
                               '[[unit]]\nid = "b"\nkind = "D4"\nscope = [{ prefix = "src/x/" }]\n',
            "KIND_ON_PART": '[[unit]]\nid = "c"\nkind = "D4"\nrole = "composite"\nscope = [{ prefix = "c/" }]\n'
                            '[[unit]]\nid = "p"\nkind = "D4"\nsubject = false\npart_of = "c"\nscope = [{ prefix = "c/p/" }]\n',
            "KIND_REQUIRED": '[[unit]]\nid = "a"\nscope = [{ prefix = "a/" }]\n',
            "CONTAINMENT": '[[unit]]\nid = "c"\nkind = "D4"\nrole = "composite"\nscope = [{ prefix = "c/" }]\n'
                           '[[unit]]\nid = "p"\nsubject = false\npart_of = "c"\nscope = [{ prefix = "d/" }]\n',
            "RESERVED_IDENTITY": '[[unit]]\nid = "ssds.mine"\nkind = "D4"\nscope = [{ prefix = "a/" }]\n',
            "RENAMED_FROM_CYCLE": '[[unit]]\nid = "a"\nkind = "D4"\nscope = [{ prefix = "a/" }]\nrenamed_from = ["b"]\n'
                                  '[[unit]]\nid = "b"\nkind = "D4"\nscope = [{ prefix = "b/" }]\nrenamed_from = ["a"]\n',
            "SYMBOL_ANALYZER": '[[unit]]\nid = "a"\nkind = "D4"\nscope = [{ file = "a.rs", symbol = "f" }]\n',
            "EMPTY_PREFIX": '[[unit]]\nid = "a"\nkind = "D4"\nscope = [{ prefix = "" }]\n',
            "MEMBERSHIP": '[[unit]]\nid = "p"\nsubject = false\npart_of = "missing"\nscope = [{ prefix = "p/" }]\n',
        }
        for code, units in cases.items():
            with self.subTest(code=code):
                self.assertIn(code, self.errors(units))
        whole_and_span = ('[[unit]]\nid = "a"\nkind = "D4"\nscope = [{ path = "f.md" }]\n'
                          '[[unit]]\nid = "b"\nkind = "D4"\nscope = [{ file = "f.md", heading = ["A"] }]\n')
        self.assertIn("SIBLING_OVERLAP", self.errors(whole_and_span))
        legal = SHARED
        self.assertEqual(self.errors(legal), set(), "two symbols on one file whose names do not nest")

    def test_new_terms_must_resolve(self) -> None:
        units = '[[unit]]\nid = "a"\nkind = "D4"\nscope = [{ file = "a.md", heading = ["Gone"] }]\n'
        v = view(tree({"a.md": "# Here\n"}, units))
        self.assertEqual(v.unresolved_declared_terms(None), ("a",))
        self.assertEqual(v.unresolved_declared_terms(v.structure), (), "a term already admitted may go ABSENT")

    def test_unparsable_and_ungrammatical_manifests_fail_closed(self) -> None:
        self.assertEqual(parse_manifest(b"schema = 1\n[[unit]\n").reason, "PARSE")
        failure = parse_manifest(manifest('[[unit]]\nid = "a"\nkind = "D4"\nscope = []\nowner = "x"\n'))
        self.assertIsInstance(failure, ManifestFailure)
        self.assertEqual(failure.reason, "GRAMMAR")
        v = TreeView(tree({".ssds/manifest.toml": b"schema = [\n"}), structure_of(tree({}, "")))
        self.assertIn("MANIFEST_UNPARSED", {f.code for f in v.integrity_findings})



class AnalyzedSourceWarnings(unittest.TestCase):
    """An analyzed file's own compile warnings are its content: they never reach the operator."""

    SOURCE = b'import re\nPATTERN = "\\w+"\n\ndef check():\n    return re.compile(PATTERN)\n'

    def test_parsing_emits_no_warning_and_still_analyzes(self) -> None:
        import ast
        import warnings

        from ssds.analyzers import python

        with warnings.catch_warnings(record=True) as raw:
            warnings.simplefilter("always")
            ast.parse(self.SOURCE)
        self.assertTrue(raw, "the fixture's escape sequence does warn when parsed bare")
        with warnings.catch_warnings(record=True) as seen:
            warnings.simplefilter("always")
            names = [d.qualname for d in python.definitions(self.SOURCE)]
            imports = python.imports("m.py", self.SOURCE)
        self.assertEqual(seen, [])
        self.assertIn("check", names)
        self.assertEqual(imports.modules, ("re",))

if __name__ == "__main__":
    unittest.main()
