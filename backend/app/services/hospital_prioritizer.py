from typing import List
from app.schemas.hospital import Hospital
from app.schemas.medical_case import MedicalCaseType

def prioritize_hospitals(
    hospitals: List[Hospital],
    case_type: MedicalCaseType,
    is_emergency: bool
) -> List[Hospital]:
    """
    Sort hospitals based on rule-based priority:
    1. Emergency readiness (if emergency case)
    2. Specialization match
    3. Available emergency beds
    """

    def hospital_priority(hospital: Hospital):
        score = 0

        # Emergency-ready hospitals get higher priority
        if is_emergency and hospital.is_emergency_ready:
            score += 3

        # Specialization match increases priority
        if case_type.value in hospital.specializations:
            score += 2

        # Availability matters
        score += hospital.available_emergency_beds

        return score

    return sorted(hospitals, key=hospital_priority, reverse=True)
