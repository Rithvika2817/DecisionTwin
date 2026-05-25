from fastapi import APIRouter, UploadFile, File
import pandas as pd
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store uploaded datasets
dataset_store = {}


@router.post("/datasets/upload")
async def upload_dataset(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    dataset_id = len(dataset_store) + 1
    dataset_store[dataset_id] = file_path

    return {
        "status": "success",
        "dataset_id": dataset_id,
        "filename": file.filename,
        "message": "Dataset uploaded successfully"
    }


@router.get("/datasets/{dataset_id}/preview")
def preview_dataset(dataset_id: int):

    if dataset_id not in dataset_store:
        return {"error": "Dataset not found"}

    file_path = dataset_store[dataset_id]

    df = pd.read_csv(file_path)

    return {
        "status": "success",
        "dataset_id": dataset_id,
        "columns": list(df.columns),
        "preview": df.head(5).to_dict(orient="records")
    }