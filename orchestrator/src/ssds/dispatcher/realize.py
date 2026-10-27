"""The Dispatcher's evidence obligations, run and submitted (catalogue §6.9, §17.2-§17.5, §25.1; Phase F step 9f-ii-iii,
readings F114-F115).

``REALIZE`` and ``RERUN`` are the Dispatcher's (``schedule.ready`` selects agent roles only). The ``Executor`` runs one
for a class of kind ``DISPATCHER`` whose runner key it holds, through ``runner.Sandbox``, and submits the
``REALIZATION`` signed by that key, its actor ``machinery:runner@<key id>`` (never the issue key, §25.1):

- **held**, never run: an external custody class (its runs are the custodian's); a class without a provider here;
  a ``RERUN`` no run here could serve ``ext``-equal (the class does not observe outside reads, so every run is
  unpinnable; or ``real(a⁻)`` recorded pins or attributes this provider does not), computed from the class's current
  facts against ``real(a⁻)``'s recorded ones (§6.9's "operational decision"; review of 8f6cec9b, note); a second
  execution of a configuration while one is outstanding; an obligation whose retry budget is spent, or waiting out
  its backoff; and everything on a real ledger (F8).
- **written ahead**: ``EXEC_INTENT`` (with the ``INCOMPLETE CRASHED`` record a restart would submit), ``EXEC_STARTED``,
  ``EXEC_ENDED``, ``REQUEST`` and ``DECIDED``. ``recover`` submits an intent never ended as ``INCOMPLETE CRASHED``
  (over-reporting is the safe side: every started execution ends in an admitted observation) and resubmits an
  undecided request.
- **the record**: the execution basis derivation decides (``execution_basis`` at the head the run starts from: the
  current one, or the failing tree's for a ``RERUN`` there), the runner's own fields, the configuration
  ``run_configuration`` gives (never the runner's own; review of bde2a6d5, note 2), and the outcome only when
  ``outcome_problems`` finds none (else ``INCOMPLETE MALFORMED_OUTPUT``; review of cc028146, note 3). A crashed or
  bounded run's surviving outputs are kept as a native artifact its record references; nothing else in ``/out`` is
  read (note 5).
"""

from __future__ import annotations

import dataclasses
import hashlib
import secrets
import time
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, PrivateFormat

from ssds.admission.request import request_message
from ssds.derivation import (Workflow, derive, effective_bound_hours, execution_basis, outcome_problems,
                             run_configuration)
from ssds.ledger.qualification import Home

from .home import DispatcherHome
from .issue import _public_hex, key_id
from .journal import Journal
from .runner import MaterializeRefused, RunnerProvider, Sandbox, Workspaces

RECORDED_AT = "1970-01-01T00:00:00Z"  # replaced by the composition root's clock


class RunnerKey:
    """A designated runner class's key in the SSDS home's checked operator tree (F114): one key, one class. Its
    rotation and retirement go through ``KEY_LIFECYCLE`` (role ``RUNNER``), its undecided observations drained first
    (runbook N2)."""

    def __init__(self, home: Home, ledger_id: str, runner_class: str) -> None:
        self.home = DispatcherHome(home.root)
        self.home.check(ledger_id)
        self.parts = self.home.runner_key_parts(ledger_id, runner_class)
        data = self.home.read_private(self.parts)
        if data is None:
            self.home.create_private(self.parts, Ed25519PrivateKey.generate().private_bytes(
                Encoding.Raw, PrivateFormat.Raw, NoEncryption()))
            data = self.home.read_private(self.parts)  # whichever creation won
        self._key = Ed25519PrivateKey.from_private_bytes(data)

    @property
    def public_hex(self) -> str:
        return _public_hex(self._key)

    @property
    def key_id(self) -> str:
        return key_id(self.public_hex)

    def trust_root(self) -> dict[str, str]:
        return {"role": "RUNNER", "id": self.key_id, "public_key": self.public_hex}

    def sign(self, request: Mapping[str, Any]) -> dict[str, Any]:
        return {**request, "binding": {"runner": {"key": self.key_id,
                                                  "signature": self._key.sign(request_message(request)).hex()}}}


@dataclass(frozen=True)
class Budget:
    """The retry budget per obligation (F95): ``attempts`` at most, each after ``base_seconds * 2**(n - 1)``."""

    attempts: int = 3
    base_seconds: float = 60.0

    def not_before(self, made: list[float]) -> float:
        return made[-1] + self.base_seconds * 2 ** (len(made) - 1) if made else 0.0


@dataclass(frozen=True)
class Run:
    """One obligation the Dispatcher could run here, or the reason it is held."""

    obligation: Any
    runner_class: str | None
    held: str | None = None


class Executor:
    def __init__(self, home: Home, ledger_id: str, chain: Callable[[], Any], trees: Callable[[str], Any],
                 providers: Mapping[str, RunnerProvider], submit: Callable[[dict[str, Any]], Any], *,
                 governs: Mapping[str, Any], budget: Budget = Budget(), wall: Callable[[], float] = time.time,
                 sandbox: Sandbox | None = None, real_ledger: bool = False,
                 recorded_at: Callable[[], str] = lambda: RECORDED_AT) -> None:
        self.home, self.ledger_id, self.chain, self.trees = DispatcherHome(home.root), ledger_id, chain, trees
        self.providers, self.submit, self.budget, self.wall = providers, submit, budget, wall
        self.journal = Journal(home, ledger_id)
        self.workspaces = Workspaces(self.home)
        self.sandbox = sandbox or Sandbox(self.workspaces, (self.home.root,))
        self.real_ledger, self.recorded_at, self.governs = real_ledger, recorded_at, dict(governs)

    # -- selection ------------------------------------------------------------------------------------------

    def runs(self, support: Any) -> list[Run]:
        """Every ``REALIZE`` and ``RERUN`` at the head, each runnable here or held with why."""

        s = support.s
        out = []
        outstanding = {e["hold"] for e in self.journal.open_executions()}
        for o in Workflow(support).obligations:
            if o.kind not in ("REALIZE", "RERUN"):
                continue
            spec, claims, real = self._subject(support, o)
            declared = s.specs.declaration(spec) if spec else None
            runner_class = getattr(declared, "runner", None)
            cls = s.policy.runners.get(runner_class) if runner_class else None
            out.append(Run(o, runner_class, self._held(support, o, cls, runner_class, real, spec, outstanding)))
        return out

    def _held(self, support: Any, o: Any, cls: Any, runner_class: str | None, real: str | None, spec: str | None,
              outstanding: set[str]) -> str | None:
        if self.real_ledger:
            return "a real ledger: nothing is executed without a campaign (F8)"
        if cls is None:
            return "no designated runner class"
        if cls.kind != "DISPATCHER":
            return "an external custody class: its runs are the custodian's"
        if runner_class not in self.providers:
            return "no provider for the class here"
        if RunnerKey(self.home, self.ledger_id, runner_class).key_id not in cls.keys:
            return "this Dispatcher holds no key the class designates"
        if o.kind == "RERUN":
            basis = support.a.basis(real)
            provider = self.providers[runner_class]
            if not cls.observes_outside_reads:
                return "the class does not observe outside reads: every run here is unpinnable, none ext-equal"
            if basis.get("pins") or dict(map(tuple, basis.get("attributes") or [])) != dict(provider.attributes):
                return "no run here records real(a⁻)'s pins and attributes: none ext-equal"
        if self._hold_key(o, spec) in outstanding:
            return "an execution of this configuration is outstanding"
        made = self.journal.attempts(o.id)
        if len(made) >= self.budget.attempts:
            return f"the retry budget is spent ({len(made)} attempts)"
        if self.wall() < self.budget.not_before(made):
            return "waiting out the retry backoff"
        return None

    def _subject(self, support: Any, o: Any) -> tuple[str | None, list[str], str | None]:
        s = support.s
        if o.kind == "REALIZE":
            return o.params["spec"]["unit"], [c["unit"] for c in o.params["claim"]], None
        real = support.a.real(o.target["record"])
        if real is None:
            return None, [], None
        record = s.record(real)
        return record["target"]["spec"]["unit"], [c["unit"] for c in record["target"]["claim"]], real

    def _hold_key(self, o: Any, spec: str | None) -> str:
        """One outstanding execution per configuration (§6.9; review of cc7abfed, note 1): the specification (its
        configuration's fixed attributes are its declaration's), no pins, the frame (always ``ADMITTED`` here), and
        the tree it runs on: the failing tree for a reproduction there, else the head."""

        on_failing = o.kind == "RERUN" and o.target.get("on") == "FAILING"
        tree = o.params.get("tree") if on_failing else "HEAD"
        return hashlib.sha256(repr((spec, "ADMITTED", tree)).encode()).hexdigest()

    # -- one run ---------------------------------------------------------------------------------------------

    def run(self, support: Any, item: Run) -> Any:
        """Runs ``item`` and submits its realization; returns the decision.

        Its request is journaled before its execution counts as ended (review of cc7abfed, B1): a failure anywhere
        after the intent leaves either an open execution, which ``recover`` reports ``INCOMPLETE CRASHED``, or an
        undecided request, which it resubmits; never neither."""

        if item.held is not None:
            raise ValueError(f"{item.obligation.id} is held: {item.held}")
        o, runner_class = item.obligation, item.runner_class
        spec, claims, real = self._subject(support, o)
        start = support.s
        if o.kind == "RERUN" and o.target["on"] == "FAILING":
            k = max(p for p in range(start.n + 1) if start.h.head(p) == o.params["tree"])
            at = derive(dataclasses.replace(self.chain(), entries=self.chain().entries[: k + 1]), self.trees)
        else:
            at = support
        basis = execution_basis(at, spec, claims, runner_class)
        if basis is None:
            raise ValueError(f"{o.id}: nothing may run (an unusable declaration or an undesignated class)")
        key = RunnerKey(self.home, self.ledger_id, runner_class)
        provider = self.providers[runner_class]
        declared = at.s.specs.declaration(spec)
        run_id = secrets.token_hex(16)
        n = support.s.n
        execution = {**basis, "runner": {"class": runner_class, "key": key.key_id},
                     "attributes": [list(a) for a in provider.attributes], "pins": [],
                     "unpinnable": not basis["observes_outside_reads"], "start": n, "end": n}
        view = at.s.view
        target = {"spec": {"unit": spec, "rev": view.rev(spec)}, "claim": [{"unit": c, "rev": view.rev(c)} for c in claims]}
        crashed = self._record(key, target, {**execution, "incomplete": "CRASHED"}, at, spec, None, run_id)
        self.journal.attempt(o.id, self.wall())
        self.journal.exec_intent(run_id, o.id, self._hold_key(o, spec), crashed)
        try:
            ws = self.workspaces.materialize(self.ledger_id, self.trees(basis["tree"]))
        except MaterializeRefused:
            record = self._record(key, target, {**execution, "incomplete": "FAILED_TO_START"}, at, spec, None, run_id)
            return self._finish(run_id, "FAILED_TO_START", record, {})
        self.journal.exec_started(run_id, ws.run_id)  # where a restart finds its outputs (review of cc7abfed, B2)
        found = self.sandbox.execute(ws, self.trees(basis["tree"]), provider,
                                     effective_bound_hours(declared, "DISPATCHER") * 3600)
        # an exception above leaves the workspace and the open execution for recover, outputs and all
        incomplete, outcome, objects = found.incomplete, found.outcome, {}
        if incomplete is None and outcome_problems(declared, outcome):
            incomplete, outcome = "MALFORMED_OUTPUT", None  # every declared output once, each canonical (§17.3)
        refs = []
        if incomplete is not None and found.raw is not None:
            refs = [self._keep(found.raw)]  # a failing outcome written before the end stays visible (F114)
        done = execution if incomplete is None else {**execution, "incomplete": incomplete}
        record = self._record(key, target, done, at, spec, outcome, run_id, refs, objects)
        decision = self._finish(run_id, incomplete, record, objects)
        self.workspaces.remove(ws)
        return decision

    def _finish(self, run_id: str, incomplete: str | None, record: dict[str, Any], objects: dict[str, str]) -> Any:
        """The request journaled, then the execution ended, then the request sent (B1's order)."""

        signed, rid = self._request(record, objects)
        self.journal.exec_ended(run_id, incomplete)
        return self._send(signed, rid)

    def _record(self, key: RunnerKey, target: dict[str, Any], execution: dict[str, Any], at: Any, spec: str,
                outcome: dict[str, Any] | None, run_id: str, refs: list[dict[str, Any]] = (),
                objects: dict[str, str] | None = None) -> dict[str, Any]:
        from ssds.core.api.v1 import canonical_json

        fields: dict[str, Any] = {"execution": execution, "configuration": run_configuration(at, spec)}
        if outcome is not None:
            text = canonical_json(outcome).decode()
            digest = "sha256:" + hashlib.sha256(text.encode()).hexdigest()
            fields["evaluated"] = digest
            if objects is not None:
                objects[digest] = text
        latest = self._latest()
        return _with_id({"kind": "REALIZATION", "schema": 1, "ruleset": dict(latest.h.ruleset(latest.n)),
                        "actor": f"machinery:runner@{key.key_id}", "actor_class": "MACHINERY", "frame": "ADMITTED",
                        "target": target, "basis": [], "outcome": "INCOMPLETE" if "incomplete" in execution else "COMPLETE",
                        "reason": [], "supersedes": [], "binding": None, "governs": dict(self.governs),
                        "provenance": {"run": run_id}, "refs": list(refs), "recorded_at": self.recorded_at(),
                        "fields": fields})

    def _keep(self, raw: bytes) -> dict[str, Any]:
        digest = "sha256:" + hashlib.sha256(raw).hexdigest()
        self.home.create_private(self.home.artifact_parts(self.ledger_id, digest), raw)
        return {"store": "RUNNER", "digest": digest, "media_type": "application/json"}

    def _request(self, record: dict[str, Any], objects: dict[str, str] | None = None) -> tuple[dict[str, Any], str]:
        """The record's request, signed by its runner key and journaled (``REQUEST``) before it is sent."""

        s = self._latest()
        request = {"binding": None, "claims": [], "base_position": s.n, "base_commit": s.h.head(s.n),
                   "candidates": [], "adopted_deltas": [], "records": [record], "objects": dict(objects or {})}
        key_class = record["fields"]["execution"]["runner"]["class"]
        signed = RunnerKey(self.home, self.ledger_id, key_class).sign(request)
        return signed, self.journal.submitted(signed)

    def _send(self, signed: dict[str, Any], rid: str) -> Any:
        decision = self.submit(signed)
        self.journal.decided(rid)
        return decision

    def _latest(self) -> Any:
        return derive(self.chain(), self.trees).s

    # -- recovery --------------------------------------------------------------------------------------------

    def recover(self) -> list[Any]:
        """After a restart (review of cc7abfed, B1 and B2): an undecided request is resubmitted by identity; an
        execution intended and never ended, whose request was never journaled, is submitted ``INCOMPLETE
        CRASHED``, once, its surviving ``outputs.json`` kept as a native artifact the record references and its
        workspace removed (§6.9; F114)."""

        from ssds.admission.request import request_id

        out = []
        for request in self.journal.undecided():
            out.append(self.submit(request))  # Admission answers a decided request by its recorded decision
            self.journal.decided(request_id(request))
        requested = {(r.get("provenance") or {}).get("run") for e in self.journal.entries() if e["kind"] == "REQUEST"
                     for r in e["request"].get("records") or []}
        started = {e["run_id"]: e.get("workspace") for e in self.journal.entries() if e["kind"] == "EXEC_STARTED"}
        for intent in self.journal.open_executions():
            run_id = intent["run_id"]
            if run_id in requested:  # its request is journaled (and answered above): it only ends here
                self.journal.exec_ended(run_id, None)
                continue
            record = dict(intent["record"])
            workspace = started.get(run_id)
            raw = self.workspaces.surviving_outputs(self.ledger_id, workspace) if workspace else None
            if raw is not None:
                record = _with_id({**record, "refs": [*record.get("refs", []), self._keep(raw)]})
            out.append(self._finish(run_id, "CRASHED", record, {}))
            if workspace:
                self.workspaces.remove_run(self.ledger_id, workspace)
        return out


def _with_id(record: Mapping[str, Any]) -> dict[str, Any]:
    """The record with its identity, ``sha256(JCS(record without id))``: the ledger's ``record_id``, which the
    dispatcher may not import (fitness); a test pins the two equal."""

    from ssds.core.api.v1 import canonical_json

    body = {k: v for k, v in record.items() if k != "id"}
    return {**body, "id": "sha256:" + hashlib.sha256(canonical_json(body)).hexdigest()}


__all__ = ["Budget", "Executor", "Run", "RunnerKey"]
