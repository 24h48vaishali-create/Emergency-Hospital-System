from app.schemas.medical_case import MedicalCaseType

# Rule-based emergency cases
EMERGENCY_CASES = {
    MedicalCaseType.cardiac,
    MedicalCaseType.accident,
    MedicalCaseType.burns,
    MedicalCaseType.poisoning,
}

def classify_case(case_type: MedicalCaseType) -> bool:
    """
    Determines whether a medical case is an emergency.
    """
    return case_type in EMERGENCY_CASES
