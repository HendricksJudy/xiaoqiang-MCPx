"""Pydantic data models used for request validation."""

from pydantic import BaseModel, validator


class KnowledgeQueryRequest(BaseModel):
    """Schema for knowledge base query requests."""

    cancer_type: str
    query: str
    detail_level: str = "详细"

    @validator("cancer_type")
    def validate_cancer_type(cls, v: str) -> str:
        allowed_types = ["肺癌", "乳腺癌", "胃癌", "肝癌", "结直肠癌"]
        if v not in allowed_types:
            raise ValueError(f"不支持的癌症类型: {v}")
        return v

    @validator("query")
    def validate_query(cls, v: str) -> str:
        if len(v.strip()) < 2:
            raise ValueError("查询内容不能少于2个字符")
        return v.strip()


class MedicalResourceQueryRequest(BaseModel):
    """Schema for medical resource lookup."""

    disease_type: str
    location: str = ""
    level: str = "三级甲等"

    @validator("disease_type")
    def validate_disease_type(cls, v: str) -> str:
        allowed_types = ["肺癌", "乳腺癌", "胃癌", "肝癌", "结直肠癌"]
        if v not in allowed_types:
            raise ValueError(f"不支持的疾病类型: {v}")
        return v


class ReportAnalysisRequest(BaseModel):
    """Schema for medical report analysis."""

    report_type: str
    content: str

    @validator("report_type")
    def validate_report_type(cls, v: str) -> str:
        allowed_types = ["病理", "影像", "血液", "基因"]
        if v not in allowed_types:
            raise ValueError(f"不支持的报告类型: {v}")
        return v

    @validator("content")
    def validate_content(cls, v: str) -> str:
        if len(v.strip()) < 5:
            raise ValueError("报告内容过短")
        return v.strip()


class ClinicalTrialQueryRequest(BaseModel):
    """Schema for clinical trials lookup."""

    disease_type: str
    location: str = ""
    patient_condition: str = ""

    @validator("disease_type")
    def validate_trial_disease(cls, v: str) -> str:
        allowed_types = ["肺癌", "乳腺癌", "胃癌", "肝癌", "结直肠癌"]
        if v not in allowed_types:
            raise ValueError(f"不支持的疾病类型: {v}")
        return v
