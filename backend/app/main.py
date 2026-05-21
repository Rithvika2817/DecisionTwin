from fastapi import FastAPI
from app.routers import health, simulation, upload, analyze

app = FastAPI(title="DecisionTwin API")

# Routers
app.include_router(health.router)
app.include_router(simulation.router)
app.include_router(upload.router)
app.include_router(analyze.router)

@app.get("/")
def root():
    return {"message": "DecisionTwin Backend Running"}