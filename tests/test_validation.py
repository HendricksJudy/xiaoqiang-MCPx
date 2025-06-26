from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.schemas import KnowledgeQueryRequest
from pydantic import ValidationError


def test_validation_error():
    with pytest.raises(ValidationError):
        KnowledgeQueryRequest(cancer_type="未知癌症", query="a")

