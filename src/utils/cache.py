import asyncio
from functools import wraps
from typing import Any, Dict, Callable, Awaitable

class MCPCache:
    """Simple async TTL cache for MCP tools."""

    def __init__(self, ttl: int = 3600) -> None:
        self.ttl = ttl
        self.cache: Dict[str, Any] = {}

    async def get_or_set(self, key: str, func: Callable[..., Awaitable[Any]], *args, **kwargs) -> Any:
        if key in self.cache:
            return self.cache[key]

        result = await func(*args, **kwargs)
        self.cache[key] = result
        loop = asyncio.get_running_loop()
        loop.call_later(self.ttl, lambda: self.cache.pop(key, None))
        return result


def cached_tool(ttl: int = 3600):
    """Decorator for caching async tool results."""

    def decorator(func: Callable[..., Awaitable[Any]]):
        cache = MCPCache(ttl)

        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"
            return await cache.get_or_set(cache_key, func, *args, **kwargs)

        return wrapper

    return decorator
