"""The MCP transport (Manual §16.10; catalogue §16.10; Phase F step 8f, reading F70).

JSON-RPC 2.0 over stdio, one message per line, built on the standard library: no runtime dependency is added (plan
line 739). It implements the Model Context Protocol revision ``PROTOCOL`` for the tools capability only, and exposes
the same logical operations as the CLI (``status``, ``ask``, ``read``, ``open``, ``inspect``) through the same
``Session``, so a transport never answers differently from another. The session factory is the composition root's.

A call's arguments are checked against the tool's input schema first: an unknown tool or invalid arguments is the
protocol error ``-32602``. A refusal is exactly the CLI's (``Refused``, ``HomeRefused``), answered as a tool result
with ``isError``; any other exception is a fault, answered ``-32603`` and never reported as a refusal, and the server
keeps serving (review of 4d949827, B1).
"""

from __future__ import annotations

import json
from collections.abc import Callable, Iterable
from pathlib import Path
from typing import Any, TextIO

from ssds.ledger.qualification import HomeRefused

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
                             "required": ["ledger", *spec["required"]], "additionalProperties": False}}
            for name, spec in TOOLS.items()]


def valid(name: Any, arguments: Any) -> bool:
    """The call names a tool and its arguments meet that tool's input schema exactly."""

    if not isinstance(name, str) or name not in TOOLS or not isinstance(arguments, dict):
        return False
    properties = {**_LEDGER, **TOOLS[name]["properties"]}
    if not {"ledger", *TOOLS[name]["required"]} <= set(arguments) or not set(arguments) <= set(properties):
        return False
    for key, value in arguments.items():
        if properties[key]["type"] == "string" and not isinstance(value, str):
            return False
        if properties[key]["type"] == "array" and not (isinstance(value, list) and all(isinstance(v, str) for v in value)):
            return False
    return True


def call(connect: Callable[[str, Path], Any], name: str, arguments: dict[str, Any]) -> Any:
    """One tool call, through the same ``Session`` the CLI uses; ``arguments`` already ``valid``."""

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

    if isinstance(message, dict) and message.get("jsonrpc") == "2.0" and "method" not in message \
            and ("result" in message or "error" in message):
        return None  # a response to a request of ours: the server sends none, so there is nothing to answer
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
        if not valid(name, arguments):
            return {"jsonrpc": "2.0", "id": ident, "error": {"code": -32602, "message": "invalid params"}}
        try:
            answer, failed = call(connect, name, arguments), False
        except (Refused, HomeRefused) as refused:  # only refusals, as the CLI's: a fault is never reported as one
            answer, failed = {"refused": refused.args[0] if refused.args else str(refused)}, True
        except Exception:  # noqa: BLE001 - a fault: an internal error, and the server keeps serving
            return {"jsonrpc": "2.0", "id": ident, "error": {"code": -32603, "message": "internal error"}}
        result = {"content": [{"type": "text", "text": json.dumps(answer, sort_keys=True, default=str)}],
                  "isError": failed}
    else:
        return {"jsonrpc": "2.0", "id": ident, "error": {"code": -32601, "message": f"method not found: {method}"}}
    return {"jsonrpc": "2.0", "id": ident, "result": result}


def serve(connect: Callable[[str, Path], Any], lines: Iterable[str | bytes], out: TextIO) -> None:
    """Answer each line of ``lines`` on ``out``, until the input ends. A line that is not UTF-8 JSON is a parse
    error, answered, and the server keeps serving."""

    for line in lines:
        if not line.strip():
            continue
        try:
            message = json.loads(line)  # bytes are decoded as UTF-8: invalid UTF-8 is a ValueError
        except ValueError:
            response: dict[str, Any] | None = {"jsonrpc": "2.0", "id": None,
                                               "error": {"code": -32700, "message": "parse error"}}
        else:
            response = handle(connect, message)
        if response is not None:
            out.write(json.dumps(response, sort_keys=True) + "\n")
            out.flush()


__all__ = ["PROTOCOL", "TOOLS", "call", "handle", "serve", "tool_list", "valid"]
