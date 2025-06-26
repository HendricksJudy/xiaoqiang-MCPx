"""Error handling utilities."""

from typing import Callable, Awaitable, Any

import structlog
from pydantic import ValidationError

logger = structlog.get_logger()


class McpError(Exception):
    """Generic MCP error with code and message."""

    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)


class MedicalDataError(McpError):
    """Medical data related error."""

    def __init__(self, message: str, code: int = -32000) -> None:
        super().__init__(code, message)


def handle_mcp_errors(func: Callable[..., Awaitable[Any]]):
    """Decorator converting common exceptions to ``McpError``."""

    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ValidationError as e:
            raise McpError(-32602, f"参数验证失败: {e}")
        except McpError:
            raise
        except Exception as e:  # pragma: no cover - unexpected errors
            logger.error("unexpected_error", error=str(e))
            raise McpError(-32603, "内部服务器错误")

    return wrapper
