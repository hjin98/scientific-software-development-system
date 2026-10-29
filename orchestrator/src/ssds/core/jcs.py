"""RFC 8785 JSON Canonicalization Scheme over the closed record value domain.

The domain is what SSDS records and identity hashes may hold: ``None``,
booleans, integers in the IEEE-754 exact range, strings without lone
surrogates, lists and string-keyed objects. Floating-point numbers are refused
rather than serialized, because no record field is a float (catalogue §3.2).
Object members are ordered by the UTF-16 code units of their keys, and strings
use the ECMAScript ``JSON.stringify`` escapes, as RFC 8785 §3.2 requires.
"""

from __future__ import annotations

import json
import re
from typing import Any

_EXACT = 2**53 - 1
_SURROGATE = re.compile(r"[\ud800-\udfff]")


class CanonicalJSONError(ValueError):
    """A value outside the canonical record domain."""


def canonical_json(value: Any) -> bytes:
    """Return the RFC 8785 canonical UTF-8 bytes of ``value``."""

    parts: list[str] = []
    _emit(value, parts)
    return "".join(parts).encode("utf-8")


def _emit(value: Any, out: list[str]) -> None:
    if value is None:
        out.append("null")
    elif value is True:
        out.append("true")
    elif value is False:
        out.append("false")
    elif isinstance(value, int):
        if not -_EXACT <= value <= _EXACT:
            raise CanonicalJSONError("integer outside the exact IEEE-754 range")
        out.append(str(value))
    elif isinstance(value, float):
        raise CanonicalJSONError("floating-point numbers are outside the record domain")
    elif isinstance(value, str):
        out.append(_string(value))
    elif isinstance(value, (list, tuple)):
        out.append("[")
        for index, item in enumerate(value):
            if index:
                out.append(",")
            _emit(item, out)
        out.append("]")
    elif isinstance(value, dict):
        for key in value:
            if not isinstance(key, str):
                raise CanonicalJSONError("object keys must be strings")
        out.append("{")
        for index, key in enumerate(sorted(value, key=lambda k: k.encode("utf-16-be"))):
            if index:
                out.append(",")
            out.append(_string(key))
            out.append(":")
            _emit(value[key], out)
        out.append("}")
    else:
        raise CanonicalJSONError(f"{type(value).__name__} is outside the record domain")


def _string(text: str) -> str:
    if _SURROGATE.search(text):
        raise CanonicalJSONError("lone surrogates are not representable")
    # With raw Unicode, the standard encoder uses exactly §3.2.2.2's string escapes.
    # Keep the closed value-domain checks in _emit, including refusal of all floats.
    return json.dumps(text, ensure_ascii=False)
