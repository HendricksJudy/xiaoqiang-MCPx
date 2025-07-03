"""Stub client for FastGPT integration."""

class FastGPTClient:
    def __init__(self, base_url: str = "http://localhost") -> None:
        self.base_url = base_url

    async def query(self, prompt: str) -> str:
        """Return a fake response for the given prompt."""
        return f"fastgpt response: {prompt}"
