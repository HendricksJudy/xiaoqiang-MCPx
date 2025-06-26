"""Insurance policy consultation tool."""

from typing import List

from ..utils.cache import cached_tool
from ..utils.errors import handle_mcp_errors
from ..schemas import InsurancePolicyQueryRequest


class InsurancePolicy:
    """Simple lookup for regional insurance policies."""

    def __init__(self) -> None:
        self.policies = {
            "北京": ["门诊报销比例70%", "住院起付线1300元"],
            "上海": ["门诊报销比例60%", "住院起付线1000元"],
        }

    @handle_mcp_errors
    @cached_tool()
    async def query(self, region: str, topic: str = "") -> List[str]:
        """Return policies for the region optionally filtered by topic."""
        req = InsurancePolicyQueryRequest(region=region, topic=topic)
        results = self.policies.get(req.region, [])
        if req.topic:
            results = [p for p in results if req.topic in p]
        return results
