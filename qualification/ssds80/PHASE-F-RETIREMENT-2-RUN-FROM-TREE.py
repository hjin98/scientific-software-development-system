"""Run a program script as __main__ and assert, in the same process, that every loaded ``ssds`` module came from
that script's own tree (runbook step C: the pre-C7 program, never the runtime's editable install).

    python -I run_from_tree.py <tree>/orchestrator/scripts/<script>.py <args...>
"""

import runpy
import sys
from pathlib import Path

script = Path(sys.argv[1]).resolve()
tree = script.parents[1] / "src"
sys.argv = [str(script), *sys.argv[2:]]
code = 0
try:
    runpy.run_path(str(script), run_name="__main__")
except SystemExit as exited:
    code = exited.code if isinstance(exited.code, int) else (0 if exited.code is None else 1)
    if not isinstance(exited.code, int) and exited.code is not None:
        print(exited.code)
finally:
    loaded = {name: Path(m.__file__).resolve() for name, m in sys.modules.items()
              if (name == "ssds" or name.startswith("ssds.")) and getattr(m, "__file__", None)}
    stray = sorted(name for name, path in loaded.items() if not path.is_relative_to(tree))
    print(f"ssds modules: {len(loaded)} loaded, all from {tree}" if loaded and not stray
          else f"ORIGIN FAILURE: {stray or 'no ssds module loaded'}")
    if stray or not loaded:
        code = 3
sys.exit(code)
