from typing import Optional

from app.schemas.base import BaseSchema


class DocumentCreate(BaseSchema):
    doc_number: str
    title: str
    classification: Optional[str] = None
    document_type_id: int
    created_by: str


class DocumentUpdate(BaseSchema):
    title: Optional[str] = None
    classification: Optional[str] = None
    current_status: Optional[str] = None


class DocumentResponse(BaseSchema):
    id: str
    doc_number: str
    title: str
    classification: Optional[str]
    current_status: str
    document_type_id: int
    created_by: str