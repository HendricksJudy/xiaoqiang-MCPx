"""Travel planning tool for out-of-town medical visits."""

from typing import List, Dict

from ..utils.cache import cached_tool
from ..utils.errors import handle_mcp_errors
from ..schemas import TravelPlanRequest


class TravelPlanner:
    """Provide simple travel plans using stubbed data."""

    def __init__(self) -> None:
        self.routes: Dict[str, List[Dict[str, str]]] = {
            "北京->上海": [
                {"mode": "高铁", "duration": "5h", "price": "553元"},
                {"mode": "飞机", "duration": "2h", "price": "1000元"},
            ],
            "广州->北京": [
                {"mode": "高铁", "duration": "8h", "price": "862元"},
            ],
        }

    @handle_mcp_errors
    @cached_tool()
    async def plan(self, origin: str, destination: str, date: str) -> List[Dict[str, str]]:
        """Return available travel options for the given route."""
        req = TravelPlanRequest(origin=origin, destination=destination, date=date)
        key = f"{req.origin}->{req.destination}"
        return self.routes.get(key, [])
