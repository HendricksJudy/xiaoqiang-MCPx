"""Asynchronous server transport implementations."""

import asyncio
from typing import Optional


class BaseTransport:
    """Abstract transport base class."""

    async def receive(self) -> Optional[str]:
        raise NotImplementedError

    async def send(self, data: str) -> None:
        raise NotImplementedError

    async def close(self) -> None:
        """Clean up transport resources."""
        return None


class StdioTransport(BaseTransport):
    """Simple stdio based transport used for local testing."""

    async def receive(self) -> Optional[str]:
        loop = asyncio.get_event_loop()
        line = await loop.run_in_executor(None, input)
        return line if line else None

    async def send(self, data: str) -> None:
        print(data)
