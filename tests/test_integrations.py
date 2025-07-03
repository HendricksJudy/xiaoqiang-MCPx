from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.integrations.fastgpt_client import FastGPTClient
from src.integrations.clinicaltrials_api import ClinicalTrialsAPI
from src.integrations.external_apis import ExternalAPI


@pytest.mark.asyncio
async def test_fastgpt():
    client = FastGPTClient()
    resp = await client.query("hello")
    assert "hello" in resp


@pytest.mark.asyncio
async def test_clinical_trials():
    api = ClinicalTrialsAPI()
    trials = await api.search("肺癌")
    assert trials[0]["title"].startswith("Trial")


@pytest.mark.asyncio
async def test_external_api():
    api = ExternalAPI()
    data = await api.fetch("/foo")
    assert data["endpoint"] == "/foo"
