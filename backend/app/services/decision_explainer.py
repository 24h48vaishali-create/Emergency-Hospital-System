from app.schemas.medical_case import MedicalCaseType

def explain_decision(case_type: MedicalCaseType, is_emergency: bool) -> str:
    """
    Provides a human-readable explanation for the classification decision.
    """

    if is_emergency:
        return (
            f"The selected case type '{case_type.value}' is classified as an emergency "
            "because it may involve immediate risk to life and requires urgent medical attention."
        )
    else:
        return (
            f"The selected case type '{case_type.value}' is classified as non-emergency "
            "as it typically does not require immediate emergency intervention."
        )
