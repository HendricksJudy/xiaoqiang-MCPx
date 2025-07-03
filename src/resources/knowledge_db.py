"""Simple in-memory knowledge database resource."""

from typing import List

from ..utils.errors import handle_mcp_errors


class KnowledgeDB:
    """Provide articles related to different cancer types."""

    def __init__(self) -> None:
        self.articles = {
            "肺癌": ["肺癌概述", "肺癌治疗方案"],
            "乳腺癌": ["乳腺癌检查项目", "乳腺癌治疗"],
        }

    @handle_mcp_errors
    async def search(self, cancer_type: str) -> List[str]:
        """Return article titles for a given cancer type."""
        return self.articles.get(cancer_type, [])
