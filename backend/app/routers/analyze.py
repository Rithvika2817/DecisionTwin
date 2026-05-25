from fastapi import APIRouter
from app.services.ml_service import get_baseline_metrics

router = APIRouter()


@router.get("/analyze/{dataset_id}")
def analyze_file(dataset_id: int):

    analytics = get_baseline_metrics()

    return {
        "status": "success",
        "dataset_id": dataset_id,
        "message": "Fraud analysis completed",
        "analytics": analytics
    }