from fastapi import APIRouter

router = APIRouter(prefix="/simulate", tags=["Simulation"])

@router.get("/")
def run_simulation():
    return {
        "message": "Simulation endpoint ready",
        "status": "waiting for ML integration"
    }