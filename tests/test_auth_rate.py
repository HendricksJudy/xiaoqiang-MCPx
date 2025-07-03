from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.server.mcp_server import MCPServer, Request
from src.security.rate_limiter import RateLimiter


@pytest.mark.asyncio
async def test_invalid_token():
    server = MCPServer()
    req = Request(id="1", method="tools/call", params={"name": "query_drug_info", "arguments": {"drug_name": "阿司匹林"}, "token": "bad"})
    resp = await server.handle_request(req)
    assert resp["error"]["code"] == -32001


@pytest.mark.asyncio
async def test_rate_limit():
    server = MCPServer()
    server.rate_limiter = RateLimiter(max_requests=1, window=3600)
    params = {"name": "query_drug_info", "arguments": {"drug_name": "阿司匹林"}, "token": "testtoken"}
    req = Request(id="1", method="tools/call", params=params)
    resp1 = await server.handle_request(req)
    assert "result" in resp1
    req2 = Request(id="2", method="tools/call", params=params)
    resp2 = await server.handle_request(req2)
    assert resp2["error"]["code"] == -32002
