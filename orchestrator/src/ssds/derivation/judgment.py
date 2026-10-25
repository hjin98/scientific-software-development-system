"""Judgment disagreement: the one owner of reach, vetoes, relief and independence (Manual §5.10; catalogue §5.10).

Everything here reads only S0 and S1 facts, so ``base`` stays an S2 constant
and the support system stays monotone (§5.6).

Phase D scope: the subject- and name-keyed kinds (acceptance, subject-triple
review, gate decision, equivalence chains, completeness unions, product scope,
intake disposition). Plan-acceptance reach needs the control-tightening order
of §13.4 (Phase E); until then a rejection vetoes every acceptance naming any
revision of the same item, which over-approximates the settled reach.
Judgments about work, whose reach and independence read ``W`` (§5.10 (b)),
are added with frames.
"""

from __future__ import annotations

import json

from dataclasses import dataclass
from functools import cached_property, lru_cache
from typing import Any

from .frames import Frame, Transformation, transformation_of
from .outcomes import ADVERSE, PASSING, adverse, covers, passing
from .state import UNKNOWN, State, target_key, triple_key

#: Kinds whose records carry an independence requirement (§5.10 (f)); machinery records never do.
REQUIREMENT = frozenset({"REVIEW", "CONFORMANCE", "ACCEPTANCE", "PLAN_ACCEPTANCE", "EQUIVALENCE", "COMPLETENESS",
                         "INTAKE_DISPOSITION", "IMMATERIALITY", "ADJUDICATION"})


def is_work(record: dict[str, Any]) -> bool:
    """A judgment about work: a transformation's review or conformance, or an integrated-result review."""

    return record["kind"] in ("REVIEW", "CONFORMANCE") and ("transformation" in record["target"]
                                                             or "integrated" in record["target"])


class Judgments:
    def __init__(self, state: State) -> None:
        self.s = state

    # -- asserting and standing (S0/S1) ------------------------------------------------------

    def asserts(self, rid: str) -> bool:
        s = self.s
        return (s.acts(rid) and not s.superseded(rid) and s.status1(rid) not in ("REVOKED", "BLOCKED")
                and s.cont(rid) and s.tgt(rid) and not self.nonind(rid))

    def stands(self, rid: str) -> bool:
        """A disposing record stands: acts, unsuperseded, CLEAR, held and independent."""

        s = self.s
        return s.acts(rid) and not s.superseded(rid) and s.status1(rid) == "CLEAR" and s.cont(rid) and not self.nonind(rid)

    @lru_cache(maxsize=None)  # noqa: B019
    def stands_adverse(self, rid: str) -> bool:
        """``stands⁻``: no standing supersession chain (routes 1-2) and no upheld challenge (route 4)."""

        s = self.s
        frontier, seen = list(s.supersessions.get(rid, [])), set()
        while frontier:
            d = frontier.pop()
            if d in seen:
                continue
            seen.add(d)
            if self.stands(d):
                return False
            frontier.extend(s.supersessions.get(d, []))
        for c in s.targeting.get(rid, []):
            if s.record(c)["kind"] != "CHALLENGE":
                continue
            for a in s.targeting.get(c, []):
                record = s.record(a)
                if record["kind"] == "ADJUDICATION" and record["outcome"] == "UPHELD" and s.in_force(a) \
                        and s.cont(a) and not self.contested(a):
                    return False
        return True

    def contested(self, rid: str) -> bool:
        s = self.s
        return any(s.record(c)["kind"] == "CHALLENGE" and s.record(c)["fields"]["blocking"] and s.open(c)
                   for c in s.targeting.get(rid, []))

    # -- reach (§5.10 (c)) ----------------------------------------------------------------------

    @cached_property
    def adverse_by_kind(self) -> dict[str, list[str]]:
        out: dict[str, list[str]] = {}
        for rid, fact in self.s.records.items():
            if adverse(fact.record):
                out.setdefault(fact.record["kind"], []).append(rid)
        return out

    def same(self, adverse_id: str, rid: str) -> bool:
        a, z = self.s.record(adverse_id), self.s.record(rid)
        kind = a["kind"]
        if kind != z["kind"]:
            return False
        if is_work(a) or is_work(z):
            return self.same_work(adverse_id, rid)
        if kind in ("ACCEPTANCE", "REVIEW", "PRODUCT_SCOPE_ACCEPTANCE", "INTAKE_DISPOSITION"):
            return a["target"] == z["target"]
        if kind == "GATE_DECISION":
            return (a["target"]["gate"], a["target"]["subject"]) == (z["target"]["gate"], z["target"]["subject"])
        if kind == "EQUIVALENCE":
            return self._on_chain(a, rid)
        if kind == "COMPLETENESS":
            return self._needed_in_union(a, rid)
        if kind == "PLAN_ACCEPTANCE":
            named = {i["unit"] for i in a["fields"]["items"]}
            return bool(named & {i["unit"] for i in z["fields"]["items"]})
        return False

    def reaches_target(self, adverse_id: str, kind: str, target: Any) -> bool:
        """Whether an adverse judgment's reach includes ``target`` asked of a judgment of ``kind`` (§5.10 (c)),
        before any answer to it exists: the reach a brief's carried objections follow (§16.5)."""

        a = self.s.record(adverse_id)
        if a["kind"] != kind or not isinstance(target, dict):
            return False
        if is_work(a) or (kind in ("REVIEW", "CONFORMANCE") and ("transformation" in target or "integrated" in target)):
            judged = self.judged_content(adverse_id)
            if not judged or not is_work(a) or not ("transformation" in target or "integrated" in target):
                return a["target"] == target
            return judged <= self._target_work(json.dumps(target, sort_keys=True))[0]
        if kind in ("ACCEPTANCE", "REVIEW", "PRODUCT_SCOPE_ACCEPTANCE", "INTAKE_DISPOSITION"):
            return a["target"] == target
        if kind == "GATE_DECISION":
            return (a["target"]["gate"], a["target"]["subject"]) == (target.get("gate"), target.get("subject"))
        if kind == "PLAN_ACCEPTANCE":
            return bool({i["unit"] for i in a["fields"]["items"]} & {i["unit"] for i in target.get("items", [])})
        return False

    def same_work(self, adverse_id: str, rid: str) -> bool:
        """``z`` is reached when ``W(z)`` contains a nonempty ``W(j⁻)`` at the same content (§5.10 (c))."""

        a, z = self.s.record(adverse_id), self.s.record(rid)
        if not (is_work(a) and is_work(z)):
            return a["target"] == z["target"]
        judged = self.judged_content(adverse_id)
        if not judged:
            return a["target"] == z["target"]
        return judged <= self.judged_content(rid)

    def _on_chain(self, a: dict[str, Any], rid: str) -> bool:
        """``z`` lies on a chain of asserting equivalences joining ``a``'s two revisions, read either way."""

        unit, cls = a["target"]["unit"], a["target"]["class"]
        edges: dict[str, list[tuple[str, str]]] = {}
        for q in self.s.of_kind("EQUIVALENCE"):
            t = self.s.record(q)["target"]
            if t["unit"] != unit or not passing(self.s.record(q)) or not (covers(t["class"], cls) or t["class"] == cls):
                continue
            if q != rid and not self.asserts(q):
                continue
            edges.setdefault(t["from"], []).append((t["to"], q))
            edges.setdefault(t["to"], []).append((t["from"], q))
        goal = a["target"]["to"]
        stack: list[tuple[str, frozenset[str], bool]] = [(a["target"]["from"], frozenset({a["target"]["from"]}), False)]
        while stack:  # simple paths only: no revision visited twice
            node, visited, used = stack.pop()
            if node == goal:
                if used:
                    return True
                continue
            for nxt, q in edges.get(node, ()):
                if nxt not in visited:
                    stack.append((nxt, visited | {nxt}, used or q == rid))
        return False

    def _member_revisions(self, rid: str) -> dict[str, str]:
        return {e["target"]["unit"]: e["target"]["rev"] for e in self.s.record(rid)["basis"] if e["mode"] == "content"}

    def _needed_in_union(self, a: dict[str, Any], rid: str) -> bool:
        """``z`` is needed in some union of asserting judgments covering ``a``'s scope, at the same member revisions."""

        scope, classes = set(a["target"]["scope"]), a["target"]["classes"]
        adverse_revs = self._member_revisions(a["id"])
        z = self.s.record(rid)["target"]

        def compatible(q: str) -> bool:
            t = self.s.record(q)["target"]
            revs = self._member_revisions(q)
            return t["classes"] == classes and set(t["scope"]) <= scope and \
                all(adverse_revs.get(u, r) == r for u, r in revs.items() if u in scope)

        if not compatible(rid):
            return False
        others = [set(self.s.record(q)["target"]["scope"]) for q in self.s.of_kind("COMPLETENESS")
                  if q != rid and passing(self.s.record(q)) and compatible(q) and self.asserts(q)]
        mine = set(z["scope"])
        for x in mine:
            without_x = set().union(*[o for o in others if x not in o]) if others else set()
            if scope <= mine | without_x:
                return True
        return False

    @lru_cache(maxsize=None)  # noqa: B019
    def vetoed(self, rid: str) -> bool:
        z = self.s.record(rid)
        if not passing(z):
            return False
        for adverse_id in self.adverse_by_kind.get(z["kind"], []):
            if self.same(adverse_id, rid) and self.stands_adverse(adverse_id) and not self.relieved(adverse_id, rid):
                return True
        return False

    def relieved(self, adverse_id: str, rid: str) -> bool:
        """Route 3: the adverse judgment's author's or the owner's passing judgment on ``z``'s exact target."""

        a, z = self.s.record(adverse_id), self.s.record(rid)
        if not (is_work(a) or a["kind"] == "PLAN_ACCEPTANCE"):
            return False
        owner = self.owner(a)
        for y in self.s.of_kind(a["kind"]):
            record = self.s.record(y)
            if passing(record) and record["target"] == z["target"] and record["actor"] in (a["actor"], owner) \
                    and self.stands(y):
                return True
        return False

    def owner(self, record: dict[str, Any]) -> str | None:
        """The actor policy names to adjudicate disagreements in the target's domain (§5.10 (e))."""

        return self.s.policy.get(self.domain_of(record), "owner", None)

    def domain_of(self, record: dict[str, Any]) -> str | None:
        """The domain whose policy owns the record's disagreements: of what it judged (§5.10 (e))."""

        structure = self.s.view.structure
        target = record["target"]
        units: list[str] = []
        if is_work(record):
            units = sorted(u for u, _ in self.judged_content(record["id"])) if record["id"] in self.s.records else []
            if not units and "transformation" in target:
                units = sorted(self._binding(target["transformation"]).get("write_scope") or [])
            units = units or list(target.get("scope", []))
        elif record["kind"] == "PLAN_ACCEPTANCE":
            units = [i["unit"] for i in record["fields"]["items"]]
        elif record["kind"] in ("EVIDENCE_ASSESSMENT", "IMMATERIALITY"):
            assessment = record["id"] if record["kind"] == "EVIDENCE_ASSESSMENT" else (target["records"] or [None])[0]
            realization = self.s.record(assessment)["target"]["realization"] if assessment in self.s.records else None
            if realization in self.s.records:
                units = [c["unit"] for c in self.s.record(realization)["target"]["claim"]]
        elif isinstance(target, dict):
            subject = target.get("subject")
            if isinstance(subject, dict):
                subject = subject.get("subject")
            units = [u for u in (subject or target.get("unit"),) if u]
        domains = {structure.domain(u) for u in units if u in structure.units}
        return domains.pop() if len(domains) == 1 else None

    # -- independence (§5.10 (f)) ----------------------------------------------------------------

    def judged_authors(self, rid: str) -> frozenset[str]:
        """The authors of what the record judged, by its kind (§5.10 (b))."""

        s = self.s
        record = s.record(rid)
        target = record["target"]
        kind = record["kind"]
        if kind in ("ACCEPTANCE", "REVIEW") and "subject" in target and isinstance(target["subject"], str):
            return s.authors(target["subject"], target["rev"])
        if kind == "EQUIVALENCE":
            return s.authors(target["unit"], target["from"]) | s.authors(target["unit"], target["to"])
        if kind == "COMPLETENESS":
            out: set[str] = set()
            for unit in target["scope"]:
                if unit in s.view.structure.units:
                    out |= s.authors(unit, s.cur(unit))
            return frozenset(out) or frozenset({UNKNOWN})
        if kind == "ADJUDICATION":
            return self.root_authors(rid)
        if is_work(record):
            return self.work_authors(rid)
        if kind == "PLAN_ACCEPTANCE":
            return self._authors_of([(i["unit"], i["rev"]) for i in record["fields"]["items"]])
        if kind == "EVIDENCE_ASSESSMENT":
            return self._claim_authors(rid)
        if kind == "IMMATERIALITY":
            out: set[str] = set()
            for covered in target["records"]:
                if covered in s.records:
                    out |= self._claim_authors(covered)
            return frozenset(out) or frozenset({UNKNOWN})
        return frozenset({UNKNOWN})

    def _authors_of(self, pieces: list[tuple[str, str]]) -> frozenset[str]:
        out: set[str] = set()
        for unit, rev in pieces:
            out |= self.s.authors(unit, rev)
        return frozenset(out) or frozenset({UNKNOWN})

    def _claim_authors(self, assessment: str) -> frozenset[str]:
        realization = self.s.record(assessment)["target"]["realization"]
        if realization not in self.s.records:
            return frozenset({UNKNOWN})
        return self._authors_of([(c["unit"], c["rev"]) for c in self.s.record(realization)["target"]["claim"]])

    def work_authors(self, rid: str) -> frozenset[str]:
        authors: set[str] = set()
        for unit, rev in self.judged_content(rid):
            authors |= self._work_producers(rid).get((unit, rev), frozenset({UNKNOWN}))
        return frozenset(authors) or frozenset({UNKNOWN})

    # -- judged content of work (§5.10 (b)) ----------------------------------------------------------

    def _work(self, rid: str) -> tuple[frozenset[tuple[str, str]], dict[tuple[str, str], frozenset[str]]]:
        """``W(j)`` for a judgment about work, and the producers of each piece of it."""

        return self._target_work(json.dumps(self.s.record(rid)["target"], sort_keys=True))

    @lru_cache(maxsize=None)  # noqa: B019
    def _target_work(self, target_json: str) -> tuple[frozenset[tuple[str, str]], dict[tuple[str, str], frozenset[str]]]:
        """``W`` of a work target (a transformation or an integrated result), whether or not it is judged yet."""

        s = self.s
        target = json.loads(target_json)
        if "transformation" in target:
            return self._transformation_work(target["transformation"], None)
        position = self._position_of_state(target["at"])
        if position is None:
            return frozenset(), {}
        at = State(s.h, position)
        if target["integrated"] == "ITEM":
            work = self._changed_by(lambda k: self._key_of(k) == target["of"], position)
        else:
            work = self._changed_by(lambda k: s.h.integrations[k].transformation in set(target["changes"]), position)
        scope = set(target.get("scope", at.view.structure.units))
        judged = frozenset((u, at.cur(u)) for u in work & scope if u in at.view.structure.units)
        return judged, {piece: at.authors(*piece) for piece in judged}

    def _transformation_work(self, transformation: str, head: int | None) -> tuple[frozenset[tuple[str, str]], dict]:
        """``W`` of a transformation: fixed by ``id(X)`` at its base, or recomputed over ``M_n(X)`` at ``head``."""

        s = self.s
        x = transformation_of(s, transformation)
        binding = self._binding(transformation)
        if x is None:
            return frozenset(), {}
        base = head if head is not None else self._base_position(x)
        if base is None:
            return frozenset(), {}
        frame = Frame(s.h, base, x, s.enactment(transformation))
        if frame.merged is None:
            return frozenset(), {}
        key = binding.get("item_key")
        work = set(frame.changed) | (self._changed_by(lambda k: key is not None and self._key_of(k) == key, base)
                                     if key else set())
        scope = set(binding.get("write_scope") or frame.structure.units)
        judged = frozenset((u, frame.view.rev(u)) for u in work & scope if u in frame.structure.units)
        before = State(s.h, base)
        makers = frozenset(self._makers(transformation)) or frozenset({UNKNOWN})
        producers = {}
        for unit, rev in judged:
            producers[(unit, rev)] = makers if unit in frame.changed else before.authors(unit, rev)
        return judged, producers

    def judged_content(self, rid: str) -> frozenset[tuple[str, str]]:
        return self._work(rid)[0]

    def _work_producers(self, rid: str) -> dict[tuple[str, str], frozenset[str]]:
        return self._work(rid)[1]

    def supports_integration(self, rid: str, head: int) -> bool:
        """A judgment of ``X`` supports an integration at ``head`` only for the content it judged (§5.10 (b))."""

        target = self.s.record(rid)["target"]
        if "transformation" not in target:
            return False
        return self._transformation_work(target["transformation"], head)[0] == self.judged_content(rid)

    def _binding(self, transformation: str) -> dict[str, Any]:
        for result in self.s.of_kind("TASK_RESULT"):
            record = self.s.record(result)
            if record["target"].get("transformation") == transformation:
                return dict(record["binding"] or {})
        return {}

    def _makers(self, transformation: str) -> list[str]:
        return self.s._makers(transformation)

    def binding_conflicts(self, transformation: str) -> bool:
        """Two producing contexts for one ``(B, C, A)``: a later result under another scope or key (§7.1 row)."""

        contexts = set()
        for result in self.s.of_kind("TASK_RESULT"):
            record = self.s.record(result)
            if record["target"].get("transformation") == transformation:
                binding = record["binding"] or {}
                contexts.add((tuple(sorted(binding.get("write_scope") or ())), binding.get("item_key")))
        return len(contexts) > 1

    def _key_of(self, position: int) -> str | None:
        transformation = self.s.h.integrations[position].transformation
        return self._binding(transformation).get("item_key") if transformation else None

    def _changed_by(self, select, through: int) -> set[str]:
        """Units an admitted integration selected by ``select`` changed, at or before ``through``."""

        h = self.s.h
        out: set[str] = set()
        for k in sorted(h.integrations):
            if k > through or k == 0 or not select(k):
                continue
            before, after = h.view(k - 1), h.view(k)
            for unit in after.structure.units:
                if unit not in before.structure.units or before.rev(unit) != after.rev(unit):
                    out.add(unit)
        return out

    def _base_position(self, x: Transformation) -> int | None:
        submitted = min((self.s.position_of(r) for r in self.s.of_kind("TASK_RESULT")
                         if self.s.record(r)["target"].get("transformation") == x.id), default=self.s.n)
        candidates = [k for k in range(min(submitted, self.s.n) + 1) if self.s.h.head(k) == x.base]
        return max(candidates) if candidates else None

    def _position_of_state(self, digest: str) -> int | None:
        for entry in self.s.h.chain.entries[: self.s.n + 1]:
            if entry.digest == digest:
                return entry.position
        return None

    def root_authors(self, rid: str) -> frozenset[str]:
        s = self.s
        current, seen = rid, set()
        while current in s.records and current not in seen:
            seen.add(current)
            record = s.record(current)
            if record["kind"] not in ("CHALLENGE", "ADJUDICATION", "WITHDRAWAL", "RISK_OVERRIDE"):
                return self.judged_authors(current)
            key = target_key(record["target"])
            if key is None:
                return frozenset({UNKNOWN})
            if key.startswith("triple:"):
                _, subject, _scope, rev = key.split(":", 3)
                return s.authors(subject, rev)
            current = key
        return frozenset({UNKNOWN})

    def requirement(self, record: dict[str, Any]) -> bool:
        """Whether the record carries an independence requirement (catalogue §5.10 (a) "Requirement"): the kinds
        of ``REQUIREMENT`` and every disposition of a failing assessment, never a machinery record."""

        if record["actor_class"] == "MACHINERY":
            return False
        if record["kind"] in ("EQUIVALENCE", "COMPLETENESS", "INTAKE_DISPOSITION") and record["actor_class"] == "ADMISSION":
            return False
        return record["kind"] in REQUIREMENT or self.disposes_failing(record)

    def disposes_failing(self, record: dict[str, Any]) -> bool:
        """A disposition of a failing assessment (§6.7): a reassessment superseding one, an ``IMMATERIALITY``
        covering one, or an adjudication whose challenge chain is rooted at one."""

        s = self.s

        def failing(rid: Any) -> bool:
            return isinstance(rid, str) and rid in s.records and s.record(rid)["kind"] == "EVIDENCE_ASSESSMENT" \
                and s.record(rid)["outcome"] == "FAIL"

        kind, target = record["kind"], record["target"]
        if kind == "EVIDENCE_ASSESSMENT":
            return any(failing(x) for x in record.get("supersedes") or [])
        if kind == "IMMATERIALITY":
            return any(failing(x) for x in (target or {}).get("records", []))
        if kind == "ADJUDICATION":
            return failing(self.root(record["id"]))
        return False

    def root(self, rid: str) -> str | None:
        """The first record that is not challenge-tier on the record's chain of targets (§5.10 (e))."""

        s = self.s
        current, seen = rid, set()
        while current in s.records and current not in seen:
            seen.add(current)
            record = s.record(current)
            if record["kind"] not in ("CHALLENGE", "ADJUDICATION", "WITHDRAWAL", "RISK_OVERRIDE"):
                return current
            key = target_key(record["target"])
            if key is None or key.startswith("triple:"):
                return None
            current = key
        return None

    @staticmethod
    def at_admission(history: Any, position: int) -> "Judgments":
        """The judgments of the admitted state at ``position``, built once per history (as ``Workflow.historical``)."""

        cache = history.__dict__.setdefault("_judgments_at", {})
        found = cache.get(position)
        if found is None:
            found = cache[position] = Judgments(State(history, position))
        return found

    def common_mode(self, rid: str) -> bool:
        """The record was admitted as independent only under the owner exception: its common-mode dependency on
        the authors, shown in the inspector view (catalogue §5.10 (a))."""

        s = self.s
        at = s.position_of(rid)
        if s.frame is not None or s.n != at:
            return Judgments.at_admission(s.h, at).common_mode(rid)
        record = s.record(rid)
        return self.requirement(record) and self._independent(record, self.judged_authors(rid)) is None \
            and self._owner_exception(record, self.judged_authors(rid))

    def _owner_exception(self, record: dict[str, Any], authors: frozenset[str]) -> bool:
        return self.disposes_failing(record) and owner_exception(self.s.policy, record["actor"], authors,
                                                                 self.domain_of(record))

    @lru_cache(maxsize=None)  # noqa: B019
    def nonind(self, rid: str) -> bool:
        """The S0 fact that the record had a requirement and was not independent at admission (§5.10 (a)): it is
        classified once, in the admitted state at the record's own admission position, so no later state changes
        it (plan review b10018de B4)."""

        s = self.s
        at = s.position_of(rid)
        if s.frame is not None or s.n != at:
            return Judgments.at_admission(s.h, at).nonind(rid)
        record = s.record(rid)
        if not self.requirement(record):
            return False
        authors = self.judged_authors(rid)
        independent = self._independent(record, authors)
        if independent is None:
            return not self._owner_exception(record, authors)
        return not independent

    def _independent(self, record: dict[str, Any], authors: frozenset[str]) -> bool | None:
        """The independence test, or ``None`` when it fails and only the owner exception could hold."""

        if record["actor_class"] == "HUMAN":
            if record["actor"] not in authors or self._non_authorship_attested(record["id"]):
                return True
            return None
        binding = record["binding"] or {}
        if binding.get("lineage_class") not in ("ATTESTED_FRESH", "HUMAN_ATTESTED_FRESH"):
            return None
        lineage = set(binding.get("lineage") or [record["actor"]])
        if UNKNOWN in authors or UNKNOWN in lineage or lineage & authors:  # an open closure is never disjoint
            return None
        return True

    def _non_authorship_attested(self, rid: str) -> bool:
        position = self.s.position_of(rid)
        return any(self.s.record(a)["target"].get("record") == rid and self.s.position_of(a) == position
                   and self.s.record(a)["actor"] == self.s.record(rid)["actor"]
                   for a in self.s.of_kind("NON_AUTHORSHIP_ATTESTATION"))


# -- ending routes, per route and per state (§5.10 (e), (f); A1, SD-51) --------------------------------


@dataclass(frozen=True)
class Routes:
    admissible: frozenset[str]

    @property
    def waiting(self) -> bool:
        """No eligible independent judge for any route here: the objection waits, with human attention."""

        return not self.admissible


def owner_exception(policy: Any, judge: str, authors: frozenset[str], domain: str | None) -> bool:
    """SD-48: the claim's owner may dispose of a failing assessment when no qualified human is outside its authors.
    The one definition both the routes and the admission-time classification read."""

    humans = set(policy.get(domain, "humans", ()))
    outside = {h for h in humans if h not in authors}
    return judge.startswith("human:") and judge == policy.get(domain, "owner", None) and (not outside or UNKNOWN in authors)


def _is_agent(actor: str) -> bool:
    return actor.startswith("agent:")


class RouteEligibility:
    """Which records could end a standing objection that vetoes a passing judgment, in one state."""

    def __init__(self, judgments: Judgments) -> None:
        self.j = judgments
        self.s = judgments.s

    def independent(self, judge: str, authors: frozenset[str], domain: str | None = None) -> bool:
        if _is_agent(judge):
            if judge in self.s.policy.get(domain, "unattested_agents", ()):
                return False  # its route cannot attest a fresh lineage (§12.2)
            return UNKNOWN not in authors and judge not in authors  # a fresh attested lineage, disjoint
        if not judge.startswith("human:"):
            return False
        return judge not in authors

    def owner_exception(self, judge: str, authors: frozenset[str], domain: str | None) -> bool:
        return owner_exception(self.s.policy, judge, authors, domain)

    def acts(self, frame: Any) -> bool:
        """Whether a record declaring ``frame`` would act in this state (§5.2)."""

        if frame == "ADMITTED":
            return True
        task = self.s.enactment(frame["transformation"])
        if task is not None and task in self.s.integrated:
            return True
        return self.s.frame is not None and task is not None and task == self.s.frame.enactment

    def frame_judging(self, record: dict[str, Any]) -> Any:
        """A record about a transformation declares its frame (§7.5); every other route record the admitted one."""

        return record["frame"] if is_work(record) and "transformation" in record["target"] else "ADMITTED"

    def routes(self, adverse_id: str, vetoed_id: str, basis_holds: Any = None) -> Routes:
        s = self.s
        a, z = s.record(adverse_id), s.record(vetoed_id)
        domain = self.j.domain_of(a)
        owner = s.policy.get(domain, "owner", None)
        adjudicators = list(s.policy.get(domain, "adjudicators", [owner] if owner else []))
        objected = self.j.judged_authors(adverse_id)
        reached = self.j.judged_authors(vetoed_id)
        failing = a["kind"] == "EVIDENCE_ASSESSMENT"
        supersession_acts = self.acts(self.frame_judging(a))
        out: set[str] = set()

        def can(judge: str | None, authors: frozenset[str]) -> bool:
            if judge is None:
                return False
            return self.independent(judge, authors, domain) or (failing and self.owner_exception(judge, authors, domain))

        if a["actor_class"] == "HUMAN" and supersession_acts and can(a["actor"], objected):
            out.add("1:reassessment")
        if supersession_acts and can(owner, objected):
            out.add("2:owner-supersession")
        if is_work(a) or a["kind"] == "PLAN_ACCEPTANCE":
            holds = basis_holds(vetoed_id) if basis_holds else True
            relief_acts = self.acts(self.frame_judging(z))
            if holds and relief_acts:
                if a["actor_class"] == "HUMAN" and self.independent(a["actor"], reached, domain):
                    out.add("3:relief-by-author")
                if owner and self.independent(owner, reached, domain):
                    out.add("3:relief-by-owner")
        if failing and can(owner, objected):
            out.add("immateriality-by-owner")
        if any(can(judge, objected) for judge in adjudicators):
            out.add("4:upheld-challenge")
        return Routes(frozenset(out))


__all__ = ["ADVERSE", "Judgments", "PASSING", "REQUIREMENT", "RouteEligibility", "Routes", "adverse", "is_work",
           "passing"]
