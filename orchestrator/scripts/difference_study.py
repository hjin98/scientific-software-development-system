#!/usr/bin/env python3
"""Phase F 11a (F123): record-free checks and scratch absorption consequences.

No actual Admission verdict is inferred from supplemental policy/authorship counterfactuals. This script never
opens a real ledger. Give a full immutable candidate ID and a new scratch SSDS_HOME outside all repositories.
The report and throwaway genesis remain there for inspection; classification belongs to frozen-candidate 11b.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from collections import Counter
from contextlib import contextmanager
from dataclasses import asdict
from functools import lru_cache
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True
REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "orchestrator" / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from shadow_boundary import differences, git, outside, snapshot  # noqa: E402
from ssds.admission.genesis import AdmissionHome, GenesisSpec, admit_genesis, prepare_genesis  # noqa: E402
from ssds.admission.request import expected_head, observe_only, shadow_boundary  # noqa: E402
from ssds.content import GitReadError, ancestry, read_tree  # noqa: E402
from ssds.core.api.v1 import canonical_json  # noqa: E402
from ssds.derivation import Consequences, Frame, Transformation, Workflow, derive, protected_touched  # noqa: E402
from ssds.derivation import baseline  # noqa: E402
from ssds.derivation.conformance import Conformance  # noqa: E402
from ssds.derivation.queries import _drifted  # noqa: E402
from ssds.ledger.read import is_commit, transformation_id  # noqa: E402

LEDGER = "difference-study"
PROTOCOL = "7.2.1"
REAL_BASELINE = "53d5a22c04f8c8035dfccd4577a3cdd9ece06a2b"
DEFAULT_MODES = {"ssdp.protocol": {"mode": "LEGACY", "protocol": PROTOCOL},
                 "ssds8.manual": {"mode": "LEGACY", "protocol": PROTOCOL}, "*": {"mode": "UNGOVERNED"}}
EXEMPT = frozenset({"ssds.manifest", "ssds.policy"})


@contextmanager
def historical_genesis_rule():
    """The two historical exemptions only; all post-genesis checks use the current owners."""
    owner = baseline.reserved_leaf_problems
    with patch.object(baseline, "reserved_leaf_problems",
                      lambda structure: [(u, d) for u, d in owner(structure) if u not in EXEMPT]):
        yield


def scratch_home(repository: Path, proposed: Path) -> AdmissionHome:
    path = proposed.expanduser().resolve()
    for forbidden in (Path.home() / ".ssds", Path.home() / ".ssh"):
        forbidden = forbidden.resolve()
        if path.is_relative_to(forbidden) or forbidden.is_relative_to(path):
            raise ValueError("the scratch home must be disjoint from the real SSDS home and stakeholder keys")
    outside(repository, path)
    if path.exists() or path.is_symlink():
        raise ValueError("the scratch home must be new: no existing ledger or workspace is reused")
    home = AdmissionHome(path)
    home.outside_repositories()
    path.mkdir(mode=0o700, parents=True, exist_ok=False)
    return home


def population(repository: Path, candidate: str, trees) -> tuple[list[str], list[dict]]:
    if not is_commit(candidate):
        raise ValueError("candidate must be a full immutable commit identity")
    commits = git(repository, "rev-list", "--first-parent", "--reverse", candidate).decode("ascii").split()
    excluded = []
    with historical_genesis_rule():
        for index, commit in enumerate(commits):
            if not git(repository, "ls-tree", "--name-only", commit, "--", ".ssds/manifest.toml").strip():
                problems = ["no unit manifest at .ssds/manifest.toml in the baseline tree"]
            else:
                problems = list(baseline.baseline_structure(trees(commit), ".ssds/manifest.toml").problems)
            if not problems:
                return commits[index:], excluded
            excluded.append({"commit": commit, "initialization_problems": problems})
    raise ValueError("no first-parent commit admits the bounded historical scratch genesis")


def initialize(repository: Path, home: AdmissionHome, first: str, trees, modes: dict) -> None:
    # These are newly generated fixture credentials, used only in this new scratch home.
    key = home.root / "study-approver"
    subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-C", "scratch-study", "-f", str(key)],
                   check=True, stdin=subprocess.DEVNULL, capture_output=True, timeout=60)
    public = key.with_suffix(".pub").read_text().strip()
    spec = GenesisSpec(project="phase-f-difference-study", ledger_id=LEDGER, product_repository=repository,
                       baseline_commit=first, human_keys=(public,), protocol=PROTOCOL, modes=modes)
    with historical_genesis_rule():
        prepared = prepare_genesis(spec, home, trees)
        if not prepared.valid:
            raise ValueError(f"scratch genesis refused: {prepared.problems}")
        message = home.root / "study-approval.txt"
        message.write_bytes(prepared.message)
        subprocess.run(["ssh-keygen", "-q", "-Y", "sign", "-f", str(key), "-n", "ssds", str(message)],
                       check=True, capture_output=True, stdin=subprocess.DEVNULL, timeout=60)
        admit_genesis(home, LEDGER, message.with_suffix(".txt.sig").read_text())


class CommitAdvisory(Conformance):
    """Only the real diff-template owner, with no contract or submitting result (F123)."""
    def __init__(self, support, frame):
        self.s = support.s
        self._frame = frame

    @property
    def frame(self):
        return self._frame


def checks(support, parent: str, candidate: str) -> dict:
    state = support.s
    if state.h.head(state.n) != parent:
        raise ValueError("the hypothetical request's parent is not the held observed tree")
    frame = Frame(state.h, state.n, Transformation(transformation_id(parent, candidate), parent, candidate), None)
    if frame.merged is None:
        raise ValueError("a direct first-parent delta unexpectedly has no clean merge")
    structure = [asdict(f) for f in frame.structural.findings]
    structure += [{"code": "ENACTMENT_MISSING", "unit": u, "detail": "no prospective acceptance on this chain"}
                  for u in frame.structural.tenure_starts]
    protected = [{"code": "AUTH_PROTECTED", "detail": detail, "owners": list(owners),
                  "applicability": "would be refused if agent-made; authorship not established"}
                 for detail, owners in protected_touched(frame, state.policy, state.h.policy_path)]
    credentials = [{"code": "credential_values", "detail": detail, "owners": list(owners),
                    "applicability": "if policy enabled it; supplemental template, no current-policy verdict"}
                   for detail, owners in CommitAdvisory(support, frame)._t_boundary_credential_values({}, None, None)]
    return {"1": {"request_scan": "no submitted strings or LEDGER objects to scan",
                  "credential_template": credentials}, "2": structure, "3": protected,
            "4": {"status": "vacuous", "reason": "no evaluated records: no relevant record dependencies or cycles"}}


def consequence_state(support) -> dict:
    state, consequence, workflow = support.s, Consequences(support), Workflow(support)
    subjects = sorted(u for u, unit in state.view.structure.units.items() if unit.subject)
    obligations = {}
    for o in consequence.obligations:
        identity = "s3:" + hashlib.sha256(canonical_json({"kind": o.kind, "about": list(o.about)})).hexdigest()
        obligations[identity] = {"id": identity, **asdict(o), "discharge": "OPEN"}
    for o in workflow.obligations:
        obligations[o.id] = {"id": o.id, "kind": o.kind, "target": o.target, "params": o.params,
                             "discharge": workflow.discharge(o)}
    return {"quarantine": {json.dumps(key): list(key) for key in sorted(state.s0.quarantine)},
            "ill_formed": {u: [asdict(d) for d in state.s0.defects
                               if d.unit in state.view.structure.units and state.view.structure.subj(d.unit) == u]
                           for u in subjects if not state.s0.well_formed(u)},
            "drift": {u: True for u in subjects if _drifted(workflow, u)}, "obligations": obligations,
            "integrity": {json.dumps([f.code, f.about, f.detail]): asdict(f) for f in consequence.findings
                          if f.integrity}}


def changes(before: dict, after: dict) -> dict:
    return {field: {"added": [{"key": k, "value": new[k]} for k in sorted(new.keys() - old.keys())],
                    "removed": [{"key": k, "value": old[k]} for k in sorted(old.keys() - new.keys())],
                    "changed": [{"key": k, "before": old[k], "after": new[k]} for k in sorted(old.keys() & new.keys())
                                if old[k] != new[k]]}
            for field in before for old, new in [(before[field], after[field])]}


def study(repository: Path, candidate: str, proposed_home: Path, *, modes: dict | None = None,
          real_baseline: str | None = REAL_BASELINE) -> dict:
    repository = repository.resolve()
    # Validate the destination before any repository snapshot or scratch write.
    home = scratch_home(repository, proposed_home)
    before = snapshot(repository)

    @lru_cache(maxsize=8)
    def trees(commit):
        return read_tree(repository, commit)

    commits, excluded = population(repository, candidate, trees)
    if real_baseline is not None and real_baseline not in commits:
        raise ValueError("the real baseline must lie in the admitted first-parent population")
    modes = DEFAULT_MODES if modes is None else modes
    initialize(repository, home, commits[0], trees, modes)
    ledger_repo = home.ledger_repository(LEDGER)
    graph = ancestry(ledger_repo)
    admission = observe_only(home.root, LEDGER, trees, repository, graph, shadow_boundary)
    support = derive(admission.held_head(), trees, ancestry=graph)
    report_path = home.root / "difference-study.json"
    report = {"schema": 1, "governing_protocol": PROTOCOL, "candidate": candidate, "real_baseline": real_baseline,
              "initialization": {"commit": commits[0], "modes": modes, "consequences": None,
                                 "exempt_reserved_leaves": sorted(EXEMPT)},
              "excluded": excluded, "commits": [], "summary": {},
              "execution": {"status": "INCOMPLETE", "phase": "INITIAL_CONSEQUENCES",
                            "expected_deltas": len(commits) - 1, "pending": None},
              "boundary": {"status": "UNEXECUTED", "unchanged": None, "differences": [],
                           "scope": "endpoint fingerprints; transient reverted writes and access times excluded"},
              "limits": ["shadow infrastructure qualification; no authority or scientific outcome claim",
                         "checks 1 and 3 include conditional observations, not current-policy refusals",
                         "check 4 is vacuous; record-dependent checks need an authorized campaign",
                         "consequences belong to this scratch ledger, not the real ledger",
                         "classification and independent other-family review belong to frozen-candidate 11b"]}
    counts = Counter()

    def save() -> None:
        """One inspectable report, replaced only after a whole new JSON document is written.

        Completed rows/counts exclude the pending commit even if its absorption finished.
        This is process-interruption visibility, not a resumable ledger or power-loss guarantee.
        """
        evaluated = len(report["commits"])
        report["summary"] = {"evaluated": evaluated, "excluded": len(excluded),
                             "findings_by_code": dict(sorted(counts.items()))}
        if real_baseline is not None:
            split = commits.index(real_baseline)
            report["summary"].update(before_or_at_real_baseline=min(evaluated, split),
                                     after_real_baseline=max(0, evaluated - split))
        temporary = report_path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        temporary.replace(report_path)

    save()
    initial = previous = consequence_state(support)
    report["initialization"]["consequences"] = initial
    for parent, commit in zip(commits, commits[1:]):
        report["execution"].update(phase="CHECKS", pending={"parent": parent, "commit": commit})
        save()
        found = checks(support, parent, commit)
        report["execution"]["phase"] = "ABSORPTION"
        save()
        chain = admission.held_head()
        if expected_head(chain.entries[:chain.readable_through + 1]) != parent:
            raise ValueError("scratch ledger moved outside the study")
        admission.absorb(list(chain.entries[:chain.readable_through + 1]), commit)
        report["execution"]["phase"] = "CONSEQUENCES"
        save()
        support = derive(admission.held_head(), trees, ancestry=graph)
        current = consequence_state(support)
        report["commits"].append({"commit": commit, "parent": parent, "checks": found,
                                  "consequence_changes": changes(previous, current)})
        for finding in found["2"] + found["3"] + found["1"]["credential_template"]:
            counts[finding["code"]] += 1
        previous = current
        report["execution"].update(phase="BETWEEN_COMMITS", pending=None)
        save()
    report["execution"]["phase"] = "BOUNDARY"
    save()
    changed = differences(before, snapshot(repository))
    report["boundary"] = {"status": "FAILED" if changed else "PASSED", "unchanged": not changed,
                          "differences": changed,
                          "scope": "endpoint fingerprints; transient reverted writes and access times excluded"}
    report["execution"].update(status="FAILED_BOUNDARY" if changed else "COMPLETE", phase="FINISHED")
    save()
    if changed:
        raise ValueError(f"product boundary changed; inspect {report_path}")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True, type=Path)
    parser.add_argument("--candidate", required=True, help="full frozen commit identity")
    parser.add_argument("--baseline", default=REAL_BASELINE, help="full real-ledger baseline identity")
    args = parser.parse_args(argv)
    home = os.environ.get("SSDS_HOME")
    if not home:
        parser.error("SSDS_HOME must explicitly name a new scratch home")
    try:
        report = study(args.repository, args.candidate, Path(home), real_baseline=args.baseline)
    except (ValueError, OSError, subprocess.SubprocessError, GitReadError) as exc:
        parser.exit(1, f"difference study refused: {exc}\n")
    print(json.dumps({"report": str(Path(home).resolve() / "difference-study.json"), **report["summary"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
