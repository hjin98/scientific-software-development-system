"""S5 catalogue §6 cases: matching predicates and mechanical staleness (Manual §6.3-§6.6, R1).

Expectations from the Manual: a run that differs from the failing one only in an external pin, a free
execution attribute or an unpinnable input is the same content adversely and a difference
permissively, so a differing outcome there sends the failure to the owner instead of making it stale;
on⁺ ⇒ on⁻ holds under any later context; a run recorded unbounded is still linked through a narrow
record; a genuine fix observed with the failing run's pins and attributes makes the failure stale.
"""

from __future__ import annotations

from cases_s5_1 import S5Case
from matching import Reading, Run, SETTLED, implication_holds, stale

T0 = (("a.py", 1), ("s.sym", 1))
T1 = (("a.py", 2), ("s.sym", 1))
RD = ("a.py", "s.sym")


def _st(runs, real, state, reading):
    return lambda: stale(real, runs, dict(state), reading)


F = Run("F", T0, RD, frozenset({"p1"}))
R = Run("R", T0, RD, frozenset({"p1"}))
H = Run("H", T1, RD, frozenset({"p1"}), outcome="good")
D_pin = Run("D", T0, RD, frozenset({"p2"}), outcome="good")
CB, GB = (("backend", "cpu"),), (("backend", "gpu"),)
Fa, Ra, Ha = (Run(n, t, RD, attrs=CB, outcome=o) for n, t, o in (("F", T0, "bad"), ("R", T0, "bad"), ("H", T1, "good")))
Da = Run("D", T0, RD, attrs=GB, outcome="good")
Fu, Ru, Hu = (Run(n, t, RD, unpinnable=True, outcome=o) for n, t, o in (("F", T0, "bad"), ("R", T0, "bad"), ("H", T1, "good")))
W0 = T0 + (("other", 1),)
W0b = T0 + (("other", 2),)
W1 = T1 + (("other", 1),)
Fw = Run("F", W0, ("a.py", "s.sym", "other"), bounded=False)
Rw = Run("R", W0, RD)
Dw = Run("D", W0b, ("a.py", "s.sym", "other"), bounded=False, outcome="good")
Hw = Run("H", W1, RD, outcome="good")
SYM = Run("S", T0, RD)

CASES = [
    S5Case("differing_pin_goes_to_owner",
           "a run on the failing content with another external pin gave another outcome: nondeterminism "
           "in fact, so the failure is not stale (c6da678 B1, 3540d98 B2)", False,
           {"settled": _st([F, R, D_pin, H], F, T1, SETTLED),
            "adverse_compares_pins": _st([F, R, D_pin, H], F, T1, Reading(adverse_compares_pins=True, use_link=False))},
           {"adverse_compares_pins": "c6da678 B1 (that candidate had no linking predicate)"}),
    S5Case("differing_free_attribute_goes_to_owner",
           "a run differing only in a free attribute (backend) gave another outcome (53669a5 B1, d837363 B1)", False,
           {"settled": _st([Fa, Ra, Da, Ha], Fa, T1, SETTLED),
            "adverse_compares_attrs": _st([Fa, Ra, Da, Ha], Fa, T1, Reading(adverse_compares_attrs=True, use_link=False))},
           {"adverse_compares_attrs": "53669a5 B1 (that candidate had no linking predicate)"}),
    S5Case("unpinnable_supports_no_stop",
           "runs that read an unpinnable input support no mechanical stop (1ffbbf0 B1, SD-18)", False,
           {"settled": _st([Fu, Ru, Hu], Fu, T1, SETTLED),
            "unpinnable_matches": _st([Fu, Ru, Hu], Fu, T1, Reading(unpinnable_matches=True))},
           {"unpinnable_matches": "1ffbbf0 B1"}),
    S5Case("context_change_keeps_implication",
           "after an analyzer or system-version change re-resolves symbol terms differently, on⁺ still "
           "implies on⁻ because both read the record's own context (6ff4ed1 B1, cc005db B2)", True,
           {"settled": lambda: implication_holds([SYM], [dict(T0), dict(T1)], SYM, SETTLED),
            "current_context": lambda: implication_holds([SYM], [dict(T0)], SYM, Reading(current_context="ctx2"))},
           {"current_context": "6ff4ed1 B1"}),
    S5Case("unbounded_run_still_linked",
           "a differing run recorded unbounded on content that differs from the failing run's only outside "
           "a narrow record is linked through that record and keeps the failure counting (0b6c4fa B1, 5c55d4b B1)",
           False,
           {"settled": _st([Fw, Rw, Dw, Hw], Fw, W1, SETTLED),
            "no_link": _st([Fw, Rw, Dw, Hw], Fw, W1, Reading(use_link=False))},
           {"no_link": "0b6c4fa B1"}),
    S5Case("genuine_fix_is_stale",
           "a reproduction on the failing content and a passing run on the fixed content, with the same pins, "
           "and no differing run: the failure is stale (control)", True,
           {"settled": _st([F, R, H], F, T1, SETTLED)}),
    S5Case("revert_yields_again",
           "after a revert to the failing content, the failing run is linked to the state and yields the "
           "failure: not stale (control)", False,
           {"settled": _st([F, R, H], F, T0, SETTLED)}),
]
