from fastapi import APIRouter, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import get_current_user
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService

router = APIRouter()
service = AuthService()
http_bearer = HTTPBearer()


@router.post("/login")
def login(credentials: LoginRequest):
    return service.login(credentials.model_dump())


@router.post("/logout")
def logout(
    credentials: HTTPAuthorizationCredentials = Security(http_bearer),
):
    return service.logout(credentials.credentials)


@router.get("/me")
def me(current_user: dict = Depends(get_current_user)):
    return service.me(current_user)