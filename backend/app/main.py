from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import health, simulation, upload

app = FastAPI(title="DecisionTwin API")

# Routers
app.include_router(health.router)
app.include_router(simulation.router)
app.include_router(upload.router)

# Serve uploaded files
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
def root():
    return {"message": "DecisionTwin Backend Running"}