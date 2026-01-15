from fastapi import FastAPI

app = FastAPI(
    title="Emergency Healthcare Decision & Coordination System",
    description="Rule-based emergency classification backend",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "Backend running successfully"}
