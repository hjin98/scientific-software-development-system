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

from ssds.ledger.read import submits

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
        domains = {structure.domain(u) for u in self._policy_units(record) if u in structure.units}
        return domains.pop() if len(domains) == 1 else None

    def _policy_units(self, record: dict[str, Any]) -> list[str]:
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
        return units

    def judged_units(self, record: dict[str, Any]) -> list[str]:
        """Every unit the record judged, for the chain class: the union over everything it judged (reviews
        799d1ba and c5a6457 B4), never its first piece only. A work judgment's units; a plan acceptance's items;
        a realization's claim; an assessment's realization; every record a record target names, transitively (an
        immateriality's assessments included); a completeness's or integrated result's scope; a report's units;
        or a subject. Empty when none can be determined. One worklist with a visited set: linear in the records
        reached, at any depth (re-checks 00fb3cb and c23f3ce)."""

        units: set[str] = set()
        pending, seen = [record], set()
        while pending:
            current = pending.pop()
            own, referenced = self._own_units(current)
            units |= own
            for r in referenced:
                if isinstance(r, str) and r in self.s.records and r not in seen:
                    seen.add(r)
                    pending.append(self.s.record(r))
        return sorted(units)

    def own_subjects(self, record: dict[str, Any]) -> frozenset[str]:
        """A record's own subjects (reading F22): the subjects of every unit it judges. It never holds a ``validity``
        entry on one (catalogue §4.1, §8.5; ``DEP_OWN_SUBJECT``)."""

        structure = self.s.view.structure
        return frozenset(structure.subj(u) for u in self.judged_units(record) if u in structure.units) - {None}

    def _own_units(self, record: dict[str, Any]) -> tuple[set[str], list[Any]]:
        """The units ``record`` itself names, and the records its target names."""

        target = record["target"]
        units: set[str] = set()
        if is_work(record):
            units |= set(self._policy_units(record))
        elif record["kind"] == "PLAN_ACCEPTANCE":
            units |= {i["unit"] for i in record["fields"]["items"]}
        if not isinstance(target, dict):
            return units, []
        claim = target.get("claim")
        if isinstance(claim, list):
            units |= {c["unit"] for c in claim if isinstance(c, dict) and isinstance(c.get("unit"), str)}
        listed = target.get("scope", target.get("units"))
        if isinstance(listed, list):
            units |= {u for u in listed if isinstance(u, str)}
        subject = target.get("subject")
        if isinstance(subject, dict):
            subject = subject.get("subject")
        units |= {u for u in (subject, target.get("unit")) if isinstance(u, str) and u}
        return units, [target.get("realization"), target.get("record"), *(target.get("records") or [])]

    # -- independence (§5.10 (f)) ----------------------------------------------------------------

    def judged_authors(self, rid: str, at: int | None = None) -> frozenset[str]:
        """The authors of what the record judged, by its kind (§5.10 (b)). With ``at``, as the ledger knew them
        at that position, with the record's judged content pinned there: the inputs of its classification at
        admission (§5.10 (a); plan review 409c2f7 B1, B4)."""

        s = self.s
        record = s.record(rid)
        target = record["target"]
        kind = record["kind"]
        authors = self._authors_for(record, at)
        if kind in ("ACCEPTANCE", "REVIEW") and "subject" in target and isinstance(target["subject"], str):
            return authors(target["subject"], target["rev"])
        if kind == "EQUIVALENCE":
            return authors(target["unit"], target["from"]) | authors(target["unit"], target["to"])
        if kind == "COMPLETENESS":
            view = s.view if at is None else s.h.view(at)
            candidate = {u: r for u, r in self._candidate_pieces(record)} if at is not None else {}
            out: set[str] = set()
            for unit in target["scope"]:
                if unit in candidate:  # a frame completeness judges the candidate's member, not the admitted one
                    out |= authors(unit, candidate[unit])
                elif unit in view.structure.units:
                    out |= authors(unit, view.rev(unit))
            return frozenset(out) or frozenset({UNKNOWN})
        if kind == "ADJUDICATION":
            return self.root_authors(rid, at)
        if is_work(record):
            return self._authors_of(sorted(self.judged_content(rid)), authors)
        if kind == "PLAN_ACCEPTANCE":
            return self._authors_of([(i["unit"], i["rev"]) for i in record["fields"]["items"]], authors)
        if kind == "EVIDENCE_ASSESSMENT":
            return self._claim_authors(rid, authors)
        if kind == "REALIZATION" and isinstance(target.get("claim"), list):
            # an observation at a chain's root: the authors of the content it ran on (§5.10 (e))
            return self._authors_of([(c["unit"], c["rev"]) for c in target["claim"]], authors)
        if kind == "IMMATERIALITY":
            out = set()
            for covered in target["records"]:
                if covered in s.records:
                    out |= self._claim_authors(covered, authors)
            return frozenset(out) or frozenset({UNKNOWN})
        return frozenset({UNKNOWN})

    def _authors_for(self, record: dict[str, Any], at: int | None):
        """``authors(u, r)`` for judging ``record``: in this state, or, for its classification, as of ``at``. One
        rule for every kind (plan review 8a41539 R-B1): the producers of ``(u, r)`` in every admitted view at or
        before ``at``, and, for a piece a candidate the record is about produces, that transformation's makers
        too (§5.10 (b): "a revert, restore or re-application that re-produced it included"); ``UNKNOWN`` when
        nothing recorded produced it."""

        produced = self._candidate_pieces(record)
        position = self.s.n if at is None else at
        return lambda unit, rev: self.piece_authors(unit, rev, position, produced)

    def piece_authors(self, unit: str, rev: str, position: int,
                      produced: dict[tuple[str, str], frozenset[str]] | None = None) -> frozenset[str]:
        """The one authorship rule every reader applies, classification and routing alike (§5.10 (b):
        "Authorship is a ledger fact, read the same way by every rule"; plan review 6e0fa9e NB-1): whoever
        produced ``(unit, rev)`` in an admitted view at or before ``position``, and, when a candidate produces
        it, that candidate's makers (``produced``); ``UNKNOWN`` when nothing recorded produced it."""

        admitted = _earlier_producers(self.s.h, unit, rev, position)
        made = (produced or {}).get((unit, rev))
        if made is None:
            return admitted or frozenset({UNKNOWN})
        return made | admitted

    def transformation_authors(self, transformation: str) -> frozenset[str]:
        """The authors of what an answer judging a transformation would judge, by the one rule."""

        judged, produced = self._transformation_work(transformation, None)
        return self._authors_of(sorted(judged), lambda u, r: self.piece_authors(u, r, self.s.n, produced))

    def _candidate_pieces(self, record: dict[str, Any]) -> dict[tuple[str, str], frozenset[str]]:
        """The pieces of the candidate a record is about (it declares the candidate's frame, or judges its
        transformation), with their makers."""

        frame, target = record.get("frame"), record.get("target") or {}
        transformation = frame.get("transformation") if isinstance(frame, dict) else None
        if transformation is None and isinstance(target, dict) and isinstance(target.get("transformation"), str):
            transformation = target["transformation"]
        if isinstance(transformation, str):
            return self._transformation_work(transformation, None)[1]
        return {}

    def _authors_of(self, pieces: list[tuple[str, str]], authors=None) -> frozenset[str]:
        authors = authors or self.s.authors
        out: set[str] = set()
        for unit, rev in pieces:
            out |= authors(unit, rev)
        return frozenset(out) or frozenset({UNKNOWN})

    def _claim_authors(self, assessment: str, authors=None) -> frozenset[str]:
        realization = self.s.record(assessment)["target"]["realization"]
        if realization not in self.s.records:
            return frozenset({UNKNOWN})
        return self._authors_of([(c["unit"], c["rev"]) for c in self.s.record(realization)["target"]["claim"]], authors)

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
            producers[(unit, rev)] = makers | _earlier_producers(s.h, unit, rev, base) if unit in frame.changed \
                else before.authors(unit, rev)
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

    def _submitting(self, transformation: str) -> list[str]:
        """The results that submit ``X`` (§7.1, ``submits``), in ledger order: a result naming ``id(X)`` without
        submitting it fixes no binding, scope or base (review dcae3e9)."""

        return [r for r in self.s.of_kind("TASK_RESULT")
                if self.s.record(r)["target"].get("transformation") == transformation
                and submits(self.s.record(r)["target"])]

    def _binding(self, transformation: str) -> dict[str, Any]:
        found = self._submitting(transformation)
        return dict(self.s.record(found[0])["binding"] or {}) if found else {}

    def _makers(self, transformation: str) -> list[str]:
        return self.s._makers(transformation)

    def binding_conflicts(self, transformation: str) -> bool:
        """Two producing contexts for one ``(B, C, A)``: a later result under another scope or key (§7.1 row)."""

        contexts = set()
        for result in self._submitting(transformation):
            binding = self.s.record(result)["binding"] or {}
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
        submitted = min((self.s.position_of(r) for r in self._submitting(x.id)), default=self.s.n)
        candidates = [k for k in range(min(submitted, self.s.n) + 1) if self.s.h.head(k) == x.base]
        return max(candidates) if candidates else None

    def _position_of_state(self, digest: str) -> int | None:
        for entry in self.s.h.chain.entries[: self.s.n + 1]:
            if entry.digest == digest:
                return entry.position
        return None

    def root_authors(self, rid: str, at: int | None = None) -> frozenset[str]:
        s = self.s
        current, seen = rid, set()
        while current in s.records and current not in seen:
            seen.add(current)
            record = s.record(current)
            if record["kind"] not in ("CHALLENGE", "ADJUDICATION", "WITHDRAWAL", "RISK_OVERRIDE"):
                return self.judged_authors(current, at)
            key = target_key(record["target"])
            if key is None:
                return frozenset({UNKNOWN})
            if key.startswith("triple:"):
                _, subject, _scope, rev = key.split(":", 3)
                return self._authors_for(record, at)(subject, rev)
            current = key
        return frozenset({UNKNOWN})

    def chain_needs_human(self, challenge: str) -> bool:
        """The chain of ``challenge`` has class R3, so only a human adjudicates it (catalogue §3.4 "R2, or R3
        (Serious Challenge, D1/D2 claims)", §5.10 (e), §12.4, §3.5): the challenge is serious; or a support-tier or
        adjudication record on the chain, the root included, is a human's (challenges carry no class); or the root
        is about a D1 or D2 claim. The walk stops at the root, the first record or triple that is not
        challenge-tier (review 8d274c4 B4, N1). The one owner judge selection and Admission both read."""

        s = self.s
        if challenge in s.records and (s.record(challenge).get("fields") or {}).get("serious"):
            return True
        seen: set[str] = set()
        current: Any = challenge
        while isinstance(current, str) and current in s.records and current not in seen:
            seen.add(current)
            record = s.record(current)
            if record["kind"] != "CHALLENGE" and record["actor_class"] == "HUMAN":
                return True
            if record["kind"] not in ("CHALLENGE", "ADJUDICATION", "WITHDRAWAL", "RISK_OVERRIDE"):
                return self._about_d1_d2(self.judged_units(record))  # the root
            key = target_key(record["target"])
            if key is not None and key.startswith("triple:"):
                return self._about_d1_d2([key.split(":", 3)[1]])
            current = key
        return True  # no root reached: fail closed

    def _about_d1_d2(self, units: list[str]) -> bool:
        """Any judged unit lies in D1 or D2; failing closed when the units cannot be determined or a unit is not
        declared (review 799d1ba B4)."""

        structure = self.s.view.structure
        if not units or any(u not in structure.units for u in units):
            return True
        return any(structure.domain(u) in ("D1", "D2") for u in units)

    def requirement(self, record: dict[str, Any]) -> bool:
        """Whether the record carries an independence requirement (catalogue §5.10 (a) "Requirement"): the kinds
        of ``REQUIREMENT`` and every disposition of a failing assessment, never a machinery record."""

        if record["actor_class"] == "MACHINERY":
            return False
        if record["kind"] in ("EQUIVALENCE", "COMPLETENESS", "INTAKE_DISPOSITION") and record["actor_class"] == "ADMISSION":
            return False
        return record["kind"] in REQUIREMENT or self.disposes_failing(record)

    def disposes_failing(self, record: dict[str, Any]) -> bool:
        """A disposition of a failing assessment (§6.7), which carries an independence requirement (§6.8)."""

        return bool(self.disposed_failures(record))

    def disposed_failures(self, record: dict[str, Any]) -> list[str]:
        """Every failing assessment the record disposes of (§6.7): each a reassessment's supersession chain reaches,
        at any depth (plan review 409c2f7 B2; review of e643fa07, B1); an ``IMMATERIALITY`` covering them; an
        ``UPHELD`` adjudication
        of a challenge targeting one or its realization, "the only premises whose revocation discredits the
        observation" (§6.7; SD-48)."""

        s = self.s

        def failing(rid: Any) -> bool:
            return isinstance(rid, str) and rid in s.records and s.record(rid)["kind"] == "EVIDENCE_ASSESSMENT" \
                and s.record(rid)["outcome"] == "FAIL"

        kind, target = record["kind"], record["target"] or {}
        if kind == "EVIDENCE_ASSESSMENT":
            frontier, seen, found = list(record.get("supersedes") or []), set(), []
            while frontier:
                x = frontier.pop()
                if not isinstance(x, str) or x in seen or x not in s.records:
                    continue
                seen.add(x)
                if failing(x):
                    found.append(x)
                if s.record(x)["kind"] == "EVIDENCE_ASSESSMENT":
                    frontier.extend(s.record(x).get("supersedes") or [])
            return sorted(found)
        if kind == "IMMATERIALITY":
            return [x for x in target.get("records", []) if failing(x)]
        if kind == "ADJUDICATION" and record["outcome"] == "UPHELD":
            challenge = target.get("record")
            if challenge in s.records and s.record(challenge)["kind"] == "CHALLENGE":
                under = (s.record(challenge)["target"] or {}).get("record")
                if failing(under):
                    return [under]
                if under in s.records and s.record(under)["kind"] == "REALIZATION":
                    return [a for a in s.of_kind("EVIDENCE_ASSESSMENT")
                            if failing(a) and s.record(a)["target"].get("realization") == under]
        return []

    def _claim_domain(self, assessment: str, at: int) -> str | None:
        """The domain whose policy owns a failing assessment's claim, as of ``at``."""

        realization = self.s.record(assessment)["target"]["realization"]
        if realization not in self.s.records:
            return None
        structure = self.s.h.view(at).structure
        domains = {structure.domain(c["unit"]) for c in self.s.record(realization)["target"]["claim"]
                   if c["unit"] in structure.units}
        return domains.pop() if len(domains) == 1 else None

    def _owner_exception(self, record: dict[str, Any], authors: frozenset[str], at: int) -> bool:
        """SD-48 at admission: the record disposes of failing assessments, and for each its actor is that claim's
        owner with no qualified human outside that claim's authors, under the policy in force at ``at``."""

        failures = self.disposed_failures(record)
        policy = self._policy_at(at)
        authors_at = self._authors_for(record, at)
        # it holds only for every failure disposed of, each in its own claim's domain against that claim's authors
        # (SD-48; plan review b8a1800 B2): an owner's IMMATERIALITY reaches no other domain's failure
        return bool(failures) and all(
            owner_exception(policy, record["actor"], self._claim_authors(f, authors_at), self._claim_domain(f, at))
            for f in failures)

    @lru_cache(maxsize=None)  # noqa: B019
    def _policy_at(self, at: int) -> Any:
        from .state import Policy

        return Policy.parse(self.s.h.objects.get(self.s.h.ruleset(at)["policy"]))

    @lru_cache(maxsize=None)  # noqa: B019
    def _classified(self, rid: str) -> tuple[bool, bool]:
        """``(nonind, common_mode)``, classified once from the facts at the record's admission position (§5.10 (a):
        "fixed at admission"): its binding, its judged content and their authors as the ledger knew them there,
        a candidate's content authored by its transformation's makers, and the policy then in force."""

        s = self.s
        record = s.record(rid)
        if not self.requirement(record):
            return False, False
        at = s.position_of(rid)
        authors = self.judged_authors(rid, at)
        if self._independent(record, authors):
            return False, False
        exception = self._owner_exception(record, authors, at)
        return not exception, exception

    def nonind(self, rid: str) -> bool:
        """The S0 fact that the record had a requirement and was not independent at admission (§5.10 (a))."""

        return self._classified(rid)[0]

    def common_mode(self, rid: str) -> bool:
        """Admitted as independent only under the owner exception: its common-mode dependency on the authors,
        shown in the inspector view (§5.10 (a), SD-48)."""

        return self._classified(rid)[1]

    def _independent(self, record: dict[str, Any], authors: frozenset[str]) -> bool | None:
        """The independence test, or ``None`` when it fails and only the owner exception could hold."""

        if record["actor_class"] == "HUMAN":
            # §5.10 (f): judged content of unknown authorship admits only a human with a non-authorship attestation
            # (re-check 6e0fa9e NB-3)
            if (record["actor"] not in authors and UNKNOWN not in authors) or self._non_authorship_attested(record["id"]):
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


#: Kinds whose supersession target (catalogue §5.10 (b), "Supersession target") is conditional: a plan acceptance's
#: is its target only while its step 6 basis holds. Not built at Admission yet: it fails closed (plan §3.1, 4b-i).
CONDITIONAL_SUPERSESSION = frozenset({"PLAN_ACCEPTANCE"})


def supersession_target(record: dict[str, Any]) -> Any:
    """What a record's superseder must judge (catalogue §5.10 (b), "Supersession target"), or ``None`` when that
    target is conditional (``CONDITIONAL_SUPERSESSION``). The column, not the wider "reach" one:
    - an acceptance or a subject review: the same triple, in any frame or tenure;
    - a gate decision: the same gate and triple, in any frame, tenure or run (its evidence core may differ);
    - an assessment: the same realization and obligation under the same reading (§6.7: "an explicit
      reassessment of the realization");
    - a completeness: its target without the analyzer (a machinery record's analyzer is its ``tgt`` condition);
    - every other kind, a transformation review, conformance and equivalence included: its target (§3.4)."""

    kind, target = record["kind"], record["target"] or {}
    if kind in CONDITIONAL_SUPERSESSION:
        return None
    if kind == "COMPLETENESS":
        return ("target", json.dumps({k: v for k, v in target.items() if k != "analyzer"}, sort_keys=True))
    if kind in ("ACCEPTANCE", "REVIEW") and isinstance(target.get("subject"), str):
        return ("triple", target.get("subject"), target.get("scope_id"), target.get("rev"))
    if kind == "GATE_DECISION":
        subject = target.get("subject") or {}
        return ("gate", target.get("gate"), subject.get("subject"), subject.get("scope_id"), subject.get("rev"))
    if kind == "EVIDENCE_ASSESSMENT":
        return ("assessment", target.get("realization"), target.get("obligation"),
                json.dumps((record.get("fields") or {}).get("reading"), sort_keys=True))
    return ("target", json.dumps(target, sort_keys=True))


def _earlier_producers(history: Any, unit: str, rev: str, position: int) -> frozenset[str]:
    """Who produced ``(unit, rev)`` in admitted views at or before ``position``, none when no admitted view did:
    a candidate that restores a revision has its makers and every earlier producer of it as authors (§5.10 (b):
    "a revert, restore or re-application that re-produced it included"; plan review b8a1800 B1)."""

    if not any(k <= position for k, _ in history.productions.get((unit, rev), ())):
        return frozenset()
    return history.authors(unit, rev, position)


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
        # a human outside the known authors can answer content of unknown authorship by presenting a
        # NON_AUTHORSHIP_ATTESTATION, which classification then requires (§5.10 (f)): eligible, never stranded
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
