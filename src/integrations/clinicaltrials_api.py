"""Stub interface for querying clinical trials."""

from typing import List, Dict


class ClinicalTrialsAPI:
    async def search(self, disease: str) -> List[Dict[str, str]]:
        """Return fake clinical trial data."""
        return [{"title": f"Trial for {disease}", "location": "N/A"}]
