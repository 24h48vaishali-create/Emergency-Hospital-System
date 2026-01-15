from fastapi import APIRouter
from app.schemas.ambulance import AmbulanceRequest, AmbulanceResponse
from app.services.ambulance_service import process_ambulance_request

router = APIRouter(
    prefix="/ambulance",
    tags=["Ambulance"]
)

@router.post("/request", response_model=AmbulanceResponse)
def request_ambulance(request: AmbulanceRequest):
    approved, message = process_ambulance_request(request.case_type)

    return AmbulanceResponse(
        approved=approved,
        message=message
    )
