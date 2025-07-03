from pathlib import Path
import sys
import os

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.server.mcp_server import MCPServer, Request

os.environ["MCP_SESSION_ID"] = "sess"


@pytest.mark.asyncio
async def test_clinical_trials_query():
    server = MCPServer()
    req = Request(
        id="1",
        method="tools/call",
        params={
            "name": "query_clinical_trials",
            "arguments": {"disease_type": "肺癌"},
            "token": "testtoken",
            "session_id": "sess",
        },
    )
    resp = await server.handle_request(req)
    assert resp["result"]
