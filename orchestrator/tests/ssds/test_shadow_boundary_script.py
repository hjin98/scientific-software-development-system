"""Phase F step 10d's boundary script on fixture repositories (plan reading F122).

A snapshot and a comparison with nothing changed pass and leave the repository as they found it, the index file
included; a ref moved, a reflog appended, an object added and a file touched are each detected.
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from ._fixtures import commit, git, init_repo

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "shadow_boundary.py"


class Boundary(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: subprocess.run(["rm", "-rf", str(self.tmp)], check=False))
        self.repo = init_repo(self.tmp / "product")
        (self.repo / "a.py").write_text("v = 1\n")
        self.first = commit(self.repo, "first")
        (self.repo / "a.py").write_text("v = 2\n")
        self.second = commit(self.repo, "second")
        self.before = self.tmp / "before.json"

    def run_script(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, timeout=120)

    def snapshot(self) -> None:
        result = self.run_script("snapshot", "--repository", str(self.repo), "--out", str(self.before))
        self.assertEqual(result.returncode, 0, result.stderr)

    def compare(self) -> subprocess.CompletedProcess:
        return self.run_script("compare", "--repository", str(self.repo), "--before", str(self.before))

    def assertChanged(self, what: str) -> None:
        result = self.compare()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("CHANGED", result.stdout)
        self.assertIn(what, result.stdout)

    def test_nothing_changed_and_the_script_changes_nothing(self) -> None:
        index = self.repo / ".git" / "index"
        (self.repo / "a.py").touch()  # a stale stat: a status that refreshed the index would rewrite it
        stamp = (index.read_bytes(), os.stat(index).st_mtime_ns)
        self.snapshot()
        for _ in range(2):
            result = self.compare()
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("unchanged", result.stdout)
        self.assertEqual((index.read_bytes(), os.stat(index).st_mtime_ns), stamp, "the index is never refreshed")

    def test_packed_objects_count(self) -> None:
        git(self.repo, "repack", "-a", "-d", "-q")
        self.snapshot()
        self.assertEqual(self.compare().returncode, 0)
        import json

        self.assertGreaterEqual(len(json.loads(self.before.read_text())["objects"]), 6, "two commits, trees, blobs")

    def test_a_ref_moved(self) -> None:
        self.snapshot()
        git(self.repo, "update-ref", "refs/heads/main", self.first, self.second)
        self.assertChanged("ref refs/heads/main")

    def test_a_ref_added(self) -> None:
        self.snapshot()
        git(self.repo, "branch", "other")
        self.assertChanged("ref refs/heads/other")

    def test_head_switched(self) -> None:
        git(self.repo, "branch", "other", self.first)
        self.snapshot()
        git(self.repo, "symbolic-ref", "HEAD", "refs/heads/other")
        self.assertChanged("HEAD: {")

    def test_a_reflog_appended(self) -> None:
        self.snapshot()
        with open(self.repo / ".git" / "logs" / "HEAD", "a") as log:
            log.write(f"{self.second} {self.second} x <x@example.invalid> 0 +0000\tcheckout: nothing\n")
        self.assertChanged("reflog common:HEAD")

    def test_a_reflog_symlink_is_refused(self) -> None:
        outside_log = self.tmp / "outside-log"
        outside_log.write_text("external bytes\n")
        log = self.repo / ".git" / "logs" / "HEAD"
        log.unlink()
        log.symlink_to(outside_log)
        result = self.run_script("snapshot", "--repository", str(self.repo), "--out", str(self.before))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("symlink reflog is unsupported", result.stderr)

    def test_an_object_added(self) -> None:
        self.snapshot()
        git(self.repo, "hash-object", "-w", "--stdin", data=b"a new object\n")
        self.assertChanged("objects: 1 added")

    def test_a_file_touched(self) -> None:
        self.snapshot()
        (self.repo / "a.py").write_text("v = 3\n")
        self.assertChanged("status")

    def test_an_untracked_file(self) -> None:
        self.snapshot()
        (self.repo / "new.txt").write_text("x\n")
        self.assertChanged("new.txt")

    def test_index_only_change(self) -> None:
        self.snapshot()
        git(self.repo, "update-index", "--assume-unchanged", "a.py")
        self.assertChanged("index changed")

    def test_ref_storage_rewrite_with_unchanged_targets(self) -> None:
        self.snapshot()
        git(self.repo, "pack-refs", "--all")
        self.assertChanged("packed-refs changed")

    def test_content_changes_with_unchanged_status(self) -> None:
        for name in ("a.py", "untracked.txt", "ignored.txt"):
            with self.subTest(name=name):
                (self.repo / ".gitignore").write_text("ignored.txt\n")
                path = self.repo / name
                path.write_text("before\n")
                self.snapshot()
                path.write_text("after!\n")
                self.assertChanged(f"{name} changed")

    def test_a_linked_worktree_and_output_containment(self) -> None:
        other = self.tmp / "linked"
        git(self.repo, "worktree", "add", "-b", "linked", str(other))
        supported = subprocess.run(["git", "-C", str(self.repo), "worktree", "list", "--porcelain", "-z"],
                                   capture_output=True).returncode == 0
        if not supported:
            result = self.run_script("snapshot", "--repository", str(self.repo), "--out", str(self.before))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("linked worktree inventory requires Git", result.stderr)
            return  # the old-Git boundary is refusal, not a partial unchanged claim
        self.snapshot()
        (other / "a.py").write_text("changed in the other worktree\n")
        self.assertChanged("a.py changed")
        result = self.run_script("snapshot", "--repository", str(self.repo), "--out", str(other / "snap.json"))
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("outside the product repository", result.stderr)
        self.assertFalse((other / "snap.json").exists())

    def test_a_newline_worktree_cannot_alias_an_unrelated_repository(self) -> None:
        alias = init_repo(self.tmp / "prefix")
        (alias / "x").write_text("unrelated\n")
        commit(alias)
        other = Path(str(alias) + "\nsuffix")
        git(self.repo, "worktree", "add", "-b", "newline", str(other))
        result = self.run_script("snapshot", "--repository", str(self.repo), "--out", str(self.before))
        if result.returncode != 0:
            self.assertIn("linked worktree inventory requires Git", result.stderr)
            return
        (other / "a.py").write_text("changed in the actual newline worktree\n")
        self.assertChanged("a.py changed")

    def test_a_symlink_target_is_not_read(self) -> None:
        target = self.tmp / "outside"
        target.write_text("private outside bytes\n")
        (self.repo / "link").symlink_to(target)
        self.snapshot()
        target.write_text("changed outside the boundary\n")
        self.assertEqual(self.compare().returncode, 0)
        (self.repo / "link").unlink()
        (self.repo / "link").symlink_to(self.tmp / "absent")
        self.assertChanged("link changed")

    def test_a_submodule_or_special_file_refuses_the_snapshot(self) -> None:
        os.mkfifo(self.repo / "pipe")
        result = self.run_script("snapshot", "--repository", str(self.repo), "--out", str(self.before))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsupported filesystem entry", result.stderr)
        (self.repo / "pipe").unlink()
        git(self.repo, "update-index", "--add", "--cacheinfo", f"160000,{self.first},module")
        result = self.run_script("snapshot", "--repository", str(self.repo), "--out", str(self.before))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("submodules are unsupported", result.stderr)

    def test_an_old_snapshot_cannot_certify_unchanged(self) -> None:
        import json

        self.snapshot()
        old = json.loads(self.before.read_text())
        del old["schema"]
        self.before.write_text(json.dumps(old))
        result = self.compare()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("take a new snapshot", result.stderr)

    def test_the_snapshot_lies_outside(self) -> None:
        for inside in (self.repo / "snap.json", self.repo / ".git" / "snap.json"):
            with self.subTest(inside=inside):
                result = self.run_script("snapshot", "--repository", str(self.repo), "--out", str(inside))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("outside the product repository", result.stderr)
                self.assertFalse(inside.exists())

    def test_a_snapshot_of_another_repository_is_refused(self) -> None:
        self.snapshot()
        other = init_repo(self.tmp / "other")
        (other / "b.txt").write_text("b\n")
        commit(other, "other")
        result = self.run_script("compare", "--repository", str(other), "--before", str(self.before))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("is a snapshot of", result.stderr)


if __name__ == "__main__":
    unittest.main()
