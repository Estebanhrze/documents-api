from fastapi import APIRouter, Depends

from app.core.security import get_current_user
from app.schemas.document import (
    DocumentCreate,
    DocumentResponse,
    DocumentUpdate,
)
from app.services.document_service import DocumentService

router = APIRouter()

service = DocumentService()


@router.get("/", response_model=list[DocumentResponse])
def get_documents():
    return service.get_all()


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: str):
    return service.get_by_id(document_id)


@router.post("/")
def create_document(
    document: DocumentCreate,
    current_user: dict = Depends(get_current_user),
):
    return service.create(document.model_dump())


@router.put("/{document_id}")
def update_document(
    document_id: str,
    document: DocumentUpdate,
    current_user: dict = Depends(get_current_user),
):
    return service.update(
        document_id,
        document.model_dump(exclude_unset=True)
    )


@router.delete("/{document_id}")
def delete_document(
    document_id: str,
    current_user: dict = Depends(get_current_user),
):
    return service.delete(document_id)