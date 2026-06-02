from fastapi import APIRouter
from app.services.ml_service import predict_fraud

router = APIRouter()


@router.post("/predict")
def predict(data: dict):
    result = predict_fraud(data)

    return {
        "status": "success",
        "result": result
    }