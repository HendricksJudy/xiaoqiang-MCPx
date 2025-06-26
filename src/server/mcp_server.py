"""Minimal MCP-like server skeleton."""

import asyncio
from dataclasses import dataclass
from typing import Any, Dict

from ..tools.knowledge_base import KnowledgeBase
from ..tools.medical_resources import MedicalResources
from ..tools.report_analysis import ReportAnalysis
from ..tools.clinical_trials import ClinicalTrials
from ..tools.travel_planner import TravelPlanner
from ..tools.insurance_policy import InsurancePolicy
from ..tools.drug_info import DrugInfo
from ..utils.metrics import MCPMetrics
from ..utils.errors import McpError


@dataclass
class Request:
    id: str
    method: str
    params: Dict[str, Any]


class MCPServer:
    def __init__(self) -> None:
        self.kb = KnowledgeBase()
        self.resources = MedicalResources()
        self.report = ReportAnalysis()
        self.trials = ClinicalTrials()
        self.travel = TravelPlanner()
        self.policy = InsurancePolicy()
        self.drug = DrugInfo()
        self.metrics = MCPMetrics()

    async def handle_request(self, request: Request) -> Dict[str, Any]:
        if request.method == "tools/call":
            name = request.params.get("name")
            args = request.params.get("arguments", {})
            start = asyncio.get_event_loop().time()
            success = True
            try:
                if name == "query_knowledge_base":
                    result = await self.kb.query(
                        cancer_type=args.get("cancer_type", ""),
                        query=args.get("query", ""),
                        detail_level=args.get("detail_level", "详细"),
                    )
                elif name == "query_medical_resources":
                    result = await self.resources.query(
                        disease_type=args.get("disease_type", ""),
                        location=args.get("location", ""),
                        level=args.get("level", "三级甲等"),
                    )
                elif name == "analyze_report":
                    result = await self.report.analyze(
                        report_type=args.get("report_type", ""),
                        content=args.get("content", ""),
                    )
                elif name == "query_clinical_trials":
                    result = await self.trials.query(
                        disease_type=args.get("disease_type", ""),
                        location=args.get("location", ""),
                        patient_condition=args.get("patient_condition", ""),
                    )
                elif name == "plan_travel":
                    result = await self.travel.plan(
                        origin=args.get("origin", ""),
                        destination=args.get("destination", ""),
                        date=args.get("date", ""),
                    )
                elif name == "query_insurance_policy":
                    result = await self.policy.query(
                        region=args.get("region", ""),
                        topic=args.get("topic", ""),
                    )
                elif name == "query_drug_info":
                    result = await self.drug.query(
                        drug_name=args.get("drug_name", "")
                    )
                else:
                    return {
                        "id": request.id,
                        "error": {"code": -32601, "message": "Method not found"},
                        "jsonrpc": "2.0",
                    }
                return {"id": request.id, "result": result, "jsonrpc": "2.0"}
            except McpError as e:
                success = False
                return {
                    "id": request.id,
                    "error": {"code": e.code, "message": e.message},
                    "jsonrpc": "2.0",
                }
            except Exception:
                success = False
                raise
            finally:
                duration = asyncio.get_event_loop().time() - start
                self.metrics.record_tool_call(name or "unknown", duration, success)
        return {
            "id": request.id,
            "error": {"code": -32601, "message": "Method not found"},
            "jsonrpc": "2.0",
        }


async def main():
    server = MCPServer()
    while True:
        line = await asyncio.get_event_loop().run_in_executor(None, input)
        if not line:
            break
        try:
            import json
            req_data = json.loads(line)
            request = Request(
                id=req_data.get("id"),
                method=req_data.get("method"),
                params=req_data.get("params", {}),
            )
            response = await server.handle_request(request)
            print(json.dumps(response))
        except Exception as e:
            print(json.dumps({"error": str(e)}))


if __name__ == "__main__":
    asyncio.run(main())
