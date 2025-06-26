from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.utils.docs import generate_tool_docs
from src.tools.knowledge_base import KnowledgeBase


def test_generate_docs():
    docs = generate_tool_docs(KnowledgeBase)
    assert docs["name"] == "KnowledgeBase"
    assert isinstance(docs["methods"], list)


