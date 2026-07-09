from fastapi import APIRouter

from app.api.v1 import (
    auth,
    document_types,
    users,
    roles,
    documents,
    versions,
    attachments,
    approvals,
    audit,
)

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(roles.router, prefix="/roles", tags=["Roles"])
api_router.include_router(documents.router, prefix="/documents", tags=["Documents"])
api_router.include_router(document_types.router, prefix="/document_types", tags=["Document Types"])
api_router.include_router(versions.router, prefix="/versions", tags=["Versions"])
api_router.include_router(attachments.router, prefix="/attachments", tags=["Attachments"])
api_router.include_router(approvals.router, prefix="/approvals", tags=["Approvals"])
api_router.include_router(audit.router, prefix="/audit", tags=["Audit"])