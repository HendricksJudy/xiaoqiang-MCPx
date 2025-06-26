"""Drug information query tool."""

from typing import Dict

from ..utils.cache import cached_tool
from ..utils.errors import handle_mcp_errors
from ..schemas import DrugInfoQueryRequest


class DrugInfo:
    """Provide basic drug information lookup."""

    def __init__(self) -> None:
        self.data: Dict[str, Dict[str, str]] = {
            "阿司匹林": {
                "usage": "解热镇痛、抗炎", "side_effect": "胃肠刺激", "price": "约20元"
            },
            "吉非替尼": {
                "usage": "肺癌靶向药物", "side_effect": "皮疹、腹泻", "price": "约5000元"
            },
        }

    @handle_mcp_errors
    @cached_tool()
    async def query(self, drug_name: str) -> Dict[str, str]:
        """Return information for the specified drug."""
        req = DrugInfoQueryRequest(drug_name=drug_name)
        return self.data.get(req.drug_name, {})
