from fastapi import APIRouter

from app.api.v1 import (
    approval_flows,
    attachments,
    audit,
    auth,
    documents,
    document_types,
    document_versions,
    reports,
    roles,
    uploads,
    users,
)

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(roles.router, prefix="/roles", tags=["Roles"])
api_router.include_router(documents.router, prefix="/documents", tags=["Documents"])
api_router.include_router(document_types.router, prefix="/document-types", tags=["Document Types"])
api_router.include_router(document_versions.router, prefix="/document-versions", tags=["Document Versions"])
api_router.include_router(attachments.router, prefix="/attachments", tags=["Attachments"])
api_router.include_router(uploads.router, prefix="/uploads", tags=["Uploads"])
api_router.include_router(approval_flows.router, prefix="/approval-flows", tags=["Approval flows"])
api_router.include_router(audit.router, prefix="/audit", tags=["Audit"])
api_router.include_router(reports.router, prefix="/reports", tags=["Reports"])
