from pydantic import BaseModel
from typing import List

class Hospital(BaseModel):
    id: int
    name: str
    city: str
    is_emergency_ready: bool
    available_emergency_beds: int
    specializations: List[str]
