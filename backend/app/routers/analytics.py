from fastapi import APIRouter

router = APIRouter()


@router.get("/analytics/baseline/{dataset_id}")
def baseline_analytics(dataset_id: int):
    return {
        "status": "success",
        "dataset_id": dataset_id,
        "summary": {
            "total_transactions": 2500,
            "fraud_detected": 34,
            "fraud_percentage": "1.36%"
        },
        "risk_distribution": {
            "low_risk": 1800,
            "medium_risk": 550,
            "high_risk": 150
        },
        "prediction": "Fraud Risk: Medium",
        "message": "Baseline analytics endpoint ready"
    }