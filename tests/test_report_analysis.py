from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.server.mcp_server import MCPServer, Request


@pytest.mark.asyncio
async def test_report_analysis():
    server = MCPServer()
    req = Request(
        id="1",
        method="tools/call",
        params={"name": "analyze_report", "arguments": {"report_type": "病理", "content": "癌细胞呈阳性"}},
    )
    resp = await server.handle_request(req)
    assert resp["result"]["report_type"] == "病理"
