from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter(tags=["Upload"])

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "preview_url": f"/uploads/{file.filename}"
    }