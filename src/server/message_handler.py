"""JSON-RPC message handling utilities."""

import json
from typing import Optional

from .mcp_server import MCPServer, Request
from .transport import BaseTransport


class MessageHandler:
    """Handle incoming JSON-RPC messages using a server and transport."""

    def __init__(self, server: MCPServer, transport: BaseTransport) -> None:
        self.server = server
        self.transport = transport

    async def handle(self) -> None:
        """Continuously process messages from the transport."""
        while True:
            raw = await self.transport.receive()
            if raw is None:
                break
            try:
                data = json.loads(raw)
                request = Request(
                    id=data.get("id", ""),
                    method=data.get("method", ""),
                    params=data.get("params", {}),
                )
                response = await self.server.handle_request(request)
            except Exception as e:  # pragma: no cover - unexpected errors
                response = {"error": str(e)}
            await self.transport.send(json.dumps(response, ensure_ascii=False))
