from fastapi import APIRouter

from app.schemas.document_version import (
    DocumentVersionCreate,
    DocumentVersionUpdate,
    DocumentVersionResponse,
)
from app.services.document_version_service import DocumentVersionService

router = APIRouter()

service = DocumentVersionService()


@router.get("/", response_model=list[DocumentVersionResponse])
def get_versions():
    return service.get_all()


@router.get("/{version_id}", response_model=DocumentVersionResponse)
def get_version(version_id: int):
    return service.get_by_id(version_id)


@router.post("/")
def create_version(version: DocumentVersionCreate):
    return service.create(version.model_dump())


@router.put("/{version_id}")
def update_version(
    version_id: int,
    version: DocumentVersionUpdate,
):
    return service.update(
        version_id,
        version.model_dump(exclude_unset=True),
    )


@router.delete("/{version_id}")
def delete_version(version_id: int):
    return service.delete(version_id)