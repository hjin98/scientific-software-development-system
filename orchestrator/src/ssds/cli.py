"""The ``ssds`` program's one composition root (Manual §26.3, A7).

It mounts one flat command set: Core's version-bound commands, with their
accepted behaviour, then the SSDS operations as their owning components provide
them (none yet; the Interface is built in Phase E). A command name claimed twice
fails composition, so the collision is caught in acceptance.
"""

from __future__ import annotations

from collections.abc import Iterable

import typer
from typer.models import CommandInfo

from ssds.core import cli as core_cli

#: SSDS operations mounted beside Core's commands; each joins when its owner exists.
SSDS_COMMANDS: tuple[CommandInfo, ...] = ()


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
