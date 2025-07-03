from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.server.mcp_server import MCPServer, Request


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
        },
    )
    resp = await server.handle_request(req)
    assert resp["result"]
