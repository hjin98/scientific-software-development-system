"""The ``ssds`` program's one composition root (Manual §26.3, A7).

It mounts one flat command set: Core's version-bound commands, with their
accepted behaviour, then the SSDS operations as their owning components provide
them (the Interface's, Phase E). It wires the Interface to the ledger, the
witnesses, the high-water mark and the content trees (reading E3). A command name
claimed twice fails composition, so the collision is caught in acceptance.
"""

from __future__ import annotations

import json
from collections.abc import Iterable
from pathlib import Path

import typer
from typer.models import CommandInfo

from ssds.content import GitReadError, read_tree
from ssds.core import cli as core_cli
from ssds.core.api.v1 import ssds_home
from ssds.interface.commands import make_commands
from ssds.interface.operations import Refused, Session
from ssds.dispatcher import observe
from ssds.ledger.qualification import FileWitness, HighWaterMark, Home, WitnessSpec, currentness, lineage_witnesses
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

    def witness_reports(self, witnesses: Iterable[WitnessSpec]):
        witnesses = list(witnesses)
        reports = {w.id: FileWitness(Path(w.location)).read(self.ledger_id) if w.kind == "FILE" else None
                   for w in witnesses}
        statements = {w.id: FileWitness(Path(w.location)).statement(self.ledger_id) if w.kind == "FILE" else None
                      for w in witnesses}
        return reports, statements

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

    def doctrine(source: str, path: str) -> bytes | None:
        """A file of the pinned doctrine source, read at its immutable commit from ``repository`` when that
        repository holds it (reading E37); None otherwise, and the brief says the text is not rendered."""

        try:
            entry = read_tree(repository, source).get(path)
        except GitReadError:
            return None
        return entry.data if entry is not None else None

    return Session(HomeAccess(Home(ssds_home()), ledger_id), trees, doctrine)


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

#: The Dispatcher's commands (Phase F step 8a): ``dispatcher serve`` is observe-only on a shadow ledger (reading F8).
dispatcher_app = typer.Typer(name="dispatcher", help="The Dispatcher: what it would issue at the qualified head.",
                             no_args_is_help=True, add_completion=False)


@dispatcher_app.command("serve")
def dispatcher_serve(ledger: str = typer.Option(..., "--ledger", help="the ledger id in the SSDS home"),
                     repository: Path = typer.Option(Path("."), "--repository",
                                                     help="the repository whose history the ledger names")) -> None:
    """The would-issue set at the qualified head ``H*``, observe-only: nothing is issued, no run ref is written, and
    no operator state changes (F8, F65)."""

    access = HomeAccess(Home(ssds_home()), ledger)
    chain = access.chain()
    reports, statements = access.witness_reports(lineage_witnesses(chain)) if chain.genesis is not None else ({}, {})
    held = currentness(chain, reports, statements, access.high_water())
    repo = repository.resolve()
    report = observe(chain, lambda commit: read_tree(repo, commit), held)
    typer.echo(json.dumps(report, indent=2, sort_keys=True))
    raise typer.Exit(0 if "withheld" not in report else 1)


if any(command_name(info) == "dispatcher" for info in app.registered_commands):
    raise CommandCollision("command 'dispatcher' is claimed twice")
app.add_typer(dispatcher_app, name="dispatcher")


def main() -> int:
    return core_cli.main(app)
