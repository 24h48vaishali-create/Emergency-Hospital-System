from pydantic import BaseModel
from enum import Enum

class MedicalCaseType(str, Enum):
    cardiac = "cardiac"
    accident = "accident"
    burns = "burns"
    poisoning = "poisoning"
    fever = "fever"
    minor_injury = "minor_injury"

class CaseRequest(BaseModel):
    case_type: MedicalCaseType

class CaseResponse(BaseModel):
    case_type: MedicalCaseType
    is_emergency: bool
    message: str
    explanation: str
