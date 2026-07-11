from typing import Optional

from pydantic import Field

from app.schemas.base import BaseSchema


class RoleCreate(BaseSchema):
    name: str = Field(..., max_length=100)
    description: Optional[str] = None
    permissions: Optional[str] = None
    is_custom: bool = False


class RoleUpdate(BaseSchema):
    name: Optional[str] = None
    description: Optional[str] = None
    permissions: Optional[str] = None
    is_custom: Optional[bool] = None


class RoleResponse(BaseSchema):
    id: int
    name: str
    description: Optional[str]
    permissions: Optional[str]
    is_custom: bool