"""RFC 8785 canonical JSON over the record value domain (``ssds.core.api.v1.canonical_json``)."""

from __future__ import annotations

import unittest

from ssds.core.api.v1 import CanonicalJSONError, canonical_json


class CanonicalJSONTests(unittest.TestCase):
    def test_string_bytes_match_predecessor_for_every_unicode_scalar(self) -> None:
        """Identity-preserving replacement: predecessor eeb870c0's encoder, in bounded chunks."""
        escapes = {'"': '\\"', '\\': '\\\\', '\b': '\\b', '\f': '\\f',
                   '\n': '\\n', '\r': '\\r', '\t': '\\t'}
        for start in range(0, 0x110000, 4096):
            text = ''.join(chr(c) for c in range(start, min(start + 4096, 0x110000))
                           if not 0xD800 <= c <= 0xDFFF)
            expected = '"' + ''.join(escapes.get(c, f'\\u{ord(c):04x}' if ord(c) < 0x20 else c)
                                    for c in text) + '"'
            self.assertEqual(canonical_json(text), expected.encode('utf-8'), hex(start))

    def test_every_surrogate_remains_refused_in_context(self) -> None:
        for code in range(0xD800, 0xE000):
            with self.assertRaises(CanonicalJSONError):
                canonical_json('prefix' + chr(code) + 'suffix')
        # Python strings containing a UTF-16 surrogate pair remain outside the predecessor's domain too.
        with self.assertRaises(CanonicalJSONError):
            canonical_json('\ud834\udd1e')

    def test_rfc8785_key_order_is_by_utf16_code_units(self) -> None:
        """RFC 8785 §3.2.3's example: code-point order would put U+FB33 before U+1F600."""

        value = {"€": "Euro Sign", "\r": "Carriage Return", "דּ": "Hebrew Letter Dalet With Dagesh",
                 "1": "One", "\U0001f600": "Emoji: Grinning Face", "\u0080": "Control", "ö": "Latin Small Letter O With Diaeresis"}
        keys = ["\r", "1", "\u0080", "ö", "€", "\U0001f600", "דּ"]
        expected = "{" + ",".join(f'"{k}":"{value[k]}"'.replace("\r", "\\r") for k in keys) + "}"
        self.assertEqual(canonical_json(value), expected.encode("utf-8"))

    def test_string_escapes_follow_json_stringify(self) -> None:
        self.assertEqual(canonical_json("a\"b\\c\b\f\n\r\t\u000f\u001f /é"),
                         '"a\\"b\\\\c\\b\\f\\n\\r\\t\\u000f\\u001f /é"'.encode("utf-8"))

    def test_no_whitespace_and_nested_values(self) -> None:
        self.assertEqual(canonical_json({"b": [1, True, None, {"a": -5}], "a": False}),
                         b'{"a":false,"b":[1,true,null,{"a":-5}]}')

    def test_values_outside_the_domain_are_refused(self) -> None:
        for value in (1.5, 2**53, -(2**53), "\ud800", {1: "x"}, b"bytes", {"a": {1, 2}}):
            with self.subTest(value=value), self.assertRaises(CanonicalJSONError):
                canonical_json(value)
        self.assertEqual(canonical_json(2**53 - 1), b"9007199254740991")


if __name__ == "__main__":
    unittest.main()
