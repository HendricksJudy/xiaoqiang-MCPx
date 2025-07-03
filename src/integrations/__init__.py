"""External integrations used by the server."""

from .fastgpt_client import FastGPTClient
from .clinicaltrials_api import ClinicalTrialsAPI
from .external_apis import ExternalAPIClient

__all__ = ["FastGPTClient", "ClinicalTrialsAPI", "ExternalAPIClient"]
