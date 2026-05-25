from fastapi import APIRouter
from app.services.ml_service import get_baseline_metrics

router = APIRouter()

@router.get("/analytics/baseline/{dataset_id}")
def baseline_analytics(dataset_id: int):

    analytics = get_baseline_metrics()

    return {
        "status": "success",
        "dataset_id": dataset_id,
        "analytics": analytics
    }