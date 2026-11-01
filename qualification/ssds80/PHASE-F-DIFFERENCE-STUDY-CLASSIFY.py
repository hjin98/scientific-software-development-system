"""F124's classification of a difference-study report (Phase F step 11b), by the rules of the preliminary
classification of 6ae91c3d (same observation identities: sha256 of the canonical ``{"source", "finding"}``).

    python3 PHASE-F-DIFFERENCE-STUDY-CLASSIFY.py <report.json> <out.json> --status <status> [--expect-sha256 <hex>]

Every observation must match exactly one rule below; any other finding or consequence change stops the run
unclassified, for a human or a reviewer, instead of being forced into a class. No credential line or value is read.
"""

import argparse
import collections
import hashlib
import json
from pathlib import Path

REPAIR = "11ec88e4105124d70e3b1e606f2ec370ef1cc841"  # declares the reserved leaves and creates .ssds/policy.toml
CREDENTIAL = "if policy enabled it; supplemental template, no current-policy verdict"
PROTECTED = "would be refused if agent-made; authorship not established"
REASONS = {
    "reserved_leaf_genesis_deviation": {"class": "iii", "meaning": "Before the reserved-leaf repair commit 11ec88e4 the bounded historical genesis exempts only ssds.manifest and ssds.policy; their absence on each evaluated tree is the declared genesis deviation."},
    "reserved_leaf_repair_quarantined_in_scratch": {"class": "iii", "meaning": "From 11ec88e4 the trees declare the leaves, but the scratch genesis has no counterpart of the human ABSORB adoption that SD-69 makes the exception and that ssdp-shadow-2 admitted at position 2 (ssdp-shadow-3's own genesis declares the leaves); the declaration delta stays quarantined, so effective structure keeps the genesis deviation. Scratch-genesis rule, not a document-control or SSDS defect."},
    "reserved_leaf_repair_absorbed_as_foreign_change": {"class": "iii", "meaning": "Absorbing 11ec88e4 quarantines its eight reserved-leaf declaration keys and derives their INTAKE obligations (Manual 8.6, 18.2, 18.5): absorption never changes the effective structure and Admission never adopts on its own. ssdp-shadow-2 received the same quarantine and then the human ABSORB adoption at position 2 (SD-69); the scratch genesis has no counterpart. Consequence of the scratch genesis rule, not a refusal or defect."},
    "protected_touch_authorship_unestablished": {"class": "v", "meaning": "11ec88e4 creates .ssds/policy.toml, the genesis-named policy path that protected_surfaces always protects (the committed policy itself lists no surfaces; the manifest is not protected). Row 11ec88e4 touches it by path and by authoring the ssds.policy unit. While ssds.policy stays quarantined in scratch, the file belongs to ssds.unclassified, so protected_touched flags every later write-set touch of that unit (unit granularity; the frozen source words this 'contains a protected surface'), although the later rows never change the policy file. In any structure the Manual accepts ssds.policy is its own leaf and unit- and path-level detection coincide; this is a conservative consequence of the class iii deviation, not an SSDS defect. The agent-authorship predicate is not established; no current-policy refusal or defect follows."},
    "unmet_policy_enablement": {"class": "v", "meaning": "Supplemental credential-values template if policy enabled it; enablement not established. No credential value or actual defect is inferred; matched lines/values are neither retained nor reconstructed."},
}


def identity(source: dict, finding) -> str:
    body = json.dumps({"source": source, "finding": finding}, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(body).hexdigest()


def classify(report: dict) -> list[dict]:
    order = [row["commit"] for row in report["commits"]]
    after_repair = set(order[order.index(REPAIR) + 1:]) if REPAIR in order else set()
    out = []

    def add(row, check, index, finding, code, reason):
        source = {"commit": row["commit"], "check": check, "index": index}
        out.append({"id": identity(source, finding), "source": source, "code": code,
                    "class": REASONS[reason]["class"], "reason": reason})

    for row in report["commits"]:
        checks = row["checks"]
        if set(checks) != {"1", "2", "3", "4"} or set(checks["1"]) != {"credential_template", "request_scan"}:
            raise SystemExit(f"{row['commit']}: unexpected check keys: unclassified")
        if checks["4"].get("status") != "vacuous":
            raise SystemExit(f"{row['commit']}: check 4 is not vacuous: unclassified")
        if not isinstance(checks["1"]["request_scan"], str) or not checks["1"]["request_scan"].startswith("no submitted"):
            raise SystemExit(f"{row['commit']}: check 1's request scan found something: unclassified")
        # check 2: exactly the two exempted leaves, except at the repair commit, which declares them
        units = sorted(f.get("unit") for f in checks["2"])
        if units != ([] if row["commit"] == REPAIR else ["ssds.manifest", "ssds.policy"]):
            raise SystemExit(f"{row['commit']}: check 2 units {units}: unclassified")
        for index, finding in enumerate(checks["2"]):
            if finding["code"] != "STRUCT_RESERVED_LEAF" or finding["unit"] not in ("ssds.manifest", "ssds.policy"):
                raise SystemExit(f"{row['commit']}: check 2 finding {finding['code']}: unclassified")
            reason = ("reserved_leaf_repair_quarantined_in_scratch" if row["commit"] in after_repair
                      else "reserved_leaf_genesis_deviation")
            add(row, "2", index, finding, finding["code"], reason)
        for index, finding in enumerate(checks["3"]):
            # a protected touch only from the repair commit on: of ssds.policy there, of ssds.unclassified after
            owners = ["ssds.policy"] if row["commit"] == REPAIR else ["ssds.unclassified"]
            if finding["code"] != "AUTH_PROTECTED" or finding["applicability"] != PROTECTED \
                    or (row["commit"] != REPAIR and row["commit"] not in after_repair) or finding["owners"] != owners:
                raise SystemExit(f"{row['commit']}: check 3 finding {finding['code']}: unclassified")
            add(row, "3", index, finding, finding["code"], "protected_touch_authorship_unestablished")
        for index, finding in enumerate(checks["1"]["credential_template"]):
            if finding["code"] != "credential_values" or finding["applicability"] != CREDENTIAL:
                raise SystemExit(f"{row['commit']}: check 1 finding {finding['code']}: unclassified")
            add(row, "1.credential_template", index, finding, finding["code"], "unmet_policy_enablement")
        for group, changes in row["consequence_changes"].items():
            for change, items in changes.items():
                for index, item in enumerate(items):
                    value = item.get("value") or {}
                    intake = group == "obligations" and change == "added" and value.get("kind") == "INTAKE" \
                        and value.get("detail") == "quarantined delta" \
                        and value.get("about", [None])[0] in ("ssds.manifest", "ssds.policy")
                    key = None
                    if group == "quarantine" and isinstance(item.get("key"), str):
                        try:
                            key = json.loads(item["key"])  # a quarantine key is the JSON text of (unit, field)
                        except ValueError:
                            key = None
                    quarantined = group == "quarantine" and change == "added" and isinstance(key, list) \
                        and key[:1] in (["ssds.manifest"], ["ssds.policy"])
                    if row["commit"] != REPAIR or not (intake or quarantined):
                        raise SystemExit(f"{row['commit']}: consequence {group}.{change}: unclassified")
                    add(row, f"consequences.{group}.{change}", index, item, None,
                        "reserved_leaf_repair_absorbed_as_foreign_change")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("report", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument("--status", required=True)
    parser.add_argument("--expect-sha256")
    parser.add_argument("--limits", nargs="*", default=[])
    args = parser.parse_args()
    raw = args.report.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if args.expect_sha256 and sha != args.expect_sha256:
        raise SystemExit(f"report sha256 {sha} is not {args.expect_sha256}")
    report = json.loads(raw)
    if report["execution"]["status"] != "COMPLETE" or report["boundary"]["status"] != "PASSED":
        raise SystemExit("the report is not COMPLETE with its final boundary PASSED")
    rows = classify(report)
    result = {"schema": 1, "status": args.status, "asserter": "AI implementing agent, Claude family",
              "governing_protocol": report["governing_protocol"],
              "authority": "Phase F F123/F124; class reasons are agent interpretations until the other-family review",
              "candidate": report["candidate"], "source_report": args.report.name, "source_sha256": sha,
              "completed_deltas": report["summary"]["evaluated"],
              "expected_deltas": report["execution"]["expected_deltas"], "reasons": REASONS,
              "summary": dict(collections.Counter(r["class"] for r in rows)),
              "by_reason": dict(collections.Counter(r["reason"] for r in rows)),
              "observations": rows, "limits": args.limits}
    if args.out.exists():
        raise SystemExit(f"{args.out} exists; never overwrite a classification")
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"observations": len(rows), "summary": result["summary"], "by_reason": result["by_reason"],
                      "sha256": hashlib.sha256(args.out.read_bytes()).hexdigest()}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
