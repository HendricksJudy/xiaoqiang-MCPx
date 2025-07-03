import os
import pytest

@pytest.fixture(autouse=True)
def set_mcp_token():
    os.environ["MCP_TOKEN"] = "testtoken"
    yield

