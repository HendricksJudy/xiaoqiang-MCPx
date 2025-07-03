"""Built-in resource providers."""

from .knowledge_db import KnowledgeDB
from .medical_data import MedicalData

__all__ = ["KnowledgeDB", "MedicalData"]
