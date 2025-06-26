"""Medical report analysis tool."""

from typing import Dict

from ..utils.cache import cached_tool
from ..utils.errors import handle_mcp_errors
from ..schemas import ReportAnalysisRequest


class ReportAnalysis:
    """Simple medical report analysis tool."""

    @handle_mcp_errors
    @cached_tool()
    async def analyze(self, report_type: str, content: str) -> Dict[str, str]:
        """Return a basic analysis result for the given report."""
        req = ReportAnalysisRequest(report_type=report_type, content=content)
        return {
            "report_type": req.report_type,
            "summary": f"{req.report_type}报告分析结果",
            "suggestion": "请咨询专业医生",
        }
