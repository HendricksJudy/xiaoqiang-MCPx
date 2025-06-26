"""Clinical trials query tool."""

from typing import List, Dict

from ..utils.cache import cached_tool
from ..utils.errors import handle_mcp_errors
from ..schemas import ClinicalTrialQueryRequest


class ClinicalTrials:
    """Simple clinical trials lookup."""

    def __init__(self) -> None:
        self.data: Dict[str, List[Dict[str, str]]] = {
            "肺癌": [
                {"title": "EGFR抑制剂研究", "location": "北京", "criteria": "18-65岁"},
            ],
            "乳腺癌": [
                {"title": "HER2靶向临床试验", "location": "上海", "criteria": "女性，18-70岁"},
            ],
        }

    @handle_mcp_errors
    @cached_tool()
    async def query(
        self, disease_type: str, location: str = "", patient_condition: str = ""
    ) -> List[Dict[str, str]]:
        """Return clinical trials for the given disease type and location."""
        req = ClinicalTrialQueryRequest(
            disease_type=disease_type, location=location, patient_condition=patient_condition
        )
        results = [
            t
            for t in self.data.get(req.disease_type, [])
            if (not req.location or t["location"] == req.location)
        ]
        return results
