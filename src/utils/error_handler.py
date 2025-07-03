"""Utility helpers for logging and formatting errors."""

import structlog

from .errors import McpError

logger = structlog.get_logger()


def log_and_format(err: Exception) -> dict:
    """Log ``err`` and return an error dict."""
    if isinstance(err, McpError):
        mcp_err = err
    else:
        mcp_err = McpError(-32603, str(err))
    logger.error("mcp_error", code=mcp_err.code, message=mcp_err.message)
    return {"code": mcp_err.code, "message": mcp_err.message}
