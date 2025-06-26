"""Medical resources lookup tool."""

from typing import List, Dict

from ..utils.cache import cached_tool
from ..utils.errors import handle_mcp_errors
from ..schemas import MedicalResourceQueryRequest


class MedicalResources:
    """Simple medical resource query tool."""

    def __init__(self) -> None:
        # minimal in-memory dataset
        self.data: Dict[str, List[Dict[str, str]]] = {
            "肺癌": [
                {"hospital": "北京肿瘤医院", "level": "三级甲等", "location": "北京"},
                {"hospital": "上海肺科医院", "level": "三级甲等", "location": "上海"},
            ],
            "乳腺癌": [
                {"hospital": "上海肿瘤医院", "level": "三级甲等", "location": "上海"},
            ],
        }

    @handle_mcp_errors
    @cached_tool()
    async def query(self, disease_type: str, location: str = "", level: str = "三级甲等") -> List[Dict[str, str]]:
        """Return hospitals matching the disease type, location and level."""
        req = MedicalResourceQueryRequest(disease_type=disease_type, location=location, level=level)
        resources = [
            r for r in self.data.get(req.disease_type, [])
            if (not req.location or r["location"] == req.location) and (not req.level or r["level"] == req.level)
        ]
        return resources
