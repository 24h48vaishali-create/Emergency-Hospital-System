from fastapi import APIRouter
from typing import List

from app.schemas.hospital import Hospital
from app.schemas.medical_case import MedicalCaseType
from app.services.hospital_service import get_hospitals_by_city
from app.services.hospital_prioritizer import prioritize_hospitals
from app.services.emergency_classifier import classify_case

router = APIRouter(
    prefix="/hospitals",
    tags=["Hospitals"]
)

# -------------------------------
# City-level hospital listing
# -------------------------------
@router.get("/city/{city}", response_model=List[Hospital])
def list_hospitals_by_city(city: str):
    return get_hospitals_by_city(city)

# -------------------------------
# Recommended hospitals endpoint
# -------------------------------
@router.get("/recommended/{city}/{case_type}", response_model=List[Hospital])
def recommended_hospitals(city: str, case_type: MedicalCaseType):
    hospitals = get_hospitals_by_city(city)
    is_emergency = classify_case(case_type)

    return prioritize_hospitals(
        hospitals=hospitals,
        case_type=case_type,
        is_emergency=is_emergency
    )
