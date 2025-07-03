from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.resources.knowledge_db import KnowledgeDB
from src.resources.medical_data import MedicalData


def test_knowledge_lookup():
    db = KnowledgeDB()
    assert db.lookup("癌症")


def test_medical_data():
    md = MedicalData()
    assert md.get("p1")["name"] == "张三"
