"""Static sensor of the SSDS dependency rule (Manual §26.2) and the shadow boundary.

The checker reads source trees and ``pyproject.toml`` files only; it never imports
the code it checks. It reports every violation it sees as a :class:`Violation`
with the rule code of the Phase D plan (§4 of
``workplans/active/SSDS-8.0-G2-PHASE-D-PLAN.md``). Fitness checks are sensors of
the dependency rule, not architecture truth: behaviour routed through runtime data
is invisible to them.
"""

from __future__ import annotations

import ast
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

SSDS = "sdp_orchestrator.ssds"
CORE = "sdp_orchestrator.core"
EXTENSION_GROUP = "sdp_orchestrator.extensions.v1"
SSDS_PYPROJECT = "orchestrator/ssds/pyproject.toml"
SSDS_ENTRY = ("sdp.ssds", "sdp_orchestrator.ssds.extension:provider")

COMPONENTS = ("content", "analyzers", "ledger", "derivation", "admission", "dispatcher", "interface")
FACADES = ("api", "spi")

#: Modules of each component that another owner may import; "" is the package itself.
PUBLIC: dict[str, frozenset[str]] = {
    "content": frozenset({""}),
    "analyzers": frozenset({""}),
    "ledger": frozenset({"read", "qualification", "append"}),
    "derivation": frozenset({""}),
    "admission": frozenset({"request"}),
    "dispatcher": frozenset({""}),
    "interface": frozenset({"render"}),
}

#: Manual §26.2, per importing component: the other components it may import and which of their modules.
ALLOWED: dict[str, dict[str, frozenset[str]]] = {
    "content": {"analyzers": frozenset({""})},
    "analyzers": {"content": frozenset({""})},
    "ledger": {},
    "derivation": {
        "content": frozenset({""}),
        "analyzers": frozenset({""}),
        "ledger": frozenset({"read"}),
    },
    "admission": {
        "derivation": frozenset({""}),
        "ledger": frozenset({"read", "qualification", "append"}),
    },
    "dispatcher": {
        "derivation": frozenset({""}),
        "ledger": frozenset({"qualification"}),
        "interface": frozenset({"render"}),
        "admission": frozenset({"request"}),
    },
    "interface": {
        "derivation": frozenset({""}),
        "ledger": frozenset({"qualification"}),
        "admission": frozenset({"request"}),
    },
}

#: The rule code reported when a component imports a component or module its row does not allow.
ROW_CODE = {
    "content": "F1",
    "analyzers": "F1",
    "ledger": "F3",
    "derivation": "F2",
    "admission": "F4",
    "dispatcher": "F5",
    "interface": "F6",
}

CORE_PUBLIC = frozenset({f"{CORE}.api.v1", f"{CORE}.spi.v1"})
#: Derivation's row lists no Core module ("imports content, analyzers, ledger (read API) only").
NO_CORE = frozenset({"derivation"})

#: Pure standard-library modules derivation may import: no clock, network, environment,
#: process, filesystem or Git access is reachable through them.
DERIVATION_STDLIB = frozenset(
    {
        "__future__", "abc", "base64", "bisect", "collections", "dataclasses", "enum",
        "fractions", "functools", "graphlib", "hashlib", "heapq", "itertools", "json",
        "math", "operator", "re", "types", "typing",
    }
)
DERIVATION_IO_BUILTINS = frozenset({"open", "input", "breakpoint", "print"})
DYNAMIC_BUILTINS = frozenset({"__import__", "eval", "exec", "compile"})
DYNAMIC_MODULES = frozenset({"importlib"})

#: Components that may start a process (Git reads for content and the ledger; the append).
PROCESS_OWNERS = frozenset({"content", "ledger"})
PROCESS_MODULES = frozenset({"subprocess", "pty", "multiprocessing"})
PROCESS_OS_CALLS = frozenset(
    {"system", "popen", "fork", "forkpty", "posix_spawn", "posix_spawnp"}
    | {f"exec{s}" for s in ("l", "le", "lp", "lpe", "v", "ve", "vp", "vpe")}
    | {f"spawn{s}" for s in ("l", "le", "lp", "lpe", "v", "ve", "vp", "vpe")}
)
MODELS_MARKER = "ssds80/models"
#: The sensor and its own discriminators name the models directory as data; their imports are still checked.
SENSOR_FILES = frozenset({"orchestrator/ssds/tests/fitness.py", "orchestrator/ssds/tests/test_fitness.py"})
LEDGER_APPEND = f"{SSDS}.ledger.append"
#: Git subcommands that write objects, refs, the index or files.
WRITING_GIT = frozenset(
    {
        "add", "am", "apply", "branch", "checkout", "cherry-pick", "clean", "clone", "commit",
        "commit-tree", "fetch", "gc", "hash-object", "init", "merge", "mktag", "mktree", "mv",
        "notes", "prune", "pull", "push", "read-tree", "rebase", "replace", "reset", "restore",
        "revert", "rm", "stash", "switch", "symbolic-ref", "tag", "update-index", "update-ref",
        "worktree", "write-tree",
    }
)


@dataclass(frozen=True, order=True)
class Violation:
    code: str
    path: str
    detail: str


@dataclass(frozen=True)
class _Import:
    target: str  # absolute module name
    names: tuple[str, ...]  # names imported from it by ``from target import ...`` (empty otherwise)
    line: int


@dataclass(frozen=True)
class _Module:
    name: str
    path: Path
    tree: ast.Module


def _module_name(root: Path, path: Path) -> str:
    parts = list(path.relative_to(root).with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def _load(root: Path) -> list[_Module]:
    modules = []
    for path in sorted(root.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        modules.append(_Module(_module_name(root, path), path, tree))
    return modules


def _imports(module: _Module, known: frozenset[str]) -> list[_Import]:
    """Every import in the module, relative ones resolved, ``from M import m`` resolved to ``M.m``."""

    is_package = module.path.name == "__init__.py"
    package = module.name if is_package else module.name.rpartition(".")[0]
    found: list[_Import] = []
    for node in ast.walk(module.tree):
        if isinstance(node, ast.Import):
            found.extend(_Import(alias.name, (), node.lineno) for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                base = package.split(".")
                if node.level > 1:
                    base = base[: -(node.level - 1)]
                parent = ".".join(base + ([node.module] if node.module else []))
            else:
                parent = node.module or ""
            plain: list[str] = []
            for alias in node.names:
                child = f"{parent}.{alias.name}"
                if child in known:
                    found.append(_Import(child, (), node.lineno))
                else:
                    plain.append(alias.name)
            if plain:
                found.append(_Import(parent, tuple(plain), node.lineno))
    return found


def _docstring_nodes(tree: ast.Module) -> set[int]:
    ids = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            body = node.body
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
                ids.add(id(body[0].value))
    return ids


def _strings(tree: ast.Module) -> list[tuple[str, int]]:
    skip = _docstring_nodes(tree)
    return [
        (node.value, node.lineno)
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in skip
    ]


def _called_builtins(tree: ast.Module) -> list[tuple[str, int]]:
    return [
        (node.func.id, node.lineno)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    ]


def _os_process_calls(tree: ast.Module) -> list[tuple[str, int]]:
    return [
        (node.func.attr, node.lineno)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "os"
        and node.func.attr in PROCESS_OS_CALLS
    ]


def _owner(name: str) -> str | None:
    """The owner of an SSDS module: a component, a facade, ``extension`` or ``top``; None if unowned."""

    if name == SSDS:
        return "top"
    rest = name[len(SSDS) + 1 :]
    head, _, tail = rest.partition(".")
    if head in COMPONENTS or head in FACADES:
        return head
    if head == "extension" and not tail:
        return "extension"
    return None


def _split(target: str) -> tuple[str, str]:
    """``sdp_orchestrator.ssds.ledger.read`` -> ("ledger", "read")."""

    rest = target[len(SSDS) + 1 :]
    head, _, tail = rest.partition(".")
    return head, tail


def _declared_import_roots(pyproject: Path) -> frozenset[str]:
    config = tomllib.loads(pyproject.read_text(encoding="utf-8"))
    roots = set()
    for requirement in config["project"].get("dependencies", []):
        name = requirement
        for stop in "<>=!~;[ ":
            name = name.split(stop)[0]
        name = name.strip().lower()
        roots.add("sdp_orchestrator" if name.startswith("sdp-orchestrator-") else name.replace("-", "_"))
    return frozenset(roots)


def _relative(repo_root: Path, path: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def _check_ssds_import(owner: str, imp: _Import, where: str) -> list[Violation]:
    target = imp.target
    out: list[Violation] = []

    def v(code: str, detail: str) -> None:
        out.append(Violation(code, where, f"line {imp.line}: {detail}"))

    if target == SSDS:
        if owner == "top":
            v("F12", "the top package imports nothing from sdp_orchestrator")
        return out
    head, tail = _split(target)
    if owner == "top":
        v("F12", f"the top package imports nothing from sdp_orchestrator ({target})")
        return out
    if head == owner:
        return out
    if head == "extension":
        v("F12", f"nothing imports the extension module ({target})")
        return out
    if head in FACADES:
        if owner in COMPONENTS:
            v("F12", f"a component never imports the public facades ({target})")
        return out
    if head not in COMPONENTS:
        v("F11", f"{target} is not a public module of any component")
        return out
    private = [part for part in tail.split(".") if part.startswith("_")] if tail else []
    private += [name for name in imp.names if name.startswith("_")]
    if private:
        v("F11", f"private name or module {private} of {head}")
    if head == "ledger" and tail == "append" and owner != "admission":
        v("F3", f"only admission imports the ledger append API ({target})")
        return out
    if tail not in PUBLIC[head]:
        v("F11", f"{target} is internal to {head}")
        return out
    if owner in COMPONENTS:
        allowed = ALLOWED[owner].get(head)
        if allowed is None or tail not in allowed:
            v(ROW_CODE[owner], f"{owner} may not import {target}")
    return out


def check(repo_root: Path, repo_files: list[str], model_stems: frozenset[str]) -> list[Violation]:
    """Return every violation in the repository rooted at ``repo_root``.

    ``repo_files`` are the repository-relative paths to consider (tracked and
    untracked-not-ignored); ``model_stems`` are the Stage S model module names.
    """

    violations: list[Violation] = []
    ssds_src = repo_root / "orchestrator/ssds/src"
    core_src = repo_root / "orchestrator/src"
    ssds_tests = repo_root / "orchestrator/ssds/tests"
    ssds_modules = _load(ssds_src) if ssds_src.is_dir() else []
    core_modules = _load(core_src) if core_src.is_dir() else []
    # Declared public modules resolve as modules even before their files exist.
    declared_public = {f"{SSDS}.{c}.{m}" for c, modules in PUBLIC.items() for m in modules if m}
    known = frozenset(m.name for m in ssds_modules + core_modules) | declared_public
    pyproject = repo_root / SSDS_PYPROJECT
    declared = _declared_import_roots(pyproject) if pyproject.is_file() else frozenset()
    stdlib = frozenset(sys.stdlib_module_names)

    for module in ssds_modules:
        where = _relative(repo_root, module.path)
        if module.name != SSDS and not module.name.startswith(SSDS + "."):
            if module.name != "sdp_orchestrator":
                violations.append(Violation("F0", where, f"{module.name} is outside {SSDS}"))
            else:
                violations.append(Violation("F0", where, "the root namespace has no __init__.py"))
            continue
        owner = _owner(module.name)
        if owner is None:
            violations.append(Violation("F0", where, f"{module.name} belongs to no §26.1 component"))
            continue
        for imp in _imports(module, known):
            root = imp.target.split(".")[0]
            line = f"line {imp.line}"
            if imp.target == SSDS or imp.target.startswith(SSDS + "."):
                violations.extend(_check_ssds_import(owner, imp, where))
            elif imp.target.startswith(CORE + ".") or imp.target == CORE:
                if owner in NO_CORE:
                    violations.append(Violation("F2", where, f"{line}: derivation imports no Core module ({imp.target})"))
                elif owner == "top":
                    violations.append(Violation("F12", where, f"{line}: the top package imports nothing ({imp.target})"))
                elif imp.target not in CORE_PUBLIC:
                    violations.append(Violation("F11", where, f"{line}: {imp.target} is not Core public API/SPI"))
            elif root == "sdp_orchestrator":
                violations.append(Violation("F12", where, f"{line}: {imp.target} is not a known public surface"))
            elif root == "qualification" or root in model_stems:
                violations.append(Violation("F13", where, f"{line}: imports the Stage S models ({imp.target})"))
            elif root in DYNAMIC_MODULES:
                violations.append(Violation("F11", where, f"{line}: dynamic import machinery ({imp.target})"))
            elif root in stdlib:
                if owner == "derivation" and root not in DERIVATION_STDLIB:
                    violations.append(Violation("F8", where, f"{line}: {imp.target} is not on derivation's allowlist"))
                if root in PROCESS_MODULES and owner not in PROCESS_OWNERS:
                    violations.append(Violation("B1", where, f"{line}: only content and ledger start processes ({imp.target})"))
            elif root in declared:
                if owner == "derivation":
                    violations.append(Violation("F8", where, f"{line}: {imp.target} is not on derivation's allowlist"))
            else:
                violations.append(Violation("F12", where, f"{line}: {imp.target} is not a declared dependency"))

        for name, lineno in _called_builtins(module.tree):
            if name in DYNAMIC_BUILTINS:
                violations.append(Violation("F11", where, f"line {lineno}: dynamic code ({name})"))
            elif owner == "derivation" and name in DERIVATION_IO_BUILTINS:
                violations.append(Violation("F8", where, f"line {lineno}: derivation performs no I/O ({name})"))
        if owner not in PROCESS_OWNERS:
            for name, lineno in _os_process_calls(module.tree):
                violations.append(Violation("B1", where, f"line {lineno}: only content and ledger start processes (os.{name})"))
        if module.name == f"{SSDS}.ledger":
            for imp in _imports(module, known):
                if imp.target == LEDGER_APPEND:
                    violations.append(Violation("F3", where, f"line {imp.line}: the ledger package re-exports append"))
        if owner in PROCESS_OWNERS and module.name != LEDGER_APPEND:
            for value, lineno in _strings(module.tree):
                if value in WRITING_GIT:
                    violations.append(Violation("B1", where, f"line {lineno}: writing Git subcommand {value!r}"))
        for value, lineno in _strings(module.tree):
            if MODELS_MARKER in value:
                violations.append(Violation("F13", where, f"line {lineno}: names the Stage S models"))

    for module in _load(ssds_tests) if ssds_tests.is_dir() else []:
        where = _relative(repo_root, module.path)
        for imp in _imports(module, frozenset()):
            root = imp.target.split(".")[0]
            if root == "qualification" or root in model_stems:
                violations.append(Violation("F13", where, f"line {imp.line}: imports the Stage S models ({imp.target})"))
        if where in SENSOR_FILES:
            continue
        for value, lineno in _strings(module.tree):
            if MODELS_MARKER in value:
                violations.append(Violation("F13", where, f"line {lineno}: names the Stage S models"))

    for module in core_modules:
        if not module.name.startswith(CORE):
            continue
        where = _relative(repo_root, module.path)
        for imp in _imports(module, known):
            if imp.target == SSDS or imp.target.startswith(SSDS + "."):
                violations.append(Violation("F7", where, f"line {imp.line}: Core imports {imp.target}"))
        for value, lineno in _strings(module.tree):
            if value.startswith(SSDS) or value == SSDS_ENTRY[0]:
                violations.append(Violation("F7", where, f"line {lineno}: Core names SSDS ({value!r})"))

    for relative in repo_files:
        if "sdp_orchestrator/ssds" in relative and not relative.startswith("orchestrator/ssds/"):
            violations.append(Violation("F9", relative, "SSDS files live under orchestrator/ssds/"))

    violations.extend(_check_registration(repo_root, repo_files))
    return sorted(set(violations))


def _check_registration(repo_root: Path, repo_files: list[str]) -> list[Violation]:
    out: list[Violation] = []
    entries: list[tuple[str, str, str]] = []
    for relative in repo_files:
        if Path(relative).name != "pyproject.toml":
            continue
        config = tomllib.loads((repo_root / relative).read_text(encoding="utf-8"))
        project = config.get("project", {})
        if project.get("name") == "sdp-orchestrator-ssds" and relative != SSDS_PYPROJECT:
            out.append(Violation("F9", relative, "the SSDS distribution is declared outside orchestrator/ssds/"))
        groups = project.get("entry-points", {})
        for name, value in groups.get(EXTENSION_GROUP, {}).items():
            entries.append((relative, name, value))
        if relative == SSDS_PYPROJECT:
            for table in ("scripts", "gui-scripts"):
                if project.get(table):
                    out.append(Violation("F10", relative, f"the SSDS distribution declares [{table}]"))
            others = sorted(set(groups) - {EXTENSION_GROUP})
            if others:
                out.append(Violation("F10", relative, f"entry-point groups other than the extension group: {others}"))
    if [(path, name, value) for path, name, value in entries] != [(SSDS_PYPROJECT, *SSDS_ENTRY)]:
        out.append(
            Violation("F10", SSDS_PYPROJECT, f"expected exactly one extension registration {SSDS_ENTRY}, found {entries}")
        )
    return out
