"""Phase F step 8f: the transports (catalogue §16.10; plan §3.5, reading F70).

The Git-envelope transport writes a task's signed envelope and rendered brief on its run ref in a scratch repository
only, refusing the product repository however it is reached, and reads the agent's result back from that one ref.
The MCP server is JSON-RPC 2.0 over stdio on the standard library, pinned to one MCP revision, and exposes the CLI's
operations through the same ``Session``.
"""

from __future__ import annotations

import io
import json
import unittest
from unittest import mock

from ssds.interface import mcp
from ssds.interface.envelope import RUN_REF, TransportRefused, fetch, publish, run_ref

from ._fixtures import commit, git, init_repo
from .test_admission_requests import RequestFixture


class GitEnvelope(RequestFixture):
    def setUp(self) -> None:
        super().setUp()
        self.scratch = init_repo(self.root / "scratch")
        commit(self.scratch, "scratch")

    def product_refs(self) -> tuple[str, str]:
        return git(self.product, "for-each-ref"), git(self.product, "status", "--porcelain", "--ignored")

    def test_a_round_trip_in_a_scratch_repository(self) -> None:
        before = self.product_refs()
        issued = self.issue("GIT_ENVELOPE")
        binding = issued.binding()
        tip = publish(self.scratch, self.product, binding, b"# The brief\n")
        ref = run_ref(issued.envelope["task_id"])
        self.assertEqual(git(self.scratch, "rev-parse", ref), tip)
        task = json.loads(git(self.scratch, "cat-file", "-p", f"{ref}:task.json"))
        self.assertEqual(task, {"envelope": issued.envelope, "signature": binding["signature"]})
        self.assertEqual(git(self.scratch, "cat-file", "-p", f"{ref}:brief.md"), "# The brief")
        self.assertIsNone(fetch(self.scratch, self.product, issued.envelope["task_id"]), "no result yet")
        # the agent writes its result envelope back onto the run ref
        work = init_repo(self.root / "agent")
        git(work, "fetch", str(self.scratch), f"{ref}:{ref}")
        git(work, "checkout", "-q", ref.removeprefix("refs/heads/"))
        (work / "result.json").write_text(json.dumps({"task_id": issued.envelope["task_id"], "outcome": "COMPLETE"}))
        answered = commit(work, "result")
        git(work, "push", "-q", str(self.scratch), f"HEAD:{ref}")
        result = fetch(self.scratch, self.product, issued.envelope["task_id"])
        self.assertEqual((result["commit"], result["result"]["outcome"]), (answered, "COMPLETE"))
        self.assertEqual(self.product_refs(), before, "no ref or file of the product repository is written")

    def test_the_product_repository_is_refused_however_reached(self) -> None:
        before = self.product_refs()
        issued = self.issue("GIT_ENVELOPE")
        with self.assertRaises(TransportRefused):
            publish(self.product, self.product, issued.binding(), b"brief")
        linked = self.root / "linked"
        git(self.product, "worktree", "add", "-q", "--detach", str(linked))
        self.addCleanup(lambda: git(self.product, "worktree", "remove", "--force", str(linked)))
        with self.assertRaises(TransportRefused):
            publish(linked, self.product, issued.binding(), b"brief")
        with self.assertRaises(TransportRefused):
            fetch(linked, self.product, issued.envelope["task_id"])
        self.assertEqual(git(self.product, "for-each-ref"), before[0])

    def test_a_run_ref_is_written_once_and_names_a_task(self) -> None:
        issued = self.issue("GIT_ENVELOPE")
        publish(self.scratch, self.product, issued.binding(), b"brief")
        with self.assertRaisesRegex(TransportRefused, "already exists"):
            publish(self.scratch, self.product, issued.binding(), b"another brief")
        for bad in ("", "../x", "a b", "a:b", "/x"):
            with self.subTest(task=bad), self.assertRaises(TransportRefused):
                run_ref(bad)
        self.assertTrue(run_ref("task-1-x").startswith(RUN_REF))


class Mcp(RequestFixture):
    def connect(self):
        from ssds.cli import connect

        def connected(ledger, repository):
            with mock.patch("ssds.cli.ssds_home", return_value=self.home.root):
                return connect(ledger, repository)
        return connected

    def call(self, name: str, **arguments) -> dict:
        message = {"jsonrpc": "2.0", "id": 7, "method": "tools/call",
                   "params": {"name": name, "arguments": {"ledger": "demo", "repository": str(self.product),
                                                          **arguments}}}
        return mcp.handle(self.connect(), message)

    def test_the_handshake_names_the_pinned_revision(self) -> None:
        response = mcp.handle(self.connect(), {"jsonrpc": "2.0", "id": 1, "method": "initialize",
                                               "params": {"protocolVersion": mcp.PROTOCOL, "capabilities": {}}})
        self.assertEqual(response["result"]["protocolVersion"], "2025-06-18")
        self.assertIn("tools", response["result"]["capabilities"])
        self.assertIsNone(mcp.handle(self.connect(), {"jsonrpc": "2.0", "method": "notifications/initialized"}))
        self.assertEqual(mcp.handle(self.connect(), {"jsonrpc": "2.0", "id": 2, "method": "ping"})["result"], {})

    def test_the_tools_are_the_clis_operations(self) -> None:
        from ssds.cli import SSDS_COMMANDS, command_name

        listed = mcp.handle(self.connect(), {"jsonrpc": "2.0", "id": 3, "method": "tools/list"})["result"]["tools"]
        self.assertEqual({t["name"] for t in listed}, {command_name(c) for c in SSDS_COMMANDS})
        for tool in listed:
            self.assertIn("ledger", tool["inputSchema"]["required"])

    def test_a_call_answers_as_the_session_does(self) -> None:
        response = self.call("status")
        self.assertFalse(response["result"]["isError"])
        answer = json.loads(response["result"]["content"][0]["text"])
        session = self.connect()("demo", self.product)
        self.assertEqual(answer, json.loads(json.dumps(session.status(), sort_keys=True, default=str)))
        read = json.loads(self.call("read", ref="guide.md")["result"]["content"][0]["text"])
        self.assertEqual(read["answer"]["path"], "guide.md")

    def test_errors(self) -> None:
        refused = self.call("read", ref="nowhere")
        self.assertTrue(refused["result"]["isError"])
        self.assertTrue(self.call("unknown-tool")["result"]["isError"])
        self.assertEqual(mcp.handle(self.connect(), {"jsonrpc": "2.0", "id": 4, "method": "resources/list"})
                         ["error"]["code"], -32601)
        self.assertEqual(mcp.handle(self.connect(), {"id": 5})["error"]["code"], -32600)
        bad = mcp.handle(self.connect(), {"jsonrpc": "2.0", "id": 6, "method": "tools/call", "params": {"name": "read"}})
        self.assertEqual(bad["error"]["code"], -32602)

    def test_serve_over_stdio(self) -> None:
        out = io.StringIO()
        lines = [json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}),
                 json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}), "", "not json",
                 json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})]
        mcp.serve(self.connect(), lines, out)
        responses = [json.loads(line) for line in out.getvalue().splitlines()]
        self.assertEqual([r.get("id") for r in responses], [1, None, 2])
        self.assertEqual(responses[1]["error"]["code"], -32700)


if __name__ == "__main__":
    unittest.main()
