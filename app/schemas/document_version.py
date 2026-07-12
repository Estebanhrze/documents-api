from typing import Optional

from app.schemas.base import BaseSchema


class DocumentVersionCreate(BaseSchema):
    document_id: str
    version_number: str
    file_path: str
    file_format: str
    file_size_kb: Optional[int] = None
    change_summary: Optional[str] = None


class DocumentVersionUpdate(BaseSchema):
    change_summary: Optional[str] = None


class DocumentVersionResponse(BaseSchema):
    id: str
    document_id: str
    version_number: str
    file_path: str
    file_format: str
    file_size_kb: Optional[int]
    change_summary: Optional[str]