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
import re
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

SSDS = "ssds"
CORE = "ssds.core"
ROOT_MODULE = "ssds.cli"
PROGRAM_PYPROJECT = "orchestrator/pyproject.toml"
PROGRAM_SRC = "orchestrator/src"
CONSOLE_SCRIPTS = {"ssds": "ssds.cli:main"}
EXTENSION_GROUP = "ssds.extensions.v1"

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
    "interface": frozenset({"render", "operations", "commands"}),
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
#: The root module mounts Core's command set, so it alone may also import Core's CLI module.
ROOT_CORE = CORE_PUBLIC | {f"{CORE}.cli"}
#: Derivation's row lists no Core module ("imports content, analyzers, ledger (read API) only").
NO_CORE = frozenset({"derivation"})
#: Import names of distributions whose names differ from them.
IMPORT_NAMES = {"python-frontmatter": "frontmatter"}

#: Pure standard-library modules derivation may import: no clock, network, environment,
#: process, filesystem or Git access is reachable through them.
DERIVATION_STDLIB = frozenset(
    {
        "__future__", "abc", "base64", "bisect", "collections", "dataclasses", "enum",
        "fractions", "functools", "graphlib", "hashlib", "heapq", "itertools", "json",
        "math", "operator", "re", "tomllib", "types", "typing",
    }
)  # tomllib parses bytes the ledger stores (the policy object); it reads no file
DERIVATION_IO_BUILTINS = frozenset({"open", "input", "breakpoint", "print"})
#: Git readers the facades derivation may import also expose (Review 0e49deb N2): derivation takes
#: trees and chains from its caller and may name none of them, by import or by attribute.
DERIVATION_IO_NAMES = frozenset({"read_tree", "GitReadError", "read_chain", "read_raw", "ledger_head"})
#: The facades that expose them (Review 517af45 NF1: only names reached through these count).
DERIVATION_IO_MODULES = frozenset({f"{SSDS}.content", f"{SSDS}.ledger.read"})
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
MODELS_MARKER = "ssds80/models"
#: The sensor and its own discriminators name the models directory as data; their imports are still checked.
SENSOR_FILES = frozenset({"orchestrator/tests/ssds/fitness.py", "orchestrator/tests/ssds/test_fitness.py"})
#: A string naming a component module or the root module (Core may name only itself).
_NAMES_SSDS_MODULE = re.compile(rf"^ssds\.(?:{'|'.join(COMPONENTS + FACADES)}|cli)(?:\.|$)")


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


def _git_readers(module: _Module) -> list[tuple[str, int]]:
    """Git readers a module reaches through the content or ``ledger.read`` facade, by import or attribute.

    Python's binding and evaluation order (Reviews 137b763 NF4, d8bdfd3 NF6, b341109 NF7, df911c0 and
    39fe39b NF8). A name denotes a set of modules, bound by imports and by plain assignment of a bound
    name (``reader = content``); any other assignment unbinds it, and a bare annotation binds nothing.
    Each scope runs in source order, a binding taking effect after the expression it evaluates:

    - a class body runs where the class statement stands, with the bindings in force there;
    - a function may run whenever it is called after its definition, so a free name denotes what it
      denotes at the definition or after any later binding in the enclosing scope (never a class
      body's); a name the function itself binds, or a parameter, is local throughout it;
    - decorators, defaults, annotations and class bases are evaluated in the enclosing scope.

    An attribute is flagged when its base name may denote one of those modules; an unrelated object's
    attribute of the same spelling is not. A sensor, not a proof (Manual §26.2).
    """

    is_package = module.path.name == "__init__.py"
    package = module.name if is_package else module.name.rpartition(".")[0]
    found: list[tuple[str, int]] = []

    def parent_of(node: ast.ImportFrom) -> str:
        if node.level:
            base = package.split(".")
            if node.level > 1:
                base = base[: -(node.level - 1)]
            return ".".join(base + ([node.module] if node.module else []))
        return node.module or ""

    functions = (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)
    scopes = (*functions, ast.ClassDef)

    def definition_time(node: ast.AST) -> list[ast.AST]:
        """What a function, lambda or class statement evaluates in its enclosing scope."""

        if isinstance(node, ast.ClassDef):
            return [*node.decorator_list, *node.bases, *(k.value for k in node.keywords)]
        arguments = node.args
        every = arguments.posonlyargs + arguments.args + arguments.kwonlyargs
        every += [a for a in (arguments.vararg, arguments.kwarg) if a]
        found_here = [*arguments.defaults, *(d for d in arguments.kw_defaults if d is not None)]
        found_here += [a.annotation for a in every if a.annotation is not None]
        if not isinstance(node, ast.Lambda):
            found_here += [*node.decorator_list, *([node.returns] if node.returns else [])]
        return found_here

    def own_nodes(body: list[ast.AST]):
        """The nodes of one scope; a nested scope is yielded with what it evaluates here, not entered."""

        stack = list(body)
        while stack:
            node = stack.pop()
            yield node
            stack.extend(definition_time(node) if isinstance(node, scopes) else ast.iter_child_nodes(node))

    def dotted(node: ast.expr) -> tuple[str, list[str]] | None:
        parts: list[str] = []
        while isinstance(node, ast.Attribute):
            parts.insert(0, node.attr)
            node = node.value
        return (node.id, parts) if isinstance(node, ast.Name) else None

    def end(node: ast.AST) -> tuple[int, int]:
        return (node.end_lineno or node.lineno, node.end_col_offset or 0)

    def locals_of(node: ast.AST, nodes: list[ast.AST]) -> set[str]:
        """The names a function binds itself (imports, assignments, annotations, nested definitions)."""

        arguments = node.args
        names = {a.arg for a in arguments.posonlyargs + arguments.args + arguments.kwonlyargs}
        names |= {a.arg for a in (arguments.vararg, arguments.kwarg) if a}
        declared: set[str] = set()
        for inner in nodes:
            if isinstance(inner, ast.Import):
                names |= {alias.asname or alias.name.split(".")[0] for alias in inner.names}
            elif isinstance(inner, ast.ImportFrom):
                names |= {alias.asname or alias.name for alias in inner.names}
            elif isinstance(inner, ast.Assign):
                names |= {t.id for t in inner.targets if isinstance(t, ast.Name)}
            elif isinstance(inner, ast.AnnAssign) and isinstance(inner.target, ast.Name):
                names.add(inner.target.id)
            elif isinstance(inner, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and inner is not node:
                names.add(inner.name)
            elif isinstance(inner, (ast.Global, ast.Nonlocal)):
                declared |= set(inner.names)
        return names - declared

    Env = dict[str, frozenset[str]]

    def visit(body: list[ast.AST], start: Env, for_functions: Env | None = None) -> None:
        """One scope. ``for_functions`` is given for a class body: what its methods see instead of it."""

        bound: Env = dict(start)
        history: list[tuple[tuple[tuple[int, int], int], str, frozenset[str]]] = []
        nodes = list(own_nodes(body))
        events: list[tuple[tuple[tuple[int, int], int], ast.AST]] = []
        for node in nodes:
            if isinstance(node, (ast.Import, ast.ImportFrom, ast.Assign, ast.AnnAssign)):
                events.append(((end(node), 1), node))
            elif isinstance(node, scopes):
                events.append(((end(node), 0), node))  # its body or definition, then its name is bound
            elif isinstance(node, ast.Attribute) and node.attr in DERIVATION_IO_NAMES:
                events.append((((node.lineno, node.col_offset), 0), node))
        nested: list[tuple[tuple[tuple[int, int], int], ast.AST, Env]] = []

        def bind(at: tuple[tuple[int, int], int], name: str, modules: frozenset[str]) -> None:
            bound[name] = modules
            history.append((at, name, modules))

        for at, node in sorted(events, key=lambda e: e[0]):
            if isinstance(node, ast.Attribute):
                base = dotted(node.value)
                if base and any(".".join([m, *base[1]]) in DERIVATION_IO_MODULES for m in bound.get(base[0], ())):
                    found.append((node.attr, node.lineno))
            elif isinstance(node, scopes):
                nested.append((at, node, dict(bound)))
                if not isinstance(node, ast.Lambda):
                    bind((at[0], 1), node.name, frozenset())
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.asname or alias.name.split(".")[0]
                    bind(at, name, frozenset({alias.name if alias.asname else name}))
            elif isinstance(node, ast.ImportFrom):
                parent = parent_of(node)
                for alias in node.names:
                    if parent in DERIVATION_IO_MODULES and alias.name in DERIVATION_IO_NAMES:
                        found.append((alias.name, node.lineno))
                    bind(at, alias.asname or alias.name, frozenset({f"{parent}.{alias.name}"}))
            elif node.value is not None:  # Assign, valued AnnAssign: what the value denotes, or nothing tracked
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                source = dotted(node.value)
                modules = frozenset(".".join([m, *source[1]]) for m in bound.get(source[0], ())) if source else frozenset()
                for target in targets:
                    if isinstance(target, ast.Name):
                        bind(at, target.id, modules)

        def callable_view(at: tuple[tuple[int, int], int], snapshot: Env) -> Env:
            """What a function defined at ``at`` may see of this scope: then, or after any later binding."""

            if for_functions is not None:
                return for_functions
            view = {name: set(modules) for name, modules in snapshot.items()}
            for when, name, modules in history:
                if when > at:
                    view.setdefault(name, set()).update(modules)
            return {name: frozenset(modules) for name, modules in view.items()}

        for at, node, snapshot in nested:
            seen = callable_view(at, snapshot)
            if isinstance(node, ast.ClassDef):
                visit(node.body, snapshot if for_functions is None else for_functions, seen)
            else:
                inner_body = node.body if isinstance(node.body, list) else [ast.Expr(node.body)]
                own = locals_of(node, list(own_nodes(inner_body)))
                visit(inner_body, {name: m for name, m in seen.items() if name not in own})

    visit(module.tree.body, {})
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


def _git_subcommands(tree: ast.Module) -> list[tuple[str, int]]:
    """Subcommands of argv-shaped literals: ``["git", <options>, sub, ...]`` or a list starting with ``sub``."""

    found = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.List, ast.Tuple)) or not node.elts:
            continue
        values = [e.value if isinstance(e, ast.Constant) and isinstance(e.value, str) else None for e in node.elts]
        if values[0] == "git":
            rest = values[1:]
            while rest and rest[0] is not None and rest[0].startswith("-"):
                rest = rest[2:] if rest[0] in ("-C", "-c") else rest[1:]
            if rest and rest[0] is not None:
                found.append((rest[0], node.lineno))
        elif values[0] is not None:
            found.append((values[0], node.lineno))
    return found


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


def _runs_as_main(tree: ast.Module) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare) and isinstance(node.left, ast.Name) and node.left.id == "__name__":
            if any(isinstance(c, ast.Constant) and c.value == "__main__" for c in node.comparators):
                return True
    return False


def _owner(name: str) -> str | None:
    """The owner of a program module: ``core``, a component, a facade, ``cli`` or ``top``; None if unowned."""

    if name == SSDS:
        return "top"
    head, _, tail = name[len(SSDS) + 1 :].partition(".")
    if head == "core" or head in COMPONENTS or head in FACADES:
        return head
    if head == "cli" and not tail:
        return "cli"
    return None


def _split(target: str) -> tuple[str, str]:
    """``ssds.ledger.read`` -> ("ledger", "read")."""

    head, _, tail = target[len(SSDS) + 1 :].partition(".")
    return head, tail


def _declared_import_roots(pyproject: Path) -> frozenset[str]:
    config = tomllib.loads(pyproject.read_text(encoding="utf-8"))
    roots = set()
    for requirement in config["project"].get("dependencies", []):
        name = requirement
        for stop in "<>=!~;[ ":
            name = name.split(stop)[0]
        name = name.strip().lower()
        roots.add(IMPORT_NAMES.get(name, name.replace("-", "_")))
    return frozenset(roots)


def _relative(repo_root: Path, path: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def _check_program_import(owner: str, imp: _Import, where: str) -> list[Violation]:
    """An import of a program module by a component, facade, the root module or the top package."""

    target = imp.target
    out: list[Violation] = []

    def v(code: str, detail: str) -> None:
        out.append(Violation(code, where, f"line {imp.line}: {detail}"))

    if owner == "top":
        v("F12", f"the top package imports nothing ({target})")
        return out
    if target == SSDS:
        return out
    head, tail = _split(target)
    if head == owner:
        return out
    if head == "cli":
        v("F12", f"nothing imports the root module ({target})")
        return out
    if head == "core":
        if owner in NO_CORE:
            v("F2", f"derivation imports no Core module ({target})")
        elif target not in (ROOT_CORE if owner == "cli" else CORE_PUBLIC):
            v("F11", f"{target} is not Core public API/SPI")
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
    src = repo_root / PROGRAM_SRC
    tests = repo_root / "orchestrator/tests"
    modules = _load(src) if src.is_dir() else []
    # Declared public modules resolve as modules even before their files exist.
    declared_public = {f"{SSDS}.{c}.{m}" for c, names in PUBLIC.items() for m in names if m}
    known = frozenset(m.name for m in modules) | declared_public
    pyproject = repo_root / PROGRAM_PYPROJECT
    declared = _declared_import_roots(pyproject) if pyproject.is_file() else frozenset()
    stdlib = frozenset(sys.stdlib_module_names)

    for module in modules:
        where = _relative(repo_root, module.path)
        if module.name != SSDS and not module.name.startswith(SSDS + "."):
            violations.append(Violation("F0", where, f"{module.name} is outside the {SSDS} package"))
            continue
        owner = _owner(module.name)
        if owner is None:
            violations.append(Violation("F0", where, f"{module.name} belongs to no §26.1 component"))
            continue
        if module.path.name == "__main__.py" or _runs_as_main(module.tree):
            violations.append(Violation("F10", where, "a second runnable entry beside the root module"))
        if owner == "core":
            violations.extend(_check_core(module, known, where))
            continue
        for imp in _imports(module, known):
            root = imp.target.split(".")[0]
            line = f"line {imp.line}"
            if root == SSDS:
                violations.extend(_check_program_import(owner, imp, where))
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

        if owner == "derivation":
            for name, lineno in _git_readers(module):
                violations.append(Violation("F8", where, f"line {lineno}: derivation reads no Git ({name})"))
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
            for value, lineno in _git_subcommands(module.tree):
                if value in WRITING_GIT:
                    violations.append(Violation("B1", where, f"line {lineno}: writing Git subcommand {value!r}"))
        for value, lineno in _strings(module.tree):
            if MODELS_MARKER in value:
                violations.append(Violation("F13", where, f"line {lineno}: names the Stage S models"))

    for module in _load(tests) if tests.is_dir() else []:
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

    for relative in repo_files:
        parents = Path(relative).parts[:-1]
        if SSDS in parents and relative.endswith(".py") and not relative.startswith(f"{PROGRAM_SRC}/ssds/") \
                and not relative.startswith("orchestrator/tests/"):
            violations.append(Violation("F9", relative, "program source lives under orchestrator/src/ssds/"))

    violations.extend(_check_packaging(repo_root, repo_files))
    return sorted(set(violations))


def _check_core(module: _Module, known: frozenset[str], where: str) -> list[Violation]:
    """Manual §26.2: the Level 0 Core imports nothing from the SSDS components or the root module."""

    out: list[Violation] = []
    for imp in _imports(module, known):
        if imp.target.split(".")[0] == SSDS and not (imp.target == CORE or imp.target.startswith(CORE + ".")):
            if imp.target != SSDS:
                out.append(Violation("F7", where, f"line {imp.line}: Core imports {imp.target}"))
    for value, lineno in _strings(module.tree):
        if _NAMES_SSDS_MODULE.match(value):
            out.append(Violation("F7", where, f"line {lineno}: Core names {value!r}"))
    return out


def _check_packaging(repo_root: Path, repo_files: list[str]) -> list[Violation]:
    """One program: one distribution, one console script, the root module as its only entry."""

    out: list[Violation] = []
    programs = []
    for relative in repo_files:
        if Path(relative).name != "pyproject.toml":
            continue
        config = tomllib.loads((repo_root / relative).read_text(encoding="utf-8"))
        project = config.get("project", {})
        groups = project.get("entry-points", {})
        if project.get("name") == "ssds":
            programs.append(relative)
        if relative != PROGRAM_PYPROJECT and "ssds" in project.get("scripts", {}):
            out.append(Violation("F10", relative, "a second distribution declares the ssds command"))
        if relative == PROGRAM_PYPROJECT:
            if project.get("scripts", {}) != CONSOLE_SCRIPTS:
                out.append(Violation("F10", relative, f"console scripts must be exactly {CONSOLE_SCRIPTS}"))
            if project.get("gui-scripts"):
                out.append(Violation("F10", relative, "the program declares [gui-scripts]"))
            if groups.get(EXTENSION_GROUP):
                out.append(Violation("F10", relative, "the program registers itself as an extension of itself"))
    if programs != [PROGRAM_PYPROJECT]:
        out.append(Violation("F9", PROGRAM_PYPROJECT, f"expected one ssds distribution at {PROGRAM_PYPROJECT}, found {programs}"))
    return out
