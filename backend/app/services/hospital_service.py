from typing import List
from app.schemas.hospital import Hospital

# Temporary in-memory hospital data (demo/testing)
HOSPITALS: List[Hospital] = [
    Hospital(
        id=1,
        name="City Care Hospital",
        city="Bangalore",
        is_emergency_ready=True,
        available_emergency_beds=5,
        specializations=["cardiac", "trauma"]
    ),
    Hospital(
        id=2,
        name="Green Life Clinic",
        city="Bangalore",
        is_emergency_ready=False,
        available_emergency_beds=0,
        specializations=["general"]
    ),
    Hospital(
        id=3,
        name="Metro Health Center",
        city="Chennai",
        is_emergency_ready=True,
        available_emergency_beds=2,
        specializations=["burns", "emergency"]
    )
]

def get_hospitals_by_city(city: str) -> List[Hospital]:
    """
    Returns hospitals filtered by city (case-insensitive).
    """
    return [h for h in HOSPITALS if h.city.lower() == city.lower()]
