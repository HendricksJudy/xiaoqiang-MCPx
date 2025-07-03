"""Stub client for interacting with a FastGPT service."""

from ..utils.errors import handle_mcp_errors


class FastGPTClient:
    """Very small wrapper around a hypothetical FastGPT API."""

    def __init__(self) -> None:
        pass

    @handle_mcp_errors
    async def query(self, prompt: str) -> str:
        """Return a mock response for the given prompt."""
        return f"FastGPT response for: {prompt}"
