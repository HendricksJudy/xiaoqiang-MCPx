"""Data validation helpers using Pydantic."""

from typing import Type, Any
from pydantic import BaseModel, ValidationError

from ..utils.errors import McpError


def validate(data: Any, schema: Type[BaseModel]) -> BaseModel:
    """Validate ``data`` against ``schema`` and return the parsed model."""
    try:
        return schema(**data)
    except ValidationError as e:
        raise McpError(-32602, f"参数验证失败: {e}")
