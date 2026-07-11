from fastapi import APIRouter

from app.schemas.approval_flow import (
    ApprovalFlowCreate,
    ApprovalFlowUpdate,
    ApprovalFlowResponse,
)
from app.services.approval_flow_service import ApprovalFlowService

router = APIRouter()

service = ApprovalFlowService()


@router.get("/", response_model=list[ApprovalFlowResponse])
def get_approval_flows():
    return service.get_all()


@router.get("/{approval_id}", response_model=ApprovalFlowResponse)
def get_approval_flow(approval_id: int):
    return service.get_by_id(approval_id)


@router.post("/")
def create_approval_flow(approval: ApprovalFlowCreate):
    return service.create(approval.model_dump())


@router.put("/{approval_id}")
def update_approval_flow(
    approval_id: int,
    approval: ApprovalFlowUpdate,
):
    return service.update(
        approval_id,
        approval.model_dump(exclude_unset=True),
    )


@router.delete("/{approval_id}")
def delete_approval_flow(approval_id: int):
    return service.delete(approval_id)