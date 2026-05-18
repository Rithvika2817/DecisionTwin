from fastapi import FastAPI
from app.routers import health, simulation

app = FastAPI(title="DecisionTwin API")

app.include_router(health.router)
app.include_router(simulation.router)

@app.get("/")
def root():
    return {"message": "DecisionTwin Backend Running"}