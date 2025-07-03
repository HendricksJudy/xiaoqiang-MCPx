from pathlib import Path
import sys
import json

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.server.mcp_server import MCPServer
from src.server.message_handler import JSONRPCMessageHandler
from src.resources.knowledge_db import KnowledgeDB
from src.prompts import get_prompt
from src.integrations.fastgpt_client import FastGPTClient


@pytest.mark.asyncio
async def test_message_handler_tools_list():
    server = MCPServer()
    handler = JSONRPCMessageHandler(server)
    msg = json.dumps({"id": "1", "method": "tools/list", "params": {}})
    resp_text = await handler.handle(msg)
    resp = json.loads(resp_text)
    assert "result" in resp


def test_resources_and_prompts():
    db = KnowledgeDB()
    assert db.lookup("癌症")
    prompt = get_prompt("medical_summary")
    assert "医学摘要" in prompt


@pytest.mark.asyncio
async def test_fastgpt_client():
    client = FastGPTClient()
    resp = await client.query("hello")
    assert "hello" in resp
