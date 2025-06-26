"""Minimal MCP-like server skeleton."""

import asyncio
from dataclasses import dataclass
from typing import Any, Dict

from ..tools.knowledge_base import KnowledgeBase
from ..utils.metrics import MCPMetrics

@dataclass
class Request:
    id: str
    method: str
    params: Dict[str, Any]

class MCPServer:
    def __init__(self) -> None:
        self.kb = KnowledgeBase()
        self.metrics = MCPMetrics()

    async def handle_request(self, request: Request) -> Dict[str, Any]:
        if request.method == "tools/call" and request.params.get("name") == "query_knowledge_base":
            args = request.params.get("arguments", {})
            start = asyncio.get_event_loop().time()
            success = True
            try:
                result = await self.kb.query(
                    cancer_type=args.get("cancer_type", ""),
                    query=args.get("query", ""),
                    detail_level=args.get("detail_level", "详细"),
                )
                return {"id": request.id, "result": result, "jsonrpc": "2.0"}
            except Exception:
                success = False
                raise
            finally:
                duration = asyncio.get_event_loop().time() - start
                self.metrics.record_tool_call("query_knowledge_base", duration, success)
        return {"id": request.id, "error": {"code": -32601, "message": "Method not found"}, "jsonrpc": "2.0"}

async def main():
    server = MCPServer()
    while True:
        line = await asyncio.get_event_loop().run_in_executor(None, input)
        if not line:
            break
        try:
            import json
            req_data = json.loads(line)
            request = Request(id=req_data.get("id"), method=req_data.get("method"), params=req_data.get("params", {}))
            response = await server.handle_request(request)
            print(json.dumps(response))
        except Exception as e:
            print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    asyncio.run(main())
