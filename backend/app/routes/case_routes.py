from fastapi import APIRouter
from app.schemas.medical_case import CaseRequest, CaseResponse
from app.services.emergency_classifier import classify_case

router = APIRouter(
    prefix="/case",
    tags=["Medical Case"]
)

@router.post("/classify", response_model=CaseResponse)
def classify_medical_case(request: CaseRequest):
    is_emergency = classify_case(request.case_type)

    message = (
        "This case is classified as an emergency."
        if is_emergency
        else "This case is classified as non-emergency."
    )

    return CaseResponse(
        case_type=request.case_type,
        is_emergency=is_emergency,
        message=message
    )
