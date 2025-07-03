from pathlib import Path
import sys
import os
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.server.mcp_server import MCPServer, Request


@pytest.mark.asyncio
async def test_handle_unexpected_error(monkeypatch):
    server = MCPServer()

    def boom(token: str):
        raise RuntimeError("boom")

    monkeypatch.setattr('src.server.mcp_server.verify_token', boom)

    req = Request(
        id="1",
        method="tools/call",
        params={"name": "query_drug_info", "arguments": {"drug_name": "阿司匹林"}, "token": "bad", "session_id": "sess"},
    )
    resp = await server.handle_request(req)
    assert resp["error"]["code"] == -32603

