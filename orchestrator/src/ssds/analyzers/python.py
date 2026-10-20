"""The pinned Python analyzer: definition spans, derived ``IMPORTS`` and completeness (catalogue §1.3, §2.6, §14.5).

Every result is a pure function of the file's bytes under this analyzer's
identity; no host input is read. Its derived relations are complete for static
``import`` statements only, and it reports the constructs that make them
incomplete.
"""

from __future__ import annotations

import ast
import warnings
from dataclasses import dataclass

ANALYZER_ID = "ssds.analyzer.python/1"
LANGUAGE = "python"
#: The constructs for which this analyzer's IMPORTS relations are complete.
COMPLETE_CONSTRUCTS = ("import", "from-import")
#: Incompleteness markers it detects (catalogue §2.6).
MARKERS = ("dynamic-import", "dynamic-code", "relative-import-above-package")


@dataclass(frozen=True)
class Definition:
    qualname: str
    start: int  # byte offset of the first line (decorators included)
    end: int  # byte offset just after the last line


@dataclass(frozen=True)
class ImportFacts:
    modules: tuple[str, ...]  # absolute module names imported, sorted
    markers: tuple[str, ...]  # incompleteness markers found, sorted


def _line_offsets(data: bytes) -> list[int]:
    offsets = [0]
    for index, byte in enumerate(data):
        if byte == 0x0A:
            offsets.append(index + 1)
    return offsets


def _parse(data: bytes) -> ast.Module | None:
    """The module's syntax tree; the analyzed source's own compile warnings are its content, not the operator's."""

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return ast.parse(data)
    except (SyntaxError, ValueError):
        return None


def definitions(data: bytes) -> tuple[Definition, ...]:
    """Every function and class definition, by qualified name within the module."""

    tree = _parse(data)
    if tree is None:
        return ()
    offsets = _line_offsets(data)
    out: list[Definition] = []

    def visit(body: list[ast.stmt], prefix: str) -> None:
        for node in body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                name = f"{prefix}{node.name}"
                first = min([node.lineno] + [d.lineno for d in node.decorator_list])
                last = node.end_lineno or node.lineno
                end = offsets[last] if last < len(offsets) else len(data)
                out.append(Definition(name, offsets[first - 1], end))
                visit(node.body, name + ".")

    visit(tree.body, "")
    return tuple(out)


def module_names(path: str) -> tuple[str, ...]:
    """The dotted module names a path may be imported under: every suffix of its package path."""

    parts = path[: -len(".py")].split("/") if path.endswith(".py") else path.split("/")
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return tuple(".".join(parts[i:]) for i in range(len(parts)) if parts[i:])


def resolve_symbol(path: str, data: bytes, symbol: str) -> tuple[int, int] | None:
    """The span of ``symbol`` in the file, or None if it does not occur exactly once.

    ``symbol`` is a definition's qualified name, optionally preceded by one of
    the file's module names.
    """

    matches = []
    names = module_names(path)
    for definition in definitions(data):
        if symbol == definition.qualname or any(symbol == f"{m}.{definition.qualname}" for m in names):
            matches.append(definition)
    if len(matches) != 1:
        return None
    return matches[0].start, matches[0].end


def imports(path: str, data: bytes) -> ImportFacts:
    """Absolute modules imported by the file, and the markers that make the set incomplete."""

    tree = _parse(data)
    if tree is None:
        return ImportFacts((), ("dynamic-code",))
    package = module_names(path)[0].split(".") if module_names(path) else []
    if not path.endswith("__init__.py"):
        package = package[:-1]
    modules: set[str] = set()
    markers: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                if node.level - 1 > len(package):
                    markers.add("relative-import-above-package")
                    continue
                base = package[: len(package) - (node.level - 1)]
                parent = ".".join(base + ([node.module] if node.module else []))
                modules.add(parent)
                modules.update(f"{parent}.{alias.name}" if parent else alias.name for alias in node.names if alias.name != "*")
            elif node.module:
                modules.add(node.module)
                modules.update(f"{node.module}.{alias.name}" for alias in node.names if alias.name != "*")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "__import__":
                markers.add("dynamic-import")
            elif node.func.id in ("exec", "eval", "compile"):
                markers.add("dynamic-code")
        elif isinstance(node, ast.Attribute) and node.attr == "import_module":
            markers.add("dynamic-import")
    return ImportFacts(tuple(sorted(m for m in modules if m)), tuple(sorted(markers)))
