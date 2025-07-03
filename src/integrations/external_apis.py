"""Generic wrapper for other external APIs."""

from ..utils.errors import handle_mcp_errors


class ExternalAPIClient:
    """Stub client for miscellaneous external services."""

    def __init__(self) -> None:
        pass

    @handle_mcp_errors
    async def get(self, name: str) -> str:
        """Return a placeholder response."""
        return f"external data for {name}"
