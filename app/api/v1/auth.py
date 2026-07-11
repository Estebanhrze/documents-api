from fastapi import APIRouter

from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService

router = APIRouter()

service = AuthService()


@router.post("/login")
def login(credentials: LoginRequest):
    return service.login(credentials.model_dump())


@router.post("/logout")
def logout():
    return service.logout()


@router.get("/me")
def me():
    return service.me()