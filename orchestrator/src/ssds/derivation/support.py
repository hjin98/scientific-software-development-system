"""S2, the support tier: one least fixed point with the support-cycle clamp (catalogue §5.5-§5.6).

Values lie in ``F < P < T``. Derivation instantiates the static support graph
of the state, forces every node of every non-trivial strongly connected
component to ``F`` before evaluating anything, then evaluates the remaining
nodes once, dependencies first. Nodes are ``("current", record)`` and
``("valid", subject)``.
"""

from __future__ import annotations

from collections.abc import Callable
from functools import cached_property, lru_cache
from typing import Any

from .assessment import Assessments
from .frames import Frame, frame_of, frame_state, role_sat, transformation_of
from .judgment import Judgments
from .outcomes import PASSING, covers
from .s0 import nontrivial, strongly_connected
from .state import ACCEPTANCE_KINDS, HUMAN_FLOOR, F, P, State, T, triple_key

Node = tuple[str, str]

#: Kinds whose currency S2 evaluates (support-tier judgments and observations).
EVALUATED = frozenset(PASSING) | {"TASK_RESULT", "REALIZATION", "CHECK_EXECUTION", "EXTERNAL_CONSULTATION",
                                  "ANALYZER_OUTPUT", "AVAILABILITY", "CUSTODY_ENUMERATION", "INTAKE_CLASSIFICATION",
                                  "RECONSTRUCTION_PROPOSAL", "LINEAGE_ATTESTATION", "NON_AUTHORSHIP_ATTESTATION"}


class Support:
    """The S2 values of one state."""

    def __init__(self, state: State, judgments: Any = None, assessments: Any = None) -> None:
        self.s = state
        # §5.10 and §6 are the one owners of what base and the evidence term read.
        self.j = judgments or Judgments(state)
        self.a = assessments or Assessments(state, self.j)

    # -- base (S0/S1 constants) ------------------------------------------------------------

    def base(self, rid: str) -> int:
        s = self.s
        if not s.acts(rid) or s.superseded(rid) or s.status1(rid) in ("REVOKED", "BLOCKED") or not s.cont(rid) \
                or not s.tgt(rid) or self.j.vetoed(rid) or self.j.nonind(rid):
            return F
        return P if s.status1(rid) == "PROVISIONAL" else T

    def passing(self, rid: str) -> bool:
        record = self.s.record(rid)
        return PASSING.get(record["kind"]) == record["outcome"]

    # -- the static support graph (§5.6) ----------------------------------------------------

    def equivalences(self, unit: str) -> list[str]:
        return [rid for rid in self.s.of_kind("EQUIVALENCE")
                if self.passing(rid) and self.s.record(rid)["target"]["unit"] == unit]

    def deps(self, node: Node) -> set[Node]:
        kind, key = node
        out: set[Node] = set()
        if kind == "current":
            for entry in self.s.record(key)["basis"]:
                mode, target = entry["mode"], entry["target"]
                if mode in ("content", "validity"):
                    out.update(("current", q) for q in self.equivalences(target["unit"]))
                    if mode == "validity":
                        subject = self.s.view.structure.subj(target["unit"])
                        if subject:
                            out.add(("valid", subject))
                elif mode == "execution":
                    for unit_entry in target.get("units", []):
                        out.update(("current", q) for q in self.equivalences(unit_entry["unit"]))
                    out.update(("current", c) for c in target.get("bounded_by", []) if c in self.s.records)
                elif mode == "record" and target["record"] in self.s.records:
                    out.add(("current", target["record"]))
            return out
        subject = key
        for rid in self.acceptances(subject) + self.required_judgments(subject):
            out.add(("current", rid))
        for rid in self.gate_decisions(subject):
            out.add(("current", rid))
        out.update(("current", rid) for rid in self.a.support_nodes(subject))
        return out

    @cached_property
    def nodes(self) -> list[Node]:
        out: list[Node] = [("current", rid) for rid, fact in self.s.records.items()
                           if fact.record["kind"] in EVALUATED]
        out += [("valid", u) for u, unit in self.s.view.structure.units.items() if unit.subject]
        return sorted(out)

    @cached_property
    def _solution(self) -> tuple[dict[Node, int], tuple[frozenset[Node], ...]]:
        graph = {node: self.deps(node) for node in self.nodes}
        edges = {(a, b) for a, targets in graph.items() for b in targets if b in graph}
        values: dict[Node, int] = {}
        forced: list[frozenset[Node]] = []
        for component in strongly_connected(graph, edges):  # dependencies are emitted before dependents
            if nontrivial(component, edges):
                forced.append(component)
                values.update((node, F) for node in component)
                continue
            (node,) = component
            values[node] = self._evaluate(node, values.__getitem__)
        return values, tuple(forced)

    def static_deps(self, node: Node) -> set[Node]:
        """§5.6's static support graph (reading F24): the evaluation graph's edges, plus every equivalence judgment
        on a unit an entry names and every acceptance or gate decision naming the subject, whatever its value. An
        acceptance from an ended tenure is left out: it can never count again (§1.6, §19.4)."""

        s = self.s
        out = set(self.deps(node))
        kind, key = node
        if kind == "current":
            for entry in s.record(key)["basis"]:
                target = entry["target"]
                units = [target.get("unit")] if entry["mode"] in ("content", "validity") else \
                    [u.get("unit") for u in target.get("units", [])] if entry["mode"] == "execution" else []
                for unit in units:
                    out.update(("current", q) for q in s.of_kind("EQUIVALENCE") if s.record(q)["target"]["unit"] == unit)
            return out
        tenure = s.tenure(key)
        for rid in s.of_kind(*{k for kinds in ACCEPTANCE_KINDS.values() for k in kinds}):
            target = s.record(rid)["target"]
            if target.get("subject") != key:
                continue
            record = s.record(rid)
            pending = record["frame"] != "ADMITTED" and s.enactment(record["frame"]["transformation"]) not in s.integrated
            if tenure is not None and s.position_of(rid) < tenure and not pending \
                    and not self.binds_tenure(rid, key, tenure):
                continue  # an ended tenure's acceptance; one in a pending frame may yet count (check 87e908d)
            out.add(("current", rid))
        out.update(("current", rid) for rid in s.of_kind("GATE_DECISION")
                   if (_triple_of(s.record(rid)["target"]["subject"]) or ("",))[0] == key)
        return out

    @cached_property
    def static_forced(self) -> tuple[frozenset[Node], ...]:
        """The non-trivial components of the static graph: what Admission keeps from appearing or growing
        (§8.3 step 5, ``CYCLE_SUPPORT``). S2's forcing and ``SUPPORT_CYCLE`` read the evaluation graph."""

        graph = {node: self.static_deps(node) for node in self.nodes}
        edges = {(a, b) for a, targets in graph.items() for b in targets if b in graph}
        return tuple(c for c in strongly_connected(graph, edges) if nontrivial(c, edges))

    def grows_a_cycle(self, before: Support) -> bool:
        """§8.3 step 5 (reading F24): this state's static graph has a non-trivial component that is no subset of
        one ``before`` has, so a cycle appears or one grows. A cycle absorbed content made, in both, is neither."""

        return any(not any(component <= c for c in before.static_forced) for component in self.static_forced)

    @property
    def values(self) -> dict[Node, int]:
        return self._solution[0]

    @property
    def forced(self) -> tuple[frozenset[Node], ...]:
        """Every non-trivial support component, forced to F (§5.6); each is an S3 finding."""

        return self._solution[1]

    def current(self, rid: str) -> int:
        return self.values.get(("current", rid), F)

    def valid(self, subject: str) -> int:
        """``valid(s)``; a part routes to its subject."""

        owner = self.s.view.structure.subj(subject)
        return self.values.get(("valid", owner), F) if owner else F

    # -- evaluation of one node --------------------------------------------------------------

    def _evaluate(self, node: Node, value: Callable[[Node], int]) -> int:
        kind, key = node
        if kind == "current":
            result = self.base(key)
            for entry in self.s.record(key)["basis"]:
                if result == F:
                    break
                result = min(result, self.sat(entry, value, key))
            return result
        return self._valid(key, value)

    def sat(self, entry: dict[str, Any], value: Callable[[Node], int], rid: str | None = None,
            frame: Frame | None = None) -> int:
        """``sat(e)`` for basis entry ``e`` of record ``rid``, whose frame gives a content entry's role; ``frame``
        stands for it when the record is no node here (Admission's step 6, reading F26)."""

        mode, target, cls = entry["mode"], entry["target"], entry["class"]
        if mode == "identity":
            return T
        if mode == "standing":
            return self.base(target["record"]) if target["record"] in self.s.records else F
        if mode == "record":
            return value(("current", target["record"])) if target["record"] in self.s.records else F
        if mode in ("content", "validity"):
            content = self.content(target["unit"], target["rev"], cls, value)
            frame = frame if frame is not None else self.frame_of(rid)
            if frame is not None and mode == "content":
                in_frame = self.s.frame is not None and self.s.frame.x.id == frame.x.id
                content = role_sat(frame, target["unit"], target["rev"], in_frame, content)
            if mode == "content" or content == F:
                return content
            subject = self.s.view.structure.subj(target["unit"])
            return min(content, value(("valid", subject))) if subject else F
        if mode == "execution":
            return self.execution(target, value)
        return F

    def stale_entries(self, record: dict[str, Any], frame: Frame | None = None) -> list[int]:
        """Catalogue §8.3 step 6 (readings F10, F26): the positions of ``record``'s basis entries that are not
        satisfied (value ``F``) in this state, read entry by entry from its values. ``record`` is no node here, so
        a record or subject it alone would make current counts as ``F``, and ``frame`` gives its entries' roles."""

        def value(node: Node) -> int:
            return self.values.get(node, F)

        return [i for i, entry in enumerate(record.get("basis") or []) if self.sat(entry, value, None, frame) == F]

    @lru_cache(maxsize=None)  # noqa: B019
    def frame_support(self, transformation: str) -> Support | None:
        """The values of ``D_n[X]`` at this head (``frame_state``), or ``None`` when ``X`` is unknown here or its
        frame does not exist."""

        framed = frame_state(self.s.h, self.s.n, transformation, self.s)
        return Support(framed) if framed is not None else None

    def transformation_frame(self, transformation: str) -> Frame | None:
        """The frame ``X``'s records' roles are computed in at this head: fixed at ``k - 1`` once ``X`` is
        integrated (reading F17)."""

        return self._frames(transformation)

    def frame_of(self, rid: str | None) -> Frame | None:
        """The frame a frame record's roles are computed in (§7.3)."""

        if rid is None or self.s.record(rid)["frame"] == "ADMITTED":
            return None
        transformation = self.s.record(rid)["frame"]["transformation"]
        if self.s.frame is not None and self.s.frame.x.id == transformation:
            return self.s.frame
        return self._frames(transformation)

    @lru_cache(maxsize=None)  # noqa: B019
    def _frames(self, transformation: str) -> Frame | None:
        x = transformation_of(self.s, transformation)
        return frame_of(self.s, x) if x else None  # reading F17

    def content(self, unit: str, rev: str, cls: str, value: Callable[[Node], int]) -> int:
        """``sat(content (u, r, k))``: the current revision, or the widest current equivalence path (§4.4)."""

        if unit not in self.s.view.structure.units:
            return F
        current = self.s.cur(unit)
        if current == rev:
            return T
        if cls == "PLAN_CONTROL" and self.s.plans.tightens_to_current(unit, rev):
            return T  # the one rule-defined coverage order: control tightening (§4.4, §13.4)
        best = {rev: T}
        frontier = [rev]
        while frontier:  # widest (max-min) path, visiting no revision twice along a path
            source = frontier.pop()
            for q in self.equivalences(unit):
                target = self.s.record(q)["target"]
                if target["from"] != source or not covers(target["class"], cls):
                    continue
                width = min(best[source], value(("current", q)))
                if width > best.get(target["to"], F):
                    best[target["to"]] = width
                    frontier.append(target["to"])
        return best.get(current, F)

    def execution(self, basis: dict[str, Any], value: Callable[[Node], int]) -> int:
        """``sat(execution E)`` (§4.1): re-resolve each recorded term; reads and widened entries by identity."""

        return self.a.execution_current(basis, lambda u, r: self.content(u, r, "CONSUMER:REALIZATION", value), value)

    # -- validity (§5.5) ----------------------------------------------------------------------

    def acceptances(self, subject: str) -> list[str]:
        """``ACC(s)``: passing acceptances of the mode on exactly the current triple, within the tenure."""

        s = self.s
        if subject not in s.view.structure.units:
            return []
        kinds = ACCEPTANCE_KINDS.get(s.mode(subject), ())
        scope_id, rev = s.view.scope_id(subject), s.cur(subject)
        tenure = s.tenure(subject)
        out = []
        for rid in s.of_kind(*kinds):
            record = s.record(rid)
            target = record["target"]
            if not self.passing(rid) or (target["subject"], target["scope_id"], target["rev"]) != (subject, scope_id, rev):
                continue
            if (tenure is None or s.position_of(rid) < tenure) and not self.binds_tenure(rid, subject, tenure):
                continue
            if self.qualified(record, s.view.structure.domain(subject)):
                out.append(rid)
        return out

    def binds_tenure(self, rid: str, subject: str, tenure: int | None) -> bool:
        """``bind(j) = τ(s)`` for a prospective acceptance made in a frame (§7.6).

        ``j`` counts for the tenure an integration ``k`` starts iff ``k`` integrates
        ``j``'s own enactment with the same proposed structure, ``j``'s basis
        holds in ``D_{k-1}[X]``, and ``j`` has counted for no earlier tenure.
        """

        s = self.s
        record = s.record(rid)
        if record["frame"] == "ADMITTED" or tenure is None:
            return False
        made_in = record["frame"]["transformation"]
        x0 = transformation_of(s, made_in)
        enactment = s.enactment(made_in)
        if x0 is None or enactment is None:
            return False
        delta0 = Frame(s.h, s.position_of(rid), x0, enactment).structure_delta
        for k in sorted(p for p in s.h.integrations if s.position_of(rid) < p <= s.n):
            integration = s.h.integrations[k]
            if not integration.transformation or s.enactment(integration.transformation) != enactment:
                continue
            frame = frame_state(s.h, k - 1, integration.transformation, State(s.h, k - 1))
            if frame is None or frame.frame.structure_delta != delta0:
                continue
            if State(s.h, k).tenure(subject) != k:
                continue
            if Support(frame).current(rid) == 0:
                continue
            return k == tenure  # the first such admission is bind(j)
        return False

    def prospectively_accepted(self, transformation: str, subject: str) -> bool:
        """§7.6's enactment condition before the integrating admission: some prospective acceptance would count
        for the tenure that integrating ``X`` starts for ``subject``. That is, a passing ``ACCEPTANCE`` made in a
        frame of ``X``'s own enactment, with the same proposed structure, naming ``subject``'s triple in
        ``D_n[X]``, current there (its basis holding, acting, independent), and counted for no earlier tenure
        (``X``'s enactment has integrated nothing). ``binds_tenure``'s conditions 1-4, read at the head that
        the integration would follow (Phase F 4c-iii)."""

        s = self.s
        enactment = s.enactment(transformation)
        if enactment is None or enactment in s.integrated:
            return False
        framed = frame_state(s.h, s.n, transformation, s)
        if framed is None:
            return False
        triple = {"subject": subject, "scope_id": framed.view.scope_id(subject), "rev": framed.cur(subject)} \
            if subject in framed.view.structure.units else None
        support = Support(framed)
        for rid in s.of_kind("ACCEPTANCE"):
            record = s.record(rid)
            if record["frame"] == "ADMITTED" or record["outcome"] != "PASS" or record["target"] != triple:
                continue
            made_in = record["frame"]["transformation"]
            x0 = transformation_of(s, made_in)
            if x0 is None or s.enactment(made_in) != enactment:
                continue
            if Frame(s.h, s.position_of(rid), x0, enactment).structure_delta != framed.frame.structure_delta:
                continue
            if support.current(rid) != 0:
                return True
        return False

    def qualified(self, record: dict[str, Any], domain: str | None) -> bool:
        kind = record["kind"]
        if (kind in HUMAN_FLOOR or (kind == "ACCEPTANCE" and domain in ("D1", "D2"))) and record["actor_class"] != "HUMAN":
            return False
        if kind == "LEGACY_ACCEPTANCE":
            return True
        acceptors = self.s.policy.get(domain, "acceptors", None)
        if acceptors is None or kind != "ACCEPTANCE":
            return True
        return record["actor"] in acceptors or f"class:{record['actor_class']}" in acceptors

    def required_judgments(self, subject: str) -> list[str]:
        kinds = self.s.policy.get(self.s.view.structure.domain(subject), "required_judgments")
        triple = self.s.subject_triple(subject)
        return [rid for rid in self.s.of_kind(*kinds) if self.passing(rid)
                and _triple_of(self.s.record(rid)["target"]) == triple]

    def gate_decisions(self, subject: str) -> list[str]:
        triple = self.s.subject_triple(subject)
        return [rid for rid in self.s.of_kind("GATE_DECISION") if self.passing(rid)
                and _triple_of(self.s.record(rid)["target"]["subject"]) == triple]

    def gterm(self, subject: str, gate: str, value: Callable[[Node], int]) -> int:
        """The gate term: the minimum over every eligible decision, ``F`` when none is eligible (§5.5)."""

        eligible = self.eligible_gate_decisions(subject, gate)
        if not eligible:
            return F
        return min(min(value(("current", rid)), P if self.s.record(rid)["fields"]["qualification"] == "QUALIFIED" else T)
                   for rid in eligible)

    def eligible_gate_decisions(self, subject: str, gate: str) -> list[str]:
        """``elig``: the passing gate decisions on the subject's current triple that may count for ``gate`` (§5.5)."""

        holders = self.s.policy.get(self.s.view.structure.domain(subject), "gate_holders", None)
        # For a NATIVE D1/D2 subject the gate obligation G derives carries its run rid_G(s) (§5.5 elig, §10.2):
        # a new run's gate decides afresh, so a decision of an earlier run is not eligible in it.
        by_run = self.s.mode(subject) == "NATIVE" and self.s.view.structure.kind(subject) in ("D1", "D2")
        run = self.s.runs.rid(subject) if by_run else None
        eligible = [rid for rid in self.gate_decisions(subject)
                    if self.s.record(rid)["target"]["gate"] == gate and self.s.acts(rid) and not self.s.superseded(rid)
                    and self.s.record(rid)["actor_class"] == "HUMAN"
                    and (holders is None or self.s.record(rid)["actor"] in holders)
                    and (not by_run or self.s.runs.named(rid, subject) == run)]
        return eligible

    def ok(self, subject: str) -> bool:
        return self.s.s0.well_formed(subject) and subject not in self.s.s0.affected_subjects

    def _valid(self, subject: str, value: Callable[[Node], int]) -> int:
        s = self.s
        triple = self.s.subject_triple(subject)
        status = s.status1(triple_key(*triple))
        result = F if status in ("REVOKED", "BLOCKED") else (P if status == "PROVISIONAL" else T)
        if result == F or not self.ok(subject):
            return F
        domain = s.view.structure.domain(subject)
        best = F
        for rid in self.acceptances(subject):
            term = value(("current", rid))
            for kind in s.policy.get(domain, "required_judgments"):
                term = min(term, max([value(("current", q)) for q in self.required_judgments(subject)
                                      if s.record(q)["kind"] == kind] or [F]))
            for gate in s.policy.get(domain, "gates"):
                term = min(term, self.gterm(subject, gate, value))
            for obligation in s.evidence.required(subject):
                term = min(term, self.a.ev(subject, obligation, value, self.base, self.j.nonind))
            best = max(best, term)
        return min(result, best, self.a.qual(subject, value, self.base, self.j.nonind))


def _triple_of(target: dict[str, Any]) -> tuple[str, str, str] | None:
    if isinstance(target, dict) and {"subject", "scope_id", "rev"} <= set(target):
        return target["subject"], target["scope_id"], target["rev"]
    return None
