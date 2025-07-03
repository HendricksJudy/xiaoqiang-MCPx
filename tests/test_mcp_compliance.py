from pathlib import Path
import json
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.server.mcp_server import MCPServer, Request
from src.server.capabilities import get_capabilities


def test_config_file():
    cfg = Path(__file__).resolve().parents[1] / "config" / "mcp_config.json"
    assert cfg.exists()
    with cfg.open("r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["name"] == "xiaoqiang-MCPx"


@pytest.mark.asyncio
async def test_capabilities_and_tools():
    server = MCPServer()
    cap_resp = await server.handle_request(Request(id="1", method="server/get_capabilities", params={}))
    assert cap_resp["jsonrpc"] == "2.0"
    tools_resp = await server.handle_request(Request(id="2", method="tools/list", params={}))
    assert isinstance(tools_resp["result"], list)
