"""The ``ssds`` program's one composition root (Manual §26.3, A7).

It mounts one flat command set: Core's version-bound commands, with their
accepted behaviour, then the SSDS operations as their owning components provide
them (the Interface's, Phase E). It wires the Interface to the ledger, the
witnesses, the high-water mark and the content trees (reading E3). A command name
claimed twice fails composition, so the collision is caught in acceptance.
"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

import typer
from typer.models import CommandInfo

from ssds.content import GitReadError, read_tree
from ssds.core import cli as core_cli
from ssds.core.api.v1 import ssds_home
from ssds.interface.commands import make_commands
from ssds.interface.operations import Refused, Session
from ssds.ledger.qualification import FileWitness, HighWaterMark, Home, WitnessModel
from ssds.ledger.read import read_chain


class HomeAccess:
    """The Interface's read access to one ledger in the SSDS home (reading E3): the chain, the declared file
    witnesses and the high-water mark, whose write goes through the checked home (SD-59)."""

    def __init__(self, home: Home, ledger_id: str) -> None:
        home.check(ledger_id)  # the Phase D threat boundary holds before anything is read or written
        self.home = home
        self.ledger_id = ledger_id

    def chain(self):
        return read_chain(self.home.ledger_repository(self.ledger_id), self.ledger_id)

    def witness_reports(self, model: WitnessModel):
        reports = {w.id: FileWitness(Path(w.location)).read(self.ledger_id) if w.kind == "FILE" else None
                   for w in model.witnesses}
        retired = any(FileWitness(Path(w.location)).retired(self.ledger_id) for w in model.witnesses if w.kind == "FILE")
        return reports, retired

    def high_water(self) -> HighWaterMark | None:
        return self.home.high_water(self.ledger_id).get()

    def raise_high_water(self, mark: HighWaterMark) -> None:
        self.home.check(self.ledger_id)
        self.home.high_water(self.ledger_id).set(mark)


def connect(ledger_id: str, repository: Path) -> Session:
    """A session over a ledger in the SSDS home, its trees read from ``repository``."""

    def trees(commit: str):
        try:
            return read_tree(repository, commit)
        except GitReadError as exc:  # the repository named is not the one the ledger records
            raise Refused(f"cannot read {commit} from {repository}: {exc}") from None

    return Session(HomeAccess(Home(ssds_home()), ledger_id), trees)


#: SSDS operations mounted beside Core's commands; each joins when its owner exists.
SSDS_COMMANDS: tuple[CommandInfo, ...] = make_commands(connect)


class CommandCollision(RuntimeError):
    """Two command sets claim one command name."""


def command_name(info: CommandInfo) -> str:
    if info.name:
        return info.name
    return typer.main.get_command_name(info.callback.__name__)


def compose(*command_sets: tuple[str, Iterable[CommandInfo]]) -> typer.Typer:
    root = typer.Typer(
        name="ssds",
        help="SSDS: scientific software development orchestration; renders profile-correct stage prompts.",
        add_completion=False,
        no_args_is_help=True,
    )
    owners: dict[str, str] = {}
    for owner, commands in command_sets:
        for info in commands:
            name = command_name(info)
            if name in owners:
                raise CommandCollision(f"command {name!r} is claimed by {owners[name]} and {owner}")
            owners[name] = owner
            root.registered_commands.append(info)
    return root


app = compose(("core", core_cli.app.registered_commands), ("ssds", SSDS_COMMANDS))


def main() -> int:
    return core_cli.main(app)
