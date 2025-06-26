"""Server capability declaration."""

from pathlib import Path
import json


_DEFAULT_CAPABILITIES = {
    "tools": {"listChanged": True},
    "resources": {"subscribe": True, "listChanged": True},
    "prompts": {"listChanged": True},
    "logging": {},
}


def get_capabilities() -> dict:
    """Return server capability declaration from ``config/capabilities.json``."""
    cfg_path = Path(__file__).resolve().parents[2] / "config" / "capabilities.json"
    if cfg_path.exists():
        with cfg_path.open("r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                pass
    return _DEFAULT_CAPABILITIES
