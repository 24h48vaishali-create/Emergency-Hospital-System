from fastapi import APIRouter
from app.schemas.medical_case import MedicalCaseType
from app.services.first_aid_service import get_first_aid_guidance

router = APIRouter(
    prefix="/first-aid",
    tags=["First Aid"]
)

@router.get("/{case_type}")
def first_aid(case_type: MedicalCaseType):
    return {
        "case_type": case_type,
        "guidance": get_first_aid_guidance(case_type)
    }
