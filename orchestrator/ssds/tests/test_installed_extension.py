"""The installed distribution registers through Core's real composition (Manual §26.3).

Core and SSDS are built as wheels and installed into a throwaway virtual
environment outside the checkout; Core's own ``sdp`` console script and
``create_application`` are the owners exercised, so nothing here passes by
importing the working tree.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CORE_ROOT = REPO_ROOT / "orchestrator"
SSDS_ROOT = REPO_ROOT / "orchestrator/ssds"
TIMEOUT = 900


def _run(args: list[str], **kwargs) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    return subprocess.run(  # noqa: S603
        args, capture_output=True, text=True, check=False, timeout=TIMEOUT, env=env, **kwargs
    )


class InstalledExtensionTests(unittest.TestCase):
    tmp: tempfile.TemporaryDirectory
    python: Path
    sdp: Path

    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        wheels = root / "wheels"
        for package in (CORE_ROOT, SSDS_ROOT):
            built = _run([sys.executable, "-m", "build", "--wheel", "--outdir", str(wheels), str(package)])
            if built.returncode != 0:
                raise AssertionError(f"wheel build failed for {package}: {built.stderr[-2000:]}")
        venv = root / "venv"
        created = _run([sys.executable, "-m", "venv", str(venv)])
        if created.returncode != 0:
            raise AssertionError(f"venv creation failed: {created.stderr[-2000:]}")
        cls.python = venv / "bin" / "python"
        cls.sdp = venv / "bin" / "sdp"
        installed = _run([str(cls.python), "-m", "pip", "install", "--quiet", *map(str, sorted(wheels.glob("*.whl")))])
        if installed.returncode != 0:
            raise AssertionError(f"wheel install failed: {installed.stderr[-2000:]}")
        cls.home = root / "home"
        cls.home.mkdir()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def _sdp(self, *args: str) -> dict:
        env = {"HOME": str(self.home), "PATH": os.environ.get("PATH", ""), "XDG_CONFIG_HOME": str(self.home / ".config")}
        result = subprocess.run(  # noqa: S603
            [str(self.sdp), *args], capture_output=True, text=True, check=False, timeout=TIMEOUT, env=env,
            cwd=str(self.home),
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def _extension(self, report: dict) -> dict:
        matches = [status for status in report["extensions"] if status["extension_id"] == "sdp.ssds"]
        self.assertEqual(len(matches), 1, report["extensions"])
        return matches[0]

    def test_core_activates_the_one_registration(self) -> None:
        status = self._extension(self._sdp("capabilities", "--load-extensions"))
        self.assertEqual(status["state"], "active", status)
        self.assertEqual(status["distribution"], "sdp-orchestrator-ssds")
        self.assertEqual(status["entry_point"], "sdp_orchestrator.ssds.extension:provider")

    def test_discovery_only_reads_metadata_without_importing_ssds(self) -> None:
        status = self._extension(self._sdp("capabilities"))
        self.assertEqual(status["state"], "discovered", status)
        probe = textwrap.dedent(
            """
            import sys
            from sdp_orchestrator.core.api.v1 import ActivationPolicy, ApplicationRequest, create_application
            app = create_application(ApplicationRequest(activation_policy=ActivationPolicy.DISCOVERY_ONLY))
            assert [e.extension_id for e in app.extensions()] == ["sdp.ssds"], app.extensions()
            assert not [m for m in sys.modules if m.startswith("sdp_orchestrator.ssds")], "imported"
            """
        )
        result = _run([str(self.python), "-I", "-c", probe], cwd=str(self.home))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_the_extension_provides_no_capability_yet(self) -> None:
        report = self._sdp("capabilities", "--load-extensions")
        ssds = [c for c in report["capabilities"] if c["key"].startswith("ssds.")]
        self.assertEqual(ssds, [])

    def test_importing_core_loads_nothing_from_ssds(self) -> None:
        probe = (
            "import sys, sdp_orchestrator.core.cli, sdp_orchestrator.core.api.v1\n"
            "assert not [m for m in sys.modules if m.startswith('sdp_orchestrator.ssds')]\n"
        )
        result = _run([str(self.python), "-I", "-c", probe], cwd=str(self.home))
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
