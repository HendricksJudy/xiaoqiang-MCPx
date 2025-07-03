import time
from typing import Dict, Tuple

from ..utils.errors import McpError


class RateLimiter:
    """Simple in-memory rate limiter."""

    def __init__(self, max_requests: int = 100, window: int = 3600) -> None:
        self.max_requests = max_requests
        self.window = window
        self._requests: Dict[str, Tuple[int, float]] = {}

    def _purge_expired(self, now: float) -> None:
        expired = [t for t, (_, start) in self._requests.items() if now - start > self.window]
        for t in expired:
            del self._requests[t]

    def check(self, token: str) -> None:
        now = time.time()
        self._purge_expired(now)
        count, start = self._requests.get(token, (0, now))
        if now - start > self.window:
            count = 0
            start = now
        if count >= self.max_requests:
            raise McpError(-32002, "请求过于频繁")
        self._requests[token] = (count + 1, start)

