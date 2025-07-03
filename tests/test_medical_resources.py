import asyncio
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.server.mcp_server import MCPServer, Request

import pytest


@pytest.mark.asyncio
async def test_medical_resources_query():
    server = MCPServer()
    req = Request(
        id="1",
        method="tools/call",
        params={
            "name": "query_medical_resources",
            "arguments": {"disease_type": "肺癌", "location": "北京"},
            "token": "testtoken",
        },
    )
    resp = await server.handle_request(req)
    assert resp["result"]
