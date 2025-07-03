from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.security.rate_limiter import RateLimiter


def test_rate_limiter_cleanup(monkeypatch):
    rl = RateLimiter(max_requests=5, window=1)
    current = [0]

    def fake_time():
        return current[0]

    monkeypatch.setattr("src.security.rate_limiter.time.time", fake_time)

    rl.check("a")
    assert "a" in rl._requests

    current[0] = 2
    rl.check("b")
    assert "a" not in rl._requests
    assert "b" in rl._requests

