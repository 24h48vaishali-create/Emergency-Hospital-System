from app.schemas.medical_case import MedicalCaseType
from app.services.emergency_classifier import classify_case

def process_ambulance_request(case_type: MedicalCaseType) -> tuple[bool, str]:
    """
    Allows ambulance dispatch only for emergency cases.
    """

    is_emergency = classify_case(case_type)

    if not is_emergency:
        return (
            False,
            "Ambulance services are restricted to emergency cases only. "
            "Please visit a nearby hospital or clinic."
        )

    return (
        True,
        "Ambulance request approved. Dispatching nearest available ambulance."
    )
