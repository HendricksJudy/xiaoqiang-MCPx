from pathlib import Path
import sys
import os
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.server.mcp_server import MCPServer, Request

os.environ["MCP_SESSION_ID"] = "sess"


@pytest.mark.asyncio
async def test_travel_plan():
    server = MCPServer()
    req = Request(
        id="1",
        method="tools/call",
        params={
            "name": "plan_travel",
            "arguments": {"origin": "北京", "destination": "上海", "date": "2024-01-01"},
            "token": "testtoken",
            "session_id": "sess",
        },
    )
    resp = await server.handle_request(req)
    assert resp["result"]
