import os
from ..utils.errors import McpError


def verify_token(token: str) -> None:
    """Verify access token against ``MCP_TOKEN`` environment variable."""
    expected = os.getenv("MCP_TOKEN", "testtoken")
    if token != expected:
        raise McpError(-32001, "无效的Token")
