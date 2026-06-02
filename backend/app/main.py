from fastapi import FastAPI

from app.routers import (
    health,
    simulation,
    analyze,
    datasets,
    analytics,
    predict
)

app = FastAPI(title="DecisionTwin API")

# Routes
app.include_router(health.router)
app.include_router(simulation.router)
app.include_router(analyze.router)
app.include_router(datasets.router)
app.include_router(analytics.router)
app.include_router(predict.router)


@app.get("/")
def root():
    return {
        "message": "DecisionTwin Backend Running"
    }