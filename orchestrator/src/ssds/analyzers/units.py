"""Unit expressions: the UCUM subset the pinned analyzers resolve to dimensions (catalogue §14.5).

A unit annotation's expression uses UCUM syntax. This analyzer resolves the
subset of SI base units, common derived and accepted units, metric prefixes,
products (``.``), quotients (``/``), integer exponents and parentheses to a
dimension vector over (length, mass, time, current, temperature, amount,
luminous intensity). An expression outside the subset resolves to ``None``:
not analyzable, never assumed consistent. Curly-brace annotations are
dimensionless, as in UCUM.
"""

from __future__ import annotations

import re

Dimension = tuple[int, int, int, int, int, int, int]
ONE: Dimension = (0, 0, 0, 0, 0, 0, 0)


def _d(L: int = 0, M: int = 0, T: int = 0, I: int = 0, K: int = 0, N: int = 0, J: int = 0) -> Dimension:  # noqa: E741
    return (L, M, T, I, K, N, J)


#: Units that take metric prefixes.
METRIC: dict[str, Dimension] = {
    "m": _d(L=1), "g": _d(M=1), "s": _d(T=1), "A": _d(I=1), "K": _d(K=1), "mol": _d(N=1), "cd": _d(J=1),
    "N": _d(L=1, M=1, T=-2), "J": _d(L=2, M=1, T=-2), "W": _d(L=2, M=1, T=-3), "Pa": _d(L=-1, M=1, T=-2),
    "Hz": _d(T=-1), "C": _d(I=1, T=1), "V": _d(L=2, M=1, T=-3, I=-1), "Ohm": _d(L=2, M=1, T=-3, I=-2),
    "F": _d(L=-2, M=-1, T=4, I=2), "T": _d(M=1, T=-2, I=-1), "Wb": _d(L=2, M=1, T=-2, I=-1),
    "L": _d(L=3), "l": _d(L=3), "eV": _d(L=2, M=1, T=-2), "bar": _d(L=-1, M=1, T=-2), "Cel": _d(K=1),
    "rad": ONE, "sr": ONE,
}
#: Units without prefixes.
PLAIN: dict[str, Dimension] = {"min": _d(T=1), "h": _d(T=1), "d": _d(T=1), "a": _d(T=1), "%": ONE, "1": ONE,
                               "deg": ONE, "atm": _d(L=-1, M=1, T=-2)}
PREFIXES = ("Y", "Z", "E", "P", "T", "G", "M", "k", "h", "da", "d", "c", "m", "u", "n", "p", "f", "a", "z", "y")
_TERM = re.compile(r"^([A-Za-z%]+|1|10\*[-+]?\d+)([-+]?\d+)?$")


def _symbol(name: str) -> Dimension | None:
    if name in PLAIN:
        return PLAIN[name]
    if name in METRIC:
        return METRIC[name]
    for prefix in sorted(PREFIXES, key=len, reverse=True):
        if name.startswith(prefix) and name[len(prefix):] in METRIC:
            return METRIC[name[len(prefix):]]
    return None


def _scale(dim: Dimension, power: int) -> Dimension:
    return tuple(x * power for x in dim)  # type: ignore[return-value]


def _combine(a: Dimension, b: Dimension, sign: int) -> Dimension:
    return tuple(x + sign * y for x, y in zip(a, b))  # type: ignore[return-value]


def dimension(expression: str) -> Dimension | None:
    """The dimension of a UCUM expression in the supported subset, else None."""

    text = re.sub(r"\{[^{}]*\}", "1", expression.strip())
    if not text:
        return None
    try:
        dim, rest = _expr(text)
    except ValueError:
        return None
    return dim if not rest else None


def _expr(text: str) -> tuple[Dimension, str]:
    if text.startswith("/"):
        dim, rest = ONE, text
    else:
        dim, rest = _term(text)
    while rest and rest[0] in "./":
        op, rest = rest[0], rest[1:]
        right, rest = _term(rest)
        dim = _combine(dim, right, 1 if op == "." else -1)
    return dim, rest


def _term(text: str) -> tuple[Dimension, str]:
    if text.startswith("("):
        inner, rest = _expr(text[1:])
        if not rest.startswith(")"):
            raise ValueError("unbalanced")
        rest = rest[1:]
        match = re.match(r"^([-+]?\d+)", rest)
        if match:
            return _scale(inner, int(match.group(1))), rest[match.end():]
        return inner, rest
    match = re.match(r"^[^./()]+", text)
    if not match:
        raise ValueError("empty term")
    token, rest = match.group(0), text[match.end():]
    parsed = _TERM.match(token)
    if not parsed:
        raise ValueError(f"unsupported term {token}")
    name, power = parsed.group(1), int(parsed.group(2) or 1)
    if name.startswith("10*") or name == "1":
        return ONE, rest
    unit = _symbol(name)
    if unit is None:
        # a trailing digit run may belong to the symbol's exponent only; anything else is outside the subset
        raise ValueError(f"unknown unit {name}")
    return _scale(unit, power), rest


def show(dim: Dimension) -> str:
    names = ("L", "M", "T", "I", "Θ", "N", "J")
    parts = [f"{n}{'' if p == 1 else p}" for n, p in zip(names, dim) if p]
    return ".".join(parts) or "1"
