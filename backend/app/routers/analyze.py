from fastapi import APIRouter

router = APIRouter()

@router.get("/analyze/")
def analyze_file():
    return {
        "status": "success",
        "message": "Analysis endpoint ready",
        "prediction": "Fraud Risk: Low"
    }