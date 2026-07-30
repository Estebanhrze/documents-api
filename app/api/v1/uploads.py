from fastapi import APIRouter, Depends, File, UploadFile, status

from app.core.security import get_current_user
from app.schemas.upload import UploadResponse
from app.services.storage_service import StorageService

router = APIRouter()
service = StorageService()


@router.post("/", response_model=UploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile = File(..., description="Archivo PDF, DOC, DOCX o TXT de máximo 10 MB."),
    current_user: dict = Depends(get_current_user),
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
