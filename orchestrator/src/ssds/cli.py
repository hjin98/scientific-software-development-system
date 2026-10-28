"""The ``ssds`` program's one composition root (Manual §26.3, A7).

It mounts one flat command set: Core's version-bound commands, with their
accepted behaviour, then the SSDS operations as their owning components provide
them (the Interface's, Phase E). It wires the Interface to the ledger, the
witnesses, the high-water mark and the content trees (reading E3). A command name
claimed twice fails composition, so the collision is caught in acceptance.
"""

from __future__ import annotations

import dataclasses
import json
import time
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import typer
from typer.models import CommandInfo

from ssds.admission.request import REPORT_KINDS, AdmissionHalted, AppendRefused, BoundaryRefused, EntryInvalid, \
    request_id
from ssds.content import GitReadError, ancestry, branch_head, read_tree
from ssds.core import cli as core_cli
from ssds.core.api.v1 import ssds_home
from ssds.derivation import trust_roots
from ssds.interface.commands import make_commands
from ssds.interface.operations import Refused, Session
from ssds.dispatcher import DispatcherHome, observe
from ssds.ledger.qualification import FileWitness, HighWaterMark, Home, HomeRefused, WitnessSpec, currentness, \
    lineage_witnesses
from ssds.ledger.read import read_chain, with_id

#: What a pass, or a request admitted through one, refuses with: reported as JSON and exit 1, never a traceback
#: (review of 6de6cf0d, N3).
PASS_REFUSALS = (Refused, HomeRefused, AdmissionHalted, BoundaryRefused, EntryInvalid, AppendRefused)

#: §16.1's human request forms (reading F121): ``report`` submits §15.1's report kinds, ``decide`` a gate or human
#: decision, ``submit`` any other kind.
DECISION_KINDS = frozenset({"GATE_DECISION", "HUMAN_DECISION"})


def command_takes(command: str, kind: Any) -> bool:
    if command == "report":
        return kind in REPORT_KINDS
    if command == "decide":
        return kind in DECISION_KINDS
    return isinstance(kind, str) and kind not in REPORT_KINDS | DECISION_KINDS


def _human_record(command: str, record: Any, actor: str) -> dict:
    """A record of ``actor``'s, its identity computed: the actor, its class and the absent binding are filled when
    the record omits them and refused when it names others (a human binding speaks only for its human, §25.1)."""

    if not isinstance(record, dict):
        raise Refused("each record is a JSON object")
    if "id" in record:
        raise Refused("a record carries no id: its identity is computed")
    if not command_takes(command, record.get("kind")):
        raise Refused(f"ssds {command} does not submit a record of kind {record.get('kind')!r}")
    filled = {"actor": actor, "actor_class": "HUMAN", "binding": None, **record}
    if (filled["actor"], filled["actor_class"], filled["binding"]) != (actor, "HUMAN", None):
        raise Refused(f"a {record.get('kind')} record of {filled['actor']!r} ({filled['actor_class']}) is not "
                      f"{actor}'s own with no binding")
    return with_id(filled)


ARMOR = ("-----BEGIN SSH SIGNATURE-----", "-----END SSH SIGNATURE-----")


def canonical_signature(text: str) -> str:
    """The armor ``ssh-keygen -Y sign`` writes (its body wrapped at 70 columns, one final newline), rebuilt from any
    re-wrapping, line-ending or whitespace variant of it, so one signature gives one request identity (review of
    2d03161c, N1). Text that is no armor is returned unchanged, for Admission to refuse."""

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) < 3 or (lines[0], lines[-1]) != ARMOR:
        return text
    body = "".join(lines[1:-1])
    return "\n".join([ARMOR[0], *(body[i:i + 70] for i in range(0, len(body), 70)), ARMOR[1]]) + "\n"


def _summary(ledger_id: str, rid: str, request: dict, actor: str) -> str:
    """A readable account of a prepared request: each record's kind, target and outcome, and each adopted delta."""

    lines = [f"request {rid}", f"ledger {ledger_id} at position {request['base_position']}, "
             f"integration head {request['base_commit']}", f"signed by {actor}", "records:"]
    for record in request["records"]:
        lines.append(f"  {record['kind']} {record['id']}")
        lines.append(f"    target  {json.dumps(record.get('target'), sort_keys=True)}")
        lines.append(f"    outcome {json.dumps(record.get('outcome'))}")
    lines.append("adopted deltas:" if request["adopted_deltas"] else "adopted deltas: none")
    lines.extend(f"  {json.dumps(delta, sort_keys=True)}" for delta in request["adopted_deltas"])
    return "\n".join(lines) + "\n"


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

        from ssds.admission.request import request_id, shadow_boundary

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

        from ssds.admission.request import observe_only

        return observe_only(self.access.home.root, self.access.ledger_id, self.trees, self.repository,
                            self.access.ancestry(), self.boundary)

    def observed(self, name: str, rebind: bool = False) -> tuple[str, dict | None]:
        """The observed ref's head (SD-64 Q-F2 (i)): ``name`` a branch of the repository, resolved to a commit, and
        the same name as on first use, recorded in operator state; another only with ``rebind``, which records the
        change (plan check of 603295c8, answer 2). Returns the head and the line to record once the pass is
        accepted, so a refused pass records nothing."""

        head = branch_head(self.repository, name)
        if head is None:
            raise Refused(f"{name!r} is not a branch of {self.repository} resolving to a commit")
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

    def _pass(self, name: str, rebind: bool):
        """The checks every pass makes before Admission acts: the observed ref (``observed``), the held head
        (this host's provisional entry completed first, §22.4), and the observed head descending from the last
        observation (SD-64)."""

        from ssds.admission.request import expected_head

        obs, line = self.observed(name, rebind)
        admission = self.admission()
        chain = admission.held_head()
        entries = chain.entries[: chain.readable_through + 1]
        expected = expected_head(entries)
        if obs != expected and ancestry(self.repository)(expected, obs) is not True:
            raise Refused(f"{name} at {obs} does not descend from the last observation {expected}: restore the branch "
                          f"(the observed branch is never rewritten, SD-64), or a ledger-level recovery is the "
                          f"stakeholder's decision (§23)")
        return admission, entries, expected, obs, line

    def _taking_effect(self, expected: str | None, obs: str, line: dict | None, action):
        """``action``'s result, the observed ref recorded only once the pass took effect: when ``action`` returns,
        or when it raises after ``obs``'s absorption was appended, so the ledger observes ``obs`` (review of
        6de6cf0d, B1). A pass refused before that records nothing. "Took effect" means the ledger observes ``obs``,
        not that this process appended it: a concurrent pass that absorbed the same ``obs`` counts, as an immediate
        retry would record the same line (re-check of 026ef60b, N-a)."""

        from ssds.admission.request import expected_head

        try:
            result = action()
        except BaseException:
            if line is not None and obs != expected:
                try:
                    chain = self.access.chain()
                    took = expected_head(chain.entries[: chain.readable_through + 1]) == obs
                except Exception:  # an unreadable ledger proves nothing took effect
                    took = False
                if took:
                    self._record_ref(line)
            raise
        self._record_ref(line)
        return result

    def serve(self, name: str, rebind: bool = False) -> dict:
        """One observe-only pass (F120): the observed head absorbed when it moved; nothing else."""

        admission, entries, expected, obs, line = self._pass(name, rebind)
        report = {"ledger_id": self.access.ledger_id, "observed_ref": name, "obs": obs, "expected": expected,
                  "absorbed": False, "mode": "observe-only: nothing is published (F1)"}
        if obs == expected:
            self._record_ref(line)
            return {**report, "position": len(entries) - 1}
        self._taking_effect(expected, obs, line, lambda: admission.absorb(entries, obs))
        return {**report, "absorbed": True, "position": len(entries)}

    # -- records-only requests (step 10c; reading F121) ---------------------------------------------------------

    def request_parts(self, rid: str, name: str) -> tuple[str, ...]:
        """A file of the request workspace ``state/<ledger>/requests/<request digest>/`` (SD-59's checked tree)."""

        return ("state", self.access.ledger_id, "requests", rid.removeprefix("sha256:"), name)

    def prepare(self, command: str, records: Any, adopted: list, actor: str) -> tuple[Path, str]:
        """A records-only request at the ledger's expected head, written unsigned to its workspace with a readable
        summary and the message the human signs (F121). Returns the workspace and the summary. Nothing here signs:
        the key stays the human's."""

        from ssds.admission.request import expected_head, request_id, request_message

        if not isinstance(records, list) or not records:
            raise Refused("RECORDS is a JSON array of one or more records")
        chain = self.access.chain()
        entries = chain.entries[: chain.readable_through + 1]
        if actor not in trust_roots(entries).humans:
            raise Refused(f"{actor!r} is not a human key registered in force on ledger {self.access.ledger_id}")
        prepared = [_human_record(command, record, actor) for record in records]
        for delta in adopted:
            if not isinstance(delta, dict):
                raise Refused("each adopted delta is a JSON object")
        request = {"binding": None, "claims": [], "base_position": len(entries) - 1,
                   "base_commit": expected_head(entries), "candidates": [], "adopted_deltas": list(adopted),
                   "records": prepared, "objects": {}}
        rid = request_id(request)
        summary = _summary(self.access.ledger_id, rid, request, actor)
        state = self.state()
        for name, data in (("request.json", json.dumps(request, indent=2, sort_keys=True).encode() + b"\n"),
                           ("summary.txt", summary.encode()),
                           ("request-message.txt", request_message(request))):
            state.create_private(self.request_parts(rid, name), data)  # identical bytes when prepared before
        return state.path(self.request_parts(rid, "request.json")).parent, summary

    def admit_prepared(self, directory: Path, name: str, rebind: bool = False, command: str | None = None) -> dict:
        """The prepared request in ``directory``, its message rebuilt from ``request.json`` (``request-message.txt``
        is never read), the human's signature from ``request-message.txt.sig`` attached in its canonical armor,
        decided by Admission after the pass's checks (F121). Its records are one human's, whose signature Admission
        verifies, and of the kinds ``command`` submits when it is named (review of 2d03161c, N4). The report
        carries the summary of what was submitted, which is what the signature covers (N3)."""

        try:
            request = json.loads((directory / "request.json").read_bytes())
            signature = canonical_signature((directory / "request-message.txt.sig").read_text(encoding="ascii"))
        except (OSError, ValueError, RecursionError) as exc:  # N5: deeply nested input is refused too
            raise Refused(f"cannot read the prepared request in {directory}: {exc}") from None
        records = request.get("records") if isinstance(request, dict) else None
        actors = {r.get("actor") for r in records if isinstance(r, dict)} if isinstance(records, list) else set()
        if len(actors) != 1 or not isinstance(next(iter(actors)), str):
            raise Refused(f"{directory}/request.json is not a prepared request: its records are not one human's")
        if command is not None and not all(isinstance(r, dict) and command_takes(command, r.get("kind"))
                                           for r in records):
            raise Refused(f"{directory} holds records ssds {command} does not submit")
        actor = actors.pop()
        signed = {**request, "binding": {"human": {"actor": actor, "signature": signature}}}
        admission, _, expected, obs, line = self._pass(name, rebind)
        decision = self._taking_effect(expected, obs, line, lambda: admission.admit(signed, obs))
        try:
            summary = _summary(self.access.ledger_id, request_id(request), request, actor)
        except (KeyError, TypeError):  # a request Admission rejected need not be summarizable
            summary = None
        return {"ledger_id": self.access.ledger_id, "observed_ref": name, "submitted": summary,
                **dataclasses.asdict(decision)}

    def observe(self) -> dict:
        """``dispatcher serve``'s report at the qualified head (F8, F65)."""

        chain = self.access.chain()
        witnesses = lineage_witnesses(chain) if chain.genesis is not None else []
        reports, statements = self.access.witness_reports(witnesses) if witnesses else ({}, {})
        held = currentness(chain, reports, statements, self.access.high_water())
        return observe(chain, self.trees, held, self.access.ancestry())


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


def request_command(command: str, purpose: str) -> CommandInfo:
    """``ssds <command> --prepare RECORDS`` and ``ssds <command> --admit DIR`` (reading F121)."""

    def run(ledger: str = typer.Option(..., "--ledger", help="the ledger id in the SSDS home"),
            prepare: Path | None = typer.Option(None, "--prepare", help="a JSON array of records, each without id"),
            adopt: list[Path] | None = typer.Option(None, "--adopt", help="a JSON file of one adopted delta"),
            actor: str | None = typer.Option(None, "--actor", help="the human (human:SHA256:...) who signs"),
            admit: Path | None = typer.Option(None, "--admit", help="a prepared request's directory, signed"),
            repository: Path = typer.Option(Path("."), "--repository",
                                            help="the repository whose history the ledger names"),
            observed_ref: str | None = typer.Option(None, "--observed-ref", help="the branch the ledger observes"),
            rebind_observed_ref: bool = typer.Option(False, "--rebind-observed-ref",
                                                     help="observe another branch than before (recorded)")) -> None:
        try:
            if (prepare is None) == (admit is None):
                raise Refused("give exactly one of --prepare RECORDS and --admit DIR")
            composition = Composition(ledger, repository)
            if prepare is not None:
                if actor is None:
                    raise Refused("--prepare needs --actor, the human who will sign")
                try:
                    records = json.loads(prepare.read_bytes())
                    adopted = [json.loads(path.read_bytes()) for path in adopt or []]
                except (OSError, ValueError) as exc:
                    raise Refused(f"cannot read the request's input: {exc}") from None
                directory, summary = composition.prepare(command, records, adopted, actor)
                typer.echo(summary + f"\nprepared in {directory}\nsign it with your own key:\n"
                           f"  ssh-keygen -Y sign -f <your key> -n ssds {directory / 'request-message.txt'}\n"
                           f"then admit it:\n  ssds {command} --ledger {ledger} --repository <repository> "
                           f"--observed-ref <branch> --admit {directory}")
                return
            if observed_ref is None:
                raise Refused("--admit needs --observed-ref, the branch the ledger observes")
            report = composition.admit_prepared(admit, observed_ref, rebind_observed_ref, command)
        except PASS_REFUSALS as exc:
            typer.echo(json.dumps({"refused": str(exc)}, indent=2, sort_keys=True))
            raise typer.Exit(1) from None
        typer.echo(json.dumps(report, indent=2, sort_keys=True))
        raise typer.Exit(0 if report["decision"] == "ACCEPT" else 1)

    run.__doc__ = (f"{purpose}: --prepare writes an unsigned records-only request and its summary; --admit submits "
                   f"it once you have signed it. Nothing here signs: the key stays yours (F121).")
    return CommandInfo(name=command, callback=run)


#: §16.1's human forms under the Manual's names (§26.3; reading F121): no envelopes on the real ledger (F4).
REQUEST_COMMANDS: tuple[CommandInfo, ...] = (
    request_command("report", "Report a finding, amendment request, blocker or question"),
    request_command("submit", "Submit records of any other kind, adopting quarantined deltas with --adopt"),
    request_command("decide", "Record a gate or human decision"),
)

app = compose(("core", core_cli.app.registered_commands), ("ssds", SSDS_COMMANDS), ("requests", REQUEST_COMMANDS))

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

    try:
        report = Composition(ledger, repository).serve(observed_ref, rebind_observed_ref)
    except PASS_REFUSALS as exc:
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
