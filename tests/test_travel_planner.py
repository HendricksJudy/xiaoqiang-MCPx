from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.server.mcp_server import MCPServer, Request


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
        },
    )
    resp = await server.handle_request(req)
    assert resp["result"]
