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


# -- conformance facts (catalogue §14.3, §14.5) -------------------------------------------------------
#
# The facts the check library's Python templates read, each a pure function of the file's bytes. An
# unparsable file yields no facts and is reported as such by the caller (a missing required execution).


def parses(data: bytes) -> bool:
    return _parse(data) is not None


def _signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    return f"{'async ' if isinstance(node, ast.AsyncFunctionDef) else ''}({ast.unparse(node.args)})" + (
        f" -> {ast.unparse(node.returns)}" if node.returns is not None else "")


def public_interface(data: bytes) -> dict[str, str]:
    """Public names and their signatures: module-level names not prefixed ``_`` (or ``__all__`` where
    declared), and the public methods of public classes (§14.5). A class's signature is its bases."""

    tree = _parse(data)
    if tree is None:
        return {}
    declared: set[str] | None = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "__all__" for t in node.targets):
            if isinstance(node.value, (ast.List, ast.Tuple)):
                declared = {e.value for e in node.value.elts if isinstance(e, ast.Constant) and isinstance(e.value, str)}

    def public(name: str) -> bool:
        return name in declared if declared is not None else not name.startswith("_")

    out: dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and public(node.name):
            out[node.name] = _signature(node)
        elif isinstance(node, ast.ClassDef) and public(node.name):
            out[node.name] = "class(" + ", ".join(ast.unparse(b) for b in node.bases) + ")"
            for member in node.body:
                if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)) and \
                        (not member.name.startswith("_") or member.name == "__init__"):
                    out[f"{node.name}.{member.name}"] = _signature(member)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Name) and public(target.id) and target.id != "__all__":
                    out[target.id] = "value"
    return out


def is_test_file(path: str) -> bool:
    name = path.rsplit("/", 1)[-1]
    return path.endswith(".py") and (name.startswith("test_") or name.endswith("_test.py") or "/tests/" in f"/{path}")


@dataclass(frozen=True)
class TestFacts:
    tests: frozenset[str]  # test qualified names
    skipped: frozenset[str]  # tests marked or calling skip
    xfail: frozenset[str]  # tests marked expected-to-fail
    assertions: tuple[tuple[str, int], ...]  # (test, assertion count)
    tolerances: tuple[tuple[str, float], ...]  # (test, largest tolerance literal it passes)


_SKIP = ("skip", "skipIf", "skipUnless", "skipTest")
_XFAIL = ("xfail", "expectedFailure")
_TOLERANCE_KEYWORDS = ("rtol", "atol", "rel", "abs", "delta", "places", "tol", "tolerance")
_ASSERTING = ("assert", "assertEqual", "assertTrue", "assertFalse", "assertAlmostEqual", "assertIn", "assertRaises",
              "assert_allclose", "assert_array_equal", "approx")


def _names_in(node: ast.AST) -> set[str]:
    out = set()
    for inner in ast.walk(node):
        if isinstance(inner, ast.Name):
            out.add(inner.id)
        elif isinstance(inner, ast.Attribute):
            out.add(inner.attr)
    return out


def test_facts(data: bytes) -> TestFacts | None:
    tree = _parse(data)
    if tree is None:
        return None
    tests: set[str] = set()
    skipped: set[str] = set()
    xfail: set[str] = set()
    assertions: dict[str, int] = {}
    tolerances: dict[str, float] = {}

    def visit_function(node: ast.FunctionDef | ast.AsyncFunctionDef, name: str, inherited: set[str]) -> None:
        tests.add(name)
        markers = inherited | set().union(*(_names_in(d) for d in node.decorator_list)) if node.decorator_list else set(inherited)
        body_calls = set()
        count = 0
        largest = 0.0
        for inner in ast.walk(node):
            if isinstance(inner, ast.Assert):
                count += 1
            elif isinstance(inner, ast.Call):
                called = _names_in(inner.func)
                body_calls |= called
                if called & set(_ASSERTING):
                    count += 1
                for keyword in inner.keywords:
                    if keyword.arg in _TOLERANCE_KEYWORDS and isinstance(keyword.value, ast.Constant) and \
                            isinstance(keyword.value.value, (int, float)) and not isinstance(keyword.value.value, bool):
                        value = float(keyword.value.value)
                        largest = max(largest, 10.0 ** -value if keyword.arg == "places" else value)
        if markers & set(_SKIP) or body_calls & {"skip", "skipTest"}:
            skipped.add(name)
        if markers & set(_XFAIL) or body_calls & {"xfail"}:
            xfail.add(name)
        assertions[name] = count
        if largest:
            tolerances[name] = largest

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test"):
            visit_function(node, node.name, set())
        elif isinstance(node, ast.ClassDef) and node.name.startswith("Test") or (
                isinstance(node, ast.ClassDef) and any("TestCase" in ast.unparse(b) for b in node.bases)):
            class_markers = set().union(*(_names_in(d) for d in node.decorator_list)) if node.decorator_list else set()
            for member in node.body:
                if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)) and member.name.startswith("test"):
                    visit_function(member, f"{node.name}.{member.name}", class_markers)
    return TestFacts(frozenset(tests), frozenset(skipped), frozenset(xfail), tuple(sorted(assertions.items())),
                     tuple(sorted(tolerances.items())))


def _is_stub(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    body = list(node.body)
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
        docstring = body[0].value.value
        body = body[1:]
        if not body:
            return True
        if "TODO" in docstring and all(isinstance(s, ast.Pass) for s in body):
            return True
    if len(body) != 1:
        return False
    only = body[0]
    if isinstance(only, ast.Pass):
        return True
    if isinstance(only, ast.Expr) and isinstance(only.value, ast.Constant) and only.value.value is Ellipsis:
        return True
    if isinstance(only, ast.Raise) and only.exc is not None and "NotImplementedError" in _names_in(only.exc):
        return True
    return False


def stubs(data: bytes) -> frozenset[str]:
    """Functions whose body is a placeholder: ``pass``, ``...``, ``raise NotImplementedError``, a docstring
    alone, or a ``TODO`` docstring with ``pass`` (§14.3 ``no_new_stubs``). Abstract methods are not stubs."""

    tree = _parse(data)
    if tree is None:
        return frozenset()
    out: set[str] = set()

    def visit(body: list[ast.stmt], prefix: str) -> None:
        for node in body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                abstract = any("abstractmethod" in _names_in(d) or "overload" in _names_in(d) for d in node.decorator_list)
                if not abstract and _is_stub(node):
                    out.add(prefix + node.name)
            elif isinstance(node, ast.ClassDef):
                visit(node.body, f"{prefix}{node.name}.")

    visit(tree.body, "")
    return frozenset(out)


def requirement_name(requirement: str) -> str:
    """The PEP 503 normalized project name of a requirement string."""

    head = requirement.strip().split(";")[0]
    for stop in "[<>=!~ @(":
        head = head.split(stop)[0]
    return "-".join(part for part in head.lower().replace("_", "-").replace(".", "-").split("-") if part)


def declared_requirements(path: str, data: bytes) -> frozenset[str] | None:
    """Normalized names a Python dependency manifest declares, or None when ``path`` is not one."""

    name = path.rsplit("/", 1)[-1]
    text = data.decode("utf-8", "replace")
    if name.startswith("requirements") and name.endswith(".txt"):
        return frozenset(requirement_name(line) for line in text.splitlines()
                         if line.strip() and not line.strip().startswith(("#", "-")))
    if name == "pyproject.toml":
        import tomllib

        try:
            raw = tomllib.loads(text)
        except tomllib.TOMLDecodeError:
            return frozenset({"<unparsable>"})
        project = raw.get("project", {})
        found = list(project.get("dependencies", []))
        for extra in project.get("optional-dependencies", {}).values():
            found.extend(extra)
        for group in raw.get("dependency-groups", {}).values():
            found.extend(r for r in group if isinstance(r, str))
        return frozenset(requirement_name(r) for r in found if isinstance(r, str))
    return None
