from fastapi import APIRouter

from app.schemas.audit_log import (
    AuditLogCreate,
    AuditLogResponse,
)
from app.services.audit_service import AuditService

router = APIRouter()

service = AuditService()


@router.get("/", response_model=list[AuditLogResponse])
def get_audit_logs():
    return service.get_all()


@router.get("/{audit_id}", response_model=AuditLogResponse)
def get_audit_log(audit_id: int):
    return service.get_by_id(audit_id)


@router.post("/")
def create_audit_log(audit: AuditLogCreate):
    return service.create(audit.model_dump())


@router.delete("/{audit_id}")
def delete_audit_log(audit_id: int):
    return service.delete(audit_id)