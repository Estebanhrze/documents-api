from fastapi import APIRouter

from app.schemas.role import (
    RoleCreate,
    RoleResponse,
    RoleUpdate,
)
from app.services.role_service import RoleService

router = APIRouter()

service = RoleService()


@router.get("/", response_model=list[RoleResponse])
def get_roles():
    return service.get_all()


@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int):
    return service.get_by_id(role_id)


@router.post("/")
def create_role(role: RoleCreate):
    return service.create(role.model_dump())


@router.put("/{role_id}")
def update_role(role_id: int, role: RoleUpdate):
    return service.update(role_id, role.model_dump(exclude_unset=True))


@router.delete("/{role_id}")
def delete_role(role_id: int):
    return service.delete(role_id)