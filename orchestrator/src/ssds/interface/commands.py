"""The Interface's commands, mounted by the root module (Manual §16.10, §26.3): ``status``, ``ask``, ``read``.

Each command takes the ledger explicitly (``--ledger``; Phase D plan §7 Q5 stays unasked) and the repository
whose history the ledger names (``--repository``, default the working directory). The root module supplies
``connect``, which builds a :class:`~ssds.interface.operations.Session` over the SSDS home; answers print as
canonical JSON. ``status`` exits 1 when no current assertion can be made; a refusal (an SSDS home that fails its
check, an unknown query class, a reference that names nothing) prints to standard error and exits 2, presenting
nothing.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path

import typer
from typer.models import CommandInfo

from ssds.ledger.qualification import HomeRefused

from .operations import Refused, Session

Connect = Callable[[str, Path], Session]


def _print(value: object) -> None:
    typer.echo(json.dumps(value, indent=2, sort_keys=True, default=str))


def _answer(produce: Callable[[], dict]) -> dict:
    try:
        return produce()
    except (Refused, HomeRefused) as refused:  # only refusals: a fault elsewhere is never reported as one
        typer.echo(f"refused: {refused.args[0] if refused.args else refused}", err=True)
        raise typer.Exit(2) from None


def make_commands(connect: Connect) -> tuple[CommandInfo, ...]:
    """The Interface's commands, bound to the root module's ``connect``."""

    ledger_option = typer.Option(..., "--ledger", help="the ledger id in the SSDS home")
    repository_option = typer.Option(Path("."), "--repository", help="the repository whose history the ledger names")

    def status(ledger: str = ledger_option, repository: Path = repository_option) -> None:
        """The ledger's qualification, current assertion, subjects and derived obligations."""

        report = _answer(lambda: connect(ledger, repository.resolve()).status())
        _print(report)
        raise typer.Exit(0 if report["current_assertion"] else 1)

    def ask(query: str = typer.Argument(..., help="a query class of Manual §16.2"),
            args: list[str] = typer.Argument(None, help="the query's arguments"),
            ledger: str = ledger_option, repository: Path = repository_option) -> None:
        """A typed query, answered at the qualified head (or labeled UNQUALIFIED)."""

        _print(_answer(lambda: connect(ledger, repository.resolve()).ask(query, *(args or []))))

    def read(ref: str = typer.Argument(..., help="a unit identity or a path"),
             ledger: str = ledger_option, repository: Path = repository_option) -> None:
        """Content by unit identity or path at the presented head."""

        _print(_answer(lambda: connect(ledger, repository.resolve()).read(ref)))

    return tuple(CommandInfo(name=name, callback=callback) for name, callback in
                 (("status", status), ("ask", ask), ("read", read)))


__all__ = ["Connect", "make_commands"]
