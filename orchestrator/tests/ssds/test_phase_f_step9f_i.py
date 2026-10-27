"""Phase F step 9f-i: materializing a tree for a designated runner (Manual §1.5, §26.3; plan §3.6, readings F2, F104).

Group 1's runner half: a CRLF file, an executable, a symbolic link, a gitlink, an LFS pointer and a submodule are
materialized under ``runs/`` exactly as the tree holds them, and read back byte-exact. A ``.git`` component in any
of Git's spellings, colliding paths and a link target holding a NUL are refused (a path that is not UTF-8 is
refused by ``Tree`` itself), as is a
link in the run's own path. Removal never descends through a link. Expected values are the tree's own entries (§1.5:
"no line-ending, filter or sparse-checkout transformation").
"""

from __future__ import annotations

import os
import stat
import tempfile
import unittest
from pathlib import Path

from ssds.content import Entry, Tree
from ssds.dispatcher.home import DispatcherHome
from ssds.dispatcher.runner import MaterializeRefused, Workspaces, reads_as_git
from ssds.ledger.qualification import HomeRefused

LFS = b"version https://git-lfs.github.com/spec/v1\noid sha256:" + b"a" * 64 + b"\nsize 12\n"
GROUP1 = Tree({
    "crlf.txt": Entry("100644", b"one\r\ntwo\r\n"),
    "bin/run.sh": Entry("100755", b"#!/bin/sh\necho ok\n"),
    "link": Entry("120000", b"crlf.txt"),
    "outside": Entry("120000", b"/etc/hostname"),
    "vendor/lib": Entry("160000", b"0123456789abcdef0123456789abcdef01234567"),
    ".gitmodules": Entry("100644", b'[submodule "lib"]\n\tpath = vendor/lib\n\turl = https://example.invalid/lib\n'),
    "data/model.bin": Entry("100644", LFS),
    "empty": Entry("100644", b""),
    "anchored.md": Entry("100644", b"<!-- ssds:anchor intro -->\n# Intro\n"),
})


class Fixture(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.home = DispatcherHome(Path(self._tmp.name) / "home")
        self.workspaces = Workspaces(self.home)


class Materialized(Fixture):
    def test_group_1_runner_half_byte_exact(self) -> None:
        old = os.umask(0o077)  # the run's umask never applies to an entry's mode
        try:
            ws = self.workspaces.materialize("demo", GROUP1)
        finally:
            os.umask(old)
        root = ws.root
        self.assertEqual(root, self.home.root / "runs" / "demo" / ws.run_id / "tree")
        self.assertEqual((root / "crlf.txt").read_bytes(), b"one\r\ntwo\r\n", "no end-of-line conversion")
        self.assertEqual(stat.S_IMODE(os.lstat(root / "bin" / "run.sh").st_mode), 0o755)
        self.assertEqual(stat.S_IMODE(os.lstat(root / "crlf.txt").st_mode), 0o644)
        self.assertEqual(os.readlink(root / "link"), "crlf.txt")
        self.assertEqual(os.readlink(root / "outside"), "/etc/hostname", "materialized, never resolved")
        self.assertTrue((root / "vendor" / "lib").is_dir() and not os.listdir(root / "vendor" / "lib"),
                        "a gitlink is Git's uninitialized submodule")
        self.assertEqual((root / "data" / "model.bin").read_bytes(), LFS, "the pointer, never smudged")
        self.assertEqual((root / "empty").read_bytes(), b"")
        self.assertEqual((root / "anchored.md").read_bytes(), GROUP1["anchored.md"].data, "the anchor line kept")
        self.workspaces.verify(ws, GROUP1)

    def test_each_run_is_its_own(self) -> None:
        a, b = self.workspaces.materialize("demo", GROUP1), self.workspaces.materialize("demo", GROUP1)
        self.assertNotEqual(a.run_id, b.run_id)

    def test_a_write_that_went_wrong_refuses_the_run(self) -> None:
        """The read-back is checked after writing (F104), so a filesystem that stored other bytes is caught."""

        from unittest import mock

        from ssds.dispatcher import runner

        def short(descriptor: int, data: bytes) -> None:
            os.write(descriptor, data[:-1])

        with mock.patch.object(runner, "write_all", short), self.assertRaises(MaterializeRefused):
            self.workspaces.materialize("demo", GROUP1)
        self.assertEqual(os.listdir(self.home.root / "runs" / "demo"), [], "nothing left behind")

    def test_a_file_swapped_after_it_was_examined(self) -> None:
        """Review of dad8e4cd, note 1: the file opened must be the one ``lstat`` examined."""

        from unittest import mock

        from ssds.dispatcher import runner

        ws = self.workspaces.materialize("demo", GROUP1)
        real = os.lstat

        def swapped(name, *, dir_fd=None):
            info = real(name, dir_fd=dir_fd)
            if name == "empty":  # as if another inode stood there when it was examined
                return os.stat_result((info.st_mode, info.st_ino + 1, *tuple(info)[2:10]))
            return info

        with mock.patch.object(runner.os, "lstat", swapped), self.assertRaisesRegex(MaterializeRefused, "replaced"):
            self.workspaces.verify(ws, GROUP1)

    def test_a_cleanup_that_fails_is_never_silent(self) -> None:
        """Review of dad8e4cd, note 3: the refusal carries the cleanup failure, and is not masked by it."""

        from unittest import mock

        from ssds.dispatcher import runner

        def failing(path, *, dir_fd=None, onexc=None):
            onexc(os.rmdir, path, OSError("busy"))

        failing.avoids_symlink_attacks = True
        with mock.patch.object(runner, "write_all", lambda descriptor, data: os.write(descriptor, data[:-1])), \
                mock.patch.object(runner.shutil, "rmtree", failing), \
                self.assertRaises(MaterializeRefused) as caught:
            self.workspaces.materialize("demo", GROUP1)
        self.assertTrue(any("not fully removed" in note for note in getattr(caught.exception, "__notes__", [])))

    def test_a_changed_workspace_fails_verification(self) -> None:
        ws = self.workspaces.materialize("demo", GROUP1)
        for change in (lambda r: (r / "crlf.txt").write_bytes(b"one\ntwo\n"),
                       lambda r: os.chmod(r / "bin" / "run.sh", 0o644),
                       lambda r: (r / "extra").write_bytes(b"x"),
                       lambda r: (r / "vendor" / "lib" / "x").write_bytes(b"x"),
                       lambda r: (os.unlink(r / "link"), os.symlink("elsewhere", r / "link")),
                       # a second name for a file: its inode is shared outside (review of dad8e4cd, note 2)
                       lambda r: os.link(r / "empty", Path(self._tmp.name) / f"hard-{os.urandom(4).hex()}")):
            with self.subTest(change=change):
                fresh = self.workspaces.materialize("demo", GROUP1)
                change(fresh.root)
                with self.assertRaises(MaterializeRefused):
                    self.workspaces.verify(fresh, GROUP1)
        self.workspaces.verify(ws, GROUP1)


class Refused(Fixture):
    def test_a_git_component_in_any_spelling(self) -> None:
        for name in (".git", ".GIT", ".git.", ".git ", ".g‌it", ".git::$INDEX_ALLOCATION", "GIT~1", "git~1"):
            with self.subTest(name=name):
                self.assertTrue(reads_as_git(name))
                with self.assertRaises(MaterializeRefused):
                    self.workspaces.materialize("demo", Tree({f"a/{name}/HEAD": b"ref: x\n"}))
        for name in (".gitignore", "git", ".github", ".git2"):
            self.assertFalse(reads_as_git(name), name)
        self.assertFalse((self.home.root / "runs" / "demo").exists() and os.listdir(self.home.root / "runs" / "demo"),
                         "a refusal leaves nothing")

    def test_colliding_paths(self) -> None:
        tree = Tree({"a": Entry("100644", b"file"), "a/b": Entry("100644", b"inner")})
        with self.assertRaises(MaterializeRefused):
            self.workspaces.materialize("demo", tree)
        self.assertEqual(os.listdir(self.home.root / "runs" / "demo"), [], "nothing left behind")

    def test_a_path_not_utf8_and_a_nul_link_target(self) -> None:
        with self.assertRaises(UnicodeEncodeError):  # the content owner refuses it: no Tree holds one
            Tree({"bad\udcff": b"x"})
        with self.assertRaises(MaterializeRefused):
            self.workspaces.materialize("demo", Tree({"l": Entry("120000", b"a\0b")}))

    def test_a_mapping_cannot_climb_out(self) -> None:
        """Review of dad8e4cd, B1: containment is the materializer's, whatever mapping it is handed."""

        from types import SimpleNamespace

        entry = SimpleNamespace(mode="100644", data=b"x")
        for path in ("../x", "../../escaped.txt", "a/./b", "a//b", "a/../../b", "/abs", "", "a\\b", "a\0b"):
            with self.subTest(path=path), self.assertRaises(MaterializeRefused):
                self.workspaces.materialize("demo", {path: entry})
        self.assertEqual(list(Path(self._tmp.name).rglob("*")), [], "refused before anything is created, anywhere")

    def test_an_entry_mode_no_workspace_holds(self) -> None:
        """The composition root supplies the tree; the materializer reads only Git modes and bytes."""

        from types import SimpleNamespace

        with self.assertRaisesRegex(MaterializeRefused, "no Git entry mode"):
            self.workspaces.materialize("demo", {"d": SimpleNamespace(mode="040000", data=b"")})

    def test_a_link_in_the_runs_path(self) -> None:
        outside = Path(self._tmp.name) / "outside"
        outside.mkdir()
        self.home.root.mkdir(parents=True)
        os.symlink(outside, self.home.root / "runs")
        with self.assertRaises(HomeRefused):
            self.workspaces.materialize("demo", GROUP1)
        self.assertEqual(os.listdir(outside), [], "nothing written through the link")


class Removal(Fixture):
    def test_removal_never_descends_through_a_link(self) -> None:
        outside = Path(self._tmp.name) / "keep"
        outside.mkdir()
        (outside / "precious").write_bytes(b"keep me")
        tree = GROUP1.replace({"to-outside": Entry("120000", os.fsencode(str(outside)))})
        ws = self.workspaces.materialize("demo", tree)
        self.workspaces.remove(ws)
        self.assertFalse((self.home.root / "runs" / "demo" / ws.run_id).exists())
        self.assertEqual((outside / "precious").read_bytes(), b"keep me")


if __name__ == "__main__":
    unittest.main()
