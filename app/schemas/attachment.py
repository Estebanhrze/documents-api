from typing import Optional

from app.schemas.base import BaseSchema


class AttachmentCreate(BaseSchema):
    document_id: str
    version_id: Optional[str] = None
    file_name: str
    file_path: str
    file_type: str


class AttachmentUpdate(BaseSchema):
    file_name: Optional[str] = None
    file_type: Optional[str] = None


class AttachmentResponse(BaseSchema):
    id: str
    document_id: str
    version_id: Optional[str]
    file_name: str
    file_path: str
    file_type: str