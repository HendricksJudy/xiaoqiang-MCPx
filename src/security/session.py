import os
from ..utils.errors import McpError


def verify_session(session_id: str) -> None:
    """Verify session id against ``MCP_SESSION_ID`` env variable if set."""
    expected = os.getenv("MCP_SESSION_ID")
    if expected and session_id != expected:
        raise McpError(-32003, "无效的会话ID")
