"""The ``ssds`` program's one composition root (Manual §26.3, A7).

It mounts one flat command set: Core's version-bound commands, with their
accepted behaviour, then the SSDS operations as their owning components provide
them (the Interface's, Phase E). It wires the Interface to the ledger, the
witnesses, the high-water mark and the content trees (reading E3). A command name
claimed twice fails composition, so the collision is caught in acceptance.
"""

from __future__ import annotations

import json
import re
import subprocess
import time
from collections.abc import Iterable
from pathlib import Path

import typer
from typer.models import CommandInfo

from ssds.content import GitReadError, ancestry, read_tree
from ssds.core import cli as core_cli
from ssds.core.api.v1 import ssds_home
from ssds.interface.commands import make_commands
from ssds.interface.operations import Refused, Session
from ssds.dispatcher import observe
from ssds.dispatcher.home import DispatcherHome
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

    def ancestry(self):
        """The ledger repository's commit graph: genesis imports its baseline and every absorption its observed
        commits there (step 6a), so each ``obs`` and each published ``C_n`` is reachable without reading the product
        repository (F119). An overtaken ``C_n`` that no ``obs`` brought in is absent, so it reads ``UNKNOWN`` until
        a later ``obs`` does, the conservative side (review of abcb194e, N3)."""

        return ancestry(self.home.ledger_repository(self.ledger_id))


class Composition:
    """The one factory through which every derivation the CLI and its serve paths build is made (reading F119; plan
    check of 603295c8, note 1): the ledger's access, which carries the commit graph, and its trees, read from the
    repository the ledger names."""

    def __init__(self, ledger_id: str, repository: Path) -> None:
        self.access = HomeAccess(Home(ssds_home()), ledger_id)
        self.repository = repository.resolve()

    def trees(self, commit: str):
        try:
            return read_tree(self.repository, commit)
        except GitReadError as exc:  # the repository named is not the one the ledger records
            raise Refused(f"cannot read {commit} from {self.repository}: {exc}") from None

    def doctrine(self, source: str, path: str) -> bytes | None:
        """A file of the pinned doctrine source, read at its immutable commit from the repository when it holds it
        (reading E37); None otherwise, and the brief says the text is not rendered."""

        try:
            entry = read_tree(self.repository, source).get(path)
        except GitReadError:
            return None
        return entry.data if entry is not None else None

    def session(self) -> Session:
        return Session(self.access, self.trees, self.doctrine)

    # -- observe-only Admission (step 10b; reading F120) ---------------------------------------------------------

    def state(self) -> DispatcherHome:
        """The ledger's operator state, ``state/<ledger>/`` inside SD-59's checked trees, through the home's safe
        file primitives."""

        return DispatcherHome(self.access.home.root)

    def boundary(self, request) -> str | None:
        """F1's shadow-boundary policy, its refusals logged in operator state and nowhere in the ledger."""

        from ssds.admission.engine import shadow_boundary
        from ssds.admission.request import request_id

        reason = shadow_boundary(request)
        if reason is not None:
            line = {"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "request_id": request_id(request),
                    "reason": reason}
            self.state().append_line(("state", self.access.ledger_id, "boundary.jsonl"),
                                     json.dumps(line, sort_keys=True).encode() + b"\n")
        return reason

    def admission(self):
        """Admission composed observe-only (F120): no publisher, the product repository read for absorptions, the
        ledger repository's graph, and the boundary policy at its entry."""

        from ssds.admission.engine import Admission
        from ssds.admission.genesis import AdmissionHome

        return Admission(AdmissionHome(self.access.home.root), self.access.ledger_id, self.trees,
                         product=self.repository, ancestry=self.access.ancestry(), entry_policy=self.boundary)

    def observed(self, name: str, rebind: bool = False) -> tuple[str, dict | None]:
        """The observed ref's head (SD-64 Q-F2 (i)): ``name`` a branch of the repository, resolved to a commit, and
        the same name as on first use, recorded in operator state; another only with ``rebind``, which records the
        change (plan check of 603295c8, answer 2). Returns the head and the line to record once the pass is
        accepted, so a refused pass records nothing."""

        if not _BRANCH.fullmatch(name) or ".." in name or name.endswith((".lock", "/")) or "//" in name:
            raise Refused(f"{name!r} is not a branch name")
        found = subprocess.run(["git", "-C", str(self.repository), "rev-parse", "--verify", "--quiet",
                                f"refs/heads/{name}^{{commit}}"], capture_output=True, text=True, check=False)
        head = found.stdout.strip()
        if found.returncode != 0 or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", head):
            raise Refused(f"{name} is not a branch of {self.repository} resolving to a commit")
        parts = ("state", self.access.ledger_id, "observed-ref.jsonl")
        recorded = self.state().read_private(parts)
        last = json.loads(recorded.splitlines()[-1])["ref"] if recorded else None
        if last is not None and last != name and not rebind:
            raise Refused(f"the ledger observes {last}; observing {name} needs --rebind-observed-ref, which is "
                          f"recorded (Q-F2)")
        line = None if last == name else {"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "ref": name,
                                          "previous": last}
        return head, line

    def _record_ref(self, line: dict | None) -> None:
        if line is not None:
            self.state().append_line(("state", self.access.ledger_id, "observed-ref.jsonl"),
                                     json.dumps(line, sort_keys=True).encode() + b"\n")

    def serve(self, name: str, rebind: bool = False) -> dict:
        """One observe-only pass (F120): the held head (this host's provisional entry completed first, §22.4), the
        observed head checked to descend from the last observation, and absorbed when it moved; nothing else."""

        from ssds.admission.engine import Admission

        obs, line = self.observed(name, rebind)
        admission = self.admission()
        chain = admission.held_head()
        entries = chain.entries[: chain.readable_through + 1]
        expected = Admission.expected_head(entries)
        report = {"ledger_id": self.access.ledger_id, "observed_ref": name, "obs": obs, "expected": expected,
                  "absorbed": False, "mode": "observe-only: nothing is published (F1)"}
        if obs == expected:
            self._record_ref(line)
            return {**report, "position": len(entries) - 1}
        if ancestry(self.repository)(expected, obs) is not True:
            raise Refused(f"{name} at {obs} does not descend from the last observation {expected}: restore the branch "
                          f"(the observed branch is never rewritten, SD-64), or a ledger-level recovery is the "
                          f"stakeholder's decision (§23)")
        self._record_ref(line)
        admission.absorb(entries, obs)
        return {**report, "absorbed": True, "position": len(entries)}

    def observe(self) -> dict:
        """``dispatcher serve``'s report at the qualified head (F8, F65)."""

        chain = self.access.chain()
        witnesses = lineage_witnesses(chain) if chain.genesis is not None else []
        reports, statements = self.access.witness_reports(witnesses) if witnesses else ({}, {})
        held = currentness(chain, reports, statements, self.access.high_water())
        return observe(chain, self.trees, held, self.access.ancestry())


#: A branch name the observed-ref option accepts (git's own rules, narrowed): no leading dash or dot.
_BRANCH = re.compile(r"[A-Za-z0-9_][A-Za-z0-9._/-]*")


def connect(ledger_id: str, repository: Path) -> Session:
    """A session over a ledger in the SSDS home, its trees read from ``repository``."""

    return Composition(ledger_id, repository).session()


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

    report = Composition(ledger, repository).observe()
    typer.echo(json.dumps(report, indent=2, sort_keys=True))
    raise typer.Exit(0 if "withheld" not in report else 1)


#: Admission's commands (Phase F step 10b): ``admission serve`` is observe-only on the real shadow ledger (F1, F120).
admission_app = typer.Typer(name="admission", help="Admission: observe the integration branch, append absorptions.",
                            no_args_is_help=True, add_completion=False)


@admission_app.command("serve")
def admission_serve(ledger: str = typer.Option(..., "--ledger", help="the ledger id in the SSDS home"),
                    repository: Path = typer.Option(Path("."), "--repository",
                                                    help="the repository whose history the ledger names"),
                    observed_ref: str = typer.Option(..., "--observed-ref", help="the branch the ledger observes"),
                    rebind_observed_ref: bool = typer.Option(False, "--rebind-observed-ref",
                                                             help="observe another branch than before (recorded)")
                    ) -> None:
    """One observe-only pass: absorb the observed branch's head if it moved, publishing nothing (F1, F120).

    Never rewrite the observed branch: a force-push rewinding it makes this command refuse until the branch again
    descends from the last observation (SD-64). A ledger holding such an absorption would carry a CRITICAL
    LATE_PUBLICATION integrity finding (catalogue §22.2), answered by a human decision (§22.3)."""

    from ssds.admission.engine import AdmissionHalted

    try:
        report = Composition(ledger, repository).serve(observed_ref, rebind_observed_ref)
    except (Refused, AdmissionHalted) as exc:
        typer.echo(json.dumps({"refused": str(exc)}, indent=2, sort_keys=True))
        raise typer.Exit(1) from None
    typer.echo(json.dumps(report, indent=2, sort_keys=True))


#: The MCP transport (Phase F step 8f, reading F70): JSON-RPC 2.0 over stdio, the CLI's operations through ``connect``.
mcp_app = typer.Typer(name="mcp", help="The MCP transport over stdio.", no_args_is_help=True, add_completion=False)


@mcp_app.command("serve")
def mcp_serve() -> None:
    """Serve the Interface's operations over MCP on stdin and stdout until the input ends."""

    import sys

    from ssds.interface.mcp import serve

    serve(connect, sys.stdin.buffer, sys.stdout)  # bytes: an undecodable line is a parse error, not a crash


for group in ("admission", "dispatcher", "mcp"):
    if any(command_name(info) == group for info in app.registered_commands):
        raise CommandCollision(f"command {group!r} is claimed twice")
app.add_typer(mcp_app, name="mcp")
app.add_typer(dispatcher_app, name="dispatcher")
app.add_typer(admission_app, name="admission")


def main() -> int:
    return core_cli.main(app)
