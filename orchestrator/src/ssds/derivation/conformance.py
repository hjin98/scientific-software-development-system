"""Conformance of a task result (catalogue §14.1-§14.6).

Conformance is an S3 classification evaluated in the candidate's frame: a pure
function of the contract at the task's basis, the base and candidate trees,
the result record and the observations recorded for that exact candidate. It
is never stored. A result without a candidate is judged over the result record
and its contract alone.

Which templates run (Phase E reading E26): every check a contract obligation
names (primary and secondary); on every result, the result-level templates
whose subject is the result itself (``OBLIGATION.slots_filled`` and the four
``HARD`` faithfulness templates); on every result with a candidate, the
contract's boundaries (``BOUNDARY.write_scope`` with the domain rule,
``protected_surfaces``, ``generated_untouched``,
``TEST_INTEGRITY.evidence_specs_untouched``) and the ``HEURISTIC`` signals. An
evidence verifier is ``OBLIGATION.required_evidence`` on its specification; a
``REVIEW`` verifier is judged in review, not here.

Classes (§14.4): a failed ``BOUNDARY`` or ``TEST_INTEGRITY`` template is
``VIOLATION``, a failed ``OBLIGATION`` template or a missing required
execution ``INCOMPLETE``, a failed ``FAITHFULNESS`` template ``DISCREPANCY``;
§14.4 does not class ``DOMAIN``, read as ``INCOMPLETE`` (reading E25); a
``HEURISTIC`` hit is ``SIGNAL``. Conformance is a set: no class takes
precedence, and it is ``CLEAN`` when none of the first three is present.
Templates a designated runner executes (§14.1) are read from ``CHECK_EXECUTION``
observations for the exact candidate; a template this derivation cannot yet
evaluate and no runner observed is ``INCOMPLETE``, never passing.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from functools import cached_property
from typing import Any

from ssds import analyzers as py
from ssds.content import REVIEW, Check, Contract, EvidenceVerifier, Item, Structure, TreeView, write_set

from .frames import Frame, transformation_of
from .library import HEURISTIC, TEMPLATES
from .plans import contained, intersects, required_slots, resolve
from .state import F

VIOLATION, INCOMPLETE, DISCREPANCY, SIGNAL, CLEAN = "VIOLATION", "INCOMPLETE", "DISCREPANCY", "SIGNAL", "CLEAN"
FAILING = frozenset({VIOLATION, INCOMPLETE, DISCREPANCY})
FAMILY_CLASS = {"BOUNDARY": VIOLATION, "TEST_INTEGRITY": VIOLATION, "OBLIGATION": INCOMPLETE,
                "FAITHFULNESS": DISCREPANCY, "DOMAIN": INCOMPLETE}
RESULT_LEVEL = ("OBLIGATION.slots_filled", "FAITHFULNESS.outcome_consistent", "FAITHFULNESS.deviations_declared",
                "FAITHFULNESS.citations_support", "FAITHFULNESS.governing_at_basis")
CANDIDATE_LEVEL = ("BOUNDARY.write_scope", "BOUNDARY.protected_surfaces", "BOUNDARY.generated_untouched",
                   "TEST_INTEGRITY.evidence_specs_untouched")
SIGNALS = tuple(sorted(name for name, t in TEMPLATES.items() if t.force == HEURISTIC))
#: Templates a designated runner executes on the exact candidate (§14.1, §14.5).
RUNNER = frozenset({"OBLIGATION.mutation_strength"})
#: Result slots of the system contracts (§13.6), by bound obligation kind.
SYSTEM_SLOTS = {"COORDINATE": ("claims",), "CONTRACT": ("claims",), "INTAKE": ("claims", "findings", "unverified_assumptions"),
                "REVIEW_REVISION": ("claims", "findings", "revision_assessments")}
JUDGMENT_SLOTS = ("claims", "findings")
WHOLE = "*"  # the obligation column of a result-level or candidate-level template
_CERTAINTY = re.compile(r"\b(proves?|proven|guarantee[sd]?|certainly|definitely|always correct|never fails)\b", re.I)
#: Credential shapes (§14.3 credential_values); a policy may add patterns through the template's parameter.
_CREDENTIALS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}\b|\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"),
)
_TOKEN = re.compile(r"[A-Za-z0-9+/=_-]{32,}")
#: Dependency manifests of languages this ruleset does not analyze: a change to one cannot be checked here.
_OTHER_MANIFESTS = ("package.json", "Cargo.toml", "go.mod", "environment.yml", "environment.yaml", "Gemfile",
                    "pom.xml", "build.gradle", "setup.py", "setup.cfg", "Pipfile", "poetry.lock")
_NUMBER = re.compile(r"(?<![\w.])\d+(?:\.\d+)?(?:e[+-]?\d+)?(?![\w.])", re.I)


@dataclass(frozen=True, order=True)
class Hit:
    obligation: str  # a contract obligation id, or WHOLE
    template: str
    cls: str  # VIOLATION | INCOMPLETE | DISCREPANCY | SIGNAL | CLEAN
    finding: str
    observations: tuple[str, ...] = ()


def _filled(value: Any) -> bool:
    """A typed value, ``{"none": <reason>}`` or ``{"ref": <content reference>}`` (§13.5; reading E27)."""

    if isinstance(value, dict) and set(value) == {"none"}:
        return isinstance(value["none"], str) and bool(value["none"])
    if isinstance(value, dict) and set(value) == {"ref"}:
        return isinstance(value["ref"], str) and bool(value["ref"])
    return value not in (None, "", [], {})


class Conformance:
    """The conformance of one admitted task result."""

    def __init__(self, workflow: Any, result: str) -> None:
        self.w = workflow
        self.s = workflow.s
        self.d = workflow.d
        self.rid = result
        self.record = self.s.record(result)

    # -- inputs -----------------------------------------------------------------------------------

    @cached_property
    def transformation(self) -> str | None:
        return self.record["target"].get("transformation")

    @cached_property
    def frame(self) -> Frame | None:
        if not self.transformation:
            return None
        x = transformation_of(self.s, self.transformation)
        if x is None:
            return None
        return Frame(self.s.h, self.s.position_of(self.rid), x, self.s.enactment(self.transformation))

    @cached_property
    def contract(self) -> tuple[Contract | None, Item | None, str]:
        """The contract at the task's basis: the item revision the binding names, else the system contract."""

        binding = self.record.get("binding") or {}
        named = binding.get("contract_revision")
        if isinstance(named, dict) and {"unit", "rev"} <= set(named):
            found = self.s.plans.item_at(named["unit"], named["rev"])
            if found is not None and isinstance(found[1].parsed, Item) and found[1].parsed.contract is not None:
                return found[1].parsed.contract, found[1].parsed, ""
            return None, None, f"no contract at item revision {named['unit']}@{named['rev']}"
        kind = self._bound_kind(binding.get("obligation"))
        if kind is None:
            return None, None, "the result names no contract and no derived obligation"
        slots = SYSTEM_SLOTS.get(kind, JUDGMENT_SLOTS)
        return Contract("NOT_APPLIES", 3, (), (), (), (), (), (), (), (), tuple(slots), ()), None, ""

    def _bound_kind(self, obligation: str | None) -> str | None:
        for o in self.w.obligations:
            if o.id == obligation:
                return o.kind
        return None

    @cached_property
    def base_view(self) -> TreeView | None:
        if self.frame is None:
            return None
        return TreeView(self.frame.base_tree, Structure(self.s.h.sigma(self.s.position_of(self.rid))),
                        self.s.h.manifest_path)

    @cached_property
    def candidate_view(self) -> TreeView | None:
        return self.frame.candidate_view if self.frame is not None else None

    @cached_property
    def writes(self) -> dict[str, frozenset[str]]:
        """The effect-keyed write set of the candidate against its base (§1.2)."""

        if self.base_view is None or self.candidate_view is None:
            return {}
        return write_set(self.base_view, self.candidate_view)

    def _region_atoms(self, unit: str) -> list[tuple[Any, ...]]:
        for view in (self.candidate_view, self.base_view):
            if view is not None and unit in view.structure.units:
                region = view.regions.get(unit)
                if region:
                    return [("span", s.path, s.start, s.end) for s in region]
        return []

    @cached_property
    def slots(self) -> dict[str, Any]:
        return dict((self.record.get("fields") or {}).get("slots") or {})

    # -- the hits ---------------------------------------------------------------------------------

    @cached_property
    def hits(self) -> tuple[Hit, ...]:
        contract, item, problem = self.contract
        if contract is None:
            return (Hit(WHOLE, "OBLIGATION.slots_filled", INCOMPLETE, problem),)
        hits: list[Hit] = []
        if self.frame is not None:
            for template in CANDIDATE_LEVEL:
                hits.extend(self._evaluate(WHOLE, Check(template), contract, item))
        for ob in contract.obligations:
            if ob.verifier == REVIEW:
                pass
            elif isinstance(ob.verifier, EvidenceVerifier):
                hits.extend(self._evaluate(ob.id, Check("OBLIGATION.required_evidence", (("spec", ob.verifier.spec),)),
                                           contract, item))
            else:
                hits.extend(self._evaluate(ob.id, ob.verifier, contract, item))
            for check in ob.secondary:
                hits.extend(self._evaluate(ob.id, check, contract, item))
        for template in RESULT_LEVEL[:1]:
            hits.extend(self._evaluate(WHOLE, Check(template), contract, item))
        hits.extend(self._faithfulness(hits, contract, item))
        if self.frame is not None:
            for template in SIGNALS:
                hits.extend(self._evaluate(WHOLE, Check(template), contract, item))
        return tuple(sorted(set(hits)))

    @cached_property
    def classes(self) -> frozenset[str]:
        found = {h.cls for h in self.hits if h.cls != CLEAN}
        return frozenset(found) if found & FAILING else frozenset(found | {CLEAN})

    @property
    def clean(self) -> bool:
        return not (self.classes & FAILING)

    def view(self) -> dict[str, list[dict[str, Any]]]:
        """Per obligation: template results with classes and findings and the observations used (§14.6)."""

        out: dict[str, list[dict[str, Any]]] = {}
        for hit in self.hits:
            out.setdefault(hit.obligation, []).append(
                {"template": hit.template, "class": hit.cls, "finding": hit.finding, "observations": list(hit.observations)})
        return out

    # -- evaluation of one template ----------------------------------------------------------------

    def _evaluate(self, obligation: str, check: Check, contract: Contract, item: Item | None) -> list[Hit]:
        template = check.template
        params = dict(check.params)
        spec = TEMPLATES.get(template)
        failing = SIGNAL if spec is not None and spec.force == HEURISTIC else FAMILY_CLASS.get(template.split(".")[0], INCOMPLETE)
        if template in RUNNER:
            return [self._observed(obligation, template, failing)]
        method = getattr(self, "_t_" + template.replace(".", "_").lower(), None)
        if method is None:
            observed = self._observation(obligation, template)
            if observed is not None:
                return [self._observed(obligation, template, failing)]
            if spec is not None and spec.force == HEURISTIC:
                return []  # a signal this derivation does not compute raises nothing
            return [Hit(obligation, template, INCOMPLETE, "not evaluated by this derivation and not observed by a runner")]
        findings = method(params, contract, item)
        if not findings:
            return [Hit(obligation, template, CLEAN, "")]
        return [Hit(obligation, template, failing, f) for f in findings]

    def _observation(self, obligation: str, template: str) -> str | None:
        candidate = self.record["target"].get("candidate")
        found = None
        for rid in self.s.of_kind("CHECK_EXECUTION"):
            record = self.s.record(rid)
            target = record["target"]
            if (target.get("candidate"), target.get("obligation"), record["fields"].get("template")) == \
                    (candidate, obligation, template) and self.d.current(rid) > F:
                found = rid  # the latest observation of that check on that exact candidate
        return found

    def _observed(self, obligation: str, template: str, failing: str) -> Hit:
        rid = self._observation(obligation, template)
        if rid is None:
            return Hit(obligation, template, INCOMPLETE, "a required execution is missing for the exact candidate")
        outcome = self.s.record(rid)["outcome"]
        if outcome == "CLEAN":
            return Hit(obligation, template, CLEAN, "", (rid,))
        if outcome == "SIGNAL":
            return Hit(obligation, template, SIGNAL, "the runner reported a signal", (rid,))
        return Hit(obligation, template, failing, "the runner reported a failure", (rid,))

    # -- BOUNDARY and the evidence-specification boundary -------------------------------------------

    def _kinds(self) -> dict[str, str | None]:
        out = {}
        for unit in self.writes:
            view = self.candidate_view if self.candidate_view and unit in self.candidate_view.structure.units else self.base_view
            out[unit] = view.structure.kind(unit) if view is not None else None
        return out

    def outside_scope(self, contract: Contract) -> list[str]:
        """Units in the write set whose bytes lie outside the write scope: the detected boundary breaches."""

        if self.candidate_view is None:
            return []
        scope, _ = resolve(self.candidate_view, contract.write_scope)
        out = []
        for unit in sorted(self.writes):
            atoms = self._region_atoms(unit)
            if not atoms or not contained(self.candidate_view, atoms, scope):
                out.append(unit)
        return out

    def _t_boundary_write_scope(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        findings = [f"{u} changed outside the write scope" for u in self.outside_scope(contract)]
        kinds = self._kinds()
        kind = item.kind if item is not None else None
        if kind in ("IMPLEMENT", "REPAIR", "MIGRATE", "DOCUMENT") or kind is None:
            findings += [f"{u} is a {k} unit: only an AUTHOR item of that domain changes it" for u, k in sorted(kinds.items())
                         if k in ("D1", "D2", "D3")]
        elif kind == "AUTHOR":
            allowed = {item.authority, "MANIFEST", "EVIDENCE_RECORD"}
            findings += [f"{u} is a {k} unit outside the AUTHOR {item.authority} domain" for u, k in sorted(kinds.items())
                         if k not in allowed and u not in contract.evidence_specs]
        return findings

    def _t_boundary_protected_surfaces(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        if self.candidate_view is None:
            return []
        entries = list(self.s.policy.flow("protected_surfaces"))
        if "ssds.policy" in self.candidate_view.structure.units:
            entries.append("ssds.policy")
        protected, _ = resolve(self.candidate_view, entries)
        protected.append(("file", self.s.h.policy_path))
        return [f"{u} is a protected surface" for u in sorted(self.writes)
                if any(intersects(self.candidate_view, protected, a[1], a[2], a[3]) for a in self._region_atoms(u))]

    def _t_boundary_generated_untouched(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        return [f"{u} is GENERATED and was edited by hand" for u, k in sorted(self._kinds().items()) if k == "GENERATED"]

    def _t_test_integrity_evidence_specs_untouched(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        return [f"evidence specification {u} changed but is not named in evidence_specs"
                for u, k in sorted(self._kinds().items()) if k == "EVIDENCE_SPEC" and u not in contract.evidence_specs]

    # -- OBLIGATION ------------------------------------------------------------------------------

    def _t_obligation_slots_filled(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        required = set(contract.slots) | (set(required_slots(item)) if item is not None else set())
        return [f"required slot {name} is empty or missing" for name in sorted(required) if not _filled(self.slots.get(name))]

    def _t_obligation_required_evidence(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        """Realized by a designated runner on the exact candidate, with a current passing assessment (§14.3)."""

        spec = params.get("spec")
        candidate = self.record["target"].get("candidate")
        if candidate is None:
            return ["required evidence needs a candidate"]
        realized = False
        for rid in self.s.of_kind("REALIZATION"):
            record = self.s.record(rid)
            if record["target"]["spec"]["unit"] != spec or (record["fields"].get("execution") or {}).get("tree") != candidate:
                continue
            realized = True
            for a in self.s.of_kind("EVIDENCE_ASSESSMENT"):
                assessment = self.s.record(a)
                if assessment["target"].get("realization") == rid and assessment["outcome"] == "PASS" and self.d.current(a) > F:
                    return []
        if not realized:
            return [f"required evidence {spec} is not realized on the exact candidate"]
        return [f"required evidence {spec} has no current passing assessment on the exact candidate"]

    _t_obligation_evidence_basis_fields = None  # §17's admissibility of the realization basis (Phase F)

    # -- FAITHFULNESS ----------------------------------------------------------------------------

    def _faithfulness(self, hits: list[Hit], contract: Contract, item: Item | None) -> list[Hit]:
        out = []
        unmet = any(h.cls == INCOMPLETE for h in hits)
        if self.record["outcome"] == "COMPLETE" and unmet:
            out.append(Hit(WHOLE, "FAITHFULNESS.outcome_consistent", DISCREPANCY, "COMPLETE with an unmet obligation"))
        else:
            out.append(Hit(WHOLE, "FAITHFULNESS.outcome_consistent", CLEAN, ""))
        declared = {d.get("unit") for d in self.slots.get("deviations") or [] if isinstance(d, dict)}
        detected = set(self.outside_scope(contract))
        problems = [f"undisclosed breach of {u}" for u in sorted(detected - declared)]
        problems += [f"declared deviation {u} was not detected" for u in sorted(declared - detected) if u]
        out += [Hit(WHOLE, "FAITHFULNESS.deviations_declared", DISCREPANCY, p) for p in problems] or \
            [Hit(WHOLE, "FAITHFULNESS.deviations_declared", CLEAN, "")]
        out += self._citations()
        out += self._governing(item)
        return out

    def _citations(self) -> list[Hit]:
        problems = []
        for claim in self.slots.get("claims") or []:
            if not isinstance(claim, dict):
                continue
            for cited in claim.get("records") or []:
                if cited not in self.s.records:
                    problems.append(f"cited record {cited} does not exist")
                    continue
                if self.s.record(cited)["kind"] == "REALIZATION":
                    assessments = [a for a in self.s.of_kind("EVIDENCE_ASSESSMENT")
                                   if self.s.record(a)["target"].get("realization") == cited]
                    if assessments and all(self.s.record(a)["outcome"] == "FAIL" for a in assessments):
                        problems.append(f"failing realization {cited} cited in support of a claim")
        return [Hit(WHOLE, "FAITHFULNESS.citations_support", DISCREPANCY, p) for p in problems] or \
            [Hit(WHOLE, "FAITHFULNESS.citations_support", CLEAN, "")]

    def _governing(self, item: Item | None) -> list[Hit]:
        problems = []
        view = self.base_view or self.s.view
        for unit, rev in (item.governing if item is not None else ()):
            if unit not in view.structure.units or view.rev(unit) != rev:
                problems.append(f"governing unit {unit} cited at {rev[:19]}, not its basis revision")
        return [Hit(WHOLE, "FAITHFULNESS.governing_at_basis", DISCREPANCY, p) for p in problems] or \
            [Hit(WHOLE, "FAITHFULNESS.governing_at_basis", CLEAN, "")]

    # -- the Python analyzer's templates (§14.3, §14.5) -------------------------------------------------

    @cached_property
    def changed_files(self) -> dict[str, tuple[bytes | None, bytes | None]]:
        """Path -> (base bytes, candidate bytes) for every file that differs between ``B`` and ``C``."""

        if self.frame is None:
            return {}
        base, cand = self.frame.base_tree, self.frame.candidate_tree
        out = {}
        for path in sorted(set(base) | set(cand)):
            before = base[path].data if path in base else None
            after = cand[path].data if path in cand else None
            if before != after:
                out[path] = (before, after)
        return out

    def _selected(self, path: str, params: dict) -> bool:
        selectors = params.get("selectors")
        return py.is_test_file(path) and (not selectors or any(path.startswith(sel) for sel in selectors))

    def _test_change(self, params: dict) -> tuple[list[tuple[str, Any, Any]], list[str]]:
        """(path, base facts, candidate facts) for changed test files, and the files the analyzer cannot read."""

        out, unreadable = [], []
        for path, (before, after) in self.changed_files.items():
            if not self._selected(path, params):
                continue
            facts_before = py.test_facts(before) if before is not None else None
            facts_after = py.test_facts(after) if after is not None else None
            if (before is not None and facts_before is None) or (after is not None and facts_after is None):
                unreadable.append(path)
                continue
            out.append((path, facts_before, facts_after))
        return out, unreadable

    def _t_test_integrity_no_deletions(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        changes, unreadable = self._test_change(params)
        findings = [f"test file {p} cannot be analyzed" for p in unreadable]
        for path, before, after in changes:
            gone = (before.tests if before else frozenset()) - (after.tests if after else frozenset())
            findings += [f"test {path}::{t} was deleted" for t in sorted(gone)]
        return findings

    def _t_test_integrity_no_skips(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        changes, unreadable = self._test_change(params)
        findings = [f"test file {p} cannot be analyzed" for p in unreadable]
        for path, before, after in changes:
            new = (after.skipped if after else frozenset()) - (before.skipped if before else frozenset())
            findings += [f"test {path}::{t} is now skipped" for t in sorted(new)]
        return findings

    def _t_test_integrity_no_xfail(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        changes, unreadable = self._test_change(params)
        findings = [f"test file {p} cannot be analyzed" for p in unreadable]
        for path, before, after in changes:
            new = (after.xfail if after else frozenset()) - (before.xfail if before else frozenset())
            findings += [f"test {path}::{t} is now expected to fail" for t in sorted(new)]
        return findings

    def _t_test_integrity_fewer_assertions(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        changes, _ = self._test_change(params)
        findings = []
        for path, before, after in changes:
            if before is None or after is None:
                continue
            old, new = dict(before.assertions), dict(after.assertions)
            findings += [f"test {path}::{t} has fewer assertions ({old[t]} -> {new[t]})"
                         for t in sorted(set(old) & set(new)) if new[t] < old[t]]
        return findings

    def _t_test_integrity_widened_tolerance(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        changes, _ = self._test_change(params)
        findings = []
        for path, before, after in changes:
            if before is None or after is None:
                continue
            old, new = dict(before.tolerances), dict(after.tolerances)
            findings += [f"test {path}::{t} widened a tolerance ({old[t]:g} -> {new[t]:g})"
                         for t in sorted(set(old) & set(new)) if new[t] > old[t]]
        return findings

    def _t_obligation_no_new_stubs(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        findings = []
        for path, (before, after) in self.changed_files.items():
            if after is None or not path.endswith(".py") or py.is_test_file(path):
                continue
            if not py.parses(after):
                findings.append(f"{path} cannot be analyzed")
                continue
            new = py.stubs(after) - (py.stubs(before) if before is not None else frozenset())
            findings += [f"{path}: {name} is a placeholder" for name in sorted(new)]
        return findings

    def _t_obligation_required_artifact(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        """Present in the candidate and linked by a derived ``TESTS`` relation: a test module imports it."""

        artifact = params.get("artifact")
        if self.frame is None:
            return ["a required artifact needs a candidate"]
        cand = self.frame.candidate_tree
        if artifact not in cand:
            return [f"required artifact {artifact} is absent"]
        if not str(artifact).endswith(".py"):
            return [f"required artifact {artifact} is in a language the pinned analyzers do not cover"]
        modules = set(py.module_names(artifact))
        for path in cand:
            if py.is_test_file(path) and path != artifact and modules & set(py.imports(path, cand[path].data).modules):
                return []
        return [f"required artifact {artifact} is linked by no TESTS relation"]

    def _frozen_symbols(self, params: dict, contract: Contract) -> list[str]:
        return sorted(set(contract.frozen) | set(params.get("symbols") or ()))

    def _t_boundary_frozen_interface(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        if self.frame is None:
            return []
        base, cand = self.frame.base_tree, self.frame.candidate_tree
        findings = []
        for symbol in self._frozen_symbols(params, contract):
            homes = []
            for path in base:
                if not path.endswith(".py"):
                    continue
                for module in py.module_names(path):
                    if symbol.startswith(module + "."):
                        homes.append((len(module), path, symbol[len(module) + 1:]))
            if not homes:
                findings.append(f"frozen symbol {symbol} is not a public name of any analyzed module")
                continue
            _, path, qualname = max(homes)
            before = py.public_interface(base[path].data).get(qualname)
            after = py.public_interface(cand[path].data).get(qualname) if path in cand else None
            if before is None:
                findings.append(f"frozen symbol {symbol} is not public in {path}")
            elif after != before:
                findings.append(f"frozen symbol {symbol} changed: {before} -> {after or 'removed'}")
        return findings

    def _t_boundary_dependency_allowance(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        allowed = {py.requirement_name(r) for lang, reqs in contract.dependencies if lang == "python" for r in reqs}
        allowed |= {py.requirement_name(r) for r in params.get("allowance") or ()}
        findings = []
        for path, (before, after) in self.changed_files.items():
            name = path.rsplit("/", 1)[-1]
            if name in _OTHER_MANIFESTS:
                findings.append(f"dependency manifest {path} is of a language this ruleset does not analyze")
                continue
            new = py.declared_requirements(path, after) if after is not None else None
            if new is None:
                continue
            old = py.declared_requirements(path, before) if before is not None else frozenset()
            findings += [f"{path} adds {r}, outside the dependency allowance" for r in sorted(new - (old or frozenset()) - allowed)]
        return findings

    def _t_boundary_credential_values(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        patterns = list(_CREDENTIALS) + [re.compile(p) for p in params.get("patterns") or () if isinstance(p, str)]
        findings = []
        for path, (before, after) in self.changed_files.items():
            if after is None:
                continue
            old_lines = set((before or b"").decode("utf-8", "replace").splitlines())
            for line in after.decode("utf-8", "replace").splitlines():
                if line in old_lines:
                    continue
                if any(p.search(line) for p in patterns) or any(_entropy(t) >= 4.5 for t in _TOKEN.findall(line)):
                    findings.append(f"{path}: an added line carries a credential-shaped value")
                    break
        return findings

    # -- HEURISTIC signals over the result's own text ----------------------------------------------

    def _strings(self) -> list[str]:
        out: list[str] = []

        def walk(value: Any) -> None:
            if isinstance(value, str):
                out.append(value)
            elif isinstance(value, dict):
                for v in value.values():
                    walk(v)
            elif isinstance(value, list):
                for v in value:
                    walk(v)

        walk(self.slots)
        return out

    def _t_faithfulness_certainty_vocabulary(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        return [f"certainty vocabulary: {m.group(0)!r}" for text in self._strings() for m in [_CERTAINTY.search(text)] if m]

    def _t_faithfulness_prose_numbers(self, params: dict, contract: Contract, item: Item | None) -> list[str]:
        cited = {c.get("claim") for c in self.slots.get("claims") or [] if isinstance(c, dict) and c.get("records")}
        return [f"a number in prose without a cited record: {text[:60]!r}" for text in self._strings()
                if _NUMBER.search(text) and text not in cited]


def _entropy(token: str) -> float:
    """Shannon entropy in bits per character."""

    counts: dict[str, int] = {}
    for ch in token:
        counts[ch] = counts.get(ch, 0) + 1
    return -sum(c / len(token) * math.log2(c / len(token)) for c in counts.values())
