from typing import Optional

from app.schemas.base import BaseSchema


class AuditLogCreate(BaseSchema):
    user_id: str
    document_id: str
    action: str
    from_status: Optional[str] = None
    to_status: Optional[str] = None
    detail: Optional[str] = None
    ip_address: Optional[str] = None


class AuditLogResponse(BaseSchema):
    id: str
    user_id: str
    document_id: str
    action: str
    from_status: Optional[str]
    to_status: Optional[str]
    detail: Optional[str]
    ip_address: Optional[str]