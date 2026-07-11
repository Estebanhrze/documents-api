from typing import Optional

from app.schemas.base import BaseSchema


class ApprovalFlowCreate(BaseSchema):
    document_id: int
    version_id: int
    step_order: int
    assigned_to: int
    action: str


class ApprovalFlowUpdate(BaseSchema):
    status: Optional[str] = None
    comments: Optional[str] = None


class ApprovalFlowResponse(BaseSchema):
    id: int
    document_id: int
    version_id: int
    step_order: int
    assigned_to: int
    action: str
    status: str
    comments: Optional[str]