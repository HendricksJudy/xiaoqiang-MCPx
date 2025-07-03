"""Simplified wrapper for a clinical trials API."""

from typing import List, Dict

from ..utils.errors import handle_mcp_errors


class ClinicalTrialsAPI:
    """Provide access to clinical trial data."""

    def __init__(self) -> None:
        pass

    @handle_mcp_errors
    async def search(self, disease: str) -> List[Dict[str, str]]:
        """Return mock clinical trial info for the given disease."""
        return [
            {"title": f"{disease} trial", "location": "N/A", "criteria": ""}
        ]
