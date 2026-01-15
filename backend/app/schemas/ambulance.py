from pydantic import BaseModel
from app.schemas.medical_case import MedicalCaseType

class AmbulanceRequest(BaseModel):
    case_type: MedicalCaseType
    location: str

class AmbulanceResponse(BaseModel):
    approved: bool
    message: str
