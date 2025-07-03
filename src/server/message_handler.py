"""JSON-RPC message handling utilities."""

import json
from typing import Any, Dict

from .mcp_server import MCPServer, Request


class JSONRPCMessageHandler:
    """Convert raw JSON-RPC strings to server responses."""

    def __init__(self, server: MCPServer) -> None:
        self.server = server

    async def handle(self, message: str) -> str:
        data: Dict[str, Any] = json.loads(message)
        request = Request(
            id=data.get("id"),
            method=data.get("method"),
            params=data.get("params", {}),
        )
        response = await self.server.handle_request(request)
        return json.dumps(response, ensure_ascii=False)
