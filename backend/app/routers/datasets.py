from fastapi import APIRouter, UploadFile, File
import os
import shutil

router = APIRouter()

UPLOAD_FOLDER = "uploads"

# Create uploads folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/datasets/upload")
async def upload_dataset(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "status": "success",
        "dataset_id": 1,
        "filename": file.filename,
        "message": "Dataset uploaded successfully"
    }


@router.get("/datasets/{dataset_id}/preview")
async def preview_dataset(dataset_id: int):
    return {
        "status": "success",
        "dataset_id": dataset_id,
        "columns": [
            "Transaction_ID",
            "Amount",
            "Merchant",
            "Risk_Score"
        ],
        "preview": [
            {
                "Transaction_ID": 101,
                "Amount": 5000,
                "Merchant": "Amazon",
                "Risk_Score": "Low"
            },
            {
                "Transaction_ID": 102,
                "Amount": 12000,
                "Merchant": "Flipkart",
                "Risk_Score": "Medium"
            }
        ]
    }