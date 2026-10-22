"""One program, one composition root (Manual §26.3, A7).

Each probe runs in a fresh, isolated interpreter against this checkout's
``orchestrator/src``, so the root module and Core are the owners exercised and an
installed copy cannot answer for them. The installed console script itself is
Core's installed-product suite's subject.
"""

from __future__ import annotations

import json
import subprocess
import sys
import textwrap
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SRC = REPO_ROOT / "orchestrator/src"
LAUNCHER = REPO_ROOT / "orchestrator/bin/ssds"
#: Core's version-bound commands (Manual §26.3), besides the profile stage commands.
CORE_COMMANDS = {"prompt", "projects", "capabilities", "doctor"}


def _probe(body: str) -> dict:
    code = f"import sys, json\nsys.path.insert(0, {str(SRC)!r})\n" + textwrap.dedent(body)
    result = subprocess.run(  # noqa: S603
        [sys.executable, "-I", "-c", code], capture_output=True, text=True, check=False, timeout=120
    )
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    return json.loads(result.stdout)


class CompositionRootTests(unittest.TestCase):
    def test_the_root_mounts_cores_command_set_flat_then_the_interfaces(self) -> None:
        report = _probe(
            """
            from ssds import cli
            from ssds.core import cli as core_cli
            print(json.dumps({
                "root": [cli.command_name(i) for i in cli.app.registered_commands],
                "core": [cli.command_name(i) for i in core_cli.app.registered_commands],
                "ssds": len(cli.SSDS_COMMANDS),
            }))
            """
        )
        self.assertEqual(report["root"], report["core"] + ["status", "ask", "read"], "Core's commands, then the Interface's (Phase E)")
        self.assertEqual(len(report["root"]), len(set(report["root"])))
        self.assertLessEqual(CORE_COMMANDS, set(report["root"]))
        self.assertIn("implementation", report["root"], "profile stage commands are mounted")
        self.assertEqual(report["ssds"], 3, "the Interface's status, ask and read (Phase E step 6)")

    def test_a_name_claimed_twice_fails_composition(self) -> None:
        report = _probe(
            """
            from typer.models import CommandInfo
            from ssds import cli
            try:
                cli.compose(("core", [CommandInfo(name="doctor")]), ("ssds", [CommandInfo(name="doctor")]))
            except cli.CommandCollision as exc:
                print(json.dumps({"collision": str(exc)}))
            else:
                print(json.dumps({"collision": None}))
            """
        )
        self.assertEqual(report["collision"], "command 'doctor' is claimed by core and ssds")

    def test_core_loads_no_component_and_not_the_root_module(self) -> None:
        report = _probe(
            """
            import ssds.core.cli, ssds.core.api.v1
            from ssds.core.api.v1 import ActivationPolicy, ApplicationRequest, create_application
            for policy in (ActivationPolicy.DISCOVERY_ONLY, ActivationPolicy.NORMAL):
                create_application(ApplicationRequest(activation_policy=policy))
            loaded = sorted(m for m in sys.modules if m.startswith("ssds.") and not m.startswith("ssds.core"))
            print(json.dumps({"loaded": loaded}))
            """
        )
        self.assertEqual(report["loaded"], [])

    def test_the_checkout_launcher_runs_the_root(self) -> None:
        result = subprocess.run(  # noqa: S603
            [sys.executable, str(LAUNCHER), "--help"], capture_output=True, text=True, check=False, timeout=120
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("SSDS", result.stdout)
        for command in CORE_COMMANDS:
            self.assertIn(command, result.stdout)


if __name__ == "__main__":
    unittest.main()
