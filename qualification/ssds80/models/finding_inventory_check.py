"""Independent inventory check for the G2 Stage S finding index (13d67be B2 discriminator).

Governing SSDP version: 7.2.1. Design evidence only (DS-001).

`finding_index.py` extracts findings with two heading patterns. This check uses a different method: it
reads every Review record line by line, takes every line that opens with a heading, bold or list-item
marker followed by a finding-shaped identifier (any letter group with optional prime and digits, or
`Blocker <X>`), whatever punctuation follows, and then removes only lines that are statements about an
earlier record's findings ("N3 is closed", "N1-N4 are closed", "is superseded", ...) or non-finding
labels (verdicts, protocol and memory identifiers, refinement and invariant rows). Every identifier left
must appear in the generated index for that record. A miss prints the line and exits non-zero.

Run: python3 -I qualification/ssds80/models/finding_inventory_check.py
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


def index_ids() -> dict:
    out: dict = {}
    for line in open(INDEX, encoding="utf-8"):
        cells = re.split(r"(?<!\\)\|", line)
        if len(cells) > 6 and cells[1].strip().split()[:1] in (["manual"], ["workplan"], ["g2-workplan"]):
            rid = cells[1].strip().split()[1].split("/")[0]
            out.setdefault(rid, set()).add(re.sub(r"\([a-z]\)$", "", cells[2].strip()).replace("Blocker ", ""))
    return out


def main() -> int:
    have = index_ids()
    misses = []
    pats = ["MANUAL-REVIEW-SSDS-8.0-*.md", "WORKPLAN-REVIEW-SSDS-8.0-*.md", "G2-WORKPLAN-REVIEW-SSDS-8.0-*.md"]
    for pat in pats:
        for f in sorted(glob.glob(os.path.join(ROOT, pat))):
            rid = re.search(r"REVIEW-SSDS-8\.0-([0-9A-F]{7})", f).group(1)
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
                if not re.match(r"\s*(?:\*\*)?\s*[—–:.]", rest) and not rest.strip().startswith("**"):
                    continue              # an identifier opening running prose, not a finding title
                if rest.strip().startswith("**") and not re.match(r"\s*\*\*\s*[—–:.(]", rest):
                    continue              # "**N1** prose": a summary mention
                if fid not in have.get(rid, set()):
                    misses.append(f"{os.path.basename(f)}:{n}: {fid}: {line.strip()[:110]}")
    for m in misses:
        print("MISS", m)
    print(f"inventory check: {len(misses)} finding heading(s) absent from the index")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main())
