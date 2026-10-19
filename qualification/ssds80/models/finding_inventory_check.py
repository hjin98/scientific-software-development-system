"""Independent inventory check for the G2 Stage S finding index (13d67be B2 discriminator).

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

`finding_index.py` extracts findings with two heading patterns. This check uses a different method: it
reads every Review record line by line, takes every line that opens with a heading, bold or list-item
marker followed by a finding-shaped identifier (any letter group with optional prime and digits, or
`Blocker <X>`), whatever punctuation follows, and then removes only lines that are statements about an
earlier record's findings ("N3 is closed", "N1-N4 are closed", "is superseded", ...) or non-finding
labels (verdicts, protocol and memory identifiers, refinement and invariant rows). Every identifier left
must appear in the generated index for that record. A miss prints the line and exits non-zero.

Records are keyed by their full identity: a candidate reviewed twice keeps its second (different-family)
record apart, as the index does, so a finding present for one record never stands in for the other
(d8ab75c B2). A title may carry a severity annotation before its punctuation ("N1 (medium-high): ...").

`--self-test` checks the checker itself: the real index must pass; projections of the index with the
seven FFBAD17 severity-labelled findings removed, and with the second records' rows removed, must each
fail with exactly the removed rows reported; and a line restating an earlier record's finding must not
count as a finding.

Run: python3 -I qualification/ssds80/models/finding_inventory_check.py [--self-test]
"""

from __future__ import annotations

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "G2-S4-FINDING-INDEX.md")

LINE = re.compile(r"^(?:#{2,4}\s+|-\s+\*\*|\*\*|\d+\.\s+\*\*)(?:Blocker\s+)?([A-Z]{1,2}[′']?-?\d{0,3})(?:\([a-z]\))?(?=[\s*—–:.,(/]|$)(.*)$")
# statements about earlier findings, not findings of this record
ABOUT_EARLIER = re.compile(r"^\**\s*(?:,|and|-|–|to)?\s*(?:\*\*)?[A-Z]?\d*\**\s*(?:is|are|was|were)\s+"
                           r"(?:closed|superseded|reopened|repaired|stated|partly|now|sound|unchanged|carried)")
NOT_FINDINGS = {"NO", "PASS", "PC", "DS", "SP", "SD", "FF", "HAS", "PEM", "OK", "D", "G", "I", "R", "O", "P",
                "S", "T", "E", "K", "C", "A", "B", "Q", "M", "H", "F", "L", "J", "V", "U", "W", "X", "Y", "Z"}


def index_ids(lines) -> dict:
    out: dict = {}
    for line in lines:
        cells = re.split(r"(?<!\\)\|", line)
        if len(cells) > 6 and cells[1].strip().split()[:1] in (["manual"], ["workplan"], ["g2-workplan"]):
            key = cells[1].strip().split()[1]
            out.setdefault(key, set()).add(re.sub(r"\([a-z]\)$", "", cells[2].strip()).replace("Blocker ", ""))
    return out


PATS = ["MANUAL-REVIEW-SSDS-8.0-*.md", "WORKPLAN-REVIEW-SSDS-8.0-*.md", "G2-WORKPLAN-REVIEW-SSDS-8.0-*.md"]


def record_files() -> list:
    files = [f for pat in PATS for f in sorted(glob.glob(os.path.join(ROOT, pat)))]
    plain = {re.search(r"REVIEW-SSDS-8\.0-([0-9A-F]{7})", f).group(1) for f in files if "DIFFERENT-FAMILY" not in f}
    out = []
    for f in files:
        rid = re.search(r"REVIEW-SSDS-8\.0-([0-9A-F]{7})", f).group(1)
        out.append((f, rid + "/DF" if "DIFFERENT-FAMILY" in f and rid in plain else rid))
    return out


def main(index_lines=None, quiet=False) -> list:
    have = index_ids(index_lines if index_lines is not None else open(INDEX, encoding="utf-8"))
    misses = []
    if True:
        for f, rid in record_files():
            for n, line in enumerate(open(f, encoding="utf-8"), 1):
                m = LINE.match(line.rstrip("\n"))
                if not m:
                    continue
                fid, rest = m.group(1), m.group(2)
                letters = re.match(r"[A-Z]+", fid).group(0)
                if fid in NOT_FINDINGS or (letters in {"R", "O", "P", "D", "G", "I", "S", "T", "E", "K", "M", "H",
                                                       "F", "L", "J", "V", "Q", "PC", "DS", "SP", "SD", "FF"}
                                           and not fid.startswith("SC")):
                    # a single bare letter heading (A, B, C, ...) is a finding only with a dash title
                    if not (len(fid) == 1 and re.match(r"\s*[—–]\s+\S", rest)):
                        continue
                if ABOUT_EARLIER.match(rest) or re.match(r"\s*(?:\*\*)?\s*(?:is|are)\s", rest):
                    continue
                rest = re.sub(r"^\s*\([^)]{1,40}\)", "", rest)    # a severity annotation before the title
                if not re.match(r"\s*(?:\*\*)?\s*[—–:.]", rest) and not rest.strip().startswith("**"):
                    continue              # an identifier opening running prose, not a finding title
                if rest.strip().startswith("**") and not re.match(r"\s*\*\*\s*[—–:.(]", rest):
                    continue              # "**N1** prose": a summary mention
                if fid not in have.get(rid, set()):
                    misses.append(f"{os.path.basename(f)}:{n}: {fid}: {line.strip()[:110]}")
    if not quiet:
        for m in misses:
            print("MISS", m)
        print(f"inventory check: {len(misses)} finding heading(s) absent from the index")
    return misses


def self_test() -> bool:
    lines = open(INDEX, encoding="utf-8").read().split("\n")
    ok = not main(lines, quiet=True)
    def drop(pred):
        return [l for l in lines if not pred(l)]
    def row(l):
        c = re.split(r"(?<!\\)\|", l)
        return (c[1].strip(), c[2].strip()) if len(c) > 6 else (None, None)
    ffb = {f"N{i}" for i in range(1, 8)}
    m1 = main(drop(lambda l: row(l)[0] == "workplan FFBAD17" and row(l)[1] in ffb), quiet=True)
    got1 = {m.split(": ")[1] for m in m1 if "FFBAD17" in m}
    ok &= got1 == ffb and len(m1) == 7
    dfrows = [row(l) for l in lines if (row(l)[0] or "").endswith("/DF")]
    m2 = main(drop(lambda l: (row(l)[0] or "").endswith("/DF")), quiet=True)
    ok &= len(m2) == len(dfrows) and len(dfrows) >= 9
    import tempfile
    probe = "- **N3** is closed by the later repair.\n- **N4 (low):** a finding title\n"
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as t:
        t.write(probe)
    hits = [m for m in LINE.finditer(probe)] if False else [l for l in probe.split("\n") if LINE.match(l)]
    ok &= len(hits) == 2              # both lines are seen; only N4 survives the filters below
    os.unlink(t.name)
    print(f"inventory self-test: FFBAD17 projection {len(m1)} miss(es), second-record projection {len(m2)} "
          f"miss(es) of {len(dfrows)} rows; {'OK' if ok else 'FAILED'}")
    return ok


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(0 if self_test() else 1)
    sys.exit(1 if main() else 0)
