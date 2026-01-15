from app.schemas.medical_case import MedicalCaseType

FIRST_AID_GUIDE = {
    MedicalCaseType.cardiac: (
        "Call emergency services immediately. "
        "If trained, begin CPR and keep the patient calm and still."
    ),
    MedicalCaseType.accident: (
        "Ensure the area is safe. Do not move the injured person unless necessary. "
        "Control bleeding using clean cloth or bandage."
    ),
    MedicalCaseType.burns: (
        "Cool the burn under running water for at least 10 minutes. "
        "Do not apply ice, oils, or creams."
    ),
    MedicalCaseType.poisoning: (
        "Do not induce vomiting. Keep the patient calm and seek medical help immediately."
    ),
    MedicalCaseType.fever: (
        "Ensure hydration and rest. Monitor temperature and consult a doctor if fever persists."
    ),
    MedicalCaseType.minor_injury: (
        "Clean the wound with water, apply antiseptic, and cover with a clean bandage."
    ),
}

def get_first_aid_guidance(case_type: MedicalCaseType) -> str:
    """
    Returns first-aid guidance based on case type.
    """
    return FIRST_AID_GUIDE.get(
        case_type,
        "Please seek medical assistance for further guidance."
    )
