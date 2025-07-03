"""Medical data resource placeholder."""

from typing import Dict, Any


class MedicalData:
    def __init__(self) -> None:
        self._patients: Dict[str, Dict[str, Any]] = {
            "p1": {"name": "张三", "age": 30},
        }

    def get(self, patient_id: str) -> Dict[str, Any]:
        """Return fake patient data."""
        return self._patients.get(patient_id, {})
