"""The MCP transport (Manual §16.10; catalogue §16.10; Phase F step 8f, reading F70).

JSON-RPC 2.0 over stdio, one message per line, built on the standard library: no runtime dependency is added (plan
line 739). It implements the Model Context Protocol revision ``PROTOCOL`` for the tools capability only, and exposes
the same logical operations as the CLI (``status``, ``ask``, ``read``, ``open``, ``inspect``) through the same
``Session``, so a transport never answers differently from another. The session factory is the composition root's.
"""

from __future__ import annotations

import json
from collections.abc import Callable, Iterable
from pathlib import Path
from typing import Any, TextIO

from .operations import Refused

#: The MCP revision this server implements, pinned: no SDK checks conformance for it (plan check of 5d4a0e2, note 6).
PROTOCOL = "2025-06-18"
SERVER = {"name": "ssds", "version": "8.0.0.dev0"}

_LEDGER = {"ledger": {"type": "string", "description": "the ledger id in the SSDS home"},
           "repository": {"type": "string", "description": "the repository whose history the ledger names"}}
#: The CLI's operations, each with its arguments (interface.commands).
TOOLS: dict[str, dict[str, Any]] = {
    "status": {"description": "The ledger's qualification, current assertion, subjects and derived obligations.",
               "properties": {}, "required": []},
    "ask": {"description": "A typed query of Manual §16.2, at the qualified head (or labeled UNQUALIFIED).",
            "properties": {"query": {"type": "string"}, "args": {"type": "array", "items": {"type": "string"}}},
            "required": ["query"]},
    "read": {"description": "Content by unit identity or path at the presented head.",
             "properties": {"ref": {"type": "string"}}, "required": ["ref"]},
    "open": {"description": "A derived obligation's brief at the presented head, labeled NOT ISSUED.",
             "properties": {"obligation": {"type": "string"}}, "required": ["obligation"]},
    "inspect": {"description": "The inspector view and digest.", "properties": {}, "required": []},
}


def tool_list() -> list[dict[str, Any]]:
    return [{"name": name, "description": spec["description"],
             "inputSchema": {"type": "object", "properties": {**_LEDGER, **spec["properties"]},
                             "required": ["ledger", *spec["required"]]}}
            for name, spec in TOOLS.items()]


def call(connect: Callable[[str, Path], Any], name: str, arguments: dict[str, Any]) -> Any:
    """One tool call, through the same ``Session`` the CLI uses."""

    if name not in TOOLS:
        raise Refused(f"unknown tool {name!r}")
    session = connect(arguments["ledger"], Path(arguments.get("repository", ".")).resolve())
    if name == "status":
        return session.status()
    if name == "ask":
        return session.ask(arguments["query"], *(arguments.get("args") or []))
    if name == "read":
        return session.read(arguments["ref"])
    if name == "open":
        return session.open(arguments["obligation"])
    return session.inspect()


def handle(connect: Callable[[str, Path], Any], message: Any) -> dict[str, Any] | None:
    """The response to one JSON-RPC message, or None for a notification."""

    if not isinstance(message, dict) or message.get("jsonrpc") != "2.0" or not isinstance(message.get("method"), str):
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "invalid request"}}
    method, ident = message["method"], message.get("id")
    if "id" not in message:
        return None  # a notification, notifications/initialized among them
    params = message.get("params") if isinstance(message.get("params"), dict) else {}
    if method == "initialize":
        result: Any = {"protocolVersion": PROTOCOL, "capabilities": {"tools": {"listChanged": False}},
                       "serverInfo": SERVER}
    elif method == "ping":
        result = {}
    elif method == "tools/list":
        result = {"tools": tool_list()}
    elif method == "tools/call":
        name, arguments = params.get("name"), params.get("arguments")
        if not isinstance(name, str) or not isinstance(arguments, dict) or "ledger" not in arguments:
            return {"jsonrpc": "2.0", "id": ident, "error": {"code": -32602, "message": "invalid params"}}
        try:
            answer, failed = call(connect, name, arguments), False
        except (Refused, KeyError) as refused:
            answer, failed = {"refused": str(refused)}, True
        result = {"content": [{"type": "text", "text": json.dumps(answer, sort_keys=True, default=str)}],
                  "isError": failed}
    else:
        return {"jsonrpc": "2.0", "id": ident, "error": {"code": -32601, "message": f"method not found: {method}"}}
    return {"jsonrpc": "2.0", "id": ident, "result": result}


def serve(connect: Callable[[str, Path], Any], lines: Iterable[str], out: TextIO) -> None:
    """Answer each line of ``lines`` on ``out``, until the input ends."""

    for line in lines:
        if not line.strip():
            continue
        try:
            message = json.loads(line)
        except ValueError:
            response: dict[str, Any] | None = {"jsonrpc": "2.0", "id": None,
                                               "error": {"code": -32700, "message": "parse error"}}
        else:
            response = handle(connect, message)
        if response is not None:
            out.write(json.dumps(response, sort_keys=True) + "\n")
            out.flush()


__all__ = ["PROTOCOL", "TOOLS", "call", "handle", "serve", "tool_list"]
