import asyncio
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.utils.cache import cached_tool


class Dummy:
    def __init__(self):
        self.calls = 0

    @cached_tool(ttl=0)
    async def tool(self, x: int) -> int:
        self.calls += 1
        await asyncio.sleep(0)  # yield
        return x * 2


@pytest.mark.asyncio
async def test_cached_tool():
    d = Dummy()
    first = await d.tool(1)
    second = await d.tool(1)
    await asyncio.sleep(0)
    assert first == second
    assert d.calls == 1

