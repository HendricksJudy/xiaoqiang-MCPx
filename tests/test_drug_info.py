from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.server.mcp_server import MCPServer, Request


@pytest.mark.asyncio
async def test_drug_info_query():
    server = MCPServer()
    req = Request(
        id="1",
        method="tools/call",
        params={
            "name": "query_drug_info",
            "arguments": {"drug_name": "阿司匹林"},
            "token": "testtoken",
        },
    )
    resp = await server.handle_request(req)
    assert resp["result"].get("usage") == "解热镇痛、抗炎"
