"""The SSDS home as the Dispatcher uses it (Manual §26.3; the SD-59 threat boundary): its issue key and its journal.

The paths are the :class:`~ssds.ledger.qualification.Home` owner's: a ledger id that is a unit identity, every path
inside the resolved home, the home outside every repository, and no symbolic link anywhere in the operator tree,
checked before any effect (Review e6ac009 B7). Every later file effect walks from the home root one directory at a
time, each opened without following a link, so a link put in place after the check is refused rather than
followed. A file is used only when it is a regular file owned by this user and readable by no one else; the
journal is appended to only through a file with a single name, so no other file is ever written through.
"""

from __future__ import annotations

import os
import secrets
import stat
from pathlib import Path

from ssds.ledger.qualification import Home, HomeRefused, write_all


class DispatcherHome(Home):
    ISSUE_KEY = ("keys", "dispatcher")
    JOURNAL = "dispatcher-journal.jsonl"

    def issue_key_parts(self, ledger_id: str) -> tuple[str, ...]:
        self.check_ledger_id(ledger_id)
        return (*self.ISSUE_KEY, f"{ledger_id}.ed25519")

    def journal_parts(self, ledger_id: str) -> tuple[str, ...]:
        self.check_ledger_id(ledger_id)
        return ("state", ledger_id, self.JOURNAL)

    def path(self, parts: tuple[str, ...]) -> Path:
        return self._file(*parts)

    def _check_paths(self, ledger_id: str) -> None:
        super()._check_paths(ledger_id)
        self.path(self.issue_key_parts(ledger_id)), self.path(self.journal_parts(ledger_id))

    # -- file effects, never through a link ---------------------------------------------------------------------

    def _directory(self, parts: tuple[str, ...], create: bool) -> int | None:
        """A descriptor of the directory ``parts`` under the home, or ``None`` when it is absent and not created."""

        if create:
            self.root.mkdir(parents=True, exist_ok=True, mode=0o700)  # the home is created on first write
        try:
            descriptor = os.open(self.root, os.O_RDONLY | os.O_DIRECTORY)  # the home itself may be reached by a link
        except FileNotFoundError:
            return None
        try:
            for part in parts:
                if create:
                    try:
                        os.mkdir(part, 0o700, dir_fd=descriptor)
                    except FileExistsError:
                        pass
                try:
                    inner = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
                except FileNotFoundError:
                    os.close(descriptor)
                    return None
                except OSError as exc:
                    raise HomeRefused(f"{part} under the SSDS home is not a directory of its own ({exc.strerror})"
                                      ) from None
                os.close(descriptor)
                descriptor = inner
        except BaseException:
            os.close(descriptor)
            raise
        return descriptor

    @staticmethod
    def _private(descriptor: int, name: str, single: bool) -> None:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.geteuid():
            raise HomeRefused(f"{name} is not a regular file of this user; the SSDS home holds only its own files")
        if stat.S_IMODE(info.st_mode) & 0o077:
            raise HomeRefused(f"{name} is readable by others ({oct(stat.S_IMODE(info.st_mode))})")
        if single and info.st_nlink != 1:
            raise HomeRefused(f"{name} has another name; the SSDS home writes through none")

    def _open(self, directory: int, name: str, flags: int) -> int:
        try:
            return os.open(name, flags | os.O_NOFOLLOW, 0o600, dir_fd=directory)
        except FileNotFoundError:
            raise
        except OSError as exc:
            raise HomeRefused(f"{name} under the SSDS home cannot be opened as its own file ({exc.strerror})") from None

    def read_private(self, parts: tuple[str, ...]) -> bytes | None:
        """The file's bytes, or ``None`` when it does not exist."""

        self.path(parts)
        directory = self._directory(parts[:-1], create=False)
        if directory is None:
            return None
        try:
            try:
                descriptor = self._open(directory, parts[-1], os.O_RDONLY)
            except FileNotFoundError:
                return None
            with os.fdopen(descriptor, "rb") as handle:
                self._private(handle.fileno(), parts[-1], single=False)
                return handle.read()
        finally:
            os.close(directory)

    def create_private(self, parts: tuple[str, ...], data: bytes) -> bool:
        """Create the file with ``data`` unless it exists, atomically: a fresh private file is written whole, then
        linked to the name, which fails if the name exists. Returns whether this call created it."""

        self.path(parts)
        directory = self._directory(parts[:-1], create=True)
        temporary = f".{parts[-1]}.{secrets.token_hex(8)}.tmp"
        try:
            descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600,
                                 dir_fd=directory)
            try:
                try:
                    write_all(descriptor, data)
                    os.fsync(descriptor)
                finally:
                    os.close(descriptor)
                try:
                    os.link(temporary, parts[-1], src_dir_fd=directory, dst_dir_fd=directory, follow_symlinks=False)
                    created = True
                except FileExistsError:
                    created = False
            finally:
                os.unlink(temporary, dir_fd=directory)
            os.fsync(directory)
            return created
        finally:
            os.close(directory)

    def append_private(self, parts: tuple[str, ...], data: bytes) -> None:
        """Append ``data`` to the file, created private if absent, and make it durable."""

        self.path(parts)
        directory = self._directory(parts[:-1], create=True)
        try:
            descriptor = self._open(directory, parts[-1], os.O_WRONLY | os.O_CREAT | os.O_APPEND)
            try:
                self._private(descriptor, parts[-1], single=True)
                write_all(descriptor, data)
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
        finally:
            os.close(directory)


__all__ = ["DispatcherHome"]
