from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.server.mcp_server import MCPServer, Request


@pytest.mark.asyncio
async def test_insurance_policy_query():
    server = MCPServer()
    req = Request(
        id="1",
        method="tools/call",
        params={"name": "query_insurance_policy", "arguments": {"region": "北京"}},
    )
    resp = await server.handle_request(req)
    assert resp["result"]
