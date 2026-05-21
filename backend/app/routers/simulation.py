from fastapi import APIRouter
from app.schemas.simulation_schema import SimulationResult

router = APIRouter()


@router.get("/simulate/", response_model=SimulationResult)
def run_simulation():
    return SimulationResult(
        simulation_id=1,
        result="Simulation endpoint ready",
        score=85.5
    )