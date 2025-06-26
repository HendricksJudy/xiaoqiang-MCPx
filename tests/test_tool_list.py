from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.server.mcp_server import MCPServer, Request

@pytest.mark.asyncio
async def test_tool_list():
    server = MCPServer()
    req = Request(id="1", method="tools/list", params={})
    resp = await server.handle_request(req)
    assert any(tool["name"] == "KnowledgeBase" for tool in resp["result"])
