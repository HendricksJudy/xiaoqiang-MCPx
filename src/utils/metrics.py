import structlog
from datetime import datetime

logger = structlog.get_logger()

class MCPMetrics:
    """Simple metrics collector with structured logging."""

    def __init__(self) -> None:
        self.tool_calls = {}
        self.error_counts = {}
        self.response_times = []

    def record_tool_call(self, tool_name: str, duration: float, success: bool) -> None:
        if tool_name not in self.tool_calls:
            self.tool_calls[tool_name] = {"count": 0, "success": 0}
        self.tool_calls[tool_name]["count"] += 1
        if success:
            self.tool_calls[tool_name]["success"] += 1

        self.response_times.append(duration)

        logger.info(
            "tool_call_completed",
            tool_name=tool_name,
            duration=duration,
            success=success,
            timestamp=datetime.now().isoformat(),
        )

