from math import ceil
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, status

from app.core.config import settings
from app.core.database import supabase_storage


class StorageService:
    """Stores document binaries in Supabase Storage and returns stable paths."""

    allowed_extensions = {".pdf", ".doc", ".docx", ".txt"}

    def upload(
        self,
        *,
        original_name: str,
        content_type: str | None,
        content: bytes,
        user_id: str,
    ) -> dict:
        extension = Path(original_name).suffix.lower()
        if extension not in self.allowed_extensions:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Formato no permitido. Use PDF, DOC, DOCX o TXT.",
            )

        max_size = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
        if not content:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El archivo está vacío.",
            )
        if len(content) > max_size:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El archivo no puede superar {settings.MAX_UPLOAD_SIZE_MB} MB.",
            )

        file_path = f"documents/{user_id}/{uuid4().hex}{extension}"
        resolved_content_type = content_type or "application/octet-stream"

        try:
            supabase_storage.storage.from_(settings.SUPABASE_STORAGE_BUCKET).upload(
                path=file_path,
                file=content,
                file_options={
                    "content-type": resolved_content_type,
                    "upsert": "false",
                },
            )
        except Exception as exc:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail="No fue posible guardar el archivo en el almacenamiento remoto.",
            ) from exc

        return {
            "file_path": file_path,
            "file_name": original_name,
            "file_type": resolved_content_type,
            "file_size_kb": ceil(len(content) / 1024),
        }
