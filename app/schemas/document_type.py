from typing import Optional

from app.schemas.base import BaseSchema


class DocumentTypeCreate(BaseSchema):
    name: str
    description: Optional[str] = None


class DocumentTypeUpdate(BaseSchema):
    name: Optional[str] = None
    description: Optional[str] = None


class DocumentTypeResponse(BaseSchema):
    id: int
    name: str
    description: Optional[str]