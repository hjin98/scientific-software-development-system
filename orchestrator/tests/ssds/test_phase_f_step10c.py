"""Phase F step 10c: records-only requests (catalogue §16.1, §25.1; Manual §26.3; plan §3.7, readings F4, F121).

On the real ledger there are no envelopes (F4), so §16.1's ``report``, ``submit`` and ``decide`` take their human
form: ``--prepare RECORDS`` writes an unsigned records-only request at the ledger's expected head, with a readable
summary and the message the human signs, to the request workspace in operator state; ``--admit DIR`` rebuilds the
message from ``request.json``, attaches the human's signature and submits through step 10b's composition. Nothing
here signs.
"""

from __future__ import annotations

import json
import os
import stat
import unittest
from pathlib import Path
from unittest import mock

from ssds.admission.request import request_id, request_message
from ssds.interface.operations import Refused
from ssds.ledger.read import with_id

from . import test_phase_f_step9d_iii as harness
from ._fixtures import commit, record, sshsig


def unsigned(kind: str, **fields) -> dict:
    """A record as a human writes it: no id, actor and binding left for ``--prepare`` to fill."""

    body = {k: v for k, v in record(kind, **fields).items() if k not in ("id", "actor", "actor_class", "binding")}
    return body


def availability() -> dict:
    return unsigned("AVAILABILITY", target={"digest": "sha256:" + "6" * 64}, outcome="AVAILABLE")


class Prepared(harness.AdmittedRuns):
    def setUp(self) -> None:
        super().setUp()
        patch = mock.patch("ssds.cli.ssds_home", return_value=self.home.root)
        patch.start()
        self.addCleanup(patch.stop)

    def composition(self):
        from ssds.cli import Composition

        return Composition("demo", self.product)

    def prepare(self, command: str, *records, adopted=()) -> Path:
        directory, _ = self.composition().prepare(command, list(records), list(adopted), self.human())
        return directory

    def sign(self, directory: Path, message: bytes | None = None) -> None:
        signed = (directory / "request-message.txt").read_bytes() if message is None else message
        (directory / "request-message.txt.sig").write_text(sshsig(self.private, signed))

    def stored(self, directory: Path) -> dict:
        return json.loads((directory / "request.json").read_text())


class Prepare(Prepared):
    def test_each_operation_takes_its_kinds(self) -> None:
        from ssds.cli import command_takes

        for command, kind, takes in (("report", "FINDING", True), ("report", "BLOCKER", True),
                                     ("report", "HUMAN_QUESTION", True), ("report", "AMENDMENT_REQUEST", True),
                                     ("report", "AVAILABILITY", False), ("report", "GATE_DECISION", False),
                                     ("decide", "GATE_DECISION", True), ("decide", "HUMAN_DECISION", True),
                                     ("decide", "FINDING", False), ("decide", "AVAILABILITY", False),
                                     ("submit", "AVAILABILITY", True), ("submit", "INTAKE_DISPOSITION", True),
                                     ("submit", "FINDING", False), ("submit", "HUMAN_DECISION", False),
                                     ("submit", None, False), ("submit", 3, False)):
            with self.subTest(command=command, kind=kind):
                self.assertEqual(command_takes(command, kind), takes)
        with self.assertRaises(Refused):
            self.prepare("report", availability())

    def test_the_workspace(self) -> None:
        directory = self.prepare("submit", availability())
        request = self.stored(directory)
        self.assertEqual(directory, self.home.root / "state" / "demo" / "requests" / request_id(request)[7:])
        self.assertEqual((request["base_position"], request["base_commit"]), (len(self.entries()) - 1, self.head()))
        self.assertEqual((request["binding"], request["candidates"], request["adopted_deltas"]), (None, [], []))
        (rec,) = request["records"]
        self.assertEqual((rec["actor"], rec["actor_class"], rec["binding"]), (self.human(), "HUMAN", None))
        from ssds.ledger.read import with_id

        self.assertEqual(rec["id"], with_id({k: v for k, v in rec.items() if k != "id"})["id"], "identity computed")
        self.assertEqual((directory / "request-message.txt").read_bytes(), request_message(request))
        summary = (directory / "summary.txt").read_text()
        self.assertIn("AVAILABILITY " + rec["id"], summary)
        self.assertIn('outcome "AVAILABLE"', summary)
        for name in ("request.json", "summary.txt", "request-message.txt"):
            self.assertEqual(stat.S_IMODE(os.stat(directory / name).st_mode), 0o600, name)
        self.assertEqual(self.prepare("submit", availability()), directory, "prepared again: the same workspace")

    def test_the_base_after_an_absorption(self) -> None:
        """Review of 2d03161c, N6: the base is the ledger's expected head, not its baseline."""

        self.write({"other.txt": "7\n"})
        moved = commit(self.product, "a later commit")
        self.composition().serve("main")
        request = self.stored(self.prepare("submit", availability()))
        self.assertEqual((request["base_commit"], request["base_position"]), (moved, len(self.entries()) - 1))
        self.assertNotEqual(moved, self.baseline)

    def test_what_prepare_refuses(self) -> None:
        other = {**availability(), "actor": "human:SHA256:someone-else"}
        with_id = {**availability(), "id": "sha256:" + "0" * 64}
        bound = {**availability(), "binding": {"envelope": "sha256:" + "1" * 64}}
        agent = {**availability(), "actor_class": "AGENT"}
        for records in ([], [other], [with_id], [bound], [agent], ["not a record"]):
            with self.subTest(records=records), self.assertRaises(Refused):
                self.prepare("submit", *records)
        with self.assertRaises(Refused):
            self.composition().prepare("submit", availability(), [], self.human())  # not an array
        with self.assertRaises(Refused):
            self.composition().prepare("submit", [availability()], [], "human:SHA256:unregistered")
        with self.assertRaises(Refused):
            self.composition().prepare("submit", [availability()], ["not a delta"], self.human())
        self.assertFalse((self.home.root / "state" / "demo" / "requests").exists(), "nothing written")

    def test_an_adoption_request_carries_its_deltas(self) -> None:
        delta = {"absorption": "sha256:" + "4" * 64, "key": ["ssds.manifest", "kind"], "value": "MANIFEST"}
        disposition = unsigned("INTAKE_DISPOSITION", target={"absorption": delta["absorption"], "key": delta["key"]},
                               outcome="ABSORB")
        directory = self.prepare("submit", disposition, adopted=[delta])
        self.assertEqual(self.stored(directory)["adopted_deltas"], [delta])
        self.assertIn(json.dumps(delta, sort_keys=True), (directory / "summary.txt").read_text())


class Admit(Prepared):
    def test_a_prepared_request_signed_and_admitted(self) -> None:
        directory = self.prepare("submit", availability())
        self.sign(directory)
        before = len(self.entries())
        report = self.composition().admit_prepared(directory, "main")
        self.assertEqual((report["decision"], report["reasons"], report["refused"]), ("ACCEPT", (), ()), report)
        self.assertEqual(report["request_id"], request_id({**self.stored(directory), "binding": {
            "human": {"actor": self.human(), "signature": (directory / "request-message.txt.sig").read_text()}}}))
        self.assertEqual(len(self.entries()), before + 1)
        self.assertEqual(report["admitted"], (self.stored(directory)["records"][0]["id"],))
        again = self.composition().admit_prepared(directory, "main")
        self.assertEqual((again["decision"], again["appended"]), ("ACCEPT", False), "a repeat returns the decision")

    def test_one_signature_one_identity(self) -> None:
        """Review of 2d03161c, N1: a re-wrapped, CRLF or padded armor is the same signature and the same request."""

        from ssds.cli import canonical_signature

        directory = self.prepare("submit", availability())
        self.sign(directory)
        signature = (directory / "request-message.txt.sig").read_text()
        self.assertEqual(canonical_signature(signature), signature, "ssh-keygen's own armor is canonical")
        first = self.composition().admit_prepared(directory, "main")
        lines = signature.splitlines()
        body = "".join(lines[1:-1])
        for variant in (signature + "\n\n", signature.replace("\n", "\r\n"),
                        "\n".join([lines[0], *(body[i:i + 40] for i in range(0, len(body), 40)), lines[-1]]) + "\n",
                        "  " + signature):
            with self.subTest(variant=variant[:40]):
                (directory / "request-message.txt.sig").write_text(variant)
                again = self.composition().admit_prepared(directory, "main")
                self.assertEqual((again["request_id"], again["appended"]), (first["request_id"], False))
        self.assertEqual(canonical_signature("not an armor"), "not an armor")

    def test_admit_checks_the_command_and_reports_what_was_signed(self) -> None:
        """Review of 2d03161c, N3 and N4."""

        directory = self.prepare("submit", availability())
        self.sign(directory)
        with self.assertRaises(Refused):
            self.composition().admit_prepared(directory, "main", command="report")
        report = self.composition().admit_prepared(directory, "main", command="submit")
        self.assertEqual(report["decision"], "ACCEPT")
        self.assertEqual(report["submitted"], (directory / "summary.txt").read_text())

    def test_a_deeply_nested_request_is_refused(self) -> None:
        directory = self.prepare("submit", availability())
        self.sign(directory)
        (directory / "request.json").write_text("[" * 100000 + "]" * 100000)
        with self.assertRaises(Refused):  # N5
            self.composition().admit_prepared(directory, "main")

    def test_a_signature_over_other_bytes_is_refused(self) -> None:
        directory = self.prepare("submit", availability())
        self.sign(directory, b"ssds request sha256:" + b"0" * 64 + b"\n")
        report = self.composition().admit_prepared(directory, "main")
        self.assertEqual(report["decision"], "REJECT")
        self.assertEqual(report["admitted"], ())

    def test_a_tampered_request_is_refused(self) -> None:
        directory = self.prepare("submit", availability())
        self.sign(directory)
        request = self.stored(directory)
        request["records"][0]["outcome"] = "UNAVAILABLE"
        (directory / "request.json").write_text(json.dumps(request))
        before = len(self.entries())
        self.assertEqual(self.composition().admit_prepared(directory, "main")["decision"], "REJECT",
                         "the message is rebuilt from request.json, which the signature does not cover")
        self.assertEqual(self.composition().admit_prepared(directory, "main")["admitted"], ())
        self.assertLessEqual(len(self.entries()), before + 1, "at most the rejection itself")

    def test_a_request_message_file_is_never_trusted(self) -> None:
        directory = self.prepare("submit", availability())
        self.sign(directory)
        (directory / "request-message.txt").write_bytes(b"something else\n")
        self.assertEqual(self.composition().admit_prepared(directory, "main")["decision"], "ACCEPT")

    def test_a_base_the_branch_moved_past(self) -> None:
        """Admission's own currency rules (§8.3 steps 2 and 6): a records-only request prepared before the observed
        branch moved is judged at the absorbed head. A record nothing in the move touched is admitted; the base
        position it names stays consistent, since the ledger only grows."""

        directory = self.prepare("submit", availability())
        self.sign(directory)
        self.write({"other.txt": "2\n"})
        commit(self.product, "a later commit on the observed branch")
        before = len(self.entries())
        report = self.composition().admit_prepared(directory, "main")
        self.assertEqual((report["decision"], report["refused"]), ("ACCEPT", ()), report)
        self.assertEqual(len(self.entries()), before + 2, "the absorption, then the admission")

    def test_the_boundary_holds_for_decide(self) -> None:
        from ssds.admission.request import BoundaryRefused

        decision = unsigned("HUMAN_DECISION", target={"units": ["code"]}, outcome="APPROVE")
        directory = self.prepare("decide", decision)
        self.sign(directory)
        before = len(self.entries())
        with self.assertRaises(BoundaryRefused):
            self.composition().admit_prepared(directory, "main")
        self.assertEqual(len(self.entries()), before, "Phase F accepts no gate or human decision (F1)")
        self.assertFalse((self.home.root / "state" / "demo" / "observed-ref.jsonl").exists(),
                         "a refused pass records no observed ref (review of 6de6cf0d, B1)")

    def test_an_unreadable_workspace_is_refused(self) -> None:
        directory = self.prepare("submit", availability())
        with self.assertRaises(Refused):
            self.composition().admit_prepared(directory, "main")  # not signed
        self.sign(directory)
        request = self.stored(directory)
        (directory / "request.json").write_text("[]")
        with self.assertRaises(Refused):
            self.composition().admit_prepared(directory, "main")
        request["records"].append({**request["records"][0], "actor": "human:SHA256:another"})
        (directory / "request.json").write_text(json.dumps(request))
        with self.assertRaises(Refused):  # a human binding speaks for one human (§25.1)
            self.composition().admit_prepared(directory, "main")


class Stale(Prepared):
    """A request whose basis the move made stale is refused by Admission and is prepared again (F121)."""

    MODES = {"code": {"mode": "NATIVE", "ruleset": "ssds-rules/1"}, "*": {"mode": "UNGOVERNED"}}

    def acceptance(self) -> tuple[dict, dict]:
        triple = self.derive().s.subject_triple("code")
        t = {"subject": triple[0], "scope_id": triple[1], "rev": triple[2]}
        basis = [{"mode": "content", "target": {"unit": "code", "rev": t["rev"]}, "class": "EXACT"}]
        acceptance = unsigned("ACCEPTANCE", target=t, outcome="PASS", basis=basis)
        prepared = with_id({**acceptance, "actor": self.human(), "actor_class": "HUMAN", "binding": None})
        attestation = unsigned("NON_AUTHORSHIP_ATTESTATION", target={"record": prepared["id"]}, outcome="NOT_AUTHOR")
        return acceptance, attestation

    def test_a_current_basis_is_admitted(self) -> None:
        directory = self.prepare("submit", *self.acceptance())
        self.sign(directory)
        report = self.composition().admit_prepared(directory, "main")
        self.assertEqual((report["decision"], report["refused"]), ("ACCEPT", ()), report)

    def test_a_basis_the_move_made_stale_is_refused(self) -> None:
        directory = self.prepare("submit", *self.acceptance())
        self.sign(directory)
        self.write({"a.py": "v = 2\n"})  # code's content moves on the observed branch
        commit(self.product, "code changes")
        report = self.composition().admit_prepared(directory, "main")
        self.assertEqual(report["decision"], "REJECT", report)
        accepted = self.stored(directory)["records"][0]["id"]
        self.assertTrue("STALE_BASIS" in dict(report["refused"]).get(accepted, ()), report)


class Commands(Prepared):
    def test_prepare_then_admit(self) -> None:
        from typer.testing import CliRunner

        from ssds.cli import app

        records = self.product.parent / "records.json"
        records.write_text(json.dumps([availability()]))
        prepared = CliRunner().invoke(app, ["submit", "--ledger", "demo", "--prepare", str(records),
                                            "--actor", self.human()])
        self.assertEqual(prepared.exit_code, 0, prepared.output)
        self.assertIn("ssh-keygen -Y sign -f <your key> -n ssds", prepared.output)
        (directory,) = (self.home.root / "state" / "demo" / "requests").iterdir()
        self.assertIn(str(directory), prepared.output)
        self.sign(directory)
        args = ["--ledger", "demo", "--repository", str(self.product), "--observed-ref", "main", "--admit",
                str(directory)]
        admitted = CliRunner().invoke(app, ["submit", *args])
        self.assertEqual(admitted.exit_code, 0, admitted.output)
        self.assertEqual(json.loads(admitted.output)["decision"], "ACCEPT")
        for wrong in (["submit", "--ledger", "demo"],  # neither form
                      ["submit", "--ledger", "demo", "--prepare", str(records), "--actor", self.human(),
                       "--admit", str(directory)],  # both
                      ["submit", "--ledger", "demo", "--prepare", str(records)],  # no actor
                      ["submit", "--ledger", "demo", "--admit", str(directory)],  # no observed ref
                      ["report", "--ledger", "demo", "--prepare", str(records), "--actor", self.human()]):  # kind
            with self.subTest(args=wrong):
                result = CliRunner().invoke(app, wrong)
                self.assertEqual(result.exit_code, 1, result.output)
                self.assertIn("refused", json.loads(result.output))

    def test_the_names_are_the_manuals(self) -> None:
        from ssds.cli import app, command_name

        names = [command_name(info) for info in app.registered_commands]
        for name in ("report", "submit", "decide"):
            self.assertEqual(names.count(name), 1, name)


if __name__ == "__main__":
    unittest.main()
