from .medical_prompts import MEDICAL_SUMMARY_PROMPT

PROMPTS = {
    "medical_summary": MEDICAL_SUMMARY_PROMPT,
}


def get_prompt(name: str) -> str:
    if name not in PROMPTS:
        raise KeyError(name)
    return PROMPTS[name]

__all__ = ["get_prompt", "MEDICAL_SUMMARY_PROMPT"]
