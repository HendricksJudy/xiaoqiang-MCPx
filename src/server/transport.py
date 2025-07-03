import asyncio

class StdioServerTransport:
    """Simple stdio-based transport for local usage."""

    async def receive(self) -> str:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, input)

    async def send(self, message: str) -> None:
        print(message)


class SseServerTransport:
    """Minimal async SSE-like transport using an in-memory queue."""

    def __init__(self, path: str = "/message", host: str = "127.0.0.1", port: int = 8080, ssl_context=None) -> None:
        self.path = path
        self.host = host
        self.port = port
        self.ssl_context = ssl_context
        self._queue: asyncio.Queue[str] = asyncio.Queue()

    async def receive(self) -> str:
        return await self._queue.get()

    async def send(self, message: str) -> None:
        await self._queue.put(message)
