from fastapi import FastAPI

from app.routes.case_routes import router as case_router
from app.routes.hospital_routes import router as hospital_router
from app.routes.ambulance_routes import router as ambulance_router

app = FastAPI(
    title="Emergency Healthcare Decision & Coordination System",
    description="Rule-based emergency classification backend",
    version="1.0.0"
)

# Register routers
app.include_router(case_router)
app.include_router(hospital_router)
app.include_router(ambulance_router)

@app.get("/")
def health_check():
    return {"status": "Backend running successfully"}

