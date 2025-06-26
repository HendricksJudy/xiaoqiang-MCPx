"""Knowledge base query tool."""

from typing import List

from ..utils.cache import cached_tool
from ..utils.errors import handle_mcp_errors
from ..schemas import KnowledgeQueryRequest

class KnowledgeBase:
    """Simple in-memory knowledge base for cancer-related information."""

    def __init__(self):
        self.data = {
            "肺癌": [
                "靶向治疗药物包括EGFR抑制剂等。",
                "早期发现对于治疗至关重要。",
            ],
            "乳腺癌": [
                "常见治疗手段包括手术、放疗和化疗。",
            ],
        }

    @handle_mcp_errors
    @cached_tool()
    async def query(self, cancer_type: str, query: str, detail_level: str = "详细") -> List[str]:
        """Return basic information for the given cancer type."""
        req = KnowledgeQueryRequest(cancer_type=cancer_type, query=query, detail_level=detail_level)
        results = self.data.get(req.cancer_type, [])
        if req.detail_level == "简要":
            return results[:1]
        return results
