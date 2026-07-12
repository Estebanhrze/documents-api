from fastapi import APIRouter

from app.schemas.attachment import (
    AttachmentCreate,
    AttachmentUpdate,
    AttachmentResponse,
)
from app.services.attachment_service import AttachmentService

router = APIRouter()

service = AttachmentService()


@router.get("/", response_model=list[AttachmentResponse])
def get_attachments():
    return service.get_all()


@router.get("/{attachment_id}", response_model=AttachmentResponse)
def get_attachment(attachment_id: str):
    return service.get_by_id(attachment_id)


@router.post("/")
def create_attachment(attachment: AttachmentCreate):
    return service.create(attachment.model_dump())


@router.put("/{attachment_id}")
def update_attachment(
    attachment_id: str,
    attachment: AttachmentUpdate,
):
    return service.update(
        attachment_id,
        attachment.model_dump(exclude_unset=True),
    )


@router.delete("/{attachment_id}")
def delete_attachment(attachment_id: str):
    return service.delete(attachment_id)