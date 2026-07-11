from fastapi import APIRouter

from app.schemas.document_type import (
    DocumentTypeCreate,
    DocumentTypeResponse,
    DocumentTypeUpdate,
)
from app.services.document_type_service import DocumentTypeService

router = APIRouter()

service = DocumentTypeService()


@router.get("/", response_model=list[DocumentTypeResponse])
def get_document_types():
    return service.get_all()


@router.get("/{document_type_id}", response_model=DocumentTypeResponse)
def get_document_type(document_type_id: int):
    return service.get_by_id(document_type_id)


@router.post("/")
def create_document_type(document_type: DocumentTypeCreate):
    return service.create(document_type.model_dump())


@router.put("/{document_type_id}")
def update_document_type(
    document_type_id: int,
    document_type: DocumentTypeUpdate,
):
    return service.update(
        document_type_id,
        document_type.model_dump(exclude_unset=True)
    )


@router.delete("/{document_type_id}")
def delete_document_type(document_type_id: int):
    return service.delete(document_type_id)