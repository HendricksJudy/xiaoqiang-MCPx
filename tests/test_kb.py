import asyncio
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.server.mcp_server import MCPServer, Request

import pytest

os.environ["MCP_SESSION_ID"] = "sess"

@pytest.mark.asyncio
async def test_query():
    server = MCPServer()
    req = Request(
        id="1",
        method="tools/call",
        params={
            "name": "query_knowledge_base",
            "arguments": {"cancer_type": "肺癌", "query": "靶向"},
            "token": "testtoken",
            "session_id": "sess",
        },
    )
    resp = await server.handle_request(req)
    assert resp["result"]

if __name__ == "__main__":
    asyncio.run(test_query())
