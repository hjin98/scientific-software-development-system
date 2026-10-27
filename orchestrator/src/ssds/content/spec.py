"""Evidence specification declarations and canonical outcome values (catalogue §17.1, §17.3, §6.5; Phase F step 9b,
readings F84-F86).

Every ``EVIDENCE_SPEC`` unit carries exactly one specification declaration: a TOML document in a fenced ``ssds-spec``
block of the unit's Markdown, or one ``*.ssds-spec.toml`` file inside its scope. It is parsed by one closed parser:
an unknown key, a missing or second declaration, or a value outside the grammar is a :class:`SpecFailure`, a static
error that makes the specification defective (F84; plan check of db0bf1ce, note 1). Parsing never executes content.

Outputs are §17.3's scalar forms: ``float64`` (canonical ``binary64-hex``, ``decimal-shortest`` or ``rounded:<n>``),
``int``, ``bool``, ``enum`` and ``digest``. An embedded oracle's verdict on an output is itself a declared ``enum``
output with values ``PASS`` and ``FAIL``, named by the verdict entry's ``embedded`` key (F85). A declarative verdict
names one of the seven templates (§6.5, §14.3); its parameters are checked statically (SD-81 item 5). ``EXACT`` is
byte equality (F86); ``ABS_TOL``, ``REL_TOL``, ``ULP_TOL``, ``RANGE`` and ``MONOTONE`` are judged by :func:`judge`
exactly on rationals, their parameters re-read as the decimals written (SD-81; reading F116); ``SET_EQUAL`` is not
evaluated (no collection form).

The canonical text of a ``float64`` value (an implementation reading of §17.3's forms, recorded with step 9b):
``binary64-hex`` is ``0x`` and the 16 lower-case hexadecimal digits of the IEEE-754 bit pattern (exact, NaN payloads
kept); ``decimal-shortest`` is the shortest decimal that round-trips, as Python's ``repr`` writes it (``0.1``,
``1e-08``, ``1e+16``, ``1.0``, ``inf``, ``-inf``, ``nan``; every NaN is ``nan``, its sign and payload not kept);
``rounded:<n>`` is the exact decimal value rounded half-even to ``n`` significant digits, in scientific notation as
``Decimal`` writes it (``6.67e-1``), with zero ``0.00e+0`` (signed) and non-finite values ``Infinity``,
``-Infinity`` and ``NaN``. A text is canonical only if it is exactly the one text its value has, so identity is byte
equality (review of a0f2e31b, B2). The ``ENSEMBLE`` outcome's stored shape (§17.3's statistic and replicate count)
is not built in Phase F. Identity of outcomes is byte equality of these
canonical values (§17.3).
"""

from __future__ import annotations

import math
import re
import struct
import tomllib
from dataclasses import dataclass, field
from collections.abc import Callable, Mapping
from decimal import ROUND_HALF_EVEN, Context, Decimal, localcontext
from fractions import Fraction
from typing import Any

from .plan import fenced_blocks
from .view import TreeView

SPEC_INFO = "ssds-spec"
SPEC_FILE_SUFFIX = ".ssds-spec.toml"
ORACLES = frozenset({"DECLARATIVE", "EMBEDDED", "ASSESSOR_READ"})
TYPES = frozenset({"float64", "int", "bool", "enum", "digest"})
NUMERIC = frozenset({"float64", "int"})
TEMPLATES = frozenset({"EXACT", "ABS_TOL", "REL_TOL", "ULP_TOL", "RANGE", "SET_EQUAL", "MONOTONE"})
ORDERS = frozenset({"INCREASING", "NON_DECREASING", "DECREASING", "NON_INCREASING"})
VERDICT_VALUES = ("FAIL", "PASS")
#: The bound on a Dispatcher-run execution (§6.9, §17.1).
SYSTEM_TIME_CAP_HOURS = 168
_KEYS = frozenset({"oracle", "runner", "time_bound_hours", "outputs", "verdicts", "fixed", "granularity",
                   "output_renames"})
_REQUIRED = frozenset({"oracle", "runner", "time_bound_hours", "outputs"})
_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_.-]{0,127}$")
_ROUNDED = re.compile(r"^rounded:([1-9][0-9]?)$")
_HEX = re.compile(r"^0x[0-9a-f]{16}$")
_DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")


@dataclass(frozen=True)
class Output:
    name: str
    type: str
    canonical: str | None = None  # a float64 output's canonical form
    values: tuple[str, ...] = ()  # an enum's values


@dataclass(frozen=True)
class Verdict:
    output: str
    template: str | None = None  # a declarative verdict's template
    params: dict[str, Any] = field(default_factory=dict)
    embedded: str | None = None  # an embedded verdict's output carrying PASS or FAIL
    exact: dict[str, Any] = field(default_factory=dict)  # numeric parameters as exact rationals (SD-81 item 7)


@dataclass(frozen=True)
class SpecDeclaration:
    oracle: str
    runner: str
    time_bound_hours: float
    outputs: tuple[Output, ...]
    verdicts: tuple[Verdict, ...]
    fixed: dict[str, str]
    granularity: dict[str, Any]
    output_renames: dict[str, str]

    def output(self, name: str) -> Output | None:
        return next((o for o in self.outputs if o.name == name), None)

    def verdict(self, name: str) -> Verdict | None:
        return next((v for v in self.verdicts if v.output == name), None)


@dataclass(frozen=True)
class SpecFailure:
    code: str  # MISSING, BLOCKS, TOML, GRAMMAR
    detail: str


class _Grammar(ValueError):
    pass


# -- canonical values (§17.3) ----------------------------------------------------------------------------------------


def canonical_float(form: str, value: float) -> str:
    """The one canonical text of a binary64 value in ``form`` (review of a0f2e31b, B2): every NaN is ``nan`` or
    ``NaN``, zero under ``rounded:<n>`` is ``0.0…e+0`` with its sign, and rounding is half-even whatever the thread's
    decimal context."""

    if form == "binary64-hex":
        return "0x" + struct.pack(">d", value).hex()
    if form == "decimal-shortest":
        return repr(float(value))
    rounded = _ROUNDED.fullmatch(form)
    if rounded is None:
        raise ValueError(f"{form!r} is no canonical float64 form")
    digits = int(rounded.group(1))
    if math.isnan(value):
        return "NaN"
    if value == 0:
        return ("-" if math.copysign(1.0, value) < 0 else "") + ("0." + "0" * (digits - 1) if digits > 1 else "0") \
            + "e+0"
    with localcontext(Context(rounding=ROUND_HALF_EVEN)):
        return f"{Decimal(value):.{digits - 1}e}"


def float_of(form: str, text: Any) -> float | None:
    """The binary64 value a canonical text in ``form`` denotes, or None unless ``text`` is exactly the one text
    :func:`canonical_float` gives for that value (§17.3: identity is byte equality of canonical values)."""

    if not isinstance(text, str):
        return None
    if form == "binary64-hex":
        return struct.unpack(">d", bytes.fromhex(text[2:]))[0] if _HEX.fullmatch(text) else None
    if form != "decimal-shortest" and _ROUNDED.fullmatch(form) is None:
        return None
    try:
        value = float(text)
    except ValueError:  # sNaN and every other text float() refuses
        return None
    return value if canonical_float(form, value) == text else None


def is_canonical(output: Output, value: Any) -> bool:
    """``value`` is a canonical value of ``output`` (§17.3)."""

    if output.type == "float64":
        return float_of(output.canonical, value) is not None
    if output.type == "int":
        return isinstance(value, int) and not isinstance(value, bool)
    if output.type == "bool":
        return isinstance(value, bool)
    if output.type == "enum":
        return isinstance(value, str) and value in output.values
    return isinstance(value, str) and bool(_DIGEST.fullmatch(value))  # digest


def canonical_reference(output: Output, reference: Any) -> Any:
    """The canonical value of a declared reference for ``output``, or raise ``ValueError``: a float64 reference is
    canonicalized by the output's own canonicalizer, except under ``rounded:<n>``, where it must already be canonical
    text (plan check of db0bf1ce, answer 3)."""

    if output.type == "float64":
        if _ROUNDED.fullmatch(output.canonical):
            if float_of(output.canonical, reference) is None:
                raise ValueError(f"a reference for {output.name} is canonical {output.canonical} text")
            return reference
        if isinstance(reference, (int, float)) and not isinstance(reference, bool):
            try:
                exact = float(reference)
            except OverflowError:
                raise ValueError(f"a reference for {output.name} is beyond binary64") from None
            if isinstance(reference, int) and exact != reference:
                raise ValueError(f"a reference for {output.name} is not exactly a binary64 value")
            return canonical_float(output.canonical, exact)
        if float_of(output.canonical, reference) is not None:
            return reference
        raise ValueError(f"a reference for {output.name} is a number or canonical {output.canonical} text")
    if not is_canonical(output, reference):
        raise ValueError(f"a reference for {output.name} is a canonical {output.type} value")
    return reference


# -- the declaration (§17.1) -----------------------------------------------------------------------------------------


def spec_declaration(view: TreeView, uid: str) -> SpecDeclaration | SpecFailure:
    """The specification declaration of ``EVIDENCE_SPEC`` unit ``uid`` in ``view``: exactly one, or a failure."""

    region = view.regions.get(uid)
    found: list[bytes] = []
    for span in region or ():
        data = view.tree[span.path].data
        if span.path.endswith(SPEC_FILE_SUFFIX):
            if span.start != 0 or span.end != len(data):
                return SpecFailure("BLOCKS", f"{span.path} is a declaration file only part of which the unit holds")
            found.append(data)
            continue
        found.extend(data[body.start: body.end] for _, body in fenced_blocks(data, span, SPEC_INFO))
    if not found:
        return SpecFailure("MISSING", f"{uid} carries no specification declaration")
    if len(found) > 1:
        return SpecFailure("BLOCKS", f"{uid} carries {len(found)} specification declarations")
    return parse_spec(found[0])


def parse_spec(data: bytes) -> SpecDeclaration | SpecFailure:
    try:
        raw = tomllib.loads(data.decode("utf-8"))
        # the declared numbers as the exact decimals written, for the oracles' parameters (SD-81 item 7)
        exact = tomllib.loads(data.decode("utf-8"), parse_float=Decimal)
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        return SpecFailure("TOML", str(error))
    try:
        return _declaration(raw, exact)
    except _Grammar as error:
        return SpecFailure("GRAMMAR", str(error))
    except (ArithmeticError, ValueError, TypeError) as error:  # total over untrusted content (§25.4; review B3)
        return SpecFailure("GRAMMAR", f"a value outside the grammar: {error}")


def _declaration(raw: dict[str, Any], exact: dict[str, Any] | None = None) -> SpecDeclaration:
    if not set(raw) <= _KEYS:
        raise _Grammar(f"unknown keys {sorted(set(raw) - _KEYS)}")
    if not _REQUIRED <= set(raw):
        raise _Grammar(f"missing keys {sorted(_REQUIRED - set(raw))}")
    oracle, runner, bound = raw["oracle"], raw["runner"], raw["time_bound_hours"]
    if oracle not in ORACLES:
        raise _Grammar(f"oracle is one of {sorted(ORACLES)}")
    if not isinstance(runner, str) or not runner:
        raise _Grammar("runner names a runner class")
    if not _number(bound) or not math.isfinite(bound) or bound <= 0:
        raise _Grammar("time_bound_hours is a positive number")
    outputs = _outputs(raw["outputs"])
    by_name = {o.name: o for o in outputs}
    verdicts = _verdicts(raw.get("verdicts", []), oracle, by_name, (exact or {}).get("verdicts", []))
    fixed = raw.get("fixed", {})
    if not isinstance(fixed, dict) or not all(isinstance(k, str) and isinstance(v, str) and v for k, v in fixed.items()):
        raise _Grammar("fixed maps attribute names to values")
    renames = raw.get("output_renames", {})
    if not isinstance(renames, dict) or len(set(renames.values())) != len(renames) \
            or not all(isinstance(old, str) and old not in by_name and new in by_name for old, new in renames.items()):
        raise _Grammar("output_renames maps an old name to a declared output")
    return SpecDeclaration(oracle, runner, float(bound), outputs, verdicts, dict(fixed),
                           _granularity(raw.get("granularity", {"mode": "SINGLE"})), dict(renames))


def _number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _outputs(raw: Any) -> tuple[Output, ...]:
    if not isinstance(raw, list) or not raw:
        raise _Grammar("outputs is a non-empty list")
    out: list[Output] = []
    for entry in raw:
        if not isinstance(entry, dict) or not {"name", "type"} <= set(entry):
            raise _Grammar("an output has a name and a type")
        name, kind = entry["name"], entry["type"]
        if not isinstance(name, str) or not _NAME.fullmatch(name) or any(o.name == name for o in out):
            raise _Grammar(f"output names are distinct names: {name!r}")
        if kind not in TYPES:
            raise _Grammar(f"output {name}'s type is one of {sorted(TYPES)}")
        allowed = {"name", "type"} | ({"canonical"} if kind == "float64" else set()) \
            | ({"values"} if kind == "enum" else set())
        if set(entry) != allowed:
            raise _Grammar(f"output {name} has exactly {sorted(allowed)}")
        canonical, values = entry.get("canonical"), entry.get("values", [])
        if kind == "float64" and canonical not in ("binary64-hex", "decimal-shortest") \
                and not _ROUNDED.fullmatch(str(canonical)):
            raise _Grammar(f"output {name}'s canonical form is binary64-hex, decimal-shortest or rounded:<n>")
        if kind == "enum" and (not isinstance(values, list) or not values or len(set(values)) != len(values)
                               or not all(isinstance(v, str) and v for v in values)):
            raise _Grammar(f"enum output {name} lists distinct values")
        out.append(Output(name, kind, canonical, tuple(values)))
    return tuple(out)


def _verdicts(raw: Any, oracle: str, outputs: dict[str, Output], exact: Any = ()) -> tuple[Verdict, ...]:
    if not isinstance(raw, list):
        raise _Grammar("verdicts is a list")
    if oracle == "ASSESSOR_READ":
        if raw:
            raise _Grammar("an assessor-read specification declares no verdicts")
        return ()
    if not raw:
        raise _Grammar(f"a {oracle.lower()} specification declares its verdicts")
    out: list[Verdict] = []
    for entry in raw:
        if not isinstance(entry, dict) or entry.get("output") not in outputs:
            raise _Grammar("a verdict names a declared output")
        name = entry["output"]
        if any(v.output == name for v in out):
            raise _Grammar(f"output {name} has one verdict")
        if oracle == "EMBEDDED":
            carrier = outputs.get(entry.get("embedded"))
            if set(entry) != {"output", "embedded"} or carrier is None or carrier.name == name \
                    or carrier.type != "enum" or sorted(carrier.values) != list(VERDICT_VALUES):
                raise _Grammar(f"an embedded verdict on {name} names the enum output (PASS, FAIL) carrying it")
            out.append(Verdict(name, embedded=carrier.name))
            continue
        if set(entry) - {"output", "template", "params"} or entry.get("template") not in TEMPLATES:
            raise _Grammar(f"a declarative verdict on {name} names one of {sorted(TEMPLATES)}")
        params = entry.get("params", {})
        if not isinstance(params, dict):
            raise _Grammar(f"verdict on {name}: params is a table")
        _check_params(entry["template"], params, outputs[name], outputs)
        exact_entry = exact[len(out)] if isinstance(exact, list) and len(exact) > len(out) else {}
        exact_params = _exact_params(entry["template"],
                                     (exact_entry.get("params") or {}) if isinstance(exact_entry, dict) else {})
        out.append(Verdict(name, entry["template"], dict(params), exact=exact_params))
    return tuple(out)


def _exact_params(template: str, params: dict[str, Any]) -> dict[str, Any]:
    """A numeric template's parameters as exact rationals of the decimals written (SD-81 item 7): a ``Fraction``, or
    an infinity, which only a ``RANGE`` bound may be (item 8); a NaN anywhere is a static error (item 5; plan check of
    6f512acd, note 1)."""

    out: dict[str, Any] = {}
    for key in ("reference", "tol", "lo", "hi"):
        if key not in params or template not in ("ABS_TOL", "REL_TOL", "ULP_TOL", "RANGE"):
            continue
        value = params[key]
        if isinstance(value, Decimal):
            if value.is_nan():
                raise _Grammar(f"{template}'s {key} is a number, not NaN")
            if value.is_infinite():
                if template != "RANGE":
                    raise _Grammar(f"{template}'s {key} is finite")
                out[key] = math.inf if value > 0 else -math.inf
                continue
            out[key] = Fraction(value)
        elif isinstance(value, int) and not isinstance(value, bool):
            out[key] = Fraction(value)
    if template == "ULP_TOL" and isinstance(out.get("reference"), Fraction) \
            and Fraction(float(out["reference"])) != out["reference"]:
        # item 7 forbids reading it as its nearest binary64 and item 2 has no distance to it: fail closed until
        # Q-F28 (re-check of 1e0d5c8a, B1)
        raise _Grammar("ULP_TOL's reference is exactly a binary64 value, written as its exact decimal (Q-F28)")
    if template == "RANGE" and all(isinstance(out.get(k), (Fraction, float)) for k in ("lo", "hi")) \
            and out["lo"] > out["hi"]:
        raise _Grammar("RANGE's lo is at most its hi")  # decided on the decimals written (item 7)
    return out


def _check_params(template: str, params: dict[str, Any], output: Output, outputs: dict[str, Output]) -> None:
    """The constraints of a template's parameters (plan check of db0bf1ce, note 3; SD-81 item 5)."""

    if any(isinstance(v, float) and math.isnan(v) for v in params.values()):
        raise _Grammar(f"{template} on {output.name}: a parameter is a number, not NaN")

    def finite_number(key: str) -> bool:
        return _number(params.get(key)) and math.isfinite(params[key])

    expected = {"EXACT": {"reference"}, "ABS_TOL": {"reference", "tol"}, "REL_TOL": {"reference", "tol"},
                "ULP_TOL": {"reference", "n"}, "RANGE": {"lo", "hi"}, "SET_EQUAL": {"reference"},
                "MONOTONE": {"outputs", "order"}}[template]
    if template == "RANGE":
        if not set(params) or not set(params) <= expected:
            raise _Grammar(f"RANGE on {output.name} declares lo, hi or both")
    elif set(params) != expected:
        raise _Grammar(f"{template} on {output.name} has exactly {sorted(expected)}")
    if template == "EXACT":
        try:
            canonical_reference(output, params["reference"])
        except ValueError as error:
            raise _Grammar(str(error)) from None
    elif template in ("ABS_TOL", "REL_TOL", "ULP_TOL"):
        if output.type not in NUMERIC or not _number(params["reference"]):
            raise _Grammar(f"{template} compares a numeric output with a numeric reference")
        if template == "ULP_TOL":
            n = params["n"]
            if output.type != "float64" or _ROUNDED.fullmatch(output.canonical or "") \
                    or not isinstance(n, int) or isinstance(n, bool) or n < 0:
                raise _Grammar("ULP_TOL takes a non-negative integer n on a binary64 output")
        elif not finite_number("tol") or params["tol"] < 0:
            raise _Grammar(f"{template}'s tol is finite and non-negative")
    elif template == "RANGE":
        if output.type not in NUMERIC or not all(_number(params[k]) for k in params):
            raise _Grammar("RANGE bounds a numeric output with numbers")
        if {"lo", "hi"} <= set(params) and params["lo"] > params["hi"]:
            raise _Grammar("RANGE's lo is at most its hi")
    elif template == "MONOTONE":
        names, order = params["outputs"], params["order"]
        if order not in ORDERS or not isinstance(names, list) or len(names) < 2 or output.name not in names \
                or len(set(names)) != len(names) \
                or not all(n in outputs and outputs[n].type in NUMERIC for n in names):
            raise _Grammar("MONOTONE orders at least two declared numeric outputs, its own among them")


# -- the numeric oracles (SD-81; Phase F reading F116) -----------------------------------------------------------------

NUMERIC_TEMPLATES = frozenset({"ABS_TOL", "REL_TOL", "ULP_TOL", "RANGE", "MONOTONE"})


def exact_of(output: Output, value: Any) -> Fraction | float | None:
    """A canonical numeric value exactly (SD-81 items 4 and 6): a ``Fraction``, or ``±inf`` or ``nan`` as floats;
    ``None`` when the value is not canonical. A ``rounded:<n>`` or ``decimal-shortest`` value is its decimal, a
    ``binary64-hex`` one its binary64."""

    if output.type == "int":
        return Fraction(value) if is_canonical(output, value) else None
    if output.type != "float64":
        return None
    binary = float_of(output.canonical, value)
    if binary is None:
        return None
    if math.isnan(binary) or math.isinf(binary):
        return binary
    if output.canonical == "binary64-hex":
        return Fraction(binary)
    return Fraction(Decimal(value))


def _ulp_index(value: float) -> int:
    """The binary64 value's place on the integer line in sign-magnitude order, ``+0`` and ``−0`` one point (item 2)."""

    bits = struct.unpack(">q", struct.pack(">d", value))[0]
    return bits if bits >= 0 else -(bits & 0x7FFFFFFFFFFFFFFF)


def judge(verdict: Verdict, outputs: Mapping[str, Output], value_of: Callable[[str], Any]) -> bool | None:
    """A numeric verdict's ``PASS`` (True) or ``FAIL`` (False) over an outcome, read exactly (SD-81 items 1-8);
    ``value_of(name)`` gives a declared output's canonical value, or ``None`` when the outcome lacks it. ``None``
    for a template this does not judge."""

    template, exact = verdict.template, verdict.exact
    output = outputs[verdict.output]
    if template == "MONOTONE":
        names = verdict.params["outputs"]
        values = [exact_of(outputs[n], value_of(n)) if n in outputs else None for n in names]
        if any(v is None or (isinstance(v, float) and math.isnan(v)) for v in values):
            return False
        order = verdict.params["order"]
        strict, rising = order in ("INCREASING", "DECREASING"), order in ("INCREASING", "NON_DECREASING")
        for a, b in zip(values, values[1:]):
            if a == b and strict:
                return False
            if a != b and (a > b if rising else a < b):
                return False
        return True
    if template not in ("ABS_TOL", "REL_TOL", "ULP_TOL", "RANGE"):
        return None
    x = exact_of(output, value_of(verdict.output))
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return False  # a NaN either side fails (item 3)
    if template == "RANGE":
        lo, hi = exact.get("lo"), exact.get("hi")
        if isinstance(x, float):  # an infinity passes only the same declared infinity on its side (item 8)
            return (hi == x) if x > 0 else (lo == x)
        return (lo is None or lo <= x) and (hi is None or x <= hi)
    r = exact["reference"]
    if isinstance(x, float):  # two equal infinities pass; any other infinity fails (item 3)
        return isinstance(r, float) and r == x
    if template == "ABS_TOL":
        return abs(x - r) <= exact["tol"]
    if template == "REL_TOL":
        return abs(x - r) <= exact["tol"] * abs(r)  # with r = 0: exact equality (item 1)
    if output.type != "float64" or _ROUNDED.fullmatch(output.canonical or ""):
        return False  # ULP_TOL is a binary64 distance; the parser refuses it elsewhere (item 5)
    # the binary64 the output denotes (item 6), and the reference, exactly a binary64 (F116; Q-F28)
    distance = abs(_ulp_index(float_of(output.canonical, value_of(verdict.output))) - _ulp_index(float(r)))
    return distance <= verdict.params["n"]


def _granularity(raw: Any) -> dict[str, Any]:
    if raw == {"mode": "SINGLE"}:
        return dict(raw)
    if isinstance(raw, dict) and set(raw) == {"mode", "replicates", "statistic", "seed_policy"} \
            and raw["mode"] == "ENSEMBLE" and isinstance(raw["replicates"], int) \
            and not isinstance(raw["replicates"], bool) and raw["replicates"] >= 2 \
            and all(isinstance(raw[k], str) and raw[k] for k in ("statistic", "seed_policy")):
        return dict(raw)
    raise _Grammar("granularity is {mode = SINGLE} or {mode = ENSEMBLE, replicates, statistic, seed_policy}")


__all__ = ["NUMERIC", "ORACLES", "SPEC_FILE_SUFFIX", "SPEC_INFO", "SYSTEM_TIME_CAP_HOURS", "TEMPLATES", "TYPES",
           "Output", "SpecDeclaration", "SpecFailure", "Verdict", "canonical_float", "canonical_reference",
           "exact_of", "float_of", "is_canonical", "judge", "parse_spec", "spec_declaration"]
