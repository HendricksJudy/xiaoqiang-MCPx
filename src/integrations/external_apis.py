"""Miscellaneous external API wrappers."""

from typing import Any, Dict


class ExternalAPI:
    async def fetch(self, endpoint: str) -> Dict[str, Any]:
        """Return fake data for the given endpoint."""
        return {"endpoint": endpoint, "data": "placeholder"}
