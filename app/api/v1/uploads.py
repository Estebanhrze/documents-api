from fastapi import APIRouter, Depends, File, Query, UploadFile, status

from app.core.security import get_upload_user
from app.schemas.upload import SignedUrlResponse, UploadResponse
from app.services.storage_service import StorageService

router = APIRouter()
service = StorageService()


@router.get("/signed-url", response_model=SignedUrlResponse)
def create_signed_download_url(
    file_path: str = Query(min_length=1),
    _current_user: dict = Depends(get_upload_user),
):
    return {"signed_url": service.create_signed_url(file_path=file_path)}


@router.post("/", response_model=UploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile = File(..., description="Archivo PDF, DOC, DOCX o TXT de máximo 10 MB."),
    current_user: dict = Depends(get_upload_user),
):
    content = await file.read()
    try:
        return service.upload(
            original_name=file.filename or "archivo",
            content_type=file.content_type,
            content=content,
            user_id=current_user["id"],
        )
    finally:
        await file.close()