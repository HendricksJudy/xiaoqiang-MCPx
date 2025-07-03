from pathlib import Path
import sys
import os
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.security.auth import verify_token
from src.utils.errors import McpError


def test_missing_token_env(monkeypatch):
    monkeypatch.delenv("MCP_TOKEN", raising=False)
    with pytest.raises(McpError) as exc:
        verify_token("anything")
    assert exc.value.code == -32004

