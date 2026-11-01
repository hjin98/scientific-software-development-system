"""The fixed helper of step 10d on ``ssdp-shadow-3`` (Phase F reading F126), run only through
``PHASE-F-10D-SHADOW-3-RUN.py ... script <this file> <subcommand> --ledger <id> ...``. Every read goes through the
program's own owners (the Composition, the derivation, Admission's checks); nothing here signs, and the only file it
writes is its ``--out``, which must lie outside the repository.

    state                                              W2 and W6: chain, reserved leaves, quarantine, policy object
    records --kind finding --narrative <commit>:<path> W4a: the FINDING of SD-97 (narrative: a committed blob)
    records --kind availability                        W5a: the policy object's AVAILABILITY of SD-97
    records --kind acknowledge --finding <record id>   W7a: an ACKNOWLEDGE of the FINDING's attention obligation
    check --request <request id>                       W4a, W5a, W7a: Admission's step-1 checks of a prepared request
    baseline --finding <record id>                     W7b: the ledger and obligation before the refused decide
    verify-decide --request <id> --baseline <file>     W7c: the signature, verified independently, and no append
    candidate                                          W8: one candidate request through the library API, refused
"""

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from ssds.admission.checks import record_problems, request_problems
from ssds.admission.request import BoundaryRefused, expected_head, request_id, request_message
from ssds.cli import Composition, read_prepared
from ssds.derivation import Workflow, derive, trust_roots
from ssds.ledger.read import with_id
from ssds.ledger.schema import record_violations
from ssds.ledger.signatures import verify_sshsig

REPOSITORY = Path(__file__).resolve().parents[2]
BRANCH = "ssds-8.0-graph-native-architecture"
GENESIS_POLICY = "sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1"
RESERVED = {"ssds.manifest": "MANIFEST", "ssds.policy": "POLICY", "ssds.unclassified": "UNCLASSIFIED"}
FINDING_UNITS = ["orchestrator.program", "ssds.manifest", "ssds.policy"]


def fail(reason: str) -> None:
    print(json.dumps({"failed": reason}, indent=2))
    raise SystemExit(1)


def git(*args: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPOSITORY), *args], check=True, capture_output=True).stdout


def outside(path: Path) -> Path:
    path = path.resolve()
    if path.is_relative_to(REPOSITORY):
        fail(f"{path} is inside the repository; a window writes nothing there")
    return path


def readable(c: Composition):
    chain = c.access.chain()
    if chain.halt is not None or chain.readable_through != len(chain.entries) - 1:
        fail(f"the chain is not readable through its head: halt {chain.halt}, reasons {chain.halt_reasons}")
    return chain


def entry_summary(entry) -> dict:
    body = entry.entry
    admission = body.get("admission") or {}
    return {"position": entry.position, "digest": entry.digest, "entry_kind": body.get("entry_kind"),
            "obs": body.get("obs"), "decision": admission.get("decision"),
            "lifecycle": (entry.lifecycle or {}).get("kind"),
            "records": [{"kind": r.get("kind"), "id": r.get("id")} for r in entry.records]}


def state(c: Composition, args) -> dict:
    chain = readable(c)
    support = derive(chain, c.trees, ancestry=c.access.ancestry())
    s = support.s
    structure = s.view.structure
    reserved = {uid: structure.kind(uid) if uid in structure.units else None for uid in RESERVED}
    quarantine = sorted([list(key) for key in s.s0.quarantine])
    policy = s.h.ruleset(s.n)["policy"]
    data = s.h.objects.get(policy)
    out = {"ledger": c.access.ledger_id, "position": s.n, "entries": len(chain.entries),
           "expected_head": expected_head(chain.entries), "humans": sorted(trust_roots(chain.entries).humans),
           "reserved_leaves": reserved, "quarantine": quarantine,
           "policy": policy, "policy_unchanged": policy == GENESIS_POLICY,
           "policy_object": None if data is None else {
               "bytes": len(data), "digest_matches": "sha256:" + hashlib.sha256(data).hexdigest() == policy,
               "text": data.decode("utf-8", "replace")},
           # observed, not a criterion (F126 W2): the derivation's latest acting AVAILABILITY outcome on the object
           "policy_availability": support.a._availability.get(policy),
           "chain": [entry_summary(e) for e in chain.entries]}
    problems = [f"{uid} is {reserved[uid]}, not {kind}" for uid, kind in RESERVED.items() if reserved[uid] != kind]
    problems += ["the quarantine is not empty"] if quarantine else []
    problems += ["the policy digest changed"] if policy != GENESIS_POLICY else []
    problems += ["the policy object is missing or mismatched"] if not (out["policy_object"] or {}).get(
        "digest_matches") else []
    out["problems"] = problems
    return out


def envelope(chain, kind: str, target, outcome, reason, basis, refs, fields) -> dict:
    genesis = chain.entries[0].lifecycle
    return {"kind": kind, "schema": 1, "frame": "ADMITTED", "target": target, "basis": basis, "outcome": outcome,
            "reason": reason, "supersedes": [], "provenance": None, "refs": refs, "governs": genesis["governs"],
            "ruleset": genesis["ruleset"], "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "fields": fields}


def attention(c: Composition, chain, finding: str):
    w = Workflow(derive(chain, c.trees, ancestry=c.access.ancestry()))
    found = [o for o in w.obligations if o.kind == "HUMAN_ATTENTION" and finding in json.dumps(o.target)]
    if len(found) != 1:
        fail(f"{len(found)} attention obligations target {finding}, not one")
    return w, found[0]


def records(c: Composition, args) -> dict:
    chain = readable(c)
    out_dir = outside(args.out)
    if args.kind == "finding":
        commit, _, path = (args.narrative or "").partition(":")
        if not commit or not path:
            fail("--narrative is <commit>:<path>")
        commit = git("rev-parse", "--verify", commit + "^{commit}").decode().strip()
        head = git("rev-parse", "--verify", "refs/heads/" + BRANCH).decode().strip()
        if subprocess.run(["git", "-C", str(REPOSITORY), "merge-base", "--is-ancestor", commit, head]).returncode:
            fail(f"the narrative commit {commit} is not on {BRANCH}")
        blob = git("rev-parse", "--verify", f"{commit}:{path}").decode().strip()
        content = git("cat-file", "blob", blob)
        ref = {"store": "REPO", "digest": "sha256:" + hashlib.sha256(content).hexdigest(),
               "media_type": "text/markdown", "locator": blob}
        record = envelope(chain, "FINDING", {"units": FINDING_UNITS}, None, ["INSPECTABILITY_GAP"], [], [ref],
                          {"materiality": "MATERIAL", "blocking": False})
        facts = {"narrative": {"commit": commit, "path": path, "blob": blob, "bytes": len(content)}}
    elif args.kind == "availability":
        s = derive(chain, c.trees, ancestry=c.access.ancestry()).s
        policy = s.h.ruleset(s.n)["policy"]
        data = s.h.objects.get(policy)
        if policy != GENESIS_POLICY or data is None or "sha256:" + hashlib.sha256(data).hexdigest() != policy:
            fail(f"the policy object {policy} is not the genesis object, held with matching bytes")
        record = envelope(chain, "AVAILABILITY", {"digest": policy}, "AVAILABLE", [], [], [], {})
        facts = {"policy_object": {"digest": policy, "bytes": len(data)}}
    else:
        if not args.finding:
            fail("--finding names the admitted FINDING")
        w, obligation = attention(c, chain, args.finding)
        if w.discharge(obligation) != "OPEN":
            fail(f"the attention obligation is {w.discharge(obligation)}, not OPEN")
        record = envelope(chain, "HUMAN_DECISION", {"obligation": obligation.id}, "ACKNOWLEDGE", [],
                          [{"mode": "identity", "target": {"record": args.finding}, "class": "EXACT"}], [], {})
        facts = {"obligation": obligation.id, "holder": obligation.holder}
    actor = sorted(trust_roots(chain.entries).humans)[0]
    problems = record_violations(with_id({"actor": actor, "actor_class": "HUMAN", "binding": None, **record}))
    if problems:
        fail(f"the {args.kind} record violates the schema: {problems}")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{args.kind}.json"
    target.write_text(json.dumps([record], indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"ledger": c.access.ledger_id, "position": len(chain.entries) - 1, "file": str(target),
            "sha256": hashlib.sha256(target.read_bytes()).hexdigest(), **facts, "record": record}


def prepared(c: Composition, rid: str):
    store = c.state()
    raw = store.read_private(c.request_parts(rid, "request.json"))
    if raw is None:
        fail(f"no prepared request {rid}")
    request = json.loads(raw)
    if request_id(request) != rid:
        fail(f"request.json is {request_id(request)}, not {rid}")
    return store, request


def check(c: Composition, args) -> dict:
    store, request = prepared(c, args.request)
    out = {"request": args.request, "request_problems": request_problems(request),
           "records": [{"kind": r.get("kind"), "id": r.get("id"), "provenance": r.get("provenance"),
                        "problems": record_problems(r, record_violations)} for r in request["records"]],
           "message_matches": store.read_private(c.request_parts(args.request, "request-message.txt"))
           == request_message(request),
           "signature_present": store.read_private(c.request_parts(args.request, "request-message.txt.sig"))
           is not None,
           "summary": (store.read_private(c.request_parts(args.request, "summary.txt")) or b"").decode()}
    bad = out["request_problems"] or any(r["problems"] or r["provenance"] is not None for r in out["records"])
    if bad or not out["message_matches"]:
        print(json.dumps(out, indent=2, sort_keys=True))
        fail("the prepared request does not pass Admission's step-1 checks")
    return out


def boundary_lines(c: Composition) -> list[str]:
    raw = c.state().read_private(("state", c.access.ledger_id, "boundary.jsonl"))
    return [] if raw is None else raw.decode().splitlines()


def baseline(c: Composition, args) -> dict:
    chain = readable(c)
    w, obligation = attention(c, chain, args.finding)
    result = {"ledger": c.access.ledger_id, "entries": len(chain.entries), "last_digest": chain.entries[-1].digest,
              "expected_head": expected_head(chain.entries), "finding": args.finding, "obligation": obligation.id,
              "discharge": w.discharge(obligation), "holder": obligation.holder,
              "human_decisions": sum(1 for rid in w.s.of_kind("HUMAN_DECISION")),
              "boundary_lines": len(boundary_lines(c))}
    if result["discharge"] != "OPEN" or result["human_decisions"]:
        fail(f"the baseline is not an OPEN obligation with no human decision: {result}")
    outside(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def verify_decide(c: Composition, args) -> dict:
    before = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    store, request = prepared(c, args.request)
    loaded, signature = read_prepared(store.path(c.request_parts(args.request, "request.json")).parent)
    if loaded != request or len(request["records"]) != 1 or request["records"][0]["kind"] != "HUMAN_DECISION":
        fail("the prepared request is not the one HUMAN_DECISION")
    chain = readable(c)
    actor = request["records"][0]["actor"]
    public = trust_roots(chain.entries).humans.get(actor)
    verified = public is not None and verify_sshsig(public, request_message(request), signature)
    signed = request_id({**request, "binding": {"human": {"actor": actor, "signature": signature}}})  # as admitted
    w, obligation = attention(c, chain, before["finding"])
    lines = boundary_lines(c)
    refusals = [json.loads(line) for line in lines[before["boundary_lines"]:]]
    result = {"request": args.request, "signed_request": signed, "actor": actor, "signature_verified": verified,
              "entries": len(chain.entries), "last_digest": chain.entries[-1].digest,
              "appended": len(chain.entries) != before["entries"] or chain.entries[-1].digest != before["last_digest"],
              "obligation": obligation.id, "discharge": w.discharge(obligation), "holder": obligation.holder,
              "human_decisions": sum(1 for rid in w.s.of_kind("HUMAN_DECISION")), "new_boundary_lines": refusals}
    if not verified or result["appended"] or result["discharge"] != "OPEN" or result["human_decisions"] \
            or obligation.id != before["obligation"] or len(refusals) != 1 or refusals[0]["request_id"] != signed:
        print(json.dumps(result, indent=2, sort_keys=True))
        fail("the decide was not a verified, logged refusal with nothing appended")
    return result


def candidate(c: Composition, args) -> dict:
    chain = readable(c)
    before = len(boundary_lines(c))
    head = expected_head(chain.entries)
    request = {"binding": None, "claims": [], "base_position": len(chain.entries) - 1, "base_commit": head,
               "candidates": ["0" * 40], "adopted_deltas": [], "records": [], "objects": {}}
    try:
        c.admission().admit(request, head)
    except BoundaryRefused as exc:
        after = c.access.chain()
        lines = boundary_lines(c)[before:]
        result = {"refused_at_entry": str(exc), "request": request_id(request),
                  "appended": len(after.entries) != len(chain.entries)
                  or after.entries[-1].digest != chain.entries[-1].digest, "new_boundary_lines": lines}
        if result["appended"] or len(lines) != 1:
            print(json.dumps(result, indent=2, sort_keys=True))
            fail("the refusal appended or was not logged once")
        return result
    fail("NOT REFUSED: stop and report")


def main() -> int:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("state", "records", "check", "baseline", "verify-decide", "candidate"):
        p = commands.add_parser(name)
        p.add_argument("--ledger", required=True)
        p.add_argument("--repository", type=Path, default=REPOSITORY)
        if name == "records":
            p.add_argument("--kind", required=True, choices=("finding", "availability", "acknowledge"))
            p.add_argument("--narrative")
            p.add_argument("--finding")
            p.add_argument("--out", required=True, type=Path)
        if name in ("check", "verify-decide"):
            p.add_argument("--request", required=True)
        if name == "baseline":
            p.add_argument("--finding", required=True)
            p.add_argument("--out", required=True, type=Path)
        if name == "verify-decide":
            p.add_argument("--baseline", required=True, type=Path)
    args = parser.parse_args()
    if args.repository.resolve() != REPOSITORY:
        fail(f"--repository is {REPOSITORY}")
    c = Composition(args.ledger, args.repository)
    run = {"state": state, "records": records, "check": check, "baseline": baseline, "verify-decide": verify_decide,
           "candidate": candidate}[args.command]
    result = run(c, args)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result.get("problems") else 0


if __name__ == "__main__":
    raise SystemExit(main())
