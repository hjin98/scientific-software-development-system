"""A scenario builder for derivation tests: a genesis over fixture trees, then admitted entries.

Each scenario produces the authenticated chain derivation receives and the
trees its entries name; tests then query the real ``ssds.derivation`` owner.
"""

from __future__ import annotations

import hashlib
from typing import Any

from ssds.content import Structure, TreeView, decl_to_json
from ssds.derivation import derive

from ._fixtures import (
    RULESET,
    absorption_body,
    admission_body,
    chain_of,
    genesis_body,
    lifecycle_body,
    record,
    structure_of,
    tree,
)

HUMAN = "human:SHA256:alice"
HUMAN_B = "human:SHA256:bob"
OWNER = "human:SHA256:owner"


def agent(name: str) -> str:
    return f"agent:{name}/1"


def fresh(actor: str, task: str = "task", lineage: list[str] | None = None, **extra: Any) -> dict:
    return {"task": task, "obligation": "obl", "role": "IMPLEMENTER", "lineage": lineage or [actor],
            "lineage_class": "ATTESTED_FRESH", **extra}


class Scenario:
    def __init__(self, manifest: str, files: dict[str, str], *, modes: dict | None = None, policy: str | None = None) -> None:
        self.trees: dict[str, Any] = {}
        self.objects: dict[int, dict[str, bytes]] = {}
        base = tree(files, manifest)
        self.head = self.add_tree(base)
        self.structure = structure_of(base)
        ruleset = dict(RULESET)
        if policy is not None:
            data = policy.encode("utf-8")
            digest = "sha256:" + hashlib.sha256(data).hexdigest()
            ruleset["policy"] = digest
            self.objects[0] = {digest: data}
        all_subjects = {u: {"mode": "NATIVE", "ruleset": "ssds-rules/1"} for u, unit in self.structure.units.items()
                        if unit.subject}
        all_subjects["*"] = {"mode": "NATIVE", "ruleset": "ssds-rules/1"}
        self.entries = [genesis_body(self.head, decl_to_json(self.structure.decl), {**all_subjects, **(modes or {})}, ruleset)]
        self.files = dict(files)
        self.manifest = manifest

    def add_tree(self, t) -> str:
        identity = hashlib.sha1(repr(sorted((p, e.mode, e.data) for p, e in t.items())).encode()).hexdigest()
        self.trees[identity] = t
        return identity

    def view(self, head: str | None = None) -> TreeView:
        return TreeView(self.trees[head or self.head], Structure(self.structure.decl))

    def triple(self, subject: str, head: str | None = None) -> dict:
        v = self.view(head)
        return {"subject": subject, "scope_id": v.scope_id(subject), "rev": v.rev(subject)}

    def rev(self, unit: str, head: str | None = None) -> str:
        return self.view(head).rev(unit)

    @property
    def position(self) -> int:
        return len(self.entries)

    def admit(self, *records: dict) -> list[dict]:
        self.entries.append(admission_body(self.position, self.head, self.head, records=list(records)))
        return list(records)

    def lifecycle(self, rec: dict) -> dict:
        self.entries.append(lifecycle_body(self.position, rec, obs=self.head))
        return rec

    def absorb(self, files: dict[str, str]) -> str:
        self.files.update(files)
        new = self.add_tree(tree(self.files, self.manifest))
        self.entries.append(absorption_body(self.position, new))
        self.head = new
        return new

    def integrate(self, files: dict[str, str], producer: str, task: str, records: tuple[dict, ...] = (),
                  lineage: list[str] | None = None, binding_extra: dict | None = None) -> tuple[str, dict]:
        """An agent's candidate integrated: a task result for the transformation, then its admission."""

        base = self.head
        merged = dict(self.files, **files)
        candidate = self.add_tree(tree(merged, self.manifest))
        transformation = "sha256:" + hashlib.sha256(f"ssds.transformation.v1|{base}|{candidate}".encode()).hexdigest()
        result = record("TASK_RESULT", target={"task": task, "candidate": candidate, "transformation": transformation,
                                               "base": base},
                        outcome="COMPLETE", actor=producer, actor_class="AGENT",
                        frame={"transformation": transformation})
        result["binding"] = fresh(producer, task, lineage, **(binding_extra or {}))
        from ssds.ledger.read import with_id

        result = with_id(result)
        self.entries.append(admission_body(self.position, base, candidate, records=[result, *records],
                                           integrates=transformation))
        self.files = merged
        self.head = candidate
        return transformation, result

    def derive(self, position: int | None = None):
        chain = chain_of("demo", self.entries, self.objects)
        return derive(chain, self.trees.__getitem__, position)


def judgment(kind: str, target: dict, outcome: str, actor: str = HUMAN, actor_class: str = "HUMAN", basis=(),
             supersedes=(), fields=None, binding=None, frame="ADMITTED") -> dict:
    from ssds.ledger.read import with_id

    rec = record(kind, target=target, outcome=outcome, actor=actor, actor_class=actor_class, basis=basis,
                 supersedes=supersedes, fields=fields, frame=frame)
    if binding is not None:
        rec["binding"] = binding
    return with_id(rec)


def content(unit: str, rev: str, cls: str = "EXACT", role: str | None = None) -> dict:
    entry = {"mode": "content", "target": {"unit": unit, "rev": rev}, "class": cls}
    if role:
        entry["role"] = role
    return entry


def validity(unit: str, rev: str, cls: str = "EXACT") -> dict:
    return {"mode": "validity", "target": {"unit": unit, "rev": rev}, "class": cls}


def on_record(rid: str, mode: str = "record") -> dict:
    return {"mode": mode, "target": {"record": rid}, "class": "EXACT"}


def challenge(target: dict, blocking: bool = True, actor: str = HUMAN_B) -> dict:
    return judgment("CHALLENGE", target, None, actor=actor,
                    fields={"blocking": blocking, "serious": False, "inquiry": "CONFIRMATORY"})


def adjudication(challenge_id: str, outcome: str, actor: str = OWNER) -> dict:
    return judgment("ADJUDICATION", {"record": challenge_id}, outcome, actor=actor)


def structure_deltas(before, after) -> list[dict]:
    """Every structural declaration change between two structures, as an admission records it."""

    from ssds.content import value_to_json

    keys = set(before.decl) | set(after.decl)
    out = []
    for key in sorted(keys):
        if before.decl.get(key) != after.decl.get(key):
            value = after.decl.get(key)
            out.append({"key": list(key), "value": None if value is None else value_to_json(key[1], value),
                        "source": "AUTHORED"})
    return out


def submit(sc: Scenario, files: dict[str, str], producer: str, task: str, manifest: str | None = None,
           base: str | None = None) -> tuple[str, str, dict]:
    """A task result submitting a candidate: (transformation, candidate commit, result record)."""

    from ssds.ledger.read import with_id

    base = base or sc.head
    candidate_tree = tree({**{p: e.data.decode() for p, e in sc.trees[base].items() if p != ".ssds/manifest.toml"},
                           **files}, manifest or sc.manifest)
    candidate = sc.add_tree(candidate_tree)
    transformation = "sha256:" + hashlib.sha256(f"ssds.transformation.v1|{base}|{candidate}".encode()).hexdigest()
    result = record("TASK_RESULT", target={"task": task, "candidate": candidate, "transformation": transformation,
                                           "base": base},
                    outcome="COMPLETE", actor=producer, actor_class="AGENT", frame={"transformation": transformation})
    result["binding"] = fresh(producer, task)
    result = with_id(result)
    sc.admit(result)
    return transformation, candidate, result


def integrate(sc: Scenario, transformation: str, candidate: str) -> None:
    """The admission that integrates a submitted candidate whose base is the current head."""

    before = structure_of(sc.trees[sc.head])
    after = structure_of(sc.trees[candidate])
    sc.entries.append(admission_body(sc.position, sc.head, candidate, deltas=structure_deltas(before, after),
                                     integrates=transformation))
    sc.structure = after
    sc.files = {p: e.data.decode() for p, e in sc.trees[candidate].items() if p != ".ssds/manifest.toml"}
    sc.head = candidate


def store(sc: Scenario, value: dict) -> str:
    """A ledger-store object carried by the next entry (an evaluated outcome); returns its digest."""

    from ssds.core.api.v1 import canonical_json

    data = canonical_json(value)
    digest = "sha256:" + hashlib.sha256(data).hexdigest()
    sc.objects.setdefault(sc.position, {})[digest] = data
    return digest
