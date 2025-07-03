"""Lightweight structured logger wrapper."""

import structlog


def get_logger(name: str = "mcp") -> structlog.BoundLogger:
    """Return a bound structlog logger."""
    return structlog.get_logger(name)
