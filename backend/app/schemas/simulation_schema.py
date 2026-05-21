from pydantic import BaseModel


class SimulationResult(BaseModel):
    simulation_id: int
    result: str
    score: float