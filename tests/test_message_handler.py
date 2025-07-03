from pathlib import Path
import sys
import json
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.server.message_handler import MessageHandler
from src.server.transport import BaseTransport


class DummyTransport(BaseTransport):
    def __init__(self, messages):
        self.messages = messages
        self.sent = []

    async def receive(self):
        return self.messages.pop(0) if self.messages else None

    async def send(self, data: str):
        self.sent.append(data)


class ErrorServer:
    async def handle_request(self, request):
        raise RuntimeError("boom")


@pytest.mark.asyncio
async def test_message_handler_generic_error():
    transport = DummyTransport(['{"id": "1", "method": "x"}'])
    handler = MessageHandler(ErrorServer(), transport)
    await handler.handle()
    assert len(transport.sent) == 1
    resp = json.loads(transport.sent[0])
    assert resp["error"] == "内部服务器错误"

