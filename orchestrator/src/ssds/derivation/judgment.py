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

from functools import cached_property, lru_cache
from typing import Any

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

    def same_work(self, adverse_id: str, rid: str) -> bool:
        """Judgments about work reach by judged content; without it, only their own target."""

        return self.s.record(adverse_id)["target"] == self.s.record(rid)["target"]

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
        target = record["target"]
        subject = None
        if isinstance(target, dict):
            subject = target.get("subject")
            if isinstance(subject, dict):
                subject = subject.get("subject")
            subject = subject or target.get("unit")
        structure = self.s.view.structure
        return structure.domain(subject) if subject and subject in structure.units else None

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
        return frozenset({UNKNOWN})

    def work_authors(self, rid: str) -> frozenset[str]:
        """Until frames supply ``W``, the producing task's lineage stands for the work's authors."""

        target = self.s.record(rid)["target"]
        makers = self.s._makers(target.get("transformation", "")) if "transformation" in target else []
        return frozenset(makers) or frozenset({UNKNOWN})

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

    @lru_cache(maxsize=None)  # noqa: B019
    def nonind(self, rid: str) -> bool:
        """The S0 fact that the record had a requirement and was not independent at admission."""

        s = self.s
        record = s.record(rid)
        if record["kind"] not in REQUIREMENT or record["actor_class"] == "MACHINERY":
            return False
        if record["kind"] in ("EQUIVALENCE", "COMPLETENESS", "INTAKE_DISPOSITION") and record["actor_class"] == "ADMISSION":
            return False
        authors = self.judged_authors(rid)
        if record["actor_class"] == "HUMAN":
            if record["actor"] not in authors:
                return False
            return not self._non_authorship_attested(rid)
        binding = record["binding"] or {}
        if binding.get("lineage_class") not in ("ATTESTED_FRESH", "HUMAN_ATTESTED_FRESH"):
            return True
        lineage = set(binding.get("lineage") or [record["actor"]])
        return UNKNOWN in authors or bool(lineage & authors)

    def _non_authorship_attested(self, rid: str) -> bool:
        position = self.s.position_of(rid)
        return any(self.s.record(a)["target"].get("record") == rid and self.s.position_of(a) == position
                   and self.s.record(a)["actor"] == self.s.record(rid)["actor"]
                   for a in self.s.of_kind("NON_AUTHORSHIP_ATTESTATION"))


__all__ = ["ADVERSE", "Judgments", "PASSING", "REQUIREMENT", "adverse", "is_work", "passing"]
