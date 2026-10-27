"""Assessment disagreement: start, matching, staleness and disposition (catalogue §6; Manual §6).

A failing assessment caps validity at ``P`` while it counts and no disposition
stands; it never makes validity ``F``. It starts counting on an admitted fact
or in its own lineage (§6.4) and stops only by a disposition (§6.7) or by
discriminating observations (§6.6).

Observations are ``REALIZATION`` records. Each records its execution basis once
(§6.3): ``tree`` (the commit it ran on), unit, read and widened entries with
their content identities, pins, an unpinnable flag, execution attributes, the
frozen resolution ``context`` and ``bounded_by`` (completeness judgments, or
``"UNBOUNDED"``). Its evaluated outcome is a ledger-store object in §17.3's shape,
``{output name: canonical value}`` over the declared outputs; an embedded verdict is itself a
declared ``enum`` output that the specification's declaration names (Phase F step 9b-ii,
readings F83-F86).

Verdicts are read through the declaration of the reading's specification revision (§6.5):
an embedded verdict only under the reading the execution ran, and ``EXACT`` recomputed from the
stored outcome under any reading; every other template is not computable until Q-F21 settles it
(F86), so it is taken as yielding the failure (fail closed), as is a reading whose declaration is
defective or unknown. A passing assessment under a defective specification is not admissible
(§17.4; F84); a failing one still counts, since failing evidence is never dropped (§6; step 9b-ii's
narrowing of F84's note 1, on the safe side). The rest of §17.4's admissibility is step 9c-ii's,
and home follows successors by file overlap, which only adds subjects.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from functools import cached_property, lru_cache
from typing import Any

from ssds.content import SpecDeclaration, TreeView, canonical_reference, is_canonical, jcs, recorded_identity

from .frames import transformation_of
from .realization import basis_problems, context_available, on_minus
from .state import F, P, State, T

SYSTEM_RULESET = "ssds-rules/1"


class Assessments:
    def __init__(self, state: State, judgments: Any = None) -> None:
        self.s = state
        self._judgments = judgments

    @cached_property
    def j(self) -> Any:
        """§5.10, the one owner of vetoes and independence a bounding judgment's standing reads."""

        if self._judgments is None:
            from .judgment import Judgments

            self._judgments = Judgments(self.s)
        return self._judgments

    # -- records ------------------------------------------------------------------------------

    @cached_property
    def by_obligation(self) -> dict[str, list[str]]:
        out: dict[str, list[str]] = {}
        for rid in self.s.of_kind("EVIDENCE_ASSESSMENT"):
            out.setdefault(self.s.record(rid)["target"]["obligation"], []).append(rid)
        return out

    def real(self, rid: str) -> str | None:
        realization = self.s.record(rid)["target"]["realization"]
        return realization if realization in self.s.records else None

    def realization(self, rid: str) -> dict[str, Any] | None:
        real = self.real(rid)
        return self.s.record(real) if real else None

    def failing(self, rid: str) -> bool:
        return self.s.record(rid)["outcome"] == "FAIL"

    def passing(self, rid: str) -> bool:
        return self.s.record(rid)["outcome"] == "PASS"

    def claim_units(self, rid: str) -> list[str]:
        realization = self.realization(rid)
        return [c["unit"] for c in realization["target"]["claim"]] if realization else []

    # -- start: anchors, home, about, starts (§6.4) -------------------------------------------------

    def _subjects_containing(self, view, units: list[str]) -> set[str]:
        out: set[str] = set()
        for unit in units:
            if unit not in view.structure.units:
                continue
            for candidate in view.structure.units:
                if view.structure.units[candidate].subject and unit in view.inside(candidate):
                    out.add(candidate)
        return out

    def base_position(self, rid: str) -> int:
        """A frame record's base is the admitted state its frame merged onto; otherwise its own position."""

        record = self.s.record(rid)
        if record["frame"] == "ADMITTED":
            return self.s.position_of(rid)
        x = transformation_of(self.s, record["frame"]["transformation"])
        if x is None:
            return self.s.position_of(rid)
        positions = [k for k in range(self.s.position_of(rid) + 1) if self.s.h.head(k) == x.base]
        return max(positions) if positions else self.s.position_of(rid)

    @lru_cache(maxsize=None)  # noqa: B019
    def home(self, rid: str) -> frozenset[str]:
        """Admitted anchors (and frame anchors in the lineage's frames) with their successors; never shed."""

        units = self.claim_units(rid)
        base = self.base_position(rid)
        anchors = self._subjects_containing(self.s.h.view(base), units)
        if self.in_lineage_frame(rid) and self.s.frame is not None:
            anchors |= self._subjects_containing(self.s.view, units)
        base_files = {span.path for s in anchors for span in (self.s.h.view(base).regions.get(s) or ())}
        for subject, unit in self.s.view.structure.units.items():
            if unit.subject and subject not in self.s.h.view(base).structure.units:
                files = {span.path for span in (self.s.view.regions.get(subject) or ())}
                if files & base_files:
                    anchors.add(subject)  # a successor that received regions of a home subject
        return frozenset(anchors)

    def lineage(self, rid: str) -> str | None:
        """The bound obligation a frame record's transformation was produced for (§6.4)."""

        record = self.s.record(rid)
        if record["frame"] == "ADMITTED":
            return None
        transformation = record["frame"]["transformation"]
        for result in self.s.of_kind("TASK_RESULT"):
            target = self.s.record(result)["target"]
            if target.get("transformation") == transformation:
                return (self.s.record(result)["binding"] or {}).get("obligation")
        return None

    def in_lineage_frame(self, rid: str) -> bool:
        lineage = self.lineage(rid)
        if lineage is None or self.s.frame is None:
            return False
        for result in self.s.of_kind("TASK_RESULT"):
            record = self.s.record(result)
            if record["target"].get("transformation") == self.s.frame.x.id:
                return (record["binding"] or {}).get("obligation") == lineage
        return False

    def required_somewhere(self, obligation: str, through: int | None = None) -> bool:
        """The obligation is required for some subject in the admitted state at some position (a latch)."""

        return self.s.evidence.required_somewhere(obligation, through)

    def starts(self, rid: str) -> bool:
        obligation = self.s.record(rid)["target"]["obligation"]
        if self.in_lineage_frame(rid) or self.required_somewhere(obligation):
            return True
        if self.s.frame is not None:
            return self.s.evidence.required_anywhere(obligation)
        return False

    def about(self, rid: str, subject: str) -> bool:
        if subject in self.home(rid):
            return True
        obligation = self.s.record(rid)["target"]["obligation"]
        if obligation in self.s.evidence.required(subject):
            return True
        home_now = {s for s in self.home(rid) if s in self.s.view.structure.units}
        units = self.claim_units(rid)
        within = any(u in self.s.view.inside(subject) for u in units if subject in self.s.view.structure.units)
        within_home = any(u in self.s.view.inside(h) for u in units for h in home_now)
        return within and not within_home

    def disposition_needs_human(self, record: dict[str, Any]) -> bool:
        """§6.8's class: R3, a human's, where a subject a failure ``record`` disposes of is about is, or has been, D1
        or D2 (reading F101). The failures are ``Judgments.disposed_failures``'s, the one owner of §6.7's
        disposition (review of e643fa07, B1); "another actor's" restricts supersessions and adjudications, not an
        ``IMMATERIALITY``. The one predicate Admission reads."""

        structure = self.s.view.structure
        subjects = [u for u, unit in structure.units.items() if unit.subject]
        disposed = [x for x in self.j.disposed_failures(record)
                    if record["kind"] == "IMMATERIALITY" or self.s.record(x)["actor"] != record["actor"]]
        for x in disposed:
            about = set(self.home(x)) | {u for u in subjects if self.about(x, u)}
            if any(self.s.ever_authority(u) for u in about):
                return True
        return False

    def admissible(self, rid: str, obligation: str) -> bool:
        """§17.4 (reading F89): the assessment names ``obligation`` and reads its specification, and its realization
        passes ``realization_ok``. A passing assessment needs every check and a usable declaration (9b-ii); a failing
        one keeps counting under a defective declaration and under its key's compromise, since failing evidence is
        never dropped (§6; F41): the owner disposes of it, first by an upheld challenge against its realization."""

        record = self.s.record(rid)
        if record["target"]["obligation"] != obligation:
            return False
        real = self.real(rid)
        if real is None:
            return False
        reading = (record["fields"].get("reading") or {}).get("unit")
        spec = self.s.record(real)["target"]["spec"]["unit"]
        if reading is None or self.s.evidence.root(reading) != self.s.evidence.root(spec):
            return False
        return self.realization_ok(real, obligation, adverse=self.failing(rid))

    def realization_ok(self, real: str, obligation: str | None, adverse: bool = False) -> bool:
        """The one owner of §17.4's admissibility of a realization for ``obligation`` (reading F89): (a) its
        specification and a claim of its target give the obligation, (b) every fixed attribute of the instantiated
        revision's declaration is recorded with that value, (c) it is complete, its outcome stored, (d) a designated
        runner of the declaration's class ran it, its key a runner trust root designated for the class by the policy
        in force at its admission, its recorded class facts that class's, and (e) its key was not compromised at or
        before its admission. ``adverse``: a failing use, which (e) and a defective declaration do not drop.
        ``obligation`` None: (b)-(e) only, as conformance's required evidence reads them (§14.3)."""

        from .realization import read

        record = self.s.record(real)
        r = read(real, record)
        if not r.well_formed or record["actor_class"] != "MACHINERY":
            return False
        if obligation is not None and not any(self.s.evidence.token(claim, r.spec) == obligation for claim, _ in r.claims):
            return False  # (a); conformance's required evidence names a specification, not an obligation (None)
        if r.outcome != "COMPLETE" or self.outcome(real) is None:
            return False  # (c)
        declared = self.s.specs.declaration_at(r.spec, r.spec_rev)
        if not isinstance(declared, SpecDeclaration):
            return adverse  # 9b-ii: a defective declaration admits no passing assessment, and drops no failing one
        if any(r.attributes.get(k) != v for k, v in declared.fixed.items()):
            return False  # (b)
        position = self.s.position_of(real)
        from .state import policy_at

        unreadable = policy_at(self.s.h, position) is None
        designated = self.designated(r, declared.runner, position) or (adverse and unreadable)
        if not designated:
            return False  # (d); an unreadable historical policy never drops failing evidence (re-check of cb146b5a)
        compromised = self.trust.compromised.get(r.runner_key)
        return adverse or compromised is None or position < compromised  # (e)

    def designated(self, r: Any, runner_class: str, position: int) -> bool:
        """F89 (d): the runner, its key and its recorded class facts, as the policy and trust roots at
        ``position`` designate them (§6.3: decided at realization, recorded by value; §17.5, §25.2)."""

        from .state import policy_at
        from .trust import trust_roots

        if r.runner_class != runner_class:
            return False
        policy = policy_at(self.s.h, position)
        cls = policy.runners.get(runner_class) if policy is not None else None  # unreadable: designates nothing
        roots = trust_roots(self.s.h.chain.entries[: position + 1])
        return cls is not None and r.runner_key in cls.keys and r.runner_key in roots.runners \
            and tuple(r.class_attributes) == cls.attributes and r.observes_outside_reads == cls.observes_outside_reads

    @cached_property
    def trust(self) -> Any:
        from .trust import trust_roots

        return trust_roots(self.s.h.chain.entries[: self.s.n + 1])

    # -- matching (§6.5) --------------------------------------------------------------------------

    def observations(self, rid: str) -> list[str]:
        """Every admitted observation of ``conf(a⁻)``: the same specification unit and configuration."""

        real = self.realization(rid)
        if real is None:
            return []
        spec, conf = real["target"]["spec"]["unit"], real["fields"].get("configuration")
        return [o for o in self.s.of_kind("REALIZATION")
                if self.s.record(o)["target"]["spec"]["unit"] == spec and self.s.record(o)["fields"].get("configuration") == conf]

    def basis(self, observation: str) -> dict[str, Any]:
        return self.s.record(observation)["fields"]["execution"]

    def _context_available(self, basis: dict[str, Any]) -> bool:
        return not basis_problems(basis) and context_available(basis, self.s.analyzer_set)

    def on_minus(self, observation: str, tree) -> bool:
        """``on⁻``: every recorded tree-resident term re-resolves, under the record's own context, to its identity
        (``realization.on_minus``, the one owner; F97)."""

        basis = self.basis(observation)
        if basis_problems(basis):
            return True  # a basis outside its types asserts nothing permissive; adversely it links (F88, F96)
        found = on_minus(basis, tree, self.s.analyzer_set)
        return True if found is None else found  # a host lacking the recorded context asserts nothing permissive

    def ext(self, o: str, x: str) -> bool:
        bo, bx = self.basis(o), self.basis(x)
        if self.unpinnable(o) or self.unpinnable(x):
            return False
        pins = lambda b: sorted(map(tuple, b.get("pins", [])))  # noqa: E731
        attributes = lambda b: dict(map(tuple, b.get("attributes", [])))  # noqa: E731
        return pins(bo) == pins(bx) and attributes(bo) == attributes(bx)

    def unpinnable(self, observation: str) -> bool:
        """Counts as having an unpinnable read (§6.3, §17.5; reading F90): it recorded one, its class does not observe
        every read outside the tree, it lacks a recorded attribute its class records, or its execution is outside
        the closed shape (F88)."""

        from .realization import read

        r = read(observation, self.s.record(observation))
        return not r.well_formed or r.unpinnable or not r.observes_outside_reads \
            or not set(r.class_attributes) <= set(r.attributes)

    def bound(self, observation: str, tree, base: Callable[[str], int], value: Callable[[Any], int] | None = None) -> bool:
        """``bound(o, K)`` (catalogue §6.5 as amended by SD-58, Manual A8).

        A bounding completeness judgment certifies the execution basis of a run on the content it
        ran on, so it is checked there: it bounds ``o`` for content ``K`` when it stands (acts, is
        not superseded, is ``CLEAR``, held, independent and not vetoed), its membership digest is
        that of ``K``, each of its ``content`` entries holds in ``K``, and each other premise holds
        in the state of evaluation (a cited record current at ``T``, a ``standing`` entry's record at
        base ``T``, a machinery judgment's analyzer in the analyzer set). A ``validity`` or
        ``execution`` premise fails closed. Completeness is read positively only.
        """

        bounded_by = self.basis(observation).get("bounded_by", "UNBOUNDED")
        if bounded_by == "UNBOUNDED" or not self._context_available(self.basis(observation)):
            return False
        view = TreeView(tree, self.s.view.structure, self.s.h.manifest_path)
        for c in bounded_by:
            if c not in self.s.records:
                return False
            record = self.s.record(c)
            if (record["kind"], record["outcome"]) != ("COMPLETENESS", "COMPLETE") or not self._stands(c):
                return False  # only a positive completeness certificate bounds; INCOMPLETE stays adverse
            target = record["target"]
            if view.membership_digest(tuple(target["scope"])) != target.get("membership"):
                return False
            if record["actor_class"] == "MACHINERY" and target.get("analyzer") not in self.s.analyzer_set:
                return False
            for entry in record["basis"]:
                mode = entry["mode"]
                if mode == "content":
                    unit, rev = entry["target"]["unit"], entry["target"]["rev"]
                    if unit not in view.structure.units or view.rev(unit) != rev:
                        return False
                elif mode == "record":
                    q = entry["target"]["record"]
                    if value is None or q not in self.s.records or value(("current", q)) != T:
                        return False
                elif mode == "standing":
                    if entry["target"]["record"] not in self.s.records or base(entry["target"]["record"]) != T:
                        return False
                elif mode != "identity":
                    return False
        return True

    def _stands(self, c: str) -> bool:
        s = self.s
        return (s.acts(c) and not s.superseded(c) and s.status1(c) == "CLEAR" and s.cont(c)
                and not self.j.vetoed(c) and not self.j.nonind(c))

    def on_plus(self, observation: str, tree, real: str, base: Callable[[str], int],
                value: Callable[[Any], int] | None = None) -> bool:
        return self._context_available(self.basis(observation)) and self.on_minus(observation, tree) and \
            self.ext(observation, real) and self.bound(observation, tree, base, value)

    def tree_of(self, observation: str):
        return self.s.h.trees(self.basis(observation)["tree"])

    def link_minus(self, observation: str, tree, configuration: list[str]) -> bool:
        return any(self.on_minus(other, tree) and self.on_minus(other, self.tree_of(observation)) for other in configuration)

    # -- outcomes and verdicts ------------------------------------------------------------------------

    def outcome(self, observation: str) -> dict[str, Any] | None:
        digest = self.s.record(observation)["fields"].get("evaluated")
        data = self.s.h.objects.get(digest) if digest else None
        return json.loads(data) if data else None

    def declaration(self, observation: str) -> SpecDeclaration | None:
        """The usable declaration of the specification revision ``observation`` ran under, or None."""

        spec = self.s.record(observation)["target"]["spec"]
        found = self.s.specs.declaration_at(spec["unit"], spec["rev"])
        return found if isinstance(found, SpecDeclaration) else None

    def failing_outputs(self, rid: str) -> list[str]:
        """The outputs ``rid`` names as failing, else every declared output, verdict carriers included (§6.5: "one
        naming none found every declared output failing"; reading F105), else every output of the outcome. An
        assessor-read declaration has no verdicts, so reading only the judged outputs left its failures nothing to
        compare."""

        named = self.s.record(rid)["fields"].get("failing_outputs") or []
        if named:
            return list(named)
        real = self.real(rid)
        declared = self.declaration(real) if real else None
        if declared is not None:
            return sorted(o.name for o in declared.outputs)
        return sorted((self.outcome(real) if real else None) or {})

    def restricted(self, observation: str, outputs: list[str]) -> dict[str, Any] | None:
        outcome = self.outcome(observation)
        if outcome is None:
            return None
        # identity of outcomes is byte equality of canonical values (§17.3), so values compare as canonical JSON,
        # type-strict: 1 is not true (review of a0f2e31b, B2); a name follows the observation's own renames (F94)
        declared = self.declaration(observation)
        names = {x: _renamed(declared, x) for x in outputs}
        return {x: jcs(outcome[n]).decode() if n in outcome else None for x, n in names.items()}

    def _in_force_at_base(self, rid: str, unit: str, x: str) -> bool:
        """``a⁻``'s check on ``x`` was in force at its base: ``x`` (or its one-hop rename) was a declared output of the
        reading's declaration at ``a⁻``'s base; a defective or unknown declaration counts as in force (§6.6; fail
        closed; reading F94; review of babcbd22, B1)."""

        view = self.s.h.view(self.base_position(rid))  # a frame record's base is its frame's (review note)
        found = self.s.specs.declaration_at(unit, view.rev(unit)) if unit in view.structure.units else None
        if not isinstance(found, SpecDeclaration):
            return True
        return found.output(_renamed(found, x)) is not None  # x was a declared output: its check was in force

    def yields(self, observation: str, rid: str) -> bool:
        """Under the reading in force: a verdict on a failing output that is not PASS, or not computable (fail
        closed), or the output missing (§6.5; F85, F86). Where the state holds the reading's revision only by
        absorption, the verdict is also taken under the revision the last admission integrated, and the failure is
        yielded if either fails (§6.6; review of a0f2e31b, B1)."""

        unit = self.s.record(rid)["fields"]["reading"]["unit"]
        reading_now = self.s.cur(unit) if unit in self.s.view.structure.units else None
        if reading_now is None:
            return True
        # in a candidate's frame the reading in force is the candidate's own, held by no absorption: §6.6's second
        # reading applies to the admitted state (re-check of 6fedb664, note)
        readings = {reading_now} if self.s.frame is not None else {reading_now, self.s.specs.integrated_rev(unit)}
        return any(self._yields_under(observation, rid, unit, rev) for rev in readings)

    def _yields_under(self, observation: str, rid: str, unit: str, rev: str | None) -> bool:
        found = self.s.specs.declaration_at(unit, rev) if rev is not None else None
        ran_under = self.s.record(observation)["target"]["spec"]["rev"]
        outcome = self.outcome(observation) or {}
        if not isinstance(found, SpecDeclaration):
            return True  # a defective or unknown reading computes nothing (fail closed)
        own_reading = self.s.record(rid)["fields"].get("reading") or {}
        own = self.s.specs.declaration_at(own_reading.get("unit"), own_reading.get("rev"))
        for x in self.failing_outputs(rid):
            if not isinstance(own, SpecDeclaration) or own.output(x) is None:
                return True  # F(a⁻) is "the declared outputs it found failing" (§6.5): a name outside a⁻'s own
                # reading, or an unusable one, fails closed (re-check of 9031b16d)
            name = _renamed(found, x)
            stored = _renamed(self.declaration(observation), x)
            if found.output(name) is None or stored not in outcome:
                # §6.5's "either" clause: G's reading does not evaluate x (x is not one of its declared outputs), or
                # the observation lacks x: yielded only if a⁻'s check on x was in force at its base (F94; review of
                # babcbd22, B1)
                if self._in_force_at_base(rid, unit, x):
                    return True
                continue
            if any(v.embedded == name for v in found.verdicts):
                continue  # an embedded verdict's carrier is judged by the output it carries (F85, F105; review of
                # 3f976498, note 1): in (4) it is no output of its own; (1) and (2) still compare it
            if found.oracle == "ASSESSOR_READ":
                return True  # yielded unless a standing discriminating reading covers it, none until 9e (§6.6)
            verdict = found.verdict(name)
            if verdict is None:
                return True  # a mechanical reading with no verdict on a declared output: not computable (§6.5)
            if verdict.embedded is not None:  # the recorded verdict counts only under the reading the run ran
                if ran_under != rev or outcome.get(verdict.embedded) != "PASS":
                    return True
            elif verdict.template == "EXACT":  # recomputed from the stored outcome under any reading
                output = found.output(name)  # the reading's output; the value is the observation's own name's
                try:
                    reference = canonical_reference(output, verdict.params["reference"])
                except ValueError:
                    return True
                if not is_canonical(output, outcome[stored]) \
                        or jcs(outcome[stored]) != jcs(reference):  # byte equality (§17.3)
                    return True
            else:
                return True  # not computable until Q-F21 settles it (F86)
        return False

    def standing(self, observation: str) -> bool:
        s = self.s
        if not s.cont(observation) or s.record(observation)["outcome"] == "INCOMPLETE":
            return False
        if self.unavailable_needed(observation):
            return False  # binding health (§17.4; reading F92)
        if not self.trusted(observation):
            return False  # F90: a permissive use needs a designated, uncompromised runner (§17.5, §25.2)
        return s.status1(observation) == "CLEAR"  # a risk override never resolves a challenge

    def trusted(self, observation: str) -> bool:
        """F89 (d)-(e) for an observation's permissive use (reading F90; review of d481277f, B1): well formed, by
        ``MACHINERY``, under a usable declaration of the revision it instantiated, by a runner the policy and trust
        roots at its admission designated for that declaration's class, its key not compromised by then. Adverse
        uses read every observation."""

        from .realization import read

        record = self.s.record(observation)
        r = read(observation, record)
        if not r.well_formed or record["actor_class"] != "MACHINERY":
            return False
        declared = self.s.specs.declaration_at(r.spec, r.spec_rev)
        if not isinstance(declared, SpecDeclaration):
            return False
        position = self.s.position_of(observation)
        compromised = self.trust.compromised.get(r.runner_key)
        return self.designated(r, declared.runner, position) and (compromised is None or position < compromised)

    @cached_property
    def _availability(self) -> dict[str, str]:
        """Digest -> the outcome of the latest acting ``AVAILABILITY`` record on it (§17.4)."""

        latest: dict[str, tuple[int, str]] = {}
        for rid in self.s.of_kind("AVAILABILITY"):
            if not self.s.acts(rid):
                continue
            digest = (self.s.record(rid).get("target") or {}).get("digest")
            position = self.s.position_of(rid)
            outcome = self.s.record(rid)["outcome"]
            if isinstance(digest, str) and (digest not in latest or position > latest[digest][0]
                                            or position == latest[digest][0] and outcome == "UNAVAILABLE"):
                latest[digest] = (position, outcome)  # a tie at one position falls to UNAVAILABLE (safe side)
        return {d: outcome for d, (_, outcome) in latest.items()}

    def unavailable_needed(self, real: str) -> bool:
        """A reference the realization needs, its evaluated outcome or one its envelope names, is marked
        unavailable by the latest acting ``AVAILABILITY`` record on it (binding health, §17.4; reading F92)."""

        record = self.s.record(real)
        needed = [(record.get("fields") or {}).get("evaluated")]
        needed += [r.get("digest") for r in record.get("refs") or [] if isinstance(r, dict)]
        return any(self._availability.get(d) == "UNAVAILABLE" for d in needed if isinstance(d, str))

    # -- stop: staleness (§6.6) -------------------------------------------------------------------------

    def stale(self, rid: str, base: Callable[[str], int], value: Callable[[Any], int] | None = None) -> bool:
        real = self.real(rid)
        if real is None or self.outcome(real) is None:
            return False
        anchors = self.observations(rid)  # link⁻'s o' ranges over every one, INCOMPLETE ones included (§6.6; F93)
        configuration = [o for o in anchors if self.s.record(o)["outcome"] != "INCOMPLETE"
                         and self.outcome(o) is not None]
        failing = self.failing_outputs(rid)
        expected = self.restricted(real, failing)
        failing_tree = self.tree_of(real)
        here = self.s.view.tree
        reproduced = any(o != real and self.standing(o) and self.custody_ok(o, anchors)
                         and self.on_plus(o, failing_tree, real, base, value)
                         and self.restricted(o, failing) == expected for o in configuration)
        if not reproduced:
            return False
        if any(self.restricted(o, failing) != expected for o in configuration
               if self.link_minus(o, failing_tree, anchors)):
            return False  # it differed: nondeterministic in fact, the owner's
        if not any(self.standing(o) and self.custody_ok(o, anchors) and self.on_plus(o, here, real, base, value)
                   for o in configuration):
            return False
        return not any(self.yields(o, rid) for o in configuration if self.link_minus(o, here, anchors))

    def _enumeration_trusted(self, enumeration: str, runner_class: str) -> bool:
        """An enumeration by ``MACHINERY`` under a key the policy and runner trust roots at its own admission
        designated for the class, not compromised by then (F89 (d)-(e) for the enumeration; review of babcbd22,
        note 1)."""

        from .state import policy_at
        from .trust import trust_roots

        record = self.s.record(enumeration)
        actor = str(record.get("actor", ""))
        key = actor.rsplit("@", 1)[1] if actor.startswith("machinery:") and "@" in actor else None
        position = self.s.position_of(enumeration)
        policy = policy_at(self.s.h, position)
        cls = policy.runners.get(runner_class) if policy is not None else None
        if record["actor_class"] != "MACHINERY" or key is None or cls is None or key not in cls.keys \
                or key not in trust_roots(self.s.h.chain.entries[: position + 1]).runners:
            return False
        compromised = self.trust.compromised.get(key)
        return compromised is None or position < compromised

    def custody_ok(self, observation: str, configuration: list[str]) -> bool:
        """§6.9, §17.5, F81 (reading F93): an external custody runner's observation serves conditions (1) and (3)
        only under the latest admitted ``CUSTODY_ENUMERATION`` of its class, signed by one of the class's keys, that
        lists it and every admitted realization of the configuration by that class, every run it lists admitted."""

        from .realization import read
        from .state import policy_at

        r = read(observation, self.s.record(observation))
        position = self.s.position_of(observation)
        policy = policy_at(self.s.h, position)
        cls = policy.runners.get(r.runner_class) if policy is not None and r.runner_class else None
        if cls is None or cls.kind != "EXTERNAL_CUSTODY":
            return True
        enumerations = [e for e in self.s.of_kind("CUSTODY_ENUMERATION")
                        if (self.s.record(e).get("target") or {}).get("runner") == r.runner_class and self.s.acts(e)
                        and self._enumeration_trusted(e, r.runner_class)]
        if not enumerations:
            return False
        latest = max(enumerations, key=self.s.position_of)
        runs = set((self.s.record(latest).get("fields") or {}).get("runs") or [])
        by_class = {o for o in configuration if read(o, self.s.record(o)).runner_class == r.runner_class}
        admitted = set(self.s.of_kind("REALIZATION"))
        return observation in runs and by_class <= runs and runs <= admitted

    def explain(self, rid: str, base: Callable[[str], int], value: Callable[[Any], int] | None = None) -> dict[str, Any]:
        """Which observations satisfy or defeat each condition, and every link traversed (798b2b4 B4)."""

        real = self.real(rid)
        anchors = self.observations(rid)
        configuration = [o for o in anchors if self.s.record(o)["outcome"] != "INCOMPLETE"
                         and self.outcome(o) is not None]
        failing = self.failing_outputs(rid)
        expected = self.restricted(real, failing) if real else None
        failing_tree = self.tree_of(real) if real else None
        here = self.s.view.tree

        def links(o: str, tree) -> list[str]:
            return [other for other in anchors if self.on_minus(other, tree) and self.on_minus(other, self.tree_of(o))]

        out: dict[str, Any] = {"reproduced": [], "differed": [], "observed_here": [], "yielding_here": [], "links": []}
        if real is None:
            return out
        for o in configuration:
            if o != real and self.standing(o) and self.custody_ok(o, anchors) \
                    and self.on_plus(o, failing_tree, real, base, value) and self.restricted(o, failing) == expected:
                out["reproduced"].append(o)
            via = links(o, failing_tree)
            if via and self.restricted(o, failing) != expected:
                out["differed"].append(o)
            out["links"].extend(("failing-content", o, v) for v in via)
            if self.standing(o) and self.custody_ok(o, anchors) and self.on_plus(o, here, real, base, value):
                out["observed_here"].append(o)
            via_here = links(o, here)
            if via_here and self.yields(o, rid):
                out["yielding_here"].append(o)
            out["links"].extend(("here", o, v) for v in via_here)
        return out

    def adverse(self, subject: str, obligation: str, base: Callable[[str], int],
                value: Callable[[Any], int] | None = None) -> list[str]:
        return [a for a in self.by_obligation.get(obligation, []) if self.failing(a) and self.admissible(a, obligation)
                and self.starts(a) and self.about(a, subject) and not self.stale(a, base, value)]

    # -- disposition (§6.7) ----------------------------------------------------------------------------

    def disposition(self, rid: str, value: Callable[[Any], int], base: Callable[[str], int], nonind: Callable[[str], bool]) -> int:
        """``disp(a⁻)``: the best effective disposition."""

        s = self.s
        best = F
        frontier, seen = list(s.supersessions.get(rid, [])), set()
        while frontier:  # supersession, directly or through a chain; the chain's last record must stand
            d = frontier.pop()
            if d in seen:
                continue
            seen.add(d)
            if not s.superseded(d) and not nonind(d):
                best = max(best, base(d))
            frontier.extend(s.supersessions.get(d, []))
        targets = {rid} | ({self.real(rid)} if self.real(rid) else set())
        for key in targets:
            for c in s.targeting.get(key, []):
                if s.record(c)["kind"] != "CHALLENGE":
                    continue
                for a in s.targeting.get(c, []):
                    record = s.record(a)
                    if record["kind"] == "ADJUDICATION" and record["outcome"] == "UPHELD" and not nonind(a) \
                            and s.in_force(a) and s.cont(a) and not self._contested(a):
                        best = T
        for d in s.of_kind("IMMATERIALITY"):
            if rid in s.record(d)["target"]["records"] and not nonind(d):
                best = max(best, value(("current", d)))
        return best

    def _contested(self, rid: str) -> bool:
        s = self.s
        return any(s.record(c)["kind"] == "CHALLENGE" and s.record(c)["fields"]["blocking"] and s.open(c)
                   for c in s.targeting.get(rid, []))

    # -- the evidence term and qual (§5.5) ----------------------------------------------------------------

    def undisputed(self, subject: str, obligation: str, value: Callable[[Any], int], base: Callable[[str], int],
                   nonind: Callable[[str], bool]) -> int:
        result = T
        for a in self.adverse(subject, obligation, base, value):
            result = min(result, max(P, self.disposition(a, value, base, nonind)))
        return result

    def ev(self, subject: str, obligation: str, value: Callable[[Any], int], base: Callable[[str], int],
           nonind: Callable[[str], bool]) -> int:
        best = F
        for a in self.by_obligation.get(obligation, []):
            if self.passing(a) and self.admissible(a, obligation) and self.about(a, subject):
                held = value(("current", a))
                real = self.real(a)
                if real is not None and self.unavailable_needed(real):
                    held = min(held, P)  # "not T": a needed reference is unavailable (§17.4; reading F92)
                best = max(best, held)
        return min(best, self.undisputed(subject, obligation, value, base, nonind))

    def qual(self, subject: str, value: Callable[[Any], int], base: Callable[[str], int],
             nonind: Callable[[str], bool]) -> int:
        result = T
        for obligation, records in self.by_obligation.items():
            if any(self.failing(a) and self.starts(a) and self.about(a, subject) for a in records):
                result = min(result, self.undisputed(subject, obligation, value, base, nonind))
        return result

    def support_nodes(self, subject: str) -> list[str]:
        """Support-graph edges 2 and 4 (§5.6): assessments, dispositions and bounding completeness judgments."""

        out = [a for records in self.by_obligation.values() for a in records if self.about(a, subject)]
        out += list(self.s.of_kind("IMMATERIALITY"))
        for a in out[:]:
            if self.s.record(a)["kind"] == "EVIDENCE_ASSESSMENT" and self.failing(a):
                for o in self.observations(a):
                    bounded_by = self.basis(o).get("bounded_by", "UNBOUNDED")
                    if bounded_by != "UNBOUNDED":
                        for c in bounded_by:
                            if c in self.s.records:  # the bounding judgment and the records it cites (§5.6 item 4)
                                out.append(c)
                                out += [e["target"]["record"] for e in self.s.record(c)["basis"]
                                        if e["mode"] == "record" and e["target"]["record"] in self.s.records]
        return out

    # -- execution-basis currency (§4.1, §6.3) --------------------------------------------------------------

    def execution_current(self, basis: dict[str, Any], content_sat: Callable[[str, str], int],
                          value: Callable[[Any], int]) -> int:
        if basis_problems(basis):
            return F  # an execution basis outside its types re-resolves nothing (F96)
        tree = self.s.view.tree
        ignore = tuple(basis["context"]["ignore"])
        result = T
        for unit_entry in basis.get("units", []):
            if all(recorded_identity(tree, term, ignore) == cid for term, cid in unit_entry["terms"]):
                continue
            result = min(result, content_sat(unit_entry["unit"], unit_entry["rev"]))
        for term, cid in list(basis.get("reads", [])) + list(basis.get("widened", [])):
            if recorded_identity(tree, term, ignore) != cid:
                return F
        bounded = basis.get("bounded_by", [])
        for judgment in bounded if isinstance(bounded, list) else []:  # §17.4: "together with its bounding
            result = min(result, value(("current", judgment)) if judgment in self.s.records else F)  # judgments"
        return result


def _renamed(declared: Any, x: str) -> str:
    """``x``'s name under ``declared``: itself when declared, else its one-hop rename (§6.5; reading F94). Renames
    are not composed along the revision lineage: a twice-renamed output is not evaluated, the coarser, safe reading."""

    if not isinstance(declared, SpecDeclaration) or declared.output(x) is not None:
        return x
    return declared.output_renames.get(x, x)
