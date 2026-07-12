from typing import Optional

from pydantic import EmailStr, Field

from app.schemas.base import BaseSchema


class UserCreate(BaseSchema):
    name: str = Field(..., max_length=150)
    email: EmailStr
    password: str
    role_id: int


class UserUpdate(BaseSchema):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role_id: Optional[int] = None
    mfa_enabled: Optional[bool] = None
    is_active: Optional[bool] = None


class UserResponse(BaseSchema):
    id: str
    name: str
    email: EmailStr
    role_id: int
    mfa_enabled: bool
    is_active: bool