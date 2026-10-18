"""Item-level review judged content, derived from integration histories (diagnostic; SD-47 register RR-1).

Governing SSDP version: 7.2.1. This is a bounded diagnostic of written rules, never adequacy or
production evidence (DS-001). It compares candidate rules for whom an item-level review of a
partitioned item must be independent of, on explicit integration histories, against expectations
written per history from the governing invariant (A5: no actor reviews its own work), not computed
by any rule under test.

The rule the Architecture Manual states (§5.10, judged content): the units in the item revision's
write scope that the item's work changed, at their content in the integrated result; the work is
every integrated enactment for an item revision with the same prose and fixed fields (any part,
a part a re-partition replaced, a copy in another plan). The authors are the producers of that
content, whoever they are.

Rules compared:
  latest_delta      the mechanism catalogue body's §4.3/§13.7 (the parts' latest integrated changes)
  required_out      SD-46 as first worded (each required part's out(o))
  work_in_scope     the Manual's rule
  same_key_global   the same-key work in any scope (the catalogue body's U_X, unscoped)

Run: python3 -I qualification/ssds80/item_review_history_probe.py  (exit 0 iff work_in_scope meets
every expectation and each other rule misses at least one).
"""

import sys

# producer of each content value (unit, content)
AUTHOR = {("u", 1): "A", ("u", 2): "B", ("v", 1): "C", ("w", 9): "D",
          ("x", 3): "F", ("u", 3): "G", ("v", 7): "H"}
ITEM_KEY = "k"  # the item revision's prose and fixed fields
ITEM_SCOPE = {"u", "v", "w"}

# A history: the required parts of the item revision, and the integrations in ledger order as
# (enactment owner, key, delta). Owner is a part name of this item, "src" (a same-key item in
# another plan whose content the copy keeps), "tmpl" (a same-key item in another scope), "other"
# (an item with other prose), or "foreign" (an absorbed change). Each history states the producers
# a correct item-level review must exclude, with the reason.
HISTORIES = {
    "first_only": (["a", "b"], [("a", "k", {"u": 1}), ("b", "k", {"w": 9})],
                   {"A", "D"}, "each part's output is in the result"),
    "empty_redispatch": (["a", "b"], [("a", "k", {"u": 1}), ("b", "k", {"w": 9}), ("a", "k", {})],
                         {"A", "D"}, "u1 is kept by an empty re-dispatch (9431629 B1 a)"),
    "partial_redispatch": (["a", "b"], [("a", "k", {"u": 1}), ("b", "k", {"w": 9}), ("a", "k", {"v": 1})],
                           {"A", "C", "D"}, "u1 is kept beside the new v1 (9431629 B1 b)"),
    "all_empty": (["a", "b"], [("a", "k", {"u": 1}), ("b", "k", {"w": 9}), ("a", "k", {}), ("b", "k", {})],
                  {"A", "D"}, "every part re-dispatched empty (9431629 B1 c)"),
    "repaired": (["a", "b"], [("a", "k", {"u": 1}), ("b", "k", {"w": 9}), ("a", "k", {"u": 2})],
                 {"B", "D"}, "u1 was replaced; its producer A judged nothing in the result"),
    "kept_part_repartition": (["a", "b1"], [("a", "k", {"u": 1}), ("b1", "k", {"w": 9}), ("a", "k", {})],
                              {"A", "D"}, "a discharged part kept by a re-partition (9431629 B1 d)"),
    "replaced_part": (["a", "b1"], [("a", "k", {"u": 1}), ("b", "k", {"w": 9}), ("b1", "k", {})],
                      {"A", "D"}, "b integrated, reopened and was replaced by b1, which kept w9"),
    "copy_empty": (["a", "b"], [("src", "k", {"u": 1}), ("a", "k", {}), ("b", "k", {"w": 9})],
                   {"A", "D"}, "a copy under the same prose and fixed fields keeps u1"),
    "same_key_other_scope": (["a", "b"], [("tmpl", "k", {"x": 3}), ("a", "k", {"u": 1}), ("b", "k", {"w": 9})],
                             {"A", "D"}, "x is outside the item's scope; its producer F judged nothing here"),
    "foreign_then_drift": (["a", "b"], [("a", "k", {"u": 1}), ("b", "k", {"w": 9}), ("foreign", None, {"u": 3}),
                                        ("a", "k", {})],
                           {"G", "D"}, "the drift re-dispatch keeps the foreign u3, which the review judges"),
    "other_item_in_scope": (["a", "b"], [("other", "j", {"v": 7}), ("a", "k", {"u": 1}), ("b", "k", {"w": 9})],
                            {"A", "D"}, "v7 is another item's work, not this item's"),
}


def tree(ints):
    t = {}
    for _, _, delta in ints:
        t.update(delta)
    return t


def producers(units, ints):
    t = tree(ints)
    return {AUTHOR[(u, t[u])] for u in units}


def latest_delta(required, ints):
    units = set()
    for p in required:
        mine = [d for owner, _, d in ints if owner == p]
        if mine:
            units |= set(mine[-1])
    return producers(units, ints)


def required_out(required, ints):
    return producers({u for owner, _, d in ints if owner in required for u in d}, ints)


def work_in_scope(required, ints):
    return producers({u for _, key, d in ints if key == ITEM_KEY for u in d if u in ITEM_SCOPE}, ints)


def same_key_global(required, ints):
    return producers({u for _, key, d in ints if key == ITEM_KEY for u in d}, ints)


RULES = {"latest_delta": latest_delta, "required_out": required_out,
         "work_in_scope": work_in_scope, "same_key_global": same_key_global}


def main() -> int:
    misses = {name: [] for name in RULES}
    for h, (required, ints, want, why) in HISTORIES.items():
        for name, rule in RULES.items():
            got = rule(required, ints)
            if got != want:
                misses[name].append(f"{h}: excludes {sorted(got)}, expected {sorted(want)} ({why})")
    for name, m in misses.items():
        print(f"{name}: {'meets every expectation' if not m else f'{len(m)} miss(es)'}")
        for line in m:
            print("   ", line)
    ok = not misses["work_in_scope"] and all(misses[n] for n in RULES if n != "work_in_scope")
    print(f"{len(HISTORIES)} histories; {'OK' if ok else 'UNEXPECTED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
