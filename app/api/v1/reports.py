from fastapi import APIRouter, Depends

from app.core.security import get_current_user
from app.services.report_service import ReportService

router = APIRouter()
service = ReportService()


@router.get("/documents")
def documents_report(current_user: dict = Depends(get_current_user)):
    return service.documents_by_status()


@router.get("/pending")
def pending_report(current_user: dict = Depends(get_current_user)):
    return service.pending_approvals()


@router.get("/audit")
def audit_report(current_user: dict = Depends(get_current_user)):
    return service.audit_summary()
