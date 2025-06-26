from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.server.mcp_server import MCPServer, Request

@pytest.mark.asyncio
async def test_get_capabilities():
    server = MCPServer()
    req = Request(id="1", method="server/get_capabilities", params={})
    resp = await server.handle_request(req)
    assert resp["result"].get("tools")
