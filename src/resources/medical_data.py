"""Stub medical data resource."""

from typing import Dict

from ..utils.errors import handle_mcp_errors


class MedicalData:
    """Provide access to simplified medical datasets."""

    def __init__(self) -> None:
        self.data: Dict[str, Dict[str, str]] = {
            "阿司匹林": {"usage": "止痛、退热", "price": "5元"},
        }

    @handle_mcp_errors
    async def get(self, name: str) -> Dict[str, str]:
        """Return information about the given medical item."""
        return self.data.get(name, {})
