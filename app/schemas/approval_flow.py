from typing import Optional

from app.schemas.base import BaseSchema


class ApprovalFlowCreate(BaseSchema):
    document_id: str
    version_id: str
    step_order: int
    assigned_to: str
    action: str


class ApprovalFlowUpdate(BaseSchema):
    status: Optional[str] = None
    comments: Optional[str] = None


class ApprovalFlowResponse(BaseSchema):
    id: str
    document_id: str
    version_id: str
    step_order: int
    assigned_to: str
    action: str
    status: str
    comments: Optional[str]